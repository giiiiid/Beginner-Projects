import string
import random
lower = []
upper = []
digits = []
symbol = []
password = []
upper_num = int(input('How many upper case? '))
lower_num = int(input('How many lower case? '))
digits_num = int(input('How many digits? '))
symbol_num = int(input('How many symbols? '))
for i in range(0,lower_num):
    lower.append(random.choice(string.ascii_lowercase))
for i in range(0,upper_num):
    upper.append(random.choice(string.ascii_uppercase))
for i in range(0,digits_num):
    digits.append(random.choice(string.digits))
for i in range(0,symbol_num):
    symbol.append(random.choice(string.punctuation))
password = lower+upper+digits+symbol
random.shuffle(password)
for i in password:
    print(i,end='')