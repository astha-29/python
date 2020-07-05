class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
        
        def start(self):
            print("start the car")
        
        
        def stop(self):
            print("stop the car")
        
        
        
class ThreeSeries(BMW):
    def __init__(self,
                 cruiseControlEnabled,  # @UnusedVariable
                 make,
                 model,
                 year):
        BMW.__init__(self, make, model, year)
        self.cruiseControlEnabled=cruiseControlEnabled
        
        
        def start(self):
            print(" button start ")
        
        
        
        
        
class FiveSeries(BMW):
    def __init__(self,
                 parkingAssistEnabled,  # @UnusedVariable
                 make,
                 model,
                 year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled=parkingAssistEnabled
        
    
threeseries=ThreeSeries(True,"BMW","328i","2018")
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)

ThreeSeries.start()
ThreeSeries.stop()