class Tree:
    def __init__(self):
        self.top = Node("/", "dir", 0, None)
    
    def dir_size(self, start=""):
        if not start: start = self.top
        total = 0
        for x in start.children:
            if x.n_type == "file":
                total += x.size
            else:
                total += self.dir_size(start=x)
        return total

    def find_dir(self, dirname, start=""):
        if not start: start = self.top
        
        if start.value == dirname and start.n_type == "dir":
            return start
    
        for x in start.children:
            
            if x.n_type == "file":
                pass
            elif x.value == dirname:
                return x

        for x in start.children:
            if x.n_type == "dir":
                return self.find_dir(dirname, start=x)

    def find_file(self, fname, start=""):
        if not start: start = self.top
        for x in start.children:
            if x.n_type == "dir":
                pass
            elif x.value == fname:
                return x
            
        return self.find_file(fname, start=x)

    def add_child(self, dname, child, dir_obj=None):
        if dir_obj is None: d = self.find_dir(dname)
        else: d = dir_obj
        child.parent = d
        d.children.append(child)

class Node:
    def __init__(self, value, n_type, size, parent=None):
        self.value = value
        self.size = size 
        self.n_type = n_type
        self.children = []
        self.parent = parent


with open("day7.txt", "r") as f:
    instructs = f.readlines()

    top = Tree()
    curr_dir = top.top
    dir_list = []
    name_list = []
    for _ in instructs:
        i = _[:-1]
        if i[0] == "$":
            command = i[2:4]
            if command == "cd":
                directory = i[5:]
                if directory == "/":
                    curr_dir = top.top
                elif directory == "..":
                    curr_dir = curr_dir.parent
                else:
                    child = Node(directory, "dir", 0)
                    top.add_child("", child, dir_obj=curr_dir)
                    curr_dir = child
                    dir_list.append(child)
                    name_list.append(directory)

        else:
            size = i[:i.index(" ")]
            name = i[i.index(" ")+1:]
            try:
                child = Node(name, "file", int(size))
                top.add_child("", child, dir_obj=curr_dir)
            except ValueError:
                child = Node(name, "dir", 0)
                top.add_child("", child, dir_obj=curr_dir)
                dir_list.append(child)
                name_list.append(directory)

    smallest = 70000000
    for d in dir_list:
        s = top.dir_size(start=d)
        if s < smallest and s >= 1035571:
            smallest = s

    print(smallest)
    