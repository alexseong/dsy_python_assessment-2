# Assessment #2

Welcome to our second assessment! You will have 30 minutes to complete the assignment at which time you will be asked to submit a pull request.

* Time: 30 minutes
* Open book
* Individual

## Assignment

The goal of this assignment is to fill in each function stub to make the associated test pass.

There are 5 questions over general python

The repository has the following folder structure:

    dsy_python_assessment-2
    ├── README.md
    └── src
       └── assessment.py
    

* If you need help forking, cloning and pulling with git, look at the instructions in the precourse: [How to Submit](https://github.com/alexseong/dsy_python_programming#how-to-submit-the-assignments)

Please read following tasks and write your code in `src/assessment.py` file. 

### Task 1 

Read two integers from STDIN and print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

<b>Input Format</b>

The first line contains the first integer, a. The second line contains the second integer, b.


<b>Output Format</b>

Print the three lines as explained above.

<b>Sample Input</b>

    3
    2

<b>Sample Output</b>

    5
    1
    6

<b>Explanation</b>

    3 + 2 ==> 5
    3 - 1 ==> 1
    3 * 2 ==> 6
 


### Task 2

Given an integer, n, perform the following conditional actions:
(You need to use <b>input()</b> function)

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird

<b>Input Format</b>

A single line containing a positive integer, .

<b>Constraints</b>
1 <= n <= 100

<b>Output Format</b>

Print Weird if the number is weird; otherwise, print Not Weird.

<b>Sample Input</b>

    3

<b>Sample Output</b>

    Weird

<b>Explanation</b>

    n = 3 
    n is odd and odd numbers are weird, so we print Weird.

<b>Sample Input</b>

    24

<b>Sample Output</b>

    Not Weird

<b>Explanation</b>

    n = 24 
    n > 20 and n is even, so it isn't weird. Thus, we print Not Weird.