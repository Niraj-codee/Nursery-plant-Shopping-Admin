import sqlite3

def initialize_db():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS plants (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 category TEXT,
                 price REAL,
                 stock INTEGER)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS categories (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS bills (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 plant_name TEXT,
                 category TEXT,
                 price REAL,
                 quantity INTEGER,
                 total REAL,
                 date TEXT)''')
    
    conn.commit()
    conn.close()

def get_plants():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("SELECT * FROM plants")
    plants = c.fetchall()
    conn.close()
    return plants

def add_plant(name, category, price, stock):
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("INSERT INTO plants (name, category, price, stock) VALUES (?, ?, ?, ?)",
              (name, category, price, stock))
    conn.commit()
    conn.close()

def update_plant(plant_id, name, category, price, stock):
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("UPDATE plants SET name = ?, category = ?, price = ?, stock = ? WHERE id = ?",
              (name, category, price, stock, plant_id))
    conn.commit()
    conn.close()

def delete_plant(plant_id):
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("DELETE FROM plants WHERE id = ?", (plant_id,))
    conn.commit()
    conn.close()

# database.py

import sqlite3

def get_customers():
    conn = sqlite3.connect('nursery.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()
    return customers

# Implement other database methods like add_customer, update_customer, etc.


def add_bill(plant_name, category, price, quantity, total, date):
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("INSERT INTO bills (plant_name, category, price, quantity, total, date) VALUES (?, ?, ?, ?, ?, ?)",
              (plant_name, category, price, quantity, total, date))
    conn.commit()
    conn.close()
def get_bills():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bills")
    bills = c.fetchall()
    conn.close()
    return bills
def get_customers():
    conn = sqlite3.connect('nursery.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()
    return customers

def add_customer(name, contact_number, email):
    conn = sqlite3.connect('nursery.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, contact_number, email) VALUES (?, ?, ?)",
                   (name, contact_number, email))
    conn.commit()
    conn.close()

def update_customer(customer_id, name, contact_number, email):
    conn = sqlite3.connect('nursery.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET name = ?, contact_number = ?, email = ? WHERE id = ?",
                   (name, contact_number, email, customer_id))
    conn.commit()
    conn.close()

def delete_customer(customer_id):
    conn = sqlite3.connect('nursery.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
    conn.commit()
    conn.close()


import sqlite3

def initialize_db():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE,
                 password TEXT)''')
    
    # Other table creation code...

    conn.commit()
    conn.close()

def register_user(username, password):
    try:
        conn = sqlite3.connect('nursery.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Username already exists
    finally:
        conn.close()

def check_login(username, password):
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user is not None


import sqlite3

def initialize_db():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS plants (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 category TEXT,
                 price REAL,
                 stock INTEGER)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS sale_plants (
                 id INTEGER PRIMARY KEY,
                 sale_price REAL,
                 FOREIGN KEY (id) REFERENCES plants(id) ON DELETE CASCADE)''')

    c.execute('''CREATE TABLE IF NOT EXISTS categories (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS bills (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 plant_name TEXT,
                 category TEXT,
                 price REAL,
                 quantity INTEGER,
                 total REAL,
                 date TEXT)''')

    conn.commit()
    conn.close()

def get_plants():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("SELECT * FROM plants")
    plants = c.fetchall()
    conn.close()
    return plants

def put_plant_on_sale(plant_id, sale_price):
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("INSERT INTO sale_plants (id, sale_price) VALUES (?, ?)", (plant_id, sale_price))
    conn.commit()
    conn.close()

def update_plant_price(plant_id, sale_price):
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("UPDATE sale_plants SET sale_price = ? WHERE id = ?", (sale_price, plant_id))
    conn.commit()
    conn.close()

def get_sale_plants():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute('''SELECT p.id, p.name, p.category, sp.sale_price
                 FROM plants p
                 JOIN sale_plants sp ON p.id = sp.id''')
    sale_plants = c.fetchall()
    conn.close()
    return sale_plants

def remove_plant_from_sale(plant_id):
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("DELETE FROM sale_plants WHERE id = ?", (plant_id,))
    conn.commit()
    conn.close()

def add_plant(name, category, price, stock):
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("INSERT INTO plants (name, category, price, stock) VALUES (?, ?, ?, ?)",
              (name, category, price, stock))
    conn.commit()
    conn.close()

# Sample usage
initialize_db()
# Uncomment below lines to test adding and managing plants
# add_plant("Rose", "Flower", 100, 50)
# put_plant_on_sale(1, 80)
# print(get_plants())
# print(get_sale_plants())
# update_plant_price(1, 70)
# remove_plant_from_sale(1)
import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database functions
def initialize_db():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS plants (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 category TEXT,
                 price REAL,
                 stock INTEGER)''')
    conn.commit()
    conn.close()

def get_plants():
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("SELECT * FROM plants")
    plants = c.fetchall()
    conn.close()
    return plants

def update_plant_price(plant_id, sale_price):
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("UPDATE plants SET price = ? WHERE id = ?", (sale_price, plant_id))
    conn.commit()
    conn.close()

def reduce_plant_stock(plant_id, quantity):
    conn = sqlite3.connect('nursery.db')
    c = conn.cursor()
    c.execute("UPDATE plants SET stock = stock - ? WHERE id = ?", (quantity, plant_id))
    conn.commit()
    conn.close()

# Admin App
class AdminApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nursery Admin")
        self.geometry("600x400")
        self.sale_price_entry = None
        self.sale_plants_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def sale_plants_screen(self):
        self.clear_screen()
        tk.Label(self, text="Manage Sale Plants", font=("Arial", 24)).pack(pady=20)

        plants = get_plants()
        for plant in plants:
            plant_frame = tk.Frame(self)
            plant_frame.pack(pady=5, fill='x')
            plant_info = f"{plant[1]} | Category: {plant[2]} | Price: ₹{plant[3]} | Stock: {plant[4]}"
            tk.Label(plant_frame, text=plant_info).pack(side='left')
            sale_button = tk.Button(plant_frame, text="Put on Sale", command=lambda p=plant: self.put_on_sale_screen(p))
            sale_button.pack(side='left', padx=5)

        tk.Button(self, text="Back", command=self.quit).pack(pady=10)

    def put_on_sale_screen(self, plant):
        self.clear_screen()
        tk.Label(self, text="Put Plant On Sale", font=("Arial", 24)).pack(pady=20)
        tk.Label(self, text="Sale Price").pack()
        self.sale_price_entry = tk.Entry(self)
        self.sale_price_entry.pack(pady=5)
        tk.Button(self, text="Confirm Sale Price", command=lambda: self.put_on_sale(plant[0], plant[4])).pack(pady=10)
        tk.Button(self, text="Back", command=self.sale_plants_screen).pack(pady=10)

    def put_on_sale(self, plant_id, stock):
        sale_price = float(self.sale_price_entry.get())
        if stock > 0:
            update_plant_price(plant_id, sale_price)
            reduce_plant_stock(plant_id, 1)  # Reduce stock by 1
            messagebox.showinfo("Success", "Plant has been put on sale and stock updated.")
        else:
            messagebox.showerror("Error", "Insufficient stock.")
        self.sale_plants_screen()

if __name__ == "__main__":
    initialize_db()
    app = AdminApp()
    app.mainloop()
