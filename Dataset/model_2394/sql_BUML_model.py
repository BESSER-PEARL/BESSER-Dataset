####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
CharacterStringTypeKind: Enumeration = Enumeration(
    name="CharacterStringTypeKind",
    literals={
            EnumerationLiteral(name="CHARACTER"),
			EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="CHARACTER_VARYING"),
			EnumerationLiteral(name="CHAR_VARYING"),
			EnumerationLiteral(name="VARCHAR")
    }
)

NationalCharacterStringTypeKind: Enumeration = Enumeration(
    name="NationalCharacterStringTypeKind",
    literals={
            EnumerationLiteral(name="NATIONAL_CHARACTER"),
			EnumerationLiteral(name="NATIONAL_CHAR"),
			EnumerationLiteral(name="NCHAR"),
			EnumerationLiteral(name="NATIONAL_CHARACTER_VARYING"),
			EnumerationLiteral(name="NATIONAL_CHAR_VARYING"),
			EnumerationLiteral(name="NCHAR_VARYING")
    }
)

BinaryLargeObjectStringTypeKind: Enumeration = Enumeration(
    name="BinaryLargeObjectStringTypeKind",
    literals={
            EnumerationLiteral(name="BINARY_LARGE_OBJECT"),
			EnumerationLiteral(name="BLOB")
    }
)

ExactNumericTypeKind: Enumeration = Enumeration(
    name="ExactNumericTypeKind",
    literals={
            EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="DEC"),
			EnumerationLiteral(name="SMALLINT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="BIGINT")
    }
)

ApproximateNumericTypeKind: Enumeration = Enumeration(
    name="ApproximateNumericTypeKind",
    literals={
            EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="DOUBLE_PRECISION")
    }
)

Multiplier: Enumeration = Enumeration(
    name="Multiplier",
    literals={
            EnumerationLiteral(name="K"),
			EnumerationLiteral(name="M"),
			EnumerationLiteral(name="G")
    }
)

CharLengthUnits: Enumeration = Enumeration(
    name="CharLengthUnits",
    literals={
            EnumerationLiteral(name="CHARACTERS"),
			EnumerationLiteral(name="CODE_UNITS"),
			EnumerationLiteral(name="OCTETS")
    }
)

DatetimeValueFunctionKind: Enumeration = Enumeration(
    name="DatetimeValueFunctionKind",
    literals={
            EnumerationLiteral(name="CURRENT_DATE"),
			EnumerationLiteral(name="CURRENT_TIMESTAMP"),
			EnumerationLiteral(name="LOCALTIMESTAMP"),
			EnumerationLiteral(name="CURRENT_TIME"),
			EnumerationLiteral(name="LOCALTIME")
    }
)

TableScope: Enumeration = Enumeration(
    name="TableScope",
    literals={
            EnumerationLiteral(name="PERSISTENT"),
			EnumerationLiteral(name="GLOBAL_TEMPORARY"),
			EnumerationLiteral(name="LOCAL_TEMPORARY")
    }
)

UniqueSpecificationKind: Enumeration = Enumeration(
    name="UniqueSpecificationKind",
    literals={
            EnumerationLiteral(name="UNIQUE"),
			EnumerationLiteral(name="PRIMARY_KEY")
    }
)

