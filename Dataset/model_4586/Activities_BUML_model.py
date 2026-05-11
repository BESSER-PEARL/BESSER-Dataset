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
StructuredActivityNode = Class(name="StructuredActivityNode")
Variable = Class(name="Variable")
Activities_FundamentalActivities_Behavior = Class(name="Activities_FundamentalActivities_Behavior", is_abstract=True)
Class_ = Class(name="Class")
ParameterSet = Class(name="ParameterSet")
Activities_FundamentalActivities_NamedElement = Class(name="Activities_FundamentalActivities_NamedElement", is_abstract=True)
Activities_FundamentalActivities_ActivityNode = Class(name="Activities_FundamentalActivities_ActivityNode", is_abstract=True)
FundamentalActivities_NamedElement = Class(name="FundamentalActivities_NamedElement")
BasicActivities_RedefinableElement = Class(name="BasicActivities_RedefinableElement")
Activities_FundamentalActivities_Activity = Class(name="Activities_FundamentalActivities_Activity")
Behavior = Class(name="Behavior")
ActivityNode = Class(name="ActivityNode")
ActivityGroup = Class(name="ActivityGroup")
ActivityEdge = Class(name="ActivityEdge")
ActivityPartition = Class(name="ActivityPartition")
NamedElement = Class(name="NamedElement")
Activity = Class(name="Activity")
Activities_FundamentalActivities_Namespace = Class(name="Activities_FundamentalActivities_Namespace", is_abstract=True)
Activities_BasicActivities_RedefinableElement = Class(name="Activities_BasicActivities_RedefinableElement", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Activities_BasicActivities_ObjectNode = Class(name="Activities_BasicActivities_ObjectNode", is_abstract=True)
FundamentalActivities_ActivityNode = Class(name="FundamentalActivities_ActivityNode")
InterruptibleActivityRegion = Class(name="InterruptibleActivityRegion")
Activities_FundamentalActivities_Action = Class(name="Activities_FundamentalActivities_Action")
Constraint = Class(name="Constraint")
InputPin = Class(name="InputPin")
OutputPin = Class(name="OutputPin")
Activities_FundamentalActivities_ActivityGroup = Class(name="Activities_FundamentalActivities_ActivityGroup", is_abstract=True)
ValueSpecification = Class(name="ValueSpecification")
Activities_BasicActivities_ControlFlow = Class(name="Activities_BasicActivities_ControlFlow")
Activities_BasicActivities_ObjectFlow = Class(name="Activities_BasicActivities_ObjectFlow")
BasicActivities_TypedElement = Class(name="BasicActivities_TypedElement")
Activities_BasicActivities_TypedElement = Class(name="Activities_BasicActivities_TypedElement")
Activities_BasicActivities_Pin = Class(name="Activities_BasicActivities_Pin", is_abstract=True)
ObjectNode = Class(name="ObjectNode")
Activities_BasicActivities_ActivityParameterNode = Class(name="Activities_BasicActivities_ActivityParameterNode")
Parameter_ = Class(name="Parameter")
Activities_BasicActivities_Parameter = Class(name="Activities_BasicActivities_Parameter")
Activities_BasicActivities_ControlNode = Class(name="Activities_BasicActivities_ControlNode", is_abstract=True)
Activities_BasicActivities_ActivityFinalNode = Class(name="Activities_BasicActivities_ActivityFinalNode")
BasicActivities_ControlNode = Class(name="BasicActivities_ControlNode")
IntermediateActivities_FinalNode = Class(name="IntermediateActivities_FinalNode")
Activities_BasicActivities_InitialNode = Class(name="Activities_BasicActivities_InitialNode")
ControlNode = Class(name="ControlNode")
Activities_BasicActivities_ActivityEdge = Class(name="Activities_BasicActivities_ActivityEdge", is_abstract=True)
Activities_IntermediateActivities_MergeNode = Class(name="Activities_IntermediateActivities_MergeNode")
Activities_IntermediateActivities_DecisionNode = Class(name="Activities_IntermediateActivities_DecisionNode")
ObjectFlow = Class(name="ObjectFlow")
Activities_IntermediateActivities_ValueSpecification = Class(name="Activities_IntermediateActivities_ValueSpecification", is_abstract=True)
Activities_IntermediateActivities_ActivityPartition = Class(name="Activities_IntermediateActivities_ActivityPartition")
Element = Class(name="Element")
State = Class(name="State")
Activities_IntermediateActivities_CentralBufferNode = Class(name="Activities_IntermediateActivities_CentralBufferNode")
Activities_IntermediateActivities_FinalNode = Class(name="Activities_IntermediateActivities_FinalNode", is_abstract=True)
Activities_IntermediateActivities_FlowFinalNode = Class(name="Activities_IntermediateActivities_FlowFinalNode")
FinalNode = Class(name="FinalNode")
Activities_IntermediateActivities_ForkNode = Class(name="Activities_IntermediateActivities_ForkNode")
Activities_IntermediateActivities_JoinNode = Class(name="Activities_IntermediateActivities_JoinNode")
Activities_IntermediateActivities_Feature = Class(name="Activities_IntermediateActivities_Feature", is_abstract=True)
Activities_IntermediateActivities_Class = Class(name="Activities_IntermediateActivities_Class")
Activities_IntermediateActivities_InterruptibleActivityRegion = Class(name="Activities_IntermediateActivities_InterruptibleActivityRegion")
Activities_StructuredActivities_StructuredActivityNode = Class(name="Activities_StructuredActivities_StructuredActivityNode")
StructuredActivities_ExecutableNode = Class(name="StructuredActivities_ExecutableNode")
FundamentalActivities_ActivityGroup = Class(name="FundamentalActivities_ActivityGroup")
FundamentalActivities_Action = Class(name="FundamentalActivities_Action")
Activities_IntermediateActivities_Element = Class(name="Activities_IntermediateActivities_Element", is_abstract=True)
Activities_IntermediateActivities_Constraint = Class(name="Activities_IntermediateActivities_Constraint")
Activities_IntermediateActivities_State = Class(name="Activities_IntermediateActivities_State")
Activities_IntermediateActivities_DataStoreNode = Class(name="Activities_IntermediateActivities_DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
Activities_IntermediateActivities_ParameterSet = Class(name="Activities_IntermediateActivities_ParameterSet")
Activities_IntermediateActivities_BehavioralFeature = Class(name="Activities_IntermediateActivities_BehavioralFeature", is_abstract=True)
FundamentalActivities_Namespace = Class(name="FundamentalActivities_Namespace")
IntermediateActivities_Feature = Class(name="IntermediateActivities_Feature")
Activities_StructuredActivities_ExecutableNode = Class(name="Activities_StructuredActivities_ExecutableNode")
ExceptionHandler = Class(name="ExceptionHandler")
Activities_StructuredActivities_Variable = Class(name="Activities_StructuredActivities_Variable")
StructuredActivities_MultiplicityElement = Class(name="StructuredActivities_MultiplicityElement")
Activities_StructuredActivities_OutputPin = Class(name="Activities_StructuredActivities_OutputPin")
Activities_StructuredActivities_MultiplicityElement = Class(name="Activities_StructuredActivities_MultiplicityElement", is_abstract=True)
Activities_StructuredActivities_ConditionalNode = Class(name="Activities_StructuredActivities_ConditionalNode")
Activities_StructuredActivities_LoopNode = Class(name="Activities_StructuredActivities_LoopNode")
Clause = Class(name="Clause")
Activities_StructuredActivities_Clause = Class(name="Activities_StructuredActivities_Clause")
Activities_StructuredActivities_SequenceNode = Class(name="Activities_StructuredActivities_SequenceNode")
ExecutableNode = Class(name="ExecutableNode")
Activities_CompleteStructuredActivities_InputPin = Class(name="Activities_CompleteStructuredActivities_InputPin")
Activities_ExtraStructuredActivities_ExceptionHandler = Class(name="Activities_ExtraStructuredActivities_ExceptionHandler")
Classifier = Class(name="Classifier")
Activities_ExtraStructuredActivities_Classifier = Class(name="Activities_ExtraStructuredActivities_Classifier", is_abstract=True)
Activities_ExtraStructuredActivities_ExpansionRegion = Class(name="Activities_ExtraStructuredActivities_ExpansionRegion")
ExpansionNode = Class(name="ExpansionNode")
Activities_ExtraStructuredActivities_ExpansionNode = Class(name="Activities_ExtraStructuredActivities_ExpansionNode")
ExpansionRegion = Class(name="ExpansionRegion")

# StructuredActivityNode class attributes and methods

# Variable class attributes and methods

# Activities_FundamentalActivities_Behavior class attributes and methods

# Class class attributes and methods

# ParameterSet class attributes and methods

# Activities_FundamentalActivities_NamedElement class attributes and methods

# Activities_FundamentalActivities_ActivityNode class attributes and methods

# FundamentalActivities_NamedElement class attributes and methods

# BasicActivities_RedefinableElement class attributes and methods

# Activities_FundamentalActivities_Activity class attributes and methods
Activities_FundamentalActivities_Activity_isSingleExecution: Property = Property(name="isSingleExecution", type=BooleanType)
Activities_FundamentalActivities_Activity_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
Activities_FundamentalActivities_Activity.attributes={Activities_FundamentalActivities_Activity_isSingleExecution, Activities_FundamentalActivities_Activity_isReadOnly}

# Behavior class attributes and methods

# ActivityNode class attributes and methods

# ActivityGroup class attributes and methods

# ActivityEdge class attributes and methods

# ActivityPartition class attributes and methods

# NamedElement class attributes and methods

# Activity class attributes and methods

# Activities_FundamentalActivities_Namespace class attributes and methods

# Activities_BasicActivities_RedefinableElement class attributes and methods

# RedefinableElement class attributes and methods

# Activities_BasicActivities_ObjectNode class attributes and methods

# FundamentalActivities_ActivityNode class attributes and methods

# InterruptibleActivityRegion class attributes and methods

# Activities_FundamentalActivities_Action class attributes and methods
Activities_FundamentalActivities_Action_isLocallyReentrant: Property = Property(name="isLocallyReentrant", type=BooleanType)
Activities_FundamentalActivities_Action.attributes={Activities_FundamentalActivities_Action_isLocallyReentrant}

# Constraint class attributes and methods

# InputPin class attributes and methods

# OutputPin class attributes and methods

# Activities_FundamentalActivities_ActivityGroup class attributes and methods

# ValueSpecification class attributes and methods

# Activities_BasicActivities_ControlFlow class attributes and methods

# Activities_BasicActivities_ObjectFlow class attributes and methods
Activities_BasicActivities_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=BooleanType)
Activities_BasicActivities_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=BooleanType)
Activities_BasicActivities_ObjectFlow_ordering: Property = Property(name="ordering", type=StringType)
Activities_BasicActivities_ObjectFlow_isControlType: Property = Property(name="isControlType", type=BooleanType)
Activities_BasicActivities_ObjectFlow.attributes={Activities_BasicActivities_ObjectFlow_isMulticast, Activities_BasicActivities_ObjectFlow_ordering, Activities_BasicActivities_ObjectFlow_isControlType, Activities_BasicActivities_ObjectFlow_isMultireceive}

