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
graph_Graph = Class(name="graph::Graph")
Named = Class(name="Named")
graph_Edge = Class(name="graph::Edge")
graph_Vertex = Class(name="graph::Vertex")
Typed = Class(name="Typed")
GraphElement = Class(name="GraphElement")
graph_Label = Class(name="graph::Label")
graph_Named = Class(name="graph::Named", is_abstract=True)
graph_Typed = Class(name="graph::Typed", is_abstract=True)
graph_Entry = Class(name="graph::Entry")
graph_GraphElement = Class(name="graph::GraphElement", is_abstract=True)

# graph_Graph class attributes and methods
graph_Graph_direct: Property = Property(name="direct", type=BooleanType)
graph_Graph.attributes={graph_Graph_direct}

# Named class attributes and methods

# graph_Edge class attributes and methods

# graph_Vertex class attributes and methods

# Typed class attributes and methods

# GraphElement class attributes and methods

# graph_Label class attributes and methods

# graph_Named class attributes and methods
graph_Named_name: Property = Property(name="name", type=StringType)
graph_Named.attributes={graph_Named_name}

# graph_Typed class attributes and methods
graph_Typed_type: Property = Property(name="type", type=StringType)
graph_Typed.attributes={graph_Typed_type}

# graph_Entry class attributes and methods
graph_Entry_key: Property = Property(name="key", type=StringType)
graph_Entry_value: Property = Property(name="value", type=StringType)
graph_Entry.attributes={graph_Entry_value, graph_Entry_key}

# graph_GraphElement class attributes and methods
graph_GraphElement_id: Property = Property(name="id", type=IntegerType)
graph_GraphElement.attributes={graph_GraphElement_id}

# Relationships
edges0: BinaryAssociation = BinaryAssociation(
    name="edges0",
    ends={
        Property(name="Edge", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vertices1: BinaryAssociation = BinaryAssociation(
    name="vertices1",
    ends={
        Property(name="Vertex", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph2", type=graph_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ingoingEdges7: BinaryAssociation = BinaryAssociation(
    name="ingoingEdges7",
    ends={
        Property(name="targetVertex", type=graph_Edge, multiplicity=Multiplicity(0, 9999)),
        Property(name="Edge8", type=graph_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
graph9: BinaryAssociation = BinaryAssociation(
    name="graph9",
    ends={
        Property(name="Graph10", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=graph_Graph, multiplicity=Multiplicity(0, 1))
    }
)
label11: BinaryAssociation = BinaryAssociation(
    name="label11",
    ends={
        Property(name="Label12", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=graph_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SourceVertex13: BinaryAssociation = BinaryAssociation(
    name="SourceVertex13",
    ends={
        Property(name="Vertex14", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=graph_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
targetVertex15: BinaryAssociation = BinaryAssociation(
    name="targetVertex15",
    ends={
        Property(name="Vertex16", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="ingoingEdges", type=graph_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
graph3: BinaryAssociation = BinaryAssociation(
    name="graph3",
    ends={
        Property(name="Graph", type=graph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="vertices", type=graph_Graph, multiplicity=Multiplicity(0, 1))
    }
)
label4: BinaryAssociation = BinaryAssociation(
    name="label4",
    ends={
        Property(name="Label", type=graph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="vertex", type=graph_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoingEdges5: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges5",
    ends={
        Property(name="Edge6", type=graph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="SourceVertex", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
edge17: BinaryAssociation = BinaryAssociation(
    name="edge17",
    ends={
        Property(name="Edge18", type=graph_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=graph_Edge, multiplicity=Multiplicity(0, 1))
    }
)
vertex19: BinaryAssociation = BinaryAssociation(
    name="vertex19",
    ends={
        Property(name="Vertex21", type=graph_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="label20", type=graph_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
entries22: BinaryAssociation = BinaryAssociation(
    name="entries22",
    ends={
        Property(name="Entry", type=graph_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="label23", type=graph_Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label24: BinaryAssociation = BinaryAssociation(
    name="label24",
    ends={
        Property(name="Label25", type=graph_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="entries", type=graph_Label, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_graph_Graph_Named = Generalization(general=Named, specific=graph_Graph)
gen_graph_Edge_Typed = Generalization(general=Typed, specific=graph_Edge)
gen_graph_Vertex_GraphElement = Generalization(general=GraphElement, specific=graph_Vertex)
gen_graph_Label_Named = Generalization(general=Named, specific=graph_Label)
gen_graph_Typed_Named = Generalization(general=Named, specific=graph_Typed)
gen_graph_GraphElement_Typed = Generalization(general=Typed, specific=graph_GraphElement)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Graph, Named, graph_Edge, graph_Vertex, Typed, GraphElement, graph_Label, graph_Named, graph_Typed, graph_Entry, graph_GraphElement},
    associations={edges0, vertices1, ingoingEdges7, graph9, label11, SourceVertex13, targetVertex15, graph3, label4, outgoingEdges5, edge17, vertex19, entries22, label24},
    generalizations={gen_graph_Graph_Named, gen_graph_Edge_Typed, gen_graph_Vertex_GraphElement, gen_graph_Label_Named, gen_graph_Typed_Named, gen_graph_GraphElement_Typed},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)