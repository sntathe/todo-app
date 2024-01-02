from functions import get_todos, write_todos
import time
#import functions
#functions.get_todos


now = time.strftime("%b %d,%Y %H:%M:%S")
print(now)
while True:
    user_action = input("Type add , show , edit , complete or Exit: ")
    user_action = user_action.strip()

    # if 'add' in user_action:
    if user_action.startswith("add"):
        # toDo = input("Enter a to Do: ") + "\n"
        toDo = user_action[4:]

        toDos = get_todos(file_path='todo.txt')

        toDos.append(toDo + '\n')

        write_todos( toDos)
    elif user_action.startswith("show"):
        toDos = get_todos()
        for index, item in enumerate(toDos):
            # for item in toDos:
            # print(item)
            # print(index, '.', item)
            index = index + 1
            item = item.strip('\n')
            row = f"{index}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            # number = int(input("Enter a Number: "))
            number = int(user_action[5:])
            number = number - 1

            toDos = get_todos()

            print(toDos[number])
            newToDo = input("Enter a new toDo: ")
            toDos[number] = newToDo + '\n'

            write_todos( toDos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("complete"):
        # number = int(input("Enter a Number: "))
        try:
            number = int(user_action[9:])

            toDos = get_todos()

            toDos.pop(number - 1)

            write_todos(toDos)
        except IndexError:
            print("There is no Index")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("This command not valid")
print("Bye")
