import tkinter as tk
from tkinter import messagebox
from controller import Controller  # make sure controller.py is in same directory or in PYTHONPATH

class CashierLoginSignupGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cashier Login / Signup")
        self.root.geometry("400x300")
        self.controller = Controller()

        self.mode = "login"  # or "signup"
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Cashier Login", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.username_label = tk.Label(self.root, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.action_button = tk.Button(self.root, text="Login", command=self.perform_action)
        self.action_button.pack(pady=10)

        self.toggle_button = tk.Button(self.root, text="Don't have an account? Sign up", command=self.toggle_mode)
        self.toggle_button.pack()

    def perform_action(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if self.mode == "login":
            success = self.controller.login_cashier(username, password)
            if success:
                messagebox.showinfo("Success", "Login successful!")
                self.root.destroy()
                # Redirect to cashier view here if needed
            else:
                messagebox.showerror("Error", "Invalid credentials.")
        else:
            success, msg = self.controller.signup_cashier(username, password)
            if success:
                messagebox.showinfo("Success", msg)
                self.toggle_mode()  # go back to login screen
            else:
                messagebox.showerror("Error", msg)

    def toggle_mode(self):
        if self.mode == "login":
            self.mode = "signup"
            self.title_label.config(text="Cashier Sign Up")
            self.action_button.config(text="Sign Up")
            self.toggle_button.config(text="Already have an account? Login")
        else:
            self.mode = "login"
            self.title_label.config(text="Cashier Login")
            self.action_button.config(text="Login")
            self.toggle_button.config(text="Don't have an account? Sign up")

if __name__ == "__main__":
    root = tk.Tk()
    app = CashierLoginSignupGUI(root)
    root.mainloop()
