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
ObjectNodeOrderingKind: Enumeration = Enumeration(
    name="ObjectNodeOrderingKind",
    literals={
            EnumerationLiteral(name="unordered"),
			EnumerationLiteral(name="ordered"),
			EnumerationLiteral(name="LIFO"),
			EnumerationLiteral(name="FIFO")
    }
)

ParameterEffectKind: Enumeration = Enumeration(
    name="ParameterEffectKind",
    literals={
            EnumerationLiteral(name="create"),
			EnumerationLiteral(name="read"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="delete")
    }
)

ExpansionKind: Enumeration = Enumeration(
    name="ExpansionKind",
    literals={
            EnumerationLiteral(name="parallel"),
			EnumerationLiteral(name="iterative"),
			EnumerationLiteral(name="stream")
    }
)

# Classes
Activities_FundamentalActivities_Activity = Class(name="Activities::FundamentalActivities::Activity")
InterruptibleActivityRegion = Class(name="InterruptibleActivityRegion")
Behavior = Class(name="Behavior")
ActivityNode = Class(name="ActivityNode")
ActivityGroup = Class(name="ActivityGroup")
ActivityEdge = Class(name="ActivityEdge")
ActivityPartition = Class(name="ActivityPartition")
StructuredActivityNode = Class(name="StructuredActivityNode")
Variable = Class(name="Variable")
Activities_FundamentalActivities_Behavior = Class(name="Activities::FundamentalActivities::Behavior", is_abstract=True)
Class_ = Class(name="Class")
ParameterSet = Class(name="ParameterSet")
Activities_FundamentalActivities_NamedElement = Class(name="Activities::FundamentalActivities::NamedElement", is_abstract=True)
Activities_FundamentalActivities_ActivityNode = Class(name="Activities::FundamentalActivities::ActivityNode", is_abstract=True)
FundamentalActivities_NamedElement = Class(name="FundamentalActivities::NamedElement")
BasicActivities_RedefinableElement = Class(name="BasicActivities::RedefinableElement")
Activities_BasicActivities_RedefinableElement = Class(name="Activities::BasicActivities::RedefinableElement", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Activities_BasicActivities_ObjectNode = Class(name="Activities::BasicActivities::ObjectNode", is_abstract=True)
FundamentalActivities_ActivityNode = Class(name="FundamentalActivities::ActivityNode")
BasicActivities_TypedElement = Class(name="BasicActivities::TypedElement")
Activities_BasicActivities_TypedElement = Class(name="Activities::BasicActivities::TypedElement")
Activities_BasicActivities_Pin = Class(name="Activities::BasicActivities::Pin", is_abstract=True)
ObjectNode = Class(name="ObjectNode")
Activities_BasicActivities_ActivityParameterNode = Class(name="Activities::BasicActivities::ActivityParameterNode")
Parameter_ = Class(name="Parameter")
Activities_FundamentalActivities_Action = Class(name="Activities::FundamentalActivities::Action")
Constraint = Class(name="Constraint")
InputPin = Class(name="InputPin")
OutputPin = Class(name="OutputPin")
Activities_FundamentalActivities_ActivityGroup = Class(name="Activities::FundamentalActivities::ActivityGroup", is_abstract=True)
NamedElement = Class(name="NamedElement")
Activity = Class(name="Activity")
Activities_FundamentalActivities_Namespace = Class(name="Activities::FundamentalActivities::Namespace", is_abstract=True)
Activities_BasicActivities_ControlFlow = Class(name="Activities::BasicActivities::ControlFlow")
Activities_BasicActivities_ObjectFlow = Class(name="Activities::BasicActivities::ObjectFlow")
Activities_BasicActivities_Parameter = Class(name="Activities::BasicActivities::Parameter")
Activities_BasicActivities_ControlNode = Class(name="Activities::BasicActivities::ControlNode", is_abstract=True)
Activities_BasicActivities_ActivityFinalNode = Class(name="Activities::BasicActivities::ActivityFinalNode")
BasicActivities_ControlNode = Class(name="BasicActivities::ControlNode")
IntermediateActivities_FinalNode = Class(name="IntermediateActivities::FinalNode")
Activities_BasicActivities_InitialNode = Class(name="Activities::BasicActivities::InitialNode")
ControlNode = Class(name="ControlNode")
Activities_BasicActivities_ActivityEdge = Class(name="Activities::BasicActivities::ActivityEdge", is_abstract=True)
ValueSpecification = Class(name="ValueSpecification")
Activities_IntermediateActivities_ValueSpecification = Class(name="Activities::IntermediateActivities::ValueSpecification", is_abstract=True)
Activities_IntermediateActivities_ActivityPartition = Class(name="Activities::IntermediateActivities::ActivityPartition")
Element = Class(name="Element")
State = Class(name="State")
Activities_IntermediateActivities_CentralBufferNode = Class(name="Activities::IntermediateActivities::CentralBufferNode")
Activities_IntermediateActivities_FinalNode = Class(name="Activities::IntermediateActivities::FinalNode", is_abstract=True)
Activities_IntermediateActivities_FlowFinalNode = Class(name="Activities::IntermediateActivities::FlowFinalNode")
FinalNode = Class(name="FinalNode")
Activities_IntermediateActivities_ForkNode = Class(name="Activities::IntermediateActivities::ForkNode")
Activities_IntermediateActivities_JoinNode = Class(name="Activities::IntermediateActivities::JoinNode")
Activities_IntermediateActivities_MergeNode = Class(name="Activities::IntermediateActivities::MergeNode")
Activities_IntermediateActivities_DecisionNode = Class(name="Activities::IntermediateActivities::DecisionNode")
ObjectFlow = Class(name="ObjectFlow")
Activities_StructuredActivities_StructuredActivityNode = Class(name="Activities::StructuredActivities::StructuredActivityNode")
StructuredActivities_ExecutableNode = Class(name="StructuredActivities::ExecutableNode")
FundamentalActivities_ActivityGroup = Class(name="FundamentalActivities::ActivityGroup")
FundamentalActivities_Action = Class(name="FundamentalActivities::Action")
Activities_IntermediateActivities_Element = Class(name="Activities::IntermediateActivities::Element", is_abstract=True)
Activities_IntermediateActivities_Constraint = Class(name="Activities::IntermediateActivities::Constraint")
Activities_IntermediateActivities_State = Class(name="Activities::IntermediateActivities::State")
Activities_IntermediateActivities_DataStoreNode = Class(name="Activities::IntermediateActivities::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
Activities_IntermediateActivities_ParameterSet = Class(name="Activities::IntermediateActivities::ParameterSet")
Activities_IntermediateActivities_BehavioralFeature = Class(name="Activities::IntermediateActivities::BehavioralFeature", is_abstract=True)
FundamentalActivities_Namespace = Class(name="FundamentalActivities::Namespace")
IntermediateActivities_Feature = Class(name="IntermediateActivities::Feature")
Activities_IntermediateActivities_Feature = Class(name="Activities::IntermediateActivities::Feature", is_abstract=True)
Activities_IntermediateActivities_Class = Class(name="Activities::IntermediateActivities::Class")
Activities_IntermediateActivities_InterruptibleActivityRegion = Class(name="Activities::IntermediateActivities::InterruptibleActivityRegion")
Activities_StructuredActivities_OutputPin = Class(name="Activities::StructuredActivities::OutputPin")
Activities_StructuredActivities_ConditionalNode = Class(name="Activities::StructuredActivities::ConditionalNode")
Activities_StructuredActivities_ExecutableNode = Class(name="Activities::StructuredActivities::ExecutableNode")
ExceptionHandler = Class(name="ExceptionHandler")
Activities_StructuredActivities_Variable = Class(name="Activities::StructuredActivities::Variable")
StructuredActivities_MultiplicityElement = Class(name="StructuredActivities::MultiplicityElement")
Activities_StructuredActivities_MultiplicityElement = Class(name="Activities::StructuredActivities::MultiplicityElement", is_abstract=True)
Activities_StructuredActivities_LoopNode = Class(name="Activities::StructuredActivities::LoopNode")
ExecutableNode = Class(name="ExecutableNode")
Activities_CompleteStructuredActivities_InputPin = Class(name="Activities::CompleteStructuredActivities::InputPin")
Activities_ExtraStructuredActivities_ExceptionHandler = Class(name="Activities::ExtraStructuredActivities::ExceptionHandler")
Classifier = Class(name="Classifier")
Activities_ExtraStructuredActivities_Classifier = Class(name="Activities::ExtraStructuredActivities::Classifier", is_abstract=True)
Activities_ExtraStructuredActivities_ExpansionRegion = Class(name="Activities::ExtraStructuredActivities::ExpansionRegion")
Clause = Class(name="Clause")
Activities_StructuredActivities_Clause = Class(name="Activities::StructuredActivities::Clause")
Activities_StructuredActivities_SequenceNode = Class(name="Activities::StructuredActivities::SequenceNode")
ExpansionNode = Class(name="ExpansionNode")
Activities_ExtraStructuredActivities_ExpansionNode = Class(name="Activities::ExtraStructuredActivities::ExpansionNode")
ExpansionRegion = Class(name="ExpansionRegion")

# Activities_FundamentalActivities_Activity class attributes and methods
Activities_FundamentalActivities_Activity_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
Activities_FundamentalActivities_Activity_isSingleExecution: Property = Property(name="isSingleExecution", type=BooleanType)
Activities_FundamentalActivities_Activity.attributes={Activities_FundamentalActivities_Activity_isReadOnly, Activities_FundamentalActivities_Activity_isSingleExecution}

# InterruptibleActivityRegion class attributes and methods

# Behavior class attributes and methods

# ActivityNode class attributes and methods

# ActivityGroup class attributes and methods

# ActivityEdge class attributes and methods

# ActivityPartition class attributes and methods

# StructuredActivityNode class attributes and methods

# Variable class attributes and methods

# Activities_FundamentalActivities_Behavior class attributes and methods

# Class class attributes and methods

# ParameterSet class attributes and methods

# Activities_FundamentalActivities_NamedElement class attributes and methods

# Activities_FundamentalActivities_ActivityNode class attributes and methods

# FundamentalActivities_NamedElement class attributes and methods

# BasicActivities_RedefinableElement class attributes and methods

# Activities_BasicActivities_RedefinableElement class attributes and methods

# RedefinableElement class attributes and methods

# Activities_BasicActivities_ObjectNode class attributes and methods

# FundamentalActivities_ActivityNode class attributes and methods

# BasicActivities_TypedElement class attributes and methods

# Activities_BasicActivities_TypedElement class attributes and methods

# Activities_BasicActivities_Pin class attributes and methods
Activities_BasicActivities_Pin_isControl: Property = Property(name="isControl", type=BooleanType)
Activities_BasicActivities_Pin.attributes={Activities_BasicActivities_Pin_isControl}

# ObjectNode class attributes and methods

# Activities_BasicActivities_ActivityParameterNode class attributes and methods

# Parameter class attributes and methods

# Activities_FundamentalActivities_Action class attributes and methods
Activities_FundamentalActivities_Action_isLocallyReentrant: Property = Property(name="isLocallyReentrant", type=BooleanType)
Activities_FundamentalActivities_Action.attributes={Activities_FundamentalActivities_Action_isLocallyReentrant}

# Constraint class attributes and methods

# InputPin class attributes and methods

# OutputPin class attributes and methods

# Activities_FundamentalActivities_ActivityGroup class attributes and methods

# NamedElement class attributes and methods

# Activity class attributes and methods

# Activities_FundamentalActivities_Namespace class attributes and methods

# Activities_BasicActivities_ControlFlow class attributes and methods

# Activities_BasicActivities_ObjectFlow class attributes and methods
Activities_BasicActivities_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=BooleanType)
Activities_BasicActivities_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=BooleanType)
Activities_BasicActivities_ObjectFlow_ordering: Property = Property(name="ordering", type=StringType)
Activities_BasicActivities_ObjectFlow_isControlType: Property = Property(name="isControlType", type=BooleanType)
Activities_BasicActivities_ObjectFlow.attributes={Activities_BasicActivities_ObjectFlow_ordering, Activities_BasicActivities_ObjectFlow_isMultireceive, Activities_BasicActivities_ObjectFlow_isControlType, Activities_BasicActivities_ObjectFlow_isMulticast}

