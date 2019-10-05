#4: Fraction Calculator
"""
Write a calculator that can perform the basic mathematical operations on two fractions. 
It should ask the user for two fractions and the operation the user wants to carry out. 
"""
import unicodedata
from fractions import Fraction

#Compare strings 
#https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
def normalize_caseless(text):
    return unicodedata.normalize('NFKD', text.casefold())

def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)

#Math operations
def add(a,b):
    print('Result of Addition: {0}'.format(a + b))

def subtract(a,b):
    print('Result of Subtraction: {0}'.format(a - b))

def divide(a,b):
    print('Result of Divide: {0}'.format(a / b))

def multiple(a,b):
    print('Result of Multiple: {0}'.format(a * b))

if __name__ == '__main__':
    a = Fraction(input('Enter first fraction: '))
    b = Fraction(input('Enter second fraction: '))
    op = input('Operation to permform - Add, Subtract, Divide, Multiply: ')
    
    if caseless_equal(op, 'Add'):
        add(a,b)

    elif caseless_equal(op, 'Subtract'):
        subtract(a,b)

    elif caseless_equal(op, 'Divide'):
        divide(a,b)

    elif caseless_equal(op, 'Multiple'):
        multiple(a,b)

    else:
        'invalid operation selected'