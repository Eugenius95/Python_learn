class Parent:
    def __init__(self, name):
        print("I am parent", name)
        
class child(Parent):
    def __init__(self):
        print("I am child")
        Parent.__init__(self, "")
    
child_obj = child()