num = int(input("enter number : "))
n = 0
while num > 0 :
    digit = num % 10
    n = n*10 + digit
    num = num // 10
print(" ",n)