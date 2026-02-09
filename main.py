from Todo import Todo
from Database import Database


def main():
    db = Database()

    while True:
        command = input("Enter a command: ")

        if command == "exit":
            break

        elif command == "add":
            title = input("Enter the title of your todo: ")
            todo = Todo(title)
            todo_id = db.add_todo(todo)
            print(f"Added todo (id={todo_id})")

        elif command == "remove":
            text = input("Enter the ID of the todo you want to remove: ")
            try:
                todo_id = int(text)
            except ValueError as error:
                print(f"Invalid input: {error}")
                continue

            if db.remove_todo(todo_id):
                print("Removed todo")
            else:
                print(f"Could not remove todo with id: {todo_id}")

        elif command == "todos":
            todos = db.get_todos()
            for todo_id in todos:
                todo = todos[todo_id]
                print(f"{todo_id}: {todo} (completed: {todo.completed})")

        elif command == "complete":
            text = input("Enter the ID of the todo you want to mark as completed: ")
            try:
                todo_id = int(text)
            except ValueError as error:
                print(f"Invalid input: {error}")
                continue

            todo = db.get_todo(todo_id)
            if todo is None:
                print(f"Could not find todo with id: {todo_id}")
                continue

            todo.completed = True
            print(f"Completed todo {todo_id}")

        elif command == "change":
            text = input("Enter the ID of the todo you want to change: ")
            try:
                todo_id = int(text)
            except ValueError as error:
                print(f"Invalid input: {error}")
                continue

            todo = db.get_todo(todo_id)
            if todo is None:
                print(f"Could not find todo with id: {todo_id}")
                continue

            new_title = input("Enter a new title for the todo: ")
            todo.title = new_title
            print("Changed title successfully")


if __name__ == "__main__":
    main()
