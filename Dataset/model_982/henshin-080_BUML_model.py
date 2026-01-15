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
henshin_NamedElement = Class(name="henshin::NamedElement", is_abstract=True)
henshin_DescribedElement = Class(name="henshin::DescribedElement", is_abstract=True)
henshin_TransformationSystem = Class(name="henshin::TransformationSystem")
DescribedElement = Class(name="DescribedElement")
NamedElement = Class(name="NamedElement")
henshin_Graph = Class(name="henshin::Graph")
henshin_TransformationUnit = Class(name="henshin::TransformationUnit", is_abstract=True)
TransformationUnit = Class(name="TransformationUnit")
henshin_AttributeCondition = Class(name="henshin::AttributeCondition")
henshin_Mapping = Class(name="henshin::Mapping")
henshin_Rule = Class(name="henshin::Rule")
henshin_EPackage = Class(name="henshin::EPackage")
henshin_Node = Class(name="henshin::Node")
henshin_Edge = Class(name="henshin::Edge")
henshin_Formula = Class(name="henshin::Formula", is_abstract=True)
henshin_GraphElement = Class(name="henshin::GraphElement", is_abstract=True)
henshin_Parameter = Class(name="henshin::Parameter")
henshin_EClass = Class(name="henshin::EClass")
henshin_Attribute = Class(name="henshin::Attribute")
henshin_EAttribute = Class(name="henshin::EAttribute")
GraphElement = Class(name="GraphElement")
henshin_ParameterMapping = Class(name="henshin::ParameterMapping")
henshin_IndependentUnit = Class(name="henshin::IndependentUnit")
henshin_SequentialUnit = Class(name="henshin::SequentialUnit")
henshin_ConditionalUnit = Class(name="henshin::ConditionalUnit")
henshin_EReference = Class(name="henshin::EReference")
henshin_CountedUnit = Class(name="henshin::CountedUnit")
henshin_NestedCondition = Class(name="henshin::NestedCondition")
Formula = Class(name="Formula")
henshin_PriorityUnit = Class(name="henshin::PriorityUnit")
henshin_AmalgamationUnit = Class(name="henshin::AmalgamationUnit")
henshin_And = Class(name="henshin::And")
BinaryFormula = Class(name="BinaryFormula")
henshin_Or = Class(name="henshin::Or")
henshin_Xor = Class(name="henshin::Xor")
henshin_Not = Class(name="henshin::Not")
UnaryFormula = Class(name="UnaryFormula")
henshin_UnaryFormula = Class(name="henshin::UnaryFormula", is_abstract=True)
henshin_BinaryFormula = Class(name="henshin::BinaryFormula", is_abstract=True)

# henshin_NamedElement class attributes and methods
henshin_NamedElement_name: Property = Property(name="name", type=StringType)
henshin_NamedElement.attributes={henshin_NamedElement_name}

# henshin_DescribedElement class attributes and methods
henshin_DescribedElement_description: Property = Property(name="description", type=StringType)
henshin_DescribedElement.attributes={henshin_DescribedElement_description}

# henshin_TransformationSystem class attributes and methods
henshin_TransformationSystem_m_findUnitByName: Method = Method(name="findUnitByName", parameters={Parameter(name='unitName')}, type=StringType)
henshin_TransformationSystem_m_findRuleByName: Method = Method(name="findRuleByName", parameters={Parameter(name='ruleName')}, type=StringType)
henshin_TransformationSystem.methods={henshin_TransformationSystem_m_findRuleByName, henshin_TransformationSystem_m_findUnitByName}

# DescribedElement class attributes and methods

# NamedElement class attributes and methods

