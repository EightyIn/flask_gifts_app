import sqlite3

conn = sqlite3.connect('gifts.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS gifts (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    gift TEXT NOT NULL,
                    price REAL NOT NULL,
                    status TEXT NOT NULL)''')

gifts_data = [
    ('Иван Иванович', 'Санки', 2000, 'куплен'),
    ('Ирина Сергеевна', 'Цветы', 3000, 'не куплен'),
    ('Сергей Петрович', 'Книга', 1500, 'куплен'),
    ('Ольга Васильевна', 'Шарф', 700, 'не куплен'),
    ('Александр Николаевич', 'Часы', 5000, 'куплен'),
    ('Елена Борисовна', 'Игрушка', 1200, 'не куплен'),
    ('Дмитрий Александрович', 'Набор для рисования', 2500, 'куплен'),
    ('Ксения Викторовна', 'Умная колонка', 6000, 'не куплен'),
    ('Федор Анатольевич', 'Кофеварка', 3500, 'куплен'),
    ('Анна Дмитриевна', 'Плед', 1800, 'не куплен')
]

cursor.executemany('INSERT INTO gifts (name, gift, price, status) VALUES (?, ?, ?, ?)', gifts_data)

conn.commit()
conn.close()

print("База данных и таблица создана, данные добавлены.")