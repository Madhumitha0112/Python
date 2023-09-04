sum = 0
a = int(input("Enter the Low Range Number:"))
b = int(input("Enter the High Range Number:"))

for i in range(a,b+1):
    sum = sum + i

print("The Sum of Numbers from", a, "to", b, "is:", sum)
