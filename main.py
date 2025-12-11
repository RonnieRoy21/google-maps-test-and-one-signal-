from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv
import os
load_dotenv()
appId=os.getenv('ONESIGNAL_APP_ID')
appRestKey=os.getenv('ONESIGNAL_APP_REST_KEY')
appUrl=os.getenv('ONESIGNAL_APP_URL')
app = FastAPI(title="OneSignal Notifications for MealMind Database")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
)

@app.post('/orderAdded')
async def orderAdded(request:Request):
            order=await request.json()
            print(f'order received : {order}')
            print(f'{order.get("records")}')

            return order

