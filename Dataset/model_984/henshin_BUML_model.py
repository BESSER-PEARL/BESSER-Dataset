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
henshin_Rule = Class(name="henshin_Rule")
henshin_EPackage = Class(name="henshin_EPackage")
henshin_TransformationUnit = Class(name="henshin_TransformationUnit", is_abstract=True)
henshin_Graph = Class(name="henshin_Graph")
TransformationUnit = Class(name="TransformationUnit")
henshin_NamedElement = Class(name="henshin_NamedElement", is_abstract=True)
henshin_TransformationSystem = Class(name="henshin_TransformationSystem")
NamedElement = Class(name="NamedElement")
henshin_Mapping = Class(name="henshin_Mapping")
henshin_Parameter = Class(name="henshin_Parameter")
henshin_EClassifier = Class(name="henshin_EClassifier")
henshin_AttributeCondition = Class(name="henshin_AttributeCondition")
GraphElement = Class(name="GraphElement")
henshin_EClass = Class(name="henshin_EClass")
henshin_Attribute = Class(name="henshin_Attribute")
henshin_Node = Class(name="henshin_Node")
henshin_Edge = Class(name="henshin_Edge")
henshin_Formula = Class(name="henshin_Formula", is_abstract=True)
henshin_GraphElement = Class(name="henshin_GraphElement", is_abstract=True)
henshin_EReference = Class(name="henshin_EReference")
henshin_ParameterMapping = Class(name="henshin_ParameterMapping")
henshin_IndependentUnit = Class(name="henshin_IndependentUnit")
henshin_SequentialUnit = Class(name="henshin_SequentialUnit")
henshin_ConditionalUnit = Class(name="henshin_ConditionalUnit")
henshin_EAttribute = Class(name="henshin_EAttribute")
henshin_LoopUnit = Class(name="henshin_LoopUnit")
henshin_NestedCondition = Class(name="henshin_NestedCondition")
Formula = Class(name="Formula")
henshin_UnaryFormula = Class(name="henshin_UnaryFormula", is_abstract=True)
henshin_BinaryFormula = Class(name="henshin_BinaryFormula", is_abstract=True)
henshin_And = Class(name="henshin_And")
BinaryFormula = Class(name="BinaryFormula")
henshin_Or = Class(name="henshin_Or")
henshin_Xor = Class(name="henshin_Xor")
henshin_Not = Class(name="henshin_Not")
UnaryFormula = Class(name="UnaryFormula")
henshin_PriorityUnit = Class(name="henshin_PriorityUnit")
henshin_IteratedUnit = Class(name="henshin_IteratedUnit")

# henshin_Rule class attributes and methods
henshin_Rule_checkDangling: Property = Property(name="checkDangling", type=BooleanType)
henshin_Rule_injectiveMatching: Property = Property(name="injectiveMatching", type=BooleanType)
henshin_Rule_m_getNode: Method = Method(name="getNode", parameters={Parameter(name='henshin_isLhs', type=StringType), Parameter(name='henshin_nodename', type=StringType)}, type=StringType)
henshin_Rule_m_containsMapping: Method = Method(name="containsMapping", parameters={Parameter(name='henshin_sourceNode', type=StringType), Parameter(name='henshin_targetNode', type=StringType)}, type=BooleanType)
henshin_Rule_m_containsMultiMapping: Method = Method(name="containsMultiMapping", parameters={Parameter(name='henshin_sourceNode', type=StringType), Parameter(name='henshin_targetNode', type=StringType)}, type=BooleanType)
henshin_Rule_m_getTransformationSystem: Method = Method(name="getTransformationSystem", parameters={}, type=StringType)
henshin_Rule_m_getKernelRule: Method = Method(name="getKernelRule", parameters={}, type=StringType)
henshin_Rule_m_getRootKernelRule: Method = Method(name="getRootKernelRule", parameters={}, type=StringType)
henshin_Rule_m_getMultiRule: Method = Method(name="getMultiRule", parameters={Parameter(name='henshin_name', type=StringType)}, type=StringType)
henshin_Rule_m_removeEdge: Method = Method(name="removeEdge", parameters={Parameter(name='henshin_removeMapped', type=StringType), Parameter(name='henshin_edge', type=StringType)})
henshin_Rule_m_removeNode: Method = Method(name="removeNode", parameters={Parameter(name='henshin_node', type=StringType), Parameter(name='henshin_removeMapped', type=StringType)})
henshin_Rule_m_getAllMultiRules: Method = Method(name="getAllMultiRules", parameters={}, type=StringType)
henshin_Rule.attributes={henshin_Rule_injectiveMatching, henshin_Rule_checkDangling}
henshin_Rule.methods={henshin_Rule_m_getAllMultiRules, henshin_Rule_m_getNode, henshin_Rule_m_getKernelRule, henshin_Rule_m_getTransformationSystem, henshin_Rule_m_getMultiRule, henshin_Rule_m_removeNode, henshin_Rule_m_getRootKernelRule, henshin_Rule_m_containsMapping, henshin_Rule_m_containsMultiMapping, henshin_Rule_m_removeEdge}

