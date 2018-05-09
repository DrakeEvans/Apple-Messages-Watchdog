
 
import sqlite3
from sqlite3 import Error
import time
import os
import urllib.request
import Personal_Info

 
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

        database = os.path.expanduser(Personal_Info.databaseFileLocation)

    
        # create a database connection
        conn = create_connection(database)
        with conn:
            cur = conn.cursor()
            cur.execute(f"SELECT date, guid, is_from_me, is_delivered FROM message WHERE handle_id={Personal_Info.handle_id} ORDER BY date DESC LIMIT 1")
            
            returnedRows = cur.fetchall()
            recentMessage = returnedRows[0]

            if recentMessage[2] == 0 and recentMessage[3] == 1 and not recentMessage[1] == lastMessageGuid: 
                '''message is not from me
                AND message is delivered
                AND its anew message
                ''' 

                if secondTest: #only send the text if its the second time, prevents being triggered for at least 5 minutes
                    getRequest = urllib.request.urlopen(Personal_Info.httpRequestURL).read() #Send http request to IFTTT
                    secondTest = False
                    lastMessageGuid = recentMessage[1]
                else:
                    secondTest = True


 
if __name__ == '__main__': # In case I want to turn this into a class
    main()