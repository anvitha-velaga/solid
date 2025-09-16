class Node:
    def __init__(self,value):
        self.value= value
        self.left=None
        self.right=None
    def insert(self,value):
        if value<self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left=Node(value)
        if value>self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right=Node(value)
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.value)
        if self.right:
            self.right.in_order()
    def pre_order(self):
        print(self.value)
        if self.left:
            self.left.in_order()
       
        if self.right:
            self.right.in_order()
    def post_order(self):
        
        if self.left:
            self.left.in_order()
       
        if self.right:
            self.right.in_order()
        print(self.value)
n=Node(20)
n.insert(10)
n.insert(30)
n.insert(15)
n.insert(35)
n.in_order()
print("pre-order")
n.pre_order()
print("post-order")
n.post_order()
    