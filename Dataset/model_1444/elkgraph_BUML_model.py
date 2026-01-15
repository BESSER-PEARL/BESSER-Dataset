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
graph_IPropertyHolder = Class(name="graph::IPropertyHolder", is_abstract=True)
graph_EMapPropertyHolder = Class(name="graph::EMapPropertyHolder", is_abstract=True)
IPropertyHolder = Class(name="IPropertyHolder")
graph_ElkGraphElement = Class(name="graph::ElkGraphElement", is_abstract=True)
EMapPropertyHolder = Class(name="EMapPropertyHolder")
graph_ElkLabel = Class(name="graph::ElkLabel")
graph_ElkPropertyToValueMapEntry = Class(name="graph::ElkPropertyToValueMapEntry")
graph_ElkShape = Class(name="graph::ElkShape", is_abstract=True)
ElkGraphElement = Class(name="ElkGraphElement")
ElkShape = Class(name="ElkShape")
graph_ElkEdge = Class(name="graph::ElkEdge")
graph_ElkNode = Class(name="graph::ElkNode")
ElkConnectableShape = Class(name="ElkConnectableShape")
graph_ElkPort = Class(name="graph::ElkPort")
graph_ElkConnectableShape = Class(name="graph::ElkConnectableShape", is_abstract=True)
graph_ElkEdgeSection = Class(name="graph::ElkEdgeSection")
graph_ElkBendPoint = Class(name="graph::ElkBendPoint")

# graph_IPropertyHolder class attributes and methods
graph_IPropertyHolder_m_setProperty: Method = Method(name="setProperty", parameters={Parameter(name='value'), Parameter(name='property')}, type=StringType)
graph_IPropertyHolder_m_hasProperty: Method = Method(name="hasProperty", parameters={Parameter(name='property')}, type=BooleanType)
graph_IPropertyHolder_m_copyProperties: Method = Method(name="copyProperties", parameters={Parameter(name='source')}, type=StringType)
graph_IPropertyHolder_m_getAllProperties: Method = Method(name="getAllProperties", parameters={})
graph_IPropertyHolder_m_getProperty: Method = Method(name="getProperty", parameters={Parameter(name='property')})
graph_IPropertyHolder.methods={graph_IPropertyHolder_m_copyProperties, graph_IPropertyHolder_m_getProperty, graph_IPropertyHolder_m_setProperty, graph_IPropertyHolder_m_getAllProperties, graph_IPropertyHolder_m_hasProperty}

# graph_EMapPropertyHolder class attributes and methods

# IPropertyHolder class attributes and methods

# graph_ElkGraphElement class attributes and methods
graph_ElkGraphElement_identifier: Property = Property(name="identifier", type=StringType)
graph_ElkGraphElement.attributes={graph_ElkGraphElement_identifier}

# EMapPropertyHolder class attributes and methods

# graph_ElkLabel class attributes and methods
graph_ElkLabel_text: Property = Property(name="text", type=StringType)
graph_ElkLabel.attributes={graph_ElkLabel_text}

# graph_ElkPropertyToValueMapEntry class attributes and methods
graph_ElkPropertyToValueMapEntry_value: Property = Property(name="value", type=StringType)
graph_ElkPropertyToValueMapEntry_key: Property = Property(name="key", type=StringType)
graph_ElkPropertyToValueMapEntry.attributes={graph_ElkPropertyToValueMapEntry_value, graph_ElkPropertyToValueMapEntry_key}

# graph_ElkShape class attributes and methods
graph_ElkShape_height: Property = Property(name="height", type=FloatType)
graph_ElkShape_width: Property = Property(name="width", type=FloatType)
graph_ElkShape_y: Property = Property(name="y", type=FloatType)
graph_ElkShape_x: Property = Property(name="x", type=FloatType)
graph_ElkShape_m_setDimensions: Method = Method(name="setDimensions", parameters={Parameter(name='height'), Parameter(name='width')})
graph_ElkShape_m_setLocation: Method = Method(name="setLocation", parameters={Parameter(name='y'), Parameter(name='x')})
graph_ElkShape.attributes={graph_ElkShape_height, graph_ElkShape_x, graph_ElkShape_y, graph_ElkShape_width}
graph_ElkShape.methods={graph_ElkShape_m_setLocation, graph_ElkShape_m_setDimensions}

# ElkGraphElement class attributes and methods

# ElkShape class attributes and methods

# graph_ElkEdge class attributes and methods
graph_ElkEdge_hyperedge: Property = Property(name="hyperedge", type=BooleanType)
graph_ElkEdge_hierarchical: Property = Property(name="hierarchical", type=BooleanType)
graph_ElkEdge_selfloop: Property = Property(name="selfloop", type=BooleanType)
graph_ElkEdge_connected: Property = Property(name="connected", type=BooleanType)
graph_ElkEdge.attributes={graph_ElkEdge_connected, graph_ElkEdge_hierarchical, graph_ElkEdge_selfloop, graph_ElkEdge_hyperedge}

