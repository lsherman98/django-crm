import psycopg2

db = psycopg2.connect(
    host = 'localhost',
    user = 'levisherman',
    password = 'password',
    port='5432'
)

cursor = db.cursor()
db.autocommit = True
cursor.execute("CREATE DATABASE elderco")

print("All Done!")