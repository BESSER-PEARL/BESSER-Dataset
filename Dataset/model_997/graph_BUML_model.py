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

# graph_Graph class attributes and methods

# graph_Node class attributes and methods
graph_Node_name: Property = Property(name="name", type=StringType)
graph_Node.attributes={graph_Node_name}

# graph_Edge class attributes and methods
graph_Edge_name: Property = Property(name="name", type=StringType)
graph_Edge.attributes={graph_Edge_name}

# Relationships
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="Edge", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph2", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph3: BinaryAssociation = BinaryAssociation(
    name="graph3",
    ends={
        Property(name="Graph", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=graph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
src4: BinaryAssociation = BinaryAssociation(
    name="src4",
    ends={
        Property(name="graph_Node", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
trg5: BinaryAssociation = BinaryAssociation(
    name="trg5",
    ends={
        Property(name="graph_Node7", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge6", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
graph8: BinaryAssociation = BinaryAssociation(
    name="graph8",
    ends={
        Property(name="Graph9", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=graph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Graph, graph_Node, graph_Edge},
    associations={edges1, graph3, src4, trg5, graph8, nodes0},
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