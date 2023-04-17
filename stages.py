# Stage 3/4: Annuity payment
import math


def find_no_months():
    loan_principal = float(input("Enter the loan principal:\n"))
    monthly_payment = float(input("Enter the monthly payment:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest / (12 * 100)
    no_months = math.ceil(math.log(monthly_payment / (monthly_payment - (i * loan_principal)), 1 + i))
    if no_months == 1:
        print("It will take 1 month to repay the loan")
    elif no_months < 12:
        print(f"It will take {no_months} months to repay the loan")
    elif no_months == 12:
        print(f"It will take 1 year to repay this loan!")
    elif no_months % 12 == 0:
        print(f"It will take {no_months // 12} years to repay this loan!")
    elif no_months % 12 == 1:
        print(f"It will take {no_months // 12} years and 1 month to repay this loan!")
    else:
        print(f"It will take {no_months // 12} years and {no_months % 12} months to repay this loan!")


def find_monthly_payment():
    loan_principal = float(input("Enter the loan principal:\n"))
    no_months = float(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest / (12 * 100)
    monthly_payment = math.ceil(loan_principal * ((i * ((1 + i) ** no_months)) / (((1 + i) ** no_months) - 1)))
    print(f"Your monthly payment = {monthly_payment}!")


def find_loan_principal():
    monthly_payment = float(input("Enter the annuity payment:\n"))
    no_months = float(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest / (12 * 100)
    loan_principal = math.floor(monthly_payment / ((i * ((1 + i) ** no_months)) / (((1 + i) ** no_months) - 1)))
    print(f"Your loan principal = {loan_principal}!")


to_calculate = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:\n""")
if to_calculate == "n":
    find_no_months()
elif to_calculate == "a":
    find_monthly_payment()
else:
    find_loan_principal()
