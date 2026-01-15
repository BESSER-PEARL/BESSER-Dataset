from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Exp:

    pass
class mathInterpreter_Minus(Exp):

    pass
class mathInterpreter_Plus(Exp):

    pass
class mathInterpreter_Exp:

    def __init__(self, value: int, mathInterpreter_Exp: "mathInterpreter_MathExp" = None, mathInterpreter_Exp3: "mathInterpreter_Exp" = None, mathInterpreter_Exp1: "mathInterpreter_Exp" = None, mathInterpreter_Exp6: "mathInterpreter_Exp" = None, mathInterpreter_Exp4: "mathInterpreter_Exp" = None, mathInterpreter_Exp9: "mathInterpreter_Exp" = None, mathInterpreter_Exp7: "mathInterpreter_Exp" = None):
        self.value = value
        self.mathInterpreter_Exp = mathInterpreter_Exp
        self.mathInterpreter_Exp3 = mathInterpreter_Exp3
        self.mathInterpreter_Exp1 = mathInterpreter_Exp1
        self.mathInterpreter_Exp6 = mathInterpreter_Exp6
        self.mathInterpreter_Exp4 = mathInterpreter_Exp4
        self.mathInterpreter_Exp9 = mathInterpreter_Exp9
        self.mathInterpreter_Exp7 = mathInterpreter_Exp7
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def mathInterpreter_Exp7(self):
        return self.__mathInterpreter_Exp7

    @mathInterpreter_Exp7.setter
    def mathInterpreter_Exp7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_Exp__mathInterpreter_Exp7", None)
        self.__mathInterpreter_Exp7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_Exp9"):
                opp_val = getattr(old_value, "mathInterpreter_Exp9", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_Exp9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_Exp9"):
                opp_val = getattr(value, "mathInterpreter_Exp9", None)
                setattr(value, "mathInterpreter_Exp9", self)

    @property
    def mathInterpreter_Exp4(self):
        return self.__mathInterpreter_Exp4

    @mathInterpreter_Exp4.setter
    def mathInterpreter_Exp4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_Exp__mathInterpreter_Exp4", None)
        self.__mathInterpreter_Exp4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_Exp6"):
                opp_val = getattr(old_value, "mathInterpreter_Exp6", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_Exp6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_Exp6"):
                opp_val = getattr(value, "mathInterpreter_Exp6", None)
                setattr(value, "mathInterpreter_Exp6", self)

    @property
    def mathInterpreter_Exp1(self):
        return self.__mathInterpreter_Exp1

    @mathInterpreter_Exp1.setter
    def mathInterpreter_Exp1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_Exp__mathInterpreter_Exp1", None)
        self.__mathInterpreter_Exp1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_Exp3"):
                opp_val = getattr(old_value, "mathInterpreter_Exp3", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_Exp3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_Exp3"):
                opp_val = getattr(value, "mathInterpreter_Exp3", None)
                setattr(value, "mathInterpreter_Exp3", self)

    @property
    def mathInterpreter_Exp3(self):
        return self.__mathInterpreter_Exp3

    @mathInterpreter_Exp3.setter
    def mathInterpreter_Exp3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_Exp__mathInterpreter_Exp3", None)
        self.__mathInterpreter_Exp3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_Exp1"):
                opp_val = getattr(old_value, "mathInterpreter_Exp1", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_Exp1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_Exp1"):
                opp_val = getattr(value, "mathInterpreter_Exp1", None)
                setattr(value, "mathInterpreter_Exp1", self)

    @property
    def mathInterpreter_Exp9(self):
        return self.__mathInterpreter_Exp9

    @mathInterpreter_Exp9.setter
    def mathInterpreter_Exp9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_Exp__mathInterpreter_Exp9", None)
        self.__mathInterpreter_Exp9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_Exp7"):
                opp_val = getattr(old_value, "mathInterpreter_Exp7", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_Exp7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_Exp7"):
                opp_val = getattr(value, "mathInterpreter_Exp7", None)
                setattr(value, "mathInterpreter_Exp7", self)

    @property
    def mathInterpreter_Exp6(self):
        return self.__mathInterpreter_Exp6

    @mathInterpreter_Exp6.setter
    def mathInterpreter_Exp6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_Exp__mathInterpreter_Exp6", None)
        self.__mathInterpreter_Exp6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_Exp4"):
                opp_val = getattr(old_value, "mathInterpreter_Exp4", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_Exp4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_Exp4"):
                opp_val = getattr(value, "mathInterpreter_Exp4", None)
                setattr(value, "mathInterpreter_Exp4", self)

    @property
    def mathInterpreter_Exp(self):
        return self.__mathInterpreter_Exp

    @mathInterpreter_Exp.setter
    def mathInterpreter_Exp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mathInterpreter_Exp__mathInterpreter_Exp", None)
        self.__mathInterpreter_Exp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mathInterpreter_MathExp"):
                opp_val = getattr(old_value, "mathInterpreter_MathExp", None)
                if opp_val == self:
                    setattr(old_value, "mathInterpreter_MathExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mathInterpreter_MathExp"):
                opp_val = getattr(value, "mathInterpreter_MathExp", None)
                setattr(value, "mathInterpreter_MathExp", self)

class mathInterpreter_MathExp:

    pass
class mathInterpreter_Div(Exp):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class mathInterpreter_Mult(Exp):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op
