from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class qvt_cst_IHasName(ABC):

    pass
class cst_qvt_EObject:

    pass
class IdentifierCS:

    pass
class cst_IHasName:

    pass
class cst_CSTNode:

    pass
class qvt_cst_IdentifierCS(cst_IHasName, cst_CSTNode):

    def __init__(self, value: str, qvt_cst_IdentifierCS: "cst_qvt_EObject" = None):
        self.value = value
        self.qvt_cst_IdentifierCS = qvt_cst_IdentifierCS
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def qvt_cst_IdentifierCS(self):
        return self.__qvt_cst_IdentifierCS

    @qvt_cst_IdentifierCS.setter
    def qvt_cst_IdentifierCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvt_cst_IdentifierCS__qvt_cst_IdentifierCS", None)
        self.__qvt_cst_IdentifierCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_qvt_EObject4"):
                opp_val = getattr(old_value, "cst_qvt_EObject4", None)
                if opp_val == self:
                    setattr(old_value, "cst_qvt_EObject4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_qvt_EObject4"):
                opp_val = getattr(value, "cst_qvt_EObject4", None)
                setattr(value, "cst_qvt_EObject4", self)

class qvt_cst_IdentifiedCS(cst_IHasName, cst_CSTNode):

    pass
class qvt_cst_ErrorNode:

    def __init__(self, message: str):
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message
