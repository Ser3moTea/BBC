from typing import Union
def expression(a: int, b: int, c: str) -> Union[str, int, float]:
    #вычесление выражения
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
            if b == 0:
                return 'ZeroDivisionError'
            else:
                return a / b
    else:
        return "NoFunctionError"

print('Ввидите первое значение')
first_num = int(input())
print('Ввидите второе значение')
second_num = int(input())
print('Ввидите операцию')
operator = str(input())
print(expression(first_num, second_num, operator))

