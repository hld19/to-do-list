from Todo import Todo

class Database:
    def __init__(self):
        self._todos: dict[int, Todo] = {}
        self._id: int = 0

    def add_todo(self, todo: Todo) -> int:
        self._id += 1
        self._todos[self._id] = todo
        return self._id
    
    def remove_todo(self, todo_id: int) -> bool:
        if todo_id in self._todos:
            self._todos.pop(todo_id)
            return True
        else:
            return False
        
    def get_todo(self, todo_id: int) -> Todo | None:
        if todo_id in self._todos:
            return self._todos[todo_id]
        else:
            return None
    
    def get_todos(self) -> dict[int, Todo]:
        return self._todos