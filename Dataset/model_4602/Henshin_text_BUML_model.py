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
ParameterKind: Enumeration = Enumeration(
    name="ParameterKind",
    literals={
            EnumerationLiteral(name="UNKNOWN"),
			EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT"),
			EnumerationLiteral(name="VAR")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="eBoolean"),
			EnumerationLiteral(name="eBooleanObject"),
			EnumerationLiteral(name="eByte"),
			EnumerationLiteral(name="eByteArray"),
			EnumerationLiteral(name="eByteObject"),
			EnumerationLiteral(name="eChar"),
			EnumerationLiteral(name="eCharacterObject"),
			EnumerationLiteral(name="eDate"),
			EnumerationLiteral(name="eDiagnosticChain"),
			EnumerationLiteral(name="eDouble"),
			EnumerationLiteral(name="eDoubleObject"),
			EnumerationLiteral(name="eEList"),
			EnumerationLiteral(name="eEnumerator"),
			EnumerationLiteral(name="eFeatureMap"),
			EnumerationLiteral(name="eFeatureMapEntry"),
			EnumerationLiteral(name="eFloat"),
			EnumerationLiteral(name="eFloatObject"),
			EnumerationLiteral(name="eInt"),
			EnumerationLiteral(name="eIntegerObject"),
			EnumerationLiteral(name="eTreeIterator"),
			EnumerationLiteral(name="eInvocationTargetException"),
			EnumerationLiteral(name="eJavaClass"),
			EnumerationLiteral(name="eJavaObject"),
			EnumerationLiteral(name="eLong"),
			EnumerationLiteral(name="eLongObject"),
			EnumerationLiteral(name="eMap"),
			EnumerationLiteral(name="eResource"),
			EnumerationLiteral(name="eResourceSet"),
			EnumerationLiteral(name="eShort"),
			EnumerationLiteral(name="eShortObject"),
			EnumerationLiteral(name="eString"),
			EnumerationLiteral(name="eBigDecimal"),
			EnumerationLiteral(name="eBigInteger")
    }
)

# Classes
henshin_text_Model = Class(name="henshin::text::Model")
henshin_text_EPackageImport = Class(name="henshin::text::EPackageImport")
henshin_text_ModelElement = Class(name="henshin::text::ModelElement")
henshin_text_EPackage = Class(name="henshin::text::EPackage")
henshin_text_Parameter = Class(name="henshin::text::Parameter")
henshin_text_RuleElement = Class(name="henshin::text::RuleElement")
henshin_text_JavaImport = Class(name="henshin::text::JavaImport")
RuleElement = Class(name="RuleElement")
henshin_text_CheckDangling = Class(name="henshin::text::CheckDangling")
henshin_text_InjectiveMatching = Class(name="henshin::text::InjectiveMatching")
henshin_text_Conditions = Class(name="henshin::text::Conditions")
henshin_text_Expression = Class(name="henshin::text::Expression")
henshin_text_Graph = Class(name="henshin::text::Graph")
henshin_text_GraphElements = Class(name="henshin::text::GraphElements")
henshin_text_Edges = Class(name="henshin::text::Edges")
GraphElements = Class(name="GraphElements")
henshin_text_Edge = Class(name="henshin::text::Edge")
henshin_text_RuleNodeTypes = Class(name="henshin::text::RuleNodeTypes")
henshin_text_EReference = Class(name="henshin::text::EReference")
henshin_text_Node = Class(name="henshin::text::Node")
RuleNodeTypes = Class(name="RuleNodeTypes")
ConditionNodeTypes = Class(name="ConditionNodeTypes")
henshin_text_Attribute = Class(name="henshin::text::Attribute")
henshin_text_MultiRuleReuseNode = Class(name="henshin::text::MultiRuleReuseNode")
henshin_text_EAttribute = Class(name="henshin::text::EAttribute")
henshin_text_MultiRule = Class(name="henshin::text::MultiRule")
henshin_text_Formula = Class(name="henshin::text::Formula")
ConditionGraphElements = Class(name="ConditionGraphElements")
henshin_text_Logic = Class(name="henshin::text::Logic")
henshin_text_ConditionGraph = Class(name="henshin::text::ConditionGraph")
henshin_text_ConditionGraphElements = Class(name="henshin::text::ConditionGraphElements")
henshin_text_ConditionEdges = Class(name="henshin::text::ConditionEdges")
henshin_text_ConditionEdge = Class(name="henshin::text::ConditionEdge")
henshin_text_EClass = Class(name="henshin::text::EClass")
henshin_text_ConditionNode = Class(name="henshin::text::ConditionNode")
henshin_text_Match = Class(name="henshin::text::Match")
henshin_text_ConditionReuseNode = Class(name="henshin::text::ConditionReuseNode")
henshin_text_UnitElement = Class(name="henshin::text::UnitElement")
henshin_text_SequentialProperties = Class(name="henshin::text::SequentialProperties")
UnitElement = Class(name="UnitElement")
henshin_text_Strict = Class(name="henshin::text::Strict")
SequentialProperties = Class(name="SequentialProperties")
henshin_text_Rollback = Class(name="henshin::text::Rollback")
henshin_text_List = Class(name="henshin::text::List")
henshin_text_ConditionNodeTypes = Class(name="henshin::text::ConditionNodeTypes")
henshin_text_ConditionalUnit = Class(name="henshin::text::ConditionalUnit")
henshin_text_PriorityUnit = Class(name="henshin::text::PriorityUnit")
henshin_text_IteratedUnit = Class(name="henshin::text::IteratedUnit")
henshin_text_LoopUnit = Class(name="henshin::text::LoopUnit")
henshin_text_ParameterType = Class(name="henshin::text::ParameterType")
henshin_text_IndependentUnit = Class(name="henshin::text::IndependentUnit")
henshin_text_Rule = Class(name="henshin::text::Rule")
ModelElement = Class(name="ModelElement")
henshin_text_Unit = Class(name="henshin::text::Unit")
henshin_text_ORorXOR = Class(name="henshin::text::ORorXOR")
Logic = Class(name="Logic")
henshin_text_AND = Class(name="henshin::text::AND")
henshin_text_Not = Class(name="henshin::text::Not")
henshin_text_ConditionGraphRef = Class(name="henshin::text::ConditionGraphRef")
henshin_text_Call = Class(name="henshin::text::Call")
henshin_text_OrExpression = Class(name="henshin::text::OrExpression")
Expression = Class(name="Expression")
henshin_text_AndExpression = Class(name="henshin::text::AndExpression")
henshin_text_EqualityExpression = Class(name="henshin::text::EqualityExpression")
henshin_text_ComparisonExpression = Class(name="henshin::text::ComparisonExpression")
henshin_text_PlusExpression = Class(name="henshin::text::PlusExpression")
henshin_text_MinusExpression = Class(name="henshin::text::MinusExpression")
henshin_text_MulOrDivExpression = Class(name="henshin::text::MulOrDivExpression")
henshin_text_BracketExpression = Class(name="henshin::text::BracketExpression")
henshin_text_NotExpression = Class(name="henshin::text::NotExpression")
henshin_text_ParameterValue = Class(name="henshin::text::ParameterValue")
henshin_text_JavaAttributeValue = Class(name="henshin::text::JavaAttributeValue")
henshin_text_StringValue = Class(name="henshin::text::StringValue")
henshin_text_NumberValue = Class(name="henshin::text::NumberValue")
henshin_text_IntegerValue = Class(name="henshin::text::IntegerValue")
henshin_text_NaturalValue = Class(name="henshin::text::NaturalValue")
henshin_text_BoolValue = Class(name="henshin::text::BoolValue")
henshin_text_JavaClassValue = Class(name="henshin::text::JavaClassValue")

