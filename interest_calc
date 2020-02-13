balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

print("--- Month 0 ---")
print("Balance: " + str(balance))

for number in range(12):
    payment = balance * monthlyPaymentRate
    unpaid = balance - payment
    interest = annualInterestRate / 12 * unpaid
    balance = unpaid + interest
    print(payment)
    print(unpaid)
    print(interest)
    print("--- Month " + str(number + 1) + " ---")
    print(balance)

print ("--- Final Balance --- \n" + str(round(balance, 2)))
