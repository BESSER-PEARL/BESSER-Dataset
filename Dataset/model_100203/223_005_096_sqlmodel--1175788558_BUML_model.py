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
GenerateType: Enumeration = Enumeration(
    name="GenerateType",
    literals={
            EnumerationLiteral(name="DEFAULT_GENERATED"),
			EnumerationLiteral(name="ALWAYS_GENERATED")
    }
)

ReferentialActionType: Enumeration = Enumeration(
    name="ReferentialActionType",
    literals={
            EnumerationLiteral(name="NO_ACTION"),
			EnumerationLiteral(name="RESTRICT"),
			EnumerationLiteral(name="CASCADE"),
			EnumerationLiteral(name="SET_NULL"),
			EnumerationLiteral(name="SET_DEFAULT")
    }
)

MatchType: Enumeration = Enumeration(
    name="MatchType",
    literals={
            EnumerationLiteral(name="MATCH_SIMPLE"),
			EnumerationLiteral(name="MATCH_FULL"),
			EnumerationLiteral(name="MATCH_PARTIAL")
    }
)

IncrementType: Enumeration = Enumeration(
    name="IncrementType",
    literals={
            EnumerationLiteral(name="ASC"),
			EnumerationLiteral(name="DESC"),
			EnumerationLiteral(name="RANDOM")
    }
)

CoercibilityType: Enumeration = Enumeration(
    name="CoercibilityType",
    literals={
            EnumerationLiteral(name="IMPLICIT"),
			EnumerationLiteral(name="EXPLICIT"),
			EnumerationLiteral(name="COERCIBILE"),
			EnumerationLiteral(name="NO_COLLATION")
    }
)

IntervalQualifierType: Enumeration = Enumeration(
    name="IntervalQualifierType",
    literals={
            EnumerationLiteral(name="DAY"),
			EnumerationLiteral(name="HOUR"),
			EnumerationLiteral(name="MINUTE"),
			EnumerationLiteral(name="SECOND"),
			EnumerationLiteral(name="FRACTION"),
			EnumerationLiteral(name="YEAR"),
			EnumerationLiteral(name="MONTH")
    }
)

OrderingType: Enumeration = Enumeration(
    name="OrderingType",
    literals={
            EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="FULL")
    }
)

OrderingCategoryType: Enumeration = Enumeration(
    name="OrderingCategoryType",
    literals={
            EnumerationLiteral(name="RELATIVE"),
			EnumerationLiteral(name="MAP"),
			EnumerationLiteral(name="STATE")
    }
)

PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
    literals={
            EnumerationLiteral(name="CHARACTER"),
			EnumerationLiteral(name="BINARY_LARGE_OBJECT"),
			EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="SMALLINT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="BIGINT"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="DOUBLE_PRECISION"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="TIMESTAMP"),
			EnumerationLiteral(name="INTERVAL"),
			EnumerationLiteral(name="DATALINK"),
			EnumerationLiteral(name="XML_TYPE"),
			EnumerationLiteral(name="CHARACTER_VARYING"),
			EnumerationLiteral(name="CHARACTER_LARGE_OBJECT"),
			EnumerationLiteral(name="NATIONAL_CHARACTER"),
			EnumerationLiteral(name="NATIONAL_CHARACTER_VARYING"),
			EnumerationLiteral(name="NATIONAL_CHARACTER_LARGE_OBJECT"),
			EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="BINARY_VARYING")
    }
)

WritePermissionOption: Enumeration = Enumeration(
    name="WritePermissionOption",
    literals={
            EnumerationLiteral(name="FS"),
			EnumerationLiteral(name="ADMIN"),
			EnumerationLiteral(name="BLOCKED")
    }
)

UnlinkOption: Enumeration = Enumeration(
    name="UnlinkOption",
    literals={
            EnumerationLiteral(name="RESTORE"),
			EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="NONE")
    }
)

LinkControlOption: Enumeration = Enumeration(
    name="LinkControlOption",
    literals={
            EnumerationLiteral(name="FILE_LINK_CONTROL"),
			EnumerationLiteral(name="NO_FILE_LINK_CONTROL")
    }
)

IntegrityControlOption: Enumeration = Enumeration(
    name="IntegrityControlOption",
    literals={
            EnumerationLiteral(name="ALL"),
			EnumerationLiteral(name="SELECTIVE"),
			EnumerationLiteral(name="NONE")
    }
)

ReadPermissionOption: Enumeration = Enumeration(
    name="ReadPermissionOption",
    literals={
            EnumerationLiteral(name="DB"),
			EnumerationLiteral(name="FS")
    }
)

