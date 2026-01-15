from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class iotdsl_IfBlock:

    pass
class Action:

    pass
class iotdsl_Expression(Action):

    pass
class iotdsl_Variable(Action):

    def __init__(self, name: str, iotdsl_Variable: "iotdsl_Expression" = None, iotdsl_Variable69: "iotdsl_VariableRef" = None):
        self.name = name
        self.iotdsl_Variable = iotdsl_Variable
        self.iotdsl_Variable69 = iotdsl_Variable69
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_Variable69(self):
        return self.__iotdsl_Variable69

    @iotdsl_Variable69.setter
    def iotdsl_Variable69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Variable__iotdsl_Variable69", None)
        self.__iotdsl_Variable69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_VariableRef"):
                opp_val = getattr(old_value, "iotdsl_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_VariableRef"):
                opp_val = getattr(value, "iotdsl_VariableRef", None)
                setattr(value, "iotdsl_VariableRef", self)

    @property
    def iotdsl_Variable(self):
        return self.__iotdsl_Variable

    @iotdsl_Variable.setter
    def iotdsl_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Variable__iotdsl_Variable", None)
        self.__iotdsl_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Expression"):
                opp_val = getattr(old_value, "iotdsl_Expression", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Expression"):
                opp_val = getattr(value, "iotdsl_Expression", None)
                setattr(value, "iotdsl_Expression", self)

class Expression:

    pass
class iotdsl_Or(Expression):

    pass
class iotdsl_And(Expression):

    pass
class iotdsl_MulOrDiv(Expression):

    def __init__(self, op: str, iotdsl_MulOrDiv: "iotdsl_Expression" = None, iotdsl_MulOrDiv64: "iotdsl_Expression" = None):
        self.op = op
        self.iotdsl_MulOrDiv = iotdsl_MulOrDiv
        self.iotdsl_MulOrDiv64 = iotdsl_MulOrDiv64
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def iotdsl_MulOrDiv(self):
        return self.__iotdsl_MulOrDiv

    @iotdsl_MulOrDiv.setter
    def iotdsl_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_MulOrDiv__iotdsl_MulOrDiv", None)
        self.__iotdsl_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Expression62"):
                opp_val = getattr(old_value, "iotdsl_Expression62", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Expression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Expression62"):
                opp_val = getattr(value, "iotdsl_Expression62", None)
                setattr(value, "iotdsl_Expression62", self)

    @property
    def iotdsl_MulOrDiv64(self):
        return self.__iotdsl_MulOrDiv64

    @iotdsl_MulOrDiv64.setter
    def iotdsl_MulOrDiv64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_MulOrDiv__iotdsl_MulOrDiv64", None)
        self.__iotdsl_MulOrDiv64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Expression65"):
                opp_val = getattr(old_value, "iotdsl_Expression65", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Expression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Expression65"):
                opp_val = getattr(value, "iotdsl_Expression65", None)
                setattr(value, "iotdsl_Expression65", self)

class iotdsl_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class iotdsl_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class iotdsl_Comparison(Expression):

    def __init__(self, op: str, iotdsl_Comparison: "iotdsl_Expression" = None, iotdsl_Comparison49: "iotdsl_Expression" = None):
        self.op = op
        self.iotdsl_Comparison = iotdsl_Comparison
        self.iotdsl_Comparison49 = iotdsl_Comparison49
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def iotdsl_Comparison(self):
        return self.__iotdsl_Comparison

    @iotdsl_Comparison.setter
    def iotdsl_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Comparison__iotdsl_Comparison", None)
        self.__iotdsl_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Expression47"):
                opp_val = getattr(old_value, "iotdsl_Expression47", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Expression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Expression47"):
                opp_val = getattr(value, "iotdsl_Expression47", None)
                setattr(value, "iotdsl_Expression47", self)

    @property
    def iotdsl_Comparison49(self):
        return self.__iotdsl_Comparison49

    @iotdsl_Comparison49.setter
    def iotdsl_Comparison49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Comparison__iotdsl_Comparison49", None)
        self.__iotdsl_Comparison49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Expression50"):
                opp_val = getattr(old_value, "iotdsl_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Expression50"):
                opp_val = getattr(value, "iotdsl_Expression50", None)
                setattr(value, "iotdsl_Expression50", self)

class iotdsl_Minus(Expression):

    pass
class iotdsl_Plus(Expression):

    pass
class iotdsl_Not(Expression):

    pass
class iotdsl_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class iotdsl_VariableRef(Expression):

    pass
class iotdsl_Equality(Expression):

    def __init__(self, op: str, iotdsl_Equality44: "iotdsl_Expression" = None, iotdsl_Equality: "iotdsl_Expression" = None):
        self.op = op
        self.iotdsl_Equality44 = iotdsl_Equality44
        self.iotdsl_Equality = iotdsl_Equality
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def iotdsl_Equality(self):
        return self.__iotdsl_Equality

    @iotdsl_Equality.setter
    def iotdsl_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Equality__iotdsl_Equality", None)
        self.__iotdsl_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Expression42"):
                opp_val = getattr(old_value, "iotdsl_Expression42", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Expression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Expression42"):
                opp_val = getattr(value, "iotdsl_Expression42", None)
                setattr(value, "iotdsl_Expression42", self)

    @property
    def iotdsl_Equality44(self):
        return self.__iotdsl_Equality44

    @iotdsl_Equality44.setter
    def iotdsl_Equality44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Equality__iotdsl_Equality44", None)
        self.__iotdsl_Equality44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Expression45"):
                opp_val = getattr(old_value, "iotdsl_Expression45", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Expression45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Expression45"):
                opp_val = getattr(value, "iotdsl_Expression45", None)
                setattr(value, "iotdsl_Expression45", self)

class iotdsl_IfStatement(Expression):

    pass
class iotdsl_Transition:

    def __init__(self, name: str, iotdsl_Transition: "iotdsl_Device" = None, iotdsl_Transition15: "iotdsl_Event" = None, iotdsl_Transition18: "iotdsl_State" = None):
        self.name = name
        self.iotdsl_Transition = iotdsl_Transition
        self.iotdsl_Transition15 = iotdsl_Transition15
        self.iotdsl_Transition18 = iotdsl_Transition18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_Transition15(self):
        return self.__iotdsl_Transition15

    @iotdsl_Transition15.setter
    def iotdsl_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Transition__iotdsl_Transition15", None)
        self.__iotdsl_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Event16"):
                opp_val = getattr(old_value, "iotdsl_Event16", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Event16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Event16"):
                opp_val = getattr(value, "iotdsl_Event16", None)
                setattr(value, "iotdsl_Event16", self)

    @property
    def iotdsl_Transition(self):
        return self.__iotdsl_Transition

    @iotdsl_Transition.setter
    def iotdsl_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Transition__iotdsl_Transition", None)
        self.__iotdsl_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Device11"):
                opp_val = getattr(old_value, "iotdsl_Device11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Device11"):
                opp_val = getattr(value, "iotdsl_Device11", None)
                if opp_val is None:
                    setattr(value, "iotdsl_Device11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotdsl_Transition18(self):
        return self.__iotdsl_Transition18

    @iotdsl_Transition18.setter
    def iotdsl_Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Transition__iotdsl_Transition18", None)
        self.__iotdsl_Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_State19"):
                opp_val = getattr(old_value, "iotdsl_State19", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_State19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_State19"):
                opp_val = getattr(value, "iotdsl_State19", None)
                setattr(value, "iotdsl_State19", self)

class iotdsl_Event:

    def __init__(self, name: str, iotdsl_Event: "iotdsl_Device" = None, iotdsl_Event16: "iotdsl_Transition" = None):
        self.name = name
        self.iotdsl_Event = iotdsl_Event
        self.iotdsl_Event16 = iotdsl_Event16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_Event(self):
        return self.__iotdsl_Event

    @iotdsl_Event.setter
    def iotdsl_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Event__iotdsl_Event", None)
        self.__iotdsl_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Device9"):
                opp_val = getattr(old_value, "iotdsl_Device9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Device9"):
                opp_val = getattr(value, "iotdsl_Device9", None)
                if opp_val is None:
                    setattr(value, "iotdsl_Device9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotdsl_Event16(self):
        return self.__iotdsl_Event16

    @iotdsl_Event16.setter
    def iotdsl_Event16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Event__iotdsl_Event16", None)
        self.__iotdsl_Event16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Transition15"):
                opp_val = getattr(old_value, "iotdsl_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Transition15"):
                opp_val = getattr(value, "iotdsl_Transition15", None)
                setattr(value, "iotdsl_Transition15", self)

class iotdsl_State:

    def __init__(self, name: str, iotdsl_State13: set["iotdsl_Action"] = None, iotdsl_State: "iotdsl_Device" = None, iotdsl_State19: "iotdsl_Transition" = None):
        self.name = name
        self.iotdsl_State13 = iotdsl_State13 if iotdsl_State13 is not None else set()
        self.iotdsl_State = iotdsl_State
        self.iotdsl_State19 = iotdsl_State19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_State(self):
        return self.__iotdsl_State

    @iotdsl_State.setter
    def iotdsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_State__iotdsl_State", None)
        self.__iotdsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Device7"):
                opp_val = getattr(old_value, "iotdsl_Device7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Device7"):
                opp_val = getattr(value, "iotdsl_Device7", None)
                if opp_val is None:
                    setattr(value, "iotdsl_Device7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotdsl_State13(self):
        return self.__iotdsl_State13

    @iotdsl_State13.setter
    def iotdsl_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_State__iotdsl_State13", None)
        self.__iotdsl_State13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotdsl_Action"):
                    opp_val = getattr(item, "iotdsl_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "iotdsl_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotdsl_Action"):
                    opp_val = getattr(item, "iotdsl_Action", None)
                    
                    setattr(item, "iotdsl_Action", self)
                    

    @property
    def iotdsl_State19(self):
        return self.__iotdsl_State19

    @iotdsl_State19.setter
    def iotdsl_State19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_State__iotdsl_State19", None)
        self.__iotdsl_State19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Transition18"):
                opp_val = getattr(old_value, "iotdsl_Transition18", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Transition18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Transition18"):
                opp_val = getattr(value, "iotdsl_Transition18", None)
                setattr(value, "iotdsl_Transition18", self)

class iotdsl_Attribute:

    def __init__(self, typeName: str, tag: str, value: str, iotdsl_Attribute: "iotdsl_Device" = None):
        self.typeName = typeName
        self.tag = tag
        self.value = value
        self.iotdsl_Attribute = iotdsl_Attribute
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def iotdsl_Attribute(self):
        return self.__iotdsl_Attribute

    @iotdsl_Attribute.setter
    def iotdsl_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Attribute__iotdsl_Attribute", None)
        self.__iotdsl_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Device5"):
                opp_val = getattr(old_value, "iotdsl_Device5", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Device5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Device5"):
                opp_val = getattr(value, "iotdsl_Device5", None)
                setattr(value, "iotdsl_Device5", self)

class iotdsl_Action:

    pass
class iotdsl_Device:

    def __init__(self, name: str, iotdsl_Device: "iotdsl_Iot" = None, iotdsl_Device3: "iotdsl_Device" = None, iotdsl_Device1: "iotdsl_Device" = None, iotdsl_Device5: "iotdsl_Attribute" = None, iotdsl_Device7: set["iotdsl_State"] = None, iotdsl_Device9: set["iotdsl_Event"] = None, iotdsl_Device11: set["iotdsl_Transition"] = None):
        self.name = name
        self.iotdsl_Device = iotdsl_Device
        self.iotdsl_Device3 = iotdsl_Device3
        self.iotdsl_Device1 = iotdsl_Device1
        self.iotdsl_Device5 = iotdsl_Device5
        self.iotdsl_Device7 = iotdsl_Device7 if iotdsl_Device7 is not None else set()
        self.iotdsl_Device9 = iotdsl_Device9 if iotdsl_Device9 is not None else set()
        self.iotdsl_Device11 = iotdsl_Device11 if iotdsl_Device11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iotdsl_Device1(self):
        return self.__iotdsl_Device1

    @iotdsl_Device1.setter
    def iotdsl_Device1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Device__iotdsl_Device1", None)
        self.__iotdsl_Device1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Device3"):
                opp_val = getattr(old_value, "iotdsl_Device3", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Device3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Device3"):
                opp_val = getattr(value, "iotdsl_Device3", None)
                setattr(value, "iotdsl_Device3", self)

    @property
    def iotdsl_Device9(self):
        return self.__iotdsl_Device9

    @iotdsl_Device9.setter
    def iotdsl_Device9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Device__iotdsl_Device9", None)
        self.__iotdsl_Device9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotdsl_Event"):
                    opp_val = getattr(item, "iotdsl_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "iotdsl_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotdsl_Event"):
                    opp_val = getattr(item, "iotdsl_Event", None)
                    
                    setattr(item, "iotdsl_Event", self)
                    

    @property
    def iotdsl_Device7(self):
        return self.__iotdsl_Device7

    @iotdsl_Device7.setter
    def iotdsl_Device7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Device__iotdsl_Device7", None)
        self.__iotdsl_Device7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotdsl_State"):
                    opp_val = getattr(item, "iotdsl_State", None)
                    
                    if opp_val == self:
                        setattr(item, "iotdsl_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotdsl_State"):
                    opp_val = getattr(item, "iotdsl_State", None)
                    
                    setattr(item, "iotdsl_State", self)
                    

    @property
    def iotdsl_Device11(self):
        return self.__iotdsl_Device11

    @iotdsl_Device11.setter
    def iotdsl_Device11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Device__iotdsl_Device11", None)
        self.__iotdsl_Device11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotdsl_Transition"):
                    opp_val = getattr(item, "iotdsl_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "iotdsl_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotdsl_Transition"):
                    opp_val = getattr(item, "iotdsl_Transition", None)
                    
                    setattr(item, "iotdsl_Transition", self)
                    

    @property
    def iotdsl_Device5(self):
        return self.__iotdsl_Device5

    @iotdsl_Device5.setter
    def iotdsl_Device5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Device__iotdsl_Device5", None)
        self.__iotdsl_Device5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Attribute"):
                opp_val = getattr(old_value, "iotdsl_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Attribute"):
                opp_val = getattr(value, "iotdsl_Attribute", None)
                setattr(value, "iotdsl_Attribute", self)

    @property
    def iotdsl_Device(self):
        return self.__iotdsl_Device

    @iotdsl_Device.setter
    def iotdsl_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Device__iotdsl_Device", None)
        self.__iotdsl_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Iot"):
                opp_val = getattr(old_value, "iotdsl_Iot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Iot"):
                opp_val = getattr(value, "iotdsl_Iot", None)
                if opp_val is None:
                    setattr(value, "iotdsl_Iot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotdsl_Device3(self):
        return self.__iotdsl_Device3

    @iotdsl_Device3.setter
    def iotdsl_Device3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotdsl_Device__iotdsl_Device3", None)
        self.__iotdsl_Device3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotdsl_Device1"):
                opp_val = getattr(old_value, "iotdsl_Device1", None)
                if opp_val == self:
                    setattr(old_value, "iotdsl_Device1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotdsl_Device1"):
                opp_val = getattr(value, "iotdsl_Device1", None)
                setattr(value, "iotdsl_Device1", self)

class iotdsl_Iot:

    pass