# henshin_text_Model class attributes and methods

# henshin_text_EPackageImport class attributes and methods

# henshin_text_ModelElement class attributes and methods
henshin_text_ModelElement_name: Property = Property(name="name", type=StringType)
henshin_text_ModelElement.attributes={henshin_text_ModelElement_name}

# henshin_text_EPackage class attributes and methods

# henshin_text_Parameter class attributes and methods
henshin_text_Parameter_kind: Property = Property(name="kind", type=StringType)
henshin_text_Parameter_name: Property = Property(name="name", type=StringType)
henshin_text_Parameter.attributes={henshin_text_Parameter_name, henshin_text_Parameter_kind}

# henshin_text_RuleElement class attributes and methods

# henshin_text_JavaImport class attributes and methods
henshin_text_JavaImport_packagename: Property = Property(name="packagename", type=StringType)
henshin_text_JavaImport.attributes={henshin_text_JavaImport_packagename}

# RuleElement class attributes and methods

# henshin_text_CheckDangling class attributes and methods
henshin_text_CheckDangling_checkDangling: Property = Property(name="checkDangling", type=BooleanType)
henshin_text_CheckDangling.attributes={henshin_text_CheckDangling_checkDangling}

# henshin_text_InjectiveMatching class attributes and methods
henshin_text_InjectiveMatching_injectiveMatching: Property = Property(name="injectiveMatching", type=BooleanType)
henshin_text_InjectiveMatching.attributes={henshin_text_InjectiveMatching_injectiveMatching}

# henshin_text_Conditions class attributes and methods

# henshin_text_Expression class attributes and methods

# henshin_text_Graph class attributes and methods

# henshin_text_GraphElements class attributes and methods

# henshin_text_Edges class attributes and methods

# GraphElements class attributes and methods

# henshin_text_Edge class attributes and methods
henshin_text_Edge_actiontype: Property = Property(name="actiontype", type=StringType)
henshin_text_Edge.attributes={henshin_text_Edge_actiontype}

# henshin_text_RuleNodeTypes class attributes and methods

# henshin_text_EReference class attributes and methods

# henshin_text_Node class attributes and methods
henshin_text_Node_actiontype: Property = Property(name="actiontype", type=StringType)
henshin_text_Node.attributes={henshin_text_Node_actiontype}

# RuleNodeTypes class attributes and methods

# ConditionNodeTypes class attributes and methods

# henshin_text_Attribute class attributes and methods
henshin_text_Attribute_actiontype: Property = Property(name="actiontype", type=StringType)
henshin_text_Attribute_update: Property = Property(name="update", type=StringType)
henshin_text_Attribute.attributes={henshin_text_Attribute_update, henshin_text_Attribute_actiontype}

# henshin_text_MultiRuleReuseNode class attributes and methods

# henshin_text_EAttribute class attributes and methods

# henshin_text_MultiRule class attributes and methods
henshin_text_MultiRule_name: Property = Property(name="name", type=StringType)
henshin_text_MultiRule.attributes={henshin_text_MultiRule_name}

# henshin_text_Formula class attributes and methods

