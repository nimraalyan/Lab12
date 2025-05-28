import tkinter as tk
from tkinter import messagebox

class AdminView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("500x500")
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Admin Panel", font=("Arial", 18)).pack(pady=10)

        # Product Management
        tk.Label(self.root, text="Product ID").pack()
        self.pid_entry = tk.Entry(self.root)
        self.pid_entry.pack()

        tk.Label(self.root, text="Name").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="Price").pack()
        self.price_entry = tk.Entry(self.root)
        self.price_entry.pack()

        tk.Label(self.root, text="Category").pack()
        self.category_entry = tk.Entry(self.root)
        self.category_entry.pack()

        tk.Button(self.root, text="Add Product", command=self.add_product).pack(pady=5)
        tk.Button(self.root, text="Delete Product", command=self.delete_product).pack(pady=5)

        # Cashier Management
        tk.Label(self.root, text="New Cashier Username").pack()
        self.cashier_user = tk.Entry(self.root)
        self.cashier_user.pack()

        tk.Label(self.root, text="Password").pack()
        self.cashier_pass = tk.Entry(self.root)
        self.cashier_pass.pack()

        tk.Button(self.root, text="Add Cashier", command=self.add_cashier).pack(pady=10)

    def add_product(self):
        pid = self.pid_entry.get()
        name = self.name_entry.get()
        price = self.price_entry.get()
        category = self.category_entry.get()
        success, msg = self.controller.add_product(pid, name, price, category)
        messagebox.showinfo("Add Product", msg)

    def delete_product(self):
        pid = self.pid_entry.get()
        success, msg = self.controller.delete_product(pid)
        messagebox.showinfo("Delete Product", msg)

    def add_cashier(self):
        username = self.cashier_user.get()
        password = self.cashier_pass.get()
        success, msg = self.controller.add_cashier(username, password)
        messagebox.showinfo("Add Cashier", msg)
