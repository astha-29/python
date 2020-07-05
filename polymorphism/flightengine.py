class Flight:
    def __init__(self,engine):
        self.engine=engine
    def startEngine(self):
        self.engine.start()
        
class AirbusEngine:
    def start(self):
        print("start airbus engine")
        
class BoingEngine:
    def start(self):
        print("start BoingEngine engine")
   
ae=AirbusEngine()
f=Flight(ae)
f.startEngine()     