# henshin_Graph class attributes and methods
henshin_Graph_m_removeEdge: Method = Method(name="removeEdge", parameters={Parameter(name='edge')})
henshin_Graph_m_removeNode: Method = Method(name="removeNode", parameters={Parameter(name='node')})
henshin_Graph_m_getContainerRule: Method = Method(name="getContainerRule", parameters={}, type=StringType)
henshin_Graph_m_findNodesByType: Method = Method(name="findNodesByType", parameters={Parameter(name='nodeType')}, type=StringType)
henshin_Graph_m_findEdgesByType: Method = Method(name="findEdgesByType", parameters={Parameter(name='edgeType')}, type=StringType)
henshin_Graph.methods={henshin_Graph_m_removeEdge, henshin_Graph_m_getContainerRule, henshin_Graph_m_removeNode, henshin_Graph_m_findEdgesByType, henshin_Graph_m_findNodesByType}

# henshin_TransformationUnit class attributes and methods
henshin_TransformationUnit_activated: Property = Property(name="activated", type=BooleanType)
henshin_TransformationUnit_m_getSubUnits: Method = Method(name="getSubUnits", parameters={Parameter(name='deep')}, type=TransformationUnit)
henshin_TransformationUnit_m_getParameterByName: Method = Method(name="getParameterByName", parameters={Parameter(name='parametername')}, type=StringType)
henshin_TransformationUnit.attributes={henshin_TransformationUnit_activated}
henshin_TransformationUnit.methods={henshin_TransformationUnit_m_getSubUnits, henshin_TransformationUnit_m_getParameterByName}

# TransformationUnit class attributes and methods

# henshin_AttributeCondition class attributes and methods
henshin_AttributeCondition_conditionText: Property = Property(name="conditionText", type=StringType)
henshin_AttributeCondition.attributes={henshin_AttributeCondition_conditionText}

# henshin_Mapping class attributes and methods

# henshin_Rule class attributes and methods
henshin_Rule_m_getNodeByName: Method = Method(name="getNodeByName", parameters={Parameter(name='isLhs'), Parameter(name='nodename')}, type=StringType)
henshin_Rule_m_containsMapping: Method = Method(name="containsMapping", parameters={Parameter(name='sourceNode'), Parameter(name='targetNode')}, type=BooleanType)
henshin_Rule.methods={henshin_Rule_m_getNodeByName, henshin_Rule_m_containsMapping}

# henshin_EPackage class attributes and methods

# henshin_Node class attributes and methods
henshin_Node_m_findIncomingEdgeByType: Method = Method(name="findIncomingEdgeByType", parameters={Parameter(name='sourceNode'), Parameter(name='edgeType')}, type=StringType)
henshin_Node_m_findOutgoingEdgesByType: Method = Method(name="findOutgoingEdgesByType", parameters={Parameter(name='edgeType')}, type=StringType)
henshin_Node_m_findIncomingEdgesByType: Method = Method(name="findIncomingEdgesByType", parameters={Parameter(name='edgeType')}, type=StringType)
henshin_Node_m_findAttributeByType: Method = Method(name="findAttributeByType", parameters={Parameter(name='attributeType')}, type=StringType)
henshin_Node_m_findOutgoingEdgeByType: Method = Method(name="findOutgoingEdgeByType", parameters={Parameter(name='edgeType'), Parameter(name='targetNode')}, type=StringType)
henshin_Node.methods={henshin_Node_m_findAttributeByType, henshin_Node_m_findIncomingEdgeByType, henshin_Node_m_findOutgoingEdgeByType, henshin_Node_m_findOutgoingEdgesByType, henshin_Node_m_findIncomingEdgesByType}

# henshin_Edge class attributes and methods

# henshin_Formula class attributes and methods
henshin_Formula_m_stringRepresentation: Method = Method(name="stringRepresentation", parameters={Parameter(name='recursive')}, type=StringType)
henshin_Formula.methods={henshin_Formula_m_stringRepresentation}

# henshin_GraphElement class attributes and methods
henshin_GraphElement_m_getGraph: Method = Method(name="getGraph", parameters={}, type=StringType)
henshin_GraphElement.methods={henshin_GraphElement_m_getGraph}

# henshin_Parameter class attributes and methods

# henshin_EClass class attributes and methods

# henshin_Attribute class attributes and methods
henshin_Attribute_value: Property = Property(name="value", type=StringType)
henshin_Attribute.attributes={henshin_Attribute_value}

