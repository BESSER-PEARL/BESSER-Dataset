from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Kind(Enum):
    Nice = "Nice"
    NotNice = "NotNice"


############################################
# Definition of Classes
############################################

class test_NamedElement(ABC):

    pass
class NamedElement:

    pass
class test_Transition(NamedElement):

    def __init__(self, test_Transition4: "test_State" = None, test_Transition: "test_StateMachine" = None, test_Transition7: "test_State" = None):
        self.test_Transition4 = test_Transition4
        self.test_Transition = test_Transition
        self.test_Transition7 = test_Transition7
        
    @property
    def test_Transition7(self):
        return self.__test_Transition7

    @test_Transition7.setter
    def test_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Transition__test_Transition7", None)
        self.__test_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_State8"):
                opp_val = getattr(old_value, "test_State8", None)
                if opp_val == self:
                    setattr(old_value, "test_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_State8"):
                opp_val = getattr(value, "test_State8", None)
                setattr(value, "test_State8", self)

    @property
    def test_Transition(self):
        return self.__test_Transition

    @test_Transition.setter
    def test_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Transition__test_Transition", None)
        self.__test_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_StateMachine"):
                opp_val = getattr(old_value, "test_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_StateMachine"):
                opp_val = getattr(value, "test_StateMachine", None)
                if opp_val is None:
                    setattr(value, "test_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_Transition4(self):
        return self.__test_Transition4

    @test_Transition4.setter
    def test_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Transition__test_Transition4", None)
        self.__test_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_State5"):
                opp_val = getattr(old_value, "test_State5", None)
                if opp_val == self:
                    setattr(old_value, "test_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_State5"):
                opp_val = getattr(value, "test_State5", None)
                setattr(value, "test_State5", self)

    def fire(self) -> bool:
        # TODO: Implement fire method
        pass

class test_State(NamedElement):

    def __init__(self, kind: str, test_State5: "test_Transition" = None, test_State: "test_StateMachine" = None, test_State8: "test_Transition" = None):
        self.kind = kind
        self.test_State5 = test_State5
        self.test_State = test_State
        self.test_State8 = test_State8
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def test_State(self):
        return self.__test_State

    @test_State.setter
    def test_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_State__test_State", None)
        self.__test_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_StateMachine2"):
                opp_val = getattr(old_value, "test_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_StateMachine2"):
                opp_val = getattr(value, "test_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "test_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_State5(self):
        return self.__test_State5

    @test_State5.setter
    def test_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_State__test_State5", None)
        self.__test_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Transition4"):
                opp_val = getattr(old_value, "test_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "test_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Transition4"):
                opp_val = getattr(value, "test_Transition4", None)
                setattr(value, "test_Transition4", self)

    @property
    def test_State8(self):
        return self.__test_State8

    @test_State8.setter
    def test_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_State__test_State8", None)
        self.__test_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Transition7"):
                opp_val = getattr(old_value, "test_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "test_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Transition7"):
                opp_val = getattr(value, "test_Transition7", None)
                setattr(value, "test_Transition7", self)

class test_StateMachine(NamedElement):

    def __init__(self, name: str, test_StateMachine: set["test_Transition"] = None, test_StateMachine2: set["test_State"] = None):
        self.name = name
        self.test_StateMachine = test_StateMachine if test_StateMachine is not None else set()
        self.test_StateMachine2 = test_StateMachine2 if test_StateMachine2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def test_StateMachine2(self):
        return self.__test_StateMachine2

    @test_StateMachine2.setter
    def test_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_StateMachine__test_StateMachine2", None)
        self.__test_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_State"):
                    opp_val = getattr(item, "test_State", None)
                    
                    if opp_val == self:
                        setattr(item, "test_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_State"):
                    opp_val = getattr(item, "test_State", None)
                    
                    setattr(item, "test_State", self)
                    

    @property
    def test_StateMachine(self):
        return self.__test_StateMachine

    @test_StateMachine.setter
    def test_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_StateMachine__test_StateMachine", None)
        self.__test_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_Transition"):
                    opp_val = getattr(item, "test_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "test_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_Transition"):
                    opp_val = getattr(item, "test_Transition", None)
                    
                    setattr(item, "test_Transition", self)
                    
