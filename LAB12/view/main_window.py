import tkinter as tk
from tkinter import messagebox
from view.admin_view import AdminView
from view.cashier_view import CashierView
from controller.controller import Controller

class MainWindow:
    def __init__(self, root):
        self.controller = Controller()
        self.root = root
        self.root.title("Smart Mart Management System")
        self.root.geometry("400x300")
        self.root.configure(bg="lightblue")
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Smart Mart", font=("Arial", 20), bg="lightblue").pack(pady=20)

        tk.Button(self.root, text="Login as Admin", command=self.login_admin, width=20).pack(pady=10)
        tk.Button(self.root, text="Login as Cashier", command=self.login_cashier, width=20).pack(pady=10)

    def login_admin(self):
        # Hardcoded admin login (from admin.txt, optionally)
        # For now, direct access
        self.root.withdraw()
        new_win = tk.Toplevel()
        AdminView(new_win, self.controller)

    def login_cashier(self):
        def validate():
            username = username_entry.get()
            password = password_entry.get()
            if self.controller.login_cashier(username, password):
                self.root.withdraw()
                new_win = tk.Toplevel()
                CashierView(new_win, self.controller)
            else:
                messagebox.showerror("Login Failed", "Invalid credentials")

        login_win = tk.Toplevel()
        login_win.title("Cashier Login")
        login_win.geometry("300x200")

        tk.Label(login_win, text="Username:").pack(pady=5)
        username_entry = tk.Entry(login_win)
        username_entry.pack()

        tk.Label(login_win, text="Password:").pack(pady=5)
        password_entry = tk.Entry(login_win, show="*")
        password_entry.pack()

        tk.Button(login_win, text="Login", command=validate).pack(pady=10)
