from random import randint

a = [randint(1,100) for x in range(20)]
print a

even = []
odd = []
for num in a:
	if num%2==0:
		even.append(num)
	else:
		odd.append(num)

even.sort()
print even

print odd
odd.reverse()
print odd
