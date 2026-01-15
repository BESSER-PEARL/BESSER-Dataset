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
BinaryStringTypes: Enumeration = Enumeration(
    name="BinaryStringTypes",
    literals={
            EnumerationLiteral(name="BINARYLARGEOBJECT"),
			EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="BINARYVARYING")
    }
)

CharacterStringTypes: Enumeration = Enumeration(
    name="CharacterStringTypes",
    literals={
            EnumerationLiteral(name="CHARACTER"),
			EnumerationLiteral(name="CHARACTERVARYING"),
			EnumerationLiteral(name="CHARACTERLARGEOBJECT")
    }
)

BooleanTypes: Enumeration = Enumeration(
    name="BooleanTypes",
    literals={
            EnumerationLiteral(name="BOOLEAN")
    }
)

DatetimeFeatures: Enumeration = Enumeration(
    name="DatetimeFeatures",
    literals={
            EnumerationLiteral(name="precision")
    }
)

DatetimeTypes: Enumeration = Enumeration(
    name="DatetimeTypes",
    literals={
            EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="TIMEWITHTIMEZONE"),
			EnumerationLiteral(name="TIMEWITHOUTTIMEZONE"),
			EnumerationLiteral(name="TIMESTAMPWITHOUTTIMEZONE"),
			EnumerationLiteral(name="TIMESTAMPWITHTIMEZONE")
    }
)

IntervalTypes: Enumeration = Enumeration(
    name="IntervalTypes",
    literals={
            EnumerationLiteral(name="YEAR_MONTH"),
			EnumerationLiteral(name="DAY_HOUR"),
			EnumerationLiteral(name="DAY_MINUTE"),
			EnumerationLiteral(name="DAY_SECOND"),
			EnumerationLiteral(name="HOUR_MINUTE"),
			EnumerationLiteral(name="HOUR_SECOND"),
			EnumerationLiteral(name="MINUTE_SECOND"),
			EnumerationLiteral(name="YEAR"),
			EnumerationLiteral(name="MONTH"),
			EnumerationLiteral(name="DAY"),
			EnumerationLiteral(name="HOUR"),
			EnumerationLiteral(name="MINUTE"),
			EnumerationLiteral(name="SECOND")
    }
)

IntervalFeatures: Enumeration = Enumeration(
    name="IntervalFeatures",
    literals={
            EnumerationLiteral(name="second_precision"),
			EnumerationLiteral(name="start_leading_precision"),
			EnumerationLiteral(name="end_leading_precision"),
			EnumerationLiteral(name="leading_precision")
    }
)

MatchTypes: Enumeration = Enumeration(
    name="MatchTypes",
    literals={
            EnumerationLiteral(name="SIMPLE"),
			EnumerationLiteral(name="PARTIAL"),
			EnumerationLiteral(name="TOTAL")
    }
)

NumericRadix: Enumeration = Enumeration(
    name="NumericRadix",
    literals={
            EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="BINARY")
    }
)

NumericFeatures: Enumeration = Enumeration(
    name="NumericFeatures",
    literals={
            EnumerationLiteral(name="precision"),
			EnumerationLiteral(name="scale"),
			EnumerationLiteral(name="radix")
    }
)

Multiplier: Enumeration = Enumeration(
    name="Multiplier",
    literals={
            EnumerationLiteral(name="K"),
			EnumerationLiteral(name="M"),
			EnumerationLiteral(name="G"),
			EnumerationLiteral(name="T"),
			EnumerationLiteral(name="P")
    }
)

ParameterMode: Enumeration = Enumeration(
    name="ParameterMode",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT")
    }
)

NumericTypes: Enumeration = Enumeration(
    name="NumericTypes",
    literals={
            EnumerationLiteral(name="BIGINT"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="DOUBLEPRECISION"),
			EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="SMALLINT"),
			EnumerationLiteral(name="INTEGER")
    }
)

ReferentialAction: Enumeration = Enumeration(
    name="ReferentialAction",
    literals={
            EnumerationLiteral(name="CASCADE"),
			EnumerationLiteral(name="SET_NULL"),
			EnumerationLiteral(name="RESTRICT"),
			EnumerationLiteral(name="NO_ACTION"),
			EnumerationLiteral(name="SET_DEFAULT")
    }
)

StringFeatures: Enumeration = Enumeration(
    name="StringFeatures",
    literals={
            EnumerationLiteral(name="length"),
			EnumerationLiteral(name="unit"),
			EnumerationLiteral(name="multiplier")
    }
)

TriggerEvent: Enumeration = Enumeration(
    name="TriggerEvent",
    literals={
            EnumerationLiteral(name="INSERT"),
			EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="UPDATE")
    }
)

Unit: Enumeration = Enumeration(
    name="Unit",
    literals={
            EnumerationLiteral(name="CHARACTERS"),
			EnumerationLiteral(name="OCTETS")
    }
)

