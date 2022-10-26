# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
numbers = [-4, 19, 22, 20, 19, 9, 25, 16, 4]
new_list = []
for number in numbers:
    if number > 0 and (number ** 0.5) % 1 == 0:
        a = int(number ** (0.5))
        new_list.append(a)
print(new_list)
