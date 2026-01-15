from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ActionType:

    pass
class co2_IntActionType(ActionType):

    pass
class co2_UnitActionType(ActionType):

    pass
class co2_StringActionType(ActionType):

    pass
class Type:

    pass
class co2_BooleanType(Type):

    pass
class co2_SessionType(Type):

    pass
class co2_StringType(Type):

    pass
class co2_IntType(Type):

    pass
class Placeholder:

    pass
class co2_StringPlaceholder(Placeholder):

    pass
class co2_BoolPlaceholder(Placeholder):

    pass
class co2_IntPlaceholder(Placeholder):

    pass
class Contract:

    pass
class co2_ContractReference(Contract):

    pass
class co2_EmptyContract(Contract):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Action:

    pass
class co2_ActionType:

    def __init__(self, value: str, co2_ActionType: "co2_Action" = None):
        self.value = value
        self.co2_ActionType = co2_ActionType
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def co2_ActionType(self):
        return self.__co2_ActionType

    @co2_ActionType.setter
    def co2_ActionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_ActionType__co2_ActionType", None)
        self.__co2_ActionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Action"):
                opp_val = getattr(old_value, "co2_Action", None)
                if opp_val == self:
                    setattr(old_value, "co2_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Action"):
                opp_val = getattr(value, "co2_Action", None)
                setattr(value, "co2_Action", self)

class co2_Action:

    def __init__(self, name: str, co2_Action: "co2_ActionType" = None, co2_Action139: "co2_Contract" = None):
        self.name = name
        self.co2_Action = co2_Action
        self.co2_Action139 = co2_Action139
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def co2_Action139(self):
        return self.__co2_Action139

    @co2_Action139.setter
    def co2_Action139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_Action__co2_Action139", None)
        self.__co2_Action139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Contract140"):
                opp_val = getattr(old_value, "co2_Contract140", None)
                if opp_val == self:
                    setattr(old_value, "co2_Contract140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Contract140"):
                opp_val = getattr(value, "co2_Contract140", None)
                setattr(value, "co2_Contract140", self)

    @property
    def co2_Action(self):
        return self.__co2_Action

    @co2_Action.setter
    def co2_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_Action__co2_Action", None)
        self.__co2_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_ActionType"):
                opp_val = getattr(old_value, "co2_ActionType", None)
                if opp_val == self:
                    setattr(old_value, "co2_ActionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_ActionType"):
                opp_val = getattr(value, "co2_ActionType", None)
                setattr(value, "co2_ActionType", self)

class co2_ExtSum(Contract):

    pass
class co2_IntSum(Contract):

    pass
class VariableDeclaration:

    pass
class co2_Type:

    def __init__(self, value: str, co2_Type: "co2_Placeholder" = None, co2_Type123: "co2_Variable" = None):
        self.value = value
        self.co2_Type = co2_Type
        self.co2_Type123 = co2_Type123
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def co2_Type123(self):
        return self.__co2_Type123

    @co2_Type123.setter
    def co2_Type123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_Type__co2_Type123", None)
        self.__co2_Type123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Variable122"):
                opp_val = getattr(old_value, "co2_Variable122", None)
                if opp_val == self:
                    setattr(old_value, "co2_Variable122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Variable122"):
                opp_val = getattr(value, "co2_Variable122", None)
                setattr(value, "co2_Variable122", self)

    @property
    def co2_Type(self):
        return self.__co2_Type

    @co2_Type.setter
    def co2_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_Type__co2_Type", None)
        self.__co2_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Placeholder"):
                opp_val = getattr(old_value, "co2_Placeholder", None)
                if opp_val == self:
                    setattr(old_value, "co2_Placeholder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Placeholder"):
                opp_val = getattr(value, "co2_Placeholder", None)
                setattr(value, "co2_Placeholder", self)

class Expression:

    pass
class co2_BooleanLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class co2_VariableReference(Expression):

    pass
