from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class BoolExpr:

    pass
class calculatrice_Boolean(BoolExpr):

    def __init__(self, BoolValue: str):
        self.BoolValue = BoolValue
        
    @property
    def BoolValue(self) -> str:
        return self.__BoolValue

    @BoolValue.setter
    def BoolValue(self, BoolValue: str):
        self.__BoolValue = BoolValue

class CalcExpr:

    pass
class calculatrice_VarCall(CalcExpr):

    def __init__(self, varCall: str):
        self.varCall = varCall
        
    @property
    def varCall(self) -> str:
        return self.__varCall

    @varCall.setter
    def varCall(self, varCall: str):
        self.__varCall = varCall

class calculatrice_Number(CalcExpr):

    def __init__(self, neg: bool, value: int):
        self.neg = neg
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def neg(self) -> bool:
        return self.__neg

    @neg.setter
    def neg(self, neg: bool):
        self.__neg = neg

class Condition:

    pass
class Calc:

    pass
class calculatrice_Condition(Calc):

    pass
class calculatrice_CalcExpr:

    def __init__(self, op: str, calculatrice_CalcExpr: "calculatrice_Calc" = None, calculatrice_CalcExpr7: "calculatrice_CalcExpr" = None, calculatrice_CalcExpr5: "calculatrice_CalcExpr" = None, calculatrice_CalcExpr10: "calculatrice_CalcExpr" = None, calculatrice_CalcExpr8: "calculatrice_CalcExpr" = None):
        self.op = op
        self.calculatrice_CalcExpr = calculatrice_CalcExpr
        self.calculatrice_CalcExpr7 = calculatrice_CalcExpr7
        self.calculatrice_CalcExpr5 = calculatrice_CalcExpr5
        self.calculatrice_CalcExpr10 = calculatrice_CalcExpr10
        self.calculatrice_CalcExpr8 = calculatrice_CalcExpr8
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def calculatrice_CalcExpr5(self):
        return self.__calculatrice_CalcExpr5

    @calculatrice_CalcExpr5.setter
    def calculatrice_CalcExpr5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_CalcExpr__calculatrice_CalcExpr5", None)
        self.__calculatrice_CalcExpr5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_CalcExpr7"):
                opp_val = getattr(old_value, "calculatrice_CalcExpr7", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_CalcExpr7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_CalcExpr7"):
                opp_val = getattr(value, "calculatrice_CalcExpr7", None)
                setattr(value, "calculatrice_CalcExpr7", self)

    @property
    def calculatrice_CalcExpr10(self):
        return self.__calculatrice_CalcExpr10

    @calculatrice_CalcExpr10.setter
    def calculatrice_CalcExpr10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_CalcExpr__calculatrice_CalcExpr10", None)
        self.__calculatrice_CalcExpr10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_CalcExpr8"):
                opp_val = getattr(old_value, "calculatrice_CalcExpr8", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_CalcExpr8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_CalcExpr8"):
                opp_val = getattr(value, "calculatrice_CalcExpr8", None)
                setattr(value, "calculatrice_CalcExpr8", self)

    @property
    def calculatrice_CalcExpr7(self):
        return self.__calculatrice_CalcExpr7

    @calculatrice_CalcExpr7.setter
    def calculatrice_CalcExpr7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_CalcExpr__calculatrice_CalcExpr7", None)
        self.__calculatrice_CalcExpr7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_CalcExpr5"):
                opp_val = getattr(old_value, "calculatrice_CalcExpr5", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_CalcExpr5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_CalcExpr5"):
                opp_val = getattr(value, "calculatrice_CalcExpr5", None)
                setattr(value, "calculatrice_CalcExpr5", self)

    @property
    def calculatrice_CalcExpr8(self):
        return self.__calculatrice_CalcExpr8

    @calculatrice_CalcExpr8.setter
    def calculatrice_CalcExpr8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_CalcExpr__calculatrice_CalcExpr8", None)
        self.__calculatrice_CalcExpr8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_CalcExpr10"):
                opp_val = getattr(old_value, "calculatrice_CalcExpr10", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_CalcExpr10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_CalcExpr10"):
                opp_val = getattr(value, "calculatrice_CalcExpr10", None)
                setattr(value, "calculatrice_CalcExpr10", self)

    @property
    def calculatrice_CalcExpr(self):
        return self.__calculatrice_CalcExpr

    @calculatrice_CalcExpr.setter
    def calculatrice_CalcExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_CalcExpr__calculatrice_CalcExpr", None)
        self.__calculatrice_CalcExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_Calc4"):
                opp_val = getattr(old_value, "calculatrice_Calc4", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_Calc4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_Calc4"):
                opp_val = getattr(value, "calculatrice_Calc4", None)
                setattr(value, "calculatrice_Calc4", self)

class calculatrice_BoolExpr(Condition):

    def __init__(self, op: str, calculatrice_BoolExpr: "calculatrice_Calc" = None, calculatrice_BoolExpr22: "calculatrice_BoolExpr" = None, calculatrice_BoolExpr20: "calculatrice_BoolExpr" = None, calculatrice_BoolExpr12: "calculatrice_Calc" = None, calculatrice_BoolExpr15: "calculatrice_Calc" = None, calculatrice_BoolExpr19: "calculatrice_BoolExpr" = None, calculatrice_BoolExpr17: "calculatrice_BoolExpr" = None):
        self.op = op
        self.calculatrice_BoolExpr = calculatrice_BoolExpr
        self.calculatrice_BoolExpr22 = calculatrice_BoolExpr22
        self.calculatrice_BoolExpr20 = calculatrice_BoolExpr20
        self.calculatrice_BoolExpr12 = calculatrice_BoolExpr12
        self.calculatrice_BoolExpr15 = calculatrice_BoolExpr15
        self.calculatrice_BoolExpr19 = calculatrice_BoolExpr19
        self.calculatrice_BoolExpr17 = calculatrice_BoolExpr17
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def calculatrice_BoolExpr22(self):
        return self.__calculatrice_BoolExpr22

    @calculatrice_BoolExpr22.setter
    def calculatrice_BoolExpr22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_BoolExpr__calculatrice_BoolExpr22", None)
        self.__calculatrice_BoolExpr22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_BoolExpr20"):
                opp_val = getattr(old_value, "calculatrice_BoolExpr20", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_BoolExpr20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_BoolExpr20"):
                opp_val = getattr(value, "calculatrice_BoolExpr20", None)
                setattr(value, "calculatrice_BoolExpr20", self)

    @property
    def calculatrice_BoolExpr12(self):
        return self.__calculatrice_BoolExpr12

    @calculatrice_BoolExpr12.setter
    def calculatrice_BoolExpr12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_BoolExpr__calculatrice_BoolExpr12", None)
        self.__calculatrice_BoolExpr12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_Calc13"):
                opp_val = getattr(old_value, "calculatrice_Calc13", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_Calc13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_Calc13"):
                opp_val = getattr(value, "calculatrice_Calc13", None)
                setattr(value, "calculatrice_Calc13", self)

    @property
    def calculatrice_BoolExpr(self):
        return self.__calculatrice_BoolExpr

    @calculatrice_BoolExpr.setter
    def calculatrice_BoolExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_BoolExpr__calculatrice_BoolExpr", None)
        self.__calculatrice_BoolExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_Calc2"):
                opp_val = getattr(old_value, "calculatrice_Calc2", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_Calc2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_Calc2"):
                opp_val = getattr(value, "calculatrice_Calc2", None)
                setattr(value, "calculatrice_Calc2", self)

    @property
    def calculatrice_BoolExpr17(self):
        return self.__calculatrice_BoolExpr17

    @calculatrice_BoolExpr17.setter
    def calculatrice_BoolExpr17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_BoolExpr__calculatrice_BoolExpr17", None)
        self.__calculatrice_BoolExpr17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_BoolExpr19"):
                opp_val = getattr(old_value, "calculatrice_BoolExpr19", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_BoolExpr19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_BoolExpr19"):
                opp_val = getattr(value, "calculatrice_BoolExpr19", None)
                setattr(value, "calculatrice_BoolExpr19", self)

    @property
    def calculatrice_BoolExpr15(self):
        return self.__calculatrice_BoolExpr15

    @calculatrice_BoolExpr15.setter
    def calculatrice_BoolExpr15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_BoolExpr__calculatrice_BoolExpr15", None)
        self.__calculatrice_BoolExpr15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_Calc16"):
                opp_val = getattr(old_value, "calculatrice_Calc16", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_Calc16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_Calc16"):
                opp_val = getattr(value, "calculatrice_Calc16", None)
                setattr(value, "calculatrice_Calc16", self)

    @property
    def calculatrice_BoolExpr19(self):
        return self.__calculatrice_BoolExpr19

    @calculatrice_BoolExpr19.setter
    def calculatrice_BoolExpr19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_BoolExpr__calculatrice_BoolExpr19", None)
        self.__calculatrice_BoolExpr19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_BoolExpr17"):
                opp_val = getattr(old_value, "calculatrice_BoolExpr17", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_BoolExpr17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_BoolExpr17"):
                opp_val = getattr(value, "calculatrice_BoolExpr17", None)
                setattr(value, "calculatrice_BoolExpr17", self)

    @property
    def calculatrice_BoolExpr20(self):
        return self.__calculatrice_BoolExpr20

    @calculatrice_BoolExpr20.setter
    def calculatrice_BoolExpr20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_BoolExpr__calculatrice_BoolExpr20", None)
        self.__calculatrice_BoolExpr20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_BoolExpr22"):
                opp_val = getattr(old_value, "calculatrice_BoolExpr22", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_BoolExpr22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_BoolExpr22"):
                opp_val = getattr(value, "calculatrice_BoolExpr22", None)
                setattr(value, "calculatrice_BoolExpr22", self)

class calculatrice_Calc:

    def __init__(self, boolName: str, decl: bool, varName: str, calculatrice_Calc: "calculatrice_Calculatrice" = None, calculatrice_Calc2: "calculatrice_BoolExpr" = None, calculatrice_Calc4: "calculatrice_CalcExpr" = None, calculatrice_Calc13: "calculatrice_BoolExpr" = None, calculatrice_Calc16: "calculatrice_BoolExpr" = None):
        self.boolName = boolName
        self.decl = decl
        self.varName = varName
        self.calculatrice_Calc = calculatrice_Calc
        self.calculatrice_Calc2 = calculatrice_Calc2
        self.calculatrice_Calc4 = calculatrice_Calc4
        self.calculatrice_Calc13 = calculatrice_Calc13
        self.calculatrice_Calc16 = calculatrice_Calc16
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def decl(self) -> bool:
        return self.__decl

    @decl.setter
    def decl(self, decl: bool):
        self.__decl = decl

    @property
    def boolName(self) -> str:
        return self.__boolName

    @boolName.setter
    def boolName(self, boolName: str):
        self.__boolName = boolName

    @property
    def calculatrice_Calc2(self):
        return self.__calculatrice_Calc2

    @calculatrice_Calc2.setter
    def calculatrice_Calc2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_Calc__calculatrice_Calc2", None)
        self.__calculatrice_Calc2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_BoolExpr"):
                opp_val = getattr(old_value, "calculatrice_BoolExpr", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_BoolExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_BoolExpr"):
                opp_val = getattr(value, "calculatrice_BoolExpr", None)
                setattr(value, "calculatrice_BoolExpr", self)

    @property
    def calculatrice_Calc16(self):
        return self.__calculatrice_Calc16

    @calculatrice_Calc16.setter
    def calculatrice_Calc16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_Calc__calculatrice_Calc16", None)
        self.__calculatrice_Calc16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_BoolExpr15"):
                opp_val = getattr(old_value, "calculatrice_BoolExpr15", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_BoolExpr15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_BoolExpr15"):
                opp_val = getattr(value, "calculatrice_BoolExpr15", None)
                setattr(value, "calculatrice_BoolExpr15", self)

    @property
    def calculatrice_Calc13(self):
        return self.__calculatrice_Calc13

    @calculatrice_Calc13.setter
    def calculatrice_Calc13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_Calc__calculatrice_Calc13", None)
        self.__calculatrice_Calc13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_BoolExpr12"):
                opp_val = getattr(old_value, "calculatrice_BoolExpr12", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_BoolExpr12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_BoolExpr12"):
                opp_val = getattr(value, "calculatrice_BoolExpr12", None)
                setattr(value, "calculatrice_BoolExpr12", self)

    @property
    def calculatrice_Calc4(self):
        return self.__calculatrice_Calc4

    @calculatrice_Calc4.setter
    def calculatrice_Calc4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_Calc__calculatrice_Calc4", None)
        self.__calculatrice_Calc4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_CalcExpr"):
                opp_val = getattr(old_value, "calculatrice_CalcExpr", None)
                if opp_val == self:
                    setattr(old_value, "calculatrice_CalcExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_CalcExpr"):
                opp_val = getattr(value, "calculatrice_CalcExpr", None)
                setattr(value, "calculatrice_CalcExpr", self)

    @property
    def calculatrice_Calc(self):
        return self.__calculatrice_Calc

    @calculatrice_Calc.setter
    def calculatrice_Calc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_calculatrice_Calc__calculatrice_Calc", None)
        self.__calculatrice_Calc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculatrice_Calculatrice"):
                opp_val = getattr(old_value, "calculatrice_Calculatrice", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculatrice_Calculatrice"):
                opp_val = getattr(value, "calculatrice_Calculatrice", None)
                if opp_val is None:
                    setattr(value, "calculatrice_Calculatrice", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class calculatrice_Calculatrice:

    pass