import sys


def totalPrint(initial=5, *numbers, **keywords):
    '''Выводит максимальное из двух чисел.'''
    print(initial)
    for number in numbers:
        print(number)
    for key in keywords:
        print(keywords[key])

print(totalPrint(10, '11', "22", '33', vegetables=50, fruits=100))
print(totalPrint.__doc__)

help(totalPrint)

