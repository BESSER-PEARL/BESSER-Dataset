from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class StatemachineMetamodel_Transition:

    pass
class StatemachineMetamodel_State:

    def __init__(self, name: str, StatemachineMetamodel_State: "StatemachineMetamodel_Statemachine" = None, StatemachineMetamodel_State2: "StatemachineMetamodel_Transition" = None, StatemachineMetamodel_State4: set["StatemachineMetamodel_Transition"] = None):
        self.name = name
        self.StatemachineMetamodel_State = StatemachineMetamodel_State
        self.StatemachineMetamodel_State2 = StatemachineMetamodel_State2
        self.StatemachineMetamodel_State4 = StatemachineMetamodel_State4 if StatemachineMetamodel_State4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StatemachineMetamodel_State2(self):
        return self.__StatemachineMetamodel_State2

    @StatemachineMetamodel_State2.setter
    def StatemachineMetamodel_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StatemachineMetamodel_State__StatemachineMetamodel_State2", None)
        self.__StatemachineMetamodel_State2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StatemachineMetamodel_Transition"):
                opp_val = getattr(old_value, "StatemachineMetamodel_Transition", None)
                if opp_val == self:
                    setattr(old_value, "StatemachineMetamodel_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StatemachineMetamodel_Transition"):
                opp_val = getattr(value, "StatemachineMetamodel_Transition", None)
                setattr(value, "StatemachineMetamodel_Transition", self)

    @property
    def StatemachineMetamodel_State4(self):
        return self.__StatemachineMetamodel_State4

    @StatemachineMetamodel_State4.setter
    def StatemachineMetamodel_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StatemachineMetamodel_State__StatemachineMetamodel_State4", None)
        self.__StatemachineMetamodel_State4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StatemachineMetamodel_Transition5"):
                    opp_val = getattr(item, "StatemachineMetamodel_Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "StatemachineMetamodel_Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StatemachineMetamodel_Transition5"):
                    opp_val = getattr(item, "StatemachineMetamodel_Transition5", None)
                    
                    setattr(item, "StatemachineMetamodel_Transition5", self)
                    

    @property
    def StatemachineMetamodel_State(self):
        return self.__StatemachineMetamodel_State

    @StatemachineMetamodel_State.setter
    def StatemachineMetamodel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StatemachineMetamodel_State__StatemachineMetamodel_State", None)
        self.__StatemachineMetamodel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StatemachineMetamodel_Statemachine"):
                opp_val = getattr(old_value, "StatemachineMetamodel_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StatemachineMetamodel_Statemachine"):
                opp_val = getattr(value, "StatemachineMetamodel_Statemachine", None)
                if opp_val is None:
                    setattr(value, "StatemachineMetamodel_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StatemachineMetamodel_Statemachine:

    pass