'''
Created on 16.02.2015

@author: gussg
'''


if __name__ == '__main__':
    print 'Hello World'
try:
#x = None
#x=123
    if x is None:
        print("x is zero")
    else:
        print ("x is nonzero")
        
        
    for i in range(1,10):
        print i
        
    for letter in "lorem Ipsum":
        if letter in "orm":
            print(letter, "ist vorhanden")
        else:
            print(letter, "ist nicht vorhanden")
        
except Exception as err:
    print("also so lautet der Fehler",err)
