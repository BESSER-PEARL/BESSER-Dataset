from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DeferrableAct(Enum):
    DEFFERABLE = "DEFFERABLE"
    NOT_DEFFERABLE = "NOT_DEFFERABLE"
class DeferredAct(Enum):
    INITIALLY_IMMEDIATE = "INITIALLY_IMMEDIATE"
    INITIALLY_DEFERRED = "INITIALLY_DEFERRED"
class Action(Enum):
    SET_DEFAULT = "SET_DEFAULT"
    CASCADE = "CASCADE"
    RESTRICT = "RESTRICT"
    NO_ACTION = "NO_ACTION"
    SET_NULL = "SET_NULL"
class ReferencingType(Enum):
    DEFAULT = "DEFAULT"
    PARTIAL = "PARTIAL"
    FULL = "FULL"


############################################
# Definition of Classes
############################################

class rdbms_ModelElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class DataType:

    pass
class PKeyAndUnique:

    pass
class Constraints:

    pass
class rdbms_PKeyAndUnique(Constraints):

    pass
class rdbms_CheckCon(Constraints):

    def __init__(self, checkCondition: str, rdbms_CheckCon: "rdbms_Table" = None):
        self.checkCondition = checkCondition
        self.rdbms_CheckCon = rdbms_CheckCon
        
    @property
    def checkCondition(self) -> str:
        return self.__checkCondition

    @checkCondition.setter
    def checkCondition(self, checkCondition: str):
        self.__checkCondition = checkCondition

    @property
    def rdbms_CheckCon(self):
        return self.__rdbms_CheckCon

    @rdbms_CheckCon.setter
    def rdbms_CheckCon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_CheckCon__rdbms_CheckCon", None)
        self.__rdbms_CheckCon = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_Table13"):
                opp_val = getattr(old_value, "rdbms_Table13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_Table13"):
                opp_val = getattr(value, "rdbms_Table13", None)
                if opp_val is None:
                    setattr(value, "rdbms_Table13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_UniqueCon(PKeyAndUnique):

    pass
class rdbms_PrimaryKeyCon(PKeyAndUnique):

    pass
class rdbms_ForeignKey(Constraints):

    def __init__(self, updateActionRHS: str, deleteActionRHS: str, match: str, inverseReferentialIntegrityCon: bool, ForeignKey: "rdbms_Table" = None, rdbms_ForeignKey: "rdbms_Column" = None, rdbms_ForeignKey21: "rdbms_PKeyAndUnique" = None, rdbms_ForeignKey24: set["rdbms_Column"] = None, rdbms_ForeignKey27: "rdbms_Table" = None, tableFKs: "rdbms_Table" = None):
        self.updateActionRHS = updateActionRHS
        self.deleteActionRHS = deleteActionRHS
        self.match = match
        self.inverseReferentialIntegrityCon = inverseReferentialIntegrityCon
        self.ForeignKey = ForeignKey
        self.rdbms_ForeignKey = rdbms_ForeignKey
        self.rdbms_ForeignKey21 = rdbms_ForeignKey21
        self.rdbms_ForeignKey24 = rdbms_ForeignKey24 if rdbms_ForeignKey24 is not None else set()
        self.rdbms_ForeignKey27 = rdbms_ForeignKey27
        self.tableFKs = tableFKs
        
    @property
    def inverseReferentialIntegrityCon(self) -> bool:
        return self.__inverseReferentialIntegrityCon

    @inverseReferentialIntegrityCon.setter
    def inverseReferentialIntegrityCon(self, inverseReferentialIntegrityCon: bool):
        self.__inverseReferentialIntegrityCon = inverseReferentialIntegrityCon

    @property
    def deleteActionRHS(self) -> str:
        return self.__deleteActionRHS

    @deleteActionRHS.setter
    def deleteActionRHS(self, deleteActionRHS: str):
        self.__deleteActionRHS = deleteActionRHS

    @property
    def updateActionRHS(self) -> str:
        return self.__updateActionRHS

    @updateActionRHS.setter
    def updateActionRHS(self, updateActionRHS: str):
        self.__updateActionRHS = updateActionRHS

    @property
    def match(self) -> str:
        return self.__match

    @match.setter
    def match(self, match: str):
        self.__match = match

    @property
    def tableFKs(self):
        return self.__tableFKs

    @tableFKs.setter
    def tableFKs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_ForeignKey__tableFKs", None)
        self.__tableFKs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table"):
                opp_val = getattr(old_value, "Table", None)
                if opp_val == self:
                    setattr(old_value, "Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table"):
                opp_val = getattr(value, "Table", None)
                setattr(value, "Table", self)

    @property
    def rdbms_ForeignKey27(self):
        return self.__rdbms_ForeignKey27

    @rdbms_ForeignKey27.setter
    def rdbms_ForeignKey27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_ForeignKey__rdbms_ForeignKey27", None)
        self.__rdbms_ForeignKey27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_Table28"):
                opp_val = getattr(old_value, "rdbms_Table28", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_Table28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_Table28"):
                opp_val = getattr(value, "rdbms_Table28", None)
                setattr(value, "rdbms_Table28", self)

    @property
    def rdbms_ForeignKey24(self):
        return self.__rdbms_ForeignKey24

    @rdbms_ForeignKey24.setter
    def rdbms_ForeignKey24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_ForeignKey__rdbms_ForeignKey24", None)
        self.__rdbms_ForeignKey24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdbms_Column25"):
                    opp_val = getattr(item, "rdbms_Column25", None)
                    
                    if opp_val == self:
                        setattr(item, "rdbms_Column25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdbms_Column25"):
                    opp_val = getattr(item, "rdbms_Column25", None)
                    
                    setattr(item, "rdbms_Column25", self)
                    

    @property
    def rdbms_ForeignKey21(self):
        return self.__rdbms_ForeignKey21

    @rdbms_ForeignKey21.setter
    def rdbms_ForeignKey21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_ForeignKey__rdbms_ForeignKey21", None)
        self.__rdbms_ForeignKey21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_PKeyAndUnique22"):
                opp_val = getattr(old_value, "rdbms_PKeyAndUnique22", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_PKeyAndUnique22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_PKeyAndUnique22"):
                opp_val = getattr(value, "rdbms_PKeyAndUnique22", None)
                setattr(value, "rdbms_PKeyAndUnique22", self)

    @property
    def ForeignKey(self):
        return self.__ForeignKey

    @ForeignKey.setter
    def ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_ForeignKey__ForeignKey", None)
        self.__ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FKTable"):
                opp_val = getattr(old_value, "FKTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FKTable"):
                opp_val = getattr(value, "FKTable", None)
                if opp_val is None:
                    setattr(value, "FKTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_ForeignKey(self):
        return self.__rdbms_ForeignKey

    @rdbms_ForeignKey.setter
    def rdbms_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_ForeignKey__rdbms_ForeignKey", None)
        self.__rdbms_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_Column17"):
                opp_val = getattr(old_value, "rdbms_Column17", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_Column17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_Column17"):
                opp_val = getattr(value, "rdbms_Column17", None)
                setattr(value, "rdbms_Column17", self)

class rdbms_UserDefinedDataType(DataType):

    def __init__(self, precision: int, length: int, defaultValue: str, rdbms_UserDefinedDataType: "rdbms_Database" = None, rdbms_UserDefinedDataType34: "rdbms_SystemDataType" = None):
        self.precision = precision
        self.length = length
        self.defaultValue = defaultValue
        self.rdbms_UserDefinedDataType = rdbms_UserDefinedDataType
        self.rdbms_UserDefinedDataType34 = rdbms_UserDefinedDataType34
        
    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def rdbms_UserDefinedDataType(self):
        return self.__rdbms_UserDefinedDataType

    @rdbms_UserDefinedDataType.setter
    def rdbms_UserDefinedDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_UserDefinedDataType__rdbms_UserDefinedDataType", None)
        self.__rdbms_UserDefinedDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_Database"):
                opp_val = getattr(old_value, "rdbms_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_Database"):
                opp_val = getattr(value, "rdbms_Database", None)
                if opp_val is None:
                    setattr(value, "rdbms_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_UserDefinedDataType34(self):
        return self.__rdbms_UserDefinedDataType34

    @rdbms_UserDefinedDataType34.setter
    def rdbms_UserDefinedDataType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_UserDefinedDataType__rdbms_UserDefinedDataType34", None)
        self.__rdbms_UserDefinedDataType34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_SystemDataType35"):
                opp_val = getattr(old_value, "rdbms_SystemDataType35", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_SystemDataType35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_SystemDataType35"):
                opp_val = getattr(value, "rdbms_SystemDataType35", None)
                setattr(value, "rdbms_SystemDataType35", self)

class ModelElement:

    pass
class rdbms_Constraints(ModelElement):

    def __init__(self, deferrable: str, deferred: str):
        self.deferrable = deferrable
        self.deferred = deferred
        
    @property
    def deferred(self) -> str:
        return self.__deferred

    @deferred.setter
    def deferred(self, deferred: str):
        self.__deferred = deferred

    @property
    def deferrable(self) -> str:
        return self.__deferrable

    @deferrable.setter
    def deferrable(self, deferrable: str):
        self.__deferrable = deferrable

class rdbms_DataType(ModelElement):

    pass
class rdbms_Column(ModelElement):

    def __init__(self, default: str, nullable: bool, precision: int, length: int, rdbms_Column: "rdbms_Table" = None, rdbms_Column15: "rdbms_PKeyAndUnique" = None, rdbms_Column17: "rdbms_ForeignKey" = None, rdbms_Column19: "rdbms_DataType" = None, rdbms_Column25: "rdbms_ForeignKey" = None, rdbms_Column32: "rdbms_PKeyAndUnique" = None):
        self.default = default
        self.nullable = nullable
        self.precision = precision
        self.length = length
        self.rdbms_Column = rdbms_Column
        self.rdbms_Column15 = rdbms_Column15
        self.rdbms_Column17 = rdbms_Column17
        self.rdbms_Column19 = rdbms_Column19
        self.rdbms_Column25 = rdbms_Column25
        self.rdbms_Column32 = rdbms_Column32
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def rdbms_Column32(self):
        return self.__rdbms_Column32

    @rdbms_Column32.setter
    def rdbms_Column32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Column__rdbms_Column32", None)
        self.__rdbms_Column32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_PKeyAndUnique31"):
                opp_val = getattr(old_value, "rdbms_PKeyAndUnique31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_PKeyAndUnique31"):
                opp_val = getattr(value, "rdbms_PKeyAndUnique31", None)
                if opp_val is None:
                    setattr(value, "rdbms_PKeyAndUnique31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_Column(self):
        return self.__rdbms_Column

    @rdbms_Column.setter
    def rdbms_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Column__rdbms_Column", None)
        self.__rdbms_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_Table11"):
                opp_val = getattr(old_value, "rdbms_Table11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_Table11"):
                opp_val = getattr(value, "rdbms_Table11", None)
                if opp_val is None:
                    setattr(value, "rdbms_Table11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbms_Column15(self):
        return self.__rdbms_Column15

    @rdbms_Column15.setter
    def rdbms_Column15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Column__rdbms_Column15", None)
        self.__rdbms_Column15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_PKeyAndUnique"):
                opp_val = getattr(old_value, "rdbms_PKeyAndUnique", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_PKeyAndUnique", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_PKeyAndUnique"):
                opp_val = getattr(value, "rdbms_PKeyAndUnique", None)
                setattr(value, "rdbms_PKeyAndUnique", self)

    @property
    def rdbms_Column17(self):
        return self.__rdbms_Column17

    @rdbms_Column17.setter
    def rdbms_Column17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Column__rdbms_Column17", None)
        self.__rdbms_Column17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_ForeignKey"):
                opp_val = getattr(old_value, "rdbms_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_ForeignKey"):
                opp_val = getattr(value, "rdbms_ForeignKey", None)
                setattr(value, "rdbms_ForeignKey", self)

    @property
    def rdbms_Column19(self):
        return self.__rdbms_Column19

    @rdbms_Column19.setter
    def rdbms_Column19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Column__rdbms_Column19", None)
        self.__rdbms_Column19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_DataType"):
                opp_val = getattr(old_value, "rdbms_DataType", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_DataType"):
                opp_val = getattr(value, "rdbms_DataType", None)
                setattr(value, "rdbms_DataType", self)

    @property
    def rdbms_Column25(self):
        return self.__rdbms_Column25

    @rdbms_Column25.setter
    def rdbms_Column25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_Column__rdbms_Column25", None)
        self.__rdbms_Column25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_ForeignKey24"):
                opp_val = getattr(old_value, "rdbms_ForeignKey24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_ForeignKey24"):
                opp_val = getattr(value, "rdbms_ForeignKey24", None)
                if opp_val is None:
                    setattr(value, "rdbms_ForeignKey24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdbms_Table(ModelElement):

    pass
class rdbms_Database(ModelElement):

    pass
class rdbms_SystemDataType(DataType):

    def __init__(self, predefinedLength: int, predefinedDecPlaces: int, rdbms_SystemDataType: "rdbms_Database" = None, rdbms_SystemDataType35: "rdbms_UserDefinedDataType" = None):
        self.predefinedLength = predefinedLength
        self.predefinedDecPlaces = predefinedDecPlaces
        self.rdbms_SystemDataType = rdbms_SystemDataType
        self.rdbms_SystemDataType35 = rdbms_SystemDataType35
        
    @property
    def predefinedLength(self) -> int:
        return self.__predefinedLength

    @predefinedLength.setter
    def predefinedLength(self, predefinedLength: int):
        self.__predefinedLength = predefinedLength

    @property
    def predefinedDecPlaces(self) -> int:
        return self.__predefinedDecPlaces

    @predefinedDecPlaces.setter
    def predefinedDecPlaces(self, predefinedDecPlaces: int):
        self.__predefinedDecPlaces = predefinedDecPlaces

    @property
    def rdbms_SystemDataType35(self):
        return self.__rdbms_SystemDataType35

    @rdbms_SystemDataType35.setter
    def rdbms_SystemDataType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_SystemDataType__rdbms_SystemDataType35", None)
        self.__rdbms_SystemDataType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_UserDefinedDataType34"):
                opp_val = getattr(old_value, "rdbms_UserDefinedDataType34", None)
                if opp_val == self:
                    setattr(old_value, "rdbms_UserDefinedDataType34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_UserDefinedDataType34"):
                opp_val = getattr(value, "rdbms_UserDefinedDataType34", None)
                setattr(value, "rdbms_UserDefinedDataType34", self)

    @property
    def rdbms_SystemDataType(self):
        return self.__rdbms_SystemDataType

    @rdbms_SystemDataType.setter
    def rdbms_SystemDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbms_SystemDataType__rdbms_SystemDataType", None)
        self.__rdbms_SystemDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbms_Database4"):
                opp_val = getattr(old_value, "rdbms_Database4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbms_Database4"):
                opp_val = getattr(value, "rdbms_Database4", None)
                if opp_val is None:
                    setattr(value, "rdbms_Database4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
