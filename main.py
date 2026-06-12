from bot import send

CHAT_ID = "5160280399"

def run():
    print("BOT STARTED")

    send(CHAT_ID, "🔥 BOT ÇALIŞTI")

    for i in range(3):
        send(CHAT_ID, f"test mesaj {i}")


if __name__ == "__main__":
    run()
