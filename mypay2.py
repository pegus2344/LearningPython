#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

inp = raw_input('Enter Hours: ')
hours = float(inp)

inp = raw_input('Enter Rate: ')
rate = float(inp) 

if hours > 40:
   normaltime = 40
   overtime = hours - 40
   pay = (normaltime * rate) + (overtime * rate * 1.5)
else:
   pay = (hours * rate)

print 'Pay:', pay
