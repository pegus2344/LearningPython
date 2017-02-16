# Rewrite your pay computation with time-and-a-half for overtime and create a function 
# called computepay which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

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

def computepay(hours,rate):
   calc_pay = hours * rate
   return calc_pay

try:
   hours = float(inp_h)
   rate = float(inp_r) 
   if hours > 40:
      normaltime = 40
      overtime = hours - 40
      pay = computepay(normaltime, rate) + computepay(overtime , (rate * 1.5))
   else:
      pay = computepay(normaltime, rate)
   print 'Pay:', pay

except:
   print('Please enter a numeric value!\n')