class co2_Comparison(Expression):

    def __init__(self, op: str, co2_Comparison: "co2_Expression" = None, co2_Comparison156: "co2_Expression" = None):
        self.op = op
        self.co2_Comparison = co2_Comparison
        self.co2_Comparison156 = co2_Comparison156
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def co2_Comparison(self):
        return self.__co2_Comparison

    @co2_Comparison.setter
    def co2_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_Comparison__co2_Comparison", None)
        self.__co2_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Expression154"):
                opp_val = getattr(old_value, "co2_Expression154", None)
                if opp_val == self:
                    setattr(old_value, "co2_Expression154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Expression154"):
                opp_val = getattr(value, "co2_Expression154", None)
                setattr(value, "co2_Expression154", self)

    @property
    def co2_Comparison156(self):
        return self.__co2_Comparison156

    @co2_Comparison156.setter
    def co2_Comparison156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_Comparison__co2_Comparison156", None)
        self.__co2_Comparison156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Expression157"):
                opp_val = getattr(old_value, "co2_Expression157", None)
                if opp_val == self:
                    setattr(old_value, "co2_Expression157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Expression157"):
                opp_val = getattr(value, "co2_Expression157", None)
                setattr(value, "co2_Expression157", self)

class co2_OrExpression(Expression):

    pass
class co2_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class co2_Plus(Expression):

    pass
class co2_ArithmeticSigned(Expression):

    pass
class co2_Equals(Expression):

    def __init__(self, op: str, co2_Equals161: "co2_Expression" = None, co2_Equals: "co2_Expression" = None):
        self.op = op
        self.co2_Equals161 = co2_Equals161
        self.co2_Equals = co2_Equals
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def co2_Equals161(self):
        return self.__co2_Equals161

    @co2_Equals161.setter
    def co2_Equals161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_Equals__co2_Equals161", None)
        self.__co2_Equals161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Expression162"):
                opp_val = getattr(old_value, "co2_Expression162", None)
                if opp_val == self:
                    setattr(old_value, "co2_Expression162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Expression162"):
                opp_val = getattr(value, "co2_Expression162", None)
                setattr(value, "co2_Expression162", self)

    @property
    def co2_Equals(self):
        return self.__co2_Equals

    @co2_Equals.setter
    def co2_Equals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_Equals__co2_Equals", None)
        self.__co2_Equals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Expression159"):
                opp_val = getattr(old_value, "co2_Expression159", None)
                if opp_val == self:
                    setattr(old_value, "co2_Expression159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Expression159"):
                opp_val = getattr(value, "co2_Expression159", None)
                setattr(value, "co2_Expression159", self)

class co2_Placeholder(Expression):

    pass
class co2_BooleanNegation(Expression):

    pass
class co2_MultiOrDiv(Expression):

    def __init__(self, op: str, co2_MultiOrDiv: "co2_Expression" = None, co2_MultiOrDiv176: "co2_Expression" = None):
        self.op = op
        self.co2_MultiOrDiv = co2_MultiOrDiv
        self.co2_MultiOrDiv176 = co2_MultiOrDiv176
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def co2_MultiOrDiv(self):
        return self.__co2_MultiOrDiv

    @co2_MultiOrDiv.setter
    def co2_MultiOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_MultiOrDiv__co2_MultiOrDiv", None)
        self.__co2_MultiOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Expression174"):
                opp_val = getattr(old_value, "co2_Expression174", None)
                if opp_val == self:
                    setattr(old_value, "co2_Expression174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Expression174"):
                opp_val = getattr(value, "co2_Expression174", None)
                setattr(value, "co2_Expression174", self)

    @property
    def co2_MultiOrDiv176(self):
        return self.__co2_MultiOrDiv176

    @co2_MultiOrDiv176.setter
    def co2_MultiOrDiv176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_MultiOrDiv__co2_MultiOrDiv176", None)
        self.__co2_MultiOrDiv176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Expression177"):
                opp_val = getattr(old_value, "co2_Expression177", None)
                if opp_val == self:
                    setattr(old_value, "co2_Expression177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Expression177"):
                opp_val = getattr(value, "co2_Expression177", None)
                setattr(value, "co2_Expression177", self)

class co2_AndExpression(Expression):

    pass
class co2_Minus(Expression):

    pass
