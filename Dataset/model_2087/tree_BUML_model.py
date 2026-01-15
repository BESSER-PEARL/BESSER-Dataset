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
tree_Node_anAttribute: Property = Property(name="anAttribute", type=IntegerType)
tree_Node_anAttribute2: Property = Property(name="anAttribute2", type=IntegerType)
tree_Node_anAttribute3: Property = Property(name="anAttribute3", type=IntegerType)
tree_Node_name: Property = Property(name="name", type=StringType)
tree_Node_anAttribute4: Property = Property(name="anAttribute4", type=IntegerType)
tree_Node.attributes={tree_Node_anAttribute3, tree_Node_anAttribute, tree_Node_anAttribute2, tree_Node_anAttribute4, tree_Node_name}

# Relationships
parent4: BinaryAssociation = BinaryAssociation(
    name="parent4",
    ends={
        Property(name="Node5", type=tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="child", type=tree_Node, multiplicity=Multiplicity(0, 1))
    }
)
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="tree_Node", type=tree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Tree", type=tree_Node, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child2: BinaryAssociation = BinaryAssociation(
    name="child2",
    ends={
        Property(name="Node", type=tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=tree_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aReference7: BinaryAssociation = BinaryAssociation(
    name="aReference7",
    ends={
        Property(name="tree_Node8", type=tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Node6", type=tree_Node, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tree",
    types={tree_Tree, tree_Node},
    associations={parent4, root0, child2, aReference7},
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