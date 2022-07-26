# Задайте список из N элементов,
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


def get_numbers(n: int):
    ran = range(- n, n + 1) 
    numbers = list(ran)
    return(numbers)


n = int(input("Введите число - "))
spisok = get_numbers(n)
print(f'Список чисел из промежутка [{-n}:{n}] - {spisok}')
path = open('file.txt', 'r')
s = int(path.readline())
print(f'Номер первой позиции из файла file.txt -  {s}')
d = int(path.readline(1))
print(f'Номер второй позиции из файла file.txt -  {d}')

multi = spisok[s] * spisok[d]
print(f'{multi} - произведение чисел на указанных позициях')

