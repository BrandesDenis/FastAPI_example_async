import uvicorn
from fastapi import FastAPI

from database import database
from routes import notes


app = FastAPI()
app.include_router(notes.router, prefix='/notes')


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
