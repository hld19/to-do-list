from Todo import Todo
from Database import Database

def main():
    database = Database()
    
    run = True

    while run:
        command = input("Enter a command: ")

        if command == "exit":
            run = False
            continue
        elif command == "add":
            title = input("Enter the title of your todo: ")
            todo = Todo(title)
            id = database.add_todo(todo)
            print(f"Added todo (id={id})")
        elif command == "remove":
            id = input("Enter the ID of the todo you want to remove: ")
            try:
                id = int(id)
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue

            if database.remove_todo(id):
                print("Removed todo")
            else:
                print(f"Could not remove todo with id: {id}")
        elif command == "todos":
            todos = database.get_todos()
            for id in todos:
                print(f"{id}: {todos[id]} (completed: {todos[id].completed()})")
        elif command == "complete":
            id = input("Enter the ID of the todo you want to mark as completed: ")
            try:
                id = int(id)
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue
        
            database.get_todo(id).mark_completed()
            print(f"Completed todo {id}")

        elif command == "change":
            id = input("Enter the ID of the todo you want to change: ")
            try:
                id = int(id)
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue

            todo = database.get_todo(id)
            if todo is None:
                print(f"Could not find todo with id: {id}")
                continue

            new_title = input("Enter a new title for the todo: ")
            todo.change_title(new_title)
            print("Changed title successfully")


if __name__ == "__main__":
    main()