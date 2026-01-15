from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EFieldState(Enum):
    EDITABLE = "EDITABLE"
    READONLY = "READONLY"
    HIDDEN = "HIDDEN"


############################################
# Definition of Classes
############################################

class stateMachine_TransSet:

    pass
class stateMachine_FieldState:

    def __init__(self, state: str, stateMachine_FieldState23: "stateMachine_DocumentField" = None, stateMachine_FieldState: "stateMachine_State" = None):
        self.state = state
        self.stateMachine_FieldState23 = stateMachine_FieldState23
        self.stateMachine_FieldState = stateMachine_FieldState
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def stateMachine_FieldState(self):
        return self.__stateMachine_FieldState

    @stateMachine_FieldState.setter
    def stateMachine_FieldState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_FieldState__stateMachine_FieldState", None)
        self.__stateMachine_FieldState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_State13"):
                opp_val = getattr(old_value, "stateMachine_State13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_State13"):
                opp_val = getattr(value, "stateMachine_State13", None)
                if opp_val is None:
                    setattr(value, "stateMachine_State13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_FieldState23(self):
        return self.__stateMachine_FieldState23

    @stateMachine_FieldState23.setter
    def stateMachine_FieldState23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_FieldState__stateMachine_FieldState23", None)
        self.__stateMachine_FieldState23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_DocumentField24"):
                opp_val = getattr(old_value, "stateMachine_DocumentField24", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_DocumentField24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_DocumentField24"):
                opp_val = getattr(value, "stateMachine_DocumentField24", None)
                setattr(value, "stateMachine_DocumentField24", self)

class stateMachine_Trans:

    pass
class stateMachine_Role:

    def __init__(self, name: str, stateMachine_Role: "stateMachine_StateMachine" = None, stateMachine_Role30: "stateMachine_TransSet" = None):
        self.name = name
        self.stateMachine_Role = stateMachine_Role
        self.stateMachine_Role30 = stateMachine_Role30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_Role(self):
        return self.__stateMachine_Role

    @stateMachine_Role.setter
    def stateMachine_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Role__stateMachine_Role", None)
        self.__stateMachine_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine9"):
                opp_val = getattr(old_value, "stateMachine_StateMachine9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine9"):
                opp_val = getattr(value, "stateMachine_StateMachine9", None)
                if opp_val is None:
                    setattr(value, "stateMachine_StateMachine9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_Role30(self):
        return self.__stateMachine_Role30

    @stateMachine_Role30.setter
    def stateMachine_Role30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Role__stateMachine_Role30", None)
        self.__stateMachine_Role30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_TransSet29"):
                opp_val = getattr(old_value, "stateMachine_TransSet29", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_TransSet29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_TransSet29"):
                opp_val = getattr(value, "stateMachine_TransSet29", None)
                setattr(value, "stateMachine_TransSet29", self)

class stateMachine_DocumentField:

    def __init__(self, name: str, stateMachine_DocumentField24: "stateMachine_FieldState" = None, stateMachine_DocumentField: "stateMachine_StateMachine" = None):
        self.name = name
        self.stateMachine_DocumentField24 = stateMachine_DocumentField24
        self.stateMachine_DocumentField = stateMachine_DocumentField
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_DocumentField24(self):
        return self.__stateMachine_DocumentField24

    @stateMachine_DocumentField24.setter
    def stateMachine_DocumentField24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_DocumentField__stateMachine_DocumentField24", None)
        self.__stateMachine_DocumentField24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_FieldState23"):
                opp_val = getattr(old_value, "stateMachine_FieldState23", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_FieldState23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_FieldState23"):
                opp_val = getattr(value, "stateMachine_FieldState23", None)
                setattr(value, "stateMachine_FieldState23", self)

    @property
    def stateMachine_DocumentField(self):
        return self.__stateMachine_DocumentField

    @stateMachine_DocumentField.setter
    def stateMachine_DocumentField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_DocumentField__stateMachine_DocumentField", None)
        self.__stateMachine_DocumentField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine7"):
                opp_val = getattr(old_value, "stateMachine_StateMachine7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine7"):
                opp_val = getattr(value, "stateMachine_StateMachine7", None)
                if opp_val is None:
                    setattr(value, "stateMachine_StateMachine7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stateMachine_State:

    def __init__(self, name: str, stateMachine_State: "stateMachine_StateMachine" = None, stateMachine_State5: "stateMachine_StateMachine" = None, stateMachine_State11: set["stateMachine_Trans"] = None, stateMachine_State13: set["stateMachine_FieldState"] = None, stateMachine_State15: set["stateMachine_TransSet"] = None, stateMachine_State21: "stateMachine_Trans" = None):
        self.name = name
        self.stateMachine_State = stateMachine_State
        self.stateMachine_State5 = stateMachine_State5
        self.stateMachine_State11 = stateMachine_State11 if stateMachine_State11 is not None else set()
        self.stateMachine_State13 = stateMachine_State13 if stateMachine_State13 is not None else set()
        self.stateMachine_State15 = stateMachine_State15 if stateMachine_State15 is not None else set()
        self.stateMachine_State21 = stateMachine_State21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_State5(self):
        return self.__stateMachine_State5

    @stateMachine_State5.setter
    def stateMachine_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State5", None)
        self.__stateMachine_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine4"):
                opp_val = getattr(old_value, "stateMachine_StateMachine4", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_StateMachine4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine4"):
                opp_val = getattr(value, "stateMachine_StateMachine4", None)
                setattr(value, "stateMachine_StateMachine4", self)

    @property
    def stateMachine_State21(self):
        return self.__stateMachine_State21

    @stateMachine_State21.setter
    def stateMachine_State21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State21", None)
        self.__stateMachine_State21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Trans20"):
                opp_val = getattr(old_value, "stateMachine_Trans20", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Trans20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Trans20"):
                opp_val = getattr(value, "stateMachine_Trans20", None)
                setattr(value, "stateMachine_Trans20", self)

    @property
    def stateMachine_State15(self):
        return self.__stateMachine_State15

    @stateMachine_State15.setter
    def stateMachine_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State15", None)
        self.__stateMachine_State15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_TransSet"):
                    opp_val = getattr(item, "stateMachine_TransSet", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_TransSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_TransSet"):
                    opp_val = getattr(item, "stateMachine_TransSet", None)
                    
                    setattr(item, "stateMachine_TransSet", self)
                    

    @property
    def stateMachine_State(self):
        return self.__stateMachine_State

    @stateMachine_State.setter
    def stateMachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State", None)
        self.__stateMachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine2"):
                opp_val = getattr(old_value, "stateMachine_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine2"):
                opp_val = getattr(value, "stateMachine_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "stateMachine_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_State11(self):
        return self.__stateMachine_State11

    @stateMachine_State11.setter
    def stateMachine_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State11", None)
        self.__stateMachine_State11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_Trans"):
                    opp_val = getattr(item, "stateMachine_Trans", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_Trans", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_Trans"):
                    opp_val = getattr(item, "stateMachine_Trans", None)
                    
                    setattr(item, "stateMachine_Trans", self)
                    

    @property
    def stateMachine_State13(self):
        return self.__stateMachine_State13

    @stateMachine_State13.setter
    def stateMachine_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State13", None)
        self.__stateMachine_State13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_FieldState"):
                    opp_val = getattr(item, "stateMachine_FieldState", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_FieldState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_FieldState"):
                    opp_val = getattr(item, "stateMachine_FieldState", None)
                    
                    setattr(item, "stateMachine_FieldState", self)
                    

class stateMachine_Event:

    def __init__(self, name: str, stateMachine_Event: "stateMachine_StateMachine" = None, stateMachine_Event18: "stateMachine_Trans" = None):
        self.name = name
        self.stateMachine_Event = stateMachine_Event
        self.stateMachine_Event18 = stateMachine_Event18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_Event18(self):
        return self.__stateMachine_Event18

    @stateMachine_Event18.setter
    def stateMachine_Event18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Event__stateMachine_Event18", None)
        self.__stateMachine_Event18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Trans17"):
                opp_val = getattr(old_value, "stateMachine_Trans17", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Trans17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Trans17"):
                opp_val = getattr(value, "stateMachine_Trans17", None)
                setattr(value, "stateMachine_Trans17", self)

    @property
    def stateMachine_Event(self):
        return self.__stateMachine_Event

    @stateMachine_Event.setter
    def stateMachine_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Event__stateMachine_Event", None)
        self.__stateMachine_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine"):
                opp_val = getattr(old_value, "stateMachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine"):
                opp_val = getattr(value, "stateMachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "stateMachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stateMachine_StateMachine:

    def __init__(self, name: str, package: str, stateMachine_StateMachine: set["stateMachine_Event"] = None, stateMachine_StateMachine2: set["stateMachine_State"] = None, stateMachine_StateMachine4: "stateMachine_State" = None, stateMachine_StateMachine7: set["stateMachine_DocumentField"] = None, stateMachine_StateMachine9: set["stateMachine_Role"] = None):
        self.name = name
        self.package = package
        self.stateMachine_StateMachine = stateMachine_StateMachine if stateMachine_StateMachine is not None else set()
        self.stateMachine_StateMachine2 = stateMachine_StateMachine2 if stateMachine_StateMachine2 is not None else set()
        self.stateMachine_StateMachine4 = stateMachine_StateMachine4
        self.stateMachine_StateMachine7 = stateMachine_StateMachine7 if stateMachine_StateMachine7 is not None else set()
        self.stateMachine_StateMachine9 = stateMachine_StateMachine9 if stateMachine_StateMachine9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def stateMachine_StateMachine4(self):
        return self.__stateMachine_StateMachine4

    @stateMachine_StateMachine4.setter
    def stateMachine_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine4", None)
        self.__stateMachine_StateMachine4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_State5"):
                opp_val = getattr(old_value, "stateMachine_State5", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_State5"):
                opp_val = getattr(value, "stateMachine_State5", None)
                setattr(value, "stateMachine_State5", self)

    @property
    def stateMachine_StateMachine9(self):
        return self.__stateMachine_StateMachine9

    @stateMachine_StateMachine9.setter
    def stateMachine_StateMachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine9", None)
        self.__stateMachine_StateMachine9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_Role"):
                    opp_val = getattr(item, "stateMachine_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_Role"):
                    opp_val = getattr(item, "stateMachine_Role", None)
                    
                    setattr(item, "stateMachine_Role", self)
                    

    @property
    def stateMachine_StateMachine2(self):
        return self.__stateMachine_StateMachine2

    @stateMachine_StateMachine2.setter
    def stateMachine_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine2", None)
        self.__stateMachine_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_State"):
                    opp_val = getattr(item, "stateMachine_State", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_State"):
                    opp_val = getattr(item, "stateMachine_State", None)
                    
                    setattr(item, "stateMachine_State", self)
                    

    @property
    def stateMachine_StateMachine(self):
        return self.__stateMachine_StateMachine

    @stateMachine_StateMachine.setter
    def stateMachine_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine", None)
        self.__stateMachine_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_Event"):
                    opp_val = getattr(item, "stateMachine_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_Event"):
                    opp_val = getattr(item, "stateMachine_Event", None)
                    
                    setattr(item, "stateMachine_Event", self)
                    

    @property
    def stateMachine_StateMachine7(self):
        return self.__stateMachine_StateMachine7

    @stateMachine_StateMachine7.setter
    def stateMachine_StateMachine7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine7", None)
        self.__stateMachine_StateMachine7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_DocumentField"):
                    opp_val = getattr(item, "stateMachine_DocumentField", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_DocumentField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_DocumentField"):
                    opp_val = getattr(item, "stateMachine_DocumentField", None)
                    
                    setattr(item, "stateMachine_DocumentField", self)
                    
