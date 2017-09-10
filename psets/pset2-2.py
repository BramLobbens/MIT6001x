# MIT 6.00.1x Pset2-2

# Set test case variables
balance = 42
annualInterestRate = 0.2
monthPay = 10 # start value of 10

def payoffDebt(bal, annInt, monthPay, month=1):
    '''
    bal (int)       : unpaid balance
    annInt (float)  : annual interest rate
    monthPay (int)  : fixed monthly payment (multiple of 10)
    month (int)     : current month, default=1
    Return remaining balance after one year.
    '''
    # new balance after each month according to below formula
    new_bal = (bal-monthPay) + ((bal-monthPay)*annInt/12)

    if month == 12:
        # base case: balance after one year
        new_bal = new_bal
    else:
        new_bal = payoffDebt(new_bal, annInt, monthPay, month+1)

    return new_bal

# Increase the monthly payment by multiple of 10 until debt is 
# paid off within one year

while payoffDebt(balance, annualInterestRate, monthPay) > 0:
    monthPay += 10

print('Lowest Payment:', monthPay)