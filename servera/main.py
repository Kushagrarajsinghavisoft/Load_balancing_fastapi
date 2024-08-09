import httpx
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(main())

async def send_request():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://nginx/backend")
        print(response.json())

async def main():
    tasks = [send_request() for _ in range(10)]
    await asyncio.gather(*tasks)

@app.get('/')
async def read_root():
    return {"message": "This is server A"}
