from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionKind(Enum):
    Collection = "Collection"
    Sequence = "Sequence"
    Bag = "Bag"
    Set = "Set"
    OrderedSet = "OrderedSet"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class essentialocl_expressions_ExpressionInOcl(Expression):

    pass
class expressions_essentialocl_EnumerationLiteral:

    pass
class CollectionLiteralPart:

    pass
class essentialocl_expressions_CollectionRange(CollectionLiteralPart):

    pass
class essentialocl_expressions_CollectionItem(CollectionLiteralPart):

    pass
class FeatureCallExp:

    pass
class essentialocl_expressions_PropertyCallExp(FeatureCallExp):

    pass
class LoopExp:

    pass
class essentialocl_expressions_IterateExp(LoopExp):

    pass
class essentialocl_expressions_IteratorExp(LoopExp):

    pass
class CallExp:

    pass
class essentialocl_expressions_FeatureCallExp(CallExp):

    pass
class essentialocl_expressions_LoopExp(CallExp):

    pass
class expressions_essentialocl_Operation:

    pass
class essentialocl_expressions_OperationCallExp(FeatureCallExp):

    pass
class SequenceType:

    pass
class PrimitiveLiteralExp:

    pass
class essentialocl_expressions_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class essentialocl_expressions_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


class essentialocl_expressions_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class TupleLiteralPart:

    pass
class expressions_essentialocl_Property:

    pass
class expressions_essentialocl_Type:

    pass
class LiteralExp:

    pass
class essentialocl_expressions_UndefinedLiteralExp(LiteralExp):

    pass
class essentialocl_expressions_TupleLiteralExp(LiteralExp):

    pass
class essentialocl_expressions_InvalidLiteralExp(LiteralExp):

    pass
class essentialocl_expressions_PrimitiveLiteralExp(LiteralExp):

    pass
class essentialocl_expressions_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, essentialocl_expressions_CollectionLiteralExp: set["CollectionLiteralPart"] = None, essentialocl_expressions_CollectionLiteralExp89: "expressions_essentialocl_Type" = None):
        self.kind = kind
        self.essentialocl_expressions_CollectionLiteralExp = essentialocl_expressions_CollectionLiteralExp if essentialocl_expressions_CollectionLiteralExp is not None else set()
        self.essentialocl_expressions_CollectionLiteralExp89 = essentialocl_expressions_CollectionLiteralExp89
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def essentialocl_expressions_CollectionLiteralExp(self):
        return self.__essentialocl_expressions_CollectionLiteralExp

    @essentialocl_expressions_CollectionLiteralExp.setter
    def essentialocl_expressions_CollectionLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_expressions_CollectionLiteralExp__essentialocl_expressions_CollectionLiteralExp", None)
        self.__essentialocl_expressions_CollectionLiteralExp = value if value is not None else set()
        
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
                    

    @property
    def essentialocl_expressions_CollectionLiteralExp89(self):
        return self.__essentialocl_expressions_CollectionLiteralExp89

    @essentialocl_expressions_CollectionLiteralExp89.setter
    def essentialocl_expressions_CollectionLiteralExp89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_expressions_CollectionLiteralExp__essentialocl_expressions_CollectionLiteralExp89", None)
        self.__essentialocl_expressions_CollectionLiteralExp89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_essentialocl_Type90"):
                opp_val = getattr(old_value, "expressions_essentialocl_Type90", None)
                if opp_val == self:
                    setattr(old_value, "expressions_essentialocl_Type90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_essentialocl_Type90"):
                opp_val = getattr(value, "expressions_essentialocl_Type90", None)
                setattr(value, "expressions_essentialocl_Type90", self)

class essentialocl_expressions_EnumLiteralExp(LiteralExp):

    pass
class essentialocl_expressions_TypeLiteralExp(LiteralExp):

    pass
class NumericLiteralExp:

    pass
class essentialocl_expressions_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol


class essentialocl_expressions_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


class essentialocl_expressions_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


class expressions_essentialocl_Parameter:

    pass
class NamedElement:

    pass
class TypedElement:

    pass
class essentialocl_expressions_CollectionLiteralPart(TypedElement):

    pass