DataAccess: Enumeration = Enumeration(
    name="DataAccess",
    literals={
            EnumerationLiteral(name="NO_SQL"),
			EnumerationLiteral(name="CONTAINS_SQL"),
			EnumerationLiteral(name="READS_SQL_DATA"),
			EnumerationLiteral(name="MODIFIES_SQL_DATA")
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

CheckType: Enumeration = Enumeration(
    name="CheckType",
    literals={
            EnumerationLiteral(name="CASCADED"),
			EnumerationLiteral(name="LOCAL"),
			EnumerationLiteral(name="NONE")
    }
)

ReferenceType: Enumeration = Enumeration(
    name="ReferenceType",
    literals={
            EnumerationLiteral(name="SYSTEM_GENERATED"),
			EnumerationLiteral(name="USER_GENERATED"),
			EnumerationLiteral(name="DERIVED_SELF_REF")
    }
)

ActionGranularityType: Enumeration = Enumeration(
    name="ActionGranularityType",
    literals={
            EnumerationLiteral(name="STATEMENT"),
			EnumerationLiteral(name="ROW")
    }
)

ActionTimeType: Enumeration = Enumeration(
    name="ActionTimeType",
    literals={
            EnumerationLiteral(name="AFTER"),
			EnumerationLiteral(name="BEFORE"),
			EnumerationLiteral(name="INSTEADOF")
    }
)

# Classes
sqlmodel_schema_IdentitySpecifier = Class(name="sqlmodel_schema_IdentitySpecifier")
SQLObject = Class(name="SQLObject")
SQLDataType = Class(name="SQLDataType")
UserDefinedType = Class(name="UserDefinedType")
sqlmodel_schema_TypedElement = Class(name="sqlmodel_schema_TypedElement", is_abstract=True)
Index = Class(name="Index")
Table = Class(name="Table")
Sequence = Class(name="Sequence")
Database = Class(name="Database")
sqlmodel_schema_Dependency = Class(name="sqlmodel_schema_Dependency")
schema_sqlmodel_EObject = Class(name="schema_sqlmodel_EObject")
sqlmodel_schema_Schema = Class(name="sqlmodel_schema_Schema")
Trigger = Class(name="Trigger")
Routine = Class(name="Routine")
AuthorizationIdentifier = Class(name="AuthorizationIdentifier")
sqlmodel_schema_SQLObject = Class(name="sqlmodel_schema_SQLObject", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
Catalog = Class(name="Catalog")
Assertion = Class(name="Assertion")
CharacterSet = Class(name="CharacterSet")
Dependency = Class(name="Dependency")
Comment = Class(name="Comment")
ObjectExtension = Class(name="ObjectExtension")
Schema = Class(name="Schema")
sqlmodel_schema_Database = Class(name="sqlmodel_schema_Database")
Privilege = Class(name="Privilege")
sqlmodel_schema_Sequence = Class(name="sqlmodel_schema_Sequence")
TypedElement = Class(name="TypedElement")
IdentitySpecifier = Class(name="IdentitySpecifier")
Event = Class(name="Event")
sqlmodel_schema_Event = Class(name="sqlmodel_schema_Event")
sqlmodel_schema_Catalog = Class(name="sqlmodel_schema_Catalog")
sqlmodel_schema_ObjectExtension = Class(name="sqlmodel_schema_ObjectExtension", is_abstract=True)
sqlmodel_schema_Comment = Class(name="sqlmodel_schema_Comment")
BaseTable = Class(name="BaseTable")
sqlmodel_constraints_Constraint = Class(name="sqlmodel_constraints_Constraint", is_abstract=True)
sqlmodel_constraints_Assertion = Class(name="sqlmodel_constraints_Assertion")
Constraint = Class(name="Constraint")
SearchCondition = Class(name="SearchCondition")
sqlmodel_constraints_ReferenceConstraint = Class(name="sqlmodel_constraints_ReferenceConstraint", is_abstract=True)
TableConstraint = Class(name="TableConstraint")
Column = Class(name="Column")
sqlmodel_constraints_CheckConstraint = Class(name="sqlmodel_constraints_CheckConstraint")
sqlmodel_constraints_TableConstraint = Class(name="sqlmodel_constraints_TableConstraint", is_abstract=True)
sqlmodel_constraints_ForeignKey = Class(name="sqlmodel_constraints_ForeignKey")
ReferenceConstraint = Class(name="ReferenceConstraint")
UniqueConstraint = Class(name="UniqueConstraint")
sqlmodel_constraints_UniqueConstraint = Class(name="sqlmodel_constraints_UniqueConstraint")
sqlmodel_constraints_PrimaryKey = Class(name="sqlmodel_constraints_PrimaryKey")
sqlmodel_constraints_Index = Class(name="sqlmodel_constraints_Index")
ForeignKey = Class(name="ForeignKey")
IndexMember = Class(name="IndexMember")
sqlmodel_constraints_IndexMember = Class(name="sqlmodel_constraints_IndexMember")
sqlmodel_constraints_IndexExpression = Class(name="sqlmodel_constraints_IndexExpression")
sqlmodel_datatypes_UserDefinedType = Class(name="sqlmodel_datatypes_UserDefinedType", is_abstract=True)
DataType = Class(name="DataType")
UserDefinedTypeOrdering = Class(name="UserDefinedTypeOrdering")
IndexExpression = Class(name="IndexExpression")
sqlmodel_datatypes_PredefinedDataType = Class(name="sqlmodel_datatypes_PredefinedDataType", is_abstract=True)
sqlmodel_datatypes_CollectionDataType = Class(name="sqlmodel_datatypes_CollectionDataType", is_abstract=True)
ConstructedDataType = Class(name="ConstructedDataType")
ElementType = Class(name="ElementType")
sqlmodel_datatypes_NumericalDataType = Class(name="sqlmodel_datatypes_NumericalDataType", is_abstract=True)
PredefinedDataType = Class(name="PredefinedDataType")
sqlmodel_datatypes_DataType = Class(name="sqlmodel_datatypes_DataType", is_abstract=True)
sqlmodel_datatypes_RowDataType = Class(name="sqlmodel_datatypes_RowDataType")
Field = Class(name="Field")
sqlmodel_datatypes_CharacterStringDataType = Class(name="sqlmodel_datatypes_CharacterStringDataType")
sqlmodel_datatypes_ArrayDataType = Class(name="sqlmodel_datatypes_ArrayDataType", is_abstract=True)
CollectionDataType = Class(name="CollectionDataType")
sqlmodel_datatypes_MultisetDataType = Class(name="sqlmodel_datatypes_MultisetDataType", is_abstract=True)
sqlmodel_datatypes_IntervalDataType = Class(name="sqlmodel_datatypes_IntervalDataType")
sqlmodel_datatypes_BooleanDataType = Class(name="sqlmodel_datatypes_BooleanDataType")
sqlmodel_datatypes_BinaryStringDataType = Class(name="sqlmodel_datatypes_BinaryStringDataType")
sqlmodel_datatypes_CharacterSet = Class(name="sqlmodel_datatypes_CharacterSet")
CharacterStringDataType = Class(name="CharacterStringDataType")
sqlmodel_datatypes_TimeDataType = Class(name="sqlmodel_datatypes_TimeDataType")
sqlmodel_datatypes_DistinctUserDefinedType = Class(name="sqlmodel_datatypes_DistinctUserDefinedType")
sqlmodel_datatypes_StructuredUserDefinedType = Class(name="sqlmodel_datatypes_StructuredUserDefinedType")
AttributeDefinition = Class(name="AttributeDefinition")
Method_ = Class(name="Method")
StructuredUserDefinedType = Class(name="StructuredUserDefinedType")
sqlmodel_datatypes_FixedPrecisionDataType = Class(name="sqlmodel_datatypes_FixedPrecisionDataType")
ExactNumericDataType = Class(name="ExactNumericDataType")
sqlmodel_datatypes_AttributeDefinition = Class(name="sqlmodel_datatypes_AttributeDefinition")
sqlmodel_datatypes_Domain = Class(name="sqlmodel_datatypes_Domain")
sqlmodel_datatypes_Field = Class(name="sqlmodel_datatypes_Field")
sqlmodel_datatypes_ReferenceDataType = Class(name="sqlmodel_datatypes_ReferenceDataType", is_abstract=True)
DistinctUserDefinedType = Class(name="DistinctUserDefinedType")
CheckConstraint = Class(name="CheckConstraint")
sqlmodel_datatypes_DataLinkDataType = Class(name="sqlmodel_datatypes_DataLinkDataType")
sqlmodel_datatypes_ConstructedDataType = Class(name="sqlmodel_datatypes_ConstructedDataType", is_abstract=True)
sqlmodel_datatypes_SQLDataType = Class(name="sqlmodel_datatypes_SQLDataType", is_abstract=True)
sqlmodel_datatypes_UserDefinedTypeOrdering = Class(name="sqlmodel_datatypes_UserDefinedTypeOrdering")
sqlmodel_datatypes_ExactNumericDataType = Class(name="sqlmodel_datatypes_ExactNumericDataType", is_abstract=True)
NumericalDataType = Class(name="NumericalDataType")
sqlmodel_datatypes_ApproximateNumericDataType = Class(name="sqlmodel_datatypes_ApproximateNumericDataType")
sqlmodel_datatypes_IntegerDataType = Class(name="sqlmodel_datatypes_IntegerDataType")
sqlmodel_datatypes_XMLDataType = Class(name="sqlmodel_datatypes_XMLDataType")
sqlmodel_datatypes_ElementType = Class(name="sqlmodel_datatypes_ElementType")
sqlmodel_datatypes_DateDataType = Class(name="sqlmodel_datatypes_DateDataType")
sqlmodel_expressions_ValueExpression = Class(name="sqlmodel_expressions_ValueExpression", is_abstract=True)
sqlmodel_expressions_SearchCondition = Class(name="sqlmodel_expressions_SearchCondition", is_abstract=True)
sqlmodel_expressions_QueryExpressionDefault = Class(name="sqlmodel_expressions_QueryExpressionDefault")
schema_SQLObject = Class(name="schema_SQLObject")
expressions_QueryExpression = Class(name="expressions_QueryExpression")
sqlmodel_expressions_QueryExpression = Class(name="sqlmodel_expressions_QueryExpression", is_abstract=True)
sqlmodel_expressions_ValueExpressionDefault = Class(name="sqlmodel_expressions_ValueExpressionDefault")
expressions_ValueExpression = Class(name="expressions_ValueExpression")
sqlmodel_routines_Routine = Class(name="sqlmodel_routines_Routine", is_abstract=True)
sqlmodel_expressions_SearchConditionDefault = Class(name="sqlmodel_expressions_SearchConditionDefault")
expressions_SearchCondition = Class(name="expressions_SearchCondition")
Parameter_ = Class(name="Parameter")
Source = Class(name="Source")
sqlmodel_routines_Source = Class(name="sqlmodel_routines_Source")
sqlmodel_routines_Procedure = Class(name="sqlmodel_routines_Procedure")
sqlmodel_routines_Parameter = Class(name="sqlmodel_routines_Parameter")
sqlmodel_routines_Function = Class(name="sqlmodel_routines_Function")
RoutineResultTable = Class(name="RoutineResultTable")
sqlmodel_routines_RoutineResultTable = Class(name="sqlmodel_routines_RoutineResultTable")
sqlmodel_routines_Method = Class(name="sqlmodel_routines_Method")
Function = Class(name="Function")
sqlmodel_routines_BuiltInFunction = Class(name="sqlmodel_routines_BuiltInFunction")
sqlmodel_statements_SQLStatement = Class(name="sqlmodel_statements_SQLStatement", is_abstract=True)
sqlmodel_statements_SQLDataStatement = Class(name="sqlmodel_statements_SQLDataStatement", is_abstract=True)
SQLStatement = Class(name="SQLStatement")
sqlmodel_statements_SQLSchemaStatement = Class(name="sqlmodel_statements_SQLSchemaStatement", is_abstract=True)
sqlmodel_routines_UserDefinedFunction = Class(name="sqlmodel_routines_UserDefinedFunction")
sqlmodel_statements_SQLDataChangeStatement = Class(name="sqlmodel_statements_SQLDataChangeStatement", is_abstract=True)
SQLDataStatement = Class(name="SQLDataStatement")
sqlmodel_statements_SQLStatementDefault = Class(name="sqlmodel_statements_SQLStatementDefault")
statements_SQLStatement = Class(name="statements_SQLStatement")
sqlmodel_statements_SQLConnectionStatement = Class(name="sqlmodel_statements_SQLConnectionStatement", is_abstract=True)
sqlmodel_statements_SQLDiagnosticsStatement = Class(name="sqlmodel_statements_SQLDiagnosticsStatement", is_abstract=True)
sqlmodel_statements_SQLDynamicStatement = Class(name="sqlmodel_statements_SQLDynamicStatement", is_abstract=True)
sqlmodel_statements_SQLControlStatement = Class(name="sqlmodel_statements_SQLControlStatement", is_abstract=True)
sqlmodel_tables_ViewTable = Class(name="sqlmodel_tables_ViewTable")
DerivedTable = Class(name="DerivedTable")
sqlmodel_tables_TemporaryTable = Class(name="sqlmodel_tables_TemporaryTable")
sqlmodel_tables_Table = Class(name="sqlmodel_tables_Table", is_abstract=True)
sqlmodel_statements_SQLSessionStatement = Class(name="sqlmodel_statements_SQLSessionStatement", is_abstract=True)
sqlmodel_statements_SQLTransactionStatement = Class(name="sqlmodel_statements_SQLTransactionStatement", is_abstract=True)
sqlmodel_tables_DerivedTable = Class(name="sqlmodel_tables_DerivedTable", is_abstract=True)
QueryExpression = Class(name="QueryExpression")
sqlmodel_tables_BaseTable = Class(name="sqlmodel_tables_BaseTable", is_abstract=True)
sqlmodel_tables_PersistentTable = Class(name="sqlmodel_tables_PersistentTable")
sqlmodel_tables_Column = Class(name="sqlmodel_tables_Column")
ValueExpression = Class(name="ValueExpression")
sqlmodel_tables_Trigger = Class(name="sqlmodel_tables_Trigger")
sqlmodel_accesscontrol_AuthorizationIdentifier = Class(name="sqlmodel_accesscontrol_AuthorizationIdentifier", is_abstract=True)
sqlmodel_accesscontrol_Privilege = Class(name="sqlmodel_accesscontrol_Privilege")
RoleAuthorization = Class(name="RoleAuthorization")
sqlmodel_accesscontrol_Group = Class(name="sqlmodel_accesscontrol_Group")
sqlmodel_accesscontrol_RoleAuthorization = Class(name="sqlmodel_accesscontrol_RoleAuthorization")
Role = Class(name="Role")
User = Class(name="User")
sqlmodel_accesscontrol_User = Class(name="sqlmodel_accesscontrol_User")
Group = Class(name="Group")
sqlmodel_accesscontrol_Role = Class(name="sqlmodel_accesscontrol_Role")

# sqlmodel_schema_IdentitySpecifier class attributes and methods
sqlmodel_schema_IdentitySpecifier_generationType: Property = Property(name="generationType", type=StringType)
sqlmodel_schema_IdentitySpecifier_startValue: Property = Property(name="startValue", type=StringType)
sqlmodel_schema_IdentitySpecifier_increment: Property = Property(name="increment", type=StringType)
sqlmodel_schema_IdentitySpecifier_minimum: Property = Property(name="minimum", type=StringType)
sqlmodel_schema_IdentitySpecifier_maximum: Property = Property(name="maximum", type=StringType)
sqlmodel_schema_IdentitySpecifier_cycleOption: Property = Property(name="cycleOption", type=BooleanType)
sqlmodel_schema_IdentitySpecifier.attributes={sqlmodel_schema_IdentitySpecifier_minimum, sqlmodel_schema_IdentitySpecifier_increment, sqlmodel_schema_IdentitySpecifier_cycleOption, sqlmodel_schema_IdentitySpecifier_startValue, sqlmodel_schema_IdentitySpecifier_generationType, sqlmodel_schema_IdentitySpecifier_maximum}

# SQLObject class attributes and methods

# SQLDataType class attributes and methods

# UserDefinedType class attributes and methods

# sqlmodel_schema_TypedElement class attributes and methods
sqlmodel_schema_TypedElement_m_setDataType: Method = Method(name="setDataType", parameters={Parameter(name='sqlmodel_newType', type=StringType)})
sqlmodel_schema_TypedElement_m_getDataType: Method = Method(name="getDataType", parameters={}, type=StringType)
sqlmodel_schema_TypedElement.methods={sqlmodel_schema_TypedElement_m_getDataType, sqlmodel_schema_TypedElement_m_setDataType}

# Index class attributes and methods

# Table class attributes and methods

# Sequence class attributes and methods

# Database class attributes and methods

# sqlmodel_schema_Dependency class attributes and methods
sqlmodel_schema_Dependency_dependencyType: Property = Property(name="dependencyType", type=StringType)
sqlmodel_schema_Dependency.attributes={sqlmodel_schema_Dependency_dependencyType}

# schema_sqlmodel_EObject class attributes and methods

# sqlmodel_schema_Schema class attributes and methods

# Trigger class attributes and methods

# Routine class attributes and methods

# AuthorizationIdentifier class attributes and methods

# sqlmodel_schema_SQLObject class attributes and methods
sqlmodel_schema_SQLObject_description: Property = Property(name="description", type=StringType)
sqlmodel_schema_SQLObject_label: Property = Property(name="label", type=StringType)
sqlmodel_schema_SQLObject_m_addEAnnotation: Method = Method(name="addEAnnotation", parameters={Parameter(name='sqlmodel_source', type=StringType)}, type=StringType)
sqlmodel_schema_SQLObject_m_addEAnnotationDetail: Method = Method(name="addEAnnotationDetail", parameters={Parameter(name='sqlmodel_key', type=StringType), Parameter(name='sqlmodel_value', type=StringType), Parameter(name='sqlmodel_eAnnotation', type=StringType)})
sqlmodel_schema_SQLObject_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='sqlmodel_source', type=StringType)}, type=StringType)
sqlmodel_schema_SQLObject_m_getEAnnotationDetail: Method = Method(name="getEAnnotationDetail", parameters={Parameter(name='sqlmodel_key', type=StringType), Parameter(name='sqlmodel_eAnnotation', type=StringType)}, type=StringType)
sqlmodel_schema_SQLObject_m_setAnnotationDetail: Method = Method(name="setAnnotationDetail", parameters={Parameter(name='sqlmodel_value', type=StringType), Parameter(name='sqlmodel_eAnnotation', type=StringType), Parameter(name='sqlmodel_key', type=StringType)})
sqlmodel_schema_SQLObject_m_removeEAnnotationDetail: Method = Method(name="removeEAnnotationDetail", parameters={Parameter(name='sqlmodel_eAnnotation', type=StringType), Parameter(name='sqlmodel_key', type=StringType)})
sqlmodel_schema_SQLObject.attributes={sqlmodel_schema_SQLObject_description, sqlmodel_schema_SQLObject_label}
sqlmodel_schema_SQLObject.methods={sqlmodel_schema_SQLObject_m_setAnnotationDetail, sqlmodel_schema_SQLObject_m_getEAnnotationDetail, sqlmodel_schema_SQLObject_m_addEAnnotation, sqlmodel_schema_SQLObject_m_addEAnnotationDetail, sqlmodel_schema_SQLObject_m_removeEAnnotationDetail, sqlmodel_schema_SQLObject_m_getEAnnotation}

# ENamedElement class attributes and methods

# Catalog class attributes and methods

# Assertion class attributes and methods

# CharacterSet class attributes and methods

# Dependency class attributes and methods

# Comment class attributes and methods

# ObjectExtension class attributes and methods

# Schema class attributes and methods

# sqlmodel_schema_Database class attributes and methods
sqlmodel_schema_Database_vendor: Property = Property(name="vendor", type=StringType)
sqlmodel_schema_Database_version: Property = Property(name="version", type=StringType)
sqlmodel_schema_Database_m_getUserDefinedTypes: Method = Method(name="getUserDefinedTypes", parameters={}, type=StringType)
sqlmodel_schema_Database.attributes={sqlmodel_schema_Database_vendor, sqlmodel_schema_Database_version}
sqlmodel_schema_Database.methods={sqlmodel_schema_Database_m_getUserDefinedTypes}

# Privilege class attributes and methods

# sqlmodel_schema_Sequence class attributes and methods

# TypedElement class attributes and methods

# IdentitySpecifier class attributes and methods

# Event class attributes and methods

# sqlmodel_schema_Event class attributes and methods
sqlmodel_schema_Event_condition: Property = Property(name="condition", type=StringType)
sqlmodel_schema_Event_action: Property = Property(name="action", type=StringType)
sqlmodel_schema_Event_enabled: Property = Property(name="enabled", type=BooleanType)
sqlmodel_schema_Event_for_: Property = Property(name="for_", type=StringType)
sqlmodel_schema_Event.attributes={sqlmodel_schema_Event_action, sqlmodel_schema_Event_condition, sqlmodel_schema_Event_for_, sqlmodel_schema_Event_enabled}

# sqlmodel_schema_Catalog class attributes and methods

# sqlmodel_schema_ObjectExtension class attributes and methods

# sqlmodel_schema_Comment class attributes and methods
sqlmodel_schema_Comment_description: Property = Property(name="description", type=StringType)
sqlmodel_schema_Comment.attributes={sqlmodel_schema_Comment_description}

# BaseTable class attributes and methods

# sqlmodel_constraints_Constraint class attributes and methods
sqlmodel_constraints_Constraint_deferrable: Property = Property(name="deferrable", type=BooleanType)
sqlmodel_constraints_Constraint_initiallyDeferred: Property = Property(name="initiallyDeferred", type=BooleanType)
sqlmodel_constraints_Constraint_enforced: Property = Property(name="enforced", type=BooleanType)
sqlmodel_constraints_Constraint.attributes={sqlmodel_constraints_Constraint_deferrable, sqlmodel_constraints_Constraint_enforced, sqlmodel_constraints_Constraint_initiallyDeferred}

# sqlmodel_constraints_Assertion class attributes and methods

# Constraint class attributes and methods

# SearchCondition class attributes and methods

# sqlmodel_constraints_ReferenceConstraint class attributes and methods

# TableConstraint class attributes and methods

# Column class attributes and methods

# sqlmodel_constraints_CheckConstraint class attributes and methods

# sqlmodel_constraints_TableConstraint class attributes and methods

