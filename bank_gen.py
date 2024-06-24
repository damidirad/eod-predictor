from bank import *
import random
import time
import pandas as pd
from featureWeights import weights

# Auxiliary functions
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

# Number of banks to be generated
num_banks = 100
banks = [Bank(f"Bank_{i + 1}") for i in range(num_banks)]

# Number of product types to be generated
num_products = 8
product_types = generate_products(8)
data = []
lp_data = []

total_accounts_per_bank = 500000

# GENERATION CODE DO NOT TOUCH
for bank in banks:
    selected_products = random.sample(product_types, k=random.randint(3, len(product_types)))
    total_accs = 0
    remaining_accounts = total_accounts_per_bank

    for i, product in enumerate(selected_products):
        bank.add_product(product)
        if i == len(selected_products) - 1:
            num_accs = remaining_accounts  
        else:
            num_accs = random.randint(int(remaining_accounts * 0.1), int(remaining_accounts * 0.4))
            remaining_accounts -= num_accs

        total_accs += num_accs
        accs = generate_accounts(num_accs, product)
        for acc in accs:
            bank.add_account(acc)
            time_multiplier = (
                    weights['ALLOWARBITRARYFEES'][product.ALLOWARBITRARYFEES] *
                    weights['ACCOUNTLINKINGENABLED'][product.ACCOUNTLINKINGENABLED] *
                    weights['SCHEDULEDUEDATESMETHOD'][product.SCHEDULEDUEDATESMETHOD] *
                    weights['TAXESONPENALTYENABLED'][product.TAXESONPENALTYENABLED] *
                    weights['INTERESTCALCULATIONMETHOD'][acc.INTERESTCALCULATIONMETHOD] *
                    weights['HASCUSTOMSCHEDULE'][acc.HASCUSTOMSCHEDULE] *
                    weights['ACCRUEINTERESTAFTERMATURITY'][acc.ACCRUEINTERESTAFTERMATURITY]
                )
            acc_time = random.uniform(0.45, 0.55) * time_multiplier
            bank.loan_processing_time += acc_time
            
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
                "ACCRUEINTERESTAFTERMATURITY": acc.ACCRUEINTERESTAFTERMATURITY,
                "ACCOUNTLOANPROCESSINGTIME": acc_time
            })
    bank.loan_processing_time = int(bank.loan_processing_time)
    lp_data.append({
        'BANK': bank.name,
        'NUMACCOUNTS': total_accs,
        "LOANPROCESSINGTIME": bank.loan_processing_time
    })
    print(f"Timestamp: {time.time() - start_time} seconds since start || {bank.name} generation complete with a processing time of {bank.loan_processing_time} milliseconds for {total_accs} accounts")

df = pd.DataFrame(data)
df.to_csv('bank.csv', index=False)
pd.DataFrame(lp_data).to_csv('processing_time.csv', index=False)
print(f"Data generation completed in {time.time() - start_time} seconds.\n"
      "Please find the generated data in 'bank.csv' and 'processing_time.csv'.")