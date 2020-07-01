import math

# code to associate all possible inputs that might come from the command prompt to variables in the program using argument parser for cmd prompt
# all the arguments that the program gets from cmp prompt are stored in a Namespace 'results'
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--type",action="store",dest="type")
parser.add_argument("--principal", action="store", dest="p",type=float)
parser.add_argument("--periods", action="store", dest="n",type=int)
parser.add_argument("--interest", action="store", dest="r",type=float)
parser.add_argument("--payment", action="store", dest="a",type=float)
results = parser.parse_args()

# this go_ahead variable will decide the flow of the logic
go_ahead = True

# code to check if length of the namespace is less than 4 ; if it is then print error message
namespace_list = []
if results.type is not None:
	namespace_list.append(results.type)
if results.p is not None:
	namespace_list.append(results.p)
if results.n is not None:
	namespace_list.append(results.n)
if results.r is not None:
	namespace_list.append(results.r)
if results.a is not None:
	namespace_list.append(results.a)
if (len(namespace_list)<4):
	print("Incorrect parameters")
	go_ahead = False

# code to check if any of the number is negative ; if yes then print error message
if go_ahead == True:
	if results.p is not None and results.p < 0:
		print("Incorrect parameters")
		go_ahead = False
	elif results.n is not None and results.n < 0:
		print("Incorrect parameters")
		go_ahead = False
	elif results.r is not None and results.r < 0:
		print("Incorrect parameters")
		go_ahead = False
	elif results.a is not None and results.a < 0:
		print("Incorrect parameters")
		go_ahead = False

# code to check if interest in none ; if its is then print error message	
if go_ahead == True:
	if results.r is None:
		print("Incorrect parameters")
		go_ahead = False

# after all errors are resolved then the following code will perform calculation based on user input
if go_ahead == True:
	if results.type == "diff" or results.type == "annuity":
		if results.type == "diff":
			if results.a is not None:
				print("Incorrect parameters")
			else:
				p = results.p
				n = results.n
				r = results.r
				i = (r*0.01)/12
				amount_paid = 0
				#caluclate the differential monthly payment based on principal, month count and rate of interest
				for m in range(1, n+1):
					num1 = (p * (m - 1)) / n
					diff_amount = (p / n) + (i * (p - num1))
					x_amount = diff_amount - int(diff_amount)
					if x_amount > 0:
						diff_amount +=1
					diff_amount = int(diff_amount)
					amount_paid += diff_amount
					print(f"Month {m}: paid out {diff_amount}")
				# calculate overpayment
				over_payment = amount_paid - int(p)
				print(f"Overpayment = {over_payment}")
		elif results.type == "annuity":
			# calculate the months required to repay the credit and also the over payment
			if results.n is None:
				p = results.p
				a = results.a
				r = results.r

				i = (r*0.01)/12
				denominator = (a - (i * p))
				num = a / denominator
				base = 1 + i

				n = math.log(num,base)
				n = int(n)
				n += 1

				if n % 12 == 0:
					yrs = n / 12
					if yrs == 1:
						print(f"You need 1 year to repay this credit!")
					else:
						print(f"You need {int(yrs)} years to repay this credit!")
				else:
					yrs = n // 12
					mnths = n % 12
					if yrs < 1:
						print(f"You need {int(mnths)} months to repay this credit!")
					else:
						print(f"You need {int(yrs)} years and {int(mnths)} months to repay this credit!")
				
				amount_paid = a * n
				over_payment = amount_paid - p
				print(f"Overpayment = {int(over_payment)}")
			# calculate the monthly payments to be made and the over payment
			elif results.a is None:
				p = results.p
				n = results.n
				r = results.r

				i = (r*0.01)/12
				numerator = i * ((1 + i) ** n)
				denominator = ((1 + i) ** n) - 1

				mp = p * (numerator / denominator)
				a = int(mp)
				a += 1

				print(f"Your annuity payment = {a}!")

				amount_paid = a * n
				over_payment = amount_paid - p
				print(f"Overpayment = {int(over_payment)}")
			# calculate pricipal credit along with the over payment
			elif results.p is None:
				a = results.a
				n = results.n
				r = results.r

				i = (r*0.01)/12
				numerator = i * ((1 + i) ** n)
				denominator = ((1 + i) ** n) - 1
				num = numerator / denominator
				
				p = a / num
				p = int(p)
				
				print(f"Your credit principal = {p}!")

				amount_paid = a * n
				over_payment = amount_paid - p
				print(f"Overpayment = {int(over_payment)}")
	else:
		print("Incorrect parameters")

