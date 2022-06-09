import sqlite3

class DataBase():
    
    def __init__(self):
        self.conn = sqlite3.connect('countries.db')
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS country_time(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Region VARCHAR(30),
            `City Name` VARCHAR(30),
            Language VARCHAR(50),
            Time float
        )
        """
        self.conn.execute(query)

    def save_dataframe(self, df):
        df.to_sql('country_time', self.conn, if_exists='replace', index=False)