TriggerActionTime: Enumeration = Enumeration(
    name="TriggerActionTime",
    literals={
            EnumerationLiteral(name="BEFORE"),
			EnumerationLiteral(name="AFTER")
    }
)

XMLTypes: Enumeration = Enumeration(
    name="XMLTypes",
    literals={
            EnumerationLiteral(name="XMLTYPE")
    }
)

# Classes
SQL2003_ARRAY = Class(name="SQL2003::ARRAY")
CollectionType = Class(name="CollectionType")
SQL2003_Attribute = Class(name="SQL2003::Attribute")
StructuralComponent = Class(name="StructuralComponent")
SQL2003_StructuredType = Class(name="SQL2003::StructuredType")
SQL2003_Schema = Class(name="SQL2003::Schema")
SQL2003_ParameterWithMode = Class(name="SQL2003::ParameterWithMode")
SQL2003_BinaryStringType = Class(name="SQL2003::BinaryStringType")
PredefinedType = Class(name="PredefinedType")
SQL2003_BooleanType = Class(name="SQL2003::BooleanType")
SQL2003_BaseTable = Class(name="SQL2003::BaseTable")
Table = Class(name="Table")
SQL2003_BehaviouralComponent = Class(name="SQL2003::BehaviouralComponent", is_abstract=True)
SQL2003_CollectionType = Class(name="SQL2003::CollectionType", is_abstract=True)
ConstructedType = Class(name="ConstructedType")
SQL2003_DataType = Class(name="SQL2003::DataType", is_abstract=True)
SQL2003_Column = Class(name="SQL2003::Column")
SQL2003_Table = Class(name="SQL2003::Table", is_abstract=True)
SQL2003_CharacterStringType = Class(name="SQL2003::CharacterStringType")
SQL2003_DatetimeFeature = Class(name="SQL2003::DatetimeFeature")
Feature = Class(name="Feature")
SQL2003_DatetimeType = Class(name="SQL2003::DatetimeType")
SQL2003_ColumnConstraint = Class(name="SQL2003::ColumnConstraint", is_abstract=True)
Restriction = Class(name="Restriction")
SQL2003_ConstructedType = Class(name="SQL2003::ConstructedType", is_abstract=True)
DataType = Class(name="DataType")
SQL2003_PredefinedType = Class(name="SQL2003::PredefinedType", is_abstract=True)
SQL2003_Feature = Class(name="SQL2003::Feature", is_abstract=True)
SQL2003_Field = Class(name="SQL2003::Field")
SQL2003_ROW = Class(name="SQL2003::ROW")
SQL2003_Function = Class(name="SQL2003::Function")
BehaviouralComponent = Class(name="BehaviouralComponent")
SQL2003_IntervalFeature = Class(name="SQL2003::IntervalFeature")
SQL2003_DerivedTable = Class(name="SQL2003::DerivedTable")
SQL2003_DistinctType = Class(name="SQL2003::DistinctType")
UserDefinedType = Class(name="UserDefinedType")
SQL2003_IntervalType = Class(name="SQL2003::IntervalType")
SQL2003_Method = Class(name="SQL2003::Method")
SQL2003_MethodParameter = Class(name="SQL2003::MethodParameter")
Parameter_ = Class(name="Parameter")
SQL2003_MULTISET = Class(name="SQL2003::MULTISET")
SQL2003_NotNull = Class(name="SQL2003::NotNull")
ColumnConstraint = Class(name="ColumnConstraint")
SQL2003_NumericFeature = Class(name="SQL2003::NumericFeature")
SQL2003_NumericType = Class(name="SQL2003::NumericType")
SQL2003_Parameter = Class(name="SQL2003::Parameter", is_abstract=True)
SQL2003_PrimaryKey = Class(name="SQL2003::PrimaryKey")
UniqueConstraint = Class(name="UniqueConstraint")
SQL2003_Procedure = Class(name="SQL2003::Procedure")
SQL2003_ReferenceType = Class(name="SQL2003::ReferenceType")
SQL2003_UniqueConstraint = Class(name="SQL2003::UniqueConstraint")
SQL2003_Restriction = Class(name="SQL2003::Restriction", is_abstract=True)
SQL2003_StructuralComponent = Class(name="SQL2003::StructuralComponent", is_abstract=True)
SQL2003_ReferentialConstraint = Class(name="SQL2003::ReferentialConstraint")
TableConstraint = Class(name="TableConstraint")
SQL2003_StringFeature = Class(name="SQL2003::StringFeature")
SQL2003_View = Class(name="SQL2003::View")
SQL2003_TypedTable = Class(name="SQL2003::TypedTable")
SQL2003_TableCheckConstraint = Class(name="SQL2003::TableCheckConstraint")
SQL2003_TableConstraint = Class(name="SQL2003::TableConstraint", is_abstract=True)
SQL2003_Trigger = Class(name="SQL2003::Trigger")
BaseTable = Class(name="BaseTable")
SQL2003_XMLType = Class(name="SQL2003::XMLType")
SQL2003_UserDefinedType = Class(name="SQL2003::UserDefinedType", is_abstract=True)
DerivedTable = Class(name="DerivedTable")

