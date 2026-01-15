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
SadlDataType: Enumeration = Enumeration(
    name="SadlDataType",
    literals={
            EnumerationLiteral(name="string"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="decimal"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="duration"),
			EnumerationLiteral(name="dateTime"),
			EnumerationLiteral(name="gYearMonth"),
			EnumerationLiteral(name="gYear"),
			EnumerationLiteral(name="gMonthDay"),
			EnumerationLiteral(name="gDay"),
			EnumerationLiteral(name="gMonth"),
			EnumerationLiteral(name="hexBinary"),
			EnumerationLiteral(name="base64Binary"),
			EnumerationLiteral(name="anyURI"),
			EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="negativeInteger"),
			EnumerationLiteral(name="nonNegativeInteger"),
			EnumerationLiteral(name="positiveInteger"),
			EnumerationLiteral(name="nonPositiveInteger"),
			EnumerationLiteral(name="byte"),
			EnumerationLiteral(name="unsignedByte"),
			EnumerationLiteral(name="unsignedInt"),
			EnumerationLiteral(name="anySimpleType"),
			EnumerationLiteral(name="time"),
			EnumerationLiteral(name="date")
    }
)

# Classes
sADL_SadlAnnotation = Class(name="sADL::SadlAnnotation")
sADL_SadlImport = Class(name="sADL::SadlImport")
sADL_SadlModelElement = Class(name="sADL::SadlModelElement")
sADL_EquationStatement = Class(name="sADL::EquationStatement")
SadlModelElement = Class(name="SadlModelElement")
AbstractSadlEquation = Class(name="AbstractSadlEquation")
sADL_Expression = Class(name="sADL::Expression")
sADL_SadlModel = Class(name="sADL::SadlModel")
sADL_AbstractSadlEquation = Class(name="sADL::AbstractSadlEquation")
sADL_SadlResource = Class(name="sADL::SadlResource")
sADL_SadlParameterDeclaration = Class(name="sADL::SadlParameterDeclaration")
sADL_SadlTypeReference = Class(name="sADL::SadlTypeReference")
sADL_SadlStatement = Class(name="sADL::SadlStatement")
sADL_SadlPropertyCondition = Class(name="sADL::SadlPropertyCondition")
SadlTypeReference = Class(name="SadlTypeReference")
sADL_ExternalEquationStatement = Class(name="sADL::ExternalEquationStatement")
sADL_SadlPropertyInitializer = Class(name="sADL::SadlPropertyInitializer")
sADL_EObject = Class(name="sADL::EObject")
sADL_SadlInstance = Class(name="sADL::SadlInstance")
SadlStatement = Class(name="SadlStatement")
sADL_SadlValueList = Class(name="sADL::SadlValueList")
SadlExplicitValueLiteral = Class(name="SadlExplicitValueLiteral")
Expression = Class(name="Expression")
sADL_SadlCondition = Class(name="sADL::SadlCondition")
sADL_SadlDataTypeFacet = Class(name="sADL::SadlDataTypeFacet")
sADL_SadlProperty = Class(name="sADL::SadlProperty")
sADL_SadlPropertyRestriction = Class(name="sADL::SadlPropertyRestriction")
SadlPropertyRestriction = Class(name="SadlPropertyRestriction")
sADL_SadlAllValuesCondition = Class(name="sADL::SadlAllValuesCondition")
SadlCondition = Class(name="SadlCondition")
sADL_SadlHasValueCondition = Class(name="sADL::SadlHasValueCondition")
sADL_SadlCardinalityCondition = Class(name="sADL::SadlCardinalityCondition")
sADL_SadlExplicitValue = Class(name="sADL::SadlExplicitValue")
sADL_SadlExplicitValueLiteral = Class(name="sADL::SadlExplicitValueLiteral")
SadlExplicitValue = Class(name="SadlExplicitValue")
sADL_ExpressionScope = Class(name="sADL::ExpressionScope")
sADL_NamedStructureAnnotation = Class(name="sADL::NamedStructureAnnotation")
sADL_PrintStatement = Class(name="sADL::PrintStatement")
sADL_ExplainStatement = Class(name="sADL::ExplainStatement")
sADL_EndWriteStatement = Class(name="sADL::EndWriteStatement")
sADL_ReadStatement = Class(name="sADL::ReadStatement")
sADL_OrderElement = Class(name="sADL::OrderElement")
sADL_ValueTable = Class(name="sADL::ValueTable")
sADL_ValueRow = Class(name="sADL::ValueRow")
sADL_StartWriteStatement = Class(name="sADL::StartWriteStatement")
sADL_SadlClassOrPropertyDeclaration = Class(name="sADL::SadlClassOrPropertyDeclaration")
sADL_SadlSameAs = Class(name="sADL::SadlSameAs")
sADL_SadlDifferentFrom = Class(name="sADL::SadlDifferentFrom")
sADL_SadlDisjointClasses = Class(name="sADL::SadlDisjointClasses")
sADL_SadlNecessaryAndSufficient = Class(name="sADL::SadlNecessaryAndSufficient")
sADL_SadlIntersectionType = Class(name="sADL::SadlIntersectionType")
sADL_SadlSimpleTypeReference = Class(name="sADL::SadlSimpleTypeReference")
sADL_SadlPrimitiveDataType = Class(name="sADL::SadlPrimitiveDataType")
sADL_SadlTypeAssociation = Class(name="sADL::SadlTypeAssociation")
sADL_SadlNestedInstance = Class(name="sADL::SadlNestedInstance")
SadlInstance = Class(name="SadlInstance")
sADL_SadlUnionType = Class(name="sADL::SadlUnionType")
sADL_SadlIsInverseOf = Class(name="sADL::SadlIsInverseOf")
sADL_SadlIsTransitive = Class(name="sADL::SadlIsTransitive")
sADL_SadlIsSymmetrical = Class(name="sADL::SadlIsSymmetrical")
sADL_SadlIsAnnotation = Class(name="sADL::SadlIsAnnotation")
sADL_SadlDefaultValue = Class(name="sADL::SadlDefaultValue")
sADL_SadlIsFunctional = Class(name="sADL::SadlIsFunctional")
sADL_SadlRangeRestriction = Class(name="sADL::SadlRangeRestriction")
sADL_SadlCanOnlyBeOneOf = Class(name="sADL::SadlCanOnlyBeOneOf")
sADL_SadlUnaryExpression = Class(name="sADL::SadlUnaryExpression")
sADL_SadlNumberLiteral = Class(name="sADL::SadlNumberLiteral")
sADL_SadlStringLiteral = Class(name="sADL::SadlStringLiteral")
sADL_SadlBooleanLiteral = Class(name="sADL::SadlBooleanLiteral")
sADL_SadlConstantLiteral = Class(name="sADL::SadlConstantLiteral")
sADL_ExpressionStatement = Class(name="sADL::ExpressionStatement")
ExpressionScope = Class(name="ExpressionScope")
sADL_SadlMustBeOneOf = Class(name="sADL::SadlMustBeOneOf")
sADL_RuleStatement = Class(name="sADL::RuleStatement")
sADL_QueryStatement = Class(name="sADL::QueryStatement")
sADL_ConstructExpression = Class(name="sADL::ConstructExpression")
sADL_AskExpression = Class(name="sADL::AskExpression")
sADL_TestStatement = Class(name="sADL::TestStatement")
sADL_SelectExpression = Class(name="sADL::SelectExpression")
sADL_Sublist = Class(name="sADL::Sublist")
sADL_BinaryOperation = Class(name="sADL::BinaryOperation")
sADL_PropOfSubject = Class(name="sADL::PropOfSubject")
sADL_SubjHasProp = Class(name="sADL::SubjHasProp")
sADL_ElementInList = Class(name="sADL::ElementInList")
sADL_UnitExpression = Class(name="sADL::UnitExpression")
sADL_UnaryExpression = Class(name="sADL::UnaryExpression")
sADL_Declaration = Class(name="sADL::Declaration")
sADL_StringLiteral = Class(name="sADL::StringLiteral")
sADL_NumberLiteral = Class(name="sADL::NumberLiteral")
sADL_BooleanLiteral = Class(name="sADL::BooleanLiteral")
sADL_Constant = Class(name="sADL::Constant")
sADL_Name = Class(name="sADL::Name")
SadlResource = Class(name="SadlResource")

