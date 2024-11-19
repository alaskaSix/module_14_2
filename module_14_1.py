import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i + 1}", f"example{i + 1}@gmail.com", f"{(i + 1) * 10}", "1000"))
# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
cursor.execute("UPDATE Users SET balance = ? WHERE id%2 <> ?", (500, 0))
# Удалите каждую 3ую запись в таблице начиная с 1ой:
cursor.execute("DELETE FROM Users WHERE (id+2)%3 = ?", (0,))
# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age <> ?", (60,))
#Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
#Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
#Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
#Вывести в консоль средний баланс всех пользователей.
print(all_balances / total_users)

connection.commit()
connection.close()
