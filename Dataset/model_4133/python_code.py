from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class mathCompiler_Minus(Expression):

    pass
class mathCompiler_Plus(Expression):

    pass
class mathCompiler_Expression:

    pass
class mathCompiler_Num(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class mathCompiler_Let(Expression):

    def __init__(self, id: str, mathCompiler_Let: "mathCompiler_Expression" = None, mathCompiler_Let26: "mathCompiler_Expression" = None):
        self.id = id
        self.mathCompiler_Let = mathCompiler_Let
        self.mathCompiler_Let26 = mathCompiler_Let26
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def mathCompiler_Let(self):
        return self.__mathCompiler_Let

    @mathCompiler_Let.setter
    def mathCompiler_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathCompiler_Let__mathCompiler_Let", None)
        self.__mathCompiler_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathCompiler_Expression24"):
                opp_val = getattr(old_value, "mathCompiler_Expression24", None)
                if opp_val == self:
                    setattr(old_value, "mathCompiler_Expression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathCompiler_Expression24"):
                opp_val = getattr(value, "mathCompiler_Expression24", None)
                setattr(value, "mathCompiler_Expression24", self)

    @property
    def mathCompiler_Let26(self):
        return self.__mathCompiler_Let26

    @mathCompiler_Let26.setter
    def mathCompiler_Let26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathCompiler_Let__mathCompiler_Let26", None)
        self.__mathCompiler_Let26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathCompiler_Expression27"):
                opp_val = getattr(old_value, "mathCompiler_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "mathCompiler_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathCompiler_Expression27"):
                opp_val = getattr(value, "mathCompiler_Expression27", None)
                setattr(value, "mathCompiler_Expression27", self)

class mathCompiler_Var(Expression):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class mathCompiler_External(Expression):

    def __init__(self, base: int, exponent: int):
        self.base = base
        self.exponent = exponent
        
    @property
    def exponent(self) -> int:
        return self.__exponent

    @exponent.setter
    def exponent(self, exponent: int):
        self.__exponent = exponent

    @property
    def base(self) -> int:
        return self.__base

    @base.setter
    def base(self, base: int):
        self.__base = base

class mathCompiler_Div(Expression):

    pass
class mathCompiler_Mult(Expression):

    pass
class mathCompiler_MathExp:

    def __init__(self, line: str, mathCompiler_MathExp: "mathCompiler_Expressions" = None, mathCompiler_MathExp2: "mathCompiler_Expression" = None):
        self.line = line
        self.mathCompiler_MathExp = mathCompiler_MathExp
        self.mathCompiler_MathExp2 = mathCompiler_MathExp2
        
    @property
    def line(self) -> str:
        return self.__line

    @line.setter
    def line(self, line: str):
        self.__line = line

    @property
    def mathCompiler_MathExp2(self):
        return self.__mathCompiler_MathExp2

    @mathCompiler_MathExp2.setter
    def mathCompiler_MathExp2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathCompiler_MathExp__mathCompiler_MathExp2", None)
        self.__mathCompiler_MathExp2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathCompiler_Expression"):
                opp_val = getattr(old_value, "mathCompiler_Expression", None)
                if opp_val == self:
                    setattr(old_value, "mathCompiler_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathCompiler_Expression"):
                opp_val = getattr(value, "mathCompiler_Expression", None)
                setattr(value, "mathCompiler_Expression", self)

    @property
    def mathCompiler_MathExp(self):
        return self.__mathCompiler_MathExp

    @mathCompiler_MathExp.setter
    def mathCompiler_MathExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathCompiler_MathExp__mathCompiler_MathExp", None)
        self.__mathCompiler_MathExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathCompiler_Expressions"):
                opp_val = getattr(old_value, "mathCompiler_Expressions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathCompiler_Expressions"):
                opp_val = getattr(value, "mathCompiler_Expressions", None)
                if opp_val is None:
                    setattr(value, "mathCompiler_Expressions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mathCompiler_Expressions:

    pass