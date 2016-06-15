pairs = { 
100 : 'One Hundred',
'abc' : 'letters',
3.14 : "pi",
"***" : 'Stars'
}

for x,y in enumerate(pairs):
	print x,y
print

for x,y in pairs.iteritems():
	print x,y

