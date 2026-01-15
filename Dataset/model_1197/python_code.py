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

class CollectionLiteralPart:

    pass
class essentialocl_expressions_CollectionRange(CollectionLiteralPart):

    pass
class essentialocl_expressions_CollectionItem(CollectionLiteralPart):

    pass
class Expression:

    pass
class essentialocl_expressions_ExpressionInOcl(Expression):

    pass
class expressions_essentialocl_EnumerationLiteral:

    pass
class LoopExp:

    pass
class essentialocl_expressions_IterateExp(LoopExp):

    pass
class essentialocl_expressions_IteratorExp(LoopExp):

    pass
class FeatureCallExp:

    pass
class essentialocl_expressions_OperationCallExp(FeatureCallExp):

    pass
class essentialocl_expressions_PropertyCallExp(FeatureCallExp):

    pass
class PrimitiveLiteralExp:

    pass
class essentialocl_expressions_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class essentialocl_expressions_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class TupleLiteralPart:

    pass
class CallExp:

    pass
class essentialocl_expressions_FeatureCallExp(CallExp):

    pass
class essentialocl_expressions_LoopExp(CallExp):

    pass
class expressions_essentialocl_Property:

    pass
class essentialocl_expressions_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class expressions_essentialocl_Operation:

    pass
class NamedElement:

    pass
class TypedElement:

    pass
class essentialocl_expressions_OclExpression(NamedElement, TypedElement):

    def __init__(self, essentialocl_expressions_OclExpression: "OclLibrary" = None):
        self.essentialocl_expressions_OclExpression = essentialocl_expressions_OclExpression
        
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
            if hasattr(old_value, "OclLibrary62"):
                opp_val = getattr(old_value, "OclLibrary62", None)
                if opp_val == self:
                    setattr(old_value, "OclLibrary62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclLibrary62"):
                opp_val = getattr(value, "OclLibrary62", None)
                setattr(value, "OclLibrary62", self)

    def withAsSet(self) -> str:
        # TODO: Implement withAsSet method
        pass

    def withAtPre(self) -> str:
        # TODO: Implement withAtPre method
        pass

class essentialocl_expressions_CollectionLiteralPart(TypedElement):

    pass
class essentialocl_expressions_Variable(NamedElement, TypedElement):

    def __init__(self, essentialocl_expressions_Variable: "expressions_essentialocl_Parameter" = None, essentialocl_expressions_Variable45: "OclExpression" = None):
        self.essentialocl_expressions_Variable = essentialocl_expressions_Variable
        self.essentialocl_expressions_Variable45 = essentialocl_expressions_Variable45
        
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
    def essentialocl_expressions_Variable45(self):
        return self.__essentialocl_expressions_Variable45

    @essentialocl_expressions_Variable45.setter
    def essentialocl_expressions_Variable45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_expressions_Variable__essentialocl_expressions_Variable45", None)
        self.__essentialocl_expressions_Variable45 = value
        
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

    def asParameter(self) -> str:
        # TODO: Implement asParameter method
        pass

    def asProperty(self) -> str:
        # TODO: Implement asProperty method
        pass

class Variable:

    pass
class OclExpression:

    pass
class essentialocl_expressions_LiteralExp(OclExpression):

    pass
class essentialocl_expressions_IfExp(OclExpression):

    pass
class essentialocl_expressions_CallExp(OclExpression):

    pass
class essentialocl_expressions_LetExp(OclExpression):

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
class essentialocl_expressions_TupleLiteralPart(TypedElement):

    pass
class expressions_essentialocl_Type:

    pass
class LiteralExp:

    pass
class essentialocl_expressions_EnumLiteralExp(LiteralExp):

    pass
class essentialocl_expressions_InvalidLiteralExp(LiteralExp):

    pass
class essentialocl_expressions_TupleLiteralExp(LiteralExp):

    pass
class essentialocl_expressions_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, essentialocl_expressions_CollectionLiteralExp: set["CollectionLiteralPart"] = None, essentialocl_expressions_CollectionLiteralExp91: "expressions_essentialocl_Type" = None):
        self.kind = kind
        self.essentialocl_expressions_CollectionLiteralExp = essentialocl_expressions_CollectionLiteralExp if essentialocl_expressions_CollectionLiteralExp is not None else set()
        self.essentialocl_expressions_CollectionLiteralExp91 = essentialocl_expressions_CollectionLiteralExp91
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def essentialocl_expressions_CollectionLiteralExp91(self):
        return self.__essentialocl_expressions_CollectionLiteralExp91

    @essentialocl_expressions_CollectionLiteralExp91.setter
    def essentialocl_expressions_CollectionLiteralExp91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_expressions_CollectionLiteralExp__essentialocl_expressions_CollectionLiteralExp91", None)
        self.__essentialocl_expressions_CollectionLiteralExp91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_essentialocl_Type92"):
                opp_val = getattr(old_value, "expressions_essentialocl_Type92", None)
                if opp_val == self:
                    setattr(old_value, "expressions_essentialocl_Type92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_essentialocl_Type92"):
                opp_val = getattr(value, "expressions_essentialocl_Type92", None)
                setattr(value, "expressions_essentialocl_Type92", self)

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
                    

