n = int(input("enter number : "))
pom = n
num = 0
while n > 0 :
	digit = n % 10
	num = num*10 + digit
	n = n // 10
if pom == num :
	print("pelidrome")
else:
	print("is not")