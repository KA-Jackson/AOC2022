class file_directory:
    def __init__(self, dir_name, parent_dir = None) -> None:
        self.name = dir_name
        self.parent = parent_dir
        self.dirs = []
        self.files = {}

    def add_sub_dir(self, dir_name):
        child_dir = file_directory(dir_name, self)
        self.dirs.append(child_dir)

    def add_file(self, file_name, file_size):
        self.files[file_name] = int(file_size)

    def move_to_sub_dir(self, child_name):
        for dir in self.dirs:
            if dir.name == child_name:
                return dir

    def move_to_parent_dir(self):
        return self.parent

    def size(self):
        size = 0
        for dir in self.dirs:
            size += dir.size()
        size += sum(self.files.values())
        return size

    def directory_list(self):
        dir_list = [self]
        
        for dir in self.dirs:
            dir_list.extend(dir.directory_list())
        return dir_list

    def __str__(self, depth = 0):
        val = '  ' * depth + '- ' + self.name + ' (dir)\n'
        depth += 1
        for dir in self.dirs:
            val += dir.__str__(depth)
        for name, size in self.files.items():
            val += '  ' * depth + '- ' + name + ' (file, size=' + str(size) + ')\n' 
        return val