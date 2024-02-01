import sys
from pathlib import Path
from colorama import init, Fore, Back, Style

init()

# Стилі
folder_back = Back.YELLOW
folder_color = Fore.BLACK
item_back = Back.LIGHTCYAN_EX
item_color = Fore.BLACK
clear = Style.RESET_ALL

def main(user_path, indent=' ', depth=5):
    """
    user_path - початковий путь
    indent - параметер за замовчуванням, кількість відступів - рекурсія
    """
    path = Path(user_path)
    
    if path.exists():
        if depth:
        
            # Проходимося по папці
            for item in path.iterdir():    
                if item.is_file(): # Перевірка на файл
                    print(indent, item_back + item_color + str(item.name) + clear)
                
                elif item.is_dir(): # Перевірка на папку
                    print(indent, folder_back + folder_color + str(item.name) + ' ↴' + Style.RESET_ALL)
                    main(item, indent * 2, depth - 1)
    else:
        print("File or direction is not exists.")



if __name__ == '__main__':
    main(str(sys.argv[1]))
