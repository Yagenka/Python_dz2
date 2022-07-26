# Напишите программу,
# которая принимает на вход
# вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = float(input("Введите вещественное число - "))
str_num = str(num).replace(".","")

def sum_float (str):
    sum = 0
    for i in str_num:
        sum = sum + int(i)
    return(sum)

summa = sum_float (str_num)
print(f'Cумма цифр в числе {num} равна {summa}')

