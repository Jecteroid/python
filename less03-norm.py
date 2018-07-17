# coding utf-8

# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

list_name = ['Гриша', 'Артемий', 'Артём', 'Маша', 'Саша', 'Вадим']
list_salary = [100000, 50000, 1000000, 50000, 75000, 245000]

list_name = list(map(lambda name: name.upper(), list_name))

list_name_salary = dict(zip(list_name, list_salary))

print(list_name_salary)

with open('salary.txt', 'w', encoding='utf-8') as file_salary:
    for name, salary in list_name_salary.items():
        if salary <= 500000:
            file_salary.write(f'{name} - {salary}\n')

with open('salary.txt', 'r', encoding='utf-8') as file_salary:
    for line in file_salary.readlines():
        name, salary = line.split(' - ')
        salary = int(salary) * 0.87
        print(f'{name} - {salary}')