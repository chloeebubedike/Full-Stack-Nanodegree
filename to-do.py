
with open('todo.txt', 'a+') as todo_file:
    # Go back to the start of the to do file if it exists
    todo_file.seek(0)
    # Read the contents of the existing to do list
    existing_todos = todo_file.read()
    # print the contents of the existing to do list
    print("Existing to do items", existing_todos)

    # Ask user to input new to do item
    new_todo = input('Enter a new to do item:')
    # Add the new item to do list
    todo_file.write(new_todo + '\n')

    # Going back up to the top of the to do file
    todo_file.seek(0)
    # Read the items in the updated to do list
    updated_todos = todo_file.read()
    # print the items in the updated to do list
    print("Updated to do items")
    print(updated_todos)


