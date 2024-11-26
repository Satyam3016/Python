class Parent:
    
    def anything(self):
        print('Function defined in parent class!')
        

class Child(Parent):
    
    pass


obj2 = Child()
obj2.anything()