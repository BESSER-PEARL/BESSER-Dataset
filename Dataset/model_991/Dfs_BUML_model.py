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
EdgeType: Enumeration = Enumeration(
    name="EdgeType",
    literals={
            EnumerationLiteral(name="TREE_EDGE"),
			EnumerationLiteral(name="BACKWARD_EDGE"),
			EnumerationLiteral(name="FORWARD_EDGE"),
			EnumerationLiteral(name="CROSS_EDGE")
    }
)

# Classes
dfs_EdgeProcessor = Class(name="dfs::EdgeProcessor", is_abstract=True)
dfs_EObject = Class(name="dfs::EObject")
dfs_DepthFirstSearch = Class(name="dfs::DepthFirstSearch")
EdgeProcessor = Class(name="EdgeProcessor")
dfs_Node = Class(name="dfs::Node")
dfs_Edge = Class(name="dfs::Edge")
dfs_DFSGraph = Class(name="dfs::DFSGraph")

# dfs_EdgeProcessor class attributes and methods
dfs_EdgeProcessor_m_processEdge: Method = Method(name="processEdge", parameters={Parameter(name='edge')}, type=StringType)
dfs_EdgeProcessor_m_processNode: Method = Method(name="processNode", parameters={Parameter(name='node')}, type=StringType)
dfs_EdgeProcessor.methods={dfs_EdgeProcessor_m_processNode, dfs_EdgeProcessor_m_processEdge}

# dfs_EObject class attributes and methods

# dfs_DepthFirstSearch class attributes and methods
dfs_DepthFirstSearch_postTraversalCounter: Property = Property(name="postTraversalCounter", type=IntegerType)
dfs_DepthFirstSearch_preTraversalCounter: Property = Property(name="preTraversalCounter", type=IntegerType)
dfs_DepthFirstSearch_m_incrementPostTraversalCounter: Method = Method(name="incrementPostTraversalCounter", parameters={}, type=IntegerType)
dfs_DepthFirstSearch_m_incrementPreTraversalCounter: Method = Method(name="incrementPreTraversalCounter", parameters={}, type=IntegerType)
dfs_DepthFirstSearch_m_processEdge: Method = Method(name="processEdge", parameters={Parameter(name='edge')}, type=StringType)
dfs_DepthFirstSearch_m_processNode: Method = Method(name="processNode", parameters={Parameter(name='node')}, type=StringType)
dfs_DepthFirstSearch.attributes={dfs_DepthFirstSearch_postTraversalCounter, dfs_DepthFirstSearch_preTraversalCounter}
dfs_DepthFirstSearch.methods={dfs_DepthFirstSearch_m_processEdge, dfs_DepthFirstSearch_m_processNode, dfs_DepthFirstSearch_m_incrementPreTraversalCounter, dfs_DepthFirstSearch_m_incrementPostTraversalCounter}

# EdgeProcessor class attributes and methods

# dfs_Node class attributes and methods
dfs_Node_postTraversal: Property = Property(name="postTraversal", type=IntegerType)
dfs_Node_preTraversal: Property = Property(name="preTraversal", type=IntegerType)
dfs_Node.attributes={dfs_Node_postTraversal, dfs_Node_preTraversal}

# dfs_Edge class attributes and methods
dfs_Edge_type: Property = Property(name="type", type=StringType)
dfs_Edge.attributes={dfs_Edge_type}

# dfs_DFSGraph class attributes and methods

# Relationships
graph3: BinaryAssociation = BinaryAssociation(
    name="graph3",
    ends={
        Property(name="nodes", type=dfs_DFSGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="DFSGraph", type=dfs_Node, multiplicity=Multiplicity(1, 1))
    }
)
origin4: BinaryAssociation = BinaryAssociation(
    name="origin4",
    ends={
        Property(name="dfs_EObject", type=dfs_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="dfs_Node", type=dfs_EObject, multiplicity=Multiplicity(1, 1))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Edge6", type=dfs_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=dfs_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
graph7: BinaryAssociation = BinaryAssociation(
    name="graph7",
    ends={
        Property(name="DFSGraph8", type=dfs_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=dfs_DFSGraph, multiplicity=Multiplicity(1, 1))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="Node", type=dfs_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=dfs_Node, multiplicity=Multiplicity(1, 1))
    }
)
origin10: BinaryAssociation = BinaryAssociation(
    name="origin10",
    ends={
        Property(name="dfs_EObject11", type=dfs_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="dfs_Edge", type=dfs_EObject, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="Node13", type=dfs_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=dfs_Node, multiplicity=Multiplicity(1, 1))
    }
)
edges14: BinaryAssociation = BinaryAssociation(
    name="edges14",
    ends={
        Property(name="Edge15", type=dfs_DFSGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=dfs_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delegate1: BinaryAssociation = BinaryAssociation(
    name="delegate1",
    ends={
        Property(name="dfs_EdgeProcessor", type=dfs_EdgeProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="dfs_EdgeProcessor0", type=dfs_EdgeProcessor, multiplicity=Multiplicity(0, 1))
    }
)
incoming2: BinaryAssociation = BinaryAssociation(
    name="incoming2",
    ends={
        Property(name="Edge", type=dfs_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=dfs_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
nodes16: BinaryAssociation = BinaryAssociation(
    name="nodes16",
    ends={
        Property(name="Node18", type=dfs_DFSGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph17", type=dfs_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dfs_DepthFirstSearch_EdgeProcessor = Generalization(general=EdgeProcessor, specific=dfs_DepthFirstSearch)

# Domain Model
domain_model = DomainModel(
    name="dfs",
    types={dfs_EdgeProcessor, dfs_EObject, dfs_DepthFirstSearch, EdgeProcessor, dfs_Node, dfs_Edge, dfs_DFSGraph, EdgeType},
    associations={graph3, origin4, outgoing5, graph7, source9, origin10, target12, edges14, delegate1, incoming2, nodes16},
    generalizations={gen_dfs_DepthFirstSearch_EdgeProcessor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)