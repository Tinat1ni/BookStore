import sqlite3


class DataBase:
    def __init__(self, db_name='bookstore.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()


    def create_tables(self):
        query1 = '''
           CREATE TABLE IF NOT EXISTS authors(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              last_name TEXT NOT NULL,
              date_of_birth DATE,
              birth_place TEXT
           );
        '''

        query2 = '''
           CREATE TABLE IF NOT EXISTS books(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              category TEXT,
              number_of_pages INTEGER,
              publication_date DATE,
              author_id INTEGER,
              FOREIGN KEY (author_id) REFERENCES authors(id)             
           )
        '''

        self.cursor.execute(query1)
        self.cursor.execute(query2)
        self.connection.commit()


    def close(self):
        self.cursor.close()
        self.connection.close()

