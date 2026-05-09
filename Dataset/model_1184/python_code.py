from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class VirtualFeature:

    pass
class gbind_dsl_VirtualAttribute(VirtualFeature):

    pass
class gbind_dsl_VirtualReference(VirtualFeature):

    pass
class gbind_dsl_Metaclass(ABC):

    def __init__(self, name: str, gbind_dsl_Metaclass: "dsl_gbind_EClass" = None):
        self.name = name
        self.gbind_dsl_Metaclass = gbind_dsl_Metaclass
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def gbind_dsl_Metaclass(self):
        return self.__gbind_dsl_Metaclass

    @gbind_dsl_Metaclass.setter
    def gbind_dsl_Metaclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_Metaclass__gbind_dsl_Metaclass", None)
        self.__gbind_dsl_Metaclass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_gbind_EClass"):
                opp_val = getattr(old_value, "dsl_gbind_EClass", None)
                if opp_val == self:
                    setattr(old_value, "dsl_gbind_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_gbind_EClass"):
                opp_val = getattr(value, "dsl_gbind_EClass", None)
                setattr(value, "dsl_gbind_EClass", self)

class gbind_dsl_BindingOptions:

    def __init__(self, enableClassMerge: bool):
        self.enableClassMerge = enableClassMerge
        
        pass
    @property
    def enableClassMerge(self):
        return self.__enableClassMerge

    @enableClassMerge.setter
    def enableClassMerge(self, enableClassMerge: bool):
        self.__enableClassMerge = enableClassMerge


class BindingOptions:

    pass
class MetamodelDeclaration:

    pass
class VirtualMetaclass:

    pass
class ConcreteMetaclass:

    pass
class ConceptMetaclass:

    pass
class BaseHelper:

    pass
class ConceptBinding:

    pass
class gbind_dsl_VirtualClassBinding(ConceptBinding):

    pass
