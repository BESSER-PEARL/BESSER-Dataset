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

# Classes
henshin_Graph = Class(name="henshin::Graph")
henshin_Parameter = Class(name="henshin::Parameter")
henshin_ParameterMapping = Class(name="henshin::ParameterMapping")
henshin_NamedElement = Class(name="henshin::NamedElement", is_abstract=True)
henshin_GraphElement = Class(name="henshin::GraphElement", is_abstract=True)
henshin_Module = Class(name="henshin::Module")
NamedElement = Class(name="NamedElement")
henshin_EPackage = Class(name="henshin::EPackage")
henshin_Unit = Class(name="henshin::Unit", is_abstract=True)
henshin_AttributeCondition = Class(name="henshin::AttributeCondition")
henshin_Mapping = Class(name="henshin::Mapping")
henshin_Rule = Class(name="henshin::Rule")
Unit = Class(name="Unit")
henshin_Node = Class(name="henshin::Node")
henshin_EClassifier = Class(name="henshin::EClassifier")
henshin_Attribute = Class(name="henshin::Attribute")
henshin_Edge = Class(name="henshin::Edge")
henshin_Formula = Class(name="henshin::Formula", is_abstract=True)
GraphElement = Class(name="GraphElement")
henshin_EClass = Class(name="henshin::EClass")
henshin_UnaryUnit = Class(name="henshin::UnaryUnit", is_abstract=True)
henshin_MultiUnit = Class(name="henshin::MultiUnit", is_abstract=True)
henshin_IndependentUnit = Class(name="henshin::IndependentUnit")
MultiUnit = Class(name="MultiUnit")
henshin_SequentialUnit = Class(name="henshin::SequentialUnit")
henshin_EReference = Class(name="henshin::EReference")
henshin_EAttribute = Class(name="henshin::EAttribute")
henshin_UnaryFormula = Class(name="henshin::UnaryFormula", is_abstract=True)
henshin_BinaryFormula = Class(name="henshin::BinaryFormula", is_abstract=True)
henshin_ConditionalUnit = Class(name="henshin::ConditionalUnit")
henshin_PriorityUnit = Class(name="henshin::PriorityUnit")
henshin_IteratedUnit = Class(name="henshin::IteratedUnit")
UnaryUnit = Class(name="UnaryUnit")
henshin_LoopUnit = Class(name="henshin::LoopUnit")
henshin_NestedCondition = Class(name="henshin::NestedCondition")
Formula = Class(name="Formula")
henshin_And = Class(name="henshin::And")
BinaryFormula = Class(name="BinaryFormula")
henshin_Or = Class(name="henshin::Or")
henshin_Xor = Class(name="henshin::Xor")
henshin_Not = Class(name="henshin::Not")
UnaryFormula = Class(name="UnaryFormula")
henshin_True = Class(name="henshin::True")

# henshin_Graph class attributes and methods
henshin_Graph_m_getNestedConditions: Method = Method(name="getNestedConditions", parameters={}, type=StringType)
henshin_Graph_m_getPAC: Method = Method(name="getPAC", parameters={Parameter(name='name')}, type=StringType)
henshin_Graph_m_getNAC: Method = Method(name="getNAC", parameters={Parameter(name='name')}, type=StringType)
henshin_Graph_m_getPACs: Method = Method(name="getPACs", parameters={}, type=StringType)
henshin_Graph_m_getNACs: Method = Method(name="getNACs", parameters={}, type=StringType)
henshin_Graph_m_isLhs: Method = Method(name="isLhs", parameters={}, type=BooleanType)
henshin_Graph_m_isRhs: Method = Method(name="isRhs", parameters={}, type=BooleanType)
henshin_Graph_m_isNestedCondition: Method = Method(name="isNestedCondition", parameters={}, type=BooleanType)
henshin_Graph_m_createPAC: Method = Method(name="createPAC", parameters={Parameter(name='name')}, type=StringType)
henshin_Graph_m_createNAC: Method = Method(name="createNAC", parameters={Parameter(name='name')}, type=StringType)
henshin_Graph_m_removeNode: Method = Method(name="removeNode", parameters={Parameter(name='node')}, type=BooleanType)
henshin_Graph_m_removeEdge: Method = Method(name="removeEdge", parameters={Parameter(name='edge')}, type=BooleanType)
henshin_Graph_m_removeNestedCondition: Method = Method(name="removeNestedCondition", parameters={Parameter(name='nestedCondition')}, type=BooleanType)
henshin_Graph_m_getRule: Method = Method(name="getRule", parameters={}, type=StringType)
henshin_Graph_m_getNode: Method = Method(name="getNode", parameters={Parameter(name='name')}, type=StringType)
henshin_Graph_m_getNodes: Method = Method(name="getNodes", parameters={Parameter(name='nodeType')}, type=StringType)
henshin_Graph_m_getEdges: Method = Method(name="getEdges", parameters={Parameter(name='edgeType')}, type=StringType)
henshin_Graph.methods={henshin_Graph_m_getNestedConditions, henshin_Graph_m_getNodes, henshin_Graph_m_isRhs, henshin_Graph_m_getRule, henshin_Graph_m_isLhs, henshin_Graph_m_createPAC, henshin_Graph_m_isNestedCondition, henshin_Graph_m_createNAC, henshin_Graph_m_getNode, henshin_Graph_m_getPAC, henshin_Graph_m_getNACs, henshin_Graph_m_removeNestedCondition, henshin_Graph_m_removeEdge, henshin_Graph_m_getEdges, henshin_Graph_m_removeNode, henshin_Graph_m_getNAC, henshin_Graph_m_getPACs}

