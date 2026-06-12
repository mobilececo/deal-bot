import requests
from bs4 import BeautifulSoup
import re

def parse(query):
    url = f"https://www.trendyol.com/sr?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    products = []

    for item in soup.find_all("div"):
        text = item.get_text(" ", strip=True)

        if len(text) < 60:
            continue

        price = re.findall(r"(\d[\d\.\,]*)\s?TL", text)
        if not price:
            continue

        price = int(price[0].replace(".", ""))

        pid = str(hash(text))

        products.append({
            "id": pid,
            "title": text[:100],
            "price": price,
            "site": "trendyol"
        })

    return products