# BasicActivities_TypedElement class attributes and methods

# Activities_BasicActivities_TypedElement class attributes and methods

# Activities_BasicActivities_Pin class attributes and methods
Activities_BasicActivities_Pin_isControl: Property = Property(name="isControl", type=BooleanType)
Activities_BasicActivities_Pin.attributes={Activities_BasicActivities_Pin_isControl}

# ObjectNode class attributes and methods

# Activities_BasicActivities_ActivityParameterNode class attributes and methods

# Parameter class attributes and methods

# Activities_BasicActivities_Parameter class attributes and methods
Activities_BasicActivities_Parameter_isException: Property = Property(name="isException", type=BooleanType)
Activities_BasicActivities_Parameter_isStream: Property = Property(name="isStream", type=BooleanType)
Activities_BasicActivities_Parameter_effect: Property = Property(name="effect", type=StringType)
Activities_BasicActivities_Parameter.attributes={Activities_BasicActivities_Parameter_isStream, Activities_BasicActivities_Parameter_isException, Activities_BasicActivities_Parameter_effect}

# Activities_BasicActivities_ControlNode class attributes and methods

# Activities_BasicActivities_ActivityFinalNode class attributes and methods

# BasicActivities_ControlNode class attributes and methods

# IntermediateActivities_FinalNode class attributes and methods