class essentialocl_expressions_PrimitiveLiteralExp(LiteralExp):

    pass
class essentialocl_expressions_UndefinedLiteralExp(LiteralExp):

    pass
class essentialocl_expressions_TypeLiteralExp(LiteralExp):

    pass
class NumericLiteralExp:

    pass
class essentialocl_expressions_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class essentialocl_expressions_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class essentialocl_expressions_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class expressions_essentialocl_Parameter:

    pass
class InvalidType:

    pass
class VoidType:

    pass
class AnyType:

    pass
class types_essentialocl_PrimitiveType:

    pass
class SequenceType:

    pass
class TypeType:

    pass
class types_essentialocl_Type:

    pass
class OclLibrary:

    pass
class essentialocl_types_OclLibrary:

    def __init__(self, InvalidType: "InvalidType" = None, essentialocl_types_OclLibrary29: "TypeType" = None, essentialocl_types_OclLibrary31: "CollectionType" = None, essentialocl_types_OclLibrary33: "SequenceType" = None, essentialocl_types_OclLibrary: "types_essentialocl_PrimitiveType" = None, essentialocl_types_OclLibrary14: "types_essentialocl_PrimitiveType" = None, essentialocl_types_OclLibrary17: "types_essentialocl_PrimitiveType" = None, essentialocl_types_OclLibrary20: "types_essentialocl_PrimitiveType" = None, essentialocl_types_OclLibrary23: "AnyType" = None, VoidType: "VoidType" = None, essentialocl_types_OclLibrary35: "BagType" = None, essentialocl_types_OclLibrary37: "SetType" = None, essentialocl_types_OclLibrary39: "OrderedSetType" = None, essentialocl_types_OclLibrary41: set["TupleType"] = None):
        self.InvalidType = InvalidType
        self.essentialocl_types_OclLibrary29 = essentialocl_types_OclLibrary29
        self.essentialocl_types_OclLibrary31 = essentialocl_types_OclLibrary31
        self.essentialocl_types_OclLibrary33 = essentialocl_types_OclLibrary33
        self.essentialocl_types_OclLibrary = essentialocl_types_OclLibrary
        self.essentialocl_types_OclLibrary14 = essentialocl_types_OclLibrary14
        self.essentialocl_types_OclLibrary17 = essentialocl_types_OclLibrary17
        self.essentialocl_types_OclLibrary20 = essentialocl_types_OclLibrary20
        self.essentialocl_types_OclLibrary23 = essentialocl_types_OclLibrary23
        self.VoidType = VoidType
        self.essentialocl_types_OclLibrary35 = essentialocl_types_OclLibrary35
        self.essentialocl_types_OclLibrary37 = essentialocl_types_OclLibrary37
        self.essentialocl_types_OclLibrary39 = essentialocl_types_OclLibrary39
        self.essentialocl_types_OclLibrary41 = essentialocl_types_OclLibrary41 if essentialocl_types_OclLibrary41 is not None else set()
        
    @property
    def InvalidType(self):
        return self.__InvalidType

    @InvalidType.setter
    def InvalidType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__InvalidType", None)
        self.__InvalidType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types27"):
                opp_val = getattr(old_value, "types27", None)
                if opp_val == self:
                    setattr(old_value, "types27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types27"):
                opp_val = getattr(value, "types27", None)
                setattr(value, "types27", self)

    @property
    def essentialocl_types_OclLibrary20(self):
        return self.__essentialocl_types_OclLibrary20

    @essentialocl_types_OclLibrary20.setter
    def essentialocl_types_OclLibrary20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary20", None)
        self.__essentialocl_types_OclLibrary20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_essentialocl_PrimitiveType21"):
                opp_val = getattr(old_value, "types_essentialocl_PrimitiveType21", None)
                if opp_val == self:
                    setattr(old_value, "types_essentialocl_PrimitiveType21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_essentialocl_PrimitiveType21"):
                opp_val = getattr(value, "types_essentialocl_PrimitiveType21", None)
                setattr(value, "types_essentialocl_PrimitiveType21", self)

    @property
    def VoidType(self):
        return self.__VoidType

    @VoidType.setter
    def VoidType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__VoidType", None)
        self.__VoidType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types25"):
                opp_val = getattr(old_value, "types25", None)
                if opp_val == self:
                    setattr(old_value, "types25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types25"):
                opp_val = getattr(value, "types25", None)
                setattr(value, "types25", self)

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
            if hasattr(old_value, "BagType"):
                opp_val = getattr(old_value, "BagType", None)
                if opp_val == self:
                    setattr(old_value, "BagType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BagType"):
                opp_val = getattr(value, "BagType", None)
                setattr(value, "BagType", self)

    @property
    def essentialocl_types_OclLibrary14(self):
        return self.__essentialocl_types_OclLibrary14

    @essentialocl_types_OclLibrary14.setter
    def essentialocl_types_OclLibrary14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary14", None)
        self.__essentialocl_types_OclLibrary14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_essentialocl_PrimitiveType15"):
                opp_val = getattr(old_value, "types_essentialocl_PrimitiveType15", None)
                if opp_val == self:
                    setattr(old_value, "types_essentialocl_PrimitiveType15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_essentialocl_PrimitiveType15"):
                opp_val = getattr(value, "types_essentialocl_PrimitiveType15", None)
                setattr(value, "types_essentialocl_PrimitiveType15", self)

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
    def essentialocl_types_OclLibrary39(self):
        return self.__essentialocl_types_OclLibrary39

    @essentialocl_types_OclLibrary39.setter
    def essentialocl_types_OclLibrary39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary39", None)
        self.__essentialocl_types_OclLibrary39 = value
        
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
    def essentialocl_types_OclLibrary37(self):
        return self.__essentialocl_types_OclLibrary37

    @essentialocl_types_OclLibrary37.setter
    def essentialocl_types_OclLibrary37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary37", None)
        self.__essentialocl_types_OclLibrary37 = value
        
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
    def essentialocl_types_OclLibrary33(self):
        return self.__essentialocl_types_OclLibrary33

    @essentialocl_types_OclLibrary33.setter
    def essentialocl_types_OclLibrary33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary33", None)
        self.__essentialocl_types_OclLibrary33 = value
        
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
    def essentialocl_types_OclLibrary31(self):
        return self.__essentialocl_types_OclLibrary31

    @essentialocl_types_OclLibrary31.setter
    def essentialocl_types_OclLibrary31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary31", None)
        self.__essentialocl_types_OclLibrary31 = value
        
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
    def essentialocl_types_OclLibrary23(self):
        return self.__essentialocl_types_OclLibrary23

    @essentialocl_types_OclLibrary23.setter
    def essentialocl_types_OclLibrary23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary23", None)
        self.__essentialocl_types_OclLibrary23 = value
        
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
    def essentialocl_types_OclLibrary17(self):
        return self.__essentialocl_types_OclLibrary17

    @essentialocl_types_OclLibrary17.setter
    def essentialocl_types_OclLibrary17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary17", None)
        self.__essentialocl_types_OclLibrary17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_essentialocl_PrimitiveType18"):
                opp_val = getattr(old_value, "types_essentialocl_PrimitiveType18", None)
                if opp_val == self:
                    setattr(old_value, "types_essentialocl_PrimitiveType18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_essentialocl_PrimitiveType18"):
                opp_val = getattr(value, "types_essentialocl_PrimitiveType18", None)
                setattr(value, "types_essentialocl_PrimitiveType18", self)

    @property
    def essentialocl_types_OclLibrary41(self):
        return self.__essentialocl_types_OclLibrary41

    @essentialocl_types_OclLibrary41.setter
    def essentialocl_types_OclLibrary41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_types_OclLibrary__essentialocl_types_OclLibrary41", None)
        self.__essentialocl_types_OclLibrary41 = value if value is not None else set()
        
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
                    

    def getSetType(self, elementType: Type) -> str:
        # TODO: Implement getSetType method
        pass

    def getTypeType(self, representedType: Type) -> str:
        # TODO: Implement getTypeType method
        pass

    def getBagType(self, elementType: Type) -> str:
        # TODO: Implement getBagType method
        pass

    def getOrderedSetType(self, elementType: Type) -> str:
        # TODO: Implement getOrderedSetType method
        pass

    def getCollectionType(self, elementType: Type) -> str:
        # TODO: Implement getCollectionType method
        pass

    def makeTupleType(self, atts: str) -> str:
        # TODO: Implement makeTupleType method
        pass

    def getSequenceType(self, elementType: Type) -> str:
        # TODO: Implement getSequenceType method
        pass

class Type:

    pass
class essentialocl_types_CollectionType(Type):

    def __init__(self, kind: str, essentialocl_types_CollectionType: "types_essentialocl_Type" = None, essentialocl_types_CollectionType3: "OclLibrary" = None):
        self.kind = kind
        self.essentialocl_types_CollectionType = essentialocl_types_CollectionType
        self.essentialocl_types_CollectionType3 = essentialocl_types_CollectionType3
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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

class essentialocl_types_InvalidType(Type):

    pass
class essentialocl_types_VoidType(Type):

    pass
class essentialocl_types_TypeType(Type):

    pass
class essentialocl_types_AnyType(Type):

    pass
class essentialocl_types_TupleType(Type):

    pass
class CollectionType:

    pass
class essentialocl_types_OrderedSetType(CollectionType):

    pass
class essentialocl_types_SetType(CollectionType):

    pass
class essentialocl_types_SequenceType(CollectionType):

    pass
class essentialocl_types_BagType(CollectionType):

    pass