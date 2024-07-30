import sqlite3

con = sqlite3.connect("exemplo")

cursor = con.cursor()

# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS usuarios(
#     id INTEGER PRIMARY KEY,
#     nome TEXT NOT NULL,
#     idade INTEGER)
# '''
# )

# cursor.execute('''
# INSERT INTO usuarios(id, nome, idade) VALUES (?, ?,?)
# ''', (1, "Teste", 30))

# con.commit()

cursor.execute(
    """
SELECT * FROM usuarios"""
)

registro = cursor.fetchall()

for regis in registro:
    print(regis)
