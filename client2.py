import asyncio
import websockets

async def send_message():
    async with websockets.connect('ws://localhost:5001/ws/2/1') as websocket:
        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            await websocket.send(message)

async def receive_message():
    async with websockets.connect('ws://localhost:5001/ws/2/1') as websocket:
        while True:
            message = await websocket.recv()
            print("Received message:", message)

async def main():
    send_task = asyncio.create_task(send_message())
    receive_task = asyncio.create_task(receive_message())
    await asyncio.gather(send_task, receive_task)

asyncio.run(main())
