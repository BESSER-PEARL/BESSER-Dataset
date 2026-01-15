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
Label = Class(name="Label")
graph_LabelValue = Class(name="graph::LabelValue", is_abstract=True)
graph_DynamicLabel = Class(name="graph::DynamicLabel", is_abstract=True)
graph_EdgeLabel = Class(name="graph::EdgeLabel", is_abstract=True)
graph_Graph = Class(name="graph::Graph")
graph_Decorator = Class(name="graph::Decorator")
graph_DynamicNodeLabel = Class(name="graph::DynamicNodeLabel", is_abstract=True)
DynamicLabel = Class(name="DynamicLabel")
NodeLabel = Class(name="NodeLabel")
graph_Edge = Class(name="graph::Edge")
Identifiable = Class(name="Identifiable")
Modifiable = Class(name="Modifiable")
graph_Node = Class(name="graph::Node")
graph_URIToEdgeMapEntry = Class(name="graph::URIToEdgeMapEntry")
graph_URIToNodeMapEntry = Class(name="graph::URIToNodeMapEntry")
graph_STEMTime = Class(name="graph::STEMTime")
graph_Label = Class(name="graph::Label", is_abstract=True)
graph_URIToLabelMapEntry = Class(name="graph::URIToLabelMapEntry")
graph_URIToNodeLabelMapEntry = Class(name="graph::URIToNodeLabelMapEntry")
graph_UnresolvedIdentifiable = Class(name="graph::UnresolvedIdentifiable")
graph_StaticNodeLabel = Class(name="graph::StaticNodeLabel", is_abstract=True)
StaticLabel = Class(name="StaticLabel")
graph_Identifiable = Class(name="graph::Identifiable")
SanityChecker = Class(name="SanityChecker")
graph_NodeLabel = Class(name="graph::NodeLabel", is_abstract=True)
graph_StaticEdgeLabel = Class(name="graph::StaticEdgeLabel", is_abstract=True)
graph_URIToIdentifiableMapEntry = Class(name="graph::URIToIdentifiableMapEntry")
graph_SanityChecker = Class(name="graph::SanityChecker", is_abstract=True)
graph_DynamicEdgeLabel = Class(name="graph::DynamicEdgeLabel", is_abstract=True)
EdgeLabel = Class(name="EdgeLabel")
graph_StaticLabel = Class(name="graph::StaticLabel", is_abstract=True)

# Label class attributes and methods

# graph_LabelValue class attributes and methods
graph_LabelValue_m_reset: Method = Method(name="reset", parameters={})
graph_LabelValue.methods={graph_LabelValue_m_reset}

# graph_DynamicLabel class attributes and methods
graph_DynamicLabel_nextValueValid: Property = Property(name="nextValueValid", type=BooleanType)
graph_DynamicLabel_m_reset: Method = Method(name="reset", parameters={})
graph_DynamicLabel_m_switchToNextValue: Method = Method(name="switchToNextValue", parameters={})
graph_DynamicLabel.attributes={graph_DynamicLabel_nextValueValid}
graph_DynamicLabel.methods={graph_DynamicLabel_m_switchToNextValue, graph_DynamicLabel_m_reset}

# graph_EdgeLabel class attributes and methods

# graph_Graph class attributes and methods
graph_Graph_numEdges: Property = Property(name="numEdges", type=IntegerType)
graph_Graph_numNodes: Property = Property(name="numNodes", type=IntegerType)
graph_Graph_numGraphLabels: Property = Property(name="numGraphLabels", type=IntegerType)
graph_Graph_numNodeLabels: Property = Property(name="numNodeLabels", type=IntegerType)
graph_Graph_numDynamicLabels: Property = Property(name="numDynamicLabels", type=IntegerType)
graph_Graph_m_getNodeLabelsByTypeURI: Method = Method(name="getNodeLabelsByTypeURI", parameters={Parameter(name='typeURI')}, type=NodeLabel)
graph_Graph_m_addDynamicLabel: Method = Method(name="addDynamicLabel", parameters={Parameter(name='dynamiclabel')})
graph_Graph_m_switchToNextValue: Method = Method(name="switchToNextValue", parameters={Parameter(name='currentTime')})
graph_Graph_m_addGraph: Method = Method(name="addGraph", parameters={Parameter(name='filter'), Parameter(name='graph')})
graph_Graph_m_putEdge: Method = Method(name="putEdge", parameters={Parameter(name='edge')})
graph_Graph_m_getEdge: Method = Method(name="getEdge", parameters={Parameter(name='uri')}, type=StringType)
graph_Graph_m_putNode: Method = Method(name="putNode", parameters={Parameter(name='node')})
graph_Graph_m_getNode: Method = Method(name="getNode", parameters={Parameter(name='uri')}, type=StringType)
graph_Graph_m_putNodeLabel: Method = Method(name="putNodeLabel", parameters={Parameter(name='label')})
graph_Graph_m_getNodeLabel: Method = Method(name="getNodeLabel", parameters={Parameter(name='uri')}, type=NodeLabel)
graph_Graph_m_putGraphLabel: Method = Method(name="putGraphLabel", parameters={Parameter(name='label')})
graph_Graph_m_getGraphLabel: Method = Method(name="getGraphLabel", parameters={Parameter(name='uri')}, type=Label)
graph_Graph.attributes={graph_Graph_numDynamicLabels, graph_Graph_numGraphLabels, graph_Graph_numNodeLabels, graph_Graph_numEdges, graph_Graph_numNodes}
graph_Graph.methods={graph_Graph_m_putNode, graph_Graph_m_getEdge, graph_Graph_m_addDynamicLabel, graph_Graph_m_getNodeLabelsByTypeURI, graph_Graph_m_putGraphLabel, graph_Graph_m_getGraphLabel, graph_Graph_m_switchToNextValue, graph_Graph_m_getNode, graph_Graph_m_getNodeLabel, graph_Graph_m_addGraph, graph_Graph_m_putEdge, graph_Graph_m_putNodeLabel}