# ConditionGraphElements class attributes and methods

# henshin_text_Logic class attributes and methods

# henshin_text_ConditionGraph class attributes and methods
henshin_text_ConditionGraph_name: Property = Property(name="name", type=StringType)
henshin_text_ConditionGraph.attributes={henshin_text_ConditionGraph_name}

# henshin_text_ConditionGraphElements class attributes and methods

# henshin_text_ConditionEdges class attributes and methods

# henshin_text_ConditionEdge class attributes and methods

# henshin_text_EClass class attributes and methods

# henshin_text_ConditionNode class attributes and methods

# henshin_text_Match class attributes and methods

# henshin_text_ConditionReuseNode class attributes and methods

# henshin_text_UnitElement class attributes and methods

# henshin_text_SequentialProperties class attributes and methods

# UnitElement class attributes and methods

# henshin_text_Strict class attributes and methods
henshin_text_Strict_strict: Property = Property(name="strict", type=BooleanType)
henshin_text_Strict.attributes={henshin_text_Strict_strict}

# SequentialProperties class attributes and methods

# henshin_text_Rollback class attributes and methods
henshin_text_Rollback_rollback: Property = Property(name="rollback", type=BooleanType)
henshin_text_Rollback.attributes={henshin_text_Rollback_rollback}

# henshin_text_List class attributes and methods

# henshin_text_ConditionNodeTypes class attributes and methods
henshin_text_ConditionNodeTypes_name: Property = Property(name="name", type=StringType)
henshin_text_ConditionNodeTypes.attributes={henshin_text_ConditionNodeTypes_name}

# henshin_text_ConditionalUnit class attributes and methods

# henshin_text_PriorityUnit class attributes and methods

# henshin_text_IteratedUnit class attributes and methods

# henshin_text_LoopUnit class attributes and methods

# henshin_text_ParameterType class attributes and methods
henshin_text_ParameterType_enumType: Property = Property(name="enumType", type=StringType)
henshin_text_ParameterType.attributes={henshin_text_ParameterType_enumType}

# henshin_text_IndependentUnit class attributes and methods

# henshin_text_Rule class attributes and methods

# ModelElement class attributes and methods

# henshin_text_Unit class attributes and methods

# henshin_text_ORorXOR class attributes and methods
henshin_text_ORorXOR_op: Property = Property(name="op", type=StringType)
henshin_text_ORorXOR.attributes={henshin_text_ORorXOR_op}

# Logic class attributes and methods

# henshin_text_AND class attributes and methods

# henshin_text_Not class attributes and methods

# henshin_text_ConditionGraphRef class attributes and methods

# henshin_text_Call class attributes and methods

# henshin_text_OrExpression class attributes and methods

# Expression class attributes and methods

# henshin_text_AndExpression class attributes and methods

# henshin_text_EqualityExpression class attributes and methods
henshin_text_EqualityExpression_op: Property = Property(name="op", type=StringType)
henshin_text_EqualityExpression.attributes={henshin_text_EqualityExpression_op}

# henshin_text_ComparisonExpression class attributes and methods
henshin_text_ComparisonExpression_op: Property = Property(name="op", type=StringType)
henshin_text_ComparisonExpression.attributes={henshin_text_ComparisonExpression_op}

# henshin_text_PlusExpression class attributes and methods

# henshin_text_MinusExpression class attributes and methods

# henshin_text_MulOrDivExpression class attributes and methods
henshin_text_MulOrDivExpression_op: Property = Property(name="op", type=StringType)
henshin_text_MulOrDivExpression.attributes={henshin_text_MulOrDivExpression_op}

# henshin_text_BracketExpression class attributes and methods

# henshin_text_NotExpression class attributes and methods

# henshin_text_ParameterValue class attributes and methods

# henshin_text_JavaAttributeValue class attributes and methods
henshin_text_JavaAttributeValue_value: Property = Property(name="value", type=StringType)
henshin_text_JavaAttributeValue.attributes={henshin_text_JavaAttributeValue_value}

# henshin_text_StringValue class attributes and methods
henshin_text_StringValue_value: Property = Property(name="value", type=StringType)
henshin_text_StringValue.attributes={henshin_text_StringValue_value}

# henshin_text_NumberValue class attributes and methods
henshin_text_NumberValue_value: Property = Property(name="value", type=StringType)
henshin_text_NumberValue.attributes={henshin_text_NumberValue_value}

# henshin_text_IntegerValue class attributes and methods
henshin_text_IntegerValue_value: Property = Property(name="value", type=StringType)
henshin_text_IntegerValue.attributes={henshin_text_IntegerValue_value}

# henshin_text_NaturalValue class attributes and methods
henshin_text_NaturalValue_value: Property = Property(name="value", type=IntegerType)
henshin_text_NaturalValue.attributes={henshin_text_NaturalValue_value}

# henshin_text_BoolValue class attributes and methods
henshin_text_BoolValue_value: Property = Property(name="value", type=BooleanType)
henshin_text_BoolValue.attributes={henshin_text_BoolValue_value}

# henshin_text_JavaClassValue class attributes and methods
henshin_text_JavaClassValue_value: Property = Property(name="value", type=StringType)
henshin_text_JavaClassValue.attributes={henshin_text_JavaClassValue_value}

