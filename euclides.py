def euclides(num1,num2):

	if num2 == 0:

		return num1

	return euclides(num2, num1 % num2)
