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
SimpleTree_Tree = Class(name="SimpleTree::Tree")
SimpleTree_NodeKind = Class(name="SimpleTree::NodeKind")

# SimpleTree_Tree class attributes and methods

# SimpleTree_NodeKind class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="SimpleTree_NodeKind", type=SimpleTree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleTree_Tree", type=SimpleTree_NodeKind, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="SimpleTree_NodeKind3", type=SimpleTree_NodeKind, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleTree_NodeKind1", type=SimpleTree_NodeKind, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="SimpleTree",
    types={SimpleTree_Tree, SimpleTree_NodeKind},
    associations={root0, children2},
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