# henshin_Parameter class attributes and methods

# henshin_ParameterMapping class attributes and methods

# henshin_NamedElement class attributes and methods
henshin_NamedElement_name: Property = Property(name="name", type=StringType)
henshin_NamedElement_description: Property = Property(name="description", type=StringType)
henshin_NamedElement.attributes={henshin_NamedElement_name, henshin_NamedElement_description}

# henshin_GraphElement class attributes and methods
henshin_GraphElement_action: Property = Property(name="action", type=StringType)
henshin_GraphElement_presenceCondition: Property = Property(name="presenceCondition", type=StringType)
henshin_GraphElement_m_getGraph: Method = Method(name="getGraph", parameters={}, type=StringType)
henshin_GraphElement.attributes={henshin_GraphElement_action, henshin_GraphElement_presenceCondition}
henshin_GraphElement.methods={henshin_GraphElement_m_getGraph}

# henshin_Module class attributes and methods
henshin_Module_m_getUnit: Method = Method(name="getUnit", parameters={Parameter(name='name')}, type=StringType)
henshin_Module_m_getSubModule: Method = Method(name="getSubModule", parameters={Parameter(name='name')}, type=StringType)
henshin_Module.methods={henshin_Module_m_getUnit, henshin_Module_m_getSubModule}

# NamedElement class attributes and methods

# henshin_EPackage class attributes and methods

# henshin_Unit class attributes and methods
henshin_Unit_activated: Property = Property(name="activated", type=BooleanType)
henshin_Unit_m_getModule: Method = Method(name="getModule", parameters={}, type=StringType)
henshin_Unit_m_getSubUnits: Method = Method(name="getSubUnits", parameters={Parameter(name='deep')}, type=StringType)
henshin_Unit_m_getParameter: Method = Method(name="getParameter", parameters={Parameter(name='parameter')}, type=StringType)
henshin_Unit.attributes={henshin_Unit_activated}
henshin_Unit.methods={henshin_Unit_m_getModule, henshin_Unit_m_getParameter, henshin_Unit_m_getSubUnits}

# henshin_AttributeCondition class attributes and methods
henshin_AttributeCondition_conditionText: Property = Property(name="conditionText", type=StringType)
henshin_AttributeCondition.attributes={henshin_AttributeCondition_conditionText}

# henshin_Mapping class attributes and methods

