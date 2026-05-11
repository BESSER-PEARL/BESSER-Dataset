from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractD:

    pass
class test_ast_D(AbstractD):

    def __init__(self, someBool: bool, someOtherBool: str, index: int, name: str, someQCollection: str, someCollection: str, test_ast_D: "D" = None, test_ast_D13: "C" = None, test_ast_D16: set["D"] = None, test_ast_D19: set["C"] = None, test_ast_D22: "D" = None, test_ast_D25: set["C"] = None, test_ast_D28: "A" = None, test_ast_D31: set["A"] = None):
        self.someBool = someBool
        self.someOtherBool = someOtherBool
        self.index = index
        self.name = name
        self.someQCollection = someQCollection
        self.someCollection = someCollection
        self.test_ast_D = test_ast_D
        self.test_ast_D13 = test_ast_D13
        self.test_ast_D16 = test_ast_D16 if test_ast_D16 is not None else set()
        self.test_ast_D19 = test_ast_D19 if test_ast_D19 is not None else set()
        self.test_ast_D22 = test_ast_D22
        self.test_ast_D25 = test_ast_D25 if test_ast_D25 is not None else set()
        self.test_ast_D28 = test_ast_D28
        self.test_ast_D31 = test_ast_D31 if test_ast_D31 is not None else set()
        
        pass
    @property
    def someQCollection(self):
        return self.__someQCollection

    @someQCollection.setter
    def someQCollection(self, someQCollection: str):
        self.__someQCollection = someQCollection


    @property
    def someCollection(self):
        return self.__someCollection

    @someCollection.setter
    def someCollection(self, someCollection: str):
        self.__someCollection = someCollection


    @property
    def someBool(self):
        return self.__someBool

    @someBool.setter
    def someBool(self, someBool: bool):
        self.__someBool = someBool


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index


    @property
    def someOtherBool(self):
        return self.__someOtherBool

    @someOtherBool.setter
    def someOtherBool(self, someOtherBool: str):
        self.__someOtherBool = someOtherBool


    @property
    def test_ast_D(self):
        return self.__test_ast_D

    @test_ast_D.setter
    def test_ast_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_ast_D__test_ast_D", None)
        self.__test_ast_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "D11"):
                opp_val = getattr(old_value, "D11", None)
                if opp_val == self:
                    setattr(old_value, "D11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "D11"):
                opp_val = getattr(value, "D11", None)
                setattr(value, "D11", self)

    @property
    def test_ast_D22(self):
        return self.__test_ast_D22

    @test_ast_D22.setter
    def test_ast_D22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_ast_D__test_ast_D22", None)
        self.__test_ast_D22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "D23"):
                opp_val = getattr(old_value, "D23", None)
                if opp_val == self:
                    setattr(old_value, "D23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "D23"):
                opp_val = getattr(value, "D23", None)
                setattr(value, "D23", self)

    @property
    def test_ast_D13(self):
        return self.__test_ast_D13

    @test_ast_D13.setter
    def test_ast_D13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_ast_D__test_ast_D13", None)
        self.__test_ast_D13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C14"):
                opp_val = getattr(old_value, "C14", None)
                if opp_val == self:
                    setattr(old_value, "C14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C14"):
                opp_val = getattr(value, "C14", None)
                setattr(value, "C14", self)

    @property
    def test_ast_D16(self):
        return self.__test_ast_D16

    @test_ast_D16.setter
    def test_ast_D16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_ast_D__test_ast_D16", None)
        self.__test_ast_D16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "D17"):
                    opp_val = getattr(item, "D17", None)
                    
                    if opp_val == self:
                        setattr(item, "D17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "D17"):
                    opp_val = getattr(item, "D17", None)
                    
                    setattr(item, "D17", self)
                    

    @property
    def test_ast_D28(self):
        return self.__test_ast_D28

    @test_ast_D28.setter
    def test_ast_D28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_ast_D__test_ast_D28", None)
        self.__test_ast_D28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "A29"):
                opp_val = getattr(old_value, "A29", None)
                if opp_val == self:
                    setattr(old_value, "A29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "A29"):
                opp_val = getattr(value, "A29", None)
                setattr(value, "A29", self)

    @property
    def test_ast_D25(self):
        return self.__test_ast_D25

    @test_ast_D25.setter
    def test_ast_D25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_ast_D__test_ast_D25", None)
        self.__test_ast_D25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "C26"):
                    opp_val = getattr(item, "C26", None)
                    
                    if opp_val == self:
                        setattr(item, "C26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "C26"):
                    opp_val = getattr(item, "C26", None)
                    
                    setattr(item, "C26", self)
                    

    @property
    def test_ast_D31(self):
        return self.__test_ast_D31

    @test_ast_D31.setter
    def test_ast_D31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_ast_D__test_ast_D31", None)
        self.__test_ast_D31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "A32"):
                    opp_val = getattr(item, "A32", None)
                    
                    if opp_val == self:
                        setattr(item, "A32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "A32"):
                    opp_val = getattr(item, "A32", None)
                    
                    setattr(item, "A32", self)
                    

    @property
    def test_ast_D19(self):
        return self.__test_ast_D19

    @test_ast_D19.setter
    def test_ast_D19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_ast_D__test_ast_D19", None)
        self.__test_ast_D19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "C20"):
                    opp_val = getattr(item, "C20", None)
                    
                    if opp_val == self:
                        setattr(item, "C20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "C20"):
                    opp_val = getattr(item, "C20", None)
                    
                    setattr(item, "C20", self)
                    

    def operationAttribute(self, test_param) :
        # TODO: Implement operationAttribute method
        pass

class test_ntas_C:

    def __init__(self, someTerminal: str):
        self.someTerminal = someTerminal
        
        pass
    @property
    def someTerminal(self):
        return self.__someTerminal

    @someTerminal.setter
    def someTerminal(self, someTerminal: str):
        self.__someTerminal = someTerminal


class test_ntas_B:

    pass
class test_ast_AbstractD(ABC):

    def __init__(self, derivedString: str, test_ast_AbstractD: "A" = None):
        self.derivedString = derivedString
        self.test_ast_AbstractD = test_ast_AbstractD
        
        pass
    @property
    def derivedString(self):
        return self.__derivedString

    @derivedString.setter
    def derivedString(self, derivedString: str):
        self.__derivedString = derivedString


    @property
    def test_ast_AbstractD(self):
        return self.__test_ast_AbstractD

    @test_ast_AbstractD.setter
    def test_ast_AbstractD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_ast_AbstractD__test_ast_AbstractD", None)
        self.__test_ast_AbstractD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "A34"):
                opp_val = getattr(old_value, "A34", None)
                if opp_val == self:
                    setattr(old_value, "A34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "A34"):
                opp_val = getattr(value, "A34", None)
                setattr(value, "A34", self)

class B:

    pass
class A:

    pass
class test_ntas_Root:

    pass
class test_ntas_A:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class D:

    pass
class test_ast_E(D):

    def __init__(self, derivedBool: bool, lazyBool: bool, D: "test_ntas_Root" = None, D23: "test_ast_D" = None, D17: "test_ast_D" = None, D11: "test_ast_D" = None):
        self.derivedBool = derivedBool
        self.lazyBool = lazyBool
        
        pass
    @property
    def derivedBool(self):
        return self.__derivedBool

    @derivedBool.setter
    def derivedBool(self, derivedBool: bool):
        self.__derivedBool = derivedBool


    @property
    def lazyBool(self):
        return self.__lazyBool

    @lazyBool.setter
    def lazyBool(self, lazyBool: bool):
        self.__lazyBool = lazyBool


class C:

    pass