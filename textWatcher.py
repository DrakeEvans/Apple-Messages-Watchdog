
 
import sqlite3
from sqlite3 import Error
import time
import os
import urllib.request

 
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
    debug = False
    secondTest = False
    lastMessageGuid = ''
    while True:
        if debug:
            time.sleep(10)
        else:
            time.sleep(60*5) #Sleep for 5  minutes

        database = os.path.expanduser(r"~/Library/Messages/chat.db")
        #print(database)
    
        # create a database connection
        conn = create_connection(database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT date, guid, is_from_me, is_delivered FROM message WHERE handle_id=7 ORDER BY date DESC LIMIT 1")
            
            returnedRows = cur.fetchall()
            recentMessage = returnedRows[0]
            if debug: print(f'Last Row:\n{recentMessage}')
            if debug: print (f'Last Message GUID: {lastMessageGuid}')
            if recentMessage[2] == 0 and recentMessage[3] == 1 and not recentMessage[1] == lastMessageGuid:
                if debug: print(f'Second Test: {secondTest}')
                if secondTest:
                    getRequest = urllib.request.urlopen("https://maker.ifttt.com/trigger/unrespondedMessage/with/key/bf-D667z5hcIbtIFPpGlvi").read()
                    secondTest = False
                    lastMessageGuid = recentMessage[1]
                else:
                    secondTest = True


 
if __name__ == '__main__':
    main()