class gbind_dsl_BindingModel:

    def __init__(self, targetBinding: bool, name: str, model_: set["ConceptBinding"] = None, model_157: set["BaseHelper"] = None, gbind_dsl_BindingModel: set["ConceptMetaclass"] = None, gbind_dsl_BindingModel160: set["ConcreteMetaclass"] = None, gbind_dsl_BindingModel162: set["VirtualMetaclass"] = None, gbind_dsl_BindingModel164: "MetamodelDeclaration" = None, gbind_dsl_BindingModel166: set["MetamodelDeclaration"] = None, gbind_dsl_BindingModel169: "BindingOptions" = None):
        self.targetBinding = targetBinding
        self.name = name
        self.model_ = model_ if model_ is not None else set()
        self.model_157 = model_157 if model_157 is not None else set()
        self.gbind_dsl_BindingModel = gbind_dsl_BindingModel if gbind_dsl_BindingModel is not None else set()
        self.gbind_dsl_BindingModel160 = gbind_dsl_BindingModel160 if gbind_dsl_BindingModel160 is not None else set()
        self.gbind_dsl_BindingModel162 = gbind_dsl_BindingModel162 if gbind_dsl_BindingModel162 is not None else set()
        self.gbind_dsl_BindingModel164 = gbind_dsl_BindingModel164
        self.gbind_dsl_BindingModel166 = gbind_dsl_BindingModel166 if gbind_dsl_BindingModel166 is not None else set()
        self.gbind_dsl_BindingModel169 = gbind_dsl_BindingModel169
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def targetBinding(self):
        return self.__targetBinding

    @targetBinding.setter
    def targetBinding(self, targetBinding: bool):
        self.__targetBinding = targetBinding


    @property
    def model_157(self):
        return self.__model_157

    @model_157.setter
    def model_157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__model_157", None)
        self.__model_157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseHelper"):
                    opp_val = getattr(item, "BaseHelper", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseHelper", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseHelper"):
                    opp_val = getattr(item, "BaseHelper", None)
                    
                    setattr(item, "BaseHelper", self)
                    

    @property
    def gbind_dsl_BindingModel(self):
        return self.__gbind_dsl_BindingModel

    @gbind_dsl_BindingModel.setter
    def gbind_dsl_BindingModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel", None)
        self.__gbind_dsl_BindingModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConceptMetaclass"):
                    opp_val = getattr(item, "ConceptMetaclass", None)
                    
                    if opp_val == self:
                        setattr(item, "ConceptMetaclass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConceptMetaclass"):
                    opp_val = getattr(item, "ConceptMetaclass", None)
                    
                    setattr(item, "ConceptMetaclass", self)
                    

    @property
    def gbind_dsl_BindingModel164(self):
        return self.__gbind_dsl_BindingModel164

    @gbind_dsl_BindingModel164.setter
    def gbind_dsl_BindingModel164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel164", None)
        self.__gbind_dsl_BindingModel164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetamodelDeclaration"):
                opp_val = getattr(old_value, "MetamodelDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "MetamodelDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetamodelDeclaration"):
                opp_val = getattr(value, "MetamodelDeclaration", None)
                setattr(value, "MetamodelDeclaration", self)

    @property
    def gbind_dsl_BindingModel160(self):
        return self.__gbind_dsl_BindingModel160

    @gbind_dsl_BindingModel160.setter
    def gbind_dsl_BindingModel160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel160", None)
        self.__gbind_dsl_BindingModel160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConcreteMetaclass"):
                    opp_val = getattr(item, "ConcreteMetaclass", None)
                    
                    if opp_val == self:
                        setattr(item, "ConcreteMetaclass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConcreteMetaclass"):
                    opp_val = getattr(item, "ConcreteMetaclass", None)
                    
                    setattr(item, "ConcreteMetaclass", self)
                    

    @property
    def gbind_dsl_BindingModel166(self):
        return self.__gbind_dsl_BindingModel166

    @gbind_dsl_BindingModel166.setter
    def gbind_dsl_BindingModel166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel166", None)
        self.__gbind_dsl_BindingModel166 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetamodelDeclaration167"):
                    opp_val = getattr(item, "MetamodelDeclaration167", None)
                    
                    if opp_val == self:
                        setattr(item, "MetamodelDeclaration167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetamodelDeclaration167"):
                    opp_val = getattr(item, "MetamodelDeclaration167", None)
                    
                    setattr(item, "MetamodelDeclaration167", self)
                    

    @property
    def gbind_dsl_BindingModel162(self):
        return self.__gbind_dsl_BindingModel162

    @gbind_dsl_BindingModel162.setter
    def gbind_dsl_BindingModel162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel162", None)
        self.__gbind_dsl_BindingModel162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VirtualMetaclass"):
                    opp_val = getattr(item, "VirtualMetaclass", None)
                    
                    if opp_val == self:
                        setattr(item, "VirtualMetaclass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VirtualMetaclass"):
                    opp_val = getattr(item, "VirtualMetaclass", None)
                    
                    setattr(item, "VirtualMetaclass", self)
                    

    @property
    def gbind_dsl_BindingModel169(self):
        return self.__gbind_dsl_BindingModel169

    @gbind_dsl_BindingModel169.setter
    def gbind_dsl_BindingModel169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__gbind_dsl_BindingModel169", None)
        self.__gbind_dsl_BindingModel169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BindingOptions"):
                opp_val = getattr(old_value, "BindingOptions", None)
                if opp_val == self:
                    setattr(old_value, "BindingOptions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BindingOptions"):
                opp_val = getattr(value, "BindingOptions", None)
                setattr(value, "BindingOptions", self)

    @property
    def model_(self):
        return self.__model_

    @model_.setter
    def model_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BindingModel__model_", None)
        self.__model_ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConceptBinding"):
                    opp_val = getattr(item, "ConceptBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "ConceptBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConceptBinding"):
                    opp_val = getattr(item, "ConceptBinding", None)
                    
                    setattr(item, "ConceptBinding", self)
                    

class gbind_dsl_ClassBinding(ConceptBinding):

    pass
class BindingModel:

    pass
class gbind_dsl_ConceptBinding(ABC):

    def __init__(self, debugName: str, bindings: "BindingModel" = None):
        self.debugName = debugName
        self.bindings = bindings
        
        pass
    @property
    def debugName(self):
        return self.__debugName

    @debugName.setter
    def debugName(self, debugName: str):
        self.__debugName = debugName


    @property
    def bindings(self):
        return self.__bindings

    @bindings.setter
    def bindings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_ConceptBinding__bindings", None)
        self.__bindings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BindingModel"):
                opp_val = getattr(old_value, "BindingModel", None)
                if opp_val == self:
                    setattr(old_value, "BindingModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BindingModel"):
                opp_val = getattr(value, "BindingModel", None)
                setattr(value, "BindingModel", self)

class Metaclass:

    pass
class gbind_dsl_ConcreteMetaclass(Metaclass):

    pass
class gbind_dsl_ConceptMetaclass(Metaclass):

    pass
class dsl_gbind_EClass:

    pass
class Parameter:

    pass
class OclFeatureDefinition:

    pass
class OclInstanceModel:

    pass
class OclModelElement:

    pass
class TupleType:

    pass
class NumericType:

    pass
class gbind_simpleocl_RealType(NumericType):

    pass
class OclFeature:

    pass
class gbind_simpleocl_Operation(OclFeature):

    pass
class gbind_simpleocl_Attribute(OclFeature):

    pass
class LambdaType:

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class gbind_simpleocl_BagType(CollectionType):

    pass
class gbind_simpleocl_SequenceType(CollectionType):

    pass
class gbind_simpleocl_OrderedSetType(CollectionType):

    pass
class gbind_simpleocl_SetType(CollectionType):

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class gbind_simpleocl_IntegerType(NumericType):

    pass
class Primitive:

    pass
class gbind_simpleocl_BooleanType(Primitive):

    pass
class gbind_simpleocl_NumericType(Primitive):

    pass
class gbind_simpleocl_StringType(Primitive):

    pass
class OclModel:

    pass
class gbind_simpleocl_OclInstanceModel(OclModel):

    pass
class gbind_simpleocl_OclMetamodel(OclModel):

    def __init__(self, uri: str, metamodel: set["OclInstanceModel"] = None, OclModel: "gbind_simpleocl_OclModelElementExp" = None, OclModel121: "gbind_simpleocl_OclModelElement" = None):
        self.uri = uri
        self.metamodel = metamodel if metamodel is not None else set()
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def metamodel(self):
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclMetamodel__metamodel", None)
        self.__metamodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclInstanceModel"):
                    opp_val = getattr(item, "OclInstanceModel", None)
                    
                    if opp_val == self:
                        setattr(item, "OclInstanceModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclInstanceModel"):
                    opp_val = getattr(item, "OclInstanceModel", None)
                    
                    setattr(item, "OclInstanceModel", self)
                    

class IterateExp:

    pass
class Iterator:

    pass
class VariableExp:

    pass
class gbind_simpleocl_LambdaCallExp(VariableExp):

    pass
class PropertyCall:

    pass
class gbind_simpleocl_LoopExp(PropertyCall):

    pass
class gbind_simpleocl_OperationCall(PropertyCall):

    def __init__(self, operationName: str, parentOperation: set["OclExpression"] = None, PropertyCall: "gbind_simpleocl_PropertyCallExp" = None):
        self.operationName = operationName
        self.parentOperation = parentOperation if parentOperation is not None else set()
        
        pass
    @property
    def operationName(self):
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName


    @property
    def parentOperation(self):
        return self.__parentOperation

    @parentOperation.setter
    def parentOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OperationCall__parentOperation", None)
        self.__parentOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression50"):
                    opp_val = getattr(item, "OclExpression50", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression50"):
                    opp_val = getattr(item, "OclExpression50", None)
                    
                    setattr(item, "OclExpression50", self)
                    

class gbind_simpleocl_NavigationOrAttributeCall(PropertyCall):

    def __init__(self, name: str, PropertyCall: "gbind_simpleocl_PropertyCallExp" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class StaticPropertyCallExp:

    pass
class StaticPropertyCall:

    pass
class gbind_simpleocl_StaticNavigationOrAttributeCall(StaticPropertyCall):

    def __init__(self, name: str, StaticPropertyCall: "gbind_simpleocl_StaticPropertyCallExp" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class gbind_simpleocl_StaticOperationCall(StaticPropertyCall):

    def __init__(self, operationName: str, gbind_simpleocl_StaticOperationCall: set["OclExpression"] = None, StaticPropertyCall: "gbind_simpleocl_StaticPropertyCallExp" = None):
        self.operationName = operationName
        self.gbind_simpleocl_StaticOperationCall = gbind_simpleocl_StaticOperationCall if gbind_simpleocl_StaticOperationCall is not None else set()
        
        pass
    @property
    def operationName(self):
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName


    @property
    def gbind_simpleocl_StaticOperationCall(self):
        return self.__gbind_simpleocl_StaticOperationCall

    @gbind_simpleocl_StaticOperationCall.setter
    def gbind_simpleocl_StaticOperationCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_StaticOperationCall__gbind_simpleocl_StaticOperationCall", None)
        self.__gbind_simpleocl_StaticOperationCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression43"):
                    opp_val = getattr(item, "OclExpression43", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression43"):
                    opp_val = getattr(item, "OclExpression43", None)
                    
                    setattr(item, "OclExpression43", self)
                    

class MapExp:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class gbind_dsl_VirtualTupleExp(TupleExp):

    def __init__(self, typeName: str, TupleExp: "gbind_simpleocl_TuplePart" = None):
        self.typeName = typeName
        
        pass
    @property
    def typeName(self):
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName


class TuplePart:

    pass
class PrimitiveExp:

    pass
class gbind_simpleocl_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class VariableDeclaration:

    pass
class gbind_simpleocl_Iterator(VariableDeclaration):

    pass
class gbind_simpleocl_Parameter(VariableDeclaration):

    pass
class gbind_simpleocl_LocalVariable(VariableDeclaration):

    def __init__(self, eq: str, variable: "LetExp" = None, initializedVariable: "OclExpression" = None, result: "IterateExp" = None, VariableDeclaration: "gbind_simpleocl_VariableExp" = None, VariableDeclaration105: "gbind_simpleocl_OclType" = None):
        self.eq = eq
        self.variable = variable
        self.initializedVariable = initializedVariable
        self.result = result
        
        pass
    @property
    def eq(self):
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq


    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_LocalVariable__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp79"):
                opp_val = getattr(old_value, "LetExp79", None)
                if opp_val == self:
                    setattr(old_value, "LetExp79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp79"):
                opp_val = getattr(value, "LetExp79", None)
                setattr(value, "LetExp79", self)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_LocalVariable__result", None)
        self.__result = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IterateExp"):
                opp_val = getattr(old_value, "IterateExp", None)
                if opp_val == self:
                    setattr(old_value, "IterateExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IterateExp"):
                opp_val = getattr(value, "IterateExp", None)
                setattr(value, "IterateExp", self)

    @property
    def initializedVariable(self):
        return self.__initializedVariable

    @initializedVariable.setter
    def initializedVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_LocalVariable__initializedVariable", None)
        self.__initializedVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression81"):
                opp_val = getattr(old_value, "OclExpression81", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression81"):
                opp_val = getattr(value, "OclExpression81", None)
                setattr(value, "OclExpression81", self)

class OclExpression:

    pass
class gbind_simpleocl_PrimitiveExp(OclExpression):

    pass
class gbind_simpleocl_OclUndefinedExp(OclExpression):

    pass
class gbind_simpleocl_OperatorCallExp(OclExpression):

    def __init__(self, operationName: str, gbind_simpleocl_OperatorCallExp: "OclExpression" = None, appliedOperator: "OclExpression" = None, OclExpression72: "gbind_simpleocl_IfExp" = None, OclExpression54: "gbind_simpleocl_OperatorCallExp" = None, OclExpression43: "gbind_simpleocl_StaticOperationCall" = None, OclExpression: "gbind_simpleocl_CollectionExp" = None, OclExpression179: "gbind_dsl_ClassBinding" = None, OclExpression52: "gbind_simpleocl_OperatorCallExp" = None, OclExpression149: "gbind_simpleocl_Operation" = None, OclExpression218: "gbind_dsl_BaseHelper" = None, OclExpression74: "gbind_simpleocl_IfExp" = None, OclExpression91: "gbind_simpleocl_OclType" = None, OclExpression70: "gbind_simpleocl_IfExp" = None, OclExpression68: "gbind_simpleocl_LetExp" = None, OclExpression50: "gbind_simpleocl_OperationCall" = None, OclExpression34: "gbind_simpleocl_MapElement" = None, OclExpression46: "gbind_simpleocl_PropertyCallExp" = None, OclExpression56: "gbind_simpleocl_LambdaCallExp" = None, OclExpression60: "gbind_simpleocl_LoopExp" = None, OclExpression216: "gbind_dsl_OclFeatureBinding" = None, OclExpression81: "gbind_simpleocl_LocalVariable" = None, OclExpression58: "gbind_simpleocl_BraceExp" = None, OclExpression37: "gbind_simpleocl_MapElement" = None, OclExpression197: "gbind_dsl_VirtualMetaclass" = None, OclExpression141: "gbind_simpleocl_Attribute" = None):
        self.operationName = operationName
        self.gbind_simpleocl_OperatorCallExp = gbind_simpleocl_OperatorCallExp
        self.appliedOperator = appliedOperator
        
        pass
    @property
    def operationName(self):
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName


    @property
    def appliedOperator(self):
        return self.__appliedOperator

    @appliedOperator.setter
    def appliedOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OperatorCallExp__appliedOperator", None)
        self.__appliedOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression54"):
                opp_val = getattr(old_value, "OclExpression54", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression54"):
                opp_val = getattr(value, "OclExpression54", None)
                setattr(value, "OclExpression54", self)

    @property
    def gbind_simpleocl_OperatorCallExp(self):
        return self.__gbind_simpleocl_OperatorCallExp

    @gbind_simpleocl_OperatorCallExp.setter
    def gbind_simpleocl_OperatorCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OperatorCallExp__gbind_simpleocl_OperatorCallExp", None)
        self.__gbind_simpleocl_OperatorCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression52"):
                opp_val = getattr(old_value, "OclExpression52", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression52"):
                opp_val = getattr(value, "OclExpression52", None)
                setattr(value, "OclExpression52", self)

class gbind_simpleocl_CollectionExp(OclExpression):

    pass
class gbind_simpleocl_PropertyCallExp(OclExpression):

    pass
class gbind_simpleocl_MapExp(OclExpression):

    pass
class gbind_simpleocl_SelfExp(OclExpression):

    pass
class gbind_simpleocl_BraceExp(OclExpression):

    pass
class gbind_simpleocl_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression72: "gbind_simpleocl_IfExp" = None, OclExpression54: "gbind_simpleocl_OperatorCallExp" = None, OclExpression43: "gbind_simpleocl_StaticOperationCall" = None, OclExpression: "gbind_simpleocl_CollectionExp" = None, OclExpression179: "gbind_dsl_ClassBinding" = None, OclExpression52: "gbind_simpleocl_OperatorCallExp" = None, OclExpression149: "gbind_simpleocl_Operation" = None, OclExpression218: "gbind_dsl_BaseHelper" = None, OclExpression74: "gbind_simpleocl_IfExp" = None, OclExpression91: "gbind_simpleocl_OclType" = None, OclExpression70: "gbind_simpleocl_IfExp" = None, OclExpression68: "gbind_simpleocl_LetExp" = None, OclExpression50: "gbind_simpleocl_OperationCall" = None, OclExpression34: "gbind_simpleocl_MapElement" = None, OclExpression46: "gbind_simpleocl_PropertyCallExp" = None, OclExpression56: "gbind_simpleocl_LambdaCallExp" = None, OclExpression60: "gbind_simpleocl_LoopExp" = None, OclExpression216: "gbind_dsl_OclFeatureBinding" = None, OclExpression81: "gbind_simpleocl_LocalVariable" = None, OclExpression58: "gbind_simpleocl_BraceExp" = None, OclExpression37: "gbind_simpleocl_MapElement" = None, OclExpression197: "gbind_dsl_VirtualMetaclass" = None, OclExpression141: "gbind_simpleocl_Attribute" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class gbind_simpleocl_TupleExp(OclExpression):

    pass
class gbind_simpleocl_EnvExp(OclExpression):

    pass
class gbind_simpleocl_OclModelElementExp(OclExpression):

    def __init__(self, name: str, gbind_simpleocl_OclModelElementExp: "OclModel" = None, OclExpression72: "gbind_simpleocl_IfExp" = None, OclExpression54: "gbind_simpleocl_OperatorCallExp" = None, OclExpression43: "gbind_simpleocl_StaticOperationCall" = None, OclExpression: "gbind_simpleocl_CollectionExp" = None, OclExpression179: "gbind_dsl_ClassBinding" = None, OclExpression52: "gbind_simpleocl_OperatorCallExp" = None, OclExpression149: "gbind_simpleocl_Operation" = None, OclExpression218: "gbind_dsl_BaseHelper" = None, OclExpression74: "gbind_simpleocl_IfExp" = None, OclExpression91: "gbind_simpleocl_OclType" = None, OclExpression70: "gbind_simpleocl_IfExp" = None, OclExpression68: "gbind_simpleocl_LetExp" = None, OclExpression50: "gbind_simpleocl_OperationCall" = None, OclExpression34: "gbind_simpleocl_MapElement" = None, OclExpression46: "gbind_simpleocl_PropertyCallExp" = None, OclExpression56: "gbind_simpleocl_LambdaCallExp" = None, OclExpression60: "gbind_simpleocl_LoopExp" = None, OclExpression216: "gbind_dsl_OclFeatureBinding" = None, OclExpression81: "gbind_simpleocl_LocalVariable" = None, OclExpression58: "gbind_simpleocl_BraceExp" = None, OclExpression37: "gbind_simpleocl_MapElement" = None, OclExpression197: "gbind_dsl_VirtualMetaclass" = None, OclExpression141: "gbind_simpleocl_Attribute" = None):
        self.name = name
        self.gbind_simpleocl_OclModelElementExp = gbind_simpleocl_OclModelElementExp
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def gbind_simpleocl_OclModelElementExp(self):
        return self.__gbind_simpleocl_OclModelElementExp

    @gbind_simpleocl_OclModelElementExp.setter
    def gbind_simpleocl_OclModelElementExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclModelElementExp__gbind_simpleocl_OclModelElementExp", None)
        self.__gbind_simpleocl_OclModelElementExp = value
        
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

class gbind_simpleocl_StaticPropertyCallExp(OclExpression):

    pass
class gbind_simpleocl_IfExp(OclExpression):

    pass
class gbind_simpleocl_LetExp(OclExpression):

    pass
class gbind_simpleocl_SuperExp(OclExpression):

    pass
class gbind_simpleocl_VariableExp(OclExpression):

    pass
class OperatorCallExp:

    pass
class gbind_simpleocl_EqOpCallExp(OperatorCallExp):

    pass
class gbind_simpleocl_MulOpCallExp(OperatorCallExp):

    pass
class gbind_simpleocl_IntOpCallExp(OperatorCallExp):

    pass
class gbind_simpleocl_AddOpCallExp(OperatorCallExp):

    pass
class gbind_simpleocl_RelOpCallExp(OperatorCallExp):

    pass
class gbind_simpleocl_NotOpCallExp(OperatorCallExp):

    pass
class Attribute:

    pass
class NumericExp:

    pass
class gbind_simpleocl_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


class gbind_simpleocl_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol


class gbind_simpleocl_NumericExp(PrimitiveExp):

    pass
class gbind_simpleocl_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


class LetExp:

    pass
class CollectionExp:

    pass
class gbind_simpleocl_SequenceExp(CollectionExp):

    pass
class gbind_simpleocl_BagExp(CollectionExp):

    pass
class gbind_simpleocl_OrderedSetExp(CollectionExp):

    pass
class gbind_simpleocl_SetExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class IfExp:

    pass
class OclType:

    pass
class gbind_simpleocl_EnvType(OclType):

    pass
class gbind_simpleocl_Primitive(OclType):

    pass
class gbind_simpleocl_CollectionType(OclType):

    pass
class gbind_simpleocl_OclModelElement(OclType):

    pass
class gbind_simpleocl_LambdaType(OclType):

    pass
class gbind_simpleocl_TupleType(OclType):

    pass
class gbind_simpleocl_OclAnyType(OclType):

    pass
class gbind_simpleocl_MapType(OclType):

    pass
class Module:

    pass
class ModuleElement:

    pass
class gbind_simpleocl_OclFeatureDefinition(ModuleElement):

    def __init__(self, static: str, definition: "OclFeature" = None, definition132: "OclContextDefinition" = None, ModuleElement: "gbind_simpleocl_Module" = None):
        self.static = static
        self.definition = definition
        self.definition132 = definition132
        
        pass
    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static


    @property
    def definition(self):
        return self.__definition

    @definition.setter
    def definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclFeatureDefinition__definition", None)
        self.__definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclFeature"):
                opp_val = getattr(old_value, "OclFeature", None)
                if opp_val == self:
                    setattr(old_value, "OclFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclFeature"):
                opp_val = getattr(value, "OclFeature", None)
                setattr(value, "OclFeature", self)

    @property
    def definition132(self):
        return self.__definition132

    @definition132.setter
    def definition132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclFeatureDefinition__definition132", None)
        self.__definition132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclContextDefinition133"):
                opp_val = getattr(old_value, "OclContextDefinition133", None)
                if opp_val == self:
                    setattr(old_value, "OclContextDefinition133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclContextDefinition133"):
                opp_val = getattr(value, "OclContextDefinition133", None)
                setattr(value, "OclContextDefinition133", self)

class Import:

    pass
class OclMetamodel:

    pass
class gbind_dsl_MetamodelDeclaration(OclMetamodel):

    def __init__(self, metamodelURI: str, resource: str, OclMetamodel: "gbind_simpleocl_Module" = None, OclMetamodel154: "gbind_simpleocl_OclInstanceModel" = None):
        self.metamodelURI = metamodelURI
        self.resource = resource
        
        pass
    @property
    def resource(self):
        return self.__resource

    @resource.setter
    def resource(self, resource: str):
        self.__resource = resource


    @property
    def metamodelURI(self):
        return self.__metamodelURI

    @metamodelURI.setter
    def metamodelURI(self, metamodelURI: str):
        self.__metamodelURI = metamodelURI


class NamedElement:

    pass
class gbind_simpleocl_OclFeature(NamedElement):

    def __init__(self, eq: str, feature: "OclFeatureDefinition" = None):
        self.eq = eq
        self.feature = feature
        
        pass
    @property
    def eq(self):
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq


    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclFeature__feature", None)
        self.__feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclFeatureDefinition139"):
                opp_val = getattr(old_value, "OclFeatureDefinition139", None)
                if opp_val == self:
                    setattr(old_value, "OclFeatureDefinition139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclFeatureDefinition139"):
                opp_val = getattr(value, "OclFeatureDefinition139", None)
                setattr(value, "OclFeatureDefinition139", self)

class gbind_simpleocl_Import(NamedElement):

    pass
class gbind_simpleocl_OclModel(NamedElement):

    pass
class gbind_simpleocl_Module(NamedElement):

    pass
class LocatedElement:

    pass
class gbind_simpleocl_StaticPropertyCall(LocatedElement):

    pass
class gbind_simpleocl_OclExpression(LocatedElement):

    pass
class gbind_simpleocl_OclType(LocatedElement):

    def __init__(self, name: str, context_: "OclContextDefinition" = None, type: "OclExpression" = None, returnType: "Operation" = None, valueType: "MapType" = None, type96: "Attribute" = None, keyType: "MapType" = None, elementType: "CollectionType" = None, type102: "TupleTypeAttribute" = None, type104: "VariableDeclaration" = None, returnType107: "LambdaType" = None, argumentTypes: "LambdaType" = None, source111: "StaticPropertyCallExp" = None):
        self.name = name
        self.context_ = context_
        self.type = type
        self.returnType = returnType
        self.valueType = valueType
        self.type96 = type96
        self.keyType = keyType
        self.elementType = elementType
        self.type102 = type102
        self.type104 = type104
        self.returnType107 = returnType107
        self.argumentTypes = argumentTypes
        self.source111 = source111
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type96(self):
        return self.__type96

    @type96.setter
    def type96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__type96", None)
        self.__type96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute97"):
                opp_val = getattr(old_value, "Attribute97", None)
                if opp_val == self:
                    setattr(old_value, "Attribute97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute97"):
                opp_val = getattr(value, "Attribute97", None)
                setattr(value, "Attribute97", self)

    @property
    def source111(self):
        return self.__source111

    @source111.setter
    def source111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__source111", None)
        self.__source111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StaticPropertyCallExp112"):
                opp_val = getattr(old_value, "StaticPropertyCallExp112", None)
                if opp_val == self:
                    setattr(old_value, "StaticPropertyCallExp112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StaticPropertyCallExp112"):
                opp_val = getattr(value, "StaticPropertyCallExp112", None)
                setattr(value, "StaticPropertyCallExp112", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression91"):
                opp_val = getattr(old_value, "OclExpression91", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression91"):
                opp_val = getattr(value, "OclExpression91", None)
                setattr(value, "OclExpression91", self)

    @property
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__keyType", None)
        self.__keyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType99"):
                opp_val = getattr(old_value, "MapType99", None)
                if opp_val == self:
                    setattr(old_value, "MapType99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType99"):
                opp_val = getattr(value, "MapType99", None)
                setattr(value, "MapType99", self)

    @property
    def type104(self):
        return self.__type104

    @type104.setter
    def type104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__type104", None)
        self.__type104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration105"):
                opp_val = getattr(old_value, "VariableDeclaration105", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration105"):
                opp_val = getattr(value, "VariableDeclaration105", None)
                setattr(value, "VariableDeclaration105", self)

    @property
    def valueType(self):
        return self.__valueType

    @valueType.setter
    def valueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__valueType", None)
        self.__valueType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType"):
                opp_val = getattr(old_value, "MapType", None)
                if opp_val == self:
                    setattr(old_value, "MapType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType"):
                opp_val = getattr(value, "MapType", None)
                setattr(value, "MapType", self)

    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation93"):
                opp_val = getattr(old_value, "Operation93", None)
                if opp_val == self:
                    setattr(old_value, "Operation93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation93"):
                opp_val = getattr(value, "Operation93", None)
                setattr(value, "Operation93", self)

    @property
    def argumentTypes(self):
        return self.__argumentTypes

    @argumentTypes.setter
    def argumentTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__argumentTypes", None)
        self.__argumentTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LambdaType109"):
                opp_val = getattr(old_value, "LambdaType109", None)
                if opp_val == self:
                    setattr(old_value, "LambdaType109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LambdaType109"):
                opp_val = getattr(value, "LambdaType109", None)
                setattr(value, "LambdaType109", self)

    @property
    def context_(self):
        return self.__context_

    @context_.setter
    def context_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__context_", None)
        self.__context_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclContextDefinition"):
                opp_val = getattr(old_value, "OclContextDefinition", None)
                if opp_val == self:
                    setattr(old_value, "OclContextDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclContextDefinition"):
                opp_val = getattr(value, "OclContextDefinition", None)
                setattr(value, "OclContextDefinition", self)

    @property
    def type102(self):
        return self.__type102

    @type102.setter
    def type102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__type102", None)
        self.__type102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TupleTypeAttribute"):
                opp_val = getattr(old_value, "TupleTypeAttribute", None)
                if opp_val == self:
                    setattr(old_value, "TupleTypeAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TupleTypeAttribute"):
                opp_val = getattr(value, "TupleTypeAttribute", None)
                setattr(value, "TupleTypeAttribute", self)

    @property
    def returnType107(self):
        return self.__returnType107

    @returnType107.setter
    def returnType107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__returnType107", None)
        self.__returnType107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LambdaType"):
                opp_val = getattr(old_value, "LambdaType", None)
                if opp_val == self:
                    setattr(old_value, "LambdaType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LambdaType"):
                opp_val = getattr(value, "LambdaType", None)
                setattr(value, "LambdaType", self)

    @property
    def elementType(self):
        return self.__elementType

    @elementType.setter
    def elementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_OclType__elementType", None)
        self.__elementType = value
        
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

class gbind_simpleocl_VariableDeclaration(LocatedElement):

    def __init__(self, varName: str, variableDeclaration: "OclType" = None, referredVariable: set["VariableExp"] = None):
        self.varName = varName
        self.variableDeclaration = variableDeclaration
        self.referredVariable = referredVariable if referredVariable is not None else set()
        
        pass
    @property
    def varName(self):
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName


    @property
    def variableDeclaration(self):
        return self.__variableDeclaration

    @variableDeclaration.setter
    def variableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_VariableDeclaration__variableDeclaration", None)
        self.__variableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType76"):
                opp_val = getattr(old_value, "OclType76", None)
                if opp_val == self:
                    setattr(old_value, "OclType76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType76"):
                opp_val = getattr(value, "OclType76", None)
                setattr(value, "OclType76", self)

    @property
    def referredVariable(self):
        return self.__referredVariable

    @referredVariable.setter
    def referredVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_VariableDeclaration__referredVariable", None)
        self.__referredVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableExp"):
                    opp_val = getattr(item, "VariableExp", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableExp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableExp"):
                    opp_val = getattr(item, "VariableExp", None)
                    
                    setattr(item, "VariableExp", self)
                    

class gbind_simpleocl_PropertyCall(LocatedElement):

    pass
class gbind_simpleocl_MapElement(LocatedElement):

    pass
class gbind_simpleocl_OclContextDefinition(LocatedElement):

    pass
class gbind_simpleocl_ModuleElement(LocatedElement):

    pass
class gbind_simpleocl_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, tupleTypeAttribute: "OclType" = None, attributes: "TupleType" = None):
        self.name = name
        self.tupleTypeAttribute = tupleTypeAttribute
        self.attributes = attributes
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_TupleTypeAttribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TupleType"):
                opp_val = getattr(old_value, "TupleType", None)
                if opp_val == self:
                    setattr(old_value, "TupleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TupleType"):
                opp_val = getattr(value, "TupleType", None)
                setattr(value, "TupleType", self)

    @property
    def tupleTypeAttribute(self):
        return self.__tupleTypeAttribute

    @tupleTypeAttribute.setter
    def tupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_simpleocl_TupleTypeAttribute__tupleTypeAttribute", None)
        self.__tupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType117"):
                opp_val = getattr(old_value, "OclType117", None)
                if opp_val == self:
                    setattr(old_value, "OclType117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType117"):
                opp_val = getattr(value, "OclType117", None)
                setattr(value, "OclType117", self)

class gbind_simpleocl_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Operation:

    pass
class LocalVariable:

    pass
class gbind_simpleocl_TuplePart(LocalVariable):

    pass
class OperationCall:

    pass
class gbind_simpleocl_CollectionOperationCall(OperationCall):

    pass
class LoopExp:

    pass
class gbind_simpleocl_IteratorExp(LoopExp):

    def __init__(self, name: str, LoopExp: "gbind_simpleocl_OclExpression" = None, LoopExp84: "gbind_simpleocl_Iterator" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class gbind_simpleocl_IterateExp(LoopExp):

    pass
class gbind_simpleocl_LocatedElement(ABC):

    def __init__(self, line: str, column: str, charStart: str, charEnd: str):
        self.line = line
        self.column = column
        self.charStart = charStart
        self.charEnd = charEnd
        
        pass
    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, line: str):
        self.__line = line


    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column


    @property
    def charStart(self):
        return self.__charStart

    @charStart.setter
    def charStart(self, charStart: str):
        self.__charStart = charStart


    @property
    def charEnd(self):
        return self.__charEnd

    @charEnd.setter
    def charEnd(self, charEnd: str):
        self.__charEnd = charEnd


class gbind_dsl_HelperParameter(VariableDeclaration):

    pass
class HelperParameter:

    pass
class gbind_dsl_BaseHelper:

    def __init__(self, feature: str, gbind_dsl_BaseHelper220: "OclType" = None, helpers: "BindingModel" = None, gbind_dsl_BaseHelper: "OclExpression" = None):
        self.feature = feature
        self.gbind_dsl_BaseHelper220 = gbind_dsl_BaseHelper220
        self.helpers = helpers
        self.gbind_dsl_BaseHelper = gbind_dsl_BaseHelper
        
        pass
    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature


    @property
    def helpers(self):
        return self.__helpers

    @helpers.setter
    def helpers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BaseHelper__helpers", None)
        self.__helpers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BindingModel223"):
                opp_val = getattr(old_value, "BindingModel223", None)
                if opp_val == self:
                    setattr(old_value, "BindingModel223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BindingModel223"):
                opp_val = getattr(value, "BindingModel223", None)
                setattr(value, "BindingModel223", self)

    @property
    def gbind_dsl_BaseHelper220(self):
        return self.__gbind_dsl_BaseHelper220

    @gbind_dsl_BaseHelper220.setter
    def gbind_dsl_BaseHelper220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BaseHelper__gbind_dsl_BaseHelper220", None)
        self.__gbind_dsl_BaseHelper220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType221"):
                opp_val = getattr(old_value, "OclType221", None)
                if opp_val == self:
                    setattr(old_value, "OclType221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType221"):
                opp_val = getattr(value, "OclType221", None)
                setattr(value, "OclType221", self)

    @property
    def gbind_dsl_BaseHelper(self):
        return self.__gbind_dsl_BaseHelper

    @gbind_dsl_BaseHelper.setter
    def gbind_dsl_BaseHelper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BaseHelper__gbind_dsl_BaseHelper", None)
        self.__gbind_dsl_BaseHelper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression218"):
                opp_val = getattr(old_value, "OclExpression218", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression218"):
                opp_val = getattr(value, "OclExpression218", None)
                setattr(value, "OclExpression218", self)

class gbind_dsl_BaseFeatureBinding(ConceptBinding):

    def __init__(self, conceptFeature: str, gbind_dsl_BaseFeatureBinding: "ConceptMetaclass" = None, gbind_dsl_BaseFeatureBinding213: "ConcreteMetaclass" = None, ConceptBinding: "gbind_dsl_BindingModel" = None):
        self.conceptFeature = conceptFeature
        self.gbind_dsl_BaseFeatureBinding = gbind_dsl_BaseFeatureBinding
        self.gbind_dsl_BaseFeatureBinding213 = gbind_dsl_BaseFeatureBinding213
        
        pass
    @property
    def conceptFeature(self):
        return self.__conceptFeature

    @conceptFeature.setter
    def conceptFeature(self, conceptFeature: str):
        self.__conceptFeature = conceptFeature


    @property
    def gbind_dsl_BaseFeatureBinding(self):
        return self.__gbind_dsl_BaseFeatureBinding

    @gbind_dsl_BaseFeatureBinding.setter
    def gbind_dsl_BaseFeatureBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BaseFeatureBinding__gbind_dsl_BaseFeatureBinding", None)
        self.__gbind_dsl_BaseFeatureBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass211"):
                opp_val = getattr(old_value, "ConceptMetaclass211", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass211"):
                opp_val = getattr(value, "ConceptMetaclass211", None)
                setattr(value, "ConceptMetaclass211", self)

    @property
    def gbind_dsl_BaseFeatureBinding213(self):
        return self.__gbind_dsl_BaseFeatureBinding213

    @gbind_dsl_BaseFeatureBinding213.setter
    def gbind_dsl_BaseFeatureBinding213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_BaseFeatureBinding__gbind_dsl_BaseFeatureBinding213", None)
        self.__gbind_dsl_BaseFeatureBinding213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConcreteMetaclass214"):
                opp_val = getattr(old_value, "ConcreteMetaclass214", None)
                if opp_val == self:
                    setattr(old_value, "ConcreteMetaclass214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConcreteMetaclass214"):
                opp_val = getattr(value, "ConcreteMetaclass214", None)
                setattr(value, "ConcreteMetaclass214", self)

class gbind_dsl_ConceptFeatureRef:

    def __init__(self, featureName: str, gbind_dsl_ConceptFeatureRef: "ConceptMetaclass" = None):
        self.featureName = featureName
        self.gbind_dsl_ConceptFeatureRef = gbind_dsl_ConceptFeatureRef
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def gbind_dsl_ConceptFeatureRef(self):
        return self.__gbind_dsl_ConceptFeatureRef

    @gbind_dsl_ConceptFeatureRef.setter
    def gbind_dsl_ConceptFeatureRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_ConceptFeatureRef__gbind_dsl_ConceptFeatureRef", None)
        self.__gbind_dsl_ConceptFeatureRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass209"):
                opp_val = getattr(old_value, "ConceptMetaclass209", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass209"):
                opp_val = getattr(value, "ConceptMetaclass209", None)
                setattr(value, "ConceptMetaclass209", self)

class ConceptFeatureRef:

    pass
class gbind_dsl_LocalHelper(BaseHelper):

    pass
class gbind_dsl_ConceptHelper(BaseHelper):

    pass
class gbind_dsl_VirtualFeature:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class VirtualAttribute:

    pass
class VirtualReference:

    pass
class gbind_dsl_VirtualMetaclass(Metaclass):

    pass
class gbind_dsl_ConcreteReferencDeclaringVar(VariableDeclaration):

    pass
class BaseFeatureBinding:

    pass
class gbind_dsl_OclFeatureBinding(BaseFeatureBinding):

    pass
class gbind_dsl_RenamingFeatureBinding(BaseFeatureBinding):

    def __init__(self, concreteFeature: str, BaseFeatureBinding: "gbind_dsl_IntermediateClassBinding" = None):
        self.concreteFeature = concreteFeature
        
        pass
    @property
    def concreteFeature(self):
        return self.__concreteFeature

    @concreteFeature.setter
    def concreteFeature(self, concreteFeature: str):
        self.__concreteFeature = concreteFeature


class ConcreteReferencDeclaringVar:

    pass
class gbind_dsl_IntermediateClassBinding(ConceptBinding):

    def __init__(self, conceptReferenceName: str, gbind_dsl_IntermediateClassBinding: "ConceptMetaclass" = None, gbind_dsl_IntermediateClassBinding183: "ConcreteMetaclass" = None, gbind_dsl_IntermediateClassBinding186: "ConcreteReferencDeclaringVar" = None, gbind_dsl_IntermediateClassBinding188: "ConceptMetaclass" = None, gbind_dsl_IntermediateClassBinding191: set["BaseFeatureBinding"] = None, ConceptBinding: "gbind_dsl_BindingModel" = None):
        self.conceptReferenceName = conceptReferenceName
        self.gbind_dsl_IntermediateClassBinding = gbind_dsl_IntermediateClassBinding
        self.gbind_dsl_IntermediateClassBinding183 = gbind_dsl_IntermediateClassBinding183
        self.gbind_dsl_IntermediateClassBinding186 = gbind_dsl_IntermediateClassBinding186
        self.gbind_dsl_IntermediateClassBinding188 = gbind_dsl_IntermediateClassBinding188
        self.gbind_dsl_IntermediateClassBinding191 = gbind_dsl_IntermediateClassBinding191 if gbind_dsl_IntermediateClassBinding191 is not None else set()
        
        pass
    @property
    def conceptReferenceName(self):
        return self.__conceptReferenceName

    @conceptReferenceName.setter
    def conceptReferenceName(self, conceptReferenceName: str):
        self.__conceptReferenceName = conceptReferenceName


    @property
    def gbind_dsl_IntermediateClassBinding(self):
        return self.__gbind_dsl_IntermediateClassBinding

    @gbind_dsl_IntermediateClassBinding.setter
    def gbind_dsl_IntermediateClassBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_IntermediateClassBinding__gbind_dsl_IntermediateClassBinding", None)
        self.__gbind_dsl_IntermediateClassBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass181"):
                opp_val = getattr(old_value, "ConceptMetaclass181", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass181"):
                opp_val = getattr(value, "ConceptMetaclass181", None)
                setattr(value, "ConceptMetaclass181", self)

    @property
    def gbind_dsl_IntermediateClassBinding183(self):
        return self.__gbind_dsl_IntermediateClassBinding183

    @gbind_dsl_IntermediateClassBinding183.setter
    def gbind_dsl_IntermediateClassBinding183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_IntermediateClassBinding__gbind_dsl_IntermediateClassBinding183", None)
        self.__gbind_dsl_IntermediateClassBinding183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConcreteMetaclass184"):
                opp_val = getattr(old_value, "ConcreteMetaclass184", None)
                if opp_val == self:
                    setattr(old_value, "ConcreteMetaclass184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConcreteMetaclass184"):
                opp_val = getattr(value, "ConcreteMetaclass184", None)
                setattr(value, "ConcreteMetaclass184", self)

    @property
    def gbind_dsl_IntermediateClassBinding186(self):
        return self.__gbind_dsl_IntermediateClassBinding186

    @gbind_dsl_IntermediateClassBinding186.setter
    def gbind_dsl_IntermediateClassBinding186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_IntermediateClassBinding__gbind_dsl_IntermediateClassBinding186", None)
        self.__gbind_dsl_IntermediateClassBinding186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConcreteReferencDeclaringVar"):
                opp_val = getattr(old_value, "ConcreteReferencDeclaringVar", None)
                if opp_val == self:
                    setattr(old_value, "ConcreteReferencDeclaringVar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConcreteReferencDeclaringVar"):
                opp_val = getattr(value, "ConcreteReferencDeclaringVar", None)
                setattr(value, "ConcreteReferencDeclaringVar", self)

    @property
    def gbind_dsl_IntermediateClassBinding191(self):
        return self.__gbind_dsl_IntermediateClassBinding191

    @gbind_dsl_IntermediateClassBinding191.setter
    def gbind_dsl_IntermediateClassBinding191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_IntermediateClassBinding__gbind_dsl_IntermediateClassBinding191", None)
        self.__gbind_dsl_IntermediateClassBinding191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseFeatureBinding"):
                    opp_val = getattr(item, "BaseFeatureBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseFeatureBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseFeatureBinding"):
                    opp_val = getattr(item, "BaseFeatureBinding", None)
                    
                    setattr(item, "BaseFeatureBinding", self)
                    

    @property
    def gbind_dsl_IntermediateClassBinding188(self):
        return self.__gbind_dsl_IntermediateClassBinding188

    @gbind_dsl_IntermediateClassBinding188.setter
    def gbind_dsl_IntermediateClassBinding188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gbind_dsl_IntermediateClassBinding__gbind_dsl_IntermediateClassBinding188", None)
        self.__gbind_dsl_IntermediateClassBinding188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConceptMetaclass189"):
                opp_val = getattr(old_value, "ConceptMetaclass189", None)
                if opp_val == self:
                    setattr(old_value, "ConceptMetaclass189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConceptMetaclass189"):
                opp_val = getattr(value, "ConceptMetaclass189", None)
                setattr(value, "ConceptMetaclass189", self)
