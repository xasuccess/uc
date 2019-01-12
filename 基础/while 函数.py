number = [23,43,23,54,66,98]
even = []
odd = []
while len(number) > 0 :
	number = number.pop()
	if(number % 2 == 0):
		even.append(number)
	else:
		odd.append(number)