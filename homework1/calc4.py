import math
from typing import Union

class Calculator:
    def expression(self, a: int, b: int, c: str) -> Union[str, int, float]:
        #вычесление простых арифметических операций
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

    def trygonometry (self, a: float, c: str ) -> Union[None, str, int, float]:
        #вычисление тригонометрических операций
        if c == 'sin':
            return math.sin(a)
        elif c == 'cos':
            return math.cos(a)
        elif c == 'tg':
            return math.tan(a)
        else:
            return "NoFunctionError"


calc = Calculator()
print("Выберите нужное действие: 1)Аримфетика; 2)Тригонометрия")
ver = int(input())
if ver == 1:
    print('Ввидите первое значение')
    first_num = int(input())
    print('Ввидите второе значение')
    second_num = int(input())
    print('Ввидите операцию')
    operator = str(input())
    print(calc.expression(first_num, second_num, operator))
elif ver == 2:
    print('Ввидите угол в градусах')
    num = int(input())
    num = math.radians(num)
    print('Ввидите функцию: sin, cos, tan')
    operator = str(input())
    print(calc.trygonometry(num, operator))
