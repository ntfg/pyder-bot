import sqlite3 

PATH = "data/main.db"

connection = sqlite3.connect(PATH)
cur = sqlite3.Cursor(connection)


def is_exist(id: int) -> bool:
    query = cur.execute(f"SELECT * FROM USERS WHERE user_id = {id}").fetchall()

    if len(query):
        return True 
    
    return False





def is_db_exsits():
    try:
        cur.execute("SELECT * FROM users")
    except:
        with open("data/createdb.sql", "r") as script:
            script = script.read()
            cur.executescript(script)
            connection.commit()
            
            
is_db_exsits()