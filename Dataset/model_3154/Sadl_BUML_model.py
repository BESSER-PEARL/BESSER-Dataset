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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="gMonthDay"),
			EnumerationLiteral(name="gDay"),
			EnumerationLiteral(name="gMonth"),
			EnumerationLiteral(name="hexBinary"),
			EnumerationLiteral(name="base64Binary"),
			EnumerationLiteral(name="anyURI"),
			EnumerationLiteral(name="data"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="decimal"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="duration"),
			EnumerationLiteral(name="dateTime"),
			EnumerationLiteral(name="time"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="gYearMonth"),
			EnumerationLiteral(name="gYear")
    }
)

# Classes
sadl_Model = Class(name="sadl::Model")
sadl_ModelName = Class(name="sadl::ModelName")
sadl_Statement = Class(name="sadl::Statement")
ModelElement = Class(name="ModelElement")
sadl_ResourceName = Class(name="sadl::ResourceName")
sadl_Import = Class(name="sadl::Import")
sadl_ModelElement = Class(name="sadl::ModelElement")
sadl_ContentList = Class(name="sadl::ContentList")
sadl_ExistingResourceList = Class(name="sadl::ExistingResourceList")
sadl_ResourceIdentifier = Class(name="sadl::ResourceIdentifier")
sadl_ResourceBySetOp = Class(name="sadl::ResourceBySetOp")
sadl_ResourceList = Class(name="sadl::ResourceList")
sadl_LiteralList = Class(name="sadl::LiteralList")
sadl_LiteralValue = Class(name="sadl::LiteralValue")
sadl_ResourceByName = Class(name="sadl::ResourceByName")
ResourceIdentifier = Class(name="ResourceIdentifier")
sadl_UnionResource = Class(name="sadl::UnionResource")
ResourceBySetOp = Class(name="ResourceBySetOp")
sadl_IntersectionResource = Class(name="sadl::IntersectionResource")
sadl_ClassDeclaration = Class(name="sadl::ClassDeclaration")
Statement = Class(name="Statement")
sadl_EnumeratedInstances = Class(name="sadl::EnumeratedInstances")
sadl_AddlClassInfo = Class(name="sadl::AddlClassInfo")
sadl_ResourceByRestriction = Class(name="sadl::ResourceByRestriction")
sadl_Condition = Class(name="sadl::Condition")
sadl_Range = Class(name="sadl::Range")
sadl_RangeType = Class(name="sadl::RangeType")
sadl_UserDefinedDataType = Class(name="sadl::UserDefinedDataType")
sadl_DataTypeRestriction = Class(name="sadl::DataTypeRestriction")
sadl_Facets = Class(name="sadl::Facets")
sadl_EquivalentConcepts = Class(name="sadl::EquivalentConcepts")
sadl_ComplementOfClass = Class(name="sadl::ComplementOfClass")
sadl_DisjointClasses = Class(name="sadl::DisjointClasses")
sadl_AllValuesFrom = Class(name="sadl::AllValuesFrom")
sadl_PropertyOfClass = Class(name="sadl::PropertyOfClass")
sadl_AllValuesCondition = Class(name="sadl::AllValuesCondition")
sadl_HasValue = Class(name="sadl::HasValue")
sadl_SomeValuesFrom = Class(name="sadl::SomeValuesFrom")
sadl_SomeValuesCondition = Class(name="sadl::SomeValuesCondition")
sadl_Cardinality = Class(name="sadl::Cardinality")
sadl_CardCondition = Class(name="sadl::CardCondition")
sadl_HasValueCondition = Class(name="sadl::HasValueCondition")
sadl_MaxCardinality = Class(name="sadl::MaxCardinality")
sadl_MaxCardCondition = Class(name="sadl::MaxCardCondition")
sadl_MinCardinality = Class(name="sadl::MinCardinality")
sadl_MinCardCondition = Class(name="sadl::MinCardCondition")
sadl_EObject = Class(name="sadl::EObject")
sadl_EnumeratedAllAndSomeValuesFrom = Class(name="sadl::EnumeratedAllAndSomeValuesFrom")
sadl_DefaultValue = Class(name="sadl::DefaultValue")
Condition = Class(name="Condition")
sadl_EnumeratedAllValuesFrom = Class(name="sadl::EnumeratedAllValuesFrom")
sadl_ExplicitValue = Class(name="sadl::ExplicitValue")
sadl_PropertyDeclaration = Class(name="sadl::PropertyDeclaration")
sadl_AdditionalPropertyInfo = Class(name="sadl::AdditionalPropertyInfo")
sadl_NecessaryAndSufficient = Class(name="sadl::NecessaryAndSufficient")
sadl_TypedBNode = Class(name="sadl::TypedBNode")
sadl_IsInverseOf = Class(name="sadl::IsInverseOf")
sadl_TransitiveProperty = Class(name="sadl::TransitiveProperty")
sadl_InverseProperty = Class(name="sadl::InverseProperty")
sadl_FunctionalProperty = Class(name="sadl::FunctionalProperty")
sadl_InverseFunctionalProperty = Class(name="sadl::InverseFunctionalProperty")
sadl_SymmetricalProperty = Class(name="sadl::SymmetricalProperty")
sadl_PropValPartialTriple = Class(name="sadl::PropValPartialTriple")
sadl_InstanceDifferentFrom = Class(name="sadl::InstanceDifferentFrom")
sadl_InstanceDeclarationStatement = Class(name="sadl::InstanceDeclarationStatement")
sadl_InstanceDeclaration = Class(name="sadl::InstanceDeclaration")
InstanceDeclarationStatement = Class(name="InstanceDeclarationStatement")
EmbeddedInstanceDeclaration = Class(name="EmbeddedInstanceDeclaration")
sadl_TypeDeclaration = Class(name="sadl::TypeDeclaration")
sadl_ExistingInstanceAttribution = Class(name="sadl::ExistingInstanceAttribution")
sadl_OfPatternReturningValues = Class(name="sadl::OfPatternReturningValues")
sadl_Object = Class(name="sadl::Object")
sadl_InstancesAllDifferent = Class(name="sadl::InstancesAllDifferent")
sadl_OfPhrase = Class(name="sadl::OfPhrase")
sadl_WithChain = Class(name="sadl::WithChain")
sadl_WithPhrase = Class(name="sadl::WithPhrase")
sadl_VariableList = Class(name="sadl::VariableList")
sadl_Rule = Class(name="sadl::Rule")
sadl_EmbeddedInstanceDeclaration = Class(name="sadl::EmbeddedInstanceDeclaration")
sadl_MergedTriples = Class(name="sadl::MergedTriples")
GraphPattern = Class(name="GraphPattern")
sadl_Query = Class(name="sadl::Query")
sadl_Expression = Class(name="sadl::Expression")
sadl_Test = Class(name="sadl::Test")
sadl_Expr = Class(name="sadl::Expr")
sadl_Display = Class(name="sadl::Display")
sadl_Explanation = Class(name="sadl::Explanation")
sadl_ElementSet = Class(name="sadl::ElementSet")
Expression = Class(name="Expression")
sadl_OrderList = Class(name="sadl::OrderList")
sadl_ConstructExpression = Class(name="sadl::ConstructExpression")
sadl_SelectExpression = Class(name="sadl::SelectExpression")
sadl_GraphPattern = Class(name="sadl::GraphPattern")
sadl_IntervalValue = Class(name="sadl::IntervalValue")
sadl_ValueTable = Class(name="sadl::ValueTable")
sadl_AskQueryExpression = Class(name="sadl::AskQueryExpression")
sadl_OrderElement = Class(name="sadl::OrderElement")
sadl_SubjProp = Class(name="sadl::SubjProp")
sadl_InstAttrSPV = Class(name="sadl::InstAttrSPV")
sadl_PropOfSubj = Class(name="sadl::PropOfSubj")
sadl_InstAttrPSV = Class(name="sadl::InstAttrPSV")
sadl_ExistentialNegation = Class(name="sadl::ExistentialNegation")
sadl_SubTypeOf = Class(name="sadl::SubTypeOf")
sadl_ValueRow = Class(name="sadl::ValueRow")
sadl_BinaryOpExpression = Class(name="sadl::BinaryOpExpression")
sadl_UnaryOpExpression = Class(name="sadl::UnaryOpExpression")
sadl_JunctionExpression = Class(name="sadl::JunctionExpression")

# sadl_Model class attributes and methods

# sadl_ModelName class attributes and methods
sadl_ModelName_baseUri: Property = Property(name="baseUri", type=StringType)
sadl_ModelName_alias: Property = Property(name="alias", type=StringType)
sadl_ModelName_version: Property = Property(name="version", type=StringType)
sadl_ModelName_annType: Property = Property(name="annType", type=StringType)
sadl_ModelName.attributes={sadl_ModelName_baseUri, sadl_ModelName_alias, sadl_ModelName_version, sadl_ModelName_annType}

# sadl_Statement class attributes and methods

# ModelElement class attributes and methods

