from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class UniqueSpecificationKind(Enum):
    UNIQUE = "UNIQUE"
    PRIMARY_KEY = "PRIMARY_KEY"
class ExactNumericTypeKind(Enum):
    NUMERIC = "NUMERIC"
    DECIMAL = "DECIMAL"
    DEC = "DEC"
    SMALLINT = "SMALLINT"
    INTEGER = "INTEGER"
    INT = "INT"
    BIGINT = "BIGINT"
class Multiplier(Enum):
    K = "K"
    M = "M"
    G = "G"
class CharLengthUnits(Enum):
    CHARACTERS = "CHARACTERS"
    CODE_UNITS = "CODE_UNITS"
    OCTETS = "OCTETS"
class ApproximateNumericTypeKind(Enum):
    FLOAT = "FLOAT"
    REAL = "REAL"
    DOUBLE_PRECISION = "DOUBLE_PRECISION"
class TableScope(Enum):
    PERSISTENT = "PERSISTENT"
    GLOBAL_TEMPORARY = "GLOBAL_TEMPORARY"
    LOCAL_TEMPORARY = "LOCAL_TEMPORARY"
class CharacterStringTypeKind(Enum):
    CHARACTER = "CHARACTER"
    CHAR = "CHAR"
    CHARACTER_VARYING = "CHARACTER_VARYING"
    CHAR_VARYING = "CHAR_VARYING"
    VARCHAR = "VARCHAR"
class NationalCharacterStringTypeKind(Enum):
    NATIONAL_CHARACTER = "NATIONAL_CHARACTER"
    NATIONAL_CHAR = "NATIONAL_CHAR"
    NCHAR = "NCHAR"
    NATIONAL_CHARACTER_VARYING = "NATIONAL_CHARACTER_VARYING"
    NATIONAL_CHAR_VARYING = "NATIONAL_CHAR_VARYING"
    NCHAR_VARYING = "NCHAR_VARYING"
class DatetimeValueFunctionKind(Enum):
    CURRENT_DATE = "CURRENT_DATE"
    CURRENT_TIMESTAMP = "CURRENT_TIMESTAMP"
    LOCALTIMESTAMP = "LOCALTIMESTAMP"
    CURRENT_TIME = "CURRENT_TIME"
    LOCALTIME = "LOCALTIME"
class BinaryLargeObjectStringTypeKind(Enum):
    BINARY_LARGE_OBJECT = "BINARY_LARGE_OBJECT"
    BLOB = "BLOB"


############################################
# Definition of Classes
############################################

class TableConstraint:

    pass
class sql_schema_TableColumnsConstraint(TableConstraint):

    pass
class sql_schema_TableReference:

    def __init__(self, catalogName: str, schemaName: str, sql_schema_TableReference: "TableDefinition" = None):
        self.catalogName = catalogName
        self.schemaName = schemaName
        self.sql_schema_TableReference = sql_schema_TableReference
        
    @property
    def catalogName(self) -> str:
        return self.__catalogName

    @catalogName.setter
    def catalogName(self, catalogName: str):
        self.__catalogName = catalogName

    @property
    def schemaName(self) -> str:
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
            if hasattr(old_value, "TableDefinition45"):
                opp_val = getattr(old_value, "TableDefinition45", None)
                if opp_val == self:
                    setattr(old_value, "TableDefinition45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableDefinition45"):
                opp_val = getattr(value, "TableDefinition45", None)
                setattr(value, "TableDefinition45", self)

class TableReference:

    pass
class sql_schema_ReferentialConstraint(ABC):

    pass
class sql_schema_UniqueConstraint(ABC):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class schema_TableColumnsConstraint:

    pass
class DatetimeValueFunction:

    pass
class TableElementList:

    pass
class sql_schema_TableElement(ABC):

    pass
class SQLSchemaStatement:

    pass
class sql_schema_SQLSchemaDefinitionStatement(SQLSchemaStatement):

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
class sql_schema_UniqueTableConstraint(schema_TableColumnsConstraint, schema_UniqueConstraint):

    pass
class sql_schema_UniqueColumnConstraint(schema_ColumnConstraint, schema_UniqueConstraint):

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
class ColumnConstraint:

    pass
class sql_schema_NotNullColumnConstraint(ColumnConstraint):

    pass
class DefaultOption:

    pass
class sql_schema_ImplicitlyTypedValueSpecificationDefaultOption(DefaultOption):

    pass
class sql_schema_DatetimeValueFunctionDefaultOption(DefaultOption):

    pass
