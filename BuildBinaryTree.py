"""
# Created by anastasia on 11/8/20
"""

# build a tree from a list of numbers

class Node:
    def __init__(self, data):
        self.left = None
        self.right=None
        self.root = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.root)
        if self.right:
            self.right.PrintTree()



    def insert(self,data):
        if self.root:
            if data < self.root:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.root:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.root = data



root = Node(10)
root.insert(34)
root.insert(67)
root.insert(5)

root.PrintTree()