def power_recursive(A, B):
    if B == 0:
        return 1
    elif B > 0:
        return A * power_recursive(A, B - 1)
    else:  
        return 1 / (A * power_recursive(A, -B - 1))

A = int(input("Введите степеннь: "))
B = int(input("Введите число: "))
result = power_recursive(A, B)
print(f'{A} в степени {B} = {result}')