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
    XOR = "XOR"
    IMPLIES = "IMPLIES"
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
class ECollectionType:

    pass
class ocl_type_ESetType(ECollectionType):

    pass
class ocl_type_EBagType(ECollectionType):

    pass
class ocl_type_ESequenceType(ECollectionType):

    pass
class ocl_type_EOrderedSetType(ECollectionType):

    pass
class EDataType:

    pass
class ocl_type_ETupleType(EDataType):

    pass
class ocl_type_EPrimitiveType(EDataType):

    pass
class ocl_type_ECollectionType(EDataType):

    pass
class ESignal:

    pass
class ocl_type_EClassifier(ABC):

    pass
class EIfExp:

    pass
class EFeatureCallExp:

    pass
class ocl_exp_EOperationCallExp(EFeatureCallExp):

    def __init__(self, referredOperation: str, EOclExpression53: set["EOclExpression"] = None):
        self.referredOperation = referredOperation
        self.EOclExpression53 = EOclExpression53 if EOclExpression53 is not None else set()
        
    @property
    def referredOperation(self) -> str:
        return self.__referredOperation

    @referredOperation.setter
    def referredOperation(self, referredOperation: str):
        self.__referredOperation = referredOperation

    @property
    def EOclExpression53(self):
        return self.__EOclExpression53

    @EOclExpression53.setter
    def EOclExpression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_exp_EOperationCallExp__EOclExpression53", None)
        self.__EOclExpression53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "exp54"):
                    opp_val = getattr(item, "exp54", None)
                    
                    if opp_val == self:
                        setattr(item, "exp54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "exp54"):
                    opp_val = getattr(item, "exp54", None)
                    
                    setattr(item, "exp54", self)
                    

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

class EOperationCallExp:

    pass
class ECallExp:

    pass
class ocl_exp_EOclExpression(ABC):

    pass
class EIterateExp:

    pass
class ELoopExp:

    pass
class ocl_exp_EIterateExp(ELoopExp):

    pass
class ocl_exp_EIteratorExp(ELoopExp):

    def __init__(self, kind: str, exp25: "ocl_exp_EOclExpression", exp15: "ocl_exp_EVariable"):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class ocl_exp_EVariable:

    def __init__(self, name: str, ELoopExp: "ELoopExp" = None, EIterateExp: "EIterateExp" = None, EOclExpression19: "EOclExpression" = None):
        self.name = name
        self.ELoopExp = ELoopExp
        self.EIterateExp = EIterateExp
        self.EOclExpression19 = EOclExpression19
        
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
            if hasattr(old_value, "exp15"):
                opp_val = getattr(old_value, "exp15", None)
                if opp_val == self:
                    setattr(old_value, "exp15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exp15"):
                opp_val = getattr(value, "exp15", None)
                setattr(value, "exp15", self)

    @property
    def EOclExpression19(self):
        return self.__EOclExpression19

    @EOclExpression19.setter
    def EOclExpression19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_exp_EVariable__EOclExpression19", None)
        self.__EOclExpression19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exp20"):
                opp_val = getattr(old_value, "exp20", None)
                if opp_val == self:
                    setattr(old_value, "exp20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exp20"):
                opp_val = getattr(value, "exp20", None)
                setattr(value, "exp20", self)

    @property
    def EIterateExp(self):
        return self.__EIterateExp

    @EIterateExp.setter
    def EIterateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ocl_exp_EVariable__EIterateExp", None)
        self.__EIterateExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exp17"):
                opp_val = getattr(old_value, "exp17", None)
                if opp_val == self:
                    setattr(old_value, "exp17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exp17"):
                opp_val = getattr(value, "exp17", None)
                setattr(value, "exp17", self)

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
class ocl_exp_EFeatureCallExp(ECallExp):

    pass
class EEntity:

    pass
class ocl_exp_ELoopExp(ECallExp):

    pass
class ocl_dm_EAssociationEnd:

    def __init__(self, name: str, opp: str, mult: str, ocl_dm_EAssociationEnd: "EEntity" = None):
        self.name = name
        self.opp = opp
        self.mult = mult
        self.ocl_dm_EAssociationEnd = ocl_dm_EAssociationEnd
        
    @property
    def opp(self) -> str:
        return self.__opp

    @opp.setter
    def opp(self, opp: str):
        self.__opp = opp

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

class EVariable:

    pass
class EOclExpression:

    pass
class ocl_exp_EIfExp(EOclExpression):

    pass
class ocl_exp_ECallExp(EOclExpression):

    pass
class ocl_exp_ELiteralExp(EOclExpression):

    pass
class ocl_exp_EMessageExp(EOclExpression):

    pass
class ocl_exp_EStateExp(EOclExpression):

    pass
class ocl_exp_ETypeExp(EOclExpression):

    pass
class ocl_exp_EVariableExp(EOclExpression):

    pass
class ocl_dm_EAttribute:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class ocl_dm_EDataModel:

    pass
class EAttribute:

    pass
class EAssociationEnd:

    pass
class EClassifier:

    pass
class ocl_type_EMessageType(EClassifier):

    def __init__(self, referredOperation: str, ocl_type_EMessageType: "ESignal" = None, EClassifier: "ocl_exp_ETypeExp", EClassifier66: "ocl_type_ECollectionType"):
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

class ocl_type_EAnyType(EClassifier):

    pass
class ocl_type_EInvalidType(EClassifier):

    pass
class ocl_type_EDataType(EClassifier):

    pass
class ocl_type_EVoidType(EClassifier):

    pass
class ocl_dm_EEntity(EClassifier):

    def __init__(self, name: str, ocl_dm_EEntity: set["EAssociationEnd"] = None, ocl_dm_EEntity2: set["EAttribute"] = None, EClassifier: "ocl_exp_ETypeExp", EClassifier66: "ocl_type_ECollectionType"):
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
                    
