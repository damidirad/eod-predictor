# loanaccount;INTERESTCALCULATIONMETHOD;simple;0.00
# loanaccount;INTERESTCALCULATIONMETHOD;compound;0.30
# loanaccount;INTERESTCALCULATIONMETHOD;continuously compound;0.70
# loanaccount;HASCUSTOMSCHEDULE;False;0.00
# loanaccount;HASCUSTOMSCHEDULE;True;1.00
# loanaccount;ACCRUEINTERESTAFTERMATURITY;False;0.00
# loanaccount;ACCRUEINTERESTAFTERMATURITY;True;1.00
# loanaccount;LINEOFCREDITKEY;1;0.01
# loanaccount;LINEOFCREDITKEY;2;0.04
# loanaccount;LINEOFCREDITKEY;3;0.05
# loanaccount;LINEOFCREDITKEY;4;0.07
# loanaccount;LINEOFCREDITKEY;5;0.09
# loanaccount;LINEOFCREDITKEY;6;0.11
# loanaccount;LINEOFCREDITKEY;7;0.13
# loanaccount;LINEOFCREDITKEY;8;0.15
# loanaccount;LINEOFCREDITKEY;9;0.16
# loanaccount;LINEOFCREDITKEY;10;0.19
# loanproduct;ALLOWARBITRARYFEES;False;0.00
# loanproduct;ALLOWARBITRARYFEES;True;1.00
# loanproduct;ACCOUNTLINKINGENABLED;False;0.00
# loanproduct;ACCOUNTLINKINGENABLED;True;1.00
# loanproduct;SCHEDULEDUEDATESMETHOD;interval;0.00
# loanproduct;SCHEDULEDUEDATESMETHOD;conditional;0.10
# loanproduct;SCHEDULEDUEDATESMETHOD;function;0.20
# loanproduct;SCHEDULEDUEDATESMETHOD;fractional;0.30
# loanproduct;SCHEDULEDUEDATESMETHOD;workday;0.40
# loanproduct;TAXESONPENALTYENABLED;False;0.00
# loanproduct;TAXESONPENALTYENABLED;True;1.00

weights = {
    'INTERESTCALCULATIONMETHOD': {'simple': 1, 'compound': 1.3, 'continuously compound': 1.7},
    'HASCUSTOMSCHEDULE': {False: 1, True: 2},
    'ACCRUEINTERESTAFTERMATURITY': {False: 1, True: 2},
    'LINEOFCREDITKEY': {1: 1.01, 2: 1.04, 3: 1.05, 4: 1.07, 5: 1.09, 6: 1.11, 7: 1.13, 8: 1.15, 9: 1.16, 10:1.19},
    'ALLOWARBITRARYFEES': {False: 1, True: 2},
    'ACCOUNTLINKINGENABLED': {False: 1, True: 2},
    'SCHEDULEDUEDATESMETHOD': {'interval': 1, 'conditional': 1.1, 'function': 1.2, 'fractional': 1.3, 'workday': 1.4},
    'TAXESONPENALTYENABLED': {False: 1, True: 2}
}