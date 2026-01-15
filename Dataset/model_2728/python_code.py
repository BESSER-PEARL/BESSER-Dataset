from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class B:

    pass
class test100_A(B):

    def __init__(self, name: str, test100_A2: set["test100_B"] = None, test100_A4: set["test100_DsmlRelation"] = None, test100_A: "test100_C" = None, test100_A7: "test100_DsmlRelation" = None, test100_A10: "test100_DsmlRelation" = None):
        self.name = name
        self.test100_A2 = test100_A2 if test100_A2 is not None else set()
        self.test100_A4 = test100_A4 if test100_A4 is not None else set()
        self.test100_A = test100_A
        self.test100_A7 = test100_A7
        self.test100_A10 = test100_A10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test100_A10(self):
        return self.__test100_A10

    @test100_A10.setter
    def test100_A10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test100_A__test100_A10", None)
        self.__test100_A10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test100_DsmlRelation9"):
                opp_val = getattr(old_value, "test100_DsmlRelation9", None)
                if opp_val == self:
                    setattr(old_value, "test100_DsmlRelation9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test100_DsmlRelation9"):
                opp_val = getattr(value, "test100_DsmlRelation9", None)
                setattr(value, "test100_DsmlRelation9", self)

    @property
    def test100_A(self):
        return self.__test100_A

    @test100_A.setter
    def test100_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test100_A__test100_A", None)
        self.__test100_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test100_C"):
                opp_val = getattr(old_value, "test100_C", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test100_C"):
                opp_val = getattr(value, "test100_C", None)
                if opp_val is None:
                    setattr(value, "test100_C", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test100_A2(self):
        return self.__test100_A2

    @test100_A2.setter
    def test100_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test100_A__test100_A2", None)
        self.__test100_A2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test100_B"):
                    opp_val = getattr(item, "test100_B", None)
                    
                    if opp_val == self:
                        setattr(item, "test100_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test100_B"):
                    opp_val = getattr(item, "test100_B", None)
                    
                    setattr(item, "test100_B", self)
                    

    @property
    def test100_A4(self):
        return self.__test100_A4

    @test100_A4.setter
    def test100_A4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test100_A__test100_A4", None)
        self.__test100_A4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test100_DsmlRelation"):
                    opp_val = getattr(item, "test100_DsmlRelation", None)
                    
                    if opp_val == self:
                        setattr(item, "test100_DsmlRelation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test100_DsmlRelation"):
                    opp_val = getattr(item, "test100_DsmlRelation", None)
                    
                    setattr(item, "test100_DsmlRelation", self)
                    

    @property
    def test100_A7(self):
        return self.__test100_A7

    @test100_A7.setter
    def test100_A7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test100_A__test100_A7", None)
        self.__test100_A7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test100_DsmlRelation6"):
                opp_val = getattr(old_value, "test100_DsmlRelation6", None)
                if opp_val == self:
                    setattr(old_value, "test100_DsmlRelation6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test100_DsmlRelation6"):
                opp_val = getattr(value, "test100_DsmlRelation6", None)
                setattr(value, "test100_DsmlRelation6", self)

class test100_C:

    pass
class test100_DsmlRelation:

    def __init__(self, name: str, mandatory: bool, details: str, test100_DsmlRelation: "test100_A" = None, test100_DsmlRelation6: "test100_A" = None, test100_DsmlRelation9: "test100_A" = None):
        self.name = name
        self.mandatory = mandatory
        self.details = details
        self.test100_DsmlRelation = test100_DsmlRelation
        self.test100_DsmlRelation6 = test100_DsmlRelation6
        self.test100_DsmlRelation9 = test100_DsmlRelation9
        
    @property
    def details(self) -> str:
        return self.__details

    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test100_DsmlRelation(self):
        return self.__test100_DsmlRelation

    @test100_DsmlRelation.setter
    def test100_DsmlRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test100_DsmlRelation__test100_DsmlRelation", None)
        self.__test100_DsmlRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test100_A4"):
                opp_val = getattr(old_value, "test100_A4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test100_A4"):
                opp_val = getattr(value, "test100_A4", None)
                if opp_val is None:
                    setattr(value, "test100_A4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test100_DsmlRelation6(self):
        return self.__test100_DsmlRelation6

    @test100_DsmlRelation6.setter
    def test100_DsmlRelation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test100_DsmlRelation__test100_DsmlRelation6", None)
        self.__test100_DsmlRelation6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test100_A7"):
                opp_val = getattr(old_value, "test100_A7", None)
                if opp_val == self:
                    setattr(old_value, "test100_A7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test100_A7"):
                opp_val = getattr(value, "test100_A7", None)
                setattr(value, "test100_A7", self)

    @property
    def test100_DsmlRelation9(self):
        return self.__test100_DsmlRelation9

    @test100_DsmlRelation9.setter
    def test100_DsmlRelation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test100_DsmlRelation__test100_DsmlRelation9", None)
        self.__test100_DsmlRelation9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test100_A10"):
                opp_val = getattr(old_value, "test100_A10", None)
                if opp_val == self:
                    setattr(old_value, "test100_A10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test100_A10"):
                opp_val = getattr(value, "test100_A10", None)
                setattr(value, "test100_A10", self)

class test100_B:

    def __init__(self, id: str, test100_B: "test100_A" = None):
        self.id = id
        self.test100_B = test100_B
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def test100_B(self):
        return self.__test100_B

    @test100_B.setter
    def test100_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test100_B__test100_B", None)
        self.__test100_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test100_A2"):
                opp_val = getattr(old_value, "test100_A2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test100_A2"):
                opp_val = getattr(value, "test100_A2", None)
                if opp_val is None:
                    setattr(value, "test100_A2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
