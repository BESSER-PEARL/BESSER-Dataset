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
graph_Edge = Class(name="graph::Edge")
GraphElement = Class(name="GraphElement")
graph_Graph = Class(name="graph::Graph")
graph_GraphElement = Class(name="graph::GraphElement", is_abstract=True)

# graph_Node class attributes and methods

# graph_Edge class attributes and methods

# GraphElement class attributes and methods

# graph_Graph class attributes and methods
graph_Graph_name: Property = Property(name="name", type=StringType)
graph_Graph.attributes={graph_Graph_name}

# graph_GraphElement class attributes and methods
graph_GraphElement_name: Property = Property(name="name", type=StringType)
graph_GraphElement.attributes={graph_GraphElement_name}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graph_Node", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="graph_Edge", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph2", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leavings3: BinaryAssociation = BinaryAssociation(
    name="leavings3",
    ends={
        Property(name="4", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
enterings5: BinaryAssociation = BinaryAssociation(
    name="enterings5",
    ends={
        Property(name="7", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
sourceNode8: BinaryAssociation = BinaryAssociation(
    name="sourceNode8",
    ends={
        Property(name="10", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
targetNode11: BinaryAssociation = BinaryAssociation(
    name="targetNode11",
    ends={
        Property(name="13", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_graph_Node_GraphElement = Generalization(general=GraphElement, specific=graph_Node)
gen_graph_Edge_GraphElement = Generalization(general=GraphElement, specific=graph_Edge)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Node, graph_Edge, GraphElement, graph_Graph, graph_GraphElement},
    associations={nodes0, edges1, leavings3, enterings5, sourceNode8, targetNode11},
    generalizations={gen_graph_Node_GraphElement, gen_graph_Edge_GraphElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)