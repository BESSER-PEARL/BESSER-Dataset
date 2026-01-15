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
Model: Enumeration = Enumeration(
    name="Model",
    literals={
            EnumerationLiteral(name="middle"),
			EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output")
    }
)

DependencyDirection: Enumeration = Enumeration(
    name="DependencyDirection",
    literals={
            EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output")
    }
)

# Classes
qVTcDataDependencyGraph_ClassNode = Class(name="qVTcDataDependencyGraph::ClassNode")
Node = Class(name="Node")
qVTcDataDependencyGraph_DataTypeNode = Class(name="qVTcDataDependencyGraph::DataTypeNode")
qVTcDataDependencyGraph_EObject = Class(name="qVTcDataDependencyGraph::EObject")
qVTcDataDependencyGraph_MappingNode = Class(name="qVTcDataDependencyGraph::MappingNode")
qVTcDataDependencyGraph_ReferenceEdge = Class(name="qVTcDataDependencyGraph::ReferenceEdge")
qVTcDataDependencyGraph_ContainmentEdge = Class(name="qVTcDataDependencyGraph::ContainmentEdge")
qVTcDataDependencyGraph_DependencyEdge = Class(name="qVTcDataDependencyGraph::DependencyEdge")
Edge = Class(name="Edge")
qVTcDataDependencyGraph_Edge = Class(name="qVTcDataDependencyGraph::Edge")
Element = Class(name="Element")
qVTcDataDependencyGraph_Node = Class(name="qVTcDataDependencyGraph::Node")
qVTcDataDependencyGraph_Element = Class(name="qVTcDataDependencyGraph::Element", is_abstract=True)
qVTcDataDependencyGraph_Graph = Class(name="qVTcDataDependencyGraph::Graph")

# qVTcDataDependencyGraph_ClassNode class attributes and methods
qVTcDataDependencyGraph_ClassNode_model: Property = Property(name="model", type=StringType)
qVTcDataDependencyGraph_ClassNode_superTypes: Property = Property(name="superTypes", type=StringType)
qVTcDataDependencyGraph_ClassNode.attributes={qVTcDataDependencyGraph_ClassNode_model, qVTcDataDependencyGraph_ClassNode_superTypes}

# Node class attributes and methods

# qVTcDataDependencyGraph_DataTypeNode class attributes and methods

# qVTcDataDependencyGraph_EObject class attributes and methods

# qVTcDataDependencyGraph_MappingNode class attributes and methods

# qVTcDataDependencyGraph_ReferenceEdge class attributes and methods

# qVTcDataDependencyGraph_ContainmentEdge class attributes and methods
qVTcDataDependencyGraph_ContainmentEdge_model: Property = Property(name="model", type=StringType)
qVTcDataDependencyGraph_ContainmentEdge.attributes={qVTcDataDependencyGraph_ContainmentEdge_model}

# qVTcDataDependencyGraph_DependencyEdge class attributes and methods
qVTcDataDependencyGraph_DependencyEdge_derived: Property = Property(name="derived", type=BooleanType)
qVTcDataDependencyGraph_DependencyEdge_multiple: Property = Property(name="multiple", type=BooleanType)
qVTcDataDependencyGraph_DependencyEdge_direction: Property = Property(name="direction", type=StringType)
qVTcDataDependencyGraph_DependencyEdge.attributes={qVTcDataDependencyGraph_DependencyEdge_direction, qVTcDataDependencyGraph_DependencyEdge_multiple, qVTcDataDependencyGraph_DependencyEdge_derived}

# Edge class attributes and methods

# qVTcDataDependencyGraph_Edge class attributes and methods

# Element class attributes and methods

# qVTcDataDependencyGraph_Node class attributes and methods
qVTcDataDependencyGraph_Node_label: Property = Property(name="label", type=StringType)
qVTcDataDependencyGraph_Node.attributes={qVTcDataDependencyGraph_Node_label}

# qVTcDataDependencyGraph_Element class attributes and methods

# qVTcDataDependencyGraph_Graph class attributes and methods
qVTcDataDependencyGraph_Graph_name: Property = Property(name="name", type=StringType)
qVTcDataDependencyGraph_Graph.attributes={qVTcDataDependencyGraph_Graph_name}

