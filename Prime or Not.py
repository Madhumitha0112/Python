a = int(input("Enter the Number:"))
prime = True

if a < 2:
    prime = False
else:
    for i in range(2, a):
        if a % i == 0:
            prime = False
            break

if prime:
    print("Prime")
else:
    print("Not Prime")
