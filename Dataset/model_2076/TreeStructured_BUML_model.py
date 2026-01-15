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
StructuredTree_Tree = Class(name="StructuredTree::Tree")
StructuredTree_NodeKind = Class(name="StructuredTree::NodeKind")
StructuredTree_BranchKind = Class(name="StructuredTree::BranchKind")
StructuredTree_LeafKind = Class(name="StructuredTree::LeafKind")
NodeKind = Class(name="NodeKind")

# StructuredTree_Tree class attributes and methods

# StructuredTree_NodeKind class attributes and methods

# StructuredTree_BranchKind class attributes and methods

# StructuredTree_LeafKind class attributes and methods

# NodeKind class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="NodeKind", type=StructuredTree_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="tree", type=StructuredTree_NodeKind, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tree1: BinaryAssociation = BinaryAssociation(
    name="tree1",
    ends={
        Property(name="Tree", type=StructuredTree_NodeKind, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=StructuredTree_Tree, multiplicity=Multiplicity(0, 1))
    }
)
parent2: BinaryAssociation = BinaryAssociation(
    name="parent2",
    ends={
        Property(name="BranchKind", type=StructuredTree_NodeKind, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=StructuredTree_BranchKind, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="NodeKind4", type=StructuredTree_BranchKind, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=StructuredTree_NodeKind, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_StructuredTree_LeafKind_NodeKind = Generalization(general=NodeKind, specific=StructuredTree_LeafKind)
gen_StructuredTree_BranchKind_NodeKind = Generalization(general=NodeKind, specific=StructuredTree_BranchKind)

# Domain Model
domain_model = DomainModel(
    name="StructuredTree",
    types={StructuredTree_Tree, StructuredTree_NodeKind, StructuredTree_BranchKind, StructuredTree_LeafKind, NodeKind},
    associations={root0, tree1, parent2, children3},
    generalizations={gen_StructuredTree_LeafKind_NodeKind, gen_StructuredTree_BranchKind_NodeKind},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)