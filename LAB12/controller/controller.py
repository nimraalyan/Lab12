import os
class Controller:
    def __init__(self):
        print("Controller initialized")

    # your methods here

    def __init__(self):
        self.products_file = "products.txt"
        self.cashiers_file = "cashiers.txt"
        self.admin_file = "admin.txt"
        self.bills_file = "bills.txt"

    # ------------------ ADMIN LOGIN ------------------

    def login_admin(self, username, password):
        try:
            with open(self.admin_file, 'r') as file:
                for line in file:
                    u, p = line.strip().split(',')
                    if u == username and p == password:
                        return True
            return False
        except FileNotFoundError:
            return False

    # ------------------ CASHIER LOGIN ------------------

    def login_cashier(self, username, password):
        try:
            with open(self.cashiers_file, 'r') as file:
                for line in file:
                    u, p = line.strip().split(',')
                    if u == username and p == password:
                        return True
            return False
        except FileNotFoundError:
            return False

    # ------------------ CASHIER SIGNUP ------------------

    def signup_cashier(self, username, password):
        if not username or not password:
            return False, "Username and password required"
        
        # Check if cashier already exists
        if self._cashier_exists(username):
            return False, "Cashier already exists"

        try:
            with open(self.cashiers_file, 'a') as file:
                file.write(f"{username},{password}\n")
            return True, "Cashier registered successfully"
        except Exception as e:
            return False, f"Error registering cashier: {str(e)}"

    def _cashier_exists(self, username):
        if not os.path.exists(self.cashiers_file):
            return False
        with open(self.cashiers_file, 'r') as file:
            for line in file:
                u, _ = line.strip().split(',')
                if u == username:
                    return True
        return False

    # ------------------ PRODUCT FUNCTIONS ------------------

    def add_product(self, pid, name, price, category):
        if not pid or not name or not price or not category:
            return False, "All fields are required"

        try:
            with open(self.products_file, 'a') as file:
                file.write(f"{pid},{name},{price},{category}\n")
            return True, "Product added successfully"
        except Exception as e:
            return False, f"Error adding product: {str(e)}"

    def browse_products(self):
        try:
            with open(self.products_file, 'r') as file:
                return [line.strip().split(',') for line in file if line.strip()]
        except FileNotFoundError:
            return []

    # ------------------ BILLING FUNCTIONS ------------------

    def create_bill(self, cart_items):
        try:
            total = sum(float(item[2]) for item in cart_items)
            with open(self.bills_file, 'a') as file:
                file.write(f"{total}\n")
            return total, "Bill saved successfully"
        except Exception as e:
            return 0.0, f"Error saving bill: {str(e)}"
