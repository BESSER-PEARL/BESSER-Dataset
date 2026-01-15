from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ChangeAction:

    pass
class stateMachineDsl_ResetAction(ChangeAction):

    pass
class stateMachineDsl_DecrementAction(ChangeAction):

    pass
class stateMachineDsl_IncrementAction(ChangeAction):

    pass
class stateMachineDsl_ProcedureUse:

    pass
class Expression:

    pass
class stateMachineDsl_BoolExp(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class stateMachineDsl_And(Expression):

    pass
class stateMachineDsl_Equality(Expression):

    def __init__(self, op: str, stateMachineDsl_Equality: "stateMachineDsl_Expression" = None, stateMachineDsl_Equality112: "stateMachineDsl_Expression" = None):
        self.op = op
        self.stateMachineDsl_Equality = stateMachineDsl_Equality
        self.stateMachineDsl_Equality112 = stateMachineDsl_Equality112
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def stateMachineDsl_Equality112(self):
        return self.__stateMachineDsl_Equality112

    @stateMachineDsl_Equality112.setter
    def stateMachineDsl_Equality112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Equality__stateMachineDsl_Equality112", None)
        self.__stateMachineDsl_Equality112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Expression113"):
                opp_val = getattr(old_value, "stateMachineDsl_Expression113", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Expression113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Expression113"):
                opp_val = getattr(value, "stateMachineDsl_Expression113", None)
                setattr(value, "stateMachineDsl_Expression113", self)

    @property
    def stateMachineDsl_Equality(self):
        return self.__stateMachineDsl_Equality

    @stateMachineDsl_Equality.setter
    def stateMachineDsl_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Equality__stateMachineDsl_Equality", None)
        self.__stateMachineDsl_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Expression110"):
                opp_val = getattr(old_value, "stateMachineDsl_Expression110", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Expression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Expression110"):
                opp_val = getattr(value, "stateMachineDsl_Expression110", None)
                setattr(value, "stateMachineDsl_Expression110", self)

class stateMachineDsl_Not(Expression):

    pass
class stateMachineDsl_MulOrDiv(Expression):

    def __init__(self, op: str, stateMachineDsl_MulOrDiv: "stateMachineDsl_Expression" = None, stateMachineDsl_MulOrDiv132: "stateMachineDsl_Expression" = None):
        self.op = op
        self.stateMachineDsl_MulOrDiv = stateMachineDsl_MulOrDiv
        self.stateMachineDsl_MulOrDiv132 = stateMachineDsl_MulOrDiv132
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def stateMachineDsl_MulOrDiv132(self):
        return self.__stateMachineDsl_MulOrDiv132

    @stateMachineDsl_MulOrDiv132.setter
    def stateMachineDsl_MulOrDiv132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_MulOrDiv__stateMachineDsl_MulOrDiv132", None)
        self.__stateMachineDsl_MulOrDiv132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Expression133"):
                opp_val = getattr(old_value, "stateMachineDsl_Expression133", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Expression133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Expression133"):
                opp_val = getattr(value, "stateMachineDsl_Expression133", None)
                setattr(value, "stateMachineDsl_Expression133", self)

    @property
    def stateMachineDsl_MulOrDiv(self):
        return self.__stateMachineDsl_MulOrDiv

    @stateMachineDsl_MulOrDiv.setter
    def stateMachineDsl_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_MulOrDiv__stateMachineDsl_MulOrDiv", None)
        self.__stateMachineDsl_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Expression130"):
                opp_val = getattr(old_value, "stateMachineDsl_Expression130", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Expression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Expression130"):
                opp_val = getattr(value, "stateMachineDsl_Expression130", None)
                setattr(value, "stateMachineDsl_Expression130", self)

class stateMachineDsl_MinusCond(Expression):

    pass
class stateMachineDsl_Or(Expression):

    pass
class stateMachineDsl_StringExp(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class stateMachineDsl_NumberExp(Expression):

    def __init__(self, negative: str, value: int):
        self.negative = negative
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def negative(self) -> str:
        return self.__negative

    @negative.setter
    def negative(self, negative: str):
        self.__negative = negative

class stateMachineDsl_Comparison(Expression):

    def __init__(self, op: str, stateMachineDsl_Comparison: "stateMachineDsl_Expression" = None, stateMachineDsl_Comparison117: "stateMachineDsl_Expression" = None):
        self.op = op
        self.stateMachineDsl_Comparison = stateMachineDsl_Comparison
        self.stateMachineDsl_Comparison117 = stateMachineDsl_Comparison117
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def stateMachineDsl_Comparison117(self):
        return self.__stateMachineDsl_Comparison117

    @stateMachineDsl_Comparison117.setter
    def stateMachineDsl_Comparison117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Comparison__stateMachineDsl_Comparison117", None)
        self.__stateMachineDsl_Comparison117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Expression118"):
                opp_val = getattr(old_value, "stateMachineDsl_Expression118", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Expression118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Expression118"):
                opp_val = getattr(value, "stateMachineDsl_Expression118", None)
                setattr(value, "stateMachineDsl_Expression118", self)

    @property
    def stateMachineDsl_Comparison(self):
        return self.__stateMachineDsl_Comparison

    @stateMachineDsl_Comparison.setter
    def stateMachineDsl_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Comparison__stateMachineDsl_Comparison", None)
        self.__stateMachineDsl_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Expression115"):
                opp_val = getattr(old_value, "stateMachineDsl_Expression115", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Expression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Expression115"):
                opp_val = getattr(value, "stateMachineDsl_Expression115", None)
                setattr(value, "stateMachineDsl_Expression115", self)

class stateMachineDsl_DoubleExp(Expression):

    def __init__(self, negative: str, number: int, decimal: int):
        self.negative = negative
        self.number = number
        self.decimal = decimal
        
    @property
    def decimal(self) -> int:
        return self.__decimal

    @decimal.setter
    def decimal(self, decimal: int):
        self.__decimal = decimal

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def negative(self) -> str:
        return self.__negative

    @negative.setter
    def negative(self, negative: str):
        self.__negative = negative

class stateMachineDsl_VarRef(Expression):

    pass
class stateMachineDsl_Parenthesis(Expression):

    pass
class stateMachineDsl_PlusCond(Expression):

    pass
class stateMachineDsl_FunctionUse(Expression):

    pass
class stateMachineDsl_ChangeAction:

    pass
class stateMachineDsl_SetAction:

    pass
class stateMachineDsl_EObject:

    pass
class ExtDeclaration:

    pass
class stateMachineDsl_Function(ExtDeclaration):

    pass
class stateMachineDsl_Parameter:

    pass
class stateMachineDsl_Member:

    pass
class stateMachineDsl_ParameterFunction:

    def __init__(self, name: str, stateMachineDsl_ParameterFunction: "stateMachineDsl_ExtDeclaration" = None, stateMachineDsl_ParameterFunction72: "stateMachineDsl_VarType" = None):
        self.name = name
        self.stateMachineDsl_ParameterFunction = stateMachineDsl_ParameterFunction
        self.stateMachineDsl_ParameterFunction72 = stateMachineDsl_ParameterFunction72
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachineDsl_ParameterFunction72(self):
        return self.__stateMachineDsl_ParameterFunction72

    @stateMachineDsl_ParameterFunction72.setter
    def stateMachineDsl_ParameterFunction72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_ParameterFunction__stateMachineDsl_ParameterFunction72", None)
        self.__stateMachineDsl_ParameterFunction72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_VarType73"):
                opp_val = getattr(old_value, "stateMachineDsl_VarType73", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_VarType73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_VarType73"):
                opp_val = getattr(value, "stateMachineDsl_VarType73", None)
                setattr(value, "stateMachineDsl_VarType73", self)

    @property
    def stateMachineDsl_ParameterFunction(self):
        return self.__stateMachineDsl_ParameterFunction

    @stateMachineDsl_ParameterFunction.setter
    def stateMachineDsl_ParameterFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_ParameterFunction__stateMachineDsl_ParameterFunction", None)
        self.__stateMachineDsl_ParameterFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_ExtDeclaration43"):
                opp_val = getattr(old_value, "stateMachineDsl_ExtDeclaration43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_ExtDeclaration43"):
                opp_val = getattr(value, "stateMachineDsl_ExtDeclaration43", None)
                if opp_val is None:
                    setattr(value, "stateMachineDsl_ExtDeclaration43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stateMachineDsl_Expression:

    pass
class stateMachineDsl_VarType:

    def __init__(self, vt: str, stateMachineDsl_VarType: "stateMachineDsl_Variable" = None, stateMachineDsl_VarType59: "stateMachineDsl_Parameter" = None, stateMachineDsl_VarType70: "stateMachineDsl_Function" = None, stateMachineDsl_VarType73: "stateMachineDsl_ParameterFunction" = None):
        self.vt = vt
        self.stateMachineDsl_VarType = stateMachineDsl_VarType
        self.stateMachineDsl_VarType59 = stateMachineDsl_VarType59
        self.stateMachineDsl_VarType70 = stateMachineDsl_VarType70
        self.stateMachineDsl_VarType73 = stateMachineDsl_VarType73
        
    @property
    def vt(self) -> str:
        return self.__vt

    @vt.setter
    def vt(self, vt: str):
        self.__vt = vt

    @property
    def stateMachineDsl_VarType70(self):
        return self.__stateMachineDsl_VarType70

    @stateMachineDsl_VarType70.setter
    def stateMachineDsl_VarType70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_VarType__stateMachineDsl_VarType70", None)
        self.__stateMachineDsl_VarType70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Function"):
                opp_val = getattr(old_value, "stateMachineDsl_Function", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Function"):
                opp_val = getattr(value, "stateMachineDsl_Function", None)
                setattr(value, "stateMachineDsl_Function", self)

    @property
    def stateMachineDsl_VarType59(self):
        return self.__stateMachineDsl_VarType59

    @stateMachineDsl_VarType59.setter
    def stateMachineDsl_VarType59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_VarType__stateMachineDsl_VarType59", None)
        self.__stateMachineDsl_VarType59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Parameter58"):
                opp_val = getattr(old_value, "stateMachineDsl_Parameter58", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Parameter58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Parameter58"):
                opp_val = getattr(value, "stateMachineDsl_Parameter58", None)
                setattr(value, "stateMachineDsl_Parameter58", self)

    @property
    def stateMachineDsl_VarType(self):
        return self.__stateMachineDsl_VarType

    @stateMachineDsl_VarType.setter
    def stateMachineDsl_VarType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_VarType__stateMachineDsl_VarType", None)
        self.__stateMachineDsl_VarType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Variable39"):
                opp_val = getattr(old_value, "stateMachineDsl_Variable39", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Variable39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Variable39"):
                opp_val = getattr(value, "stateMachineDsl_Variable39", None)
                setattr(value, "stateMachineDsl_Variable39", self)

    @property
    def stateMachineDsl_VarType73(self):
        return self.__stateMachineDsl_VarType73

    @stateMachineDsl_VarType73.setter
    def stateMachineDsl_VarType73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_VarType__stateMachineDsl_VarType73", None)
        self.__stateMachineDsl_VarType73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_ParameterFunction72"):
                opp_val = getattr(old_value, "stateMachineDsl_ParameterFunction72", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_ParameterFunction72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_ParameterFunction72"):
                opp_val = getattr(value, "stateMachineDsl_ParameterFunction72", None)
                setattr(value, "stateMachineDsl_ParameterFunction72", self)

class stateMachineDsl_VarParName:

    def __init__(self, name: str, stateMachineDsl_VarParName: "stateMachineDsl_Variable" = None, stateMachineDsl_VarParName62: "stateMachineDsl_Parameter" = None, stateMachineDsl_VarParName80: "stateMachineDsl_SetAction" = None, stateMachineDsl_VarParName85: "stateMachineDsl_ChangeAction" = None, stateMachineDsl_VarParName137: "stateMachineDsl_VarRef" = None):
        self.name = name
        self.stateMachineDsl_VarParName = stateMachineDsl_VarParName
        self.stateMachineDsl_VarParName62 = stateMachineDsl_VarParName62
        self.stateMachineDsl_VarParName80 = stateMachineDsl_VarParName80
        self.stateMachineDsl_VarParName85 = stateMachineDsl_VarParName85
        self.stateMachineDsl_VarParName137 = stateMachineDsl_VarParName137
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachineDsl_VarParName85(self):
        return self.__stateMachineDsl_VarParName85

    @stateMachineDsl_VarParName85.setter
    def stateMachineDsl_VarParName85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_VarParName__stateMachineDsl_VarParName85", None)
        self.__stateMachineDsl_VarParName85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_ChangeAction"):
                opp_val = getattr(old_value, "stateMachineDsl_ChangeAction", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_ChangeAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_ChangeAction"):
                opp_val = getattr(value, "stateMachineDsl_ChangeAction", None)
                setattr(value, "stateMachineDsl_ChangeAction", self)

    @property
    def stateMachineDsl_VarParName62(self):
        return self.__stateMachineDsl_VarParName62

    @stateMachineDsl_VarParName62.setter
    def stateMachineDsl_VarParName62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_VarParName__stateMachineDsl_VarParName62", None)
        self.__stateMachineDsl_VarParName62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Parameter61"):
                opp_val = getattr(old_value, "stateMachineDsl_Parameter61", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Parameter61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Parameter61"):
                opp_val = getattr(value, "stateMachineDsl_Parameter61", None)
                setattr(value, "stateMachineDsl_Parameter61", self)

    @property
    def stateMachineDsl_VarParName80(self):
        return self.__stateMachineDsl_VarParName80

    @stateMachineDsl_VarParName80.setter
    def stateMachineDsl_VarParName80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_VarParName__stateMachineDsl_VarParName80", None)
        self.__stateMachineDsl_VarParName80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_SetAction"):
                opp_val = getattr(old_value, "stateMachineDsl_SetAction", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_SetAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_SetAction"):
                opp_val = getattr(value, "stateMachineDsl_SetAction", None)
                setattr(value, "stateMachineDsl_SetAction", self)

    @property
    def stateMachineDsl_VarParName137(self):
        return self.__stateMachineDsl_VarParName137

    @stateMachineDsl_VarParName137.setter
    def stateMachineDsl_VarParName137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_VarParName__stateMachineDsl_VarParName137", None)
        self.__stateMachineDsl_VarParName137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_VarRef"):
                opp_val = getattr(old_value, "stateMachineDsl_VarRef", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_VarRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_VarRef"):
                opp_val = getattr(value, "stateMachineDsl_VarRef", None)
                setattr(value, "stateMachineDsl_VarRef", self)

    @property
    def stateMachineDsl_VarParName(self):
        return self.__stateMachineDsl_VarParName

    @stateMachineDsl_VarParName.setter
    def stateMachineDsl_VarParName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_VarParName__stateMachineDsl_VarParName", None)
        self.__stateMachineDsl_VarParName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Variable37"):
                opp_val = getattr(old_value, "stateMachineDsl_Variable37", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Variable37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Variable37"):
                opp_val = getattr(value, "stateMachineDsl_Variable37", None)
                setattr(value, "stateMachineDsl_Variable37", self)

class stateMachineDsl_Condition:

    pass
class stateMachineDsl_CommandAction(ExtDeclaration):

    pass
class stateMachineDsl_Transition:

    pass
class stateMachineDsl_Action:

    pass
class stateMachineDsl_MemberState:

    pass
class stateMachineDsl_Procedure:

    def __init__(self, name: str, stateMachineDsl_Procedure: "stateMachineDsl_Declaration" = None, stateMachineDsl_Procedure50: set["stateMachineDsl_Parameter"] = None, stateMachineDsl_Procedure52: "stateMachineDsl_Condition" = None, stateMachineDsl_Procedure55: set["stateMachineDsl_Member"] = None, stateMachineDsl_Procedure92: "stateMachineDsl_ProcedureUse" = None):
        self.name = name
        self.stateMachineDsl_Procedure = stateMachineDsl_Procedure
        self.stateMachineDsl_Procedure50 = stateMachineDsl_Procedure50 if stateMachineDsl_Procedure50 is not None else set()
        self.stateMachineDsl_Procedure52 = stateMachineDsl_Procedure52
        self.stateMachineDsl_Procedure55 = stateMachineDsl_Procedure55 if stateMachineDsl_Procedure55 is not None else set()
        self.stateMachineDsl_Procedure92 = stateMachineDsl_Procedure92
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachineDsl_Procedure55(self):
        return self.__stateMachineDsl_Procedure55

    @stateMachineDsl_Procedure55.setter
    def stateMachineDsl_Procedure55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Procedure__stateMachineDsl_Procedure55", None)
        self.__stateMachineDsl_Procedure55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachineDsl_Member56"):
                    opp_val = getattr(item, "stateMachineDsl_Member56", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachineDsl_Member56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachineDsl_Member56"):
                    opp_val = getattr(item, "stateMachineDsl_Member56", None)
                    
                    setattr(item, "stateMachineDsl_Member56", self)
                    

    @property
    def stateMachineDsl_Procedure52(self):
        return self.__stateMachineDsl_Procedure52

    @stateMachineDsl_Procedure52.setter
    def stateMachineDsl_Procedure52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Procedure__stateMachineDsl_Procedure52", None)
        self.__stateMachineDsl_Procedure52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Condition53"):
                opp_val = getattr(old_value, "stateMachineDsl_Condition53", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Condition53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Condition53"):
                opp_val = getattr(value, "stateMachineDsl_Condition53", None)
                setattr(value, "stateMachineDsl_Condition53", self)

    @property
    def stateMachineDsl_Procedure(self):
        return self.__stateMachineDsl_Procedure

    @stateMachineDsl_Procedure.setter
    def stateMachineDsl_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Procedure__stateMachineDsl_Procedure", None)
        self.__stateMachineDsl_Procedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Declaration13"):
                opp_val = getattr(old_value, "stateMachineDsl_Declaration13", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Declaration13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Declaration13"):
                opp_val = getattr(value, "stateMachineDsl_Declaration13", None)
                setattr(value, "stateMachineDsl_Declaration13", self)

    @property
    def stateMachineDsl_Procedure92(self):
        return self.__stateMachineDsl_Procedure92

    @stateMachineDsl_Procedure92.setter
    def stateMachineDsl_Procedure92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Procedure__stateMachineDsl_Procedure92", None)
        self.__stateMachineDsl_Procedure92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_ProcedureUse"):
                opp_val = getattr(old_value, "stateMachineDsl_ProcedureUse", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_ProcedureUse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_ProcedureUse"):
                opp_val = getattr(value, "stateMachineDsl_ProcedureUse", None)
                setattr(value, "stateMachineDsl_ProcedureUse", self)

    @property
    def stateMachineDsl_Procedure50(self):
        return self.__stateMachineDsl_Procedure50

    @stateMachineDsl_Procedure50.setter
    def stateMachineDsl_Procedure50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Procedure__stateMachineDsl_Procedure50", None)
        self.__stateMachineDsl_Procedure50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachineDsl_Parameter"):
                    opp_val = getattr(item, "stateMachineDsl_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachineDsl_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachineDsl_Parameter"):
                    opp_val = getattr(item, "stateMachineDsl_Parameter", None)
                    
                    setattr(item, "stateMachineDsl_Parameter", self)
                    

class stateMachineDsl_Event:

    def __init__(self, name: str, stateMachineDsl_Event: "stateMachineDsl_Declaration" = None, stateMachineDsl_Event30: "stateMachineDsl_Transition" = None, stateMachineDsl_Event45: "stateMachineDsl_Condition" = None, stateMachineDsl_Event48: set["stateMachineDsl_Member"] = None):
        self.name = name
        self.stateMachineDsl_Event = stateMachineDsl_Event
        self.stateMachineDsl_Event30 = stateMachineDsl_Event30
        self.stateMachineDsl_Event45 = stateMachineDsl_Event45
        self.stateMachineDsl_Event48 = stateMachineDsl_Event48 if stateMachineDsl_Event48 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachineDsl_Event45(self):
        return self.__stateMachineDsl_Event45

    @stateMachineDsl_Event45.setter
    def stateMachineDsl_Event45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Event__stateMachineDsl_Event45", None)
        self.__stateMachineDsl_Event45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Condition46"):
                opp_val = getattr(old_value, "stateMachineDsl_Condition46", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Condition46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Condition46"):
                opp_val = getattr(value, "stateMachineDsl_Condition46", None)
                setattr(value, "stateMachineDsl_Condition46", self)

    @property
    def stateMachineDsl_Event30(self):
        return self.__stateMachineDsl_Event30

    @stateMachineDsl_Event30.setter
    def stateMachineDsl_Event30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Event__stateMachineDsl_Event30", None)
        self.__stateMachineDsl_Event30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Transition29"):
                opp_val = getattr(old_value, "stateMachineDsl_Transition29", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Transition29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Transition29"):
                opp_val = getattr(value, "stateMachineDsl_Transition29", None)
                setattr(value, "stateMachineDsl_Transition29", self)

    @property
    def stateMachineDsl_Event48(self):
        return self.__stateMachineDsl_Event48

    @stateMachineDsl_Event48.setter
    def stateMachineDsl_Event48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Event__stateMachineDsl_Event48", None)
        self.__stateMachineDsl_Event48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachineDsl_Member"):
                    opp_val = getattr(item, "stateMachineDsl_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachineDsl_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachineDsl_Member"):
                    opp_val = getattr(item, "stateMachineDsl_Member", None)
                    
                    setattr(item, "stateMachineDsl_Member", self)
                    

    @property
    def stateMachineDsl_Event(self):
        return self.__stateMachineDsl_Event

    @stateMachineDsl_Event.setter
    def stateMachineDsl_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_Event__stateMachineDsl_Event", None)
        self.__stateMachineDsl_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Declaration11"):
                opp_val = getattr(old_value, "stateMachineDsl_Declaration11", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Declaration11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Declaration11"):
                opp_val = getattr(value, "stateMachineDsl_Declaration11", None)
                setattr(value, "stateMachineDsl_Declaration11", self)

class stateMachineDsl_ExtDeclaration:

    def __init__(self, name: str, stateMachineDsl_ExtDeclaration: "stateMachineDsl_Declaration" = None, stateMachineDsl_ExtDeclaration43: set["stateMachineDsl_ParameterFunction"] = None):
        self.name = name
        self.stateMachineDsl_ExtDeclaration = stateMachineDsl_ExtDeclaration
        self.stateMachineDsl_ExtDeclaration43 = stateMachineDsl_ExtDeclaration43 if stateMachineDsl_ExtDeclaration43 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachineDsl_ExtDeclaration43(self):
        return self.__stateMachineDsl_ExtDeclaration43

    @stateMachineDsl_ExtDeclaration43.setter
    def stateMachineDsl_ExtDeclaration43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_ExtDeclaration__stateMachineDsl_ExtDeclaration43", None)
        self.__stateMachineDsl_ExtDeclaration43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachineDsl_ParameterFunction"):
                    opp_val = getattr(item, "stateMachineDsl_ParameterFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachineDsl_ParameterFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachineDsl_ParameterFunction"):
                    opp_val = getattr(item, "stateMachineDsl_ParameterFunction", None)
                    
                    setattr(item, "stateMachineDsl_ParameterFunction", self)
                    

    @property
    def stateMachineDsl_ExtDeclaration(self):
        return self.__stateMachineDsl_ExtDeclaration

    @stateMachineDsl_ExtDeclaration.setter
    def stateMachineDsl_ExtDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_ExtDeclaration__stateMachineDsl_ExtDeclaration", None)
        self.__stateMachineDsl_ExtDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Declaration9"):
                opp_val = getattr(old_value, "stateMachineDsl_Declaration9", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Declaration9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Declaration9"):
                opp_val = getattr(value, "stateMachineDsl_Declaration9", None)
                setattr(value, "stateMachineDsl_Declaration9", self)

class stateMachineDsl_Variable:

    pass
class stateMachineDsl_State:

    def __init__(self, name: str, stateMachineDsl_State: "stateMachineDsl_StateMachine" = None, stateMachineDsl_State5: "stateMachineDsl_StateMachine" = None, stateMachineDsl_State15: set["stateMachineDsl_MemberState"] = None, stateMachineDsl_State27: "stateMachineDsl_Transition" = None):
        self.name = name
        self.stateMachineDsl_State = stateMachineDsl_State
        self.stateMachineDsl_State5 = stateMachineDsl_State5
        self.stateMachineDsl_State15 = stateMachineDsl_State15 if stateMachineDsl_State15 is not None else set()
        self.stateMachineDsl_State27 = stateMachineDsl_State27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachineDsl_State15(self):
        return self.__stateMachineDsl_State15

    @stateMachineDsl_State15.setter
    def stateMachineDsl_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_State__stateMachineDsl_State15", None)
        self.__stateMachineDsl_State15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachineDsl_MemberState"):
                    opp_val = getattr(item, "stateMachineDsl_MemberState", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachineDsl_MemberState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachineDsl_MemberState"):
                    opp_val = getattr(item, "stateMachineDsl_MemberState", None)
                    
                    setattr(item, "stateMachineDsl_MemberState", self)
                    

    @property
    def stateMachineDsl_State27(self):
        return self.__stateMachineDsl_State27

    @stateMachineDsl_State27.setter
    def stateMachineDsl_State27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_State__stateMachineDsl_State27", None)
        self.__stateMachineDsl_State27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_Transition26"):
                opp_val = getattr(old_value, "stateMachineDsl_Transition26", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_Transition26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_Transition26"):
                opp_val = getattr(value, "stateMachineDsl_Transition26", None)
                setattr(value, "stateMachineDsl_Transition26", self)

    @property
    def stateMachineDsl_State5(self):
        return self.__stateMachineDsl_State5

    @stateMachineDsl_State5.setter
    def stateMachineDsl_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_State__stateMachineDsl_State5", None)
        self.__stateMachineDsl_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_StateMachine4"):
                opp_val = getattr(old_value, "stateMachineDsl_StateMachine4", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_StateMachine4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_StateMachine4"):
                opp_val = getattr(value, "stateMachineDsl_StateMachine4", None)
                setattr(value, "stateMachineDsl_StateMachine4", self)

    @property
    def stateMachineDsl_State(self):
        return self.__stateMachineDsl_State

    @stateMachineDsl_State.setter
    def stateMachineDsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_State__stateMachineDsl_State", None)
        self.__stateMachineDsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_StateMachine2"):
                opp_val = getattr(old_value, "stateMachineDsl_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_StateMachine2"):
                opp_val = getattr(value, "stateMachineDsl_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "stateMachineDsl_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stateMachineDsl_Declaration:

    pass
class stateMachineDsl_StateMachine:

    def __init__(self, name: str, stateMachineDsl_StateMachine: set["stateMachineDsl_Declaration"] = None, stateMachineDsl_StateMachine2: set["stateMachineDsl_State"] = None, stateMachineDsl_StateMachine4: "stateMachineDsl_State" = None):
        self.name = name
        self.stateMachineDsl_StateMachine = stateMachineDsl_StateMachine if stateMachineDsl_StateMachine is not None else set()
        self.stateMachineDsl_StateMachine2 = stateMachineDsl_StateMachine2 if stateMachineDsl_StateMachine2 is not None else set()
        self.stateMachineDsl_StateMachine4 = stateMachineDsl_StateMachine4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachineDsl_StateMachine4(self):
        return self.__stateMachineDsl_StateMachine4

    @stateMachineDsl_StateMachine4.setter
    def stateMachineDsl_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_StateMachine__stateMachineDsl_StateMachine4", None)
        self.__stateMachineDsl_StateMachine4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineDsl_State5"):
                opp_val = getattr(old_value, "stateMachineDsl_State5", None)
                if opp_val == self:
                    setattr(old_value, "stateMachineDsl_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineDsl_State5"):
                opp_val = getattr(value, "stateMachineDsl_State5", None)
                setattr(value, "stateMachineDsl_State5", self)

    @property
    def stateMachineDsl_StateMachine2(self):
        return self.__stateMachineDsl_StateMachine2

    @stateMachineDsl_StateMachine2.setter
    def stateMachineDsl_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_StateMachine__stateMachineDsl_StateMachine2", None)
        self.__stateMachineDsl_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachineDsl_State"):
                    opp_val = getattr(item, "stateMachineDsl_State", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachineDsl_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachineDsl_State"):
                    opp_val = getattr(item, "stateMachineDsl_State", None)
                    
                    setattr(item, "stateMachineDsl_State", self)
                    

    @property
    def stateMachineDsl_StateMachine(self):
        return self.__stateMachineDsl_StateMachine

    @stateMachineDsl_StateMachine.setter
    def stateMachineDsl_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachineDsl_StateMachine__stateMachineDsl_StateMachine", None)
        self.__stateMachineDsl_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachineDsl_Declaration"):
                    opp_val = getattr(item, "stateMachineDsl_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachineDsl_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachineDsl_Declaration"):
                    opp_val = getattr(item, "stateMachineDsl_Declaration", None)
                    
                    setattr(item, "stateMachineDsl_Declaration", self)
                    
