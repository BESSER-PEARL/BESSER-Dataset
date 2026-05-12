from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActionTimeType(Enum):
    AFTER = "AFTER"
    BEFORE = "BEFORE"
    INSTEADOF = "INSTEADOF"
class CheckType(Enum):
    CASCADED = "CASCADED"
    LOCAL = "LOCAL"
    NONE = "NONE"
class IntegrityControlOption(Enum):
    ALL = "ALL"
    SELECTIVE = "SELECTIVE"
    NONE = "NONE"
class GenerateType(Enum):
    DEFAULT_GENERATED = "DEFAULT_GENERATED"
    ALWAYS_GENERATED = "ALWAYS_GENERATED"
class OrderingType(Enum):
    EQUALS = "EQUALS"
    FULL = "FULL"
class LinkControlOption(Enum):
    FILE_LINK_CONTROL = "FILE_LINK_CONTROL"
    NO_FILE_LINK_CONTROL = "NO_FILE_LINK_CONTROL"
class PrimitiveType(Enum):
    CHARACTER = "CHARACTER"
    BINARY_LARGE_OBJECT = "BINARY_LARGE_OBJECT"
    NUMERIC = "NUMERIC"
    DECIMAL = "DECIMAL"
    SMALLINT = "SMALLINT"
    INTEGER = "INTEGER"
    BIGINT = "BIGINT"
    FLOAT = "FLOAT"
    REAL = "REAL"
    DOUBLE_PRECISION = "DOUBLE_PRECISION"
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    TIME = "TIME"
    TIMESTAMP = "TIMESTAMP"
    INTERVAL = "INTERVAL"
    DATALINK = "DATALINK"
    XML_TYPE = "XML_TYPE"
    CHARACTER_VARYING = "CHARACTER_VARYING"
    CHARACTER_LARGE_OBJECT = "CHARACTER_LARGE_OBJECT"
    NATIONAL_CHARACTER = "NATIONAL_CHARACTER"
    NATIONAL_CHARACTER_VARYING = "NATIONAL_CHARACTER_VARYING"
    NATIONAL_CHARACTER_LARGE_OBJECT = "NATIONAL_CHARACTER_LARGE_OBJECT"
    BINARY = "BINARY"
    BINARY_VARYING = "BINARY_VARYING"
class WritePermissionOption(Enum):
    FS = "FS"
    ADMIN = "ADMIN"
    BLOCKED = "BLOCKED"
