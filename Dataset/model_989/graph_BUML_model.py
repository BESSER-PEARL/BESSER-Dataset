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
graph_Graph = Class(name="graph::Graph")
graph_Node = Class(name="graph::Node")
graph_Edge = Class(name="graph::Edge")
graph_Mark = Class(name="graph::Mark")

# graph_Graph class attributes and methods
graph_Graph_name: Property = Property(name="name", type=StringType)
graph_Graph.attributes={graph_Graph_name}

# graph_Node class attributes and methods
graph_Node_name: Property = Property(name="name", type=StringType)
graph_Node.attributes={graph_Node_name}

# graph_Edge class attributes and methods
graph_Edge_name: Property = Property(name="name", type=StringType)
graph_Edge.attributes={graph_Edge_name}

# graph_Mark class attributes and methods
graph_Mark_time: Property = Property(name="time", type=StringType)
graph_Mark.attributes={graph_Mark_time}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="Edge", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph2", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
marks3: BinaryAssociation = BinaryAssociation(
    name="marks3",
    ends={
        Property(name="Mark", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph4", type=graph_Mark, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mark5: BinaryAssociation = BinaryAssociation(
    name="mark5",
    ends={
        Property(name="Mark6", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=graph_Mark, multiplicity=Multiplicity(0, 1))
    }
)
graph7: BinaryAssociation = BinaryAssociation(
    name="graph7",
    ends={
        Property(name="Graph", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=graph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="graph_Node", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="graph_Node11", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge10", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
graph12: BinaryAssociation = BinaryAssociation(
    name="graph12",
    ends={
        Property(name="Graph13", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=graph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
node14: BinaryAssociation = BinaryAssociation(
    name="node14",
    ends={
        Property(name="Node15", type=graph_Mark, multiplicity=Multiplicity(1, 1)),
        Property(name="mark", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
graph16: BinaryAssociation = BinaryAssociation(
    name="graph16",
    ends={
        Property(name="Graph17", type=graph_Mark, multiplicity=Multiplicity(1, 1)),
        Property(name="marks", type=graph_Graph, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Graph, graph_Node, graph_Edge, graph_Mark},
    associations={nodes0, edges1, marks3, mark5, graph7, source8, target9, graph12, node14, graph16},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)