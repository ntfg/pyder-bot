import sqlite3 

PATH = "data/main.db"

connection = sqlite3.connect(PATH)
cur = sqlite3.Cursor(connection)


def is_exist(id: int) -> bool:
    query = cur.execute(f"SELECT * FROM USERS WHERE user_id = {id}").fetchall()

    if len(query):
        return True 
    
    return False


def new_user(data: list):
    user_id = data[0]
    name = data[1]
    age = data[2]
    photo = data[3]
    description = data[4]
    telegram = data[5]
    
    cur.execute(f'''INSERT INTO users (user_id, name, age, photo, description, telegram)
                VALUES ({user_id}, "{name}", {age}, "{photo}", "{description}", "{telegram}")''')

    connection.commit()
    
    
def load_match(user_id: int) -> list[tuple]:
    return cur.execute(f'''SELECT * FROM matches WHERE receive = {user_id}''').fetchone()


def make_match(send_id: int, receive: int):
    cur.execute(f'''INSERT INTO matches (send, receive)
                VALUES ({send_id}, {receive})''')
    

def get_app(user_id: int) -> list[tuple]:
    return cur.execute(f'''SELECT * FROM users WHERE user_id <> {user_id} ORDER BY RANDOM() LIMIT 1''').fetchone()
    

def is_db_exsits():
    try:
        cur.execute("SELECT * FROM users")
    except:
        with open("data/createdb.sql", "r") as script:
            script = script.read()
            cur.executescript(script)
            connection.commit()
            
            
is_db_exsits()