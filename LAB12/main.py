import tkinter as tk
from admin_login import AdminLoginGUI

from cashier_login_signup import CashierLoginSignupGUI

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Mart Management System")
        self.root.geometry("400x250")
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Smart Mart Management System", font=("Arial", 16))
        title.pack(pady=20)

        admin_btn = tk.Button(self.root, text="Admin Login", width=25, command=self.open_admin_login)
        admin_btn.pack(pady=10)

        cashier_btn = tk.Button(self.root, text="Cashier Login / Signup", width=25, command=self.open_cashier_login)
        cashier_btn.pack(pady=10)

        exit_btn = tk.Button(self.root, text="Exit", width=25, command=self.root.quit)
        exit_btn.pack(pady=10)

    def open_admin_login(self):
        self.root.withdraw()
        admin_root = tk.Toplevel()
        AdminLoginGUI(admin_root)
        admin_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(admin_root))

    def open_cashier_login(self):
        self.root.withdraw()
        cashier_root = tk.Toplevel()
        CashierLoginSignupGUI(cashier_root)
        cashier_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(cashier_root))

    def on_close(self, window):
        window.destroy()
        self.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()
