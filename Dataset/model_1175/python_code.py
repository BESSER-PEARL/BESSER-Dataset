from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclFeature:

    pass
class CollectionType:

    pass
class EmigOcl_OrderedSetType(CollectionType):

    pass
class EmigOcl_BagType(CollectionType):

    pass
class NumericType:

    pass
class EmigOcl_RealType(NumericType):

    pass
class EmigOcl_IntegerType(NumericType):

    pass
class Primitive:

    pass
class EmigOcl_NumericType(Primitive):

    pass
class EmigOcl_BooleanType(Primitive):

    pass
class EmigOcl_StringType(Primitive):

    pass
class EmigOcl_SetType(CollectionType):

    pass
class EmigOcl_SequenceType(CollectionType):

    pass
class OclType:

    pass
class EmigOcl_TupleType(OclType):

    pass
class EmigOcl_OclAnyType(OclType):

    pass
class EmigOcl_LambdaType(OclType):

    pass
class EmigOcl_OclModelElement(OclType):

    pass
class EmigOcl_Primitive(OclType):

    pass
class EmigOcl_CollectionType(OclType):

    pass
class EmigOcl_MapType(OclType):

    pass
class LoopExp:

    pass
class EmigOcl_IteratorExp(LoopExp):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class EmigOcl_IterateExp(LoopExp):

    pass
class VariableDeclaration:

    pass
class EmigOcl_Parameter(VariableDeclaration):

    pass
class VariableExp:

    pass
class EmigOcl_LambdaCallExp(VariableExp):

    pass
class OperatorCallExp:

    pass
class EmigOcl_MulOpCallExp(OperatorCallExp):

    pass
class EmigOcl_EqOpCallExp(OperatorCallExp):

    pass
class EmigOcl_RelOpCallExp(OperatorCallExp):

    pass
class EmigOcl_IntOpCallExp(OperatorCallExp):

    pass
class EmigOcl_AddOpCallExp(OperatorCallExp):

    pass
class EmigOcl_NotOpCallExp(OperatorCallExp):

    pass
class PropertyCallExp:

    pass
class EmigOcl_OperatorCallExp(PropertyCallExp):

    def __init__(self, operationName: str, EmigOcl_OperatorCallExp: "EmigOcl_OclExpression" = None):
        self.operationName = operationName
        self.EmigOcl_OperatorCallExp = EmigOcl_OperatorCallExp
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def EmigOcl_OperatorCallExp(self):
        return self.__EmigOcl_OperatorCallExp

    @EmigOcl_OperatorCallExp.setter
    def EmigOcl_OperatorCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OperatorCallExp__EmigOcl_OperatorCallExp", None)
        self.__EmigOcl_OperatorCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmigOcl_OclExpression41"):
                opp_val = getattr(old_value, "EmigOcl_OclExpression41", None)
                if opp_val == self:
                    setattr(old_value, "EmigOcl_OclExpression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmigOcl_OclExpression41"):
                opp_val = getattr(value, "EmigOcl_OclExpression41", None)
                setattr(value, "EmigOcl_OclExpression41", self)

class EmigOcl_Iterator(VariableDeclaration):

    pass
class OperationCall:

    pass
class EmigOcl_CollectionOperationCall(OperationCall):

    pass
class StaticPropertyCall:

    pass
class EmigOcl_StaticNavigationOrAttributeCall(StaticPropertyCall):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class EmigOcl_StaticPropertyCall(ABC):

    pass
class PropertyCall:

    pass
class EmigOcl_NavigationOrAttributeCall(PropertyCall):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class EmigOcl_PropertyCall(ABC):

    pass
class EmigOcl_StaticOperationCall(StaticPropertyCall):

    def __init__(self, operationName: str, EmigOcl_StaticOperationCall: set["EmigOcl_OclExpression"] = None):
        self.operationName = operationName
        self.EmigOcl_StaticOperationCall = EmigOcl_StaticOperationCall if EmigOcl_StaticOperationCall is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def EmigOcl_StaticOperationCall(self):
        return self.__EmigOcl_StaticOperationCall

    @EmigOcl_StaticOperationCall.setter
    def EmigOcl_StaticOperationCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_StaticOperationCall__EmigOcl_StaticOperationCall", None)
        self.__EmigOcl_StaticOperationCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmigOcl_OclExpression34"):
                    opp_val = getattr(item, "EmigOcl_OclExpression34", None)
                    
                    if opp_val == self:
                        setattr(item, "EmigOcl_OclExpression34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmigOcl_OclExpression34"):
                    opp_val = getattr(item, "EmigOcl_OclExpression34", None)
                    
                    setattr(item, "EmigOcl_OclExpression34", self)
                    

