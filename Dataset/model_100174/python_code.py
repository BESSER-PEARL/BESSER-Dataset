from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DirectionKind(Enum):
    INOUT = "INOUT"
    RETURN = "RETURN"
    UNKNOWN = "UNKNOWN"
    IN = "IN"
    OUT = "OUT"
class MultiplicityKind(Enum):
    UNSPECIFIED = "UNSPECIFIED"
    ONE = "ONE"
    MANY = "MANY"
    ZERO_TO_ONE = "ZERO_TO_ONE"
    ZERO_TO_MANY = "ZERO_TO_MANY"
class ProcedureUpdateCount(Enum):
    AUTO = "AUTO"
    ZERO = "ZERO"
    ONE = "ONE"
    MULTIPLE = "MULTIPLE"
class SearchabilityType(Enum):
    SEARCHABLE = "SEARCHABLE"
    ALL_EXCEPT_LIKE = "ALL_EXCEPT_LIKE"
    LIKE_ONLY = "LIKE_ONLY"
    UNSEARCHABLE = "UNSEARCHABLE"
class NullableType(Enum):
    NO_NULLS = "NO_NULLS"
    NULLABLE = "NULLABLE"
    NULLABLE_UNKNOWN = "NULLABLE_UNKNOWN"


############################################
# Definition of Classes
############################################

class Table:

    pass
class relational_View(Table):

    pass
class relational_RelationalEntity(ABC):

    def __init__(self, name: str, nameInSource: str):
        self.name = name
        self.nameInSource = nameInSource
        
        pass
    @property
    def nameInSource(self):
        return self.__nameInSource

    @nameInSource.setter
    def nameInSource(self, nameInSource: str):
        self.__nameInSource = nameInSource


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Relationship:

    pass
class relational_BaseTable(Table):

    pass
class UniqueKey:

    pass
class relational_UniqueConstraint(UniqueKey):

    pass
class relational_PrimaryKey(UniqueKey):

    pass
class relational_LogicalRelationship(Relationship):

    pass
class relational_EObject:

    pass
