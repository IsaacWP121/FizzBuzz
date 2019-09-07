def calc(num, par1=3, par2=5):
	out = ""
	if num % par1 == 0:
		out += "Fizz"
	if num % par2 == 0:
		out += "Buzz"
	if num % par1 != 0 and num % par2 != 0:
		out = num
	print(out)
	
if __name__ == "__main__":
	r = 100
	for i in range(1, r):
		calc(i)
