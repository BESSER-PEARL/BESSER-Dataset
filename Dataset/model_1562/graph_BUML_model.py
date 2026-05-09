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
graph_LabelValue = Class(name="graph_LabelValue", is_abstract=True)
graph_Decorator = Class(name="graph_Decorator")
graph_DynamicNodeLabel = Class(name="graph_DynamicNodeLabel", is_abstract=True)
DynamicLabel = Class(name="DynamicLabel")
NodeLabel = Class(name="NodeLabel")
graph_Edge = Class(name="graph_Edge")
Identifiable = Class(name="Identifiable")
Modifiable = Class(name="Modifiable")
graph_Node = Class(name="graph_Node")
graph_EdgeLabel = Class(name="graph_EdgeLabel", is_abstract=True)
graph_DynamicLabel = Class(name="graph_DynamicLabel", is_abstract=True)
Label = Class(name="Label")
graph_URIToEdgeMapEntry = Class(name="graph_URIToEdgeMapEntry")
graph_URIToNodeMapEntry = Class(name="graph_URIToNodeMapEntry")
graph_URIToLabelMapEntry = Class(name="graph_URIToLabelMapEntry")
graph_URIToNodeLabelMapEntry = Class(name="graph_URIToNodeLabelMapEntry")
graph_Graph = Class(name="graph_Graph")
graph_Identifiable = Class(name="graph_Identifiable")
SanityChecker = Class(name="SanityChecker")
graph_NodeLabel = Class(name="graph_NodeLabel", is_abstract=True)
graph_StaticNodeLabel = Class(name="graph_StaticNodeLabel", is_abstract=True)
StaticLabel = Class(name="StaticLabel")
graph_URIToIdentifiableMapEntry = Class(name="graph_URIToIdentifiableMapEntry")
graph_UnresolvedIdentifiable = Class(name="graph_UnresolvedIdentifiable")
graph_STEMTime = Class(name="graph_STEMTime")
graph_Label = Class(name="graph_Label", is_abstract=True)
graph_StaticLabel = Class(name="graph_StaticLabel", is_abstract=True)
graph_SanityChecker = Class(name="graph_SanityChecker", is_abstract=True)
graph_DynamicEdgeLabel = Class(name="graph_DynamicEdgeLabel", is_abstract=True)
EdgeLabel = Class(name="EdgeLabel")
graph_StaticEdgeLabel = Class(name="graph_StaticEdgeLabel", is_abstract=True)

# graph_LabelValue class attributes and methods
graph_LabelValue_m_reset: Method = Method(name="reset", parameters={})
graph_LabelValue.methods={graph_LabelValue_m_reset}

# graph_Decorator class attributes and methods

# graph_DynamicNodeLabel class attributes and methods

# DynamicLabel class attributes and methods

# NodeLabel class attributes and methods

# graph_Edge class attributes and methods
graph_Edge_nodeAURI: Property = Property(name="nodeAURI", type=StringType)
graph_Edge_nodeBURI: Property = Property(name="nodeBURI", type=StringType)
graph_Edge_directed: Property = Property(name="directed", type=BooleanType)
graph_Edge_m_getOtherNode: Method = Method(name="getOtherNode", parameters={Parameter(name='graph_node', type=StringType)}, type=StringType)
graph_Edge_m_isDirectedAt: Method = Method(name="isDirectedAt", parameters={Parameter(name='graph_node', type=StringType)}, type=BooleanType)
graph_Edge.attributes={graph_Edge_nodeAURI, graph_Edge_directed, graph_Edge_nodeBURI}
graph_Edge.methods={graph_Edge_m_isDirectedAt, graph_Edge_m_getOtherNode}

# Identifiable class attributes and methods

# Modifiable class attributes and methods

# graph_Node class attributes and methods

# graph_EdgeLabel class attributes and methods

