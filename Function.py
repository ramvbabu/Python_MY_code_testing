import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from Log_File import logger

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
logger.info(f'Sum of {a} and {b} is {sum(a, b)}')

#change push
print("sairam")
print("naresh")
print("kumar")