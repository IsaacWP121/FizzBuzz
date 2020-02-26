def calc(num, par1=3, par2=5): # num is the number being checked, par1 is the first parameter checked against num and is usually set to 3, par2 is the second paramter and is the second parameter usually set to 5
	out = "" # this is the output string which will be concatinated with the appropriete output ("Fizz, Buzz, Both or it will return the original num variable") 
	if num % par1 == 0: # if the var num is devisable by par1 (3) with no remainders it will add the string "Fizz" to the output
		out += "Fizz" 
	if num % par2 == 0: # if the var num is devisable by par2 (5) with no remainders it will add the string "Buzz" to the output
		out += "Buzz"
	elif num % par1 != 0 and num % par2 != 0: # if neither of the above statements are true then it will set the output to the input effectivly just returning the same number in the num variable
		out = num
	print(out) # prints the out variable to the console
	
if __name__ == "__main__": #if the file is run independently and not imported by another project
	r = 100 # setting int variable r to 100, this is the defualt amount of numbers that will be 
	#passed through the "FizzBuzz" Calculation 
	for i in range(1, r): # for each number between 1 and r
		calc(i)# calculate the current number being iterated
