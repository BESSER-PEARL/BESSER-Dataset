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
graph_Graph = Class(name="graph::Graph")

# graph_Node class attributes and methods
graph_Node_name: Property = Property(name="name", type=StringType)
graph_Node.attributes={graph_Node_name}

# graph_Edge class attributes and methods

# graph_Graph class attributes and methods

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
src3: BinaryAssociation = BinaryAssociation(
    name="src3",
    ends={
        Property(name="graph_Node5", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge4", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
trg6: BinaryAssociation = BinaryAssociation(
    name="trg6",
    ends={
        Property(name="graph_Node8", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge7", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Node, graph_Edge, graph_Graph},
    associations={nodes0, edges1, src3, trg6},
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