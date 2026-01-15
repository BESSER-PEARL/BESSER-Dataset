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
Graph_Node = Class(name="Graph::Node")
Graph_Edge = Class(name="Graph::Edge")

# Graph_Node class attributes and methods
Graph_Node_name: Property = Property(name="name", type=StringType)
Graph_Node_type: Property = Property(name="type", type=StringType)
Graph_Node_size: Property = Property(name="size", type=FloatType)
Graph_Node.attributes={Graph_Node_size, Graph_Node_name, Graph_Node_type}

# Graph_Edge class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="Graph_Node", type=Graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Edge", type=Graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="Graph_Node3", type=Graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph_Edge2", type=Graph_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Graph",
    types={Graph_Node, Graph_Edge},
    associations={source0, target1},
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