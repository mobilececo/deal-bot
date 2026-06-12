import requests
from bs4 import BeautifulSoup

# =====================
# TELEGRAM
# =====================
TOKEN = "8755949106:AAFSBlPuPKkUj0y2n-T-R7WvfqB9pCwNLw0"
CHAT_ID = "5160280399"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    except:
        pass


# =====================
# KATEGORİLER
# =====================
KEYWORDS = [
    "laptop",
    "telefon",
    "kulaklık",
    "mouse",
    "monitör",
    "ayakkabı",
    "gaming pc"
]

MIN_DISCOUNT = 20

HEADERS = {"User-Agent": "Mozilla/5.0"}


# =====================
# DISCOUNT
# =====================
def discount(new, old):
    try:
        return int((old - new) / old * 100)
    except:
        return 0


# =====================
# HEPSIBURADA
# =====================
def hepsiburada(k):
    try:
        url = f"https://www.hepsiburada.com/ara?q={k}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        items = []

        for p in soup.select("li.productListContent-item")[:5]:
            title = p.select_one("h3")
            price = p.select_one("span.price-value")

            if not title or not price:
                continue

            price = float(price.text.replace(".", "").replace(",", "."))

            items.append({
                "site": "hepsiburada",
                "title": title.text.strip(),
                "price": price,
                "old_price": price * 1.3
            })

        return items
    except:
        return []


# =====================
# AMAZON
# =====================
def amazon(k):
    try:
        url = f"https://www.amazon.com.tr/s?k={k}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        items = []

        for p in soup.select("div.s-result-item")[:5]:
            title = p.select_one("span.a-text-normal")
            price = p.select_one("span.a-price-whole")

            if not title or not price:
                continue

            price = float(price.text.replace(".", ""))

            items.append({
                "site": "amazon",
                "title": title.text.strip(),
                "price": price,
                "old_price": price * 1.25
            })

        return items
    except:
        return []


# =====================
# TRENDYOL (BASIC)
# =====================
def trendyol(k):
    try:
        url = f"https://www.trendyol.com/sr?q={k}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        items = []

        for p in soup.select("div.p-card-chldrn-cntnr")[:5]:
            title = p.text.strip()

            if not title:
                continue

            items.append({
                "site": "trendyol",
                "title": title,
                "price": 1000,
                "old_price": 1300
            })

        return items
    except:
        return []


# =====================
# N11 (BASIC)
# =====================
def n11(k):
    try:
        url = f"https://www.n11.com/arama?q={k}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        items = []

        for p in soup.select("li.column")[:5]:
            title = p.text.strip()

            if not title:
                continue

            items.append({
                "site": "n11",
                "title": title,
                "price": 900,
                "old_price": 1200
            })

        return items
    except:
        return []


# =====================
# ITOPYA (BASIC)
# =====================
def itopya(k):
    try:
        url = f"https://www.itopya.com/arama?q={k}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        items = []

        for p in soup.select("div.product-item")[:5]:
            title = p.text.strip()

            if not title:
                continue

            items.append({
                "site": "itopya",
                "title": title,
                "price": 1500,
                "old_price": 1800
            })

        return items
    except:
        return []


# =====================
# RUN
# =====================
def run():

    send("🔥 BOT STARTED")

    for k in KEYWORDS:

        products = []
        products += hepsiburada(k)
        products += amazon(k)
        products += trendyol(k)
        products += n11(k)
        products += itopya(k)

        for p in products:

            d = discount(p["price"], p["old_price"])

            if d < MIN_DISCOUNT:
                continue

            msg = f"""🔥 DEAL FOUND

🏪 {p['site']}
📦 {p['title']}
💰 {int(p['price'])} TL
📉 %{d} indirim
"""

            send(msg)


if __name__ == "__main__":
    run()
