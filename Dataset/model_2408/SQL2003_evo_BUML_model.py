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
            EnumerationLiteral(name="DAY_SECOND"),
			EnumerationLiteral(name="HOUR_MINUTE"),
			EnumerationLiteral(name="YEAR_MONTH"),
			EnumerationLiteral(name="DAY_HOUR"),
			EnumerationLiteral(name="DAY_MINUTE"),
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

MatchTypes: Enumeration = Enumeration(
    name="MatchTypes",
    literals={
            EnumerationLiteral(name="SIMPLE"),
			EnumerationLiteral(name="PARTIAL"),
			EnumerationLiteral(name="TOTAL")
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
            EnumerationLiteral(name="CHARACTERS"),
			EnumerationLiteral(name="OCTETS")
    }
)

XMLTypes: Enumeration = Enumeration(
    name="XMLTypes",
    literals={
            EnumerationLiteral(name="XMLTYPE")
    }
)

# Classes
SQL2003_evo_ARRAY = Class(name="SQL2003::evo::ARRAY")
CollectionType = Class(name="CollectionType")
SQL2003_evo_Attribute = Class(name="SQL2003::evo::Attribute")
StructuralComponent = Class(name="StructuralComponent")
SQL2003_evo_StructuredType = Class(name="SQL2003::evo::StructuredType")
SQL2003_evo_BaseTable = Class(name="SQL2003::evo::BaseTable")
Table = Class(name="Table")
SQL2003_evo_BehaviouralComponent = Class(name="SQL2003::evo::BehaviouralComponent", is_abstract=True)
SQL2003_evo_Schema = Class(name="SQL2003::evo::Schema")
SQL2003_evo_ParameterWithMode = Class(name="SQL2003::evo::ParameterWithMode")
SQL2003_evo_BinaryStringType = Class(name="SQL2003::evo::BinaryStringType")
PredefinedType = Class(name="PredefinedType")
SQL2003_evo_BooleanType = Class(name="SQL2003::evo::BooleanType")
SQL2003_evo_CharacterStringType = Class(name="SQL2003::evo::CharacterStringType")
SQL2003_evo_Table = Class(name="SQL2003::evo::Table", is_abstract=True)
SQL2003_evo_CollectionType = Class(name="SQL2003::evo::CollectionType", is_abstract=True)
ConstructedType = Class(name="ConstructedType")
SQL2003_evo_DataType = Class(name="SQL2003::evo::DataType", is_abstract=True)
SQL2003_evo_Column = Class(name="SQL2003::evo::Column")
SQL2003_evo_ColumnConstraint = Class(name="SQL2003::evo::ColumnConstraint", is_abstract=True)
Restriction = Class(name="Restriction")
SQL2003_evo_ConstructedType = Class(name="SQL2003::evo::ConstructedType", is_abstract=True)
DataType = Class(name="DataType")
SQL2003_evo_DatetimeFeature = Class(name="SQL2003::evo::DatetimeFeature")
Feature = Class(name="Feature")
SQL2003_evo_Field = Class(name="SQL2003::evo::Field")
SQL2003_evo_DatetimeType = Class(name="SQL2003::evo::DatetimeType")
SQL2003_evo_DerivedTable = Class(name="SQL2003::evo::DerivedTable")
SQL2003_evo_DistinctType = Class(name="SQL2003::evo::DistinctType")
UserDefinedType = Class(name="UserDefinedType")
SQL2003_evo_PredefinedType = Class(name="SQL2003::evo::PredefinedType", is_abstract=True)
SQL2003_evo_Feature = Class(name="SQL2003::evo::Feature", is_abstract=True)
SQL2003_evo_ROW = Class(name="SQL2003::evo::ROW")
SQL2003_evo_Function = Class(name="SQL2003::evo::Function")
BehaviouralComponent = Class(name="BehaviouralComponent")
SQL2003_evo_IntervalFeature = Class(name="SQL2003::evo::IntervalFeature")
SQL2003_evo_IntervalType = Class(name="SQL2003::evo::IntervalType")
SQL2003_evo_MethodParameter = Class(name="SQL2003::evo::MethodParameter")
SQL2003_evo_MULTISET = Class(name="SQL2003::evo::MULTISET")
SQL2003_evo_Method = Class(name="SQL2003::evo::Method")
Parameter_ = Class(name="Parameter")
SQL2003_evo_NotNull = Class(name="SQL2003::evo::NotNull")
ColumnConstraint = Class(name="ColumnConstraint")
SQL2003_evo_NumericFeature = Class(name="SQL2003::evo::NumericFeature")
SQL2003_evo_NumericType = Class(name="SQL2003::evo::NumericType")
SQL2003_evo_PrimaryKey = Class(name="SQL2003::evo::PrimaryKey")
UniqueConstraint = Class(name="UniqueConstraint")
SQL2003_evo_Procedure = Class(name="SQL2003::evo::Procedure")
SQL2003_evo_Parameter = Class(name="SQL2003::evo::Parameter", is_abstract=True)
SQL2003_evo_ReferenceType = Class(name="SQL2003::evo::ReferenceType")
SQL2003_evo_ReferentialConstraint = Class(name="SQL2003::evo::ReferentialConstraint")
TableConstraint = Class(name="TableConstraint")
SQL2003_evo_UniqueConstraint = Class(name="SQL2003::evo::UniqueConstraint")
SQL2003_evo_Restriction = Class(name="SQL2003::evo::Restriction", is_abstract=True)
SQL2003_evo_StructuralComponent = Class(name="SQL2003::evo::StructuralComponent", is_abstract=True)
SQL2003_evo_StringFeature = Class(name="SQL2003::evo::StringFeature")
SQL2003_evo_View = Class(name="SQL2003::evo::View")
SQL2003_evo_TypedTable = Class(name="SQL2003::evo::TypedTable")
SQL2003_evo_TableCheckConstraint = Class(name="SQL2003::evo::TableCheckConstraint")
SQL2003_evo_TableConstraint = Class(name="SQL2003::evo::TableConstraint", is_abstract=True)
SQL2003_evo_Trigger = Class(name="SQL2003::evo::Trigger")
SQL2003_evo_TriggerDescriptor = Class(name="SQL2003::evo::TriggerDescriptor")
BaseTable = Class(name="BaseTable")
SQL2003_evo_UserDefinedType = Class(name="SQL2003::evo::UserDefinedType", is_abstract=True)
DerivedTable = Class(name="DerivedTable")
SQL2003_evo_XMLType = Class(name="SQL2003::evo::XMLType")

