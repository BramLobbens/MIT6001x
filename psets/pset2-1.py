# MIT 6.00.1x Pset2-1

# Set test case variables
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def payingDebt(bal, annInt, monthPay, month=1):
    '''
    bal (int)       : balance
    annInt (float)  : annualInterestRate
    monthPay (float): monthlyPaymentRate
    month (int)     : default=1
    Return remaining balance after one year
    '''

    # New balance after every month set to below formula
    new_bal = (bal-(bal*monthPay)) + ((bal-(bal*monthPay))*annInt/12)

    #Test print every month
    #print('Month',month,'Bal:',round(new_bal,2))

    if month == 12:
        # Base case after 12 months
        new_bal = new_bal
    else:
        new_bal = payingDebt(new_bal, annInt, monthPay, month+1)
        
    return round(new_bal, 2)

print('Remaining balance:', payingDebt(
                            balance, 
                            annualInterestRate, 
                            monthlyPaymentRate))