'''
Write your code under the commented(#) question.
'''

### Task 1
num1 = input('Enter number: ')
int(num1)
num2 = input('Enter number: ')
int(num2)
Sum = num1 + num2
print(Sum)
Difference = num1 - num2
print(Difference)
Product = num1 * num2
print(Product)
### Task 2
N = input('Enter number: ')
if N % 2 == 1:
    print('weird')
elif N in range (2,6):
    print('Not Weird')
elif N in range(6,21):
    pritn('weird')
elif N in range(20, 101):
    print('Not Weird')
else:
    print('weird')