# Activities_BasicActivities_InitialNode class attributes and methods

# ControlNode class attributes and methods

# Activities_BasicActivities_ActivityEdge class attributes and methods

# Activities_IntermediateActivities_MergeNode class attributes and methods

# Activities_IntermediateActivities_DecisionNode class attributes and methods

# ObjectFlow class attributes and methods

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

# Activities_IntermediateActivities_Feature class attributes and methods

# Activities_IntermediateActivities_Class class attributes and methods

# Activities_IntermediateActivities_InterruptibleActivityRegion class attributes and methods

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

# Activities_StructuredActivities_ExecutableNode class attributes and methods

# ExceptionHandler class attributes and methods

# Activities_StructuredActivities_Variable class attributes and methods

# StructuredActivities_MultiplicityElement class attributes and methods

# Activities_StructuredActivities_OutputPin class attributes and methods

# Activities_StructuredActivities_MultiplicityElement class attributes and methods

# Activities_StructuredActivities_ConditionalNode class attributes and methods
Activities_StructuredActivities_ConditionalNode_isDeterminate: Property = Property(name="isDeterminate", type=BooleanType)
Activities_StructuredActivities_ConditionalNode_isAssumed: Property = Property(name="isAssumed", type=BooleanType)
Activities_StructuredActivities_ConditionalNode.attributes={Activities_StructuredActivities_ConditionalNode_isDeterminate, Activities_StructuredActivities_ConditionalNode_isAssumed}

# Activities_StructuredActivities_LoopNode class attributes and methods
Activities_StructuredActivities_LoopNode_isTestedFirst: Property = Property(name="isTestedFirst", type=BooleanType)
Activities_StructuredActivities_LoopNode.attributes={Activities_StructuredActivities_LoopNode_isTestedFirst}

# Clause class attributes and methods

# Activities_StructuredActivities_Clause class attributes and methods

# Activities_StructuredActivities_SequenceNode class attributes and methods

# ExecutableNode class attributes and methods

# Activities_CompleteStructuredActivities_InputPin class attributes and methods

# Activities_ExtraStructuredActivities_ExceptionHandler class attributes and methods

# Classifier class attributes and methods

# Activities_ExtraStructuredActivities_Classifier class attributes and methods

# Activities_ExtraStructuredActivities_ExpansionRegion class attributes and methods
Activities_ExtraStructuredActivities_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
Activities_ExtraStructuredActivities_ExpansionRegion.attributes={Activities_ExtraStructuredActivities_ExpansionRegion_mode}

# ExpansionNode class attributes and methods

# Activities_ExtraStructuredActivities_ExpansionNode class attributes and methods

# ExpansionRegion class attributes and methods

