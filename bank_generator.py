import random
import pandas as pd
import numpy as np

class Product:
    def __init__(self, name, interest_rate, penalties_range, duration_range, is_revolving, repayment_schedule, interest_calc):
        self.name = name
        self.interest_rate = interest_rate
        self.penalties_range = penalties_range
        self.duration_range = duration_range
        self.is_revolving = is_revolving
        self.repayment_schedule = repayment_schedule
        self.interest_calc = interest_calc

    def generate_random_penalties(self):
        return random.choice(self.penalties_range)

    def generate_random_duration(self):
        if isinstance(self.duration_range, tuple):
            return random.randint(*self.duration_range)
        return self.duration_range

class Bank:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.clients = []

    def add_product(self, product):
        self.products.append(product)

    def generate_clients(self, num_clients):
        for _ in range(num_clients):
            product = random.choice(self.products)
            self.clients.append(User(f"Client_{len(self.clients) + 1}", self, product))

    def calculate_eod_processing_time(self):
        revolving_loan_clients = sum(1 for client in self.clients if client.product.name == "Revolving Loan")
        other_clients = len(self.clients) - revolving_loan_clients
        # Higher weight for revolving loan clients
        return revolving_loan_clients * 0.2 + other_clients * 0.05

class User:
    def __init__(self, name, bank, product):
        self.name = name
        self.bank = bank
        self.product = product
        self.penalties = product.generate_random_penalties()
        self.duration = product.generate_random_duration()

# Define the products as shown in the image with variable features
hypotheek_a = Product("Hypotheek A", 3.2, [0, 1], 360, 0, "maand", 12)
hypotheek_b = Product("Hypotheek B", 4.7, [0, 1], 180, 0, "maand", 12)
revolving_loan = Product("Revolving Loan", 20.1, [0, 1], (0, 100), 0, "Flexible", 365)
persoonlijke_lening = Product("Persoonlijke Lening", 8, [0, 1], (0, 100), 0, "maand", 12)
studie_lening = Product("Studie Lening", 5, [0, 1], (0, 120), 0, "maand", 12)

# Define the list of product types
product_types = [hypotheek_a, hypotheek_b, revolving_loan, persoonlijke_lening, studie_lening]

# Create 100 banks
banks = [Bank(f"Bank_{i + 1}") for i in range(100)]

# Assign random distributions of products to each bank
for bank in banks:
    selected_products = random.sample(product_types, k=random.randint(1, len(product_types)))
    for product in selected_products:
        bank.add_product(product)

# Generate a normally distributed number of clients for each bank
num_clients_mean = 1500000
num_clients_std = 500000

for bank in banks:
    num_clients = max(1, int(np.random.normal(num_clients_mean, num_clients_std)))
    bank.generate_clients(num_clients)

# Convert users data to pandas DataFrame
data = []
for bank in banks:
    eod_processing_time = bank.calculate_eod_processing_time()
    for user in bank.clients:
        data.append({
            "User": user.name,
            "Bank": user.bank.name,
            "Product": user.product.name,
            "Interest Rate": user.product.interest_rate,
            "Penalties": user.penalties,
            "Duration": user.duration,
            "Is Revolving": user.product.is_revolving,
            "Repayment Schedule": user.product.repayment_schedule,
            "Interest Calculation": user.product.interest_calc,
            "EOD Processing Time": eod_processing_time
        })

df = pd.DataFrame(data)
print(df)