class CollectionExp:

    pass
class EmigOcl_BagExp(CollectionExp):

    pass
class NumericExp:

    pass
class EmigOcl_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class EmigOcl_RealExp(NumericExp):

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
class EmigOcl_NumericExp(PrimitiveExp):

    pass
class EmigOcl_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class EmigOcl_StringExp(PrimitiveExp):

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
class EmigOcl_EnumLiteralExp(OclExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class EmigOcl_OclUndefinedExp(OclExpression):

    pass
class EmigOcl_BraceExp(OclExpression):

    pass
class EmigOcl_PrimitiveExp(OclExpression):

    pass
class EmigOcl_OclModelElementExp(OclExpression):

    def __init__(self, name: str, EmigOcl_OclModelElementExp: "EmigOcl_OclModel" = None):
        self.name = name
        self.EmigOcl_OclModelElementExp = EmigOcl_OclModelElementExp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EmigOcl_OclModelElementExp(self):
        return self.__EmigOcl_OclModelElementExp

    @EmigOcl_OclModelElementExp.setter
    def EmigOcl_OclModelElementExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclModelElementExp__EmigOcl_OclModelElementExp", None)
        self.__EmigOcl_OclModelElementExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmigOcl_OclModel94"):
                opp_val = getattr(old_value, "EmigOcl_OclModel94", None)
                if opp_val == self:
                    setattr(old_value, "EmigOcl_OclModel94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmigOcl_OclModel94"):
                opp_val = getattr(value, "EmigOcl_OclModel94", None)
                setattr(value, "EmigOcl_OclModel94", self)

class EmigOcl_SelfExp(OclExpression):

    pass
class EmigOcl_SuperExp(OclExpression):

    pass
class EmigOcl_StaticPropertyCallExp(OclExpression):

    pass
class EmigOcl_MapExp(OclExpression):

    pass
class EmigOcl_VariableExp(OclExpression):

    pass
class LocalVariable:

    pass
class EmigOcl_TuplePart(LocalVariable):

    pass
class EmigOcl_TupleExp(OclExpression):

    pass
class EmigOcl_SetExp(CollectionExp):

    pass
class EmigOcl_SequenceExp(CollectionExp):

    pass
class EmigOcl_OrderedSetExp(CollectionExp):

    pass
class EmigOcl_OperationCall(PropertyCall):

    def __init__(self, operationName: str, OperationCall: "EmigOcl_OclExpression" = None, parentOperation: set["EmigOcl_OclExpression"] = None):
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
        old_value = getattr(self, f"_EmigOcl_OperationCall__OperationCall", None)
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
        old_value = getattr(self, f"_EmigOcl_OperationCall__parentOperation", None)
        self.__parentOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression39"):
                    opp_val = getattr(item, "OclExpression39", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression39"):
                    opp_val = getattr(item, "OclExpression39", None)
                    
                    setattr(item, "OclExpression39", self)
                    

class EmigOcl_LoopExp(PropertyCall):

    pass
class EmigOcl_LetExp(OclExpression):

    pass
class EmigOcl_CollectionExp(OclExpression):

    pass
class EmigOcl_PropertyCallExp(OclExpression):

    pass
class EmigOcl_IfExp(OclExpression):

    pass
class LocatedElement:

    pass
class EmigOcl_OclModel(LocatedElement):

    def __init__(self, name: str, EmigOcl_OclModel: "EmigOcl_Module" = None, EmigOcl_OclModel94: "EmigOcl_OclModelElementExp" = None, OclModel: "EmigOcl_OclModelElement" = None, OclModel133: "EmigOcl_OclModel" = None, model: "EmigOcl_OclModel" = None, model135: set["EmigOcl_OclModelElement"] = None, OclModel138: "EmigOcl_OclModel" = None, metamodel: set["EmigOcl_OclModel"] = None):
        self.name = name
        self.EmigOcl_OclModel = EmigOcl_OclModel
        self.EmigOcl_OclModel94 = EmigOcl_OclModel94
        self.OclModel = OclModel
        self.OclModel133 = OclModel133
        self.model = model
        self.model135 = model135 if model135 is not None else set()
        self.OclModel138 = OclModel138
        self.metamodel = metamodel if metamodel is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model135(self):
        return self.__model135

    @model135.setter
    def model135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclModel__model135", None)
        self.__model135 = value if value is not None else set()
        
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
    def OclModel133(self):
        return self.__OclModel133

    @OclModel133.setter
    def OclModel133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclModel__OclModel133", None)
        self.__OclModel133 = value
        
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
        old_value = getattr(self, f"_EmigOcl_OclModel__model", None)
        self.__model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclModel133"):
                opp_val = getattr(old_value, "OclModel133", None)
                if opp_val == self:
                    setattr(old_value, "OclModel133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel133"):
                opp_val = getattr(value, "OclModel133", None)
                setattr(value, "OclModel133", self)

    @property
    def EmigOcl_OclModel94(self):
        return self.__EmigOcl_OclModel94

    @EmigOcl_OclModel94.setter
    def EmigOcl_OclModel94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclModel__EmigOcl_OclModel94", None)
        self.__EmigOcl_OclModel94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmigOcl_OclModelElementExp"):
                opp_val = getattr(old_value, "EmigOcl_OclModelElementExp", None)
                if opp_val == self:
                    setattr(old_value, "EmigOcl_OclModelElementExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmigOcl_OclModelElementExp"):
                opp_val = getattr(value, "EmigOcl_OclModelElementExp", None)
                setattr(value, "EmigOcl_OclModelElementExp", self)

    @property
    def OclModel(self):
        return self.__OclModel

    @OclModel.setter
    def OclModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclModel__OclModel", None)
        self.__OclModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements101"):
                opp_val = getattr(old_value, "elements101", None)
                if opp_val == self:
                    setattr(old_value, "elements101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements101"):
                opp_val = getattr(value, "elements101", None)
                setattr(value, "elements101", self)

    @property
    def OclModel138(self):
        return self.__OclModel138

    @OclModel138.setter
    def OclModel138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclModel__OclModel138", None)
        self.__OclModel138 = value
        
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
        old_value = getattr(self, f"_EmigOcl_OclModel__metamodel", None)
        self.__metamodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel138"):
                    opp_val = getattr(item, "OclModel138", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel138"):
                    opp_val = getattr(item, "OclModel138", None)
                    
                    setattr(item, "OclModel138", self)
                    

    @property
    def EmigOcl_OclModel(self):
        return self.__EmigOcl_OclModel

    @EmigOcl_OclModel.setter
    def EmigOcl_OclModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclModel__EmigOcl_OclModel", None)
        self.__EmigOcl_OclModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmigOcl_Module"):
                opp_val = getattr(old_value, "EmigOcl_Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmigOcl_Module"):
                opp_val = getattr(value, "EmigOcl_Module", None)
                if opp_val is None:
                    setattr(value, "EmigOcl_Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EmigOcl_OclType(LocatedElement):

    def __init__(self, name: str, OclType: "EmigOcl_OclExpression" = None, EmigOcl_OclType: "EmigOcl_StaticPropertyCallExp" = None, OclType63: "EmigOcl_VariableDeclaration" = None, type: "EmigOcl_OclExpression" = None, returnType: "EmigOcl_Operation" = None, valueType: "EmigOcl_MapType" = None, type83: "EmigOcl_Attribute" = None, OclType75: "EmigOcl_CollectionType" = None, context_: "EmigOcl_OclContextDefinition" = None, OclType98: "EmigOcl_TupleTypeAttribute" = None, keyType: "EmigOcl_MapType" = None, elementType: "EmigOcl_CollectionType" = None, type89: "EmigOcl_TupleTypeAttribute" = None, type91: "EmigOcl_VariableDeclaration" = None, OclType118: "EmigOcl_OclContextDefinition" = None, OclType103: "EmigOcl_MapType" = None, OclType105: "EmigOcl_MapType" = None, EmigOcl_OclType107: "EmigOcl_LambdaType" = None, EmigOcl_OclType110: "EmigOcl_LambdaType" = None, OclType124: "EmigOcl_Attribute" = None, OclType128: "EmigOcl_Operation" = None):
        self.name = name
        self.OclType = OclType
        self.EmigOcl_OclType = EmigOcl_OclType
        self.OclType63 = OclType63
        self.type = type
        self.returnType = returnType
        self.valueType = valueType
        self.type83 = type83
        self.OclType75 = OclType75
        self.context_ = context_
        self.OclType98 = OclType98
        self.keyType = keyType
        self.elementType = elementType
        self.type89 = type89
        self.type91 = type91
        self.OclType118 = OclType118
        self.OclType103 = OclType103
        self.OclType105 = OclType105
        self.EmigOcl_OclType107 = EmigOcl_OclType107
        self.EmigOcl_OclType110 = EmigOcl_OclType110
        self.OclType124 = OclType124
        self.OclType128 = OclType128
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EmigOcl_OclType(self):
        return self.__EmigOcl_OclType

    @EmigOcl_OclType.setter
    def EmigOcl_OclType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__EmigOcl_OclType", None)
        self.__EmigOcl_OclType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmigOcl_StaticPropertyCallExp"):
                opp_val = getattr(old_value, "EmigOcl_StaticPropertyCallExp", None)
                if opp_val == self:
                    setattr(old_value, "EmigOcl_StaticPropertyCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmigOcl_StaticPropertyCallExp"):
                opp_val = getattr(value, "EmigOcl_StaticPropertyCallExp", None)
                setattr(value, "EmigOcl_StaticPropertyCallExp", self)

    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation80"):
                opp_val = getattr(old_value, "Operation80", None)
                if opp_val == self:
                    setattr(old_value, "Operation80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation80"):
                opp_val = getattr(value, "Operation80", None)
                setattr(value, "Operation80", self)

    @property
    def OclType(self):
        return self.__OclType

    @OclType.setter
    def OclType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__OclType", None)
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
    def OclType118(self):
        return self.__OclType118

    @OclType118.setter
    def OclType118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__OclType118", None)
        self.__OclType118 = value
        
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
    def valueType(self):
        return self.__valueType

    @valueType.setter
    def valueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__valueType", None)
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
    def OclType75(self):
        return self.__OclType75

    @OclType75.setter
    def OclType75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__OclType75", None)
        self.__OclType75 = value
        
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
    def EmigOcl_OclType107(self):
        return self.__EmigOcl_OclType107

    @EmigOcl_OclType107.setter
    def EmigOcl_OclType107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__EmigOcl_OclType107", None)
        self.__EmigOcl_OclType107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmigOcl_LambdaType"):
                opp_val = getattr(old_value, "EmigOcl_LambdaType", None)
                if opp_val == self:
                    setattr(old_value, "EmigOcl_LambdaType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmigOcl_LambdaType"):
                opp_val = getattr(value, "EmigOcl_LambdaType", None)
                setattr(value, "EmigOcl_LambdaType", self)

    @property
    def OclType63(self):
        return self.__OclType63

    @OclType63.setter
    def OclType63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__OclType63", None)
        self.__OclType63 = value
        
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
    def context_(self):
        return self.__context_

    @context_.setter
    def context_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__context_", None)
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
    def EmigOcl_OclType110(self):
        return self.__EmigOcl_OclType110

    @EmigOcl_OclType110.setter
    def EmigOcl_OclType110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__EmigOcl_OclType110", None)
        self.__EmigOcl_OclType110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmigOcl_LambdaType109"):
                opp_val = getattr(old_value, "EmigOcl_LambdaType109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmigOcl_LambdaType109"):
                opp_val = getattr(value, "EmigOcl_LambdaType109", None)
                if opp_val is None:
                    setattr(value, "EmigOcl_LambdaType109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OclType128(self):
        return self.__OclType128

    @OclType128.setter
    def OclType128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__OclType128", None)
        self.__OclType128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation127"):
                opp_val = getattr(old_value, "operation127", None)
                if opp_val == self:
                    setattr(old_value, "operation127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation127"):
                opp_val = getattr(value, "operation127", None)
                setattr(value, "operation127", self)

    @property
    def OclType98(self):
        return self.__OclType98

    @OclType98.setter
    def OclType98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__OclType98", None)
        self.__OclType98 = value
        
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
    def elementType(self):
        return self.__elementType

    @elementType.setter
    def elementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__elementType", None)
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
    def OclType124(self):
        return self.__OclType124

    @OclType124.setter
    def OclType124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__OclType124", None)
        self.__OclType124 = value
        
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
    def type89(self):
        return self.__type89

    @type89.setter
    def type89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__type89", None)
        self.__type89 = value
        
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
    def type83(self):
        return self.__type83

    @type83.setter
    def type83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__type83", None)
        self.__type83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute84"):
                opp_val = getattr(old_value, "Attribute84", None)
                if opp_val == self:
                    setattr(old_value, "Attribute84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute84"):
                opp_val = getattr(value, "Attribute84", None)
                setattr(value, "Attribute84", self)

    @property
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__keyType", None)
        self.__keyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType86"):
                opp_val = getattr(old_value, "MapType86", None)
                if opp_val == self:
                    setattr(old_value, "MapType86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType86"):
                opp_val = getattr(value, "MapType86", None)
                setattr(value, "MapType86", self)

    @property
    def type91(self):
        return self.__type91

    @type91.setter
    def type91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__type91", None)
        self.__type91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration92"):
                opp_val = getattr(old_value, "VariableDeclaration92", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration92"):
                opp_val = getattr(value, "VariableDeclaration92", None)
                setattr(value, "VariableDeclaration92", self)

    @property
    def OclType105(self):
        return self.__OclType105

    @OclType105.setter
    def OclType105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__OclType105", None)
        self.__OclType105 = value
        
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
    def OclType103(self):
        return self.__OclType103

    @OclType103.setter
    def OclType103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__OclType103", None)
        self.__OclType103 = value
        
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
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression78"):
                opp_val = getattr(old_value, "OclExpression78", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression78"):
                opp_val = getattr(value, "OclExpression78", None)
                setattr(value, "OclExpression78", self)

class EmigOcl_MapElement(LocatedElement):

    pass
class EmigOcl_VariableDeclaration(LocatedElement):

    def __init__(self, varName: str, VariableDeclaration: "EmigOcl_VariableExp" = None, variableDeclaration: "EmigOcl_OclType" = None, referredVariable: set["EmigOcl_VariableExp"] = None, VariableDeclaration92: "EmigOcl_OclType" = None):
        self.varName = varName
        self.VariableDeclaration = VariableDeclaration
        self.variableDeclaration = variableDeclaration
        self.referredVariable = referredVariable if referredVariable is not None else set()
        self.VariableDeclaration92 = VariableDeclaration92
        
    @property
    def varName(self) -> str:
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
        old_value = getattr(self, f"_EmigOcl_VariableDeclaration__variableDeclaration", None)
        self.__variableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType63"):
                opp_val = getattr(old_value, "OclType63", None)
                if opp_val == self:
                    setattr(old_value, "OclType63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType63"):
                opp_val = getattr(value, "OclType63", None)
                setattr(value, "OclType63", self)

    @property
    def referredVariable(self):
        return self.__referredVariable

    @referredVariable.setter
    def referredVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_VariableDeclaration__referredVariable", None)
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
    def VariableDeclaration92(self):
        return self.__VariableDeclaration92

    @VariableDeclaration92.setter
    def VariableDeclaration92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_VariableDeclaration__VariableDeclaration92", None)
        self.__VariableDeclaration92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type91"):
                opp_val = getattr(old_value, "type91", None)
                if opp_val == self:
                    setattr(old_value, "type91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type91"):
                opp_val = getattr(value, "type91", None)
                setattr(value, "type91", self)

    @property
    def VariableDeclaration(self):
        return self.__VariableDeclaration

    @VariableDeclaration.setter
    def VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_VariableDeclaration__VariableDeclaration", None)
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

class EmigOcl_OclFeature(LocatedElement):

    def __init__(self, eq: str, feature: "EmigOcl_OclFeatureDefinition" = None, OclFeature: "EmigOcl_OclFeatureDefinition" = None):
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
        old_value = getattr(self, f"_EmigOcl_OclFeature__OclFeature", None)
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
        old_value = getattr(self, f"_EmigOcl_OclFeature__feature", None)
        self.__feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclFeatureDefinition120"):
                opp_val = getattr(old_value, "OclFeatureDefinition120", None)
                if opp_val == self:
                    setattr(old_value, "OclFeatureDefinition120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclFeatureDefinition120"):
                opp_val = getattr(value, "OclFeatureDefinition120", None)
                setattr(value, "OclFeatureDefinition120", self)

class EmigOcl_OclContextDefinition(LocatedElement):

    pass
class EmigOcl_OclExpression(LocatedElement):

    pass
class EmigOcl_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, TupleTypeAttribute96: "EmigOcl_TupleType" = None, tupleTypeAttribute: "EmigOcl_OclType" = None, attributes: "EmigOcl_TupleType" = None, TupleTypeAttribute: "EmigOcl_OclType" = None):
        self.name = name
        self.TupleTypeAttribute96 = TupleTypeAttribute96
        self.tupleTypeAttribute = tupleTypeAttribute
        self.attributes = attributes
        self.TupleTypeAttribute = TupleTypeAttribute
        
    @property
    def name(self) -> str:
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
        old_value = getattr(self, f"_EmigOcl_TupleTypeAttribute__attributes", None)
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
        old_value = getattr(self, f"_EmigOcl_TupleTypeAttribute__tupleTypeAttribute", None)
        self.__tupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType98"):
                opp_val = getattr(old_value, "OclType98", None)
                if opp_val == self:
                    setattr(old_value, "OclType98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType98"):
                opp_val = getattr(value, "OclType98", None)
                setattr(value, "OclType98", self)

    @property
    def TupleTypeAttribute(self):
        return self.__TupleTypeAttribute

    @TupleTypeAttribute.setter
    def TupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_TupleTypeAttribute__TupleTypeAttribute", None)
        self.__TupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type89"):
                opp_val = getattr(old_value, "type89", None)
                if opp_val == self:
                    setattr(old_value, "type89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type89"):
                opp_val = getattr(value, "type89", None)
                setattr(value, "type89", self)

    @property
    def TupleTypeAttribute96(self):
        return self.__TupleTypeAttribute96

    @TupleTypeAttribute96.setter
    def TupleTypeAttribute96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_TupleTypeAttribute__TupleTypeAttribute96", None)
        self.__TupleTypeAttribute96 = value
        
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

class EmigOcl_OclFeatureDefinition(LocatedElement):

    def __init__(self, static: str, EmigOcl_OclFeatureDefinition: "EmigOcl_Module" = None, definition113: "EmigOcl_OclContextDefinition" = None, OclFeatureDefinition: "EmigOcl_OclContextDefinition" = None, OclFeatureDefinition120: "EmigOcl_OclFeature" = None, definition: "EmigOcl_OclFeature" = None):
        self.static = static
        self.EmigOcl_OclFeatureDefinition = EmigOcl_OclFeatureDefinition
        self.definition113 = definition113
        self.OclFeatureDefinition = OclFeatureDefinition
        self.OclFeatureDefinition120 = OclFeatureDefinition120
        self.definition = definition
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def definition113(self):
        return self.__definition113

    @definition113.setter
    def definition113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclFeatureDefinition__definition113", None)
        self.__definition113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclContextDefinition114"):
                opp_val = getattr(old_value, "OclContextDefinition114", None)
                if opp_val == self:
                    setattr(old_value, "OclContextDefinition114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclContextDefinition114"):
                opp_val = getattr(value, "OclContextDefinition114", None)
                setattr(value, "OclContextDefinition114", self)

    @property
    def definition(self):
        return self.__definition

    @definition.setter
    def definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclFeatureDefinition__definition", None)
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
    def OclFeatureDefinition120(self):
        return self.__OclFeatureDefinition120

    @OclFeatureDefinition120.setter
    def OclFeatureDefinition120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclFeatureDefinition__OclFeatureDefinition120", None)
        self.__OclFeatureDefinition120 = value
        
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
    def OclFeatureDefinition(self):
        return self.__OclFeatureDefinition

    @OclFeatureDefinition.setter
    def OclFeatureDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclFeatureDefinition__OclFeatureDefinition", None)
        self.__OclFeatureDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "context_116"):
                opp_val = getattr(old_value, "context_116", None)
                if opp_val == self:
                    setattr(old_value, "context_116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "context_116"):
                opp_val = getattr(value, "context_116", None)
                setattr(value, "context_116", self)

    @property
    def EmigOcl_OclFeatureDefinition(self):
        return self.__EmigOcl_OclFeatureDefinition

    @EmigOcl_OclFeatureDefinition.setter
    def EmigOcl_OclFeatureDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_OclFeatureDefinition__EmigOcl_OclFeatureDefinition", None)
        self.__EmigOcl_OclFeatureDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmigOcl_Module2"):
                opp_val = getattr(old_value, "EmigOcl_Module2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmigOcl_Module2"):
                opp_val = getattr(value, "EmigOcl_Module2", None)
                if opp_val is None:
                    setattr(value, "EmigOcl_Module2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EmigOcl_Module(LocatedElement):

    def __init__(self, name: str, EmigOcl_Module: set["EmigOcl_OclModel"] = None, EmigOcl_Module2: set["EmigOcl_OclFeatureDefinition"] = None):
        self.name = name
        self.EmigOcl_Module = EmigOcl_Module if EmigOcl_Module is not None else set()
        self.EmigOcl_Module2 = EmigOcl_Module2 if EmigOcl_Module2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EmigOcl_Module(self):
        return self.__EmigOcl_Module

    @EmigOcl_Module.setter
    def EmigOcl_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_Module__EmigOcl_Module", None)
        self.__EmigOcl_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmigOcl_OclModel"):
                    opp_val = getattr(item, "EmigOcl_OclModel", None)
                    
                    if opp_val == self:
                        setattr(item, "EmigOcl_OclModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmigOcl_OclModel"):
                    opp_val = getattr(item, "EmigOcl_OclModel", None)
                    
                    setattr(item, "EmigOcl_OclModel", self)
                    

    @property
    def EmigOcl_Module2(self):
        return self.__EmigOcl_Module2

    @EmigOcl_Module2.setter
    def EmigOcl_Module2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_Module__EmigOcl_Module2", None)
        self.__EmigOcl_Module2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmigOcl_OclFeatureDefinition"):
                    opp_val = getattr(item, "EmigOcl_OclFeatureDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "EmigOcl_OclFeatureDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmigOcl_OclFeatureDefinition"):
                    opp_val = getattr(item, "EmigOcl_OclFeatureDefinition", None)
                    
                    setattr(item, "EmigOcl_OclFeatureDefinition", self)
                    

class EmigOcl_Attribute(OclFeature):

    def __init__(self, name: str, Attribute: "EmigOcl_OclExpression" = None, Attribute84: "EmigOcl_OclType" = None, owningAttribute: "EmigOcl_OclExpression" = None, attribute: "EmigOcl_OclType" = None):
        self.name = name
        self.Attribute = Attribute
        self.Attribute84 = Attribute84
        self.owningAttribute = owningAttribute
        self.attribute = attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Attribute84(self):
        return self.__Attribute84

    @Attribute84.setter
    def Attribute84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_Attribute__Attribute84", None)
        self.__Attribute84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type83"):
                opp_val = getattr(old_value, "type83", None)
                if opp_val == self:
                    setattr(old_value, "type83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type83"):
                opp_val = getattr(value, "type83", None)
                setattr(value, "type83", self)

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType124"):
                opp_val = getattr(old_value, "OclType124", None)
                if opp_val == self:
                    setattr(old_value, "OclType124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType124"):
                opp_val = getattr(value, "OclType124", None)
                setattr(value, "OclType124", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "initExpression18"):
                opp_val = getattr(old_value, "initExpression18", None)
                if opp_val == self:
                    setattr(old_value, "initExpression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "initExpression18"):
                opp_val = getattr(value, "initExpression18", None)
                setattr(value, "initExpression18", self)

    @property
    def owningAttribute(self):
        return self.__owningAttribute

    @owningAttribute.setter
    def owningAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_Attribute__owningAttribute", None)
        self.__owningAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression122"):
                opp_val = getattr(old_value, "OclExpression122", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression122"):
                opp_val = getattr(value, "OclExpression122", None)
                setattr(value, "OclExpression122", self)

class EmigOcl_Operation(OclFeature):

    def __init__(self, name: str, Operation: "EmigOcl_OclExpression" = None, Operation80: "EmigOcl_OclType" = None, Operation73: "EmigOcl_Parameter" = None, operation: set["EmigOcl_Parameter"] = None, operation127: "EmigOcl_OclType" = None, owningOperation: "EmigOcl_OclExpression" = None):
        self.name = name
        self.Operation = Operation
        self.Operation80 = Operation80
        self.Operation73 = Operation73
        self.operation = operation if operation is not None else set()
        self.operation127 = operation127
        self.owningOperation = owningOperation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "body14"):
                opp_val = getattr(old_value, "body14", None)
                if opp_val == self:
                    setattr(old_value, "body14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "body14"):
                opp_val = getattr(value, "body14", None)
                setattr(value, "body14", self)

    @property
    def Operation80(self):
        return self.__Operation80

    @Operation80.setter
    def Operation80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_Operation__Operation80", None)
        self.__Operation80 = value
        
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
    def operation127(self):
        return self.__operation127

    @operation127.setter
    def operation127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_Operation__operation127", None)
        self.__operation127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType128"):
                opp_val = getattr(old_value, "OclType128", None)
                if opp_val == self:
                    setattr(old_value, "OclType128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType128"):
                opp_val = getattr(value, "OclType128", None)
                setattr(value, "OclType128", self)

    @property
    def Operation73(self):
        return self.__Operation73

    @Operation73.setter
    def Operation73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_Operation__Operation73", None)
        self.__Operation73 = value
        
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

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_Operation__operation", None)
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
        old_value = getattr(self, f"_EmigOcl_Operation__owningOperation", None)
        self.__owningOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression130"):
                opp_val = getattr(old_value, "OclExpression130", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression130"):
                opp_val = getattr(value, "OclExpression130", None)
                setattr(value, "OclExpression130", self)

class EmigOcl_LocalVariable(VariableDeclaration):

    def __init__(self, eq: str, LocalVariable: "EmigOcl_OclExpression" = None, variable: "EmigOcl_LetExp" = None, initializedVariable: "EmigOcl_OclExpression" = None, result: "EmigOcl_IterateExp" = None, LocalVariable50: "EmigOcl_IterateExp" = None, LocalVariable52: "EmigOcl_LetExp" = None):
        self.eq = eq
        self.LocalVariable = LocalVariable
        self.variable = variable
        self.initializedVariable = initializedVariable
        self.result = result
        self.LocalVariable50 = LocalVariable50
        self.LocalVariable52 = LocalVariable52
        
    @property
    def eq(self) -> str:
        return self.__eq

    @eq.setter
    def eq(self, eq: str):
        self.__eq = eq

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_LocalVariable__result", None)
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
    def LocalVariable(self):
        return self.__LocalVariable

    @LocalVariable.setter
    def LocalVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_LocalVariable__LocalVariable", None)
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
        old_value = getattr(self, f"_EmigOcl_LocalVariable__initializedVariable", None)
        self.__initializedVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression68"):
                opp_val = getattr(old_value, "OclExpression68", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression68"):
                opp_val = getattr(value, "OclExpression68", None)
                setattr(value, "OclExpression68", self)

    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_LocalVariable__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp66"):
                opp_val = getattr(old_value, "LetExp66", None)
                if opp_val == self:
                    setattr(old_value, "LetExp66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp66"):
                opp_val = getattr(value, "LetExp66", None)
                setattr(value, "LetExp66", self)

    @property
    def LocalVariable52(self):
        return self.__LocalVariable52

    @LocalVariable52.setter
    def LocalVariable52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_LocalVariable__LocalVariable52", None)
        self.__LocalVariable52 = value
        
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
    def LocalVariable50(self):
        return self.__LocalVariable50

    @LocalVariable50.setter
    def LocalVariable50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmigOcl_LocalVariable__LocalVariable50", None)
        self.__LocalVariable50 = value
        
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

class EmigOcl_LocatedElement(ABC):

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

    @property
    def charEnd(self) -> str:
        return self.__charEnd

    @charEnd.setter
    def charEnd(self, charEnd: str):
        self.__charEnd = charEnd
