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

# graph_Graph class attributes and methods

# graph_Node class attributes and methods
graph_Node_name: Property = Property(name="name", type=StringType)
graph_Node.attributes={graph_Node_name}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graph_Node", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
related2: BinaryAssociation = BinaryAssociation(
    name="related2",
    ends={
        Property(name="graph_Graph3", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph1", type=graph_Graph, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Graph, graph_Node},
    associations={nodes0, related2},
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