class essentialocl_expressions_TupleLiteralPart(TypedElement):

    pass
class essentialocl_expressions_OclExpression(NamedElement, TypedElement):

    def __init__(self, essentialocl_expressions_OclExpression: "OclLibrary" = None):
        self.essentialocl_expressions_OclExpression = essentialocl_expressions_OclExpression
        
        pass
    @property
    def essentialocl_expressions_OclExpression(self):
        return self.__essentialocl_expressions_OclExpression

    @essentialocl_expressions_OclExpression.setter
    def essentialocl_expressions_OclExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_expressions_OclExpression__essentialocl_expressions_OclExpression", None)
        self.__essentialocl_expressions_OclExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclLibrary60"):
                opp_val = getattr(old_value, "OclLibrary60", None)
                if opp_val == self:
                    setattr(old_value, "OclLibrary60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclLibrary60"):
                opp_val = getattr(value, "OclLibrary60", None)
                setattr(value, "OclLibrary60", self)

    def withAsSet(self) :
        # TODO: Implement withAsSet method
        pass

    def withAtPre(self) :
        # TODO: Implement withAtPre method
        pass

class essentialocl_expressions_Variable(NamedElement, TypedElement):

    def __init__(self, essentialocl_expressions_Variable43: "OclExpression" = None, essentialocl_expressions_Variable: "expressions_essentialocl_Parameter" = None):
        self.essentialocl_expressions_Variable43 = essentialocl_expressions_Variable43
        self.essentialocl_expressions_Variable = essentialocl_expressions_Variable
        
        pass
    @property
    def essentialocl_expressions_Variable(self):
        return self.__essentialocl_expressions_Variable

    @essentialocl_expressions_Variable.setter
    def essentialocl_expressions_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_expressions_Variable__essentialocl_expressions_Variable", None)
        self.__essentialocl_expressions_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_essentialocl_Parameter"):
                opp_val = getattr(old_value, "expressions_essentialocl_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "expressions_essentialocl_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_essentialocl_Parameter"):
                opp_val = getattr(value, "expressions_essentialocl_Parameter", None)
                setattr(value, "expressions_essentialocl_Parameter", self)

    @property
    def essentialocl_expressions_Variable43(self):
        return self.__essentialocl_expressions_Variable43

    @essentialocl_expressions_Variable43.setter
    def essentialocl_expressions_Variable43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_expressions_Variable__essentialocl_expressions_Variable43", None)
        self.__essentialocl_expressions_Variable43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression"):
                opp_val = getattr(old_value, "OclExpression", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression"):
                opp_val = getattr(value, "OclExpression", None)
                setattr(value, "OclExpression", self)

    def asParameter(self) :
        # TODO: Implement asParameter method
        pass

    def asProperty(self) :
        # TODO: Implement asProperty method
        pass

class Variable:

    pass
class OclExpression:

    pass
class essentialocl_expressions_CallExp(OclExpression):

    pass
class essentialocl_expressions_LetExp(OclExpression):

    pass
class essentialocl_expressions_IfExp(OclExpression):

    pass
class essentialocl_expressions_LiteralExp(OclExpression):

    pass
class essentialocl_expressions_VariableExp(OclExpression):

    pass
class TupleType:

    pass
class OrderedSetType:

    pass
class SetType:

    pass
class BagType:

    pass
class TypeType:

    pass
class InvalidType:

    pass
class VoidType:

    pass
class AnyType:

    pass
class types_essentialocl_PrimitiveType:

    pass
class essentialocl_types_OclLibrary:

    def __init__(self, essentialocl_types_OclLibrary: "types_essentialocl_PrimitiveType" = None, essentialocl_types_OclLibrary13: "types_essentialocl_PrimitiveType" = None, essentialocl_types_OclLibrary16: "types_essentialocl_PrimitiveType" = None, essentialocl_types_OclLibrary19: "types_essentialocl_PrimitiveType" = None, essentialocl_types_OclLibrary22: "AnyType" = None, essentialocl_types_OclLibrary31: "SequenceType" = None, oclLibrary: "VoidType" = None, oclLibrary25: "InvalidType" = None, essentialocl_types_OclLibrary27: "TypeType" = None, essentialocl_types_OclLibrary29: "CollectionType" = None, essentialocl_types_OclLibrary33: "BagType" = None, essentialocl_types_OclLibrary35: "SetType" = None, essentialocl_types_OclLibrary37: "OrderedSetType" = None, essentialocl_types_OclLibrary39: set["TupleType"] = None):
        self.essentialocl_types_OclLibrary = essentialocl_types_OclLibrary
        self.essentialocl_types_OclLibrary13 = essentialocl_types_OclLibrary13
        self.essentialocl_types_OclLibrary16 = essentialocl_types_OclLibrary16
        self.essentialocl_types_OclLibrary19 = essentialocl_types_OclLibrary19
        self.essentialocl_types_OclLibrary22 = essentialocl_types_OclLibrary22
        self.essentialocl_types_OclLibrary31 = essentialocl_types_OclLibrary31
        self.oclLibrary = oclLibrary
        self.oclLibrary25 = oclLibrary25
        self.essentialocl_types_OclLibrary27 = essentialocl_types_OclLibrary27
        self.essentialocl_types_OclLibrary29 = essentialocl_types_OclLibrary29
        self.essentialocl_types_OclLibrary33 = essentialocl_types_OclLibrary33
        self.essentialocl_types_OclLibrary35 = essentialocl_types_OclLibrary35
        self.essentialocl_types_OclLibrary37 = essentialocl_types_OclLibrary37
        self.essentialocl_types_OclLibrary39 = essentialocl_types_OclLibrary39 if essentialocl_types_OclLibrary39 is not None else set()
        
        pass
    @property
    def essentialocl_types_OclLibrary13(self):
        return self.__essentialocl_types_OclLibrary13

    @essentialocl_types_OclLibrary13.setter
    def essentialocl_types_OclLibrary13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary13", None)
        self.__essentialocl_types_OclLibrary13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_essentialocl_PrimitiveType14"):
                opp_val = getattr(old_value, "types_essentialocl_PrimitiveType14", None)
                if opp_val == self:
                    setattr(old_value, "types_essentialocl_PrimitiveType14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_essentialocl_PrimitiveType14"):
                opp_val = getattr(value, "types_essentialocl_PrimitiveType14", None)
                setattr(value, "types_essentialocl_PrimitiveType14", self)

    @property
    def essentialocl_types_OclLibrary22(self):
        return self.__essentialocl_types_OclLibrary22

    @essentialocl_types_OclLibrary22.setter
    def essentialocl_types_OclLibrary22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary22", None)
        self.__essentialocl_types_OclLibrary22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnyType"):
                opp_val = getattr(old_value, "AnyType", None)
                if opp_val == self:
                    setattr(old_value, "AnyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnyType"):
                opp_val = getattr(value, "AnyType", None)
                setattr(value, "AnyType", self)

    @property
    def essentialocl_types_OclLibrary31(self):
        return self.__essentialocl_types_OclLibrary31

    @essentialocl_types_OclLibrary31.setter
    def essentialocl_types_OclLibrary31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary31", None)
        self.__essentialocl_types_OclLibrary31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SequenceType"):
                opp_val = getattr(old_value, "SequenceType", None)
                if opp_val == self:
                    setattr(old_value, "SequenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SequenceType"):
                opp_val = getattr(value, "SequenceType", None)
                setattr(value, "SequenceType", self)

    @property
    def essentialocl_types_OclLibrary35(self):
        return self.__essentialocl_types_OclLibrary35

    @essentialocl_types_OclLibrary35.setter
    def essentialocl_types_OclLibrary35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary35", None)
        self.__essentialocl_types_OclLibrary35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SetType"):
                opp_val = getattr(old_value, "SetType", None)
                if opp_val == self:
                    setattr(old_value, "SetType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SetType"):
                opp_val = getattr(value, "SetType", None)
                setattr(value, "SetType", self)

    @property
    def essentialocl_types_OclLibrary19(self):
        return self.__essentialocl_types_OclLibrary19

    @essentialocl_types_OclLibrary19.setter
    def essentialocl_types_OclLibrary19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary19", None)
        self.__essentialocl_types_OclLibrary19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_essentialocl_PrimitiveType20"):
                opp_val = getattr(old_value, "types_essentialocl_PrimitiveType20", None)
                if opp_val == self:
                    setattr(old_value, "types_essentialocl_PrimitiveType20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_essentialocl_PrimitiveType20"):
                opp_val = getattr(value, "types_essentialocl_PrimitiveType20", None)
                setattr(value, "types_essentialocl_PrimitiveType20", self)

    @property
    def essentialocl_types_OclLibrary29(self):
        return self.__essentialocl_types_OclLibrary29

    @essentialocl_types_OclLibrary29.setter
    def essentialocl_types_OclLibrary29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary29", None)
        self.__essentialocl_types_OclLibrary29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CollectionType"):
                opp_val = getattr(old_value, "CollectionType", None)
                if opp_val == self:
                    setattr(old_value, "CollectionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CollectionType"):
                opp_val = getattr(value, "CollectionType", None)
                setattr(value, "CollectionType", self)

    @property
    def essentialocl_types_OclLibrary(self):
        return self.__essentialocl_types_OclLibrary

    @essentialocl_types_OclLibrary.setter
    def essentialocl_types_OclLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary", None)
        self.__essentialocl_types_OclLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_essentialocl_PrimitiveType"):
                opp_val = getattr(old_value, "types_essentialocl_PrimitiveType", None)
                if opp_val == self:
                    setattr(old_value, "types_essentialocl_PrimitiveType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_essentialocl_PrimitiveType"):
                opp_val = getattr(value, "types_essentialocl_PrimitiveType", None)
                setattr(value, "types_essentialocl_PrimitiveType", self)

    @property
    def essentialocl_types_OclLibrary37(self):
        return self.__essentialocl_types_OclLibrary37

    @essentialocl_types_OclLibrary37.setter
    def essentialocl_types_OclLibrary37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary37", None)
        self.__essentialocl_types_OclLibrary37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrderedSetType"):
                opp_val = getattr(old_value, "OrderedSetType", None)
                if opp_val == self:
                    setattr(old_value, "OrderedSetType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrderedSetType"):
                opp_val = getattr(value, "OrderedSetType", None)
                setattr(value, "OrderedSetType", self)

    @property
    def essentialocl_types_OclLibrary39(self):
        return self.__essentialocl_types_OclLibrary39

    @essentialocl_types_OclLibrary39.setter
    def essentialocl_types_OclLibrary39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary39", None)
        self.__essentialocl_types_OclLibrary39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TupleType"):
                    opp_val = getattr(item, "TupleType", None)
                    
                    if opp_val == self:
                        setattr(item, "TupleType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TupleType"):
                    opp_val = getattr(item, "TupleType", None)
                    
                    setattr(item, "TupleType", self)
                    

    @property
    def essentialocl_types_OclLibrary27(self):
        return self.__essentialocl_types_OclLibrary27

    @essentialocl_types_OclLibrary27.setter
    def essentialocl_types_OclLibrary27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary27", None)
        self.__essentialocl_types_OclLibrary27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeType"):
                opp_val = getattr(old_value, "TypeType", None)
                if opp_val == self:
                    setattr(old_value, "TypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeType"):
                opp_val = getattr(value, "TypeType", None)
                setattr(value, "TypeType", self)

    @property
    def essentialocl_types_OclLibrary16(self):
        return self.__essentialocl_types_OclLibrary16

    @essentialocl_types_OclLibrary16.setter
    def essentialocl_types_OclLibrary16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary16", None)
        self.__essentialocl_types_OclLibrary16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_essentialocl_PrimitiveType17"):
                opp_val = getattr(old_value, "types_essentialocl_PrimitiveType17", None)
                if opp_val == self:
                    setattr(old_value, "types_essentialocl_PrimitiveType17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_essentialocl_PrimitiveType17"):
                opp_val = getattr(value, "types_essentialocl_PrimitiveType17", None)
                setattr(value, "types_essentialocl_PrimitiveType17", self)

    @property
    def oclLibrary(self):
        return self.__oclLibrary

    @oclLibrary.setter
    def oclLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__oclLibrary", None)
        self.__oclLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VoidType"):
                opp_val = getattr(old_value, "VoidType", None)
                if opp_val == self:
                    setattr(old_value, "VoidType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VoidType"):
                opp_val = getattr(value, "VoidType", None)
                setattr(value, "VoidType", self)

    @property
    def oclLibrary25(self):
        return self.__oclLibrary25

    @oclLibrary25.setter
    def oclLibrary25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__oclLibrary25", None)
        self.__oclLibrary25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InvalidType"):
                opp_val = getattr(old_value, "InvalidType", None)
                if opp_val == self:
                    setattr(old_value, "InvalidType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InvalidType"):
                opp_val = getattr(value, "InvalidType", None)
                setattr(value, "InvalidType", self)

    @property
    def essentialocl_types_OclLibrary33(self):
        return self.__essentialocl_types_OclLibrary33

    @essentialocl_types_OclLibrary33.setter
    def essentialocl_types_OclLibrary33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary33", None)
        self.__essentialocl_types_OclLibrary33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BagType"):
                opp_val = getattr(old_value, "BagType", None)
                if opp_val == self:
                    setattr(old_value, "BagType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BagType"):
                opp_val = getattr(value, "BagType", None)
                setattr(value, "BagType", self)

    def makeTupleType(self, essentialocl_atts) :
        # TODO: Implement makeTupleType method
        pass

    def getBagType(self, essentialocl_elementType) :
        # TODO: Implement getBagType method
        pass

    def getCollectionType(self, essentialocl_elementType) :
        # TODO: Implement getCollectionType method
        pass

    def getSetType(self, essentialocl_elementType) :
        # TODO: Implement getSetType method
        pass

    def getSequenceType(self, essentialocl_elementType) :
        # TODO: Implement getSequenceType method
        pass

    def getOrderedSetType(self, essentialocl_elementType) :
        # TODO: Implement getOrderedSetType method
        pass

    def getTypeType(self, essentialocl_representedType) :
        # TODO: Implement getTypeType method
        pass

class types_essentialocl_Type:

    pass
class OclLibrary:

    pass
class Type:

    pass
class essentialocl_types_CollectionType(Type):

    def __init__(self, kind: str, essentialocl_types_CollectionType: "types_essentialocl_Type" = None, essentialocl_types_CollectionType3: "OclLibrary" = None):
        self.kind = kind
        self.essentialocl_types_CollectionType = essentialocl_types_CollectionType
        self.essentialocl_types_CollectionType3 = essentialocl_types_CollectionType3
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def essentialocl_types_CollectionType(self):
        return self.__essentialocl_types_CollectionType

    @essentialocl_types_CollectionType.setter
    def essentialocl_types_CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_CollectionType__essentialocl_types_CollectionType", None)
        self.__essentialocl_types_CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_essentialocl_Type"):
                opp_val = getattr(old_value, "types_essentialocl_Type", None)
                if opp_val == self:
                    setattr(old_value, "types_essentialocl_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_essentialocl_Type"):
                opp_val = getattr(value, "types_essentialocl_Type", None)
                setattr(value, "types_essentialocl_Type", self)

    @property
    def essentialocl_types_CollectionType3(self):
        return self.__essentialocl_types_CollectionType3

    @essentialocl_types_CollectionType3.setter
    def essentialocl_types_CollectionType3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_CollectionType__essentialocl_types_CollectionType3", None)
        self.__essentialocl_types_CollectionType3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclLibrary4"):
                opp_val = getattr(old_value, "OclLibrary4", None)
                if opp_val == self:
                    setattr(old_value, "OclLibrary4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclLibrary4"):
                opp_val = getattr(value, "OclLibrary4", None)
                setattr(value, "OclLibrary4", self)

class essentialocl_types_VoidType(Type):

    pass
class essentialocl_types_TypeType(Type):

    pass
class essentialocl_types_AnyType(Type):

    pass
class essentialocl_types_InvalidType(Type):

    pass
class essentialocl_types_TupleType(Type):

    pass
class CollectionType:

    pass
class essentialocl_types_SetType(CollectionType):

    pass
class essentialocl_types_OrderedSetType(CollectionType):

    pass
class essentialocl_types_SequenceType(CollectionType):

    pass
class essentialocl_types_BagType(CollectionType):

    pass