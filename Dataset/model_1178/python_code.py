from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclModel:

    pass
class simpleocl_OclInstanceModel(OclModel):

    pass
class ModuleElement:

    pass
class simpleocl_OclFeatureDefinition(ModuleElement):

    def __init__(self, static: str, definition130: "simpleocl_OclContextDefinition" = None, OclFeatureDefinition: "simpleocl_OclContextDefinition" = None, OclFeatureDefinition137: "simpleocl_OclFeature" = None, definition: "simpleocl_OclFeature" = None):
        self.static = static
        self.definition130 = definition130
        self.OclFeatureDefinition = OclFeatureDefinition
        self.OclFeatureDefinition137 = OclFeatureDefinition137
        self.definition = definition
        
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
            if hasattr(old_value, "context_133"):
                opp_val = getattr(old_value, "context_133", None)
                if opp_val == self:
                    setattr(old_value, "context_133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "context_133"):
                opp_val = getattr(value, "context_133", None)
                setattr(value, "context_133", self)

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

    @property
    def OclFeatureDefinition137(self):
        return self.__OclFeatureDefinition137

    @OclFeatureDefinition137.setter
    def OclFeatureDefinition137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclFeatureDefinition__OclFeatureDefinition137", None)
        self.__OclFeatureDefinition137 = value
        
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
    def definition130(self):
        return self.__definition130

    @definition130.setter
    def definition130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclFeatureDefinition__definition130", None)
        self.__definition130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclContextDefinition131"):
                opp_val = getattr(old_value, "OclContextDefinition131", None)
                if opp_val == self:
                    setattr(old_value, "OclContextDefinition131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclContextDefinition131"):
                opp_val = getattr(value, "OclContextDefinition131", None)
                setattr(value, "OclContextDefinition131", self)

class OclFeature:

    pass
class CollectionType:

    pass
class simpleocl_OrderedSetType(CollectionType):

    pass
class simpleocl_SequenceType(CollectionType):

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
class simpleocl_SetType(CollectionType):

    pass
class OclType:

    pass
class simpleocl_TupleType(OclType):

    pass
class simpleocl_OclModelElement(OclType):

    pass
class simpleocl_Primitive(OclType):

    pass
class simpleocl_OclAnyType(OclType):

    pass
class simpleocl_EnvType(OclType):

    pass
class simpleocl_CollectionType(OclType):

    pass
class simpleocl_LambdaType(OclType):

    pass
class simpleocl_MapType(OclType):

    pass
class VariableDeclaration:

    pass
class simpleocl_Parameter(VariableDeclaration):

    pass
class VariableExp:

    pass
class simpleocl_LambdaCallExp(VariableExp):

    pass
class OperatorCallExp:

    pass
class simpleocl_EqOpCallExp(OperatorCallExp):

    pass
class simpleocl_AddOpCallExp(OperatorCallExp):

    pass
class simpleocl_RelOpCallExp(OperatorCallExp):

    pass
class simpleocl_IntOpCallExp(OperatorCallExp):

    pass
class simpleocl_MulOpCallExp(OperatorCallExp):

    pass
class simpleocl_NotOpCallExp(OperatorCallExp):

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
                if hasattr(item, "simpleocl_OclExpression42"):
                    opp_val = getattr(item, "simpleocl_OclExpression42", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleocl_OclExpression42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleocl_OclExpression42"):
                    opp_val = getattr(item, "simpleocl_OclExpression42", None)
                    
                    setattr(item, "simpleocl_OclExpression42", self)
                    

class simpleocl_StaticNavigationOrAttributeCall(StaticPropertyCall):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class LocalVariable:

    pass
class simpleocl_Attribute(OclFeature):

    pass
class simpleocl_TuplePart(LocalVariable):

    pass
class CollectionExp:

    pass
class simpleocl_SequenceExp(CollectionExp):

    pass
class simpleocl_SetExp(CollectionExp):

    pass
class simpleocl_OrderedSetExp(CollectionExp):

    pass
class simpleocl_BagExp(CollectionExp):

    pass
class NumericExp:

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

class simpleocl_RealExp(NumericExp):

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

class OclExpression:

    pass
class simpleocl_SuperExp(OclExpression):

    pass
class simpleocl_MapExp(OclExpression):

    pass
class simpleocl_EnvExp(OclExpression):

    pass
class simpleocl_OperatorCallExp(OclExpression):

    def __init__(self, operationName: str, OperatorCallExp: "simpleocl_OclExpression" = None, simpleocl_OperatorCallExp: "simpleocl_OclExpression" = None, appliedOperator: "simpleocl_OclExpression" = None):
        self.operationName = operationName
        self.OperatorCallExp = OperatorCallExp
        self.simpleocl_OperatorCallExp = simpleocl_OperatorCallExp
        self.appliedOperator = appliedOperator
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

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
            if hasattr(old_value, "source25"):
                opp_val = getattr(old_value, "source25", None)
                if opp_val == self:
                    setattr(old_value, "source25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source25"):
                opp_val = getattr(value, "source25", None)
                setattr(value, "source25", self)

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
            if hasattr(old_value, "simpleocl_OclExpression51"):
                opp_val = getattr(old_value, "simpleocl_OclExpression51", None)
                if opp_val == self:
                    setattr(old_value, "simpleocl_OclExpression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleocl_OclExpression51"):
                opp_val = getattr(value, "simpleocl_OclExpression51", None)
                setattr(value, "simpleocl_OclExpression51", self)

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
            if hasattr(old_value, "OclExpression53"):
                opp_val = getattr(old_value, "OclExpression53", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression53"):
                opp_val = getattr(value, "OclExpression53", None)
                setattr(value, "OclExpression53", self)

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
class simpleocl_BraceExp(OclExpression):

    pass
class simpleocl_PrimitiveExp(OclExpression):

    pass
class simpleocl_TupleExp(OclExpression):

    pass
class simpleocl_OclUndefinedExp(OclExpression):

    pass
class simpleocl_StaticPropertyCallExp(OclExpression):

    pass
class simpleocl_VariableExp(OclExpression):

    pass
class simpleocl_Operation(OclFeature):

    pass
class simpleocl_LocalVariable(VariableDeclaration):

    def __init__(self, eq: str, LocalVariable: "simpleocl_OclExpression" = None, LocalVariable62: "simpleocl_IterateExp" = None, LocalVariable64: "simpleocl_LetExp" = None, variable: "simpleocl_LetExp" = None, initializedVariable: "simpleocl_OclExpression" = None, result: "simpleocl_IterateExp" = None):
        self.eq = eq
        self.LocalVariable = LocalVariable
        self.LocalVariable62 = LocalVariable62
        self.LocalVariable64 = LocalVariable64
        self.variable = variable
        self.initializedVariable = initializedVariable
        self.result = result
        
    @property
    def eq(self) -> str:
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq

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
            if hasattr(old_value, "OclExpression80"):
                opp_val = getattr(old_value, "OclExpression80", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression80"):
                opp_val = getattr(value, "OclExpression80", None)
                setattr(value, "OclExpression80", self)

    @property
    def LocalVariable62(self):
        return self.__LocalVariable62

    @LocalVariable62.setter
    def LocalVariable62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_LocalVariable__LocalVariable62", None)
        self.__LocalVariable62 = value
        
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
            if hasattr(old_value, "LetExp78"):
                opp_val = getattr(old_value, "LetExp78", None)
                if opp_val == self:
                    setattr(old_value, "LetExp78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp78"):
                opp_val = getattr(value, "LetExp78", None)
                setattr(value, "LetExp78", self)

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
    def LocalVariable64(self):
        return self.__LocalVariable64

    @LocalVariable64.setter
    def LocalVariable64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_LocalVariable__LocalVariable64", None)
        self.__LocalVariable64 = value
        
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
                if hasattr(item, "OclExpression49"):
                    opp_val = getattr(item, "OclExpression49", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression49"):
                    opp_val = getattr(item, "OclExpression49", None)
                    
                    setattr(item, "OclExpression49", self)
                    

class simpleocl_LoopExp(PropertyCall):

    pass
class simpleocl_LetExp(OclExpression):

    pass
class simpleocl_CollectionExp(OclExpression):

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
    def OclMetamodel(self):
        return self.__OclMetamodel

    @OclMetamodel.setter
    def OclMetamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclMetamodel__OclMetamodel", None)
        self.__OclMetamodel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model151"):
                opp_val = getattr(old_value, "model151", None)
                if opp_val == self:
                    setattr(old_value, "model151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model151"):
                opp_val = getattr(value, "model151", None)
                setattr(value, "model151", self)

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

class NamedElement:

    pass
class simpleocl_OclModel(NamedElement):

    pass
class simpleocl_OclFeature(NamedElement):

    def __init__(self, eq: str, feature: "simpleocl_OclFeatureDefinition" = None, OclFeature: "simpleocl_OclFeatureDefinition" = None):
        self.eq = eq
        self.feature = feature
        self.OclFeature = OclFeature
        
    @property
    def eq(self) -> str:
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq

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
            if hasattr(old_value, "OclFeatureDefinition137"):
                opp_val = getattr(old_value, "OclFeatureDefinition137", None)
                if opp_val == self:
                    setattr(old_value, "OclFeatureDefinition137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclFeatureDefinition137"):
                opp_val = getattr(value, "OclFeatureDefinition137", None)
                setattr(value, "OclFeatureDefinition137", self)

class simpleocl_Import(NamedElement):

    pass
class simpleocl_Module(NamedElement):

    pass
class LocatedElement:

    pass
class simpleocl_OclExpression(LocatedElement):

    pass
class simpleocl_OclContextDefinition(LocatedElement):

    pass
class simpleocl_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, TupleTypeAttribute: "simpleocl_OclType" = None, TupleTypeAttribute114: "simpleocl_TupleType" = None, tupleTypeAttribute: "simpleocl_OclType" = None, attributes: "simpleocl_TupleType" = None):
        self.name = name
        self.TupleTypeAttribute = TupleTypeAttribute
        self.TupleTypeAttribute114 = TupleTypeAttribute114
        self.tupleTypeAttribute = tupleTypeAttribute
        self.attributes = attributes
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TupleTypeAttribute114(self):
        return self.__TupleTypeAttribute114

    @TupleTypeAttribute114.setter
    def TupleTypeAttribute114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_TupleTypeAttribute__TupleTypeAttribute114", None)
        self.__TupleTypeAttribute114 = value
        
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
            if hasattr(old_value, "type101"):
                opp_val = getattr(old_value, "type101", None)
                if opp_val == self:
                    setattr(old_value, "type101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type101"):
                opp_val = getattr(value, "type101", None)
                setattr(value, "type101", self)

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
            if hasattr(old_value, "OclType116"):
                opp_val = getattr(old_value, "OclType116", None)
                if opp_val == self:
                    setattr(old_value, "OclType116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType116"):
                opp_val = getattr(value, "OclType116", None)
                setattr(value, "OclType116", self)

class simpleocl_ModuleElement(LocatedElement):

    pass
class simpleocl_StaticPropertyCall(LocatedElement):

    pass
class simpleocl_OclType(LocatedElement):

    def __init__(self, name: str, OclType: "simpleocl_OclExpression" = None, OclType38: "simpleocl_StaticPropertyCallExp" = None, OclType75: "simpleocl_VariableDeclaration" = None, valueType: "simpleocl_MapType" = None, type95: "simpleocl_Attribute" = None, keyType: "simpleocl_MapType" = None, elementType: "simpleocl_CollectionType" = None, type101: "simpleocl_TupleTypeAttribute" = None, type103: "simpleocl_VariableDeclaration" = None, returnType106: "simpleocl_LambdaType" = None, argumentTypes: "simpleocl_LambdaType" = None, OclType87: "simpleocl_CollectionType" = None, context_: "simpleocl_OclContextDefinition" = None, type: "simpleocl_OclExpression" = None, returnType: "simpleocl_Operation" = None, OclType116: "simpleocl_TupleTypeAttribute" = None, source110: "simpleocl_StaticPropertyCallExp" = None, OclType135: "simpleocl_OclContextDefinition" = None, OclType121: "simpleocl_MapType" = None, OclType123: "simpleocl_MapType" = None, OclType125: "simpleocl_LambdaType" = None, OclType127: "simpleocl_LambdaType" = None, OclType141: "simpleocl_Attribute" = None, OclType145: "simpleocl_Operation" = None):
        self.name = name
        self.OclType = OclType
        self.OclType38 = OclType38
        self.OclType75 = OclType75
        self.valueType = valueType
        self.type95 = type95
        self.keyType = keyType
        self.elementType = elementType
        self.type101 = type101
        self.type103 = type103
        self.returnType106 = returnType106
        self.argumentTypes = argumentTypes
        self.OclType87 = OclType87
        self.context_ = context_
        self.type = type
        self.returnType = returnType
        self.OclType116 = OclType116
        self.source110 = source110
        self.OclType135 = OclType135
        self.OclType121 = OclType121
        self.OclType123 = OclType123
        self.OclType125 = OclType125
        self.OclType127 = OclType127
        self.OclType141 = OclType141
        self.OclType145 = OclType145
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def OclType125(self):
        return self.__OclType125

    @OclType125.setter
    def OclType125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType125", None)
        self.__OclType125 = value
        
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
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__keyType", None)
        self.__keyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType98"):
                opp_val = getattr(old_value, "MapType98", None)
                if opp_val == self:
                    setattr(old_value, "MapType98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType98"):
                opp_val = getattr(value, "MapType98", None)
                setattr(value, "MapType98", self)

    @property
    def OclType116(self):
        return self.__OclType116

    @OclType116.setter
    def OclType116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType116", None)
        self.__OclType116 = value
        
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
    def OclType121(self):
        return self.__OclType121

    @OclType121.setter
    def OclType121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType121", None)
        self.__OclType121 = value
        
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
    def OclType38(self):
        return self.__OclType38

    @OclType38.setter
    def OclType38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType38", None)
        self.__OclType38 = value
        
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
    def OclType145(self):
        return self.__OclType145

    @OclType145.setter
    def OclType145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType145", None)
        self.__OclType145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation144"):
                opp_val = getattr(old_value, "operation144", None)
                if opp_val == self:
                    setattr(old_value, "operation144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation144"):
                opp_val = getattr(value, "operation144", None)
                setattr(value, "operation144", self)

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
            if hasattr(old_value, "OclExpression90"):
                opp_val = getattr(old_value, "OclExpression90", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression90"):
                opp_val = getattr(value, "OclExpression90", None)
                setattr(value, "OclExpression90", self)

    @property
    def OclType141(self):
        return self.__OclType141

    @OclType141.setter
    def OclType141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType141", None)
        self.__OclType141 = value
        
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
    def returnType106(self):
        return self.__returnType106

    @returnType106.setter
    def returnType106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__returnType106", None)
        self.__returnType106 = value
        
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
    def OclType75(self):
        return self.__OclType75

    @OclType75.setter
    def OclType75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType75", None)
        self.__OclType75 = value
        
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
    def OclType127(self):
        return self.__OclType127

    @OclType127.setter
    def OclType127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType127", None)
        self.__OclType127 = value
        
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
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation92"):
                opp_val = getattr(old_value, "Operation92", None)
                if opp_val == self:
                    setattr(old_value, "Operation92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation92"):
                opp_val = getattr(value, "Operation92", None)
                setattr(value, "Operation92", self)

    @property
    def OclType123(self):
        return self.__OclType123

    @OclType123.setter
    def OclType123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType123", None)
        self.__OclType123 = value
        
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
    def type95(self):
        return self.__type95

    @type95.setter
    def type95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__type95", None)
        self.__type95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute96"):
                opp_val = getattr(old_value, "Attribute96", None)
                if opp_val == self:
                    setattr(old_value, "Attribute96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute96"):
                opp_val = getattr(value, "Attribute96", None)
                setattr(value, "Attribute96", self)

    @property
    def OclType87(self):
        return self.__OclType87

    @OclType87.setter
    def OclType87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType87", None)
        self.__OclType87 = value
        
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
    def OclType135(self):
        return self.__OclType135

    @OclType135.setter
    def OclType135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__OclType135", None)
        self.__OclType135 = value
        
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
    def type101(self):
        return self.__type101

    @type101.setter
    def type101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__type101", None)
        self.__type101 = value
        
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
    def source110(self):
        return self.__source110

    @source110.setter
    def source110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__source110", None)
        self.__source110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StaticPropertyCallExp111"):
                opp_val = getattr(old_value, "StaticPropertyCallExp111", None)
                if opp_val == self:
                    setattr(old_value, "StaticPropertyCallExp111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StaticPropertyCallExp111"):
                opp_val = getattr(value, "StaticPropertyCallExp111", None)
                setattr(value, "StaticPropertyCallExp111", self)

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
    def argumentTypes(self):
        return self.__argumentTypes

    @argumentTypes.setter
    def argumentTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__argumentTypes", None)
        self.__argumentTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LambdaType108"):
                opp_val = getattr(old_value, "LambdaType108", None)
                if opp_val == self:
                    setattr(old_value, "LambdaType108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LambdaType108"):
                opp_val = getattr(value, "LambdaType108", None)
                setattr(value, "LambdaType108", self)

    @property
    def type103(self):
        return self.__type103

    @type103.setter
    def type103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_OclType__type103", None)
        self.__type103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration104"):
                opp_val = getattr(old_value, "VariableDeclaration104", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration104"):
                opp_val = getattr(value, "VariableDeclaration104", None)
                setattr(value, "VariableDeclaration104", self)

class simpleocl_VariableDeclaration(LocatedElement):

    def __init__(self, varName: str, VariableDeclaration: "simpleocl_VariableExp" = None, referredVariable: set["simpleocl_VariableExp"] = None, variableDeclaration: "simpleocl_OclType" = None, VariableDeclaration104: "simpleocl_OclType" = None):
        self.varName = varName
        self.VariableDeclaration = VariableDeclaration
        self.referredVariable = referredVariable if referredVariable is not None else set()
        self.variableDeclaration = variableDeclaration
        self.VariableDeclaration104 = VariableDeclaration104
        
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
    def VariableDeclaration104(self):
        return self.__VariableDeclaration104

    @VariableDeclaration104.setter
    def VariableDeclaration104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleocl_VariableDeclaration__VariableDeclaration104", None)
        self.__VariableDeclaration104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type103"):
                opp_val = getattr(old_value, "type103", None)
                if opp_val == self:
                    setattr(old_value, "type103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type103"):
                opp_val = getattr(value, "type103", None)
                setattr(value, "type103", self)

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
            if hasattr(old_value, "OclType75"):
                opp_val = getattr(old_value, "OclType75", None)
                if opp_val == self:
                    setattr(old_value, "OclType75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType75"):
                opp_val = getattr(value, "OclType75", None)
                setattr(value, "OclType75", self)

class simpleocl_MapElement(LocatedElement):

    pass
class simpleocl_PropertyCall(LocatedElement):

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

class simpleocl_LocatedElement(ABC):

    def __init__(self, line: str, column: str, charStart: str, charEnd: str):
        self.line = line
        self.column = column
        self.charStart = charStart
        self.charEnd = charEnd
        
    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column

    @property
    def line(self) -> str:
        return self.__line

    @line.setter
    def line(self, line: str):
        self.__line = line

    @property
    def charEnd(self) -> str:
        return self.__charEnd

    @charEnd.setter
    def charEnd(self, charEnd: str):
        self.__charEnd = charEnd

    @property
    def charStart(self) -> str:
        return self.__charStart

    @charStart.setter
    def charStart(self, charStart: str):
        self.__charStart = charStart
