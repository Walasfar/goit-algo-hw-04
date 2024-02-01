import sys
from pathlib import Path
from colorama import init, Fore, Back, Style

init()

# Стилі
folder_back = Back.YELLOW
folder_color = Fore.BLACK
item_back = Back.LIGHTMAGENTA_EX
item_color = Fore.GREEN
clear = Style.RESET_ALL

def backgroundp(answer):
    """
    Вертає якщо так то буде бекграунд.
    """
    if answer != 'y':
        return ""
    else:
        return item_back

def main(user_path, indent='  ', depth=6):
    """
    user_path - початковий путь
    indent - параметер за замовчуванням, кількість відступів - рекурсія
    """
    path = Path(user_path)
    if path.exists():
        answer = input(Fore.YELLOW + "Show backgrounde? y/n " + clear)
        
        # Якщо передали безпосередньо путь до файлу верне файл
        if path.is_file():
            return print(indent, item_back + item_color + str(path.name) + clear)
        
        if depth:
            
            print(indent, folder_back + folder_color + str(path.name) + ' ↴' + Style.RESET_ALL)
            # Проходимося по папці
            for item in path.iterdir():
                if item.is_file(): # Перевірка на файл
                    print(indent+'  ', backgroundp(answer) + item_color + str(item.name) + clear)
                
                elif item.is_dir(): # Перевірка на папку
                    main(item, indent + '  ', depth - 1)
    else:
        print(Fore.GREEN + "File or direction is not exists." + clear)



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(Fore.RED + "|You must provide argument-path.| Path to file or directory |" + clear)
    else:
        main(str(sys.argv[1]))