# Classes
sql_Dummy = Class(name="sql::Dummy")
sql_common_SQLScript = Class(name="sql::common::SQLScript")
Statement = Class(name="Statement")
sql_common_DirectSQLStatement = Class(name="sql::common::DirectSQLStatement", is_abstract=True)
sql_common_Separator = Class(name="sql::common::Separator", is_abstract=True)
sql_common_Comment = Class(name="sql::common::Comment", is_abstract=True)
Separator = Class(name="Separator")
sql_common_SimpleComment = Class(name="sql::common::SimpleComment")
Comment = Class(name="Comment")
sql_common_BracketedComment = Class(name="sql::common::BracketedComment")
sql_common_Statement = Class(name="sql::common::Statement", is_abstract=True)
sql_common_SchemaQualifiedName = Class(name="sql::common::SchemaQualifiedName")
sql_literal_Literal = Class(name="sql::literal::Literal", is_abstract=True)
sql_literal_GeneralLiteral = Class(name="sql::literal::GeneralLiteral", is_abstract=True)
Literal = Class(name="Literal")
sql_literal_CharacterStringLiteral = Class(name="sql::literal::CharacterStringLiteral")
NationalCharacterStringLiteral = Class(name="NationalCharacterStringLiteral")
SchemaQualifiedName = Class(name="SchemaQualifiedName")
sql_literal_NationalCharacterStringLiteral = Class(name="sql::literal::NationalCharacterStringLiteral")
GeneralLiteral = Class(name="GeneralLiteral")
sql_literal_DatetimeLiteral = Class(name="sql::literal::DatetimeLiteral", is_abstract=True)
sql_literal_BooleanLiteral = Class(name="sql::literal::BooleanLiteral")
sql_literal_DateLiteral = Class(name="sql::literal::DateLiteral")
DatetimeLiteral = Class(name="DatetimeLiteral")
sql_literal_TimestampLiteral = Class(name="sql::literal::TimestampLiteral")
sql_literal_ExactNumericLiteral = Class(name="sql::literal::ExactNumericLiteral")
NumericLiteral = Class(name="NumericLiteral")
sql_literal_ApproximateNumericLiteral = Class(name="sql::literal::ApproximateNumericLiteral")
sql_literal_NumericLiteral = Class(name="sql::literal::NumericLiteral", is_abstract=True)
sql_datatype_DataType = Class(name="sql::datatype::DataType", is_abstract=True)
sql_datatype_PredefinedType = Class(name="sql::datatype::PredefinedType", is_abstract=True)
DataType = Class(name="DataType")
sql_datatype_CharacterStringType = Class(name="sql::datatype::CharacterStringType")
PredefinedType = Class(name="PredefinedType")
sql_literal_TimeLiteral = Class(name="sql::literal::TimeLiteral")
sql_datatype_BinaryLargeObjectStringType = Class(name="sql::datatype::BinaryLargeObjectStringType")
LargeObjectLength = Class(name="LargeObjectLength")
sql_datatype_NumericType = Class(name="sql::datatype::NumericType", is_abstract=True)
sql_datatype_BooleanType = Class(name="sql::datatype::BooleanType")
sql_datatype_DatetimeType = Class(name="sql::datatype::DatetimeType", is_abstract=True)
sql_datatype_NationalCharacterStringType = Class(name="sql::datatype::NationalCharacterStringType")
sql_datatype_ExactNumericType = Class(name="sql::datatype::ExactNumericType")
NumericType = Class(name="NumericType")
sql_datatype_ApproximateNumericType = Class(name="sql::datatype::ApproximateNumericType")
sql_datatype_LargeObjectLength = Class(name="sql::datatype::LargeObjectLength")
sql_datatype_DateType = Class(name="sql::datatype::DateType")
DatetimeType = Class(name="DatetimeType")
sql_datatype_TimeType = Class(name="sql::datatype::TimeType")
sql_datatype_TimestampType = Class(name="sql::datatype::TimestampType")
sql_function_DatetimeValueFunction = Class(name="sql::function::DatetimeValueFunction")
sql_expression_ImplicitlyTypedValueSpecification = Class(name="sql::expression::ImplicitlyTypedValueSpecification", is_abstract=True)
sql_expression_NullSpecification = Class(name="sql::expression::NullSpecification")
ImplicitlyTypedValueSpecification = Class(name="ImplicitlyTypedValueSpecification")
sql_schema_TableDefinition = Class(name="sql::schema::TableDefinition")
schema_SQLSchemaDefinitionStatement = Class(name="schema::SQLSchemaDefinitionStatement")
EObject = Class(name="EObject")
TableContentsSource = Class(name="TableContentsSource")
sql_schema_TableElementList = Class(name="sql::schema::TableElementList")
TableElement = Class(name="TableElement")
DefaultOption = Class(name="DefaultOption")
ColumnConstraint = Class(name="ColumnConstraint")
sql_schema_TableConstraint = Class(name="sql::schema::TableConstraint", is_abstract=True)
schema_TableElement = Class(name="schema::TableElement")
sql_schema_TableContentsSource = Class(name="sql::schema::TableContentsSource", is_abstract=True)
TableDefinition = Class(name="TableDefinition")
sql_schema_DefaultOption = Class(name="sql::schema::DefaultOption", is_abstract=True)
Column = Class(name="Column")
sql_schema_ColumnConstraint = Class(name="sql::schema::ColumnConstraint", is_abstract=True)
sql_schema_NotNullColumnConstraint = Class(name="sql::schema::NotNullColumnConstraint")
sql_schema_UniqueColumnConstraint = Class(name="sql::schema::UniqueColumnConstraint")
schema_UniqueConstraint = Class(name="schema::UniqueConstraint")
schema_ColumnConstraint = Class(name="schema::ColumnConstraint")
sql_schema_ReferentialColumnConstraint = Class(name="sql::schema::ReferentialColumnConstraint")
schema_ReferentialConstraint = Class(name="schema::ReferentialConstraint")
sql_schema_SQLSchemaStatement = Class(name="sql::schema::SQLSchemaStatement", is_abstract=True)
DirectSQLStatement = Class(name="DirectSQLStatement")
sql_schema_SQLSchemaDefinitionStatement = Class(name="sql::schema::SQLSchemaDefinitionStatement", is_abstract=True)
SQLSchemaStatement = Class(name="SQLSchemaStatement")
sql_schema_TableElement = Class(name="sql::schema::TableElement", is_abstract=True)
TableElementList = Class(name="TableElementList")
sql_schema_Column = Class(name="sql::schema::Column")
DatetimeValueFunction = Class(name="DatetimeValueFunction")
sql_schema_ImplicitlyTypedValueSpecificationDefaultOption = Class(name="sql::schema::ImplicitlyTypedValueSpecificationDefaultOption")
sql_schema_UniqueTableConstraint = Class(name="sql::schema::UniqueTableConstraint")
schema_TableColumnsConstraint = Class(name="schema::TableColumnsConstraint")
sql_schema_ReferentialTableConstraint = Class(name="sql::schema::ReferentialTableConstraint")
sql_schema_UniqueConstraint = Class(name="sql::schema::UniqueConstraint", is_abstract=True)
sql_schema_ReferentialConstraint = Class(name="sql::schema::ReferentialConstraint", is_abstract=True)
TableReference = Class(name="TableReference")
sql_schema_TableReference = Class(name="sql::schema::TableReference")
sql_schema_LiteralDefaultOption = Class(name="sql::schema::LiteralDefaultOption")
sql_schema_DatetimeValueFunctionDefaultOption = Class(name="sql::schema::DatetimeValueFunctionDefaultOption")
sql_schema_TableColumnsConstraint = Class(name="sql::schema::TableColumnsConstraint", is_abstract=True)
TableConstraint = Class(name="TableConstraint")