# henshin_EAttribute class attributes and methods

# GraphElement class attributes and methods

# henshin_ParameterMapping class attributes and methods

# henshin_IndependentUnit class attributes and methods

# henshin_SequentialUnit class attributes and methods
henshin_SequentialUnit_strict: Property = Property(name="strict", type=BooleanType)
henshin_SequentialUnit_rollback: Property = Property(name="rollback", type=BooleanType)
henshin_SequentialUnit.attributes={henshin_SequentialUnit_strict, henshin_SequentialUnit_rollback}

# henshin_ConditionalUnit class attributes and methods

# henshin_EReference class attributes and methods

# henshin_CountedUnit class attributes and methods
henshin_CountedUnit_count: Property = Property(name="count", type=IntegerType)
henshin_CountedUnit.attributes={henshin_CountedUnit_count}

# henshin_NestedCondition class attributes and methods
henshin_NestedCondition_negated: Property = Property(name="negated", type=BooleanType)
henshin_NestedCondition.attributes={henshin_NestedCondition_negated}

# Formula class attributes and methods

# henshin_PriorityUnit class attributes and methods

# henshin_AmalgamationUnit class attributes and methods

# henshin_And class attributes and methods

# BinaryFormula class attributes and methods

# henshin_Or class attributes and methods

# henshin_Xor class attributes and methods

# henshin_Not class attributes and methods

# UnaryFormula class attributes and methods

# henshin_UnaryFormula class attributes and methods

# henshin_BinaryFormula class attributes and methods

