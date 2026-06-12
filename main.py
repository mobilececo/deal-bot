import hashlib
from parsers import hepsiburada, trendyol, amazon, n11, itopya
from bot import send

CHAT_ID = "5160280399"  # 👈 kendi Telegram user ID

# 🔁 bellekte duplicate engel
seen = set()

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


def make_id(text, site):
    return hashlib.md5((text + site).encode()).hexdigest()


def process(products):
    for p in products:

        pid = make_id(p["title"], p["site"])

        if pid in seen:
            continue

        seen.add(pid)

        msg = f"""🔥 DEAL FOUND

🏪 {p['site']}
📦 {p['title'][:100]}
💰 {p['price']} TL
"""

        send(CHAT_ID, msg)


def run():

    for cat in CATEGORIES:

        try:
            hb = hepsiburada.parse(cat)
            tr = trendyol.parse(cat)
            am = amazon.parse(cat)
            n1 = n11.parse(cat)
            it = itopya.parse(cat)

            process(hb)
            process(tr)
            process(am)
            process(n1)
            process(it)

        except Exception as e:
            print("ERROR:", e)


if __name__ == "__main__":
    run()

send(CHAT_ID, "🔥 BOT ÇALIŞIYOR TEST")
