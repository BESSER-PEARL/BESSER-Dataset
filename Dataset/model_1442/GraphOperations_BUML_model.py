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
EdgeState: Enumeration = Enumeration(
    name="EdgeState",
    literals={
            EnumerationLiteral(name="ACTIVE"),
			EnumerationLiteral(name="INACTIVE")
    }
)

# Classes
GraphOperations_Node = Class(name="GraphOperations_Node")
GraphOperations_Graph = Class(name="GraphOperations_Graph")
GraphOperations_Element = Class(name="GraphOperations_Element")
GraphOperations_Triangle = Class(name="GraphOperations_Triangle")
GraphOperations_Edge = Class(name="GraphOperations_Edge")
Element = Class(name="Element")
GraphOperations_ConstantUtils = Class(name="GraphOperations_ConstantUtils")
GraphOperations_EIntContainer = Class(name="GraphOperations_EIntContainer")

# GraphOperations_Node class attributes and methods
GraphOperations_Node_depth: Property = Property(name="depth", type=IntegerType)
GraphOperations_Node_degree: Property = Property(name="degree", type=FloatType)
GraphOperations_Node_m_calculateDegree: Method = Method(name="calculateDegree", parameters={}, type=IntegerType)
GraphOperations_Node_m_assignIdCAC: Method = Method(name="assignIdCAC", parameters={})
GraphOperations_Node.attributes={GraphOperations_Node_depth, GraphOperations_Node_degree}
GraphOperations_Node.methods={GraphOperations_Node_m_assignIdCAC, GraphOperations_Node_m_calculateDegree}

# GraphOperations_Graph class attributes and methods
GraphOperations_Graph_m_removeEdge: Method = Method(name="removeEdge", parameters={Parameter(name='GraphOperations_edgeId', type=StringType)})
GraphOperations_Graph_m_clear: Method = Method(name="clear", parameters={})
GraphOperations_Graph_m_calculateNodeCount: Method = Method(name="calculateNodeCount", parameters={}, type=IntegerType)
GraphOperations_Graph_m_isNode: Method = Method(name="isNode", parameters={Parameter(name='GraphOperations_element', type=StringType)}, type=BooleanType)
GraphOperations_Graph_m_getIsolatedNode: Method = Method(name="getIsolatedNode", parameters={}, type=StringType)
GraphOperations_Graph_m_getTriangleWithLongestEdge: Method = Method(name="getTriangleWithLongestEdge", parameters={}, type=StringType)
GraphOperations_Graph_m_addNode: Method = Method(name="addNode", parameters={Parameter(name='GraphOperations_nodeId', type=StringType)}, type=StringType)
GraphOperations_Graph_m_getSomeNode: Method = Method(name="getSomeNode", parameters={}, type=StringType)
GraphOperations_Graph_m_addGivenNode: Method = Method(name="addGivenNode", parameters={Parameter(name='GraphOperations_node', type=StringType)})
GraphOperations_Graph_m_emptyOperation: Method = Method(name="emptyOperation", parameters={})
GraphOperations_Graph_m_calculateDoubleNodeCount: Method = Method(name="calculateDoubleNodeCount", parameters={}, type=IntegerType)
GraphOperations_Graph_m_getNodeWithId_CAC: Method = Method(name="getNodeWithId_CAC", parameters={}, type=StringType)
GraphOperations_Graph_m_addNodeWithFixedId: Method = Method(name="addNodeWithFixedId", parameters={}, type=StringType)
GraphOperations_Graph_m_addEdgeWithIncidentNodes: Method = Method(name="addEdgeWithIncidentNodes", parameters={Parameter(name='GraphOperations_edgeId', type=StringType), Parameter(name='GraphOperations_trgId', type=StringType), Parameter(name='GraphOperations_srcId', type=StringType)}, type=StringType)
GraphOperations_Graph.methods={GraphOperations_Graph_m_emptyOperation, GraphOperations_Graph_m_addNode, GraphOperations_Graph_m_getSomeNode, GraphOperations_Graph_m_addEdgeWithIncidentNodes, GraphOperations_Graph_m_getTriangleWithLongestEdge, GraphOperations_Graph_m_addGivenNode, GraphOperations_Graph_m_calculateNodeCount, GraphOperations_Graph_m_removeEdge, GraphOperations_Graph_m_clear, GraphOperations_Graph_m_calculateDoubleNodeCount, GraphOperations_Graph_m_getNodeWithId_CAC, GraphOperations_Graph_m_isNode, GraphOperations_Graph_m_addNodeWithFixedId, GraphOperations_Graph_m_getIsolatedNode}

# GraphOperations_Element class attributes and methods
GraphOperations_Element_id: Property = Property(name="id", type=StringType)
GraphOperations_Element.attributes={GraphOperations_Element_id}

