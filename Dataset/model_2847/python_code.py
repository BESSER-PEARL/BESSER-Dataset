from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class aDSL_This(Expression):

    pass
class aDSL_New(Expression):

    pass
class aDSL_Init(Expression):

    pass
class aDSL_Minus(Expression):

    pass
class aDSL_Plus(Expression):

    pass
class aDSL_Reference(Expression):

    def __init__(self, isarray: bool, aDSL_Reference: "aDSL_VarDef" = None, aDSL_Reference172: set["aDSL_Expression"] = None):
        self.isarray = isarray
        self.aDSL_Reference = aDSL_Reference
        self.aDSL_Reference172 = aDSL_Reference172 if aDSL_Reference172 is not None else set()
        
    @property
    def isarray(self) -> bool:
        return self.__isarray

    @isarray.setter
    def isarray(self, isarray: bool):
        self.__isarray = isarray

    @property
    def aDSL_Reference172(self):
        return self.__aDSL_Reference172

    @aDSL_Reference172.setter
    def aDSL_Reference172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Reference__aDSL_Reference172", None)
        self.__aDSL_Reference172 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDSL_Expression173"):
                    opp_val = getattr(item, "aDSL_Expression173", None)
                    
                    if opp_val == self:
                        setattr(item, "aDSL_Expression173", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDSL_Expression173"):
                    opp_val = getattr(item, "aDSL_Expression173", None)
                    
                    setattr(item, "aDSL_Expression173", self)
                    

    @property
    def aDSL_Reference(self):
        return self.__aDSL_Reference

    @aDSL_Reference.setter
    def aDSL_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Reference__aDSL_Reference", None)
        self.__aDSL_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_VarDef170"):
                opp_val = getattr(old_value, "aDSL_VarDef170", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_VarDef170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_VarDef170"):
                opp_val = getattr(value, "aDSL_VarDef170", None)
                setattr(value, "aDSL_VarDef170", self)

class aDSL_And(Expression):

    pass
class aDSL_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class aDSL_DeRef(Expression):

    pass
class aDSL_Or(Expression):

    pass
class aDSL_Null(Expression):

    pass
class aDSL_IntConstant(Expression):

    pass
class aDSL_MemberSelection(Expression):

    def __init__(self, ispar: bool, methodinvocation: bool, aDSL_MemberSelection: "aDSL_Expression" = None, aDSL_MemberSelection121: "aDSL_Member" = None, aDSL_MemberSelection124: "aDSL_XClass" = None, aDSL_MemberSelection127: set["aDSL_Expression"] = None):
        self.ispar = ispar
        self.methodinvocation = methodinvocation
        self.aDSL_MemberSelection = aDSL_MemberSelection
        self.aDSL_MemberSelection121 = aDSL_MemberSelection121
        self.aDSL_MemberSelection124 = aDSL_MemberSelection124
        self.aDSL_MemberSelection127 = aDSL_MemberSelection127 if aDSL_MemberSelection127 is not None else set()
        
    @property
    def methodinvocation(self) -> bool:
        return self.__methodinvocation

    @methodinvocation.setter
    def methodinvocation(self, methodinvocation: bool):
        self.__methodinvocation = methodinvocation

    @property
    def ispar(self) -> bool:
        return self.__ispar

    @ispar.setter
    def ispar(self, ispar: bool):
        self.__ispar = ispar

    @property
    def aDSL_MemberSelection127(self):
        return self.__aDSL_MemberSelection127

    @aDSL_MemberSelection127.setter
    def aDSL_MemberSelection127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_MemberSelection__aDSL_MemberSelection127", None)
        self.__aDSL_MemberSelection127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDSL_Expression128"):
                    opp_val = getattr(item, "aDSL_Expression128", None)
                    
                    if opp_val == self:
                        setattr(item, "aDSL_Expression128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDSL_Expression128"):
                    opp_val = getattr(item, "aDSL_Expression128", None)
                    
                    setattr(item, "aDSL_Expression128", self)
                    

    @property
    def aDSL_MemberSelection121(self):
        return self.__aDSL_MemberSelection121

    @aDSL_MemberSelection121.setter
    def aDSL_MemberSelection121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_MemberSelection__aDSL_MemberSelection121", None)
        self.__aDSL_MemberSelection121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Member122"):
                opp_val = getattr(old_value, "aDSL_Member122", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Member122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Member122"):
                opp_val = getattr(value, "aDSL_Member122", None)
                setattr(value, "aDSL_Member122", self)

    @property
    def aDSL_MemberSelection124(self):
        return self.__aDSL_MemberSelection124

    @aDSL_MemberSelection124.setter
    def aDSL_MemberSelection124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_MemberSelection__aDSL_MemberSelection124", None)
        self.__aDSL_MemberSelection124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_XClass125"):
                opp_val = getattr(old_value, "aDSL_XClass125", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_XClass125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_XClass125"):
                opp_val = getattr(value, "aDSL_XClass125", None)
                setattr(value, "aDSL_XClass125", self)

    @property
    def aDSL_MemberSelection(self):
        return self.__aDSL_MemberSelection

    @aDSL_MemberSelection.setter
    def aDSL_MemberSelection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_MemberSelection__aDSL_MemberSelection", None)
        self.__aDSL_MemberSelection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Expression119"):
                opp_val = getattr(old_value, "aDSL_Expression119", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Expression119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Expression119"):
                opp_val = getattr(value, "aDSL_Expression119", None)
                setattr(value, "aDSL_Expression119", self)

class aDSL_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class aDSL_Here(Expression):

    pass
class aDSL_MulOrDiv(Expression):

    def __init__(self, op: str, aDSL_MulOrDiv162: "aDSL_Expression" = None, aDSL_MulOrDiv: "aDSL_Expression" = None):
        self.op = op
        self.aDSL_MulOrDiv162 = aDSL_MulOrDiv162
        self.aDSL_MulOrDiv = aDSL_MulOrDiv
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def aDSL_MulOrDiv(self):
        return self.__aDSL_MulOrDiv

    @aDSL_MulOrDiv.setter
    def aDSL_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_MulOrDiv__aDSL_MulOrDiv", None)
        self.__aDSL_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Expression160"):
                opp_val = getattr(old_value, "aDSL_Expression160", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Expression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Expression160"):
                opp_val = getattr(value, "aDSL_Expression160", None)
                setattr(value, "aDSL_Expression160", self)

    @property
    def aDSL_MulOrDiv162(self):
        return self.__aDSL_MulOrDiv162

    @aDSL_MulOrDiv162.setter
    def aDSL_MulOrDiv162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_MulOrDiv__aDSL_MulOrDiv162", None)
        self.__aDSL_MulOrDiv162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Expression163"):
                opp_val = getattr(old_value, "aDSL_Expression163", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Expression163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Expression163"):
                opp_val = getattr(value, "aDSL_Expression163", None)
                setattr(value, "aDSL_Expression163", self)

class aDSL_Not(Expression):

    pass
class aDSL_Equality(Expression):

    def __init__(self, op: str, aDSL_Equality: "aDSL_Expression" = None, aDSL_Equality142: "aDSL_Expression" = None):
        self.op = op
        self.aDSL_Equality = aDSL_Equality
        self.aDSL_Equality142 = aDSL_Equality142
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def aDSL_Equality(self):
        return self.__aDSL_Equality

    @aDSL_Equality.setter
    def aDSL_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Equality__aDSL_Equality", None)
        self.__aDSL_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Expression140"):
                opp_val = getattr(old_value, "aDSL_Expression140", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Expression140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Expression140"):
                opp_val = getattr(value, "aDSL_Expression140", None)
                setattr(value, "aDSL_Expression140", self)

    @property
    def aDSL_Equality142(self):
        return self.__aDSL_Equality142

    @aDSL_Equality142.setter
    def aDSL_Equality142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Equality__aDSL_Equality142", None)
        self.__aDSL_Equality142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Expression143"):
                opp_val = getattr(old_value, "aDSL_Expression143", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Expression143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Expression143"):
                opp_val = getattr(value, "aDSL_Expression143", None)
                setattr(value, "aDSL_Expression143", self)

class aDSL_Comparison(Expression):

    def __init__(self, op: str, aDSL_Comparison: "aDSL_Expression" = None, aDSL_Comparison147: "aDSL_Expression" = None):
        self.op = op
        self.aDSL_Comparison = aDSL_Comparison
        self.aDSL_Comparison147 = aDSL_Comparison147
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def aDSL_Comparison(self):
        return self.__aDSL_Comparison

    @aDSL_Comparison.setter
    def aDSL_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Comparison__aDSL_Comparison", None)
        self.__aDSL_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Expression145"):
                opp_val = getattr(old_value, "aDSL_Expression145", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Expression145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Expression145"):
                opp_val = getattr(value, "aDSL_Expression145", None)
                setattr(value, "aDSL_Expression145", self)

    @property
    def aDSL_Comparison147(self):
        return self.__aDSL_Comparison147

    @aDSL_Comparison147.setter
    def aDSL_Comparison147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Comparison__aDSL_Comparison147", None)
        self.__aDSL_Comparison147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Expression148"):
                opp_val = getattr(old_value, "aDSL_Expression148", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Expression148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Expression148"):
                opp_val = getattr(value, "aDSL_Expression148", None)
                setattr(value, "aDSL_Expression148", self)

class aDSL_Assignment(Expression):

    pass
class aDSL_IntegerNegative:

    def __init__(self, isneg: bool, value: int, aDSL_IntegerNegative: "aDSL_IntConstant" = None):
        self.isneg = isneg
        self.value = value
        self.aDSL_IntegerNegative = aDSL_IntegerNegative
        
    @property
    def isneg(self) -> bool:
        return self.__isneg

    @isneg.setter
    def isneg(self, isneg: bool):
        self.__isneg = isneg

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def aDSL_IntegerNegative(self):
        return self.__aDSL_IntegerNegative

    @aDSL_IntegerNegative.setter
    def aDSL_IntegerNegative(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_IntegerNegative__aDSL_IntegerNegative", None)
        self.__aDSL_IntegerNegative = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_IntConstant"):
                opp_val = getattr(old_value, "aDSL_IntConstant", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_IntConstant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_IntConstant"):
                opp_val = getattr(value, "aDSL_IntConstant", None)
                setattr(value, "aDSL_IntConstant", self)

class aDSL_VarDef:

    pass
class aDSL_Block:

    def __init__(self, ispar: bool, aDSL_Block: set["aDSL_Statement"] = None, aDSL_Block55: "aDSL_AsyncStat" = None, aDSL_Block57: "aDSL_FinishStat" = None, aDSL_Block62: "aDSL_AtStat" = None, aDSL_Block77: "aDSL_For2Statement" = None, aDSL_Block102: "aDSL_ForStat" = None, aDSL_Block109: "aDSL_IfStat" = None, aDSL_Block112: "aDSL_IfStat" = None):
        self.ispar = ispar
        self.aDSL_Block = aDSL_Block if aDSL_Block is not None else set()
        self.aDSL_Block55 = aDSL_Block55
        self.aDSL_Block57 = aDSL_Block57
        self.aDSL_Block62 = aDSL_Block62
        self.aDSL_Block77 = aDSL_Block77
        self.aDSL_Block102 = aDSL_Block102
        self.aDSL_Block109 = aDSL_Block109
        self.aDSL_Block112 = aDSL_Block112
        
    @property
    def ispar(self) -> bool:
        return self.__ispar

    @ispar.setter
    def ispar(self, ispar: bool):
        self.__ispar = ispar

    @property
    def aDSL_Block(self):
        return self.__aDSL_Block

    @aDSL_Block.setter
    def aDSL_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Block__aDSL_Block", None)
        self.__aDSL_Block = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDSL_Statement47"):
                    opp_val = getattr(item, "aDSL_Statement47", None)
                    
                    if opp_val == self:
                        setattr(item, "aDSL_Statement47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDSL_Statement47"):
                    opp_val = getattr(item, "aDSL_Statement47", None)
                    
                    setattr(item, "aDSL_Statement47", self)
                    

    @property
    def aDSL_Block57(self):
        return self.__aDSL_Block57

    @aDSL_Block57.setter
    def aDSL_Block57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Block__aDSL_Block57", None)
        self.__aDSL_Block57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_FinishStat"):
                opp_val = getattr(old_value, "aDSL_FinishStat", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_FinishStat", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_FinishStat"):
                opp_val = getattr(value, "aDSL_FinishStat", None)
                setattr(value, "aDSL_FinishStat", self)

    @property
    def aDSL_Block62(self):
        return self.__aDSL_Block62

    @aDSL_Block62.setter
    def aDSL_Block62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Block__aDSL_Block62", None)
        self.__aDSL_Block62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_AtStat61"):
                opp_val = getattr(old_value, "aDSL_AtStat61", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_AtStat61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_AtStat61"):
                opp_val = getattr(value, "aDSL_AtStat61", None)
                setattr(value, "aDSL_AtStat61", self)

    @property
    def aDSL_Block55(self):
        return self.__aDSL_Block55

    @aDSL_Block55.setter
    def aDSL_Block55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Block__aDSL_Block55", None)
        self.__aDSL_Block55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_AsyncStat"):
                opp_val = getattr(old_value, "aDSL_AsyncStat", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_AsyncStat", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_AsyncStat"):
                opp_val = getattr(value, "aDSL_AsyncStat", None)
                setattr(value, "aDSL_AsyncStat", self)

    @property
    def aDSL_Block109(self):
        return self.__aDSL_Block109

    @aDSL_Block109.setter
    def aDSL_Block109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Block__aDSL_Block109", None)
        self.__aDSL_Block109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_IfStat108"):
                opp_val = getattr(old_value, "aDSL_IfStat108", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_IfStat108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_IfStat108"):
                opp_val = getattr(value, "aDSL_IfStat108", None)
                setattr(value, "aDSL_IfStat108", self)

    @property
    def aDSL_Block77(self):
        return self.__aDSL_Block77

    @aDSL_Block77.setter
    def aDSL_Block77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Block__aDSL_Block77", None)
        self.__aDSL_Block77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_For2Statement76"):
                opp_val = getattr(old_value, "aDSL_For2Statement76", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_For2Statement76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_For2Statement76"):
                opp_val = getattr(value, "aDSL_For2Statement76", None)
                setattr(value, "aDSL_For2Statement76", self)

    @property
    def aDSL_Block102(self):
        return self.__aDSL_Block102

    @aDSL_Block102.setter
    def aDSL_Block102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Block__aDSL_Block102", None)
        self.__aDSL_Block102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_ForStat101"):
                opp_val = getattr(old_value, "aDSL_ForStat101", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_ForStat101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_ForStat101"):
                opp_val = getattr(value, "aDSL_ForStat101", None)
                setattr(value, "aDSL_ForStat101", self)

    @property
    def aDSL_Block112(self):
        return self.__aDSL_Block112

    @aDSL_Block112.setter
    def aDSL_Block112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Block__aDSL_Block112", None)
        self.__aDSL_Block112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_IfStat111"):
                opp_val = getattr(old_value, "aDSL_IfStat111", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_IfStat111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_IfStat111"):
                opp_val = getattr(value, "aDSL_IfStat111", None)
                setattr(value, "aDSL_IfStat111", self)

class aDSL_Statement:

    pass
class SharedDef:

    pass
class aDSL_SharedVarDef(SharedDef):

    pass
class aDSL_SharedArrayDef(SharedDef):

    pass
class aDSL_Member:

    pass
class Statement:

    pass
class aDSL_ReturnStat(Statement):

    pass
class aDSL_AsyncStat(Statement):

    pass
class aDSL_Expression(Statement):

    pass
class aDSL_WhileStat(Statement):

    pass
class aDSL_AtomicStatement(Statement):

    pass
class aDSL_TryCatchStat(Statement):

    def __init__(self, name: str, aDSL_TryCatchStat85: "aDSL_Body" = None, aDSL_TryCatchStat: "aDSL_Body" = None):
        self.name = name
        self.aDSL_TryCatchStat85 = aDSL_TryCatchStat85
        self.aDSL_TryCatchStat = aDSL_TryCatchStat
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aDSL_TryCatchStat85(self):
        return self.__aDSL_TryCatchStat85

    @aDSL_TryCatchStat85.setter
    def aDSL_TryCatchStat85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_TryCatchStat__aDSL_TryCatchStat85", None)
        self.__aDSL_TryCatchStat85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Body86"):
                opp_val = getattr(old_value, "aDSL_Body86", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Body86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Body86"):
                opp_val = getattr(value, "aDSL_Body86", None)
                setattr(value, "aDSL_Body86", self)

    @property
    def aDSL_TryCatchStat(self):
        return self.__aDSL_TryCatchStat

    @aDSL_TryCatchStat.setter
    def aDSL_TryCatchStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_TryCatchStat__aDSL_TryCatchStat", None)
        self.__aDSL_TryCatchStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Body83"):
                opp_val = getattr(old_value, "aDSL_Body83", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Body83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Body83"):
                opp_val = getattr(value, "aDSL_Body83", None)
                setattr(value, "aDSL_Body83", self)

class aDSL_IfStat(Statement):

    def __init__(self, iselse: bool, aDSL_IfStat: "aDSL_Expression" = None, aDSL_IfStat108: "aDSL_Block" = None, aDSL_IfStat111: "aDSL_Block" = None):
        self.iselse = iselse
        self.aDSL_IfStat = aDSL_IfStat
        self.aDSL_IfStat108 = aDSL_IfStat108
        self.aDSL_IfStat111 = aDSL_IfStat111
        
    @property
    def iselse(self) -> bool:
        return self.__iselse

    @iselse.setter
    def iselse(self, iselse: bool):
        self.__iselse = iselse

    @property
    def aDSL_IfStat(self):
        return self.__aDSL_IfStat

    @aDSL_IfStat.setter
    def aDSL_IfStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_IfStat__aDSL_IfStat", None)
        self.__aDSL_IfStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Expression106"):
                opp_val = getattr(old_value, "aDSL_Expression106", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Expression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Expression106"):
                opp_val = getattr(value, "aDSL_Expression106", None)
                setattr(value, "aDSL_Expression106", self)

    @property
    def aDSL_IfStat108(self):
        return self.__aDSL_IfStat108

    @aDSL_IfStat108.setter
    def aDSL_IfStat108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_IfStat__aDSL_IfStat108", None)
        self.__aDSL_IfStat108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Block109"):
                opp_val = getattr(old_value, "aDSL_Block109", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Block109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Block109"):
                opp_val = getattr(value, "aDSL_Block109", None)
                setattr(value, "aDSL_Block109", self)

    @property
    def aDSL_IfStat111(self):
        return self.__aDSL_IfStat111

    @aDSL_IfStat111.setter
    def aDSL_IfStat111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_IfStat__aDSL_IfStat111", None)
        self.__aDSL_IfStat111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Block112"):
                opp_val = getattr(old_value, "aDSL_Block112", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Block112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Block112"):
                opp_val = getattr(value, "aDSL_Block112", None)
                setattr(value, "aDSL_Block112", self)

class aDSL_ForStat(Statement):

    pass
class aDSL_For2Statement(Statement):

    pass
class aDSL_AtStat(Statement):

    pass
class aDSL_FinishStat(Statement):

    pass
class aDSL_WhenStatement(Statement):

    pass
class aDSL_Body:

    pass
class Member:

    pass
class aDSL_PrintInst(Member, Statement):

    pass
class aDSL_Method(Member):

    def __init__(self, isconst: bool, name: str, istyped: bool, aDSL_Method: set["aDSL_Parameter"] = None, aDSL_Method14: "aDSL_VariableType" = None, aDSL_Method17: "aDSL_Body" = None):
        self.isconst = isconst
        self.name = name
        self.istyped = istyped
        self.aDSL_Method = aDSL_Method if aDSL_Method is not None else set()
        self.aDSL_Method14 = aDSL_Method14
        self.aDSL_Method17 = aDSL_Method17
        
    @property
    def istyped(self) -> bool:
        return self.__istyped

    @istyped.setter
    def istyped(self, istyped: bool):
        self.__istyped = istyped

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isconst(self) -> bool:
        return self.__isconst

    @isconst.setter
    def isconst(self, isconst: bool):
        self.__isconst = isconst

    @property
    def aDSL_Method(self):
        return self.__aDSL_Method

    @aDSL_Method.setter
    def aDSL_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Method__aDSL_Method", None)
        self.__aDSL_Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDSL_Parameter"):
                    opp_val = getattr(item, "aDSL_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "aDSL_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDSL_Parameter"):
                    opp_val = getattr(item, "aDSL_Parameter", None)
                    
                    setattr(item, "aDSL_Parameter", self)
                    

    @property
    def aDSL_Method17(self):
        return self.__aDSL_Method17

    @aDSL_Method17.setter
    def aDSL_Method17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Method__aDSL_Method17", None)
        self.__aDSL_Method17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Body18"):
                opp_val = getattr(old_value, "aDSL_Body18", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Body18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Body18"):
                opp_val = getattr(value, "aDSL_Body18", None)
                setattr(value, "aDSL_Body18", self)

    @property
    def aDSL_Method14(self):
        return self.__aDSL_Method14

    @aDSL_Method14.setter
    def aDSL_Method14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Method__aDSL_Method14", None)
        self.__aDSL_Method14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_VariableType15"):
                opp_val = getattr(old_value, "aDSL_VariableType15", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_VariableType15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_VariableType15"):
                opp_val = getattr(value, "aDSL_VariableType15", None)
                setattr(value, "aDSL_VariableType15", self)

class aDSL_Operator(Member):

    def __init__(self, opName: str, aDSL_Operator: set["aDSL_Parameter"] = None, aDSL_Operator22: "aDSL_Expression" = None):
        self.opName = opName
        self.aDSL_Operator = aDSL_Operator if aDSL_Operator is not None else set()
        self.aDSL_Operator22 = aDSL_Operator22
        
    @property
    def opName(self) -> str:
        return self.__opName

    @opName.setter
    def opName(self, opName: str):
        self.__opName = opName

    @property
    def aDSL_Operator(self):
        return self.__aDSL_Operator

    @aDSL_Operator.setter
    def aDSL_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Operator__aDSL_Operator", None)
        self.__aDSL_Operator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDSL_Parameter20"):
                    opp_val = getattr(item, "aDSL_Parameter20", None)
                    
                    if opp_val == self:
                        setattr(item, "aDSL_Parameter20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDSL_Parameter20"):
                    opp_val = getattr(item, "aDSL_Parameter20", None)
                    
                    setattr(item, "aDSL_Parameter20", self)
                    

    @property
    def aDSL_Operator22(self):
        return self.__aDSL_Operator22

    @aDSL_Operator22.setter
    def aDSL_Operator22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Operator__aDSL_Operator22", None)
        self.__aDSL_Operator22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Expression23"):
                opp_val = getattr(old_value, "aDSL_Expression23", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Expression23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Expression23"):
                opp_val = getattr(value, "aDSL_Expression23", None)
                setattr(value, "aDSL_Expression23", self)

class aDSL_MainMethod(Member):

    pass
class VarDef:

    pass
class aDSL_VariableDef(Member, VarDef, Statement):

    def __init__(self, isstatic: bool, vartype: str, name: str, istyped: bool, isinit: bool, aDSL_VariableDef: "aDSL_VariableType" = None, aDSL_VariableDef38: "aDSL_SharedArrayDef" = None, aDSL_VariableDef35: "aDSL_Expression" = None, aDSL_VariableDef93: "aDSL_ForStat" = None):
        self.isstatic = isstatic
        self.vartype = vartype
        self.name = name
        self.istyped = istyped
        self.isinit = isinit
        self.aDSL_VariableDef = aDSL_VariableDef
        self.aDSL_VariableDef38 = aDSL_VariableDef38
        self.aDSL_VariableDef35 = aDSL_VariableDef35
        self.aDSL_VariableDef93 = aDSL_VariableDef93
        
    @property
    def isstatic(self) -> bool:
        return self.__isstatic

    @isstatic.setter
    def isstatic(self, isstatic: bool):
        self.__isstatic = isstatic

    @property
    def vartype(self) -> str:
        return self.__vartype

    @vartype.setter
    def vartype(self, vartype: str):
        self.__vartype = vartype

    @property
    def istyped(self) -> bool:
        return self.__istyped

    @istyped.setter
    def istyped(self, istyped: bool):
        self.__istyped = istyped

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isinit(self) -> bool:
        return self.__isinit

    @isinit.setter
    def isinit(self, isinit: bool):
        self.__isinit = isinit

    @property
    def aDSL_VariableDef38(self):
        return self.__aDSL_VariableDef38

    @aDSL_VariableDef38.setter
    def aDSL_VariableDef38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableDef__aDSL_VariableDef38", None)
        self.__aDSL_VariableDef38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_SharedArrayDef"):
                opp_val = getattr(old_value, "aDSL_SharedArrayDef", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_SharedArrayDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_SharedArrayDef"):
                opp_val = getattr(value, "aDSL_SharedArrayDef", None)
                setattr(value, "aDSL_SharedArrayDef", self)

    @property
    def aDSL_VariableDef(self):
        return self.__aDSL_VariableDef

    @aDSL_VariableDef.setter
    def aDSL_VariableDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableDef__aDSL_VariableDef", None)
        self.__aDSL_VariableDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_VariableType33"):
                opp_val = getattr(old_value, "aDSL_VariableType33", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_VariableType33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_VariableType33"):
                opp_val = getattr(value, "aDSL_VariableType33", None)
                setattr(value, "aDSL_VariableType33", self)

    @property
    def aDSL_VariableDef35(self):
        return self.__aDSL_VariableDef35

    @aDSL_VariableDef35.setter
    def aDSL_VariableDef35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableDef__aDSL_VariableDef35", None)
        self.__aDSL_VariableDef35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Expression36"):
                opp_val = getattr(old_value, "aDSL_Expression36", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Expression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Expression36"):
                opp_val = getattr(value, "aDSL_Expression36", None)
                setattr(value, "aDSL_Expression36", self)

    @property
    def aDSL_VariableDef93(self):
        return self.__aDSL_VariableDef93

    @aDSL_VariableDef93.setter
    def aDSL_VariableDef93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableDef__aDSL_VariableDef93", None)
        self.__aDSL_VariableDef93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_ForStat"):
                opp_val = getattr(old_value, "aDSL_ForStat", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_ForStat", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_ForStat"):
                opp_val = getattr(value, "aDSL_ForStat", None)
                setattr(value, "aDSL_ForStat", self)

class aDSL_Parameter(VarDef):

    def __init__(self, name: str, istyped: bool, aDSL_Parameter: "aDSL_Method" = None, aDSL_Parameter20: "aDSL_Operator" = None, aDSL_Parameter25: "aDSL_FuncVarDef" = None, aDSL_Parameter42: "aDSL_VariableType" = None, aDSL_Parameter71: "aDSL_For2Statement" = None):
        self.name = name
        self.istyped = istyped
        self.aDSL_Parameter = aDSL_Parameter
        self.aDSL_Parameter20 = aDSL_Parameter20
        self.aDSL_Parameter25 = aDSL_Parameter25
        self.aDSL_Parameter42 = aDSL_Parameter42
        self.aDSL_Parameter71 = aDSL_Parameter71
        
    @property
    def istyped(self) -> bool:
        return self.__istyped

    @istyped.setter
    def istyped(self, istyped: bool):
        self.__istyped = istyped

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aDSL_Parameter25(self):
        return self.__aDSL_Parameter25

    @aDSL_Parameter25.setter
    def aDSL_Parameter25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Parameter__aDSL_Parameter25", None)
        self.__aDSL_Parameter25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_FuncVarDef"):
                opp_val = getattr(old_value, "aDSL_FuncVarDef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_FuncVarDef"):
                opp_val = getattr(value, "aDSL_FuncVarDef", None)
                if opp_val is None:
                    setattr(value, "aDSL_FuncVarDef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aDSL_Parameter42(self):
        return self.__aDSL_Parameter42

    @aDSL_Parameter42.setter
    def aDSL_Parameter42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Parameter__aDSL_Parameter42", None)
        self.__aDSL_Parameter42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_VariableType43"):
                opp_val = getattr(old_value, "aDSL_VariableType43", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_VariableType43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_VariableType43"):
                opp_val = getattr(value, "aDSL_VariableType43", None)
                setattr(value, "aDSL_VariableType43", self)

    @property
    def aDSL_Parameter71(self):
        return self.__aDSL_Parameter71

    @aDSL_Parameter71.setter
    def aDSL_Parameter71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Parameter__aDSL_Parameter71", None)
        self.__aDSL_Parameter71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_For2Statement"):
                opp_val = getattr(old_value, "aDSL_For2Statement", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_For2Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_For2Statement"):
                opp_val = getattr(value, "aDSL_For2Statement", None)
                setattr(value, "aDSL_For2Statement", self)

    @property
    def aDSL_Parameter(self):
        return self.__aDSL_Parameter

    @aDSL_Parameter.setter
    def aDSL_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Parameter__aDSL_Parameter", None)
        self.__aDSL_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Method"):
                opp_val = getattr(old_value, "aDSL_Method", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Method"):
                opp_val = getattr(value, "aDSL_Method", None)
                if opp_val is None:
                    setattr(value, "aDSL_Method", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aDSL_Parameter20(self):
        return self.__aDSL_Parameter20

    @aDSL_Parameter20.setter
    def aDSL_Parameter20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Parameter__aDSL_Parameter20", None)
        self.__aDSL_Parameter20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Operator"):
                opp_val = getattr(old_value, "aDSL_Operator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Operator"):
                opp_val = getattr(value, "aDSL_Operator", None)
                if opp_val is None:
                    setattr(value, "aDSL_Operator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aDSL_SharedDef(Member, VarDef, Statement):

    def __init__(self, replicas: bool, name: str, aDSL_SharedDef: "aDSL_VariableType" = None, aDSL_SharedDef81: "aDSL_VarDef" = None):
        self.replicas = replicas
        self.name = name
        self.aDSL_SharedDef = aDSL_SharedDef
        self.aDSL_SharedDef81 = aDSL_SharedDef81
        
    @property
    def replicas(self) -> bool:
        return self.__replicas

    @replicas.setter
    def replicas(self, replicas: bool):
        self.__replicas = replicas

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aDSL_SharedDef81(self):
        return self.__aDSL_SharedDef81

    @aDSL_SharedDef81.setter
    def aDSL_SharedDef81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_SharedDef__aDSL_SharedDef81", None)
        self.__aDSL_SharedDef81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_VarDef"):
                opp_val = getattr(old_value, "aDSL_VarDef", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_VarDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_VarDef"):
                opp_val = getattr(value, "aDSL_VarDef", None)
                setattr(value, "aDSL_VarDef", self)

    @property
    def aDSL_SharedDef(self):
        return self.__aDSL_SharedDef

    @aDSL_SharedDef.setter
    def aDSL_SharedDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_SharedDef__aDSL_SharedDef", None)
        self.__aDSL_SharedDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_VariableType79"):
                opp_val = getattr(old_value, "aDSL_VariableType79", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_VariableType79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_VariableType79"):
                opp_val = getattr(value, "aDSL_VariableType79", None)
                setattr(value, "aDSL_VariableType79", self)

class aDSL_FuncVarDef(Member, VarDef, Statement):

    def __init__(self, name: str, aDSL_FuncVarDef: set["aDSL_Parameter"] = None, aDSL_FuncVarDef27: "aDSL_VariableType" = None, aDSL_FuncVarDef30: "aDSL_Body" = None):
        self.name = name
        self.aDSL_FuncVarDef = aDSL_FuncVarDef if aDSL_FuncVarDef is not None else set()
        self.aDSL_FuncVarDef27 = aDSL_FuncVarDef27
        self.aDSL_FuncVarDef30 = aDSL_FuncVarDef30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aDSL_FuncVarDef27(self):
        return self.__aDSL_FuncVarDef27

    @aDSL_FuncVarDef27.setter
    def aDSL_FuncVarDef27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_FuncVarDef__aDSL_FuncVarDef27", None)
        self.__aDSL_FuncVarDef27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_VariableType28"):
                opp_val = getattr(old_value, "aDSL_VariableType28", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_VariableType28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_VariableType28"):
                opp_val = getattr(value, "aDSL_VariableType28", None)
                setattr(value, "aDSL_VariableType28", self)

    @property
    def aDSL_FuncVarDef(self):
        return self.__aDSL_FuncVarDef

    @aDSL_FuncVarDef.setter
    def aDSL_FuncVarDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_FuncVarDef__aDSL_FuncVarDef", None)
        self.__aDSL_FuncVarDef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDSL_Parameter25"):
                    opp_val = getattr(item, "aDSL_Parameter25", None)
                    
                    if opp_val == self:
                        setattr(item, "aDSL_Parameter25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDSL_Parameter25"):
                    opp_val = getattr(item, "aDSL_Parameter25", None)
                    
                    setattr(item, "aDSL_Parameter25", self)
                    

    @property
    def aDSL_FuncVarDef30(self):
        return self.__aDSL_FuncVarDef30

    @aDSL_FuncVarDef30.setter
    def aDSL_FuncVarDef30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_FuncVarDef__aDSL_FuncVarDef30", None)
        self.__aDSL_FuncVarDef30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Body31"):
                opp_val = getattr(old_value, "aDSL_Body31", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Body31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Body31"):
                opp_val = getattr(value, "aDSL_Body31", None)
                setattr(value, "aDSL_Body31", self)

class aDSL_VariableType(VarDef):

    def __init__(self, isarray: bool, aDSL_VariableType: "aDSL_MainMethod" = None, aDSL_VariableType15: "aDSL_Method" = None, aDSL_VariableType28: "aDSL_FuncVarDef" = None, aDSL_VariableType33: "aDSL_VariableDef" = None, aDSL_VariableType43: "aDSL_Parameter" = None, aDSL_VariableType49: "aDSL_XClass" = None, aDSL_VariableType53: "aDSL_VariableType" = None, aDSL_VariableType51: "aDSL_VariableType" = None, aDSL_VariableType79: "aDSL_SharedDef" = None, aDSL_VariableType175: "aDSL_New" = None, aDSL_VariableType180: "aDSL_Init" = None):
        self.isarray = isarray
        self.aDSL_VariableType = aDSL_VariableType
        self.aDSL_VariableType15 = aDSL_VariableType15
        self.aDSL_VariableType28 = aDSL_VariableType28
        self.aDSL_VariableType33 = aDSL_VariableType33
        self.aDSL_VariableType43 = aDSL_VariableType43
        self.aDSL_VariableType49 = aDSL_VariableType49
        self.aDSL_VariableType53 = aDSL_VariableType53
        self.aDSL_VariableType51 = aDSL_VariableType51
        self.aDSL_VariableType79 = aDSL_VariableType79
        self.aDSL_VariableType175 = aDSL_VariableType175
        self.aDSL_VariableType180 = aDSL_VariableType180
        
    @property
    def isarray(self) -> bool:
        return self.__isarray

    @isarray.setter
    def isarray(self, isarray: bool):
        self.__isarray = isarray

    @property
    def aDSL_VariableType180(self):
        return self.__aDSL_VariableType180

    @aDSL_VariableType180.setter
    def aDSL_VariableType180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableType__aDSL_VariableType180", None)
        self.__aDSL_VariableType180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Init"):
                opp_val = getattr(old_value, "aDSL_Init", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Init", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Init"):
                opp_val = getattr(value, "aDSL_Init", None)
                setattr(value, "aDSL_Init", self)

    @property
    def aDSL_VariableType43(self):
        return self.__aDSL_VariableType43

    @aDSL_VariableType43.setter
    def aDSL_VariableType43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableType__aDSL_VariableType43", None)
        self.__aDSL_VariableType43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Parameter42"):
                opp_val = getattr(old_value, "aDSL_Parameter42", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Parameter42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Parameter42"):
                opp_val = getattr(value, "aDSL_Parameter42", None)
                setattr(value, "aDSL_Parameter42", self)

    @property
    def aDSL_VariableType53(self):
        return self.__aDSL_VariableType53

    @aDSL_VariableType53.setter
    def aDSL_VariableType53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableType__aDSL_VariableType53", None)
        self.__aDSL_VariableType53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_VariableType51"):
                opp_val = getattr(old_value, "aDSL_VariableType51", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_VariableType51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_VariableType51"):
                opp_val = getattr(value, "aDSL_VariableType51", None)
                setattr(value, "aDSL_VariableType51", self)

    @property
    def aDSL_VariableType175(self):
        return self.__aDSL_VariableType175

    @aDSL_VariableType175.setter
    def aDSL_VariableType175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableType__aDSL_VariableType175", None)
        self.__aDSL_VariableType175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_New"):
                opp_val = getattr(old_value, "aDSL_New", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_New", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_New"):
                opp_val = getattr(value, "aDSL_New", None)
                setattr(value, "aDSL_New", self)

    @property
    def aDSL_VariableType51(self):
        return self.__aDSL_VariableType51

    @aDSL_VariableType51.setter
    def aDSL_VariableType51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableType__aDSL_VariableType51", None)
        self.__aDSL_VariableType51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_VariableType53"):
                opp_val = getattr(old_value, "aDSL_VariableType53", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_VariableType53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_VariableType53"):
                opp_val = getattr(value, "aDSL_VariableType53", None)
                setattr(value, "aDSL_VariableType53", self)

    @property
    def aDSL_VariableType28(self):
        return self.__aDSL_VariableType28

    @aDSL_VariableType28.setter
    def aDSL_VariableType28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableType__aDSL_VariableType28", None)
        self.__aDSL_VariableType28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_FuncVarDef27"):
                opp_val = getattr(old_value, "aDSL_FuncVarDef27", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_FuncVarDef27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_FuncVarDef27"):
                opp_val = getattr(value, "aDSL_FuncVarDef27", None)
                setattr(value, "aDSL_FuncVarDef27", self)

    @property
    def aDSL_VariableType15(self):
        return self.__aDSL_VariableType15

    @aDSL_VariableType15.setter
    def aDSL_VariableType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableType__aDSL_VariableType15", None)
        self.__aDSL_VariableType15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Method14"):
                opp_val = getattr(old_value, "aDSL_Method14", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_Method14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Method14"):
                opp_val = getattr(value, "aDSL_Method14", None)
                setattr(value, "aDSL_Method14", self)

    @property
    def aDSL_VariableType(self):
        return self.__aDSL_VariableType

    @aDSL_VariableType.setter
    def aDSL_VariableType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableType__aDSL_VariableType", None)
        self.__aDSL_VariableType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_MainMethod"):
                opp_val = getattr(old_value, "aDSL_MainMethod", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_MainMethod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_MainMethod"):
                opp_val = getattr(value, "aDSL_MainMethod", None)
                setattr(value, "aDSL_MainMethod", self)

    @property
    def aDSL_VariableType79(self):
        return self.__aDSL_VariableType79

    @aDSL_VariableType79.setter
    def aDSL_VariableType79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableType__aDSL_VariableType79", None)
        self.__aDSL_VariableType79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_SharedDef"):
                opp_val = getattr(old_value, "aDSL_SharedDef", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_SharedDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_SharedDef"):
                opp_val = getattr(value, "aDSL_SharedDef", None)
                setattr(value, "aDSL_SharedDef", self)

    @property
    def aDSL_VariableType49(self):
        return self.__aDSL_VariableType49

    @aDSL_VariableType49.setter
    def aDSL_VariableType49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableType__aDSL_VariableType49", None)
        self.__aDSL_VariableType49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_XClass50"):
                opp_val = getattr(old_value, "aDSL_XClass50", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_XClass50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_XClass50"):
                opp_val = getattr(value, "aDSL_XClass50", None)
                setattr(value, "aDSL_XClass50", self)

    @property
    def aDSL_VariableType33(self):
        return self.__aDSL_VariableType33

    @aDSL_VariableType33.setter
    def aDSL_VariableType33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_VariableType__aDSL_VariableType33", None)
        self.__aDSL_VariableType33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_VariableDef"):
                opp_val = getattr(old_value, "aDSL_VariableDef", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_VariableDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_VariableDef"):
                opp_val = getattr(value, "aDSL_VariableDef", None)
                setattr(value, "aDSL_VariableDef", self)

class aDSL_XClass(VarDef):

    def __init__(self, name: str, aDSL_XClass: "aDSL_Program" = None, aDSL_XClass5: "aDSL_XClass" = None, aDSL_XClass7: set["aDSL_Member"] = None, aDSL_XClass3: "aDSL_XClass" = None, aDSL_XClass50: "aDSL_VariableType" = None, aDSL_XClass125: "aDSL_MemberSelection" = None):
        self.name = name
        self.aDSL_XClass = aDSL_XClass
        self.aDSL_XClass5 = aDSL_XClass5
        self.aDSL_XClass7 = aDSL_XClass7 if aDSL_XClass7 is not None else set()
        self.aDSL_XClass3 = aDSL_XClass3
        self.aDSL_XClass50 = aDSL_XClass50
        self.aDSL_XClass125 = aDSL_XClass125
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aDSL_XClass3(self):
        return self.__aDSL_XClass3

    @aDSL_XClass3.setter
    def aDSL_XClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_XClass__aDSL_XClass3", None)
        self.__aDSL_XClass3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_XClass5"):
                opp_val = getattr(old_value, "aDSL_XClass5", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_XClass5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_XClass5"):
                opp_val = getattr(value, "aDSL_XClass5", None)
                setattr(value, "aDSL_XClass5", self)

    @property
    def aDSL_XClass125(self):
        return self.__aDSL_XClass125

    @aDSL_XClass125.setter
    def aDSL_XClass125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_XClass__aDSL_XClass125", None)
        self.__aDSL_XClass125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_MemberSelection124"):
                opp_val = getattr(old_value, "aDSL_MemberSelection124", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_MemberSelection124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_MemberSelection124"):
                opp_val = getattr(value, "aDSL_MemberSelection124", None)
                setattr(value, "aDSL_MemberSelection124", self)

    @property
    def aDSL_XClass50(self):
        return self.__aDSL_XClass50

    @aDSL_XClass50.setter
    def aDSL_XClass50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_XClass__aDSL_XClass50", None)
        self.__aDSL_XClass50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_VariableType49"):
                opp_val = getattr(old_value, "aDSL_VariableType49", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_VariableType49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_VariableType49"):
                opp_val = getattr(value, "aDSL_VariableType49", None)
                setattr(value, "aDSL_VariableType49", self)

    @property
    def aDSL_XClass7(self):
        return self.__aDSL_XClass7

    @aDSL_XClass7.setter
    def aDSL_XClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_XClass__aDSL_XClass7", None)
        self.__aDSL_XClass7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDSL_Member"):
                    opp_val = getattr(item, "aDSL_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "aDSL_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDSL_Member"):
                    opp_val = getattr(item, "aDSL_Member", None)
                    
                    setattr(item, "aDSL_Member", self)
                    

    @property
    def aDSL_XClass(self):
        return self.__aDSL_XClass

    @aDSL_XClass.setter
    def aDSL_XClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_XClass__aDSL_XClass", None)
        self.__aDSL_XClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Program2"):
                opp_val = getattr(old_value, "aDSL_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Program2"):
                opp_val = getattr(value, "aDSL_Program2", None)
                if opp_val is None:
                    setattr(value, "aDSL_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aDSL_XClass5(self):
        return self.__aDSL_XClass5

    @aDSL_XClass5.setter
    def aDSL_XClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_XClass__aDSL_XClass5", None)
        self.__aDSL_XClass5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_XClass3"):
                opp_val = getattr(old_value, "aDSL_XClass3", None)
                if opp_val == self:
                    setattr(old_value, "aDSL_XClass3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_XClass3"):
                opp_val = getattr(value, "aDSL_XClass3", None)
                setattr(value, "aDSL_XClass3", self)

class aDSL_AbstractElements:

    def __init__(self, importedNamespace: str, aDSL_AbstractElements: "aDSL_Program" = None):
        self.importedNamespace = importedNamespace
        self.aDSL_AbstractElements = aDSL_AbstractElements
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def aDSL_AbstractElements(self):
        return self.__aDSL_AbstractElements

    @aDSL_AbstractElements.setter
    def aDSL_AbstractElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_AbstractElements__aDSL_AbstractElements", None)
        self.__aDSL_AbstractElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aDSL_Program"):
                opp_val = getattr(old_value, "aDSL_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aDSL_Program"):
                opp_val = getattr(value, "aDSL_Program", None)
                if opp_val is None:
                    setattr(value, "aDSL_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aDSL_Program:

    def __init__(self, name: str, aDSL_Program: set["aDSL_AbstractElements"] = None, aDSL_Program2: set["aDSL_XClass"] = None):
        self.name = name
        self.aDSL_Program = aDSL_Program if aDSL_Program is not None else set()
        self.aDSL_Program2 = aDSL_Program2 if aDSL_Program2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aDSL_Program(self):
        return self.__aDSL_Program

    @aDSL_Program.setter
    def aDSL_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Program__aDSL_Program", None)
        self.__aDSL_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDSL_AbstractElements"):
                    opp_val = getattr(item, "aDSL_AbstractElements", None)
                    
                    if opp_val == self:
                        setattr(item, "aDSL_AbstractElements", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDSL_AbstractElements"):
                    opp_val = getattr(item, "aDSL_AbstractElements", None)
                    
                    setattr(item, "aDSL_AbstractElements", self)
                    

    @property
    def aDSL_Program2(self):
        return self.__aDSL_Program2

    @aDSL_Program2.setter
    def aDSL_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aDSL_Program__aDSL_Program2", None)
        self.__aDSL_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDSL_XClass"):
                    opp_val = getattr(item, "aDSL_XClass", None)
                    
                    if opp_val == self:
                        setattr(item, "aDSL_XClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDSL_XClass"):
                    opp_val = getattr(item, "aDSL_XClass", None)
                    
                    setattr(item, "aDSL_XClass", self)
                    
