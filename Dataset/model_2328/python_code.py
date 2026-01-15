from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TestEnum(Enum):
    testLiteral = "testLiteral"
    testLiteral2 = "testLiteral2"


############################################
# Definition of Classes
############################################

class My_TestEnum2:

    pass
class My_TestClass2:

    pass
class My_TestClass:

    def __init__(self, testAtt: str, testAtt2: str):
        self.testAtt = testAtt
        self.testAtt2 = testAtt2
        
    @property
    def testAtt(self) -> str:
        return self.__testAtt

    @testAtt.setter
    def testAtt(self, testAtt: str):
        self.__testAtt = testAtt

    @property
    def testAtt2(self) -> str:
        return self.__testAtt2

    @testAtt2.setter
    def testAtt2(self, testAtt2: str):
        self.__testAtt2 = testAtt2
