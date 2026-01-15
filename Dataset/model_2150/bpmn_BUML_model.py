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
ActivityType: Enumeration = Enumeration(
    name="ActivityType",
    literals={
            EnumerationLiteral(name="Task"),
			EnumerationLiteral(name="SubProcess"),
			EnumerationLiteral(name="EventStartEmpty"),
			EnumerationLiteral(name="EventStartMessage"),
			EnumerationLiteral(name="EventStartRule"),
			EnumerationLiteral(name="EventStartTimer"),
			EnumerationLiteral(name="EventStartLink"),
			EnumerationLiteral(name="EventStartMultiple"),
			EnumerationLiteral(name="EventIntermediateEmpty"),
			EnumerationLiteral(name="EventIntermediateMessage"),
			EnumerationLiteral(name="EventIntermediateTimer"),
			EnumerationLiteral(name="EventIntermediateError"),
			EnumerationLiteral(name="EventIntermediateCompensation"),
			EnumerationLiteral(name="EventIntermediateRule"),
			EnumerationLiteral(name="EventIntermediateLink"),
			EnumerationLiteral(name="EventIntermediateMultiple"),
			EnumerationLiteral(name="EventIntermediateCancel"),
			EnumerationLiteral(name="EventEndEmpty"),
			EnumerationLiteral(name="EventEndMessage"),
			EnumerationLiteral(name="EventEndError"),
			EnumerationLiteral(name="EventEndCompensation"),
			EnumerationLiteral(name="EventEndTerminate"),
			EnumerationLiteral(name="EventEndLink"),
			EnumerationLiteral(name="EventEndMultiple"),
			EnumerationLiteral(name="EventEndCancel"),
			EnumerationLiteral(name="GatewayDataBasedExclusive"),
			EnumerationLiteral(name="GatewayEventBasedExclusive"),
			EnumerationLiteral(name="GatewayDataBasedInclusive"),
			EnumerationLiteral(name="GatewayParallel"),
			EnumerationLiteral(name="GatewayComplex")
    }
)

DirectionType: Enumeration = Enumeration(
    name="DirectionType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="To"),
			EnumerationLiteral(name="From"),
			EnumerationLiteral(name="Both")
    }
)

SequenceFlowConditionType: Enumeration = Enumeration(
    name="SequenceFlowConditionType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Expression"),
			EnumerationLiteral(name="Default")
    }
)

# Classes
NamedBpmnObject = Class(name="NamedBpmnObject")
bpmn_MessagingEdge = Class(name="bpmn::MessagingEdge")
bpmn_Group = Class(name="bpmn::Group")
bpmn_SubProcess = Class(name="bpmn::SubProcess")
bpmn_Activity = Class(name="bpmn::Activity")
Vertex = Class(name="Vertex")
bpmn_Artifact = Class(name="bpmn::Artifact")
Identifiable = Class(name="Identifiable")
bpmn_Association = Class(name="bpmn::Association")
bpmn_Lane = Class(name="bpmn::Lane")
EModelElement = Class(name="EModelElement")
bpmn_IdentifiableNode = Class(name="bpmn::IdentifiableNode")
bpmn_BpmnDiagram = Class(name="bpmn::BpmnDiagram")
ArtifactsContainer = Class(name="ArtifactsContainer")
bpmn_Pool = Class(name="bpmn::Pool")
bpmn_ArtifactsContainer = Class(name="bpmn::ArtifactsContainer")
Artifact = Class(name="Artifact")
bpmn_Graph = Class(name="bpmn::Graph")
IdentifiableNode = Class(name="IdentifiableNode")
bpmn_Vertex = Class(name="bpmn::Vertex")
bpmn_SequenceEdge = Class(name="bpmn::SequenceEdge")
bpmn_Identifiable = Class(name="bpmn::Identifiable")
bpmn_DataObject = Class(name="bpmn::DataObject")
bpmn_NamedBpmnObject = Class(name="bpmn::NamedBpmnObject")
Graph = Class(name="Graph")
Activity = Class(name="Activity")
bpmn_TextAnnotation = Class(name="bpmn::TextAnnotation")

# NamedBpmnObject class attributes and methods

# bpmn_MessagingEdge class attributes and methods

# bpmn_Group class attributes and methods

# bpmn_SubProcess class attributes and methods
bpmn_SubProcess_isTransaction: Property = Property(name="isTransaction", type=StringType)
bpmn_SubProcess.attributes={bpmn_SubProcess_isTransaction}

# bpmn_Activity class attributes and methods
bpmn_Activity_orderedMessages: Property = Property(name="orderedMessages", type=StringType)
bpmn_Activity_activityType: Property = Property(name="activityType", type=StringType)
bpmn_Activity_looping: Property = Property(name="looping", type=StringType)
bpmn_Activity.attributes={bpmn_Activity_activityType, bpmn_Activity_orderedMessages, bpmn_Activity_looping}

