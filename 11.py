def getWords(n):
	num_to_words = {
	1 : "One",
	2 : "Two",
	3 : "Three",
	4 : "Four",
	5 : "Five",
	6 : "Six",
	7 : "Seven",
	8 : "Eight",
	9 : "Nine",
	0 : "Zero"
	}
	return num_to_words[n]

num = 1359
num = str(num)
for digit in num :
	print getWords(int(digit))
