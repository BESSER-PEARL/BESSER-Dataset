from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SomeTestClass:

    pass
class test_SomeTestClassWithID(SomeTestClass):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class test_SomeTestClass:

    def __init__(self, attribute: str, test_SomeTestClass9: "test_PatchTestModel" = None, test_SomeTestClass: "test_PatchTestModel" = None, test_SomeTestClass3: "test_PatchTestModel" = None, test_SomeTestClass6: "test_PatchTestModel" = None):
        self.attribute = attribute
        self.test_SomeTestClass9 = test_SomeTestClass9
        self.test_SomeTestClass = test_SomeTestClass
        self.test_SomeTestClass3 = test_SomeTestClass3
        self.test_SomeTestClass6 = test_SomeTestClass6
        
    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def test_SomeTestClass(self):
        return self.__test_SomeTestClass

    @test_SomeTestClass.setter
    def test_SomeTestClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_SomeTestClass__test_SomeTestClass", None)
        self.__test_SomeTestClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_PatchTestModel"):
                opp_val = getattr(old_value, "test_PatchTestModel", None)
                if opp_val == self:
                    setattr(old_value, "test_PatchTestModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_PatchTestModel"):
                opp_val = getattr(value, "test_PatchTestModel", None)
                setattr(value, "test_PatchTestModel", self)

    @property
    def test_SomeTestClass9(self):
        return self.__test_SomeTestClass9

    @test_SomeTestClass9.setter
    def test_SomeTestClass9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_SomeTestClass__test_SomeTestClass9", None)
        self.__test_SomeTestClass9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_PatchTestModel8"):
                opp_val = getattr(old_value, "test_PatchTestModel8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_PatchTestModel8"):
                opp_val = getattr(value, "test_PatchTestModel8", None)
                if opp_val is None:
                    setattr(value, "test_PatchTestModel8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_SomeTestClass6(self):
        return self.__test_SomeTestClass6

    @test_SomeTestClass6.setter
    def test_SomeTestClass6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_SomeTestClass__test_SomeTestClass6", None)
        self.__test_SomeTestClass6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_PatchTestModel5"):
                opp_val = getattr(old_value, "test_PatchTestModel5", None)
                if opp_val == self:
                    setattr(old_value, "test_PatchTestModel5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_PatchTestModel5"):
                opp_val = getattr(value, "test_PatchTestModel5", None)
                setattr(value, "test_PatchTestModel5", self)

    @property
    def test_SomeTestClass3(self):
        return self.__test_SomeTestClass3

    @test_SomeTestClass3.setter
    def test_SomeTestClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_SomeTestClass__test_SomeTestClass3", None)
        self.__test_SomeTestClass3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_PatchTestModel2"):
                opp_val = getattr(old_value, "test_PatchTestModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_PatchTestModel2"):
                opp_val = getattr(value, "test_PatchTestModel2", None)
                if opp_val is None:
                    setattr(value, "test_PatchTestModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test_PatchTestModel:

    def __init__(self, id: str, oneAttribute: str, multiAttribute: str, test_PatchTestModel: "test_SomeTestClass" = None, test_PatchTestModel2: set["test_SomeTestClass"] = None, test_PatchTestModel5: "test_SomeTestClass" = None, test_PatchTestModel8: set["test_SomeTestClass"] = None):
        self.id = id
        self.oneAttribute = oneAttribute
        self.multiAttribute = multiAttribute
        self.test_PatchTestModel = test_PatchTestModel
        self.test_PatchTestModel2 = test_PatchTestModel2 if test_PatchTestModel2 is not None else set()
        self.test_PatchTestModel5 = test_PatchTestModel5
        self.test_PatchTestModel8 = test_PatchTestModel8 if test_PatchTestModel8 is not None else set()
        
    @property
    def multiAttribute(self) -> str:
        return self.__multiAttribute

    @multiAttribute.setter
    def multiAttribute(self, multiAttribute: str):
        self.__multiAttribute = multiAttribute

    @property
    def oneAttribute(self) -> str:
        return self.__oneAttribute

    @oneAttribute.setter
    def oneAttribute(self, oneAttribute: str):
        self.__oneAttribute = oneAttribute

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def test_PatchTestModel8(self):
        return self.__test_PatchTestModel8

    @test_PatchTestModel8.setter
    def test_PatchTestModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_PatchTestModel__test_PatchTestModel8", None)
        self.__test_PatchTestModel8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_SomeTestClass9"):
                    opp_val = getattr(item, "test_SomeTestClass9", None)
                    
                    if opp_val == self:
                        setattr(item, "test_SomeTestClass9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_SomeTestClass9"):
                    opp_val = getattr(item, "test_SomeTestClass9", None)
                    
                    setattr(item, "test_SomeTestClass9", self)
                    

    @property
    def test_PatchTestModel2(self):
        return self.__test_PatchTestModel2

    @test_PatchTestModel2.setter
    def test_PatchTestModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_PatchTestModel__test_PatchTestModel2", None)
        self.__test_PatchTestModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_SomeTestClass3"):
                    opp_val = getattr(item, "test_SomeTestClass3", None)
                    
                    if opp_val == self:
                        setattr(item, "test_SomeTestClass3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_SomeTestClass3"):
                    opp_val = getattr(item, "test_SomeTestClass3", None)
                    
                    setattr(item, "test_SomeTestClass3", self)
                    

    @property
    def test_PatchTestModel(self):
        return self.__test_PatchTestModel

    @test_PatchTestModel.setter
    def test_PatchTestModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_PatchTestModel__test_PatchTestModel", None)
        self.__test_PatchTestModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_SomeTestClass"):
                opp_val = getattr(old_value, "test_SomeTestClass", None)
                if opp_val == self:
                    setattr(old_value, "test_SomeTestClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_SomeTestClass"):
                opp_val = getattr(value, "test_SomeTestClass", None)
                setattr(value, "test_SomeTestClass", self)

    @property
    def test_PatchTestModel5(self):
        return self.__test_PatchTestModel5

    @test_PatchTestModel5.setter
    def test_PatchTestModel5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_PatchTestModel__test_PatchTestModel5", None)
        self.__test_PatchTestModel5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_SomeTestClass6"):
                opp_val = getattr(old_value, "test_SomeTestClass6", None)
                if opp_val == self:
                    setattr(old_value, "test_SomeTestClass6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_SomeTestClass6"):
                opp_val = getattr(value, "test_SomeTestClass6", None)
                setattr(value, "test_SomeTestClass6", self)