# sADL_SadlAnnotation class attributes and methods
sADL_SadlAnnotation_type: Property = Property(name="type", type=StringType)
sADL_SadlAnnotation_contents: Property = Property(name="contents", type=StringType)
sADL_SadlAnnotation.attributes={sADL_SadlAnnotation_contents, sADL_SadlAnnotation_type}

# sADL_SadlImport class attributes and methods
sADL_SadlImport_alias: Property = Property(name="alias", type=StringType)
sADL_SadlImport.attributes={sADL_SadlImport_alias}

# sADL_SadlModelElement class attributes and methods

# sADL_EquationStatement class attributes and methods

# SadlModelElement class attributes and methods

# AbstractSadlEquation class attributes and methods

# sADL_Expression class attributes and methods

# sADL_SadlModel class attributes and methods
sADL_SadlModel_baseUri: Property = Property(name="baseUri", type=StringType)
sADL_SadlModel_alias: Property = Property(name="alias", type=StringType)
sADL_SadlModel_version: Property = Property(name="version", type=StringType)
sADL_SadlModel.attributes={sADL_SadlModel_baseUri, sADL_SadlModel_version, sADL_SadlModel_alias}

# sADL_AbstractSadlEquation class attributes and methods
sADL_AbstractSadlEquation_unknown: Property = Property(name="unknown", type=StringType)
sADL_AbstractSadlEquation.attributes={sADL_AbstractSadlEquation_unknown}

# sADL_SadlResource class attributes and methods

# sADL_SadlParameterDeclaration class attributes and methods
sADL_SadlParameterDeclaration_unknown: Property = Property(name="unknown", type=StringType)
sADL_SadlParameterDeclaration_ellipsis: Property = Property(name="ellipsis", type=StringType)
sADL_SadlParameterDeclaration.attributes={sADL_SadlParameterDeclaration_ellipsis, sADL_SadlParameterDeclaration_unknown}

# sADL_SadlTypeReference class attributes and methods

# sADL_SadlStatement class attributes and methods

# sADL_SadlPropertyCondition class attributes and methods

# SadlTypeReference class attributes and methods

# sADL_ExternalEquationStatement class attributes and methods
sADL_ExternalEquationStatement_uri: Property = Property(name="uri", type=StringType)
sADL_ExternalEquationStatement_location: Property = Property(name="location", type=StringType)
sADL_ExternalEquationStatement.attributes={sADL_ExternalEquationStatement_location, sADL_ExternalEquationStatement_uri}

# sADL_SadlPropertyInitializer class attributes and methods

# sADL_EObject class attributes and methods

# sADL_SadlInstance class attributes and methods

# SadlStatement class attributes and methods

# sADL_SadlValueList class attributes and methods

# SadlExplicitValueLiteral class attributes and methods

# Expression class attributes and methods

# sADL_SadlCondition class attributes and methods

# sADL_SadlDataTypeFacet class attributes and methods
sADL_SadlDataTypeFacet_minInclusive: Property = Property(name="minInclusive", type=BooleanType)
sADL_SadlDataTypeFacet_min: Property = Property(name="min", type=StringType)
sADL_SadlDataTypeFacet_max: Property = Property(name="max", type=StringType)
sADL_SadlDataTypeFacet_maxInclusive: Property = Property(name="maxInclusive", type=BooleanType)
sADL_SadlDataTypeFacet_regex: Property = Property(name="regex", type=StringType)
sADL_SadlDataTypeFacet_len: Property = Property(name="len", type=StringType)
sADL_SadlDataTypeFacet_minlen: Property = Property(name="minlen", type=StringType)
sADL_SadlDataTypeFacet_maxlen: Property = Property(name="maxlen", type=StringType)
sADL_SadlDataTypeFacet_values: Property = Property(name="values", type=StringType)
sADL_SadlDataTypeFacet.attributes={sADL_SadlDataTypeFacet_len, sADL_SadlDataTypeFacet_max, sADL_SadlDataTypeFacet_minInclusive, sADL_SadlDataTypeFacet_min, sADL_SadlDataTypeFacet_minlen, sADL_SadlDataTypeFacet_maxlen, sADL_SadlDataTypeFacet_maxInclusive, sADL_SadlDataTypeFacet_regex, sADL_SadlDataTypeFacet_values}

# sADL_SadlProperty class attributes and methods
sADL_SadlProperty_primaryDeclaration: Property = Property(name="primaryDeclaration", type=BooleanType)
sADL_SadlProperty.attributes={sADL_SadlProperty_primaryDeclaration}

# sADL_SadlPropertyRestriction class attributes and methods

# SadlPropertyRestriction class attributes and methods

# sADL_SadlAllValuesCondition class attributes and methods

# SadlCondition class attributes and methods

# sADL_SadlHasValueCondition class attributes and methods

# sADL_SadlCardinalityCondition class attributes and methods
sADL_SadlCardinalityCondition_operator: Property = Property(name="operator", type=StringType)
sADL_SadlCardinalityCondition_cardinality: Property = Property(name="cardinality", type=StringType)
sADL_SadlCardinalityCondition.attributes={sADL_SadlCardinalityCondition_cardinality, sADL_SadlCardinalityCondition_operator}

# sADL_SadlExplicitValue class attributes and methods

# sADL_SadlExplicitValueLiteral class attributes and methods

# SadlExplicitValue class attributes and methods

# sADL_ExpressionScope class attributes and methods

# sADL_NamedStructureAnnotation class attributes and methods

# sADL_PrintStatement class attributes and methods
sADL_PrintStatement_displayString: Property = Property(name="displayString", type=StringType)
sADL_PrintStatement_model: Property = Property(name="model", type=StringType)
sADL_PrintStatement.attributes={sADL_PrintStatement_model, sADL_PrintStatement_displayString}

# sADL_ExplainStatement class attributes and methods

# sADL_EndWriteStatement class attributes and methods
sADL_EndWriteStatement_filename: Property = Property(name="filename", type=StringType)
sADL_EndWriteStatement.attributes={sADL_EndWriteStatement_filename}

# sADL_ReadStatement class attributes and methods
sADL_ReadStatement_filename: Property = Property(name="filename", type=StringType)
sADL_ReadStatement_templateFilename: Property = Property(name="templateFilename", type=StringType)
sADL_ReadStatement.attributes={sADL_ReadStatement_templateFilename, sADL_ReadStatement_filename}

# sADL_OrderElement class attributes and methods
sADL_OrderElement_desc: Property = Property(name="desc", type=BooleanType)
sADL_OrderElement.attributes={sADL_OrderElement_desc}

# sADL_ValueTable class attributes and methods

# sADL_ValueRow class attributes and methods

# sADL_StartWriteStatement class attributes and methods
sADL_StartWriteStatement_write: Property = Property(name="write", type=StringType)
sADL_StartWriteStatement_dataOnly: Property = Property(name="dataOnly", type=StringType)
sADL_StartWriteStatement.attributes={sADL_StartWriteStatement_write, sADL_StartWriteStatement_dataOnly}

# sADL_SadlClassOrPropertyDeclaration class attributes and methods

# sADL_SadlSameAs class attributes and methods
sADL_SadlSameAs_complement: Property = Property(name="complement", type=BooleanType)
sADL_SadlSameAs.attributes={sADL_SadlSameAs_complement}