# sadl_ResourceName class attributes and methods
sadl_ResourceName_name: Property = Property(name="name", type=StringType)
sadl_ResourceName_annType: Property = Property(name="annType", type=StringType)
sadl_ResourceName.attributes={sadl_ResourceName_annType, sadl_ResourceName_name}

# sadl_Import class attributes and methods
sadl_Import_importURI: Property = Property(name="importURI", type=StringType)
sadl_Import_alias: Property = Property(name="alias", type=StringType)
sadl_Import.attributes={sadl_Import_alias, sadl_Import_importURI}

# sadl_ModelElement class attributes and methods

# sadl_ContentList class attributes and methods
sadl_ContentList_annContent: Property = Property(name="annContent", type=StringType)
sadl_ContentList.attributes={sadl_ContentList_annContent}

# sadl_ExistingResourceList class attributes and methods

# sadl_ResourceIdentifier class attributes and methods

# sadl_ResourceBySetOp class attributes and methods
sadl_ResourceBySetOp_annType: Property = Property(name="annType", type=StringType)
sadl_ResourceBySetOp_op: Property = Property(name="op", type=StringType)
sadl_ResourceBySetOp.attributes={sadl_ResourceBySetOp_annType, sadl_ResourceBySetOp_op}

# sadl_ResourceList class attributes and methods

# sadl_LiteralList class attributes and methods

# sadl_LiteralValue class attributes and methods
sadl_LiteralValue_literalNumber: Property = Property(name="literalNumber", type=StringType)
sadl_LiteralValue_literalString: Property = Property(name="literalString", type=StringType)
sadl_LiteralValue_literalBoolean: Property = Property(name="literalBoolean", type=StringType)
sadl_LiteralValue.attributes={sadl_LiteralValue_literalBoolean, sadl_LiteralValue_literalString, sadl_LiteralValue_literalNumber}

# sadl_ResourceByName class attributes and methods

# ResourceIdentifier class attributes and methods

# sadl_UnionResource class attributes and methods

# ResourceBySetOp class attributes and methods

# sadl_IntersectionResource class attributes and methods

# sadl_ClassDeclaration class attributes and methods

# Statement class attributes and methods

# sadl_EnumeratedInstances class attributes and methods

# sadl_AddlClassInfo class attributes and methods

# sadl_ResourceByRestriction class attributes and methods
sadl_ResourceByRestriction_annType: Property = Property(name="annType", type=StringType)
sadl_ResourceByRestriction.attributes={sadl_ResourceByRestriction_annType}

# sadl_Condition class attributes and methods

# sadl_Range class attributes and methods
sadl_Range_single: Property = Property(name="single", type=StringType)
sadl_Range_list: Property = Property(name="list", type=StringType)
sadl_Range_lists: Property = Property(name="lists", type=StringType)
sadl_Range.attributes={sadl_Range_single, sadl_Range_lists, sadl_Range_list}

# sadl_RangeType class attributes and methods
sadl_RangeType_dataType: Property = Property(name="dataType", type=StringType)
sadl_RangeType.attributes={sadl_RangeType_dataType}

# sadl_UserDefinedDataType class attributes and methods

# sadl_DataTypeRestriction class attributes and methods
sadl_DataTypeRestriction_basetypes: Property = Property(name="basetypes", type=StringType)
sadl_DataTypeRestriction_basetype: Property = Property(name="basetype", type=StringType)
sadl_DataTypeRestriction.attributes={sadl_DataTypeRestriction_basetype, sadl_DataTypeRestriction_basetypes}

# sadl_Facets class attributes and methods
sadl_Facets_minexin: Property = Property(name="minexin", type=StringType)
sadl_Facets_min: Property = Property(name="min", type=StringType)
sadl_Facets_max: Property = Property(name="max", type=StringType)
sadl_Facets_maxexin: Property = Property(name="maxexin", type=StringType)
sadl_Facets_regex: Property = Property(name="regex", type=StringType)
sadl_Facets_len: Property = Property(name="len", type=StringType)
sadl_Facets_minlen: Property = Property(name="minlen", type=StringType)
sadl_Facets_maxlen: Property = Property(name="maxlen", type=StringType)
sadl_Facets_values: Property = Property(name="values", type=StringType)
sadl_Facets.attributes={sadl_Facets_len, sadl_Facets_maxexin, sadl_Facets_values, sadl_Facets_maxlen, sadl_Facets_max, sadl_Facets_regex, sadl_Facets_min, sadl_Facets_minexin, sadl_Facets_minlen}

# sadl_EquivalentConcepts class attributes and methods

# sadl_ComplementOfClass class attributes and methods

# sadl_DisjointClasses class attributes and methods

# sadl_AllValuesFrom class attributes and methods

# sadl_PropertyOfClass class attributes and methods

# sadl_AllValuesCondition class attributes and methods

# sadl_HasValue class attributes and methods

# sadl_SomeValuesFrom class attributes and methods

# sadl_SomeValuesCondition class attributes and methods

# sadl_Cardinality class attributes and methods

# sadl_CardCondition class attributes and methods
sadl_CardCondition_card: Property = Property(name="card", type=StringType)
sadl_CardCondition.attributes={sadl_CardCondition_card}

# sadl_HasValueCondition class attributes and methods

# sadl_MaxCardinality class attributes and methods

# sadl_MaxCardCondition class attributes and methods
sadl_MaxCardCondition_card: Property = Property(name="card", type=StringType)
sadl_MaxCardCondition.attributes={sadl_MaxCardCondition_card}

# sadl_MinCardinality class attributes and methods

# sadl_MinCardCondition class attributes and methods
sadl_MinCardCondition_card: Property = Property(name="card", type=StringType)
sadl_MinCardCondition.attributes={sadl_MinCardCondition_card}

# sadl_EObject class attributes and methods

# sadl_EnumeratedAllAndSomeValuesFrom class attributes and methods

# sadl_DefaultValue class attributes and methods
sadl_DefaultValue_level: Property = Property(name="level", type=StringType)
sadl_DefaultValue.attributes={sadl_DefaultValue_level}

# Condition class attributes and methods

# sadl_EnumeratedAllValuesFrom class attributes and methods

# sadl_ExplicitValue class attributes and methods
sadl_ExplicitValue_valueList: Property = Property(name="valueList", type=StringType)
sadl_ExplicitValue_term: Property = Property(name="term", type=StringType)
sadl_ExplicitValue.attributes={sadl_ExplicitValue_valueList, sadl_ExplicitValue_term}

# sadl_PropertyDeclaration class attributes and methods
sadl_PropertyDeclaration_article: Property = Property(name="article", type=StringType)
sadl_PropertyDeclaration.attributes={sadl_PropertyDeclaration_article}

# sadl_AdditionalPropertyInfo class attributes and methods
sadl_AdditionalPropertyInfo_isfunc: Property = Property(name="isfunc", type=StringType)
sadl_AdditionalPropertyInfo_isinvfunc: Property = Property(name="isinvfunc", type=StringType)
sadl_AdditionalPropertyInfo_isSym: Property = Property(name="isSym", type=StringType)
sadl_AdditionalPropertyInfo_isTrans: Property = Property(name="isTrans", type=StringType)
sadl_AdditionalPropertyInfo.attributes={sadl_AdditionalPropertyInfo_isTrans, sadl_AdditionalPropertyInfo_isfunc, sadl_AdditionalPropertyInfo_isinvfunc, sadl_AdditionalPropertyInfo_isSym}

# sadl_NecessaryAndSufficient class attributes and methods
sadl_NecessaryAndSufficient_article: Property = Property(name="article", type=StringType)
sadl_NecessaryAndSufficient.attributes={sadl_NecessaryAndSufficient_article}

# sadl_TypedBNode class attributes and methods
sadl_TypedBNode_article: Property = Property(name="article", type=StringType)
sadl_TypedBNode.attributes={sadl_TypedBNode_article}

# sadl_IsInverseOf class attributes and methods

# sadl_TransitiveProperty class attributes and methods

# sadl_InverseProperty class attributes and methods

# sadl_FunctionalProperty class attributes and methods

# sadl_InverseFunctionalProperty class attributes and methods

# sadl_SymmetricalProperty class attributes and methods

# sadl_PropValPartialTriple class attributes and methods

# sadl_InstanceDifferentFrom class attributes and methods

# sadl_InstanceDeclarationStatement class attributes and methods

# sadl_InstanceDeclaration class attributes and methods
sadl_InstanceDeclaration_article: Property = Property(name="article", type=StringType)
sadl_InstanceDeclaration.attributes={sadl_InstanceDeclaration_article}

# InstanceDeclarationStatement class attributes and methods

# EmbeddedInstanceDeclaration class attributes and methods

# sadl_TypeDeclaration class attributes and methods

# sadl_ExistingInstanceAttribution class attributes and methods

# sadl_OfPatternReturningValues class attributes and methods

# sadl_Object class attributes and methods

# sadl_InstancesAllDifferent class attributes and methods