# SQL2003_ARRAY class attributes and methods
SQL2003_ARRAY_num_elements: Property = Property(name="num_elements", type=StringType)
SQL2003_ARRAY.attributes={SQL2003_ARRAY_num_elements}

# CollectionType class attributes and methods

# SQL2003_Attribute class attributes and methods
SQL2003_Attribute_default: Property = Property(name="default", type=StringType)
SQL2003_Attribute.attributes={SQL2003_Attribute_default}

# StructuralComponent class attributes and methods

# SQL2003_StructuredType class attributes and methods
SQL2003_StructuredType_is_instantiable: Property = Property(name="is_instantiable", type=BooleanType)
SQL2003_StructuredType_is_final: Property = Property(name="is_final", type=BooleanType)
SQL2003_StructuredType.attributes={SQL2003_StructuredType_is_final, SQL2003_StructuredType_is_instantiable}

# SQL2003_Schema class attributes and methods
SQL2003_Schema_name: Property = Property(name="name", type=StringType)
SQL2003_Schema.attributes={SQL2003_Schema_name}

# SQL2003_ParameterWithMode class attributes and methods
SQL2003_ParameterWithMode_mode: Property = Property(name="mode", type=StringType)
SQL2003_ParameterWithMode.attributes={SQL2003_ParameterWithMode_mode}

# SQL2003_BinaryStringType class attributes and methods
SQL2003_BinaryStringType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_BinaryStringType_length_def: Property = Property(name="length_def", type=StringType)
SQL2003_BinaryStringType.attributes={SQL2003_BinaryStringType_descriptor, SQL2003_BinaryStringType_length_def}

# PredefinedType class attributes and methods

# SQL2003_BooleanType class attributes and methods
SQL2003_BooleanType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_BooleanType.attributes={SQL2003_BooleanType_descriptor}

# SQL2003_BaseTable class attributes and methods

# Table class attributes and methods

# SQL2003_BehaviouralComponent class attributes and methods
SQL2003_BehaviouralComponent_name: Property = Property(name="name", type=StringType)
SQL2003_BehaviouralComponent_body: Property = Property(name="body", type=StringType)
SQL2003_BehaviouralComponent.attributes={SQL2003_BehaviouralComponent_body, SQL2003_BehaviouralComponent_name}

# SQL2003_CollectionType class attributes and methods

# ConstructedType class attributes and methods

# SQL2003_DataType class attributes and methods

# SQL2003_Column class attributes and methods
SQL2003_Column_default: Property = Property(name="default", type=StringType)
SQL2003_Column.attributes={SQL2003_Column_default}

# SQL2003_Table class attributes and methods
SQL2003_Table_name: Property = Property(name="name", type=StringType)
SQL2003_Table.attributes={SQL2003_Table_name}

# SQL2003_CharacterStringType class attributes and methods
SQL2003_CharacterStringType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_CharacterStringType_length_def: Property = Property(name="length_def", type=StringType)
SQL2003_CharacterStringType.attributes={SQL2003_CharacterStringType_length_def, SQL2003_CharacterStringType_descriptor}

# SQL2003_DatetimeFeature class attributes and methods
SQL2003_DatetimeFeature_key: Property = Property(name="key", type=StringType)
SQL2003_DatetimeFeature_value: Property = Property(name="value", type=StringType)
SQL2003_DatetimeFeature.attributes={SQL2003_DatetimeFeature_value, SQL2003_DatetimeFeature_key}

# Feature class attributes and methods

# SQL2003_DatetimeType class attributes and methods
SQL2003_DatetimeType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_DatetimeType.attributes={SQL2003_DatetimeType_descriptor}

# SQL2003_ColumnConstraint class attributes and methods

# Restriction class attributes and methods

# SQL2003_ConstructedType class attributes and methods
SQL2003_ConstructedType_name: Property = Property(name="name", type=StringType)
SQL2003_ConstructedType.attributes={SQL2003_ConstructedType_name}

# DataType class attributes and methods

# SQL2003_PredefinedType class attributes and methods

# SQL2003_Feature class attributes and methods

# SQL2003_Field class attributes and methods

# SQL2003_ROW class attributes and methods

# SQL2003_Function class attributes and methods

# BehaviouralComponent class attributes and methods

# SQL2003_IntervalFeature class attributes and methods
SQL2003_IntervalFeature_key: Property = Property(name="key", type=StringType)
SQL2003_IntervalFeature_value: Property = Property(name="value", type=StringType)
SQL2003_IntervalFeature.attributes={SQL2003_IntervalFeature_value, SQL2003_IntervalFeature_key}

# SQL2003_DerivedTable class attributes and methods
SQL2003_DerivedTable_query_expression: Property = Property(name="query_expression", type=StringType)
SQL2003_DerivedTable.attributes={SQL2003_DerivedTable_query_expression}

