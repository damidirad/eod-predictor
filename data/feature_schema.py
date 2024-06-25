# Product feature names and constraints
product_schema = {
    'ID': (str, {'max_length': 32}),
    'ACTIVATED': (bool, {}),
    'CREATIONDATE': (str, {}), 
    'DEFAULTGRACEPERIOD': (int, {}),
    'DEFAULTLOANAMOUNT': (float, {}),
    'DEFAULTNUMINSTALLMENTS': (int, {}),
    'DEFAULTREPAYMENTPERIODCOUNT': (int, {}),
    'GRACEPERIODTYPE': (str, {'max_length': 256}),
    'INTERESTCALCULATIONMETHOD': (str, {'max_length': 256}),
    'INTERESTTYPE': (str, {'max_length': 255, 'default': 'SIMPLE_INTEREST'}),
    'REPAYMENTSCHEDULEMETHOD': (str, {'max_length': 256, 'not_null': True, 'default': 'FIXED'}),
    'LASTMODIFIEDDATE': (str, {}), # str used to represent date
    'MAXGRACEPERIOD': (int, {}),
    'MAXLOANAMOUNT': (float, {}),
    'MAXNUMINSTALLMENTS': (int, {}),
    'MAXPENALTYRATE': (float, {}),
    'MINGRACEPERIOD': (int, {}),
    'MINLOANAMOUNT': (float, {}),
    'MINNUMINSTALLMENTS': (int, {}),
    'MINPENALTYRATE': (float, {}),
    'DEFAULTPENALTYRATE': (float, {}),
    'PRODUCTDESCRIPTION': (str, {}),  
    'PRODUCTNAME': (str, {'max_length': 256}),
    'REPAYMENTPERIODUNIT': (str, {'max_length': 256}),
    'PREPAYMENTACCEPTANCE': (str, {'max_length': 256, 'default': 'ACCEPT_PREPAYMENTS'}),
    'INTERESTAPPLICATIONMETHOD': (str, {'max_length': 256, 'not_null': True, 'default': 'ON_DISBURSEMENT'}),
    'ALLOWARBITRARYFEES': (bool, {'not_null': True, 'default': False}),
    'DEFAULTPRINCIPALREPAYMENTINTERVAL': (int, {}),
    'LOANPENALTYCALCULATIONMETHOD': (str, {'max_length': 256, 'default': 'NONE'}),
    'LOANPENALTYGRACEPERIOD': (int, {}),
    'REPAYMENTCURRENCYROUNDING': (str, {'max_length': 256, 'default': 'NO_ROUNDING'}),
    'ROUNDINGREPAYMENTSCHEDULEMETHOD': (str, {'max_length': 256, 'default': 'NO_ROUNDING'}),
    'PREPAYMENTRECALCULATIONMETHOD': (str, {'max_length': 255}),
    'PRINCIPALPAIDINSTALLMENTSTATUS': (str, {'max_length': 255}),
    'DAYSINYEAR': (str, {'max_length': 256, 'default': 'DAYS_365'}),
    'SCHEDULEINTERESTDAYSCOUNTMETHOD': (str, {'max_length': 256}),
    'REPAYMENTALLOCATIONORDER': (bytes, {}),  
    'IDGENERATORTYPE': (str, {'max_length': 256, 'not_null': True, 'default': 'RANDOM_PATTERN'}),
    'IDPATTERN': (str, {'max_length': 256, 'not_null': True, 'default': '@@@@###'}),
    'ACCOUNTINGMETHOD': (str, {'max_length': 256, 'default': 'NONE'}),
    'ACCOUNTLINKINGENABLED': (bool, {'not_null': True, 'default': False}),
    'LINKABLESAVINGSPRODUCTKEY': (str, {'max_length': 32}),
    'AUTOLINKACCOUNTS': (bool, {'not_null': True, 'default': False}),
    'AUTOCREATELINKEDACCOUNTS': (bool, {'not_null': True, 'default': False}),
    'REPAYMENTSCHEDULEEDITOPTIONS': (bytes, {}),  
    'SCHEDULEDUEDATESMETHOD': (str, {'max_length': 256, 'not_null': True, 'default': 'INTERVAL'}),
    'PAYMENTMETHOD': (str, {'max_length': 256, 'not_null': True, 'default': 'HORIZONTAL'}),
    'FIXEDDAYSOFMONTH': (bytes, {}),  
    'SHORTMONTHHANDLINGMETHOD': (str, {'max_length': 256}),
    'TAXESONINTERESTENABLED': (bool, {'not_null': True, 'default': False}),
    'TAXSOURCEKEY': (str, {'max_length': 32}),
    'TAXCALCULATIONMETHOD': (str, {'max_length': 256}),
    'FUTUREPAYMENTSACCEPTANCE': (str, {'max_length': 256, 'not_null': True, 'default': 'NO_FUTURE_PAYMENTS'}),
    'TAXESONFEESENABLED': (bool, {'not_null': True, 'default': False}),
    'TAXESONPENALTYENABLED': (bool, {'not_null': True, 'default': False}),
    'APPLYINTERESTONPREPAYMENTMETHOD': (str, {'max_length': 256}),
    'REPAYMENTELEMENTSROUNDINGMETHOD': (str, {'max_length': 256, 'not_null': True, 'default': 'NO_ROUNDING'}),
    'ELEMENTSRECALCULATIONMETHOD': (str, {'max_length': 256}),
    'DORMANCYPERIODDAYS': (int, {}),
    'LOCKPERIODDAYS': (int, {}),
    'CAPPINGMETHOD': (str, {'max_length': 255}),
    'CAPPINGCONSTRAINTTYPE': (str, {'max_length': 255}),
    'CAPPINGPERCENTAGE': (float, {}),
    'CAPPINGAPPLYACCRUEDCHARGESBEFORELOCKING': (bool, {'not_null': True, 'default': False}),
    'SETTLEMENTOPTIONS': (str, {'max_length': 32, 'not_null': True, 'default': 'FULL_DUE_AMOUNTS'}),
    'OFFSETPERCENTAGE': (float, {}),
    'ACCOUNTINITIALSTATE': (str, {'max_length': 32, 'not_null': True, 'default': 'PENDING_APPROVAL'}),
    'MAXNUMBEROFDISBURSEMENTTRANCHES': (int, {'default': 1}),
    'LATEPAYMENTSRECALCULATIONMETHOD': (str, {'max_length': 256, 'not_null': True, 'default': 'INCREASE_OVERDUE_INSTALLMENTS'}),
    'AMORTIZATIONMETHOD': (str, {'max_length': 32, 'default': 'STANDARD_PAYMENTS'}),
    'INTERESTRATESETTINGSKEY': (str, {'max_length': 32}),
    'LINEOFCREDITREQUIREMENT': (str, {'max_length': 255, 'not_null': True, 'default': 'OPTIONAL'}),
    'PRODUCTSECURITYSETTINGSKEY': (str, {'max_length': 32}),
    'DEFAULTFIRSTREPAYMENTDUEDATEOFFSET': (float, {}),
    'MINFIRSTREPAYMENTDUEDATEOFFSET': (float, {}),
    'MAXFIRSTREPAYMENTDUEDATEOFFSET': (float, {}),
    'INTERESTACCRUEDACCOUNTINGMETHOD': (str, {'max_length': 32, 'not_null': True, 'default': 'NONE'}),
    'LOANPRODUCTTYPE': (str, {'max_length': 255, 'not_null': True, 'default': 'FIXED_TERM_LOAN'}),
    'FORINDIVIDUALS': (bool, {'not_null': True, 'default': False}),
    'FORPUREGROUPS': (bool, {'not_null': True, 'default': False}),
    'FORHYBRIDGROUPS': (bool, {'not_null': True, 'default': False}),
    'FORALLBRANCHES': (bool, {'not_null': True, 'default': True}),
    'PRINCIPALPAYMENTSETTINGSKEY': (str, {'max_length': 32}),
    'REPAYMENTRESCHEDULINGMETHOD': (str, {'max_length': 256, 'not_null': True, 'default': 'NEXT_WORKING_DAY'}),
    'INTERESTBALANCECALCULATIONMETHOD': (str, {'max_length': 32, 'default': 'PRINCIPAL_ONLY'}),
    'ARREARSSETTINGSKEY': (str, {'max_length': 32}),
    'REDRAWSETTINGSKEY': (str, {'max_length': 32}),
    'ALLOWCUSTOMREPAYMENTALLOCATION': (bool, {'not_null': True, 'default': False}),
    'ACCRUELATEINTEREST': (bool, {'not_null': True, 'default': True}),
    'INTERESTACCRUALCALCULATION': (str, {'max_length': 256, 'default': 'NONE'}),
    'CATEGORY': (str, {'max_length': 256}),
    'CURRENCYCODE': (str, {'max_length': 3}),
    'FOUREYESPRINCIPLELOANAPPROVAL': (bool, {'not_null': True, 'default': False}),
}