# sadl_OfPhrase class attributes and methods
sadl_OfPhrase_article: Property = Property(name="article", type=StringType)
sadl_OfPhrase.attributes={sadl_OfPhrase_article}

# sadl_WithChain class attributes and methods

# sadl_WithPhrase class attributes and methods

# sadl_VariableList class attributes and methods

# sadl_Rule class attributes and methods
sadl_Rule_name: Property = Property(name="name", type=StringType)
sadl_Rule.attributes={sadl_Rule_name}

# sadl_EmbeddedInstanceDeclaration class attributes and methods

# sadl_MergedTriples class attributes and methods

# GraphPattern class attributes and methods

# sadl_Query class attributes and methods

# sadl_Expression class attributes and methods
sadl_Expression_func: Property = Property(name="func", type=StringType)
sadl_Expression.attributes={sadl_Expression_func}

# sadl_Test class attributes and methods

# sadl_Expr class attributes and methods

# sadl_Display class attributes and methods
sadl_Display_displayString: Property = Property(name="displayString", type=StringType)
sadl_Display_model: Property = Property(name="model", type=StringType)
sadl_Display.attributes={sadl_Display_displayString, sadl_Display_model}

# sadl_Explanation class attributes and methods
sadl_Explanation_rulename: Property = Property(name="rulename", type=StringType)
sadl_Explanation.attributes={sadl_Explanation_rulename}

# sadl_ElementSet class attributes and methods

# Expression class attributes and methods

# sadl_OrderList class attributes and methods

# sadl_ConstructExpression class attributes and methods

# sadl_SelectExpression class attributes and methods
sadl_SelectExpression_distinct: Property = Property(name="distinct", type=StringType)
sadl_SelectExpression_allVars: Property = Property(name="allVars", type=StringType)
sadl_SelectExpression_orderby: Property = Property(name="orderby", type=StringType)
sadl_SelectExpression.attributes={sadl_SelectExpression_allVars, sadl_SelectExpression_distinct, sadl_SelectExpression_orderby}

# sadl_GraphPattern class attributes and methods

# sadl_IntervalValue class attributes and methods
sadl_IntervalValue_op: Property = Property(name="op", type=StringType)
sadl_IntervalValue.attributes={sadl_IntervalValue_op}

# sadl_ValueTable class attributes and methods

# sadl_AskQueryExpression class attributes and methods

# sadl_OrderElement class attributes and methods
sadl_OrderElement_order: Property = Property(name="order", type=StringType)
sadl_OrderElement.attributes={sadl_OrderElement_order}

# sadl_SubjProp class attributes and methods

# sadl_InstAttrSPV class attributes and methods

# sadl_PropOfSubj class attributes and methods

# sadl_InstAttrPSV class attributes and methods

# sadl_ExistentialNegation class attributes and methods

# sadl_SubTypeOf class attributes and methods

# sadl_ValueRow class attributes and methods

# sadl_BinaryOpExpression class attributes and methods
sadl_BinaryOpExpression_op: Property = Property(name="op", type=StringType)
sadl_BinaryOpExpression.attributes={sadl_BinaryOpExpression_op}

# sadl_UnaryOpExpression class attributes and methods
sadl_UnaryOpExpression_op: Property = Property(name="op", type=StringType)
sadl_UnaryOpExpression.attributes={sadl_UnaryOpExpression_op}

# sadl_JunctionExpression class attributes and methods
sadl_JunctionExpression_op: Property = Property(name="op", type=StringType)
sadl_JunctionExpression.attributes={sadl_JunctionExpression_op}

