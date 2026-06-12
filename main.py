import requests

# =====================
# TELEGRAM AYARLARI
# =====================
TOKEN = "8755949106:AAFSBlPuPKkUj0y2n-T-R7WvfqB9pCwNLw0"
CHAT_ID = "5160280399"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    r = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

    print("STATUS:", r.status_code)
    print("RESPONSE:", r.text)


# =====================
# AYARLAR
# =====================
CATEGORIES = [
    "laptop",
    "telefon",
    "kulaklık",
    "mouse",
    "klavye",
    "monitör"
]

MIN_DISCOUNT = 40


# =====================
# FAKE PRODUCT DATA
# =====================
def get_products(category):
    return [
        {
            "site": "demo-shop",
            "title": f"{category} Gaming Pro",
            "price": 1200,
            "old_price": 1800
        },
        {
            "site": "demo-shop",
            "title": f"{category} Basic Model",
            "price": 900,
            "old_price": 1000
        }
    ]


# =====================
# İNDİRİM HESABI
# =====================
def discount(p):
    return int((p["old_price"] - p["price"]) / p["old_price"] * 100)


# =====================
# BOT RUN
# =====================
def run():

    print("BOT STARTED")
    send("🔥 BOT BAŞLADI")

    for cat in CATEGORIES:

        print("CATEGORY:", cat)

        products = get_products(cat)

        for p in products:

            d = discount(p)

            if d < MIN_DISCOUNT:
                continue

            msg = f"""🔥 FİYAT DÜŞTÜ

🏪 {p['site']}
📦 {p['title']}
💰 {p['price']} TL
📉 %{d} indirim
"""

            send(msg)


# =====================
# ENTRY POINT
# =====================
if __name__ == "__main__":
    run()
