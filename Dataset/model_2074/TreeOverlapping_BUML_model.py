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
OverlappingTree_Tree = Class(name="OverlappingTree::Tree")
OverlappingTree_NodeKind = Class(name="OverlappingTree::NodeKind")
OverlappingTree_Child = Class(name="OverlappingTree::Child")

# OverlappingTree_Tree class attributes and methods

# OverlappingTree_NodeKind class attributes and methods

# OverlappingTree_Child class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="NodeKind", type=OverlappingTree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="tree", type=OverlappingTree_NodeKind, multiplicity=Multiplicity(1, 1))
    }
)
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="OverlappingTree_Child", type=OverlappingTree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="OverlappingTree_Tree", type=OverlappingTree_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tree2: BinaryAssociation = BinaryAssociation(
    name="tree2",
    ends={
        Property(name="Tree", type=OverlappingTree_NodeKind, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=OverlappingTree_Tree, multiplicity=Multiplicity(0, 9999))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="Child", type=OverlappingTree_NodeKind, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=OverlappingTree_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeChildren4: BinaryAssociation = BinaryAssociation(
    name="nodeChildren4",
    ends={
        Property(name="Child5", type=OverlappingTree_NodeKind, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=OverlappingTree_Child, multiplicity=Multiplicity(0, 9999))
    }
)
node6: BinaryAssociation = BinaryAssociation(
    name="node6",
    ends={
        Property(name="NodeKind7", type=OverlappingTree_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="nodeChildren", type=OverlappingTree_NodeKind, multiplicity=Multiplicity(1, 1))
    }
)
parent8: BinaryAssociation = BinaryAssociation(
    name="parent8",
    ends={
        Property(name="NodeKind9", type=OverlappingTree_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=OverlappingTree_NodeKind, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="OverlappingTree",
    types={OverlappingTree_Tree, OverlappingTree_NodeKind, OverlappingTree_Child},
    associations={root0, children1, tree2, children3, nodeChildren4, node6, parent8},
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