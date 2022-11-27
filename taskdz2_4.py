# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

with open('file.txt','r') as f:
    list = f.read().split('\n')

print('Введите число')
pos = []
n = int(input())


for i in range (-n,n + 1):
    pos.append(i)
print(f'Список из N элементов, из промежутка [{-n}, {n}] {pos}')
print(f'Список позиций из файла {list}')
for j in range(0, len(list)): 
    mult = 1
    for m in range(0,int(list[j])):
        mult = mult * int(pos[m]) 
        
    print(f'Произведение элементов позиция {[j]} {mult}')    


