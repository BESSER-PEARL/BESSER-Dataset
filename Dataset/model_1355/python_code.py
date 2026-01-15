from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class statemachine_Simple(State):

    pass
class statemachine_Composite(State):

    pass
class statemachine_Initial(State):

    pass
class statemachine_Resource:

    def __init__(self, name: str, statemachine_Resource: "statemachine_StateMachine" = None, statemachine_Resource13: "statemachine_State" = None):
        self.name = name
        self.statemachine_Resource = statemachine_Resource
        self.statemachine_Resource13 = statemachine_Resource13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_Resource(self):
        return self.__statemachine_Resource

    @statemachine_Resource.setter
    def statemachine_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Resource__statemachine_Resource", None)
        self.__statemachine_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateMachine4"):
                opp_val = getattr(old_value, "statemachine_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachine4"):
                opp_val = getattr(value, "statemachine_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Resource13(self):
        return self.__statemachine_Resource13

    @statemachine_Resource13.setter
    def statemachine_Resource13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Resource__statemachine_Resource13", None)
        self.__statemachine_Resource13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State12"):
                opp_val = getattr(old_value, "statemachine_State12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State12"):
                opp_val = getattr(value, "statemachine_State12", None)
                if opp_val is None:
                    setattr(value, "statemachine_State12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_State(ABC):

    def __init__(self, name: str, statemachine_State7: "statemachine_Transition" = None, statemachine_State10: "statemachine_Transition" = None, statemachine_State: "statemachine_StateMachine" = None, statemachine_State12: set["statemachine_Resource"] = None, statemachine_State15: "statemachine_Composite" = None):
        self.name = name
        self.statemachine_State7 = statemachine_State7
        self.statemachine_State10 = statemachine_State10
        self.statemachine_State = statemachine_State
        self.statemachine_State12 = statemachine_State12 if statemachine_State12 is not None else set()
        self.statemachine_State15 = statemachine_State15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_State12(self):
        return self.__statemachine_State12

    @statemachine_State12.setter
    def statemachine_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State12", None)
        self.__statemachine_State12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Resource13"):
                    opp_val = getattr(item, "statemachine_Resource13", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Resource13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Resource13"):
                    opp_val = getattr(item, "statemachine_Resource13", None)
                    
                    setattr(item, "statemachine_Resource13", self)
                    

    @property
    def statemachine_State10(self):
        return self.__statemachine_State10

    @statemachine_State10.setter
    def statemachine_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State10", None)
        self.__statemachine_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition9"):
                opp_val = getattr(old_value, "statemachine_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition9"):
                opp_val = getattr(value, "statemachine_Transition9", None)
                setattr(value, "statemachine_Transition9", self)

    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateMachine2"):
                opp_val = getattr(old_value, "statemachine_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachine2"):
                opp_val = getattr(value, "statemachine_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State15(self):
        return self.__statemachine_State15

    @statemachine_State15.setter
    def statemachine_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State15", None)
        self.__statemachine_State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Composite"):
                opp_val = getattr(old_value, "statemachine_Composite", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Composite"):
                opp_val = getattr(value, "statemachine_Composite", None)
                if opp_val is None:
                    setattr(value, "statemachine_Composite", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State7(self):
        return self.__statemachine_State7

    @statemachine_State7.setter
    def statemachine_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State7", None)
        self.__statemachine_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition6"):
                opp_val = getattr(old_value, "statemachine_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition6"):
                opp_val = getattr(value, "statemachine_Transition6", None)
                setattr(value, "statemachine_Transition6", self)

class statemachine_Transition:

    def __init__(self, duration: int, Id: int, statemachine_Transition: "statemachine_StateMachine" = None, statemachine_Transition6: "statemachine_State" = None, statemachine_Transition9: "statemachine_State" = None):
        self.duration = duration
        self.Id = Id
        self.statemachine_Transition = statemachine_Transition
        self.statemachine_Transition6 = statemachine_Transition6
        self.statemachine_Transition9 = statemachine_Transition9
        
    @property
    def Id(self) -> int:
        return self.__Id

    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def statemachine_Transition6(self):
        return self.__statemachine_Transition6

    @statemachine_Transition6.setter
    def statemachine_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition6", None)
        self.__statemachine_Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State7"):
                opp_val = getattr(old_value, "statemachine_State7", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State7"):
                opp_val = getattr(value, "statemachine_State7", None)
                setattr(value, "statemachine_State7", self)

    @property
    def statemachine_Transition9(self):
        return self.__statemachine_Transition9

    @statemachine_Transition9.setter
    def statemachine_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition9", None)
        self.__statemachine_Transition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State10"):
                opp_val = getattr(old_value, "statemachine_State10", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State10"):
                opp_val = getattr(value, "statemachine_State10", None)
                setattr(value, "statemachine_State10", self)

    @property
    def statemachine_Transition(self):
        return self.__statemachine_Transition

    @statemachine_Transition.setter
    def statemachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition", None)
        self.__statemachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateMachine"):
                opp_val = getattr(old_value, "statemachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachine"):
                opp_val = getattr(value, "statemachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_StateMachine:

    def __init__(self, name: str, statemachine_StateMachine: set["statemachine_Transition"] = None, statemachine_StateMachine2: set["statemachine_State"] = None, statemachine_StateMachine4: set["statemachine_Resource"] = None):
        self.name = name
        self.statemachine_StateMachine = statemachine_StateMachine if statemachine_StateMachine is not None else set()
        self.statemachine_StateMachine2 = statemachine_StateMachine2 if statemachine_StateMachine2 is not None else set()
        self.statemachine_StateMachine4 = statemachine_StateMachine4 if statemachine_StateMachine4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_StateMachine4(self):
        return self.__statemachine_StateMachine4

    @statemachine_StateMachine4.setter
    def statemachine_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachine__statemachine_StateMachine4", None)
        self.__statemachine_StateMachine4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Resource"):
                    opp_val = getattr(item, "statemachine_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Resource"):
                    opp_val = getattr(item, "statemachine_Resource", None)
                    
                    setattr(item, "statemachine_Resource", self)
                    

    @property
    def statemachine_StateMachine2(self):
        return self.__statemachine_StateMachine2

    @statemachine_StateMachine2.setter
    def statemachine_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachine__statemachine_StateMachine2", None)
        self.__statemachine_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_State"):
                    opp_val = getattr(item, "statemachine_State", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_State"):
                    opp_val = getattr(item, "statemachine_State", None)
                    
                    setattr(item, "statemachine_State", self)
                    

    @property
    def statemachine_StateMachine(self):
        return self.__statemachine_StateMachine

    @statemachine_StateMachine.setter
    def statemachine_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachine__statemachine_StateMachine", None)
        self.__statemachine_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    setattr(item, "statemachine_Transition", self)
                    
