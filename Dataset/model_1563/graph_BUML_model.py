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
graph_GraphElement = Class(name="graph::GraphElement", is_abstract=True)
graph_Vertex = Class(name="graph::Vertex")
graph_Edge = Class(name="graph::Edge")

# graph_Graph class attributes and methods
graph_Graph_name: Property = Property(name="name", type=StringType)
graph_Graph_description: Property = Property(name="description", type=StringType)
graph_Graph_m_addAdjacent: Method = Method(name="addAdjacent", parameters={Parameter(name='source_p'), Parameter(name='target_p'), Parameter(name='edgeContent_p')})
graph_Graph_m_addAdjacent: Method = Method(name="addAdjacent", parameters={Parameter(name='source_p'), Parameter(name='edgeContent_p'), Parameter(name='critical_p'), Parameter(name='target_p')})
graph_Graph_m_addNamedAdjacent: Method = Method(name="addNamedAdjacent", parameters={Parameter(name='edgeContent_p'), Parameter(name='edgeName_p'), Parameter(name='source_p'), Parameter(name='target_p'), Parameter(name='critical_p')})
graph_Graph_m_addNamedAdjacent: Method = Method(name="addNamedAdjacent", parameters={Parameter(name='edgeName'), Parameter(name='edgeContent'), Parameter(name='source'), Parameter(name='target')})
graph_Graph_m_addVertex: Method = Method(name="addVertex", parameters={Parameter(name='vertex_p')})
graph_Graph_m_addEdge: Method = Method(name="addEdge", parameters={Parameter(name='edge_p')})
graph_Graph.attributes={graph_Graph_description, graph_Graph_name}
graph_Graph.methods={graph_Graph_m_addAdjacent, graph_Graph_m_addVertex, graph_Graph_m_addNamedAdjacent, graph_Graph_m_addEdge, graph_Graph_m_addAdjacent, graph_Graph_m_addNamedAdjacent}

# graph_GraphElement class attributes and methods
graph_GraphElement_name: Property = Property(name="name", type=StringType)
graph_GraphElement.attributes={graph_GraphElement_name}

# graph_Vertex class attributes and methods
graph_Vertex_hotSpot: Property = Property(name="hotSpot", type=BooleanType)
graph_Vertex_m_hasForIncomingAdjacent: Method = Method(name="hasForIncomingAdjacent", parameters={Parameter(name='vertex_p')}, type=BooleanType)
graph_Vertex_m_getIncomingEdgeFrom: Method = Method(name="getIncomingEdgeFrom", parameters={Parameter(name='vertex_p')})
graph_Vertex_m_getOutgoingEdgeTo: Method = Method(name="getOutgoingEdgeTo", parameters={Parameter(name='vertex_p')})
graph_Vertex_m_hasForAdjacent: Method = Method(name="hasForAdjacent", parameters={Parameter(name='vertex_p')}, type=BooleanType)
graph_Vertex_m_hasForOutgoingAdjacent: Method = Method(name="hasForOutgoingAdjacent", parameters={Parameter(name='vertex_p')}, type=BooleanType)
graph_Vertex_m_getEdgeTo: Method = Method(name="getEdgeTo", parameters={Parameter(name='vertex_p')})
graph_Vertex.attributes={graph_Vertex_hotSpot}
graph_Vertex.methods={graph_Vertex_m_hasForOutgoingAdjacent, graph_Vertex_m_hasForIncomingAdjacent, graph_Vertex_m_getOutgoingEdgeTo, graph_Vertex_m_getEdgeTo, graph_Vertex_m_getIncomingEdgeFrom, graph_Vertex_m_hasForAdjacent}

# graph_Edge class attributes and methods
graph_Edge_critical: Property = Property(name="critical", type=BooleanType)
graph_Edge_m_update: Method = Method(name="update", parameters={Parameter(name='targetVertex_p'), Parameter(name='sourceVertex_p')})
graph_Edge_m_update: Method = Method(name="update", parameters={Parameter(name='sourceVertex_p'), Parameter(name='criticalEdge_p'), Parameter(name='edgeName_p'), Parameter(name='targetVertex_p')})
graph_Edge_m_update: Method = Method(name="update", parameters={Parameter(name='criticalEdge_p'), Parameter(name='sourceVertex_p'), Parameter(name='targetVertex_p'), Parameter(name='edgeName_p'), Parameter(name='edgeContent_p')})
graph_Edge_m_update: Method = Method(name="update", parameters={Parameter(name='sourceVertex_p'), Parameter(name='criticalEdge_p'), Parameter(name='targetVertex_p')})
graph_Edge.attributes={graph_Edge_critical}
graph_Edge.methods={graph_Edge_m_update, graph_Edge_m_update, graph_Edge_m_update, graph_Edge_m_update}

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Graph, graph_GraphElement, graph_Vertex, graph_Edge},
    associations={},
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