'''
Write your code under the commented(#) question.
'''

### Task 1

first = input('Enter first number: ')
first = int(first)

second = input('Enter second number: ')
second = int(second)

print(first+second)
print(first-second)
print(first*second)

### Task 2

num = input('Enter a number: ')
num = int(num)

if num%2 == 1:
    print('Weird')
elif num in range (2,6): #including 2 but not 6 >>> 2,3,4,5
    print('Not Weird')
elif num in range (6,21):
    print('Weird')
elif num in range (21,101):
    print('Not Weird')
else:
    print('Weird')