# graph_DynamicLabel class attributes and methods
graph_DynamicLabel_nextValueValid: Property = Property(name="nextValueValid", type=BooleanType)
graph_DynamicLabel_m_reset: Method = Method(name="reset", parameters={})
graph_DynamicLabel_m_switchToNextValue: Method = Method(name="switchToNextValue", parameters={})
graph_DynamicLabel.attributes={graph_DynamicLabel_nextValueValid}
graph_DynamicLabel.methods={graph_DynamicLabel_m_reset, graph_DynamicLabel_m_switchToNextValue}

# Label class attributes and methods

# graph_URIToEdgeMapEntry class attributes and methods
graph_URIToEdgeMapEntry_key: Property = Property(name="key", type=StringType)
graph_URIToEdgeMapEntry.attributes={graph_URIToEdgeMapEntry_key}

# graph_URIToNodeMapEntry class attributes and methods
graph_URIToNodeMapEntry_key: Property = Property(name="key", type=StringType)
graph_URIToNodeMapEntry.attributes={graph_URIToNodeMapEntry_key}

# graph_URIToLabelMapEntry class attributes and methods
graph_URIToLabelMapEntry_key: Property = Property(name="key", type=StringType)
graph_URIToLabelMapEntry.attributes={graph_URIToLabelMapEntry_key}

# graph_URIToNodeLabelMapEntry class attributes and methods
graph_URIToNodeLabelMapEntry_key: Property = Property(name="key", type=StringType)
graph_URIToNodeLabelMapEntry.attributes={graph_URIToNodeLabelMapEntry_key}

# graph_Graph class attributes and methods
graph_Graph_numEdges: Property = Property(name="numEdges", type=IntegerType)
graph_Graph_numNodes: Property = Property(name="numNodes", type=IntegerType)
graph_Graph_numGraphLabels: Property = Property(name="numGraphLabels", type=IntegerType)
graph_Graph_numNodeLabels: Property = Property(name="numNodeLabels", type=IntegerType)
graph_Graph_numDynamicLabels: Property = Property(name="numDynamicLabels", type=IntegerType)
graph_Graph_m_putGraphLabel: Method = Method(name="putGraphLabel", parameters={Parameter(name='graph_label', type=StringType)})
graph_Graph_m_getGraphLabel: Method = Method(name="getGraphLabel", parameters={Parameter(name='graph_uri', type=StringType)}, type=Label)
graph_Graph_m_addDynamicLabel: Method = Method(name="addDynamicLabel", parameters={Parameter(name='graph_dynamiclabel', type=StringType)})
graph_Graph_m_switchToNextValue: Method = Method(name="switchToNextValue", parameters={Parameter(name='graph_currentTime', type=StringType)})
graph_Graph_m_getNodeLabelsByTypeURI: Method = Method(name="getNodeLabelsByTypeURI", parameters={Parameter(name='graph_typeURI', type=StringType)}, type=NodeLabel)
graph_Graph_m_addGraph: Method = Method(name="addGraph", parameters={Parameter(name='graph_filter', type=StringType), Parameter(name='graph_graph', type=StringType)})
graph_Graph_m_putEdge: Method = Method(name="putEdge", parameters={Parameter(name='graph_edge', type=StringType)})
graph_Graph_m_getEdge: Method = Method(name="getEdge", parameters={Parameter(name='graph_uri', type=StringType)}, type=StringType)
graph_Graph_m_putNode: Method = Method(name="putNode", parameters={Parameter(name='graph_node', type=StringType)})
graph_Graph_m_getNode: Method = Method(name="getNode", parameters={Parameter(name='graph_uri', type=StringType)}, type=StringType)
graph_Graph_m_putNodeLabel: Method = Method(name="putNodeLabel", parameters={Parameter(name='graph_label', type=StringType)})
graph_Graph_m_getNodeLabel: Method = Method(name="getNodeLabel", parameters={Parameter(name='graph_uri', type=StringType)}, type=NodeLabel)
graph_Graph.attributes={graph_Graph_numEdges, graph_Graph_numNodes, graph_Graph_numNodeLabels, graph_Graph_numDynamicLabels, graph_Graph_numGraphLabels}
graph_Graph.methods={graph_Graph_m_putEdge, graph_Graph_m_getNodeLabelsByTypeURI, graph_Graph_m_putNodeLabel, graph_Graph_m_getGraphLabel, graph_Graph_m_addDynamicLabel, graph_Graph_m_getEdge, graph_Graph_m_getNodeLabel, graph_Graph_m_putGraphLabel, graph_Graph_m_addGraph, graph_Graph_m_switchToNextValue, graph_Graph_m_putNode, graph_Graph_m_getNode}