# sql_Dummy class attributes and methods

# sql_common_SQLScript class attributes and methods

# Statement class attributes and methods

# sql_common_DirectSQLStatement class attributes and methods

# sql_common_Separator class attributes and methods

# sql_common_Comment class attributes and methods
sql_common_Comment_value: Property = Property(name="value", type=StringType)
sql_common_Comment.attributes={sql_common_Comment_value}

# Separator class attributes and methods

# sql_common_SimpleComment class attributes and methods

# Comment class attributes and methods

# sql_common_BracketedComment class attributes and methods

# sql_common_Statement class attributes and methods

# sql_common_SchemaQualifiedName class attributes and methods
sql_common_SchemaQualifiedName_catalogName: Property = Property(name="catalogName", type=StringType)
sql_common_SchemaQualifiedName_schemaName: Property = Property(name="schemaName", type=StringType)
sql_common_SchemaQualifiedName_name: Property = Property(name="name", type=StringType)
sql_common_SchemaQualifiedName.attributes={sql_common_SchemaQualifiedName_schemaName, sql_common_SchemaQualifiedName_name, sql_common_SchemaQualifiedName_catalogName}

# sql_literal_Literal class attributes and methods

# sql_literal_GeneralLiteral class attributes and methods

# Literal class attributes and methods

# sql_literal_CharacterStringLiteral class attributes and methods

# NationalCharacterStringLiteral class attributes and methods

# SchemaQualifiedName class attributes and methods

# sql_literal_NationalCharacterStringLiteral class attributes and methods
sql_literal_NationalCharacterStringLiteral_values: Property = Property(name="values", type=StringType)
sql_literal_NationalCharacterStringLiteral.attributes={sql_literal_NationalCharacterStringLiteral_values}

# GeneralLiteral class attributes and methods

# sql_literal_DatetimeLiteral class attributes and methods

# sql_literal_BooleanLiteral class attributes and methods
sql_literal_BooleanLiteral_value: Property = Property(name="value", type=StringType)
sql_literal_BooleanLiteral.attributes={sql_literal_BooleanLiteral_value}

# sql_literal_DateLiteral class attributes and methods
sql_literal_DateLiteral_value: Property = Property(name="value", type=StringType)
sql_literal_DateLiteral.attributes={sql_literal_DateLiteral_value}

# DatetimeLiteral class attributes and methods

# sql_literal_TimestampLiteral class attributes and methods
sql_literal_TimestampLiteral_value: Property = Property(name="value", type=StringType)
sql_literal_TimestampLiteral.attributes={sql_literal_TimestampLiteral_value}

# sql_literal_ExactNumericLiteral class attributes and methods
sql_literal_ExactNumericLiteral_value: Property = Property(name="value", type=StringType)
sql_literal_ExactNumericLiteral.attributes={sql_literal_ExactNumericLiteral_value}

# NumericLiteral class attributes and methods

# sql_literal_ApproximateNumericLiteral class attributes and methods
sql_literal_ApproximateNumericLiteral_value: Property = Property(name="value", type=FloatType)
sql_literal_ApproximateNumericLiteral.attributes={sql_literal_ApproximateNumericLiteral_value}

# sql_literal_NumericLiteral class attributes and methods

# sql_datatype_DataType class attributes and methods

# sql_datatype_PredefinedType class attributes and methods

# DataType class attributes and methods

# sql_datatype_CharacterStringType class attributes and methods
sql_datatype_CharacterStringType_kind: Property = Property(name="kind", type=StringType)
sql_datatype_CharacterStringType_length: Property = Property(name="length", type=StringType)
sql_datatype_CharacterStringType.attributes={sql_datatype_CharacterStringType_length, sql_datatype_CharacterStringType_kind}

# PredefinedType class attributes and methods

# sql_literal_TimeLiteral class attributes and methods
sql_literal_TimeLiteral_value: Property = Property(name="value", type=StringType)
sql_literal_TimeLiteral.attributes={sql_literal_TimeLiteral_value}

# sql_datatype_BinaryLargeObjectStringType class attributes and methods
sql_datatype_BinaryLargeObjectStringType_kind: Property = Property(name="kind", type=StringType)
sql_datatype_BinaryLargeObjectStringType.attributes={sql_datatype_BinaryLargeObjectStringType_kind}

# LargeObjectLength class attributes and methods

# sql_datatype_NumericType class attributes and methods

# sql_datatype_BooleanType class attributes and methods

# sql_datatype_DatetimeType class attributes and methods

# sql_datatype_NationalCharacterStringType class attributes and methods
sql_datatype_NationalCharacterStringType_kind: Property = Property(name="kind", type=StringType)
sql_datatype_NationalCharacterStringType_length: Property = Property(name="length", type=StringType)
sql_datatype_NationalCharacterStringType.attributes={sql_datatype_NationalCharacterStringType_length, sql_datatype_NationalCharacterStringType_kind}

