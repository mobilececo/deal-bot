import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36"
}

# ----------------------------
# KATEGORİLER
# ----------------------------
CATEGORIES = {
    "ayakkabi": "koşu ayakkabı",
    "telefon": "akıllı telefon",
    "laptop": "laptop",
    "monitör": "monitör",
    "kulaklik": "bluetooth kulaklık",
    "mouse": "gaming mouse"
}

# ----------------------------
# TRENDYOL
# ----------------------------
def trendyol(q):
    url = f"https://www.trendyol.com/sr?q={q}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    items = soup.select("div.p-card-wrppr")
    res = []

    for i in items[:8]:
        try:
            title = i.select_one("span.prdct-desc-cntnr-name").text.strip()
            price = i.select_one("div.prc-box-dscntd").text.strip()
            link = "https://www.trendyol.com" + i.a["href"]
            res.append(("Trendyol", title, price, link))
        except:
            continue

    return res


# ----------------------------
# HEPSIBURADA
# ----------------------------
def hepsiburada(q):
    url = f"https://www.hepsiburada.com/ara?q={q}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    items = soup.select("li.productListContent-item")
    res = []

    for i in items[:8]:
        try:
            title = i.select_one("h3").text.strip()
            price = i.select_one("div.price-value").text.strip()
            link = "https://www.hepsiburada.com" + i.a["href"]
            res.append(("Hepsiburada", title, price, link))
        except:
            continue

    return res


# ----------------------------
# N11
# ----------------------------
def n11(q):
    url = f"https://www.n11.com/arama?q={q}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    items = soup.select("li.column")
    res = []

    for i in items[:6]:
        try:
            title = i.select_one("h3").text.strip()
            price = i.select_one(".newPrice ins").text.strip()
            link = i.a["href"]
            res.append(("n11", title, price, link))
        except:
            continue

    return res


# ----------------------------
# ITOPYA
# ----------------------------
def itopya(q):
    url = f"https://www.itopya.com/arama?q={q}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    items = soup.select("div.product-item")
    res = []

    for i in items[:6]:
        try:
            title = i.select_one("a").get("title")
            price = i.select_one(".price").text.strip()
            link = "https://www.itopya.com" + i.a["href"]
            res.append(("İtopya", title, price, link))
        except:
            continue

    return res


# ----------------------------
# AMAZON (çoğu zaman sınırlı)
# ----------------------------
def amazon(q):
    url = f"https://www.amazon.com.tr/s?k={q}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    items = soup.select("div.s-result-item")
    res = []

    for i in items[:5]:
        try:
            title = i.select_one("h2 span")
            price = i.select_one(".a-price-whole")
            link = i.select_one("a.a-link-normal")

            if not title or not price or not link:
                continue

            res.append((
                "Amazon",
                title.text.strip(),
                price.text.strip(),
                "https://www.amazon.com.tr" + link["href"]
            ))
        except:
            continue

    return res


# ----------------------------
# ANA ARAMA
# ----------------------------
def search(category_key):
    if category_key not in CATEGORIES:
        print("❌ Geçersiz kategori")
        return

    query = CATEGORIES[category_key]

    print(f"\n🔎 Arama: {query}\n")

    all_results = []

    for fn in [trendyol, hepsiburada, n11, itopya, amazon]:
        try:
            all_results += fn(query)
        except Exception as e:
            print(f"⚠️ Hata ({fn.__name__}): {e}")

    if not all_results:
        print("❌ Ürün bulunamadı (site engeli olabilir)")
        return

    for i, (site, title, price, link) in enumerate(all_results, 1):
        print(f"{i}. [{site}] {title}")
        print(f"   💰 {price}")
        print(f"   🔗 {link}\n")


# ----------------------------
# RUN
# ----------------------------
if __name__ == "__main__":
    print("📦 Kategoriler:")
    for k in CATEGORIES:
        print("-", k)

    cat = input("\nKategori seç: ").strip().lower()
    search(cat)
