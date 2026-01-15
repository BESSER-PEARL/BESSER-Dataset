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
graph_Node = Class(name="graph::Node", is_abstract=True)
graph_Center = Class(name="graph::Center")
Node = Class(name="Node")
graph_Boundary = Class(name="graph::Boundary")
graph_G = Class(name="graph::G")

# graph_Node class attributes and methods
graph_Node_id: Property = Property(name="id", type=StringType)
graph_Node.attributes={graph_Node_id}

# graph_Center class attributes and methods

# Node class attributes and methods

# graph_Boundary class attributes and methods

# graph_G class attributes and methods

# Relationships
out1: BinaryAssociation = BinaryAssociation(
    name="out1",
    ends={
        Property(name="graph_Node", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Node0", type=graph_Node, multiplicity=Multiplicity(0, 9999))
    }
)
in3: BinaryAssociation = BinaryAssociation(
    name="in3",
    ends={
        Property(name="graph_Node4", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Node2", type=graph_Node, multiplicity=Multiplicity(0, 9999))
    }
)
node5: BinaryAssociation = BinaryAssociation(
    name="node5",
    ends={
        Property(name="graph_Node6", type=graph_G, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_G", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_graph_Center_Node = Generalization(general=Node, specific=graph_Center)
gen_graph_Boundary_Node = Generalization(general=Node, specific=graph_Boundary)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Node, graph_Center, Node, graph_Boundary, graph_G},
    associations={out1, in3, node5},
    generalizations={gen_graph_Center_Node, gen_graph_Boundary_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)