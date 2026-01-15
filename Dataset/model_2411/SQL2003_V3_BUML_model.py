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

BinaryStringTypes: Enumeration = Enumeration(
    name="BinaryStringTypes",
    literals={
            EnumerationLiteral(name="BINARYLARGEOBJECT"),
			EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="BINARYVARYING")
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

MatchTypes: Enumeration = Enumeration(
    name="MatchTypes",
    literals={
            EnumerationLiteral(name="SIMPLE"),
			EnumerationLiteral(name="PARTIAL"),
			EnumerationLiteral(name="TOTAL")
    }
)

IntervalTypes: Enumeration = Enumeration(
    name="IntervalTypes",
    literals={
            EnumerationLiteral(name="MONTH"),
			EnumerationLiteral(name="DAY"),
			EnumerationLiteral(name="HOUR"),
			EnumerationLiteral(name="MINUTE"),
			EnumerationLiteral(name="SECOND"),
			EnumerationLiteral(name="YEAR_MONTH"),
			EnumerationLiteral(name="DAY_HOUR"),
			EnumerationLiteral(name="DAY_MINUTE"),
			EnumerationLiteral(name="DAY_SECOND"),
			EnumerationLiteral(name="HOUR_MINUTE"),
			EnumerationLiteral(name="HOUR_SECOND"),
			EnumerationLiteral(name="MINUTE_SECOND"),
			EnumerationLiteral(name="YEAR")
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

NumericRadix: Enumeration = Enumeration(
    name="NumericRadix",
    literals={
            EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="BINARY")
    }
)

NumericTypes: Enumeration = Enumeration(
    name="NumericTypes",
    literals={
            EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="SMALLINT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="BIGINT"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="DOUBLEPRECISION"),
			EnumerationLiteral(name="NUMERIC")
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

Unit: Enumeration = Enumeration(
    name="Unit",
    literals={
            EnumerationLiteral(name="CHARACTERS"),
			EnumerationLiteral(name="OCTETS")
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

XMLTypes: Enumeration = Enumeration(
    name="XMLTypes",
    literals={
            EnumerationLiteral(name="XMLTYPE")
    }
)

# Classes
SQL2003_V3_Attribute = Class(name="SQL2003::V3::Attribute")
StructuralComponent = Class(name="StructuralComponent")
SQL2003_V3_StructuredType = Class(name="SQL2003::V3::StructuredType")
SQL2003_V3_BaseTable = Class(name="SQL2003::V3::BaseTable")
Table = Class(name="Table")
SQL2003_V3_BehaviouralComponent = Class(name="SQL2003::V3::BehaviouralComponent", is_abstract=True)
SQL2003_V3_Schema = Class(name="SQL2003::V3::Schema")
SQL2003_V3_ParameterWithMode = Class(name="SQL2003::V3::ParameterWithMode")
SQL2003_V3_ARRAY = Class(name="SQL2003::V3::ARRAY")
CollectionType = Class(name="CollectionType")
SQL2003_V3_BooleanType = Class(name="SQL2003::V3::BooleanType")
SQL2003_V3_CharacterStringType = Class(name="SQL2003::V3::CharacterStringType")
SQL2003_V3_CollectionType = Class(name="SQL2003::V3::CollectionType", is_abstract=True)
ConstructedType = Class(name="ConstructedType")
SQL2003_V3_DataType = Class(name="SQL2003::V3::DataType", is_abstract=True)
SQL2003_V3_BinaryStringType = Class(name="SQL2003::V3::BinaryStringType")
PredefinedType = Class(name="PredefinedType")
SQL2003_V3_ConstructedType = Class(name="SQL2003::V3::ConstructedType", is_abstract=True)
DataType = Class(name="DataType")
SQL2003_V3_DatetimeFeature = Class(name="SQL2003::V3::DatetimeFeature")
Feature = Class(name="Feature")
SQL2003_V3_DatetimeType = Class(name="SQL2003::V3::DatetimeType")
SQL2003_V3_Column = Class(name="SQL2003::V3::Column")
SQL2003_V3_Table = Class(name="SQL2003::V3::Table", is_abstract=True)
SQL2003_V3_ColumnConstraint = Class(name="SQL2003::V3::ColumnConstraint", is_abstract=True)
Restriction = Class(name="Restriction")
SQL2003_V3_PredefinedType = Class(name="SQL2003::V3::PredefinedType", is_abstract=True)
SQL2003_V3_Feature = Class(name="SQL2003::V3::Feature", is_abstract=True)
SQL2003_V3_Domain = Class(name="SQL2003::V3::Domain")
SQL2003_V3_StructuralComponent = Class(name="SQL2003::V3::StructuralComponent", is_abstract=True)
SQL2003_V3_DomainConstraint = Class(name="SQL2003::V3::DomainConstraint")
SQL2003_V3_DerivedTable = Class(name="SQL2003::V3::DerivedTable")
SQL2003_V3_DistinctType = Class(name="SQL2003::V3::DistinctType")
UserDefinedType = Class(name="UserDefinedType")
SQL2003_V3_ROW = Class(name="SQL2003::V3::ROW")
SQL2003_V3_Function = Class(name="SQL2003::V3::Function")
BehaviouralComponent = Class(name="BehaviouralComponent")
SQL2003_V3_IntervalFeature = Class(name="SQL2003::V3::IntervalFeature")
SQL2003_V3_IntervalType = Class(name="SQL2003::V3::IntervalType")
TableConstraint = Class(name="TableConstraint")
SQL2003_V3_Field = Class(name="SQL2003::V3::Field")
SQL2003_V3_MULTISET = Class(name="SQL2003::V3::MULTISET")
SQL2003_V3_Method = Class(name="SQL2003::V3::Method")
SQL2003_V3_NotNull = Class(name="SQL2003::V3::NotNull")
ColumnConstraint = Class(name="ColumnConstraint")
SQL2003_V3_NumericFeature = Class(name="SQL2003::V3::NumericFeature")
SQL2003_V3_MethodParameter = Class(name="SQL2003::V3::MethodParameter")
Parameter_ = Class(name="Parameter")
SQL2003_V3_Parameter = Class(name="SQL2003::V3::Parameter", is_abstract=True)
SQL2003_V3_NumericType = Class(name="SQL2003::V3::NumericType")
SQL2003_V3_Procedure = Class(name="SQL2003::V3::Procedure")
SQL2003_V3_ReferenceType = Class(name="SQL2003::V3::ReferenceType")
SQL2003_V3_PrimaryKey = Class(name="SQL2003::V3::PrimaryKey")
UniqueConstraint = Class(name="UniqueConstraint")
SQL2003_V3_Restriction = Class(name="SQL2003::V3::Restriction", is_abstract=True)
SQL2003_V3_ReferentialConstraint = Class(name="SQL2003::V3::ReferentialConstraint")
SQL2003_V3_UniqueConstraint = Class(name="SQL2003::V3::UniqueConstraint")
SQL2003_V3_View = Class(name="SQL2003::V3::View")
SQL2003_V3_StringFeature = Class(name="SQL2003::V3::StringFeature")
SQL2003_V3_TypedTable = Class(name="SQL2003::V3::TypedTable")
SQL2003_V3_Trigger = Class(name="SQL2003::V3::Trigger")
SQL2003_V3_TriggerDescriptor = Class(name="SQL2003::V3::TriggerDescriptor")
SQL2003_V3_TableCheckConstraint = Class(name="SQL2003::V3::TableCheckConstraint")
SQL2003_V3_TableConstraint = Class(name="SQL2003::V3::TableConstraint", is_abstract=True)
BaseTable = Class(name="BaseTable")
SQL2003_V3_UserDefinedType = Class(name="SQL2003::V3::UserDefinedType", is_abstract=True)
DerivedTable = Class(name="DerivedTable")
SQL2003_V3_XMLType = Class(name="SQL2003::V3::XMLType")

# SQL2003_V3_Attribute class attributes and methods
SQL2003_V3_Attribute_default: Property = Property(name="default", type=StringType)
SQL2003_V3_Attribute.attributes={SQL2003_V3_Attribute_default}

# StructuralComponent class attributes and methods

# SQL2003_V3_StructuredType class attributes and methods
SQL2003_V3_StructuredType_is_final: Property = Property(name="is_final", type=BooleanType)
SQL2003_V3_StructuredType_is_instantiable: Property = Property(name="is_instantiable", type=BooleanType)
SQL2003_V3_StructuredType.attributes={SQL2003_V3_StructuredType_is_instantiable, SQL2003_V3_StructuredType_is_final}

# SQL2003_V3_BaseTable class attributes and methods

# Table class attributes and methods

# SQL2003_V3_BehaviouralComponent class attributes and methods
SQL2003_V3_BehaviouralComponent_name: Property = Property(name="name", type=StringType)
SQL2003_V3_BehaviouralComponent_body: Property = Property(name="body", type=StringType)
SQL2003_V3_BehaviouralComponent.attributes={SQL2003_V3_BehaviouralComponent_name, SQL2003_V3_BehaviouralComponent_body}

# SQL2003_V3_Schema class attributes and methods
SQL2003_V3_Schema_name: Property = Property(name="name", type=StringType)
SQL2003_V3_Schema.attributes={SQL2003_V3_Schema_name}

# SQL2003_V3_ParameterWithMode class attributes and methods
SQL2003_V3_ParameterWithMode_mode: Property = Property(name="mode", type=StringType)
SQL2003_V3_ParameterWithMode.attributes={SQL2003_V3_ParameterWithMode_mode}

# SQL2003_V3_ARRAY class attributes and methods
SQL2003_V3_ARRAY_num_elements: Property = Property(name="num_elements", type=StringType)
SQL2003_V3_ARRAY.attributes={SQL2003_V3_ARRAY_num_elements}

# CollectionType class attributes and methods

# SQL2003_V3_BooleanType class attributes and methods
SQL2003_V3_BooleanType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V3_BooleanType.attributes={SQL2003_V3_BooleanType_descriptor}

# SQL2003_V3_CharacterStringType class attributes and methods
SQL2003_V3_CharacterStringType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V3_CharacterStringType_length_def: Property = Property(name="length_def", type=StringType)
SQL2003_V3_CharacterStringType.attributes={SQL2003_V3_CharacterStringType_length_def, SQL2003_V3_CharacterStringType_descriptor}

# SQL2003_V3_CollectionType class attributes and methods

# ConstructedType class attributes and methods

# SQL2003_V3_DataType class attributes and methods

# SQL2003_V3_BinaryStringType class attributes and methods
SQL2003_V3_BinaryStringType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V3_BinaryStringType_length_def: Property = Property(name="length_def", type=StringType)
SQL2003_V3_BinaryStringType.attributes={SQL2003_V3_BinaryStringType_descriptor, SQL2003_V3_BinaryStringType_length_def}

# PredefinedType class attributes and methods

# SQL2003_V3_ConstructedType class attributes and methods
SQL2003_V3_ConstructedType_name: Property = Property(name="name", type=StringType)
SQL2003_V3_ConstructedType.attributes={SQL2003_V3_ConstructedType_name}

# DataType class attributes and methods

# SQL2003_V3_DatetimeFeature class attributes and methods
SQL2003_V3_DatetimeFeature_key: Property = Property(name="key", type=StringType)
SQL2003_V3_DatetimeFeature_value: Property = Property(name="value", type=StringType)
SQL2003_V3_DatetimeFeature.attributes={SQL2003_V3_DatetimeFeature_value, SQL2003_V3_DatetimeFeature_key}

# Feature class attributes and methods

# SQL2003_V3_DatetimeType class attributes and methods
SQL2003_V3_DatetimeType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V3_DatetimeType.attributes={SQL2003_V3_DatetimeType_descriptor}

# SQL2003_V3_Column class attributes and methods
SQL2003_V3_Column_default: Property = Property(name="default", type=StringType)
SQL2003_V3_Column.attributes={SQL2003_V3_Column_default}

# SQL2003_V3_Table class attributes and methods
SQL2003_V3_Table_name: Property = Property(name="name", type=StringType)
SQL2003_V3_Table.attributes={SQL2003_V3_Table_name}

# SQL2003_V3_ColumnConstraint class attributes and methods

# Restriction class attributes and methods

# SQL2003_V3_PredefinedType class attributes and methods

# SQL2003_V3_Feature class attributes and methods

# SQL2003_V3_Domain class attributes and methods
SQL2003_V3_Domain_name: Property = Property(name="name", type=StringType)
SQL2003_V3_Domain_expression: Property = Property(name="expression", type=StringType)
SQL2003_V3_Domain_default: Property = Property(name="default", type=StringType)
SQL2003_V3_Domain.attributes={SQL2003_V3_Domain_expression, SQL2003_V3_Domain_name, SQL2003_V3_Domain_default}

# SQL2003_V3_StructuralComponent class attributes and methods
SQL2003_V3_StructuralComponent_name: Property = Property(name="name", type=StringType)
SQL2003_V3_StructuralComponent.attributes={SQL2003_V3_StructuralComponent_name}

# SQL2003_V3_DomainConstraint class attributes and methods

# SQL2003_V3_DerivedTable class attributes and methods
SQL2003_V3_DerivedTable_query_expression: Property = Property(name="query_expression", type=StringType)
SQL2003_V3_DerivedTable.attributes={SQL2003_V3_DerivedTable_query_expression}

# SQL2003_V3_DistinctType class attributes and methods

# UserDefinedType class attributes and methods

# SQL2003_V3_ROW class attributes and methods

# SQL2003_V3_Function class attributes and methods

# BehaviouralComponent class attributes and methods

# SQL2003_V3_IntervalFeature class attributes and methods
SQL2003_V3_IntervalFeature_key: Property = Property(name="key", type=StringType)
SQL2003_V3_IntervalFeature_value: Property = Property(name="value", type=StringType)
SQL2003_V3_IntervalFeature.attributes={SQL2003_V3_IntervalFeature_key, SQL2003_V3_IntervalFeature_value}

# SQL2003_V3_IntervalType class attributes and methods
SQL2003_V3_IntervalType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V3_IntervalType.attributes={SQL2003_V3_IntervalType_descriptor}

# TableConstraint class attributes and methods

# SQL2003_V3_Field class attributes and methods

# SQL2003_V3_MULTISET class attributes and methods

# SQL2003_V3_Method class attributes and methods
SQL2003_V3_Method_name: Property = Property(name="name", type=StringType)
SQL2003_V3_Method_body: Property = Property(name="body", type=StringType)
SQL2003_V3_Method.attributes={SQL2003_V3_Method_name, SQL2003_V3_Method_body}

# SQL2003_V3_NotNull class attributes and methods

# ColumnConstraint class attributes and methods

# SQL2003_V3_NumericFeature class attributes and methods
SQL2003_V3_NumericFeature_key: Property = Property(name="key", type=StringType)
SQL2003_V3_NumericFeature_value: Property = Property(name="value", type=StringType)
SQL2003_V3_NumericFeature.attributes={SQL2003_V3_NumericFeature_key, SQL2003_V3_NumericFeature_value}

# SQL2003_V3_MethodParameter class attributes and methods

# Parameter class attributes and methods

# SQL2003_V3_Parameter class attributes and methods
SQL2003_V3_Parameter_name: Property = Property(name="name", type=StringType)
SQL2003_V3_Parameter.attributes={SQL2003_V3_Parameter_name}

# SQL2003_V3_NumericType class attributes and methods
SQL2003_V3_NumericType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V3_NumericType.attributes={SQL2003_V3_NumericType_descriptor}

# SQL2003_V3_Procedure class attributes and methods

# SQL2003_V3_ReferenceType class attributes and methods

# SQL2003_V3_PrimaryKey class attributes and methods

# UniqueConstraint class attributes and methods

# SQL2003_V3_Restriction class attributes and methods

# SQL2003_V3_ReferentialConstraint class attributes and methods
SQL2003_V3_ReferentialConstraint_delete_action: Property = Property(name="delete_action", type=StringType)
SQL2003_V3_ReferentialConstraint_update_action: Property = Property(name="update_action", type=StringType)
SQL2003_V3_ReferentialConstraint_match: Property = Property(name="match", type=StringType)
SQL2003_V3_ReferentialConstraint.attributes={SQL2003_V3_ReferentialConstraint_match, SQL2003_V3_ReferentialConstraint_delete_action, SQL2003_V3_ReferentialConstraint_update_action}

# SQL2003_V3_UniqueConstraint class attributes and methods

# SQL2003_V3_View class attributes and methods

# SQL2003_V3_StringFeature class attributes and methods
SQL2003_V3_StringFeature_key: Property = Property(name="key", type=StringType)
SQL2003_V3_StringFeature_value: Property = Property(name="value", type=StringType)
SQL2003_V3_StringFeature.attributes={SQL2003_V3_StringFeature_key, SQL2003_V3_StringFeature_value}

# SQL2003_V3_TypedTable class attributes and methods

# SQL2003_V3_Trigger class attributes and methods
SQL2003_V3_Trigger_name: Property = Property(name="name", type=StringType)
SQL2003_V3_Trigger.attributes={SQL2003_V3_Trigger_name}

# SQL2003_V3_TriggerDescriptor class attributes and methods
SQL2003_V3_TriggerDescriptor_event: Property = Property(name="event", type=StringType)
SQL2003_V3_TriggerDescriptor_actionTime: Property = Property(name="actionTime", type=StringType)
SQL2003_V3_TriggerDescriptor_triggeredAction: Property = Property(name="triggeredAction", type=StringType)
SQL2003_V3_TriggerDescriptor_level: Property = Property(name="level", type=StringType)
SQL2003_V3_TriggerDescriptor.attributes={SQL2003_V3_TriggerDescriptor_event, SQL2003_V3_TriggerDescriptor_level, SQL2003_V3_TriggerDescriptor_triggeredAction, SQL2003_V3_TriggerDescriptor_actionTime}

# SQL2003_V3_TableCheckConstraint class attributes and methods
SQL2003_V3_TableCheckConstraint_expression: Property = Property(name="expression", type=StringType)
SQL2003_V3_TableCheckConstraint.attributes={SQL2003_V3_TableCheckConstraint_expression}

# SQL2003_V3_TableConstraint class attributes and methods
SQL2003_V3_TableConstraint_name: Property = Property(name="name", type=StringType)
SQL2003_V3_TableConstraint.attributes={SQL2003_V3_TableConstraint_name}

# BaseTable class attributes and methods

# SQL2003_V3_UserDefinedType class attributes and methods
SQL2003_V3_UserDefinedType_name: Property = Property(name="name", type=StringType)
SQL2003_V3_UserDefinedType.attributes={SQL2003_V3_UserDefinedType_name}

# DerivedTable class attributes and methods

# SQL2003_V3_XMLType class attributes and methods
SQL2003_V3_XMLType_descriptor: Property = Property(name="descriptor", type=StringType)
SQL2003_V3_XMLType.attributes={SQL2003_V3_XMLType_descriptor}

# Relationships
structured0: BinaryAssociation = BinaryAssociation(
    name="structured0",
    ends={
        Property(name="StructuredType", type=SQL2003_V3_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=SQL2003_V3_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
schema1: BinaryAssociation = BinaryAssociation(
    name="schema1",
    ends={
        Property(name="Schema", type=SQL2003_V3_BehaviouralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralComponents", type=SQL2003_V3_Schema, multiplicity=Multiplicity(1, 1))
    }
)
parametersWithMode2: BinaryAssociation = BinaryAssociation(
    name="parametersWithMode2",
    ends={
        Property(name="ParameterWithMode", type=SQL2003_V3_BehaviouralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralComponent", type=SQL2003_V3_ParameterWithMode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super_type4: BinaryAssociation = BinaryAssociation(
    name="super_type4",
    ends={
        Property(name="SQL2003_V3_CollectionType", type=SQL2003_V3_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_CollectionType3", type=SQL2003_V3_CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
schema8: BinaryAssociation = BinaryAssociation(
    name="schema8",
    ends={
        Property(name="Schema9", type=SQL2003_V3_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypes", type=SQL2003_V3_Schema, multiplicity=Multiplicity(1, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="SQL2003_V3_DataType", type=SQL2003_V3_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_CollectionType6", type=SQL2003_V3_DataType, multiplicity=Multiplicity(1, 1))
    }
)
table7: BinaryAssociation = BinaryAssociation(
    name="table7",
    ends={
        Property(name="Table", type=SQL2003_V3_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=SQL2003_V3_Table, multiplicity=Multiplicity(1, 1))
    }
)
source_type10: BinaryAssociation = BinaryAssociation(
    name="source_type10",
    ends={
        Property(name="PredefinedType", type=SQL2003_V3_DistinctType, multiplicity=Multiplicity(1, 1)),
        Property(name="is_source_of", type=SQL2003_V3_PredefinedType, multiplicity=Multiplicity(1, 1))
    }
)
features11: BinaryAssociation = BinaryAssociation(
    name="features11",
    ends={
        Property(name="SQL2003_V3_Feature", type=SQL2003_V3_DistinctType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_DistinctType", type=SQL2003_V3_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema12: BinaryAssociation = BinaryAssociation(
    name="schema12",
    ends={
        Property(name="Schema13", type=SQL2003_V3_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="domains", type=SQL2003_V3_Schema, multiplicity=Multiplicity(1, 1))
    }
)
defines14: BinaryAssociation = BinaryAssociation(
    name="defines14",
    ends={
        Property(name="StructuralComponent", type=SQL2003_V3_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="has_domain", type=SQL2003_V3_StructuralComponent, multiplicity=Multiplicity(0, 9999))
    }
)
row17: BinaryAssociation = BinaryAssociation(
    name="row17",
    ends={
        Property(name="ROW", type=SQL2003_V3_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=SQL2003_V3_ROW, multiplicity=Multiplicity(1, 1))
    }
)
return_type18: BinaryAssociation = BinaryAssociation(
    name="return_type18",
    ends={
        Property(name="SQL2003_V3_DataType19", type=SQL2003_V3_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_Function", type=SQL2003_V3_DataType, multiplicity=Multiplicity(1, 1))
    }
)
constraint15: BinaryAssociation = BinaryAssociation(
    name="constraint15",
    ends={
        Property(name="DomainConstraint", type=SQL2003_V3_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="domain", type=SQL2003_V3_DomainConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
domain16: BinaryAssociation = BinaryAssociation(
    name="domain16",
    ends={
        Property(name="Domain", type=SQL2003_V3_DomainConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint", type=SQL2003_V3_Domain, multiplicity=Multiplicity(1, 1))
    }
)
override21: BinaryAssociation = BinaryAssociation(
    name="override21",
    ends={
        Property(name="SQL2003_V3_Method", type=SQL2003_V3_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_Method20", type=SQL2003_V3_Method, multiplicity=Multiplicity(0, 1))
    }
)
method28: BinaryAssociation = BinaryAssociation(
    name="method28",
    ends={
        Property(name="Method", type=SQL2003_V3_MethodParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=SQL2003_V3_Method, multiplicity=Multiplicity(1, 1))
    }
)
structured22: BinaryAssociation = BinaryAssociation(
    name="structured22",
    ends={
        Property(name="StructuredType23", type=SQL2003_V3_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=SQL2003_V3_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
return_type24: BinaryAssociation = BinaryAssociation(
    name="return_type24",
    ends={
        Property(name="SQL2003_V3_DataType26", type=SQL2003_V3_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_Method25", type=SQL2003_V3_DataType, multiplicity=Multiplicity(1, 1))
    }
)
parameters27: BinaryAssociation = BinaryAssociation(
    name="parameters27",
    ends={
        Property(name="MethodParameter", type=SQL2003_V3_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=SQL2003_V3_MethodParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="SQL2003_V3_DataType30", type=SQL2003_V3_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_Parameter", type=SQL2003_V3_DataType, multiplicity=Multiplicity(1, 1))
    }
)
super_type34: BinaryAssociation = BinaryAssociation(
    name="super_type34",
    ends={
        Property(name="ROW35", type=SQL2003_V3_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="sub_types", type=SQL2003_V3_ROW, multiplicity=Multiplicity(0, 1))
    }
)
fields36: BinaryAssociation = BinaryAssociation(
    name="fields36",
    ends={
        Property(name="Field", type=SQL2003_V3_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="row", type=SQL2003_V3_Field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sub_types38: BinaryAssociation = BinaryAssociation(
    name="sub_types38",
    ends={
        Property(name="ROW39", type=SQL2003_V3_ROW, multiplicity=Multiplicity(1, 1)),
        Property(name="super_type", type=SQL2003_V3_ROW, multiplicity=Multiplicity(0, 9999))
    }
)
type40: BinaryAssociation = BinaryAssociation(
    name="type40",
    ends={
        Property(name="SQL2003_V3_StructuredType", type=SQL2003_V3_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_ReferenceType", type=SQL2003_V3_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
behaviouralComponent31: BinaryAssociation = BinaryAssociation(
    name="behaviouralComponent31",
    ends={
        Property(name="BehaviouralComponent", type=SQL2003_V3_ParameterWithMode, multiplicity=Multiplicity(1, 1)),
        Property(name="parametersWithMode", type=SQL2003_V3_BehaviouralComponent, multiplicity=Multiplicity(1, 1))
    }
)
is_source_of32: BinaryAssociation = BinaryAssociation(
    name="is_source_of32",
    ends={
        Property(name="DistinctType", type=SQL2003_V3_PredefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="source_type", type=SQL2003_V3_DistinctType, multiplicity=Multiplicity(0, 9999))
    }
)
references41: BinaryAssociation = BinaryAssociation(
    name="references41",
    ends={
        Property(name="SQL2003_V3_UniqueConstraint", type=SQL2003_V3_ReferentialConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_ReferentialConstraint", type=SQL2003_V3_UniqueConstraint, multiplicity=Multiplicity(1, 1))
    }
)
table42: BinaryAssociation = BinaryAssociation(
    name="table42",
    ends={
        Property(name="Table43", type=SQL2003_V3_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictions", type=SQL2003_V3_Table, multiplicity=Multiplicity(1, 1))
    }
)
columns44: BinaryAssociation = BinaryAssociation(
    name="columns44",
    ends={
        Property(name="StructuralComponent46", type=SQL2003_V3_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictions45", type=SQL2003_V3_StructuralComponent, multiplicity=Multiplicity(1, 9999))
    }
)
behaviouralComponents47: BinaryAssociation = BinaryAssociation(
    name="behaviouralComponents47",
    ends={
        Property(name="BehaviouralComponent48", type=SQL2003_V3_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=SQL2003_V3_BehaviouralComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypes49: BinaryAssociation = BinaryAssociation(
    name="datatypes49",
    ends={
        Property(name="DataType", type=SQL2003_V3_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema50", type=SQL2003_V3_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables51: BinaryAssociation = BinaryAssociation(
    name="tables51",
    ends={
        Property(name="Table53", type=SQL2003_V3_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema52", type=SQL2003_V3_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type57: BinaryAssociation = BinaryAssociation(
    name="type57",
    ends={
        Property(name="SQL2003_V3_DataType58", type=SQL2003_V3_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_StructuralComponent", type=SQL2003_V3_DataType, multiplicity=Multiplicity(1, 1))
    }
)
views59: BinaryAssociation = BinaryAssociation(
    name="views59",
    ends={
        Property(name="View", type=SQL2003_V3_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="components", type=SQL2003_V3_View, multiplicity=Multiplicity(0, 9999))
    }
)
restrictions60: BinaryAssociation = BinaryAssociation(
    name="restrictions60",
    ends={
        Property(name="Restriction", type=SQL2003_V3_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="columns61", type=SQL2003_V3_Restriction, multiplicity=Multiplicity(0, 9999))
    }
)
features62: BinaryAssociation = BinaryAssociation(
    name="features62",
    ends={
        Property(name="SQL2003_V3_Feature64", type=SQL2003_V3_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_StructuralComponent63", type=SQL2003_V3_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
has_domain65: BinaryAssociation = BinaryAssociation(
    name="has_domain65",
    ends={
        Property(name="Domain66", type=SQL2003_V3_StructuralComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="defines", type=SQL2003_V3_Domain, multiplicity=Multiplicity(0, 1))
    }
)
domains54: BinaryAssociation = BinaryAssociation(
    name="domains54",
    ends={
        Property(name="Domain56", type=SQL2003_V3_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema55", type=SQL2003_V3_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods71: BinaryAssociation = BinaryAssociation(
    name="methods71",
    ends={
        Property(name="Method73", type=SQL2003_V3_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured72", type=SQL2003_V3_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typed74: BinaryAssociation = BinaryAssociation(
    name="typed74",
    ends={
        Property(name="TypedTable", type=SQL2003_V3_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured75", type=SQL2003_V3_TypedTable, multiplicity=Multiplicity(0, 9999))
    }
)
schema76: BinaryAssociation = BinaryAssociation(
    name="schema76",
    ends={
        Property(name="Schema77", type=SQL2003_V3_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=SQL2003_V3_Schema, multiplicity=Multiplicity(1, 1))
    }
)
columns78: BinaryAssociation = BinaryAssociation(
    name="columns78",
    ends={
        Property(name="Column", type=SQL2003_V3_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=SQL2003_V3_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views79: BinaryAssociation = BinaryAssociation(
    name="views79",
    ends={
        Property(name="View81", type=SQL2003_V3_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables80", type=SQL2003_V3_View, multiplicity=Multiplicity(0, 9999))
    }
)
super_type68: BinaryAssociation = BinaryAssociation(
    name="super_type68",
    ends={
        Property(name="SQL2003_V3_StructuredType69", type=SQL2003_V3_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_StructuredType67", type=SQL2003_V3_StructuredType, multiplicity=Multiplicity(0, 1))
    }
)
attributes70: BinaryAssociation = BinaryAssociation(
    name="attributes70",
    ends={
        Property(name="Attribute", type=SQL2003_V3_StructuredType, multiplicity=Multiplicity(1, 1)),
        Property(name="structured", type=SQL2003_V3_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description85: BinaryAssociation = BinaryAssociation(
    name="description85",
    ends={
        Property(name="TriggerDescriptor", type=SQL2003_V3_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="trigger", type=SQL2003_V3_TriggerDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateColumns86: BinaryAssociation = BinaryAssociation(
    name="updateColumns86",
    ends={
        Property(name="SQL2003_V3_StructuralComponent87", type=SQL2003_V3_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="SQL2003_V3_Trigger", type=SQL2003_V3_StructuralComponent, multiplicity=Multiplicity(0, 1))
    }
)
restrictions82: BinaryAssociation = BinaryAssociation(
    name="restrictions82",
    ends={
        Property(name="Restriction84", type=SQL2003_V3_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table83", type=SQL2003_V3_Restriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structured89: BinaryAssociation = BinaryAssociation(
    name="structured89",
    ends={
        Property(name="StructuredType90", type=SQL2003_V3_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="typed", type=SQL2003_V3_StructuredType, multiplicity=Multiplicity(1, 1))
    }
)
supertable92: BinaryAssociation = BinaryAssociation(
    name="supertable92",
    ends={
        Property(name="TypedTable93", type=SQL2003_V3_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="subtables", type=SQL2003_V3_TypedTable, multiplicity=Multiplicity(0, 1))
    }
)
subtables95: BinaryAssociation = BinaryAssociation(
    name="subtables95",
    ends={
        Property(name="TypedTable96", type=SQL2003_V3_TypedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="supertable", type=SQL2003_V3_TypedTable, multiplicity=Multiplicity(0, 9999))
    }
)
trigger88: BinaryAssociation = BinaryAssociation(
    name="trigger88",
    ends={
        Property(name="Trigger", type=SQL2003_V3_TriggerDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="description", type=SQL2003_V3_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
tables97: BinaryAssociation = BinaryAssociation(
    name="tables97",
    ends={
        Property(name="Table98", type=SQL2003_V3_View, multiplicity=Multiplicity(1, 1)),
        Property(name="views", type=SQL2003_V3_Table, multiplicity=Multiplicity(1, 9999))
    }
)
components99: BinaryAssociation = BinaryAssociation(
    name="components99",
    ends={
        Property(name="StructuralComponent101", type=SQL2003_V3_View, multiplicity=Multiplicity(1, 1)),
        Property(name="views100", type=SQL2003_V3_StructuralComponent, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_SQL2003_V3_Attribute_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_V3_Attribute)
gen_SQL2003_V3_BaseTable_Table = Generalization(general=Table, specific=SQL2003_V3_BaseTable)
gen_SQL2003_V3_ARRAY_CollectionType = Generalization(general=CollectionType, specific=SQL2003_V3_ARRAY)
gen_SQL2003_V3_BooleanType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V3_BooleanType)
gen_SQL2003_V3_CharacterStringType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V3_CharacterStringType)
gen_SQL2003_V3_CollectionType_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_V3_CollectionType)
gen_SQL2003_V3_BinaryStringType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V3_BinaryStringType)
gen_SQL2003_V3_ConstructedType_DataType = Generalization(general=DataType, specific=SQL2003_V3_ConstructedType)
gen_SQL2003_V3_DatetimeFeature_Feature = Generalization(general=Feature, specific=SQL2003_V3_DatetimeFeature)
gen_SQL2003_V3_DatetimeType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V3_DatetimeType)
gen_SQL2003_V3_Column_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_V3_Column)
gen_SQL2003_V3_ColumnConstraint_Restriction = Generalization(general=Restriction, specific=SQL2003_V3_ColumnConstraint)
gen_SQL2003_V3_DerivedTable_Table = Generalization(general=Table, specific=SQL2003_V3_DerivedTable)
gen_SQL2003_V3_DistinctType_UserDefinedType = Generalization(general=UserDefinedType, specific=SQL2003_V3_DistinctType)
gen_SQL2003_V3_Function_BehaviouralComponent = Generalization(general=BehaviouralComponent, specific=SQL2003_V3_Function)
gen_SQL2003_V3_IntervalFeature_Feature = Generalization(general=Feature, specific=SQL2003_V3_IntervalFeature)
gen_SQL2003_V3_IntervalType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V3_IntervalType)
gen_SQL2003_V3_DomainConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_V3_DomainConstraint)
gen_SQL2003_V3_Field_StructuralComponent = Generalization(general=StructuralComponent, specific=SQL2003_V3_Field)
gen_SQL2003_V3_MULTISET_CollectionType = Generalization(general=CollectionType, specific=SQL2003_V3_MULTISET)
gen_SQL2003_V3_NotNull_ColumnConstraint = Generalization(general=ColumnConstraint, specific=SQL2003_V3_NotNull)
gen_SQL2003_V3_NumericFeature_Feature = Generalization(general=Feature, specific=SQL2003_V3_NumericFeature)
gen_SQL2003_V3_MethodParameter_Parameter = Generalization(general=Parameter_, specific=SQL2003_V3_MethodParameter)
gen_SQL2003_V3_ParameterWithMode_Parameter = Generalization(general=Parameter_, specific=SQL2003_V3_ParameterWithMode)
gen_SQL2003_V3_NumericType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V3_NumericType)
gen_SQL2003_V3_Procedure_BehaviouralComponent = Generalization(general=BehaviouralComponent, specific=SQL2003_V3_Procedure)
gen_SQL2003_V3_ROW_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_V3_ROW)
gen_SQL2003_V3_ReferenceType_ConstructedType = Generalization(general=ConstructedType, specific=SQL2003_V3_ReferenceType)
gen_SQL2003_V3_PredefinedType_DataType = Generalization(general=DataType, specific=SQL2003_V3_PredefinedType)
gen_SQL2003_V3_PrimaryKey_UniqueConstraint = Generalization(general=UniqueConstraint, specific=SQL2003_V3_PrimaryKey)
gen_SQL2003_V3_ReferentialConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_V3_ReferentialConstraint)
gen_SQL2003_V3_StringFeature_Feature = Generalization(general=Feature, specific=SQL2003_V3_StringFeature)
gen_SQL2003_V3_StructuredType_UserDefinedType = Generalization(general=UserDefinedType, specific=SQL2003_V3_StructuredType)
gen_SQL2003_V3_Trigger_Restriction = Generalization(general=Restriction, specific=SQL2003_V3_Trigger)
gen_SQL2003_V3_TableCheckConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_V3_TableCheckConstraint)
gen_SQL2003_V3_TableConstraint_Restriction = Generalization(general=Restriction, specific=SQL2003_V3_TableConstraint)
gen_SQL2003_V3_TypedTable_BaseTable = Generalization(general=BaseTable, specific=SQL2003_V3_TypedTable)
gen_SQL2003_V3_UniqueConstraint_TableConstraint = Generalization(general=TableConstraint, specific=SQL2003_V3_UniqueConstraint)
gen_SQL2003_V3_UserDefinedType_DataType = Generalization(general=DataType, specific=SQL2003_V3_UserDefinedType)
gen_SQL2003_V3_View_DerivedTable = Generalization(general=DerivedTable, specific=SQL2003_V3_View)
gen_SQL2003_V3_XMLType_PredefinedType = Generalization(general=PredefinedType, specific=SQL2003_V3_XMLType)

# Domain Model
domain_model = DomainModel(
    name="SQL2003_V3",
    types={SQL2003_V3_Attribute, StructuralComponent, SQL2003_V3_StructuredType, SQL2003_V3_BaseTable, Table, SQL2003_V3_BehaviouralComponent, SQL2003_V3_Schema, SQL2003_V3_ParameterWithMode, SQL2003_V3_ARRAY, CollectionType, SQL2003_V3_BooleanType, SQL2003_V3_CharacterStringType, SQL2003_V3_CollectionType, ConstructedType, SQL2003_V3_DataType, SQL2003_V3_BinaryStringType, PredefinedType, SQL2003_V3_ConstructedType, DataType, SQL2003_V3_DatetimeFeature, Feature, SQL2003_V3_DatetimeType, SQL2003_V3_Column, SQL2003_V3_Table, SQL2003_V3_ColumnConstraint, Restriction, SQL2003_V3_PredefinedType, SQL2003_V3_Feature, SQL2003_V3_Domain, SQL2003_V3_StructuralComponent, SQL2003_V3_DomainConstraint, SQL2003_V3_DerivedTable, SQL2003_V3_DistinctType, UserDefinedType, SQL2003_V3_ROW, SQL2003_V3_Function, BehaviouralComponent, SQL2003_V3_IntervalFeature, SQL2003_V3_IntervalType, TableConstraint, SQL2003_V3_Field, SQL2003_V3_MULTISET, SQL2003_V3_Method, SQL2003_V3_NotNull, ColumnConstraint, SQL2003_V3_NumericFeature, SQL2003_V3_MethodParameter, Parameter_, SQL2003_V3_Parameter, SQL2003_V3_NumericType, SQL2003_V3_Procedure, SQL2003_V3_ReferenceType, SQL2003_V3_PrimaryKey, UniqueConstraint, SQL2003_V3_Restriction, SQL2003_V3_ReferentialConstraint, SQL2003_V3_UniqueConstraint, SQL2003_V3_View, SQL2003_V3_StringFeature, SQL2003_V3_TypedTable, SQL2003_V3_Trigger, SQL2003_V3_TriggerDescriptor, SQL2003_V3_TableCheckConstraint, SQL2003_V3_TableConstraint, BaseTable, SQL2003_V3_UserDefinedType, DerivedTable, SQL2003_V3_XMLType, BooleanTypes, CharacterStringTypes, BinaryStringTypes, DatetimeFeatures, DatetimeTypes, IntervalFeatures, MatchTypes, IntervalTypes, Multiplier, NumericFeatures, ParameterMode, NumericRadix, NumericTypes, ReferentialAction, StringFeatures, TriggerActionTime, Unit, TriggerEvent, TriggerLevel, XMLTypes},
    associations={structured0, schema1, parametersWithMode2, super_type4, schema8, type5, table7, source_type10, features11, schema12, defines14, row17, return_type18, constraint15, domain16, override21, method28, structured22, return_type24, parameters27, type29, super_type34, fields36, sub_types38, type40, behaviouralComponent31, is_source_of32, references41, table42, columns44, behaviouralComponents47, datatypes49, tables51, type57, views59, restrictions60, features62, has_domain65, domains54, methods71, typed74, schema76, columns78, views79, super_type68, attributes70, description85, updateColumns86, restrictions82, structured89, supertable92, subtables95, trigger88, tables97, components99},
    generalizations={gen_SQL2003_V3_Attribute_StructuralComponent, gen_SQL2003_V3_BaseTable_Table, gen_SQL2003_V3_ARRAY_CollectionType, gen_SQL2003_V3_BooleanType_PredefinedType, gen_SQL2003_V3_CharacterStringType_PredefinedType, gen_SQL2003_V3_CollectionType_ConstructedType, gen_SQL2003_V3_BinaryStringType_PredefinedType, gen_SQL2003_V3_ConstructedType_DataType, gen_SQL2003_V3_DatetimeFeature_Feature, gen_SQL2003_V3_DatetimeType_PredefinedType, gen_SQL2003_V3_Column_StructuralComponent, gen_SQL2003_V3_ColumnConstraint_Restriction, gen_SQL2003_V3_DerivedTable_Table, gen_SQL2003_V3_DistinctType_UserDefinedType, gen_SQL2003_V3_Function_BehaviouralComponent, gen_SQL2003_V3_IntervalFeature_Feature, gen_SQL2003_V3_IntervalType_PredefinedType, gen_SQL2003_V3_DomainConstraint_TableConstraint, gen_SQL2003_V3_Field_StructuralComponent, gen_SQL2003_V3_MULTISET_CollectionType, gen_SQL2003_V3_NotNull_ColumnConstraint, gen_SQL2003_V3_NumericFeature_Feature, gen_SQL2003_V3_MethodParameter_Parameter, gen_SQL2003_V3_ParameterWithMode_Parameter, gen_SQL2003_V3_NumericType_PredefinedType, gen_SQL2003_V3_Procedure_BehaviouralComponent, gen_SQL2003_V3_ROW_ConstructedType, gen_SQL2003_V3_ReferenceType_ConstructedType, gen_SQL2003_V3_PredefinedType_DataType, gen_SQL2003_V3_PrimaryKey_UniqueConstraint, gen_SQL2003_V3_ReferentialConstraint_TableConstraint, gen_SQL2003_V3_StringFeature_Feature, gen_SQL2003_V3_StructuredType_UserDefinedType, gen_SQL2003_V3_Trigger_Restriction, gen_SQL2003_V3_TableCheckConstraint_TableConstraint, gen_SQL2003_V3_TableConstraint_Restriction, gen_SQL2003_V3_TypedTable_BaseTable, gen_SQL2003_V3_UniqueConstraint_TableConstraint, gen_SQL2003_V3_UserDefinedType_DataType, gen_SQL2003_V3_View_DerivedTable, gen_SQL2003_V3_XMLType_PredefinedType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)