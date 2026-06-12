import requests
from bs4 import BeautifulSoup
import re

def parse(query):
    url = f"https://www.n11.com/arama?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    products = []

    # N11 genelde product-item structure kullanır ama değişebilir
    cards = soup.find_all("li", class_="column")

    for c in cards:
        text = c.get_text(" ", strip=True)

        if len(text) < 50:
            continue

        price = re.findall(r"(\d[\d\.\,]*)\s?TL", text)
        if not price:
            continue

        price = int(price[0].replace(".", "").replace(",", ""))

        products.append({
            "id": str(hash(text)),
            "title": text[:120],
            "price": price,
            "site": "n11"
        })

    return products
