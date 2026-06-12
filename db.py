import sqlite3

conn = sqlite3.connect("prices.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS products (
    id TEXT PRIMARY KEY,
    title TEXT,
    last_price REAL,
    site TEXT
)
""")

conn.commit()


def get_price(pid):
    c.execute("SELECT last_price FROM products WHERE id=?", (pid,))
    row = c.fetchone()
    return row[0] if row else None


def save(pid, title, price, site):
    if get_price(pid) is None:
        c.execute(
            "INSERT INTO products VALUES (?,?,?,?)",
            (pid, title, price, site)
        )
    else:
        c.execute(
            "UPDATE products SET last_price=? WHERE id=?",
            (price, pid)
        )

    conn.commit()