# sqlmodel_constraints_ForeignKey class attributes and methods
sqlmodel_constraints_ForeignKey_match: Property = Property(name="match", type=StringType)
sqlmodel_constraints_ForeignKey_onUpdate: Property = Property(name="onUpdate", type=StringType)
sqlmodel_constraints_ForeignKey_onDelete: Property = Property(name="onDelete", type=StringType)
sqlmodel_constraints_ForeignKey.attributes={sqlmodel_constraints_ForeignKey_onDelete, sqlmodel_constraints_ForeignKey_match, sqlmodel_constraints_ForeignKey_onUpdate}

# ReferenceConstraint class attributes and methods

# UniqueConstraint class attributes and methods

# sqlmodel_constraints_UniqueConstraint class attributes and methods
sqlmodel_constraints_UniqueConstraint_clustered: Property = Property(name="clustered", type=BooleanType)
sqlmodel_constraints_UniqueConstraint.attributes={sqlmodel_constraints_UniqueConstraint_clustered}

# sqlmodel_constraints_PrimaryKey class attributes and methods

# sqlmodel_constraints_Index class attributes and methods
sqlmodel_constraints_Index_unique: Property = Property(name="unique", type=BooleanType)
sqlmodel_constraints_Index_systemGenerated: Property = Property(name="systemGenerated", type=BooleanType)
sqlmodel_constraints_Index_clustered: Property = Property(name="clustered", type=BooleanType)
sqlmodel_constraints_Index_fillFactor: Property = Property(name="fillFactor", type=IntegerType)
sqlmodel_constraints_Index.attributes={sqlmodel_constraints_Index_unique, sqlmodel_constraints_Index_fillFactor, sqlmodel_constraints_Index_clustered, sqlmodel_constraints_Index_systemGenerated}

# ForeignKey class attributes and methods

# IndexMember class attributes and methods

# sqlmodel_constraints_IndexMember class attributes and methods
sqlmodel_constraints_IndexMember_incrementType: Property = Property(name="incrementType", type=StringType)
sqlmodel_constraints_IndexMember.attributes={sqlmodel_constraints_IndexMember_incrementType}

# sqlmodel_constraints_IndexExpression class attributes and methods
sqlmodel_constraints_IndexExpression_sql: Property = Property(name="sql", type=StringType)
sqlmodel_constraints_IndexExpression.attributes={sqlmodel_constraints_IndexExpression_sql}

# sqlmodel_datatypes_UserDefinedType class attributes and methods

# DataType class attributes and methods

# UserDefinedTypeOrdering class attributes and methods

# IndexExpression class attributes and methods

# sqlmodel_datatypes_PredefinedDataType class attributes and methods
sqlmodel_datatypes_PredefinedDataType_primitiveType: Property = Property(name="primitiveType", type=StringType)
sqlmodel_datatypes_PredefinedDataType.attributes={sqlmodel_datatypes_PredefinedDataType_primitiveType}

# sqlmodel_datatypes_CollectionDataType class attributes and methods

# ConstructedDataType class attributes and methods

# ElementType class attributes and methods

# sqlmodel_datatypes_NumericalDataType class attributes and methods
sqlmodel_datatypes_NumericalDataType_precision: Property = Property(name="precision", type=IntegerType)
sqlmodel_datatypes_NumericalDataType.attributes={sqlmodel_datatypes_NumericalDataType_precision}

# PredefinedDataType class attributes and methods

# sqlmodel_datatypes_DataType class attributes and methods
sqlmodel_datatypes_DataType_m_setContainer: Method = Method(name="setContainer", parameters={Parameter(name='sqlmodel_newContainer', type=StringType)})
sqlmodel_datatypes_DataType.methods={sqlmodel_datatypes_DataType_m_setContainer}

# sqlmodel_datatypes_RowDataType class attributes and methods

# Field class attributes and methods

# sqlmodel_datatypes_CharacterStringDataType class attributes and methods
sqlmodel_datatypes_CharacterStringDataType_collationName: Property = Property(name="collationName", type=StringType)
sqlmodel_datatypes_CharacterStringDataType_length: Property = Property(name="length", type=IntegerType)
sqlmodel_datatypes_CharacterStringDataType_coercibility: Property = Property(name="coercibility", type=StringType)
sqlmodel_datatypes_CharacterStringDataType_fixedLength: Property = Property(name="fixedLength", type=BooleanType)
sqlmodel_datatypes_CharacterStringDataType.attributes={sqlmodel_datatypes_CharacterStringDataType_fixedLength, sqlmodel_datatypes_CharacterStringDataType_length, sqlmodel_datatypes_CharacterStringDataType_coercibility, sqlmodel_datatypes_CharacterStringDataType_collationName}

# sqlmodel_datatypes_ArrayDataType class attributes and methods
sqlmodel_datatypes_ArrayDataType_maxCardinality: Property = Property(name="maxCardinality", type=IntegerType)
sqlmodel_datatypes_ArrayDataType.attributes={sqlmodel_datatypes_ArrayDataType_maxCardinality}

# CollectionDataType class attributes and methods

# sqlmodel_datatypes_MultisetDataType class attributes and methods

# sqlmodel_datatypes_IntervalDataType class attributes and methods
sqlmodel_datatypes_IntervalDataType_leadingQualifier: Property = Property(name="leadingQualifier", type=StringType)
sqlmodel_datatypes_IntervalDataType_trailingQualifier: Property = Property(name="trailingQualifier", type=StringType)
sqlmodel_datatypes_IntervalDataType_leadingFieldPrecision: Property = Property(name="leadingFieldPrecision", type=IntegerType)
sqlmodel_datatypes_IntervalDataType_trailingFieldPrecision: Property = Property(name="trailingFieldPrecision", type=IntegerType)
sqlmodel_datatypes_IntervalDataType_fractionalSecondsPrecision: Property = Property(name="fractionalSecondsPrecision", type=IntegerType)
sqlmodel_datatypes_IntervalDataType.attributes={sqlmodel_datatypes_IntervalDataType_leadingFieldPrecision, sqlmodel_datatypes_IntervalDataType_leadingQualifier, sqlmodel_datatypes_IntervalDataType_trailingFieldPrecision, sqlmodel_datatypes_IntervalDataType_fractionalSecondsPrecision, sqlmodel_datatypes_IntervalDataType_trailingQualifier}

# sqlmodel_datatypes_BooleanDataType class attributes and methods

# sqlmodel_datatypes_BinaryStringDataType class attributes and methods
sqlmodel_datatypes_BinaryStringDataType_length: Property = Property(name="length", type=IntegerType)
sqlmodel_datatypes_BinaryStringDataType_m_equals: Method = Method(name="equals", parameters={}, type=BooleanType)
sqlmodel_datatypes_BinaryStringDataType.attributes={sqlmodel_datatypes_BinaryStringDataType_length}
sqlmodel_datatypes_BinaryStringDataType.methods={sqlmodel_datatypes_BinaryStringDataType_m_equals}

# sqlmodel_datatypes_CharacterSet class attributes and methods
sqlmodel_datatypes_CharacterSet_defaultCollation: Property = Property(name="defaultCollation", type=StringType)
sqlmodel_datatypes_CharacterSet_encoding: Property = Property(name="encoding", type=StringType)
sqlmodel_datatypes_CharacterSet_repertoire: Property = Property(name="repertoire", type=StringType)
sqlmodel_datatypes_CharacterSet.attributes={sqlmodel_datatypes_CharacterSet_repertoire, sqlmodel_datatypes_CharacterSet_defaultCollation, sqlmodel_datatypes_CharacterSet_encoding}

# CharacterStringDataType class attributes and methods

# sqlmodel_datatypes_TimeDataType class attributes and methods
sqlmodel_datatypes_TimeDataType_fractionalSecondsPrecision: Property = Property(name="fractionalSecondsPrecision", type=IntegerType)
sqlmodel_datatypes_TimeDataType_timeZone: Property = Property(name="timeZone", type=BooleanType)
sqlmodel_datatypes_TimeDataType.attributes={sqlmodel_datatypes_TimeDataType_fractionalSecondsPrecision, sqlmodel_datatypes_TimeDataType_timeZone}

# sqlmodel_datatypes_DistinctUserDefinedType class attributes and methods

# sqlmodel_datatypes_StructuredUserDefinedType class attributes and methods
sqlmodel_datatypes_StructuredUserDefinedType_instantiable: Property = Property(name="instantiable", type=BooleanType)
sqlmodel_datatypes_StructuredUserDefinedType_final: Property = Property(name="final", type=BooleanType)
sqlmodel_datatypes_StructuredUserDefinedType.attributes={sqlmodel_datatypes_StructuredUserDefinedType_final, sqlmodel_datatypes_StructuredUserDefinedType_instantiable}

# AttributeDefinition class attributes and methods

# Method class attributes and methods

# StructuredUserDefinedType class attributes and methods

# sqlmodel_datatypes_FixedPrecisionDataType class attributes and methods

# ExactNumericDataType class attributes and methods

# sqlmodel_datatypes_AttributeDefinition class attributes and methods
sqlmodel_datatypes_AttributeDefinition_scopeCheck: Property = Property(name="scopeCheck", type=StringType)
sqlmodel_datatypes_AttributeDefinition_scopeChecked: Property = Property(name="scopeChecked", type=BooleanType)
sqlmodel_datatypes_AttributeDefinition_defaultValue: Property = Property(name="defaultValue", type=StringType)
sqlmodel_datatypes_AttributeDefinition.attributes={sqlmodel_datatypes_AttributeDefinition_scopeChecked, sqlmodel_datatypes_AttributeDefinition_scopeCheck, sqlmodel_datatypes_AttributeDefinition_defaultValue}

# sqlmodel_datatypes_Domain class attributes and methods
sqlmodel_datatypes_Domain_defaultValue: Property = Property(name="defaultValue", type=StringType)
sqlmodel_datatypes_Domain.attributes={sqlmodel_datatypes_Domain_defaultValue}

# sqlmodel_datatypes_Field class attributes and methods
sqlmodel_datatypes_Field_scopeCheck: Property = Property(name="scopeCheck", type=StringType)
sqlmodel_datatypes_Field_scopeChecked: Property = Property(name="scopeChecked", type=BooleanType)
sqlmodel_datatypes_Field.attributes={sqlmodel_datatypes_Field_scopeChecked, sqlmodel_datatypes_Field_scopeCheck}

# sqlmodel_datatypes_ReferenceDataType class attributes and methods

# DistinctUserDefinedType class attributes and methods

# CheckConstraint class attributes and methods

# sqlmodel_datatypes_DataLinkDataType class attributes and methods
sqlmodel_datatypes_DataLinkDataType_length: Property = Property(name="length", type=IntegerType)
sqlmodel_datatypes_DataLinkDataType_linkControl: Property = Property(name="linkControl", type=StringType)
sqlmodel_datatypes_DataLinkDataType_integrityControl: Property = Property(name="integrityControl", type=StringType)
sqlmodel_datatypes_DataLinkDataType_readPermission: Property = Property(name="readPermission", type=StringType)
sqlmodel_datatypes_DataLinkDataType_writePermission: Property = Property(name="writePermission", type=StringType)
sqlmodel_datatypes_DataLinkDataType_recovery: Property = Property(name="recovery", type=BooleanType)
sqlmodel_datatypes_DataLinkDataType_unlink: Property = Property(name="unlink", type=StringType)
sqlmodel_datatypes_DataLinkDataType.attributes={sqlmodel_datatypes_DataLinkDataType_length, sqlmodel_datatypes_DataLinkDataType_recovery, sqlmodel_datatypes_DataLinkDataType_writePermission, sqlmodel_datatypes_DataLinkDataType_linkControl, sqlmodel_datatypes_DataLinkDataType_readPermission, sqlmodel_datatypes_DataLinkDataType_unlink, sqlmodel_datatypes_DataLinkDataType_integrityControl}

# sqlmodel_datatypes_ConstructedDataType class attributes and methods

# sqlmodel_datatypes_SQLDataType class attributes and methods

# sqlmodel_datatypes_UserDefinedTypeOrdering class attributes and methods
sqlmodel_datatypes_UserDefinedTypeOrdering_orderingForm: Property = Property(name="orderingForm", type=StringType)
sqlmodel_datatypes_UserDefinedTypeOrdering_orderingCategory: Property = Property(name="orderingCategory", type=StringType)
sqlmodel_datatypes_UserDefinedTypeOrdering.attributes={sqlmodel_datatypes_UserDefinedTypeOrdering_orderingForm, sqlmodel_datatypes_UserDefinedTypeOrdering_orderingCategory}

# sqlmodel_datatypes_ExactNumericDataType class attributes and methods
sqlmodel_datatypes_ExactNumericDataType_scale: Property = Property(name="scale", type=IntegerType)
sqlmodel_datatypes_ExactNumericDataType.attributes={sqlmodel_datatypes_ExactNumericDataType_scale}

# NumericalDataType class attributes and methods

# sqlmodel_datatypes_ApproximateNumericDataType class attributes and methods

# sqlmodel_datatypes_IntegerDataType class attributes and methods

# sqlmodel_datatypes_XMLDataType class attributes and methods

# sqlmodel_datatypes_ElementType class attributes and methods

# sqlmodel_datatypes_DateDataType class attributes and methods

# sqlmodel_expressions_ValueExpression class attributes and methods
sqlmodel_expressions_ValueExpression_m_getSQL: Method = Method(name="getSQL", parameters={}, type=StringType)
sqlmodel_expressions_ValueExpression_m_setSQL: Method = Method(name="setSQL", parameters={Parameter(name='sqlmodel_sqlText', type=StringType)})
sqlmodel_expressions_ValueExpression.methods={sqlmodel_expressions_ValueExpression_m_getSQL, sqlmodel_expressions_ValueExpression_m_setSQL}

