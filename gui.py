import functions
import PySimpleGUI as sg
import time

# import functions
# functions.get_todos

sg.theme("Black")
clock = sg.Text('', key='clock')
label = sg.Text("Type in a To-Do")

input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("complete")

window = sg.Window("My To Do App",
                   layout=[[label],
                           [clock],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window['clock'].Update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_to_do = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_to_do
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select Item First", font=("Helvetica", 20))

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'complete':
            try:
                todo_to_delete = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_delete)
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select Item First", font=("Helvetica", 20))

        case sg.WIN_CLOSED:
            break

window.close()
