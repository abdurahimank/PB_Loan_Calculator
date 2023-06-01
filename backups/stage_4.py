# Project: Loan Calculator
# Stage 4/4: Differentiate payment
import math
import argparse


def find_no_months(p, m, i):  # p = principal, m = monthly_payment, i = interest
    i = i / (12 * 100)
    no_months = math.ceil(math.log(m / (m - (i * p)), 1 + i))
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
    print(f"Overpayment = {round((m * no_months) - p)}")


def find_monthly_payment(p, n, i):  # p = principal, n = periods, i = interest
    i = i / (12 * 100)
    monthly_payment = math.ceil(p * ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))
    print(f"Your monthly payment = {monthly_payment}!")
    print(f"Overpayment = {round(p - (n * monthly_payment))}")


def find_loan_principal(m, n, i):  # m = monthly_payment, n = periods, i = interest
    i = i / (12 * 100)
    loan_principal = math.floor(m / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))
    print(f"Your loan principal = {loan_principal}!")
    print(f"Overpayment = {round((m * n) - loan_principal)}")


def diff_payment(p, n, i):  # p = principal, n = periods, i = interest
    i = i / (12 * 100)
    total_amount = 0
    for m in range(1, n + 1):
        nth_payment = math.ceil((p / n) + (i * (p - ((p * (m - 1)) / (n)))))
        print(f"Month {m}: payment is {nth_payment}")
        total_amount += nth_payment
    print(f"\nOverpayment = {round(total_amount - p)}")


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()
parameters = dict(type=args.type, payment=0 if args.payment is None else float(args.payment),
                  principal=0 if args.principal is None else float(args.principal),
                  periods=0 if args.periods is None else int(args.periods),
                  interest=0 if args.interest is None else float(args.interest))
if args.type not in ["annuity", "diff"] or (args.type == "diff" and args.payment) or args.interest is None \
        or list(parameters.values()).count(0) > 1 or any([True for i in list(parameters.values())[1:] if i < 0]):
    print("Incorrect parameters")
elif parameters["type"] == "diff":
    diff_payment(parameters["principal"], parameters["periods"], parameters["interest"])
elif parameters["type"] == "annuity" and parameters["principal"] == 0:
    find_loan_principal(parameters["payment"], parameters["periods"], parameters["interest"])
elif parameters["type"] == "annuity" and parameters["payment"] == 0:
    find_monthly_payment(parameters["principal"], parameters["periods"], parameters["interest"])
elif parameters["type"] == "annuity" and parameters["periods"] == 0:
    find_no_months(parameters["principal"], parameters["payment"], parameters["interest"])
