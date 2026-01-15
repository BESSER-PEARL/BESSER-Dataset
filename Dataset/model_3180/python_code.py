from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class expressionDSL_BooleanConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressionDSL_UnaryMinus(Expression):

    pass
class expressionDSL_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressionDSL_BinaryMinus(Expression):

    pass
class expressionDSL_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class expressionDSL_And(Expression):

    pass
class expressionDSL_Not(Expression):

    pass
class expressionDSL_MulOrDiv(Expression):

    def __init__(self, op: str, expressionDSL_MulOrDiv: "expressionDSL_Expression" = None, expressionDSL_MulOrDiv52: "expressionDSL_Expression" = None):
        self.op = op
        self.expressionDSL_MulOrDiv = expressionDSL_MulOrDiv
        self.expressionDSL_MulOrDiv52 = expressionDSL_MulOrDiv52
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expressionDSL_MulOrDiv52(self):
        return self.__expressionDSL_MulOrDiv52

    @expressionDSL_MulOrDiv52.setter
    def expressionDSL_MulOrDiv52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_MulOrDiv__expressionDSL_MulOrDiv52", None)
        self.__expressionDSL_MulOrDiv52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_Expression53"):
                opp_val = getattr(old_value, "expressionDSL_Expression53", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_Expression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_Expression53"):
                opp_val = getattr(value, "expressionDSL_Expression53", None)
                setattr(value, "expressionDSL_Expression53", self)

    @property
    def expressionDSL_MulOrDiv(self):
        return self.__expressionDSL_MulOrDiv

    @expressionDSL_MulOrDiv.setter
    def expressionDSL_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_MulOrDiv__expressionDSL_MulOrDiv", None)
        self.__expressionDSL_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_Expression50"):
                opp_val = getattr(old_value, "expressionDSL_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_Expression50"):
                opp_val = getattr(value, "expressionDSL_Expression50", None)
                setattr(value, "expressionDSL_Expression50", self)

class expressionDSL_UnaryPlus(Expression):

    pass
class expressionDSL_QualifiedRef(Expression):

    pass
class expressionDSL_Exponent(Expression):

    pass
class expressionDSL_Or(Expression):

    pass
class expressionDSL_VariableArrayOrFunctionRef(Expression):

    pass
class expressionDSL_Named:

    def __init__(self, name: str, expressionDSL_Named: "expressionDSL_VariableArrayOrFunctionRef" = None):
        self.name = name
        self.expressionDSL_Named = expressionDSL_Named
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expressionDSL_Named(self):
        return self.__expressionDSL_Named

    @expressionDSL_Named.setter
    def expressionDSL_Named(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_Named__expressionDSL_Named", None)
        self.__expressionDSL_Named = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_VariableArrayOrFunctionRef"):
                opp_val = getattr(old_value, "expressionDSL_VariableArrayOrFunctionRef", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_VariableArrayOrFunctionRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_VariableArrayOrFunctionRef"):
                opp_val = getattr(value, "expressionDSL_VariableArrayOrFunctionRef", None)
                setattr(value, "expressionDSL_VariableArrayOrFunctionRef", self)

class expressionDSL_FunctionCall:

    pass
class expressionDSL_Expression:

    pass
class expressionDSL_BinaryPlus(Expression):

    pass
class expressionDSL_Comparison(Expression):

    def __init__(self, op: str, expressionDSL_Comparison: "expressionDSL_Expression" = None, expressionDSL_Comparison37: "expressionDSL_Expression" = None):
        self.op = op
        self.expressionDSL_Comparison = expressionDSL_Comparison
        self.expressionDSL_Comparison37 = expressionDSL_Comparison37
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expressionDSL_Comparison37(self):
        return self.__expressionDSL_Comparison37

    @expressionDSL_Comparison37.setter
    def expressionDSL_Comparison37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_Comparison__expressionDSL_Comparison37", None)
        self.__expressionDSL_Comparison37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_Expression38"):
                opp_val = getattr(old_value, "expressionDSL_Expression38", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_Expression38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_Expression38"):
                opp_val = getattr(value, "expressionDSL_Expression38", None)
                setattr(value, "expressionDSL_Expression38", self)

    @property
    def expressionDSL_Comparison(self):
        return self.__expressionDSL_Comparison

    @expressionDSL_Comparison.setter
    def expressionDSL_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_Comparison__expressionDSL_Comparison", None)
        self.__expressionDSL_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_Expression35"):
                opp_val = getattr(old_value, "expressionDSL_Expression35", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_Expression35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_Expression35"):
                opp_val = getattr(value, "expressionDSL_Expression35", None)
                setattr(value, "expressionDSL_Expression35", self)

class expressionDSL_SubField:

    pass
class SubField:

    pass
class expressionDSL_Dim:

    def __init__(self, arrayDimensions: int, expressionDSL_Dim9: "expressionDSL_SubFieldDef" = None, expressionDSL_Dim: "expressionDSL_VariableDef" = None, expressionDSL_Dim3: "expressionDSL_ConstDef" = None, expressionDSL_Dim5: "expressionDSL_StructDef" = None):
        self.arrayDimensions = arrayDimensions
        self.expressionDSL_Dim9 = expressionDSL_Dim9
        self.expressionDSL_Dim = expressionDSL_Dim
        self.expressionDSL_Dim3 = expressionDSL_Dim3
        self.expressionDSL_Dim5 = expressionDSL_Dim5
        
    @property
    def arrayDimensions(self) -> int:
        return self.__arrayDimensions

    @arrayDimensions.setter
    def arrayDimensions(self, arrayDimensions: int):
        self.__arrayDimensions = arrayDimensions

    @property
    def expressionDSL_Dim9(self):
        return self.__expressionDSL_Dim9

    @expressionDSL_Dim9.setter
    def expressionDSL_Dim9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_Dim__expressionDSL_Dim9", None)
        self.__expressionDSL_Dim9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_SubFieldDef"):
                opp_val = getattr(old_value, "expressionDSL_SubFieldDef", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_SubFieldDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_SubFieldDef"):
                opp_val = getattr(value, "expressionDSL_SubFieldDef", None)
                setattr(value, "expressionDSL_SubFieldDef", self)

    @property
    def expressionDSL_Dim3(self):
        return self.__expressionDSL_Dim3

    @expressionDSL_Dim3.setter
    def expressionDSL_Dim3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_Dim__expressionDSL_Dim3", None)
        self.__expressionDSL_Dim3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_ConstDef"):
                opp_val = getattr(old_value, "expressionDSL_ConstDef", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_ConstDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_ConstDef"):
                opp_val = getattr(value, "expressionDSL_ConstDef", None)
                setattr(value, "expressionDSL_ConstDef", self)

    @property
    def expressionDSL_Dim(self):
        return self.__expressionDSL_Dim

    @expressionDSL_Dim.setter
    def expressionDSL_Dim(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_Dim__expressionDSL_Dim", None)
        self.__expressionDSL_Dim = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_VariableDef"):
                opp_val = getattr(old_value, "expressionDSL_VariableDef", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_VariableDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_VariableDef"):
                opp_val = getattr(value, "expressionDSL_VariableDef", None)
                setattr(value, "expressionDSL_VariableDef", self)

    @property
    def expressionDSL_Dim5(self):
        return self.__expressionDSL_Dim5

    @expressionDSL_Dim5.setter
    def expressionDSL_Dim5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_Dim__expressionDSL_Dim5", None)
        self.__expressionDSL_Dim5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_StructDef"):
                opp_val = getattr(old_value, "expressionDSL_StructDef", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_StructDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_StructDef"):
                opp_val = getattr(value, "expressionDSL_StructDef", None)
                setattr(value, "expressionDSL_StructDef", self)

class Named:

    pass
class Statement:

    pass
class expressionDSL_StructDef(Statement, SubField, Named):

    pass
class expressionDSL_FunctionCallStatement(Statement):

    pass
class expressionDSL_ConstDef(Statement, Named):

    def __init__(self, type: str, expressionDSL_ConstDef: "expressionDSL_Dim" = None):
        self.type = type
        self.expressionDSL_ConstDef = expressionDSL_ConstDef
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def expressionDSL_ConstDef(self):
        return self.__expressionDSL_ConstDef

    @expressionDSL_ConstDef.setter
    def expressionDSL_ConstDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_ConstDef__expressionDSL_ConstDef", None)
        self.__expressionDSL_ConstDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_Dim3"):
                opp_val = getattr(old_value, "expressionDSL_Dim3", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_Dim3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_Dim3"):
                opp_val = getattr(value, "expressionDSL_Dim3", None)
                setattr(value, "expressionDSL_Dim3", self)

class expressionDSL_VariableDef(Statement, Named):

    def __init__(self, type: str, expressionDSL_VariableDef: "expressionDSL_Dim" = None, expressionDSL_VariableDef11: "expressionDSL_VariableAssignment" = None):
        self.type = type
        self.expressionDSL_VariableDef = expressionDSL_VariableDef
        self.expressionDSL_VariableDef11 = expressionDSL_VariableDef11
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def expressionDSL_VariableDef11(self):
        return self.__expressionDSL_VariableDef11

    @expressionDSL_VariableDef11.setter
    def expressionDSL_VariableDef11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_VariableDef__expressionDSL_VariableDef11", None)
        self.__expressionDSL_VariableDef11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_VariableAssignment"):
                opp_val = getattr(old_value, "expressionDSL_VariableAssignment", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_VariableAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_VariableAssignment"):
                opp_val = getattr(value, "expressionDSL_VariableAssignment", None)
                setattr(value, "expressionDSL_VariableAssignment", self)

    @property
    def expressionDSL_VariableDef(self):
        return self.__expressionDSL_VariableDef

    @expressionDSL_VariableDef.setter
    def expressionDSL_VariableDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_VariableDef__expressionDSL_VariableDef", None)
        self.__expressionDSL_VariableDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_Dim"):
                opp_val = getattr(old_value, "expressionDSL_Dim", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_Dim", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_Dim"):
                opp_val = getattr(value, "expressionDSL_Dim", None)
                setattr(value, "expressionDSL_Dim", self)

class expressionDSL_Statement:

    pass
class expressionDSL_Model:

    pass
class expressionDSL_VariableAssignment(Statement):

    def __init__(self, op: str, expressionDSL_VariableAssignment: "expressionDSL_VariableDef" = None, expressionDSL_VariableAssignment13: "expressionDSL_Expression" = None):
        self.op = op
        self.expressionDSL_VariableAssignment = expressionDSL_VariableAssignment
        self.expressionDSL_VariableAssignment13 = expressionDSL_VariableAssignment13
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expressionDSL_VariableAssignment(self):
        return self.__expressionDSL_VariableAssignment

    @expressionDSL_VariableAssignment.setter
    def expressionDSL_VariableAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_VariableAssignment__expressionDSL_VariableAssignment", None)
        self.__expressionDSL_VariableAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_VariableDef11"):
                opp_val = getattr(old_value, "expressionDSL_VariableDef11", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_VariableDef11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_VariableDef11"):
                opp_val = getattr(value, "expressionDSL_VariableDef11", None)
                setattr(value, "expressionDSL_VariableDef11", self)

    @property
    def expressionDSL_VariableAssignment13(self):
        return self.__expressionDSL_VariableAssignment13

    @expressionDSL_VariableAssignment13.setter
    def expressionDSL_VariableAssignment13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_VariableAssignment__expressionDSL_VariableAssignment13", None)
        self.__expressionDSL_VariableAssignment13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_Expression"):
                opp_val = getattr(old_value, "expressionDSL_Expression", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_Expression"):
                opp_val = getattr(value, "expressionDSL_Expression", None)
                setattr(value, "expressionDSL_Expression", self)

class expressionDSL_FunctionDef(Statement, Named):

    def __init__(self, type: str, expressionDSL_FunctionDef: "expressionDSL_FunctionCall" = None):
        self.type = type
        self.expressionDSL_FunctionDef = expressionDSL_FunctionDef
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def expressionDSL_FunctionDef(self):
        return self.__expressionDSL_FunctionDef

    @expressionDSL_FunctionDef.setter
    def expressionDSL_FunctionDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_FunctionDef__expressionDSL_FunctionDef", None)
        self.__expressionDSL_FunctionDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_FunctionCall16"):
                opp_val = getattr(old_value, "expressionDSL_FunctionCall16", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_FunctionCall16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_FunctionCall16"):
                opp_val = getattr(value, "expressionDSL_FunctionCall16", None)
                setattr(value, "expressionDSL_FunctionCall16", self)

class expressionDSL_SubFieldDef(SubField, Named):

    def __init__(self, type: str, expressionDSL_SubFieldDef: "expressionDSL_Dim" = None):
        self.type = type
        self.expressionDSL_SubFieldDef = expressionDSL_SubFieldDef
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def expressionDSL_SubFieldDef(self):
        return self.__expressionDSL_SubFieldDef

    @expressionDSL_SubFieldDef.setter
    def expressionDSL_SubFieldDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressionDSL_SubFieldDef__expressionDSL_SubFieldDef", None)
        self.__expressionDSL_SubFieldDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressionDSL_Dim9"):
                opp_val = getattr(old_value, "expressionDSL_Dim9", None)
                if opp_val == self:
                    setattr(old_value, "expressionDSL_Dim9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressionDSL_Dim9"):
                opp_val = getattr(value, "expressionDSL_Dim9", None)
                setattr(value, "expressionDSL_Dim9", self)
