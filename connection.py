import sqlite3
import bcrypt

class Connection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    
    def close(self):
        self.conn.close()