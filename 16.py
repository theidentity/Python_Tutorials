l1 = [x for x in range(10)]
l2 = [x for x in range(10,20)]
print l1
print l2

print (map(lambda x,y:x*20, l1,l2))
print (filter(lambda x: x%2==0,l2))
print (reduce(lambda x,y:x+y, l1))