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
Tree_Node = Class(name="Tree::Node")
Tree_Tree = Class(name="Tree::Tree")
Node = Class(name="Node")

# Tree_Node class attributes and methods
Tree_Node_id: Property = Property(name="id", type=StringType)
Tree_Node.attributes={Tree_Node_id}

# Tree_Tree class attributes and methods

# Node class attributes and methods

# Relationships
childs1: BinaryAssociation = BinaryAssociation(
    name="childs1",
    ends={
        Property(name="Node", type=Tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=Tree_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent3: BinaryAssociation = BinaryAssociation(
    name="parent3",
    ends={
        Property(name="Node4", type=Tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="childs", type=Tree_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Tree_Tree_Node = Generalization(general=Node, specific=Tree_Tree)

# Domain Model
domain_model = DomainModel(
    name="Tree",
    types={Tree_Node, Tree_Tree, Node},
    associations={childs1, parent3},
    generalizations={gen_Tree_Tree_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)