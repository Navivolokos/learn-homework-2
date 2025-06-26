"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, date, timedelta

def print_days():
	"""
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """ 
		
	today=date.today()
	
	print(f'Сегодняшняя дата: {today}')
	yesterday=today-timedelta(days=1)
	print(f'Вчерашняя дата: {yesterday}')
	days_ago_30=today-timedelta(days=30)
	print(f'30 дней назад: {days_ago_30}')

	date_object = datetime.strptime("2023-04-12", "%Y-%m-%d").date()
	print(date_object)



def str_2_datetime(date_string):
	
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_t=datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return date_t
    
if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))