# sqlmodel_expressions_SearchCondition class attributes and methods
sqlmodel_expressions_SearchCondition_m_getSQL: Method = Method(name="getSQL", parameters={}, type=StringType)
sqlmodel_expressions_SearchCondition_m_setSQL: Method = Method(name="setSQL", parameters={Parameter(name='sqlmodel_sqlText', type=StringType)})
sqlmodel_expressions_SearchCondition.methods={sqlmodel_expressions_SearchCondition_m_setSQL, sqlmodel_expressions_SearchCondition_m_getSQL}

# sqlmodel_expressions_QueryExpressionDefault class attributes and methods
sqlmodel_expressions_QueryExpressionDefault_SQL: Property = Property(name="SQL", type=StringType)
sqlmodel_expressions_QueryExpressionDefault.attributes={sqlmodel_expressions_QueryExpressionDefault_SQL}

# schema_SQLObject class attributes and methods

# expressions_QueryExpression class attributes and methods

# sqlmodel_expressions_QueryExpression class attributes and methods
sqlmodel_expressions_QueryExpression_m_getSQL: Method = Method(name="getSQL", parameters={}, type=StringType)
sqlmodel_expressions_QueryExpression_m_setSQL: Method = Method(name="setSQL", parameters={Parameter(name='sqlmodel_sqlText', type=StringType)})
sqlmodel_expressions_QueryExpression.methods={sqlmodel_expressions_QueryExpression_m_getSQL, sqlmodel_expressions_QueryExpression_m_setSQL}

# sqlmodel_expressions_ValueExpressionDefault class attributes and methods
sqlmodel_expressions_ValueExpressionDefault_SQL: Property = Property(name="SQL", type=StringType)
sqlmodel_expressions_ValueExpressionDefault.attributes={sqlmodel_expressions_ValueExpressionDefault_SQL}

# expressions_ValueExpression class attributes and methods

# sqlmodel_routines_Routine class attributes and methods
sqlmodel_routines_Routine_specificName: Property = Property(name="specificName", type=StringType)
sqlmodel_routines_Routine_sqlDataAccess: Property = Property(name="sqlDataAccess", type=StringType)
sqlmodel_routines_Routine_creationTS: Property = Property(name="creationTS", type=StringType)
sqlmodel_routines_Routine_lastAlteredTS: Property = Property(name="lastAlteredTS", type=StringType)
sqlmodel_routines_Routine_authorizationID: Property = Property(name="authorizationID", type=StringType)
sqlmodel_routines_Routine_security: Property = Property(name="security", type=StringType)
sqlmodel_routines_Routine_language: Property = Property(name="language", type=StringType)
sqlmodel_routines_Routine_parameterStyle: Property = Property(name="parameterStyle", type=StringType)
sqlmodel_routines_Routine_deterministic: Property = Property(name="deterministic", type=BooleanType)
sqlmodel_routines_Routine_externalName: Property = Property(name="externalName", type=StringType)
sqlmodel_routines_Routine.attributes={sqlmodel_routines_Routine_externalName, sqlmodel_routines_Routine_creationTS, sqlmodel_routines_Routine_security, sqlmodel_routines_Routine_parameterStyle, sqlmodel_routines_Routine_specificName, sqlmodel_routines_Routine_deterministic, sqlmodel_routines_Routine_authorizationID, sqlmodel_routines_Routine_sqlDataAccess, sqlmodel_routines_Routine_lastAlteredTS, sqlmodel_routines_Routine_language}

# sqlmodel_expressions_SearchConditionDefault class attributes and methods
sqlmodel_expressions_SearchConditionDefault_SQL: Property = Property(name="SQL", type=StringType)
sqlmodel_expressions_SearchConditionDefault.attributes={sqlmodel_expressions_SearchConditionDefault_SQL}

# expressions_SearchCondition class attributes and methods

# Parameter class attributes and methods

# Source class attributes and methods

# sqlmodel_routines_Source class attributes and methods
sqlmodel_routines_Source_body: Property = Property(name="body", type=StringType)
sqlmodel_routines_Source.attributes={sqlmodel_routines_Source_body}

# sqlmodel_routines_Procedure class attributes and methods
sqlmodel_routines_Procedure_maxResultSets: Property = Property(name="maxResultSets", type=IntegerType)
sqlmodel_routines_Procedure_oldSavePoint: Property = Property(name="oldSavePoint", type=BooleanType)
sqlmodel_routines_Procedure.attributes={sqlmodel_routines_Procedure_oldSavePoint, sqlmodel_routines_Procedure_maxResultSets}

# sqlmodel_routines_Parameter class attributes and methods
sqlmodel_routines_Parameter_locator: Property = Property(name="locator", type=BooleanType)
sqlmodel_routines_Parameter_mode: Property = Property(name="mode", type=StringType)
sqlmodel_routines_Parameter.attributes={sqlmodel_routines_Parameter_locator, sqlmodel_routines_Parameter_mode}

# sqlmodel_routines_Function class attributes and methods
sqlmodel_routines_Function_nullCall: Property = Property(name="nullCall", type=BooleanType)
sqlmodel_routines_Function_static: Property = Property(name="static", type=BooleanType)
sqlmodel_routines_Function_transformGroup: Property = Property(name="transformGroup", type=StringType)
sqlmodel_routines_Function_typePreserving: Property = Property(name="typePreserving", type=BooleanType)
sqlmodel_routines_Function_mutator: Property = Property(name="mutator", type=BooleanType)
sqlmodel_routines_Function.attributes={sqlmodel_routines_Function_typePreserving, sqlmodel_routines_Function_mutator, sqlmodel_routines_Function_nullCall, sqlmodel_routines_Function_transformGroup, sqlmodel_routines_Function_static}

# RoutineResultTable class attributes and methods

# sqlmodel_routines_RoutineResultTable class attributes and methods

# sqlmodel_routines_Method class attributes and methods
sqlmodel_routines_Method_overriding: Property = Property(name="overriding", type=BooleanType)
sqlmodel_routines_Method_constructor: Property = Property(name="constructor", type=BooleanType)
sqlmodel_routines_Method.attributes={sqlmodel_routines_Method_overriding, sqlmodel_routines_Method_constructor}

# Function class attributes and methods

# sqlmodel_routines_BuiltInFunction class attributes and methods

# sqlmodel_statements_SQLStatement class attributes and methods
sqlmodel_statements_SQLStatement_m_getSQL: Method = Method(name="getSQL", parameters={}, type=StringType)
sqlmodel_statements_SQLStatement_m_setSQL: Method = Method(name="setSQL", parameters={Parameter(name='sqlmodel_sqlText', type=StringType)})
sqlmodel_statements_SQLStatement.methods={sqlmodel_statements_SQLStatement_m_getSQL, sqlmodel_statements_SQLStatement_m_setSQL}

# sqlmodel_statements_SQLDataStatement class attributes and methods

# SQLStatement class attributes and methods

# sqlmodel_statements_SQLSchemaStatement class attributes and methods

# sqlmodel_routines_UserDefinedFunction class attributes and methods

# sqlmodel_statements_SQLDataChangeStatement class attributes and methods

# SQLDataStatement class attributes and methods

# sqlmodel_statements_SQLStatementDefault class attributes and methods
sqlmodel_statements_SQLStatementDefault_SQL: Property = Property(name="SQL", type=StringType)
sqlmodel_statements_SQLStatementDefault.attributes={sqlmodel_statements_SQLStatementDefault_SQL}

# statements_SQLStatement class attributes and methods

# sqlmodel_statements_SQLConnectionStatement class attributes and methods

# sqlmodel_statements_SQLDiagnosticsStatement class attributes and methods

# sqlmodel_statements_SQLDynamicStatement class attributes and methods

# sqlmodel_statements_SQLControlStatement class attributes and methods

# sqlmodel_tables_ViewTable class attributes and methods
sqlmodel_tables_ViewTable_checkType: Property = Property(name="checkType", type=StringType)
sqlmodel_tables_ViewTable.attributes={sqlmodel_tables_ViewTable_checkType}

# DerivedTable class attributes and methods

# sqlmodel_tables_TemporaryTable class attributes and methods
sqlmodel_tables_TemporaryTable_local: Property = Property(name="local", type=BooleanType)
sqlmodel_tables_TemporaryTable_deleteOnCommit: Property = Property(name="deleteOnCommit", type=BooleanType)
sqlmodel_tables_TemporaryTable.attributes={sqlmodel_tables_TemporaryTable_deleteOnCommit, sqlmodel_tables_TemporaryTable_local}

# sqlmodel_tables_Table class attributes and methods
sqlmodel_tables_Table_selfRefColumnGeneration: Property = Property(name="selfRefColumnGeneration", type=StringType)
sqlmodel_tables_Table_insertable: Property = Property(name="insertable", type=BooleanType)
sqlmodel_tables_Table_updatable: Property = Property(name="updatable", type=BooleanType)
sqlmodel_tables_Table.attributes={sqlmodel_tables_Table_selfRefColumnGeneration, sqlmodel_tables_Table_updatable, sqlmodel_tables_Table_insertable}

# sqlmodel_statements_SQLSessionStatement class attributes and methods

# sqlmodel_statements_SQLTransactionStatement class attributes and methods

# sqlmodel_tables_DerivedTable class attributes and methods

# QueryExpression class attributes and methods

# sqlmodel_tables_BaseTable class attributes and methods
sqlmodel_tables_BaseTable_m_getUniqueConstraints: Method = Method(name="getUniqueConstraints", parameters={}, type=StringType)
sqlmodel_tables_BaseTable_m_getForeignKeys: Method = Method(name="getForeignKeys", parameters={}, type=StringType)
sqlmodel_tables_BaseTable_m_getPrimaryKey: Method = Method(name="getPrimaryKey", parameters={}, type=StringType)
sqlmodel_tables_BaseTable.methods={sqlmodel_tables_BaseTable_m_getForeignKeys, sqlmodel_tables_BaseTable_m_getUniqueConstraints, sqlmodel_tables_BaseTable_m_getPrimaryKey}

# sqlmodel_tables_PersistentTable class attributes and methods

# sqlmodel_tables_Column class attributes and methods
sqlmodel_tables_Column_implementationDependent: Property = Property(name="implementationDependent", type=BooleanType)
sqlmodel_tables_Column_nullable: Property = Property(name="nullable", type=BooleanType)
sqlmodel_tables_Column_defaultValue: Property = Property(name="defaultValue", type=StringType)
sqlmodel_tables_Column_scopeCheck: Property = Property(name="scopeCheck", type=StringType)
sqlmodel_tables_Column_scopeChecked: Property = Property(name="scopeChecked", type=BooleanType)
sqlmodel_tables_Column_m_isPartOfForeignKey: Method = Method(name="isPartOfForeignKey", parameters={}, type=BooleanType)
sqlmodel_tables_Column_m_isPartOfUniqueConstraint: Method = Method(name="isPartOfUniqueConstraint", parameters={}, type=BooleanType)
sqlmodel_tables_Column_m_isPartOfPrimaryKey: Method = Method(name="isPartOfPrimaryKey", parameters={}, type=BooleanType)
sqlmodel_tables_Column.attributes={sqlmodel_tables_Column_scopeCheck, sqlmodel_tables_Column_scopeChecked, sqlmodel_tables_Column_defaultValue, sqlmodel_tables_Column_implementationDependent, sqlmodel_tables_Column_nullable}
sqlmodel_tables_Column.methods={sqlmodel_tables_Column_m_isPartOfUniqueConstraint, sqlmodel_tables_Column_m_isPartOfPrimaryKey, sqlmodel_tables_Column_m_isPartOfForeignKey}

# ValueExpression class attributes and methods

# sqlmodel_tables_Trigger class attributes and methods
sqlmodel_tables_Trigger_actionGranularity: Property = Property(name="actionGranularity", type=StringType)
sqlmodel_tables_Trigger_timeStamp: Property = Property(name="timeStamp", type=StringType)
sqlmodel_tables_Trigger_actionTime: Property = Property(name="actionTime", type=StringType)
sqlmodel_tables_Trigger_updateType: Property = Property(name="updateType", type=BooleanType)
sqlmodel_tables_Trigger_insertType: Property = Property(name="insertType", type=BooleanType)
sqlmodel_tables_Trigger_deleteType: Property = Property(name="deleteType", type=BooleanType)
sqlmodel_tables_Trigger_oldRow: Property = Property(name="oldRow", type=StringType)
sqlmodel_tables_Trigger_newRow: Property = Property(name="newRow", type=StringType)
sqlmodel_tables_Trigger_oldTable: Property = Property(name="oldTable", type=StringType)
sqlmodel_tables_Trigger_newTable: Property = Property(name="newTable", type=StringType)
sqlmodel_tables_Trigger.attributes={sqlmodel_tables_Trigger_actionGranularity, sqlmodel_tables_Trigger_oldTable, sqlmodel_tables_Trigger_updateType, sqlmodel_tables_Trigger_actionTime, sqlmodel_tables_Trigger_timeStamp, sqlmodel_tables_Trigger_deleteType, sqlmodel_tables_Trigger_oldRow, sqlmodel_tables_Trigger_newRow, sqlmodel_tables_Trigger_insertType, sqlmodel_tables_Trigger_newTable}

# sqlmodel_accesscontrol_AuthorizationIdentifier class attributes and methods

