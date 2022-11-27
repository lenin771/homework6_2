# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

print('Введите вещественное число')
n = input()
suma = 0
 
for digit in n:
    if digit.isdigit():
        suma += int(digit)
         
print("Сумма:", suma)
