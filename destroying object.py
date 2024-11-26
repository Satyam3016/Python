class Animals:  
    
    #  we will initialize the class  
    def __init__(self):  
        print('The class called Animals is CREATED.')  
    
    # now, we will Call the destructor  
    def __del__(self):  
        print('The destructor is called for deleting the Animals.')  
    
object = Animals()  
del object  