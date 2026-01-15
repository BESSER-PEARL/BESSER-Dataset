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
graph_Node = Class(name="graph::Node")
graph_Edge = Class(name="graph::Edge")
graph_AbstractNamedObject = Class(name="graph::AbstractNamedObject", is_abstract=True)
graph_Graph = Class(name="graph::Graph")
AbstractNamedObject = Class(name="AbstractNamedObject")

# graph_Node class attributes and methods

# graph_Edge class attributes and methods

# graph_AbstractNamedObject class attributes and methods
graph_AbstractNamedObject_name: Property = Property(name="name", type=StringType)
graph_AbstractNamedObject.attributes={graph_AbstractNamedObject_name}

# graph_Graph class attributes and methods

# AbstractNamedObject class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graph_Node", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingEdges1: BinaryAssociation = BinaryAssociation(
    name="incomingEdges1",
    ends={
        Property(name="Edge", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingEdges2: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges2",
    ends={
        Property(name="Edge3", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="Node", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="Node6", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_graph_Node_AbstractNamedObject = Generalization(general=AbstractNamedObject, specific=graph_Node)
gen_graph_Graph_AbstractNamedObject = Generalization(general=AbstractNamedObject, specific=graph_Graph)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Node, graph_Edge, graph_AbstractNamedObject, graph_Graph, AbstractNamedObject},
    associations={nodes0, incomingEdges1, outgoingEdges2, source4, target5},
    generalizations={gen_graph_Node_AbstractNamedObject, gen_graph_Graph_AbstractNamedObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)