from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SimpleType:

    pass
class HALL_Types_Number(SimpleType):

    pass
class HALL_Types_Boolean(SimpleType):

    pass
class HALL_Types_String(SimpleType):

    pass
class FSMActions_HALL_Data:

    pass
class Set:

    pass
class HALL_Types_Type(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class FSMActions_Let:

    pass
class ActionExpression:

    pass
class HALL_FSMActions_GetData(ActionExpression):

    pass
class HALL_FSMActions_Let(ActionExpression):

    def __init__(self, name: str, HALL_FSMActions_Let: "FSMActions_ActionExpression" = None, HALL_FSMActions_Let318: "FSMActions_ActionExpression" = None, HALL_FSMActions_Let321: "Type" = None):
        self.name = name
        self.HALL_FSMActions_Let = HALL_FSMActions_Let
        self.HALL_FSMActions_Let318 = HALL_FSMActions_Let318
        self.HALL_FSMActions_Let321 = HALL_FSMActions_Let321
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_FSMActions_Let(self):
        return self.__HALL_FSMActions_Let

    @HALL_FSMActions_Let.setter
    def HALL_FSMActions_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_Let__HALL_FSMActions_Let", None)
        self.__HALL_FSMActions_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression316"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression316", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression316"):
                opp_val = getattr(value, "FSMActions_ActionExpression316", None)
                setattr(value, "FSMActions_ActionExpression316", self)

    @property
    def HALL_FSMActions_Let318(self):
        return self.__HALL_FSMActions_Let318

    @HALL_FSMActions_Let318.setter
    def HALL_FSMActions_Let318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_Let__HALL_FSMActions_Let318", None)
        self.__HALL_FSMActions_Let318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression319"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression319", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression319"):
                opp_val = getattr(value, "FSMActions_ActionExpression319", None)
                setattr(value, "FSMActions_ActionExpression319", self)

    @property
    def HALL_FSMActions_Let321(self):
        return self.__HALL_FSMActions_Let321

    @HALL_FSMActions_Let321.setter
    def HALL_FSMActions_Let321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_Let__HALL_FSMActions_Let321", None)
        self.__HALL_FSMActions_Let321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type322"):
                opp_val = getattr(old_value, "Type322", None)
                if opp_val == self:
                    setattr(old_value, "Type322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type322"):
                opp_val = getattr(value, "Type322", None)
                setattr(value, "Type322", self)

class HALL_FSMActions_MessageInvocation(ActionExpression):

    def __init__(self, isTopDown: bool, HALL_FSMActions_MessageInvocation: "MessageDefinition" = None, HALL_FSMActions_MessageInvocation326: set["FSMActions_ActionExpression"] = None):
        self.isTopDown = isTopDown
        self.HALL_FSMActions_MessageInvocation = HALL_FSMActions_MessageInvocation
        self.HALL_FSMActions_MessageInvocation326 = HALL_FSMActions_MessageInvocation326 if HALL_FSMActions_MessageInvocation326 is not None else set()
        
    @property
    def isTopDown(self) -> bool:
        return self.__isTopDown

    @isTopDown.setter
    def isTopDown(self, isTopDown: bool):
        self.__isTopDown = isTopDown

    @property
    def HALL_FSMActions_MessageInvocation326(self):
        return self.__HALL_FSMActions_MessageInvocation326

    @HALL_FSMActions_MessageInvocation326.setter
    def HALL_FSMActions_MessageInvocation326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_MessageInvocation__HALL_FSMActions_MessageInvocation326", None)
        self.__HALL_FSMActions_MessageInvocation326 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSMActions_ActionExpression327"):
                    opp_val = getattr(item, "FSMActions_ActionExpression327", None)
                    
                    if opp_val == self:
                        setattr(item, "FSMActions_ActionExpression327", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSMActions_ActionExpression327"):
                    opp_val = getattr(item, "FSMActions_ActionExpression327", None)
                    
                    setattr(item, "FSMActions_ActionExpression327", self)
                    

    @property
    def HALL_FSMActions_MessageInvocation(self):
        return self.__HALL_FSMActions_MessageInvocation

    @HALL_FSMActions_MessageInvocation.setter
    def HALL_FSMActions_MessageInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_MessageInvocation__HALL_FSMActions_MessageInvocation", None)
        self.__HALL_FSMActions_MessageInvocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageDefinition324"):
                opp_val = getattr(old_value, "MessageDefinition324", None)
                if opp_val == self:
                    setattr(old_value, "MessageDefinition324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageDefinition324"):
                opp_val = getattr(value, "MessageDefinition324", None)
                setattr(value, "MessageDefinition324", self)

class HALL_FSMActions_UnaryOperator(ActionExpression):

    def __init__(self, operatorname: str, HALL_FSMActions_UnaryOperator: "FSMActions_ActionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMActions_UnaryOperator = HALL_FSMActions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_FSMActions_UnaryOperator(self):
        return self.__HALL_FSMActions_UnaryOperator

    @HALL_FSMActions_UnaryOperator.setter
    def HALL_FSMActions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_UnaryOperator__HALL_FSMActions_UnaryOperator", None)
        self.__HALL_FSMActions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression342"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression342", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression342"):
                opp_val = getattr(value, "FSMActions_ActionExpression342", None)
                setattr(value, "FSMActions_ActionExpression342", self)

class HALL_FSMActions_BinaryOperator(ActionExpression):

    def __init__(self, operatorname: str, HALL_FSMActions_BinaryOperator: "FSMActions_ActionExpression" = None, HALL_FSMActions_BinaryOperator339: "FSMActions_ActionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMActions_BinaryOperator = HALL_FSMActions_BinaryOperator
        self.HALL_FSMActions_BinaryOperator339 = HALL_FSMActions_BinaryOperator339
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_FSMActions_BinaryOperator339(self):
        return self.__HALL_FSMActions_BinaryOperator339

    @HALL_FSMActions_BinaryOperator339.setter
    def HALL_FSMActions_BinaryOperator339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_BinaryOperator__HALL_FSMActions_BinaryOperator339", None)
        self.__HALL_FSMActions_BinaryOperator339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression340"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression340", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression340"):
                opp_val = getattr(value, "FSMActions_ActionExpression340", None)
                setattr(value, "FSMActions_ActionExpression340", self)

    @property
    def HALL_FSMActions_BinaryOperator(self):
        return self.__HALL_FSMActions_BinaryOperator

    @HALL_FSMActions_BinaryOperator.setter
    def HALL_FSMActions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_BinaryOperator__HALL_FSMActions_BinaryOperator", None)
        self.__HALL_FSMActions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression337"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression337", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression337"):
                opp_val = getattr(value, "FSMActions_ActionExpression337", None)
                setattr(value, "FSMActions_ActionExpression337", self)

class HALL_FSMActions_DomainPropertyGet(ActionExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_FSMActions_VarRef(ActionExpression):

    pass
class HALL_FSMActions_DomainPropertySet(ActionExpression):

    def __init__(self, name: str, HALL_FSMActions_DomainPropertySet: "FSMActions_ActionExpression" = None):
        self.name = name
        self.HALL_FSMActions_DomainPropertySet = HALL_FSMActions_DomainPropertySet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_FSMActions_DomainPropertySet(self):
        return self.__HALL_FSMActions_DomainPropertySet

    @HALL_FSMActions_DomainPropertySet.setter
    def HALL_FSMActions_DomainPropertySet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMActions_DomainPropertySet__HALL_FSMActions_DomainPropertySet", None)
        self.__HALL_FSMActions_DomainPropertySet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_ActionExpression334"):
                opp_val = getattr(old_value, "FSMActions_ActionExpression334", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_ActionExpression334", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_ActionExpression334"):
                opp_val = getattr(value, "FSMActions_ActionExpression334", None)
                setattr(value, "FSMActions_ActionExpression334", self)

class HALL_FSMActions_Literal(ActionExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_FSMActions_ActionExpression:

    pass
class FSMActions_ActionExpression:

    pass
class HALL_FSMActions_Action:

    pass
class FSMConditions_Let:

    pass
class FSMConditions_HALL_Data:

    pass
class FSMConditions_HALL_Component:

    pass
class PreConditionExpression:

    pass
class HALL_FSMConditions_Let(PreConditionExpression):

    def __init__(self, name: str, HALL_FSMConditions_Let: "FSMConditions_PreConditionExpression" = None, HALL_FSMConditions_Let308: "FSMConditions_PreConditionExpression" = None, HALL_FSMConditions_Let311: "Type" = None):
        self.name = name
        self.HALL_FSMConditions_Let = HALL_FSMConditions_Let
        self.HALL_FSMConditions_Let308 = HALL_FSMConditions_Let308
        self.HALL_FSMConditions_Let311 = HALL_FSMConditions_Let311
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_FSMConditions_Let308(self):
        return self.__HALL_FSMConditions_Let308

    @HALL_FSMConditions_Let308.setter
    def HALL_FSMConditions_Let308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_Let__HALL_FSMConditions_Let308", None)
        self.__HALL_FSMConditions_Let308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpression309"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpression309", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpression309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpression309"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpression309", None)
                setattr(value, "FSMConditions_PreConditionExpression309", self)

    @property
    def HALL_FSMConditions_Let311(self):
        return self.__HALL_FSMConditions_Let311

    @HALL_FSMConditions_Let311.setter
    def HALL_FSMConditions_Let311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_Let__HALL_FSMConditions_Let311", None)
        self.__HALL_FSMConditions_Let311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type312"):
                opp_val = getattr(old_value, "Type312", None)
                if opp_val == self:
                    setattr(old_value, "Type312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type312"):
                opp_val = getattr(value, "Type312", None)
                setattr(value, "Type312", self)

    @property
    def HALL_FSMConditions_Let(self):
        return self.__HALL_FSMConditions_Let

    @HALL_FSMConditions_Let.setter
    def HALL_FSMConditions_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_Let__HALL_FSMConditions_Let", None)
        self.__HALL_FSMConditions_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpression306"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpression306", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpression306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpression306"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpression306", None)
                setattr(value, "FSMConditions_PreConditionExpression306", self)

class HALL_FSMConditions_BinaryOperator(PreConditionExpression):

    def __init__(self, operatorname: str, HALL_FSMConditions_BinaryOperator: "FSMConditions_PreConditionExpression" = None, HALL_FSMConditions_BinaryOperator299: "FSMConditions_PreConditionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMConditions_BinaryOperator = HALL_FSMConditions_BinaryOperator
        self.HALL_FSMConditions_BinaryOperator299 = HALL_FSMConditions_BinaryOperator299
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_FSMConditions_BinaryOperator(self):
        return self.__HALL_FSMConditions_BinaryOperator

    @HALL_FSMConditions_BinaryOperator.setter
    def HALL_FSMConditions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_BinaryOperator__HALL_FSMConditions_BinaryOperator", None)
        self.__HALL_FSMConditions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpression297"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpression297", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpression297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpression297"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpression297", None)
                setattr(value, "FSMConditions_PreConditionExpression297", self)

    @property
    def HALL_FSMConditions_BinaryOperator299(self):
        return self.__HALL_FSMConditions_BinaryOperator299

    @HALL_FSMConditions_BinaryOperator299.setter
    def HALL_FSMConditions_BinaryOperator299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_BinaryOperator__HALL_FSMConditions_BinaryOperator299", None)
        self.__HALL_FSMConditions_BinaryOperator299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpression300"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpression300", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpression300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpression300"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpression300", None)
                setattr(value, "FSMConditions_PreConditionExpression300", self)

class HALL_FSMConditions_DomainPropertyGet(PreConditionExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_FSMConditions_GetState(PreConditionExpression):

    pass
class HALL_FSMConditions_GetData(PreConditionExpression):

    pass
class HALL_FSMConditions_VarRef(PreConditionExpression):

    pass
class HALL_FSMConditions_UnaryOperator(PreConditionExpression):

    def __init__(self, operatorname: str, HALL_FSMConditions_UnaryOperator: "FSMConditions_PreConditionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMConditions_UnaryOperator = HALL_FSMConditions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_FSMConditions_UnaryOperator(self):
        return self.__HALL_FSMConditions_UnaryOperator

    @HALL_FSMConditions_UnaryOperator.setter
    def HALL_FSMConditions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMConditions_UnaryOperator__HALL_FSMConditions_UnaryOperator", None)
        self.__HALL_FSMConditions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreConditionExpression302"):
                opp_val = getattr(old_value, "FSMConditions_PreConditionExpression302", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreConditionExpression302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreConditionExpression302"):
                opp_val = getattr(value, "FSMConditions_PreConditionExpression302", None)
                setattr(value, "FSMConditions_PreConditionExpression302", self)

class HALL_FSMConditions_Literal(PreConditionExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_FSMConditions_PreConditionExpression(ABC):

    pass
class FSMConditions_PreConditionExpression:

    pass
class HALL_FSMConditions_PreCondition:

    pass
class FSMInstructions_Let:

    pass
class PosConditionExpression:

    pass
class HALL_FSMInstructions_DomainPropertyGet(PosConditionExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_FSMInstructions_Let(PosConditionExpression):

    def __init__(self, name: str, HALL_FSMInstructions_Let: "FSMInstructions_PosConditionExpression" = None, HALL_FSMInstructions_Let289: "FSMInstructions_PosConditionExpression" = None, HALL_FSMInstructions_Let292: "Type" = None):
        self.name = name
        self.HALL_FSMInstructions_Let = HALL_FSMInstructions_Let
        self.HALL_FSMInstructions_Let289 = HALL_FSMInstructions_Let289
        self.HALL_FSMInstructions_Let292 = HALL_FSMInstructions_Let292
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_FSMInstructions_Let(self):
        return self.__HALL_FSMInstructions_Let

    @HALL_FSMInstructions_Let.setter
    def HALL_FSMInstructions_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_Let__HALL_FSMInstructions_Let", None)
        self.__HALL_FSMInstructions_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression287"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression287", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression287"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression287", None)
                setattr(value, "FSMInstructions_PosConditionExpression287", self)

    @property
    def HALL_FSMInstructions_Let292(self):
        return self.__HALL_FSMInstructions_Let292

    @HALL_FSMInstructions_Let292.setter
    def HALL_FSMInstructions_Let292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_Let__HALL_FSMInstructions_Let292", None)
        self.__HALL_FSMInstructions_Let292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type293"):
                opp_val = getattr(old_value, "Type293", None)
                if opp_val == self:
                    setattr(old_value, "Type293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type293"):
                opp_val = getattr(value, "Type293", None)
                setattr(value, "Type293", self)

    @property
    def HALL_FSMInstructions_Let289(self):
        return self.__HALL_FSMInstructions_Let289

    @HALL_FSMInstructions_Let289.setter
    def HALL_FSMInstructions_Let289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_Let__HALL_FSMInstructions_Let289", None)
        self.__HALL_FSMInstructions_Let289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression290"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression290", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression290"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression290", None)
                setattr(value, "FSMInstructions_PosConditionExpression290", self)

class HALL_FSMInstructions_BinaryOperator(PosConditionExpression):

    def __init__(self, operatorname: str, HALL_FSMInstructions_BinaryOperator: "FSMInstructions_PosConditionExpression" = None, HALL_FSMInstructions_BinaryOperator270: "FSMInstructions_PosConditionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMInstructions_BinaryOperator = HALL_FSMInstructions_BinaryOperator
        self.HALL_FSMInstructions_BinaryOperator270 = HALL_FSMInstructions_BinaryOperator270
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_FSMInstructions_BinaryOperator270(self):
        return self.__HALL_FSMInstructions_BinaryOperator270

    @HALL_FSMInstructions_BinaryOperator270.setter
    def HALL_FSMInstructions_BinaryOperator270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_BinaryOperator__HALL_FSMInstructions_BinaryOperator270", None)
        self.__HALL_FSMInstructions_BinaryOperator270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression271"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression271", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression271"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression271", None)
                setattr(value, "FSMInstructions_PosConditionExpression271", self)

    @property
    def HALL_FSMInstructions_BinaryOperator(self):
        return self.__HALL_FSMInstructions_BinaryOperator

    @HALL_FSMInstructions_BinaryOperator.setter
    def HALL_FSMInstructions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_BinaryOperator__HALL_FSMInstructions_BinaryOperator", None)
        self.__HALL_FSMInstructions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression268"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression268", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression268"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression268", None)
                setattr(value, "FSMInstructions_PosConditionExpression268", self)

class HALL_FSMInstructions_VarRef(PosConditionExpression):

    pass
class HALL_FSMInstructions_Literal(PosConditionExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_FSMInstructions_PosConditionExpression(ABC):

    pass
class FSMInstructions_PosConditionExpression:

    pass
class HALL_FSMInstructions_PosCondition:

    pass
class FSMInstructions_HALL_Data:

    pass
class HALL_FSMInstructions_SetData(PosConditionExpression):

    def __init__(self, field: str, HALL_FSMInstructions_SetData: "FSMInstructions_PosConditionExpression" = None, HALL_FSMInstructions_SetData285: "FSMInstructions_HALL_Data" = None):
        self.field = field
        self.HALL_FSMInstructions_SetData = HALL_FSMInstructions_SetData
        self.HALL_FSMInstructions_SetData285 = HALL_FSMInstructions_SetData285
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def HALL_FSMInstructions_SetData285(self):
        return self.__HALL_FSMInstructions_SetData285

    @HALL_FSMInstructions_SetData285.setter
    def HALL_FSMInstructions_SetData285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_SetData__HALL_FSMInstructions_SetData285", None)
        self.__HALL_FSMInstructions_SetData285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_HALL_Data"):
                opp_val = getattr(old_value, "FSMInstructions_HALL_Data", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_HALL_Data", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_HALL_Data"):
                opp_val = getattr(value, "FSMInstructions_HALL_Data", None)
                setattr(value, "FSMInstructions_HALL_Data", self)

    @property
    def HALL_FSMInstructions_SetData(self):
        return self.__HALL_FSMInstructions_SetData

    @HALL_FSMInstructions_SetData.setter
    def HALL_FSMInstructions_SetData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_SetData__HALL_FSMInstructions_SetData", None)
        self.__HALL_FSMInstructions_SetData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression283"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression283", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression283"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression283", None)
                setattr(value, "FSMInstructions_PosConditionExpression283", self)

class HALL_FSMInstructions_SetState(PosConditionExpression):

    pass
class HALL_FSMInstructions_GetState(PosConditionExpression):

    pass
class FSMInstructions_HALL_Component:

    pass
class HALL_FSMInstructions_GetData(PosConditionExpression):

    def __init__(self, field: str, HALL_FSMInstructions_GetData: "FSMInstructions_HALL_Component" = None):
        self.field = field
        self.HALL_FSMInstructions_GetData = HALL_FSMInstructions_GetData
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def HALL_FSMInstructions_GetData(self):
        return self.__HALL_FSMInstructions_GetData

    @HALL_FSMInstructions_GetData.setter
    def HALL_FSMInstructions_GetData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_GetData__HALL_FSMInstructions_GetData", None)
        self.__HALL_FSMInstructions_GetData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_HALL_Component"):
                opp_val = getattr(old_value, "FSMInstructions_HALL_Component", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_HALL_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_HALL_Component"):
                opp_val = getattr(value, "FSMInstructions_HALL_Component", None)
                setattr(value, "FSMInstructions_HALL_Component", self)

class HALL_FSMInstructions_UnaryOperator(PosConditionExpression):

    def __init__(self, operatorname: str, HALL_FSMInstructions_UnaryOperator: "FSMInstructions_PosConditionExpression" = None):
        self.operatorname = operatorname
        self.HALL_FSMInstructions_UnaryOperator = HALL_FSMInstructions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_FSMInstructions_UnaryOperator(self):
        return self.__HALL_FSMInstructions_UnaryOperator

    @HALL_FSMInstructions_UnaryOperator.setter
    def HALL_FSMInstructions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSMInstructions_UnaryOperator__HALL_FSMInstructions_UnaryOperator", None)
        self.__HALL_FSMInstructions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosConditionExpression273"):
                opp_val = getattr(old_value, "FSMInstructions_PosConditionExpression273", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosConditionExpression273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosConditionExpression273"):
                opp_val = getattr(value, "FSMInstructions_PosConditionExpression273", None)
                setattr(value, "FSMInstructions_PosConditionExpression273", self)

class RegularState:

    pass
class InitialState:

    pass
class FSM_HALL_Component:

    pass
class HALL_FSM_FSM:

    pass
class TriggerExpression:

    pass
class HALL_Trigger_DomainEventFired(TriggerExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_Trigger_MessageNotification(TriggerExpression):

    pass
class HALL_Trigger_TriggerExpression(ABC):

    pass
class Trigger_TriggerExpression:

    pass
class HALL_Trigger_Trigger:

    pass
class Transition:

    pass
class HALL_FSM_State(ABC):

    def __init__(self, isActive: bool, name: str, Transition: set["Transition"] = None, HALL_FSM_State: "FSM" = None):
        self.isActive = isActive
        self.name = name
        self.Transition = Transition if Transition is not None else set()
        self.HALL_FSM_State = HALL_FSM_State
        
    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_State__Transition", None)
        self.__Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSM260"):
                    opp_val = getattr(item, "FSM260", None)
                    
                    if opp_val == self:
                        setattr(item, "FSM260", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSM260"):
                    opp_val = getattr(item, "FSM260", None)
                    
                    setattr(item, "FSM260", self)
                    

    @property
    def HALL_FSM_State(self):
        return self.__HALL_FSM_State

    @HALL_FSM_State.setter
    def HALL_FSM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_State__HALL_FSM_State", None)
        self.__HALL_FSM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM262"):
                opp_val = getattr(old_value, "FSM262", None)
                if opp_val == self:
                    setattr(old_value, "FSM262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM262"):
                opp_val = getattr(value, "FSM262", None)
                setattr(value, "FSM262", self)

class Trigger_Trigger:

    pass
class FSMActions_Action:

    pass
class FSMInstructions_PosCondition:

    pass
class FSMConditions_PreCondition:

    pass
class HALL_FSM_Transition:

    def __init__(self, name: str, State247: "State" = None, HALL_FSM_Transition: "State" = None, HALL_FSM_Transition252: "FSMConditions_PreCondition" = None, HALL_FSM_Transition254: "FSMInstructions_PosCondition" = None, HALL_FSM_Transition256: "FSMActions_Action" = None, HALL_FSM_Transition258: "Trigger_Trigger" = None):
        self.name = name
        self.State247 = State247
        self.HALL_FSM_Transition = HALL_FSM_Transition
        self.HALL_FSM_Transition252 = HALL_FSM_Transition252
        self.HALL_FSM_Transition254 = HALL_FSM_Transition254
        self.HALL_FSM_Transition256 = HALL_FSM_Transition256
        self.HALL_FSM_Transition258 = HALL_FSM_Transition258
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_FSM_Transition252(self):
        return self.__HALL_FSM_Transition252

    @HALL_FSM_Transition252.setter
    def HALL_FSM_Transition252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__HALL_FSM_Transition252", None)
        self.__HALL_FSM_Transition252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMConditions_PreCondition"):
                opp_val = getattr(old_value, "FSMConditions_PreCondition", None)
                if opp_val == self:
                    setattr(old_value, "FSMConditions_PreCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMConditions_PreCondition"):
                opp_val = getattr(value, "FSMConditions_PreCondition", None)
                setattr(value, "FSMConditions_PreCondition", self)

    @property
    def HALL_FSM_Transition(self):
        return self.__HALL_FSM_Transition

    @HALL_FSM_Transition.setter
    def HALL_FSM_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__HALL_FSM_Transition", None)
        self.__HALL_FSM_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State250"):
                opp_val = getattr(old_value, "State250", None)
                if opp_val == self:
                    setattr(old_value, "State250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State250"):
                opp_val = getattr(value, "State250", None)
                setattr(value, "State250", self)

    @property
    def HALL_FSM_Transition254(self):
        return self.__HALL_FSM_Transition254

    @HALL_FSM_Transition254.setter
    def HALL_FSM_Transition254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__HALL_FSM_Transition254", None)
        self.__HALL_FSM_Transition254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMInstructions_PosCondition"):
                opp_val = getattr(old_value, "FSMInstructions_PosCondition", None)
                if opp_val == self:
                    setattr(old_value, "FSMInstructions_PosCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMInstructions_PosCondition"):
                opp_val = getattr(value, "FSMInstructions_PosCondition", None)
                setattr(value, "FSMInstructions_PosCondition", self)

    @property
    def HALL_FSM_Transition256(self):
        return self.__HALL_FSM_Transition256

    @HALL_FSM_Transition256.setter
    def HALL_FSM_Transition256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__HALL_FSM_Transition256", None)
        self.__HALL_FSM_Transition256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSMActions_Action"):
                opp_val = getattr(old_value, "FSMActions_Action", None)
                if opp_val == self:
                    setattr(old_value, "FSMActions_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSMActions_Action"):
                opp_val = getattr(value, "FSMActions_Action", None)
                setattr(value, "FSMActions_Action", self)

    @property
    def HALL_FSM_Transition258(self):
        return self.__HALL_FSM_Transition258

    @HALL_FSM_Transition258.setter
    def HALL_FSM_Transition258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__HALL_FSM_Transition258", None)
        self.__HALL_FSM_Transition258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Trigger_Trigger"):
                opp_val = getattr(old_value, "Trigger_Trigger", None)
                if opp_val == self:
                    setattr(old_value, "Trigger_Trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Trigger_Trigger"):
                opp_val = getattr(value, "Trigger_Trigger", None)
                setattr(value, "Trigger_Trigger", self)

    @property
    def State247(self):
        return self.__State247

    @State247.setter
    def State247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_FSM_Transition__State247", None)
        self.__State247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM248"):
                opp_val = getattr(old_value, "FSM248", None)
                if opp_val == self:
                    setattr(old_value, "FSM248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM248"):
                opp_val = getattr(value, "FSM248", None)
                setattr(value, "FSM248", self)

class Actions_HALL_Component:

    pass
class Conditions_Let:

    pass
class Actions_Let:

    pass
class ActionMessageExpression:

    pass
class HALL_Actions_DomainPropertyGet(ActionMessageExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_Actions_BinaryOperator(ActionMessageExpression):

    def __init__(self, operatorname: str, HALL_Actions_BinaryOperator: "Actions_ActionMessageExpression" = None, HALL_Actions_BinaryOperator215: "Actions_ActionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Actions_BinaryOperator = HALL_Actions_BinaryOperator
        self.HALL_Actions_BinaryOperator215 = HALL_Actions_BinaryOperator215
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_Actions_BinaryOperator(self):
        return self.__HALL_Actions_BinaryOperator

    @HALL_Actions_BinaryOperator.setter
    def HALL_Actions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_BinaryOperator__HALL_Actions_BinaryOperator", None)
        self.__HALL_Actions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpression213"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpression213", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpression213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpression213"):
                opp_val = getattr(value, "Actions_ActionMessageExpression213", None)
                setattr(value, "Actions_ActionMessageExpression213", self)

    @property
    def HALL_Actions_BinaryOperator215(self):
        return self.__HALL_Actions_BinaryOperator215

    @HALL_Actions_BinaryOperator215.setter
    def HALL_Actions_BinaryOperator215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_BinaryOperator__HALL_Actions_BinaryOperator215", None)
        self.__HALL_Actions_BinaryOperator215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpression216"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpression216", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpression216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpression216"):
                opp_val = getattr(value, "Actions_ActionMessageExpression216", None)
                setattr(value, "Actions_ActionMessageExpression216", self)

class HALL_Actions_Literal(ActionMessageExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_FSMActions_Enable(ActionMessageExpression):

    pass
class HALL_Actions_GetData(ActionMessageExpression):

    pass
class HALL_Actions_Let(ActionMessageExpression):

    pass
class HALL_Actions_UnaryOperator(ActionMessageExpression):

    def __init__(self, operatorname: str, HALL_Actions_UnaryOperator: "Actions_ActionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Actions_UnaryOperator = HALL_Actions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_Actions_UnaryOperator(self):
        return self.__HALL_Actions_UnaryOperator

    @HALL_Actions_UnaryOperator.setter
    def HALL_Actions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_UnaryOperator__HALL_Actions_UnaryOperator", None)
        self.__HALL_Actions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpression231"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpression231", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpression231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpression231"):
                opp_val = getattr(value, "Actions_ActionMessageExpression231", None)
                setattr(value, "Actions_ActionMessageExpression231", self)

class HALL_Actions_GetMessageParameter(ActionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Actions_GetMessageData(ActionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Actions_Enable(ActionMessageExpression):

    pass
class HALL_Actions_MessageInvocation(ActionMessageExpression):

    def __init__(self, isTopDown: bool, HALL_Actions_MessageInvocation: "MessageDefinition" = None, HALL_Actions_MessageInvocation228: set["Actions_ActionMessageExpression"] = None):
        self.isTopDown = isTopDown
        self.HALL_Actions_MessageInvocation = HALL_Actions_MessageInvocation
        self.HALL_Actions_MessageInvocation228 = HALL_Actions_MessageInvocation228 if HALL_Actions_MessageInvocation228 is not None else set()
        
    @property
    def isTopDown(self) -> bool:
        return self.__isTopDown

    @isTopDown.setter
    def isTopDown(self, isTopDown: bool):
        self.__isTopDown = isTopDown

    @property
    def HALL_Actions_MessageInvocation228(self):
        return self.__HALL_Actions_MessageInvocation228

    @HALL_Actions_MessageInvocation228.setter
    def HALL_Actions_MessageInvocation228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_MessageInvocation__HALL_Actions_MessageInvocation228", None)
        self.__HALL_Actions_MessageInvocation228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actions_ActionMessageExpression229"):
                    opp_val = getattr(item, "Actions_ActionMessageExpression229", None)
                    
                    if opp_val == self:
                        setattr(item, "Actions_ActionMessageExpression229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actions_ActionMessageExpression229"):
                    opp_val = getattr(item, "Actions_ActionMessageExpression229", None)
                    
                    setattr(item, "Actions_ActionMessageExpression229", self)
                    

    @property
    def HALL_Actions_MessageInvocation(self):
        return self.__HALL_Actions_MessageInvocation

    @HALL_Actions_MessageInvocation.setter
    def HALL_Actions_MessageInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_MessageInvocation__HALL_Actions_MessageInvocation", None)
        self.__HALL_Actions_MessageInvocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageDefinition226"):
                opp_val = getattr(old_value, "MessageDefinition226", None)
                if opp_val == self:
                    setattr(old_value, "MessageDefinition226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageDefinition226"):
                opp_val = getattr(value, "MessageDefinition226", None)
                setattr(value, "MessageDefinition226", self)

class HALL_Actions_DomainPropertySet(ActionMessageExpression):

    def __init__(self, name: str, HALL_Actions_DomainPropertySet: "Actions_ActionMessageExpression" = None):
        self.name = name
        self.HALL_Actions_DomainPropertySet = HALL_Actions_DomainPropertySet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_Actions_DomainPropertySet(self):
        return self.__HALL_Actions_DomainPropertySet

    @HALL_Actions_DomainPropertySet.setter
    def HALL_Actions_DomainPropertySet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Actions_DomainPropertySet__HALL_Actions_DomainPropertySet", None)
        self.__HALL_Actions_DomainPropertySet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessageExpression234"):
                opp_val = getattr(old_value, "Actions_ActionMessageExpression234", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessageExpression234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessageExpression234"):
                opp_val = getattr(value, "Actions_ActionMessageExpression234", None)
                setattr(value, "Actions_ActionMessageExpression234", self)

class HALL_Actions_VarRef(ActionMessageExpression):

    pass
class HALL_Actions_ActionMessageExpression(ABC):

    pass
class Actions_ActionMessageExpression:

    pass
class HALL_Actions_ActionMessage:

    pass
class Conditions_PreConditionMessageExpression:

    pass
class HALL_Conditions_PreConditionMessage:

    pass
class Instructions_Let:

    pass
class Conditions_HALL_Data:

    pass
class Conditions_HALL_Component:

    pass
class PreConditionMessageExpression:

    pass
class HALL_Conditions_GetState(PreConditionMessageExpression):

    pass
class HALL_Conditions_DomainPropertyGet(PreConditionMessageExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_Conditions_GetData(PreConditionMessageExpression):

    pass
class HALL_Conditions_UnaryOperator(PreConditionMessageExpression):

    def __init__(self, operatorname: str, HALL_Conditions_UnaryOperator: "Conditions_PreConditionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Conditions_UnaryOperator = HALL_Conditions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_Conditions_UnaryOperator(self):
        return self.__HALL_Conditions_UnaryOperator

    @HALL_Conditions_UnaryOperator.setter
    def HALL_Conditions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_UnaryOperator__HALL_Conditions_UnaryOperator", None)
        self.__HALL_Conditions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpression203"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpression203", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpression203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpression203"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpression203", None)
                setattr(value, "Conditions_PreConditionMessageExpression203", self)

class HALL_Conditions_BinaryOperator(PreConditionMessageExpression):

    def __init__(self, operatorname: str, HALL_Conditions_BinaryOperator: "Conditions_PreConditionMessageExpression" = None, HALL_Conditions_BinaryOperator207: "Conditions_PreConditionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Conditions_BinaryOperator = HALL_Conditions_BinaryOperator
        self.HALL_Conditions_BinaryOperator207 = HALL_Conditions_BinaryOperator207
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_Conditions_BinaryOperator207(self):
        return self.__HALL_Conditions_BinaryOperator207

    @HALL_Conditions_BinaryOperator207.setter
    def HALL_Conditions_BinaryOperator207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_BinaryOperator__HALL_Conditions_BinaryOperator207", None)
        self.__HALL_Conditions_BinaryOperator207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpression208"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpression208", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpression208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpression208"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpression208", None)
                setattr(value, "Conditions_PreConditionMessageExpression208", self)

    @property
    def HALL_Conditions_BinaryOperator(self):
        return self.__HALL_Conditions_BinaryOperator

    @HALL_Conditions_BinaryOperator.setter
    def HALL_Conditions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_BinaryOperator__HALL_Conditions_BinaryOperator", None)
        self.__HALL_Conditions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpression205"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpression205", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpression205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpression205"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpression205", None)
                setattr(value, "Conditions_PreConditionMessageExpression205", self)

class HALL_Conditions_VarRef(PreConditionMessageExpression):

    pass
class HALL_Conditions_Let(PreConditionMessageExpression):

    def __init__(self, name: str, HALL_Conditions_Let: "Type" = None, HALL_Conditions_Let197: "Conditions_PreConditionMessageExpression" = None, HALL_Conditions_Let200: "Conditions_PreConditionMessageExpression" = None):
        self.name = name
        self.HALL_Conditions_Let = HALL_Conditions_Let
        self.HALL_Conditions_Let197 = HALL_Conditions_Let197
        self.HALL_Conditions_Let200 = HALL_Conditions_Let200
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_Conditions_Let200(self):
        return self.__HALL_Conditions_Let200

    @HALL_Conditions_Let200.setter
    def HALL_Conditions_Let200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_Let__HALL_Conditions_Let200", None)
        self.__HALL_Conditions_Let200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpression201"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpression201", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpression201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpression201"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpression201", None)
                setattr(value, "Conditions_PreConditionMessageExpression201", self)

    @property
    def HALL_Conditions_Let(self):
        return self.__HALL_Conditions_Let

    @HALL_Conditions_Let.setter
    def HALL_Conditions_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_Let__HALL_Conditions_Let", None)
        self.__HALL_Conditions_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type195"):
                opp_val = getattr(old_value, "Type195", None)
                if opp_val == self:
                    setattr(old_value, "Type195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type195"):
                opp_val = getattr(value, "Type195", None)
                setattr(value, "Type195", self)

    @property
    def HALL_Conditions_Let197(self):
        return self.__HALL_Conditions_Let197

    @HALL_Conditions_Let197.setter
    def HALL_Conditions_Let197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Conditions_Let__HALL_Conditions_Let197", None)
        self.__HALL_Conditions_Let197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessageExpression198"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessageExpression198", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessageExpression198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessageExpression198"):
                opp_val = getattr(value, "Conditions_PreConditionMessageExpression198", None)
                setattr(value, "Conditions_PreConditionMessageExpression198", self)

class HALL_Conditions_GetMessageData(PreConditionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Conditions_GetMessageParameter(PreConditionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Conditions_Literal(PreConditionMessageExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_Conditions_PreConditionMessageExpression(ABC):

    pass
class State:

    pass
class HALL_FSM_RegularState(State):

    pass
class HALL_FSM_InitialState(State):

    pass
class Instructions_HALL_Component:

    pass
class Instructions_HALL_Data:

    pass
class Messages_HALL_Parameter:

    pass
class Messages_HALL_Model:

    pass
class HALL_Messages_MessageDefinition:

    def __init__(self, name: str, dataInvMessageDefinition: set["Messages_HALL_Data"] = None, messageDefinition: "Messages_HALL_Model" = None, parameterInv: set["Messages_HALL_Parameter"] = None):
        self.name = name
        self.dataInvMessageDefinition = dataInvMessageDefinition if dataInvMessageDefinition is not None else set()
        self.messageDefinition = messageDefinition
        self.parameterInv = parameterInv if parameterInv is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def messageDefinition(self):
        return self.__messageDefinition

    @messageDefinition.setter
    def messageDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageDefinition__messageDefinition", None)
        self.__messageDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model143"):
                opp_val = getattr(old_value, "Model143", None)
                if opp_val == self:
                    setattr(old_value, "Model143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model143"):
                opp_val = getattr(value, "Model143", None)
                setattr(value, "Model143", self)

    @property
    def dataInvMessageDefinition(self):
        return self.__dataInvMessageDefinition

    @dataInvMessageDefinition.setter
    def dataInvMessageDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageDefinition__dataInvMessageDefinition", None)
        self.__dataInvMessageDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data146"):
                    opp_val = getattr(item, "Data146", None)
                    
                    if opp_val == self:
                        setattr(item, "Data146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data146"):
                    opp_val = getattr(item, "Data146", None)
                    
                    setattr(item, "Data146", self)
                    

    @property
    def parameterInv(self):
        return self.__parameterInv

    @parameterInv.setter
    def parameterInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageDefinition__parameterInv", None)
        self.__parameterInv = value if value is not None else set()
        
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
                    

class Actions_ActionMessage:

    pass
class PosConditionMessageExpression:

    pass
class HALL_Instructions_GetData(PosConditionMessageExpression):

    pass
class HALL_Instructions_SetState(PosConditionMessageExpression):

    pass
class HALL_Instructions_VarRef(PosConditionMessageExpression):

    pass
class HALL_Instructions_DomainPropertyGet(PosConditionMessageExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HALL_Instructions_SetTopDown(PosConditionMessageExpression):

    pass
class HALL_Instructions_GetMessageParameter(PosConditionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Instructions_GetState(PosConditionMessageExpression):

    pass
class HALL_Instructions_SetMessageParameter(PosConditionMessageExpression):

    def __init__(self, field: str, HALL_Instructions_SetMessageParameter: "Instructions_PosConditionMessageExpression" = None):
        self.field = field
        self.HALL_Instructions_SetMessageParameter = HALL_Instructions_SetMessageParameter
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def HALL_Instructions_SetMessageParameter(self):
        return self.__HALL_Instructions_SetMessageParameter

    @HALL_Instructions_SetMessageParameter.setter
    def HALL_Instructions_SetMessageParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_SetMessageParameter__HALL_Instructions_SetMessageParameter", None)
        self.__HALL_Instructions_SetMessageParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression179"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression179", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression179"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression179", None)
                setattr(value, "Instructions_PosConditionMessageExpression179", self)

class HALL_Instructions_UnaryOperator(PosConditionMessageExpression):

    def __init__(self, operatorname: str, HALL_Instructions_UnaryOperator: "Instructions_PosConditionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Instructions_UnaryOperator = HALL_Instructions_UnaryOperator
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_Instructions_UnaryOperator(self):
        return self.__HALL_Instructions_UnaryOperator

    @HALL_Instructions_UnaryOperator.setter
    def HALL_Instructions_UnaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_UnaryOperator__HALL_Instructions_UnaryOperator", None)
        self.__HALL_Instructions_UnaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression167"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression167", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression167"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression167", None)
                setattr(value, "Instructions_PosConditionMessageExpression167", self)

class HALL_Instructions_GetMessageData(PosConditionMessageExpression):

    def __init__(self, field: str):
        self.field = field
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

class HALL_Instructions_Let(PosConditionMessageExpression):

    def __init__(self, name: str, HALL_Instructions_Let: "Instructions_PosConditionMessageExpression" = None, HALL_Instructions_Let183: "Instructions_PosConditionMessageExpression" = None, HALL_Instructions_Let186: "Type" = None):
        self.name = name
        self.HALL_Instructions_Let = HALL_Instructions_Let
        self.HALL_Instructions_Let183 = HALL_Instructions_Let183
        self.HALL_Instructions_Let186 = HALL_Instructions_Let186
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_Instructions_Let(self):
        return self.__HALL_Instructions_Let

    @HALL_Instructions_Let.setter
    def HALL_Instructions_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_Let__HALL_Instructions_Let", None)
        self.__HALL_Instructions_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression181"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression181", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression181"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression181", None)
                setattr(value, "Instructions_PosConditionMessageExpression181", self)

    @property
    def HALL_Instructions_Let186(self):
        return self.__HALL_Instructions_Let186

    @HALL_Instructions_Let186.setter
    def HALL_Instructions_Let186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_Let__HALL_Instructions_Let186", None)
        self.__HALL_Instructions_Let186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type187"):
                opp_val = getattr(old_value, "Type187", None)
                if opp_val == self:
                    setattr(old_value, "Type187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type187"):
                opp_val = getattr(value, "Type187", None)
                setattr(value, "Type187", self)

    @property
    def HALL_Instructions_Let183(self):
        return self.__HALL_Instructions_Let183

    @HALL_Instructions_Let183.setter
    def HALL_Instructions_Let183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_Let__HALL_Instructions_Let183", None)
        self.__HALL_Instructions_Let183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression184"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression184", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression184"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression184", None)
                setattr(value, "Instructions_PosConditionMessageExpression184", self)

class HALL_Instructions_BinaryOperator(PosConditionMessageExpression):

    def __init__(self, operatorname: str, HALL_Instructions_BinaryOperator164: "Instructions_PosConditionMessageExpression" = None, HALL_Instructions_BinaryOperator: "Instructions_PosConditionMessageExpression" = None):
        self.operatorname = operatorname
        self.HALL_Instructions_BinaryOperator164 = HALL_Instructions_BinaryOperator164
        self.HALL_Instructions_BinaryOperator = HALL_Instructions_BinaryOperator
        
    @property
    def operatorname(self) -> str:
        return self.__operatorname

    @operatorname.setter
    def operatorname(self, operatorname: str):
        self.__operatorname = operatorname

    @property
    def HALL_Instructions_BinaryOperator164(self):
        return self.__HALL_Instructions_BinaryOperator164

    @HALL_Instructions_BinaryOperator164.setter
    def HALL_Instructions_BinaryOperator164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_BinaryOperator__HALL_Instructions_BinaryOperator164", None)
        self.__HALL_Instructions_BinaryOperator164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression165"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression165", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression165"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression165", None)
                setattr(value, "Instructions_PosConditionMessageExpression165", self)

    @property
    def HALL_Instructions_BinaryOperator(self):
        return self.__HALL_Instructions_BinaryOperator

    @HALL_Instructions_BinaryOperator.setter
    def HALL_Instructions_BinaryOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_BinaryOperator__HALL_Instructions_BinaryOperator", None)
        self.__HALL_Instructions_BinaryOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression162"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression162", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression162"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression162", None)
                setattr(value, "Instructions_PosConditionMessageExpression162", self)

class HALL_Instructions_SetData(PosConditionMessageExpression):

    pass
class HALL_Instructions_SetMessageData(PosConditionMessageExpression):

    def __init__(self, field: str, HALL_Instructions_SetMessageData: "Instructions_PosConditionMessageExpression" = None):
        self.field = field
        self.HALL_Instructions_SetMessageData = HALL_Instructions_SetMessageData
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def HALL_Instructions_SetMessageData(self):
        return self.__HALL_Instructions_SetMessageData

    @HALL_Instructions_SetMessageData.setter
    def HALL_Instructions_SetMessageData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Instructions_SetMessageData__HALL_Instructions_SetMessageData", None)
        self.__HALL_Instructions_SetMessageData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessageExpression177"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessageExpression177", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessageExpression177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessageExpression177"):
                opp_val = getattr(value, "Instructions_PosConditionMessageExpression177", None)
                setattr(value, "Instructions_PosConditionMessageExpression177", self)

class HALL_Instructions_Literal(PosConditionMessageExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class HALL_Instructions_PosConditionMessageExpression(ABC):

    pass
class Instructions_PosConditionMessageExpression:

    pass
class HALL_Instructions_PosConditionMessage:

    pass
class MessageTransition:

    pass
class HALL_Messages_MessageState:

    def __init__(self, name: str, isEnd: bool, isContinue: bool, isActive: bool, MessageTransition: set["MessageTransition"] = None):
        self.name = name
        self.isEnd = isEnd
        self.isContinue = isContinue
        self.isActive = isActive
        self.MessageTransition = MessageTransition if MessageTransition is not None else set()
        
    @property
    def isContinue(self) -> bool:
        return self.__isContinue

    @isContinue.setter
    def isContinue(self, isContinue: bool):
        self.__isContinue = isContinue

    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isEnd(self) -> bool:
        return self.__isEnd

    @isEnd.setter
    def isEnd(self, isEnd: bool):
        self.__isEnd = isEnd

    @property
    def MessageTransition(self):
        return self.__MessageTransition

    @MessageTransition.setter
    def MessageTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageState__MessageTransition", None)
        self.__MessageTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Messages156"):
                    opp_val = getattr(item, "Messages156", None)
                    
                    if opp_val == self:
                        setattr(item, "Messages156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Messages156"):
                    opp_val = getattr(item, "Messages156", None)
                    
                    setattr(item, "Messages156", self)
                    

class Messages_HALL_Component:

    pass
class InitialMessageState:

    pass
class RegularMessageState:

    pass
class HALL_Messages_MessageHandler:

    pass
class Messages_HALL_Data:

    pass
class Point2D:

    pass
class Face:

    pass
class HALL_Geometry_GeometryData(ABC):

    pass
class Instructions_PosConditionMessage:

    pass
class Conditions_PreConditionMessage:

    pass
class MessageState:

    pass
class HALL_Messages_InitialMessageState(MessageState):

    pass
class HALL_Messages_RegularMessageState(MessageState):

    pass
class HALL_Messages_MessageTransition:

    def __init__(self, name: str, MessageState: "MessageState" = None, HALL_Messages_MessageTransition: "MessageState" = None, HALL_Messages_MessageTransition134: "Conditions_PreConditionMessage" = None, HALL_Messages_MessageTransition136: "Instructions_PosConditionMessage" = None, HALL_Messages_MessageTransition138: "Actions_ActionMessage" = None):
        self.name = name
        self.MessageState = MessageState
        self.HALL_Messages_MessageTransition = HALL_Messages_MessageTransition
        self.HALL_Messages_MessageTransition134 = HALL_Messages_MessageTransition134
        self.HALL_Messages_MessageTransition136 = HALL_Messages_MessageTransition136
        self.HALL_Messages_MessageTransition138 = HALL_Messages_MessageTransition138
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MessageState(self):
        return self.__MessageState

    @MessageState.setter
    def MessageState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__MessageState", None)
        self.__MessageState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages130"):
                opp_val = getattr(old_value, "Messages130", None)
                if opp_val == self:
                    setattr(old_value, "Messages130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages130"):
                opp_val = getattr(value, "Messages130", None)
                setattr(value, "Messages130", self)

    @property
    def HALL_Messages_MessageTransition134(self):
        return self.__HALL_Messages_MessageTransition134

    @HALL_Messages_MessageTransition134.setter
    def HALL_Messages_MessageTransition134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__HALL_Messages_MessageTransition134", None)
        self.__HALL_Messages_MessageTransition134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Conditions_PreConditionMessage"):
                opp_val = getattr(old_value, "Conditions_PreConditionMessage", None)
                if opp_val == self:
                    setattr(old_value, "Conditions_PreConditionMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Conditions_PreConditionMessage"):
                opp_val = getattr(value, "Conditions_PreConditionMessage", None)
                setattr(value, "Conditions_PreConditionMessage", self)

    @property
    def HALL_Messages_MessageTransition136(self):
        return self.__HALL_Messages_MessageTransition136

    @HALL_Messages_MessageTransition136.setter
    def HALL_Messages_MessageTransition136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__HALL_Messages_MessageTransition136", None)
        self.__HALL_Messages_MessageTransition136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instructions_PosConditionMessage"):
                opp_val = getattr(old_value, "Instructions_PosConditionMessage", None)
                if opp_val == self:
                    setattr(old_value, "Instructions_PosConditionMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instructions_PosConditionMessage"):
                opp_val = getattr(value, "Instructions_PosConditionMessage", None)
                setattr(value, "Instructions_PosConditionMessage", self)

    @property
    def HALL_Messages_MessageTransition(self):
        return self.__HALL_Messages_MessageTransition

    @HALL_Messages_MessageTransition.setter
    def HALL_Messages_MessageTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__HALL_Messages_MessageTransition", None)
        self.__HALL_Messages_MessageTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageState132"):
                opp_val = getattr(old_value, "MessageState132", None)
                if opp_val == self:
                    setattr(old_value, "MessageState132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageState132"):
                opp_val = getattr(value, "MessageState132", None)
                setattr(value, "MessageState132", self)

    @property
    def HALL_Messages_MessageTransition138(self):
        return self.__HALL_Messages_MessageTransition138

    @HALL_Messages_MessageTransition138.setter
    def HALL_Messages_MessageTransition138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Messages_MessageTransition__HALL_Messages_MessageTransition138", None)
        self.__HALL_Messages_MessageTransition138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actions_ActionMessage"):
                opp_val = getattr(old_value, "Actions_ActionMessage", None)
                if opp_val == self:
                    setattr(old_value, "Actions_ActionMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actions_ActionMessage"):
                opp_val = getattr(value, "Actions_ActionMessage", None)
                setattr(value, "Actions_ActionMessage", self)

class HALL_Geometry_Point:

    def __init__(self, xCoord: int, yCoord: int):
        self.xCoord = xCoord
        self.yCoord = yCoord
        
    @property
    def xCoord(self) -> int:
        return self.__xCoord

    @xCoord.setter
    def xCoord(self, xCoord: int):
        self.__xCoord = xCoord

    @property
    def yCoord(self) -> int:
        return self.__yCoord

    @yCoord.setter
    def yCoord(self, yCoord: int):
        self.__yCoord = yCoord

class GeometryData2D:

    pass
class Point:

    pass
class HALL_Geometry_Point2D(Point):

    pass
class HALL_Geometry_Point3D(Point):

    def __init__(self, zCoord: int, Face125: "Face" = None):
        self.zCoord = zCoord
        self.Face125 = Face125
        
    @property
    def zCoord(self) -> int:
        return self.__zCoord

    @zCoord.setter
    def zCoord(self, zCoord: int):
        self.__zCoord = zCoord

    @property
    def Face125(self):
        return self.__Face125

    @Face125.setter
    def Face125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_Point3D__Face125", None)
        self.__Face125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry126"):
                opp_val = getattr(old_value, "Geometry126", None)
                if opp_val == self:
                    setattr(old_value, "Geometry126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry126"):
                opp_val = getattr(value, "Geometry126", None)
                setattr(value, "Geometry126", self)

class GeometryData3D:

    pass
class Point3D:

    pass
class HALL_Geometry_Face:

    def __init__(self, labelText: str, Point3D: set["Point3D"] = None, GeometryData3D: "GeometryData3D" = None):
        self.labelText = labelText
        self.Point3D = Point3D if Point3D is not None else set()
        self.GeometryData3D = GeometryData3D
        
    @property
    def labelText(self) -> str:
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText

    @property
    def Point3D(self):
        return self.__Point3D

    @Point3D.setter
    def Point3D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_Face__Point3D", None)
        self.__Point3D = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Geometry121"):
                    opp_val = getattr(item, "Geometry121", None)
                    
                    if opp_val == self:
                        setattr(item, "Geometry121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Geometry121"):
                    opp_val = getattr(item, "Geometry121", None)
                    
                    setattr(item, "Geometry121", self)
                    

    @property
    def GeometryData3D(self):
        return self.__GeometryData3D

    @GeometryData3D.setter
    def GeometryData3D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_Face__GeometryData3D", None)
        self.__GeometryData3D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry123"):
                opp_val = getattr(old_value, "Geometry123", None)
                if opp_val == self:
                    setattr(old_value, "Geometry123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry123"):
                opp_val = getattr(value, "Geometry123", None)
                setattr(value, "Geometry123", self)

class Color:

    pass
class HALL_Geometry_RGBColor:

    def __init__(self, redValue: int, greenValue: int, blueValue: int, Color: "Color" = None, Color81: "Color" = None, Color84: "Color" = None):
        self.redValue = redValue
        self.greenValue = greenValue
        self.blueValue = blueValue
        self.Color = Color
        self.Color81 = Color81
        self.Color84 = Color84
        
    @property
    def redValue(self) -> int:
        return self.__redValue

    @redValue.setter
    def redValue(self, redValue: int):
        self.__redValue = redValue

    @property
    def blueValue(self) -> int:
        return self.__blueValue

    @blueValue.setter
    def blueValue(self, blueValue: int):
        self.__blueValue = blueValue

    @property
    def greenValue(self) -> int:
        return self.__greenValue

    @greenValue.setter
    def greenValue(self, greenValue: int):
        self.__greenValue = greenValue

    @property
    def Color84(self):
        return self.__Color84

    @Color84.setter
    def Color84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_RGBColor__Color84", None)
        self.__Color84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry85"):
                opp_val = getattr(old_value, "Geometry85", None)
                if opp_val == self:
                    setattr(old_value, "Geometry85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry85"):
                opp_val = getattr(value, "Geometry85", None)
                setattr(value, "Geometry85", self)

    @property
    def Color(self):
        return self.__Color

    @Color.setter
    def Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_RGBColor__Color", None)
        self.__Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry79"):
                opp_val = getattr(old_value, "Geometry79", None)
                if opp_val == self:
                    setattr(old_value, "Geometry79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry79"):
                opp_val = getattr(value, "Geometry79", None)
                setattr(value, "Geometry79", self)

    @property
    def Color81(self):
        return self.__Color81

    @Color81.setter
    def Color81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_RGBColor__Color81", None)
        self.__Color81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry82"):
                opp_val = getattr(old_value, "Geometry82", None)
                if opp_val == self:
                    setattr(old_value, "Geometry82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry82"):
                opp_val = getattr(value, "Geometry82", None)
                setattr(value, "Geometry82", self)

class ColorState:

    pass
class Geometry_HALL_VisualObject:

    pass
class NormalColors:

    pass
class DisabledColors:

    pass
class SelectedColors:

    pass
class HALL_Geometry_ColorData:

    pass
class HALL_Geometry_DisabledColors(ColorState):

    pass
class HALL_Geometry_SelectedColors(ColorState):

    pass
class HALL_Geometry_NormalColors(ColorState):

    pass
class HALL_Geometry_AlphaTransparency:

    def __init__(self, value: int, ColorState95: "ColorState" = None):
        self.value = value
        self.ColorState95 = ColorState95
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def ColorState95(self):
        return self.__ColorState95

    @ColorState95.setter
    def ColorState95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_AlphaTransparency__ColorState95", None)
        self.__ColorState95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry96"):
                opp_val = getattr(old_value, "Geometry96", None)
                if opp_val == self:
                    setattr(old_value, "Geometry96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry96"):
                opp_val = getattr(value, "Geometry96", None)
                setattr(value, "Geometry96", self)

class AlphaTransparency:

    pass
class HALL_Geometry_ColorState(ABC):

    pass
class HALL_Goal:

    def __init__(self, condition: str, goal: "HALL_TaskObject" = None, Goal: "HALL_TaskObject" = None):
        self.condition = condition
        self.goal = goal
        self.Goal = Goal
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def Goal(self):
        return self.__Goal

    @Goal.setter
    def Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Goal__Goal", None)
        self.__Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "goalInv"):
                opp_val = getattr(old_value, "goalInv", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "goalInv"):
                opp_val = getattr(value, "goalInv", None)
                if opp_val is None:
                    setattr(value, "goalInv", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def goal(self):
        return self.__goal

    @goal.setter
    def goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Goal__goal", None)
        self.__goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskObject53"):
                opp_val = getattr(old_value, "TaskObject53", None)
                if opp_val == self:
                    setattr(old_value, "TaskObject53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskObject53"):
                opp_val = getattr(value, "TaskObject53", None)
                setattr(value, "TaskObject53", self)

class RGBColor:

    pass
class HALL_Geometry_Color:

    pass
class Type:

    pass
class HALL_Types_SimpleType(Type):

    pass
class HALL_Types_Set(Type):

    pass
class MessageDefinition:

    pass
class HALL_Parameter:

    def __init__(self, name: str, HALL_Parameter: "Type" = None, MessageDefinition57: "MessageDefinition" = None):
        self.name = name
        self.HALL_Parameter = HALL_Parameter
        self.MessageDefinition57 = MessageDefinition57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def HALL_Parameter(self):
        return self.__HALL_Parameter

    @HALL_Parameter.setter
    def HALL_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Parameter__HALL_Parameter", None)
        self.__HALL_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type55"):
                opp_val = getattr(old_value, "Type55", None)
                if opp_val == self:
                    setattr(old_value, "Type55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type55"):
                opp_val = getattr(value, "Type55", None)
                setattr(value, "Type55", self)

    @property
    def MessageDefinition57(self):
        return self.__MessageDefinition57

    @MessageDefinition57.setter
    def MessageDefinition57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Parameter__MessageDefinition57", None)
        self.__MessageDefinition57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages58"):
                opp_val = getattr(old_value, "Messages58", None)
                if opp_val == self:
                    setattr(old_value, "Messages58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages58"):
                opp_val = getattr(value, "Messages58", None)
                setattr(value, "Messages58", self)

class HALL_Model:

    pass
class MessageHandler:

    pass
class FSM:

    pass
class HALL_Data:

    def __init__(self, name: str, initValue: str, currentValue: str, Data: "HALL_Component" = None, HALL_Data: "Type" = None, MessageDefinition62: "MessageDefinition" = None, data: "HALL_Component" = None):
        self.name = name
        self.initValue = initValue
        self.currentValue = currentValue
        self.Data = Data
        self.HALL_Data = HALL_Data
        self.MessageDefinition62 = MessageDefinition62
        self.data = data
        
    @property
    def currentValue(self) -> str:
        return self.__currentValue

    @currentValue.setter
    def currentValue(self, currentValue: str):
        self.__currentValue = currentValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def initValue(self) -> str:
        return self.__initValue

    @initValue.setter
    def initValue(self, initValue: str):
        self.__initValue = initValue

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Data__data", None)
        self.__data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Component"):
                opp_val = getattr(old_value, "Component", None)
                if opp_val == self:
                    setattr(old_value, "Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component"):
                opp_val = getattr(value, "Component", None)
                setattr(value, "Component", self)

    @property
    def MessageDefinition62(self):
        return self.__MessageDefinition62

    @MessageDefinition62.setter
    def MessageDefinition62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Data__MessageDefinition62", None)
        self.__MessageDefinition62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Messages63"):
                opp_val = getattr(old_value, "Messages63", None)
                if opp_val == self:
                    setattr(old_value, "Messages63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Messages63"):
                opp_val = getattr(value, "Messages63", None)
                setattr(value, "Messages63", self)

    @property
    def Data(self):
        return self.__Data

    @Data.setter
    def Data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Data__Data", None)
        self.__Data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataInvComponent"):
                opp_val = getattr(old_value, "dataInvComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataInvComponent"):
                opp_val = getattr(value, "dataInvComponent", None)
                if opp_val is None:
                    setattr(value, "dataInvComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HALL_Data(self):
        return self.__HALL_Data

    @HALL_Data.setter
    def HALL_Data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Data__HALL_Data", None)
        self.__HALL_Data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type60"):
                opp_val = getattr(old_value, "Type60", None)
                if opp_val == self:
                    setattr(old_value, "Type60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type60"):
                opp_val = getattr(value, "Type60", None)
                setattr(value, "Type60", self)

class HALL_Component(ABC):

    def __init__(self, name: str, dataInvComponent: set["HALL_Data"] = None, FSM: "FSM" = None, MessageHandler: set["MessageHandler"] = None, Component: "HALL_Data" = None):
        self.name = name
        self.dataInvComponent = dataInvComponent if dataInvComponent is not None else set()
        self.FSM = FSM
        self.MessageHandler = MessageHandler if MessageHandler is not None else set()
        self.Component = Component
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dataInvComponent(self):
        return self.__dataInvComponent

    @dataInvComponent.setter
    def dataInvComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Component__dataInvComponent", None)
        self.__dataInvComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data"):
                    opp_val = getattr(item, "Data", None)
                    
                    if opp_val == self:
                        setattr(item, "Data", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data"):
                    opp_val = getattr(item, "Data", None)
                    
                    setattr(item, "Data", self)
                    

    @property
    def MessageHandler(self):
        return self.__MessageHandler

    @MessageHandler.setter
    def MessageHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Component__MessageHandler", None)
        self.__MessageHandler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Messages"):
                    opp_val = getattr(item, "Messages", None)
                    
                    if opp_val == self:
                        setattr(item, "Messages", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Messages"):
                    opp_val = getattr(item, "Messages", None)
                    
                    setattr(item, "Messages", self)
                    

    @property
    def FSM(self):
        return self.__FSM

    @FSM.setter
    def FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Component__FSM", None)
        self.__FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM11"):
                opp_val = getattr(old_value, "FSM11", None)
                if opp_val == self:
                    setattr(old_value, "FSM11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM11"):
                opp_val = getattr(value, "FSM11", None)
                setattr(value, "FSM11", self)

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Component__Component", None)
        self.__Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data"):
                opp_val = getattr(old_value, "data", None)
                if opp_val == self:
                    setattr(old_value, "data", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data"):
                opp_val = getattr(value, "data", None)
                setattr(value, "data", self)

class GeometryData:

    pass
class HALL_Geometry_GeometryData3D(GeometryData):

    pass
class HALL_Geometry_GeometryData2D(GeometryData):

    def __init__(self, labelText: str, Point2D: set["Point2D"] = None, Geometry2: "HALL_VisualObject"):
        self.labelText = labelText
        self.Point2D = Point2D if Point2D is not None else set()
        
    @property
    def labelText(self) -> str:
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText

    @property
    def Point2D(self):
        return self.__Point2D

    @Point2D.setter
    def Point2D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_Geometry_GeometryData2D__Point2D", None)
        self.__Point2D = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Geometry119"):
                    opp_val = getattr(item, "Geometry119", None)
                    
                    if opp_val == self:
                        setattr(item, "Geometry119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Geometry119"):
                    opp_val = getattr(item, "Geometry119", None)
                    
                    setattr(item, "Geometry119", self)
                    

class ColorData:

    pass
class Component:

    pass
class HALL_SystemComponent(Component):

    pass
class HALL_UserProfile(Component):

    def __init__(self, numberofcompletedtasks: int, UserProfile: "HALL_VisualObject" = None, UserProfile22: "HALL_Model" = None, visualObjectInv: set["HALL_VisualObject"] = None, taskObjectInv: set["HALL_TaskObject"] = None, userProfile: "HALL_Model" = None, UserProfile36: "HALL_UserProfile" = None, componentSetInv35: set["HALL_UserProfile"] = None, UserProfile40: "HALL_UserProfile" = None, componentSet39: "HALL_UserProfile" = None, UserProfile43: "HALL_TaskObject" = None):
        self.numberofcompletedtasks = numberofcompletedtasks
        self.UserProfile = UserProfile
        self.UserProfile22 = UserProfile22
        self.visualObjectInv = visualObjectInv if visualObjectInv is not None else set()
        self.taskObjectInv = taskObjectInv if taskObjectInv is not None else set()
        self.userProfile = userProfile
        self.UserProfile36 = UserProfile36
        self.componentSetInv35 = componentSetInv35 if componentSetInv35 is not None else set()
        self.UserProfile40 = UserProfile40
        self.componentSet39 = componentSet39
        self.UserProfile43 = UserProfile43
        
    @property
    def numberofcompletedtasks(self) -> int:
        return self.__numberofcompletedtasks

    @numberofcompletedtasks.setter
    def numberofcompletedtasks(self, numberofcompletedtasks: int):
        self.__numberofcompletedtasks = numberofcompletedtasks

    @property
    def taskObjectInv(self):
        return self.__taskObjectInv

    @taskObjectInv.setter
    def taskObjectInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__taskObjectInv", None)
        self.__taskObjectInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskObject"):
                    opp_val = getattr(item, "TaskObject", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskObject"):
                    opp_val = getattr(item, "TaskObject", None)
                    
                    setattr(item, "TaskObject", self)
                    

    @property
    def UserProfile43(self):
        return self.__UserProfile43

    @UserProfile43.setter
    def UserProfile43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile43", None)
        self.__UserProfile43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskObject"):
                opp_val = getattr(old_value, "taskObject", None)
                if opp_val == self:
                    setattr(old_value, "taskObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskObject"):
                opp_val = getattr(value, "taskObject", None)
                setattr(value, "taskObject", self)

    @property
    def visualObjectInv(self):
        return self.__visualObjectInv

    @visualObjectInv.setter
    def visualObjectInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__visualObjectInv", None)
        self.__visualObjectInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualObject29"):
                    opp_val = getattr(item, "VisualObject29", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualObject29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualObject29"):
                    opp_val = getattr(item, "VisualObject29", None)
                    
                    setattr(item, "VisualObject29", self)
                    

    @property
    def componentSetInv35(self):
        return self.__componentSetInv35

    @componentSetInv35.setter
    def componentSetInv35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__componentSetInv35", None)
        self.__componentSetInv35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UserProfile36"):
                    opp_val = getattr(item, "UserProfile36", None)
                    
                    if opp_val == self:
                        setattr(item, "UserProfile36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UserProfile36"):
                    opp_val = getattr(item, "UserProfile36", None)
                    
                    setattr(item, "UserProfile36", self)
                    

    @property
    def componentSet39(self):
        return self.__componentSet39

    @componentSet39.setter
    def componentSet39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__componentSet39", None)
        self.__componentSet39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserProfile40"):
                opp_val = getattr(old_value, "UserProfile40", None)
                if opp_val == self:
                    setattr(old_value, "UserProfile40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserProfile40"):
                opp_val = getattr(value, "UserProfile40", None)
                setattr(value, "UserProfile40", self)

    @property
    def UserProfile22(self):
        return self.__UserProfile22

    @UserProfile22.setter
    def UserProfile22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile22", None)
        self.__UserProfile22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "userProfileInv"):
                opp_val = getattr(old_value, "userProfileInv", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "userProfileInv"):
                opp_val = getattr(value, "userProfileInv", None)
                if opp_val is None:
                    setattr(value, "userProfileInv", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UserProfile40(self):
        return self.__UserProfile40

    @UserProfile40.setter
    def UserProfile40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile40", None)
        self.__UserProfile40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSet39"):
                opp_val = getattr(old_value, "componentSet39", None)
                if opp_val == self:
                    setattr(old_value, "componentSet39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSet39"):
                opp_val = getattr(value, "componentSet39", None)
                setattr(value, "componentSet39", self)

    @property
    def UserProfile(self):
        return self.__UserProfile

    @UserProfile.setter
    def UserProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile", None)
        self.__UserProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "visualObject"):
                opp_val = getattr(old_value, "visualObject", None)
                if opp_val == self:
                    setattr(old_value, "visualObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "visualObject"):
                opp_val = getattr(value, "visualObject", None)
                setattr(value, "visualObject", self)

    @property
    def userProfile(self):
        return self.__userProfile

    @userProfile.setter
    def userProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__userProfile", None)
        self.__userProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model32"):
                opp_val = getattr(old_value, "Model32", None)
                if opp_val == self:
                    setattr(old_value, "Model32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model32"):
                opp_val = getattr(value, "Model32", None)
                setattr(value, "Model32", self)

    @property
    def UserProfile36(self):
        return self.__UserProfile36

    @UserProfile36.setter
    def UserProfile36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_UserProfile__UserProfile36", None)
        self.__UserProfile36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSetInv35"):
                opp_val = getattr(old_value, "componentSetInv35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSetInv35"):
                opp_val = getattr(value, "componentSetInv35", None)
                if opp_val is None:
                    setattr(value, "componentSetInv35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HALL_TaskObject(Component):

    def __init__(self, completionTime: int, numberofgoalscompleted: int, TaskObject51: "HALL_TaskObject" = None, componentSet50: "HALL_TaskObject" = None, TaskObject53: "HALL_Goal" = None, TaskObject: "HALL_UserProfile" = None, goalInv: set["HALL_Goal"] = None, taskObject: "HALL_UserProfile" = None, TaskObject47: "HALL_TaskObject" = None, componentSetInv46: set["HALL_TaskObject"] = None):
        self.completionTime = completionTime
        self.numberofgoalscompleted = numberofgoalscompleted
        self.TaskObject51 = TaskObject51
        self.componentSet50 = componentSet50
        self.TaskObject53 = TaskObject53
        self.TaskObject = TaskObject
        self.goalInv = goalInv if goalInv is not None else set()
        self.taskObject = taskObject
        self.TaskObject47 = TaskObject47
        self.componentSetInv46 = componentSetInv46 if componentSetInv46 is not None else set()
        
    @property
    def completionTime(self) -> int:
        return self.__completionTime

    @completionTime.setter
    def completionTime(self, completionTime: int):
        self.__completionTime = completionTime

    @property
    def numberofgoalscompleted(self) -> int:
        return self.__numberofgoalscompleted

    @numberofgoalscompleted.setter
    def numberofgoalscompleted(self, numberofgoalscompleted: int):
        self.__numberofgoalscompleted = numberofgoalscompleted

    @property
    def TaskObject51(self):
        return self.__TaskObject51

    @TaskObject51.setter
    def TaskObject51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject51", None)
        self.__TaskObject51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSet50"):
                opp_val = getattr(old_value, "componentSet50", None)
                if opp_val == self:
                    setattr(old_value, "componentSet50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSet50"):
                opp_val = getattr(value, "componentSet50", None)
                setattr(value, "componentSet50", self)

    @property
    def taskObject(self):
        return self.__taskObject

    @taskObject.setter
    def taskObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__taskObject", None)
        self.__taskObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserProfile43"):
                opp_val = getattr(old_value, "UserProfile43", None)
                if opp_val == self:
                    setattr(old_value, "UserProfile43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserProfile43"):
                opp_val = getattr(value, "UserProfile43", None)
                setattr(value, "UserProfile43", self)

    @property
    def componentSet50(self):
        return self.__componentSet50

    @componentSet50.setter
    def componentSet50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__componentSet50", None)
        self.__componentSet50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskObject51"):
                opp_val = getattr(old_value, "TaskObject51", None)
                if opp_val == self:
                    setattr(old_value, "TaskObject51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskObject51"):
                opp_val = getattr(value, "TaskObject51", None)
                setattr(value, "TaskObject51", self)

    @property
    def TaskObject(self):
        return self.__TaskObject

    @TaskObject.setter
    def TaskObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject", None)
        self.__TaskObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskObjectInv"):
                opp_val = getattr(old_value, "taskObjectInv", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskObjectInv"):
                opp_val = getattr(value, "taskObjectInv", None)
                if opp_val is None:
                    setattr(value, "taskObjectInv", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def goalInv(self):
        return self.__goalInv

    @goalInv.setter
    def goalInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__goalInv", None)
        self.__goalInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Goal"):
                    opp_val = getattr(item, "Goal", None)
                    
                    if opp_val == self:
                        setattr(item, "Goal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Goal"):
                    opp_val = getattr(item, "Goal", None)
                    
                    setattr(item, "Goal", self)
                    

    @property
    def TaskObject47(self):
        return self.__TaskObject47

    @TaskObject47.setter
    def TaskObject47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject47", None)
        self.__TaskObject47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSetInv46"):
                opp_val = getattr(old_value, "componentSetInv46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSetInv46"):
                opp_val = getattr(value, "componentSetInv46", None)
                if opp_val is None:
                    setattr(value, "componentSetInv46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TaskObject53(self):
        return self.__TaskObject53

    @TaskObject53.setter
    def TaskObject53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__TaskObject53", None)
        self.__TaskObject53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "goal"):
                opp_val = getattr(old_value, "goal", None)
                if opp_val == self:
                    setattr(old_value, "goal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "goal"):
                opp_val = getattr(value, "goal", None)
                setattr(value, "goal", self)

    @property
    def componentSetInv46(self):
        return self.__componentSetInv46

    @componentSetInv46.setter
    def componentSetInv46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_TaskObject__componentSetInv46", None)
        self.__componentSetInv46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskObject47"):
                    opp_val = getattr(item, "TaskObject47", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskObject47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskObject47"):
                    opp_val = getattr(item, "TaskObject47", None)
                    
                    setattr(item, "TaskObject47", self)
                    

class HALL_VisualObject(Component):

    def __init__(self, vtype: str, ColorData: "ColorData" = None, GeometryData: "GeometryData" = None, visualObject: "HALL_UserProfile" = None, VisualObject: "HALL_VisualObject" = None, componentSetInv: set["HALL_VisualObject"] = None, VisualObject8: "HALL_VisualObject" = None, componentSet: "HALL_VisualObject" = None, VisualObject29: "HALL_UserProfile" = None):
        self.vtype = vtype
        self.ColorData = ColorData
        self.GeometryData = GeometryData
        self.visualObject = visualObject
        self.VisualObject = VisualObject
        self.componentSetInv = componentSetInv if componentSetInv is not None else set()
        self.VisualObject8 = VisualObject8
        self.componentSet = componentSet
        self.VisualObject29 = VisualObject29
        
    @property
    def vtype(self) -> str:
        return self.__vtype

    @vtype.setter
    def vtype(self, vtype: str):
        self.__vtype = vtype

    @property
    def VisualObject29(self):
        return self.__VisualObject29

    @VisualObject29.setter
    def VisualObject29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__VisualObject29", None)
        self.__VisualObject29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "visualObjectInv"):
                opp_val = getattr(old_value, "visualObjectInv", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "visualObjectInv"):
                opp_val = getattr(value, "visualObjectInv", None)
                if opp_val is None:
                    setattr(value, "visualObjectInv", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def VisualObject8(self):
        return self.__VisualObject8

    @VisualObject8.setter
    def VisualObject8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__VisualObject8", None)
        self.__VisualObject8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSet"):
                opp_val = getattr(old_value, "componentSet", None)
                if opp_val == self:
                    setattr(old_value, "componentSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSet"):
                opp_val = getattr(value, "componentSet", None)
                setattr(value, "componentSet", self)

    @property
    def VisualObject(self):
        return self.__VisualObject

    @VisualObject.setter
    def VisualObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__VisualObject", None)
        self.__VisualObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentSetInv"):
                opp_val = getattr(old_value, "componentSetInv", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentSetInv"):
                opp_val = getattr(value, "componentSetInv", None)
                if opp_val is None:
                    setattr(value, "componentSetInv", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ColorData(self):
        return self.__ColorData

    @ColorData.setter
    def ColorData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__ColorData", None)
        self.__ColorData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry"):
                opp_val = getattr(old_value, "Geometry", None)
                if opp_val == self:
                    setattr(old_value, "Geometry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry"):
                opp_val = getattr(value, "Geometry", None)
                setattr(value, "Geometry", self)

    @property
    def componentSet(self):
        return self.__componentSet

    @componentSet.setter
    def componentSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__componentSet", None)
        self.__componentSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualObject8"):
                opp_val = getattr(old_value, "VisualObject8", None)
                if opp_val == self:
                    setattr(old_value, "VisualObject8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualObject8"):
                opp_val = getattr(value, "VisualObject8", None)
                setattr(value, "VisualObject8", self)

    @property
    def visualObject(self):
        return self.__visualObject

    @visualObject.setter
    def visualObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__visualObject", None)
        self.__visualObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserProfile"):
                opp_val = getattr(old_value, "UserProfile", None)
                if opp_val == self:
                    setattr(old_value, "UserProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserProfile"):
                opp_val = getattr(value, "UserProfile", None)
                setattr(value, "UserProfile", self)

    @property
    def GeometryData(self):
        return self.__GeometryData

    @GeometryData.setter
    def GeometryData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__GeometryData", None)
        self.__GeometryData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry2"):
                opp_val = getattr(old_value, "Geometry2", None)
                if opp_val == self:
                    setattr(old_value, "Geometry2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry2"):
                opp_val = getattr(value, "Geometry2", None)
                setattr(value, "Geometry2", self)

    @property
    def componentSetInv(self):
        return self.__componentSetInv

    @componentSetInv.setter
    def componentSetInv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HALL_VisualObject__componentSetInv", None)
        self.__componentSetInv = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualObject"):
                    opp_val = getattr(item, "VisualObject", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualObject"):
                    opp_val = getattr(item, "VisualObject", None)
                    
                    setattr(item, "VisualObject", self)
                    
