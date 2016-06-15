sentence = "This sentence is full of letters"
sentence = sentence.lower()
sentence = sentence.replace(' ','')
print sentence

letters = set(x for x in sentence)
for l in letters:
	print l,