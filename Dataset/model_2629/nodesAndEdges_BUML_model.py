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
EdgeViewType: Enumeration = Enumeration(
    name="EdgeViewType",
    literals={
            EnumerationLiteral(name="solidline"),
			EnumerationLiteral(name="dashline")
    }
)

Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="red"),
			EnumerationLiteral(name="blue")
    }
)

Shape: Enumeration = Enumeration(
    name="Shape",
    literals={
            EnumerationLiteral(name="round"),
			EnumerationLiteral(name="square")
    }
)

# Classes
nodesAndEdges_ColoredNode = Class(name="nodesAndEdges::ColoredNode")
Node = Class(name="Node")
nodesAndEdges_Node = Class(name="nodesAndEdges::Node")
nodesAndEdges_Node_toString = Class(name="nodesAndEdges::Node::toString")
nodesAndEdges_ColoredNode_toString = Class(name="nodesAndEdges::ColoredNode::toString")
nodesAndEdges_Edge = Class(name="nodesAndEdges::Edge")
nodesAndEdges_Edge_toString = Class(name="nodesAndEdges::Edge::toString")
nodesAndEdges_ShapedNode = Class(name="nodesAndEdges::ShapedNode")
nodesAndEdges_ShapedNode_toString = Class(name="nodesAndEdges::ShapedNode::toString")

# nodesAndEdges_ColoredNode class attributes and methods
nodesAndEdges_ColoredNode_color: Property = Property(name="color", type=StringType)
nodesAndEdges_ColoredNode_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
nodesAndEdges_ColoredNode.attributes={nodesAndEdges_ColoredNode_color}
nodesAndEdges_ColoredNode.methods={nodesAndEdges_ColoredNode_m_toString}

# Node class attributes and methods

# nodesAndEdges_Node class attributes and methods
nodesAndEdges_Node_name: Property = Property(name="name", type=StringType)
nodesAndEdges_Node.attributes={nodesAndEdges_Node_name}

# nodesAndEdges_Node_toString class attributes and methods

# nodesAndEdges_ColoredNode_toString class attributes and methods

# nodesAndEdges_Edge class attributes and methods
nodesAndEdges_Edge_name: Property = Property(name="name", type=StringType)
nodesAndEdges_Edge_type: Property = Property(name="type", type=StringType)
nodesAndEdges_Edge_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
nodesAndEdges_Edge.attributes={nodesAndEdges_Edge_name, nodesAndEdges_Edge_type}
nodesAndEdges_Edge.methods={nodesAndEdges_Edge_m_toString}

# nodesAndEdges_Edge_toString class attributes and methods

# nodesAndEdges_ShapedNode class attributes and methods
nodesAndEdges_ShapedNode_size: Property = Property(name="size", type=FloatType)
nodesAndEdges_ShapedNode_shape: Property = Property(name="shape", type=StringType)
nodesAndEdges_ShapedNode_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
nodesAndEdges_ShapedNode.attributes={nodesAndEdges_ShapedNode_shape, nodesAndEdges_ShapedNode_size}
nodesAndEdges_ShapedNode.methods={nodesAndEdges_ShapedNode_m_toString}

# nodesAndEdges_ShapedNode_toString class attributes and methods

# Generalizations
gen_nodesAndEdges_ColoredNode_Node = Generalization(general=Node, specific=nodesAndEdges_ColoredNode)
gen_nodesAndEdges_ShapedNode_Node = Generalization(general=Node, specific=nodesAndEdges_ShapedNode)

# Domain Model
domain_model = DomainModel(
    name="nodesAndEdges",
    types={nodesAndEdges_ColoredNode, Node, nodesAndEdges_Node, nodesAndEdges_Node_toString, nodesAndEdges_ColoredNode_toString, nodesAndEdges_Edge, nodesAndEdges_Edge_toString, nodesAndEdges_ShapedNode, nodesAndEdges_ShapedNode_toString, EdgeViewType, Color, Shape},
    associations={},
    generalizations={gen_nodesAndEdges_ColoredNode_Node, gen_nodesAndEdges_ShapedNode_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)