# SQL2003_evo_ARRAY class attributes and methods
SQL2003_evo_ARRAY_num_elements: Property = Property(name="num_elements", type=StringType)
SQL2003_evo_ARRAY.attributes={SQL2003_evo_ARRAY_num_elements}

# CollectionType class attributes and methods

# SQL2003_evo_Attribute class attributes and methods
SQL2003_evo_Attribute_default: Property = Property(name="default", type=StringType)
SQL2003_evo_Attribute.attributes={SQL2003_evo_Attribute_default}

# StructuralComponent class attributes and methods

# SQL2003_evo_StructuredType class attributes and methods
SQL2003_evo_StructuredType_is_final: Property = Property(name="is_final", type=BooleanType)
SQL2003_evo_StructuredType_is_instantiable: Property = Property(name="is_instantiable", type=BooleanType)
SQL2003_evo_StructuredType.attributes={SQL2003_evo_StructuredType_is_final, SQL2003_evo_StructuredType_is_instantiable}

# SQL2003_evo_BaseTable class attributes and methods

# Table class attributes and methods

# SQL2003_evo_BehaviouralComponent class attributes and methods
SQL2003_evo_BehaviouralComponent_name: Property = Property(name="name", type=StringType)
SQL2003_evo_BehaviouralComponent_body: Property = Property(name="body", type=StringType)
SQL2003_evo_BehaviouralComponent.attributes={SQL2003_evo_BehaviouralComponent_body, SQL2003_evo_BehaviouralComponent_name}

# SQL2003_evo_Schema class attributes and methods
SQL2003_evo_Schema_name: Property = Property(name="name", type=StringType)
SQL2003_evo_Schema.attributes={SQL2003_evo_Schema_name}

# SQL2003_evo_ParameterWithMode class attributes and methods
SQL2003_evo_ParameterWithMode_mode: Property = Property(name="mode", type=StringType)
SQL2003_evo_ParameterWithMode.attributes={SQL2003_evo_ParameterWithMode_mode}

# SQL2003_evo_BinaryStringType class attributes and methods
SQL2003_evo_BinaryStringType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_evo_BinaryStringType_length_def: Property = Property(name="length_def", type=StringType)
SQL2003_evo_BinaryStringType.attributes={SQL2003_evo_BinaryStringType_descriptor, SQL2003_evo_BinaryStringType_length_def}

# PredefinedType class attributes and methods

# SQL2003_evo_BooleanType class attributes and methods
SQL2003_evo_BooleanType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_evo_BooleanType.attributes={SQL2003_evo_BooleanType_descriptor}

# SQL2003_evo_CharacterStringType class attributes and methods
SQL2003_evo_CharacterStringType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_evo_CharacterStringType_length_def: Property = Property(name="length_def", type=StringType)
SQL2003_evo_CharacterStringType.attributes={SQL2003_evo_CharacterStringType_length_def, SQL2003_evo_CharacterStringType_descriptor}

# SQL2003_evo_Table class attributes and methods
SQL2003_evo_Table_name: Property = Property(name="name", type=StringType)
SQL2003_evo_Table.attributes={SQL2003_evo_Table_name}

# SQL2003_evo_CollectionType class attributes and methods

# ConstructedType class attributes and methods

# SQL2003_evo_DataType class attributes and methods

