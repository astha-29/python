from abc import abstractmethod,ABC
class TouchScreenLaptop(ABC) :
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop) :
    def __init__(self, HPNotebook , make , model, year):
        super().__init__(make , model , year)
        self.HPNotebook = HPNotebook

    def scroll(self):
        super().scroll()
        print("HP has enabled scrolling")

    def click(self):
        super().click()
        print("This notebook has a click")

class  Dell(TouchScreenLaptop) :
    def __init__(self,DellNotebook, make , model, year):
        super().__init__(make , model , year)
        self.DellNotebook = DellNotebook

    def scroll(self):
        super ().scroll()
        print ( "Dell has enabled scrolling" )

    def click(self):
        super().click()
        print("This notebook has a click")



hp = HP(True , "HP", "INTEL", "2019")

print(hp.HPNotebook, hp.make , hp.model , hp.year)

hp.scroll()
hp.click()
dell = Dell(True , "DELL", "Vostro", "2019")

print(dell.DellNotebook, dell.make , dell.model , dell.year)

dell.scroll()
dell.click()