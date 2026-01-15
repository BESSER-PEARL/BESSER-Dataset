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
tree2talltree_Node2TallNode = Class(name="tree2talltree::Node2TallNode")
tree2talltree_Node = Class(name="tree2talltree::Node")
tree2talltree_TallNode = Class(name="tree2talltree::TallNode")

# tree2talltree_Node2TallNode class attributes and methods
tree2talltree_Node2TallNode_name: Property = Property(name="name", type=StringType)
tree2talltree_Node2TallNode.attributes={tree2talltree_Node2TallNode_name}

# tree2talltree_Node class attributes and methods

# tree2talltree_TallNode class attributes and methods

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="Node2TallNode", type=tree2talltree_Node2TallNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=tree2talltree_Node2TallNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent3: BinaryAssociation = BinaryAssociation(
    name="parent3",
    ends={
        Property(name="Node2TallNode4", type=tree2talltree_Node2TallNode, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=tree2talltree_Node2TallNode, multiplicity=Multiplicity(0, 1))
    }
)
node5: BinaryAssociation = BinaryAssociation(
    name="node5",
    ends={
        Property(name="tree2talltree_Node", type=tree2talltree_Node2TallNode, multiplicity=Multiplicity(1, 1)),
        Property(name="tree2talltree_Node2TallNode", type=tree2talltree_Node, multiplicity=Multiplicity(1, 1))
    }
)
tallNode6: BinaryAssociation = BinaryAssociation(
    name="tallNode6",
    ends={
        Property(name="tree2talltree_TallNode", type=tree2talltree_Node2TallNode, multiplicity=Multiplicity(1, 1)),
        Property(name="tree2talltree_Node2TallNode7", type=tree2talltree_TallNode, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tree2talltree",
    types={tree2talltree_Node2TallNode, tree2talltree_Node, tree2talltree_TallNode},
    associations={children1, parent3, node5, tallNode6},
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