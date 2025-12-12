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



@app.post("/orderAdded")
async def handle_db_event(request: Request):
    payload = await request.json()

    # Paste this if you want to see the structure
    print("DB Event:", payload)

    record = payload.get("record", {})

    user_id = record.get("userId")
    send_low_stock_notification(user_id)

    return {"status": "ok"}


def send_low_stock_notification(user_id):
    url = "https://api.onesignal.com/notifications"

    body = {
        "app_id": appId,
        "include_external_user_ids": [str(user_id)],
        "contents": {"en": f"New Order Placed ."},
    }

    headers = {
        "Authorization": f"Basic {appRestKey}",
        "Content-Type": "application/json",
    }

    res = requests.post(url, json=body, headers=headers)
    print("OneSignal Response:", res.json())


