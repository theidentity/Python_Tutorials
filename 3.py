a = raw_input("Enter a string : ")
b = raw_input("Enter the substring : ")

print 'Length of a is : '+str(len(a))
if b in a:
	print b+" is present in "+a
else:
	print b+" is not present in "+a
