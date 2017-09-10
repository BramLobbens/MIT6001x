# MIT 6.00.1x Pset2-3
# Set test case variables
balance = 320000
annualInterestRate = 0.2

def payoffDebt(bal, annInt, monthPay, month=1):
    '''
    bal (int)       : unpaid balance
    annInt (float)  : annual interest rate
    monthPay (int)  : fixed monthly payment (multiple of 10)
    month (int)     : current month, default=1
    Return remaining balance after one year.
    '''
    # new balance after each month according to below formula
    new_bal = (bal - monthPay) + ((bal - monthPay)*annInt/12)

    if month == 12:
        # base case: balance after one year
        new_bal = new_bal
    else:
        new_bal = payoffDebt(new_bal, annInt, monthPay, month+1)

    return new_bal

# Use bisection search so that remaining balance is within epsilon margin
ans = False
epsilon = 0.10 # margin of remaining balance
lower = (balance/12)
upper = (balance * (1 + (annualInterestRate/12))**12) / 12.0
middle = (lower + upper)/2

while ans == False:
    # Return remaining balance
    result = payoffDebt(balance, annualInterestRate, middle)

    if abs(result) <= epsilon:
        ans = True
    else:
        if result < 0:
            # if remaining balance is still negative, set upper bound to middle
            upper = middle
        else:
            # if remaining balance is still positive, set lower bound to middle
            lower = middle

    middle = (lower + upper)/2

print('Lowest Payment:', round(middle,2))