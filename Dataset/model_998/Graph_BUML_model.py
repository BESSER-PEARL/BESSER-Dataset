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
graph_Named = Class(name="graph::Named")
graph_Graph = Class(name="graph::Graph")
Named = Class(name="Named")
graph_Node = Class(name="graph::Node")
graph_Edge = Class(name="graph::Edge")

# graph_Named class attributes and methods
graph_Named_name: Property = Property(name="name", type=StringType)
graph_Named.attributes={graph_Named_name}

# graph_Graph class attributes and methods
graph_Graph_owner: Property = Property(name="owner", type=StringType)
graph_Graph.attributes={graph_Graph_owner}

# Named class attributes and methods

# graph_Node class attributes and methods
graph_Node_uri: Property = Property(name="uri", type=StringType)
graph_Node_type: Property = Property(name="type", type=StringType)
graph_Node_derivedOrNotExists: Property = Property(name="derivedOrNotExists", type=BooleanType)
graph_Node.attributes={graph_Node_derivedOrNotExists, graph_Node_type, graph_Node_uri}

# graph_Edge class attributes and methods
graph_Edge_exact: Property = Property(name="exact", type=BooleanType)
graph_Edge_pathDiscoveredByHeuristic: Property = Property(name="pathDiscoveredByHeuristic", type=StringType)
graph_Edge.attributes={graph_Edge_pathDiscoveredByHeuristic, graph_Edge_exact}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graph_Node", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="graph_Edge", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph2", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="graph_Node5", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge4", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="graph_Node8", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge7", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)
discoverBy9: BinaryAssociation = BinaryAssociation(
    name="discoverBy9",
    ends={
        Property(name="graph_Node11", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge10", type=graph_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_graph_Graph_Named = Generalization(general=Named, specific=graph_Graph)
gen_graph_Node_Named = Generalization(general=Named, specific=graph_Node)
gen_graph_Edge_Named = Generalization(general=Named, specific=graph_Edge)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Named, graph_Graph, Named, graph_Node, graph_Edge},
    associations={nodes0, edges1, source3, target6, discoverBy9},
    generalizations={gen_graph_Graph_Named, gen_graph_Node_Named, gen_graph_Edge_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)