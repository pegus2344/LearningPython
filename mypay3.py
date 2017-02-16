#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by 
#printing a message and exiting the program. The following shows two executions of the program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Enter Hours: forty
#Error, please enter numeric input


inp_h = raw_input('Enter Hours: ')


inp_r = raw_input('Enter Rate: ')

try:
   hours = float(inp_h)
   rate = float(inp_r) 
   if hours > 40:
      normaltime = 40
      overtime = hours - 40
      pay = (normaltime * rate) + (overtime * rate * 1.5)
   else:
      pay = (hours * rate)
   print 'Pay:', pay

except:
   print('Please enter a numeric value!\n')


