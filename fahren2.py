# Exercise 2.5 Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.

inp = raw_input('Bitte geben Sie die Temperatur in Grad Fahrenheit ein!\n')

try:
    temp_fahr = float(inp)
    temp_cel=(temp_fahr - 32.0) * 5.0 / 9.0

    print(' Die Temperatur in Grad Celsius ist:' + str(temp_cel)+'\n')

except:
    print 'No valid input. Please enter a number:'




