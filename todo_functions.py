def read_todos():
    with open('todo.txt', 'r+') as second_todo_file:
        current_todos = second_todo_file.read()
        print("--------")
        print("Your current to dos are: \n", current_todos)


def write_todo(new_input):
    with open('todo.txt', 'a+') as second_todo_file:
        second_todo_file.write(new_input)


action = input('Would you like to view your to do items or make a new one? (view/make)')

if action == 'view':
    read_todos()
elif action == 'make':
    user_input = input('What else do you need to do? ')
    write_todo('\n' + user_input)
