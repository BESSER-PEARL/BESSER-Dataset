from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TransStatus(Enum):
    normal = "normal"
    error = "error"
    unsafeTrans = "unsafeTrans"
    redundantTrans = "redundantTrans"
class StateStatus(Enum):
    new = "new"
    unSafeState = "unSafeState"
    Repeated = "Repeated"


############################################
# Definition of Classes
############################################

class execTraces_Edge:

    def __init__(self, guard: str, trigger: str, actions: str, status: str, execTraces_Edge13: "execTraces_Node" = None, execTraces_Edge16: "execTraces_Node" = None, execTraces_Edge: "execTraces_ExecTraces" = None, execTraces_Edge4: "execTraces_Node" = None, execTraces_Edge7: "execTraces_Node" = None):
        self.guard = guard
        self.trigger = trigger
        self.actions = actions
        self.status = status
        self.execTraces_Edge13 = execTraces_Edge13
        self.execTraces_Edge16 = execTraces_Edge16
        self.execTraces_Edge = execTraces_Edge
        self.execTraces_Edge4 = execTraces_Edge4
        self.execTraces_Edge7 = execTraces_Edge7
        
    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def actions(self) -> str:
        return self.__actions

    @actions.setter
    def actions(self, actions: str):
        self.__actions = actions

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def execTraces_Edge4(self):
        return self.__execTraces_Edge4

    @execTraces_Edge4.setter
    def execTraces_Edge4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Edge__execTraces_Edge4", None)
        self.__execTraces_Edge4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execTraces_Node5"):
                opp_val = getattr(old_value, "execTraces_Node5", None)
                if opp_val == self:
                    setattr(old_value, "execTraces_Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execTraces_Node5"):
                opp_val = getattr(value, "execTraces_Node5", None)
                setattr(value, "execTraces_Node5", self)

    @property
    def execTraces_Edge13(self):
        return self.__execTraces_Edge13

    @execTraces_Edge13.setter
    def execTraces_Edge13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Edge__execTraces_Edge13", None)
        self.__execTraces_Edge13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execTraces_Node12"):
                opp_val = getattr(old_value, "execTraces_Node12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execTraces_Node12"):
                opp_val = getattr(value, "execTraces_Node12", None)
                if opp_val is None:
                    setattr(value, "execTraces_Node12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def execTraces_Edge16(self):
        return self.__execTraces_Edge16

    @execTraces_Edge16.setter
    def execTraces_Edge16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Edge__execTraces_Edge16", None)
        self.__execTraces_Edge16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execTraces_Node15"):
                opp_val = getattr(old_value, "execTraces_Node15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execTraces_Node15"):
                opp_val = getattr(value, "execTraces_Node15", None)
                if opp_val is None:
                    setattr(value, "execTraces_Node15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def execTraces_Edge7(self):
        return self.__execTraces_Edge7

    @execTraces_Edge7.setter
    def execTraces_Edge7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Edge__execTraces_Edge7", None)
        self.__execTraces_Edge7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execTraces_Node8"):
                opp_val = getattr(old_value, "execTraces_Node8", None)
                if opp_val == self:
                    setattr(old_value, "execTraces_Node8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execTraces_Node8"):
                opp_val = getattr(value, "execTraces_Node8", None)
                setattr(value, "execTraces_Node8", self)

    @property
    def execTraces_Edge(self):
        return self.__execTraces_Edge

    @execTraces_Edge.setter
    def execTraces_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Edge__execTraces_Edge", None)
        self.__execTraces_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execTraces_ExecTraces2"):
                opp_val = getattr(old_value, "execTraces_ExecTraces2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execTraces_ExecTraces2"):
                opp_val = getattr(value, "execTraces_ExecTraces2", None)
                if opp_val is None:
                    setattr(value, "execTraces_ExecTraces2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Literal:

    pass
class execTraces_IntLiteral(Literal):

    def __init__(self, int: int):
        self.int = int
        
    @property
    def int(self) -> int:
        return self.__int

    @int.setter
    def int(self, int: int):
        self.__int = int

class execTraces_BoolLiteral(Literal):

    def __init__(self, bool: str):
        self.bool = bool
        
    @property
    def bool(self) -> str:
        return self.__bool

    @bool.setter
    def bool(self, bool: str):
        self.__bool = bool

class execTraces_RealLiteral(Literal):

    def __init__(self, intPart: int, decimalPart: int):
        self.intPart = intPart
        self.decimalPart = decimalPart
        
    @property
    def intPart(self) -> int:
        return self.__intPart

    @intPart.setter
    def intPart(self, intPart: int):
        self.__intPart = intPart

    @property
    def decimalPart(self) -> int:
        return self.__decimalPart

    @decimalPart.setter
    def decimalPart(self, decimalPart: int):
        self.__decimalPart = decimalPart

class execTraces_Literal:

    pass
class execTraces_Variable:

    def __init__(self, name: str, execTraces_Variable: "execTraces_Node" = None, execTraces_Variable18: "execTraces_Literal" = None):
        self.name = name
        self.execTraces_Variable = execTraces_Variable
        self.execTraces_Variable18 = execTraces_Variable18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def execTraces_Variable18(self):
        return self.__execTraces_Variable18

    @execTraces_Variable18.setter
    def execTraces_Variable18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Variable__execTraces_Variable18", None)
        self.__execTraces_Variable18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execTraces_Literal"):
                opp_val = getattr(old_value, "execTraces_Literal", None)
                if opp_val == self:
                    setattr(old_value, "execTraces_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execTraces_Literal"):
                opp_val = getattr(value, "execTraces_Literal", None)
                setattr(value, "execTraces_Literal", self)

    @property
    def execTraces_Variable(self):
        return self.__execTraces_Variable

    @execTraces_Variable.setter
    def execTraces_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Variable__execTraces_Variable", None)
        self.__execTraces_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execTraces_Node10"):
                opp_val = getattr(old_value, "execTraces_Node10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execTraces_Node10"):
                opp_val = getattr(value, "execTraces_Node10", None)
                if opp_val is None:
                    setattr(value, "execTraces_Node10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class execTraces_Node:

    def __init__(self, name: str, id: int, level: int, status: str, constraints: str, execTraces_Node: "execTraces_ExecTraces" = None, execTraces_Node10: set["execTraces_Variable"] = None, execTraces_Node12: set["execTraces_Edge"] = None, execTraces_Node15: set["execTraces_Edge"] = None, execTraces_Node5: "execTraces_Edge" = None, execTraces_Node8: "execTraces_Edge" = None):
        self.name = name
        self.id = id
        self.level = level
        self.status = status
        self.constraints = constraints
        self.execTraces_Node = execTraces_Node
        self.execTraces_Node10 = execTraces_Node10 if execTraces_Node10 is not None else set()
        self.execTraces_Node12 = execTraces_Node12 if execTraces_Node12 is not None else set()
        self.execTraces_Node15 = execTraces_Node15 if execTraces_Node15 is not None else set()
        self.execTraces_Node5 = execTraces_Node5
        self.execTraces_Node8 = execTraces_Node8
        
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def constraints(self) -> str:
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: str):
        self.__constraints = constraints

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def execTraces_Node(self):
        return self.__execTraces_Node

    @execTraces_Node.setter
    def execTraces_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Node__execTraces_Node", None)
        self.__execTraces_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execTraces_ExecTraces"):
                opp_val = getattr(old_value, "execTraces_ExecTraces", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execTraces_ExecTraces"):
                opp_val = getattr(value, "execTraces_ExecTraces", None)
                if opp_val is None:
                    setattr(value, "execTraces_ExecTraces", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def execTraces_Node12(self):
        return self.__execTraces_Node12

    @execTraces_Node12.setter
    def execTraces_Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Node__execTraces_Node12", None)
        self.__execTraces_Node12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "execTraces_Edge13"):
                    opp_val = getattr(item, "execTraces_Edge13", None)
                    
                    if opp_val == self:
                        setattr(item, "execTraces_Edge13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "execTraces_Edge13"):
                    opp_val = getattr(item, "execTraces_Edge13", None)
                    
                    setattr(item, "execTraces_Edge13", self)
                    

    @property
    def execTraces_Node5(self):
        return self.__execTraces_Node5

    @execTraces_Node5.setter
    def execTraces_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Node__execTraces_Node5", None)
        self.__execTraces_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execTraces_Edge4"):
                opp_val = getattr(old_value, "execTraces_Edge4", None)
                if opp_val == self:
                    setattr(old_value, "execTraces_Edge4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execTraces_Edge4"):
                opp_val = getattr(value, "execTraces_Edge4", None)
                setattr(value, "execTraces_Edge4", self)

    @property
    def execTraces_Node15(self):
        return self.__execTraces_Node15

    @execTraces_Node15.setter
    def execTraces_Node15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Node__execTraces_Node15", None)
        self.__execTraces_Node15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "execTraces_Edge16"):
                    opp_val = getattr(item, "execTraces_Edge16", None)
                    
                    if opp_val == self:
                        setattr(item, "execTraces_Edge16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "execTraces_Edge16"):
                    opp_val = getattr(item, "execTraces_Edge16", None)
                    
                    setattr(item, "execTraces_Edge16", self)
                    

    @property
    def execTraces_Node8(self):
        return self.__execTraces_Node8

    @execTraces_Node8.setter
    def execTraces_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Node__execTraces_Node8", None)
        self.__execTraces_Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execTraces_Edge7"):
                opp_val = getattr(old_value, "execTraces_Edge7", None)
                if opp_val == self:
                    setattr(old_value, "execTraces_Edge7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execTraces_Edge7"):
                opp_val = getattr(value, "execTraces_Edge7", None)
                setattr(value, "execTraces_Edge7", self)

    @property
    def execTraces_Node10(self):
        return self.__execTraces_Node10

    @execTraces_Node10.setter
    def execTraces_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_Node__execTraces_Node10", None)
        self.__execTraces_Node10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "execTraces_Variable"):
                    opp_val = getattr(item, "execTraces_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "execTraces_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "execTraces_Variable"):
                    opp_val = getattr(item, "execTraces_Variable", None)
                    
                    setattr(item, "execTraces_Variable", self)
                    

class execTraces_ExecTraces:

    def __init__(self, ComponentName: str, execTraces_ExecTraces: set["execTraces_Node"] = None, execTraces_ExecTraces2: set["execTraces_Edge"] = None):
        self.ComponentName = ComponentName
        self.execTraces_ExecTraces = execTraces_ExecTraces if execTraces_ExecTraces is not None else set()
        self.execTraces_ExecTraces2 = execTraces_ExecTraces2 if execTraces_ExecTraces2 is not None else set()
        
    @property
    def ComponentName(self) -> str:
        return self.__ComponentName

    @ComponentName.setter
    def ComponentName(self, ComponentName: str):
        self.__ComponentName = ComponentName

    @property
    def execTraces_ExecTraces(self):
        return self.__execTraces_ExecTraces

    @execTraces_ExecTraces.setter
    def execTraces_ExecTraces(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_ExecTraces__execTraces_ExecTraces", None)
        self.__execTraces_ExecTraces = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "execTraces_Node"):
                    opp_val = getattr(item, "execTraces_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "execTraces_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "execTraces_Node"):
                    opp_val = getattr(item, "execTraces_Node", None)
                    
                    setattr(item, "execTraces_Node", self)
                    

    @property
    def execTraces_ExecTraces2(self):
        return self.__execTraces_ExecTraces2

    @execTraces_ExecTraces2.setter
    def execTraces_ExecTraces2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_execTraces_ExecTraces__execTraces_ExecTraces2", None)
        self.__execTraces_ExecTraces2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "execTraces_Edge"):
                    opp_val = getattr(item, "execTraces_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "execTraces_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "execTraces_Edge"):
                    opp_val = getattr(item, "execTraces_Edge", None)
                    
                    setattr(item, "execTraces_Edge", self)
                    