# SQL2003_DistinctType class attributes and methods

# UserDefinedType class attributes and methods

# SQL2003_IntervalType class attributes and methods
SQL2003_IntervalType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_IntervalType.attributes={SQL2003_IntervalType_descriptor}

# SQL2003_Method class attributes and methods
SQL2003_Method_name: Property = Property(name="name", type=StringType)
SQL2003_Method_body: Property = Property(name="body", type=StringType)
SQL2003_Method.attributes={SQL2003_Method_body, SQL2003_Method_name}

# SQL2003_MethodParameter class attributes and methods

# Parameter class attributes and methods

# SQL2003_MULTISET class attributes and methods

# SQL2003_NotNull class attributes and methods

# ColumnConstraint class attributes and methods

# SQL2003_NumericFeature class attributes and methods
SQL2003_NumericFeature_key: Property = Property(name="key", type=StringType)
SQL2003_NumericFeature_value: Property = Property(name="value", type=StringType)
SQL2003_NumericFeature.attributes={SQL2003_NumericFeature_key, SQL2003_NumericFeature_value}

# SQL2003_NumericType class attributes and methods
SQL2003_NumericType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_NumericType.attributes={SQL2003_NumericType_descriptor}

# SQL2003_Parameter class attributes and methods
SQL2003_Parameter_name: Property = Property(name="name", type=StringType)
SQL2003_Parameter.attributes={SQL2003_Parameter_name}

# SQL2003_PrimaryKey class attributes and methods

# UniqueConstraint class attributes and methods

# SQL2003_Procedure class attributes and methods

# SQL2003_ReferenceType class attributes and methods

# SQL2003_UniqueConstraint class attributes and methods

# SQL2003_Restriction class attributes and methods

# SQL2003_StructuralComponent class attributes and methods
SQL2003_StructuralComponent_name: Property = Property(name="name", type=StringType)
SQL2003_StructuralComponent.attributes={SQL2003_StructuralComponent_name}

# SQL2003_ReferentialConstraint class attributes and methods
SQL2003_ReferentialConstraint_delete_action: Property = Property(name="delete_action", type=StringType)
SQL2003_ReferentialConstraint_update_action: Property = Property(name="update_action", type=StringType)
SQL2003_ReferentialConstraint_match: Property = Property(name="match", type=StringType)
SQL2003_ReferentialConstraint.attributes={SQL2003_ReferentialConstraint_update_action, SQL2003_ReferentialConstraint_match, SQL2003_ReferentialConstraint_delete_action}

# TableConstraint class attributes and methods

# SQL2003_StringFeature class attributes and methods
SQL2003_StringFeature_key: Property = Property(name="key", type=StringType)
SQL2003_StringFeature_value: Property = Property(name="value", type=StringType)
SQL2003_StringFeature.attributes={SQL2003_StringFeature_value, SQL2003_StringFeature_key}

# SQL2003_View class attributes and methods

# SQL2003_TypedTable class attributes and methods

# SQL2003_TableCheckConstraint class attributes and methods
SQL2003_TableCheckConstraint_expression: Property = Property(name="expression", type=StringType)
SQL2003_TableCheckConstraint.attributes={SQL2003_TableCheckConstraint_expression}

# SQL2003_TableConstraint class attributes and methods
SQL2003_TableConstraint_name: Property = Property(name="name", type=StringType)
SQL2003_TableConstraint.attributes={SQL2003_TableConstraint_name}

# SQL2003_Trigger class attributes and methods
SQL2003_Trigger_name: Property = Property(name="name", type=StringType)
SQL2003_Trigger_event: Property = Property(name="event", type=StringType)
SQL2003_Trigger_actionTime: Property = Property(name="actionTime", type=StringType)
SQL2003_Trigger_triggeredAction: Property = Property(name="triggeredAction", type=StringType)
SQL2003_Trigger.attributes={SQL2003_Trigger_triggeredAction, SQL2003_Trigger_event, SQL2003_Trigger_name, SQL2003_Trigger_actionTime}

# BaseTable class attributes and methods

# SQL2003_XMLType class attributes and methods
SQL2003_XMLType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_XMLType.attributes={SQL2003_XMLType_descriptor}

# SQL2003_UserDefinedType class attributes and methods
SQL2003_UserDefinedType_name: Property = Property(name="name", type=StringType)
SQL2003_UserDefinedType.attributes={SQL2003_UserDefinedType_name}

# DerivedTable class attributes and methods

