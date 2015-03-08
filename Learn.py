import AufnahmeundVerarbeitung

print "Calibrating..."
print "Please speak a sentence in your normal voice!"
normal1 = AufnahmeundVerarbeitung.analyse()
print "And again!"
normal2 = AufnahmeundVerarbeitung.analyse()

print "Please speak a sentence in your tired voice!"
tired1 = AufnahmeundVerarbeitung.analyse()
print "And again!"
tired2 = AufnahmeundVerarbeitung.analyse()

print "Please speak a sentence in your angry voice!"
angry1 = AufnahmeundVerarbeitung.analyse()
print "And again!"
angry2 = AufnahmeundVerarbeitung.analyse()

normal = sum([normal1, normal2]) / 2
tired = min([tired1, tired2])
angry = max([angry1, angry1])

def classify(value):
	if value < angry:
		print "You are angry!"
	elif value => angry:
		print "You are tired..."
	else:
		print "You are meh."

while(True):
	print "Say something!"
	classify(AufnahmeundVerarbeitung.analyse())