# Activities_BasicActivities_Parameter class attributes and methods
Activities_BasicActivities_Parameter_isException: Property = Property(name="isException", type=BooleanType)
Activities_BasicActivities_Parameter_isStream: Property = Property(name="isStream", type=BooleanType)
Activities_BasicActivities_Parameter_effect: Property = Property(name="effect", type=StringType)
Activities_BasicActivities_Parameter.attributes={Activities_BasicActivities_Parameter_isException, Activities_BasicActivities_Parameter_isStream, Activities_BasicActivities_Parameter_effect}

# Activities_BasicActivities_ControlNode class attributes and methods

# Activities_BasicActivities_ActivityFinalNode class attributes and methods

# BasicActivities_ControlNode class attributes and methods

# IntermediateActivities_FinalNode class attributes and methods

# Activities_BasicActivities_InitialNode class attributes and methods

# ControlNode class attributes and methods

# Activities_BasicActivities_ActivityEdge class attributes and methods

# ValueSpecification class attributes and methods

# Activities_IntermediateActivities_ValueSpecification class attributes and methods

# Activities_IntermediateActivities_ActivityPartition class attributes and methods

# Element class attributes and methods

# State class attributes and methods

# Activities_IntermediateActivities_CentralBufferNode class attributes and methods

# Activities_IntermediateActivities_FinalNode class attributes and methods

