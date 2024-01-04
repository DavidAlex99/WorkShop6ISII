import task

class ToDo:
    def __init__(self):
        self.toDoList = ['a', 'b', 'c']

    def print_list(self):
        for item in self.toDoList:
            print(item)

    def remove_items(self):
        self.toDoList.clear()


todo = ToDo()
todo.print_list()
todo.remove_items()


