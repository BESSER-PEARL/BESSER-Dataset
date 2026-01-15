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
CST_Tree = Class(name="CST::Tree")
CST_Node = Class(name="CST::Node")
CST_RNode = Class(name="CST::RNode")
Node = Class(name="Node")
CST_TNode = Class(name="CST::TNode")

# CST_Tree class attributes and methods

# CST_Node class attributes and methods
CST_Node_kind: Property = Property(name="kind", type=StringType)
CST_Node.attributes={CST_Node_kind}

# CST_RNode class attributes and methods

# Node class attributes and methods

# CST_TNode class attributes and methods
CST_TNode_value: Property = Property(name="value", type=StringType)
CST_TNode.attributes={CST_TNode_value}

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="CST_Node", type=CST_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="CST_Tree", type=CST_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="Node", type=CST_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=CST_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent4: BinaryAssociation = BinaryAssociation(
    name="parent4",
    ends={
        Property(name="Node5", type=CST_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=CST_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_CST_RNode_Node = Generalization(general=Node, specific=CST_RNode)
gen_CST_TNode_Node = Generalization(general=Node, specific=CST_TNode)

# Domain Model
domain_model = DomainModel(
    name="CST",
    types={CST_Tree, CST_Node, CST_RNode, Node, CST_TNode},
    associations={root0, children2, parent4},
    generalizations={gen_CST_RNode_Node, gen_CST_TNode_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)