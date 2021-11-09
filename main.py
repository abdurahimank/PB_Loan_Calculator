import math
import argparse

# Command Line Arguments
parser = argparse.ArgumentParser(description="This is a loan calculator either in annuity or diff mode")

parser.add_argument("--type")  # choices=["annuity", "diff"]
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=float)
parser.add_argument("--interest", type=float)

args = parser.parse_args()
dic_args = vars(args)

loan_type = args.type
monthly_payment = args.payment
principal = args.principal
no_months = args.periods
interest = args.interest


# Functions
def fun_no_months(principal, monthly_payment, interest):
    i = interest / (12 * 100)  # nominal interest
    x = monthly_payment / (monthly_payment - (i * principal))
    no_months = int(math.ceil((math.log(x, (1 + i)))))
    if no_months == 1:
        print("It will take {no_months} month to repay this loan!")
    elif no_months < 12:
        print("It will take {no_months} months to repay this loan!")
    elif no_months == 12:
        print("It will take 1 year to repay this loan!")
    else:
        if no_months % 12 == 0:
            print(f"It will take {no_months // 12} years to repay this loan!")
        elif no_months % 12 == 1:
            print(f"It will take {no_months // 12} years and {no_months % 12} month to repay this loan!")
        else:
            print(f"It will take {no_months // 12} years and {no_months % 12} months to repay this loan!")
    over_payment = (no_months * monthly_payment) - principal
    print(f"Overpayment = {int(over_payment)}")


def fun_principle(monthly_payment, no_months, interest):
    i = interest / (12 * 100)  # nominal interest
    x = (i * pow((1 + i), no_months)) / ((pow((1 + i), no_months)) - 1)
    principal = int(monthly_payment / x)
    print(f"Your loan principal = {principal}!")
    over_payment = (no_months * monthly_payment) - principal
    print(f"Overpayment = {int(over_payment)}")


def fun_monthly_payment(principal, no_months, interest):
    i = interest / (12 * 100)  # nominal interest
    x = (i * pow((1 + i), no_months)) / ((pow((1 + i), no_months)) - 1)
    monthly_payment = int(math.ceil(principal * x))
    print(f"Your annuity payment = {monthly_payment}!")
    over_payment = (no_months * monthly_payment) - principal
    print(f"Overpayment = {int(over_payment)}")


def fun_diff_loan(principal, no_months, interest):
    i = interest / (12 * 100)  # nominal interest
    total_ = 0
    for m in range(1, int(no_months + 1)):
        x = principal - ((principal * (m - 1)) / no_months)
        monthly_payment = int(math.ceil((principal / no_months) + (i * x)))
        print(f"Month {m}: payment is {monthly_payment}")
        total_ += monthly_payment
    overpayment = total_ - principal
    print()
    print(f"Overpayment = {int(overpayment)}")


# Error checking
neg = False
nos_value = 0
for i in dic_args.values():
    if i is None:
        nos_value += 1
    if type(i) is float and i < 0:
        neg = True

if loan_type not in ["annuity", "diff"] or ((loan_type == "diff") and monthly_payment) or (interest is None):
    print("Incorrect parameters")
elif nos_value > 1 or neg:
    print("Incorrect parameters")

# program running...
else:
    if loan_type == "diff":
        fun_diff_loan(principal, no_months, interest)
    else:
        if no_months is None:
            fun_no_months(principal, monthly_payment, interest)
        elif principal is None:
            fun_principle(monthly_payment, no_months, interest)
        else:
            fun_monthly_payment(principal, no_months, interest)