# Vertex class attributes and methods

# bpmn_Artifact class attributes and methods

# Identifiable class attributes and methods

# bpmn_Association class attributes and methods
bpmn_Association_direction: Property = Property(name="direction", type=StringType)
bpmn_Association.attributes={bpmn_Association_direction}

# bpmn_Lane class attributes and methods

# EModelElement class attributes and methods

# bpmn_IdentifiableNode class attributes and methods

# bpmn_BpmnDiagram class attributes and methods
bpmn_BpmnDiagram_author: Property = Property(name="author", type=StringType)
bpmn_BpmnDiagram_title: Property = Property(name="title", type=StringType)
bpmn_BpmnDiagram.attributes={bpmn_BpmnDiagram_author, bpmn_BpmnDiagram_title}

# ArtifactsContainer class attributes and methods

# bpmn_Pool class attributes and methods

# bpmn_ArtifactsContainer class attributes and methods

# Artifact class attributes and methods

# bpmn_Graph class attributes and methods

# IdentifiableNode class attributes and methods

# bpmn_Vertex class attributes and methods

# bpmn_SequenceEdge class attributes and methods
bpmn_SequenceEdge_conditionType: Property = Property(name="conditionType", type=StringType)
bpmn_SequenceEdge_isDefault: Property = Property(name="isDefault", type=StringType)
bpmn_SequenceEdge.attributes={bpmn_SequenceEdge_conditionType, bpmn_SequenceEdge_isDefault}

# bpmn_Identifiable class attributes and methods
bpmn_Identifiable_iD: Property = Property(name="iD", type=StringType)
bpmn_Identifiable.attributes={bpmn_Identifiable_iD}

# bpmn_DataObject class attributes and methods

# bpmn_NamedBpmnObject class attributes and methods
bpmn_NamedBpmnObject_ncname: Property = Property(name="ncname", type=StringType)
bpmn_NamedBpmnObject_documentation: Property = Property(name="documentation", type=StringType)
bpmn_NamedBpmnObject_name: Property = Property(name="name", type=StringType)
bpmn_NamedBpmnObject.attributes={bpmn_NamedBpmnObject_name, bpmn_NamedBpmnObject_documentation, bpmn_NamedBpmnObject_ncname}

# Graph class attributes and methods

# Activity class attributes and methods

# bpmn_TextAnnotation class attributes and methods

