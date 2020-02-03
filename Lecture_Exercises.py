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

#LOOP EXERCISES

x = 2
while x <= 10:
        print(x)
        x += 2
print('Goodbye!')

print("")

print('Hello!')
x = 10
while x <= 10 and x >= 2:
        print(x)
        x -= 2

print("")

end = 6
x = 0
y = 0
while x < end:
    x += 1
    y += x
    print("X " + str(x))
    print("Y " + str(y))
print("Final result: " + str(y))

print("")

for num in (2, 4, 6, 8, 10):
    print(num)
print('Goodbye!')

print("")

print('Hello!')
for num in (10, 8, 6, 4, 2):
    print(num)

print("")

end = 6
x = 0
y = 0

for num in range(0, end):
    x += 1
    y += x
    print("X " + str(x))
    print("Y " + str(y))
print("Final result: " + str(y))

s = "Hello!"
s[0] = "Y"

# TypeError: 'str' object does not support item assignment

s = "Hello!"
s = "Y" + s[1:]
print(s)

# Yello!