# graph_ElkNode class attributes and methods
graph_ElkNode_hierarchical: Property = Property(name="hierarchical", type=BooleanType)
graph_ElkNode.attributes={graph_ElkNode_hierarchical}

# ElkConnectableShape class attributes and methods

# graph_ElkPort class attributes and methods

# graph_ElkConnectableShape class attributes and methods

# graph_ElkEdgeSection class attributes and methods
graph_ElkEdgeSection_startX: Property = Property(name="startX", type=FloatType)
graph_ElkEdgeSection_startY: Property = Property(name="startY", type=FloatType)
graph_ElkEdgeSection_endX: Property = Property(name="endX", type=FloatType)
graph_ElkEdgeSection_endY: Property = Property(name="endY", type=FloatType)
graph_ElkEdgeSection_identifier: Property = Property(name="identifier", type=StringType)
graph_ElkEdgeSection_m_setStartLocation: Method = Method(name="setStartLocation", parameters={Parameter(name='y'), Parameter(name='x')})
graph_ElkEdgeSection_m_setEndLocation: Method = Method(name="setEndLocation", parameters={Parameter(name='y'), Parameter(name='x')})
graph_ElkEdgeSection.attributes={graph_ElkEdgeSection_endY, graph_ElkEdgeSection_startY, graph_ElkEdgeSection_identifier, graph_ElkEdgeSection_startX, graph_ElkEdgeSection_endX}
graph_ElkEdgeSection.methods={graph_ElkEdgeSection_m_setStartLocation, graph_ElkEdgeSection_m_setEndLocation}

# graph_ElkBendPoint class attributes and methods
graph_ElkBendPoint_x: Property = Property(name="x", type=FloatType)
graph_ElkBendPoint_y: Property = Property(name="y", type=FloatType)
graph_ElkBendPoint_m_set: Method = Method(name="set", parameters={Parameter(name='y'), Parameter(name='x')})
graph_ElkBendPoint.attributes={graph_ElkBendPoint_y, graph_ElkBendPoint_x}
graph_ElkBendPoint.methods={graph_ElkBendPoint_m_set}

