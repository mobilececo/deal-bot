from bot import send
from parsers import hepsiburada, trendyol, amazon, n11, itopya

CHAT_ID = "5160280399"

CATEGORIES = [
    "laptop",
    "telefon",
    "kulaklık",
    "mouse",
    "klavye",
    "monitör",
    "ayakkabı",
    "elektrikli mutfak",
    "gaming pc"
]
def run():

    send(CHAT_ID, "🔥 BOT BAŞLADI")

    for cat in CATEGORIES:

        try:
            hb = hepsiburada.parse(cat)
            tr = trendyol.parse(cat)
            am = amazon.parse(cat)
            n1 = n11.parse(cat)
            it = itopya.parse(cat)

            for product in hb + tr + am + n1 + it:

                msg = f"""🔥 DEAL

🏪 {product['site']}
📦 {product['title']}
💰 {product['price']} TL
"""

                send(CHAT_ID, msg)

        except Exception as e:
            send(CHAT_ID, f"ERROR: {e}")
          def run():
print("FILE STARTED")

def run():
    print("RUN CALLED")

if __name__ == "__main__":
    print("ENTRYPOINT OK")
    run()
