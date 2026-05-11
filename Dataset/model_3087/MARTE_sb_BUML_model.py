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
ConstraintKind: Enumeration = Enumeration(
    name="ConstraintKind",
    literals={
            EnumerationLiteral(name="required"),
			EnumerationLiteral(name="offered"),
			EnumerationLiteral(name="contract")
    }
)

AssignmentKind: Enumeration = Enumeration(
    name="AssignmentKind",
    literals={
            EnumerationLiteral(name="structural"),
			EnumerationLiteral(name="behavioral"),
			EnumerationLiteral(name="hybrid")
    }
)

AllocationEndKind: Enumeration = Enumeration(
    name="AllocationEndKind",
    literals={
            
    }
)

AllocationNature: Enumeration = Enumeration(
    name="AllocationNature",
    literals={
            EnumerationLiteral(name="spatialDistribution"),
			EnumerationLiteral(name="timeScheduling")
    }
)

AllocationKind: Enumeration = Enumeration(
    name="AllocationKind",
    literals={
            
    }
)

AssignmentNature: Enumeration = Enumeration(
    name="AssignmentNature",
    literals={
            
    }
)

VariableDirectionKind: Enumeration = Enumeration(
    name="VariableDirectionKind",
    literals={
            EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout")
    }
)

PoolMgtPolicyKind: Enumeration = Enumeration(
    name="PoolMgtPolicyKind",
    literals={
            EnumerationLiteral(name="infiniteWait"),
			EnumerationLiteral(name="timedWait"),
			EnumerationLiteral(name="dynamic"),
			EnumerationLiteral(name="exception"),
			EnumerationLiteral(name="other")
    }
)

CallConcurrencyKind: Enumeration = Enumeration(
    name="CallConcurrencyKind",
    literals={
            EnumerationLiteral(name="sequential"),
			EnumerationLiteral(name="guarded"),
			EnumerationLiteral(name="concurrent")
    }
)

