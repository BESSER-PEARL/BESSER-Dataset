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
tree_Node = Class(name="tree::Node")

# tree_Node class attributes and methods
tree_Node_name: Property = Property(name="name", type=StringType)
tree_Node.attributes={tree_Node_name}

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="tree_Node", type=tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Node0", type=tree_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
related3: BinaryAssociation = BinaryAssociation(
    name="related3",
    ends={
        Property(name="tree_Node4", type=tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Node2", type=tree_Node, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tree",
    types={tree_Node},
    associations={children1, related3},
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