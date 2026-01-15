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
graphdom_Graph = Class(name="graphdom::Graph")
graphdom_Node = Class(name="graphdom::Node")
graphdom_Edge = Class(name="graphdom::Edge")

# graphdom_Graph class attributes and methods
graphdom_Graph_graphName: Property = Property(name="graphName", type=StringType)
graphdom_Graph_m_findNodeById: Method = Method(name="findNodeById", parameters={Parameter(name='id')}, type=StringType)
graphdom_Graph_m_unmarkAllNodes: Method = Method(name="unmarkAllNodes", parameters={})
graphdom_Graph_m_removeNode: Method = Method(name="removeNode", parameters={Parameter(name='node')})
graphdom_Graph_m_isDominated: Method = Method(name="isDominated", parameters={}, type=BooleanType)
graphdom_Graph_m_getDominatingSet: Method = Method(name="getDominatingSet", parameters={}, type=StringType)
graphdom_Graph_m_checkNodesDomination: Method = Method(name="checkNodesDomination", parameters={})
graphdom_Graph_m_isTotallyDominated: Method = Method(name="isTotallyDominated", parameters={}, type=BooleanType)
graphdom_Graph_m_isIndependentlyDominated: Method = Method(name="isIndependentlyDominated", parameters={}, type=BooleanType)
graphdom_Graph_m_isConnectedDomination: Method = Method(name="isConnectedDomination", parameters={}, type=BooleanType)
graphdom_Graph_m_getNextNodeId: Method = Method(name="getNextNodeId", parameters={}, type=IntegerType)
graphdom_Graph.attributes={graphdom_Graph_graphName}
graphdom_Graph.methods={graphdom_Graph_m_checkNodesDomination, graphdom_Graph_m_isIndependentlyDominated, graphdom_Graph_m_findNodeById, graphdom_Graph_m_getNextNodeId, graphdom_Graph_m_isTotallyDominated, graphdom_Graph_m_isConnectedDomination, graphdom_Graph_m_removeNode, graphdom_Graph_m_getDominatingSet, graphdom_Graph_m_isDominated, graphdom_Graph_m_unmarkAllNodes}

# graphdom_Node class attributes and methods
graphdom_Node_nodeName: Property = Property(name="nodeName", type=StringType)
graphdom_Node_color: Property = Property(name="color", type=StringType)
graphdom_Node_dominating: Property = Property(name="dominating", type=BooleanType)
graphdom_Node_grade: Property = Property(name="grade", type=StringType)
graphdom_Node_guid: Property = Property(name="guid", type=StringType)
graphdom_Node_xCoord: Property = Property(name="xCoord", type=IntegerType)
graphdom_Node_yCoord: Property = Property(name="yCoord", type=IntegerType)
graphdom_Node_dominated: Property = Property(name="dominated", type=BooleanType)
graphdom_Node_m_getAdjacentNodes: Method = Method(name="getAdjacentNodes", parameters={}, type=StringType)
graphdom_Node.attributes={graphdom_Node_dominated, graphdom_Node_grade, graphdom_Node_nodeName, graphdom_Node_dominating, graphdom_Node_xCoord, graphdom_Node_guid, graphdom_Node_yCoord, graphdom_Node_color}
graphdom_Node.methods={graphdom_Node_m_getAdjacentNodes}

# graphdom_Edge class attributes and methods
graphdom_Edge_guid: Property = Property(name="guid", type=StringType)
graphdom_Edge_weight: Property = Property(name="weight", type=IntegerType)
graphdom_Edge_marked: Property = Property(name="marked", type=BooleanType)
graphdom_Edge_m_flip: Method = Method(name="flip", parameters={}, type=BooleanType)
graphdom_Edge.attributes={graphdom_Edge_marked, graphdom_Edge_weight, graphdom_Edge_guid}
graphdom_Edge.methods={graphdom_Edge_m_flip}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graphdom_Node", type=graphdom_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphdom_Graph", type=graphdom_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="graphdom_Edge", type=graphdom_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphdom_Graph2", type=graphdom_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedEdges3: BinaryAssociation = BinaryAssociation(
    name="connectedEdges3",
    ends={
        Property(name="Edge", type=graphdom_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="connectedNodes", type=graphdom_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
connectedNodes4: BinaryAssociation = BinaryAssociation(
    name="connectedNodes4",
    ends={
        Property(name="Node", type=graphdom_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="connectedEdges", type=graphdom_Node, multiplicity=Multiplicity(2, 2))
    }
)

# Domain Model
domain_model = DomainModel(
    name="graphdom",
    types={graphdom_Graph, graphdom_Node, graphdom_Edge},
    associations={nodes0, edges1, connectedEdges3, connectedNodes4},
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