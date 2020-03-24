while True:
	n=input("Please enter a number(o to exit):")
	n=int(n)
	if n<0:
		print("We allow positive number.Please try again.")
		continue
	if n==0:
		break
	print("Square of:",n,"is",n*n)