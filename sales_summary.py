import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "sales_data.db"

def run_queries():
    conn = sqlite3.connect(DB_PATH)

    # Total quantity & revenue per product
    query_group = """
    SELECT
      product,
      SUM(quantity) AS total_qty,
      SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC;
    """
    df = pd.read_sql_query(query_group, conn)

    # Overall total
    query_total = "SELECT SUM(quantity) AS total_qty, SUM(quantity * price) AS total_revenue FROM sales;"
    totals = pd.read_sql_query(query_total, conn).iloc[0]

    conn.close()
    return df, totals

def print_summary(df, totals):
    print("\n=== Sales by product ===")
    print(df.to_string(index=False))
    print("\n=== Overall totals ===")
    print(f"Total quantity sold: {int(totals['total_qty'])}")
    print(f"Total revenue: {totals['total_revenue']:.2f}")

def plot_revenue(df):
    # Sorting
    df_sorted = df.sort_values("revenue", ascending=False).reset_index(drop=True)

    ax = df_sorted.plot(kind="bar", x="product", y="revenue", legend=False)
    ax.set_title("Revenue by Product")
    ax.set_xlabel("Product")
    ax.set_ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("sales_revenue_by_product.png")
    print("Saved chart: sales_revenue_by_product.png")
    plt.show()

if __name__ == "__main__":
    df, totals = run_queries()
    print_summary(df, totals)
    plot_revenue(df)
