import sqlite3

class sqliteDb:
   def __init__(self):
      self.conn = sqlite3.connect('../sql/vineyard.db')
      self.cursor = self.conn.cursor()

   def get_output_model_records(self):
       query = ("SELECT * FROM output_model")
       return self.cursor.execute(query).fetchall()

