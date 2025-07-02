import sqlite3

con = sqlite3.connect("users.db")
cur = con.cursor()

def add_user(username, password):
    cur.execute("INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "');")
    con.commit()

def is_user_authorized(name_of_user, password):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute(f"SELECT * FROM users WHERE username='{name_of_user}' AND password='{password}';")
    return (res.fetchall() != [])  


# cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL UNIQUE)")



# cur.execute("""
#             INSERT INTO users (username, password) 
#             VALUES ('JewSpirit', 'Rfrfujuj1');
# """)
# if input("""
#          save this users in database? 
#          0 - don't save
#          1 - save
#          """) == "1":
#     con.commit()



res = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(res.fetchone())
res = cur.execute("SELECT * FROM users")
print(res.fetchall())