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
activitydiagram_Activity = Class(name="activitydiagram::Activity")
ADElement = Class(name="ADElement")
activitydiagram_ADElement = Class(name="activitydiagram::ADElement", is_abstract=True)
activitydiagram_ActivityNode = Class(name="activitydiagram::ActivityNode", is_abstract=True)
activitydiagram_ActivityEdge = Class(name="activitydiagram::ActivityEdge")
activitydiagram_MergeNode = Class(name="activitydiagram::MergeNode")
activitydiagram_DecisionNode = Class(name="activitydiagram::DecisionNode")
activitydiagram_AcceptSignalNode = Class(name="activitydiagram::AcceptSignalNode")
activitydiagram_TimeEventNode = Class(name="activitydiagram::TimeEventNode")
activitydiagram_ActivityFinalNode = Class(name="activitydiagram::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
activitydiagram_FlowFinalNode = Class(name="activitydiagram::FlowFinalNode")
activitydiagram_ActivityParameterNode = Class(name="activitydiagram::ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
activitydiagram_DataStoreNode = Class(name="activitydiagram::DataStoreNode")
activitydiagram_Pin = Class(name="activitydiagram::Pin")
activitydiagram_ExpansionNode = Class(name="activitydiagram::ExpansionNode")
activitydiagram_ActionNode = Class(name="activitydiagram::ActionNode")
ActivityNode = Class(name="ActivityNode")
activitydiagram_ControlNode = Class(name="activitydiagram::ControlNode", is_abstract=True)
activitydiagram_ObjectNode = Class(name="activitydiagram::ObjectNode", is_abstract=True)
activitydiagram_SignalNode = Class(name="activitydiagram::SignalNode")
activitydiagram_InitialNode = Class(name="activitydiagram::InitialNode")
ControlNode = Class(name="ControlNode")
activitydiagram_FinalNode = Class(name="activitydiagram::FinalNode", is_abstract=True)
activitydiagram_ForkNode = Class(name="activitydiagram::ForkNode")
activitydiagram_JoinNode = Class(name="activitydiagram::JoinNode")

# activitydiagram_Activity class attributes and methods

# ADElement class attributes and methods

# activitydiagram_ADElement class attributes and methods
activitydiagram_ADElement_name: Property = Property(name="name", type=StringType)
activitydiagram_ADElement.attributes={activitydiagram_ADElement_name}

# activitydiagram_ActivityNode class attributes and methods
activitydiagram_ActivityNode_current: Property = Property(name="current", type=BooleanType)
activitydiagram_ActivityNode.attributes={activitydiagram_ActivityNode_current}

# activitydiagram_ActivityEdge class attributes and methods
activitydiagram_ActivityEdge_guard: Property = Property(name="guard", type=BooleanType)
activitydiagram_ActivityEdge.attributes={activitydiagram_ActivityEdge_guard}

# activitydiagram_MergeNode class attributes and methods

# activitydiagram_DecisionNode class attributes and methods

# activitydiagram_AcceptSignalNode class attributes and methods
activitydiagram_AcceptSignalNode_signalId: Property = Property(name="signalId", type=StringType)
activitydiagram_AcceptSignalNode.attributes={activitydiagram_AcceptSignalNode_signalId}

# activitydiagram_TimeEventNode class attributes and methods
activitydiagram_TimeEventNode_cycle: Property = Property(name="cycle", type=StringType)
activitydiagram_TimeEventNode.attributes={activitydiagram_TimeEventNode_cycle}

# activitydiagram_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# activitydiagram_FlowFinalNode class attributes and methods

# activitydiagram_ActivityParameterNode class attributes and methods
activitydiagram_ActivityParameterNode_parameter: Property = Property(name="parameter", type=StringType)
activitydiagram_ActivityParameterNode.attributes={activitydiagram_ActivityParameterNode_parameter}

# ObjectNode class attributes and methods

# activitydiagram_DataStoreNode class attributes and methods

# activitydiagram_Pin class attributes and methods

# activitydiagram_ExpansionNode class attributes and methods

# activitydiagram_ActionNode class attributes and methods

# ActivityNode class attributes and methods

# activitydiagram_ControlNode class attributes and methods

# activitydiagram_ObjectNode class attributes and methods

# activitydiagram_SignalNode class attributes and methods
activitydiagram_SignalNode_signalId: Property = Property(name="signalId", type=StringType)
activitydiagram_SignalNode.attributes={activitydiagram_SignalNode_signalId}

# activitydiagram_InitialNode class attributes and methods

# ControlNode class attributes and methods

# activitydiagram_FinalNode class attributes and methods

# activitydiagram_ForkNode class attributes and methods

# activitydiagram_JoinNode class attributes and methods

# Relationships
contains0: BinaryAssociation = BinaryAssociation(
    name="contains0",
    ends={
        Property(name="ADElement", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activityDiag", type=activitydiagram_ADElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activityDiag1: BinaryAssociation = BinaryAssociation(
    name="activityDiag1",
    ends={
        Property(name="Activity", type=activitydiagram_ADElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contains", type=activitydiagram_Activity, multiplicity=Multiplicity(1, 1))
    }
)
sedges2: BinaryAssociation = BinaryAssociation(
    name="sedges2",
    ends={
        Property(name="ActivityEdge", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
tedges3: BinaryAssociation = BinaryAssociation(
    name="tedges3",
    ends={
        Property(name="ActivityEdge4", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="ActivityNode", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="sedges", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="ActivityNode7", type=activitydiagram_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="tedges", type=activitydiagram_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_activitydiagram_Activity_ADElement = Generalization(general=ADElement, specific=activitydiagram_Activity)
gen_activitydiagram_ActivityNode_ADElement = Generalization(general=ADElement, specific=activitydiagram_ActivityNode)
gen_activitydiagram_ActivityEdge_ADElement = Generalization(general=ADElement, specific=activitydiagram_ActivityEdge)
gen_activitydiagram_MergeNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_MergeNode)
gen_activitydiagram_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_DecisionNode)
gen_activitydiagram_AcceptSignalNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_AcceptSignalNode)
gen_activitydiagram_TimeEventNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_TimeEventNode)
gen_activitydiagram_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_ActivityFinalNode)
gen_activitydiagram_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=activitydiagram_FlowFinalNode)
gen_activitydiagram_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=activitydiagram_ActivityParameterNode)
gen_activitydiagram_DataStoreNode_ObjectNode = Generalization(general=ObjectNode, specific=activitydiagram_DataStoreNode)
gen_activitydiagram_Pin_ObjectNode = Generalization(general=ObjectNode, specific=activitydiagram_Pin)
gen_activitydiagram_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=activitydiagram_ExpansionNode)
gen_activitydiagram_ActionNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ActionNode)
gen_activitydiagram_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ControlNode)
gen_activitydiagram_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_ObjectNode)
gen_activitydiagram_SignalNode_ActivityNode = Generalization(general=ActivityNode, specific=activitydiagram_SignalNode)
gen_activitydiagram_InitialNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_InitialNode)
gen_activitydiagram_FinalNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_FinalNode)
gen_activitydiagram_ForkNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_ForkNode)
gen_activitydiagram_JoinNode_ControlNode = Generalization(general=ControlNode, specific=activitydiagram_JoinNode)

