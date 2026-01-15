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
DatetimeFeatures: Enumeration = Enumeration(
    name="DatetimeFeatures",
    literals={
            EnumerationLiteral(name="precision")
    }
)

BinaryStringTypes: Enumeration = Enumeration(
    name="BinaryStringTypes",
    literals={
            EnumerationLiteral(name="BINARYLARGEOBJECT"),
			EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="BINARYVARYING")
    }
)

BooleanTypes: Enumeration = Enumeration(
    name="BooleanTypes",
    literals={
            EnumerationLiteral(name="BOOLEAN")
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

IntervalFeatures: Enumeration = Enumeration(
    name="IntervalFeatures",
    literals={
            EnumerationLiteral(name="start_leading_precision"),
			EnumerationLiteral(name="end_leading_precision"),
			EnumerationLiteral(name="leading_precision"),
			EnumerationLiteral(name="second_precision")
    }
)

IntervalTypes: Enumeration = Enumeration(
    name="IntervalTypes",
    literals={
            EnumerationLiteral(name="HOUR_MINUTE"),
			EnumerationLiteral(name="HOUR_SECOND"),
			EnumerationLiteral(name="MINUTE_SECOND"),
			EnumerationLiteral(name="YEAR"),
			EnumerationLiteral(name="YEAR_MONTH"),
			EnumerationLiteral(name="DAY_HOUR"),
			EnumerationLiteral(name="DAY_MINUTE"),
			EnumerationLiteral(name="DAY_SECOND"),
			EnumerationLiteral(name="MONTH"),
			EnumerationLiteral(name="DAY"),
			EnumerationLiteral(name="HOUR"),
			EnumerationLiteral(name="MINUTE"),
			EnumerationLiteral(name="SECOND")
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

NumericRadix: Enumeration = Enumeration(
    name="NumericRadix",
    literals={
            EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="DECIMAL")
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

NumericTypes: Enumeration = Enumeration(
    name="NumericTypes",
    literals={
            EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="SMALLINT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="BIGINT"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="DOUBLEPRECISION")
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

TriggerActionTime: Enumeration = Enumeration(
    name="TriggerActionTime",
    literals={
            EnumerationLiteral(name="BEFORE"),
			EnumerationLiteral(name="AFTER")
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

TriggerLevel: Enumeration = Enumeration(
    name="TriggerLevel",
    literals={
            EnumerationLiteral(name="ROW_LEVEL"),
			EnumerationLiteral(name="STATEMENT_LEVEL")
    }
)

Unit: Enumeration = Enumeration(
    name="Unit",
    literals={
            EnumerationLiteral(name="OCTETS"),
			EnumerationLiteral(name="CHARACTERS")
    }
)

XMLTypes: Enumeration = Enumeration(
    name="XMLTypes",
    literals={
            EnumerationLiteral(name="XMLTYPE")
    }
)

# Classes
SQL2003_V2_BinaryStringType = Class(name="SQL2003::V2::BinaryStringType")
PredefinedType = Class(name="PredefinedType")
SQL2003_V2_ARRAY = Class(name="SQL2003::V2::ARRAY")
CollectionType = Class(name="CollectionType")
SQL2003_V2_Attribute = Class(name="SQL2003::V2::Attribute")
StructuralComponent = Class(name="StructuralComponent")
SQL2003_V2_StructuredType = Class(name="SQL2003::V2::StructuredType")
SQL2003_V2_BaseTable = Class(name="SQL2003::V2::BaseTable")
Table = Class(name="Table")
SQL2003_V2_BehaviouralComponent = Class(name="SQL2003::V2::BehaviouralComponent", is_abstract=True)
SQL2003_V2_Schema = Class(name="SQL2003::V2::Schema")
SQL2003_V2_ParameterWithMode = Class(name="SQL2003::V2::ParameterWithMode")
SQL2003_V2_DatetimeType = Class(name="SQL2003::V2::DatetimeType")
SQL2003_V2_BooleanType = Class(name="SQL2003::V2::BooleanType")
SQL2003_V2_CharacterStringType = Class(name="SQL2003::V2::CharacterStringType")
SQL2003_V2_CollectionType = Class(name="SQL2003::V2::CollectionType", is_abstract=True)
ConstructedType = Class(name="ConstructedType")
SQL2003_V2_DataType = Class(name="SQL2003::V2::DataType", is_abstract=True)
SQL2003_V2_Column = Class(name="SQL2003::V2::Column")
SQL2003_V2_Table = Class(name="SQL2003::V2::Table", is_abstract=True)
SQL2003_V2_ColumnConstraint = Class(name="SQL2003::V2::ColumnConstraint", is_abstract=True)
Restriction = Class(name="Restriction")
SQL2003_V2_ConstructedType = Class(name="SQL2003::V2::ConstructedType", is_abstract=True)
DataType = Class(name="DataType")
SQL2003_V2_DatetimeFeature = Class(name="SQL2003::V2::DatetimeFeature")
Feature = Class(name="Feature")
SQL2003_V2_DerivedTable = Class(name="SQL2003::V2::DerivedTable")
SQL2003_V2_DistinctType = Class(name="SQL2003::V2::DistinctType")
UserDefinedType = Class(name="UserDefinedType")
SQL2003_V2_PredefinedType = Class(name="SQL2003::V2::PredefinedType", is_abstract=True)
SQL2003_V2_Feature = Class(name="SQL2003::V2::Feature", is_abstract=True)
SQL2003_V2_Field = Class(name="SQL2003::V2::Field")
SQL2003_V2_ROW = Class(name="SQL2003::V2::ROW")
SQL2003_V2_Function = Class(name="SQL2003::V2::Function")
BehaviouralComponent = Class(name="BehaviouralComponent")
SQL2003_V2_IntervalFeature = Class(name="SQL2003::V2::IntervalFeature")
SQL2003_V2_IntervalType = Class(name="SQL2003::V2::IntervalType")
SQL2003_V2_NumericFeature = Class(name="SQL2003::V2::NumericFeature")
SQL2003_V2_MULTISET = Class(name="SQL2003::V2::MULTISET")
SQL2003_V2_Method = Class(name="SQL2003::V2::Method")
SQL2003_V2_MethodParameter = Class(name="SQL2003::V2::MethodParameter")
Parameter_ = Class(name="Parameter")
SQL2003_V2_NotNull = Class(name="SQL2003::V2::NotNull")
ColumnConstraint = Class(name="ColumnConstraint")
SQL2003_V2_NumericType = Class(name="SQL2003::V2::NumericType")
SQL2003_V2_Parameter = Class(name="SQL2003::V2::Parameter", is_abstract=True)
SQL2003_V2_PrimaryKey = Class(name="SQL2003::V2::PrimaryKey")
UniqueConstraint = Class(name="UniqueConstraint")
SQL2003_V2_Procedure = Class(name="SQL2003::V2::Procedure")
SQL2003_V2_ReferenceType = Class(name="SQL2003::V2::ReferenceType")
SQL2003_V2_ReferentialConstraint = Class(name="SQL2003::V2::ReferentialConstraint")
TableConstraint = Class(name="TableConstraint")
SQL2003_V2_UniqueConstraint = Class(name="SQL2003::V2::UniqueConstraint")
SQL2003_V2_Restriction = Class(name="SQL2003::V2::Restriction", is_abstract=True)
SQL2003_V2_StructuralComponent = Class(name="SQL2003::V2::StructuralComponent", is_abstract=True)
SQL2003_V2_View = Class(name="SQL2003::V2::View")
SQL2003_V2_Domain = Class(name="SQL2003::V2::Domain")
SQL2003_V2_StringFeature = Class(name="SQL2003::V2::StringFeature")
SQL2003_V2_TypedTable = Class(name="SQL2003::V2::TypedTable")
SQL2003_V2_TableConstraint = Class(name="SQL2003::V2::TableConstraint", is_abstract=True)
SQL2003_V2_TableCheckConstraint = Class(name="SQL2003::V2::TableCheckConstraint")
SQL2003_V2_Trigger = Class(name="SQL2003::V2::Trigger")
SQL2003_V2_TriggerDescriptor = Class(name="SQL2003::V2::TriggerDescriptor")
SQL2003_V2_UserDefinedType = Class(name="SQL2003::V2::UserDefinedType", is_abstract=True)
BaseTable = Class(name="BaseTable")
DerivedTable = Class(name="DerivedTable")
SQL2003_V2_XMLType = Class(name="SQL2003::V2::XMLType")

# SQL2003_V2_BinaryStringType class attributes and methods
SQL2003_V2_BinaryStringType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V2_BinaryStringType_length_def: Property = Property(name="length_def", type=StringType)
SQL2003_V2_BinaryStringType.attributes={SQL2003_V2_BinaryStringType_length_def, SQL2003_V2_BinaryStringType_descriptor}

# PredefinedType class attributes and methods

# SQL2003_V2_ARRAY class attributes and methods
SQL2003_V2_ARRAY_num_elements: Property = Property(name="num_elements", type=StringType)
SQL2003_V2_ARRAY.attributes={SQL2003_V2_ARRAY_num_elements}

# CollectionType class attributes and methods

# SQL2003_V2_Attribute class attributes and methods
SQL2003_V2_Attribute_default: Property = Property(name="default", type=StringType)
SQL2003_V2_Attribute.attributes={SQL2003_V2_Attribute_default}

# StructuralComponent class attributes and methods

# SQL2003_V2_StructuredType class attributes and methods
SQL2003_V2_StructuredType_is_final: Property = Property(name="is_final", type=BooleanType)
SQL2003_V2_StructuredType_is_instantiable: Property = Property(name="is_instantiable", type=BooleanType)
SQL2003_V2_StructuredType.attributes={SQL2003_V2_StructuredType_is_instantiable, SQL2003_V2_StructuredType_is_final}

# SQL2003_V2_BaseTable class attributes and methods

# Table class attributes and methods

# SQL2003_V2_BehaviouralComponent class attributes and methods
SQL2003_V2_BehaviouralComponent_name: Property = Property(name="name", type=StringType)
SQL2003_V2_BehaviouralComponent_body: Property = Property(name="body", type=StringType)
SQL2003_V2_BehaviouralComponent.attributes={SQL2003_V2_BehaviouralComponent_name, SQL2003_V2_BehaviouralComponent_body}

# SQL2003_V2_Schema class attributes and methods
SQL2003_V2_Schema_name: Property = Property(name="name", type=StringType)
SQL2003_V2_Schema.attributes={SQL2003_V2_Schema_name}

# SQL2003_V2_ParameterWithMode class attributes and methods
SQL2003_V2_ParameterWithMode_mode: Property = Property(name="mode", type=StringType)
SQL2003_V2_ParameterWithMode.attributes={SQL2003_V2_ParameterWithMode_mode}

# SQL2003_V2_DatetimeType class attributes and methods
SQL2003_V2_DatetimeType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V2_DatetimeType.attributes={SQL2003_V2_DatetimeType_descriptor}

# SQL2003_V2_BooleanType class attributes and methods
SQL2003_V2_BooleanType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V2_BooleanType.attributes={SQL2003_V2_BooleanType_descriptor}

# SQL2003_V2_CharacterStringType class attributes and methods
SQL2003_V2_CharacterStringType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V2_CharacterStringType_length_def: Property = Property(name="length_def", type=StringType)
SQL2003_V2_CharacterStringType.attributes={SQL2003_V2_CharacterStringType_length_def, SQL2003_V2_CharacterStringType_descriptor}

# SQL2003_V2_CollectionType class attributes and methods

# ConstructedType class attributes and methods

# SQL2003_V2_DataType class attributes and methods

# SQL2003_V2_Column class attributes and methods
SQL2003_V2_Column_default: Property = Property(name="default", type=StringType)
SQL2003_V2_Column.attributes={SQL2003_V2_Column_default}

# SQL2003_V2_Table class attributes and methods
SQL2003_V2_Table_name: Property = Property(name="name", type=StringType)
SQL2003_V2_Table.attributes={SQL2003_V2_Table_name}

# SQL2003_V2_ColumnConstraint class attributes and methods

# Restriction class attributes and methods

# SQL2003_V2_ConstructedType class attributes and methods
SQL2003_V2_ConstructedType_name: Property = Property(name="name", type=StringType)
SQL2003_V2_ConstructedType.attributes={SQL2003_V2_ConstructedType_name}

# DataType class attributes and methods

# SQL2003_V2_DatetimeFeature class attributes and methods
SQL2003_V2_DatetimeFeature_key: Property = Property(name="key", type=StringType)
SQL2003_V2_DatetimeFeature_value: Property = Property(name="value", type=StringType)
SQL2003_V2_DatetimeFeature.attributes={SQL2003_V2_DatetimeFeature_value, SQL2003_V2_DatetimeFeature_key}

# Feature class attributes and methods

# SQL2003_V2_DerivedTable class attributes and methods
SQL2003_V2_DerivedTable_query_expression: Property = Property(name="query_expression", type=StringType)
SQL2003_V2_DerivedTable.attributes={SQL2003_V2_DerivedTable_query_expression}

# SQL2003_V2_DistinctType class attributes and methods

# UserDefinedType class attributes and methods

# SQL2003_V2_PredefinedType class attributes and methods

# SQL2003_V2_Feature class attributes and methods

# SQL2003_V2_Field class attributes and methods

# SQL2003_V2_ROW class attributes and methods

# SQL2003_V2_Function class attributes and methods

# BehaviouralComponent class attributes and methods

# SQL2003_V2_IntervalFeature class attributes and methods
SQL2003_V2_IntervalFeature_key: Property = Property(name="key", type=StringType)
SQL2003_V2_IntervalFeature_value: Property = Property(name="value", type=StringType)
SQL2003_V2_IntervalFeature.attributes={SQL2003_V2_IntervalFeature_value, SQL2003_V2_IntervalFeature_key}

# SQL2003_V2_IntervalType class attributes and methods
SQL2003_V2_IntervalType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V2_IntervalType.attributes={SQL2003_V2_IntervalType_descriptor}

# SQL2003_V2_NumericFeature class attributes and methods
SQL2003_V2_NumericFeature_key: Property = Property(name="key", type=StringType)
SQL2003_V2_NumericFeature_value: Property = Property(name="value", type=StringType)
SQL2003_V2_NumericFeature.attributes={SQL2003_V2_NumericFeature_value, SQL2003_V2_NumericFeature_key}

# SQL2003_V2_MULTISET class attributes and methods

# SQL2003_V2_Method class attributes and methods
SQL2003_V2_Method_name: Property = Property(name="name", type=StringType)
SQL2003_V2_Method_body: Property = Property(name="body", type=StringType)
SQL2003_V2_Method.attributes={SQL2003_V2_Method_name, SQL2003_V2_Method_body}

# SQL2003_V2_MethodParameter class attributes and methods

# Parameter class attributes and methods

# SQL2003_V2_NotNull class attributes and methods

# ColumnConstraint class attributes and methods

# SQL2003_V2_NumericType class attributes and methods
SQL2003_V2_NumericType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V2_NumericType.attributes={SQL2003_V2_NumericType_descriptor}

# SQL2003_V2_Parameter class attributes and methods
SQL2003_V2_Parameter_name: Property = Property(name="name", type=StringType)
SQL2003_V2_Parameter.attributes={SQL2003_V2_Parameter_name}

# SQL2003_V2_PrimaryKey class attributes and methods

# UniqueConstraint class attributes and methods

# SQL2003_V2_Procedure class attributes and methods

# SQL2003_V2_ReferenceType class attributes and methods

# SQL2003_V2_ReferentialConstraint class attributes and methods
SQL2003_V2_ReferentialConstraint_update_action: Property = Property(name="update_action", type=StringType)
SQL2003_V2_ReferentialConstraint_delete_action: Property = Property(name="delete_action", type=StringType)
SQL2003_V2_ReferentialConstraint_match: Property = Property(name="match", type=StringType)
SQL2003_V2_ReferentialConstraint.attributes={SQL2003_V2_ReferentialConstraint_match, SQL2003_V2_ReferentialConstraint_update_action, SQL2003_V2_ReferentialConstraint_delete_action}

# TableConstraint class attributes and methods

# SQL2003_V2_UniqueConstraint class attributes and methods

# SQL2003_V2_Restriction class attributes and methods

# SQL2003_V2_StructuralComponent class attributes and methods
SQL2003_V2_StructuralComponent_name: Property = Property(name="name", type=StringType)
SQL2003_V2_StructuralComponent.attributes={SQL2003_V2_StructuralComponent_name}

# SQL2003_V2_View class attributes and methods

# SQL2003_V2_Domain class attributes and methods
SQL2003_V2_Domain_name: Property = Property(name="name", type=StringType)
SQL2003_V2_Domain_expression: Property = Property(name="expression", type=StringType)
SQL2003_V2_Domain_default: Property = Property(name="default", type=StringType)
SQL2003_V2_Domain.attributes={SQL2003_V2_Domain_expression, SQL2003_V2_Domain_default, SQL2003_V2_Domain_name}

# SQL2003_V2_StringFeature class attributes and methods
SQL2003_V2_StringFeature_key: Property = Property(name="key", type=StringType)
SQL2003_V2_StringFeature_value: Property = Property(name="value", type=StringType)
SQL2003_V2_StringFeature.attributes={SQL2003_V2_StringFeature_key, SQL2003_V2_StringFeature_value}

# SQL2003_V2_TypedTable class attributes and methods

# SQL2003_V2_TableConstraint class attributes and methods
SQL2003_V2_TableConstraint_name: Property = Property(name="name", type=StringType)
SQL2003_V2_TableConstraint.attributes={SQL2003_V2_TableConstraint_name}

# SQL2003_V2_TableCheckConstraint class attributes and methods
SQL2003_V2_TableCheckConstraint_expression: Property = Property(name="expression", type=StringType)
SQL2003_V2_TableCheckConstraint.attributes={SQL2003_V2_TableCheckConstraint_expression}

# SQL2003_V2_Trigger class attributes and methods
SQL2003_V2_Trigger_name: Property = Property(name="name", type=StringType)
SQL2003_V2_Trigger.attributes={SQL2003_V2_Trigger_name}

# SQL2003_V2_TriggerDescriptor class attributes and methods
SQL2003_V2_TriggerDescriptor_event: Property = Property(name="event", type=StringType)
SQL2003_V2_TriggerDescriptor_actionTime: Property = Property(name="actionTime", type=StringType)
SQL2003_V2_TriggerDescriptor_triggeredAction: Property = Property(name="triggeredAction", type=StringType)
SQL2003_V2_TriggerDescriptor_level: Property = Property(name="level", type=StringType)
SQL2003_V2_TriggerDescriptor.attributes={SQL2003_V2_TriggerDescriptor_triggeredAction, SQL2003_V2_TriggerDescriptor_event, SQL2003_V2_TriggerDescriptor_level, SQL2003_V2_TriggerDescriptor_actionTime}

# SQL2003_V2_UserDefinedType class attributes and methods
SQL2003_V2_UserDefinedType_name: Property = Property(name="name", type=StringType)
SQL2003_V2_UserDefinedType.attributes={SQL2003_V2_UserDefinedType_name}

# BaseTable class attributes and methods

# DerivedTable class attributes and methods

# SQL2003_V2_XMLType class attributes and methods
SQL2003_V2_XMLType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V2_XMLType.attributes={SQL2003_V2_XMLType_descriptor}

# Relationships
structured0: BinaryAssociation = BinaryAssociation(
    name="structured0",
    ends={
        Property(name="StructuredType", type=SQL2003_V2_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=SQL2003_V2_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
schema1: BinaryAssociation = BinaryAssociation(
    name="schema1",
    ends={
        Property(name="Schema", type=SQL2003_V2_BehaviouralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralComponents", type=SQL2003_V2_Schema, multiplicity=Multiplicity(1, 1))
    }
)
parametersWithMode2: BinaryAssociation = BinaryAssociation(
    name="parametersWithMode2",
    ends={
        Property(name="ParameterWithMode", type=SQL2003_V2_BehaviouralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralComponent", type=SQL2003_V2_ParameterWithMode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super_type4: BinaryAssociation = BinaryAssociation(
    name="super_type4",
    ends={
        Property(name="SQL2003_V2_CollectionType", type=SQL2003_V2_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_CollectionType3", type=SQL2003_V2_CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="SQL2003_V2_DataType", type=SQL2003_V2_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_CollectionType6", type=SQL2003_V2_DataType, multiplicity=Multiplicity(1, 1))
    }
)
table7: BinaryAssociation = BinaryAssociation(
    name="table7",
    ends={
        Property(name="Table", type=SQL2003_V2_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=SQL2003_V2_Table, multiplicity=Multiplicity(1, 1))
    }
)
schema8: BinaryAssociation = BinaryAssociation(
    name="schema8",
    ends={
        Property(name="Schema9", type=SQL2003_V2_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes", type=SQL2003_V2_Schema, multiplicity=Multiplicity(1, 1))
    }
)
source_type10: BinaryAssociation = BinaryAssociation(
    name="source_type10",
    ends={
        Property(name="PredefinedType", type=SQL2003_V2_DistinctType, multiplicity=Multiplicity(1, 1)),
        Property(name="is_source_of", type=SQL2003_V2_PredefinedType, multiplicity=Multiplicity(1, 1))
    }
)
features11: BinaryAssociation = BinaryAssociation(
    name="features11",
    ends={
        Property(name="SQL2003_V2_Feature", type=SQL2003_V2_DistinctType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_DistinctType", type=SQL2003_V2_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
row12: BinaryAssociation = BinaryAssociation(
    name="row12",
    ends={
        Property(name="ROW", type=SQL2003_V2_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=SQL2003_V2_ROW, multiplicity=Multiplicity(1, 1))
    }
)
return_type13: BinaryAssociation = BinaryAssociation(
    name="return_type13",
    ends={
        Property(name="SQL2003_V2_DataType14", type=SQL2003_V2_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_Function", type=SQL2003_V2_DataType, multiplicity=Multiplicity(1, 1))
    }
)
override16: BinaryAssociation = BinaryAssociation(
    name="override16",
    ends={
        Property(name="SQL2003_V2_Method", type=SQL2003_V2_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_Method15", type=SQL2003_V2_Method, multiplicity=Multiplicity(0, 1))
    }
)
structured17: BinaryAssociation = BinaryAssociation(
    name="structured17",
    ends={
        Property(name="StructuredType18", type=SQL2003_V2_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=SQL2003_V2_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
return_type19: BinaryAssociation = BinaryAssociation(
    name="return_type19",
    ends={
        Property(name="SQL2003_V2_DataType21", type=SQL2003_V2_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_Method20", type=SQL2003_V2_DataType, multiplicity=Multiplicity(1, 1))
    }
)
parameters22: BinaryAssociation = BinaryAssociation(
    name="parameters22",
    ends={
        Property(name="MethodParameter", type=SQL2003_V2_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=SQL2003_V2_MethodParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method23: BinaryAssociation = BinaryAssociation(
    name="method23",
    ends={
        Property(name="Method", type=SQL2003_V2_MethodParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=SQL2003_V2_Method, multiplicity=Multiplicity(1, 1))
    }
)
super_type29: BinaryAssociation = BinaryAssociation(
    name="super_type29",
    ends={
        Property(name="ROW30", type=SQL2003_V2_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="sub_types", type=SQL2003_V2_ROW, multiplicity=Multiplicity(0, 1))
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="SQL2003_V2_DataType25", type=SQL2003_V2_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_Parameter", type=SQL2003_V2_DataType, multiplicity=Multiplicity(1, 1))
    }
)
behaviouralComponent26: BinaryAssociation = BinaryAssociation(
    name="behaviouralComponent26",
    ends={
        Property(name="BehaviouralComponent", type=SQL2003_V2_ParameterWithMode, multiplicity=Multiplicity(1, 1)),
        Property(name="parametersWithMode", type=SQL2003_V2_BehaviouralComponent, multiplicity=Multiplicity(1, 1))
    }
)
is_source_of27: BinaryAssociation = BinaryAssociation(
    name="is_source_of27",
    ends={
        Property(name="DistinctType", type=SQL2003_V2_PredefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="source_type", type=SQL2003_V2_DistinctType, multiplicity=Multiplicity(0, 9999))
    }
)
fields31: BinaryAssociation = BinaryAssociation(
    name="fields31",
    ends={
        Property(name="Field", type=SQL2003_V2_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="row", type=SQL2003_V2_Field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sub_types33: BinaryAssociation = BinaryAssociation(
    name="sub_types33",
    ends={
        Property(name="ROW34", type=SQL2003_V2_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="super_type", type=SQL2003_V2_ROW, multiplicity=Multiplicity(0, 9999))
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="SQL2003_V2_StructuredType", type=SQL2003_V2_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_ReferenceType", type=SQL2003_V2_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
tables45: BinaryAssociation = BinaryAssociation(
    name="tables45",
    ends={
        Property(name="Table47", type=SQL2003_V2_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema46", type=SQL2003_V2_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references36: BinaryAssociation = BinaryAssociation(
    name="references36",
    ends={
        Property(name="SQL2003_V2_UniqueConstraint", type=SQL2003_V2_ReferentialConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_ReferentialConstraint", type=SQL2003_V2_UniqueConstraint, multiplicity=Multiplicity(1, 1))
    }
)
table37: BinaryAssociation = BinaryAssociation(
    name="table37",
    ends={
        Property(name="Table38", type=SQL2003_V2_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictions", type=SQL2003_V2_Table, multiplicity=Multiplicity(1, 1))
    }
)
columns39: BinaryAssociation = BinaryAssociation(
    name="columns39",
    ends={
        Property(name="StructuralComponent", type=SQL2003_V2_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictions40", type=SQL2003_V2_StructuralComponent, multiplicity=Multiplicity(1, 9999))
    }
)
behaviouralComponents41: BinaryAssociation = BinaryAssociation(
    name="behaviouralComponents41",
    ends={
        Property(name="BehaviouralComponent42", type=SQL2003_V2_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=SQL2003_V2_BehaviouralComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypes43: BinaryAssociation = BinaryAssociation(
    name="datatypes43",
    ends={
        Property(name="DataType", type=SQL2003_V2_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema44", type=SQL2003_V2_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views52: BinaryAssociation = BinaryAssociation(
    name="views52",
    ends={
        Property(name="View", type=SQL2003_V2_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components", type=SQL2003_V2_View, multiplicity=Multiplicity(0, 9999))
    }
)
domains48: BinaryAssociation = BinaryAssociation(
    name="domains48",
    ends={
        Property(name="Domain", type=SQL2003_V2_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema49", type=SQL2003_V2_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type50: BinaryAssociation = BinaryAssociation(
    name="type50",
    ends={
        Property(name="SQL2003_V2_DataType51", type=SQL2003_V2_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_StructuralComponent", type=SQL2003_V2_DataType, multiplicity=Multiplicity(1, 1))
    }
)
restrictions53: BinaryAssociation = BinaryAssociation(
    name="restrictions53",
    ends={
        Property(name="Restriction", type=SQL2003_V2_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="columns54", type=SQL2003_V2_Restriction, multiplicity=Multiplicity(0, 9999))
    }
)
features55: BinaryAssociation = BinaryAssociation(
    name="features55",
    ends={
        Property(name="SQL2003_V2_Feature57", type=SQL2003_V2_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_StructuralComponent56", type=SQL2003_V2_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
has_domain58: BinaryAssociation = BinaryAssociation(
    name="has_domain58",
    ends={
        Property(name="Domain59", type=SQL2003_V2_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="defines", type=SQL2003_V2_Domain, multiplicity=Multiplicity(0, 1))
    }
)
super_type61: BinaryAssociation = BinaryAssociation(
    name="super_type61",
    ends={
        Property(name="SQL2003_V2_StructuredType62", type=SQL2003_V2_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_StructuredType60", type=SQL2003_V2_StructuredType, multiplicity=Multiplicity(0, 1))
    }
)
attributes63: BinaryAssociation = BinaryAssociation(
    name="attributes63",
    ends={
        Property(name="Attribute", type=SQL2003_V2_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured", type=SQL2003_V2_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods64: BinaryAssociation = BinaryAssociation(
    name="methods64",
    ends={
        Property(name="Method66", type=SQL2003_V2_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured65", type=SQL2003_V2_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typed67: BinaryAssociation = BinaryAssociation(
    name="typed67",
    ends={
        Property(name="TypedTable", type=SQL2003_V2_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured68", type=SQL2003_V2_TypedTable, multiplicity=Multiplicity(0, 9999))
    }
)
schema69: BinaryAssociation = BinaryAssociation(
    name="schema69",
    ends={
        Property(name="Schema70", type=SQL2003_V2_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=SQL2003_V2_Schema, multiplicity=Multiplicity(1, 1))
    }
)
columns71: BinaryAssociation = BinaryAssociation(
    name="columns71",
    ends={
        Property(name="Column", type=SQL2003_V2_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=SQL2003_V2_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views72: BinaryAssociation = BinaryAssociation(
    name="views72",
    ends={
        Property(name="View74", type=SQL2003_V2_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables73", type=SQL2003_V2_View, multiplicity=Multiplicity(0, 9999))
    }
)
restrictions75: BinaryAssociation = BinaryAssociation(
    name="restrictions75",
    ends={
        Property(name="Restriction77", type=SQL2003_V2_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table76", type=SQL2003_V2_Restriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description78: BinaryAssociation = BinaryAssociation(
    name="description78",
    ends={
        Property(name="TriggerDescriptor", type=SQL2003_V2_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="trigger", type=SQL2003_V2_TriggerDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateColumns79: BinaryAssociation = BinaryAssociation(
    name="updateColumns79",
    ends={
        Property(name="SQL2003_V2_StructuralComponent80", type=SQL2003_V2_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V2_Trigger", type=SQL2003_V2_StructuralComponent, multiplicity=Multiplicity(0, 1))
    }
)
trigger81: BinaryAssociation = BinaryAssociation(
    name="trigger81",
    ends={
        Property(name="Trigger", type=SQL2003_V2_TriggerDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="description", type=SQL2003_V2_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
structured82: BinaryAssociation = BinaryAssociation(
    name="structured82",
    ends={
        Property(name="StructuredType83", type=SQL2003_V2_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="typed", type=SQL2003_V2_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
supertable85: BinaryAssociation = BinaryAssociation(
    name="supertable85",
    ends={
        Property(name="TypedTable86", type=SQL2003_V2_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="subtables", type=SQL2003_V2_TypedTable, multiplicity=Multiplicity(0, 1))
    }
)
subtables88: BinaryAssociation = BinaryAssociation(
    name="subtables88",
    ends={
        Property(name="TypedTable89", type=SQL2003_V2_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="supertable", type=SQL2003_V2_TypedTable, multiplicity=Multiplicity(0, 9999))
    }
)
schema95: BinaryAssociation = BinaryAssociation(
    name="schema95",
    ends={
        Property(name="Schema96", type=SQL2003_V2_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="domains", type=SQL2003_V2_Schema, multiplicity=Multiplicity(1, 1))
    }
)
tables90: BinaryAssociation = BinaryAssociation(
    name="tables90",
    ends={
        Property(name="Table91", type=SQL2003_V2_View, multiplicity=Multiplicity(1, 1)),
        Property(name="views", type=SQL2003_V2_Table, multiplicity=Multiplicity(1, 9999))
    }
)
components92: BinaryAssociation = BinaryAssociation(
    name="components92",
    ends={
        Property(name="StructuralComponent94", type=SQL2003_V2_View, multiplicity=Multiplicity(1, 1)),
        Property(name="views93", type=SQL2003_V2_StructuralComponent, multiplicity=Multiplicity(0, 9999))
    }
)
defines97: BinaryAssociation = BinaryAssociation(
    name="defines97",
    ends={
        Property(name="StructuralComponent98", type=SQL2003_V2_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="has_domain", type=SQL2003_V2_StructuralComponent, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_SQL2003_V2_BinaryStringType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V2_BinaryStringType)
gen_SQL2003_V2_ARRAY_CollectionType = Generalization(general=CollectionType, specific=SQL2003_V2_ARRAY)
gen_SQL2003_V2_Attribute_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_V2_Attribute)
gen_SQL2003_V2_BaseTable_Table = Generalization(general=Table, specific=SQL2003_V2_BaseTable)
gen_SQL2003_V2_DatetimeType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V2_DatetimeType)
gen_SQL2003_V2_BooleanType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V2_BooleanType)
gen_SQL2003_V2_CharacterStringType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V2_CharacterStringType)
gen_SQL2003_V2_CollectionType_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_V2_CollectionType)
gen_SQL2003_V2_Column_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_V2_Column)
gen_SQL2003_V2_ColumnConstraint_Restriction = Generalization(general=Restriction, specific=SQL2003_V2_ColumnConstraint)
gen_SQL2003_V2_ConstructedType_DataType = Generalization(general=DataType, specific=SQL2003_V2_ConstructedType)
gen_SQL2003_V2_DatetimeFeature_Feature = Generalization(general=Feature, specific=SQL2003_V2_DatetimeFeature)
gen_SQL2003_V2_DerivedTable_Table = Generalization(general=Table, specific=SQL2003_V2_DerivedTable)
gen_SQL2003_V2_DistinctType_UserDefinedType = Generalization(general=UserDefinedType, specific=SQL2003_V2_DistinctType)
gen_SQL2003_V2_Field_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_V2_Field)
gen_SQL2003_V2_Function_BehaviouralComponent = Generalization(general=BehaviouralComponent, specific=SQL2003_V2_Function)
gen_SQL2003_V2_IntervalFeature_Feature = Generalization(general=Feature, specific=SQL2003_V2_IntervalFeature)
gen_SQL2003_V2_IntervalType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V2_IntervalType)
gen_SQL2003_V2_NumericFeature_Feature = Generalization(general=Feature, specific=SQL2003_V2_NumericFeature)
gen_SQL2003_V2_MULTISET_CollectionType = Generalization(general=CollectionType, specific=SQL2003_V2_MULTISET)
gen_SQL2003_V2_MethodParameter_Parameter = Generalization(general=Parameter_, specific=SQL2003_V2_MethodParameter)
gen_SQL2003_V2_NotNull_ColumnConstraint = Generalization(general=ColumnConstraint, specific=SQL2003_V2_NotNull)
gen_SQL2003_V2_NumericType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V2_NumericType)
gen_SQL2003_V2_ParameterWithMode_Parameter = Generalization(general=Parameter_, specific=SQL2003_V2_ParameterWithMode)
gen_SQL2003_V2_PredefinedType_DataType = Generalization(general=DataType, specific=SQL2003_V2_PredefinedType)
gen_SQL2003_V2_PrimaryKey_UniqueConstraint = Generalization(general=UniqueConstraint, specific=SQL2003_V2_PrimaryKey)
gen_SQL2003_V2_Procedure_BehaviouralComponent = Generalization(general=BehaviouralComponent, specific=SQL2003_V2_Procedure)
gen_SQL2003_V2_ROW_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_V2_ROW)
gen_SQL2003_V2_ReferenceType_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_V2_ReferenceType)
gen_SQL2003_V2_ReferentialConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_V2_ReferentialConstraint)
gen_SQL2003_V2_StringFeature_Feature = Generalization(general=Feature, specific=SQL2003_V2_StringFeature)
gen_SQL2003_V2_StructuredType_UserDefinedType = Generalization(general=UserDefinedType, specific=SQL2003_V2_StructuredType)
gen_SQL2003_V2_TableConstraint_Restriction = Generalization(general=Restriction, specific=SQL2003_V2_TableConstraint)
gen_SQL2003_V2_TableCheckConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_V2_TableCheckConstraint)
gen_SQL2003_V2_Trigger_Restriction = Generalization(general=Restriction, specific=SQL2003_V2_Trigger)
gen_SQL2003_V2_TypedTable_BaseTable = Generalization(general=BaseTable, specific=SQL2003_V2_TypedTable)
gen_SQL2003_V2_UniqueConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_V2_UniqueConstraint)
gen_SQL2003_V2_UserDefinedType_DataType = Generalization(general=DataType, specific=SQL2003_V2_UserDefinedType)
gen_SQL2003_V2_View_DerivedTable = Generalization(general=DerivedTable, specific=SQL2003_V2_View)
gen_SQL2003_V2_XMLType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V2_XMLType)

# Domain Model
domain_model = DomainModel(
    name="SQL2003_V2",
    types={SQL2003_V2_BinaryStringType, PredefinedType, SQL2003_V2_ARRAY, CollectionType, SQL2003_V2_Attribute, StructuralComponent, SQL2003_V2_StructuredType, SQL2003_V2_BaseTable, Table, SQL2003_V2_BehaviouralComponent, SQL2003_V2_Schema, SQL2003_V2_ParameterWithMode, SQL2003_V2_DatetimeType, SQL2003_V2_BooleanType, SQL2003_V2_CharacterStringType, SQL2003_V2_CollectionType, ConstructedType, SQL2003_V2_DataType, SQL2003_V2_Column, SQL2003_V2_Table, SQL2003_V2_ColumnConstraint, Restriction, SQL2003_V2_ConstructedType, DataType, SQL2003_V2_DatetimeFeature, Feature, SQL2003_V2_DerivedTable, SQL2003_V2_DistinctType, UserDefinedType, SQL2003_V2_PredefinedType, SQL2003_V2_Feature, SQL2003_V2_Field, SQL2003_V2_ROW, SQL2003_V2_Function, BehaviouralComponent, SQL2003_V2_IntervalFeature, SQL2003_V2_IntervalType, SQL2003_V2_NumericFeature, SQL2003_V2_MULTISET, SQL2003_V2_Method, SQL2003_V2_MethodParameter, Parameter_, SQL2003_V2_NotNull, ColumnConstraint, SQL2003_V2_NumericType, SQL2003_V2_Parameter, SQL2003_V2_PrimaryKey, UniqueConstraint, SQL2003_V2_Procedure, SQL2003_V2_ReferenceType, SQL2003_V2_ReferentialConstraint, TableConstraint, SQL2003_V2_UniqueConstraint, SQL2003_V2_Restriction, SQL2003_V2_StructuralComponent, SQL2003_V2_View, SQL2003_V2_Domain, SQL2003_V2_StringFeature, SQL2003_V2_TypedTable, SQL2003_V2_TableConstraint, SQL2003_V2_TableCheckConstraint, SQL2003_V2_Trigger, SQL2003_V2_TriggerDescriptor, SQL2003_V2_UserDefinedType, BaseTable, DerivedTable, SQL2003_V2_XMLType, DatetimeFeatures, BinaryStringTypes, BooleanTypes, CharacterStringTypes, DatetimeTypes, IntervalFeatures, IntervalTypes, MatchTypes, Multiplier, NumericRadix, NumericFeatures, NumericTypes, ParameterMode, ReferentialAction, StringFeatures, TriggerActionTime, TriggerEvent, TriggerLevel, Unit, XMLTypes},
    associations={structured0, schema1, parametersWithMode2, super_type4, type5, table7, schema8, source_type10, features11, row12, return_type13, override16, structured17, return_type19, parameters22, method23, super_type29, type24, behaviouralComponent26, is_source_of27, fields31, sub_types33, type35, tables45, references36, table37, columns39, behaviouralComponents41, datatypes43, views52, domains48, type50, restrictions53, features55, has_domain58, super_type61, attributes63, methods64, typed67, schema69, columns71, views72, restrictions75, description78, updateColumns79, trigger81, structured82, supertable85, subtables88, schema95, tables90, components92, defines97},
    generalizations={gen_SQL2003_V2_BinaryStringType_PredefinedType, gen_SQL2003_V2_ARRAY_CollectionType, gen_SQL2003_V2_Attribute_StructuralComponent, gen_SQL2003_V2_BaseTable_Table, gen_SQL2003_V2_DatetimeType_PredefinedType, gen_SQL2003_V2_BooleanType_PredefinedType, gen_SQL2003_V2_CharacterStringType_PredefinedType, gen_SQL2003_V2_CollectionType_ConstructedType, gen_SQL2003_V2_Column_StructuralComponent, gen_SQL2003_V2_ColumnConstraint_Restriction, gen_SQL2003_V2_ConstructedType_DataType, gen_SQL2003_V2_DatetimeFeature_Feature, gen_SQL2003_V2_DerivedTable_Table, gen_SQL2003_V2_DistinctType_UserDefinedType, gen_SQL2003_V2_Field_StructuralComponent, gen_SQL2003_V2_Function_BehaviouralComponent, gen_SQL2003_V2_IntervalFeature_Feature, gen_SQL2003_V2_IntervalType_PredefinedType, gen_SQL2003_V2_NumericFeature_Feature, gen_SQL2003_V2_MULTISET_CollectionType, gen_SQL2003_V2_MethodParameter_Parameter, gen_SQL2003_V2_NotNull_ColumnConstraint, gen_SQL2003_V2_NumericType_PredefinedType, gen_SQL2003_V2_ParameterWithMode_Parameter, gen_SQL2003_V2_PredefinedType_DataType, gen_SQL2003_V2_PrimaryKey_UniqueConstraint, gen_SQL2003_V2_Procedure_BehaviouralComponent, gen_SQL2003_V2_ROW_ConstructedType, gen_SQL2003_V2_ReferenceType_ConstructedType, gen_SQL2003_V2_ReferentialConstraint_TableConstraint, gen_SQL2003_V2_StringFeature_Feature, gen_SQL2003_V2_StructuredType_UserDefinedType, gen_SQL2003_V2_TableConstraint_Restriction, gen_SQL2003_V2_TableCheckConstraint_TableConstraint, gen_SQL2003_V2_Trigger_Restriction, gen_SQL2003_V2_TypedTable_BaseTable, gen_SQL2003_V2_UniqueConstraint_TableConstraint, gen_SQL2003_V2_UserDefinedType_DataType, gen_SQL2003_V2_View_DerivedTable, gen_SQL2003_V2_XMLType_PredefinedType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)