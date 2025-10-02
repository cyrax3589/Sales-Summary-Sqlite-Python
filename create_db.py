import sqlite3

conn = sqlite3.connect("sales_data.db")
cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# sample data
rows = [
    ("2025-09-01", "T-shirt", 10, 299.0),
    ("2025-09-02", "T-shirt", 5, 299.0),
    ("2025-09-03", "Jeans", 4, 999.0),
    ("2025-09-03", "Sneakers", 2, 2499.0),
    ("2025-09-04", "Jeans", 1, 999.0),
    ("2025-09-05", "Cap", 20, 199.0),
    ("2025-09-06", "Sneakers", 1, 2499.0),
    ("2025-09-07", "Cap", 5, 199.0),
]

cur.executemany("INSERT INTO sales (date, product, quantity, price) VALUES (?, ?, ?, ?)", rows)
conn.commit()
conn.close()
print("sales_data.db created with sample data.")
