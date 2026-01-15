from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclModelElement:

    pass
class OclFeature:

    pass
class atlstatic_OCL_Attribute(OclFeature):

    def __init__(self, name: str, OclExpression257: "OclExpression" = None, OclType260: "OclType" = None, OCL243: "atlstatic_OCL_OclFeatureDefinition"):
        self.name = name
        self.OclExpression257 = OclExpression257
        self.OclType260 = OclType260
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclType260(self):
        return self.__OclType260

    @OclType260.setter
    def OclType260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Attribute__OclType260", None)
        self.__OclType260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL261"):
                opp_val = getattr(old_value, "OCL261", None)
                if opp_val == self:
                    setattr(old_value, "OCL261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL261"):
                opp_val = getattr(value, "OCL261", None)
                setattr(value, "OCL261", self)

    @property
    def OclExpression257(self):
        return self.__OclExpression257

    @OclExpression257.setter
    def OclExpression257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Attribute__OclExpression257", None)
        self.__OclExpression257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL258"):
                opp_val = getattr(old_value, "OCL258", None)
                if opp_val == self:
                    setattr(old_value, "OCL258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL258"):
                opp_val = getattr(value, "OCL258", None)
                setattr(value, "OCL258", self)

class atlstatic_OCL_Operation(OclFeature):

    def __init__(self, name: str, atlstatic_OCL_Operation: set["Parameter"] = None, OclType265: "OclType" = None, OclExpression268: "OclExpression" = None, OCL243: "atlstatic_OCL_OclFeatureDefinition"):
        self.name = name
        self.atlstatic_OCL_Operation = atlstatic_OCL_Operation if atlstatic_OCL_Operation is not None else set()
        self.OclType265 = OclType265
        self.OclExpression268 = OclExpression268
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclType265(self):
        return self.__OclType265

    @OclType265.setter
    def OclType265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Operation__OclType265", None)
        self.__OclType265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL266"):
                opp_val = getattr(old_value, "OCL266", None)
                if opp_val == self:
                    setattr(old_value, "OCL266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL266"):
                opp_val = getattr(value, "OCL266", None)
                setattr(value, "OCL266", self)

    @property
    def atlstatic_OCL_Operation(self):
        return self.__atlstatic_OCL_Operation

    @atlstatic_OCL_Operation.setter
    def atlstatic_OCL_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Operation__atlstatic_OCL_Operation", None)
        self.__atlstatic_OCL_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter263"):
                    opp_val = getattr(item, "Parameter263", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter263", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter263"):
                    opp_val = getattr(item, "Parameter263", None)
                    
                    setattr(item, "Parameter263", self)
                    

    @property
    def OclExpression268(self):
        return self.__OclExpression268

    @OclExpression268.setter
    def OclExpression268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Operation__OclExpression268", None)
        self.__OclExpression268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL269"):
                opp_val = getattr(old_value, "OCL269", None)
                if opp_val == self:
                    setattr(old_value, "OCL269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL269"):
                opp_val = getattr(value, "OCL269", None)
                setattr(value, "OCL269", self)

class TupleType:

    pass
class NumericType:

    pass
class atlstatic_OCL_RealType(NumericType):

    pass
class atlstatic_OCL_IntegerType(NumericType):

    pass
class Primitive:

    pass
class atlstatic_OCL_BooleanType(Primitive):

    pass
class atlstatic_OCL_NumericType(Primitive):

    pass
class atlstatic_OCL_StringType(Primitive):

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class atlstatic_OCL_SequenceType(CollectionType):

    pass
class atlstatic_OCL_SetType(CollectionType):

    pass
class atlstatic_OCL_BagType(CollectionType):

    pass
class atlstatic_OCL_OrderedSetType(CollectionType):

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class MapExp:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class TuplePart:

    pass
class NumericExp:

    pass
class atlstatic_OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class atlstatic_OCL_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class PrimitiveExp:

    pass
class atlstatic_OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class atlstatic_OCL_NumericExp(PrimitiveExp):

    pass
class atlstatic_OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class Attribute:

    pass
class Operation:

    pass
class OperationCallExp:

    pass
class atlstatic_OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class atlstatic_OCL_OperatorCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class atlstatic_OCL_IterateExp(LoopExp):

    pass