# henshin_Rule class attributes and methods
henshin_Rule_checkDangling: Property = Property(name="checkDangling", type=BooleanType)
henshin_Rule_injectiveMatching: Property = Property(name="injectiveMatching", type=BooleanType)
henshin_Rule_featureModel: Property = Property(name="featureModel", type=StringType)
henshin_Rule_injectiveMatchingPresenceCondition: Property = Property(name="injectiveMatchingPresenceCondition", type=StringType)
henshin_Rule_m_removeAttribute: Method = Method(name="removeAttribute", parameters={Parameter(name='removeMapped'), Parameter(name='attribute')}, type=BooleanType)
henshin_Rule_m_getKernelRule: Method = Method(name="getKernelRule", parameters={}, type=StringType)
henshin_Rule_m_getRootRule: Method = Method(name="getRootRule", parameters={}, type=StringType)
henshin_Rule_m_getMultiRule: Method = Method(name="getMultiRule", parameters={Parameter(name='name')}, type=StringType)
henshin_Rule_m_getMultiRulePath: Method = Method(name="getMultiRulePath", parameters={Parameter(name='multiRule')}, type=StringType)
henshin_Rule_m_getAllMultiRules: Method = Method(name="getAllMultiRules", parameters={}, type=StringType)
henshin_Rule_m_getAllMappings: Method = Method(name="getAllMappings", parameters={}, type=StringType)
henshin_Rule_m_getActionNodes: Method = Method(name="getActionNodes", parameters={Parameter(name='action')}, type=StringType)
henshin_Rule_m_getActionEdges: Method = Method(name="getActionEdges", parameters={Parameter(name='action')}, type=StringType)
henshin_Rule_m_getParameterNodes: Method = Method(name="getParameterNodes", parameters={}, type=StringType)
henshin_Rule_m_isMultiRule: Method = Method(name="isMultiRule", parameters={}, type=BooleanType)
henshin_Rule_m_createNode: Method = Method(name="createNode", parameters={Parameter(name='type')}, type=StringType)
henshin_Rule_m_createEdge: Method = Method(name="createEdge", parameters={Parameter(name='type'), Parameter(name='source'), Parameter(name='target')}, type=StringType)
henshin_Rule_m_canCreateEdge: Method = Method(name="canCreateEdge", parameters={Parameter(name='target'), Parameter(name='source'), Parameter(name='type')}, type=BooleanType)
henshin_Rule_m_removeEdge: Method = Method(name="removeEdge", parameters={Parameter(name='edge'), Parameter(name='removeMapped')}, type=BooleanType)
henshin_Rule_m_removeNode: Method = Method(name="removeNode", parameters={Parameter(name='node'), Parameter(name='removeMapped')}, type=BooleanType)
henshin_Rule.attributes={henshin_Rule_featureModel, henshin_Rule_checkDangling, henshin_Rule_injectiveMatching, henshin_Rule_injectiveMatchingPresenceCondition}
henshin_Rule.methods={henshin_Rule_m_getKernelRule, henshin_Rule_m_getActionEdges, henshin_Rule_m_getAllMappings, henshin_Rule_m_removeNode, henshin_Rule_m_getParameterNodes, henshin_Rule_m_removeAttribute, henshin_Rule_m_getMultiRule, henshin_Rule_m_isMultiRule, henshin_Rule_m_createEdge, henshin_Rule_m_removeEdge, henshin_Rule_m_canCreateEdge, henshin_Rule_m_getRootRule, henshin_Rule_m_getAllMultiRules, henshin_Rule_m_createNode, henshin_Rule_m_getMultiRulePath, henshin_Rule_m_getActionNodes}

# Unit class attributes and methods

# henshin_Node class attributes and methods
henshin_Node_m_getAllEdges: Method = Method(name="getAllEdges", parameters={}, type=StringType)
henshin_Node_m_getOutgoing: Method = Method(name="getOutgoing", parameters={Parameter(name='type')}, type=StringType)
henshin_Node_m_getIncoming: Method = Method(name="getIncoming", parameters={Parameter(name='type')}, type=StringType)
henshin_Node_m_getOutgoing: Method = Method(name="getOutgoing", parameters={Parameter(name='type'), Parameter(name='target')}, type=StringType)
henshin_Node_m_getIncoming: Method = Method(name="getIncoming", parameters={Parameter(name='source'), Parameter(name='type')}, type=StringType)
henshin_Node_m_getAttribute: Method = Method(name="getAttribute", parameters={Parameter(name='type')}, type=StringType)
henshin_Node_m_getActionAttributes: Method = Method(name="getActionAttributes", parameters={Parameter(name='action')}, type=StringType)
henshin_Node_m_getActionNode: Method = Method(name="getActionNode", parameters={}, type=StringType)
henshin_Node.methods={henshin_Node_m_getAttribute, henshin_Node_m_getAllEdges, henshin_Node_m_getActionNode, henshin_Node_m_getOutgoing, henshin_Node_m_getOutgoing, henshin_Node_m_getActionAttributes, henshin_Node_m_getIncoming, henshin_Node_m_getIncoming}

# henshin_EClassifier class attributes and methods

