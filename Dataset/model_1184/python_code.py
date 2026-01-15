from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclModelElement:

    pass
class atl_n_ocl_OCL_OclModel:

    def __init__(self, name: str, atl_n_ocl_OCL_OclModel: "OclModel" = None, atl_n_ocl_OCL_OclModel141: set["OclModelElement"] = None, atl_n_ocl_OCL_OclModel143: set["OclModel"] = None):
        self.name = name
        self.atl_n_ocl_OCL_OclModel = atl_n_ocl_OCL_OclModel
        self.atl_n_ocl_OCL_OclModel141 = atl_n_ocl_OCL_OclModel141 if atl_n_ocl_OCL_OclModel141 is not None else set()
        self.atl_n_ocl_OCL_OclModel143 = atl_n_ocl_OCL_OclModel143 if atl_n_ocl_OCL_OclModel143 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atl_n_ocl_OCL_OclModel141(self):
        return self.__atl_n_ocl_OCL_OclModel141

    @atl_n_ocl_OCL_OclModel141.setter
    def atl_n_ocl_OCL_OclModel141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_OclModel__atl_n_ocl_OCL_OclModel141", None)
        self.__atl_n_ocl_OCL_OclModel141 = value if value is not None else set()
        
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
    def atl_n_ocl_OCL_OclModel(self):
        return self.__atl_n_ocl_OCL_OclModel

    @atl_n_ocl_OCL_OclModel.setter
    def atl_n_ocl_OCL_OclModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_OclModel__atl_n_ocl_OCL_OclModel", None)
        self.__atl_n_ocl_OCL_OclModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclModel139"):
                opp_val = getattr(old_value, "OclModel139", None)
                if opp_val == self:
                    setattr(old_value, "OclModel139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel139"):
                opp_val = getattr(value, "OclModel139", None)
                setattr(value, "OclModel139", self)

    @property
    def atl_n_ocl_OCL_OclModel143(self):
        return self.__atl_n_ocl_OCL_OclModel143

    @atl_n_ocl_OCL_OclModel143.setter
    def atl_n_ocl_OCL_OclModel143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_OclModel__atl_n_ocl_OCL_OclModel143", None)
        self.__atl_n_ocl_OCL_OclModel143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel144"):
                    opp_val = getattr(item, "OclModel144", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel144"):
                    opp_val = getattr(item, "OclModel144", None)
                    
                    setattr(item, "OclModel144", self)
                    

class atl_n_ocl_OCL_OclFeature(ABC):

    pass
class atl_n_ocl_OCL_OclContextDefinition:

    pass
class OclContextDefinition:

    pass
class OclFeature:

    pass
class atl_n_ocl_OCL_OclFeatureDefinition:

    pass
class atl_n_ocl_OCL_TupleTypeAttribute:

    def __init__(self, name: str, atl_n_ocl_OCL_TupleTypeAttribute: "OclType" = None):
        self.name = name
        self.atl_n_ocl_OCL_TupleTypeAttribute = atl_n_ocl_OCL_TupleTypeAttribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atl_n_ocl_OCL_TupleTypeAttribute(self):
        return self.__atl_n_ocl_OCL_TupleTypeAttribute

    @atl_n_ocl_OCL_TupleTypeAttribute.setter
    def atl_n_ocl_OCL_TupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_TupleTypeAttribute__atl_n_ocl_OCL_TupleTypeAttribute", None)
        self.__atl_n_ocl_OCL_TupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType114"):
                opp_val = getattr(old_value, "OclType114", None)
                if opp_val == self:
                    setattr(old_value, "OclType114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType114"):
                opp_val = getattr(value, "OclType114", None)
                setattr(value, "OclType114", self)

class TupleTypeAttribute:

    pass
class atl_n_ocl_OCL_Operation(OclFeature):

    def __init__(self, name: str, atl_n_ocl_OCL_Operation: set["Parameter"] = None, atl_n_ocl_OCL_Operation133: "OclType" = None, atl_n_ocl_OCL_Operation136: "OclExpression" = None, OclFeature: "atl_n_ocl_OCL_OclFeatureDefinition"):
        self.name = name
        self.atl_n_ocl_OCL_Operation = atl_n_ocl_OCL_Operation if atl_n_ocl_OCL_Operation is not None else set()
        self.atl_n_ocl_OCL_Operation133 = atl_n_ocl_OCL_Operation133
        self.atl_n_ocl_OCL_Operation136 = atl_n_ocl_OCL_Operation136
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atl_n_ocl_OCL_Operation133(self):
        return self.__atl_n_ocl_OCL_Operation133

    @atl_n_ocl_OCL_Operation133.setter
    def atl_n_ocl_OCL_Operation133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_Operation__atl_n_ocl_OCL_Operation133", None)
        self.__atl_n_ocl_OCL_Operation133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType134"):
                opp_val = getattr(old_value, "OclType134", None)
                if opp_val == self:
                    setattr(old_value, "OclType134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType134"):
                opp_val = getattr(value, "OclType134", None)
                setattr(value, "OclType134", self)

    @property
    def atl_n_ocl_OCL_Operation136(self):
        return self.__atl_n_ocl_OCL_Operation136

    @atl_n_ocl_OCL_Operation136.setter
    def atl_n_ocl_OCL_Operation136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_Operation__atl_n_ocl_OCL_Operation136", None)
        self.__atl_n_ocl_OCL_Operation136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression137"):
                opp_val = getattr(old_value, "OclExpression137", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression137"):
                opp_val = getattr(value, "OclExpression137", None)
                setattr(value, "OclExpression137", self)

    @property
    def atl_n_ocl_OCL_Operation(self):
        return self.__atl_n_ocl_OCL_Operation

    @atl_n_ocl_OCL_Operation.setter
    def atl_n_ocl_OCL_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_Operation__atl_n_ocl_OCL_Operation", None)
        self.__atl_n_ocl_OCL_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter131"):
                    opp_val = getattr(item, "Parameter131", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter131"):
                    opp_val = getattr(item, "Parameter131", None)
                    
                    setattr(item, "Parameter131", self)
                    

class atl_n_ocl_OCL_Attribute(OclFeature):

    def __init__(self, name: str, atl_n_ocl_OCL_Attribute: "OclExpression" = None, atl_n_ocl_OCL_Attribute128: "OclType" = None, OclFeature: "atl_n_ocl_OCL_OclFeatureDefinition"):
        self.name = name
        self.atl_n_ocl_OCL_Attribute = atl_n_ocl_OCL_Attribute
        self.atl_n_ocl_OCL_Attribute128 = atl_n_ocl_OCL_Attribute128
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atl_n_ocl_OCL_Attribute128(self):
        return self.__atl_n_ocl_OCL_Attribute128

    @atl_n_ocl_OCL_Attribute128.setter
    def atl_n_ocl_OCL_Attribute128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_Attribute__atl_n_ocl_OCL_Attribute128", None)
        self.__atl_n_ocl_OCL_Attribute128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType129"):
                opp_val = getattr(old_value, "OclType129", None)
                if opp_val == self:
                    setattr(old_value, "OclType129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType129"):
                opp_val = getattr(value, "OclType129", None)
                setattr(value, "OclType129", self)

    @property
    def atl_n_ocl_OCL_Attribute(self):
        return self.__atl_n_ocl_OCL_Attribute

    @atl_n_ocl_OCL_Attribute.setter
    def atl_n_ocl_OCL_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_Attribute__atl_n_ocl_OCL_Attribute", None)
        self.__atl_n_ocl_OCL_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression126"):
                opp_val = getattr(old_value, "OclExpression126", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression126"):
                opp_val = getattr(value, "OclExpression126", None)
                setattr(value, "OclExpression126", self)

class Primitive:

    pass
class atl_n_ocl_OCL_StringType(Primitive):

    pass
class atl_n_ocl_OCL_VariableDeclaration:

    def __init__(self, id: str, varName: str, atl_n_ocl_OCL_VariableDeclaration: "OclType" = None, atl_n_ocl_OCL_VariableDeclaration108: "OclExpression" = None):
        self.id = id
        self.varName = varName
        self.atl_n_ocl_OCL_VariableDeclaration = atl_n_ocl_OCL_VariableDeclaration
        self.atl_n_ocl_OCL_VariableDeclaration108 = atl_n_ocl_OCL_VariableDeclaration108
        
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
    def atl_n_ocl_OCL_VariableDeclaration108(self):
        return self.__atl_n_ocl_OCL_VariableDeclaration108

    @atl_n_ocl_OCL_VariableDeclaration108.setter
    def atl_n_ocl_OCL_VariableDeclaration108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_VariableDeclaration__atl_n_ocl_OCL_VariableDeclaration108", None)
        self.__atl_n_ocl_OCL_VariableDeclaration108 = value
        
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
    def atl_n_ocl_OCL_VariableDeclaration(self):
        return self.__atl_n_ocl_OCL_VariableDeclaration

    @atl_n_ocl_OCL_VariableDeclaration.setter
    def atl_n_ocl_OCL_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_VariableDeclaration__atl_n_ocl_OCL_VariableDeclaration", None)
        self.__atl_n_ocl_OCL_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType106"):
                opp_val = getattr(old_value, "OclType106", None)
                if opp_val == self:
                    setattr(old_value, "OclType106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType106"):
                opp_val = getattr(value, "OclType106", None)
                setattr(value, "OclType106", self)

class CollectionType:

    pass
class atl_n_ocl_OCL_SequenceType(CollectionType):

    pass
class atl_n_ocl_OCL_SetType(CollectionType):

    pass
class atl_n_ocl_OCL_OrderedSetType(CollectionType):

    pass
class atl_n_ocl_OCL_BagType(CollectionType):

    pass
class NumericType:

    pass
class atl_n_ocl_OCL_RealType(NumericType):

    pass
class atl_n_ocl_OCL_IntegerType(NumericType):

    pass
class atl_n_ocl_OCL_NumericType(Primitive):

    pass
class atl_n_ocl_OCL_BooleanType(Primitive):

    pass
class LoopExp:

    pass
class atl_n_ocl_OCL_IteratorExp(LoopExp):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class atl_n_ocl_OCL_IterateExp(LoopExp):

    pass
class OperationCallExp:

    pass
class atl_n_ocl_OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class atl_n_ocl_OCL_OperatorCallExp(OperationCallExp):

    pass
class atl_n_ocl_OCL_MapElement:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class TuplePart:

    pass
class CollectionExp:

    pass
class atl_n_ocl_OCL_SequenceExp(CollectionExp):

    pass
class atl_n_ocl_OCL_SetExp(CollectionExp):

    pass
class atl_n_ocl_OCL_OrderedSetExp(CollectionExp):

    pass
class atl_n_ocl_OCL_BagExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class atl_n_ocl_OCL_LoopExp(PropertyCallExp):

    pass
class atl_n_ocl_OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, atl_n_ocl_OCL_OperationCallExp: set["OclExpression"] = None):
        self.operationName = operationName
        self.atl_n_ocl_OCL_OperationCallExp = atl_n_ocl_OCL_OperationCallExp if atl_n_ocl_OCL_OperationCallExp is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def atl_n_ocl_OCL_OperationCallExp(self):
        return self.__atl_n_ocl_OCL_OperationCallExp

    @atl_n_ocl_OCL_OperationCallExp.setter
    def atl_n_ocl_OCL_OperationCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_OCL_OperationCallExp__atl_n_ocl_OCL_OperationCallExp", None)
        self.__atl_n_ocl_OCL_OperationCallExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression84"):
                    opp_val = getattr(item, "OclExpression84", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression84"):
                    opp_val = getattr(item, "OclExpression84", None)
                    
                    setattr(item, "OclExpression84", self)
                    

class atl_n_ocl_OCL_NavigationOrAttributeCallExp(PropertyCallExp):

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
class atl_n_ocl_OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: int):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> int:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: int):
        self.__integerSymbol = integerSymbol

class atl_n_ocl_OCL_RealExp(NumericExp):

    def __init__(self, realSymbol: float):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> float:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: float):
        self.__realSymbol = realSymbol

class PrimitiveExp:

    pass
class atl_n_ocl_OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: bool):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> bool:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: bool):
        self.__booleanSymbol = booleanSymbol

