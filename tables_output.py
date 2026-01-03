import pandas as pd
from sqlalchemy import create_engine
from tabulate import tabulate

engine = create_engine(
    "postgresql+psycopg2://supply_user:supply_pass@db/supply_db"
)

def print_table(title, query):
    print("\n" + title)
    df = pd.read_sql_query(query, engine)
    if df.empty:
        print("Таблиця порожня.")
    else:
        print(tabulate(df, headers='keys', tablefmt='psql'))

queries = [
    ("Всі постачальники", "SELECT * FROM Suppliers"),
    ("Всі матеріали", "SELECT * FROM Materials"),
    ("Всі поставки", "SELECT * FROM Supplies"),

    ("Поставки за 3 або менше днів (сортування за назвою постачальника)",
     """SELECT s.supply_id, sp.company_name, s.delivery_days
        FROM Supplies s
        JOIN Suppliers sp ON s.supplier_id = sp.supplier_id
        WHERE s.delivery_days <= 3
        ORDER BY sp.company_name"""),

    ("Сума до оплати за кожну поставку",
     """SELECT s.supply_id, m.material_name, s.quantity * m.price AS total_cost
        FROM Supplies s
        JOIN Materials m ON s.material_id = m.material_id"""),

    ("Поставки обраного матеріалу (наприклад 'Деревина')",
     """SELECT *
        FROM Supplies s
        JOIN Materials m ON s.material_id = m.material_id
        WHERE m.material_name = 'Деревина'"""),

    ("Кількість кожного матеріалу від кожного постачальника",
     """SELECT sp.company_name, m.material_name, SUM(s.quantity) AS total_quantity
        FROM Supplies s
        JOIN Suppliers sp ON s.supplier_id = sp.supplier_id
        JOIN Materials m ON s.material_id = m.material_id
        GROUP BY sp.company_name, m.material_name
        ORDER BY sp.company_name"""),

    ("Загальна кількість кожного матеріалу",
     """SELECT m.material_name, SUM(s.quantity) AS total_quantity
        FROM Supplies s
        JOIN Materials m ON s.material_id = m.material_id
        GROUP BY m.material_name"""),

    ("Кількість поставок від кожного постачальника",
     """SELECT sp.company_name, COUNT(*) AS supply_count
        FROM Supplies s
        JOIN Suppliers sp ON s.supplier_id = sp.supplier_id
        GROUP BY sp.company_name""")
]

for title, query in queries:
    print_table(title, query)