# Activities_IntermediateActivities_FlowFinalNode class attributes and methods

# FinalNode class attributes and methods

# Activities_IntermediateActivities_ForkNode class attributes and methods

# Activities_IntermediateActivities_JoinNode class attributes and methods
Activities_IntermediateActivities_JoinNode_isCombineDuplicate: Property = Property(name="isCombineDuplicate", type=BooleanType)
Activities_IntermediateActivities_JoinNode.attributes={Activities_IntermediateActivities_JoinNode_isCombineDuplicate}

# Activities_IntermediateActivities_MergeNode class attributes and methods

# Activities_IntermediateActivities_DecisionNode class attributes and methods

# ObjectFlow class attributes and methods

# Activities_StructuredActivities_StructuredActivityNode class attributes and methods
Activities_StructuredActivities_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
Activities_StructuredActivities_StructuredActivityNode.attributes={Activities_StructuredActivities_StructuredActivityNode_mustIsolate}

# StructuredActivities_ExecutableNode class attributes and methods

# FundamentalActivities_ActivityGroup class attributes and methods

# FundamentalActivities_Action class attributes and methods

# Activities_IntermediateActivities_Element class attributes and methods

# Activities_IntermediateActivities_Constraint class attributes and methods

# Activities_IntermediateActivities_State class attributes and methods

# Activities_IntermediateActivities_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# Activities_IntermediateActivities_ParameterSet class attributes and methods

# Activities_IntermediateActivities_BehavioralFeature class attributes and methods

# FundamentalActivities_Namespace class attributes and methods

# IntermediateActivities_Feature class attributes and methods

# Activities_IntermediateActivities_Feature class attributes and methods

# Activities_IntermediateActivities_Class class attributes and methods

# Activities_IntermediateActivities_InterruptibleActivityRegion class attributes and methods

# Activities_StructuredActivities_OutputPin class attributes and methods

# Activities_StructuredActivities_ConditionalNode class attributes and methods
Activities_StructuredActivities_ConditionalNode_isDeterminate: Property = Property(name="isDeterminate", type=BooleanType)
Activities_StructuredActivities_ConditionalNode_isAssumed: Property = Property(name="isAssumed", type=BooleanType)
Activities_StructuredActivities_ConditionalNode.attributes={Activities_StructuredActivities_ConditionalNode_isAssumed, Activities_StructuredActivities_ConditionalNode_isDeterminate}

# Activities_StructuredActivities_ExecutableNode class attributes and methods

# ExceptionHandler class attributes and methods

# Activities_StructuredActivities_Variable class attributes and methods

# StructuredActivities_MultiplicityElement class attributes and methods

# Activities_StructuredActivities_MultiplicityElement class attributes and methods

# Activities_StructuredActivities_LoopNode class attributes and methods
Activities_StructuredActivities_LoopNode_isTestedFirst: Property = Property(name="isTestedFirst", type=BooleanType)
Activities_StructuredActivities_LoopNode.attributes={Activities_StructuredActivities_LoopNode_isTestedFirst}

# ExecutableNode class attributes and methods

# Activities_CompleteStructuredActivities_InputPin class attributes and methods

# Activities_ExtraStructuredActivities_ExceptionHandler class attributes and methods

# Classifier class attributes and methods

# Activities_ExtraStructuredActivities_Classifier class attributes and methods

# Activities_ExtraStructuredActivities_ExpansionRegion class attributes and methods
Activities_ExtraStructuredActivities_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
Activities_ExtraStructuredActivities_ExpansionRegion.attributes={Activities_ExtraStructuredActivities_ExpansionRegion_mode}

# Clause class attributes and methods

# Activities_StructuredActivities_Clause class attributes and methods

# Activities_StructuredActivities_SequenceNode class attributes and methods

