"""
Create a to-list program that writes user input to a file

The program should:
1. Ask the user to input a new to-do item
2. Read the contents of the existing to-do items
3. Add the new to do item to the existing to-do items
4. Save the updated to-do items

Manually create a new file called todo.txt in the same folder as your program before you start
# write the file before you read the file
"""

user_todo = input("Add an item to the to-do list: ")

# adds information to the file
with open('todo.txt', "w") as text_file:
    text_file.write(user_todo)

# Another section to append
user_todo2 = input("Add another item to the to-do list: ")

with open("todo.txt", "a") as text_file:
    text_file.write("\n"+ user_todo2)

# reads the file
with open("todo.txt", "r") as text_file:
    todolist = text_file.read()

    print(todolist)








