class Car:
    def __init__(self,make,year):
        self.make=make
        self.year=year
    class Engine:
        def __init__(self,number):
            self.number=number
        def start(self):
            print("engine started")
    
c=Car("bin",2017)
e=c.Engine(123)
e.start()