# graph_Identifiable class attributes and methods

# SanityChecker class attributes and methods

# graph_NodeLabel class attributes and methods

# graph_StaticNodeLabel class attributes and methods

# StaticLabel class attributes and methods

# graph_URIToIdentifiableMapEntry class attributes and methods
graph_URIToIdentifiableMapEntry_key: Property = Property(name="key", type=StringType)
graph_URIToIdentifiableMapEntry.attributes={graph_URIToIdentifiableMapEntry_key}

# graph_UnresolvedIdentifiable class attributes and methods
graph_UnresolvedIdentifiable_unresolvedURI: Property = Property(name="unresolvedURI", type=StringType)
graph_UnresolvedIdentifiable_fieldName: Property = Property(name="fieldName", type=StringType)
graph_UnresolvedIdentifiable.attributes={graph_UnresolvedIdentifiable_fieldName, graph_UnresolvedIdentifiable_unresolvedURI}

# graph_STEMTime class attributes and methods

# graph_Label class attributes and methods
graph_Label_uRIOfIdentifiableToBeLabeled: Property = Property(name="uRIOfIdentifiableToBeLabeled", type=StringType)
graph_Label.attributes={graph_Label_uRIOfIdentifiableToBeLabeled}

# graph_StaticLabel class attributes and methods

# graph_SanityChecker class attributes and methods

# graph_DynamicEdgeLabel class attributes and methods

# EdgeLabel class attributes and methods

# graph_StaticEdgeLabel class attributes and methods