# Relationships
schema1: BinaryAssociation = BinaryAssociation(
    name="schema1",
    ends={
        Property(name="Schema", type=SQL2003_BehaviouralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralComponents", type=SQL2003_Schema, multiplicity=Multiplicity(1, 1))
    }
)
parametersWithMode2: BinaryAssociation = BinaryAssociation(
    name="parametersWithMode2",
    ends={
        Property(name="ParameterWithMode", type=SQL2003_BehaviouralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralComponent", type=SQL2003_ParameterWithMode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structured0: BinaryAssociation = BinaryAssociation(
    name="structured0",
    ends={
        Property(name="StructuredType", type=SQL2003_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=SQL2003_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
super_type4: BinaryAssociation = BinaryAssociation(
    name="super_type4",
    ends={
        Property(name="SQL2003_CollectionType", type=SQL2003_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_CollectionType3", type=SQL2003_CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="SQL2003_DataType", type=SQL2003_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_CollectionType6", type=SQL2003_DataType, multiplicity=Multiplicity(1, 1))
    }
)
table7: BinaryAssociation = BinaryAssociation(
    name="table7",
    ends={
        Property(name="Table", type=SQL2003_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=SQL2003_Table, multiplicity=Multiplicity(1, 1))
    }
)
schema8: BinaryAssociation = BinaryAssociation(
    name="schema8",
    ends={
        Property(name="Schema9", type=SQL2003_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes", type=SQL2003_Schema, multiplicity=Multiplicity(1, 1))
    }
)
source_type10: BinaryAssociation = BinaryAssociation(
    name="source_type10",
    ends={
        Property(name="PredefinedType", type=SQL2003_DistinctType, multiplicity=Multiplicity(1, 1)),
        Property(name="is_source_of", type=SQL2003_PredefinedType, multiplicity=Multiplicity(1, 1))
    }
)
features11: BinaryAssociation = BinaryAssociation(
    name="features11",
    ends={
        Property(name="SQL2003_Feature", type=SQL2003_DistinctType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_DistinctType", type=SQL2003_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
row12: BinaryAssociation = BinaryAssociation(
    name="row12",
    ends={
        Property(name="ROW", type=SQL2003_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=SQL2003_ROW, multiplicity=Multiplicity(1, 1))
    }
)
return_type13: BinaryAssociation = BinaryAssociation(
    name="return_type13",
    ends={
        Property(name="SQL2003_DataType14", type=SQL2003_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_Function", type=SQL2003_DataType, multiplicity=Multiplicity(1, 1))
    }
)
override16: BinaryAssociation = BinaryAssociation(
    name="override16",
    ends={
        Property(name="SQL2003_Method", type=SQL2003_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_Method15", type=SQL2003_Method, multiplicity=Multiplicity(0, 1))
    }
)
structured17: BinaryAssociation = BinaryAssociation(
    name="structured17",
    ends={
        Property(name="StructuredType18", type=SQL2003_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=SQL2003_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
return_type19: BinaryAssociation = BinaryAssociation(
    name="return_type19",
    ends={
        Property(name="SQL2003_DataType21", type=SQL2003_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_Method20", type=SQL2003_DataType, multiplicity=Multiplicity(1, 1))
    }
)
parameters22: BinaryAssociation = BinaryAssociation(
    name="parameters22",
    ends={
        Property(name="MethodParameter", type=SQL2003_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=SQL2003_MethodParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method23: BinaryAssociation = BinaryAssociation(
    name="method23",
    ends={
        Property(name="Method", type=SQL2003_MethodParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=SQL2003_Method, multiplicity=Multiplicity(1, 1))
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="SQL2003_DataType25", type=SQL2003_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_Parameter", type=SQL2003_DataType, multiplicity=Multiplicity(1, 1))
    }
)
behaviouralComponent26: BinaryAssociation = BinaryAssociation(
    name="behaviouralComponent26",
    ends={
        Property(name="BehaviouralComponent", type=SQL2003_ParameterWithMode, multiplicity=Multiplicity(1, 1)),
        Property(name="parametersWithMode", type=SQL2003_BehaviouralComponent, multiplicity=Multiplicity(1, 1))
    }
)
super_type29: BinaryAssociation = BinaryAssociation(
    name="super_type29",
    ends={
        Property(name="ROW30", type=SQL2003_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="sub_types", type=SQL2003_ROW, multiplicity=Multiplicity(0, 1))
    }
)
fields31: BinaryAssociation = BinaryAssociation(
    name="fields31",
    ends={
        Property(name="Field", type=SQL2003_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="row", type=SQL2003_Field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sub_types33: BinaryAssociation = BinaryAssociation(
    name="sub_types33",
    ends={
        Property(name="ROW34", type=SQL2003_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="super_type", type=SQL2003_ROW, multiplicity=Multiplicity(0, 9999))
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="SQL2003_StructuredType", type=SQL2003_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_ReferenceType", type=SQL2003_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
is_source_of27: BinaryAssociation = BinaryAssociation(
    name="is_source_of27",
    ends={
        Property(name="DistinctType", type=SQL2003_PredefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="source_type", type=SQL2003_DistinctType, multiplicity=Multiplicity(0, 9999))
    }
)
references36: BinaryAssociation = BinaryAssociation(
    name="references36",
    ends={
        Property(name="SQL2003_UniqueConstraint", type=SQL2003_ReferentialConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_ReferentialConstraint", type=SQL2003_UniqueConstraint, multiplicity=Multiplicity(1, 1))
    }
)
table37: BinaryAssociation = BinaryAssociation(
    name="table37",
    ends={
        Property(name="Table38", type=SQL2003_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictions", type=SQL2003_Table, multiplicity=Multiplicity(1, 1))
    }
)
columns39: BinaryAssociation = BinaryAssociation(
    name="columns39",
    ends={
        Property(name="StructuralComponent", type=SQL2003_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictions40", type=SQL2003_StructuralComponent, multiplicity=Multiplicity(1, 9999))
    }
)
behaviouralComponents41: BinaryAssociation = BinaryAssociation(
    name="behaviouralComponents41",
    ends={
        Property(name="BehaviouralComponent42", type=SQL2003_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=SQL2003_BehaviouralComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type48: BinaryAssociation = BinaryAssociation(
    name="type48",
    ends={
        Property(name="SQL2003_DataType49", type=SQL2003_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_StructuralComponent", type=SQL2003_DataType, multiplicity=Multiplicity(1, 1))
    }
)
views50: BinaryAssociation = BinaryAssociation(
    name="views50",
    ends={
        Property(name="View", type=SQL2003_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components", type=SQL2003_View, multiplicity=Multiplicity(0, 9999))
    }
)
restrictions51: BinaryAssociation = BinaryAssociation(
    name="restrictions51",
    ends={
        Property(name="Restriction", type=SQL2003_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="columns52", type=SQL2003_Restriction, multiplicity=Multiplicity(0, 9999))
    }
)
datatypes43: BinaryAssociation = BinaryAssociation(
    name="datatypes43",
    ends={
        Property(name="DataType", type=SQL2003_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema44", type=SQL2003_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables45: BinaryAssociation = BinaryAssociation(
    name="tables45",
    ends={
        Property(name="Table47", type=SQL2003_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema46", type=SQL2003_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super_type57: BinaryAssociation = BinaryAssociation(
    name="super_type57",
    ends={
        Property(name="SQL2003_StructuredType58", type=SQL2003_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_StructuredType56", type=SQL2003_StructuredType, multiplicity=Multiplicity(0, 1))
    }
)
attributes59: BinaryAssociation = BinaryAssociation(
    name="attributes59",
    ends={
        Property(name="Attribute", type=SQL2003_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured", type=SQL2003_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods60: BinaryAssociation = BinaryAssociation(
    name="methods60",
    ends={
        Property(name="Method62", type=SQL2003_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured61", type=SQL2003_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typed63: BinaryAssociation = BinaryAssociation(
    name="typed63",
    ends={
        Property(name="TypedTable", type=SQL2003_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured64", type=SQL2003_TypedTable, multiplicity=Multiplicity(0, 9999))
    }
)
schema65: BinaryAssociation = BinaryAssociation(
    name="schema65",
    ends={
        Property(name="Schema66", type=SQL2003_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=SQL2003_Schema, multiplicity=Multiplicity(1, 1))
    }
)
columns67: BinaryAssociation = BinaryAssociation(
    name="columns67",
    ends={
        Property(name="Column", type=SQL2003_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=SQL2003_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features53: BinaryAssociation = BinaryAssociation(
    name="features53",
    ends={
        Property(name="SQL2003_Feature55", type=SQL2003_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_StructuralComponent54", type=SQL2003_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
restrictions73: BinaryAssociation = BinaryAssociation(
    name="restrictions73",
    ends={
        Property(name="Restriction75", type=SQL2003_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table74", type=SQL2003_Restriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table76: BinaryAssociation = BinaryAssociation(
    name="table76",
    ends={
        Property(name="Table77", type=SQL2003_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggers", type=SQL2003_Table, multiplicity=Multiplicity(1, 1))
    }
)
views68: BinaryAssociation = BinaryAssociation(
    name="views68",
    ends={
        Property(name="View70", type=SQL2003_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables69", type=SQL2003_View, multiplicity=Multiplicity(0, 9999))
    }
)
triggers71: BinaryAssociation = BinaryAssociation(
    name="triggers71",
    ends={
        Property(name="Trigger", type=SQL2003_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table72", type=SQL2003_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structured80: BinaryAssociation = BinaryAssociation(
    name="structured80",
    ends={
        Property(name="StructuredType81", type=SQL2003_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="typed", type=SQL2003_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
supertable83: BinaryAssociation = BinaryAssociation(
    name="supertable83",
    ends={
        Property(name="TypedTable84", type=SQL2003_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="subtables", type=SQL2003_TypedTable, multiplicity=Multiplicity(0, 1))
    }
)
subtables86: BinaryAssociation = BinaryAssociation(
    name="subtables86",
    ends={
        Property(name="TypedTable87", type=SQL2003_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="supertable", type=SQL2003_TypedTable, multiplicity=Multiplicity(0, 9999))
    }
)
updateColumns78: BinaryAssociation = BinaryAssociation(
    name="updateColumns78",
    ends={
        Property(name="SQL2003_StructuralComponent79", type=SQL2003_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_Trigger", type=SQL2003_StructuralComponent, multiplicity=Multiplicity(0, 9999))
    }
)
tables88: BinaryAssociation = BinaryAssociation(
    name="tables88",
    ends={
        Property(name="Table89", type=SQL2003_View, multiplicity=Multiplicity(1, 1)),
        Property(name="views", type=SQL2003_Table, multiplicity=Multiplicity(1, 9999))
    }
)
components90: BinaryAssociation = BinaryAssociation(
    name="components90",
    ends={
        Property(name="StructuralComponent92", type=SQL2003_View, multiplicity=Multiplicity(1, 1)),
        Property(name="views91", type=SQL2003_StructuralComponent, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_SQL2003_ARRAY_CollectionType = Generalization(general=CollectionType, specific=SQL2003_ARRAY)
gen_SQL2003_Attribute_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_Attribute)
gen_SQL2003_BinaryStringType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_BinaryStringType)
gen_SQL2003_BooleanType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_BooleanType)
gen_SQL2003_BaseTable_Table = Generalization(general=Table, specific=SQL2003_BaseTable)
gen_SQL2003_CollectionType_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_CollectionType)
gen_SQL2003_Column_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_Column)
gen_SQL2003_CharacterStringType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_CharacterStringType)
gen_SQL2003_DatetimeFeature_Feature = Generalization(general=Feature, specific=SQL2003_DatetimeFeature)
gen_SQL2003_DatetimeType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_DatetimeType)
gen_SQL2003_ColumnConstraint_Restriction = Generalization(general=Restriction, specific=SQL2003_ColumnConstraint)
gen_SQL2003_ConstructedType_DataType = Generalization(general=DataType, specific=SQL2003_ConstructedType)
gen_SQL2003_DistinctType_UserDefinedType = Generalization(general=UserDefinedType, specific=SQL2003_DistinctType)
gen_SQL2003_Field_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_Field)
gen_SQL2003_Function_BehaviouralComponent = Generalization(general=BehaviouralComponent, specific=SQL2003_Function)
gen_SQL2003_IntervalFeature_Feature = Generalization(general=Feature, specific=SQL2003_IntervalFeature)
gen_SQL2003_DerivedTable_Table = Generalization(general=Table, specific=SQL2003_DerivedTable)
gen_SQL2003_IntervalType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_IntervalType)
gen_SQL2003_MethodParameter_Parameter = Generalization(general=Parameter_, specific=SQL2003_MethodParameter)
gen_SQL2003_MULTISET_CollectionType = Generalization(general=CollectionType, specific=SQL2003_MULTISET)
gen_SQL2003_NotNull_ColumnConstraint = Generalization(general=ColumnConstraint, specific=SQL2003_NotNull)
gen_SQL2003_NumericFeature_Feature = Generalization(general=Feature, specific=SQL2003_NumericFeature)
gen_SQL2003_NumericType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_NumericType)
gen_SQL2003_ParameterWithMode_Parameter = Generalization(general=Parameter_, specific=SQL2003_ParameterWithMode)
gen_SQL2003_PrimaryKey_UniqueConstraint = Generalization(general=UniqueConstraint, specific=SQL2003_PrimaryKey)
gen_SQL2003_Procedure_BehaviouralComponent = Generalization(general=BehaviouralComponent, specific=SQL2003_Procedure)
gen_SQL2003_ROW_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_ROW)
gen_SQL2003_ReferenceType_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_ReferenceType)
gen_SQL2003_PredefinedType_DataType = Generalization(general=DataType, specific=SQL2003_PredefinedType)
gen_SQL2003_ReferentialConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_ReferentialConstraint)
gen_SQL2003_StringFeature_Feature = Generalization(general=Feature, specific=SQL2003_StringFeature)
gen_SQL2003_StructuredType_UserDefinedType = Generalization(general=UserDefinedType, specific=SQL2003_StructuredType)
gen_SQL2003_TableCheckConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_TableCheckConstraint)
gen_SQL2003_TableConstraint_Restriction = Generalization(general=Restriction, specific=SQL2003_TableConstraint)
gen_SQL2003_TypedTable_BaseTable = Generalization(general=BaseTable, specific=SQL2003_TypedTable)
gen_SQL2003_UniqueConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_UniqueConstraint)
gen_SQL2003_XMLType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_XMLType)
gen_SQL2003_UserDefinedType_DataType = Generalization(general=DataType, specific=SQL2003_UserDefinedType)
gen_SQL2003_View_DerivedTable = Generalization(general=DerivedTable, specific=SQL2003_View)

# Domain Model
domain_model = DomainModel(
    name="SQL2003",
    types={SQL2003_ARRAY, CollectionType, SQL2003_Attribute, StructuralComponent, SQL2003_StructuredType, SQL2003_Schema, SQL2003_ParameterWithMode, SQL2003_BinaryStringType, PredefinedType, SQL2003_BooleanType, SQL2003_BaseTable, Table, SQL2003_BehaviouralComponent, SQL2003_CollectionType, ConstructedType, SQL2003_DataType, SQL2003_Column, SQL2003_Table, SQL2003_CharacterStringType, SQL2003_DatetimeFeature, Feature, SQL2003_DatetimeType, SQL2003_ColumnConstraint, Restriction, SQL2003_ConstructedType, DataType, SQL2003_PredefinedType, SQL2003_Feature, SQL2003_Field, SQL2003_ROW, SQL2003_Function, BehaviouralComponent, SQL2003_IntervalFeature, SQL2003_DerivedTable, SQL2003_DistinctType, UserDefinedType, SQL2003_IntervalType, SQL2003_Method, SQL2003_MethodParameter, Parameter_, SQL2003_MULTISET, SQL2003_NotNull, ColumnConstraint, SQL2003_NumericFeature, SQL2003_NumericType, SQL2003_Parameter, SQL2003_PrimaryKey, UniqueConstraint, SQL2003_Procedure, SQL2003_ReferenceType, SQL2003_UniqueConstraint, SQL2003_Restriction, SQL2003_StructuralComponent, SQL2003_ReferentialConstraint, TableConstraint, SQL2003_StringFeature, SQL2003_View, SQL2003_TypedTable, SQL2003_TableCheckConstraint, SQL2003_TableConstraint, SQL2003_Trigger, BaseTable, SQL2003_XMLType, SQL2003_UserDefinedType, DerivedTable, BinaryStringTypes, CharacterStringTypes, BooleanTypes, DatetimeFeatures, DatetimeTypes, IntervalTypes, IntervalFeatures, MatchTypes, NumericRadix, NumericFeatures, Multiplier, ParameterMode, NumericTypes, ReferentialAction, StringFeatures, TriggerEvent, Unit, TriggerActionTime, XMLTypes},
    associations={schema1, parametersWithMode2, structured0, super_type4, type5, table7, schema8, source_type10, features11, row12, return_type13, override16, structured17, return_type19, parameters22, method23, type24, behaviouralComponent26, super_type29, fields31, sub_types33, type35, is_source_of27, references36, table37, columns39, behaviouralComponents41, type48, views50, restrictions51, datatypes43, tables45, super_type57, attributes59, methods60, typed63, schema65, columns67, features53, restrictions73, table76, views68, triggers71, structured80, supertable83, subtables86, updateColumns78, tables88, components90},
    generalizations={gen_SQL2003_ARRAY_CollectionType, gen_SQL2003_Attribute_StructuralComponent, gen_SQL2003_BinaryStringType_PredefinedType, gen_SQL2003_BooleanType_PredefinedType, gen_SQL2003_BaseTable_Table, gen_SQL2003_CollectionType_ConstructedType, gen_SQL2003_Column_StructuralComponent, gen_SQL2003_CharacterStringType_PredefinedType, gen_SQL2003_DatetimeFeature_Feature, gen_SQL2003_DatetimeType_PredefinedType, gen_SQL2003_ColumnConstraint_Restriction, gen_SQL2003_ConstructedType_DataType, gen_SQL2003_DistinctType_UserDefinedType, gen_SQL2003_Field_StructuralComponent, gen_SQL2003_Function_BehaviouralComponent, gen_SQL2003_IntervalFeature_Feature, gen_SQL2003_DerivedTable_Table, gen_SQL2003_IntervalType_PredefinedType, gen_SQL2003_MethodParameter_Parameter, gen_SQL2003_MULTISET_CollectionType, gen_SQL2003_NotNull_ColumnConstraint, gen_SQL2003_NumericFeature_Feature, gen_SQL2003_NumericType_PredefinedType, gen_SQL2003_ParameterWithMode_Parameter, gen_SQL2003_PrimaryKey_UniqueConstraint, gen_SQL2003_Procedure_BehaviouralComponent, gen_SQL2003_ROW_ConstructedType, gen_SQL2003_ReferenceType_ConstructedType, gen_SQL2003_PredefinedType_DataType, gen_SQL2003_ReferentialConstraint_TableConstraint, gen_SQL2003_StringFeature_Feature, gen_SQL2003_StructuredType_UserDefinedType, gen_SQL2003_TableCheckConstraint_TableConstraint, gen_SQL2003_TableConstraint_Restriction, gen_SQL2003_TypedTable_BaseTable, gen_SQL2003_UniqueConstraint_TableConstraint, gen_SQL2003_XMLType_PredefinedType, gen_SQL2003_UserDefinedType_DataType, gen_SQL2003_View_DerivedTable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)