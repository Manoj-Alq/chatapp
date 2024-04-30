from fastapi.exceptions import HTTPException
from fastapi import FastAPI, WebSocket

class ConnectionManager:
    # initialize list for websockets connections
    def __init__(self):
        self.active_rooms: dict = {}

    # accept and append the connection to the list
    async def connect(self, websocket: WebSocket, name: str):
        await websocket.accept()

        # Append the websocket to the list
        if name not in self.active_rooms:
            self.active_rooms[name] = websocket  
            print(self.active_rooms)

    # remove the connection from list
    def disconnect(self, websocket: WebSocket):
        for room_id, connections in self.active_rooms.items():
            if websocket in connections:
                connections.remove(websocket)   
                if not connections:  # If no more connections in the room, remove the room
                    del self.active_rooms[room_id]
                break

    # send personal message to the connection
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    # send message to the list of connections
    async def broadcast(self, message: str,room_id:int, websocket: WebSocket):
        for connection in self.active_rooms[room_id]:
            if (connection == websocket):
                continue
            await connection.send_text(message)

def response_handler(status_code, message, success) -> dict:
    return {"status": status_code,"success": success,"message": message}

def error_handler(status_code, message) -> dict:
    raise HTTPException(status_code=status_code, detail=message)