# Relationships
incomingMessages0: BinaryAssociation = BinaryAssociation(
    name="incomingMessages0",
    ends={
        Property(name="MessagingEdge", type=bpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=bpmn_MessagingEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingMessages1: BinaryAssociation = BinaryAssociation(
    name="outgoingMessages1",
    ends={
        Property(name="MessagingEdge2", type=bpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=bpmn_MessagingEdge, multiplicity=Multiplicity(0, 9999))
    }
)
groups3: BinaryAssociation = BinaryAssociation(
    name="groups3",
    ends={
        Property(name="Group", type=bpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activities", type=bpmn_Group, multiplicity=Multiplicity(0, 9999))
    }
)
eventHandlerFor4: BinaryAssociation = BinaryAssociation(
    name="eventHandlerFor4",
    ends={
        Property(name="SubProcess", type=bpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="eventHandlers", type=bpmn_SubProcess, multiplicity=Multiplicity(0, 1))
    }
)
associations7: BinaryAssociation = BinaryAssociation(
    name="associations7",
    ends={
        Property(name="Association", type=bpmn_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="source8", type=bpmn_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lane5: BinaryAssociation = BinaryAssociation(
    name="lane5",
    ends={
        Property(name="Lane", type=bpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activities6", type=bpmn_Lane, multiplicity=Multiplicity(0, 1))
    }
)
artifacts10: BinaryAssociation = BinaryAssociation(
    name="artifacts10",
    ends={
        Property(name="Artifact", type=bpmn_ArtifactsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="artifactsContainer", type=bpmn_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="Artifact12", type=bpmn_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associations", type=bpmn_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="IdentifiableNode", type=bpmn_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associations14", type=bpmn_IdentifiableNode, multiplicity=Multiplicity(0, 1))
    }
)
pools15: BinaryAssociation = BinaryAssociation(
    name="pools15",
    ends={
        Property(name="Pool", type=bpmn_BpmnDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnDiagram", type=bpmn_Pool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messages16: BinaryAssociation = BinaryAssociation(
    name="messages16",
    ends={
        Property(name="MessagingEdge18", type=bpmn_BpmnDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnDiagram17", type=bpmn_MessagingEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifactsContainer9: BinaryAssociation = BinaryAssociation(
    name="artifactsContainer9",
    ends={
        Property(name="ArtifactsContainer", type=bpmn_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="artifacts", type=bpmn_ArtifactsContainer, multiplicity=Multiplicity(0, 1))
    }
)
vertices19: BinaryAssociation = BinaryAssociation(
    name="vertices19",
    ends={
        Property(name="Vertex", type=bpmn_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=bpmn_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceEdges20: BinaryAssociation = BinaryAssociation(
    name="sequenceEdges20",
    ends={
        Property(name="SequenceEdge", type=bpmn_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph21", type=bpmn_SequenceEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities22: BinaryAssociation = BinaryAssociation(
    name="activities22",
    ends={
        Property(name="Activity", type=bpmn_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=bpmn_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
activities26: BinaryAssociation = BinaryAssociation(
    name="activities26",
    ends={
        Property(name="Activity27", type=bpmn_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="lane", type=bpmn_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
pool28: BinaryAssociation = BinaryAssociation(
    name="pool28",
    ends={
        Property(name="Pool29", type=bpmn_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="lanes", type=bpmn_Pool, multiplicity=Multiplicity(0, 1))
    }
)
bpmnDiagram30: BinaryAssociation = BinaryAssociation(
    name="bpmnDiagram30",
    ends={
        Property(name="BpmnDiagram", type=bpmn_MessagingEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="messages", type=bpmn_BpmnDiagram, multiplicity=Multiplicity(0, 1))
    }
)
source31: BinaryAssociation = BinaryAssociation(
    name="source31",
    ends={
        Property(name="Activity32", type=bpmn_MessagingEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingMessages", type=bpmn_Activity, multiplicity=Multiplicity(0, 1))
    }
)
target33: BinaryAssociation = BinaryAssociation(
    name="target33",
    ends={
        Property(name="Activity34", type=bpmn_MessagingEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingMessages", type=bpmn_Activity, multiplicity=Multiplicity(0, 1))
    }
)
associations23: BinaryAssociation = BinaryAssociation(
    name="associations23",
    ends={
        Property(name="Association25", type=bpmn_IdentifiableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target24", type=bpmn_Association, multiplicity=Multiplicity(0, 9999))
    }
)
lanes35: BinaryAssociation = BinaryAssociation(
    name="lanes35",
    ends={
        Property(name="Lane36", type=bpmn_Pool, multiplicity=Multiplicity(1, 1)),
        Property(name="pool", type=bpmn_Lane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bpmnDiagram37: BinaryAssociation = BinaryAssociation(
    name="bpmnDiagram37",
    ends={
        Property(name="BpmnDiagram38", type=bpmn_Pool, multiplicity=Multiplicity(1, 1)),
        Property(name="pools", type=bpmn_BpmnDiagram, multiplicity=Multiplicity(0, 1))
    }
)
graph39: BinaryAssociation = BinaryAssociation(
    name="graph39",
    ends={
        Property(name="Graph", type=bpmn_SequenceEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="sequenceEdges", type=bpmn_Graph, multiplicity=Multiplicity(0, 1))
    }
)
source40: BinaryAssociation = BinaryAssociation(
    name="source40",
    ends={
        Property(name="Vertex41", type=bpmn_SequenceEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=bpmn_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
target42: BinaryAssociation = BinaryAssociation(
    name="target42",
    ends={
        Property(name="Vertex43", type=bpmn_SequenceEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=bpmn_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
eventHandlers44: BinaryAssociation = BinaryAssociation(
    name="eventHandlers44",
    ends={
        Property(name="Activity45", type=bpmn_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="eventHandlerFor", type=bpmn_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingEdges46: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges46",
    ends={
        Property(name="SequenceEdge48", type=bpmn_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source47", type=bpmn_SequenceEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incomingEdges49: BinaryAssociation = BinaryAssociation(
    name="incomingEdges49",
    ends={
        Property(name="SequenceEdge51", type=bpmn_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target50", type=bpmn_SequenceEdge, multiplicity=Multiplicity(0, 9999))
    }
)
graph52: BinaryAssociation = BinaryAssociation(
    name="graph52",
    ends={
        Property(name="Graph53", type=bpmn_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="vertices", type=bpmn_Graph, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_bpmn_Activity_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_Activity)
gen_bpmn_Activity_Vertex = Generalization(general=Vertex, specific=bpmn_Activity)
gen_bpmn_Artifact_Identifiable = Generalization(general=Identifiable, specific=bpmn_Artifact)
gen_bpmn_Artifact_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_Artifact)
gen_bpmn_Association_EModelElement = Generalization(general=EModelElement, specific=bpmn_Association)
gen_bpmn_BpmnDiagram_Identifiable = Generalization(general=Identifiable, specific=bpmn_BpmnDiagram)
gen_bpmn_BpmnDiagram_ArtifactsContainer = Generalization(general=ArtifactsContainer, specific=bpmn_BpmnDiagram)
gen_bpmn_ArtifactsContainer_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_ArtifactsContainer)
gen_bpmn_DataObject_Artifact = Generalization(general=Artifact, specific=bpmn_DataObject)
gen_bpmn_Graph_IdentifiableNode = Generalization(general=IdentifiableNode, specific=bpmn_Graph)
gen_bpmn_Graph_ArtifactsContainer = Generalization(general=ArtifactsContainer, specific=bpmn_Graph)
gen_bpmn_Group_Artifact = Generalization(general=Artifact, specific=bpmn_Group)
gen_bpmn_Identifiable_EModelElement = Generalization(general=EModelElement, specific=bpmn_Identifiable)
gen_bpmn_Lane_Identifiable = Generalization(general=Identifiable, specific=bpmn_Lane)
gen_bpmn_Lane_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_Lane)
gen_bpmn_MessagingEdge_Identifiable = Generalization(general=Identifiable, specific=bpmn_MessagingEdge)
gen_bpmn_MessagingEdge_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_MessagingEdge)
gen_bpmn_IdentifiableNode_Identifiable = Generalization(general=Identifiable, specific=bpmn_IdentifiableNode)
gen_bpmn_Pool_Graph = Generalization(general=Graph, specific=bpmn_Pool)
gen_bpmn_Pool_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_Pool)
gen_bpmn_SequenceEdge_Identifiable = Generalization(general=Identifiable, specific=bpmn_SequenceEdge)
gen_bpmn_SequenceEdge_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_SequenceEdge)
gen_bpmn_SubProcess_Activity = Generalization(general=Activity, specific=bpmn_SubProcess)
gen_bpmn_SubProcess_Graph = Generalization(general=Graph, specific=bpmn_SubProcess)
gen_bpmn_TextAnnotation_Artifact = Generalization(general=Artifact, specific=bpmn_TextAnnotation)
gen_bpmn_Vertex_IdentifiableNode = Generalization(general=IdentifiableNode, specific=bpmn_Vertex)

# Domain Model
domain_model = DomainModel(
    name="bpmn",
    types={NamedBpmnObject, bpmn_MessagingEdge, bpmn_Group, bpmn_SubProcess, bpmn_Activity, Vertex, bpmn_Artifact, Identifiable, bpmn_Association, bpmn_Lane, EModelElement, bpmn_IdentifiableNode, bpmn_BpmnDiagram, ArtifactsContainer, bpmn_Pool, bpmn_ArtifactsContainer, Artifact, bpmn_Graph, IdentifiableNode, bpmn_Vertex, bpmn_SequenceEdge, bpmn_Identifiable, bpmn_DataObject, bpmn_NamedBpmnObject, Graph, Activity, bpmn_TextAnnotation, ActivityType, DirectionType, SequenceFlowConditionType},
    associations={incomingMessages0, outgoingMessages1, groups3, eventHandlerFor4, associations7, lane5, artifacts10, source11, target13, pools15, messages16, artifactsContainer9, vertices19, sequenceEdges20, activities22, activities26, pool28, bpmnDiagram30, source31, target33, associations23, lanes35, bpmnDiagram37, graph39, source40, target42, eventHandlers44, outgoingEdges46, incomingEdges49, graph52},
    generalizations={gen_bpmn_Activity_NamedBpmnObject, gen_bpmn_Activity_Vertex, gen_bpmn_Artifact_Identifiable, gen_bpmn_Artifact_NamedBpmnObject, gen_bpmn_Association_EModelElement, gen_bpmn_BpmnDiagram_Identifiable, gen_bpmn_BpmnDiagram_ArtifactsContainer, gen_bpmn_ArtifactsContainer_NamedBpmnObject, gen_bpmn_DataObject_Artifact, gen_bpmn_Graph_IdentifiableNode, gen_bpmn_Graph_ArtifactsContainer, gen_bpmn_Group_Artifact, gen_bpmn_Identifiable_EModelElement, gen_bpmn_Lane_Identifiable, gen_bpmn_Lane_NamedBpmnObject, gen_bpmn_MessagingEdge_Identifiable, gen_bpmn_MessagingEdge_NamedBpmnObject, gen_bpmn_IdentifiableNode_Identifiable, gen_bpmn_Pool_Graph, gen_bpmn_Pool_NamedBpmnObject, gen_bpmn_SequenceEdge_Identifiable, gen_bpmn_SequenceEdge_NamedBpmnObject, gen_bpmn_SubProcess_Activity, gen_bpmn_SubProcess_Graph, gen_bpmn_TextAnnotation_Artifact, gen_bpmn_Vertex_IdentifiableNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)