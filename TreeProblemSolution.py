# Build a Tree
## Why does this code go in an infinite loop?
class Node:
    #children = []
    def __init__(self, name, parent=None):
        self.children = []
        self.name = name
        self.parent = parent
        
        #print("id of parent",id(parent),"parent",parent)
        #print("id of None",id(None))
        
        if parent is not None:
            #print("id of parent inner",id(parent),"parent",parent)
            #print("id of None inner",id(None))
            parent.children.append(self)
            
    def __str__(self):
        return self.name
    
    def get_children_list(self):
        return self.children
    
    #for debugging 
    def print_children_list(self):
        for item in self.children:
            print(item,"parent", self.parent,"node_name",self.name)
        
        
  
def printer(root, level=0):
    print(" "*level+ "|-", root.name)
    for node in root.children:
        printer(node, level+1)


if __name__ == "__main__":
    root = Node("Root")
    node1 = Node("1",root)
    node11 = Node("1.1", node1)
    node12 = Node("1.2", node1)
    node13 = Node("1.3", node1)
    node14 = Node("1.4", node1)
    node15 = Node("1.5", node1)
    node2 = Node("2",root)
    node21 = Node("2.1", node2)
    node22 = Node("2.2", node2)
    node23 = Node("2.3", node2)
    node24 = Node("2.4", node2)
    node25 = Node("2.5", node2)
    node3 = Node("3",root)
    
    printer(root)
    
     
    #node3.print_children_list()
    