from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclModelElement:

    pass
class OclFeature:

    pass
class Parameter:

    pass
class OCL_Operation(OclFeature):

    def __init__(self, name: str, 1209: set["Parameter"] = None, 1212: "OclType" = None, 1215: "OclExpression" = None, 189: "OCL_OclFeatureDefinition"):
        self.name = name
        self.1209 = 1209 if 1209 is not None else set()
        self.1212 = 1212
        self.1215 = 1215
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1212(self):
        return self.__1212

    @1212.setter
    def 1212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1212", None)
        self.__1212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "213"):
                opp_val = getattr(old_value, "213", None)
                if opp_val == self:
                    setattr(old_value, "213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "213"):
                opp_val = getattr(value, "213", None)
                setattr(value, "213", self)

    @property
    def 1215(self):
        return self.__1215

    @1215.setter
    def 1215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1215", None)
        self.__1215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "216"):
                opp_val = getattr(old_value, "216", None)
                if opp_val == self:
                    setattr(old_value, "216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "216"):
                opp_val = getattr(value, "216", None)
                setattr(value, "216", self)

    @property
    def 1209(self):
        return self.__1209

    @1209.setter
    def 1209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__1209", None)
        self.__1209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "210"):
                    opp_val = getattr(item, "210", None)
                    
                    if opp_val == self:
                        setattr(item, "210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "210"):
                    opp_val = getattr(item, "210", None)
                    
                    setattr(item, "210", self)
                    

class OCL_Attribute(OclFeature):

    def __init__(self, name: str, 1203: "OclExpression" = None, 1206: "OclType" = None, 189: "OCL_OclFeatureDefinition"):
        self.name = name
        self.1203 = 1203
        self.1206 = 1206
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1206(self):
        return self.__1206

    @1206.setter
    def 1206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__1206", None)
        self.__1206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "207"):
                opp_val = getattr(old_value, "207", None)
                if opp_val == self:
                    setattr(old_value, "207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "207"):
                opp_val = getattr(value, "207", None)
                setattr(value, "207", self)

    @property
    def 1203(self):
        return self.__1203

    @1203.setter
    def 1203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__1203", None)
        self.__1203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "204"):
                opp_val = getattr(old_value, "204", None)
                if opp_val == self:
                    setattr(old_value, "204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "204"):
                opp_val = getattr(value, "204", None)
                setattr(value, "204", self)

class OclFeatureDefinition:

    pass
class OclModel:

    pass
class TupleType:

    pass
class NumericType:

    pass
class OCL_RealType(NumericType):

    pass
class OCL_IntegerType(NumericType):

    pass
class Primitive:

    pass
class OCL_BooleanType(Primitive):

    pass
class OCL_NumericType(Primitive):

    pass
class OCL_StringType(Primitive):

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class OCL_SetType(CollectionType):

    pass
class OCL_SequenceType(CollectionType):

    pass
class OCL_OrderedSetType(CollectionType):

    pass
class OCL_BagType(CollectionType):

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class Iterator:

    pass
class TupleExp:

    pass
class MapExp:

    pass
class MapElement:

    pass
class Attribute:

    pass
class TuplePart:

    pass
class NumericExp:

    pass
class OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class OCL_RealExp(NumericExp):

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
class OCL_NumericExp(PrimitiveExp):

    pass
class OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class genericity_dsl_LocatedElement(ABC):

    def __init__(self, commentsBefore: str, commentsAfter: str, location: str):
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

class Operation:

    pass
class OperationCallExp:

    pass
class OCL_OperatorCallExp(OperationCallExp):

    pass
class OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class OCL_IterateExp(LoopExp):

    pass
class OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, 46: "OCL_OclExpression", 135: "OCL_Iterator"):
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
class OCL_BagExp(CollectionExp):

    pass
class OCL_SequenceExp(CollectionExp):

    pass
class OCL_SetExp(CollectionExp):

    pass
