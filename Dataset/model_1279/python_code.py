from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EMultiplicity(Enum):
    one = "one"
    many = "many"
class EIteratorKind(Enum):
    forAll = "forAll"
    exists = "exists"
    collect = "collect"
    select = "select"
class EOperator(Enum):
    equal = "equal"
    allInstances = "allInstances"
    greater = "greater"
    less = "less"
    notEqual = "notEqual"
    greaterOrEqual = "greaterOrEqual"
    lessOrEqual = "lessOrEqual"
    AND = "AND"
    OR = "OR"
    size = "size"
    isEmpty = "isEmpty"
    oclIsUndefined = "oclIsUndefined"
    flatten = "flatten"
    notEmpty = "notEmpty"
    isUnique = "isUnique"


############################################
# Definition of Classes
############################################

class ocl_type_ESignal:

    pass
class ocl_type_EClassifier(ABC):

    pass
class EFeatureCallExp:

    pass
class ocl_exp_EOperationCallExp(EFeatureCallExp):

    def __init__(self, referredOperation: str, EOclExpression43: set["EOclExpression"] = None):
        self.referredOperation = referredOperation
        self.EOclExpression43 = EOclExpression43 if EOclExpression43 is not None else set()
        
    @property
    def referredOperation(self) -> str:
        return self.__referredOperation

    @referredOperation.setter
    def referredOperation(self, referredOperation: str):
        self.__referredOperation = referredOperation

    @property
    def EOclExpression43(self):
        return self.__EOclExpression43

    @EOclExpression43.setter
    def EOclExpression43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_exp_EOperationCallExp__EOclExpression43", None)
        self.__EOclExpression43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "exp44"):
                    opp_val = getattr(item, "exp44", None)
                    
                    if opp_val == self:
                        setattr(item, "exp44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "exp44"):
                    opp_val = getattr(item, "exp44", None)
                    
                    setattr(item, "exp44", self)
                    

class ocl_exp_ENavigationCallExp(EFeatureCallExp):

    pass
class ELiteralExp:

    pass
class ocl_exp_EPrimitiveType(ELiteralExp):

    pass
class ENumericLiteralExp:

    pass
class ocl_exp_EIntegerLiteralExp(ENumericLiteralExp):

    def __init__(self, integerValue: str):
        self.integerValue = integerValue
        
    @property
    def integerValue(self) -> str:
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: str):
        self.__integerValue = integerValue

class ECollectionType:

    pass
class ocl_type_ESequenceType(ECollectionType):

    pass
class ocl_type_EBagType(ECollectionType):

    pass
class ocl_type_ESetType(ECollectionType):

    pass
class ocl_type_EOrderedSetType(ECollectionType):

    pass
class EDataType:

    pass
class ocl_type_EPrimitiveType(EDataType):

    pass
class ocl_type_ETupleType(EDataType):

    pass
class ocl_type_ECollectionType(EDataType):

    pass
class ESignal:

    pass
class ocl_exp_EOclExpression(ABC):

    pass
class ELoopExp:

    pass
class ocl_exp_EIteratorExp(ELoopExp):

    def __init__(self, kind: str, exp18: "ocl_exp_EVariable", exp26: "ocl_exp_EOclExpression"):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class ocl_exp_EVariable:

    def __init__(self, name: str, ELoopExp: "ELoopExp" = None, EOclExpression20: "EOclExpression" = None):
        self.name = name
        self.ELoopExp = ELoopExp
        self.EOclExpression20 = EOclExpression20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ELoopExp(self):
        return self.__ELoopExp

    @ELoopExp.setter
    def ELoopExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_exp_EVariable__ELoopExp", None)
        self.__ELoopExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exp18"):
                opp_val = getattr(old_value, "exp18", None)
                if opp_val == self:
                    setattr(old_value, "exp18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exp18"):
                opp_val = getattr(value, "exp18", None)
                setattr(value, "exp18", self)

    @property
    def EOclExpression20(self):
        return self.__EOclExpression20

    @EOclExpression20.setter
    def EOclExpression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_exp_EVariable__EOclExpression20", None)
        self.__EOclExpression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exp21"):
                opp_val = getattr(old_value, "exp21", None)
                if opp_val == self:
                    setattr(old_value, "exp21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exp21"):
                opp_val = getattr(value, "exp21", None)
                setattr(value, "exp21", self)

class EPrimitiveType:

    pass
class ocl_exp_EBooleanLiteralExp(EPrimitiveType):

    def __init__(self, booleanValue: str):
        self.booleanValue = booleanValue
        
    @property
    def booleanValue(self) -> str:
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: str):
        self.__booleanValue = booleanValue

class ocl_exp_EStringLiteralExp(EPrimitiveType):

    def __init__(self, stringValue: str):
        self.stringValue = stringValue
        
    @property
    def stringValue(self) -> str:
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue

class ocl_exp_ENumericLiteralExp(EPrimitiveType):

    pass
class ENavigationCallExp:

    pass
class ocl_exp_EPropertyCallExp(ENavigationCallExp):

    pass
class ocl_exp_EAssociationClassCallExp(ENavigationCallExp):

    pass
class EOperationCallExp:

    pass
class ocl_dm_EAttribute:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ocl_dm_EDataModel:

    pass
class ECallExp:

    pass
