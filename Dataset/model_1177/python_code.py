from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclInstanceModel:

    pass
class OclModelElement:

    pass
class OclFeatureDefinition:

    pass
class OclFeature:

    pass
class QualityMetamodel_QMM_OCL_Attribute(OclFeature):

    pass
class Parameter:

    pass
class QualityMetamodel_QMM_OCL_Operation(OclFeature):

    pass
class TupleType:

    pass
class NumericType:

    pass
class QualityMetamodel_QMM_OCL_RealType(NumericType):

    pass
class QualityMetamodel_QMM_OCL_IntegerType(NumericType):

    pass
class OclModel:

    pass
class QualityMetamodel_QMM_OCL_OclMetamodel(OclModel):

    def __init__(self, uri: str, OclInstanceModel: set["OclInstanceModel"] = None, QMM_OCL204: "QualityMetamodel_QMM_OCL_OclModelElement", OclModel: "QualityMetamodel_QMM_OCL_OclModelElementExp"):
        self.uri = uri
        self.OclInstanceModel = OclInstanceModel if OclInstanceModel is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def OclInstanceModel(self):
        return self.__OclInstanceModel

    @OclInstanceModel.setter
    def OclInstanceModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclMetamodel__OclInstanceModel", None)
        self.__OclInstanceModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QMM_OCL247"):
                    opp_val = getattr(item, "QMM_OCL247", None)
                    
                    if opp_val == self:
                        setattr(item, "QMM_OCL247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QMM_OCL247"):
                    opp_val = getattr(item, "QMM_OCL247", None)
                    
                    setattr(item, "QMM_OCL247", self)
                    

class QualityMetamodel_QMM_OCL_OclInstanceModel(OclModel):

    pass
class LambdaType:

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class QualityMetamodel_QMM_OCL_SequenceType(CollectionType):

    pass
class QualityMetamodel_QMM_OCL_OrderedSetType(CollectionType):

    pass
class QualityMetamodel_QMM_OCL_SetType(CollectionType):

    pass
class QualityMetamodel_QMM_OCL_BagType(CollectionType):

    pass
class MapType:

    pass
class Primitive:

    pass
class QualityMetamodel_QMM_OCL_BooleanType(Primitive):

    pass
class QualityMetamodel_QMM_OCL_NumericType(Primitive):

    pass
class QualityMetamodel_QMM_OCL_StringType(Primitive):

    pass
class IterateExp:

    pass
class OclContextDefinition:

    pass
class Iterator:

    pass
class VariableExp:

    pass
class QualityMetamodel_QMM_OCL_LambdaCallExp(VariableExp):

    pass
class PropertyCall:

    pass
class QualityMetamodel_QMM_OCL_LoopExp(PropertyCall):

    pass