class co2_NumberLiteral(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class co2_Case:

    pass
class co2_Input:

    pass
class ReceiveGroup:

    pass
class co2_Receive(ReceiveGroup):

    def __init__(self, timeout: bool, co2_Receive: set["co2_Input"] = None, co2_Receive93: "co2_TimeoutProcess" = None):
        self.timeout = timeout
        self.co2_Receive = co2_Receive if co2_Receive is not None else set()
        self.co2_Receive93 = co2_Receive93
        
    @property
    def timeout(self) -> bool:
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: bool):
        self.__timeout = timeout

    @property
    def co2_Receive93(self):
        return self.__co2_Receive93

    @co2_Receive93.setter
    def co2_Receive93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_Receive__co2_Receive93", None)
        self.__co2_Receive93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_TimeoutProcess94"):
                opp_val = getattr(old_value, "co2_TimeoutProcess94", None)
                if opp_val == self:
                    setattr(old_value, "co2_TimeoutProcess94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_TimeoutProcess94"):
                opp_val = getattr(value, "co2_TimeoutProcess94", None)
                setattr(value, "co2_TimeoutProcess94", self)

    @property
    def co2_Receive(self):
        return self.__co2_Receive

    @co2_Receive.setter
    def co2_Receive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_Receive__co2_Receive", None)
        self.__co2_Receive = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "co2_Input"):
                    opp_val = getattr(item, "co2_Input", None)
                    
                    if opp_val == self:
                        setattr(item, "co2_Input", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "co2_Input"):
                    opp_val = getattr(item, "co2_Input", None)
                    
                    setattr(item, "co2_Input", self)
                    

class SendGroup:

    pass
class co2_Send(SendGroup):

    pass
class co2_TimeoutProcess:

    pass
class co2_Session(VariableDeclaration):

    pass
class co2_ExtAction(Action):

    pass
class co2_IntAction(Action):

    pass
class co2_Contract:

    pass
