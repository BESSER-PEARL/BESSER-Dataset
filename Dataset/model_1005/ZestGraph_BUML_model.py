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
ZestGraph_NamedElement = Class(name="ZestGraph::NamedElement")
ZestGraph_ZestGraph = Class(name="ZestGraph::ZestGraph")
NamedElement = Class(name="NamedElement")
ZestGraph_GraphItem = Class(name="ZestGraph::GraphItem", is_abstract=True)
ZestGraph_GraphContainer = Class(name="ZestGraph::GraphContainer")
GraphItem = Class(name="GraphItem")
ZestGraph_GraphConnection = Class(name="ZestGraph::GraphConnection")
ZestGraph_GraphNode = Class(name="ZestGraph::GraphNode")

# ZestGraph_NamedElement class attributes and methods
ZestGraph_NamedElement_name: Property = Property(name="name", type=StringType)
ZestGraph_NamedElement.attributes={ZestGraph_NamedElement_name}

# ZestGraph_ZestGraph class attributes and methods

# NamedElement class attributes and methods

# ZestGraph_GraphItem class attributes and methods
ZestGraph_GraphItem_text: Property = Property(name="text", type=StringType)
ZestGraph_GraphItem.attributes={ZestGraph_GraphItem_text}

# ZestGraph_GraphContainer class attributes and methods

# GraphItem class attributes and methods

# ZestGraph_GraphConnection class attributes and methods
ZestGraph_GraphConnection_color: Property = Property(name="color", type=StringType)
ZestGraph_GraphConnection_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
ZestGraph_GraphConnection_lineStyle: Property = Property(name="lineStyle", type=IntegerType)
ZestGraph_GraphConnection.attributes={ZestGraph_GraphConnection_lineStyle, ZestGraph_GraphConnection_color, ZestGraph_GraphConnection_lineWidth}

# ZestGraph_GraphNode class attributes and methods
ZestGraph_GraphNode_shape: Property = Property(name="shape", type=StringType)
ZestGraph_GraphNode_nodeStyle: Property = Property(name="nodeStyle", type=StringType)
ZestGraph_GraphNode_backColor: Property = Property(name="backColor", type=StringType)
ZestGraph_GraphNode_width: Property = Property(name="width", type=FloatType)
ZestGraph_GraphNode_height: Property = Property(name="height", type=FloatType)
ZestGraph_GraphNode.attributes={ZestGraph_GraphNode_width, ZestGraph_GraphNode_shape, ZestGraph_GraphNode_backColor, ZestGraph_GraphNode_height, ZestGraph_GraphNode_nodeStyle}

# Relationships
items0: BinaryAssociation = BinaryAssociation(
    name="items0",
    ends={
        Property(name="GraphItem", type=ZestGraph_ZestGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=ZestGraph_GraphItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containers1: BinaryAssociation = BinaryAssociation(
    name="containers1",
    ends={
        Property(name="ZestGraph_GraphContainer", type=ZestGraph_ZestGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="ZestGraph_ZestGraph", type=ZestGraph_GraphContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="GraphConnection", type=ZestGraph_GraphNode, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceNode", type=ZestGraph_GraphConnection, multiplicity=Multiplicity(0, 9999))
    }
)
ingoing6: BinaryAssociation = BinaryAssociation(
    name="ingoing6",
    ends={
        Property(name="GraphConnection7", type=ZestGraph_GraphNode, multiplicity=Multiplicity(1, 1)),
        Property(name="targetNode", type=ZestGraph_GraphConnection, multiplicity=Multiplicity(0, 9999))
    }
)
sourceNode8: BinaryAssociation = BinaryAssociation(
    name="sourceNode8",
    ends={
        Property(name="GraphNode", type=ZestGraph_GraphConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=ZestGraph_GraphNode, multiplicity=Multiplicity(0, 1))
    }
)
targetNode9: BinaryAssociation = BinaryAssociation(
    name="targetNode9",
    ends={
        Property(name="GraphNode10", type=ZestGraph_GraphConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="ingoing", type=ZestGraph_GraphNode, multiplicity=Multiplicity(0, 1))
    }
)
nodes2: BinaryAssociation = BinaryAssociation(
    name="nodes2",
    ends={
        Property(name="ZestGraph_GraphNode", type=ZestGraph_GraphContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ZestGraph_GraphContainer3", type=ZestGraph_GraphNode, multiplicity=Multiplicity(0, 9999))
    }
)
graph4: BinaryAssociation = BinaryAssociation(
    name="graph4",
    ends={
        Property(name="ZestGraph", type=ZestGraph_GraphItem, multiplicity=Multiplicity(1, 1)),
        Property(name="items", type=ZestGraph_ZestGraph, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ZestGraph_ZestGraph_NamedElement = Generalization(general=NamedElement, specific=ZestGraph_ZestGraph)
gen_ZestGraph_GraphNode_GraphItem = Generalization(general=GraphItem, specific=ZestGraph_GraphNode)
gen_ZestGraph_GraphConnection_GraphItem = Generalization(general=GraphItem, specific=ZestGraph_GraphConnection)
gen_ZestGraph_GraphContainer_NamedElement = Generalization(general=NamedElement, specific=ZestGraph_GraphContainer)

# Domain Model
domain_model = DomainModel(
    name="ZestGraph",
    types={ZestGraph_NamedElement, ZestGraph_ZestGraph, NamedElement, ZestGraph_GraphItem, ZestGraph_GraphContainer, GraphItem, ZestGraph_GraphConnection, ZestGraph_GraphNode},
    associations={items0, containers1, outgoing5, ingoing6, sourceNode8, targetNode9, nodes2, graph4},
    generalizations={gen_ZestGraph_ZestGraph_NamedElement, gen_ZestGraph_GraphNode_GraphItem, gen_ZestGraph_GraphConnection_GraphItem, gen_ZestGraph_GraphContainer_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)