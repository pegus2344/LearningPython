# Exercise 2.3 Write a program to prompt the user for hours and rate per hour to
# compute gross pay.

stunden = raw_input('Anzahl der Stunden?\n')
rate = raw_input('Stundensatz?\n')

lohn=int(stunden)*float(rate)
print('Lohn: ' + str(lohn))
