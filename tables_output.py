import pandas as pd
from sqlalchemy import create_engine
from tabulate import tabulate

engine = create_engine("postgresql+psycopg2://hotel_user:hotel_pass@db/hotel_db")

def print_table(title, query):
    print("\n"+title)
    df = pd.read_sql_query(query, engine)
    if df.empty:
        print("Таблиця порожня.")
    else:
        print(tabulate(df, headers='keys', tablefmt='psql'))

queries = [
    ("Всі гості", "SELECT * FROM Guests"),
    
    ("Всі номери", "SELECT * FROM Rooms"),

    ("Всі реєстрації", "SELECT * FROM Registrations"),

    ("Номери з телевізором", "SELECT * FROM Rooms WHERE tv=TRUE"),

    ("Кінцева дата проживання для кожного гостя",
     "SELECT g.last_name, g.first_name, g.patronymic, r.arrival_date + r.num_days AS departure_date "
     "FROM Registrations r "
     "JOIN Guests g ON r.guest_id=g.guest_id"),

    ("Кількість номерів кожної категорії", 
     "SELECT category, COUNT(*) "
     "FROM Rooms "
     "GROUP BY category"),

    ("Повна вартість проживання для кожного гостя",
     "SELECT g.last_name, g.first_name, g.patronymic, SUM(r.num_days * rm.price_per_day) AS total_cost "
     "FROM Registrations r "
     "JOIN Guests g ON r.guest_id=g.guest_id JOIN Rooms rm ON r.room_number=rm.room_number "
     "GROUP BY g.last_name, g.first_name, g.patronymic"),

    ("Кількість номерів кожної категорії на кожному поверсі",
     "SELECT floor, category, COUNT(*) "
     "FROM Rooms "
     "GROUP BY floor, category "
     "ORDER BY floor, category"),
     
    ("Гості в обраній категорії номерів (наприклад 'люкс')",
     "SELECT g.* "
     "FROM Guests g JOIN Registrations r ON g.guest_id=r.guest_id "
     "JOIN Rooms rm ON r.room_number=rm.room_number "
     "WHERE rm.category='люкс' "
     "ORDER BY g.last_name")
]

for title, query in queries:
    print_table(title, query)
