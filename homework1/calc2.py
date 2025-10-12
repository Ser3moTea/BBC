def summ (a: int, b: int, c: str) -> int:
    return first_num + second_num
def minus (a: int, b: int, c: str) -> int:
    return first_num - second_num
def multiply (a: int, b: int, c: str) -> int:
    return first_num * second_num
def division (a: int, b: int, c: str) -> float:
    return first_num / second_num

print('Ввидите первое значение')
first_num = int(input())
print('Ввидите второе значение')
second_num = int(input())
print('Ввидите операцию')
operator = str(input())

if operator == '+':
    print(summ (first_num, second_num, operator))
elif operator == '-':
    print(minus (first_num, second_num, operator))
elif operator == '*':
    print(multiply (first_num, second_num, operator))
elif operator == '/':
    if second_num == 0:
        print('ZeroDivisionError')
    else:
        print(division (first_num, second_num, operator))
