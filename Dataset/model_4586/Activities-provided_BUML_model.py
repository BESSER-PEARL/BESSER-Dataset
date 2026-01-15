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
ActivitiesProv_Activity = Class(name="ActivitiesProv::Activity")
ActivitiesProv_ActivityNode = Class(name="ActivitiesProv::ActivityNode", is_abstract=True)
ActivitiesProv_ActivityGroup = Class(name="ActivitiesProv::ActivityGroup", is_abstract=True)
ActivitiesProv_ActivityEdge = Class(name="ActivitiesProv::ActivityEdge", is_abstract=True)
ActivitiesProv_ActivityPartition = Class(name="ActivitiesProv::ActivityPartition")
ActivitiesProv_StructuredActivityNode = Class(name="ActivitiesProv::StructuredActivityNode")
ActivitiesProv_InterruptibleActivityRegion = Class(name="ActivitiesProv::InterruptibleActivityRegion")
ActivitiesProv_ObjectNode = Class(name="ActivitiesProv::ObjectNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
ActivitiesProv_ActivityParameterNode = Class(name="ActivitiesProv::ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
ActivitiesProv_ControlNode = Class(name="ActivitiesProv::ControlNode", is_abstract=True)
ActivitiesProv_ActivityFinalNode = Class(name="ActivitiesProv::ActivityFinalNode")
ControlNode = Class(name="ControlNode")
FinalNode = Class(name="FinalNode")
ActivitiesProv_InitialNode = Class(name="ActivitiesProv::InitialNode")
ActivitiesProv_ControlFlow = Class(name="ActivitiesProv::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
ActivitiesProv_ObjectFlow = Class(name="ActivitiesProv::ObjectFlow")
ActivitiesProv_MergeNode = Class(name="ActivitiesProv::MergeNode")
ActivitiesProv_DecisionNode = Class(name="ActivitiesProv::DecisionNode")
ActivityGroup = Class(name="ActivityGroup")
ActivitiesProv_DataStoreNode = Class(name="ActivitiesProv::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
ActivitiesProv_ParameterSet = Class(name="ActivitiesProv::ParameterSet")
ExecutableNode = Class(name="ExecutableNode")
ActivitiesProv_ExecutableNode = Class(name="ActivitiesProv::ExecutableNode")
ActivitiesProv_CentralBufferNode = Class(name="ActivitiesProv::CentralBufferNode")
ActivitiesProv_FinalNode = Class(name="ActivitiesProv::FinalNode", is_abstract=True)
ActivitiesProv_FlowFinalNode = Class(name="ActivitiesProv::FlowFinalNode")
ActivitiesProv_ForkNode = Class(name="ActivitiesProv::ForkNode")
ActivitiesProv_JoinNode = Class(name="ActivitiesProv::JoinNode")
ActivitiesProv_ConditionalNode = Class(name="ActivitiesProv::ConditionalNode")
ActivitiesProv_Clause = Class(name="ActivitiesProv::Clause")
ActivitiesProv_SequenceNode = Class(name="ActivitiesProv::SequenceNode")
ActivitiesProv_ExpansionRegion = Class(name="ActivitiesProv::ExpansionRegion")
ActivitiesProv_ExpansionNode = Class(name="ActivitiesProv::ExpansionNode")
ActivitiesProv_ExceptionHandler = Class(name="ActivitiesProv::ExceptionHandler")
ActivitiesProv_LoopNode = Class(name="ActivitiesProv::LoopNode")
StructuredActivityNode = Class(name="StructuredActivityNode")

# ActivitiesProv_Activity class attributes and methods
ActivitiesProv_Activity_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
ActivitiesProv_Activity_isSingleExecution: Property = Property(name="isSingleExecution", type=BooleanType)
ActivitiesProv_Activity.attributes={ActivitiesProv_Activity_isSingleExecution, ActivitiesProv_Activity_isReadOnly}

# ActivitiesProv_ActivityNode class attributes and methods

# ActivitiesProv_ActivityGroup class attributes and methods

# ActivitiesProv_ActivityEdge class attributes and methods

# ActivitiesProv_ActivityPartition class attributes and methods

# ActivitiesProv_StructuredActivityNode class attributes and methods
ActivitiesProv_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
ActivitiesProv_StructuredActivityNode.attributes={ActivitiesProv_StructuredActivityNode_mustIsolate}

# ActivitiesProv_InterruptibleActivityRegion class attributes and methods

# ActivitiesProv_ObjectNode class attributes and methods

# ActivityNode class attributes and methods

# ActivitiesProv_ActivityParameterNode class attributes and methods

# ObjectNode class attributes and methods

# ActivitiesProv_ControlNode class attributes and methods

# ActivitiesProv_ActivityFinalNode class attributes and methods

# ControlNode class attributes and methods

# FinalNode class attributes and methods

# ActivitiesProv_InitialNode class attributes and methods

# ActivitiesProv_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# ActivitiesProv_ObjectFlow class attributes and methods
ActivitiesProv_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=BooleanType)
ActivitiesProv_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=BooleanType)
ActivitiesProv_ObjectFlow_isControlType: Property = Property(name="isControlType", type=BooleanType)
ActivitiesProv_ObjectFlow.attributes={ActivitiesProv_ObjectFlow_isMulticast, ActivitiesProv_ObjectFlow_isMultireceive, ActivitiesProv_ObjectFlow_isControlType}

# ActivitiesProv_MergeNode class attributes and methods

# ActivitiesProv_DecisionNode class attributes and methods

# ActivityGroup class attributes and methods

# ActivitiesProv_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# ActivitiesProv_ParameterSet class attributes and methods

# ExecutableNode class attributes and methods

# ActivitiesProv_ExecutableNode class attributes and methods

# ActivitiesProv_CentralBufferNode class attributes and methods

# ActivitiesProv_FinalNode class attributes and methods

# ActivitiesProv_FlowFinalNode class attributes and methods

# ActivitiesProv_ForkNode class attributes and methods

# ActivitiesProv_JoinNode class attributes and methods
ActivitiesProv_JoinNode_isCombineDuplicate: Property = Property(name="isCombineDuplicate", type=BooleanType)
ActivitiesProv_JoinNode.attributes={ActivitiesProv_JoinNode_isCombineDuplicate}

# ActivitiesProv_ConditionalNode class attributes and methods
ActivitiesProv_ConditionalNode_isDeterminate: Property = Property(name="isDeterminate", type=BooleanType)
ActivitiesProv_ConditionalNode_isAssumed: Property = Property(name="isAssumed", type=BooleanType)
ActivitiesProv_ConditionalNode.attributes={ActivitiesProv_ConditionalNode_isAssumed, ActivitiesProv_ConditionalNode_isDeterminate}

# ActivitiesProv_Clause class attributes and methods

# ActivitiesProv_SequenceNode class attributes and methods

# ActivitiesProv_ExpansionRegion class attributes and methods

# ActivitiesProv_ExpansionNode class attributes and methods

# ActivitiesProv_ExceptionHandler class attributes and methods

# ActivitiesProv_LoopNode class attributes and methods
ActivitiesProv_LoopNode_isTestedFirst: Property = Property(name="isTestedFirst", type=BooleanType)
ActivitiesProv_LoopNode.attributes={ActivitiesProv_LoopNode_isTestedFirst}

# StructuredActivityNode class attributes and methods

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="ActivitiesProv_ActivityNode", type=ActivitiesProv_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_Activity", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group1: BinaryAssociation = BinaryAssociation(
    name="group1",
    ends={
        Property(name="ActivitiesProv_ActivityGroup", type=ActivitiesProv_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_Activity2", type=ActivitiesProv_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge3: BinaryAssociation = BinaryAssociation(
    name="edge3",
    ends={
        Property(name="ActivitiesProv_ActivityEdge", type=ActivitiesProv_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_Activity4", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partition5: BinaryAssociation = BinaryAssociation(
    name="partition5",
    ends={
        Property(name="ActivitiesProv_ActivityPartition", type=ActivitiesProv_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_Activity6", type=ActivitiesProv_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNode7: BinaryAssociation = BinaryAssociation(
    name="structuredNode7",
    ends={
        Property(name="ActivitiesProv_StructuredActivityNode", type=ActivitiesProv_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_Activity8", type=ActivitiesProv_StructuredActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inGroup9: BinaryAssociation = BinaryAssociation(
    name="inGroup9",
    ends={
        Property(name="ActivitiesProv_ActivityGroup11", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityNode10", type=ActivitiesProv_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedNode13: BinaryAssociation = BinaryAssociation(
    name="redefinedNode13",
    ends={
        Property(name="ActivitiesProv_ActivityNode14", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityNode12", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
incoming15: BinaryAssociation = BinaryAssociation(
    name="incoming15",
    ends={
        Property(name="ActivitiesProv_ActivityEdge17", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityNode16", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing18: BinaryAssociation = BinaryAssociation(
    name="outgoing18",
    ends={
        Property(name="ActivitiesProv_ActivityEdge20", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityNode19", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition21: BinaryAssociation = BinaryAssociation(
    name="inPartition21",
    ends={
        Property(name="ActivitiesProv_ActivityPartition23", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityNode22", type=ActivitiesProv_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
inInterruptibleRegion24: BinaryAssociation = BinaryAssociation(
    name="inInterruptibleRegion24",
    ends={
        Property(name="ActivitiesProv_InterruptibleActivityRegion", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityNode25", type=ActivitiesProv_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
containedNode38: BinaryAssociation = BinaryAssociation(
    name="containedNode38",
    ends={
        Property(name="ActivitiesProv_ActivityGroup39", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(0, 9999)),
        Property(name="ActivitiesProv_ActivityNode40", type=ActivitiesProv_ActivityGroup, multiplicity=Multiplicity(1, 1))
    }
)
containedEdge41: BinaryAssociation = BinaryAssociation(
    name="containedEdge41",
    ends={
        Property(name="ActivitiesProv_ActivityEdge43", type=ActivitiesProv_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityGroup42", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
target44: BinaryAssociation = BinaryAssociation(
    name="target44",
    ends={
        Property(name="ActivitiesProv_ActivityNode46", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityEdge45", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
source47: BinaryAssociation = BinaryAssociation(
    name="source47",
    ends={
        Property(name="ActivitiesProv_ActivityNode49", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityEdge48", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
redefinedEdge51: BinaryAssociation = BinaryAssociation(
    name="redefinedEdge51",
    ends={
        Property(name="ActivitiesProv_ActivityEdge52", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityEdge50", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inGroup53: BinaryAssociation = BinaryAssociation(
    name="inGroup53",
    ends={
        Property(name="ActivitiesProv_ActivityGroup55", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityEdge54", type=ActivitiesProv_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition56: BinaryAssociation = BinaryAssociation(
    name="inPartition56",
    ends={
        Property(name="ActivitiesProv_ActivityPartition58", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityEdge57", type=ActivitiesProv_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
interrupts59: BinaryAssociation = BinaryAssociation(
    name="interrupts59",
    ends={
        Property(name="ActivitiesProv_InterruptibleActivityRegion61", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityEdge60", type=ActivitiesProv_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode62: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode62",
    ends={
        Property(name="ActivitiesProv_StructuredActivityNode64", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityEdge63", type=ActivitiesProv_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode26: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode26",
    ends={
        Property(name="ActivitiesProv_StructuredActivityNode28", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityNode27", type=ActivitiesProv_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
subgroup30: BinaryAssociation = BinaryAssociation(
    name="subgroup30",
    ends={
        Property(name="ActivitiesProv_ActivityGroup31", type=ActivitiesProv_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityGroup29", type=ActivitiesProv_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superGroup33: BinaryAssociation = BinaryAssociation(
    name="superGroup33",
    ends={
        Property(name="ActivitiesProv_ActivityGroup34", type=ActivitiesProv_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityGroup32", type=ActivitiesProv_ActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
inActivity35: BinaryAssociation = BinaryAssociation(
    name="inActivity35",
    ends={
        Property(name="ActivitiesProv_Activity37", type=ActivitiesProv_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityGroup36", type=ActivitiesProv_Activity, multiplicity=Multiplicity(0, 1))
    }
)
decisionInputFlow65: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow65",
    ends={
        Property(name="ActivitiesProv_ObjectFlow", type=ActivitiesProv_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_DecisionNode", type=ActivitiesProv_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
edge66: BinaryAssociation = BinaryAssociation(
    name="edge66",
    ends={
        Property(name="ActivitiesProv_ActivityEdge68", type=ActivitiesProv_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityPartition67", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
subpartition70: BinaryAssociation = BinaryAssociation(
    name="subpartition70",
    ends={
        Property(name="ActivitiesProv_ActivityPartition71", type=ActivitiesProv_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityPartition69", type=ActivitiesProv_ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superPartition73: BinaryAssociation = BinaryAssociation(
    name="superPartition73",
    ends={
        Property(name="ActivitiesProv_ActivityPartition74", type=ActivitiesProv_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityPartition72", type=ActivitiesProv_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
node75: BinaryAssociation = BinaryAssociation(
    name="node75",
    ends={
        Property(name="ActivitiesProv_ActivityNode77", type=ActivitiesProv_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ActivityPartition76", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
interruptingEdge78: BinaryAssociation = BinaryAssociation(
    name="interruptingEdge78",
    ends={
        Property(name="ActivitiesProv_ActivityEdge80", type=ActivitiesProv_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_InterruptibleActivityRegion79", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
node81: BinaryAssociation = BinaryAssociation(
    name="node81",
    ends={
        Property(name="ActivitiesProv_ActivityNode83", type=ActivitiesProv_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_InterruptibleActivityRegion82", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
activity84: BinaryAssociation = BinaryAssociation(
    name="activity84",
    ends={
        Property(name="ActivitiesProv_Activity86", type=ActivitiesProv_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_StructuredActivityNode85", type=ActivitiesProv_Activity, multiplicity=Multiplicity(0, 1))
    }
)
node87: BinaryAssociation = BinaryAssociation(
    name="node87",
    ends={
        Property(name="ActivitiesProv_ActivityNode89", type=ActivitiesProv_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_StructuredActivityNode88", type=ActivitiesProv_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge90: BinaryAssociation = BinaryAssociation(
    name="edge90",
    ends={
        Property(name="ActivitiesProv_ActivityEdge92", type=ActivitiesProv_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_StructuredActivityNode91", type=ActivitiesProv_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test99: BinaryAssociation = BinaryAssociation(
    name="test99",
    ends={
        Property(name="ActivitiesProv_ExecutableNode101", type=ActivitiesProv_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_LoopNode100", type=ActivitiesProv_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
clause102: BinaryAssociation = BinaryAssociation(
    name="clause102",
    ends={
        Property(name="ActivitiesProv_Clause", type=ActivitiesProv_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ConditionalNode", type=ActivitiesProv_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
test103: BinaryAssociation = BinaryAssociation(
    name="test103",
    ends={
        Property(name="ActivitiesProv_ExecutableNode105", type=ActivitiesProv_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ConditionalNode104", type=ActivitiesProv_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body106: BinaryAssociation = BinaryAssociation(
    name="body106",
    ends={
        Property(name="ActivitiesProv_ExecutableNode108", type=ActivitiesProv_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ConditionalNode107", type=ActivitiesProv_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
predecessorClause110: BinaryAssociation = BinaryAssociation(
    name="predecessorClause110",
    ends={
        Property(name="ActivitiesProv_Clause111", type=ActivitiesProv_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_Clause109", type=ActivitiesProv_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
sucessorClause113: BinaryAssociation = BinaryAssociation(
    name="sucessorClause113",
    ends={
        Property(name="ActivitiesProv_Clause114", type=ActivitiesProv_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_Clause112", type=ActivitiesProv_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
executableNode115: BinaryAssociation = BinaryAssociation(
    name="executableNode115",
    ends={
        Property(name="ActivitiesProv_ExecutableNode116", type=ActivitiesProv_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_SequenceNode", type=ActivitiesProv_ExecutableNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handlerBody117: BinaryAssociation = BinaryAssociation(
    name="handlerBody117",
    ends={
        Property(name="ActivitiesProv_ExecutableNode119", type=ActivitiesProv_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ExceptionHandler118", type=ActivitiesProv_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
protectedNode120: BinaryAssociation = BinaryAssociation(
    name="protectedNode120",
    ends={
        Property(name="ActivitiesProv_ExecutableNode122", type=ActivitiesProv_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ExceptionHandler121", type=ActivitiesProv_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionInput123: BinaryAssociation = BinaryAssociation(
    name="exceptionInput123",
    ends={
        Property(name="ActivitiesProv_ObjectNode", type=ActivitiesProv_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ExceptionHandler124", type=ActivitiesProv_ObjectNode, multiplicity=Multiplicity(1, 1))
    }
)
inputElement125: BinaryAssociation = BinaryAssociation(
    name="inputElement125",
    ends={
        Property(name="ActivitiesProv_ExpansionNode", type=ActivitiesProv_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ExpansionRegion", type=ActivitiesProv_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement126: BinaryAssociation = BinaryAssociation(
    name="outputElement126",
    ends={
        Property(name="ActivitiesProv_ExpansionNode128", type=ActivitiesProv_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ExpansionRegion127", type=ActivitiesProv_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
handler93: BinaryAssociation = BinaryAssociation(
    name="handler93",
    ends={
        Property(name="ActivitiesProv_ExceptionHandler", type=ActivitiesProv_ExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ExecutableNode", type=ActivitiesProv_ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setupPart94: BinaryAssociation = BinaryAssociation(
    name="setupPart94",
    ends={
        Property(name="ActivitiesProv_ExecutableNode95", type=ActivitiesProv_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_LoopNode", type=ActivitiesProv_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
bodyPart96: BinaryAssociation = BinaryAssociation(
    name="bodyPart96",
    ends={
        Property(name="ActivitiesProv_ExecutableNode98", type=ActivitiesProv_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_LoopNode97", type=ActivitiesProv_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
regionAsInput129: BinaryAssociation = BinaryAssociation(
    name="regionAsInput129",
    ends={
        Property(name="ActivitiesProv_ExpansionRegion131", type=ActivitiesProv_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ExpansionNode130", type=ActivitiesProv_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsOutput132: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput132",
    ends={
        Property(name="ActivitiesProv_ExpansionRegion134", type=ActivitiesProv_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivitiesProv_ExpansionNode133", type=ActivitiesProv_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ActivitiesProv_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=ActivitiesProv_ObjectNode)
gen_ActivitiesProv_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=ActivitiesProv_ActivityParameterNode)
gen_ActivitiesProv_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=ActivitiesProv_ControlNode)
gen_ActivitiesProv_ActivityFinalNode_ControlNode = Generalization(general=ControlNode, specific=ActivitiesProv_ActivityFinalNode)
gen_ActivitiesProv_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=ActivitiesProv_ActivityFinalNode)
gen_ActivitiesProv_InitialNode_ControlNode = Generalization(general=ControlNode, specific=ActivitiesProv_InitialNode)
gen_ActivitiesProv_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=ActivitiesProv_ControlFlow)
gen_ActivitiesProv_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=ActivitiesProv_ObjectFlow)
gen_ActivitiesProv_MergeNode_ControlNode = Generalization(general=ControlNode, specific=ActivitiesProv_MergeNode)
gen_ActivitiesProv_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=ActivitiesProv_DecisionNode)
gen_ActivitiesProv_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=ActivitiesProv_ActivityPartition)
gen_ActivitiesProv_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=ActivitiesProv_DataStoreNode)
gen_ActivitiesProv_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=ActivitiesProv_InterruptibleActivityRegion)
gen_ActivitiesProv_StructuredActivityNode_ExecutableNode = Generalization(general=ExecutableNode, specific=ActivitiesProv_StructuredActivityNode)
gen_ActivitiesProv_StructuredActivityNode_ActivityGroup = Generalization(general=ActivityGroup, specific=ActivitiesProv_StructuredActivityNode)
gen_ActivitiesProv_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=ActivitiesProv_ExecutableNode)
gen_ActivitiesProv_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=ActivitiesProv_CentralBufferNode)
gen_ActivitiesProv_FinalNode_ControlNode = Generalization(general=ControlNode, specific=ActivitiesProv_FinalNode)
gen_ActivitiesProv_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=ActivitiesProv_FlowFinalNode)
gen_ActivitiesProv_ForkNode_ControlNode = Generalization(general=ControlNode, specific=ActivitiesProv_ForkNode)
gen_ActivitiesProv_JoinNode_ControlNode = Generalization(general=ControlNode, specific=ActivitiesProv_JoinNode)
gen_ActivitiesProv_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=ActivitiesProv_ConditionalNode)
gen_ActivitiesProv_SequenceNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=ActivitiesProv_SequenceNode)
gen_ActivitiesProv_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=ActivitiesProv_ExpansionRegion)
gen_ActivitiesProv_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=ActivitiesProv_ExpansionNode)
gen_ActivitiesProv_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=ActivitiesProv_LoopNode)

# Domain Model
domain_model = DomainModel(
    name="ActivitiesProv",
    types={ActivitiesProv_Activity, ActivitiesProv_ActivityNode, ActivitiesProv_ActivityGroup, ActivitiesProv_ActivityEdge, ActivitiesProv_ActivityPartition, ActivitiesProv_StructuredActivityNode, ActivitiesProv_InterruptibleActivityRegion, ActivitiesProv_ObjectNode, ActivityNode, ActivitiesProv_ActivityParameterNode, ObjectNode, ActivitiesProv_ControlNode, ActivitiesProv_ActivityFinalNode, ControlNode, FinalNode, ActivitiesProv_InitialNode, ActivitiesProv_ControlFlow, ActivityEdge, ActivitiesProv_ObjectFlow, ActivitiesProv_MergeNode, ActivitiesProv_DecisionNode, ActivityGroup, ActivitiesProv_DataStoreNode, CentralBufferNode, ActivitiesProv_ParameterSet, ExecutableNode, ActivitiesProv_ExecutableNode, ActivitiesProv_CentralBufferNode, ActivitiesProv_FinalNode, ActivitiesProv_FlowFinalNode, ActivitiesProv_ForkNode, ActivitiesProv_JoinNode, ActivitiesProv_ConditionalNode, ActivitiesProv_Clause, ActivitiesProv_SequenceNode, ActivitiesProv_ExpansionRegion, ActivitiesProv_ExpansionNode, ActivitiesProv_ExceptionHandler, ActivitiesProv_LoopNode, StructuredActivityNode},
    associations={node0, group1, edge3, partition5, structuredNode7, inGroup9, redefinedNode13, incoming15, outgoing18, inPartition21, inInterruptibleRegion24, containedNode38, containedEdge41, target44, source47, redefinedEdge51, inGroup53, inPartition56, interrupts59, inStructuredNode62, inStructuredNode26, subgroup30, superGroup33, inActivity35, decisionInputFlow65, edge66, subpartition70, superPartition73, node75, interruptingEdge78, node81, activity84, node87, edge90, test99, clause102, test103, body106, predecessorClause110, sucessorClause113, executableNode115, handlerBody117, protectedNode120, exceptionInput123, inputElement125, outputElement126, handler93, setupPart94, bodyPart96, regionAsInput129, regionAsOutput132},
    generalizations={gen_ActivitiesProv_ObjectNode_ActivityNode, gen_ActivitiesProv_ActivityParameterNode_ObjectNode, gen_ActivitiesProv_ControlNode_ActivityNode, gen_ActivitiesProv_ActivityFinalNode_ControlNode, gen_ActivitiesProv_ActivityFinalNode_FinalNode, gen_ActivitiesProv_InitialNode_ControlNode, gen_ActivitiesProv_ControlFlow_ActivityEdge, gen_ActivitiesProv_ObjectFlow_ActivityEdge, gen_ActivitiesProv_MergeNode_ControlNode, gen_ActivitiesProv_DecisionNode_ControlNode, gen_ActivitiesProv_ActivityPartition_ActivityGroup, gen_ActivitiesProv_DataStoreNode_CentralBufferNode, gen_ActivitiesProv_InterruptibleActivityRegion_ActivityGroup, gen_ActivitiesProv_StructuredActivityNode_ExecutableNode, gen_ActivitiesProv_StructuredActivityNode_ActivityGroup, gen_ActivitiesProv_ExecutableNode_ActivityNode, gen_ActivitiesProv_CentralBufferNode_ObjectNode, gen_ActivitiesProv_FinalNode_ControlNode, gen_ActivitiesProv_FlowFinalNode_FinalNode, gen_ActivitiesProv_ForkNode_ControlNode, gen_ActivitiesProv_JoinNode_ControlNode, gen_ActivitiesProv_ConditionalNode_StructuredActivityNode, gen_ActivitiesProv_SequenceNode_StructuredActivityNode, gen_ActivitiesProv_ExpansionRegion_StructuredActivityNode, gen_ActivitiesProv_ExpansionNode_ObjectNode, gen_ActivitiesProv_LoopNode_StructuredActivityNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)