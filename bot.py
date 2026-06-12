import requests

TOKEN = "7756549139:AAHiBgFspGrKGbbnir0tNPx6DtGM_baRjX0"

def send(chat_id, msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": chat_id, "text": msg}
    )
