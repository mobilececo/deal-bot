import requests
from bs4 import BeautifulSoup
import re

def parse(query):
    url = f"https://www.amazon.com.tr/s?k={query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-Language": "tr-TR,tr;q=0.9,en;q=0.8"
    }

    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    products = []

    # Amazon kart yapısı (en yaygın selector)
    cards = soup.find_all("div", {"data-component-type": "s-search-result"})

    for c in cards:

        title_tag = c.find("span", class_="a-text-normal")
        price_tag = c.find("span", class_="a-price-whole")

        if not title_tag or not price_tag:
            continue

        title = title_tag.get_text(strip=True)
        price_text = price_tag.get_text(strip=True)

        price_text = price_text.replace(".", "").replace(",", "")
        if not price_text.isdigit():
            continue

        price = int(price_text)

        pid = str(hash(title))

        products.append({
            "id": pid,
            "title": title,
            "price": price,
            "site": "amazon"
        })

    return products
