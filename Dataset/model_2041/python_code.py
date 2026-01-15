from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class StringExpression:

    pass
class urml_ConcatenateExpression(StringExpression):

    pass
class urml_Identifiable:

    def __init__(self, isBool: bool, isInt: bool, name: str, urml_Identifiable: "urml_Identifier" = None):
        self.isBool = isBool
        self.isInt = isInt
        self.name = name
        self.urml_Identifiable = urml_Identifiable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isInt(self) -> bool:
        return self.__isInt

    @isInt.setter
    def isInt(self, isInt: bool):
        self.__isInt = isInt

    @property
    def isBool(self) -> bool:
        return self.__isBool

    @isBool.setter
    def isBool(self, isBool: bool):
        self.__isBool = isBool

    @property
    def urml_Identifiable(self):
        return self.__urml_Identifiable

    @urml_Identifiable.setter
    def urml_Identifiable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Identifiable__urml_Identifiable", None)
        self.__urml_Identifiable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Identifier"):
                opp_val = getattr(old_value, "urml_Identifier", None)
                if opp_val == self:
                    setattr(old_value, "urml_Identifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Identifier"):
                opp_val = getattr(value, "urml_Identifier", None)
                setattr(value, "urml_Identifier", self)

class Literal:

    pass
class urml_BoolLiteral(Literal):

    def __init__(self, true: bool):
        self.true = true
        
    @property
    def true(self) -> bool:
        return self.__true

    @true.setter
    def true(self, true: bool):
        self.__true = true

class urml_FunctionCall(Literal):

    pass
class urml_IntLiteral(Literal):

    def __init__(self, int: int):
        self.int = int
        
    @property
    def int(self) -> int:
        return self.__int

    @int.setter
    def int(self, int: int):
        self.__int = int

class Expression:

    pass
class urml_UnaryExpression(Expression):

    pass
class urml_Plus(Expression):

    pass
class urml_Multiply(Expression):

    pass
class urml_GreaterThanOrEqual(Expression):

    pass
class urml_ConditionalOrExpression(Expression):

    pass
class urml_GreaterThan(Expression):

    pass
class urml_Divide(Expression):

    pass
class urml_LessThanOrEqual(Expression):

    pass
class urml_Minus(Expression):

    pass
class urml_NotEqual(Expression):

    pass
class urml_LessThan(Expression):

    pass
class urml_Equal(Expression):

    pass
class urml_ConditionalAndExpression(Expression):

    pass
class urml_Literal(Expression):

    pass
class urml_Identifier(Expression):

    pass
class urml_Modulo(Expression):

    pass
class urml_NotBooleanExpression(Expression):

    pass
class urml_StringExpression:

    def __init__(self, str: str, urml_StringExpression: "urml_LogStatement" = None, urml_StringExpression157: "urml_Expression" = None, urml_StringExpression168: "urml_ConcatenateExpression" = None, urml_StringExpression171: "urml_ConcatenateExpression" = None):
        self.str = str
        self.urml_StringExpression = urml_StringExpression
        self.urml_StringExpression157 = urml_StringExpression157
        self.urml_StringExpression168 = urml_StringExpression168
        self.urml_StringExpression171 = urml_StringExpression171
        
    @property
    def str(self) -> str:
        return self.__str

    @str.setter
    def str(self, str: str):
        self.__str = str

    @property
    def urml_StringExpression168(self):
        return self.__urml_StringExpression168

    @urml_StringExpression168.setter
    def urml_StringExpression168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_StringExpression__urml_StringExpression168", None)
        self.__urml_StringExpression168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_ConcatenateExpression"):
                opp_val = getattr(old_value, "urml_ConcatenateExpression", None)
                if opp_val == self:
                    setattr(old_value, "urml_ConcatenateExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_ConcatenateExpression"):
                opp_val = getattr(value, "urml_ConcatenateExpression", None)
                setattr(value, "urml_ConcatenateExpression", self)

    @property
    def urml_StringExpression171(self):
        return self.__urml_StringExpression171

    @urml_StringExpression171.setter
    def urml_StringExpression171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_StringExpression__urml_StringExpression171", None)
        self.__urml_StringExpression171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_ConcatenateExpression170"):
                opp_val = getattr(old_value, "urml_ConcatenateExpression170", None)
                if opp_val == self:
                    setattr(old_value, "urml_ConcatenateExpression170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_ConcatenateExpression170"):
                opp_val = getattr(value, "urml_ConcatenateExpression170", None)
                setattr(value, "urml_ConcatenateExpression170", self)

    @property
    def urml_StringExpression157(self):
        return self.__urml_StringExpression157

    @urml_StringExpression157.setter
    def urml_StringExpression157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_StringExpression__urml_StringExpression157", None)
        self.__urml_StringExpression157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Expression158"):
                opp_val = getattr(old_value, "urml_Expression158", None)
                if opp_val == self:
                    setattr(old_value, "urml_Expression158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Expression158"):
                opp_val = getattr(value, "urml_Expression158", None)
                setattr(value, "urml_Expression158", self)

    @property
    def urml_StringExpression(self):
        return self.__urml_StringExpression

    @urml_StringExpression.setter
    def urml_StringExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_StringExpression__urml_StringExpression", None)
        self.__urml_StringExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_LogStatement155"):
                opp_val = getattr(old_value, "urml_LogStatement155", None)
                if opp_val == self:
                    setattr(old_value, "urml_LogStatement155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_LogStatement155"):
                opp_val = getattr(value, "urml_LogStatement155", None)
                setattr(value, "urml_LogStatement155", self)

