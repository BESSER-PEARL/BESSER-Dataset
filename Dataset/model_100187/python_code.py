from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CharacterStringTypeKind(Enum):
    CHARACTER = "CHARACTER"
    CHAR = "CHAR"
    CHARACTER_VARYING = "CHARACTER_VARYING"
    CHAR_VARYING = "CHAR_VARYING"
    VARCHAR = "VARCHAR"
class DatetimeValueFunctionKind(Enum):
    CURRENT_DATE = "CURRENT_DATE"
    CURRENT_TIME = "CURRENT_TIME"
    LOCALTIME = "LOCALTIME"
    CURRENT_TIMESTAMP = "CURRENT_TIMESTAMP"
    LOCALTIMESTAMP = "LOCALTIMESTAMP"
class ApproximateNumericTypeKind(Enum):
    FLOAT = "FLOAT"
    REAL = "REAL"
    DOUBLE_PRECISION = "DOUBLE_PRECISION"
class CharLengthUnits(Enum):
    CHARACTERS = "CHARACTERS"
    CODE_UNITS = "CODE_UNITS"
    OCTETS = "OCTETS"
class UniqueSpecificationKind(Enum):
    UNIQUE = "UNIQUE"
    PRIMARY_KEY = "PRIMARY_KEY"
class ExactNumericTypeKind(Enum):
    DEC = "DEC"
    SMALLINT = "SMALLINT"
    INTEGER = "INTEGER"
    INT = "INT"
    BIGINT = "BIGINT"
    NUMERIC = "NUMERIC"
    DECIMAL = "DECIMAL"
class NationalCharacterStringTypeKind(Enum):
    NATIONAL_CHARACTER = "NATIONAL_CHARACTER"
    NATIONAL_CHAR = "NATIONAL_CHAR"
    NCHAR = "NCHAR"
    NATIONAL_CHARACTER_VARYING = "NATIONAL_CHARACTER_VARYING"
    NATIONAL_CHAR_VARYING = "NATIONAL_CHAR_VARYING"
    NCHAR_VARYING = "NCHAR_VARYING"
class Multiplier(Enum):
    K = "K"
    M = "M"
    G = "G"
class TableScope(Enum):
    PERSISTENT = "PERSISTENT"
    GLOBAL_TEMPORARY = "GLOBAL_TEMPORARY"
    LOCAL_TEMPORARY = "LOCAL_TEMPORARY"
class BinaryLargeObjectStringTypeKind(Enum):
    BINARY_LARGE_OBJECT = "BINARY_LARGE_OBJECT"
    BLOB = "BLOB"


############################################
# Definition of Classes
############################################

class sql_schema_TableReference:

    def __init__(self, catalogName: str, schemaName: str, sql_schema_TableReference: "TableDefinition" = None):
        self.catalogName = catalogName
        self.schemaName = schemaName
        self.sql_schema_TableReference = sql_schema_TableReference
        
        pass
    @property
    def catalogName(self):
        return self.__catalogName

    @catalogName.setter
    def catalogName(self, catalogName: str):
        self.__catalogName = catalogName


    @property
    def schemaName(self):
        return self.__schemaName

    @schemaName.setter
    def schemaName(self, schemaName: str):
        self.__schemaName = schemaName


    @property
    def sql_schema_TableReference(self):
        return self.__sql_schema_TableReference

    @sql_schema_TableReference.setter
    def sql_schema_TableReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_schema_TableReference__sql_schema_TableReference", None)
        self.__sql_schema_TableReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableDefinition41"):
                opp_val = getattr(old_value, "TableDefinition41", None)
                if opp_val == self:
                    setattr(old_value, "TableDefinition41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableDefinition41"):
                opp_val = getattr(value, "TableDefinition41", None)
                setattr(value, "TableDefinition41", self)

class TableReference:

    pass
class sql_schema_ReferentialConstraint(ABC):

    pass
class sql_schema_UniqueConstraint(ABC):

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class TableConstraint:

    pass
class sql_schema_TableColumnsConstraint(TableConstraint):

    pass
class DatetimeValueFunction:

    pass
class schema_TableColumnsConstraint:

    pass
class DirectSQLStatement:

    pass
class sql_schema_SQLSchemaStatement(DirectSQLStatement):

    pass
class schema_ReferentialConstraint:

    pass
class sql_schema_ReferentialTableConstraint(schema_ReferentialConstraint, schema_TableColumnsConstraint):

    pass
class schema_ColumnConstraint:

    pass
class sql_schema_ReferentialColumnConstraint(schema_ReferentialConstraint, schema_ColumnConstraint):

    pass
class schema_UniqueConstraint:

    pass
class sql_schema_UniqueTableConstraint(schema_UniqueConstraint, schema_TableColumnsConstraint):

    pass
