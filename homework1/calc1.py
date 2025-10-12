print('Ввидите первое значение')
first_num = int(input())
print('Ввидите второе значение')
second_num = int(input())
print('Ввидите операцию')
operator = str(input())

if operator == '+':
    print(first_num + second_num)
elif operator == '*':
    print(first_num * second_num)
elif operator == '-':
    print(first_num - second_num)
elif operator == '/':
    if second_num == 0:
        print('ZeroDivisionError')
    else:
        print(first_num / second_num)

