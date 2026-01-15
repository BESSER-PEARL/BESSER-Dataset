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
bintree_BinTreeNode = Class(name="bintree::BinTreeNode")

# bintree_BinTreeNode class attributes and methods
bintree_BinTreeNode_data: Property = Property(name="data", type=StringType)
bintree_BinTreeNode.attributes={bintree_BinTreeNode_data}

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="bintree_BinTreeNode", type=bintree_BinTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bintree_BinTreeNode0", type=bintree_BinTreeNode, multiplicity=Multiplicity(0, 1))
    }
)
left3: BinaryAssociation = BinaryAssociation(
    name="left3",
    ends={
        Property(name="bintree_BinTreeNode4", type=bintree_BinTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bintree_BinTreeNode2", type=bintree_BinTreeNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right6: BinaryAssociation = BinaryAssociation(
    name="right6",
    ends={
        Property(name="bintree_BinTreeNode7", type=bintree_BinTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="bintree_BinTreeNode5", type=bintree_BinTreeNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="bintree",
    types={bintree_BinTreeNode},
    associations={parent1, left3, right6},
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