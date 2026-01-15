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
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="BLACK")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="NODE"),
			EnumerationLiteral(name="LEAF"),
			EnumerationLiteral(name="ROOT")
    }
)

# Classes
redblacktree2_Tree = Class(name="redblacktree2::Tree")
redblacktree2_Node = Class(name="redblacktree2::Node")

# redblacktree2_Tree class attributes and methods

# redblacktree2_Node class attributes and methods
redblacktree2_Node_value: Property = Property(name="value", type=IntegerType)
redblacktree2_Node.attributes={redblacktree2_Node_value}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="redblacktree2_Node", type=redblacktree2_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="redblacktree2_Tree", type=redblacktree2_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left5: BinaryAssociation = BinaryAssociation(
    name="left5",
    ends={
        Property(name="redblacktree2_Node6", type=redblacktree2_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="redblacktree2_Node4", type=redblacktree2_Node, multiplicity=Multiplicity(0, 1))
    }
)
root1: BinaryAssociation = BinaryAssociation(
    name="root1",
    ends={
        Property(name="redblacktree2_Node3", type=redblacktree2_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="redblacktree2_Tree2", type=redblacktree2_Node, multiplicity=Multiplicity(0, 1))
    }
)
right8: BinaryAssociation = BinaryAssociation(
    name="right8",
    ends={
        Property(name="redblacktree2_Node9", type=redblacktree2_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="redblacktree2_Node7", type=redblacktree2_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="redblacktree2",
    types={redblacktree2_Tree, redblacktree2_Node, Color, Type},
    associations={nodes0, left5, root1, right8},
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