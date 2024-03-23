import re  # Імпорт модуля для роботи з регулярними виразами (Regular Expressions).
from typing import Callable  # Імпорт типу Callable для анотації типів аргументів функції.

def generator_numbers(text: str):
    # Функція, яка шукає всі числа з плаваючою точкою у тексті та повертає їх у вигляді генератора.
    numbers = re.findall(r'\b\d+\.\d+\b', text)  # Використання регулярного виразу для пошуку чисел.
    for number in numbers:
        yield float(number)  # Кожне знайдене число конвертується у десяткове число з плаваючою точкою та повертається.

def sum_profit(text: str, func: Callable):
    # Функція, яка обчислює суму чисел, отриманих з генератора.
    numbers_generator = func(text)  # Виклик функції generator_numbers для створення генератора чисел.
    total = sum(numbers_generator)  # Обчислення загальної суми чисел.
    return total  # Повернення обчисленої суми.

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)  # Виклик функції sum_profit для обчислення загального доходу.
print(f"Загальний дохід: {total_income}")  # Виведення результату обчислення загального доходу.