# henshin_EPackage class attributes and methods

# henshin_TransformationUnit class attributes and methods
henshin_TransformationUnit_activated: Property = Property(name="activated", type=BooleanType)
henshin_TransformationUnit_m_getSubUnits: Method = Method(name="getSubUnits", parameters={Parameter(name='henshin_deep', type=StringType)}, type=TransformationUnit)
henshin_TransformationUnit_m_getParameter: Method = Method(name="getParameter", parameters={Parameter(name='henshin_parameter', type=StringType)}, type=StringType)
henshin_TransformationUnit.attributes={henshin_TransformationUnit_activated}
henshin_TransformationUnit.methods={henshin_TransformationUnit_m_getSubUnits, henshin_TransformationUnit_m_getParameter}

# henshin_Graph class attributes and methods
henshin_Graph_m_removeEdge: Method = Method(name="removeEdge", parameters={Parameter(name='henshin_edge', type=StringType)})
henshin_Graph_m_removeNode: Method = Method(name="removeNode", parameters={Parameter(name='henshin_node', type=StringType)})
henshin_Graph_m_getContainerRule: Method = Method(name="getContainerRule", parameters={}, type=StringType)
henshin_Graph_m_getNodes: Method = Method(name="getNodes", parameters={Parameter(name='henshin_nodeType', type=StringType)}, type=StringType)
henshin_Graph_m_getEdges: Method = Method(name="getEdges", parameters={Parameter(name='henshin_edgeType', type=StringType)}, type=StringType)
henshin_Graph_m_isLhs: Method = Method(name="isLhs", parameters={}, type=BooleanType)
henshin_Graph_m_isRhs: Method = Method(name="isRhs", parameters={}, type=BooleanType)
henshin_Graph_m_isNestedCondition: Method = Method(name="isNestedCondition", parameters={}, type=BooleanType)
henshin_Graph.methods={henshin_Graph_m_removeEdge, henshin_Graph_m_getEdges, henshin_Graph_m_getNodes, henshin_Graph_m_isNestedCondition, henshin_Graph_m_removeNode, henshin_Graph_m_isRhs, henshin_Graph_m_isLhs, henshin_Graph_m_getContainerRule}

# TransformationUnit class attributes and methods

# henshin_NamedElement class attributes and methods
henshin_NamedElement_name: Property = Property(name="name", type=StringType)
henshin_NamedElement_description: Property = Property(name="description", type=StringType)
henshin_NamedElement.attributes={henshin_NamedElement_description, henshin_NamedElement_name}

# henshin_TransformationSystem class attributes and methods
henshin_TransformationSystem_m_getTransformationUnit: Method = Method(name="getTransformationUnit", parameters={Parameter(name='henshin_unitName', type=StringType)}, type=StringType)
henshin_TransformationSystem_m_getRule: Method = Method(name="getRule", parameters={Parameter(name='henshin_ruleName', type=StringType)}, type=StringType)
henshin_TransformationSystem.methods={henshin_TransformationSystem_m_getRule, henshin_TransformationSystem_m_getTransformationUnit}

# NamedElement class attributes and methods

# henshin_Mapping class attributes and methods

# henshin_Parameter class attributes and methods

# henshin_EClassifier class attributes and methods

# henshin_AttributeCondition class attributes and methods
henshin_AttributeCondition_conditionText: Property = Property(name="conditionText", type=StringType)
henshin_AttributeCondition.attributes={henshin_AttributeCondition_conditionText}