# Relationships
structuredNode6: BinaryAssociation = BinaryAssociation(
    name="structuredNode6",
    ends={
        Property(name="StructuredActivityNode", type=Activities_FundamentalActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=StructuredActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
inGroup10: BinaryAssociation = BinaryAssociation(
    name="inGroup10",
    ends={
        Property(name="ActivityGroup11", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="containedNode", type=ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedNode12: BinaryAssociation = BinaryAssociation(
    name="redefinedNode12",
    ends={
        Property(name="ActivityNode13", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_ActivityNode", type=ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
incoming14: BinaryAssociation = BinaryAssociation(
    name="incoming14",
    ends={
        Property(name="ActivityEdge15", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing16: BinaryAssociation = BinaryAssociation(
    name="outgoing16",
    ends={
        Property(name="ActivityEdge17", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition18: BinaryAssociation = BinaryAssociation(
    name="inPartition18",
    ends={
        Property(name="ActivityPartition19", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=ActivityPartition, multiplicity=Multiplicity(0, 9999))
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
        Property(name="ActivityGroup", type=Activities_FundamentalActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="inActivity", type=ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
subgroup33: BinaryAssociation = BinaryAssociation(
    name="subgroup33",
    ends={
        Property(name="ActivityGroup34", type=Activities_FundamentalActivities_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="superGroup", type=ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superGroup35: BinaryAssociation = BinaryAssociation(
    name="superGroup35",
    ends={
        Property(name="ActivityGroup36", type=Activities_FundamentalActivities_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="subgroup", type=ActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
inActivity37: BinaryAssociation = BinaryAssociation(
    name="inActivity37",
    ends={
        Property(name="Activity", type=Activities_FundamentalActivities_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=Activity, multiplicity=Multiplicity(0, 1))
    }
)
containedNode38: BinaryAssociation = BinaryAssociation(
    name="containedNode38",
    ends={
        Property(name="ActivityNode39", type=Activities_FundamentalActivities_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="inGroup", type=ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
containedEdge40: BinaryAssociation = BinaryAssociation(
    name="containedEdge40",
    ends={
        Property(name="ActivityEdge42", type=Activities_FundamentalActivities_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="inGroup41", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement43: BinaryAssociation = BinaryAssociation(
    name="redefinedElement43",
    ends={
        Property(name="RedefinableElement", type=Activities_BasicActivities_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_RedefinableElement", type=RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
inInterruptibleRegion20: BinaryAssociation = BinaryAssociation(
    name="inInterruptibleRegion20",
    ends={
        Property(name="InterruptibleActivityRegion", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node21", type=InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode22: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode22",
    ends={
        Property(name="StructuredActivityNode24", type=Activities_FundamentalActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node23", type=StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
localPrecondition25: BinaryAssociation = BinaryAssociation(
    name="localPrecondition25",
    ends={
        Property(name="Constraint", type=Activities_FundamentalActivities_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Action", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localPostcondition26: BinaryAssociation = BinaryAssociation(
    name="localPostcondition26",
    ends={
        Property(name="Constraint28", type=Activities_FundamentalActivities_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Action27", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input29: BinaryAssociation = BinaryAssociation(
    name="input29",
    ends={
        Property(name="InputPin", type=Activities_FundamentalActivities_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Action30", type=InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source49: BinaryAssociation = BinaryAssociation(
    name="source49",
    ends={
        Property(name="ActivityNode50", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
output31: BinaryAssociation = BinaryAssociation(
    name="output31",
    ends={
        Property(name="OutputPin", type=Activities_FundamentalActivities_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_FundamentalActivities_Action32", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedEdge51: BinaryAssociation = BinaryAssociation(
    name="redefinedEdge51",
    ends={
        Property(name="ActivityEdge52", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ActivityEdge", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inGroup53: BinaryAssociation = BinaryAssociation(
    name="inGroup53",
    ends={
        Property(name="ActivityGroup54", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="containedEdge", type=ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
guard55: BinaryAssociation = BinaryAssociation(
    name="guard55",
    ends={
        Property(name="ValueSpecification", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ActivityEdge56", type=ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPartition57: BinaryAssociation = BinaryAssociation(
    name="inPartition57",
    ends={
        Property(name="ActivityPartition58", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
weight59: BinaryAssociation = BinaryAssociation(
    name="weight59",
    ends={
        Property(name="ValueSpecification61", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ActivityEdge60", type=ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interrupts62: BinaryAssociation = BinaryAssociation(
    name="interrupts62",
    ends={
        Property(name="InterruptibleActivityRegion63", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="interruptingEdge", type=InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode64: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode64",
    ends={
        Property(name="StructuredActivityNode66", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge65", type=StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
parameter44: BinaryAssociation = BinaryAssociation(
    name="parameter44",
    ends={
        Property(name="Parameter", type=Activities_BasicActivities_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ActivityParameterNode", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
parameterSet45: BinaryAssociation = BinaryAssociation(
    name="parameterSet45",
    ends={
        Property(name="ParameterSet46", type=Activities_BasicActivities_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=ParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
target47: BinaryAssociation = BinaryAssociation(
    name="target47",
    ends={
        Property(name="ActivityNode48", type=Activities_BasicActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
joinSpec73: BinaryAssociation = BinaryAssociation(
    name="joinSpec73",
    ends={
        Property(name="ValueSpecification74", type=Activities_IntermediateActivities_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_JoinNode", type=ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
decisionInputFlow75: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow75",
    ends={
        Property(name="ObjectFlow", type=Activities_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_DecisionNode", type=ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
decisionInput76: BinaryAssociation = BinaryAssociation(
    name="decisionInput76",
    ends={
        Property(name="Behavior78", type=Activities_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_DecisionNode77", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
edge79: BinaryAssociation = BinaryAssociation(
    name="edge79",
    ends={
        Property(name="ActivityEdge80", type=Activities_IntermediateActivities_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="inPartition", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
subpartition81: BinaryAssociation = BinaryAssociation(
    name="subpartition81",
    ends={
        Property(name="ActivityPartition82", type=Activities_IntermediateActivities_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="superPartition", type=ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superPartition83: BinaryAssociation = BinaryAssociation(
    name="superPartition83",
    ends={
        Property(name="ActivityPartition84", type=Activities_IntermediateActivities_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="subpartition", type=ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
represents85: BinaryAssociation = BinaryAssociation(
    name="represents85",
    ends={
        Property(name="Element", type=Activities_IntermediateActivities_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_ActivityPartition", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
transformation67: BinaryAssociation = BinaryAssociation(
    name="transformation67",
    ends={
        Property(name="Behavior", type=Activities_BasicActivities_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ObjectFlow", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
selection68: BinaryAssociation = BinaryAssociation(
    name="selection68",
    ends={
        Property(name="Behavior70", type=Activities_BasicActivities_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ObjectFlow69", type=Behavior, multiplicity=Multiplicity(0, 1))
    }
)
inState71: BinaryAssociation = BinaryAssociation(
    name="inState71",
    ends={
        Property(name="State", type=Activities_BasicActivities_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_BasicActivities_ObjectFlow72", type=State, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameterSet93: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet93",
    ends={
        Property(name="ParameterSet94", type=Activities_IntermediateActivities_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_BehavioralFeature", type=ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interruptingEdge95: BinaryAssociation = BinaryAssociation(
    name="interruptingEdge95",
    ends={
        Property(name="ActivityEdge96", type=Activities_IntermediateActivities_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="interrupts", type=ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
node97: BinaryAssociation = BinaryAssociation(
    name="node97",
    ends={
        Property(name="ActivityNode98", type=Activities_IntermediateActivities_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="inInterruptibleRegion", type=ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
activity99: BinaryAssociation = BinaryAssociation(
    name="activity99",
    ends={
        Property(name="Activity100", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="structuredNode", type=Activity, multiplicity=Multiplicity(0, 1))
    }
)
variable101: BinaryAssociation = BinaryAssociation(
    name="variable101",
    ends={
        Property(name="Variable102", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_StructuredActivityNode", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node86: BinaryAssociation = BinaryAssociation(
    name="node86",
    ends={
        Property(name="ActivityNode88", type=Activities_IntermediateActivities_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="inPartition87", type=ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
parameter89: BinaryAssociation = BinaryAssociation(
    name="parameter89",
    ends={
        Property(name="Parameter90", type=Activities_IntermediateActivities_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSet", type=Parameter_, multiplicity=Multiplicity(1, 9999))
    }
)
condition91: BinaryAssociation = BinaryAssociation(
    name="condition91",
    ends={
        Property(name="Constraint92", type=Activities_IntermediateActivities_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_IntermediateActivities_ParameterSet", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node103: BinaryAssociation = BinaryAssociation(
    name="node103",
    ends={
        Property(name="ActivityNode104", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode", type=ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyPart116: BinaryAssociation = BinaryAssociation(
    name="bodyPart116",
    ends={
        Property(name="ExecutableNode118", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode117", type=ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNodeInput105: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput105",
    ends={
        Property(name="InputPin107", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_StructuredActivityNode106", type=InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test119: BinaryAssociation = BinaryAssociation(
    name="test119",
    ends={
        Property(name="ExecutableNode121", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode120", type=ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
edge108: BinaryAssociation = BinaryAssociation(
    name="edge108",
    ends={
        Property(name="ActivityEdge110", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode109", type=ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decider122: BinaryAssociation = BinaryAssociation(
    name="decider122",
    ends={
        Property(name="OutputPin124", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode123", type=OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
loopVariableInput125: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput125",
    ends={
        Property(name="InputPin127", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode126", type=InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeOutput111: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput111",
    ends={
        Property(name="OutputPin113", type=Activities_StructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_StructuredActivityNode112", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable128: BinaryAssociation = BinaryAssociation(
    name="loopVariable128",
    ends={
        Property(name="OutputPin130", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode129", type=OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
bodyOutput131: BinaryAssociation = BinaryAssociation(
    name="bodyOutput131",
    ends={
        Property(name="OutputPin133", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode132", type=OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
handler114: BinaryAssociation = BinaryAssociation(
    name="handler114",
    ends={
        Property(name="ExceptionHandler", type=Activities_StructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="protectedNode", type=ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result134: BinaryAssociation = BinaryAssociation(
    name="result134",
    ends={
        Property(name="OutputPin136", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode135", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clause137: BinaryAssociation = BinaryAssociation(
    name="clause137",
    ends={
        Property(name="Clause", type=Activities_StructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_ConditionalNode", type=Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
test138: BinaryAssociation = BinaryAssociation(
    name="test138",
    ends={
        Property(name="ExecutableNode140", type=Activities_StructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_ConditionalNode139", type=ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body141: BinaryAssociation = BinaryAssociation(
    name="body141",
    ends={
        Property(name="ExecutableNode143", type=Activities_StructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_ConditionalNode142", type=ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
result144: BinaryAssociation = BinaryAssociation(
    name="result144",
    ends={
        Property(name="OutputPin146", type=Activities_StructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_ConditionalNode145", type=OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessorClause147: BinaryAssociation = BinaryAssociation(
    name="predecessorClause147",
    ends={
        Property(name="Clause148", type=Activities_StructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="sucessorClause", type=Clause, multiplicity=Multiplicity(0, 9999))
    }
)
sucessorClause149: BinaryAssociation = BinaryAssociation(
    name="sucessorClause149",
    ends={
        Property(name="Clause150", type=Activities_StructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessorClause", type=Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider151: BinaryAssociation = BinaryAssociation(
    name="decider151",
    ends={
        Property(name="OutputPin152", type=Activities_StructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_Clause", type=OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
executableNode153: BinaryAssociation = BinaryAssociation(
    name="executableNode153",
    ends={
        Property(name="ExecutableNode154", type=Activities_StructuredActivities_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_SequenceNode", type=ExecutableNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setupPart115: BinaryAssociation = BinaryAssociation(
    name="setupPart115",
    ends={
        Property(name="ExecutableNode", type=Activities_StructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_StructuredActivities_LoopNode", type=ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
handlerBody155: BinaryAssociation = BinaryAssociation(
    name="handlerBody155",
    ends={
        Property(name="ExecutableNode156", type=Activities_ExtraStructuredActivities_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_ExtraStructuredActivities_ExceptionHandler", type=ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
protectedNode157: BinaryAssociation = BinaryAssociation(
    name="protectedNode157",
    ends={
        Property(name="ExecutableNode158", type=Activities_ExtraStructuredActivities_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="handler", type=ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionInput159: BinaryAssociation = BinaryAssociation(
    name="exceptionInput159",
    ends={
        Property(name="ObjectNode", type=Activities_ExtraStructuredActivities_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_ExtraStructuredActivities_ExceptionHandler160", type=ObjectNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionType161: BinaryAssociation = BinaryAssociation(
    name="exceptionType161",
    ends={
        Property(name="Classifier", type=Activities_ExtraStructuredActivities_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities_ExtraStructuredActivities_ExceptionHandler162", type=Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
inputElement163: BinaryAssociation = BinaryAssociation(
    name="inputElement163",
    ends={
        Property(name="ExpansionNode", type=Activities_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsInput", type=ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement164: BinaryAssociation = BinaryAssociation(
    name="outputElement164",
    ends={
        Property(name="regionAsOutput", type=ExpansionNode, multiplicity=Multiplicity(0, 9999)),
        Property(name="ExpansionNode165", type=Activities_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1))
    }
)
regionAsInput166: BinaryAssociation = BinaryAssociation(
    name="regionAsInput166",
    ends={
        Property(name="ExpansionRegion", type=Activities_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inputElement", type=ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsOutput167: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput167",
    ends={
        Property(name="ExpansionRegion168", type=Activities_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="outputElement", type=ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Activities_FundamentalActivities_Behavior_Class = Generalization(general=Class_, specific=Activities_FundamentalActivities_Behavior)
gen_Activities_FundamentalActivities_ActivityNode_FundamentalActivities_NamedElement = Generalization(general=FundamentalActivities_NamedElement, specific=Activities_FundamentalActivities_ActivityNode)
gen_Activities_FundamentalActivities_ActivityNode_BasicActivities_RedefinableElement = Generalization(general=BasicActivities_RedefinableElement, specific=Activities_FundamentalActivities_ActivityNode)
gen_Activities_FundamentalActivities_Activity_Behavior = Generalization(general=Behavior, specific=Activities_FundamentalActivities_Activity)
gen_Activities_FundamentalActivities_ActivityGroup_NamedElement = Generalization(general=NamedElement, specific=Activities_FundamentalActivities_ActivityGroup)
gen_Activities_BasicActivities_ObjectNode_FundamentalActivities_ActivityNode = Generalization(general=FundamentalActivities_ActivityNode, specific=Activities_BasicActivities_ObjectNode)
gen_Activities_FundamentalActivities_Action_ActivityNode = Generalization(general=ActivityNode, specific=Activities_FundamentalActivities_Action)
gen_Activities_BasicActivities_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=Activities_BasicActivities_ControlFlow)
gen_Activities_BasicActivities_ObjectNode_BasicActivities_TypedElement = Generalization(general=BasicActivities_TypedElement, specific=Activities_BasicActivities_ObjectNode)
gen_Activities_BasicActivities_Pin_ObjectNode = Generalization(general=ObjectNode, specific=Activities_BasicActivities_Pin)
gen_Activities_BasicActivities_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=Activities_BasicActivities_ActivityParameterNode)
gen_Activities_BasicActivities_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=Activities_BasicActivities_ControlNode)
gen_Activities_BasicActivities_ActivityFinalNode_BasicActivities_ControlNode = Generalization(general=BasicActivities_ControlNode, specific=Activities_BasicActivities_ActivityFinalNode)
gen_Activities_BasicActivities_ActivityFinalNode_IntermediateActivities_FinalNode = Generalization(general=IntermediateActivities_FinalNode, specific=Activities_BasicActivities_ActivityFinalNode)
gen_Activities_BasicActivities_InitialNode_ControlNode = Generalization(general=ControlNode, specific=Activities_BasicActivities_InitialNode)
gen_Activities_BasicActivities_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=Activities_BasicActivities_ActivityEdge)
gen_Activities_IntermediateActivities_MergeNode_ControlNode = Generalization(general=ControlNode, specific=Activities_IntermediateActivities_MergeNode)
gen_Activities_IntermediateActivities_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=Activities_IntermediateActivities_DecisionNode)
gen_Activities_IntermediateActivities_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=Activities_IntermediateActivities_ActivityPartition)
gen_Activities_BasicActivities_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=Activities_BasicActivities_ObjectFlow)
gen_Activities_IntermediateActivities_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=Activities_IntermediateActivities_CentralBufferNode)
gen_Activities_IntermediateActivities_FinalNode_ControlNode = Generalization(general=ControlNode, specific=Activities_IntermediateActivities_FinalNode)
gen_Activities_IntermediateActivities_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=Activities_IntermediateActivities_FlowFinalNode)
gen_Activities_IntermediateActivities_ForkNode_ControlNode = Generalization(general=ControlNode, specific=Activities_IntermediateActivities_ForkNode)
gen_Activities_IntermediateActivities_JoinNode_ControlNode = Generalization(general=ControlNode, specific=Activities_IntermediateActivities_JoinNode)
gen_Activities_IntermediateActivities_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=Activities_IntermediateActivities_InterruptibleActivityRegion)
gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_Namespace = Generalization(general=FundamentalActivities_Namespace, specific=Activities_StructuredActivities_StructuredActivityNode)
gen_Activities_StructuredActivities_StructuredActivityNode_StructuredActivities_ExecutableNode = Generalization(general=StructuredActivities_ExecutableNode, specific=Activities_StructuredActivities_StructuredActivityNode)
gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_ActivityGroup = Generalization(general=FundamentalActivities_ActivityGroup, specific=Activities_StructuredActivities_StructuredActivityNode)
gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_Action = Generalization(general=FundamentalActivities_Action, specific=Activities_StructuredActivities_StructuredActivityNode)
gen_Activities_IntermediateActivities_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=Activities_IntermediateActivities_DataStoreNode)
gen_Activities_IntermediateActivities_ParameterSet_NamedElement = Generalization(general=NamedElement, specific=Activities_IntermediateActivities_ParameterSet)
gen_Activities_IntermediateActivities_BehavioralFeature_FundamentalActivities_Namespace = Generalization(general=FundamentalActivities_Namespace, specific=Activities_IntermediateActivities_BehavioralFeature)
gen_Activities_IntermediateActivities_BehavioralFeature_IntermediateActivities_Feature = Generalization(general=IntermediateActivities_Feature, specific=Activities_IntermediateActivities_BehavioralFeature)
gen_Activities_StructuredActivities_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=Activities_StructuredActivities_ExecutableNode)
gen_Activities_StructuredActivities_Variable_StructuredActivities_MultiplicityElement = Generalization(general=StructuredActivities_MultiplicityElement, specific=Activities_StructuredActivities_Variable)
gen_Activities_StructuredActivities_Variable_BasicActivities_TypedElement = Generalization(general=BasicActivities_TypedElement, specific=Activities_StructuredActivities_Variable)
gen_Activities_StructuredActivities_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=Activities_StructuredActivities_ConditionalNode)
gen_Activities_StructuredActivities_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=Activities_StructuredActivities_LoopNode)
gen_Activities_StructuredActivities_Clause_Element = Generalization(general=Element, specific=Activities_StructuredActivities_Clause)
gen_Activities_StructuredActivities_SequenceNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=Activities_StructuredActivities_SequenceNode)
gen_Activities_ExtraStructuredActivities_ExceptionHandler_Element = Generalization(general=Element, specific=Activities_ExtraStructuredActivities_ExceptionHandler)
gen_Activities_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=Activities_ExtraStructuredActivities_ExpansionRegion)
gen_Activities_ExtraStructuredActivities_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=Activities_ExtraStructuredActivities_ExpansionNode)

# Domain Model
domain_model = DomainModel(
    name="Activities",
    types={StructuredActivityNode, Variable, Activities_FundamentalActivities_Behavior, Class_, ParameterSet, Activities_FundamentalActivities_NamedElement, Activities_FundamentalActivities_ActivityNode, FundamentalActivities_NamedElement, BasicActivities_RedefinableElement, Activities_FundamentalActivities_Activity, Behavior, ActivityNode, ActivityGroup, ActivityEdge, ActivityPartition, NamedElement, Activity, Activities_FundamentalActivities_Namespace, Activities_BasicActivities_RedefinableElement, RedefinableElement, Activities_BasicActivities_ObjectNode, FundamentalActivities_ActivityNode, InterruptibleActivityRegion, Activities_FundamentalActivities_Action, Constraint, InputPin, OutputPin, Activities_FundamentalActivities_ActivityGroup, ValueSpecification, Activities_BasicActivities_ControlFlow, Activities_BasicActivities_ObjectFlow, BasicActivities_TypedElement, Activities_BasicActivities_TypedElement, Activities_BasicActivities_Pin, ObjectNode, Activities_BasicActivities_ActivityParameterNode, Parameter_, Activities_BasicActivities_Parameter, Activities_BasicActivities_ControlNode, Activities_BasicActivities_ActivityFinalNode, BasicActivities_ControlNode, IntermediateActivities_FinalNode, Activities_BasicActivities_InitialNode, ControlNode, Activities_BasicActivities_ActivityEdge, Activities_IntermediateActivities_MergeNode, Activities_IntermediateActivities_DecisionNode, ObjectFlow, Activities_IntermediateActivities_ValueSpecification, Activities_IntermediateActivities_ActivityPartition, Element, State, Activities_IntermediateActivities_CentralBufferNode, Activities_IntermediateActivities_FinalNode, Activities_IntermediateActivities_FlowFinalNode, FinalNode, Activities_IntermediateActivities_ForkNode, Activities_IntermediateActivities_JoinNode, Activities_IntermediateActivities_Feature, Activities_IntermediateActivities_Class, Activities_IntermediateActivities_InterruptibleActivityRegion, Activities_StructuredActivities_StructuredActivityNode, StructuredActivities_ExecutableNode, FundamentalActivities_ActivityGroup, FundamentalActivities_Action, Activities_IntermediateActivities_Element, Activities_IntermediateActivities_Constraint, Activities_IntermediateActivities_State, Activities_IntermediateActivities_DataStoreNode, CentralBufferNode, Activities_IntermediateActivities_ParameterSet, Activities_IntermediateActivities_BehavioralFeature, FundamentalActivities_Namespace, IntermediateActivities_Feature, Activities_StructuredActivities_ExecutableNode, ExceptionHandler, Activities_StructuredActivities_Variable, StructuredActivities_MultiplicityElement, Activities_StructuredActivities_OutputPin, Activities_StructuredActivities_MultiplicityElement, Activities_StructuredActivities_ConditionalNode, Activities_StructuredActivities_LoopNode, Clause, Activities_StructuredActivities_Clause, Activities_StructuredActivities_SequenceNode, ExecutableNode, Activities_CompleteStructuredActivities_InputPin, Activities_ExtraStructuredActivities_ExceptionHandler, Classifier, Activities_ExtraStructuredActivities_Classifier, Activities_ExtraStructuredActivities_ExpansionRegion, ExpansionNode, Activities_ExtraStructuredActivities_ExpansionNode, ExpansionRegion, ObjectNodeOrderingKind, ParameterEffectKind, ExpansionKind},
    associations={structuredNode6, variable7, ownedParameterSet9, inGroup10, redefinedNode12, incoming14, outgoing16, inPartition18, node0, group1, edge2, partition4, subgroup33, superGroup35, inActivity37, containedNode38, containedEdge40, redefinedElement43, inInterruptibleRegion20, inStructuredNode22, localPrecondition25, localPostcondition26, input29, source49, output31, redefinedEdge51, inGroup53, guard55, inPartition57, weight59, interrupts62, inStructuredNode64, parameter44, parameterSet45, target47, joinSpec73, decisionInputFlow75, decisionInput76, edge79, subpartition81, superPartition83, represents85, transformation67, selection68, inState71, ownedParameterSet93, interruptingEdge95, node97, activity99, variable101, node86, parameter89, condition91, node103, bodyPart116, structuredNodeInput105, test119, edge108, decider122, loopVariableInput125, structuredNodeOutput111, loopVariable128, bodyOutput131, handler114, result134, clause137, test138, body141, result144, predecessorClause147, sucessorClause149, decider151, executableNode153, setupPart115, handlerBody155, protectedNode157, exceptionInput159, exceptionType161, inputElement163, outputElement164, regionAsInput166, regionAsOutput167},
    generalizations={gen_Activities_FundamentalActivities_Behavior_Class, gen_Activities_FundamentalActivities_ActivityNode_FundamentalActivities_NamedElement, gen_Activities_FundamentalActivities_ActivityNode_BasicActivities_RedefinableElement, gen_Activities_FundamentalActivities_Activity_Behavior, gen_Activities_FundamentalActivities_ActivityGroup_NamedElement, gen_Activities_BasicActivities_ObjectNode_FundamentalActivities_ActivityNode, gen_Activities_FundamentalActivities_Action_ActivityNode, gen_Activities_BasicActivities_ControlFlow_ActivityEdge, gen_Activities_BasicActivities_ObjectNode_BasicActivities_TypedElement, gen_Activities_BasicActivities_Pin_ObjectNode, gen_Activities_BasicActivities_ActivityParameterNode_ObjectNode, gen_Activities_BasicActivities_ControlNode_ActivityNode, gen_Activities_BasicActivities_ActivityFinalNode_BasicActivities_ControlNode, gen_Activities_BasicActivities_ActivityFinalNode_IntermediateActivities_FinalNode, gen_Activities_BasicActivities_InitialNode_ControlNode, gen_Activities_BasicActivities_ActivityEdge_RedefinableElement, gen_Activities_IntermediateActivities_MergeNode_ControlNode, gen_Activities_IntermediateActivities_DecisionNode_ControlNode, gen_Activities_IntermediateActivities_ActivityPartition_ActivityGroup, gen_Activities_BasicActivities_ObjectFlow_ActivityEdge, gen_Activities_IntermediateActivities_CentralBufferNode_ObjectNode, gen_Activities_IntermediateActivities_FinalNode_ControlNode, gen_Activities_IntermediateActivities_FlowFinalNode_FinalNode, gen_Activities_IntermediateActivities_ForkNode_ControlNode, gen_Activities_IntermediateActivities_JoinNode_ControlNode, gen_Activities_IntermediateActivities_InterruptibleActivityRegion_ActivityGroup, gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_Namespace, gen_Activities_StructuredActivities_StructuredActivityNode_StructuredActivities_ExecutableNode, gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_ActivityGroup, gen_Activities_StructuredActivities_StructuredActivityNode_FundamentalActivities_Action, gen_Activities_IntermediateActivities_DataStoreNode_CentralBufferNode, gen_Activities_IntermediateActivities_ParameterSet_NamedElement, gen_Activities_IntermediateActivities_BehavioralFeature_FundamentalActivities_Namespace, gen_Activities_IntermediateActivities_BehavioralFeature_IntermediateActivities_Feature, gen_Activities_StructuredActivities_ExecutableNode_ActivityNode, gen_Activities_StructuredActivities_Variable_StructuredActivities_MultiplicityElement, gen_Activities_StructuredActivities_Variable_BasicActivities_TypedElement, gen_Activities_StructuredActivities_ConditionalNode_StructuredActivityNode, gen_Activities_StructuredActivities_LoopNode_StructuredActivityNode, gen_Activities_StructuredActivities_Clause_Element, gen_Activities_StructuredActivities_SequenceNode_StructuredActivityNode, gen_Activities_ExtraStructuredActivities_ExceptionHandler_Element, gen_Activities_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode, gen_Activities_ExtraStructuredActivities_ExpansionNode_ObjectNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)