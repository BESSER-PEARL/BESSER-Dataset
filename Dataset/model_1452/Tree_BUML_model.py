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
tree_Node = Class(name="tree::Node")
tree_Edge = Class(name="tree::Edge")
tree_Diagram = Class(name="tree::Diagram")

# tree_Node class attributes and methods
tree_Node_name: Property = Property(name="name", type=StringType)
tree_Node.attributes={tree_Node_name}

# tree_Edge class attributes and methods

# tree_Diagram class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="tree_Node", type=tree_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Diagram", type=tree_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="tree_Edge", type=tree_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Diagram2", type=tree_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="tree_Node5", type=tree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Node3", type=tree_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="tree_Node8", type=tree_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Edge7", type=tree_Node, multiplicity=Multiplicity(0, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="tree_Node11", type=tree_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="tree_Edge10", type=tree_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tree",
    types={tree_Node, tree_Edge, tree_Diagram},
    associations={nodes0, edges1, children4, source6, target9},
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