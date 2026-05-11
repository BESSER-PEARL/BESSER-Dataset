from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_Output:

    def __init__(self, key: str):
        self.key = key
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    def test(self) :
        # TODO: Implement test method
        pass

class test_Input:

    def __init__(self, test: str, key: str):
        self.test = test
        self.key = key
        
        pass
    @property
    def test(self):
        return self.__test

    @test.setter
    def test(self, test: str):
        self.__test = test


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

