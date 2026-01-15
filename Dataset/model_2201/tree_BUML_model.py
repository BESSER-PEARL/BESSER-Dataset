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
tree_Tree = Class(name="tree::Tree")

# tree_Node class attributes and methods
tree_Node_name: Property = Property(name="name", type=StringType)
tree_Node.attributes={tree_Node_name}

# tree_Tree class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="tree_Node", type=tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Tree", type=tree_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="tree_Node3", type=tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Node1", type=tree_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="tree",
    types={tree_Node, tree_Tree},
    associations={children0, children2},
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