# Relationships
instances2: BinaryAssociation = BinaryAssociation(
    name="instances2",
    ends={
        Property(name="henshin_Graph", type=henshin_TransformationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_TransformationSystem3", type=henshin_Graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformationUnits4: BinaryAssociation = BinaryAssociation(
    name="transformationUnits4",
    ends={
        Property(name="henshin_TransformationUnit", type=henshin_TransformationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_TransformationSystem5", type=henshin_TransformationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs6: BinaryAssociation = BinaryAssociation(
    name="lhs6",
    ends={
        Property(name="henshin_Graph7", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule", type=henshin_Graph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs8: BinaryAssociation = BinaryAssociation(
    name="rhs8",
    ends={
        Property(name="henshin_Graph10", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule9", type=henshin_Graph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributeConditions11: BinaryAssociation = BinaryAssociation(
    name="attributeConditions11",
    ends={
        Property(name="AttributeCondition", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule", type=henshin_AttributeCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappings12: BinaryAssociation = BinaryAssociation(
    name="mappings12",
    ends={
        Property(name="henshin_Mapping", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule13", type=henshin_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformationSystem14: BinaryAssociation = BinaryAssociation(
    name="transformationSystem14",
    ends={
        Property(name="TransformationSystem", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rules", type=henshin_TransformationSystem, multiplicity=Multiplicity(0, 1))
    }
)
rule15: BinaryAssociation = BinaryAssociation(
    name="rule15",
    ends={
        Property(name="Rule16", type=henshin_AttributeCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="attributeConditions", type=henshin_Rule, multiplicity=Multiplicity(1, 1))
    }
)
rules0: BinaryAssociation = BinaryAssociation(
    name="rules0",
    ends={
        Property(name="Rule", type=henshin_TransformationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="transformationSystem", type=henshin_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="henshin_EPackage", type=henshin_TransformationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_TransformationSystem", type=henshin_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
nodes18: BinaryAssociation = BinaryAssociation(
    name="nodes18",
    ends={
        Property(name="Node", type=henshin_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=henshin_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges19: BinaryAssociation = BinaryAssociation(
    name="edges19",
    ends={
        Property(name="Edge", type=henshin_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph20", type=henshin_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formula21: BinaryAssociation = BinaryAssociation(
    name="formula21",
    ends={
        Property(name="henshin_Formula", type=henshin_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Graph22", type=henshin_Formula, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
origin23: BinaryAssociation = BinaryAssociation(
    name="origin23",
    ends={
        Property(name="henshin_Node", type=henshin_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Mapping24", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
image25: BinaryAssociation = BinaryAssociation(
    name="image25",
    ends={
        Property(name="henshin_Node27", type=henshin_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Mapping26", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
unit17: BinaryAssociation = BinaryAssociation(
    name="unit17",
    ends={
        Property(name="TransformationUnit", type=henshin_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1))
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="henshin_EClass", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Node29", type=henshin_EClass, multiplicity=Multiplicity(1, 1))
    }
)
attributes30: BinaryAssociation = BinaryAssociation(
    name="attributes30",
    ends={
        Property(name="Attribute", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=henshin_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph31: BinaryAssociation = BinaryAssociation(
    name="graph31",
    ends={
        Property(name="Graph", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=henshin_Graph, multiplicity=Multiplicity(1, 1))
    }
)
incoming32: BinaryAssociation = BinaryAssociation(
    name="incoming32",
    ends={
        Property(name="Edge33", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=henshin_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing34: BinaryAssociation = BinaryAssociation(
    name="outgoing34",
    ends={
        Property(name="Edge35", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=henshin_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
allEdges36: BinaryAssociation = BinaryAssociation(
    name="allEdges36",
    ends={
        Property(name="henshin_Edge", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Node37", type=henshin_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="henshin_EAttribute", type=henshin_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Attribute", type=henshin_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
node39: BinaryAssociation = BinaryAssociation(
    name="node39",
    ends={
        Property(name="Node40", type=henshin_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
parameters49: BinaryAssociation = BinaryAssociation(
    name="parameters49",
    ends={
        Property(name="Parameter", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="unit", type=henshin_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterMappings50: BinaryAssociation = BinaryAssociation(
    name="parameterMappings50",
    ends={
        Property(name="henshin_ParameterMapping", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_TransformationUnit51", type=henshin_ParameterMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subUnits52: BinaryAssociation = BinaryAssociation(
    name="subUnits52",
    ends={
        Property(name="henshin_TransformationUnit53", type=henshin_IndependentUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_IndependentUnit", type=henshin_TransformationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
subUnits54: BinaryAssociation = BinaryAssociation(
    name="subUnits54",
    ends={
        Property(name="henshin_TransformationUnit55", type=henshin_SequentialUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_SequentialUnit", type=henshin_TransformationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
if56: BinaryAssociation = BinaryAssociation(
    name="if56",
    ends={
        Property(name="henshin_TransformationUnit57", type=henshin_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ConditionalUnit", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1))
    }
)
source41: BinaryAssociation = BinaryAssociation(
    name="source41",
    ends={
        Property(name="Node42", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
target43: BinaryAssociation = BinaryAssociation(
    name="target43",
    ends={
        Property(name="Node44", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="henshin_EReference", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Edge46", type=henshin_EReference, multiplicity=Multiplicity(1, 1))
    }
)
graph47: BinaryAssociation = BinaryAssociation(
    name="graph47",
    ends={
        Property(name="Graph48", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=henshin_Graph, multiplicity=Multiplicity(1, 1))
    }
)
kernelRule66: BinaryAssociation = BinaryAssociation(
    name="kernelRule66",
    ends={
        Property(name="henshin_Rule67", type=henshin_AmalgamationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_AmalgamationUnit", type=henshin_Rule, multiplicity=Multiplicity(1, 1))
    }
)
multiRules68: BinaryAssociation = BinaryAssociation(
    name="multiRules68",
    ends={
        Property(name="henshin_Rule70", type=henshin_AmalgamationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_AmalgamationUnit69", type=henshin_Rule, multiplicity=Multiplicity(1, 9999))
    }
)
lhsMappings71: BinaryAssociation = BinaryAssociation(
    name="lhsMappings71",
    ends={
        Property(name="henshin_Mapping73", type=henshin_AmalgamationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_AmalgamationUnit72", type=henshin_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rhsMappings74: BinaryAssociation = BinaryAssociation(
    name="rhsMappings74",
    ends={
        Property(name="henshin_Mapping76", type=henshin_AmalgamationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_AmalgamationUnit75", type=henshin_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subUnit77: BinaryAssociation = BinaryAssociation(
    name="subUnit77",
    ends={
        Property(name="henshin_TransformationUnit78", type=henshin_CountedUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_CountedUnit", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1))
    }
)
then58: BinaryAssociation = BinaryAssociation(
    name="then58",
    ends={
        Property(name="henshin_TransformationUnit60", type=henshin_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ConditionalUnit59", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1))
    }
)
else61: BinaryAssociation = BinaryAssociation(
    name="else61",
    ends={
        Property(name="henshin_TransformationUnit63", type=henshin_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ConditionalUnit62", type=henshin_TransformationUnit, multiplicity=Multiplicity(0, 1))
    }
)
subUnits64: BinaryAssociation = BinaryAssociation(
    name="subUnits64",
    ends={
        Property(name="henshin_TransformationUnit65", type=henshin_PriorityUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_PriorityUnit", type=henshin_TransformationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
right88: BinaryAssociation = BinaryAssociation(
    name="right88",
    ends={
        Property(name="henshin_Formula90", type=henshin_BinaryFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_BinaryFormula89", type=henshin_Formula, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source91: BinaryAssociation = BinaryAssociation(
    name="source91",
    ends={
        Property(name="henshin_Parameter", type=henshin_ParameterMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ParameterMapping92", type=henshin_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
target93: BinaryAssociation = BinaryAssociation(
    name="target93",
    ends={
        Property(name="henshin_Parameter95", type=henshin_ParameterMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ParameterMapping94", type=henshin_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
conclusion79: BinaryAssociation = BinaryAssociation(
    name="conclusion79",
    ends={
        Property(name="henshin_Graph80", type=henshin_NestedCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_NestedCondition", type=henshin_Graph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappings81: BinaryAssociation = BinaryAssociation(
    name="mappings81",
    ends={
        Property(name="henshin_Mapping83", type=henshin_NestedCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_NestedCondition82", type=henshin_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child84: BinaryAssociation = BinaryAssociation(
    name="child84",
    ends={
        Property(name="henshin_Formula85", type=henshin_UnaryFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_UnaryFormula", type=henshin_Formula, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left86: BinaryAssociation = BinaryAssociation(
    name="left86",
    ends={
        Property(name="henshin_Formula87", type=henshin_BinaryFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_BinaryFormula", type=henshin_Formula, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_henshin_TransformationSystem_DescribedElement = Generalization(general=DescribedElement, specific=henshin_TransformationSystem)
gen_henshin_TransformationSystem_NamedElement = Generalization(general=NamedElement, specific=henshin_TransformationSystem)
gen_henshin_Rule_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_Rule)
gen_henshin_AttributeCondition_DescribedElement = Generalization(general=DescribedElement, specific=henshin_AttributeCondition)
gen_henshin_AttributeCondition_NamedElement = Generalization(general=NamedElement, specific=henshin_AttributeCondition)
gen_henshin_Parameter_DescribedElement = Generalization(general=DescribedElement, specific=henshin_Parameter)
gen_henshin_Parameter_NamedElement = Generalization(general=NamedElement, specific=henshin_Parameter)
gen_henshin_Graph_NamedElement = Generalization(general=NamedElement, specific=henshin_Graph)
gen_henshin_Edge_GraphElement = Generalization(general=GraphElement, specific=henshin_Edge)
gen_henshin_Node_NamedElement = Generalization(general=NamedElement, specific=henshin_Node)
gen_henshin_Node_GraphElement = Generalization(general=GraphElement, specific=henshin_Node)
gen_henshin_TransformationUnit_NamedElement = Generalization(general=NamedElement, specific=henshin_TransformationUnit)
gen_henshin_IndependentUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_IndependentUnit)
gen_henshin_SequentialUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_SequentialUnit)
gen_henshin_ConditionalUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_ConditionalUnit)
gen_henshin_TransformationUnit_DescribedElement = Generalization(general=DescribedElement, specific=henshin_TransformationUnit)
gen_henshin_CountedUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_CountedUnit)
gen_henshin_NestedCondition_Formula = Generalization(general=Formula, specific=henshin_NestedCondition)
gen_henshin_PriorityUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_PriorityUnit)
gen_henshin_AmalgamationUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_AmalgamationUnit)
gen_henshin_And_BinaryFormula = Generalization(general=BinaryFormula, specific=henshin_And)
gen_henshin_Or_BinaryFormula = Generalization(general=BinaryFormula, specific=henshin_Or)
gen_henshin_Xor_BinaryFormula = Generalization(general=BinaryFormula, specific=henshin_Xor)
gen_henshin_Not_UnaryFormula = Generalization(general=UnaryFormula, specific=henshin_Not)
gen_henshin_UnaryFormula_Formula = Generalization(general=Formula, specific=henshin_UnaryFormula)
gen_henshin_BinaryFormula_Formula = Generalization(general=Formula, specific=henshin_BinaryFormula)

# Domain Model
domain_model = DomainModel(
    name="henshin",
    types={henshin_NamedElement, henshin_DescribedElement, henshin_TransformationSystem, DescribedElement, NamedElement, henshin_Graph, henshin_TransformationUnit, TransformationUnit, henshin_AttributeCondition, henshin_Mapping, henshin_Rule, henshin_EPackage, henshin_Node, henshin_Edge, henshin_Formula, henshin_GraphElement, henshin_Parameter, henshin_EClass, henshin_Attribute, henshin_EAttribute, GraphElement, henshin_ParameterMapping, henshin_IndependentUnit, henshin_SequentialUnit, henshin_ConditionalUnit, henshin_EReference, henshin_CountedUnit, henshin_NestedCondition, Formula, henshin_PriorityUnit, henshin_AmalgamationUnit, henshin_And, BinaryFormula, henshin_Or, henshin_Xor, henshin_Not, UnaryFormula, henshin_UnaryFormula, henshin_BinaryFormula},
    associations={instances2, transformationUnits4, lhs6, rhs8, attributeConditions11, mappings12, transformationSystem14, rule15, rules0, imports1, nodes18, edges19, formula21, origin23, image25, unit17, type28, attributes30, graph31, incoming32, outgoing34, allEdges36, type38, node39, parameters49, parameterMappings50, subUnits52, subUnits54, if56, source41, target43, type45, graph47, kernelRule66, multiRules68, lhsMappings71, rhsMappings74, subUnit77, then58, else61, subUnits64, right88, source91, target93, conclusion79, mappings81, child84, left86},
    generalizations={gen_henshin_TransformationSystem_DescribedElement, gen_henshin_TransformationSystem_NamedElement, gen_henshin_Rule_TransformationUnit, gen_henshin_AttributeCondition_DescribedElement, gen_henshin_AttributeCondition_NamedElement, gen_henshin_Parameter_DescribedElement, gen_henshin_Parameter_NamedElement, gen_henshin_Graph_NamedElement, gen_henshin_Edge_GraphElement, gen_henshin_Node_NamedElement, gen_henshin_Node_GraphElement, gen_henshin_TransformationUnit_NamedElement, gen_henshin_IndependentUnit_TransformationUnit, gen_henshin_SequentialUnit_TransformationUnit, gen_henshin_ConditionalUnit_TransformationUnit, gen_henshin_TransformationUnit_DescribedElement, gen_henshin_CountedUnit_TransformationUnit, gen_henshin_NestedCondition_Formula, gen_henshin_PriorityUnit_TransformationUnit, gen_henshin_AmalgamationUnit_TransformationUnit, gen_henshin_And_BinaryFormula, gen_henshin_Or_BinaryFormula, gen_henshin_Xor_BinaryFormula, gen_henshin_Not_UnaryFormula, gen_henshin_UnaryFormula_Formula, gen_henshin_BinaryFormula_Formula},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)