# Приймає команду юзера
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  
    return cmd, *args

# Добавляє контакт в базу
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

# Міняє номер
def change_number(args, contacts):
    name, new_number = args
    if name in contacts:
        contacts[name] = new_number
        return "Contact updated."
    else:
        return "Name not found!"

def show_base(adress_book):
    for key, value in adress_book.items():
        return (f"Name: {key}, number: {value}")

commands = "Commands:\n\tall;\n\tcommands\n\tadd user number;\n\tphone user;\n\tchange user number;\n\texit/quit/close"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print(commands)
    
    # Цикл бота
    while True:
        
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        try:
            if command in ["close", "quit", "exit"]:
                print("Good bye!")
                break
            
            elif command == 'hello':
                print("Hello im Jarvis! Im here for help you!")
            
            elif command == 'all':
                
                if len(contacts) == 0:
                    print("Base is empty.")
                    
                else:
                    print(show_base(contacts))
                
            match command:    
                case 'add':
                    add_contact(args, contacts)
                    
                case 'change':
                    print (change_number(args, contacts))
                    
                case 'phone':
                    
                    if len(contacts) > 0:
                        print(f"Phone {args[0]} - {contacts[args[0]]}")
                    else:
                        print("User not found.")
                    
                case 'commands':
                    print(commands)
                    
        except ValueError as e:
            print("Number argumets is required!")

if __name__ == "__main__":
    main()
