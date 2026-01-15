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
class Power:

    pass
class mathinterpreter_Pow(Power):

    pass
class Number:

    pass
class mathinterpreter_Negative(Number):

    pass
class mathinterpreter_Positive(Number):

    pass
class PowExpression:

    pass
class mathinterpreter_MultiplyDivide:

    pass
class mathinterpreter_PlusMinus:

    pass
class mathinterpreter_Power:

    pass
class MDExpression:

    pass
class mathinterpreter_PowExpression(MDExpression):

    pass
class PMExpression:

    pass
class mathinterpreter_MDExpression(PMExpression):

    pass
class mathinterpreter_Variable:

    def __init__(self, name: str, mathinterpreter_Variable: "mathinterpreter_DefineExpr" = None, mathinterpreter_Variable5: "mathinterpreter_PMExpression" = None):
        self.name = name
        self.mathinterpreter_Variable = mathinterpreter_Variable
        self.mathinterpreter_Variable5 = mathinterpreter_Variable5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mathinterpreter_Variable5(self):
        return self.__mathinterpreter_Variable5

    @mathinterpreter_Variable5.setter
    def mathinterpreter_Variable5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathinterpreter_Variable__mathinterpreter_Variable5", None)
        self.__mathinterpreter_Variable5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathinterpreter_PMExpression6"):
                opp_val = getattr(old_value, "mathinterpreter_PMExpression6", None)
                if opp_val == self:
                    setattr(old_value, "mathinterpreter_PMExpression6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathinterpreter_PMExpression6"):
                opp_val = getattr(value, "mathinterpreter_PMExpression6", None)
                setattr(value, "mathinterpreter_PMExpression6", self)

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

class DefParenthesis:

    pass
class MathExpression:

    pass
class mathinterpreter_DefineExpr(DefParenthesis, MathExpression):

    pass
class mathinterpreter_Function(MathExpression):

    pass
class mathinterpreter_PMExpression:

    pass
class mathinterpreter_MathExpression:

    def __init__(self, description: str, mathinterpreter_MathExpression: "mathinterpreter_Model" = None, mathinterpreter_MathExpression2: "mathinterpreter_PMExpression" = None):
        self.description = description
        self.mathinterpreter_MathExpression = mathinterpreter_MathExpression
        self.mathinterpreter_MathExpression2 = mathinterpreter_MathExpression2
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def mathinterpreter_MathExpression2(self):
        return self.__mathinterpreter_MathExpression2

    @mathinterpreter_MathExpression2.setter
    def mathinterpreter_MathExpression2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathinterpreter_MathExpression__mathinterpreter_MathExpression2", None)
        self.__mathinterpreter_MathExpression2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathinterpreter_PMExpression"):
                opp_val = getattr(old_value, "mathinterpreter_PMExpression", None)
                if opp_val == self:
                    setattr(old_value, "mathinterpreter_PMExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathinterpreter_PMExpression"):
                opp_val = getattr(value, "mathinterpreter_PMExpression", None)
                setattr(value, "mathinterpreter_PMExpression", self)

    @property
    def mathinterpreter_MathExpression(self):
        return self.__mathinterpreter_MathExpression

    @mathinterpreter_MathExpression.setter
    def mathinterpreter_MathExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathinterpreter_MathExpression__mathinterpreter_MathExpression", None)
        self.__mathinterpreter_MathExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathinterpreter_Model"):
                opp_val = getattr(old_value, "mathinterpreter_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathinterpreter_Model"):
                opp_val = getattr(value, "mathinterpreter_Model", None)
                if opp_val is None:
                    setattr(value, "mathinterpreter_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mathinterpreter_Model:

    pass
class mathinterpreter_EObject:

    pass
class mathinterpreter_Primary(PowExpression):

    pass
class Primary:

    pass
class mathinterpreter_DefParenthesis(Primary):

    pass
class mathinterpreter_PMParenthesis(Primary):

    pass
class mathinterpreter_VariableName(Primary):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class mathinterpreter_Number(Primary):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class mathinterpreter_External(Primary):

    def __init__(self, name: str, mathinterpreter_External: set["mathinterpreter_Primary"] = None):
        self.name = name
        self.mathinterpreter_External = mathinterpreter_External if mathinterpreter_External is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mathinterpreter_External(self):
        return self.__mathinterpreter_External

    @mathinterpreter_External.setter
    def mathinterpreter_External(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathinterpreter_External__mathinterpreter_External", None)
        self.__mathinterpreter_External = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mathinterpreter_Primary"):
                    opp_val = getattr(item, "mathinterpreter_Primary", None)
                    
                    if opp_val == self:
                        setattr(item, "mathinterpreter_Primary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mathinterpreter_Primary"):
                    opp_val = getattr(item, "mathinterpreter_Primary", None)
                    
                    setattr(item, "mathinterpreter_Primary", self)
                    