# Domain Model
domain_model = DomainModel(
    name="activitydiagram",
    types={activitydiagram_Activity, ADElement, activitydiagram_ADElement, activitydiagram_ActivityNode, activitydiagram_ActivityEdge, activitydiagram_MergeNode, activitydiagram_DecisionNode, activitydiagram_AcceptSignalNode, activitydiagram_TimeEventNode, activitydiagram_ActivityFinalNode, FinalNode, activitydiagram_FlowFinalNode, activitydiagram_ActivityParameterNode, ObjectNode, activitydiagram_DataStoreNode, activitydiagram_Pin, activitydiagram_ExpansionNode, activitydiagram_ActionNode, ActivityNode, activitydiagram_ControlNode, activitydiagram_ObjectNode, activitydiagram_SignalNode, activitydiagram_InitialNode, ControlNode, activitydiagram_FinalNode, activitydiagram_ForkNode, activitydiagram_JoinNode},
    associations={contains0, activityDiag1, sedges2, tedges3, source5, target6},
    generalizations={gen_activitydiagram_Activity_ADElement, gen_activitydiagram_ActivityNode_ADElement, gen_activitydiagram_ActivityEdge_ADElement, gen_activitydiagram_MergeNode_ControlNode, gen_activitydiagram_DecisionNode_ControlNode, gen_activitydiagram_AcceptSignalNode_ActivityNode, gen_activitydiagram_TimeEventNode_ActivityNode, gen_activitydiagram_ActivityFinalNode_FinalNode, gen_activitydiagram_FlowFinalNode_FinalNode, gen_activitydiagram_ActivityParameterNode_ObjectNode, gen_activitydiagram_DataStoreNode_ObjectNode, gen_activitydiagram_Pin_ObjectNode, gen_activitydiagram_ExpansionNode_ObjectNode, gen_activitydiagram_ActionNode_ActivityNode, gen_activitydiagram_ControlNode_ActivityNode, gen_activitydiagram_ObjectNode_ActivityNode, gen_activitydiagram_SignalNode_ActivityNode, gen_activitydiagram_InitialNode_ControlNode, gen_activitydiagram_FinalNode_ControlNode, gen_activitydiagram_ForkNode_ControlNode, gen_activitydiagram_JoinNode_ControlNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)