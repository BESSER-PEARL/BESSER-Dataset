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
CrudOperationType: Enumeration = Enumeration(
    name="CrudOperationType",
    literals={
            EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="CREATE"),
			EnumerationLiteral(name="READ"),
			EnumerationLiteral(name="UPDATE"),
			EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="ALL")
    }
)

DataBaseConstraintType: Enumeration = Enumeration(
    name="DataBaseConstraintType",
    literals={
            EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="INDEX"),
			EnumerationLiteral(name="UNIQUE"),
			EnumerationLiteral(name="NATURAL"),
			EnumerationLiteral(name="PRIMARY")
    }
)

# Classes
dom_ComplexType = Class(name="dom::ComplexType", is_abstract=True)
ModelElement = Class(name="ModelElement")
Type = Class(name="Type")
dom_Attribute = Class(name="dom::Attribute")
DaoOperation = Class(name="DaoOperation")
dom_Parameter = Class(name="dom::Parameter")
dom_Service = Class(name="dom::Service")
Dependant = Class(name="Dependant")
dom_Dependant = Class(name="dom::Dependant", is_abstract=True)
dom_Operation = Class(name="dom::Operation")
dom_DelegateOperation = Class(name="dom::DelegateOperation")
dom_Property = Class(name="dom::Property")
ReferenceableByXmadslVariable = Class(name="ReferenceableByXmadslVariable")
IDocumentable = Class(name="IDocumentable")
dom_SimpleType = Class(name="dom::SimpleType")
dom_DaoOperation = Class(name="dom::DaoOperation")
QueryParameter = Class(name="QueryParameter")
QueryParameterReference = Class(name="QueryParameterReference")
dom_Type = Class(name="dom::Type")
dom_DataView = Class(name="dom::DataView")
dom_Dao = Class(name="dom::Dao")
dom_Expression = Class(name="dom::Expression")
dom_ValueObject = Class(name="dom::ValueObject")
ComplexType = Class(name="ComplexType")
dom_FeatureReference = Class(name="dom::FeatureReference")
PresentableFeature = Class(name="PresentableFeature")
dom_Entity = Class(name="dom::Entity")
dom_AttributeProperty = Class(name="dom::AttributeProperty")
dom_Mapper = Class(name="dom::Mapper")
dom_PropertyMapping = Class(name="dom::PropertyMapping")
dom_AttributeGroup = Class(name="dom::AttributeGroup")
dom_ConditionsBlock = Class(name="dom::ConditionsBlock")
dom_DataTypeAndTypeParameter = Class(name="dom::DataTypeAndTypeParameter")
dom_IncrementerReference = Class(name="dom::IncrementerReference")
dom_AttributeFlag = Class(name="dom::AttributeFlag")
AttributeProperty = Class(name="AttributeProperty")
dom_AvailableFlag = Class(name="dom::AvailableFlag")
dom_DerivedFlag = Class(name="dom::DerivedFlag")
dom_BoolLiteral = Class(name="dom::BoolLiteral")
dom_ExpressionFlag = Class(name="dom::ExpressionFlag")
AttributeFlag = Class(name="AttributeFlag")
dom_EqualityExpr = Class(name="dom::EqualityExpr")
dom_RequiredFlag = Class(name="dom::RequiredFlag")
ExpressionFlag = Class(name="ExpressionFlag")
dom_ReadOnlyFlag = Class(name="dom::ReadOnlyFlag")
dom_AttributeSortOrder = Class(name="dom::AttributeSortOrder")
dom_TransientFlag = Class(name="dom::TransientFlag")
dom_AttributeValidationProperty = Class(name="dom::AttributeValidationProperty")
dom_Constraint = Class(name="dom::Constraint")
dom_ValidatorReference = Class(name="dom::ValidatorReference")
dom_AttributeTextProperty = Class(name="dom::AttributeTextProperty")
dom_DaoFeature = Class(name="dom::DaoFeature", is_abstract=True)
dom_QueryOperation = Class(name="dom::QueryOperation")
dom_DataBaseConstraint = Class(name="dom::DataBaseConstraint")
dom_Column = Class(name="dom::Column")
dom_ManyToOne = Class(name="dom::ManyToOne")
dom_OneToOne = Class(name="dom::OneToOne")
dom_OneToMany = Class(name="dom::OneToMany")
dom_ManyToMany = Class(name="dom::ManyToMany")
dom_QueryParameter = Class(name="dom::QueryParameter")
dom_QlStatement = Class(name="dom::QlStatement")
DaoFeature = Class(name="DaoFeature")
dom_SqlType = Class(name="dom::SqlType")
dom_ApplicationSession = Class(name="dom::ApplicationSession")
dom_Function = Class(name="dom::Function")
dom_InsertStatement = Class(name="dom::InsertStatement")
dom_CallableStatement = Class(name="dom::CallableStatement")
QlStatement = Class(name="QlStatement")
dom_CallInputParameter = Class(name="dom::CallInputParameter")
dom_CallOutputParameter = Class(name="dom::CallOutputParameter")
dom_PropertyAssignment = Class(name="dom::PropertyAssignment")
dom_SelectStatement = Class(name="dom::SelectStatement")
dom_DeleteStatement = Class(name="dom::DeleteStatement")
dom_UpdateStatement = Class(name="dom::UpdateStatement")
dom_SortOrderElement = Class(name="dom::SortOrderElement")
dom_PropertyValue = Class(name="dom::PropertyValue")
dom_FromRange = Class(name="dom::FromRange")
dom_Join = Class(name="dom::Join")
dom_InClass = Class(name="dom::InClass")
dom_InCollection = Class(name="dom::InCollection")
dom_SelectProperties = Class(name="dom::SelectProperties")
SelectStatement = Class(name="SelectStatement")
dom_SelectClass = Class(name="dom::SelectClass")
dom_SelectObject = Class(name="dom::SelectObject")
dom_FromClass = Class(name="dom::FromClass")
FromRange = Class(name="FromRange")
JoinEntity = Class(name="JoinEntity")
Expression = Class(name="Expression")
dom_InCollectionElements = Class(name="dom::InCollectionElements")
dom_JoinEntity = Class(name="dom::JoinEntity")
dom_FunctionCall = Class(name="dom::FunctionCall")
dom_TrimFunction = Class(name="dom::TrimFunction")
dom_StringLiteralValue = Class(name="dom::StringLiteralValue")
dom_CastFunction = Class(name="dom::CastFunction")
dom_CaseExpression = Class(name="dom::CaseExpression")
dom_AggregateFunction = Class(name="dom::AggregateFunction")
dom_WhenClause = Class(name="dom::WhenClause")
dom_CollectionFunction = Class(name="dom::CollectionFunction")
dom_QueryParameterReference = Class(name="dom::QueryParameterReference")
dom_QueryParameterValue = Class(name="dom::QueryParameterValue")
dom_QuantifiedExpression = Class(name="dom::QuantifiedExpression")
dom_AltWhenClause = Class(name="dom::AltWhenClause")
dom_BooleanLiteralValue = Class(name="dom::BooleanLiteralValue")
dom_NullLiteralValue = Class(name="dom::NullLiteralValue")
dom_EmptyLiteralValue = Class(name="dom::EmptyLiteralValue")
dom_IElementWithNoName = Class(name="dom::IElementWithNoName")
dom_SubQuery = Class(name="dom::SubQuery")
dom_ParenthesizedExpression = Class(name="dom::ParenthesizedExpression")
dom_LiteralValue = Class(name="dom::LiteralValue")
LiteralValue = Class(name="LiteralValue")
dom_IntegerLiteralValue = Class(name="dom::IntegerLiteralValue")
dom_RealLiteralValue = Class(name="dom::RealLiteralValue")
dom_NotExpression = Class(name="dom::NotExpression")
dom_InExpression = Class(name="dom::InExpression")
dom_PresentableFeature = Class(name="dom::PresentableFeature", is_abstract=True)
dom_AliasedExpression = Class(name="dom::AliasedExpression")
dom_BinaryExpression = Class(name="dom::BinaryExpression")
dom_LikeExpression = Class(name="dom::LikeExpression")
dom_BetweenExpression = Class(name="dom::BetweenExpression")
dom_MemberOfExpression = Class(name="dom::MemberOfExpression")
dom_UnaryExpression = Class(name="dom::UnaryExpression")

# dom_ComplexType class attributes and methods

# ModelElement class attributes and methods

# Type class attributes and methods

# dom_Attribute class attributes and methods
dom_Attribute_identifier: Property = Property(name="identifier", type=BooleanType)
dom_Attribute_version: Property = Property(name="version", type=BooleanType)
dom_Attribute_composition: Property = Property(name="composition", type=BooleanType)
dom_Attribute_many: Property = Property(name="many", type=BooleanType)
dom_Attribute_defaultValue: Property = Property(name="defaultValue", type=StringType)
dom_Attribute_dataTypeName: Property = Property(name="dataTypeName", type=StringType)
dom_Attribute_reference: Property = Property(name="reference", type=BooleanType)
dom_Attribute_readOnly: Property = Property(name="readOnly", type=BooleanType)
dom_Attribute_required: Property = Property(name="required", type=BooleanType)
dom_Attribute_derived: Property = Property(name="derived", type=BooleanType)
dom_Attribute_transient: Property = Property(name="transient", type=BooleanType)
dom_Attribute.attributes={dom_Attribute_identifier, dom_Attribute_composition, dom_Attribute_defaultValue, dom_Attribute_version, dom_Attribute_dataTypeName, dom_Attribute_derived, dom_Attribute_many, dom_Attribute_reference, dom_Attribute_required, dom_Attribute_transient, dom_Attribute_readOnly}

