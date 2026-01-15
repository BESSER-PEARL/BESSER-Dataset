from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class MultiplyDivide:

    pass
class mathinterpreter_Divide(MultiplyDivide):

    pass
class mathinterpreter_Multiply(MultiplyDivide):

    pass
class PlusMinus:

    pass
class mathinterpreter_Minus(PlusMinus):

    pass
class mathinterpreter_Plus(PlusMinus):

    pass
class Number:

    pass
class mathinterpreter_Negative(Number):

    pass
class mathinterpreter_Positive(Number):

    pass
class Primary:

    pass
class mathinterpreter_PMParenthesis(Primary):

    pass
class mathinterpreter_DefParenthesis(Primary):

    pass
class mathinterpreter_Number(Primary):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class mathinterpreter_VariableName(Primary):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class MDExpression:

    pass
class mathinterpreter_Primary(MDExpression):

    pass
class mathinterpreter_MultiplyDivide:

    pass
class mathinterpreter_PlusMinus:

    pass
class PMExpression:

    pass
class mathinterpreter_MDExpression(PMExpression):

    pass
class DefParenthesis:

    pass
class mathinterpreter_PMExpression:

    pass
class mathinterpreter_Variable:

    def __init__(self, name: str, mathinterpreter_Variable9: "mathinterpreter_PMExpression" = None, mathinterpreter_Variable: "mathinterpreter_VariableDefinition" = None, mathinterpreter_Variable4: "mathinterpreter_DefineExpr" = None):
        self.name = name
        self.mathinterpreter_Variable9 = mathinterpreter_Variable9
        self.mathinterpreter_Variable = mathinterpreter_Variable
        self.mathinterpreter_Variable4 = mathinterpreter_Variable4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mathinterpreter_Variable4(self):
        return self.__mathinterpreter_Variable4

    @mathinterpreter_Variable4.setter
    def mathinterpreter_Variable4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathinterpreter_Variable__mathinterpreter_Variable4", None)
        self.__mathinterpreter_Variable4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathinterpreter_DefineExpr"):
                opp_val = getattr(old_value, "mathinterpreter_DefineExpr", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathinterpreter_DefineExpr"):
                opp_val = getattr(value, "mathinterpreter_DefineExpr", None)
                if opp_val is None:
                    setattr(value, "mathinterpreter_DefineExpr", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mathinterpreter_Variable9(self):
        return self.__mathinterpreter_Variable9

    @mathinterpreter_Variable9.setter
    def mathinterpreter_Variable9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathinterpreter_Variable__mathinterpreter_Variable9", None)
        self.__mathinterpreter_Variable9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathinterpreter_PMExpression10"):
                opp_val = getattr(old_value, "mathinterpreter_PMExpression10", None)
                if opp_val == self:
                    setattr(old_value, "mathinterpreter_PMExpression10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathinterpreter_PMExpression10"):
                opp_val = getattr(value, "mathinterpreter_PMExpression10", None)
                setattr(value, "mathinterpreter_PMExpression10", self)

    @property
    def mathinterpreter_Variable(self):
        return self.__mathinterpreter_Variable

    @mathinterpreter_Variable.setter
    def mathinterpreter_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathinterpreter_Variable__mathinterpreter_Variable", None)
        self.__mathinterpreter_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathinterpreter_VariableDefinition"):
                opp_val = getattr(old_value, "mathinterpreter_VariableDefinition", None)
                if opp_val == self:
                    setattr(old_value, "mathinterpreter_VariableDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathinterpreter_VariableDefinition"):
                opp_val = getattr(value, "mathinterpreter_VariableDefinition", None)
                setattr(value, "mathinterpreter_VariableDefinition", self)

class MathExpression:

    pass
class mathinterpreter_Function(MathExpression):

    pass
class mathinterpreter_DefineExpr(MathExpression, DefParenthesis):

    pass
class mathinterpreter_VariableDefinition(MathExpression):

    pass
class mathinterpreter_MathExpression:

    pass
class mathinterpreter_Model:

    pass
class mathinterpreter_EObject:

    pass