class atl_n_ocl_OCL_NumericExp(PrimitiveExp):

    pass
class atl_n_ocl_OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class OclType:

    pass
class atl_n_ocl_OCL_Primitive(OclType):

    pass
class atl_n_ocl_OCL_TupleType(OclType):

    pass
class atl_n_ocl_OCL_MapType(OclType):

    pass
class atl_n_ocl_OCL_CollectionType(OclType):

    pass
class atl_n_ocl_OCL_OclAnyType(OclType):

    pass
class atl_n_ocl_OCL_OclModelElement(OclType):

    pass
class atl_n_ocl_OCL_OclExpression(ABC):

    pass
class atl_n_ocl_ATL_Statement(ABC):

    pass
class Statement:

    pass
class atl_n_ocl_ATL_ExpressionStat(Statement):

    pass
class atl_n_ocl_ATL_BindingStat(Statement):

    def __init__(self, isAssignment: bool, propertyName: str, atl_n_ocl_ATL_BindingStat51: "OclExpression" = None, atl_n_ocl_ATL_BindingStat: "OclExpression" = None, Statement: "atl_n_ocl_ATL_ActionBlock", Statement60: "atl_n_ocl_ATL_IfStat", Statement57: "atl_n_ocl_ATL_IfStat", Statement68: "atl_n_ocl_ATL_ForStat"):
        self.isAssignment = isAssignment
        self.propertyName = propertyName
        self.atl_n_ocl_ATL_BindingStat51 = atl_n_ocl_ATL_BindingStat51
        self.atl_n_ocl_ATL_BindingStat = atl_n_ocl_ATL_BindingStat
        
    @property
    def isAssignment(self) -> bool:
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: bool):
        self.__isAssignment = isAssignment

    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def atl_n_ocl_ATL_BindingStat51(self):
        return self.__atl_n_ocl_ATL_BindingStat51

    @atl_n_ocl_ATL_BindingStat51.setter
    def atl_n_ocl_ATL_BindingStat51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_BindingStat__atl_n_ocl_ATL_BindingStat51", None)
        self.__atl_n_ocl_ATL_BindingStat51 = value
        
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

    @property
    def atl_n_ocl_ATL_BindingStat(self):
        return self.__atl_n_ocl_ATL_BindingStat

    @atl_n_ocl_ATL_BindingStat.setter
    def atl_n_ocl_ATL_BindingStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_BindingStat__atl_n_ocl_ATL_BindingStat", None)
        self.__atl_n_ocl_ATL_BindingStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression49"):
                opp_val = getattr(old_value, "OclExpression49", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression49"):
                opp_val = getattr(value, "OclExpression49", None)
                setattr(value, "OclExpression49", self)

class atl_n_ocl_ATL_ForStat(Statement):

    pass
class atl_n_ocl_ATL_ActionBlock:

    pass
class atl_n_ocl_ATL_Binding:

    def __init__(self, propertyName: str, isAssignment: bool, atl_n_ocl_ATL_Binding: "OclExpression" = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atl_n_ocl_ATL_Binding = atl_n_ocl_ATL_Binding
        
    @property
    def isAssignment(self) -> bool:
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: bool):
        self.__isAssignment = isAssignment

    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def atl_n_ocl_ATL_Binding(self):
        return self.__atl_n_ocl_ATL_Binding

    @atl_n_ocl_ATL_Binding.setter
    def atl_n_ocl_ATL_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_Binding__atl_n_ocl_ATL_Binding", None)
        self.__atl_n_ocl_ATL_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression44"):
                opp_val = getattr(old_value, "OclExpression44", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression44"):
                opp_val = getattr(value, "OclExpression44", None)
                setattr(value, "OclExpression44", self)

class Iterator:

    pass
class atl_n_ocl_ATL_IfStat(Statement):

    pass
class PatternElement:

    pass
class atl_n_ocl_ATL_InPatternElement(PatternElement):

    pass
class VariableDeclaration:

    pass
class atl_n_ocl_OCL_Iterator(VariableDeclaration):

    pass
class atl_n_ocl_OCL_TuplePart(VariableDeclaration):

    pass
class atl_n_ocl_OCL_Parameter(VariableDeclaration):

    pass
class atl_n_ocl_ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class atl_n_ocl_ATL_PatternElement(VariableDeclaration):

    pass
class atl_n_ocl_ATL_DropPattern:

    pass
class OutPatternElement:

    pass
class atl_n_ocl_ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class DropPattern:

    pass
class atl_n_ocl_ATL_OutPattern:

    pass
class InPatternElement:

    pass
class atl_n_ocl_ATL_SimpleInPatternElement(InPatternElement):

    pass
class atl_n_ocl_ATL_InPattern:

    pass
class Parameter:

    pass
class atl_n_ocl_ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class Binding:

    pass
class atl_n_ocl_ATL_OutPatternElement(PatternElement):

    pass
class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class OutPattern:

    pass
class OclFeatureDefinition:

    pass
class atl_n_ocl_ATL_ModuleElement(ABC):

    pass
class ModuleElement:

    pass
class atl_n_ocl_ATL_Helper(ModuleElement):

    pass
class atl_n_ocl_ATL_Rule(ModuleElement):

    def __init__(self, name: str, atl_n_ocl_ATL_Rule: "OutPattern" = None, atl_n_ocl_ATL_Rule12: "ActionBlock" = None, atl_n_ocl_ATL_Rule14: set["RuleVariableDeclaration"] = None, ModuleElement: "atl_n_ocl_ATL_Module"):
        self.name = name
        self.atl_n_ocl_ATL_Rule = atl_n_ocl_ATL_Rule
        self.atl_n_ocl_ATL_Rule12 = atl_n_ocl_ATL_Rule12
        self.atl_n_ocl_ATL_Rule14 = atl_n_ocl_ATL_Rule14 if atl_n_ocl_ATL_Rule14 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atl_n_ocl_ATL_Rule(self):
        return self.__atl_n_ocl_ATL_Rule

    @atl_n_ocl_ATL_Rule.setter
    def atl_n_ocl_ATL_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_Rule__atl_n_ocl_ATL_Rule", None)
        self.__atl_n_ocl_ATL_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutPattern"):
                opp_val = getattr(old_value, "OutPattern", None)
                if opp_val == self:
                    setattr(old_value, "OutPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutPattern"):
                opp_val = getattr(value, "OutPattern", None)
                setattr(value, "OutPattern", self)

    @property
    def atl_n_ocl_ATL_Rule12(self):
        return self.__atl_n_ocl_ATL_Rule12

    @atl_n_ocl_ATL_Rule12.setter
    def atl_n_ocl_ATL_Rule12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_Rule__atl_n_ocl_ATL_Rule12", None)
        self.__atl_n_ocl_ATL_Rule12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionBlock"):
                opp_val = getattr(old_value, "ActionBlock", None)
                if opp_val == self:
                    setattr(old_value, "ActionBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionBlock"):
                opp_val = getattr(value, "ActionBlock", None)
                setattr(value, "ActionBlock", self)

    @property
    def atl_n_ocl_ATL_Rule14(self):
        return self.__atl_n_ocl_ATL_Rule14

    @atl_n_ocl_ATL_Rule14.setter
    def atl_n_ocl_ATL_Rule14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_Rule__atl_n_ocl_ATL_Rule14", None)
        self.__atl_n_ocl_ATL_Rule14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RuleVariableDeclaration"):
                    opp_val = getattr(item, "RuleVariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "RuleVariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RuleVariableDeclaration"):
                    opp_val = getattr(item, "RuleVariableDeclaration", None)
                    
                    setattr(item, "RuleVariableDeclaration", self)
                    

class OclModel:

    pass
class atl_n_ocl_ATL_Module:

    def __init__(self, isRefining: bool, atl_n_ocl_ATL_Module: set["OclModel"] = None, atl_n_ocl_ATL_Module5: set["OclModel"] = None, atl_n_ocl_ATL_Module8: set["ModuleElement"] = None):
        self.isRefining = isRefining
        self.atl_n_ocl_ATL_Module = atl_n_ocl_ATL_Module if atl_n_ocl_ATL_Module is not None else set()
        self.atl_n_ocl_ATL_Module5 = atl_n_ocl_ATL_Module5 if atl_n_ocl_ATL_Module5 is not None else set()
        self.atl_n_ocl_ATL_Module8 = atl_n_ocl_ATL_Module8 if atl_n_ocl_ATL_Module8 is not None else set()
        
    @property
    def isRefining(self) -> bool:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: bool):
        self.__isRefining = isRefining

    @property
    def atl_n_ocl_ATL_Module5(self):
        return self.__atl_n_ocl_ATL_Module5

    @atl_n_ocl_ATL_Module5.setter
    def atl_n_ocl_ATL_Module5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_Module__atl_n_ocl_ATL_Module5", None)
        self.__atl_n_ocl_ATL_Module5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel6"):
                    opp_val = getattr(item, "OclModel6", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel6"):
                    opp_val = getattr(item, "OclModel6", None)
                    
                    setattr(item, "OclModel6", self)
                    

    @property
    def atl_n_ocl_ATL_Module(self):
        return self.__atl_n_ocl_ATL_Module

    @atl_n_ocl_ATL_Module.setter
    def atl_n_ocl_ATL_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_Module__atl_n_ocl_ATL_Module", None)
        self.__atl_n_ocl_ATL_Module = value if value is not None else set()
        
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
    def atl_n_ocl_ATL_Module8(self):
        return self.__atl_n_ocl_ATL_Module8

    @atl_n_ocl_ATL_Module8.setter
    def atl_n_ocl_ATL_Module8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_Module__atl_n_ocl_ATL_Module8", None)
        self.__atl_n_ocl_ATL_Module8 = value if value is not None else set()
        
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
                    

class MatchedRule:

    pass
class atl_n_ocl_ATL_LazyMatchedRule(MatchedRule):

    def __init__(self, isUnique: bool, MatchedRule: "atl_n_ocl_ATL_MatchedRule"):
        self.isUnique = isUnique
        
    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

class InPattern:

    pass
class Rule:

    pass
class atl_n_ocl_ATL_CalledRule(Rule):

    def __init__(self, isEntrypoint: bool, isEndpoint: bool, atl_n_ocl_ATL_CalledRule: set["Parameter"] = None):
        self.isEntrypoint = isEntrypoint
        self.isEndpoint = isEndpoint
        self.atl_n_ocl_ATL_CalledRule = atl_n_ocl_ATL_CalledRule if atl_n_ocl_ATL_CalledRule is not None else set()
        
    @property
    def isEndpoint(self) -> bool:
        return self.__isEndpoint

    @isEndpoint.setter
    def isEndpoint(self, isEndpoint: bool):
        self.__isEndpoint = isEndpoint

    @property
    def isEntrypoint(self) -> bool:
        return self.__isEntrypoint

    @isEntrypoint.setter
    def isEntrypoint(self, isEntrypoint: bool):
        self.__isEntrypoint = isEntrypoint

    @property
    def atl_n_ocl_ATL_CalledRule(self):
        return self.__atl_n_ocl_ATL_CalledRule

    @atl_n_ocl_ATL_CalledRule.setter
    def atl_n_ocl_ATL_CalledRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_CalledRule__atl_n_ocl_ATL_CalledRule", None)
        self.__atl_n_ocl_ATL_CalledRule = value if value is not None else set()
        
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
                    

class atl_n_ocl_ATL_MatchedRule(Rule):

    def __init__(self, isAbstract: bool, isRefining: bool, isNoDefault: bool, atl_n_ocl_ATL_MatchedRule: "InPattern" = None, atl_n_ocl_ATL_MatchedRule17: set["MatchedRule"] = None):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.atl_n_ocl_ATL_MatchedRule = atl_n_ocl_ATL_MatchedRule
        self.atl_n_ocl_ATL_MatchedRule17 = atl_n_ocl_ATL_MatchedRule17 if atl_n_ocl_ATL_MatchedRule17 is not None else set()
        
    @property
    def isNoDefault(self) -> bool:
        return self.__isNoDefault

    @isNoDefault.setter
    def isNoDefault(self, isNoDefault: bool):
        self.__isNoDefault = isNoDefault

    @property
    def isRefining(self) -> bool:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: bool):
        self.__isRefining = isRefining

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def atl_n_ocl_ATL_MatchedRule(self):
        return self.__atl_n_ocl_ATL_MatchedRule

    @atl_n_ocl_ATL_MatchedRule.setter
    def atl_n_ocl_ATL_MatchedRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_MatchedRule__atl_n_ocl_ATL_MatchedRule", None)
        self.__atl_n_ocl_ATL_MatchedRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InPattern"):
                opp_val = getattr(old_value, "InPattern", None)
                if opp_val == self:
                    setattr(old_value, "InPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InPattern"):
                opp_val = getattr(value, "InPattern", None)
                setattr(value, "InPattern", self)

    @property
    def atl_n_ocl_ATL_MatchedRule17(self):
        return self.__atl_n_ocl_ATL_MatchedRule17

    @atl_n_ocl_ATL_MatchedRule17.setter
    def atl_n_ocl_ATL_MatchedRule17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_n_ocl_ATL_MatchedRule__atl_n_ocl_ATL_MatchedRule17", None)
        self.__atl_n_ocl_ATL_MatchedRule17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MatchedRule"):
                    opp_val = getattr(item, "MatchedRule", None)
                    
                    if opp_val == self:
                        setattr(item, "MatchedRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MatchedRule"):
                    opp_val = getattr(item, "MatchedRule", None)
                    
                    setattr(item, "MatchedRule", self)
                    

class Helper:

    pass
class OclExpression:

    pass
class atl_n_ocl_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression77: "atl_n_ocl_OCL_MapElement", OclExpression40: "atl_n_ocl_ATL_ForEachOutPatternElement", OclExpression126: "atl_n_ocl_OCL_Attribute", OclExpression80: "atl_n_ocl_OCL_MapElement", OclExpression72: "atl_n_ocl_OCL_CollectionExp", OclExpression109: "atl_n_ocl_OCL_VariableDeclaration", OclExpression104: "atl_n_ocl_OCL_IfExp", OclExpression101: "atl_n_ocl_OCL_IfExp", OclExpression86: "atl_n_ocl_OCL_LoopExp", OclExpression22: "atl_n_ocl_ATL_InPattern", OclExpression98: "atl_n_ocl_OCL_IfExp", OclExpression44: "atl_n_ocl_ATL_Binding", OclExpression96: "atl_n_ocl_OCL_LetExp", OclExpression38: "atl_n_ocl_ATL_SimpleOutPatternElement", OclExpression137: "atl_n_ocl_OCL_Operation", OclExpression47: "atl_n_ocl_ATL_ExpressionStat", OclExpression54: "atl_n_ocl_ATL_IfStat", OclExpression49: "atl_n_ocl_ATL_BindingStat", OclExpression82: "atl_n_ocl_OCL_PropertyCallExp", OclExpression: "atl_n_ocl_ATL_Query", OclExpression52: "atl_n_ocl_ATL_BindingStat", OclExpression65: "atl_n_ocl_ATL_ForStat", OclExpression84: "atl_n_ocl_OCL_OperationCallExp"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class atl_n_ocl_OCL_CollectionExp(OclExpression):

    pass
class atl_n_ocl_OCL_MapExp(OclExpression):

    pass
class atl_n_ocl_OCL_PropertyCallExp(OclExpression):

    pass
class atl_n_ocl_OCL_TupleExp(OclExpression):

    pass
class atl_n_ocl_OCL_SuperExp(OclExpression):

    pass
class atl_n_ocl_OCL_IfExp(OclExpression):

    pass
class atl_n_ocl_OCL_PrimitiveExp(OclExpression):

    pass
class atl_n_ocl_OCL_VariableExp(OclExpression):

    pass
class atl_n_ocl_OCL_OclType(OclExpression):

    def __init__(self, name: str, OclExpression77: "atl_n_ocl_OCL_MapElement", OclExpression40: "atl_n_ocl_ATL_ForEachOutPatternElement", OclExpression126: "atl_n_ocl_OCL_Attribute", OclExpression80: "atl_n_ocl_OCL_MapElement", OclExpression72: "atl_n_ocl_OCL_CollectionExp", OclExpression109: "atl_n_ocl_OCL_VariableDeclaration", OclExpression104: "atl_n_ocl_OCL_IfExp", OclExpression101: "atl_n_ocl_OCL_IfExp", OclExpression86: "atl_n_ocl_OCL_LoopExp", OclExpression22: "atl_n_ocl_ATL_InPattern", OclExpression98: "atl_n_ocl_OCL_IfExp", OclExpression44: "atl_n_ocl_ATL_Binding", OclExpression96: "atl_n_ocl_OCL_LetExp", OclExpression38: "atl_n_ocl_ATL_SimpleOutPatternElement", OclExpression137: "atl_n_ocl_OCL_Operation", OclExpression47: "atl_n_ocl_ATL_ExpressionStat", OclExpression54: "atl_n_ocl_ATL_IfStat", OclExpression49: "atl_n_ocl_ATL_BindingStat", OclExpression82: "atl_n_ocl_OCL_PropertyCallExp", OclExpression: "atl_n_ocl_ATL_Query", OclExpression52: "atl_n_ocl_ATL_BindingStat", OclExpression65: "atl_n_ocl_ATL_ForStat", OclExpression84: "atl_n_ocl_OCL_OperationCallExp"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class atl_n_ocl_OCL_LetExp(OclExpression):

    pass
class atl_n_ocl_OCL_OclUndefinedExp(OclExpression):

    pass
class atl_n_ocl_ATL_Query:

    pass