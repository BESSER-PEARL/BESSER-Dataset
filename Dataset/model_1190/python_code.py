from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionKind(Enum):
    Set = "Set"
    OrderedSet = "OrderedSet"
    Bag = "Bag"
    Sequence = "Sequence"
    Collection = "Collection"


############################################
# Definition of Classes
############################################

class LetExp:

    pass
class Parameter:

    pass
class Class:

    pass
class TupleLiteralExp:

    pass
class TupleLiteralPart:

    pass
class FeatureCallExp:

    pass
class EssentialOCL_NavigationCallExp(FeatureCallExp):

    pass
class Property:

    pass
class NavigationCallExp:

    pass
class EssentialOCL_PropertyCallExp(NavigationCallExp):

    pass
class Operation:

    pass
class EssentialOCL_OperationCallExp(FeatureCallExp):

    pass
class LoopExp:

    pass
class EssentialOCL_IterateExp(LoopExp):

    pass
class EssentialOCL_IteratorExp(LoopExp):

    pass
class NumericLiteralExp:

    pass
class EssentialOCL_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class EssentialOCL_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class EssentialOCL_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class CallExp:

    pass
class EssentialOCL_FeatureCallExp(CallExp):

    pass
class CollectionLiteralExp:

    pass
class TypedElement:

    pass
class EssentialOCL_Variable(TypedElement):

    pass
class EssentialOCL_OclExpression(TypedElement):

    pass
class EssentialOCL_TupleLiteralPart(TypedElement):

    pass
class EssentialOCL_CollectionLiteralPart(TypedElement):

    pass
class Variable:

    pass
class EssentialOCL_ExpressionInOcl(TypedElement):

    pass
class EnumerationLiteral:

    pass
class DataType:

    pass
class EssentialOCL_TupleType(DataType, Class):

    pass
class EssentialOCL_CollectionType(DataType):

    pass
class PrimitiveLiteralExp:

    pass
class EssentialOCL_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class EssentialOCL_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class EssentialOCL_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class CollectionType:

    pass
class EssentialOCL_OrderedSetType(CollectionType):

    pass
class EssentialOCL_SetType(CollectionType):

    pass
class EssentialOCL_SequenceType(CollectionType):

    pass
class EssentialOCL_BagType(CollectionType):

    pass
class Type:

    pass
class EssentialOCL_InvalidType(Type):

    pass
class EssentialOCL_VoidType(Type):

    pass
class EssentialOCL_TemplateParameterType(Type):

    def __init__(self, specification: str, Type59: "EssentialOCL_TypeExp", Type: "EssentialOCL_CollectionType", Type18: "EssentialOCL_ExpressionInOcl"):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class EssentialOCL_AnyType(Type):

    pass
class LiteralExp:

    pass
class EssentialOCL_TupleLiteralExp(LiteralExp):

    pass
class EssentialOCL_InvalidLiteralExp(LiteralExp):

    pass
class EssentialOCL_EnumLiteralExp(LiteralExp):

    pass
class EssentialOCL_PrimitiveLiteralExp(LiteralExp):

    pass
class EssentialOCL_NullLiteralExp(LiteralExp):

    pass
class EssentialOCL_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, EssentialOCL_CollectionLiteralExp: set["CollectionLiteralPart"] = None):
        self.kind = kind
        self.EssentialOCL_CollectionLiteralExp = EssentialOCL_CollectionLiteralExp if EssentialOCL_CollectionLiteralExp is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def EssentialOCL_CollectionLiteralExp(self):
        return self.__EssentialOCL_CollectionLiteralExp

    @EssentialOCL_CollectionLiteralExp.setter
    def EssentialOCL_CollectionLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EssentialOCL_CollectionLiteralExp__EssentialOCL_CollectionLiteralExp", None)
        self.__EssentialOCL_CollectionLiteralExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CollectionLiteralPart"):
                    opp_val = getattr(item, "CollectionLiteralPart", None)
                    
                    if opp_val == self:
                        setattr(item, "CollectionLiteralPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CollectionLiteralPart"):
                    opp_val = getattr(item, "CollectionLiteralPart", None)
                    
                    setattr(item, "CollectionLiteralPart", self)
                    

class CollectionLiteralPart:

    pass
class EssentialOCL_CollectionRange(CollectionLiteralPart):

    pass
class EssentialOCL_CollectionItem(CollectionLiteralPart):

    pass
class OclExpression:

    pass
class EssentialOCL_LiteralExp(OclExpression):

    pass
class EssentialOCL_LetExp(OclExpression):

    pass
class EssentialOCL_IfExp(OclExpression):

    pass
class EssentialOCL_VariableExp(OclExpression):

    pass
class EssentialOCL_LoopExp(OclExpression, CallExp):

    pass
class EssentialOCL_TypeExp(OclExpression):

    pass
class EssentialOCL_CallExp(OclExpression):

    pass