class sql_schema_LiteralDefaultOption(DefaultOption):

    pass
class TableElement:

    pass
class sql_schema_Column(TableElement):

    def __init__(self, name: str, sql_schema_Column: "DataType" = None, DefaultOption: "DefaultOption" = None, ColumnConstraint: "ColumnConstraint" = None, sql_schema_Column24: "SchemaQualifiedName" = None, schema15: "sql_schema_TableElementList"):
        self.name = name
        self.sql_schema_Column = sql_schema_Column
        self.DefaultOption = DefaultOption
        self.ColumnConstraint = ColumnConstraint
        self.sql_schema_Column24 = sql_schema_Column24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sql_schema_Column24(self):
        return self.__sql_schema_Column24

    @sql_schema_Column24.setter
    def sql_schema_Column24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_schema_Column__sql_schema_Column24", None)
        self.__sql_schema_Column24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchemaQualifiedName25"):
                opp_val = getattr(old_value, "SchemaQualifiedName25", None)
                if opp_val == self:
                    setattr(old_value, "SchemaQualifiedName25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchemaQualifiedName25"):
                opp_val = getattr(value, "SchemaQualifiedName25", None)
                setattr(value, "SchemaQualifiedName25", self)

    @property
    def DefaultOption(self):
        return self.__DefaultOption

    @DefaultOption.setter
    def DefaultOption(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_schema_Column__DefaultOption", None)
        self.__DefaultOption = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema20"):
                opp_val = getattr(old_value, "schema20", None)
                if opp_val == self:
                    setattr(old_value, "schema20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema20"):
                opp_val = getattr(value, "schema20", None)
                setattr(value, "schema20", self)

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
    def ColumnConstraint(self):
        return self.__ColumnConstraint

    @ColumnConstraint.setter
    def ColumnConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_schema_Column__ColumnConstraint", None)
        self.__ColumnConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema22"):
                opp_val = getattr(old_value, "schema22", None)
                if opp_val == self:
                    setattr(old_value, "schema22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema22"):
                opp_val = getattr(value, "schema22", None)
                setattr(value, "schema22", self)

class TableContentsSource:

    pass
class sql_schema_TableElementList(TableContentsSource):

    pass
class EObject:

    pass
class sql_schema_ColumnConstraint(EObject):

    pass
class sql_schema_TableConstraint(schema_TableElement, EObject):

    pass
class schema_SQLSchemaDefinitionStatement:

    pass
class sql_schema_TableDefinition(schema_SQLSchemaDefinitionStatement, EObject):

    def __init__(self, label: str, scope: str, sql_schema_TableDefinition: "SchemaQualifiedName" = None, TableContentsSource: "TableContentsSource" = None):
        self.label = label
        self.scope = scope
        self.sql_schema_TableDefinition = sql_schema_TableDefinition
        self.TableContentsSource = TableContentsSource
        
    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def TableContentsSource(self):
        return self.__TableContentsSource

    @TableContentsSource.setter
    def TableContentsSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_schema_TableDefinition__TableContentsSource", None)
        self.__TableContentsSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema"):
                opp_val = getattr(old_value, "schema", None)
                if opp_val == self:
                    setattr(old_value, "schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema"):
                opp_val = getattr(value, "schema", None)
                setattr(value, "schema", self)

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

class ImplicitlyTypedValueSpecification:

    pass
class sql_expression_NullSpecification(ImplicitlyTypedValueSpecification):

    pass
class sql_expression_ImplicitlyTypedValueSpecification(ABC):

    pass
class sql_function_DatetimeValueFunction:

    def __init__(self, kind: str, precision: str):
        self.kind = kind
        self.precision = precision
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class DatetimeType:

    pass
class sql_datatype_TimestampType(DatetimeType):

    def __init__(self, precision: str, withTimeZone: str):
        self.precision = precision
        self.withTimeZone = withTimeZone
        
    @property
    def withTimeZone(self) -> str:
        return self.__withTimeZone

    @withTimeZone.setter
    def withTimeZone(self, withTimeZone: str):
        self.__withTimeZone = withTimeZone

    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class sql_datatype_TimeType(DatetimeType):

    def __init__(self, precision: str, withTimeZone: str):
        self.precision = precision
        self.withTimeZone = withTimeZone
        
    @property
    def withTimeZone(self) -> str:
        return self.__withTimeZone

    @withTimeZone.setter
    def withTimeZone(self, withTimeZone: str):
        self.__withTimeZone = withTimeZone

    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class sql_datatype_DateType(DatetimeType):

    pass
class sql_datatype_LargeObjectLength:

    def __init__(self, value: str, multiplier: str, units: str):
        self.value = value
        self.multiplier = multiplier
        self.units = units
        
    @property
    def multiplier(self) -> str:
        return self.__multiplier

    @multiplier.setter
    def multiplier(self, multiplier: str):
        self.__multiplier = multiplier

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def units(self) -> str:
        return self.__units

    @units.setter
    def units(self, units: str):
        self.__units = units

class NumericType:

    pass
class sql_datatype_ApproximateNumericType(NumericType):

    def __init__(self, kind: str, precision: str):
        self.kind = kind
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class sql_datatype_ExactNumericType(NumericType):

    def __init__(self, kind: str, precision: str, scale: str):
        self.kind = kind
        self.precision = precision
        self.scale = scale
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class LargeObjectLength:

    pass
class PredefinedType:

    pass
class sql_datatype_NationalCharacterStringType(PredefinedType):

    def __init__(self, kind: str, length: str, sql_datatype_NationalCharacterStringType: "SchemaQualifiedName" = None):
        self.kind = kind
        self.length = length
        self.sql_datatype_NationalCharacterStringType = sql_datatype_NationalCharacterStringType
        
    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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

class sql_datatype_BooleanType(PredefinedType):

    pass
class sql_datatype_NumericType(PredefinedType):

    pass
class sql_datatype_DatetimeType(PredefinedType):

    pass
class sql_datatype_BinaryLargeObjectStringType(PredefinedType):

    def __init__(self, kind: str, sql_datatype_BinaryLargeObjectStringType: "LargeObjectLength" = None):
        self.kind = kind
        self.sql_datatype_BinaryLargeObjectStringType = sql_datatype_BinaryLargeObjectStringType
        
    @property
    def kind(self) -> str:
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

class sql_datatype_CharacterStringType(PredefinedType):

    def __init__(self, kind: str, length: str, sql_datatype_CharacterStringType: "SchemaQualifiedName" = None, sql_datatype_CharacterStringType6: "SchemaQualifiedName" = None):
        self.kind = kind
        self.length = length
        self.sql_datatype_CharacterStringType = sql_datatype_CharacterStringType
        self.sql_datatype_CharacterStringType6 = sql_datatype_CharacterStringType6
        
    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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

class DataType:

    pass
class sql_datatype_PredefinedType(DataType):

    pass
class sql_datatype_DataType(ABC):

    pass
class NumericLiteral:

    pass
class sql_literal_ApproximateNumericLiteral(NumericLiteral):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class sql_literal_ExactNumericLiteral(NumericLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class DatetimeLiteral:

    pass
class sql_literal_TimestampLiteral(DatetimeLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sql_literal_TimeLiteral(DatetimeLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sql_literal_DateLiteral(DatetimeLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class GeneralLiteral:

    pass
class sql_literal_DatetimeLiteral(GeneralLiteral):

    pass
class sql_literal_BooleanLiteral(GeneralLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sql_literal_NationalCharacterStringLiteral(GeneralLiteral):

    def __init__(self, values: str, sql_literal_NationalCharacterStringLiteral: set["Separator"] = None):
        self.values = values
        self.sql_literal_NationalCharacterStringLiteral = sql_literal_NationalCharacterStringLiteral if sql_literal_NationalCharacterStringLiteral is not None else set()
        
    @property
    def values(self) -> str:
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
class sql_common_SchemaQualifiedName:

    def __init__(self, catalogName: str, schemaName: str, name: str):
        self.catalogName = catalogName
        self.schemaName = schemaName
        self.name = name
        
    @property
    def schemaName(self) -> str:
        return self.__schemaName

    @schemaName.setter
    def schemaName(self, schemaName: str):
        self.__schemaName = schemaName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def catalogName(self) -> str:
        return self.__catalogName

    @catalogName.setter
    def catalogName(self, catalogName: str):
        self.__catalogName = catalogName

class sql_common_Statement(ABC):

    pass
class Comment:

    pass
class sql_common_BracketedComment(Comment):

    pass
class sql_common_SimpleComment(Comment):

    pass
class Separator:

    pass
class sql_common_Comment(Separator):

    def __init__(self, value: str, Separator: "sql_literal_NationalCharacterStringLiteral"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Statement:

    pass
class sql_common_DirectSQLStatement(Statement):

    pass
class sql_common_Separator(Statement):

    pass
class sql_common_SQLScript:

    pass
class sql_Dummy:

    pass