# Relationships
ePackageimports0: BinaryAssociation = BinaryAssociation(
    name="ePackageimports0",
    ends={
        Property(name="henshin_text_EPackageImport", type=henshin_text_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Model", type=henshin_text_EPackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformationsystem1: BinaryAssociation = BinaryAssociation(
    name="transformationsystem1",
    ends={
        Property(name="henshin_text_ModelElement", type=henshin_text_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Model2", type=henshin_text_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref3: BinaryAssociation = BinaryAssociation(
    name="ref3",
    ends={
        Property(name="henshin_text_EPackage", type=henshin_text_EPackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_EPackageImport4", type=henshin_text_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
parameters5: BinaryAssociation = BinaryAssociation(
    name="parameters5",
    ends={
        Property(name="henshin_text_Parameter", type=henshin_text_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ModelElement6", type=henshin_text_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeConditions7: BinaryAssociation = BinaryAssociation(
    name="attributeConditions7",
    ends={
        Property(name="henshin_text_Expression", type=henshin_text_Conditions, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Conditions", type=henshin_text_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphElements8: BinaryAssociation = BinaryAssociation(
    name="graphElements8",
    ends={
        Property(name="henshin_text_GraphElements", type=henshin_text_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Graph", type=henshin_text_GraphElements, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges9: BinaryAssociation = BinaryAssociation(
    name="edges9",
    ends={
        Property(name="henshin_text_Edge", type=henshin_text_Edges, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Edges", type=henshin_text_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="henshin_text_RuleNodeTypes", type=henshin_text_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Edge11", type=henshin_text_RuleNodeTypes, multiplicity=Multiplicity(0, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="henshin_text_RuleNodeTypes14", type=henshin_text_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Edge13", type=henshin_text_RuleNodeTypes, multiplicity=Multiplicity(0, 1))
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="henshin_text_EReference", type=henshin_text_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Edge16", type=henshin_text_EReference, multiplicity=Multiplicity(0, 1))
    }
)
attribute18: BinaryAssociation = BinaryAssociation(
    name="attribute18",
    ends={
        Property(name="henshin_text_Attribute", type=henshin_text_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Node19", type=henshin_text_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name20: BinaryAssociation = BinaryAssociation(
    name="name20",
    ends={
        Property(name="henshin_text_Node21", type=henshin_text_MultiRuleReuseNode, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_MultiRuleReuseNode", type=henshin_text_Node, multiplicity=Multiplicity(0, 1))
    }
)
attribute22: BinaryAssociation = BinaryAssociation(
    name="attribute22",
    ends={
        Property(name="henshin_text_Attribute24", type=henshin_text_MultiRuleReuseNode, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_MultiRuleReuseNode23", type=henshin_text_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name25: BinaryAssociation = BinaryAssociation(
    name="name25",
    ends={
        Property(name="henshin_text_EAttribute", type=henshin_text_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Attribute26", type=henshin_text_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
value27: BinaryAssociation = BinaryAssociation(
    name="value27",
    ends={
        Property(name="henshin_text_Expression29", type=henshin_text_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Attribute28", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiruleElements30: BinaryAssociation = BinaryAssociation(
    name="multiruleElements30",
    ends={
        Property(name="henshin_text_RuleElement", type=henshin_text_MultiRule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_MultiRule", type=henshin_text_RuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formula31: BinaryAssociation = BinaryAssociation(
    name="formula31",
    ends={
        Property(name="henshin_text_Logic", type=henshin_text_Formula, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Formula", type=henshin_text_Logic, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionGraphs32: BinaryAssociation = BinaryAssociation(
    name="conditionGraphs32",
    ends={
        Property(name="henshin_text_ConditionGraph", type=henshin_text_Formula, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Formula33", type=henshin_text_ConditionGraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionGraphElements34: BinaryAssociation = BinaryAssociation(
    name="conditionGraphElements34",
    ends={
        Property(name="henshin_text_ConditionGraphElements", type=henshin_text_ConditionGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionGraph35", type=henshin_text_ConditionGraphElements, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges36: BinaryAssociation = BinaryAssociation(
    name="edges36",
    ends={
        Property(name="henshin_text_ConditionEdge", type=henshin_text_ConditionEdges, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionEdges", type=henshin_text_ConditionEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodetype17: BinaryAssociation = BinaryAssociation(
    name="nodetype17",
    ends={
        Property(name="henshin_text_EClass", type=henshin_text_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Node", type=henshin_text_EClass, multiplicity=Multiplicity(0, 1))
    }
)
target39: BinaryAssociation = BinaryAssociation(
    name="target39",
    ends={
        Property(name="henshin_text_ConditionNodeTypes41", type=henshin_text_ConditionEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionEdge40", type=henshin_text_ConditionNodeTypes, multiplicity=Multiplicity(0, 1))
    }
)
type42: BinaryAssociation = BinaryAssociation(
    name="type42",
    ends={
        Property(name="henshin_text_EReference44", type=henshin_text_ConditionEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionEdge43", type=henshin_text_EReference, multiplicity=Multiplicity(0, 1))
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="henshin_text_EClass46", type=henshin_text_ConditionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionNode", type=henshin_text_EClass, multiplicity=Multiplicity(0, 1))
    }
)
attribute47: BinaryAssociation = BinaryAssociation(
    name="attribute47",
    ends={
        Property(name="henshin_text_Match", type=henshin_text_ConditionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionNode48", type=henshin_text_Match, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name49: BinaryAssociation = BinaryAssociation(
    name="name49",
    ends={
        Property(name="henshin_text_ConditionNodeTypes50", type=henshin_text_ConditionReuseNode, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionReuseNode", type=henshin_text_ConditionNodeTypes, multiplicity=Multiplicity(0, 1))
    }
)
attribute51: BinaryAssociation = BinaryAssociation(
    name="attribute51",
    ends={
        Property(name="henshin_text_Match53", type=henshin_text_ConditionReuseNode, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionReuseNode52", type=henshin_text_Match, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name54: BinaryAssociation = BinaryAssociation(
    name="name54",
    ends={
        Property(name="henshin_text_EAttribute56", type=henshin_text_Match, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Match55", type=henshin_text_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
value57: BinaryAssociation = BinaryAssociation(
    name="value57",
    ends={
        Property(name="henshin_text_Expression59", type=henshin_text_Match, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Match58", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subSequence61: BinaryAssociation = BinaryAssociation(
    name="subSequence61",
    ends={
        Property(name="henshin_text_UnitElement", type=henshin_text_UnitElement, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_UnitElement60", type=henshin_text_UnitElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subElements62: BinaryAssociation = BinaryAssociation(
    name="subElements62",
    ends={
        Property(name="henshin_text_UnitElement63", type=henshin_text_List, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_List", type=henshin_text_UnitElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source37: BinaryAssociation = BinaryAssociation(
    name="source37",
    ends={
        Property(name="henshin_text_ConditionNodeTypes", type=henshin_text_ConditionEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionEdge38", type=henshin_text_ConditionNodeTypes, multiplicity=Multiplicity(0, 1))
    }
)
listOfLists64: BinaryAssociation = BinaryAssociation(
    name="listOfLists64",
    ends={
        Property(name="henshin_text_List65", type=henshin_text_IndependentUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_IndependentUnit", type=henshin_text_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if66: BinaryAssociation = BinaryAssociation(
    name="if66",
    ends={
        Property(name="henshin_text_UnitElement67", type=henshin_text_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionalUnit", type=henshin_text_UnitElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
then68: BinaryAssociation = BinaryAssociation(
    name="then68",
    ends={
        Property(name="henshin_text_UnitElement70", type=henshin_text_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionalUnit69", type=henshin_text_UnitElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else71: BinaryAssociation = BinaryAssociation(
    name="else71",
    ends={
        Property(name="henshin_text_UnitElement73", type=henshin_text_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionalUnit72", type=henshin_text_UnitElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listOfLists74: BinaryAssociation = BinaryAssociation(
    name="listOfLists74",
    ends={
        Property(name="henshin_text_List75", type=henshin_text_PriorityUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_PriorityUnit", type=henshin_text_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterations76: BinaryAssociation = BinaryAssociation(
    name="iterations76",
    ends={
        Property(name="henshin_text_Expression77", type=henshin_text_IteratedUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_IteratedUnit", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subElement78: BinaryAssociation = BinaryAssociation(
    name="subElement78",
    ends={
        Property(name="henshin_text_UnitElement80", type=henshin_text_IteratedUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_IteratedUnit79", type=henshin_text_UnitElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subElement81: BinaryAssociation = BinaryAssociation(
    name="subElement81",
    ends={
        Property(name="henshin_text_UnitElement82", type=henshin_text_LoopUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_LoopUnit", type=henshin_text_UnitElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type83: BinaryAssociation = BinaryAssociation(
    name="type83",
    ends={
        Property(name="henshin_text_ParameterType", type=henshin_text_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Parameter84", type=henshin_text_ParameterType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type85: BinaryAssociation = BinaryAssociation(
    name="type85",
    ends={
        Property(name="henshin_text_EClass87", type=henshin_text_ParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ParameterType86", type=henshin_text_EClass, multiplicity=Multiplicity(0, 1))
    }
)
ruleElements88: BinaryAssociation = BinaryAssociation(
    name="ruleElements88",
    ends={
        Property(name="henshin_text_RuleElement89", type=henshin_text_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Rule", type=henshin_text_RuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unitElements90: BinaryAssociation = BinaryAssociation(
    name="unitElements90",
    ends={
        Property(name="henshin_text_UnitElement91", type=henshin_text_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Unit", type=henshin_text_UnitElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right94: BinaryAssociation = BinaryAssociation(
    name="right94",
    ends={
        Property(name="henshin_text_Logic96", type=henshin_text_ORorXOR, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ORorXOR95", type=henshin_text_Logic, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left97: BinaryAssociation = BinaryAssociation(
    name="left97",
    ends={
        Property(name="henshin_text_Logic98", type=henshin_text_AND, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_AND", type=henshin_text_Logic, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right99: BinaryAssociation = BinaryAssociation(
    name="right99",
    ends={
        Property(name="henshin_text_Logic101", type=henshin_text_AND, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_AND100", type=henshin_text_Logic, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
negation102: BinaryAssociation = BinaryAssociation(
    name="negation102",
    ends={
        Property(name="henshin_text_Logic103", type=henshin_text_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Not", type=henshin_text_Logic, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionGraphRef104: BinaryAssociation = BinaryAssociation(
    name="conditionGraphRef104",
    ends={
        Property(name="henshin_text_ConditionGraph105", type=henshin_text_ConditionGraphRef, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ConditionGraphRef", type=henshin_text_ConditionGraph, multiplicity=Multiplicity(0, 1))
    }
)
elementCall106: BinaryAssociation = BinaryAssociation(
    name="elementCall106",
    ends={
        Property(name="henshin_text_ModelElement107", type=henshin_text_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Call", type=henshin_text_ModelElement, multiplicity=Multiplicity(0, 1))
    }
)
parameters108: BinaryAssociation = BinaryAssociation(
    name="parameters108",
    ends={
        Property(name="henshin_text_Parameter110", type=henshin_text_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_Call109", type=henshin_text_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
left111: BinaryAssociation = BinaryAssociation(
    name="left111",
    ends={
        Property(name="henshin_text_Expression112", type=henshin_text_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_OrExpression", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right113: BinaryAssociation = BinaryAssociation(
    name="right113",
    ends={
        Property(name="henshin_text_Expression115", type=henshin_text_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_OrExpression114", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left116: BinaryAssociation = BinaryAssociation(
    name="left116",
    ends={
        Property(name="henshin_text_Expression117", type=henshin_text_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_AndExpression", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right118: BinaryAssociation = BinaryAssociation(
    name="right118",
    ends={
        Property(name="henshin_text_Expression120", type=henshin_text_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_AndExpression119", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left121: BinaryAssociation = BinaryAssociation(
    name="left121",
    ends={
        Property(name="henshin_text_Expression122", type=henshin_text_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_EqualityExpression", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left92: BinaryAssociation = BinaryAssociation(
    name="left92",
    ends={
        Property(name="henshin_text_Logic93", type=henshin_text_ORorXOR, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ORorXOR", type=henshin_text_Logic, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left126: BinaryAssociation = BinaryAssociation(
    name="left126",
    ends={
        Property(name="henshin_text_Expression127", type=henshin_text_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ComparisonExpression", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right128: BinaryAssociation = BinaryAssociation(
    name="right128",
    ends={
        Property(name="henshin_text_Expression130", type=henshin_text_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ComparisonExpression129", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left131: BinaryAssociation = BinaryAssociation(
    name="left131",
    ends={
        Property(name="henshin_text_Expression132", type=henshin_text_PlusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_PlusExpression", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right133: BinaryAssociation = BinaryAssociation(
    name="right133",
    ends={
        Property(name="henshin_text_Expression135", type=henshin_text_PlusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_PlusExpression134", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left136: BinaryAssociation = BinaryAssociation(
    name="left136",
    ends={
        Property(name="henshin_text_Expression137", type=henshin_text_MinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_MinusExpression", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right138: BinaryAssociation = BinaryAssociation(
    name="right138",
    ends={
        Property(name="henshin_text_Expression140", type=henshin_text_MinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_MinusExpression139", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left141: BinaryAssociation = BinaryAssociation(
    name="left141",
    ends={
        Property(name="henshin_text_Expression142", type=henshin_text_MulOrDivExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_MulOrDivExpression", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right143: BinaryAssociation = BinaryAssociation(
    name="right143",
    ends={
        Property(name="henshin_text_Expression145", type=henshin_text_MulOrDivExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_MulOrDivExpression144", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression146: BinaryAssociation = BinaryAssociation(
    name="expression146",
    ends={
        Property(name="henshin_text_Expression147", type=henshin_text_BracketExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_BracketExpression", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression148: BinaryAssociation = BinaryAssociation(
    name="expression148",
    ends={
        Property(name="henshin_text_Expression149", type=henshin_text_NotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_NotExpression", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value150: BinaryAssociation = BinaryAssociation(
    name="value150",
    ends={
        Property(name="henshin_text_Parameter151", type=henshin_text_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_ParameterValue", type=henshin_text_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
right123: BinaryAssociation = BinaryAssociation(
    name="right123",
    ends={
        Property(name="henshin_text_Expression125", type=henshin_text_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_EqualityExpression124", type=henshin_text_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
javaParameter152: BinaryAssociation = BinaryAssociation(
    name="javaParameter152",
    ends={
        Property(name="henshin_text_Expression153", type=henshin_text_JavaClassValue, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_text_JavaClassValue", type=henshin_text_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_henshin_text_JavaImport_RuleElement = Generalization(general=RuleElement, specific=henshin_text_JavaImport)
gen_henshin_text_CheckDangling_RuleElement = Generalization(general=RuleElement, specific=henshin_text_CheckDangling)
gen_henshin_text_InjectiveMatching_RuleElement = Generalization(general=RuleElement, specific=henshin_text_InjectiveMatching)
gen_henshin_text_Conditions_RuleElement = Generalization(general=RuleElement, specific=henshin_text_Conditions)
gen_henshin_text_Graph_RuleElement = Generalization(general=RuleElement, specific=henshin_text_Graph)
gen_henshin_text_Edges_GraphElements = Generalization(general=GraphElements, specific=henshin_text_Edges)
gen_henshin_text_Node_GraphElements = Generalization(general=GraphElements, specific=henshin_text_Node)
gen_henshin_text_Node_RuleNodeTypes = Generalization(general=RuleNodeTypes, specific=henshin_text_Node)
gen_henshin_text_Node_ConditionNodeTypes = Generalization(general=ConditionNodeTypes, specific=henshin_text_Node)
gen_henshin_text_MultiRuleReuseNode_GraphElements = Generalization(general=GraphElements, specific=henshin_text_MultiRuleReuseNode)
gen_henshin_text_MultiRuleReuseNode_RuleNodeTypes = Generalization(general=RuleNodeTypes, specific=henshin_text_MultiRuleReuseNode)
gen_henshin_text_MultiRule_GraphElements = Generalization(general=GraphElements, specific=henshin_text_MultiRule)
gen_henshin_text_Formula_GraphElements = Generalization(general=GraphElements, specific=henshin_text_Formula)
gen_henshin_text_Formula_ConditionGraphElements = Generalization(general=ConditionGraphElements, specific=henshin_text_Formula)
gen_henshin_text_ConditionEdges_ConditionGraphElements = Generalization(general=ConditionGraphElements, specific=henshin_text_ConditionEdges)
gen_henshin_text_ConditionNode_ConditionGraphElements = Generalization(general=ConditionGraphElements, specific=henshin_text_ConditionNode)
gen_henshin_text_ConditionNode_ConditionNodeTypes = Generalization(general=ConditionNodeTypes, specific=henshin_text_ConditionNode)
gen_henshin_text_ConditionReuseNode_ConditionGraphElements = Generalization(general=ConditionGraphElements, specific=henshin_text_ConditionReuseNode)
gen_henshin_text_SequentialProperties_UnitElement = Generalization(general=UnitElement, specific=henshin_text_SequentialProperties)
gen_henshin_text_Strict_SequentialProperties = Generalization(general=SequentialProperties, specific=henshin_text_Strict)
gen_henshin_text_Rollback_SequentialProperties = Generalization(general=SequentialProperties, specific=henshin_text_Rollback)
gen_henshin_text_ConditionalUnit_UnitElement = Generalization(general=UnitElement, specific=henshin_text_ConditionalUnit)
gen_henshin_text_PriorityUnit_UnitElement = Generalization(general=UnitElement, specific=henshin_text_PriorityUnit)
gen_henshin_text_IteratedUnit_UnitElement = Generalization(general=UnitElement, specific=henshin_text_IteratedUnit)
gen_henshin_text_LoopUnit_UnitElement = Generalization(general=UnitElement, specific=henshin_text_LoopUnit)
gen_henshin_text_IndependentUnit_UnitElement = Generalization(general=UnitElement, specific=henshin_text_IndependentUnit)
gen_henshin_text_Rule_ModelElement = Generalization(general=ModelElement, specific=henshin_text_Rule)
gen_henshin_text_Unit_ModelElement = Generalization(general=ModelElement, specific=henshin_text_Unit)
gen_henshin_text_ORorXOR_Logic = Generalization(general=Logic, specific=henshin_text_ORorXOR)
gen_henshin_text_AND_Logic = Generalization(general=Logic, specific=henshin_text_AND)
gen_henshin_text_Not_Logic = Generalization(general=Logic, specific=henshin_text_Not)
gen_henshin_text_ConditionGraphRef_Logic = Generalization(general=Logic, specific=henshin_text_ConditionGraphRef)
gen_henshin_text_Call_UnitElement = Generalization(general=UnitElement, specific=henshin_text_Call)
gen_henshin_text_OrExpression_Expression = Generalization(general=Expression, specific=henshin_text_OrExpression)
gen_henshin_text_AndExpression_Expression = Generalization(general=Expression, specific=henshin_text_AndExpression)
gen_henshin_text_EqualityExpression_Expression = Generalization(general=Expression, specific=henshin_text_EqualityExpression)
gen_henshin_text_ComparisonExpression_Expression = Generalization(general=Expression, specific=henshin_text_ComparisonExpression)
gen_henshin_text_PlusExpression_Expression = Generalization(general=Expression, specific=henshin_text_PlusExpression)
gen_henshin_text_MinusExpression_Expression = Generalization(general=Expression, specific=henshin_text_MinusExpression)
gen_henshin_text_MulOrDivExpression_Expression = Generalization(general=Expression, specific=henshin_text_MulOrDivExpression)
gen_henshin_text_BracketExpression_Expression = Generalization(general=Expression, specific=henshin_text_BracketExpression)
gen_henshin_text_NotExpression_Expression = Generalization(general=Expression, specific=henshin_text_NotExpression)
gen_henshin_text_ParameterValue_Expression = Generalization(general=Expression, specific=henshin_text_ParameterValue)
gen_henshin_text_JavaAttributeValue_Expression = Generalization(general=Expression, specific=henshin_text_JavaAttributeValue)
gen_henshin_text_StringValue_Expression = Generalization(general=Expression, specific=henshin_text_StringValue)
gen_henshin_text_NumberValue_Expression = Generalization(general=Expression, specific=henshin_text_NumberValue)
gen_henshin_text_IntegerValue_Expression = Generalization(general=Expression, specific=henshin_text_IntegerValue)
gen_henshin_text_NaturalValue_Expression = Generalization(general=Expression, specific=henshin_text_NaturalValue)
gen_henshin_text_BoolValue_Expression = Generalization(general=Expression, specific=henshin_text_BoolValue)
gen_henshin_text_JavaClassValue_Expression = Generalization(general=Expression, specific=henshin_text_JavaClassValue)

# Domain Model
domain_model = DomainModel(
    name="henshin_text",
    types={henshin_text_Model, henshin_text_EPackageImport, henshin_text_ModelElement, henshin_text_EPackage, henshin_text_Parameter, henshin_text_RuleElement, henshin_text_JavaImport, RuleElement, henshin_text_CheckDangling, henshin_text_InjectiveMatching, henshin_text_Conditions, henshin_text_Expression, henshin_text_Graph, henshin_text_GraphElements, henshin_text_Edges, GraphElements, henshin_text_Edge, henshin_text_RuleNodeTypes, henshin_text_EReference, henshin_text_Node, RuleNodeTypes, ConditionNodeTypes, henshin_text_Attribute, henshin_text_MultiRuleReuseNode, henshin_text_EAttribute, henshin_text_MultiRule, henshin_text_Formula, ConditionGraphElements, henshin_text_Logic, henshin_text_ConditionGraph, henshin_text_ConditionGraphElements, henshin_text_ConditionEdges, henshin_text_ConditionEdge, henshin_text_EClass, henshin_text_ConditionNode, henshin_text_Match, henshin_text_ConditionReuseNode, henshin_text_UnitElement, henshin_text_SequentialProperties, UnitElement, henshin_text_Strict, SequentialProperties, henshin_text_Rollback, henshin_text_List, henshin_text_ConditionNodeTypes, henshin_text_ConditionalUnit, henshin_text_PriorityUnit, henshin_text_IteratedUnit, henshin_text_LoopUnit, henshin_text_ParameterType, henshin_text_IndependentUnit, henshin_text_Rule, ModelElement, henshin_text_Unit, henshin_text_ORorXOR, Logic, henshin_text_AND, henshin_text_Not, henshin_text_ConditionGraphRef, henshin_text_Call, henshin_text_OrExpression, Expression, henshin_text_AndExpression, henshin_text_EqualityExpression, henshin_text_ComparisonExpression, henshin_text_PlusExpression, henshin_text_MinusExpression, henshin_text_MulOrDivExpression, henshin_text_BracketExpression, henshin_text_NotExpression, henshin_text_ParameterValue, henshin_text_JavaAttributeValue, henshin_text_StringValue, henshin_text_NumberValue, henshin_text_IntegerValue, henshin_text_NaturalValue, henshin_text_BoolValue, henshin_text_JavaClassValue, ParameterKind, Type},
    associations={ePackageimports0, transformationsystem1, ref3, parameters5, attributeConditions7, graphElements8, edges9, source10, target12, type15, attribute18, name20, attribute22, name25, value27, multiruleElements30, formula31, conditionGraphs32, conditionGraphElements34, edges36, nodetype17, target39, type42, type45, attribute47, name49, attribute51, name54, value57, subSequence61, subElements62, source37, listOfLists64, if66, then68, else71, listOfLists74, iterations76, subElement78, subElement81, type83, type85, ruleElements88, unitElements90, right94, left97, right99, negation102, conditionGraphRef104, elementCall106, parameters108, left111, right113, left116, right118, left121, left92, left126, right128, left131, right133, left136, right138, left141, right143, expression146, expression148, value150, right123, javaParameter152},
    generalizations={gen_henshin_text_JavaImport_RuleElement, gen_henshin_text_CheckDangling_RuleElement, gen_henshin_text_InjectiveMatching_RuleElement, gen_henshin_text_Conditions_RuleElement, gen_henshin_text_Graph_RuleElement, gen_henshin_text_Edges_GraphElements, gen_henshin_text_Node_GraphElements, gen_henshin_text_Node_RuleNodeTypes, gen_henshin_text_Node_ConditionNodeTypes, gen_henshin_text_MultiRuleReuseNode_GraphElements, gen_henshin_text_MultiRuleReuseNode_RuleNodeTypes, gen_henshin_text_MultiRule_GraphElements, gen_henshin_text_Formula_GraphElements, gen_henshin_text_Formula_ConditionGraphElements, gen_henshin_text_ConditionEdges_ConditionGraphElements, gen_henshin_text_ConditionNode_ConditionGraphElements, gen_henshin_text_ConditionNode_ConditionNodeTypes, gen_henshin_text_ConditionReuseNode_ConditionGraphElements, gen_henshin_text_SequentialProperties_UnitElement, gen_henshin_text_Strict_SequentialProperties, gen_henshin_text_Rollback_SequentialProperties, gen_henshin_text_ConditionalUnit_UnitElement, gen_henshin_text_PriorityUnit_UnitElement, gen_henshin_text_IteratedUnit_UnitElement, gen_henshin_text_LoopUnit_UnitElement, gen_henshin_text_IndependentUnit_UnitElement, gen_henshin_text_Rule_ModelElement, gen_henshin_text_Unit_ModelElement, gen_henshin_text_ORorXOR_Logic, gen_henshin_text_AND_Logic, gen_henshin_text_Not_Logic, gen_henshin_text_ConditionGraphRef_Logic, gen_henshin_text_Call_UnitElement, gen_henshin_text_OrExpression_Expression, gen_henshin_text_AndExpression_Expression, gen_henshin_text_EqualityExpression_Expression, gen_henshin_text_ComparisonExpression_Expression, gen_henshin_text_PlusExpression_Expression, gen_henshin_text_MinusExpression_Expression, gen_henshin_text_MulOrDivExpression_Expression, gen_henshin_text_BracketExpression_Expression, gen_henshin_text_NotExpression_Expression, gen_henshin_text_ParameterValue_Expression, gen_henshin_text_JavaAttributeValue_Expression, gen_henshin_text_StringValue_Expression, gen_henshin_text_NumberValue_Expression, gen_henshin_text_IntegerValue_Expression, gen_henshin_text_NaturalValue_Expression, gen_henshin_text_BoolValue_Expression, gen_henshin_text_JavaClassValue_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)