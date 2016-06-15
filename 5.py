a = 0
b = 1
print a,b
a,b = b,a
print a,b

test = [31,56,21,5,100]
print test
test.sort()
print test
test.sort(reverse=True)
print test

name = "Balagopal"
print name[::-1]