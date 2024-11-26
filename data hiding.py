class CounterClass:  
   __privateCount = 0  
   def count(self):  
      self.__privateCount += 1  
      print(self.__privateCount)  
counter = CounterClass()  
counter.count()  
counter.count()  
print(counter.__privateCount)  