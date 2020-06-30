class person:
    def setfullname(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def printfullname(self):
        print(self.firstname," ",self.lastname)
personname=person()
personname.setfullname("raju","ramu")
personname.printfullname()
