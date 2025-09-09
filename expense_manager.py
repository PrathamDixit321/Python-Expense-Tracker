from datetime import datetime
from database import connect_db

class ExpenseManager:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def add_expense(self, category, amount, description):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                            (date, category, amount, description))
        self.conn.commit()

    def get_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        return self.cursor.fetchall()
