from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclFeature:

    pass
class OclModel:

    pass
class simpleocl_OclInstanceModel(OclModel):

    pass
class ModuleElement:

    pass
class simpleocl_OclFeatureDefinition(ModuleElement):

    def __init__(self, static: str, OclFeatureDefinition: "simpleocl_OclContextDefinition" = None, definition: "simpleocl_OclFeature" = None, definition135: "simpleocl_OclContextDefinition" = None, OclFeatureDefinition142: "simpleocl_OclFeature" = None):
        self.static = static
        self.OclFeatureDefinition = OclFeatureDefinition
        self.definition = definition
        self.definition135 = definition135
        self.OclFeatureDefinition142 = OclFeatureDefinition142
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def OclFeatureDefinition(self):
        return self.__OclFeatureDefinition

    @OclFeatureDefinition.setter
    def OclFeatureDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclFeatureDefinition__OclFeatureDefinition", None)
        self.__OclFeatureDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "context_138"):
                opp_val = getattr(old_value, "context_138", None)
                if opp_val == self:
                    setattr(old_value, "context_138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "context_138"):
                opp_val = getattr(value, "context_138", None)
                setattr(value, "context_138", self)

    @property
    def OclFeatureDefinition142(self):
        return self.__OclFeatureDefinition142

    @OclFeatureDefinition142.setter
    def OclFeatureDefinition142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclFeatureDefinition__OclFeatureDefinition142", None)
        self.__OclFeatureDefinition142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature"):
                opp_val = getattr(old_value, "feature", None)
                if opp_val == self:
                    setattr(old_value, "feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature"):
                opp_val = getattr(value, "feature", None)
                setattr(value, "feature", self)

    @property
    def definition135(self):
        return self.__definition135

    @definition135.setter
    def definition135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclFeatureDefinition__definition135", None)
        self.__definition135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclContextDefinition136"):
                opp_val = getattr(old_value, "OclContextDefinition136", None)
                if opp_val == self:
                    setattr(old_value, "OclContextDefinition136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclContextDefinition136"):
                opp_val = getattr(value, "OclContextDefinition136", None)
                setattr(value, "OclContextDefinition136", self)

    @property
    def definition(self):
        return self.__definition

    @definition.setter
    def definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclFeatureDefinition__definition", None)
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

class CollectionType:

    pass
class simpleocl_OrderedSetType(CollectionType):

    pass
class simpleocl_SequenceType(CollectionType):

    pass
class simpleocl_SetType(CollectionType):

    pass
class simpleocl_BagType(CollectionType):

    pass
class NumericType:

    pass
class simpleocl_RealType(NumericType):

    pass
class simpleocl_IntegerType(NumericType):

    pass
class Primitive:

    pass
class simpleocl_NumericType(Primitive):

    pass
class simpleocl_BooleanType(Primitive):

    pass
class simpleocl_StringType(Primitive):

    pass
class OclType:

    pass
class simpleocl_OclAnyType(OclType):

    pass
class simpleocl_EnvType(OclType):

    pass
class simpleocl_OclModelElement(OclType):

    pass
class simpleocl_MapType(OclType):

    pass
class simpleocl_LambdaType(OclType):

    pass
class simpleocl_TupleType(OclType):

    pass
class simpleocl_Primitive(OclType):

    pass
class simpleocl_CollectionType(OclType):

    pass
class VariableDeclaration:

    pass
class simpleocl_Parameter(VariableDeclaration):

    pass
class LoopExp:

    pass
class simpleocl_IteratorExp(LoopExp):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simpleocl_IterateExp(LoopExp):

    pass
class simpleocl_Iterator(VariableDeclaration):

    pass
class OperationCall:

    pass
class simpleocl_CollectionOperationCall(OperationCall):

    pass
class VariableExp:

    pass
class simpleocl_LambdaCallExp(VariableExp):

    pass
class OperatorCallExp:

    pass
class simpleocl_MulOpCallExp(OperatorCallExp):

    pass
class simpleocl_IntOpCallExp(OperatorCallExp):

    pass
class simpleocl_RelOpCallExp(OperatorCallExp):

    pass
class simpleocl_EqOpCallExp(OperatorCallExp):

    pass
class simpleocl_AddOpCallExp(OperatorCallExp):

    pass
class PropertyCall:

    pass
class simpleocl_NavigationOrAttributeCall(PropertyCall):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simpleocl_NotOpCallExp(OperatorCallExp):

    pass
class LocalVariable:

    pass
class StaticPropertyCall:

    pass
class simpleocl_StaticOperationCall(StaticPropertyCall):

    def __init__(self, operationName: str, simpleocl_StaticOperationCall: set["simpleocl_OclExpression"] = None):
        self.operationName = operationName
        self.simpleocl_StaticOperationCall = simpleocl_StaticOperationCall if simpleocl_StaticOperationCall is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def simpleocl_StaticOperationCall(self):
        return self.__simpleocl_StaticOperationCall

    @simpleocl_StaticOperationCall.setter
    def simpleocl_StaticOperationCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_StaticOperationCall__simpleocl_StaticOperationCall", None)
        self.__simpleocl_StaticOperationCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleocl_OclExpression48"):
                    opp_val = getattr(item, "simpleocl_OclExpression48", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleocl_OclExpression48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleocl_OclExpression48"):
                    opp_val = getattr(item, "simpleocl_OclExpression48", None)
                    
                    setattr(item, "simpleocl_OclExpression48", self)
                    

class simpleocl_StaticNavigationOrAttributeCall(StaticPropertyCall):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NumericExp:

    pass
class simpleocl_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class simpleocl_TuplePart(LocalVariable):

    pass
class PrimitiveExp:

    pass
class simpleocl_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class simpleocl_NumericExp(PrimitiveExp):

    pass
class simpleocl_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class CollectionExp:

    pass
class simpleocl_SetExp(CollectionExp):

    pass
class simpleocl_SequenceExp(CollectionExp):

    pass
class simpleocl_OrderedSetExp(CollectionExp):

    pass
class simpleocl_BagExp(CollectionExp):

    pass
class OclExpression:

    pass
class simpleocl_MapExp(OclExpression):

    pass
class simpleocl_PrimitiveExp(OclExpression):

    pass
class simpleocl_BraceExp(OclExpression):

    pass
class simpleocl_TupleExp(OclExpression):

    pass
class simpleocl_SuperExp(OclExpression):

    pass
class simpleocl_OclModelElementExp(OclExpression):

    def __init__(self, name: str, simpleocl_OclModelElementExp: "simpleocl_OclModel" = None):
        self.name = name
        self.simpleocl_OclModelElementExp = simpleocl_OclModelElementExp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleocl_OclModelElementExp(self):
        return self.__simpleocl_OclModelElementExp

    @simpleocl_OclModelElementExp.setter
    def simpleocl_OclModelElementExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclModelElementExp__simpleocl_OclModelElementExp", None)
        self.__simpleocl_OclModelElementExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl_OclModel"):
                opp_val = getattr(old_value, "simpleocl_OclModel", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl_OclModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl_OclModel"):
                opp_val = getattr(value, "simpleocl_OclModel", None)
                setattr(value, "simpleocl_OclModel", self)

class simpleocl_StaticPropertyCallExp(OclExpression):

    pass
class simpleocl_OclUndefinedExp(OclExpression):

    pass
class simpleocl_EnumLiteralExp(OclExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simpleocl_SelfExp(OclExpression):

    pass
class simpleocl_EnvExp(OclExpression):

    pass
class simpleocl_VariableExp(OclExpression):

    pass
class simpleocl_OperatorCallExp(OclExpression):

    def __init__(self, operationName: str, OperatorCallExp: "simpleocl_OclExpression" = None, appliedOperator: "simpleocl_OclExpression" = None, simpleocl_OperatorCallExp: "simpleocl_OclExpression" = None):
        self.operationName = operationName
        self.OperatorCallExp = OperatorCallExp
        self.appliedOperator = appliedOperator
        self.simpleocl_OperatorCallExp = simpleocl_OperatorCallExp
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def simpleocl_OperatorCallExp(self):
        return self.__simpleocl_OperatorCallExp

    @simpleocl_OperatorCallExp.setter
    def simpleocl_OperatorCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OperatorCallExp__simpleocl_OperatorCallExp", None)
        self.__simpleocl_OperatorCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl_OclExpression56"):
                opp_val = getattr(old_value, "simpleocl_OclExpression56", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl_OclExpression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl_OclExpression56"):
                opp_val = getattr(value, "simpleocl_OclExpression56", None)
                setattr(value, "simpleocl_OclExpression56", self)

    @property
    def OperatorCallExp(self):
        return self.__OperatorCallExp

    @OperatorCallExp.setter
    def OperatorCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OperatorCallExp__OperatorCallExp", None)
        self.__OperatorCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source23"):
                opp_val = getattr(old_value, "source23", None)
                if opp_val == self:
                    setattr(old_value, "source23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source23"):
                opp_val = getattr(value, "source23", None)
                setattr(value, "source23", self)

    @property
    def appliedOperator(self):
        return self.__appliedOperator

    @appliedOperator.setter
    def appliedOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OperatorCallExp__appliedOperator", None)
        self.__appliedOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression58"):
                opp_val = getattr(old_value, "OclExpression58", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression58"):
                opp_val = getattr(value, "OclExpression58", None)
                setattr(value, "OclExpression58", self)

class simpleocl_Attribute(OclFeature):

    pass
class CollectionPart:

    pass
class simpleocl_CollectionItem(CollectionPart):

    pass
class simpleocl_CollectionRange(CollectionPart):

    pass
class simpleocl_CollectionExp(OclExpression):

    pass
class simpleocl_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class simpleocl_LoopExp(PropertyCall):

    pass
class simpleocl_LetExp(OclExpression):

    pass
class simpleocl_PropertyCallExp(OclExpression):

    pass
class simpleocl_IfExp(OclExpression):

    pass
class simpleocl_OclMetamodel(OclModel):

    def __init__(self, uri: str, simpleocl_OclMetamodel: "simpleocl_Module" = None, metamodel: set["simpleocl_OclInstanceModel"] = None, OclMetamodel: "simpleocl_OclInstanceModel" = None):
        self.uri = uri
        self.simpleocl_OclMetamodel = simpleocl_OclMetamodel
        self.metamodel = metamodel if metamodel is not None else set()
        self.OclMetamodel = OclMetamodel
        
    @property
    def uri(self) -> str:
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
        old_value = getattr(self, f"_simpleocl_OclMetamodel__metamodel", None)
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
                    

    @property
    def simpleocl_OclMetamodel(self):
        return self.__simpleocl_OclMetamodel

    @simpleocl_OclMetamodel.setter
    def simpleocl_OclMetamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclMetamodel__simpleocl_OclMetamodel", None)
        self.__simpleocl_OclMetamodel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleocl_Module"):
                opp_val = getattr(old_value, "simpleocl_Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl_Module"):
                opp_val = getattr(value, "simpleocl_Module", None)
                if opp_val is None:
                    setattr(value, "simpleocl_Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OclMetamodel(self):
        return self.__OclMetamodel

    @OclMetamodel.setter
    def OclMetamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclMetamodel__OclMetamodel", None)
        self.__OclMetamodel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model156"):
                opp_val = getattr(old_value, "model156", None)
                if opp_val == self:
                    setattr(old_value, "model156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model156"):
                opp_val = getattr(value, "model156", None)
                setattr(value, "model156", self)

class simpleocl_Operation(OclFeature):

    pass
class NamedElement:

    pass
class simpleocl_OclFeature(NamedElement):

    def __init__(self, eq: str, OclFeature: "simpleocl_OclFeatureDefinition" = None, feature: "simpleocl_OclFeatureDefinition" = None):
        self.eq = eq
        self.OclFeature = OclFeature
        self.feature = feature
        
    @property
    def eq(self) -> str:
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
        old_value = getattr(self, f"_simpleocl_OclFeature__feature", None)
        self.__feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclFeatureDefinition142"):
                opp_val = getattr(old_value, "OclFeatureDefinition142", None)
                if opp_val == self:
                    setattr(old_value, "OclFeatureDefinition142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclFeatureDefinition142"):
                opp_val = getattr(value, "OclFeatureDefinition142", None)
                setattr(value, "OclFeatureDefinition142", self)

    @property
    def OclFeature(self):
        return self.__OclFeature

    @OclFeature.setter
    def OclFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclFeature__OclFeature", None)
        self.__OclFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "definition"):
                opp_val = getattr(old_value, "definition", None)
                if opp_val == self:
                    setattr(old_value, "definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "definition"):
                opp_val = getattr(value, "definition", None)
                setattr(value, "definition", self)

class simpleocl_Import(NamedElement):

    pass
class simpleocl_OclModel(NamedElement):

    pass
class simpleocl_Module(NamedElement):

    pass
class simpleocl_LocalVariable(VariableDeclaration):

    def __init__(self, eq: str, LocalVariable: "simpleocl_OclExpression" = None, LocalVariable69: "simpleocl_LetExp" = None, LocalVariable67: "simpleocl_IterateExp" = None, result: "simpleocl_IterateExp" = None, variable: "simpleocl_LetExp" = None, initializedVariable: "simpleocl_OclExpression" = None):
        self.eq = eq
        self.LocalVariable = LocalVariable
        self.LocalVariable69 = LocalVariable69
        self.LocalVariable67 = LocalVariable67
        self.result = result
        self.variable = variable
        self.initializedVariable = initializedVariable
        
    @property
    def eq(self) -> str:
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq

    @property
    def LocalVariable69(self):
        return self.__LocalVariable69

    @LocalVariable69.setter
    def LocalVariable69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_LocalVariable__LocalVariable69", None)
        self.__LocalVariable69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "letExp"):
                opp_val = getattr(old_value, "letExp", None)
                if opp_val == self:
                    setattr(old_value, "letExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "letExp"):
                opp_val = getattr(value, "letExp", None)
                setattr(value, "letExp", self)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_LocalVariable__result", None)
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
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_LocalVariable__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp83"):
                opp_val = getattr(old_value, "LetExp83", None)
                if opp_val == self:
                    setattr(old_value, "LetExp83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp83"):
                opp_val = getattr(value, "LetExp83", None)
                setattr(value, "LetExp83", self)

    @property
    def LocalVariable(self):
        return self.__LocalVariable

    @LocalVariable.setter
    def LocalVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_LocalVariable__LocalVariable", None)
        self.__LocalVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "initExpression"):
                opp_val = getattr(old_value, "initExpression", None)
                if opp_val == self:
                    setattr(old_value, "initExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "initExpression"):
                opp_val = getattr(value, "initExpression", None)
                setattr(value, "initExpression", self)

    @property
    def initializedVariable(self):
        return self.__initializedVariable

    @initializedVariable.setter
    def initializedVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_LocalVariable__initializedVariable", None)
        self.__initializedVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression85"):
                opp_val = getattr(old_value, "OclExpression85", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression85"):
                opp_val = getattr(value, "OclExpression85", None)
                setattr(value, "OclExpression85", self)

    @property
    def LocalVariable67(self):
        return self.__LocalVariable67

    @LocalVariable67.setter
    def LocalVariable67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_LocalVariable__LocalVariable67", None)
        self.__LocalVariable67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseExp"):
                opp_val = getattr(old_value, "baseExp", None)
                if opp_val == self:
                    setattr(old_value, "baseExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseExp"):
                opp_val = getattr(value, "baseExp", None)
                setattr(value, "baseExp", self)

class LocatedElement:

    pass
class simpleocl_OclType(LocatedElement):

    def __init__(self, name: str, OclType: "simpleocl_OclExpression" = None, OclType44: "simpleocl_StaticPropertyCallExp" = None, OclType80: "simpleocl_VariableDeclaration" = None, type106: "simpleocl_TupleTypeAttribute" = None, type108: "simpleocl_VariableDeclaration" = None, OclType92: "simpleocl_CollectionType" = None, context_: "simpleocl_OclContextDefinition" = None, type: "simpleocl_OclExpression" = None, returnType: "simpleocl_Operation" = None, valueType: "simpleocl_MapType" = None, type100: "simpleocl_Attribute" = None, keyType: "simpleocl_MapType" = None, elementType: "simpleocl_CollectionType" = None, OclType121: "simpleocl_TupleTypeAttribute" = None, returnType111: "simpleocl_LambdaType" = None, argumentTypes: "simpleocl_LambdaType" = None, source115: "simpleocl_StaticPropertyCallExp" = None, OclType140: "simpleocl_OclContextDefinition" = None, OclType126: "simpleocl_MapType" = None, OclType128: "simpleocl_MapType" = None, OclType130: "simpleocl_LambdaType" = None, OclType132: "simpleocl_LambdaType" = None, OclType146: "simpleocl_Attribute" = None, OclType150: "simpleocl_Operation" = None):
        self.name = name
        self.OclType = OclType
        self.OclType44 = OclType44
        self.OclType80 = OclType80
        self.type106 = type106
        self.type108 = type108
        self.OclType92 = OclType92
        self.context_ = context_
        self.type = type
        self.returnType = returnType
        self.valueType = valueType
        self.type100 = type100
        self.keyType = keyType
        self.elementType = elementType
        self.OclType121 = OclType121
        self.returnType111 = returnType111
        self.argumentTypes = argumentTypes
        self.source115 = source115
        self.OclType140 = OclType140
        self.OclType126 = OclType126
        self.OclType128 = OclType128
        self.OclType130 = OclType130
        self.OclType132 = OclType132
        self.OclType146 = OclType146
        self.OclType150 = OclType150
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation97"):
                opp_val = getattr(old_value, "Operation97", None)
                if opp_val == self:
                    setattr(old_value, "Operation97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation97"):
                opp_val = getattr(value, "Operation97", None)
                setattr(value, "Operation97", self)

    @property
    def elementType(self):
        return self.__elementType

    @elementType.setter
    def elementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__elementType", None)
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

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression95"):
                opp_val = getattr(old_value, "OclExpression95", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression95"):
                opp_val = getattr(value, "OclExpression95", None)
                setattr(value, "OclExpression95", self)

    @property
    def type108(self):
        return self.__type108

    @type108.setter
    def type108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__type108", None)
        self.__type108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration109"):
                opp_val = getattr(old_value, "VariableDeclaration109", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration109"):
                opp_val = getattr(value, "VariableDeclaration109", None)
                setattr(value, "VariableDeclaration109", self)

    @property
    def OclType150(self):
        return self.__OclType150

    @OclType150.setter
    def OclType150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType150", None)
        self.__OclType150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation149"):
                opp_val = getattr(old_value, "operation149", None)
                if opp_val == self:
                    setattr(old_value, "operation149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation149"):
                opp_val = getattr(value, "operation149", None)
                setattr(value, "operation149", self)

    @property
    def OclType44(self):
        return self.__OclType44

    @OclType44.setter
    def OclType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType44", None)
        self.__OclType44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staticPropertyCall"):
                opp_val = getattr(old_value, "staticPropertyCall", None)
                if opp_val == self:
                    setattr(old_value, "staticPropertyCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staticPropertyCall"):
                opp_val = getattr(value, "staticPropertyCall", None)
                setattr(value, "staticPropertyCall", self)

    @property
    def argumentTypes(self):
        return self.__argumentTypes

    @argumentTypes.setter
    def argumentTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__argumentTypes", None)
        self.__argumentTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LambdaType113"):
                opp_val = getattr(old_value, "LambdaType113", None)
                if opp_val == self:
                    setattr(old_value, "LambdaType113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LambdaType113"):
                opp_val = getattr(value, "LambdaType113", None)
                setattr(value, "LambdaType113", self)

    @property
    def OclType128(self):
        return self.__OclType128

    @OclType128.setter
    def OclType128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType128", None)
        self.__OclType128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapType"):
                opp_val = getattr(old_value, "mapType", None)
                if opp_val == self:
                    setattr(old_value, "mapType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapType"):
                opp_val = getattr(value, "mapType", None)
                setattr(value, "mapType", self)

    @property
    def OclType92(self):
        return self.__OclType92

    @OclType92.setter
    def OclType92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType92", None)
        self.__OclType92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "collectionTypes"):
                opp_val = getattr(old_value, "collectionTypes", None)
                if opp_val == self:
                    setattr(old_value, "collectionTypes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "collectionTypes"):
                opp_val = getattr(value, "collectionTypes", None)
                setattr(value, "collectionTypes", self)

    @property
    def context_(self):
        return self.__context_

    @context_.setter
    def context_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__context_", None)
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
    def OclType130(self):
        return self.__OclType130

    @OclType130.setter
    def OclType130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType130", None)
        self.__OclType130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lambdaReturnType"):
                opp_val = getattr(old_value, "lambdaReturnType", None)
                if opp_val == self:
                    setattr(old_value, "lambdaReturnType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lambdaReturnType"):
                opp_val = getattr(value, "lambdaReturnType", None)
                setattr(value, "lambdaReturnType", self)

    @property
    def OclType121(self):
        return self.__OclType121

    @OclType121.setter
    def OclType121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType121", None)
        self.__OclType121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tupleTypeAttribute"):
                opp_val = getattr(old_value, "tupleTypeAttribute", None)
                if opp_val == self:
                    setattr(old_value, "tupleTypeAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tupleTypeAttribute"):
                opp_val = getattr(value, "tupleTypeAttribute", None)
                setattr(value, "tupleTypeAttribute", self)

    @property
    def OclType(self):
        return self.__OclType

    @OclType.setter
    def OclType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType", None)
        self.__OclType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclExpression"):
                opp_val = getattr(old_value, "oclExpression", None)
                if opp_val == self:
                    setattr(old_value, "oclExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclExpression"):
                opp_val = getattr(value, "oclExpression", None)
                setattr(value, "oclExpression", self)

    @property
    def OclType80(self):
        return self.__OclType80

    @OclType80.setter
    def OclType80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType80", None)
        self.__OclType80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variableDeclaration"):
                opp_val = getattr(old_value, "variableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "variableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variableDeclaration"):
                opp_val = getattr(value, "variableDeclaration", None)
                setattr(value, "variableDeclaration", self)

    @property
    def type106(self):
        return self.__type106

    @type106.setter
    def type106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__type106", None)
        self.__type106 = value
        
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
    def returnType111(self):
        return self.__returnType111

    @returnType111.setter
    def returnType111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__returnType111", None)
        self.__returnType111 = value
        
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
    def source115(self):
        return self.__source115

    @source115.setter
    def source115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__source115", None)
        self.__source115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StaticPropertyCallExp116"):
                opp_val = getattr(old_value, "StaticPropertyCallExp116", None)
                if opp_val == self:
                    setattr(old_value, "StaticPropertyCallExp116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StaticPropertyCallExp116"):
                opp_val = getattr(value, "StaticPropertyCallExp116", None)
                setattr(value, "StaticPropertyCallExp116", self)

    @property
    def valueType(self):
        return self.__valueType

    @valueType.setter
    def valueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__valueType", None)
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
    def OclType140(self):
        return self.__OclType140

    @OclType140.setter
    def OclType140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType140", None)
        self.__OclType140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "definitions"):
                opp_val = getattr(old_value, "definitions", None)
                if opp_val == self:
                    setattr(old_value, "definitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "definitions"):
                opp_val = getattr(value, "definitions", None)
                setattr(value, "definitions", self)

    @property
    def OclType146(self):
        return self.__OclType146

    @OclType146.setter
    def OclType146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType146", None)
        self.__OclType146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attribute"):
                opp_val = getattr(old_value, "attribute", None)
                if opp_val == self:
                    setattr(old_value, "attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attribute"):
                opp_val = getattr(value, "attribute", None)
                setattr(value, "attribute", self)

    @property
    def OclType126(self):
        return self.__OclType126

    @OclType126.setter
    def OclType126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType126", None)
        self.__OclType126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapType2"):
                opp_val = getattr(old_value, "mapType2", None)
                if opp_val == self:
                    setattr(old_value, "mapType2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapType2"):
                opp_val = getattr(value, "mapType2", None)
                setattr(value, "mapType2", self)

    @property
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__keyType", None)
        self.__keyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType103"):
                opp_val = getattr(old_value, "MapType103", None)
                if opp_val == self:
                    setattr(old_value, "MapType103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType103"):
                opp_val = getattr(value, "MapType103", None)
                setattr(value, "MapType103", self)

    @property
    def type100(self):
        return self.__type100

    @type100.setter
    def type100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__type100", None)
        self.__type100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute101"):
                opp_val = getattr(old_value, "Attribute101", None)
                if opp_val == self:
                    setattr(old_value, "Attribute101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute101"):
                opp_val = getattr(value, "Attribute101", None)
                setattr(value, "Attribute101", self)

    @property
    def OclType132(self):
        return self.__OclType132

    @OclType132.setter
    def OclType132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType132", None)
        self.__OclType132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lambdaArgType"):
                opp_val = getattr(old_value, "lambdaArgType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lambdaArgType"):
                opp_val = getattr(value, "lambdaArgType", None)
                if opp_val is None:
                    setattr(value, "lambdaArgType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleocl_StaticPropertyCall(LocatedElement):

    pass
class simpleocl_MapElement(LocatedElement):

    pass
class simpleocl_PropertyCall(LocatedElement):

    pass
class simpleocl_CollectionPart(LocatedElement):

    pass
class simpleocl_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, TupleTypeAttribute: "simpleocl_OclType" = None, tupleTypeAttribute: "simpleocl_OclType" = None, TupleTypeAttribute119: "simpleocl_TupleType" = None, attributes: "simpleocl_TupleType" = None):
        self.name = name
        self.TupleTypeAttribute = TupleTypeAttribute
        self.tupleTypeAttribute = tupleTypeAttribute
        self.TupleTypeAttribute119 = TupleTypeAttribute119
        self.attributes = attributes
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TupleTypeAttribute119(self):
        return self.__TupleTypeAttribute119

    @TupleTypeAttribute119.setter
    def TupleTypeAttribute119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_TupleTypeAttribute__TupleTypeAttribute119", None)
        self.__TupleTypeAttribute119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tupleType"):
                opp_val = getattr(old_value, "tupleType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tupleType"):
                opp_val = getattr(value, "tupleType", None)
                if opp_val is None:
                    setattr(value, "tupleType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TupleTypeAttribute(self):
        return self.__TupleTypeAttribute

    @TupleTypeAttribute.setter
    def TupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_TupleTypeAttribute__TupleTypeAttribute", None)
        self.__TupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type106"):
                opp_val = getattr(old_value, "type106", None)
                if opp_val == self:
                    setattr(old_value, "type106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type106"):
                opp_val = getattr(value, "type106", None)
                setattr(value, "type106", self)

    @property
    def tupleTypeAttribute(self):
        return self.__tupleTypeAttribute

    @tupleTypeAttribute.setter
    def tupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_TupleTypeAttribute__tupleTypeAttribute", None)
        self.__tupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType121"):
                opp_val = getattr(old_value, "OclType121", None)
                if opp_val == self:
                    setattr(old_value, "OclType121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType121"):
                opp_val = getattr(value, "OclType121", None)
                setattr(value, "OclType121", self)

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_TupleTypeAttribute__attributes", None)
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

class simpleocl_VariableDeclaration(LocatedElement):

    def __init__(self, varName: str, VariableDeclaration: "simpleocl_VariableExp" = None, variableDeclaration: "simpleocl_OclType" = None, referredVariable: set["simpleocl_VariableExp"] = None, VariableDeclaration109: "simpleocl_OclType" = None):
        self.varName = varName
        self.VariableDeclaration = VariableDeclaration
        self.variableDeclaration = variableDeclaration
        self.referredVariable = referredVariable if referredVariable is not None else set()
        self.VariableDeclaration109 = VariableDeclaration109
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def VariableDeclaration(self):
        return self.__VariableDeclaration

    @VariableDeclaration.setter
    def VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_VariableDeclaration__VariableDeclaration", None)
        self.__VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variableExp"):
                opp_val = getattr(old_value, "variableExp", None)
                if opp_val == self:
                    setattr(old_value, "variableExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variableExp"):
                opp_val = getattr(value, "variableExp", None)
                setattr(value, "variableExp", self)

    @property
    def VariableDeclaration109(self):
        return self.__VariableDeclaration109

    @VariableDeclaration109.setter
    def VariableDeclaration109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_VariableDeclaration__VariableDeclaration109", None)
        self.__VariableDeclaration109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type108"):
                opp_val = getattr(old_value, "type108", None)
                if opp_val == self:
                    setattr(old_value, "type108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type108"):
                opp_val = getattr(value, "type108", None)
                setattr(value, "type108", self)

    @property
    def referredVariable(self):
        return self.__referredVariable

    @referredVariable.setter
    def referredVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_VariableDeclaration__referredVariable", None)
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
                    

    @property
    def variableDeclaration(self):
        return self.__variableDeclaration

    @variableDeclaration.setter
    def variableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_VariableDeclaration__variableDeclaration", None)
        self.__variableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType80"):
                opp_val = getattr(old_value, "OclType80", None)
                if opp_val == self:
                    setattr(old_value, "OclType80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType80"):
                opp_val = getattr(value, "OclType80", None)
                setattr(value, "OclType80", self)

class simpleocl_OclContextDefinition(LocatedElement):

    pass
class simpleocl_ModuleElement(LocatedElement):

    pass
class simpleocl_OclExpression(LocatedElement):

    pass
class simpleocl_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simpleocl_OperationCall(PropertyCall):

    def __init__(self, operationName: str, OperationCall: "simpleocl_OclExpression" = None, parentOperation: set["simpleocl_OclExpression"] = None):
        self.operationName = operationName
        self.OperationCall = OperationCall
        self.parentOperation = parentOperation if parentOperation is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def OperationCall(self):
        return self.__OperationCall

    @OperationCall.setter
    def OperationCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OperationCall__OperationCall", None)
        self.__OperationCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arguments"):
                opp_val = getattr(old_value, "arguments", None)
                if opp_val == self:
                    setattr(old_value, "arguments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arguments"):
                opp_val = getattr(value, "arguments", None)
                setattr(value, "arguments", self)

    @property
    def parentOperation(self):
        return self.__parentOperation

    @parentOperation.setter
    def parentOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OperationCall__parentOperation", None)
        self.__parentOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression54"):
                    opp_val = getattr(item, "OclExpression54", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression54"):
                    opp_val = getattr(item, "OclExpression54", None)
                    
                    setattr(item, "OclExpression54", self)
                    

class simpleocl_LocatedElement(ABC):

    def __init__(self, line: str, charStart: str, charEnd: str, column: str):
        self.line = line
        self.charStart = charStart
        self.charEnd = charEnd
        self.column = column
        
    @property
    def charEnd(self) -> str:
        return self.__charEnd

    @charEnd.setter
    def charEnd(self, charEnd: str):
        self.__charEnd = charEnd

    @property
    def line(self) -> str:
        return self.__line

    @line.setter
    def line(self, line: str):
        self.__line = line

    @property
    def charStart(self) -> str:
        return self.__charStart

    @charStart.setter
    def charStart(self, charStart: str):
        self.__charStart = charStart

    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column
