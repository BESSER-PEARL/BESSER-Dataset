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
graph_Pattern_Matching_Master_Project_Graph = Class(name="graph::Pattern::Matching::Master::Project::Graph")
graph_Pattern_Matching_Master_Project_Edge = Class(name="graph::Pattern::Matching::Master::Project::Edge")
graph_Pattern_Matching_Master_Project_Vertex = Class(name="graph::Pattern::Matching::Master::Project::Vertex")
graph_Pattern_Matching_Master_Project_Entry = Class(name="graph::Pattern::Matching::Master::Project::Entry")

# graph_Pattern_Matching_Master_Project_Graph class attributes and methods
graph_Pattern_Matching_Master_Project_Graph_name: Property = Property(name="name", type=StringType)
graph_Pattern_Matching_Master_Project_Graph_direct: Property = Property(name="direct", type=BooleanType)
graph_Pattern_Matching_Master_Project_Graph_m_isConnected: Method = Method(name="isConnected", parameters={}, type=BooleanType)
graph_Pattern_Matching_Master_Project_Graph.attributes={graph_Pattern_Matching_Master_Project_Graph_name, graph_Pattern_Matching_Master_Project_Graph_direct}
graph_Pattern_Matching_Master_Project_Graph.methods={graph_Pattern_Matching_Master_Project_Graph_m_isConnected}

# graph_Pattern_Matching_Master_Project_Edge class attributes and methods
graph_Pattern_Matching_Master_Project_Edge_label: Property = Property(name="label", type=StringType)
graph_Pattern_Matching_Master_Project_Edge.attributes={graph_Pattern_Matching_Master_Project_Edge_label}

# graph_Pattern_Matching_Master_Project_Vertex class attributes and methods
graph_Pattern_Matching_Master_Project_Vertex_name: Property = Property(name="name", type=StringType)
graph_Pattern_Matching_Master_Project_Vertex.attributes={graph_Pattern_Matching_Master_Project_Vertex_name}

# graph_Pattern_Matching_Master_Project_Entry class attributes and methods
graph_Pattern_Matching_Master_Project_Entry_key: Property = Property(name="key", type=StringType)
graph_Pattern_Matching_Master_Project_Entry_value: Property = Property(name="value", type=StringType)
graph_Pattern_Matching_Master_Project_Entry.attributes={graph_Pattern_Matching_Master_Project_Entry_key, graph_Pattern_Matching_Master_Project_Entry_value}

# Relationships
edges0: BinaryAssociation = BinaryAssociation(
    name="edges0",
    ends={
        Property(name="Edge", type=graph_Pattern_Matching_Master_Project_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=graph_Pattern_Matching_Master_Project_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
vertices1: BinaryAssociation = BinaryAssociation(
    name="vertices1",
    ends={
        Property(name="Vertex", type=graph_Pattern_Matching_Master_Project_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph2", type=graph_Pattern_Matching_Master_Project_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
graph3: BinaryAssociation = BinaryAssociation(
    name="graph3",
    ends={
        Property(name="Graph", type=graph_Pattern_Matching_Master_Project_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="vertices", type=graph_Pattern_Matching_Master_Project_Graph, multiplicity=Multiplicity(1, 1))
    }
)
entries4: BinaryAssociation = BinaryAssociation(
    name="entries4",
    ends={
        Property(name="graph_Pattern_Matching_Master_Project_Entry", type=graph_Pattern_Matching_Master_Project_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Pattern_Matching_Master_Project_Vertex", type=graph_Pattern_Matching_Master_Project_Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph5: BinaryAssociation = BinaryAssociation(
    name="graph5",
    ends={
        Property(name="Graph6", type=graph_Pattern_Matching_Master_Project_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=graph_Pattern_Matching_Master_Project_Graph, multiplicity=Multiplicity(1, 1))
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="graph_Pattern_Matching_Master_Project_Vertex8", type=graph_Pattern_Matching_Master_Project_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Pattern_Matching_Master_Project_Edge", type=graph_Pattern_Matching_Master_Project_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="graph_Pattern_Matching_Master_Project_Vertex11", type=graph_Pattern_Matching_Master_Project_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Pattern_Matching_Master_Project_Edge10", type=graph_Pattern_Matching_Master_Project_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
entries12: BinaryAssociation = BinaryAssociation(
    name="entries12",
    ends={
        Property(name="graph_Pattern_Matching_Master_Project_Entry14", type=graph_Pattern_Matching_Master_Project_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Pattern_Matching_Master_Project_Edge13", type=graph_Pattern_Matching_Master_Project_Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph_Pattern_Matching_Master_Project",
    types={graph_Pattern_Matching_Master_Project_Graph, graph_Pattern_Matching_Master_Project_Edge, graph_Pattern_Matching_Master_Project_Vertex, graph_Pattern_Matching_Master_Project_Entry},
    associations={edges0, vertices1, graph3, entries4, graph5, source7, target9, entries12},
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