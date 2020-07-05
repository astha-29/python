class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
    def average(self):
        numberOfratings=len(self.ratings)
        average=sum(self.ratings)/numberOfratings
        print("average ratings of ",self.name,"is",average)



c1=Course("java course",[1,2,3,4])
print(c1.name)
print(c1.ratings)
c1.average()