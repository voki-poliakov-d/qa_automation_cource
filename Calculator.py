def add (a, b= None):
    if b is None:
        if isinstance(a, (list, tuple, set)):
            return sum(a)
        return a
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

import re

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculate():
    pattern = r'^\s*(-?\d+(\.\d+)?)\s*([\+\-\*/])\s*(-?\d+(\.\d+)?)\s*$'

    while True:
        expr = input("Введите пример: ")

        match = re.match(pattern, expr)
        if match:
            num1, _, operator, num2, _ = match.groups()
            num1 = float(num1)
            num2 = float(num2)

            result = operations[operator](num1, num2)
            print(f"Результат: {result}")
            break

        else:
            print("Ошибка: некорректный ввод. Попробуйте снова.")



calculate()

2



