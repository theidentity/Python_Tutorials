i = 1
while i<=10 :
	print i,
	i+=1
print "One to 10"

i=1
while i<=10 :
	if i==5:
		break
	print i,
	i+=1
print "One to 4"

i=0
while i<=10 :
	i+=1
	if i==5:
		continue
	print i,
print "One to 10 without 5"