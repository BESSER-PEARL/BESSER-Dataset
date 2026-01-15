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
graph_Node = Class(name="graph::Node")
Element = Class(name="Element")
graph_Edge = Class(name="graph::Edge")
graph_NodeType = Class(name="graph::NodeType")
graph_EdgeType = Class(name="graph::EdgeType")
graph_Element = Class(name="graph::Element", is_abstract=True)
graph_Graph = Class(name="graph::Graph")
graph_ElementType = Class(name="graph::ElementType", is_abstract=True)
ElementType = Class(name="ElementType")

# graph_Node class attributes and methods
graph_Node_label: Property = Property(name="label", type=StringType)
graph_Node.attributes={graph_Node_label}

# Element class attributes and methods

# graph_Edge class attributes and methods

# graph_NodeType class attributes and methods

# graph_EdgeType class attributes and methods

# graph_Element class attributes and methods

# graph_Graph class attributes and methods
graph_Graph_name: Property = Property(name="name", type=StringType)
graph_Graph.attributes={graph_Graph_name}

# graph_ElementType class attributes and methods
graph_ElementType_name: Property = Property(name="name", type=StringType)
graph_ElementType.attributes={graph_ElementType_name}

# ElementType class attributes and methods

# Relationships
incoming0: BinaryAssociation = BinaryAssociation(
    name="incoming0",
    ends={
        Property(name="Edge", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing1: BinaryAssociation = BinaryAssociation(
    name="outgoing1",
    ends={
        Property(name="Edge2", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="graph_NodeType", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Node", type=graph_NodeType, multiplicity=Multiplicity(0, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="Node", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="Node6", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="graph_EdgeType", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge", type=graph_EdgeType, multiplicity=Multiplicity(0, 1))
    }
)
graph8: BinaryAssociation = BinaryAssociation(
    name="graph8",
    ends={
        Property(name="Graph", type=graph_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=graph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
graph9: BinaryAssociation = BinaryAssociation(
    name="graph9",
    ends={
        Property(name="Graph10", type=graph_ElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=graph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
element11: BinaryAssociation = BinaryAssociation(
    name="element11",
    ends={
        Property(name="Element", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=graph_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementType12: BinaryAssociation = BinaryAssociation(
    name="elementType12",
    ends={
        Property(name="ElementType", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph13", type=graph_ElementType, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_graph_Node_Element = Generalization(general=Element, specific=graph_Node)
gen_graph_Edge_Element = Generalization(general=Element, specific=graph_Edge)
gen_graph_EdgeType_ElementType = Generalization(general=ElementType, specific=graph_EdgeType)
gen_graph_NodeType_ElementType = Generalization(general=ElementType, specific=graph_NodeType)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Node, Element, graph_Edge, graph_NodeType, graph_EdgeType, graph_Element, graph_Graph, graph_ElementType, ElementType},
    associations={incoming0, outgoing1, type3, target4, source5, type7, graph8, graph9, element11, elementType12},
    generalizations={gen_graph_Node_Element, gen_graph_Edge_Element, gen_graph_EdgeType_ElementType, gen_graph_NodeType_ElementType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)