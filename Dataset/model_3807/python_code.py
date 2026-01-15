from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class exercises_NamableElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamableElement:

    pass
class exercises_Transition(NamableElement):

    def __init__(self, input: str, exercises_Transition: "exercises_DFA" = None, exercises_Transition5: "exercises_State" = None, exercises_Transition8: "exercises_State" = None):
        self.input = input
        self.exercises_Transition = exercises_Transition
        self.exercises_Transition5 = exercises_Transition5
        self.exercises_Transition8 = exercises_Transition8
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def exercises_Transition5(self):
        return self.__exercises_Transition5

    @exercises_Transition5.setter
    def exercises_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exercises_Transition__exercises_Transition5", None)
        self.__exercises_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exercises_State4"):
                opp_val = getattr(old_value, "exercises_State4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exercises_State4"):
                opp_val = getattr(value, "exercises_State4", None)
                if opp_val is None:
                    setattr(value, "exercises_State4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def exercises_Transition8(self):
        return self.__exercises_Transition8

    @exercises_Transition8.setter
    def exercises_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exercises_Transition__exercises_Transition8", None)
        self.__exercises_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exercises_State7"):
                opp_val = getattr(old_value, "exercises_State7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exercises_State7"):
                opp_val = getattr(value, "exercises_State7", None)
                if opp_val is None:
                    setattr(value, "exercises_State7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def exercises_Transition(self):
        return self.__exercises_Transition

    @exercises_Transition.setter
    def exercises_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exercises_Transition__exercises_Transition", None)
        self.__exercises_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exercises_DFA2"):
                opp_val = getattr(old_value, "exercises_DFA2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exercises_DFA2"):
                opp_val = getattr(value, "exercises_DFA2", None)
                if opp_val is None:
                    setattr(value, "exercises_DFA2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class exercises_State(NamableElement):

    def __init__(self, id: str, isStart: bool, isEnd: bool, exercises_State: "exercises_DFA" = None, exercises_State4: set["exercises_Transition"] = None, exercises_State7: set["exercises_Transition"] = None):
        self.id = id
        self.isStart = isStart
        self.isEnd = isEnd
        self.exercises_State = exercises_State
        self.exercises_State4 = exercises_State4 if exercises_State4 is not None else set()
        self.exercises_State7 = exercises_State7 if exercises_State7 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def isStart(self) -> bool:
        return self.__isStart

    @isStart.setter
    def isStart(self, isStart: bool):
        self.__isStart = isStart

    @property
    def isEnd(self) -> bool:
        return self.__isEnd

    @isEnd.setter
    def isEnd(self, isEnd: bool):
        self.__isEnd = isEnd

    @property
    def exercises_State(self):
        return self.__exercises_State

    @exercises_State.setter
    def exercises_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exercises_State__exercises_State", None)
        self.__exercises_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exercises_DFA"):
                opp_val = getattr(old_value, "exercises_DFA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exercises_DFA"):
                opp_val = getattr(value, "exercises_DFA", None)
                if opp_val is None:
                    setattr(value, "exercises_DFA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def exercises_State7(self):
        return self.__exercises_State7

    @exercises_State7.setter
    def exercises_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exercises_State__exercises_State7", None)
        self.__exercises_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "exercises_Transition8"):
                    opp_val = getattr(item, "exercises_Transition8", None)
                    
                    if opp_val == self:
                        setattr(item, "exercises_Transition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "exercises_Transition8"):
                    opp_val = getattr(item, "exercises_Transition8", None)
                    
                    setattr(item, "exercises_Transition8", self)
                    

    @property
    def exercises_State4(self):
        return self.__exercises_State4

    @exercises_State4.setter
    def exercises_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exercises_State__exercises_State4", None)
        self.__exercises_State4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "exercises_Transition5"):
                    opp_val = getattr(item, "exercises_Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "exercises_Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "exercises_Transition5"):
                    opp_val = getattr(item, "exercises_Transition5", None)
                    
                    setattr(item, "exercises_Transition5", self)
                    

class exercises_DFA(NamableElement):

    pass