import requests

TOKEN = "8755949106:AAFSBlPuPKkUj0y2n-T-R7WvfqB9pCwNLw0"

def send(chat_id, msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    r = requests.post(url, data={
        "chat_id": chat_id,
        "text": msg
    })

    print("STATUS:", r.status_code)
    print("RESPONSE:", r.text)