# DaoOperation class attributes and methods

# dom_Parameter class attributes and methods
dom_Parameter_many: Property = Property(name="many", type=BooleanType)
dom_Parameter_name: Property = Property(name="name", type=StringType)
dom_Parameter.attributes={dom_Parameter_name, dom_Parameter_many}

# dom_Service class attributes and methods

# Dependant class attributes and methods

# dom_Dependant class attributes and methods

# dom_Operation class attributes and methods
dom_Operation_expression: Property = Property(name="expression", type=StringType)
dom_Operation.attributes={dom_Operation_expression}

# dom_DelegateOperation class attributes and methods
dom_DelegateOperation_crudOperationType: Property = Property(name="crudOperationType", type=StringType)
dom_DelegateOperation_many: Property = Property(name="many", type=BooleanType)
dom_DelegateOperation_name: Property = Property(name="name", type=StringType)
dom_DelegateOperation.attributes={dom_DelegateOperation_many, dom_DelegateOperation_name, dom_DelegateOperation_crudOperationType}

# dom_Property class attributes and methods
dom_Property_name: Property = Property(name="name", type=StringType)
dom_Property_defaultValue: Property = Property(name="defaultValue", type=StringType)
dom_Property.attributes={dom_Property_name, dom_Property_defaultValue}

# ReferenceableByXmadslVariable class attributes and methods

# IDocumentable class attributes and methods

# dom_SimpleType class attributes and methods

# dom_DaoOperation class attributes and methods
dom_DaoOperation_many: Property = Property(name="many", type=BooleanType)
dom_DaoOperation_name: Property = Property(name="name", type=StringType)
dom_DaoOperation.attributes={dom_DaoOperation_name, dom_DaoOperation_many}

# QueryParameter class attributes and methods

# QueryParameterReference class attributes and methods

# dom_Type class attributes and methods

# dom_DataView class attributes and methods

# dom_Dao class attributes and methods
dom_Dao_discriminator: Property = Property(name="discriminator", type=StringType)
dom_Dao_qualifier: Property = Property(name="qualifier", type=StringType)
dom_Dao_tableName: Property = Property(name="tableName", type=StringType)
dom_Dao.attributes={dom_Dao_tableName, dom_Dao_qualifier, dom_Dao_discriminator}

# dom_Expression class attributes and methods

# dom_ValueObject class attributes and methods

# ComplexType class attributes and methods

# dom_FeatureReference class attributes and methods
dom_FeatureReference_all: Property = Property(name="all", type=BooleanType)
dom_FeatureReference.attributes={dom_FeatureReference_all}

# PresentableFeature class attributes and methods

# dom_Entity class attributes and methods

# dom_AttributeProperty class attributes and methods

# dom_Mapper class attributes and methods
dom_Mapper_biDirectional: Property = Property(name="biDirectional", type=BooleanType)
dom_Mapper_toLeft: Property = Property(name="toLeft", type=BooleanType)
dom_Mapper_toRight: Property = Property(name="toRight", type=BooleanType)
dom_Mapper.attributes={dom_Mapper_toRight, dom_Mapper_toLeft, dom_Mapper_biDirectional}

# dom_PropertyMapping class attributes and methods
dom_PropertyMapping_biDirectional: Property = Property(name="biDirectional", type=BooleanType)
dom_PropertyMapping_toLeft: Property = Property(name="toLeft", type=BooleanType)
dom_PropertyMapping_toRight: Property = Property(name="toRight", type=BooleanType)
dom_PropertyMapping.attributes={dom_PropertyMapping_toLeft, dom_PropertyMapping_toRight, dom_PropertyMapping_biDirectional}

# dom_AttributeGroup class attributes and methods
dom_AttributeGroup_key: Property = Property(name="key", type=BooleanType)
dom_AttributeGroup_unique: Property = Property(name="unique", type=BooleanType)
dom_AttributeGroup_filter: Property = Property(name="filter", type=BooleanType)
dom_AttributeGroup_sortorder: Property = Property(name="sortorder", type=BooleanType)
dom_AttributeGroup_name: Property = Property(name="name", type=StringType)
dom_AttributeGroup.attributes={dom_AttributeGroup_sortorder, dom_AttributeGroup_unique, dom_AttributeGroup_filter, dom_AttributeGroup_key, dom_AttributeGroup_name}

# dom_ConditionsBlock class attributes and methods

# dom_DataTypeAndTypeParameter class attributes and methods

# dom_IncrementerReference class attributes and methods

# dom_AttributeFlag class attributes and methods

# AttributeProperty class attributes and methods

# dom_AvailableFlag class attributes and methods

# dom_DerivedFlag class attributes and methods

# dom_BoolLiteral class attributes and methods

# dom_ExpressionFlag class attributes and methods

# AttributeFlag class attributes and methods

# dom_EqualityExpr class attributes and methods

# dom_RequiredFlag class attributes and methods

# ExpressionFlag class attributes and methods

# dom_ReadOnlyFlag class attributes and methods

# dom_AttributeSortOrder class attributes and methods
dom_AttributeSortOrder_asc: Property = Property(name="asc", type=BooleanType)
dom_AttributeSortOrder_desc: Property = Property(name="desc", type=BooleanType)
dom_AttributeSortOrder.attributes={dom_AttributeSortOrder_asc, dom_AttributeSortOrder_desc}

# dom_TransientFlag class attributes and methods

# dom_AttributeValidationProperty class attributes and methods

# dom_Constraint class attributes and methods

# dom_ValidatorReference class attributes and methods

# dom_AttributeTextProperty class attributes and methods
dom_AttributeTextProperty_labelText: Property = Property(name="labelText", type=StringType)
dom_AttributeTextProperty_tooltipText: Property = Property(name="tooltipText", type=StringType)
dom_AttributeTextProperty_unitText: Property = Property(name="unitText", type=StringType)
dom_AttributeTextProperty_hstoreColumn: Property = Property(name="hstoreColumn", type=StringType)
dom_AttributeTextProperty.attributes={dom_AttributeTextProperty_hstoreColumn, dom_AttributeTextProperty_labelText, dom_AttributeTextProperty_unitText, dom_AttributeTextProperty_tooltipText}

# dom_DaoFeature class attributes and methods

# dom_QueryOperation class attributes and methods

# dom_DataBaseConstraint class attributes and methods
dom_DataBaseConstraint_type: Property = Property(name="type", type=StringType)
dom_DataBaseConstraint_name: Property = Property(name="name", type=StringType)
dom_DataBaseConstraint.attributes={dom_DataBaseConstraint_name, dom_DataBaseConstraint_type}

# dom_Column class attributes and methods
dom_Column_columnName: Property = Property(name="columnName", type=StringType)
dom_Column.attributes={dom_Column_columnName}

# dom_ManyToOne class attributes and methods
dom_ManyToOne_columnName: Property = Property(name="columnName", type=StringType)
dom_ManyToOne_derived: Property = Property(name="derived", type=BooleanType)
dom_ManyToOne.attributes={dom_ManyToOne_derived, dom_ManyToOne_columnName}

# dom_OneToOne class attributes and methods

# dom_OneToMany class attributes and methods
dom_OneToMany_columnName: Property = Property(name="columnName", type=StringType)
dom_OneToMany.attributes={dom_OneToMany_columnName}

# dom_ManyToMany class attributes and methods
dom_ManyToMany_tableName: Property = Property(name="tableName", type=StringType)
dom_ManyToMany_columnName: Property = Property(name="columnName", type=StringType)
dom_ManyToMany_inverse: Property = Property(name="inverse", type=BooleanType)
dom_ManyToMany.attributes={dom_ManyToMany_inverse, dom_ManyToMany_tableName, dom_ManyToMany_columnName}

# dom_QueryParameter class attributes and methods

# dom_QlStatement class attributes and methods

# DaoFeature class attributes and methods

# dom_SqlType class attributes and methods

# dom_ApplicationSession class attributes and methods

# dom_Function class attributes and methods

# dom_InsertStatement class attributes and methods

# dom_CallableStatement class attributes and methods
dom_CallableStatement_functionCall: Property = Property(name="functionCall", type=BooleanType)
dom_CallableStatement_name: Property = Property(name="name", type=StringType)
dom_CallableStatement.attributes={dom_CallableStatement_name, dom_CallableStatement_functionCall}

# QlStatement class attributes and methods

# dom_CallInputParameter class attributes and methods
dom_CallInputParameter_name: Property = Property(name="name", type=StringType)
dom_CallInputParameter.attributes={dom_CallInputParameter_name}

# dom_CallOutputParameter class attributes and methods
dom_CallOutputParameter_name: Property = Property(name="name", type=StringType)
dom_CallOutputParameter.attributes={dom_CallOutputParameter_name}

# dom_PropertyAssignment class attributes and methods

# dom_SelectStatement class attributes and methods

# dom_DeleteStatement class attributes and methods
dom_DeleteStatement_name: Property = Property(name="name", type=StringType)
dom_DeleteStatement.attributes={dom_DeleteStatement_name}

# dom_UpdateStatement class attributes and methods
dom_UpdateStatement_name: Property = Property(name="name", type=StringType)
dom_UpdateStatement_versioned: Property = Property(name="versioned", type=BooleanType)
dom_UpdateStatement.attributes={dom_UpdateStatement_versioned, dom_UpdateStatement_name}

