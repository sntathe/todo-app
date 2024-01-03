import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")

input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")

window = sg.Window("My To Do App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            toDos = functions.get_todos()
            new_todo = values['todo']
            toDos.append(new_todo)
            functions.write_todos(new_todo)
        case sg.WIN_CLOSED:
            break


window.close()
