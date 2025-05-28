import tkinter as tk
from tkinter import messagebox

class AdminLoginGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Login")
        self.master.geometry("300x200")

        # Labels
        tk.Label(master, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=5)

        tk.Label(master, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=5)

        # Login button
        tk.Button(master, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Hardcoded credentials (replace with file/db check for real use)
        if username == "admin" and password == "admin123":
            messagebox.showinfo("Login Successful", "Welcome Admin!")
            # Proceed to admin dashboard or main menu
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
