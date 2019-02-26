'''
Write your code under the commented(#) question. 
'''

### Task 1
# Enter your code here. Read input from STDIN. Print output to STDOUT

N1 = int(raw_input().strip())
N2 = int(raw_input().strip())

print (N1+N2)
print (N1-N2)
print (N1*N2)


### Task 2

import sys


N = int(raw_input().strip())
if N % 2 == 1:
    print ("Weird")
elif N in range(3,6):
    print ("Not Weird")
elif N in range(6,21):
    print ("Weird")
elif N in range(20, 101):
    print ("Not Weird")