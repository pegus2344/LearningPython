Enter file contents here'''
Created on 16.02.2015

@author: gussg
'''

s=input("Enter an integer: ")
try:
    i = int(s)
    print("valid integer entered:",i)
    
except ValueError as err:
    print("Also so geht das nicht! Das ist keine Integerzahl",err)    
