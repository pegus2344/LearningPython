# Exercise 2.5 Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.

temp_cel = raw_input('Bitte geben Sie die Temperatur in Grad Celsius ein!\n')

temp_far = (9/5) * int(temp_cel) + 35

print(str(temp_cel) +' Grad Celsius sind ' + str(temp_far) + ' Grad Fahrenheit.\n')