# dom_SortOrderElement class attributes and methods
dom_SortOrderElement_sortOrder: Property = Property(name="sortOrder", type=StringType)
dom_SortOrderElement.attributes={dom_SortOrderElement_sortOrder}

# dom_PropertyValue class attributes and methods
dom_PropertyValue_name: Property = Property(name="name", type=StringType)
dom_PropertyValue_segments: Property = Property(name="segments", type=StringType)
dom_PropertyValue_classProperty: Property = Property(name="classProperty", type=BooleanType)
dom_PropertyValue.attributes={dom_PropertyValue_segments, dom_PropertyValue_classProperty, dom_PropertyValue_name}

# dom_FromRange class attributes and methods

# dom_Join class attributes and methods
dom_Join_type: Property = Property(name="type", type=StringType)
dom_Join_fetch: Property = Property(name="fetch", type=BooleanType)
dom_Join_propertyFetch: Property = Property(name="propertyFetch", type=BooleanType)
dom_Join.attributes={dom_Join_type, dom_Join_fetch, dom_Join_propertyFetch}

# dom_InClass class attributes and methods
dom_InClass_name: Property = Property(name="name", type=StringType)
dom_InClass_class: Property = Property(name="class", type=StringType)
dom_InClass.attributes={dom_InClass_name, dom_InClass_class}

# dom_InCollection class attributes and methods
dom_InCollection_path: Property = Property(name="path", type=StringType)
dom_InCollection_alias: Property = Property(name="alias", type=StringType)
dom_InCollection.attributes={dom_InCollection_alias, dom_InCollection_path}

# dom_SelectProperties class attributes and methods
dom_SelectProperties_distinct: Property = Property(name="distinct", type=BooleanType)
dom_SelectProperties.attributes={dom_SelectProperties_distinct}

# SelectStatement class attributes and methods

# dom_SelectClass class attributes and methods
dom_SelectClass_class: Property = Property(name="class", type=StringType)
dom_SelectClass.attributes={dom_SelectClass_class}

# dom_SelectObject class attributes and methods
dom_SelectObject_name: Property = Property(name="name", type=StringType)
dom_SelectObject.attributes={dom_SelectObject_name}

# dom_FromClass class attributes and methods
dom_FromClass_popertyFetch: Property = Property(name="popertyFetch", type=BooleanType)
dom_FromClass.attributes={dom_FromClass_popertyFetch}

# FromRange class attributes and methods

# JoinEntity class attributes and methods

# Expression class attributes and methods

# dom_InCollectionElements class attributes and methods
dom_InCollectionElements_name: Property = Property(name="name", type=StringType)
dom_InCollectionElements_reference: Property = Property(name="reference", type=StringType)
dom_InCollectionElements.attributes={dom_InCollectionElements_reference, dom_InCollectionElements_name}

# dom_JoinEntity class attributes and methods
dom_JoinEntity_name: Property = Property(name="name", type=StringType)
dom_JoinEntity.attributes={dom_JoinEntity_name}

# dom_FunctionCall class attributes and methods
dom_FunctionCall_function: Property = Property(name="function", type=StringType)
dom_FunctionCall.attributes={dom_FunctionCall_function}

# dom_TrimFunction class attributes and methods
dom_TrimFunction_function: Property = Property(name="function", type=StringType)
dom_TrimFunction_mode: Property = Property(name="mode", type=StringType)
dom_TrimFunction.attributes={dom_TrimFunction_mode, dom_TrimFunction_function}

# dom_StringLiteralValue class attributes and methods
dom_StringLiteralValue_value: Property = Property(name="value", type=StringType)
dom_StringLiteralValue.attributes={dom_StringLiteralValue_value}

# dom_CastFunction class attributes and methods
dom_CastFunction_function: Property = Property(name="function", type=StringType)
dom_CastFunction_name: Property = Property(name="name", type=StringType)
dom_CastFunction.attributes={dom_CastFunction_function, dom_CastFunction_name}

# dom_CaseExpression class attributes and methods

# dom_AggregateFunction class attributes and methods
dom_AggregateFunction_function: Property = Property(name="function", type=StringType)
dom_AggregateFunction_all: Property = Property(name="all", type=BooleanType)
dom_AggregateFunction_distinct: Property = Property(name="distinct", type=BooleanType)
dom_AggregateFunction_from: Property = Property(name="from", type=StringType)
dom_AggregateFunction.attributes={dom_AggregateFunction_all, dom_AggregateFunction_distinct, dom_AggregateFunction_function, dom_AggregateFunction_from}

# dom_WhenClause class attributes and methods

# dom_CollectionFunction class attributes and methods
dom_CollectionFunction_function: Property = Property(name="function", type=StringType)
dom_CollectionFunction.attributes={dom_CollectionFunction_function}

# dom_QueryParameterReference class attributes and methods

# dom_QueryParameterValue class attributes and methods

# dom_QuantifiedExpression class attributes and methods
dom_QuantifiedExpression_quantifier: Property = Property(name="quantifier", type=StringType)
dom_QuantifiedExpression_name: Property = Property(name="name", type=StringType)
dom_QuantifiedExpression.attributes={dom_QuantifiedExpression_name, dom_QuantifiedExpression_quantifier}

# dom_AltWhenClause class attributes and methods

# dom_BooleanLiteralValue class attributes and methods
dom_BooleanLiteralValue_isTrue: Property = Property(name="isTrue", type=BooleanType)
dom_BooleanLiteralValue.attributes={dom_BooleanLiteralValue_isTrue}

# dom_NullLiteralValue class attributes and methods

# dom_EmptyLiteralValue class attributes and methods

# dom_IElementWithNoName class attributes and methods
dom_IElementWithNoName_noName: Property = Property(name="noName", type=StringType)
dom_IElementWithNoName.attributes={dom_IElementWithNoName_noName}

# dom_SubQuery class attributes and methods

# dom_ParenthesizedExpression class attributes and methods

# dom_LiteralValue class attributes and methods

# LiteralValue class attributes and methods

# dom_IntegerLiteralValue class attributes and methods
dom_IntegerLiteralValue_value: Property = Property(name="value", type=StringType)
dom_IntegerLiteralValue.attributes={dom_IntegerLiteralValue_value}

# dom_RealLiteralValue class attributes and methods
dom_RealLiteralValue_value: Property = Property(name="value", type=StringType)
dom_RealLiteralValue.attributes={dom_RealLiteralValue_value}

# dom_NotExpression class attributes and methods

# dom_InExpression class attributes and methods
dom_InExpression_not: Property = Property(name="not", type=BooleanType)
dom_InExpression_operator: Property = Property(name="operator", type=StringType)
dom_InExpression.attributes={dom_InExpression_operator, dom_InExpression_not}

# dom_PresentableFeature class attributes and methods
dom_PresentableFeature_name: Property = Property(name="name", type=StringType)
dom_PresentableFeature.attributes={dom_PresentableFeature_name}

# dom_AliasedExpression class attributes and methods
dom_AliasedExpression_name: Property = Property(name="name", type=StringType)
dom_AliasedExpression.attributes={dom_AliasedExpression_name}

# dom_BinaryExpression class attributes and methods
dom_BinaryExpression_operator: Property = Property(name="operator", type=StringType)
dom_BinaryExpression.attributes={dom_BinaryExpression_operator}

# dom_LikeExpression class attributes and methods
dom_LikeExpression_not: Property = Property(name="not", type=BooleanType)
dom_LikeExpression_operator: Property = Property(name="operator", type=StringType)
dom_LikeExpression.attributes={dom_LikeExpression_not, dom_LikeExpression_operator}

# dom_BetweenExpression class attributes and methods
dom_BetweenExpression_not: Property = Property(name="not", type=BooleanType)
dom_BetweenExpression_operator: Property = Property(name="operator", type=StringType)
dom_BetweenExpression.attributes={dom_BetweenExpression_not, dom_BetweenExpression_operator}

# dom_MemberOfExpression class attributes and methods
dom_MemberOfExpression_not: Property = Property(name="not", type=BooleanType)
dom_MemberOfExpression_operator: Property = Property(name="operator", type=StringType)
dom_MemberOfExpression_memberOf: Property = Property(name="memberOf", type=StringType)
dom_MemberOfExpression.attributes={dom_MemberOfExpression_memberOf, dom_MemberOfExpression_not, dom_MemberOfExpression_operator}

# dom_UnaryExpression class attributes and methods
dom_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
dom_UnaryExpression.attributes={dom_UnaryExpression_operator}

