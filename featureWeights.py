
weights = {
    'INTERESTCALCULATIONMETHOD': {'simple': 1, 'compound': 1.3, 'continuously compound': 13},
    'HASCUSTOMSCHEDULE': {False: 1, True: 1.3},
    'ACCRUEINTERESTAFTERMATURITY': {False: 1, True: 1.3},
    'LINEOFCREDITKEY': {1: 1.01, 2: 1.04, 3: 1.05, 4: 1.07, 5: 1.09, 6: 1.11, 7: 1.13, 8: 1.15, 9: 1.16, 10:1.19},
    'ALLOWARBITRARYFEES': {False: 1, True: 1.3},
    'ACCOUNTLINKINGENABLED': {False: 1, True: 1.3},
    'SCHEDULEDUEDATESMETHOD': {'interval': 1, 'conditional': 1.1, 'function': 5, 'fractional': 1.3, 'workday': 1.4},
    'TAXESONPENALTYENABLED': {False: 1, True: 1.3}
}