# sADL_SadlDifferentFrom class attributes and methods
sADL_SadlDifferentFrom_complement: Property = Property(name="complement", type=BooleanType)
sADL_SadlDifferentFrom.attributes={sADL_SadlDifferentFrom_complement}

# sADL_SadlDisjointClasses class attributes and methods

# sADL_SadlNecessaryAndSufficient class attributes and methods

# sADL_SadlIntersectionType class attributes and methods

# sADL_SadlSimpleTypeReference class attributes and methods
sADL_SadlSimpleTypeReference_list: Property = Property(name="list", type=BooleanType)
sADL_SadlSimpleTypeReference.attributes={sADL_SadlSimpleTypeReference_list}

# sADL_SadlPrimitiveDataType class attributes and methods
sADL_SadlPrimitiveDataType_primitiveType: Property = Property(name="primitiveType", type=StringType)
sADL_SadlPrimitiveDataType_list: Property = Property(name="list", type=BooleanType)
sADL_SadlPrimitiveDataType.attributes={sADL_SadlPrimitiveDataType_list, sADL_SadlPrimitiveDataType_primitiveType}

# sADL_SadlTypeAssociation class attributes and methods

# sADL_SadlNestedInstance class attributes and methods
sADL_SadlNestedInstance_article: Property = Property(name="article", type=StringType)
sADL_SadlNestedInstance.attributes={sADL_SadlNestedInstance_article}

# SadlInstance class attributes and methods

# sADL_SadlUnionType class attributes and methods

# sADL_SadlIsInverseOf class attributes and methods

# sADL_SadlIsTransitive class attributes and methods

# sADL_SadlIsSymmetrical class attributes and methods

# sADL_SadlIsAnnotation class attributes and methods

# sADL_SadlDefaultValue class attributes and methods
sADL_SadlDefaultValue_level: Property = Property(name="level", type=IntegerType)
sADL_SadlDefaultValue.attributes={sADL_SadlDefaultValue_level}

# sADL_SadlIsFunctional class attributes and methods
sADL_SadlIsFunctional_inverse: Property = Property(name="inverse", type=BooleanType)
sADL_SadlIsFunctional.attributes={sADL_SadlIsFunctional_inverse}

# sADL_SadlRangeRestriction class attributes and methods
sADL_SadlRangeRestriction_singleValued: Property = Property(name="singleValued", type=BooleanType)
sADL_SadlRangeRestriction_typeonly: Property = Property(name="typeonly", type=StringType)
sADL_SadlRangeRestriction.attributes={sADL_SadlRangeRestriction_singleValued, sADL_SadlRangeRestriction_typeonly}

# sADL_SadlCanOnlyBeOneOf class attributes and methods

# sADL_SadlUnaryExpression class attributes and methods
sADL_SadlUnaryExpression_operator: Property = Property(name="operator", type=StringType)
sADL_SadlUnaryExpression.attributes={sADL_SadlUnaryExpression_operator}

# sADL_SadlNumberLiteral class attributes and methods
sADL_SadlNumberLiteral_literalNumber: Property = Property(name="literalNumber", type=StringType)
sADL_SadlNumberLiteral_unit: Property = Property(name="unit", type=StringType)
sADL_SadlNumberLiteral.attributes={sADL_SadlNumberLiteral_unit, sADL_SadlNumberLiteral_literalNumber}

# sADL_SadlStringLiteral class attributes and methods
sADL_SadlStringLiteral_literalString: Property = Property(name="literalString", type=StringType)
sADL_SadlStringLiteral.attributes={sADL_SadlStringLiteral_literalString}

# sADL_SadlBooleanLiteral class attributes and methods
sADL_SadlBooleanLiteral_truethy: Property = Property(name="truethy", type=BooleanType)
sADL_SadlBooleanLiteral.attributes={sADL_SadlBooleanLiteral_truethy}

# sADL_SadlConstantLiteral class attributes and methods
sADL_SadlConstantLiteral_term: Property = Property(name="term", type=StringType)
sADL_SadlConstantLiteral.attributes={sADL_SadlConstantLiteral_term}

# sADL_ExpressionStatement class attributes and methods
sADL_ExpressionStatement_evaluatesTo: Property = Property(name="evaluatesTo", type=StringType)
sADL_ExpressionStatement.attributes={sADL_ExpressionStatement_evaluatesTo}

# ExpressionScope class attributes and methods

# sADL_SadlMustBeOneOf class attributes and methods

# sADL_RuleStatement class attributes and methods

# sADL_QueryStatement class attributes and methods
sADL_QueryStatement_start: Property = Property(name="start", type=StringType)
sADL_QueryStatement.attributes={sADL_QueryStatement_start}

# sADL_ConstructExpression class attributes and methods

# sADL_AskExpression class attributes and methods

# sADL_TestStatement class attributes and methods

# sADL_SelectExpression class attributes and methods
sADL_SelectExpression_distinct: Property = Property(name="distinct", type=BooleanType)
sADL_SelectExpression_orderby: Property = Property(name="orderby", type=StringType)
sADL_SelectExpression.attributes={sADL_SelectExpression_distinct, sADL_SelectExpression_orderby}

# sADL_Sublist class attributes and methods

# sADL_BinaryOperation class attributes and methods
sADL_BinaryOperation_op: Property = Property(name="op", type=StringType)
sADL_BinaryOperation.attributes={sADL_BinaryOperation_op}

# sADL_PropOfSubject class attributes and methods
sADL_PropOfSubject_of: Property = Property(name="of", type=StringType)
sADL_PropOfSubject.attributes={sADL_PropOfSubject_of}

# sADL_SubjHasProp class attributes and methods
sADL_SubjHasProp_comma: Property = Property(name="comma", type=BooleanType)
sADL_SubjHasProp.attributes={sADL_SubjHasProp_comma}

# sADL_ElementInList class attributes and methods
sADL_ElementInList_before: Property = Property(name="before", type=BooleanType)
sADL_ElementInList_after: Property = Property(name="after", type=BooleanType)
sADL_ElementInList.attributes={sADL_ElementInList_after, sADL_ElementInList_before}

# sADL_UnitExpression class attributes and methods
sADL_UnitExpression_unit: Property = Property(name="unit", type=StringType)
sADL_UnitExpression.attributes={sADL_UnitExpression_unit}

# sADL_UnaryExpression class attributes and methods
sADL_UnaryExpression_op: Property = Property(name="op", type=StringType)
sADL_UnaryExpression.attributes={sADL_UnaryExpression_op}

# sADL_Declaration class attributes and methods
sADL_Declaration_ordinal: Property = Property(name="ordinal", type=StringType)
sADL_Declaration_len: Property = Property(name="len", type=StringType)
sADL_Declaration_maxlen: Property = Property(name="maxlen", type=StringType)
sADL_Declaration_article: Property = Property(name="article", type=StringType)
sADL_Declaration.attributes={sADL_Declaration_maxlen, sADL_Declaration_len, sADL_Declaration_article, sADL_Declaration_ordinal}

# sADL_StringLiteral class attributes and methods
sADL_StringLiteral_value: Property = Property(name="value", type=StringType)
sADL_StringLiteral.attributes={sADL_StringLiteral_value}

# sADL_NumberLiteral class attributes and methods
sADL_NumberLiteral_value: Property = Property(name="value", type=StringType)
sADL_NumberLiteral.attributes={sADL_NumberLiteral_value}

# sADL_BooleanLiteral class attributes and methods
sADL_BooleanLiteral_value: Property = Property(name="value", type=StringType)
sADL_BooleanLiteral.attributes={sADL_BooleanLiteral_value}

# sADL_Constant class attributes and methods
sADL_Constant_constant: Property = Property(name="constant", type=StringType)
sADL_Constant.attributes={sADL_Constant_constant}

# sADL_Name class attributes and methods
sADL_Name_function: Property = Property(name="function", type=BooleanType)
sADL_Name.attributes={sADL_Name_function}

# SadlResource class attributes and methods

