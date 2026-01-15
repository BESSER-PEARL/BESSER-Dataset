from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class GExpression:

    pass
class gpfl_CmdEq(GExpression):

    pass
class gpfl_Variable(GExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class gpfl_IntLitCmd(GExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class gpfl_StpCmd(GExpression):

    pass
class gpfl_AutomatonCmd(GExpression):

    def __init__(self, name: str, gpfl_AutomatonCmd: "gpfl_AutomataDef" = None, gpfl_AutomatonCmd48: "gpfl_StpCmd" = None):
        self.name = name
        self.gpfl_AutomatonCmd = gpfl_AutomatonCmd
        self.gpfl_AutomatonCmd48 = gpfl_AutomatonCmd48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gpfl_AutomatonCmd(self):
        return self.__gpfl_AutomatonCmd

    @gpfl_AutomatonCmd.setter
    def gpfl_AutomatonCmd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_AutomatonCmd__gpfl_AutomatonCmd", None)
        self.__gpfl_AutomatonCmd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_AutomataDef46"):
                opp_val = getattr(old_value, "gpfl_AutomataDef46", None)
                if opp_val == self:
                    setattr(old_value, "gpfl_AutomataDef46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_AutomataDef46"):
                opp_val = getattr(value, "gpfl_AutomataDef46", None)
                setattr(value, "gpfl_AutomataDef46", self)

    @property
    def gpfl_AutomatonCmd48(self):
        return self.__gpfl_AutomatonCmd48

    @gpfl_AutomatonCmd48.setter
    def gpfl_AutomatonCmd48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_AutomatonCmd__gpfl_AutomatonCmd48", None)
        self.__gpfl_AutomatonCmd48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_StpCmd"):
                opp_val = getattr(old_value, "gpfl_StpCmd", None)
                if opp_val == self:
                    setattr(old_value, "gpfl_StpCmd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_StpCmd"):
                opp_val = getattr(value, "gpfl_StpCmd", None)
                setattr(value, "gpfl_StpCmd", self)

class gpfl_InPort(GExpression):

    pass
class gpfl_CmdNEq(GExpression):

    pass
class gpfl_PortLit(GExpression):

    def __init__(self, inSide: bool):
        self.inSide = inSide
        
    @property
    def inSide(self) -> bool:
        return self.__inSide

    @inSide.setter
    def inSide(self, inSide: bool):
        self.__inSide = inSide

class gpfl_CmdAnd(GExpression):

    pass
class gpfl_StringLit(GExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class gpfl_OutPort(GExpression):

    pass
class gpfl_CmdLCompare(GExpression):

    pass
class gpfl_AlarmCmd(GExpression):

    pass
class gpfl_SetCmd(GExpression):

    def __init__(self, name: str, gpfl_SetCmd: "gpfl_GExpression" = None):
        self.name = name
        self.gpfl_SetCmd = gpfl_SetCmd
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gpfl_SetCmd(self):
        return self.__gpfl_SetCmd

    @gpfl_SetCmd.setter
    def gpfl_SetCmd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_SetCmd__gpfl_SetCmd", None)
        self.__gpfl_SetCmd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_GExpression44"):
                opp_val = getattr(old_value, "gpfl_GExpression44", None)
                if opp_val == self:
                    setattr(old_value, "gpfl_GExpression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_GExpression44"):
                opp_val = getattr(value, "gpfl_GExpression44", None)
                setattr(value, "gpfl_GExpression44", self)

class gpfl_CmdGCompare(GExpression):

    pass
class gpfl_CmdGECompare(GExpression):

    pass
class gpfl_CmdAdd(GExpression):

    pass
class gpfl_GBoolTrue(GExpression):

    pass
class gpfl_CmdLECompare(GExpression):

    pass
class gpfl_GBoolFalse(GExpression):

    pass
class gpfl_CmdSub(GExpression):

    pass
class gpfl_InterruptStmt(GExpression):

    def __init__(self, timeout: int, gpfl_InterruptStmt34: set["gpfl_GExpression"] = None, gpfl_InterruptStmt: "gpfl_GExpression" = None):
        self.timeout = timeout
        self.gpfl_InterruptStmt34 = gpfl_InterruptStmt34 if gpfl_InterruptStmt34 is not None else set()
        self.gpfl_InterruptStmt = gpfl_InterruptStmt
        
    @property
    def timeout(self) -> int:
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: int):
        self.__timeout = timeout

    @property
    def gpfl_InterruptStmt34(self):
        return self.__gpfl_InterruptStmt34

    @gpfl_InterruptStmt34.setter
    def gpfl_InterruptStmt34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_InterruptStmt__gpfl_InterruptStmt34", None)
        self.__gpfl_InterruptStmt34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gpfl_GExpression35"):
                    opp_val = getattr(item, "gpfl_GExpression35", None)
                    
                    if opp_val == self:
                        setattr(item, "gpfl_GExpression35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gpfl_GExpression35"):
                    opp_val = getattr(item, "gpfl_GExpression35", None)
                    
                    setattr(item, "gpfl_GExpression35", self)
                    

    @property
    def gpfl_InterruptStmt(self):
        return self.__gpfl_InterruptStmt

    @gpfl_InterruptStmt.setter
    def gpfl_InterruptStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_InterruptStmt__gpfl_InterruptStmt", None)
        self.__gpfl_InterruptStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_GExpression32"):
                opp_val = getattr(old_value, "gpfl_GExpression32", None)
                if opp_val == self:
                    setattr(old_value, "gpfl_GExpression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_GExpression32"):
                opp_val = getattr(value, "gpfl_GExpression32", None)
                setattr(value, "gpfl_GExpression32", self)

class gpfl_IterStmt(GExpression):

    pass
class gpfl_CondStmt(GExpression):

    pass
class gpfl_Transition:

    def __init__(self, event: str, gpfl_Transition: "gpfl_State" = None, gpfl_Transition19: "gpfl_State" = None):
        self.event = event
        self.gpfl_Transition = gpfl_Transition
        self.gpfl_Transition19 = gpfl_Transition19
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def gpfl_Transition19(self):
        return self.__gpfl_Transition19

    @gpfl_Transition19.setter
    def gpfl_Transition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_Transition__gpfl_Transition19", None)
        self.__gpfl_Transition19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_State20"):
                opp_val = getattr(old_value, "gpfl_State20", None)
                if opp_val == self:
                    setattr(old_value, "gpfl_State20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_State20"):
                opp_val = getattr(value, "gpfl_State20", None)
                setattr(value, "gpfl_State20", self)

    @property
    def gpfl_Transition(self):
        return self.__gpfl_Transition

    @gpfl_Transition.setter
    def gpfl_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_Transition__gpfl_Transition", None)
        self.__gpfl_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_State17"):
                opp_val = getattr(old_value, "gpfl_State17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_State17"):
                opp_val = getattr(value, "gpfl_State17", None)
                if opp_val is None:
                    setattr(value, "gpfl_State17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gpfl_State:

    def __init__(self, name: str, gpfl_State: "gpfl_AutomataDef" = None, gpfl_State15: "gpfl_AutomataDef" = None, gpfl_State17: set["gpfl_Transition"] = None, gpfl_State20: "gpfl_Transition" = None):
        self.name = name
        self.gpfl_State = gpfl_State
        self.gpfl_State15 = gpfl_State15
        self.gpfl_State17 = gpfl_State17 if gpfl_State17 is not None else set()
        self.gpfl_State20 = gpfl_State20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gpfl_State20(self):
        return self.__gpfl_State20

    @gpfl_State20.setter
    def gpfl_State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_State__gpfl_State20", None)
        self.__gpfl_State20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_Transition19"):
                opp_val = getattr(old_value, "gpfl_Transition19", None)
                if opp_val == self:
                    setattr(old_value, "gpfl_Transition19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_Transition19"):
                opp_val = getattr(value, "gpfl_Transition19", None)
                setattr(value, "gpfl_Transition19", self)

    @property
    def gpfl_State15(self):
        return self.__gpfl_State15

    @gpfl_State15.setter
    def gpfl_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_State__gpfl_State15", None)
        self.__gpfl_State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_AutomataDef14"):
                opp_val = getattr(old_value, "gpfl_AutomataDef14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_AutomataDef14"):
                opp_val = getattr(value, "gpfl_AutomataDef14", None)
                if opp_val is None:
                    setattr(value, "gpfl_AutomataDef14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gpfl_State(self):
        return self.__gpfl_State

    @gpfl_State.setter
    def gpfl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_State__gpfl_State", None)
        self.__gpfl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_AutomataDef12"):
                opp_val = getattr(old_value, "gpfl_AutomataDef12", None)
                if opp_val == self:
                    setattr(old_value, "gpfl_AutomataDef12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_AutomataDef12"):
                opp_val = getattr(value, "gpfl_AutomataDef12", None)
                setattr(value, "gpfl_AutomataDef12", self)

    @property
    def gpfl_State17(self):
        return self.__gpfl_State17

    @gpfl_State17.setter
    def gpfl_State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_State__gpfl_State17", None)
        self.__gpfl_State17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gpfl_Transition"):
                    opp_val = getattr(item, "gpfl_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "gpfl_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gpfl_Transition"):
                    opp_val = getattr(item, "gpfl_Transition", None)
                    
                    setattr(item, "gpfl_Transition", self)
                    

class gpfl_SendCmd(GExpression):

    pass
class gpfl_DropCmd(GExpression):

    pass
class gpfl_AcceptCmd(GExpression):

    pass
class gpfl_NopCmd(GExpression):

    pass
class gpfl_GExpression:

    pass
class gpfl_AutomataDef:

    def __init__(self, name: str, gpfl_AutomataDef: "gpfl_Program" = None, gpfl_AutomataDef12: "gpfl_State" = None, gpfl_AutomataDef14: set["gpfl_State"] = None, gpfl_AutomataDef46: "gpfl_AutomatonCmd" = None):
        self.name = name
        self.gpfl_AutomataDef = gpfl_AutomataDef
        self.gpfl_AutomataDef12 = gpfl_AutomataDef12
        self.gpfl_AutomataDef14 = gpfl_AutomataDef14 if gpfl_AutomataDef14 is not None else set()
        self.gpfl_AutomataDef46 = gpfl_AutomataDef46
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gpfl_AutomataDef12(self):
        return self.__gpfl_AutomataDef12

    @gpfl_AutomataDef12.setter
    def gpfl_AutomataDef12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_AutomataDef__gpfl_AutomataDef12", None)
        self.__gpfl_AutomataDef12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_State"):
                opp_val = getattr(old_value, "gpfl_State", None)
                if opp_val == self:
                    setattr(old_value, "gpfl_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_State"):
                opp_val = getattr(value, "gpfl_State", None)
                setattr(value, "gpfl_State", self)

    @property
    def gpfl_AutomataDef(self):
        return self.__gpfl_AutomataDef

    @gpfl_AutomataDef.setter
    def gpfl_AutomataDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_AutomataDef__gpfl_AutomataDef", None)
        self.__gpfl_AutomataDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_Program"):
                opp_val = getattr(old_value, "gpfl_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_Program"):
                opp_val = getattr(value, "gpfl_Program", None)
                if opp_val is None:
                    setattr(value, "gpfl_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gpfl_AutomataDef46(self):
        return self.__gpfl_AutomataDef46

    @gpfl_AutomataDef46.setter
    def gpfl_AutomataDef46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_AutomataDef__gpfl_AutomataDef46", None)
        self.__gpfl_AutomataDef46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_AutomatonCmd"):
                opp_val = getattr(old_value, "gpfl_AutomatonCmd", None)
                if opp_val == self:
                    setattr(old_value, "gpfl_AutomatonCmd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_AutomatonCmd"):
                opp_val = getattr(value, "gpfl_AutomatonCmd", None)
                setattr(value, "gpfl_AutomatonCmd", self)

    @property
    def gpfl_AutomataDef14(self):
        return self.__gpfl_AutomataDef14

    @gpfl_AutomataDef14.setter
    def gpfl_AutomataDef14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_AutomataDef__gpfl_AutomataDef14", None)
        self.__gpfl_AutomataDef14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gpfl_State15"):
                    opp_val = getattr(item, "gpfl_State15", None)
                    
                    if opp_val == self:
                        setattr(item, "gpfl_State15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gpfl_State15"):
                    opp_val = getattr(item, "gpfl_State15", None)
                    
                    setattr(item, "gpfl_State15", self)
                    

class gpfl_Program:

    def __init__(self, name: str, gpfl_Program: set["gpfl_AutomataDef"] = None, gpfl_Program2: set["gpfl_GExpression"] = None, gpfl_Program4: set["gpfl_GExpression"] = None):
        self.name = name
        self.gpfl_Program = gpfl_Program if gpfl_Program is not None else set()
        self.gpfl_Program2 = gpfl_Program2 if gpfl_Program2 is not None else set()
        self.gpfl_Program4 = gpfl_Program4 if gpfl_Program4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gpfl_Program(self):
        return self.__gpfl_Program

    @gpfl_Program.setter
    def gpfl_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_Program__gpfl_Program", None)
        self.__gpfl_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gpfl_AutomataDef"):
                    opp_val = getattr(item, "gpfl_AutomataDef", None)
                    
                    if opp_val == self:
                        setattr(item, "gpfl_AutomataDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gpfl_AutomataDef"):
                    opp_val = getattr(item, "gpfl_AutomataDef", None)
                    
                    setattr(item, "gpfl_AutomataDef", self)
                    

    @property
    def gpfl_Program4(self):
        return self.__gpfl_Program4

    @gpfl_Program4.setter
    def gpfl_Program4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_Program__gpfl_Program4", None)
        self.__gpfl_Program4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gpfl_GExpression5"):
                    opp_val = getattr(item, "gpfl_GExpression5", None)
                    
                    if opp_val == self:
                        setattr(item, "gpfl_GExpression5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gpfl_GExpression5"):
                    opp_val = getattr(item, "gpfl_GExpression5", None)
                    
                    setattr(item, "gpfl_GExpression5", self)
                    

    @property
    def gpfl_Program2(self):
        return self.__gpfl_Program2

    @gpfl_Program2.setter
    def gpfl_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_Program__gpfl_Program2", None)
        self.__gpfl_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gpfl_GExpression"):
                    opp_val = getattr(item, "gpfl_GExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "gpfl_GExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gpfl_GExpression"):
                    opp_val = getattr(item, "gpfl_GExpression", None)
                    
                    setattr(item, "gpfl_GExpression", self)
                    

class gpfl_Field:

    def __init__(self, name: str, gpfl_Field: "gpfl_GExpression" = None, gpfl_Field40: "gpfl_SendCmd" = None):
        self.name = name
        self.gpfl_Field = gpfl_Field
        self.gpfl_Field40 = gpfl_Field40
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gpfl_Field40(self):
        return self.__gpfl_Field40

    @gpfl_Field40.setter
    def gpfl_Field40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_Field__gpfl_Field40", None)
        self.__gpfl_Field40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_SendCmd39"):
                opp_val = getattr(old_value, "gpfl_SendCmd39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_SendCmd39"):
                opp_val = getattr(value, "gpfl_SendCmd39", None)
                if opp_val is None:
                    setattr(value, "gpfl_SendCmd39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gpfl_Field(self):
        return self.__gpfl_Field

    @gpfl_Field.setter
    def gpfl_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gpfl_Field__gpfl_Field", None)
        self.__gpfl_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gpfl_GExpression10"):
                opp_val = getattr(old_value, "gpfl_GExpression10", None)
                if opp_val == self:
                    setattr(old_value, "gpfl_GExpression10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gpfl_GExpression10"):
                opp_val = getattr(value, "gpfl_GExpression10", None)
                setattr(value, "gpfl_GExpression10", self)
