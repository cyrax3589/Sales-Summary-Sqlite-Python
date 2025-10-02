# Sales Summary using SQLite and Python

This project demonstrates how to connect Python with an SQLite database, run SQL queries for sales analysis, and generate visual outputs such as summary tables and bar charts.

## Project Structure
- `create_db.py` — Script to create a sample SQLite database (`sales_data.db`) and insert sample data.
- `sales_summary.py` — Main analysis script. Runs SQL queries, prints sales summary, and generates a revenue bar chart.
- `sales_data.db` — SQLite database file (generated after running `create_db.py`).
- `sales_revenue_by_product.png` — Example output chart image (generated after running `sales_summary.py`).

## Features
- Uses SQLite as a lightweight database.
- Executes SQL queries from Python (`sqlite3` + `pandas`).
- Aggregates sales data (total quantity and revenue by product).
- Saves results to both the terminal and a bar chart image.

## Console Output
<img width="424" height="248" alt="image" src="https://github.com/user-attachments/assets/1a5697b3-4eb4-458d-8bf5-ca380be22f68" />

## Visual Representation
<img width="640" height="480" alt="sales_revenue_by_product" src="https://github.com/user-attachments/assets/bfbe9cfc-42a0-4ea5-abd6-de8a0bc0bf59" />
