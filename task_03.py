# Задайте список из n чисел последовательности
# (1+1\n)^n и выведите на экран их сумму.

def find_lim (n: int):
    result = 0
    sum = 0
    count = 0
    for i in range (1, n+1):
        result = (1 + 1/i)**i
        count += 1
        print(f"{count}: {round(result, 2)}")
        sum += result
    return(round(sum, 2))
        
       
n = int(input("Введите число - "))
print(f'Сумма чисел списка равна - {find_lim(n)}')