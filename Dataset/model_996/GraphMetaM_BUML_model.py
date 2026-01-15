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
Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or")
    }
)

# Classes
GraphMetaM_Graph = Class(name="GraphMetaM::Graph")
GraphMetaM_Vertex = Class(name="GraphMetaM::Vertex")
GraphMetaM_Edge = Class(name="GraphMetaM::Edge")
GraphMetaM_Model = Class(name="GraphMetaM::Model")

# GraphMetaM_Graph class attributes and methods
GraphMetaM_Graph_cycles: Property = Property(name="cycles", type=IntegerType)
GraphMetaM_Graph_rName: Property = Property(name="rName", type=StringType)
GraphMetaM_Graph_name: Property = Property(name="name", type=StringType)
GraphMetaM_Graph.attributes={GraphMetaM_Graph_rName, GraphMetaM_Graph_name, GraphMetaM_Graph_cycles}

# GraphMetaM_Vertex class attributes and methods
GraphMetaM_Vertex_cycles: Property = Property(name="cycles", type=IntegerType)
GraphMetaM_Vertex_globalPriority: Property = Property(name="globalPriority", type=IntegerType)
GraphMetaM_Vertex_activity: Property = Property(name="activity", type=StringType)
GraphMetaM_Vertex_rName: Property = Property(name="rName", type=StringType)
GraphMetaM_Vertex_type: Property = Property(name="type", type=StringType)
GraphMetaM_Vertex_name: Property = Property(name="name", type=StringType)
GraphMetaM_Vertex.attributes={GraphMetaM_Vertex_name, GraphMetaM_Vertex_globalPriority, GraphMetaM_Vertex_type, GraphMetaM_Vertex_rName, GraphMetaM_Vertex_activity, GraphMetaM_Vertex_cycles}

# GraphMetaM_Edge class attributes and methods
GraphMetaM_Edge_localPriority: Property = Property(name="localPriority", type=IntegerType)
GraphMetaM_Edge_rName: Property = Property(name="rName", type=StringType)
GraphMetaM_Edge_name: Property = Property(name="name", type=StringType)
GraphMetaM_Edge_async: Property = Property(name="async", type=BooleanType)
GraphMetaM_Edge.attributes={GraphMetaM_Edge_rName, GraphMetaM_Edge_name, GraphMetaM_Edge_async, GraphMetaM_Edge_localPriority}

# GraphMetaM_Model class attributes and methods
GraphMetaM_Model_name: Property = Property(name="name", type=StringType)
GraphMetaM_Model.attributes={GraphMetaM_Model_name}

# Relationships
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="Vertex", type=GraphMetaM_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=GraphMetaM_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="Vertex5", type=GraphMetaM_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=GraphMetaM_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
vertex0: BinaryAssociation = BinaryAssociation(
    name="vertex0",
    ends={
        Property(name="GraphMetaM_Vertex", type=GraphMetaM_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphMetaM_Graph", type=GraphMetaM_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge1: BinaryAssociation = BinaryAssociation(
    name="edge1",
    ends={
        Property(name="GraphMetaM_Edge", type=GraphMetaM_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphMetaM_Graph2", type=GraphMetaM_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Edge", type=GraphMetaM_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=GraphMetaM_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing7: BinaryAssociation = BinaryAssociation(
    name="outgoing7",
    ends={
        Property(name="Edge8", type=GraphMetaM_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=GraphMetaM_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
graph9: BinaryAssociation = BinaryAssociation(
    name="graph9",
    ends={
        Property(name="GraphMetaM_Graph10", type=GraphMetaM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphMetaM_Model", type=GraphMetaM_Graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="GraphMetaM",
    types={GraphMetaM_Graph, GraphMetaM_Vertex, GraphMetaM_Edge, GraphMetaM_Model, Type},
    associations={target3, source4, vertex0, edge1, incoming6, outgoing7, graph9},
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