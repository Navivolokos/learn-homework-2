"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt"""

from collections import Counter
    
def main():   
	with open('referat.txt', 'r', encoding='utf-8') as file1:
		fread=file1.read()
		print(fread)
		dlina=len(fread)
		print(dlina)
		num_words=len(fread.split())
		print(num_words)
		new_fread = fread.replace('.', '!')
		print(new_fread)
	with open('referat2.txt', 'w', encoding='utf-8') as file2:	
		file2.write(new_fread)
		
if __name__ == "__main__":
    main()
