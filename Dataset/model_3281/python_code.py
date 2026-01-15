from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class statediagram_Transition:

    pass
class statediagram_StateDiagram:

    def __init__(self, name: str, statediagram_StateDiagram: set["statediagram_State"] = None):
        self.name = name
        self.statediagram_StateDiagram = statediagram_StateDiagram if statediagram_StateDiagram is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statediagram_StateDiagram(self):
        return self.__statediagram_StateDiagram

    @statediagram_StateDiagram.setter
    def statediagram_StateDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statediagram_StateDiagram__statediagram_StateDiagram", None)
        self.__statediagram_StateDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statediagram_State"):
                    opp_val = getattr(item, "statediagram_State", None)
                    
                    if opp_val == self:
                        setattr(item, "statediagram_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statediagram_State"):
                    opp_val = getattr(item, "statediagram_State", None)
                    
                    setattr(item, "statediagram_State", self)
                    

class statediagram_State:

    def __init__(self, name: str, isInitial: bool, statediagram_State: "statediagram_StateDiagram" = None, statediagram_State2: set["statediagram_Transition"] = None, statediagram_State5: "statediagram_Transition" = None):
        self.name = name
        self.isInitial = isInitial
        self.statediagram_State = statediagram_State
        self.statediagram_State2 = statediagram_State2 if statediagram_State2 is not None else set()
        self.statediagram_State5 = statediagram_State5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def statediagram_State5(self):
        return self.__statediagram_State5

    @statediagram_State5.setter
    def statediagram_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statediagram_State__statediagram_State5", None)
        self.__statediagram_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statediagram_Transition4"):
                opp_val = getattr(old_value, "statediagram_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "statediagram_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statediagram_Transition4"):
                opp_val = getattr(value, "statediagram_Transition4", None)
                setattr(value, "statediagram_Transition4", self)

    @property
    def statediagram_State(self):
        return self.__statediagram_State

    @statediagram_State.setter
    def statediagram_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statediagram_State__statediagram_State", None)
        self.__statediagram_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statediagram_StateDiagram"):
                opp_val = getattr(old_value, "statediagram_StateDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statediagram_StateDiagram"):
                opp_val = getattr(value, "statediagram_StateDiagram", None)
                if opp_val is None:
                    setattr(value, "statediagram_StateDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statediagram_State2(self):
        return self.__statediagram_State2

    @statediagram_State2.setter
    def statediagram_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statediagram_State__statediagram_State2", None)
        self.__statediagram_State2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statediagram_Transition"):
                    opp_val = getattr(item, "statediagram_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statediagram_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statediagram_Transition"):
                    opp_val = getattr(item, "statediagram_Transition", None)
                    
                    setattr(item, "statediagram_Transition", self)
                    
