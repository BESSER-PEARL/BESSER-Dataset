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
DirectedGraph_Node = Class(name="DirectedGraph::Node")
GraphElement = Class(name="GraphElement")
DirectedGraph_Edge = Class(name="DirectedGraph::Edge")
DirectedGraph_Graph = Class(name="DirectedGraph::Graph")
DirectedGraph_GraphElement = Class(name="DirectedGraph::GraphElement", is_abstract=True)

# DirectedGraph_Node class attributes and methods
DirectedGraph_Node_label: Property = Property(name="label", type=StringType)
DirectedGraph_Node.attributes={DirectedGraph_Node_label}

# GraphElement class attributes and methods

# DirectedGraph_Edge class attributes and methods
DirectedGraph_Edge_weight: Property = Property(name="weight", type=StringType)
DirectedGraph_Edge.attributes={DirectedGraph_Edge_weight}

# DirectedGraph_Graph class attributes and methods

# DirectedGraph_GraphElement class attributes and methods

# Relationships
outgoing2: BinaryAssociation = BinaryAssociation(
    name="outgoing2",
    ends={
        Property(name="Edge", type=DirectedGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=DirectedGraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Edge4", type=DirectedGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=DirectedGraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="Node", type=DirectedGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=DirectedGraph_Node, multiplicity=Multiplicity(0, 1))
    }
)
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="GraphElement", type=DirectedGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=DirectedGraph_GraphElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph1: BinaryAssociation = BinaryAssociation(
    name="graph1",
    ends={
        Property(name="Graph", type=DirectedGraph_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=DirectedGraph_Graph, multiplicity=Multiplicity(0, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="Node7", type=DirectedGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=DirectedGraph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_DirectedGraph_Node_GraphElement = Generalization(general=GraphElement, specific=DirectedGraph_Node)
gen_DirectedGraph_Edge_GraphElement = Generalization(general=GraphElement, specific=DirectedGraph_Edge)

# Domain Model
domain_model = DomainModel(
    name="DirectedGraph",
    types={DirectedGraph_Node, GraphElement, DirectedGraph_Edge, DirectedGraph_Graph, DirectedGraph_GraphElement},
    associations={outgoing2, incoming3, source5, contents0, graph1, target6},
    generalizations={gen_DirectedGraph_Node_GraphElement, gen_DirectedGraph_Edge_GraphElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)