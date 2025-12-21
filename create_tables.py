import psycopg2

conn = psycopg2.connect(
    host="db",
    database="hotel_db",
    user="hotel_user",
    password="hotel_pass"
)

cur = conn.cursor()

# Таблиця Guests
cur.execute("""
CREATE TABLE IF NOT EXISTS Guests (
    guest_id SERIAL PRIMARY KEY,
    last_name VARCHAR(50),
    first_name VARCHAR(50),
    patronymic VARCHAR(50),
    city VARCHAR(50)
)
""")

# Таблиця Rooms
cur.execute("""
CREATE TABLE IF NOT EXISTS Rooms (
    room_number SERIAL PRIMARY KEY,
    num_rooms INTEGER,
    floor INTEGER,
    tv BOOLEAN,
    fridge BOOLEAN,
    num_places INTEGER,
    category VARCHAR(20),
    price_per_day NUMERIC(8,2)
)
""")

# Таблиця Registrations
cur.execute("""
CREATE TABLE IF NOT EXISTS Registrations (
    registration_id SERIAL PRIMARY KEY,
    guest_id INTEGER REFERENCES Guests(guest_id) ON DELETE CASCADE,
    arrival_date DATE,
    num_days INTEGER,
    room_number INTEGER REFERENCES Rooms(room_number) ON DELETE CASCADE
)
""")

conn.commit()
cur.close()
conn.close()

print("Таблиці успішно створено")
