# Задайте список из n чисел последовательности
# (1+1\n)^n и выведите на экран их сумму.

def find_lim (n: int):
    res = 0
    sum = 0
    count = 0
    for i in range (1, n+1):
        res = (1 + 1/i)**i
        count += 1
        print(f"{count}: {round(res, 2)}")
        sum += res
    return(round(sum, 2))

n = int(input("Введите число - "))
print(f'Сумма чисел списка равна - {find_lim(n)}')