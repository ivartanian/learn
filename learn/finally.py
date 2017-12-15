import time

try:
    f = open('poemm.txt')
    while True: # наш обычный способ читать файлы
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2) # Пусть подождёт некоторое время
except FileNotFoundError:
    print('File not found!!!')
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла.')
finally:
    f.close()
    print('(Очистка: Закрытие файла)')


with open("poemm.txt") as theFile:
    for line in theFile:
        print(line, end='')