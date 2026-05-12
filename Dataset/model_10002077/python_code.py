from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class QuotaType(Enum):
    pass

############################################
# Definition of Classes
############################################










class QuotaItem:

    def __init__(self, id: str, quotaItemName: str, amount: int, comment: str, createdOn: str, type: QuotaType, sueprClassId: str, quota1: "Quota" = None):
        self.id = id
        self.quotaItemName = quotaItemName
        self.amount = amount
        self.comment = comment
        self.createdOn = createdOn
        self.type = type
        self.sueprClassId = sueprClassId
        self.quota1 = quota1
        
        pass
    @property
    def quotaItemName(self):
        return self.__quotaItemName
    @quotaItemName.setter
    def quotaItemName(self, quotaItemName: str):
        self.__quotaItemName = quotaItemName

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: QuotaType):
        self.__type = type

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def sueprClassId(self):
        return self.__sueprClassId
    @sueprClassId.setter
    def sueprClassId(self, sueprClassId: str):
        self.__sueprClassId = sueprClassId

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def createdOn(self):
        return self.__createdOn
    @createdOn.setter
    def createdOn(self, createdOn: str):
        self.__createdOn = createdOn

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def quota1(self):
        return self.__quota1
    @quota1.setter
    def quota1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QuotaItem__quota1", None)
        self.__quota1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "quotaItem0"):
                opp_val = getattr(old_value, "quotaItem0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "quotaItem0"):
                opp_val = getattr(value, "quotaItem0", None)
                if opp_val is None:
                    setattr(value, "quotaItem0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Quota:

    def __init__(self, id: str, quotaName: str, current: int, max: int, comment: str, quotaItem0: set["QuotaItem"] = None):
        self.id = id
        self.quotaName = quotaName
        self.current = current
        self.max = max
        self.comment = comment
        self.quotaItem0 = quotaItem0 if quotaItem0 is not None else set()
        
        pass
    @property
    def max(self):
        return self.__max
    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def current(self):
        return self.__current
    @current.setter
    def current(self, current: int):
        self.__current = current

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def quotaName(self):
        return self.__quotaName
    @quotaName.setter
    def quotaName(self, quotaName: str):
        self.__quotaName = quotaName

    @property
    def quotaItem0(self):
        return self.__quotaItem0
    @quotaItem0.setter
    def quotaItem0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Quota__quotaItem0", None)
        self.__quotaItem0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "quota1"):
                    opp_val = getattr(item, "quota1", None)
                    
                    if opp_val == self:
                        setattr(item, "quota1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "quota1"):
                    opp_val = getattr(item, "quota1", None)
                    
                    setattr(item, "quota1", self)
                    

