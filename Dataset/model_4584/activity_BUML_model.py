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
activity_Activity = Class(name="activity::Activity")
activity_ActivityEdge = Class(name="activity::ActivityEdge", is_abstract=True)
activity_ActivityNode = Class(name="activity::ActivityNode", is_abstract=True)
ActivityGroup = Class(name="ActivityGroup")
activity_InterruptibleActivityRegion = Class(name="activity::InterruptibleActivityRegion")
activity_NamedElement = Class(name="activity::NamedElement", is_abstract=True)
activity_ControlNode = Class(name="activity::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
activity_InitialNode = Class(name="activity::InitialNode")
ControlNode = Class(name="ControlNode")
activity_FinalNode = Class(name="activity::FinalNode", is_abstract=True)
activity_ForkNode = Class(name="activity::ForkNode")
activity_JoinNode = Class(name="activity::JoinNode")
activity_Connector = Class(name="activity::Connector")
activity_ActivityParameterNode = Class(name="activity::ActivityParameterNode")
activity_MergeNode = Class(name="activity::MergeNode")
activity_DecisionNode = Class(name="activity::DecisionNode")
activity_ActivityPartition = Class(name="activity::ActivityPartition")
activity_ActivityGroup = Class(name="activity::ActivityGroup", is_abstract=True)
Activity = Class(name="Activity")
NamedElement = Class(name="NamedElement")
activity_CentralBufferNode = Class(name="activity::CentralBufferNode")
activity_DataStoreNode = Class(name="activity::DataStoreNode")
activity_ControlFlow = Class(name="activity::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
activity_ObjectFlow = Class(name="activity::ObjectFlow")
activity_InterruptEdge = Class(name="activity::InterruptEdge")
activity_FlowFinalNode = Class(name="activity::FlowFinalNode")
FinalNode = Class(name="FinalNode")
activity_ActivityFinalNode = Class(name="activity::ActivityFinalNode")
activity_ExecutableNode = Class(name="activity::ExecutableNode", is_abstract=True)
activity_Action = Class(name="activity::Action")
ExecutableNode = Class(name="ExecutableNode")
activity_OutputPin = Class(name="activity::OutputPin")
activity_InputPin = Class(name="activity::InputPin")
activity_SendSignalAction = Class(name="activity::SendSignalAction")
activity_AcceptTimeEventAction = Class(name="activity::AcceptTimeEventAction")
activity_AcceptEventAction = Class(name="activity::AcceptEventAction")
Pin = Class(name="Pin")
activity_ObjectNode = Class(name="activity::ObjectNode", is_abstract=True)
activity_Pin = Class(name="activity::Pin", is_abstract=True)
ObjectNode = Class(name="ObjectNode")
activity_Object = Class(name="activity::Object")

# activity_Activity class attributes and methods

# activity_ActivityEdge class attributes and methods

# activity_ActivityNode class attributes and methods

# ActivityGroup class attributes and methods

# activity_InterruptibleActivityRegion class attributes and methods

# activity_NamedElement class attributes and methods
activity_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
activity_NamedElement_Name: Property = Property(name="Name", type=StringType)
activity_NamedElement.attributes={activity_NamedElement_Name, activity_NamedElement_qualifiedName}

# activity_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# activity_InitialNode class attributes and methods

# ControlNode class attributes and methods

# activity_FinalNode class attributes and methods

# activity_ForkNode class attributes and methods

# activity_JoinNode class attributes and methods

# activity_Connector class attributes and methods

# activity_ActivityParameterNode class attributes and methods
activity_ActivityParameterNode_name: Property = Property(name="name", type=StringType)
activity_ActivityParameterNode.attributes={activity_ActivityParameterNode_name}

# activity_MergeNode class attributes and methods

# activity_DecisionNode class attributes and methods

# activity_ActivityPartition class attributes and methods

# activity_ActivityGroup class attributes and methods
activity_ActivityGroup_name: Property = Property(name="name", type=StringType)
activity_ActivityGroup.attributes={activity_ActivityGroup_name}

# Activity class attributes and methods

# NamedElement class attributes and methods

# activity_CentralBufferNode class attributes and methods

# activity_DataStoreNode class attributes and methods

# activity_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# activity_ObjectFlow class attributes and methods

# activity_InterruptEdge class attributes and methods

# activity_FlowFinalNode class attributes and methods

# FinalNode class attributes and methods

# activity_ActivityFinalNode class attributes and methods

# activity_ExecutableNode class attributes and methods

# activity_Action class attributes and methods

# ExecutableNode class attributes and methods

# activity_OutputPin class attributes and methods

# activity_InputPin class attributes and methods

# activity_SendSignalAction class attributes and methods

# activity_AcceptTimeEventAction class attributes and methods

# activity_AcceptEventAction class attributes and methods

# Pin class attributes and methods

# activity_ObjectNode class attributes and methods

# activity_Pin class attributes and methods

# ObjectNode class attributes and methods

# activity_Object class attributes and methods

# Relationships
edges0: BinaryAssociation = BinaryAssociation(
    name="edges0",
    ends={
        Property(name="activity_ActivityEdge", type=activity_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_Activity", type=activity_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="activity_ActivityNode", type=activity_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_Activity2", type=activity_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing16: BinaryAssociation = BinaryAssociation(
    name="outgoing16",
    ends={
        Property(name="ActivityEdge17", type=activity_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=activity_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activityPartions19: BinaryAssociation = BinaryAssociation(
    name="activityPartions19",
    ends={
        Property(name="activity_ActivityPartition20", type=activity_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ActivityPartition18", type=activity_ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connected22: BinaryAssociation = BinaryAssociation(
    name="connected22",
    ends={
        Property(name="activity_Connector", type=activity_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_Connector21", type=activity_Connector, multiplicity=Multiplicity(0, 1))
    }
)
activityparameternode3: BinaryAssociation = BinaryAssociation(
    name="activityparameternode3",
    ends={
        Property(name="activity_ActivityParameterNode", type=activity_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_Activity4", type=activity_ActivityParameterNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activityPartion5: BinaryAssociation = BinaryAssociation(
    name="activityPartion5",
    ends={
        Property(name="activity_ActivityPartition", type=activity_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_Activity6", type=activity_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
activityGroups7: BinaryAssociation = BinaryAssociation(
    name="activityGroups7",
    ends={
        Property(name="activity_ActivityGroup", type=activity_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_Activity8", type=activity_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inBorder9: BinaryAssociation = BinaryAssociation(
    name="inBorder9",
    ends={
        Property(name="activity_ActivityNode11", type=activity_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_ActivityParameterNode10", type=activity_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="ActivityNode", type=activity_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=activity_ActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="ActivityNode14", type=activity_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=activity_ActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
incoming15: BinaryAssociation = BinaryAssociation(
    name="incoming15",
    ends={
        Property(name="ActivityEdge", type=activity_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=activity_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
output23: BinaryAssociation = BinaryAssociation(
    name="output23",
    ends={
        Property(name="activity_OutputPin", type=activity_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_Action", type=activity_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input24: BinaryAssociation = BinaryAssociation(
    name="input24",
    ends={
        Property(name="activity_InputPin", type=activity_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_Action25", type=activity_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_activity_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=activity_ActivityPartition)
gen_activity_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=activity_InterruptibleActivityRegion)
gen_activity_ActivityGroup_Activity = Generalization(general=Activity, specific=activity_ActivityGroup)
gen_activity_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activity_ControlNode)
gen_activity_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activity_InitialNode)
gen_activity_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activity_FinalNode)
gen_activity_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activity_ForkNode)
gen_activity_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activity_JoinNode)
gen_activity_Connector_ControlNode = Generalization(general=ControlNode, specific=activity_Connector)
gen_activity_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activity_MergeNode)
gen_activity_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activity_DecisionNode)
gen_activity_ActivityParameterNode_Activity = Generalization(general=Activity, specific=activity_ActivityParameterNode)
gen_activity_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=activity_ActivityEdge)
gen_activity_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=activity_ActivityNode)
gen_activity_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=activity_CentralBufferNode)
gen_activity_DataStoreNode_ObjectNode = Generalization(general=ObjectNode, specific=activity_DataStoreNode)
gen_activity_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activity_ControlFlow)
gen_activity_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=activity_ObjectFlow)
gen_activity_InterruptEdge_ActivityEdge = Generalization(general=ActivityEdge, specific=activity_InterruptEdge)
gen_activity_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=activity_FlowFinalNode)
gen_activity_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activity_ActivityFinalNode)
gen_activity_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=activity_ExecutableNode)
gen_activity_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=activity_Action)
gen_activity_SendSignalAction_ExecutableNode = Generalization(general=ExecutableNode, specific=activity_SendSignalAction)
gen_activity_AcceptTimeEventAction_ExecutableNode = Generalization(general=ExecutableNode, specific=activity_AcceptTimeEventAction)
gen_activity_AcceptEventAction_ExecutableNode = Generalization(general=ExecutableNode, specific=activity_AcceptEventAction)
gen_activity_InputPin_Pin = Generalization(general=Pin, specific=activity_InputPin)
gen_activity_OutputPin_Pin = Generalization(general=Pin, specific=activity_OutputPin)
gen_activity_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=activity_ObjectNode)
gen_activity_Pin_ObjectNode = Generalization(general=ObjectNode, specific=activity_Pin)
gen_activity_Object_ObjectNode = Generalization(general=ObjectNode, specific=activity_Object)

# Domain Model
domain_model = DomainModel(
    name="activity",
    types={activity_Activity, activity_ActivityEdge, activity_ActivityNode, ActivityGroup, activity_InterruptibleActivityRegion, activity_NamedElement, activity_ControlNode, ActivityNode, activity_InitialNode, ControlNode, activity_FinalNode, activity_ForkNode, activity_JoinNode, activity_Connector, activity_ActivityParameterNode, activity_MergeNode, activity_DecisionNode, activity_ActivityPartition, activity_ActivityGroup, Activity, NamedElement, activity_CentralBufferNode, activity_DataStoreNode, activity_ControlFlow, ActivityEdge, activity_ObjectFlow, activity_InterruptEdge, activity_FlowFinalNode, FinalNode, activity_ActivityFinalNode, activity_ExecutableNode, activity_Action, ExecutableNode, activity_OutputPin, activity_InputPin, activity_SendSignalAction, activity_AcceptTimeEventAction, activity_AcceptEventAction, Pin, activity_ObjectNode, activity_Pin, ObjectNode, activity_Object},
    associations={edges0, nodes1, outgoing16, activityPartions19, connected22, activityparameternode3, activityPartion5, activityGroups7, inBorder9, target12, source13, incoming15, output23, input24},
    generalizations={gen_activity_ActivityPartition_ActivityGroup, gen_activity_InterruptibleActivityRegion_ActivityGroup, gen_activity_ActivityGroup_Activity, gen_activity_ControlNode_ActivityNode, gen_activity_InitialNode_ControlNode, gen_activity_FinalNode_ControlNode, gen_activity_ForkNode_ControlNode, gen_activity_JoinNode_ControlNode, gen_activity_Connector_ControlNode, gen_activity_MergeNode_ControlNode, gen_activity_DecisionNode_ControlNode, gen_activity_ActivityParameterNode_Activity, gen_activity_ActivityEdge_NamedElement, gen_activity_ActivityNode_NamedElement, gen_activity_CentralBufferNode_ObjectNode, gen_activity_DataStoreNode_ObjectNode, gen_activity_ControlFlow_ActivityEdge, gen_activity_ObjectFlow_ActivityEdge, gen_activity_InterruptEdge_ActivityEdge, gen_activity_FlowFinalNode_FinalNode, gen_activity_ActivityFinalNode_FinalNode, gen_activity_ExecutableNode_ActivityNode, gen_activity_Action_ExecutableNode, gen_activity_SendSignalAction_ExecutableNode, gen_activity_AcceptTimeEventAction_ExecutableNode, gen_activity_AcceptEventAction_ExecutableNode, gen_activity_InputPin_Pin, gen_activity_OutputPin_Pin, gen_activity_ObjectNode_ActivityNode, gen_activity_Pin_ObjectNode, gen_activity_Object_ObjectNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)