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
tree_TreeNode = Class(name="tree_TreeNode")
tree_EObject = Class(name="tree_EObject")

# tree_TreeNode class attributes and methods

# tree_EObject class attributes and methods

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="TreeNode", type=tree_TreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=tree_TreeNode, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="TreeNode4", type=tree_TreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=tree_TreeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data5: BinaryAssociation = BinaryAssociation(
    name="data5",
    ends={
        Property(name="tree_EObject", type=tree_TreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_TreeNode", type=tree_EObject, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tree",
    types={tree_TreeNode, tree_EObject},
    associations={parent1, children3, data5},
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