class Product:
    def __init__(self, pid, name, price, category):
        self.pid = pid
        self.name = name
        self.price = price
        self.category = category

    def to_line(self):
        return f"{self.pid},{self.name},{self.price},{self.category}\n"

    @staticmethod
    def from_line(line):
        pid, name, price, category = line.strip().split(",")
        return Product(pid, name, float(price), category)


class ProductModel:
    def __init__(self, filepath="data/products.txt"):
        self.filepath = filepath

    def load_products(self):
        with open(self.filepath, "r") as f:
            return [Product.from_line(line) for line in f]

    def add_product(self, product):
        with open(self.filepath, "a") as f:
            f.write(product.to_line())