# SQL2003_evo_Column class attributes and methods
SQL2003_evo_Column_default: Property = Property(name="default", type=StringType)
SQL2003_evo_Column.attributes={SQL2003_evo_Column_default}

# SQL2003_evo_ColumnConstraint class attributes and methods

# Restriction class attributes and methods

# SQL2003_evo_ConstructedType class attributes and methods
SQL2003_evo_ConstructedType_name: Property = Property(name="name", type=StringType)
SQL2003_evo_ConstructedType.attributes={SQL2003_evo_ConstructedType_name}

# DataType class attributes and methods

# SQL2003_evo_DatetimeFeature class attributes and methods
SQL2003_evo_DatetimeFeature_key: Property = Property(name="key", type=StringType)
SQL2003_evo_DatetimeFeature_value: Property = Property(name="value", type=StringType)
SQL2003_evo_DatetimeFeature.attributes={SQL2003_evo_DatetimeFeature_value, SQL2003_evo_DatetimeFeature_key}

# Feature class attributes and methods

# SQL2003_evo_Field class attributes and methods

# SQL2003_evo_DatetimeType class attributes and methods
SQL2003_evo_DatetimeType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_evo_DatetimeType.attributes={SQL2003_evo_DatetimeType_descriptor}

# SQL2003_evo_DerivedTable class attributes and methods
SQL2003_evo_DerivedTable_query_expression: Property = Property(name="query_expression", type=StringType)
SQL2003_evo_DerivedTable.attributes={SQL2003_evo_DerivedTable_query_expression}

# SQL2003_evo_DistinctType class attributes and methods

# UserDefinedType class attributes and methods

# SQL2003_evo_PredefinedType class attributes and methods

# SQL2003_evo_Feature class attributes and methods

# SQL2003_evo_ROW class attributes and methods

# SQL2003_evo_Function class attributes and methods

# BehaviouralComponent class attributes and methods

# SQL2003_evo_IntervalFeature class attributes and methods
SQL2003_evo_IntervalFeature_key: Property = Property(name="key", type=StringType)
SQL2003_evo_IntervalFeature_value: Property = Property(name="value", type=StringType)
SQL2003_evo_IntervalFeature.attributes={SQL2003_evo_IntervalFeature_value, SQL2003_evo_IntervalFeature_key}

# SQL2003_evo_IntervalType class attributes and methods
SQL2003_evo_IntervalType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_evo_IntervalType.attributes={SQL2003_evo_IntervalType_descriptor}

# SQL2003_evo_MethodParameter class attributes and methods

# SQL2003_evo_MULTISET class attributes and methods

# SQL2003_evo_Method class attributes and methods
SQL2003_evo_Method_name: Property = Property(name="name", type=StringType)
SQL2003_evo_Method_body: Property = Property(name="body", type=StringType)
SQL2003_evo_Method.attributes={SQL2003_evo_Method_body, SQL2003_evo_Method_name}

# Parameter class attributes and methods

# SQL2003_evo_NotNull class attributes and methods

# ColumnConstraint class attributes and methods

# SQL2003_evo_NumericFeature class attributes and methods
SQL2003_evo_NumericFeature_key: Property = Property(name="key", type=StringType)
SQL2003_evo_NumericFeature_value: Property = Property(name="value", type=StringType)
SQL2003_evo_NumericFeature.attributes={SQL2003_evo_NumericFeature_key, SQL2003_evo_NumericFeature_value}

# SQL2003_evo_NumericType class attributes and methods
SQL2003_evo_NumericType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_evo_NumericType.attributes={SQL2003_evo_NumericType_descriptor}

# SQL2003_evo_PrimaryKey class attributes and methods

# UniqueConstraint class attributes and methods

# SQL2003_evo_Procedure class attributes and methods

# SQL2003_evo_Parameter class attributes and methods
SQL2003_evo_Parameter_name: Property = Property(name="name", type=StringType)
SQL2003_evo_Parameter.attributes={SQL2003_evo_Parameter_name}

# SQL2003_evo_ReferenceType class attributes and methods

# SQL2003_evo_ReferentialConstraint class attributes and methods
SQL2003_evo_ReferentialConstraint_delete_action: Property = Property(name="delete_action", type=StringType)
SQL2003_evo_ReferentialConstraint_update_action: Property = Property(name="update_action", type=StringType)
SQL2003_evo_ReferentialConstraint_match: Property = Property(name="match", type=StringType)
SQL2003_evo_ReferentialConstraint.attributes={SQL2003_evo_ReferentialConstraint_update_action, SQL2003_evo_ReferentialConstraint_delete_action, SQL2003_evo_ReferentialConstraint_match}

# TableConstraint class attributes and methods

# SQL2003_evo_UniqueConstraint class attributes and methods

# SQL2003_evo_Restriction class attributes and methods

# SQL2003_evo_StructuralComponent class attributes and methods
SQL2003_evo_StructuralComponent_name: Property = Property(name="name", type=StringType)
SQL2003_evo_StructuralComponent.attributes={SQL2003_evo_StructuralComponent_name}

