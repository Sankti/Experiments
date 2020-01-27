pi = 3.1459
pi_approx = 22/7

radius = 2.2
area = pi*(radius**2)

if x%2 == 0:
    if x%3 == 0:
        print("Divisible by 3")
    else:
        print("Divisible by 2 and not by 3")
elif x%3 == 0:
    print("Divisible by 3 and not by 2")
    

mysum = 0

for i in range (5, 11, 2):
    mysum += i
    if mysum == 5:
        break
