class Todo:
    def __init__(self, title: str, completed: bool = False):
        self._title = title
        self._completed = completed

    def completed(self) -> bool:
        return self._completed

    def mark_completed(self, completed: bool = True):
        self._completed = completed

    def get_title(self) -> str:
        return self._title

    def change_title(self, title: str):
        self._title = title

    def __str__(self) -> str:
        return self._title