class co2_VariableDeclaration:

    def __init__(self, name: str, co2_VariableDeclaration: "co2_Tell" = None, co2_VariableDeclaration46: "co2_Retract" = None, co2_VariableDeclaration48: "co2_DoOutput" = None, co2_VariableDeclaration55: "co2_DoInput" = None, co2_VariableDeclaration62: "co2_Ask" = None, co2_VariableDeclaration90: "co2_Send" = None, co2_VariableDeclaration106: "co2_Input" = None, co2_VariableDeclaration183: "co2_VariableReference" = None):
        self.name = name
        self.co2_VariableDeclaration = co2_VariableDeclaration
        self.co2_VariableDeclaration46 = co2_VariableDeclaration46
        self.co2_VariableDeclaration48 = co2_VariableDeclaration48
        self.co2_VariableDeclaration55 = co2_VariableDeclaration55
        self.co2_VariableDeclaration62 = co2_VariableDeclaration62
        self.co2_VariableDeclaration90 = co2_VariableDeclaration90
        self.co2_VariableDeclaration106 = co2_VariableDeclaration106
        self.co2_VariableDeclaration183 = co2_VariableDeclaration183
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def co2_VariableDeclaration62(self):
        return self.__co2_VariableDeclaration62

    @co2_VariableDeclaration62.setter
    def co2_VariableDeclaration62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_VariableDeclaration__co2_VariableDeclaration62", None)
        self.__co2_VariableDeclaration62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Ask"):
                opp_val = getattr(old_value, "co2_Ask", None)
                if opp_val == self:
                    setattr(old_value, "co2_Ask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Ask"):
                opp_val = getattr(value, "co2_Ask", None)
                setattr(value, "co2_Ask", self)

    @property
    def co2_VariableDeclaration106(self):
        return self.__co2_VariableDeclaration106

    @co2_VariableDeclaration106.setter
    def co2_VariableDeclaration106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_VariableDeclaration__co2_VariableDeclaration106", None)
        self.__co2_VariableDeclaration106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Input105"):
                opp_val = getattr(old_value, "co2_Input105", None)
                if opp_val == self:
                    setattr(old_value, "co2_Input105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Input105"):
                opp_val = getattr(value, "co2_Input105", None)
                setattr(value, "co2_Input105", self)

    @property
    def co2_VariableDeclaration55(self):
        return self.__co2_VariableDeclaration55

    @co2_VariableDeclaration55.setter
    def co2_VariableDeclaration55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_VariableDeclaration__co2_VariableDeclaration55", None)
        self.__co2_VariableDeclaration55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_DoInput"):
                opp_val = getattr(old_value, "co2_DoInput", None)
                if opp_val == self:
                    setattr(old_value, "co2_DoInput", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_DoInput"):
                opp_val = getattr(value, "co2_DoInput", None)
                setattr(value, "co2_DoInput", self)

    @property
    def co2_VariableDeclaration46(self):
        return self.__co2_VariableDeclaration46

    @co2_VariableDeclaration46.setter
    def co2_VariableDeclaration46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_VariableDeclaration__co2_VariableDeclaration46", None)
        self.__co2_VariableDeclaration46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Retract"):
                opp_val = getattr(old_value, "co2_Retract", None)
                if opp_val == self:
                    setattr(old_value, "co2_Retract", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Retract"):
                opp_val = getattr(value, "co2_Retract", None)
                setattr(value, "co2_Retract", self)

    @property
    def co2_VariableDeclaration(self):
        return self.__co2_VariableDeclaration

    @co2_VariableDeclaration.setter
    def co2_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_VariableDeclaration__co2_VariableDeclaration", None)
        self.__co2_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Tell"):
                opp_val = getattr(old_value, "co2_Tell", None)
                if opp_val == self:
                    setattr(old_value, "co2_Tell", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Tell"):
                opp_val = getattr(value, "co2_Tell", None)
                setattr(value, "co2_Tell", self)

    @property
    def co2_VariableDeclaration90(self):
        return self.__co2_VariableDeclaration90

    @co2_VariableDeclaration90.setter
    def co2_VariableDeclaration90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_VariableDeclaration__co2_VariableDeclaration90", None)
        self.__co2_VariableDeclaration90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Send89"):
                opp_val = getattr(old_value, "co2_Send89", None)
                if opp_val == self:
                    setattr(old_value, "co2_Send89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Send89"):
                opp_val = getattr(value, "co2_Send89", None)
                setattr(value, "co2_Send89", self)

    @property
    def co2_VariableDeclaration48(self):
        return self.__co2_VariableDeclaration48

    @co2_VariableDeclaration48.setter
    def co2_VariableDeclaration48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_VariableDeclaration__co2_VariableDeclaration48", None)
        self.__co2_VariableDeclaration48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_DoOutput"):
                opp_val = getattr(old_value, "co2_DoOutput", None)
                if opp_val == self:
                    setattr(old_value, "co2_DoOutput", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_DoOutput"):
                opp_val = getattr(value, "co2_DoOutput", None)
                setattr(value, "co2_DoOutput", self)

    @property
    def co2_VariableDeclaration183(self):
        return self.__co2_VariableDeclaration183

    @co2_VariableDeclaration183.setter
    def co2_VariableDeclaration183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_VariableDeclaration__co2_VariableDeclaration183", None)
        self.__co2_VariableDeclaration183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_VariableReference"):
                opp_val = getattr(old_value, "co2_VariableReference", None)
                if opp_val == self:
                    setattr(old_value, "co2_VariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_VariableReference"):
                opp_val = getattr(value, "co2_VariableReference", None)
                setattr(value, "co2_VariableReference", self)

class Prefix:

    pass
class co2_DoInput(Prefix):

    pass
class co2_DoOutput(Prefix):

    pass
class co2_Tau(Prefix):

    pass
class co2_Ask(Prefix):

    def __init__(self, formula: str, co2_Ask: "co2_VariableDeclaration" = None):
        self.formula = formula
        self.co2_Ask = co2_Ask
        
    @property
    def formula(self) -> str:
        return self.__formula

    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula

    @property
    def co2_Ask(self):
        return self.__co2_Ask

    @co2_Ask.setter
    def co2_Ask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_Ask__co2_Ask", None)
        self.__co2_Ask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_VariableDeclaration62"):
                opp_val = getattr(old_value, "co2_VariableDeclaration62", None)
                if opp_val == self:
                    setattr(old_value, "co2_VariableDeclaration62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_VariableDeclaration62"):
                opp_val = getattr(value, "co2_VariableDeclaration62", None)
                setattr(value, "co2_VariableDeclaration62", self)

class co2_Retract(Prefix):

    pass
class co2_Tell(Prefix):

    pass
class co2_Expression:

    pass
class co2_Prefix:

    pass
class co2_ContractDefinition:

    def __init__(self, name: str, co2_ContractDefinition: "co2_ContractsAndProcessesDeclaration" = None, co2_ContractDefinition44: "co2_Tell" = None, co2_ContractDefinition129: "co2_Session" = None, co2_ContractDefinition131: "co2_Contract" = None, co2_ContractDefinition185: "co2_ContractReference" = None):
        self.name = name
        self.co2_ContractDefinition = co2_ContractDefinition
        self.co2_ContractDefinition44 = co2_ContractDefinition44
        self.co2_ContractDefinition129 = co2_ContractDefinition129
        self.co2_ContractDefinition131 = co2_ContractDefinition131
        self.co2_ContractDefinition185 = co2_ContractDefinition185
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def co2_ContractDefinition129(self):
        return self.__co2_ContractDefinition129

    @co2_ContractDefinition129.setter
    def co2_ContractDefinition129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_ContractDefinition__co2_ContractDefinition129", None)
        self.__co2_ContractDefinition129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Session128"):
                opp_val = getattr(old_value, "co2_Session128", None)
                if opp_val == self:
                    setattr(old_value, "co2_Session128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Session128"):
                opp_val = getattr(value, "co2_Session128", None)
                setattr(value, "co2_Session128", self)

    @property
    def co2_ContractDefinition131(self):
        return self.__co2_ContractDefinition131

    @co2_ContractDefinition131.setter
    def co2_ContractDefinition131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_ContractDefinition__co2_ContractDefinition131", None)
        self.__co2_ContractDefinition131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Contract132"):
                opp_val = getattr(old_value, "co2_Contract132", None)
                if opp_val == self:
                    setattr(old_value, "co2_Contract132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Contract132"):
                opp_val = getattr(value, "co2_Contract132", None)
                setattr(value, "co2_Contract132", self)

    @property
    def co2_ContractDefinition(self):
        return self.__co2_ContractDefinition

    @co2_ContractDefinition.setter
    def co2_ContractDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_ContractDefinition__co2_ContractDefinition", None)
        self.__co2_ContractDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_ContractsAndProcessesDeclaration8"):
                opp_val = getattr(old_value, "co2_ContractsAndProcessesDeclaration8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_ContractsAndProcessesDeclaration8"):
                opp_val = getattr(value, "co2_ContractsAndProcessesDeclaration8", None)
                if opp_val is None:
                    setattr(value, "co2_ContractsAndProcessesDeclaration8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def co2_ContractDefinition185(self):
        return self.__co2_ContractDefinition185

    @co2_ContractDefinition185.setter
    def co2_ContractDefinition185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_ContractDefinition__co2_ContractDefinition185", None)
        self.__co2_ContractDefinition185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_ContractReference"):
                opp_val = getattr(old_value, "co2_ContractReference", None)
                if opp_val == self:
                    setattr(old_value, "co2_ContractReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_ContractReference"):
                opp_val = getattr(value, "co2_ContractReference", None)
                setattr(value, "co2_ContractReference", self)

    @property
    def co2_ContractDefinition44(self):
        return self.__co2_ContractDefinition44

    @co2_ContractDefinition44.setter
    def co2_ContractDefinition44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_ContractDefinition__co2_ContractDefinition44", None)
        self.__co2_ContractDefinition44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Tell43"):
                opp_val = getattr(old_value, "co2_Tell43", None)
                if opp_val == self:
                    setattr(old_value, "co2_Tell43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Tell43"):
                opp_val = getattr(value, "co2_Tell43", None)
                setattr(value, "co2_Tell43", self)

class co2_Process:

    pass
class co2_DelimitedProcess:

    pass
class Process:

    pass
class co2_Sum(Process):

    pass
class co2_SendGroup(Process):

    pass
class co2_TellAndReturn(Process):

    pass
class co2_ReceiveGroup(Process):

    pass
class co2_SwitchCase(Process):

    def __init__(self, default: bool, co2_SwitchCase: "co2_Expression" = None, co2_SwitchCase110: set["co2_Case"] = None, co2_SwitchCase112: "co2_Process" = None):
        self.default = default
        self.co2_SwitchCase = co2_SwitchCase
        self.co2_SwitchCase110 = co2_SwitchCase110 if co2_SwitchCase110 is not None else set()
        self.co2_SwitchCase112 = co2_SwitchCase112
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def co2_SwitchCase112(self):
        return self.__co2_SwitchCase112

    @co2_SwitchCase112.setter
    def co2_SwitchCase112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_SwitchCase__co2_SwitchCase112", None)
        self.__co2_SwitchCase112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Process113"):
                opp_val = getattr(old_value, "co2_Process113", None)
                if opp_val == self:
                    setattr(old_value, "co2_Process113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Process113"):
                opp_val = getattr(value, "co2_Process113", None)
                setattr(value, "co2_Process113", self)

    @property
    def co2_SwitchCase(self):
        return self.__co2_SwitchCase

    @co2_SwitchCase.setter
    def co2_SwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_SwitchCase__co2_SwitchCase", None)
        self.__co2_SwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Expression108"):
                opp_val = getattr(old_value, "co2_Expression108", None)
                if opp_val == self:
                    setattr(old_value, "co2_Expression108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Expression108"):
                opp_val = getattr(value, "co2_Expression108", None)
                setattr(value, "co2_Expression108", self)

    @property
    def co2_SwitchCase110(self):
        return self.__co2_SwitchCase110

    @co2_SwitchCase110.setter
    def co2_SwitchCase110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_SwitchCase__co2_SwitchCase110", None)
        self.__co2_SwitchCase110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "co2_Case"):
                    opp_val = getattr(item, "co2_Case", None)
                    
                    if opp_val == self:
                        setattr(item, "co2_Case", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "co2_Case"):
                    opp_val = getattr(item, "co2_Case", None)
                    
                    setattr(item, "co2_Case", self)
                    

class co2_EmptyProcess(Process):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class co2_TellAndWait(Process):

    def __init__(self, timeout: bool, co2_TellAndWait: "co2_Session" = None, co2_TellAndWait70: "co2_Process" = None, co2_TellAndWait73: "co2_TimeoutProcess" = None):
        self.timeout = timeout
        self.co2_TellAndWait = co2_TellAndWait
        self.co2_TellAndWait70 = co2_TellAndWait70
        self.co2_TellAndWait73 = co2_TellAndWait73
        
    @property
    def timeout(self) -> bool:
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: bool):
        self.__timeout = timeout

    @property
    def co2_TellAndWait(self):
        return self.__co2_TellAndWait

    @co2_TellAndWait.setter
    def co2_TellAndWait(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_TellAndWait__co2_TellAndWait", None)
        self.__co2_TellAndWait = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Session68"):
                opp_val = getattr(old_value, "co2_Session68", None)
                if opp_val == self:
                    setattr(old_value, "co2_Session68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Session68"):
                opp_val = getattr(value, "co2_Session68", None)
                setattr(value, "co2_Session68", self)

    @property
    def co2_TellAndWait70(self):
        return self.__co2_TellAndWait70

    @co2_TellAndWait70.setter
    def co2_TellAndWait70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_TellAndWait__co2_TellAndWait70", None)
        self.__co2_TellAndWait70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_Process71"):
                opp_val = getattr(old_value, "co2_Process71", None)
                if opp_val == self:
                    setattr(old_value, "co2_Process71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_Process71"):
                opp_val = getattr(value, "co2_Process71", None)
                setattr(value, "co2_Process71", self)

    @property
    def co2_TellAndWait73(self):
        return self.__co2_TellAndWait73

    @co2_TellAndWait73.setter
    def co2_TellAndWait73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_TellAndWait__co2_TellAndWait73", None)
        self.__co2_TellAndWait73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_TimeoutProcess"):
                opp_val = getattr(old_value, "co2_TimeoutProcess", None)
                if opp_val == self:
                    setattr(old_value, "co2_TimeoutProcess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_TimeoutProcess"):
                opp_val = getattr(value, "co2_TimeoutProcess", None)
                setattr(value, "co2_TimeoutProcess", self)

class co2_IfThenElse(Process):

    pass
class co2_ProcessCall(Process):

    pass
class co2_RetractedProcess(Process):

    pass
class co2_ParallelProcesses(Process):

    pass
class co2_Variable(VariableDeclaration):

    pass
class co2_ProcessDefinition:

    def __init__(self, withoutRestrictions: bool, name: str, co2_ProcessDefinition: "co2_HonestyDeclaration" = None, co2_ProcessDefinition11: "co2_ContractsAndProcessesDeclaration" = None, co2_ProcessDefinition13: set["co2_Variable"] = None, co2_ProcessDefinition15: "co2_ParallelProcesses" = None, co2_ProcessDefinition32: "co2_ProcessCall" = None):
        self.withoutRestrictions = withoutRestrictions
        self.name = name
        self.co2_ProcessDefinition = co2_ProcessDefinition
        self.co2_ProcessDefinition11 = co2_ProcessDefinition11
        self.co2_ProcessDefinition13 = co2_ProcessDefinition13 if co2_ProcessDefinition13 is not None else set()
        self.co2_ProcessDefinition15 = co2_ProcessDefinition15
        self.co2_ProcessDefinition32 = co2_ProcessDefinition32
        
    @property
    def withoutRestrictions(self) -> bool:
        return self.__withoutRestrictions

    @withoutRestrictions.setter
    def withoutRestrictions(self, withoutRestrictions: bool):
        self.__withoutRestrictions = withoutRestrictions

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def co2_ProcessDefinition(self):
        return self.__co2_ProcessDefinition

    @co2_ProcessDefinition.setter
    def co2_ProcessDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_ProcessDefinition__co2_ProcessDefinition", None)
        self.__co2_ProcessDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_HonestyDeclaration6"):
                opp_val = getattr(old_value, "co2_HonestyDeclaration6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_HonestyDeclaration6"):
                opp_val = getattr(value, "co2_HonestyDeclaration6", None)
                if opp_val is None:
                    setattr(value, "co2_HonestyDeclaration6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def co2_ProcessDefinition32(self):
        return self.__co2_ProcessDefinition32

    @co2_ProcessDefinition32.setter
    def co2_ProcessDefinition32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_ProcessDefinition__co2_ProcessDefinition32", None)
        self.__co2_ProcessDefinition32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_ProcessCall"):
                opp_val = getattr(old_value, "co2_ProcessCall", None)
                if opp_val == self:
                    setattr(old_value, "co2_ProcessCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_ProcessCall"):
                opp_val = getattr(value, "co2_ProcessCall", None)
                setattr(value, "co2_ProcessCall", self)

    @property
    def co2_ProcessDefinition15(self):
        return self.__co2_ProcessDefinition15

    @co2_ProcessDefinition15.setter
    def co2_ProcessDefinition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_ProcessDefinition__co2_ProcessDefinition15", None)
        self.__co2_ProcessDefinition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_ParallelProcesses"):
                opp_val = getattr(old_value, "co2_ParallelProcesses", None)
                if opp_val == self:
                    setattr(old_value, "co2_ParallelProcesses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_ParallelProcesses"):
                opp_val = getattr(value, "co2_ParallelProcesses", None)
                setattr(value, "co2_ParallelProcesses", self)

    @property
    def co2_ProcessDefinition13(self):
        return self.__co2_ProcessDefinition13

    @co2_ProcessDefinition13.setter
    def co2_ProcessDefinition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_ProcessDefinition__co2_ProcessDefinition13", None)
        self.__co2_ProcessDefinition13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "co2_Variable"):
                    opp_val = getattr(item, "co2_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "co2_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "co2_Variable"):
                    opp_val = getattr(item, "co2_Variable", None)
                    
                    setattr(item, "co2_Variable", self)
                    

    @property
    def co2_ProcessDefinition11(self):
        return self.__co2_ProcessDefinition11

    @co2_ProcessDefinition11.setter
    def co2_ProcessDefinition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_ProcessDefinition__co2_ProcessDefinition11", None)
        self.__co2_ProcessDefinition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_ContractsAndProcessesDeclaration10"):
                opp_val = getattr(old_value, "co2_ContractsAndProcessesDeclaration10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_ContractsAndProcessesDeclaration10"):
                opp_val = getattr(value, "co2_ContractsAndProcessesDeclaration10", None)
                if opp_val is None:
                    setattr(value, "co2_ContractsAndProcessesDeclaration10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class co2_Import:

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class co2_ContractsAndProcessesDeclaration:

    pass
class co2_HonestyDeclaration:

    pass
class co2_PackageDeclaration:

    def __init__(self, single: bool, name: str, co2_PackageDeclaration: "co2_CO2System" = None):
        self.single = single
        self.name = name
        self.co2_PackageDeclaration = co2_PackageDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def single(self) -> bool:
        return self.__single

    @single.setter
    def single(self, single: bool):
        self.__single = single

    @property
    def co2_PackageDeclaration(self):
        return self.__co2_PackageDeclaration

    @co2_PackageDeclaration.setter
    def co2_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_co2_PackageDeclaration__co2_PackageDeclaration", None)
        self.__co2_PackageDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "co2_CO2System"):
                opp_val = getattr(old_value, "co2_CO2System", None)
                if opp_val == self:
                    setattr(old_value, "co2_CO2System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "co2_CO2System"):
                opp_val = getattr(value, "co2_CO2System", None)
                setattr(value, "co2_CO2System", self)

class co2_CO2System:

    pass