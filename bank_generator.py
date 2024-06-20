import random
import pandas as pd
import numpy as np
import time

class Product:
    def __init__(self, name, interest_rate, penalties_range, term_range, is_revolving, repayment_schedule, interest_calc):
        self.name = name
        self.interest_rate = interest_rate
        self.penalties_range = penalties_range
        self.term_range = term_range
        self.is_revolving = is_revolving
        self.repayment_schedule = repayment_schedule
        self.interest_calc = interest_calc

    def generate_random_penalties(self):
        return random.choice(self.penalties_range)

    def generate_random_term(self):
        if isinstance(self.term_range, tuple):
            return random.randint(*self.term_range)
        return self.term_range

class Bank:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.accounts = []

    def add_product(self, product):
        self.products.append(product)

    def generate_accounts(self, num_accounts):
        for _ in range(num_accounts):
            product = random.choice(self.products)
            if product.is_revolving:
                eod_processing_time = random.uniform(0.3, 0.5)  
            else:
                eod_processing_time = random.uniform(0.05, 0.2)  
            self.accounts.append(Account(f"Account_{len(self.accounts) + 1}", self, product, eod_processing_time))

class Account:
    def __init__(self, name, bank, product, eod_processing_time):
        self.name = name
        self.bank = bank
        self.product = product
        self.penalties = product.generate_random_penalties()
        self.term = product.generate_random_term()
        self.eod_processing_time = eod_processing_time

start_time = time.time()

# Define the products as shown in the image with variable features
mortgage_a = Product("Mortgage A", 3.2, [0, 1], 360, 0, "month", 12)
mortgage_b = Product("Mortgage B", 4.7, [0, 1], 180, 0, "month", 12)
revolving_loan = Product("Revolving Loan", 20.1, [0, 1], (0, 100), 1, "flexible", 365)
personal_loan = Product("Personal Loan", 8, [0, 1], (0, 100), 0, "month", 12)
student_loan = Product("Student Loan", 5, [0, 1], (0, 120), 0, "month", 12)

# Define the list of product types
product_types = [mortgage_a, mortgage_b, revolving_loan, personal_loan, student_loan]

# Create 100 banks
banks = [Bank(f"Bank_{i + 1}") for i in range(100)]

# Assign random distributions of products to each bank
for bank in banks:
    selected_products = random.sample(product_types, k=random.randint(1, len(product_types)))
    for product in selected_products:
        bank.add_product(product)

# Generate a normally distributed number of accounts for each bank
num_accounts_mean = 300000
num_accounts_std = 30000

for bank in banks:
    num_accounts = max(1, int(np.random.normal(num_accounts_mean, num_accounts_std)))
    if random.random() < 0.05:  
        num_accounts = int(np.random.normal(num_accounts_mean * 3, num_accounts_std * 2))
    bank.generate_accounts(num_accounts)

# Convert accounts data to pandas DataFrame
data = []
for bank in banks:
    for account in bank.accounts:
        data.append({
            "Account": account.name,
            "Bank": account.bank.name,
            "Product": account.product.name,
            "Interest Rate": account.product.interest_rate,
            "Penalties": account.penalties,
            "Term": account.term,
            "Is Revolving": account.product.is_revolving,
            "Repayment Schedule": account.product.repayment_schedule,
            "Interest Calculation": account.product.interest_calc,
            "EOD Processing Time": account.eod_processing_time
        })

df = pd.DataFrame(data)
df.to_csv('out.csv')
bank_eod_sum = df.groupby('Bank')['EOD Processing Time'].sum()

# Timing complete process
end_time = time.time()
total_time = end_time - start_time
print(f"Total processing time: {total_time} seconds")


