#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*
#6 -> 1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

x = int(input("Введите общее количество журавликов, которые сделали все дети: "))
a = int(x/3/2)
b = int(x/3*2)
print(f"Катя сделала {b} журавликов")
print(f"Петя и Сережа сделали по {a} журавликов")
print(a, b, a)