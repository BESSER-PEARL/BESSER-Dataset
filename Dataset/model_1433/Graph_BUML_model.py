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
GraphMM_Node = Class(name="GraphMM::Node")
GraphMM_Edge = Class(name="GraphMM::Edge")

# GraphMM_Node class attributes and methods
GraphMM_Node_name: Property = Property(name="name", type=StringType)
GraphMM_Node_type: Property = Property(name="type", type=StringType)
GraphMM_Node_size: Property = Property(name="size", type=FloatType)
GraphMM_Node.attributes={GraphMM_Node_name, GraphMM_Node_type, GraphMM_Node_size}

# GraphMM_Edge class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="GraphMM_Node", type=GraphMM_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphMM_Edge", type=GraphMM_Node, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="GraphMM_Node3", type=GraphMM_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphMM_Edge2", type=GraphMM_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="GraphMM",
    types={GraphMM_Node, GraphMM_Edge},
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