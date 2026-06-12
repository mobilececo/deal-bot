import requests

TOKEN = "BOTFATHER_TOKEN"

def send(chat_id, msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    r = requests.post(url, data={
        "chat_id": chat_id,
        "text": msg
    })

    print("STATUS:", r.status_code)
    print("RESPONSE:", r.text)
