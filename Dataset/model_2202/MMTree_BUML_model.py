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

# Enumerations
LeafSize: Enumeration = Enumeration(
    name="LeafSize",
    literals={
            EnumerationLiteral(name="small"),
			EnumerationLiteral(name="medium"),
			EnumerationLiteral(name="big")
    }
)

# Classes
MMTree_TreeElement = Class(name="MMTree::TreeElement", is_abstract=True)
MMTree_Leaf = Class(name="MMTree::Leaf")
MMTree_Node = Class(name="MMTree::Node")
TreeElement = Class(name="TreeElement")

# MMTree_TreeElement class attributes and methods
MMTree_TreeElement_name: Property = Property(name="name", type=StringType)
MMTree_TreeElement.attributes={MMTree_TreeElement_name}

# MMTree_Leaf class attributes and methods
MMTree_Leaf_size: Property = Property(name="size", type=StringType)
MMTree_Leaf.attributes={MMTree_Leaf_size}

# MMTree_Node class attributes and methods

# TreeElement class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="MMTree_TreeElement", type=MMTree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="MMTree_Node", type=MMTree_TreeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_MMTree_Leaf_TreeElement = Generalization(general=TreeElement, specific=MMTree_Leaf)
gen_MMTree_Node_TreeElement = Generalization(general=TreeElement, specific=MMTree_Node)

# Domain Model
domain_model = DomainModel(
    name="MMTree",
    types={MMTree_TreeElement, MMTree_Leaf, MMTree_Node, TreeElement, LeafSize},
    associations={children0},
    generalizations={gen_MMTree_Leaf_TreeElement, gen_MMTree_Node_TreeElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)