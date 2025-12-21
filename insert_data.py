import psycopg2

conn = psycopg2.connect(
    host="db",
    user="hotel_user",
    password="hotel_pass",
    database="hotel_db"
)

cur = conn.cursor()

# Вставка гостей
cur.execute("""
INSERT INTO Guests (last_name, first_name, patronymic, city)
VALUES
('Кравець', 'Віктор', 'Павлович', 'Київ'),
('Мельник', 'Оксана', 'Андріївна', 'Одеса'),
('Ткаченко', 'Сергій', 'Миколайович', 'Івано-Франківськ'),
('Гончар', 'Наталія', 'Володимирівна', 'Львів'),
('Литвин', 'Роман', 'Олександрович', 'Чернівці'),
('Федоренко', 'Світлана', 'Іванівна', 'Житомир'),
('Даниленко', 'Михайло', 'Петрович', 'Хмельницький');
""")

# Вставка номерів
cur.execute("""
INSERT INTO Rooms (num_rooms, floor, tv, fridge, num_places, category, price_per_day)
VALUES
(1, 1, TRUE, TRUE, 1, 'звичайний', 500.00),
(2, 1, TRUE, FALSE, 2, 'звичайний', 600.00),
(2, 2, TRUE, TRUE, 2, 'півлюкс', 800.00),
(3, 2, TRUE, TRUE, 3, 'люкс', 1200.00),
(1, 3, FALSE, TRUE, 1, 'звичайний', 450.00),
(2, 3, TRUE, TRUE, 2, 'півлюкс', 850.00),
(3, 3, TRUE, TRUE, 3, 'люкс', 1300.00),
(1, 2, TRUE, FALSE, 1, 'звичайний', 480.00),
(2, 1, FALSE, TRUE, 2, 'півлюкс', 750.00),
(3, 2, TRUE, TRUE, 3, 'люкс', 1250.00);
""")

# Вставка реєстрацій гостей
cur.execute("""
INSERT INTO Registrations (guest_id, arrival_date, num_days, room_number)
VALUES
(1, '2025-01-10', 3, 1),
(2, '2025-01-12', 2, 3),
(3, '2025-01-15', 5, 4),
(4, '2025-01-20', 1, 2),
(5, '2025-02-01', 4, 5),
(6, '2025-02-05', 2, 6),
(7, '2025-02-07', 3, 7),
(1, '2025-02-10', 2, 8),
(2, '2025-02-17', 4, 9),
(3, '2025-02-20', 3, 10);
""")

conn.commit()
cur.close()
conn.close()

print("Дані успішно вставлено")
