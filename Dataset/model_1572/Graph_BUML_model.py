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
ScaffoldGraph_Graph = Class(name="ScaffoldGraph::Graph")
ScaffoldGraph_Vertex = Class(name="ScaffoldGraph::Vertex")
ScaffoldGraph_Edge = Class(name="ScaffoldGraph::Edge")

# ScaffoldGraph_Graph class attributes and methods
ScaffoldGraph_Graph_name: Property = Property(name="name", type=StringType)
ScaffoldGraph_Graph.attributes={ScaffoldGraph_Graph_name}

# ScaffoldGraph_Vertex class attributes and methods

# ScaffoldGraph_Edge class attributes and methods
ScaffoldGraph_Edge_weight: Property = Property(name="weight", type=IntegerType)
ScaffoldGraph_Edge.attributes={ScaffoldGraph_Edge_weight}

# Relationships
VEin3: BinaryAssociation = BinaryAssociation(
    name="VEin3",
    ends={
        Property(name="Edge", type=ScaffoldGraph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="EVin", type=ScaffoldGraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
VEout4: BinaryAssociation = BinaryAssociation(
    name="VEout4",
    ends={
        Property(name="Edge5", type=ScaffoldGraph_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="EVout", type=ScaffoldGraph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
EVin6: BinaryAssociation = BinaryAssociation(
    name="EVin6",
    ends={
        Property(name="Vertex", type=ScaffoldGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="VEin", type=ScaffoldGraph_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
EVout7: BinaryAssociation = BinaryAssociation(
    name="EVout7",
    ends={
        Property(name="Vertex8", type=ScaffoldGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="VEout", type=ScaffoldGraph_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
vertices0: BinaryAssociation = BinaryAssociation(
    name="vertices0",
    ends={
        Property(name="ScaffoldGraph_Vertex", type=ScaffoldGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="ScaffoldGraph_Graph", type=ScaffoldGraph_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="ScaffoldGraph_Edge", type=ScaffoldGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="ScaffoldGraph_Graph2", type=ScaffoldGraph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ScaffoldGraph",
    types={ScaffoldGraph_Graph, ScaffoldGraph_Vertex, ScaffoldGraph_Edge},
    associations={VEin3, VEout4, EVin6, EVout7, vertices0, edges1},
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