ISA_Type: Enumeration = Enumeration(
    name="ISA_Type",
    literals={
            EnumerationLiteral(name="RISC"),
			EnumerationLiteral(name="CISC"),
			EnumerationLiteral(name="VLIW"),
			EnumerationLiteral(name="SIMD"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef")
    }
)

SynchronizationKind: Enumeration = Enumeration(
    name="SynchronizationKind",
    literals={
            EnumerationLiteral(name="synchronous"),
			EnumerationLiteral(name="asynchronous"),
			EnumerationLiteral(name="delayedSynchronous"),
			EnumerationLiteral(name="rendezVous"),
			EnumerationLiteral(name="other")
    }
)

ExecutionKind: Enumeration = Enumeration(
    name="ExecutionKind",
    literals={
            EnumerationLiteral(name="deferred"),
			EnumerationLiteral(name="remoteImmediate"),
			EnumerationLiteral(name="localImmediate")
    }
)

ConcurrencyKind: Enumeration = Enumeration(
    name="ConcurrencyKind",
    literals={
            EnumerationLiteral(name="reader"),
			EnumerationLiteral(name="writer"),
			EnumerationLiteral(name="parallel")
    }
)

PLD_Technology: Enumeration = Enumeration(
    name="PLD_Technology",
    literals={
            EnumerationLiteral(name="SRAM"),
			EnumerationLiteral(name="antifuse"),
			EnumerationLiteral(name="flash"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef")
    }
)

PLD_Class: Enumeration = Enumeration(
    name="PLD_Class",
    literals={
            EnumerationLiteral(name="symetricalArray"),
			EnumerationLiteral(name="rowBased"),
			EnumerationLiteral(name="seaOfGates"),
			EnumerationLiteral(name="hierarchicalPLD"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef")
    }
)

Repl_Policy: Enumeration = Enumeration(
    name="Repl_Policy",
    literals={
            EnumerationLiteral(name="LRU"),
			EnumerationLiteral(name="NFU"),
			EnumerationLiteral(name="FIFO"),
			EnumerationLiteral(name="random"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef")
    }
)

WritePolicy: Enumeration = Enumeration(
    name="WritePolicy",
    literals={
            EnumerationLiteral(name="writeBack"),
			EnumerationLiteral(name="writeThrough"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef")
    }
)

CacheType: Enumeration = Enumeration(
    name="CacheType",
    literals={
            EnumerationLiteral(name="data"),
			EnumerationLiteral(name="instruction"),
			EnumerationLiteral(name="unified"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef")
    }
)

ROM_Type: Enumeration = Enumeration(
    name="ROM_Type",
    literals={
            EnumerationLiteral(name="maskedROM"),
			EnumerationLiteral(name="EPROM"),
			EnumerationLiteral(name="OTP_EPROM"),
			EnumerationLiteral(name="EEPROM"),
			EnumerationLiteral(name="Flash"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef")
    }
)

ConditionType: Enumeration = Enumeration(
    name="ConditionType",
    literals={
            EnumerationLiteral(name="temperature"),
			EnumerationLiteral(name="humidity"),
			EnumerationLiteral(name="altitude"),
			EnumerationLiteral(name="vibration"),
			EnumerationLiteral(name="shock"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef")
    }
)

ComponentKind: Enumeration = Enumeration(
    name="ComponentKind",
    literals={
            EnumerationLiteral(name="card"),
			EnumerationLiteral(name="channel"),
			EnumerationLiteral(name="chip"),
			EnumerationLiteral(name="port"),
			EnumerationLiteral(name="unit"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef")
    }
)

ComponentState: Enumeration = Enumeration(
    name="ComponentState",
    literals={
            EnumerationLiteral(name="operating"),
			EnumerationLiteral(name="storage"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef")
    }
)

InterruptKind: Enumeration = Enumeration(
    name="InterruptKind",
    literals={
            EnumerationLiteral(name="HardwareInterruption"),
			EnumerationLiteral(name="ProcessorDetectedException"),
			EnumerationLiteral(name="ProgrammedException"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other")
    }
)

AccessPolicyKind: Enumeration = Enumeration(
    name="AccessPolicyKind",
    literals={
            EnumerationLiteral(name="Read"),
			EnumerationLiteral(name="Write"),
			EnumerationLiteral(name="ReadWrite"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other")
    }
)

QueuePolicyKind: Enumeration = Enumeration(
    name="QueuePolicyKind",
    literals={
            EnumerationLiteral(name="FIFO"),
			EnumerationLiteral(name="LIFO"),
			EnumerationLiteral(name="Priority"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other")
    }
)

MessageResourceKind: Enumeration = Enumeration(
    name="MessageResourceKind",
    literals={
            EnumerationLiteral(name="MessageQueue"),
			EnumerationLiteral(name="Pipe"),
			EnumerationLiteral(name="Blackboard"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other")
    }
)

NotificationKind: Enumeration = Enumeration(
    name="NotificationKind",
    literals={
            EnumerationLiteral(name="Memorized"),
			EnumerationLiteral(name="Bounded"),
			EnumerationLiteral(name="Memoryless"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other")
    }
)

NotificationResourceKind: Enumeration = Enumeration(
    name="NotificationResourceKind",
    literals={
            EnumerationLiteral(name="Event"),
			EnumerationLiteral(name="Barrier"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other")
    }
)

MutualExclusionResourceKind: Enumeration = Enumeration(
    name="MutualExclusionResourceKind",
    literals={
            EnumerationLiteral(name="BooleanSemaphore"),
			EnumerationLiteral(name="CountSemaphore"),
			EnumerationLiteral(name="Mutex"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other")
    }
)

ConcurrentAccessProtocolKind: Enumeration = Enumeration(
    name="ConcurrentAccessProtocolKind",
    literals={
            EnumerationLiteral(name="PIP"),
			EnumerationLiteral(name="PCP"),
			EnumerationLiteral(name="NoPreemption"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other")
    }
)

PortSpecificationKind: Enumeration = Enumeration(
    name="PortSpecificationKind",
    literals={
            EnumerationLiteral(name="atomic"),
			EnumerationLiteral(name="interfaceBased"),
			EnumerationLiteral(name="featureBased")
    }
)

FlowDirectionKind: Enumeration = Enumeration(
    name="FlowDirectionKind",
    literals={
            EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="out")
    }
)

ClientServerKind: Enumeration = Enumeration(
    name="ClientServerKind",
    literals={
            EnumerationLiteral(name="required"),
			EnumerationLiteral(name="provided"),
			EnumerationLiteral(name="proreq")
    }
)

DataPoolOrderingKind: Enumeration = Enumeration(
    name="DataPoolOrderingKind",
    literals={
            EnumerationLiteral(name="FIFO"),
			EnumerationLiteral(name="LIFO"),
			EnumerationLiteral(name="UserDefined")
    }
)

LaxityKind: Enumeration = Enumeration(
    name="LaxityKind",
    literals={
            EnumerationLiteral(name="hard"),
			EnumerationLiteral(name="soft"),
			EnumerationLiteral(name="other")
    }
)

OptimallityCriterionKind: Enumeration = Enumeration(
    name="OptimallityCriterionKind",
    literals={
            EnumerationLiteral(name="meetHardDeadlines"),
			EnumerationLiteral(name="minimizeMissedDeadlines"),
			EnumerationLiteral(name="minimizedMeanTardiness"),
			EnumerationLiteral(name="undef"),
			EnumerationLiteral(name="other")
    }
)

# Classes
NFPs_MARTE_Property = Class(name="NFPs_MARTE_Property")
MARTE_NFPs_Unit = Class(name="MARTE_NFPs_Unit")
NFPs_Unit = Class(name="NFPs_Unit")
MARTE_NFPs_Nfp = Class(name="MARTE_NFPs_Nfp")
MARTE_CoreElements_ModeBehavior = Class(name="MARTE_CoreElements_ModeBehavior")
CoreElements_MARTE_StateMachine = Class(name="CoreElements_MARTE_StateMachine")
MARTE_CoreElements_Configuration = Class(name="MARTE_CoreElements_Configuration")
CoreElements_MARTE_StructuredClassifier = Class(name="CoreElements_MARTE_StructuredClassifier")
CoreElements_MARTE_Package = Class(name="CoreElements_MARTE_Package")
NFPs_MARTE_EnumerationLiteral = Class(name="NFPs_MARTE_EnumerationLiteral")
MARTE_NFPs_NfpConstraint = Class(name="MARTE_NFPs_NfpConstraint")
NFPs_MARTE_Constraint = Class(name="NFPs_MARTE_Constraint")
CoreElements_Mode = Class(name="CoreElements_Mode")
MARTE_NFPs_NfpType = Class(name="MARTE_NFPs_NfpType")
TupleType = Class(name="TupleType")
MARTE_NFPs_Dimension = Class(name="MARTE_NFPs_Dimension")
NFPs_Dimension = Class(name="NFPs_Dimension")
NFPs_MARTE_Enumeration = Class(name="NFPs_MARTE_Enumeration")
MARTE_CoreElements_ModeTransition = Class(name="MARTE_CoreElements_ModeTransition")
CoreElements_MARTE_Transition = Class(name="CoreElements_MARTE_Transition")
Alloc_MARTE_Element = Class(name="Alloc_MARTE_Element")
Alloc_MARTE_Comment = Class(name="Alloc_MARTE_Comment")
MARTE_CoreElements_Mode = Class(name="MARTE_CoreElements_Mode")
CoreElements_MARTE_State = Class(name="CoreElements_MARTE_State")
MARTE_Alloc_Allocated = Class(name="MARTE_Alloc_Allocated")
Alloc_MARTE_NamedElement = Class(name="Alloc_MARTE_NamedElement")
Alloc_Allocated = Class(name="Alloc_Allocated")
MARTE_Alloc_AllocateActivityGroup = Class(name="MARTE_Alloc_AllocateActivityGroup")
Alloc_MARTE_ActivityPartition = Class(name="Alloc_MARTE_ActivityPartition")
MARTE_Alloc_NfpRefine = Class(name="MARTE_Alloc_NfpRefine")
Alloc_MARTE_Dependency = Class(name="Alloc_MARTE_Dependency")
NFPs_NfpConstraint = Class(name="NFPs_NfpConstraint")
MARTE_Alloc_Assign = Class(name="MARTE_Alloc_Assign")
Time_MARTE_Operation = Class(name="Time_MARTE_Operation")
MARTE_Alloc_Allocate = Class(name="MARTE_Alloc_Allocate")
Alloc_MARTE_Abstraction = Class(name="Alloc_MARTE_Abstraction")
MARTE_Time_TimedDomain = Class(name="MARTE_Time_TimedDomain")
Time_MARTE_Namespace = Class(name="Time_MARTE_Namespace")
MARTE_Time_Clock = Class(name="MARTE_Time_Clock")
Time_MARTE_InstanceSpecification = Class(name="Time_MARTE_InstanceSpecification")
Time_ClockType = Class(name="Time_ClockType")
Time_MARTE_Property = Class(name="Time_MARTE_Property")
MARTE_Time_ClockType = Class(name="MARTE_Time_ClockType")
Time_MARTE_Enumeration = Class(name="Time_MARTE_Enumeration")
Time_MARTE_TimeObservation = Class(name="Time_MARTE_TimeObservation")
MARTE_Time_TimedDurationObservation = Class(name="MARTE_Time_TimedDurationObservation")
Time_MARTE_DurationObservation = Class(name="Time_MARTE_DurationObservation")
MARTE_Time_TimedEvent = Class(name="MARTE_Time_TimedEvent")
Time_MARTE_Class = Class(name="Time_MARTE_Class")
MARTE_Time_TimedElement = Class(name="MARTE_Time_TimedElement", is_abstract=True)
Time_Clock = Class(name="Time_Clock")
MARTE_Time_TimedValueSpecification = Class(name="MARTE_Time_TimedValueSpecification")
TimedElement = Class(name="TimedElement")
Time_MARTE_ValueSpecification = Class(name="Time_MARTE_ValueSpecification")
MARTE_Time_TimedConstraint = Class(name="MARTE_Time_TimedConstraint")
Time_TimedElement = Class(name="Time_TimedElement")
MARTE_Time_ClockConstraint = Class(name="MARTE_Time_ClockConstraint")
MARTE_Time_TimedObservation = Class(name="MARTE_Time_TimedObservation", is_abstract=True)
MARTE_Time_TimedInstantObservation = Class(name="MARTE_Time_TimedInstantObservation")
TimedObservation = Class(name="TimedObservation")
GRM_MARTE_Classifier = Class(name="GRM_MARTE_Classifier")
GRM_MARTE_Lifeline = Class(name="GRM_MARTE_Lifeline")
GRM_MARTE_ConnectableElement = Class(name="GRM_MARTE_ConnectableElement")
MARTE_GRM_StorageResource = Class(name="MARTE_GRM_StorageResource")
Resource = Class(name="Resource")
Time_MARTE_TimeEvent = Class(name="Time_MARTE_TimeEvent")
MARTE_Time_TimedProcessing = Class(name="MARTE_Time_TimedProcessing")
Time_MARTE_Action = Class(name="Time_MARTE_Action")
Time_MARTE_Behavior = Class(name="Time_MARTE_Behavior")
Time_MARTE_Message = Class(name="Time_MARTE_Message")
Time_MARTE_Event = Class(name="Time_MARTE_Event")
MARTE_GRM_Resource = Class(name="MARTE_GRM_Resource")
NFP_Integer = Class(name="NFP_Integer")
GRM_MARTE_Property = Class(name="GRM_MARTE_Property")
GRM_MARTE_InstanceSpecification = Class(name="GRM_MARTE_InstanceSpecification")
MARTE_GRM_ComputingResource = Class(name="MARTE_GRM_ComputingResource")
ProcessingResource = Class(name="ProcessingResource")
MARTE_GRM_MutualExclusionResource = Class(name="MARTE_GRM_MutualExclusionResource")
MARTE_GRM_CommunicationEndPoint = Class(name="MARTE_GRM_CommunicationEndPoint")
MARTE_GRM_SynchronizationResource = Class(name="MARTE_GRM_SynchronizationResource")
MARTE_GRM_ConcurrencyResource = Class(name="MARTE_GRM_ConcurrencyResource")
MARTE_GRM_Scheduler = Class(name="MARTE_GRM_Scheduler")
GRM_MARTE_OpaqueExpression = Class(name="GRM_MARTE_OpaqueExpression")
GRM_ProcessingResource = Class(name="GRM_ProcessingResource")
GRM_ComputingResource = Class(name="GRM_ComputingResource")
GRM_MutualExclusionResource = Class(name="GRM_MutualExclusionResource")
GRM_SchedulableResource = Class(name="GRM_SchedulableResource")
MARTE_GRM_ProcessingResource = Class(name="MARTE_GRM_ProcessingResource")
NFP_Real = Class(name="NFP_Real")
GRM_Scheduler = Class(name="GRM_Scheduler")
MARTE_GRM_TimingResource = Class(name="MARTE_GRM_TimingResource")
MARTE_GRM_ClockResource = Class(name="MARTE_GRM_ClockResource")
TimingResource = Class(name="TimingResource")
MARTE_GRM_TimerResource = Class(name="MARTE_GRM_TimerResource")
MARTE_GRM_SchedulableResource = Class(name="MARTE_GRM_SchedulableResource")
SchedParameters = Class(name="SchedParameters")
GRM_SecondaryScheduler = Class(name="GRM_SecondaryScheduler")
MARTE_GRM_SecondaryScheduler = Class(name="MARTE_GRM_SecondaryScheduler")
Scheduler = Class(name="Scheduler")
MARTE_GRM_CommunicationMedia = Class(name="MARTE_GRM_CommunicationMedia")
GRM_MARTE_Connector = Class(name="GRM_MARTE_Connector")
NFP_Duration = Class(name="NFP_Duration")
NFP_DataTxRate = Class(name="NFP_DataTxRate")
MARTE_GRM_DeviceResource = Class(name="MARTE_GRM_DeviceResource")
GRM_MARTE_NamedElement = Class(name="GRM_MARTE_NamedElement")
GRM_ResourceUsage = Class(name="GRM_ResourceUsage")
MARTE_GRM_GrService = Class(name="MARTE_GRM_GrService")
GRM_Resource = Class(name="GRM_Resource")
GRM_MARTE_ExecutionSpecification = Class(name="GRM_MARTE_ExecutionSpecification")
GRM_MARTE_BehavioralFeature = Class(name="GRM_MARTE_BehavioralFeature")
GRM_MARTE_Behavior = Class(name="GRM_MARTE_Behavior")
GRM_MARTE_Collaboration = Class(name="GRM_MARTE_Collaboration")
GRM_MARTE_CollaborationUse = Class(name="GRM_MARTE_CollaborationUse")
MARTE_GRM_Release = Class(name="MARTE_GRM_Release")
GrService = Class(name="GrService")
MARTE_GRM_Acquire = Class(name="MARTE_GRM_Acquire")
MARTE_GRM_ResourceUsage = Class(name="MARTE_GRM_ResourceUsage")
NFP_DataSize = Class(name="NFP_DataSize")
NFP_Power = Class(name="NFP_Power")
NFP_Energy = Class(name="NFP_Energy")
MARTE_RSM_Tiler = Class(name="MARTE_RSM_Tiler")
IntegerMatrix = Class(name="IntegerMatrix")
MARTE_RSM_LinkTopology = Class(name="MARTE_RSM_LinkTopology", is_abstract=True)
RSM_MARTE_Connector = Class(name="RSM_MARTE_Connector")
MARTE_RSM_DefaultLink = Class(name="MARTE_RSM_DefaultLink")
LinkTopology = Class(name="LinkTopology")
MARTE_RSM_InterRepetition = Class(name="MARTE_RSM_InterRepetition")
IntegerVector = Class(name="IntegerVector")
MARTE_RSM_Distribute = Class(name="MARTE_RSM_Distribute")
Allocate = Class(name="Allocate")
ShapeSpecification = Class(name="ShapeSpecification")
TilerSpecification = Class(name="TilerSpecification")
MARTE_RSM_Reshape = Class(name="MARTE_RSM_Reshape")
DataTypes_MARTE_DataType = Class(name="DataTypes_MARTE_DataType")
MARTE_DataTypes_IntervalType = Class(name="MARTE_DataTypes_IntervalType")
MARTE_DataTypes_CollectionType = Class(name="MARTE_DataTypes_CollectionType")
RSM_MARTE_ConnectorEnd = Class(name="RSM_MARTE_ConnectorEnd")
MARTE_RSM_Shaped = Class(name="MARTE_RSM_Shaped")
RSM_MARTE_MultiplicityElement = Class(name="RSM_MARTE_MultiplicityElement")
MARTE_Variables_Var = Class(name="MARTE_Variables_Var")
Variables_MARTE_Property = Class(name="Variables_MARTE_Property")
MARTE_Variables_ExpressionContext = Class(name="MARTE_Variables_ExpressionContext")
Variables_MARTE_NamedElement = Class(name="Variables_MARTE_NamedElement")
MARTE_DataTypes_BoundedSubtype = Class(name="MARTE_DataTypes_BoundedSubtype")
DataTypes_MARTE_Property = Class(name="DataTypes_MARTE_Property")
HLAM_MARTE_BehavioredClassifier = Class(name="HLAM_MARTE_BehavioredClassifier")
MARTE_DataTypes_ChoiceType = Class(name="MARTE_DataTypes_ChoiceType")
MARTE_DataTypes_TupleType = Class(name="MARTE_DataTypes_TupleType")
MARTE_HLAM_RtUnit = Class(name="MARTE_HLAM_RtUnit")
HLAM_MARTE_Behavior = Class(name="HLAM_MARTE_Behavior")
HLAM_MARTE_Operation = Class(name="HLAM_MARTE_Operation")
MARTE_HLAM_RtSpecification = Class(name="MARTE_HLAM_RtSpecification")
UtilityType = Class(name="UtilityType")
ArrivalPattern = Class(name="ArrivalPattern")
Time_TimedInstantObservation = Class(name="Time_TimedInstantObservation")
MARTE_HLAM_PpUnit = Class(name="MARTE_HLAM_PpUnit")
MARTE_HLAM_RtFeature = Class(name="MARTE_HLAM_RtFeature")
HLAM_MARTE_BehavioralFeature = Class(name="HLAM_MARTE_BehavioralFeature")
HLAM_MARTE_Message = Class(name="HLAM_MARTE_Message")
HLAM_MARTE_Signal = Class(name="HLAM_MARTE_Signal")
HLAM_MARTE_Port = Class(name="HLAM_MARTE_Port")
HLAM_MARTE_InvocationAction = Class(name="HLAM_MARTE_InvocationAction")
HLAM_RtSpecification = Class(name="HLAM_RtSpecification")
NFP_Percentage = Class(name="NFP_Percentage")
HLAM_MARTE_Comment = Class(name="HLAM_MARTE_Comment")
NFP_DateTime = Class(name="NFP_DateTime")
MARTE_HLAM_RtAction = Class(name="MARTE_HLAM_RtAction")
MARTE_HLAM_RtService = Class(name="MARTE_HLAM_RtService")
HwComputing_HwISA = Class(name="HwComputing_HwISA")
MARTE_HwComputing_PLD_Organization = Class(name="MARTE_HwComputing_PLD_Organization")
NFP_Natural = Class(name="NFP_Natural")
MARTE_HwComputing_HwProcessor = Class(name="MARTE_HwComputing_HwProcessor")
HwComputingResource = Class(name="HwComputingResource")
HwMemory_HwRAM = Class(name="HwMemory_HwRAM")
HwComputing_HwBranchPredictor = Class(name="HwComputing_HwBranchPredictor")
HwMemory_HwCache = Class(name="HwMemory_HwCache")
HwStorageManager_HwMMU = Class(name="HwStorageManager_HwMMU")
MARTE_HwComputing_HwComputingResource = Class(name="MARTE_HwComputing_HwComputingResource")
HwGeneral_HwResource = Class(name="HwGeneral_HwResource")
NFP_FrequencyInterval = Class(name="NFP_FrequencyInterval")
MARTE_HwComputing_HwISA = Class(name="MARTE_HwComputing_HwISA")
HwResource = Class(name="HwResource")
NFP_String = Class(name="NFP_String")
MARTE_HwComputing_HwBranchPredictor = Class(name="MARTE_HwComputing_HwBranchPredictor")
MARTE_HwComputing_HwASIC = Class(name="MARTE_HwComputing_HwASIC")
MARTE_HwComputing_HwPLD = Class(name="MARTE_HwComputing_HwPLD")
HwComputing_PLD_Organization = Class(name="HwComputing_PLD_Organization")
HwCommunication_HwArbiter = Class(name="HwCommunication_HwArbiter")
MARTE_HwCommunication_HwBus = Class(name="MARTE_HwCommunication_HwBus")
HwMedia = Class(name="HwMedia")
HwComputing_HwComputingResource = Class(name="HwComputing_HwComputingResource")
MARTE_HwComputing_HwMCU = Class(name="MARTE_HwComputing_HwMCU")
HwComputing_HwProcessor = Class(name="HwComputing_HwProcessor")
HwDevice_HwPeripheral = Class(name="HwDevice_HwPeripheral")
HwRegister_HwRegister = Class(name="HwRegister_HwRegister")
HwPackage_HwPackage = Class(name="HwPackage_HwPackage")
HwIO_HwPin = Class(name="HwIO_HwPin")
HwCommunication_HwPort = Class(name="HwCommunication_HwPort")
MARTE_HwCommunication_HwCommunicationResource = Class(name="MARTE_HwCommunication_HwCommunicationResource")
MARTE_HwCommunication_HwArbiter = Class(name="MARTE_HwCommunication_HwArbiter")
HwCommunicationResource = Class(name="HwCommunicationResource")
HwCommunication_HwMedia = Class(name="HwCommunication_HwMedia")
MARTE_HwCommunication_HwMedia = Class(name="MARTE_HwCommunication_HwMedia")
GRM_CommunicationMedia = Class(name="GRM_CommunicationMedia")
HwCommunication_HwCommunicationResource = Class(name="HwCommunication_HwCommunicationResource")
MARTE_HwStorageManager_HwMMU = Class(name="MARTE_HwStorageManager_HwMMU")
HwStorageManager = Class(name="HwStorageManager")
NFP_Boolean = Class(name="NFP_Boolean")
MARTE_HwCommunication_HwBridge = Class(name="MARTE_HwCommunication_HwBridge")
MARTE_HwCommunication_HwEndPoint = Class(name="MARTE_HwCommunication_HwEndPoint")
GRM_CommunicationEndPoint = Class(name="GRM_CommunicationEndPoint")
MARTE_HwCommunication_HwPort = Class(name="MARTE_HwCommunication_HwPort")
HwEndPoint = Class(name="HwEndPoint")
MARTE_HwCommunication_HwConnection = Class(name="MARTE_HwCommunication_HwConnection")
HwProtocol_HwProtocol = Class(name="HwProtocol_HwProtocol")
MARTE_HwStorageManager_HwStorageManager = Class(name="MARTE_HwStorageManager_HwStorageManager")
GRM_StorageResource = Class(name="GRM_StorageResource")
HwMemory_HwMemory = Class(name="HwMemory_HwMemory")
MARTE_HwStorageManager_HwDMA = Class(name="MARTE_HwStorageManager_HwDMA")
HwStorageManager_HwStorageManager = Class(name="HwStorageManager_HwStorageManager")
MARTE_HwMemory_HwMemory = Class(name="MARTE_HwMemory_HwMemory")
HwMemory_Timing = Class(name="HwMemory_Timing")
MARTE_HwMemory_Timing = Class(name="MARTE_HwMemory_Timing")
MARTE_HwMemory_HwROM = Class(name="MARTE_HwMemory_HwROM")
MARTE_HwMemory_CacheStructure = Class(name="MARTE_HwMemory_CacheStructure")
MARTE_HwMemory_MemoryOrganization = Class(name="MARTE_HwMemory_MemoryOrganization")
MARTE_HwMemory_HwRAM = Class(name="MARTE_HwMemory_HwRAM")
HwMemory = Class(name="HwMemory")
HwMemory_MemoryOrganization = Class(name="HwMemory_MemoryOrganization")
HwTiming_HwClock = Class(name="HwTiming_HwClock")
MARTE_HwDevice_HwDevice = Class(name="MARTE_HwDevice_HwDevice")
GRM_DeviceResource = Class(name="GRM_DeviceResource")
HwDeviceFunction_HwDeviceFunction = Class(name="HwDeviceFunction_HwDeviceFunction")
MARTE_HwMemory_HwDrive = Class(name="MARTE_HwMemory_HwDrive")
MARTE_HwMemory_HwCache = Class(name="MARTE_HwMemory_HwCache")
HwMemory_CacheStructure = Class(name="HwMemory_CacheStructure")
MARTE_HwTiming_HwTimingResource = Class(name="MARTE_HwTiming_HwTimingResource")
GRM_TimingResource = Class(name="GRM_TimingResource")
MARTE_HwTiming_HwClock = Class(name="MARTE_HwTiming_HwClock")
HwTimingResource = Class(name="HwTimingResource")
MARTE_HwTiming_HwTimer = Class(name="MARTE_HwTiming_HwTimer")
MARTE_HwGeneral_HwResourceService = Class(name="MARTE_HwGeneral_HwResourceService")
MARTE_HwGeneral_HwResource = Class(name="MARTE_HwGeneral_HwResource")
MARTE_HwDevice_HwI_O = Class(name="MARTE_HwDevice_HwI_O")
HwDevice = Class(name="HwDevice")
MARTE_HwDevice_HwSupport = Class(name="MARTE_HwDevice_HwSupport")
MARTE_HwDevice_HWActuator = Class(name="MARTE_HwDevice_HWActuator")
HwI_O = Class(name="HwI_O")
MARTE_HwDevice_HWSensor = Class(name="MARTE_HwDevice_HWSensor")
MARTE_HwDevice_HwPeripheral = Class(name="MARTE_HwDevice_HwPeripheral")
HwPeripheral_OperationImpl = Class(name="HwPeripheral_OperationImpl")
HwPeripheral_PeripheralActivity = Class(name="HwPeripheral_PeripheralActivity")
NFP_Area = Class(name="NFP_Area")
NFP_NaturalInterval = Class(name="NFP_NaturalInterval")
HwGeneral_HwResourceService = Class(name="HwGeneral_HwResourceService")
HwCommunication_HwEndPoint = Class(name="HwCommunication_HwEndPoint")
NFP_Frequency = Class(name="NFP_Frequency")
HwGeneral_MARTE_Operation = Class(name="HwGeneral_MARTE_Operation")
HwGeneral_MARTE_Activity = Class(name="HwGeneral_MARTE_Activity")
MARTE_HwLayout_HwComponent = Class(name="MARTE_HwLayout_HwComponent")
NFP_Length = Class(name="NFP_Length")
Realnterval = Class(name="Realnterval")
NFP_Price = Class(name="NFP_Price")
HwLayout_Env_Condition = Class(name="HwLayout_Env_Condition")
HwLayout_HwComponent = Class(name="HwLayout_HwComponent")
MARTE_HwLayout_Env_Condition = Class(name="MARTE_HwLayout_Env_Condition")
MARTE_HwPower_HwCoolingSupply = Class(name="MARTE_HwPower_HwCoolingSupply")
MARTE_HwPower_HwPowerSupply = Class(name="MARTE_HwPower_HwPowerSupply")
HwComponent = Class(name="HwComponent")
HwPackage_HwPackagePin = Class(name="HwPackage_HwPackagePin")
HwIO_HwLine = Class(name="HwIO_HwLine")
MARTE_HwIO_HwLine = Class(name="MARTE_HwIO_HwLine")
MARTE_HwPeripheral_OperationImpl = Class(name="MARTE_HwPeripheral_OperationImpl")
Operation = Class(name="Operation")
HwPeripheral_MARTE_Operation = Class(name="HwPeripheral_MARTE_Operation")
MARTE_HwPeripheral_RegisterAction = Class(name="MARTE_HwPeripheral_RegisterAction", is_abstract=True)
Action = Class(name="Action")
MARTE_HwPeripheral_WriteRegisterAction = Class(name="MARTE_HwPeripheral_WriteRegisterAction")
RegisterAction = Class(name="RegisterAction")
HwPeripheral_MARTE_InputPin = Class(name="HwPeripheral_MARTE_InputPin")
MARTE_HwPeripheral_ReadRegisterAction = Class(name="MARTE_HwPeripheral_ReadRegisterAction")
HwPeripheral_MARTE_OutputPin = Class(name="HwPeripheral_MARTE_OutputPin")
MARTE_HwPeripheral_PeripheralActivity = Class(name="MARTE_HwPeripheral_PeripheralActivity")
Activity = Class(name="Activity")
HwPeripheral_RegisterAction = Class(name="HwPeripheral_RegisterAction")
MARTE_HwDeviceFunction_HwDeviceFunction = Class(name="MARTE_HwDeviceFunction_HwDeviceFunction")
MARTE_HwIO_HwPin = Class(name="MARTE_HwIO_HwPin")
MARTE_HwPackage_HwWire = Class(name="MARTE_HwPackage_HwWire")
MARTE_HwProtocol_HwProtocol = Class(name="MARTE_HwProtocol_HwProtocol")
HwProtocol_MARTE_Operation = Class(name="HwProtocol_MARTE_Operation")
MARTE_HwDiagram_HwBlockDiagram = Class(name="MARTE_HwDiagram_HwBlockDiagram")
MARTE_HwRegister_HwRegister = Class(name="MARTE_HwRegister_HwRegister")
MARTE_HwDatasheet_HwDatasheet = Class(name="MARTE_HwDatasheet_HwDatasheet")
MARTE_HwPackage_HwPackage = Class(name="MARTE_HwPackage_HwPackage")
MARTE_HwPackage_HwPackagePin = Class(name="MARTE_HwPackage_HwPackagePin")
HwPackage_HwWire = Class(name="HwPackage_HwWire")
MARTE_HwDiagram_HwHRMDiagram = Class(name="MARTE_HwDiagram_HwHRMDiagram")
HwCommunication_HwConnection = Class(name="HwCommunication_HwConnection")
MARTE_HwDiagram_HwCircuitDiagram = Class(name="MARTE_HwDiagram_HwCircuitDiagram")
MARTE_SW_ResourceCore_SwAccessService = Class(name="MARTE_SW_ResourceCore_SwAccessService")
HwDiagram_MARTE_DataType = Class(name="HwDiagram_MARTE_DataType")
SW_ResourceCore_MARTE_Property = Class(name="SW_ResourceCore_MARTE_Property")
MARTE_HwDiagram_SRMDiagram = Class(name="MARTE_HwDiagram_SRMDiagram")
SW_Brokering_DeviceBroker = Class(name="SW_Brokering_DeviceBroker")
MARTE_SW_Concurrency_EntryPoint = Class(name="MARTE_SW_Concurrency_EntryPoint")
MARTE_SW_ResourceCore_SwResource = Class(name="MARTE_SW_ResourceCore_SwResource", is_abstract=True)
SW_Concurrency_MARTE_BehavioralFeature = Class(name="SW_Concurrency_MARTE_BehavioralFeature")
SW_ResourceCore_MARTE_TypedElement = Class(name="SW_ResourceCore_MARTE_TypedElement")
SW_ResourceCore_MARTE_BehavioralFeature = Class(name="SW_ResourceCore_MARTE_BehavioralFeature")
MARTE_SW_Concurrency_SwConcurrentResource = Class(name="MARTE_SW_Concurrency_SwConcurrentResource", is_abstract=True)
SwResource = Class(name="SwResource")
SW_Concurrency_MARTE_Element = Class(name="SW_Concurrency_MARTE_Element")
SW_Concurrency_MARTE_TypedElement = Class(name="SW_Concurrency_MARTE_TypedElement")
SwConcurrentResource = Class(name="SwConcurrentResource")
MARTE_SW_Concurrency_SwSchedulableResource = Class(name="MARTE_SW_Concurrency_SwSchedulableResource")
SW_Concurrency_SwConcurrentResource = Class(name="SW_Concurrency_SwConcurrentResource")
SW_Concurrency_MARTE_NamedElement = Class(name="SW_Concurrency_MARTE_NamedElement")
MARTE_SW_Concurrency_InterruptResource = Class(name="MARTE_SW_Concurrency_InterruptResource")
MARTE_SW_Concurrency_SwTimerResource = Class(name="MARTE_SW_Concurrency_SwTimerResource")
TimerResource = Class(name="TimerResource")
MARTE_SW_Concurrency_MemoryPartition = Class(name="MARTE_SW_Concurrency_MemoryPartition")
SW_Concurrency_MARTE_Namespace = Class(name="SW_Concurrency_MARTE_Namespace")
MARTE_SW_Concurrency_Alarm = Class(name="MARTE_SW_Concurrency_Alarm")
InterruptResource = Class(name="InterruptResource")
SW_Brokering_MARTE_TypedElement = Class(name="SW_Brokering_MARTE_TypedElement")
SW_Brokering_MARTE_BehavioralFeature = Class(name="SW_Brokering_MARTE_BehavioralFeature")
SW_Brokering_MARTE_Operation = Class(name="SW_Brokering_MARTE_Operation")
SW_Brokering_MARTE_Activity = Class(name="SW_Brokering_MARTE_Activity")
MARTE_SW_Brokering_MemoryBroker = Class(name="MARTE_SW_Brokering_MemoryBroker")
MARTE_SW_Brokering_DeviceBroker = Class(name="MARTE_SW_Brokering_DeviceBroker")
SW_Interaction_MARTE_TypedElement = Class(name="SW_Interaction_MARTE_TypedElement")
MARTE_SW_Interaction_SwCommunicationResource = Class(name="MARTE_SW_Interaction_SwCommunicationResource", is_abstract=True)
SW_Interaction_SwInteractionResource = Class(name="SW_Interaction_SwInteractionResource")
MARTE_SW_Interaction_SwSynchronizationResource = Class(name="MARTE_SW_Interaction_SwSynchronizationResource", is_abstract=True)
GRM_SynchronizationResource = Class(name="GRM_SynchronizationResource")
MARTE_SW_Interaction_SharedDataComResource = Class(name="MARTE_SW_Interaction_SharedDataComResource")
SwCommunicationResource = Class(name="SwCommunicationResource")
SW_Interaction_MARTE_BehavioralFeature = Class(name="SW_Interaction_MARTE_BehavioralFeature")
MARTE_SW_Interaction_MessageComResource = Class(name="MARTE_SW_Interaction_MessageComResource")
MARTE_SW_Interaction_SwInteractionResource = Class(name="MARTE_SW_Interaction_SwInteractionResource", is_abstract=True)
MARTE_SW_Interaction_SwMutualExclusionResource = Class(name="MARTE_SW_Interaction_SwMutualExclusionResource")
SW_Interaction_SwSynchronizationResource = Class(name="SW_Interaction_SwSynchronizationResource")
MARTE_SW_Interaction_NotificationResource = Class(name="MARTE_SW_Interaction_NotificationResource")
SwSynchronizationResource = Class(name="SwSynchronizationResource")
MARTE_GCM_FlowPort = Class(name="MARTE_GCM_FlowPort")
GCM_MARTE_Port = Class(name="GCM_MARTE_Port")
MARTE_GCM_ClientServerPort = Class(name="MARTE_GCM_ClientServerPort")
GCM_MARTE_Interface = Class(name="GCM_MARTE_Interface")
GCM_ClientServerSpecification = Class(name="GCM_ClientServerSpecification")
MARTE_GCM_FlowProperty = Class(name="MARTE_GCM_FlowProperty")
GCM_MARTE_Property = Class(name="GCM_MARTE_Property")
MARTE_GCM_ClientServerFeature = Class(name="MARTE_GCM_ClientServerFeature")
GCM_MARTE_BehavioralFeature = Class(name="GCM_MARTE_BehavioralFeature")
MARTE_GCM_GCMTrigger = Class(name="MARTE_GCM_GCMTrigger")
GCM_MARTE_Trigger = Class(name="GCM_MARTE_Trigger")
GCM_MARTE_Feature = Class(name="GCM_MARTE_Feature")
MARTE_GCM_GCMInvocationAction = Class(name="MARTE_GCM_GCMInvocationAction")
GCM_MARTE_InvocationAction = Class(name="GCM_MARTE_InvocationAction")
MARTE_GCM_DataEvent = Class(name="MARTE_GCM_DataEvent")
GCM_MARTE_AnyReceiveEvent = Class(name="GCM_MARTE_AnyReceiveEvent")
GCM_MARTE_Classifier = Class(name="GCM_MARTE_Classifier")
MARTE_GCM_DataPool = Class(name="MARTE_GCM_DataPool")
MARTE_GCM_ClientServerSpecification = Class(name="MARTE_GCM_ClientServerSpecification")
MARTE_GCM_FlowSpecification = Class(name="MARTE_GCM_FlowSpecification")
GQAM_MARTE_Behavior = Class(name="GQAM_MARTE_Behavior")
MARTE_GQAM_GaEventTrace = Class(name="MARTE_GQAM_GaEventTrace")
GQAM_MARTE_NamedElement = Class(name="GQAM_MARTE_NamedElement")
MARTE_GQAM_GaWorkloadEvent = Class(name="MARTE_GQAM_GaWorkloadEvent")
GQAM_GaWorkloadGenerator = Class(name="GQAM_GaWorkloadGenerator")
GQAM_GaEventTrace = Class(name="GQAM_GaEventTrace")
GQAM_GaScenario = Class(name="GQAM_GaScenario")
GQAM_MARTE_TimeEvent = Class(name="GQAM_MARTE_TimeEvent")
GCM_MARTE_Behavior = Class(name="GCM_MARTE_Behavior")
MARTE_GQAM_GaWorkloadGenerator = Class(name="MARTE_GQAM_GaWorkloadGenerator")
MARTE_GQAM_GaScenario = Class(name="MARTE_GQAM_GaScenario")
Time_TimedProcessing = Class(name="Time_TimedProcessing")
GQAM_GaWorkloadEvent = Class(name="GQAM_GaWorkloadEvent")
GQAM_GaExecHost = Class(name="GQAM_GaExecHost")
GQAM_GaRequestedService = Class(name="GQAM_GaRequestedService")
MARTE_GQAM_GaExecHost = Class(name="MARTE_GQAM_GaExecHost")
GQAM_GaStep = Class(name="GQAM_GaStep")
GQAM_GaTimedObs = Class(name="GQAM_GaTimedObs")
MARTE_GQAM_GaStep = Class(name="MARTE_GQAM_GaStep")
GaScenario = Class(name="GaScenario")
IntegerInterval = Class(name="IntegerInterval")
MARTE_GQAM_GaRequestedService = Class(name="MARTE_GQAM_GaRequestedService")
GaStep = Class(name="GaStep")
GQAM_MARTE_Operation = Class(name="GQAM_MARTE_Operation")
MARTE_GQAM_GaTimedObs = Class(name="MARTE_GQAM_GaTimedObs")
NfpConstraint = Class(name="NfpConstraint")
GQAM_MARTE_TimeObservation = Class(name="GQAM_MARTE_TimeObservation")
MARTE_GQAM_GaAcqStep = Class(name="MARTE_GQAM_GaAcqStep")
MARTE_GQAM_GaRelStep = Class(name="MARTE_GQAM_GaRelStep")
MARTE_GQAM_GaLatencyObs = Class(name="MARTE_GQAM_GaLatencyObs")
GaTimedObs = Class(name="GaTimedObs")
MARTE_GQAM_GaCommStep = Class(name="MARTE_GQAM_GaCommStep")
MARTE_GQAM_GaWorkloadBehavior = Class(name="MARTE_GQAM_GaWorkloadBehavior")
MARTE_GQAM_GaAnalysisContext = Class(name="MARTE_GQAM_GaAnalysisContext")
CoreElements_Configuration = Class(name="CoreElements_Configuration")
Variables_ExpressionContext = Class(name="Variables_ExpressionContext")
GQAM_GaWorkloadBehavior = Class(name="GQAM_GaWorkloadBehavior")
GQAM_GaResourcesPlatform = Class(name="GQAM_GaResourcesPlatform")
MARTE_GQAM_GaResourcesPlatform = Class(name="MARTE_GQAM_GaResourcesPlatform")
MARTE_GQAM_GaCommHost = Class(name="MARTE_GQAM_GaCommHost")
MARTE_GQAM_GaCommChannel = Class(name="MARTE_GQAM_GaCommChannel")
SchedulableResource = Class(name="SchedulableResource")
MARTE_SAM_SaEndtoEndFlow = Class(name="MARTE_SAM_SaEndtoEndFlow")
SAM_MARTE_NamedElement = Class(name="SAM_MARTE_NamedElement")
MARTE_SAM_SaCommStep = Class(name="MARTE_SAM_SaCommStep")
GaCommStep = Class(name="GaCommStep")
GQAM_MARTE_Classifier = Class(name="GQAM_MARTE_Classifier")
MARTE_SAM_SaAnalysisContext = Class(name="MARTE_SAM_SaAnalysisContext")
GaAnalysisContext = Class(name="GaAnalysisContext")
SAM_SaSharedResource = Class(name="SAM_SaSharedResource")
SAM_MARTE_BehavioralFeature = Class(name="SAM_MARTE_BehavioralFeature")
MARTE_SAM_SaStep = Class(name="MARTE_SAM_SaStep")
MARTE_SAM_SaSchedObs = Class(name="MARTE_SAM_SaSchedObs")
MARTE_SAM_SaCommHost = Class(name="MARTE_SAM_SaCommHost")
GaCommHost = Class(name="GaCommHost")
MARTE_SAM_SaSharedResource = Class(name="MARTE_SAM_SaSharedResource")
MutualExclusionResource = Class(name="MutualExclusionResource")
MARTE_PAM_PaStep = Class(name="MARTE_PAM_PaStep")
MARTE_SAM_SaExecHost = Class(name="MARTE_SAM_SaExecHost")
GaExecHost = Class(name="GaExecHost")
MARTE_PAM_PaLogicalResource = Class(name="MARTE_PAM_PaLogicalResource")
MARTE_PAM_PaRunTInstance = Class(name="MARTE_PAM_PaRunTInstance")
MARTE_PAM_PaRequestedStep = Class(name="MARTE_PAM_PaRequestedStep")
PAM_PaStep = Class(name="PAM_PaStep")
MARTE_PAM_PaCommStep = Class(name="MARTE_PAM_PaCommStep")
GQAM_GaCommStep = Class(name="GQAM_GaCommStep")
MARTE_PAM_PaResPassStep = Class(name="MARTE_PAM_PaResPassStep")
PAM_MARTE_NamedElement = Class(name="PAM_MARTE_NamedElement")

# NFPs_MARTE_Property class attributes and methods

# MARTE_NFPs_Unit class attributes and methods
MARTE_NFPs_Unit_convFactor: Property = Property(name="convFactor", type=StringType)
MARTE_NFPs_Unit_offsetFactor: Property = Property(name="offsetFactor", type=StringType)
MARTE_NFPs_Unit.attributes={MARTE_NFPs_Unit_convFactor, MARTE_NFPs_Unit_offsetFactor}

# NFPs_Unit class attributes and methods

# MARTE_NFPs_Nfp class attributes and methods

# MARTE_CoreElements_ModeBehavior class attributes and methods

# CoreElements_MARTE_StateMachine class attributes and methods

# MARTE_CoreElements_Configuration class attributes and methods

# CoreElements_MARTE_StructuredClassifier class attributes and methods

# CoreElements_MARTE_Package class attributes and methods

# NFPs_MARTE_EnumerationLiteral class attributes and methods

# MARTE_NFPs_NfpConstraint class attributes and methods
MARTE_NFPs_NfpConstraint_kind: Property = Property(name="kind", type=StringType)
MARTE_NFPs_NfpConstraint.attributes={MARTE_NFPs_NfpConstraint_kind}

# NFPs_MARTE_Constraint class attributes and methods

# CoreElements_Mode class attributes and methods

# MARTE_NFPs_NfpType class attributes and methods

# TupleType class attributes and methods

# MARTE_NFPs_Dimension class attributes and methods
MARTE_NFPs_Dimension_symbol: Property = Property(name="symbol", type=StringType)
MARTE_NFPs_Dimension_baseExponent: Property = Property(name="baseExponent", type=IntegerType)
MARTE_NFPs_Dimension.attributes={MARTE_NFPs_Dimension_baseExponent, MARTE_NFPs_Dimension_symbol}

# NFPs_Dimension class attributes and methods

# NFPs_MARTE_Enumeration class attributes and methods

# MARTE_CoreElements_ModeTransition class attributes and methods

# CoreElements_MARTE_Transition class attributes and methods

# Alloc_MARTE_Element class attributes and methods

# Alloc_MARTE_Comment class attributes and methods

# MARTE_CoreElements_Mode class attributes and methods

# CoreElements_MARTE_State class attributes and methods

# MARTE_Alloc_Allocated class attributes and methods

# Alloc_MARTE_NamedElement class attributes and methods

# Alloc_Allocated class attributes and methods

# MARTE_Alloc_AllocateActivityGroup class attributes and methods

# Alloc_MARTE_ActivityPartition class attributes and methods

# MARTE_Alloc_NfpRefine class attributes and methods

# Alloc_MARTE_Dependency class attributes and methods

# NFPs_NfpConstraint class attributes and methods

# MARTE_Alloc_Assign class attributes and methods

# Time_MARTE_Operation class attributes and methods

# MARTE_Alloc_Allocate class attributes and methods
MARTE_Alloc_Allocate_kind: Property = Property(name="kind", type=StringType)
MARTE_Alloc_Allocate_nature: Property = Property(name="nature", type=StringType)
MARTE_Alloc_Allocate.attributes={MARTE_Alloc_Allocate_kind, MARTE_Alloc_Allocate_nature}

# Alloc_MARTE_Abstraction class attributes and methods

# MARTE_Time_TimedDomain class attributes and methods

# Time_MARTE_Namespace class attributes and methods

# MARTE_Time_Clock class attributes and methods
MARTE_Time_Clock_standard: Property = Property(name="standard", type=StringType)
MARTE_Time_Clock.attributes={MARTE_Time_Clock_standard}

# Time_MARTE_InstanceSpecification class attributes and methods

# Time_ClockType class attributes and methods

# Time_MARTE_Property class attributes and methods

# MARTE_Time_ClockType class attributes and methods
MARTE_Time_ClockType_isLogical: Property = Property(name="isLogical", type=StringType)
MARTE_Time_ClockType_nature: Property = Property(name="nature", type=StringType)
MARTE_Time_ClockType.attributes={MARTE_Time_ClockType_isLogical, MARTE_Time_ClockType_nature}

# Time_MARTE_Enumeration class attributes and methods

# Time_MARTE_TimeObservation class attributes and methods

# MARTE_Time_TimedDurationObservation class attributes and methods
MARTE_Time_TimedDurationObservation_obsKind: Property = Property(name="obsKind", type=StringType)
MARTE_Time_TimedDurationObservation.attributes={MARTE_Time_TimedDurationObservation_obsKind}

# Time_MARTE_DurationObservation class attributes and methods

# MARTE_Time_TimedEvent class attributes and methods
MARTE_Time_TimedEvent_repetition: Property = Property(name="repetition", type=StringType)
MARTE_Time_TimedEvent.attributes={MARTE_Time_TimedEvent_repetition}

# Time_MARTE_Class class attributes and methods

# MARTE_Time_TimedElement class attributes and methods

# Time_Clock class attributes and methods

# MARTE_Time_TimedValueSpecification class attributes and methods
MARTE_Time_TimedValueSpecification_interpretation: Property = Property(name="interpretation", type=StringType)
MARTE_Time_TimedValueSpecification.attributes={MARTE_Time_TimedValueSpecification_interpretation}

# TimedElement class attributes and methods

# Time_MARTE_ValueSpecification class attributes and methods

# MARTE_Time_TimedConstraint class attributes and methods
MARTE_Time_TimedConstraint_interpretation: Property = Property(name="interpretation", type=StringType)
MARTE_Time_TimedConstraint.attributes={MARTE_Time_TimedConstraint_interpretation}

# Time_TimedElement class attributes and methods

# MARTE_Time_ClockConstraint class attributes and methods
MARTE_Time_ClockConstraint_isCoincidenceBased: Property = Property(name="isCoincidenceBased", type=StringType)
MARTE_Time_ClockConstraint_isPrecedenceBased: Property = Property(name="isPrecedenceBased", type=BooleanType)
MARTE_Time_ClockConstraint_isChronometricBased: Property = Property(name="isChronometricBased", type=StringType)
MARTE_Time_ClockConstraint.attributes={MARTE_Time_ClockConstraint_isPrecedenceBased, MARTE_Time_ClockConstraint_isChronometricBased, MARTE_Time_ClockConstraint_isCoincidenceBased}

# MARTE_Time_TimedObservation class attributes and methods

# MARTE_Time_TimedInstantObservation class attributes and methods
MARTE_Time_TimedInstantObservation_obsKind: Property = Property(name="obsKind", type=StringType)
MARTE_Time_TimedInstantObservation.attributes={MARTE_Time_TimedInstantObservation_obsKind}

# TimedObservation class attributes and methods

# GRM_MARTE_Classifier class attributes and methods

# GRM_MARTE_Lifeline class attributes and methods

# GRM_MARTE_ConnectableElement class attributes and methods

# MARTE_GRM_StorageResource class attributes and methods

# Resource class attributes and methods

# Time_MARTE_TimeEvent class attributes and methods

# MARTE_Time_TimedProcessing class attributes and methods

# Time_MARTE_Action class attributes and methods

# Time_MARTE_Behavior class attributes and methods

# Time_MARTE_Message class attributes and methods

# Time_MARTE_Event class attributes and methods

# MARTE_GRM_Resource class attributes and methods
MARTE_GRM_Resource_isProtected: Property = Property(name="isProtected", type=StringType)
MARTE_GRM_Resource.attributes={MARTE_GRM_Resource_isProtected}

# NFP_Integer class attributes and methods

# GRM_MARTE_Property class attributes and methods

# GRM_MARTE_InstanceSpecification class attributes and methods

# MARTE_GRM_ComputingResource class attributes and methods

# ProcessingResource class attributes and methods

# MARTE_GRM_MutualExclusionResource class attributes and methods
MARTE_GRM_MutualExclusionResource_protectKind: Property = Property(name="protectKind", type=StringType)
MARTE_GRM_MutualExclusionResource_otherProtectProtocol: Property = Property(name="otherProtectProtocol", type=StringType)
MARTE_GRM_MutualExclusionResource.attributes={MARTE_GRM_MutualExclusionResource_otherProtectProtocol, MARTE_GRM_MutualExclusionResource_protectKind}

# MARTE_GRM_CommunicationEndPoint class attributes and methods

# MARTE_GRM_SynchronizationResource class attributes and methods

# MARTE_GRM_ConcurrencyResource class attributes and methods

# MARTE_GRM_Scheduler class attributes and methods
MARTE_GRM_Scheduler_isPreemptible: Property = Property(name="isPreemptible", type=StringType)
MARTE_GRM_Scheduler_schedPolicy: Property = Property(name="schedPolicy", type=StringType)
MARTE_GRM_Scheduler_otherSchedPolicy: Property = Property(name="otherSchedPolicy", type=StringType)
MARTE_GRM_Scheduler.attributes={MARTE_GRM_Scheduler_schedPolicy, MARTE_GRM_Scheduler_isPreemptible, MARTE_GRM_Scheduler_otherSchedPolicy}

# GRM_MARTE_OpaqueExpression class attributes and methods

# GRM_ProcessingResource class attributes and methods

# GRM_ComputingResource class attributes and methods

# GRM_MutualExclusionResource class attributes and methods

# GRM_SchedulableResource class attributes and methods

# MARTE_GRM_ProcessingResource class attributes and methods

# NFP_Real class attributes and methods

# GRM_Scheduler class attributes and methods

# MARTE_GRM_TimingResource class attributes and methods

# MARTE_GRM_ClockResource class attributes and methods

# TimingResource class attributes and methods

# MARTE_GRM_TimerResource class attributes and methods
MARTE_GRM_TimerResource_isPeriodic: Property = Property(name="isPeriodic", type=StringType)
MARTE_GRM_TimerResource.attributes={MARTE_GRM_TimerResource_isPeriodic}

# MARTE_GRM_SchedulableResource class attributes and methods

# SchedParameters class attributes and methods

# GRM_SecondaryScheduler class attributes and methods

# MARTE_GRM_SecondaryScheduler class attributes and methods

# Scheduler class attributes and methods

# MARTE_GRM_CommunicationMedia class attributes and methods
MARTE_GRM_CommunicationMedia_transmMode: Property = Property(name="transmMode", type=StringType)
MARTE_GRM_CommunicationMedia.attributes={MARTE_GRM_CommunicationMedia_transmMode}

# GRM_MARTE_Connector class attributes and methods

# NFP_Duration class attributes and methods

# NFP_DataTxRate class attributes and methods

# MARTE_GRM_DeviceResource class attributes and methods

# GRM_MARTE_NamedElement class attributes and methods

# GRM_ResourceUsage class attributes and methods

# MARTE_GRM_GrService class attributes and methods

# GRM_Resource class attributes and methods

# GRM_MARTE_ExecutionSpecification class attributes and methods

# GRM_MARTE_BehavioralFeature class attributes and methods

# GRM_MARTE_Behavior class attributes and methods

# GRM_MARTE_Collaboration class attributes and methods

# GRM_MARTE_CollaborationUse class attributes and methods

# MARTE_GRM_Release class attributes and methods

# GrService class attributes and methods

# MARTE_GRM_Acquire class attributes and methods
MARTE_GRM_Acquire_isBlocking: Property = Property(name="isBlocking", type=StringType)
MARTE_GRM_Acquire.attributes={MARTE_GRM_Acquire_isBlocking}

# MARTE_GRM_ResourceUsage class attributes and methods

# NFP_DataSize class attributes and methods

# NFP_Power class attributes and methods

# NFP_Energy class attributes and methods

# MARTE_RSM_Tiler class attributes and methods

# IntegerMatrix class attributes and methods

# MARTE_RSM_LinkTopology class attributes and methods

# RSM_MARTE_Connector class attributes and methods

# MARTE_RSM_DefaultLink class attributes and methods

# LinkTopology class attributes and methods

# MARTE_RSM_InterRepetition class attributes and methods
MARTE_RSM_InterRepetition_isModulo: Property = Property(name="isModulo", type=StringType)
MARTE_RSM_InterRepetition.attributes={MARTE_RSM_InterRepetition_isModulo}

# IntegerVector class attributes and methods

# MARTE_RSM_Distribute class attributes and methods

# Allocate class attributes and methods

# ShapeSpecification class attributes and methods

# TilerSpecification class attributes and methods

# MARTE_RSM_Reshape class attributes and methods

# DataTypes_MARTE_DataType class attributes and methods

# MARTE_DataTypes_IntervalType class attributes and methods

# MARTE_DataTypes_CollectionType class attributes and methods

# RSM_MARTE_ConnectorEnd class attributes and methods

# MARTE_RSM_Shaped class attributes and methods

# RSM_MARTE_MultiplicityElement class attributes and methods

# MARTE_Variables_Var class attributes and methods
MARTE_Variables_Var_dir: Property = Property(name="dir", type=StringType)
MARTE_Variables_Var.attributes={MARTE_Variables_Var_dir}

# Variables_MARTE_Property class attributes and methods

# MARTE_Variables_ExpressionContext class attributes and methods

# Variables_MARTE_NamedElement class attributes and methods

# MARTE_DataTypes_BoundedSubtype class attributes and methods
MARTE_DataTypes_BoundedSubtype_minValue: Property = Property(name="minValue", type=StringType)
MARTE_DataTypes_BoundedSubtype_maxValue: Property = Property(name="maxValue", type=StringType)
MARTE_DataTypes_BoundedSubtype_isMinOpen: Property = Property(name="isMinOpen", type=BooleanType)
MARTE_DataTypes_BoundedSubtype_isMaxOpen: Property = Property(name="isMaxOpen", type=BooleanType)
MARTE_DataTypes_BoundedSubtype.attributes={MARTE_DataTypes_BoundedSubtype_maxValue, MARTE_DataTypes_BoundedSubtype_minValue, MARTE_DataTypes_BoundedSubtype_isMaxOpen, MARTE_DataTypes_BoundedSubtype_isMinOpen}

# DataTypes_MARTE_Property class attributes and methods

# HLAM_MARTE_BehavioredClassifier class attributes and methods

# MARTE_DataTypes_ChoiceType class attributes and methods

# MARTE_DataTypes_TupleType class attributes and methods

# MARTE_HLAM_RtUnit class attributes and methods
MARTE_HLAM_RtUnit_queueSchedPolicy: Property = Property(name="queueSchedPolicy", type=StringType)
MARTE_HLAM_RtUnit_queueSize: Property = Property(name="queueSize", type=StringType)
MARTE_HLAM_RtUnit_isDynamic: Property = Property(name="isDynamic", type=StringType)
MARTE_HLAM_RtUnit_isMain: Property = Property(name="isMain", type=StringType)
MARTE_HLAM_RtUnit_srPoolSize: Property = Property(name="srPoolSize", type=StringType)
MARTE_HLAM_RtUnit_srPoolPolicy: Property = Property(name="srPoolPolicy", type=StringType)
MARTE_HLAM_RtUnit.attributes={MARTE_HLAM_RtUnit_queueSize, MARTE_HLAM_RtUnit_srPoolPolicy, MARTE_HLAM_RtUnit_isDynamic, MARTE_HLAM_RtUnit_queueSchedPolicy, MARTE_HLAM_RtUnit_srPoolSize, MARTE_HLAM_RtUnit_isMain}

# HLAM_MARTE_Behavior class attributes and methods

# HLAM_MARTE_Operation class attributes and methods

# MARTE_HLAM_RtSpecification class attributes and methods

# UtilityType class attributes and methods

# ArrivalPattern class attributes and methods

# Time_TimedInstantObservation class attributes and methods

# MARTE_HLAM_PpUnit class attributes and methods
MARTE_HLAM_PpUnit_concPolicy: Property = Property(name="concPolicy", type=StringType)
MARTE_HLAM_PpUnit.attributes={MARTE_HLAM_PpUnit_concPolicy}

# MARTE_HLAM_RtFeature class attributes and methods

# HLAM_MARTE_BehavioralFeature class attributes and methods

# HLAM_MARTE_Message class attributes and methods

# HLAM_MARTE_Signal class attributes and methods

# HLAM_MARTE_Port class attributes and methods

# HLAM_MARTE_InvocationAction class attributes and methods

# HLAM_RtSpecification class attributes and methods

# NFP_Percentage class attributes and methods

# HLAM_MARTE_Comment class attributes and methods

# NFP_DateTime class attributes and methods

# MARTE_HLAM_RtAction class attributes and methods
MARTE_HLAM_RtAction_isAtomic: Property = Property(name="isAtomic", type=StringType)
MARTE_HLAM_RtAction_synchKind: Property = Property(name="synchKind", type=StringType)
MARTE_HLAM_RtAction.attributes={MARTE_HLAM_RtAction_isAtomic, MARTE_HLAM_RtAction_synchKind}

# MARTE_HLAM_RtService class attributes and methods
MARTE_HLAM_RtService_concPolicy: Property = Property(name="concPolicy", type=StringType)
MARTE_HLAM_RtService_exeKind: Property = Property(name="exeKind", type=StringType)
MARTE_HLAM_RtService_isAtomic: Property = Property(name="isAtomic", type=StringType)
MARTE_HLAM_RtService_synchKind: Property = Property(name="synchKind", type=StringType)
MARTE_HLAM_RtService.attributes={MARTE_HLAM_RtService_concPolicy, MARTE_HLAM_RtService_isAtomic, MARTE_HLAM_RtService_exeKind, MARTE_HLAM_RtService_synchKind}

# HwComputing_HwISA class attributes and methods

# MARTE_HwComputing_PLD_Organization class attributes and methods
MARTE_HwComputing_PLD_Organization_class_: Property = Property(name="class_", type=StringType)
MARTE_HwComputing_PLD_Organization.attributes={MARTE_HwComputing_PLD_Organization_class_}

# NFP_Natural class attributes and methods

# MARTE_HwComputing_HwProcessor class attributes and methods

# HwComputingResource class attributes and methods

# HwMemory_HwRAM class attributes and methods

# HwComputing_HwBranchPredictor class attributes and methods

# HwMemory_HwCache class attributes and methods

# HwStorageManager_HwMMU class attributes and methods

# MARTE_HwComputing_HwComputingResource class attributes and methods

# HwGeneral_HwResource class attributes and methods

# NFP_FrequencyInterval class attributes and methods

# MARTE_HwComputing_HwISA class attributes and methods
MARTE_HwComputing_HwISA_type: Property = Property(name="type", type=StringType)
MARTE_HwComputing_HwISA.attributes={MARTE_HwComputing_HwISA_type}

# HwResource class attributes and methods

# NFP_String class attributes and methods

# MARTE_HwComputing_HwBranchPredictor class attributes and methods

# MARTE_HwComputing_HwASIC class attributes and methods

# MARTE_HwComputing_HwPLD class attributes and methods
MARTE_HwComputing_HwPLD_technology: Property = Property(name="technology", type=StringType)
MARTE_HwComputing_HwPLD.attributes={MARTE_HwComputing_HwPLD_technology}

# HwComputing_PLD_Organization class attributes and methods

# HwCommunication_HwArbiter class attributes and methods

# MARTE_HwCommunication_HwBus class attributes and methods

# HwMedia class attributes and methods

# HwComputing_HwComputingResource class attributes and methods

# MARTE_HwComputing_HwMCU class attributes and methods

# HwComputing_HwProcessor class attributes and methods

# HwDevice_HwPeripheral class attributes and methods

# HwRegister_HwRegister class attributes and methods

# HwPackage_HwPackage class attributes and methods

# HwIO_HwPin class attributes and methods

# HwCommunication_HwPort class attributes and methods

# MARTE_HwCommunication_HwCommunicationResource class attributes and methods

# MARTE_HwCommunication_HwArbiter class attributes and methods

# HwCommunicationResource class attributes and methods

# HwCommunication_HwMedia class attributes and methods

# MARTE_HwCommunication_HwMedia class attributes and methods

# GRM_CommunicationMedia class attributes and methods

# HwCommunication_HwCommunicationResource class attributes and methods

# MARTE_HwStorageManager_HwMMU class attributes and methods

# HwStorageManager class attributes and methods

# NFP_Boolean class attributes and methods

# MARTE_HwCommunication_HwBridge class attributes and methods

# MARTE_HwCommunication_HwEndPoint class attributes and methods

# GRM_CommunicationEndPoint class attributes and methods

# MARTE_HwCommunication_HwPort class attributes and methods

# HwEndPoint class attributes and methods

# MARTE_HwCommunication_HwConnection class attributes and methods

# HwProtocol_HwProtocol class attributes and methods

# MARTE_HwStorageManager_HwStorageManager class attributes and methods

# GRM_StorageResource class attributes and methods

# HwMemory_HwMemory class attributes and methods

# MARTE_HwStorageManager_HwDMA class attributes and methods

# HwStorageManager_HwStorageManager class attributes and methods

# MARTE_HwMemory_HwMemory class attributes and methods

# HwMemory_Timing class attributes and methods

# MARTE_HwMemory_Timing class attributes and methods

# MARTE_HwMemory_HwROM class attributes and methods
MARTE_HwMemory_HwROM_type: Property = Property(name="type", type=StringType)
MARTE_HwMemory_HwROM.attributes={MARTE_HwMemory_HwROM_type}

# MARTE_HwMemory_CacheStructure class attributes and methods

# MARTE_HwMemory_MemoryOrganization class attributes and methods

# MARTE_HwMemory_HwRAM class attributes and methods
MARTE_HwMemory_HwRAM_repl_Policy: Property = Property(name="repl_Policy", type=StringType)
MARTE_HwMemory_HwRAM_writePolicy: Property = Property(name="writePolicy", type=StringType)
MARTE_HwMemory_HwRAM.attributes={MARTE_HwMemory_HwRAM_writePolicy, MARTE_HwMemory_HwRAM_repl_Policy}

# HwMemory class attributes and methods

# HwMemory_MemoryOrganization class attributes and methods

# HwTiming_HwClock class attributes and methods

# MARTE_HwDevice_HwDevice class attributes and methods

# GRM_DeviceResource class attributes and methods

# HwDeviceFunction_HwDeviceFunction class attributes and methods

# MARTE_HwMemory_HwDrive class attributes and methods

# MARTE_HwMemory_HwCache class attributes and methods
MARTE_HwMemory_HwCache_type: Property = Property(name="type", type=StringType)
MARTE_HwMemory_HwCache_repl_Policy: Property = Property(name="repl_Policy", type=StringType)
MARTE_HwMemory_HwCache_writePolicy: Property = Property(name="writePolicy", type=StringType)
MARTE_HwMemory_HwCache.attributes={MARTE_HwMemory_HwCache_writePolicy, MARTE_HwMemory_HwCache_repl_Policy, MARTE_HwMemory_HwCache_type}

# HwMemory_CacheStructure class attributes and methods

# MARTE_HwTiming_HwTimingResource class attributes and methods

# GRM_TimingResource class attributes and methods

# MARTE_HwTiming_HwClock class attributes and methods

# HwTimingResource class attributes and methods

# MARTE_HwTiming_HwTimer class attributes and methods

# MARTE_HwGeneral_HwResourceService class attributes and methods

# MARTE_HwGeneral_HwResource class attributes and methods
MARTE_HwGeneral_HwResource_name: Property = Property(name="name", type=StringType)
MARTE_HwGeneral_HwResource.attributes={MARTE_HwGeneral_HwResource_name}

# MARTE_HwDevice_HwI_O class attributes and methods

# HwDevice class attributes and methods

# MARTE_HwDevice_HwSupport class attributes and methods

# MARTE_HwDevice_HWActuator class attributes and methods

# HwI_O class attributes and methods

# MARTE_HwDevice_HWSensor class attributes and methods

# MARTE_HwDevice_HwPeripheral class attributes and methods

# HwPeripheral_OperationImpl class attributes and methods

# HwPeripheral_PeripheralActivity class attributes and methods

# NFP_Area class attributes and methods

# NFP_NaturalInterval class attributes and methods

# HwGeneral_HwResourceService class attributes and methods

# HwCommunication_HwEndPoint class attributes and methods

# NFP_Frequency class attributes and methods

# HwGeneral_MARTE_Operation class attributes and methods

# HwGeneral_MARTE_Activity class attributes and methods

# MARTE_HwLayout_HwComponent class attributes and methods
MARTE_HwLayout_HwComponent_kind: Property = Property(name="kind", type=StringType)
MARTE_HwLayout_HwComponent.attributes={MARTE_HwLayout_HwComponent_kind}

# NFP_Length class attributes and methods

# Realnterval class attributes and methods

# NFP_Price class attributes and methods

# HwLayout_Env_Condition class attributes and methods

# HwLayout_HwComponent class attributes and methods

# MARTE_HwLayout_Env_Condition class attributes and methods
MARTE_HwLayout_Env_Condition_type: Property = Property(name="type", type=StringType)
MARTE_HwLayout_Env_Condition_status: Property = Property(name="status", type=StringType)
MARTE_HwLayout_Env_Condition.attributes={MARTE_HwLayout_Env_Condition_status, MARTE_HwLayout_Env_Condition_type}

# MARTE_HwPower_HwCoolingSupply class attributes and methods

# MARTE_HwPower_HwPowerSupply class attributes and methods

# HwComponent class attributes and methods

# HwPackage_HwPackagePin class attributes and methods

# HwIO_HwLine class attributes and methods

# MARTE_HwIO_HwLine class attributes and methods

# MARTE_HwPeripheral_OperationImpl class attributes and methods

# Operation class attributes and methods

# HwPeripheral_MARTE_Operation class attributes and methods

# MARTE_HwPeripheral_RegisterAction class attributes and methods

# Action class attributes and methods

# MARTE_HwPeripheral_WriteRegisterAction class attributes and methods

# RegisterAction class attributes and methods

# HwPeripheral_MARTE_InputPin class attributes and methods

# MARTE_HwPeripheral_ReadRegisterAction class attributes and methods

# HwPeripheral_MARTE_OutputPin class attributes and methods

# MARTE_HwPeripheral_PeripheralActivity class attributes and methods

# Activity class attributes and methods

# HwPeripheral_RegisterAction class attributes and methods

# MARTE_HwDeviceFunction_HwDeviceFunction class attributes and methods

# MARTE_HwIO_HwPin class attributes and methods

# MARTE_HwPackage_HwWire class attributes and methods

# MARTE_HwProtocol_HwProtocol class attributes and methods
MARTE_HwProtocol_HwProtocol_name: Property = Property(name="name", type=StringType)
MARTE_HwProtocol_HwProtocol.attributes={MARTE_HwProtocol_HwProtocol_name}

# HwProtocol_MARTE_Operation class attributes and methods

# MARTE_HwDiagram_HwBlockDiagram class attributes and methods
MARTE_HwDiagram_HwBlockDiagram_name: Property = Property(name="name", type=StringType)
MARTE_HwDiagram_HwBlockDiagram.attributes={MARTE_HwDiagram_HwBlockDiagram_name}

# MARTE_HwRegister_HwRegister class attributes and methods
MARTE_HwRegister_HwRegister_address: Property = Property(name="address", type=StringType)
MARTE_HwRegister_HwRegister.attributes={MARTE_HwRegister_HwRegister_address}

# MARTE_HwDatasheet_HwDatasheet class attributes and methods
MARTE_HwDatasheet_HwDatasheet_revision: Property = Property(name="revision", type=StringType)
MARTE_HwDatasheet_HwDatasheet_name: Property = Property(name="name", type=StringType)
MARTE_HwDatasheet_HwDatasheet.attributes={MARTE_HwDatasheet_HwDatasheet_name, MARTE_HwDatasheet_HwDatasheet_revision}

# MARTE_HwPackage_HwPackage class attributes and methods
MARTE_HwPackage_HwPackage_pinNum: Property = Property(name="pinNum", type=IntegerType)
MARTE_HwPackage_HwPackage_packageType: Property = Property(name="packageType", type=StringType)
MARTE_HwPackage_HwPackage_name: Property = Property(name="name", type=StringType)
MARTE_HwPackage_HwPackage.attributes={MARTE_HwPackage_HwPackage_packageType, MARTE_HwPackage_HwPackage_pinNum, MARTE_HwPackage_HwPackage_name}

# MARTE_HwPackage_HwPackagePin class attributes and methods
MARTE_HwPackage_HwPackagePin_altNames: Property = Property(name="altNames", type=StringType)
MARTE_HwPackage_HwPackagePin_pinNo: Property = Property(name="pinNo", type=StringType)
MARTE_HwPackage_HwPackagePin.attributes={MARTE_HwPackage_HwPackagePin_pinNo, MARTE_HwPackage_HwPackagePin_altNames}

# HwPackage_HwWire class attributes and methods

# MARTE_HwDiagram_HwHRMDiagram class attributes and methods
MARTE_HwDiagram_HwHRMDiagram_name: Property = Property(name="name", type=StringType)
MARTE_HwDiagram_HwHRMDiagram.attributes={MARTE_HwDiagram_HwHRMDiagram_name}

# HwCommunication_HwConnection class attributes and methods

# MARTE_HwDiagram_HwCircuitDiagram class attributes and methods
MARTE_HwDiagram_HwCircuitDiagram_name: Property = Property(name="name", type=StringType)
MARTE_HwDiagram_HwCircuitDiagram.attributes={MARTE_HwDiagram_HwCircuitDiagram_name}

# MARTE_SW_ResourceCore_SwAccessService class attributes and methods
MARTE_SW_ResourceCore_SwAccessService_isModifier: Property = Property(name="isModifier", type=StringType)
MARTE_SW_ResourceCore_SwAccessService.attributes={MARTE_SW_ResourceCore_SwAccessService_isModifier}

# HwDiagram_MARTE_DataType class attributes and methods

# SW_ResourceCore_MARTE_Property class attributes and methods

# MARTE_HwDiagram_SRMDiagram class attributes and methods

# SW_Brokering_DeviceBroker class attributes and methods

# MARTE_SW_Concurrency_EntryPoint class attributes and methods
MARTE_SW_Concurrency_EntryPoint_isReentrant: Property = Property(name="isReentrant", type=StringType)
MARTE_SW_Concurrency_EntryPoint.attributes={MARTE_SW_Concurrency_EntryPoint_isReentrant}

# MARTE_SW_ResourceCore_SwResource class attributes and methods

# SW_Concurrency_MARTE_BehavioralFeature class attributes and methods

# SW_ResourceCore_MARTE_TypedElement class attributes and methods

# SW_ResourceCore_MARTE_BehavioralFeature class attributes and methods

# MARTE_SW_Concurrency_SwConcurrentResource class attributes and methods
MARTE_SW_Concurrency_SwConcurrentResource_activationCapacity: Property = Property(name="activationCapacity", type=StringType)
MARTE_SW_Concurrency_SwConcurrentResource.attributes={MARTE_SW_Concurrency_SwConcurrentResource_activationCapacity}

# SwResource class attributes and methods

# SW_Concurrency_MARTE_Element class attributes and methods

# SW_Concurrency_MARTE_TypedElement class attributes and methods

# SwConcurrentResource class attributes and methods

# MARTE_SW_Concurrency_SwSchedulableResource class attributes and methods
MARTE_SW_Concurrency_SwSchedulableResource_isStaticSchedulingFeature: Property = Property(name="isStaticSchedulingFeature", type=StringType)
MARTE_SW_Concurrency_SwSchedulableResource_isPreemptable: Property = Property(name="isPreemptable", type=StringType)
MARTE_SW_Concurrency_SwSchedulableResource.attributes={MARTE_SW_Concurrency_SwSchedulableResource_isStaticSchedulingFeature, MARTE_SW_Concurrency_SwSchedulableResource_isPreemptable}

# SW_Concurrency_SwConcurrentResource class attributes and methods

# SW_Concurrency_MARTE_NamedElement class attributes and methods

# MARTE_SW_Concurrency_InterruptResource class attributes and methods
MARTE_SW_Concurrency_InterruptResource_kind: Property = Property(name="kind", type=StringType)
MARTE_SW_Concurrency_InterruptResource_isMaskable: Property = Property(name="isMaskable", type=StringType)
MARTE_SW_Concurrency_InterruptResource.attributes={MARTE_SW_Concurrency_InterruptResource_isMaskable, MARTE_SW_Concurrency_InterruptResource_kind}

# MARTE_SW_Concurrency_SwTimerResource class attributes and methods

# TimerResource class attributes and methods

# MARTE_SW_Concurrency_MemoryPartition class attributes and methods

# SW_Concurrency_MARTE_Namespace class attributes and methods

# MARTE_SW_Concurrency_Alarm class attributes and methods
MARTE_SW_Concurrency_Alarm_isWatchdog: Property = Property(name="isWatchdog", type=StringType)
MARTE_SW_Concurrency_Alarm.attributes={MARTE_SW_Concurrency_Alarm_isWatchdog}

# InterruptResource class attributes and methods

# SW_Brokering_MARTE_TypedElement class attributes and methods

# SW_Brokering_MARTE_BehavioralFeature class attributes and methods

# SW_Brokering_MARTE_Operation class attributes and methods

# SW_Brokering_MARTE_Activity class attributes and methods

# MARTE_SW_Brokering_MemoryBroker class attributes and methods
MARTE_SW_Brokering_MemoryBroker_accessPolicy: Property = Property(name="accessPolicy", type=StringType)
MARTE_SW_Brokering_MemoryBroker.attributes={MARTE_SW_Brokering_MemoryBroker_accessPolicy}

# MARTE_SW_Brokering_DeviceBroker class attributes and methods
MARTE_SW_Brokering_DeviceBroker_accessPolicy: Property = Property(name="accessPolicy", type=StringType)
MARTE_SW_Brokering_DeviceBroker_isBuffered: Property = Property(name="isBuffered", type=StringType)
MARTE_SW_Brokering_DeviceBroker_name: Property = Property(name="name", type=StringType)
MARTE_SW_Brokering_DeviceBroker.attributes={MARTE_SW_Brokering_DeviceBroker_name, MARTE_SW_Brokering_DeviceBroker_accessPolicy, MARTE_SW_Brokering_DeviceBroker_isBuffered}

# SW_Interaction_MARTE_TypedElement class attributes and methods

# MARTE_SW_Interaction_SwCommunicationResource class attributes and methods

# SW_Interaction_SwInteractionResource class attributes and methods

# MARTE_SW_Interaction_SwSynchronizationResource class attributes and methods

# GRM_SynchronizationResource class attributes and methods

# MARTE_SW_Interaction_SharedDataComResource class attributes and methods

# SwCommunicationResource class attributes and methods

# SW_Interaction_MARTE_BehavioralFeature class attributes and methods

# MARTE_SW_Interaction_MessageComResource class attributes and methods
MARTE_SW_Interaction_MessageComResource_isFixedMessageSize: Property = Property(name="isFixedMessageSize", type=StringType)
MARTE_SW_Interaction_MessageComResource_mechanism: Property = Property(name="mechanism", type=StringType)
MARTE_SW_Interaction_MessageComResource_messageQueuePolicy: Property = Property(name="messageQueuePolicy", type=StringType)
MARTE_SW_Interaction_MessageComResource.attributes={MARTE_SW_Interaction_MessageComResource_messageQueuePolicy, MARTE_SW_Interaction_MessageComResource_isFixedMessageSize, MARTE_SW_Interaction_MessageComResource_mechanism}

# MARTE_SW_Interaction_SwInteractionResource class attributes and methods
MARTE_SW_Interaction_SwInteractionResource_waitingQueueCapacity: Property = Property(name="waitingQueueCapacity", type=StringType)
MARTE_SW_Interaction_SwInteractionResource_isIntraMemoryPartitionInteraction: Property = Property(name="isIntraMemoryPartitionInteraction", type=BooleanType)
MARTE_SW_Interaction_SwInteractionResource_waitingQueuePolicy: Property = Property(name="waitingQueuePolicy", type=StringType)
MARTE_SW_Interaction_SwInteractionResource.attributes={MARTE_SW_Interaction_SwInteractionResource_waitingQueuePolicy, MARTE_SW_Interaction_SwInteractionResource_isIntraMemoryPartitionInteraction, MARTE_SW_Interaction_SwInteractionResource_waitingQueueCapacity}

# MARTE_SW_Interaction_SwMutualExclusionResource class attributes and methods
MARTE_SW_Interaction_SwMutualExclusionResource_mechanism: Property = Property(name="mechanism", type=StringType)
MARTE_SW_Interaction_SwMutualExclusionResource_concurrentAccessProtocol: Property = Property(name="concurrentAccessProtocol", type=StringType)
MARTE_SW_Interaction_SwMutualExclusionResource.attributes={MARTE_SW_Interaction_SwMutualExclusionResource_mechanism, MARTE_SW_Interaction_SwMutualExclusionResource_concurrentAccessProtocol}

# SW_Interaction_SwSynchronizationResource class attributes and methods

# MARTE_SW_Interaction_NotificationResource class attributes and methods
MARTE_SW_Interaction_NotificationResource_occurence: Property = Property(name="occurence", type=StringType)
MARTE_SW_Interaction_NotificationResource_mechanism: Property = Property(name="mechanism", type=StringType)
MARTE_SW_Interaction_NotificationResource.attributes={MARTE_SW_Interaction_NotificationResource_mechanism, MARTE_SW_Interaction_NotificationResource_occurence}

# SwSynchronizationResource class attributes and methods

# MARTE_GCM_FlowPort class attributes and methods
MARTE_GCM_FlowPort_isAtomic: Property = Property(name="isAtomic", type=StringType)
MARTE_GCM_FlowPort_isConjugated: Property = Property(name="isConjugated", type=StringType)
MARTE_GCM_FlowPort_direction: Property = Property(name="direction", type=StringType)
MARTE_GCM_FlowPort.attributes={MARTE_GCM_FlowPort_isConjugated, MARTE_GCM_FlowPort_direction, MARTE_GCM_FlowPort_isAtomic}

# GCM_MARTE_Port class attributes and methods

# MARTE_GCM_ClientServerPort class attributes and methods
MARTE_GCM_ClientServerPort_specificationKind: Property = Property(name="specificationKind", type=StringType)
MARTE_GCM_ClientServerPort_isConjugated: Property = Property(name="isConjugated", type=StringType)
MARTE_GCM_ClientServerPort_kind: Property = Property(name="kind", type=StringType)
MARTE_GCM_ClientServerPort.attributes={MARTE_GCM_ClientServerPort_specificationKind, MARTE_GCM_ClientServerPort_kind, MARTE_GCM_ClientServerPort_isConjugated}

# GCM_MARTE_Interface class attributes and methods

# GCM_ClientServerSpecification class attributes and methods

# MARTE_GCM_FlowProperty class attributes and methods
MARTE_GCM_FlowProperty_direction: Property = Property(name="direction", type=StringType)
MARTE_GCM_FlowProperty.attributes={MARTE_GCM_FlowProperty_direction}

# GCM_MARTE_Property class attributes and methods

# MARTE_GCM_ClientServerFeature class attributes and methods
MARTE_GCM_ClientServerFeature_kind: Property = Property(name="kind", type=StringType)
MARTE_GCM_ClientServerFeature.attributes={MARTE_GCM_ClientServerFeature_kind}

# GCM_MARTE_BehavioralFeature class attributes and methods

# MARTE_GCM_GCMTrigger class attributes and methods

# GCM_MARTE_Trigger class attributes and methods

# GCM_MARTE_Feature class attributes and methods

# MARTE_GCM_GCMInvocationAction class attributes and methods

# GCM_MARTE_InvocationAction class attributes and methods

# MARTE_GCM_DataEvent class attributes and methods

# GCM_MARTE_AnyReceiveEvent class attributes and methods

# GCM_MARTE_Classifier class attributes and methods

# MARTE_GCM_DataPool class attributes and methods
MARTE_GCM_DataPool_ordering: Property = Property(name="ordering", type=StringType)
MARTE_GCM_DataPool.attributes={MARTE_GCM_DataPool_ordering}

# MARTE_GCM_ClientServerSpecification class attributes and methods

# MARTE_GCM_FlowSpecification class attributes and methods

# GQAM_MARTE_Behavior class attributes and methods

# MARTE_GQAM_GaEventTrace class attributes and methods
MARTE_GQAM_GaEventTrace_content: Property = Property(name="content", type=StringType)
MARTE_GQAM_GaEventTrace_format: Property = Property(name="format", type=StringType)
MARTE_GQAM_GaEventTrace_location: Property = Property(name="location", type=StringType)
MARTE_GQAM_GaEventTrace.attributes={MARTE_GQAM_GaEventTrace_content, MARTE_GQAM_GaEventTrace_format, MARTE_GQAM_GaEventTrace_location}

# GQAM_MARTE_NamedElement class attributes and methods

# MARTE_GQAM_GaWorkloadEvent class attributes and methods

# GQAM_GaWorkloadGenerator class attributes and methods

# GQAM_GaEventTrace class attributes and methods

# GQAM_GaScenario class attributes and methods

# GQAM_MARTE_TimeEvent class attributes and methods

# GCM_MARTE_Behavior class attributes and methods

# MARTE_GQAM_GaWorkloadGenerator class attributes and methods

# MARTE_GQAM_GaScenario class attributes and methods

# Time_TimedProcessing class attributes and methods

# GQAM_GaWorkloadEvent class attributes and methods

# GQAM_GaExecHost class attributes and methods

# GQAM_GaRequestedService class attributes and methods

# MARTE_GQAM_GaExecHost class attributes and methods

# GQAM_GaStep class attributes and methods

# GQAM_GaTimedObs class attributes and methods

# MARTE_GQAM_GaStep class attributes and methods

# GaScenario class attributes and methods

# IntegerInterval class attributes and methods

# MARTE_GQAM_GaRequestedService class attributes and methods

# GaStep class attributes and methods

# GQAM_MARTE_Operation class attributes and methods

# MARTE_GQAM_GaTimedObs class attributes and methods
MARTE_GQAM_GaTimedObs_laxity: Property = Property(name="laxity", type=StringType)
MARTE_GQAM_GaTimedObs.attributes={MARTE_GQAM_GaTimedObs_laxity}

# NfpConstraint class attributes and methods

# GQAM_MARTE_TimeObservation class attributes and methods

# MARTE_GQAM_GaAcqStep class attributes and methods

# MARTE_GQAM_GaRelStep class attributes and methods

# MARTE_GQAM_GaLatencyObs class attributes and methods

# GaTimedObs class attributes and methods

# MARTE_GQAM_GaCommStep class attributes and methods

# MARTE_GQAM_GaWorkloadBehavior class attributes and methods

# MARTE_GQAM_GaAnalysisContext class attributes and methods

# CoreElements_Configuration class attributes and methods

# Variables_ExpressionContext class attributes and methods

# GQAM_GaWorkloadBehavior class attributes and methods

# GQAM_GaResourcesPlatform class attributes and methods

# MARTE_GQAM_GaResourcesPlatform class attributes and methods

# MARTE_GQAM_GaCommHost class attributes and methods

# MARTE_GQAM_GaCommChannel class attributes and methods

# SchedulableResource class attributes and methods

# MARTE_SAM_SaEndtoEndFlow class attributes and methods

# SAM_MARTE_NamedElement class attributes and methods

# MARTE_SAM_SaCommStep class attributes and methods

# GaCommStep class attributes and methods

# GQAM_MARTE_Classifier class attributes and methods

# MARTE_SAM_SaAnalysisContext class attributes and methods
MARTE_SAM_SaAnalysisContext_optCriterion: Property = Property(name="optCriterion", type=StringType)
MARTE_SAM_SaAnalysisContext.attributes={MARTE_SAM_SaAnalysisContext_optCriterion}

# GaAnalysisContext class attributes and methods

# SAM_SaSharedResource class attributes and methods

# SAM_MARTE_BehavioralFeature class attributes and methods

# MARTE_SAM_SaStep class attributes and methods

# MARTE_SAM_SaSchedObs class attributes and methods

# MARTE_SAM_SaCommHost class attributes and methods

# GaCommHost class attributes and methods

# MARTE_SAM_SaSharedResource class attributes and methods

# MutualExclusionResource class attributes and methods

# MARTE_PAM_PaStep class attributes and methods
MARTE_PAM_PaStep_extOpDemand: Property = Property(name="extOpDemand", type=StringType)
MARTE_PAM_PaStep.attributes={MARTE_PAM_PaStep_extOpDemand}

# MARTE_SAM_SaExecHost class attributes and methods

# GaExecHost class attributes and methods

# MARTE_PAM_PaLogicalResource class attributes and methods

# MARTE_PAM_PaRunTInstance class attributes and methods
MARTE_PAM_PaRunTInstance_unbddPool: Property = Property(name="unbddPool", type=StringType)
MARTE_PAM_PaRunTInstance.attributes={MARTE_PAM_PaRunTInstance_unbddPool}

# MARTE_PAM_PaRequestedStep class attributes and methods

# PAM_PaStep class attributes and methods

# MARTE_PAM_PaCommStep class attributes and methods

# GQAM_GaCommStep class attributes and methods

# MARTE_PAM_PaResPassStep class attributes and methods

# PAM_MARTE_NamedElement class attributes and methods

# Relationships
base_Property0: BinaryAssociation = BinaryAssociation(
    name="base_Property0",
    ends={
        Property(name="NFPs_MARTE_Property", type=MARTE_NFPs_Nfp, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_NFPs_Nfp", type=NFPs_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_Transition18: BinaryAssociation = BinaryAssociation(
    name="base_Transition18",
    ends={
        Property(name="CoreElements_MARTE_Transition", type=MARTE_CoreElements_ModeTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_CoreElements_ModeTransition", type=CoreElements_MARTE_Transition, multiplicity=Multiplicity(1, 1))
    }
)
base_StateMachine19: BinaryAssociation = BinaryAssociation(
    name="base_StateMachine19",
    ends={
        Property(name="CoreElements_MARTE_StateMachine", type=MARTE_CoreElements_ModeBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_CoreElements_ModeBehavior", type=CoreElements_MARTE_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
base_StructuredClassifier20: BinaryAssociation = BinaryAssociation(
    name="base_StructuredClassifier20",
    ends={
        Property(name="CoreElements_MARTE_StructuredClassifier", type=MARTE_CoreElements_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_CoreElements_Configuration", type=CoreElements_MARTE_StructuredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Package21: BinaryAssociation = BinaryAssociation(
    name="base_Package21",
    ends={
        Property(name="CoreElements_MARTE_Package", type=MARTE_CoreElements_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_CoreElements_Configuration22", type=CoreElements_MARTE_Package, multiplicity=Multiplicity(1, 1))
    }
)
baseUnit1: BinaryAssociation = BinaryAssociation(
    name="baseUnit1",
    ends={
        Property(name="NFPs_Unit", type=MARTE_NFPs_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_NFPs_Unit", type=NFPs_Unit, multiplicity=Multiplicity(0, 1))
    }
)
base_EnumerationLiteral2: BinaryAssociation = BinaryAssociation(
    name="base_EnumerationLiteral2",
    ends={
        Property(name="NFPs_MARTE_EnumerationLiteral", type=MARTE_NFPs_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_NFPs_Unit3", type=NFPs_MARTE_EnumerationLiteral, multiplicity=Multiplicity(1, 1))
    }
)
base_Constraint4: BinaryAssociation = BinaryAssociation(
    name="base_Constraint4",
    ends={
        Property(name="NFPs_MARTE_Constraint", type=MARTE_NFPs_NfpConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_NFPs_NfpConstraint", type=NFPs_MARTE_Constraint, multiplicity=Multiplicity(1, 1))
    }
)
mode5: BinaryAssociation = BinaryAssociation(
    name="mode5",
    ends={
        Property(name="CoreElements_Mode", type=MARTE_NFPs_NfpConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_NFPs_NfpConstraint6", type=CoreElements_Mode, multiplicity=Multiplicity(0, 9999))
    }
)
valueAttrib7: BinaryAssociation = BinaryAssociation(
    name="valueAttrib7",
    ends={
        Property(name="NFPs_MARTE_Property8", type=MARTE_NFPs_NfpType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_NFPs_NfpType", type=NFPs_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
unitAttrib9: BinaryAssociation = BinaryAssociation(
    name="unitAttrib9",
    ends={
        Property(name="NFPs_MARTE_Property11", type=MARTE_NFPs_NfpType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_NFPs_NfpType10", type=NFPs_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
exprAttrib12: BinaryAssociation = BinaryAssociation(
    name="exprAttrib12",
    ends={
        Property(name="NFPs_MARTE_Property14", type=MARTE_NFPs_NfpType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_NFPs_NfpType13", type=NFPs_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
baseDimension15: BinaryAssociation = BinaryAssociation(
    name="baseDimension15",
    ends={
        Property(name="NFPs_Dimension", type=MARTE_NFPs_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_NFPs_Dimension", type=NFPs_Dimension, multiplicity=Multiplicity(0, 9999))
    }
)
base_Enumeration16: BinaryAssociation = BinaryAssociation(
    name="base_Enumeration16",
    ends={
        Property(name="NFPs_MARTE_Enumeration", type=MARTE_NFPs_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_NFPs_Dimension17", type=NFPs_MARTE_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
from_39: BinaryAssociation = BinaryAssociation(
    name="from_39",
    ends={
        Property(name="Alloc_MARTE_Element", type=MARTE_Alloc_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_Assign40", type=Alloc_MARTE_Element, multiplicity=Multiplicity(1, 9999))
    }
)
to41: BinaryAssociation = BinaryAssociation(
    name="to41",
    ends={
        Property(name="Alloc_MARTE_Element43", type=MARTE_Alloc_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_Assign42", type=Alloc_MARTE_Element, multiplicity=Multiplicity(1, 9999))
    }
)
base_Comment44: BinaryAssociation = BinaryAssociation(
    name="base_Comment44",
    ends={
        Property(name="Alloc_MARTE_Comment", type=MARTE_Alloc_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_Assign45", type=Alloc_MARTE_Comment, multiplicity=Multiplicity(1, 1))
    }
)
mode23: BinaryAssociation = BinaryAssociation(
    name="mode23",
    ends={
        Property(name="CoreElements_Mode25", type=MARTE_CoreElements_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_CoreElements_Configuration24", type=CoreElements_Mode, multiplicity=Multiplicity(0, 9999))
    }
)
base_State26: BinaryAssociation = BinaryAssociation(
    name="base_State26",
    ends={
        Property(name="CoreElements_MARTE_State", type=MARTE_CoreElements_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_CoreElements_Mode", type=CoreElements_MARTE_State, multiplicity=Multiplicity(1, 1))
    }
)
base_NamedElement27: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement27",
    ends={
        Property(name="Alloc_MARTE_NamedElement", type=MARTE_Alloc_Allocated, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_Allocated", type=Alloc_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
allocatedTo28: BinaryAssociation = BinaryAssociation(
    name="allocatedTo28",
    ends={
        Property(name="Alloc_Allocated", type=MARTE_Alloc_Allocated, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_Allocated29", type=Alloc_Allocated, multiplicity=Multiplicity(0, 9999))
    }
)
allocatedFrom30: BinaryAssociation = BinaryAssociation(
    name="allocatedFrom30",
    ends={
        Property(name="Alloc_Allocated32", type=MARTE_Alloc_Allocated, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_Allocated31", type=Alloc_Allocated, multiplicity=Multiplicity(0, 9999))
    }
)
base_ActivityPartition33: BinaryAssociation = BinaryAssociation(
    name="base_ActivityPartition33",
    ends={
        Property(name="Alloc_MARTE_ActivityPartition", type=MARTE_Alloc_AllocateActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_AllocateActivityGroup", type=Alloc_MARTE_ActivityPartition, multiplicity=Multiplicity(1, 1))
    }
)
base_Dependency34: BinaryAssociation = BinaryAssociation(
    name="base_Dependency34",
    ends={
        Property(name="Alloc_MARTE_Dependency", type=MARTE_Alloc_NfpRefine, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_NfpRefine", type=Alloc_MARTE_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
constraint35: BinaryAssociation = BinaryAssociation(
    name="constraint35",
    ends={
        Property(name="NFPs_NfpConstraint", type=MARTE_Alloc_NfpRefine, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_NfpRefine36", type=NFPs_NfpConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
impliedConstraint37: BinaryAssociation = BinaryAssociation(
    name="impliedConstraint37",
    ends={
        Property(name="NFPs_NfpConstraint38", type=MARTE_Alloc_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_Assign", type=NFPs_NfpConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
unitType59: BinaryAssociation = BinaryAssociation(
    name="unitType59",
    ends={
        Property(name="Time_MARTE_Enumeration", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType", type=Time_MARTE_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
resolAttr60: BinaryAssociation = BinaryAssociation(
    name="resolAttr60",
    ends={
        Property(name="Time_MARTE_Property62", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType61", type=Time_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
maxValAttr63: BinaryAssociation = BinaryAssociation(
    name="maxValAttr63",
    ends={
        Property(name="Time_MARTE_Property65", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType64", type=Time_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
offsetAttr66: BinaryAssociation = BinaryAssociation(
    name="offsetAttr66",
    ends={
        Property(name="Time_MARTE_Property68", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType67", type=Time_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
base_Abstraction46: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction46",
    ends={
        Property(name="Alloc_MARTE_Abstraction", type=MARTE_Alloc_Allocate, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_Allocate", type=Alloc_MARTE_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
impliedConstraint47: BinaryAssociation = BinaryAssociation(
    name="impliedConstraint47",
    ends={
        Property(name="NFPs_NfpConstraint49", type=MARTE_Alloc_Allocate, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_Allocate48", type=NFPs_NfpConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
base_Namespace50: BinaryAssociation = BinaryAssociation(
    name="base_Namespace50",
    ends={
        Property(name="Time_MARTE_Namespace", type=MARTE_Time_TimedDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedDomain", type=Time_MARTE_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
base_InstanceSpecification51: BinaryAssociation = BinaryAssociation(
    name="base_InstanceSpecification51",
    ends={
        Property(name="Time_MARTE_InstanceSpecification", type=MARTE_Time_Clock, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_Clock", type=Time_MARTE_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="Time_ClockType", type=MARTE_Time_Clock, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_Clock53", type=Time_ClockType, multiplicity=Multiplicity(1, 1))
    }
)
unit54: BinaryAssociation = BinaryAssociation(
    name="unit54",
    ends={
        Property(name="NFPs_Unit56", type=MARTE_Time_Clock, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_Clock55", type=NFPs_Unit, multiplicity=Multiplicity(0, 1))
    }
)
base_Property57: BinaryAssociation = BinaryAssociation(
    name="base_Property57",
    ends={
        Property(name="Time_MARTE_Property", type=MARTE_Time_Clock, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_Clock58", type=Time_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_TimeObservation81: BinaryAssociation = BinaryAssociation(
    name="base_TimeObservation81",
    ends={
        Property(name="Time_MARTE_TimeObservation", type=MARTE_Time_TimedInstantObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedInstantObservation", type=Time_MARTE_TimeObservation, multiplicity=Multiplicity(1, 1))
    }
)
base_DurationObservation82: BinaryAssociation = BinaryAssociation(
    name="base_DurationObservation82",
    ends={
        Property(name="Time_MARTE_DurationObservation", type=MARTE_Time_TimedDurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedDurationObservation", type=Time_MARTE_DurationObservation, multiplicity=Multiplicity(1, 1))
    }
)
getTime69: BinaryAssociation = BinaryAssociation(
    name="getTime69",
    ends={
        Property(name="Time_MARTE_Operation", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType70", type=Time_MARTE_Operation, multiplicity=Multiplicity(0, 1))
    }
)
setTime71: BinaryAssociation = BinaryAssociation(
    name="setTime71",
    ends={
        Property(name="Time_MARTE_Operation73", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType72", type=Time_MARTE_Operation, multiplicity=Multiplicity(0, 1))
    }
)
indexToValue74: BinaryAssociation = BinaryAssociation(
    name="indexToValue74",
    ends={
        Property(name="Time_MARTE_Operation76", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType75", type=Time_MARTE_Operation, multiplicity=Multiplicity(0, 1))
    }
)
base_Class77: BinaryAssociation = BinaryAssociation(
    name="base_Class77",
    ends={
        Property(name="Time_MARTE_Class", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType78", type=Time_MARTE_Class, multiplicity=Multiplicity(1, 1))
    }
)
on79: BinaryAssociation = BinaryAssociation(
    name="on79",
    ends={
        Property(name="Time_Clock", type=MARTE_Time_TimedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedElement", type=Time_Clock, multiplicity=Multiplicity(1, 9999))
    }
)
base_ValueSpecification80: BinaryAssociation = BinaryAssociation(
    name="base_ValueSpecification80",
    ends={
        Property(name="Time_MARTE_ValueSpecification", type=MARTE_Time_TimedValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedValueSpecification", type=Time_MARTE_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier105: BinaryAssociation = BinaryAssociation(
    name="base_Classifier105",
    ends={
        Property(name="GRM_MARTE_Classifier", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource106", type=GRM_MARTE_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
base_Lifeline107: BinaryAssociation = BinaryAssociation(
    name="base_Lifeline107",
    ends={
        Property(name="GRM_MARTE_Lifeline", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource108", type=GRM_MARTE_Lifeline, multiplicity=Multiplicity(0, 1))
    }
)
base_ConnectableElement109: BinaryAssociation = BinaryAssociation(
    name="base_ConnectableElement109",
    ends={
        Property(name="GRM_MARTE_ConnectableElement", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource110", type=GRM_MARTE_ConnectableElement, multiplicity=Multiplicity(0, 1))
    }
)
base_TimeEvent83: BinaryAssociation = BinaryAssociation(
    name="base_TimeEvent83",
    ends={
        Property(name="Time_MARTE_TimeEvent", type=MARTE_Time_TimedEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedEvent", type=Time_MARTE_TimeEvent, multiplicity=Multiplicity(1, 1))
    }
)
every84: BinaryAssociation = BinaryAssociation(
    name="every84",
    ends={
        Property(name="Time_MARTE_ValueSpecification86", type=MARTE_Time_TimedEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedEvent85", type=Time_MARTE_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_Action87: BinaryAssociation = BinaryAssociation(
    name="base_Action87",
    ends={
        Property(name="Time_MARTE_Action", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing", type=Time_MARTE_Action, multiplicity=Multiplicity(1, 1))
    }
)
base_Behavior88: BinaryAssociation = BinaryAssociation(
    name="base_Behavior88",
    ends={
        Property(name="Time_MARTE_Behavior", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing89", type=Time_MARTE_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Message90: BinaryAssociation = BinaryAssociation(
    name="base_Message90",
    ends={
        Property(name="Time_MARTE_Message", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing91", type=Time_MARTE_Message, multiplicity=Multiplicity(1, 1))
    }
)
duration92: BinaryAssociation = BinaryAssociation(
    name="duration92",
    ends={
        Property(name="Time_MARTE_ValueSpecification94", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing93", type=Time_MARTE_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start95: BinaryAssociation = BinaryAssociation(
    name="start95",
    ends={
        Property(name="Time_MARTE_Event", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing96", type=Time_MARTE_Event, multiplicity=Multiplicity(0, 1))
    }
)
finish97: BinaryAssociation = BinaryAssociation(
    name="finish97",
    ends={
        Property(name="Time_MARTE_Event99", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing98", type=Time_MARTE_Event, multiplicity=Multiplicity(0, 1))
    }
)
resMult100: BinaryAssociation = BinaryAssociation(
    name="resMult100",
    ends={
        Property(name="NFP_Integer", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_Property101: BinaryAssociation = BinaryAssociation(
    name="base_Property101",
    ends={
        Property(name="GRM_MARTE_Property", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource102", type=GRM_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
base_InstanceSpecification103: BinaryAssociation = BinaryAssociation(
    name="base_InstanceSpecification103",
    ends={
        Property(name="GRM_MARTE_InstanceSpecification", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource104", type=GRM_MARTE_InstanceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
mainScheduler123: BinaryAssociation = BinaryAssociation(
    name="mainScheduler123",
    ends={
        Property(name="GRM_Scheduler", type=MARTE_GRM_ProcessingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ProcessingResource124", type=GRM_Scheduler, multiplicity=Multiplicity(0, 1))
    }
)
ceiling125: BinaryAssociation = BinaryAssociation(
    name="ceiling125",
    ends={
        Property(name="NFP_Integer126", type=MARTE_GRM_MutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_MutualExclusionResource", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementSize111: BinaryAssociation = BinaryAssociation(
    name="elementSize111",
    ends={
        Property(name="NFP_Integer112", type=MARTE_GRM_StorageResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_StorageResource", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packetSize113: BinaryAssociation = BinaryAssociation(
    name="packetSize113",
    ends={
        Property(name="NFP_Integer114", type=MARTE_GRM_CommunicationEndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationEndPoint", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schedule115: BinaryAssociation = BinaryAssociation(
    name="schedule115",
    ends={
        Property(name="GRM_MARTE_OpaqueExpression", type=MARTE_GRM_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Scheduler", type=GRM_MARTE_OpaqueExpression, multiplicity=Multiplicity(0, 1))
    }
)
processingUnits116: BinaryAssociation = BinaryAssociation(
    name="processingUnits116",
    ends={
        Property(name="GRM_ProcessingResource", type=MARTE_GRM_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Scheduler117", type=GRM_ProcessingResource, multiplicity=Multiplicity(0, 9999))
    }
)
host118: BinaryAssociation = BinaryAssociation(
    name="host118",
    ends={
        Property(name="GRM_ComputingResource", type=MARTE_GRM_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Scheduler119", type=GRM_ComputingResource, multiplicity=Multiplicity(0, 1))
    }
)
protectedSharedRsources120: BinaryAssociation = BinaryAssociation(
    name="protectedSharedRsources120",
    ends={
        Property(name="MutualExclusionResource", type=MARTE_GRM_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="scheduler", type=GRM_MutualExclusionResource, multiplicity=Multiplicity(0, 9999))
    }
)
schedulableResources121: BinaryAssociation = BinaryAssociation(
    name="schedulableResources121",
    ends={
        Property(name="SchedulableResource", type=MARTE_GRM_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="host", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 9999))
    }
)
speedFactor122: BinaryAssociation = BinaryAssociation(
    name="speedFactor122",
    ends={
        Property(name="NFP_Real", type=MARTE_GRM_ProcessingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ProcessingResource", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration145: BinaryAssociation = BinaryAssociation(
    name="duration145",
    ends={
        Property(name="NFP_Duration146", type=MARTE_GRM_TimerResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_TimerResource", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scheduler127: BinaryAssociation = BinaryAssociation(
    name="scheduler127",
    ends={
        Property(name="Scheduler", type=MARTE_GRM_MutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="protectedSharedRsources", type=GRM_Scheduler, multiplicity=Multiplicity(0, 1))
    }
)
schedParams128: BinaryAssociation = BinaryAssociation(
    name="schedParams128",
    ends={
        Property(name="SchedParameters", type=MARTE_GRM_SchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_SchedulableResource", type=SchedParameters, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependentScheduler129: BinaryAssociation = BinaryAssociation(
    name="dependentScheduler129",
    ends={
        Property(name="SecondaryScheduler", type=MARTE_GRM_SchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="virtualProcessingUnits", type=GRM_SecondaryScheduler, multiplicity=Multiplicity(0, 1))
    }
)
host130: BinaryAssociation = BinaryAssociation(
    name="host130",
    ends={
        Property(name="Scheduler131", type=MARTE_GRM_SchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="schedulableResources", type=GRM_Scheduler, multiplicity=Multiplicity(0, 1))
    }
)
virtualProcessingUnits132: BinaryAssociation = BinaryAssociation(
    name="virtualProcessingUnits132",
    ends={
        Property(name="SchedulableResource133", type=MARTE_GRM_SecondaryScheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="dependentScheduler", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 9999))
    }
)
elementSize134: BinaryAssociation = BinaryAssociation(
    name="elementSize134",
    ends={
        Property(name="NFP_Integer135", type=MARTE_GRM_CommunicationMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationMedia", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_Connector136: BinaryAssociation = BinaryAssociation(
    name="base_Connector136",
    ends={
        Property(name="GRM_MARTE_Connector", type=MARTE_GRM_CommunicationMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationMedia137", type=GRM_MARTE_Connector, multiplicity=Multiplicity(0, 1))
    }
)
blockT138: BinaryAssociation = BinaryAssociation(
    name="blockT138",
    ends={
        Property(name="NFP_Duration", type=MARTE_GRM_CommunicationMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationMedia139", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packetT140: BinaryAssociation = BinaryAssociation(
    name="packetT140",
    ends={
        Property(name="NFP_Duration142", type=MARTE_GRM_CommunicationMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationMedia141", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capacity143: BinaryAssociation = BinaryAssociation(
    name="capacity143",
    ends={
        Property(name="NFP_DataTxRate", type=MARTE_GRM_CommunicationMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationMedia144", type=NFP_DataTxRate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
energy167: BinaryAssociation = BinaryAssociation(
    name="energy167",
    ends={
        Property(name="NFP_Energy", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage168", type=NFP_Energy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base_NamedElement169: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement169",
    ends={
        Property(name="GRM_MARTE_NamedElement", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage170", type=GRM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
subUsage171: BinaryAssociation = BinaryAssociation(
    name="subUsage171",
    ends={
        Property(name="GRM_ResourceUsage", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage172", type=GRM_ResourceUsage, multiplicity=Multiplicity(0, 9999))
    }
)
usedResources173: BinaryAssociation = BinaryAssociation(
    name="usedResources173",
    ends={
        Property(name="GRM_Resource175", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage174", type=GRM_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
owner147: BinaryAssociation = BinaryAssociation(
    name="owner147",
    ends={
        Property(name="GRM_Resource", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)
base_ExecutionSpecification148: BinaryAssociation = BinaryAssociation(
    name="base_ExecutionSpecification148",
    ends={
        Property(name="GRM_MARTE_ExecutionSpecification", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService149", type=GRM_MARTE_ExecutionSpecification, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature150: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature150",
    ends={
        Property(name="GRM_MARTE_BehavioralFeature", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService151", type=GRM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Behavior152: BinaryAssociation = BinaryAssociation(
    name="base_Behavior152",
    ends={
        Property(name="GRM_MARTE_Behavior", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService153", type=GRM_MARTE_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Collaboration154: BinaryAssociation = BinaryAssociation(
    name="base_Collaboration154",
    ends={
        Property(name="GRM_MARTE_Collaboration", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService155", type=GRM_MARTE_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
base_CollaborationUse156: BinaryAssociation = BinaryAssociation(
    name="base_CollaborationUse156",
    ends={
        Property(name="GRM_MARTE_CollaborationUse", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService157", type=GRM_MARTE_CollaborationUse, multiplicity=Multiplicity(1, 1))
    }
)
execTime158: BinaryAssociation = BinaryAssociation(
    name="execTime158",
    ends={
        Property(name="NFP_Duration159", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allocatedMemory160: BinaryAssociation = BinaryAssociation(
    name="allocatedMemory160",
    ends={
        Property(name="NFP_DataSize", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage161", type=NFP_DataSize, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedMemory162: BinaryAssociation = BinaryAssociation(
    name="usedMemory162",
    ends={
        Property(name="NFP_DataSize164", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage163", type=NFP_DataSize, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powerPeak165: BinaryAssociation = BinaryAssociation(
    name="powerPeak165",
    ends={
        Property(name="NFP_Power", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage166", type=NFP_Power, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
origin195: BinaryAssociation = BinaryAssociation(
    name="origin195",
    ends={
        Property(name="IntegerVector196", type=MARTE_RSM_Tiler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Tiler", type=IntegerVector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paving197: BinaryAssociation = BinaryAssociation(
    name="paving197",
    ends={
        Property(name="IntegerMatrix", type=MARTE_RSM_Tiler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Tiler198", type=IntegerMatrix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fitting199: BinaryAssociation = BinaryAssociation(
    name="fitting199",
    ends={
        Property(name="IntegerMatrix201", type=MARTE_RSM_Tiler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Tiler200", type=IntegerMatrix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
msgSize176: BinaryAssociation = BinaryAssociation(
    name="msgSize176",
    ends={
        Property(name="NFP_DataSize178", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage177", type=NFP_DataSize, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base_Connector179: BinaryAssociation = BinaryAssociation(
    name="base_Connector179",
    ends={
        Property(name="RSM_MARTE_Connector", type=MARTE_RSM_LinkTopology, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_LinkTopology", type=RSM_MARTE_Connector, multiplicity=Multiplicity(1, 1))
    }
)
repetitionShapeDependence180: BinaryAssociation = BinaryAssociation(
    name="repetitionShapeDependence180",
    ends={
        Property(name="IntegerVector", type=MARTE_RSM_InterRepetition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_InterRepetition", type=IntegerVector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
patternShape181: BinaryAssociation = BinaryAssociation(
    name="patternShape181",
    ends={
        Property(name="ShapeSpecification", type=MARTE_RSM_Distribute, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Distribute", type=ShapeSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
repetitionSpace182: BinaryAssociation = BinaryAssociation(
    name="repetitionSpace182",
    ends={
        Property(name="ShapeSpecification184", type=MARTE_RSM_Distribute, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Distribute183", type=ShapeSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fromTiler185: BinaryAssociation = BinaryAssociation(
    name="fromTiler185",
    ends={
        Property(name="TilerSpecification", type=MARTE_RSM_Distribute, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Distribute186", type=TilerSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
toTiler187: BinaryAssociation = BinaryAssociation(
    name="toTiler187",
    ends={
        Property(name="TilerSpecification189", type=MARTE_RSM_Distribute, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Distribute188", type=TilerSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
patternShape190: BinaryAssociation = BinaryAssociation(
    name="patternShape190",
    ends={
        Property(name="ShapeSpecification191", type=MARTE_RSM_Reshape, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Reshape", type=ShapeSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
repetitonShape192: BinaryAssociation = BinaryAssociation(
    name="repetitonShape192",
    ends={
        Property(name="ShapeSpecification194", type=MARTE_RSM_Reshape, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Reshape193", type=ShapeSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
base_DataType214: BinaryAssociation = BinaryAssociation(
    name="base_DataType214",
    ends={
        Property(name="DataTypes_MARTE_DataType", type=MARTE_DataTypes_BoundedSubtype, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_BoundedSubtype215", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
intervalAttrib216: BinaryAssociation = BinaryAssociation(
    name="intervalAttrib216",
    ends={
        Property(name="DataTypes_MARTE_Property217", type=MARTE_DataTypes_IntervalType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_IntervalType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_DataType218: BinaryAssociation = BinaryAssociation(
    name="base_DataType218",
    ends={
        Property(name="DataTypes_MARTE_DataType220", type=MARTE_DataTypes_IntervalType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_IntervalType219", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
tiler202: BinaryAssociation = BinaryAssociation(
    name="tiler202",
    ends={
        Property(name="TilerSpecification204", type=MARTE_RSM_Tiler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Tiler203", type=TilerSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_ConnectorEnd205: BinaryAssociation = BinaryAssociation(
    name="base_ConnectorEnd205",
    ends={
        Property(name="RSM_MARTE_ConnectorEnd", type=MARTE_RSM_Tiler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Tiler206", type=RSM_MARTE_ConnectorEnd, multiplicity=Multiplicity(1, 1))
    }
)
shape207: BinaryAssociation = BinaryAssociation(
    name="shape207",
    ends={
        Property(name="ShapeSpecification208", type=MARTE_RSM_Shaped, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Shaped", type=ShapeSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
base_MultiplicityElement209: BinaryAssociation = BinaryAssociation(
    name="base_MultiplicityElement209",
    ends={
        Property(name="RSM_MARTE_MultiplicityElement", type=MARTE_RSM_Shaped, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Shaped210", type=RSM_MARTE_MultiplicityElement, multiplicity=Multiplicity(1, 1))
    }
)
base_Property211: BinaryAssociation = BinaryAssociation(
    name="base_Property211",
    ends={
        Property(name="Variables_MARTE_Property", type=MARTE_Variables_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Variables_Var", type=Variables_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_NamedElement212: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement212",
    ends={
        Property(name="Variables_MARTE_NamedElement", type=MARTE_Variables_ExpressionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Variables_ExpressionContext", type=Variables_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
baseType213: BinaryAssociation = BinaryAssociation(
    name="baseType213",
    ends={
        Property(name="DataTypes_MARTE_Property", type=MARTE_DataTypes_BoundedSubtype, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_BoundedSubtype", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
main243: BinaryAssociation = BinaryAssociation(
    name="main243",
    ends={
        Property(name="HLAM_MARTE_Operation", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit244", type=HLAM_MARTE_Operation, multiplicity=Multiplicity(0, 1))
    }
)
memorySize245: BinaryAssociation = BinaryAssociation(
    name="memorySize245",
    ends={
        Property(name="NFP_DataSize247", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit246", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_BehavioredClassifier248: BinaryAssociation = BinaryAssociation(
    name="base_BehavioredClassifier248",
    ends={
        Property(name="HLAM_MARTE_BehavioredClassifier", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit249", type=HLAM_MARTE_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
collectionAttrib221: BinaryAssociation = BinaryAssociation(
    name="collectionAttrib221",
    ends={
        Property(name="DataTypes_MARTE_Property222", type=MARTE_DataTypes_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_CollectionType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_DataType223: BinaryAssociation = BinaryAssociation(
    name="base_DataType223",
    ends={
        Property(name="DataTypes_MARTE_DataType225", type=MARTE_DataTypes_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_CollectionType224", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
choiceAttrib226: BinaryAssociation = BinaryAssociation(
    name="choiceAttrib226",
    ends={
        Property(name="DataTypes_MARTE_Property227", type=MARTE_DataTypes_ChoiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_ChoiceType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(0, 9999))
    }
)
defaultAttrib228: BinaryAssociation = BinaryAssociation(
    name="defaultAttrib228",
    ends={
        Property(name="DataTypes_MARTE_Property230", type=MARTE_DataTypes_ChoiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_ChoiceType229", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
base_DataType231: BinaryAssociation = BinaryAssociation(
    name="base_DataType231",
    ends={
        Property(name="DataTypes_MARTE_DataType233", type=MARTE_DataTypes_ChoiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_ChoiceType232", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
tupleAttrib234: BinaryAssociation = BinaryAssociation(
    name="tupleAttrib234",
    ends={
        Property(name="DataTypes_MARTE_Property235", type=MARTE_DataTypes_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_TupleType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(0, 9999))
    }
)
base_DataType236: BinaryAssociation = BinaryAssociation(
    name="base_DataType236",
    ends={
        Property(name="DataTypes_MARTE_DataType238", type=MARTE_DataTypes_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_TupleType237", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
srPoolWaitingTime239: BinaryAssociation = BinaryAssociation(
    name="srPoolWaitingTime239",
    ends={
        Property(name="NFP_Duration240", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationalMode241: BinaryAssociation = BinaryAssociation(
    name="operationalMode241",
    ends={
        Property(name="HLAM_MARTE_Behavior", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit242", type=HLAM_MARTE_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
utility269: BinaryAssociation = BinaryAssociation(
    name="utility269",
    ends={
        Property(name="UtilityType", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification", type=UtilityType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
occKind270: BinaryAssociation = BinaryAssociation(
    name="occKind270",
    ends={
        Property(name="ArrivalPattern", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification271", type=ArrivalPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tRef272: BinaryAssociation = BinaryAssociation(
    name="tRef272",
    ends={
        Property(name="Time_TimedInstantObservation", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification273", type=Time_TimedInstantObservation, multiplicity=Multiplicity(0, 1))
    }
)
msgMaxSize250: BinaryAssociation = BinaryAssociation(
    name="msgMaxSize250",
    ends={
        Property(name="NFP_DataSize252", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit251", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memorySize253: BinaryAssociation = BinaryAssociation(
    name="memorySize253",
    ends={
        Property(name="NFP_DataSize254", type=MARTE_HLAM_PpUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_PpUnit", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_BehavioredClassifier255: BinaryAssociation = BinaryAssociation(
    name="base_BehavioredClassifier255",
    ends={
        Property(name="HLAM_MARTE_BehavioredClassifier257", type=MARTE_HLAM_PpUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_PpUnit256", type=HLAM_MARTE_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature258: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature258",
    ends={
        Property(name="HLAM_MARTE_BehavioralFeature", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature", type=HLAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Message259: BinaryAssociation = BinaryAssociation(
    name="base_Message259",
    ends={
        Property(name="HLAM_MARTE_Message", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature260", type=HLAM_MARTE_Message, multiplicity=Multiplicity(1, 1))
    }
)
base_Signal261: BinaryAssociation = BinaryAssociation(
    name="base_Signal261",
    ends={
        Property(name="HLAM_MARTE_Signal", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature262", type=HLAM_MARTE_Signal, multiplicity=Multiplicity(1, 1))
    }
)
base_Port263: BinaryAssociation = BinaryAssociation(
    name="base_Port263",
    ends={
        Property(name="HLAM_MARTE_Port", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature264", type=HLAM_MARTE_Port, multiplicity=Multiplicity(1, 1))
    }
)
base_InvocationAction265: BinaryAssociation = BinaryAssociation(
    name="base_InvocationAction265",
    ends={
        Property(name="HLAM_MARTE_InvocationAction", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature266", type=HLAM_MARTE_InvocationAction, multiplicity=Multiplicity(1, 1))
    }
)
specification267: BinaryAssociation = BinaryAssociation(
    name="specification267",
    ends={
        Property(name="HLAM_RtSpecification", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature268", type=HLAM_RtSpecification, multiplicity=Multiplicity(1, 9999))
    }
)
miss285: BinaryAssociation = BinaryAssociation(
    name="miss285",
    ends={
        Property(name="NFP_Percentage", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification286", type=NFP_Percentage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
priority287: BinaryAssociation = BinaryAssociation(
    name="priority287",
    ends={
        Property(name="NFP_Integer289", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification288", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_Comment290: BinaryAssociation = BinaryAssociation(
    name="base_Comment290",
    ends={
        Property(name="HLAM_MARTE_Comment", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification291", type=HLAM_MARTE_Comment, multiplicity=Multiplicity(1, 1))
    }
)
relDl274: BinaryAssociation = BinaryAssociation(
    name="relDl274",
    ends={
        Property(name="NFP_Duration276", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification275", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
absDl277: BinaryAssociation = BinaryAssociation(
    name="absDl277",
    ends={
        Property(name="NFP_DateTime", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification278", type=NFP_DateTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boundDl279: BinaryAssociation = BinaryAssociation(
    name="boundDl279",
    ends={
        Property(name="NFP_Duration281", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification280", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rdTime282: BinaryAssociation = BinaryAssociation(
    name="rdTime282",
    ends={
        Property(name="NFP_Duration284", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification283", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
msgSize292: BinaryAssociation = BinaryAssociation(
    name="msgSize292",
    ends={
        Property(name="NFP_DataSize293", type=MARTE_HLAM_RtAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtAction", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_BehavioralFeature294: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature294",
    ends={
        Property(name="HLAM_MARTE_BehavioralFeature296", type=MARTE_HLAM_RtAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtAction295", type=HLAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_InvocationAction297: BinaryAssociation = BinaryAssociation(
    name="base_InvocationAction297",
    ends={
        Property(name="HLAM_MARTE_InvocationAction299", type=MARTE_HLAM_RtAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtAction298", type=HLAM_MARTE_InvocationAction, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature300: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature300",
    ends={
        Property(name="HLAM_MARTE_BehavioralFeature301", type=MARTE_HLAM_RtService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtService", type=HLAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
nbPipelines317: BinaryAssociation = BinaryAssociation(
    name="nbPipelines317",
    ends={
        Property(name="MARTE_HwComputing_HwProcessor318", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="NFP_Natural319", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1))
    }
)
nbStages320: BinaryAssociation = BinaryAssociation(
    name="nbStages320",
    ends={
        Property(name="NFP_Natural322", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor321", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbALUs323: BinaryAssociation = BinaryAssociation(
    name="nbALUs323",
    ends={
        Property(name="NFP_Natural325", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor324", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbFPUs326: BinaryAssociation = BinaryAssociation(
    name="nbFPUs326",
    ends={
        Property(name="NFP_Natural328", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor327", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbRows302: BinaryAssociation = BinaryAssociation(
    name="nbRows302",
    ends={
        Property(name="NFP_Integer303", type=MARTE_HwComputing_PLD_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_PLD_Organization", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbColumns304: BinaryAssociation = BinaryAssociation(
    name="nbColumns304",
    ends={
        Property(name="NFP_Natural", type=MARTE_HwComputing_PLD_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_PLD_Organization305", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
architecture306: BinaryAssociation = BinaryAssociation(
    name="architecture306",
    ends={
        Property(name="NFP_DataSize307", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor", type=NFP_DataSize, multiplicity=Multiplicity(0, 1))
    }
)
mips308: BinaryAssociation = BinaryAssociation(
    name="mips308",
    ends={
        Property(name="NFP_Natural310", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor309", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ipc311: BinaryAssociation = BinaryAssociation(
    name="ipc311",
    ends={
        Property(name="NFP_Real313", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor312", type=NFP_Real, multiplicity=Multiplicity(0, 1))
    }
)
nbCores314: BinaryAssociation = BinaryAssociation(
    name="nbCores314",
    ends={
        Property(name="NFP_Natural316", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor315", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization342: BinaryAssociation = BinaryAssociation(
    name="organization342",
    ends={
        Property(name="HwComputing_PLD_Organization", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD", type=HwComputing_PLD_Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbLUTs343: BinaryAssociation = BinaryAssociation(
    name="nbLUTs343",
    ends={
        Property(name="NFP_Natural345", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD344", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ndLUT_Inputs346: BinaryAssociation = BinaryAssociation(
    name="ndLUT_Inputs346",
    ends={
        Property(name="NFP_Natural348", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD347", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbFlipFlops349: BinaryAssociation = BinaryAssociation(
    name="nbFlipFlops349",
    ends={
        Property(name="NFP_Natural351", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD350", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedISAs329: BinaryAssociation = BinaryAssociation(
    name="ownedISAs329",
    ends={
        Property(name="HwComputing_HwISA", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor330", type=HwComputing_HwISA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predictors331: BinaryAssociation = BinaryAssociation(
    name="predictors331",
    ends={
        Property(name="HwComputing_HwBranchPredictor", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor332", type=HwComputing_HwBranchPredictor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caches333: BinaryAssociation = BinaryAssociation(
    name="caches333",
    ends={
        Property(name="HwMemory_HwCache", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor334", type=HwMemory_HwCache, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMMUs335: BinaryAssociation = BinaryAssociation(
    name="ownedMMUs335",
    ends={
        Property(name="HwStorageManager_HwMMU", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor336", type=HwStorageManager_HwMMU, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op_Frequencies337: BinaryAssociation = BinaryAssociation(
    name="op_Frequencies337",
    ends={
        Property(name="NFP_FrequencyInterval", type=MARTE_HwComputing_HwComputingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwComputingResource", type=NFP_FrequencyInterval, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
family338: BinaryAssociation = BinaryAssociation(
    name="family338",
    ends={
        Property(name="NFP_String", type=MARTE_HwComputing_HwISA, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwISA", type=NFP_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inst_Width339: BinaryAssociation = BinaryAssociation(
    name="inst_Width339",
    ends={
        Property(name="NFP_DataSize341", type=MARTE_HwComputing_HwISA, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwISA340", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arbiters370: BinaryAssociation = BinaryAssociation(
    name="arbiters370",
    ends={
        Property(name="HwArbiter", type=MARTE_HwCommunication_HwMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="controlledMedias", type=HwCommunication_HwArbiter, multiplicity=Multiplicity(0, 9999))
    }
)
adressWidth371: BinaryAssociation = BinaryAssociation(
    name="adressWidth371",
    ends={
        Property(name="NFP_DataSize372", type=MARTE_HwCommunication_HwBus, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwBus", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wordWidth373: BinaryAssociation = BinaryAssociation(
    name="wordWidth373",
    ends={
        Property(name="NFP_DataSize375", type=MARTE_HwCommunication_HwBus, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwBus374", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocksRAM352: BinaryAssociation = BinaryAssociation(
    name="blocksRAM352",
    ends={
        Property(name="HwMemory_HwRAM", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD353", type=HwMemory_HwRAM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blocksComputing354: BinaryAssociation = BinaryAssociation(
    name="blocksComputing354",
    ends={
        Property(name="HwComputing_HwComputingResource", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD355", type=HwComputing_HwComputingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processor356: BinaryAssociation = BinaryAssociation(
    name="processor356",
    ends={
        Property(name="HwComputing_HwProcessor", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU", type=HwComputing_HwProcessor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
peripherals357: BinaryAssociation = BinaryAssociation(
    name="peripherals357",
    ends={
        Property(name="HwDevice_HwPeripheral", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU358", type=HwDevice_HwPeripheral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sfr359: BinaryAssociation = BinaryAssociation(
    name="sfr359",
    ends={
        Property(name="HwRegister_HwRegister", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU360", type=HwRegister_HwRegister, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages361: BinaryAssociation = BinaryAssociation(
    name="packages361",
    ends={
        Property(name="HwPackage_HwPackage", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU362", type=HwPackage_HwPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pins363: BinaryAssociation = BinaryAssociation(
    name="pins363",
    ends={
        Property(name="HwIO_HwPin", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU364", type=HwIO_HwPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports365: BinaryAssociation = BinaryAssociation(
    name="ports365",
    ends={
        Property(name="HwCommunication_HwPort", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU366", type=HwCommunication_HwPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlledMedias367: BinaryAssociation = BinaryAssociation(
    name="controlledMedias367",
    ends={
        Property(name="HwMedia", type=MARTE_HwCommunication_HwArbiter, multiplicity=Multiplicity(1, 1)),
        Property(name="arbiters", type=HwCommunication_HwMedia, multiplicity=Multiplicity(0, 9999))
    }
)
bandWidth368: BinaryAssociation = BinaryAssociation(
    name="bandWidth368",
    ends={
        Property(name="NFP_DataTxRate369", type=MARTE_HwCommunication_HwMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwMedia", type=NFP_DataTxRate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transferWidth390: BinaryAssociation = BinaryAssociation(
    name="transferWidth390",
    ends={
        Property(name="NFP_DataSize392", type=MARTE_HwStorageManager_HwDMA, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwDMA391", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
drivenBy393: BinaryAssociation = BinaryAssociation(
    name="drivenBy393",
    ends={
        Property(name="HwComputing_HwProcessor395", type=MARTE_HwStorageManager_HwDMA, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwDMA394", type=HwComputing_HwProcessor, multiplicity=Multiplicity(0, 9999))
    }
)
isSynchronous376: BinaryAssociation = BinaryAssociation(
    name="isSynchronous376",
    ends={
        Property(name="NFP_Boolean", type=MARTE_HwCommunication_HwBus, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwBus377", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isSerial378: BinaryAssociation = BinaryAssociation(
    name="isSerial378",
    ends={
        Property(name="NFP_Boolean380", type=MARTE_HwCommunication_HwBus, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwBus379", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sides381: BinaryAssociation = BinaryAssociation(
    name="sides381",
    ends={
        Property(name="HwCommunication_HwMedia", type=MARTE_HwCommunication_HwBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwBridge", type=HwCommunication_HwMedia, multiplicity=Multiplicity(0, 9999))
    }
)
connectedTo382: BinaryAssociation = BinaryAssociation(
    name="connectedTo382",
    ends={
        Property(name="HwCommunication_HwMedia383", type=MARTE_HwCommunication_HwEndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwEndPoint", type=HwCommunication_HwMedia, multiplicity=Multiplicity(0, 9999))
    }
)
pins384: BinaryAssociation = BinaryAssociation(
    name="pins384",
    ends={
        Property(name="HwIO_HwPin385", type=MARTE_HwCommunication_HwPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwPort", type=HwIO_HwPin, multiplicity=Multiplicity(0, 9999))
    }
)
protocols386: BinaryAssociation = BinaryAssociation(
    name="protocols386",
    ends={
        Property(name="HwProtocol_HwProtocol", type=MARTE_HwCommunication_HwConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwConnection", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999))
    }
)
managedMemories387: BinaryAssociation = BinaryAssociation(
    name="managedMemories387",
    ends={
        Property(name="HwMemory_HwMemory", type=MARTE_HwStorageManager_HwStorageManager, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwStorageManager", type=HwMemory_HwMemory, multiplicity=Multiplicity(0, 9999))
    }
)
nbChannels388: BinaryAssociation = BinaryAssociation(
    name="nbChannels388",
    ends={
        Property(name="NFP_Natural389", type=MARTE_HwStorageManager_HwDMA, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwDMA", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
virtualAddrSpace396: BinaryAssociation = BinaryAssociation(
    name="virtualAddrSpace396",
    ends={
        Property(name="NFP_DataSize397", type=MARTE_HwStorageManager_HwMMU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwMMU", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
physicalAddrSpace398: BinaryAssociation = BinaryAssociation(
    name="physicalAddrSpace398",
    ends={
        Property(name="NFP_DataSize400", type=MARTE_HwStorageManager_HwMMU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwMMU399", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memoryProtection401: BinaryAssociation = BinaryAssociation(
    name="memoryProtection401",
    ends={
        Property(name="NFP_Boolean403", type=MARTE_HwStorageManager_HwMMU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwMMU402", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbEntries404: BinaryAssociation = BinaryAssociation(
    name="nbEntries404",
    ends={
        Property(name="NFP_Natural406", type=MARTE_HwStorageManager_HwMMU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwMMU405", type=NFP_Natural, multiplicity=Multiplicity(0, 1))
    }
)
ownedTLBs407: BinaryAssociation = BinaryAssociation(
    name="ownedTLBs407",
    ends={
        Property(name="HwMemory_HwCache409", type=MARTE_HwStorageManager_HwMMU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwMMU408", type=HwMemory_HwCache, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memorySize410: BinaryAssociation = BinaryAssociation(
    name="memorySize410",
    ends={
        Property(name="NFP_DataSize411", type=MARTE_HwMemory_HwMemory, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwMemory", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
adressSize412: BinaryAssociation = BinaryAssociation(
    name="adressSize412",
    ends={
        Property(name="NFP_DataSize414", type=MARTE_HwMemory_HwMemory, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwMemory413", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timings415: BinaryAssociation = BinaryAssociation(
    name="timings415",
    ends={
        Property(name="HwMemory_Timing", type=MARTE_HwMemory_HwMemory, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwMemory416", type=HwMemory_Timing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
throughput417: BinaryAssociation = BinaryAssociation(
    name="throughput417",
    ends={
        Property(name="NFP_DataTxRate419", type=MARTE_HwMemory_HwMemory, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwMemory418", type=NFP_DataTxRate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
notation420: BinaryAssociation = BinaryAssociation(
    name="notation420",
    ends={
        Property(name="NFP_String421", type=MARTE_HwMemory_Timing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_Timing", type=NFP_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description422: BinaryAssociation = BinaryAssociation(
    name="description422",
    ends={
        Property(name="NFP_String424", type=MARTE_HwMemory_Timing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_Timing423", type=NFP_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value425: BinaryAssociation = BinaryAssociation(
    name="value425",
    ends={
        Property(name="NFP_Duration427", type=MARTE_HwMemory_Timing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_Timing426", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isSynchronous448: BinaryAssociation = BinaryAssociation(
    name="isSynchronous448",
    ends={
        Property(name="NFP_Boolean450", type=MARTE_HwMemory_HwRAM, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwRAM449", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isStatic451: BinaryAssociation = BinaryAssociation(
    name="isStatic451",
    ends={
        Property(name="NFP_Boolean453", type=MARTE_HwMemory_HwRAM, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwRAM452", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isNonVolatile454: BinaryAssociation = BinaryAssociation(
    name="isNonVolatile454",
    ends={
        Property(name="NFP_Boolean456", type=MARTE_HwMemory_HwRAM, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwRAM455", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbSets428: BinaryAssociation = BinaryAssociation(
    name="nbSets428",
    ends={
        Property(name="NFP_Natural429", type=MARTE_HwMemory_CacheStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_CacheStructure", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blockSize430: BinaryAssociation = BinaryAssociation(
    name="blockSize430",
    ends={
        Property(name="NFP_DataSize432", type=MARTE_HwMemory_CacheStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_CacheStructure431", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
associativity433: BinaryAssociation = BinaryAssociation(
    name="associativity433",
    ends={
        Property(name="NFP_Natural435", type=MARTE_HwMemory_CacheStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_CacheStructure434", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbRows436: BinaryAssociation = BinaryAssociation(
    name="nbRows436",
    ends={
        Property(name="NFP_Natural437", type=MARTE_HwMemory_MemoryOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_MemoryOrganization", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbColumns438: BinaryAssociation = BinaryAssociation(
    name="nbColumns438",
    ends={
        Property(name="NFP_Natural440", type=MARTE_HwMemory_MemoryOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_MemoryOrganization439", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbBanks441: BinaryAssociation = BinaryAssociation(
    name="nbBanks441",
    ends={
        Property(name="NFP_Natural443", type=MARTE_HwMemory_MemoryOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_MemoryOrganization442", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wordSize444: BinaryAssociation = BinaryAssociation(
    name="wordSize444",
    ends={
        Property(name="NFP_DataSize446", type=MARTE_HwMemory_MemoryOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_MemoryOrganization445", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization447: BinaryAssociation = BinaryAssociation(
    name="organization447",
    ends={
        Property(name="HwMemory_MemoryOrganization", type=MARTE_HwMemory_HwRAM, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwRAM", type=HwMemory_MemoryOrganization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
counterWidth470: BinaryAssociation = BinaryAssociation(
    name="counterWidth470",
    ends={
        Property(name="NFP_DataSize472", type=MARTE_HwTiming_HwTimer, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwTiming_HwTimer471", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputClock473: BinaryAssociation = BinaryAssociation(
    name="inputClock473",
    ends={
        Property(name="HwTiming_HwClock", type=MARTE_HwTiming_HwTimer, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwTiming_HwTimer474", type=HwTiming_HwClock, multiplicity=Multiplicity(0, 1))
    }
)
functions475: BinaryAssociation = BinaryAssociation(
    name="functions475",
    ends={
        Property(name="HwDeviceFunction_HwDeviceFunction", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice", type=HwDeviceFunction_HwDeviceFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organization457: BinaryAssociation = BinaryAssociation(
    name="organization457",
    ends={
        Property(name="HwMemory_MemoryOrganization458", type=MARTE_HwMemory_HwROM, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwROM", type=HwMemory_MemoryOrganization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sectorSize459: BinaryAssociation = BinaryAssociation(
    name="sectorSize459",
    ends={
        Property(name="NFP_DataSize460", type=MARTE_HwMemory_HwDrive, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwDrive", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buffer461: BinaryAssociation = BinaryAssociation(
    name="buffer461",
    ends={
        Property(name="HwMemory_HwRAM463", type=MARTE_HwMemory_HwDrive, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwDrive462", type=HwMemory_HwRAM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
level464: BinaryAssociation = BinaryAssociation(
    name="level464",
    ends={
        Property(name="NFP_Natural465", type=MARTE_HwMemory_HwCache, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwCache", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structure466: BinaryAssociation = BinaryAssociation(
    name="structure466",
    ends={
        Property(name="HwMemory_CacheStructure", type=MARTE_HwMemory_HwCache, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwCache467", type=HwMemory_CacheStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbCounters468: BinaryAssociation = BinaryAssociation(
    name="nbCounters468",
    ends={
        Property(name="NFP_Natural469", type=MARTE_HwTiming_HwTimer, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwTiming_HwTimer", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
consumption503: BinaryAssociation = BinaryAssociation(
    name="consumption503",
    ends={
        Property(name="NFP_Power504", type=MARTE_HwGeneral_HwResourceService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResourceService", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dissipation505: BinaryAssociation = BinaryAssociation(
    name="dissipation505",
    ends={
        Property(name="NFP_Power507", type=MARTE_HwGeneral_HwResourceService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResourceService506", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compliant476: BinaryAssociation = BinaryAssociation(
    name="compliant476",
    ends={
        Property(name="HwProtocol_HwProtocol478", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice477", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999))
    }
)
packages479: BinaryAssociation = BinaryAssociation(
    name="packages479",
    ends={
        Property(name="HwPackage_HwPackage481", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice480", type=HwPackage_HwPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pins482: BinaryAssociation = BinaryAssociation(
    name="pins482",
    ends={
        Property(name="HwIO_HwPin484", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice483", type=HwIO_HwPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
registers485: BinaryAssociation = BinaryAssociation(
    name="registers485",
    ends={
        Property(name="HwRegister_HwRegister487", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice486", type=HwRegister_HwRegister, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports488: BinaryAssociation = BinaryAssociation(
    name="ports488",
    ends={
        Property(name="HwCommunication_HwPort490", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice489", type=HwCommunication_HwPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements491: BinaryAssociation = BinaryAssociation(
    name="implements491",
    ends={
        Property(name="HwProtocol_HwProtocol492", type=MARTE_HwDevice_HwPeripheral, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwPeripheral", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999))
    }
)
operationimpls493: BinaryAssociation = BinaryAssociation(
    name="operationimpls493",
    ends={
        Property(name="HwPeripheral_OperationImpl", type=MARTE_HwDevice_HwPeripheral, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwPeripheral494", type=HwPeripheral_OperationImpl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refsfr495: BinaryAssociation = BinaryAssociation(
    name="refsfr495",
    ends={
        Property(name="HwRegister_HwRegister497", type=MARTE_HwDevice_HwPeripheral, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwPeripheral496", type=HwRegister_HwRegister, multiplicity=Multiplicity(0, 9999))
    }
)
refports498: BinaryAssociation = BinaryAssociation(
    name="refports498",
    ends={
        Property(name="HwCommunication_HwPort500", type=MARTE_HwDevice_HwPeripheral, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwPeripheral499", type=HwCommunication_HwPort, multiplicity=Multiplicity(0, 9999))
    }
)
peripheralActivities501: BinaryAssociation = BinaryAssociation(
    name="peripheralActivities501",
    ends={
        Property(name="HwPeripheral_PeripheralActivity", type=MARTE_HwDevice_HwPeripheral, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwPeripheral502", type=HwPeripheral_PeripheralActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
area526: BinaryAssociation = BinaryAssociation(
    name="area526",
    ends={
        Property(name="NFP_Area", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent527", type=NFP_Area, multiplicity=Multiplicity(0, 1))
    }
)
position528: BinaryAssociation = BinaryAssociation(
    name="position528",
    ends={
        Property(name="NFP_NaturalInterval", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent529", type=NFP_NaturalInterval, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
grid530: BinaryAssociation = BinaryAssociation(
    name="grid530",
    ends={
        Property(name="NFP_Natural532", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent531", type=NFP_Natural, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
nbPins533: BinaryAssociation = BinaryAssociation(
    name="nbPins533",
    ends={
        Property(name="NFP_Natural535", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent534", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description508: BinaryAssociation = BinaryAssociation(
    name="description508",
    ends={
        Property(name="NFP_String509", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource", type=NFP_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
p_HW_Services510: BinaryAssociation = BinaryAssociation(
    name="p_HW_Services510",
    ends={
        Property(name="HwGeneral_HwResourceService", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource511", type=HwGeneral_HwResourceService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
r_HW_Services512: BinaryAssociation = BinaryAssociation(
    name="r_HW_Services512",
    ends={
        Property(name="HwGeneral_HwResourceService514", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource513", type=HwGeneral_HwResourceService, multiplicity=Multiplicity(0, 9999))
    }
)
ownedHW515: BinaryAssociation = BinaryAssociation(
    name="ownedHW515",
    ends={
        Property(name="HwGeneral_HwResource", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource516", type=HwGeneral_HwResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endPoints517: BinaryAssociation = BinaryAssociation(
    name="endPoints517",
    ends={
        Property(name="HwCommunication_HwEndPoint", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource518", type=HwCommunication_HwEndPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
frequency519: BinaryAssociation = BinaryAssociation(
    name="frequency519",
    ends={
        Property(name="NFP_Frequency", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource520", type=NFP_Frequency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operations521: BinaryAssociation = BinaryAssociation(
    name="operations521",
    ends={
        Property(name="HwGeneral_MARTE_Operation", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource522", type=HwGeneral_MARTE_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities523: BinaryAssociation = BinaryAssociation(
    name="activities523",
    ends={
        Property(name="HwGeneral_MARTE_Activity", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource524", type=HwGeneral_MARTE_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimensions525: BinaryAssociation = BinaryAssociation(
    name="dimensions525",
    ends={
        Property(name="NFP_Length", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent", type=NFP_Length, multiplicity=Multiplicity(0, 3), is_composite=True)
    }
)
range556: BinaryAssociation = BinaryAssociation(
    name="range556",
    ends={
        Property(name="Realnterval", type=MARTE_HwLayout_Env_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_Env_Condition557", type=Realnterval, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
weight536: BinaryAssociation = BinaryAssociation(
    name="weight536",
    ends={
        Property(name="NFP_Real538", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent537", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
price539: BinaryAssociation = BinaryAssociation(
    name="price539",
    ends={
        Property(name="NFP_Price", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent540", type=NFP_Price, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
r_Conditions541: BinaryAssociation = BinaryAssociation(
    name="r_Conditions541",
    ends={
        Property(name="HwLayout_Env_Condition", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent542", type=HwLayout_Env_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
poweredServices543: BinaryAssociation = BinaryAssociation(
    name="poweredServices543",
    ends={
        Property(name="HwGeneral_HwResourceService545", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent544", type=HwGeneral_HwResourceService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticConsumption546: BinaryAssociation = BinaryAssociation(
    name="staticConsumption546",
    ends={
        Property(name="NFP_Power548", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent547", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
staticDissipation549: BinaryAssociation = BinaryAssociation(
    name="staticDissipation549",
    ends={
        Property(name="NFP_Power551", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent550", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subComponents552: BinaryAssociation = BinaryAssociation(
    name="subComponents552",
    ends={
        Property(name="HwLayout_HwComponent", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent553", type=HwLayout_HwComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description554: BinaryAssociation = BinaryAssociation(
    name="description554",
    ends={
        Property(name="NFP_String555", type=MARTE_HwLayout_Env_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_Env_Condition", type=NFP_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suppliedPower558: BinaryAssociation = BinaryAssociation(
    name="suppliedPower558",
    ends={
        Property(name="NFP_Power559", type=MARTE_HwPower_HwPowerSupply, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPower_HwPowerSupply", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity560: BinaryAssociation = BinaryAssociation(
    name="capacity560",
    ends={
        Property(name="NFP_Energy562", type=MARTE_HwPower_HwPowerSupply, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPower_HwPowerSupply561", type=NFP_Energy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
coolingPower563: BinaryAssociation = BinaryAssociation(
    name="coolingPower563",
    ends={
        Property(name="NFP_Power564", type=MARTE_HwPower_HwCoolingSupply, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPower_HwCoolingSupply", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pkgPin571: BinaryAssociation = BinaryAssociation(
    name="pkgPin571",
    ends={
        Property(name="HwPackagePin", type=MARTE_HwIO_HwPin, multiplicity=Multiplicity(1, 1)),
        Property(name="refpin", type=HwPackage_HwPackagePin, multiplicity=Multiplicity(0, 1))
    }
)
lines572: BinaryAssociation = BinaryAssociation(
    name="lines572",
    ends={
        Property(name="HwIO_HwLine", type=MARTE_HwIO_HwPin, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwIO_HwPin", type=HwIO_HwLine, multiplicity=Multiplicity(0, 9999))
    }
)
override565: BinaryAssociation = BinaryAssociation(
    name="override565",
    ends={
        Property(name="HwPeripheral_MARTE_Operation", type=MARTE_HwPeripheral_OperationImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPeripheral_OperationImpl", type=HwPeripheral_MARTE_Operation, multiplicity=Multiplicity(0, 1))
    }
)
register566: BinaryAssociation = BinaryAssociation(
    name="register566",
    ends={
        Property(name="HwRegister_HwRegister567", type=MARTE_HwPeripheral_RegisterAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPeripheral_RegisterAction", type=HwRegister_HwRegister, multiplicity=Multiplicity(0, 1))
    }
)
value568: BinaryAssociation = BinaryAssociation(
    name="value568",
    ends={
        Property(name="HwPeripheral_MARTE_InputPin", type=MARTE_HwPeripheral_WriteRegisterAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPeripheral_WriteRegisterAction", type=HwPeripheral_MARTE_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result569: BinaryAssociation = BinaryAssociation(
    name="result569",
    ends={
        Property(name="HwPeripheral_MARTE_OutputPin", type=MARTE_HwPeripheral_ReadRegisterAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPeripheral_ReadRegisterAction", type=HwPeripheral_MARTE_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
registerActions570: BinaryAssociation = BinaryAssociation(
    name="registerActions570",
    ends={
        Property(name="HwPeripheral_RegisterAction", type=MARTE_HwPeripheral_PeripheralActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPeripheral_PeripheralActivity", type=HwPeripheral_RegisterAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations581: BinaryAssociation = BinaryAssociation(
    name="operations581",
    ends={
        Property(name="HwProtocol_MARTE_Operation", type=MARTE_HwProtocol_HwProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwProtocol_HwProtocol", type=HwProtocol_MARTE_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components573: BinaryAssociation = BinaryAssociation(
    name="components573",
    ends={
        Property(name="HwGeneral_HwResource574", type=MARTE_HwDatasheet_HwDatasheet, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDatasheet_HwDatasheet", type=HwGeneral_HwResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocols575: BinaryAssociation = BinaryAssociation(
    name="protocols575",
    ends={
        Property(name="HwProtocol_HwProtocol577", type=MARTE_HwDatasheet_HwDatasheet, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDatasheet_HwDatasheet576", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pins578: BinaryAssociation = BinaryAssociation(
    name="pins578",
    ends={
        Property(name="HwPackage_HwPackagePin", type=MARTE_HwPackage_HwPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPackage_HwPackage", type=HwPackage_HwPackagePin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refpin579: BinaryAssociation = BinaryAssociation(
    name="refpin579",
    ends={
        Property(name="HwPin", type=MARTE_HwPackage_HwPackagePin, multiplicity=Multiplicity(1, 1)),
        Property(name="pkgPin", type=HwIO_HwPin, multiplicity=Multiplicity(0, 9999))
    }
)
wire580: BinaryAssociation = BinaryAssociation(
    name="wire580",
    ends={
        Property(name="HwPackage_HwWire", type=MARTE_HwPackage_HwPackagePin, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPackage_HwPackagePin", type=HwPackage_HwWire, multiplicity=Multiplicity(0, 9999))
    }
)
components594: BinaryAssociation = BinaryAssociation(
    name="components594",
    ends={
        Property(name="HwGeneral_HwResource595", type=MARTE_HwDiagram_HwHRMDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwHRMDiagram", type=HwGeneral_HwResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections596: BinaryAssociation = BinaryAssociation(
    name="connections596",
    ends={
        Property(name="HwCommunication_HwMedia598", type=MARTE_HwDiagram_HwHRMDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwHRMDiagram597", type=HwCommunication_HwMedia, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocols582: BinaryAssociation = BinaryAssociation(
    name="protocols582",
    ends={
        Property(name="HwProtocol_HwProtocol583", type=MARTE_HwDiagram_HwBlockDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwBlockDiagram", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections584: BinaryAssociation = BinaryAssociation(
    name="connections584",
    ends={
        Property(name="HwCommunication_HwConnection", type=MARTE_HwDiagram_HwBlockDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwBlockDiagram585", type=HwCommunication_HwConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components586: BinaryAssociation = BinaryAssociation(
    name="components586",
    ends={
        Property(name="HwGeneral_HwResource588", type=MARTE_HwDiagram_HwBlockDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwBlockDiagram587", type=HwGeneral_HwResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components589: BinaryAssociation = BinaryAssociation(
    name="components589",
    ends={
        Property(name="HwPackage_HwPackage590", type=MARTE_HwDiagram_HwCircuitDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwCircuitDiagram", type=HwPackage_HwPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wires591: BinaryAssociation = BinaryAssociation(
    name="wires591",
    ends={
        Property(name="HwPackage_HwWire593", type=MARTE_HwDiagram_HwCircuitDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwCircuitDiagram592", type=HwPackage_HwWire, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createServices615: BinaryAssociation = BinaryAssociation(
    name="createServices615",
    ends={
        Property(name="MARTE_SW_ResourceCore_SwResource616", type=SW_ResourceCore_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999)),
        Property(name="SW_ResourceCore_MARTE_BehavioralFeature", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1))
    }
)
deleteServices617: BinaryAssociation = BinaryAssociation(
    name="deleteServices617",
    ends={
        Property(name="SW_ResourceCore_MARTE_BehavioralFeature619", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource618", type=SW_ResourceCore_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
initializeServices620: BinaryAssociation = BinaryAssociation(
    name="initializeServices620",
    ends={
        Property(name="SW_ResourceCore_MARTE_BehavioralFeature622", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource621", type=SW_ResourceCore_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
protocols599: BinaryAssociation = BinaryAssociation(
    name="protocols599",
    ends={
        Property(name="HwProtocol_HwProtocol601", type=MARTE_HwDiagram_HwHRMDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwHRMDiagram600", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypes602: BinaryAssociation = BinaryAssociation(
    name="datatypes602",
    ends={
        Property(name="HwDiagram_MARTE_DataType", type=MARTE_HwDiagram_HwHRMDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwHRMDiagram603", type=HwDiagram_MARTE_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessedElement623: BinaryAssociation = BinaryAssociation(
    name="accessedElement623",
    ends={
        Property(name="SW_ResourceCore_MARTE_Property", type=MARTE_SW_ResourceCore_SwAccessService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwAccessService", type=SW_ResourceCore_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
devices604: BinaryAssociation = BinaryAssociation(
    name="devices604",
    ends={
        Property(name="SW_Brokering_DeviceBroker", type=MARTE_HwDiagram_SRMDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_SRMDiagram", type=SW_Brokering_DeviceBroker, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hwcomponents605: BinaryAssociation = BinaryAssociation(
    name="hwcomponents605",
    ends={
        Property(name="HwGeneral_HwResource607", type=MARTE_HwDiagram_SRMDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_SRMDiagram606", type=HwGeneral_HwResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
routine624: BinaryAssociation = BinaryAssociation(
    name="routine624",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature", type=MARTE_SW_Concurrency_EntryPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_EntryPoint", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
identifierElements608: BinaryAssociation = BinaryAssociation(
    name="identifierElements608",
    ends={
        Property(name="SW_ResourceCore_MARTE_TypedElement", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource", type=SW_ResourceCore_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
stateElements609: BinaryAssociation = BinaryAssociation(
    name="stateElements609",
    ends={
        Property(name="SW_ResourceCore_MARTE_TypedElement611", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource610", type=SW_ResourceCore_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
memorySizeFootprint612: BinaryAssociation = BinaryAssociation(
    name="memorySizeFootprint612",
    ends={
        Property(name="SW_ResourceCore_MARTE_TypedElement614", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource613", type=SW_ResourceCore_MARTE_TypedElement, multiplicity=Multiplicity(0, 1))
    }
)
periodElements631: BinaryAssociation = BinaryAssociation(
    name="periodElements631",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement633", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource632", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
priorityElements634: BinaryAssociation = BinaryAssociation(
    name="priorityElements634",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement636", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource635", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
stackSizeElements637: BinaryAssociation = BinaryAssociation(
    name="stackSizeElements637",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement639", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource638", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
activateServices640: BinaryAssociation = BinaryAssociation(
    name="activateServices640",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature642", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource641", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
enableConcurrencyServices643: BinaryAssociation = BinaryAssociation(
    name="enableConcurrencyServices643",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature645", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource644", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
resumeServices646: BinaryAssociation = BinaryAssociation(
    name="resumeServices646",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature648", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource647", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
suspendServices649: BinaryAssociation = BinaryAssociation(
    name="suspendServices649",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature651", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource650", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
terminateServices652: BinaryAssociation = BinaryAssociation(
    name="terminateServices652",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature654", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource653", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
disableConcurrencyServices655: BinaryAssociation = BinaryAssociation(
    name="disableConcurrencyServices655",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature657", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource656", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
shareDataResources658: BinaryAssociation = BinaryAssociation(
    name="shareDataResources658",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement660", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource659", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
messageResources661: BinaryAssociation = BinaryAssociation(
    name="messageResources661",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement663", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource662", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
type625: BinaryAssociation = BinaryAssociation(
    name="type625",
    ends={
        Property(name="ArrivalPattern626", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource", type=ArrivalPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryPoints627: BinaryAssociation = BinaryAssociation(
    name="entryPoints627",
    ends={
        Property(name="SW_Concurrency_MARTE_Element", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource628", type=SW_Concurrency_MARTE_Element, multiplicity=Multiplicity(0, 9999))
    }
)
adressSpace629: BinaryAssociation = BinaryAssociation(
    name="adressSpace629",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource630", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
vectorElements673: BinaryAssociation = BinaryAssociation(
    name="vectorElements673",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement674", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
maskElements675: BinaryAssociation = BinaryAssociation(
    name="maskElements675",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement677", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource676", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
routineConnectServices678: BinaryAssociation = BinaryAssociation(
    name="routineConnectServices678",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature680", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource679", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
routineDisconnectServices681: BinaryAssociation = BinaryAssociation(
    name="routineDisconnectServices681",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature683", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource682", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
schedulers684: BinaryAssociation = BinaryAssociation(
    name="schedulers684",
    ends={
        Property(name="SW_Concurrency_MARTE_NamedElement", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource", type=SW_Concurrency_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
deadlineElements685: BinaryAssociation = BinaryAssociation(
    name="deadlineElements685",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement687", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource686", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
deadlineTypeElements688: BinaryAssociation = BinaryAssociation(
    name="deadlineTypeElements688",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement690", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource689", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
mutualExclusionResources664: BinaryAssociation = BinaryAssociation(
    name="mutualExclusionResources664",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement666", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource665", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
notificationResources667: BinaryAssociation = BinaryAssociation(
    name="notificationResources667",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement669", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource668", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
heapSizeElements670: BinaryAssociation = BinaryAssociation(
    name="heapSizeElements670",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement672", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource671", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
yieldServices700: BinaryAssociation = BinaryAssociation(
    name="yieldServices700",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature702", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource701", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
durationElements703: BinaryAssociation = BinaryAssociation(
    name="durationElements703",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement704", type=MARTE_SW_Concurrency_SwTimerResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwTimerResource", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 1))
    }
)
concurrentResources705: BinaryAssociation = BinaryAssociation(
    name="concurrentResources705",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement706", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
memorySpaces707: BinaryAssociation = BinaryAssociation(
    name="memorySpaces707",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement709", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition708", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
fork710: BinaryAssociation = BinaryAssociation(
    name="fork710",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature712", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition711", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
exit713: BinaryAssociation = BinaryAssociation(
    name="exit713",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature715", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition714", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
base_Namespace716: BinaryAssociation = BinaryAssociation(
    name="base_Namespace716",
    ends={
        Property(name="SW_Concurrency_MARTE_Namespace", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition717", type=SW_Concurrency_MARTE_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
timeSliceElements691: BinaryAssociation = BinaryAssociation(
    name="timeSliceElements691",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement693", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource692", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
delayServices694: BinaryAssociation = BinaryAssociation(
    name="delayServices694",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature696", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource695", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
joinServices697: BinaryAssociation = BinaryAssociation(
    name="joinServices697",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature699", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource698", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
devices720: BinaryAssociation = BinaryAssociation(
    name="devices720",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
closeServices721: BinaryAssociation = BinaryAssociation(
    name="closeServices721",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker722", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
controlServices723: BinaryAssociation = BinaryAssociation(
    name="controlServices723",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature725", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker724", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
openServices726: BinaryAssociation = BinaryAssociation(
    name="openServices726",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature728", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker727", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
readServices729: BinaryAssociation = BinaryAssociation(
    name="readServices729",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature731", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker730", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
writeServices732: BinaryAssociation = BinaryAssociation(
    name="writeServices732",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature734", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker733", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
operations735: BinaryAssociation = BinaryAssociation(
    name="operations735",
    ends={
        Property(name="SW_Brokering_MARTE_Operation", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker736", type=SW_Brokering_MARTE_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities737: BinaryAssociation = BinaryAssociation(
    name="activities737",
    ends={
        Property(name="SW_Brokering_MARTE_Activity", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker738", type=SW_Brokering_MARTE_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timers718: BinaryAssociation = BinaryAssociation(
    name="timers718",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement719", type=MARTE_SW_Concurrency_Alarm, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_Alarm", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
unlockServices750: BinaryAssociation = BinaryAssociation(
    name="unlockServices750",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature752", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker751", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
mapServices753: BinaryAssociation = BinaryAssociation(
    name="mapServices753",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature755", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker754", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
unMapServices756: BinaryAssociation = BinaryAssociation(
    name="unMapServices756",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature758", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker757", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
memories739: BinaryAssociation = BinaryAssociation(
    name="memories739",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement740", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
memoryBlockAdressElements741: BinaryAssociation = BinaryAssociation(
    name="memoryBlockAdressElements741",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement743", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker742", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
memoryBlockSizeElements744: BinaryAssociation = BinaryAssociation(
    name="memoryBlockSizeElements744",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement746", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker745", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
lockServices747: BinaryAssociation = BinaryAssociation(
    name="lockServices747",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature749", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker748", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
waitingPolicyElements759: BinaryAssociation = BinaryAssociation(
    name="waitingPolicyElements759",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement", type=MARTE_SW_Interaction_SwInteractionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwInteractionResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
readServices760: BinaryAssociation = BinaryAssociation(
    name="readServices760",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature", type=MARTE_SW_Interaction_SharedDataComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SharedDataComResource", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
writeServices761: BinaryAssociation = BinaryAssociation(
    name="writeServices761",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature763", type=MARTE_SW_Interaction_SharedDataComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SharedDataComResource762", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
messageSizeElements764: BinaryAssociation = BinaryAssociation(
    name="messageSizeElements764",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement765", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
messageQueueCapacityElements766: BinaryAssociation = BinaryAssociation(
    name="messageQueueCapacityElements766",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement768", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource767", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
sendServices769: BinaryAssociation = BinaryAssociation(
    name="sendServices769",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature771", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource770", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
maskElements777: BinaryAssociation = BinaryAssociation(
    name="maskElements777",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement779", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource778", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
flushServices780: BinaryAssociation = BinaryAssociation(
    name="flushServices780",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature782", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource781", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
signalServices783: BinaryAssociation = BinaryAssociation(
    name="signalServices783",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature785", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource784", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
waitServices786: BinaryAssociation = BinaryAssociation(
    name="waitServices786",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature788", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource787", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
clearServices789: BinaryAssociation = BinaryAssociation(
    name="clearServices789",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature791", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource790", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
accessTokenElements792: BinaryAssociation = BinaryAssociation(
    name="accessTokenElements792",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement793", type=MARTE_SW_Interaction_SwMutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwMutualExclusionResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
releaseServices794: BinaryAssociation = BinaryAssociation(
    name="releaseServices794",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature796", type=MARTE_SW_Interaction_SwMutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwMutualExclusionResource795", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
acquireServices797: BinaryAssociation = BinaryAssociation(
    name="acquireServices797",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature799", type=MARTE_SW_Interaction_SwMutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwMutualExclusionResource798", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
receiveServices772: BinaryAssociation = BinaryAssociation(
    name="receiveServices772",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature774", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource773", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
occurenceCountElements775: BinaryAssociation = BinaryAssociation(
    name="occurenceCountElements775",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement776", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
base_Port801: BinaryAssociation = BinaryAssociation(
    name="base_Port801",
    ends={
        Property(name="GCM_MARTE_Port", type=MARTE_GCM_FlowPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_FlowPort", type=GCM_MARTE_Port, multiplicity=Multiplicity(1, 1))
    }
)
base_Port802: BinaryAssociation = BinaryAssociation(
    name="base_Port802",
    ends={
        Property(name="GCM_MARTE_Port803", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort", type=GCM_MARTE_Port, multiplicity=Multiplicity(1, 1))
    }
)
provInterface804: BinaryAssociation = BinaryAssociation(
    name="provInterface804",
    ends={
        Property(name="GCM_MARTE_Interface", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort805", type=GCM_MARTE_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
reqInterface806: BinaryAssociation = BinaryAssociation(
    name="reqInterface806",
    ends={
        Property(name="GCM_MARTE_Interface808", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort807", type=GCM_MARTE_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
featuresSpec809: BinaryAssociation = BinaryAssociation(
    name="featuresSpec809",
    ends={
        Property(name="GCM_ClientServerSpecification", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort810", type=GCM_ClientServerSpecification, multiplicity=Multiplicity(0, 1))
    }
)
base_Property800: BinaryAssociation = BinaryAssociation(
    name="base_Property800",
    ends={
        Property(name="GCM_MARTE_Property", type=MARTE_GCM_FlowProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_FlowProperty", type=GCM_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature815: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature815",
    ends={
        Property(name="GCM_MARTE_BehavioralFeature", type=MARTE_GCM_ClientServerFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerFeature", type=GCM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Trigger816: BinaryAssociation = BinaryAssociation(
    name="base_Trigger816",
    ends={
        Property(name="GCM_MARTE_Trigger", type=MARTE_GCM_GCMTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMTrigger", type=GCM_MARTE_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
feature817: BinaryAssociation = BinaryAssociation(
    name="feature817",
    ends={
        Property(name="GCM_MARTE_Feature", type=MARTE_GCM_GCMTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMTrigger818", type=GCM_MARTE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
base_InvocationAction819: BinaryAssociation = BinaryAssociation(
    name="base_InvocationAction819",
    ends={
        Property(name="GCM_MARTE_InvocationAction", type=MARTE_GCM_GCMInvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMInvocationAction", type=GCM_MARTE_InvocationAction, multiplicity=Multiplicity(1, 1))
    }
)
onFeature820: BinaryAssociation = BinaryAssociation(
    name="onFeature820",
    ends={
        Property(name="GCM_MARTE_Feature822", type=MARTE_GCM_GCMInvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMInvocationAction821", type=GCM_MARTE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
base_AnyReceiveEvent823: BinaryAssociation = BinaryAssociation(
    name="base_AnyReceiveEvent823",
    ends={
        Property(name="GCM_MARTE_AnyReceiveEvent", type=MARTE_GCM_DataEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataEvent", type=GCM_MARTE_AnyReceiveEvent, multiplicity=Multiplicity(1, 1))
    }
)
classifier824: BinaryAssociation = BinaryAssociation(
    name="classifier824",
    ends={
        Property(name="GCM_MARTE_Classifier", type=MARTE_GCM_DataEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataEvent825", type=GCM_MARTE_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Property826: BinaryAssociation = BinaryAssociation(
    name="base_Property826",
    ends={
        Property(name="GCM_MARTE_Property827", type=MARTE_GCM_DataPool, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataPool", type=GCM_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_Interface811: BinaryAssociation = BinaryAssociation(
    name="base_Interface811",
    ends={
        Property(name="GCM_MARTE_Interface812", type=MARTE_GCM_ClientServerSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerSpecification", type=GCM_MARTE_Interface, multiplicity=Multiplicity(1, 1))
    }
)
base_Interface813: BinaryAssociation = BinaryAssociation(
    name="base_Interface813",
    ends={
        Property(name="GCM_MARTE_Interface814", type=MARTE_GCM_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_FlowSpecification", type=GCM_MARTE_Interface, multiplicity=Multiplicity(1, 1))
    }
)
pop833: BinaryAssociation = BinaryAssociation(
    name="pop833",
    ends={
        Property(name="NFP_Integer834", type=MARTE_GQAM_GaWorkloadGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadGenerator", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_Behavior835: BinaryAssociation = BinaryAssociation(
    name="base_Behavior835",
    ends={
        Property(name="GQAM_MARTE_Behavior", type=MARTE_GQAM_GaWorkloadGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadGenerator836", type=GQAM_MARTE_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
base_NamedElement837: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement837",
    ends={
        Property(name="GQAM_MARTE_NamedElement", type=MARTE_GQAM_GaEventTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaEventTrace", type=GQAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
pattern838: BinaryAssociation = BinaryAssociation(
    name="pattern838",
    ends={
        Property(name="ArrivalPattern839", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent", type=ArrivalPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generator840: BinaryAssociation = BinaryAssociation(
    name="generator840",
    ends={
        Property(name="GQAM_GaWorkloadGenerator", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent841", type=GQAM_GaWorkloadGenerator, multiplicity=Multiplicity(0, 1))
    }
)
trace842: BinaryAssociation = BinaryAssociation(
    name="trace842",
    ends={
        Property(name="GQAM_GaEventTrace", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent843", type=GQAM_GaEventTrace, multiplicity=Multiplicity(0, 1))
    }
)
effect844: BinaryAssociation = BinaryAssociation(
    name="effect844",
    ends={
        Property(name="GQAM_GaScenario", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent845", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 1))
    }
)
insertion828: BinaryAssociation = BinaryAssociation(
    name="insertion828",
    ends={
        Property(name="GCM_MARTE_Behavior", type=MARTE_GCM_DataPool, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataPool829", type=GCM_MARTE_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
selection830: BinaryAssociation = BinaryAssociation(
    name="selection830",
    ends={
        Property(name="GCM_MARTE_Behavior832", type=MARTE_GCM_DataPool, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataPool831", type=GCM_MARTE_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
base_NamedElement848: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement848",
    ends={
        Property(name="GQAM_MARTE_NamedElement850", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent849", type=GQAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
cause851: BinaryAssociation = BinaryAssociation(
    name="cause851",
    ends={
        Property(name="GQAM_GaWorkloadEvent", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario", type=GQAM_GaWorkloadEvent, multiplicity=Multiplicity(0, 1))
    }
)
hostDemand852: BinaryAssociation = BinaryAssociation(
    name="hostDemand852",
    ends={
        Property(name="NFP_Duration854", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario853", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hostDemandOps855: BinaryAssociation = BinaryAssociation(
    name="hostDemandOps855",
    ends={
        Property(name="NFP_Real857", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario856", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interOccT858: BinaryAssociation = BinaryAssociation(
    name="interOccT858",
    ends={
        Property(name="NFP_Duration860", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario859", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
throughput861: BinaryAssociation = BinaryAssociation(
    name="throughput861",
    ends={
        Property(name="NFP_Frequency863", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario862", type=NFP_Frequency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
respT864: BinaryAssociation = BinaryAssociation(
    name="respT864",
    ends={
        Property(name="NFP_Duration866", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario865", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilization867: BinaryAssociation = BinaryAssociation(
    name="utilization867",
    ends={
        Property(name="NFP_Real869", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario868", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilizationOnHost870: BinaryAssociation = BinaryAssociation(
    name="utilizationOnHost870",
    ends={
        Property(name="NFP_Real872", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario871", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timedEvent846: BinaryAssociation = BinaryAssociation(
    name="timedEvent846",
    ends={
        Property(name="GQAM_MARTE_TimeEvent", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent847", type=GQAM_MARTE_TimeEvent, multiplicity=Multiplicity(0, 1))
    }
)
blockT879: BinaryAssociation = BinaryAssociation(
    name="blockT879",
    ends={
        Property(name="NFP_Duration881", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep880", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rep882: BinaryAssociation = BinaryAssociation(
    name="rep882",
    ends={
        Property(name="NFP_Real884", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep883", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prob885: BinaryAssociation = BinaryAssociation(
    name="prob885",
    ends={
        Property(name="NFP_Real887", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep886", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
priority888: BinaryAssociation = BinaryAssociation(
    name="priority888",
    ends={
        Property(name="NFP_Integer890", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep889", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concurRes891: BinaryAssociation = BinaryAssociation(
    name="concurRes891",
    ends={
        Property(name="GRM_SchedulableResource", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep892", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 1))
    }
)
host893: BinaryAssociation = BinaryAssociation(
    name="host893",
    ends={
        Property(name="GQAM_GaExecHost", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep894", type=GQAM_GaExecHost, multiplicity=Multiplicity(0, 1))
    }
)
servDemand895: BinaryAssociation = BinaryAssociation(
    name="servDemand895",
    ends={
        Property(name="GQAM_GaRequestedService", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep896", type=GQAM_GaRequestedService, multiplicity=Multiplicity(0, 9999))
    }
)
servCount897: BinaryAssociation = BinaryAssociation(
    name="servCount897",
    ends={
        Property(name="NFP_Real899", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep898", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behavior900: BinaryAssociation = BinaryAssociation(
    name="behavior900",
    ends={
        Property(name="GQAM_GaScenario902", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep901", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 1))
    }
)
selfDelay903: BinaryAssociation = BinaryAssociation(
    name="selfDelay903",
    ends={
        Property(name="NFP_Duration905", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep904", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
root873: BinaryAssociation = BinaryAssociation(
    name="root873",
    ends={
        Property(name="GQAM_GaStep", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario874", type=GQAM_GaStep, multiplicity=Multiplicity(0, 1))
    }
)
timing875: BinaryAssociation = BinaryAssociation(
    name="timing875",
    ends={
        Property(name="GQAM_GaTimedObs", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario876", type=GQAM_GaTimedObs, multiplicity=Multiplicity(0, 9999))
    }
)
isAtomic877: BinaryAssociation = BinaryAssociation(
    name="isAtomic877",
    ends={
        Property(name="NFP_Boolean878", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clockOvh914: BinaryAssociation = BinaryAssociation(
    name="clockOvh914",
    ends={
        Property(name="NFP_Duration916", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost915", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schedPriRange917: BinaryAssociation = BinaryAssociation(
    name="schedPriRange917",
    ends={
        Property(name="IntegerInterval", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost918", type=IntegerInterval, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memSize919: BinaryAssociation = BinaryAssociation(
    name="memSize919",
    ends={
        Property(name="NFP_DataSize921", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost920", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
utilization922: BinaryAssociation = BinaryAssociation(
    name="utilization922",
    ends={
        Property(name="NFP_Real924", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost923", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
throughput925: BinaryAssociation = BinaryAssociation(
    name="throughput925",
    ends={
        Property(name="NFP_Frequency927", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost926", type=NFP_Frequency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base_Operation928: BinaryAssociation = BinaryAssociation(
    name="base_Operation928",
    ends={
        Property(name="GQAM_MARTE_Operation", type=MARTE_GQAM_GaRequestedService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaRequestedService", type=GQAM_MARTE_Operation, multiplicity=Multiplicity(1, 1))
    }
)
startObs929: BinaryAssociation = BinaryAssociation(
    name="startObs929",
    ends={
        Property(name="GQAM_MARTE_TimeObservation", type=MARTE_GQAM_GaTimedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaTimedObs", type=GQAM_MARTE_TimeObservation, multiplicity=Multiplicity(0, 9999))
    }
)
commTxOvh906: BinaryAssociation = BinaryAssociation(
    name="commTxOvh906",
    ends={
        Property(name="NFP_Duration907", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commRcvOvh908: BinaryAssociation = BinaryAssociation(
    name="commRcvOvh908",
    ends={
        Property(name="NFP_Duration910", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost909", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cntxtSwT911: BinaryAssociation = BinaryAssociation(
    name="cntxtSwT911",
    ends={
        Property(name="NFP_Duration913", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost912", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
acqRes933: BinaryAssociation = BinaryAssociation(
    name="acqRes933",
    ends={
        Property(name="GRM_Resource934", type=MARTE_GQAM_GaAcqStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAcqStep", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resUnits935: BinaryAssociation = BinaryAssociation(
    name="resUnits935",
    ends={
        Property(name="NFP_Integer937", type=MARTE_GQAM_GaAcqStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAcqStep936", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relRes938: BinaryAssociation = BinaryAssociation(
    name="relRes938",
    ends={
        Property(name="GRM_Resource939", type=MARTE_GQAM_GaRelStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaRelStep", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resUnits940: BinaryAssociation = BinaryAssociation(
    name="resUnits940",
    ends={
        Property(name="NFP_Integer942", type=MARTE_GQAM_GaRelStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaRelStep941", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
latency943: BinaryAssociation = BinaryAssociation(
    name="latency943",
    ends={
        Property(name="NFP_Duration944", type=MARTE_GQAM_GaLatencyObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaLatencyObs", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
miss945: BinaryAssociation = BinaryAssociation(
    name="miss945",
    ends={
        Property(name="NFP_Real947", type=MARTE_GQAM_GaLatencyObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaLatencyObs946", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utility948: BinaryAssociation = BinaryAssociation(
    name="utility948",
    ends={
        Property(name="UtilityType950", type=MARTE_GQAM_GaLatencyObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaLatencyObs949", type=UtilityType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maxJitter951: BinaryAssociation = BinaryAssociation(
    name="maxJitter951",
    ends={
        Property(name="NFP_Duration953", type=MARTE_GQAM_GaLatencyObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaLatencyObs952", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endObs930: BinaryAssociation = BinaryAssociation(
    name="endObs930",
    ends={
        Property(name="GQAM_MARTE_TimeObservation932", type=MARTE_GQAM_GaTimedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaTimedObs931", type=GQAM_MARTE_TimeObservation, multiplicity=Multiplicity(0, 9999))
    }
)
utlization961: BinaryAssociation = BinaryAssociation(
    name="utlization961",
    ends={
        Property(name="NFP_Real963", type=MARTE_GQAM_GaCommChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaCommChannel962", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behavior964: BinaryAssociation = BinaryAssociation(
    name="behavior964",
    ends={
        Property(name="GQAM_GaScenario965", type=MARTE_GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadBehavior", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 9999))
    }
)
demand966: BinaryAssociation = BinaryAssociation(
    name="demand966",
    ends={
        Property(name="GQAM_GaWorkloadEvent968", type=MARTE_GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadBehavior967", type=GQAM_GaWorkloadEvent, multiplicity=Multiplicity(0, 9999))
    }
)
base_NamedElement969: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement969",
    ends={
        Property(name="GQAM_MARTE_NamedElement971", type=MARTE_GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadBehavior970", type=GQAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
context972: BinaryAssociation = BinaryAssociation(
    name="context972",
    ends={
        Property(name="NFP_String973", type=MARTE_GQAM_GaAnalysisContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAnalysisContext", type=NFP_String, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workload974: BinaryAssociation = BinaryAssociation(
    name="workload974",
    ends={
        Property(name="GQAM_GaWorkloadBehavior", type=MARTE_GQAM_GaAnalysisContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAnalysisContext975", type=GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 9999))
    }
)
platform976: BinaryAssociation = BinaryAssociation(
    name="platform976",
    ends={
        Property(name="GQAM_GaResourcesPlatform", type=MARTE_GQAM_GaAnalysisContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAnalysisContext977", type=GQAM_GaResourcesPlatform, multiplicity=Multiplicity(1, 9999))
    }
)
resources978: BinaryAssociation = BinaryAssociation(
    name="resources978",
    ends={
        Property(name="GRM_Resource979", type=MARTE_GQAM_GaResourcesPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaResourcesPlatform", type=GRM_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
throughput954: BinaryAssociation = BinaryAssociation(
    name="throughput954",
    ends={
        Property(name="NFP_Frequency955", type=MARTE_GQAM_GaCommHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaCommHost", type=NFP_Frequency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilization956: BinaryAssociation = BinaryAssociation(
    name="utilization956",
    ends={
        Property(name="NFP_Real958", type=MARTE_GQAM_GaCommHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaCommHost957", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packetSize959: BinaryAssociation = BinaryAssociation(
    name="packetSize959",
    ends={
        Property(name="NFP_DataSize960", type=MARTE_GQAM_GaCommChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaCommChannel", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isSched984: BinaryAssociation = BinaryAssociation(
    name="isSched984",
    ends={
        Property(name="NFP_Boolean985", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schSlack986: BinaryAssociation = BinaryAssociation(
    name="schSlack986",
    ends={
        Property(name="NFP_Real988", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow987", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end2EndT989: BinaryAssociation = BinaryAssociation(
    name="end2EndT989",
    ends={
        Property(name="NFP_Duration991", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow990", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end2EndD992: BinaryAssociation = BinaryAssociation(
    name="end2EndD992",
    ends={
        Property(name="NFP_Duration994", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow993", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timing995: BinaryAssociation = BinaryAssociation(
    name="timing995",
    ends={
        Property(name="GQAM_GaTimedObs997", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow996", type=GQAM_GaTimedObs, multiplicity=Multiplicity(0, 9999))
    }
)
base_NamedElement998: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement998",
    ends={
        Property(name="SAM_MARTE_NamedElement", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow999", type=SAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
deadline1000: BinaryAssociation = BinaryAssociation(
    name="deadline1000",
    ends={
        Property(name="NFP_Duration1001", type=MARTE_SAM_SaCommStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommStep", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spareCap1002: BinaryAssociation = BinaryAssociation(
    name="spareCap1002",
    ends={
        Property(name="NFP_Duration1004", type=MARTE_SAM_SaCommStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommStep1003", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_Classifier980: BinaryAssociation = BinaryAssociation(
    name="base_Classifier980",
    ends={
        Property(name="GQAM_MARTE_Classifier", type=MARTE_GQAM_GaResourcesPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaResourcesPlatform981", type=GQAM_MARTE_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
isSched982: BinaryAssociation = BinaryAssociation(
    name="isSched982",
    ends={
        Property(name="NFP_Boolean983", type=MARTE_SAM_SaAnalysisContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaAnalysisContext", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spareCap1015: BinaryAssociation = BinaryAssociation(
    name="spareCap1015",
    ends={
        Property(name="NFP_Duration1017", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1016", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schSlack1018: BinaryAssociation = BinaryAssociation(
    name="schSlack1018",
    ends={
        Property(name="NFP_Real1020", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1019", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preemptT1021: BinaryAssociation = BinaryAssociation(
    name="preemptT1021",
    ends={
        Property(name="NFP_Duration1023", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1022", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
readyT1024: BinaryAssociation = BinaryAssociation(
    name="readyT1024",
    ends={
        Property(name="NFP_Duration1026", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1025", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nonpreemptionBlocking1027: BinaryAssociation = BinaryAssociation(
    name="nonpreemptionBlocking1027",
    ends={
        Property(name="NFP_Duration1029", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1028", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sharedRes1030: BinaryAssociation = BinaryAssociation(
    name="sharedRes1030",
    ends={
        Property(name="SAM_SaSharedResource", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1031", type=SAM_SaSharedResource, multiplicity=Multiplicity(0, 9999))
    }
)
selfSuspensionBlocking1032: BinaryAssociation = BinaryAssociation(
    name="selfSuspensionBlocking1032",
    ends={
        Property(name="NFP_Duration1034", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1033", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
numberSelfSuspensions1035: BinaryAssociation = BinaryAssociation(
    name="numberSelfSuspensions1035",
    ends={
        Property(name="NFP_Integer1037", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1036", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schSlack1005: BinaryAssociation = BinaryAssociation(
    name="schSlack1005",
    ends={
        Property(name="NFP_Real1007", type=MARTE_SAM_SaCommStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommStep1006", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_BehavioralFeature1008: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature1008",
    ends={
        Property(name="SAM_MARTE_BehavioralFeature", type=MARTE_SAM_SaCommStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommStep1009", type=SAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature1010: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature1010",
    ends={
        Property(name="SAM_MARTE_BehavioralFeature1011", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep", type=SAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
deadline1012: BinaryAssociation = BinaryAssociation(
    name="deadline1012",
    ends={
        Property(name="NFP_Duration1014", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1013", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isConsum1043: BinaryAssociation = BinaryAssociation(
    name="isConsum1043",
    ends={
        Property(name="MARTE_SAM_SaSharedResource1044", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="NFP_Boolean1045", type=MARTE_SAM_SaSharedResource, multiplicity=Multiplicity(1, 1))
    }
)
acquisT1046: BinaryAssociation = BinaryAssociation(
    name="acquisT1046",
    ends={
        Property(name="NFP_Duration1048", type=MARTE_SAM_SaSharedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSharedResource1047", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
releaseT1049: BinaryAssociation = BinaryAssociation(
    name="releaseT1049",
    ends={
        Property(name="NFP_Duration1051", type=MARTE_SAM_SaSharedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSharedResource1050", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
suspentions1052: BinaryAssociation = BinaryAssociation(
    name="suspentions1052",
    ends={
        Property(name="NFP_Integer1053", type=MARTE_SAM_SaSchedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSchedObs", type=NFP_Integer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockT1054: BinaryAssociation = BinaryAssociation(
    name="blockT1054",
    ends={
        Property(name="NFP_Duration1056", type=MARTE_SAM_SaSchedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSchedObs1055", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overlaps1057: BinaryAssociation = BinaryAssociation(
    name="overlaps1057",
    ends={
        Property(name="NFP_Integer1059", type=MARTE_SAM_SaSchedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSchedObs1058", type=NFP_Integer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isSched1060: BinaryAssociation = BinaryAssociation(
    name="isSched1060",
    ends={
        Property(name="NFP_Boolean1061", type=MARTE_SAM_SaCommHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommHost", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity1038: BinaryAssociation = BinaryAssociation(
    name="capacity1038",
    ends={
        Property(name="NFP_Integer1039", type=MARTE_SAM_SaSharedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSharedResource", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isPreemp1040: BinaryAssociation = BinaryAssociation(
    name="isPreemp1040",
    ends={
        Property(name="NFP_Boolean1042", type=MARTE_SAM_SaSharedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSharedResource1041", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schedUtiliz1070: BinaryAssociation = BinaryAssociation(
    name="schedUtiliz1070",
    ends={
        Property(name="NFP_Real1072", type=MARTE_SAM_SaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaExecHost1071", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ISRswitchT1073: BinaryAssociation = BinaryAssociation(
    name="ISRswitchT1073",
    ends={
        Property(name="NFP_Duration1075", type=MARTE_SAM_SaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaExecHost1074", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ISRprioRange1076: BinaryAssociation = BinaryAssociation(
    name="ISRprioRange1076",
    ends={
        Property(name="IntegerInterval1078", type=MARTE_SAM_SaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaExecHost1077", type=IntegerInterval, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noSync1079: BinaryAssociation = BinaryAssociation(
    name="noSync1079",
    ends={
        Property(name="NFP_Boolean1080", type=MARTE_PAM_PaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaStep", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extOpCount1081: BinaryAssociation = BinaryAssociation(
    name="extOpCount1081",
    ends={
        Property(name="NFP_Real1083", type=MARTE_PAM_PaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaStep1082", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behavDemand1084: BinaryAssociation = BinaryAssociation(
    name="behavDemand1084",
    ends={
        Property(name="GQAM_GaScenario1086", type=MARTE_PAM_PaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaStep1085", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 9999))
    }
)
schSlack1062: BinaryAssociation = BinaryAssociation(
    name="schSlack1062",
    ends={
        Property(name="NFP_Real1064", type=MARTE_SAM_SaCommHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommHost1063", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isSched1065: BinaryAssociation = BinaryAssociation(
    name="isSched1065",
    ends={
        Property(name="NFP_Boolean1066", type=MARTE_SAM_SaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaExecHost", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schSlack1067: BinaryAssociation = BinaryAssociation(
    name="schSlack1067",
    ends={
        Property(name="NFP_Real1069", type=MARTE_SAM_SaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaExecHost1068", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resUnits1092: BinaryAssociation = BinaryAssociation(
    name="resUnits1092",
    ends={
        Property(name="NFP_Integer1094", type=MARTE_PAM_PaResPassStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaResPassStep1093", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
utilization1095: BinaryAssociation = BinaryAssociation(
    name="utilization1095",
    ends={
        Property(name="NFP_Real1096", type=MARTE_PAM_PaLogicalResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaLogicalResource", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput1097: BinaryAssociation = BinaryAssociation(
    name="throughput1097",
    ends={
        Property(name="NFP_Frequency1099", type=MARTE_PAM_PaLogicalResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaLogicalResource1098", type=NFP_Frequency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
poolSize1100: BinaryAssociation = BinaryAssociation(
    name="poolSize1100",
    ends={
        Property(name="NFP_Integer1102", type=MARTE_PAM_PaLogicalResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaLogicalResource1101", type=NFP_Integer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
poolSize1103: BinaryAssociation = BinaryAssociation(
    name="poolSize1103",
    ends={
        Property(name="NFP_Integer1104", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instance1105: BinaryAssociation = BinaryAssociation(
    name="instance1105",
    ends={
        Property(name="GRM_SchedulableResource1107", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance1106", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 1))
    }
)
host1108: BinaryAssociation = BinaryAssociation(
    name="host1108",
    ends={
        Property(name="GQAM_GaExecHost1110", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance1109", type=GQAM_GaExecHost, multiplicity=Multiplicity(0, 1))
    }
)
utilization1111: BinaryAssociation = BinaryAssociation(
    name="utilization1111",
    ends={
        Property(name="NFP_Real1113", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance1112", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput1114: BinaryAssociation = BinaryAssociation(
    name="throughput1114",
    ends={
        Property(name="NFP_Frequency1116", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance1115", type=NFP_Frequency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
behavCount1087: BinaryAssociation = BinaryAssociation(
    name="behavCount1087",
    ends={
        Property(name="NFP_Real1089", type=MARTE_PAM_PaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaStep1088", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource1090: BinaryAssociation = BinaryAssociation(
    name="resource1090",
    ends={
        Property(name="GRM_Resource1091", type=MARTE_PAM_PaResPassStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaResPassStep", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)
base_NamedElement1117: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement1117",
    ends={
        Property(name="PAM_MARTE_NamedElement", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance1118", type=PAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_MARTE_NFPs_NfpType_TupleType = Generalization(general=TupleType, specific=MARTE_NFPs_NfpType)
gen_MARTE_Time_TimedDurationObservation_TimedObservation = Generalization(general=TimedObservation, specific=MARTE_Time_TimedDurationObservation)
gen_MARTE_Time_TimedEvent_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedEvent)
gen_MARTE_Time_TimedValueSpecification_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedValueSpecification)
gen_MARTE_Time_TimedConstraint_NFPs_NfpConstraint = Generalization(general=NFPs_NfpConstraint, specific=MARTE_Time_TimedConstraint)
gen_MARTE_Time_TimedConstraint_Time_TimedElement = Generalization(general=Time_TimedElement, specific=MARTE_Time_TimedConstraint)
gen_MARTE_Time_ClockConstraint_NFPs_NfpConstraint = Generalization(general=NFPs_NfpConstraint, specific=MARTE_Time_ClockConstraint)
gen_MARTE_Time_ClockConstraint_Time_TimedElement = Generalization(general=Time_TimedElement, specific=MARTE_Time_ClockConstraint)
gen_MARTE_Time_TimedObservation_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedObservation)
gen_MARTE_Time_TimedInstantObservation_TimedObservation = Generalization(general=TimedObservation, specific=MARTE_Time_TimedInstantObservation)
gen_MARTE_GRM_StorageResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_StorageResource)
gen_MARTE_Time_TimedProcessing_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedProcessing)
gen_MARTE_GRM_ComputingResource_ProcessingResource = Generalization(general=ProcessingResource, specific=MARTE_GRM_ComputingResource)
gen_MARTE_GRM_MutualExclusionResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_MutualExclusionResource)
gen_MARTE_GRM_CommunicationEndPoint_Resource = Generalization(general=Resource, specific=MARTE_GRM_CommunicationEndPoint)
gen_MARTE_GRM_SynchronizationResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_SynchronizationResource)
gen_MARTE_GRM_ConcurrencyResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_ConcurrencyResource)
gen_MARTE_GRM_Scheduler_Resource = Generalization(general=Resource, specific=MARTE_GRM_Scheduler)
gen_MARTE_GRM_ProcessingResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_ProcessingResource)
gen_MARTE_GRM_DeviceResource_ProcessingResource = Generalization(general=ProcessingResource, specific=MARTE_GRM_DeviceResource)
gen_MARTE_GRM_TimingResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_TimingResource)
gen_MARTE_GRM_ClockResource_TimingResource = Generalization(general=TimingResource, specific=MARTE_GRM_ClockResource)
gen_MARTE_GRM_TimerResource_TimingResource = Generalization(general=TimingResource, specific=MARTE_GRM_TimerResource)
gen_MARTE_GRM_SchedulableResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_SchedulableResource)
gen_MARTE_GRM_SecondaryScheduler_Scheduler = Generalization(general=Scheduler, specific=MARTE_GRM_SecondaryScheduler)
gen_MARTE_GRM_CommunicationMedia_ProcessingResource = Generalization(general=ProcessingResource, specific=MARTE_GRM_CommunicationMedia)
gen_MARTE_GRM_Release_GrService = Generalization(general=GrService, specific=MARTE_GRM_Release)
gen_MARTE_GRM_Acquire_GrService = Generalization(general=GrService, specific=MARTE_GRM_Acquire)
gen_MARTE_RSM_Tiler_LinkTopology = Generalization(general=LinkTopology, specific=MARTE_RSM_Tiler)
gen_MARTE_RSM_DefaultLink_LinkTopology = Generalization(general=LinkTopology, specific=MARTE_RSM_DefaultLink)
gen_MARTE_RSM_InterRepetition_LinkTopology = Generalization(general=LinkTopology, specific=MARTE_RSM_InterRepetition)
gen_MARTE_RSM_Distribute_Allocate = Generalization(general=Allocate, specific=MARTE_RSM_Distribute)
gen_MARTE_RSM_Reshape_LinkTopology = Generalization(general=LinkTopology, specific=MARTE_RSM_Reshape)
gen_MARTE_HwComputing_HwProcessor_HwComputingResource = Generalization(general=HwComputingResource, specific=MARTE_HwComputing_HwProcessor)
gen_MARTE_HwComputing_HwComputingResource_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwComputing_HwComputingResource)
gen_MARTE_HwComputing_HwComputingResource_GRM_ComputingResource = Generalization(general=GRM_ComputingResource, specific=MARTE_HwComputing_HwComputingResource)
gen_MARTE_HwComputing_HwISA_HwResource = Generalization(general=HwResource, specific=MARTE_HwComputing_HwISA)
gen_MARTE_HwComputing_HwBranchPredictor_HwResource = Generalization(general=HwResource, specific=MARTE_HwComputing_HwBranchPredictor)
gen_MARTE_HwComputing_HwASIC_HwComputingResource = Generalization(general=HwComputingResource, specific=MARTE_HwComputing_HwASIC)
gen_MARTE_HwComputing_HwPLD_HwComputingResource = Generalization(general=HwComputingResource, specific=MARTE_HwComputing_HwPLD)
gen_MARTE_HwCommunication_HwBus_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwCommunication_HwBus)
gen_MARTE_HwComputing_HwMCU_HwComputingResource = Generalization(general=HwComputingResource, specific=MARTE_HwComputing_HwMCU)
gen_MARTE_HwCommunication_HwCommunicationResource_HwResource = Generalization(general=HwResource, specific=MARTE_HwCommunication_HwCommunicationResource)
gen_MARTE_HwCommunication_HwArbiter_HwCommunicationResource = Generalization(general=HwCommunicationResource, specific=MARTE_HwCommunication_HwArbiter)
gen_MARTE_HwCommunication_HwMedia_GRM_CommunicationMedia = Generalization(general=GRM_CommunicationMedia, specific=MARTE_HwCommunication_HwMedia)
gen_MARTE_HwCommunication_HwMedia_HwCommunication_HwCommunicationResource = Generalization(general=HwCommunication_HwCommunicationResource, specific=MARTE_HwCommunication_HwMedia)
gen_MARTE_HwStorageManager_HwMMU_HwStorageManager = Generalization(general=HwStorageManager, specific=MARTE_HwStorageManager_HwMMU)
gen_MARTE_HwCommunication_HwBridge_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwCommunication_HwBridge)
gen_MARTE_HwCommunication_HwEndPoint_HwCommunication_HwCommunicationResource = Generalization(general=HwCommunication_HwCommunicationResource, specific=MARTE_HwCommunication_HwEndPoint)
gen_MARTE_HwCommunication_HwEndPoint_GRM_CommunicationEndPoint = Generalization(general=GRM_CommunicationEndPoint, specific=MARTE_HwCommunication_HwEndPoint)
gen_MARTE_HwCommunication_HwPort_HwEndPoint = Generalization(general=HwEndPoint, specific=MARTE_HwCommunication_HwPort)
gen_MARTE_HwCommunication_HwConnection_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwCommunication_HwConnection)
gen_MARTE_HwStorageManager_HwStorageManager_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwStorageManager_HwStorageManager)
gen_MARTE_HwStorageManager_HwStorageManager_GRM_StorageResource = Generalization(general=GRM_StorageResource, specific=MARTE_HwStorageManager_HwStorageManager)
gen_MARTE_HwStorageManager_HwDMA_HwStorageManager_HwStorageManager = Generalization(general=HwStorageManager_HwStorageManager, specific=MARTE_HwStorageManager_HwDMA)
gen_MARTE_HwStorageManager_HwDMA_HwCommunication_HwArbiter = Generalization(general=HwCommunication_HwArbiter, specific=MARTE_HwStorageManager_HwDMA)
gen_MARTE_HwMemory_HwMemory_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwMemory_HwMemory)
gen_MARTE_HwMemory_HwMemory_GRM_StorageResource = Generalization(general=GRM_StorageResource, specific=MARTE_HwMemory_HwMemory)
gen_MARTE_HwMemory_HwROM_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwROM)
gen_MARTE_HwMemory_HwRAM_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwRAM)
gen_MARTE_HwDevice_HwDevice_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwDevice_HwDevice)
gen_MARTE_HwDevice_HwDevice_GRM_DeviceResource = Generalization(general=GRM_DeviceResource, specific=MARTE_HwDevice_HwDevice)
gen_MARTE_HwMemory_HwDrive_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwDrive)
gen_MARTE_HwMemory_HwCache_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwCache)
gen_MARTE_HwTiming_HwTimingResource_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwTiming_HwTimingResource)
gen_MARTE_HwTiming_HwTimingResource_GRM_TimingResource = Generalization(general=GRM_TimingResource, specific=MARTE_HwTiming_HwTimingResource)
gen_MARTE_HwTiming_HwClock_HwTimingResource = Generalization(general=HwTimingResource, specific=MARTE_HwTiming_HwClock)
gen_MARTE_HwTiming_HwTimer_HwTimingResource = Generalization(general=HwTimingResource, specific=MARTE_HwTiming_HwTimer)
gen_MARTE_HwGeneral_HwResourceService_GrService = Generalization(general=GrService, specific=MARTE_HwGeneral_HwResourceService)
gen_MARTE_HwGeneral_HwResource_Resource = Generalization(general=Resource, specific=MARTE_HwGeneral_HwResource)
gen_MARTE_HwDevice_HwI_O_HwDevice = Generalization(general=HwDevice, specific=MARTE_HwDevice_HwI_O)
gen_MARTE_HwDevice_HwSupport_HwDevice = Generalization(general=HwDevice, specific=MARTE_HwDevice_HwSupport)
gen_MARTE_HwDevice_HWActuator_HwI_O = Generalization(general=HwI_O, specific=MARTE_HwDevice_HWActuator)
gen_MARTE_HwDevice_HWSensor_HwI_O = Generalization(general=HwI_O, specific=MARTE_HwDevice_HWSensor)
gen_MARTE_HwDevice_HwPeripheral_HwDevice = Generalization(general=HwDevice, specific=MARTE_HwDevice_HwPeripheral)
gen_MARTE_HwLayout_HwComponent_HwResource = Generalization(general=HwResource, specific=MARTE_HwLayout_HwComponent)
gen_MARTE_HwPower_HwCoolingSupply_HwComponent = Generalization(general=HwComponent, specific=MARTE_HwPower_HwCoolingSupply)
gen_MARTE_HwPower_HwPowerSupply_HwComponent = Generalization(general=HwComponent, specific=MARTE_HwPower_HwPowerSupply)
gen_MARTE_HwIO_HwLine_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwIO_HwLine)
gen_MARTE_HwPeripheral_OperationImpl_Operation = Generalization(general=Operation, specific=MARTE_HwPeripheral_OperationImpl)
gen_MARTE_HwPeripheral_RegisterAction_Action = Generalization(general=Action, specific=MARTE_HwPeripheral_RegisterAction)
gen_MARTE_HwPeripheral_WriteRegisterAction_RegisterAction = Generalization(general=RegisterAction, specific=MARTE_HwPeripheral_WriteRegisterAction)
gen_MARTE_HwPeripheral_ReadRegisterAction_RegisterAction = Generalization(general=RegisterAction, specific=MARTE_HwPeripheral_ReadRegisterAction)
gen_MARTE_HwPeripheral_PeripheralActivity_Activity = Generalization(general=Activity, specific=MARTE_HwPeripheral_PeripheralActivity)
gen_MARTE_HwDeviceFunction_HwDeviceFunction_Operation = Generalization(general=Operation, specific=MARTE_HwDeviceFunction_HwDeviceFunction)
gen_MARTE_HwIO_HwPin_HwEndPoint = Generalization(general=HwEndPoint, specific=MARTE_HwIO_HwPin)
gen_MARTE_HwPackage_HwWire_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwPackage_HwWire)
gen_MARTE_HwRegister_HwRegister_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwRegister_HwRegister)
gen_MARTE_HwPackage_HwPackagePin_HwEndPoint = Generalization(general=HwEndPoint, specific=MARTE_HwPackage_HwPackagePin)
gen_MARTE_SW_ResourceCore_SwAccessService_GrService = Generalization(general=GrService, specific=MARTE_SW_ResourceCore_SwAccessService)
gen_MARTE_SW_Concurrency_EntryPoint_Allocate = Generalization(general=Allocate, specific=MARTE_SW_Concurrency_EntryPoint)
gen_MARTE_SW_ResourceCore_SwResource_Resource = Generalization(general=Resource, specific=MARTE_SW_ResourceCore_SwResource)
gen_MARTE_SW_Concurrency_SwConcurrentResource_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Concurrency_SwConcurrentResource)
gen_MARTE_SW_Concurrency_InterruptResource_SwConcurrentResource = Generalization(general=SwConcurrentResource, specific=MARTE_SW_Concurrency_InterruptResource)
gen_MARTE_SW_Concurrency_SwSchedulableResource_SW_Concurrency_SwConcurrentResource = Generalization(general=SW_Concurrency_SwConcurrentResource, specific=MARTE_SW_Concurrency_SwSchedulableResource)
gen_MARTE_SW_Concurrency_SwSchedulableResource_GRM_SchedulableResource = Generalization(general=GRM_SchedulableResource, specific=MARTE_SW_Concurrency_SwSchedulableResource)
gen_MARTE_SW_Concurrency_SwTimerResource_TimerResource = Generalization(general=TimerResource, specific=MARTE_SW_Concurrency_SwTimerResource)
gen_MARTE_SW_Concurrency_MemoryPartition_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Concurrency_MemoryPartition)
gen_MARTE_SW_Concurrency_Alarm_InterruptResource = Generalization(general=InterruptResource, specific=MARTE_SW_Concurrency_Alarm)
gen_MARTE_SW_Brokering_DeviceBroker_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Brokering_DeviceBroker)
gen_MARTE_SW_Brokering_MemoryBroker_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Brokering_MemoryBroker)
gen_MARTE_SW_Interaction_SwCommunicationResource_SW_Interaction_SwInteractionResource = Generalization(general=SW_Interaction_SwInteractionResource, specific=MARTE_SW_Interaction_SwCommunicationResource)
gen_MARTE_SW_Interaction_SwCommunicationResource_GRM_CommunicationMedia = Generalization(general=GRM_CommunicationMedia, specific=MARTE_SW_Interaction_SwCommunicationResource)
gen_MARTE_SW_Interaction_SwSynchronizationResource_SW_Interaction_SwInteractionResource = Generalization(general=SW_Interaction_SwInteractionResource, specific=MARTE_SW_Interaction_SwSynchronizationResource)
gen_MARTE_SW_Interaction_SwSynchronizationResource_GRM_SynchronizationResource = Generalization(general=GRM_SynchronizationResource, specific=MARTE_SW_Interaction_SwSynchronizationResource)
gen_MARTE_SW_Interaction_SharedDataComResource_SwCommunicationResource = Generalization(general=SwCommunicationResource, specific=MARTE_SW_Interaction_SharedDataComResource)
gen_MARTE_SW_Interaction_MessageComResource_SwCommunicationResource = Generalization(general=SwCommunicationResource, specific=MARTE_SW_Interaction_MessageComResource)
gen_MARTE_SW_Interaction_SwInteractionResource_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Interaction_SwInteractionResource)
gen_MARTE_SW_Interaction_SwMutualExclusionResource_SW_Interaction_SwSynchronizationResource = Generalization(general=SW_Interaction_SwSynchronizationResource, specific=MARTE_SW_Interaction_SwMutualExclusionResource)
gen_MARTE_SW_Interaction_SwMutualExclusionResource_GRM_MutualExclusionResource = Generalization(general=GRM_MutualExclusionResource, specific=MARTE_SW_Interaction_SwMutualExclusionResource)
gen_MARTE_SW_Interaction_NotificationResource_SwSynchronizationResource = Generalization(general=SwSynchronizationResource, specific=MARTE_SW_Interaction_NotificationResource)
gen_MARTE_GQAM_GaScenario_GRM_ResourceUsage = Generalization(general=GRM_ResourceUsage, specific=MARTE_GQAM_GaScenario)
gen_MARTE_GQAM_GaScenario_Time_TimedProcessing = Generalization(general=Time_TimedProcessing, specific=MARTE_GQAM_GaScenario)
gen_MARTE_GQAM_GaStep_GaScenario = Generalization(general=GaScenario, specific=MARTE_GQAM_GaStep)
gen_MARTE_GQAM_GaRequestedService_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaRequestedService)
gen_MARTE_GQAM_GaTimedObs_NfpConstraint = Generalization(general=NfpConstraint, specific=MARTE_GQAM_GaTimedObs)
gen_MARTE_GQAM_GaExecHost_GRM_Scheduler = Generalization(general=GRM_Scheduler, specific=MARTE_GQAM_GaExecHost)
gen_MARTE_GQAM_GaExecHost_GRM_ComputingResource = Generalization(general=GRM_ComputingResource, specific=MARTE_GQAM_GaExecHost)
gen_MARTE_GQAM_GaAcqStep_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaAcqStep)
gen_MARTE_GQAM_GaRelStep_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaRelStep)
gen_MARTE_GQAM_GaLatencyObs_GaTimedObs = Generalization(general=GaTimedObs, specific=MARTE_GQAM_GaLatencyObs)
gen_MARTE_GQAM_GaCommStep_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaCommStep)
gen_MARTE_GQAM_GaAnalysisContext_CoreElements_Configuration = Generalization(general=CoreElements_Configuration, specific=MARTE_GQAM_GaAnalysisContext)
gen_MARTE_GQAM_GaAnalysisContext_Variables_ExpressionContext = Generalization(general=Variables_ExpressionContext, specific=MARTE_GQAM_GaAnalysisContext)
gen_MARTE_GQAM_GaCommHost_GRM_CommunicationMedia = Generalization(general=GRM_CommunicationMedia, specific=MARTE_GQAM_GaCommHost)
gen_MARTE_GQAM_GaCommHost_GRM_Scheduler = Generalization(general=GRM_Scheduler, specific=MARTE_GQAM_GaCommHost)
gen_MARTE_GQAM_GaCommChannel_SchedulableResource = Generalization(general=SchedulableResource, specific=MARTE_GQAM_GaCommChannel)
gen_MARTE_SAM_SaCommStep_GaCommStep = Generalization(general=GaCommStep, specific=MARTE_SAM_SaCommStep)
gen_MARTE_SAM_SaAnalysisContext_GaAnalysisContext = Generalization(general=GaAnalysisContext, specific=MARTE_SAM_SaAnalysisContext)
gen_MARTE_SAM_SaStep_GaStep = Generalization(general=GaStep, specific=MARTE_SAM_SaStep)
gen_MARTE_SAM_SaSchedObs_GaTimedObs = Generalization(general=GaTimedObs, specific=MARTE_SAM_SaSchedObs)
gen_MARTE_SAM_SaCommHost_GaCommHost = Generalization(general=GaCommHost, specific=MARTE_SAM_SaCommHost)
gen_MARTE_SAM_SaSharedResource_MutualExclusionResource = Generalization(general=MutualExclusionResource, specific=MARTE_SAM_SaSharedResource)
gen_MARTE_PAM_PaStep_GaStep = Generalization(general=GaStep, specific=MARTE_PAM_PaStep)
gen_MARTE_SAM_SaExecHost_GaExecHost = Generalization(general=GaExecHost, specific=MARTE_SAM_SaExecHost)
gen_MARTE_PAM_PaLogicalResource_Resource = Generalization(general=Resource, specific=MARTE_PAM_PaLogicalResource)
gen_MARTE_PAM_PaRequestedStep_PAM_PaStep = Generalization(general=PAM_PaStep, specific=MARTE_PAM_PaRequestedStep)
gen_MARTE_PAM_PaRequestedStep_GQAM_GaRequestedService = Generalization(general=GQAM_GaRequestedService, specific=MARTE_PAM_PaRequestedStep)
gen_MARTE_PAM_PaCommStep_PAM_PaStep = Generalization(general=PAM_PaStep, specific=MARTE_PAM_PaCommStep)
gen_MARTE_PAM_PaCommStep_GQAM_GaCommStep = Generalization(general=GQAM_GaCommStep, specific=MARTE_PAM_PaCommStep)
gen_MARTE_PAM_PaResPassStep_GaStep = Generalization(general=GaStep, specific=MARTE_PAM_PaResPassStep)

# Domain Model
domain_model = DomainModel(
    name="MARTE",
    types={NFPs_MARTE_Property, MARTE_NFPs_Unit, NFPs_Unit, MARTE_NFPs_Nfp, MARTE_CoreElements_ModeBehavior, CoreElements_MARTE_StateMachine, MARTE_CoreElements_Configuration, CoreElements_MARTE_StructuredClassifier, CoreElements_MARTE_Package, NFPs_MARTE_EnumerationLiteral, MARTE_NFPs_NfpConstraint, NFPs_MARTE_Constraint, CoreElements_Mode, MARTE_NFPs_NfpType, TupleType, MARTE_NFPs_Dimension, NFPs_Dimension, NFPs_MARTE_Enumeration, MARTE_CoreElements_ModeTransition, CoreElements_MARTE_Transition, Alloc_MARTE_Element, Alloc_MARTE_Comment, MARTE_CoreElements_Mode, CoreElements_MARTE_State, MARTE_Alloc_Allocated, Alloc_MARTE_NamedElement, Alloc_Allocated, MARTE_Alloc_AllocateActivityGroup, Alloc_MARTE_ActivityPartition, MARTE_Alloc_NfpRefine, Alloc_MARTE_Dependency, NFPs_NfpConstraint, MARTE_Alloc_Assign, Time_MARTE_Operation, MARTE_Alloc_Allocate, Alloc_MARTE_Abstraction, MARTE_Time_TimedDomain, Time_MARTE_Namespace, MARTE_Time_Clock, Time_MARTE_InstanceSpecification, Time_ClockType, Time_MARTE_Property, MARTE_Time_ClockType, Time_MARTE_Enumeration, Time_MARTE_TimeObservation, MARTE_Time_TimedDurationObservation, Time_MARTE_DurationObservation, MARTE_Time_TimedEvent, Time_MARTE_Class, MARTE_Time_TimedElement, Time_Clock, MARTE_Time_TimedValueSpecification, TimedElement, Time_MARTE_ValueSpecification, MARTE_Time_TimedConstraint, Time_TimedElement, MARTE_Time_ClockConstraint, MARTE_Time_TimedObservation, MARTE_Time_TimedInstantObservation, TimedObservation, GRM_MARTE_Classifier, GRM_MARTE_Lifeline, GRM_MARTE_ConnectableElement, MARTE_GRM_StorageResource, Resource, Time_MARTE_TimeEvent, MARTE_Time_TimedProcessing, Time_MARTE_Action, Time_MARTE_Behavior, Time_MARTE_Message, Time_MARTE_Event, MARTE_GRM_Resource, NFP_Integer, GRM_MARTE_Property, GRM_MARTE_InstanceSpecification, MARTE_GRM_ComputingResource, ProcessingResource, MARTE_GRM_MutualExclusionResource, MARTE_GRM_CommunicationEndPoint, MARTE_GRM_SynchronizationResource, MARTE_GRM_ConcurrencyResource, MARTE_GRM_Scheduler, GRM_MARTE_OpaqueExpression, GRM_ProcessingResource, GRM_ComputingResource, GRM_MutualExclusionResource, GRM_SchedulableResource, MARTE_GRM_ProcessingResource, NFP_Real, GRM_Scheduler, MARTE_GRM_TimingResource, MARTE_GRM_ClockResource, TimingResource, MARTE_GRM_TimerResource, MARTE_GRM_SchedulableResource, SchedParameters, GRM_SecondaryScheduler, MARTE_GRM_SecondaryScheduler, Scheduler, MARTE_GRM_CommunicationMedia, GRM_MARTE_Connector, NFP_Duration, NFP_DataTxRate, MARTE_GRM_DeviceResource, GRM_MARTE_NamedElement, GRM_ResourceUsage, MARTE_GRM_GrService, GRM_Resource, GRM_MARTE_ExecutionSpecification, GRM_MARTE_BehavioralFeature, GRM_MARTE_Behavior, GRM_MARTE_Collaboration, GRM_MARTE_CollaborationUse, MARTE_GRM_Release, GrService, MARTE_GRM_Acquire, MARTE_GRM_ResourceUsage, NFP_DataSize, NFP_Power, NFP_Energy, MARTE_RSM_Tiler, IntegerMatrix, MARTE_RSM_LinkTopology, RSM_MARTE_Connector, MARTE_RSM_DefaultLink, LinkTopology, MARTE_RSM_InterRepetition, IntegerVector, MARTE_RSM_Distribute, Allocate, ShapeSpecification, TilerSpecification, MARTE_RSM_Reshape, DataTypes_MARTE_DataType, MARTE_DataTypes_IntervalType, MARTE_DataTypes_CollectionType, RSM_MARTE_ConnectorEnd, MARTE_RSM_Shaped, RSM_MARTE_MultiplicityElement, MARTE_Variables_Var, Variables_MARTE_Property, MARTE_Variables_ExpressionContext, Variables_MARTE_NamedElement, MARTE_DataTypes_BoundedSubtype, DataTypes_MARTE_Property, HLAM_MARTE_BehavioredClassifier, MARTE_DataTypes_ChoiceType, MARTE_DataTypes_TupleType, MARTE_HLAM_RtUnit, HLAM_MARTE_Behavior, HLAM_MARTE_Operation, MARTE_HLAM_RtSpecification, UtilityType, ArrivalPattern, Time_TimedInstantObservation, MARTE_HLAM_PpUnit, MARTE_HLAM_RtFeature, HLAM_MARTE_BehavioralFeature, HLAM_MARTE_Message, HLAM_MARTE_Signal, HLAM_MARTE_Port, HLAM_MARTE_InvocationAction, HLAM_RtSpecification, NFP_Percentage, HLAM_MARTE_Comment, NFP_DateTime, MARTE_HLAM_RtAction, MARTE_HLAM_RtService, HwComputing_HwISA, MARTE_HwComputing_PLD_Organization, NFP_Natural, MARTE_HwComputing_HwProcessor, HwComputingResource, HwMemory_HwRAM, HwComputing_HwBranchPredictor, HwMemory_HwCache, HwStorageManager_HwMMU, MARTE_HwComputing_HwComputingResource, HwGeneral_HwResource, NFP_FrequencyInterval, MARTE_HwComputing_HwISA, HwResource, NFP_String, MARTE_HwComputing_HwBranchPredictor, MARTE_HwComputing_HwASIC, MARTE_HwComputing_HwPLD, HwComputing_PLD_Organization, HwCommunication_HwArbiter, MARTE_HwCommunication_HwBus, HwMedia, HwComputing_HwComputingResource, MARTE_HwComputing_HwMCU, HwComputing_HwProcessor, HwDevice_HwPeripheral, HwRegister_HwRegister, HwPackage_HwPackage, HwIO_HwPin, HwCommunication_HwPort, MARTE_HwCommunication_HwCommunicationResource, MARTE_HwCommunication_HwArbiter, HwCommunicationResource, HwCommunication_HwMedia, MARTE_HwCommunication_HwMedia, GRM_CommunicationMedia, HwCommunication_HwCommunicationResource, MARTE_HwStorageManager_HwMMU, HwStorageManager, NFP_Boolean, MARTE_HwCommunication_HwBridge, MARTE_HwCommunication_HwEndPoint, GRM_CommunicationEndPoint, MARTE_HwCommunication_HwPort, HwEndPoint, MARTE_HwCommunication_HwConnection, HwProtocol_HwProtocol, MARTE_HwStorageManager_HwStorageManager, GRM_StorageResource, HwMemory_HwMemory, MARTE_HwStorageManager_HwDMA, HwStorageManager_HwStorageManager, MARTE_HwMemory_HwMemory, HwMemory_Timing, MARTE_HwMemory_Timing, MARTE_HwMemory_HwROM, MARTE_HwMemory_CacheStructure, MARTE_HwMemory_MemoryOrganization, MARTE_HwMemory_HwRAM, HwMemory, HwMemory_MemoryOrganization, HwTiming_HwClock, MARTE_HwDevice_HwDevice, GRM_DeviceResource, HwDeviceFunction_HwDeviceFunction, MARTE_HwMemory_HwDrive, MARTE_HwMemory_HwCache, HwMemory_CacheStructure, MARTE_HwTiming_HwTimingResource, GRM_TimingResource, MARTE_HwTiming_HwClock, HwTimingResource, MARTE_HwTiming_HwTimer, MARTE_HwGeneral_HwResourceService, MARTE_HwGeneral_HwResource, MARTE_HwDevice_HwI_O, HwDevice, MARTE_HwDevice_HwSupport, MARTE_HwDevice_HWActuator, HwI_O, MARTE_HwDevice_HWSensor, MARTE_HwDevice_HwPeripheral, HwPeripheral_OperationImpl, HwPeripheral_PeripheralActivity, NFP_Area, NFP_NaturalInterval, HwGeneral_HwResourceService, HwCommunication_HwEndPoint, NFP_Frequency, HwGeneral_MARTE_Operation, HwGeneral_MARTE_Activity, MARTE_HwLayout_HwComponent, NFP_Length, Realnterval, NFP_Price, HwLayout_Env_Condition, HwLayout_HwComponent, MARTE_HwLayout_Env_Condition, MARTE_HwPower_HwCoolingSupply, MARTE_HwPower_HwPowerSupply, HwComponent, HwPackage_HwPackagePin, HwIO_HwLine, MARTE_HwIO_HwLine, MARTE_HwPeripheral_OperationImpl, Operation, HwPeripheral_MARTE_Operation, MARTE_HwPeripheral_RegisterAction, Action, MARTE_HwPeripheral_WriteRegisterAction, RegisterAction, HwPeripheral_MARTE_InputPin, MARTE_HwPeripheral_ReadRegisterAction, HwPeripheral_MARTE_OutputPin, MARTE_HwPeripheral_PeripheralActivity, Activity, HwPeripheral_RegisterAction, MARTE_HwDeviceFunction_HwDeviceFunction, MARTE_HwIO_HwPin, MARTE_HwPackage_HwWire, MARTE_HwProtocol_HwProtocol, HwProtocol_MARTE_Operation, MARTE_HwDiagram_HwBlockDiagram, MARTE_HwRegister_HwRegister, MARTE_HwDatasheet_HwDatasheet, MARTE_HwPackage_HwPackage, MARTE_HwPackage_HwPackagePin, HwPackage_HwWire, MARTE_HwDiagram_HwHRMDiagram, HwCommunication_HwConnection, MARTE_HwDiagram_HwCircuitDiagram, MARTE_SW_ResourceCore_SwAccessService, HwDiagram_MARTE_DataType, SW_ResourceCore_MARTE_Property, MARTE_HwDiagram_SRMDiagram, SW_Brokering_DeviceBroker, MARTE_SW_Concurrency_EntryPoint, MARTE_SW_ResourceCore_SwResource, SW_Concurrency_MARTE_BehavioralFeature, SW_ResourceCore_MARTE_TypedElement, SW_ResourceCore_MARTE_BehavioralFeature, MARTE_SW_Concurrency_SwConcurrentResource, SwResource, SW_Concurrency_MARTE_Element, SW_Concurrency_MARTE_TypedElement, SwConcurrentResource, MARTE_SW_Concurrency_SwSchedulableResource, SW_Concurrency_SwConcurrentResource, SW_Concurrency_MARTE_NamedElement, MARTE_SW_Concurrency_InterruptResource, MARTE_SW_Concurrency_SwTimerResource, TimerResource, MARTE_SW_Concurrency_MemoryPartition, SW_Concurrency_MARTE_Namespace, MARTE_SW_Concurrency_Alarm, InterruptResource, SW_Brokering_MARTE_TypedElement, SW_Brokering_MARTE_BehavioralFeature, SW_Brokering_MARTE_Operation, SW_Brokering_MARTE_Activity, MARTE_SW_Brokering_MemoryBroker, MARTE_SW_Brokering_DeviceBroker, SW_Interaction_MARTE_TypedElement, MARTE_SW_Interaction_SwCommunicationResource, SW_Interaction_SwInteractionResource, MARTE_SW_Interaction_SwSynchronizationResource, GRM_SynchronizationResource, MARTE_SW_Interaction_SharedDataComResource, SwCommunicationResource, SW_Interaction_MARTE_BehavioralFeature, MARTE_SW_Interaction_MessageComResource, MARTE_SW_Interaction_SwInteractionResource, MARTE_SW_Interaction_SwMutualExclusionResource, SW_Interaction_SwSynchronizationResource, MARTE_SW_Interaction_NotificationResource, SwSynchronizationResource, MARTE_GCM_FlowPort, GCM_MARTE_Port, MARTE_GCM_ClientServerPort, GCM_MARTE_Interface, GCM_ClientServerSpecification, MARTE_GCM_FlowProperty, GCM_MARTE_Property, MARTE_GCM_ClientServerFeature, GCM_MARTE_BehavioralFeature, MARTE_GCM_GCMTrigger, GCM_MARTE_Trigger, GCM_MARTE_Feature, MARTE_GCM_GCMInvocationAction, GCM_MARTE_InvocationAction, MARTE_GCM_DataEvent, GCM_MARTE_AnyReceiveEvent, GCM_MARTE_Classifier, MARTE_GCM_DataPool, MARTE_GCM_ClientServerSpecification, MARTE_GCM_FlowSpecification, GQAM_MARTE_Behavior, MARTE_GQAM_GaEventTrace, GQAM_MARTE_NamedElement, MARTE_GQAM_GaWorkloadEvent, GQAM_GaWorkloadGenerator, GQAM_GaEventTrace, GQAM_GaScenario, GQAM_MARTE_TimeEvent, GCM_MARTE_Behavior, MARTE_GQAM_GaWorkloadGenerator, MARTE_GQAM_GaScenario, Time_TimedProcessing, GQAM_GaWorkloadEvent, GQAM_GaExecHost, GQAM_GaRequestedService, MARTE_GQAM_GaExecHost, GQAM_GaStep, GQAM_GaTimedObs, MARTE_GQAM_GaStep, GaScenario, IntegerInterval, MARTE_GQAM_GaRequestedService, GaStep, GQAM_MARTE_Operation, MARTE_GQAM_GaTimedObs, NfpConstraint, GQAM_MARTE_TimeObservation, MARTE_GQAM_GaAcqStep, MARTE_GQAM_GaRelStep, MARTE_GQAM_GaLatencyObs, GaTimedObs, MARTE_GQAM_GaCommStep, MARTE_GQAM_GaWorkloadBehavior, MARTE_GQAM_GaAnalysisContext, CoreElements_Configuration, Variables_ExpressionContext, GQAM_GaWorkloadBehavior, GQAM_GaResourcesPlatform, MARTE_GQAM_GaResourcesPlatform, MARTE_GQAM_GaCommHost, MARTE_GQAM_GaCommChannel, SchedulableResource, MARTE_SAM_SaEndtoEndFlow, SAM_MARTE_NamedElement, MARTE_SAM_SaCommStep, GaCommStep, GQAM_MARTE_Classifier, MARTE_SAM_SaAnalysisContext, GaAnalysisContext, SAM_SaSharedResource, SAM_MARTE_BehavioralFeature, MARTE_SAM_SaStep, MARTE_SAM_SaSchedObs, MARTE_SAM_SaCommHost, GaCommHost, MARTE_SAM_SaSharedResource, MutualExclusionResource, MARTE_PAM_PaStep, MARTE_SAM_SaExecHost, GaExecHost, MARTE_PAM_PaLogicalResource, MARTE_PAM_PaRunTInstance, MARTE_PAM_PaRequestedStep, PAM_PaStep, MARTE_PAM_PaCommStep, GQAM_GaCommStep, MARTE_PAM_PaResPassStep, PAM_MARTE_NamedElement, ConstraintKind, AssignmentKind, AllocationEndKind, AllocationNature, AllocationKind, AssignmentNature, VariableDirectionKind, PoolMgtPolicyKind, CallConcurrencyKind, ISA_Type, SynchronizationKind, ExecutionKind, ConcurrencyKind, PLD_Technology, PLD_Class, Repl_Policy, WritePolicy, CacheType, ROM_Type, ConditionType, ComponentKind, ComponentState, InterruptKind, AccessPolicyKind, QueuePolicyKind, MessageResourceKind, NotificationKind, NotificationResourceKind, MutualExclusionResourceKind, ConcurrentAccessProtocolKind, PortSpecificationKind, FlowDirectionKind, ClientServerKind, DataPoolOrderingKind, LaxityKind, OptimallityCriterionKind},
    associations={base_Property0, base_Transition18, base_StateMachine19, base_StructuredClassifier20, base_Package21, baseUnit1, base_EnumerationLiteral2, base_Constraint4, mode5, valueAttrib7, unitAttrib9, exprAttrib12, baseDimension15, base_Enumeration16, from_39, to41, base_Comment44, mode23, base_State26, base_NamedElement27, allocatedTo28, allocatedFrom30, base_ActivityPartition33, base_Dependency34, constraint35, impliedConstraint37, unitType59, resolAttr60, maxValAttr63, offsetAttr66, base_Abstraction46, impliedConstraint47, base_Namespace50, base_InstanceSpecification51, type52, unit54, base_Property57, base_TimeObservation81, base_DurationObservation82, getTime69, setTime71, indexToValue74, base_Class77, on79, base_ValueSpecification80, base_Classifier105, base_Lifeline107, base_ConnectableElement109, base_TimeEvent83, every84, base_Action87, base_Behavior88, base_Message90, duration92, start95, finish97, resMult100, base_Property101, base_InstanceSpecification103, mainScheduler123, ceiling125, elementSize111, packetSize113, schedule115, processingUnits116, host118, protectedSharedRsources120, schedulableResources121, speedFactor122, duration145, scheduler127, schedParams128, dependentScheduler129, host130, virtualProcessingUnits132, elementSize134, base_Connector136, blockT138, packetT140, capacity143, energy167, base_NamedElement169, subUsage171, usedResources173, owner147, base_ExecutionSpecification148, base_BehavioralFeature150, base_Behavior152, base_Collaboration154, base_CollaborationUse156, execTime158, allocatedMemory160, usedMemory162, powerPeak165, origin195, paving197, fitting199, msgSize176, base_Connector179, repetitionShapeDependence180, patternShape181, repetitionSpace182, fromTiler185, toTiler187, patternShape190, repetitonShape192, base_DataType214, intervalAttrib216, base_DataType218, tiler202, base_ConnectorEnd205, shape207, base_MultiplicityElement209, base_Property211, base_NamedElement212, baseType213, main243, memorySize245, base_BehavioredClassifier248, collectionAttrib221, base_DataType223, choiceAttrib226, defaultAttrib228, base_DataType231, tupleAttrib234, base_DataType236, srPoolWaitingTime239, operationalMode241, utility269, occKind270, tRef272, msgMaxSize250, memorySize253, base_BehavioredClassifier255, base_BehavioralFeature258, base_Message259, base_Signal261, base_Port263, base_InvocationAction265, specification267, miss285, priority287, base_Comment290, relDl274, absDl277, boundDl279, rdTime282, msgSize292, base_BehavioralFeature294, base_InvocationAction297, base_BehavioralFeature300, nbPipelines317, nbStages320, nbALUs323, nbFPUs326, nbRows302, nbColumns304, architecture306, mips308, ipc311, nbCores314, organization342, nbLUTs343, ndLUT_Inputs346, nbFlipFlops349, ownedISAs329, predictors331, caches333, ownedMMUs335, op_Frequencies337, family338, inst_Width339, arbiters370, adressWidth371, wordWidth373, blocksRAM352, blocksComputing354, processor356, peripherals357, sfr359, packages361, pins363, ports365, controlledMedias367, bandWidth368, transferWidth390, drivenBy393, isSynchronous376, isSerial378, sides381, connectedTo382, pins384, protocols386, managedMemories387, nbChannels388, virtualAddrSpace396, physicalAddrSpace398, memoryProtection401, nbEntries404, ownedTLBs407, memorySize410, adressSize412, timings415, throughput417, notation420, description422, value425, isSynchronous448, isStatic451, isNonVolatile454, nbSets428, blockSize430, associativity433, nbRows436, nbColumns438, nbBanks441, wordSize444, organization447, counterWidth470, inputClock473, functions475, organization457, sectorSize459, buffer461, level464, structure466, nbCounters468, consumption503, dissipation505, compliant476, packages479, pins482, registers485, ports488, implements491, operationimpls493, refsfr495, refports498, peripheralActivities501, area526, position528, grid530, nbPins533, description508, p_HW_Services510, r_HW_Services512, ownedHW515, endPoints517, frequency519, operations521, activities523, dimensions525, range556, weight536, price539, r_Conditions541, poweredServices543, staticConsumption546, staticDissipation549, subComponents552, description554, suppliedPower558, capacity560, coolingPower563, pkgPin571, lines572, override565, register566, value568, result569, registerActions570, operations581, components573, protocols575, pins578, refpin579, wire580, components594, connections596, protocols582, connections584, components586, components589, wires591, createServices615, deleteServices617, initializeServices620, protocols599, datatypes602, accessedElement623, devices604, hwcomponents605, routine624, identifierElements608, stateElements609, memorySizeFootprint612, periodElements631, priorityElements634, stackSizeElements637, activateServices640, enableConcurrencyServices643, resumeServices646, suspendServices649, terminateServices652, disableConcurrencyServices655, shareDataResources658, messageResources661, type625, entryPoints627, adressSpace629, vectorElements673, maskElements675, routineConnectServices678, routineDisconnectServices681, schedulers684, deadlineElements685, deadlineTypeElements688, mutualExclusionResources664, notificationResources667, heapSizeElements670, yieldServices700, durationElements703, concurrentResources705, memorySpaces707, fork710, exit713, base_Namespace716, timeSliceElements691, delayServices694, joinServices697, devices720, closeServices721, controlServices723, openServices726, readServices729, writeServices732, operations735, activities737, timers718, unlockServices750, mapServices753, unMapServices756, memories739, memoryBlockAdressElements741, memoryBlockSizeElements744, lockServices747, waitingPolicyElements759, readServices760, writeServices761, messageSizeElements764, messageQueueCapacityElements766, sendServices769, maskElements777, flushServices780, signalServices783, waitServices786, clearServices789, accessTokenElements792, releaseServices794, acquireServices797, receiveServices772, occurenceCountElements775, base_Port801, base_Port802, provInterface804, reqInterface806, featuresSpec809, base_Property800, base_BehavioralFeature815, base_Trigger816, feature817, base_InvocationAction819, onFeature820, base_AnyReceiveEvent823, classifier824, base_Property826, base_Interface811, base_Interface813, pop833, base_Behavior835, base_NamedElement837, pattern838, generator840, trace842, effect844, insertion828, selection830, base_NamedElement848, cause851, hostDemand852, hostDemandOps855, interOccT858, throughput861, respT864, utilization867, utilizationOnHost870, timedEvent846, blockT879, rep882, prob885, priority888, concurRes891, host893, servDemand895, servCount897, behavior900, selfDelay903, root873, timing875, isAtomic877, clockOvh914, schedPriRange917, memSize919, utilization922, throughput925, base_Operation928, startObs929, commTxOvh906, commRcvOvh908, cntxtSwT911, acqRes933, resUnits935, relRes938, resUnits940, latency943, miss945, utility948, maxJitter951, endObs930, utlization961, behavior964, demand966, base_NamedElement969, context972, workload974, platform976, resources978, throughput954, utilization956, packetSize959, isSched984, schSlack986, end2EndT989, end2EndD992, timing995, base_NamedElement998, deadline1000, spareCap1002, base_Classifier980, isSched982, spareCap1015, schSlack1018, preemptT1021, readyT1024, nonpreemptionBlocking1027, sharedRes1030, selfSuspensionBlocking1032, numberSelfSuspensions1035, schSlack1005, base_BehavioralFeature1008, base_BehavioralFeature1010, deadline1012, isConsum1043, acquisT1046, releaseT1049, suspentions1052, blockT1054, overlaps1057, isSched1060, capacity1038, isPreemp1040, schedUtiliz1070, ISRswitchT1073, ISRprioRange1076, noSync1079, extOpCount1081, behavDemand1084, schSlack1062, isSched1065, schSlack1067, resUnits1092, utilization1095, throughput1097, poolSize1100, poolSize1103, instance1105, host1108, utilization1111, throughput1114, behavCount1087, resource1090, base_NamedElement1117},
    generalizations={gen_MARTE_NFPs_NfpType_TupleType, gen_MARTE_Time_TimedDurationObservation_TimedObservation, gen_MARTE_Time_TimedEvent_TimedElement, gen_MARTE_Time_TimedValueSpecification_TimedElement, gen_MARTE_Time_TimedConstraint_NFPs_NfpConstraint, gen_MARTE_Time_TimedConstraint_Time_TimedElement, gen_MARTE_Time_ClockConstraint_NFPs_NfpConstraint, gen_MARTE_Time_ClockConstraint_Time_TimedElement, gen_MARTE_Time_TimedObservation_TimedElement, gen_MARTE_Time_TimedInstantObservation_TimedObservation, gen_MARTE_GRM_StorageResource_Resource, gen_MARTE_Time_TimedProcessing_TimedElement, gen_MARTE_GRM_ComputingResource_ProcessingResource, gen_MARTE_GRM_MutualExclusionResource_Resource, gen_MARTE_GRM_CommunicationEndPoint_Resource, gen_MARTE_GRM_SynchronizationResource_Resource, gen_MARTE_GRM_ConcurrencyResource_Resource, gen_MARTE_GRM_Scheduler_Resource, gen_MARTE_GRM_ProcessingResource_Resource, gen_MARTE_GRM_DeviceResource_ProcessingResource, gen_MARTE_GRM_TimingResource_Resource, gen_MARTE_GRM_ClockResource_TimingResource, gen_MARTE_GRM_TimerResource_TimingResource, gen_MARTE_GRM_SchedulableResource_Resource, gen_MARTE_GRM_SecondaryScheduler_Scheduler, gen_MARTE_GRM_CommunicationMedia_ProcessingResource, gen_MARTE_GRM_Release_GrService, gen_MARTE_GRM_Acquire_GrService, gen_MARTE_RSM_Tiler_LinkTopology, gen_MARTE_RSM_DefaultLink_LinkTopology, gen_MARTE_RSM_InterRepetition_LinkTopology, gen_MARTE_RSM_Distribute_Allocate, gen_MARTE_RSM_Reshape_LinkTopology, gen_MARTE_HwComputing_HwProcessor_HwComputingResource, gen_MARTE_HwComputing_HwComputingResource_HwGeneral_HwResource, gen_MARTE_HwComputing_HwComputingResource_GRM_ComputingResource, gen_MARTE_HwComputing_HwISA_HwResource, gen_MARTE_HwComputing_HwBranchPredictor_HwResource, gen_MARTE_HwComputing_HwASIC_HwComputingResource, gen_MARTE_HwComputing_HwPLD_HwComputingResource, gen_MARTE_HwCommunication_HwBus_HwMedia, gen_MARTE_HwComputing_HwMCU_HwComputingResource, gen_MARTE_HwCommunication_HwCommunicationResource_HwResource, gen_MARTE_HwCommunication_HwArbiter_HwCommunicationResource, gen_MARTE_HwCommunication_HwMedia_GRM_CommunicationMedia, gen_MARTE_HwCommunication_HwMedia_HwCommunication_HwCommunicationResource, gen_MARTE_HwStorageManager_HwMMU_HwStorageManager, gen_MARTE_HwCommunication_HwBridge_HwMedia, gen_MARTE_HwCommunication_HwEndPoint_HwCommunication_HwCommunicationResource, gen_MARTE_HwCommunication_HwEndPoint_GRM_CommunicationEndPoint, gen_MARTE_HwCommunication_HwPort_HwEndPoint, gen_MARTE_HwCommunication_HwConnection_HwMedia, gen_MARTE_HwStorageManager_HwStorageManager_HwGeneral_HwResource, gen_MARTE_HwStorageManager_HwStorageManager_GRM_StorageResource, gen_MARTE_HwStorageManager_HwDMA_HwStorageManager_HwStorageManager, gen_MARTE_HwStorageManager_HwDMA_HwCommunication_HwArbiter, gen_MARTE_HwMemory_HwMemory_HwGeneral_HwResource, gen_MARTE_HwMemory_HwMemory_GRM_StorageResource, gen_MARTE_HwMemory_HwROM_HwMemory, gen_MARTE_HwMemory_HwRAM_HwMemory, gen_MARTE_HwDevice_HwDevice_HwGeneral_HwResource, gen_MARTE_HwDevice_HwDevice_GRM_DeviceResource, gen_MARTE_HwMemory_HwDrive_HwMemory, gen_MARTE_HwMemory_HwCache_HwMemory, gen_MARTE_HwTiming_HwTimingResource_HwGeneral_HwResource, gen_MARTE_HwTiming_HwTimingResource_GRM_TimingResource, gen_MARTE_HwTiming_HwClock_HwTimingResource, gen_MARTE_HwTiming_HwTimer_HwTimingResource, gen_MARTE_HwGeneral_HwResourceService_GrService, gen_MARTE_HwGeneral_HwResource_Resource, gen_MARTE_HwDevice_HwI_O_HwDevice, gen_MARTE_HwDevice_HwSupport_HwDevice, gen_MARTE_HwDevice_HWActuator_HwI_O, gen_MARTE_HwDevice_HWSensor_HwI_O, gen_MARTE_HwDevice_HwPeripheral_HwDevice, gen_MARTE_HwLayout_HwComponent_HwResource, gen_MARTE_HwPower_HwCoolingSupply_HwComponent, gen_MARTE_HwPower_HwPowerSupply_HwComponent, gen_MARTE_HwIO_HwLine_HwMedia, gen_MARTE_HwPeripheral_OperationImpl_Operation, gen_MARTE_HwPeripheral_RegisterAction_Action, gen_MARTE_HwPeripheral_WriteRegisterAction_RegisterAction, gen_MARTE_HwPeripheral_ReadRegisterAction_RegisterAction, gen_MARTE_HwPeripheral_PeripheralActivity_Activity, gen_MARTE_HwDeviceFunction_HwDeviceFunction_Operation, gen_MARTE_HwIO_HwPin_HwEndPoint, gen_MARTE_HwPackage_HwWire_HwMedia, gen_MARTE_HwRegister_HwRegister_HwMemory, gen_MARTE_HwPackage_HwPackagePin_HwEndPoint, gen_MARTE_SW_ResourceCore_SwAccessService_GrService, gen_MARTE_SW_Concurrency_EntryPoint_Allocate, gen_MARTE_SW_ResourceCore_SwResource_Resource, gen_MARTE_SW_Concurrency_SwConcurrentResource_SwResource, gen_MARTE_SW_Concurrency_InterruptResource_SwConcurrentResource, gen_MARTE_SW_Concurrency_SwSchedulableResource_SW_Concurrency_SwConcurrentResource, gen_MARTE_SW_Concurrency_SwSchedulableResource_GRM_SchedulableResource, gen_MARTE_SW_Concurrency_SwTimerResource_TimerResource, gen_MARTE_SW_Concurrency_MemoryPartition_SwResource, gen_MARTE_SW_Concurrency_Alarm_InterruptResource, gen_MARTE_SW_Brokering_DeviceBroker_SwResource, gen_MARTE_SW_Brokering_MemoryBroker_SwResource, gen_MARTE_SW_Interaction_SwCommunicationResource_SW_Interaction_SwInteractionResource, gen_MARTE_SW_Interaction_SwCommunicationResource_GRM_CommunicationMedia, gen_MARTE_SW_Interaction_SwSynchronizationResource_SW_Interaction_SwInteractionResource, gen_MARTE_SW_Interaction_SwSynchronizationResource_GRM_SynchronizationResource, gen_MARTE_SW_Interaction_SharedDataComResource_SwCommunicationResource, gen_MARTE_SW_Interaction_MessageComResource_SwCommunicationResource, gen_MARTE_SW_Interaction_SwInteractionResource_SwResource, gen_MARTE_SW_Interaction_SwMutualExclusionResource_SW_Interaction_SwSynchronizationResource, gen_MARTE_SW_Interaction_SwMutualExclusionResource_GRM_MutualExclusionResource, gen_MARTE_SW_Interaction_NotificationResource_SwSynchronizationResource, gen_MARTE_GQAM_GaScenario_GRM_ResourceUsage, gen_MARTE_GQAM_GaScenario_Time_TimedProcessing, gen_MARTE_GQAM_GaStep_GaScenario, gen_MARTE_GQAM_GaRequestedService_GaStep, gen_MARTE_GQAM_GaTimedObs_NfpConstraint, gen_MARTE_GQAM_GaExecHost_GRM_Scheduler, gen_MARTE_GQAM_GaExecHost_GRM_ComputingResource, gen_MARTE_GQAM_GaAcqStep_GaStep, gen_MARTE_GQAM_GaRelStep_GaStep, gen_MARTE_GQAM_GaLatencyObs_GaTimedObs, gen_MARTE_GQAM_GaCommStep_GaStep, gen_MARTE_GQAM_GaAnalysisContext_CoreElements_Configuration, gen_MARTE_GQAM_GaAnalysisContext_Variables_ExpressionContext, gen_MARTE_GQAM_GaCommHost_GRM_CommunicationMedia, gen_MARTE_GQAM_GaCommHost_GRM_Scheduler, gen_MARTE_GQAM_GaCommChannel_SchedulableResource, gen_MARTE_SAM_SaCommStep_GaCommStep, gen_MARTE_SAM_SaAnalysisContext_GaAnalysisContext, gen_MARTE_SAM_SaStep_GaStep, gen_MARTE_SAM_SaSchedObs_GaTimedObs, gen_MARTE_SAM_SaCommHost_GaCommHost, gen_MARTE_SAM_SaSharedResource_MutualExclusionResource, gen_MARTE_PAM_PaStep_GaStep, gen_MARTE_SAM_SaExecHost_GaExecHost, gen_MARTE_PAM_PaLogicalResource_Resource, gen_MARTE_PAM_PaRequestedStep_PAM_PaStep, gen_MARTE_PAM_PaRequestedStep_GQAM_GaRequestedService, gen_MARTE_PAM_PaCommStep_PAM_PaStep, gen_MARTE_PAM_PaCommStep_GQAM_GaCommStep, gen_MARTE_PAM_PaResPassStep_GaStep},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)