# Relationships
annotations0: BinaryAssociation = BinaryAssociation(
    name="annotations0",
    ends={
        Property(name="sADL_SadlAnnotation", type=sADL_SadlModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlModel", type=sADL_SadlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="sADL_SadlImport", type=sADL_SadlModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlModel2", type=sADL_SadlImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="sADL_SadlModelElement", type=sADL_SadlModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlModel4", type=sADL_SadlModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedResource5: BinaryAssociation = BinaryAssociation(
    name="importedResource5",
    ends={
        Property(name="sADL_SadlModel7", type=sADL_SadlImport, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlImport6", type=sADL_SadlModel, multiplicity=Multiplicity(0, 1))
    }
)
body8: BinaryAssociation = BinaryAssociation(
    name="body8",
    ends={
        Property(name="sADL_Expression", type=sADL_EquationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_EquationStatement", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name9: BinaryAssociation = BinaryAssociation(
    name="name9",
    ends={
        Property(name="sADL_SadlResource", type=sADL_AbstractSadlEquation, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_AbstractSadlEquation", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter10: BinaryAssociation = BinaryAssociation(
    name="parameter10",
    ends={
        Property(name="sADL_SadlParameterDeclaration", type=sADL_AbstractSadlEquation, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_AbstractSadlEquation11", type=sADL_SadlParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType12: BinaryAssociation = BinaryAssociation(
    name="returnType12",
    ends={
        Property(name="sADL_SadlTypeReference", type=sADL_AbstractSadlEquation, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_AbstractSadlEquation13", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="sADL_SadlTypeReference16", type=sADL_SadlParameterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlParameterDeclaration15", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name17: BinaryAssociation = BinaryAssociation(
    name="name17",
    ends={
        Property(name="sADL_SadlResource19", type=sADL_SadlParameterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlParameterDeclaration18", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property20: BinaryAssociation = BinaryAssociation(
    name="property20",
    ends={
        Property(name="sADL_SadlResource21", type=sADL_SadlPropertyCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlPropertyCondition", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1))
    }
)
property24: BinaryAssociation = BinaryAssociation(
    name="property24",
    ends={
        Property(name="sADL_SadlResource25", type=sADL_SadlPropertyInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlPropertyInitializer", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1))
    }
)
value26: BinaryAssociation = BinaryAssociation(
    name="value26",
    ends={
        Property(name="sADL_EObject", type=sADL_SadlPropertyInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlPropertyInitializer27", type=sADL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="sADL_SadlResource30", type=sADL_SadlPropertyInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlPropertyInitializer29", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1))
    }
)
nameOrRef31: BinaryAssociation = BinaryAssociation(
    name="nameOrRef31",
    ends={
        Property(name="sADL_SadlResource32", type=sADL_SadlInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlInstance", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="sADL_SadlTypeReference35", type=sADL_SadlInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlInstance34", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listInitializer36: BinaryAssociation = BinaryAssociation(
    name="listInitializer36",
    ends={
        Property(name="sADL_SadlValueList", type=sADL_SadlInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlInstance37", type=sADL_SadlValueList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyInitializers38: BinaryAssociation = BinaryAssociation(
    name="propertyInitializers38",
    ends={
        Property(name="sADL_SadlPropertyInitializer40", type=sADL_SadlInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlInstance39", type=sADL_SadlPropertyInitializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance41: BinaryAssociation = BinaryAssociation(
    name="instance41",
    ends={
        Property(name="sADL_SadlResource43", type=sADL_SadlInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlInstance42", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond22: BinaryAssociation = BinaryAssociation(
    name="cond22",
    ends={
        Property(name="sADL_SadlCondition", type=sADL_SadlPropertyCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlPropertyCondition23", type=sADL_SadlCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations47: BinaryAssociation = BinaryAssociation(
    name="annotations47",
    ends={
        Property(name="sADL_SadlAnnotation49", type=sADL_SadlResource, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlResource48", type=sADL_SadlAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name45: BinaryAssociation = BinaryAssociation(
    name="name45",
    ends={
        Property(name="sADL_SadlResource46", type=sADL_SadlResource, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlResource44", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1))
    }
)
nameOrRef50: BinaryAssociation = BinaryAssociation(
    name="nameOrRef50",
    ends={
        Property(name="sADL_SadlResource51", type=sADL_SadlProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlProperty", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restrictions52: BinaryAssociation = BinaryAssociation(
    name="restrictions52",
    ends={
        Property(name="sADL_SadlPropertyRestriction", type=sADL_SadlProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlProperty53", type=sADL_SadlPropertyRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to57: BinaryAssociation = BinaryAssociation(
    name="to57",
    ends={
        Property(name="sADL_SadlTypeReference59", type=sADL_SadlProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlProperty58", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property60: BinaryAssociation = BinaryAssociation(
    name="property60",
    ends={
        Property(name="sADL_SadlResource62", type=sADL_SadlProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlProperty61", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameDeclarations63: BinaryAssociation = BinaryAssociation(
    name="nameDeclarations63",
    ends={
        Property(name="sADL_SadlResource65", type=sADL_SadlProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlProperty64", type=sADL_SadlResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type66: BinaryAssociation = BinaryAssociation(
    name="type66",
    ends={
        Property(name="sADL_SadlTypeReference67", type=sADL_SadlAllValuesCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlAllValuesCondition", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
facet68: BinaryAssociation = BinaryAssociation(
    name="facet68",
    ends={
        Property(name="sADL_SadlDataTypeFacet", type=sADL_SadlAllValuesCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlAllValuesCondition69", type=sADL_SadlDataTypeFacet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restriction70: BinaryAssociation = BinaryAssociation(
    name="restriction70",
    ends={
        Property(name="sADL_EObject71", type=sADL_SadlHasValueCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlHasValueCondition", type=sADL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from54: BinaryAssociation = BinaryAssociation(
    name="from54",
    ends={
        Property(name="sADL_SadlTypeReference56", type=sADL_SadlProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlProperty55", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
facet74: BinaryAssociation = BinaryAssociation(
    name="facet74",
    ends={
        Property(name="sADL_SadlDataTypeFacet76", type=sADL_SadlCardinalityCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlCardinalityCondition75", type=sADL_SadlDataTypeFacet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
explicitValues77: BinaryAssociation = BinaryAssociation(
    name="explicitValues77",
    ends={
        Property(name="sADL_SadlExplicitValue", type=sADL_SadlValueList, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlValueList78", type=sADL_SadlExplicitValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type79: BinaryAssociation = BinaryAssociation(
    name="type79",
    ends={
        Property(name="sADL_SadlResource80", type=sADL_NamedStructureAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_NamedStructureAnnotation", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents81: BinaryAssociation = BinaryAssociation(
    name="contents81",
    ends={
        Property(name="sADL_SadlExplicitValue83", type=sADL_NamedStructureAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_NamedStructureAnnotation82", type=sADL_SadlExplicitValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr84: BinaryAssociation = BinaryAssociation(
    name="expr84",
    ends={
        Property(name="sADL_Expression85", type=sADL_ExplainStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ExplainStatement", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type72: BinaryAssociation = BinaryAssociation(
    name="type72",
    ends={
        Property(name="sADL_SadlTypeReference73", type=sADL_SadlCardinalityCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlCardinalityCondition", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderBy89: BinaryAssociation = BinaryAssociation(
    name="orderBy89",
    ends={
        Property(name="sADL_SadlResource90", type=sADL_OrderElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_OrderElement", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueTable92: BinaryAssociation = BinaryAssociation(
    name="valueTable92",
    ends={
        Property(name="sADL_ValueTable", type=sADL_ValueTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ValueTable91", type=sADL_ValueTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
row93: BinaryAssociation = BinaryAssociation(
    name="row93",
    ends={
        Property(name="sADL_ValueRow", type=sADL_ValueTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ValueTable94", type=sADL_ValueRow, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rows95: BinaryAssociation = BinaryAssociation(
    name="rows95",
    ends={
        Property(name="sADL_ValueRow97", type=sADL_ValueTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ValueTable96", type=sADL_ValueRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rulename86: BinaryAssociation = BinaryAssociation(
    name="rulename86",
    ends={
        Property(name="sADL_SadlResource88", type=sADL_ExplainStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ExplainStatement87", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classOrProperty101: BinaryAssociation = BinaryAssociation(
    name="classOrProperty101",
    ends={
        Property(name="sADL_SadlResource102", type=sADL_SadlClassOrPropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlClassOrPropertyDeclaration", type=sADL_SadlResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superElement103: BinaryAssociation = BinaryAssociation(
    name="superElement103",
    ends={
        Property(name="sADL_SadlTypeReference105", type=sADL_SadlClassOrPropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlClassOrPropertyDeclaration104", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
facet106: BinaryAssociation = BinaryAssociation(
    name="facet106",
    ends={
        Property(name="sADL_SadlDataTypeFacet108", type=sADL_SadlClassOrPropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlClassOrPropertyDeclaration107", type=sADL_SadlDataTypeFacet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
describedBy109: BinaryAssociation = BinaryAssociation(
    name="describedBy109",
    ends={
        Property(name="sADL_SadlProperty111", type=sADL_SadlClassOrPropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlClassOrPropertyDeclaration110", type=sADL_SadlProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
restrictions112: BinaryAssociation = BinaryAssociation(
    name="restrictions112",
    ends={
        Property(name="sADL_SadlPropertyRestriction114", type=sADL_SadlClassOrPropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlClassOrPropertyDeclaration113", type=sADL_SadlPropertyRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameOrRef115: BinaryAssociation = BinaryAssociation(
    name="nameOrRef115",
    ends={
        Property(name="sADL_SadlResource116", type=sADL_SadlSameAs, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlSameAs", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sameAs117: BinaryAssociation = BinaryAssociation(
    name="sameAs117",
    ends={
        Property(name="sADL_SadlTypeReference119", type=sADL_SadlSameAs, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlSameAs118", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
explicitValues98: BinaryAssociation = BinaryAssociation(
    name="explicitValues98",
    ends={
        Property(name="sADL_Expression100", type=sADL_ValueRow, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ValueRow99", type=sADL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
notTheSameAs122: BinaryAssociation = BinaryAssociation(
    name="notTheSameAs122",
    ends={
        Property(name="sADL_SadlTypeReference124", type=sADL_SadlDifferentFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlDifferentFrom123", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types125: BinaryAssociation = BinaryAssociation(
    name="types125",
    ends={
        Property(name="sADL_SadlClassOrPropertyDeclaration127", type=sADL_SadlDifferentFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlDifferentFrom126", type=sADL_SadlClassOrPropertyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes128: BinaryAssociation = BinaryAssociation(
    name="classes128",
    ends={
        Property(name="sADL_SadlResource129", type=sADL_SadlDisjointClasses, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlDisjointClasses", type=sADL_SadlResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types130: BinaryAssociation = BinaryAssociation(
    name="types130",
    ends={
        Property(name="sADL_SadlClassOrPropertyDeclaration132", type=sADL_SadlDisjointClasses, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlDisjointClasses131", type=sADL_SadlClassOrPropertyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject133: BinaryAssociation = BinaryAssociation(
    name="subject133",
    ends={
        Property(name="sADL_SadlTypeReference134", type=sADL_SadlNecessaryAndSufficient, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlNecessaryAndSufficient", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object135: BinaryAssociation = BinaryAssociation(
    name="object135",
    ends={
        Property(name="sADL_SadlResource137", type=sADL_SadlNecessaryAndSufficient, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlNecessaryAndSufficient136", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propConditions138: BinaryAssociation = BinaryAssociation(
    name="propConditions138",
    ends={
        Property(name="sADL_SadlPropertyCondition140", type=sADL_SadlNecessaryAndSufficient, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlNecessaryAndSufficient139", type=sADL_SadlPropertyCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameOrRef120: BinaryAssociation = BinaryAssociation(
    name="nameOrRef120",
    ends={
        Property(name="sADL_SadlResource121", type=sADL_SadlDifferentFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlDifferentFrom", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left141: BinaryAssociation = BinaryAssociation(
    name="left141",
    ends={
        Property(name="sADL_SadlTypeReference142", type=sADL_SadlUnionType, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlUnionType", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right143: BinaryAssociation = BinaryAssociation(
    name="right143",
    ends={
        Property(name="sADL_SadlTypeReference145", type=sADL_SadlUnionType, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlUnionType144", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left146: BinaryAssociation = BinaryAssociation(
    name="left146",
    ends={
        Property(name="sADL_SadlTypeReference147", type=sADL_SadlIntersectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlIntersectionType", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right148: BinaryAssociation = BinaryAssociation(
    name="right148",
    ends={
        Property(name="sADL_SadlTypeReference150", type=sADL_SadlIntersectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlIntersectionType149", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type151: BinaryAssociation = BinaryAssociation(
    name="type151",
    ends={
        Property(name="sADL_SadlResource152", type=sADL_SadlSimpleTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlSimpleTypeReference", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1))
    }
)
domain153: BinaryAssociation = BinaryAssociation(
    name="domain153",
    ends={
        Property(name="sADL_SadlTypeReference154", type=sADL_SadlTypeAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlTypeAssociation", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
range155: BinaryAssociation = BinaryAssociation(
    name="range155",
    ends={
        Property(name="sADL_SadlTypeReference156", type=sADL_SadlRangeRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlRangeRestriction", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
facet157: BinaryAssociation = BinaryAssociation(
    name="facet157",
    ends={
        Property(name="sADL_SadlDataTypeFacet159", type=sADL_SadlRangeRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlRangeRestriction158", type=sADL_SadlDataTypeFacet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
otherProperty160: BinaryAssociation = BinaryAssociation(
    name="otherProperty160",
    ends={
        Property(name="sADL_SadlResource161", type=sADL_SadlIsInverseOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlIsInverseOf", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1))
    }
)
defValue162: BinaryAssociation = BinaryAssociation(
    name="defValue162",
    ends={
        Property(name="sADL_SadlExplicitValue163", type=sADL_SadlDefaultValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlDefaultValue", type=sADL_SadlExplicitValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values164: BinaryAssociation = BinaryAssociation(
    name="values164",
    ends={
        Property(name="sADL_SadlMustBeOneOf", type=sADL_SadlExplicitValue, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="sADL_SadlExplicitValue165", type=sADL_SadlMustBeOneOf, multiplicity=Multiplicity(1, 1))
    }
)
values166: BinaryAssociation = BinaryAssociation(
    name="values166",
    ends={
        Property(name="sADL_SadlExplicitValue167", type=sADL_SadlCanOnlyBeOneOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlCanOnlyBeOneOf", type=sADL_SadlExplicitValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value168: BinaryAssociation = BinaryAssociation(
    name="value168",
    ends={
        Property(name="sADL_SadlExplicitValueLiteral", type=sADL_SadlUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SadlUnaryExpression", type=sADL_SadlExplicitValueLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr169: BinaryAssociation = BinaryAssociation(
    name="expr169",
    ends={
        Property(name="sADL_Expression170", type=sADL_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ExpressionStatement", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name171: BinaryAssociation = BinaryAssociation(
    name="name171",
    ends={
        Property(name="sADL_SadlResource172", type=sADL_RuleStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_RuleStatement", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations173: BinaryAssociation = BinaryAssociation(
    name="annotations173",
    ends={
        Property(name="sADL_NamedStructureAnnotation175", type=sADL_RuleStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_RuleStatement174", type=sADL_NamedStructureAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifs176: BinaryAssociation = BinaryAssociation(
    name="ifs176",
    ends={
        Property(name="sADL_Expression178", type=sADL_RuleStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_RuleStatement177", type=sADL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thens179: BinaryAssociation = BinaryAssociation(
    name="thens179",
    ends={
        Property(name="sADL_Expression181", type=sADL_RuleStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_RuleStatement180", type=sADL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name182: BinaryAssociation = BinaryAssociation(
    name="name182",
    ends={
        Property(name="sADL_SadlResource183", type=sADL_QueryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_QueryStatement", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations184: BinaryAssociation = BinaryAssociation(
    name="annotations184",
    ends={
        Property(name="sADL_NamedStructureAnnotation186", type=sADL_QueryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_QueryStatement185", type=sADL_NamedStructureAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr187: BinaryAssociation = BinaryAssociation(
    name="expr187",
    ends={
        Property(name="sADL_Expression189", type=sADL_QueryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_QueryStatement188", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pred192: BinaryAssociation = BinaryAssociation(
    name="pred192",
    ends={
        Property(name="sADL_SadlResource194", type=sADL_ConstructExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ConstructExpression193", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
obj195: BinaryAssociation = BinaryAssociation(
    name="obj195",
    ends={
        Property(name="sADL_SadlResource197", type=sADL_ConstructExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ConstructExpression196", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereExpression198: BinaryAssociation = BinaryAssociation(
    name="whereExpression198",
    ends={
        Property(name="sADL_Expression200", type=sADL_ConstructExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ConstructExpression199", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereExpression201: BinaryAssociation = BinaryAssociation(
    name="whereExpression201",
    ends={
        Property(name="sADL_Expression202", type=sADL_AskExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_AskExpression", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tests203: BinaryAssociation = BinaryAssociation(
    name="tests203",
    ends={
        Property(name="sADL_Expression204", type=sADL_TestStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_TestStatement", type=sADL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectFrom205: BinaryAssociation = BinaryAssociation(
    name="selectFrom205",
    ends={
        Property(name="sADL_SadlResource206", type=sADL_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SelectExpression", type=sADL_SadlResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereExpression207: BinaryAssociation = BinaryAssociation(
    name="whereExpression207",
    ends={
        Property(name="sADL_Expression209", type=sADL_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SelectExpression208", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subj190: BinaryAssociation = BinaryAssociation(
    name="subj190",
    ends={
        Property(name="sADL_SadlResource191", type=sADL_ConstructExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ConstructExpression", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list213: BinaryAssociation = BinaryAssociation(
    name="list213",
    ends={
        Property(name="sADL_Expression214", type=sADL_Sublist, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_Sublist", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where215: BinaryAssociation = BinaryAssociation(
    name="where215",
    ends={
        Property(name="sADL_Expression217", type=sADL_Sublist, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_Sublist216", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left218: BinaryAssociation = BinaryAssociation(
    name="left218",
    ends={
        Property(name="sADL_Expression219", type=sADL_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_BinaryOperation", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right220: BinaryAssociation = BinaryAssociation(
    name="right220",
    ends={
        Property(name="sADL_Expression222", type=sADL_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_BinaryOperation221", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left223: BinaryAssociation = BinaryAssociation(
    name="left223",
    ends={
        Property(name="sADL_Expression224", type=sADL_PropOfSubject, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_PropOfSubject", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right225: BinaryAssociation = BinaryAssociation(
    name="right225",
    ends={
        Property(name="sADL_Expression227", type=sADL_PropOfSubject, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_PropOfSubject226", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderList210: BinaryAssociation = BinaryAssociation(
    name="orderList210",
    ends={
        Property(name="sADL_OrderElement212", type=sADL_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SelectExpression211", type=sADL_OrderElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prop230: BinaryAssociation = BinaryAssociation(
    name="prop230",
    ends={
        Property(name="sADL_SadlResource232", type=sADL_SubjHasProp, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SubjHasProp231", type=sADL_SadlResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right233: BinaryAssociation = BinaryAssociation(
    name="right233",
    ends={
        Property(name="sADL_Expression235", type=sADL_SubjHasProp, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SubjHasProp234", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element236: BinaryAssociation = BinaryAssociation(
    name="element236",
    ends={
        Property(name="sADL_Expression237", type=sADL_ElementInList, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_ElementInList", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left238: BinaryAssociation = BinaryAssociation(
    name="left238",
    ends={
        Property(name="sADL_Expression239", type=sADL_UnitExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_UnitExpression", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr240: BinaryAssociation = BinaryAssociation(
    name="expr240",
    ends={
        Property(name="sADL_Expression241", type=sADL_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_UnaryExpression", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left228: BinaryAssociation = BinaryAssociation(
    name="left228",
    ends={
        Property(name="sADL_Expression229", type=sADL_SubjHasProp, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_SubjHasProp", type=sADL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type242: BinaryAssociation = BinaryAssociation(
    name="type242",
    ends={
        Property(name="sADL_SadlTypeReference243", type=sADL_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_Declaration", type=sADL_SadlTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arglist244: BinaryAssociation = BinaryAssociation(
    name="arglist244",
    ends={
        Property(name="sADL_Expression246", type=sADL_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_Declaration245", type=sADL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arglist247: BinaryAssociation = BinaryAssociation(
    name="arglist247",
    ends={
        Property(name="sADL_Expression248", type=sADL_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="sADL_Name", type=sADL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sADL_EquationStatement_SadlModelElement = Generalization(general=SadlModelElement, specific=sADL_EquationStatement)
gen_sADL_EquationStatement_AbstractSadlEquation = Generalization(general=AbstractSadlEquation, specific=sADL_EquationStatement)
gen_sADL_SadlStatement_SadlModelElement = Generalization(general=SadlModelElement, specific=sADL_SadlStatement)
gen_sADL_SadlPropertyCondition_SadlTypeReference = Generalization(general=SadlTypeReference, specific=sADL_SadlPropertyCondition)
gen_sADL_ExternalEquationStatement_SadlModelElement = Generalization(general=SadlModelElement, specific=sADL_ExternalEquationStatement)
gen_sADL_ExternalEquationStatement_AbstractSadlEquation = Generalization(general=AbstractSadlEquation, specific=sADL_ExternalEquationStatement)
gen_sADL_SadlInstance_SadlStatement = Generalization(general=SadlStatement, specific=sADL_SadlInstance)
gen_sADL_SadlResource_SadlStatement = Generalization(general=SadlStatement, specific=sADL_SadlResource)
gen_sADL_SadlResource_SadlExplicitValueLiteral = Generalization(general=SadlExplicitValueLiteral, specific=sADL_SadlResource)
gen_sADL_SadlResource_Expression = Generalization(general=Expression, specific=sADL_SadlResource)
gen_sADL_SadlTypeReference_SadlStatement = Generalization(general=SadlStatement, specific=sADL_SadlTypeReference)
gen_sADL_SadlProperty_SadlStatement = Generalization(general=SadlStatement, specific=sADL_SadlProperty)
gen_sADL_SadlCondition_SadlPropertyRestriction = Generalization(general=SadlPropertyRestriction, specific=sADL_SadlCondition)
gen_sADL_SadlAllValuesCondition_SadlCondition = Generalization(general=SadlCondition, specific=sADL_SadlAllValuesCondition)
gen_sADL_SadlHasValueCondition_SadlCondition = Generalization(general=SadlCondition, specific=sADL_SadlHasValueCondition)
gen_sADL_SadlCardinalityCondition_SadlCondition = Generalization(general=SadlCondition, specific=sADL_SadlCardinalityCondition)
gen_sADL_SadlExplicitValueLiteral_SadlExplicitValue = Generalization(general=SadlExplicitValue, specific=sADL_SadlExplicitValueLiteral)
gen_sADL_SadlValueList_SadlExplicitValueLiteral = Generalization(general=SadlExplicitValueLiteral, specific=sADL_SadlValueList)
gen_sADL_ExpressionScope_SadlModelElement = Generalization(general=SadlModelElement, specific=sADL_ExpressionScope)
gen_sADL_PrintStatement_SadlModelElement = Generalization(general=SadlModelElement, specific=sADL_PrintStatement)
gen_sADL_ExplainStatement_SadlModelElement = Generalization(general=SadlModelElement, specific=sADL_ExplainStatement)
gen_sADL_StartWriteStatement_SadlModelElement = Generalization(general=SadlModelElement, specific=sADL_StartWriteStatement)
gen_sADL_EndWriteStatement_SadlModelElement = Generalization(general=SadlModelElement, specific=sADL_EndWriteStatement)
gen_sADL_ReadStatement_SadlModelElement = Generalization(general=SadlModelElement, specific=sADL_ReadStatement)
gen_sADL_ValueTable_Expression = Generalization(general=Expression, specific=sADL_ValueTable)
gen_sADL_SadlClassOrPropertyDeclaration_SadlStatement = Generalization(general=SadlStatement, specific=sADL_SadlClassOrPropertyDeclaration)
gen_sADL_SadlSameAs_SadlStatement = Generalization(general=SadlStatement, specific=sADL_SadlSameAs)
gen_sADL_SadlDifferentFrom_SadlStatement = Generalization(general=SadlStatement, specific=sADL_SadlDifferentFrom)
gen_sADL_SadlDisjointClasses_SadlStatement = Generalization(general=SadlStatement, specific=sADL_SadlDisjointClasses)
gen_sADL_SadlNecessaryAndSufficient_SadlStatement = Generalization(general=SadlStatement, specific=sADL_SadlNecessaryAndSufficient)
gen_sADL_SadlIntersectionType_SadlTypeReference = Generalization(general=SadlTypeReference, specific=sADL_SadlIntersectionType)
gen_sADL_SadlSimpleTypeReference_SadlTypeReference = Generalization(general=SadlTypeReference, specific=sADL_SadlSimpleTypeReference)
gen_sADL_SadlPrimitiveDataType_SadlTypeReference = Generalization(general=SadlTypeReference, specific=sADL_SadlPrimitiveDataType)
gen_sADL_SadlTypeAssociation_SadlPropertyRestriction = Generalization(general=SadlPropertyRestriction, specific=sADL_SadlTypeAssociation)
gen_sADL_SadlNestedInstance_SadlInstance = Generalization(general=SadlInstance, specific=sADL_SadlNestedInstance)
gen_sADL_SadlUnionType_SadlTypeReference = Generalization(general=SadlTypeReference, specific=sADL_SadlUnionType)
gen_sADL_SadlIsInverseOf_SadlPropertyRestriction = Generalization(general=SadlPropertyRestriction, specific=sADL_SadlIsInverseOf)
gen_sADL_SadlIsTransitive_SadlPropertyRestriction = Generalization(general=SadlPropertyRestriction, specific=sADL_SadlIsTransitive)
gen_sADL_SadlIsSymmetrical_SadlPropertyRestriction = Generalization(general=SadlPropertyRestriction, specific=sADL_SadlIsSymmetrical)
gen_sADL_SadlIsAnnotation_SadlPropertyRestriction = Generalization(general=SadlPropertyRestriction, specific=sADL_SadlIsAnnotation)
gen_sADL_SadlDefaultValue_SadlPropertyRestriction = Generalization(general=SadlPropertyRestriction, specific=sADL_SadlDefaultValue)
gen_sADL_SadlIsFunctional_SadlPropertyRestriction = Generalization(general=SadlPropertyRestriction, specific=sADL_SadlIsFunctional)
gen_sADL_SadlRangeRestriction_SadlPropertyRestriction = Generalization(general=SadlPropertyRestriction, specific=sADL_SadlRangeRestriction)
gen_sADL_SadlCanOnlyBeOneOf_SadlPropertyRestriction = Generalization(general=SadlPropertyRestriction, specific=sADL_SadlCanOnlyBeOneOf)
gen_sADL_SadlUnaryExpression_SadlExplicitValue = Generalization(general=SadlExplicitValue, specific=sADL_SadlUnaryExpression)
gen_sADL_SadlNumberLiteral_SadlExplicitValueLiteral = Generalization(general=SadlExplicitValueLiteral, specific=sADL_SadlNumberLiteral)
gen_sADL_SadlStringLiteral_SadlExplicitValueLiteral = Generalization(general=SadlExplicitValueLiteral, specific=sADL_SadlStringLiteral)
gen_sADL_SadlBooleanLiteral_SadlExplicitValueLiteral = Generalization(general=SadlExplicitValueLiteral, specific=sADL_SadlBooleanLiteral)
gen_sADL_SadlConstantLiteral_SadlExplicitValueLiteral = Generalization(general=SadlExplicitValueLiteral, specific=sADL_SadlConstantLiteral)
gen_sADL_ExpressionStatement_ExpressionScope = Generalization(general=ExpressionScope, specific=sADL_ExpressionStatement)
gen_sADL_SadlMustBeOneOf_SadlPropertyRestriction = Generalization(general=SadlPropertyRestriction, specific=sADL_SadlMustBeOneOf)
gen_sADL_RuleStatement_ExpressionScope = Generalization(general=ExpressionScope, specific=sADL_RuleStatement)
gen_sADL_QueryStatement_ExpressionScope = Generalization(general=ExpressionScope, specific=sADL_QueryStatement)
gen_sADL_ConstructExpression_Expression = Generalization(general=Expression, specific=sADL_ConstructExpression)
gen_sADL_AskExpression_Expression = Generalization(general=Expression, specific=sADL_AskExpression)
gen_sADL_TestStatement_ExpressionScope = Generalization(general=ExpressionScope, specific=sADL_TestStatement)
gen_sADL_SelectExpression_Expression = Generalization(general=Expression, specific=sADL_SelectExpression)
gen_sADL_Sublist_Expression = Generalization(general=Expression, specific=sADL_Sublist)
gen_sADL_BinaryOperation_Expression = Generalization(general=Expression, specific=sADL_BinaryOperation)
gen_sADL_PropOfSubject_Expression = Generalization(general=Expression, specific=sADL_PropOfSubject)
gen_sADL_SubjHasProp_Expression = Generalization(general=Expression, specific=sADL_SubjHasProp)
gen_sADL_ElementInList_Expression = Generalization(general=Expression, specific=sADL_ElementInList)
gen_sADL_UnitExpression_Expression = Generalization(general=Expression, specific=sADL_UnitExpression)
gen_sADL_UnaryExpression_Expression = Generalization(general=Expression, specific=sADL_UnaryExpression)
gen_sADL_StringLiteral_Expression = Generalization(general=Expression, specific=sADL_StringLiteral)
gen_sADL_NumberLiteral_Expression = Generalization(general=Expression, specific=sADL_NumberLiteral)
gen_sADL_BooleanLiteral_Expression = Generalization(general=Expression, specific=sADL_BooleanLiteral)
gen_sADL_Constant_Expression = Generalization(general=Expression, specific=sADL_Constant)
gen_sADL_Name_SadlResource = Generalization(general=SadlResource, specific=sADL_Name)
gen_sADL_Declaration_Expression = Generalization(general=Expression, specific=sADL_Declaration)

# Domain Model
domain_model = DomainModel(
    name="sADL",
    types={sADL_SadlAnnotation, sADL_SadlImport, sADL_SadlModelElement, sADL_EquationStatement, SadlModelElement, AbstractSadlEquation, sADL_Expression, sADL_SadlModel, sADL_AbstractSadlEquation, sADL_SadlResource, sADL_SadlParameterDeclaration, sADL_SadlTypeReference, sADL_SadlStatement, sADL_SadlPropertyCondition, SadlTypeReference, sADL_ExternalEquationStatement, sADL_SadlPropertyInitializer, sADL_EObject, sADL_SadlInstance, SadlStatement, sADL_SadlValueList, SadlExplicitValueLiteral, Expression, sADL_SadlCondition, sADL_SadlDataTypeFacet, sADL_SadlProperty, sADL_SadlPropertyRestriction, SadlPropertyRestriction, sADL_SadlAllValuesCondition, SadlCondition, sADL_SadlHasValueCondition, sADL_SadlCardinalityCondition, sADL_SadlExplicitValue, sADL_SadlExplicitValueLiteral, SadlExplicitValue, sADL_ExpressionScope, sADL_NamedStructureAnnotation, sADL_PrintStatement, sADL_ExplainStatement, sADL_EndWriteStatement, sADL_ReadStatement, sADL_OrderElement, sADL_ValueTable, sADL_ValueRow, sADL_StartWriteStatement, sADL_SadlClassOrPropertyDeclaration, sADL_SadlSameAs, sADL_SadlDifferentFrom, sADL_SadlDisjointClasses, sADL_SadlNecessaryAndSufficient, sADL_SadlIntersectionType, sADL_SadlSimpleTypeReference, sADL_SadlPrimitiveDataType, sADL_SadlTypeAssociation, sADL_SadlNestedInstance, SadlInstance, sADL_SadlUnionType, sADL_SadlIsInverseOf, sADL_SadlIsTransitive, sADL_SadlIsSymmetrical, sADL_SadlIsAnnotation, sADL_SadlDefaultValue, sADL_SadlIsFunctional, sADL_SadlRangeRestriction, sADL_SadlCanOnlyBeOneOf, sADL_SadlUnaryExpression, sADL_SadlNumberLiteral, sADL_SadlStringLiteral, sADL_SadlBooleanLiteral, sADL_SadlConstantLiteral, sADL_ExpressionStatement, ExpressionScope, sADL_SadlMustBeOneOf, sADL_RuleStatement, sADL_QueryStatement, sADL_ConstructExpression, sADL_AskExpression, sADL_TestStatement, sADL_SelectExpression, sADL_Sublist, sADL_BinaryOperation, sADL_PropOfSubject, sADL_SubjHasProp, sADL_ElementInList, sADL_UnitExpression, sADL_UnaryExpression, sADL_Declaration, sADL_StringLiteral, sADL_NumberLiteral, sADL_BooleanLiteral, sADL_Constant, sADL_Name, SadlResource, SadlDataType},
    associations={annotations0, imports1, elements3, importedResource5, body8, name9, parameter10, returnType12, type14, name17, property20, property24, value26, type28, nameOrRef31, type33, listInitializer36, propertyInitializers38, instance41, cond22, annotations47, name45, nameOrRef50, restrictions52, to57, property60, nameDeclarations63, type66, facet68, restriction70, from54, facet74, explicitValues77, type79, contents81, expr84, type72, orderBy89, valueTable92, row93, rows95, rulename86, classOrProperty101, superElement103, facet106, describedBy109, restrictions112, nameOrRef115, sameAs117, explicitValues98, notTheSameAs122, types125, classes128, types130, subject133, object135, propConditions138, nameOrRef120, left141, right143, left146, right148, type151, domain153, range155, facet157, otherProperty160, defValue162, values164, values166, value168, expr169, name171, annotations173, ifs176, thens179, name182, annotations184, expr187, pred192, obj195, whereExpression198, whereExpression201, tests203, selectFrom205, whereExpression207, subj190, list213, where215, left218, right220, left223, right225, orderList210, prop230, right233, element236, left238, expr240, left228, type242, arglist244, arglist247},
    generalizations={gen_sADL_EquationStatement_SadlModelElement, gen_sADL_EquationStatement_AbstractSadlEquation, gen_sADL_SadlStatement_SadlModelElement, gen_sADL_SadlPropertyCondition_SadlTypeReference, gen_sADL_ExternalEquationStatement_SadlModelElement, gen_sADL_ExternalEquationStatement_AbstractSadlEquation, gen_sADL_SadlInstance_SadlStatement, gen_sADL_SadlResource_SadlStatement, gen_sADL_SadlResource_SadlExplicitValueLiteral, gen_sADL_SadlResource_Expression, gen_sADL_SadlTypeReference_SadlStatement, gen_sADL_SadlProperty_SadlStatement, gen_sADL_SadlCondition_SadlPropertyRestriction, gen_sADL_SadlAllValuesCondition_SadlCondition, gen_sADL_SadlHasValueCondition_SadlCondition, gen_sADL_SadlCardinalityCondition_SadlCondition, gen_sADL_SadlExplicitValueLiteral_SadlExplicitValue, gen_sADL_SadlValueList_SadlExplicitValueLiteral, gen_sADL_ExpressionScope_SadlModelElement, gen_sADL_PrintStatement_SadlModelElement, gen_sADL_ExplainStatement_SadlModelElement, gen_sADL_StartWriteStatement_SadlModelElement, gen_sADL_EndWriteStatement_SadlModelElement, gen_sADL_ReadStatement_SadlModelElement, gen_sADL_ValueTable_Expression, gen_sADL_SadlClassOrPropertyDeclaration_SadlStatement, gen_sADL_SadlSameAs_SadlStatement, gen_sADL_SadlDifferentFrom_SadlStatement, gen_sADL_SadlDisjointClasses_SadlStatement, gen_sADL_SadlNecessaryAndSufficient_SadlStatement, gen_sADL_SadlIntersectionType_SadlTypeReference, gen_sADL_SadlSimpleTypeReference_SadlTypeReference, gen_sADL_SadlPrimitiveDataType_SadlTypeReference, gen_sADL_SadlTypeAssociation_SadlPropertyRestriction, gen_sADL_SadlNestedInstance_SadlInstance, gen_sADL_SadlUnionType_SadlTypeReference, gen_sADL_SadlIsInverseOf_SadlPropertyRestriction, gen_sADL_SadlIsTransitive_SadlPropertyRestriction, gen_sADL_SadlIsSymmetrical_SadlPropertyRestriction, gen_sADL_SadlIsAnnotation_SadlPropertyRestriction, gen_sADL_SadlDefaultValue_SadlPropertyRestriction, gen_sADL_SadlIsFunctional_SadlPropertyRestriction, gen_sADL_SadlRangeRestriction_SadlPropertyRestriction, gen_sADL_SadlCanOnlyBeOneOf_SadlPropertyRestriction, gen_sADL_SadlUnaryExpression_SadlExplicitValue, gen_sADL_SadlNumberLiteral_SadlExplicitValueLiteral, gen_sADL_SadlStringLiteral_SadlExplicitValueLiteral, gen_sADL_SadlBooleanLiteral_SadlExplicitValueLiteral, gen_sADL_SadlConstantLiteral_SadlExplicitValueLiteral, gen_sADL_ExpressionStatement_ExpressionScope, gen_sADL_SadlMustBeOneOf_SadlPropertyRestriction, gen_sADL_RuleStatement_ExpressionScope, gen_sADL_QueryStatement_ExpressionScope, gen_sADL_ConstructExpression_Expression, gen_sADL_AskExpression_Expression, gen_sADL_TestStatement_ExpressionScope, gen_sADL_SelectExpression_Expression, gen_sADL_Sublist_Expression, gen_sADL_BinaryOperation_Expression, gen_sADL_PropOfSubject_Expression, gen_sADL_SubjHasProp_Expression, gen_sADL_ElementInList_Expression, gen_sADL_UnitExpression_Expression, gen_sADL_UnaryExpression_Expression, gen_sADL_StringLiteral_Expression, gen_sADL_NumberLiteral_Expression, gen_sADL_BooleanLiteral_Expression, gen_sADL_Constant_Expression, gen_sADL_Name_SadlResource, gen_sADL_Declaration_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)