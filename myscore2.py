# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score 
# as its parameter and returns a grade as a string.
# Score   Grade
# > 0.9     A
# > 0.8     B
# > 0.7     C
# > 0.6     D
# <= 0.6    F

# Program Execution:

# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F


#==============================================================================================================
# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:


inp = raw_input('Geben Sie einen Score zwischen 0.0 und 1.0 ein!\n')

def computegrade(p_score):
   if p_score > 1.0 or p_score < 0.0:
      r_grade = 'Schlechtes Ergebnis!'
   elif p_score >= 0.9:
      r_grade = 'A'
   elif score >= 0.8:
      r_grade = 'B'
   elif score >= 0.7:
      r_grade = 'C'
   elif score >= 0.6:
      r_grade = 'D'
   else:
      r_grade = 'F'
   return r_grade

try:
   p_score = float(inp) 
except:
   p_score = -1

print computegrade(inp)