# Relationships
attribute0: BinaryAssociation = BinaryAssociation(
    name="attribute0",
    ends={
        Property(name="qVTcDataDependencyGraph_EObject", type=qVTcDataDependencyGraph_DataTypeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="qVTcDataDependencyGraph_DataTypeNode", type=qVTcDataDependencyGraph_EObject, multiplicity=Multiplicity(1, 1))
    }
)
incoming11: BinaryAssociation = BinaryAssociation(
    name="incoming11",
    ends={
        Property(name="Edge", type=qVTcDataDependencyGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=qVTcDataDependencyGraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing12: BinaryAssociation = BinaryAssociation(
    name="outgoing12",
    ends={
        Property(name="Edge13", type=qVTcDataDependencyGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=qVTcDataDependencyGraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
qvtAstNode14: BinaryAssociation = BinaryAssociation(
    name="qvtAstNode14",
    ends={
        Property(name="qVTcDataDependencyGraph_EObject15", type=qVTcDataDependencyGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="qVTcDataDependencyGraph_Node", type=qVTcDataDependencyGraph_EObject, multiplicity=Multiplicity(0, 1))
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="qVTcDataDependencyGraph_EObject3", type=qVTcDataDependencyGraph_DataTypeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="qVTcDataDependencyGraph_DataTypeNode2", type=qVTcDataDependencyGraph_EObject, multiplicity=Multiplicity(1, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="Node", type=qVTcDataDependencyGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=qVTcDataDependencyGraph_Node, multiplicity=Multiplicity(1, 1))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="Node6", type=qVTcDataDependencyGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=qVTcDataDependencyGraph_Node, multiplicity=Multiplicity(1, 1))
    }
)
referredProperty7: BinaryAssociation = BinaryAssociation(
    name="referredProperty7",
    ends={
        Property(name="qVTcDataDependencyGraph_EObject8", type=qVTcDataDependencyGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="qVTcDataDependencyGraph_Edge", type=qVTcDataDependencyGraph_EObject, multiplicity=Multiplicity(0, 1))
    }
)
graph9: BinaryAssociation = BinaryAssociation(
    name="graph9",
    ends={
        Property(name="Graph", type=qVTcDataDependencyGraph_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=qVTcDataDependencyGraph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
elements10: BinaryAssociation = BinaryAssociation(
    name="elements10",
    ends={
        Property(name="Element", type=qVTcDataDependencyGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=qVTcDataDependencyGraph_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_qVTcDataDependencyGraph_ClassNode_Node = Generalization(general=Node, specific=qVTcDataDependencyGraph_ClassNode)
gen_qVTcDataDependencyGraph_DataTypeNode_Node = Generalization(general=Node, specific=qVTcDataDependencyGraph_DataTypeNode)
gen_qVTcDataDependencyGraph_MappingNode_Node = Generalization(general=Node, specific=qVTcDataDependencyGraph_MappingNode)
gen_qVTcDataDependencyGraph_Node_Element = Generalization(general=Element, specific=qVTcDataDependencyGraph_Node)
gen_qVTcDataDependencyGraph_ReferenceEdge_Edge = Generalization(general=Edge, specific=qVTcDataDependencyGraph_ReferenceEdge)
gen_qVTcDataDependencyGraph_ContainmentEdge_Edge = Generalization(general=Edge, specific=qVTcDataDependencyGraph_ContainmentEdge)
gen_qVTcDataDependencyGraph_DependencyEdge_Edge = Generalization(general=Edge, specific=qVTcDataDependencyGraph_DependencyEdge)
gen_qVTcDataDependencyGraph_Edge_Element = Generalization(general=Element, specific=qVTcDataDependencyGraph_Edge)

# Domain Model
domain_model = DomainModel(
    name="qVTcDataDependencyGraph",
    types={qVTcDataDependencyGraph_ClassNode, Node, qVTcDataDependencyGraph_DataTypeNode, qVTcDataDependencyGraph_EObject, qVTcDataDependencyGraph_MappingNode, qVTcDataDependencyGraph_ReferenceEdge, qVTcDataDependencyGraph_ContainmentEdge, qVTcDataDependencyGraph_DependencyEdge, Edge, qVTcDataDependencyGraph_Edge, Element, qVTcDataDependencyGraph_Node, qVTcDataDependencyGraph_Element, qVTcDataDependencyGraph_Graph, Model, DependencyDirection},
    associations={attribute0, incoming11, outgoing12, qvtAstNode14, type1, target4, source5, referredProperty7, graph9, elements10},
    generalizations={gen_qVTcDataDependencyGraph_ClassNode_Node, gen_qVTcDataDependencyGraph_DataTypeNode_Node, gen_qVTcDataDependencyGraph_MappingNode_Node, gen_qVTcDataDependencyGraph_Node_Element, gen_qVTcDataDependencyGraph_ReferenceEdge_Edge, gen_qVTcDataDependencyGraph_ContainmentEdge_Edge, gen_qVTcDataDependencyGraph_DependencyEdge_Edge, gen_qVTcDataDependencyGraph_Edge_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)