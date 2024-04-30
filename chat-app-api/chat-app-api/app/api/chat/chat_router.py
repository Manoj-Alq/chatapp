from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from utils.handlers import ConnectionManager
from .chat_controller import *

router = APIRouter()

# instance for hndling and dealing with the websocket connections
connectionmanager = ConnectionManager()

@app.websocket("/send_message/{name}")
async def websocket_endpoint(websocket: WebSocket,name:str):
    # accept connections
    await connectionmanager.connect(websocket, name)
    try:
        while True:
            # receive text from the user
            receiver_name = await websocket.receive_text()
            data = await websocket.receive_text()
            if name in connectionmanager.active_rooms:
                user = connectionmanager.active_rooms[receiver_name]
            else:
                await websocket.send_text("receiver not found")
                
            await connectionmanager.send_personal_message(f"You : {data}", user )
            # broadcast message to the connected user
            # await connectionmanager.broadcast(f"Client #{room_id}: {data}",room_id, websocket)
    except Exception as e:
        print(e)
        websocket.send_text(f"Error: {e}")

    # WebSocketDisconnect exception will be raised when client is disconnected
    except WebSocketDisconnect as e:
        connectionmanager.disconnect(websocket)
        # Broadcast a message indicating that the client has left the chat
        for room_id, connections in connectionmanager.active_rooms.items():
            if websocket in connections:
                await connectionmanager.broadcast(f"Client #{room_id} left the chat", room_id, websocket)
                break

