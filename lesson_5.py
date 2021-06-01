"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
my_string = input('Введите строку: ')
with open("Text_file", "w") as text_file:
    while my_string != '':
        text_file.write(my_string+'\n')
        my_string = input('Введите строку: ')

"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке."""
with open("Text_file") as text_file:
    lines = text_file.readlines()
    print('Количество строк в файле: ', len(lines))
    for line_num, line in enumerate(lines, 1):
        print(f'Количество слов в строке номер {line_num}: ', line.count(' ') + 1)


"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""
total = 0
with open("emploees.txt") as file:
    lines = file.readlines()
    for line in lines:
        name, surname, salary = line.split()
        total += int(salary)
        if int(salary) < 20000:
            print(f'{name} {surname} получает меньше 20000')
    print('Средняя зарплата сотрудников составляет: ', total / len(lines))

"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""
translator = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять'
}
file = open("file.txt", "r")
new_file = open('new_file', 'w')
for line in file.readlines():
    eng_number, number = line.split(' - ')
    new_file.write(f'{translator[eng_number]} - {number}')
file.close()
new_file.close()

"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран"""
with open("file.txt", "w") as file:
    numbers = input('Введите числа через пробел: ')
    file.write(numbers)

with open("file.txt", "r") as file:
    numbers = file.read().rstrip().split()
    total = 0
    for number in numbers:
        if number.isdigit() is True:
            total = total + int(number)
        else:
            continue
    print('Сумма введенных чисел: ', total)

"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран."""
result = {}
with open("lessons.txt", "r") as file:
    for line in file.readlines():
        lesson_type, *hours = line.split()
        count = [int(hour.rstrip('(л)(пр)(лаб)')) for hour in hours if hour != '-']
        result.update({lesson_type: sum(count)})
print(result)

"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл."""
import json
companies = {}
av_profit_dict = {}
average_profit_list = []
result_list = []
with open('companies.txt') as file:
    for line in file.readlines():
        name = line.split()[0]
        revenue = int(line.split()[2])
        waste = int(line.split()[3])
        profit = revenue - waste
        companies.update({name: profit})
        if profit >= 0:
            average_profit_list.append(profit)
            print(f'Прибыль компании {name} составила {profit}')
    av_profit = sum(average_profit_list) / len(average_profit_list)
    av_profit_dict.update({'average_profit': av_profit})
    result_list.insert(0, companies)
    result_list.insert(1, av_profit_dict)
    print(result_list)

with open('result.json', 'w') as file:
    json.dump(result_list, file)