# henshin_Attribute class attributes and methods
henshin_Attribute_value: Property = Property(name="value", type=StringType)
henshin_Attribute_constant: Property = Property(name="constant", type=StringType)
henshin_Attribute_null: Property = Property(name="null", type=BooleanType)
henshin_Attribute_m_getActionAttribute: Method = Method(name="getActionAttribute", parameters={}, type=StringType)
henshin_Attribute.attributes={henshin_Attribute_null, henshin_Attribute_value, henshin_Attribute_constant}
henshin_Attribute.methods={henshin_Attribute_m_getActionAttribute}

# henshin_Edge class attributes and methods
henshin_Edge_index: Property = Property(name="index", type=StringType)
henshin_Edge_indexConstant: Property = Property(name="indexConstant", type=StringType)
henshin_Edge_m_getActionEdge: Method = Method(name="getActionEdge", parameters={}, type=StringType)
henshin_Edge.attributes={henshin_Edge_indexConstant, henshin_Edge_index}
henshin_Edge.methods={henshin_Edge_m_getActionEdge}

# henshin_Formula class attributes and methods
henshin_Formula_m_isTrue: Method = Method(name="isTrue", parameters={}, type=BooleanType)
henshin_Formula_m_isFalse: Method = Method(name="isFalse", parameters={}, type=BooleanType)
henshin_Formula.methods={henshin_Formula_m_isFalse, henshin_Formula_m_isTrue}

# GraphElement class attributes and methods

# henshin_EClass class attributes and methods

# henshin_UnaryUnit class attributes and methods

# henshin_MultiUnit class attributes and methods

# henshin_IndependentUnit class attributes and methods

# MultiUnit class attributes and methods

# henshin_SequentialUnit class attributes and methods
henshin_SequentialUnit_strict: Property = Property(name="strict", type=BooleanType)
henshin_SequentialUnit_rollback: Property = Property(name="rollback", type=BooleanType)
henshin_SequentialUnit.attributes={henshin_SequentialUnit_rollback, henshin_SequentialUnit_strict}

# henshin_EReference class attributes and methods

# henshin_EAttribute class attributes and methods

# henshin_UnaryFormula class attributes and methods

# henshin_BinaryFormula class attributes and methods

# henshin_ConditionalUnit class attributes and methods

# henshin_PriorityUnit class attributes and methods

# henshin_IteratedUnit class attributes and methods
henshin_IteratedUnit_iterations: Property = Property(name="iterations", type=StringType)
henshin_IteratedUnit.attributes={henshin_IteratedUnit_iterations}

# UnaryUnit class attributes and methods

# henshin_LoopUnit class attributes and methods

# henshin_NestedCondition class attributes and methods
henshin_NestedCondition_presenceCondition: Property = Property(name="presenceCondition", type=StringType)
henshin_NestedCondition_m_getHost: Method = Method(name="getHost", parameters={}, type=StringType)
henshin_NestedCondition_m_isPAC: Method = Method(name="isPAC", parameters={}, type=BooleanType)
henshin_NestedCondition_m_isNAC: Method = Method(name="isNAC", parameters={}, type=BooleanType)
henshin_NestedCondition.attributes={henshin_NestedCondition_presenceCondition}
henshin_NestedCondition.methods={henshin_NestedCondition_m_getHost, henshin_NestedCondition_m_isPAC, henshin_NestedCondition_m_isNAC}

# Formula class attributes and methods

# henshin_And class attributes and methods

# BinaryFormula class attributes and methods

# henshin_Or class attributes and methods

# henshin_Xor class attributes and methods

# henshin_Not class attributes and methods

# UnaryFormula class attributes and methods

# henshin_True class attributes and methods