# sql_datatype_ExactNumericType class attributes and methods
sql_datatype_ExactNumericType_kind: Property = Property(name="kind", type=StringType)
sql_datatype_ExactNumericType_precision: Property = Property(name="precision", type=StringType)
sql_datatype_ExactNumericType_scale: Property = Property(name="scale", type=StringType)
sql_datatype_ExactNumericType.attributes={sql_datatype_ExactNumericType_precision, sql_datatype_ExactNumericType_scale, sql_datatype_ExactNumericType_kind}

# NumericType class attributes and methods

# sql_datatype_ApproximateNumericType class attributes and methods
sql_datatype_ApproximateNumericType_kind: Property = Property(name="kind", type=StringType)
sql_datatype_ApproximateNumericType_precision: Property = Property(name="precision", type=StringType)
sql_datatype_ApproximateNumericType.attributes={sql_datatype_ApproximateNumericType_precision, sql_datatype_ApproximateNumericType_kind}

# sql_datatype_LargeObjectLength class attributes and methods
sql_datatype_LargeObjectLength_value: Property = Property(name="value", type=StringType)
sql_datatype_LargeObjectLength_multiplier: Property = Property(name="multiplier", type=StringType)
sql_datatype_LargeObjectLength_units: Property = Property(name="units", type=StringType)
sql_datatype_LargeObjectLength.attributes={sql_datatype_LargeObjectLength_multiplier, sql_datatype_LargeObjectLength_value, sql_datatype_LargeObjectLength_units}

# sql_datatype_DateType class attributes and methods

# DatetimeType class attributes and methods

# sql_datatype_TimeType class attributes and methods
sql_datatype_TimeType_precision: Property = Property(name="precision", type=StringType)
sql_datatype_TimeType_withTimeZone: Property = Property(name="withTimeZone", type=StringType)
sql_datatype_TimeType.attributes={sql_datatype_TimeType_withTimeZone, sql_datatype_TimeType_precision}

# sql_datatype_TimestampType class attributes and methods
sql_datatype_TimestampType_precision: Property = Property(name="precision", type=StringType)
sql_datatype_TimestampType_withTimeZone: Property = Property(name="withTimeZone", type=StringType)
sql_datatype_TimestampType.attributes={sql_datatype_TimestampType_withTimeZone, sql_datatype_TimestampType_precision}

# sql_function_DatetimeValueFunction class attributes and methods
sql_function_DatetimeValueFunction_kind: Property = Property(name="kind", type=StringType)
sql_function_DatetimeValueFunction_precision: Property = Property(name="precision", type=StringType)
sql_function_DatetimeValueFunction.attributes={sql_function_DatetimeValueFunction_kind, sql_function_DatetimeValueFunction_precision}

# sql_expression_ImplicitlyTypedValueSpecification class attributes and methods

# sql_expression_NullSpecification class attributes and methods

# ImplicitlyTypedValueSpecification class attributes and methods

# sql_schema_TableDefinition class attributes and methods
sql_schema_TableDefinition_label: Property = Property(name="label", type=StringType)
sql_schema_TableDefinition_scope: Property = Property(name="scope", type=StringType)
sql_schema_TableDefinition.attributes={sql_schema_TableDefinition_scope, sql_schema_TableDefinition_label}

# schema_SQLSchemaDefinitionStatement class attributes and methods

# EObject class attributes and methods

# TableContentsSource class attributes and methods

# sql_schema_TableElementList class attributes and methods

# TableElement class attributes and methods

# DefaultOption class attributes and methods

# ColumnConstraint class attributes and methods

# sql_schema_TableConstraint class attributes and methods

# schema_TableElement class attributes and methods

# sql_schema_TableContentsSource class attributes and methods

# TableDefinition class attributes and methods

# sql_schema_DefaultOption class attributes and methods

# Column class attributes and methods

# sql_schema_ColumnConstraint class attributes and methods

# sql_schema_NotNullColumnConstraint class attributes and methods

# sql_schema_UniqueColumnConstraint class attributes and methods

# schema_UniqueConstraint class attributes and methods

# schema_ColumnConstraint class attributes and methods

# sql_schema_ReferentialColumnConstraint class attributes and methods

# schema_ReferentialConstraint class attributes and methods

# sql_schema_SQLSchemaStatement class attributes and methods

# DirectSQLStatement class attributes and methods

# sql_schema_SQLSchemaDefinitionStatement class attributes and methods

# SQLSchemaStatement class attributes and methods

# sql_schema_TableElement class attributes and methods

# TableElementList class attributes and methods

# sql_schema_Column class attributes and methods
sql_schema_Column_name: Property = Property(name="name", type=StringType)
sql_schema_Column.attributes={sql_schema_Column_name}

# DatetimeValueFunction class attributes and methods

# sql_schema_ImplicitlyTypedValueSpecificationDefaultOption class attributes and methods

# sql_schema_UniqueTableConstraint class attributes and methods

# schema_TableColumnsConstraint class attributes and methods

# sql_schema_ReferentialTableConstraint class attributes and methods

# sql_schema_UniqueConstraint class attributes and methods
sql_schema_UniqueConstraint_kind: Property = Property(name="kind", type=StringType)
sql_schema_UniqueConstraint.attributes={sql_schema_UniqueConstraint_kind}

# sql_schema_ReferentialConstraint class attributes and methods

# TableReference class attributes and methods

# sql_schema_TableReference class attributes and methods
sql_schema_TableReference_catalogName: Property = Property(name="catalogName", type=StringType)
sql_schema_TableReference_schemaName: Property = Property(name="schemaName", type=StringType)
sql_schema_TableReference.attributes={sql_schema_TableReference_catalogName, sql_schema_TableReference_schemaName}

