import math as m

n = int(input("Please the number for which you want to evaluate it's Phi function: "))

ls = []
for i in range(1,n):
	if m.gcd(i,n)==1:
		ls.append(i)
	else: pass
	print("The completion is", i*100/n,"%")

print("The Phi(",n,") is", len(ls))