class relational_ForeignKey(Relationship):

    def __init__(self, foreignKeyMultiplicity: str, primaryKeyMultiplicity: str, ForeignKey: "relational_Column" = None, foreignKeys: set["relational_Column"] = None, foreignKeys30: "relational_UniqueKey" = None, foreignKeys33: "relational_BaseTable" = None, ForeignKey38: "relational_UniqueKey" = None, ForeignKey94: "relational_BaseTable" = None):
        self.foreignKeyMultiplicity = foreignKeyMultiplicity
        self.primaryKeyMultiplicity = primaryKeyMultiplicity
        self.ForeignKey = ForeignKey
        self.foreignKeys = foreignKeys if foreignKeys is not None else set()
        self.foreignKeys30 = foreignKeys30
        self.foreignKeys33 = foreignKeys33
        self.ForeignKey38 = ForeignKey38
        self.ForeignKey94 = ForeignKey94
        
        pass
    @property
    def primaryKeyMultiplicity(self):
        return self.__primaryKeyMultiplicity

    @primaryKeyMultiplicity.setter
    def primaryKeyMultiplicity(self, primaryKeyMultiplicity: str):
        self.__primaryKeyMultiplicity = primaryKeyMultiplicity


    @property
    def foreignKeyMultiplicity(self):
        return self.__foreignKeyMultiplicity

    @foreignKeyMultiplicity.setter
    def foreignKeyMultiplicity(self, foreignKeyMultiplicity: str):
        self.__foreignKeyMultiplicity = foreignKeyMultiplicity


    @property
    def foreignKeys33(self):
        return self.__foreignKeys33

    @foreignKeys33.setter
    def foreignKeys33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__foreignKeys33", None)
        self.__foreignKeys33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BaseTable34"):
                opp_val = getattr(old_value, "BaseTable34", None)
                if opp_val == self:
                    setattr(old_value, "BaseTable34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BaseTable34"):
                opp_val = getattr(value, "BaseTable34", None)
                setattr(value, "BaseTable34", self)

    @property
    def ForeignKey94(self):
        return self.__ForeignKey94

    @ForeignKey94.setter
    def ForeignKey94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__ForeignKey94", None)
        self.__ForeignKey94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table93"):
                opp_val = getattr(old_value, "table93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table93"):
                opp_val = getattr(value, "table93", None)
                if opp_val is None:
                    setattr(value, "table93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ForeignKey(self):
        return self.__ForeignKey

    @ForeignKey.setter
    def ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__ForeignKey", None)
        self.__ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columns10"):
                opp_val = getattr(old_value, "columns10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columns10"):
                opp_val = getattr(value, "columns10", None)
                if opp_val is None:
                    setattr(value, "columns10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def foreignKeys30(self):
        return self.__foreignKeys30

    @foreignKeys30.setter
    def foreignKeys30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__foreignKeys30", None)
        self.__foreignKeys30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UniqueKey31"):
                opp_val = getattr(old_value, "UniqueKey31", None)
                if opp_val == self:
                    setattr(old_value, "UniqueKey31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UniqueKey31"):
                opp_val = getattr(value, "UniqueKey31", None)
                setattr(value, "UniqueKey31", self)

    @property
    def ForeignKey38(self):
        return self.__ForeignKey38

    @ForeignKey38.setter
    def ForeignKey38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__ForeignKey38", None)
        self.__ForeignKey38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uniqueKey"):
                opp_val = getattr(old_value, "uniqueKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uniqueKey"):
                opp_val = getattr(value, "uniqueKey", None)
                if opp_val is None:
                    setattr(value, "uniqueKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def foreignKeys(self):
        return self.__foreignKeys

    @foreignKeys.setter
    def foreignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ForeignKey__foreignKeys", None)
        self.__foreignKeys = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    if opp_val == self:
                        setattr(item, "Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    setattr(item, "Column", self)
                    

class RelationalEntity:

    pass
class relational_ColumnSet(RelationalEntity):

    pass
class relational_Relationship(RelationalEntity):

    pass
class relational_Procedure(RelationalEntity):

    def __init__(self, function: bool, updateCount: str, Procedure: "relational_Schema" = None, procedures: "relational_Schema" = None, procedure: set["relational_ProcedureParameter"] = None, procedures57: "relational_Catalog" = None, procedure60: "relational_ProcedureResult" = None, Procedure102: "relational_ProcedureResult" = None, Procedure43: "relational_Catalog" = None, Procedure70: "relational_ProcedureParameter" = None):
        self.function = function
        self.updateCount = updateCount
        self.Procedure = Procedure
        self.procedures = procedures
        self.procedure = procedure if procedure is not None else set()
        self.procedures57 = procedures57
        self.procedure60 = procedure60
        self.Procedure102 = Procedure102
        self.Procedure43 = Procedure43
        self.Procedure70 = Procedure70
        
        pass
    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, function: bool):
        self.__function = function


    @property
    def updateCount(self):
        return self.__updateCount

    @updateCount.setter
    def updateCount(self, updateCount: str):
        self.__updateCount = updateCount


    @property
    def Procedure43(self):
        return self.__Procedure43

    @Procedure43.setter
    def Procedure43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Procedure__Procedure43", None)
        self.__Procedure43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "catalog42"):
                opp_val = getattr(old_value, "catalog42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "catalog42"):
                opp_val = getattr(value, "catalog42", None)
                if opp_val is None:
                    setattr(value, "catalog42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def procedure60(self):
        return self.__procedure60

    @procedure60.setter
    def procedure60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Procedure__procedure60", None)
        self.__procedure60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcedureResult"):
                opp_val = getattr(old_value, "ProcedureResult", None)
                if opp_val == self:
                    setattr(old_value, "ProcedureResult", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcedureResult"):
                opp_val = getattr(value, "ProcedureResult", None)
                setattr(value, "ProcedureResult", self)

    @property
    def Procedure102(self):
        return self.__Procedure102

    @Procedure102.setter
    def Procedure102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Procedure__Procedure102", None)
        self.__Procedure102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "result"):
                opp_val = getattr(old_value, "result", None)
                if opp_val == self:
                    setattr(old_value, "result", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "result"):
                opp_val = getattr(value, "result", None)
                setattr(value, "result", self)

    @property
    def procedure(self):
        return self.__procedure

    @procedure.setter
    def procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Procedure__procedure", None)
        self.__procedure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProcedureParameter"):
                    opp_val = getattr(item, "ProcedureParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ProcedureParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProcedureParameter"):
                    opp_val = getattr(item, "ProcedureParameter", None)
                    
                    setattr(item, "ProcedureParameter", self)
                    

    @property
    def Procedure70(self):
        return self.__Procedure70

    @Procedure70.setter
    def Procedure70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Procedure__Procedure70", None)
        self.__Procedure70 = value
        
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
    def procedures57(self):
        return self.__procedures57

    @procedures57.setter
    def procedures57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Procedure__procedures57", None)
        self.__procedures57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Catalog58"):
                opp_val = getattr(old_value, "Catalog58", None)
                if opp_val == self:
                    setattr(old_value, "Catalog58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Catalog58"):
                opp_val = getattr(value, "Catalog58", None)
                setattr(value, "Catalog58", self)

    @property
    def procedures(self):
        return self.__procedures

    @procedures.setter
    def procedures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Procedure__procedures", None)
        self.__procedures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema54"):
                opp_val = getattr(old_value, "Schema54", None)
                if opp_val == self:
                    setattr(old_value, "Schema54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema54"):
                opp_val = getattr(value, "Schema54", None)
                setattr(value, "Schema54", self)

    @property
    def Procedure(self):
        return self.__Procedure

    @Procedure.setter
    def Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Procedure__Procedure", None)
        self.__Procedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema21"):
                opp_val = getattr(old_value, "schema21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema21"):
                opp_val = getattr(value, "schema21", None)
                if opp_val is None:
                    setattr(value, "schema21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class relational_ProcedureParameter(RelationalEntity):

    def __init__(self, direction: str, defaultValue: str, nativeType: str, length: int, precision: int, scale: int, nullable: str, radix: int, relational_ProcedureParameter: "relational_EObject" = None, ProcedureParameter: "relational_Procedure" = None, parameters: "relational_Procedure" = None):
        self.direction = direction
        self.defaultValue = defaultValue
        self.nativeType = nativeType
        self.length = length
        self.precision = precision
        self.scale = scale
        self.nullable = nullable
        self.radix = radix
        self.relational_ProcedureParameter = relational_ProcedureParameter
        self.ProcedureParameter = ProcedureParameter
        self.parameters = parameters
        
        pass
    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision


    @property
    def nativeType(self):
        return self.__nativeType

    @nativeType.setter
    def nativeType(self, nativeType: str):
        self.__nativeType = nativeType


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: str):
        self.__nullable = nullable


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def radix(self):
        return self.__radix

    @radix.setter
    def radix(self, radix: int):
        self.__radix = radix


    @property
    def ProcedureParameter(self):
        return self.__ProcedureParameter

    @ProcedureParameter.setter
    def ProcedureParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ProcedureParameter__ProcedureParameter", None)
        self.__ProcedureParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "procedure"):
                opp_val = getattr(old_value, "procedure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "procedure"):
                opp_val = getattr(value, "procedure", None)
                if opp_val is None:
                    setattr(value, "procedure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relational_ProcedureParameter(self):
        return self.__relational_ProcedureParameter

    @relational_ProcedureParameter.setter
    def relational_ProcedureParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ProcedureParameter__relational_ProcedureParameter", None)
        self.__relational_ProcedureParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_EObject72"):
                opp_val = getattr(old_value, "relational_EObject72", None)
                if opp_val == self:
                    setattr(old_value, "relational_EObject72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_EObject72"):
                opp_val = getattr(value, "relational_EObject72", None)
                setattr(value, "relational_EObject72", self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_ProcedureParameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Procedure70"):
                opp_val = getattr(old_value, "Procedure70", None)
                if opp_val == self:
                    setattr(old_value, "Procedure70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Procedure70"):
                opp_val = getattr(value, "Procedure70", None)
                setattr(value, "Procedure70", self)

class relational_Index(RelationalEntity):

    def __init__(self, filterCondition: str, nullable: bool, autoUpdate: bool, unique: bool, Index: "relational_Column" = None, Index24: "relational_Schema" = None, indexes64: set["relational_Column"] = None, indexes67: "relational_Catalog" = None, indexes: "relational_Schema" = None, Index46: "relational_Catalog" = None):
        self.filterCondition = filterCondition
        self.nullable = nullable
        self.autoUpdate = autoUpdate
        self.unique = unique
        self.Index = Index
        self.Index24 = Index24
        self.indexes64 = indexes64 if indexes64 is not None else set()
        self.indexes67 = indexes67
        self.indexes = indexes
        self.Index46 = Index46
        
        pass
    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def autoUpdate(self):
        return self.__autoUpdate

    @autoUpdate.setter
    def autoUpdate(self, autoUpdate: bool):
        self.__autoUpdate = autoUpdate


    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def filterCondition(self):
        return self.__filterCondition

    @filterCondition.setter
    def filterCondition(self, filterCondition: str):
        self.__filterCondition = filterCondition


    @property
    def Index24(self):
        return self.__Index24

    @Index24.setter
    def Index24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Index__Index24", None)
        self.__Index24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema23"):
                opp_val = getattr(old_value, "schema23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema23"):
                opp_val = getattr(value, "schema23", None)
                if opp_val is None:
                    setattr(value, "schema23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def indexes(self):
        return self.__indexes

    @indexes.setter
    def indexes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Index__indexes", None)
        self.__indexes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema62"):
                opp_val = getattr(old_value, "Schema62", None)
                if opp_val == self:
                    setattr(old_value, "Schema62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema62"):
                opp_val = getattr(value, "Schema62", None)
                setattr(value, "Schema62", self)

    @property
    def Index46(self):
        return self.__Index46

    @Index46.setter
    def Index46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Index__Index46", None)
        self.__Index46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "catalog45"):
                opp_val = getattr(old_value, "catalog45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "catalog45"):
                opp_val = getattr(value, "catalog45", None)
                if opp_val is None:
                    setattr(value, "catalog45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def indexes67(self):
        return self.__indexes67

    @indexes67.setter
    def indexes67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Index__indexes67", None)
        self.__indexes67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Catalog68"):
                opp_val = getattr(old_value, "Catalog68", None)
                if opp_val == self:
                    setattr(old_value, "Catalog68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Catalog68"):
                opp_val = getattr(value, "Catalog68", None)
                setattr(value, "Catalog68", self)

    @property
    def Index(self):
        return self.__Index

    @Index.setter
    def Index(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Index__Index", None)
        self.__Index = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columns8"):
                opp_val = getattr(old_value, "columns8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columns8"):
                opp_val = getattr(value, "columns8", None)
                if opp_val is None:
                    setattr(value, "columns8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def indexes64(self):
        return self.__indexes64

    @indexes64.setter
    def indexes64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Index__indexes64", None)
        self.__indexes64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column65"):
                    opp_val = getattr(item, "Column65", None)
                    
                    if opp_val == self:
                        setattr(item, "Column65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column65"):
                    opp_val = getattr(item, "Column65", None)
                    
                    setattr(item, "Column65", self)
                    

class relational_UniqueKey(RelationalEntity):

    def __init__(self, UniqueKey: "relational_Column" = None, UniqueKey31: "relational_ForeignKey" = None, uniqueKeys: set["relational_Column"] = None, uniqueKey: set["relational_ForeignKey"] = None):
        self.UniqueKey = UniqueKey
        self.UniqueKey31 = UniqueKey31
        self.uniqueKeys = uniqueKeys if uniqueKeys is not None else set()
        self.uniqueKey = uniqueKey if uniqueKey is not None else set()
        
        pass
    @property
    def UniqueKey(self):
        return self.__UniqueKey

    @UniqueKey.setter
    def UniqueKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_UniqueKey__UniqueKey", None)
        self.__UniqueKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columns"):
                opp_val = getattr(old_value, "columns", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columns"):
                opp_val = getattr(value, "columns", None)
                if opp_val is None:
                    setattr(value, "columns", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uniqueKey(self):
        return self.__uniqueKey

    @uniqueKey.setter
    def uniqueKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_UniqueKey__uniqueKey", None)
        self.__uniqueKey = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey38"):
                    opp_val = getattr(item, "ForeignKey38", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey38"):
                    opp_val = getattr(item, "ForeignKey38", None)
                    
                    setattr(item, "ForeignKey38", self)
                    

    @property
    def UniqueKey31(self):
        return self.__UniqueKey31

    @UniqueKey31.setter
    def UniqueKey31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_UniqueKey__UniqueKey31", None)
        self.__UniqueKey31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foreignKeys30"):
                opp_val = getattr(old_value, "foreignKeys30", None)
                if opp_val == self:
                    setattr(old_value, "foreignKeys30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foreignKeys30"):
                opp_val = getattr(value, "foreignKeys30", None)
                setattr(value, "foreignKeys30", self)

    @property
    def uniqueKeys(self):
        return self.__uniqueKeys

    @uniqueKeys.setter
    def uniqueKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_UniqueKey__uniqueKeys", None)
        self.__uniqueKeys = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column36"):
                    opp_val = getattr(item, "Column36", None)
                    
                    if opp_val == self:
                        setattr(item, "Column36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column36"):
                    opp_val = getattr(item, "Column36", None)
                    
                    setattr(item, "Column36", self)
                    

    def getTable(self) :
        # TODO: Implement getTable method
        pass

class relational_Column(RelationalEntity):

    def __init__(self, nullable: str, autoIncremented: bool, defaultValue: str, minimumValue: str, maximumValue: str, format: str, nativeType: str, length: int, fixedLength: bool, precision: int, scale: int, characterSetName: str, collationName: str, selectable: bool, updateable: bool, caseSensitive: bool, searchability: str, currency: bool, radix: int, signed: bool, distinctValueCount: int, nullValueCount: int, columns: set["relational_UniqueKey"] = None, columns8: set["relational_Index"] = None, columns10: set["relational_ForeignKey"] = None, columns12: set["relational_AccessPattern"] = None, columns15: "relational_ColumnSet" = None, relational_Column: "relational_EObject" = None, Column: "relational_ForeignKey" = None, Column36: "relational_UniqueKey" = None, Column65: "relational_Index" = None, Column76: "relational_AccessPattern" = None, Column100: "relational_ColumnSet" = None):
        self.nullable = nullable
        self.autoIncremented = autoIncremented
        self.defaultValue = defaultValue
        self.minimumValue = minimumValue
        self.maximumValue = maximumValue
        self.format = format
        self.nativeType = nativeType
        self.length = length
        self.fixedLength = fixedLength
        self.precision = precision
        self.scale = scale
        self.characterSetName = characterSetName
        self.collationName = collationName
        self.selectable = selectable
        self.updateable = updateable
        self.caseSensitive = caseSensitive
        self.searchability = searchability
        self.currency = currency
        self.radix = radix
        self.signed = signed
        self.distinctValueCount = distinctValueCount
        self.nullValueCount = nullValueCount
        self.columns = columns if columns is not None else set()
        self.columns8 = columns8 if columns8 is not None else set()
        self.columns10 = columns10 if columns10 is not None else set()
        self.columns12 = columns12 if columns12 is not None else set()
        self.columns15 = columns15
        self.relational_Column = relational_Column
        self.Column = Column
        self.Column36 = Column36
        self.Column65 = Column65
        self.Column76 = Column76
        self.Column100 = Column100
        
        pass
    @property
    def fixedLength(self):
        return self.__fixedLength

    @fixedLength.setter
    def fixedLength(self, fixedLength: bool):
        self.__fixedLength = fixedLength


    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency: bool):
        self.__currency = currency


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


    @property
    def updateable(self):
        return self.__updateable

    @updateable.setter
    def updateable(self, updateable: bool):
        self.__updateable = updateable


    @property
    def minimumValue(self):
        return self.__minimumValue

    @minimumValue.setter
    def minimumValue(self, minimumValue: str):
        self.__minimumValue = minimumValue


    @property
    def searchability(self):
        return self.__searchability

    @searchability.setter
    def searchability(self, searchability: str):
        self.__searchability = searchability


    @property
    def distinctValueCount(self):
        return self.__distinctValueCount

    @distinctValueCount.setter
    def distinctValueCount(self, distinctValueCount: int):
        self.__distinctValueCount = distinctValueCount


    @property
    def radix(self):
        return self.__radix

    @radix.setter
    def radix(self, radix: int):
        self.__radix = radix


    @property
    def collationName(self):
        return self.__collationName

    @collationName.setter
    def collationName(self, collationName: str):
        self.__collationName = collationName


    @property
    def selectable(self):
        return self.__selectable

    @selectable.setter
    def selectable(self, selectable: bool):
        self.__selectable = selectable


    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: str):
        self.__nullable = nullable


    @property
    def autoIncremented(self):
        return self.__autoIncremented

    @autoIncremented.setter
    def autoIncremented(self, autoIncremented: bool):
        self.__autoIncremented = autoIncremented


    @property
    def nativeType(self):
        return self.__nativeType

    @nativeType.setter
    def nativeType(self, nativeType: str):
        self.__nativeType = nativeType


    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format


    @property
    def signed(self):
        return self.__signed

    @signed.setter
    def signed(self, signed: bool):
        self.__signed = signed


    @property
    def caseSensitive(self):
        return self.__caseSensitive

    @caseSensitive.setter
    def caseSensitive(self, caseSensitive: bool):
        self.__caseSensitive = caseSensitive


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def nullValueCount(self):
        return self.__nullValueCount

    @nullValueCount.setter
    def nullValueCount(self, nullValueCount: int):
        self.__nullValueCount = nullValueCount


    @property
    def characterSetName(self):
        return self.__characterSetName

    @characterSetName.setter
    def characterSetName(self, characterSetName: str):
        self.__characterSetName = characterSetName


    @property
    def maximumValue(self):
        return self.__maximumValue

    @maximumValue.setter
    def maximumValue(self, maximumValue: str):
        self.__maximumValue = maximumValue


    @property
    def Column36(self):
        return self.__Column36

    @Column36.setter
    def Column36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__Column36", None)
        self.__Column36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uniqueKeys"):
                opp_val = getattr(old_value, "uniqueKeys", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uniqueKeys"):
                opp_val = getattr(value, "uniqueKeys", None)
                if opp_val is None:
                    setattr(value, "uniqueKeys", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column100(self):
        return self.__Column100

    @Column100.setter
    def Column100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__Column100", None)
        self.__Column100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relational_Column(self):
        return self.__relational_Column

    @relational_Column.setter
    def relational_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__relational_Column", None)
        self.__relational_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_EObject"):
                opp_val = getattr(old_value, "relational_EObject", None)
                if opp_val == self:
                    setattr(old_value, "relational_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_EObject"):
                opp_val = getattr(value, "relational_EObject", None)
                setattr(value, "relational_EObject", self)

    @property
    def columns15(self):
        return self.__columns15

    @columns15.setter
    def columns15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__columns15", None)
        self.__columns15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColumnSet"):
                opp_val = getattr(old_value, "ColumnSet", None)
                if opp_val == self:
                    setattr(old_value, "ColumnSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColumnSet"):
                opp_val = getattr(value, "ColumnSet", None)
                setattr(value, "ColumnSet", self)

    @property
    def Column76(self):
        return self.__Column76

    @Column76.setter
    def Column76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__Column76", None)
        self.__Column76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accessPatterns"):
                opp_val = getattr(old_value, "accessPatterns", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accessPatterns"):
                opp_val = getattr(value, "accessPatterns", None)
                if opp_val is None:
                    setattr(value, "accessPatterns", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column65(self):
        return self.__Column65

    @Column65.setter
    def Column65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__Column65", None)
        self.__Column65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "indexes64"):
                opp_val = getattr(old_value, "indexes64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "indexes64"):
                opp_val = getattr(value, "indexes64", None)
                if opp_val is None:
                    setattr(value, "indexes64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def columns8(self):
        return self.__columns8

    @columns8.setter
    def columns8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__columns8", None)
        self.__columns8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Index"):
                    opp_val = getattr(item, "Index", None)
                    
                    if opp_val == self:
                        setattr(item, "Index", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Index"):
                    opp_val = getattr(item, "Index", None)
                    
                    setattr(item, "Index", self)
                    

    @property
    def columns12(self):
        return self.__columns12

    @columns12.setter
    def columns12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__columns12", None)
        self.__columns12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AccessPattern13"):
                    opp_val = getattr(item, "AccessPattern13", None)
                    
                    if opp_val == self:
                        setattr(item, "AccessPattern13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AccessPattern13"):
                    opp_val = getattr(item, "AccessPattern13", None)
                    
                    setattr(item, "AccessPattern13", self)
                    

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__columns", None)
        self.__columns = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UniqueKey"):
                    opp_val = getattr(item, "UniqueKey", None)
                    
                    if opp_val == self:
                        setattr(item, "UniqueKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UniqueKey"):
                    opp_val = getattr(item, "UniqueKey", None)
                    
                    setattr(item, "UniqueKey", self)
                    

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foreignKeys"):
                opp_val = getattr(old_value, "foreignKeys", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foreignKeys"):
                opp_val = getattr(value, "foreignKeys", None)
                if opp_val is None:
                    setattr(value, "foreignKeys", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def columns10(self):
        return self.__columns10

    @columns10.setter
    def columns10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Column__columns10", None)
        self.__columns10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey"):
                    opp_val = getattr(item, "ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey"):
                    opp_val = getattr(item, "ForeignKey", None)
                    
                    setattr(item, "ForeignKey", self)
                    

class relational_LogicalRelationshipEnd(RelationalEntity):

    def __init__(self, multiplicity: str, LogicalRelationshipEnd: "relational_Table" = None, LogicalRelationshipEnd86: "relational_LogicalRelationship" = None, logicalRelationships88: "relational_Table" = None, ends: "relational_LogicalRelationship" = None):
        self.multiplicity = multiplicity
        self.LogicalRelationshipEnd = LogicalRelationshipEnd
        self.LogicalRelationshipEnd86 = LogicalRelationshipEnd86
        self.logicalRelationships88 = logicalRelationships88
        self.ends = ends
        
        pass
    @property
    def multiplicity(self):
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: str):
        self.__multiplicity = multiplicity


    @property
    def LogicalRelationshipEnd(self):
        return self.__LogicalRelationshipEnd

    @LogicalRelationshipEnd.setter
    def LogicalRelationshipEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_LogicalRelationshipEnd__LogicalRelationshipEnd", None)
        self.__LogicalRelationshipEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table5"):
                opp_val = getattr(old_value, "table5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table5"):
                opp_val = getattr(value, "table5", None)
                if opp_val is None:
                    setattr(value, "table5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def LogicalRelationshipEnd86(self):
        return self.__LogicalRelationshipEnd86

    @LogicalRelationshipEnd86.setter
    def LogicalRelationshipEnd86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_LogicalRelationshipEnd__LogicalRelationshipEnd86", None)
        self.__LogicalRelationshipEnd86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship"):
                opp_val = getattr(old_value, "relationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship"):
                opp_val = getattr(value, "relationship", None)
                if opp_val is None:
                    setattr(value, "relationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def logicalRelationships88(self):
        return self.__logicalRelationships88

    @logicalRelationships88.setter
    def logicalRelationships88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_LogicalRelationshipEnd__logicalRelationships88", None)
        self.__logicalRelationships88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table89"):
                opp_val = getattr(old_value, "Table89", None)
                if opp_val == self:
                    setattr(old_value, "Table89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table89"):
                opp_val = getattr(value, "Table89", None)
                setattr(value, "Table89", self)

    @property
    def ends(self):
        return self.__ends

    @ends.setter
    def ends(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_LogicalRelationshipEnd__ends", None)
        self.__ends = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LogicalRelationship91"):
                opp_val = getattr(old_value, "LogicalRelationship91", None)
                if opp_val == self:
                    setattr(old_value, "LogicalRelationship91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogicalRelationship91"):
                opp_val = getattr(value, "LogicalRelationship91", None)
                setattr(value, "LogicalRelationship91", self)

class relational_Catalog(RelationalEntity):

    pass
class relational_AccessPattern(RelationalEntity):

    pass
class relational_Schema(RelationalEntity):

    pass
class ColumnSet:

    pass
class relational_ProcedureResult(ColumnSet):

    pass
class relational_Table(ColumnSet):

    def __init__(self, system: bool, cardinality: int, supportsUpdate: bool, materialized: bool, tables: "relational_Schema" = None, table: set["relational_AccessPattern"] = None, tables3: "relational_Catalog" = None, table5: set["relational_LogicalRelationshipEnd"] = None, Table: "relational_Schema" = None, Table89: "relational_LogicalRelationshipEnd" = None, Table79: "relational_AccessPattern" = None, Table49: "relational_Catalog" = None):
        self.system = system
        self.cardinality = cardinality
        self.supportsUpdate = supportsUpdate
        self.materialized = materialized
        self.tables = tables
        self.table = table if table is not None else set()
        self.tables3 = tables3
        self.table5 = table5 if table5 is not None else set()
        self.Table = Table
        self.Table89 = Table89
        self.Table79 = Table79
        self.Table49 = Table49
        
        pass
    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: int):
        self.__cardinality = cardinality


    @property
    def materialized(self):
        return self.__materialized

    @materialized.setter
    def materialized(self, materialized: bool):
        self.__materialized = materialized


    @property
    def supportsUpdate(self):
        return self.__supportsUpdate

    @supportsUpdate.setter
    def supportsUpdate(self, supportsUpdate: bool):
        self.__supportsUpdate = supportsUpdate


    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system: bool):
        self.__system = system


    @property
    def Table79(self):
        return self.__Table79

    @Table79.setter
    def Table79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__Table79", None)
        self.__Table79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accessPatterns78"):
                opp_val = getattr(old_value, "accessPatterns78", None)
                if opp_val == self:
                    setattr(old_value, "accessPatterns78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accessPatterns78"):
                opp_val = getattr(value, "accessPatterns78", None)
                setattr(value, "accessPatterns78", self)

    @property
    def tables3(self):
        return self.__tables3

    @tables3.setter
    def tables3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__tables3", None)
        self.__tables3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Catalog"):
                opp_val = getattr(old_value, "Catalog", None)
                if opp_val == self:
                    setattr(old_value, "Catalog", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Catalog"):
                opp_val = getattr(value, "Catalog", None)
                setattr(value, "Catalog", self)

    @property
    def Table89(self):
        return self.__Table89

    @Table89.setter
    def Table89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__Table89", None)
        self.__Table89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "logicalRelationships88"):
                opp_val = getattr(old_value, "logicalRelationships88", None)
                if opp_val == self:
                    setattr(old_value, "logicalRelationships88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logicalRelationships88"):
                opp_val = getattr(value, "logicalRelationships88", None)
                setattr(value, "logicalRelationships88", self)

    @property
    def table5(self):
        return self.__table5

    @table5.setter
    def table5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__table5", None)
        self.__table5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LogicalRelationshipEnd"):
                    opp_val = getattr(item, "LogicalRelationshipEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "LogicalRelationshipEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LogicalRelationshipEnd"):
                    opp_val = getattr(item, "LogicalRelationshipEnd", None)
                    
                    setattr(item, "LogicalRelationshipEnd", self)
                    

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__table", None)
        self.__table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AccessPattern"):
                    opp_val = getattr(item, "AccessPattern", None)
                    
                    if opp_val == self:
                        setattr(item, "AccessPattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AccessPattern"):
                    opp_val = getattr(item, "AccessPattern", None)
                    
                    setattr(item, "AccessPattern", self)
                    

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__Table", None)
        self.__Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema"):
                opp_val = getattr(old_value, "schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema"):
                opp_val = getattr(value, "schema", None)
                if opp_val is None:
                    setattr(value, "schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__tables", None)
        self.__tables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema"):
                opp_val = getattr(old_value, "Schema", None)
                if opp_val == self:
                    setattr(old_value, "Schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema"):
                opp_val = getattr(value, "Schema", None)
                setattr(value, "Schema", self)

    @property
    def Table49(self):
        return self.__Table49

    @Table49.setter
    def Table49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relational_Table__Table49", None)
        self.__Table49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "catalog48"):
                opp_val = getattr(old_value, "catalog48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "catalog48"):
                opp_val = getattr(value, "catalog48", None)
                if opp_val is None:
                    setattr(value, "catalog48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
