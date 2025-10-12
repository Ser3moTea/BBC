from typing import Union

def level_1(a: str, h: int) -> str:
    """
    Уровень 1: изменение регистра строки
    Методы: str.upper(), str.lower(), str.capitalize()
    Аргументы: a - пользовательская строка, h - выбранный режим
    """
    if h == 1:
        print(f"Перенос всех символов в верхний регистр: {a} в {a.upper()}")
    if h == 2:
        print(f"Перенос всех символов в нижний регистр: {a} в {a.lower()}")
    if h == 3:
        print(f"Строка с большой буквы: {a} в {a.capitalize()}")
def level_2(b: str, m: int, word: str, word2: str, word3: str, word4: str) -> str:
    """
    Уровень 2: нахождение вхождений подстроки в строку, замена символов и их подсчет
    Методы: str.find(str), str.replace(str, str), str.count(str)
    Аргументы: b - пользовательская строка, m - выбранный режим, word1 - строка для поиска вхождения, word2 - строка замены, word3 - строка на которую заменяют, word4 - строика подсчета символов
    """
    if m == 1:
        print(f"первое вхождение {word1}: {str(b.find(word1))}")
    if m == 2:
        print(f"замена '{word2}' на '{word3}': {b.replace(word2, word3)}")
    if m == 3:
        print(f"количество символов {word4}: {str(b.count(word4))}")
def level_3(c: Union[list[str], str], e: int, sign1: str, sign2: str) -> str:
    """
    Уровень 3: разделение строки на подстроки и обратное воссоединение
    Методы: str.split(str), str.join(str)
    Аргументы: с - пользовательская строка, е - выбранныый режим,  sigh1 - знак разделитель, sign2 - знак соединитель
    """
    if e == 1:
        print(f"разделение по '{sign1}' : {c.split(sign1)}")
    if e == 2:
        print(f"обратное соединение через '{sign2}' : {sign2.join(c)}")
def level_4(d: str, f: int, des: str) -> str:
    """
    Уровень 4: проверка строк на состав, удаление элементов в конце и начале
    Методы: str.isdigit(), str.isalpha(), str.strip()
    Аргументы: d - пользовательская строка, f - выбранныый режим, des - удаляемые символы
    """
    if f == 1:
        print(f"строка пользователя: '{d}', состоит ли она только из цифр - {d.isdigit()}")
    if f == 2:
        print(f"строка пользователя: '{d}', состоит ли она только из букв - {d.isalpha()}")
    if f == 3:
        print(f"строка пользователя: '{d}', строка без удаленных символов '{des}' - '{d.strip(des)}'")
def level_5(ustr: str) -> str:
    """
    Уровень 5: полное пошаговое преобразование строки
    Методы: str.strip(), str.replace(), str.capitalize(), ''.join(str)
    Аргументы: ustr
    """
    step1 = ustr.strip()
    step2 = step1.replace(";", ",", 2)
    step3 = step2.replace(";", "")
    step4 = step3.replace(",", " ")
    step5 = step4.capitalize()
    step6 = ' '.join(step5.split())
    result = step6
    print(f"Преобазование {ustr} в {result}")

print('Ввидите уровень')
lvl = int(input())
if lvl == 1:
    print('Ввидите текст')
    text = str(input())
    print('Что хотите сделать: 1)Написать текст в верхнем регистре; 2)Написать текст в нижнем регистре; 3)Написать текст с заглавной буквы')
    mod = int(input())
    level_1(text, mod)
if lvl == 2:
    word, word2, word3, word4 = '', '', '', ''
    print('Ввидите текст')
    text_2 = str(input())
    print("Что вы хотите найти?")
    word1 = str(input())
    print("Что вы хотите заменить?")
    word2 = str(input())
    print("На что хотите заменить?")
    word3 = str(input())
    print("Что вы хотите посчитать?")
    word4 = str(input())
    print(f"строка пользователя: {text_2}")
    level_2(text_2, 1,  word1, '', '', '')
    level_2(text_2, 2,  '', word2, word3, '')
    level_2(text_2, 3, '', '', '', word4)
if lvl == 3:
    print('Ввидите текст')
    text_3 = str(input())
    print('Ввидите по какому знаку разделять')
    sign1 = str(input())
    print('Ввидите с каким знаком соединять')
    sign2 = str(input())
    print(f"строка пользователя: {text_3}")
    level_3(text_3, 1, sign1, '')
    text_3 = text_3.split(',')
    level_3(text_3, 2, '', sign2)
if lvl == 4:
    print('Ввидите текст, который хотите проверить на состав из чисел')
    text_4a = str(input())
    print('Ввидите текст, который хотите проверить на состав из букв')
    text_4b = str(input())
    print('Ввидите текст, который хотите проверить на состав из букв и из которого хотите удалить символы по краям')
    text_4c = str(input())
    print('Какие символы вы хотите удалить')
    des = str(input())
    level_4(text_4a, 1, '')
    level_4(text_4b, 2, ''), level_4(text_4c, 2, '')
    level_4(text_4c, 3, des)
if lvl == 5:
    print('Ввидите текст')
    text_5 = str(input())
    level_5(text_5)
#python;IS;AWEsomE;!
#Ботать – это круто. Очень круто!
# 1, 2, 3, 4, 5, 6