# Account feature names and constraints
account_schema = {
    'ENCODEDKEY': (str, {'max_length': 32, 'not_null': True}),
    'ACCOUNTHOLDERKEY': (str, {'max_length': 32, 'not_null': True}),
    'ACCOUNTHOLDERTYPE': (str, {'max_length': 256, 'not_null': True}),
    'ACCOUNTSTATE': (str, {'max_length': 256}),
    'ACCOUNTSUBSTATE': (str, {'max_length': 256}),
    'RESCHEDULEDACCOUNTKEY': (str, {'max_length': 32}),
    'ASSIGNEDBRANCHKEY': (str, {'max_length': 32}),
    'ASSIGNEDUSERKEY': (str, {'max_length': 32}),
    'CLOSEDDATE': (str, {}), 
    'LASTLOCKEDDATE': (str, {}),
    'CREATIONDATE': (str, {}), 
    'APPROVEDDATE': (str, {}),  
    'FEESDUE': (float, {}),
    'FEESPAID': (float, {}),
    'GRACEPERIOD': (int, {'not_null': True}),
    'GRACEPERIODTYPE': (str, {'max_length': 256}),
    'ID': (str, {'max_length': 32}),
    'INTERESTCALCULATIONMETHOD': (str, {'max_length': 256}),
    'INTERESTTYPE': (str, {'max_length': 255, 'default': 'SIMPLE_INTEREST'}),
    'REPAYMENTSCHEDULEMETHOD': (str, {'max_length': 256}),
    'INTERESTAPPLICATIONMETHOD': (str, {'max_length': 256}),
    'PAYMENTMETHOD': (str, {'max_length': 256}),
    'INTERESTCHARGEFREQUENCY': (str, {'max_length': 256}),
    'INTERESTBALANCE': (float, {}),
    'INTERESTPAID': (float, {}),
    'INTERESTRATE': (float, {}),
    'LASTMODIFIEDDATE': (str, {}), 
    'LASTSETTOARREARSDATE': (str, {}), 
    'LOANAMOUNT': (float, {}),
    'PERIODICPAYMENT': (float, {'not_null': True, 'default': 0.0}),
    'LOANGROUP_ENCODEDKEY_OID': (str, {'max_length': 32}),
    'LOANNAME': (str, {'max_length': 256}),
    'NOTES': (str, {}),  
    'PENALTYDUE': (float, {}),
    'PENALTYPAID': (float, {}),
    'PRINCIPALBALANCE': (float, {}),
    'PRINCIPALPAID': (float, {}),
    'PRODUCTTYPEKEY': (str, {'max_length': 32}),
    'REPAYMENTINSTALLMENTS': (int, {'not_null': True}),
    'REPAYMENTPERIODCOUNT': (int, {}),
    'REPAYMENTPERIODUNIT': (str, {'max_length': 256}),
    'ACCOUNTS_INTEGER_IDX': (int, {}),
    'MIGRATIONEVENTKEY': (str, {'max_length': 32}),
    'ASSIGNEDCENTREKEY': (str, {'max_length': 32}),
    'LASTACCOUNTAPPRAISALDATE': (str, {}), 
    'PRINCIPALREPAYMENTINTERVAL': (int, {'default': 1}),
    'PRINCIPALDUE': (float, {}),
    'INTERESTDUE': (float, {}),
    'LASTINTERESTREVIEWDATE': (str, {}), 
    'ACCRUELATEINTEREST': (bool, {'not_null': True, 'default': True}),
    'INTERESTSPREAD': (float, {}),
    'INTERESTRATESOURCE': (str, {'max_length': 256, 'not_null': True, 'default': 'FIXED_INTEREST_RATE'}),
    'INTERESTRATEREVIEWUNIT': (str, {'max_length': 256}),
    'INTERESTRATEREVIEWCOUNT': (int, {}),
    'ACCRUEDINTEREST': (float, {'default': 0.0}),
    'LASTINTERESTAPPLIEDDATE': (str, {}), 
    'FEESBALANCE': (float, {'default': 0.0}),
    'PENALTYBALANCE': (float, {'default': 0.0}),
    'SCHEDULEDUEDATESMETHOD': (str, {'max_length': 256, 'not_null': True, 'default': 'INTERVAL'}),
    'HASCUSTOMSCHEDULE': (bool, {'not_null': True, 'default': False}),
    'FIXEDDAYSOFMONTH': (bytes, {}),  
    'SHORTMONTHHANDLINGMETHOD': (str, {'max_length': 256}),
    'TAXRATE': (float, {}),
    'LASTTAXRATEREVIEWDATE': (str, {}), 
    'PENALTYRATE': (float, {}),
    'LOANPENALTYCALCULATIONMETHOD': (str, {'max_length': 256, 'default': 'NONE'}),
    'ACCRUEDPENALTY': (float, {'default': 0.0}),
    'ACTIVATIONTRANSACTIONKEY': (str, {'max_length': 32}),
    'LINEOFCREDITKEY': (str, {'max_length': 32}),
    'LOCKEDOPERATIONS': (bytes, {}),  
    'INTERESTCOMMISSION': (float, {}),
    'DEFAULTFIRSTREPAYMENTDUEDATEOFFSET': (float, {}),
    'PRINCIPALPAYMENTSETTINGSKEY': (str, {'max_length': 32}),
    'INTERESTBALANCECALCULATIONMETHOD': (str, {'max_length': 32, 'default': 'PRINCIPAL_ONLY'}),
    'DISBURSEMENTDETAILSKEY': (str, {'max_length': 32}),
    'ARREARSTOLERANCEPERIOD': (int, {'not_null': True, 'default': 0}),
    'ACCRUEINTERESTAFTERMATURITY': (bool, {'not_null': True, 'default': False}),
    'PREPAYMENTRECALCULATIONMETHOD': (str, {'max_length': 255}),
    'PRINCIPALPAIDINSTALLMENTSTATUS': (str, {'max_length': 255}),
    'ELEMENTSRECALCULATIONMETHOD': (str, {'max_length': 256}),
    'LATEPAYMENTSRECALCULATIONMETHOD': (str, {'max_length': 256}),
    'APPLYINTERESTONPREPAYMENTMETHOD': (str, {'max_length': 256}),
    'ALLOWOFFSET': (bool, {'not_null': True, 'default': False}),
    'FUTUREPAYMENTSACCEPTANCE': (str, {'max_length': 256, 'not_null': True, 'default': 'NO_FUTURE_PAYMENTS'}),
    'REDRAWBALANCE': (float, {}),
    'PREPAYMENTACCEPTANCE': (str, {'max_length': 256, 'default': 'ACCEPT_PREPAYMENTS'}),
    'INTERESTFROMARREARSACCRUED': (float, {'default': 0.0}),
    'INTERESTFROMARREARSDUE': (float, {'default': 0.0}),
    'INTERESTFROMARREARSPAID': (float, {'default': 0.0}),
    'INTERESTFROMARREARSBALANCE': (float, {'default': 0.0}),
    'INTERESTROUNDINGVERSION': (str, {'max_length': 256, 'default': 'VERSION_1'}),
    'ACCOUNTARREARSSETTINGSKEY': (str, {'max_length': 32}),
    'HOLDBALANCE': (float, {'not_null': True, 'default': 0.0}),
}