# GraphOperations_Triangle class attributes and methods

# GraphOperations_Edge class attributes and methods
GraphOperations_Edge_state: Property = Property(name="state", type=StringType)
GraphOperations_Edge_weight: Property = Property(name="weight", type=FloatType)
GraphOperations_Edge.attributes={GraphOperations_Edge_weight, GraphOperations_Edge_state}

# Element class attributes and methods

# GraphOperations_ConstantUtils class attributes and methods
GraphOperations_ConstantUtils_m_getFloat: Method = Method(name="getFloat", parameters={}, type=FloatType)
GraphOperations_ConstantUtils_m_getString: Method = Method(name="getString", parameters={}, type=StringType)
GraphOperations_ConstantUtils_m_getInt: Method = Method(name="getInt", parameters={}, type=IntegerType)
GraphOperations_ConstantUtils_m_getDouble: Method = Method(name="getDouble", parameters={}, type=FloatType)
GraphOperations_ConstantUtils_m_getLong: Method = Method(name="getLong", parameters={}, type=StringType)
GraphOperations_ConstantUtils_m_getEdgeState: Method = Method(name="getEdgeState", parameters={}, type=StringType)
GraphOperations_ConstantUtils.methods={GraphOperations_ConstantUtils_m_getFloat, GraphOperations_ConstantUtils_m_getDouble, GraphOperations_ConstantUtils_m_getString, GraphOperations_ConstantUtils_m_getInt, GraphOperations_ConstantUtils_m_getLong, GraphOperations_ConstantUtils_m_getEdgeState}

# GraphOperations_EIntContainer class attributes and methods
GraphOperations_EIntContainer_value: Property = Property(name="value", type=IntegerType)
GraphOperations_EIntContainer_m_increment: Method = Method(name="increment", parameters={}, type=IntegerType)
GraphOperations_EIntContainer_m_incrementBy: Method = Method(name="incrementBy", parameters={Parameter(name='GraphOperations_value', type=StringType)}, type=IntegerType)
GraphOperations_EIntContainer.attributes={GraphOperations_EIntContainer_value}
GraphOperations_EIntContainer.methods={GraphOperations_EIntContainer_m_incrementBy, GraphOperations_EIntContainer_m_increment}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=GraphOperations_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=GraphOperations_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingEdges6: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges6",
    ends={
        Property(name="Edge7", type=GraphOperations_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=GraphOperations_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
graph8: BinaryAssociation = BinaryAssociation(
    name="graph8",
    ends={
        Property(name="Graph9", type=GraphOperations_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=GraphOperations_Graph, multiplicity=Multiplicity(1, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="Node11", type=GraphOperations_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=GraphOperations_Node, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="Node13", type=GraphOperations_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=GraphOperations_Node, multiplicity=Multiplicity(1, 1))
    }
)
longEdge14: BinaryAssociation = BinaryAssociation(
    name="longEdge14",
    ends={
        Property(name="GraphOperations_Edge", type=GraphOperations_Triangle, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphOperations_Triangle", type=GraphOperations_Edge, multiplicity=Multiplicity(0, 1))
    }
)
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="Edge", type=GraphOperations_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph2", type=GraphOperations_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph3: BinaryAssociation = BinaryAssociation(
    name="graph3",
    ends={
        Property(name="Graph", type=GraphOperations_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=GraphOperations_Graph, multiplicity=Multiplicity(1, 1))
    }
)
incomingEdges4: BinaryAssociation = BinaryAssociation(
    name="incomingEdges4",
    ends={
        Property(name="Edge5", type=GraphOperations_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=GraphOperations_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
shortEdges15: BinaryAssociation = BinaryAssociation(
    name="shortEdges15",
    ends={
        Property(name="GraphOperations_Edge17", type=GraphOperations_Triangle, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphOperations_Triangle16", type=GraphOperations_Edge, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_GraphOperations_Edge_Element = Generalization(general=Element, specific=GraphOperations_Edge)
gen_GraphOperations_Node_Element = Generalization(general=Element, specific=GraphOperations_Node)

# Domain Model
domain_model = DomainModel(
    name="GraphOperations",
    types={GraphOperations_Node, GraphOperations_Graph, GraphOperations_Element, GraphOperations_Triangle, GraphOperations_Edge, Element, GraphOperations_ConstantUtils, GraphOperations_EIntContainer, EdgeState},
    associations={nodes0, outgoingEdges6, graph8, source10, target12, longEdge14, edges1, graph3, incomingEdges4, shortEdges15},
    generalizations={gen_GraphOperations_Edge_Element, gen_GraphOperations_Node_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)