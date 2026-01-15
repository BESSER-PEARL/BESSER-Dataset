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
Tree_Storage = Class(name="Tree::Storage")
Tree_Node = Class(name="Tree::Node")

# Tree_Storage class attributes and methods

# Tree_Node class attributes and methods
Tree_Node_value: Property = Property(name="value", type=IntegerType)
Tree_Node.attributes={Tree_Node_value}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Tree_Node", type=Tree_Storage, multiplicity=Multiplicity(1, 1)),
        Property(name="Tree_Storage", type=Tree_Node, multiplicity=Multiplicity(0, 9999))
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="Tree_Node3", type=Tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Tree_Node1", type=Tree_Node, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Tree",
    types={Tree_Storage, Tree_Node},
    associations={nodes0, children2},
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