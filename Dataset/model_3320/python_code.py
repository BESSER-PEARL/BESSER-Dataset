from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Ampersand_Rule:

    def __init__(self, a1: str, a2: str, myDsl_Ampersand_Rule: "myDsl_Expression_aux" = None):
        self.a1 = a1
        self.a2 = a2
        self.myDsl_Ampersand_Rule = myDsl_Ampersand_Rule
        
    @property
    def a1(self) -> str:
        return self.__a1

    @a1.setter
    def a1(self, a1: str):
        self.__a1 = a1

    @property
    def a2(self) -> str:
        return self.__a2

    @a2.setter
    def a2(self, a2: str):
        self.__a2 = a2

    @property
    def myDsl_Ampersand_Rule(self):
        return self.__myDsl_Ampersand_Rule

    @myDsl_Ampersand_Rule.setter
    def myDsl_Ampersand_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Ampersand_Rule__myDsl_Ampersand_Rule", None)
        self.__myDsl_Ampersand_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression_aux145"):
                opp_val = getattr(old_value, "myDsl_Expression_aux145", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression_aux145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression_aux145"):
                opp_val = getattr(value, "myDsl_Expression_aux145", None)
                setattr(value, "myDsl_Expression_aux145", self)

class myDsl_Arg_List:

    pass
class myDsl_Float_Literal:

    def __init__(self, decimalDigits1: int, decimalDigits2: int, exp: str, floatTypeSufix: str, myDsl_Float_Literal: "myDsl_Literal_Expression" = None):
        self.decimalDigits1 = decimalDigits1
        self.decimalDigits2 = decimalDigits2
        self.exp = exp
        self.floatTypeSufix = floatTypeSufix
        self.myDsl_Float_Literal = myDsl_Float_Literal
        
    @property
    def decimalDigits2(self) -> int:
        return self.__decimalDigits2

    @decimalDigits2.setter
    def decimalDigits2(self, decimalDigits2: int):
        self.__decimalDigits2 = decimalDigits2

    @property
    def decimalDigits1(self) -> int:
        return self.__decimalDigits1

    @decimalDigits1.setter
    def decimalDigits1(self, decimalDigits1: int):
        self.__decimalDigits1 = decimalDigits1

    @property
    def floatTypeSufix(self) -> str:
        return self.__floatTypeSufix

    @floatTypeSufix.setter
    def floatTypeSufix(self, floatTypeSufix: str):
        self.__floatTypeSufix = floatTypeSufix

    @property
    def exp(self) -> str:
        return self.__exp

    @exp.setter
    def exp(self, exp: str):
        self.__exp = exp

    @property
    def myDsl_Float_Literal(self):
        return self.__myDsl_Float_Literal

    @myDsl_Float_Literal.setter
    def myDsl_Float_Literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Float_Literal__myDsl_Float_Literal", None)
        self.__myDsl_Float_Literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Literal_Expression153"):
                opp_val = getattr(old_value, "myDsl_Literal_Expression153", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Literal_Expression153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Literal_Expression153"):
                opp_val = getattr(value, "myDsl_Literal_Expression153", None)
                setattr(value, "myDsl_Literal_Expression153", self)

class myDsl_Cast_Expression:

    pass
class myDsl_Bit_Expression_NR:

    pass
class myDsl_Logical_Expression_NR:

    def __init__(self, exclamation: str, true: str, false: str, myDsl_Logical_Expression_NR: "myDsl_Expression" = None, myDsl_Logical_Expression_NR173: "myDsl_Expression" = None):
        self.exclamation = exclamation
        self.true = true
        self.false = false
        self.myDsl_Logical_Expression_NR = myDsl_Logical_Expression_NR
        self.myDsl_Logical_Expression_NR173 = myDsl_Logical_Expression_NR173
        
    @property
    def true(self) -> str:
        return self.__true

    @true.setter
    def true(self, true: str):
        self.__true = true

    @property
    def false(self) -> str:
        return self.__false

    @false.setter
    def false(self, false: str):
        self.__false = false

    @property
    def exclamation(self) -> str:
        return self.__exclamation

    @exclamation.setter
    def exclamation(self, exclamation: str):
        self.__exclamation = exclamation

    @property
    def myDsl_Logical_Expression_NR173(self):
        return self.__myDsl_Logical_Expression_NR173

    @myDsl_Logical_Expression_NR173.setter
    def myDsl_Logical_Expression_NR173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Logical_Expression_NR__myDsl_Logical_Expression_NR173", None)
        self.__myDsl_Logical_Expression_NR173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression174"):
                opp_val = getattr(old_value, "myDsl_Expression174", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression174"):
                opp_val = getattr(value, "myDsl_Expression174", None)
                setattr(value, "myDsl_Expression174", self)

    @property
    def myDsl_Logical_Expression_NR(self):
        return self.__myDsl_Logical_Expression_NR

    @myDsl_Logical_Expression_NR.setter
    def myDsl_Logical_Expression_NR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Logical_Expression_NR__myDsl_Logical_Expression_NR", None)
        self.__myDsl_Logical_Expression_NR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression118"):
                opp_val = getattr(old_value, "myDsl_Expression118", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression118"):
                opp_val = getattr(value, "myDsl_Expression118", None)
                setattr(value, "myDsl_Expression118", self)

class myDsl_Expression_aux:

    def __init__(self, bitSign: str, logicOp: str, name: str, sgin: str, numericSign: str, testingSign: str, logicalSign: str, stringSign: str, myDsl_Expression_aux: "myDsl_Expression" = None, myDsl_Expression_aux147: "myDsl_Expression" = None, myDsl_Expression_aux150: "myDsl_Expression" = None, myDsl_Expression_aux128: "myDsl_Arg_List" = None, myDsl_Expression_aux131: "myDsl_Expression_aux" = None, myDsl_Expression_aux129: "myDsl_Expression_aux" = None, myDsl_Expression_aux133: "myDsl_Expression" = None, myDsl_Expression_aux136: "myDsl_Expression" = None, myDsl_Expression_aux139: "myDsl_Expression" = None, myDsl_Expression_aux142: "myDsl_Expression" = None, myDsl_Expression_aux145: "myDsl_Ampersand_Rule" = None):
        self.bitSign = bitSign
        self.logicOp = logicOp
        self.name = name
        self.sgin = sgin
        self.numericSign = numericSign
        self.testingSign = testingSign
        self.logicalSign = logicalSign
        self.stringSign = stringSign
        self.myDsl_Expression_aux = myDsl_Expression_aux
        self.myDsl_Expression_aux147 = myDsl_Expression_aux147
        self.myDsl_Expression_aux150 = myDsl_Expression_aux150
        self.myDsl_Expression_aux128 = myDsl_Expression_aux128
        self.myDsl_Expression_aux131 = myDsl_Expression_aux131
        self.myDsl_Expression_aux129 = myDsl_Expression_aux129
        self.myDsl_Expression_aux133 = myDsl_Expression_aux133
        self.myDsl_Expression_aux136 = myDsl_Expression_aux136
        self.myDsl_Expression_aux139 = myDsl_Expression_aux139
        self.myDsl_Expression_aux142 = myDsl_Expression_aux142
        self.myDsl_Expression_aux145 = myDsl_Expression_aux145
        
    @property
    def stringSign(self) -> str:
        return self.__stringSign

    @stringSign.setter
    def stringSign(self, stringSign: str):
        self.__stringSign = stringSign

    @property
    def logicalSign(self) -> str:
        return self.__logicalSign

    @logicalSign.setter
    def logicalSign(self, logicalSign: str):
        self.__logicalSign = logicalSign

    @property
    def numericSign(self) -> str:
        return self.__numericSign

    @numericSign.setter
    def numericSign(self, numericSign: str):
        self.__numericSign = numericSign

    @property
    def bitSign(self) -> str:
        return self.__bitSign

    @bitSign.setter
    def bitSign(self, bitSign: str):
        self.__bitSign = bitSign

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def logicOp(self) -> str:
        return self.__logicOp

    @logicOp.setter
    def logicOp(self, logicOp: str):
        self.__logicOp = logicOp

    @property
    def testingSign(self) -> str:
        return self.__testingSign

    @testingSign.setter
    def testingSign(self, testingSign: str):
        self.__testingSign = testingSign

    @property
    def sgin(self) -> str:
        return self.__sgin

    @sgin.setter
    def sgin(self, sgin: str):
        self.__sgin = sgin

    @property
    def myDsl_Expression_aux147(self):
        return self.__myDsl_Expression_aux147

    @myDsl_Expression_aux147.setter
    def myDsl_Expression_aux147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression_aux__myDsl_Expression_aux147", None)
        self.__myDsl_Expression_aux147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression148"):
                opp_val = getattr(old_value, "myDsl_Expression148", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression148"):
                opp_val = getattr(value, "myDsl_Expression148", None)
                setattr(value, "myDsl_Expression148", self)

    @property
    def myDsl_Expression_aux145(self):
        return self.__myDsl_Expression_aux145

    @myDsl_Expression_aux145.setter
    def myDsl_Expression_aux145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression_aux__myDsl_Expression_aux145", None)
        self.__myDsl_Expression_aux145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Ampersand_Rule"):
                opp_val = getattr(old_value, "myDsl_Ampersand_Rule", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Ampersand_Rule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Ampersand_Rule"):
                opp_val = getattr(value, "myDsl_Ampersand_Rule", None)
                setattr(value, "myDsl_Ampersand_Rule", self)

    @property
    def myDsl_Expression_aux133(self):
        return self.__myDsl_Expression_aux133

    @myDsl_Expression_aux133.setter
    def myDsl_Expression_aux133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression_aux__myDsl_Expression_aux133", None)
        self.__myDsl_Expression_aux133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression134"):
                opp_val = getattr(old_value, "myDsl_Expression134", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression134"):
                opp_val = getattr(value, "myDsl_Expression134", None)
                setattr(value, "myDsl_Expression134", self)

    @property
    def myDsl_Expression_aux136(self):
        return self.__myDsl_Expression_aux136

    @myDsl_Expression_aux136.setter
    def myDsl_Expression_aux136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression_aux__myDsl_Expression_aux136", None)
        self.__myDsl_Expression_aux136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression137"):
                opp_val = getattr(old_value, "myDsl_Expression137", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression137"):
                opp_val = getattr(value, "myDsl_Expression137", None)
                setattr(value, "myDsl_Expression137", self)

    @property
    def myDsl_Expression_aux150(self):
        return self.__myDsl_Expression_aux150

    @myDsl_Expression_aux150.setter
    def myDsl_Expression_aux150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression_aux__myDsl_Expression_aux150", None)
        self.__myDsl_Expression_aux150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression151"):
                opp_val = getattr(old_value, "myDsl_Expression151", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression151"):
                opp_val = getattr(value, "myDsl_Expression151", None)
                setattr(value, "myDsl_Expression151", self)

    @property
    def myDsl_Expression_aux139(self):
        return self.__myDsl_Expression_aux139

    @myDsl_Expression_aux139.setter
    def myDsl_Expression_aux139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression_aux__myDsl_Expression_aux139", None)
        self.__myDsl_Expression_aux139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression140"):
                opp_val = getattr(old_value, "myDsl_Expression140", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression140"):
                opp_val = getattr(value, "myDsl_Expression140", None)
                setattr(value, "myDsl_Expression140", self)

    @property
    def myDsl_Expression_aux128(self):
        return self.__myDsl_Expression_aux128

    @myDsl_Expression_aux128.setter
    def myDsl_Expression_aux128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression_aux__myDsl_Expression_aux128", None)
        self.__myDsl_Expression_aux128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Arg_List"):
                opp_val = getattr(old_value, "myDsl_Arg_List", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Arg_List", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Arg_List"):
                opp_val = getattr(value, "myDsl_Arg_List", None)
                setattr(value, "myDsl_Arg_List", self)

    @property
    def myDsl_Expression_aux129(self):
        return self.__myDsl_Expression_aux129

    @myDsl_Expression_aux129.setter
    def myDsl_Expression_aux129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression_aux__myDsl_Expression_aux129", None)
        self.__myDsl_Expression_aux129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression_aux131"):
                opp_val = getattr(old_value, "myDsl_Expression_aux131", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression_aux131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression_aux131"):
                opp_val = getattr(value, "myDsl_Expression_aux131", None)
                setattr(value, "myDsl_Expression_aux131", self)

    @property
    def myDsl_Expression_aux142(self):
        return self.__myDsl_Expression_aux142

    @myDsl_Expression_aux142.setter
    def myDsl_Expression_aux142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression_aux__myDsl_Expression_aux142", None)
        self.__myDsl_Expression_aux142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression143"):
                opp_val = getattr(old_value, "myDsl_Expression143", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression143"):
                opp_val = getattr(value, "myDsl_Expression143", None)
                setattr(value, "myDsl_Expression143", self)

    @property
    def myDsl_Expression_aux131(self):
        return self.__myDsl_Expression_aux131

    @myDsl_Expression_aux131.setter
    def myDsl_Expression_aux131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression_aux__myDsl_Expression_aux131", None)
        self.__myDsl_Expression_aux131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression_aux129"):
                opp_val = getattr(old_value, "myDsl_Expression_aux129", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression_aux129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression_aux129"):
                opp_val = getattr(value, "myDsl_Expression_aux129", None)
                setattr(value, "myDsl_Expression_aux129", self)

    @property
    def myDsl_Expression_aux(self):
        return self.__myDsl_Expression_aux

    @myDsl_Expression_aux.setter
    def myDsl_Expression_aux(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression_aux__myDsl_Expression_aux", None)
        self.__myDsl_Expression_aux = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression116"):
                opp_val = getattr(old_value, "myDsl_Expression116", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression116"):
                opp_val = getattr(value, "myDsl_Expression116", None)
                setattr(value, "myDsl_Expression116", self)

class myDsl_Numeric_Expression_NR:

    def __init__(self, sinal_numeric: str, myDsl_Numeric_Expression_NR: "myDsl_Expression" = None, myDsl_Numeric_Expression_NR182: "myDsl_Expression" = None):
        self.sinal_numeric = sinal_numeric
        self.myDsl_Numeric_Expression_NR = myDsl_Numeric_Expression_NR
        self.myDsl_Numeric_Expression_NR182 = myDsl_Numeric_Expression_NR182
        
    @property
    def sinal_numeric(self) -> str:
        return self.__sinal_numeric

    @sinal_numeric.setter
    def sinal_numeric(self, sinal_numeric: str):
        self.__sinal_numeric = sinal_numeric

    @property
    def myDsl_Numeric_Expression_NR(self):
        return self.__myDsl_Numeric_Expression_NR

    @myDsl_Numeric_Expression_NR.setter
    def myDsl_Numeric_Expression_NR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Numeric_Expression_NR__myDsl_Numeric_Expression_NR", None)
        self.__myDsl_Numeric_Expression_NR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression114"):
                opp_val = getattr(old_value, "myDsl_Expression114", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression114"):
                opp_val = getattr(value, "myDsl_Expression114", None)
                setattr(value, "myDsl_Expression114", self)

    @property
    def myDsl_Numeric_Expression_NR182(self):
        return self.__myDsl_Numeric_Expression_NR182

    @myDsl_Numeric_Expression_NR182.setter
    def myDsl_Numeric_Expression_NR182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Numeric_Expression_NR__myDsl_Numeric_Expression_NR182", None)
        self.__myDsl_Numeric_Expression_NR182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression183"):
                opp_val = getattr(old_value, "myDsl_Expression183", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression183"):
                opp_val = getattr(value, "myDsl_Expression183", None)
                setattr(value, "myDsl_Expression183", self)

class myDsl_Literal_Expression:

    def __init__(self, exp: str, exp1: int, string: str, charLit: str, myDsl_Literal_Expression: "myDsl_Expression" = None, myDsl_Literal_Expression153: "myDsl_Float_Literal" = None):
        self.exp = exp
        self.exp1 = exp1
        self.string = string
        self.charLit = charLit
        self.myDsl_Literal_Expression = myDsl_Literal_Expression
        self.myDsl_Literal_Expression153 = myDsl_Literal_Expression153
        
    @property
    def exp1(self) -> int:
        return self.__exp1

    @exp1.setter
    def exp1(self, exp1: int):
        self.__exp1 = exp1

    @property
    def charLit(self) -> str:
        return self.__charLit

    @charLit.setter
    def charLit(self, charLit: str):
        self.__charLit = charLit

    @property
    def exp(self) -> str:
        return self.__exp

    @exp.setter
    def exp(self, exp: str):
        self.__exp = exp

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def myDsl_Literal_Expression(self):
        return self.__myDsl_Literal_Expression

    @myDsl_Literal_Expression.setter
    def myDsl_Literal_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Literal_Expression__myDsl_Literal_Expression", None)
        self.__myDsl_Literal_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression126"):
                opp_val = getattr(old_value, "myDsl_Expression126", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression126"):
                opp_val = getattr(value, "myDsl_Expression126", None)
                setattr(value, "myDsl_Expression126", self)

    @property
    def myDsl_Literal_Expression153(self):
        return self.__myDsl_Literal_Expression153

    @myDsl_Literal_Expression153.setter
    def myDsl_Literal_Expression153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Literal_Expression__myDsl_Literal_Expression153", None)
        self.__myDsl_Literal_Expression153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Float_Literal"):
                opp_val = getattr(old_value, "myDsl_Float_Literal", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Float_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Float_Literal"):
                opp_val = getattr(value, "myDsl_Float_Literal", None)
                setattr(value, "myDsl_Float_Literal", self)

class myDsl_Creating_Expression:

    def __init__(self, className: str, myDsl_Creating_Expression: "myDsl_Expression" = None, myDsl_Creating_Expression155: "myDsl_Arg_List" = None, myDsl_Creating_Expression158: "myDsl_Type_specifier" = None, myDsl_Creating_Expression161: "myDsl_Expression" = None):
        self.className = className
        self.myDsl_Creating_Expression = myDsl_Creating_Expression
        self.myDsl_Creating_Expression155 = myDsl_Creating_Expression155
        self.myDsl_Creating_Expression158 = myDsl_Creating_Expression158
        self.myDsl_Creating_Expression161 = myDsl_Creating_Expression161
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def myDsl_Creating_Expression158(self):
        return self.__myDsl_Creating_Expression158

    @myDsl_Creating_Expression158.setter
    def myDsl_Creating_Expression158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Creating_Expression__myDsl_Creating_Expression158", None)
        self.__myDsl_Creating_Expression158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type_specifier159"):
                opp_val = getattr(old_value, "myDsl_Type_specifier159", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type_specifier159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type_specifier159"):
                opp_val = getattr(value, "myDsl_Type_specifier159", None)
                setattr(value, "myDsl_Type_specifier159", self)

    @property
    def myDsl_Creating_Expression(self):
        return self.__myDsl_Creating_Expression

    @myDsl_Creating_Expression.setter
    def myDsl_Creating_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Creating_Expression__myDsl_Creating_Expression", None)
        self.__myDsl_Creating_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression124"):
                opp_val = getattr(old_value, "myDsl_Expression124", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression124"):
                opp_val = getattr(value, "myDsl_Expression124", None)
                setattr(value, "myDsl_Expression124", self)

    @property
    def myDsl_Creating_Expression155(self):
        return self.__myDsl_Creating_Expression155

    @myDsl_Creating_Expression155.setter
    def myDsl_Creating_Expression155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Creating_Expression__myDsl_Creating_Expression155", None)
        self.__myDsl_Creating_Expression155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Arg_List156"):
                opp_val = getattr(old_value, "myDsl_Arg_List156", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Arg_List156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Arg_List156"):
                opp_val = getattr(value, "myDsl_Arg_List156", None)
                setattr(value, "myDsl_Arg_List156", self)

    @property
    def myDsl_Creating_Expression161(self):
        return self.__myDsl_Creating_Expression161

    @myDsl_Creating_Expression161.setter
    def myDsl_Creating_Expression161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Creating_Expression__myDsl_Creating_Expression161", None)
        self.__myDsl_Creating_Expression161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression162"):
                opp_val = getattr(old_value, "myDsl_Expression162", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression162"):
                opp_val = getattr(value, "myDsl_Expression162", None)
                setattr(value, "myDsl_Expression162", self)

class myDsl_Try_statement:

    def __init__(self, lParen: str, rparent: str, myDsl_Try_statement: "myDsl_Statement" = None, myDsl_Try_statement212: "myDsl_Statement" = None, myDsl_Try_statement215: set["myDsl_Parameter"] = None, myDsl_Try_statement218: set["myDsl_Statement"] = None, myDsl_Try_statement221: "myDsl_Statement" = None):
        self.lParen = lParen
        self.rparent = rparent
        self.myDsl_Try_statement = myDsl_Try_statement
        self.myDsl_Try_statement212 = myDsl_Try_statement212
        self.myDsl_Try_statement215 = myDsl_Try_statement215 if myDsl_Try_statement215 is not None else set()
        self.myDsl_Try_statement218 = myDsl_Try_statement218 if myDsl_Try_statement218 is not None else set()
        self.myDsl_Try_statement221 = myDsl_Try_statement221
        
    @property
    def lParen(self) -> str:
        return self.__lParen

    @lParen.setter
    def lParen(self, lParen: str):
        self.__lParen = lParen

    @property
    def rparent(self) -> str:
        return self.__rparent

    @rparent.setter
    def rparent(self, rparent: str):
        self.__rparent = rparent

    @property
    def myDsl_Try_statement221(self):
        return self.__myDsl_Try_statement221

    @myDsl_Try_statement221.setter
    def myDsl_Try_statement221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Try_statement__myDsl_Try_statement221", None)
        self.__myDsl_Try_statement221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement222"):
                opp_val = getattr(old_value, "myDsl_Statement222", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement222"):
                opp_val = getattr(value, "myDsl_Statement222", None)
                setattr(value, "myDsl_Statement222", self)

    @property
    def myDsl_Try_statement(self):
        return self.__myDsl_Try_statement

    @myDsl_Try_statement.setter
    def myDsl_Try_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Try_statement__myDsl_Try_statement", None)
        self.__myDsl_Try_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement94"):
                opp_val = getattr(old_value, "myDsl_Statement94", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement94"):
                opp_val = getattr(value, "myDsl_Statement94", None)
                setattr(value, "myDsl_Statement94", self)

    @property
    def myDsl_Try_statement212(self):
        return self.__myDsl_Try_statement212

    @myDsl_Try_statement212.setter
    def myDsl_Try_statement212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Try_statement__myDsl_Try_statement212", None)
        self.__myDsl_Try_statement212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement213"):
                opp_val = getattr(old_value, "myDsl_Statement213", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement213"):
                opp_val = getattr(value, "myDsl_Statement213", None)
                setattr(value, "myDsl_Statement213", self)

    @property
    def myDsl_Try_statement218(self):
        return self.__myDsl_Try_statement218

    @myDsl_Try_statement218.setter
    def myDsl_Try_statement218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Try_statement__myDsl_Try_statement218", None)
        self.__myDsl_Try_statement218 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Statement219"):
                    opp_val = getattr(item, "myDsl_Statement219", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Statement219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Statement219"):
                    opp_val = getattr(item, "myDsl_Statement219", None)
                    
                    setattr(item, "myDsl_Statement219", self)
                    

    @property
    def myDsl_Try_statement215(self):
        return self.__myDsl_Try_statement215

    @myDsl_Try_statement215.setter
    def myDsl_Try_statement215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Try_statement__myDsl_Try_statement215", None)
        self.__myDsl_Try_statement215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Parameter216"):
                    opp_val = getattr(item, "myDsl_Parameter216", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Parameter216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Parameter216"):
                    opp_val = getattr(item, "myDsl_Parameter216", None)
                    
                    setattr(item, "myDsl_Parameter216", self)
                    

class myDsl_Switch_statement:

    def __init__(self, lParen: str, rparent: str, myDsl_Switch_statement: "myDsl_Statement" = None, myDsl_Switch_statement185: "myDsl_Expression" = None, myDsl_Switch_statement188: set["myDsl_Expression"] = None, myDsl_Switch_statement191: set["myDsl_Statement"] = None):
        self.lParen = lParen
        self.rparent = rparent
        self.myDsl_Switch_statement = myDsl_Switch_statement
        self.myDsl_Switch_statement185 = myDsl_Switch_statement185
        self.myDsl_Switch_statement188 = myDsl_Switch_statement188 if myDsl_Switch_statement188 is not None else set()
        self.myDsl_Switch_statement191 = myDsl_Switch_statement191 if myDsl_Switch_statement191 is not None else set()
        
    @property
    def lParen(self) -> str:
        return self.__lParen

    @lParen.setter
    def lParen(self, lParen: str):
        self.__lParen = lParen

    @property
    def rparent(self) -> str:
        return self.__rparent

    @rparent.setter
    def rparent(self, rparent: str):
        self.__rparent = rparent

    @property
    def myDsl_Switch_statement(self):
        return self.__myDsl_Switch_statement

    @myDsl_Switch_statement.setter
    def myDsl_Switch_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Switch_statement__myDsl_Switch_statement", None)
        self.__myDsl_Switch_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement83"):
                opp_val = getattr(old_value, "myDsl_Statement83", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement83"):
                opp_val = getattr(value, "myDsl_Statement83", None)
                setattr(value, "myDsl_Statement83", self)

    @property
    def myDsl_Switch_statement191(self):
        return self.__myDsl_Switch_statement191

    @myDsl_Switch_statement191.setter
    def myDsl_Switch_statement191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Switch_statement__myDsl_Switch_statement191", None)
        self.__myDsl_Switch_statement191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Statement192"):
                    opp_val = getattr(item, "myDsl_Statement192", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Statement192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Statement192"):
                    opp_val = getattr(item, "myDsl_Statement192", None)
                    
                    setattr(item, "myDsl_Statement192", self)
                    

    @property
    def myDsl_Switch_statement188(self):
        return self.__myDsl_Switch_statement188

    @myDsl_Switch_statement188.setter
    def myDsl_Switch_statement188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Switch_statement__myDsl_Switch_statement188", None)
        self.__myDsl_Switch_statement188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Expression189"):
                    opp_val = getattr(item, "myDsl_Expression189", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Expression189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Expression189"):
                    opp_val = getattr(item, "myDsl_Expression189", None)
                    
                    setattr(item, "myDsl_Expression189", self)
                    

    @property
    def myDsl_Switch_statement185(self):
        return self.__myDsl_Switch_statement185

    @myDsl_Switch_statement185.setter
    def myDsl_Switch_statement185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Switch_statement__myDsl_Switch_statement185", None)
        self.__myDsl_Switch_statement185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression186"):
                opp_val = getattr(old_value, "myDsl_Expression186", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression186"):
                opp_val = getattr(value, "myDsl_Expression186", None)
                setattr(value, "myDsl_Expression186", self)

class myDsl_For_Statement:

    pass
class myDsl_While_Statement:

    def __init__(self, rparent: str, myDsl_While_Statement: "myDsl_Statement" = None, myDsl_While_Statement194: "myDsl_Expression" = None, myDsl_While_Statement197: "myDsl_Statement" = None):
        self.rparent = rparent
        self.myDsl_While_Statement = myDsl_While_Statement
        self.myDsl_While_Statement194 = myDsl_While_Statement194
        self.myDsl_While_Statement197 = myDsl_While_Statement197
        
    @property
    def rparent(self) -> str:
        return self.__rparent

    @rparent.setter
    def rparent(self, rparent: str):
        self.__rparent = rparent

    @property
    def myDsl_While_Statement197(self):
        return self.__myDsl_While_Statement197

    @myDsl_While_Statement197.setter
    def myDsl_While_Statement197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_While_Statement__myDsl_While_Statement197", None)
        self.__myDsl_While_Statement197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement198"):
                opp_val = getattr(old_value, "myDsl_Statement198", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement198"):
                opp_val = getattr(value, "myDsl_Statement198", None)
                setattr(value, "myDsl_Statement198", self)

    @property
    def myDsl_While_Statement(self):
        return self.__myDsl_While_Statement

    @myDsl_While_Statement.setter
    def myDsl_While_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_While_Statement__myDsl_While_Statement", None)
        self.__myDsl_While_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement79"):
                opp_val = getattr(old_value, "myDsl_Statement79", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement79"):
                opp_val = getattr(value, "myDsl_Statement79", None)
                setattr(value, "myDsl_Statement79", self)

    @property
    def myDsl_While_Statement194(self):
        return self.__myDsl_While_Statement194

    @myDsl_While_Statement194.setter
    def myDsl_While_Statement194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_While_Statement__myDsl_While_Statement194", None)
        self.__myDsl_While_Statement194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression195"):
                opp_val = getattr(old_value, "myDsl_Expression195", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression195"):
                opp_val = getattr(value, "myDsl_Expression195", None)
                setattr(value, "myDsl_Expression195", self)

class myDsl_Do_Statement:

    def __init__(self, lparent: str, rparent: str, myDsl_Do_Statement: "myDsl_Statement" = None, myDsl_Do_Statement200: "myDsl_Statement" = None):
        self.lparent = lparent
        self.rparent = rparent
        self.myDsl_Do_Statement = myDsl_Do_Statement
        self.myDsl_Do_Statement200 = myDsl_Do_Statement200
        
    @property
    def lparent(self) -> str:
        return self.__lparent

    @lparent.setter
    def lparent(self, lparent: str):
        self.__lparent = lparent

    @property
    def rparent(self) -> str:
        return self.__rparent

    @rparent.setter
    def rparent(self, rparent: str):
        self.__rparent = rparent

    @property
    def myDsl_Do_Statement(self):
        return self.__myDsl_Do_Statement

    @myDsl_Do_Statement.setter
    def myDsl_Do_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Do_Statement__myDsl_Do_Statement", None)
        self.__myDsl_Do_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement77"):
                opp_val = getattr(old_value, "myDsl_Statement77", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement77"):
                opp_val = getattr(value, "myDsl_Statement77", None)
                setattr(value, "myDsl_Statement77", self)

    @property
    def myDsl_Do_Statement200(self):
        return self.__myDsl_Do_Statement200

    @myDsl_Do_Statement200.setter
    def myDsl_Do_Statement200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Do_Statement__myDsl_Do_Statement200", None)
        self.__myDsl_Do_Statement200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement201"):
                opp_val = getattr(old_value, "myDsl_Statement201", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement201"):
                opp_val = getattr(value, "myDsl_Statement201", None)
                setattr(value, "myDsl_Statement201", self)

class myDsl_If_statement:

    def __init__(self, rparent: str, lparen: str, myDsl_If_statement: "myDsl_Statement" = None, myDsl_If_statement206: "myDsl_Statement" = None, myDsl_If_statement209: "myDsl_Statement" = None, myDsl_If_statement203: "myDsl_Expression" = None):
        self.rparent = rparent
        self.lparen = lparen
        self.myDsl_If_statement = myDsl_If_statement
        self.myDsl_If_statement206 = myDsl_If_statement206
        self.myDsl_If_statement209 = myDsl_If_statement209
        self.myDsl_If_statement203 = myDsl_If_statement203
        
    @property
    def lparen(self) -> str:
        return self.__lparen

    @lparen.setter
    def lparen(self, lparen: str):
        self.__lparen = lparen

    @property
    def rparent(self) -> str:
        return self.__rparent

    @rparent.setter
    def rparent(self, rparent: str):
        self.__rparent = rparent

    @property
    def myDsl_If_statement206(self):
        return self.__myDsl_If_statement206

    @myDsl_If_statement206.setter
    def myDsl_If_statement206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_If_statement__myDsl_If_statement206", None)
        self.__myDsl_If_statement206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement207"):
                opp_val = getattr(old_value, "myDsl_Statement207", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement207"):
                opp_val = getattr(value, "myDsl_Statement207", None)
                setattr(value, "myDsl_Statement207", self)

    @property
    def myDsl_If_statement209(self):
        return self.__myDsl_If_statement209

    @myDsl_If_statement209.setter
    def myDsl_If_statement209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_If_statement__myDsl_If_statement209", None)
        self.__myDsl_If_statement209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement210"):
                opp_val = getattr(old_value, "myDsl_Statement210", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement210"):
                opp_val = getattr(value, "myDsl_Statement210", None)
                setattr(value, "myDsl_Statement210", self)

    @property
    def myDsl_If_statement203(self):
        return self.__myDsl_If_statement203

    @myDsl_If_statement203.setter
    def myDsl_If_statement203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_If_statement__myDsl_If_statement203", None)
        self.__myDsl_If_statement203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression204"):
                opp_val = getattr(old_value, "myDsl_Expression204", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression204"):
                opp_val = getattr(value, "myDsl_Expression204", None)
                setattr(value, "myDsl_Expression204", self)

    @property
    def myDsl_If_statement(self):
        return self.__myDsl_If_statement

    @myDsl_If_statement.setter
    def myDsl_If_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_If_statement__myDsl_If_statement", None)
        self.__myDsl_If_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement75"):
                opp_val = getattr(old_value, "myDsl_Statement75", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement75"):
                opp_val = getattr(value, "myDsl_Statement75", None)
                setattr(value, "myDsl_Statement75", self)

class myDsl_Type_specifier:

    def __init__(self, primitiveType: str, className: str, myDsl_Type_specifier: "myDsl_Type" = None, myDsl_Type_specifier159: "myDsl_Creating_Expression" = None):
        self.primitiveType = primitiveType
        self.className = className
        self.myDsl_Type_specifier = myDsl_Type_specifier
        self.myDsl_Type_specifier159 = myDsl_Type_specifier159
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

    @property
    def myDsl_Type_specifier(self):
        return self.__myDsl_Type_specifier

    @myDsl_Type_specifier.setter
    def myDsl_Type_specifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type_specifier__myDsl_Type_specifier", None)
        self.__myDsl_Type_specifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type62"):
                opp_val = getattr(old_value, "myDsl_Type62", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type62"):
                opp_val = getattr(value, "myDsl_Type62", None)
                setattr(value, "myDsl_Type62", self)

    @property
    def myDsl_Type_specifier159(self):
        return self.__myDsl_Type_specifier159

    @myDsl_Type_specifier159.setter
    def myDsl_Type_specifier159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type_specifier__myDsl_Type_specifier159", None)
        self.__myDsl_Type_specifier159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Creating_Expression158"):
                opp_val = getattr(old_value, "myDsl_Creating_Expression158", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Creating_Expression158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Creating_Expression158"):
                opp_val = getattr(value, "myDsl_Creating_Expression158", None)
                setattr(value, "myDsl_Creating_Expression158", self)

class myDsl_Expression:

    def __init__(self, null: str, super: str, this: str, name: str, myDsl_Expression73: "myDsl_Statement" = None, myDsl_Expression: "myDsl_Variable_initializer" = None, myDsl_Expression103: "myDsl_For_Statement" = None, myDsl_Expression106: "myDsl_For_Statement" = None, myDsl_Expression86: "myDsl_Statement" = None, myDsl_Expression124: "myDsl_Creating_Expression" = None, myDsl_Expression126: "myDsl_Literal_Expression" = None, myDsl_Expression109: "myDsl_For_Statement" = None, myDsl_Expression114: "myDsl_Numeric_Expression_NR" = None, myDsl_Expression116: "myDsl_Expression_aux" = None, myDsl_Expression118: "myDsl_Logical_Expression_NR" = None, myDsl_Expression120: "myDsl_Bit_Expression_NR" = None, myDsl_Expression122: "myDsl_Cast_Expression" = None, myDsl_Expression148: "myDsl_Expression_aux" = None, myDsl_Expression151: "myDsl_Expression_aux" = None, myDsl_Expression134: "myDsl_Expression_aux" = None, myDsl_Expression137: "myDsl_Expression_aux" = None, myDsl_Expression140: "myDsl_Expression_aux" = None, myDsl_Expression143: "myDsl_Expression_aux" = None, myDsl_Expression183: "myDsl_Numeric_Expression_NR" = None, myDsl_Expression186: "myDsl_Switch_statement" = None, myDsl_Expression189: "myDsl_Switch_statement" = None, myDsl_Expression195: "myDsl_While_Statement" = None, myDsl_Expression162: "myDsl_Creating_Expression" = None, myDsl_Expression168: "myDsl_Cast_Expression" = None, myDsl_Expression171: "myDsl_Bit_Expression_NR" = None, myDsl_Expression174: "myDsl_Logical_Expression_NR" = None, myDsl_Expression177: "myDsl_Arg_List" = None, myDsl_Expression180: "myDsl_Arg_List" = None, myDsl_Expression204: "myDsl_If_statement" = None):
        self.null = null
        self.super = super
        self.this = this
        self.name = name
        self.myDsl_Expression73 = myDsl_Expression73
        self.myDsl_Expression = myDsl_Expression
        self.myDsl_Expression103 = myDsl_Expression103
        self.myDsl_Expression106 = myDsl_Expression106
        self.myDsl_Expression86 = myDsl_Expression86
        self.myDsl_Expression124 = myDsl_Expression124
        self.myDsl_Expression126 = myDsl_Expression126
        self.myDsl_Expression109 = myDsl_Expression109
        self.myDsl_Expression114 = myDsl_Expression114
        self.myDsl_Expression116 = myDsl_Expression116
        self.myDsl_Expression118 = myDsl_Expression118
        self.myDsl_Expression120 = myDsl_Expression120
        self.myDsl_Expression122 = myDsl_Expression122
        self.myDsl_Expression148 = myDsl_Expression148
        self.myDsl_Expression151 = myDsl_Expression151
        self.myDsl_Expression134 = myDsl_Expression134
        self.myDsl_Expression137 = myDsl_Expression137
        self.myDsl_Expression140 = myDsl_Expression140
        self.myDsl_Expression143 = myDsl_Expression143
        self.myDsl_Expression183 = myDsl_Expression183
        self.myDsl_Expression186 = myDsl_Expression186
        self.myDsl_Expression189 = myDsl_Expression189
        self.myDsl_Expression195 = myDsl_Expression195
        self.myDsl_Expression162 = myDsl_Expression162
        self.myDsl_Expression168 = myDsl_Expression168
        self.myDsl_Expression171 = myDsl_Expression171
        self.myDsl_Expression174 = myDsl_Expression174
        self.myDsl_Expression177 = myDsl_Expression177
        self.myDsl_Expression180 = myDsl_Expression180
        self.myDsl_Expression204 = myDsl_Expression204
        
    @property
    def this(self) -> str:
        return self.__this

    @this.setter
    def this(self, this: str):
        self.__this = this

    @property
    def super(self) -> str:
        return self.__super

    @super.setter
    def super(self, super: str):
        self.__super = super

    @property
    def null(self) -> str:
        return self.__null

    @null.setter
    def null(self, null: str):
        self.__null = null

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Expression204(self):
        return self.__myDsl_Expression204

    @myDsl_Expression204.setter
    def myDsl_Expression204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression204", None)
        self.__myDsl_Expression204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_If_statement203"):
                opp_val = getattr(old_value, "myDsl_If_statement203", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_If_statement203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_If_statement203"):
                opp_val = getattr(value, "myDsl_If_statement203", None)
                setattr(value, "myDsl_If_statement203", self)

    @property
    def myDsl_Expression140(self):
        return self.__myDsl_Expression140

    @myDsl_Expression140.setter
    def myDsl_Expression140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression140", None)
        self.__myDsl_Expression140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression_aux139"):
                opp_val = getattr(old_value, "myDsl_Expression_aux139", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression_aux139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression_aux139"):
                opp_val = getattr(value, "myDsl_Expression_aux139", None)
                setattr(value, "myDsl_Expression_aux139", self)

    @property
    def myDsl_Expression137(self):
        return self.__myDsl_Expression137

    @myDsl_Expression137.setter
    def myDsl_Expression137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression137", None)
        self.__myDsl_Expression137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression_aux136"):
                opp_val = getattr(old_value, "myDsl_Expression_aux136", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression_aux136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression_aux136"):
                opp_val = getattr(value, "myDsl_Expression_aux136", None)
                setattr(value, "myDsl_Expression_aux136", self)

    @property
    def myDsl_Expression120(self):
        return self.__myDsl_Expression120

    @myDsl_Expression120.setter
    def myDsl_Expression120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression120", None)
        self.__myDsl_Expression120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Bit_Expression_NR"):
                opp_val = getattr(old_value, "myDsl_Bit_Expression_NR", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Bit_Expression_NR", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Bit_Expression_NR"):
                opp_val = getattr(value, "myDsl_Bit_Expression_NR", None)
                setattr(value, "myDsl_Bit_Expression_NR", self)

    @property
    def myDsl_Expression151(self):
        return self.__myDsl_Expression151

    @myDsl_Expression151.setter
    def myDsl_Expression151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression151", None)
        self.__myDsl_Expression151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression_aux150"):
                opp_val = getattr(old_value, "myDsl_Expression_aux150", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression_aux150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression_aux150"):
                opp_val = getattr(value, "myDsl_Expression_aux150", None)
                setattr(value, "myDsl_Expression_aux150", self)

    @property
    def myDsl_Expression148(self):
        return self.__myDsl_Expression148

    @myDsl_Expression148.setter
    def myDsl_Expression148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression148", None)
        self.__myDsl_Expression148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression_aux147"):
                opp_val = getattr(old_value, "myDsl_Expression_aux147", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression_aux147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression_aux147"):
                opp_val = getattr(value, "myDsl_Expression_aux147", None)
                setattr(value, "myDsl_Expression_aux147", self)

    @property
    def myDsl_Expression143(self):
        return self.__myDsl_Expression143

    @myDsl_Expression143.setter
    def myDsl_Expression143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression143", None)
        self.__myDsl_Expression143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression_aux142"):
                opp_val = getattr(old_value, "myDsl_Expression_aux142", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression_aux142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression_aux142"):
                opp_val = getattr(value, "myDsl_Expression_aux142", None)
                setattr(value, "myDsl_Expression_aux142", self)

    @property
    def myDsl_Expression116(self):
        return self.__myDsl_Expression116

    @myDsl_Expression116.setter
    def myDsl_Expression116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression116", None)
        self.__myDsl_Expression116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression_aux"):
                opp_val = getattr(old_value, "myDsl_Expression_aux", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression_aux", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression_aux"):
                opp_val = getattr(value, "myDsl_Expression_aux", None)
                setattr(value, "myDsl_Expression_aux", self)

    @property
    def myDsl_Expression106(self):
        return self.__myDsl_Expression106

    @myDsl_Expression106.setter
    def myDsl_Expression106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression106", None)
        self.__myDsl_Expression106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_For_Statement105"):
                opp_val = getattr(old_value, "myDsl_For_Statement105", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_For_Statement105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_For_Statement105"):
                opp_val = getattr(value, "myDsl_For_Statement105", None)
                setattr(value, "myDsl_For_Statement105", self)

    @property
    def myDsl_Expression118(self):
        return self.__myDsl_Expression118

    @myDsl_Expression118.setter
    def myDsl_Expression118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression118", None)
        self.__myDsl_Expression118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Logical_Expression_NR"):
                opp_val = getattr(old_value, "myDsl_Logical_Expression_NR", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Logical_Expression_NR", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Logical_Expression_NR"):
                opp_val = getattr(value, "myDsl_Logical_Expression_NR", None)
                setattr(value, "myDsl_Logical_Expression_NR", self)

    @property
    def myDsl_Expression180(self):
        return self.__myDsl_Expression180

    @myDsl_Expression180.setter
    def myDsl_Expression180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression180", None)
        self.__myDsl_Expression180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Arg_List179"):
                opp_val = getattr(old_value, "myDsl_Arg_List179", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Arg_List179"):
                opp_val = getattr(value, "myDsl_Arg_List179", None)
                if opp_val is None:
                    setattr(value, "myDsl_Arg_List179", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Expression189(self):
        return self.__myDsl_Expression189

    @myDsl_Expression189.setter
    def myDsl_Expression189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression189", None)
        self.__myDsl_Expression189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Switch_statement188"):
                opp_val = getattr(old_value, "myDsl_Switch_statement188", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Switch_statement188"):
                opp_val = getattr(value, "myDsl_Switch_statement188", None)
                if opp_val is None:
                    setattr(value, "myDsl_Switch_statement188", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Expression122(self):
        return self.__myDsl_Expression122

    @myDsl_Expression122.setter
    def myDsl_Expression122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression122", None)
        self.__myDsl_Expression122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Cast_Expression"):
                opp_val = getattr(old_value, "myDsl_Cast_Expression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Cast_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Cast_Expression"):
                opp_val = getattr(value, "myDsl_Cast_Expression", None)
                setattr(value, "myDsl_Cast_Expression", self)

    @property
    def myDsl_Expression134(self):
        return self.__myDsl_Expression134

    @myDsl_Expression134.setter
    def myDsl_Expression134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression134", None)
        self.__myDsl_Expression134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression_aux133"):
                opp_val = getattr(old_value, "myDsl_Expression_aux133", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression_aux133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression_aux133"):
                opp_val = getattr(value, "myDsl_Expression_aux133", None)
                setattr(value, "myDsl_Expression_aux133", self)

    @property
    def myDsl_Expression177(self):
        return self.__myDsl_Expression177

    @myDsl_Expression177.setter
    def myDsl_Expression177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression177", None)
        self.__myDsl_Expression177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Arg_List176"):
                opp_val = getattr(old_value, "myDsl_Arg_List176", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Arg_List176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Arg_List176"):
                opp_val = getattr(value, "myDsl_Arg_List176", None)
                setattr(value, "myDsl_Arg_List176", self)

    @property
    def myDsl_Expression124(self):
        return self.__myDsl_Expression124

    @myDsl_Expression124.setter
    def myDsl_Expression124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression124", None)
        self.__myDsl_Expression124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Creating_Expression"):
                opp_val = getattr(old_value, "myDsl_Creating_Expression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Creating_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Creating_Expression"):
                opp_val = getattr(value, "myDsl_Creating_Expression", None)
                setattr(value, "myDsl_Creating_Expression", self)

    @property
    def myDsl_Expression126(self):
        return self.__myDsl_Expression126

    @myDsl_Expression126.setter
    def myDsl_Expression126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression126", None)
        self.__myDsl_Expression126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Literal_Expression"):
                opp_val = getattr(old_value, "myDsl_Literal_Expression", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Literal_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Literal_Expression"):
                opp_val = getattr(value, "myDsl_Literal_Expression", None)
                setattr(value, "myDsl_Literal_Expression", self)

    @property
    def myDsl_Expression174(self):
        return self.__myDsl_Expression174

    @myDsl_Expression174.setter
    def myDsl_Expression174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression174", None)
        self.__myDsl_Expression174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Logical_Expression_NR173"):
                opp_val = getattr(old_value, "myDsl_Logical_Expression_NR173", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Logical_Expression_NR173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Logical_Expression_NR173"):
                opp_val = getattr(value, "myDsl_Logical_Expression_NR173", None)
                setattr(value, "myDsl_Logical_Expression_NR173", self)

    @property
    def myDsl_Expression171(self):
        return self.__myDsl_Expression171

    @myDsl_Expression171.setter
    def myDsl_Expression171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression171", None)
        self.__myDsl_Expression171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Bit_Expression_NR170"):
                opp_val = getattr(old_value, "myDsl_Bit_Expression_NR170", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Bit_Expression_NR170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Bit_Expression_NR170"):
                opp_val = getattr(value, "myDsl_Bit_Expression_NR170", None)
                setattr(value, "myDsl_Bit_Expression_NR170", self)

    @property
    def myDsl_Expression186(self):
        return self.__myDsl_Expression186

    @myDsl_Expression186.setter
    def myDsl_Expression186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression186", None)
        self.__myDsl_Expression186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Switch_statement185"):
                opp_val = getattr(old_value, "myDsl_Switch_statement185", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Switch_statement185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Switch_statement185"):
                opp_val = getattr(value, "myDsl_Switch_statement185", None)
                setattr(value, "myDsl_Switch_statement185", self)

    @property
    def myDsl_Expression162(self):
        return self.__myDsl_Expression162

    @myDsl_Expression162.setter
    def myDsl_Expression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression162", None)
        self.__myDsl_Expression162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Creating_Expression161"):
                opp_val = getattr(old_value, "myDsl_Creating_Expression161", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Creating_Expression161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Creating_Expression161"):
                opp_val = getattr(value, "myDsl_Creating_Expression161", None)
                setattr(value, "myDsl_Creating_Expression161", self)

    @property
    def myDsl_Expression(self):
        return self.__myDsl_Expression

    @myDsl_Expression.setter
    def myDsl_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression", None)
        self.__myDsl_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Variable_initializer57"):
                opp_val = getattr(old_value, "myDsl_Variable_initializer57", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Variable_initializer57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Variable_initializer57"):
                opp_val = getattr(value, "myDsl_Variable_initializer57", None)
                setattr(value, "myDsl_Variable_initializer57", self)

    @property
    def myDsl_Expression183(self):
        return self.__myDsl_Expression183

    @myDsl_Expression183.setter
    def myDsl_Expression183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression183", None)
        self.__myDsl_Expression183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Numeric_Expression_NR182"):
                opp_val = getattr(old_value, "myDsl_Numeric_Expression_NR182", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Numeric_Expression_NR182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Numeric_Expression_NR182"):
                opp_val = getattr(value, "myDsl_Numeric_Expression_NR182", None)
                setattr(value, "myDsl_Numeric_Expression_NR182", self)

    @property
    def myDsl_Expression103(self):
        return self.__myDsl_Expression103

    @myDsl_Expression103.setter
    def myDsl_Expression103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression103", None)
        self.__myDsl_Expression103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_For_Statement102"):
                opp_val = getattr(old_value, "myDsl_For_Statement102", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_For_Statement102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_For_Statement102"):
                opp_val = getattr(value, "myDsl_For_Statement102", None)
                setattr(value, "myDsl_For_Statement102", self)

    @property
    def myDsl_Expression114(self):
        return self.__myDsl_Expression114

    @myDsl_Expression114.setter
    def myDsl_Expression114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression114", None)
        self.__myDsl_Expression114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Numeric_Expression_NR"):
                opp_val = getattr(old_value, "myDsl_Numeric_Expression_NR", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Numeric_Expression_NR", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Numeric_Expression_NR"):
                opp_val = getattr(value, "myDsl_Numeric_Expression_NR", None)
                setattr(value, "myDsl_Numeric_Expression_NR", self)

    @property
    def myDsl_Expression73(self):
        return self.__myDsl_Expression73

    @myDsl_Expression73.setter
    def myDsl_Expression73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression73", None)
        self.__myDsl_Expression73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement72"):
                opp_val = getattr(old_value, "myDsl_Statement72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement72"):
                opp_val = getattr(value, "myDsl_Statement72", None)
                if opp_val is None:
                    setattr(value, "myDsl_Statement72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Expression168(self):
        return self.__myDsl_Expression168

    @myDsl_Expression168.setter
    def myDsl_Expression168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression168", None)
        self.__myDsl_Expression168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Cast_Expression167"):
                opp_val = getattr(old_value, "myDsl_Cast_Expression167", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Cast_Expression167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Cast_Expression167"):
                opp_val = getattr(value, "myDsl_Cast_Expression167", None)
                setattr(value, "myDsl_Cast_Expression167", self)

    @property
    def myDsl_Expression195(self):
        return self.__myDsl_Expression195

    @myDsl_Expression195.setter
    def myDsl_Expression195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression195", None)
        self.__myDsl_Expression195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_While_Statement194"):
                opp_val = getattr(old_value, "myDsl_While_Statement194", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_While_Statement194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_While_Statement194"):
                opp_val = getattr(value, "myDsl_While_Statement194", None)
                setattr(value, "myDsl_While_Statement194", self)

    @property
    def myDsl_Expression86(self):
        return self.__myDsl_Expression86

    @myDsl_Expression86.setter
    def myDsl_Expression86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression86", None)
        self.__myDsl_Expression86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement85"):
                opp_val = getattr(old_value, "myDsl_Statement85", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement85"):
                opp_val = getattr(value, "myDsl_Statement85", None)
                setattr(value, "myDsl_Statement85", self)

    @property
    def myDsl_Expression109(self):
        return self.__myDsl_Expression109

    @myDsl_Expression109.setter
    def myDsl_Expression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Expression__myDsl_Expression109", None)
        self.__myDsl_Expression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_For_Statement108"):
                opp_val = getattr(old_value, "myDsl_For_Statement108", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_For_Statement108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_For_Statement108"):
                opp_val = getattr(value, "myDsl_For_Statement108", None)
                setattr(value, "myDsl_For_Statement108", self)

class myDsl_Array_initializer:

    pass
class myDsl_Variable_initializer:

    pass
class myDsl_Statement:

    def __init__(self, nameStatement: str, name: str, g: str, rparent: str, ret: str, myDsl_Statement: "myDsl_Statement_block" = None, myDsl_Statement69: "myDsl_Variable_declaration" = None, myDsl_Statement72: set["myDsl_Expression"] = None, myDsl_Statement94: "myDsl_Try_statement" = None, myDsl_Statement97: "myDsl_Statement" = None, myDsl_Statement95: "myDsl_Statement" = None, myDsl_Statement75: "myDsl_If_statement" = None, myDsl_Statement77: "myDsl_Do_Statement" = None, myDsl_Statement79: "myDsl_While_Statement" = None, myDsl_Statement81: "myDsl_For_Statement" = None, myDsl_Statement83: "myDsl_Switch_statement" = None, myDsl_Statement85: "myDsl_Expression" = None, myDsl_Statement89: "myDsl_Statement" = None, myDsl_Statement87: "myDsl_Statement" = None, myDsl_Statement91: "myDsl_Statement_block" = None, myDsl_Statement112: "myDsl_For_Statement" = None, myDsl_Statement192: "myDsl_Switch_statement" = None, myDsl_Statement207: "myDsl_If_statement" = None, myDsl_Statement210: "myDsl_If_statement" = None, myDsl_Statement198: "myDsl_While_Statement" = None, myDsl_Statement201: "myDsl_Do_Statement" = None, myDsl_Statement213: "myDsl_Try_statement" = None, myDsl_Statement219: "myDsl_Try_statement" = None, myDsl_Statement222: "myDsl_Try_statement" = None):
        self.nameStatement = nameStatement
        self.name = name
        self.g = g
        self.rparent = rparent
        self.ret = ret
        self.myDsl_Statement = myDsl_Statement
        self.myDsl_Statement69 = myDsl_Statement69
        self.myDsl_Statement72 = myDsl_Statement72 if myDsl_Statement72 is not None else set()
        self.myDsl_Statement94 = myDsl_Statement94
        self.myDsl_Statement97 = myDsl_Statement97
        self.myDsl_Statement95 = myDsl_Statement95
        self.myDsl_Statement75 = myDsl_Statement75
        self.myDsl_Statement77 = myDsl_Statement77
        self.myDsl_Statement79 = myDsl_Statement79
        self.myDsl_Statement81 = myDsl_Statement81
        self.myDsl_Statement83 = myDsl_Statement83
        self.myDsl_Statement85 = myDsl_Statement85
        self.myDsl_Statement89 = myDsl_Statement89
        self.myDsl_Statement87 = myDsl_Statement87
        self.myDsl_Statement91 = myDsl_Statement91
        self.myDsl_Statement112 = myDsl_Statement112
        self.myDsl_Statement192 = myDsl_Statement192
        self.myDsl_Statement207 = myDsl_Statement207
        self.myDsl_Statement210 = myDsl_Statement210
        self.myDsl_Statement198 = myDsl_Statement198
        self.myDsl_Statement201 = myDsl_Statement201
        self.myDsl_Statement213 = myDsl_Statement213
        self.myDsl_Statement219 = myDsl_Statement219
        self.myDsl_Statement222 = myDsl_Statement222
        
    @property
    def g(self) -> str:
        return self.__g

    @g.setter
    def g(self, g: str):
        self.__g = g

    @property
    def ret(self) -> str:
        return self.__ret

    @ret.setter
    def ret(self, ret: str):
        self.__ret = ret

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rparent(self) -> str:
        return self.__rparent

    @rparent.setter
    def rparent(self, rparent: str):
        self.__rparent = rparent

    @property
    def nameStatement(self) -> str:
        return self.__nameStatement

    @nameStatement.setter
    def nameStatement(self, nameStatement: str):
        self.__nameStatement = nameStatement

    @property
    def myDsl_Statement69(self):
        return self.__myDsl_Statement69

    @myDsl_Statement69.setter
    def myDsl_Statement69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement69", None)
        self.__myDsl_Statement69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Variable_declaration70"):
                opp_val = getattr(old_value, "myDsl_Variable_declaration70", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Variable_declaration70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Variable_declaration70"):
                opp_val = getattr(value, "myDsl_Variable_declaration70", None)
                setattr(value, "myDsl_Variable_declaration70", self)

    @property
    def myDsl_Statement83(self):
        return self.__myDsl_Statement83

    @myDsl_Statement83.setter
    def myDsl_Statement83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement83", None)
        self.__myDsl_Statement83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Switch_statement"):
                opp_val = getattr(old_value, "myDsl_Switch_statement", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Switch_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Switch_statement"):
                opp_val = getattr(value, "myDsl_Switch_statement", None)
                setattr(value, "myDsl_Switch_statement", self)

    @property
    def myDsl_Statement198(self):
        return self.__myDsl_Statement198

    @myDsl_Statement198.setter
    def myDsl_Statement198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement198", None)
        self.__myDsl_Statement198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_While_Statement197"):
                opp_val = getattr(old_value, "myDsl_While_Statement197", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_While_Statement197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_While_Statement197"):
                opp_val = getattr(value, "myDsl_While_Statement197", None)
                setattr(value, "myDsl_While_Statement197", self)

    @property
    def myDsl_Statement219(self):
        return self.__myDsl_Statement219

    @myDsl_Statement219.setter
    def myDsl_Statement219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement219", None)
        self.__myDsl_Statement219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Try_statement218"):
                opp_val = getattr(old_value, "myDsl_Try_statement218", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Try_statement218"):
                opp_val = getattr(value, "myDsl_Try_statement218", None)
                if opp_val is None:
                    setattr(value, "myDsl_Try_statement218", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Statement72(self):
        return self.__myDsl_Statement72

    @myDsl_Statement72.setter
    def myDsl_Statement72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement72", None)
        self.__myDsl_Statement72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Expression73"):
                    opp_val = getattr(item, "myDsl_Expression73", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Expression73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Expression73"):
                    opp_val = getattr(item, "myDsl_Expression73", None)
                    
                    setattr(item, "myDsl_Expression73", self)
                    

    @property
    def myDsl_Statement192(self):
        return self.__myDsl_Statement192

    @myDsl_Statement192.setter
    def myDsl_Statement192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement192", None)
        self.__myDsl_Statement192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Switch_statement191"):
                opp_val = getattr(old_value, "myDsl_Switch_statement191", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Switch_statement191"):
                opp_val = getattr(value, "myDsl_Switch_statement191", None)
                if opp_val is None:
                    setattr(value, "myDsl_Switch_statement191", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Statement75(self):
        return self.__myDsl_Statement75

    @myDsl_Statement75.setter
    def myDsl_Statement75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement75", None)
        self.__myDsl_Statement75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_If_statement"):
                opp_val = getattr(old_value, "myDsl_If_statement", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_If_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_If_statement"):
                opp_val = getattr(value, "myDsl_If_statement", None)
                setattr(value, "myDsl_If_statement", self)

    @property
    def myDsl_Statement97(self):
        return self.__myDsl_Statement97

    @myDsl_Statement97.setter
    def myDsl_Statement97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement97", None)
        self.__myDsl_Statement97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement95"):
                opp_val = getattr(old_value, "myDsl_Statement95", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement95"):
                opp_val = getattr(value, "myDsl_Statement95", None)
                setattr(value, "myDsl_Statement95", self)

    @property
    def myDsl_Statement222(self):
        return self.__myDsl_Statement222

    @myDsl_Statement222.setter
    def myDsl_Statement222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement222", None)
        self.__myDsl_Statement222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Try_statement221"):
                opp_val = getattr(old_value, "myDsl_Try_statement221", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Try_statement221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Try_statement221"):
                opp_val = getattr(value, "myDsl_Try_statement221", None)
                setattr(value, "myDsl_Try_statement221", self)

    @property
    def myDsl_Statement201(self):
        return self.__myDsl_Statement201

    @myDsl_Statement201.setter
    def myDsl_Statement201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement201", None)
        self.__myDsl_Statement201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Do_Statement200"):
                opp_val = getattr(old_value, "myDsl_Do_Statement200", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Do_Statement200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Do_Statement200"):
                opp_val = getattr(value, "myDsl_Do_Statement200", None)
                setattr(value, "myDsl_Do_Statement200", self)

    @property
    def myDsl_Statement91(self):
        return self.__myDsl_Statement91

    @myDsl_Statement91.setter
    def myDsl_Statement91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement91", None)
        self.__myDsl_Statement91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement_block92"):
                opp_val = getattr(old_value, "myDsl_Statement_block92", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement_block92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement_block92"):
                opp_val = getattr(value, "myDsl_Statement_block92", None)
                setattr(value, "myDsl_Statement_block92", self)

    @property
    def myDsl_Statement95(self):
        return self.__myDsl_Statement95

    @myDsl_Statement95.setter
    def myDsl_Statement95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement95", None)
        self.__myDsl_Statement95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement97"):
                opp_val = getattr(old_value, "myDsl_Statement97", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement97"):
                opp_val = getattr(value, "myDsl_Statement97", None)
                setattr(value, "myDsl_Statement97", self)

    @property
    def myDsl_Statement210(self):
        return self.__myDsl_Statement210

    @myDsl_Statement210.setter
    def myDsl_Statement210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement210", None)
        self.__myDsl_Statement210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_If_statement209"):
                opp_val = getattr(old_value, "myDsl_If_statement209", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_If_statement209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_If_statement209"):
                opp_val = getattr(value, "myDsl_If_statement209", None)
                setattr(value, "myDsl_If_statement209", self)

    @property
    def myDsl_Statement94(self):
        return self.__myDsl_Statement94

    @myDsl_Statement94.setter
    def myDsl_Statement94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement94", None)
        self.__myDsl_Statement94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Try_statement"):
                opp_val = getattr(old_value, "myDsl_Try_statement", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Try_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Try_statement"):
                opp_val = getattr(value, "myDsl_Try_statement", None)
                setattr(value, "myDsl_Try_statement", self)

    @property
    def myDsl_Statement87(self):
        return self.__myDsl_Statement87

    @myDsl_Statement87.setter
    def myDsl_Statement87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement87", None)
        self.__myDsl_Statement87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement89"):
                opp_val = getattr(old_value, "myDsl_Statement89", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement89"):
                opp_val = getattr(value, "myDsl_Statement89", None)
                setattr(value, "myDsl_Statement89", self)

    @property
    def myDsl_Statement207(self):
        return self.__myDsl_Statement207

    @myDsl_Statement207.setter
    def myDsl_Statement207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement207", None)
        self.__myDsl_Statement207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_If_statement206"):
                opp_val = getattr(old_value, "myDsl_If_statement206", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_If_statement206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_If_statement206"):
                opp_val = getattr(value, "myDsl_If_statement206", None)
                setattr(value, "myDsl_If_statement206", self)

    @property
    def myDsl_Statement112(self):
        return self.__myDsl_Statement112

    @myDsl_Statement112.setter
    def myDsl_Statement112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement112", None)
        self.__myDsl_Statement112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_For_Statement111"):
                opp_val = getattr(old_value, "myDsl_For_Statement111", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_For_Statement111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_For_Statement111"):
                opp_val = getattr(value, "myDsl_For_Statement111", None)
                setattr(value, "myDsl_For_Statement111", self)

    @property
    def myDsl_Statement77(self):
        return self.__myDsl_Statement77

    @myDsl_Statement77.setter
    def myDsl_Statement77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement77", None)
        self.__myDsl_Statement77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Do_Statement"):
                opp_val = getattr(old_value, "myDsl_Do_Statement", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Do_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Do_Statement"):
                opp_val = getattr(value, "myDsl_Do_Statement", None)
                setattr(value, "myDsl_Do_Statement", self)

    @property
    def myDsl_Statement(self):
        return self.__myDsl_Statement

    @myDsl_Statement.setter
    def myDsl_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement", None)
        self.__myDsl_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement_block67"):
                opp_val = getattr(old_value, "myDsl_Statement_block67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement_block67"):
                opp_val = getattr(value, "myDsl_Statement_block67", None)
                if opp_val is None:
                    setattr(value, "myDsl_Statement_block67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Statement85(self):
        return self.__myDsl_Statement85

    @myDsl_Statement85.setter
    def myDsl_Statement85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement85", None)
        self.__myDsl_Statement85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Expression86"):
                opp_val = getattr(old_value, "myDsl_Expression86", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Expression86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Expression86"):
                opp_val = getattr(value, "myDsl_Expression86", None)
                setattr(value, "myDsl_Expression86", self)

    @property
    def myDsl_Statement81(self):
        return self.__myDsl_Statement81

    @myDsl_Statement81.setter
    def myDsl_Statement81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement81", None)
        self.__myDsl_Statement81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_For_Statement"):
                opp_val = getattr(old_value, "myDsl_For_Statement", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_For_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_For_Statement"):
                opp_val = getattr(value, "myDsl_For_Statement", None)
                setattr(value, "myDsl_For_Statement", self)

    @property
    def myDsl_Statement89(self):
        return self.__myDsl_Statement89

    @myDsl_Statement89.setter
    def myDsl_Statement89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement89", None)
        self.__myDsl_Statement89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement87"):
                opp_val = getattr(old_value, "myDsl_Statement87", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement87"):
                opp_val = getattr(value, "myDsl_Statement87", None)
                setattr(value, "myDsl_Statement87", self)

    @property
    def myDsl_Statement213(self):
        return self.__myDsl_Statement213

    @myDsl_Statement213.setter
    def myDsl_Statement213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement213", None)
        self.__myDsl_Statement213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Try_statement212"):
                opp_val = getattr(old_value, "myDsl_Try_statement212", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Try_statement212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Try_statement212"):
                opp_val = getattr(value, "myDsl_Try_statement212", None)
                setattr(value, "myDsl_Try_statement212", self)

    @property
    def myDsl_Statement79(self):
        return self.__myDsl_Statement79

    @myDsl_Statement79.setter
    def myDsl_Statement79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement__myDsl_Statement79", None)
        self.__myDsl_Statement79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_While_Statement"):
                opp_val = getattr(old_value, "myDsl_While_Statement", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_While_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_While_Statement"):
                opp_val = getattr(value, "myDsl_While_Statement", None)
                setattr(value, "myDsl_While_Statement", self)

class myDsl_Parameter:

    def __init__(self, parameterName: str, myDsl_Parameter: "myDsl_Parameter_list" = None, myDsl_Parameter40: "myDsl_Parameter_list" = None, myDsl_Parameter42: "myDsl_Type" = None, myDsl_Parameter216: "myDsl_Try_statement" = None):
        self.parameterName = parameterName
        self.myDsl_Parameter = myDsl_Parameter
        self.myDsl_Parameter40 = myDsl_Parameter40
        self.myDsl_Parameter42 = myDsl_Parameter42
        self.myDsl_Parameter216 = myDsl_Parameter216
        
    @property
    def parameterName(self) -> str:
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName

    @property
    def myDsl_Parameter42(self):
        return self.__myDsl_Parameter42

    @myDsl_Parameter42.setter
    def myDsl_Parameter42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Parameter__myDsl_Parameter42", None)
        self.__myDsl_Parameter42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type43"):
                opp_val = getattr(old_value, "myDsl_Type43", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type43"):
                opp_val = getattr(value, "myDsl_Type43", None)
                setattr(value, "myDsl_Type43", self)

    @property
    def myDsl_Parameter(self):
        return self.__myDsl_Parameter

    @myDsl_Parameter.setter
    def myDsl_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Parameter__myDsl_Parameter", None)
        self.__myDsl_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Parameter_list37"):
                opp_val = getattr(old_value, "myDsl_Parameter_list37", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Parameter_list37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Parameter_list37"):
                opp_val = getattr(value, "myDsl_Parameter_list37", None)
                setattr(value, "myDsl_Parameter_list37", self)

    @property
    def myDsl_Parameter40(self):
        return self.__myDsl_Parameter40

    @myDsl_Parameter40.setter
    def myDsl_Parameter40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Parameter__myDsl_Parameter40", None)
        self.__myDsl_Parameter40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Parameter_list39"):
                opp_val = getattr(old_value, "myDsl_Parameter_list39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Parameter_list39"):
                opp_val = getattr(value, "myDsl_Parameter_list39", None)
                if opp_val is None:
                    setattr(value, "myDsl_Parameter_list39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Parameter216(self):
        return self.__myDsl_Parameter216

    @myDsl_Parameter216.setter
    def myDsl_Parameter216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Parameter__myDsl_Parameter216", None)
        self.__myDsl_Parameter216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Try_statement215"):
                opp_val = getattr(old_value, "myDsl_Try_statement215", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Try_statement215"):
                opp_val = getattr(value, "myDsl_Try_statement215", None)
                if opp_val is None:
                    setattr(value, "myDsl_Try_statement215", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Statement_block:

    def __init__(self, rCurly: str, lCurly: str, myDsl_Statement_block: "myDsl_Method_declaration" = None, myDsl_Statement_block35: "myDsl_Constructor_declaration" = None, myDsl_Statement_block67: set["myDsl_Statement"] = None, myDsl_Statement_block65: "myDsl_Static_initializer" = None, myDsl_Statement_block92: "myDsl_Statement" = None):
        self.rCurly = rCurly
        self.lCurly = lCurly
        self.myDsl_Statement_block = myDsl_Statement_block
        self.myDsl_Statement_block35 = myDsl_Statement_block35
        self.myDsl_Statement_block67 = myDsl_Statement_block67 if myDsl_Statement_block67 is not None else set()
        self.myDsl_Statement_block65 = myDsl_Statement_block65
        self.myDsl_Statement_block92 = myDsl_Statement_block92
        
    @property
    def rCurly(self) -> str:
        return self.__rCurly

    @rCurly.setter
    def rCurly(self, rCurly: str):
        self.__rCurly = rCurly

    @property
    def lCurly(self) -> str:
        return self.__lCurly

    @lCurly.setter
    def lCurly(self, lCurly: str):
        self.__lCurly = lCurly

    @property
    def myDsl_Statement_block(self):
        return self.__myDsl_Statement_block

    @myDsl_Statement_block.setter
    def myDsl_Statement_block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement_block__myDsl_Statement_block", None)
        self.__myDsl_Statement_block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Method_declaration29"):
                opp_val = getattr(old_value, "myDsl_Method_declaration29", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Method_declaration29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Method_declaration29"):
                opp_val = getattr(value, "myDsl_Method_declaration29", None)
                setattr(value, "myDsl_Method_declaration29", self)

    @property
    def myDsl_Statement_block67(self):
        return self.__myDsl_Statement_block67

    @myDsl_Statement_block67.setter
    def myDsl_Statement_block67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement_block__myDsl_Statement_block67", None)
        self.__myDsl_Statement_block67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Statement"):
                    opp_val = getattr(item, "myDsl_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Statement"):
                    opp_val = getattr(item, "myDsl_Statement", None)
                    
                    setattr(item, "myDsl_Statement", self)
                    

    @property
    def myDsl_Statement_block35(self):
        return self.__myDsl_Statement_block35

    @myDsl_Statement_block35.setter
    def myDsl_Statement_block35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement_block__myDsl_Statement_block35", None)
        self.__myDsl_Statement_block35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Constructor_declaration34"):
                opp_val = getattr(old_value, "myDsl_Constructor_declaration34", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Constructor_declaration34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Constructor_declaration34"):
                opp_val = getattr(value, "myDsl_Constructor_declaration34", None)
                setattr(value, "myDsl_Constructor_declaration34", self)

    @property
    def myDsl_Statement_block65(self):
        return self.__myDsl_Statement_block65

    @myDsl_Statement_block65.setter
    def myDsl_Statement_block65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement_block__myDsl_Statement_block65", None)
        self.__myDsl_Statement_block65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Static_initializer64"):
                opp_val = getattr(old_value, "myDsl_Static_initializer64", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Static_initializer64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Static_initializer64"):
                opp_val = getattr(value, "myDsl_Static_initializer64", None)
                setattr(value, "myDsl_Static_initializer64", self)

    @property
    def myDsl_Statement_block92(self):
        return self.__myDsl_Statement_block92

    @myDsl_Statement_block92.setter
    def myDsl_Statement_block92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Statement_block__myDsl_Statement_block92", None)
        self.__myDsl_Statement_block92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement91"):
                opp_val = getattr(old_value, "myDsl_Statement91", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement91"):
                opp_val = getattr(value, "myDsl_Statement91", None)
                setattr(value, "myDsl_Statement91", self)

class myDsl_Variable_declarator:

    def __init__(self, nameVariable: str, lenVector: str, myDsl_Variable_declarator: "myDsl_Variable_declaration" = None, myDsl_Variable_declarator51: "myDsl_Variable_declaration" = None, myDsl_Variable_declarator53: "myDsl_Variable_initializer" = None):
        self.nameVariable = nameVariable
        self.lenVector = lenVector
        self.myDsl_Variable_declarator = myDsl_Variable_declarator
        self.myDsl_Variable_declarator51 = myDsl_Variable_declarator51
        self.myDsl_Variable_declarator53 = myDsl_Variable_declarator53
        
    @property
    def lenVector(self) -> str:
        return self.__lenVector

    @lenVector.setter
    def lenVector(self, lenVector: str):
        self.__lenVector = lenVector

    @property
    def nameVariable(self) -> str:
        return self.__nameVariable

    @nameVariable.setter
    def nameVariable(self, nameVariable: str):
        self.__nameVariable = nameVariable

    @property
    def myDsl_Variable_declarator53(self):
        return self.__myDsl_Variable_declarator53

    @myDsl_Variable_declarator53.setter
    def myDsl_Variable_declarator53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Variable_declarator__myDsl_Variable_declarator53", None)
        self.__myDsl_Variable_declarator53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Variable_initializer"):
                opp_val = getattr(old_value, "myDsl_Variable_initializer", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Variable_initializer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Variable_initializer"):
                opp_val = getattr(value, "myDsl_Variable_initializer", None)
                setattr(value, "myDsl_Variable_initializer", self)

    @property
    def myDsl_Variable_declarator(self):
        return self.__myDsl_Variable_declarator

    @myDsl_Variable_declarator.setter
    def myDsl_Variable_declarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Variable_declarator__myDsl_Variable_declarator", None)
        self.__myDsl_Variable_declarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Variable_declaration48"):
                opp_val = getattr(old_value, "myDsl_Variable_declaration48", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Variable_declaration48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Variable_declaration48"):
                opp_val = getattr(value, "myDsl_Variable_declaration48", None)
                setattr(value, "myDsl_Variable_declaration48", self)

    @property
    def myDsl_Variable_declarator51(self):
        return self.__myDsl_Variable_declarator51

    @myDsl_Variable_declarator51.setter
    def myDsl_Variable_declarator51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Variable_declarator__myDsl_Variable_declarator51", None)
        self.__myDsl_Variable_declarator51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Variable_declaration50"):
                opp_val = getattr(old_value, "myDsl_Variable_declaration50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Variable_declaration50"):
                opp_val = getattr(value, "myDsl_Variable_declaration50", None)
                if opp_val is None:
                    setattr(value, "myDsl_Variable_declaration50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Method_declaration:

    def __init__(self, modifiersMethod: str, nameMethod: str, lParen: str, rparent: str, debug: str, myDsl_Method_declaration25: "myDsl_Type" = None, myDsl_Method_declaration27: "myDsl_Parameter_list" = None, myDsl_Method_declaration: "myDsl_Field_declaration" = None, myDsl_Method_declaration29: "myDsl_Statement_block" = None):
        self.modifiersMethod = modifiersMethod
        self.nameMethod = nameMethod
        self.lParen = lParen
        self.rparent = rparent
        self.debug = debug
        self.myDsl_Method_declaration25 = myDsl_Method_declaration25
        self.myDsl_Method_declaration27 = myDsl_Method_declaration27
        self.myDsl_Method_declaration = myDsl_Method_declaration
        self.myDsl_Method_declaration29 = myDsl_Method_declaration29
        
    @property
    def lParen(self) -> str:
        return self.__lParen

    @lParen.setter
    def lParen(self, lParen: str):
        self.__lParen = lParen

    @property
    def modifiersMethod(self) -> str:
        return self.__modifiersMethod

    @modifiersMethod.setter
    def modifiersMethod(self, modifiersMethod: str):
        self.__modifiersMethod = modifiersMethod

    @property
    def debug(self) -> str:
        return self.__debug

    @debug.setter
    def debug(self, debug: str):
        self.__debug = debug

    @property
    def rparent(self) -> str:
        return self.__rparent

    @rparent.setter
    def rparent(self, rparent: str):
        self.__rparent = rparent

    @property
    def nameMethod(self) -> str:
        return self.__nameMethod

    @nameMethod.setter
    def nameMethod(self, nameMethod: str):
        self.__nameMethod = nameMethod

    @property
    def myDsl_Method_declaration27(self):
        return self.__myDsl_Method_declaration27

    @myDsl_Method_declaration27.setter
    def myDsl_Method_declaration27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Method_declaration__myDsl_Method_declaration27", None)
        self.__myDsl_Method_declaration27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Parameter_list"):
                opp_val = getattr(old_value, "myDsl_Parameter_list", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Parameter_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Parameter_list"):
                opp_val = getattr(value, "myDsl_Parameter_list", None)
                setattr(value, "myDsl_Parameter_list", self)

    @property
    def myDsl_Method_declaration25(self):
        return self.__myDsl_Method_declaration25

    @myDsl_Method_declaration25.setter
    def myDsl_Method_declaration25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Method_declaration__myDsl_Method_declaration25", None)
        self.__myDsl_Method_declaration25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type"):
                opp_val = getattr(old_value, "myDsl_Type", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type"):
                opp_val = getattr(value, "myDsl_Type", None)
                setattr(value, "myDsl_Type", self)

    @property
    def myDsl_Method_declaration29(self):
        return self.__myDsl_Method_declaration29

    @myDsl_Method_declaration29.setter
    def myDsl_Method_declaration29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Method_declaration__myDsl_Method_declaration29", None)
        self.__myDsl_Method_declaration29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement_block"):
                opp_val = getattr(old_value, "myDsl_Statement_block", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement_block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement_block"):
                opp_val = getattr(value, "myDsl_Statement_block", None)
                setattr(value, "myDsl_Statement_block", self)

    @property
    def myDsl_Method_declaration(self):
        return self.__myDsl_Method_declaration

    @myDsl_Method_declaration.setter
    def myDsl_Method_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Method_declaration__myDsl_Method_declaration", None)
        self.__myDsl_Method_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Field_declaration21"):
                opp_val = getattr(old_value, "myDsl_Field_declaration21", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Field_declaration21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Field_declaration21"):
                opp_val = getattr(value, "myDsl_Field_declaration21", None)
                setattr(value, "myDsl_Field_declaration21", self)

class myDsl_Constructor_declaration:

    def __init__(self, modifiersConstructor: str, nameConstructor: str, lParen: str, rparent: str, myDsl_Constructor_declaration: "myDsl_Field_declaration" = None, myDsl_Constructor_declaration31: "myDsl_Parameter_list" = None, myDsl_Constructor_declaration34: "myDsl_Statement_block" = None):
        self.modifiersConstructor = modifiersConstructor
        self.nameConstructor = nameConstructor
        self.lParen = lParen
        self.rparent = rparent
        self.myDsl_Constructor_declaration = myDsl_Constructor_declaration
        self.myDsl_Constructor_declaration31 = myDsl_Constructor_declaration31
        self.myDsl_Constructor_declaration34 = myDsl_Constructor_declaration34
        
    @property
    def lParen(self) -> str:
        return self.__lParen

    @lParen.setter
    def lParen(self, lParen: str):
        self.__lParen = lParen

    @property
    def rparent(self) -> str:
        return self.__rparent

    @rparent.setter
    def rparent(self, rparent: str):
        self.__rparent = rparent

    @property
    def nameConstructor(self) -> str:
        return self.__nameConstructor

    @nameConstructor.setter
    def nameConstructor(self, nameConstructor: str):
        self.__nameConstructor = nameConstructor

    @property
    def modifiersConstructor(self) -> str:
        return self.__modifiersConstructor

    @modifiersConstructor.setter
    def modifiersConstructor(self, modifiersConstructor: str):
        self.__modifiersConstructor = modifiersConstructor

    @property
    def myDsl_Constructor_declaration(self):
        return self.__myDsl_Constructor_declaration

    @myDsl_Constructor_declaration.setter
    def myDsl_Constructor_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Constructor_declaration__myDsl_Constructor_declaration", None)
        self.__myDsl_Constructor_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Field_declaration19"):
                opp_val = getattr(old_value, "myDsl_Field_declaration19", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Field_declaration19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Field_declaration19"):
                opp_val = getattr(value, "myDsl_Field_declaration19", None)
                setattr(value, "myDsl_Field_declaration19", self)

    @property
    def myDsl_Constructor_declaration31(self):
        return self.__myDsl_Constructor_declaration31

    @myDsl_Constructor_declaration31.setter
    def myDsl_Constructor_declaration31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Constructor_declaration__myDsl_Constructor_declaration31", None)
        self.__myDsl_Constructor_declaration31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Parameter_list32"):
                opp_val = getattr(old_value, "myDsl_Parameter_list32", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Parameter_list32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Parameter_list32"):
                opp_val = getattr(value, "myDsl_Parameter_list32", None)
                setattr(value, "myDsl_Parameter_list32", self)

    @property
    def myDsl_Constructor_declaration34(self):
        return self.__myDsl_Constructor_declaration34

    @myDsl_Constructor_declaration34.setter
    def myDsl_Constructor_declaration34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Constructor_declaration__myDsl_Constructor_declaration34", None)
        self.__myDsl_Constructor_declaration34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement_block35"):
                opp_val = getattr(old_value, "myDsl_Statement_block35", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement_block35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement_block35"):
                opp_val = getattr(value, "myDsl_Statement_block35", None)
                setattr(value, "myDsl_Statement_block35", self)

class myDsl_Variable_declaration:

    def __init__(self, modifiersVariable: str, myDsl_Variable_declaration: "myDsl_Field_declaration" = None, myDsl_Variable_declaration45: "myDsl_Type" = None, myDsl_Variable_declaration48: "myDsl_Variable_declarator" = None, myDsl_Variable_declaration50: set["myDsl_Variable_declarator"] = None, myDsl_Variable_declaration70: "myDsl_Statement" = None, myDsl_Variable_declaration100: "myDsl_For_Statement" = None):
        self.modifiersVariable = modifiersVariable
        self.myDsl_Variable_declaration = myDsl_Variable_declaration
        self.myDsl_Variable_declaration45 = myDsl_Variable_declaration45
        self.myDsl_Variable_declaration48 = myDsl_Variable_declaration48
        self.myDsl_Variable_declaration50 = myDsl_Variable_declaration50 if myDsl_Variable_declaration50 is not None else set()
        self.myDsl_Variable_declaration70 = myDsl_Variable_declaration70
        self.myDsl_Variable_declaration100 = myDsl_Variable_declaration100
        
    @property
    def modifiersVariable(self) -> str:
        return self.__modifiersVariable

    @modifiersVariable.setter
    def modifiersVariable(self, modifiersVariable: str):
        self.__modifiersVariable = modifiersVariable

    @property
    def myDsl_Variable_declaration(self):
        return self.__myDsl_Variable_declaration

    @myDsl_Variable_declaration.setter
    def myDsl_Variable_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Variable_declaration__myDsl_Variable_declaration", None)
        self.__myDsl_Variable_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Field_declaration17"):
                opp_val = getattr(old_value, "myDsl_Field_declaration17", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Field_declaration17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Field_declaration17"):
                opp_val = getattr(value, "myDsl_Field_declaration17", None)
                setattr(value, "myDsl_Field_declaration17", self)

    @property
    def myDsl_Variable_declaration100(self):
        return self.__myDsl_Variable_declaration100

    @myDsl_Variable_declaration100.setter
    def myDsl_Variable_declaration100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Variable_declaration__myDsl_Variable_declaration100", None)
        self.__myDsl_Variable_declaration100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_For_Statement99"):
                opp_val = getattr(old_value, "myDsl_For_Statement99", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_For_Statement99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_For_Statement99"):
                opp_val = getattr(value, "myDsl_For_Statement99", None)
                setattr(value, "myDsl_For_Statement99", self)

    @property
    def myDsl_Variable_declaration50(self):
        return self.__myDsl_Variable_declaration50

    @myDsl_Variable_declaration50.setter
    def myDsl_Variable_declaration50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Variable_declaration__myDsl_Variable_declaration50", None)
        self.__myDsl_Variable_declaration50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Variable_declarator51"):
                    opp_val = getattr(item, "myDsl_Variable_declarator51", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Variable_declarator51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Variable_declarator51"):
                    opp_val = getattr(item, "myDsl_Variable_declarator51", None)
                    
                    setattr(item, "myDsl_Variable_declarator51", self)
                    

    @property
    def myDsl_Variable_declaration48(self):
        return self.__myDsl_Variable_declaration48

    @myDsl_Variable_declaration48.setter
    def myDsl_Variable_declaration48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Variable_declaration__myDsl_Variable_declaration48", None)
        self.__myDsl_Variable_declaration48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Variable_declarator"):
                opp_val = getattr(old_value, "myDsl_Variable_declarator", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Variable_declarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Variable_declarator"):
                opp_val = getattr(value, "myDsl_Variable_declarator", None)
                setattr(value, "myDsl_Variable_declarator", self)

    @property
    def myDsl_Variable_declaration45(self):
        return self.__myDsl_Variable_declaration45

    @myDsl_Variable_declaration45.setter
    def myDsl_Variable_declaration45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Variable_declaration__myDsl_Variable_declaration45", None)
        self.__myDsl_Variable_declaration45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type46"):
                opp_val = getattr(old_value, "myDsl_Type46", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type46"):
                opp_val = getattr(value, "myDsl_Type46", None)
                setattr(value, "myDsl_Type46", self)

    @property
    def myDsl_Variable_declaration70(self):
        return self.__myDsl_Variable_declaration70

    @myDsl_Variable_declaration70.setter
    def myDsl_Variable_declaration70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Variable_declaration__myDsl_Variable_declaration70", None)
        self.__myDsl_Variable_declaration70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement69"):
                opp_val = getattr(old_value, "myDsl_Statement69", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement69"):
                opp_val = getattr(value, "myDsl_Statement69", None)
                setattr(value, "myDsl_Statement69", self)

class myDsl_Field_declaration:

    def __init__(self, comment: str, myDsl_Field_declaration23: "myDsl_Static_initializer" = None, myDsl_Field_declaration: "myDsl_Interface_declaration" = None, myDsl_Field_declaration15: "myDsl_Class_declaration" = None, myDsl_Field_declaration17: "myDsl_Variable_declaration" = None, myDsl_Field_declaration19: "myDsl_Constructor_declaration" = None, myDsl_Field_declaration21: "myDsl_Method_declaration" = None):
        self.comment = comment
        self.myDsl_Field_declaration23 = myDsl_Field_declaration23
        self.myDsl_Field_declaration = myDsl_Field_declaration
        self.myDsl_Field_declaration15 = myDsl_Field_declaration15
        self.myDsl_Field_declaration17 = myDsl_Field_declaration17
        self.myDsl_Field_declaration19 = myDsl_Field_declaration19
        self.myDsl_Field_declaration21 = myDsl_Field_declaration21
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def myDsl_Field_declaration15(self):
        return self.__myDsl_Field_declaration15

    @myDsl_Field_declaration15.setter
    def myDsl_Field_declaration15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Field_declaration__myDsl_Field_declaration15", None)
        self.__myDsl_Field_declaration15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Class_declaration14"):
                opp_val = getattr(old_value, "myDsl_Class_declaration14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Class_declaration14"):
                opp_val = getattr(value, "myDsl_Class_declaration14", None)
                if opp_val is None:
                    setattr(value, "myDsl_Class_declaration14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Field_declaration19(self):
        return self.__myDsl_Field_declaration19

    @myDsl_Field_declaration19.setter
    def myDsl_Field_declaration19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Field_declaration__myDsl_Field_declaration19", None)
        self.__myDsl_Field_declaration19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Constructor_declaration"):
                opp_val = getattr(old_value, "myDsl_Constructor_declaration", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Constructor_declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Constructor_declaration"):
                opp_val = getattr(value, "myDsl_Constructor_declaration", None)
                setattr(value, "myDsl_Constructor_declaration", self)

    @property
    def myDsl_Field_declaration17(self):
        return self.__myDsl_Field_declaration17

    @myDsl_Field_declaration17.setter
    def myDsl_Field_declaration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Field_declaration__myDsl_Field_declaration17", None)
        self.__myDsl_Field_declaration17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Variable_declaration"):
                opp_val = getattr(old_value, "myDsl_Variable_declaration", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Variable_declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Variable_declaration"):
                opp_val = getattr(value, "myDsl_Variable_declaration", None)
                setattr(value, "myDsl_Variable_declaration", self)

    @property
    def myDsl_Field_declaration(self):
        return self.__myDsl_Field_declaration

    @myDsl_Field_declaration.setter
    def myDsl_Field_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Field_declaration__myDsl_Field_declaration", None)
        self.__myDsl_Field_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Interface_declaration12"):
                opp_val = getattr(old_value, "myDsl_Interface_declaration12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Interface_declaration12"):
                opp_val = getattr(value, "myDsl_Interface_declaration12", None)
                if opp_val is None:
                    setattr(value, "myDsl_Interface_declaration12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Field_declaration21(self):
        return self.__myDsl_Field_declaration21

    @myDsl_Field_declaration21.setter
    def myDsl_Field_declaration21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Field_declaration__myDsl_Field_declaration21", None)
        self.__myDsl_Field_declaration21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Method_declaration"):
                opp_val = getattr(old_value, "myDsl_Method_declaration", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Method_declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Method_declaration"):
                opp_val = getattr(value, "myDsl_Method_declaration", None)
                setattr(value, "myDsl_Method_declaration", self)

    @property
    def myDsl_Field_declaration23(self):
        return self.__myDsl_Field_declaration23

    @myDsl_Field_declaration23.setter
    def myDsl_Field_declaration23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Field_declaration__myDsl_Field_declaration23", None)
        self.__myDsl_Field_declaration23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Static_initializer"):
                opp_val = getattr(old_value, "myDsl_Static_initializer", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Static_initializer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Static_initializer"):
                opp_val = getattr(value, "myDsl_Static_initializer", None)
                setattr(value, "myDsl_Static_initializer", self)

class myDsl_Parameter_list:

    pass
class myDsl_Type:

    def __init__(self, typeVector: str, myDsl_Type: "myDsl_Method_declaration" = None, myDsl_Type46: "myDsl_Variable_declaration" = None, myDsl_Type43: "myDsl_Parameter" = None, myDsl_Type62: "myDsl_Type_specifier" = None, myDsl_Type165: "myDsl_Cast_Expression" = None):
        self.typeVector = typeVector
        self.myDsl_Type = myDsl_Type
        self.myDsl_Type46 = myDsl_Type46
        self.myDsl_Type43 = myDsl_Type43
        self.myDsl_Type62 = myDsl_Type62
        self.myDsl_Type165 = myDsl_Type165
        
    @property
    def typeVector(self) -> str:
        return self.__typeVector

    @typeVector.setter
    def typeVector(self, typeVector: str):
        self.__typeVector = typeVector

    @property
    def myDsl_Type62(self):
        return self.__myDsl_Type62

    @myDsl_Type62.setter
    def myDsl_Type62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type62", None)
        self.__myDsl_Type62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type_specifier"):
                opp_val = getattr(old_value, "myDsl_Type_specifier", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type_specifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type_specifier"):
                opp_val = getattr(value, "myDsl_Type_specifier", None)
                setattr(value, "myDsl_Type_specifier", self)

    @property
    def myDsl_Type(self):
        return self.__myDsl_Type

    @myDsl_Type.setter
    def myDsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type", None)
        self.__myDsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Method_declaration25"):
                opp_val = getattr(old_value, "myDsl_Method_declaration25", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Method_declaration25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Method_declaration25"):
                opp_val = getattr(value, "myDsl_Method_declaration25", None)
                setattr(value, "myDsl_Method_declaration25", self)

    @property
    def myDsl_Type46(self):
        return self.__myDsl_Type46

    @myDsl_Type46.setter
    def myDsl_Type46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type46", None)
        self.__myDsl_Type46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Variable_declaration45"):
                opp_val = getattr(old_value, "myDsl_Variable_declaration45", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Variable_declaration45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Variable_declaration45"):
                opp_val = getattr(value, "myDsl_Variable_declaration45", None)
                setattr(value, "myDsl_Variable_declaration45", self)

    @property
    def myDsl_Type43(self):
        return self.__myDsl_Type43

    @myDsl_Type43.setter
    def myDsl_Type43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type43", None)
        self.__myDsl_Type43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Parameter42"):
                opp_val = getattr(old_value, "myDsl_Parameter42", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Parameter42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Parameter42"):
                opp_val = getattr(value, "myDsl_Parameter42", None)
                setattr(value, "myDsl_Parameter42", self)

    @property
    def myDsl_Type165(self):
        return self.__myDsl_Type165

    @myDsl_Type165.setter
    def myDsl_Type165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type165", None)
        self.__myDsl_Type165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Cast_Expression164"):
                opp_val = getattr(old_value, "myDsl_Cast_Expression164", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Cast_Expression164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Cast_Expression164"):
                opp_val = getattr(value, "myDsl_Cast_Expression164", None)
                setattr(value, "myDsl_Cast_Expression164", self)

class myDsl_Static_initializer:

    def __init__(self, static: str, myDsl_Static_initializer: "myDsl_Field_declaration" = None, myDsl_Static_initializer64: "myDsl_Statement_block" = None):
        self.static = static
        self.myDsl_Static_initializer = myDsl_Static_initializer
        self.myDsl_Static_initializer64 = myDsl_Static_initializer64
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def myDsl_Static_initializer(self):
        return self.__myDsl_Static_initializer

    @myDsl_Static_initializer.setter
    def myDsl_Static_initializer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Static_initializer__myDsl_Static_initializer", None)
        self.__myDsl_Static_initializer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Field_declaration23"):
                opp_val = getattr(old_value, "myDsl_Field_declaration23", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Field_declaration23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Field_declaration23"):
                opp_val = getattr(value, "myDsl_Field_declaration23", None)
                setattr(value, "myDsl_Field_declaration23", self)

    @property
    def myDsl_Static_initializer64(self):
        return self.__myDsl_Static_initializer64

    @myDsl_Static_initializer64.setter
    def myDsl_Static_initializer64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Static_initializer__myDsl_Static_initializer64", None)
        self.__myDsl_Static_initializer64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Statement_block65"):
                opp_val = getattr(old_value, "myDsl_Statement_block65", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Statement_block65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Statement_block65"):
                opp_val = getattr(value, "myDsl_Statement_block65", None)
                setattr(value, "myDsl_Statement_block65", self)

class myDsl_Import_statement:

    def __init__(self, pacName: str, className: str, myDsl_Import_statement: "myDsl_Compilation_unit" = None):
        self.pacName = pacName
        self.className = className
        self.myDsl_Import_statement = myDsl_Import_statement
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def pacName(self) -> str:
        return self.__pacName

    @pacName.setter
    def pacName(self, pacName: str):
        self.__pacName = pacName

    @property
    def myDsl_Import_statement(self):
        return self.__myDsl_Import_statement

    @myDsl_Import_statement.setter
    def myDsl_Import_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Import_statement__myDsl_Import_statement", None)
        self.__myDsl_Import_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Compilation_unit4"):
                opp_val = getattr(old_value, "myDsl_Compilation_unit4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Compilation_unit4"):
                opp_val = getattr(value, "myDsl_Compilation_unit4", None)
                if opp_val is None:
                    setattr(value, "myDsl_Compilation_unit4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Package_statement:

    def __init__(self, pacName: str, myDsl_Package_statement: "myDsl_Compilation_unit" = None):
        self.pacName = pacName
        self.myDsl_Package_statement = myDsl_Package_statement
        
    @property
    def pacName(self) -> str:
        return self.__pacName

    @pacName.setter
    def pacName(self, pacName: str):
        self.__pacName = pacName

    @property
    def myDsl_Package_statement(self):
        return self.__myDsl_Package_statement

    @myDsl_Package_statement.setter
    def myDsl_Package_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Package_statement__myDsl_Package_statement", None)
        self.__myDsl_Package_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Compilation_unit2"):
                opp_val = getattr(old_value, "myDsl_Compilation_unit2", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Compilation_unit2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Compilation_unit2"):
                opp_val = getattr(value, "myDsl_Compilation_unit2", None)
                setattr(value, "myDsl_Compilation_unit2", self)

class myDsl_Compilation_unit:

    pass
class myDsl_Model:

    pass
class myDsl_Interface_declaration:

    def __init__(self, modifiers: str, interfaceName: str, interfaceHerdada: str, interfacesHerdadas: str, myDsl_Interface_declaration: "myDsl_Type_declaration" = None, myDsl_Interface_declaration12: set["myDsl_Field_declaration"] = None):
        self.modifiers = modifiers
        self.interfaceName = interfaceName
        self.interfaceHerdada = interfaceHerdada
        self.interfacesHerdadas = interfacesHerdadas
        self.myDsl_Interface_declaration = myDsl_Interface_declaration
        self.myDsl_Interface_declaration12 = myDsl_Interface_declaration12 if myDsl_Interface_declaration12 is not None else set()
        
    @property
    def interfaceName(self) -> str:
        return self.__interfaceName

    @interfaceName.setter
    def interfaceName(self, interfaceName: str):
        self.__interfaceName = interfaceName

    @property
    def interfacesHerdadas(self) -> str:
        return self.__interfacesHerdadas

    @interfacesHerdadas.setter
    def interfacesHerdadas(self, interfacesHerdadas: str):
        self.__interfacesHerdadas = interfacesHerdadas

    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def interfaceHerdada(self) -> str:
        return self.__interfaceHerdada

    @interfaceHerdada.setter
    def interfaceHerdada(self, interfaceHerdada: str):
        self.__interfaceHerdada = interfaceHerdada

    @property
    def myDsl_Interface_declaration(self):
        return self.__myDsl_Interface_declaration

    @myDsl_Interface_declaration.setter
    def myDsl_Interface_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Interface_declaration__myDsl_Interface_declaration", None)
        self.__myDsl_Interface_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type_declaration10"):
                opp_val = getattr(old_value, "myDsl_Type_declaration10", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type_declaration10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type_declaration10"):
                opp_val = getattr(value, "myDsl_Type_declaration10", None)
                setattr(value, "myDsl_Type_declaration10", self)

    @property
    def myDsl_Interface_declaration12(self):
        return self.__myDsl_Interface_declaration12

    @myDsl_Interface_declaration12.setter
    def myDsl_Interface_declaration12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Interface_declaration__myDsl_Interface_declaration12", None)
        self.__myDsl_Interface_declaration12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Field_declaration"):
                    opp_val = getattr(item, "myDsl_Field_declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Field_declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Field_declaration"):
                    opp_val = getattr(item, "myDsl_Field_declaration", None)
                    
                    setattr(item, "myDsl_Field_declaration", self)
                    

class myDsl_Class_declaration:

    def __init__(self, modifiers: str, className: str, classHerdada: str, interfaceImplementada: str, interfacesImplementadas: str, myDsl_Class_declaration: "myDsl_Type_declaration" = None, myDsl_Class_declaration14: set["myDsl_Field_declaration"] = None):
        self.modifiers = modifiers
        self.className = className
        self.classHerdada = classHerdada
        self.interfaceImplementada = interfaceImplementada
        self.interfacesImplementadas = interfacesImplementadas
        self.myDsl_Class_declaration = myDsl_Class_declaration
        self.myDsl_Class_declaration14 = myDsl_Class_declaration14 if myDsl_Class_declaration14 is not None else set()
        
    @property
    def interfaceImplementada(self) -> str:
        return self.__interfaceImplementada

    @interfaceImplementada.setter
    def interfaceImplementada(self, interfaceImplementada: str):
        self.__interfaceImplementada = interfaceImplementada

    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def classHerdada(self) -> str:
        return self.__classHerdada

    @classHerdada.setter
    def classHerdada(self, classHerdada: str):
        self.__classHerdada = classHerdada

    @property
    def interfacesImplementadas(self) -> str:
        return self.__interfacesImplementadas

    @interfacesImplementadas.setter
    def interfacesImplementadas(self, interfacesImplementadas: str):
        self.__interfacesImplementadas = interfacesImplementadas

    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def myDsl_Class_declaration(self):
        return self.__myDsl_Class_declaration

    @myDsl_Class_declaration.setter
    def myDsl_Class_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Class_declaration__myDsl_Class_declaration", None)
        self.__myDsl_Class_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type_declaration8"):
                opp_val = getattr(old_value, "myDsl_Type_declaration8", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type_declaration8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type_declaration8"):
                opp_val = getattr(value, "myDsl_Type_declaration8", None)
                setattr(value, "myDsl_Type_declaration8", self)

    @property
    def myDsl_Class_declaration14(self):
        return self.__myDsl_Class_declaration14

    @myDsl_Class_declaration14.setter
    def myDsl_Class_declaration14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Class_declaration__myDsl_Class_declaration14", None)
        self.__myDsl_Class_declaration14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Field_declaration15"):
                    opp_val = getattr(item, "myDsl_Field_declaration15", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Field_declaration15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Field_declaration15"):
                    opp_val = getattr(item, "myDsl_Field_declaration15", None)
                    
                    setattr(item, "myDsl_Field_declaration15", self)
                    

class myDsl_Type_declaration:

    def __init__(self, comment: str, myDsl_Type_declaration: "myDsl_Compilation_unit" = None, myDsl_Type_declaration8: "myDsl_Class_declaration" = None, myDsl_Type_declaration10: "myDsl_Interface_declaration" = None):
        self.comment = comment
        self.myDsl_Type_declaration = myDsl_Type_declaration
        self.myDsl_Type_declaration8 = myDsl_Type_declaration8
        self.myDsl_Type_declaration10 = myDsl_Type_declaration10
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def myDsl_Type_declaration(self):
        return self.__myDsl_Type_declaration

    @myDsl_Type_declaration.setter
    def myDsl_Type_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type_declaration__myDsl_Type_declaration", None)
        self.__myDsl_Type_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Compilation_unit6"):
                opp_val = getattr(old_value, "myDsl_Compilation_unit6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Compilation_unit6"):
                opp_val = getattr(value, "myDsl_Compilation_unit6", None)
                if opp_val is None:
                    setattr(value, "myDsl_Compilation_unit6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Type_declaration8(self):
        return self.__myDsl_Type_declaration8

    @myDsl_Type_declaration8.setter
    def myDsl_Type_declaration8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type_declaration__myDsl_Type_declaration8", None)
        self.__myDsl_Type_declaration8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Class_declaration"):
                opp_val = getattr(old_value, "myDsl_Class_declaration", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Class_declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Class_declaration"):
                opp_val = getattr(value, "myDsl_Class_declaration", None)
                setattr(value, "myDsl_Class_declaration", self)

    @property
    def myDsl_Type_declaration10(self):
        return self.__myDsl_Type_declaration10

    @myDsl_Type_declaration10.setter
    def myDsl_Type_declaration10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type_declaration__myDsl_Type_declaration10", None)
        self.__myDsl_Type_declaration10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Interface_declaration"):
                opp_val = getattr(old_value, "myDsl_Interface_declaration", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Interface_declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Interface_declaration"):
                opp_val = getattr(value, "myDsl_Interface_declaration", None)
                setattr(value, "myDsl_Interface_declaration", self)
