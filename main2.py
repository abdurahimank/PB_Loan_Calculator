import math
import argparse


def calculate_no_months(principal, monthly_payment, interest):
    i = interest / (12 * 100)
    no_months = math.ceil(math.log((monthly_payment / (monthly_payment - (i * principal))), 1 + i))
    if no_months == 1:
        print('\nIt will take 1 month to repay the loan!')
    elif no_months < 12:
        print(f'\nIt will take {no_months} months to repay the loan!')
    elif no_months == 12:
        print(f'It will take 1 year to repay this loan!')
    elif no_months % 12 == 1:
        print(f'It will take {no_months // 12} years and 1 month to repay this loan!')
    elif no_months % 12 == 0:
        print(f'It will take {no_months // 12} years to repay this loan!')
    else:
        print(f'It will take {no_months // 12} years and {no_months % 12} months to repay this loan!')
    print(f'Overpayment = {round((no_months * monthly_payment) - principal)}')


def calculate_monthly_payment(principal, periods, interest):
    i = interest / (12 * 100)
    monthly_payment = math.ceil(principal * ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1)))
    print(f'Your annuity payment = {monthly_payment}!')
    print(f'Overpayment = {round((monthly_payment * periods) - principal)}')


def calculate_principal(monthly_payment, periods, interest):
    i = interest / (12 * 100)
    principal = math.floor(monthly_payment / ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1)))
    print(f'Your loan principal = {principal}!')
    print(f'Overpayment = {round((monthly_payment * periods) - principal)}')


def calculate_diff_payment(principal, periods, interest):
    i = interest / (12 * 100)
    total_amount = 0
    for j in range(1, int(periods + 1)):
        payment = math.ceil((principal / periods) + (i * (principal - ((principal * (j - 1)) / periods))))
        print(f'Month {j}: payment is {payment}')
        total_amount += payment
    print(f'\nOverpayment = {round(total_amount - principal)}')


parser = argparse.ArgumentParser(description='Credit Calculator')
parser.add_argument("--type")  # "annuity" or "diff"
parser.add_argument("--payment")  # don't come with 'diff' type
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

variables = [args.type, args.payment, args.principal, args.periods, args.interest]
# print(variables, variables.count(None))
if variables.count(None) > 1 or variables[0] not in ["annuity", "diff"] \
        or (variables[0] == 'diff' and variables[1] is not None) or variables[4] is None \
        or any([1 for i in variables if i not in [None, "annuity", "diff"] and float(i) < 0]):
    print('Incorrect parameters')
elif variables[0] == 'diff' and variables[1] is None:
    calculate_diff_payment(float(variables[2]), float(variables[3]), float(variables[4]))
elif variables[0] == 'annuity' and variables[1] is None:
    calculate_monthly_payment(float(variables[2]), float(variables[3]), float(variables[4]))
elif variables[0] == 'annuity' and variables[2] is None:
    calculate_principal(float(variables[1]), float(variables[3]), float(variables[4]))
elif variables[0] == 'annuity' and variables[3] is None:
    calculate_no_months(float(variables[2]), float(variables[1]), float(variables[4]))
