import math
import argparse

parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument("-t", "--type")
parser.add_argument("-pr", "--principal")
parser.add_argument("-pa", "--payment")
parser.add_argument("-pe", "--periods")
parser.add_argument("-i", "--interest")

args = parser.parse_args()
# All parameters are converted to a dictionary for is of use.
# Digits in string format is converted to float and "None" is replaced by zero for ease of calculation.
args = dict(type=args.type, principal=0 if args.principal is None else float(args.principal),
            payment=0 if args.payment is None else float(args.payment),
            periods=0 if args.periods is None else float(args.periods),
            interest=0 if args.interest is None else float(args.interest))
if args["type"] not in ["annuity", "diff"] or (args["type"] == "diff" and args["payment"]) or not args["interest"] \
        or list(args.values()).count(0) > 1 or any([True if i < 0 else False for i in list(args.values())[1:]]):
    print("Incorrect parameters")

# Calculating differentiated payment for each month.
elif args["type"] == "diff":
    total_payment = 0
    i = args["interest"] / (12 * 100)
    for j in range(1, int(args["periods"]) + 1):
        monthly_payment = math.ceil((args["principal"] / args["periods"])
                                    + (i * (args["principal"] - ((args["principal"] * (j - 1)) / args["periods"]))))
        total_payment += monthly_payment
        print(f"Month {i}: payment is {monthly_payment}")
    print(f"\nOverpayment = {round(total_payment - args['principal'])}")

# Calculating monthly annuity payment.
elif args["type"] == "annuity" and args["payment"] == 0:
    i = args["interest"] / (12 * 100)
    monthly_payment = math.ceil(args["principal"]
                                * ((i * math.pow(1 + i, args["periods"])) / (math.pow(1 + i, args["periods"]) - 1)))
    print(f"Your annuity payment = {monthly_payment}!")
    print(f"Overpayment = {round((monthly_payment * args['periods']) - args['principal'])}")

# Calculating loan principal for annuity payment.
elif args["type"] == "annuity" and args["principal"] == 0:
    i = args["interest"] / (12 * 100)
    principal = math.floor(args["payment"]
                           / ((i * math.pow(1 + i, args["periods"])) / (math.pow(1 + i, args["periods"]) - 1)))
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {round((args['payment'] * args['periods']) - principal)}")

# Calculating number of periods for annuity payment.
elif args["type"] == "annuity" and args["periods"] == 0:
    i = args["interest"] / (12 * 100)
    no_months = math.ceil(math.log((args["payment"] / (args["payment"] - (i * args["principal"]))), 1 + i))
    if no_months == 1:
        print("It will take 1 month to repay the loan")
    elif no_months < 12:
        print(f"It will take {no_months} months to repay the loan")
    elif no_months == 12:
        print("It will take 1 year to repay the loan")
    elif no_months % 12 == 0:
        print(f"It will take {no_months // 12} years to repay the loan")
    elif no_months % 12 == 1:
        print(f"It will take {no_months // 12} years and 1 month to repay this loan!")
    else:
        print(f"It will take {no_months // 12} years and {no_months % 12} months to repay this loan!")
    print(f"Overpayment = {round((no_months * args['payment']) - args['principal'])}")