class ocl_exp_EFeatureCallExp(ECallExp):

    pass
class ocl_exp_ELoopExp(ECallExp):

    pass
class EVariable:

    pass
class EOclExpression:

    pass
class ocl_exp_ELiteralExp(EOclExpression):

    pass
class ocl_exp_ETypeExp(EOclExpression):

    pass
class ocl_exp_ECallExp(EOclExpression):

    pass
class ocl_exp_EVariableExp(EOclExpression):

    pass
class EClassifier:

    pass
class ocl_type_EDataType(EClassifier):

    pass
class ocl_type_EMessageType(EClassifier):

    def __init__(self, referredOperation: str, ocl_type_EMessageType: "ESignal" = None, EClassifier: "ocl_exp_ETypeExp", EClassifier47: "ocl_type_ECollectionType"):
        self.referredOperation = referredOperation
        self.ocl_type_EMessageType = ocl_type_EMessageType
        
    @property
    def referredOperation(self) -> str:
        return self.__referredOperation

    @referredOperation.setter
    def referredOperation(self, referredOperation: str):
        self.__referredOperation = referredOperation

    @property
    def ocl_type_EMessageType(self):
        return self.__ocl_type_EMessageType

    @ocl_type_EMessageType.setter
    def ocl_type_EMessageType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_type_EMessageType__ocl_type_EMessageType", None)
        self.__ocl_type_EMessageType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ESignal"):
                opp_val = getattr(old_value, "ESignal", None)
                if opp_val == self:
                    setattr(old_value, "ESignal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ESignal"):
                opp_val = getattr(value, "ESignal", None)
                setattr(value, "ESignal", self)

class ocl_type_EInvalidType(EClassifier):

    pass
class ocl_type_EVoidType(EClassifier):

    pass
class ocl_type_EAnyType(EClassifier):

    pass
class ocl_dm_EEntity(EClassifier):

    def __init__(self, name: str, ocl_dm_EEntity: set["EAssociationEnd"] = None, ocl_dm_EEntity2: set["EAttribute"] = None, EClassifier: "ocl_exp_ETypeExp", EClassifier47: "ocl_type_ECollectionType"):
        self.name = name
        self.ocl_dm_EEntity = ocl_dm_EEntity if ocl_dm_EEntity is not None else set()
        self.ocl_dm_EEntity2 = ocl_dm_EEntity2 if ocl_dm_EEntity2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ocl_dm_EEntity(self):
        return self.__ocl_dm_EEntity

    @ocl_dm_EEntity.setter
    def ocl_dm_EEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_dm_EEntity__ocl_dm_EEntity", None)
        self.__ocl_dm_EEntity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EAssociationEnd"):
                    opp_val = getattr(item, "EAssociationEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "EAssociationEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EAssociationEnd"):
                    opp_val = getattr(item, "EAssociationEnd", None)
                    
                    setattr(item, "EAssociationEnd", self)
                    

    @property
    def ocl_dm_EEntity2(self):
        return self.__ocl_dm_EEntity2

    @ocl_dm_EEntity2.setter
    def ocl_dm_EEntity2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_dm_EEntity__ocl_dm_EEntity2", None)
        self.__ocl_dm_EEntity2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EAttribute"):
                    opp_val = getattr(item, "EAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "EAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EAttribute"):
                    opp_val = getattr(item, "EAttribute", None)
                    
                    setattr(item, "EAttribute", self)
                    

class EEntity:

    pass
class ocl_dm_EAssociationEnd:

    def __init__(self, name: str, mult: str, ocl_dm_EAssociationEnd: "EEntity" = None, ocl_dm_EAssociationEnd5: "EAssociationEnd" = None):
        self.name = name
        self.mult = mult
        self.ocl_dm_EAssociationEnd = ocl_dm_EAssociationEnd
        self.ocl_dm_EAssociationEnd5 = ocl_dm_EAssociationEnd5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mult(self) -> str:
        return self.__mult

    @mult.setter
    def mult(self, mult: str):
        self.__mult = mult

    @property
    def ocl_dm_EAssociationEnd(self):
        return self.__ocl_dm_EAssociationEnd

    @ocl_dm_EAssociationEnd.setter
    def ocl_dm_EAssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_dm_EAssociationEnd__ocl_dm_EAssociationEnd", None)
        self.__ocl_dm_EAssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EEntity"):
                opp_val = getattr(old_value, "EEntity", None)
                if opp_val == self:
                    setattr(old_value, "EEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EEntity"):
                opp_val = getattr(value, "EEntity", None)
                setattr(value, "EEntity", self)

    @property
    def ocl_dm_EAssociationEnd5(self):
        return self.__ocl_dm_EAssociationEnd5

    @ocl_dm_EAssociationEnd5.setter
    def ocl_dm_EAssociationEnd5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_dm_EAssociationEnd__ocl_dm_EAssociationEnd5", None)
        self.__ocl_dm_EAssociationEnd5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EAssociationEnd6"):
                opp_val = getattr(old_value, "EAssociationEnd6", None)
                if opp_val == self:
                    setattr(old_value, "EAssociationEnd6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EAssociationEnd6"):
                opp_val = getattr(value, "EAssociationEnd6", None)
                setattr(value, "EAssociationEnd6", self)

class EAttribute:

    pass
class EAssociationEnd:

    pass