class atlstatic_OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, OCL198: "atlstatic_OCL_Iterator", OCL119: "atlstatic_OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class LetExp:

    pass
class CollectionExp:

    pass
class atlstatic_OCL_BagExp(CollectionExp):

    pass
class atlstatic_OCL_SequenceExp(CollectionExp):

    pass
class atlstatic_OCL_SetExp(CollectionExp):

    pass
class atlstatic_OCL_OrderedSetExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class atlstatic_OCL_LoopExp(PropertyCallExp):

    pass
class atlstatic_OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, OCL113: "atlstatic_OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class atlstatic_OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, OclExpression157: set["OclExpression"] = None, OCL113: "atlstatic_OCL_OclExpression"):
        self.operationName = operationName
        self.OclExpression157 = OclExpression157 if OclExpression157 is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def OclExpression157(self):
        return self.__OclExpression157

    @OclExpression157.setter
    def OclExpression157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OperationCallExp__OclExpression157", None)
        self.__OclExpression157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL158"):
                    opp_val = getattr(item, "OCL158", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL158"):
                    opp_val = getattr(item, "OCL158", None)
                    
                    setattr(item, "OCL158", self)
                    

class IfExp:

    pass
class OclType:

    pass
class atlstatic_OCL_Primitive(OclType):

    pass
class atlstatic_OCL_MapType(OclType):

    pass
class atlstatic_OCL_CollectionType(OclType):

    pass
class atlstatic_OCL_OclModelElement(OclType):

    pass
class atlstatic_OCL_OclAnyType(OclType):

    pass
class atlstatic_OCL_TupleType(OclType):

    pass
class Statement:

    pass
class atlstatic_ATL_IfStat(Statement):

    pass
class atlstatic_ATL_ForStat(Statement):

    pass
class atlstatic_ATL_BindingStat(Statement):

    def __init__(self, propertyName: str, isAssignment: str, atlstatic_ATL_BindingStat: "OclExpression" = None, atlstatic_ATL_BindingStat91: "OclExpression" = None, Statement: "atlstatic_ATL_ActionBlock", Statement108: "atlstatic_ATL_ForStat", Statement97: "atlstatic_ATL_IfStat", Statement100: "atlstatic_ATL_IfStat"):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlstatic_ATL_BindingStat = atlstatic_ATL_BindingStat
        self.atlstatic_ATL_BindingStat91 = atlstatic_ATL_BindingStat91
        
    @property
    def isAssignment(self) -> str:
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment

    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def atlstatic_ATL_BindingStat91(self):
        return self.__atlstatic_ATL_BindingStat91

    @atlstatic_ATL_BindingStat91.setter
    def atlstatic_ATL_BindingStat91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_BindingStat__atlstatic_ATL_BindingStat91", None)
        self.__atlstatic_ATL_BindingStat91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression92"):
                opp_val = getattr(old_value, "OclExpression92", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression92"):
                opp_val = getattr(value, "OclExpression92", None)
                setattr(value, "OclExpression92", self)

    @property
    def atlstatic_ATL_BindingStat(self):
        return self.__atlstatic_ATL_BindingStat

    @atlstatic_ATL_BindingStat.setter
    def atlstatic_ATL_BindingStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_BindingStat__atlstatic_ATL_BindingStat", None)
        self.__atlstatic_ATL_BindingStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression89"):
                opp_val = getattr(old_value, "OclExpression89", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression89"):
                opp_val = getattr(value, "OclExpression89", None)
                setattr(value, "OclExpression89", self)

class atlstatic_ATL_ExpressionStat(Statement):

    pass
class Iterator:

    pass
class Binding:

    pass
class Parameter:

    pass
class PatternElement:

    pass
class atlstatic_ATL_OutPatternElement(PatternElement):

    pass
class atlstatic_ATL_InPatternElement(PatternElement):

    pass
class VariableDeclaration:

    pass
class atlstatic_OCL_Parameter(VariableDeclaration):

    pass
class atlstatic_ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class atlstatic_OCL_Iterator(VariableDeclaration):

    pass
class atlstatic_OCL_TuplePart(VariableDeclaration):

    pass
class atlstatic_ATL_PatternElement(VariableDeclaration):

    pass
class OutPatternElement:

    pass
class atlstatic_ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class atlstatic_ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class DropPattern:

    pass
class InPatternElement:

    pass
class atlstatic_ATL_SimpleInPatternElement(InPatternElement):

    pass
class ModuleElement:

    pass
class OclModel:

    pass
class MatchedRule:

    pass
class atlstatic_ATL_LazyMatchedRule(MatchedRule):

    def __init__(self, isUnique: str, ATL36: "atlstatic_ATL_InPattern", ATL30: "atlstatic_ATL_MatchedRule", ATL27: "atlstatic_ATL_MatchedRule"):
        self.isUnique = isUnique
        
    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

class OclExpression:

    pass
class atlstatic_OCL_MapExp(OclExpression):

    pass
class atlstatic_OCL_OclUndefinedExp(OclExpression):

    pass
class atlstatic_OCL_OclType(OclExpression):

    def __init__(self, name: str, OclContextDefinition: "OclContextDefinition" = None, OclExpression205: "OclExpression" = None, MapType: "MapType" = None, Attribute213: "Attribute" = None, MapType216: "MapType" = None, CollectionType: "CollectionType" = None, TupleTypeAttribute: "TupleTypeAttribute" = None, VariableDeclaration223: "VariableDeclaration" = None, Operation208: "Operation" = None, OclExpression89: "atlstatic_ATL_BindingStat", OCL176: "atlstatic_OCL_IfExp", OclExpression92: "atlstatic_ATL_BindingStat", OCL188: "atlstatic_OCL_VariableDeclaration", OCL155: "atlstatic_OCL_PropertyCallExp", OclExpression73: "atlstatic_ATL_Binding", OCL158: "atlstatic_OCL_OperationCallExp", OclExpression69: "atlstatic_ATL_ForEachOutPatternElement", OclExpression67: "atlstatic_ATL_SimpleOutPatternElement", OclExpression: "atlstatic_ATL_Query", OCL179: "atlstatic_OCL_IfExp", OclExpression94: "atlstatic_ATL_IfStat", OclExpression87: "atlstatic_ATL_ExpressionStat", OCL139: "atlstatic_OCL_CollectionExp", OclExpression105: "atlstatic_ATL_ForStat", OCL161: "atlstatic_OCL_LoopExp", OclExpression149: "atlstatic_OCL_MapElement", OCL258: "atlstatic_OCL_Attribute", OCL206: "atlstatic_OCL_OclType", OCL269: "atlstatic_OCL_Operation", OCL173: "atlstatic_OCL_LetExp", OclExpression152: "atlstatic_OCL_MapElement", OCL182: "atlstatic_OCL_IfExp", OclExpression38: "atlstatic_ATL_InPattern"):
        self.name = name
        self.OclContextDefinition = OclContextDefinition
        self.OclExpression205 = OclExpression205
        self.MapType = MapType
        self.Attribute213 = Attribute213
        self.MapType216 = MapType216
        self.CollectionType = CollectionType
        self.TupleTypeAttribute = TupleTypeAttribute
        self.VariableDeclaration223 = VariableDeclaration223
        self.Operation208 = Operation208
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MapType216(self):
        return self.__MapType216

    @MapType216.setter
    def MapType216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__MapType216", None)
        self.__MapType216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL217"):
                opp_val = getattr(old_value, "OCL217", None)
                if opp_val == self:
                    setattr(old_value, "OCL217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL217"):
                opp_val = getattr(value, "OCL217", None)
                setattr(value, "OCL217", self)

    @property
    def VariableDeclaration223(self):
        return self.__VariableDeclaration223

    @VariableDeclaration223.setter
    def VariableDeclaration223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__VariableDeclaration223", None)
        self.__VariableDeclaration223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL224"):
                opp_val = getattr(old_value, "OCL224", None)
                if opp_val == self:
                    setattr(old_value, "OCL224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL224"):
                opp_val = getattr(value, "OCL224", None)
                setattr(value, "OCL224", self)

    @property
    def TupleTypeAttribute(self):
        return self.__TupleTypeAttribute

    @TupleTypeAttribute.setter
    def TupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__TupleTypeAttribute", None)
        self.__TupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL221"):
                opp_val = getattr(old_value, "OCL221", None)
                if opp_val == self:
                    setattr(old_value, "OCL221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL221"):
                opp_val = getattr(value, "OCL221", None)
                setattr(value, "OCL221", self)

    @property
    def Operation208(self):
        return self.__Operation208

    @Operation208.setter
    def Operation208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__Operation208", None)
        self.__Operation208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL209"):
                opp_val = getattr(old_value, "OCL209", None)
                if opp_val == self:
                    setattr(old_value, "OCL209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL209"):
                opp_val = getattr(value, "OCL209", None)
                setattr(value, "OCL209", self)

    @property
    def OclExpression205(self):
        return self.__OclExpression205

    @OclExpression205.setter
    def OclExpression205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__OclExpression205", None)
        self.__OclExpression205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL206"):
                opp_val = getattr(old_value, "OCL206", None)
                if opp_val == self:
                    setattr(old_value, "OCL206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL206"):
                opp_val = getattr(value, "OCL206", None)
                setattr(value, "OCL206", self)

    @property
    def CollectionType(self):
        return self.__CollectionType

    @CollectionType.setter
    def CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__CollectionType", None)
        self.__CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL219"):
                opp_val = getattr(old_value, "OCL219", None)
                if opp_val == self:
                    setattr(old_value, "OCL219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL219"):
                opp_val = getattr(value, "OCL219", None)
                setattr(value, "OCL219", self)

    @property
    def Attribute213(self):
        return self.__Attribute213

    @Attribute213.setter
    def Attribute213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__Attribute213", None)
        self.__Attribute213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL214"):
                opp_val = getattr(old_value, "OCL214", None)
                if opp_val == self:
                    setattr(old_value, "OCL214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL214"):
                opp_val = getattr(value, "OCL214", None)
                setattr(value, "OCL214", self)

    @property
    def MapType(self):
        return self.__MapType

    @MapType.setter
    def MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__MapType", None)
        self.__MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL211"):
                opp_val = getattr(old_value, "OCL211", None)
                if opp_val == self:
                    setattr(old_value, "OCL211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL211"):
                opp_val = getattr(value, "OCL211", None)
                setattr(value, "OCL211", self)

    @property
    def OclContextDefinition(self):
        return self.__OclContextDefinition

    @OclContextDefinition.setter
    def OclContextDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__OclContextDefinition", None)
        self.__OclContextDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL203"):
                opp_val = getattr(old_value, "OCL203", None)
                if opp_val == self:
                    setattr(old_value, "OCL203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL203"):
                opp_val = getattr(value, "OCL203", None)
                setattr(value, "OCL203", self)

class atlstatic_OCL_PropertyCallExp(OclExpression):

    pass
class atlstatic_OCL_VariableExp(OclExpression):

    pass
class atlstatic_OCL_IfExp(OclExpression):

    pass
class atlstatic_OCL_CollectionExp(OclExpression):

    pass
class atlstatic_OCL_PrimitiveExp(OclExpression):

    pass
class atlstatic_OCL_SuperExp(OclExpression):

    pass
class atlstatic_OCL_TupleExp(OclExpression):

    pass
class atlstatic_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression89: "atlstatic_ATL_BindingStat", OCL176: "atlstatic_OCL_IfExp", OclExpression92: "atlstatic_ATL_BindingStat", OCL188: "atlstatic_OCL_VariableDeclaration", OCL155: "atlstatic_OCL_PropertyCallExp", OclExpression73: "atlstatic_ATL_Binding", OCL158: "atlstatic_OCL_OperationCallExp", OclExpression69: "atlstatic_ATL_ForEachOutPatternElement", OclExpression67: "atlstatic_ATL_SimpleOutPatternElement", OclExpression: "atlstatic_ATL_Query", OCL179: "atlstatic_OCL_IfExp", OclExpression94: "atlstatic_ATL_IfStat", OclExpression87: "atlstatic_ATL_ExpressionStat", OCL139: "atlstatic_OCL_CollectionExp", OclExpression105: "atlstatic_ATL_ForStat", OCL161: "atlstatic_OCL_LoopExp", OclExpression149: "atlstatic_OCL_MapElement", OCL258: "atlstatic_OCL_Attribute", OCL206: "atlstatic_OCL_OclType", OCL269: "atlstatic_OCL_Operation", OCL173: "atlstatic_OCL_LetExp", OclExpression152: "atlstatic_OCL_MapElement", OCL182: "atlstatic_OCL_IfExp", OclExpression38: "atlstatic_ATL_InPattern"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class atlstatic_OCL_LetExp(OclExpression):

    pass
class InPattern:

    pass
class Rule:

    pass
class atlstatic_ATL_CalledRule(Rule):

    def __init__(self, isEntrypoint: str, isEndpoint: str, atlstatic_ATL_CalledRule: set["Parameter"] = None, ATL79: "atlstatic_ATL_RuleVariableDeclaration", ATL40: "atlstatic_ATL_OutPattern", ATL84: "atlstatic_ATL_ActionBlock"):
        self.isEntrypoint = isEntrypoint
        self.isEndpoint = isEndpoint
        self.atlstatic_ATL_CalledRule = atlstatic_ATL_CalledRule if atlstatic_ATL_CalledRule is not None else set()
        
    @property
    def isEntrypoint(self) -> str:
        return self.__isEntrypoint

    @isEntrypoint.setter
    def isEntrypoint(self, isEntrypoint: str):
        self.__isEntrypoint = isEntrypoint

    @property
    def isEndpoint(self) -> str:
        return self.__isEndpoint

    @isEndpoint.setter
    def isEndpoint(self, isEndpoint: str):
        self.__isEndpoint = isEndpoint

    @property
    def atlstatic_ATL_CalledRule(self):
        return self.__atlstatic_ATL_CalledRule

    @atlstatic_ATL_CalledRule.setter
    def atlstatic_ATL_CalledRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_CalledRule__atlstatic_ATL_CalledRule", None)
        self.__atlstatic_ATL_CalledRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

class atlstatic_ATL_MatchedRule(Rule):

    def __init__(self, isAbstract: str, isRefining: str, isNoDefault: str, InPattern: "InPattern" = None, MatchedRule: set["MatchedRule"] = None, MatchedRule29: "MatchedRule" = None, ATL79: "atlstatic_ATL_RuleVariableDeclaration", ATL40: "atlstatic_ATL_OutPattern", ATL84: "atlstatic_ATL_ActionBlock"):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.InPattern = InPattern
        self.MatchedRule = MatchedRule if MatchedRule is not None else set()
        self.MatchedRule29 = MatchedRule29
        
    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

    @property
    def isNoDefault(self) -> str:
        return self.__isNoDefault

    @isNoDefault.setter
    def isNoDefault(self, isNoDefault: str):
        self.__isNoDefault = isNoDefault

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def InPattern(self):
        return self.__InPattern

    @InPattern.setter
    def InPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_MatchedRule__InPattern", None)
        self.__InPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL25"):
                opp_val = getattr(old_value, "ATL25", None)
                if opp_val == self:
                    setattr(old_value, "ATL25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL25"):
                opp_val = getattr(value, "ATL25", None)
                setattr(value, "ATL25", self)

    @property
    def MatchedRule29(self):
        return self.__MatchedRule29

    @MatchedRule29.setter
    def MatchedRule29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_MatchedRule__MatchedRule29", None)
        self.__MatchedRule29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL30"):
                opp_val = getattr(old_value, "ATL30", None)
                if opp_val == self:
                    setattr(old_value, "ATL30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL30"):
                opp_val = getattr(value, "ATL30", None)
                setattr(value, "ATL30", self)

    @property
    def MatchedRule(self):
        return self.__MatchedRule

    @MatchedRule.setter
    def MatchedRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_MatchedRule__MatchedRule", None)
        self.__MatchedRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL27"):
                    opp_val = getattr(item, "ATL27", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL27"):
                    opp_val = getattr(item, "ATL27", None)
                    
                    setattr(item, "ATL27", self)
                    

class Helper:

    pass
class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class OutPattern:

    pass
class atlstatic_ATL_Rule(ModuleElement):

    def __init__(self, name: str, OutPattern: "OutPattern" = None, ActionBlock: "ActionBlock" = None, RuleVariableDeclaration: set["RuleVariableDeclaration"] = None, ModuleElement: "atlstatic_ATL_Module"):
        self.name = name
        self.OutPattern = OutPattern
        self.ActionBlock = ActionBlock
        self.RuleVariableDeclaration = RuleVariableDeclaration if RuleVariableDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ActionBlock(self):
        return self.__ActionBlock

    @ActionBlock.setter
    def ActionBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Rule__ActionBlock", None)
        self.__ActionBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL21"):
                opp_val = getattr(old_value, "ATL21", None)
                if opp_val == self:
                    setattr(old_value, "ATL21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL21"):
                opp_val = getattr(value, "ATL21", None)
                setattr(value, "ATL21", self)

    @property
    def RuleVariableDeclaration(self):
        return self.__RuleVariableDeclaration

    @RuleVariableDeclaration.setter
    def RuleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Rule__RuleVariableDeclaration", None)
        self.__RuleVariableDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL23"):
                    opp_val = getattr(item, "ATL23", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL23"):
                    opp_val = getattr(item, "ATL23", None)
                    
                    setattr(item, "ATL23", self)
                    

    @property
    def OutPattern(self):
        return self.__OutPattern

    @OutPattern.setter
    def OutPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Rule__OutPattern", None)
        self.__OutPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL19"):
                opp_val = getattr(old_value, "ATL19", None)
                if opp_val == self:
                    setattr(old_value, "ATL19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL19"):
                opp_val = getattr(value, "ATL19", None)
                setattr(value, "ATL19", self)

class OclFeatureDefinition:

    pass
class Library:

    pass
class Query:

    pass
class atlstatic_ATL_Helper(ModuleElement):

    pass
class Unit:

    pass
class atlstatic_ATL_Module(Unit):

    def __init__(self, isRefining: str, atlstatic_ATL_Module: set["OclModel"] = None, atlstatic_ATL_Module9: set["OclModel"] = None, atlstatic_ATL_Module12: set["ModuleElement"] = None, ATL81: "atlstatic_ATL_LibraryRef"):
        self.isRefining = isRefining
        self.atlstatic_ATL_Module = atlstatic_ATL_Module if atlstatic_ATL_Module is not None else set()
        self.atlstatic_ATL_Module9 = atlstatic_ATL_Module9 if atlstatic_ATL_Module9 is not None else set()
        self.atlstatic_ATL_Module12 = atlstatic_ATL_Module12 if atlstatic_ATL_Module12 is not None else set()
        
    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

    @property
    def atlstatic_ATL_Module12(self):
        return self.__atlstatic_ATL_Module12

    @atlstatic_ATL_Module12.setter
    def atlstatic_ATL_Module12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Module__atlstatic_ATL_Module12", None)
        self.__atlstatic_ATL_Module12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModuleElement"):
                    opp_val = getattr(item, "ModuleElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ModuleElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModuleElement"):
                    opp_val = getattr(item, "ModuleElement", None)
                    
                    setattr(item, "ModuleElement", self)
                    

    @property
    def atlstatic_ATL_Module(self):
        return self.__atlstatic_ATL_Module

    @atlstatic_ATL_Module.setter
    def atlstatic_ATL_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Module__atlstatic_ATL_Module", None)
        self.__atlstatic_ATL_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel"):
                    opp_val = getattr(item, "OclModel", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel"):
                    opp_val = getattr(item, "OclModel", None)
                    
                    setattr(item, "OclModel", self)
                    

    @property
    def atlstatic_ATL_Module9(self):
        return self.__atlstatic_ATL_Module9

    @atlstatic_ATL_Module9.setter
    def atlstatic_ATL_Module9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Module__atlstatic_ATL_Module9", None)
        self.__atlstatic_ATL_Module9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel10"):
                    opp_val = getattr(item, "OclModel10", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel10"):
                    opp_val = getattr(item, "OclModel10", None)
                    
                    setattr(item, "OclModel10", self)
                    

class atlstatic_ATL_Query(Unit):

    pass
class atlstatic_ATL_Library(Unit):

    pass
class LibraryRef:

    pass
class LocatedElement:

    pass
class atlstatic_OCL_VariableDeclaration(LocatedElement):

    def __init__(self, id: str, varName: str, LetExp190: "LetExp" = None, IterateExp: "IterateExp" = None, VariableExp: set["VariableExp"] = None, OclType184: "OclType" = None, OclExpression187: "OclExpression" = None):
        self.id = id
        self.varName = varName
        self.LetExp190 = LetExp190
        self.IterateExp = IterateExp
        self.VariableExp = VariableExp if VariableExp is not None else set()
        self.OclType184 = OclType184
        self.OclExpression187 = OclExpression187
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def OclType184(self):
        return self.__OclType184

    @OclType184.setter
    def OclType184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__OclType184", None)
        self.__OclType184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL185"):
                opp_val = getattr(old_value, "OCL185", None)
                if opp_val == self:
                    setattr(old_value, "OCL185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL185"):
                opp_val = getattr(value, "OCL185", None)
                setattr(value, "OCL185", self)

    @property
    def IterateExp(self):
        return self.__IterateExp

    @IterateExp.setter
    def IterateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__IterateExp", None)
        self.__IterateExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL193"):
                opp_val = getattr(old_value, "OCL193", None)
                if opp_val == self:
                    setattr(old_value, "OCL193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL193"):
                opp_val = getattr(value, "OCL193", None)
                setattr(value, "OCL193", self)

    @property
    def VariableExp(self):
        return self.__VariableExp

    @VariableExp.setter
    def VariableExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__VariableExp", None)
        self.__VariableExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL195"):
                    opp_val = getattr(item, "OCL195", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL195"):
                    opp_val = getattr(item, "OCL195", None)
                    
                    setattr(item, "OCL195", self)
                    

    @property
    def LetExp190(self):
        return self.__LetExp190

    @LetExp190.setter
    def LetExp190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__LetExp190", None)
        self.__LetExp190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL191"):
                opp_val = getattr(old_value, "OCL191", None)
                if opp_val == self:
                    setattr(old_value, "OCL191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL191"):
                opp_val = getattr(value, "OCL191", None)
                setattr(value, "OCL191", self)

    @property
    def OclExpression187(self):
        return self.__OclExpression187

    @OclExpression187.setter
    def OclExpression187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__OclExpression187", None)
        self.__OclExpression187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL188"):
                opp_val = getattr(old_value, "OCL188", None)
                if opp_val == self:
                    setattr(old_value, "OCL188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL188"):
                opp_val = getattr(value, "OCL188", None)
                setattr(value, "OCL188", self)

class atlstatic_OCL_OclExpression(LocatedElement):

    pass
class atlstatic_ATL_ModuleElement(LocatedElement):

    pass
class atlstatic_ATL_DropPattern(LocatedElement):

    pass
class atlstatic_ATL_InPattern(LocatedElement):

    pass
class atlstatic_OCL_OclModel(LocatedElement):

    def __init__(self, name: str, OclModel271: "OclModel" = None, OclModelElement: set["OclModelElement"] = None, OclModel276: set["OclModel"] = None):
        self.name = name
        self.OclModel271 = OclModel271
        self.OclModelElement = OclModelElement if OclModelElement is not None else set()
        self.OclModel276 = OclModel276 if OclModel276 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclModelElement(self):
        return self.__OclModelElement

    @OclModelElement.setter
    def OclModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclModel__OclModelElement", None)
        self.__OclModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL274"):
                    opp_val = getattr(item, "OCL274", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL274"):
                    opp_val = getattr(item, "OCL274", None)
                    
                    setattr(item, "OCL274", self)
                    

    @property
    def OclModel276(self):
        return self.__OclModel276

    @OclModel276.setter
    def OclModel276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclModel__OclModel276", None)
        self.__OclModel276 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL277"):
                    opp_val = getattr(item, "OCL277", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL277"):
                    opp_val = getattr(item, "OCL277", None)
                    
                    setattr(item, "OCL277", self)
                    

    @property
    def OclModel271(self):
        return self.__OclModel271

    @OclModel271.setter
    def OclModel271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclModel__OclModel271", None)
        self.__OclModel271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL272"):
                opp_val = getattr(old_value, "OCL272", None)
                if opp_val == self:
                    setattr(old_value, "OCL272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL272"):
                opp_val = getattr(value, "OCL272", None)
                setattr(value, "OCL272", self)

class atlstatic_ATL_Statement(LocatedElement):

    pass
class atlstatic_ATL_ActionBlock(LocatedElement):

    pass
class atlstatic_ATL_LibraryRef(LocatedElement):

    def __init__(self, name: str, Unit: "Unit" = None):
        self.name = name
        self.Unit = Unit
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Unit(self):
        return self.__Unit

    @Unit.setter
    def Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_LibraryRef__Unit", None)
        self.__Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL81"):
                opp_val = getattr(old_value, "ATL81", None)
                if opp_val == self:
                    setattr(old_value, "ATL81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL81"):
                opp_val = getattr(value, "ATL81", None)
                setattr(value, "ATL81", self)

class atlstatic_OCL_OclContextDefinition(LocatedElement):

    pass
class atlstatic_OCL_MapElement(LocatedElement):

    pass
class atlstatic_ATL_Binding(LocatedElement):

    def __init__(self, propertyName: str, isAssignment: str, atlstatic_ATL_Binding: "OclExpression" = None, OutPatternElement75: "OutPatternElement" = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlstatic_ATL_Binding = atlstatic_ATL_Binding
        self.OutPatternElement75 = OutPatternElement75
        
    @property
    def isAssignment(self) -> str:
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment

    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def atlstatic_ATL_Binding(self):
        return self.__atlstatic_ATL_Binding

    @atlstatic_ATL_Binding.setter
    def atlstatic_ATL_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Binding__atlstatic_ATL_Binding", None)
        self.__atlstatic_ATL_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression73"):
                opp_val = getattr(old_value, "OclExpression73", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression73"):
                opp_val = getattr(value, "OclExpression73", None)
                setattr(value, "OclExpression73", self)

    @property
    def OutPatternElement75(self):
        return self.__OutPatternElement75

    @OutPatternElement75.setter
    def OutPatternElement75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Binding__OutPatternElement75", None)
        self.__OutPatternElement75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL76"):
                opp_val = getattr(old_value, "ATL76", None)
                if opp_val == self:
                    setattr(old_value, "ATL76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL76"):
                opp_val = getattr(value, "ATL76", None)
                setattr(value, "ATL76", self)

class atlstatic_OCL_OclFeatureDefinition(LocatedElement):

    pass
class atlstatic_OCL_OclFeature(LocatedElement):

    pass
class atlstatic_OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, OclType229: "OclType" = None, TupleType: "TupleType" = None):
        self.name = name
        self.OclType229 = OclType229
        self.TupleType = TupleType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclType229(self):
        return self.__OclType229

    @OclType229.setter
    def OclType229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_TupleTypeAttribute__OclType229", None)
        self.__OclType229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL230"):
                opp_val = getattr(old_value, "OCL230", None)
                if opp_val == self:
                    setattr(old_value, "OCL230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL230"):
                opp_val = getattr(value, "OCL230", None)
                setattr(value, "OCL230", self)

    @property
    def TupleType(self):
        return self.__TupleType

    @TupleType.setter
    def TupleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_TupleTypeAttribute__TupleType", None)
        self.__TupleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL232"):
                opp_val = getattr(old_value, "OCL232", None)
                if opp_val == self:
                    setattr(old_value, "OCL232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL232"):
                opp_val = getattr(value, "OCL232", None)
                setattr(value, "OCL232", self)

class atlstatic_ATL_OutPattern(LocatedElement):

    pass
class atlstatic_ATL_Unit(LocatedElement):

    def __init__(self, name: str, LibraryRef: set["LibraryRef"] = None):
        self.name = name
        self.LibraryRef = LibraryRef if LibraryRef is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LibraryRef(self):
        return self.__LibraryRef

    @LibraryRef.setter
    def LibraryRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Unit__LibraryRef", None)
        self.__LibraryRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL"):
                    opp_val = getattr(item, "ATL", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL"):
                    opp_val = getattr(item, "ATL", None)
                    
                    setattr(item, "ATL", self)
                    

class atlstatic_ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore
