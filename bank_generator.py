import random
import pandas as pd
import numpy as np
import time

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
            if product.is_revolving:
                eod_processing_time = random.uniform(0.3, 0.5)  
            else:
                eod_processing_time = random.uniform(0.05, 0.2)  
            self.clients.append(User(f"Client_{len(self.clients) + 1}", self, product, eod_processing_time))

class User:
    def __init__(self, name, bank, product, eod_processing_time):
        self.name = name
        self.bank = bank
        self.product = product
        self.penalties = product.generate_random_penalties()
        self.duration = product.generate_random_duration()
        self.eod_processing_time = eod_processing_time

start_time = time.time()

# Define the products as shown in the image with variable features
hypotheek_a = Product("Mortgage A", 3.2, [0, 1], 360, 0, "month", 12)
hypotheek_b = Product("Mortgage B", 4.7, [0, 1], 180, 0, "month", 12)
revolving_loan = Product("Revolving Loan", 20.1, [0, 1], (0, 100), 1, "flexible", 365)
persoonlijke_lening = Product("Personal Loan", 8, [0, 1], (0, 100), 0, "month", 12)
studie_lening = Product("Student Loan", 5, [0, 1], (0, 120), 0, "month", 12)

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
num_clients_mean = 300000
num_clients_std = 80000

for bank in banks:
    num_clients = max(1, int(np.random.normal(num_clients_mean, num_clients_std)))
    if random.random() < 0.03:  
        num_clients = int(np.random.normal(num_clients_mean * 3, num_clients_std * 2))
    bank.generate_clients(num_clients)

# Convert users data to pandas DataFrame
data = []
for bank in banks:
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
            "EOD Processing Time": user.eod_processing_time
        })

df = pd.DataFrame(data)
df.to_csv('out.csv')
bank_eod_sum = df.groupby('Bank')['EOD Processing Time'].sum()

# Timing complete process
end_time = time.time()
total_time = end_time - start_time
print(f"Total processing time: {total_time} seconds")