# graph_Decorator class attributes and methods

# graph_DynamicNodeLabel class attributes and methods

# DynamicLabel class attributes and methods

# NodeLabel class attributes and methods

# graph_Edge class attributes and methods
graph_Edge_nodeBURI: Property = Property(name="nodeBURI", type=StringType)
graph_Edge_directed: Property = Property(name="directed", type=BooleanType)
graph_Edge_nodeAURI: Property = Property(name="nodeAURI", type=StringType)
graph_Edge_m_getOtherNode: Method = Method(name="getOtherNode", parameters={Parameter(name='node')}, type=StringType)
graph_Edge_m_isDirectedAt: Method = Method(name="isDirectedAt", parameters={Parameter(name='node')}, type=BooleanType)
graph_Edge.attributes={graph_Edge_directed, graph_Edge_nodeAURI, graph_Edge_nodeBURI}
graph_Edge.methods={graph_Edge_m_getOtherNode, graph_Edge_m_isDirectedAt}

# Identifiable class attributes and methods

# Modifiable class attributes and methods

# graph_Node class attributes and methods

# graph_URIToEdgeMapEntry class attributes and methods
graph_URIToEdgeMapEntry_key: Property = Property(name="key", type=StringType)
graph_URIToEdgeMapEntry.attributes={graph_URIToEdgeMapEntry_key}

# graph_URIToNodeMapEntry class attributes and methods
graph_URIToNodeMapEntry_key: Property = Property(name="key", type=StringType)
graph_URIToNodeMapEntry.attributes={graph_URIToNodeMapEntry_key}

# graph_STEMTime class attributes and methods

# graph_Label class attributes and methods
graph_Label_uRIOfIdentifiableToBeLabeled: Property = Property(name="uRIOfIdentifiableToBeLabeled", type=StringType)
graph_Label.attributes={graph_Label_uRIOfIdentifiableToBeLabeled}

# graph_URIToLabelMapEntry class attributes and methods
graph_URIToLabelMapEntry_key: Property = Property(name="key", type=StringType)
graph_URIToLabelMapEntry.attributes={graph_URIToLabelMapEntry_key}

# graph_URIToNodeLabelMapEntry class attributes and methods
graph_URIToNodeLabelMapEntry_key: Property = Property(name="key", type=StringType)
graph_URIToNodeLabelMapEntry.attributes={graph_URIToNodeLabelMapEntry_key}

# graph_UnresolvedIdentifiable class attributes and methods
graph_UnresolvedIdentifiable_unresolvedURI: Property = Property(name="unresolvedURI", type=StringType)
graph_UnresolvedIdentifiable_fieldName: Property = Property(name="fieldName", type=StringType)
graph_UnresolvedIdentifiable.attributes={graph_UnresolvedIdentifiable_fieldName, graph_UnresolvedIdentifiable_unresolvedURI}

# graph_StaticNodeLabel class attributes and methods

# StaticLabel class attributes and methods

# graph_Identifiable class attributes and methods

# SanityChecker class attributes and methods

# graph_NodeLabel class attributes and methods

# graph_StaticEdgeLabel class attributes and methods

# graph_URIToIdentifiableMapEntry class attributes and methods
graph_URIToIdentifiableMapEntry_key: Property = Property(name="key", type=StringType)
graph_URIToIdentifiableMapEntry.attributes={graph_URIToIdentifiableMapEntry_key}

# graph_SanityChecker class attributes and methods

# graph_DynamicEdgeLabel class attributes and methods

# EdgeLabel class attributes and methods

# graph_StaticLabel class attributes and methods

