driving = input ('if you drive? ')
if driving != 'yes' and driving != 'no':
	print ('answer yes / no')
	raise SystemExit  #triggger program exit



age = input ('your age? ')
age = int (age)
if driving == 'yes':
	if age >= 18:
		print ('you pass the test')
	else:
		print ('wired, you might not drive')
elif driving == 'no':
	if age >= 18:
		print ('you could get license')
	else:
		print ('wait few years')
else:
	print ("answer yes / no")