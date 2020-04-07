import database.connection as conn

def startup():
    conn.connect()

if __name__ == "__main__":
    startup()
