import requests
from bs4 import BeautifulSoup
import re

def parse(query):
    url = f"https://www.itopya.com/arama?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    products = []

    # İtopya genelde product box yapısı kullanır
    cards = soup.find_all("div")

    for c in cards:
        text = c.get_text(" ", strip=True)

        if len(text) < 60:
            continue

        if "TL" not in text:
            continue

        price = re.findall(r"(\d[\d\.\,]*)\s?TL", text)
        if not price:
            continue

        price = int(price[0].replace(".", "").replace(",", ""))

        products.append({
            "id": str(hash(text)),
            "title": text[:120],
            "price": price,
            "site": "itopya"
        })

    return products