# Relationships
units6: BinaryAssociation = BinaryAssociation(
    name="units6",
    ends={
        Property(name="henshin_Module7", type=henshin_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="henshin_Unit", type=henshin_Module, multiplicity=Multiplicity(1, 1))
    }
)
instances8: BinaryAssociation = BinaryAssociation(
    name="instances8",
    ends={
        Property(name="henshin_Graph", type=henshin_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Module9", type=henshin_Graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters10: BinaryAssociation = BinaryAssociation(
    name="parameters10",
    ends={
        Property(name="Parameter", type=henshin_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="unit", type=henshin_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterMappings11: BinaryAssociation = BinaryAssociation(
    name="parameterMappings11",
    ends={
        Property(name="henshin_ParameterMapping", type=henshin_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Unit12", type=henshin_ParameterMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subModules1: BinaryAssociation = BinaryAssociation(
    name="subModules1",
    ends={
        Property(name="Module", type=henshin_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="superModule", type=henshin_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superModule3: BinaryAssociation = BinaryAssociation(
    name="superModule3",
    ends={
        Property(name="Module4", type=henshin_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="subModules", type=henshin_Module, multiplicity=Multiplicity(0, 1))
    }
)
imports5: BinaryAssociation = BinaryAssociation(
    name="imports5",
    ends={
        Property(name="henshin_EPackage", type=henshin_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Module", type=henshin_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
lhs13: BinaryAssociation = BinaryAssociation(
    name="lhs13",
    ends={
        Property(name="henshin_Graph14", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule", type=henshin_Graph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs15: BinaryAssociation = BinaryAssociation(
    name="rhs15",
    ends={
        Property(name="henshin_Graph17", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule16", type=henshin_Graph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributeConditions18: BinaryAssociation = BinaryAssociation(
    name="attributeConditions18",
    ends={
        Property(name="AttributeCondition", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule", type=henshin_AttributeCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappings19: BinaryAssociation = BinaryAssociation(
    name="mappings19",
    ends={
        Property(name="henshin_Mapping", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule20", type=henshin_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiRules22: BinaryAssociation = BinaryAssociation(
    name="multiRules22",
    ends={
        Property(name="henshin_Rule23", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule21", type=henshin_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiMappings24: BinaryAssociation = BinaryAssociation(
    name="multiMappings24",
    ends={
        Property(name="henshin_Mapping26", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule25", type=henshin_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit27: BinaryAssociation = BinaryAssociation(
    name="unit27",
    ends={
        Property(name="Unit", type=henshin_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=henshin_Unit, multiplicity=Multiplicity(0, 1))
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="henshin_EClassifier", type=henshin_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Parameter", type=henshin_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
source29: BinaryAssociation = BinaryAssociation(
    name="source29",
    ends={
        Property(name="henshin_Parameter31", type=henshin_ParameterMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ParameterMapping30", type=henshin_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
target32: BinaryAssociation = BinaryAssociation(
    name="target32",
    ends={
        Property(name="henshin_Parameter34", type=henshin_ParameterMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ParameterMapping33", type=henshin_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
type40: BinaryAssociation = BinaryAssociation(
    name="type40",
    ends={
        Property(name="henshin_Node", type=henshin_EClass, multiplicity=Multiplicity(0, 1)),
        Property(name="henshin_EClass", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
attributes41: BinaryAssociation = BinaryAssociation(
    name="attributes41",
    ends={
        Property(name="Attribute", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=henshin_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph42: BinaryAssociation = BinaryAssociation(
    name="graph42",
    ends={
        Property(name="Graph", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=henshin_Graph, multiplicity=Multiplicity(0, 1))
    }
)
incoming43: BinaryAssociation = BinaryAssociation(
    name="incoming43",
    ends={
        Property(name="Edge44", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=henshin_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing45: BinaryAssociation = BinaryAssociation(
    name="outgoing45",
    ends={
        Property(name="Edge46", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=henshin_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
source47: BinaryAssociation = BinaryAssociation(
    name="source47",
    ends={
        Property(name="Node48", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
nodes35: BinaryAssociation = BinaryAssociation(
    name="nodes35",
    ends={
        Property(name="Node", type=henshin_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=henshin_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges36: BinaryAssociation = BinaryAssociation(
    name="edges36",
    ends={
        Property(name="Edge", type=henshin_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph37", type=henshin_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formula38: BinaryAssociation = BinaryAssociation(
    name="formula38",
    ends={
        Property(name="henshin_Formula", type=henshin_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Graph39", type=henshin_Formula, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
origin58: BinaryAssociation = BinaryAssociation(
    name="origin58",
    ends={
        Property(name="henshin_Node60", type=henshin_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Mapping59", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
image61: BinaryAssociation = BinaryAssociation(
    name="image61",
    ends={
        Property(name="henshin_Node63", type=henshin_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Mapping62", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
subUnit64: BinaryAssociation = BinaryAssociation(
    name="subUnit64",
    ends={
        Property(name="henshin_Unit65", type=henshin_UnaryUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_UnaryUnit", type=henshin_Unit, multiplicity=Multiplicity(1, 1))
    }
)
subUnits66: BinaryAssociation = BinaryAssociation(
    name="subUnits66",
    ends={
        Property(name="henshin_Unit67", type=henshin_MultiUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_MultiUnit", type=henshin_Unit, multiplicity=Multiplicity(0, 9999))
    }
)
target49: BinaryAssociation = BinaryAssociation(
    name="target49",
    ends={
        Property(name="Node50", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
type51: BinaryAssociation = BinaryAssociation(
    name="type51",
    ends={
        Property(name="henshin_EReference", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Edge", type=henshin_EReference, multiplicity=Multiplicity(0, 1))
    }
)
graph52: BinaryAssociation = BinaryAssociation(
    name="graph52",
    ends={
        Property(name="Graph53", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=henshin_Graph, multiplicity=Multiplicity(0, 1))
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="henshin_EAttribute", type=henshin_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Attribute", type=henshin_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
node55: BinaryAssociation = BinaryAssociation(
    name="node55",
    ends={
        Property(name="Node56", type=henshin_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=henshin_Node, multiplicity=Multiplicity(0, 1))
    }
)
rule57: BinaryAssociation = BinaryAssociation(
    name="rule57",
    ends={
        Property(name="Rule", type=henshin_AttributeCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="attributeConditions", type=henshin_Rule, multiplicity=Multiplicity(1, 1))
    }
)
conclusion76: BinaryAssociation = BinaryAssociation(
    name="conclusion76",
    ends={
        Property(name="henshin_Graph77", type=henshin_NestedCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_NestedCondition", type=henshin_Graph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappings78: BinaryAssociation = BinaryAssociation(
    name="mappings78",
    ends={
        Property(name="henshin_Mapping80", type=henshin_NestedCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_NestedCondition79", type=henshin_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child81: BinaryAssociation = BinaryAssociation(
    name="child81",
    ends={
        Property(name="henshin_Formula82", type=henshin_UnaryFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_UnaryFormula", type=henshin_Formula, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left83: BinaryAssociation = BinaryAssociation(
    name="left83",
    ends={
        Property(name="henshin_Formula84", type=henshin_BinaryFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_BinaryFormula", type=henshin_Formula, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
if68: BinaryAssociation = BinaryAssociation(
    name="if68",
    ends={
        Property(name="henshin_Unit69", type=henshin_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ConditionalUnit", type=henshin_Unit, multiplicity=Multiplicity(1, 1))
    }
)
then70: BinaryAssociation = BinaryAssociation(
    name="then70",
    ends={
        Property(name="henshin_Unit72", type=henshin_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ConditionalUnit71", type=henshin_Unit, multiplicity=Multiplicity(1, 1))
    }
)
else73: BinaryAssociation = BinaryAssociation(
    name="else73",
    ends={
        Property(name="henshin_Unit75", type=henshin_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ConditionalUnit74", type=henshin_Unit, multiplicity=Multiplicity(0, 1))
    }
)
right85: BinaryAssociation = BinaryAssociation(
    name="right85",
    ends={
        Property(name="henshin_Formula87", type=henshin_BinaryFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_BinaryFormula86", type=henshin_Formula, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_henshin_Unit_NamedElement = Generalization(general=NamedElement, specific=henshin_Unit)
gen_henshin_Module_NamedElement = Generalization(general=NamedElement, specific=henshin_Module)
gen_henshin_Rule_Unit = Generalization(general=Unit, specific=henshin_Rule)
gen_henshin_Parameter_NamedElement = Generalization(general=NamedElement, specific=henshin_Parameter)
gen_henshin_Graph_NamedElement = Generalization(general=NamedElement, specific=henshin_Graph)
gen_henshin_Edge_GraphElement = Generalization(general=GraphElement, specific=henshin_Edge)
gen_henshin_Node_NamedElement = Generalization(general=NamedElement, specific=henshin_Node)
gen_henshin_Node_GraphElement = Generalization(general=GraphElement, specific=henshin_Node)
gen_henshin_UnaryUnit_Unit = Generalization(general=Unit, specific=henshin_UnaryUnit)
gen_henshin_MultiUnit_Unit = Generalization(general=Unit, specific=henshin_MultiUnit)
gen_henshin_IndependentUnit_MultiUnit = Generalization(general=MultiUnit, specific=henshin_IndependentUnit)
gen_henshin_SequentialUnit_MultiUnit = Generalization(general=MultiUnit, specific=henshin_SequentialUnit)
gen_henshin_Attribute_GraphElement = Generalization(general=GraphElement, specific=henshin_Attribute)
gen_henshin_AttributeCondition_NamedElement = Generalization(general=NamedElement, specific=henshin_AttributeCondition)
gen_henshin_NestedCondition_Formula = Generalization(general=Formula, specific=henshin_NestedCondition)
gen_henshin_UnaryFormula_Formula = Generalization(general=Formula, specific=henshin_UnaryFormula)
gen_henshin_BinaryFormula_Formula = Generalization(general=Formula, specific=henshin_BinaryFormula)
gen_henshin_ConditionalUnit_Unit = Generalization(general=Unit, specific=henshin_ConditionalUnit)
gen_henshin_PriorityUnit_MultiUnit = Generalization(general=MultiUnit, specific=henshin_PriorityUnit)
gen_henshin_IteratedUnit_UnaryUnit = Generalization(general=UnaryUnit, specific=henshin_IteratedUnit)
gen_henshin_LoopUnit_UnaryUnit = Generalization(general=UnaryUnit, specific=henshin_LoopUnit)
gen_henshin_And_BinaryFormula = Generalization(general=BinaryFormula, specific=henshin_And)
gen_henshin_Or_BinaryFormula = Generalization(general=BinaryFormula, specific=henshin_Or)
gen_henshin_Xor_BinaryFormula = Generalization(general=BinaryFormula, specific=henshin_Xor)
gen_henshin_Not_UnaryFormula = Generalization(general=UnaryFormula, specific=henshin_Not)
gen_henshin_True_Formula = Generalization(general=Formula, specific=henshin_True)

# Domain Model
domain_model = DomainModel(
    name="henshin",
    types={henshin_Graph, henshin_Parameter, henshin_ParameterMapping, henshin_NamedElement, henshin_GraphElement, henshin_Module, NamedElement, henshin_EPackage, henshin_Unit, henshin_AttributeCondition, henshin_Mapping, henshin_Rule, Unit, henshin_Node, henshin_EClassifier, henshin_Attribute, henshin_Edge, henshin_Formula, GraphElement, henshin_EClass, henshin_UnaryUnit, henshin_MultiUnit, henshin_IndependentUnit, MultiUnit, henshin_SequentialUnit, henshin_EReference, henshin_EAttribute, henshin_UnaryFormula, henshin_BinaryFormula, henshin_ConditionalUnit, henshin_PriorityUnit, henshin_IteratedUnit, UnaryUnit, henshin_LoopUnit, henshin_NestedCondition, Formula, henshin_And, BinaryFormula, henshin_Or, henshin_Xor, henshin_Not, UnaryFormula, henshin_True},
    associations={units6, instances8, parameters10, parameterMappings11, subModules1, superModule3, imports5, lhs13, rhs15, attributeConditions18, mappings19, multiRules22, multiMappings24, unit27, type28, source29, target32, type40, attributes41, graph42, incoming43, outgoing45, source47, nodes35, edges36, formula38, origin58, image61, subUnit64, subUnits66, target49, type51, graph52, type54, node55, rule57, conclusion76, mappings78, child81, left83, if68, then70, else73, right85},
    generalizations={gen_henshin_Unit_NamedElement, gen_henshin_Module_NamedElement, gen_henshin_Rule_Unit, gen_henshin_Parameter_NamedElement, gen_henshin_Graph_NamedElement, gen_henshin_Edge_GraphElement, gen_henshin_Node_NamedElement, gen_henshin_Node_GraphElement, gen_henshin_UnaryUnit_Unit, gen_henshin_MultiUnit_Unit, gen_henshin_IndependentUnit_MultiUnit, gen_henshin_SequentialUnit_MultiUnit, gen_henshin_Attribute_GraphElement, gen_henshin_AttributeCondition_NamedElement, gen_henshin_NestedCondition_Formula, gen_henshin_UnaryFormula_Formula, gen_henshin_BinaryFormula_Formula, gen_henshin_ConditionalUnit_Unit, gen_henshin_PriorityUnit_MultiUnit, gen_henshin_IteratedUnit_UnaryUnit, gen_henshin_LoopUnit_UnaryUnit, gen_henshin_And_BinaryFormula, gen_henshin_Or_BinaryFormula, gen_henshin_Xor_BinaryFormula, gen_henshin_Not_UnaryFormula, gen_henshin_True_Formula},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)