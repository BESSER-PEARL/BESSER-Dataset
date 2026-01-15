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
tree_Tree = Class(name="tree::Tree")
tree_Node = Class(name="tree::Node")

# tree_Tree class attributes and methods
tree_Tree_name: Property = Property(name="name", type=StringType)
tree_Tree.attributes={tree_Tree_name}

# tree_Node class attributes and methods
tree_Node_label: Property = Property(name="label", type=StringType)
tree_Node_data: Property = Property(name="data", type=StringType)
tree_Node.attributes={tree_Node_label, tree_Node_data}

# Relationships
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="tree_Node3", type=tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Node1", type=tree_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="tree_Node", type=tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Tree", type=tree_Node, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="tree",
    types={tree_Tree, tree_Node},
    associations={children2, root0},
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