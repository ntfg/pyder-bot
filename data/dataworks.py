import sqlite3 

PATH = "data/main.db"

connection = sqlite3.connect(PATH)
cur = sqlite3.Cursor(connection)


def is_exist(id: int) -> bool:
    query = cur.execute(f"SELECT * FROM USERS WHERE user_id = {id}").fetchall()

    if len(query):
        return True 
    
    return False


def create_app(data: list):
    user_id = data[0]
    name = data[1]
    age = data[2]
    photo = data[3]
    description = data[4]
    telegram = data[5]
    
    cur.execute(f'''DELETE FROM users WHERE user_id = {user_id}''')
    cur.execute(f'''INSERT INTO users (user_id, name, age, photo, description, telegram)
                VALUES ({user_id}, "{name}", {age}, "{photo}", "{description}", "{telegram}")''')

    connection.commit()
    
    
def load_match(user_id: int) -> list[tuple]:
    try:
        user_id = cur.execute(f'''SELECT send FROM matches WHERE receive = {user_id}''').fetchone()[0]
        return get_user_app(user_id)
    except:
        return


def make_match(send_id: int, receive: int):
    cur.execute(f'''INSERT INTO matches (send, receive)
                VALUES ({send_id}, {receive})''')
    connection.commit()
    

def get_random_app(user_id: int) -> list[tuple]:
    return cur.execute(f'''SELECT * FROM users WHERE user_id <> {user_id} ORDER BY RANDOM() LIMIT 1''').fetchone()
    

def is_db_exsits():
    try:
        cur.execute("SELECT * FROM users")
    except:
        with open("data/createdb.sql", "r") as script:
            script = script.read()
            cur.executescript(script)
            connection.commit()
            

def get_user_app(user_id: int) -> list[tuple]:
    return cur.execute(f'''SELECT * FROM users WHERE user_id = {user_id}''').fetchone()
            
            
def remove_match(send_id: int, receive_id: int):
    cur.execute(f'''DELETE FROM matches WHERE receive = {receive_id} AND send = {send_id}''')
    
is_db_exsits()