class Statement:

    pass
class urml_IfStatement(Statement):

    pass
class urml_WhileLoop(Statement):

    pass
class urml_Statement:

    pass
class StatementOperation:

    pass
class urml_Variable(Statement, StatementOperation):

    def __init__(self, assign: bool, urml_Variable: "urml_LocalVar" = None, urml_Variable121: "urml_Expression" = None):
        self.assign = assign
        self.urml_Variable = urml_Variable
        self.urml_Variable121 = urml_Variable121
        
    @property
    def assign(self) -> bool:
        return self.__assign

    @assign.setter
    def assign(self, assign: bool):
        self.__assign = assign

    @property
    def urml_Variable121(self):
        return self.__urml_Variable121

    @urml_Variable121.setter
    def urml_Variable121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Variable__urml_Variable121", None)
        self.__urml_Variable121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Expression122"):
                opp_val = getattr(old_value, "urml_Expression122", None)
                if opp_val == self:
                    setattr(old_value, "urml_Expression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Expression122"):
                opp_val = getattr(value, "urml_Expression122", None)
                setattr(value, "urml_Expression122", self)

    @property
    def urml_Variable(self):
        return self.__urml_Variable

    @urml_Variable.setter
    def urml_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Variable__urml_Variable", None)
        self.__urml_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_LocalVar119"):
                opp_val = getattr(old_value, "urml_LocalVar119", None)
                if opp_val == self:
                    setattr(old_value, "urml_LocalVar119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_LocalVar119"):
                opp_val = getattr(value, "urml_LocalVar119", None)
                setattr(value, "urml_LocalVar119", self)

class urml_NoOp(Statement, StatementOperation):

    pass
class urml_IfStatementOperation(StatementOperation):

    pass
class urml_Invoke(Statement, StatementOperation):

    pass
class urml_SendTrigger(Statement, StatementOperation):

    pass
class urml_Assignment(Statement, StatementOperation):

    pass
class urml_ReturnStatement(StatementOperation):

    pass
class urml_LogStatement(Statement, StatementOperation):

    pass
class urml_InformTimer(Statement, StatementOperation):

    pass
class urml_WhileLoopOperation(StatementOperation):

    pass
class urml_StatementOperation:

    pass
class urml_Trigger_out:

    pass
class Identifiable:

    pass
class urml_Assignable(Identifiable):

    pass
class urml_IncomingVariable(Identifiable):

    pass
