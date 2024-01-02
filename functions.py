
def get_todos(file_path='todo.txt'):
    """" get to dos from list"""
    with open(file_path, 'r') as file:
        toDos = file.readlines()
    return toDos


def write_todos(todos , file_path='todo.txt'):
    """" write to dos from list"""
    with open(file_path, 'w') as file:
        file.writelines(todos)
