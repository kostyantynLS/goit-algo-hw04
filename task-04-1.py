'''
Перше завдання
У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників 
у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, 
які розділені комою без пробілів.
'''
import os

def total_salary(path_to_salary_text = "salary.txt") -> tuple:

    total = 0
    average = 0
    items = 0
#check&open file
    if not os.path.exists(path_to_salary_text):
        print(f'file {path_to_salary_text} not exist!')
    else:   
        with open(path_to_salary_text, "r", encoding="utf-8") as salary_file: #path_to_salary_text
            salaries = salary_file.readlines()
            for lines in salaries:
                try:
                    name, value = lines.split(',')
                    val_int = int(value)
                    items += 1
                    total += val_int
                except ValueError:
                    print(f'invalid error at line {lines}', end="")
            #check average
            if items >0:
                average = total / items
                average = round(average, 2) # as XXXXXX.YY
            else:
                print('No salaries found')

    return (total, average)
