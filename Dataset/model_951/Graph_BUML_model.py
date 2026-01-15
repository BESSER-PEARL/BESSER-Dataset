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
Graph_Graph = Class(name="Graph::Graph")
Graph_Node = Class(name="Graph::Node")
Graph_Edge = Class(name="Graph::Edge")

# Graph_Graph class attributes and methods

# Graph_Node class attributes and methods
Graph_Node_name: Property = Property(name="name", type=StringType)
Graph_Node.attributes={Graph_Node_name}

# Graph_Edge class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Graph_Node", type=Graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Graph", type=Graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing1: BinaryAssociation = BinaryAssociation(
    name="outgoing1",
    ends={
        Property(name="Edge", type=Graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming2: BinaryAssociation = BinaryAssociation(
    name="incoming2",
    ends={
        Property(name="Edge3", type=Graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="Node", type=Graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=Graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="Node6", type=Graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=Graph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Graph",
    types={Graph_Graph, Graph_Node, Graph_Edge},
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