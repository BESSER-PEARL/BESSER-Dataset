from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class VariableExpCS:

    pass
class essentialOCLCST_TypeCS:

    pass
class TypeLiteralExpCS:

    pass
class CollectionLiteralExpCS:

    pass
class TypeCS:

    pass
class essentialOCLCST_SimpleNameCS(TypeLiteralExpCS, CollectionLiteralExpCS, TypeCS, VariableExpCS):

    def __init__(self, value: str, essentialOCLCST_SimpleNameCS: "essentialOCLCST_CollectionTypeCS" = None, essentialOCLCST_SimpleNameCS48: "essentialOCLCST_PathNameCS" = None, essentialOCLCST_SimpleNameCS50: set["essentialOCLCST_CollectionLiteralPartCS"] = None, essentialOCLCST_SimpleNameCS60: "essentialOCLCST_VariableCS" = None):
        self.value = value
        self.essentialOCLCST_SimpleNameCS = essentialOCLCST_SimpleNameCS
        self.essentialOCLCST_SimpleNameCS48 = essentialOCLCST_SimpleNameCS48
        self.essentialOCLCST_SimpleNameCS50 = essentialOCLCST_SimpleNameCS50 if essentialOCLCST_SimpleNameCS50 is not None else set()
        self.essentialOCLCST_SimpleNameCS60 = essentialOCLCST_SimpleNameCS60
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def essentialOCLCST_SimpleNameCS(self):
        return self.__essentialOCLCST_SimpleNameCS

    @essentialOCLCST_SimpleNameCS.setter
    def essentialOCLCST_SimpleNameCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialOCLCST_SimpleNameCS__essentialOCLCST_SimpleNameCS", None)
        self.__essentialOCLCST_SimpleNameCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialOCLCST_CollectionTypeCS"):
                opp_val = getattr(old_value, "essentialOCLCST_CollectionTypeCS", None)
                if opp_val == self:
                    setattr(old_value, "essentialOCLCST_CollectionTypeCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialOCLCST_CollectionTypeCS"):
                opp_val = getattr(value, "essentialOCLCST_CollectionTypeCS", None)
                setattr(value, "essentialOCLCST_CollectionTypeCS", self)

    @property
    def essentialOCLCST_SimpleNameCS50(self):
        return self.__essentialOCLCST_SimpleNameCS50

    @essentialOCLCST_SimpleNameCS50.setter
    def essentialOCLCST_SimpleNameCS50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialOCLCST_SimpleNameCS__essentialOCLCST_SimpleNameCS50", None)
        self.__essentialOCLCST_SimpleNameCS50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialOCLCST_CollectionLiteralPartCS51"):
                    opp_val = getattr(item, "essentialOCLCST_CollectionLiteralPartCS51", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialOCLCST_CollectionLiteralPartCS51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialOCLCST_CollectionLiteralPartCS51"):
                    opp_val = getattr(item, "essentialOCLCST_CollectionLiteralPartCS51", None)
                    
                    setattr(item, "essentialOCLCST_CollectionLiteralPartCS51", self)
                    

    @property
    def essentialOCLCST_SimpleNameCS60(self):
        return self.__essentialOCLCST_SimpleNameCS60

    @essentialOCLCST_SimpleNameCS60.setter
    def essentialOCLCST_SimpleNameCS60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialOCLCST_SimpleNameCS__essentialOCLCST_SimpleNameCS60", None)
        self.__essentialOCLCST_SimpleNameCS60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialOCLCST_VariableCS59"):
                opp_val = getattr(old_value, "essentialOCLCST_VariableCS59", None)
                if opp_val == self:
                    setattr(old_value, "essentialOCLCST_VariableCS59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialOCLCST_VariableCS59"):
                opp_val = getattr(value, "essentialOCLCST_VariableCS59", None)
                setattr(value, "essentialOCLCST_VariableCS59", self)

    @property
    def essentialOCLCST_SimpleNameCS48(self):
        return self.__essentialOCLCST_SimpleNameCS48

    @essentialOCLCST_SimpleNameCS48.setter
    def essentialOCLCST_SimpleNameCS48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialOCLCST_SimpleNameCS__essentialOCLCST_SimpleNameCS48", None)
        self.__essentialOCLCST_SimpleNameCS48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialOCLCST_PathNameCS47"):
                opp_val = getattr(old_value, "essentialOCLCST_PathNameCS47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialOCLCST_PathNameCS47"):
                opp_val = getattr(value, "essentialOCLCST_PathNameCS47", None)
                if opp_val is None:
                    setattr(value, "essentialOCLCST_PathNameCS47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class essentialOCLCST_TupleTypeCS(TypeLiteralExpCS, TypeCS):

    def __init__(self, value: str, essentialOCLCST_TupleTypeCS: set["essentialOCLCST_VariableCS"] = None):
        self.value = value
        self.essentialOCLCST_TupleTypeCS = essentialOCLCST_TupleTypeCS if essentialOCLCST_TupleTypeCS is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def essentialOCLCST_TupleTypeCS(self):
        return self.__essentialOCLCST_TupleTypeCS

    @essentialOCLCST_TupleTypeCS.setter
    def essentialOCLCST_TupleTypeCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialOCLCST_TupleTypeCS__essentialOCLCST_TupleTypeCS", None)
        self.__essentialOCLCST_TupleTypeCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialOCLCST_VariableCS55"):
                    opp_val = getattr(item, "essentialOCLCST_VariableCS55", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialOCLCST_VariableCS55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialOCLCST_VariableCS55"):
                    opp_val = getattr(item, "essentialOCLCST_VariableCS55", None)
                    
                    setattr(item, "essentialOCLCST_VariableCS55", self)
                    

class essentialOCLCST_CollectionTypeCS(TypeLiteralExpCS, CollectionLiteralExpCS, TypeCS):

    pass
class essentialOCLCST_CollectionLiteralPartCS:

    pass
class LiteralExpCS:

    pass
class essentialOCLCST_PrimitiveLiteralExpCS(LiteralExpCS):

    pass
class essentialOCLCST_TupleLiteralExpCS(LiteralExpCS):

    pass
class essentialOCLCST_TypeLiteralExpCS(LiteralExpCS):

    pass
class essentialOCLCST_CollectionLiteralExpCS(LiteralExpCS):

    pass
class essentialOCLCST_OclExpressionCS:

    pass
class essentialOCLCST_PathNameCS(TypeLiteralExpCS, TypeCS):

    pass
class essentialOCLCST_CallArgumentsCS:

    pass
class PrimitiveLiteralExpCS:

    pass
class essentialOCLCST_InvalidLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class essentialOCLCST_RealLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class essentialOCLCST_UnlimitedNaturalLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class essentialOCLCST_StringLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class essentialOCLCST_NullLiteralExpCS(PrimitiveLiteralExpCS):

    pass
class essentialOCLCST_IntegerLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class essentialOCLCST_BooleanLiteralExpCS(PrimitiveLiteralExpCS):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class essentialOCLCST_VariableCS:

    pass
class OclExpressionCS:

    pass
class essentialOCLCST_LetExpCS(OclExpressionCS):

    pass
class essentialOCLCST_CallExpCS(OclExpressionCS):

    pass
class essentialOCLCST_IfExpCS(OclExpressionCS):

    pass
class essentialOCLCST_LiteralExpCS(OclExpressionCS):

    pass
class essentialOCLCST_UnaryExpressionCS(OclExpressionCS):

    def __init__(self, op: str, essentialOCLCST_UnaryExpressionCS: "essentialOCLCST_OclExpressionCS" = None):
        self.op = op
        self.essentialOCLCST_UnaryExpressionCS = essentialOCLCST_UnaryExpressionCS
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def essentialOCLCST_UnaryExpressionCS(self):
        return self.__essentialOCLCST_UnaryExpressionCS

    @essentialOCLCST_UnaryExpressionCS.setter
    def essentialOCLCST_UnaryExpressionCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialOCLCST_UnaryExpressionCS__essentialOCLCST_UnaryExpressionCS", None)
        self.__essentialOCLCST_UnaryExpressionCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialOCLCST_OclExpressionCS57"):
                opp_val = getattr(old_value, "essentialOCLCST_OclExpressionCS57", None)
                if opp_val == self:
                    setattr(old_value, "essentialOCLCST_OclExpressionCS57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialOCLCST_OclExpressionCS57"):
                opp_val = getattr(value, "essentialOCLCST_OclExpressionCS57", None)
                setattr(value, "essentialOCLCST_OclExpressionCS57", self)

class essentialOCLCST_VariableExpCS(OclExpressionCS):

    pass
class CallArgumentsCS:

    pass
class essentialOCLCST_DotIndexArgumentsCS(CallArgumentsCS):

    def __init__(self, isPre: bool, essentialOCLCST_DotIndexArgumentsCS: set["essentialOCLCST_OclExpressionCS"] = None):
        self.isPre = isPre
        self.essentialOCLCST_DotIndexArgumentsCS = essentialOCLCST_DotIndexArgumentsCS if essentialOCLCST_DotIndexArgumentsCS is not None else set()
        
    @property
    def isPre(self) -> bool:
        return self.__isPre

    @isPre.setter
    def isPre(self, isPre: bool):
        self.__isPre = isPre

    @property
    def essentialOCLCST_DotIndexArgumentsCS(self):
        return self.__essentialOCLCST_DotIndexArgumentsCS

    @essentialOCLCST_DotIndexArgumentsCS.setter
    def essentialOCLCST_DotIndexArgumentsCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialOCLCST_DotIndexArgumentsCS__essentialOCLCST_DotIndexArgumentsCS", None)
        self.__essentialOCLCST_DotIndexArgumentsCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "essentialOCLCST_OclExpressionCS32"):
                    opp_val = getattr(item, "essentialOCLCST_OclExpressionCS32", None)
                    
                    if opp_val == self:
                        setattr(item, "essentialOCLCST_OclExpressionCS32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "essentialOCLCST_OclExpressionCS32"):
                    opp_val = getattr(item, "essentialOCLCST_OclExpressionCS32", None)
                    
                    setattr(item, "essentialOCLCST_OclExpressionCS32", self)
                    

class essentialOCLCST_BinaryExpressionCS(OclExpressionCS):

    def __init__(self, op: str, essentialOCLCST_BinaryExpressionCS: "essentialOCLCST_OclExpressionCS" = None, essentialOCLCST_BinaryExpressionCS9: "essentialOCLCST_OclExpressionCS" = None):
        self.op = op
        self.essentialOCLCST_BinaryExpressionCS = essentialOCLCST_BinaryExpressionCS
        self.essentialOCLCST_BinaryExpressionCS9 = essentialOCLCST_BinaryExpressionCS9
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def essentialOCLCST_BinaryExpressionCS9(self):
        return self.__essentialOCLCST_BinaryExpressionCS9

    @essentialOCLCST_BinaryExpressionCS9.setter
    def essentialOCLCST_BinaryExpressionCS9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialOCLCST_BinaryExpressionCS__essentialOCLCST_BinaryExpressionCS9", None)
        self.__essentialOCLCST_BinaryExpressionCS9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialOCLCST_OclExpressionCS10"):
                opp_val = getattr(old_value, "essentialOCLCST_OclExpressionCS10", None)
                if opp_val == self:
                    setattr(old_value, "essentialOCLCST_OclExpressionCS10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialOCLCST_OclExpressionCS10"):
                opp_val = getattr(value, "essentialOCLCST_OclExpressionCS10", None)
                setattr(value, "essentialOCLCST_OclExpressionCS10", self)

    @property
    def essentialOCLCST_BinaryExpressionCS(self):
        return self.__essentialOCLCST_BinaryExpressionCS

    @essentialOCLCST_BinaryExpressionCS.setter
    def essentialOCLCST_BinaryExpressionCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialOCLCST_BinaryExpressionCS__essentialOCLCST_BinaryExpressionCS", None)
        self.__essentialOCLCST_BinaryExpressionCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "essentialOCLCST_OclExpressionCS7"):
                opp_val = getattr(old_value, "essentialOCLCST_OclExpressionCS7", None)
                if opp_val == self:
                    setattr(old_value, "essentialOCLCST_OclExpressionCS7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "essentialOCLCST_OclExpressionCS7"):
                opp_val = getattr(value, "essentialOCLCST_OclExpressionCS7", None)
                setattr(value, "essentialOCLCST_OclExpressionCS7", self)

class essentialOCLCST_ArrowCallArgumentsCS(CallArgumentsCS):

    pass