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
graph_Node = Class(name="graph_Node")
HasName = Class(name="HasName")
graph_Edge = Class(name="graph_Edge")
graph_SubNode = Class(name="graph_SubNode")
graph_Root = Class(name="graph_Root")
graph_HasName = Class(name="graph_HasName", is_abstract=True)

# graph_Node class attributes and methods

# HasName class attributes and methods

# graph_Edge class attributes and methods

# graph_SubNode class attributes and methods

# graph_Root class attributes and methods

# graph_HasName class attributes and methods
graph_HasName_name: Property = Property(name="name", type=StringType)
graph_HasName.attributes={graph_HasName_name}

# Relationships
outgoingEdge0: BinaryAssociation = BinaryAssociation(
    name="outgoingEdge0",
    ends={
        Property(name="Edge", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceNode", type=graph_Edge, multiplicity=Multiplicity(0, 1))
    }
)
incomingEdge1: BinaryAssociation = BinaryAssociation(
    name="incomingEdge1",
    ends={
        Property(name="Edge2", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="destinationNode", type=graph_Edge, multiplicity=Multiplicity(0, 1))
    }
)
subNodes3: BinaryAssociation = BinaryAssociation(
    name="subNodes3",
    ends={
        Property(name="SubNode", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="masterNode", type=graph_SubNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destinationNode4: BinaryAssociation = BinaryAssociation(
    name="destinationNode4",
    ends={
        Property(name="Node", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdge", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
sourceNode5: BinaryAssociation = BinaryAssociation(
    name="sourceNode5",
    ends={
        Property(name="Node6", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdge", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
edges7: BinaryAssociation = BinaryAssociation(
    name="edges7",
    ends={
        Property(name="graph_Edge", type=graph_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Root", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes8: BinaryAssociation = BinaryAssociation(
    name="nodes8",
    ends={
        Property(name="graph_Node", type=graph_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Root9", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
masterNode10: BinaryAssociation = BinaryAssociation(
    name="masterNode10",
    ends={
        Property(name="Node11", type=graph_SubNode, multiplicity=Multiplicity(1, 1)),
        Property(name="subNodes", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_graph_Node_HasName = Generalization(general=HasName, specific=graph_Node)
gen_graph_SubNode_HasName = Generalization(general=HasName, specific=graph_SubNode)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Node, HasName, graph_Edge, graph_SubNode, graph_Root, graph_HasName},
    associations={outgoingEdge0, incomingEdge1, subNodes3, destinationNode4, sourceNode5, edges7, nodes8, masterNode10},
    generalizations={gen_graph_Node_HasName, gen_graph_SubNode_HasName},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)