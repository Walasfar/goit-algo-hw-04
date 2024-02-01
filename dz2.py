def get_cats_info(filename):
    
    list_of_cats = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            
            while True:
            
                line = file.readline().rstrip() # Видаляю символ переносу рядка
                cat_data = line.split(',')

                if not line:
                    break
                
                cat = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]} # Шаблон для котика
                list_of_cats.append(cat)
                
    except FileNotFoundError:
        
        print("File not found or corrupted!")
        return 0
    
    return list_of_cats

cats = get_cats_info("dz2.txt")

for cat in cats:
    print(cat)