# sql_schema_LiteralDefaultOption class attributes and methods

# sql_schema_DatetimeValueFunctionDefaultOption class attributes and methods

# sql_schema_TableColumnsConstraint class attributes and methods

# TableConstraint class attributes and methods

# Relationships
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="Statement", type=sql_common_SQLScript, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_common_SQLScript", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
characterSetName1: BinaryAssociation = BinaryAssociation(
    name="characterSetName1",
    ends={
        Property(name="SchemaQualifiedName", type=sql_literal_CharacterStringLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_literal_CharacterStringLiteral", type=SchemaQualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
separators2: BinaryAssociation = BinaryAssociation(
    name="separators2",
    ends={
        Property(name="Separator", type=sql_literal_NationalCharacterStringLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_literal_NationalCharacterStringLiteral", type=Separator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
characterSetName3: BinaryAssociation = BinaryAssociation(
    name="characterSetName3",
    ends={
        Property(name="SchemaQualifiedName4", type=sql_datatype_CharacterStringType, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_datatype_CharacterStringType", type=SchemaQualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collationName5: BinaryAssociation = BinaryAssociation(
    name="collationName5",
    ends={
        Property(name="SchemaQualifiedName7", type=sql_datatype_CharacterStringType, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_datatype_CharacterStringType6", type=SchemaQualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collationName8: BinaryAssociation = BinaryAssociation(
    name="collationName8",
    ends={
        Property(name="SchemaQualifiedName9", type=sql_datatype_NationalCharacterStringType, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_datatype_NationalCharacterStringType", type=SchemaQualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
length10: BinaryAssociation = BinaryAssociation(
    name="length10",
    ends={
        Property(name="LargeObjectLength", type=sql_datatype_BinaryLargeObjectStringType, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_datatype_BinaryLargeObjectStringType", type=LargeObjectLength, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemaQualifiedName11: BinaryAssociation = BinaryAssociation(
    name="schemaQualifiedName11",
    ends={
        Property(name="SchemaQualifiedName12", type=sql_schema_TableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_TableDefinition", type=SchemaQualifiedName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contentsSource13: BinaryAssociation = BinaryAssociation(
    name="contentsSource13",
    ends={
        Property(name="schema", type=sql_schema_TableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TableContentsSource", type=TableContentsSource, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements14: BinaryAssociation = BinaryAssociation(
    name="elements14",
    ends={
        Property(name="schema15", type=sql_schema_TableElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="TableElement", type=TableElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dataType18: BinaryAssociation = BinaryAssociation(
    name="dataType18",
    ends={
        Property(name="DataType", type=sql_schema_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_Column", type=DataType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defaultOption19: BinaryAssociation = BinaryAssociation(
    name="defaultOption19",
    ends={
        Property(name="schema20", type=sql_schema_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="DefaultOption", type=DefaultOption, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint21: BinaryAssociation = BinaryAssociation(
    name="constraint21",
    ends={
        Property(name="schema22", type=sql_schema_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ColumnConstraint", type=ColumnConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collationName23: BinaryAssociation = BinaryAssociation(
    name="collationName23",
    ends={
        Property(name="SchemaQualifiedName25", type=sql_schema_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_Column24", type=SchemaQualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemaQualifiedName26: BinaryAssociation = BinaryAssociation(
    name="schemaQualifiedName26",
    ends={
        Property(name="SchemaQualifiedName27", type=sql_schema_TableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_TableConstraint", type=SchemaQualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner28: BinaryAssociation = BinaryAssociation(
    name="owner28",
    ends={
        Property(name="schema29", type=sql_schema_TableContentsSource, multiplicity=Multiplicity(1, 1)),
        Property(name="TableDefinition", type=TableDefinition, multiplicity=Multiplicity(1, 1))
    }
)
owner30: BinaryAssociation = BinaryAssociation(
    name="owner30",
    ends={
        Property(name="schema31", type=sql_schema_DefaultOption, multiplicity=Multiplicity(1, 1)),
        Property(name="Column", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
owner32: BinaryAssociation = BinaryAssociation(
    name="owner32",
    ends={
        Property(name="schema34", type=sql_schema_ColumnConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Column33", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
schemaQualifiedName35: BinaryAssociation = BinaryAssociation(
    name="schemaQualifiedName35",
    ends={
        Property(name="SchemaQualifiedName36", type=sql_schema_ColumnConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_ColumnConstraint", type=SchemaQualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner16: BinaryAssociation = BinaryAssociation(
    name="owner16",
    ends={
        Property(name="schema17", type=sql_schema_TableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TableElementList", type=TableElementList, multiplicity=Multiplicity(1, 1))
    }
)
function38: BinaryAssociation = BinaryAssociation(
    name="function38",
    ends={
        Property(name="DatetimeValueFunction", type=sql_schema_DatetimeValueFunctionDefaultOption, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_DatetimeValueFunctionDefaultOption", type=DatetimeValueFunction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
specification39: BinaryAssociation = BinaryAssociation(
    name="specification39",
    ends={
        Property(name="ImplicitlyTypedValueSpecification", type=sql_schema_ImplicitlyTypedValueSpecificationDefaultOption, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_ImplicitlyTypedValueSpecificationDefaultOption", type=ImplicitlyTypedValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referencedColumns40: BinaryAssociation = BinaryAssociation(
    name="referencedColumns40",
    ends={
        Property(name="Column41", type=sql_schema_ReferentialConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_ReferentialConstraint", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
referencedTable42: BinaryAssociation = BinaryAssociation(
    name="referencedTable42",
    ends={
        Property(name="TableReference", type=sql_schema_ReferentialConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_ReferentialConstraint43", type=TableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literal37: BinaryAssociation = BinaryAssociation(
    name="literal37",
    ends={
        Property(name="Literal", type=sql_schema_LiteralDefaultOption, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_LiteralDefaultOption", type=Literal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target44: BinaryAssociation = BinaryAssociation(
    name="target44",
    ends={
        Property(name="TableDefinition45", type=sql_schema_TableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_TableReference", type=TableDefinition, multiplicity=Multiplicity(1, 1))
    }
)
columns46: BinaryAssociation = BinaryAssociation(
    name="columns46",
    ends={
        Property(name="Column47", type=sql_schema_TableColumnsConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_schema_TableColumnsConstraint", type=Column, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_sql_common_DirectSQLStatement_Statement = Generalization(general=Statement, specific=sql_common_DirectSQLStatement)
gen_sql_common_Separator_Statement = Generalization(general=Statement, specific=sql_common_Separator)
gen_sql_common_Comment_Separator = Generalization(general=Separator, specific=sql_common_Comment)
gen_sql_common_SimpleComment_Comment = Generalization(general=Comment, specific=sql_common_SimpleComment)
gen_sql_common_BracketedComment_Comment = Generalization(general=Comment, specific=sql_common_BracketedComment)
gen_sql_literal_GeneralLiteral_Literal = Generalization(general=Literal, specific=sql_literal_GeneralLiteral)
gen_sql_literal_CharacterStringLiteral_NationalCharacterStringLiteral = Generalization(general=NationalCharacterStringLiteral, specific=sql_literal_CharacterStringLiteral)
gen_sql_literal_NationalCharacterStringLiteral_GeneralLiteral = Generalization(general=GeneralLiteral, specific=sql_literal_NationalCharacterStringLiteral)
gen_sql_literal_DatetimeLiteral_GeneralLiteral = Generalization(general=GeneralLiteral, specific=sql_literal_DatetimeLiteral)
gen_sql_literal_BooleanLiteral_GeneralLiteral = Generalization(general=GeneralLiteral, specific=sql_literal_BooleanLiteral)
gen_sql_literal_DateLiteral_DatetimeLiteral = Generalization(general=DatetimeLiteral, specific=sql_literal_DateLiteral)
gen_sql_literal_TimestampLiteral_DatetimeLiteral = Generalization(general=DatetimeLiteral, specific=sql_literal_TimestampLiteral)
gen_sql_literal_ExactNumericLiteral_NumericLiteral = Generalization(general=NumericLiteral, specific=sql_literal_ExactNumericLiteral)
gen_sql_literal_ApproximateNumericLiteral_NumericLiteral = Generalization(general=NumericLiteral, specific=sql_literal_ApproximateNumericLiteral)
gen_sql_literal_NumericLiteral_Literal = Generalization(general=Literal, specific=sql_literal_NumericLiteral)
gen_sql_datatype_PredefinedType_DataType = Generalization(general=DataType, specific=sql_datatype_PredefinedType)
gen_sql_datatype_CharacterStringType_PredefinedType = Generalization(general=PredefinedType, specific=sql_datatype_CharacterStringType)
gen_sql_literal_TimeLiteral_DatetimeLiteral = Generalization(general=DatetimeLiteral, specific=sql_literal_TimeLiteral)
gen_sql_datatype_BinaryLargeObjectStringType_PredefinedType = Generalization(general=PredefinedType, specific=sql_datatype_BinaryLargeObjectStringType)
gen_sql_datatype_NumericType_PredefinedType = Generalization(general=PredefinedType, specific=sql_datatype_NumericType)
gen_sql_datatype_BooleanType_PredefinedType = Generalization(general=PredefinedType, specific=sql_datatype_BooleanType)
gen_sql_datatype_DatetimeType_PredefinedType = Generalization(general=PredefinedType, specific=sql_datatype_DatetimeType)
gen_sql_datatype_NationalCharacterStringType_PredefinedType = Generalization(general=PredefinedType, specific=sql_datatype_NationalCharacterStringType)
gen_sql_datatype_ExactNumericType_NumericType = Generalization(general=NumericType, specific=sql_datatype_ExactNumericType)
gen_sql_datatype_ApproximateNumericType_NumericType = Generalization(general=NumericType, specific=sql_datatype_ApproximateNumericType)
gen_sql_datatype_DateType_DatetimeType = Generalization(general=DatetimeType, specific=sql_datatype_DateType)
gen_sql_datatype_TimeType_DatetimeType = Generalization(general=DatetimeType, specific=sql_datatype_TimeType)
gen_sql_datatype_TimestampType_DatetimeType = Generalization(general=DatetimeType, specific=sql_datatype_TimestampType)
gen_sql_expression_NullSpecification_ImplicitlyTypedValueSpecification = Generalization(general=ImplicitlyTypedValueSpecification, specific=sql_expression_NullSpecification)
gen_sql_schema_TableDefinition_schema_SQLSchemaDefinitionStatement = Generalization(general=schema_SQLSchemaDefinitionStatement, specific=sql_schema_TableDefinition)
gen_sql_schema_TableDefinition_EObject = Generalization(general=EObject, specific=sql_schema_TableDefinition)
gen_sql_schema_TableElementList_TableContentsSource = Generalization(general=TableContentsSource, specific=sql_schema_TableElementList)
gen_sql_schema_TableConstraint_schema_TableElement = Generalization(general=schema_TableElement, specific=sql_schema_TableConstraint)
gen_sql_schema_TableConstraint_EObject = Generalization(general=EObject, specific=sql_schema_TableConstraint)
gen_sql_schema_ColumnConstraint_EObject = Generalization(general=EObject, specific=sql_schema_ColumnConstraint)
gen_sql_schema_NotNullColumnConstraint_ColumnConstraint = Generalization(general=ColumnConstraint, specific=sql_schema_NotNullColumnConstraint)
gen_sql_schema_UniqueColumnConstraint_schema_UniqueConstraint = Generalization(general=schema_UniqueConstraint, specific=sql_schema_UniqueColumnConstraint)
gen_sql_schema_UniqueColumnConstraint_schema_ColumnConstraint = Generalization(general=schema_ColumnConstraint, specific=sql_schema_UniqueColumnConstraint)
gen_sql_schema_ReferentialColumnConstraint_schema_ReferentialConstraint = Generalization(general=schema_ReferentialConstraint, specific=sql_schema_ReferentialColumnConstraint)
gen_sql_schema_ReferentialColumnConstraint_schema_ColumnConstraint = Generalization(general=schema_ColumnConstraint, specific=sql_schema_ReferentialColumnConstraint)
gen_sql_schema_SQLSchemaStatement_DirectSQLStatement = Generalization(general=DirectSQLStatement, specific=sql_schema_SQLSchemaStatement)
gen_sql_schema_SQLSchemaDefinitionStatement_SQLSchemaStatement = Generalization(general=SQLSchemaStatement, specific=sql_schema_SQLSchemaDefinitionStatement)
gen_sql_schema_Column_TableElement = Generalization(general=TableElement, specific=sql_schema_Column)
gen_sql_schema_ImplicitlyTypedValueSpecificationDefaultOption_DefaultOption = Generalization(general=DefaultOption, specific=sql_schema_ImplicitlyTypedValueSpecificationDefaultOption)
gen_sql_schema_UniqueTableConstraint_schema_UniqueConstraint = Generalization(general=schema_UniqueConstraint, specific=sql_schema_UniqueTableConstraint)
gen_sql_schema_UniqueTableConstraint_schema_TableColumnsConstraint = Generalization(general=schema_TableColumnsConstraint, specific=sql_schema_UniqueTableConstraint)
gen_sql_schema_ReferentialTableConstraint_schema_ReferentialConstraint = Generalization(general=schema_ReferentialConstraint, specific=sql_schema_ReferentialTableConstraint)
gen_sql_schema_ReferentialTableConstraint_schema_TableColumnsConstraint = Generalization(general=schema_TableColumnsConstraint, specific=sql_schema_ReferentialTableConstraint)
gen_sql_schema_LiteralDefaultOption_DefaultOption = Generalization(general=DefaultOption, specific=sql_schema_LiteralDefaultOption)
gen_sql_schema_DatetimeValueFunctionDefaultOption_DefaultOption = Generalization(general=DefaultOption, specific=sql_schema_DatetimeValueFunctionDefaultOption)
gen_sql_schema_TableColumnsConstraint_TableConstraint = Generalization(general=TableConstraint, specific=sql_schema_TableColumnsConstraint)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_Dummy, sql_common_SQLScript, Statement, sql_common_DirectSQLStatement, sql_common_Separator, sql_common_Comment, Separator, sql_common_SimpleComment, Comment, sql_common_BracketedComment, sql_common_Statement, sql_common_SchemaQualifiedName, sql_literal_Literal, sql_literal_GeneralLiteral, Literal, sql_literal_CharacterStringLiteral, NationalCharacterStringLiteral, SchemaQualifiedName, sql_literal_NationalCharacterStringLiteral, GeneralLiteral, sql_literal_DatetimeLiteral, sql_literal_BooleanLiteral, sql_literal_DateLiteral, DatetimeLiteral, sql_literal_TimestampLiteral, sql_literal_ExactNumericLiteral, NumericLiteral, sql_literal_ApproximateNumericLiteral, sql_literal_NumericLiteral, sql_datatype_DataType, sql_datatype_PredefinedType, DataType, sql_datatype_CharacterStringType, PredefinedType, sql_literal_TimeLiteral, sql_datatype_BinaryLargeObjectStringType, LargeObjectLength, sql_datatype_NumericType, sql_datatype_BooleanType, sql_datatype_DatetimeType, sql_datatype_NationalCharacterStringType, sql_datatype_ExactNumericType, NumericType, sql_datatype_ApproximateNumericType, sql_datatype_LargeObjectLength, sql_datatype_DateType, DatetimeType, sql_datatype_TimeType, sql_datatype_TimestampType, sql_function_DatetimeValueFunction, sql_expression_ImplicitlyTypedValueSpecification, sql_expression_NullSpecification, ImplicitlyTypedValueSpecification, sql_schema_TableDefinition, schema_SQLSchemaDefinitionStatement, EObject, TableContentsSource, sql_schema_TableElementList, TableElement, DefaultOption, ColumnConstraint, sql_schema_TableConstraint, schema_TableElement, sql_schema_TableContentsSource, TableDefinition, sql_schema_DefaultOption, Column, sql_schema_ColumnConstraint, sql_schema_NotNullColumnConstraint, sql_schema_UniqueColumnConstraint, schema_UniqueConstraint, schema_ColumnConstraint, sql_schema_ReferentialColumnConstraint, schema_ReferentialConstraint, sql_schema_SQLSchemaStatement, DirectSQLStatement, sql_schema_SQLSchemaDefinitionStatement, SQLSchemaStatement, sql_schema_TableElement, TableElementList, sql_schema_Column, DatetimeValueFunction, sql_schema_ImplicitlyTypedValueSpecificationDefaultOption, sql_schema_UniqueTableConstraint, schema_TableColumnsConstraint, sql_schema_ReferentialTableConstraint, sql_schema_UniqueConstraint, sql_schema_ReferentialConstraint, TableReference, sql_schema_TableReference, sql_schema_LiteralDefaultOption, sql_schema_DatetimeValueFunctionDefaultOption, sql_schema_TableColumnsConstraint, TableConstraint, CharacterStringTypeKind, NationalCharacterStringTypeKind, BinaryLargeObjectStringTypeKind, ExactNumericTypeKind, ApproximateNumericTypeKind, Multiplier, CharLengthUnits, DatetimeValueFunctionKind, TableScope, UniqueSpecificationKind},
    associations={statements0, characterSetName1, separators2, characterSetName3, collationName5, collationName8, length10, schemaQualifiedName11, contentsSource13, elements14, dataType18, defaultOption19, constraint21, collationName23, schemaQualifiedName26, owner28, owner30, owner32, schemaQualifiedName35, owner16, function38, specification39, referencedColumns40, referencedTable42, literal37, target44, columns46},
    generalizations={gen_sql_common_DirectSQLStatement_Statement, gen_sql_common_Separator_Statement, gen_sql_common_Comment_Separator, gen_sql_common_SimpleComment_Comment, gen_sql_common_BracketedComment_Comment, gen_sql_literal_GeneralLiteral_Literal, gen_sql_literal_CharacterStringLiteral_NationalCharacterStringLiteral, gen_sql_literal_NationalCharacterStringLiteral_GeneralLiteral, gen_sql_literal_DatetimeLiteral_GeneralLiteral, gen_sql_literal_BooleanLiteral_GeneralLiteral, gen_sql_literal_DateLiteral_DatetimeLiteral, gen_sql_literal_TimestampLiteral_DatetimeLiteral, gen_sql_literal_ExactNumericLiteral_NumericLiteral, gen_sql_literal_ApproximateNumericLiteral_NumericLiteral, gen_sql_literal_NumericLiteral_Literal, gen_sql_datatype_PredefinedType_DataType, gen_sql_datatype_CharacterStringType_PredefinedType, gen_sql_literal_TimeLiteral_DatetimeLiteral, gen_sql_datatype_BinaryLargeObjectStringType_PredefinedType, gen_sql_datatype_NumericType_PredefinedType, gen_sql_datatype_BooleanType_PredefinedType, gen_sql_datatype_DatetimeType_PredefinedType, gen_sql_datatype_NationalCharacterStringType_PredefinedType, gen_sql_datatype_ExactNumericType_NumericType, gen_sql_datatype_ApproximateNumericType_NumericType, gen_sql_datatype_DateType_DatetimeType, gen_sql_datatype_TimeType_DatetimeType, gen_sql_datatype_TimestampType_DatetimeType, gen_sql_expression_NullSpecification_ImplicitlyTypedValueSpecification, gen_sql_schema_TableDefinition_schema_SQLSchemaDefinitionStatement, gen_sql_schema_TableDefinition_EObject, gen_sql_schema_TableElementList_TableContentsSource, gen_sql_schema_TableConstraint_schema_TableElement, gen_sql_schema_TableConstraint_EObject, gen_sql_schema_ColumnConstraint_EObject, gen_sql_schema_NotNullColumnConstraint_ColumnConstraint, gen_sql_schema_UniqueColumnConstraint_schema_UniqueConstraint, gen_sql_schema_UniqueColumnConstraint_schema_ColumnConstraint, gen_sql_schema_ReferentialColumnConstraint_schema_ReferentialConstraint, gen_sql_schema_ReferentialColumnConstraint_schema_ColumnConstraint, gen_sql_schema_SQLSchemaStatement_DirectSQLStatement, gen_sql_schema_SQLSchemaDefinitionStatement_SQLSchemaStatement, gen_sql_schema_Column_TableElement, gen_sql_schema_ImplicitlyTypedValueSpecificationDefaultOption_DefaultOption, gen_sql_schema_UniqueTableConstraint_schema_UniqueConstraint, gen_sql_schema_UniqueTableConstraint_schema_TableColumnsConstraint, gen_sql_schema_ReferentialTableConstraint_schema_ReferentialConstraint, gen_sql_schema_ReferentialTableConstraint_schema_TableColumnsConstraint, gen_sql_schema_LiteralDefaultOption_DefaultOption, gen_sql_schema_DatetimeValueFunctionDefaultOption_DefaultOption, gen_sql_schema_TableColumnsConstraint_TableConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)