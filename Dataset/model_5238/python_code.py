from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class introduction_con:

    pass
class A:

    pass
class introduction_B(A):

    pass
class introduction_Y:

    def __init__(self, id: str, test: int, introduction_Y: "introduction_A" = None, introduction_Y7: "introduction_con" = None):
        self.id = id
        self.test = test
        self.introduction_Y = introduction_Y
        self.introduction_Y7 = introduction_Y7
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def test(self) -> int:
        return self.__test

    @test.setter
    def test(self, test: int):
        self.__test = test

    @property
    def introduction_Y(self):
        return self.__introduction_Y

    @introduction_Y.setter
    def introduction_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_introduction_Y__introduction_Y", None)
        self.__introduction_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "introduction_A2"):
                opp_val = getattr(old_value, "introduction_A2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "introduction_A2"):
                opp_val = getattr(value, "introduction_A2", None)
                if opp_val is None:
                    setattr(value, "introduction_A2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def introduction_Y7(self):
        return self.__introduction_Y7

    @introduction_Y7.setter
    def introduction_Y7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_introduction_Y__introduction_Y7", None)
        self.__introduction_Y7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "introduction_con6"):
                opp_val = getattr(old_value, "introduction_con6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "introduction_con6"):
                opp_val = getattr(value, "introduction_con6", None)
                if opp_val is None:
                    setattr(value, "introduction_con6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class introduction_X:

    def __init__(self, id: str, introduction_X: "introduction_A" = None):
        self.id = id
        self.introduction_X = introduction_X
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def introduction_X(self):
        return self.__introduction_X

    @introduction_X.setter
    def introduction_X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_introduction_X__introduction_X", None)
        self.__introduction_X = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "introduction_A"):
                opp_val = getattr(old_value, "introduction_A", None)
                if opp_val == self:
                    setattr(old_value, "introduction_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "introduction_A"):
                opp_val = getattr(value, "introduction_A", None)
                setattr(value, "introduction_A", self)

class introduction_A:

    def __init__(self, id: str, introduction_A: "introduction_X" = None, introduction_A2: set["introduction_Y"] = None, introduction_A4: "introduction_con" = None):
        self.id = id
        self.introduction_A = introduction_A
        self.introduction_A2 = introduction_A2 if introduction_A2 is not None else set()
        self.introduction_A4 = introduction_A4
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def introduction_A(self):
        return self.__introduction_A

    @introduction_A.setter
    def introduction_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_introduction_A__introduction_A", None)
        self.__introduction_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "introduction_X"):
                opp_val = getattr(old_value, "introduction_X", None)
                if opp_val == self:
                    setattr(old_value, "introduction_X", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "introduction_X"):
                opp_val = getattr(value, "introduction_X", None)
                setattr(value, "introduction_X", self)

    @property
    def introduction_A4(self):
        return self.__introduction_A4

    @introduction_A4.setter
    def introduction_A4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_introduction_A__introduction_A4", None)
        self.__introduction_A4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "introduction_con"):
                opp_val = getattr(old_value, "introduction_con", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "introduction_con"):
                opp_val = getattr(value, "introduction_con", None)
                if opp_val is None:
                    setattr(value, "introduction_con", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def introduction_A2(self):
        return self.__introduction_A2

    @introduction_A2.setter
    def introduction_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_introduction_A__introduction_A2", None)
        self.__introduction_A2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "introduction_Y"):
                    opp_val = getattr(item, "introduction_Y", None)
                    
                    if opp_val == self:
                        setattr(item, "introduction_Y", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "introduction_Y"):
                    opp_val = getattr(item, "introduction_Y", None)
                    
                    setattr(item, "introduction_Y", self)
                    
