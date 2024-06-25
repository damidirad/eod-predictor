from data.bank import *
import random
import time
import pandas as pd
from data.feature_weights import weights

# Product generator with four selected features for demonstration
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

# Account generator with four selected features for demonstration
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

# Bank generator
def generate_banks(n_banks, n_products, acc_per_bank):
    banks = [Bank(f"Bank_{i + 1}") for i in range(n_banks)]
    product_types = generate_products(n_products)
    account_data = []
    bank_data = []

    for bank in banks:
        # Generate between 3 and n_products products for each bank
        selected_products = random.sample(product_types, k=random.randint(3, len(product_types)))
        total_accs = 0
        remaining_accounts = acc_per_bank
    
        for i, product in enumerate(selected_products):
            bank.add_product(product)
            # Distribute accounts over bank products
            if i == len(selected_products) - 1:
                num_accs = remaining_accounts  
            else:
                num_accs = random.randint(int(remaining_accounts * 0.1), int(remaining_accounts * 0.4))
                remaining_accounts -= num_accs

            total_accs += num_accs 
            accs = generate_accounts(num_accs, product)
            for acc in accs:
                bank.add_account(acc)
                # Calculate multiplier to increase base processing time based on simulated feature importance
                time_multiplier = (
                    weights['ALLOWARBITRARYFEES'][product.ALLOWARBITRARYFEES] *
                    weights['ACCOUNTLINKINGENABLED'][product.ACCOUNTLINKINGENABLED] *
                    weights['SCHEDULEDUEDATESMETHOD'][product.SCHEDULEDUEDATESMETHOD] *
                    weights['TAXESONPENALTYENABLED'][product.TAXESONPENALTYENABLED] *
                    weights['INTERESTCALCULATIONMETHOD'][acc.INTERESTCALCULATIONMETHOD] *
                    weights['HASCUSTOMSCHEDULE'][acc.HASCUSTOMSCHEDULE] *
                    weights['ACCRUEINTERESTAFTERMATURITY'][acc.ACCRUEINTERESTAFTERMATURITY]
                )
                # Base account processing time is randomly generated between values to add more variation to simulated data
                acc_time = random.uniform(0.45, 0.55) * time_multiplier
                bank.loan_processing_time += acc_time
                # Store generated account data
                account_data.append({
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
        # Store generated bank data
        bank_data.append({
            "BANK": bank.name,
            "NUMACCOUNT": total_accs,
            "LOANPROCESSINGTIME": bank.loan_processing_time
        })
        print(f"Timestamp: {time.time() - start_time} seconds since start || {bank.name} generation complete with a processing time of {bank.loan_processing_time} milliseconds for {total_accs} accounts")
    return account_data, bank_data

# Generate 100 banks, 8 products and 500000 accounts per bank
account_data, bank_data = generate_banks(100, 8, 500000)

# Store generated data in dataframes to use in model
df = pd.DataFrame(account_data)
df.to_csv('account_data.csv', index=False)
pd.DataFrame(bank_data).to_csv('bank_data.csv', index=False)
print(f"Data generation completed in {time.time() - start_time} seconds.\n"
      "Please find the generated data in 'bank.csv' and 'processing_time.csv'.")