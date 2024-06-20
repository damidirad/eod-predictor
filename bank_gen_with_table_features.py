from bank import *
import random
import time
import pandas as pd

def generate_products(n):
    products = []
    for i in range(1, n+1):
        products.append(Product(PRODUCTNAME=f"Product_{i}", 
                                ALLOWARBITRARYFEES=random.choices([True, False],
                                                                 weights=[0.6, 0.4])[0],
                                ACCOUNTLINKINGENABLED=random.choices([True, False],
                                                                     weights=[0.6, 0.4])[0],
                                SCHEDULEDUEDATESMETHOD=random.choices(['conditional', 'interval', 'function', 'fractional', 'workday'],
                                                                      weights=[0.3, 0.2, 0.1, 0.3, 0.1])[0],
                                TAXESONPENALTYENABLED=random.choices([True, False],
                                                                    weights=[0.4, 0.6])[0]))
    return products

def generate_accounts(n, product):
    accounts = []
    for i in range(1, n+1):
        accounts.append(Account(product=product,
                                ACCOUNTHOLDERKEY=f"Account_{i}", 
                                INTERESTCALCULATIONMETHOD=random.choices(['simple', 'compound', 'continuously compound'],
                                                                 weights=[0.5, 0.3, 0.2])[0],
                                HASCUSTOMSCHEDULE=random.choices([True, False],
                                                                     weights=[0.6, 0.4])[0],
                                LINEOFCREDITKEY=str(random.randint(0, 10)),
                                ACCRUEINTERESTAFTERMATURITY=random.choices([True, False],
                                                                    weights=[0.4, 0.6])[0]))
    return accounts

start_time = time.time()

banks = [Bank(f"Bank_{i + 1}") for i in range(50)]

product_types = generate_products(10)
data = []

for bank in banks:
    selected_products = random.sample(product_types, k=random.randint(3, len(product_types)))
    for product in selected_products:
        bank.add_product(product)
        accs = generate_accounts(random.randint(40000, 150000), product)
        for acc in accs:
            bank.add_account(acc)
            data.append({
                "BANK": bank.name,
                "ACCOUNTHOLDERKEY": acc.ACCOUNTHOLDERKEY,
                "PRODUCTNAME": product.PRODUCTNAME,
                "ALLOWARBITRARYFEES": product.ALLOWARBITRARYFEES,
                "ACCOUNTLINKINGENABLED": product.ACCOUNTLINKINGENABLED,
                "SCHEDULEDUEDATESMETHOD": product.SCHEDULEDUEDATESMETHOD,
                "TAXESONPENALTYENABLED": product.TAXESONPENALTYENABLED,
                "INTERESTCALCULATIONMETHOD": acc.INTERESTCALCULATIONMETHOD,
                "HASCUSTOMSCHEDULE": acc.HASCUSTOMSCHEDULE,
                "LINEOFCREDITKEY": acc.LINEOFCREDITKEY,
                "ACCRUEINTERESTAFTERMATURITY": acc.ACCRUEINTERESTAFTERMATURITY
            })
    print(time.time(), bank.name)
df = pd.DataFrame(data)
df.to_csv('bank.csv')
print(f"Data generation completed in {time.time() - start_time} seconds")