# GraphElement class attributes and methods

# henshin_EClass class attributes and methods

# henshin_Attribute class attributes and methods
henshin_Attribute_value: Property = Property(name="value", type=StringType)
henshin_Attribute.attributes={henshin_Attribute_value}

# henshin_Node class attributes and methods
henshin_Node_m_getOutgoing: Method = Method(name="getOutgoing", parameters={Parameter(name='henshin_type', type=StringType)}, type=StringType)
henshin_Node_m_getIncoming: Method = Method(name="getIncoming", parameters={Parameter(name='henshin_type', type=StringType)}, type=StringType)
henshin_Node_m_getOutgoing: Method = Method(name="getOutgoing", parameters={Parameter(name='henshin_target', type=StringType), Parameter(name='henshin_type', type=StringType)}, type=StringType)
henshin_Node_m_getIncoming: Method = Method(name="getIncoming", parameters={Parameter(name='henshin_type', type=StringType), Parameter(name='henshin_source', type=StringType)}, type=StringType)
henshin_Node_m_getAttribute: Method = Method(name="getAttribute", parameters={Parameter(name='henshin_type', type=StringType)}, type=StringType)
henshin_Node.methods={henshin_Node_m_getIncoming, henshin_Node_m_getAttribute, henshin_Node_m_getOutgoing, henshin_Node_m_getOutgoing, henshin_Node_m_getIncoming}

# henshin_Edge class attributes and methods

# henshin_Formula class attributes and methods
henshin_Formula_m_stringRepresentation: Method = Method(name="stringRepresentation", parameters={Parameter(name='henshin_recursive', type=StringType)}, type=StringType)
henshin_Formula.methods={henshin_Formula_m_stringRepresentation}

# henshin_GraphElement class attributes and methods
henshin_GraphElement_m_getGraph: Method = Method(name="getGraph", parameters={}, type=StringType)
henshin_GraphElement.methods={henshin_GraphElement_m_getGraph}

# henshin_EReference class attributes and methods

# henshin_ParameterMapping class attributes and methods

# henshin_IndependentUnit class attributes and methods

# henshin_SequentialUnit class attributes and methods
henshin_SequentialUnit_strict: Property = Property(name="strict", type=BooleanType)
henshin_SequentialUnit_rollback: Property = Property(name="rollback", type=BooleanType)
henshin_SequentialUnit.attributes={henshin_SequentialUnit_strict, henshin_SequentialUnit_rollback}

# henshin_ConditionalUnit class attributes and methods

# henshin_EAttribute class attributes and methods

# henshin_LoopUnit class attributes and methods

# henshin_NestedCondition class attributes and methods
henshin_NestedCondition_m_isPAC: Method = Method(name="isPAC", parameters={}, type=BooleanType)
henshin_NestedCondition_m_isNAC: Method = Method(name="isNAC", parameters={}, type=BooleanType)
henshin_NestedCondition.methods={henshin_NestedCondition_m_isPAC, henshin_NestedCondition_m_isNAC}

# Formula class attributes and methods

# henshin_UnaryFormula class attributes and methods

# henshin_BinaryFormula class attributes and methods

# henshin_And class attributes and methods

# BinaryFormula class attributes and methods

# henshin_Or class attributes and methods

# henshin_Xor class attributes and methods

# henshin_Not class attributes and methods

# UnaryFormula class attributes and methods

# henshin_PriorityUnit class attributes and methods

# henshin_IteratedUnit class attributes and methods
henshin_IteratedUnit_iterations: Property = Property(name="iterations", type=StringType)
henshin_IteratedUnit.attributes={henshin_IteratedUnit_iterations}

