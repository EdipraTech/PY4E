import re

x = '''This file contains the actual data for your assignment - good luck!


Why should you learn to write programs?

Writing programs (or programming) is a very creative 
and rewarding activity.  You can write programs for 
many reasons, ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem.  This book assumes that 
everyone needs to know how to program, and that once 
you know how to program you will figure out what you want 
to 2555 do 4435 with 6336 your newfound skills. '''
y = re.findall('$', x)
print(y)