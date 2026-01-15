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
			EnumerationLiteral(name="GatewayComplex"),
			EnumerationLiteral(name="EventStartSignal"),
			EnumerationLiteral(name="EventIntermediateSignal"),
			EnumerationLiteral(name="EventEndSignal")
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
bpmn_SubProcess = Class(name="bpmn::SubProcess")
bpmn_Activity = Class(name="bpmn::Activity")
Vertex = Class(name="Vertex")
MessageVertex = Class(name="MessageVertex")
bpmn_Group = Class(name="bpmn::Group")
bpmn_Lane = Class(name="bpmn::Lane")
bpmn_ArtifactsContainer = Class(name="bpmn::ArtifactsContainer")
EModelElement = Class(name="EModelElement")
bpmn_Artifact = Class(name="bpmn::Artifact")
Identifiable = Class(name="Identifiable")
NamedBpmnObject = Class(name="NamedBpmnObject")
bpmn_Association = Class(name="bpmn::Association")
bpmn_MessagingEdge = Class(name="bpmn::MessagingEdge")
bpmn_DataObject = Class(name="bpmn::DataObject")
Artifact = Class(name="Artifact")
bpmn_AssociationTarget = Class(name="bpmn::AssociationTarget")
bpmn_BpmnDiagram = Class(name="bpmn::BpmnDiagram")
ArtifactsContainer = Class(name="ArtifactsContainer")
bpmn_Pool = Class(name="bpmn::Pool")
bpmn_MessageVertex = Class(name="bpmn::MessageVertex")
bpmn_Graph = Class(name="bpmn::Graph")
AssociationTarget = Class(name="AssociationTarget")
bpmn_Vertex = Class(name="bpmn::Vertex")
bpmn_SequenceEdge = Class(name="bpmn::SequenceEdge")
bpmn_Identifiable = Class(name="bpmn::Identifiable")
Graph = Class(name="Graph")
bpmn_NamedBpmnObject = Class(name="bpmn::NamedBpmnObject")
Activity = Class(name="Activity")
bpmn_TextAnnotation = Class(name="bpmn::TextAnnotation")

# bpmn_SubProcess class attributes and methods
bpmn_SubProcess_isTransaction: Property = Property(name="isTransaction", type=StringType)
bpmn_SubProcess_adhoc: Property = Property(name="adhoc", type=StringType)
bpmn_SubProcess.attributes={bpmn_SubProcess_isTransaction, bpmn_SubProcess_adhoc}

# bpmn_Activity class attributes and methods
bpmn_Activity_looping: Property = Property(name="looping", type=StringType)
bpmn_Activity_activityType: Property = Property(name="activityType", type=StringType)
bpmn_Activity.attributes={bpmn_Activity_activityType, bpmn_Activity_looping}

# Vertex class attributes and methods

# MessageVertex class attributes and methods

# bpmn_Group class attributes and methods

# bpmn_Lane class attributes and methods

# bpmn_ArtifactsContainer class attributes and methods

# EModelElement class attributes and methods

# bpmn_Artifact class attributes and methods

# Identifiable class attributes and methods

# NamedBpmnObject class attributes and methods

# bpmn_Association class attributes and methods
bpmn_Association_direction: Property = Property(name="direction", type=StringType)
bpmn_Association.attributes={bpmn_Association_direction}

# bpmn_MessagingEdge class attributes and methods

# bpmn_DataObject class attributes and methods

# Artifact class attributes and methods

# bpmn_AssociationTarget class attributes and methods

# bpmn_BpmnDiagram class attributes and methods
bpmn_BpmnDiagram_author: Property = Property(name="author", type=StringType)
bpmn_BpmnDiagram_title: Property = Property(name="title", type=StringType)
bpmn_BpmnDiagram.attributes={bpmn_BpmnDiagram_author, bpmn_BpmnDiagram_title}

# ArtifactsContainer class attributes and methods

# bpmn_Pool class attributes and methods

# bpmn_MessageVertex class attributes and methods
bpmn_MessageVertex_orderedMessages: Property = Property(name="orderedMessages", type=StringType)
bpmn_MessageVertex.attributes={bpmn_MessageVertex_orderedMessages}

# bpmn_Graph class attributes and methods