# SQL2003_evo_StringFeature class attributes and methods
SQL2003_evo_StringFeature_key: Property = Property(name="key", type=StringType)
SQL2003_evo_StringFeature_value: Property = Property(name="value", type=StringType)
SQL2003_evo_StringFeature.attributes={SQL2003_evo_StringFeature_value, SQL2003_evo_StringFeature_key}

# SQL2003_evo_View class attributes and methods

# SQL2003_evo_TypedTable class attributes and methods

# SQL2003_evo_TableCheckConstraint class attributes and methods
SQL2003_evo_TableCheckConstraint_expression: Property = Property(name="expression", type=StringType)
SQL2003_evo_TableCheckConstraint.attributes={SQL2003_evo_TableCheckConstraint_expression}

# SQL2003_evo_TableConstraint class attributes and methods
SQL2003_evo_TableConstraint_name: Property = Property(name="name", type=StringType)
SQL2003_evo_TableConstraint.attributes={SQL2003_evo_TableConstraint_name}

# SQL2003_evo_Trigger class attributes and methods
SQL2003_evo_Trigger_name: Property = Property(name="name", type=StringType)
SQL2003_evo_Trigger.attributes={SQL2003_evo_Trigger_name}

# SQL2003_evo_TriggerDescriptor class attributes and methods
SQL2003_evo_TriggerDescriptor_event: Property = Property(name="event", type=StringType)
SQL2003_evo_TriggerDescriptor_actionTime: Property = Property(name="actionTime", type=StringType)
SQL2003_evo_TriggerDescriptor_triggeredAction: Property = Property(name="triggeredAction", type=StringType)
SQL2003_evo_TriggerDescriptor_level: Property = Property(name="level", type=StringType)
SQL2003_evo_TriggerDescriptor.attributes={SQL2003_evo_TriggerDescriptor_level, SQL2003_evo_TriggerDescriptor_triggeredAction, SQL2003_evo_TriggerDescriptor_actionTime, SQL2003_evo_TriggerDescriptor_event}

# BaseTable class attributes and methods

# SQL2003_evo_UserDefinedType class attributes and methods
SQL2003_evo_UserDefinedType_name: Property = Property(name="name", type=StringType)
SQL2003_evo_UserDefinedType.attributes={SQL2003_evo_UserDefinedType_name}

# DerivedTable class attributes and methods

# SQL2003_evo_XMLType class attributes and methods
SQL2003_evo_XMLType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_evo_XMLType.attributes={SQL2003_evo_XMLType_descriptor}

