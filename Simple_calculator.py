def add(num1,num2):
    ans = num1+num2
    return ans
def sub(num1,num2):
    ans = num1-num2
    return ans
def mul(num1,num2):
    ans = num1*num2
    return ans
def div(num1,num2):
    ans = num1/num2
    return ans

while True:
    request = input('Would you like to add/sub/mul/div? ')

    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    if request == 'add':
        print(add(num1, num2))
    elif request == 'sub':
        print(sub(num1, num2))
    elif request == 'mul':
        print(mul(num1, num2))
    elif request == 'div':
        print(div(num1, num2))
    else:
        print('Invalid digits')