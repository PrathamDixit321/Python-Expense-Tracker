import pandas as pd
import matplotlib.pyplot as plt
from database import connect_db

def generate_reports():
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = df['amount'].astype(float)

    print("\nTotal spent by category:")
    print(df.groupby("category")["amount"].sum())

    # Pie chart
    df.groupby("category")["amount"].sum().plot(kind='pie', autopct='%1.1f%%', title='Spending by Category')
    plt.axis('equal')
    plt.show()

    # Line chart
    df.set_index("date").resample('D')["amount"].sum().plot(title='Daily Spending')
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.grid()
    plt.show()