# ExpansionNode class attributes and methods

# Activities_ExtraStructuredActivities_ExpansionNode class attributes and methods

# ExpansionRegion class attributes and methods

# Relationships
inGroup10: BinaryAssociation = BinaryAssociation(
    name="inGroup10",
    ends={
        Property(name="FundamentalActivities12", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityGroup11", type=ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedNode13: BinaryAssociation = BinaryAssociation(
    name="redefinedNode13",
    ends={
        Property(name="ActivityNode14", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_ActivityNode", type=ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
incoming15: BinaryAssociation = BinaryAssociation(
    name="incoming15",
    ends={
        Property(name="BasicActivities", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdge16", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing17: BinaryAssociation = BinaryAssociation(
    name="outgoing17",
    ends={
        Property(name="BasicActivities19", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdge18", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition20: BinaryAssociation = BinaryAssociation(
    name="inPartition20",
    ends={
        Property(name="IntermediateActivities", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityPartition21", type=ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
inInterruptibleRegion22: BinaryAssociation = BinaryAssociation(
    name="inInterruptibleRegion22",
    ends={
        Property(name="IntermediateActivities23", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="InterruptibleActivityRegion", type=InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode24: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode24",
    ends={
        Property(name="StructuredActivities26", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="StructuredActivityNode25", type=StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="ActivityNode", type=Activities_FundamentalActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Activity", type=ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group1: BinaryAssociation = BinaryAssociation(
    name="group1",
    ends={
        Property(name="FundamentalActivities", type=Activities_FundamentalActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityGroup", type=ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge2: BinaryAssociation = BinaryAssociation(
    name="edge2",
    ends={
        Property(name="ActivityEdge", type=Activities_FundamentalActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Activity3", type=ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partition4: BinaryAssociation = BinaryAssociation(
    name="partition4",
    ends={
        Property(name="ActivityPartition", type=Activities_FundamentalActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Activity5", type=ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNode6: BinaryAssociation = BinaryAssociation(
    name="structuredNode6",
    ends={
        Property(name="StructuredActivities", type=Activities_FundamentalActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="StructuredActivityNode", type=StructuredActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable7: BinaryAssociation = BinaryAssociation(
    name="variable7",
    ends={
        Property(name="Variable", type=Activities_FundamentalActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Activity8", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameterSet9: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet9",
    ends={
        Property(name="ParameterSet", type=Activities_FundamentalActivities_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Behavior", type=ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedElement49: BinaryAssociation = BinaryAssociation(
    name="redefinedElement49",
    ends={
        Property(name="RedefinableElement", type=Activities_BasicActivities_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_RedefinableElement", type=RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
parameter50: BinaryAssociation = BinaryAssociation(
    name="parameter50",
    ends={
        Property(name="Parameter", type=Activities_BasicActivities_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ActivityParameterNode", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
localPrecondition27: BinaryAssociation = BinaryAssociation(
    name="localPrecondition27",
    ends={
        Property(name="Constraint", type=Activities_FundamentalActivities_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Action", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localPostcondition28: BinaryAssociation = BinaryAssociation(
    name="localPostcondition28",
    ends={
        Property(name="Constraint30", type=Activities_FundamentalActivities_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Action29", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input31: BinaryAssociation = BinaryAssociation(
    name="input31",
    ends={
        Property(name="InputPin", type=Activities_FundamentalActivities_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Action32", type=InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output33: BinaryAssociation = BinaryAssociation(
    name="output33",
    ends={
        Property(name="OutputPin", type=Activities_FundamentalActivities_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Action34", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subgroup35: BinaryAssociation = BinaryAssociation(
    name="subgroup35",
    ends={
        Property(name="FundamentalActivities37", type=Activities_FundamentalActivities_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityGroup36", type=ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superGroup38: BinaryAssociation = BinaryAssociation(
    name="superGroup38",
    ends={
        Property(name="FundamentalActivities40", type=Activities_FundamentalActivities_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityGroup39", type=ActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
inActivity41: BinaryAssociation = BinaryAssociation(
    name="inActivity41",
    ends={
        Property(name="FundamentalActivities42", type=Activities_FundamentalActivities_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="Activity", type=Activity, multiplicity=Multiplicity(0, 1))
    }
)
containedNode43: BinaryAssociation = BinaryAssociation(
    name="containedNode43",
    ends={
        Property(name="FundamentalActivities45", type=Activities_FundamentalActivities_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode44", type=ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
containedEdge46: BinaryAssociation = BinaryAssociation(
    name="containedEdge46",
    ends={
        Property(name="BasicActivities48", type=Activities_FundamentalActivities_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdge47", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
weight70: BinaryAssociation = BinaryAssociation(
    name="weight70",
    ends={
        Property(name="ValueSpecification72", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ActivityEdge71", type=ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interrupts73: BinaryAssociation = BinaryAssociation(
    name="interrupts73",
    ends={
        Property(name="IntermediateActivities75", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="InterruptibleActivityRegion74", type=InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode76: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode76",
    ends={
        Property(name="StructuredActivities78", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="StructuredActivityNode77", type=StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
transformation79: BinaryAssociation = BinaryAssociation(
    name="transformation79",
    ends={
        Property(name="Behavior", type=Activities_BasicActivities_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ObjectFlow", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
parameterSet51: BinaryAssociation = BinaryAssociation(
    name="parameterSet51",
    ends={
        Property(name="IntermediateActivities53", type=Activities_BasicActivities_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ParameterSet52", type=ParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
target54: BinaryAssociation = BinaryAssociation(
    name="target54",
    ends={
        Property(name="FundamentalActivities56", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode55", type=ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
source57: BinaryAssociation = BinaryAssociation(
    name="source57",
    ends={
        Property(name="FundamentalActivities59", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode58", type=ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
redefinedEdge60: BinaryAssociation = BinaryAssociation(
    name="redefinedEdge60",
    ends={
        Property(name="ActivityEdge61", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ActivityEdge", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inGroup62: BinaryAssociation = BinaryAssociation(
    name="inGroup62",
    ends={
        Property(name="FundamentalActivities64", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityGroup63", type=ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
guard65: BinaryAssociation = BinaryAssociation(
    name="guard65",
    ends={
        Property(name="ValueSpecification", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ActivityEdge66", type=ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPartition67: BinaryAssociation = BinaryAssociation(
    name="inPartition67",
    ends={
        Property(name="IntermediateActivities69", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityPartition68", type=ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
edge91: BinaryAssociation = BinaryAssociation(
    name="edge91",
    ends={
        Property(name="BasicActivities93", type=Activities_IntermediateActivities_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdge92", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
subpartition94: BinaryAssociation = BinaryAssociation(
    name="subpartition94",
    ends={
        Property(name="IntermediateActivities96", type=Activities_IntermediateActivities_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityPartition95", type=ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superPartition97: BinaryAssociation = BinaryAssociation(
    name="superPartition97",
    ends={
        Property(name="IntermediateActivities99", type=Activities_IntermediateActivities_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityPartition98", type=ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
represents100: BinaryAssociation = BinaryAssociation(
    name="represents100",
    ends={
        Property(name="Element", type=Activities_IntermediateActivities_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_ActivityPartition", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
selection80: BinaryAssociation = BinaryAssociation(
    name="selection80",
    ends={
        Property(name="Behavior82", type=Activities_BasicActivities_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ObjectFlow81", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
inState83: BinaryAssociation = BinaryAssociation(
    name="inState83",
    ends={
        Property(name="State", type=Activities_BasicActivities_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ObjectFlow84", type=State, multiplicity=Multiplicity(0, 9999))
    }
)
joinSpec85: BinaryAssociation = BinaryAssociation(
    name="joinSpec85",
    ends={
        Property(name="ValueSpecification86", type=Activities_IntermediateActivities_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_JoinNode", type=ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
decisionInputFlow87: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow87",
    ends={
        Property(name="ObjectFlow", type=Activities_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_DecisionNode", type=ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
decisionInput88: BinaryAssociation = BinaryAssociation(
    name="decisionInput88",
    ends={
        Property(name="Behavior90", type=Activities_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_DecisionNode89", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
node114: BinaryAssociation = BinaryAssociation(
    name="node114",
    ends={
        Property(name="FundamentalActivities116", type=Activities_IntermediateActivities_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode115", type=ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
activity117: BinaryAssociation = BinaryAssociation(
    name="activity117",
    ends={
        Property(name="FundamentalActivities119", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activity118", type=Activity, multiplicity=Multiplicity(0, 1))
    }
)
variable120: BinaryAssociation = BinaryAssociation(
    name="variable120",
    ends={
        Property(name="Variable121", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_StructuredActivityNode", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node122: BinaryAssociation = BinaryAssociation(
    name="node122",
    ends={
        Property(name="FundamentalActivities124", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode123", type=ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node101: BinaryAssociation = BinaryAssociation(
    name="node101",
    ends={
        Property(name="FundamentalActivities103", type=Activities_IntermediateActivities_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode102", type=ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
parameter104: BinaryAssociation = BinaryAssociation(
    name="parameter104",
    ends={
        Property(name="BasicActivities106", type=Activities_IntermediateActivities_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter105", type=Parameter_, multiplicity=Multiplicity(1, 9999))
    }
)
condition107: BinaryAssociation = BinaryAssociation(
    name="condition107",
    ends={
        Property(name="Constraint108", type=Activities_IntermediateActivities_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_ParameterSet", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameterSet109: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet109",
    ends={
        Property(name="ParameterSet110", type=Activities_IntermediateActivities_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_BehavioralFeature", type=ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interruptingEdge111: BinaryAssociation = BinaryAssociation(
    name="interruptingEdge111",
    ends={
        Property(name="BasicActivities113", type=Activities_IntermediateActivities_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdge112", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
bodyPart136: BinaryAssociation = BinaryAssociation(
    name="bodyPart136",
    ends={
        Property(name="ExecutableNode138", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode137", type=ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test139: BinaryAssociation = BinaryAssociation(
    name="test139",
    ends={
        Property(name="ExecutableNode141", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode140", type=ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
decider142: BinaryAssociation = BinaryAssociation(
    name="decider142",
    ends={
        Property(name="OutputPin144", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode143", type=OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
loopVariableInput145: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput145",
    ends={
        Property(name="InputPin147", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode146", type=InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable148: BinaryAssociation = BinaryAssociation(
    name="loopVariable148",
    ends={
        Property(name="OutputPin150", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode149", type=OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
bodyOutput151: BinaryAssociation = BinaryAssociation(
    name="bodyOutput151",
    ends={
        Property(name="OutputPin153", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode152", type=OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
result154: BinaryAssociation = BinaryAssociation(
    name="result154",
    ends={
        Property(name="OutputPin156", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode155", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeInput125: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput125",
    ends={
        Property(name="InputPin127", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_StructuredActivityNode126", type=InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge128: BinaryAssociation = BinaryAssociation(
    name="edge128",
    ends={
        Property(name="BasicActivities130", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdge129", type=ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeOutput131: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput131",
    ends={
        Property(name="OutputPin133", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_StructuredActivityNode132", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handler134: BinaryAssociation = BinaryAssociation(
    name="handler134",
    ends={
        Property(name="ExtraStructuredActivities", type=Activities_StructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ExceptionHandler", type=ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setupPart135: BinaryAssociation = BinaryAssociation(
    name="setupPart135",
    ends={
        Property(name="ExecutableNode", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode", type=ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
handlerBody177: BinaryAssociation = BinaryAssociation(
    name="handlerBody177",
    ends={
        Property(name="ExecutableNode178", type=Activities_ExtraStructuredActivities_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_ExtraStructuredActivities_ExceptionHandler", type=ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
protectedNode179: BinaryAssociation = BinaryAssociation(
    name="protectedNode179",
    ends={
        Property(name="StructuredActivities181", type=Activities_ExtraStructuredActivities_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="ExecutableNode180", type=ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionInput182: BinaryAssociation = BinaryAssociation(
    name="exceptionInput182",
    ends={
        Property(name="ObjectNode", type=Activities_ExtraStructuredActivities_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_ExtraStructuredActivities_ExceptionHandler183", type=ObjectNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionType184: BinaryAssociation = BinaryAssociation(
    name="exceptionType184",
    ends={
        Property(name="Classifier", type=Activities_ExtraStructuredActivities_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_ExtraStructuredActivities_ExceptionHandler185", type=Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
clause157: BinaryAssociation = BinaryAssociation(
    name="clause157",
    ends={
        Property(name="Clause", type=Activities_StructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_ConditionalNode", type=Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
test158: BinaryAssociation = BinaryAssociation(
    name="test158",
    ends={
        Property(name="ExecutableNode160", type=Activities_StructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_ConditionalNode159", type=ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body161: BinaryAssociation = BinaryAssociation(
    name="body161",
    ends={
        Property(name="ExecutableNode163", type=Activities_StructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_ConditionalNode162", type=ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
result164: BinaryAssociation = BinaryAssociation(
    name="result164",
    ends={
        Property(name="OutputPin166", type=Activities_StructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_ConditionalNode165", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessorClause167: BinaryAssociation = BinaryAssociation(
    name="predecessorClause167",
    ends={
        Property(name="StructuredActivities169", type=Activities_StructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Clause168", type=Clause, multiplicity=Multiplicity(0, 9999))
    }
)
sucessorClause170: BinaryAssociation = BinaryAssociation(
    name="sucessorClause170",
    ends={
        Property(name="StructuredActivities172", type=Activities_StructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Clause171", type=Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider173: BinaryAssociation = BinaryAssociation(
    name="decider173",
    ends={
        Property(name="OutputPin174", type=Activities_StructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_Clause", type=OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
executableNode175: BinaryAssociation = BinaryAssociation(
    name="executableNode175",
    ends={
        Property(name="ExecutableNode176", type=Activities_StructuredActivities_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_SequenceNode", type=ExecutableNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputElement186: BinaryAssociation = BinaryAssociation(
    name="inputElement186",
    ends={
        Property(name="ExtraStructuredActivities187", type=Activities_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ExpansionNode", type=ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement188: BinaryAssociation = BinaryAssociation(
    name="outputElement188",
    ends={
        Property(name="ExtraStructuredActivities190", type=Activities_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ExpansionNode189", type=ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
regionAsInput191: BinaryAssociation = BinaryAssociation(
    name="regionAsInput191",
    ends={
        Property(name="ExtraStructuredActivities192", type=Activities_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ExpansionRegion", type=ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsOutput193: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput193",
    ends={
        Property(name="ExtraStructuredActivities195", type=Activities_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ExpansionRegion194", type=ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Activities_FundamentalActivities_Activity_Behavior = Generalization(general=Behavior, specific=Activities_FundamentalActivities_Activity)
gen_Activities_FundamentalActivities_Behavior_Class = Generalization(general=Class_, specific=Activities_FundamentalActivities_Behavior)
gen_Activities_FundamentalActivities_ActivityNode_FundamentalActivities_NamedElement = Generalization(general=FundamentalActivities_NamedElement, specific=Activities_FundamentalActivities_ActivityNode)
gen_Activities_FundamentalActivities_ActivityNode_BasicActivities_RedefinableElement = Generalization(general=BasicActivities_RedefinableElement, specific=Activities_FundamentalActivities_ActivityNode)
gen_Activities_BasicActivities_ObjectNode_FundamentalActivities_ActivityNode = Generalization(general=FundamentalActivities_ActivityNode, specific=Activities_BasicActivities_ObjectNode)
gen_Activities_BasicActivities_ObjectNode_BasicActivities_TypedElement = Generalization(general=BasicActivities_TypedElement, specific=Activities_BasicActivities_ObjectNode)
gen_Activities_BasicActivities_Pin_ObjectNode = Generalization(general=ObjectNode, specific=Activities_BasicActivities_Pin)
gen_Activities_BasicActivities_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=Activities_BasicActivities_ActivityParameterNode)
gen_Activities_FundamentalActivities_Action_ActivityNode = Generalization(general=ActivityNode, specific=Activities_FundamentalActivities_Action)
gen_Activities_FundamentalActivities_ActivityGroup_NamedElement = Generalization(general=NamedElement, specific=Activities_FundamentalActivities_ActivityGroup)
gen_Activities_BasicActivities_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=Activities_BasicActivities_ControlFlow)
gen_Activities_BasicActivities_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=Activities_BasicActivities_ObjectFlow)
gen_Activities_BasicActivities_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=Activities_BasicActivities_ControlNode)
gen_Activities_BasicActivities_ActivityFinalNode_BasicActivities_ControlNode = Generalization(general=BasicActivities_ControlNode, specific=Activities_BasicActivities_ActivityFinalNode)
gen_Activities_BasicActivities_ActivityFinalNode_IntermediateActivities_FinalNode = Generalization(general=IntermediateActivities_FinalNode, specific=Activities_BasicActivities_ActivityFinalNode)
gen_Activities_BasicActivities_InitialNode_ControlNode = Generalization(general=ControlNode, specific=Activities_BasicActivities_InitialNode)
gen_Activities_BasicActivities_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=Activities_BasicActivities_ActivityEdge)
gen_Activities_IntermediateActivities_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=Activities_IntermediateActivities_ActivityPartition)
gen_Activities_IntermediateActivities_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=Activities_IntermediateActivities_CentralBufferNode)
gen_Activities_IntermediateActivities_FinalNode_ControlNode = Generalization(general=ControlNode, specific=Activities_IntermediateActivities_FinalNode)
gen_Activities_IntermediateActivities_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=Activities_IntermediateActivities_FlowFinalNode)
gen_Activities_IntermediateActivities_ForkNode_ControlNode = Generalization(general=ControlNode, specific=Activities_IntermediateActivities_ForkNode)
gen_Activities_IntermediateActivities_JoinNode_ControlNode = Generalization(general=ControlNode, specific=Activities_IntermediateActivities_JoinNode)
gen_Activities_IntermediateActivities_MergeNode_ControlNode = Generalization(general=ControlNode, specific=Activities_IntermediateActivities_MergeNode)
gen_Activities_IntermediateActivities_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=Activities_IntermediateActivities_DecisionNode)
gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_Namespace = Generalization(general=FundamentalActivities_Namespace, specific=Activities_StructuredActivities_StructuredActivityNode)
gen_Activities_StructuredActivities_StructuredActivityNode_StructuredActivities_ExecutableNode = Generalization(general=StructuredActivities_ExecutableNode, specific=Activities_StructuredActivities_StructuredActivityNode)
gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_ActivityGroup = Generalization(general=FundamentalActivities_ActivityGroup, specific=Activities_StructuredActivities_StructuredActivityNode)
gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_Action = Generalization(general=FundamentalActivities_Action, specific=Activities_StructuredActivities_StructuredActivityNode)
gen_Activities_IntermediateActivities_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=Activities_IntermediateActivities_DataStoreNode)
gen_Activities_IntermediateActivities_ParameterSet_NamedElement = Generalization(general=NamedElement, specific=Activities_IntermediateActivities_ParameterSet)
gen_Activities_IntermediateActivities_BehavioralFeature_FundamentalActivities_Namespace = Generalization(general=FundamentalActivities_Namespace, specific=Activities_IntermediateActivities_BehavioralFeature)
gen_Activities_IntermediateActivities_BehavioralFeature_IntermediateActivities_Feature = Generalization(general=IntermediateActivities_Feature, specific=Activities_IntermediateActivities_BehavioralFeature)
gen_Activities_IntermediateActivities_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=Activities_IntermediateActivities_InterruptibleActivityRegion)
gen_Activities_StructuredActivities_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=Activities_StructuredActivities_ConditionalNode)
gen_Activities_StructuredActivities_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=Activities_StructuredActivities_ExecutableNode)
gen_Activities_StructuredActivities_Variable_StructuredActivities_MultiplicityElement = Generalization(general=StructuredActivities_MultiplicityElement, specific=Activities_StructuredActivities_Variable)
gen_Activities_StructuredActivities_Variable_BasicActivities_TypedElement = Generalization(general=BasicActivities_TypedElement, specific=Activities_StructuredActivities_Variable)
gen_Activities_StructuredActivities_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=Activities_StructuredActivities_LoopNode)
gen_Activities_ExtraStructuredActivities_ExceptionHandler_Element = Generalization(general=Element, specific=Activities_ExtraStructuredActivities_ExceptionHandler)
gen_Activities_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=Activities_ExtraStructuredActivities_ExpansionRegion)
gen_Activities_StructuredActivities_Clause_Element = Generalization(general=Element, specific=Activities_StructuredActivities_Clause)
gen_Activities_StructuredActivities_SequenceNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=Activities_StructuredActivities_SequenceNode)
gen_Activities_ExtraStructuredActivities_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=Activities_ExtraStructuredActivities_ExpansionNode)

# Domain Model
domain_model = DomainModel(
    name="Activities",
    types={Activities_FundamentalActivities_Activity, InterruptibleActivityRegion, Behavior, ActivityNode, ActivityGroup, ActivityEdge, ActivityPartition, StructuredActivityNode, Variable, Activities_FundamentalActivities_Behavior, Class_, ParameterSet, Activities_FundamentalActivities_NamedElement, Activities_FundamentalActivities_ActivityNode, FundamentalActivities_NamedElement, BasicActivities_RedefinableElement, Activities_BasicActivities_RedefinableElement, RedefinableElement, Activities_BasicActivities_ObjectNode, FundamentalActivities_ActivityNode, BasicActivities_TypedElement, Activities_BasicActivities_TypedElement, Activities_BasicActivities_Pin, ObjectNode, Activities_BasicActivities_ActivityParameterNode, Parameter_, Activities_FundamentalActivities_Action, Constraint, InputPin, OutputPin, Activities_FundamentalActivities_ActivityGroup, NamedElement, Activity, Activities_FundamentalActivities_Namespace, Activities_BasicActivities_ControlFlow, Activities_BasicActivities_ObjectFlow, Activities_BasicActivities_Parameter, Activities_BasicActivities_ControlNode, Activities_BasicActivities_ActivityFinalNode, BasicActivities_ControlNode, IntermediateActivities_FinalNode, Activities_BasicActivities_InitialNode, ControlNode, Activities_BasicActivities_ActivityEdge, ValueSpecification, Activities_IntermediateActivities_ValueSpecification, Activities_IntermediateActivities_ActivityPartition, Element, State, Activities_IntermediateActivities_CentralBufferNode, Activities_IntermediateActivities_FinalNode, Activities_IntermediateActivities_FlowFinalNode, FinalNode, Activities_IntermediateActivities_ForkNode, Activities_IntermediateActivities_JoinNode, Activities_IntermediateActivities_MergeNode, Activities_IntermediateActivities_DecisionNode, ObjectFlow, Activities_StructuredActivities_StructuredActivityNode, StructuredActivities_ExecutableNode, FundamentalActivities_ActivityGroup, FundamentalActivities_Action, Activities_IntermediateActivities_Element, Activities_IntermediateActivities_Constraint, Activities_IntermediateActivities_State, Activities_IntermediateActivities_DataStoreNode, CentralBufferNode, Activities_IntermediateActivities_ParameterSet, Activities_IntermediateActivities_BehavioralFeature, FundamentalActivities_Namespace, IntermediateActivities_Feature, Activities_IntermediateActivities_Feature, Activities_IntermediateActivities_Class, Activities_IntermediateActivities_InterruptibleActivityRegion, Activities_StructuredActivities_OutputPin, Activities_StructuredActivities_ConditionalNode, Activities_StructuredActivities_ExecutableNode, ExceptionHandler, Activities_StructuredActivities_Variable, StructuredActivities_MultiplicityElement, Activities_StructuredActivities_MultiplicityElement, Activities_StructuredActivities_LoopNode, ExecutableNode, Activities_CompleteStructuredActivities_InputPin, Activities_ExtraStructuredActivities_ExceptionHandler, Classifier, Activities_ExtraStructuredActivities_Classifier, Activities_ExtraStructuredActivities_ExpansionRegion, Clause, Activities_StructuredActivities_Clause, Activities_StructuredActivities_SequenceNode, ExpansionNode, Activities_ExtraStructuredActivities_ExpansionNode, ExpansionRegion, ObjectNodeOrderingKind, ParameterEffectKind, ExpansionKind},
    associations={inGroup10, redefinedNode13, incoming15, outgoing17, inPartition20, inInterruptibleRegion22, inStructuredNode24, node0, group1, edge2, partition4, structuredNode6, variable7, ownedParameterSet9, redefinedElement49, parameter50, localPrecondition27, localPostcondition28, input31, output33, subgroup35, superGroup38, inActivity41, containedNode43, containedEdge46, weight70, interrupts73, inStructuredNode76, transformation79, parameterSet51, target54, source57, redefinedEdge60, inGroup62, guard65, inPartition67, edge91, subpartition94, superPartition97, represents100, selection80, inState83, joinSpec85, decisionInputFlow87, decisionInput88, node114, activity117, variable120, node122, node101, parameter104, condition107, ownedParameterSet109, interruptingEdge111, bodyPart136, test139, decider142, loopVariableInput145, loopVariable148, bodyOutput151, result154, structuredNodeInput125, edge128, structuredNodeOutput131, handler134, setupPart135, handlerBody177, protectedNode179, exceptionInput182, exceptionType184, clause157, test158, body161, result164, predecessorClause167, sucessorClause170, decider173, executableNode175, inputElement186, outputElement188, regionAsInput191, regionAsOutput193},
    generalizations={gen_Activities_FundamentalActivities_Activity_Behavior, gen_Activities_FundamentalActivities_Behavior_Class, gen_Activities_FundamentalActivities_ActivityNode_FundamentalActivities_NamedElement, gen_Activities_FundamentalActivities_ActivityNode_BasicActivities_RedefinableElement, gen_Activities_BasicActivities_ObjectNode_FundamentalActivities_ActivityNode, gen_Activities_BasicActivities_ObjectNode_BasicActivities_TypedElement, gen_Activities_BasicActivities_Pin_ObjectNode, gen_Activities_BasicActivities_ActivityParameterNode_ObjectNode, gen_Activities_FundamentalActivities_Action_ActivityNode, gen_Activities_FundamentalActivities_ActivityGroup_NamedElement, gen_Activities_BasicActivities_ControlFlow_ActivityEdge, gen_Activities_BasicActivities_ObjectFlow_ActivityEdge, gen_Activities_BasicActivities_ControlNode_ActivityNode, gen_Activities_BasicActivities_ActivityFinalNode_BasicActivities_ControlNode, gen_Activities_BasicActivities_ActivityFinalNode_IntermediateActivities_FinalNode, gen_Activities_BasicActivities_InitialNode_ControlNode, gen_Activities_BasicActivities_ActivityEdge_RedefinableElement, gen_Activities_IntermediateActivities_ActivityPartition_ActivityGroup, gen_Activities_IntermediateActivities_CentralBufferNode_ObjectNode, gen_Activities_IntermediateActivities_FinalNode_ControlNode, gen_Activities_IntermediateActivities_FlowFinalNode_FinalNode, gen_Activities_IntermediateActivities_ForkNode_ControlNode, gen_Activities_IntermediateActivities_JoinNode_ControlNode, gen_Activities_IntermediateActivities_MergeNode_ControlNode, gen_Activities_IntermediateActivities_DecisionNode_ControlNode, gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_Namespace, gen_Activities_StructuredActivities_StructuredActivityNode_StructuredActivities_ExecutableNode, gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_ActivityGroup, gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_Action, gen_Activities_IntermediateActivities_DataStoreNode_CentralBufferNode, gen_Activities_IntermediateActivities_ParameterSet_NamedElement, gen_Activities_IntermediateActivities_BehavioralFeature_FundamentalActivities_Namespace, gen_Activities_IntermediateActivities_BehavioralFeature_IntermediateActivities_Feature, gen_Activities_IntermediateActivities_InterruptibleActivityRegion_ActivityGroup, gen_Activities_StructuredActivities_ConditionalNode_StructuredActivityNode, gen_Activities_StructuredActivities_ExecutableNode_ActivityNode, gen_Activities_StructuredActivities_Variable_StructuredActivities_MultiplicityElement, gen_Activities_StructuredActivities_Variable_BasicActivities_TypedElement, gen_Activities_StructuredActivities_LoopNode_StructuredActivityNode, gen_Activities_ExtraStructuredActivities_ExceptionHandler_Element, gen_Activities_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode, gen_Activities_StructuredActivities_Clause_Element, gen_Activities_StructuredActivities_SequenceNode_StructuredActivityNode, gen_Activities_ExtraStructuredActivities_ExpansionNode_ObjectNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)