# AssociationTarget class attributes and methods

# bpmn_Vertex class attributes and methods

# bpmn_SequenceEdge class attributes and methods
bpmn_SequenceEdge_conditionType: Property = Property(name="conditionType", type=StringType)
bpmn_SequenceEdge_isDefault: Property = Property(name="isDefault", type=StringType)
bpmn_SequenceEdge.attributes={bpmn_SequenceEdge_isDefault, bpmn_SequenceEdge_conditionType}

# bpmn_Identifiable class attributes and methods
bpmn_Identifiable_iD: Property = Property(name="iD", type=StringType)
bpmn_Identifiable.attributes={bpmn_Identifiable_iD}

# Graph class attributes and methods

# bpmn_NamedBpmnObject class attributes and methods
bpmn_NamedBpmnObject_documentation: Property = Property(name="documentation", type=StringType)
bpmn_NamedBpmnObject_name: Property = Property(name="name", type=StringType)
bpmn_NamedBpmnObject_ncname: Property = Property(name="ncname", type=StringType)
bpmn_NamedBpmnObject.attributes={bpmn_NamedBpmnObject_documentation, bpmn_NamedBpmnObject_name, bpmn_NamedBpmnObject_ncname}

# Activity class attributes and methods

# bpmn_TextAnnotation class attributes and methods

