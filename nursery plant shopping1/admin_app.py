import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import database
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 

class AdminApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nursery Plant Shopping Admin")
        self.state('zoomed')
        self.geometry("800x600")
        self.configure(bg="#f0f8ff")  # Light background color
        self.login_screen()

    def login_screen(self):

        
     def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_screen()

        # Load the background image
           # Load the image
        self.bg_image = Image.open(r"D:\Raj Pro 2024\Nursery Plant\nursery plant shopping1\Image1.jpeg")  # Replace with your image path
        
        # Resize the image to fit the canvas
        self.bg_image = self.bg_image.resize((1700, 800), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a canvas to hold the background image
        self.canvas = tk.Canvas(self, width=1200, height=700)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)
        # Set up the window
        self.title("Nursery Plant Shopping Admin")
        self.geometry("400x400")
        self.configure(bg="#f0ffff")

        # Title label
        tk.Label(self, text="Nursery Plant Shopping Admin", font=("Arial", 70), bg="#171714", fg="#FFFFFF").place(relx=0.5, rely=0.1, anchor="center")
        tk.Label(self, text="WWW.nurseryplant.com", font=("Arial", 40), bg="#171714", fg="#FFFFFF").place(relx=0.2, rely=0.9, anchor="center")

        # Create a frame for the login area
        login_frame = tk.Frame(self, bg="#faeb7a", bd=2, relief="groove")
        login_frame.place(relx=0.13, rely=0.5, anchor="center", width=300, height=250)

        # Admin Login label
        tk.Label(login_frame, text="Admin Login", font=("Arial", 20), bg="#f0f8ff", fg="#000080").pack(pady=(10, 10))

        # Username label and entry
        tk.Label(login_frame, text="Username", font=("Arial", 16), bg="#f0f8ff", fg="#000080").pack(pady=(5, 0))
        self.username_entry = tk.Entry(login_frame, bg="#ffffff", fg="#000000")
        self.username_entry.pack(pady=(0, 10), padx=10, fill=tk.X)

        # Password label and entry
        tk.Label(login_frame, text="Password", font=("Arial", 16), bg="#f0f8ff", fg="#000080").pack(pady=(5, 0))
        self.password_entry = tk.Entry(login_frame, show="*", bg="#ffffff", fg="#000000")
        self.password_entry.pack(pady=(0, 10), padx=10, fill=tk.X)

        # Show/Hide Password Checkbox
        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbox = tk.Checkbutton(login_frame, text="Show Password", variable=self.show_password_var, bg="#f0f8ff", command=self.toggle_password)
        self.show_password_checkbox.pack()

        # Buttons
        tk.Button(login_frame, text="Login", command=self.check_login, bg="#4CAF50", fg="#ffffff").pack(side=tk.LEFT, padx=(10, 5), pady=(5, 10))
        tk.Button(login_frame, text="Register", command=self.register_screen, bg="#2196F3", fg="#ffffff").pack(side=tk.RIGHT, padx=(5, 10), pady=(5, 10))

    def toggle_password(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def register_screen(self):
        self.clear_screen()

        # Create a frame for the registration area
        register_frame = tk.Frame(self, bg="#faeb7a", bd=2, relief="groove")
        register_frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=250)

        # Registration label
        tk.Label(register_frame, text="Register User", font=("Arial", 20), bg="#f0f8ff", fg="#000080").pack(pady=(10, 10))

        # New Username label and entry
        tk.Label(register_frame, text="New Username", font=("Arial", 16), bg="#f0f8ff", fg="#000080").pack(pady=(5, 0))
        self.new_username_entry = tk.Entry(register_frame, bg="#ffffff", fg="#000000")
        self.new_username_entry.pack(pady=(0, 10), padx=10, fill=tk.X)

        # New Password label and entry
        tk.Label(register_frame, text="New Password", font=("Arial", 16), bg="#f0f8ff", fg="#000080").pack(pady=(5, 0))
        self.new_password_entry = tk.Entry(register_frame, show="*", bg="#ffffff", fg="#000000")
        self.new_password_entry.pack(pady=(0, 10), padx=10, fill=tk.X)

        # Show/Hide Password Checkbox for registration
        self.show_new_password_var = tk.BooleanVar()
        self.show_new_password_checkbox = tk.Checkbutton(register_frame, text="Show Password", variable=self.show_new_password_var, bg="#f0f8ff", command=self.toggle_new_password)
        self.show_new_password_checkbox.pack()

        # Buttons
        tk.Button(register_frame, text="Register", command=self.register_user, bg="#4CAF50", fg="#ffffff").pack(pady=(10, 5))
        tk.Button(register_frame, text="Back to Login", command=self.login_screen, bg="#2196F3", fg="#ffffff").pack(pady=(5, 10))

    def toggle_new_password(self):
        if self.show_new_password_var.get():
            self.new_password_entry.config(show="")
        else:
            self.new_password_entry.config(show="*")

    def register_user(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()

        # Password length check
        if len(password) <= 3 or len(password) >= 8:
            messagebox.showerror("Error", "Password must be greater than 3 characters and less than 8 characters.")
            return

        # Here you should save the new user to the database (implement database function)
        if database.register_user(username, password):
            messagebox.showinfo("Success", f"User {username} registered successfully.")
            self.login_screen()
        else:
            messagebox.showerror("Error", "User registration failed. Username may already exist.")

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Password length check for login
        if len(password) <= 3 or len(password) >= 8:
            messagebox.showerror("Error", "Password must be greater than 3 characters and less than 8 characters.")
            return

        # Check login credentials with the database
        if database.check_login(username, password):  # Implement this function
            self.admin_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")


    def admin_menu(self):
        self.clear_screen()

        # Load the background image for the admin menu
        self.bg_image = Image.open(r"D:\Raj Pro 2024\Nursery Plant\nursery plant shopping1\Image2.jpg")  # Replace with your image path
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a canvas to hold the background image
        self.canvas = tk.Canvas(self, width=1500, height=1300)
        self.canvas.pack(fill="both", expand=True)

        # Add the background image to the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        # Create the admin menu title
        tk.Label(self, text="Admin Menu", font=("Arial", 58), bg="#f0f8ff", fg="#000080",borderwidth=2,         # Set the border width
    relief="solid",).place(relx=0.26, rely=0.18, anchor="center")

        # Create a frame to hold the menu buttons
        menu_frame = tk.Frame(self,  bg="#fff048")
        menu_frame.place(relx=0.5, rely=0.34, anchor="center")

        # Create buttons for each menu option
        tk.Button(menu_frame, text="Add Plant", command=self.add_plant_screen,font=("Arial", 24), bg="#2196F3", fg="#ffffff").pack(side="left", padx=5)
        tk.Button(menu_frame, text="View Plants", command=self.view_plants_screen,font=("Arial", 24), bg="#2196F3", fg="#ffffff").pack(side="left", padx=5)
        tk.Button(menu_frame, text="Sale Plants", command=self.sale_plants_screen,font=("Arial", 24), bg="#2196F3", fg="#ffffff").pack(side="left", padx=5)
        tk.Button(menu_frame, text="Generate Bill", command=self.generate_bill_screen,font=("Arial", 24), bg="#2196F3", fg="#ffffff").pack(side="left", padx=5)
        tk.Button(menu_frame, text="View Bills", command=self.view_bills_screen,font=("Arial", 24), bg="#2196F3", fg="#ffffff").pack(side="left", padx=5)
        tk.Button(menu_frame, text="Manage Customers", command=self.manage_customers_screen,font=("Arial", 24), bg="#2196F3", fg="#ffffff").pack(side="left", padx=5)

         # Add button to return to the login page
        tk.Button(menu_frame, text="Logout",font=("Arial", 24), command=self.login_screen, bg="#f44336", fg="#ffffff").pack(side="left", padx=5)


        # Add address or additional info in the bottom right corner
        address_info = " Address:- Sonbarsa Bazar, Gorakhpur \n Mob no: 7310172553"
        tk.Label(self, text=address_info, font=("Arial", 17), bg="#eca1a6", fg="#000000",borderwidth=3,         # Set the border width
    relief="solid",).place(relx=0.99, rely=0.99, anchor="se")

        address_info = "About:-  We have all types of Nursery plants available here,\n lots of discounts are available at very low prices during Diwali."
        tk.Label(self, text=address_info, font=("Arial", 20), bg="#eca1a6", fg="#000080",borderwidth=2,         # Set the border width
    relief="solid",).place(relx=0.50, rely=0.98, anchor="se")

    # ... [Rest of the methods remain unchanged] ...

 


    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def add_plant_screen(self):
        self.clear_screen()
        tk.Label(self, text="Add New Plant", font=("Arial", 24), bg="#f0f8ff", fg="#000080").pack(pady=20)

        tk.Label(self, text="Plant Name", bg="#f0f8ff", fg="#000080").pack()
        self.plant_name_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.plant_name_entry.pack(pady=5)

        tk.Label(self, text="Category", bg="#f0f8ff", fg="#000080").pack()

        # Create a combobox for category selection
        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(self, textvariable=self.category_var)
        self.category_combobox['values'] = ["","Flower", "Tree", "Fruit", "Vegetable","Seasonal Plants (Mausami Podhe)","Citrus Plants (Narangi ke Podhe)","Shade Plants (Chhaya Mein Ugnay Wale)","Herbaceous Plants (Ghani Patte Wale Podhe)"]
        self.category_combobox.current(0)  # Set default selection
        self.category_combobox.pack(pady=5)

        tk.Label(self, text="Price", bg="#f0f8ff", fg="#000080").pack()
        self.price_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.price_entry.pack(pady=5)

        tk.Label(self, text="Stock in pieces", bg="#f0f8ff", fg="#000080").pack()
        self.stock_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.stock_entry.pack(pady=5)

        tk.Button(self, text="Add Plant", command=self.add_plant, bg="#4CAF50", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="Back", command=self.admin_menu, bg="#FFC107", fg="#000000").pack(pady=10)

    def add_plant(self):
        try:
            name = self.plant_name_entry.get()
            category = self.category_var.get()  # Get selected category from combobox
            price = float(self.price_entry.get())
            stock = int(self.stock_entry.get())

            # Assuming database.add_plant() is defined elsewhere
            database.add_plant(name, category, price, stock)
            messagebox.showinfo("Success", f"{name} has been added to the inventory.")
            self.admin_menu()  # Navigate back to admin menu
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data.")

    def view_plants_screen(self):
        self.clear_screen()
        tk.Label(self, text="All Plants", font=("Arial", 24), bg="#f0f8ff", fg="#000080").pack(pady=20)

        plants = database.get_plants()

        for plant in plants:
            plant_frame = tk.Frame(self, bg="#e3f2fd")
            plant_frame.pack(pady=5, fill='x')

            plant_info = f"{plant[1]} | Category: {plant[2]} | Price: ₹{plant[3]} | Stock: {plant[4]}"
            tk.Label(plant_frame, text=plant_info, bg="#e3f2fd").pack(side='left')

            edit_button = tk.Button(plant_frame, text="Edit", command=lambda p=plant: self.edit_plant_screen(p), bg="#FFC107", fg="#000000")
            edit_button.pack(side='left', padx=5)

            delete_button = tk.Button(plant_frame, text="Delete", command=lambda p=plant: self.delete_plant(p[0]), bg="#f44336", fg="#ffffff")
            delete_button.pack(side='left', padx=5)

        tk.Button(self, text="Back", command=self.admin_menu, bg="#FFC107", fg="#000000").pack(pady=10)

    def sale_plants_screen(self):
        self.clear_screen()
        tk.Label(self, text="Manage Sale Plants", font=("Arial", 24), bg="#f0f8ff", fg="#000080").pack(pady=20)

        plants = database.get_plants()  # Assuming you have a method to fetch all plants

        for plant in plants:
            plant_frame = tk.Frame(self, bg="#e3f2fd")
            plant_frame.pack(pady=5, fill='x')

            plant_info = f"{plant[1]} | Category: {plant[2]} | Price: ₹{plant[3]} | Stock: {plant[4]}"
            tk.Label(plant_frame, text=plant_info, bg="#e3f2fd").pack(side='left')

            sale_button = tk.Button(plant_frame, text="Put on Sale", command=lambda p=plant: self.put_on_sale_screen(p), bg="#4CAF50", fg="#ffffff")
            sale_button.pack(side='left', padx=5)

        tk.Button(self, text="Back", command=self.admin_menu, bg="#FFC107", fg="#000000").pack(pady=10)

    def put_on_sale_screen(self, plant):
        self.clear_screen()
        tk.Label(self, text="Put Plant On Sale", font=("Arial", 24), bg="#f0f8ff", fg="#000080").pack(pady=20)

        tk.Label(self, text="Sale Price", bg="#f0f8ff", fg="#000080").pack()
        self.sale_price_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.sale_price_entry.pack(pady=5)

        tk.Button(self, text="Confirm Sale Price", command=lambda: self.put_on_sale(plant[0]), bg="#4CAF50", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="Back", command=self.sale_plants_screen, bg="#FFC107", fg="#000000").pack(pady=10)

    def put_on_sale(self, plant_id):
        sale_price = float(self.sale_price_entry.get())

        database.update_plant_price(plant_id, sale_price)  # Assuming you have a method to update the price
        messagebox.showinfo("Success", "Plant has been put on sale.")
        self.sale_plants_screen()

    def edit_plant_screen(self, plant):
        self.clear_screen()
        tk.Label(self, text="Edit Plant", font=("Arial", 24), bg="#f0f8ff", fg="#000080").pack(pady=20)

        tk.Label(self, text="Plant Name", bg="#f0f8ff", fg="#000080").pack()
        self.edit_plant_name_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.edit_plant_name_entry.insert(0, plant[1])
        self.edit_plant_name_entry.pack(pady=5)

        tk.Label(self, text="Category", bg="#f0f8ff", fg="#000080").pack()
        self.edit_category_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.edit_category_entry.insert(0, plant[2])
        self.edit_category_entry.pack(pady=5)

        tk.Label(self, text="Price", bg="#f0f8ff", fg="#000080").pack()
        self.edit_price_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.edit_price_entry.insert(0, plant[3])
        self.edit_price_entry.pack(pady=5)

        tk.Label(self, text="Stock in pieces", bg="#f0f8ff", fg="#000080").pack()
        self.edit_stock_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.edit_stock_entry.insert(0, plant[4])
        self.edit_stock_entry.pack(pady=5)

        tk.Button(self, text="Save Changes", command=lambda: self.update_plant(plant[0]), bg="#4CAF50", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="Back", command=self.view_plants_screen, bg="#FFC107", fg="#000000").pack(pady=10)

    def update_plant(self, plant_id):
        name = self.edit_plant_name_entry.get()
        category = self.edit_category_entry.get()
        price = float(self.edit_price_entry.get())
        stock = int(self.edit_stock_entry.get())

        database.update_plant(plant_id, name, category, price, stock)
        messagebox.showinfo("Success", "Plant details have been updated.")
        self.view_plants_screen()

    def delete_plant(self, plant_id):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this plant?"):
            database.delete_plant(plant_id)
            messagebox.showinfo("Success", "Plant has been deleted.")
            self.view_plants_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def generate_bill_screen(self):
        self.clear_screen()
        tk.Label(self, text="Generate Bill", font=("Arial", 24), bg="#f0f8ff", fg="#000080").pack(pady=20)

        tk.Label(self, text="Plant Name", bg="#f0f8ff", fg="#000080").pack()
        self.bill_plant_name_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.bill_plant_name_entry.pack(pady=5)

        tk.Label(self, text="Category", bg="#f0f8ff", fg="#000080").pack()

        # Create a combobox for category selection
        self.bill_category_var = tk.StringVar()
        self.bill_category_combobox = ttk.Combobox(self, textvariable=self.bill_category_var)
        self.bill_category_combobox['values'] = ["","Flower", "Tree", "Fruit", "Vegetable","Seasonal Plants (Mausami Podhe)","Citrus Plants (Narangi ke Podhe)","Shade Plants (Chhaya Mein Ugnay Wale)","Herbaceous Plants (Ghani Patte Wale Podhe)"]
        self.bill_category_combobox.current(0)  # Set default selection
        self.bill_category_combobox.pack(pady=5)

        tk.Label(self, text="Price", bg="#f0f8ff", fg="#000080").pack()
        self.bill_price_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.bill_price_entry.pack(pady=5)

        tk.Label(self, text="Quantity", bg="#f0f8ff", fg="#000080").pack()
        self.bill_quantity_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.bill_quantity_entry.pack(pady=5)

        tk.Button(self, text="Generate Bill", command=self.generate_bill, bg="#4CAF50", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="Back", command=self.admin_menu, bg="#FFC107", fg="#000000").pack(pady=10)

    def generate_bill(self):
        try:
            name = self.bill_plant_name_entry.get()
            category = self.bill_category_var.get()  # Get selected category from combobox
            price = float(self.bill_price_entry.get())
            quantity = int(self.bill_quantity_entry.get())
            total = price * quantity

            # Assuming database.add_bill() is defined elsewhere
            bill_id = database.add_bill(name, category, price, quantity, total, datetime.now())
            messagebox.showinfo("Bill Generated", f"Bill ID: {bill_id}\nTotal Amount: ₹{total:.2f}")
            self.admin_menu()  # Navigate back to admin menu
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data.")

    def view_bills_screen(self):
        self.clear_screen()
        tk.Label(self, text="All Bills", font=("Arial", 24), bg="#f0f8ff", fg="#000080").pack(pady=20)

        bills = database.get_bills()

        for bill in bills:
            bill_frame = tk.Frame(self, bg="#e3f2fd")
            bill_frame.pack(pady=5, fill='x')

            bill_info = f"Bill ID: {bill[0]} | Plant: {bill[1]} | Quantity: {bill[4]} | Total: ₹{bill[5]:.2f} | Date: {bill[6]}"
            tk.Label(bill_frame, text=bill_info, bg="#e3f2fd").pack(side='left')

        tk.Button(self, text="Back", command=self.admin_menu, bg="#FFC107", fg="#000000").pack(pady=10)

    def manage_customers_screen(self):
        self.clear_screen()
        tk.Label(self, text="Manage Customers", font=("Arial", 24), bg="#f0f8ff", fg="#000080").pack(pady=20)
        tk.Button(self, text="Add Customer", command=self.add_customer_screen, bg="#2196F3", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="View Customers", command=self.view_customers_screen, bg="#2196F3", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="Back", command=self.admin_menu, bg="#FFC107", fg="#000000").pack(pady=10)

    def add_customer_screen(self):
        self.clear_screen()
        tk.Label(self, text="Add New Customer", font=("Arial", 24), bg="#f0f8ff", fg="#000080").pack(pady=20)

        tk.Label(self, text="Customer Name", bg="#f0f8ff", fg="#000080").pack()
        self.customer_name_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.customer_name_entry.pack(pady=5)

        tk.Label(self, text="Contact Number", bg="#f0f8ff", fg="#000080").pack()
        self.contact_number_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.contact_number_entry.pack(pady=5)

        tk.Label(self, text="Email", bg="#f0f8ff", fg="#000080").pack()
        self.email_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.email_entry.pack(pady=5)

        tk.Button(self, text="Add Customer", command=self.add_customer, bg="#4CAF50", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="Back", command=self.manage_customers_screen, bg="#FFC107", fg="#000000").pack(pady=10)

    def add_customer(self):
        name = self.customer_name_entry.get()
        contact_number = self.contact_number_entry.get()
        email = self.email_entry.get()

        database.add_customer(name, contact_number, email)
        messagebox.showinfo("Success", f"Customer {name} has been added.")
        self.manage_customers_screen()

    def view_customers_screen(self):
        self.clear_screen()
        tk.Label(self, text="All Customers", font=("Arial", 24), bg="#f0f8ff", fg="#000080").pack(pady=20)

        customers = database.get_customers()

        for customer in customers:
            customer_frame = tk.Frame(self, bg="#e3f2fd")
            customer_frame.pack(pady=5, fill='x')

            customer_info = f"Name: {customer[1]} | Contact: {customer[2]} | Email: {customer[3]}"
            tk.Label(customer_frame, text=customer_info, bg="#e3f2fd").pack(side='left')

            edit_button = tk.Button(customer_frame, text="Edit", command=lambda c=customer: self.edit_customer_screen(c), bg="#FFC107", fg="#000000")
            edit_button.pack(side='left', padx=5)

            delete_button = tk.Button(customer_frame, text="Delete", command=lambda c=customer: self.delete_customer(c[0]), bg="#f44336", fg="#ffffff")
            delete_button.pack(side='left', padx=5)

        tk.Button(self, text="Back", command=self.manage_customers_screen, bg="#FFC107", fg="#000000").pack(pady=10)

    def edit_customer_screen(self, customer):
        self.clear_screen()
        tk.Label(self, text="Edit Customer", font=("Arial", 24), bg="#f0f8ff", fg="#000080").pack(pady=20)

        tk.Label(self, text="Customer Name", bg="#f0f8ff", fg="#000080").pack()
        self.edit_customer_name_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.edit_customer_name_entry.insert(0, customer[1])
        self.edit_customer_name_entry.pack(pady=5)

        tk.Label(self, text="Contact Number", bg="#f0f8ff", fg="#000080").pack()
        self.edit_contact_number_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.edit_contact_number_entry.insert(0, customer[2])
        self.edit_contact_number_entry.pack(pady=5)

        tk.Label(self, text="Email", bg="#f0f8ff", fg="#000080").pack()
        self.edit_email_entry = tk.Entry(self, bg="#ffffff", fg="#000000")
        self.edit_email_entry.insert(0, customer[3])
        self.edit_email_entry.pack(pady=5)

        tk.Button(self, text="Save Changes", command=lambda: self.update_customer(customer[0]), bg="#4CAF50", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="Back", command=self.view_customers_screen, bg="#FFC107", fg="#000000").pack(pady=10)

    def update_customer(self, customer_id):
        name = self.edit_customer_name_entry.get()
        contact_number = self.edit_contact_number_entry.get()
        email = self.edit_email_entry.get()

        database.update_customer(customer_id, name, contact_number, email)
        messagebox.showinfo("Success", "Customer details have been updated.")
        self.view_customers_screen()

    def delete_customer(self, customer_id):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this customer?"):
            database.delete_customer(customer_id)
            messagebox.showinfo("Success", "Customer has been deleted.")
            self.view_customers_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    
    


if __name__ == "__main__":
    
    app = AdminApp()
    app.mainloop()

    
