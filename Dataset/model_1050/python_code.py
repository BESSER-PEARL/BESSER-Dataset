from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, event: str, fsm_Transition: "fsm_Machine" = None, fsm_Transition10: "fsm_State" = None, fsm_Transition13: "fsm_State" = None):
        self.event = event
        self.fsm_Transition = fsm_Transition
        self.fsm_Transition10 = fsm_Transition10
        self.fsm_Transition13 = fsm_Transition13
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def fsm_Transition10(self):
        return self.__fsm_Transition10

    @fsm_Transition10.setter
    def fsm_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition10", None)
        self.__fsm_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State11"):
                opp_val = getattr(old_value, "fsm_State11", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State11"):
                opp_val = getattr(value, "fsm_State11", None)
                setattr(value, "fsm_State11", self)

    @property
    def fsm_Transition(self):
        return self.__fsm_Transition

    @fsm_Transition.setter
    def fsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition", None)
        self.__fsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Machine8"):
                opp_val = getattr(old_value, "fsm_Machine8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Machine8"):
                opp_val = getattr(value, "fsm_Machine8", None)
                if opp_val is None:
                    setattr(value, "fsm_Machine8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Transition13(self):
        return self.__fsm_Transition13

    @fsm_Transition13.setter
    def fsm_Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition13", None)
        self.__fsm_Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State14"):
                opp_val = getattr(old_value, "fsm_State14", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State14"):
                opp_val = getattr(value, "fsm_State14", None)
                setattr(value, "fsm_State14", self)

class fsm_State:

    def __init__(self, initial: bool, final: bool, name: str, fsm_State: "fsm_Machine" = None, fsm_State11: "fsm_Transition" = None, fsm_State14: "fsm_Transition" = None):
        self.initial = initial
        self.final = final
        self.name = name
        self.fsm_State = fsm_State
        self.fsm_State11 = fsm_State11
        self.fsm_State14 = fsm_State14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def fsm_State14(self):
        return self.__fsm_State14

    @fsm_State14.setter
    def fsm_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State14", None)
        self.__fsm_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition13"):
                opp_val = getattr(old_value, "fsm_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition13"):
                opp_val = getattr(value, "fsm_Transition13", None)
                setattr(value, "fsm_Transition13", self)

    @property
    def fsm_State11(self):
        return self.__fsm_State11

    @fsm_State11.setter
    def fsm_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State11", None)
        self.__fsm_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition10"):
                opp_val = getattr(old_value, "fsm_Transition10", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition10"):
                opp_val = getattr(value, "fsm_Transition10", None)
                setattr(value, "fsm_Transition10", self)

    @property
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Machine6"):
                opp_val = getattr(old_value, "fsm_Machine6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Machine6"):
                opp_val = getattr(value, "fsm_Machine6", None)
                if opp_val is None:
                    setattr(value, "fsm_Machine6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_Machine:

    pass
class fsm_Language:

    def __init__(self, name: str, target: str, fsm_Language: "fsm_Model" = None):
        self.name = name
        self.target = target
        self.fsm_Language = fsm_Language
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def fsm_Language(self):
        return self.__fsm_Language

    @fsm_Language.setter
    def fsm_Language(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Language__fsm_Language", None)
        self.__fsm_Language = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Model2"):
                opp_val = getattr(old_value, "fsm_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Model2"):
                opp_val = getattr(value, "fsm_Model2", None)
                if opp_val is None:
                    setattr(value, "fsm_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_Constraint:

    def __init__(self, name: str, true: bool, fsm_Constraint: "fsm_Model" = None):
        self.name = name
        self.true = true
        self.fsm_Constraint = fsm_Constraint
        
    @property
    def true(self) -> bool:
        return self.__true

    @true.setter
    def true(self, true: bool):
        self.__true = true

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_Constraint(self):
        return self.__fsm_Constraint

    @fsm_Constraint.setter
    def fsm_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Constraint__fsm_Constraint", None)
        self.__fsm_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Model"):
                opp_val = getattr(old_value, "fsm_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Model"):
                opp_val = getattr(value, "fsm_Model", None)
                if opp_val is None:
                    setattr(value, "fsm_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_Model:

    def __init__(self, name: str, fsm_Model: set["fsm_Constraint"] = None, fsm_Model2: set["fsm_Language"] = None, fsm_Model4: "fsm_Machine" = None):
        self.name = name
        self.fsm_Model = fsm_Model if fsm_Model is not None else set()
        self.fsm_Model2 = fsm_Model2 if fsm_Model2 is not None else set()
        self.fsm_Model4 = fsm_Model4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_Model(self):
        return self.__fsm_Model

    @fsm_Model.setter
    def fsm_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Model__fsm_Model", None)
        self.__fsm_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Constraint"):
                    opp_val = getattr(item, "fsm_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Constraint"):
                    opp_val = getattr(item, "fsm_Constraint", None)
                    
                    setattr(item, "fsm_Constraint", self)
                    

    @property
    def fsm_Model4(self):
        return self.__fsm_Model4

    @fsm_Model4.setter
    def fsm_Model4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Model__fsm_Model4", None)
        self.__fsm_Model4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Machine"):
                opp_val = getattr(old_value, "fsm_Machine", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Machine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Machine"):
                opp_val = getattr(value, "fsm_Machine", None)
                setattr(value, "fsm_Machine", self)

    @property
    def fsm_Model2(self):
        return self.__fsm_Model2

    @fsm_Model2.setter
    def fsm_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Model__fsm_Model2", None)
        self.__fsm_Model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Language"):
                    opp_val = getattr(item, "fsm_Language", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Language", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Language"):
                    opp_val = getattr(item, "fsm_Language", None)
                    
                    setattr(item, "fsm_Language", self)
                    