# Relationships
labels1: BinaryAssociation = BinaryAssociation(
    name="labels1",
    ends={
        Property(name="ElkLabel", type=graph_ElkGraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=graph_ElkLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="graph_ElkPropertyToValueMapEntry", type=graph_EMapPropertyHolder, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_EMapPropertyHolder", type=graph_ElkPropertyToValueMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingEdges3: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges3",
    ends={
        Property(name="ElkEdge", type=graph_ElkConnectableShape, multiplicity=Multiplicity(1, 1)),
        Property(name="sources", type=graph_ElkEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incomingEdges4: BinaryAssociation = BinaryAssociation(
    name="incomingEdges4",
    ends={
        Property(name="ElkEdge5", type=graph_ElkConnectableShape, multiplicity=Multiplicity(1, 1)),
        Property(name="targets", type=graph_ElkEdge, multiplicity=Multiplicity(0, 9999))
    }
)
ports6: BinaryAssociation = BinaryAssociation(
    name="ports6",
    ends={
        Property(name="ElkPort", type=graph_ElkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent7", type=graph_ElkPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children9: BinaryAssociation = BinaryAssociation(
    name="children9",
    ends={
        Property(name="ElkNode", type=graph_ElkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent10", type=graph_ElkNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent12: BinaryAssociation = BinaryAssociation(
    name="parent12",
    ends={
        Property(name="ElkNode13", type=graph_ElkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=graph_ElkNode, multiplicity=Multiplicity(0, 1))
    }
)
containedEdges14: BinaryAssociation = BinaryAssociation(
    name="containedEdges14",
    ends={
        Property(name="ElkEdge15", type=graph_ElkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="containingNode", type=graph_ElkEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent2: BinaryAssociation = BinaryAssociation(
    name="parent2",
    ends={
        Property(name="ElkGraphElement", type=graph_ElkLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=graph_ElkGraphElement, multiplicity=Multiplicity(0, 1))
    }
)
parent16: BinaryAssociation = BinaryAssociation(
    name="parent16",
    ends={
        Property(name="ElkNode17", type=graph_ElkPort, multiplicity=Multiplicity(1, 1)),
        Property(name="ports", type=graph_ElkNode, multiplicity=Multiplicity(0, 1))
    }
)
sources20: BinaryAssociation = BinaryAssociation(
    name="sources20",
    ends={
        Property(name="ElkConnectableShape", type=graph_ElkEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=graph_ElkConnectableShape, multiplicity=Multiplicity(0, 9999))
    }
)
targets21: BinaryAssociation = BinaryAssociation(
    name="targets21",
    ends={
        Property(name="ElkConnectableShape22", type=graph_ElkEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=graph_ElkConnectableShape, multiplicity=Multiplicity(0, 9999))
    }
)
sections23: BinaryAssociation = BinaryAssociation(
    name="sections23",
    ends={
        Property(name="ElkEdgeSection", type=graph_ElkEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="parent24", type=graph_ElkEdgeSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containingNode18: BinaryAssociation = BinaryAssociation(
    name="containingNode18",
    ends={
        Property(name="ElkNode19", type=graph_ElkEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="containedEdges", type=graph_ElkNode, multiplicity=Multiplicity(0, 1))
    }
)
bendPoints25: BinaryAssociation = BinaryAssociation(
    name="bendPoints25",
    ends={
        Property(name="graph_ElkBendPoint", type=graph_ElkEdgeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_ElkEdgeSection", type=graph_ElkBendPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent26: BinaryAssociation = BinaryAssociation(
    name="parent26",
    ends={
        Property(name="ElkEdge27", type=graph_ElkEdgeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="sections", type=graph_ElkEdge, multiplicity=Multiplicity(0, 1))
    }
)
outgoingShape28: BinaryAssociation = BinaryAssociation(
    name="outgoingShape28",
    ends={
        Property(name="graph_ElkConnectableShape", type=graph_ElkEdgeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_ElkEdgeSection29", type=graph_ElkConnectableShape, multiplicity=Multiplicity(0, 1))
    }
)
incomingShape30: BinaryAssociation = BinaryAssociation(
    name="incomingShape30",
    ends={
        Property(name="graph_ElkConnectableShape32", type=graph_ElkEdgeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_ElkEdgeSection31", type=graph_ElkConnectableShape, multiplicity=Multiplicity(0, 1))
    }
)
outgoingSections34: BinaryAssociation = BinaryAssociation(
    name="outgoingSections34",
    ends={
        Property(name="ElkEdgeSection35", type=graph_ElkEdgeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingSections", type=graph_ElkEdgeSection, multiplicity=Multiplicity(0, 9999))
    }
)
incomingSections37: BinaryAssociation = BinaryAssociation(
    name="incomingSections37",
    ends={
        Property(name="ElkEdgeSection38", type=graph_ElkEdgeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingSections", type=graph_ElkEdgeSection, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_graph_EMapPropertyHolder_IPropertyHolder = Generalization(general=IPropertyHolder, specific=graph_EMapPropertyHolder)
gen_graph_ElkGraphElement_EMapPropertyHolder = Generalization(general=EMapPropertyHolder, specific=graph_ElkGraphElement)
gen_graph_ElkShape_ElkGraphElement = Generalization(general=ElkGraphElement, specific=graph_ElkShape)
gen_graph_ElkLabel_ElkShape = Generalization(general=ElkShape, specific=graph_ElkLabel)
gen_graph_ElkNode_ElkConnectableShape = Generalization(general=ElkConnectableShape, specific=graph_ElkNode)
gen_graph_ElkPort_ElkConnectableShape = Generalization(general=ElkConnectableShape, specific=graph_ElkPort)
gen_graph_ElkConnectableShape_ElkShape = Generalization(general=ElkShape, specific=graph_ElkConnectableShape)
gen_graph_ElkEdge_ElkGraphElement = Generalization(general=ElkGraphElement, specific=graph_ElkEdge)
gen_graph_ElkEdgeSection_EMapPropertyHolder = Generalization(general=EMapPropertyHolder, specific=graph_ElkEdgeSection)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_IPropertyHolder, graph_EMapPropertyHolder, IPropertyHolder, graph_ElkGraphElement, EMapPropertyHolder, graph_ElkLabel, graph_ElkPropertyToValueMapEntry, graph_ElkShape, ElkGraphElement, ElkShape, graph_ElkEdge, graph_ElkNode, ElkConnectableShape, graph_ElkPort, graph_ElkConnectableShape, graph_ElkEdgeSection, graph_ElkBendPoint},
    associations={labels1, properties0, outgoingEdges3, incomingEdges4, ports6, children9, parent12, containedEdges14, parent2, parent16, sources20, targets21, sections23, containingNode18, bendPoints25, parent26, outgoingShape28, incomingShape30, outgoingSections34, incomingSections37},
    generalizations={gen_graph_EMapPropertyHolder_IPropertyHolder, gen_graph_ElkGraphElement_EMapPropertyHolder, gen_graph_ElkShape_ElkGraphElement, gen_graph_ElkLabel_ElkShape, gen_graph_ElkNode_ElkConnectableShape, gen_graph_ElkPort_ElkConnectableShape, gen_graph_ElkConnectableShape_ElkShape, gen_graph_ElkEdge_ElkGraphElement, gen_graph_ElkEdgeSection_EMapPropertyHolder},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)