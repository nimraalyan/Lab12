import tkinter as tk
from tkinter import messagebox

class CashierView:
    def __init__(self, root, controller):
        self.controller = controller
        self.cart = []
        self.total = 0.0
        self.root = root
        self.root.title("Cashier Interface")
        self.root.geometry("500x500")
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Cashier Panel", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="Load Products", command=self.load_products).pack(pady=5)

        self.products_list = tk.Listbox(self.root, width=50)
        self.products_list.pack(pady=5)

        tk.Button(self.root, text="Add to Cart", command=self.add_to_cart).pack(pady=5)

        self.cart_list = tk.Listbox(self.root, width=50)
        self.cart_list.pack(pady=5)

        tk.Button(self.root, text="Checkout", command=self.checkout).pack(pady=10)

    def load_products(self):
        self.products_list.delete(0, tk.END)
        for p in self.controller.get_all_products():
            self.products_list.insert(tk.END, f"{p.pid} - {p.name} - ${p.price}")

    def add_to_cart(self):
        selected = self.products_list.get(tk.ACTIVE)
        if selected:
            parts = selected.split("-")
            price = float(parts[-1].strip().replace("$", ""))
            self.total += price
            self.cart.append(selected)
            self.cart_list.insert(tk.END, selected)

    def checkout(self):
        if self.total == 0:
            messagebox.showwarning("Cart Empty", "No items in the cart.")
            return
        self.controller.save_bill(self.total)
        messagebox.showinfo("Checkout", f"Total Bill: ${self.total:.2f}")
        self.cart_list.delete(0, tk.END)
        self.total = 0.0
        self.cart.clear()