# Relationships
nextValue0: BinaryAssociation = BinaryAssociation(
    name="nextValue0",
    ends={
        Property(name="graph_LabelValue", type=graph_DynamicLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DynamicLabel", type=graph_LabelValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label6: BinaryAssociation = BinaryAssociation(
    name="label6",
    ends={
        Property(name="EdgeLabel", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=graph_EdgeLabel, multiplicity=Multiplicity(0, 1), is_composite=True)
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
unresolvedIdentifiables17: BinaryAssociation = BinaryAssociation(
    name="unresolvedIdentifiables17",
    ends={
        Property(name="graph_UnresolvedIdentifiable", type=graph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Graph18", type=graph_UnresolvedIdentifiable, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
currentValue23: BinaryAssociation = BinaryAssociation(
    name="currentValue23",
    ends={
        Property(name="graph_LabelValue24", type=graph_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Label", type=graph_LabelValue, multiplicity=Multiplicity(1, 1), is_composite=True)
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
value47: BinaryAssociation = BinaryAssociation(
    name="value47",
    ends={
        Property(name="graph_Edge49", type=graph_URIToEdgeMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_URIToEdgeMapEntry48", type=graph_Edge, multiplicity=Multiplicity(0, 1), is_composite=True)
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

# Generalizations
gen_graph_DynamicLabel_Label = Generalization(general=Label, specific=graph_DynamicLabel)
gen_graph_Graph_Identifiable = Generalization(general=Identifiable, specific=graph_Graph)
gen_graph_DynamicNodeLabel_DynamicLabel = Generalization(general=DynamicLabel, specific=graph_DynamicNodeLabel)
gen_graph_DynamicNodeLabel_NodeLabel = Generalization(general=NodeLabel, specific=graph_DynamicNodeLabel)
gen_graph_Edge_Identifiable = Generalization(general=Identifiable, specific=graph_Edge)
gen_graph_Edge_Modifiable = Generalization(general=Modifiable, specific=graph_Edge)
gen_graph_Label_Identifiable = Generalization(general=Identifiable, specific=graph_Label)
gen_graph_StaticNodeLabel_NodeLabel = Generalization(general=NodeLabel, specific=graph_StaticNodeLabel)
gen_graph_StaticNodeLabel_StaticLabel = Generalization(general=StaticLabel, specific=graph_StaticNodeLabel)
gen_graph_LabelValue_SanityChecker = Generalization(general=SanityChecker, specific=graph_LabelValue)
gen_graph_Node_Identifiable = Generalization(general=Identifiable, specific=graph_Node)
gen_graph_NodeLabel_Label = Generalization(general=Label, specific=graph_NodeLabel)
gen_graph_StaticEdgeLabel_EdgeLabel = Generalization(general=EdgeLabel, specific=graph_StaticEdgeLabel)
gen_graph_StaticEdgeLabel_StaticLabel = Generalization(general=StaticLabel, specific=graph_StaticEdgeLabel)
gen_graph_DynamicEdgeLabel_DynamicLabel = Generalization(general=DynamicLabel, specific=graph_DynamicEdgeLabel)
gen_graph_DynamicEdgeLabel_EdgeLabel = Generalization(general=EdgeLabel, specific=graph_DynamicEdgeLabel)
gen_graph_EdgeLabel_Label = Generalization(general=Label, specific=graph_EdgeLabel)
gen_graph_StaticLabel_Label = Generalization(general=Label, specific=graph_StaticLabel)
gen_graph_StaticLabel_Modifiable = Generalization(general=Modifiable, specific=graph_StaticLabel)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={Label, graph_LabelValue, graph_DynamicLabel, graph_EdgeLabel, graph_Graph, graph_Decorator, graph_DynamicNodeLabel, DynamicLabel, NodeLabel, graph_Edge, Identifiable, Modifiable, graph_Node, graph_URIToEdgeMapEntry, graph_URIToNodeMapEntry, graph_STEMTime, graph_Label, graph_URIToLabelMapEntry, graph_URIToNodeLabelMapEntry, graph_UnresolvedIdentifiable, graph_StaticNodeLabel, StaticLabel, graph_Identifiable, SanityChecker, graph_NodeLabel, graph_StaticEdgeLabel, graph_URIToIdentifiableMapEntry, graph_SanityChecker, graph_DynamicEdgeLabel, EdgeLabel, graph_StaticLabel},
    associations={nextValue0, label6, decorator1, a2, b3, edges7, nodes8, decorators19, time21, graphLabels10, nodeLabels12, dynamicLabels14, unresolvedIdentifiables17, scenario32, model35, currentValue23, identifiable25, edges27, labels30, node31, value47, graph38, identifiable41, value44, edge46, value50, value53, value56},
    generalizations={gen_graph_DynamicLabel_Label, gen_graph_Graph_Identifiable, gen_graph_DynamicNodeLabel_DynamicLabel, gen_graph_DynamicNodeLabel_NodeLabel, gen_graph_Edge_Identifiable, gen_graph_Edge_Modifiable, gen_graph_Label_Identifiable, gen_graph_StaticNodeLabel_NodeLabel, gen_graph_StaticNodeLabel_StaticLabel, gen_graph_LabelValue_SanityChecker, gen_graph_Node_Identifiable, gen_graph_NodeLabel_Label, gen_graph_StaticEdgeLabel_EdgeLabel, gen_graph_StaticEdgeLabel_StaticLabel, gen_graph_DynamicEdgeLabel_DynamicLabel, gen_graph_DynamicEdgeLabel_EdgeLabel, gen_graph_EdgeLabel_Label, gen_graph_StaticLabel_Label, gen_graph_StaticLabel_Modifiable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)