class QualityMetamodel_QMM_OCL_NavigationOrAttributeCall(PropertyCall):

    def __init__(self, name: str, QMM_OCL98: "QualityMetamodel_QMM_OCL_PropertyCallExp"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class QualityMetamodel_QMM_OCL_OperationCall(PropertyCall):

    def __init__(self, operationName: str, OclExpression106: set["OclExpression"] = None, QMM_OCL98: "QualityMetamodel_QMM_OCL_PropertyCallExp"):
        self.operationName = operationName
        self.OclExpression106 = OclExpression106 if OclExpression106 is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def OclExpression106(self):
        return self.__OclExpression106

    @OclExpression106.setter
    def OclExpression106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OperationCall__OclExpression106", None)
        self.__OclExpression106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QMM_OCL107"):
                    opp_val = getattr(item, "QMM_OCL107", None)
                    
                    if opp_val == self:
                        setattr(item, "QMM_OCL107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QMM_OCL107"):
                    opp_val = getattr(item, "QMM_OCL107", None)
                    
                    setattr(item, "QMM_OCL107", self)
                    

class StaticPropertyCallExp:

    pass
class StaticPropertyCall:

    pass
class QualityMetamodel_QMM_OCL_StaticNavigationOrAttributeCall(StaticPropertyCall):

    def __init__(self, name: str, QMM_OCL92: "QualityMetamodel_QMM_OCL_StaticPropertyCallExp"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class MapExp:

    pass
class MapElement:

    pass
class QualityMetamodel_QMM_OCL_StaticOperationCall(StaticPropertyCall):

    def __init__(self, operationName: str, QualityMetamodel_QMM_OCL_StaticOperationCall: set["OclExpression"] = None, QMM_OCL92: "QualityMetamodel_QMM_OCL_StaticPropertyCallExp"):
        self.operationName = operationName
        self.QualityMetamodel_QMM_OCL_StaticOperationCall = QualityMetamodel_QMM_OCL_StaticOperationCall if QualityMetamodel_QMM_OCL_StaticOperationCall is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def QualityMetamodel_QMM_OCL_StaticOperationCall(self):
        return self.__QualityMetamodel_QMM_OCL_StaticOperationCall

    @QualityMetamodel_QMM_OCL_StaticOperationCall.setter
    def QualityMetamodel_QMM_OCL_StaticOperationCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_StaticOperationCall__QualityMetamodel_QMM_OCL_StaticOperationCall", None)
        self.__QualityMetamodel_QMM_OCL_StaticOperationCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression96"):
                    opp_val = getattr(item, "OclExpression96", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression96"):
                    opp_val = getattr(item, "OclExpression96", None)
                    
                    setattr(item, "OclExpression96", self)
                    

class CollectionExp:

    pass
class QualityMetamodel_QMM_OCL_OrderedSetExp(CollectionExp):

    pass
class QualityMetamodel_QMM_OCL_BagExp(CollectionExp):

    pass
class QualityMetamodel_QMM_OCL_SequenceExp(CollectionExp):

    pass
class QualityMetamodel_QMM_OCL_SetExp(CollectionExp):

    pass
class CollectionPart:

    pass
class QualityMetamodel_QMM_OCL_CollectionRange(CollectionPart):

    pass
class QualityMetamodel_QMM_OCL_CollectionItem(CollectionPart):

    pass
class NumericExp:

    pass
class QualityMetamodel_QMM_OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class QualityMetamodel_QMM_OCL_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class TupleExp:

    pass
class TuplePart:

    pass
class OperatorCallExp:

    pass
class QualityMetamodel_QMM_OCL_MulOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_EqOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_NotOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_AddOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_IntOpCallExp(OperatorCallExp):

    pass
class QualityMetamodel_QMM_OCL_RelOpCallExp(OperatorCallExp):

    pass
class Attribute:

    pass
class Operation:

    pass
class LocalVariable:

    pass
class QualityMetamodel_QMM_OCL_TuplePart(LocalVariable):

    pass
class OperationCall:

    pass
class QualityMetamodel_QMM_OCL_CollectionOperationCall(OperationCall):

    pass
class LoopExp:

    pass
class QualityMetamodel_QMM_OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, QMM_OCL155: "QualityMetamodel_QMM_OCL_Iterator", QMM_OCL45: "QualityMetamodel_QMM_OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class QualityMetamodel_QMM_OCL_IterateExp(LoopExp):

    pass
class LetExp:

    pass
class PrimitiveExp:

    pass
class QualityMetamodel_QMM_OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class QualityMetamodel_QMM_OCL_NumericExp(PrimitiveExp):

    pass
class QualityMetamodel_QMM_OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class ModuleElement:

    pass
class QualityMetamodel_QMM_OCL_OclFeatureDefinition(ModuleElement):

    def __init__(self, static: str, OclFeature: "OclFeature" = None, OclContextDefinition220: "OclContextDefinition" = None, QMM_OCL30: "QualityMetamodel_QMM_OCL_Module"):
        self.static = static
        self.OclFeature = OclFeature
        self.OclContextDefinition220 = OclContextDefinition220
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def OclContextDefinition220(self):
        return self.__OclContextDefinition220

    @OclContextDefinition220.setter
    def OclContextDefinition220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclFeatureDefinition__OclContextDefinition220", None)
        self.__OclContextDefinition220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL221"):
                opp_val = getattr(old_value, "QMM_OCL221", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL221"):
                opp_val = getattr(value, "QMM_OCL221", None)
                setattr(value, "QMM_OCL221", self)

    @property
    def OclFeature(self):
        return self.__OclFeature

    @OclFeature.setter
    def OclFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclFeatureDefinition__OclFeature", None)
        self.__OclFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL218"):
                opp_val = getattr(old_value, "QMM_OCL218", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL218"):
                opp_val = getattr(value, "QMM_OCL218", None)
                setattr(value, "QMM_OCL218", self)

class Import:

    pass
class OclMetamodel:

    pass
class NamedElement:

    pass
class QualityMetamodel_QMM_OCL_OclModel(NamedElement):

    pass
class QualityMetamodel_QMM_OCL_OclFeature(NamedElement):

    def __init__(self, eq: str, OclFeatureDefinition228: "OclFeatureDefinition" = None):
        self.eq = eq
        self.OclFeatureDefinition228 = OclFeatureDefinition228
        
    @property
    def eq(self) -> str:
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq

    @property
    def OclFeatureDefinition228(self):
        return self.__OclFeatureDefinition228

    @OclFeatureDefinition228.setter
    def OclFeatureDefinition228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclFeature__OclFeatureDefinition228", None)
        self.__OclFeatureDefinition228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL229"):
                opp_val = getattr(old_value, "QMM_OCL229", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL229"):
                opp_val = getattr(value, "QMM_OCL229", None)
                setattr(value, "QMM_OCL229", self)

class QualityMetamodel_QMM_OCL_Import(NamedElement):

    pass
class QualityMetamodel_QMM_OCL_Module(NamedElement):

    pass
class LocatedElement:

    pass
class QualityMetamodel_QMM_OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, OclType198: "OclType" = None, TupleType: "TupleType" = None):
        self.name = name
        self.OclType198 = OclType198
        self.TupleType = TupleType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TupleType(self):
        return self.__TupleType

    @TupleType.setter
    def TupleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_TupleTypeAttribute__TupleType", None)
        self.__TupleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL201"):
                opp_val = getattr(old_value, "QMM_OCL201", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL201"):
                opp_val = getattr(value, "QMM_OCL201", None)
                setattr(value, "QMM_OCL201", self)

    @property
    def OclType198(self):
        return self.__OclType198

    @OclType198.setter
    def OclType198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_TupleTypeAttribute__OclType198", None)
        self.__OclType198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL199"):
                opp_val = getattr(old_value, "QMM_OCL199", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL199"):
                opp_val = getattr(value, "QMM_OCL199", None)
                setattr(value, "QMM_OCL199", self)

class QualityMetamodel_QMM_OCL_OclType(LocatedElement):

    def __init__(self, name: str, OclContextDefinition: "OclContextDefinition" = None, OclExpression165: "OclExpression" = None, Operation168: "Operation" = None, MapType: "MapType" = None, Attribute173: "Attribute" = None, MapType176: "MapType" = None, CollectionType: "CollectionType" = None, TupleTypeAttribute: "TupleTypeAttribute" = None, VariableDeclaration183: "VariableDeclaration" = None, LambdaType: "LambdaType" = None, LambdaType188: "LambdaType" = None, StaticPropertyCallExp191: "StaticPropertyCallExp" = None):
        self.name = name
        self.OclContextDefinition = OclContextDefinition
        self.OclExpression165 = OclExpression165
        self.Operation168 = Operation168
        self.MapType = MapType
        self.Attribute173 = Attribute173
        self.MapType176 = MapType176
        self.CollectionType = CollectionType
        self.TupleTypeAttribute = TupleTypeAttribute
        self.VariableDeclaration183 = VariableDeclaration183
        self.LambdaType = LambdaType
        self.LambdaType188 = LambdaType188
        self.StaticPropertyCallExp191 = StaticPropertyCallExp191
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def VariableDeclaration183(self):
        return self.__VariableDeclaration183

    @VariableDeclaration183.setter
    def VariableDeclaration183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__VariableDeclaration183", None)
        self.__VariableDeclaration183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL184"):
                opp_val = getattr(old_value, "QMM_OCL184", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL184"):
                opp_val = getattr(value, "QMM_OCL184", None)
                setattr(value, "QMM_OCL184", self)

    @property
    def OclContextDefinition(self):
        return self.__OclContextDefinition

    @OclContextDefinition.setter
    def OclContextDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__OclContextDefinition", None)
        self.__OclContextDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL163"):
                opp_val = getattr(old_value, "QMM_OCL163", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL163"):
                opp_val = getattr(value, "QMM_OCL163", None)
                setattr(value, "QMM_OCL163", self)

    @property
    def MapType176(self):
        return self.__MapType176

    @MapType176.setter
    def MapType176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__MapType176", None)
        self.__MapType176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL177"):
                opp_val = getattr(old_value, "QMM_OCL177", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL177"):
                opp_val = getattr(value, "QMM_OCL177", None)
                setattr(value, "QMM_OCL177", self)

    @property
    def TupleTypeAttribute(self):
        return self.__TupleTypeAttribute

    @TupleTypeAttribute.setter
    def TupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__TupleTypeAttribute", None)
        self.__TupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL181"):
                opp_val = getattr(old_value, "QMM_OCL181", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL181"):
                opp_val = getattr(value, "QMM_OCL181", None)
                setattr(value, "QMM_OCL181", self)

    @property
    def LambdaType188(self):
        return self.__LambdaType188

    @LambdaType188.setter
    def LambdaType188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__LambdaType188", None)
        self.__LambdaType188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL189"):
                opp_val = getattr(old_value, "QMM_OCL189", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL189"):
                opp_val = getattr(value, "QMM_OCL189", None)
                setattr(value, "QMM_OCL189", self)

    @property
    def StaticPropertyCallExp191(self):
        return self.__StaticPropertyCallExp191

    @StaticPropertyCallExp191.setter
    def StaticPropertyCallExp191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__StaticPropertyCallExp191", None)
        self.__StaticPropertyCallExp191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL192"):
                opp_val = getattr(old_value, "QMM_OCL192", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL192"):
                opp_val = getattr(value, "QMM_OCL192", None)
                setattr(value, "QMM_OCL192", self)

    @property
    def MapType(self):
        return self.__MapType

    @MapType.setter
    def MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__MapType", None)
        self.__MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL171"):
                opp_val = getattr(old_value, "QMM_OCL171", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL171"):
                opp_val = getattr(value, "QMM_OCL171", None)
                setattr(value, "QMM_OCL171", self)

    @property
    def LambdaType(self):
        return self.__LambdaType

    @LambdaType.setter
    def LambdaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__LambdaType", None)
        self.__LambdaType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL186"):
                opp_val = getattr(old_value, "QMM_OCL186", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL186"):
                opp_val = getattr(value, "QMM_OCL186", None)
                setattr(value, "QMM_OCL186", self)

    @property
    def CollectionType(self):
        return self.__CollectionType

    @CollectionType.setter
    def CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__CollectionType", None)
        self.__CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL179"):
                opp_val = getattr(old_value, "QMM_OCL179", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL179"):
                opp_val = getattr(value, "QMM_OCL179", None)
                setattr(value, "QMM_OCL179", self)

    @property
    def Attribute173(self):
        return self.__Attribute173

    @Attribute173.setter
    def Attribute173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__Attribute173", None)
        self.__Attribute173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL174"):
                opp_val = getattr(old_value, "QMM_OCL174", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL174"):
                opp_val = getattr(value, "QMM_OCL174", None)
                setattr(value, "QMM_OCL174", self)

    @property
    def Operation168(self):
        return self.__Operation168

    @Operation168.setter
    def Operation168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__Operation168", None)
        self.__Operation168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL169"):
                opp_val = getattr(old_value, "QMM_OCL169", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL169"):
                opp_val = getattr(value, "QMM_OCL169", None)
                setattr(value, "QMM_OCL169", self)

    @property
    def OclExpression165(self):
        return self.__OclExpression165

    @OclExpression165.setter
    def OclExpression165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclType__OclExpression165", None)
        self.__OclExpression165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL166"):
                opp_val = getattr(old_value, "QMM_OCL166", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL166"):
                opp_val = getattr(value, "QMM_OCL166", None)
                setattr(value, "QMM_OCL166", self)

class QualityMetamodel_QMM_OCL_ModuleElement(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_OclExpression(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_MapElement(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_StaticPropertyCall(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_OclContextDefinition(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_VariableDeclaration(LocatedElement):

    def __init__(self, varName: str, OclType141: "OclType" = None, VariableExp: set["VariableExp"] = None):
        self.varName = varName
        self.OclType141 = OclType141
        self.VariableExp = VariableExp if VariableExp is not None else set()
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def OclType141(self):
        return self.__OclType141

    @OclType141.setter
    def OclType141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_VariableDeclaration__OclType141", None)
        self.__OclType141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL142"):
                opp_val = getattr(old_value, "QMM_OCL142", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL142"):
                opp_val = getattr(value, "QMM_OCL142", None)
                setattr(value, "QMM_OCL142", self)

    @property
    def VariableExp(self):
        return self.__VariableExp

    @VariableExp.setter
    def VariableExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_VariableDeclaration__VariableExp", None)
        self.__VariableExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QMM_OCL144"):
                    opp_val = getattr(item, "QMM_OCL144", None)
                    
                    if opp_val == self:
                        setattr(item, "QMM_OCL144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QMM_OCL144"):
                    opp_val = getattr(item, "QMM_OCL144", None)
                    
                    setattr(item, "QMM_OCL144", self)
                    

class QualityMetamodel_QMM_OCL_PropertyCall(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_CollectionPart(LocatedElement):

    pass
class QualityMetamodel_QMM_OCL_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class QualityMetamodel_QMM_OCL_LocatedElement(ABC):

    def __init__(self, line: str, column: str, charStart: str, charEnd: str):
        self.line = line
        self.column = column
        self.charStart = charStart
        self.charEnd = charEnd
        
    @property
    def line(self) -> str:
        return self.__line

    @line.setter
    def line(self, line: str):
        self.__line = line

    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column

    @property
    def charStart(self) -> str:
        return self.__charStart

    @charStart.setter
    def charStart(self, charStart: str):
        self.__charStart = charStart

    @property
    def charEnd(self) -> str:
        return self.__charEnd

    @charEnd.setter
    def charEnd(self, charEnd: str):
        self.__charEnd = charEnd

class PropertyCallExp:

    pass
class IfExp:

    pass
class OclType:

    pass
class QualityMetamodel_QMM_OCL_EnvType(OclType):

    pass
class QualityMetamodel_QMM_OCL_OclModelElement(OclType):

    pass
class QualityMetamodel_QMM_OCL_CollectionType(OclType):

    pass
class QualityMetamodel_QMM_OCL_OclAnyType(OclType):

    pass
class QualityMetamodel_QMM_OCL_MapType(OclType):

    pass
class QualityMetamodel_QMM_OCL_Primitive(OclType):

    pass
class QualityMetamodel_QMM_OCL_TupleType(OclType):

    pass
class QualityMetamodel_QMM_OCL_LambdaType(OclType):

    pass
class QualityMetamodel_EnumerationItem:

    def __init__(self, name: str, QualityMetamodel_EnumerationItem: "QualityMetamodel_EnumerationMetric" = None, QualityMetamodel_EnumerationItem26: "QualityMetamodel_EnumerationMetric" = None):
        self.name = name
        self.QualityMetamodel_EnumerationItem = QualityMetamodel_EnumerationItem
        self.QualityMetamodel_EnumerationItem26 = QualityMetamodel_EnumerationItem26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def QualityMetamodel_EnumerationItem26(self):
        return self.__QualityMetamodel_EnumerationItem26

    @QualityMetamodel_EnumerationItem26.setter
    def QualityMetamodel_EnumerationItem26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_EnumerationItem__QualityMetamodel_EnumerationItem26", None)
        self.__QualityMetamodel_EnumerationItem26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_EnumerationMetric25"):
                opp_val = getattr(old_value, "QualityMetamodel_EnumerationMetric25", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_EnumerationMetric25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_EnumerationMetric25"):
                opp_val = getattr(value, "QualityMetamodel_EnumerationMetric25", None)
                setattr(value, "QualityMetamodel_EnumerationMetric25", self)

    @property
    def QualityMetamodel_EnumerationItem(self):
        return self.__QualityMetamodel_EnumerationItem

    @QualityMetamodel_EnumerationItem.setter
    def QualityMetamodel_EnumerationItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_EnumerationItem__QualityMetamodel_EnumerationItem", None)
        self.__QualityMetamodel_EnumerationItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_EnumerationMetric"):
                opp_val = getattr(old_value, "QualityMetamodel_EnumerationMetric", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_EnumerationMetric"):
                opp_val = getattr(value, "QualityMetamodel_EnumerationMetric", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_EnumerationMetric", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ValueType:

    pass
class QualityMetamodel_AggregatedValueMetric(ValueType):

    def __init__(self, minimum: str, maximum: str, average: str, median: str, standardDeviation: str):
        self.minimum = minimum
        self.maximum = maximum
        self.average = average
        self.median = median
        self.standardDeviation = standardDeviation
        
    @property
    def minimum(self) -> str:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum

    @property
    def maximum(self) -> str:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum

    @property
    def median(self) -> str:
        return self.__median

    @median.setter
    def median(self, median: str):
        self.__median = median

    @property
    def average(self) -> str:
        return self.__average

    @average.setter
    def average(self, average: str):
        self.__average = average

    @property
    def standardDeviation(self) -> str:
        return self.__standardDeviation

    @standardDeviation.setter
    def standardDeviation(self, standardDeviation: str):
        self.__standardDeviation = standardDeviation

class QualityMetamodel_EnumerationMetric(ValueType):

    pass
class QualityMetamodel_RangeValueType(ValueType):

    def __init__(self, min: str, max: str):
        self.min = min
        self.max = max
        
    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

class QualityMetamodel_TextValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class OclExpression:

    pass
class QualityMetamodel_QMM_OCL_SelfExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_EnvExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_MapExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_OclModelElementExp(OclExpression):

    def __init__(self, name: str, QualityMetamodel_QMM_OCL_OclModelElementExp: "OclModel" = None, OclExpression74: "QualityMetamodel_QMM_OCL_CollectionItem", QMM_OCL139: "QualityMetamodel_QMM_OCL_IfExp", QMM_OCL119: "QualityMetamodel_QMM_OCL_LoopExp", QMM_OCL136: "QualityMetamodel_QMM_OCL_IfExp", QMM_OCL232: "QualityMetamodel_QMM_OCL_Attribute", OclExpression69: "QualityMetamodel_QMM_OCL_CollectionRange", OclExpression84: "QualityMetamodel_QMM_OCL_MapElement", QMM_OCL112: "QualityMetamodel_QMM_OCL_OperatorCallExp", QMM_OCL133: "QualityMetamodel_QMM_OCL_IfExp", OclExpression116: "QualityMetamodel_QMM_OCL_BraceExp", OclExpression114: "QualityMetamodel_QMM_OCL_LambdaCallExp", QMM_OCL166: "QualityMetamodel_QMM_OCL_OclType", QMM_OCL150: "QualityMetamodel_QMM_OCL_LocalVariable", OclExpression96: "QualityMetamodel_QMM_OCL_StaticOperationCall", QMM_OCL243: "QualityMetamodel_QMM_OCL_Operation", QMM_OCL107: "QualityMetamodel_QMM_OCL_OperationCall", QMM_OCL101: "QualityMetamodel_QMM_OCL_PropertyCallExp", OclExpression109: "QualityMetamodel_QMM_OCL_OperatorCallExp", OclExpression72: "QualityMetamodel_QMM_OCL_CollectionRange", OclExpression87: "QualityMetamodel_QMM_OCL_MapElement", QMM_OCL130: "QualityMetamodel_QMM_OCL_LetExp", OclExpression: "QualityMetamodel_Operation"):
        self.name = name
        self.QualityMetamodel_QMM_OCL_OclModelElementExp = QualityMetamodel_QMM_OCL_OclModelElementExp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def QualityMetamodel_QMM_OCL_OclModelElementExp(self):
        return self.__QualityMetamodel_QMM_OCL_OclModelElementExp

    @QualityMetamodel_QMM_OCL_OclModelElementExp.setter
    def QualityMetamodel_QMM_OCL_OclModelElementExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OclModelElementExp__QualityMetamodel_QMM_OCL_OclModelElementExp", None)
        self.__QualityMetamodel_QMM_OCL_OclModelElementExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclModel"):
                opp_val = getattr(old_value, "OclModel", None)
                if opp_val == self:
                    setattr(old_value, "OclModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel"):
                opp_val = getattr(value, "OclModel", None)
                setattr(value, "OclModel", self)

class QualityMetamodel_QMM_OCL_OperatorCallExp(OclExpression):

    def __init__(self, operationName: str, QualityMetamodel_QMM_OCL_OperatorCallExp: "OclExpression" = None, OclExpression111: "OclExpression" = None, OclExpression74: "QualityMetamodel_QMM_OCL_CollectionItem", QMM_OCL139: "QualityMetamodel_QMM_OCL_IfExp", QMM_OCL119: "QualityMetamodel_QMM_OCL_LoopExp", QMM_OCL136: "QualityMetamodel_QMM_OCL_IfExp", QMM_OCL232: "QualityMetamodel_QMM_OCL_Attribute", OclExpression69: "QualityMetamodel_QMM_OCL_CollectionRange", OclExpression84: "QualityMetamodel_QMM_OCL_MapElement", QMM_OCL112: "QualityMetamodel_QMM_OCL_OperatorCallExp", QMM_OCL133: "QualityMetamodel_QMM_OCL_IfExp", OclExpression116: "QualityMetamodel_QMM_OCL_BraceExp", OclExpression114: "QualityMetamodel_QMM_OCL_LambdaCallExp", QMM_OCL166: "QualityMetamodel_QMM_OCL_OclType", QMM_OCL150: "QualityMetamodel_QMM_OCL_LocalVariable", OclExpression96: "QualityMetamodel_QMM_OCL_StaticOperationCall", QMM_OCL243: "QualityMetamodel_QMM_OCL_Operation", QMM_OCL107: "QualityMetamodel_QMM_OCL_OperationCall", QMM_OCL101: "QualityMetamodel_QMM_OCL_PropertyCallExp", OclExpression109: "QualityMetamodel_QMM_OCL_OperatorCallExp", OclExpression72: "QualityMetamodel_QMM_OCL_CollectionRange", OclExpression87: "QualityMetamodel_QMM_OCL_MapElement", QMM_OCL130: "QualityMetamodel_QMM_OCL_LetExp", OclExpression: "QualityMetamodel_Operation"):
        self.operationName = operationName
        self.QualityMetamodel_QMM_OCL_OperatorCallExp = QualityMetamodel_QMM_OCL_OperatorCallExp
        self.OclExpression111 = OclExpression111
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def QualityMetamodel_QMM_OCL_OperatorCallExp(self):
        return self.__QualityMetamodel_QMM_OCL_OperatorCallExp

    @QualityMetamodel_QMM_OCL_OperatorCallExp.setter
    def QualityMetamodel_QMM_OCL_OperatorCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OperatorCallExp__QualityMetamodel_QMM_OCL_OperatorCallExp", None)
        self.__QualityMetamodel_QMM_OCL_OperatorCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression109"):
                opp_val = getattr(old_value, "OclExpression109", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression109"):
                opp_val = getattr(value, "OclExpression109", None)
                setattr(value, "OclExpression109", self)

    @property
    def OclExpression111(self):
        return self.__OclExpression111

    @OclExpression111.setter
    def OclExpression111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_OperatorCallExp__OclExpression111", None)
        self.__OclExpression111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL112"):
                opp_val = getattr(old_value, "QMM_OCL112", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL112"):
                opp_val = getattr(value, "QMM_OCL112", None)
                setattr(value, "QMM_OCL112", self)

class QualityMetamodel_QMM_OCL_OclUndefinedExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_TupleExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_IfExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_CollectionExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_StaticPropertyCallExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_SuperExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_VariableExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_PrimitiveExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_LetExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_PropertyCallExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_BraceExp(OclExpression):

    pass
class QualityMetamodel_QMM_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression74: "QualityMetamodel_QMM_OCL_CollectionItem", QMM_OCL139: "QualityMetamodel_QMM_OCL_IfExp", QMM_OCL119: "QualityMetamodel_QMM_OCL_LoopExp", QMM_OCL136: "QualityMetamodel_QMM_OCL_IfExp", QMM_OCL232: "QualityMetamodel_QMM_OCL_Attribute", OclExpression69: "QualityMetamodel_QMM_OCL_CollectionRange", OclExpression84: "QualityMetamodel_QMM_OCL_MapElement", QMM_OCL112: "QualityMetamodel_QMM_OCL_OperatorCallExp", QMM_OCL133: "QualityMetamodel_QMM_OCL_IfExp", OclExpression116: "QualityMetamodel_QMM_OCL_BraceExp", OclExpression114: "QualityMetamodel_QMM_OCL_LambdaCallExp", QMM_OCL166: "QualityMetamodel_QMM_OCL_OclType", QMM_OCL150: "QualityMetamodel_QMM_OCL_LocalVariable", OclExpression96: "QualityMetamodel_QMM_OCL_StaticOperationCall", QMM_OCL243: "QualityMetamodel_QMM_OCL_Operation", QMM_OCL107: "QualityMetamodel_QMM_OCL_OperationCall", QMM_OCL101: "QualityMetamodel_QMM_OCL_PropertyCallExp", OclExpression109: "QualityMetamodel_QMM_OCL_OperatorCallExp", OclExpression72: "QualityMetamodel_QMM_OCL_CollectionRange", OclExpression87: "QualityMetamodel_QMM_OCL_MapElement", QMM_OCL130: "QualityMetamodel_QMM_OCL_LetExp", OclExpression: "QualityMetamodel_Operation"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class QualityMetamodel_IntegerValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class QualityMetamodel_BooleanValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class QualityMetamodel_RealValueType(ValueType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class VariableDeclaration:

    pass
class QualityMetamodel_QMM_OCL_Parameter(VariableDeclaration):

    pass
class QualityMetamodel_QMM_OCL_Iterator(VariableDeclaration):

    pass
class QualityMetamodel_QMM_OCL_LocalVariable(VariableDeclaration):

    def __init__(self, eq: str, LetExp146: "LetExp" = None, OclExpression149: "OclExpression" = None, IterateExp: "IterateExp" = None, QMM_OCL63: "QualityMetamodel_QMM_OCL_VariableExp", QMM_OCL184: "QualityMetamodel_QMM_OCL_OclType"):
        self.eq = eq
        self.LetExp146 = LetExp146
        self.OclExpression149 = OclExpression149
        self.IterateExp = IterateExp
        
    @property
    def eq(self) -> str:
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq

    @property
    def OclExpression149(self):
        return self.__OclExpression149

    @OclExpression149.setter
    def OclExpression149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_LocalVariable__OclExpression149", None)
        self.__OclExpression149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL150"):
                opp_val = getattr(old_value, "QMM_OCL150", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL150"):
                opp_val = getattr(value, "QMM_OCL150", None)
                setattr(value, "QMM_OCL150", self)

    @property
    def LetExp146(self):
        return self.__LetExp146

    @LetExp146.setter
    def LetExp146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_LocalVariable__LetExp146", None)
        self.__LetExp146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL147"):
                opp_val = getattr(old_value, "QMM_OCL147", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL147"):
                opp_val = getattr(value, "QMM_OCL147", None)
                setattr(value, "QMM_OCL147", self)

    @property
    def IterateExp(self):
        return self.__IterateExp

    @IterateExp.setter
    def IterateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_QMM_OCL_LocalVariable__IterateExp", None)
        self.__IterateExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QMM_OCL152"):
                opp_val = getattr(old_value, "QMM_OCL152", None)
                if opp_val == self:
                    setattr(old_value, "QMM_OCL152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QMM_OCL152"):
                opp_val = getattr(value, "QMM_OCL152", None)
                setattr(value, "QMM_OCL152", self)

class QualityMetamodel_Value(VariableDeclaration):

    def __init__(self, description: str, QualityMetamodel_Value: "QualityMetamodel_QualityModel" = None, QualityMetamodel_Value9: "QualityMetamodel_QualityAttribute" = None, val: "QualityMetamodel_ValueType" = None, Value: "QualityMetamodel_ValueType" = None, QualityMetamodel_Value20: "QualityMetamodel_Operation" = None, QMM_OCL63: "QualityMetamodel_QMM_OCL_VariableExp", QMM_OCL184: "QualityMetamodel_QMM_OCL_OclType"):
        self.description = description
        self.QualityMetamodel_Value = QualityMetamodel_Value
        self.QualityMetamodel_Value9 = QualityMetamodel_Value9
        self.val = val
        self.Value = Value
        self.QualityMetamodel_Value20 = QualityMetamodel_Value20
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__val", None)
        self.__val = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueType"):
                opp_val = getattr(old_value, "ValueType", None)
                if opp_val == self:
                    setattr(old_value, "ValueType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueType"):
                opp_val = getattr(value, "ValueType", None)
                setattr(value, "ValueType", self)

    @property
    def QualityMetamodel_Value9(self):
        return self.__QualityMetamodel_Value9

    @QualityMetamodel_Value9.setter
    def QualityMetamodel_Value9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__QualityMetamodel_Value9", None)
        self.__QualityMetamodel_Value9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityAttribute8"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityAttribute8", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_QualityAttribute8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityAttribute8"):
                opp_val = getattr(value, "QualityMetamodel_QualityAttribute8", None)
                setattr(value, "QualityMetamodel_QualityAttribute8", self)

    @property
    def QualityMetamodel_Value(self):
        return self.__QualityMetamodel_Value

    @QualityMetamodel_Value.setter
    def QualityMetamodel_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__QualityMetamodel_Value", None)
        self.__QualityMetamodel_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityModel6"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityModel6"):
                opp_val = getattr(value, "QualityMetamodel_QualityModel6", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_QualityModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__Value", None)
        self.__Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueType"):
                opp_val = getattr(old_value, "valueType", None)
                if opp_val == self:
                    setattr(old_value, "valueType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueType"):
                opp_val = getattr(value, "valueType", None)
                setattr(value, "valueType", self)

    @property
    def QualityMetamodel_Value20(self):
        return self.__QualityMetamodel_Value20

    @QualityMetamodel_Value20.setter
    def QualityMetamodel_Value20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Value__QualityMetamodel_Value20", None)
        self.__QualityMetamodel_Value20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_Operation19"):
                opp_val = getattr(old_value, "QualityMetamodel_Operation19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_Operation19"):
                opp_val = getattr(value, "QualityMetamodel_Operation19", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_Operation19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class QualityMetamodel_QualityAttribute(VariableDeclaration):

    pass
class QualityMetamodel_ValueType(VariableDeclaration):

    pass
class QualityMetamodel_MetricProvider:

    def __init__(self, name: str, description: str, id: str, QualityMetamodel_MetricProvider16: "QualityMetamodel_SingleValue" = None, QualityMetamodel_MetricProvider: "QualityMetamodel_QualityModel" = None):
        self.name = name
        self.description = description
        self.id = id
        self.QualityMetamodel_MetricProvider16 = QualityMetamodel_MetricProvider16
        self.QualityMetamodel_MetricProvider = QualityMetamodel_MetricProvider
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def QualityMetamodel_MetricProvider16(self):
        return self.__QualityMetamodel_MetricProvider16

    @QualityMetamodel_MetricProvider16.setter
    def QualityMetamodel_MetricProvider16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_MetricProvider__QualityMetamodel_MetricProvider16", None)
        self.__QualityMetamodel_MetricProvider16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_SingleValue"):
                opp_val = getattr(old_value, "QualityMetamodel_SingleValue", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_SingleValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_SingleValue"):
                opp_val = getattr(value, "QualityMetamodel_SingleValue", None)
                setattr(value, "QualityMetamodel_SingleValue", self)

    @property
    def QualityMetamodel_MetricProvider(self):
        return self.__QualityMetamodel_MetricProvider

    @QualityMetamodel_MetricProvider.setter
    def QualityMetamodel_MetricProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_MetricProvider__QualityMetamodel_MetricProvider", None)
        self.__QualityMetamodel_MetricProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_QualityModel"):
                opp_val = getattr(old_value, "QualityMetamodel_QualityModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_QualityModel"):
                opp_val = getattr(value, "QualityMetamodel_QualityModel", None)
                if opp_val is None:
                    setattr(value, "QualityMetamodel_QualityModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Module:

    pass
class QualityMetamodel_QualityModel(Module):

    pass
class QualityMetamodel_Operation:

    def __init__(self, name: str, body: str, QualityMetamodel_Operation: "QualityMetamodel_AggregatedValue" = None, QualityMetamodel_Operation19: set["QualityMetamodel_Value"] = None, QualityMetamodel_Operation22: "OclExpression" = None):
        self.name = name
        self.body = body
        self.QualityMetamodel_Operation = QualityMetamodel_Operation
        self.QualityMetamodel_Operation19 = QualityMetamodel_Operation19 if QualityMetamodel_Operation19 is not None else set()
        self.QualityMetamodel_Operation22 = QualityMetamodel_Operation22
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def QualityMetamodel_Operation22(self):
        return self.__QualityMetamodel_Operation22

    @QualityMetamodel_Operation22.setter
    def QualityMetamodel_Operation22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Operation__QualityMetamodel_Operation22", None)
        self.__QualityMetamodel_Operation22 = value
        
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

    @property
    def QualityMetamodel_Operation19(self):
        return self.__QualityMetamodel_Operation19

    @QualityMetamodel_Operation19.setter
    def QualityMetamodel_Operation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Operation__QualityMetamodel_Operation19", None)
        self.__QualityMetamodel_Operation19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QualityMetamodel_Value20"):
                    opp_val = getattr(item, "QualityMetamodel_Value20", None)
                    
                    if opp_val == self:
                        setattr(item, "QualityMetamodel_Value20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QualityMetamodel_Value20"):
                    opp_val = getattr(item, "QualityMetamodel_Value20", None)
                    
                    setattr(item, "QualityMetamodel_Value20", self)
                    

    @property
    def QualityMetamodel_Operation(self):
        return self.__QualityMetamodel_Operation

    @QualityMetamodel_Operation.setter
    def QualityMetamodel_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetamodel_Operation__QualityMetamodel_Operation", None)
        self.__QualityMetamodel_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetamodel_AggregatedValue"):
                opp_val = getattr(old_value, "QualityMetamodel_AggregatedValue", None)
                if opp_val == self:
                    setattr(old_value, "QualityMetamodel_AggregatedValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetamodel_AggregatedValue"):
                opp_val = getattr(value, "QualityMetamodel_AggregatedValue", None)
                setattr(value, "QualityMetamodel_AggregatedValue", self)

class Value:

    pass
class QualityMetamodel_AggregatedValue(Value):

    pass
class QualityMetamodel_SingleValue(Value):

    pass