# Relationships
rules0: BinaryAssociation = BinaryAssociation(
    name="rules0",
    ends={
        Property(name="henshin_Rule", type=henshin_TransformationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_TransformationSystem", type=henshin_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="henshin_EPackage", type=henshin_TransformationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_TransformationSystem2", type=henshin_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
transformationUnits3: BinaryAssociation = BinaryAssociation(
    name="transformationUnits3",
    ends={
        Property(name="henshin_TransformationUnit", type=henshin_TransformationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_TransformationSystem4", type=henshin_TransformationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instances5: BinaryAssociation = BinaryAssociation(
    name="instances5",
    ends={
        Property(name="henshin_Graph", type=henshin_TransformationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_TransformationSystem6", type=henshin_Graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeConditions13: BinaryAssociation = BinaryAssociation(
    name="attributeConditions13",
    ends={
        Property(name="rule", type=henshin_AttributeCondition, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="AttributeCondition", type=henshin_Rule, multiplicity=Multiplicity(1, 1))
    }
)
mappings14: BinaryAssociation = BinaryAssociation(
    name="mappings14",
    ends={
        Property(name="henshin_Mapping", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule15", type=henshin_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiRules17: BinaryAssociation = BinaryAssociation(
    name="multiRules17",
    ends={
        Property(name="henshin_Rule18", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule16", type=henshin_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiMappings19: BinaryAssociation = BinaryAssociation(
    name="multiMappings19",
    ends={
        Property(name="henshin_Mapping21", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule20", type=henshin_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule22: BinaryAssociation = BinaryAssociation(
    name="rule22",
    ends={
        Property(name="Rule", type=henshin_AttributeCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="attributeConditions", type=henshin_Rule, multiplicity=Multiplicity(1, 1))
    }
)
unit23: BinaryAssociation = BinaryAssociation(
    name="unit23",
    ends={
        Property(name="TransformationUnit", type=henshin_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=henshin_TransformationUnit, multiplicity=Multiplicity(0, 1))
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="henshin_EClassifier", type=henshin_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Parameter", type=henshin_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
lhs7: BinaryAssociation = BinaryAssociation(
    name="lhs7",
    ends={
        Property(name="henshin_Graph9", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule8", type=henshin_Graph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs10: BinaryAssociation = BinaryAssociation(
    name="rhs10",
    ends={
        Property(name="henshin_Graph12", type=henshin_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Rule11", type=henshin_Graph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
origin30: BinaryAssociation = BinaryAssociation(
    name="origin30",
    ends={
        Property(name="henshin_Node", type=henshin_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Mapping31", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
image32: BinaryAssociation = BinaryAssociation(
    name="image32",
    ends={
        Property(name="henshin_Node34", type=henshin_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Mapping33", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="henshin_EClass", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Node36", type=henshin_EClass, multiplicity=Multiplicity(1, 1))
    }
)
attributes37: BinaryAssociation = BinaryAssociation(
    name="attributes37",
    ends={
        Property(name="Attribute", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=henshin_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph38: BinaryAssociation = BinaryAssociation(
    name="graph38",
    ends={
        Property(name="Graph", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=henshin_Graph, multiplicity=Multiplicity(1, 1))
    }
)
incoming39: BinaryAssociation = BinaryAssociation(
    name="incoming39",
    ends={
        Property(name="Edge40", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=henshin_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
nodes25: BinaryAssociation = BinaryAssociation(
    name="nodes25",
    ends={
        Property(name="Node", type=henshin_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=henshin_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges26: BinaryAssociation = BinaryAssociation(
    name="edges26",
    ends={
        Property(name="Edge", type=henshin_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph27", type=henshin_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formula28: BinaryAssociation = BinaryAssociation(
    name="formula28",
    ends={
        Property(name="henshin_Formula", type=henshin_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Graph29", type=henshin_Formula, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target50: BinaryAssociation = BinaryAssociation(
    name="target50",
    ends={
        Property(name="Node51", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="henshin_EReference", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Edge53", type=henshin_EReference, multiplicity=Multiplicity(1, 1))
    }
)
graph54: BinaryAssociation = BinaryAssociation(
    name="graph54",
    ends={
        Property(name="Graph55", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=henshin_Graph, multiplicity=Multiplicity(1, 1))
    }
)
parameters56: BinaryAssociation = BinaryAssociation(
    name="parameters56",
    ends={
        Property(name="Parameter", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="unit", type=henshin_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterMappings57: BinaryAssociation = BinaryAssociation(
    name="parameterMappings57",
    ends={
        Property(name="henshin_ParameterMapping", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_TransformationUnit58", type=henshin_ParameterMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subUnits59: BinaryAssociation = BinaryAssociation(
    name="subUnits59",
    ends={
        Property(name="henshin_TransformationUnit60", type=henshin_IndependentUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_IndependentUnit", type=henshin_TransformationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
subUnits61: BinaryAssociation = BinaryAssociation(
    name="subUnits61",
    ends={
        Property(name="henshin_TransformationUnit62", type=henshin_SequentialUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_SequentialUnit", type=henshin_TransformationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing41: BinaryAssociation = BinaryAssociation(
    name="outgoing41",
    ends={
        Property(name="Edge42", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=henshin_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
if_63: BinaryAssociation = BinaryAssociation(
    name="if_63",
    ends={
        Property(name="henshin_TransformationUnit64", type=henshin_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ConditionalUnit", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1))
    }
)
allEdges43: BinaryAssociation = BinaryAssociation(
    name="allEdges43",
    ends={
        Property(name="henshin_Edge", type=henshin_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Node44", type=henshin_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="henshin_EAttribute", type=henshin_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_Attribute", type=henshin_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
node46: BinaryAssociation = BinaryAssociation(
    name="node46",
    ends={
        Property(name="Node47", type=henshin_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
source48: BinaryAssociation = BinaryAssociation(
    name="source48",
    ends={
        Property(name="Node49", type=henshin_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=henshin_Node, multiplicity=Multiplicity(1, 1))
    }
)
subUnit75: BinaryAssociation = BinaryAssociation(
    name="subUnit75",
    ends={
        Property(name="henshin_TransformationUnit76", type=henshin_LoopUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_LoopUnit", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1))
    }
)
conclusion77: BinaryAssociation = BinaryAssociation(
    name="conclusion77",
    ends={
        Property(name="henshin_Graph78", type=henshin_NestedCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_NestedCondition", type=henshin_Graph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappings79: BinaryAssociation = BinaryAssociation(
    name="mappings79",
    ends={
        Property(name="henshin_Mapping81", type=henshin_NestedCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_NestedCondition80", type=henshin_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child82: BinaryAssociation = BinaryAssociation(
    name="child82",
    ends={
        Property(name="henshin_Formula83", type=henshin_UnaryFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_UnaryFormula", type=henshin_Formula, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left84: BinaryAssociation = BinaryAssociation(
    name="left84",
    ends={
        Property(name="henshin_Formula85", type=henshin_BinaryFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_BinaryFormula", type=henshin_Formula, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right86: BinaryAssociation = BinaryAssociation(
    name="right86",
    ends={
        Property(name="henshin_Formula88", type=henshin_BinaryFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_BinaryFormula87", type=henshin_Formula, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then65: BinaryAssociation = BinaryAssociation(
    name="then65",
    ends={
        Property(name="henshin_TransformationUnit67", type=henshin_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ConditionalUnit66", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1))
    }
)
else_68: BinaryAssociation = BinaryAssociation(
    name="else_68",
    ends={
        Property(name="henshin_TransformationUnit70", type=henshin_ConditionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ConditionalUnit69", type=henshin_TransformationUnit, multiplicity=Multiplicity(0, 1))
    }
)
source89: BinaryAssociation = BinaryAssociation(
    name="source89",
    ends={
        Property(name="henshin_Parameter91", type=henshin_ParameterMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ParameterMapping90", type=henshin_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
target92: BinaryAssociation = BinaryAssociation(
    name="target92",
    ends={
        Property(name="henshin_Parameter94", type=henshin_ParameterMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_ParameterMapping93", type=henshin_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
subUnits71: BinaryAssociation = BinaryAssociation(
    name="subUnits71",
    ends={
        Property(name="henshin_TransformationUnit72", type=henshin_PriorityUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_PriorityUnit", type=henshin_TransformationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
subUnit73: BinaryAssociation = BinaryAssociation(
    name="subUnit73",
    ends={
        Property(name="henshin_TransformationUnit74", type=henshin_IteratedUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="henshin_IteratedUnit", type=henshin_TransformationUnit, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_henshin_Rule_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_Rule)
gen_henshin_TransformationSystem_NamedElement = Generalization(general=NamedElement, specific=henshin_TransformationSystem)
gen_henshin_AttributeCondition_NamedElement = Generalization(general=NamedElement, specific=henshin_AttributeCondition)
gen_henshin_Parameter_NamedElement = Generalization(general=NamedElement, specific=henshin_Parameter)
gen_henshin_Graph_NamedElement = Generalization(general=NamedElement, specific=henshin_Graph)
gen_henshin_Node_NamedElement = Generalization(general=NamedElement, specific=henshin_Node)
gen_henshin_Node_GraphElement = Generalization(general=GraphElement, specific=henshin_Node)
gen_henshin_TransformationUnit_NamedElement = Generalization(general=NamedElement, specific=henshin_TransformationUnit)
gen_henshin_IndependentUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_IndependentUnit)
gen_henshin_SequentialUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_SequentialUnit)
gen_henshin_ConditionalUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_ConditionalUnit)
gen_henshin_Edge_GraphElement = Generalization(general=GraphElement, specific=henshin_Edge)
gen_henshin_LoopUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_LoopUnit)
gen_henshin_NestedCondition_Formula = Generalization(general=Formula, specific=henshin_NestedCondition)
gen_henshin_UnaryFormula_Formula = Generalization(general=Formula, specific=henshin_UnaryFormula)
gen_henshin_BinaryFormula_Formula = Generalization(general=Formula, specific=henshin_BinaryFormula)
gen_henshin_And_BinaryFormula = Generalization(general=BinaryFormula, specific=henshin_And)
gen_henshin_Or_BinaryFormula = Generalization(general=BinaryFormula, specific=henshin_Or)
gen_henshin_Xor_BinaryFormula = Generalization(general=BinaryFormula, specific=henshin_Xor)
gen_henshin_Not_UnaryFormula = Generalization(general=UnaryFormula, specific=henshin_Not)
gen_henshin_PriorityUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_PriorityUnit)
gen_henshin_IteratedUnit_TransformationUnit = Generalization(general=TransformationUnit, specific=henshin_IteratedUnit)

# Domain Model
domain_model = DomainModel(
    name="henshin",
    types={henshin_Rule, henshin_EPackage, henshin_TransformationUnit, henshin_Graph, TransformationUnit, henshin_NamedElement, henshin_TransformationSystem, NamedElement, henshin_Mapping, henshin_Parameter, henshin_EClassifier, henshin_AttributeCondition, GraphElement, henshin_EClass, henshin_Attribute, henshin_Node, henshin_Edge, henshin_Formula, henshin_GraphElement, henshin_EReference, henshin_ParameterMapping, henshin_IndependentUnit, henshin_SequentialUnit, henshin_ConditionalUnit, henshin_EAttribute, henshin_LoopUnit, henshin_NestedCondition, Formula, henshin_UnaryFormula, henshin_BinaryFormula, henshin_And, BinaryFormula, henshin_Or, henshin_Xor, henshin_Not, UnaryFormula, henshin_PriorityUnit, henshin_IteratedUnit},
    associations={rules0, imports1, transformationUnits3, instances5, attributeConditions13, mappings14, multiRules17, multiMappings19, rule22, unit23, type24, lhs7, rhs10, origin30, image32, type35, attributes37, graph38, incoming39, nodes25, edges26, formula28, target50, type52, graph54, parameters56, parameterMappings57, subUnits59, subUnits61, outgoing41, if_63, allEdges43, type45, node46, source48, subUnit75, conclusion77, mappings79, child82, left84, right86, then65, else_68, source89, target92, subUnits71, subUnit73},
    generalizations={gen_henshin_Rule_TransformationUnit, gen_henshin_TransformationSystem_NamedElement, gen_henshin_AttributeCondition_NamedElement, gen_henshin_Parameter_NamedElement, gen_henshin_Graph_NamedElement, gen_henshin_Node_NamedElement, gen_henshin_Node_GraphElement, gen_henshin_TransformationUnit_NamedElement, gen_henshin_IndependentUnit_TransformationUnit, gen_henshin_SequentialUnit_TransformationUnit, gen_henshin_ConditionalUnit_TransformationUnit, gen_henshin_Edge_GraphElement, gen_henshin_LoopUnit_TransformationUnit, gen_henshin_NestedCondition_Formula, gen_henshin_UnaryFormula_Formula, gen_henshin_BinaryFormula_Formula, gen_henshin_And_BinaryFormula, gen_henshin_Or_BinaryFormula, gen_henshin_Xor_BinaryFormula, gen_henshin_Not_UnaryFormula, gen_henshin_PriorityUnit_TransformationUnit, gen_henshin_IteratedUnit_TransformationUnit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)