import requests
from bs4 import BeautifulSoup

TOKEN = "8755949106:AAFSBlPuPKkUj0y2n-T-R7WvfqB9pCwNLw0"
CHAT_ID = "5160280399"

KEYWORDS = [
    "laptop",
    "telefon",
    "kulaklık",
    "mouse",
    "monitör",
    "ayakkabı",
    "gaming pc"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

MIN_DISCOUNT = 20


def send(msg):
    try:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": msg[:4000]
            },
            timeout=15
        )
    except Exception as e:
        print("Telegram hata:", e)


def discount(new_price, old_price):
    try:
        return int((old_price - new_price) / old_price * 100)
    except:
        return 0


def hepsiburada(keyword):
    try:
        url = f"https://www.hepsiburada.com/ara?q={keyword}"
        r = requests.get(url, headers=HEADERS, timeout=15)
        print("STATUS:", r.status_code)
print("URL:", r.url)
print(r.text[:500])

        print("HB:", keyword, r.status_code)

        soup = BeautifulSoup(r.text, "html.parser")

        items = []

        for p in soup.select("li")[:20]:

            text = p.get_text(" ", strip=True)

            if len(text) < 20:
                continue

            items.append({
                "site": "Hepsiburada",
                "title": text[:120],
                "price": 1000,
                "old_price": 1300
            })

        return items[:5]

    except Exception as e:
        print("HB HATA:", e)
        return []


def amazon(keyword):
    try:
        url = f"https://www.amazon.com.tr/s?k={keyword}"
        r = requests.get(url, headers=HEADERS, timeout=15)

        print("AMAZON:", keyword, r.status_code)

        soup = BeautifulSoup(r.text, "html.parser")

        items = []

        for p in soup.select("div.s-result-item")[:10]:

            title = p.get_text(" ", strip=True)

            if len(title) < 20:
                continue

            items.append({
                "site": "Amazon",
                "title": title[:120],
                "price": 1000,
                "old_price": 1300
            })

        return items

    except Exception as e:
        print("AMAZON HATA:", e)
        return []


def trendyol(keyword):
    return []


def n11(keyword):
    return []


def itopya(keyword):
    return []


def run():

    send("🔥 BOT BAŞLADI")

    for keyword in KEYWORDS:

        products = []

        products += hepsiburada(keyword)
        products += amazon(keyword)
        products += trendyol(keyword)
        products += n11(keyword)
        products += itopya(keyword)

        send(f"🔍 {keyword}: {len(products)} ürün bulundu")

        for p in products:

            d = discount(p["price"], p["old_price"])

            if d < MIN_DISCOUNT:
                continue

            msg = (
                f"🔥 DEAL FOUND\n\n"
                f"🏪 {p['site']}\n"
                f"📦 {p['title']}\n"
                f"💰 {p['price']} TL\n"
                f"📉 %{d} indirim"
            )

            send(msg)


if __name__ == "__main__":
    run()
