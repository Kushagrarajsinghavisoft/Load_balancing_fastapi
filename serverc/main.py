from fastapi import FastAPI

app = FastAPI()

@app.get('/backend')
async def home():
    return {"message": "This is server C"}
