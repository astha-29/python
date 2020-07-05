class patient:
    def setId(self,id):  # @ReservedAssignment
        self.id=id
    def getId(self):
        return self.id
    
        
    def setName(self,name):  # @ReservedAssignment
        self.name=name
    def getName(self):
        return self.name
            
        
    def setSSN(self,ssn):  # @ReservedAssignment
        self.ssn=ssn
    def getSSN(self):
        return self.ssn
            
s=patient()
s.setId(123)
s.setName("john")
s.setSSN(2345)

print(s.getId())
print(s.getName())
print(s.getSSN())
