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
            
        return find_file(fname, start=x)

    def add_child(self, dname, child):
        directory = self.find_dir(dname)
        child.parent = directory
        directory.children.append(child)

class Node:
    def __init__(self, value, n_type, size, parent):
        self.value = value
        self.size = size 
        self.n_type = n_type
        self.children = []
        self.parent = None


with open("day7.txt", "r") as f:
    instructs = f.readlines()

    top = Tree()
    curr_dir = top
    for _ in instructs:
        i = _[:-1]
        if i[0] == "$":
            command = i[2:4]
            if command == "cd":
                directory = i[5:]
                if directory == "/":
                    curr_dir = top
    

# directory = Tree()
# a_dir = Node("a", "dir", 0)
# e_dir = Node("e", "dir", 0)
# i_file = Node("i", "file", 584)
# f_file = Node("f", "file", 29116)
# g_file = Node("g", "file", 2557)
# h_file = Node("h.lst", "file", 62596)
# b_file = Node("b.txt", "file", 14848514)
# c_file = Node("c.dat", "file", 8504156)
# d_dir = Node("d", "dir", 0)
# j_file = Node("j", "file", 4060174)
# d_file = Node("d.log", "file", 8033020)
# d2_file = Node("d.ext", "file", 5626152)
# k_file = Node("k", "file", 7214296)

# directory.add_child("/", a_dir)
# directory.add_child("/", b_file)
# directory.add_child("/", c_file)
# directory.add_child("/", d_dir)
# directory.add_child("a", e_dir)
# directory.add_child("a", f_file)
# directory.add_child("a", g_file)
# directory.add_child("a", h_file)
# directory.add_child("e", i_file)
# directory.add_child("d", j_file)
# directory.add_child("d", d_file)
# directory.add_child("d", d2_file)
# directory.add_child("d", k_file) 

# print(directory.dir_size())