class ParameterMode(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class OrderingCategoryType(Enum):
    RELATIVE = "RELATIVE"
    MAP = "MAP"
    STATE = "STATE"
class DataAccess(Enum):
    NO_SQL = "NO_SQL"
    CONTAINS_SQL = "CONTAINS_SQL"
    READS_SQL_DATA = "READS_SQL_DATA"
    MODIFIES_SQL_DATA = "MODIFIES_SQL_DATA"
class ReferentialActionType(Enum):
    NO_ACTION = "NO_ACTION"
    RESTRICT = "RESTRICT"
    CASCADE = "CASCADE"
    SET_NULL = "SET_NULL"
    SET_DEFAULT = "SET_DEFAULT"
class IncrementType(Enum):
    ASC = "ASC"
    DESC = "DESC"
    RANDOM = "RANDOM"
class ReadPermissionOption(Enum):
    DB = "DB"
    FS = "FS"
class UnlinkOption(Enum):
    RESTORE = "RESTORE"
    DELETE = "DELETE"
    NONE = "NONE"
class ReferenceType(Enum):
    SYSTEM_GENERATED = "SYSTEM_GENERATED"
    USER_GENERATED = "USER_GENERATED"
    DERIVED_SELF_REF = "DERIVED_SELF_REF"
class MatchType(Enum):
    MATCH_SIMPLE = "MATCH_SIMPLE"
    MATCH_FULL = "MATCH_FULL"
    MATCH_PARTIAL = "MATCH_PARTIAL"
class CoercibilityType(Enum):
    IMPLICIT = "IMPLICIT"
    EXPLICIT = "EXPLICIT"
    COERCIBILE = "COERCIBILE"
    NO_COLLATION = "NO_COLLATION"
class ActionGranularityType(Enum):
    STATEMENT = "STATEMENT"
    ROW = "ROW"
class IntervalQualifierType(Enum):
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"
    SECOND = "SECOND"
    FRACTION = "FRACTION"
    YEAR = "YEAR"
    MONTH = "MONTH"


############################################
# Definition of Classes
############################################

class Group:

    pass
class User:

    pass
class Role:

    pass
class RoleAuthorization:

    pass
class ValueExpression:

    pass
class QueryExpression:

    pass
class DerivedTable:

    pass
class sqlmodel_tables_ViewTable(DerivedTable):

    def __init__(self, checkType: str):
        self.checkType = checkType
        
        pass
    @property
    def checkType(self):
        return self.__checkType

    @checkType.setter
    def checkType(self, checkType: str):
        self.__checkType = checkType


class statements_SQLStatement:

    pass
class SQLDataStatement:

    pass
class sqlmodel_statements_SQLDataChangeStatement(SQLDataStatement):

    pass
class SQLStatement:

    pass
class sqlmodel_statements_SQLConnectionStatement(SQLStatement):

    pass
class sqlmodel_statements_SQLDynamicStatement(SQLStatement):

    pass
class sqlmodel_statements_SQLDiagnosticsStatement(SQLStatement):

    pass
class sqlmodel_statements_SQLControlStatement(SQLStatement):

    pass
class sqlmodel_statements_SQLSessionStatement(SQLStatement):

    pass
class sqlmodel_statements_SQLSchemaStatement(SQLStatement):

    pass
class sqlmodel_statements_SQLTransactionStatement(SQLStatement):

    pass
class sqlmodel_statements_SQLDataStatement(SQLStatement):

    pass
class sqlmodel_statements_SQLStatement(ABC):

    def __init__(self):
        
        pass
    def getSQL(self) :
        # TODO: Implement getSQL method
        pass

    def setSQL(self, sqlmodel_sqlText):
        # TODO: Implement setSQL method
        pass

class Function:

    pass
class sqlmodel_routines_BuiltInFunction(Function):

    pass
class sqlmodel_routines_UserDefinedFunction(Function):

    pass
class sqlmodel_routines_Method(Function):

    def __init__(self, overriding: bool, constructor: bool):
        self.overriding = overriding
        self.constructor = constructor
        
        pass
    @property
    def constructor(self):
        return self.__constructor

    @constructor.setter
    def constructor(self, constructor: bool):
        self.__constructor = constructor


    @property
    def overriding(self):
        return self.__overriding

    @overriding.setter
    def overriding(self, overriding: bool):
        self.__overriding = overriding


class RoutineResultTable:

    pass
class Source:

    pass
class Parameter:

    pass
class expressions_SearchCondition:

    pass
class expressions_ValueExpression:

    pass
class sqlmodel_expressions_QueryExpression(ABC):

    def __init__(self):
        
        pass
    def getSQL(self) :
        # TODO: Implement getSQL method
        pass

    def setSQL(self, sqlmodel_sqlText):
        # TODO: Implement setSQL method
        pass

class expressions_QueryExpression:

    pass
class schema_SQLObject:

    pass
class sqlmodel_expressions_SearchConditionDefault(expressions_SearchCondition, schema_SQLObject):

    def __init__(self, SQL: str):
        self.SQL = SQL
        
        pass
    @property
    def SQL(self):
        return self.__SQL

    @SQL.setter
    def SQL(self, SQL: str):
        self.__SQL = SQL


class sqlmodel_statements_SQLStatementDefault(statements_SQLStatement, schema_SQLObject):

    def __init__(self, SQL: str):
        self.SQL = SQL
        
        pass
    @property
    def SQL(self):
        return self.__SQL

    @SQL.setter
    def SQL(self, SQL: str):
        self.__SQL = SQL


class sqlmodel_expressions_ValueExpressionDefault(expressions_ValueExpression, schema_SQLObject):

    def __init__(self, SQL: str):
        self.SQL = SQL
        
        pass
    @property
    def SQL(self):
        return self.__SQL

    @SQL.setter
    def SQL(self, SQL: str):
        self.__SQL = SQL


class sqlmodel_expressions_QueryExpressionDefault(expressions_QueryExpression, schema_SQLObject):

    def __init__(self, SQL: str):
        self.SQL = SQL
        
        pass
    @property
    def SQL(self):
        return self.__SQL

    @SQL.setter
    def SQL(self, SQL: str):
        self.__SQL = SQL


class sqlmodel_expressions_SearchCondition(ABC):

    def __init__(self):
        
        pass
    def setSQL(self, sqlmodel_sqlText):
        # TODO: Implement setSQL method
        pass

    def getSQL(self) :
        # TODO: Implement getSQL method
        pass

class sqlmodel_expressions_ValueExpression(ABC):

    def __init__(self):
        
        pass
    def setSQL(self, sqlmodel_sqlText):
        # TODO: Implement setSQL method
        pass

    def getSQL(self) :
        # TODO: Implement getSQL method
        pass

class NumericalDataType:

    pass
class sqlmodel_datatypes_ApproximateNumericDataType(NumericalDataType):

    pass
class sqlmodel_datatypes_ExactNumericDataType(NumericalDataType):

    def __init__(self, scale: int):
        self.scale = scale
        
        pass
    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale


class CheckConstraint:

    pass
class DistinctUserDefinedType:

    pass
class sqlmodel_datatypes_Domain(DistinctUserDefinedType):

    def __init__(self, defaultValue: str, sqlmodel_datatypes_Domain: set["CheckConstraint"] = None):
        self.defaultValue = defaultValue
        self.sqlmodel_datatypes_Domain = sqlmodel_datatypes_Domain if sqlmodel_datatypes_Domain is not None else set()
        
        pass
    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def sqlmodel_datatypes_Domain(self):
        return self.__sqlmodel_datatypes_Domain

    @sqlmodel_datatypes_Domain.setter
    def sqlmodel_datatypes_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_datatypes_Domain__sqlmodel_datatypes_Domain", None)
        self.__sqlmodel_datatypes_Domain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CheckConstraint"):
                    opp_val = getattr(item, "CheckConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "CheckConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CheckConstraint"):
                    opp_val = getattr(item, "CheckConstraint", None)
                    
                    setattr(item, "CheckConstraint", self)
                    

class ExactNumericDataType:

    pass
class sqlmodel_datatypes_IntegerDataType(ExactNumericDataType):

    pass
class sqlmodel_datatypes_FixedPrecisionDataType(ExactNumericDataType):

    pass
class StructuredUserDefinedType:

    pass
class Method:

    pass
class AttributeDefinition:

    pass
class CharacterStringDataType:

    pass
class CollectionDataType:

    pass
class sqlmodel_datatypes_MultisetDataType(CollectionDataType):

    pass
class sqlmodel_datatypes_ArrayDataType(CollectionDataType):

    def __init__(self, maxCardinality: int, CollectionDataType113: "sqlmodel_datatypes_ElementType" = None):
        self.maxCardinality = maxCardinality
        
        pass
    @property
    def maxCardinality(self):
        return self.__maxCardinality

    @maxCardinality.setter
    def maxCardinality(self, maxCardinality: int):
        self.__maxCardinality = maxCardinality


class Field:

    pass
class PredefinedDataType:

    pass
class sqlmodel_datatypes_IntervalDataType(PredefinedDataType):

    def __init__(self, leadingQualifier: str, trailingQualifier: str, leadingFieldPrecision: int, trailingFieldPrecision: int, fractionalSecondsPrecision: int, PredefinedDataType: "sqlmodel_datatypes_DistinctUserDefinedType" = None):
        self.leadingQualifier = leadingQualifier
        self.trailingQualifier = trailingQualifier
        self.leadingFieldPrecision = leadingFieldPrecision
        self.trailingFieldPrecision = trailingFieldPrecision
        self.fractionalSecondsPrecision = fractionalSecondsPrecision
        
        pass
    @property
    def trailingQualifier(self):
        return self.__trailingQualifier

    @trailingQualifier.setter
    def trailingQualifier(self, trailingQualifier: str):
        self.__trailingQualifier = trailingQualifier


    @property
    def leadingFieldPrecision(self):
        return self.__leadingFieldPrecision

    @leadingFieldPrecision.setter
    def leadingFieldPrecision(self, leadingFieldPrecision: int):
        self.__leadingFieldPrecision = leadingFieldPrecision


    @property
    def fractionalSecondsPrecision(self):
        return self.__fractionalSecondsPrecision

    @fractionalSecondsPrecision.setter
    def fractionalSecondsPrecision(self, fractionalSecondsPrecision: int):
        self.__fractionalSecondsPrecision = fractionalSecondsPrecision


    @property
    def leadingQualifier(self):
        return self.__leadingQualifier

    @leadingQualifier.setter
    def leadingQualifier(self, leadingQualifier: str):
        self.__leadingQualifier = leadingQualifier


    @property
    def trailingFieldPrecision(self):
        return self.__trailingFieldPrecision

    @trailingFieldPrecision.setter
    def trailingFieldPrecision(self, trailingFieldPrecision: int):
        self.__trailingFieldPrecision = trailingFieldPrecision


class sqlmodel_datatypes_CharacterStringDataType(PredefinedDataType):

    def __init__(self, length: int, coercibility: str, fixedLength: bool, collationName: str, CharacterStringDataType: "CharacterSet" = None, PredefinedDataType: "sqlmodel_datatypes_DistinctUserDefinedType" = None):
        self.length = length
        self.coercibility = coercibility
        self.fixedLength = fixedLength
        self.collationName = collationName
        self.CharacterStringDataType = CharacterStringDataType
        
        pass
    @property
    def fixedLength(self):
        return self.__fixedLength

    @fixedLength.setter
    def fixedLength(self, fixedLength: bool):
        self.__fixedLength = fixedLength


    @property
    def collationName(self):
        return self.__collationName

    @collationName.setter
    def collationName(self, collationName: str):
        self.__collationName = collationName


    @property
    def coercibility(self):
        return self.__coercibility

    @coercibility.setter
    def coercibility(self, coercibility: str):
        self.__coercibility = coercibility


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


    @property
    def CharacterStringDataType(self):
        return self.__CharacterStringDataType

    @CharacterStringDataType.setter
    def CharacterStringDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_datatypes_CharacterStringDataType__CharacterStringDataType", None)
        self.__CharacterStringDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CharacterSet91"):
                opp_val = getattr(old_value, "CharacterSet91", None)
                if opp_val == self:
                    setattr(old_value, "CharacterSet91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CharacterSet91"):
                opp_val = getattr(value, "CharacterSet91", None)
                setattr(value, "CharacterSet91", self)

class sqlmodel_datatypes_DateDataType(PredefinedDataType):

    pass
class sqlmodel_datatypes_TimeDataType(PredefinedDataType):

    def __init__(self, fractionalSecondsPrecision: int, timeZone: bool, PredefinedDataType: "sqlmodel_datatypes_DistinctUserDefinedType" = None):
        self.fractionalSecondsPrecision = fractionalSecondsPrecision
        self.timeZone = timeZone
        
        pass
    @property
    def timeZone(self):
        return self.__timeZone

    @timeZone.setter
    def timeZone(self, timeZone: bool):
        self.__timeZone = timeZone


    @property
    def fractionalSecondsPrecision(self):
        return self.__fractionalSecondsPrecision

    @fractionalSecondsPrecision.setter
    def fractionalSecondsPrecision(self, fractionalSecondsPrecision: int):
        self.__fractionalSecondsPrecision = fractionalSecondsPrecision


class sqlmodel_datatypes_XMLDataType(PredefinedDataType):

    pass
class sqlmodel_datatypes_BinaryStringDataType(PredefinedDataType):

    def __init__(self, length: int, PredefinedDataType: "sqlmodel_datatypes_DistinctUserDefinedType" = None):
        self.length = length
        
        pass
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


    def equals(self) :
        # TODO: Implement equals method
        pass

class sqlmodel_datatypes_BooleanDataType(PredefinedDataType):

    pass
class sqlmodel_datatypes_DataLinkDataType(PredefinedDataType):

    def __init__(self, length: int, linkControl: str, integrityControl: str, readPermission: str, writePermission: str, recovery: bool, unlink: str, PredefinedDataType: "sqlmodel_datatypes_DistinctUserDefinedType" = None):
        self.length = length
        self.linkControl = linkControl
        self.integrityControl = integrityControl
        self.readPermission = readPermission
        self.writePermission = writePermission
        self.recovery = recovery
        self.unlink = unlink
        
        pass
    @property
    def readPermission(self):
        return self.__readPermission

    @readPermission.setter
    def readPermission(self, readPermission: str):
        self.__readPermission = readPermission


    @property
    def integrityControl(self):
        return self.__integrityControl

    @integrityControl.setter
    def integrityControl(self, integrityControl: str):
        self.__integrityControl = integrityControl


    @property
    def linkControl(self):
        return self.__linkControl

    @linkControl.setter
    def linkControl(self, linkControl: str):
        self.__linkControl = linkControl


    @property
    def unlink(self):
        return self.__unlink

    @unlink.setter
    def unlink(self, unlink: str):
        self.__unlink = unlink


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


    @property
    def writePermission(self):
        return self.__writePermission

    @writePermission.setter
    def writePermission(self, writePermission: str):
        self.__writePermission = writePermission


    @property
    def recovery(self):
        return self.__recovery

    @recovery.setter
    def recovery(self, recovery: bool):
        self.__recovery = recovery


class sqlmodel_datatypes_NumericalDataType(PredefinedDataType):

    def __init__(self, precision: int, PredefinedDataType: "sqlmodel_datatypes_DistinctUserDefinedType" = None):
        self.precision = precision
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision


class ElementType:

    pass
class ConstructedDataType:

    pass
class sqlmodel_datatypes_RowDataType(ConstructedDataType):

    pass
class sqlmodel_datatypes_ReferenceDataType(ConstructedDataType):

    pass
class sqlmodel_datatypes_CollectionDataType(ConstructedDataType):

    pass
class IndexExpression:

    pass
class UserDefinedTypeOrdering:

    pass
class DataType:

    pass
class sqlmodel_datatypes_ConstructedDataType(DataType):

    pass
class sqlmodel_datatypes_SQLDataType(DataType):

    pass
class sqlmodel_datatypes_UserDefinedType(DataType):

    pass
class IndexMember:

    pass
class ForeignKey:

    pass
class UniqueConstraint:

    pass
class sqlmodel_constraints_PrimaryKey(UniqueConstraint):

    pass
class ReferenceConstraint:

    pass
class sqlmodel_constraints_UniqueConstraint(ReferenceConstraint):

    def __init__(self, clustered: bool, uniqueConstraint: set["ForeignKey"] = None):
        self.clustered = clustered
        self.uniqueConstraint = uniqueConstraint if uniqueConstraint is not None else set()
        
        pass
    @property
    def clustered(self):
        return self.__clustered

    @clustered.setter
    def clustered(self, clustered: bool):
        self.__clustered = clustered


    @property
    def uniqueConstraint(self):
        return self.__uniqueConstraint

    @uniqueConstraint.setter
    def uniqueConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_UniqueConstraint__uniqueConstraint", None)
        self.__uniqueConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey71"):
                    opp_val = getattr(item, "ForeignKey71", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey71"):
                    opp_val = getattr(item, "ForeignKey71", None)
                    
                    setattr(item, "ForeignKey71", self)
                    

class sqlmodel_constraints_ForeignKey(ReferenceConstraint):

    def __init__(self, match: str, onUpdate: str, onDelete: str, ForeignKey: "UniqueConstraint" = None, ForeignKey66: "Index" = None, referencingForeignKeys: "BaseTable" = None, sqlmodel_constraints_ForeignKey: set["Column"] = None):
        self.match = match
        self.onUpdate = onUpdate
        self.onDelete = onDelete
        self.ForeignKey = ForeignKey
        self.ForeignKey66 = ForeignKey66
        self.referencingForeignKeys = referencingForeignKeys
        self.sqlmodel_constraints_ForeignKey = sqlmodel_constraints_ForeignKey if sqlmodel_constraints_ForeignKey is not None else set()
        
        pass
    @property
    def onUpdate(self):
        return self.__onUpdate

    @onUpdate.setter
    def onUpdate(self, onUpdate: str):
        self.__onUpdate = onUpdate


    @property
    def onDelete(self):
        return self.__onDelete

    @onDelete.setter
    def onDelete(self, onDelete: str):
        self.__onDelete = onDelete


    @property
    def match(self):
        return self.__match

    @match.setter
    def match(self, match: str):
        self.__match = match


    @property
    def ForeignKey(self):
        return self.__ForeignKey

    @ForeignKey.setter
    def ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_ForeignKey__ForeignKey", None)
        self.__ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UniqueConstraint"):
                opp_val = getattr(old_value, "UniqueConstraint", None)
                if opp_val == self:
                    setattr(old_value, "UniqueConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UniqueConstraint"):
                opp_val = getattr(value, "UniqueConstraint", None)
                setattr(value, "UniqueConstraint", self)

    @property
    def ForeignKey66(self):
        return self.__ForeignKey66

    @ForeignKey66.setter
    def ForeignKey66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_ForeignKey__ForeignKey66", None)
        self.__ForeignKey66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Index67"):
                opp_val = getattr(old_value, "Index67", None)
                if opp_val == self:
                    setattr(old_value, "Index67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Index67"):
                opp_val = getattr(value, "Index67", None)
                setattr(value, "Index67", self)

    @property
    def sqlmodel_constraints_ForeignKey(self):
        return self.__sqlmodel_constraints_ForeignKey

    @sqlmodel_constraints_ForeignKey.setter
    def sqlmodel_constraints_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_ForeignKey__sqlmodel_constraints_ForeignKey", None)
        self.__sqlmodel_constraints_ForeignKey = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column64"):
                    opp_val = getattr(item, "Column64", None)
                    
                    if opp_val == self:
                        setattr(item, "Column64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column64"):
                    opp_val = getattr(item, "Column64", None)
                    
                    setattr(item, "Column64", self)
                    

    @property
    def referencingForeignKeys(self):
        return self.__referencingForeignKeys

    @referencingForeignKeys.setter
    def referencingForeignKeys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_ForeignKey__referencingForeignKeys", None)
        self.__referencingForeignKeys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BaseTable69"):
                opp_val = getattr(old_value, "BaseTable69", None)
                if opp_val == self:
                    setattr(old_value, "BaseTable69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BaseTable69"):
                opp_val = getattr(value, "BaseTable69", None)
                setattr(value, "BaseTable69", self)

class Column:

    pass
class TableConstraint:

    pass
class sqlmodel_constraints_CheckConstraint(TableConstraint):

    pass
class sqlmodel_constraints_ReferenceConstraint(TableConstraint):

    pass
class SearchCondition:

    pass
class Constraint:

    pass
class sqlmodel_constraints_TableConstraint(Constraint):

    pass
class sqlmodel_constraints_Assertion(Constraint):

    pass
class BaseTable:

    pass
class sqlmodel_tables_PersistentTable(BaseTable):

    pass
class sqlmodel_tables_TemporaryTable(BaseTable):

    def __init__(self, local: bool, deleteOnCommit: bool, BaseTable58: "sqlmodel_constraints_TableConstraint" = None, BaseTable69: "sqlmodel_constraints_ForeignKey" = None, BaseTable: "sqlmodel_constraints_Assertion" = None):
        self.local = local
        self.deleteOnCommit = deleteOnCommit
        
        pass
    @property
    def deleteOnCommit(self):
        return self.__deleteOnCommit

    @deleteOnCommit.setter
    def deleteOnCommit(self, deleteOnCommit: bool):
        self.__deleteOnCommit = deleteOnCommit


    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local: bool):
        self.__local = local


class sqlmodel_schema_Comment:

    def __init__(self, description: str, comments: "SQLObject" = None):
        self.description = description
        self.comments = comments
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_Comment__comments", None)
        self.__comments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQLObject44"):
                opp_val = getattr(old_value, "SQLObject44", None)
                if opp_val == self:
                    setattr(old_value, "SQLObject44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQLObject44"):
                opp_val = getattr(value, "SQLObject44", None)
                setattr(value, "SQLObject44", self)

class sqlmodel_schema_ObjectExtension(ABC):

    pass
class Event:

    pass
class IdentitySpecifier:

    pass
class TypedElement:

    pass
class sqlmodel_tables_Column(TypedElement):

    def __init__(self, implementationDependent: bool, nullable: bool, defaultValue: str, scopeCheck: str, scopeChecked: bool, columns: "Table" = None, sqlmodel_tables_Column: "IdentitySpecifier" = None, sqlmodel_tables_Column156: "ValueExpression" = None):
        self.implementationDependent = implementationDependent
        self.nullable = nullable
        self.defaultValue = defaultValue
        self.scopeCheck = scopeCheck
        self.scopeChecked = scopeChecked
        self.columns = columns
        self.sqlmodel_tables_Column = sqlmodel_tables_Column
        self.sqlmodel_tables_Column156 = sqlmodel_tables_Column156
        
        pass
    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def scopeCheck(self):
        return self.__scopeCheck

    @scopeCheck.setter
    def scopeCheck(self, scopeCheck: str):
        self.__scopeCheck = scopeCheck


    @property
    def implementationDependent(self):
        return self.__implementationDependent

    @implementationDependent.setter
    def implementationDependent(self, implementationDependent: bool):
        self.__implementationDependent = implementationDependent


    @property
    def scopeChecked(self):
        return self.__scopeChecked

    @scopeChecked.setter
    def scopeChecked(self, scopeChecked: bool):
        self.__scopeChecked = scopeChecked


    @property
    def sqlmodel_tables_Column(self):
        return self.__sqlmodel_tables_Column

    @sqlmodel_tables_Column.setter
    def sqlmodel_tables_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Column__sqlmodel_tables_Column", None)
        self.__sqlmodel_tables_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IdentitySpecifier154"):
                opp_val = getattr(old_value, "IdentitySpecifier154", None)
                if opp_val == self:
                    setattr(old_value, "IdentitySpecifier154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentitySpecifier154"):
                opp_val = getattr(value, "IdentitySpecifier154", None)
                setattr(value, "IdentitySpecifier154", self)

    @property
    def sqlmodel_tables_Column156(self):
        return self.__sqlmodel_tables_Column156

    @sqlmodel_tables_Column156.setter
    def sqlmodel_tables_Column156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Column__sqlmodel_tables_Column156", None)
        self.__sqlmodel_tables_Column156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpression"):
                opp_val = getattr(old_value, "ValueExpression", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpression"):
                opp_val = getattr(value, "ValueExpression", None)
                setattr(value, "ValueExpression", self)

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Column__columns", None)
        self.__columns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table152"):
                opp_val = getattr(old_value, "Table152", None)
                if opp_val == self:
                    setattr(old_value, "Table152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table152"):
                opp_val = getattr(value, "Table152", None)
                setattr(value, "Table152", self)

    def isPartOfUniqueConstraint(self) :
        # TODO: Implement isPartOfUniqueConstraint method
        pass

    def isPartOfPrimaryKey(self) :
        # TODO: Implement isPartOfPrimaryKey method
        pass

    def isPartOfForeignKey(self) :
        # TODO: Implement isPartOfForeignKey method
        pass

class sqlmodel_routines_Parameter(TypedElement):

    def __init__(self, locator: bool, mode: str, parameters: "Routine" = None, sqlmodel_routines_Parameter: "CharacterStringDataType" = None):
        self.locator = locator
        self.mode = mode
        self.parameters = parameters
        self.sqlmodel_routines_Parameter = sqlmodel_routines_Parameter
        
        pass
    @property
    def locator(self):
        return self.__locator

    @locator.setter
    def locator(self, locator: bool):
        self.__locator = locator


    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def sqlmodel_routines_Parameter(self):
        return self.__sqlmodel_routines_Parameter

    @sqlmodel_routines_Parameter.setter
    def sqlmodel_routines_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_routines_Parameter__sqlmodel_routines_Parameter", None)
        self.__sqlmodel_routines_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CharacterStringDataType121"):
                opp_val = getattr(old_value, "CharacterStringDataType121", None)
                if opp_val == self:
                    setattr(old_value, "CharacterStringDataType121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CharacterStringDataType121"):
                opp_val = getattr(value, "CharacterStringDataType121", None)
                setattr(value, "CharacterStringDataType121", self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_routines_Parameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Routine119"):
                opp_val = getattr(old_value, "Routine119", None)
                if opp_val == self:
                    setattr(old_value, "Routine119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Routine119"):
                opp_val = getattr(value, "Routine119", None)
                setattr(value, "Routine119", self)

class sqlmodel_datatypes_Field(TypedElement):

    def __init__(self, scopeCheck: str, scopeChecked: bool):
        self.scopeCheck = scopeCheck
        self.scopeChecked = scopeChecked
        
        pass
    @property
    def scopeCheck(self):
        return self.__scopeCheck

    @scopeCheck.setter
    def scopeCheck(self, scopeCheck: str):
        self.__scopeCheck = scopeCheck


    @property
    def scopeChecked(self):
        return self.__scopeChecked

    @scopeChecked.setter
    def scopeChecked(self, scopeChecked: bool):
        self.__scopeChecked = scopeChecked


class sqlmodel_datatypes_ElementType(TypedElement):

    pass
class sqlmodel_datatypes_AttributeDefinition(TypedElement):

    def __init__(self, scopeCheck: str, scopeChecked: bool, defaultValue: str):
        self.scopeCheck = scopeCheck
        self.scopeChecked = scopeChecked
        self.defaultValue = defaultValue
        
        pass
    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def scopeChecked(self):
        return self.__scopeChecked

    @scopeChecked.setter
    def scopeChecked(self, scopeChecked: bool):
        self.__scopeChecked = scopeChecked


    @property
    def scopeCheck(self):
        return self.__scopeCheck

    @scopeCheck.setter
    def scopeCheck(self, scopeCheck: str):
        self.__scopeCheck = scopeCheck


class sqlmodel_schema_Sequence(TypedElement):

    pass
class Privilege:

    pass
class Schema:

    pass
class ObjectExtension:

    pass
class Comment:

    pass
class Dependency:

    pass
class CharacterSet:

    pass
class Assertion:

    pass
class Catalog:

    pass
class ENamedElement:

    pass
class sqlmodel_schema_SQLObject(ENamedElement):

    def __init__(self, description: str, label: str, sqlmodel_schema_SQLObject: set["Dependency"] = None, SQLObject: set["Comment"] = None, SQLObject26: set["ObjectExtension"] = None, object: set["Privilege"] = None):
        self.description = description
        self.label = label
        self.sqlmodel_schema_SQLObject = sqlmodel_schema_SQLObject if sqlmodel_schema_SQLObject is not None else set()
        self.SQLObject = SQLObject if SQLObject is not None else set()
        self.SQLObject26 = SQLObject26 if SQLObject26 is not None else set()
        self.object = object if object is not None else set()
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def SQLObject(self):
        return self.__SQLObject

    @SQLObject.setter
    def SQLObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_SQLObject__SQLObject", None)
        self.__SQLObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    setattr(item, "Comment", self)
                    

    @property
    def object(self):
        return self.__object

    @object.setter
    def object(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_SQLObject__object", None)
        self.__object = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Privilege"):
                    opp_val = getattr(item, "Privilege", None)
                    
                    if opp_val == self:
                        setattr(item, "Privilege", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Privilege"):
                    opp_val = getattr(item, "Privilege", None)
                    
                    setattr(item, "Privilege", self)
                    

    @property
    def SQLObject26(self):
        return self.__SQLObject26

    @SQLObject26.setter
    def SQLObject26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_SQLObject__SQLObject26", None)
        self.__SQLObject26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ObjectExtension"):
                    opp_val = getattr(item, "ObjectExtension", None)
                    
                    if opp_val == self:
                        setattr(item, "ObjectExtension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ObjectExtension"):
                    opp_val = getattr(item, "ObjectExtension", None)
                    
                    setattr(item, "ObjectExtension", self)
                    

    @property
    def sqlmodel_schema_SQLObject(self):
        return self.__sqlmodel_schema_SQLObject

    @sqlmodel_schema_SQLObject.setter
    def sqlmodel_schema_SQLObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_SQLObject__sqlmodel_schema_SQLObject", None)
        self.__sqlmodel_schema_SQLObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    setattr(item, "Dependency", self)
                    

    def removeEAnnotationDetail(self, sqlmodel_eAnnotation, sqlmodel_key):
        # TODO: Implement removeEAnnotationDetail method
        pass

    def setAnnotationDetail(self, sqlmodel_key, sqlmodel_eAnnotation, sqlmodel_value):
        # TODO: Implement setAnnotationDetail method
        pass

    def getEAnnotationDetail(self, sqlmodel_eAnnotation, sqlmodel_key) :
        # TODO: Implement getEAnnotationDetail method
        pass

    def getEAnnotation(self, sqlmodel_source) :
        # TODO: Implement getEAnnotation method
        pass

    def addEAnnotationDetail(self, sqlmodel_eAnnotation, sqlmodel_key, sqlmodel_value):
        # TODO: Implement addEAnnotationDetail method
        pass

    def addEAnnotation(self, sqlmodel_source) :
        # TODO: Implement addEAnnotation method
        pass

class AuthorizationIdentifier:

    pass
class sqlmodel_accesscontrol_User(AuthorizationIdentifier):

    pass
class sqlmodel_accesscontrol_Group(AuthorizationIdentifier):

    pass
class sqlmodel_accesscontrol_Role(AuthorizationIdentifier):

    pass
class Routine:

    pass
class sqlmodel_routines_Procedure(Routine):

    def __init__(self, maxResultSets: int, oldSavePoint: bool, sqlmodel_routines_Procedure: set["RoutineResultTable"] = None, Routine: "sqlmodel_schema_Schema" = None, Routine119: "sqlmodel_routines_Parameter" = None, Routine111: "sqlmodel_datatypes_UserDefinedTypeOrdering" = None):
        self.maxResultSets = maxResultSets
        self.oldSavePoint = oldSavePoint
        self.sqlmodel_routines_Procedure = sqlmodel_routines_Procedure if sqlmodel_routines_Procedure is not None else set()
        
        pass
    @property
    def maxResultSets(self):
        return self.__maxResultSets

    @maxResultSets.setter
    def maxResultSets(self, maxResultSets: int):
        self.__maxResultSets = maxResultSets


    @property
    def oldSavePoint(self):
        return self.__oldSavePoint

    @oldSavePoint.setter
    def oldSavePoint(self, oldSavePoint: bool):
        self.__oldSavePoint = oldSavePoint


    @property
    def sqlmodel_routines_Procedure(self):
        return self.__sqlmodel_routines_Procedure

    @sqlmodel_routines_Procedure.setter
    def sqlmodel_routines_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_routines_Procedure__sqlmodel_routines_Procedure", None)
        self.__sqlmodel_routines_Procedure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RoutineResultTable"):
                    opp_val = getattr(item, "RoutineResultTable", None)
                    
                    if opp_val == self:
                        setattr(item, "RoutineResultTable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RoutineResultTable"):
                    opp_val = getattr(item, "RoutineResultTable", None)
                    
                    setattr(item, "RoutineResultTable", self)
                    

class sqlmodel_routines_Function(Routine):

    def __init__(self, nullCall: bool, static: bool, transformGroup: str, typePreserving: bool, mutator: bool, sqlmodel_routines_Function: "RoutineResultTable" = None, sqlmodel_routines_Function126: "Parameter" = None, sqlmodel_routines_Function129: "Parameter" = None, Routine: "sqlmodel_schema_Schema" = None, Routine119: "sqlmodel_routines_Parameter" = None, Routine111: "sqlmodel_datatypes_UserDefinedTypeOrdering" = None):
        self.nullCall = nullCall
        self.static = static
        self.transformGroup = transformGroup
        self.typePreserving = typePreserving
        self.mutator = mutator
        self.sqlmodel_routines_Function = sqlmodel_routines_Function
        self.sqlmodel_routines_Function126 = sqlmodel_routines_Function126
        self.sqlmodel_routines_Function129 = sqlmodel_routines_Function129
        
        pass
    @property
    def transformGroup(self):
        return self.__transformGroup

    @transformGroup.setter
    def transformGroup(self, transformGroup: str):
        self.__transformGroup = transformGroup


    @property
    def nullCall(self):
        return self.__nullCall

    @nullCall.setter
    def nullCall(self, nullCall: bool):
        self.__nullCall = nullCall


    @property
    def typePreserving(self):
        return self.__typePreserving

    @typePreserving.setter
    def typePreserving(self, typePreserving: bool):
        self.__typePreserving = typePreserving


    @property
    def mutator(self):
        return self.__mutator

    @mutator.setter
    def mutator(self, mutator: bool):
        self.__mutator = mutator


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def sqlmodel_routines_Function129(self):
        return self.__sqlmodel_routines_Function129

    @sqlmodel_routines_Function129.setter
    def sqlmodel_routines_Function129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_routines_Function__sqlmodel_routines_Function129", None)
        self.__sqlmodel_routines_Function129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter130"):
                opp_val = getattr(old_value, "Parameter130", None)
                if opp_val == self:
                    setattr(old_value, "Parameter130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter130"):
                opp_val = getattr(value, "Parameter130", None)
                setattr(value, "Parameter130", self)

    @property
    def sqlmodel_routines_Function126(self):
        return self.__sqlmodel_routines_Function126

    @sqlmodel_routines_Function126.setter
    def sqlmodel_routines_Function126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_routines_Function__sqlmodel_routines_Function126", None)
        self.__sqlmodel_routines_Function126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter127"):
                opp_val = getattr(old_value, "Parameter127", None)
                if opp_val == self:
                    setattr(old_value, "Parameter127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter127"):
                opp_val = getattr(value, "Parameter127", None)
                setattr(value, "Parameter127", self)

    @property
    def sqlmodel_routines_Function(self):
        return self.__sqlmodel_routines_Function

    @sqlmodel_routines_Function.setter
    def sqlmodel_routines_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_routines_Function__sqlmodel_routines_Function", None)
        self.__sqlmodel_routines_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoutineResultTable124"):
                opp_val = getattr(old_value, "RoutineResultTable124", None)
                if opp_val == self:
                    setattr(old_value, "RoutineResultTable124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoutineResultTable124"):
                opp_val = getattr(value, "RoutineResultTable124", None)
                setattr(value, "RoutineResultTable124", self)

class Trigger:

    pass
class schema_sqlmodel_EObject:

    pass
class Database:

    pass
class Sequence:

    pass
class Table:

    pass
class sqlmodel_tables_DerivedTable(Table):

    pass
class sqlmodel_routines_RoutineResultTable(Table):

    pass
class sqlmodel_tables_BaseTable(Table):

    def __init__(self, BaseTable148: set["TableConstraint"] = None, referencedTable: set["ForeignKey"] = None, Table136: "sqlmodel_tables_Table" = None, Table134: "sqlmodel_tables_Table" = None, Table76: "sqlmodel_constraints_Index" = None, Table: "sqlmodel_schema_Schema" = None, Table152: "sqlmodel_tables_Column" = None, Table106: "sqlmodel_datatypes_ReferenceDataType" = None, Table161: "sqlmodel_tables_Trigger" = None):
        self.BaseTable148 = BaseTable148 if BaseTable148 is not None else set()
        self.referencedTable = referencedTable if referencedTable is not None else set()
        
        pass
    @property
    def BaseTable148(self):
        return self.__BaseTable148

    @BaseTable148.setter
    def BaseTable148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_BaseTable__BaseTable148", None)
        self.__BaseTable148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TableConstraint"):
                    opp_val = getattr(item, "TableConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "TableConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TableConstraint"):
                    opp_val = getattr(item, "TableConstraint", None)
                    
                    setattr(item, "TableConstraint", self)
                    

    @property
    def referencedTable(self):
        return self.__referencedTable

    @referencedTable.setter
    def referencedTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_BaseTable__referencedTable", None)
        self.__referencedTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey150"):
                    opp_val = getattr(item, "ForeignKey150", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey150"):
                    opp_val = getattr(item, "ForeignKey150", None)
                    
                    setattr(item, "ForeignKey150", self)
                    

    def getPrimaryKey(self) :
        # TODO: Implement getPrimaryKey method
        pass

    def getForeignKeys(self) :
        # TODO: Implement getForeignKeys method
        pass

    def getUniqueConstraints(self) :
        # TODO: Implement getUniqueConstraints method
        pass

class Index:

    pass
class UserDefinedType:

    pass
class sqlmodel_datatypes_DistinctUserDefinedType(UserDefinedType):

    pass
class sqlmodel_datatypes_StructuredUserDefinedType(UserDefinedType):

    def __init__(self, instantiable: bool, final: bool, sub: "StructuredUserDefinedType" = None, super: set["StructuredUserDefinedType"] = None, sqlmodel_datatypes_StructuredUserDefinedType: set["AttributeDefinition"] = None, sqlmodel_datatypes_StructuredUserDefinedType103: set["Method"] = None, UserDefinedType: "sqlmodel_schema_TypedElement" = None, UserDefinedType17: "sqlmodel_schema_Schema" = None):
        self.instantiable = instantiable
        self.final = final
        self.sub = sub
        self.super = super if super is not None else set()
        self.sqlmodel_datatypes_StructuredUserDefinedType = sqlmodel_datatypes_StructuredUserDefinedType if sqlmodel_datatypes_StructuredUserDefinedType is not None else set()
        self.sqlmodel_datatypes_StructuredUserDefinedType103 = sqlmodel_datatypes_StructuredUserDefinedType103 if sqlmodel_datatypes_StructuredUserDefinedType103 is not None else set()
        
        pass
    @property
    def instantiable(self):
        return self.__instantiable

    @instantiable.setter
    def instantiable(self, instantiable: bool):
        self.__instantiable = instantiable


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def super(self):
        return self.__super

    @super.setter
    def super(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_datatypes_StructuredUserDefinedType__super", None)
        self.__super = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StructuredUserDefinedType100"):
                    opp_val = getattr(item, "StructuredUserDefinedType100", None)
                    
                    if opp_val == self:
                        setattr(item, "StructuredUserDefinedType100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StructuredUserDefinedType100"):
                    opp_val = getattr(item, "StructuredUserDefinedType100", None)
                    
                    setattr(item, "StructuredUserDefinedType100", self)
                    

    @property
    def sqlmodel_datatypes_StructuredUserDefinedType(self):
        return self.__sqlmodel_datatypes_StructuredUserDefinedType

    @sqlmodel_datatypes_StructuredUserDefinedType.setter
    def sqlmodel_datatypes_StructuredUserDefinedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_datatypes_StructuredUserDefinedType__sqlmodel_datatypes_StructuredUserDefinedType", None)
        self.__sqlmodel_datatypes_StructuredUserDefinedType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeDefinition"):
                    opp_val = getattr(item, "AttributeDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeDefinition"):
                    opp_val = getattr(item, "AttributeDefinition", None)
                    
                    setattr(item, "AttributeDefinition", self)
                    

    @property
    def sqlmodel_datatypes_StructuredUserDefinedType103(self):
        return self.__sqlmodel_datatypes_StructuredUserDefinedType103

    @sqlmodel_datatypes_StructuredUserDefinedType103.setter
    def sqlmodel_datatypes_StructuredUserDefinedType103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_datatypes_StructuredUserDefinedType__sqlmodel_datatypes_StructuredUserDefinedType103", None)
        self.__sqlmodel_datatypes_StructuredUserDefinedType103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    setattr(item, "Method", self)
                    

    @property
    def sub(self):
        return self.__sub

    @sub.setter
    def sub(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_datatypes_StructuredUserDefinedType__sub", None)
        self.__sub = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StructuredUserDefinedType"):
                opp_val = getattr(old_value, "StructuredUserDefinedType", None)
                if opp_val == self:
                    setattr(old_value, "StructuredUserDefinedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StructuredUserDefinedType"):
                opp_val = getattr(value, "StructuredUserDefinedType", None)
                setattr(value, "StructuredUserDefinedType", self)

class SQLDataType:

    pass
class sqlmodel_datatypes_PredefinedDataType(SQLDataType):

    def __init__(self, primitiveType: str, SQLDataType: "sqlmodel_schema_TypedElement" = None):
        self.primitiveType = primitiveType
        
        pass
    @property
    def primitiveType(self):
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType


class SQLObject:

    pass
class sqlmodel_datatypes_UserDefinedTypeOrdering(SQLObject):

    def __init__(self, orderingForm: str, orderingCategory: str, sqlmodel_datatypes_UserDefinedTypeOrdering: "Routine" = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.orderingForm = orderingForm
        self.orderingCategory = orderingCategory
        self.sqlmodel_datatypes_UserDefinedTypeOrdering = sqlmodel_datatypes_UserDefinedTypeOrdering
        
        pass
    @property
    def orderingForm(self):
        return self.__orderingForm

    @orderingForm.setter
    def orderingForm(self, orderingForm: str):
        self.__orderingForm = orderingForm


    @property
    def orderingCategory(self):
        return self.__orderingCategory

    @orderingCategory.setter
    def orderingCategory(self, orderingCategory: str):
        self.__orderingCategory = orderingCategory


    @property
    def sqlmodel_datatypes_UserDefinedTypeOrdering(self):
        return self.__sqlmodel_datatypes_UserDefinedTypeOrdering

    @sqlmodel_datatypes_UserDefinedTypeOrdering.setter
    def sqlmodel_datatypes_UserDefinedTypeOrdering(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_datatypes_UserDefinedTypeOrdering__sqlmodel_datatypes_UserDefinedTypeOrdering", None)
        self.__sqlmodel_datatypes_UserDefinedTypeOrdering = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Routine111"):
                opp_val = getattr(old_value, "Routine111", None)
                if opp_val == self:
                    setattr(old_value, "Routine111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Routine111"):
                opp_val = getattr(value, "Routine111", None)
                setattr(value, "Routine111", self)

class sqlmodel_tables_Trigger(SQLObject):

    def __init__(self, actionGranularity: str, timeStamp: str, actionTime: str, updateType: bool, insertType: bool, deleteType: bool, oldRow: str, newRow: str, oldTable: str, newTable: str, sqlmodel_tables_Trigger167: "SearchCondition" = None, triggers: "Schema" = None, triggers160: "Table" = None, sqlmodel_tables_Trigger: set["SQLStatement"] = None, sqlmodel_tables_Trigger164: set["Column"] = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.actionGranularity = actionGranularity
        self.timeStamp = timeStamp
        self.actionTime = actionTime
        self.updateType = updateType
        self.insertType = insertType
        self.deleteType = deleteType
        self.oldRow = oldRow
        self.newRow = newRow
        self.oldTable = oldTable
        self.newTable = newTable
        self.sqlmodel_tables_Trigger167 = sqlmodel_tables_Trigger167
        self.triggers = triggers
        self.triggers160 = triggers160
        self.sqlmodel_tables_Trigger = sqlmodel_tables_Trigger if sqlmodel_tables_Trigger is not None else set()
        self.sqlmodel_tables_Trigger164 = sqlmodel_tables_Trigger164 if sqlmodel_tables_Trigger164 is not None else set()
        
        pass
    @property
    def oldRow(self):
        return self.__oldRow

    @oldRow.setter
    def oldRow(self, oldRow: str):
        self.__oldRow = oldRow


    @property
    def newRow(self):
        return self.__newRow

    @newRow.setter
    def newRow(self, newRow: str):
        self.__newRow = newRow


    @property
    def newTable(self):
        return self.__newTable

    @newTable.setter
    def newTable(self, newTable: str):
        self.__newTable = newTable


    @property
    def deleteType(self):
        return self.__deleteType

    @deleteType.setter
    def deleteType(self, deleteType: bool):
        self.__deleteType = deleteType


    @property
    def oldTable(self):
        return self.__oldTable

    @oldTable.setter
    def oldTable(self, oldTable: str):
        self.__oldTable = oldTable


    @property
    def updateType(self):
        return self.__updateType

    @updateType.setter
    def updateType(self, updateType: bool):
        self.__updateType = updateType


    @property
    def actionTime(self):
        return self.__actionTime

    @actionTime.setter
    def actionTime(self, actionTime: str):
        self.__actionTime = actionTime


    @property
    def insertType(self):
        return self.__insertType

    @insertType.setter
    def insertType(self, insertType: bool):
        self.__insertType = insertType


    @property
    def timeStamp(self):
        return self.__timeStamp

    @timeStamp.setter
    def timeStamp(self, timeStamp: str):
        self.__timeStamp = timeStamp


    @property
    def actionGranularity(self):
        return self.__actionGranularity

    @actionGranularity.setter
    def actionGranularity(self, actionGranularity: str):
        self.__actionGranularity = actionGranularity


    @property
    def triggers160(self):
        return self.__triggers160

    @triggers160.setter
    def triggers160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Trigger__triggers160", None)
        self.__triggers160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table161"):
                opp_val = getattr(old_value, "Table161", None)
                if opp_val == self:
                    setattr(old_value, "Table161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table161"):
                opp_val = getattr(value, "Table161", None)
                setattr(value, "Table161", self)

    @property
    def sqlmodel_tables_Trigger167(self):
        return self.__sqlmodel_tables_Trigger167

    @sqlmodel_tables_Trigger167.setter
    def sqlmodel_tables_Trigger167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Trigger__sqlmodel_tables_Trigger167", None)
        self.__sqlmodel_tables_Trigger167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SearchCondition168"):
                opp_val = getattr(old_value, "SearchCondition168", None)
                if opp_val == self:
                    setattr(old_value, "SearchCondition168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SearchCondition168"):
                opp_val = getattr(value, "SearchCondition168", None)
                setattr(value, "SearchCondition168", self)

    @property
    def sqlmodel_tables_Trigger(self):
        return self.__sqlmodel_tables_Trigger

    @sqlmodel_tables_Trigger.setter
    def sqlmodel_tables_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Trigger__sqlmodel_tables_Trigger", None)
        self.__sqlmodel_tables_Trigger = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SQLStatement"):
                    opp_val = getattr(item, "SQLStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "SQLStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SQLStatement"):
                    opp_val = getattr(item, "SQLStatement", None)
                    
                    setattr(item, "SQLStatement", self)
                    

    @property
    def triggers(self):
        return self.__triggers

    @triggers.setter
    def triggers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Trigger__triggers", None)
        self.__triggers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema158"):
                opp_val = getattr(old_value, "Schema158", None)
                if opp_val == self:
                    setattr(old_value, "Schema158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema158"):
                opp_val = getattr(value, "Schema158", None)
                setattr(value, "Schema158", self)

    @property
    def sqlmodel_tables_Trigger164(self):
        return self.__sqlmodel_tables_Trigger164

    @sqlmodel_tables_Trigger164.setter
    def sqlmodel_tables_Trigger164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Trigger__sqlmodel_tables_Trigger164", None)
        self.__sqlmodel_tables_Trigger164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column165"):
                    opp_val = getattr(item, "Column165", None)
                    
                    if opp_val == self:
                        setattr(item, "Column165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column165"):
                    opp_val = getattr(item, "Column165", None)
                    
                    setattr(item, "Column165", self)
                    

class sqlmodel_constraints_IndexExpression(SQLObject):

    def __init__(self, sql: str, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.sql = sql
        
        pass
    @property
    def sql(self):
        return self.__sql

    @sql.setter
    def sql(self, sql: str):
        self.__sql = sql


class sqlmodel_accesscontrol_Privilege(SQLObject):

    def __init__(self, grantable: bool, action: str, withHierarchy: bool, privileges: "SQLObject" = None, grantedPrivilege: "AuthorizationIdentifier" = None, receivedPrivilege: "AuthorizationIdentifier" = None, sqlmodel_accesscontrol_Privilege: set["SQLObject"] = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.grantable = grantable
        self.action = action
        self.withHierarchy = withHierarchy
        self.privileges = privileges
        self.grantedPrivilege = grantedPrivilege
        self.receivedPrivilege = receivedPrivilege
        self.sqlmodel_accesscontrol_Privilege = sqlmodel_accesscontrol_Privilege if sqlmodel_accesscontrol_Privilege is not None else set()
        
        pass
    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def withHierarchy(self):
        return self.__withHierarchy

    @withHierarchy.setter
    def withHierarchy(self, withHierarchy: bool):
        self.__withHierarchy = withHierarchy


    @property
    def grantable(self):
        return self.__grantable

    @grantable.setter
    def grantable(self, grantable: bool):
        self.__grantable = grantable


    @property
    def privileges(self):
        return self.__privileges

    @privileges.setter
    def privileges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_accesscontrol_Privilege__privileges", None)
        self.__privileges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQLObject189"):
                opp_val = getattr(old_value, "SQLObject189", None)
                if opp_val == self:
                    setattr(old_value, "SQLObject189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQLObject189"):
                opp_val = getattr(value, "SQLObject189", None)
                setattr(value, "SQLObject189", self)

    @property
    def grantedPrivilege(self):
        return self.__grantedPrivilege

    @grantedPrivilege.setter
    def grantedPrivilege(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_accesscontrol_Privilege__grantedPrivilege", None)
        self.__grantedPrivilege = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AuthorizationIdentifier183"):
                opp_val = getattr(old_value, "AuthorizationIdentifier183", None)
                if opp_val == self:
                    setattr(old_value, "AuthorizationIdentifier183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AuthorizationIdentifier183"):
                opp_val = getattr(value, "AuthorizationIdentifier183", None)
                setattr(value, "AuthorizationIdentifier183", self)

    @property
    def sqlmodel_accesscontrol_Privilege(self):
        return self.__sqlmodel_accesscontrol_Privilege

    @sqlmodel_accesscontrol_Privilege.setter
    def sqlmodel_accesscontrol_Privilege(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_accesscontrol_Privilege__sqlmodel_accesscontrol_Privilege", None)
        self.__sqlmodel_accesscontrol_Privilege = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SQLObject187"):
                    opp_val = getattr(item, "SQLObject187", None)
                    
                    if opp_val == self:
                        setattr(item, "SQLObject187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SQLObject187"):
                    opp_val = getattr(item, "SQLObject187", None)
                    
                    setattr(item, "SQLObject187", self)
                    

    @property
    def receivedPrivilege(self):
        return self.__receivedPrivilege

    @receivedPrivilege.setter
    def receivedPrivilege(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_accesscontrol_Privilege__receivedPrivilege", None)
        self.__receivedPrivilege = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AuthorizationIdentifier185"):
                opp_val = getattr(old_value, "AuthorizationIdentifier185", None)
                if opp_val == self:
                    setattr(old_value, "AuthorizationIdentifier185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AuthorizationIdentifier185"):
                opp_val = getattr(value, "AuthorizationIdentifier185", None)
                setattr(value, "AuthorizationIdentifier185", self)

class sqlmodel_schema_TypedElement(SQLObject):

    def __init__(self, sqlmodel_schema_TypedElement: "SQLDataType" = None, sqlmodel_schema_TypedElement2: "UserDefinedType" = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.sqlmodel_schema_TypedElement = sqlmodel_schema_TypedElement
        self.sqlmodel_schema_TypedElement2 = sqlmodel_schema_TypedElement2
        
        pass
    @property
    def sqlmodel_schema_TypedElement2(self):
        return self.__sqlmodel_schema_TypedElement2

    @sqlmodel_schema_TypedElement2.setter
    def sqlmodel_schema_TypedElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_TypedElement__sqlmodel_schema_TypedElement2", None)
        self.__sqlmodel_schema_TypedElement2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserDefinedType"):
                opp_val = getattr(old_value, "UserDefinedType", None)
                if opp_val == self:
                    setattr(old_value, "UserDefinedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserDefinedType"):
                opp_val = getattr(value, "UserDefinedType", None)
                setattr(value, "UserDefinedType", self)

    @property
    def sqlmodel_schema_TypedElement(self):
        return self.__sqlmodel_schema_TypedElement

    @sqlmodel_schema_TypedElement.setter
    def sqlmodel_schema_TypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_TypedElement__sqlmodel_schema_TypedElement", None)
        self.__sqlmodel_schema_TypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQLDataType"):
                opp_val = getattr(old_value, "SQLDataType", None)
                if opp_val == self:
                    setattr(old_value, "SQLDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQLDataType"):
                opp_val = getattr(value, "SQLDataType", None)
                setattr(value, "SQLDataType", self)

    def getDataType(self) :
        # TODO: Implement getDataType method
        pass

    def setDataType(self, sqlmodel_newType):
        # TODO: Implement setDataType method
        pass

class sqlmodel_accesscontrol_AuthorizationIdentifier(SQLObject):

    pass
class sqlmodel_routines_Routine(SQLObject):

    def __init__(self, specificName: str, sqlDataAccess: str, creationTS: str, lastAlteredTS: str, authorizationID: str, security: str, language: str, parameterStyle: str, deterministic: bool, externalName: str, routine: set["Parameter"] = None, sqlmodel_routines_Routine: "Source" = None, routines: "Schema" = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.specificName = specificName
        self.sqlDataAccess = sqlDataAccess
        self.creationTS = creationTS
        self.lastAlteredTS = lastAlteredTS
        self.authorizationID = authorizationID
        self.security = security
        self.language = language
        self.parameterStyle = parameterStyle
        self.deterministic = deterministic
        self.externalName = externalName
        self.routine = routine if routine is not None else set()
        self.sqlmodel_routines_Routine = sqlmodel_routines_Routine
        self.routines = routines
        
        pass
    @property
    def deterministic(self):
        return self.__deterministic

    @deterministic.setter
    def deterministic(self, deterministic: bool):
        self.__deterministic = deterministic


    @property
    def authorizationID(self):
        return self.__authorizationID

    @authorizationID.setter
    def authorizationID(self, authorizationID: str):
        self.__authorizationID = authorizationID


    @property
    def security(self):
        return self.__security

    @security.setter
    def security(self, security: str):
        self.__security = security


    @property
    def specificName(self):
        return self.__specificName

    @specificName.setter
    def specificName(self, specificName: str):
        self.__specificName = specificName


    @property
    def lastAlteredTS(self):
        return self.__lastAlteredTS

    @lastAlteredTS.setter
    def lastAlteredTS(self, lastAlteredTS: str):
        self.__lastAlteredTS = lastAlteredTS


    @property
    def parameterStyle(self):
        return self.__parameterStyle

    @parameterStyle.setter
    def parameterStyle(self, parameterStyle: str):
        self.__parameterStyle = parameterStyle


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def sqlDataAccess(self):
        return self.__sqlDataAccess

    @sqlDataAccess.setter
    def sqlDataAccess(self, sqlDataAccess: str):
        self.__sqlDataAccess = sqlDataAccess


    @property
    def externalName(self):
        return self.__externalName

    @externalName.setter
    def externalName(self, externalName: str):
        self.__externalName = externalName


    @property
    def creationTS(self):
        return self.__creationTS

    @creationTS.setter
    def creationTS(self, creationTS: str):
        self.__creationTS = creationTS


    @property
    def routines(self):
        return self.__routines

    @routines.setter
    def routines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_routines_Routine__routines", None)
        self.__routines = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema117"):
                opp_val = getattr(old_value, "Schema117", None)
                if opp_val == self:
                    setattr(old_value, "Schema117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema117"):
                opp_val = getattr(value, "Schema117", None)
                setattr(value, "Schema117", self)

    @property
    def sqlmodel_routines_Routine(self):
        return self.__sqlmodel_routines_Routine

    @sqlmodel_routines_Routine.setter
    def sqlmodel_routines_Routine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_routines_Routine__sqlmodel_routines_Routine", None)
        self.__sqlmodel_routines_Routine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Source"):
                opp_val = getattr(old_value, "Source", None)
                if opp_val == self:
                    setattr(old_value, "Source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Source"):
                opp_val = getattr(value, "Source", None)
                setattr(value, "Source", self)

    @property
    def routine(self):
        return self.__routine

    @routine.setter
    def routine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_routines_Routine__routine", None)
        self.__routine = value if value is not None else set()
        
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
                    

class sqlmodel_constraints_Index(SQLObject):

    def __init__(self, unique: bool, systemGenerated: bool, clustered: bool, fillFactor: int, sqlmodel_constraints_Index: set["IndexMember"] = None, index: "Table" = None, uniqueIndex: set["ForeignKey"] = None, sqlmodel_constraints_Index80: set["IndexMember"] = None, indices: "Schema" = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.unique = unique
        self.systemGenerated = systemGenerated
        self.clustered = clustered
        self.fillFactor = fillFactor
        self.sqlmodel_constraints_Index = sqlmodel_constraints_Index if sqlmodel_constraints_Index is not None else set()
        self.index = index
        self.uniqueIndex = uniqueIndex if uniqueIndex is not None else set()
        self.sqlmodel_constraints_Index80 = sqlmodel_constraints_Index80 if sqlmodel_constraints_Index80 is not None else set()
        self.indices = indices
        
        pass
    @property
    def fillFactor(self):
        return self.__fillFactor

    @fillFactor.setter
    def fillFactor(self, fillFactor: int):
        self.__fillFactor = fillFactor


    @property
    def systemGenerated(self):
        return self.__systemGenerated

    @systemGenerated.setter
    def systemGenerated(self, systemGenerated: bool):
        self.__systemGenerated = systemGenerated


    @property
    def clustered(self):
        return self.__clustered

    @clustered.setter
    def clustered(self, clustered: bool):
        self.__clustered = clustered


    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def indices(self):
        return self.__indices

    @indices.setter
    def indices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_Index__indices", None)
        self.__indices = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema73"):
                opp_val = getattr(old_value, "Schema73", None)
                if opp_val == self:
                    setattr(old_value, "Schema73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema73"):
                opp_val = getattr(value, "Schema73", None)
                setattr(value, "Schema73", self)

    @property
    def sqlmodel_constraints_Index80(self):
        return self.__sqlmodel_constraints_Index80

    @sqlmodel_constraints_Index80.setter
    def sqlmodel_constraints_Index80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_Index__sqlmodel_constraints_Index80", None)
        self.__sqlmodel_constraints_Index80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IndexMember81"):
                    opp_val = getattr(item, "IndexMember81", None)
                    
                    if opp_val == self:
                        setattr(item, "IndexMember81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IndexMember81"):
                    opp_val = getattr(item, "IndexMember81", None)
                    
                    setattr(item, "IndexMember81", self)
                    

    @property
    def sqlmodel_constraints_Index(self):
        return self.__sqlmodel_constraints_Index

    @sqlmodel_constraints_Index.setter
    def sqlmodel_constraints_Index(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_Index__sqlmodel_constraints_Index", None)
        self.__sqlmodel_constraints_Index = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IndexMember"):
                    opp_val = getattr(item, "IndexMember", None)
                    
                    if opp_val == self:
                        setattr(item, "IndexMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IndexMember"):
                    opp_val = getattr(item, "IndexMember", None)
                    
                    setattr(item, "IndexMember", self)
                    

    @property
    def uniqueIndex(self):
        return self.__uniqueIndex

    @uniqueIndex.setter
    def uniqueIndex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_Index__uniqueIndex", None)
        self.__uniqueIndex = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey78"):
                    opp_val = getattr(item, "ForeignKey78", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey78"):
                    opp_val = getattr(item, "ForeignKey78", None)
                    
                    setattr(item, "ForeignKey78", self)
                    

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_Index__index", None)
        self.__index = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table76"):
                opp_val = getattr(old_value, "Table76", None)
                if opp_val == self:
                    setattr(old_value, "Table76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table76"):
                opp_val = getattr(value, "Table76", None)
                setattr(value, "Table76", self)

class sqlmodel_constraints_IndexMember(SQLObject):

    def __init__(self, incrementType: str, sqlmodel_constraints_IndexMember: "Column" = None, sqlmodel_constraints_IndexMember85: "IndexExpression" = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.incrementType = incrementType
        self.sqlmodel_constraints_IndexMember = sqlmodel_constraints_IndexMember
        self.sqlmodel_constraints_IndexMember85 = sqlmodel_constraints_IndexMember85
        
        pass
    @property
    def incrementType(self):
        return self.__incrementType

    @incrementType.setter
    def incrementType(self, incrementType: str):
        self.__incrementType = incrementType


    @property
    def sqlmodel_constraints_IndexMember85(self):
        return self.__sqlmodel_constraints_IndexMember85

    @sqlmodel_constraints_IndexMember85.setter
    def sqlmodel_constraints_IndexMember85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_IndexMember__sqlmodel_constraints_IndexMember85", None)
        self.__sqlmodel_constraints_IndexMember85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IndexExpression"):
                opp_val = getattr(old_value, "IndexExpression", None)
                if opp_val == self:
                    setattr(old_value, "IndexExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IndexExpression"):
                opp_val = getattr(value, "IndexExpression", None)
                setattr(value, "IndexExpression", self)

    @property
    def sqlmodel_constraints_IndexMember(self):
        return self.__sqlmodel_constraints_IndexMember

    @sqlmodel_constraints_IndexMember.setter
    def sqlmodel_constraints_IndexMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_constraints_IndexMember__sqlmodel_constraints_IndexMember", None)
        self.__sqlmodel_constraints_IndexMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Column83"):
                opp_val = getattr(old_value, "Column83", None)
                if opp_val == self:
                    setattr(old_value, "Column83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Column83"):
                opp_val = getattr(value, "Column83", None)
                setattr(value, "Column83", self)

class sqlmodel_tables_Table(SQLObject):

    def __init__(self, selfRefColumnGeneration: str, insertable: bool, updatable: bool, supertable: set["Table"] = None, tables: "Schema" = None, table: set["Column"] = None, sqlmodel_tables_Table: "StructuredUserDefinedType" = None, subtables: "Table" = None, subjectTable: set["Trigger"] = None, table144: set["Index"] = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.selfRefColumnGeneration = selfRefColumnGeneration
        self.insertable = insertable
        self.updatable = updatable
        self.supertable = supertable if supertable is not None else set()
        self.tables = tables
        self.table = table if table is not None else set()
        self.sqlmodel_tables_Table = sqlmodel_tables_Table
        self.subtables = subtables
        self.subjectTable = subjectTable if subjectTable is not None else set()
        self.table144 = table144 if table144 is not None else set()
        
        pass
    @property
    def selfRefColumnGeneration(self):
        return self.__selfRefColumnGeneration

    @selfRefColumnGeneration.setter
    def selfRefColumnGeneration(self, selfRefColumnGeneration: str):
        self.__selfRefColumnGeneration = selfRefColumnGeneration


    @property
    def updatable(self):
        return self.__updatable

    @updatable.setter
    def updatable(self, updatable: bool):
        self.__updatable = updatable


    @property
    def insertable(self):
        return self.__insertable

    @insertable.setter
    def insertable(self, insertable: bool):
        self.__insertable = insertable


    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Table__table", None)
        self.__table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column132"):
                    opp_val = getattr(item, "Column132", None)
                    
                    if opp_val == self:
                        setattr(item, "Column132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column132"):
                    opp_val = getattr(item, "Column132", None)
                    
                    setattr(item, "Column132", self)
                    

    @property
    def table144(self):
        return self.__table144

    @table144.setter
    def table144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Table__table144", None)
        self.__table144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Index145"):
                    opp_val = getattr(item, "Index145", None)
                    
                    if opp_val == self:
                        setattr(item, "Index145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Index145"):
                    opp_val = getattr(item, "Index145", None)
                    
                    setattr(item, "Index145", self)
                    

    @property
    def supertable(self):
        return self.__supertable

    @supertable.setter
    def supertable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Table__supertable", None)
        self.__supertable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table136"):
                    opp_val = getattr(item, "Table136", None)
                    
                    if opp_val == self:
                        setattr(item, "Table136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table136"):
                    opp_val = getattr(item, "Table136", None)
                    
                    setattr(item, "Table136", self)
                    

    @property
    def subtables(self):
        return self.__subtables

    @subtables.setter
    def subtables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Table__subtables", None)
        self.__subtables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table134"):
                opp_val = getattr(old_value, "Table134", None)
                if opp_val == self:
                    setattr(old_value, "Table134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table134"):
                opp_val = getattr(value, "Table134", None)
                setattr(value, "Table134", self)

    @property
    def sqlmodel_tables_Table(self):
        return self.__sqlmodel_tables_Table

    @sqlmodel_tables_Table.setter
    def sqlmodel_tables_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Table__sqlmodel_tables_Table", None)
        self.__sqlmodel_tables_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StructuredUserDefinedType140"):
                opp_val = getattr(old_value, "StructuredUserDefinedType140", None)
                if opp_val == self:
                    setattr(old_value, "StructuredUserDefinedType140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StructuredUserDefinedType140"):
                opp_val = getattr(value, "StructuredUserDefinedType140", None)
                setattr(value, "StructuredUserDefinedType140", self)

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Table__tables", None)
        self.__tables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema138"):
                opp_val = getattr(old_value, "Schema138", None)
                if opp_val == self:
                    setattr(old_value, "Schema138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema138"):
                opp_val = getattr(value, "Schema138", None)
                setattr(value, "Schema138", self)

    @property
    def subjectTable(self):
        return self.__subjectTable

    @subjectTable.setter
    def subjectTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_tables_Table__subjectTable", None)
        self.__subjectTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trigger142"):
                    opp_val = getattr(item, "Trigger142", None)
                    
                    if opp_val == self:
                        setattr(item, "Trigger142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trigger142"):
                    opp_val = getattr(item, "Trigger142", None)
                    
                    setattr(item, "Trigger142", self)
                    

class sqlmodel_schema_Dependency(SQLObject):

    def __init__(self, dependencyType: str, sqlmodel_schema_Dependency: "schema_sqlmodel_EObject" = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.dependencyType = dependencyType
        self.sqlmodel_schema_Dependency = sqlmodel_schema_Dependency
        
        pass
    @property
    def dependencyType(self):
        return self.__dependencyType

    @dependencyType.setter
    def dependencyType(self, dependencyType: str):
        self.__dependencyType = dependencyType


    @property
    def sqlmodel_schema_Dependency(self):
        return self.__sqlmodel_schema_Dependency

    @sqlmodel_schema_Dependency.setter
    def sqlmodel_schema_Dependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_Dependency__sqlmodel_schema_Dependency", None)
        self.__sqlmodel_schema_Dependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema_sqlmodel_EObject"):
                opp_val = getattr(old_value, "schema_sqlmodel_EObject", None)
                if opp_val == self:
                    setattr(old_value, "schema_sqlmodel_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema_sqlmodel_EObject"):
                opp_val = getattr(value, "schema_sqlmodel_EObject", None)
                setattr(value, "schema_sqlmodel_EObject", self)

class sqlmodel_schema_Database(SQLObject):

    def __init__(self, vendor: str, version: str, database: set["Schema"] = None, Database39: set["AuthorizationIdentifier"] = None, Database34: set["Event"] = None, Database36: set["Catalog"] = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.vendor = vendor
        self.version = version
        self.database = database if database is not None else set()
        self.Database39 = Database39 if Database39 is not None else set()
        self.Database34 = Database34 if Database34 is not None else set()
        self.Database36 = Database36 if Database36 is not None else set()
        
        pass
    @property
    def vendor(self):
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def Database36(self):
        return self.__Database36

    @Database36.setter
    def Database36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_Database__Database36", None)
        self.__Database36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Catalog37"):
                    opp_val = getattr(item, "Catalog37", None)
                    
                    if opp_val == self:
                        setattr(item, "Catalog37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Catalog37"):
                    opp_val = getattr(item, "Catalog37", None)
                    
                    setattr(item, "Catalog37", self)
                    

    @property
    def Database34(self):
        return self.__Database34

    @Database34.setter
    def Database34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_Database__Database34", None)
        self.__Database34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    if opp_val == self:
                        setattr(item, "Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    setattr(item, "Event", self)
                    

    @property
    def Database39(self):
        return self.__Database39

    @Database39.setter
    def Database39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_Database__Database39", None)
        self.__Database39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AuthorizationIdentifier40"):
                    opp_val = getattr(item, "AuthorizationIdentifier40", None)
                    
                    if opp_val == self:
                        setattr(item, "AuthorizationIdentifier40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AuthorizationIdentifier40"):
                    opp_val = getattr(item, "AuthorizationIdentifier40", None)
                    
                    setattr(item, "AuthorizationIdentifier40", self)
                    

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_Database__database", None)
        self.__database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Schema32"):
                    opp_val = getattr(item, "Schema32", None)
                    
                    if opp_val == self:
                        setattr(item, "Schema32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Schema32"):
                    opp_val = getattr(item, "Schema32", None)
                    
                    setattr(item, "Schema32", self)
                    

    def getUserDefinedTypes(self) :
        # TODO: Implement getUserDefinedTypes method
        pass

class sqlmodel_schema_Event(SQLObject):

    def __init__(self, condition: str, action: str, enabled: bool, for_: str, events: "Database" = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.condition = condition
        self.action = action
        self.enabled = enabled
        self.for_ = for_
        self.events = events
        
        pass
    @property
    def for_(self):
        return self.__for_

    @for_.setter
    def for_(self, for_: str):
        self.__for_ = for_


    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_schema_Event__events", None)
        self.__events = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Database42"):
                opp_val = getattr(old_value, "Database42", None)
                if opp_val == self:
                    setattr(old_value, "Database42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Database42"):
                opp_val = getattr(value, "Database42", None)
                setattr(value, "Database42", self)

class sqlmodel_accesscontrol_RoleAuthorization(SQLObject):

    def __init__(self, grantable: bool, roleAuthorization: "Role" = None, receivedRoleAuthorization: "AuthorizationIdentifier" = None, grantedRoleAuthorization: "AuthorizationIdentifier" = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.grantable = grantable
        self.roleAuthorization = roleAuthorization
        self.receivedRoleAuthorization = receivedRoleAuthorization
        self.grantedRoleAuthorization = grantedRoleAuthorization
        
        pass
    @property
    def grantable(self):
        return self.__grantable

    @grantable.setter
    def grantable(self, grantable: bool):
        self.__grantable = grantable


    @property
    def receivedRoleAuthorization(self):
        return self.__receivedRoleAuthorization

    @receivedRoleAuthorization.setter
    def receivedRoleAuthorization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_accesscontrol_RoleAuthorization__receivedRoleAuthorization", None)
        self.__receivedRoleAuthorization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AuthorizationIdentifier196"):
                opp_val = getattr(old_value, "AuthorizationIdentifier196", None)
                if opp_val == self:
                    setattr(old_value, "AuthorizationIdentifier196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AuthorizationIdentifier196"):
                opp_val = getattr(value, "AuthorizationIdentifier196", None)
                setattr(value, "AuthorizationIdentifier196", self)

    @property
    def grantedRoleAuthorization(self):
        return self.__grantedRoleAuthorization

    @grantedRoleAuthorization.setter
    def grantedRoleAuthorization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_accesscontrol_RoleAuthorization__grantedRoleAuthorization", None)
        self.__grantedRoleAuthorization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AuthorizationIdentifier198"):
                opp_val = getattr(old_value, "AuthorizationIdentifier198", None)
                if opp_val == self:
                    setattr(old_value, "AuthorizationIdentifier198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AuthorizationIdentifier198"):
                opp_val = getattr(value, "AuthorizationIdentifier198", None)
                setattr(value, "AuthorizationIdentifier198", self)

    @property
    def roleAuthorization(self):
        return self.__roleAuthorization

    @roleAuthorization.setter
    def roleAuthorization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_accesscontrol_RoleAuthorization__roleAuthorization", None)
        self.__roleAuthorization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role"):
                opp_val = getattr(old_value, "Role", None)
                if opp_val == self:
                    setattr(old_value, "Role", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role"):
                opp_val = getattr(value, "Role", None)
                setattr(value, "Role", self)

class sqlmodel_datatypes_DataType(SQLObject):

    def __init__(self, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        
        pass
    def setContainer(self, sqlmodel_newContainer):
        # TODO: Implement setContainer method
        pass

class sqlmodel_schema_Catalog(SQLObject):

    pass
class sqlmodel_schema_Schema(SQLObject):

    pass
class sqlmodel_datatypes_CharacterSet(SQLObject):

    def __init__(self, defaultCollation: str, encoding: str, repertoire: str, characterSet: "CharacterStringDataType" = None, charSets: "Schema" = None, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.defaultCollation = defaultCollation
        self.encoding = encoding
        self.repertoire = repertoire
        self.characterSet = characterSet
        self.charSets = charSets
        
        pass
    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding: str):
        self.__encoding = encoding


    @property
    def repertoire(self):
        return self.__repertoire

    @repertoire.setter
    def repertoire(self, repertoire: str):
        self.__repertoire = repertoire


    @property
    def defaultCollation(self):
        return self.__defaultCollation

    @defaultCollation.setter
    def defaultCollation(self, defaultCollation: str):
        self.__defaultCollation = defaultCollation


    @property
    def characterSet(self):
        return self.__characterSet

    @characterSet.setter
    def characterSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_datatypes_CharacterSet__characterSet", None)
        self.__characterSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CharacterStringDataType94"):
                opp_val = getattr(old_value, "CharacterStringDataType94", None)
                if opp_val == self:
                    setattr(old_value, "CharacterStringDataType94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CharacterStringDataType94"):
                opp_val = getattr(value, "CharacterStringDataType94", None)
                setattr(value, "CharacterStringDataType94", self)

    @property
    def charSets(self):
        return self.__charSets

    @charSets.setter
    def charSets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlmodel_datatypes_CharacterSet__charSets", None)
        self.__charSets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema96"):
                opp_val = getattr(old_value, "Schema96", None)
                if opp_val == self:
                    setattr(old_value, "Schema96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema96"):
                opp_val = getattr(value, "Schema96", None)
                setattr(value, "Schema96", self)

class sqlmodel_routines_Source(SQLObject):

    def __init__(self, body: str, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.body = body
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


class sqlmodel_constraints_Constraint(SQLObject):

    def __init__(self, deferrable: bool, initiallyDeferred: bool, enforced: bool, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.deferrable = deferrable
        self.initiallyDeferred = initiallyDeferred
        self.enforced = enforced
        
        pass
    @property
    def deferrable(self):
        return self.__deferrable

    @deferrable.setter
    def deferrable(self, deferrable: bool):
        self.__deferrable = deferrable


    @property
    def initiallyDeferred(self):
        return self.__initiallyDeferred

    @initiallyDeferred.setter
    def initiallyDeferred(self, initiallyDeferred: bool):
        self.__initiallyDeferred = initiallyDeferred


    @property
    def enforced(self):
        return self.__enforced

    @enforced.setter
    def enforced(self, enforced: bool):
        self.__enforced = enforced


class sqlmodel_schema_IdentitySpecifier(SQLObject):

    def __init__(self, generationType: str, startValue: str, increment: str, minimum: str, maximum: str, cycleOption: bool, SQLObject51: "sqlmodel_schema_ObjectExtension" = None, SQLObject187: "sqlmodel_accesscontrol_Privilege" = None, SQLObject189: "sqlmodel_accesscontrol_Privilege" = None, SQLObject44: "sqlmodel_schema_Comment" = None):
        self.generationType = generationType
        self.startValue = startValue
        self.increment = increment
        self.minimum = minimum
        self.maximum = maximum
        self.cycleOption = cycleOption
        
        pass
    @property
    def cycleOption(self):
        return self.__cycleOption

    @cycleOption.setter
    def cycleOption(self, cycleOption: bool):
        self.__cycleOption = cycleOption


    @property
    def generationType(self):
        return self.__generationType

    @generationType.setter
    def generationType(self, generationType: str):
        self.__generationType = generationType


    @property
    def maximum(self):
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum


    @property
    def increment(self):
        return self.__increment

    @increment.setter
    def increment(self, increment: str):
        self.__increment = increment


    @property
    def minimum(self):
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum


    @property
    def startValue(self):
        return self.__startValue

    @startValue.setter
    def startValue(self, startValue: str):
        self.__startValue = startValue

