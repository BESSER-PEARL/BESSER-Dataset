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
tree_TreeNode = Class(name="tree::TreeNode", is_abstract=True)
tree_Leaf = Class(name="tree::Leaf")
TreeNode = Class(name="TreeNode")
tree_NonTerminal = Class(name="tree::NonTerminal")

# tree_TreeNode class attributes and methods
tree_TreeNode_data: Property = Property(name="data", type=StringType)
tree_TreeNode.attributes={tree_TreeNode_data}

# tree_Leaf class attributes and methods

# TreeNode class attributes and methods

# tree_NonTerminal class attributes and methods

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="tree_TreeNode", type=tree_TreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_TreeNode0", type=tree_TreeNode, multiplicity=Multiplicity(0, 1))
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="tree_TreeNode3", type=tree_NonTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_NonTerminal", type=tree_TreeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tree_Leaf_TreeNode = Generalization(general=TreeNode, specific=tree_Leaf)
gen_tree_NonTerminal_TreeNode = Generalization(general=TreeNode, specific=tree_NonTerminal)

# Domain Model
domain_model = DomainModel(
    name="tree",
    types={tree_TreeNode, tree_Leaf, TreeNode, tree_NonTerminal},
    associations={parent1, children2},
    generalizations={gen_tree_Leaf_TreeNode, gen_tree_NonTerminal_TreeNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)