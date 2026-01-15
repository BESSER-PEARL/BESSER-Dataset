from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class statemachine_Composite(State):

    pass
class statemachine_Initial(State):

    pass
class statemachine_Final(State):

    pass
class statemachine_Simple(State):

    pass
class statemachine_Need:

    pass
class statemachine_Transition:

    def __init__(self, Id: int, statemachine_Transition: "statemachine_State" = None, statemachine_Transition8: "statemachine_State" = None):
        self.Id = Id
        self.statemachine_Transition = statemachine_Transition
        self.statemachine_Transition8 = statemachine_Transition8
        
    @property
    def Id(self) -> int:
        return self.__Id

    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def statemachine_Transition8(self):
        return self.__statemachine_Transition8

    @statemachine_Transition8.setter
    def statemachine_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition8", None)
        self.__statemachine_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State9"):
                opp_val = getattr(old_value, "statemachine_State9", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State9"):
                opp_val = getattr(value, "statemachine_State9", None)
                setattr(value, "statemachine_State9", self)

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
            if hasattr(old_value, "statemachine_State4"):
                opp_val = getattr(old_value, "statemachine_State4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State4"):
                opp_val = getattr(value, "statemachine_State4", None)
                if opp_val is None:
                    setattr(value, "statemachine_State4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_Resource:

    def __init__(self, name: str, statemachine_Resource: "statemachine_StateMachine" = None, statemachine_Resource12: "statemachine_Need" = None):
        self.name = name
        self.statemachine_Resource = statemachine_Resource
        self.statemachine_Resource12 = statemachine_Resource12
        
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
    def statemachine_Resource12(self):
        return self.__statemachine_Resource12

    @statemachine_Resource12.setter
    def statemachine_Resource12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Resource__statemachine_Resource12", None)
        self.__statemachine_Resource12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Need11"):
                opp_val = getattr(old_value, "statemachine_Need11", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Need11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Need11"):
                opp_val = getattr(value, "statemachine_Need11", None)
                setattr(value, "statemachine_Need11", self)

class statemachine_State(ABC):

    def __init__(self, name: str, statemachine_State6: set["statemachine_Need"] = None, statemachine_State: "statemachine_StateMachine" = None, statemachine_State4: set["statemachine_Transition"] = None, statemachine_State9: "statemachine_Transition" = None):
        self.name = name
        self.statemachine_State6 = statemachine_State6 if statemachine_State6 is not None else set()
        self.statemachine_State = statemachine_State
        self.statemachine_State4 = statemachine_State4 if statemachine_State4 is not None else set()
        self.statemachine_State9 = statemachine_State9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_State6(self):
        return self.__statemachine_State6

    @statemachine_State6.setter
    def statemachine_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State6", None)
        self.__statemachine_State6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Need"):
                    opp_val = getattr(item, "statemachine_Need", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Need", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Need"):
                    opp_val = getattr(item, "statemachine_Need", None)
                    
                    setattr(item, "statemachine_Need", self)
                    

    @property
    def statemachine_State4(self):
        return self.__statemachine_State4

    @statemachine_State4.setter
    def statemachine_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State4", None)
        self.__statemachine_State4 = value if value is not None else set()
        
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

    @property
    def statemachine_State9(self):
        return self.__statemachine_State9

    @statemachine_State9.setter
    def statemachine_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State9", None)
        self.__statemachine_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition8"):
                opp_val = getattr(old_value, "statemachine_Transition8", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition8"):
                opp_val = getattr(value, "statemachine_Transition8", None)
                setattr(value, "statemachine_Transition8", self)

class statemachine_StateMachine:

    def __init__(self, name: str, statemachine_StateMachine: set["statemachine_State"] = None, statemachine_StateMachine2: set["statemachine_Resource"] = None):
        self.name = name
        self.statemachine_StateMachine = statemachine_StateMachine if statemachine_StateMachine is not None else set()
        self.statemachine_StateMachine2 = statemachine_StateMachine2 if statemachine_StateMachine2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    
