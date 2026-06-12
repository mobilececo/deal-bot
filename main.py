from parsers import hepsiburada, trendyol, amazon, n11, itopya,
from db import get_price, save
from bot import send

CHAT_ID = "5160280399"

CATEGORIES = ["laptop", "telefon", "kulaklık", "monitör" "mouse" "klavye" "ayakkabı" "gaming pc"]


def process(products):
    for p in products:

        old_price = get_price(p["id"])

        # ilk kez görülüyorsa kaydet
        if old_price is None:
            save(p["id"], p["title"], p["price"], p["site"])
            continue

        # fiyat düştüyse
        if p["price"] < old_price:

            drop = int(((old_price - p["price"]) / old_price) * 100)

            send(CHAT_ID, f"""
🔥 FİYAT DÜŞTÜ!

🏪 {p['site']}
🛒 {p['title']}
💰 Eski: {old_price}
💸 Yeni: {p['price']}
📉 %{drop}
""")


        save(p["id"], p["title"], p["price"], p["site"])


def run():

    for cat in CATEGORIES:

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


if __name__ == "__main__":
    run()
