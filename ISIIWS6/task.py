class Task:
    def __init__(self):
        self.completed = False
        self.name = ""

    def set_completed(self, state):
        self.completed = state

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_completed(self):
        return self.completed