# Relationships
nextValue0: BinaryAssociation = BinaryAssociation(
    name="nextValue0",
    ends={
        Property(name="graph_LabelValue", type=graph_DynamicLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DynamicLabel", type=graph_LabelValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
decorator1: BinaryAssociation = BinaryAssociation(
    name="decorator1",
    ends={
        Property(name="model.ecoreDecorator", type=graph_DynamicLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="labelsToUpdate", type=graph_Decorator, multiplicity=Multiplicity(0, 1))
    }
)
a2: BinaryAssociation = BinaryAssociation(
    name="a2",
    ends={
        Property(name="graph_Node", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
b3: BinaryAssociation = BinaryAssociation(
    name="b3",
    ends={
        Property(name="graph_Node5", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge4", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
label6: BinaryAssociation = BinaryAssociation(
    name="label6",
    ends={
        Property(name="EdgeLabel", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=graph_EdgeLabel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
edges7: BinaryAssociation = BinaryAssociation(
    name="edges7",
    ends={
        Property(name="graph_URIToEdgeMapEntry", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph", type=graph_URIToEdgeMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes8: BinaryAssociation = BinaryAssociation(
    name="nodes8",
    ends={
        Property(name="graph_URIToNodeMapEntry", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph9", type=graph_URIToNodeMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphLabels10: BinaryAssociation = BinaryAssociation(
    name="graphLabels10",
    ends={
        Property(name="graph_URIToLabelMapEntry", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph11", type=graph_URIToLabelMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeLabels12: BinaryAssociation = BinaryAssociation(
    name="nodeLabels12",
    ends={
        Property(name="graph_URIToNodeLabelMapEntry", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph13", type=graph_URIToNodeLabelMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dynamicLabels14: BinaryAssociation = BinaryAssociation(
    name="dynamicLabels14",
    ends={
        Property(name="graph_DynamicLabel16", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph15", type=graph_DynamicLabel, multiplicity=Multiplicity(0, 9999))
    }
)
identifiable25: BinaryAssociation = BinaryAssociation(
    name="identifiable25",
    ends={
        Property(name="graph_Identifiable", type=graph_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Label26", type=graph_Identifiable, multiplicity=Multiplicity(0, 1))
    }
)
edges27: BinaryAssociation = BinaryAssociation(
    name="edges27",
    ends={
        Property(name="graph_Edge29", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Node28", type=graph_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
labels30: BinaryAssociation = BinaryAssociation(
    name="labels30",
    ends={
        Property(name="NodeLabel", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=graph_NodeLabel, multiplicity=Multiplicity(0, 9999))
    }
)
node31: BinaryAssociation = BinaryAssociation(
    name="node31",
    ends={
        Property(name="Node", type=graph_NodeLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
scenario32: BinaryAssociation = BinaryAssociation(
    name="scenario32",
    ends={
        Property(name="graph_Identifiable34", type=graph_UnresolvedIdentifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_UnresolvedIdentifiable33", type=graph_Identifiable, multiplicity=Multiplicity(0, 1))
    }
)
model35: BinaryAssociation = BinaryAssociation(
    name="model35",
    ends={
        Property(name="graph_Identifiable37", type=graph_UnresolvedIdentifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_UnresolvedIdentifiable36", type=graph_Identifiable, multiplicity=Multiplicity(0, 1))
    }
)
graph38: BinaryAssociation = BinaryAssociation(
    name="graph38",
    ends={
        Property(name="graph_Identifiable40", type=graph_UnresolvedIdentifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_UnresolvedIdentifiable39", type=graph_Identifiable, multiplicity=Multiplicity(0, 1))
    }
)
identifiable41: BinaryAssociation = BinaryAssociation(
    name="identifiable41",
    ends={
        Property(name="graph_Identifiable43", type=graph_UnresolvedIdentifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_UnresolvedIdentifiable42", type=graph_Identifiable, multiplicity=Multiplicity(0, 1))
    }
)
unresolvedIdentifiables17: BinaryAssociation = BinaryAssociation(
    name="unresolvedIdentifiables17",
    ends={
        Property(name="graph_UnresolvedIdentifiable", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph18", type=graph_UnresolvedIdentifiable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decorators19: BinaryAssociation = BinaryAssociation(
    name="decorators19",
    ends={
        Property(name="model.ecoreDecorator20", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=graph_Decorator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
time21: BinaryAssociation = BinaryAssociation(
    name="time21",
    ends={
        Property(name="graph_STEMTime", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph22", type=graph_STEMTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currentValue23: BinaryAssociation = BinaryAssociation(
    name="currentValue23",
    ends={
        Property(name="graph_LabelValue24", type=graph_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Label", type=graph_LabelValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value47: BinaryAssociation = BinaryAssociation(
    name="value47",
    ends={
        Property(name="graph_Edge49", type=graph_URIToEdgeMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_URIToEdgeMapEntry48", type=graph_Edge, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value50: BinaryAssociation = BinaryAssociation(
    name="value50",
    ends={
        Property(name="graph_Node52", type=graph_URIToNodeMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_URIToNodeMapEntry51", type=graph_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value53: BinaryAssociation = BinaryAssociation(
    name="value53",
    ends={
        Property(name="graph_Label55", type=graph_URIToLabelMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_URIToLabelMapEntry54", type=graph_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value56: BinaryAssociation = BinaryAssociation(
    name="value56",
    ends={
        Property(name="graph_NodeLabel", type=graph_URIToNodeLabelMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_URIToNodeLabelMapEntry57", type=graph_NodeLabel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value44: BinaryAssociation = BinaryAssociation(
    name="value44",
    ends={
        Property(name="graph_Identifiable45", type=graph_URIToIdentifiableMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_URIToIdentifiableMapEntry", type=graph_Identifiable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
edge46: BinaryAssociation = BinaryAssociation(
    name="edge46",
    ends={
        Property(name="Edge", type=graph_EdgeLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=graph_Edge, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_graph_DynamicNodeLabel_DynamicLabel = Generalization(general=DynamicLabel, specific=graph_DynamicNodeLabel)
gen_graph_DynamicNodeLabel_NodeLabel = Generalization(general=NodeLabel, specific=graph_DynamicNodeLabel)
gen_graph_Edge_Identifiable = Generalization(general=Identifiable, specific=graph_Edge)
gen_graph_Edge_Modifiable = Generalization(general=Modifiable, specific=graph_Edge)
gen_graph_DynamicLabel_Label = Generalization(general=Label, specific=graph_DynamicLabel)
gen_graph_Graph_Identifiable = Generalization(general=Identifiable, specific=graph_Graph)
gen_graph_LabelValue_SanityChecker = Generalization(general=SanityChecker, specific=graph_LabelValue)
gen_graph_Node_Identifiable = Generalization(general=Identifiable, specific=graph_Node)
gen_graph_NodeLabel_Label = Generalization(general=Label, specific=graph_NodeLabel)
gen_graph_StaticNodeLabel_NodeLabel = Generalization(general=NodeLabel, specific=graph_StaticNodeLabel)
gen_graph_StaticNodeLabel_StaticLabel = Generalization(general=StaticLabel, specific=graph_StaticNodeLabel)
gen_graph_Label_Identifiable = Generalization(general=Identifiable, specific=graph_Label)
gen_graph_StaticLabel_Label = Generalization(general=Label, specific=graph_StaticLabel)
gen_graph_StaticLabel_Modifiable = Generalization(general=Modifiable, specific=graph_StaticLabel)
gen_graph_DynamicEdgeLabel_DynamicLabel = Generalization(general=DynamicLabel, specific=graph_DynamicEdgeLabel)
gen_graph_DynamicEdgeLabel_EdgeLabel = Generalization(general=EdgeLabel, specific=graph_DynamicEdgeLabel)
gen_graph_EdgeLabel_Label = Generalization(general=Label, specific=graph_EdgeLabel)
gen_graph_StaticEdgeLabel_EdgeLabel = Generalization(general=EdgeLabel, specific=graph_StaticEdgeLabel)
gen_graph_StaticEdgeLabel_StaticLabel = Generalization(general=StaticLabel, specific=graph_StaticEdgeLabel)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_LabelValue, graph_Decorator, graph_DynamicNodeLabel, DynamicLabel, NodeLabel, graph_Edge, Identifiable, Modifiable, graph_Node, graph_EdgeLabel, graph_DynamicLabel, Label, graph_URIToEdgeMapEntry, graph_URIToNodeMapEntry, graph_URIToLabelMapEntry, graph_URIToNodeLabelMapEntry, graph_Graph, graph_Identifiable, SanityChecker, graph_NodeLabel, graph_StaticNodeLabel, StaticLabel, graph_URIToIdentifiableMapEntry, graph_UnresolvedIdentifiable, graph_STEMTime, graph_Label, graph_StaticLabel, graph_SanityChecker, graph_DynamicEdgeLabel, EdgeLabel, graph_StaticEdgeLabel},
    associations={nextValue0, decorator1, a2, b3, label6, edges7, nodes8, graphLabels10, nodeLabels12, dynamicLabels14, identifiable25, edges27, labels30, node31, scenario32, model35, graph38, identifiable41, unresolvedIdentifiables17, decorators19, time21, currentValue23, value47, value50, value53, value56, value44, edge46},
    generalizations={gen_graph_DynamicNodeLabel_DynamicLabel, gen_graph_DynamicNodeLabel_NodeLabel, gen_graph_Edge_Identifiable, gen_graph_Edge_Modifiable, gen_graph_DynamicLabel_Label, gen_graph_Graph_Identifiable, gen_graph_LabelValue_SanityChecker, gen_graph_Node_Identifiable, gen_graph_NodeLabel_Label, gen_graph_StaticNodeLabel_NodeLabel, gen_graph_StaticNodeLabel_StaticLabel, gen_graph_Label_Identifiable, gen_graph_StaticLabel_Label, gen_graph_StaticLabel_Modifiable, gen_graph_DynamicEdgeLabel_DynamicLabel, gen_graph_DynamicEdgeLabel_EdgeLabel, gen_graph_EdgeLabel_Label, gen_graph_StaticEdgeLabel_EdgeLabel, gen_graph_StaticEdgeLabel_StaticLabel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)