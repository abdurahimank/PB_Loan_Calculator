import math
import argparse


def loan_principal(monthly_payment, no_months, interest):
    i = interest / (12 * 100)
    principal = math.floor(monthly_payment / ((i * ((1 + i) ** no_months)) / (((1 + i) ** no_months) - 1)))
    print(f'Your loan principal = {principal}!')
    print(f'Overpayment = {round((monthly_payment * no_months) - principal)}')


def monthly_payments(principal, no_months, interest):
    i = interest / (12 * 100)
    monthly_payment = math.ceil(principal * ((i * ((1 + i) ** no_months)) / (((1 + i) ** no_months) - 1)))
    print(f'Your annuity payment = {monthly_payment}!')
    print(f'Overpayment = {round((no_months * monthly_payment) - principal)}')


def no_of_months(principal, monthly_payment, interest):
    i = interest / (12 * 100)
    no_months = math.ceil(math.log((monthly_payment / (monthly_payment - (i * principal))), 1 + i))
    if no_months == 1:
        print('It will take 1 month to repay the loan!')
    elif no_months < 12:
        print(f'It will take {no_months} months to repay the loan!')
    elif no_months == 12:
        print('It will take 1 year to repay the loan!')
    elif no_months % 12 == 1 and no_months // 12 == 1:
        print('It will take 1 year and 1 month to repay the loan!')
    elif no_months // 12 > 1 and no_months % 12 == 0:
        print(f'It will take {no_months // 12} years to repay this loan!')
    elif no_months % 12 == 1:
        print(f'It will take {no_months // 12} years and 1 month to repay the loan!')
    else:
        print(f'It will take {no_months // 12} years and {no_months % 12} months to repay the loan!')
    print(f'Overpayment = {round((no_months * monthly_payment) - principal)}')


def diff_payment(p, n, i):
    i = i / (12 * 100)
    total = 0
    for j in range(1, int(n) + 1):
        payment = math.ceil((p / n) + (i * (p - ((p * (j - 1)) / n))))
        total += payment
        print(f'Month {j}: payment is {payment}')
    print(f'\nOverpayment = {round(total - p)}')


parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
args = parser.parse_args()
para_list = [i for i in list(args.__dict__.values()) if i not in [None, "annuity", "diff"] and float(i) < 0]
while True:
    if (args.type not in ["annuity", "diff"]) or (args.type == 'diff' and args.payment is not None) \
            or (args.interest is None):
        print('Incorrect parameters')
    elif list(args.__dict__.values()).count(None) > 1 or len(para_list) > 0:
        print('Incorrect parameters')
    elif args.type == 'diff':
        diff_payment(float(args.principal), float(args.periods), float(args.interest))
    elif args.payment is None:
        monthly_payments(float(args.principal), float(args.periods), float(args.interest))
    elif args.principal is None:
        loan_principal(float(args.payment), float(args.periods), float(args.interest))
    else:
        no_of_months(float(args.principal), float(args.payment), float(args.interest))
    break
