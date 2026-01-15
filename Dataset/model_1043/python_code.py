from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class MetaModel_State(ABC):

    def __init__(self, name: str, MetaModel_State16: "MetaModel_InitialState" = None, MetaModel_State19: "MetaModel_IntermidiateState" = None, MetaModel_State22: "MetaModel_IntermidiateState" = None, MetaModel_State25: "MetaModel_FinalState" = None, MetaModel_State: "MetaModel_Transition" = None, MetaModel_State13: "MetaModel_Transition" = None):
        self.name = name
        self.MetaModel_State16 = MetaModel_State16
        self.MetaModel_State19 = MetaModel_State19
        self.MetaModel_State22 = MetaModel_State22
        self.MetaModel_State25 = MetaModel_State25
        self.MetaModel_State = MetaModel_State
        self.MetaModel_State13 = MetaModel_State13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MetaModel_State22(self):
        return self.__MetaModel_State22

    @MetaModel_State22.setter
    def MetaModel_State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_State__MetaModel_State22", None)
        self.__MetaModel_State22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_IntermidiateState21"):
                opp_val = getattr(old_value, "MetaModel_IntermidiateState21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_IntermidiateState21"):
                opp_val = getattr(value, "MetaModel_IntermidiateState21", None)
                if opp_val is None:
                    setattr(value, "MetaModel_IntermidiateState21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MetaModel_State(self):
        return self.__MetaModel_State

    @MetaModel_State.setter
    def MetaModel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_State__MetaModel_State", None)
        self.__MetaModel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_Transition10"):
                opp_val = getattr(old_value, "MetaModel_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "MetaModel_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_Transition10"):
                opp_val = getattr(value, "MetaModel_Transition10", None)
                setattr(value, "MetaModel_Transition10", self)

    @property
    def MetaModel_State16(self):
        return self.__MetaModel_State16

    @MetaModel_State16.setter
    def MetaModel_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_State__MetaModel_State16", None)
        self.__MetaModel_State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_InitialState15"):
                opp_val = getattr(old_value, "MetaModel_InitialState15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_InitialState15"):
                opp_val = getattr(value, "MetaModel_InitialState15", None)
                if opp_val is None:
                    setattr(value, "MetaModel_InitialState15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MetaModel_State13(self):
        return self.__MetaModel_State13

    @MetaModel_State13.setter
    def MetaModel_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_State__MetaModel_State13", None)
        self.__MetaModel_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_Transition12"):
                opp_val = getattr(old_value, "MetaModel_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "MetaModel_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_Transition12"):
                opp_val = getattr(value, "MetaModel_Transition12", None)
                setattr(value, "MetaModel_Transition12", self)

    @property
    def MetaModel_State25(self):
        return self.__MetaModel_State25

    @MetaModel_State25.setter
    def MetaModel_State25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_State__MetaModel_State25", None)
        self.__MetaModel_State25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_FinalState24"):
                opp_val = getattr(old_value, "MetaModel_FinalState24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_FinalState24"):
                opp_val = getattr(value, "MetaModel_FinalState24", None)
                if opp_val is None:
                    setattr(value, "MetaModel_FinalState24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MetaModel_State19(self):
        return self.__MetaModel_State19

    @MetaModel_State19.setter
    def MetaModel_State19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_State__MetaModel_State19", None)
        self.__MetaModel_State19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_IntermidiateState18"):
                opp_val = getattr(old_value, "MetaModel_IntermidiateState18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_IntermidiateState18"):
                opp_val = getattr(value, "MetaModel_IntermidiateState18", None)
                if opp_val is None:
                    setattr(value, "MetaModel_IntermidiateState18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MetaModel_Operation:

    def __init__(self, name: str, cost: str, time: str, MetaModel_Operation: "MetaModel_Transition" = None):
        self.name = name
        self.cost = cost
        self.time = time
        self.MetaModel_Operation = MetaModel_Operation
        
    @property
    def cost(self) -> str:
        return self.__cost

    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def MetaModel_Operation(self):
        return self.__MetaModel_Operation

    @MetaModel_Operation.setter
    def MetaModel_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_Operation__MetaModel_Operation", None)
        self.__MetaModel_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_Transition8"):
                opp_val = getattr(old_value, "MetaModel_Transition8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_Transition8"):
                opp_val = getattr(value, "MetaModel_Transition8", None)
                if opp_val is None:
                    setattr(value, "MetaModel_Transition8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MetaModel_FinalState(State):

    pass
class MetaModel_IntermidiateState(State):

    pass
class MetaModel_InitialState(State):

    pass
class MetaModel_Transition:

    def __init__(self, name: str, description: str, MetaModel_Transition: "MetaModel_EvolutionStyle" = None, MetaModel_Transition8: set["MetaModel_Operation"] = None, MetaModel_Transition10: "MetaModel_State" = None, MetaModel_Transition12: "MetaModel_State" = None):
        self.name = name
        self.description = description
        self.MetaModel_Transition = MetaModel_Transition
        self.MetaModel_Transition8 = MetaModel_Transition8 if MetaModel_Transition8 is not None else set()
        self.MetaModel_Transition10 = MetaModel_Transition10
        self.MetaModel_Transition12 = MetaModel_Transition12
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MetaModel_Transition(self):
        return self.__MetaModel_Transition

    @MetaModel_Transition.setter
    def MetaModel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_Transition__MetaModel_Transition", None)
        self.__MetaModel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_EvolutionStyle"):
                opp_val = getattr(old_value, "MetaModel_EvolutionStyle", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_EvolutionStyle"):
                opp_val = getattr(value, "MetaModel_EvolutionStyle", None)
                if opp_val is None:
                    setattr(value, "MetaModel_EvolutionStyle", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MetaModel_Transition10(self):
        return self.__MetaModel_Transition10

    @MetaModel_Transition10.setter
    def MetaModel_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_Transition__MetaModel_Transition10", None)
        self.__MetaModel_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_State"):
                opp_val = getattr(old_value, "MetaModel_State", None)
                if opp_val == self:
                    setattr(old_value, "MetaModel_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_State"):
                opp_val = getattr(value, "MetaModel_State", None)
                setattr(value, "MetaModel_State", self)

    @property
    def MetaModel_Transition8(self):
        return self.__MetaModel_Transition8

    @MetaModel_Transition8.setter
    def MetaModel_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_Transition__MetaModel_Transition8", None)
        self.__MetaModel_Transition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModel_Operation"):
                    opp_val = getattr(item, "MetaModel_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModel_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModel_Operation"):
                    opp_val = getattr(item, "MetaModel_Operation", None)
                    
                    setattr(item, "MetaModel_Operation", self)
                    

    @property
    def MetaModel_Transition12(self):
        return self.__MetaModel_Transition12

    @MetaModel_Transition12.setter
    def MetaModel_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_Transition__MetaModel_Transition12", None)
        self.__MetaModel_Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_State13"):
                opp_val = getattr(old_value, "MetaModel_State13", None)
                if opp_val == self:
                    setattr(old_value, "MetaModel_State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_State13"):
                opp_val = getattr(value, "MetaModel_State13", None)
                setattr(value, "MetaModel_State13", self)

class MetaModel_EvolutionStyle:

    def __init__(self, name: str, MetaModel_EvolutionStyle: set["MetaModel_Transition"] = None, MetaModel_EvolutionStyle2: "MetaModel_InitialState" = None, MetaModel_EvolutionStyle4: set["MetaModel_IntermidiateState"] = None, MetaModel_EvolutionStyle6: "MetaModel_FinalState" = None):
        self.name = name
        self.MetaModel_EvolutionStyle = MetaModel_EvolutionStyle if MetaModel_EvolutionStyle is not None else set()
        self.MetaModel_EvolutionStyle2 = MetaModel_EvolutionStyle2
        self.MetaModel_EvolutionStyle4 = MetaModel_EvolutionStyle4 if MetaModel_EvolutionStyle4 is not None else set()
        self.MetaModel_EvolutionStyle6 = MetaModel_EvolutionStyle6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MetaModel_EvolutionStyle6(self):
        return self.__MetaModel_EvolutionStyle6

    @MetaModel_EvolutionStyle6.setter
    def MetaModel_EvolutionStyle6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_EvolutionStyle__MetaModel_EvolutionStyle6", None)
        self.__MetaModel_EvolutionStyle6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_FinalState"):
                opp_val = getattr(old_value, "MetaModel_FinalState", None)
                if opp_val == self:
                    setattr(old_value, "MetaModel_FinalState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_FinalState"):
                opp_val = getattr(value, "MetaModel_FinalState", None)
                setattr(value, "MetaModel_FinalState", self)

    @property
    def MetaModel_EvolutionStyle2(self):
        return self.__MetaModel_EvolutionStyle2

    @MetaModel_EvolutionStyle2.setter
    def MetaModel_EvolutionStyle2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_EvolutionStyle__MetaModel_EvolutionStyle2", None)
        self.__MetaModel_EvolutionStyle2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetaModel_InitialState"):
                opp_val = getattr(old_value, "MetaModel_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "MetaModel_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetaModel_InitialState"):
                opp_val = getattr(value, "MetaModel_InitialState", None)
                setattr(value, "MetaModel_InitialState", self)

    @property
    def MetaModel_EvolutionStyle(self):
        return self.__MetaModel_EvolutionStyle

    @MetaModel_EvolutionStyle.setter
    def MetaModel_EvolutionStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_EvolutionStyle__MetaModel_EvolutionStyle", None)
        self.__MetaModel_EvolutionStyle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModel_Transition"):
                    opp_val = getattr(item, "MetaModel_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModel_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModel_Transition"):
                    opp_val = getattr(item, "MetaModel_Transition", None)
                    
                    setattr(item, "MetaModel_Transition", self)
                    

    @property
    def MetaModel_EvolutionStyle4(self):
        return self.__MetaModel_EvolutionStyle4

    @MetaModel_EvolutionStyle4.setter
    def MetaModel_EvolutionStyle4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetaModel_EvolutionStyle__MetaModel_EvolutionStyle4", None)
        self.__MetaModel_EvolutionStyle4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetaModel_IntermidiateState"):
                    opp_val = getattr(item, "MetaModel_IntermidiateState", None)
                    
                    if opp_val == self:
                        setattr(item, "MetaModel_IntermidiateState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetaModel_IntermidiateState"):
                    opp_val = getattr(item, "MetaModel_IntermidiateState", None)
                    
                    setattr(item, "MetaModel_IntermidiateState", self)
                    
