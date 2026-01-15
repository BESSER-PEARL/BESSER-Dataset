from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Primary:

    pass
class mathInterpreter_Num(Primary):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class MultiplyOrDivide:

    pass
class mathInterpreter_Divide(MultiplyOrDivide):

    pass
class mathInterpreter_Multiply(MultiplyOrDivide):

    pass
class PlusOrMinus:

    pass
class mathInterpreter_Minus(PlusOrMinus):

    pass
class mathInterpreter_Plus(PlusOrMinus):

    pass
class mathInterpreter_Bracket(Primary):

    pass
class mathInterpreter_VariableRef(Primary):

    pass
class mathInterpreter_Primary:

    pass
class mathInterpreter_MultiplyOrDivide:

    def __init__(self, operator: str, mathInterpreter_MultiplyOrDivide: "mathInterpreter_PlusOrMinus" = None, mathInterpreter_MultiplyOrDivide13: "mathInterpreter_EObject" = None, mathInterpreter_MultiplyOrDivide16: "mathInterpreter_Primary" = None):
        self.operator = operator
        self.mathInterpreter_MultiplyOrDivide = mathInterpreter_MultiplyOrDivide
        self.mathInterpreter_MultiplyOrDivide13 = mathInterpreter_MultiplyOrDivide13
        self.mathInterpreter_MultiplyOrDivide16 = mathInterpreter_MultiplyOrDivide16
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def mathInterpreter_MultiplyOrDivide(self):
        return self.__mathInterpreter_MultiplyOrDivide

    @mathInterpreter_MultiplyOrDivide.setter
    def mathInterpreter_MultiplyOrDivide(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_MultiplyOrDivide__mathInterpreter_MultiplyOrDivide", None)
        self.__mathInterpreter_MultiplyOrDivide = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_PlusOrMinus11"):
                opp_val = getattr(old_value, "mathInterpreter_PlusOrMinus11", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_PlusOrMinus11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_PlusOrMinus11"):
                opp_val = getattr(value, "mathInterpreter_PlusOrMinus11", None)
                setattr(value, "mathInterpreter_PlusOrMinus11", self)

    @property
    def mathInterpreter_MultiplyOrDivide13(self):
        return self.__mathInterpreter_MultiplyOrDivide13

    @mathInterpreter_MultiplyOrDivide13.setter
    def mathInterpreter_MultiplyOrDivide13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_MultiplyOrDivide__mathInterpreter_MultiplyOrDivide13", None)
        self.__mathInterpreter_MultiplyOrDivide13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_EObject14"):
                opp_val = getattr(old_value, "mathInterpreter_EObject14", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_EObject14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_EObject14"):
                opp_val = getattr(value, "mathInterpreter_EObject14", None)
                setattr(value, "mathInterpreter_EObject14", self)

    @property
    def mathInterpreter_MultiplyOrDivide16(self):
        return self.__mathInterpreter_MultiplyOrDivide16

    @mathInterpreter_MultiplyOrDivide16.setter
    def mathInterpreter_MultiplyOrDivide16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_MultiplyOrDivide__mathInterpreter_MultiplyOrDivide16", None)
        self.__mathInterpreter_MultiplyOrDivide16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_Primary"):
                opp_val = getattr(old_value, "mathInterpreter_Primary", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_Primary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_Primary"):
                opp_val = getattr(value, "mathInterpreter_Primary", None)
                setattr(value, "mathInterpreter_Primary", self)

class mathInterpreter_EObject:

    pass
class mathInterpreter_PlusOrMinus:

    def __init__(self, operator: str, mathInterpreter_PlusOrMinus: "mathInterpreter_Expression" = None, mathInterpreter_PlusOrMinus9: "mathInterpreter_EObject" = None, mathInterpreter_PlusOrMinus11: "mathInterpreter_MultiplyOrDivide" = None):
        self.operator = operator
        self.mathInterpreter_PlusOrMinus = mathInterpreter_PlusOrMinus
        self.mathInterpreter_PlusOrMinus9 = mathInterpreter_PlusOrMinus9
        self.mathInterpreter_PlusOrMinus11 = mathInterpreter_PlusOrMinus11
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def mathInterpreter_PlusOrMinus9(self):
        return self.__mathInterpreter_PlusOrMinus9

    @mathInterpreter_PlusOrMinus9.setter
    def mathInterpreter_PlusOrMinus9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_PlusOrMinus__mathInterpreter_PlusOrMinus9", None)
        self.__mathInterpreter_PlusOrMinus9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_EObject"):
                opp_val = getattr(old_value, "mathInterpreter_EObject", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_EObject"):
                opp_val = getattr(value, "mathInterpreter_EObject", None)
                setattr(value, "mathInterpreter_EObject", self)

    @property
    def mathInterpreter_PlusOrMinus(self):
        return self.__mathInterpreter_PlusOrMinus

    @mathInterpreter_PlusOrMinus.setter
    def mathInterpreter_PlusOrMinus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_PlusOrMinus__mathInterpreter_PlusOrMinus", None)
        self.__mathInterpreter_PlusOrMinus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_Expression7"):
                opp_val = getattr(old_value, "mathInterpreter_Expression7", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_Expression7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_Expression7"):
                opp_val = getattr(value, "mathInterpreter_Expression7", None)
                setattr(value, "mathInterpreter_Expression7", self)

    @property
    def mathInterpreter_PlusOrMinus11(self):
        return self.__mathInterpreter_PlusOrMinus11

    @mathInterpreter_PlusOrMinus11.setter
    def mathInterpreter_PlusOrMinus11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_PlusOrMinus__mathInterpreter_PlusOrMinus11", None)
        self.__mathInterpreter_PlusOrMinus11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_MultiplyOrDivide"):
                opp_val = getattr(old_value, "mathInterpreter_MultiplyOrDivide", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_MultiplyOrDivide", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_MultiplyOrDivide"):
                opp_val = getattr(value, "mathInterpreter_MultiplyOrDivide", None)
                setattr(value, "mathInterpreter_MultiplyOrDivide", self)

class mathInterpreter_Expression:

    pass
class mathInterpreter_Variable:

    def __init__(self, name: str, mathInterpreter_Variable: "mathInterpreter_Solution" = None, mathInterpreter_Variable4: "mathInterpreter_Expression" = None, mathInterpreter_Variable18: "mathInterpreter_VariableRef" = None):
        self.name = name
        self.mathInterpreter_Variable = mathInterpreter_Variable
        self.mathInterpreter_Variable4 = mathInterpreter_Variable4
        self.mathInterpreter_Variable18 = mathInterpreter_Variable18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mathInterpreter_Variable4(self):
        return self.__mathInterpreter_Variable4

    @mathInterpreter_Variable4.setter
    def mathInterpreter_Variable4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_Variable__mathInterpreter_Variable4", None)
        self.__mathInterpreter_Variable4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_Expression5"):
                opp_val = getattr(old_value, "mathInterpreter_Expression5", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_Expression5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_Expression5"):
                opp_val = getattr(value, "mathInterpreter_Expression5", None)
                setattr(value, "mathInterpreter_Expression5", self)

    @property
    def mathInterpreter_Variable18(self):
        return self.__mathInterpreter_Variable18

    @mathInterpreter_Variable18.setter
    def mathInterpreter_Variable18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_Variable__mathInterpreter_Variable18", None)
        self.__mathInterpreter_Variable18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_VariableRef"):
                opp_val = getattr(old_value, "mathInterpreter_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_VariableRef"):
                opp_val = getattr(value, "mathInterpreter_VariableRef", None)
                setattr(value, "mathInterpreter_VariableRef", self)

    @property
    def mathInterpreter_Variable(self):
        return self.__mathInterpreter_Variable

    @mathInterpreter_Variable.setter
    def mathInterpreter_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_Variable__mathInterpreter_Variable", None)
        self.__mathInterpreter_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_Solution"):
                opp_val = getattr(old_value, "mathInterpreter_Solution", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_Solution"):
                opp_val = getattr(value, "mathInterpreter_Solution", None)
                if opp_val is None:
                    setattr(value, "mathInterpreter_Solution", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mathInterpreter_Solution:

    pass