class urml_Transition:

    def __init__(self, name: str, init: bool, universal: bool, urml_Transition67: "urml_State_" = None, urml_Transition70: "urml_State_" = None, urml_Transition73: "urml_Expression" = None, urml_Transition76: set["urml_Trigger_in"] = None, urml_Transition: "urml_StateMachine" = None, urml_Transition78: "urml_TimerPort" = None, urml_Transition81: "urml_ActionCode" = None):
        self.name = name
        self.init = init
        self.universal = universal
        self.urml_Transition67 = urml_Transition67
        self.urml_Transition70 = urml_Transition70
        self.urml_Transition73 = urml_Transition73
        self.urml_Transition76 = urml_Transition76 if urml_Transition76 is not None else set()
        self.urml_Transition = urml_Transition
        self.urml_Transition78 = urml_Transition78
        self.urml_Transition81 = urml_Transition81
        
    @property
    def universal(self) -> bool:
        return self.__universal

    @universal.setter
    def universal(self, universal: bool):
        self.__universal = universal

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def init(self) -> bool:
        return self.__init

    @init.setter
    def init(self, init: bool):
        self.__init = init

    @property
    def urml_Transition70(self):
        return self.__urml_Transition70

    @urml_Transition70.setter
    def urml_Transition70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Transition__urml_Transition70", None)
        self.__urml_Transition70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_State_71"):
                opp_val = getattr(old_value, "urml_State_71", None)
                if opp_val == self:
                    setattr(old_value, "urml_State_71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_State_71"):
                opp_val = getattr(value, "urml_State_71", None)
                setattr(value, "urml_State_71", self)

    @property
    def urml_Transition73(self):
        return self.__urml_Transition73

    @urml_Transition73.setter
    def urml_Transition73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Transition__urml_Transition73", None)
        self.__urml_Transition73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Expression74"):
                opp_val = getattr(old_value, "urml_Expression74", None)
                if opp_val == self:
                    setattr(old_value, "urml_Expression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Expression74"):
                opp_val = getattr(value, "urml_Expression74", None)
                setattr(value, "urml_Expression74", self)

    @property
    def urml_Transition78(self):
        return self.__urml_Transition78

    @urml_Transition78.setter
    def urml_Transition78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Transition__urml_Transition78", None)
        self.__urml_Transition78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_TimerPort79"):
                opp_val = getattr(old_value, "urml_TimerPort79", None)
                if opp_val == self:
                    setattr(old_value, "urml_TimerPort79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_TimerPort79"):
                opp_val = getattr(value, "urml_TimerPort79", None)
                setattr(value, "urml_TimerPort79", self)

    @property
    def urml_Transition67(self):
        return self.__urml_Transition67

    @urml_Transition67.setter
    def urml_Transition67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Transition__urml_Transition67", None)
        self.__urml_Transition67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_State_68"):
                opp_val = getattr(old_value, "urml_State_68", None)
                if opp_val == self:
                    setattr(old_value, "urml_State_68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_State_68"):
                opp_val = getattr(value, "urml_State_68", None)
                setattr(value, "urml_State_68", self)

    @property
    def urml_Transition76(self):
        return self.__urml_Transition76

    @urml_Transition76.setter
    def urml_Transition76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Transition__urml_Transition76", None)
        self.__urml_Transition76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_Trigger_in"):
                    opp_val = getattr(item, "urml_Trigger_in", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_Trigger_in", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_Trigger_in"):
                    opp_val = getattr(item, "urml_Trigger_in", None)
                    
                    setattr(item, "urml_Trigger_in", self)
                    

    @property
    def urml_Transition81(self):
        return self.__urml_Transition81

    @urml_Transition81.setter
    def urml_Transition81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Transition__urml_Transition81", None)
        self.__urml_Transition81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_ActionCode82"):
                opp_val = getattr(old_value, "urml_ActionCode82", None)
                if opp_val == self:
                    setattr(old_value, "urml_ActionCode82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_ActionCode82"):
                opp_val = getattr(value, "urml_ActionCode82", None)
                setattr(value, "urml_ActionCode82", self)

    @property
    def urml_Transition(self):
        return self.__urml_Transition

    @urml_Transition.setter
    def urml_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Transition__urml_Transition", None)
        self.__urml_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_StateMachine57"):
                opp_val = getattr(old_value, "urml_StateMachine57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_StateMachine57"):
                opp_val = getattr(value, "urml_StateMachine57", None)
                if opp_val is None:
                    setattr(value, "urml_StateMachine57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class urml_State_:

    def __init__(self, final: bool, name: str, urml_State_59: "urml_ActionCode" = None, urml_State_61: "urml_ActionCode" = None, urml_State_64: "urml_StateMachine" = None, urml_State_68: "urml_Transition" = None, urml_State_71: "urml_Transition" = None, urml_State_: "urml_StateMachine" = None):
        self.final = final
        self.name = name
        self.urml_State_59 = urml_State_59
        self.urml_State_61 = urml_State_61
        self.urml_State_64 = urml_State_64
        self.urml_State_68 = urml_State_68
        self.urml_State_71 = urml_State_71
        self.urml_State_ = urml_State_
        
    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def urml_State_61(self):
        return self.__urml_State_61

    @urml_State_61.setter
    def urml_State_61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_State___urml_State_61", None)
        self.__urml_State_61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_ActionCode62"):
                opp_val = getattr(old_value, "urml_ActionCode62", None)
                if opp_val == self:
                    setattr(old_value, "urml_ActionCode62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_ActionCode62"):
                opp_val = getattr(value, "urml_ActionCode62", None)
                setattr(value, "urml_ActionCode62", self)

    @property
    def urml_State_68(self):
        return self.__urml_State_68

    @urml_State_68.setter
    def urml_State_68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_State___urml_State_68", None)
        self.__urml_State_68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Transition67"):
                opp_val = getattr(old_value, "urml_Transition67", None)
                if opp_val == self:
                    setattr(old_value, "urml_Transition67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Transition67"):
                opp_val = getattr(value, "urml_Transition67", None)
                setattr(value, "urml_Transition67", self)

    @property
    def urml_State_59(self):
        return self.__urml_State_59

    @urml_State_59.setter
    def urml_State_59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_State___urml_State_59", None)
        self.__urml_State_59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_ActionCode"):
                opp_val = getattr(old_value, "urml_ActionCode", None)
                if opp_val == self:
                    setattr(old_value, "urml_ActionCode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_ActionCode"):
                opp_val = getattr(value, "urml_ActionCode", None)
                setattr(value, "urml_ActionCode", self)

    @property
    def urml_State_(self):
        return self.__urml_State_

    @urml_State_.setter
    def urml_State_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_State___urml_State_", None)
        self.__urml_State_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_StateMachine55"):
                opp_val = getattr(old_value, "urml_StateMachine55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_StateMachine55"):
                opp_val = getattr(value, "urml_StateMachine55", None)
                if opp_val is None:
                    setattr(value, "urml_StateMachine55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def urml_State_64(self):
        return self.__urml_State_64

    @urml_State_64.setter
    def urml_State_64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_State___urml_State_64", None)
        self.__urml_State_64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_StateMachine65"):
                opp_val = getattr(old_value, "urml_StateMachine65", None)
                if opp_val == self:
                    setattr(old_value, "urml_StateMachine65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_StateMachine65"):
                opp_val = getattr(value, "urml_StateMachine65", None)
                setattr(value, "urml_StateMachine65", self)

    @property
    def urml_State_71(self):
        return self.__urml_State_71

    @urml_State_71.setter
    def urml_State_71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_State___urml_State_71", None)
        self.__urml_State_71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Transition70"):
                opp_val = getattr(old_value, "urml_Transition70", None)
                if opp_val == self:
                    setattr(old_value, "urml_Transition70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Transition70"):
                opp_val = getattr(value, "urml_Transition70", None)
                setattr(value, "urml_Transition70", self)

class urml_Trigger_in:

    pass
class urml_ActionCode:

    pass
class urml_LogPort:

    def __init__(self, name: str, urml_LogPort: "urml_Capsule" = None, urml_LogPort153: "urml_LogStatement" = None):
        self.name = name
        self.urml_LogPort = urml_LogPort
        self.urml_LogPort153 = urml_LogPort153
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def urml_LogPort(self):
        return self.__urml_LogPort

    @urml_LogPort.setter
    def urml_LogPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_LogPort__urml_LogPort", None)
        self.__urml_LogPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Capsule19"):
                opp_val = getattr(old_value, "urml_Capsule19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Capsule19"):
                opp_val = getattr(value, "urml_Capsule19", None)
                if opp_val is None:
                    setattr(value, "urml_Capsule19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def urml_LogPort153(self):
        return self.__urml_LogPort153

    @urml_LogPort153.setter
    def urml_LogPort153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_LogPort__urml_LogPort153", None)
        self.__urml_LogPort153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_LogStatement"):
                opp_val = getattr(old_value, "urml_LogStatement", None)
                if opp_val == self:
                    setattr(old_value, "urml_LogStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_LogStatement"):
                opp_val = getattr(value, "urml_LogStatement", None)
                setattr(value, "urml_LogStatement", self)

class urml_TimerPort:

    def __init__(self, name: str, urml_TimerPort: "urml_Capsule" = None, urml_TimerPort79: "urml_Transition" = None, urml_TimerPort126: "urml_InformTimer" = None):
        self.name = name
        self.urml_TimerPort = urml_TimerPort
        self.urml_TimerPort79 = urml_TimerPort79
        self.urml_TimerPort126 = urml_TimerPort126
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def urml_TimerPort79(self):
        return self.__urml_TimerPort79

    @urml_TimerPort79.setter
    def urml_TimerPort79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_TimerPort__urml_TimerPort79", None)
        self.__urml_TimerPort79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Transition78"):
                opp_val = getattr(old_value, "urml_Transition78", None)
                if opp_val == self:
                    setattr(old_value, "urml_Transition78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Transition78"):
                opp_val = getattr(value, "urml_Transition78", None)
                setattr(value, "urml_Transition78", self)

    @property
    def urml_TimerPort126(self):
        return self.__urml_TimerPort126

    @urml_TimerPort126.setter
    def urml_TimerPort126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_TimerPort__urml_TimerPort126", None)
        self.__urml_TimerPort126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_InformTimer"):
                opp_val = getattr(old_value, "urml_InformTimer", None)
                if opp_val == self:
                    setattr(old_value, "urml_InformTimer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_InformTimer"):
                opp_val = getattr(value, "urml_InformTimer", None)
                setattr(value, "urml_InformTimer", self)

    @property
    def urml_TimerPort(self):
        return self.__urml_TimerPort

    @urml_TimerPort.setter
    def urml_TimerPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_TimerPort__urml_TimerPort", None)
        self.__urml_TimerPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Capsule17"):
                opp_val = getattr(old_value, "urml_Capsule17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Capsule17"):
                opp_val = getattr(value, "urml_Capsule17", None)
                if opp_val is None:
                    setattr(value, "urml_Capsule17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class urml_OperationCode:

    pass
class urml_StateMachine:

    pass
class urml_Operation:

    def __init__(self, isBool: bool, isInt: bool, isVoid: bool, name: str, urml_Operation: "urml_Capsule" = None, urml_Operation32: set["urml_LocalVar"] = None, urml_Operation35: "urml_OperationCode" = None, urml_Operation131: "urml_Invoke" = None, urml_Operation163: "urml_FunctionCall" = None):
        self.isBool = isBool
        self.isInt = isInt
        self.isVoid = isVoid
        self.name = name
        self.urml_Operation = urml_Operation
        self.urml_Operation32 = urml_Operation32 if urml_Operation32 is not None else set()
        self.urml_Operation35 = urml_Operation35
        self.urml_Operation131 = urml_Operation131
        self.urml_Operation163 = urml_Operation163
        
    @property
    def isBool(self) -> bool:
        return self.__isBool

    @isBool.setter
    def isBool(self, isBool: bool):
        self.__isBool = isBool

    @property
    def isVoid(self) -> bool:
        return self.__isVoid

    @isVoid.setter
    def isVoid(self, isVoid: bool):
        self.__isVoid = isVoid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isInt(self) -> bool:
        return self.__isInt

    @isInt.setter
    def isInt(self, isInt: bool):
        self.__isInt = isInt

    @property
    def urml_Operation(self):
        return self.__urml_Operation

    @urml_Operation.setter
    def urml_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Operation__urml_Operation", None)
        self.__urml_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Capsule28"):
                opp_val = getattr(old_value, "urml_Capsule28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Capsule28"):
                opp_val = getattr(value, "urml_Capsule28", None)
                if opp_val is None:
                    setattr(value, "urml_Capsule28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def urml_Operation131(self):
        return self.__urml_Operation131

    @urml_Operation131.setter
    def urml_Operation131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Operation__urml_Operation131", None)
        self.__urml_Operation131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Invoke"):
                opp_val = getattr(old_value, "urml_Invoke", None)
                if opp_val == self:
                    setattr(old_value, "urml_Invoke", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Invoke"):
                opp_val = getattr(value, "urml_Invoke", None)
                setattr(value, "urml_Invoke", self)

    @property
    def urml_Operation35(self):
        return self.__urml_Operation35

    @urml_Operation35.setter
    def urml_Operation35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Operation__urml_Operation35", None)
        self.__urml_Operation35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_OperationCode"):
                opp_val = getattr(old_value, "urml_OperationCode", None)
                if opp_val == self:
                    setattr(old_value, "urml_OperationCode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_OperationCode"):
                opp_val = getattr(value, "urml_OperationCode", None)
                setattr(value, "urml_OperationCode", self)

    @property
    def urml_Operation32(self):
        return self.__urml_Operation32

    @urml_Operation32.setter
    def urml_Operation32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Operation__urml_Operation32", None)
        self.__urml_Operation32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_LocalVar33"):
                    opp_val = getattr(item, "urml_LocalVar33", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_LocalVar33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_LocalVar33"):
                    opp_val = getattr(item, "urml_LocalVar33", None)
                    
                    setattr(item, "urml_LocalVar33", self)
                    

    @property
    def urml_Operation163(self):
        return self.__urml_Operation163

    @urml_Operation163.setter
    def urml_Operation163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Operation__urml_Operation163", None)
        self.__urml_Operation163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_FunctionCall"):
                opp_val = getattr(old_value, "urml_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "urml_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_FunctionCall"):
                opp_val = getattr(value, "urml_FunctionCall", None)
                setattr(value, "urml_FunctionCall", self)

class urml_Connector:

    pass
class urml_CapsuleInst:

    def __init__(self, name: str, urml_CapsuleInst: "urml_Capsule" = None, urml_CapsuleInst41: "urml_Connector" = None, urml_CapsuleInst47: "urml_Connector" = None, urml_CapsuleInst52: "urml_Capsule" = None):
        self.name = name
        self.urml_CapsuleInst = urml_CapsuleInst
        self.urml_CapsuleInst41 = urml_CapsuleInst41
        self.urml_CapsuleInst47 = urml_CapsuleInst47
        self.urml_CapsuleInst52 = urml_CapsuleInst52
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def urml_CapsuleInst(self):
        return self.__urml_CapsuleInst

    @urml_CapsuleInst.setter
    def urml_CapsuleInst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_CapsuleInst__urml_CapsuleInst", None)
        self.__urml_CapsuleInst = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Capsule24"):
                opp_val = getattr(old_value, "urml_Capsule24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Capsule24"):
                opp_val = getattr(value, "urml_Capsule24", None)
                if opp_val is None:
                    setattr(value, "urml_Capsule24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def urml_CapsuleInst41(self):
        return self.__urml_CapsuleInst41

    @urml_CapsuleInst41.setter
    def urml_CapsuleInst41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_CapsuleInst__urml_CapsuleInst41", None)
        self.__urml_CapsuleInst41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Connector40"):
                opp_val = getattr(old_value, "urml_Connector40", None)
                if opp_val == self:
                    setattr(old_value, "urml_Connector40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Connector40"):
                opp_val = getattr(value, "urml_Connector40", None)
                setattr(value, "urml_Connector40", self)

    @property
    def urml_CapsuleInst47(self):
        return self.__urml_CapsuleInst47

    @urml_CapsuleInst47.setter
    def urml_CapsuleInst47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_CapsuleInst__urml_CapsuleInst47", None)
        self.__urml_CapsuleInst47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Connector46"):
                opp_val = getattr(old_value, "urml_Connector46", None)
                if opp_val == self:
                    setattr(old_value, "urml_Connector46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Connector46"):
                opp_val = getattr(value, "urml_Connector46", None)
                setattr(value, "urml_Connector46", self)

    @property
    def urml_CapsuleInst52(self):
        return self.__urml_CapsuleInst52

    @urml_CapsuleInst52.setter
    def urml_CapsuleInst52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_CapsuleInst__urml_CapsuleInst52", None)
        self.__urml_CapsuleInst52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Capsule53"):
                opp_val = getattr(old_value, "urml_Capsule53", None)
                if opp_val == self:
                    setattr(old_value, "urml_Capsule53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Capsule53"):
                opp_val = getattr(value, "urml_Capsule53", None)
                setattr(value, "urml_Capsule53", self)

class Assignable:

    pass
class urml_LocalVar(Assignable):

    pass
class urml_Protocol:

    def __init__(self, name: str, urml_Protocol5: set["urml_Signal"] = None, urml_Protocol7: set["urml_Signal"] = None, urml_Protocol: "urml_Model" = None, urml_Protocol38: "urml_Port" = None):
        self.name = name
        self.urml_Protocol5 = urml_Protocol5 if urml_Protocol5 is not None else set()
        self.urml_Protocol7 = urml_Protocol7 if urml_Protocol7 is not None else set()
        self.urml_Protocol = urml_Protocol
        self.urml_Protocol38 = urml_Protocol38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def urml_Protocol38(self):
        return self.__urml_Protocol38

    @urml_Protocol38.setter
    def urml_Protocol38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Protocol__urml_Protocol38", None)
        self.__urml_Protocol38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Port37"):
                opp_val = getattr(old_value, "urml_Port37", None)
                if opp_val == self:
                    setattr(old_value, "urml_Port37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Port37"):
                opp_val = getattr(value, "urml_Port37", None)
                setattr(value, "urml_Port37", self)

    @property
    def urml_Protocol7(self):
        return self.__urml_Protocol7

    @urml_Protocol7.setter
    def urml_Protocol7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Protocol__urml_Protocol7", None)
        self.__urml_Protocol7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_Signal8"):
                    opp_val = getattr(item, "urml_Signal8", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_Signal8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_Signal8"):
                    opp_val = getattr(item, "urml_Signal8", None)
                    
                    setattr(item, "urml_Signal8", self)
                    

    @property
    def urml_Protocol5(self):
        return self.__urml_Protocol5

    @urml_Protocol5.setter
    def urml_Protocol5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Protocol__urml_Protocol5", None)
        self.__urml_Protocol5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_Signal"):
                    opp_val = getattr(item, "urml_Signal", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_Signal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_Signal"):
                    opp_val = getattr(item, "urml_Signal", None)
                    
                    setattr(item, "urml_Signal", self)
                    

    @property
    def urml_Protocol(self):
        return self.__urml_Protocol

    @urml_Protocol.setter
    def urml_Protocol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Protocol__urml_Protocol", None)
        self.__urml_Protocol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Model2"):
                opp_val = getattr(old_value, "urml_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Model2"):
                opp_val = getattr(value, "urml_Model2", None)
                if opp_val is None:
                    setattr(value, "urml_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class urml_Port:

    def __init__(self, conjugated: bool, name: str, urml_Port: "urml_Capsule" = None, urml_Port15: "urml_Capsule" = None, urml_Port37: "urml_Protocol" = None, urml_Port44: "urml_Connector" = None, urml_Port50: "urml_Connector" = None, urml_Port85: "urml_Trigger_in" = None, urml_Port92: "urml_Trigger_out" = None):
        self.conjugated = conjugated
        self.name = name
        self.urml_Port = urml_Port
        self.urml_Port15 = urml_Port15
        self.urml_Port37 = urml_Port37
        self.urml_Port44 = urml_Port44
        self.urml_Port50 = urml_Port50
        self.urml_Port85 = urml_Port85
        self.urml_Port92 = urml_Port92
        
    @property
    def conjugated(self) -> bool:
        return self.__conjugated

    @conjugated.setter
    def conjugated(self, conjugated: bool):
        self.__conjugated = conjugated

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def urml_Port50(self):
        return self.__urml_Port50

    @urml_Port50.setter
    def urml_Port50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Port__urml_Port50", None)
        self.__urml_Port50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Connector49"):
                opp_val = getattr(old_value, "urml_Connector49", None)
                if opp_val == self:
                    setattr(old_value, "urml_Connector49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Connector49"):
                opp_val = getattr(value, "urml_Connector49", None)
                setattr(value, "urml_Connector49", self)

    @property
    def urml_Port85(self):
        return self.__urml_Port85

    @urml_Port85.setter
    def urml_Port85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Port__urml_Port85", None)
        self.__urml_Port85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Trigger_in84"):
                opp_val = getattr(old_value, "urml_Trigger_in84", None)
                if opp_val == self:
                    setattr(old_value, "urml_Trigger_in84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Trigger_in84"):
                opp_val = getattr(value, "urml_Trigger_in84", None)
                setattr(value, "urml_Trigger_in84", self)

    @property
    def urml_Port15(self):
        return self.__urml_Port15

    @urml_Port15.setter
    def urml_Port15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Port__urml_Port15", None)
        self.__urml_Port15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Capsule14"):
                opp_val = getattr(old_value, "urml_Capsule14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Capsule14"):
                opp_val = getattr(value, "urml_Capsule14", None)
                if opp_val is None:
                    setattr(value, "urml_Capsule14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def urml_Port37(self):
        return self.__urml_Port37

    @urml_Port37.setter
    def urml_Port37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Port__urml_Port37", None)
        self.__urml_Port37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Protocol38"):
                opp_val = getattr(old_value, "urml_Protocol38", None)
                if opp_val == self:
                    setattr(old_value, "urml_Protocol38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Protocol38"):
                opp_val = getattr(value, "urml_Protocol38", None)
                setattr(value, "urml_Protocol38", self)

    @property
    def urml_Port(self):
        return self.__urml_Port

    @urml_Port.setter
    def urml_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Port__urml_Port", None)
        self.__urml_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Capsule12"):
                opp_val = getattr(old_value, "urml_Capsule12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Capsule12"):
                opp_val = getattr(value, "urml_Capsule12", None)
                if opp_val is None:
                    setattr(value, "urml_Capsule12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def urml_Port44(self):
        return self.__urml_Port44

    @urml_Port44.setter
    def urml_Port44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Port__urml_Port44", None)
        self.__urml_Port44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Connector43"):
                opp_val = getattr(old_value, "urml_Connector43", None)
                if opp_val == self:
                    setattr(old_value, "urml_Connector43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Connector43"):
                opp_val = getattr(value, "urml_Connector43", None)
                setattr(value, "urml_Connector43", self)

    @property
    def urml_Port92(self):
        return self.__urml_Port92

    @urml_Port92.setter
    def urml_Port92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Port__urml_Port92", None)
        self.__urml_Port92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Trigger_out"):
                opp_val = getattr(old_value, "urml_Trigger_out", None)
                if opp_val == self:
                    setattr(old_value, "urml_Trigger_out", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Trigger_out"):
                opp_val = getattr(value, "urml_Trigger_out", None)
                setattr(value, "urml_Trigger_out", self)

class urml_Signal:

    def __init__(self, name: str, urml_Signal: "urml_Protocol" = None, urml_Signal8: "urml_Protocol" = None, urml_Signal10: set["urml_LocalVar"] = None, urml_Signal88: "urml_Trigger_in" = None, urml_Signal95: "urml_Trigger_out" = None):
        self.name = name
        self.urml_Signal = urml_Signal
        self.urml_Signal8 = urml_Signal8
        self.urml_Signal10 = urml_Signal10 if urml_Signal10 is not None else set()
        self.urml_Signal88 = urml_Signal88
        self.urml_Signal95 = urml_Signal95
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def urml_Signal95(self):
        return self.__urml_Signal95

    @urml_Signal95.setter
    def urml_Signal95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Signal__urml_Signal95", None)
        self.__urml_Signal95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Trigger_out94"):
                opp_val = getattr(old_value, "urml_Trigger_out94", None)
                if opp_val == self:
                    setattr(old_value, "urml_Trigger_out94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Trigger_out94"):
                opp_val = getattr(value, "urml_Trigger_out94", None)
                setattr(value, "urml_Trigger_out94", self)

    @property
    def urml_Signal(self):
        return self.__urml_Signal

    @urml_Signal.setter
    def urml_Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Signal__urml_Signal", None)
        self.__urml_Signal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Protocol5"):
                opp_val = getattr(old_value, "urml_Protocol5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Protocol5"):
                opp_val = getattr(value, "urml_Protocol5", None)
                if opp_val is None:
                    setattr(value, "urml_Protocol5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def urml_Signal8(self):
        return self.__urml_Signal8

    @urml_Signal8.setter
    def urml_Signal8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Signal__urml_Signal8", None)
        self.__urml_Signal8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Protocol7"):
                opp_val = getattr(old_value, "urml_Protocol7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Protocol7"):
                opp_val = getattr(value, "urml_Protocol7", None)
                if opp_val is None:
                    setattr(value, "urml_Protocol7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def urml_Signal10(self):
        return self.__urml_Signal10

    @urml_Signal10.setter
    def urml_Signal10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Signal__urml_Signal10", None)
        self.__urml_Signal10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_LocalVar"):
                    opp_val = getattr(item, "urml_LocalVar", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_LocalVar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_LocalVar"):
                    opp_val = getattr(item, "urml_LocalVar", None)
                    
                    setattr(item, "urml_LocalVar", self)
                    

    @property
    def urml_Signal88(self):
        return self.__urml_Signal88

    @urml_Signal88.setter
    def urml_Signal88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Signal__urml_Signal88", None)
        self.__urml_Signal88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Trigger_in87"):
                opp_val = getattr(old_value, "urml_Trigger_in87", None)
                if opp_val == self:
                    setattr(old_value, "urml_Trigger_in87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Trigger_in87"):
                opp_val = getattr(value, "urml_Trigger_in87", None)
                setattr(value, "urml_Trigger_in87", self)

class urml_Expression:

    pass
class urml_Attribute(Assignable):

    pass
class urml_Capsule:

    def __init__(self, root: bool, name: str, urml_Capsule: "urml_Model" = None, urml_Capsule12: set["urml_Port"] = None, urml_Capsule14: set["urml_Port"] = None, urml_Capsule21: set["urml_Attribute"] = None, urml_Capsule24: set["urml_CapsuleInst"] = None, urml_Capsule26: set["urml_Connector"] = None, urml_Capsule28: set["urml_Operation"] = None, urml_Capsule30: set["urml_StateMachine"] = None, urml_Capsule17: set["urml_TimerPort"] = None, urml_Capsule19: set["urml_LogPort"] = None, urml_Capsule53: "urml_CapsuleInst" = None):
        self.root = root
        self.name = name
        self.urml_Capsule = urml_Capsule
        self.urml_Capsule12 = urml_Capsule12 if urml_Capsule12 is not None else set()
        self.urml_Capsule14 = urml_Capsule14 if urml_Capsule14 is not None else set()
        self.urml_Capsule21 = urml_Capsule21 if urml_Capsule21 is not None else set()
        self.urml_Capsule24 = urml_Capsule24 if urml_Capsule24 is not None else set()
        self.urml_Capsule26 = urml_Capsule26 if urml_Capsule26 is not None else set()
        self.urml_Capsule28 = urml_Capsule28 if urml_Capsule28 is not None else set()
        self.urml_Capsule30 = urml_Capsule30 if urml_Capsule30 is not None else set()
        self.urml_Capsule17 = urml_Capsule17 if urml_Capsule17 is not None else set()
        self.urml_Capsule19 = urml_Capsule19 if urml_Capsule19 is not None else set()
        self.urml_Capsule53 = urml_Capsule53
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def root(self) -> bool:
        return self.__root

    @root.setter
    def root(self, root: bool):
        self.__root = root

    @property
    def urml_Capsule17(self):
        return self.__urml_Capsule17

    @urml_Capsule17.setter
    def urml_Capsule17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Capsule__urml_Capsule17", None)
        self.__urml_Capsule17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_TimerPort"):
                    opp_val = getattr(item, "urml_TimerPort", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_TimerPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_TimerPort"):
                    opp_val = getattr(item, "urml_TimerPort", None)
                    
                    setattr(item, "urml_TimerPort", self)
                    

    @property
    def urml_Capsule21(self):
        return self.__urml_Capsule21

    @urml_Capsule21.setter
    def urml_Capsule21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Capsule__urml_Capsule21", None)
        self.__urml_Capsule21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_Attribute22"):
                    opp_val = getattr(item, "urml_Attribute22", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_Attribute22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_Attribute22"):
                    opp_val = getattr(item, "urml_Attribute22", None)
                    
                    setattr(item, "urml_Attribute22", self)
                    

    @property
    def urml_Capsule24(self):
        return self.__urml_Capsule24

    @urml_Capsule24.setter
    def urml_Capsule24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Capsule__urml_Capsule24", None)
        self.__urml_Capsule24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_CapsuleInst"):
                    opp_val = getattr(item, "urml_CapsuleInst", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_CapsuleInst", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_CapsuleInst"):
                    opp_val = getattr(item, "urml_CapsuleInst", None)
                    
                    setattr(item, "urml_CapsuleInst", self)
                    

    @property
    def urml_Capsule53(self):
        return self.__urml_Capsule53

    @urml_Capsule53.setter
    def urml_Capsule53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Capsule__urml_Capsule53", None)
        self.__urml_Capsule53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_CapsuleInst52"):
                opp_val = getattr(old_value, "urml_CapsuleInst52", None)
                if opp_val == self:
                    setattr(old_value, "urml_CapsuleInst52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_CapsuleInst52"):
                opp_val = getattr(value, "urml_CapsuleInst52", None)
                setattr(value, "urml_CapsuleInst52", self)

    @property
    def urml_Capsule19(self):
        return self.__urml_Capsule19

    @urml_Capsule19.setter
    def urml_Capsule19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Capsule__urml_Capsule19", None)
        self.__urml_Capsule19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_LogPort"):
                    opp_val = getattr(item, "urml_LogPort", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_LogPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_LogPort"):
                    opp_val = getattr(item, "urml_LogPort", None)
                    
                    setattr(item, "urml_LogPort", self)
                    

    @property
    def urml_Capsule14(self):
        return self.__urml_Capsule14

    @urml_Capsule14.setter
    def urml_Capsule14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Capsule__urml_Capsule14", None)
        self.__urml_Capsule14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_Port15"):
                    opp_val = getattr(item, "urml_Port15", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_Port15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_Port15"):
                    opp_val = getattr(item, "urml_Port15", None)
                    
                    setattr(item, "urml_Port15", self)
                    

    @property
    def urml_Capsule30(self):
        return self.__urml_Capsule30

    @urml_Capsule30.setter
    def urml_Capsule30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Capsule__urml_Capsule30", None)
        self.__urml_Capsule30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_StateMachine"):
                    opp_val = getattr(item, "urml_StateMachine", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_StateMachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_StateMachine"):
                    opp_val = getattr(item, "urml_StateMachine", None)
                    
                    setattr(item, "urml_StateMachine", self)
                    

    @property
    def urml_Capsule26(self):
        return self.__urml_Capsule26

    @urml_Capsule26.setter
    def urml_Capsule26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Capsule__urml_Capsule26", None)
        self.__urml_Capsule26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_Connector"):
                    opp_val = getattr(item, "urml_Connector", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_Connector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_Connector"):
                    opp_val = getattr(item, "urml_Connector", None)
                    
                    setattr(item, "urml_Connector", self)
                    

    @property
    def urml_Capsule28(self):
        return self.__urml_Capsule28

    @urml_Capsule28.setter
    def urml_Capsule28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Capsule__urml_Capsule28", None)
        self.__urml_Capsule28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_Operation"):
                    opp_val = getattr(item, "urml_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_Operation"):
                    opp_val = getattr(item, "urml_Operation", None)
                    
                    setattr(item, "urml_Operation", self)
                    

    @property
    def urml_Capsule(self):
        return self.__urml_Capsule

    @urml_Capsule.setter
    def urml_Capsule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Capsule__urml_Capsule", None)
        self.__urml_Capsule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "urml_Model"):
                opp_val = getattr(old_value, "urml_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "urml_Model"):
                opp_val = getattr(value, "urml_Model", None)
                if opp_val is None:
                    setattr(value, "urml_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def urml_Capsule12(self):
        return self.__urml_Capsule12

    @urml_Capsule12.setter
    def urml_Capsule12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Capsule__urml_Capsule12", None)
        self.__urml_Capsule12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_Port"):
                    opp_val = getattr(item, "urml_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_Port"):
                    opp_val = getattr(item, "urml_Port", None)
                    
                    setattr(item, "urml_Port", self)
                    

class urml_Model:

    def __init__(self, name: str, urml_Model: set["urml_Capsule"] = None, urml_Model2: set["urml_Protocol"] = None):
        self.name = name
        self.urml_Model = urml_Model if urml_Model is not None else set()
        self.urml_Model2 = urml_Model2 if urml_Model2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def urml_Model2(self):
        return self.__urml_Model2

    @urml_Model2.setter
    def urml_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Model__urml_Model2", None)
        self.__urml_Model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_Protocol"):
                    opp_val = getattr(item, "urml_Protocol", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_Protocol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_Protocol"):
                    opp_val = getattr(item, "urml_Protocol", None)
                    
                    setattr(item, "urml_Protocol", self)
                    

    @property
    def urml_Model(self):
        return self.__urml_Model

    @urml_Model.setter
    def urml_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_urml_Model__urml_Model", None)
        self.__urml_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "urml_Capsule"):
                    opp_val = getattr(item, "urml_Capsule", None)
                    
                    if opp_val == self:
                        setattr(item, "urml_Capsule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "urml_Capsule"):
                    opp_val = getattr(item, "urml_Capsule", None)
                    
                    setattr(item, "urml_Capsule", self)
                    
