class TestPythonMethod
    def _init_(self,PassSomeThingHere):
        self.PassSomeThingHere=PassSomeThingHere
        
    def setPassSomeThingHere_Name(self,PassSomeThingHere):
         self.PassSomeThingHere=PassSomeThingHere
        
    def getPassSomeThingHere_Name(self):
            return(self.PassSomeThingHere)
			
####### Test Below ############
			
test = TestPythonMethod

print (test.getTestPythonMethods())

test.setTestPythonMethods_Name("You got it ")
print(test.getTestPythonMethods_Name())