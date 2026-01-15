from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    HOLD = "HOLD"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


############################################
# Definition of Classes
############################################

class turingmodel_Transition:

    def __init__(self, condition: str, write: str, dir: str, Transition: "turingmodel_State" = None, turingmodel_Transition15: "turingmodel_State" = None, turingmodel_Transition: "turingmodel_TuringMachine" = None, next: "turingmodel_State" = None, turingmodel_Transition18: "turingmodel_State" = None):
        self.condition = condition
        self.write = write
        self.dir = dir
        self.Transition = Transition
        self.turingmodel_Transition15 = turingmodel_Transition15
        self.turingmodel_Transition = turingmodel_Transition
        self.next = next
        self.turingmodel_Transition18 = turingmodel_Transition18
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def write(self) -> str:
        return self.__write

    @write.setter
    def write(self, write: str):
        self.__write = write

    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def turingmodel_Transition(self):
        return self.__turingmodel_Transition

    @turingmodel_Transition.setter
    def turingmodel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_Transition__turingmodel_Transition", None)
        self.__turingmodel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turingmodel_TuringMachine2"):
                opp_val = getattr(old_value, "turingmodel_TuringMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turingmodel_TuringMachine2"):
                opp_val = getattr(value, "turingmodel_TuringMachine2", None)
                if opp_val is None:
                    setattr(value, "turingmodel_TuringMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def turingmodel_Transition15(self):
        return self.__turingmodel_Transition15

    @turingmodel_Transition15.setter
    def turingmodel_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_Transition__turingmodel_Transition15", None)
        self.__turingmodel_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turingmodel_State14"):
                opp_val = getattr(old_value, "turingmodel_State14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turingmodel_State14"):
                opp_val = getattr(value, "turingmodel_State14", None)
                if opp_val is None:
                    setattr(value, "turingmodel_State14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_Transition__next", None)
        self.__next = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def turingmodel_Transition18(self):
        return self.__turingmodel_Transition18

    @turingmodel_Transition18.setter
    def turingmodel_Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_Transition__turingmodel_Transition18", None)
        self.__turingmodel_Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turingmodel_State19"):
                opp_val = getattr(old_value, "turingmodel_State19", None)
                if opp_val == self:
                    setattr(old_value, "turingmodel_State19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turingmodel_State19"):
                opp_val = getattr(value, "turingmodel_State19", None)
                setattr(value, "turingmodel_State19", self)

class turingmodel_State:

    def __init__(self, name: str, isEndState: bool, turingmodel_State5: "turingmodel_TuringMachine" = None, source: set["turingmodel_Transition"] = None, turingmodel_State9: "turingmodel_State" = None, turingmodel_State7: set["turingmodel_State"] = None, turingmodel_State12: "turingmodel_State" = None, turingmodel_State10: "turingmodel_State" = None, turingmodel_State14: set["turingmodel_Transition"] = None, turingmodel_State: "turingmodel_TuringMachine" = None, State: "turingmodel_Transition" = None, turingmodel_State19: "turingmodel_Transition" = None):
        self.name = name
        self.isEndState = isEndState
        self.turingmodel_State5 = turingmodel_State5
        self.source = source if source is not None else set()
        self.turingmodel_State9 = turingmodel_State9
        self.turingmodel_State7 = turingmodel_State7 if turingmodel_State7 is not None else set()
        self.turingmodel_State12 = turingmodel_State12
        self.turingmodel_State10 = turingmodel_State10
        self.turingmodel_State14 = turingmodel_State14 if turingmodel_State14 is not None else set()
        self.turingmodel_State = turingmodel_State
        self.State = State
        self.turingmodel_State19 = turingmodel_State19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isEndState(self) -> bool:
        return self.__isEndState

    @isEndState.setter
    def isEndState(self, isEndState: bool):
        self.__isEndState = isEndState

    @property
    def turingmodel_State(self):
        return self.__turingmodel_State

    @turingmodel_State.setter
    def turingmodel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_State__turingmodel_State", None)
        self.__turingmodel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turingmodel_TuringMachine"):
                opp_val = getattr(old_value, "turingmodel_TuringMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turingmodel_TuringMachine"):
                opp_val = getattr(value, "turingmodel_TuringMachine", None)
                if opp_val is None:
                    setattr(value, "turingmodel_TuringMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def turingmodel_State19(self):
        return self.__turingmodel_State19

    @turingmodel_State19.setter
    def turingmodel_State19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_State__turingmodel_State19", None)
        self.__turingmodel_State19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turingmodel_Transition18"):
                opp_val = getattr(old_value, "turingmodel_Transition18", None)
                if opp_val == self:
                    setattr(old_value, "turingmodel_Transition18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turingmodel_Transition18"):
                opp_val = getattr(value, "turingmodel_Transition18", None)
                setattr(value, "turingmodel_Transition18", self)

    @property
    def turingmodel_State14(self):
        return self.__turingmodel_State14

    @turingmodel_State14.setter
    def turingmodel_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_State__turingmodel_State14", None)
        self.__turingmodel_State14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "turingmodel_Transition15"):
                    opp_val = getattr(item, "turingmodel_Transition15", None)
                    
                    if opp_val == self:
                        setattr(item, "turingmodel_Transition15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "turingmodel_Transition15"):
                    opp_val = getattr(item, "turingmodel_Transition15", None)
                    
                    setattr(item, "turingmodel_Transition15", self)
                    

    @property
    def turingmodel_State7(self):
        return self.__turingmodel_State7

    @turingmodel_State7.setter
    def turingmodel_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_State__turingmodel_State7", None)
        self.__turingmodel_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "turingmodel_State9"):
                    opp_val = getattr(item, "turingmodel_State9", None)
                    
                    if opp_val == self:
                        setattr(item, "turingmodel_State9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "turingmodel_State9"):
                    opp_val = getattr(item, "turingmodel_State9", None)
                    
                    setattr(item, "turingmodel_State9", self)
                    

    @property
    def turingmodel_State5(self):
        return self.__turingmodel_State5

    @turingmodel_State5.setter
    def turingmodel_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_State__turingmodel_State5", None)
        self.__turingmodel_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turingmodel_TuringMachine4"):
                opp_val = getattr(old_value, "turingmodel_TuringMachine4", None)
                if opp_val == self:
                    setattr(old_value, "turingmodel_TuringMachine4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turingmodel_TuringMachine4"):
                opp_val = getattr(value, "turingmodel_TuringMachine4", None)
                setattr(value, "turingmodel_TuringMachine4", self)

    @property
    def turingmodel_State12(self):
        return self.__turingmodel_State12

    @turingmodel_State12.setter
    def turingmodel_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_State__turingmodel_State12", None)
        self.__turingmodel_State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turingmodel_State10"):
                opp_val = getattr(old_value, "turingmodel_State10", None)
                if opp_val == self:
                    setattr(old_value, "turingmodel_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turingmodel_State10"):
                opp_val = getattr(value, "turingmodel_State10", None)
                setattr(value, "turingmodel_State10", self)

    @property
    def turingmodel_State9(self):
        return self.__turingmodel_State9

    @turingmodel_State9.setter
    def turingmodel_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_State__turingmodel_State9", None)
        self.__turingmodel_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turingmodel_State7"):
                opp_val = getattr(old_value, "turingmodel_State7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turingmodel_State7"):
                opp_val = getattr(value, "turingmodel_State7", None)
                if opp_val is None:
                    setattr(value, "turingmodel_State7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "next"):
                opp_val = getattr(old_value, "next", None)
                if opp_val == self:
                    setattr(old_value, "next", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "next"):
                opp_val = getattr(value, "next", None)
                setattr(value, "next", self)

    @property
    def turingmodel_State10(self):
        return self.__turingmodel_State10

    @turingmodel_State10.setter
    def turingmodel_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turingmodel_State__turingmodel_State10", None)
        self.__turingmodel_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turingmodel_State12"):
                opp_val = getattr(old_value, "turingmodel_State12", None)
                if opp_val == self:
                    setattr(old_value, "turingmodel_State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turingmodel_State12"):
                opp_val = getattr(value, "turingmodel_State12", None)
                setattr(value, "turingmodel_State12", self)

class turingmodel_TuringMachine:

    pass