# Relationships
eventHandlerFor3: BinaryAssociation = BinaryAssociation(
    name="eventHandlerFor3",
    ends={
        Property(name="SubProcess", type=bpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="eventHandlers", type=bpmn_SubProcess, multiplicity=Multiplicity(0, 1))
    }
)
groups0: BinaryAssociation = BinaryAssociation(
    name="groups0",
    ends={
        Property(name="Group", type=bpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activities", type=bpmn_Group, multiplicity=Multiplicity(0, 9999))
    }
)
lanes1: BinaryAssociation = BinaryAssociation(
    name="lanes1",
    ends={
        Property(name="Lane", type=bpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activities2", type=bpmn_Lane, multiplicity=Multiplicity(0, 9999))
    }
)
artifactsContainer5: BinaryAssociation = BinaryAssociation(
    name="artifactsContainer5",
    ends={
        Property(name="ArtifactsContainer", type=bpmn_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="artifacts", type=bpmn_ArtifactsContainer, multiplicity=Multiplicity(0, 1))
    }
)
artifacts6: BinaryAssociation = BinaryAssociation(
    name="artifacts6",
    ends={
        Property(name="Artifact", type=bpmn_ArtifactsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="artifactsContainer", type=bpmn_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations4: BinaryAssociation = BinaryAssociation(
    name="associations4",
    ends={
        Property(name="Association", type=bpmn_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=bpmn_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messages14: BinaryAssociation = BinaryAssociation(
    name="messages14",
    ends={
        Property(name="MessagingEdge", type=bpmn_BpmnDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnDiagram15", type=bpmn_MessagingEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="Artifact8", type=bpmn_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associations", type=bpmn_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="AssociationTarget", type=bpmn_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associations10", type=bpmn_AssociationTarget, multiplicity=Multiplicity(0, 1))
    }
)
associations11: BinaryAssociation = BinaryAssociation(
    name="associations11",
    ends={
        Property(name="Association12", type=bpmn_AssociationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=bpmn_Association, multiplicity=Multiplicity(0, 9999))
    }
)
pools13: BinaryAssociation = BinaryAssociation(
    name="pools13",
    ends={
        Property(name="Pool", type=bpmn_BpmnDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="bpmnDiagram", type=bpmn_Pool, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities20: BinaryAssociation = BinaryAssociation(
    name="activities20",
    ends={
        Property(name="Activity21", type=bpmn_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="lanes", type=bpmn_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
pool22: BinaryAssociation = BinaryAssociation(
    name="pool22",
    ends={
        Property(name="Pool24", type=bpmn_Lane, multiplicity=Multiplicity(1, 1)),
        Property(name="lanes23", type=bpmn_Pool, multiplicity=Multiplicity(0, 1))
    }
)
vertices16: BinaryAssociation = BinaryAssociation(
    name="vertices16",
    ends={
        Property(name="Vertex", type=bpmn_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=bpmn_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceEdges17: BinaryAssociation = BinaryAssociation(
    name="sequenceEdges17",
    ends={
        Property(name="SequenceEdge", type=bpmn_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph18", type=bpmn_SequenceEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities19: BinaryAssociation = BinaryAssociation(
    name="activities19",
    ends={
        Property(name="Activity", type=bpmn_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=bpmn_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
incomingMessages25: BinaryAssociation = BinaryAssociation(
    name="incomingMessages25",
    ends={
        Property(name="MessagingEdge27", type=bpmn_MessageVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target26", type=bpmn_MessagingEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingMessages28: BinaryAssociation = BinaryAssociation(
    name="outgoingMessages28",
    ends={
        Property(name="MessagingEdge30", type=bpmn_MessageVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source29", type=bpmn_MessagingEdge, multiplicity=Multiplicity(0, 9999))
    }
)
source31: BinaryAssociation = BinaryAssociation(
    name="source31",
    ends={
        Property(name="MessageVertex", type=bpmn_MessagingEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingMessages", type=bpmn_MessageVertex, multiplicity=Multiplicity(0, 1))
    }
)
target32: BinaryAssociation = BinaryAssociation(
    name="target32",
    ends={
        Property(name="MessageVertex33", type=bpmn_MessagingEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingMessages", type=bpmn_MessageVertex, multiplicity=Multiplicity(0, 1))
    }
)
bpmnDiagram34: BinaryAssociation = BinaryAssociation(
    name="bpmnDiagram34",
    ends={
        Property(name="BpmnDiagram", type=bpmn_MessagingEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="messages", type=bpmn_BpmnDiagram, multiplicity=Multiplicity(0, 1))
    }
)
eventHandlers44: BinaryAssociation = BinaryAssociation(
    name="eventHandlers44",
    ends={
        Property(name="Activity45", type=bpmn_SubProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="eventHandlerFor", type=bpmn_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
source39: BinaryAssociation = BinaryAssociation(
    name="source39",
    ends={
        Property(name="Vertex40", type=bpmn_SequenceEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=bpmn_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
target41: BinaryAssociation = BinaryAssociation(
    name="target41",
    ends={
        Property(name="Vertex42", type=bpmn_SequenceEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=bpmn_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
graph43: BinaryAssociation = BinaryAssociation(
    name="graph43",
    ends={
        Property(name="Graph", type=bpmn_SequenceEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="sequenceEdges", type=bpmn_Graph, multiplicity=Multiplicity(0, 1))
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
gen_bpmn_Activity_Vertex = Generalization(general=Vertex, specific=bpmn_Activity)
gen_bpmn_Activity_MessageVertex = Generalization(general=MessageVertex, specific=bpmn_Activity)
gen_bpmn_ArtifactsContainer_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_ArtifactsContainer)
gen_bpmn_Association_EModelElement = Generalization(general=EModelElement, specific=bpmn_Association)
gen_bpmn_Artifact_Identifiable = Generalization(general=Identifiable, specific=bpmn_Artifact)
gen_bpmn_Artifact_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_Artifact)
gen_bpmn_DataObject_Artifact = Generalization(general=Artifact, specific=bpmn_DataObject)
gen_bpmn_AssociationTarget_Identifiable = Generalization(general=Identifiable, specific=bpmn_AssociationTarget)
gen_bpmn_BpmnDiagram_Identifiable = Generalization(general=Identifiable, specific=bpmn_BpmnDiagram)
gen_bpmn_BpmnDiagram_ArtifactsContainer = Generalization(general=ArtifactsContainer, specific=bpmn_BpmnDiagram)
gen_bpmn_Lane_AssociationTarget = Generalization(general=AssociationTarget, specific=bpmn_Lane)
gen_bpmn_Lane_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_Lane)
gen_bpmn_MessageVertex_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_MessageVertex)
gen_bpmn_MessageVertex_Identifiable = Generalization(general=Identifiable, specific=bpmn_MessageVertex)
gen_bpmn_Graph_AssociationTarget = Generalization(general=AssociationTarget, specific=bpmn_Graph)
gen_bpmn_Graph_ArtifactsContainer = Generalization(general=ArtifactsContainer, specific=bpmn_Graph)
gen_bpmn_Group_Artifact = Generalization(general=Artifact, specific=bpmn_Group)
gen_bpmn_Identifiable_EModelElement = Generalization(general=EModelElement, specific=bpmn_Identifiable)
gen_bpmn_Pool_Graph = Generalization(general=Graph, specific=bpmn_Pool)
gen_bpmn_Pool_MessageVertex = Generalization(general=MessageVertex, specific=bpmn_Pool)
gen_bpmn_MessagingEdge_AssociationTarget = Generalization(general=AssociationTarget, specific=bpmn_MessagingEdge)
gen_bpmn_MessagingEdge_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_MessagingEdge)
gen_bpmn_SubProcess_Activity = Generalization(general=Activity, specific=bpmn_SubProcess)
gen_bpmn_SubProcess_Graph = Generalization(general=Graph, specific=bpmn_SubProcess)
gen_bpmn_SequenceEdge_AssociationTarget = Generalization(general=AssociationTarget, specific=bpmn_SequenceEdge)
gen_bpmn_SequenceEdge_NamedBpmnObject = Generalization(general=NamedBpmnObject, specific=bpmn_SequenceEdge)
gen_bpmn_TextAnnotation_Artifact = Generalization(general=Artifact, specific=bpmn_TextAnnotation)
gen_bpmn_Vertex_AssociationTarget = Generalization(general=AssociationTarget, specific=bpmn_Vertex)

# Domain Model
domain_model = DomainModel(
    name="bpmn",
    types={bpmn_SubProcess, bpmn_Activity, Vertex, MessageVertex, bpmn_Group, bpmn_Lane, bpmn_ArtifactsContainer, EModelElement, bpmn_Artifact, Identifiable, NamedBpmnObject, bpmn_Association, bpmn_MessagingEdge, bpmn_DataObject, Artifact, bpmn_AssociationTarget, bpmn_BpmnDiagram, ArtifactsContainer, bpmn_Pool, bpmn_MessageVertex, bpmn_Graph, AssociationTarget, bpmn_Vertex, bpmn_SequenceEdge, bpmn_Identifiable, Graph, bpmn_NamedBpmnObject, Activity, bpmn_TextAnnotation, ActivityType, DirectionType, SequenceFlowConditionType},
    associations={eventHandlerFor3, groups0, lanes1, artifactsContainer5, artifacts6, associations4, messages14, source7, target9, associations11, pools13, activities20, pool22, vertices16, sequenceEdges17, activities19, incomingMessages25, outgoingMessages28, source31, target32, bpmnDiagram34, eventHandlers44, lanes35, bpmnDiagram37, source39, target41, graph43, outgoingEdges46, incomingEdges49, graph52},
    generalizations={gen_bpmn_Activity_Vertex, gen_bpmn_Activity_MessageVertex, gen_bpmn_ArtifactsContainer_NamedBpmnObject, gen_bpmn_Association_EModelElement, gen_bpmn_Artifact_Identifiable, gen_bpmn_Artifact_NamedBpmnObject, gen_bpmn_DataObject_Artifact, gen_bpmn_AssociationTarget_Identifiable, gen_bpmn_BpmnDiagram_Identifiable, gen_bpmn_BpmnDiagram_ArtifactsContainer, gen_bpmn_Lane_AssociationTarget, gen_bpmn_Lane_NamedBpmnObject, gen_bpmn_MessageVertex_NamedBpmnObject, gen_bpmn_MessageVertex_Identifiable, gen_bpmn_Graph_AssociationTarget, gen_bpmn_Graph_ArtifactsContainer, gen_bpmn_Group_Artifact, gen_bpmn_Identifiable_EModelElement, gen_bpmn_Pool_Graph, gen_bpmn_Pool_MessageVertex, gen_bpmn_MessagingEdge_AssociationTarget, gen_bpmn_MessagingEdge_NamedBpmnObject, gen_bpmn_SubProcess_Activity, gen_bpmn_SubProcess_Graph, gen_bpmn_SequenceEdge_AssociationTarget, gen_bpmn_SequenceEdge_NamedBpmnObject, gen_bpmn_TextAnnotation_Artifact, gen_bpmn_Vertex_AssociationTarget},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)