import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                               (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)''')
        self.connection.commit()

    def add_score(self, name, score):
        self.cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))
        self.connection.commit()

    def get_scores(self):
        self.cursor.execute("SELECT * FROM scores ORDER BY score DESC")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
