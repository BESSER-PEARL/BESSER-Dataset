from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclFeature:

    pass
class OCLinEmig_Module:

    def __init__(self, name: str, OCLinEmig_Module: set["OCLinEmig_OclFeatureDefinition"] = None):
        self.name = name
        self.OCLinEmig_Module = OCLinEmig_Module if OCLinEmig_Module is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OCLinEmig_Module(self):
        return self.__OCLinEmig_Module

    @OCLinEmig_Module.setter
    def OCLinEmig_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_Module__OCLinEmig_Module", None)
        self.__OCLinEmig_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCLinEmig_OclFeatureDefinition"):
                    opp_val = getattr(item, "OCLinEmig_OclFeatureDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "OCLinEmig_OclFeatureDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCLinEmig_OclFeatureDefinition"):
                    opp_val = getattr(item, "OCLinEmig_OclFeatureDefinition", None)
                    
                    setattr(item, "OCLinEmig_OclFeatureDefinition", self)
                    

class OCLinEmig_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
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

class CollectionType:

    pass
class OCLinEmig_OrderedSetType(CollectionType):

    pass
class OCLinEmig_SequenceType(CollectionType):

    pass
class OCLinEmig_SetType(CollectionType):

    pass
class OCLinEmig_BagType(CollectionType):

    pass
class NumericType:

    pass
class OCLinEmig_RealType(NumericType):

    pass
class OCLinEmig_IntegerType(NumericType):

    pass
class Primitive:

    pass
class OCLinEmig_NumericType(Primitive):

    pass
class OCLinEmig_BooleanType(Primitive):

    pass
class OCLinEmig_StringType(Primitive):

    pass
class OclType:

    pass
class OCLinEmig_OclModelElement(OclType):

    pass
class OCLinEmig_TupleType(OclType):

    pass
class OCLinEmig_Primitive(OclType):

    pass
class OCLinEmig_OclAnyType(OclType):

    pass
class OCLinEmig_MapType(OclType):

    pass
class OCLinEmig_CollectionType(OclType):

    pass
class OperationCallExp:

    pass
class OCLinEmig_CollectionOperationCallExp(OperationCallExp):

    pass
class OCLinEmig_OperatorCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class OCLinEmig_IteratorExp(LoopExp):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCLinEmig_IterateExp(LoopExp):

    pass
class VariableDeclaration:

    pass
class OCLinEmig_Parameter(VariableDeclaration):

    pass
class OCLinEmig_Iterator(VariableDeclaration):

    pass
class OCLinEmig_TuplePart(VariableDeclaration):

    pass
class PropertyCallExp:

    pass
class OCLinEmig_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class CollectionExp:

    pass
class OCLinEmig_SequenceExp(CollectionExp):

    pass
class OCLinEmig_SetExp(CollectionExp):

    pass
class OCLinEmig_OrderedSetExp(CollectionExp):

    pass
class OCLinEmig_BagExp(CollectionExp):

    pass
class NumericExp:

    pass
class OCLinEmig_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class OCLinEmig_RealExp(NumericExp):

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
class OCLinEmig_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class OCLinEmig_NumericExp(PrimitiveExp):

    pass
class OCLinEmig_StringExp(PrimitiveExp):

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
class OCLinEmig_OclUndefinedExp(OclExpression):

    pass
class OCLinEmig_PrimitiveExp(OclExpression):

    pass
class OCLinEmig_MapExp(OclExpression):

    pass
class OCLinEmig_TupleExp(OclExpression):

    pass
class OCLinEmig_SuperExp(OclExpression):

    pass
class OCLinEmig_EnumLiteralExp(OclExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCLinEmig_LetExp(OclExpression):

    pass
class OCLinEmig_VariableExp(OclExpression):

    pass
class OCLinEmig_Attribute(OclFeature):

    def __init__(self, name: str, Attribute: "OCLinEmig_OclExpression" = None, Attribute70: "OCLinEmig_OclType" = None, attribute: "OCLinEmig_OclType" = None, owningAttribute: "OCLinEmig_OclExpression" = None):
        self.name = name
        self.Attribute = Attribute
        self.Attribute70 = Attribute70
        self.attribute = attribute
        self.owningAttribute = owningAttribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType103"):
                opp_val = getattr(old_value, "OclType103", None)
                if opp_val == self:
                    setattr(old_value, "OclType103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType103"):
                opp_val = getattr(value, "OclType103", None)
                setattr(value, "OclType103", self)

    @property
    def owningAttribute(self):
        return self.__owningAttribute

    @owningAttribute.setter
    def owningAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_Attribute__owningAttribute", None)
        self.__owningAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression101"):
                opp_val = getattr(old_value, "OclExpression101", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression101"):
                opp_val = getattr(value, "OclExpression101", None)
                setattr(value, "OclExpression101", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "initExpression15"):
                opp_val = getattr(old_value, "initExpression15", None)
                if opp_val == self:
                    setattr(old_value, "initExpression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "initExpression15"):
                opp_val = getattr(value, "initExpression15", None)
                setattr(value, "initExpression15", self)

    @property
    def Attribute70(self):
        return self.__Attribute70

    @Attribute70.setter
    def Attribute70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_Attribute__Attribute70", None)
        self.__Attribute70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type69"):
                opp_val = getattr(old_value, "type69", None)
                if opp_val == self:
                    setattr(old_value, "type69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type69"):
                opp_val = getattr(value, "type69", None)
                setattr(value, "type69", self)

class OCLinEmig_Operation(OclFeature):

    def __init__(self, name: str, Operation: "OCLinEmig_OclExpression" = None, Operation59: "OCLinEmig_Parameter" = None, Operation66: "OCLinEmig_OclType" = None, operation: set["OCLinEmig_Parameter"] = None, operation106: "OCLinEmig_OclType" = None, owningOperation: "OCLinEmig_OclExpression" = None):
        self.name = name
        self.Operation = Operation
        self.Operation59 = Operation59
        self.Operation66 = Operation66
        self.operation = operation if operation is not None else set()
        self.operation106 = operation106
        self.owningOperation = owningOperation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Operation66(self):
        return self.__Operation66

    @Operation66.setter
    def Operation66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_Operation__Operation66", None)
        self.__Operation66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "returnType"):
                opp_val = getattr(old_value, "returnType", None)
                if opp_val == self:
                    setattr(old_value, "returnType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "returnType"):
                opp_val = getattr(value, "returnType", None)
                setattr(value, "returnType", self)

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "body11"):
                opp_val = getattr(old_value, "body11", None)
                if opp_val == self:
                    setattr(old_value, "body11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "body11"):
                opp_val = getattr(value, "body11", None)
                setattr(value, "body11", self)

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_Operation__operation", None)
        self.__operation = value if value is not None else set()
        
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
                    

    @property
    def owningOperation(self):
        return self.__owningOperation

    @owningOperation.setter
    def owningOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_Operation__owningOperation", None)
        self.__owningOperation = value
        
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
    def operation106(self):
        return self.__operation106

    @operation106.setter
    def operation106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_Operation__operation106", None)
        self.__operation106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType107"):
                opp_val = getattr(old_value, "OclType107", None)
                if opp_val == self:
                    setattr(old_value, "OclType107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType107"):
                opp_val = getattr(value, "OclType107", None)
                setattr(value, "OclType107", self)

    @property
    def Operation59(self):
        return self.__Operation59

    @Operation59.setter
    def Operation59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_Operation__Operation59", None)
        self.__Operation59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters"):
                opp_val = getattr(old_value, "parameters", None)
                if opp_val == self:
                    setattr(old_value, "parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters"):
                opp_val = getattr(value, "parameters", None)
                setattr(value, "parameters", self)

class OCLinEmig_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, OperationCallExp: "OCLinEmig_OclExpression" = None, parentOperation: set["OCLinEmig_OclExpression"] = None):
        self.operationName = operationName
        self.OperationCallExp = OperationCallExp
        self.parentOperation = parentOperation if parentOperation is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def OperationCallExp(self):
        return self.__OperationCallExp

    @OperationCallExp.setter
    def OperationCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OperationCallExp__OperationCallExp", None)
        self.__OperationCallExp = value
        
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
        old_value = getattr(self, f"_OCLinEmig_OperationCallExp__parentOperation", None)
        self.__parentOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression31"):
                    opp_val = getattr(item, "OclExpression31", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression31"):
                    opp_val = getattr(item, "OclExpression31", None)
                    
                    setattr(item, "OclExpression31", self)
                    

class OCLinEmig_LoopExp(PropertyCallExp):

    pass
class OCLinEmig_CollectionExp(OclExpression):

    pass
class OCLinEmig_PropertyCallExp(OclExpression):

    pass
class OCLinEmig_IfExp(OclExpression):

    pass
class OCLinEmig_OclType(OclExpression):

    def __init__(self, name: str, OclType: "OCLinEmig_OclExpression" = None, OclType61: "OCLinEmig_CollectionType" = None, context_: "OCLinEmig_OclContextDefinition" = None, type: "OCLinEmig_OclExpression" = None, returnType: "OCLinEmig_Operation" = None, OclType49: "OCLinEmig_VariableDeclaration" = None, keyType: "OCLinEmig_MapType" = None, elementType: "OCLinEmig_CollectionType" = None, type75: "OCLinEmig_TupleTypeAttribute" = None, type77: "OCLinEmig_VariableDeclaration" = None, valueType: "OCLinEmig_MapType" = None, type69: "OCLinEmig_Attribute" = None, OclType87: "OCLinEmig_MapType" = None, OclType89: "OCLinEmig_MapType" = None, OclType97: "OCLinEmig_OclContextDefinition" = None, OclType82: "OCLinEmig_TupleTypeAttribute" = None, OclType103: "OCLinEmig_Attribute" = None, OclType107: "OCLinEmig_Operation" = None):
        self.name = name
        self.OclType = OclType
        self.OclType61 = OclType61
        self.context_ = context_
        self.type = type
        self.returnType = returnType
        self.OclType49 = OclType49
        self.keyType = keyType
        self.elementType = elementType
        self.type75 = type75
        self.type77 = type77
        self.valueType = valueType
        self.type69 = type69
        self.OclType87 = OclType87
        self.OclType89 = OclType89
        self.OclType97 = OclType97
        self.OclType82 = OclType82
        self.OclType103 = OclType103
        self.OclType107 = OclType107
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def context_(self):
        return self.__context_

    @context_.setter
    def context_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__context_", None)
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
    def type77(self):
        return self.__type77

    @type77.setter
    def type77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__type77", None)
        self.__type77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration78"):
                opp_val = getattr(old_value, "VariableDeclaration78", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration78"):
                opp_val = getattr(value, "VariableDeclaration78", None)
                setattr(value, "VariableDeclaration78", self)

    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation66"):
                opp_val = getattr(old_value, "Operation66", None)
                if opp_val == self:
                    setattr(old_value, "Operation66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation66"):
                opp_val = getattr(value, "Operation66", None)
                setattr(value, "Operation66", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression64"):
                opp_val = getattr(old_value, "OclExpression64", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression64"):
                opp_val = getattr(value, "OclExpression64", None)
                setattr(value, "OclExpression64", self)

    @property
    def OclType49(self):
        return self.__OclType49

    @OclType49.setter
    def OclType49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__OclType49", None)
        self.__OclType49 = value
        
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
    def type69(self):
        return self.__type69

    @type69.setter
    def type69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__type69", None)
        self.__type69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute70"):
                opp_val = getattr(old_value, "Attribute70", None)
                if opp_val == self:
                    setattr(old_value, "Attribute70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute70"):
                opp_val = getattr(value, "Attribute70", None)
                setattr(value, "Attribute70", self)

    @property
    def OclType97(self):
        return self.__OclType97

    @OclType97.setter
    def OclType97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__OclType97", None)
        self.__OclType97 = value
        
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
    def OclType61(self):
        return self.__OclType61

    @OclType61.setter
    def OclType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__OclType61", None)
        self.__OclType61 = value
        
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
    def OclType107(self):
        return self.__OclType107

    @OclType107.setter
    def OclType107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__OclType107", None)
        self.__OclType107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation106"):
                opp_val = getattr(old_value, "operation106", None)
                if opp_val == self:
                    setattr(old_value, "operation106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation106"):
                opp_val = getattr(value, "operation106", None)
                setattr(value, "operation106", self)

    @property
    def type75(self):
        return self.__type75

    @type75.setter
    def type75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__type75", None)
        self.__type75 = value
        
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
    def OclType103(self):
        return self.__OclType103

    @OclType103.setter
    def OclType103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__OclType103", None)
        self.__OclType103 = value
        
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
    def valueType(self):
        return self.__valueType

    @valueType.setter
    def valueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__valueType", None)
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
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__keyType", None)
        self.__keyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType72"):
                opp_val = getattr(old_value, "MapType72", None)
                if opp_val == self:
                    setattr(old_value, "MapType72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType72"):
                opp_val = getattr(value, "MapType72", None)
                setattr(value, "MapType72", self)

    @property
    def elementType(self):
        return self.__elementType

    @elementType.setter
    def elementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__elementType", None)
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
    def OclType87(self):
        return self.__OclType87

    @OclType87.setter
    def OclType87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__OclType87", None)
        self.__OclType87 = value
        
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
    def OclType82(self):
        return self.__OclType82

    @OclType82.setter
    def OclType82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__OclType82", None)
        self.__OclType82 = value
        
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
    def OclType89(self):
        return self.__OclType89

    @OclType89.setter
    def OclType89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__OclType89", None)
        self.__OclType89 = value
        
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
    def OclType(self):
        return self.__OclType

    @OclType.setter
    def OclType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclType__OclType", None)
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

class LocatedElement:

    pass
class OCLinEmig_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, TupleTypeAttribute: "OCLinEmig_OclType" = None, TupleTypeAttribute80: "OCLinEmig_TupleType" = None, attributes: "OCLinEmig_TupleType" = None, tupleTypeAttribute: "OCLinEmig_OclType" = None):
        self.name = name
        self.TupleTypeAttribute = TupleTypeAttribute
        self.TupleTypeAttribute80 = TupleTypeAttribute80
        self.attributes = attributes
        self.tupleTypeAttribute = tupleTypeAttribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TupleTypeAttribute80(self):
        return self.__TupleTypeAttribute80

    @TupleTypeAttribute80.setter
    def TupleTypeAttribute80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_TupleTypeAttribute__TupleTypeAttribute80", None)
        self.__TupleTypeAttribute80 = value
        
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
        old_value = getattr(self, f"_OCLinEmig_TupleTypeAttribute__attributes", None)
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
        old_value = getattr(self, f"_OCLinEmig_TupleTypeAttribute__tupleTypeAttribute", None)
        self.__tupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType82"):
                opp_val = getattr(old_value, "OclType82", None)
                if opp_val == self:
                    setattr(old_value, "OclType82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType82"):
                opp_val = getattr(value, "OclType82", None)
                setattr(value, "OclType82", self)

    @property
    def TupleTypeAttribute(self):
        return self.__TupleTypeAttribute

    @TupleTypeAttribute.setter
    def TupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_TupleTypeAttribute__TupleTypeAttribute", None)
        self.__TupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type75"):
                opp_val = getattr(old_value, "type75", None)
                if opp_val == self:
                    setattr(old_value, "type75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type75"):
                opp_val = getattr(value, "type75", None)
                setattr(value, "type75", self)

class OCLinEmig_MapElement(LocatedElement):

    pass
class OCLinEmig_OclModel(LocatedElement):

    def __init__(self, name: str, OclModel: "OCLinEmig_OclModelElement" = None, OclModel112: "OCLinEmig_OclModel" = None, model: "OCLinEmig_OclModel" = None, model114: set["OCLinEmig_OclModelElement"] = None, OclModel117: "OCLinEmig_OclModel" = None, metamodel: set["OCLinEmig_OclModel"] = None):
        self.name = name
        self.OclModel = OclModel
        self.OclModel112 = OclModel112
        self.model = model
        self.model114 = model114 if model114 is not None else set()
        self.OclModel117 = OclModel117
        self.metamodel = metamodel if metamodel is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclModel(self):
        return self.__OclModel

    @OclModel.setter
    def OclModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclModel__OclModel", None)
        self.__OclModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements85"):
                opp_val = getattr(old_value, "elements85", None)
                if opp_val == self:
                    setattr(old_value, "elements85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements85"):
                opp_val = getattr(value, "elements85", None)
                setattr(value, "elements85", self)

    @property
    def model114(self):
        return self.__model114

    @model114.setter
    def model114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclModel__model114", None)
        self.__model114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModelElement"):
                    opp_val = getattr(item, "OclModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModelElement"):
                    opp_val = getattr(item, "OclModelElement", None)
                    
                    setattr(item, "OclModelElement", self)
                    

    @property
    def OclModel117(self):
        return self.__OclModel117

    @OclModel117.setter
    def OclModel117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclModel__OclModel117", None)
        self.__OclModel117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel"):
                opp_val = getattr(old_value, "metamodel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel"):
                opp_val = getattr(value, "metamodel", None)
                if opp_val is None:
                    setattr(value, "metamodel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel(self):
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclModel__metamodel", None)
        self.__metamodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel117"):
                    opp_val = getattr(item, "OclModel117", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel117"):
                    opp_val = getattr(item, "OclModel117", None)
                    
                    setattr(item, "OclModel117", self)
                    

    @property
    def OclModel112(self):
        return self.__OclModel112

    @OclModel112.setter
    def OclModel112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclModel__OclModel112", None)
        self.__OclModel112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model"):
                opp_val = getattr(old_value, "model", None)
                if opp_val == self:
                    setattr(old_value, "model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model"):
                opp_val = getattr(value, "model", None)
                setattr(value, "model", self)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_OclModel__model", None)
        self.__model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclModel112"):
                opp_val = getattr(old_value, "OclModel112", None)
                if opp_val == self:
                    setattr(old_value, "OclModel112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel112"):
                opp_val = getattr(value, "OclModel112", None)
                setattr(value, "OclModel112", self)

class OCLinEmig_OclContextDefinition(LocatedElement):

    pass
class OCLinEmig_VariableDeclaration(LocatedElement):

    def __init__(self, id: str, varName: str, VariableDeclaration: "OCLinEmig_OclExpression" = None, VariableDeclaration17: "OCLinEmig_VariableExp" = None, VariableDeclaration36: "OCLinEmig_IterateExp" = None, VariableDeclaration38: "OCLinEmig_LetExp" = None, initializedVariable: "OCLinEmig_OclExpression" = None, variable: "OCLinEmig_LetExp" = None, result: "OCLinEmig_IterateExp" = None, referredVariable: set["OCLinEmig_VariableExp"] = None, variableDeclaration: "OCLinEmig_OclType" = None, VariableDeclaration78: "OCLinEmig_OclType" = None):
        self.id = id
        self.varName = varName
        self.VariableDeclaration = VariableDeclaration
        self.VariableDeclaration17 = VariableDeclaration17
        self.VariableDeclaration36 = VariableDeclaration36
        self.VariableDeclaration38 = VariableDeclaration38
        self.initializedVariable = initializedVariable
        self.variable = variable
        self.result = result
        self.referredVariable = referredVariable if referredVariable is not None else set()
        self.variableDeclaration = variableDeclaration
        self.VariableDeclaration78 = VariableDeclaration78
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
        old_value = getattr(self, f"_OCLinEmig_VariableDeclaration__VariableDeclaration", None)
        self.__VariableDeclaration = value
        
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
    def VariableDeclaration78(self):
        return self.__VariableDeclaration78

    @VariableDeclaration78.setter
    def VariableDeclaration78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_VariableDeclaration__VariableDeclaration78", None)
        self.__VariableDeclaration78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type77"):
                opp_val = getattr(old_value, "type77", None)
                if opp_val == self:
                    setattr(old_value, "type77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type77"):
                opp_val = getattr(value, "type77", None)
                setattr(value, "type77", self)

    @property
    def variableDeclaration(self):
        return self.__variableDeclaration

    @variableDeclaration.setter
    def variableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_VariableDeclaration__variableDeclaration", None)
        self.__variableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType49"):
                opp_val = getattr(old_value, "OclType49", None)
                if opp_val == self:
                    setattr(old_value, "OclType49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType49"):
                opp_val = getattr(value, "OclType49", None)
                setattr(value, "OclType49", self)

    @property
    def referredVariable(self):
        return self.__referredVariable

    @referredVariable.setter
    def referredVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_VariableDeclaration__referredVariable", None)
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
    def VariableDeclaration17(self):
        return self.__VariableDeclaration17

    @VariableDeclaration17.setter
    def VariableDeclaration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_VariableDeclaration__VariableDeclaration17", None)
        self.__VariableDeclaration17 = value
        
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
    def initializedVariable(self):
        return self.__initializedVariable

    @initializedVariable.setter
    def initializedVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_VariableDeclaration__initializedVariable", None)
        self.__initializedVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression51"):
                opp_val = getattr(old_value, "OclExpression51", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression51"):
                opp_val = getattr(value, "OclExpression51", None)
                setattr(value, "OclExpression51", self)

    @property
    def VariableDeclaration38(self):
        return self.__VariableDeclaration38

    @VariableDeclaration38.setter
    def VariableDeclaration38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_VariableDeclaration__VariableDeclaration38", None)
        self.__VariableDeclaration38 = value
        
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
    def VariableDeclaration36(self):
        return self.__VariableDeclaration36

    @VariableDeclaration36.setter
    def VariableDeclaration36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_VariableDeclaration__VariableDeclaration36", None)
        self.__VariableDeclaration36 = value
        
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
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCLinEmig_VariableDeclaration__result", None)
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
        old_value = getattr(self, f"_OCLinEmig_VariableDeclaration__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp53"):
                opp_val = getattr(old_value, "LetExp53", None)
                if opp_val == self:
                    setattr(old_value, "LetExp53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp53"):
                opp_val = getattr(value, "LetExp53", None)
                setattr(value, "LetExp53", self)

class OCLinEmig_OclFeature(LocatedElement):

    pass
class OCLinEmig_OclFeatureDefinition(LocatedElement):

    pass
class OCLinEmig_OclExpression(LocatedElement):

    pass