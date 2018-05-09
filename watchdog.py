
 
import sqlite3
from sqlite3 import Error
import personalInfo
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
def main():
    database = r"C:\Users\MBP\chat.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT date, text, is_from_me, is_delivered FROM message WHERE handle_id=7 ORDER BY date DESC LIMIT 1")
 
        returnedRows = cur.fetchall()
        recentMessage = returnedRows[0]
        if recentMessage[2] == 0 and recentMessage[3] == 1:
            #make IFTTT request
            print("You need to send a text asshole")

 
if __name__ == '__main__':
    main()