class queue:
    def __init__(self, initial_list = None) -> None:
        if initial_list == None:
            self.list = []
        else:
            self.list = initial_list

    def enqueue(self, item):
        self.list.insert(0, item)

    def dequeue(self):
        if self.list:
            return self.list.pop()
        return None        

    def items(self):
        return self.list