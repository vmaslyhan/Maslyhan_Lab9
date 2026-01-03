import psycopg2

conn = psycopg2.connect(
    host="db",
    database="supply_db",
    user="supply_user",
    password="supply_pass"
)

cur = conn.cursor()

# Постачальники
cur.execute("""
CREATE TABLE IF NOT EXISTS Suppliers (
    supplier_id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    phone VARCHAR(20),
    bank_account VARCHAR(30)
)
""")

# Матеріали
cur.execute("""
CREATE TABLE IF NOT EXISTS Materials (
    material_id SERIAL PRIMARY KEY,
    material_name VARCHAR(50) NOT NULL,
    price NUMERIC(10,2) NOT NULL CHECK (price > 0)
)
""")

# Поставки
cur.execute("""
CREATE TABLE IF NOT EXISTS Supplies (
    supply_id SERIAL PRIMARY KEY,
    supply_date DATE NOT NULL,
    supplier_id INTEGER REFERENCES Suppliers(supplier_id) ON DELETE CASCADE,
    material_id INTEGER REFERENCES Materials(material_id) ON DELETE CASCADE,
    delivery_days INTEGER CHECK (delivery_days BETWEEN 1 AND 7),
    quantity INTEGER CHECK (quantity > 0)
)
""")

conn.commit()
cur.close()
conn.close()

print("Таблиці успішно створено")
