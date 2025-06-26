"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
import csv
list_dic=[{"name": "Ivan", "age": 25, "job": "Scientist"},
 {"name": "Roman", "age": 8, "job": "Programmer"}, 
 {"name": "Olga", "age": 48, "job": "Big boss"}, 
 {"name": "Anna", "age": 56, "job": "small boss"}]

with open('workers.csv', 'w', newline='') as csv_file:
	keys = list_dic[0].keys()
	writer=csv.DictWriter(csv_file, keys, delimiter=';')
	writer.writeheader()
	writer.writerows(list_dic)
			
if __name__ == "__main__":
    main()
