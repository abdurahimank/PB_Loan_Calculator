import math
import argparse


def find_loan_principal(monthly_payment, no_months, interest):
    i = interest / (12 * 100)
    principal = monthly_payment / (i * ((1 + i) ** no_months) / (((1 + i) ** no_months) - 1))
    print(f'Your loan principal = {math.floor(principal)}!')
    print(f'Overpayment = {round((monthly_payment * no_months) - math.floor(principal))}')


def find_monthly_payment(principal, no_months, interest):
    i = interest / (12 * 100)
    monthly_payment = principal * ((i * ((1 + i) ** no_months)) / (((1 + i) ** no_months) - 1))
    print(f'Your monthly payment = {math.ceil(monthly_payment)}!')
    print(f'Overpayment = {round((math.ceil(monthly_payment) * no_months) - principal)}')


def find_no_months(principal, monthly_payment, interest):
    i = interest / (12 * 100)
    no_months = math.ceil(math.log(monthly_payment / (monthly_payment - (i * principal)), 1 + i))
    if no_months == 1:
        print('It will take 1 month to repay the loan!')
    elif no_months < 12:
        print(f'It will take {no_months} months to repay the loan!')
    elif no_months == 12:
        print('It will take 1 year to repay the loan!')
    else:
        if no_months == 13:
            print('It will take 1 year and 1 month to repay the loan!')
        elif no_months % 12 == 0:
            print(f'It will take {no_months // 12} years to repay the loan!')
        elif no_months % 12 == 1:
            print(f'It will take {no_months // 12} year and 1 month to repay the loan!')
        else:
            print(f'It will take {no_months // 12} years and {no_months % 12} months to repay the loan!')
    print(f'Overpayment = {round((no_months * monthly_payment) - principal)}')


def find_diff_payments(p, n, interest):
    i = interest / (12 * 100)
    total = 0
    for j in range(1, int(n) + 1):
        payment = math.ceil((p / n) + (i * (p - ((p * (j - 1)) / n))))
        total += payment
        print(f'Month {j}: payment is {payment}')
    print(f'\nOverpayment = {round(total - p)}')


parser = argparse.ArgumentParser(description='Credit Calculator')
parser.add_argument("--type")  # choices = ["annuity", "diff"]
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser = parser.parse_args()
data = [parser.type, parser.payment, parser.principal, parser.periods, parser.interest]
if data.count(None) > 1 or data[0] not in ["annuity", "diff"] or (data[0] == "diff" and data[1] is not None) or \
        data[4] is None or any([False if i is None or float(i) > 0 else True for i in data[1:]]):
    print("Incorrect parameters")
elif parser.type == "diff":
    find_diff_payments(float(data[2]), float(data[3]), float(data[4]))
elif parser.payment is None:
    find_monthly_payment(float(data[2]), float(data[3]), float(data[4]))
elif parser.principal is None:
    find_loan_principal(float(data[1]), float(data[3]), float(data[4]))
elif parser.periods is None:
    find_no_months(float(data[2]), float(data[1]), float(data[4]))