# Relationships
attributes0: BinaryAssociation = BinaryAssociation(
    name="attributes0",
    ends={
        Property(name="dom_Attribute", type=dom_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ComplexType", type=dom_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allAttributes1: BinaryAssociation = BinaryAssociation(
    name="allAttributes1",
    ends={
        Property(name="dom_Attribute3", type=dom_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ComplexType2", type=dom_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
dependencies4: BinaryAssociation = BinaryAssociation(
    name="dependencies4",
    ends={
        Property(name="dom_Dependant", type=dom_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Service", type=dom_Dependant, multiplicity=Multiplicity(0, 9999))
    }
)
operations5: BinaryAssociation = BinaryAssociation(
    name="operations5",
    ends={
        Property(name="dom_Operation", type=dom_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Service6", type=dom_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delegateOperations7: BinaryAssociation = BinaryAssociation(
    name="delegateOperations7",
    ends={
        Property(name="dom_DelegateOperation", type=dom_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Service8", type=dom_DelegateOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="dom_SimpleType", type=dom_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Property", type=dom_SimpleType, multiplicity=Multiplicity(0, 1))
    }
)
operation21: BinaryAssociation = BinaryAssociation(
    name="operation21",
    ends={
        Property(name="dom_DaoOperation", type=dom_DelegateOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DelegateOperation22", type=dom_DaoOperation, multiplicity=Multiplicity(0, 1))
    }
)
viewParameter23: BinaryAssociation = BinaryAssociation(
    name="viewParameter23",
    ends={
        Property(name="dom_DataView25", type=dom_DelegateOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DelegateOperation24", type=dom_DataView, multiplicity=Multiplicity(0, 1))
    }
)
parameters10: BinaryAssociation = BinaryAssociation(
    name="parameters10",
    ends={
        Property(name="dom_Parameter", type=dom_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Operation11", type=dom_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delegate12: BinaryAssociation = BinaryAssociation(
    name="delegate12",
    ends={
        Property(name="dom_DelegateOperation14", type=dom_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Operation13", type=dom_DelegateOperation, multiplicity=Multiplicity(0, 1))
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="dom_Type", type=dom_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Parameter16", type=dom_Type, multiplicity=Multiplicity(0, 1))
    }
)
view17: BinaryAssociation = BinaryAssociation(
    name="view17",
    ends={
        Property(name="dom_DataView", type=dom_DelegateOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DelegateOperation18", type=dom_DataView, multiplicity=Multiplicity(0, 1))
    }
)
repository19: BinaryAssociation = BinaryAssociation(
    name="repository19",
    ends={
        Property(name="dom_Dao", type=dom_DelegateOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DelegateOperation20", type=dom_Dao, multiplicity=Multiplicity(0, 1))
    }
)
view41: BinaryAssociation = BinaryAssociation(
    name="view41",
    ends={
        Property(name="dom_DataView43", type=dom_FeatureReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FeatureReference42", type=dom_DataView, multiplicity=Multiplicity(0, 1))
    }
)
filter26: BinaryAssociation = BinaryAssociation(
    name="filter26",
    ends={
        Property(name="dom_Expression", type=dom_DelegateOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DelegateOperation27", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="dom_Type30", type=dom_DaoOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DaoOperation29", type=dom_Type, multiplicity=Multiplicity(0, 1))
    }
)
superType32: BinaryAssociation = BinaryAssociation(
    name="superType32",
    ends={
        Property(name="dom_DataView33", type=dom_DataView, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DataView31", type=dom_DataView, multiplicity=Multiplicity(0, 1))
    }
)
featureReferences34: BinaryAssociation = BinaryAssociation(
    name="featureReferences34",
    ends={
        Property(name="dom_FeatureReference", type=dom_DataView, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DataView35", type=dom_FeatureReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source36: BinaryAssociation = BinaryAssociation(
    name="source36",
    ends={
        Property(name="dom_Entity", type=dom_FeatureReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FeatureReference37", type=dom_Entity, multiplicity=Multiplicity(0, 1))
    }
)
attribute38: BinaryAssociation = BinaryAssociation(
    name="attribute38",
    ends={
        Property(name="dom_Attribute40", type=dom_FeatureReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FeatureReference39", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
right59: BinaryAssociation = BinaryAssociation(
    name="right59",
    ends={
        Property(name="dom_Attribute61", type=dom_PropertyMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_PropertyMapping60", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
properties44: BinaryAssociation = BinaryAssociation(
    name="properties44",
    ends={
        Property(name="dom_AttributeProperty", type=dom_FeatureReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FeatureReference45", type=dom_AttributeProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target46: BinaryAssociation = BinaryAssociation(
    name="target46",
    ends={
        Property(name="dom_Attribute48", type=dom_FeatureReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FeatureReference47", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
left49: BinaryAssociation = BinaryAssociation(
    name="left49",
    ends={
        Property(name="dom_ComplexType50", type=dom_Mapper, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Mapper", type=dom_ComplexType, multiplicity=Multiplicity(0, 1))
    }
)
right51: BinaryAssociation = BinaryAssociation(
    name="right51",
    ends={
        Property(name="dom_ComplexType53", type=dom_Mapper, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Mapper52", type=dom_ComplexType, multiplicity=Multiplicity(0, 1))
    }
)
propertyMappings54: BinaryAssociation = BinaryAssociation(
    name="propertyMappings54",
    ends={
        Property(name="dom_PropertyMapping", type=dom_Mapper, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Mapper55", type=dom_PropertyMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left56: BinaryAssociation = BinaryAssociation(
    name="left56",
    ends={
        Property(name="dom_Attribute58", type=dom_PropertyMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_PropertyMapping57", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
requiredReferences84: BinaryAssociation = BinaryAssociation(
    name="requiredReferences84",
    ends={
        Property(name="dom_Attribute86", type=dom_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Entity85", type=dom_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
requiredAttributes87: BinaryAssociation = BinaryAssociation(
    name="requiredAttributes87",
    ends={
        Property(name="dom_Attribute89", type=dom_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Entity88", type=dom_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
superType63: BinaryAssociation = BinaryAssociation(
    name="superType63",
    ends={
        Property(name="dom_Entity64", type=dom_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Entity62", type=dom_Entity, multiplicity=Multiplicity(0, 1))
    }
)
attributeGroups65: BinaryAssociation = BinaryAssociation(
    name="attributeGroups65",
    ends={
        Property(name="dom_AttributeGroup", type=dom_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Entity66", type=dom_AttributeGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionsBlock67: BinaryAssociation = BinaryAssociation(
    name="conditionsBlock67",
    ends={
        Property(name="dom_ConditionsBlock", type=dom_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Entity68", type=dom_ConditionsBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repository69: BinaryAssociation = BinaryAssociation(
    name="repository69",
    ends={
        Property(name="dom_Dao71", type=dom_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Entity70", type=dom_Dao, multiplicity=Multiplicity(0, 1))
    }
)
key72: BinaryAssociation = BinaryAssociation(
    name="key72",
    ends={
        Property(name="dom_AttributeGroup74", type=dom_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Entity73", type=dom_AttributeGroup, multiplicity=Multiplicity(0, 1))
    }
)
sortOrders75: BinaryAssociation = BinaryAssociation(
    name="sortOrders75",
    ends={
        Property(name="dom_AttributeGroup77", type=dom_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Entity76", type=dom_AttributeGroup, multiplicity=Multiplicity(0, 9999))
    }
)
identifier78: BinaryAssociation = BinaryAssociation(
    name="identifier78",
    ends={
        Property(name="dom_Attribute80", type=dom_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Entity79", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
version81: BinaryAssociation = BinaryAssociation(
    name="version81",
    ends={
        Property(name="dom_Attribute83", type=dom_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Entity82", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
dataType103: BinaryAssociation = BinaryAssociation(
    name="dataType103",
    ends={
        Property(name="dom_Type105", type=dom_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Attribute104", type=dom_Type, multiplicity=Multiplicity(0, 1))
    }
)
oppositeReference107: BinaryAssociation = BinaryAssociation(
    name="oppositeReference107",
    ends={
        Property(name="dom_Attribute108", type=dom_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Attribute106", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
type90: BinaryAssociation = BinaryAssociation(
    name="type90",
    ends={
        Property(name="dom_DataTypeAndTypeParameter", type=dom_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Attribute91", type=dom_DataTypeAndTypeParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incrementerReference92: BinaryAssociation = BinaryAssociation(
    name="incrementerReference92",
    ends={
        Property(name="dom_IncrementerReference", type=dom_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Attribute93", type=dom_IncrementerReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite95: BinaryAssociation = BinaryAssociation(
    name="opposite95",
    ends={
        Property(name="dom_Attribute96", type=dom_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Attribute94", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
attributProperties97: BinaryAssociation = BinaryAssociation(
    name="attributProperties97",
    ends={
        Property(name="dom_AttributeProperty99", type=dom_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Attribute98", type=dom_AttributeProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sortOrder100: BinaryAssociation = BinaryAssociation(
    name="sortOrder100",
    ends={
        Property(name="dom_AttributeGroup102", type=dom_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Attribute101", type=dom_AttributeGroup, multiplicity=Multiplicity(0, 1))
    }
)
resolvedAttributeList110: BinaryAssociation = BinaryAssociation(
    name="resolvedAttributeList110",
    ends={
        Property(name="dom_Attribute111", type=dom_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Attribute109", type=dom_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
expression113: BinaryAssociation = BinaryAssociation(
    name="expression113",
    ends={
        Property(name="dom_BoolLiteral", type=dom_DerivedFlag, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DerivedFlag", type=dom_BoolLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression112: BinaryAssociation = BinaryAssociation(
    name="expression112",
    ends={
        Property(name="dom_EqualityExpr", type=dom_ExpressionFlag, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ExpressionFlag", type=dom_EqualityExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression114: BinaryAssociation = BinaryAssociation(
    name="expression114",
    ends={
        Property(name="dom_BoolLiteral115", type=dom_TransientFlag, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_TransientFlag", type=dom_BoolLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints116: BinaryAssociation = BinaryAssociation(
    name="constraints116",
    ends={
        Property(name="dom_Constraint", type=dom_AttributeValidationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AttributeValidationProperty", type=dom_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
format117: BinaryAssociation = BinaryAssociation(
    name="format117",
    ends={
        Property(name="dom_ValidatorReference", type=dom_AttributeValidationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AttributeValidationProperty118", type=dom_ValidatorReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unitAttribute119: BinaryAssociation = BinaryAssociation(
    name="unitAttribute119",
    ends={
        Property(name="dom_Attribute120", type=dom_AttributeTextProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AttributeTextProperty", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
operations134: BinaryAssociation = BinaryAssociation(
    name="operations134",
    ends={
        Property(name="dom_Operation136", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao135", type=dom_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes121: BinaryAssociation = BinaryAssociation(
    name="attributes121",
    ends={
        Property(name="dom_AttributeSortOrder", type=dom_AttributeGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AttributeGroup122", type=dom_AttributeSortOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolvedAttributeList123: BinaryAssociation = BinaryAssociation(
    name="resolvedAttributeList123",
    ends={
        Property(name="dom_Attribute125", type=dom_AttributeGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AttributeGroup124", type=dom_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
attribute126: BinaryAssociation = BinaryAssociation(
    name="attribute126",
    ends={
        Property(name="dom_Attribute128", type=dom_AttributeSortOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AttributeSortOrder127", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
attribute129: BinaryAssociation = BinaryAssociation(
    name="attribute129",
    ends={
        Property(name="dom_Attribute130", type=dom_DaoFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DaoFeature", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
entity131: BinaryAssociation = BinaryAssociation(
    name="entity131",
    ends={
        Property(name="dom_Entity133", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao132", type=dom_Entity, multiplicity=Multiplicity(0, 1))
    }
)
naturalKeyColumns154: BinaryAssociation = BinaryAssociation(
    name="naturalKeyColumns154",
    ends={
        Property(name="dom_Column156", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao155", type=dom_Column, multiplicity=Multiplicity(0, 9999))
    }
)
queryOperation137: BinaryAssociation = BinaryAssociation(
    name="queryOperation137",
    ends={
        Property(name="dom_QueryOperation", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao138", type=dom_QueryOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataBaseConstraints139: BinaryAssociation = BinaryAssociation(
    name="dataBaseConstraints139",
    ends={
        Property(name="dom_DataBaseConstraint", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao140", type=dom_DataBaseConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns141: BinaryAssociation = BinaryAssociation(
    name="columns141",
    ends={
        Property(name="dom_Column", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao142", type=dom_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manyToOneAssociations143: BinaryAssociation = BinaryAssociation(
    name="manyToOneAssociations143",
    ends={
        Property(name="dom_ManyToOne", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao144", type=dom_ManyToOne, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oneToOneAssociations145: BinaryAssociation = BinaryAssociation(
    name="oneToOneAssociations145",
    ends={
        Property(name="dom_OneToOne", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao146", type=dom_OneToOne, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oneToManyAssociations147: BinaryAssociation = BinaryAssociation(
    name="oneToManyAssociations147",
    ends={
        Property(name="dom_OneToMany", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao148", type=dom_OneToMany, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manyToManyAssociations149: BinaryAssociation = BinaryAssociation(
    name="manyToManyAssociations149",
    ends={
        Property(name="dom_ManyToMany", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao150", type=dom_ManyToMany, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKeyColumn151: BinaryAssociation = BinaryAssociation(
    name="primaryKeyColumn151",
    ends={
        Property(name="dom_Column153", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao152", type=dom_Column, multiplicity=Multiplicity(0, 1))
    }
)
userType173: BinaryAssociation = BinaryAssociation(
    name="userType173",
    ends={
        Property(name="dom_DataTypeAndTypeParameter175", type=dom_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Column174", type=dom_DataTypeAndTypeParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnType176: BinaryAssociation = BinaryAssociation(
    name="columnType176",
    ends={
        Property(name="dom_Type178", type=dom_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Column177", type=dom_Type, multiplicity=Multiplicity(0, 1))
    }
)
versionColumn157: BinaryAssociation = BinaryAssociation(
    name="versionColumn157",
    ends={
        Property(name="dom_Column159", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao158", type=dom_Column, multiplicity=Multiplicity(0, 1))
    }
)
columns180: BinaryAssociation = BinaryAssociation(
    name="columns180",
    ends={
        Property(name="dom_Column181", type=dom_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Column179", type=dom_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey160: BinaryAssociation = BinaryAssociation(
    name="primaryKey160",
    ends={
        Property(name="dom_DataBaseConstraint162", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao161", type=dom_DataBaseConstraint, multiplicity=Multiplicity(0, 1))
    }
)
naturalKey163: BinaryAssociation = BinaryAssociation(
    name="naturalKey163",
    ends={
        Property(name="dom_DataBaseConstraint165", type=dom_Dao, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Dao164", type=dom_DataBaseConstraint, multiplicity=Multiplicity(0, 1))
    }
)
queryParameters166: BinaryAssociation = BinaryAssociation(
    name="queryParameters166",
    ends={
        Property(name="dom_QueryParameter", type=dom_QueryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_QueryOperation167", type=dom_QueryParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement168: BinaryAssociation = BinaryAssociation(
    name="statement168",
    ends={
        Property(name="dom_QlStatement", type=dom_QueryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_QueryOperation169", type=dom_QlStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute170: BinaryAssociation = BinaryAssociation(
    name="attribute170",
    ends={
        Property(name="dom_Attribute172", type=dom_QueryParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_QueryParameter171", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
attributes193: BinaryAssociation = BinaryAssociation(
    name="attributes193",
    ends={
        Property(name="dom_Attribute195", type=dom_DataBaseConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DataBaseConstraint194", type=dom_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
userType182: BinaryAssociation = BinaryAssociation(
    name="userType182",
    ends={
        Property(name="dom_Type184", type=dom_ManyToOne, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ManyToOne183", type=dom_Type, multiplicity=Multiplicity(0, 1))
    }
)
sqlType185: BinaryAssociation = BinaryAssociation(
    name="sqlType185",
    ends={
        Property(name="dom_SqlType", type=dom_ManyToOne, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ManyToOne186", type=dom_SqlType, multiplicity=Multiplicity(0, 1))
    }
)
columns187: BinaryAssociation = BinaryAssociation(
    name="columns187",
    ends={
        Property(name="dom_Column189", type=dom_ManyToOne, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ManyToOne188", type=dom_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns190: BinaryAssociation = BinaryAssociation(
    name="columns190",
    ends={
        Property(name="dom_Column192", type=dom_OneToMany, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_OneToMany191", type=dom_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties199: BinaryAssociation = BinaryAssociation(
    name="properties199",
    ends={
        Property(name="dom_Property200", type=dom_ApplicationSession, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ApplicationSession", type=dom_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions201: BinaryAssociation = BinaryAssociation(
    name="functions201",
    ends={
        Property(name="dom_Function", type=dom_ApplicationSession, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ApplicationSession202", type=dom_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionsBlock203: BinaryAssociation = BinaryAssociation(
    name="conditionsBlock203",
    ends={
        Property(name="dom_ConditionsBlock205", type=dom_ApplicationSession, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ApplicationSession204", type=dom_ConditionsBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resolvedAttributeList196: BinaryAssociation = BinaryAssociation(
    name="resolvedAttributeList196",
    ends={
        Property(name="dom_Attribute198", type=dom_DataBaseConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DataBaseConstraint197", type=dom_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
attribute215: BinaryAssociation = BinaryAssociation(
    name="attribute215",
    ends={
        Property(name="dom_Attribute217", type=dom_CallOutputParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CallOutputParameter216", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
nestedAttribute218: BinaryAssociation = BinaryAssociation(
    name="nestedAttribute218",
    ends={
        Property(name="dom_Attribute220", type=dom_CallOutputParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CallOutputParameter219", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
inParameter206: BinaryAssociation = BinaryAssociation(
    name="inParameter206",
    ends={
        Property(name="dom_CallInputParameter", type=dom_CallableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CallableStatement", type=dom_CallInputParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outParameter207: BinaryAssociation = BinaryAssociation(
    name="outParameter207",
    ends={
        Property(name="dom_CallOutputParameter", type=dom_CallableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CallableStatement208", type=dom_CallOutputParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter209: BinaryAssociation = BinaryAssociation(
    name="parameter209",
    ends={
        Property(name="dom_QueryParameter211", type=dom_CallInputParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CallInputParameter210", type=dom_QueryParameter, multiplicity=Multiplicity(0, 1))
    }
)
attribute212: BinaryAssociation = BinaryAssociation(
    name="attribute212",
    ends={
        Property(name="dom_Attribute214", type=dom_CallInputParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CallInputParameter213", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
entity233: BinaryAssociation = BinaryAssociation(
    name="entity233",
    ends={
        Property(name="dom_UpdateStatement", type=dom_Entity, multiplicity=Multiplicity(0, 1)),
        Property(name="dom_Entity234", type=dom_UpdateStatement, multiplicity=Multiplicity(1, 1))
    }
)
assignment235: BinaryAssociation = BinaryAssociation(
    name="assignment235",
    ends={
        Property(name="dom_PropertyAssignment", type=dom_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_UpdateStatement236", type=dom_PropertyAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
where237: BinaryAssociation = BinaryAssociation(
    name="where237",
    ends={
        Property(name="dom_Expression239", type=dom_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_UpdateStatement238", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entity221: BinaryAssociation = BinaryAssociation(
    name="entity221",
    ends={
        Property(name="dom_Entity222", type=dom_InsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_InsertStatement", type=dom_Entity, multiplicity=Multiplicity(0, 1))
    }
)
expression223: BinaryAssociation = BinaryAssociation(
    name="expression223",
    ends={
        Property(name="dom_Expression225", type=dom_InsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_InsertStatement224", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectStatement226: BinaryAssociation = BinaryAssociation(
    name="selectStatement226",
    ends={
        Property(name="dom_SelectStatement", type=dom_InsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_InsertStatement227", type=dom_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entity228: BinaryAssociation = BinaryAssociation(
    name="entity228",
    ends={
        Property(name="dom_Entity229", type=dom_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DeleteStatement", type=dom_Entity, multiplicity=Multiplicity(0, 1))
    }
)
where230: BinaryAssociation = BinaryAssociation(
    name="where230",
    ends={
        Property(name="dom_Expression232", type=dom_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DeleteStatement231", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderBy258: BinaryAssociation = BinaryAssociation(
    name="orderBy258",
    ends={
        Property(name="dom_SortOrderElement", type=dom_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SelectStatement259", type=dom_SortOrderElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property240: BinaryAssociation = BinaryAssociation(
    name="property240",
    ends={
        Property(name="dom_PropertyValue", type=dom_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_PropertyAssignment241", type=dom_PropertyValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression242: BinaryAssociation = BinaryAssociation(
    name="expression242",
    ends={
        Property(name="dom_Expression244", type=dom_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_PropertyAssignment243", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from245: BinaryAssociation = BinaryAssociation(
    name="from245",
    ends={
        Property(name="dom_FromRange", type=dom_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SelectStatement246", type=dom_FromRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join247: BinaryAssociation = BinaryAssociation(
    name="join247",
    ends={
        Property(name="dom_Join", type=dom_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SelectStatement248", type=dom_Join, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
where249: BinaryAssociation = BinaryAssociation(
    name="where249",
    ends={
        Property(name="dom_Expression251", type=dom_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SelectStatement250", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupBy252: BinaryAssociation = BinaryAssociation(
    name="groupBy252",
    ends={
        Property(name="dom_Expression254", type=dom_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SelectStatement253", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity267: BinaryAssociation = BinaryAssociation(
    name="entity267",
    ends={
        Property(name="dom_Entity268", type=dom_FromClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FromClass", type=dom_Entity, multiplicity=Multiplicity(0, 1))
    }
)
having255: BinaryAssociation = BinaryAssociation(
    name="having255",
    ends={
        Property(name="dom_Expression257", type=dom_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SelectStatement256", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression260: BinaryAssociation = BinaryAssociation(
    name="expression260",
    ends={
        Property(name="dom_Expression262", type=dom_SortOrderElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SortOrderElement261", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties263: BinaryAssociation = BinaryAssociation(
    name="properties263",
    ends={
        Property(name="dom_Expression264", type=dom_SelectProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SelectProperties", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments265: BinaryAssociation = BinaryAssociation(
    name="arguments265",
    ends={
        Property(name="dom_Expression266", type=dom_SelectClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SelectClass", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
index277: BinaryAssociation = BinaryAssociation(
    name="index277",
    ends={
        Property(name="dom_Expression279", type=dom_PropertyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_PropertyValue278", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity269: BinaryAssociation = BinaryAssociation(
    name="entity269",
    ends={
        Property(name="dom_JoinEntity", type=dom_Join, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Join270", type=dom_JoinEntity, multiplicity=Multiplicity(0, 1))
    }
)
reference271: BinaryAssociation = BinaryAssociation(
    name="reference271",
    ends={
        Property(name="dom_Attribute273", type=dom_Join, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Join272", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
expression274: BinaryAssociation = BinaryAssociation(
    name="expression274",
    ends={
        Property(name="dom_Expression276", type=dom_Join, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Join275", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from286: BinaryAssociation = BinaryAssociation(
    name="from286",
    ends={
        Property(name="dom_Expression287", type=dom_CastFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CastFunction", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments280: BinaryAssociation = BinaryAssociation(
    name="arguments280",
    ends={
        Property(name="dom_Expression281", type=dom_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FunctionCall", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
character282: BinaryAssociation = BinaryAssociation(
    name="character282",
    ends={
        Property(name="dom_StringLiteralValue", type=dom_TrimFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_TrimFunction", type=dom_StringLiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from283: BinaryAssociation = BinaryAssociation(
    name="from283",
    ends={
        Property(name="dom_Expression285", type=dom_TrimFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_TrimFunction284", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression296: BinaryAssociation = BinaryAssociation(
    name="expression296",
    ends={
        Property(name="dom_Expression297", type=dom_QuantifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_QuantifiedExpression", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whenClause298: BinaryAssociation = BinaryAssociation(
    name="whenClause298",
    ends={
        Property(name="dom_WhenClause", type=dom_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CaseExpression", type=dom_WhenClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aggregateExpression288: BinaryAssociation = BinaryAssociation(
    name="aggregateExpression288",
    ends={
        Property(name="dom_Expression289", type=dom_AggregateFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AggregateFunction", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collection290: BinaryAssociation = BinaryAssociation(
    name="collection290",
    ends={
        Property(name="dom_CollectionFunction", type=dom_AggregateFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AggregateFunction291", type=dom_CollectionFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter292: BinaryAssociation = BinaryAssociation(
    name="parameter292",
    ends={
        Property(name="dom_QueryParameterReference", type=dom_QueryParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_QueryParameterValue", type=dom_QueryParameterReference, multiplicity=Multiplicity(0, 1))
    }
)
attribute293: BinaryAssociation = BinaryAssociation(
    name="attribute293",
    ends={
        Property(name="dom_Attribute295", type=dom_QueryParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_QueryParameterValue294", type=dom_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
thenExpression316: BinaryAssociation = BinaryAssociation(
    name="thenExpression316",
    ends={
        Property(name="dom_Expression318", type=dom_AltWhenClause, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AltWhenClause317", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property319: BinaryAssociation = BinaryAssociation(
    name="property319",
    ends={
        Property(name="dom_PropertyValue321", type=dom_CollectionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CollectionFunction320", type=dom_PropertyValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression299: BinaryAssociation = BinaryAssociation(
    name="elseExpression299",
    ends={
        Property(name="dom_Expression301", type=dom_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CaseExpression300", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression302: BinaryAssociation = BinaryAssociation(
    name="expression302",
    ends={
        Property(name="dom_Expression304", type=dom_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CaseExpression303", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
altWhenClause305: BinaryAssociation = BinaryAssociation(
    name="altWhenClause305",
    ends={
        Property(name="dom_AltWhenClause", type=dom_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CaseExpression306", type=dom_AltWhenClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whenExpression307: BinaryAssociation = BinaryAssociation(
    name="whenExpression307",
    ends={
        Property(name="dom_Expression309", type=dom_WhenClause, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_WhenClause308", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression310: BinaryAssociation = BinaryAssociation(
    name="thenExpression310",
    ends={
        Property(name="dom_Expression312", type=dom_WhenClause, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_WhenClause311", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whenExpression313: BinaryAssociation = BinaryAssociation(
    name="whenExpression313",
    ends={
        Property(name="dom_Expression315", type=dom_AltWhenClause, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AltWhenClause314", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
queries322: BinaryAssociation = BinaryAssociation(
    name="queries322",
    ends={
        Property(name="dom_SelectStatement323", type=dom_SubQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SubQuery", type=dom_SelectStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions324: BinaryAssociation = BinaryAssociation(
    name="expressions324",
    ends={
        Property(name="dom_Expression325", type=dom_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ParenthesizedExpression", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression333: BinaryAssociation = BinaryAssociation(
    name="expression333",
    ends={
        Property(name="dom_Expression334", type=dom_NotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_NotExpression", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression335: BinaryAssociation = BinaryAssociation(
    name="expression335",
    ends={
        Property(name="dom_Expression336", type=dom_InExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_InExpression", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression326: BinaryAssociation = BinaryAssociation(
    name="expression326",
    ends={
        Property(name="dom_Expression327", type=dom_AliasedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AliasedExpression", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left328: BinaryAssociation = BinaryAssociation(
    name="left328",
    ends={
        Property(name="dom_Expression329", type=dom_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_BinaryExpression", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right330: BinaryAssociation = BinaryAssociation(
    name="right330",
    ends={
        Property(name="dom_Expression332", type=dom_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_BinaryExpression331", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression348: BinaryAssociation = BinaryAssociation(
    name="expression348",
    ends={
        Property(name="dom_Expression349", type=dom_LikeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_LikeExpression", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
like350: BinaryAssociation = BinaryAssociation(
    name="like350",
    ends={
        Property(name="dom_Expression352", type=dom_LikeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_LikeExpression351", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in337: BinaryAssociation = BinaryAssociation(
    name="in337",
    ends={
        Property(name="dom_Expression339", type=dom_InExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_InExpression338", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression340: BinaryAssociation = BinaryAssociation(
    name="expression340",
    ends={
        Property(name="dom_Expression341", type=dom_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_BetweenExpression", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left342: BinaryAssociation = BinaryAssociation(
    name="left342",
    ends={
        Property(name="dom_Expression344", type=dom_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_BetweenExpression343", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right345: BinaryAssociation = BinaryAssociation(
    name="right345",
    ends={
        Property(name="dom_Expression347", type=dom_BetweenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_BetweenExpression346", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
escape353: BinaryAssociation = BinaryAssociation(
    name="escape353",
    ends={
        Property(name="dom_Expression355", type=dom_LikeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_LikeExpression354", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression356: BinaryAssociation = BinaryAssociation(
    name="expression356",
    ends={
        Property(name="dom_Expression357", type=dom_MemberOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_MemberOfExpression", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression358: BinaryAssociation = BinaryAssociation(
    name="expression358",
    ends={
        Property(name="dom_Expression359", type=dom_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_UnaryExpression", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dom_ComplexType_ModelElement = Generalization(general=ModelElement, specific=dom_ComplexType)
gen_dom_ComplexType_Type = Generalization(general=Type, specific=dom_ComplexType)
gen_dom_Operation_DaoOperation = Generalization(general=DaoOperation, specific=dom_Operation)
gen_dom_Operation_IDocumentable = Generalization(general=IDocumentable, specific=dom_Operation)
gen_dom_Service_ModelElement = Generalization(general=ModelElement, specific=dom_Service)
gen_dom_Service_Dependant = Generalization(general=Dependant, specific=dom_Service)
gen_dom_Property_ReferenceableByXmadslVariable = Generalization(general=ReferenceableByXmadslVariable, specific=dom_Property)
gen_dom_Property_IDocumentable = Generalization(general=IDocumentable, specific=dom_Property)
gen_dom_Parameter_QueryParameter = Generalization(general=QueryParameter, specific=dom_Parameter)
gen_dom_Parameter_QueryParameterReference = Generalization(general=QueryParameterReference, specific=dom_Parameter)
gen_dom_DelegateOperation_IDocumentable = Generalization(general=IDocumentable, specific=dom_DelegateOperation)
gen_dom_ValueObject_ComplexType = Generalization(general=ComplexType, specific=dom_ValueObject)
gen_dom_DataView_ComplexType = Generalization(general=ComplexType, specific=dom_DataView)
gen_dom_FeatureReference_PresentableFeature = Generalization(general=PresentableFeature, specific=dom_FeatureReference)
gen_dom_FeatureReference_IDocumentable = Generalization(general=IDocumentable, specific=dom_FeatureReference)
gen_dom_Entity_ComplexType = Generalization(general=ComplexType, specific=dom_Entity)
gen_dom_Entity_Dependant = Generalization(general=Dependant, specific=dom_Entity)
gen_dom_Mapper_ModelElement = Generalization(general=ModelElement, specific=dom_Mapper)
gen_dom_Attribute_ReferenceableByXmadslVariable = Generalization(general=ReferenceableByXmadslVariable, specific=dom_Attribute)
gen_dom_Attribute_QueryParameterReference = Generalization(general=QueryParameterReference, specific=dom_Attribute)
gen_dom_Attribute_PresentableFeature = Generalization(general=PresentableFeature, specific=dom_Attribute)
gen_dom_Attribute_IDocumentable = Generalization(general=IDocumentable, specific=dom_Attribute)
gen_dom_AttributeFlag_AttributeProperty = Generalization(general=AttributeProperty, specific=dom_AttributeFlag)
gen_dom_AvailableFlag_ExpressionFlag = Generalization(general=ExpressionFlag, specific=dom_AvailableFlag)
gen_dom_DerivedFlag_AttributeFlag = Generalization(general=AttributeFlag, specific=dom_DerivedFlag)
gen_dom_ExpressionFlag_AttributeFlag = Generalization(general=AttributeFlag, specific=dom_ExpressionFlag)
gen_dom_RequiredFlag_ExpressionFlag = Generalization(general=ExpressionFlag, specific=dom_RequiredFlag)
gen_dom_ReadOnlyFlag_ExpressionFlag = Generalization(general=ExpressionFlag, specific=dom_ReadOnlyFlag)
gen_dom_TransientFlag_AttributeFlag = Generalization(general=AttributeFlag, specific=dom_TransientFlag)
gen_dom_AttributeValidationProperty_AttributeProperty = Generalization(general=AttributeProperty, specific=dom_AttributeValidationProperty)
gen_dom_AttributeTextProperty_AttributeProperty = Generalization(general=AttributeProperty, specific=dom_AttributeTextProperty)
gen_dom_AttributeGroup_IDocumentable = Generalization(general=IDocumentable, specific=dom_AttributeGroup)
gen_dom_Dao_ModelElement = Generalization(general=ModelElement, specific=dom_Dao)
gen_dom_Dao_Dependant = Generalization(general=Dependant, specific=dom_Dao)
gen_dom_QueryOperation_DaoOperation = Generalization(general=DaoOperation, specific=dom_QueryOperation)
gen_dom_QueryOperation_IDocumentable = Generalization(general=IDocumentable, specific=dom_QueryOperation)
gen_dom_Column_DaoFeature = Generalization(general=DaoFeature, specific=dom_Column)
gen_dom_ManyToMany_DaoFeature = Generalization(general=DaoFeature, specific=dom_ManyToMany)
gen_dom_ManyToOne_DaoFeature = Generalization(general=DaoFeature, specific=dom_ManyToOne)
gen_dom_OneToOne_DaoFeature = Generalization(general=DaoFeature, specific=dom_OneToOne)
gen_dom_OneToMany_DaoFeature = Generalization(general=DaoFeature, specific=dom_OneToMany)
gen_dom_ApplicationSession_ModelElement = Generalization(general=ModelElement, specific=dom_ApplicationSession)
gen_dom_InsertStatement_QlStatement = Generalization(general=QlStatement, specific=dom_InsertStatement)
gen_dom_CallableStatement_QlStatement = Generalization(general=QlStatement, specific=dom_CallableStatement)
gen_dom_DeleteStatement_QlStatement = Generalization(general=QlStatement, specific=dom_DeleteStatement)
gen_dom_UpdateStatement_QlStatement = Generalization(general=QlStatement, specific=dom_UpdateStatement)
gen_dom_SelectStatement_QlStatement = Generalization(general=QlStatement, specific=dom_SelectStatement)
gen_dom_InClass_FromRange = Generalization(general=FromRange, specific=dom_InClass)
gen_dom_InCollection_FromRange = Generalization(general=FromRange, specific=dom_InCollection)
gen_dom_SelectProperties_SelectStatement = Generalization(general=SelectStatement, specific=dom_SelectProperties)
gen_dom_SelectClass_SelectStatement = Generalization(general=SelectStatement, specific=dom_SelectClass)
gen_dom_SelectObject_SelectStatement = Generalization(general=SelectStatement, specific=dom_SelectObject)
gen_dom_FromClass_FromRange = Generalization(general=FromRange, specific=dom_FromClass)
gen_dom_FromClass_JoinEntity = Generalization(general=JoinEntity, specific=dom_FromClass)
gen_dom_PropertyValue_Expression = Generalization(general=Expression, specific=dom_PropertyValue)
gen_dom_InCollectionElements_FromRange = Generalization(general=FromRange, specific=dom_InCollectionElements)
gen_dom_Join_JoinEntity = Generalization(general=JoinEntity, specific=dom_Join)
gen_dom_FunctionCall_Expression = Generalization(general=Expression, specific=dom_FunctionCall)
gen_dom_TrimFunction_Expression = Generalization(general=Expression, specific=dom_TrimFunction)
gen_dom_CastFunction_Expression = Generalization(general=Expression, specific=dom_CastFunction)
gen_dom_CaseExpression_Expression = Generalization(general=Expression, specific=dom_CaseExpression)
gen_dom_AggregateFunction_Expression = Generalization(general=Expression, specific=dom_AggregateFunction)
gen_dom_QueryParameterValue_Expression = Generalization(general=Expression, specific=dom_QueryParameterValue)
gen_dom_QuantifiedExpression_Expression = Generalization(general=Expression, specific=dom_QuantifiedExpression)
gen_dom_CollectionFunction_Expression = Generalization(general=Expression, specific=dom_CollectionFunction)
gen_dom_BooleanLiteralValue_LiteralValue = Generalization(general=LiteralValue, specific=dom_BooleanLiteralValue)
gen_dom_NullLiteralValue_LiteralValue = Generalization(general=LiteralValue, specific=dom_NullLiteralValue)
gen_dom_EmptyLiteralValue_LiteralValue = Generalization(general=LiteralValue, specific=dom_EmptyLiteralValue)
gen_dom_IElementWithNoName_ReferenceableByXmadslVariable = Generalization(general=ReferenceableByXmadslVariable, specific=dom_IElementWithNoName)
gen_dom_IElementWithNoName_QueryParameterReference = Generalization(general=QueryParameterReference, specific=dom_IElementWithNoName)
gen_dom_SubQuery_Expression = Generalization(general=Expression, specific=dom_SubQuery)
gen_dom_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=dom_ParenthesizedExpression)
gen_dom_LiteralValue_Expression = Generalization(general=Expression, specific=dom_LiteralValue)
gen_dom_StringLiteralValue_LiteralValue = Generalization(general=LiteralValue, specific=dom_StringLiteralValue)
gen_dom_IntegerLiteralValue_LiteralValue = Generalization(general=LiteralValue, specific=dom_IntegerLiteralValue)
gen_dom_RealLiteralValue_LiteralValue = Generalization(general=LiteralValue, specific=dom_RealLiteralValue)
gen_dom_NotExpression_Expression = Generalization(general=Expression, specific=dom_NotExpression)
gen_dom_InExpression_Expression = Generalization(general=Expression, specific=dom_InExpression)
gen_dom_AliasedExpression_Expression = Generalization(general=Expression, specific=dom_AliasedExpression)
gen_dom_BinaryExpression_Expression = Generalization(general=Expression, specific=dom_BinaryExpression)
gen_dom_LikeExpression_Expression = Generalization(general=Expression, specific=dom_LikeExpression)
gen_dom_BetweenExpression_Expression = Generalization(general=Expression, specific=dom_BetweenExpression)
gen_dom_MemberOfExpression_Expression = Generalization(general=Expression, specific=dom_MemberOfExpression)
gen_dom_UnaryExpression_Expression = Generalization(general=Expression, specific=dom_UnaryExpression)

# Domain Model
domain_model = DomainModel(
    name="dom",
    types={dom_ComplexType, ModelElement, Type, dom_Attribute, DaoOperation, dom_Parameter, dom_Service, Dependant, dom_Dependant, dom_Operation, dom_DelegateOperation, dom_Property, ReferenceableByXmadslVariable, IDocumentable, dom_SimpleType, dom_DaoOperation, QueryParameter, QueryParameterReference, dom_Type, dom_DataView, dom_Dao, dom_Expression, dom_ValueObject, ComplexType, dom_FeatureReference, PresentableFeature, dom_Entity, dom_AttributeProperty, dom_Mapper, dom_PropertyMapping, dom_AttributeGroup, dom_ConditionsBlock, dom_DataTypeAndTypeParameter, dom_IncrementerReference, dom_AttributeFlag, AttributeProperty, dom_AvailableFlag, dom_DerivedFlag, dom_BoolLiteral, dom_ExpressionFlag, AttributeFlag, dom_EqualityExpr, dom_RequiredFlag, ExpressionFlag, dom_ReadOnlyFlag, dom_AttributeSortOrder, dom_TransientFlag, dom_AttributeValidationProperty, dom_Constraint, dom_ValidatorReference, dom_AttributeTextProperty, dom_DaoFeature, dom_QueryOperation, dom_DataBaseConstraint, dom_Column, dom_ManyToOne, dom_OneToOne, dom_OneToMany, dom_ManyToMany, dom_QueryParameter, dom_QlStatement, DaoFeature, dom_SqlType, dom_ApplicationSession, dom_Function, dom_InsertStatement, dom_CallableStatement, QlStatement, dom_CallInputParameter, dom_CallOutputParameter, dom_PropertyAssignment, dom_SelectStatement, dom_DeleteStatement, dom_UpdateStatement, dom_SortOrderElement, dom_PropertyValue, dom_FromRange, dom_Join, dom_InClass, dom_InCollection, dom_SelectProperties, SelectStatement, dom_SelectClass, dom_SelectObject, dom_FromClass, FromRange, JoinEntity, Expression, dom_InCollectionElements, dom_JoinEntity, dom_FunctionCall, dom_TrimFunction, dom_StringLiteralValue, dom_CastFunction, dom_CaseExpression, dom_AggregateFunction, dom_WhenClause, dom_CollectionFunction, dom_QueryParameterReference, dom_QueryParameterValue, dom_QuantifiedExpression, dom_AltWhenClause, dom_BooleanLiteralValue, dom_NullLiteralValue, dom_EmptyLiteralValue, dom_IElementWithNoName, dom_SubQuery, dom_ParenthesizedExpression, dom_LiteralValue, LiteralValue, dom_IntegerLiteralValue, dom_RealLiteralValue, dom_NotExpression, dom_InExpression, dom_PresentableFeature, dom_AliasedExpression, dom_BinaryExpression, dom_LikeExpression, dom_BetweenExpression, dom_MemberOfExpression, dom_UnaryExpression, CrudOperationType, DataBaseConstraintType},
    associations={attributes0, allAttributes1, dependencies4, operations5, delegateOperations7, type9, operation21, viewParameter23, parameters10, delegate12, type15, view17, repository19, view41, filter26, type28, superType32, featureReferences34, source36, attribute38, right59, properties44, target46, left49, right51, propertyMappings54, left56, requiredReferences84, requiredAttributes87, superType63, attributeGroups65, conditionsBlock67, repository69, key72, sortOrders75, identifier78, version81, dataType103, oppositeReference107, type90, incrementerReference92, opposite95, attributProperties97, sortOrder100, resolvedAttributeList110, expression113, expression112, expression114, constraints116, format117, unitAttribute119, operations134, attributes121, resolvedAttributeList123, attribute126, attribute129, entity131, naturalKeyColumns154, queryOperation137, dataBaseConstraints139, columns141, manyToOneAssociations143, oneToOneAssociations145, oneToManyAssociations147, manyToManyAssociations149, primaryKeyColumn151, userType173, columnType176, versionColumn157, columns180, primaryKey160, naturalKey163, queryParameters166, statement168, attribute170, attributes193, userType182, sqlType185, columns187, columns190, properties199, functions201, conditionsBlock203, resolvedAttributeList196, attribute215, nestedAttribute218, inParameter206, outParameter207, parameter209, attribute212, entity233, assignment235, where237, entity221, expression223, selectStatement226, entity228, where230, orderBy258, property240, expression242, from245, join247, where249, groupBy252, entity267, having255, expression260, properties263, arguments265, index277, entity269, reference271, expression274, from286, arguments280, character282, from283, expression296, whenClause298, aggregateExpression288, collection290, parameter292, attribute293, thenExpression316, property319, elseExpression299, expression302, altWhenClause305, whenExpression307, thenExpression310, whenExpression313, queries322, expressions324, expression333, expression335, expression326, left328, right330, expression348, like350, in337, expression340, left342, right345, escape353, expression356, expression358},
    generalizations={gen_dom_ComplexType_ModelElement, gen_dom_ComplexType_Type, gen_dom_Operation_DaoOperation, gen_dom_Operation_IDocumentable, gen_dom_Service_ModelElement, gen_dom_Service_Dependant, gen_dom_Property_ReferenceableByXmadslVariable, gen_dom_Property_IDocumentable, gen_dom_Parameter_QueryParameter, gen_dom_Parameter_QueryParameterReference, gen_dom_DelegateOperation_IDocumentable, gen_dom_ValueObject_ComplexType, gen_dom_DataView_ComplexType, gen_dom_FeatureReference_PresentableFeature, gen_dom_FeatureReference_IDocumentable, gen_dom_Entity_ComplexType, gen_dom_Entity_Dependant, gen_dom_Mapper_ModelElement, gen_dom_Attribute_ReferenceableByXmadslVariable, gen_dom_Attribute_QueryParameterReference, gen_dom_Attribute_PresentableFeature, gen_dom_Attribute_IDocumentable, gen_dom_AttributeFlag_AttributeProperty, gen_dom_AvailableFlag_ExpressionFlag, gen_dom_DerivedFlag_AttributeFlag, gen_dom_ExpressionFlag_AttributeFlag, gen_dom_RequiredFlag_ExpressionFlag, gen_dom_ReadOnlyFlag_ExpressionFlag, gen_dom_TransientFlag_AttributeFlag, gen_dom_AttributeValidationProperty_AttributeProperty, gen_dom_AttributeTextProperty_AttributeProperty, gen_dom_AttributeGroup_IDocumentable, gen_dom_Dao_ModelElement, gen_dom_Dao_Dependant, gen_dom_QueryOperation_DaoOperation, gen_dom_QueryOperation_IDocumentable, gen_dom_Column_DaoFeature, gen_dom_ManyToMany_DaoFeature, gen_dom_ManyToOne_DaoFeature, gen_dom_OneToOne_DaoFeature, gen_dom_OneToMany_DaoFeature, gen_dom_ApplicationSession_ModelElement, gen_dom_InsertStatement_QlStatement, gen_dom_CallableStatement_QlStatement, gen_dom_DeleteStatement_QlStatement, gen_dom_UpdateStatement_QlStatement, gen_dom_SelectStatement_QlStatement, gen_dom_InClass_FromRange, gen_dom_InCollection_FromRange, gen_dom_SelectProperties_SelectStatement, gen_dom_SelectClass_SelectStatement, gen_dom_SelectObject_SelectStatement, gen_dom_FromClass_FromRange, gen_dom_FromClass_JoinEntity, gen_dom_PropertyValue_Expression, gen_dom_InCollectionElements_FromRange, gen_dom_Join_JoinEntity, gen_dom_FunctionCall_Expression, gen_dom_TrimFunction_Expression, gen_dom_CastFunction_Expression, gen_dom_CaseExpression_Expression, gen_dom_AggregateFunction_Expression, gen_dom_QueryParameterValue_Expression, gen_dom_QuantifiedExpression_Expression, gen_dom_CollectionFunction_Expression, gen_dom_BooleanLiteralValue_LiteralValue, gen_dom_NullLiteralValue_LiteralValue, gen_dom_EmptyLiteralValue_LiteralValue, gen_dom_IElementWithNoName_ReferenceableByXmadslVariable, gen_dom_IElementWithNoName_QueryParameterReference, gen_dom_SubQuery_Expression, gen_dom_ParenthesizedExpression_Expression, gen_dom_LiteralValue_Expression, gen_dom_StringLiteralValue_LiteralValue, gen_dom_IntegerLiteralValue_LiteralValue, gen_dom_RealLiteralValue_LiteralValue, gen_dom_NotExpression_Expression, gen_dom_InExpression_Expression, gen_dom_AliasedExpression_Expression, gen_dom_BinaryExpression_Expression, gen_dom_LikeExpression_Expression, gen_dom_BetweenExpression_Expression, gen_dom_MemberOfExpression_Expression, gen_dom_UnaryExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)