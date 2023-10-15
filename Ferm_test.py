p = int(input("Please enter the no. which you want to test for it's primality: "))
count = 0

for i in range(2,p):
	if ((i**p)-i)%p!=0:
		print("The given number is not a prime number.")
		exit()
		count = count + 1
	else: pass
	print("The progress of code is", i*100/p, "%")

if count==0:
	print("The given number is a prime number.")
	exit()
