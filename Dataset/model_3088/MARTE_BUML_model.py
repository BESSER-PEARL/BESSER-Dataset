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

AllocationEndKind: Enumeration = Enumeration(
    name="AllocationEndKind",
    literals={
            EnumerationLiteral(name="undef"),
			EnumerationLiteral(name="application"),
			EnumerationLiteral(name="executionPlatform"),
			EnumerationLiteral(name="both")
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
            EnumerationLiteral(name="structural"),
			EnumerationLiteral(name="behavioral"),
			EnumerationLiteral(name="hybrid")
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

AssignmentNature: Enumeration = Enumeration(
    name="AssignmentNature",
    literals={
            EnumerationLiteral(name="timeScheduling"),
			EnumerationLiteral(name="spatialDistribution")
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

dummy: Enumeration = Enumeration(
    name="dummy",
    literals={
            
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

FlowDirectionKind: Enumeration = Enumeration(
    name="FlowDirectionKind",
    literals={
            EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout")
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
MARTE_NFPs_Nfp = Class(name="MARTE_NFPs_Nfp")
NFPs_MARTE_Property = Class(name="NFPs_MARTE_Property")
MARTE_NFPs_Unit = Class(name="MARTE_NFPs_Unit")
NFPs_Unit = Class(name="NFPs_Unit")
NFPs_MARTE_EnumerationLiteral = Class(name="NFPs_MARTE_EnumerationLiteral")
MARTE_NFPs_NfpConstraint = Class(name="MARTE_NFPs_NfpConstraint")
NFPs_MARTE_Constraint = Class(name="NFPs_MARTE_Constraint")
MARTE_NFPs_Dimension = Class(name="MARTE_NFPs_Dimension")
NFPs_Dimension = Class(name="NFPs_Dimension")
NFPs_MARTE_Enumeration = Class(name="NFPs_MARTE_Enumeration")
MARTE_CoreElements_ModeTransition = Class(name="MARTE_CoreElements_ModeTransition")
CoreElements_MARTE_Transition = Class(name="CoreElements_MARTE_Transition")
MARTE_CoreElements_ModeBehavior = Class(name="MARTE_CoreElements_ModeBehavior")
CoreElements_MARTE_StateMachine = Class(name="CoreElements_MARTE_StateMachine")
MARTE_CoreElements_Configuration = Class(name="MARTE_CoreElements_Configuration")
CoreElements_MARTE_StructuredClassifier = Class(name="CoreElements_MARTE_StructuredClassifier")
CoreElements_MARTE_Package = Class(name="CoreElements_MARTE_Package")
MARTE_CoreElements_Mode = Class(name="MARTE_CoreElements_Mode")
CoreElements_MARTE_State = Class(name="CoreElements_MARTE_State")
MARTE_Alloc_Allocated = Class(name="MARTE_Alloc_Allocated")
Alloc_MARTE_NamedElement = Class(name="Alloc_MARTE_NamedElement")
CoreElements_Mode = Class(name="CoreElements_Mode")
MARTE_NFPs_NfpType = Class(name="MARTE_NFPs_NfpType")
TupleType = Class(name="TupleType")
Alloc_MARTE_Dependency = Class(name="Alloc_MARTE_Dependency")
MARTE_Alloc_AllocateActivityGroup = Class(name="MARTE_Alloc_AllocateActivityGroup")
Alloc_MARTE_ActivityPartition = Class(name="Alloc_MARTE_ActivityPartition")
Alloc_Allocated = Class(name="Alloc_Allocated")
MARTE_Alloc_NfpRefine = Class(name="MARTE_Alloc_NfpRefine")
MARTE_Alloc_Allocate = Class(name="MARTE_Alloc_Allocate")
NFPs_NfpConstraint = Class(name="NFPs_NfpConstraint")
MARTE_Alloc_Assign = Class(name="MARTE_Alloc_Assign")
Alloc_MARTE_Element = Class(name="Alloc_MARTE_Element")
Alloc_MARTE_Comment = Class(name="Alloc_MARTE_Comment")
Time_MARTE_Enumeration = Class(name="Time_MARTE_Enumeration")
Alloc_MARTE_Abstraction = Class(name="Alloc_MARTE_Abstraction")
MARTE_Time_TimedDomain = Class(name="MARTE_Time_TimedDomain")
Time_MARTE_Namespace = Class(name="Time_MARTE_Namespace")
MARTE_Time_Clock = Class(name="MARTE_Time_Clock")
Time_MARTE_InstanceSpecification = Class(name="Time_MARTE_InstanceSpecification")
Time_ClockType = Class(name="Time_ClockType")
Time_MARTE_Property = Class(name="Time_MARTE_Property")
Time_MARTE_Event = Class(name="Time_MARTE_Event")
MARTE_Time_ClockType = Class(name="MARTE_Time_ClockType")
Time_MARTE_Operation = Class(name="Time_MARTE_Operation")
Time_MARTE_Class = Class(name="Time_MARTE_Class")
MARTE_Time_TimedElement = Class(name="MARTE_Time_TimedElement", is_abstract=True)
Time_Clock = Class(name="Time_Clock")
MARTE_Time_TimedValueSpecification = Class(name="MARTE_Time_TimedValueSpecification")
TimedElement = Class(name="TimedElement")
Time_MARTE_ValueSpecification = Class(name="Time_MARTE_ValueSpecification")
MARTE_Time_TimedConstraint = Class(name="MARTE_Time_TimedConstraint")
Time_TimedElement = Class(name="Time_TimedElement")
MARTE_Time_ClockConstraint = Class(name="MARTE_Time_ClockConstraint")
MARTE_Time_TimedInstantObservation = Class(name="MARTE_Time_TimedInstantObservation")
Time_MARTE_TimeObservation = Class(name="Time_MARTE_TimeObservation")
MARTE_Time_TimedDurationObservation = Class(name="MARTE_Time_TimedDurationObservation")
Time_MARTE_DurationObservation = Class(name="Time_MARTE_DurationObservation")
MARTE_Time_TimedEvent = Class(name="MARTE_Time_TimedEvent")
Time_MARTE_TimeEvent = Class(name="Time_MARTE_TimeEvent")
MARTE_Time_TimedProcessing = Class(name="MARTE_Time_TimedProcessing")
Time_MARTE_Action = Class(name="Time_MARTE_Action")
GRM_MARTE_ConnectableElement = Class(name="GRM_MARTE_ConnectableElement")
Time_MARTE_Behavior = Class(name="Time_MARTE_Behavior")
Time_MARTE_Message = Class(name="Time_MARTE_Message")
MARTE_GRM_Resource = Class(name="MARTE_GRM_Resource")
GRM_MARTE_Property = Class(name="GRM_MARTE_Property")
GRM_MARTE_InstanceSpecification = Class(name="GRM_MARTE_InstanceSpecification")
GRM_MARTE_Classifier = Class(name="GRM_MARTE_Classifier")
GRM_MARTE_Lifeline = Class(name="GRM_MARTE_Lifeline")
MARTE_GRM_StorageResource = Class(name="MARTE_GRM_StorageResource")
Resource = Class(name="Resource")
MARTE_GRM_CommunicationEndPoint = Class(name="MARTE_GRM_CommunicationEndPoint")
MARTE_GRM_SynchronizationResource = Class(name="MARTE_GRM_SynchronizationResource")
MARTE_GRM_ConcurrencyResource = Class(name="MARTE_GRM_ConcurrencyResource")
MARTE_GRM_Scheduler = Class(name="MARTE_GRM_Scheduler")
GRM_ProcessingResource = Class(name="GRM_ProcessingResource")
GRM_ComputingResource = Class(name="GRM_ComputingResource")
GRM_MutualExclusionResource = Class(name="GRM_MutualExclusionResource")
GRM_SchedulableResource = Class(name="GRM_SchedulableResource")
MARTE_GRM_ProcessingResource = Class(name="MARTE_GRM_ProcessingResource")
GRM_Scheduler = Class(name="GRM_Scheduler")
MARTE_GRM_ComputingResource = Class(name="MARTE_GRM_ComputingResource")
ProcessingResource = Class(name="ProcessingResource")
MARTE_GRM_MutualExclusionResource = Class(name="MARTE_GRM_MutualExclusionResource")
MARTE_GRM_SchedulableResource = Class(name="MARTE_GRM_SchedulableResource")
GRM_SecondaryScheduler = Class(name="GRM_SecondaryScheduler")
MARTE_GRM_SecondaryScheduler = Class(name="MARTE_GRM_SecondaryScheduler")
Scheduler = Class(name="Scheduler")
MARTE_GRM_CommunicationMedia = Class(name="MARTE_GRM_CommunicationMedia")
GRM_MARTE_Connector = Class(name="GRM_MARTE_Connector")
MARTE_GRM_ResourceUsage = Class(name="MARTE_GRM_ResourceUsage")
MARTE_GRM_DeviceResource = Class(name="MARTE_GRM_DeviceResource")
MARTE_GRM_TimingResource = Class(name="MARTE_GRM_TimingResource")
MARTE_GRM_ClockResource = Class(name="MARTE_GRM_ClockResource")
TimingResource = Class(name="TimingResource")
MARTE_GRM_TimerResource = Class(name="MARTE_GRM_TimerResource")
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
RSM_MARTE_ConnectorEnd = Class(name="RSM_MARTE_ConnectorEnd")
GRM_MARTE_NamedElement = Class(name="GRM_MARTE_NamedElement")
GRM_ResourceUsage = Class(name="GRM_ResourceUsage")
MARTE_RSM_LinkTopology = Class(name="MARTE_RSM_LinkTopology", is_abstract=True)
RSM_MARTE_Connector = Class(name="RSM_MARTE_Connector")
MARTE_RSM_DefaultLink = Class(name="MARTE_RSM_DefaultLink")
LinkTopology = Class(name="LinkTopology")
MARTE_RSM_InterRepetition = Class(name="MARTE_RSM_InterRepetition")
MARTE_RSM_Distribute = Class(name="MARTE_RSM_Distribute")
Allocate = Class(name="Allocate")
MARTE_RSM_Reshape = Class(name="MARTE_RSM_Reshape")
MARTE_RSM_Tiler = Class(name="MARTE_RSM_Tiler")
DataTypes_MARTE_Property = Class(name="DataTypes_MARTE_Property")
MARTE_RSM_Shaped = Class(name="MARTE_RSM_Shaped")
RSM_MARTE_MultiplicityElement = Class(name="RSM_MARTE_MultiplicityElement")
MARTE_Variables_Var = Class(name="MARTE_Variables_Var")
Variables_MARTE_Property = Class(name="Variables_MARTE_Property")
MARTE_Variables_ExpressionContext = Class(name="MARTE_Variables_ExpressionContext")
Variables_MARTE_NamedElement = Class(name="Variables_MARTE_NamedElement")
MARTE_Operators_Operator = Class(name="MARTE_Operators_Operator")
Operators_MARTE_Behavior = Class(name="Operators_MARTE_Behavior")
MARTE_DataTypes_BoundedSubtype = Class(name="MARTE_DataTypes_BoundedSubtype")
DataTypes_MARTE_DataType = Class(name="DataTypes_MARTE_DataType")
MARTE_DataTypes_IntervalType = Class(name="MARTE_DataTypes_IntervalType")
HLAM_MARTE_BehavioredClassifier = Class(name="HLAM_MARTE_BehavioredClassifier")
MARTE_DataTypes_CollectionType = Class(name="MARTE_DataTypes_CollectionType")
MARTE_DataTypes_ChoiceType = Class(name="MARTE_DataTypes_ChoiceType")
MARTE_DataTypes_TupleType = Class(name="MARTE_DataTypes_TupleType")
MARTE_HLAM_RtUnit = Class(name="MARTE_HLAM_RtUnit")
HLAM_MARTE_Behavior = Class(name="HLAM_MARTE_Behavior")
HLAM_MARTE_Operation = Class(name="HLAM_MARTE_Operation")
MARTE_HLAM_PpUnit = Class(name="MARTE_HLAM_PpUnit")
MARTE_HLAM_RtFeature = Class(name="MARTE_HLAM_RtFeature")
HLAM_MARTE_BehavioralFeature = Class(name="HLAM_MARTE_BehavioralFeature")
HLAM_MARTE_Message = Class(name="HLAM_MARTE_Message")
HLAM_MARTE_Signal = Class(name="HLAM_MARTE_Signal")
HLAM_MARTE_Port = Class(name="HLAM_MARTE_Port")
HLAM_MARTE_InvocationAction = Class(name="HLAM_MARTE_InvocationAction")
HLAM_RtSpecification = Class(name="HLAM_RtSpecification")
MARTE_HLAM_RtSpecification = Class(name="MARTE_HLAM_RtSpecification")
Time_TimedInstantObservation = Class(name="Time_TimedInstantObservation")
HLAM_MARTE_Comment = Class(name="HLAM_MARTE_Comment")
MARTE_HLAM_RtAction = Class(name="MARTE_HLAM_RtAction")
MARTE_HLAM_RtService = Class(name="MARTE_HLAM_RtService")
HwStorageManager_HwMMU = Class(name="HwStorageManager_HwMMU")
MARTE_HwComputing_HwProcessor = Class(name="MARTE_HwComputing_HwProcessor")
HwComputingResource = Class(name="HwComputingResource")
HwComputing_HwISA = Class(name="HwComputing_HwISA")
HwComputing_HwBranchPredictor = Class(name="HwComputing_HwBranchPredictor")
HwMemory_HwCache = Class(name="HwMemory_HwCache")
MARTE_HwCommunication_HwArbiter = Class(name="MARTE_HwCommunication_HwArbiter")
HwCommunicationResource = Class(name="HwCommunicationResource")
HwCommunication_HwMedia = Class(name="HwCommunication_HwMedia")
MARTE_HwComputing_HwComputingResource = Class(name="MARTE_HwComputing_HwComputingResource")
HwGeneral_HwResource = Class(name="HwGeneral_HwResource")
MARTE_HwComputing_HwISA = Class(name="MARTE_HwComputing_HwISA")
HwResource = Class(name="HwResource")
MARTE_HwComputing_HwBranchPredictor = Class(name="MARTE_HwComputing_HwBranchPredictor")
MARTE_HwComputing_HwASIC = Class(name="MARTE_HwComputing_HwASIC")
MARTE_HwComputing_HwPLD = Class(name="MARTE_HwComputing_HwPLD")
HwMemory_HwRAM = Class(name="HwMemory_HwRAM")
HwComputing_HwComputingResource = Class(name="HwComputing_HwComputingResource")
MARTE_HwCommunication_HwCommunicationResource = Class(name="MARTE_HwCommunication_HwCommunicationResource")
MARTE_HwStorageManager_HwMMU = Class(name="MARTE_HwStorageManager_HwMMU")
HwStorageManager = Class(name="HwStorageManager")
MARTE_HwCommunication_HwMedia = Class(name="MARTE_HwCommunication_HwMedia")
GRM_CommunicationMedia = Class(name="GRM_CommunicationMedia")
HwCommunication_HwCommunicationResource = Class(name="HwCommunication_HwCommunicationResource")
HwCommunication_HwArbiter = Class(name="HwCommunication_HwArbiter")
MARTE_HwCommunication_HwBus = Class(name="MARTE_HwCommunication_HwBus")
HwMedia = Class(name="HwMedia")
MARTE_HwCommunication_HwBridge = Class(name="MARTE_HwCommunication_HwBridge")
MARTE_HwCommunication_HwEndPoint = Class(name="MARTE_HwCommunication_HwEndPoint")
GRM_CommunicationEndPoint = Class(name="GRM_CommunicationEndPoint")
MARTE_HwStorageManager_HwStorageManager = Class(name="MARTE_HwStorageManager_HwStorageManager")
GRM_StorageResource = Class(name="GRM_StorageResource")
HwMemory_HwMemory = Class(name="HwMemory_HwMemory")
MARTE_HwStorageManager_HwDMA = Class(name="MARTE_HwStorageManager_HwDMA")
HwStorageManager_HwStorageManager = Class(name="HwStorageManager_HwStorageManager")
HwComputing_HwProcessor = Class(name="HwComputing_HwProcessor")
MARTE_HwMemory_HwMemory = Class(name="MARTE_HwMemory_HwMemory")
MARTE_HwMemory_HwRAM = Class(name="MARTE_HwMemory_HwRAM")
HwMemory = Class(name="HwMemory")
GRM_DeviceResource = Class(name="GRM_DeviceResource")
MARTE_HwDevice_HwI_O = Class(name="MARTE_HwDevice_HwI_O")
HwDevice = Class(name="HwDevice")
MARTE_HwDevice_HwSupport = Class(name="MARTE_HwDevice_HwSupport")
MARTE_HwMemory_HwROM = Class(name="MARTE_HwMemory_HwROM")
MARTE_HwMemory_HwDrive = Class(name="MARTE_HwMemory_HwDrive")
MARTE_HwMemory_HwCache = Class(name="MARTE_HwMemory_HwCache")
MARTE_HwTiming_HwTimingResource = Class(name="MARTE_HwTiming_HwTimingResource")
GRM_TimingResource = Class(name="GRM_TimingResource")
MARTE_HwTiming_HwClock = Class(name="MARTE_HwTiming_HwClock")
HwTimingResource = Class(name="HwTimingResource")
MARTE_HwTiming_HwTimer = Class(name="MARTE_HwTiming_HwTimer")
HwTiming_HwClock = Class(name="HwTiming_HwClock")
MARTE_HwDevice_HwDevice = Class(name="MARTE_HwDevice_HwDevice")
MARTE_HwDevice_HWActuator = Class(name="MARTE_HwDevice_HWActuator")
HwI_O = Class(name="HwI_O")
MARTE_HwDevice_HWSensor = Class(name="MARTE_HwDevice_HWSensor")
MARTE_HwGeneral_HwResourceService = Class(name="MARTE_HwGeneral_HwResourceService")
MARTE_HwGeneral_HwResource = Class(name="MARTE_HwGeneral_HwResource")
HwGeneral_HwResourceService = Class(name="HwGeneral_HwResourceService")
HwCommunication_HwEndPoint = Class(name="HwCommunication_HwEndPoint")
MARTE_HwLayout_HwComponent = Class(name="MARTE_HwLayout_HwComponent")
MARTE_SW_ResourceCore_SwResource = Class(name="MARTE_SW_ResourceCore_SwResource", is_abstract=True)
HwLayout_HwComponent = Class(name="HwLayout_HwComponent")
MARTE_HwPower_HwPowerSupply = Class(name="MARTE_HwPower_HwPowerSupply")
HwComponent = Class(name="HwComponent")
MARTE_HwPower_HwCoolingSupply = Class(name="MARTE_HwPower_HwCoolingSupply")
SW_Concurrency_MARTE_TypedElement = Class(name="SW_Concurrency_MARTE_TypedElement")
SW_ResourceCore_MARTE_TypedElement = Class(name="SW_ResourceCore_MARTE_TypedElement")
SW_ResourceCore_MARTE_BehavioralFeature = Class(name="SW_ResourceCore_MARTE_BehavioralFeature")
MARTE_SW_ResourceCore_SwAccessService = Class(name="MARTE_SW_ResourceCore_SwAccessService")
SW_ResourceCore_MARTE_Property = Class(name="SW_ResourceCore_MARTE_Property")
MARTE_SW_Concurrency_EntryPoint = Class(name="MARTE_SW_Concurrency_EntryPoint")
SW_Concurrency_MARTE_BehavioralFeature = Class(name="SW_Concurrency_MARTE_BehavioralFeature")
MARTE_SW_Concurrency_SwConcurrentResource = Class(name="MARTE_SW_Concurrency_SwConcurrentResource", is_abstract=True)
SwResource = Class(name="SwResource")
SW_Concurrency_MARTE_Element = Class(name="SW_Concurrency_MARTE_Element")
MARTE_SW_Concurrency_InterruptResource = Class(name="MARTE_SW_Concurrency_InterruptResource")
SwConcurrentResource = Class(name="SwConcurrentResource")
MARTE_SW_Concurrency_MemoryPartition = Class(name="MARTE_SW_Concurrency_MemoryPartition")
MARTE_SW_Concurrency_SwSchedulableResource = Class(name="MARTE_SW_Concurrency_SwSchedulableResource")
SW_Concurrency_SwConcurrentResource = Class(name="SW_Concurrency_SwConcurrentResource")
SW_Concurrency_MARTE_NamedElement = Class(name="SW_Concurrency_MARTE_NamedElement")
MARTE_SW_Concurrency_SwTimerResource = Class(name="MARTE_SW_Concurrency_SwTimerResource")
TimerResource = Class(name="TimerResource")
SW_Concurrency_MARTE_Namespace = Class(name="SW_Concurrency_MARTE_Namespace")
MARTE_SW_Concurrency_Alarm = Class(name="MARTE_SW_Concurrency_Alarm")
InterruptResource = Class(name="InterruptResource")
MARTE_SW_Brokering_DeviceBroker = Class(name="MARTE_SW_Brokering_DeviceBroker")
SW_Brokering_MARTE_TypedElement = Class(name="SW_Brokering_MARTE_TypedElement")
SW_Brokering_MARTE_BehavioralFeature = Class(name="SW_Brokering_MARTE_BehavioralFeature")
MARTE_SW_Brokering_MemoryBroker = Class(name="MARTE_SW_Brokering_MemoryBroker")
MARTE_SW_Interaction_SwInteractionResource = Class(name="MARTE_SW_Interaction_SwInteractionResource", is_abstract=True)
SW_Interaction_MARTE_TypedElement = Class(name="SW_Interaction_MARTE_TypedElement")
MARTE_SW_Interaction_SwCommunicationResource = Class(name="MARTE_SW_Interaction_SwCommunicationResource", is_abstract=True)
SW_Interaction_SwInteractionResource = Class(name="SW_Interaction_SwInteractionResource")
MARTE_SW_Interaction_SwSynchronizationResource = Class(name="MARTE_SW_Interaction_SwSynchronizationResource", is_abstract=True)
GRM_SynchronizationResource = Class(name="GRM_SynchronizationResource")
MARTE_SW_Interaction_SharedDataComResource = Class(name="MARTE_SW_Interaction_SharedDataComResource")
SwCommunicationResource = Class(name="SwCommunicationResource")
SW_Interaction_MARTE_BehavioralFeature = Class(name="SW_Interaction_MARTE_BehavioralFeature")
MARTE_SW_Interaction_MessageComResource = Class(name="MARTE_SW_Interaction_MessageComResource")
GCM_MARTE_Property = Class(name="GCM_MARTE_Property")
MARTE_SW_Interaction_NotificationResource = Class(name="MARTE_SW_Interaction_NotificationResource")
SwSynchronizationResource = Class(name="SwSynchronizationResource")
MARTE_SW_Interaction_SwMutualExclusionResource = Class(name="MARTE_SW_Interaction_SwMutualExclusionResource")
SW_Interaction_SwSynchronizationResource = Class(name="SW_Interaction_SwSynchronizationResource")
MARTE_GCM_FlowProperty = Class(name="MARTE_GCM_FlowProperty")
MARTE_GCM_GCMTrigger = Class(name="MARTE_GCM_GCMTrigger")
GCM_MARTE_Trigger = Class(name="GCM_MARTE_Trigger")
MARTE_GCM_FlowPort = Class(name="MARTE_GCM_FlowPort")
GCM_MARTE_Port = Class(name="GCM_MARTE_Port")
MARTE_GCM_ClientServerPort = Class(name="MARTE_GCM_ClientServerPort")
GCM_MARTE_Interface = Class(name="GCM_MARTE_Interface")
GCM_ClientServerSpecification = Class(name="GCM_ClientServerSpecification")
MARTE_GCM_ClientServerSpecification = Class(name="MARTE_GCM_ClientServerSpecification")
MARTE_GCM_FlowSpecification = Class(name="MARTE_GCM_FlowSpecification")
MARTE_GCM_ClientServerFeature = Class(name="MARTE_GCM_ClientServerFeature")
GCM_MARTE_BehavioralFeature = Class(name="GCM_MARTE_BehavioralFeature")
GQAM_MARTE_Behavior = Class(name="GQAM_MARTE_Behavior")
MARTE_GQAM_GaEventTrace = Class(name="MARTE_GQAM_GaEventTrace")
GCM_MARTE_Feature = Class(name="GCM_MARTE_Feature")
MARTE_GCM_GCMInvocationAction = Class(name="MARTE_GCM_GCMInvocationAction")
GCM_MARTE_InvocationAction = Class(name="GCM_MARTE_InvocationAction")
MARTE_GCM_DataEvent = Class(name="MARTE_GCM_DataEvent")
GCM_MARTE_AnyReceiveEvent = Class(name="GCM_MARTE_AnyReceiveEvent")
GCM_MARTE_Classifier = Class(name="GCM_MARTE_Classifier")
MARTE_GCM_DataPool = Class(name="MARTE_GCM_DataPool")
GCM_MARTE_Behavior = Class(name="GCM_MARTE_Behavior")
MARTE_GCM_GCMInvocatingBehavior = Class(name="MARTE_GCM_GCMInvocatingBehavior")
MARTE_GQAM_GaWorkloadGenerator = Class(name="MARTE_GQAM_GaWorkloadGenerator")
GQAM_GaStep = Class(name="GQAM_GaStep")
GQAM_MARTE_NamedElement = Class(name="GQAM_MARTE_NamedElement")
MARTE_GQAM_GaWorkloadEvent = Class(name="MARTE_GQAM_GaWorkloadEvent")
GQAM_GaWorkloadGenerator = Class(name="GQAM_GaWorkloadGenerator")
GQAM_GaEventTrace = Class(name="GQAM_GaEventTrace")
GQAM_GaScenario = Class(name="GQAM_GaScenario")
GQAM_MARTE_TimeEvent = Class(name="GQAM_MARTE_TimeEvent")
MARTE_GQAM_GaScenario = Class(name="MARTE_GQAM_GaScenario")
Time_TimedProcessing = Class(name="Time_TimedProcessing")
GQAM_GaWorkloadEvent = Class(name="GQAM_GaWorkloadEvent")
GQAM_GaRequestedService = Class(name="GQAM_GaRequestedService")
GQAM_GaTimedObs = Class(name="GQAM_GaTimedObs")
MARTE_GQAM_GaStep = Class(name="MARTE_GQAM_GaStep")
GaScenario = Class(name="GaScenario")
GQAM_GaExecHost = Class(name="GQAM_GaExecHost")
MARTE_GQAM_GaExecHost = Class(name="MARTE_GQAM_GaExecHost")
MARTE_GQAM_GaRequestedService = Class(name="MARTE_GQAM_GaRequestedService")
GaStep = Class(name="GaStep")
GQAM_MARTE_Operation = Class(name="GQAM_MARTE_Operation")
MARTE_GQAM_GaTimedObs = Class(name="MARTE_GQAM_GaTimedObs")
NfpConstraint = Class(name="NfpConstraint")
GQAM_MARTE_TimeObservation = Class(name="GQAM_MARTE_TimeObservation")
MARTE_GQAM_GaCommStep = Class(name="MARTE_GQAM_GaCommStep")
MARTE_GQAM_GaAcqStep = Class(name="MARTE_GQAM_GaAcqStep")
MARTE_GQAM_GaRelStep = Class(name="MARTE_GQAM_GaRelStep")
MARTE_GQAM_GaLatencyObs = Class(name="MARTE_GQAM_GaLatencyObs")
GaTimedObs = Class(name="GaTimedObs")
MARTE_GQAM_GaCommHost = Class(name="MARTE_GQAM_GaCommHost")
MARTE_GQAM_GaCommChannel = Class(name="MARTE_GQAM_GaCommChannel")
SchedulableResource = Class(name="SchedulableResource")
MARTE_GQAM_GaWorkloadBehavior = Class(name="MARTE_GQAM_GaWorkloadBehavior")
SAM_MARTE_NamedElement = Class(name="SAM_MARTE_NamedElement")
MARTE_SAM_SaCommStep = Class(name="MARTE_SAM_SaCommStep")
GaCommStep = Class(name="GaCommStep")
MARTE_GQAM_GaAnalysisContext = Class(name="MARTE_GQAM_GaAnalysisContext")
CoreElements_Configuration = Class(name="CoreElements_Configuration")
Variables_ExpressionContext = Class(name="Variables_ExpressionContext")
GQAM_GaWorkloadBehavior = Class(name="GQAM_GaWorkloadBehavior")
GQAM_GaResourcesPlatform = Class(name="GQAM_GaResourcesPlatform")
MARTE_GQAM_GaResourcesPlatform = Class(name="MARTE_GQAM_GaResourcesPlatform")
GQAM_MARTE_Classifier = Class(name="GQAM_MARTE_Classifier")
MARTE_SAM_SaAnalysisContext = Class(name="MARTE_SAM_SaAnalysisContext")
GaAnalysisContext = Class(name="GaAnalysisContext")
MARTE_SAM_SaEndtoEndFlow = Class(name="MARTE_SAM_SaEndtoEndFlow")
MARTE_SAM_SaSchedObs = Class(name="MARTE_SAM_SaSchedObs")
SAM_MARTE_BehavioralFeature = Class(name="SAM_MARTE_BehavioralFeature")
MARTE_SAM_SaStep = Class(name="MARTE_SAM_SaStep")
SAM_SaSharedResource = Class(name="SAM_SaSharedResource")
MARTE_SAM_SaSharedResource = Class(name="MARTE_SAM_SaSharedResource")
MutualExclusionResource = Class(name="MutualExclusionResource")
MARTE_SAM_SaCommHost = Class(name="MARTE_SAM_SaCommHost")
GaCommHost = Class(name="GaCommHost")
MARTE_SAM_SaExecHost = Class(name="MARTE_SAM_SaExecHost")
GaExecHost = Class(name="GaExecHost")
MARTE_PAM_PaStep = Class(name="MARTE_PAM_PaStep")
MARTE_PAM_PaLogicalResource = Class(name="MARTE_PAM_PaLogicalResource")
MARTE_PAM_PaRunTInstance = Class(name="MARTE_PAM_PaRunTInstance")
PAM_MARTE_NamedElement = Class(name="PAM_MARTE_NamedElement")
MARTE_PAM_PaRequestedStep = Class(name="MARTE_PAM_PaRequestedStep")
PAM_PaStep = Class(name="PAM_PaStep")
MARTE_PAM_PaCommStep = Class(name="MARTE_PAM_PaCommStep")
GQAM_GaCommStep = Class(name="GQAM_GaCommStep")
MARTE_PAM_PaResPassStep = Class(name="MARTE_PAM_PaResPassStep")

# MARTE_NFPs_Nfp class attributes and methods

# NFPs_MARTE_Property class attributes and methods

# MARTE_NFPs_Unit class attributes and methods
MARTE_NFPs_Unit_convFactor: Property = Property(name="convFactor", type=StringType)
MARTE_NFPs_Unit_convOffset: Property = Property(name="convOffset", type=StringType)
MARTE_NFPs_Unit.attributes={MARTE_NFPs_Unit_convFactor, MARTE_NFPs_Unit_convOffset}

# NFPs_Unit class attributes and methods

# NFPs_MARTE_EnumerationLiteral class attributes and methods

# MARTE_NFPs_NfpConstraint class attributes and methods
MARTE_NFPs_NfpConstraint_kind: Property = Property(name="kind", type=StringType)
MARTE_NFPs_NfpConstraint.attributes={MARTE_NFPs_NfpConstraint_kind}

# NFPs_MARTE_Constraint class attributes and methods

# MARTE_NFPs_Dimension class attributes and methods
MARTE_NFPs_Dimension_symbol: Property = Property(name="symbol", type=StringType)
MARTE_NFPs_Dimension_baseExponent: Property = Property(name="baseExponent", type=IntegerType)
MARTE_NFPs_Dimension.attributes={MARTE_NFPs_Dimension_symbol, MARTE_NFPs_Dimension_baseExponent}

# NFPs_Dimension class attributes and methods

# NFPs_MARTE_Enumeration class attributes and methods

# MARTE_CoreElements_ModeTransition class attributes and methods

# CoreElements_MARTE_Transition class attributes and methods

# MARTE_CoreElements_ModeBehavior class attributes and methods

# CoreElements_MARTE_StateMachine class attributes and methods

# MARTE_CoreElements_Configuration class attributes and methods

# CoreElements_MARTE_StructuredClassifier class attributes and methods

# CoreElements_MARTE_Package class attributes and methods

# MARTE_CoreElements_Mode class attributes and methods

# CoreElements_MARTE_State class attributes and methods

# MARTE_Alloc_Allocated class attributes and methods
MARTE_Alloc_Allocated_kind: Property = Property(name="kind", type=StringType)
MARTE_Alloc_Allocated.attributes={MARTE_Alloc_Allocated_kind}

# Alloc_MARTE_NamedElement class attributes and methods

# CoreElements_Mode class attributes and methods

# MARTE_NFPs_NfpType class attributes and methods

# TupleType class attributes and methods

# Alloc_MARTE_Dependency class attributes and methods

# MARTE_Alloc_AllocateActivityGroup class attributes and methods
MARTE_Alloc_AllocateActivityGroup_isUnique: Property = Property(name="isUnique", type=StringType)
MARTE_Alloc_AllocateActivityGroup.attributes={MARTE_Alloc_AllocateActivityGroup_isUnique}

# Alloc_MARTE_ActivityPartition class attributes and methods

# Alloc_Allocated class attributes and methods

# MARTE_Alloc_NfpRefine class attributes and methods

# MARTE_Alloc_Allocate class attributes and methods
MARTE_Alloc_Allocate_kind: Property = Property(name="kind", type=StringType)
MARTE_Alloc_Allocate_nature: Property = Property(name="nature", type=StringType)
MARTE_Alloc_Allocate.attributes={MARTE_Alloc_Allocate_nature, MARTE_Alloc_Allocate_kind}

# NFPs_NfpConstraint class attributes and methods

# MARTE_Alloc_Assign class attributes and methods
MARTE_Alloc_Assign_kind: Property = Property(name="kind", type=StringType)
MARTE_Alloc_Assign_nature: Property = Property(name="nature", type=StringType)
MARTE_Alloc_Assign.attributes={MARTE_Alloc_Assign_nature, MARTE_Alloc_Assign_kind}

# Alloc_MARTE_Element class attributes and methods

# Alloc_MARTE_Comment class attributes and methods

# Time_MARTE_Enumeration class attributes and methods

# Alloc_MARTE_Abstraction class attributes and methods

# MARTE_Time_TimedDomain class attributes and methods

# Time_MARTE_Namespace class attributes and methods

# MARTE_Time_Clock class attributes and methods
MARTE_Time_Clock_standard: Property = Property(name="standard", type=StringType)
MARTE_Time_Clock.attributes={MARTE_Time_Clock_standard}

# Time_MARTE_InstanceSpecification class attributes and methods

# Time_ClockType class attributes and methods

# Time_MARTE_Property class attributes and methods

# Time_MARTE_Event class attributes and methods

# MARTE_Time_ClockType class attributes and methods
MARTE_Time_ClockType_nature: Property = Property(name="nature", type=StringType)
MARTE_Time_ClockType_isLogical: Property = Property(name="isLogical", type=StringType)
MARTE_Time_ClockType.attributes={MARTE_Time_ClockType_nature, MARTE_Time_ClockType_isLogical}

# Time_MARTE_Operation class attributes and methods

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
MARTE_Time_ClockConstraint.attributes={MARTE_Time_ClockConstraint_isCoincidenceBased, MARTE_Time_ClockConstraint_isChronometricBased, MARTE_Time_ClockConstraint_isPrecedenceBased}

# MARTE_Time_TimedInstantObservation class attributes and methods
MARTE_Time_TimedInstantObservation_obsKind: Property = Property(name="obsKind", type=StringType)
MARTE_Time_TimedInstantObservation.attributes={MARTE_Time_TimedInstantObservation_obsKind}

# Time_MARTE_TimeObservation class attributes and methods

# MARTE_Time_TimedDurationObservation class attributes and methods
MARTE_Time_TimedDurationObservation_obsKind: Property = Property(name="obsKind", type=StringType)
MARTE_Time_TimedDurationObservation.attributes={MARTE_Time_TimedDurationObservation_obsKind}

# Time_MARTE_DurationObservation class attributes and methods

# MARTE_Time_TimedEvent class attributes and methods
MARTE_Time_TimedEvent_repetition: Property = Property(name="repetition", type=StringType)
MARTE_Time_TimedEvent.attributes={MARTE_Time_TimedEvent_repetition}

# Time_MARTE_TimeEvent class attributes and methods

# MARTE_Time_TimedProcessing class attributes and methods

# Time_MARTE_Action class attributes and methods

# GRM_MARTE_ConnectableElement class attributes and methods

# Time_MARTE_Behavior class attributes and methods

# Time_MARTE_Message class attributes and methods

# MARTE_GRM_Resource class attributes and methods
MARTE_GRM_Resource_resMult: Property = Property(name="resMult", type=StringType)
MARTE_GRM_Resource_isProtected: Property = Property(name="isProtected", type=StringType)
MARTE_GRM_Resource_isActive: Property = Property(name="isActive", type=StringType)
MARTE_GRM_Resource.attributes={MARTE_GRM_Resource_isActive, MARTE_GRM_Resource_resMult, MARTE_GRM_Resource_isProtected}

# GRM_MARTE_Property class attributes and methods

# GRM_MARTE_InstanceSpecification class attributes and methods

# GRM_MARTE_Classifier class attributes and methods

# GRM_MARTE_Lifeline class attributes and methods

# MARTE_GRM_StorageResource class attributes and methods
MARTE_GRM_StorageResource_elementSize: Property = Property(name="elementSize", type=StringType)
MARTE_GRM_StorageResource.attributes={MARTE_GRM_StorageResource_elementSize}

# Resource class attributes and methods

# MARTE_GRM_CommunicationEndPoint class attributes and methods
MARTE_GRM_CommunicationEndPoint_packetSize: Property = Property(name="packetSize", type=StringType)
MARTE_GRM_CommunicationEndPoint.attributes={MARTE_GRM_CommunicationEndPoint_packetSize}

# MARTE_GRM_SynchronizationResource class attributes and methods

# MARTE_GRM_ConcurrencyResource class attributes and methods

# MARTE_GRM_Scheduler class attributes and methods
MARTE_GRM_Scheduler_isPreemptible: Property = Property(name="isPreemptible", type=StringType)
MARTE_GRM_Scheduler_schedPolicy: Property = Property(name="schedPolicy", type=StringType)
MARTE_GRM_Scheduler_otherSchedPolicy: Property = Property(name="otherSchedPolicy", type=StringType)
MARTE_GRM_Scheduler_schedule: Property = Property(name="schedule", type=StringType)
MARTE_GRM_Scheduler.attributes={MARTE_GRM_Scheduler_isPreemptible, MARTE_GRM_Scheduler_schedule, MARTE_GRM_Scheduler_otherSchedPolicy, MARTE_GRM_Scheduler_schedPolicy}

# GRM_ProcessingResource class attributes and methods

# GRM_ComputingResource class attributes and methods

# GRM_MutualExclusionResource class attributes and methods

# GRM_SchedulableResource class attributes and methods

# MARTE_GRM_ProcessingResource class attributes and methods
MARTE_GRM_ProcessingResource_speedFactor: Property = Property(name="speedFactor", type=StringType)
MARTE_GRM_ProcessingResource.attributes={MARTE_GRM_ProcessingResource_speedFactor}

# GRM_Scheduler class attributes and methods

# MARTE_GRM_ComputingResource class attributes and methods

# ProcessingResource class attributes and methods

# MARTE_GRM_MutualExclusionResource class attributes and methods
MARTE_GRM_MutualExclusionResource_protectKind: Property = Property(name="protectKind", type=StringType)
MARTE_GRM_MutualExclusionResource_ceiling: Property = Property(name="ceiling", type=StringType)
MARTE_GRM_MutualExclusionResource_otherProtectProtocol: Property = Property(name="otherProtectProtocol", type=StringType)
MARTE_GRM_MutualExclusionResource.attributes={MARTE_GRM_MutualExclusionResource_ceiling, MARTE_GRM_MutualExclusionResource_protectKind, MARTE_GRM_MutualExclusionResource_otherProtectProtocol}

# MARTE_GRM_SchedulableResource class attributes and methods
MARTE_GRM_SchedulableResource_schedParams: Property = Property(name="schedParams", type=StringType)
MARTE_GRM_SchedulableResource.attributes={MARTE_GRM_SchedulableResource_schedParams}

# GRM_SecondaryScheduler class attributes and methods

# MARTE_GRM_SecondaryScheduler class attributes and methods

# Scheduler class attributes and methods

# MARTE_GRM_CommunicationMedia class attributes and methods
MARTE_GRM_CommunicationMedia_transmMode: Property = Property(name="transmMode", type=StringType)
MARTE_GRM_CommunicationMedia_blockT: Property = Property(name="blockT", type=StringType)
MARTE_GRM_CommunicationMedia_elementSize: Property = Property(name="elementSize", type=StringType)
MARTE_GRM_CommunicationMedia_packetT: Property = Property(name="packetT", type=StringType)
MARTE_GRM_CommunicationMedia_capacity: Property = Property(name="capacity", type=StringType)
MARTE_GRM_CommunicationMedia.attributes={MARTE_GRM_CommunicationMedia_transmMode, MARTE_GRM_CommunicationMedia_capacity, MARTE_GRM_CommunicationMedia_blockT, MARTE_GRM_CommunicationMedia_elementSize, MARTE_GRM_CommunicationMedia_packetT}

# GRM_MARTE_Connector class attributes and methods

# MARTE_GRM_ResourceUsage class attributes and methods
MARTE_GRM_ResourceUsage_execTime: Property = Property(name="execTime", type=StringType)
MARTE_GRM_ResourceUsage_allocatedMemory: Property = Property(name="allocatedMemory", type=StringType)
MARTE_GRM_ResourceUsage_usedMemory: Property = Property(name="usedMemory", type=StringType)
MARTE_GRM_ResourceUsage_powerPeak: Property = Property(name="powerPeak", type=StringType)
MARTE_GRM_ResourceUsage_energy: Property = Property(name="energy", type=StringType)
MARTE_GRM_ResourceUsage_msgSize: Property = Property(name="msgSize", type=StringType)
MARTE_GRM_ResourceUsage.attributes={MARTE_GRM_ResourceUsage_usedMemory, MARTE_GRM_ResourceUsage_allocatedMemory, MARTE_GRM_ResourceUsage_execTime, MARTE_GRM_ResourceUsage_msgSize, MARTE_GRM_ResourceUsage_powerPeak, MARTE_GRM_ResourceUsage_energy}

# MARTE_GRM_DeviceResource class attributes and methods

# MARTE_GRM_TimingResource class attributes and methods

# MARTE_GRM_ClockResource class attributes and methods

# TimingResource class attributes and methods

# MARTE_GRM_TimerResource class attributes and methods
MARTE_GRM_TimerResource_duration: Property = Property(name="duration", type=StringType)
MARTE_GRM_TimerResource_isPeriodic: Property = Property(name="isPeriodic", type=StringType)
MARTE_GRM_TimerResource.attributes={MARTE_GRM_TimerResource_isPeriodic, MARTE_GRM_TimerResource_duration}

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

# RSM_MARTE_ConnectorEnd class attributes and methods

# GRM_MARTE_NamedElement class attributes and methods

# GRM_ResourceUsage class attributes and methods

# MARTE_RSM_LinkTopology class attributes and methods

# RSM_MARTE_Connector class attributes and methods

# MARTE_RSM_DefaultLink class attributes and methods

# LinkTopology class attributes and methods

# MARTE_RSM_InterRepetition class attributes and methods
MARTE_RSM_InterRepetition_repetitionShapeDependence: Property = Property(name="repetitionShapeDependence", type=StringType)
MARTE_RSM_InterRepetition_isModulo: Property = Property(name="isModulo", type=StringType)
MARTE_RSM_InterRepetition.attributes={MARTE_RSM_InterRepetition_repetitionShapeDependence, MARTE_RSM_InterRepetition_isModulo}

# MARTE_RSM_Distribute class attributes and methods
MARTE_RSM_Distribute_patternShape: Property = Property(name="patternShape", type=StringType)
MARTE_RSM_Distribute_repetitionSpace: Property = Property(name="repetitionSpace", type=StringType)
MARTE_RSM_Distribute_fromTiler: Property = Property(name="fromTiler", type=StringType)
MARTE_RSM_Distribute_toTiler: Property = Property(name="toTiler", type=StringType)
MARTE_RSM_Distribute.attributes={MARTE_RSM_Distribute_toTiler, MARTE_RSM_Distribute_patternShape, MARTE_RSM_Distribute_fromTiler, MARTE_RSM_Distribute_repetitionSpace}

# Allocate class attributes and methods

# MARTE_RSM_Reshape class attributes and methods
MARTE_RSM_Reshape_patternShape: Property = Property(name="patternShape", type=StringType)
MARTE_RSM_Reshape_repetitonShape: Property = Property(name="repetitonShape", type=StringType)
MARTE_RSM_Reshape.attributes={MARTE_RSM_Reshape_repetitonShape, MARTE_RSM_Reshape_patternShape}

# MARTE_RSM_Tiler class attributes and methods
MARTE_RSM_Tiler_fitting: Property = Property(name="fitting", type=StringType)
MARTE_RSM_Tiler_tiler: Property = Property(name="tiler", type=StringType)
MARTE_RSM_Tiler_origin: Property = Property(name="origin", type=StringType)
MARTE_RSM_Tiler_paving: Property = Property(name="paving", type=StringType)
MARTE_RSM_Tiler.attributes={MARTE_RSM_Tiler_paving, MARTE_RSM_Tiler_tiler, MARTE_RSM_Tiler_origin, MARTE_RSM_Tiler_fitting}

# DataTypes_MARTE_Property class attributes and methods

# MARTE_RSM_Shaped class attributes and methods
MARTE_RSM_Shaped_shape: Property = Property(name="shape", type=StringType)
MARTE_RSM_Shaped.attributes={MARTE_RSM_Shaped_shape}

# RSM_MARTE_MultiplicityElement class attributes and methods

# MARTE_Variables_Var class attributes and methods
MARTE_Variables_Var_dir: Property = Property(name="dir", type=StringType)
MARTE_Variables_Var.attributes={MARTE_Variables_Var_dir}

# Variables_MARTE_Property class attributes and methods

# MARTE_Variables_ExpressionContext class attributes and methods

# Variables_MARTE_NamedElement class attributes and methods

# MARTE_Operators_Operator class attributes and methods
MARTE_Operators_Operator_symbol: Property = Property(name="symbol", type=StringType)
MARTE_Operators_Operator_arity: Property = Property(name="arity", type=StringType)
MARTE_Operators_Operator.attributes={MARTE_Operators_Operator_arity, MARTE_Operators_Operator_symbol}

# Operators_MARTE_Behavior class attributes and methods

# MARTE_DataTypes_BoundedSubtype class attributes and methods
MARTE_DataTypes_BoundedSubtype_minValue: Property = Property(name="minValue", type=StringType)
MARTE_DataTypes_BoundedSubtype_maxValue: Property = Property(name="maxValue", type=StringType)
MARTE_DataTypes_BoundedSubtype_isMinOpen: Property = Property(name="isMinOpen", type=BooleanType)
MARTE_DataTypes_BoundedSubtype_isMaxOpen: Property = Property(name="isMaxOpen", type=BooleanType)
MARTE_DataTypes_BoundedSubtype.attributes={MARTE_DataTypes_BoundedSubtype_isMinOpen, MARTE_DataTypes_BoundedSubtype_maxValue, MARTE_DataTypes_BoundedSubtype_minValue, MARTE_DataTypes_BoundedSubtype_isMaxOpen}

# DataTypes_MARTE_DataType class attributes and methods

# MARTE_DataTypes_IntervalType class attributes and methods

# HLAM_MARTE_BehavioredClassifier class attributes and methods

# MARTE_DataTypes_CollectionType class attributes and methods

# MARTE_DataTypes_ChoiceType class attributes and methods

# MARTE_DataTypes_TupleType class attributes and methods

# MARTE_HLAM_RtUnit class attributes and methods
MARTE_HLAM_RtUnit_queueSchedPolicy: Property = Property(name="queueSchedPolicy", type=StringType)
MARTE_HLAM_RtUnit_isDynamic: Property = Property(name="isDynamic", type=StringType)
MARTE_HLAM_RtUnit_isMain: Property = Property(name="isMain", type=StringType)
MARTE_HLAM_RtUnit_srPoolSize: Property = Property(name="srPoolSize", type=StringType)
MARTE_HLAM_RtUnit_srPoolPolicy: Property = Property(name="srPoolPolicy", type=StringType)
MARTE_HLAM_RtUnit_srPoolWaitingTime: Property = Property(name="srPoolWaitingTime", type=StringType)
MARTE_HLAM_RtUnit_memorySize: Property = Property(name="memorySize", type=StringType)
MARTE_HLAM_RtUnit_queueSize: Property = Property(name="queueSize", type=StringType)
MARTE_HLAM_RtUnit_msgMaxSize: Property = Property(name="msgMaxSize", type=StringType)
MARTE_HLAM_RtUnit.attributes={MARTE_HLAM_RtUnit_isDynamic, MARTE_HLAM_RtUnit_srPoolSize, MARTE_HLAM_RtUnit_isMain, MARTE_HLAM_RtUnit_srPoolWaitingTime, MARTE_HLAM_RtUnit_srPoolPolicy, MARTE_HLAM_RtUnit_queueSize, MARTE_HLAM_RtUnit_memorySize, MARTE_HLAM_RtUnit_queueSchedPolicy, MARTE_HLAM_RtUnit_msgMaxSize}

# HLAM_MARTE_Behavior class attributes and methods

# HLAM_MARTE_Operation class attributes and methods

# MARTE_HLAM_PpUnit class attributes and methods
MARTE_HLAM_PpUnit_concPolicy: Property = Property(name="concPolicy", type=StringType)
MARTE_HLAM_PpUnit_memorySize: Property = Property(name="memorySize", type=StringType)
MARTE_HLAM_PpUnit.attributes={MARTE_HLAM_PpUnit_memorySize, MARTE_HLAM_PpUnit_concPolicy}

# MARTE_HLAM_RtFeature class attributes and methods

# HLAM_MARTE_BehavioralFeature class attributes and methods

# HLAM_MARTE_Message class attributes and methods

# HLAM_MARTE_Signal class attributes and methods

# HLAM_MARTE_Port class attributes and methods

# HLAM_MARTE_InvocationAction class attributes and methods

# HLAM_RtSpecification class attributes and methods

# MARTE_HLAM_RtSpecification class attributes and methods
MARTE_HLAM_RtSpecification_relDl: Property = Property(name="relDl", type=StringType)
MARTE_HLAM_RtSpecification_absDl: Property = Property(name="absDl", type=StringType)
MARTE_HLAM_RtSpecification_utility: Property = Property(name="utility", type=StringType)
MARTE_HLAM_RtSpecification_occKind: Property = Property(name="occKind", type=StringType)
MARTE_HLAM_RtSpecification_boundDl: Property = Property(name="boundDl", type=StringType)
MARTE_HLAM_RtSpecification_rdTime: Property = Property(name="rdTime", type=StringType)
MARTE_HLAM_RtSpecification_miss: Property = Property(name="miss", type=StringType)
MARTE_HLAM_RtSpecification_priority: Property = Property(name="priority", type=StringType)
MARTE_HLAM_RtSpecification.attributes={MARTE_HLAM_RtSpecification_absDl, MARTE_HLAM_RtSpecification_rdTime, MARTE_HLAM_RtSpecification_miss, MARTE_HLAM_RtSpecification_boundDl, MARTE_HLAM_RtSpecification_utility, MARTE_HLAM_RtSpecification_relDl, MARTE_HLAM_RtSpecification_priority, MARTE_HLAM_RtSpecification_occKind}

# Time_TimedInstantObservation class attributes and methods

# HLAM_MARTE_Comment class attributes and methods

# MARTE_HLAM_RtAction class attributes and methods
MARTE_HLAM_RtAction_isAtomic: Property = Property(name="isAtomic", type=StringType)
MARTE_HLAM_RtAction_synchKind: Property = Property(name="synchKind", type=StringType)
MARTE_HLAM_RtAction_msgSize: Property = Property(name="msgSize", type=StringType)
MARTE_HLAM_RtAction.attributes={MARTE_HLAM_RtAction_msgSize, MARTE_HLAM_RtAction_synchKind, MARTE_HLAM_RtAction_isAtomic}

# MARTE_HLAM_RtService class attributes and methods
MARTE_HLAM_RtService_concPolicy: Property = Property(name="concPolicy", type=StringType)
MARTE_HLAM_RtService_exeKind: Property = Property(name="exeKind", type=StringType)
MARTE_HLAM_RtService_isAtomic: Property = Property(name="isAtomic", type=StringType)
MARTE_HLAM_RtService_synchKind: Property = Property(name="synchKind", type=StringType)
MARTE_HLAM_RtService.attributes={MARTE_HLAM_RtService_concPolicy, MARTE_HLAM_RtService_isAtomic, MARTE_HLAM_RtService_synchKind, MARTE_HLAM_RtService_exeKind}

# HwStorageManager_HwMMU class attributes and methods

# MARTE_HwComputing_HwProcessor class attributes and methods
MARTE_HwComputing_HwProcessor_architecture: Property = Property(name="architecture", type=StringType)
MARTE_HwComputing_HwProcessor_mips: Property = Property(name="mips", type=StringType)
MARTE_HwComputing_HwProcessor_ipc: Property = Property(name="ipc", type=StringType)
MARTE_HwComputing_HwProcessor_nbCores: Property = Property(name="nbCores", type=StringType)
MARTE_HwComputing_HwProcessor_nbPipelines: Property = Property(name="nbPipelines", type=StringType)
MARTE_HwComputing_HwProcessor_nbStages: Property = Property(name="nbStages", type=StringType)
MARTE_HwComputing_HwProcessor_nbALUs: Property = Property(name="nbALUs", type=StringType)
MARTE_HwComputing_HwProcessor_nbFPUs: Property = Property(name="nbFPUs", type=StringType)
MARTE_HwComputing_HwProcessor.attributes={MARTE_HwComputing_HwProcessor_architecture, MARTE_HwComputing_HwProcessor_nbCores, MARTE_HwComputing_HwProcessor_nbPipelines, MARTE_HwComputing_HwProcessor_nbStages, MARTE_HwComputing_HwProcessor_nbALUs, MARTE_HwComputing_HwProcessor_ipc, MARTE_HwComputing_HwProcessor_mips, MARTE_HwComputing_HwProcessor_nbFPUs}

# HwComputingResource class attributes and methods

# HwComputing_HwISA class attributes and methods

# HwComputing_HwBranchPredictor class attributes and methods

# HwMemory_HwCache class attributes and methods

# MARTE_HwCommunication_HwArbiter class attributes and methods

# HwCommunicationResource class attributes and methods

# HwCommunication_HwMedia class attributes and methods

# MARTE_HwComputing_HwComputingResource class attributes and methods
MARTE_HwComputing_HwComputingResource_op_Frequencies: Property = Property(name="op_Frequencies", type=StringType)
MARTE_HwComputing_HwComputingResource.attributes={MARTE_HwComputing_HwComputingResource_op_Frequencies}

# HwGeneral_HwResource class attributes and methods

# MARTE_HwComputing_HwISA class attributes and methods
MARTE_HwComputing_HwISA_family: Property = Property(name="family", type=StringType)
MARTE_HwComputing_HwISA_inst_Width: Property = Property(name="inst_Width", type=StringType)
MARTE_HwComputing_HwISA_type: Property = Property(name="type", type=StringType)
MARTE_HwComputing_HwISA.attributes={MARTE_HwComputing_HwISA_family, MARTE_HwComputing_HwISA_inst_Width, MARTE_HwComputing_HwISA_type}

# HwResource class attributes and methods

# MARTE_HwComputing_HwBranchPredictor class attributes and methods

# MARTE_HwComputing_HwASIC class attributes and methods

# MARTE_HwComputing_HwPLD class attributes and methods
MARTE_HwComputing_HwPLD_technology: Property = Property(name="technology", type=StringType)
MARTE_HwComputing_HwPLD_organization: Property = Property(name="organization", type=StringType)
MARTE_HwComputing_HwPLD_nbLUTs: Property = Property(name="nbLUTs", type=StringType)
MARTE_HwComputing_HwPLD_ndLUT_Inputs: Property = Property(name="ndLUT_Inputs", type=StringType)
MARTE_HwComputing_HwPLD_nbFlipFlops: Property = Property(name="nbFlipFlops", type=StringType)
MARTE_HwComputing_HwPLD.attributes={MARTE_HwComputing_HwPLD_organization, MARTE_HwComputing_HwPLD_nbLUTs, MARTE_HwComputing_HwPLD_ndLUT_Inputs, MARTE_HwComputing_HwPLD_nbFlipFlops, MARTE_HwComputing_HwPLD_technology}

# HwMemory_HwRAM class attributes and methods

# HwComputing_HwComputingResource class attributes and methods

# MARTE_HwCommunication_HwCommunicationResource class attributes and methods

# MARTE_HwStorageManager_HwMMU class attributes and methods
MARTE_HwStorageManager_HwMMU_virtualAddrSpace: Property = Property(name="virtualAddrSpace", type=StringType)
MARTE_HwStorageManager_HwMMU_physicalAddrSpace: Property = Property(name="physicalAddrSpace", type=StringType)
MARTE_HwStorageManager_HwMMU_memoryProtection: Property = Property(name="memoryProtection", type=StringType)
MARTE_HwStorageManager_HwMMU_nbEntries: Property = Property(name="nbEntries", type=StringType)
MARTE_HwStorageManager_HwMMU.attributes={MARTE_HwStorageManager_HwMMU_physicalAddrSpace, MARTE_HwStorageManager_HwMMU_nbEntries, MARTE_HwStorageManager_HwMMU_memoryProtection, MARTE_HwStorageManager_HwMMU_virtualAddrSpace}

# HwStorageManager class attributes and methods

# MARTE_HwCommunication_HwMedia class attributes and methods
MARTE_HwCommunication_HwMedia_bandWidth: Property = Property(name="bandWidth", type=StringType)
MARTE_HwCommunication_HwMedia.attributes={MARTE_HwCommunication_HwMedia_bandWidth}

# GRM_CommunicationMedia class attributes and methods

# HwCommunication_HwCommunicationResource class attributes and methods

# HwCommunication_HwArbiter class attributes and methods

# MARTE_HwCommunication_HwBus class attributes and methods
MARTE_HwCommunication_HwBus_adressWidth: Property = Property(name="adressWidth", type=StringType)
MARTE_HwCommunication_HwBus_wordWidth: Property = Property(name="wordWidth", type=StringType)
MARTE_HwCommunication_HwBus_isSynchronous: Property = Property(name="isSynchronous", type=StringType)
MARTE_HwCommunication_HwBus_isSerial: Property = Property(name="isSerial", type=StringType)
MARTE_HwCommunication_HwBus.attributes={MARTE_HwCommunication_HwBus_adressWidth, MARTE_HwCommunication_HwBus_wordWidth, MARTE_HwCommunication_HwBus_isSynchronous, MARTE_HwCommunication_HwBus_isSerial}

# HwMedia class attributes and methods

# MARTE_HwCommunication_HwBridge class attributes and methods

# MARTE_HwCommunication_HwEndPoint class attributes and methods

# GRM_CommunicationEndPoint class attributes and methods

# MARTE_HwStorageManager_HwStorageManager class attributes and methods

# GRM_StorageResource class attributes and methods

# HwMemory_HwMemory class attributes and methods

# MARTE_HwStorageManager_HwDMA class attributes and methods
MARTE_HwStorageManager_HwDMA_nbChannels: Property = Property(name="nbChannels", type=StringType)
MARTE_HwStorageManager_HwDMA_transferWidth: Property = Property(name="transferWidth", type=StringType)
MARTE_HwStorageManager_HwDMA.attributes={MARTE_HwStorageManager_HwDMA_nbChannels, MARTE_HwStorageManager_HwDMA_transferWidth}

# HwStorageManager_HwStorageManager class attributes and methods

# HwComputing_HwProcessor class attributes and methods

# MARTE_HwMemory_HwMemory class attributes and methods
MARTE_HwMemory_HwMemory_memorySize: Property = Property(name="memorySize", type=StringType)
MARTE_HwMemory_HwMemory_adressSize: Property = Property(name="adressSize", type=StringType)
MARTE_HwMemory_HwMemory_timings: Property = Property(name="timings", type=StringType)
MARTE_HwMemory_HwMemory_throughput: Property = Property(name="throughput", type=StringType)
MARTE_HwMemory_HwMemory.attributes={MARTE_HwMemory_HwMemory_memorySize, MARTE_HwMemory_HwMemory_adressSize, MARTE_HwMemory_HwMemory_throughput, MARTE_HwMemory_HwMemory_timings}

# MARTE_HwMemory_HwRAM class attributes and methods
MARTE_HwMemory_HwRAM_isSynchronous: Property = Property(name="isSynchronous", type=StringType)
MARTE_HwMemory_HwRAM_isStatic: Property = Property(name="isStatic", type=StringType)
MARTE_HwMemory_HwRAM_isNonVolatile: Property = Property(name="isNonVolatile", type=StringType)
MARTE_HwMemory_HwRAM_organization: Property = Property(name="organization", type=StringType)
MARTE_HwMemory_HwRAM_repl_Policy: Property = Property(name="repl_Policy", type=StringType)
MARTE_HwMemory_HwRAM_writePolicy: Property = Property(name="writePolicy", type=StringType)
MARTE_HwMemory_HwRAM.attributes={MARTE_HwMemory_HwRAM_isNonVolatile, MARTE_HwMemory_HwRAM_isStatic, MARTE_HwMemory_HwRAM_organization, MARTE_HwMemory_HwRAM_writePolicy, MARTE_HwMemory_HwRAM_repl_Policy, MARTE_HwMemory_HwRAM_isSynchronous}

# HwMemory class attributes and methods

# GRM_DeviceResource class attributes and methods

# MARTE_HwDevice_HwI_O class attributes and methods

# HwDevice class attributes and methods

# MARTE_HwDevice_HwSupport class attributes and methods

# MARTE_HwMemory_HwROM class attributes and methods
MARTE_HwMemory_HwROM_type: Property = Property(name="type", type=StringType)
MARTE_HwMemory_HwROM_organization: Property = Property(name="organization", type=StringType)
MARTE_HwMemory_HwROM.attributes={MARTE_HwMemory_HwROM_organization, MARTE_HwMemory_HwROM_type}

# MARTE_HwMemory_HwDrive class attributes and methods
MARTE_HwMemory_HwDrive_sectorSize: Property = Property(name="sectorSize", type=StringType)
MARTE_HwMemory_HwDrive.attributes={MARTE_HwMemory_HwDrive_sectorSize}

# MARTE_HwMemory_HwCache class attributes and methods
MARTE_HwMemory_HwCache_level: Property = Property(name="level", type=StringType)
MARTE_HwMemory_HwCache_type: Property = Property(name="type", type=StringType)
MARTE_HwMemory_HwCache_structure: Property = Property(name="structure", type=StringType)
MARTE_HwMemory_HwCache_repl_Policy: Property = Property(name="repl_Policy", type=StringType)
MARTE_HwMemory_HwCache_writePolicy: Property = Property(name="writePolicy", type=StringType)
MARTE_HwMemory_HwCache.attributes={MARTE_HwMemory_HwCache_type, MARTE_HwMemory_HwCache_repl_Policy, MARTE_HwMemory_HwCache_level, MARTE_HwMemory_HwCache_writePolicy, MARTE_HwMemory_HwCache_structure}

# MARTE_HwTiming_HwTimingResource class attributes and methods

# GRM_TimingResource class attributes and methods

# MARTE_HwTiming_HwClock class attributes and methods

# HwTimingResource class attributes and methods

# MARTE_HwTiming_HwTimer class attributes and methods
MARTE_HwTiming_HwTimer_nbCounters: Property = Property(name="nbCounters", type=StringType)
MARTE_HwTiming_HwTimer_counterWidth: Property = Property(name="counterWidth", type=StringType)
MARTE_HwTiming_HwTimer.attributes={MARTE_HwTiming_HwTimer_nbCounters, MARTE_HwTiming_HwTimer_counterWidth}

# HwTiming_HwClock class attributes and methods

# MARTE_HwDevice_HwDevice class attributes and methods

# MARTE_HwDevice_HWActuator class attributes and methods

# HwI_O class attributes and methods

# MARTE_HwDevice_HWSensor class attributes and methods

# MARTE_HwGeneral_HwResourceService class attributes and methods
MARTE_HwGeneral_HwResourceService_consumption: Property = Property(name="consumption", type=StringType)
MARTE_HwGeneral_HwResourceService_dissipation: Property = Property(name="dissipation", type=StringType)
MARTE_HwGeneral_HwResourceService.attributes={MARTE_HwGeneral_HwResourceService_consumption, MARTE_HwGeneral_HwResourceService_dissipation}

# MARTE_HwGeneral_HwResource class attributes and methods
MARTE_HwGeneral_HwResource_description: Property = Property(name="description", type=StringType)
MARTE_HwGeneral_HwResource_frequency: Property = Property(name="frequency", type=StringType)
MARTE_HwGeneral_HwResource.attributes={MARTE_HwGeneral_HwResource_description, MARTE_HwGeneral_HwResource_frequency}

# HwGeneral_HwResourceService class attributes and methods

# HwCommunication_HwEndPoint class attributes and methods

# MARTE_HwLayout_HwComponent class attributes and methods
MARTE_HwLayout_HwComponent_grid: Property = Property(name="grid", type=StringType)
MARTE_HwLayout_HwComponent_nbPins: Property = Property(name="nbPins", type=StringType)
MARTE_HwLayout_HwComponent_weight: Property = Property(name="weight", type=StringType)
MARTE_HwLayout_HwComponent_kind: Property = Property(name="kind", type=StringType)
MARTE_HwLayout_HwComponent_dimensions: Property = Property(name="dimensions", type=StringType)
MARTE_HwLayout_HwComponent_area: Property = Property(name="area", type=StringType)
MARTE_HwLayout_HwComponent_position: Property = Property(name="position", type=StringType)
MARTE_HwLayout_HwComponent_price: Property = Property(name="price", type=StringType)
MARTE_HwLayout_HwComponent_r_Conditions: Property = Property(name="r_Conditions", type=StringType)
MARTE_HwLayout_HwComponent_staticConsumption: Property = Property(name="staticConsumption", type=StringType)
MARTE_HwLayout_HwComponent_staticDissipation: Property = Property(name="staticDissipation", type=StringType)
MARTE_HwLayout_HwComponent.attributes={MARTE_HwLayout_HwComponent_grid, MARTE_HwLayout_HwComponent_price, MARTE_HwLayout_HwComponent_position, MARTE_HwLayout_HwComponent_kind, MARTE_HwLayout_HwComponent_nbPins, MARTE_HwLayout_HwComponent_dimensions, MARTE_HwLayout_HwComponent_staticDissipation, MARTE_HwLayout_HwComponent_area, MARTE_HwLayout_HwComponent_weight, MARTE_HwLayout_HwComponent_staticConsumption, MARTE_HwLayout_HwComponent_r_Conditions}

# MARTE_SW_ResourceCore_SwResource class attributes and methods

# HwLayout_HwComponent class attributes and methods

# MARTE_HwPower_HwPowerSupply class attributes and methods
MARTE_HwPower_HwPowerSupply_suppliedPower: Property = Property(name="suppliedPower", type=StringType)
MARTE_HwPower_HwPowerSupply_capacity: Property = Property(name="capacity", type=StringType)
MARTE_HwPower_HwPowerSupply.attributes={MARTE_HwPower_HwPowerSupply_capacity, MARTE_HwPower_HwPowerSupply_suppliedPower}

# HwComponent class attributes and methods

# MARTE_HwPower_HwCoolingSupply class attributes and methods
MARTE_HwPower_HwCoolingSupply_coolingPower: Property = Property(name="coolingPower", type=StringType)
MARTE_HwPower_HwCoolingSupply.attributes={MARTE_HwPower_HwCoolingSupply_coolingPower}

# SW_Concurrency_MARTE_TypedElement class attributes and methods

# SW_ResourceCore_MARTE_TypedElement class attributes and methods

# SW_ResourceCore_MARTE_BehavioralFeature class attributes and methods

# MARTE_SW_ResourceCore_SwAccessService class attributes and methods
MARTE_SW_ResourceCore_SwAccessService_isModifier: Property = Property(name="isModifier", type=StringType)
MARTE_SW_ResourceCore_SwAccessService.attributes={MARTE_SW_ResourceCore_SwAccessService_isModifier}

# SW_ResourceCore_MARTE_Property class attributes and methods

# MARTE_SW_Concurrency_EntryPoint class attributes and methods
MARTE_SW_Concurrency_EntryPoint_isReentrant: Property = Property(name="isReentrant", type=StringType)
MARTE_SW_Concurrency_EntryPoint.attributes={MARTE_SW_Concurrency_EntryPoint_isReentrant}

# SW_Concurrency_MARTE_BehavioralFeature class attributes and methods

# MARTE_SW_Concurrency_SwConcurrentResource class attributes and methods
MARTE_SW_Concurrency_SwConcurrentResource_type: Property = Property(name="type", type=StringType)
MARTE_SW_Concurrency_SwConcurrentResource_activationCapacity: Property = Property(name="activationCapacity", type=StringType)
MARTE_SW_Concurrency_SwConcurrentResource.attributes={MARTE_SW_Concurrency_SwConcurrentResource_type, MARTE_SW_Concurrency_SwConcurrentResource_activationCapacity}

# SwResource class attributes and methods

# SW_Concurrency_MARTE_Element class attributes and methods

# MARTE_SW_Concurrency_InterruptResource class attributes and methods
MARTE_SW_Concurrency_InterruptResource_kind: Property = Property(name="kind", type=StringType)
MARTE_SW_Concurrency_InterruptResource_isMaskable: Property = Property(name="isMaskable", type=StringType)
MARTE_SW_Concurrency_InterruptResource.attributes={MARTE_SW_Concurrency_InterruptResource_kind, MARTE_SW_Concurrency_InterruptResource_isMaskable}

# SwConcurrentResource class attributes and methods

# MARTE_SW_Concurrency_MemoryPartition class attributes and methods

# MARTE_SW_Concurrency_SwSchedulableResource class attributes and methods
MARTE_SW_Concurrency_SwSchedulableResource_isStaticSchedulingFeature: Property = Property(name="isStaticSchedulingFeature", type=StringType)
MARTE_SW_Concurrency_SwSchedulableResource_isPreemptable: Property = Property(name="isPreemptable", type=StringType)
MARTE_SW_Concurrency_SwSchedulableResource.attributes={MARTE_SW_Concurrency_SwSchedulableResource_isPreemptable, MARTE_SW_Concurrency_SwSchedulableResource_isStaticSchedulingFeature}

# SW_Concurrency_SwConcurrentResource class attributes and methods

# SW_Concurrency_MARTE_NamedElement class attributes and methods

# MARTE_SW_Concurrency_SwTimerResource class attributes and methods

# TimerResource class attributes and methods

# SW_Concurrency_MARTE_Namespace class attributes and methods

# MARTE_SW_Concurrency_Alarm class attributes and methods
MARTE_SW_Concurrency_Alarm_isWatchdog: Property = Property(name="isWatchdog", type=StringType)
MARTE_SW_Concurrency_Alarm.attributes={MARTE_SW_Concurrency_Alarm_isWatchdog}

# InterruptResource class attributes and methods

# MARTE_SW_Brokering_DeviceBroker class attributes and methods
MARTE_SW_Brokering_DeviceBroker_accessPolicy: Property = Property(name="accessPolicy", type=StringType)
MARTE_SW_Brokering_DeviceBroker_isBuffered: Property = Property(name="isBuffered", type=StringType)
MARTE_SW_Brokering_DeviceBroker.attributes={MARTE_SW_Brokering_DeviceBroker_isBuffered, MARTE_SW_Brokering_DeviceBroker_accessPolicy}

# SW_Brokering_MARTE_TypedElement class attributes and methods

# SW_Brokering_MARTE_BehavioralFeature class attributes and methods

# MARTE_SW_Brokering_MemoryBroker class attributes and methods
MARTE_SW_Brokering_MemoryBroker_accessPolicy: Property = Property(name="accessPolicy", type=StringType)
MARTE_SW_Brokering_MemoryBroker.attributes={MARTE_SW_Brokering_MemoryBroker_accessPolicy}

# MARTE_SW_Interaction_SwInteractionResource class attributes and methods
MARTE_SW_Interaction_SwInteractionResource_isIntraMemoryPartitionInteraction: Property = Property(name="isIntraMemoryPartitionInteraction", type=BooleanType)
MARTE_SW_Interaction_SwInteractionResource_waitingQueuePolicy: Property = Property(name="waitingQueuePolicy", type=StringType)
MARTE_SW_Interaction_SwInteractionResource_waitingQueueCapacity: Property = Property(name="waitingQueueCapacity", type=StringType)
MARTE_SW_Interaction_SwInteractionResource.attributes={MARTE_SW_Interaction_SwInteractionResource_isIntraMemoryPartitionInteraction, MARTE_SW_Interaction_SwInteractionResource_waitingQueueCapacity, MARTE_SW_Interaction_SwInteractionResource_waitingQueuePolicy}

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
MARTE_SW_Interaction_MessageComResource.attributes={MARTE_SW_Interaction_MessageComResource_isFixedMessageSize, MARTE_SW_Interaction_MessageComResource_mechanism, MARTE_SW_Interaction_MessageComResource_messageQueuePolicy}

# GCM_MARTE_Property class attributes and methods

# MARTE_SW_Interaction_NotificationResource class attributes and methods
MARTE_SW_Interaction_NotificationResource_occurence: Property = Property(name="occurence", type=StringType)
MARTE_SW_Interaction_NotificationResource_mechanism: Property = Property(name="mechanism", type=StringType)
MARTE_SW_Interaction_NotificationResource.attributes={MARTE_SW_Interaction_NotificationResource_mechanism, MARTE_SW_Interaction_NotificationResource_occurence}

# SwSynchronizationResource class attributes and methods

# MARTE_SW_Interaction_SwMutualExclusionResource class attributes and methods
MARTE_SW_Interaction_SwMutualExclusionResource_mechanism: Property = Property(name="mechanism", type=StringType)
MARTE_SW_Interaction_SwMutualExclusionResource_concurrentAccessProtocol: Property = Property(name="concurrentAccessProtocol", type=StringType)
MARTE_SW_Interaction_SwMutualExclusionResource.attributes={MARTE_SW_Interaction_SwMutualExclusionResource_concurrentAccessProtocol, MARTE_SW_Interaction_SwMutualExclusionResource_mechanism}

# SW_Interaction_SwSynchronizationResource class attributes and methods

# MARTE_GCM_FlowProperty class attributes and methods
MARTE_GCM_FlowProperty_direction: Property = Property(name="direction", type=StringType)
MARTE_GCM_FlowProperty.attributes={MARTE_GCM_FlowProperty_direction}

# MARTE_GCM_GCMTrigger class attributes and methods

# GCM_MARTE_Trigger class attributes and methods

# MARTE_GCM_FlowPort class attributes and methods
MARTE_GCM_FlowPort_isAtomic: Property = Property(name="isAtomic", type=StringType)
MARTE_GCM_FlowPort_direction: Property = Property(name="direction", type=StringType)
MARTE_GCM_FlowPort.attributes={MARTE_GCM_FlowPort_direction, MARTE_GCM_FlowPort_isAtomic}

# GCM_MARTE_Port class attributes and methods

# MARTE_GCM_ClientServerPort class attributes and methods
MARTE_GCM_ClientServerPort_specificationKind: Property = Property(name="specificationKind", type=StringType)
MARTE_GCM_ClientServerPort_kind: Property = Property(name="kind", type=StringType)
MARTE_GCM_ClientServerPort.attributes={MARTE_GCM_ClientServerPort_specificationKind, MARTE_GCM_ClientServerPort_kind}

# GCM_MARTE_Interface class attributes and methods

# GCM_ClientServerSpecification class attributes and methods

# MARTE_GCM_ClientServerSpecification class attributes and methods

# MARTE_GCM_FlowSpecification class attributes and methods

# MARTE_GCM_ClientServerFeature class attributes and methods
MARTE_GCM_ClientServerFeature_kind: Property = Property(name="kind", type=StringType)
MARTE_GCM_ClientServerFeature.attributes={MARTE_GCM_ClientServerFeature_kind}

# GCM_MARTE_BehavioralFeature class attributes and methods

# GQAM_MARTE_Behavior class attributes and methods

# MARTE_GQAM_GaEventTrace class attributes and methods
MARTE_GQAM_GaEventTrace_content: Property = Property(name="content", type=StringType)
MARTE_GQAM_GaEventTrace_format: Property = Property(name="format", type=StringType)
MARTE_GQAM_GaEventTrace_location: Property = Property(name="location", type=StringType)
MARTE_GQAM_GaEventTrace.attributes={MARTE_GQAM_GaEventTrace_content, MARTE_GQAM_GaEventTrace_format, MARTE_GQAM_GaEventTrace_location}

# GCM_MARTE_Feature class attributes and methods

# MARTE_GCM_GCMInvocationAction class attributes and methods

# GCM_MARTE_InvocationAction class attributes and methods

# MARTE_GCM_DataEvent class attributes and methods

# GCM_MARTE_AnyReceiveEvent class attributes and methods

# GCM_MARTE_Classifier class attributes and methods

# MARTE_GCM_DataPool class attributes and methods
MARTE_GCM_DataPool_ordering: Property = Property(name="ordering", type=StringType)
MARTE_GCM_DataPool.attributes={MARTE_GCM_DataPool_ordering}

# GCM_MARTE_Behavior class attributes and methods

# MARTE_GCM_GCMInvocatingBehavior class attributes and methods

# MARTE_GQAM_GaWorkloadGenerator class attributes and methods
MARTE_GQAM_GaWorkloadGenerator_pop: Property = Property(name="pop", type=StringType)
MARTE_GQAM_GaWorkloadGenerator.attributes={MARTE_GQAM_GaWorkloadGenerator_pop}

# GQAM_GaStep class attributes and methods

# GQAM_MARTE_NamedElement class attributes and methods

# MARTE_GQAM_GaWorkloadEvent class attributes and methods
MARTE_GQAM_GaWorkloadEvent_pattern: Property = Property(name="pattern", type=StringType)
MARTE_GQAM_GaWorkloadEvent.attributes={MARTE_GQAM_GaWorkloadEvent_pattern}

# GQAM_GaWorkloadGenerator class attributes and methods

# GQAM_GaEventTrace class attributes and methods

# GQAM_GaScenario class attributes and methods

# GQAM_MARTE_TimeEvent class attributes and methods

# MARTE_GQAM_GaScenario class attributes and methods
MARTE_GQAM_GaScenario_throughput: Property = Property(name="throughput", type=StringType)
MARTE_GQAM_GaScenario_respT: Property = Property(name="respT", type=StringType)
MARTE_GQAM_GaScenario_utilization: Property = Property(name="utilization", type=StringType)
MARTE_GQAM_GaScenario_utilizationOnHost: Property = Property(name="utilizationOnHost", type=StringType)
MARTE_GQAM_GaScenario_hostDemand: Property = Property(name="hostDemand", type=StringType)
MARTE_GQAM_GaScenario_hostDemandOps: Property = Property(name="hostDemandOps", type=StringType)
MARTE_GQAM_GaScenario_interOccT: Property = Property(name="interOccT", type=StringType)
MARTE_GQAM_GaScenario.attributes={MARTE_GQAM_GaScenario_hostDemand, MARTE_GQAM_GaScenario_utilizationOnHost, MARTE_GQAM_GaScenario_hostDemandOps, MARTE_GQAM_GaScenario_throughput, MARTE_GQAM_GaScenario_respT, MARTE_GQAM_GaScenario_utilization, MARTE_GQAM_GaScenario_interOccT}

# Time_TimedProcessing class attributes and methods

# GQAM_GaWorkloadEvent class attributes and methods

# GQAM_GaRequestedService class attributes and methods

# GQAM_GaTimedObs class attributes and methods

# MARTE_GQAM_GaStep class attributes and methods
MARTE_GQAM_GaStep_isAtomic: Property = Property(name="isAtomic", type=StringType)
MARTE_GQAM_GaStep_blockT: Property = Property(name="blockT", type=StringType)
MARTE_GQAM_GaStep_rep: Property = Property(name="rep", type=StringType)
MARTE_GQAM_GaStep_prob: Property = Property(name="prob", type=StringType)
MARTE_GQAM_GaStep_priority: Property = Property(name="priority", type=StringType)
MARTE_GQAM_GaStep_servCount: Property = Property(name="servCount", type=StringType)
MARTE_GQAM_GaStep_selfDelay: Property = Property(name="selfDelay", type=StringType)
MARTE_GQAM_GaStep.attributes={MARTE_GQAM_GaStep_blockT, MARTE_GQAM_GaStep_servCount, MARTE_GQAM_GaStep_priority, MARTE_GQAM_GaStep_prob, MARTE_GQAM_GaStep_rep, MARTE_GQAM_GaStep_isAtomic, MARTE_GQAM_GaStep_selfDelay}

# GaScenario class attributes and methods

# GQAM_GaExecHost class attributes and methods

# MARTE_GQAM_GaExecHost class attributes and methods
MARTE_GQAM_GaExecHost_commTxOvh: Property = Property(name="commTxOvh", type=StringType)
MARTE_GQAM_GaExecHost_commRcvOvh: Property = Property(name="commRcvOvh", type=StringType)
MARTE_GQAM_GaExecHost_cntxtSwT: Property = Property(name="cntxtSwT", type=StringType)
MARTE_GQAM_GaExecHost_clockOvh: Property = Property(name="clockOvh", type=StringType)
MARTE_GQAM_GaExecHost_schedPriRange: Property = Property(name="schedPriRange", type=StringType)
MARTE_GQAM_GaExecHost_memSize: Property = Property(name="memSize", type=StringType)
MARTE_GQAM_GaExecHost_utilization: Property = Property(name="utilization", type=StringType)
MARTE_GQAM_GaExecHost_throughput: Property = Property(name="throughput", type=StringType)
MARTE_GQAM_GaExecHost.attributes={MARTE_GQAM_GaExecHost_commTxOvh, MARTE_GQAM_GaExecHost_clockOvh, MARTE_GQAM_GaExecHost_memSize, MARTE_GQAM_GaExecHost_throughput, MARTE_GQAM_GaExecHost_utilization, MARTE_GQAM_GaExecHost_schedPriRange, MARTE_GQAM_GaExecHost_cntxtSwT, MARTE_GQAM_GaExecHost_commRcvOvh}

# MARTE_GQAM_GaRequestedService class attributes and methods

# GaStep class attributes and methods

# GQAM_MARTE_Operation class attributes and methods

# MARTE_GQAM_GaTimedObs class attributes and methods
MARTE_GQAM_GaTimedObs_laxity: Property = Property(name="laxity", type=StringType)
MARTE_GQAM_GaTimedObs.attributes={MARTE_GQAM_GaTimedObs_laxity}

# NfpConstraint class attributes and methods

# GQAM_MARTE_TimeObservation class attributes and methods

# MARTE_GQAM_GaCommStep class attributes and methods

# MARTE_GQAM_GaAcqStep class attributes and methods
MARTE_GQAM_GaAcqStep_resUnits: Property = Property(name="resUnits", type=StringType)
MARTE_GQAM_GaAcqStep.attributes={MARTE_GQAM_GaAcqStep_resUnits}

# MARTE_GQAM_GaRelStep class attributes and methods
MARTE_GQAM_GaRelStep_resUnits: Property = Property(name="resUnits", type=StringType)
MARTE_GQAM_GaRelStep.attributes={MARTE_GQAM_GaRelStep_resUnits}

# MARTE_GQAM_GaLatencyObs class attributes and methods
MARTE_GQAM_GaLatencyObs_latency: Property = Property(name="latency", type=StringType)
MARTE_GQAM_GaLatencyObs_miss: Property = Property(name="miss", type=StringType)
MARTE_GQAM_GaLatencyObs_utility: Property = Property(name="utility", type=StringType)
MARTE_GQAM_GaLatencyObs_maxJitter: Property = Property(name="maxJitter", type=StringType)
MARTE_GQAM_GaLatencyObs.attributes={MARTE_GQAM_GaLatencyObs_maxJitter, MARTE_GQAM_GaLatencyObs_miss, MARTE_GQAM_GaLatencyObs_latency, MARTE_GQAM_GaLatencyObs_utility}

# GaTimedObs class attributes and methods

# MARTE_GQAM_GaCommHost class attributes and methods
MARTE_GQAM_GaCommHost_throughput: Property = Property(name="throughput", type=StringType)
MARTE_GQAM_GaCommHost_utilization: Property = Property(name="utilization", type=StringType)
MARTE_GQAM_GaCommHost.attributes={MARTE_GQAM_GaCommHost_utilization, MARTE_GQAM_GaCommHost_throughput}

# MARTE_GQAM_GaCommChannel class attributes and methods
MARTE_GQAM_GaCommChannel_packetSize: Property = Property(name="packetSize", type=StringType)
MARTE_GQAM_GaCommChannel_utilization: Property = Property(name="utilization", type=StringType)
MARTE_GQAM_GaCommChannel.attributes={MARTE_GQAM_GaCommChannel_packetSize, MARTE_GQAM_GaCommChannel_utilization}

# SchedulableResource class attributes and methods

# MARTE_GQAM_GaWorkloadBehavior class attributes and methods

# SAM_MARTE_NamedElement class attributes and methods

# MARTE_SAM_SaCommStep class attributes and methods
MARTE_SAM_SaCommStep_deadline: Property = Property(name="deadline", type=StringType)
MARTE_SAM_SaCommStep_spareCap: Property = Property(name="spareCap", type=StringType)
MARTE_SAM_SaCommStep_schSlack: Property = Property(name="schSlack", type=StringType)
MARTE_SAM_SaCommStep.attributes={MARTE_SAM_SaCommStep_spareCap, MARTE_SAM_SaCommStep_deadline, MARTE_SAM_SaCommStep_schSlack}

# GaCommStep class attributes and methods

# MARTE_GQAM_GaAnalysisContext class attributes and methods
MARTE_GQAM_GaAnalysisContext_context: Property = Property(name="context", type=StringType)
MARTE_GQAM_GaAnalysisContext.attributes={MARTE_GQAM_GaAnalysisContext_context}

# CoreElements_Configuration class attributes and methods

# Variables_ExpressionContext class attributes and methods

# GQAM_GaWorkloadBehavior class attributes and methods

# GQAM_GaResourcesPlatform class attributes and methods

# MARTE_GQAM_GaResourcesPlatform class attributes and methods

# GQAM_MARTE_Classifier class attributes and methods

# MARTE_SAM_SaAnalysisContext class attributes and methods
MARTE_SAM_SaAnalysisContext_isSched: Property = Property(name="isSched", type=StringType)
MARTE_SAM_SaAnalysisContext_optCriterion: Property = Property(name="optCriterion", type=StringType)
MARTE_SAM_SaAnalysisContext.attributes={MARTE_SAM_SaAnalysisContext_optCriterion, MARTE_SAM_SaAnalysisContext_isSched}

# GaAnalysisContext class attributes and methods

# MARTE_SAM_SaEndtoEndFlow class attributes and methods
MARTE_SAM_SaEndtoEndFlow_isSched: Property = Property(name="isSched", type=StringType)
MARTE_SAM_SaEndtoEndFlow_schSlack: Property = Property(name="schSlack", type=StringType)
MARTE_SAM_SaEndtoEndFlow_end2EndT: Property = Property(name="end2EndT", type=StringType)
MARTE_SAM_SaEndtoEndFlow_end2EndD: Property = Property(name="end2EndD", type=StringType)
MARTE_SAM_SaEndtoEndFlow.attributes={MARTE_SAM_SaEndtoEndFlow_end2EndD, MARTE_SAM_SaEndtoEndFlow_end2EndT, MARTE_SAM_SaEndtoEndFlow_schSlack, MARTE_SAM_SaEndtoEndFlow_isSched}

# MARTE_SAM_SaSchedObs class attributes and methods
MARTE_SAM_SaSchedObs_suspentions: Property = Property(name="suspentions", type=StringType)
MARTE_SAM_SaSchedObs_blockT: Property = Property(name="blockT", type=StringType)
MARTE_SAM_SaSchedObs_overlaps: Property = Property(name="overlaps", type=StringType)
MARTE_SAM_SaSchedObs.attributes={MARTE_SAM_SaSchedObs_overlaps, MARTE_SAM_SaSchedObs_blockT, MARTE_SAM_SaSchedObs_suspentions}

# SAM_MARTE_BehavioralFeature class attributes and methods

# MARTE_SAM_SaStep class attributes and methods
MARTE_SAM_SaStep_deadline: Property = Property(name="deadline", type=StringType)
MARTE_SAM_SaStep_spareCap: Property = Property(name="spareCap", type=StringType)
MARTE_SAM_SaStep_schSlack: Property = Property(name="schSlack", type=StringType)
MARTE_SAM_SaStep_preemptT: Property = Property(name="preemptT", type=StringType)
MARTE_SAM_SaStep_readyT: Property = Property(name="readyT", type=StringType)
MARTE_SAM_SaStep_nonpreemptionBlocking: Property = Property(name="nonpreemptionBlocking", type=StringType)
MARTE_SAM_SaStep_selfSuspensionBlocking: Property = Property(name="selfSuspensionBlocking", type=StringType)
MARTE_SAM_SaStep_numberSelfSuspensions: Property = Property(name="numberSelfSuspensions", type=StringType)
MARTE_SAM_SaStep.attributes={MARTE_SAM_SaStep_readyT, MARTE_SAM_SaStep_schSlack, MARTE_SAM_SaStep_selfSuspensionBlocking, MARTE_SAM_SaStep_spareCap, MARTE_SAM_SaStep_nonpreemptionBlocking, MARTE_SAM_SaStep_numberSelfSuspensions, MARTE_SAM_SaStep_preemptT, MARTE_SAM_SaStep_deadline}

# SAM_SaSharedResource class attributes and methods

# MARTE_SAM_SaSharedResource class attributes and methods
MARTE_SAM_SaSharedResource_releaseT: Property = Property(name="releaseT", type=StringType)
MARTE_SAM_SaSharedResource_capacity: Property = Property(name="capacity", type=StringType)
MARTE_SAM_SaSharedResource_isPreemp: Property = Property(name="isPreemp", type=StringType)
MARTE_SAM_SaSharedResource_isConsum: Property = Property(name="isConsum", type=StringType)
MARTE_SAM_SaSharedResource_acquisT: Property = Property(name="acquisT", type=StringType)
MARTE_SAM_SaSharedResource.attributes={MARTE_SAM_SaSharedResource_releaseT, MARTE_SAM_SaSharedResource_isConsum, MARTE_SAM_SaSharedResource_capacity, MARTE_SAM_SaSharedResource_isPreemp, MARTE_SAM_SaSharedResource_acquisT}

# MutualExclusionResource class attributes and methods

# MARTE_SAM_SaCommHost class attributes and methods
MARTE_SAM_SaCommHost_isSched: Property = Property(name="isSched", type=StringType)
MARTE_SAM_SaCommHost_schSlack: Property = Property(name="schSlack", type=StringType)
MARTE_SAM_SaCommHost.attributes={MARTE_SAM_SaCommHost_isSched, MARTE_SAM_SaCommHost_schSlack}

# GaCommHost class attributes and methods

# MARTE_SAM_SaExecHost class attributes and methods
MARTE_SAM_SaExecHost_isSched: Property = Property(name="isSched", type=StringType)
MARTE_SAM_SaExecHost_schSlack: Property = Property(name="schSlack", type=StringType)
MARTE_SAM_SaExecHost_schedUtiliz: Property = Property(name="schedUtiliz", type=StringType)
MARTE_SAM_SaExecHost_ISRswitchT: Property = Property(name="ISRswitchT", type=StringType)
MARTE_SAM_SaExecHost_ISRprioRange: Property = Property(name="ISRprioRange", type=StringType)
MARTE_SAM_SaExecHost.attributes={MARTE_SAM_SaExecHost_schSlack, MARTE_SAM_SaExecHost_schedUtiliz, MARTE_SAM_SaExecHost_ISRprioRange, MARTE_SAM_SaExecHost_ISRswitchT, MARTE_SAM_SaExecHost_isSched}

# GaExecHost class attributes and methods

# MARTE_PAM_PaStep class attributes and methods
MARTE_PAM_PaStep_noSync: Property = Property(name="noSync", type=StringType)
MARTE_PAM_PaStep_extOpDemand: Property = Property(name="extOpDemand", type=StringType)
MARTE_PAM_PaStep_extOpCount: Property = Property(name="extOpCount", type=StringType)
MARTE_PAM_PaStep_behavCount: Property = Property(name="behavCount", type=StringType)
MARTE_PAM_PaStep.attributes={MARTE_PAM_PaStep_behavCount, MARTE_PAM_PaStep_noSync, MARTE_PAM_PaStep_extOpCount, MARTE_PAM_PaStep_extOpDemand}

# MARTE_PAM_PaLogicalResource class attributes and methods
MARTE_PAM_PaLogicalResource_utilization: Property = Property(name="utilization", type=StringType)
MARTE_PAM_PaLogicalResource_throughput: Property = Property(name="throughput", type=StringType)
MARTE_PAM_PaLogicalResource_poolSize: Property = Property(name="poolSize", type=StringType)
MARTE_PAM_PaLogicalResource.attributes={MARTE_PAM_PaLogicalResource_poolSize, MARTE_PAM_PaLogicalResource_throughput, MARTE_PAM_PaLogicalResource_utilization}

# MARTE_PAM_PaRunTInstance class attributes and methods
MARTE_PAM_PaRunTInstance_poolSize: Property = Property(name="poolSize", type=StringType)
MARTE_PAM_PaRunTInstance_unbddPool: Property = Property(name="unbddPool", type=StringType)
MARTE_PAM_PaRunTInstance_utilization: Property = Property(name="utilization", type=StringType)
MARTE_PAM_PaRunTInstance_throughput: Property = Property(name="throughput", type=StringType)
MARTE_PAM_PaRunTInstance.attributes={MARTE_PAM_PaRunTInstance_unbddPool, MARTE_PAM_PaRunTInstance_poolSize, MARTE_PAM_PaRunTInstance_throughput, MARTE_PAM_PaRunTInstance_utilization}

# PAM_MARTE_NamedElement class attributes and methods

# MARTE_PAM_PaRequestedStep class attributes and methods

# PAM_PaStep class attributes and methods

# MARTE_PAM_PaCommStep class attributes and methods

# GQAM_GaCommStep class attributes and methods

# MARTE_PAM_PaResPassStep class attributes and methods
MARTE_PAM_PaResPassStep_resUnits: Property = Property(name="resUnits", type=StringType)
MARTE_PAM_PaResPassStep.attributes={MARTE_PAM_PaResPassStep_resUnits}

# Relationships
base_Property0: BinaryAssociation = BinaryAssociation(
    name="base_Property0",
    ends={
        Property(name="NFPs_MARTE_Property", type=MARTE_NFPs_Nfp, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_NFPs_Nfp", type=NFPs_MARTE_Property, multiplicity=Multiplicity(1, 1))
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
allocatedTo28: BinaryAssociation = BinaryAssociation(
    name="allocatedTo28",
    ends={
        Property(name="Alloc_Allocated", type=MARTE_Alloc_Allocated, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_Allocated29", type=Alloc_Allocated, multiplicity=Multiplicity(0, 9999))
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
unitType61: BinaryAssociation = BinaryAssociation(
    name="unitType61",
    ends={
        Property(name="Time_MARTE_Enumeration", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType", type=Time_MARTE_Enumeration, multiplicity=Multiplicity(0, 1))
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
base_Event59: BinaryAssociation = BinaryAssociation(
    name="base_Event59",
    ends={
        Property(name="Time_MARTE_Event", type=MARTE_Time_Clock, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_Clock60", type=Time_MARTE_Event, multiplicity=Multiplicity(1, 1))
    }
)
resolAttr62: BinaryAssociation = BinaryAssociation(
    name="resolAttr62",
    ends={
        Property(name="Time_MARTE_Property64", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType63", type=Time_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
maxValAttr65: BinaryAssociation = BinaryAssociation(
    name="maxValAttr65",
    ends={
        Property(name="Time_MARTE_Property67", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType66", type=Time_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
offsetAttr68: BinaryAssociation = BinaryAssociation(
    name="offsetAttr68",
    ends={
        Property(name="Time_MARTE_Property70", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType69", type=Time_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
getTime71: BinaryAssociation = BinaryAssociation(
    name="getTime71",
    ends={
        Property(name="Time_MARTE_Operation", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType72", type=Time_MARTE_Operation, multiplicity=Multiplicity(0, 1))
    }
)
setTime73: BinaryAssociation = BinaryAssociation(
    name="setTime73",
    ends={
        Property(name="Time_MARTE_Operation75", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType74", type=Time_MARTE_Operation, multiplicity=Multiplicity(0, 1))
    }
)
indexToValue76: BinaryAssociation = BinaryAssociation(
    name="indexToValue76",
    ends={
        Property(name="Time_MARTE_Operation78", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType77", type=Time_MARTE_Operation, multiplicity=Multiplicity(0, 1))
    }
)
base_Class79: BinaryAssociation = BinaryAssociation(
    name="base_Class79",
    ends={
        Property(name="Time_MARTE_Class", type=MARTE_Time_ClockType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_ClockType80", type=Time_MARTE_Class, multiplicity=Multiplicity(1, 1))
    }
)
on81: BinaryAssociation = BinaryAssociation(
    name="on81",
    ends={
        Property(name="Time_Clock", type=MARTE_Time_TimedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedElement", type=Time_Clock, multiplicity=Multiplicity(1, 9999))
    }
)
base_ValueSpecification82: BinaryAssociation = BinaryAssociation(
    name="base_ValueSpecification82",
    ends={
        Property(name="Time_MARTE_ValueSpecification", type=MARTE_Time_TimedValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedValueSpecification", type=Time_MARTE_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
base_Action89: BinaryAssociation = BinaryAssociation(
    name="base_Action89",
    ends={
        Property(name="Time_MARTE_Action", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing", type=Time_MARTE_Action, multiplicity=Multiplicity(1, 1))
    }
)
base_TimeObservation83: BinaryAssociation = BinaryAssociation(
    name="base_TimeObservation83",
    ends={
        Property(name="Time_MARTE_TimeObservation", type=MARTE_Time_TimedInstantObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedInstantObservation", type=Time_MARTE_TimeObservation, multiplicity=Multiplicity(1, 1))
    }
)
base_DurationObservation84: BinaryAssociation = BinaryAssociation(
    name="base_DurationObservation84",
    ends={
        Property(name="Time_MARTE_DurationObservation", type=MARTE_Time_TimedDurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedDurationObservation", type=Time_MARTE_DurationObservation, multiplicity=Multiplicity(1, 1))
    }
)
base_TimeEvent85: BinaryAssociation = BinaryAssociation(
    name="base_TimeEvent85",
    ends={
        Property(name="Time_MARTE_TimeEvent", type=MARTE_Time_TimedEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedEvent", type=Time_MARTE_TimeEvent, multiplicity=Multiplicity(1, 1))
    }
)
every86: BinaryAssociation = BinaryAssociation(
    name="every86",
    ends={
        Property(name="Time_MARTE_ValueSpecification88", type=MARTE_Time_TimedEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedEvent87", type=Time_MARTE_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_ConnectableElement110: BinaryAssociation = BinaryAssociation(
    name="base_ConnectableElement110",
    ends={
        Property(name="GRM_MARTE_ConnectableElement", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource111", type=GRM_MARTE_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
base_Behavior90: BinaryAssociation = BinaryAssociation(
    name="base_Behavior90",
    ends={
        Property(name="Time_MARTE_Behavior", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing91", type=Time_MARTE_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Message92: BinaryAssociation = BinaryAssociation(
    name="base_Message92",
    ends={
        Property(name="Time_MARTE_Message", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing93", type=Time_MARTE_Message, multiplicity=Multiplicity(1, 1))
    }
)
duration94: BinaryAssociation = BinaryAssociation(
    name="duration94",
    ends={
        Property(name="Time_MARTE_ValueSpecification96", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing95", type=Time_MARTE_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start97: BinaryAssociation = BinaryAssociation(
    name="start97",
    ends={
        Property(name="Time_MARTE_Event99", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing98", type=Time_MARTE_Event, multiplicity=Multiplicity(0, 1))
    }
)
finish100: BinaryAssociation = BinaryAssociation(
    name="finish100",
    ends={
        Property(name="Time_MARTE_Event102", type=MARTE_Time_TimedProcessing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedProcessing101", type=Time_MARTE_Event, multiplicity=Multiplicity(0, 1))
    }
)
base_Property103: BinaryAssociation = BinaryAssociation(
    name="base_Property103",
    ends={
        Property(name="GRM_MARTE_Property", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource", type=GRM_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_InstanceSpecification104: BinaryAssociation = BinaryAssociation(
    name="base_InstanceSpecification104",
    ends={
        Property(name="GRM_MARTE_InstanceSpecification", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource105", type=GRM_MARTE_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier106: BinaryAssociation = BinaryAssociation(
    name="base_Classifier106",
    ends={
        Property(name="GRM_MARTE_Classifier", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource107", type=GRM_MARTE_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Lifeline108: BinaryAssociation = BinaryAssociation(
    name="base_Lifeline108",
    ends={
        Property(name="GRM_MARTE_Lifeline", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource109", type=GRM_MARTE_Lifeline, multiplicity=Multiplicity(1, 1))
    }
)
processingUnits112: BinaryAssociation = BinaryAssociation(
    name="processingUnits112",
    ends={
        Property(name="GRM_ProcessingResource", type=MARTE_GRM_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Scheduler", type=GRM_ProcessingResource, multiplicity=Multiplicity(0, 9999))
    }
)
host113: BinaryAssociation = BinaryAssociation(
    name="host113",
    ends={
        Property(name="GRM_ComputingResource", type=MARTE_GRM_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Scheduler114", type=GRM_ComputingResource, multiplicity=Multiplicity(0, 1))
    }
)
protectedSharedResources115: BinaryAssociation = BinaryAssociation(
    name="protectedSharedResources115",
    ends={
        Property(name="MutualExclusionResource", type=MARTE_GRM_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="scheduler", type=GRM_MutualExclusionResource, multiplicity=Multiplicity(0, 9999))
    }
)
schedulableResources116: BinaryAssociation = BinaryAssociation(
    name="schedulableResources116",
    ends={
        Property(name="SchedulableResource", type=MARTE_GRM_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="host", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 9999))
    }
)
mainScheduler117: BinaryAssociation = BinaryAssociation(
    name="mainScheduler117",
    ends={
        Property(name="GRM_Scheduler", type=MARTE_GRM_ProcessingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ProcessingResource", type=GRM_Scheduler, multiplicity=Multiplicity(0, 1))
    }
)
scheduler118: BinaryAssociation = BinaryAssociation(
    name="scheduler118",
    ends={
        Property(name="Scheduler", type=MARTE_GRM_MutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="protectedSharedResources", type=GRM_Scheduler, multiplicity=Multiplicity(0, 1))
    }
)
dependentScheduler119: BinaryAssociation = BinaryAssociation(
    name="dependentScheduler119",
    ends={
        Property(name="SecondaryScheduler", type=MARTE_GRM_SchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="virtualProcessingUnits", type=GRM_SecondaryScheduler, multiplicity=Multiplicity(0, 1))
    }
)
host120: BinaryAssociation = BinaryAssociation(
    name="host120",
    ends={
        Property(name="Scheduler121", type=MARTE_GRM_SchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="schedulableResources", type=GRM_Scheduler, multiplicity=Multiplicity(0, 1))
    }
)
virtualProcessingUnits122: BinaryAssociation = BinaryAssociation(
    name="virtualProcessingUnits122",
    ends={
        Property(name="SchedulableResource123", type=MARTE_GRM_SecondaryScheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="dependentScheduler", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 9999))
    }
)
base_Connector124: BinaryAssociation = BinaryAssociation(
    name="base_Connector124",
    ends={
        Property(name="GRM_MARTE_Connector", type=MARTE_GRM_CommunicationMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationMedia", type=GRM_MARTE_Connector, multiplicity=Multiplicity(1, 1))
    }
)
owner125: BinaryAssociation = BinaryAssociation(
    name="owner125",
    ends={
        Property(name="GRM_Resource", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)
base_ExecutionSpecification126: BinaryAssociation = BinaryAssociation(
    name="base_ExecutionSpecification126",
    ends={
        Property(name="GRM_MARTE_ExecutionSpecification", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService127", type=GRM_MARTE_ExecutionSpecification, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature128: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature128",
    ends={
        Property(name="GRM_MARTE_BehavioralFeature", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService129", type=GRM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Behavior130: BinaryAssociation = BinaryAssociation(
    name="base_Behavior130",
    ends={
        Property(name="GRM_MARTE_Behavior", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService131", type=GRM_MARTE_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Collaboration132: BinaryAssociation = BinaryAssociation(
    name="base_Collaboration132",
    ends={
        Property(name="GRM_MARTE_Collaboration", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService133", type=GRM_MARTE_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
base_CollaborationUse134: BinaryAssociation = BinaryAssociation(
    name="base_CollaborationUse134",
    ends={
        Property(name="GRM_MARTE_CollaborationUse", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService135", type=GRM_MARTE_CollaborationUse, multiplicity=Multiplicity(1, 1))
    }
)
base_NamedElement136: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement136",
    ends={
        Property(name="GRM_MARTE_NamedElement", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage", type=GRM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
subUsage137: BinaryAssociation = BinaryAssociation(
    name="subUsage137",
    ends={
        Property(name="GRM_ResourceUsage", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage138", type=GRM_ResourceUsage, multiplicity=Multiplicity(0, 9999))
    }
)
usedResources139: BinaryAssociation = BinaryAssociation(
    name="usedResources139",
    ends={
        Property(name="GRM_Resource141", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage140", type=GRM_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
base_Connector142: BinaryAssociation = BinaryAssociation(
    name="base_Connector142",
    ends={
        Property(name="RSM_MARTE_Connector", type=MARTE_RSM_LinkTopology, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_LinkTopology", type=RSM_MARTE_Connector, multiplicity=Multiplicity(1, 1))
    }
)
intervalAttrib152: BinaryAssociation = BinaryAssociation(
    name="intervalAttrib152",
    ends={
        Property(name="DataTypes_MARTE_Property", type=MARTE_DataTypes_IntervalType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_IntervalType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_DataType153: BinaryAssociation = BinaryAssociation(
    name="base_DataType153",
    ends={
        Property(name="DataTypes_MARTE_DataType155", type=MARTE_DataTypes_IntervalType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_IntervalType154", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
base_ConnectorEnd143: BinaryAssociation = BinaryAssociation(
    name="base_ConnectorEnd143",
    ends={
        Property(name="RSM_MARTE_ConnectorEnd", type=MARTE_RSM_Tiler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Tiler", type=RSM_MARTE_ConnectorEnd, multiplicity=Multiplicity(1, 1))
    }
)
base_MultiplicityElement144: BinaryAssociation = BinaryAssociation(
    name="base_MultiplicityElement144",
    ends={
        Property(name="RSM_MARTE_MultiplicityElement", type=MARTE_RSM_Shaped, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Shaped", type=RSM_MARTE_MultiplicityElement, multiplicity=Multiplicity(1, 1))
    }
)
base_Property145: BinaryAssociation = BinaryAssociation(
    name="base_Property145",
    ends={
        Property(name="Variables_MARTE_Property", type=MARTE_Variables_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Variables_Var", type=Variables_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_NamedElement146: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement146",
    ends={
        Property(name="Variables_MARTE_NamedElement", type=MARTE_Variables_ExpressionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Variables_ExpressionContext", type=Variables_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
base_Behavior147: BinaryAssociation = BinaryAssociation(
    name="base_Behavior147",
    ends={
        Property(name="Operators_MARTE_Behavior", type=MARTE_Operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Operators_Operator", type=Operators_MARTE_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
baseType148: BinaryAssociation = BinaryAssociation(
    name="baseType148",
    ends={
        Property(name="DataTypes_MARTE_DataType", type=MARTE_DataTypes_BoundedSubtype, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_BoundedSubtype", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
base_DataType149: BinaryAssociation = BinaryAssociation(
    name="base_DataType149",
    ends={
        Property(name="DataTypes_MARTE_DataType151", type=MARTE_DataTypes_BoundedSubtype, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_BoundedSubtype150", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioredClassifier177: BinaryAssociation = BinaryAssociation(
    name="base_BehavioredClassifier177",
    ends={
        Property(name="HLAM_MARTE_BehavioredClassifier", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit178", type=HLAM_MARTE_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
collectionAttrib156: BinaryAssociation = BinaryAssociation(
    name="collectionAttrib156",
    ends={
        Property(name="DataTypes_MARTE_Property157", type=MARTE_DataTypes_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_CollectionType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_DataType158: BinaryAssociation = BinaryAssociation(
    name="base_DataType158",
    ends={
        Property(name="DataTypes_MARTE_DataType160", type=MARTE_DataTypes_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_CollectionType159", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
choiceAttrib161: BinaryAssociation = BinaryAssociation(
    name="choiceAttrib161",
    ends={
        Property(name="DataTypes_MARTE_Property162", type=MARTE_DataTypes_ChoiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_ChoiceType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(0, 9999))
    }
)
defaultAttrib163: BinaryAssociation = BinaryAssociation(
    name="defaultAttrib163",
    ends={
        Property(name="DataTypes_MARTE_Property165", type=MARTE_DataTypes_ChoiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_ChoiceType164", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(0, 1))
    }
)
base_DataType166: BinaryAssociation = BinaryAssociation(
    name="base_DataType166",
    ends={
        Property(name="DataTypes_MARTE_DataType168", type=MARTE_DataTypes_ChoiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_ChoiceType167", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
tupleAttrib169: BinaryAssociation = BinaryAssociation(
    name="tupleAttrib169",
    ends={
        Property(name="DataTypes_MARTE_Property170", type=MARTE_DataTypes_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_TupleType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(0, 9999))
    }
)
base_DataType171: BinaryAssociation = BinaryAssociation(
    name="base_DataType171",
    ends={
        Property(name="DataTypes_MARTE_DataType173", type=MARTE_DataTypes_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_TupleType172", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
operationalMode174: BinaryAssociation = BinaryAssociation(
    name="operationalMode174",
    ends={
        Property(name="HLAM_MARTE_Behavior", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit", type=HLAM_MARTE_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
main175: BinaryAssociation = BinaryAssociation(
    name="main175",
    ends={
        Property(name="HLAM_MARTE_Operation", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit176", type=HLAM_MARTE_Operation, multiplicity=Multiplicity(0, 1))
    }
)
tRef192: BinaryAssociation = BinaryAssociation(
    name="tRef192",
    ends={
        Property(name="Time_TimedInstantObservation", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification", type=Time_TimedInstantObservation, multiplicity=Multiplicity(0, 1))
    }
)
base_BehavioredClassifier179: BinaryAssociation = BinaryAssociation(
    name="base_BehavioredClassifier179",
    ends={
        Property(name="HLAM_MARTE_BehavioredClassifier180", type=MARTE_HLAM_PpUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_PpUnit", type=HLAM_MARTE_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature181: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature181",
    ends={
        Property(name="HLAM_MARTE_BehavioralFeature", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature", type=HLAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Message182: BinaryAssociation = BinaryAssociation(
    name="base_Message182",
    ends={
        Property(name="HLAM_MARTE_Message", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature183", type=HLAM_MARTE_Message, multiplicity=Multiplicity(1, 1))
    }
)
base_Signal184: BinaryAssociation = BinaryAssociation(
    name="base_Signal184",
    ends={
        Property(name="HLAM_MARTE_Signal", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature185", type=HLAM_MARTE_Signal, multiplicity=Multiplicity(1, 1))
    }
)
base_Port186: BinaryAssociation = BinaryAssociation(
    name="base_Port186",
    ends={
        Property(name="HLAM_MARTE_Port", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature187", type=HLAM_MARTE_Port, multiplicity=Multiplicity(1, 1))
    }
)
base_InvocationAction188: BinaryAssociation = BinaryAssociation(
    name="base_InvocationAction188",
    ends={
        Property(name="HLAM_MARTE_InvocationAction", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature189", type=HLAM_MARTE_InvocationAction, multiplicity=Multiplicity(1, 1))
    }
)
specification190: BinaryAssociation = BinaryAssociation(
    name="specification190",
    ends={
        Property(name="HLAM_RtSpecification", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature191", type=HLAM_RtSpecification, multiplicity=Multiplicity(1, 9999))
    }
)
base_Comment193: BinaryAssociation = BinaryAssociation(
    name="base_Comment193",
    ends={
        Property(name="HLAM_MARTE_Comment", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification194", type=HLAM_MARTE_Comment, multiplicity=Multiplicity(1, 1))
    }
)
context195: BinaryAssociation = BinaryAssociation(
    name="context195",
    ends={
        Property(name="HLAM_MARTE_BehavioralFeature197", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification196", type=HLAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
base_BehavioralFeature198: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature198",
    ends={
        Property(name="HLAM_MARTE_BehavioralFeature199", type=MARTE_HLAM_RtAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtAction", type=HLAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_InvocationAction200: BinaryAssociation = BinaryAssociation(
    name="base_InvocationAction200",
    ends={
        Property(name="HLAM_MARTE_InvocationAction202", type=MARTE_HLAM_RtAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtAction201", type=HLAM_MARTE_InvocationAction, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature203: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature203",
    ends={
        Property(name="HLAM_MARTE_BehavioralFeature204", type=MARTE_HLAM_RtService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtService", type=HLAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
ownedMMUs210: BinaryAssociation = BinaryAssociation(
    name="ownedMMUs210",
    ends={
        Property(name="HwStorageManager_HwMMU", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor211", type=HwStorageManager_HwMMU, multiplicity=Multiplicity(0, 9999))
    }
)
ownedISAs205: BinaryAssociation = BinaryAssociation(
    name="ownedISAs205",
    ends={
        Property(name="HwComputing_HwISA", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor", type=HwComputing_HwISA, multiplicity=Multiplicity(0, 9999))
    }
)
predictors206: BinaryAssociation = BinaryAssociation(
    name="predictors206",
    ends={
        Property(name="HwComputing_HwBranchPredictor", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor207", type=HwComputing_HwBranchPredictor, multiplicity=Multiplicity(0, 9999))
    }
)
caches208: BinaryAssociation = BinaryAssociation(
    name="caches208",
    ends={
        Property(name="HwMemory_HwCache", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor209", type=HwMemory_HwCache, multiplicity=Multiplicity(0, 9999))
    }
)
blocksRAM212: BinaryAssociation = BinaryAssociation(
    name="blocksRAM212",
    ends={
        Property(name="HwMemory_HwRAM", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD", type=HwMemory_HwRAM, multiplicity=Multiplicity(0, 9999))
    }
)
blocksComputing213: BinaryAssociation = BinaryAssociation(
    name="blocksComputing213",
    ends={
        Property(name="HwComputing_HwComputingResource", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD214", type=HwComputing_HwComputingResource, multiplicity=Multiplicity(0, 9999))
    }
)
controlledMedias215: BinaryAssociation = BinaryAssociation(
    name="controlledMedias215",
    ends={
        Property(name="HwMedia", type=MARTE_HwCommunication_HwArbiter, multiplicity=Multiplicity(1, 1)),
        Property(name="arbiters", type=HwCommunication_HwMedia, multiplicity=Multiplicity(0, 9999))
    }
)
arbiters216: BinaryAssociation = BinaryAssociation(
    name="arbiters216",
    ends={
        Property(name="HwArbiter", type=MARTE_HwCommunication_HwMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="controlledMedias", type=HwCommunication_HwArbiter, multiplicity=Multiplicity(0, 9999))
    }
)
sides217: BinaryAssociation = BinaryAssociation(
    name="sides217",
    ends={
        Property(name="HwCommunication_HwMedia", type=MARTE_HwCommunication_HwBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwBridge", type=HwCommunication_HwMedia, multiplicity=Multiplicity(0, 9999))
    }
)
connectedTo218: BinaryAssociation = BinaryAssociation(
    name="connectedTo218",
    ends={
        Property(name="HwCommunication_HwMedia219", type=MARTE_HwCommunication_HwEndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwEndPoint", type=HwCommunication_HwMedia, multiplicity=Multiplicity(0, 9999))
    }
)
managedMemories220: BinaryAssociation = BinaryAssociation(
    name="managedMemories220",
    ends={
        Property(name="HwMemory_HwMemory", type=MARTE_HwStorageManager_HwStorageManager, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwStorageManager", type=HwMemory_HwMemory, multiplicity=Multiplicity(0, 9999))
    }
)
drivenBy221: BinaryAssociation = BinaryAssociation(
    name="drivenBy221",
    ends={
        Property(name="HwComputing_HwProcessor", type=MARTE_HwStorageManager_HwDMA, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwDMA", type=HwComputing_HwProcessor, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTLBs222: BinaryAssociation = BinaryAssociation(
    name="ownedTLBs222",
    ends={
        Property(name="HwMemory_HwCache223", type=MARTE_HwStorageManager_HwMMU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwMMU", type=HwMemory_HwCache, multiplicity=Multiplicity(0, 9999))
    }
)
buffer224: BinaryAssociation = BinaryAssociation(
    name="buffer224",
    ends={
        Property(name="HwMemory_HwRAM225", type=MARTE_HwMemory_HwDrive, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwDrive", type=HwMemory_HwRAM, multiplicity=Multiplicity(0, 1))
    }
)
inputClock226: BinaryAssociation = BinaryAssociation(
    name="inputClock226",
    ends={
        Property(name="HwTiming_HwClock", type=MARTE_HwTiming_HwTimer, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwTiming_HwTimer", type=HwTiming_HwClock, multiplicity=Multiplicity(0, 1))
    }
)
p_HW_Services227: BinaryAssociation = BinaryAssociation(
    name="p_HW_Services227",
    ends={
        Property(name="HwGeneral_HwResourceService", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource", type=HwGeneral_HwResourceService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
r_HW_Services228: BinaryAssociation = BinaryAssociation(
    name="r_HW_Services228",
    ends={
        Property(name="HwGeneral_HwResourceService230", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource229", type=HwGeneral_HwResourceService, multiplicity=Multiplicity(0, 9999))
    }
)
ownedHW231: BinaryAssociation = BinaryAssociation(
    name="ownedHW231",
    ends={
        Property(name="HwGeneral_HwResource", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource232", type=HwGeneral_HwResource, multiplicity=Multiplicity(0, 9999))
    }
)
endPoints233: BinaryAssociation = BinaryAssociation(
    name="endPoints233",
    ends={
        Property(name="HwCommunication_HwEndPoint", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource234", type=HwCommunication_HwEndPoint, multiplicity=Multiplicity(0, 9999))
    }
)
poweredServices235: BinaryAssociation = BinaryAssociation(
    name="poweredServices235",
    ends={
        Property(name="HwGeneral_HwResourceService236", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent", type=HwGeneral_HwResourceService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subComponents237: BinaryAssociation = BinaryAssociation(
    name="subComponents237",
    ends={
        Property(name="HwLayout_HwComponent", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent238", type=HwLayout_HwComponent, multiplicity=Multiplicity(0, 9999))
    }
)
adressSpace257: BinaryAssociation = BinaryAssociation(
    name="adressSpace257",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource258", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
identifierElements239: BinaryAssociation = BinaryAssociation(
    name="identifierElements239",
    ends={
        Property(name="SW_ResourceCore_MARTE_TypedElement", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource", type=SW_ResourceCore_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
stateElements240: BinaryAssociation = BinaryAssociation(
    name="stateElements240",
    ends={
        Property(name="SW_ResourceCore_MARTE_TypedElement242", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource241", type=SW_ResourceCore_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
memorySizeFootprint243: BinaryAssociation = BinaryAssociation(
    name="memorySizeFootprint243",
    ends={
        Property(name="SW_ResourceCore_MARTE_TypedElement245", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource244", type=SW_ResourceCore_MARTE_TypedElement, multiplicity=Multiplicity(0, 1))
    }
)
createServices246: BinaryAssociation = BinaryAssociation(
    name="createServices246",
    ends={
        Property(name="SW_ResourceCore_MARTE_BehavioralFeature", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource247", type=SW_ResourceCore_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
deleteServices248: BinaryAssociation = BinaryAssociation(
    name="deleteServices248",
    ends={
        Property(name="SW_ResourceCore_MARTE_BehavioralFeature250", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource249", type=SW_ResourceCore_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
initializeServices251: BinaryAssociation = BinaryAssociation(
    name="initializeServices251",
    ends={
        Property(name="SW_ResourceCore_MARTE_BehavioralFeature253", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource252", type=SW_ResourceCore_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
accessedElement254: BinaryAssociation = BinaryAssociation(
    name="accessedElement254",
    ends={
        Property(name="SW_ResourceCore_MARTE_Property", type=MARTE_SW_ResourceCore_SwAccessService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwAccessService", type=SW_ResourceCore_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
routine255: BinaryAssociation = BinaryAssociation(
    name="routine255",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature", type=MARTE_SW_Concurrency_EntryPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_EntryPoint", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
entryPoints256: BinaryAssociation = BinaryAssociation(
    name="entryPoints256",
    ends={
        Property(name="SW_Concurrency_MARTE_Element", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource", type=SW_Concurrency_MARTE_Element, multiplicity=Multiplicity(0, 9999))
    }
)
vectorElements301: BinaryAssociation = BinaryAssociation(
    name="vectorElements301",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement302", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
periodElements259: BinaryAssociation = BinaryAssociation(
    name="periodElements259",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement261", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource260", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
priorityElements262: BinaryAssociation = BinaryAssociation(
    name="priorityElements262",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement264", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource263", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
stackSizeElements265: BinaryAssociation = BinaryAssociation(
    name="stackSizeElements265",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement267", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource266", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
activateServices268: BinaryAssociation = BinaryAssociation(
    name="activateServices268",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature270", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource269", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
enableConcurrencyServices271: BinaryAssociation = BinaryAssociation(
    name="enableConcurrencyServices271",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature273", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource272", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
resumeServices274: BinaryAssociation = BinaryAssociation(
    name="resumeServices274",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature276", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource275", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
suspendServices277: BinaryAssociation = BinaryAssociation(
    name="suspendServices277",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature279", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource278", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
terminateServices280: BinaryAssociation = BinaryAssociation(
    name="terminateServices280",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature282", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource281", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
disableConcurrencyServices283: BinaryAssociation = BinaryAssociation(
    name="disableConcurrencyServices283",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature285", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource284", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
shareDataResources286: BinaryAssociation = BinaryAssociation(
    name="shareDataResources286",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement288", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource287", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
messageResources289: BinaryAssociation = BinaryAssociation(
    name="messageResources289",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement291", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource290", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
mutualExclusionResources292: BinaryAssociation = BinaryAssociation(
    name="mutualExclusionResources292",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement294", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource293", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
notificationResources295: BinaryAssociation = BinaryAssociation(
    name="notificationResources295",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement297", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource296", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
heapSizeElements298: BinaryAssociation = BinaryAssociation(
    name="heapSizeElements298",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement300", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource299", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
concurrentResources333: BinaryAssociation = BinaryAssociation(
    name="concurrentResources333",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement334", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
maskElements303: BinaryAssociation = BinaryAssociation(
    name="maskElements303",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement305", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource304", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
routineConnectServices306: BinaryAssociation = BinaryAssociation(
    name="routineConnectServices306",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature308", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource307", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
routineDisconnectServices309: BinaryAssociation = BinaryAssociation(
    name="routineDisconnectServices309",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature311", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource310", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
schedulers312: BinaryAssociation = BinaryAssociation(
    name="schedulers312",
    ends={
        Property(name="SW_Concurrency_MARTE_NamedElement", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource", type=SW_Concurrency_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
deadlineElements313: BinaryAssociation = BinaryAssociation(
    name="deadlineElements313",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement315", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource314", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
deadlineTypeElements316: BinaryAssociation = BinaryAssociation(
    name="deadlineTypeElements316",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement318", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource317", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
timeSliceElements319: BinaryAssociation = BinaryAssociation(
    name="timeSliceElements319",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement321", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource320", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
delayServices322: BinaryAssociation = BinaryAssociation(
    name="delayServices322",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature324", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource323", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
joinServices325: BinaryAssociation = BinaryAssociation(
    name="joinServices325",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature327", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource326", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
yieldServices328: BinaryAssociation = BinaryAssociation(
    name="yieldServices328",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature330", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource329", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
durationElements331: BinaryAssociation = BinaryAssociation(
    name="durationElements331",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement332", type=MARTE_SW_Concurrency_SwTimerResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwTimerResource", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 1))
    }
)
readServices357: BinaryAssociation = BinaryAssociation(
    name="readServices357",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature359", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker358", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
writeServices360: BinaryAssociation = BinaryAssociation(
    name="writeServices360",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature362", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker361", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
memorySpaces335: BinaryAssociation = BinaryAssociation(
    name="memorySpaces335",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement337", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition336", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
fork338: BinaryAssociation = BinaryAssociation(
    name="fork338",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature340", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition339", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
exit341: BinaryAssociation = BinaryAssociation(
    name="exit341",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature343", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition342", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
base_Namespace344: BinaryAssociation = BinaryAssociation(
    name="base_Namespace344",
    ends={
        Property(name="SW_Concurrency_MARTE_Namespace", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition345", type=SW_Concurrency_MARTE_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
timers346: BinaryAssociation = BinaryAssociation(
    name="timers346",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement347", type=MARTE_SW_Concurrency_Alarm, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_Alarm", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
devices348: BinaryAssociation = BinaryAssociation(
    name="devices348",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
closeServices349: BinaryAssociation = BinaryAssociation(
    name="closeServices349",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker350", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
controlServices351: BinaryAssociation = BinaryAssociation(
    name="controlServices351",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature353", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker352", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
openServices354: BinaryAssociation = BinaryAssociation(
    name="openServices354",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature356", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker355", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
memories363: BinaryAssociation = BinaryAssociation(
    name="memories363",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement364", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
memoryBlockAdressElements365: BinaryAssociation = BinaryAssociation(
    name="memoryBlockAdressElements365",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement367", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker366", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
memoryBlockSizeElements368: BinaryAssociation = BinaryAssociation(
    name="memoryBlockSizeElements368",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement370", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker369", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
lockServices371: BinaryAssociation = BinaryAssociation(
    name="lockServices371",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature373", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker372", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
unlockServices374: BinaryAssociation = BinaryAssociation(
    name="unlockServices374",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature376", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker375", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
mapServices377: BinaryAssociation = BinaryAssociation(
    name="mapServices377",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature379", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker378", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
unMapServices380: BinaryAssociation = BinaryAssociation(
    name="unMapServices380",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature382", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker381", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
sendServices393: BinaryAssociation = BinaryAssociation(
    name="sendServices393",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature395", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource394", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
waitingPolicyElements383: BinaryAssociation = BinaryAssociation(
    name="waitingPolicyElements383",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement", type=MARTE_SW_Interaction_SwInteractionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwInteractionResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
readServices384: BinaryAssociation = BinaryAssociation(
    name="readServices384",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature", type=MARTE_SW_Interaction_SharedDataComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SharedDataComResource", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
writeServices385: BinaryAssociation = BinaryAssociation(
    name="writeServices385",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature387", type=MARTE_SW_Interaction_SharedDataComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SharedDataComResource386", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
messageSizeElements388: BinaryAssociation = BinaryAssociation(
    name="messageSizeElements388",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement389", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
messageQueueCapacityElements390: BinaryAssociation = BinaryAssociation(
    name="messageQueueCapacityElements390",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement392", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource391", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
base_Property424: BinaryAssociation = BinaryAssociation(
    name="base_Property424",
    ends={
        Property(name="GCM_MARTE_Property", type=MARTE_GCM_FlowProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_FlowProperty", type=GCM_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
receiveServices396: BinaryAssociation = BinaryAssociation(
    name="receiveServices396",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature398", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource397", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
occurenceCountElements399: BinaryAssociation = BinaryAssociation(
    name="occurenceCountElements399",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement400", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
maskElements401: BinaryAssociation = BinaryAssociation(
    name="maskElements401",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement403", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource402", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
flushServices404: BinaryAssociation = BinaryAssociation(
    name="flushServices404",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature406", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource405", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
signalServices407: BinaryAssociation = BinaryAssociation(
    name="signalServices407",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature409", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource408", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
waitServices410: BinaryAssociation = BinaryAssociation(
    name="waitServices410",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature412", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource411", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
clearServices413: BinaryAssociation = BinaryAssociation(
    name="clearServices413",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature415", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource414", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
accessTokenElements416: BinaryAssociation = BinaryAssociation(
    name="accessTokenElements416",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement417", type=MARTE_SW_Interaction_SwMutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwMutualExclusionResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
releaseServices418: BinaryAssociation = BinaryAssociation(
    name="releaseServices418",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature420", type=MARTE_SW_Interaction_SwMutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwMutualExclusionResource419", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
acquireServices421: BinaryAssociation = BinaryAssociation(
    name="acquireServices421",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature423", type=MARTE_SW_Interaction_SwMutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwMutualExclusionResource422", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
base_Trigger440: BinaryAssociation = BinaryAssociation(
    name="base_Trigger440",
    ends={
        Property(name="GCM_MARTE_Trigger", type=MARTE_GCM_GCMTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMTrigger", type=GCM_MARTE_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
base_Port425: BinaryAssociation = BinaryAssociation(
    name="base_Port425",
    ends={
        Property(name="GCM_MARTE_Port", type=MARTE_GCM_FlowPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_FlowPort", type=GCM_MARTE_Port, multiplicity=Multiplicity(1, 1))
    }
)
base_Port426: BinaryAssociation = BinaryAssociation(
    name="base_Port426",
    ends={
        Property(name="GCM_MARTE_Port427", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort", type=GCM_MARTE_Port, multiplicity=Multiplicity(1, 1))
    }
)
provInterface428: BinaryAssociation = BinaryAssociation(
    name="provInterface428",
    ends={
        Property(name="GCM_MARTE_Interface", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort429", type=GCM_MARTE_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
reqInterface430: BinaryAssociation = BinaryAssociation(
    name="reqInterface430",
    ends={
        Property(name="GCM_MARTE_Interface432", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort431", type=GCM_MARTE_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
featuresSpec433: BinaryAssociation = BinaryAssociation(
    name="featuresSpec433",
    ends={
        Property(name="GCM_ClientServerSpecification", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort434", type=GCM_ClientServerSpecification, multiplicity=Multiplicity(0, 1))
    }
)
base_Interface435: BinaryAssociation = BinaryAssociation(
    name="base_Interface435",
    ends={
        Property(name="GCM_MARTE_Interface436", type=MARTE_GCM_ClientServerSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerSpecification", type=GCM_MARTE_Interface, multiplicity=Multiplicity(1, 1))
    }
)
base_Interface437: BinaryAssociation = BinaryAssociation(
    name="base_Interface437",
    ends={
        Property(name="GCM_MARTE_Interface438", type=MARTE_GCM_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_FlowSpecification", type=GCM_MARTE_Interface, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature439: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature439",
    ends={
        Property(name="GCM_MARTE_BehavioralFeature", type=MARTE_GCM_ClientServerFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerFeature", type=GCM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Behavior468: BinaryAssociation = BinaryAssociation(
    name="base_Behavior468",
    ends={
        Property(name="GQAM_MARTE_Behavior", type=MARTE_GQAM_GaWorkloadGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadGenerator", type=GQAM_MARTE_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
feature441: BinaryAssociation = BinaryAssociation(
    name="feature441",
    ends={
        Property(name="GCM_MARTE_Feature", type=MARTE_GCM_GCMTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMTrigger442", type=GCM_MARTE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
base_InvocationAction443: BinaryAssociation = BinaryAssociation(
    name="base_InvocationAction443",
    ends={
        Property(name="GCM_MARTE_InvocationAction", type=MARTE_GCM_GCMInvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMInvocationAction", type=GCM_MARTE_InvocationAction, multiplicity=Multiplicity(1, 1))
    }
)
onFeature444: BinaryAssociation = BinaryAssociation(
    name="onFeature444",
    ends={
        Property(name="GCM_MARTE_Feature446", type=MARTE_GCM_GCMInvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMInvocationAction445", type=GCM_MARTE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
base_AnyReceiveEvent447: BinaryAssociation = BinaryAssociation(
    name="base_AnyReceiveEvent447",
    ends={
        Property(name="GCM_MARTE_AnyReceiveEvent", type=MARTE_GCM_DataEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataEvent", type=GCM_MARTE_AnyReceiveEvent, multiplicity=Multiplicity(1, 1))
    }
)
classifier448: BinaryAssociation = BinaryAssociation(
    name="classifier448",
    ends={
        Property(name="GCM_MARTE_Classifier", type=MARTE_GCM_DataEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataEvent449", type=GCM_MARTE_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Property450: BinaryAssociation = BinaryAssociation(
    name="base_Property450",
    ends={
        Property(name="GCM_MARTE_Property451", type=MARTE_GCM_DataPool, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataPool", type=GCM_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
insertion452: BinaryAssociation = BinaryAssociation(
    name="insertion452",
    ends={
        Property(name="GCM_MARTE_Behavior", type=MARTE_GCM_DataPool, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataPool453", type=GCM_MARTE_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
selection454: BinaryAssociation = BinaryAssociation(
    name="selection454",
    ends={
        Property(name="GCM_MARTE_Behavior456", type=MARTE_GCM_DataPool, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataPool455", type=GCM_MARTE_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
base_Behavior457: BinaryAssociation = BinaryAssociation(
    name="base_Behavior457",
    ends={
        Property(name="GCM_MARTE_Behavior458", type=MARTE_GCM_GCMInvocatingBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMInvocatingBehavior", type=GCM_MARTE_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
onPorts459: BinaryAssociation = BinaryAssociation(
    name="onPorts459",
    ends={
        Property(name="GCM_MARTE_Port461", type=MARTE_GCM_GCMInvocatingBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMInvocatingBehavior460", type=GCM_MARTE_Port, multiplicity=Multiplicity(0, 9999))
    }
)
onFeatures462: BinaryAssociation = BinaryAssociation(
    name="onFeatures462",
    ends={
        Property(name="GCM_MARTE_Feature464", type=MARTE_GCM_GCMInvocatingBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMInvocatingBehavior463", type=GCM_MARTE_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
invocations465: BinaryAssociation = BinaryAssociation(
    name="invocations465",
    ends={
        Property(name="GCM_MARTE_InvocationAction467", type=MARTE_GCM_GCMInvocatingBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMInvocatingBehavior466", type=GCM_MARTE_InvocationAction, multiplicity=Multiplicity(0, 9999))
    }
)
root481: BinaryAssociation = BinaryAssociation(
    name="root481",
    ends={
        Property(name="GQAM_GaStep", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario482", type=GQAM_GaStep, multiplicity=Multiplicity(0, 1))
    }
)
base_NamedElement469: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement469",
    ends={
        Property(name="GQAM_MARTE_NamedElement", type=MARTE_GQAM_GaEventTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaEventTrace", type=GQAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
generator470: BinaryAssociation = BinaryAssociation(
    name="generator470",
    ends={
        Property(name="GQAM_GaWorkloadGenerator", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent", type=GQAM_GaWorkloadGenerator, multiplicity=Multiplicity(0, 1))
    }
)
trace471: BinaryAssociation = BinaryAssociation(
    name="trace471",
    ends={
        Property(name="GQAM_GaEventTrace", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent472", type=GQAM_GaEventTrace, multiplicity=Multiplicity(0, 1))
    }
)
effect473: BinaryAssociation = BinaryAssociation(
    name="effect473",
    ends={
        Property(name="GQAM_GaScenario", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent474", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 1))
    }
)
timedEvent475: BinaryAssociation = BinaryAssociation(
    name="timedEvent475",
    ends={
        Property(name="GQAM_MARTE_TimeEvent", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent476", type=GQAM_MARTE_TimeEvent, multiplicity=Multiplicity(0, 1))
    }
)
base_NamedElement477: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement477",
    ends={
        Property(name="GQAM_MARTE_NamedElement479", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent478", type=GQAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
cause480: BinaryAssociation = BinaryAssociation(
    name="cause480",
    ends={
        Property(name="GQAM_GaWorkloadEvent", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario", type=GQAM_GaWorkloadEvent, multiplicity=Multiplicity(0, 1))
    }
)
servDemand491: BinaryAssociation = BinaryAssociation(
    name="servDemand491",
    ends={
        Property(name="GQAM_GaRequestedService", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep492", type=GQAM_GaRequestedService, multiplicity=Multiplicity(0, 9999))
    }
)
steps483: BinaryAssociation = BinaryAssociation(
    name="steps483",
    ends={
        Property(name="GaStep", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="scenario", type=GQAM_GaStep, multiplicity=Multiplicity(1, 9999))
    }
)
parentStep484: BinaryAssociation = BinaryAssociation(
    name="parentStep484",
    ends={
        Property(name="GaStep485", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="childScenario", type=GQAM_GaStep, multiplicity=Multiplicity(1, 9999))
    }
)
timing486: BinaryAssociation = BinaryAssociation(
    name="timing486",
    ends={
        Property(name="GQAM_GaTimedObs", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario487", type=GQAM_GaTimedObs, multiplicity=Multiplicity(0, 9999))
    }
)
concurRes488: BinaryAssociation = BinaryAssociation(
    name="concurRes488",
    ends={
        Property(name="GRM_SchedulableResource", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 1))
    }
)
endObs498: BinaryAssociation = BinaryAssociation(
    name="endObs498",
    ends={
        Property(name="GQAM_MARTE_TimeObservation500", type=MARTE_GQAM_GaTimedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaTimedObs499", type=GQAM_MARTE_TimeObservation, multiplicity=Multiplicity(0, 9999))
    }
)
host489: BinaryAssociation = BinaryAssociation(
    name="host489",
    ends={
        Property(name="GQAM_GaExecHost", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep490", type=GQAM_GaExecHost, multiplicity=Multiplicity(0, 1))
    }
)
scenario493: BinaryAssociation = BinaryAssociation(
    name="scenario493",
    ends={
        Property(name="GaScenario", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="steps", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 1))
    }
)
childScenario494: BinaryAssociation = BinaryAssociation(
    name="childScenario494",
    ends={
        Property(name="GaScenario495", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="parentStep", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 1))
    }
)
base_Operation496: BinaryAssociation = BinaryAssociation(
    name="base_Operation496",
    ends={
        Property(name="GQAM_MARTE_Operation", type=MARTE_GQAM_GaRequestedService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaRequestedService", type=GQAM_MARTE_Operation, multiplicity=Multiplicity(1, 1))
    }
)
startObs497: BinaryAssociation = BinaryAssociation(
    name="startObs497",
    ends={
        Property(name="GQAM_MARTE_TimeObservation", type=MARTE_GQAM_GaTimedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaTimedObs", type=GQAM_MARTE_TimeObservation, multiplicity=Multiplicity(0, 9999))
    }
)
behavior505: BinaryAssociation = BinaryAssociation(
    name="behavior505",
    ends={
        Property(name="MARTE_GQAM_GaWorkloadBehavior", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 9999)),
        Property(name="GQAM_GaScenario506", type=MARTE_GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 1))
    }
)
demand507: BinaryAssociation = BinaryAssociation(
    name="demand507",
    ends={
        Property(name="GQAM_GaWorkloadEvent509", type=MARTE_GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadBehavior508", type=GQAM_GaWorkloadEvent, multiplicity=Multiplicity(0, 9999))
    }
)
acqRes501: BinaryAssociation = BinaryAssociation(
    name="acqRes501",
    ends={
        Property(name="GRM_Resource502", type=MARTE_GQAM_GaAcqStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAcqStep", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)
relRes503: BinaryAssociation = BinaryAssociation(
    name="relRes503",
    ends={
        Property(name="GRM_Resource504", type=MARTE_GQAM_GaRelStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaRelStep", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)
base_NamedElement522: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement522",
    ends={
        Property(name="SAM_MARTE_NamedElement", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow523", type=SAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
base_NamedElement510: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement510",
    ends={
        Property(name="GQAM_MARTE_NamedElement512", type=MARTE_GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadBehavior511", type=GQAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
workload513: BinaryAssociation = BinaryAssociation(
    name="workload513",
    ends={
        Property(name="GQAM_GaWorkloadBehavior", type=MARTE_GQAM_GaAnalysisContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAnalysisContext", type=GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 9999))
    }
)
platform514: BinaryAssociation = BinaryAssociation(
    name="platform514",
    ends={
        Property(name="GQAM_GaResourcesPlatform", type=MARTE_GQAM_GaAnalysisContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAnalysisContext515", type=GQAM_GaResourcesPlatform, multiplicity=Multiplicity(1, 9999))
    }
)
resources516: BinaryAssociation = BinaryAssociation(
    name="resources516",
    ends={
        Property(name="GRM_Resource517", type=MARTE_GQAM_GaResourcesPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaResourcesPlatform", type=GRM_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
base_Classifier518: BinaryAssociation = BinaryAssociation(
    name="base_Classifier518",
    ends={
        Property(name="GQAM_MARTE_Classifier", type=MARTE_GQAM_GaResourcesPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaResourcesPlatform519", type=GQAM_MARTE_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
timing520: BinaryAssociation = BinaryAssociation(
    name="timing520",
    ends={
        Property(name="GQAM_GaTimedObs521", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow", type=GQAM_GaTimedObs, multiplicity=Multiplicity(0, 9999))
    }
)
base_BehavioralFeature524: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature524",
    ends={
        Property(name="SAM_MARTE_BehavioralFeature", type=MARTE_SAM_SaCommStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommStep", type=SAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature525: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature525",
    ends={
        Property(name="SAM_MARTE_BehavioralFeature526", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep", type=SAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
sharedRes527: BinaryAssociation = BinaryAssociation(
    name="sharedRes527",
    ends={
        Property(name="SAM_SaSharedResource", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep528", type=SAM_SaSharedResource, multiplicity=Multiplicity(0, 9999))
    }
)
instance533: BinaryAssociation = BinaryAssociation(
    name="instance533",
    ends={
        Property(name="GRM_SchedulableResource534", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 1))
    }
)
host535: BinaryAssociation = BinaryAssociation(
    name="host535",
    ends={
        Property(name="GQAM_GaExecHost537", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance536", type=GQAM_GaExecHost, multiplicity=Multiplicity(0, 1))
    }
)
base_NamedElement538: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement538",
    ends={
        Property(name="PAM_MARTE_NamedElement", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance539", type=PAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
behavDemand529: BinaryAssociation = BinaryAssociation(
    name="behavDemand529",
    ends={
        Property(name="GQAM_GaScenario530", type=MARTE_PAM_PaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaStep", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 9999))
    }
)
resource531: BinaryAssociation = BinaryAssociation(
    name="resource531",
    ends={
        Property(name="GRM_Resource532", type=MARTE_PAM_PaResPassStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaResPassStep", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_MARTE_NFPs_NfpType_TupleType = Generalization(general=TupleType, specific=MARTE_NFPs_NfpType)
gen_MARTE_Time_TimedValueSpecification_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedValueSpecification)
gen_MARTE_Time_TimedConstraint_NFPs_NfpConstraint = Generalization(general=NFPs_NfpConstraint, specific=MARTE_Time_TimedConstraint)
gen_MARTE_Time_TimedConstraint_Time_TimedElement = Generalization(general=Time_TimedElement, specific=MARTE_Time_TimedConstraint)
gen_MARTE_Time_ClockConstraint_NFPs_NfpConstraint = Generalization(general=NFPs_NfpConstraint, specific=MARTE_Time_ClockConstraint)
gen_MARTE_Time_ClockConstraint_Time_TimedElement = Generalization(general=Time_TimedElement, specific=MARTE_Time_ClockConstraint)
gen_MARTE_Time_TimedInstantObservation_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedInstantObservation)
gen_MARTE_Time_TimedDurationObservation_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedDurationObservation)
gen_MARTE_Time_TimedEvent_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedEvent)
gen_MARTE_Time_TimedProcessing_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedProcessing)
gen_MARTE_GRM_StorageResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_StorageResource)
gen_MARTE_GRM_CommunicationEndPoint_Resource = Generalization(general=Resource, specific=MARTE_GRM_CommunicationEndPoint)
gen_MARTE_GRM_SynchronizationResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_SynchronizationResource)
gen_MARTE_GRM_ConcurrencyResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_ConcurrencyResource)
gen_MARTE_GRM_Scheduler_Resource = Generalization(general=Resource, specific=MARTE_GRM_Scheduler)
gen_MARTE_GRM_ProcessingResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_ProcessingResource)
gen_MARTE_GRM_ComputingResource_ProcessingResource = Generalization(general=ProcessingResource, specific=MARTE_GRM_ComputingResource)
gen_MARTE_GRM_MutualExclusionResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_MutualExclusionResource)
gen_MARTE_GRM_SchedulableResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_SchedulableResource)
gen_MARTE_GRM_SecondaryScheduler_Scheduler = Generalization(general=Scheduler, specific=MARTE_GRM_SecondaryScheduler)
gen_MARTE_GRM_CommunicationMedia_ProcessingResource = Generalization(general=ProcessingResource, specific=MARTE_GRM_CommunicationMedia)
gen_MARTE_GRM_DeviceResource_ProcessingResource = Generalization(general=ProcessingResource, specific=MARTE_GRM_DeviceResource)
gen_MARTE_GRM_TimingResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_TimingResource)
gen_MARTE_GRM_ClockResource_TimingResource = Generalization(general=TimingResource, specific=MARTE_GRM_ClockResource)
gen_MARTE_GRM_TimerResource_TimingResource = Generalization(general=TimingResource, specific=MARTE_GRM_TimerResource)
gen_MARTE_GRM_Release_GrService = Generalization(general=GrService, specific=MARTE_GRM_Release)
gen_MARTE_GRM_Acquire_GrService = Generalization(general=GrService, specific=MARTE_GRM_Acquire)
gen_MARTE_RSM_DefaultLink_LinkTopology = Generalization(general=LinkTopology, specific=MARTE_RSM_DefaultLink)
gen_MARTE_RSM_InterRepetition_LinkTopology = Generalization(general=LinkTopology, specific=MARTE_RSM_InterRepetition)
gen_MARTE_RSM_Distribute_Allocate = Generalization(general=Allocate, specific=MARTE_RSM_Distribute)
gen_MARTE_RSM_Reshape_LinkTopology = Generalization(general=LinkTopology, specific=MARTE_RSM_Reshape)
gen_MARTE_RSM_Tiler_LinkTopology = Generalization(general=LinkTopology, specific=MARTE_RSM_Tiler)
gen_MARTE_HwComputing_HwProcessor_HwComputingResource = Generalization(general=HwComputingResource, specific=MARTE_HwComputing_HwProcessor)
gen_MARTE_HwCommunication_HwCommunicationResource_HwResource = Generalization(general=HwResource, specific=MARTE_HwCommunication_HwCommunicationResource)
gen_MARTE_HwCommunication_HwArbiter_HwCommunicationResource = Generalization(general=HwCommunicationResource, specific=MARTE_HwCommunication_HwArbiter)
gen_MARTE_HwComputing_HwComputingResource_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwComputing_HwComputingResource)
gen_MARTE_HwComputing_HwComputingResource_GRM_ComputingResource = Generalization(general=GRM_ComputingResource, specific=MARTE_HwComputing_HwComputingResource)
gen_MARTE_HwComputing_HwISA_HwResource = Generalization(general=HwResource, specific=MARTE_HwComputing_HwISA)
gen_MARTE_HwComputing_HwBranchPredictor_HwResource = Generalization(general=HwResource, specific=MARTE_HwComputing_HwBranchPredictor)
gen_MARTE_HwComputing_HwASIC_HwComputingResource = Generalization(general=HwComputingResource, specific=MARTE_HwComputing_HwASIC)
gen_MARTE_HwComputing_HwPLD_HwComputingResource = Generalization(general=HwComputingResource, specific=MARTE_HwComputing_HwPLD)
gen_MARTE_HwStorageManager_HwMMU_HwStorageManager = Generalization(general=HwStorageManager, specific=MARTE_HwStorageManager_HwMMU)
gen_MARTE_HwCommunication_HwMedia_GRM_CommunicationMedia = Generalization(general=GRM_CommunicationMedia, specific=MARTE_HwCommunication_HwMedia)
gen_MARTE_HwCommunication_HwMedia_HwCommunication_HwCommunicationResource = Generalization(general=HwCommunication_HwCommunicationResource, specific=MARTE_HwCommunication_HwMedia)
gen_MARTE_HwCommunication_HwBus_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwCommunication_HwBus)
gen_MARTE_HwCommunication_HwBridge_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwCommunication_HwBridge)
gen_MARTE_HwCommunication_HwEndPoint_HwCommunication_HwCommunicationResource = Generalization(general=HwCommunication_HwCommunicationResource, specific=MARTE_HwCommunication_HwEndPoint)
gen_MARTE_HwCommunication_HwEndPoint_GRM_CommunicationEndPoint = Generalization(general=GRM_CommunicationEndPoint, specific=MARTE_HwCommunication_HwEndPoint)
gen_MARTE_HwStorageManager_HwStorageManager_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwStorageManager_HwStorageManager)
gen_MARTE_HwStorageManager_HwStorageManager_GRM_StorageResource = Generalization(general=GRM_StorageResource, specific=MARTE_HwStorageManager_HwStorageManager)
gen_MARTE_HwStorageManager_HwDMA_HwStorageManager_HwStorageManager = Generalization(general=HwStorageManager_HwStorageManager, specific=MARTE_HwStorageManager_HwDMA)
gen_MARTE_HwStorageManager_HwDMA_HwCommunication_HwArbiter = Generalization(general=HwCommunication_HwArbiter, specific=MARTE_HwStorageManager_HwDMA)
gen_MARTE_HwMemory_HwMemory_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwMemory_HwMemory)
gen_MARTE_HwMemory_HwMemory_GRM_StorageResource = Generalization(general=GRM_StorageResource, specific=MARTE_HwMemory_HwMemory)
gen_MARTE_HwMemory_HwRAM_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwRAM)
gen_MARTE_HwDevice_HwDevice_GRM_DeviceResource = Generalization(general=GRM_DeviceResource, specific=MARTE_HwDevice_HwDevice)
gen_MARTE_HwDevice_HwI_O_HwDevice = Generalization(general=HwDevice, specific=MARTE_HwDevice_HwI_O)
gen_MARTE_HwDevice_HwSupport_HwDevice = Generalization(general=HwDevice, specific=MARTE_HwDevice_HwSupport)
gen_MARTE_HwMemory_HwROM_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwROM)
gen_MARTE_HwMemory_HwDrive_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwDrive)
gen_MARTE_HwMemory_HwCache_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwCache)
gen_MARTE_HwTiming_HwTimingResource_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwTiming_HwTimingResource)
gen_MARTE_HwTiming_HwTimingResource_GRM_TimingResource = Generalization(general=GRM_TimingResource, specific=MARTE_HwTiming_HwTimingResource)
gen_MARTE_HwTiming_HwClock_HwTimingResource = Generalization(general=HwTimingResource, specific=MARTE_HwTiming_HwClock)
gen_MARTE_HwTiming_HwTimer_HwTimingResource = Generalization(general=HwTimingResource, specific=MARTE_HwTiming_HwTimer)
gen_MARTE_HwDevice_HwDevice_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwDevice_HwDevice)
gen_MARTE_HwDevice_HWActuator_HwI_O = Generalization(general=HwI_O, specific=MARTE_HwDevice_HWActuator)
gen_MARTE_HwDevice_HWSensor_HwI_O = Generalization(general=HwI_O, specific=MARTE_HwDevice_HWSensor)
gen_MARTE_HwGeneral_HwResourceService_GrService = Generalization(general=GrService, specific=MARTE_HwGeneral_HwResourceService)
gen_MARTE_HwGeneral_HwResource_Resource = Generalization(general=Resource, specific=MARTE_HwGeneral_HwResource)
gen_MARTE_HwLayout_HwComponent_HwResource = Generalization(general=HwResource, specific=MARTE_HwLayout_HwComponent)
gen_MARTE_SW_ResourceCore_SwResource_Resource = Generalization(general=Resource, specific=MARTE_SW_ResourceCore_SwResource)
gen_MARTE_HwPower_HwPowerSupply_HwComponent = Generalization(general=HwComponent, specific=MARTE_HwPower_HwPowerSupply)
gen_MARTE_HwPower_HwCoolingSupply_HwComponent = Generalization(general=HwComponent, specific=MARTE_HwPower_HwCoolingSupply)
gen_MARTE_SW_ResourceCore_SwAccessService_GrService = Generalization(general=GrService, specific=MARTE_SW_ResourceCore_SwAccessService)
gen_MARTE_SW_Concurrency_EntryPoint_Allocate = Generalization(general=Allocate, specific=MARTE_SW_Concurrency_EntryPoint)
gen_MARTE_SW_Concurrency_SwConcurrentResource_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Concurrency_SwConcurrentResource)
gen_MARTE_SW_Concurrency_InterruptResource_SwConcurrentResource = Generalization(general=SwConcurrentResource, specific=MARTE_SW_Concurrency_InterruptResource)
gen_MARTE_SW_Concurrency_MemoryPartition_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Concurrency_MemoryPartition)
gen_MARTE_SW_Concurrency_SwSchedulableResource_SW_Concurrency_SwConcurrentResource = Generalization(general=SW_Concurrency_SwConcurrentResource, specific=MARTE_SW_Concurrency_SwSchedulableResource)
gen_MARTE_SW_Concurrency_SwSchedulableResource_GRM_SchedulableResource = Generalization(general=GRM_SchedulableResource, specific=MARTE_SW_Concurrency_SwSchedulableResource)
gen_MARTE_SW_Concurrency_SwTimerResource_TimerResource = Generalization(general=TimerResource, specific=MARTE_SW_Concurrency_SwTimerResource)
gen_MARTE_SW_Concurrency_Alarm_InterruptResource = Generalization(general=InterruptResource, specific=MARTE_SW_Concurrency_Alarm)
gen_MARTE_SW_Brokering_DeviceBroker_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Brokering_DeviceBroker)
gen_MARTE_SW_Brokering_MemoryBroker_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Brokering_MemoryBroker)
gen_MARTE_SW_Interaction_SwInteractionResource_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Interaction_SwInteractionResource)
gen_MARTE_SW_Interaction_SwCommunicationResource_SW_Interaction_SwInteractionResource = Generalization(general=SW_Interaction_SwInteractionResource, specific=MARTE_SW_Interaction_SwCommunicationResource)
gen_MARTE_SW_Interaction_SwCommunicationResource_GRM_CommunicationMedia = Generalization(general=GRM_CommunicationMedia, specific=MARTE_SW_Interaction_SwCommunicationResource)
gen_MARTE_SW_Interaction_SwSynchronizationResource_SW_Interaction_SwInteractionResource = Generalization(general=SW_Interaction_SwInteractionResource, specific=MARTE_SW_Interaction_SwSynchronizationResource)
gen_MARTE_SW_Interaction_SwSynchronizationResource_GRM_SynchronizationResource = Generalization(general=GRM_SynchronizationResource, specific=MARTE_SW_Interaction_SwSynchronizationResource)
gen_MARTE_SW_Interaction_SharedDataComResource_SwCommunicationResource = Generalization(general=SwCommunicationResource, specific=MARTE_SW_Interaction_SharedDataComResource)
gen_MARTE_SW_Interaction_MessageComResource_SwCommunicationResource = Generalization(general=SwCommunicationResource, specific=MARTE_SW_Interaction_MessageComResource)
gen_MARTE_SW_Interaction_NotificationResource_SwSynchronizationResource = Generalization(general=SwSynchronizationResource, specific=MARTE_SW_Interaction_NotificationResource)
gen_MARTE_SW_Interaction_SwMutualExclusionResource_SW_Interaction_SwSynchronizationResource = Generalization(general=SW_Interaction_SwSynchronizationResource, specific=MARTE_SW_Interaction_SwMutualExclusionResource)
gen_MARTE_SW_Interaction_SwMutualExclusionResource_GRM_MutualExclusionResource = Generalization(general=GRM_MutualExclusionResource, specific=MARTE_SW_Interaction_SwMutualExclusionResource)
gen_MARTE_GQAM_GaScenario_GRM_ResourceUsage = Generalization(general=GRM_ResourceUsage, specific=MARTE_GQAM_GaScenario)
gen_MARTE_GQAM_GaScenario_Time_TimedProcessing = Generalization(general=Time_TimedProcessing, specific=MARTE_GQAM_GaScenario)
gen_MARTE_GQAM_GaStep_GaScenario = Generalization(general=GaScenario, specific=MARTE_GQAM_GaStep)
gen_MARTE_GQAM_GaExecHost_GRM_Scheduler = Generalization(general=GRM_Scheduler, specific=MARTE_GQAM_GaExecHost)
gen_MARTE_GQAM_GaExecHost_GRM_ComputingResource = Generalization(general=GRM_ComputingResource, specific=MARTE_GQAM_GaExecHost)
gen_MARTE_GQAM_GaRequestedService_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaRequestedService)
gen_MARTE_GQAM_GaTimedObs_NfpConstraint = Generalization(general=NfpConstraint, specific=MARTE_GQAM_GaTimedObs)
gen_MARTE_GQAM_GaCommStep_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaCommStep)
gen_MARTE_GQAM_GaAcqStep_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaAcqStep)
gen_MARTE_GQAM_GaRelStep_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaRelStep)
gen_MARTE_GQAM_GaLatencyObs_GaTimedObs = Generalization(general=GaTimedObs, specific=MARTE_GQAM_GaLatencyObs)
gen_MARTE_GQAM_GaCommHost_GRM_CommunicationMedia = Generalization(general=GRM_CommunicationMedia, specific=MARTE_GQAM_GaCommHost)
gen_MARTE_GQAM_GaCommHost_GRM_Scheduler = Generalization(general=GRM_Scheduler, specific=MARTE_GQAM_GaCommHost)
gen_MARTE_GQAM_GaCommChannel_SchedulableResource = Generalization(general=SchedulableResource, specific=MARTE_GQAM_GaCommChannel)
gen_MARTE_GQAM_GaAnalysisContext_CoreElements_Configuration = Generalization(general=CoreElements_Configuration, specific=MARTE_GQAM_GaAnalysisContext)
gen_MARTE_GQAM_GaAnalysisContext_Variables_ExpressionContext = Generalization(general=Variables_ExpressionContext, specific=MARTE_GQAM_GaAnalysisContext)
gen_MARTE_SAM_SaAnalysisContext_GaAnalysisContext = Generalization(general=GaAnalysisContext, specific=MARTE_SAM_SaAnalysisContext)
gen_MARTE_SAM_SaSchedObs_GaTimedObs = Generalization(general=GaTimedObs, specific=MARTE_SAM_SaSchedObs)
gen_MARTE_SAM_SaCommStep_GaCommStep = Generalization(general=GaCommStep, specific=MARTE_SAM_SaCommStep)
gen_MARTE_SAM_SaStep_GaStep = Generalization(general=GaStep, specific=MARTE_SAM_SaStep)
gen_MARTE_SAM_SaSharedResource_MutualExclusionResource = Generalization(general=MutualExclusionResource, specific=MARTE_SAM_SaSharedResource)
gen_MARTE_SAM_SaCommHost_GaCommHost = Generalization(general=GaCommHost, specific=MARTE_SAM_SaCommHost)
gen_MARTE_SAM_SaExecHost_GaExecHost = Generalization(general=GaExecHost, specific=MARTE_SAM_SaExecHost)
gen_MARTE_PAM_PaStep_GaStep = Generalization(general=GaStep, specific=MARTE_PAM_PaStep)
gen_MARTE_PAM_PaLogicalResource_Resource = Generalization(general=Resource, specific=MARTE_PAM_PaLogicalResource)
gen_MARTE_PAM_PaRequestedStep_PAM_PaStep = Generalization(general=PAM_PaStep, specific=MARTE_PAM_PaRequestedStep)
gen_MARTE_PAM_PaRequestedStep_GQAM_GaRequestedService = Generalization(general=GQAM_GaRequestedService, specific=MARTE_PAM_PaRequestedStep)
gen_MARTE_PAM_PaCommStep_PAM_PaStep = Generalization(general=PAM_PaStep, specific=MARTE_PAM_PaCommStep)
gen_MARTE_PAM_PaCommStep_GQAM_GaCommStep = Generalization(general=GQAM_GaCommStep, specific=MARTE_PAM_PaCommStep)
gen_MARTE_PAM_PaResPassStep_GaStep = Generalization(general=GaStep, specific=MARTE_PAM_PaResPassStep)

# Domain Model
domain_model = DomainModel(
    name="MARTE",
    types={MARTE_NFPs_Nfp, NFPs_MARTE_Property, MARTE_NFPs_Unit, NFPs_Unit, NFPs_MARTE_EnumerationLiteral, MARTE_NFPs_NfpConstraint, NFPs_MARTE_Constraint, MARTE_NFPs_Dimension, NFPs_Dimension, NFPs_MARTE_Enumeration, MARTE_CoreElements_ModeTransition, CoreElements_MARTE_Transition, MARTE_CoreElements_ModeBehavior, CoreElements_MARTE_StateMachine, MARTE_CoreElements_Configuration, CoreElements_MARTE_StructuredClassifier, CoreElements_MARTE_Package, MARTE_CoreElements_Mode, CoreElements_MARTE_State, MARTE_Alloc_Allocated, Alloc_MARTE_NamedElement, CoreElements_Mode, MARTE_NFPs_NfpType, TupleType, Alloc_MARTE_Dependency, MARTE_Alloc_AllocateActivityGroup, Alloc_MARTE_ActivityPartition, Alloc_Allocated, MARTE_Alloc_NfpRefine, MARTE_Alloc_Allocate, NFPs_NfpConstraint, MARTE_Alloc_Assign, Alloc_MARTE_Element, Alloc_MARTE_Comment, Time_MARTE_Enumeration, Alloc_MARTE_Abstraction, MARTE_Time_TimedDomain, Time_MARTE_Namespace, MARTE_Time_Clock, Time_MARTE_InstanceSpecification, Time_ClockType, Time_MARTE_Property, Time_MARTE_Event, MARTE_Time_ClockType, Time_MARTE_Operation, Time_MARTE_Class, MARTE_Time_TimedElement, Time_Clock, MARTE_Time_TimedValueSpecification, TimedElement, Time_MARTE_ValueSpecification, MARTE_Time_TimedConstraint, Time_TimedElement, MARTE_Time_ClockConstraint, MARTE_Time_TimedInstantObservation, Time_MARTE_TimeObservation, MARTE_Time_TimedDurationObservation, Time_MARTE_DurationObservation, MARTE_Time_TimedEvent, Time_MARTE_TimeEvent, MARTE_Time_TimedProcessing, Time_MARTE_Action, GRM_MARTE_ConnectableElement, Time_MARTE_Behavior, Time_MARTE_Message, MARTE_GRM_Resource, GRM_MARTE_Property, GRM_MARTE_InstanceSpecification, GRM_MARTE_Classifier, GRM_MARTE_Lifeline, MARTE_GRM_StorageResource, Resource, MARTE_GRM_CommunicationEndPoint, MARTE_GRM_SynchronizationResource, MARTE_GRM_ConcurrencyResource, MARTE_GRM_Scheduler, GRM_ProcessingResource, GRM_ComputingResource, GRM_MutualExclusionResource, GRM_SchedulableResource, MARTE_GRM_ProcessingResource, GRM_Scheduler, MARTE_GRM_ComputingResource, ProcessingResource, MARTE_GRM_MutualExclusionResource, MARTE_GRM_SchedulableResource, GRM_SecondaryScheduler, MARTE_GRM_SecondaryScheduler, Scheduler, MARTE_GRM_CommunicationMedia, GRM_MARTE_Connector, MARTE_GRM_ResourceUsage, MARTE_GRM_DeviceResource, MARTE_GRM_TimingResource, MARTE_GRM_ClockResource, TimingResource, MARTE_GRM_TimerResource, MARTE_GRM_GrService, GRM_Resource, GRM_MARTE_ExecutionSpecification, GRM_MARTE_BehavioralFeature, GRM_MARTE_Behavior, GRM_MARTE_Collaboration, GRM_MARTE_CollaborationUse, MARTE_GRM_Release, GrService, MARTE_GRM_Acquire, RSM_MARTE_ConnectorEnd, GRM_MARTE_NamedElement, GRM_ResourceUsage, MARTE_RSM_LinkTopology, RSM_MARTE_Connector, MARTE_RSM_DefaultLink, LinkTopology, MARTE_RSM_InterRepetition, MARTE_RSM_Distribute, Allocate, MARTE_RSM_Reshape, MARTE_RSM_Tiler, DataTypes_MARTE_Property, MARTE_RSM_Shaped, RSM_MARTE_MultiplicityElement, MARTE_Variables_Var, Variables_MARTE_Property, MARTE_Variables_ExpressionContext, Variables_MARTE_NamedElement, MARTE_Operators_Operator, Operators_MARTE_Behavior, MARTE_DataTypes_BoundedSubtype, DataTypes_MARTE_DataType, MARTE_DataTypes_IntervalType, HLAM_MARTE_BehavioredClassifier, MARTE_DataTypes_CollectionType, MARTE_DataTypes_ChoiceType, MARTE_DataTypes_TupleType, MARTE_HLAM_RtUnit, HLAM_MARTE_Behavior, HLAM_MARTE_Operation, MARTE_HLAM_PpUnit, MARTE_HLAM_RtFeature, HLAM_MARTE_BehavioralFeature, HLAM_MARTE_Message, HLAM_MARTE_Signal, HLAM_MARTE_Port, HLAM_MARTE_InvocationAction, HLAM_RtSpecification, MARTE_HLAM_RtSpecification, Time_TimedInstantObservation, HLAM_MARTE_Comment, MARTE_HLAM_RtAction, MARTE_HLAM_RtService, HwStorageManager_HwMMU, MARTE_HwComputing_HwProcessor, HwComputingResource, HwComputing_HwISA, HwComputing_HwBranchPredictor, HwMemory_HwCache, MARTE_HwCommunication_HwArbiter, HwCommunicationResource, HwCommunication_HwMedia, MARTE_HwComputing_HwComputingResource, HwGeneral_HwResource, MARTE_HwComputing_HwISA, HwResource, MARTE_HwComputing_HwBranchPredictor, MARTE_HwComputing_HwASIC, MARTE_HwComputing_HwPLD, HwMemory_HwRAM, HwComputing_HwComputingResource, MARTE_HwCommunication_HwCommunicationResource, MARTE_HwStorageManager_HwMMU, HwStorageManager, MARTE_HwCommunication_HwMedia, GRM_CommunicationMedia, HwCommunication_HwCommunicationResource, HwCommunication_HwArbiter, MARTE_HwCommunication_HwBus, HwMedia, MARTE_HwCommunication_HwBridge, MARTE_HwCommunication_HwEndPoint, GRM_CommunicationEndPoint, MARTE_HwStorageManager_HwStorageManager, GRM_StorageResource, HwMemory_HwMemory, MARTE_HwStorageManager_HwDMA, HwStorageManager_HwStorageManager, HwComputing_HwProcessor, MARTE_HwMemory_HwMemory, MARTE_HwMemory_HwRAM, HwMemory, GRM_DeviceResource, MARTE_HwDevice_HwI_O, HwDevice, MARTE_HwDevice_HwSupport, MARTE_HwMemory_HwROM, MARTE_HwMemory_HwDrive, MARTE_HwMemory_HwCache, MARTE_HwTiming_HwTimingResource, GRM_TimingResource, MARTE_HwTiming_HwClock, HwTimingResource, MARTE_HwTiming_HwTimer, HwTiming_HwClock, MARTE_HwDevice_HwDevice, MARTE_HwDevice_HWActuator, HwI_O, MARTE_HwDevice_HWSensor, MARTE_HwGeneral_HwResourceService, MARTE_HwGeneral_HwResource, HwGeneral_HwResourceService, HwCommunication_HwEndPoint, MARTE_HwLayout_HwComponent, MARTE_SW_ResourceCore_SwResource, HwLayout_HwComponent, MARTE_HwPower_HwPowerSupply, HwComponent, MARTE_HwPower_HwCoolingSupply, SW_Concurrency_MARTE_TypedElement, SW_ResourceCore_MARTE_TypedElement, SW_ResourceCore_MARTE_BehavioralFeature, MARTE_SW_ResourceCore_SwAccessService, SW_ResourceCore_MARTE_Property, MARTE_SW_Concurrency_EntryPoint, SW_Concurrency_MARTE_BehavioralFeature, MARTE_SW_Concurrency_SwConcurrentResource, SwResource, SW_Concurrency_MARTE_Element, MARTE_SW_Concurrency_InterruptResource, SwConcurrentResource, MARTE_SW_Concurrency_MemoryPartition, MARTE_SW_Concurrency_SwSchedulableResource, SW_Concurrency_SwConcurrentResource, SW_Concurrency_MARTE_NamedElement, MARTE_SW_Concurrency_SwTimerResource, TimerResource, SW_Concurrency_MARTE_Namespace, MARTE_SW_Concurrency_Alarm, InterruptResource, MARTE_SW_Brokering_DeviceBroker, SW_Brokering_MARTE_TypedElement, SW_Brokering_MARTE_BehavioralFeature, MARTE_SW_Brokering_MemoryBroker, MARTE_SW_Interaction_SwInteractionResource, SW_Interaction_MARTE_TypedElement, MARTE_SW_Interaction_SwCommunicationResource, SW_Interaction_SwInteractionResource, MARTE_SW_Interaction_SwSynchronizationResource, GRM_SynchronizationResource, MARTE_SW_Interaction_SharedDataComResource, SwCommunicationResource, SW_Interaction_MARTE_BehavioralFeature, MARTE_SW_Interaction_MessageComResource, GCM_MARTE_Property, MARTE_SW_Interaction_NotificationResource, SwSynchronizationResource, MARTE_SW_Interaction_SwMutualExclusionResource, SW_Interaction_SwSynchronizationResource, MARTE_GCM_FlowProperty, MARTE_GCM_GCMTrigger, GCM_MARTE_Trigger, MARTE_GCM_FlowPort, GCM_MARTE_Port, MARTE_GCM_ClientServerPort, GCM_MARTE_Interface, GCM_ClientServerSpecification, MARTE_GCM_ClientServerSpecification, MARTE_GCM_FlowSpecification, MARTE_GCM_ClientServerFeature, GCM_MARTE_BehavioralFeature, GQAM_MARTE_Behavior, MARTE_GQAM_GaEventTrace, GCM_MARTE_Feature, MARTE_GCM_GCMInvocationAction, GCM_MARTE_InvocationAction, MARTE_GCM_DataEvent, GCM_MARTE_AnyReceiveEvent, GCM_MARTE_Classifier, MARTE_GCM_DataPool, GCM_MARTE_Behavior, MARTE_GCM_GCMInvocatingBehavior, MARTE_GQAM_GaWorkloadGenerator, GQAM_GaStep, GQAM_MARTE_NamedElement, MARTE_GQAM_GaWorkloadEvent, GQAM_GaWorkloadGenerator, GQAM_GaEventTrace, GQAM_GaScenario, GQAM_MARTE_TimeEvent, MARTE_GQAM_GaScenario, Time_TimedProcessing, GQAM_GaWorkloadEvent, GQAM_GaRequestedService, GQAM_GaTimedObs, MARTE_GQAM_GaStep, GaScenario, GQAM_GaExecHost, MARTE_GQAM_GaExecHost, MARTE_GQAM_GaRequestedService, GaStep, GQAM_MARTE_Operation, MARTE_GQAM_GaTimedObs, NfpConstraint, GQAM_MARTE_TimeObservation, MARTE_GQAM_GaCommStep, MARTE_GQAM_GaAcqStep, MARTE_GQAM_GaRelStep, MARTE_GQAM_GaLatencyObs, GaTimedObs, MARTE_GQAM_GaCommHost, MARTE_GQAM_GaCommChannel, SchedulableResource, MARTE_GQAM_GaWorkloadBehavior, SAM_MARTE_NamedElement, MARTE_SAM_SaCommStep, GaCommStep, MARTE_GQAM_GaAnalysisContext, CoreElements_Configuration, Variables_ExpressionContext, GQAM_GaWorkloadBehavior, GQAM_GaResourcesPlatform, MARTE_GQAM_GaResourcesPlatform, GQAM_MARTE_Classifier, MARTE_SAM_SaAnalysisContext, GaAnalysisContext, MARTE_SAM_SaEndtoEndFlow, MARTE_SAM_SaSchedObs, SAM_MARTE_BehavioralFeature, MARTE_SAM_SaStep, SAM_SaSharedResource, MARTE_SAM_SaSharedResource, MutualExclusionResource, MARTE_SAM_SaCommHost, GaCommHost, MARTE_SAM_SaExecHost, GaExecHost, MARTE_PAM_PaStep, MARTE_PAM_PaLogicalResource, MARTE_PAM_PaRunTInstance, PAM_MARTE_NamedElement, MARTE_PAM_PaRequestedStep, PAM_PaStep, MARTE_PAM_PaCommStep, GQAM_GaCommStep, MARTE_PAM_PaResPassStep, ConstraintKind, AllocationEndKind, AllocationNature, AllocationKind, AssignmentKind, AssignmentNature, VariableDirectionKind, PoolMgtPolicyKind, CallConcurrencyKind, SynchronizationKind, ExecutionKind, ConcurrencyKind, ISA_Type, PLD_Technology, PLD_Class, Repl_Policy, WritePolicy, CacheType, ROM_Type, dummy, ComponentKind, ConditionType, ComponentState, InterruptKind, AccessPolicyKind, MutualExclusionResourceKind, QueuePolicyKind, MessageResourceKind, NotificationKind, NotificationResourceKind, ConcurrentAccessProtocolKind, FlowDirectionKind, PortSpecificationKind, ClientServerKind, DataPoolOrderingKind, LaxityKind, OptimallityCriterionKind},
    associations={base_Property0, baseUnit1, base_EnumerationLiteral2, base_Constraint4, unitAttrib9, exprAttrib12, baseDimension15, base_Enumeration16, base_Transition18, base_StateMachine19, base_StructuredClassifier20, base_Package21, mode23, base_State26, base_NamedElement27, mode5, valueAttrib7, allocatedFrom30, base_ActivityPartition33, allocatedTo28, base_Dependency34, constraint35, impliedConstraint37, from_39, to41, base_Comment44, unitType61, base_Abstraction46, impliedConstraint47, base_Namespace50, base_InstanceSpecification51, type52, unit54, base_Property57, base_Event59, resolAttr62, maxValAttr65, offsetAttr68, getTime71, setTime73, indexToValue76, base_Class79, on81, base_ValueSpecification82, base_Action89, base_TimeObservation83, base_DurationObservation84, base_TimeEvent85, every86, base_ConnectableElement110, base_Behavior90, base_Message92, duration94, start97, finish100, base_Property103, base_InstanceSpecification104, base_Classifier106, base_Lifeline108, processingUnits112, host113, protectedSharedResources115, schedulableResources116, mainScheduler117, scheduler118, dependentScheduler119, host120, virtualProcessingUnits122, base_Connector124, owner125, base_ExecutionSpecification126, base_BehavioralFeature128, base_Behavior130, base_Collaboration132, base_CollaborationUse134, base_NamedElement136, subUsage137, usedResources139, base_Connector142, intervalAttrib152, base_DataType153, base_ConnectorEnd143, base_MultiplicityElement144, base_Property145, base_NamedElement146, base_Behavior147, baseType148, base_DataType149, base_BehavioredClassifier177, collectionAttrib156, base_DataType158, choiceAttrib161, defaultAttrib163, base_DataType166, tupleAttrib169, base_DataType171, operationalMode174, main175, tRef192, base_BehavioredClassifier179, base_BehavioralFeature181, base_Message182, base_Signal184, base_Port186, base_InvocationAction188, specification190, base_Comment193, context195, base_BehavioralFeature198, base_InvocationAction200, base_BehavioralFeature203, ownedMMUs210, ownedISAs205, predictors206, caches208, blocksRAM212, blocksComputing213, controlledMedias215, arbiters216, sides217, connectedTo218, managedMemories220, drivenBy221, ownedTLBs222, buffer224, inputClock226, p_HW_Services227, r_HW_Services228, ownedHW231, endPoints233, poweredServices235, subComponents237, adressSpace257, identifierElements239, stateElements240, memorySizeFootprint243, createServices246, deleteServices248, initializeServices251, accessedElement254, routine255, entryPoints256, vectorElements301, periodElements259, priorityElements262, stackSizeElements265, activateServices268, enableConcurrencyServices271, resumeServices274, suspendServices277, terminateServices280, disableConcurrencyServices283, shareDataResources286, messageResources289, mutualExclusionResources292, notificationResources295, heapSizeElements298, concurrentResources333, maskElements303, routineConnectServices306, routineDisconnectServices309, schedulers312, deadlineElements313, deadlineTypeElements316, timeSliceElements319, delayServices322, joinServices325, yieldServices328, durationElements331, readServices357, writeServices360, memorySpaces335, fork338, exit341, base_Namespace344, timers346, devices348, closeServices349, controlServices351, openServices354, memories363, memoryBlockAdressElements365, memoryBlockSizeElements368, lockServices371, unlockServices374, mapServices377, unMapServices380, sendServices393, waitingPolicyElements383, readServices384, writeServices385, messageSizeElements388, messageQueueCapacityElements390, base_Property424, receiveServices396, occurenceCountElements399, maskElements401, flushServices404, signalServices407, waitServices410, clearServices413, accessTokenElements416, releaseServices418, acquireServices421, base_Trigger440, base_Port425, base_Port426, provInterface428, reqInterface430, featuresSpec433, base_Interface435, base_Interface437, base_BehavioralFeature439, base_Behavior468, feature441, base_InvocationAction443, onFeature444, base_AnyReceiveEvent447, classifier448, base_Property450, insertion452, selection454, base_Behavior457, onPorts459, onFeatures462, invocations465, root481, base_NamedElement469, generator470, trace471, effect473, timedEvent475, base_NamedElement477, cause480, servDemand491, steps483, parentStep484, timing486, concurRes488, endObs498, host489, scenario493, childScenario494, base_Operation496, startObs497, behavior505, demand507, acqRes501, relRes503, base_NamedElement522, base_NamedElement510, workload513, platform514, resources516, base_Classifier518, timing520, base_BehavioralFeature524, base_BehavioralFeature525, sharedRes527, instance533, host535, base_NamedElement538, behavDemand529, resource531},
    generalizations={gen_MARTE_NFPs_NfpType_TupleType, gen_MARTE_Time_TimedValueSpecification_TimedElement, gen_MARTE_Time_TimedConstraint_NFPs_NfpConstraint, gen_MARTE_Time_TimedConstraint_Time_TimedElement, gen_MARTE_Time_ClockConstraint_NFPs_NfpConstraint, gen_MARTE_Time_ClockConstraint_Time_TimedElement, gen_MARTE_Time_TimedInstantObservation_TimedElement, gen_MARTE_Time_TimedDurationObservation_TimedElement, gen_MARTE_Time_TimedEvent_TimedElement, gen_MARTE_Time_TimedProcessing_TimedElement, gen_MARTE_GRM_StorageResource_Resource, gen_MARTE_GRM_CommunicationEndPoint_Resource, gen_MARTE_GRM_SynchronizationResource_Resource, gen_MARTE_GRM_ConcurrencyResource_Resource, gen_MARTE_GRM_Scheduler_Resource, gen_MARTE_GRM_ProcessingResource_Resource, gen_MARTE_GRM_ComputingResource_ProcessingResource, gen_MARTE_GRM_MutualExclusionResource_Resource, gen_MARTE_GRM_SchedulableResource_Resource, gen_MARTE_GRM_SecondaryScheduler_Scheduler, gen_MARTE_GRM_CommunicationMedia_ProcessingResource, gen_MARTE_GRM_DeviceResource_ProcessingResource, gen_MARTE_GRM_TimingResource_Resource, gen_MARTE_GRM_ClockResource_TimingResource, gen_MARTE_GRM_TimerResource_TimingResource, gen_MARTE_GRM_Release_GrService, gen_MARTE_GRM_Acquire_GrService, gen_MARTE_RSM_DefaultLink_LinkTopology, gen_MARTE_RSM_InterRepetition_LinkTopology, gen_MARTE_RSM_Distribute_Allocate, gen_MARTE_RSM_Reshape_LinkTopology, gen_MARTE_RSM_Tiler_LinkTopology, gen_MARTE_HwComputing_HwProcessor_HwComputingResource, gen_MARTE_HwCommunication_HwCommunicationResource_HwResource, gen_MARTE_HwCommunication_HwArbiter_HwCommunicationResource, gen_MARTE_HwComputing_HwComputingResource_HwGeneral_HwResource, gen_MARTE_HwComputing_HwComputingResource_GRM_ComputingResource, gen_MARTE_HwComputing_HwISA_HwResource, gen_MARTE_HwComputing_HwBranchPredictor_HwResource, gen_MARTE_HwComputing_HwASIC_HwComputingResource, gen_MARTE_HwComputing_HwPLD_HwComputingResource, gen_MARTE_HwStorageManager_HwMMU_HwStorageManager, gen_MARTE_HwCommunication_HwMedia_GRM_CommunicationMedia, gen_MARTE_HwCommunication_HwMedia_HwCommunication_HwCommunicationResource, gen_MARTE_HwCommunication_HwBus_HwMedia, gen_MARTE_HwCommunication_HwBridge_HwMedia, gen_MARTE_HwCommunication_HwEndPoint_HwCommunication_HwCommunicationResource, gen_MARTE_HwCommunication_HwEndPoint_GRM_CommunicationEndPoint, gen_MARTE_HwStorageManager_HwStorageManager_HwGeneral_HwResource, gen_MARTE_HwStorageManager_HwStorageManager_GRM_StorageResource, gen_MARTE_HwStorageManager_HwDMA_HwStorageManager_HwStorageManager, gen_MARTE_HwStorageManager_HwDMA_HwCommunication_HwArbiter, gen_MARTE_HwMemory_HwMemory_HwGeneral_HwResource, gen_MARTE_HwMemory_HwMemory_GRM_StorageResource, gen_MARTE_HwMemory_HwRAM_HwMemory, gen_MARTE_HwDevice_HwDevice_GRM_DeviceResource, gen_MARTE_HwDevice_HwI_O_HwDevice, gen_MARTE_HwDevice_HwSupport_HwDevice, gen_MARTE_HwMemory_HwROM_HwMemory, gen_MARTE_HwMemory_HwDrive_HwMemory, gen_MARTE_HwMemory_HwCache_HwMemory, gen_MARTE_HwTiming_HwTimingResource_HwGeneral_HwResource, gen_MARTE_HwTiming_HwTimingResource_GRM_TimingResource, gen_MARTE_HwTiming_HwClock_HwTimingResource, gen_MARTE_HwTiming_HwTimer_HwTimingResource, gen_MARTE_HwDevice_HwDevice_HwGeneral_HwResource, gen_MARTE_HwDevice_HWActuator_HwI_O, gen_MARTE_HwDevice_HWSensor_HwI_O, gen_MARTE_HwGeneral_HwResourceService_GrService, gen_MARTE_HwGeneral_HwResource_Resource, gen_MARTE_HwLayout_HwComponent_HwResource, gen_MARTE_SW_ResourceCore_SwResource_Resource, gen_MARTE_HwPower_HwPowerSupply_HwComponent, gen_MARTE_HwPower_HwCoolingSupply_HwComponent, gen_MARTE_SW_ResourceCore_SwAccessService_GrService, gen_MARTE_SW_Concurrency_EntryPoint_Allocate, gen_MARTE_SW_Concurrency_SwConcurrentResource_SwResource, gen_MARTE_SW_Concurrency_InterruptResource_SwConcurrentResource, gen_MARTE_SW_Concurrency_MemoryPartition_SwResource, gen_MARTE_SW_Concurrency_SwSchedulableResource_SW_Concurrency_SwConcurrentResource, gen_MARTE_SW_Concurrency_SwSchedulableResource_GRM_SchedulableResource, gen_MARTE_SW_Concurrency_SwTimerResource_TimerResource, gen_MARTE_SW_Concurrency_Alarm_InterruptResource, gen_MARTE_SW_Brokering_DeviceBroker_SwResource, gen_MARTE_SW_Brokering_MemoryBroker_SwResource, gen_MARTE_SW_Interaction_SwInteractionResource_SwResource, gen_MARTE_SW_Interaction_SwCommunicationResource_SW_Interaction_SwInteractionResource, gen_MARTE_SW_Interaction_SwCommunicationResource_GRM_CommunicationMedia, gen_MARTE_SW_Interaction_SwSynchronizationResource_SW_Interaction_SwInteractionResource, gen_MARTE_SW_Interaction_SwSynchronizationResource_GRM_SynchronizationResource, gen_MARTE_SW_Interaction_SharedDataComResource_SwCommunicationResource, gen_MARTE_SW_Interaction_MessageComResource_SwCommunicationResource, gen_MARTE_SW_Interaction_NotificationResource_SwSynchronizationResource, gen_MARTE_SW_Interaction_SwMutualExclusionResource_SW_Interaction_SwSynchronizationResource, gen_MARTE_SW_Interaction_SwMutualExclusionResource_GRM_MutualExclusionResource, gen_MARTE_GQAM_GaScenario_GRM_ResourceUsage, gen_MARTE_GQAM_GaScenario_Time_TimedProcessing, gen_MARTE_GQAM_GaStep_GaScenario, gen_MARTE_GQAM_GaExecHost_GRM_Scheduler, gen_MARTE_GQAM_GaExecHost_GRM_ComputingResource, gen_MARTE_GQAM_GaRequestedService_GaStep, gen_MARTE_GQAM_GaTimedObs_NfpConstraint, gen_MARTE_GQAM_GaCommStep_GaStep, gen_MARTE_GQAM_GaAcqStep_GaStep, gen_MARTE_GQAM_GaRelStep_GaStep, gen_MARTE_GQAM_GaLatencyObs_GaTimedObs, gen_MARTE_GQAM_GaCommHost_GRM_CommunicationMedia, gen_MARTE_GQAM_GaCommHost_GRM_Scheduler, gen_MARTE_GQAM_GaCommChannel_SchedulableResource, gen_MARTE_GQAM_GaAnalysisContext_CoreElements_Configuration, gen_MARTE_GQAM_GaAnalysisContext_Variables_ExpressionContext, gen_MARTE_SAM_SaAnalysisContext_GaAnalysisContext, gen_MARTE_SAM_SaSchedObs_GaTimedObs, gen_MARTE_SAM_SaCommStep_GaCommStep, gen_MARTE_SAM_SaStep_GaStep, gen_MARTE_SAM_SaSharedResource_MutualExclusionResource, gen_MARTE_SAM_SaCommHost_GaCommHost, gen_MARTE_SAM_SaExecHost_GaExecHost, gen_MARTE_PAM_PaStep_GaStep, gen_MARTE_PAM_PaLogicalResource_Resource, gen_MARTE_PAM_PaRequestedStep_PAM_PaStep, gen_MARTE_PAM_PaRequestedStep_GQAM_GaRequestedService, gen_MARTE_PAM_PaCommStep_PAM_PaStep, gen_MARTE_PAM_PaCommStep_GQAM_GaCommStep, gen_MARTE_PAM_PaResPassStep_GaStep},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)