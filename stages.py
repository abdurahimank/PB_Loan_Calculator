# Stage 2/4: Dreamworld
import math


loan_principal = float(input("Enter the loan principal:\n"))
to_calculate = input("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:\n""")
if to_calculate == "m":
    monthly_payment = float(input("Enter the monthly payment:\n"))
    no_months = math.ceil(loan_principal / monthly_payment)
    if no_months == 1:
        print("It will take 1 month to repay the loan")
    elif no_months < 12:
        print(f"It will take {no_months} months to repay the loan")
    elif no_months == 12:
        print("")
    elif no_months % 12 == 0:
        print("")
    elif no_months % 12 == 1:
        print("")
    else:
        print("")
elif to_calculate == "p":
    no_months = int(input("Enter the number of months:\n"))
    monthly_payment = loan_principal / no_months
    if monthly_payment % 1 != 0:
        monthly_payment = math.ceil(monthly_payment)
        last_month_payment = loan_principal - (monthly_payment * (no_months - 1))
        print(f"Your monthly payment = {monthly_payment} and the last payment = {last_month_payment}.")
    else:
        print(f"Your monthly payment = {monthly_payment}")

