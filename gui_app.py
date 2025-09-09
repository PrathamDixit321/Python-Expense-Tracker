import tkinter as tk
from tkinter import messagebox
from expense_manager import ExpenseManager

manager = ExpenseManager()

def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    desc = desc_entry.get()
    try:
        manager.add_expense(category, float(amount), desc)
        messagebox.showinfo("Success", "Expense added!")
    except:
        messagebox.showerror("Error", "Invalid input.")

app = tk.Tk()
app.title("Expense Tracker")
app.geometry("300x250")

tk.Label(app, text="Category").pack()
category_entry = tk.Entry(app)
category_entry.pack()

tk.Label(app, text="Amount").pack()
amount_entry = tk.Entry(app)
amount_entry.pack()

tk.Label(app, text="Description").pack()
desc_entry = tk.Entry(app)
desc_entry.pack()

tk.Button(app, text="Add Expense", command=add_expense).pack(pady=10)
tk.Button(app, text="Quit", command=app.quit).pack()

app.mainloop()