class sql_schema_UniqueColumnConstraint(schema_UniqueConstraint, schema_ColumnConstraint):

    pass
class SQLSchemaStatement:

    pass
class sql_schema_SQLSchemaDefinitionStatement(SQLSchemaStatement):

    pass
class Column:

    pass
class sql_schema_DefaultOption(ABC):

    pass
class TableDefinition:

    pass
class sql_schema_TableContentsSource(ABC):

    pass
class schema_TableElement:

    pass
class DefaultOption:

    pass
class sql_schema_DatetimeValueFunctionDefaultOption(DefaultOption):

    pass
class sql_schema_LiteralDefaultOption(DefaultOption):

    pass
class sql_schema_ImplicitlyTypedValueSpecificationDefaultOption(DefaultOption):

    pass
class ColumnConstraint:

    pass
class sql_schema_NotNullColumnConstraint(ColumnConstraint):

    pass
class TableElement:

    pass
class sql_schema_Column(TableElement):

    def __init__(self, name: str, owner21: "ColumnConstraint" = None, sql_schema_Column23: "SchemaQualifiedName" = None, sql_schema_Column: "DataType" = None, owner19: "DefaultOption" = None, TableElement: "sql_schema_TableElementList" = None):
        self.name = name
        self.owner21 = owner21
        self.sql_schema_Column23 = sql_schema_Column23
        self.sql_schema_Column = sql_schema_Column
        self.owner19 = owner19
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owner19(self):
        return self.__owner19

    @owner19.setter
    def owner19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_schema_Column__owner19", None)
        self.__owner19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DefaultOption"):
                opp_val = getattr(old_value, "DefaultOption", None)
                if opp_val == self:
                    setattr(old_value, "DefaultOption", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DefaultOption"):
                opp_val = getattr(value, "DefaultOption", None)
                setattr(value, "DefaultOption", self)

    @property
    def sql_schema_Column(self):
        return self.__sql_schema_Column

    @sql_schema_Column.setter
    def sql_schema_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_schema_Column__sql_schema_Column", None)
        self.__sql_schema_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

    @property
    def owner21(self):
        return self.__owner21

    @owner21.setter
    def owner21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_schema_Column__owner21", None)
        self.__owner21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColumnConstraint"):
                opp_val = getattr(old_value, "ColumnConstraint", None)
                if opp_val == self:
                    setattr(old_value, "ColumnConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColumnConstraint"):
                opp_val = getattr(value, "ColumnConstraint", None)
                setattr(value, "ColumnConstraint", self)

    @property
    def sql_schema_Column23(self):
        return self.__sql_schema_Column23

    @sql_schema_Column23.setter
    def sql_schema_Column23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_schema_Column__sql_schema_Column23", None)
        self.__sql_schema_Column23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchemaQualifiedName24"):
                opp_val = getattr(old_value, "SchemaQualifiedName24", None)
                if opp_val == self:
                    setattr(old_value, "SchemaQualifiedName24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchemaQualifiedName24"):
                opp_val = getattr(value, "SchemaQualifiedName24", None)
                setattr(value, "SchemaQualifiedName24", self)

class TableContentsSource:

    pass
class sql_schema_TableElementList(TableContentsSource):

    pass
class TableElementList:

    pass
class sql_schema_TableElement(ABC):

    pass
class ImplicitlyTypedValueSpecification:

    pass
class sql_expression_NullSpecification(ImplicitlyTypedValueSpecification):

    pass
class sql_expression_ImplicitlyTypedValueSpecification(ABC):

    pass
class EObject:

    pass
class sql_schema_TableConstraint(EObject, schema_TableElement):

    pass
class sql_schema_ColumnConstraint(EObject):

    pass
class schema_SQLSchemaDefinitionStatement:

    pass
class sql_schema_TableDefinition(schema_SQLSchemaDefinitionStatement, EObject):

    def __init__(self, label: str, scope: str, sql_schema_TableDefinition: "SchemaQualifiedName" = None, owner: "TableContentsSource" = None):
        self.label = label
        self.scope = scope
        self.sql_schema_TableDefinition = sql_schema_TableDefinition
        self.owner = owner
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope


    @property
    def sql_schema_TableDefinition(self):
        return self.__sql_schema_TableDefinition

    @sql_schema_TableDefinition.setter
    def sql_schema_TableDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_schema_TableDefinition__sql_schema_TableDefinition", None)
        self.__sql_schema_TableDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchemaQualifiedName12"):
                opp_val = getattr(old_value, "SchemaQualifiedName12", None)
                if opp_val == self:
                    setattr(old_value, "SchemaQualifiedName12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchemaQualifiedName12"):
                opp_val = getattr(value, "SchemaQualifiedName12", None)
                setattr(value, "SchemaQualifiedName12", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_schema_TableDefinition__owner", None)
        self.__owner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableContentsSource"):
                opp_val = getattr(old_value, "TableContentsSource", None)
                if opp_val == self:
                    setattr(old_value, "TableContentsSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableContentsSource"):
                opp_val = getattr(value, "TableContentsSource", None)
                setattr(value, "TableContentsSource", self)

class DatetimeType:

    pass
class sql_datatype_TimeType(DatetimeType):

    def __init__(self, precision: str, withTimeZone: str):
        self.precision = precision
        self.withTimeZone = withTimeZone
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


    @property
    def withTimeZone(self):
        return self.__withTimeZone

    @withTimeZone.setter
    def withTimeZone(self, withTimeZone: str):
        self.__withTimeZone = withTimeZone


class sql_datatype_TimestampType(DatetimeType):

    def __init__(self, precision: str, withTimeZone: str):
        self.precision = precision
        self.withTimeZone = withTimeZone
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


    @property
    def withTimeZone(self):
        return self.__withTimeZone

    @withTimeZone.setter
    def withTimeZone(self, withTimeZone: str):
        self.__withTimeZone = withTimeZone


class sql_datatype_DateType(DatetimeType):

    pass
class sql_function_DatetimeValueFunction:

    def __init__(self, kind: str, precision: str):
        self.kind = kind
        self.precision = precision
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class sql_datatype_LargeObjectLength:

    def __init__(self, multiplier: str, units: str, value: str):
        self.multiplier = multiplier
        self.units = units
        self.value = value
        
        pass
    @property
    def units(self):
        return self.__units

    @units.setter
    def units(self, units: str):
        self.__units = units


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def multiplier(self):
        return self.__multiplier

    @multiplier.setter
    def multiplier(self, multiplier: str):
        self.__multiplier = multiplier


class NumericType:

    pass
class sql_datatype_ApproximateNumericType(NumericType):

    def __init__(self, kind: str, precision: str):
        self.kind = kind
        self.precision = precision
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


class sql_datatype_ExactNumericType(NumericType):

    def __init__(self, kind: str, precision: str, scale: str):
        self.kind = kind
        self.precision = precision
        self.scale = scale
        
        pass
    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


class LargeObjectLength:

    pass
class PredefinedType:

    pass
class sql_datatype_BooleanType(PredefinedType):

    pass
class sql_datatype_BinaryLargeObjectStringType(PredefinedType):

    def __init__(self, kind: str, sql_datatype_BinaryLargeObjectStringType: "LargeObjectLength" = None):
        self.kind = kind
        self.sql_datatype_BinaryLargeObjectStringType = sql_datatype_BinaryLargeObjectStringType
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def sql_datatype_BinaryLargeObjectStringType(self):
        return self.__sql_datatype_BinaryLargeObjectStringType

    @sql_datatype_BinaryLargeObjectStringType.setter
    def sql_datatype_BinaryLargeObjectStringType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_datatype_BinaryLargeObjectStringType__sql_datatype_BinaryLargeObjectStringType", None)
        self.__sql_datatype_BinaryLargeObjectStringType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LargeObjectLength"):
                opp_val = getattr(old_value, "LargeObjectLength", None)
                if opp_val == self:
                    setattr(old_value, "LargeObjectLength", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LargeObjectLength"):
                opp_val = getattr(value, "LargeObjectLength", None)
                setattr(value, "LargeObjectLength", self)

class sql_datatype_DatetimeType(PredefinedType):

    pass
class sql_datatype_NumericType(PredefinedType):

    pass
class sql_datatype_CharacterStringType(PredefinedType):

    def __init__(self, kind: str, length: str, sql_datatype_CharacterStringType6: "SchemaQualifiedName" = None, sql_datatype_CharacterStringType: "SchemaQualifiedName" = None):
        self.kind = kind
        self.length = length
        self.sql_datatype_CharacterStringType6 = sql_datatype_CharacterStringType6
        self.sql_datatype_CharacterStringType = sql_datatype_CharacterStringType
        
        pass
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def sql_datatype_CharacterStringType(self):
        return self.__sql_datatype_CharacterStringType

    @sql_datatype_CharacterStringType.setter
    def sql_datatype_CharacterStringType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_datatype_CharacterStringType__sql_datatype_CharacterStringType", None)
        self.__sql_datatype_CharacterStringType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchemaQualifiedName4"):
                opp_val = getattr(old_value, "SchemaQualifiedName4", None)
                if opp_val == self:
                    setattr(old_value, "SchemaQualifiedName4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchemaQualifiedName4"):
                opp_val = getattr(value, "SchemaQualifiedName4", None)
                setattr(value, "SchemaQualifiedName4", self)

    @property
    def sql_datatype_CharacterStringType6(self):
        return self.__sql_datatype_CharacterStringType6

    @sql_datatype_CharacterStringType6.setter
    def sql_datatype_CharacterStringType6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_datatype_CharacterStringType__sql_datatype_CharacterStringType6", None)
        self.__sql_datatype_CharacterStringType6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchemaQualifiedName7"):
                opp_val = getattr(old_value, "SchemaQualifiedName7", None)
                if opp_val == self:
                    setattr(old_value, "SchemaQualifiedName7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchemaQualifiedName7"):
                opp_val = getattr(value, "SchemaQualifiedName7", None)
                setattr(value, "SchemaQualifiedName7", self)

class DataType:

    pass
class sql_datatype_PredefinedType(DataType):

    pass
class sql_datatype_DataType(ABC):

    pass
class sql_datatype_NationalCharacterStringType(PredefinedType):

    def __init__(self, kind: str, length: str, sql_datatype_NationalCharacterStringType: "SchemaQualifiedName" = None):
        self.kind = kind
        self.length = length
        self.sql_datatype_NationalCharacterStringType = sql_datatype_NationalCharacterStringType
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length


    @property
    def sql_datatype_NationalCharacterStringType(self):
        return self.__sql_datatype_NationalCharacterStringType

    @sql_datatype_NationalCharacterStringType.setter
    def sql_datatype_NationalCharacterStringType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_datatype_NationalCharacterStringType__sql_datatype_NationalCharacterStringType", None)
        self.__sql_datatype_NationalCharacterStringType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchemaQualifiedName9"):
                opp_val = getattr(old_value, "SchemaQualifiedName9", None)
                if opp_val == self:
                    setattr(old_value, "SchemaQualifiedName9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchemaQualifiedName9"):
                opp_val = getattr(value, "SchemaQualifiedName9", None)
                setattr(value, "SchemaQualifiedName9", self)

class DatetimeLiteral:

    pass
class sql_literal_TimestampLiteral(DatetimeLiteral):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class sql_literal_TimeLiteral(DatetimeLiteral):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class sql_literal_DateLiteral(DatetimeLiteral):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class NumericLiteral:

    pass
class sql_literal_ApproximateNumericLiteral(NumericLiteral):

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class sql_literal_ExactNumericLiteral(NumericLiteral):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SchemaQualifiedName:

    pass
class NationalCharacterStringLiteral:

    pass
class sql_literal_CharacterStringLiteral(NationalCharacterStringLiteral):

    pass
class Literal:

    pass
class sql_literal_NumericLiteral(Literal):

    pass
class sql_literal_GeneralLiteral(Literal):

    pass
class sql_literal_Literal(ABC):

    pass
class GeneralLiteral:

    pass
class sql_literal_BooleanLiteral(GeneralLiteral):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class sql_literal_DatetimeLiteral(GeneralLiteral):

    pass
class sql_literal_NationalCharacterStringLiteral(GeneralLiteral):

    def __init__(self, values: str, sql_literal_NationalCharacterStringLiteral: set["Separator"] = None):
        self.values = values
        self.sql_literal_NationalCharacterStringLiteral = sql_literal_NationalCharacterStringLiteral if sql_literal_NationalCharacterStringLiteral is not None else set()
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


    @property
    def sql_literal_NationalCharacterStringLiteral(self):
        return self.__sql_literal_NationalCharacterStringLiteral

    @sql_literal_NationalCharacterStringLiteral.setter
    def sql_literal_NationalCharacterStringLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_literal_NationalCharacterStringLiteral__sql_literal_NationalCharacterStringLiteral", None)
        self.__sql_literal_NationalCharacterStringLiteral = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Separator"):
                    opp_val = getattr(item, "Separator", None)
                    
                    if opp_val == self:
                        setattr(item, "Separator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Separator"):
                    opp_val = getattr(item, "Separator", None)
                    
                    setattr(item, "Separator", self)
                    

class Comment:

    pass
class sql_common_BracketedComment(Comment):

    pass
class sql_common_SimpleComment(Comment):

    pass
class Separator:

    pass
class sql_common_Comment(Separator):

    def __init__(self, value: str, Separator: "sql_literal_NationalCharacterStringLiteral" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class sql_common_SchemaQualifiedName:

    def __init__(self, catalogName: str, schemaName: str, name: str):
        self.catalogName = catalogName
        self.schemaName = schemaName
        self.name = name
        
        pass
    @property
    def schemaName(self):
        return self.__schemaName

    @schemaName.setter
    def schemaName(self, schemaName: str):
        self.__schemaName = schemaName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def catalogName(self):
        return self.__catalogName

    @catalogName.setter
    def catalogName(self, catalogName: str):
        self.__catalogName = catalogName


class sql_common_Statement(ABC):

    pass
class sql_Dummy:

    pass
class Statement:

    pass
class sql_common_DirectSQLStatement(Statement):

    pass
class sql_common_Separator(Statement):

    pass
class sql_common_SQLScript:

    pass