# sqlmodel_accesscontrol_Privilege class attributes and methods
sqlmodel_accesscontrol_Privilege_grantable: Property = Property(name="grantable", type=BooleanType)
sqlmodel_accesscontrol_Privilege_action: Property = Property(name="action", type=StringType)
sqlmodel_accesscontrol_Privilege_withHierarchy: Property = Property(name="withHierarchy", type=BooleanType)
sqlmodel_accesscontrol_Privilege.attributes={sqlmodel_accesscontrol_Privilege_grantable, sqlmodel_accesscontrol_Privilege_action, sqlmodel_accesscontrol_Privilege_withHierarchy}

# RoleAuthorization class attributes and methods

# sqlmodel_accesscontrol_Group class attributes and methods

# sqlmodel_accesscontrol_RoleAuthorization class attributes and methods
sqlmodel_accesscontrol_RoleAuthorization_grantable: Property = Property(name="grantable", type=BooleanType)
sqlmodel_accesscontrol_RoleAuthorization.attributes={sqlmodel_accesscontrol_RoleAuthorization_grantable}

# Role class attributes and methods

# User class attributes and methods

# sqlmodel_accesscontrol_User class attributes and methods

# Group class attributes and methods

# sqlmodel_accesscontrol_Role class attributes and methods

# Relationships
containedType0: BinaryAssociation = BinaryAssociation(
    name="containedType0",
    ends={
        Property(name="SQLDataType", type=sqlmodel_schema_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_schema_TypedElement", type=SQLDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedType1: BinaryAssociation = BinaryAssociation(
    name="referencedType1",
    ends={
        Property(name="UserDefinedType", type=sqlmodel_schema_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_schema_TypedElement2", type=UserDefinedType, multiplicity=Multiplicity(0, 1))
    }
)
triggers4: BinaryAssociation = BinaryAssociation(
    name="triggers4",
    ends={
        Property(name="Trigger", type=sqlmodel_schema_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
indices5: BinaryAssociation = BinaryAssociation(
    name="indices5",
    ends={
        Property(name="Index", type=sqlmodel_schema_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema", type=Index, multiplicity=Multiplicity(0, 9999))
    }
)
tables6: BinaryAssociation = BinaryAssociation(
    name="tables6",
    ends={
        Property(name="Table", type=sqlmodel_schema_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema7", type=Table, multiplicity=Multiplicity(0, 9999))
    }
)
sequences8: BinaryAssociation = BinaryAssociation(
    name="sequences8",
    ends={
        Property(name="Sequence", type=sqlmodel_schema_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema9", type=Sequence, multiplicity=Multiplicity(0, 9999))
    }
)
database10: BinaryAssociation = BinaryAssociation(
    name="database10",
    ends={
        Property(name="Database", type=sqlmodel_schema_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schemas", type=Database, multiplicity=Multiplicity(1, 1))
    }
)
targetEnd3: BinaryAssociation = BinaryAssociation(
    name="targetEnd3",
    ends={
        Property(name="schema_sqlmodel_EObject", type=sqlmodel_schema_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_schema_Dependency", type=schema_sqlmodel_EObject, multiplicity=Multiplicity(1, 1))
    }
)
routines20: BinaryAssociation = BinaryAssociation(
    name="routines20",
    ends={
        Property(name="Routine", type=sqlmodel_schema_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema21", type=Routine, multiplicity=Multiplicity(0, 9999))
    }
)
owner22: BinaryAssociation = BinaryAssociation(
    name="owner22",
    ends={
        Property(name="AuthorizationIdentifier", type=sqlmodel_schema_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedSchema", type=AuthorizationIdentifier, multiplicity=Multiplicity(1, 1))
    }
)
Catalog11: BinaryAssociation = BinaryAssociation(
    name="Catalog11",
    ends={
        Property(name="Catalog", type=sqlmodel_schema_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schemas12", type=Catalog, multiplicity=Multiplicity(1, 1))
    }
)
assertions13: BinaryAssociation = BinaryAssociation(
    name="assertions13",
    ends={
        Property(name="Assertion", type=sqlmodel_schema_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema14", type=Assertion, multiplicity=Multiplicity(0, 9999))
    }
)
userDefinedTypes15: BinaryAssociation = BinaryAssociation(
    name="userDefinedTypes15",
    ends={
        Property(name="UserDefinedType17", type=sqlmodel_schema_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema16", type=UserDefinedType, multiplicity=Multiplicity(0, 9999))
    }
)
charSets18: BinaryAssociation = BinaryAssociation(
    name="charSets18",
    ends={
        Property(name="CharacterSet", type=sqlmodel_schema_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema19", type=CharacterSet, multiplicity=Multiplicity(0, 9999))
    }
)
dependencies23: BinaryAssociation = BinaryAssociation(
    name="dependencies23",
    ends={
        Property(name="Dependency", type=sqlmodel_schema_SQLObject, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_schema_SQLObject", type=Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments24: BinaryAssociation = BinaryAssociation(
    name="comments24",
    ends={
        Property(name="Comment", type=sqlmodel_schema_SQLObject, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLObject", type=Comment, multiplicity=Multiplicity(0, 9999))
    }
)
identity28: BinaryAssociation = BinaryAssociation(
    name="identity28",
    ends={
        Property(name="sqlmodel_schema_Sequence", type=IdentitySpecifier, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="IdentitySpecifier", type=sqlmodel_schema_Sequence, multiplicity=Multiplicity(1, 1))
    }
)
schema29: BinaryAssociation = BinaryAssociation(
    name="schema29",
    ends={
        Property(name="Schema30", type=sqlmodel_schema_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="sequences", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
schemas31: BinaryAssociation = BinaryAssociation(
    name="schemas31",
    ends={
        Property(name="Schema32", type=sqlmodel_schema_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="database", type=Schema, multiplicity=Multiplicity(0, 9999))
    }
)
extensions25: BinaryAssociation = BinaryAssociation(
    name="extensions25",
    ends={
        Property(name="ObjectExtension", type=sqlmodel_schema_SQLObject, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLObject26", type=ObjectExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
privileges27: BinaryAssociation = BinaryAssociation(
    name="privileges27",
    ends={
        Property(name="Privilege", type=sqlmodel_schema_SQLObject, multiplicity=Multiplicity(1, 1)),
        Property(name="object", type=Privilege, multiplicity=Multiplicity(0, 9999))
    }
)
authorizationIds38: BinaryAssociation = BinaryAssociation(
    name="authorizationIds38",
    ends={
        Property(name="Database39", type=AuthorizationIdentifier, multiplicity=Multiplicity(0, 9999)),
        Property(name="AuthorizationIdentifier40", type=sqlmodel_schema_Database, multiplicity=Multiplicity(1, 1))
    }
)
events33: BinaryAssociation = BinaryAssociation(
    name="events33",
    ends={
        Property(name="Event", type=sqlmodel_schema_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Database34", type=Event, multiplicity=Multiplicity(0, 9999))
    }
)
catalogs35: BinaryAssociation = BinaryAssociation(
    name="catalogs35",
    ends={
        Property(name="Catalog37", type=sqlmodel_schema_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="Database36", type=Catalog, multiplicity=Multiplicity(0, 9999))
    }
)
Database41: BinaryAssociation = BinaryAssociation(
    name="Database41",
    ends={
        Property(name="Database42", type=sqlmodel_schema_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="events", type=Database, multiplicity=Multiplicity(1, 1))
    }
)
Database45: BinaryAssociation = BinaryAssociation(
    name="Database45",
    ends={
        Property(name="Database46", type=sqlmodel_schema_Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="catalogs", type=Database, multiplicity=Multiplicity(1, 1))
    }
)
schemas47: BinaryAssociation = BinaryAssociation(
    name="schemas47",
    ends={
        Property(name="Schema49", type=sqlmodel_schema_Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="Catalog48", type=Schema, multiplicity=Multiplicity(0, 9999))
    }
)
SQLObject50: BinaryAssociation = BinaryAssociation(
    name="SQLObject50",
    ends={
        Property(name="SQLObject51", type=sqlmodel_schema_ObjectExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="extensions", type=SQLObject, multiplicity=Multiplicity(1, 1))
    }
)
SQLObject43: BinaryAssociation = BinaryAssociation(
    name="SQLObject43",
    ends={
        Property(name="SQLObject44", type=sqlmodel_schema_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments", type=SQLObject, multiplicity=Multiplicity(1, 1))
    }
)
searchCondition52: BinaryAssociation = BinaryAssociation(
    name="searchCondition52",
    ends={
        Property(name="sqlmodel_constraints_Assertion", type=SearchCondition, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="SearchCondition", type=sqlmodel_constraints_Assertion, multiplicity=Multiplicity(1, 1))
    }
)
schema53: BinaryAssociation = BinaryAssociation(
    name="schema53",
    ends={
        Property(name="Schema54", type=sqlmodel_constraints_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="assertions", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
constrainedTables55: BinaryAssociation = BinaryAssociation(
    name="constrainedTables55",
    ends={
        Property(name="BaseTable", type=sqlmodel_constraints_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_constraints_Assertion56", type=BaseTable, multiplicity=Multiplicity(1, 9999))
    }
)
members59: BinaryAssociation = BinaryAssociation(
    name="members59",
    ends={
        Property(name="Column", type=sqlmodel_constraints_ReferenceConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_constraints_ReferenceConstraint", type=Column, multiplicity=Multiplicity(1, 9999))
    }
)
BaseTable57: BinaryAssociation = BinaryAssociation(
    name="BaseTable57",
    ends={
        Property(name="BaseTable58", type=sqlmodel_constraints_TableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=BaseTable, multiplicity=Multiplicity(0, 1))
    }
)
uniqueConstraint62: BinaryAssociation = BinaryAssociation(
    name="uniqueConstraint62",
    ends={
        Property(name="UniqueConstraint", type=sqlmodel_constraints_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ForeignKey", type=UniqueConstraint, multiplicity=Multiplicity(0, 1))
    }
)
searchCondition60: BinaryAssociation = BinaryAssociation(
    name="searchCondition60",
    ends={
        Property(name="SearchCondition61", type=sqlmodel_constraints_CheckConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_constraints_CheckConstraint", type=SearchCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uniqueIndex65: BinaryAssociation = BinaryAssociation(
    name="uniqueIndex65",
    ends={
        Property(name="Index67", type=sqlmodel_constraints_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ForeignKey66", type=Index, multiplicity=Multiplicity(0, 1))
    }
)
referencedTable68: BinaryAssociation = BinaryAssociation(
    name="referencedTable68",
    ends={
        Property(name="BaseTable69", type=sqlmodel_constraints_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingForeignKeys", type=BaseTable, multiplicity=Multiplicity(0, 1))
    }
)
referencedMembers63: BinaryAssociation = BinaryAssociation(
    name="referencedMembers63",
    ends={
        Property(name="Column64", type=sqlmodel_constraints_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_constraints_ForeignKey", type=Column, multiplicity=Multiplicity(1, 9999))
    }
)
ForeignKey70: BinaryAssociation = BinaryAssociation(
    name="ForeignKey70",
    ends={
        Property(name="ForeignKey71", type=sqlmodel_constraints_UniqueConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueConstraint", type=ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
members74: BinaryAssociation = BinaryAssociation(
    name="members74",
    ends={
        Property(name="IndexMember", type=sqlmodel_constraints_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_constraints_Index", type=IndexMember, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
table75: BinaryAssociation = BinaryAssociation(
    name="table75",
    ends={
        Property(name="Table76", type=sqlmodel_constraints_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="index", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
ForeignKey77: BinaryAssociation = BinaryAssociation(
    name="ForeignKey77",
    ends={
        Property(name="ForeignKey78", type=sqlmodel_constraints_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueIndex", type=ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
includedMembers79: BinaryAssociation = BinaryAssociation(
    name="includedMembers79",
    ends={
        Property(name="IndexMember81", type=sqlmodel_constraints_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_constraints_Index80", type=IndexMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Schema72: BinaryAssociation = BinaryAssociation(
    name="Schema72",
    ends={
        Property(name="Schema73", type=sqlmodel_constraints_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="indices", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
schema86: BinaryAssociation = BinaryAssociation(
    name="schema86",
    ends={
        Property(name="Schema87", type=sqlmodel_datatypes_UserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="userDefinedTypes", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
column82: BinaryAssociation = BinaryAssociation(
    name="column82",
    ends={
        Property(name="Column83", type=sqlmodel_constraints_IndexMember, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_constraints_IndexMember", type=Column, multiplicity=Multiplicity(0, 1))
    }
)
expression84: BinaryAssociation = BinaryAssociation(
    name="expression84",
    ends={
        Property(name="IndexExpression", type=sqlmodel_constraints_IndexMember, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_constraints_IndexMember85", type=IndexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType89: BinaryAssociation = BinaryAssociation(
    name="elementType89",
    ends={
        Property(name="ElementType", type=sqlmodel_datatypes_CollectionDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionDataType", type=ElementType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ordering88: BinaryAssociation = BinaryAssociation(
    name="ordering88",
    ends={
        Property(name="UserDefinedTypeOrdering", type=sqlmodel_datatypes_UserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_datatypes_UserDefinedType", type=UserDefinedTypeOrdering, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
characterSet90: BinaryAssociation = BinaryAssociation(
    name="characterSet90",
    ends={
        Property(name="CharacterSet91", type=sqlmodel_datatypes_CharacterStringDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="CharacterStringDataType", type=CharacterSet, multiplicity=Multiplicity(1, 1))
    }
)
fields92: BinaryAssociation = BinaryAssociation(
    name="fields92",
    ends={
        Property(name="Field", type=sqlmodel_datatypes_RowDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_datatypes_RowDataType", type=Field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
CharacterStringDataType93: BinaryAssociation = BinaryAssociation(
    name="CharacterStringDataType93",
    ends={
        Property(name="CharacterStringDataType94", type=sqlmodel_datatypes_CharacterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="characterSet", type=CharacterStringDataType, multiplicity=Multiplicity(1, 1))
    }
)
schema95: BinaryAssociation = BinaryAssociation(
    name="schema95",
    ends={
        Property(name="Schema96", type=sqlmodel_datatypes_CharacterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="charSets", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
predefinedRepresentation97: BinaryAssociation = BinaryAssociation(
    name="predefinedRepresentation97",
    ends={
        Property(name="PredefinedDataType", type=sqlmodel_datatypes_DistinctUserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_datatypes_DistinctUserDefinedType", type=PredefinedDataType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
super98: BinaryAssociation = BinaryAssociation(
    name="super98",
    ends={
        Property(name="StructuredUserDefinedType", type=sqlmodel_datatypes_StructuredUserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="sub", type=StructuredUserDefinedType, multiplicity=Multiplicity(0, 1))
    }
)
sub99: BinaryAssociation = BinaryAssociation(
    name="sub99",
    ends={
        Property(name="StructuredUserDefinedType100", type=sqlmodel_datatypes_StructuredUserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="super", type=StructuredUserDefinedType, multiplicity=Multiplicity(0, 9999))
    }
)
attributes101: BinaryAssociation = BinaryAssociation(
    name="attributes101",
    ends={
        Property(name="AttributeDefinition", type=sqlmodel_datatypes_StructuredUserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_datatypes_StructuredUserDefinedType", type=AttributeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods102: BinaryAssociation = BinaryAssociation(
    name="methods102",
    ends={
        Property(name="Method", type=sqlmodel_datatypes_StructuredUserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_datatypes_StructuredUserDefinedType103", type=Method_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopeTable105: BinaryAssociation = BinaryAssociation(
    name="scopeTable105",
    ends={
        Property(name="Table106", type=sqlmodel_datatypes_ReferenceDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_datatypes_ReferenceDataType", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
referencedType107: BinaryAssociation = BinaryAssociation(
    name="referencedType107",
    ends={
        Property(name="StructuredUserDefinedType109", type=sqlmodel_datatypes_ReferenceDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_datatypes_ReferenceDataType108", type=StructuredUserDefinedType, multiplicity=Multiplicity(1, 1))
    }
)
constraint104: BinaryAssociation = BinaryAssociation(
    name="constraint104",
    ends={
        Property(name="CheckConstraint", type=sqlmodel_datatypes_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_datatypes_Domain", type=CheckConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CollectionDataType112: BinaryAssociation = BinaryAssociation(
    name="CollectionDataType112",
    ends={
        Property(name="CollectionDataType113", type=sqlmodel_datatypes_ElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionDataType, multiplicity=Multiplicity(0, 1))
    }
)
orderingRoutine110: BinaryAssociation = BinaryAssociation(
    name="orderingRoutine110",
    ends={
        Property(name="Routine111", type=sqlmodel_datatypes_UserDefinedTypeOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_datatypes_UserDefinedTypeOrdering", type=Routine, multiplicity=Multiplicity(1, 1))
    }
)
parameters114: BinaryAssociation = BinaryAssociation(
    name="parameters114",
    ends={
        Property(name="Parameter", type=sqlmodel_routines_Routine, multiplicity=Multiplicity(1, 1)),
        Property(name="routine", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source115: BinaryAssociation = BinaryAssociation(
    name="source115",
    ends={
        Property(name="Source", type=sqlmodel_routines_Routine, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_routines_Routine", type=Source, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schema116: BinaryAssociation = BinaryAssociation(
    name="schema116",
    ends={
        Property(name="Schema117", type=sqlmodel_routines_Routine, multiplicity=Multiplicity(1, 1)),
        Property(name="routines", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
routine118: BinaryAssociation = BinaryAssociation(
    name="routine118",
    ends={
        Property(name="Routine119", type=sqlmodel_routines_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Routine, multiplicity=Multiplicity(1, 1))
    }
)
stringTypeOption120: BinaryAssociation = BinaryAssociation(
    name="stringTypeOption120",
    ends={
        Property(name="CharacterStringDataType121", type=sqlmodel_routines_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_routines_Parameter", type=CharacterStringDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnTable123: BinaryAssociation = BinaryAssociation(
    name="returnTable123",
    ends={
        Property(name="RoutineResultTable124", type=sqlmodel_routines_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_routines_Function", type=RoutineResultTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultSet122: BinaryAssociation = BinaryAssociation(
    name="resultSet122",
    ends={
        Property(name="RoutineResultTable", type=sqlmodel_routines_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_routines_Procedure", type=RoutineResultTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnScalar125: BinaryAssociation = BinaryAssociation(
    name="returnScalar125",
    ends={
        Property(name="Parameter127", type=sqlmodel_routines_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_routines_Function126", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnCast128: BinaryAssociation = BinaryAssociation(
    name="returnCast128",
    ends={
        Property(name="Parameter130", type=sqlmodel_routines_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_routines_Function129", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtables135: BinaryAssociation = BinaryAssociation(
    name="subtables135",
    ends={
        Property(name="Table136", type=sqlmodel_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="supertable", type=Table, multiplicity=Multiplicity(0, 9999))
    }
)
schema137: BinaryAssociation = BinaryAssociation(
    name="schema137",
    ends={
        Property(name="Schema138", type=sqlmodel_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
columns131: BinaryAssociation = BinaryAssociation(
    name="columns131",
    ends={
        Property(name="Column132", type=sqlmodel_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
udt139: BinaryAssociation = BinaryAssociation(
    name="udt139",
    ends={
        Property(name="StructuredUserDefinedType140", type=sqlmodel_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_tables_Table", type=StructuredUserDefinedType, multiplicity=Multiplicity(0, 1))
    }
)
queryExpression146: BinaryAssociation = BinaryAssociation(
    name="queryExpression146",
    ends={
        Property(name="QueryExpression", type=sqlmodel_tables_DerivedTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_tables_DerivedTable", type=QueryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
supertable133: BinaryAssociation = BinaryAssociation(
    name="supertable133",
    ends={
        Property(name="Table134", type=sqlmodel_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="subtables", type=Table, multiplicity=Multiplicity(0, 1))
    }
)
triggers141: BinaryAssociation = BinaryAssociation(
    name="triggers141",
    ends={
        Property(name="Trigger142", type=sqlmodel_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="subjectTable", type=Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
index143: BinaryAssociation = BinaryAssociation(
    name="index143",
    ends={
        Property(name="Index145", type=sqlmodel_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table144", type=Index, multiplicity=Multiplicity(0, 9999))
    }
)
table151: BinaryAssociation = BinaryAssociation(
    name="table151",
    ends={
        Property(name="Table152", type=sqlmodel_tables_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
identitySpecifier153: BinaryAssociation = BinaryAssociation(
    name="identitySpecifier153",
    ends={
        Property(name="IdentitySpecifier154", type=sqlmodel_tables_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_tables_Column", type=IdentitySpecifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints147: BinaryAssociation = BinaryAssociation(
    name="constraints147",
    ends={
        Property(name="TableConstraint", type=sqlmodel_tables_BaseTable, multiplicity=Multiplicity(1, 1)),
        Property(name="BaseTable148", type=TableConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generateExpression155: BinaryAssociation = BinaryAssociation(
    name="generateExpression155",
    ends={
        Property(name="ValueExpression", type=sqlmodel_tables_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_tables_Column156", type=ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencingForeignKeys149: BinaryAssociation = BinaryAssociation(
    name="referencingForeignKeys149",
    ends={
        Property(name="ForeignKey150", type=sqlmodel_tables_BaseTable, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedTable", type=ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
when166: BinaryAssociation = BinaryAssociation(
    name="when166",
    ends={
        Property(name="SearchCondition168", type=sqlmodel_tables_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_tables_Trigger167", type=SearchCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schema157: BinaryAssociation = BinaryAssociation(
    name="schema157",
    ends={
        Property(name="Schema158", type=sqlmodel_tables_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggers", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
subjectTable159: BinaryAssociation = BinaryAssociation(
    name="subjectTable159",
    ends={
        Property(name="Table161", type=sqlmodel_tables_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggers160", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
actionStatement162: BinaryAssociation = BinaryAssociation(
    name="actionStatement162",
    ends={
        Property(name="SQLStatement", type=sqlmodel_tables_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_tables_Trigger", type=SQLStatement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
triggerColumn163: BinaryAssociation = BinaryAssociation(
    name="triggerColumn163",
    ends={
        Property(name="Column165", type=sqlmodel_tables_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_tables_Trigger164", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
receivedPrivilege179: BinaryAssociation = BinaryAssociation(
    name="receivedPrivilege179",
    ends={
        Property(name="Privilege181", type=sqlmodel_accesscontrol_AuthorizationIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="grantee180", type=Privilege, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSchema169: BinaryAssociation = BinaryAssociation(
    name="ownedSchema169",
    ends={
        Property(name="Schema170", type=sqlmodel_accesscontrol_AuthorizationIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Schema, multiplicity=Multiplicity(0, 9999))
    }
)
Database171: BinaryAssociation = BinaryAssociation(
    name="Database171",
    ends={
        Property(name="Database172", type=sqlmodel_accesscontrol_AuthorizationIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="authorizationIds", type=Database, multiplicity=Multiplicity(1, 1))
    }
)
receivedRoleAuthorization173: BinaryAssociation = BinaryAssociation(
    name="receivedRoleAuthorization173",
    ends={
        Property(name="RoleAuthorization", type=sqlmodel_accesscontrol_AuthorizationIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="grantee", type=RoleAuthorization, multiplicity=Multiplicity(0, 9999))
    }
)
grantedRoleAuthorization174: BinaryAssociation = BinaryAssociation(
    name="grantedRoleAuthorization174",
    ends={
        Property(name="RoleAuthorization175", type=sqlmodel_accesscontrol_AuthorizationIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="grantor", type=RoleAuthorization, multiplicity=Multiplicity(0, 9999))
    }
)
grantedPrivilege176: BinaryAssociation = BinaryAssociation(
    name="grantedPrivilege176",
    ends={
        Property(name="Privilege178", type=sqlmodel_accesscontrol_AuthorizationIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="grantor177", type=Privilege, multiplicity=Multiplicity(0, 9999))
    }
)
object188: BinaryAssociation = BinaryAssociation(
    name="object188",
    ends={
        Property(name="SQLObject189", type=sqlmodel_accesscontrol_Privilege, multiplicity=Multiplicity(1, 1)),
        Property(name="privileges", type=SQLObject, multiplicity=Multiplicity(1, 1))
    }
)
grantor182: BinaryAssociation = BinaryAssociation(
    name="grantor182",
    ends={
        Property(name="AuthorizationIdentifier183", type=sqlmodel_accesscontrol_Privilege, multiplicity=Multiplicity(1, 1)),
        Property(name="grantedPrivilege", type=AuthorizationIdentifier, multiplicity=Multiplicity(1, 1))
    }
)
grantee184: BinaryAssociation = BinaryAssociation(
    name="grantee184",
    ends={
        Property(name="AuthorizationIdentifier185", type=sqlmodel_accesscontrol_Privilege, multiplicity=Multiplicity(1, 1)),
        Property(name="receivedPrivilege", type=AuthorizationIdentifier, multiplicity=Multiplicity(0, 1))
    }
)
actionObjects186: BinaryAssociation = BinaryAssociation(
    name="actionObjects186",
    ends={
        Property(name="SQLObject187", type=sqlmodel_accesscontrol_Privilege, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlmodel_accesscontrol_Privilege", type=SQLObject, multiplicity=Multiplicity(0, 9999))
    }
)
roleAuthorization192: BinaryAssociation = BinaryAssociation(
    name="roleAuthorization192",
    ends={
        Property(name="RoleAuthorization193", type=sqlmodel_accesscontrol_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="role", type=RoleAuthorization, multiplicity=Multiplicity(1, 9999))
    }
)
role194: BinaryAssociation = BinaryAssociation(
    name="role194",
    ends={
        Property(name="Role", type=sqlmodel_accesscontrol_RoleAuthorization, multiplicity=Multiplicity(1, 1)),
        Property(name="roleAuthorization", type=Role, multiplicity=Multiplicity(1, 1))
    }
)
grantee195: BinaryAssociation = BinaryAssociation(
    name="grantee195",
    ends={
        Property(name="AuthorizationIdentifier196", type=sqlmodel_accesscontrol_RoleAuthorization, multiplicity=Multiplicity(1, 1)),
        Property(name="receivedRoleAuthorization", type=AuthorizationIdentifier, multiplicity=Multiplicity(1, 1))
    }
)
user190: BinaryAssociation = BinaryAssociation(
    name="user190",
    ends={
        Property(name="User", type=sqlmodel_accesscontrol_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
grantor197: BinaryAssociation = BinaryAssociation(
    name="grantor197",
    ends={
        Property(name="AuthorizationIdentifier198", type=sqlmodel_accesscontrol_RoleAuthorization, multiplicity=Multiplicity(1, 1)),
        Property(name="grantedRoleAuthorization", type=AuthorizationIdentifier, multiplicity=Multiplicity(1, 1))
    }
)
group191: BinaryAssociation = BinaryAssociation(
    name="group191",
    ends={
        Property(name="Group", type=sqlmodel_accesscontrol_User, multiplicity=Multiplicity(1, 1)),
        Property(name="user", type=Group, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_sqlmodel_schema_IdentitySpecifier_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_schema_IdentitySpecifier)
gen_sqlmodel_schema_TypedElement_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_schema_TypedElement)
gen_sqlmodel_schema_Dependency_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_schema_Dependency)
gen_sqlmodel_schema_Schema_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_schema_Schema)
gen_sqlmodel_schema_SQLObject_ENamedElement = Generalization(general=ENamedElement, specific=sqlmodel_schema_SQLObject)
gen_sqlmodel_schema_Database_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_schema_Database)
gen_sqlmodel_schema_Sequence_TypedElement = Generalization(general=TypedElement, specific=sqlmodel_schema_Sequence)
gen_sqlmodel_schema_Event_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_schema_Event)
gen_sqlmodel_schema_Catalog_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_schema_Catalog)
gen_sqlmodel_constraints_Constraint_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_constraints_Constraint)
gen_sqlmodel_constraints_Assertion_Constraint = Generalization(general=Constraint, specific=sqlmodel_constraints_Assertion)
gen_sqlmodel_constraints_ReferenceConstraint_TableConstraint = Generalization(general=TableConstraint, specific=sqlmodel_constraints_ReferenceConstraint)
gen_sqlmodel_constraints_CheckConstraint_TableConstraint = Generalization(general=TableConstraint, specific=sqlmodel_constraints_CheckConstraint)
gen_sqlmodel_constraints_TableConstraint_Constraint = Generalization(general=Constraint, specific=sqlmodel_constraints_TableConstraint)
gen_sqlmodel_constraints_ForeignKey_ReferenceConstraint = Generalization(general=ReferenceConstraint, specific=sqlmodel_constraints_ForeignKey)
gen_sqlmodel_constraints_UniqueConstraint_ReferenceConstraint = Generalization(general=ReferenceConstraint, specific=sqlmodel_constraints_UniqueConstraint)
gen_sqlmodel_constraints_PrimaryKey_UniqueConstraint = Generalization(general=UniqueConstraint, specific=sqlmodel_constraints_PrimaryKey)
gen_sqlmodel_constraints_Index_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_constraints_Index)
gen_sqlmodel_constraints_IndexMember_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_constraints_IndexMember)
gen_sqlmodel_constraints_IndexExpression_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_constraints_IndexExpression)
gen_sqlmodel_datatypes_UserDefinedType_DataType = Generalization(general=DataType, specific=sqlmodel_datatypes_UserDefinedType)
gen_sqlmodel_datatypes_PredefinedDataType_SQLDataType = Generalization(general=SQLDataType, specific=sqlmodel_datatypes_PredefinedDataType)
gen_sqlmodel_datatypes_CollectionDataType_ConstructedDataType = Generalization(general=ConstructedDataType, specific=sqlmodel_datatypes_CollectionDataType)
gen_sqlmodel_datatypes_NumericalDataType_PredefinedDataType = Generalization(general=PredefinedDataType, specific=sqlmodel_datatypes_NumericalDataType)
gen_sqlmodel_datatypes_DataType_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_datatypes_DataType)
gen_sqlmodel_datatypes_RowDataType_ConstructedDataType = Generalization(general=ConstructedDataType, specific=sqlmodel_datatypes_RowDataType)
gen_sqlmodel_datatypes_CharacterStringDataType_PredefinedDataType = Generalization(general=PredefinedDataType, specific=sqlmodel_datatypes_CharacterStringDataType)
gen_sqlmodel_datatypes_ArrayDataType_CollectionDataType = Generalization(general=CollectionDataType, specific=sqlmodel_datatypes_ArrayDataType)
gen_sqlmodel_datatypes_MultisetDataType_CollectionDataType = Generalization(general=CollectionDataType, specific=sqlmodel_datatypes_MultisetDataType)
gen_sqlmodel_datatypes_IntervalDataType_PredefinedDataType = Generalization(general=PredefinedDataType, specific=sqlmodel_datatypes_IntervalDataType)
gen_sqlmodel_datatypes_BooleanDataType_PredefinedDataType = Generalization(general=PredefinedDataType, specific=sqlmodel_datatypes_BooleanDataType)
gen_sqlmodel_datatypes_BinaryStringDataType_PredefinedDataType = Generalization(general=PredefinedDataType, specific=sqlmodel_datatypes_BinaryStringDataType)
gen_sqlmodel_datatypes_CharacterSet_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_datatypes_CharacterSet)
gen_sqlmodel_datatypes_TimeDataType_PredefinedDataType = Generalization(general=PredefinedDataType, specific=sqlmodel_datatypes_TimeDataType)
gen_sqlmodel_datatypes_DistinctUserDefinedType_UserDefinedType = Generalization(general=UserDefinedType, specific=sqlmodel_datatypes_DistinctUserDefinedType)
gen_sqlmodel_datatypes_StructuredUserDefinedType_UserDefinedType = Generalization(general=UserDefinedType, specific=sqlmodel_datatypes_StructuredUserDefinedType)
gen_sqlmodel_datatypes_FixedPrecisionDataType_ExactNumericDataType = Generalization(general=ExactNumericDataType, specific=sqlmodel_datatypes_FixedPrecisionDataType)
gen_sqlmodel_datatypes_AttributeDefinition_TypedElement = Generalization(general=TypedElement, specific=sqlmodel_datatypes_AttributeDefinition)
gen_sqlmodel_datatypes_Field_TypedElement = Generalization(general=TypedElement, specific=sqlmodel_datatypes_Field)
gen_sqlmodel_datatypes_ReferenceDataType_ConstructedDataType = Generalization(general=ConstructedDataType, specific=sqlmodel_datatypes_ReferenceDataType)
gen_sqlmodel_datatypes_Domain_DistinctUserDefinedType = Generalization(general=DistinctUserDefinedType, specific=sqlmodel_datatypes_Domain)
gen_sqlmodel_datatypes_DataLinkDataType_PredefinedDataType = Generalization(general=PredefinedDataType, specific=sqlmodel_datatypes_DataLinkDataType)
gen_sqlmodel_datatypes_ConstructedDataType_DataType = Generalization(general=DataType, specific=sqlmodel_datatypes_ConstructedDataType)
gen_sqlmodel_datatypes_SQLDataType_DataType = Generalization(general=DataType, specific=sqlmodel_datatypes_SQLDataType)
gen_sqlmodel_datatypes_UserDefinedTypeOrdering_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_datatypes_UserDefinedTypeOrdering)
gen_sqlmodel_datatypes_ExactNumericDataType_NumericalDataType = Generalization(general=NumericalDataType, specific=sqlmodel_datatypes_ExactNumericDataType)
gen_sqlmodel_datatypes_ApproximateNumericDataType_NumericalDataType = Generalization(general=NumericalDataType, specific=sqlmodel_datatypes_ApproximateNumericDataType)
gen_sqlmodel_datatypes_IntegerDataType_ExactNumericDataType = Generalization(general=ExactNumericDataType, specific=sqlmodel_datatypes_IntegerDataType)
gen_sqlmodel_datatypes_XMLDataType_PredefinedDataType = Generalization(general=PredefinedDataType, specific=sqlmodel_datatypes_XMLDataType)
gen_sqlmodel_datatypes_ElementType_TypedElement = Generalization(general=TypedElement, specific=sqlmodel_datatypes_ElementType)
gen_sqlmodel_datatypes_DateDataType_PredefinedDataType = Generalization(general=PredefinedDataType, specific=sqlmodel_datatypes_DateDataType)
gen_sqlmodel_expressions_QueryExpressionDefault_schema_SQLObject = Generalization(general=schema_SQLObject, specific=sqlmodel_expressions_QueryExpressionDefault)
gen_sqlmodel_expressions_QueryExpressionDefault_expressions_QueryExpression = Generalization(general=expressions_QueryExpression, specific=sqlmodel_expressions_QueryExpressionDefault)
gen_sqlmodel_expressions_ValueExpressionDefault_schema_SQLObject = Generalization(general=schema_SQLObject, specific=sqlmodel_expressions_ValueExpressionDefault)
gen_sqlmodel_expressions_ValueExpressionDefault_expressions_ValueExpression = Generalization(general=expressions_ValueExpression, specific=sqlmodel_expressions_ValueExpressionDefault)
gen_sqlmodel_routines_Routine_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_routines_Routine)
gen_sqlmodel_expressions_SearchConditionDefault_schema_SQLObject = Generalization(general=schema_SQLObject, specific=sqlmodel_expressions_SearchConditionDefault)
gen_sqlmodel_expressions_SearchConditionDefault_expressions_SearchCondition = Generalization(general=expressions_SearchCondition, specific=sqlmodel_expressions_SearchConditionDefault)
gen_sqlmodel_routines_Source_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_routines_Source)
gen_sqlmodel_routines_Procedure_Routine = Generalization(general=Routine, specific=sqlmodel_routines_Procedure)
gen_sqlmodel_routines_Parameter_TypedElement = Generalization(general=TypedElement, specific=sqlmodel_routines_Parameter)
gen_sqlmodel_routines_Function_Routine = Generalization(general=Routine, specific=sqlmodel_routines_Function)
gen_sqlmodel_routines_RoutineResultTable_Table = Generalization(general=Table, specific=sqlmodel_routines_RoutineResultTable)
gen_sqlmodel_routines_Method_Function = Generalization(general=Function, specific=sqlmodel_routines_Method)
gen_sqlmodel_routines_BuiltInFunction_Function = Generalization(general=Function, specific=sqlmodel_routines_BuiltInFunction)
gen_sqlmodel_statements_SQLDataStatement_SQLStatement = Generalization(general=SQLStatement, specific=sqlmodel_statements_SQLDataStatement)
gen_sqlmodel_routines_UserDefinedFunction_Function = Generalization(general=Function, specific=sqlmodel_routines_UserDefinedFunction)
gen_sqlmodel_statements_SQLDataChangeStatement_SQLDataStatement = Generalization(general=SQLDataStatement, specific=sqlmodel_statements_SQLDataChangeStatement)
gen_sqlmodel_statements_SQLStatementDefault_schema_SQLObject = Generalization(general=schema_SQLObject, specific=sqlmodel_statements_SQLStatementDefault)
gen_sqlmodel_statements_SQLStatementDefault_statements_SQLStatement = Generalization(general=statements_SQLStatement, specific=sqlmodel_statements_SQLStatementDefault)
gen_sqlmodel_statements_SQLConnectionStatement_SQLStatement = Generalization(general=SQLStatement, specific=sqlmodel_statements_SQLConnectionStatement)
gen_sqlmodel_statements_SQLDiagnosticsStatement_SQLStatement = Generalization(general=SQLStatement, specific=sqlmodel_statements_SQLDiagnosticsStatement)
gen_sqlmodel_statements_SQLDynamicStatement_SQLStatement = Generalization(general=SQLStatement, specific=sqlmodel_statements_SQLDynamicStatement)
gen_sqlmodel_statements_SQLSchemaStatement_SQLStatement = Generalization(general=SQLStatement, specific=sqlmodel_statements_SQLSchemaStatement)
gen_sqlmodel_statements_SQLControlStatement_SQLStatement = Generalization(general=SQLStatement, specific=sqlmodel_statements_SQLControlStatement)
gen_sqlmodel_statements_SQLTransactionStatement_SQLStatement = Generalization(general=SQLStatement, specific=sqlmodel_statements_SQLTransactionStatement)
gen_sqlmodel_tables_ViewTable_DerivedTable = Generalization(general=DerivedTable, specific=sqlmodel_tables_ViewTable)
gen_sqlmodel_tables_TemporaryTable_BaseTable = Generalization(general=BaseTable, specific=sqlmodel_tables_TemporaryTable)
gen_sqlmodel_tables_Table_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_tables_Table)
gen_sqlmodel_statements_SQLSessionStatement_SQLStatement = Generalization(general=SQLStatement, specific=sqlmodel_statements_SQLSessionStatement)
gen_sqlmodel_tables_DerivedTable_Table = Generalization(general=Table, specific=sqlmodel_tables_DerivedTable)
gen_sqlmodel_tables_BaseTable_Table = Generalization(general=Table, specific=sqlmodel_tables_BaseTable)
gen_sqlmodel_tables_PersistentTable_BaseTable = Generalization(general=BaseTable, specific=sqlmodel_tables_PersistentTable)
gen_sqlmodel_tables_Column_TypedElement = Generalization(general=TypedElement, specific=sqlmodel_tables_Column)
gen_sqlmodel_tables_Trigger_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_tables_Trigger)
gen_sqlmodel_accesscontrol_AuthorizationIdentifier_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_accesscontrol_AuthorizationIdentifier)
gen_sqlmodel_accesscontrol_Privilege_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_accesscontrol_Privilege)
gen_sqlmodel_accesscontrol_Group_AuthorizationIdentifier = Generalization(general=AuthorizationIdentifier, specific=sqlmodel_accesscontrol_Group)
gen_sqlmodel_accesscontrol_RoleAuthorization_SQLObject = Generalization(general=SQLObject, specific=sqlmodel_accesscontrol_RoleAuthorization)
gen_sqlmodel_accesscontrol_User_AuthorizationIdentifier = Generalization(general=AuthorizationIdentifier, specific=sqlmodel_accesscontrol_User)
gen_sqlmodel_accesscontrol_Role_AuthorizationIdentifier = Generalization(general=AuthorizationIdentifier, specific=sqlmodel_accesscontrol_Role)

# Domain Model
domain_model = DomainModel(
    name="sqlmodel",
    types={sqlmodel_schema_IdentitySpecifier, SQLObject, SQLDataType, UserDefinedType, sqlmodel_schema_TypedElement, Index, Table, Sequence, Database, sqlmodel_schema_Dependency, schema_sqlmodel_EObject, sqlmodel_schema_Schema, Trigger, Routine, AuthorizationIdentifier, sqlmodel_schema_SQLObject, ENamedElement, Catalog, Assertion, CharacterSet, Dependency, Comment, ObjectExtension, Schema, sqlmodel_schema_Database, Privilege, sqlmodel_schema_Sequence, TypedElement, IdentitySpecifier, Event, sqlmodel_schema_Event, sqlmodel_schema_Catalog, sqlmodel_schema_ObjectExtension, sqlmodel_schema_Comment, BaseTable, sqlmodel_constraints_Constraint, sqlmodel_constraints_Assertion, Constraint, SearchCondition, sqlmodel_constraints_ReferenceConstraint, TableConstraint, Column, sqlmodel_constraints_CheckConstraint, sqlmodel_constraints_TableConstraint, sqlmodel_constraints_ForeignKey, ReferenceConstraint, UniqueConstraint, sqlmodel_constraints_UniqueConstraint, sqlmodel_constraints_PrimaryKey, sqlmodel_constraints_Index, ForeignKey, IndexMember, sqlmodel_constraints_IndexMember, sqlmodel_constraints_IndexExpression, sqlmodel_datatypes_UserDefinedType, DataType, UserDefinedTypeOrdering, IndexExpression, sqlmodel_datatypes_PredefinedDataType, sqlmodel_datatypes_CollectionDataType, ConstructedDataType, ElementType, sqlmodel_datatypes_NumericalDataType, PredefinedDataType, sqlmodel_datatypes_DataType, sqlmodel_datatypes_RowDataType, Field, sqlmodel_datatypes_CharacterStringDataType, sqlmodel_datatypes_ArrayDataType, CollectionDataType, sqlmodel_datatypes_MultisetDataType, sqlmodel_datatypes_IntervalDataType, sqlmodel_datatypes_BooleanDataType, sqlmodel_datatypes_BinaryStringDataType, sqlmodel_datatypes_CharacterSet, CharacterStringDataType, sqlmodel_datatypes_TimeDataType, sqlmodel_datatypes_DistinctUserDefinedType, sqlmodel_datatypes_StructuredUserDefinedType, AttributeDefinition, Method_, StructuredUserDefinedType, sqlmodel_datatypes_FixedPrecisionDataType, ExactNumericDataType, sqlmodel_datatypes_AttributeDefinition, sqlmodel_datatypes_Domain, sqlmodel_datatypes_Field, sqlmodel_datatypes_ReferenceDataType, DistinctUserDefinedType, CheckConstraint, sqlmodel_datatypes_DataLinkDataType, sqlmodel_datatypes_ConstructedDataType, sqlmodel_datatypes_SQLDataType, sqlmodel_datatypes_UserDefinedTypeOrdering, sqlmodel_datatypes_ExactNumericDataType, NumericalDataType, sqlmodel_datatypes_ApproximateNumericDataType, sqlmodel_datatypes_IntegerDataType, sqlmodel_datatypes_XMLDataType, sqlmodel_datatypes_ElementType, sqlmodel_datatypes_DateDataType, sqlmodel_expressions_ValueExpression, sqlmodel_expressions_SearchCondition, sqlmodel_expressions_QueryExpressionDefault, schema_SQLObject, expressions_QueryExpression, sqlmodel_expressions_QueryExpression, sqlmodel_expressions_ValueExpressionDefault, expressions_ValueExpression, sqlmodel_routines_Routine, sqlmodel_expressions_SearchConditionDefault, expressions_SearchCondition, Parameter_, Source, sqlmodel_routines_Source, sqlmodel_routines_Procedure, sqlmodel_routines_Parameter, sqlmodel_routines_Function, RoutineResultTable, sqlmodel_routines_RoutineResultTable, sqlmodel_routines_Method, Function, sqlmodel_routines_BuiltInFunction, sqlmodel_statements_SQLStatement, sqlmodel_statements_SQLDataStatement, SQLStatement, sqlmodel_statements_SQLSchemaStatement, sqlmodel_routines_UserDefinedFunction, sqlmodel_statements_SQLDataChangeStatement, SQLDataStatement, sqlmodel_statements_SQLStatementDefault, statements_SQLStatement, sqlmodel_statements_SQLConnectionStatement, sqlmodel_statements_SQLDiagnosticsStatement, sqlmodel_statements_SQLDynamicStatement, sqlmodel_statements_SQLControlStatement, sqlmodel_tables_ViewTable, DerivedTable, sqlmodel_tables_TemporaryTable, sqlmodel_tables_Table, sqlmodel_statements_SQLSessionStatement, sqlmodel_statements_SQLTransactionStatement, sqlmodel_tables_DerivedTable, QueryExpression, sqlmodel_tables_BaseTable, sqlmodel_tables_PersistentTable, sqlmodel_tables_Column, ValueExpression, sqlmodel_tables_Trigger, sqlmodel_accesscontrol_AuthorizationIdentifier, sqlmodel_accesscontrol_Privilege, RoleAuthorization, sqlmodel_accesscontrol_Group, sqlmodel_accesscontrol_RoleAuthorization, Role, User, sqlmodel_accesscontrol_User, Group, sqlmodel_accesscontrol_Role, GenerateType, ReferentialActionType, MatchType, IncrementType, CoercibilityType, IntervalQualifierType, OrderingType, OrderingCategoryType, PrimitiveType, WritePermissionOption, UnlinkOption, LinkControlOption, IntegrityControlOption, ReadPermissionOption, DataAccess, ParameterMode, CheckType, ReferenceType, ActionGranularityType, ActionTimeType},
    associations={containedType0, referencedType1, triggers4, indices5, tables6, sequences8, database10, targetEnd3, routines20, owner22, Catalog11, assertions13, userDefinedTypes15, charSets18, dependencies23, comments24, identity28, schema29, schemas31, extensions25, privileges27, authorizationIds38, events33, catalogs35, Database41, Database45, schemas47, SQLObject50, SQLObject43, searchCondition52, schema53, constrainedTables55, members59, BaseTable57, uniqueConstraint62, searchCondition60, uniqueIndex65, referencedTable68, referencedMembers63, ForeignKey70, members74, table75, ForeignKey77, includedMembers79, Schema72, schema86, column82, expression84, elementType89, ordering88, characterSet90, fields92, CharacterStringDataType93, schema95, predefinedRepresentation97, super98, sub99, attributes101, methods102, scopeTable105, referencedType107, constraint104, CollectionDataType112, orderingRoutine110, parameters114, source115, schema116, routine118, stringTypeOption120, returnTable123, resultSet122, returnScalar125, returnCast128, subtables135, schema137, columns131, udt139, queryExpression146, supertable133, triggers141, index143, table151, identitySpecifier153, constraints147, generateExpression155, referencingForeignKeys149, when166, schema157, subjectTable159, actionStatement162, triggerColumn163, receivedPrivilege179, ownedSchema169, Database171, receivedRoleAuthorization173, grantedRoleAuthorization174, grantedPrivilege176, object188, grantor182, grantee184, actionObjects186, roleAuthorization192, role194, grantee195, user190, grantor197, group191},
    generalizations={gen_sqlmodel_schema_IdentitySpecifier_SQLObject, gen_sqlmodel_schema_TypedElement_SQLObject, gen_sqlmodel_schema_Dependency_SQLObject, gen_sqlmodel_schema_Schema_SQLObject, gen_sqlmodel_schema_SQLObject_ENamedElement, gen_sqlmodel_schema_Database_SQLObject, gen_sqlmodel_schema_Sequence_TypedElement, gen_sqlmodel_schema_Event_SQLObject, gen_sqlmodel_schema_Catalog_SQLObject, gen_sqlmodel_constraints_Constraint_SQLObject, gen_sqlmodel_constraints_Assertion_Constraint, gen_sqlmodel_constraints_ReferenceConstraint_TableConstraint, gen_sqlmodel_constraints_CheckConstraint_TableConstraint, gen_sqlmodel_constraints_TableConstraint_Constraint, gen_sqlmodel_constraints_ForeignKey_ReferenceConstraint, gen_sqlmodel_constraints_UniqueConstraint_ReferenceConstraint, gen_sqlmodel_constraints_PrimaryKey_UniqueConstraint, gen_sqlmodel_constraints_Index_SQLObject, gen_sqlmodel_constraints_IndexMember_SQLObject, gen_sqlmodel_constraints_IndexExpression_SQLObject, gen_sqlmodel_datatypes_UserDefinedType_DataType, gen_sqlmodel_datatypes_PredefinedDataType_SQLDataType, gen_sqlmodel_datatypes_CollectionDataType_ConstructedDataType, gen_sqlmodel_datatypes_NumericalDataType_PredefinedDataType, gen_sqlmodel_datatypes_DataType_SQLObject, gen_sqlmodel_datatypes_RowDataType_ConstructedDataType, gen_sqlmodel_datatypes_CharacterStringDataType_PredefinedDataType, gen_sqlmodel_datatypes_ArrayDataType_CollectionDataType, gen_sqlmodel_datatypes_MultisetDataType_CollectionDataType, gen_sqlmodel_datatypes_IntervalDataType_PredefinedDataType, gen_sqlmodel_datatypes_BooleanDataType_PredefinedDataType, gen_sqlmodel_datatypes_BinaryStringDataType_PredefinedDataType, gen_sqlmodel_datatypes_CharacterSet_SQLObject, gen_sqlmodel_datatypes_TimeDataType_PredefinedDataType, gen_sqlmodel_datatypes_DistinctUserDefinedType_UserDefinedType, gen_sqlmodel_datatypes_StructuredUserDefinedType_UserDefinedType, gen_sqlmodel_datatypes_FixedPrecisionDataType_ExactNumericDataType, gen_sqlmodel_datatypes_AttributeDefinition_TypedElement, gen_sqlmodel_datatypes_Field_TypedElement, gen_sqlmodel_datatypes_ReferenceDataType_ConstructedDataType, gen_sqlmodel_datatypes_Domain_DistinctUserDefinedType, gen_sqlmodel_datatypes_DataLinkDataType_PredefinedDataType, gen_sqlmodel_datatypes_ConstructedDataType_DataType, gen_sqlmodel_datatypes_SQLDataType_DataType, gen_sqlmodel_datatypes_UserDefinedTypeOrdering_SQLObject, gen_sqlmodel_datatypes_ExactNumericDataType_NumericalDataType, gen_sqlmodel_datatypes_ApproximateNumericDataType_NumericalDataType, gen_sqlmodel_datatypes_IntegerDataType_ExactNumericDataType, gen_sqlmodel_datatypes_XMLDataType_PredefinedDataType, gen_sqlmodel_datatypes_ElementType_TypedElement, gen_sqlmodel_datatypes_DateDataType_PredefinedDataType, gen_sqlmodel_expressions_QueryExpressionDefault_schema_SQLObject, gen_sqlmodel_expressions_QueryExpressionDefault_expressions_QueryExpression, gen_sqlmodel_expressions_ValueExpressionDefault_schema_SQLObject, gen_sqlmodel_expressions_ValueExpressionDefault_expressions_ValueExpression, gen_sqlmodel_routines_Routine_SQLObject, gen_sqlmodel_expressions_SearchConditionDefault_schema_SQLObject, gen_sqlmodel_expressions_SearchConditionDefault_expressions_SearchCondition, gen_sqlmodel_routines_Source_SQLObject, gen_sqlmodel_routines_Procedure_Routine, gen_sqlmodel_routines_Parameter_TypedElement, gen_sqlmodel_routines_Function_Routine, gen_sqlmodel_routines_RoutineResultTable_Table, gen_sqlmodel_routines_Method_Function, gen_sqlmodel_routines_BuiltInFunction_Function, gen_sqlmodel_statements_SQLDataStatement_SQLStatement, gen_sqlmodel_routines_UserDefinedFunction_Function, gen_sqlmodel_statements_SQLDataChangeStatement_SQLDataStatement, gen_sqlmodel_statements_SQLStatementDefault_schema_SQLObject, gen_sqlmodel_statements_SQLStatementDefault_statements_SQLStatement, gen_sqlmodel_statements_SQLConnectionStatement_SQLStatement, gen_sqlmodel_statements_SQLDiagnosticsStatement_SQLStatement, gen_sqlmodel_statements_SQLDynamicStatement_SQLStatement, gen_sqlmodel_statements_SQLSchemaStatement_SQLStatement, gen_sqlmodel_statements_SQLControlStatement_SQLStatement, gen_sqlmodel_statements_SQLTransactionStatement_SQLStatement, gen_sqlmodel_tables_ViewTable_DerivedTable, gen_sqlmodel_tables_TemporaryTable_BaseTable, gen_sqlmodel_tables_Table_SQLObject, gen_sqlmodel_statements_SQLSessionStatement_SQLStatement, gen_sqlmodel_tables_DerivedTable_Table, gen_sqlmodel_tables_BaseTable_Table, gen_sqlmodel_tables_PersistentTable_BaseTable, gen_sqlmodel_tables_Column_TypedElement, gen_sqlmodel_tables_Trigger_SQLObject, gen_sqlmodel_accesscontrol_AuthorizationIdentifier_SQLObject, gen_sqlmodel_accesscontrol_Privilege_SQLObject, gen_sqlmodel_accesscontrol_Group_AuthorizationIdentifier, gen_sqlmodel_accesscontrol_RoleAuthorization_SQLObject, gen_sqlmodel_accesscontrol_User_AuthorizationIdentifier, gen_sqlmodel_accesscontrol_Role_AuthorizationIdentifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)