# Relationships
modelName0: BinaryAssociation = BinaryAssociation(
    name="modelName0",
    ends={
        Property(name="sadl_ModelName", type=sadl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Model", type=sadl_ModelName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annContent7: BinaryAssociation = BinaryAssociation(
    name="annContent7",
    ends={
        Property(name="sadl_ContentList8", type=sadl_ResourceName, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ResourceName", type=sadl_ContentList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="sadl_Import", type=sadl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Model2", type=sadl_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="sadl_ModelElement", type=sadl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Model4", type=sadl_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annContent5: BinaryAssociation = BinaryAssociation(
    name="annContent5",
    ends={
        Property(name="sadl_ContentList", type=sadl_ModelName, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ModelName6", type=sadl_ContentList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
names14: BinaryAssociation = BinaryAssociation(
    name="names14",
    ends={
        Property(name="sadl_ResourceIdentifier", type=sadl_ExistingResourceList, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ExistingResourceList", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annContent15: BinaryAssociation = BinaryAssociation(
    name="annContent15",
    ends={
        Property(name="sadl_ContentList16", type=sadl_ResourceBySetOp, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ResourceBySetOp", type=sadl_ContentList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
names17: BinaryAssociation = BinaryAssociation(
    name="names17",
    ends={
        Property(name="sadl_ResourceIdentifier19", type=sadl_ResourceBySetOp, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ResourceBySetOp18", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
names9: BinaryAssociation = BinaryAssociation(
    name="names9",
    ends={
        Property(name="sadl_ResourceName10", type=sadl_ResourceList, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ResourceList", type=sadl_ResourceName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literals11: BinaryAssociation = BinaryAssociation(
    name="literals11",
    ends={
        Property(name="sadl_LiteralValue", type=sadl_LiteralList, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_LiteralList", type=sadl_LiteralValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name12: BinaryAssociation = BinaryAssociation(
    name="name12",
    ends={
        Property(name="sadl_ResourceName13", type=sadl_ResourceByName, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ResourceByName", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1))
    }
)
className27: BinaryAssociation = BinaryAssociation(
    name="className27",
    ends={
        Property(name="sadl_ResourceName28", type=sadl_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ClassDeclaration", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mustBeOneOf29: BinaryAssociation = BinaryAssociation(
    name="mustBeOneOf29",
    ends={
        Property(name="sadl_EnumeratedInstances", type=sadl_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ClassDeclaration30", type=sadl_EnumeratedInstances, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
describedBy31: BinaryAssociation = BinaryAssociation(
    name="describedBy31",
    ends={
        Property(name="sadl_AddlClassInfo", type=sadl_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ClassDeclaration32", type=sadl_AddlClassInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annContent20: BinaryAssociation = BinaryAssociation(
    name="annContent20",
    ends={
        Property(name="sadl_ContentList21", type=sadl_ResourceByRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ResourceByRestriction", type=sadl_ContentList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propName22: BinaryAssociation = BinaryAssociation(
    name="propName22",
    ends={
        Property(name="sadl_ResourceByName24", type=sadl_ResourceByRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ResourceByRestriction23", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond25: BinaryAssociation = BinaryAssociation(
    name="cond25",
    ends={
        Property(name="sadl_Condition", type=sadl_ResourceByRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ResourceByRestriction26", type=sadl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
range48: BinaryAssociation = BinaryAssociation(
    name="range48",
    ends={
        Property(name="sadl_Range", type=sadl_AddlClassInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AddlClassInfo49", type=sadl_Range, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restriction50: BinaryAssociation = BinaryAssociation(
    name="restriction50",
    ends={
        Property(name="sadl_Condition52", type=sadl_AddlClassInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AddlClassInfo51", type=sadl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type53: BinaryAssociation = BinaryAssociation(
    name="type53",
    ends={
        Property(name="sadl_RangeType", type=sadl_Range, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Range54", type=sadl_RangeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classList33: BinaryAssociation = BinaryAssociation(
    name="classList33",
    ends={
        Property(name="sadl_ResourceList35", type=sadl_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ClassDeclaration34", type=sadl_ResourceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classIdentifier36: BinaryAssociation = BinaryAssociation(
    name="classIdentifier36",
    ends={
        Property(name="sadl_ResourceIdentifier38", type=sadl_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ClassDeclaration37", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instanceList39: BinaryAssociation = BinaryAssociation(
    name="instanceList39",
    ends={
        Property(name="sadl_ResourceList41", type=sadl_EnumeratedInstances, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_EnumeratedInstances40", type=sadl_ResourceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyByName42: BinaryAssociation = BinaryAssociation(
    name="propertyByName42",
    ends={
        Property(name="sadl_ResourceByName44", type=sadl_AddlClassInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AddlClassInfo43", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName45: BinaryAssociation = BinaryAssociation(
    name="propertyName45",
    ends={
        Property(name="sadl_ResourceName47", type=sadl_AddlClassInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AddlClassInfo46", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classIdentifier55: BinaryAssociation = BinaryAssociation(
    name="classIdentifier55",
    ends={
        Property(name="sadl_ResourceIdentifier57", type=sadl_RangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_RangeType56", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userDefinedDataType58: BinaryAssociation = BinaryAssociation(
    name="userDefinedDataType58",
    ends={
        Property(name="sadl_ResourceName59", type=sadl_UserDefinedDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_UserDefinedDataType", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restriction60: BinaryAssociation = BinaryAssociation(
    name="restriction60",
    ends={
        Property(name="sadl_DataTypeRestriction", type=sadl_UserDefinedDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_UserDefinedDataType61", type=sadl_DataTypeRestriction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
facets62: BinaryAssociation = BinaryAssociation(
    name="facets62",
    ends={
        Property(name="sadl_Facets", type=sadl_DataTypeRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_DataTypeRestriction63", type=sadl_Facets, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class164: BinaryAssociation = BinaryAssociation(
    name="class164",
    ends={
        Property(name="sadl_ResourceByName65", type=sadl_EquivalentConcepts, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_EquivalentConcepts", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class266: BinaryAssociation = BinaryAssociation(
    name="class266",
    ends={
        Property(name="sadl_ResourceIdentifier68", type=sadl_EquivalentConcepts, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_EquivalentConcepts67", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class177: BinaryAssociation = BinaryAssociation(
    name="class177",
    ends={
        Property(name="sadl_ResourceByName78", type=sadl_ComplementOfClass, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ComplementOfClass", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class279: BinaryAssociation = BinaryAssociation(
    name="class279",
    ends={
        Property(name="sadl_ResourceIdentifier81", type=sadl_ComplementOfClass, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ComplementOfClass80", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class169: BinaryAssociation = BinaryAssociation(
    name="class169",
    ends={
        Property(name="sadl_ResourceByName70", type=sadl_DisjointClasses, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_DisjointClasses", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class271: BinaryAssociation = BinaryAssociation(
    name="class271",
    ends={
        Property(name="sadl_ResourceIdentifier73", type=sadl_DisjointClasses, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_DisjointClasses72", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classes74: BinaryAssociation = BinaryAssociation(
    name="classes74",
    ends={
        Property(name="sadl_ExistingResourceList76", type=sadl_DisjointClasses, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_DisjointClasses75", type=sadl_ExistingResourceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className85: BinaryAssociation = BinaryAssociation(
    name="className85",
    ends={
        Property(name="sadl_ResourceIdentifier87", type=sadl_AllValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AllValuesFrom86", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName88: BinaryAssociation = BinaryAssociation(
    name="propertyName88",
    ends={
        Property(name="sadl_ResourceByName90", type=sadl_AllValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AllValuesFrom89", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restricted82: BinaryAssociation = BinaryAssociation(
    name="restricted82",
    ends={
        Property(name="sadl_PropertyOfClass", type=sadl_AllValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AllValuesFrom", type=sadl_PropertyOfClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond83: BinaryAssociation = BinaryAssociation(
    name="cond83",
    ends={
        Property(name="sadl_AllValuesCondition", type=sadl_AllValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AllValuesFrom84", type=sadl_AllValuesCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className95: BinaryAssociation = BinaryAssociation(
    name="className95",
    ends={
        Property(name="sadl_SomeValuesFrom96", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="sadl_ResourceIdentifier97", type=sadl_SomeValuesFrom, multiplicity=Multiplicity(1, 1))
    }
)
propertyName98: BinaryAssociation = BinaryAssociation(
    name="propertyName98",
    ends={
        Property(name="sadl_ResourceByName100", type=sadl_SomeValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_SomeValuesFrom99", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restricted91: BinaryAssociation = BinaryAssociation(
    name="restricted91",
    ends={
        Property(name="sadl_PropertyOfClass92", type=sadl_SomeValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_SomeValuesFrom", type=sadl_PropertyOfClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond93: BinaryAssociation = BinaryAssociation(
    name="cond93",
    ends={
        Property(name="sadl_SomeValuesCondition", type=sadl_SomeValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_SomeValuesFrom94", type=sadl_SomeValuesCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restricted111: BinaryAssociation = BinaryAssociation(
    name="restricted111",
    ends={
        Property(name="sadl_PropertyOfClass112", type=sadl_Cardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Cardinality", type=sadl_PropertyOfClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond113: BinaryAssociation = BinaryAssociation(
    name="cond113",
    ends={
        Property(name="sadl_CardCondition", type=sadl_Cardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Cardinality114", type=sadl_CardCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className115: BinaryAssociation = BinaryAssociation(
    name="className115",
    ends={
        Property(name="sadl_ResourceIdentifier117", type=sadl_Cardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Cardinality116", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName118: BinaryAssociation = BinaryAssociation(
    name="propertyName118",
    ends={
        Property(name="sadl_ResourceByName120", type=sadl_Cardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Cardinality119", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restricted101: BinaryAssociation = BinaryAssociation(
    name="restricted101",
    ends={
        Property(name="sadl_PropertyOfClass102", type=sadl_HasValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_HasValue", type=sadl_PropertyOfClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond103: BinaryAssociation = BinaryAssociation(
    name="cond103",
    ends={
        Property(name="sadl_HasValueCondition", type=sadl_HasValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_HasValue104", type=sadl_HasValueCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className105: BinaryAssociation = BinaryAssociation(
    name="className105",
    ends={
        Property(name="sadl_ResourceIdentifier107", type=sadl_HasValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_HasValue106", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName108: BinaryAssociation = BinaryAssociation(
    name="propertyName108",
    ends={
        Property(name="sadl_ResourceByName110", type=sadl_HasValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_HasValue109", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restricted131: BinaryAssociation = BinaryAssociation(
    name="restricted131",
    ends={
        Property(name="sadl_PropertyOfClass132", type=sadl_MaxCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MaxCardinality", type=sadl_PropertyOfClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond133: BinaryAssociation = BinaryAssociation(
    name="cond133",
    ends={
        Property(name="sadl_MaxCardCondition", type=sadl_MaxCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MaxCardinality134", type=sadl_MaxCardCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className135: BinaryAssociation = BinaryAssociation(
    name="className135",
    ends={
        Property(name="sadl_ResourceIdentifier137", type=sadl_MaxCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MaxCardinality136", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName138: BinaryAssociation = BinaryAssociation(
    name="propertyName138",
    ends={
        Property(name="sadl_ResourceByName140", type=sadl_MaxCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MaxCardinality139", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restricted121: BinaryAssociation = BinaryAssociation(
    name="restricted121",
    ends={
        Property(name="sadl_PropertyOfClass122", type=sadl_MinCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MinCardinality", type=sadl_PropertyOfClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond123: BinaryAssociation = BinaryAssociation(
    name="cond123",
    ends={
        Property(name="sadl_MinCardCondition", type=sadl_MinCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MinCardinality124", type=sadl_MinCardCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className125: BinaryAssociation = BinaryAssociation(
    name="className125",
    ends={
        Property(name="sadl_ResourceIdentifier127", type=sadl_MinCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MinCardinality126", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName128: BinaryAssociation = BinaryAssociation(
    name="propertyName128",
    ends={
        Property(name="sadl_ResourceByName130", type=sadl_MinCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MinCardinality129", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumeration152: BinaryAssociation = BinaryAssociation(
    name="enumeration152",
    ends={
        Property(name="sadl_EObject", type=sadl_EnumeratedAllValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_EnumeratedAllValuesFrom153", type=sadl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restricted154: BinaryAssociation = BinaryAssociation(
    name="restricted154",
    ends={
        Property(name="sadl_PropertyOfClass155", type=sadl_EnumeratedAllAndSomeValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_EnumeratedAllAndSomeValuesFrom", type=sadl_PropertyOfClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumeration156: BinaryAssociation = BinaryAssociation(
    name="enumeration156",
    ends={
        Property(name="sadl_EObject158", type=sadl_EnumeratedAllAndSomeValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_EnumeratedAllAndSomeValuesFrom157", type=sadl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName141: BinaryAssociation = BinaryAssociation(
    name="propertyName141",
    ends={
        Property(name="sadl_ResourceByName143", type=sadl_PropertyOfClass, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropertyOfClass142", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className144: BinaryAssociation = BinaryAssociation(
    name="className144",
    ends={
        Property(name="sadl_ResourceIdentifier146", type=sadl_PropertyOfClass, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropertyOfClass145", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restriction147: BinaryAssociation = BinaryAssociation(
    name="restriction147",
    ends={
        Property(name="sadl_ResourceIdentifier149", type=sadl_AllValuesCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AllValuesCondition148", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restricted150: BinaryAssociation = BinaryAssociation(
    name="restricted150",
    ends={
        Property(name="sadl_PropertyOfClass151", type=sadl_EnumeratedAllValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_EnumeratedAllValuesFrom", type=sadl_PropertyOfClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classQualifier169: BinaryAssociation = BinaryAssociation(
    name="classQualifier169",
    ends={
        Property(name="sadl_ResourceIdentifier171", type=sadl_MinCardCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MinCardCondition170", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classQualifier172: BinaryAssociation = BinaryAssociation(
    name="classQualifier172",
    ends={
        Property(name="sadl_ResourceIdentifier174", type=sadl_MaxCardCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MaxCardCondition173", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defValueClass159: BinaryAssociation = BinaryAssociation(
    name="defValueClass159",
    ends={
        Property(name="sadl_PropertyOfClass160", type=sadl_DefaultValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_DefaultValue", type=sadl_PropertyOfClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defValue161: BinaryAssociation = BinaryAssociation(
    name="defValue161",
    ends={
        Property(name="sadl_ExplicitValue", type=sadl_DefaultValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_DefaultValue162", type=sadl_ExplicitValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restriction163: BinaryAssociation = BinaryAssociation(
    name="restriction163",
    ends={
        Property(name="sadl_EObject165", type=sadl_SomeValuesCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_SomeValuesCondition164", type=sadl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restriction166: BinaryAssociation = BinaryAssociation(
    name="restriction166",
    ends={
        Property(name="sadl_ExplicitValue168", type=sadl_HasValueCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_HasValueCondition167", type=sadl_ExplicitValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond185: BinaryAssociation = BinaryAssociation(
    name="cond185",
    ends={
        Property(name="sadl_Condition187", type=sadl_NecessaryAndSufficient, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_NecessaryAndSufficient186", type=sadl_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyName188: BinaryAssociation = BinaryAssociation(
    name="propertyName188",
    ends={
        Property(name="sadl_ResourceName189", type=sadl_PropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropertyDeclaration", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superPropName190: BinaryAssociation = BinaryAssociation(
    name="superPropName190",
    ends={
        Property(name="sadl_ResourceByName192", type=sadl_PropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropertyDeclaration191", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addlPropInfo193: BinaryAssociation = BinaryAssociation(
    name="addlPropInfo193",
    ends={
        Property(name="sadl_AdditionalPropertyInfo", type=sadl_PropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropertyDeclaration194", type=sadl_AdditionalPropertyInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classQualifier175: BinaryAssociation = BinaryAssociation(
    name="classQualifier175",
    ends={
        Property(name="sadl_ResourceIdentifier177", type=sadl_CardCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_CardCondition176", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superClass178: BinaryAssociation = BinaryAssociation(
    name="superClass178",
    ends={
        Property(name="sadl_TypedBNode", type=sadl_NecessaryAndSufficient, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_NecessaryAndSufficient", type=sadl_TypedBNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subClass179: BinaryAssociation = BinaryAssociation(
    name="subClass179",
    ends={
        Property(name="sadl_ResourceName181", type=sadl_NecessaryAndSufficient, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_NecessaryAndSufficient180", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName182: BinaryAssociation = BinaryAssociation(
    name="propertyName182",
    ends={
        Property(name="sadl_ResourceByName184", type=sadl_NecessaryAndSufficient, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_NecessaryAndSufficient183", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond207: BinaryAssociation = BinaryAssociation(
    name="cond207",
    ends={
        Property(name="sadl_Condition209", type=sadl_AdditionalPropertyInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AdditionalPropertyInfo208", type=sadl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
range210: BinaryAssociation = BinaryAssociation(
    name="range210",
    ends={
        Property(name="sadl_Range212", type=sadl_AdditionalPropertyInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AdditionalPropertyInfo211", type=sadl_Range, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain195: BinaryAssociation = BinaryAssociation(
    name="domain195",
    ends={
        Property(name="sadl_ResourceIdentifier197", type=sadl_PropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropertyDeclaration196", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rangeResource198: BinaryAssociation = BinaryAssociation(
    name="rangeResource198",
    ends={
        Property(name="sadl_ResourceIdentifier200", type=sadl_PropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropertyDeclaration199", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationProperty201: BinaryAssociation = BinaryAssociation(
    name="annotationProperty201",
    ends={
        Property(name="sadl_ResourceName203", type=sadl_PropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropertyDeclaration202", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain204: BinaryAssociation = BinaryAssociation(
    name="domain204",
    ends={
        Property(name="sadl_ResourceIdentifier206", type=sadl_AdditionalPropertyInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AdditionalPropertyInfo205", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName221: BinaryAssociation = BinaryAssociation(
    name="propertyName221",
    ends={
        Property(name="sadl_ResourceByName222", type=sadl_TransitiveProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_TransitiveProperty", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName1223: BinaryAssociation = BinaryAssociation(
    name="propertyName1223",
    ends={
        Property(name="sadl_ResourceByName224", type=sadl_InverseProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InverseProperty", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invOf225: BinaryAssociation = BinaryAssociation(
    name="invOf225",
    ends={
        Property(name="sadl_IsInverseOf227", type=sadl_InverseProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InverseProperty226", type=sadl_IsInverseOf, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isInvOf213: BinaryAssociation = BinaryAssociation(
    name="isInvOf213",
    ends={
        Property(name="sadl_IsInverseOf", type=sadl_AdditionalPropertyInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_AdditionalPropertyInfo214", type=sadl_IsInverseOf, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName215: BinaryAssociation = BinaryAssociation(
    name="propertyName215",
    ends={
        Property(name="sadl_ResourceByName216", type=sadl_FunctionalProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_FunctionalProperty", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName217: BinaryAssociation = BinaryAssociation(
    name="propertyName217",
    ends={
        Property(name="sadl_ResourceByName218", type=sadl_InverseFunctionalProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InverseFunctionalProperty", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName219: BinaryAssociation = BinaryAssociation(
    name="propertyName219",
    ends={
        Property(name="sadl_ResourceByName220", type=sadl_SymmetricalProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_SymmetricalProperty", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDecl234: BinaryAssociation = BinaryAssociation(
    name="typeDecl234",
    ends={
        Property(name="sadl_TypeDeclaration", type=sadl_InstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstanceDeclaration", type=sadl_TypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addlInfoItems235: BinaryAssociation = BinaryAssociation(
    name="addlInfoItems235",
    ends={
        Property(name="sadl_PropValPartialTriple", type=sadl_InstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstanceDeclaration236", type=sadl_PropValPartialTriple, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
className237: BinaryAssociation = BinaryAssociation(
    name="className237",
    ends={
        Property(name="sadl_ResourceByName239", type=sadl_InstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstanceDeclaration238", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instanceName240: BinaryAssociation = BinaryAssociation(
    name="instanceName240",
    ends={
        Property(name="sadl_ResourceName242", type=sadl_InstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstanceDeclaration241", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instName243: BinaryAssociation = BinaryAssociation(
    name="instName243",
    ends={
        Property(name="sadl_ResourceName245", type=sadl_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_TypeDeclaration244", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName2228: BinaryAssociation = BinaryAssociation(
    name="propertyName2228",
    ends={
        Property(name="sadl_ResourceByName230", type=sadl_IsInverseOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_IsInverseOf229", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type246: BinaryAssociation = BinaryAssociation(
    name="type246",
    ends={
        Property(name="sadl_TypedBNode248", type=sadl_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_TypeDeclaration247", type=sadl_TypedBNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classIdentifier231: BinaryAssociation = BinaryAssociation(
    name="classIdentifier231",
    ends={
        Property(name="sadl_ResourceIdentifier233", type=sadl_TypedBNode, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_TypedBNode232", type=sadl_ResourceIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instances254: BinaryAssociation = BinaryAssociation(
    name="instances254",
    ends={
        Property(name="sadl_ExistingResourceList255", type=sadl_InstancesAllDifferent, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstancesAllDifferent", type=sadl_ExistingResourceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subj256: BinaryAssociation = BinaryAssociation(
    name="subj256",
    ends={
        Property(name="sadl_ResourceByName257", type=sadl_ExistingInstanceAttribution, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ExistingInstanceAttribution", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addlInfoItems258: BinaryAssociation = BinaryAssociation(
    name="addlInfoItems258",
    ends={
        Property(name="sadl_PropValPartialTriple260", type=sadl_ExistingInstanceAttribution, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ExistingInstanceAttribution259", type=sadl_PropValPartialTriple, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pOfS261: BinaryAssociation = BinaryAssociation(
    name="pOfS261",
    ends={
        Property(name="sadl_OfPatternReturningValues", type=sadl_ExistingInstanceAttribution, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ExistingInstanceAttribution262", type=sadl_OfPatternReturningValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
obj263: BinaryAssociation = BinaryAssociation(
    name="obj263",
    ends={
        Property(name="sadl_EObject265", type=sadl_ExistingInstanceAttribution, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ExistingInstanceAttribution264", type=sadl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val266: BinaryAssociation = BinaryAssociation(
    name="val266",
    ends={
        Property(name="sadl_EObject267", type=sadl_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Object", type=sadl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instName1249: BinaryAssociation = BinaryAssociation(
    name="instName1249",
    ends={
        Property(name="sadl_ResourceByName250", type=sadl_InstanceDifferentFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstanceDifferentFrom", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instName2251: BinaryAssociation = BinaryAssociation(
    name="instName2251",
    ends={
        Property(name="sadl_ResourceByName253", type=sadl_InstanceDifferentFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstanceDifferentFrom252", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectValueBNode274: BinaryAssociation = BinaryAssociation(
    name="objectValueBNode274",
    ends={
        Property(name="sadl_InstanceDeclaration276", type=sadl_PropValPartialTriple, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropValPartialTriple275", type=sadl_InstanceDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ofphrs277: BinaryAssociation = BinaryAssociation(
    name="ofphrs277",
    ends={
        Property(name="sadl_OfPhrase", type=sadl_OfPatternReturningValues, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_OfPatternReturningValues278", type=sadl_OfPhrase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject279: BinaryAssociation = BinaryAssociation(
    name="subject279",
    ends={
        Property(name="sadl_ResourceByName281", type=sadl_OfPatternReturningValues, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_OfPatternReturningValues280", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type282: BinaryAssociation = BinaryAssociation(
    name="type282",
    ends={
        Property(name="sadl_TypedBNode284", type=sadl_OfPatternReturningValues, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_OfPatternReturningValues283", type=sadl_TypedBNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wps285: BinaryAssociation = BinaryAssociation(
    name="wps285",
    ends={
        Property(name="sadl_WithPhrase", type=sadl_WithChain, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_WithChain", type=sadl_WithPhrase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyName286: BinaryAssociation = BinaryAssociation(
    name="propertyName286",
    ends={
        Property(name="sadl_ResourceByName288", type=sadl_WithPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_WithPhrase287", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyName268: BinaryAssociation = BinaryAssociation(
    name="propertyName268",
    ends={
        Property(name="sadl_ResourceByName270", type=sadl_PropValPartialTriple, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropValPartialTriple269", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectValue271: BinaryAssociation = BinaryAssociation(
    name="objectValue271",
    ends={
        Property(name="sadl_ExplicitValue273", type=sadl_PropValPartialTriple, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropValPartialTriple272", type=sadl_ExplicitValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ops292: BinaryAssociation = BinaryAssociation(
    name="ops292",
    ends={
        Property(name="sadl_OfPhrase293", type=sadl_MergedTriples, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MergedTriples", type=sadl_OfPhrase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pivot294: BinaryAssociation = BinaryAssociation(
    name="pivot294",
    ends={
        Property(name="sadl_TypedBNode296", type=sadl_MergedTriples, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MergedTriples295", type=sadl_TypedBNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wcs297: BinaryAssociation = BinaryAssociation(
    name="wcs297",
    ends={
        Property(name="sadl_WithChain299", type=sadl_MergedTriples, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_MergedTriples298", type=sadl_WithChain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyName300: BinaryAssociation = BinaryAssociation(
    name="propertyName300",
    ends={
        Property(name="sadl_ResourceByName302", type=sadl_OfPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_OfPhrase301", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
names303: BinaryAssociation = BinaryAssociation(
    name="names303",
    ends={
        Property(name="sadl_ResourceName304", type=sadl_VariableList, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_VariableList", type=sadl_ResourceName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value289: BinaryAssociation = BinaryAssociation(
    name="value289",
    ends={
        Property(name="sadl_EObject291", type=sadl_WithPhrase, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_WithPhrase290", type=sadl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr312: BinaryAssociation = BinaryAssociation(
    name="expr312",
    ends={
        Property(name="sadl_Expression", type=sadl_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Query", type=sadl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr313: BinaryAssociation = BinaryAssociation(
    name="expr313",
    ends={
        Property(name="sadl_Expression314", type=sadl_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Test", type=sadl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr315: BinaryAssociation = BinaryAssociation(
    name="expr315",
    ends={
        Property(name="sadl_Expression316", type=sadl_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Expr", type=sadl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
givens305: BinaryAssociation = BinaryAssociation(
    name="givens305",
    ends={
        Property(name="sadl_ElementSet", type=sadl_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Rule", type=sadl_ElementSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifs306: BinaryAssociation = BinaryAssociation(
    name="ifs306",
    ends={
        Property(name="sadl_ElementSet308", type=sadl_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Rule307", type=sadl_ElementSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thens309: BinaryAssociation = BinaryAssociation(
    name="thens309",
    ends={
        Property(name="sadl_ElementSet311", type=sadl_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Rule310", type=sadl_ElementSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varList322: BinaryAssociation = BinaryAssociation(
    name="varList322",
    ends={
        Property(name="sadl_VariableList323", type=sadl_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_SelectExpression", type=sadl_VariableList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderList324: BinaryAssociation = BinaryAssociation(
    name="orderList324",
    ends={
        Property(name="sadl_OrderList", type=sadl_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_SelectExpression325", type=sadl_OrderList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subj326: BinaryAssociation = BinaryAssociation(
    name="subj326",
    ends={
        Property(name="sadl_ResourceName327", type=sadl_ConstructExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ConstructExpression", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pred328: BinaryAssociation = BinaryAssociation(
    name="pred328",
    ends={
        Property(name="sadl_ResourceName330", type=sadl_ConstructExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ConstructExpression329", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
obj331: BinaryAssociation = BinaryAssociation(
    name="obj331",
    ends={
        Property(name="sadl_ResourceName333", type=sadl_ConstructExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ConstructExpression332", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr317: BinaryAssociation = BinaryAssociation(
    name="expr317",
    ends={
        Property(name="sadl_EObject318", type=sadl_Explanation, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Explanation", type=sadl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements319: BinaryAssociation = BinaryAssociation(
    name="elements319",
    ends={
        Property(name="sadl_Expression321", type=sadl_ElementSet, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ElementSet320", type=sadl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name336: BinaryAssociation = BinaryAssociation(
    name="name336",
    ends={
        Property(name="sadl_ResourceName338", type=sadl_OrderElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_OrderElement337", type=sadl_ResourceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr340: BinaryAssociation = BinaryAssociation(
    name="expr340",
    ends={
        Property(name="sadl_Expression341", type=sadl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Expression339", type=sadl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args343: BinaryAssociation = BinaryAssociation(
    name="args343",
    ends={
        Property(name="sadl_Expression344", type=sadl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Expression342", type=sadl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gp345: BinaryAssociation = BinaryAssociation(
    name="gp345",
    ends={
        Property(name="sadl_GraphPattern", type=sadl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Expression346", type=sadl_GraphPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ivalue347: BinaryAssociation = BinaryAssociation(
    name="ivalue347",
    ends={
        Property(name="sadl_IntervalValue", type=sadl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Expression348", type=sadl_IntervalValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value349: BinaryAssociation = BinaryAssociation(
    name="value349",
    ends={
        Property(name="sadl_ExplicitValue351", type=sadl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Expression350", type=sadl_ExplicitValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderList334: BinaryAssociation = BinaryAssociation(
    name="orderList334",
    ends={
        Property(name="sadl_OrderElement", type=sadl_OrderList, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_OrderList335", type=sadl_OrderElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subj356: BinaryAssociation = BinaryAssociation(
    name="subj356",
    ends={
        Property(name="sadl_ResourceByName358", type=sadl_PropOfSubj, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropOfSubj357", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subj359: BinaryAssociation = BinaryAssociation(
    name="subj359",
    ends={
        Property(name="sadl_ResourceByName360", type=sadl_SubjProp, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_SubjProp", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hwPhr361: BinaryAssociation = BinaryAssociation(
    name="hwPhr361",
    ends={
        Property(name="sadl_WithPhrase363", type=sadl_SubjProp, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_SubjProp362", type=sadl_WithPhrase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subj364: BinaryAssociation = BinaryAssociation(
    name="subj364",
    ends={
        Property(name="sadl_ResourceByName365", type=sadl_InstAttrSPV, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstAttrSPV", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueTable352: BinaryAssociation = BinaryAssociation(
    name="valueTable352",
    ends={
        Property(name="sadl_ValueTable", type=sadl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_Expression353", type=sadl_ValueTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ofPhr354: BinaryAssociation = BinaryAssociation(
    name="ofPhr354",
    ends={
        Property(name="sadl_OfPhrase355", type=sadl_PropOfSubj, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_PropOfSubj", type=sadl_OfPhrase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vals369: BinaryAssociation = BinaryAssociation(
    name="vals369",
    ends={
        Property(name="sadl_Expression371", type=sadl_InstAttrSPV, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstAttrSPV370", type=sadl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prop372: BinaryAssociation = BinaryAssociation(
    name="prop372",
    ends={
        Property(name="sadl_PropOfSubj373", type=sadl_InstAttrPSV, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstAttrPSV", type=sadl_PropOfSubj, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val374: BinaryAssociation = BinaryAssociation(
    name="val374",
    ends={
        Property(name="sadl_ExplicitValue376", type=sadl_InstAttrPSV, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstAttrPSV375", type=sadl_ExplicitValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
props366: BinaryAssociation = BinaryAssociation(
    name="props366",
    ends={
        Property(name="sadl_ResourceByName368", type=sadl_InstAttrSPV, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_InstAttrSPV367", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subclass377: BinaryAssociation = BinaryAssociation(
    name="subclass377",
    ends={
        Property(name="sadl_ResourceByName378", type=sadl_SubTypeOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_SubTypeOf", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superclass379: BinaryAssociation = BinaryAssociation(
    name="superclass379",
    ends={
        Property(name="sadl_ResourceByName381", type=sadl_SubTypeOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_SubTypeOf380", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varList382: BinaryAssociation = BinaryAssociation(
    name="varList382",
    ends={
        Property(name="sadl_VariableList383", type=sadl_ExistentialNegation, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ExistentialNegation", type=sadl_VariableList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
quantified384: BinaryAssociation = BinaryAssociation(
    name="quantified384",
    ends={
        Property(name="sadl_Expression386", type=sadl_ExistentialNegation, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ExistentialNegation385", type=sadl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr387: BinaryAssociation = BinaryAssociation(
    name="expr387",
    ends={
        Property(name="sadl_IntervalValue388", type=sadl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="sadl_Expression389", type=sadl_IntervalValue, multiplicity=Multiplicity(1, 1))
    }
)
instName390: BinaryAssociation = BinaryAssociation(
    name="instName390",
    ends={
        Property(name="sadl_ResourceByName392", type=sadl_ExplicitValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ExplicitValue391", type=sadl_ResourceByName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
litValue393: BinaryAssociation = BinaryAssociation(
    name="litValue393",
    ends={
        Property(name="sadl_LiteralValue395", type=sadl_ExplicitValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ExplicitValue394", type=sadl_LiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
row396: BinaryAssociation = BinaryAssociation(
    name="row396",
    ends={
        Property(name="sadl_ValueRow", type=sadl_ExplicitValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ExplicitValue397", type=sadl_ValueRow, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rows398: BinaryAssociation = BinaryAssociation(
    name="rows398",
    ends={
        Property(name="sadl_ValueRow400", type=sadl_ValueTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ValueTable399", type=sadl_ValueRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left404: BinaryAssociation = BinaryAssociation(
    name="left404",
    ends={
        Property(name="sadl_Expression405", type=sadl_JunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_JunctionExpression", type=sadl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right406: BinaryAssociation = BinaryAssociation(
    name="right406",
    ends={
        Property(name="sadl_Expression408", type=sadl_JunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_JunctionExpression407", type=sadl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left409: BinaryAssociation = BinaryAssociation(
    name="left409",
    ends={
        Property(name="sadl_Expression410", type=sadl_BinaryOpExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_BinaryOpExpression", type=sadl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right411: BinaryAssociation = BinaryAssociation(
    name="right411",
    ends={
        Property(name="sadl_Expression413", type=sadl_BinaryOpExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_BinaryOpExpression412", type=sadl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
explicitValues401: BinaryAssociation = BinaryAssociation(
    name="explicitValues401",
    ends={
        Property(name="sadl_ExplicitValue403", type=sadl_ValueRow, multiplicity=Multiplicity(1, 1)),
        Property(name="sadl_ValueRow402", type=sadl_ExplicitValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sadl_Statement_ModelElement = Generalization(general=ModelElement, specific=sadl_Statement)
gen_sadl_ResourceBySetOp_ResourceIdentifier = Generalization(general=ResourceIdentifier, specific=sadl_ResourceBySetOp)
gen_sadl_ResourceByName_ResourceIdentifier = Generalization(general=ResourceIdentifier, specific=sadl_ResourceByName)
gen_sadl_UnionResource_ResourceBySetOp = Generalization(general=ResourceBySetOp, specific=sadl_UnionResource)
gen_sadl_IntersectionResource_ResourceBySetOp = Generalization(general=ResourceBySetOp, specific=sadl_IntersectionResource)
gen_sadl_ClassDeclaration_Statement = Generalization(general=Statement, specific=sadl_ClassDeclaration)
gen_sadl_ResourceByRestriction_ResourceIdentifier = Generalization(general=ResourceIdentifier, specific=sadl_ResourceByRestriction)
gen_sadl_UserDefinedDataType_Statement = Generalization(general=Statement, specific=sadl_UserDefinedDataType)
gen_sadl_EquivalentConcepts_Statement = Generalization(general=Statement, specific=sadl_EquivalentConcepts)
gen_sadl_ComplementOfClass_Statement = Generalization(general=Statement, specific=sadl_ComplementOfClass)
gen_sadl_DisjointClasses_Statement = Generalization(general=Statement, specific=sadl_DisjointClasses)
gen_sadl_AllValuesFrom_Statement = Generalization(general=Statement, specific=sadl_AllValuesFrom)
gen_sadl_HasValue_Statement = Generalization(general=Statement, specific=sadl_HasValue)
gen_sadl_SomeValuesFrom_Statement = Generalization(general=Statement, specific=sadl_SomeValuesFrom)
gen_sadl_Cardinality_Statement = Generalization(general=Statement, specific=sadl_Cardinality)
gen_sadl_MaxCardinality_Statement = Generalization(general=Statement, specific=sadl_MaxCardinality)
gen_sadl_MinCardinality_Statement = Generalization(general=Statement, specific=sadl_MinCardinality)
gen_sadl_EnumeratedAllAndSomeValuesFrom_Statement = Generalization(general=Statement, specific=sadl_EnumeratedAllAndSomeValuesFrom)
gen_sadl_DefaultValue_Statement = Generalization(general=Statement, specific=sadl_DefaultValue)
gen_sadl_AllValuesCondition_Condition = Generalization(general=Condition, specific=sadl_AllValuesCondition)
gen_sadl_EnumeratedAllValuesFrom_Statement = Generalization(general=Statement, specific=sadl_EnumeratedAllValuesFrom)
gen_sadl_MinCardCondition_Condition = Generalization(general=Condition, specific=sadl_MinCardCondition)
gen_sadl_MaxCardCondition_Condition = Generalization(general=Condition, specific=sadl_MaxCardCondition)
gen_sadl_CardCondition_Condition = Generalization(general=Condition, specific=sadl_CardCondition)
gen_sadl_SomeValuesCondition_Condition = Generalization(general=Condition, specific=sadl_SomeValuesCondition)
gen_sadl_HasValueCondition_Condition = Generalization(general=Condition, specific=sadl_HasValueCondition)
gen_sadl_PropertyDeclaration_Statement = Generalization(general=Statement, specific=sadl_PropertyDeclaration)
gen_sadl_NecessaryAndSufficient_Statement = Generalization(general=Statement, specific=sadl_NecessaryAndSufficient)
gen_sadl_TransitiveProperty_Statement = Generalization(general=Statement, specific=sadl_TransitiveProperty)
gen_sadl_InverseProperty_Statement = Generalization(general=Statement, specific=sadl_InverseProperty)
gen_sadl_FunctionalProperty_Statement = Generalization(general=Statement, specific=sadl_FunctionalProperty)
gen_sadl_InverseFunctionalProperty_Statement = Generalization(general=Statement, specific=sadl_InverseFunctionalProperty)
gen_sadl_SymmetricalProperty_Statement = Generalization(general=Statement, specific=sadl_SymmetricalProperty)
gen_sadl_InstanceDifferentFrom_Statement = Generalization(general=Statement, specific=sadl_InstanceDifferentFrom)
gen_sadl_InstanceDeclarationStatement_Statement = Generalization(general=Statement, specific=sadl_InstanceDeclarationStatement)
gen_sadl_InstanceDeclaration_InstanceDeclarationStatement = Generalization(general=InstanceDeclarationStatement, specific=sadl_InstanceDeclaration)
gen_sadl_InstanceDeclaration_EmbeddedInstanceDeclaration = Generalization(general=EmbeddedInstanceDeclaration, specific=sadl_InstanceDeclaration)
gen_sadl_ExistingInstanceAttribution_Statement = Generalization(general=Statement, specific=sadl_ExistingInstanceAttribution)
gen_sadl_InstancesAllDifferent_Statement = Generalization(general=Statement, specific=sadl_InstancesAllDifferent)
gen_sadl_Rule_ModelElement = Generalization(general=ModelElement, specific=sadl_Rule)
gen_sadl_MergedTriples_GraphPattern = Generalization(general=GraphPattern, specific=sadl_MergedTriples)
gen_sadl_Query_ModelElement = Generalization(general=ModelElement, specific=sadl_Query)
gen_sadl_Test_ModelElement = Generalization(general=ModelElement, specific=sadl_Test)
gen_sadl_Expr_ModelElement = Generalization(general=ModelElement, specific=sadl_Expr)
gen_sadl_Display_ModelElement = Generalization(general=ModelElement, specific=sadl_Display)
gen_sadl_Explanation_ModelElement = Generalization(general=ModelElement, specific=sadl_Explanation)
gen_sadl_SelectExpression_Expression = Generalization(general=Expression, specific=sadl_SelectExpression)
gen_sadl_ConstructExpression_Expression = Generalization(general=Expression, specific=sadl_ConstructExpression)
gen_sadl_AskQueryExpression_Expression = Generalization(general=Expression, specific=sadl_AskQueryExpression)
gen_sadl_SubjProp_GraphPattern = Generalization(general=GraphPattern, specific=sadl_SubjProp)
gen_sadl_InstAttrSPV_GraphPattern = Generalization(general=GraphPattern, specific=sadl_InstAttrSPV)
gen_sadl_PropOfSubj_GraphPattern = Generalization(general=GraphPattern, specific=sadl_PropOfSubj)
gen_sadl_InstAttrPSV_GraphPattern = Generalization(general=GraphPattern, specific=sadl_InstAttrPSV)
gen_sadl_ExistentialNegation_GraphPattern = Generalization(general=GraphPattern, specific=sadl_ExistentialNegation)
gen_sadl_SubTypeOf_GraphPattern = Generalization(general=GraphPattern, specific=sadl_SubTypeOf)
gen_sadl_JunctionExpression_Expression = Generalization(general=Expression, specific=sadl_JunctionExpression)
gen_sadl_BinaryOpExpression_Expression = Generalization(general=Expression, specific=sadl_BinaryOpExpression)
gen_sadl_UnaryOpExpression_Expression = Generalization(general=Expression, specific=sadl_UnaryOpExpression)

# Domain Model
domain_model = DomainModel(
    name="sadl",
    types={sadl_Model, sadl_ModelName, sadl_Statement, ModelElement, sadl_ResourceName, sadl_Import, sadl_ModelElement, sadl_ContentList, sadl_ExistingResourceList, sadl_ResourceIdentifier, sadl_ResourceBySetOp, sadl_ResourceList, sadl_LiteralList, sadl_LiteralValue, sadl_ResourceByName, ResourceIdentifier, sadl_UnionResource, ResourceBySetOp, sadl_IntersectionResource, sadl_ClassDeclaration, Statement, sadl_EnumeratedInstances, sadl_AddlClassInfo, sadl_ResourceByRestriction, sadl_Condition, sadl_Range, sadl_RangeType, sadl_UserDefinedDataType, sadl_DataTypeRestriction, sadl_Facets, sadl_EquivalentConcepts, sadl_ComplementOfClass, sadl_DisjointClasses, sadl_AllValuesFrom, sadl_PropertyOfClass, sadl_AllValuesCondition, sadl_HasValue, sadl_SomeValuesFrom, sadl_SomeValuesCondition, sadl_Cardinality, sadl_CardCondition, sadl_HasValueCondition, sadl_MaxCardinality, sadl_MaxCardCondition, sadl_MinCardinality, sadl_MinCardCondition, sadl_EObject, sadl_EnumeratedAllAndSomeValuesFrom, sadl_DefaultValue, Condition, sadl_EnumeratedAllValuesFrom, sadl_ExplicitValue, sadl_PropertyDeclaration, sadl_AdditionalPropertyInfo, sadl_NecessaryAndSufficient, sadl_TypedBNode, sadl_IsInverseOf, sadl_TransitiveProperty, sadl_InverseProperty, sadl_FunctionalProperty, sadl_InverseFunctionalProperty, sadl_SymmetricalProperty, sadl_PropValPartialTriple, sadl_InstanceDifferentFrom, sadl_InstanceDeclarationStatement, sadl_InstanceDeclaration, InstanceDeclarationStatement, EmbeddedInstanceDeclaration, sadl_TypeDeclaration, sadl_ExistingInstanceAttribution, sadl_OfPatternReturningValues, sadl_Object, sadl_InstancesAllDifferent, sadl_OfPhrase, sadl_WithChain, sadl_WithPhrase, sadl_VariableList, sadl_Rule, sadl_EmbeddedInstanceDeclaration, sadl_MergedTriples, GraphPattern, sadl_Query, sadl_Expression, sadl_Test, sadl_Expr, sadl_Display, sadl_Explanation, sadl_ElementSet, Expression, sadl_OrderList, sadl_ConstructExpression, sadl_SelectExpression, sadl_GraphPattern, sadl_IntervalValue, sadl_ValueTable, sadl_AskQueryExpression, sadl_OrderElement, sadl_SubjProp, sadl_InstAttrSPV, sadl_PropOfSubj, sadl_InstAttrPSV, sadl_ExistentialNegation, sadl_SubTypeOf, sadl_ValueRow, sadl_BinaryOpExpression, sadl_UnaryOpExpression, sadl_JunctionExpression, DataType},
    associations={modelName0, annContent7, imports1, elements3, annContent5, names14, annContent15, names17, names9, literals11, name12, className27, mustBeOneOf29, describedBy31, annContent20, propName22, cond25, range48, restriction50, type53, classList33, classIdentifier36, instanceList39, propertyByName42, propertyName45, classIdentifier55, userDefinedDataType58, restriction60, facets62, class164, class266, class177, class279, class169, class271, classes74, className85, propertyName88, restricted82, cond83, className95, propertyName98, restricted91, cond93, restricted111, cond113, className115, propertyName118, restricted101, cond103, className105, propertyName108, restricted131, cond133, className135, propertyName138, restricted121, cond123, className125, propertyName128, enumeration152, restricted154, enumeration156, propertyName141, className144, restriction147, restricted150, classQualifier169, classQualifier172, defValueClass159, defValue161, restriction163, restriction166, cond185, propertyName188, superPropName190, addlPropInfo193, classQualifier175, superClass178, subClass179, propertyName182, cond207, range210, domain195, rangeResource198, annotationProperty201, domain204, propertyName221, propertyName1223, invOf225, isInvOf213, propertyName215, propertyName217, propertyName219, typeDecl234, addlInfoItems235, className237, instanceName240, instName243, propertyName2228, type246, classIdentifier231, instances254, subj256, addlInfoItems258, pOfS261, obj263, val266, instName1249, instName2251, objectValueBNode274, ofphrs277, subject279, type282, wps285, propertyName286, propertyName268, objectValue271, ops292, pivot294, wcs297, propertyName300, names303, value289, expr312, expr313, expr315, givens305, ifs306, thens309, varList322, orderList324, subj326, pred328, obj331, expr317, elements319, name336, expr340, args343, gp345, ivalue347, value349, orderList334, subj356, subj359, hwPhr361, subj364, valueTable352, ofPhr354, vals369, prop372, val374, props366, subclass377, superclass379, varList382, quantified384, expr387, instName390, litValue393, row396, rows398, left404, right406, left409, right411, explicitValues401},
    generalizations={gen_sadl_Statement_ModelElement, gen_sadl_ResourceBySetOp_ResourceIdentifier, gen_sadl_ResourceByName_ResourceIdentifier, gen_sadl_UnionResource_ResourceBySetOp, gen_sadl_IntersectionResource_ResourceBySetOp, gen_sadl_ClassDeclaration_Statement, gen_sadl_ResourceByRestriction_ResourceIdentifier, gen_sadl_UserDefinedDataType_Statement, gen_sadl_EquivalentConcepts_Statement, gen_sadl_ComplementOfClass_Statement, gen_sadl_DisjointClasses_Statement, gen_sadl_AllValuesFrom_Statement, gen_sadl_HasValue_Statement, gen_sadl_SomeValuesFrom_Statement, gen_sadl_Cardinality_Statement, gen_sadl_MaxCardinality_Statement, gen_sadl_MinCardinality_Statement, gen_sadl_EnumeratedAllAndSomeValuesFrom_Statement, gen_sadl_DefaultValue_Statement, gen_sadl_AllValuesCondition_Condition, gen_sadl_EnumeratedAllValuesFrom_Statement, gen_sadl_MinCardCondition_Condition, gen_sadl_MaxCardCondition_Condition, gen_sadl_CardCondition_Condition, gen_sadl_SomeValuesCondition_Condition, gen_sadl_HasValueCondition_Condition, gen_sadl_PropertyDeclaration_Statement, gen_sadl_NecessaryAndSufficient_Statement, gen_sadl_TransitiveProperty_Statement, gen_sadl_InverseProperty_Statement, gen_sadl_FunctionalProperty_Statement, gen_sadl_InverseFunctionalProperty_Statement, gen_sadl_SymmetricalProperty_Statement, gen_sadl_InstanceDifferentFrom_Statement, gen_sadl_InstanceDeclarationStatement_Statement, gen_sadl_InstanceDeclaration_InstanceDeclarationStatement, gen_sadl_InstanceDeclaration_EmbeddedInstanceDeclaration, gen_sadl_ExistingInstanceAttribution_Statement, gen_sadl_InstancesAllDifferent_Statement, gen_sadl_Rule_ModelElement, gen_sadl_MergedTriples_GraphPattern, gen_sadl_Query_ModelElement, gen_sadl_Test_ModelElement, gen_sadl_Expr_ModelElement, gen_sadl_Display_ModelElement, gen_sadl_Explanation_ModelElement, gen_sadl_SelectExpression_Expression, gen_sadl_ConstructExpression_Expression, gen_sadl_AskQueryExpression_Expression, gen_sadl_SubjProp_GraphPattern, gen_sadl_InstAttrSPV_GraphPattern, gen_sadl_PropOfSubj_GraphPattern, gen_sadl_InstAttrPSV_GraphPattern, gen_sadl_ExistentialNegation_GraphPattern, gen_sadl_SubTypeOf_GraphPattern, gen_sadl_JunctionExpression_Expression, gen_sadl_BinaryOpExpression_Expression, gen_sadl_UnaryOpExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)