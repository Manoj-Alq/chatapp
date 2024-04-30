from configuration.config import *
import uvicorn
from api.user.user_router import router as user_router
from api.chat.chat_router import router as chat_router

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(chat_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost",port=5001, reload=True)