class OCL_OrderedSetExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, 37: "OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, 192: set["OclExpression"] = None, 37: "OCL_OclExpression"):
        self.operationName = operationName
        self.192 = 192 if 192 is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def 192(self):
        return self.__192

    @192.setter
    def 192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OperationCallExp__192", None)
        self.__192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "93"):
                    opp_val = getattr(item, "93", None)
                    
                    if opp_val == self:
                        setattr(item, "93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "93"):
                    opp_val = getattr(item, "93", None)
                    
                    setattr(item, "93", self)
                    

class OCL_LoopExp(PropertyCallExp):

    pass
class IfExp:

    pass
class BindingModel:

    pass
class OclType:

    pass
class OCL_TupleType(OclType):

    pass
class OCL_MapType(OclType):

    pass
class OCL_OclAnyType(OclType):

    pass
class OCL_CollectionType(OclType):

    pass
class OCL_Primitive(OclType):

    pass
class OCL_OclModelElement(OclType):

    pass
class BaseFeatureBinding:

    pass
class genericity_dsl_OclFeatureBinding(BaseFeatureBinding):

    pass
class genericity_dsl_RenamingFeatureBinding(BaseFeatureBinding):

    def __init__(self, concreteFeature: str):
        self.concreteFeature = concreteFeature
        
    @property
    def concreteFeature(self) -> str:
        return self.__concreteFeature

    @concreteFeature.setter
    def concreteFeature(self, concreteFeature: str):
        self.__concreteFeature = concreteFeature

class OclExpression:

    pass
class OCL_LetExp(OclExpression):

    pass
class OCL_IfExp(OclExpression):

    pass
class OCL_SuperExp(OclExpression):

    pass
class OCL_PropertyCallExp(OclExpression):

    pass
class OCL_MapExp(OclExpression):

    pass
class OCL_OclType(OclExpression):

    def __init__(self, name: str, 1143: "OclContextDefinition" = None, 1146: "OclExpression" = None, 1149: "Operation" = None, 1152: "MapType" = None, 1155: "Attribute" = None, 1158: "MapType" = None, 1161: "CollectionType" = None, 1164: "TupleTypeAttribute" = None, 1167: "VariableDeclaration" = None, 108: "OCL_LetExp", OclExpression: "genericity_dsl_ClassBinding", 111: "OCL_IfExp", 70: "OCL_CollectionExp", 123: "OCL_VariableDeclaration", 93: "OCL_OperationCallExp", 114: "OCL_IfExp", 117: "OCL_IfExp", 96: "OCL_LoopExp", 204: "OCL_Attribute", OclExpression84: "OCL_MapElement", OclExpression87: "OCL_MapElement", 147: "OCL_OclType", OclExpression24: "genericity_dsl_BHelper", 216: "OCL_Operation", 90: "OCL_PropertyCallExp", OclExpression19: "genericity_dsl_OclFeatureBinding"):
        self.name = name
        self.1143 = 1143
        self.1146 = 1146
        self.1149 = 1149
        self.1152 = 1152
        self.1155 = 1155
        self.1158 = 1158
        self.1161 = 1161
        self.1164 = 1164
        self.1167 = 1167
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1155(self):
        return self.__1155

    @1155.setter
    def 1155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1155", None)
        self.__1155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "156"):
                opp_val = getattr(old_value, "156", None)
                if opp_val == self:
                    setattr(old_value, "156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "156"):
                opp_val = getattr(value, "156", None)
                setattr(value, "156", self)

    @property
    def 1164(self):
        return self.__1164

    @1164.setter
    def 1164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1164", None)
        self.__1164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "165"):
                opp_val = getattr(old_value, "165", None)
                if opp_val == self:
                    setattr(old_value, "165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "165"):
                opp_val = getattr(value, "165", None)
                setattr(value, "165", self)

    @property
    def 1143(self):
        return self.__1143

    @1143.setter
    def 1143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1143", None)
        self.__1143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "144"):
                opp_val = getattr(old_value, "144", None)
                if opp_val == self:
                    setattr(old_value, "144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "144"):
                opp_val = getattr(value, "144", None)
                setattr(value, "144", self)

    @property
    def 1167(self):
        return self.__1167

    @1167.setter
    def 1167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1167", None)
        self.__1167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "168"):
                opp_val = getattr(old_value, "168", None)
                if opp_val == self:
                    setattr(old_value, "168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "168"):
                opp_val = getattr(value, "168", None)
                setattr(value, "168", self)

    @property
    def 1152(self):
        return self.__1152

    @1152.setter
    def 1152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1152", None)
        self.__1152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "153"):
                opp_val = getattr(old_value, "153", None)
                if opp_val == self:
                    setattr(old_value, "153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "153"):
                opp_val = getattr(value, "153", None)
                setattr(value, "153", self)

    @property
    def 1158(self):
        return self.__1158

    @1158.setter
    def 1158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1158", None)
        self.__1158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "159"):
                opp_val = getattr(old_value, "159", None)
                if opp_val == self:
                    setattr(old_value, "159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "159"):
                opp_val = getattr(value, "159", None)
                setattr(value, "159", self)

    @property
    def 1161(self):
        return self.__1161

    @1161.setter
    def 1161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1161", None)
        self.__1161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "162"):
                opp_val = getattr(old_value, "162", None)
                if opp_val == self:
                    setattr(old_value, "162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "162"):
                opp_val = getattr(value, "162", None)
                setattr(value, "162", self)

    @property
    def 1146(self):
        return self.__1146

    @1146.setter
    def 1146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1146", None)
        self.__1146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "147"):
                opp_val = getattr(old_value, "147", None)
                if opp_val == self:
                    setattr(old_value, "147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "147"):
                opp_val = getattr(value, "147", None)
                setattr(value, "147", self)

    @property
    def 1149(self):
        return self.__1149

    @1149.setter
    def 1149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__1149", None)
        self.__1149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "150"):
                opp_val = getattr(old_value, "150", None)
                if opp_val == self:
                    setattr(old_value, "150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "150"):
                opp_val = getattr(value, "150", None)
                setattr(value, "150", self)

class OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, 108: "OCL_LetExp", OclExpression: "genericity_dsl_ClassBinding", 111: "OCL_IfExp", 70: "OCL_CollectionExp", 123: "OCL_VariableDeclaration", 93: "OCL_OperationCallExp", 114: "OCL_IfExp", 117: "OCL_IfExp", 96: "OCL_LoopExp", 204: "OCL_Attribute", OclExpression84: "OCL_MapElement", OclExpression87: "OCL_MapElement", 147: "OCL_OclType", OclExpression24: "genericity_dsl_BHelper", 216: "OCL_Operation", 90: "OCL_PropertyCallExp", OclExpression19: "genericity_dsl_OclFeatureBinding"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCL_TupleExp(OclExpression):

    pass
class OCL_CollectionExp(OclExpression):

    pass
class OCL_PrimitiveExp(OclExpression):

    pass
class OCL_VariableExp(OclExpression):

    pass
class OCL_OclUndefinedExp(OclExpression):

    pass
class ConcreteMetaclass:

    pass
class ConceptMetaclass:

    pass
class Metaclass:

    pass
class genericity_dsl_ConcreteMetaclass(Metaclass):

    pass
class genericity_dsl_ConceptMetaclass(Metaclass):

    pass
class VariableDeclaration:

    pass
class OCL_TuplePart(VariableDeclaration):

    pass
class OCL_Iterator(VariableDeclaration):

    pass
class OCL_Parameter(VariableDeclaration):

    pass
class BHelper:

    pass
class ConceptBinding:

    pass
class genericity_dsl_BaseFeatureBinding(ConceptBinding):

    def __init__(self, conceptFeature: str, genericity_dsl_BaseFeatureBinding: "ConceptMetaclass" = None, genericity_dsl_BaseFeatureBinding16: "ConcreteMetaclass" = None, : "genericity_dsl_BindingModel"):
        self.conceptFeature = conceptFeature
        self.genericity_dsl_BaseFeatureBinding = genericity_dsl_BaseFeatureBinding
        self.genericity_dsl_BaseFeatureBinding16 = genericity_dsl_BaseFeatureBinding16
        
    @property
    def conceptFeature(self) -> str:
        return self.__conceptFeature

    @conceptFeature.setter
    def conceptFeature(self, conceptFeature: str):
        self.__conceptFeature = conceptFeature

    @property
    def genericity_dsl_BaseFeatureBinding(self):
        return self.__genericity_dsl_BaseFeatureBinding

    @genericity_dsl_BaseFeatureBinding.setter
    def genericity_dsl_BaseFeatureBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BaseFeatureBinding__genericity_dsl_BaseFeatureBinding", None)
        self.__genericity_dsl_BaseFeatureBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass14"):
                opp_val = getattr(old_value, "ConceptMetaclass14", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass14"):
                opp_val = getattr(value, "ConceptMetaclass14", None)
                setattr(value, "ConceptMetaclass14", self)

    @property
    def genericity_dsl_BaseFeatureBinding16(self):
        return self.__genericity_dsl_BaseFeatureBinding16

    @genericity_dsl_BaseFeatureBinding16.setter
    def genericity_dsl_BaseFeatureBinding16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BaseFeatureBinding__genericity_dsl_BaseFeatureBinding16", None)
        self.__genericity_dsl_BaseFeatureBinding16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConcreteMetaclass17"):
                opp_val = getattr(old_value, "ConcreteMetaclass17", None)
                if opp_val == self:
                    setattr(old_value, "ConcreteMetaclass17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConcreteMetaclass17"):
                opp_val = getattr(value, "ConcreteMetaclass17", None)
                setattr(value, "ConcreteMetaclass17", self)

class genericity_dsl_ClassBinding(ConceptBinding):

    pass
class LocatedElement:

    pass
class OCL_OclContextDefinition(LocatedElement):

    pass
class OCL_OclExpression(LocatedElement):

    pass
class OCL_OclModel(LocatedElement):

    def __init__(self, name: str, 1221: set["OclModelElement"] = None, 1224: set["OclModel"] = None, 1218: "OclModel" = None):
        self.name = name
        self.1221 = 1221 if 1221 is not None else set()
        self.1224 = 1224 if 1224 is not None else set()
        self.1218 = 1218
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1221(self):
        return self.__1221

    @1221.setter
    def 1221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1221", None)
        self.__1221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "222"):
                    opp_val = getattr(item, "222", None)
                    
                    if opp_val == self:
                        setattr(item, "222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "222"):
                    opp_val = getattr(item, "222", None)
                    
                    setattr(item, "222", self)
                    

    @property
    def 1224(self):
        return self.__1224

    @1224.setter
    def 1224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1224", None)
        self.__1224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "225"):
                    opp_val = getattr(item, "225", None)
                    
                    if opp_val == self:
                        setattr(item, "225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "225"):
                    opp_val = getattr(item, "225", None)
                    
                    setattr(item, "225", self)
                    

    @property
    def 1218(self):
        return self.__1218

    @1218.setter
    def 1218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__1218", None)
        self.__1218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "219"):
                opp_val = getattr(old_value, "219", None)
                if opp_val == self:
                    setattr(old_value, "219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "219"):
                opp_val = getattr(value, "219", None)
                setattr(value, "219", self)

class OCL_MapElement(LocatedElement):

    pass
class OCL_OclFeatureDefinition(LocatedElement):

    pass
class genericity_dsl_ConceptBinding(LocatedElement):

    def __init__(self, debugName: str, 06: "BindingModel" = None):
        self.debugName = debugName
        self.06 = 06
        
    @property
    def debugName(self) -> str:
        return self.__debugName

    @debugName.setter
    def debugName(self, debugName: str):
        self.__debugName = debugName

    @property
    def 06(self):
        return self.__06

    @06.setter
    def 06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_ConceptBinding__06", None)
        self.__06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "7"):
                opp_val = getattr(old_value, "7", None)
                if opp_val == self:
                    setattr(old_value, "7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "7"):
                opp_val = getattr(value, "7", None)
                setattr(value, "7", self)

class OCL_VariableDeclaration(LocatedElement):

    def __init__(self, id: str, varName: str, 1119: "OclType" = None, 1122: "OclExpression" = None, 1125: "LetExp" = None, 1131: set["VariableExp"] = None, 1128: "IterateExp" = None):
        self.id = id
        self.varName = varName
        self.1119 = 1119
        self.1122 = 1122
        self.1125 = 1125
        self.1131 = 1131 if 1131 is not None else set()
        self.1128 = 1128
        
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
    def 1128(self):
        return self.__1128

    @1128.setter
    def 1128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1128", None)
        self.__1128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "129"):
                opp_val = getattr(old_value, "129", None)
                if opp_val == self:
                    setattr(old_value, "129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "129"):
                opp_val = getattr(value, "129", None)
                setattr(value, "129", self)

    @property
    def 1122(self):
        return self.__1122

    @1122.setter
    def 1122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1122", None)
        self.__1122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "123"):
                opp_val = getattr(old_value, "123", None)
                if opp_val == self:
                    setattr(old_value, "123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "123"):
                opp_val = getattr(value, "123", None)
                setattr(value, "123", self)

    @property
    def 1125(self):
        return self.__1125

    @1125.setter
    def 1125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1125", None)
        self.__1125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "126"):
                opp_val = getattr(old_value, "126", None)
                if opp_val == self:
                    setattr(old_value, "126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "126"):
                opp_val = getattr(value, "126", None)
                setattr(value, "126", self)

    @property
    def 1131(self):
        return self.__1131

    @1131.setter
    def 1131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1131", None)
        self.__1131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "132"):
                    opp_val = getattr(item, "132", None)
                    
                    if opp_val == self:
                        setattr(item, "132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "132"):
                    opp_val = getattr(item, "132", None)
                    
                    setattr(item, "132", self)
                    

    @property
    def 1119(self):
        return self.__1119

    @1119.setter
    def 1119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__1119", None)
        self.__1119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "120"):
                opp_val = getattr(old_value, "120", None)
                if opp_val == self:
                    setattr(old_value, "120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "120"):
                opp_val = getattr(value, "120", None)
                setattr(value, "120", self)

class OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, 1173: "OclType" = None, 1176: "TupleType" = None):
        self.name = name
        self.1173 = 1173
        self.1176 = 1176
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 1176(self):
        return self.__1176

    @1176.setter
    def 1176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__1176", None)
        self.__1176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "177"):
                opp_val = getattr(old_value, "177", None)
                if opp_val == self:
                    setattr(old_value, "177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "177"):
                opp_val = getattr(value, "177", None)
                setattr(value, "177", self)

    @property
    def 1173(self):
        return self.__1173

    @1173.setter
    def 1173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__1173", None)
        self.__1173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "174"):
                opp_val = getattr(old_value, "174", None)
                if opp_val == self:
                    setattr(old_value, "174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "174"):
                opp_val = getattr(value, "174", None)
                setattr(value, "174", self)

class genericity_dsl_BHelper(LocatedElement):

    def __init__(self, feature: str, genericity_dsl_BHelper: "ConceptMetaclass" = None, genericity_dsl_BHelper23: "OclExpression" = None, genericity_dsl_BHelper26: "OclType" = None, 028: "BindingModel" = None):
        self.feature = feature
        self.genericity_dsl_BHelper = genericity_dsl_BHelper
        self.genericity_dsl_BHelper23 = genericity_dsl_BHelper23
        self.genericity_dsl_BHelper26 = genericity_dsl_BHelper26
        self.028 = 028
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

    @property
    def 028(self):
        return self.__028

    @028.setter
    def 028(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BHelper__028", None)
        self.__028 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "29"):
                opp_val = getattr(old_value, "29", None)
                if opp_val == self:
                    setattr(old_value, "29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "29"):
                opp_val = getattr(value, "29", None)
                setattr(value, "29", self)

    @property
    def genericity_dsl_BHelper23(self):
        return self.__genericity_dsl_BHelper23

    @genericity_dsl_BHelper23.setter
    def genericity_dsl_BHelper23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BHelper__genericity_dsl_BHelper23", None)
        self.__genericity_dsl_BHelper23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression24"):
                opp_val = getattr(old_value, "OclExpression24", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression24"):
                opp_val = getattr(value, "OclExpression24", None)
                setattr(value, "OclExpression24", self)

    @property
    def genericity_dsl_BHelper26(self):
        return self.__genericity_dsl_BHelper26

    @genericity_dsl_BHelper26.setter
    def genericity_dsl_BHelper26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BHelper__genericity_dsl_BHelper26", None)
        self.__genericity_dsl_BHelper26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType"):
                opp_val = getattr(old_value, "OclType", None)
                if opp_val == self:
                    setattr(old_value, "OclType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType"):
                opp_val = getattr(value, "OclType", None)
                setattr(value, "OclType", self)

    @property
    def genericity_dsl_BHelper(self):
        return self.__genericity_dsl_BHelper

    @genericity_dsl_BHelper.setter
    def genericity_dsl_BHelper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BHelper__genericity_dsl_BHelper", None)
        self.__genericity_dsl_BHelper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass21"):
                opp_val = getattr(old_value, "ConceptMetaclass21", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass21"):
                opp_val = getattr(value, "ConceptMetaclass21", None)
                setattr(value, "ConceptMetaclass21", self)

class genericity_dsl_Metaclass(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCL_OclFeature(LocatedElement):

    pass
class genericity_dsl_BindingModel(LocatedElement):

    def __init__(self, metamodel: str, name: str, 0: set["ConceptBinding"] = None, 02: set["BHelper"] = None, genericity_dsl_BindingModel: set["VariableDeclaration"] = None):
        self.metamodel = metamodel
        self.name = name
        self.0 = 0 if 0 is not None else set()
        self.02 = 02 if 02 is not None else set()
        self.genericity_dsl_BindingModel = genericity_dsl_BindingModel if genericity_dsl_BindingModel is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel(self) -> str:
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BindingModel__0", None)
        self.__0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, ""):
                    opp_val = getattr(item, "", None)
                    
                    if opp_val == self:
                        setattr(item, "", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, ""):
                    opp_val = getattr(item, "", None)
                    
                    setattr(item, "", self)
                    

    @property
    def genericity_dsl_BindingModel(self):
        return self.__genericity_dsl_BindingModel

    @genericity_dsl_BindingModel.setter
    def genericity_dsl_BindingModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BindingModel__genericity_dsl_BindingModel", None)
        self.__genericity_dsl_BindingModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableDeclaration"):
                    opp_val = getattr(item, "VariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableDeclaration"):
                    opp_val = getattr(item, "VariableDeclaration", None)
                    
                    setattr(item, "VariableDeclaration", self)
                    

    @property
    def 02(self):
        return self.__02

    @02.setter
    def 02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_genericity_dsl_BindingModel__02", None)
        self.__02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "3"):
                    opp_val = getattr(item, "3", None)
                    
                    if opp_val == self:
                        setattr(item, "3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "3"):
                    opp_val = getattr(item, "3", None)
                    
                    setattr(item, "3", self)
                    
