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

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graph_Node", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing1: BinaryAssociation = BinaryAssociation(
    name="outgoing1",
    ends={
        Property(name="Edge", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming2: BinaryAssociation = BinaryAssociation(
    name="incoming2",
    ends={
        Property(name="Edge3", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="Node", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="Node6", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Graph, graph_Node, graph_Edge},
    associations={nodes0, outgoing1, incoming2, source4, target5},
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