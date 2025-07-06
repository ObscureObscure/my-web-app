import sqlite3
import wiki

con = sqlite3.connect("users.db")
cur = con.cursor()

def add_user(username, password):
    con = sqlite3.connect("users.db")
    cur = con.cursor()

    cur.execute("INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "');")
    con.commit()

def is_user_authorized(name_of_user, password):
    con = sqlite3.connect("users.db")
    cur = con.cursor()

    res = cur.execute(f"SELECT * FROM users WHERE username='{name_of_user}' AND password='{password}';")
    return (res.fetchall() != [])  

def add_film(wiki_link):
    con = sqlite3.connect("users.db")
    cur = con.cursor()

    film = wiki.parse_film(wiki_link)
    cur.execute(f"INSERT INTO films (title, link, image) VALUES ('{film[0]}', '{film[1]}', '{film[2]}');")
    con.commit()

# films = wiki.parse_film_info()

# for film in films:
#     print(film[3])
#     cur.execute(f"INSERT INTO films (title, link, image) VALUES ('{film[3]}', '{film[1]}', '{film[2]}');")
    
#     con.commit()
#     print(film)

# add_film(input('введи ссылку на вики статью о фильме'))

res = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(res.fetchall())
res = cur.execute("SELECT * FROM users")
print(res.fetchall())