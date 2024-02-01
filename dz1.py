'''
Functions take a path to file with data salaries,
and return tuple with total salary and average salaries.
'''

def total_salary(path):
    # Пробуємо відкрити файл
    try: 
        with open(path, 'r', encoding='utf-8' ) as file:

            total_salary = 0
            all_salaries = []
            
            while True:

                line = file.readline()
                
                # Коли рядки закінчаться цикл перестане читати файл
                if not line:
                    break
                
                # Забираємо зарплату та перетворюємо на int
                salary = int(line.split(",")[1])
                total_salary += salary
                all_salaries.append(salary)
                average_salary = total_salary / len(all_salaries)
                
    except FileNotFoundError:
        print("File not found!")
        return 0
    
    return [total_salary, average_salary]

total, average = total_salary('dz1.txt')
print(f"total_salary: {total}, average_salary: {average}")

