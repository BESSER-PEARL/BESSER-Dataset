from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    Final = "Final"
    Initial = "Initial"


############################################
# Definition of Classes
############################################

class Type:

    pass
class stateMachine_FloatType(Type):

    pass
class stateMachine_StringType(Type):

    pass
class stateMachine_VarName:

    def __init__(self, value: str, stateMachine_VarName: "stateMachine_DeclaredParameter" = None):
        self.value = value
        self.stateMachine_VarName = stateMachine_VarName
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def stateMachine_VarName(self):
        return self.__stateMachine_VarName

    @stateMachine_VarName.setter
    def stateMachine_VarName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_VarName__stateMachine_VarName", None)
        self.__stateMachine_VarName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_DeclaredParameter36"):
                opp_val = getattr(old_value, "stateMachine_DeclaredParameter36", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_DeclaredParameter36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_DeclaredParameter36"):
                opp_val = getattr(value, "stateMachine_DeclaredParameter36", None)
                setattr(value, "stateMachine_DeclaredParameter36", self)

class stateMachine_Condition:

    def __init__(self, name: str, stateMachine_Condition: "stateMachine_Transition" = None):
        self.name = name
        self.stateMachine_Condition = stateMachine_Condition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_Condition(self):
        return self.__stateMachine_Condition

    @stateMachine_Condition.setter
    def stateMachine_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Condition__stateMachine_Condition", None)
        self.__stateMachine_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Transition34"):
                opp_val = getattr(old_value, "stateMachine_Transition34", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Transition34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Transition34"):
                opp_val = getattr(value, "stateMachine_Transition34", None)
                setattr(value, "stateMachine_Transition34", self)

class stateMachine_Transition:

    pass
class stateMachine_Modifier:

    def __init__(self, visibility: str):
        self.visibility = visibility
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

class stateMachine_Test:

    pass
class stateMachine_Type:

    def __init__(self, type: str, stateMachine_Type19: "stateMachine_Test" = None, stateMachine_Type: "stateMachine_Event" = None):
        self.type = type
        self.stateMachine_Type19 = stateMachine_Type19
        self.stateMachine_Type = stateMachine_Type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def stateMachine_Type(self):
        return self.__stateMachine_Type

    @stateMachine_Type.setter
    def stateMachine_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Type__stateMachine_Type", None)
        self.__stateMachine_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Event14"):
                opp_val = getattr(old_value, "stateMachine_Event14", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Event14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Event14"):
                opp_val = getattr(value, "stateMachine_Event14", None)
                setattr(value, "stateMachine_Event14", self)

    @property
    def stateMachine_Type19(self):
        return self.__stateMachine_Type19

    @stateMachine_Type19.setter
    def stateMachine_Type19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Type__stateMachine_Type19", None)
        self.__stateMachine_Type19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Test18"):
                opp_val = getattr(old_value, "stateMachine_Test18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Test18"):
                opp_val = getattr(value, "stateMachine_Test18", None)
                if opp_val is None:
                    setattr(value, "stateMachine_Test18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stateMachine_State:

    def __init__(self, name: str, stateMachine_State: "stateMachine_StateMachine" = None, stateMachine_State9: "stateMachine_StateMachine" = None, stateMachine_State12: "stateMachine_StateMachine" = None, stateMachine_State23: set["stateMachine_Command"] = None, stateMachine_State26: set["stateMachine_Transition"] = None, stateMachine_State32: "stateMachine_Transition" = None):
        self.name = name
        self.stateMachine_State = stateMachine_State
        self.stateMachine_State9 = stateMachine_State9
        self.stateMachine_State12 = stateMachine_State12
        self.stateMachine_State23 = stateMachine_State23 if stateMachine_State23 is not None else set()
        self.stateMachine_State26 = stateMachine_State26 if stateMachine_State26 is not None else set()
        self.stateMachine_State32 = stateMachine_State32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_State12(self):
        return self.__stateMachine_State12

    @stateMachine_State12.setter
    def stateMachine_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State12", None)
        self.__stateMachine_State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine11"):
                opp_val = getattr(old_value, "stateMachine_StateMachine11", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_StateMachine11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine11"):
                opp_val = getattr(value, "stateMachine_StateMachine11", None)
                setattr(value, "stateMachine_StateMachine11", self)

    @property
    def stateMachine_State32(self):
        return self.__stateMachine_State32

    @stateMachine_State32.setter
    def stateMachine_State32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State32", None)
        self.__stateMachine_State32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Transition31"):
                opp_val = getattr(old_value, "stateMachine_Transition31", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Transition31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Transition31"):
                opp_val = getattr(value, "stateMachine_Transition31", None)
                setattr(value, "stateMachine_Transition31", self)

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
            if hasattr(old_value, "stateMachine_StateMachine6"):
                opp_val = getattr(old_value, "stateMachine_StateMachine6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine6"):
                opp_val = getattr(value, "stateMachine_StateMachine6", None)
                if opp_val is None:
                    setattr(value, "stateMachine_StateMachine6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_State9(self):
        return self.__stateMachine_State9

    @stateMachine_State9.setter
    def stateMachine_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State9", None)
        self.__stateMachine_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine8"):
                opp_val = getattr(old_value, "stateMachine_StateMachine8", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_StateMachine8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine8"):
                opp_val = getattr(value, "stateMachine_StateMachine8", None)
                setattr(value, "stateMachine_StateMachine8", self)

    @property
    def stateMachine_State23(self):
        return self.__stateMachine_State23

    @stateMachine_State23.setter
    def stateMachine_State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State23", None)
        self.__stateMachine_State23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_Command24"):
                    opp_val = getattr(item, "stateMachine_Command24", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_Command24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_Command24"):
                    opp_val = getattr(item, "stateMachine_Command24", None)
                    
                    setattr(item, "stateMachine_Command24", self)
                    

    @property
    def stateMachine_State26(self):
        return self.__stateMachine_State26

    @stateMachine_State26.setter
    def stateMachine_State26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State26", None)
        self.__stateMachine_State26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_Transition"):
                    opp_val = getattr(item, "stateMachine_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_Transition"):
                    opp_val = getattr(item, "stateMachine_Transition", None)
                    
                    setattr(item, "stateMachine_Transition", self)
                    

class stateMachine_Command:

    def __init__(self, name: str, stateMachine_Command: "stateMachine_StateMachine" = None, stateMachine_Command24: "stateMachine_State" = None):
        self.name = name
        self.stateMachine_Command = stateMachine_Command
        self.stateMachine_Command24 = stateMachine_Command24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_Command(self):
        return self.__stateMachine_Command

    @stateMachine_Command.setter
    def stateMachine_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Command__stateMachine_Command", None)
        self.__stateMachine_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine4"):
                opp_val = getattr(old_value, "stateMachine_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine4"):
                opp_val = getattr(value, "stateMachine_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "stateMachine_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_Command24(self):
        return self.__stateMachine_Command24

    @stateMachine_Command24.setter
    def stateMachine_Command24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Command__stateMachine_Command24", None)
        self.__stateMachine_Command24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_State23"):
                opp_val = getattr(old_value, "stateMachine_State23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_State23"):
                opp_val = getattr(value, "stateMachine_State23", None)
                if opp_val is None:
                    setattr(value, "stateMachine_State23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stateMachine_Event:

    def __init__(self, name: str, stateMachine_Event: "stateMachine_StateMachine" = None, stateMachine_Event14: "stateMachine_Type" = None, stateMachine_Event16: set["stateMachine_Test"] = None, stateMachine_Event29: "stateMachine_Transition" = None):
        self.name = name
        self.stateMachine_Event = stateMachine_Event
        self.stateMachine_Event14 = stateMachine_Event14
        self.stateMachine_Event16 = stateMachine_Event16 if stateMachine_Event16 is not None else set()
        self.stateMachine_Event29 = stateMachine_Event29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_Event14(self):
        return self.__stateMachine_Event14

    @stateMachine_Event14.setter
    def stateMachine_Event14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Event__stateMachine_Event14", None)
        self.__stateMachine_Event14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Type"):
                opp_val = getattr(old_value, "stateMachine_Type", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Type"):
                opp_val = getattr(value, "stateMachine_Type", None)
                setattr(value, "stateMachine_Type", self)

    @property
    def stateMachine_Event29(self):
        return self.__stateMachine_Event29

    @stateMachine_Event29.setter
    def stateMachine_Event29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Event__stateMachine_Event29", None)
        self.__stateMachine_Event29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Transition28"):
                opp_val = getattr(old_value, "stateMachine_Transition28", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Transition28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Transition28"):
                opp_val = getattr(value, "stateMachine_Transition28", None)
                setattr(value, "stateMachine_Transition28", self)

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
    def stateMachine_Event16(self):
        return self.__stateMachine_Event16

    @stateMachine_Event16.setter
    def stateMachine_Event16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Event__stateMachine_Event16", None)
        self.__stateMachine_Event16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_Test"):
                    opp_val = getattr(item, "stateMachine_Test", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_Test", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_Test"):
                    opp_val = getattr(item, "stateMachine_Test", None)
                    
                    setattr(item, "stateMachine_Test", self)
                    

class stateMachine_StateMachine:

    def __init__(self, name: str, stateMachine_StateMachine: "stateMachine_model" = None, stateMachine_StateMachine2: set["stateMachine_Event"] = None, stateMachine_StateMachine4: set["stateMachine_Command"] = None, stateMachine_StateMachine6: set["stateMachine_State"] = None, stateMachine_StateMachine8: "stateMachine_State" = None, stateMachine_StateMachine11: "stateMachine_State" = None):
        self.name = name
        self.stateMachine_StateMachine = stateMachine_StateMachine
        self.stateMachine_StateMachine2 = stateMachine_StateMachine2 if stateMachine_StateMachine2 is not None else set()
        self.stateMachine_StateMachine4 = stateMachine_StateMachine4 if stateMachine_StateMachine4 is not None else set()
        self.stateMachine_StateMachine6 = stateMachine_StateMachine6 if stateMachine_StateMachine6 is not None else set()
        self.stateMachine_StateMachine8 = stateMachine_StateMachine8
        self.stateMachine_StateMachine11 = stateMachine_StateMachine11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_StateMachine6(self):
        return self.__stateMachine_StateMachine6

    @stateMachine_StateMachine6.setter
    def stateMachine_StateMachine6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine6", None)
        self.__stateMachine_StateMachine6 = value if value is not None else set()
        
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
        self.__stateMachine_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_model"):
                opp_val = getattr(old_value, "stateMachine_model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_model"):
                opp_val = getattr(value, "stateMachine_model", None)
                if opp_val is None:
                    setattr(value, "stateMachine_model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_StateMachine4(self):
        return self.__stateMachine_StateMachine4

    @stateMachine_StateMachine4.setter
    def stateMachine_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine4", None)
        self.__stateMachine_StateMachine4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_Command"):
                    opp_val = getattr(item, "stateMachine_Command", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_Command", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_Command"):
                    opp_val = getattr(item, "stateMachine_Command", None)
                    
                    setattr(item, "stateMachine_Command", self)
                    

    @property
    def stateMachine_StateMachine8(self):
        return self.__stateMachine_StateMachine8

    @stateMachine_StateMachine8.setter
    def stateMachine_StateMachine8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine8", None)
        self.__stateMachine_StateMachine8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_State9"):
                opp_val = getattr(old_value, "stateMachine_State9", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_State9"):
                opp_val = getattr(value, "stateMachine_State9", None)
                setattr(value, "stateMachine_State9", self)

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
    def stateMachine_StateMachine11(self):
        return self.__stateMachine_StateMachine11

    @stateMachine_StateMachine11.setter
    def stateMachine_StateMachine11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine11", None)
        self.__stateMachine_StateMachine11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_State12"):
                opp_val = getattr(old_value, "stateMachine_State12", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_State12"):
                opp_val = getattr(value, "stateMachine_State12", None)
                setattr(value, "stateMachine_State12", self)

class stateMachine_model:

    pass
class stateMachine_DeclaredParameter:

    pass