# Relationships
schema1: BinaryAssociation = BinaryAssociation(
    name="schema1",
    ends={
        Property(name="Schema", type=SQL2003_evo_BehaviouralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralComponents", type=SQL2003_evo_Schema, multiplicity=Multiplicity(1, 1))
    }
)
parametersWithMode2: BinaryAssociation = BinaryAssociation(
    name="parametersWithMode2",
    ends={
        Property(name="ParameterWithMode", type=SQL2003_evo_BehaviouralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralComponent", type=SQL2003_evo_ParameterWithMode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structured0: BinaryAssociation = BinaryAssociation(
    name="structured0",
    ends={
        Property(name="StructuredType", type=SQL2003_evo_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=SQL2003_evo_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
super_type4: BinaryAssociation = BinaryAssociation(
    name="super_type4",
    ends={
        Property(name="SQL2003_evo_CollectionType", type=SQL2003_evo_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_CollectionType3", type=SQL2003_evo_CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="SQL2003_evo_DataType", type=SQL2003_evo_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_CollectionType6", type=SQL2003_evo_DataType, multiplicity=Multiplicity(1, 1))
    }
)
table7: BinaryAssociation = BinaryAssociation(
    name="table7",
    ends={
        Property(name="Table", type=SQL2003_evo_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=SQL2003_evo_Table, multiplicity=Multiplicity(1, 1))
    }
)
schema8: BinaryAssociation = BinaryAssociation(
    name="schema8",
    ends={
        Property(name="Schema9", type=SQL2003_evo_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes", type=SQL2003_evo_Schema, multiplicity=Multiplicity(1, 1))
    }
)
source_type10: BinaryAssociation = BinaryAssociation(
    name="source_type10",
    ends={
        Property(name="PredefinedType", type=SQL2003_evo_DistinctType, multiplicity=Multiplicity(1, 1)),
        Property(name="is_source_of", type=SQL2003_evo_PredefinedType, multiplicity=Multiplicity(1, 1))
    }
)
features11: BinaryAssociation = BinaryAssociation(
    name="features11",
    ends={
        Property(name="SQL2003_evo_Feature", type=SQL2003_evo_DistinctType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_DistinctType", type=SQL2003_evo_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
row12: BinaryAssociation = BinaryAssociation(
    name="row12",
    ends={
        Property(name="ROW", type=SQL2003_evo_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=SQL2003_evo_ROW, multiplicity=Multiplicity(1, 1))
    }
)
return_type13: BinaryAssociation = BinaryAssociation(
    name="return_type13",
    ends={
        Property(name="SQL2003_evo_DataType14", type=SQL2003_evo_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_Function", type=SQL2003_evo_DataType, multiplicity=Multiplicity(1, 1))
    }
)
parameters22: BinaryAssociation = BinaryAssociation(
    name="parameters22",
    ends={
        Property(name="MethodParameter", type=SQL2003_evo_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=SQL2003_evo_MethodParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
override16: BinaryAssociation = BinaryAssociation(
    name="override16",
    ends={
        Property(name="SQL2003_evo_Method", type=SQL2003_evo_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_Method15", type=SQL2003_evo_Method, multiplicity=Multiplicity(0, 1))
    }
)
structured17: BinaryAssociation = BinaryAssociation(
    name="structured17",
    ends={
        Property(name="StructuredType18", type=SQL2003_evo_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=SQL2003_evo_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
return_type19: BinaryAssociation = BinaryAssociation(
    name="return_type19",
    ends={
        Property(name="SQL2003_evo_DataType21", type=SQL2003_evo_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_Method20", type=SQL2003_evo_DataType, multiplicity=Multiplicity(1, 1))
    }
)
method23: BinaryAssociation = BinaryAssociation(
    name="method23",
    ends={
        Property(name="Method", type=SQL2003_evo_MethodParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=SQL2003_evo_Method, multiplicity=Multiplicity(1, 1))
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="SQL2003_evo_DataType25", type=SQL2003_evo_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_Parameter", type=SQL2003_evo_DataType, multiplicity=Multiplicity(1, 1))
    }
)
behaviouralComponent26: BinaryAssociation = BinaryAssociation(
    name="behaviouralComponent26",
    ends={
        Property(name="BehaviouralComponent", type=SQL2003_evo_ParameterWithMode, multiplicity=Multiplicity(1, 1)),
        Property(name="parametersWithMode", type=SQL2003_evo_BehaviouralComponent, multiplicity=Multiplicity(1, 1))
    }
)
is_source_of27: BinaryAssociation = BinaryAssociation(
    name="is_source_of27",
    ends={
        Property(name="DistinctType", type=SQL2003_evo_PredefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="source_type", type=SQL2003_evo_DistinctType, multiplicity=Multiplicity(0, 9999))
    }
)
references36: BinaryAssociation = BinaryAssociation(
    name="references36",
    ends={
        Property(name="SQL2003_evo_UniqueConstraint", type=SQL2003_evo_ReferentialConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_ReferentialConstraint", type=SQL2003_evo_UniqueConstraint, multiplicity=Multiplicity(1, 1))
    }
)
super_type29: BinaryAssociation = BinaryAssociation(
    name="super_type29",
    ends={
        Property(name="ROW30", type=SQL2003_evo_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="sub_types", type=SQL2003_evo_ROW, multiplicity=Multiplicity(0, 1))
    }
)
fields31: BinaryAssociation = BinaryAssociation(
    name="fields31",
    ends={
        Property(name="Field", type=SQL2003_evo_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="row", type=SQL2003_evo_Field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sub_types33: BinaryAssociation = BinaryAssociation(
    name="sub_types33",
    ends={
        Property(name="ROW34", type=SQL2003_evo_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="super_type", type=SQL2003_evo_ROW, multiplicity=Multiplicity(0, 9999))
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="SQL2003_evo_StructuredType", type=SQL2003_evo_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_ReferenceType", type=SQL2003_evo_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
table37: BinaryAssociation = BinaryAssociation(
    name="table37",
    ends={
        Property(name="Table38", type=SQL2003_evo_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictions", type=SQL2003_evo_Table, multiplicity=Multiplicity(1, 1))
    }
)
columns39: BinaryAssociation = BinaryAssociation(
    name="columns39",
    ends={
        Property(name="StructuralComponent", type=SQL2003_evo_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictions40", type=SQL2003_evo_StructuralComponent, multiplicity=Multiplicity(1, 9999))
    }
)
behaviouralComponents41: BinaryAssociation = BinaryAssociation(
    name="behaviouralComponents41",
    ends={
        Property(name="BehaviouralComponent42", type=SQL2003_evo_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=SQL2003_evo_BehaviouralComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypes43: BinaryAssociation = BinaryAssociation(
    name="datatypes43",
    ends={
        Property(name="DataType", type=SQL2003_evo_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema44", type=SQL2003_evo_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables45: BinaryAssociation = BinaryAssociation(
    name="tables45",
    ends={
        Property(name="Table47", type=SQL2003_evo_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema46", type=SQL2003_evo_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema65: BinaryAssociation = BinaryAssociation(
    name="schema65",
    ends={
        Property(name="Schema66", type=SQL2003_evo_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=SQL2003_evo_Schema, multiplicity=Multiplicity(1, 1))
    }
)
type48: BinaryAssociation = BinaryAssociation(
    name="type48",
    ends={
        Property(name="SQL2003_evo_DataType49", type=SQL2003_evo_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_StructuralComponent", type=SQL2003_evo_DataType, multiplicity=Multiplicity(1, 1))
    }
)
views50: BinaryAssociation = BinaryAssociation(
    name="views50",
    ends={
        Property(name="View", type=SQL2003_evo_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components", type=SQL2003_evo_View, multiplicity=Multiplicity(0, 9999))
    }
)
restrictions51: BinaryAssociation = BinaryAssociation(
    name="restrictions51",
    ends={
        Property(name="Restriction", type=SQL2003_evo_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="columns52", type=SQL2003_evo_Restriction, multiplicity=Multiplicity(0, 9999))
    }
)
features53: BinaryAssociation = BinaryAssociation(
    name="features53",
    ends={
        Property(name="SQL2003_evo_Feature55", type=SQL2003_evo_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_StructuralComponent54", type=SQL2003_evo_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super_type57: BinaryAssociation = BinaryAssociation(
    name="super_type57",
    ends={
        Property(name="SQL2003_evo_StructuredType58", type=SQL2003_evo_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_StructuredType56", type=SQL2003_evo_StructuredType, multiplicity=Multiplicity(0, 1))
    }
)
attributes59: BinaryAssociation = BinaryAssociation(
    name="attributes59",
    ends={
        Property(name="Attribute", type=SQL2003_evo_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured", type=SQL2003_evo_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods60: BinaryAssociation = BinaryAssociation(
    name="methods60",
    ends={
        Property(name="Method62", type=SQL2003_evo_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured61", type=SQL2003_evo_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typed63: BinaryAssociation = BinaryAssociation(
    name="typed63",
    ends={
        Property(name="TypedTable", type=SQL2003_evo_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured64", type=SQL2003_evo_TypedTable, multiplicity=Multiplicity(0, 9999))
    }
)
columns67: BinaryAssociation = BinaryAssociation(
    name="columns67",
    ends={
        Property(name="Column", type=SQL2003_evo_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=SQL2003_evo_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views68: BinaryAssociation = BinaryAssociation(
    name="views68",
    ends={
        Property(name="View70", type=SQL2003_evo_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables69", type=SQL2003_evo_View, multiplicity=Multiplicity(0, 9999))
    }
)
restrictions71: BinaryAssociation = BinaryAssociation(
    name="restrictions71",
    ends={
        Property(name="Restriction73", type=SQL2003_evo_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table72", type=SQL2003_evo_Restriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description74: BinaryAssociation = BinaryAssociation(
    name="description74",
    ends={
        Property(name="TriggerDescriptor", type=SQL2003_evo_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="trigger", type=SQL2003_evo_TriggerDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateColumns75: BinaryAssociation = BinaryAssociation(
    name="updateColumns75",
    ends={
        Property(name="SQL2003_evo_StructuralComponent76", type=SQL2003_evo_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_evo_Trigger", type=SQL2003_evo_StructuralComponent, multiplicity=Multiplicity(0, 1))
    }
)
subtables84: BinaryAssociation = BinaryAssociation(
    name="subtables84",
    ends={
        Property(name="TypedTable85", type=SQL2003_evo_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="supertable", type=SQL2003_evo_TypedTable, multiplicity=Multiplicity(0, 9999))
    }
)
trigger77: BinaryAssociation = BinaryAssociation(
    name="trigger77",
    ends={
        Property(name="Trigger", type=SQL2003_evo_TriggerDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="description", type=SQL2003_evo_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
structured78: BinaryAssociation = BinaryAssociation(
    name="structured78",
    ends={
        Property(name="StructuredType79", type=SQL2003_evo_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="typed", type=SQL2003_evo_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
supertable81: BinaryAssociation = BinaryAssociation(
    name="supertable81",
    ends={
        Property(name="TypedTable82", type=SQL2003_evo_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="subtables", type=SQL2003_evo_TypedTable, multiplicity=Multiplicity(0, 1))
    }
)
tables86: BinaryAssociation = BinaryAssociation(
    name="tables86",
    ends={
        Property(name="Table87", type=SQL2003_evo_View, multiplicity=Multiplicity(1, 1)),
        Property(name="views", type=SQL2003_evo_Table, multiplicity=Multiplicity(1, 9999))
    }
)
components88: BinaryAssociation = BinaryAssociation(
    name="components88",
    ends={
        Property(name="StructuralComponent90", type=SQL2003_evo_View, multiplicity=Multiplicity(1, 1)),
        Property(name="views89", type=SQL2003_evo_StructuralComponent, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_SQL2003_evo_ARRAY_CollectionType = Generalization(general=CollectionType, specific=SQL2003_evo_ARRAY)
gen_SQL2003_evo_Attribute_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_evo_Attribute)
gen_SQL2003_evo_BaseTable_Table = Generalization(general=Table, specific=SQL2003_evo_BaseTable)
gen_SQL2003_evo_BinaryStringType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_evo_BinaryStringType)
gen_SQL2003_evo_BooleanType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_evo_BooleanType)
gen_SQL2003_evo_CharacterStringType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_evo_CharacterStringType)
gen_SQL2003_evo_CollectionType_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_evo_CollectionType)
gen_SQL2003_evo_Column_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_evo_Column)
gen_SQL2003_evo_ColumnConstraint_Restriction = Generalization(general=Restriction, specific=SQL2003_evo_ColumnConstraint)
gen_SQL2003_evo_ConstructedType_DataType = Generalization(general=DataType, specific=SQL2003_evo_ConstructedType)
gen_SQL2003_evo_DatetimeFeature_Feature = Generalization(general=Feature, specific=SQL2003_evo_DatetimeFeature)
gen_SQL2003_evo_Field_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_evo_Field)
gen_SQL2003_evo_DatetimeType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_evo_DatetimeType)
gen_SQL2003_evo_DerivedTable_Table = Generalization(general=Table, specific=SQL2003_evo_DerivedTable)
gen_SQL2003_evo_DistinctType_UserDefinedType = Generalization(general=UserDefinedType, specific=SQL2003_evo_DistinctType)
gen_SQL2003_evo_Function_BehaviouralComponent = Generalization(general=BehaviouralComponent, specific=SQL2003_evo_Function)
gen_SQL2003_evo_IntervalFeature_Feature = Generalization(general=Feature, specific=SQL2003_evo_IntervalFeature)
gen_SQL2003_evo_IntervalType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_evo_IntervalType)
gen_SQL2003_evo_MULTISET_CollectionType = Generalization(general=CollectionType, specific=SQL2003_evo_MULTISET)
gen_SQL2003_evo_MethodParameter_Parameter = Generalization(general=Parameter_, specific=SQL2003_evo_MethodParameter)
gen_SQL2003_evo_NotNull_ColumnConstraint = Generalization(general=ColumnConstraint, specific=SQL2003_evo_NotNull)
gen_SQL2003_evo_NumericFeature_Feature = Generalization(general=Feature, specific=SQL2003_evo_NumericFeature)
gen_SQL2003_evo_NumericType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_evo_NumericType)
gen_SQL2003_evo_PrimaryKey_UniqueConstraint = Generalization(general=UniqueConstraint, specific=SQL2003_evo_PrimaryKey)
gen_SQL2003_evo_ParameterWithMode_Parameter = Generalization(general=Parameter_, specific=SQL2003_evo_ParameterWithMode)
gen_SQL2003_evo_PredefinedType_DataType = Generalization(general=DataType, specific=SQL2003_evo_PredefinedType)
gen_SQL2003_evo_Procedure_BehaviouralComponent = Generalization(general=BehaviouralComponent, specific=SQL2003_evo_Procedure)
gen_SQL2003_evo_ROW_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_evo_ROW)
gen_SQL2003_evo_ReferenceType_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_evo_ReferenceType)
gen_SQL2003_evo_ReferentialConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_evo_ReferentialConstraint)
gen_SQL2003_evo_StringFeature_Feature = Generalization(general=Feature, specific=SQL2003_evo_StringFeature)
gen_SQL2003_evo_StructuredType_UserDefinedType = Generalization(general=UserDefinedType, specific=SQL2003_evo_StructuredType)
gen_SQL2003_evo_TableCheckConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_evo_TableCheckConstraint)
gen_SQL2003_evo_TableConstraint_Restriction = Generalization(general=Restriction, specific=SQL2003_evo_TableConstraint)
gen_SQL2003_evo_Trigger_Restriction = Generalization(general=Restriction, specific=SQL2003_evo_Trigger)
gen_SQL2003_evo_TypedTable_BaseTable = Generalization(general=BaseTable, specific=SQL2003_evo_TypedTable)
gen_SQL2003_evo_UniqueConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_evo_UniqueConstraint)
gen_SQL2003_evo_UserDefinedType_DataType = Generalization(general=DataType, specific=SQL2003_evo_UserDefinedType)
gen_SQL2003_evo_View_DerivedTable = Generalization(general=DerivedTable, specific=SQL2003_evo_View)
gen_SQL2003_evo_XMLType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_evo_XMLType)

# Domain Model
domain_model = DomainModel(
    name="SQL2003_evo",
    types={SQL2003_evo_ARRAY, CollectionType, SQL2003_evo_Attribute, StructuralComponent, SQL2003_evo_StructuredType, SQL2003_evo_BaseTable, Table, SQL2003_evo_BehaviouralComponent, SQL2003_evo_Schema, SQL2003_evo_ParameterWithMode, SQL2003_evo_BinaryStringType, PredefinedType, SQL2003_evo_BooleanType, SQL2003_evo_CharacterStringType, SQL2003_evo_Table, SQL2003_evo_CollectionType, ConstructedType, SQL2003_evo_DataType, SQL2003_evo_Column, SQL2003_evo_ColumnConstraint, Restriction, SQL2003_evo_ConstructedType, DataType, SQL2003_evo_DatetimeFeature, Feature, SQL2003_evo_Field, SQL2003_evo_DatetimeType, SQL2003_evo_DerivedTable, SQL2003_evo_DistinctType, UserDefinedType, SQL2003_evo_PredefinedType, SQL2003_evo_Feature, SQL2003_evo_ROW, SQL2003_evo_Function, BehaviouralComponent, SQL2003_evo_IntervalFeature, SQL2003_evo_IntervalType, SQL2003_evo_MethodParameter, SQL2003_evo_MULTISET, SQL2003_evo_Method, Parameter_, SQL2003_evo_NotNull, ColumnConstraint, SQL2003_evo_NumericFeature, SQL2003_evo_NumericType, SQL2003_evo_PrimaryKey, UniqueConstraint, SQL2003_evo_Procedure, SQL2003_evo_Parameter, SQL2003_evo_ReferenceType, SQL2003_evo_ReferentialConstraint, TableConstraint, SQL2003_evo_UniqueConstraint, SQL2003_evo_Restriction, SQL2003_evo_StructuralComponent, SQL2003_evo_StringFeature, SQL2003_evo_View, SQL2003_evo_TypedTable, SQL2003_evo_TableCheckConstraint, SQL2003_evo_TableConstraint, SQL2003_evo_Trigger, SQL2003_evo_TriggerDescriptor, BaseTable, SQL2003_evo_UserDefinedType, DerivedTable, SQL2003_evo_XMLType, BinaryStringTypes, BooleanTypes, CharacterStringTypes, DatetimeFeatures, DatetimeTypes, IntervalFeatures, IntervalTypes, MatchTypes, NumericTypes, Multiplier, NumericRadix, NumericFeatures, ParameterMode, ReferentialAction, StringFeatures, TriggerActionTime, TriggerEvent, TriggerLevel, Unit, XMLTypes},
    associations={schema1, parametersWithMode2, structured0, super_type4, type5, table7, schema8, source_type10, features11, row12, return_type13, parameters22, override16, structured17, return_type19, method23, type24, behaviouralComponent26, is_source_of27, references36, super_type29, fields31, sub_types33, type35, table37, columns39, behaviouralComponents41, datatypes43, tables45, schema65, type48, views50, restrictions51, features53, super_type57, attributes59, methods60, typed63, columns67, views68, restrictions71, description74, updateColumns75, subtables84, trigger77, structured78, supertable81, tables86, components88},
    generalizations={gen_SQL2003_evo_ARRAY_CollectionType, gen_SQL2003_evo_Attribute_StructuralComponent, gen_SQL2003_evo_BaseTable_Table, gen_SQL2003_evo_BinaryStringType_PredefinedType, gen_SQL2003_evo_BooleanType_PredefinedType, gen_SQL2003_evo_CharacterStringType_PredefinedType, gen_SQL2003_evo_CollectionType_ConstructedType, gen_SQL2003_evo_Column_StructuralComponent, gen_SQL2003_evo_ColumnConstraint_Restriction, gen_SQL2003_evo_ConstructedType_DataType, gen_SQL2003_evo_DatetimeFeature_Feature, gen_SQL2003_evo_Field_StructuralComponent, gen_SQL2003_evo_DatetimeType_PredefinedType, gen_SQL2003_evo_DerivedTable_Table, gen_SQL2003_evo_DistinctType_UserDefinedType, gen_SQL2003_evo_Function_BehaviouralComponent, gen_SQL2003_evo_IntervalFeature_Feature, gen_SQL2003_evo_IntervalType_PredefinedType, gen_SQL2003_evo_MULTISET_CollectionType, gen_SQL2003_evo_MethodParameter_Parameter, gen_SQL2003_evo_NotNull_ColumnConstraint, gen_SQL2003_evo_NumericFeature_Feature, gen_SQL2003_evo_NumericType_PredefinedType, gen_SQL2003_evo_PrimaryKey_UniqueConstraint, gen_SQL2003_evo_ParameterWithMode_Parameter, gen_SQL2003_evo_PredefinedType_DataType, gen_SQL2003_evo_Procedure_BehaviouralComponent, gen_SQL2003_evo_ROW_ConstructedType, gen_SQL2003_evo_ReferenceType_ConstructedType, gen_SQL2003_evo_ReferentialConstraint_TableConstraint, gen_SQL2003_evo_StringFeature_Feature, gen_SQL2003_evo_StructuredType_UserDefinedType, gen_SQL2003_evo_TableCheckConstraint_TableConstraint, gen_SQL2003_evo_TableConstraint_Restriction, gen_SQL2003_evo_Trigger_Restriction, gen_SQL2003_evo_TypedTable_BaseTable, gen_SQL2003_evo_UniqueConstraint_TableConstraint, gen_SQL2003_evo_UserDefinedType_DataType, gen_SQL2003_evo_View_DerivedTable, gen_SQL2003_evo_XMLType_PredefinedType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)