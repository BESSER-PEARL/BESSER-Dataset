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

AllocationEndKind: Enumeration = Enumeration(
    name="AllocationEndKind",
    literals={
            
    }
)

AssignmentNature: Enumeration = Enumeration(
    name="AssignmentNature",
    literals={
            
    }
)

AssignmentKind: Enumeration = Enumeration(
    name="AssignmentKind",
    literals={
            EnumerationLiteral(name="hybrid"),
			EnumerationLiteral(name="structural"),
			EnumerationLiteral(name="behavioral")
    }
)

VariableDirectionKind: Enumeration = Enumeration(
    name="VariableDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
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

SynchronizationKind: Enumeration = Enumeration(
    name="SynchronizationKind",
    literals={
            EnumerationLiteral(name="other"),
			EnumerationLiteral(name="synchronous"),
			EnumerationLiteral(name="asynchronous"),
			EnumerationLiteral(name="delayedSynchronous"),
			EnumerationLiteral(name="rendezVous")
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
            EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef"),
			EnumerationLiteral(name="maskedROM"),
			EnumerationLiteral(name="EPROM"),
			EnumerationLiteral(name="OTP_EPROM"),
			EnumerationLiteral(name="EEPROM"),
			EnumerationLiteral(name="Flash")
    }
)

Repl_Policy: Enumeration = Enumeration(
    name="Repl_Policy",
    literals={
            EnumerationLiteral(name="NFU"),
			EnumerationLiteral(name="FIFO"),
			EnumerationLiteral(name="random"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="undef"),
			EnumerationLiteral(name="LRU")
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

MutualExclusionResourceKind: Enumeration = Enumeration(
    name="MutualExclusionResourceKind",
    literals={
            EnumerationLiteral(name="CountSemaphore"),
			EnumerationLiteral(name="Mutex"),
			EnumerationLiteral(name="Undef"),
			EnumerationLiteral(name="Other"),
			EnumerationLiteral(name="BooleanSemaphore")
    }
)

FlowDirectionKind: Enumeration = Enumeration(
    name="FlowDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout")
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

PortSpecificationKind: Enumeration = Enumeration(
    name="PortSpecificationKind",
    literals={
            EnumerationLiteral(name="featureBased"),
			EnumerationLiteral(name="atomic"),
			EnumerationLiteral(name="interfaceBased")
    }
)

DataPoolOrderingKind: Enumeration = Enumeration(
    name="DataPoolOrderingKind",
    literals={
            EnumerationLiteral(name="LIFO"),
			EnumerationLiteral(name="UserDefined"),
			EnumerationLiteral(name="FIFO")
    }
)

LaxityKind: Enumeration = Enumeration(
    name="LaxityKind",
    literals={
            EnumerationLiteral(name="other"),
			EnumerationLiteral(name="hard"),
			EnumerationLiteral(name="soft")
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
MARTE_NFPs_Nfp = Class(name="MARTE::NFPs::Nfp")
NFPs_MARTE_Property = Class(name="NFPs::MARTE::Property")
NFPs_Unit = Class(name="NFPs::Unit")
NFPs_MARTE_EnumerationLiteral = Class(name="NFPs::MARTE::EnumerationLiteral")
MARTE_NFPs_NfpConstraint = Class(name="MARTE::NFPs::NfpConstraint")
MARTE_NFPs_Unit = Class(name="MARTE::NFPs::Unit")
MARTE_NFPs_NfpType = Class(name="MARTE::NFPs::NfpType")
TupleType = Class(name="TupleType")
MARTE_NFPs_Dimension = Class(name="MARTE::NFPs::Dimension")
NFPs_Dimension = Class(name="NFPs::Dimension")
NFPs_MARTE_Enumeration = Class(name="NFPs::MARTE::Enumeration")
NFPs_MARTE_Constraint = Class(name="NFPs::MARTE::Constraint")
CoreElements_Mode = Class(name="CoreElements::Mode")
MARTE_CoreElements_Configuration = Class(name="MARTE::CoreElements::Configuration")
CoreElements_MARTE_StructuredClassifier = Class(name="CoreElements::MARTE::StructuredClassifier")
CoreElements_MARTE_Package = Class(name="CoreElements::MARTE::Package")
MARTE_CoreElements_Mode = Class(name="MARTE::CoreElements::Mode")
CoreElements_MARTE_State = Class(name="CoreElements::MARTE::State")
MARTE_Alloc_Allocated = Class(name="MARTE::Alloc::Allocated")
Alloc_MARTE_NamedElement = Class(name="Alloc::MARTE::NamedElement")
MARTE_CoreElements_ModeTransition = Class(name="MARTE::CoreElements::ModeTransition")
CoreElements_MARTE_Transition = Class(name="CoreElements::MARTE::Transition")
MARTE_CoreElements_ModeBehavior = Class(name="MARTE::CoreElements::ModeBehavior")
CoreElements_MARTE_StateMachine = Class(name="CoreElements::MARTE::StateMachine")
MARTE_Alloc_AllocateActivityGroup = Class(name="MARTE::Alloc::AllocateActivityGroup")
Alloc_MARTE_ActivityPartition = Class(name="Alloc::MARTE::ActivityPartition")
MARTE_Alloc_NfpRefine = Class(name="MARTE::Alloc::NfpRefine")
Alloc_MARTE_Dependency = Class(name="Alloc::MARTE::Dependency")
NFPs_NfpConstraint = Class(name="NFPs::NfpConstraint")
MARTE_Alloc_Assign = Class(name="MARTE::Alloc::Assign")
Alloc_MARTE_Element = Class(name="Alloc::MARTE::Element")
Alloc_Allocated = Class(name="Alloc::Allocated")
MARTE_Alloc_Allocate = Class(name="MARTE::Alloc::Allocate")
Alloc_MARTE_Abstraction = Class(name="Alloc::MARTE::Abstraction")
MARTE_Time_TimedDomain = Class(name="MARTE::Time::TimedDomain")
Time_MARTE_Namespace = Class(name="Time::MARTE::Namespace")
MARTE_Time_Clock = Class(name="MARTE::Time::Clock")
Time_MARTE_InstanceSpecification = Class(name="Time::MARTE::InstanceSpecification")
Alloc_MARTE_Comment = Class(name="Alloc::MARTE::Comment")
MARTE_Time_ClockType = Class(name="MARTE::Time::ClockType")
Time_MARTE_Enumeration = Class(name="Time::MARTE::Enumeration")
Time_MARTE_Operation = Class(name="Time::MARTE::Operation")
Time_ClockType = Class(name="Time::ClockType")
Time_MARTE_Property = Class(name="Time::MARTE::Property")
Time_Clock = Class(name="Time::Clock")
MARTE_Time_TimedValueSpecification = Class(name="MARTE::Time::TimedValueSpecification")
TimedElement = Class(name="TimedElement")
Time_MARTE_ValueSpecification = Class(name="Time::MARTE::ValueSpecification")
MARTE_Time_TimedConstraint = Class(name="MARTE::Time::TimedConstraint")
Time_TimedElement = Class(name="Time::TimedElement")
MARTE_Time_ClockConstraint = Class(name="MARTE::Time::ClockConstraint")
Time_MARTE_Class = Class(name="Time::MARTE::Class")
MARTE_Time_TimedElement = Class(name="MARTE::Time::TimedElement", is_abstract=True)
MARTE_Time_TimedDurationObservation = Class(name="MARTE::Time::TimedDurationObservation")
Time_MARTE_DurationObservation = Class(name="Time::MARTE::DurationObservation")
MARTE_Time_TimedEvent = Class(name="MARTE::Time::TimedEvent")
Time_MARTE_TimeEvent = Class(name="Time::MARTE::TimeEvent")
MARTE_Time_TimedProcessing = Class(name="MARTE::Time::TimedProcessing")
Time_MARTE_Action = Class(name="Time::MARTE::Action")
Time_MARTE_Behavior = Class(name="Time::MARTE::Behavior")
MARTE_Time_TimedObservation = Class(name="MARTE::Time::TimedObservation", is_abstract=True)
MARTE_Time_TimedInstantObservation = Class(name="MARTE::Time::TimedInstantObservation")
TimedObservation = Class(name="TimedObservation")
Time_MARTE_TimeObservation = Class(name="Time::MARTE::TimeObservation")
Time_MARTE_Event = Class(name="Time::MARTE::Event")
MARTE_GRM_Resource = Class(name="MARTE::GRM::Resource")
NFP_Integer = Class(name="NFP::Integer")
GRM_MARTE_Property = Class(name="GRM::MARTE::Property")
GRM_MARTE_InstanceSpecification = Class(name="GRM::MARTE::InstanceSpecification")
GRM_MARTE_Classifier = Class(name="GRM::MARTE::Classifier")
GRM_MARTE_Lifeline = Class(name="GRM::MARTE::Lifeline")
Time_MARTE_Message = Class(name="Time::MARTE::Message")
MARTE_GRM_CommunicationEndPoint = Class(name="MARTE::GRM::CommunicationEndPoint")
MARTE_GRM_SynchronizationResource = Class(name="MARTE::GRM::SynchronizationResource")
MARTE_GRM_ConcurrencyResource = Class(name="MARTE::GRM::ConcurrencyResource")
MARTE_GRM_Scheduler = Class(name="MARTE::GRM::Scheduler")
GRM_MARTE_OpaqueExpression = Class(name="GRM::MARTE::OpaqueExpression")
GRM_ProcessingResource = Class(name="GRM::ProcessingResource")
GRM_MARTE_ConnectableElement = Class(name="GRM::MARTE::ConnectableElement")
MARTE_GRM_StorageResource = Class(name="MARTE::GRM::StorageResource")
Resource = Class(name="Resource")
GRM_MutualExclusionResource = Class(name="GRM::MutualExclusionResource")
GRM_SchedulableResource = Class(name="GRM::SchedulableResource")
MARTE_GRM_ProcessingResource = Class(name="MARTE::GRM::ProcessingResource")
NFP_Real = Class(name="NFP::Real")
GRM_Scheduler = Class(name="GRM::Scheduler")
MARTE_GRM_ComputingResource = Class(name="MARTE::GRM::ComputingResource")
ProcessingResource = Class(name="ProcessingResource")
MARTE_GRM_MutualExclusionResource = Class(name="MARTE::GRM::MutualExclusionResource")
GRM_ComputingResource = Class(name="GRM::ComputingResource")
GRM_SecondaryScheduler = Class(name="GRM::SecondaryScheduler")
MARTE_GRM_SecondaryScheduler = Class(name="MARTE::GRM::SecondaryScheduler")
Scheduler = Class(name="Scheduler")
MARTE_GRM_CommunicationMedia = Class(name="MARTE::GRM::CommunicationMedia")
GRM_MARTE_Connector = Class(name="GRM::MARTE::Connector")
MARTE_GRM_SchedulableResource = Class(name="MARTE::GRM::SchedulableResource")
SchedParameters = Class(name="SchedParameters")
MARTE_GRM_DeviceResource = Class(name="MARTE::GRM::DeviceResource")
MARTE_GRM_TimingResource = Class(name="MARTE::GRM::TimingResource")
MARTE_GRM_ClockResource = Class(name="MARTE::GRM::ClockResource")
TimingResource = Class(name="TimingResource")
MARTE_GRM_TimerResource = Class(name="MARTE::GRM::TimerResource")
MARTE_GRM_GrService = Class(name="MARTE::GRM::GrService")
GRM_Resource = Class(name="GRM::Resource")
GRM_MARTE_ExecutionSpecification = Class(name="GRM::MARTE::ExecutionSpecification")
GRM_MARTE_BehavioralFeature = Class(name="GRM::MARTE::BehavioralFeature")
NFP_Duration = Class(name="NFP::Duration")
NFP_DataTxRate = Class(name="NFP::DataTxRate")
MARTE_GRM_Release = Class(name="MARTE::GRM::Release")
GrService = Class(name="GrService")
MARTE_GRM_Acquire = Class(name="MARTE::GRM::Acquire")
MARTE_GRM_ResourceUsage = Class(name="MARTE::GRM::ResourceUsage")
NFP_DataSize = Class(name="NFP::DataSize")
NFP_Power = Class(name="NFP::Power")
NFP_Energy = Class(name="NFP::Energy")
GRM_MARTE_Behavior = Class(name="GRM::MARTE::Behavior")
GRM_MARTE_Collaboration = Class(name="GRM::MARTE::Collaboration")
GRM_MARTE_CollaborationUse = Class(name="GRM::MARTE::CollaborationUse")
MARTE_RSM_LinkTopology = Class(name="MARTE::RSM::LinkTopology", is_abstract=True)
RSM_MARTE_Connector = Class(name="RSM::MARTE::Connector")
MARTE_RSM_DefaultLink = Class(name="MARTE::RSM::DefaultLink")
LinkTopology = Class(name="LinkTopology")
MARTE_RSM_InterRepetition = Class(name="MARTE::RSM::InterRepetition")
IntegerVector = Class(name="IntegerVector")
MARTE_RSM_Distribute = Class(name="MARTE::RSM::Distribute")
Allocate = Class(name="Allocate")
GRM_MARTE_NamedElement = Class(name="GRM::MARTE::NamedElement")
GRM_ResourceUsage = Class(name="GRM::ResourceUsage")
MARTE_RSM_Reshape = Class(name="MARTE::RSM::Reshape")
MARTE_RSM_Tiler = Class(name="MARTE::RSM::Tiler")
IntegerMatrix = Class(name="IntegerMatrix")
ShapeSpecification = Class(name="ShapeSpecification")
TilerSpecification = Class(name="TilerSpecification")
MARTE_RSM_Shaped = Class(name="MARTE::RSM::Shaped")
RSM_MARTE_MultiplicityElement = Class(name="RSM::MARTE::MultiplicityElement")
MARTE_Variables_Var = Class(name="MARTE::Variables::Var")
Variables_MARTE_Property = Class(name="Variables::MARTE::Property")
MARTE_Variables_ExpressionContext = Class(name="MARTE::Variables::ExpressionContext")
Variables_MARTE_NamedElement = Class(name="Variables::MARTE::NamedElement")
RSM_MARTE_ConnectorEnd = Class(name="RSM::MARTE::ConnectorEnd")
DataTypes_MARTE_DataType = Class(name="DataTypes::MARTE::DataType")
MARTE_DataTypes_IntervalType = Class(name="MARTE::DataTypes::IntervalType")
MARTE_DataTypes_CollectionType = Class(name="MARTE::DataTypes::CollectionType")
MARTE_DataTypes_BoundedSubtype = Class(name="MARTE::DataTypes::BoundedSubtype")
DataTypes_MARTE_Property = Class(name="DataTypes::MARTE::Property")
MARTE_DataTypes_TupleType = Class(name="MARTE::DataTypes::TupleType")
MARTE_HLAM_RtUnit = Class(name="MARTE::HLAM::RtUnit")
MARTE_DataTypes_ChoiceType = Class(name="MARTE::DataTypes::ChoiceType")
HLAM_MARTE_BehavioredClassifier = Class(name="HLAM::MARTE::BehavioredClassifier")
MARTE_HLAM_PpUnit = Class(name="MARTE::HLAM::PpUnit")
HLAM_MARTE_Behavior = Class(name="HLAM::MARTE::Behavior")
HLAM_MARTE_Operation = Class(name="HLAM::MARTE::Operation")
MARTE_HLAM_RtFeature = Class(name="MARTE::HLAM::RtFeature")
HLAM_MARTE_BehavioralFeature = Class(name="HLAM::MARTE::BehavioralFeature")
HLAM_MARTE_Message = Class(name="HLAM::MARTE::Message")
HLAM_MARTE_Signal = Class(name="HLAM::MARTE::Signal")
HLAM_MARTE_Port = Class(name="HLAM::MARTE::Port")
HLAM_MARTE_InvocationAction = Class(name="HLAM::MARTE::InvocationAction")
HLAM_RtSpecification = Class(name="HLAM::RtSpecification")
Time_TimedInstantObservation = Class(name="Time::TimedInstantObservation")
NFP_DateTime = Class(name="NFP::DateTime")
NFP_Percentage = Class(name="NFP::Percentage")
MARTE_HLAM_RtSpecification = Class(name="MARTE::HLAM::RtSpecification")
UtilityType = Class(name="UtilityType")
ArrivalPattern = Class(name="ArrivalPattern")
MARTE_HLAM_RtAction = Class(name="MARTE::HLAM::RtAction")
HLAM_MARTE_Comment = Class(name="HLAM::MARTE::Comment")
MARTE_HLAM_RtService = Class(name="MARTE::HLAM::RtService")
MARTE_HwComputing_HwProcessor = Class(name="MARTE::HwComputing::HwProcessor")
HwComputingResource = Class(name="HwComputingResource")
MARTE_HwComputing_PLD_Organization = Class(name="MARTE::HwComputing::PLD::Organization")
NFP_Natural = Class(name="NFP::Natural")
HwComputing_HwISA = Class(name="HwComputing::HwISA")
HwComputing_HwBranchPredictor = Class(name="HwComputing::HwBranchPredictor")
HwMemory_HwCache = Class(name="HwMemory::HwCache")
HwStorageManager_HwMMU = Class(name="HwStorageManager::HwMMU")
MARTE_HwComputing_HwComputingResource = Class(name="MARTE::HwComputing::HwComputingResource")
HwGeneral_HwResource = Class(name="HwGeneral::HwResource")
NFP_FrequencyInterval = Class(name="NFP::FrequencyInterval")
MARTE_HwComputing_HwBranchPredictor = Class(name="MARTE::HwComputing::HwBranchPredictor")
MARTE_HwComputing_HwASIC = Class(name="MARTE::HwComputing::HwASIC")
MARTE_HwComputing_HwPLD = Class(name="MARTE::HwComputing::HwPLD")
HwComputing_PLD_Organization = Class(name="HwComputing::PLD::Organization")
MARTE_HwComputing_HwISA = Class(name="MARTE::HwComputing::HwISA")
HwResource = Class(name="HwResource")
NFP_String = Class(name="NFP::String")
MARTE_HwComputing_HwMCU = Class(name="MARTE::HwComputing::HwMCU")
HwComputing_HwProcessor = Class(name="HwComputing::HwProcessor")
HwDevice_HwPeripheral = Class(name="HwDevice::HwPeripheral")
HwRegister_HwRegister = Class(name="HwRegister::HwRegister")
HwPackage_HwPackage = Class(name="HwPackage::HwPackage")
HwIO_HwPin = Class(name="HwIO::HwPin")
HwCommunication_HwPort = Class(name="HwCommunication::HwPort")
HwMemory_HwRAM = Class(name="HwMemory::HwRAM")
HwComputing_HwComputingResource = Class(name="HwComputing::HwComputingResource")
MARTE_HwCommunication_HwMedia = Class(name="MARTE::HwCommunication::HwMedia")
GRM_CommunicationMedia = Class(name="GRM::CommunicationMedia")
HwCommunication_HwCommunicationResource = Class(name="HwCommunication::HwCommunicationResource")
HwCommunication_HwArbiter = Class(name="HwCommunication::HwArbiter")
MARTE_HwCommunication_HwBus = Class(name="MARTE::HwCommunication::HwBus")
HwMedia = Class(name="HwMedia")
NFP_Boolean = Class(name="NFP::Boolean")
MARTE_HwCommunication_HwCommunicationResource = Class(name="MARTE::HwCommunication::HwCommunicationResource")
MARTE_HwCommunication_HwArbiter = Class(name="MARTE::HwCommunication::HwArbiter")
HwCommunicationResource = Class(name="HwCommunicationResource")
HwCommunication_HwMedia = Class(name="HwCommunication::HwMedia")
MARTE_HwCommunication_HwBridge = Class(name="MARTE::HwCommunication::HwBridge")
MARTE_HwCommunication_HwEndPoint = Class(name="MARTE::HwCommunication::HwEndPoint")
GRM_CommunicationEndPoint = Class(name="GRM::CommunicationEndPoint")
MARTE_HwCommunication_HwPort = Class(name="MARTE::HwCommunication::HwPort")
HwEndPoint = Class(name="HwEndPoint")
HwProtocol_HwProtocol = Class(name="HwProtocol::HwProtocol")
MARTE_HwStorageManager_HwStorageManager = Class(name="MARTE::HwStorageManager::HwStorageManager")
GRM_StorageResource = Class(name="GRM::StorageResource")
HwMemory_HwMemory = Class(name="HwMemory::HwMemory")
MARTE_HwStorageManager_HwDMA = Class(name="MARTE::HwStorageManager::HwDMA")
HwStorageManager_HwStorageManager = Class(name="HwStorageManager::HwStorageManager")
MARTE_HwCommunication_HwConnection = Class(name="MARTE::HwCommunication::HwConnection")
MARTE_HwStorageManager_HwMMU = Class(name="MARTE::HwStorageManager::HwMMU")
HwStorageManager = Class(name="HwStorageManager")
MARTE_HwMemory_HwMemory = Class(name="MARTE::HwMemory::HwMemory")
MARTE_HwMemory_Timing = Class(name="MARTE::HwMemory::Timing")
HwMemory_Timing = Class(name="HwMemory::Timing")
MARTE_HwMemory_CacheStructure = Class(name="MARTE::HwMemory::CacheStructure")
MARTE_HwMemory_MemoryOrganization = Class(name="MARTE::HwMemory::MemoryOrganization")
MARTE_HwMemory_HwRAM = Class(name="MARTE::HwMemory::HwRAM")
HwMemory = Class(name="HwMemory")
HwMemory_MemoryOrganization = Class(name="HwMemory::MemoryOrganization")
MARTE_HwMemory_HwROM = Class(name="MARTE::HwMemory::HwROM")
MARTE_HwMemory_HwDrive = Class(name="MARTE::HwMemory::HwDrive")
HwMemory_CacheStructure = Class(name="HwMemory::CacheStructure")
MARTE_HwTiming_HwTimingResource = Class(name="MARTE::HwTiming::HwTimingResource")
GRM_TimingResource = Class(name="GRM::TimingResource")
MARTE_HwTiming_HwClock = Class(name="MARTE::HwTiming::HwClock")
HwTimingResource = Class(name="HwTimingResource")
MARTE_HwTiming_HwTimer = Class(name="MARTE::HwTiming::HwTimer")
MARTE_HwMemory_HwCache = Class(name="MARTE::HwMemory::HwCache")
MARTE_HwDevice_HwDevice = Class(name="MARTE::HwDevice::HwDevice")
GRM_DeviceResource = Class(name="GRM::DeviceResource")
HwDeviceFunction_HwDeviceFunction = Class(name="HwDeviceFunction::HwDeviceFunction")
MARTE_HwDevice_HwI_O = Class(name="MARTE::HwDevice::HwI::O")
HwDevice = Class(name="HwDevice")
MARTE_HwDevice_HwSupport = Class(name="MARTE::HwDevice::HwSupport")
HwTiming_HwClock = Class(name="HwTiming::HwClock")
HwPeripheral_OperationImpl = Class(name="HwPeripheral::OperationImpl")
HwPeripheral_PeripheralActivity = Class(name="HwPeripheral::PeripheralActivity")
MARTE_HwGeneral_HwResourceService = Class(name="MARTE::HwGeneral::HwResourceService")
MARTE_HwDevice_HWActuator = Class(name="MARTE::HwDevice::HWActuator")
HwI_O = Class(name="HwI::O")
MARTE_HwDevice_HWSensor = Class(name="MARTE::HwDevice::HWSensor")
MARTE_HwDevice_HwPeripheral = Class(name="MARTE::HwDevice::HwPeripheral")
HwGeneral_HwResourceService = Class(name="HwGeneral::HwResourceService")
HwCommunication_HwEndPoint = Class(name="HwCommunication::HwEndPoint")
NFP_Frequency = Class(name="NFP::Frequency")
HwGeneral_MARTE_Operation = Class(name="HwGeneral::MARTE::Operation")
HwGeneral_MARTE_Activity = Class(name="HwGeneral::MARTE::Activity")
MARTE_HwGeneral_HwResource = Class(name="MARTE::HwGeneral::HwResource")
NFP_Length = Class(name="NFP::Length")
NFP_Area = Class(name="NFP::Area")
NFP_NaturalInterval = Class(name="NFP::NaturalInterval")
MARTE_HwLayout_HwComponent = Class(name="MARTE::HwLayout::HwComponent")
HwLayout_HwComponent = Class(name="HwLayout::HwComponent")
MARTE_HwLayout_Env_Condition = Class(name="MARTE::HwLayout::Env::Condition")
NFP_Price = Class(name="NFP::Price")
HwLayout_Env_Condition = Class(name="HwLayout::Env::Condition")
MARTE_HwPower_HwPowerSupply = Class(name="MARTE::HwPower::HwPowerSupply")
HwComponent = Class(name="HwComponent")
Realnterval = Class(name="Realnterval")
Operation = Class(name="Operation")
HwPeripheral_MARTE_Operation = Class(name="HwPeripheral::MARTE::Operation")
MARTE_HwPeripheral_RegisterAction = Class(name="MARTE::HwPeripheral::RegisterAction", is_abstract=True)
Action = Class(name="Action")
MARTE_HwPeripheral_WriteRegisterAction = Class(name="MARTE::HwPeripheral::WriteRegisterAction")
RegisterAction = Class(name="RegisterAction")
HwPeripheral_MARTE_InputPin = Class(name="HwPeripheral::MARTE::InputPin")
MARTE_HwPeripheral_ReadRegisterAction = Class(name="MARTE::HwPeripheral::ReadRegisterAction")
HwPeripheral_MARTE_OutputPin = Class(name="HwPeripheral::MARTE::OutputPin")
MARTE_HwPeripheral_PeripheralActivity = Class(name="MARTE::HwPeripheral::PeripheralActivity")
Activity = Class(name="Activity")
HwPeripheral_RegisterAction = Class(name="HwPeripheral::RegisterAction")
MARTE_HwPower_HwCoolingSupply = Class(name="MARTE::HwPower::HwCoolingSupply")
MARTE_HwPeripheral_OperationImpl = Class(name="MARTE::HwPeripheral::OperationImpl")
HwIO_HwLine = Class(name="HwIO::HwLine")
MARTE_HwIO_HwLine = Class(name="MARTE::HwIO::HwLine")
MARTE_HwRegister_HwRegister = Class(name="MARTE::HwRegister::HwRegister")
MARTE_HwDatasheet_HwDatasheet = Class(name="MARTE::HwDatasheet::HwDatasheet")
MARTE_HwDeviceFunction_HwDeviceFunction = Class(name="MARTE::HwDeviceFunction::HwDeviceFunction")
MARTE_HwIO_HwPin = Class(name="MARTE::HwIO::HwPin")
HwPackage_HwPackagePin = Class(name="HwPackage::HwPackagePin")
MARTE_HwPackage_HwPackagePin = Class(name="MARTE::HwPackage::HwPackagePin")
HwPackage_HwWire = Class(name="HwPackage::HwWire")
MARTE_HwPackage_HwWire = Class(name="MARTE::HwPackage::HwWire")
MARTE_HwProtocol_HwProtocol = Class(name="MARTE::HwProtocol::HwProtocol")
HwProtocol_MARTE_Operation = Class(name="HwProtocol::MARTE::Operation")
MARTE_HwDiagram_HwBlockDiagram = Class(name="MARTE::HwDiagram::HwBlockDiagram")
MARTE_HwPackage_HwPackage = Class(name="MARTE::HwPackage::HwPackage")
MARTE_HwDiagram_HwCircuitDiagram = Class(name="MARTE::HwDiagram::HwCircuitDiagram")
MARTE_HwDiagram_HwHRMDiagram = Class(name="MARTE::HwDiagram::HwHRMDiagram")
HwCommunication_HwConnection = Class(name="HwCommunication::HwConnection")
MARTE_HwDiagram_SRMDiagram = Class(name="MARTE::HwDiagram::SRMDiagram")
SW_Brokering_DeviceBroker = Class(name="SW::Brokering::DeviceBroker")
MARTE_SW_ResourceCore_SwResource = Class(name="MARTE::SW::ResourceCore::SwResource", is_abstract=True)
SW_ResourceCore_MARTE_TypedElement = Class(name="SW::ResourceCore::MARTE::TypedElement")
HwDiagram_MARTE_DataType = Class(name="HwDiagram::MARTE::DataType")
MARTE_SW_ResourceCore_SwAccessService = Class(name="MARTE::SW::ResourceCore::SwAccessService")
SW_ResourceCore_MARTE_Property = Class(name="SW::ResourceCore::MARTE::Property")
MARTE_SW_Concurrency_EntryPoint = Class(name="MARTE::SW::Concurrency::EntryPoint")
SW_ResourceCore_MARTE_BehavioralFeature = Class(name="SW::ResourceCore::MARTE::BehavioralFeature")
MARTE_SW_Concurrency_SwConcurrentResource = Class(name="MARTE::SW::Concurrency::SwConcurrentResource", is_abstract=True)
SwResource = Class(name="SwResource")
SW_Concurrency_MARTE_Element = Class(name="SW::Concurrency::MARTE::Element")
SW_Concurrency_MARTE_TypedElement = Class(name="SW::Concurrency::MARTE::TypedElement")
SW_Concurrency_MARTE_BehavioralFeature = Class(name="SW::Concurrency::MARTE::BehavioralFeature")
MARTE_SW_Concurrency_InterruptResource = Class(name="MARTE::SW::Concurrency::InterruptResource")
SwConcurrentResource = Class(name="SwConcurrentResource")
MARTE_SW_Concurrency_SwSchedulableResource = Class(name="MARTE::SW::Concurrency::SwSchedulableResource")
SW_Concurrency_SwConcurrentResource = Class(name="SW::Concurrency::SwConcurrentResource")
SW_Concurrency_MARTE_NamedElement = Class(name="SW::Concurrency::MARTE::NamedElement")
MARTE_SW_Concurrency_MemoryPartition = Class(name="MARTE::SW::Concurrency::MemoryPartition")
SW_Concurrency_MARTE_Namespace = Class(name="SW::Concurrency::MARTE::Namespace")
MARTE_SW_Concurrency_Alarm = Class(name="MARTE::SW::Concurrency::Alarm")
InterruptResource = Class(name="InterruptResource")
MARTE_SW_Concurrency_SwTimerResource = Class(name="MARTE::SW::Concurrency::SwTimerResource")
TimerResource = Class(name="TimerResource")
MARTE_SW_Brokering_DeviceBroker = Class(name="MARTE::SW::Brokering::DeviceBroker")
SW_Brokering_MARTE_TypedElement = Class(name="SW::Brokering::MARTE::TypedElement")
SW_Brokering_MARTE_BehavioralFeature = Class(name="SW::Brokering::MARTE::BehavioralFeature")
SW_Brokering_MARTE_Operation = Class(name="SW::Brokering::MARTE::Operation")
SW_Brokering_MARTE_Activity = Class(name="SW::Brokering::MARTE::Activity")
MARTE_SW_Brokering_MemoryBroker = Class(name="MARTE::SW::Brokering::MemoryBroker")
MARTE_SW_Interaction_SwInteractionResource = Class(name="MARTE::SW::Interaction::SwInteractionResource", is_abstract=True)
SW_Interaction_MARTE_TypedElement = Class(name="SW::Interaction::MARTE::TypedElement")
MARTE_SW_Interaction_SwCommunicationResource = Class(name="MARTE::SW::Interaction::SwCommunicationResource", is_abstract=True)
SW_Interaction_SwInteractionResource = Class(name="SW::Interaction::SwInteractionResource")
MARTE_SW_Interaction_SwSynchronizationResource = Class(name="MARTE::SW::Interaction::SwSynchronizationResource", is_abstract=True)
GRM_SynchronizationResource = Class(name="GRM::SynchronizationResource")
MARTE_SW_Interaction_SharedDataComResource = Class(name="MARTE::SW::Interaction::SharedDataComResource")
SwCommunicationResource = Class(name="SwCommunicationResource")
MARTE_SW_Interaction_MessageComResource = Class(name="MARTE::SW::Interaction::MessageComResource")
MARTE_SW_Interaction_NotificationResource = Class(name="MARTE::SW::Interaction::NotificationResource")
SwSynchronizationResource = Class(name="SwSynchronizationResource")
SW_Interaction_MARTE_BehavioralFeature = Class(name="SW::Interaction::MARTE::BehavioralFeature")
MARTE_SW_Interaction_SwMutualExclusionResource = Class(name="MARTE::SW::Interaction::SwMutualExclusionResource")
SW_Interaction_SwSynchronizationResource = Class(name="SW::Interaction::SwSynchronizationResource")
MARTE_GCM_FlowProperty = Class(name="MARTE::GCM::FlowProperty")
GCM_MARTE_Property = Class(name="GCM::MARTE::Property")
MARTE_GCM_FlowPort = Class(name="MARTE::GCM::FlowPort")
MARTE_GCM_ClientServerPort = Class(name="MARTE::GCM::ClientServerPort")
GCM_MARTE_Interface = Class(name="GCM::MARTE::Interface")
GCM_ClientServerSpecification = Class(name="GCM::ClientServerSpecification")
GCM_MARTE_Port = Class(name="GCM::MARTE::Port")
MARTE_GCM_ClientServerSpecification = Class(name="MARTE::GCM::ClientServerSpecification")
MARTE_GCM_FlowSpecification = Class(name="MARTE::GCM::FlowSpecification")
MARTE_GCM_ClientServerFeature = Class(name="MARTE::GCM::ClientServerFeature")
GCM_MARTE_BehavioralFeature = Class(name="GCM::MARTE::BehavioralFeature")
MARTE_GCM_GCMTrigger = Class(name="MARTE::GCM::GCMTrigger")
GCM_MARTE_Trigger = Class(name="GCM::MARTE::Trigger")
GCM_MARTE_InvocationAction = Class(name="GCM::MARTE::InvocationAction")
MARTE_GCM_DataEvent = Class(name="MARTE::GCM::DataEvent")
GCM_MARTE_AnyReceiveEvent = Class(name="GCM::MARTE::AnyReceiveEvent")
GCM_MARTE_Classifier = Class(name="GCM::MARTE::Classifier")
MARTE_GCM_DataPool = Class(name="MARTE::GCM::DataPool")
GCM_MARTE_Behavior = Class(name="GCM::MARTE::Behavior")
GCM_MARTE_Feature = Class(name="GCM::MARTE::Feature")
MARTE_GCM_GCMInvocationAction = Class(name="MARTE::GCM::GCMInvocationAction")
MARTE_GQAM_GaWorkloadGenerator = Class(name="MARTE::GQAM::GaWorkloadGenerator")
GQAM_MARTE_Behavior = Class(name="GQAM::MARTE::Behavior")
GQAM_GaEventTrace = Class(name="GQAM::GaEventTrace")
GQAM_GaScenario = Class(name="GQAM::GaScenario")
GQAM_MARTE_TimeEvent = Class(name="GQAM::MARTE::TimeEvent")
MARTE_GQAM_GaEventTrace = Class(name="MARTE::GQAM::GaEventTrace")
GQAM_MARTE_NamedElement = Class(name="GQAM::MARTE::NamedElement")
MARTE_GQAM_GaWorkloadEvent = Class(name="MARTE::GQAM::GaWorkloadEvent")
GQAM_GaWorkloadGenerator = Class(name="GQAM::GaWorkloadGenerator")
MARTE_GQAM_GaScenario = Class(name="MARTE::GQAM::GaScenario")
Time_TimedProcessing = Class(name="Time::TimedProcessing")
GQAM_GaWorkloadEvent = Class(name="GQAM::GaWorkloadEvent")
GQAM_GaStep = Class(name="GQAM::GaStep")
GQAM_GaTimedObs = Class(name="GQAM::GaTimedObs")
MARTE_GQAM_GaStep = Class(name="MARTE::GQAM::GaStep")
GaScenario = Class(name="GaScenario")
MARTE_GQAM_GaExecHost = Class(name="MARTE::GQAM::GaExecHost")
GQAM_GaExecHost = Class(name="GQAM::GaExecHost")
GQAM_GaRequestedService = Class(name="GQAM::GaRequestedService")
MARTE_GQAM_GaRequestedService = Class(name="MARTE::GQAM::GaRequestedService")
GaStep = Class(name="GaStep")
IntegerInterval = Class(name="IntegerInterval")
MARTE_GQAM_GaCommStep = Class(name="MARTE::GQAM::GaCommStep")
MARTE_GQAM_GaAcqStep = Class(name="MARTE::GQAM::GaAcqStep")
MARTE_GQAM_GaRelStep = Class(name="MARTE::GQAM::GaRelStep")
GQAM_MARTE_Operation = Class(name="GQAM::MARTE::Operation")
MARTE_GQAM_GaTimedObs = Class(name="MARTE::GQAM::GaTimedObs")
NfpConstraint = Class(name="NfpConstraint")
GQAM_MARTE_TimeObservation = Class(name="GQAM::MARTE::TimeObservation")
MARTE_GQAM_GaCommHost = Class(name="MARTE::GQAM::GaCommHost")
MARTE_GQAM_GaLatencyObs = Class(name="MARTE::GQAM::GaLatencyObs")
GaTimedObs = Class(name="GaTimedObs")
MARTE_GQAM_GaAnalysisContext = Class(name="MARTE::GQAM::GaAnalysisContext")
CoreElements_Configuration = Class(name="CoreElements::Configuration")
Variables_ExpressionContext = Class(name="Variables::ExpressionContext")
MARTE_GQAM_GaCommChannel = Class(name="MARTE::GQAM::GaCommChannel")
SchedulableResource = Class(name="SchedulableResource")
MARTE_GQAM_GaWorkloadBehavior = Class(name="MARTE::GQAM::GaWorkloadBehavior")
MARTE_SAM_SaAnalysisContext = Class(name="MARTE::SAM::SaAnalysisContext")
GaAnalysisContext = Class(name="GaAnalysisContext")
MARTE_SAM_SaEndtoEndFlow = Class(name="MARTE::SAM::SaEndtoEndFlow")
GQAM_GaWorkloadBehavior = Class(name="GQAM::GaWorkloadBehavior")
GQAM_GaResourcesPlatform = Class(name="GQAM::GaResourcesPlatform")
MARTE_GQAM_GaResourcesPlatform = Class(name="MARTE::GQAM::GaResourcesPlatform")
GQAM_MARTE_Classifier = Class(name="GQAM::MARTE::Classifier")
SAM_MARTE_NamedElement = Class(name="SAM::MARTE::NamedElement")
MARTE_SAM_SaCommStep = Class(name="MARTE::SAM::SaCommStep")
GaCommStep = Class(name="GaCommStep")
SAM_MARTE_BehavioralFeature = Class(name="SAM::MARTE::BehavioralFeature")
MARTE_SAM_SaStep = Class(name="MARTE::SAM::SaStep")
MARTE_SAM_SaSharedResource = Class(name="MARTE::SAM::SaSharedResource")
MutualExclusionResource = Class(name="MutualExclusionResource")
SAM_SaSharedResource = Class(name="SAM::SaSharedResource")
MARTE_SAM_SaCommHost = Class(name="MARTE::SAM::SaCommHost")
GaCommHost = Class(name="GaCommHost")
MARTE_SAM_SaSchedObs = Class(name="MARTE::SAM::SaSchedObs")
MARTE_PAM_PaStep = Class(name="MARTE::PAM::PaStep")
MARTE_SAM_SaExecHost = Class(name="MARTE::SAM::SaExecHost")
GaExecHost = Class(name="GaExecHost")
MARTE_PAM_PaCommStep = Class(name="MARTE::PAM::PaCommStep")
GQAM_GaCommStep = Class(name="GQAM::GaCommStep")
MARTE_PAM_PaResPassStep = Class(name="MARTE::PAM::PaResPassStep")
MARTE_PAM_PaLogicalResource = Class(name="MARTE::PAM::PaLogicalResource")
MARTE_PAM_PaRequestedStep = Class(name="MARTE::PAM::PaRequestedStep")
PAM_PaStep = Class(name="PAM::PaStep")
MARTE_PAM_PaRunTInstance = Class(name="MARTE::PAM::PaRunTInstance")
PAM_MARTE_NamedElement = Class(name="PAM::MARTE::NamedElement")

# MARTE_NFPs_Nfp class attributes and methods

# NFPs_MARTE_Property class attributes and methods

# NFPs_Unit class attributes and methods

# NFPs_MARTE_EnumerationLiteral class attributes and methods

# MARTE_NFPs_NfpConstraint class attributes and methods
MARTE_NFPs_NfpConstraint_kind: Property = Property(name="kind", type=StringType)
MARTE_NFPs_NfpConstraint.attributes={MARTE_NFPs_NfpConstraint_kind}

# MARTE_NFPs_Unit class attributes and methods
MARTE_NFPs_Unit_offsetFactor: Property = Property(name="offsetFactor", type=StringType)
MARTE_NFPs_Unit_convFactor: Property = Property(name="convFactor", type=StringType)
MARTE_NFPs_Unit.attributes={MARTE_NFPs_Unit_convFactor, MARTE_NFPs_Unit_offsetFactor}

# MARTE_NFPs_NfpType class attributes and methods

# TupleType class attributes and methods

# MARTE_NFPs_Dimension class attributes and methods
MARTE_NFPs_Dimension_symbol: Property = Property(name="symbol", type=StringType)
MARTE_NFPs_Dimension_baseExponent: Property = Property(name="baseExponent", type=IntegerType)
MARTE_NFPs_Dimension.attributes={MARTE_NFPs_Dimension_baseExponent, MARTE_NFPs_Dimension_symbol}

# NFPs_Dimension class attributes and methods

# NFPs_MARTE_Enumeration class attributes and methods

# NFPs_MARTE_Constraint class attributes and methods

# CoreElements_Mode class attributes and methods

# MARTE_CoreElements_Configuration class attributes and methods

# CoreElements_MARTE_StructuredClassifier class attributes and methods

# CoreElements_MARTE_Package class attributes and methods

# MARTE_CoreElements_Mode class attributes and methods

# CoreElements_MARTE_State class attributes and methods

# MARTE_Alloc_Allocated class attributes and methods

# Alloc_MARTE_NamedElement class attributes and methods

# MARTE_CoreElements_ModeTransition class attributes and methods

# CoreElements_MARTE_Transition class attributes and methods

# MARTE_CoreElements_ModeBehavior class attributes and methods

# CoreElements_MARTE_StateMachine class attributes and methods

# MARTE_Alloc_AllocateActivityGroup class attributes and methods

# Alloc_MARTE_ActivityPartition class attributes and methods

# MARTE_Alloc_NfpRefine class attributes and methods

# Alloc_MARTE_Dependency class attributes and methods

# NFPs_NfpConstraint class attributes and methods

# MARTE_Alloc_Assign class attributes and methods

# Alloc_MARTE_Element class attributes and methods

# Alloc_Allocated class attributes and methods

# MARTE_Alloc_Allocate class attributes and methods
MARTE_Alloc_Allocate_kind: Property = Property(name="kind", type=StringType)
MARTE_Alloc_Allocate_nature: Property = Property(name="nature", type=StringType)
MARTE_Alloc_Allocate.attributes={MARTE_Alloc_Allocate_nature, MARTE_Alloc_Allocate_kind}

# Alloc_MARTE_Abstraction class attributes and methods

# MARTE_Time_TimedDomain class attributes and methods

# Time_MARTE_Namespace class attributes and methods

# MARTE_Time_Clock class attributes and methods
MARTE_Time_Clock_standard: Property = Property(name="standard", type=StringType)
MARTE_Time_Clock.attributes={MARTE_Time_Clock_standard}

# Time_MARTE_InstanceSpecification class attributes and methods

# Alloc_MARTE_Comment class attributes and methods

# MARTE_Time_ClockType class attributes and methods
MARTE_Time_ClockType_nature: Property = Property(name="nature", type=StringType)
MARTE_Time_ClockType_isLogical: Property = Property(name="isLogical", type=StringType)
MARTE_Time_ClockType.attributes={MARTE_Time_ClockType_isLogical, MARTE_Time_ClockType_nature}

# Time_MARTE_Enumeration class attributes and methods

# Time_MARTE_Operation class attributes and methods

# Time_ClockType class attributes and methods

# Time_MARTE_Property class attributes and methods

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
MARTE_Time_ClockConstraint.attributes={MARTE_Time_ClockConstraint_isCoincidenceBased, MARTE_Time_ClockConstraint_isPrecedenceBased, MARTE_Time_ClockConstraint_isChronometricBased}

# Time_MARTE_Class class attributes and methods

# MARTE_Time_TimedElement class attributes and methods

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

# Time_MARTE_Behavior class attributes and methods

# MARTE_Time_TimedObservation class attributes and methods

# MARTE_Time_TimedInstantObservation class attributes and methods
MARTE_Time_TimedInstantObservation_obsKind: Property = Property(name="obsKind", type=StringType)
MARTE_Time_TimedInstantObservation.attributes={MARTE_Time_TimedInstantObservation_obsKind}

# TimedObservation class attributes and methods

# Time_MARTE_TimeObservation class attributes and methods

# Time_MARTE_Event class attributes and methods

# MARTE_GRM_Resource class attributes and methods
MARTE_GRM_Resource_isProtected: Property = Property(name="isProtected", type=StringType)
MARTE_GRM_Resource.attributes={MARTE_GRM_Resource_isProtected}

# NFP_Integer class attributes and methods

# GRM_MARTE_Property class attributes and methods

# GRM_MARTE_InstanceSpecification class attributes and methods

# GRM_MARTE_Classifier class attributes and methods

# GRM_MARTE_Lifeline class attributes and methods

# Time_MARTE_Message class attributes and methods

# MARTE_GRM_CommunicationEndPoint class attributes and methods

# MARTE_GRM_SynchronizationResource class attributes and methods

# MARTE_GRM_ConcurrencyResource class attributes and methods

# MARTE_GRM_Scheduler class attributes and methods
MARTE_GRM_Scheduler_isPreemptible: Property = Property(name="isPreemptible", type=StringType)
MARTE_GRM_Scheduler_schedPolicy: Property = Property(name="schedPolicy", type=StringType)
MARTE_GRM_Scheduler_otherSchedPolicy: Property = Property(name="otherSchedPolicy", type=StringType)
MARTE_GRM_Scheduler.attributes={MARTE_GRM_Scheduler_schedPolicy, MARTE_GRM_Scheduler_otherSchedPolicy, MARTE_GRM_Scheduler_isPreemptible}

# GRM_MARTE_OpaqueExpression class attributes and methods

# GRM_ProcessingResource class attributes and methods

# GRM_MARTE_ConnectableElement class attributes and methods

# MARTE_GRM_StorageResource class attributes and methods

# Resource class attributes and methods

# GRM_MutualExclusionResource class attributes and methods

# GRM_SchedulableResource class attributes and methods

# MARTE_GRM_ProcessingResource class attributes and methods

# NFP_Real class attributes and methods

# GRM_Scheduler class attributes and methods

# MARTE_GRM_ComputingResource class attributes and methods

# ProcessingResource class attributes and methods

# MARTE_GRM_MutualExclusionResource class attributes and methods
MARTE_GRM_MutualExclusionResource_protectKind: Property = Property(name="protectKind", type=StringType)
MARTE_GRM_MutualExclusionResource_otherProtectProtocol: Property = Property(name="otherProtectProtocol", type=StringType)
MARTE_GRM_MutualExclusionResource.attributes={MARTE_GRM_MutualExclusionResource_otherProtectProtocol, MARTE_GRM_MutualExclusionResource_protectKind}

# GRM_ComputingResource class attributes and methods

# GRM_SecondaryScheduler class attributes and methods

# MARTE_GRM_SecondaryScheduler class attributes and methods

# Scheduler class attributes and methods

# MARTE_GRM_CommunicationMedia class attributes and methods
MARTE_GRM_CommunicationMedia_transmMode: Property = Property(name="transmMode", type=StringType)
MARTE_GRM_CommunicationMedia.attributes={MARTE_GRM_CommunicationMedia_transmMode}

# GRM_MARTE_Connector class attributes and methods

# MARTE_GRM_SchedulableResource class attributes and methods

# SchedParameters class attributes and methods

# MARTE_GRM_DeviceResource class attributes and methods

# MARTE_GRM_TimingResource class attributes and methods

# MARTE_GRM_ClockResource class attributes and methods

# TimingResource class attributes and methods

# MARTE_GRM_TimerResource class attributes and methods
MARTE_GRM_TimerResource_isPeriodic: Property = Property(name="isPeriodic", type=StringType)
MARTE_GRM_TimerResource.attributes={MARTE_GRM_TimerResource_isPeriodic}

# MARTE_GRM_GrService class attributes and methods

# GRM_Resource class attributes and methods

# GRM_MARTE_ExecutionSpecification class attributes and methods

# GRM_MARTE_BehavioralFeature class attributes and methods

# NFP_Duration class attributes and methods

# NFP_DataTxRate class attributes and methods

# MARTE_GRM_Release class attributes and methods

# GrService class attributes and methods

# MARTE_GRM_Acquire class attributes and methods
MARTE_GRM_Acquire_isBlocking: Property = Property(name="isBlocking", type=StringType)
MARTE_GRM_Acquire.attributes={MARTE_GRM_Acquire_isBlocking}

# MARTE_GRM_ResourceUsage class attributes and methods

# NFP_DataSize class attributes and methods

# NFP_Power class attributes and methods

# NFP_Energy class attributes and methods

# GRM_MARTE_Behavior class attributes and methods

# GRM_MARTE_Collaboration class attributes and methods

# GRM_MARTE_CollaborationUse class attributes and methods

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

# GRM_MARTE_NamedElement class attributes and methods

# GRM_ResourceUsage class attributes and methods

# MARTE_RSM_Reshape class attributes and methods

# MARTE_RSM_Tiler class attributes and methods

# IntegerMatrix class attributes and methods

# ShapeSpecification class attributes and methods

# TilerSpecification class attributes and methods

# MARTE_RSM_Shaped class attributes and methods

# RSM_MARTE_MultiplicityElement class attributes and methods

# MARTE_Variables_Var class attributes and methods
MARTE_Variables_Var_dir: Property = Property(name="dir", type=StringType)
MARTE_Variables_Var.attributes={MARTE_Variables_Var_dir}

# Variables_MARTE_Property class attributes and methods

# MARTE_Variables_ExpressionContext class attributes and methods

# Variables_MARTE_NamedElement class attributes and methods

# RSM_MARTE_ConnectorEnd class attributes and methods

# DataTypes_MARTE_DataType class attributes and methods

# MARTE_DataTypes_IntervalType class attributes and methods

# MARTE_DataTypes_CollectionType class attributes and methods

# MARTE_DataTypes_BoundedSubtype class attributes and methods
MARTE_DataTypes_BoundedSubtype_maxValue: Property = Property(name="maxValue", type=StringType)
MARTE_DataTypes_BoundedSubtype_isMinOpen: Property = Property(name="isMinOpen", type=BooleanType)
MARTE_DataTypes_BoundedSubtype_isMaxOpen: Property = Property(name="isMaxOpen", type=BooleanType)
MARTE_DataTypes_BoundedSubtype_minValue: Property = Property(name="minValue", type=StringType)
MARTE_DataTypes_BoundedSubtype.attributes={MARTE_DataTypes_BoundedSubtype_isMinOpen, MARTE_DataTypes_BoundedSubtype_minValue, MARTE_DataTypes_BoundedSubtype_isMaxOpen, MARTE_DataTypes_BoundedSubtype_maxValue}

# DataTypes_MARTE_Property class attributes and methods

# MARTE_DataTypes_TupleType class attributes and methods

# MARTE_HLAM_RtUnit class attributes and methods
MARTE_HLAM_RtUnit_isDynamic: Property = Property(name="isDynamic", type=StringType)
MARTE_HLAM_RtUnit_isMain: Property = Property(name="isMain", type=StringType)
MARTE_HLAM_RtUnit_srPoolSize: Property = Property(name="srPoolSize", type=StringType)
MARTE_HLAM_RtUnit_queueSchedPolicy: Property = Property(name="queueSchedPolicy", type=StringType)
MARTE_HLAM_RtUnit_queueSize: Property = Property(name="queueSize", type=StringType)
MARTE_HLAM_RtUnit_srPoolPolicy: Property = Property(name="srPoolPolicy", type=StringType)
MARTE_HLAM_RtUnit.attributes={MARTE_HLAM_RtUnit_queueSchedPolicy, MARTE_HLAM_RtUnit_isDynamic, MARTE_HLAM_RtUnit_srPoolPolicy, MARTE_HLAM_RtUnit_srPoolSize, MARTE_HLAM_RtUnit_isMain, MARTE_HLAM_RtUnit_queueSize}

# MARTE_DataTypes_ChoiceType class attributes and methods

# HLAM_MARTE_BehavioredClassifier class attributes and methods

# MARTE_HLAM_PpUnit class attributes and methods
MARTE_HLAM_PpUnit_concPolicy: Property = Property(name="concPolicy", type=StringType)
MARTE_HLAM_PpUnit.attributes={MARTE_HLAM_PpUnit_concPolicy}

# HLAM_MARTE_Behavior class attributes and methods

# HLAM_MARTE_Operation class attributes and methods

# MARTE_HLAM_RtFeature class attributes and methods

# HLAM_MARTE_BehavioralFeature class attributes and methods

# HLAM_MARTE_Message class attributes and methods

# HLAM_MARTE_Signal class attributes and methods

# HLAM_MARTE_Port class attributes and methods

# HLAM_MARTE_InvocationAction class attributes and methods

# HLAM_RtSpecification class attributes and methods

# Time_TimedInstantObservation class attributes and methods

# NFP_DateTime class attributes and methods

# NFP_Percentage class attributes and methods

# MARTE_HLAM_RtSpecification class attributes and methods

# UtilityType class attributes and methods

# ArrivalPattern class attributes and methods

# MARTE_HLAM_RtAction class attributes and methods
MARTE_HLAM_RtAction_isAtomic: Property = Property(name="isAtomic", type=StringType)
MARTE_HLAM_RtAction_synchKind: Property = Property(name="synchKind", type=StringType)
MARTE_HLAM_RtAction.attributes={MARTE_HLAM_RtAction_synchKind, MARTE_HLAM_RtAction_isAtomic}

# HLAM_MARTE_Comment class attributes and methods

# MARTE_HLAM_RtService class attributes and methods
MARTE_HLAM_RtService_concPolicy: Property = Property(name="concPolicy", type=StringType)
MARTE_HLAM_RtService_exeKind: Property = Property(name="exeKind", type=StringType)
MARTE_HLAM_RtService_isAtomic: Property = Property(name="isAtomic", type=StringType)
MARTE_HLAM_RtService_synchKind: Property = Property(name="synchKind", type=StringType)
MARTE_HLAM_RtService.attributes={MARTE_HLAM_RtService_concPolicy, MARTE_HLAM_RtService_isAtomic, MARTE_HLAM_RtService_synchKind, MARTE_HLAM_RtService_exeKind}

# MARTE_HwComputing_HwProcessor class attributes and methods

# HwComputingResource class attributes and methods

# MARTE_HwComputing_PLD_Organization class attributes and methods
MARTE_HwComputing_PLD_Organization_class: Property = Property(name="class", type=StringType)
MARTE_HwComputing_PLD_Organization.attributes={MARTE_HwComputing_PLD_Organization_class}

# NFP_Natural class attributes and methods

# HwComputing_HwISA class attributes and methods

# HwComputing_HwBranchPredictor class attributes and methods

# HwMemory_HwCache class attributes and methods

# HwStorageManager_HwMMU class attributes and methods

# MARTE_HwComputing_HwComputingResource class attributes and methods

# HwGeneral_HwResource class attributes and methods

# NFP_FrequencyInterval class attributes and methods

# MARTE_HwComputing_HwBranchPredictor class attributes and methods

# MARTE_HwComputing_HwASIC class attributes and methods

# MARTE_HwComputing_HwPLD class attributes and methods
MARTE_HwComputing_HwPLD_technology: Property = Property(name="technology", type=StringType)
MARTE_HwComputing_HwPLD.attributes={MARTE_HwComputing_HwPLD_technology}

# HwComputing_PLD_Organization class attributes and methods

# MARTE_HwComputing_HwISA class attributes and methods
MARTE_HwComputing_HwISA_type: Property = Property(name="type", type=StringType)
MARTE_HwComputing_HwISA.attributes={MARTE_HwComputing_HwISA_type}

# HwResource class attributes and methods

# NFP_String class attributes and methods

# MARTE_HwComputing_HwMCU class attributes and methods

# HwComputing_HwProcessor class attributes and methods

# HwDevice_HwPeripheral class attributes and methods

# HwRegister_HwRegister class attributes and methods

# HwPackage_HwPackage class attributes and methods

# HwIO_HwPin class attributes and methods

# HwCommunication_HwPort class attributes and methods

# HwMemory_HwRAM class attributes and methods

# HwComputing_HwComputingResource class attributes and methods

# MARTE_HwCommunication_HwMedia class attributes and methods

# GRM_CommunicationMedia class attributes and methods

# HwCommunication_HwCommunicationResource class attributes and methods

# HwCommunication_HwArbiter class attributes and methods

# MARTE_HwCommunication_HwBus class attributes and methods

# HwMedia class attributes and methods

# NFP_Boolean class attributes and methods

# MARTE_HwCommunication_HwCommunicationResource class attributes and methods

# MARTE_HwCommunication_HwArbiter class attributes and methods

# HwCommunicationResource class attributes and methods

# HwCommunication_HwMedia class attributes and methods

# MARTE_HwCommunication_HwBridge class attributes and methods

# MARTE_HwCommunication_HwEndPoint class attributes and methods

# GRM_CommunicationEndPoint class attributes and methods

# MARTE_HwCommunication_HwPort class attributes and methods

# HwEndPoint class attributes and methods

# HwProtocol_HwProtocol class attributes and methods

# MARTE_HwStorageManager_HwStorageManager class attributes and methods

# GRM_StorageResource class attributes and methods

# HwMemory_HwMemory class attributes and methods

# MARTE_HwStorageManager_HwDMA class attributes and methods

# HwStorageManager_HwStorageManager class attributes and methods

# MARTE_HwCommunication_HwConnection class attributes and methods

# MARTE_HwStorageManager_HwMMU class attributes and methods

# HwStorageManager class attributes and methods

# MARTE_HwMemory_HwMemory class attributes and methods

# MARTE_HwMemory_Timing class attributes and methods

# HwMemory_Timing class attributes and methods

# MARTE_HwMemory_CacheStructure class attributes and methods

# MARTE_HwMemory_MemoryOrganization class attributes and methods

# MARTE_HwMemory_HwRAM class attributes and methods
MARTE_HwMemory_HwRAM_repl_Policy: Property = Property(name="repl_Policy", type=StringType)
MARTE_HwMemory_HwRAM_writePolicy: Property = Property(name="writePolicy", type=StringType)
MARTE_HwMemory_HwRAM.attributes={MARTE_HwMemory_HwRAM_writePolicy, MARTE_HwMemory_HwRAM_repl_Policy}

# HwMemory class attributes and methods

# HwMemory_MemoryOrganization class attributes and methods

# MARTE_HwMemory_HwROM class attributes and methods
MARTE_HwMemory_HwROM_type: Property = Property(name="type", type=StringType)
MARTE_HwMemory_HwROM.attributes={MARTE_HwMemory_HwROM_type}

# MARTE_HwMemory_HwDrive class attributes and methods

# HwMemory_CacheStructure class attributes and methods

# MARTE_HwTiming_HwTimingResource class attributes and methods

# GRM_TimingResource class attributes and methods

# MARTE_HwTiming_HwClock class attributes and methods

# HwTimingResource class attributes and methods

# MARTE_HwTiming_HwTimer class attributes and methods

# MARTE_HwMemory_HwCache class attributes and methods
MARTE_HwMemory_HwCache_type: Property = Property(name="type", type=StringType)
MARTE_HwMemory_HwCache_repl_Policy: Property = Property(name="repl_Policy", type=StringType)
MARTE_HwMemory_HwCache_writePolicy: Property = Property(name="writePolicy", type=StringType)
MARTE_HwMemory_HwCache.attributes={MARTE_HwMemory_HwCache_writePolicy, MARTE_HwMemory_HwCache_type, MARTE_HwMemory_HwCache_repl_Policy}

# MARTE_HwDevice_HwDevice class attributes and methods

# GRM_DeviceResource class attributes and methods

# HwDeviceFunction_HwDeviceFunction class attributes and methods

# MARTE_HwDevice_HwI_O class attributes and methods

# HwDevice class attributes and methods

# MARTE_HwDevice_HwSupport class attributes and methods

# HwTiming_HwClock class attributes and methods

# HwPeripheral_OperationImpl class attributes and methods

# HwPeripheral_PeripheralActivity class attributes and methods

# MARTE_HwGeneral_HwResourceService class attributes and methods

# MARTE_HwDevice_HWActuator class attributes and methods

# HwI_O class attributes and methods

# MARTE_HwDevice_HWSensor class attributes and methods

# MARTE_HwDevice_HwPeripheral class attributes and methods

# HwGeneral_HwResourceService class attributes and methods

# HwCommunication_HwEndPoint class attributes and methods

# NFP_Frequency class attributes and methods

# HwGeneral_MARTE_Operation class attributes and methods

# HwGeneral_MARTE_Activity class attributes and methods

# MARTE_HwGeneral_HwResource class attributes and methods
MARTE_HwGeneral_HwResource_name: Property = Property(name="name", type=StringType)
MARTE_HwGeneral_HwResource.attributes={MARTE_HwGeneral_HwResource_name}

# NFP_Length class attributes and methods

# NFP_Area class attributes and methods

# NFP_NaturalInterval class attributes and methods

# MARTE_HwLayout_HwComponent class attributes and methods
MARTE_HwLayout_HwComponent_kind: Property = Property(name="kind", type=StringType)
MARTE_HwLayout_HwComponent.attributes={MARTE_HwLayout_HwComponent_kind}

# HwLayout_HwComponent class attributes and methods

# MARTE_HwLayout_Env_Condition class attributes and methods
MARTE_HwLayout_Env_Condition_type: Property = Property(name="type", type=StringType)
MARTE_HwLayout_Env_Condition_status: Property = Property(name="status", type=StringType)
MARTE_HwLayout_Env_Condition.attributes={MARTE_HwLayout_Env_Condition_type, MARTE_HwLayout_Env_Condition_status}

# NFP_Price class attributes and methods

# HwLayout_Env_Condition class attributes and methods

# MARTE_HwPower_HwPowerSupply class attributes and methods

# HwComponent class attributes and methods

# Realnterval class attributes and methods

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

# MARTE_HwPower_HwCoolingSupply class attributes and methods

# MARTE_HwPeripheral_OperationImpl class attributes and methods

# HwIO_HwLine class attributes and methods

# MARTE_HwIO_HwLine class attributes and methods

# MARTE_HwRegister_HwRegister class attributes and methods
MARTE_HwRegister_HwRegister_address: Property = Property(name="address", type=StringType)
MARTE_HwRegister_HwRegister.attributes={MARTE_HwRegister_HwRegister_address}

# MARTE_HwDatasheet_HwDatasheet class attributes and methods
MARTE_HwDatasheet_HwDatasheet_revision: Property = Property(name="revision", type=StringType)
MARTE_HwDatasheet_HwDatasheet_name: Property = Property(name="name", type=StringType)
MARTE_HwDatasheet_HwDatasheet.attributes={MARTE_HwDatasheet_HwDatasheet_name, MARTE_HwDatasheet_HwDatasheet_revision}

# MARTE_HwDeviceFunction_HwDeviceFunction class attributes and methods

# MARTE_HwIO_HwPin class attributes and methods

# HwPackage_HwPackagePin class attributes and methods

# MARTE_HwPackage_HwPackagePin class attributes and methods
MARTE_HwPackage_HwPackagePin_pinNo: Property = Property(name="pinNo", type=StringType)
MARTE_HwPackage_HwPackagePin_altNames: Property = Property(name="altNames", type=StringType)
MARTE_HwPackage_HwPackagePin.attributes={MARTE_HwPackage_HwPackagePin_pinNo, MARTE_HwPackage_HwPackagePin_altNames}

# HwPackage_HwWire class attributes and methods

# MARTE_HwPackage_HwWire class attributes and methods

# MARTE_HwProtocol_HwProtocol class attributes and methods
MARTE_HwProtocol_HwProtocol_name: Property = Property(name="name", type=StringType)
MARTE_HwProtocol_HwProtocol.attributes={MARTE_HwProtocol_HwProtocol_name}

# HwProtocol_MARTE_Operation class attributes and methods

# MARTE_HwDiagram_HwBlockDiagram class attributes and methods
MARTE_HwDiagram_HwBlockDiagram_name: Property = Property(name="name", type=StringType)
MARTE_HwDiagram_HwBlockDiagram.attributes={MARTE_HwDiagram_HwBlockDiagram_name}

# MARTE_HwPackage_HwPackage class attributes and methods
MARTE_HwPackage_HwPackage_name: Property = Property(name="name", type=StringType)
MARTE_HwPackage_HwPackage_pinNum: Property = Property(name="pinNum", type=IntegerType)
MARTE_HwPackage_HwPackage_packageType: Property = Property(name="packageType", type=StringType)
MARTE_HwPackage_HwPackage.attributes={MARTE_HwPackage_HwPackage_pinNum, MARTE_HwPackage_HwPackage_name, MARTE_HwPackage_HwPackage_packageType}

# MARTE_HwDiagram_HwCircuitDiagram class attributes and methods
MARTE_HwDiagram_HwCircuitDiagram_name: Property = Property(name="name", type=StringType)
MARTE_HwDiagram_HwCircuitDiagram.attributes={MARTE_HwDiagram_HwCircuitDiagram_name}

# MARTE_HwDiagram_HwHRMDiagram class attributes and methods
MARTE_HwDiagram_HwHRMDiagram_name: Property = Property(name="name", type=StringType)
MARTE_HwDiagram_HwHRMDiagram.attributes={MARTE_HwDiagram_HwHRMDiagram_name}

# HwCommunication_HwConnection class attributes and methods

# MARTE_HwDiagram_SRMDiagram class attributes and methods

# SW_Brokering_DeviceBroker class attributes and methods

# MARTE_SW_ResourceCore_SwResource class attributes and methods

# SW_ResourceCore_MARTE_TypedElement class attributes and methods

# HwDiagram_MARTE_DataType class attributes and methods

# MARTE_SW_ResourceCore_SwAccessService class attributes and methods
MARTE_SW_ResourceCore_SwAccessService_isModifier: Property = Property(name="isModifier", type=StringType)
MARTE_SW_ResourceCore_SwAccessService.attributes={MARTE_SW_ResourceCore_SwAccessService_isModifier}

# SW_ResourceCore_MARTE_Property class attributes and methods

# MARTE_SW_Concurrency_EntryPoint class attributes and methods
MARTE_SW_Concurrency_EntryPoint_isReentrant: Property = Property(name="isReentrant", type=StringType)
MARTE_SW_Concurrency_EntryPoint.attributes={MARTE_SW_Concurrency_EntryPoint_isReentrant}

# SW_ResourceCore_MARTE_BehavioralFeature class attributes and methods

# MARTE_SW_Concurrency_SwConcurrentResource class attributes and methods
MARTE_SW_Concurrency_SwConcurrentResource_activationCapacity: Property = Property(name="activationCapacity", type=StringType)
MARTE_SW_Concurrency_SwConcurrentResource.attributes={MARTE_SW_Concurrency_SwConcurrentResource_activationCapacity}

# SwResource class attributes and methods

# SW_Concurrency_MARTE_Element class attributes and methods

# SW_Concurrency_MARTE_TypedElement class attributes and methods

# SW_Concurrency_MARTE_BehavioralFeature class attributes and methods

# MARTE_SW_Concurrency_InterruptResource class attributes and methods
MARTE_SW_Concurrency_InterruptResource_kind: Property = Property(name="kind", type=StringType)
MARTE_SW_Concurrency_InterruptResource_isMaskable: Property = Property(name="isMaskable", type=StringType)
MARTE_SW_Concurrency_InterruptResource.attributes={MARTE_SW_Concurrency_InterruptResource_isMaskable, MARTE_SW_Concurrency_InterruptResource_kind}

# SwConcurrentResource class attributes and methods

# MARTE_SW_Concurrency_SwSchedulableResource class attributes and methods
MARTE_SW_Concurrency_SwSchedulableResource_isStaticSchedulingFeature: Property = Property(name="isStaticSchedulingFeature", type=StringType)
MARTE_SW_Concurrency_SwSchedulableResource_isPreemptable: Property = Property(name="isPreemptable", type=StringType)
MARTE_SW_Concurrency_SwSchedulableResource.attributes={MARTE_SW_Concurrency_SwSchedulableResource_isStaticSchedulingFeature, MARTE_SW_Concurrency_SwSchedulableResource_isPreemptable}

# SW_Concurrency_SwConcurrentResource class attributes and methods

# SW_Concurrency_MARTE_NamedElement class attributes and methods

# MARTE_SW_Concurrency_MemoryPartition class attributes and methods

# SW_Concurrency_MARTE_Namespace class attributes and methods

# MARTE_SW_Concurrency_Alarm class attributes and methods
MARTE_SW_Concurrency_Alarm_isWatchdog: Property = Property(name="isWatchdog", type=StringType)
MARTE_SW_Concurrency_Alarm.attributes={MARTE_SW_Concurrency_Alarm_isWatchdog}

# InterruptResource class attributes and methods

# MARTE_SW_Concurrency_SwTimerResource class attributes and methods

# TimerResource class attributes and methods

# MARTE_SW_Brokering_DeviceBroker class attributes and methods
MARTE_SW_Brokering_DeviceBroker_accessPolicy: Property = Property(name="accessPolicy", type=StringType)
MARTE_SW_Brokering_DeviceBroker_isBuffered: Property = Property(name="isBuffered", type=StringType)
MARTE_SW_Brokering_DeviceBroker_name: Property = Property(name="name", type=StringType)
MARTE_SW_Brokering_DeviceBroker.attributes={MARTE_SW_Brokering_DeviceBroker_name, MARTE_SW_Brokering_DeviceBroker_isBuffered, MARTE_SW_Brokering_DeviceBroker_accessPolicy}

# SW_Brokering_MARTE_TypedElement class attributes and methods

# SW_Brokering_MARTE_BehavioralFeature class attributes and methods

# SW_Brokering_MARTE_Operation class attributes and methods

# SW_Brokering_MARTE_Activity class attributes and methods

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

# MARTE_SW_Interaction_MessageComResource class attributes and methods
MARTE_SW_Interaction_MessageComResource_isFixedMessageSize: Property = Property(name="isFixedMessageSize", type=StringType)
MARTE_SW_Interaction_MessageComResource_mechanism: Property = Property(name="mechanism", type=StringType)
MARTE_SW_Interaction_MessageComResource_messageQueuePolicy: Property = Property(name="messageQueuePolicy", type=StringType)
MARTE_SW_Interaction_MessageComResource.attributes={MARTE_SW_Interaction_MessageComResource_messageQueuePolicy, MARTE_SW_Interaction_MessageComResource_isFixedMessageSize, MARTE_SW_Interaction_MessageComResource_mechanism}

# MARTE_SW_Interaction_NotificationResource class attributes and methods
MARTE_SW_Interaction_NotificationResource_mechanism: Property = Property(name="mechanism", type=StringType)
MARTE_SW_Interaction_NotificationResource_occurence: Property = Property(name="occurence", type=StringType)
MARTE_SW_Interaction_NotificationResource.attributes={MARTE_SW_Interaction_NotificationResource_occurence, MARTE_SW_Interaction_NotificationResource_mechanism}

# SwSynchronizationResource class attributes and methods

# SW_Interaction_MARTE_BehavioralFeature class attributes and methods

# MARTE_SW_Interaction_SwMutualExclusionResource class attributes and methods
MARTE_SW_Interaction_SwMutualExclusionResource_mechanism: Property = Property(name="mechanism", type=StringType)
MARTE_SW_Interaction_SwMutualExclusionResource_concurrentAccessProtocol: Property = Property(name="concurrentAccessProtocol", type=StringType)
MARTE_SW_Interaction_SwMutualExclusionResource.attributes={MARTE_SW_Interaction_SwMutualExclusionResource_mechanism, MARTE_SW_Interaction_SwMutualExclusionResource_concurrentAccessProtocol}

# SW_Interaction_SwSynchronizationResource class attributes and methods

# MARTE_GCM_FlowProperty class attributes and methods
MARTE_GCM_FlowProperty_direction: Property = Property(name="direction", type=StringType)
MARTE_GCM_FlowProperty.attributes={MARTE_GCM_FlowProperty_direction}

# GCM_MARTE_Property class attributes and methods

# MARTE_GCM_FlowPort class attributes and methods
MARTE_GCM_FlowPort_isAtomic: Property = Property(name="isAtomic", type=StringType)
MARTE_GCM_FlowPort_isConjugated: Property = Property(name="isConjugated", type=StringType)
MARTE_GCM_FlowPort_direction: Property = Property(name="direction", type=StringType)
MARTE_GCM_FlowPort.attributes={MARTE_GCM_FlowPort_direction, MARTE_GCM_FlowPort_isConjugated, MARTE_GCM_FlowPort_isAtomic}

# MARTE_GCM_ClientServerPort class attributes and methods
MARTE_GCM_ClientServerPort_specificationKind: Property = Property(name="specificationKind", type=StringType)
MARTE_GCM_ClientServerPort_isConjugated: Property = Property(name="isConjugated", type=StringType)
MARTE_GCM_ClientServerPort_kind: Property = Property(name="kind", type=StringType)
MARTE_GCM_ClientServerPort.attributes={MARTE_GCM_ClientServerPort_kind, MARTE_GCM_ClientServerPort_specificationKind, MARTE_GCM_ClientServerPort_isConjugated}

# GCM_MARTE_Interface class attributes and methods

# GCM_ClientServerSpecification class attributes and methods

# GCM_MARTE_Port class attributes and methods

# MARTE_GCM_ClientServerSpecification class attributes and methods

# MARTE_GCM_FlowSpecification class attributes and methods

# MARTE_GCM_ClientServerFeature class attributes and methods
MARTE_GCM_ClientServerFeature_kind: Property = Property(name="kind", type=StringType)
MARTE_GCM_ClientServerFeature.attributes={MARTE_GCM_ClientServerFeature_kind}

# GCM_MARTE_BehavioralFeature class attributes and methods

# MARTE_GCM_GCMTrigger class attributes and methods

# GCM_MARTE_Trigger class attributes and methods

# GCM_MARTE_InvocationAction class attributes and methods

# MARTE_GCM_DataEvent class attributes and methods

# GCM_MARTE_AnyReceiveEvent class attributes and methods

# GCM_MARTE_Classifier class attributes and methods

# MARTE_GCM_DataPool class attributes and methods
MARTE_GCM_DataPool_ordering: Property = Property(name="ordering", type=StringType)
MARTE_GCM_DataPool.attributes={MARTE_GCM_DataPool_ordering}

# GCM_MARTE_Behavior class attributes and methods

# GCM_MARTE_Feature class attributes and methods

# MARTE_GCM_GCMInvocationAction class attributes and methods

# MARTE_GQAM_GaWorkloadGenerator class attributes and methods

# GQAM_MARTE_Behavior class attributes and methods

# GQAM_GaEventTrace class attributes and methods

# GQAM_GaScenario class attributes and methods

# GQAM_MARTE_TimeEvent class attributes and methods

# MARTE_GQAM_GaEventTrace class attributes and methods
MARTE_GQAM_GaEventTrace_content: Property = Property(name="content", type=StringType)
MARTE_GQAM_GaEventTrace_format: Property = Property(name="format", type=StringType)
MARTE_GQAM_GaEventTrace_location: Property = Property(name="location", type=StringType)
MARTE_GQAM_GaEventTrace.attributes={MARTE_GQAM_GaEventTrace_location, MARTE_GQAM_GaEventTrace_format, MARTE_GQAM_GaEventTrace_content}

# GQAM_MARTE_NamedElement class attributes and methods

# MARTE_GQAM_GaWorkloadEvent class attributes and methods

# GQAM_GaWorkloadGenerator class attributes and methods

# MARTE_GQAM_GaScenario class attributes and methods

# Time_TimedProcessing class attributes and methods

# GQAM_GaWorkloadEvent class attributes and methods

# GQAM_GaStep class attributes and methods

# GQAM_GaTimedObs class attributes and methods

# MARTE_GQAM_GaStep class attributes and methods

# GaScenario class attributes and methods

# MARTE_GQAM_GaExecHost class attributes and methods

# GQAM_GaExecHost class attributes and methods

# GQAM_GaRequestedService class attributes and methods

# MARTE_GQAM_GaRequestedService class attributes and methods

# GaStep class attributes and methods

# IntegerInterval class attributes and methods

# MARTE_GQAM_GaCommStep class attributes and methods

# MARTE_GQAM_GaAcqStep class attributes and methods

# MARTE_GQAM_GaRelStep class attributes and methods

# GQAM_MARTE_Operation class attributes and methods

# MARTE_GQAM_GaTimedObs class attributes and methods
MARTE_GQAM_GaTimedObs_laxity: Property = Property(name="laxity", type=StringType)
MARTE_GQAM_GaTimedObs.attributes={MARTE_GQAM_GaTimedObs_laxity}

# NfpConstraint class attributes and methods

# GQAM_MARTE_TimeObservation class attributes and methods

# MARTE_GQAM_GaCommHost class attributes and methods

# MARTE_GQAM_GaLatencyObs class attributes and methods

# GaTimedObs class attributes and methods

# MARTE_GQAM_GaAnalysisContext class attributes and methods

# CoreElements_Configuration class attributes and methods

# Variables_ExpressionContext class attributes and methods

# MARTE_GQAM_GaCommChannel class attributes and methods

# SchedulableResource class attributes and methods

# MARTE_GQAM_GaWorkloadBehavior class attributes and methods

# MARTE_SAM_SaAnalysisContext class attributes and methods
MARTE_SAM_SaAnalysisContext_optCriterion: Property = Property(name="optCriterion", type=StringType)
MARTE_SAM_SaAnalysisContext.attributes={MARTE_SAM_SaAnalysisContext_optCriterion}

# GaAnalysisContext class attributes and methods

# MARTE_SAM_SaEndtoEndFlow class attributes and methods

# GQAM_GaWorkloadBehavior class attributes and methods

# GQAM_GaResourcesPlatform class attributes and methods

# MARTE_GQAM_GaResourcesPlatform class attributes and methods

# GQAM_MARTE_Classifier class attributes and methods

# SAM_MARTE_NamedElement class attributes and methods

# MARTE_SAM_SaCommStep class attributes and methods

# GaCommStep class attributes and methods

# SAM_MARTE_BehavioralFeature class attributes and methods

# MARTE_SAM_SaStep class attributes and methods

# MARTE_SAM_SaSharedResource class attributes and methods

# MutualExclusionResource class attributes and methods

# SAM_SaSharedResource class attributes and methods

# MARTE_SAM_SaCommHost class attributes and methods

# GaCommHost class attributes and methods

# MARTE_SAM_SaSchedObs class attributes and methods

# MARTE_PAM_PaStep class attributes and methods
MARTE_PAM_PaStep_extOpDemand: Property = Property(name="extOpDemand", type=StringType)
MARTE_PAM_PaStep.attributes={MARTE_PAM_PaStep_extOpDemand}

# MARTE_SAM_SaExecHost class attributes and methods

# GaExecHost class attributes and methods

# MARTE_PAM_PaCommStep class attributes and methods

# GQAM_GaCommStep class attributes and methods

# MARTE_PAM_PaResPassStep class attributes and methods

# MARTE_PAM_PaLogicalResource class attributes and methods

# MARTE_PAM_PaRequestedStep class attributes and methods

# PAM_PaStep class attributes and methods

# MARTE_PAM_PaRunTInstance class attributes and methods
MARTE_PAM_PaRunTInstance_unbddPool: Property = Property(name="unbddPool", type=StringType)
MARTE_PAM_PaRunTInstance.attributes={MARTE_PAM_PaRunTInstance_unbddPool}

# PAM_MARTE_NamedElement class attributes and methods

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
from39: BinaryAssociation = BinaryAssociation(
    name="from39",
    ends={
        Property(name="Alloc_MARTE_Element", type=MARTE_Alloc_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Alloc_Assign40", type=Alloc_MARTE_Element, multiplicity=Multiplicity(1, 9999))
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
base_Property57: BinaryAssociation = BinaryAssociation(
    name="base_Property57",
    ends={
        Property(name="MARTE_Time_Clock58", type=Time_MARTE_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Time_MARTE_Property", type=MARTE_Time_Clock, multiplicity=Multiplicity(1, 1))
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
base_DurationObservation82: BinaryAssociation = BinaryAssociation(
    name="base_DurationObservation82",
    ends={
        Property(name="Time_MARTE_DurationObservation", type=MARTE_Time_TimedDurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedDurationObservation", type=Time_MARTE_DurationObservation, multiplicity=Multiplicity(1, 1))
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
base_TimeObservation81: BinaryAssociation = BinaryAssociation(
    name="base_TimeObservation81",
    ends={
        Property(name="Time_MARTE_TimeObservation", type=MARTE_Time_TimedInstantObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Time_TimedInstantObservation", type=Time_MARTE_TimeObservation, multiplicity=Multiplicity(1, 1))
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
base_Classifier105: BinaryAssociation = BinaryAssociation(
    name="base_Classifier105",
    ends={
        Property(name="GRM_MARTE_Classifier", type=MARTE_GRM_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_Resource106", type=GRM_MARTE_Classifier, multiplicity=Multiplicity(0, 1))
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
protectedSharedRsources120: BinaryAssociation = BinaryAssociation(
    name="protectedSharedRsources120",
    ends={
        Property(name="MARTE_Foundations", type=MARTE_GRM_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="GRM", type=GRM_MutualExclusionResource, multiplicity=Multiplicity(0, 9999))
    }
)
schedulableResources121: BinaryAssociation = BinaryAssociation(
    name="schedulableResources121",
    ends={
        Property(name="MARTE_Foundations123", type=MARTE_GRM_Scheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="GRM122", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 9999))
    }
)
speedFactor124: BinaryAssociation = BinaryAssociation(
    name="speedFactor124",
    ends={
        Property(name="NFP_Real", type=MARTE_GRM_ProcessingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ProcessingResource", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mainScheduler125: BinaryAssociation = BinaryAssociation(
    name="mainScheduler125",
    ends={
        Property(name="GRM_Scheduler", type=MARTE_GRM_ProcessingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ProcessingResource126", type=GRM_Scheduler, multiplicity=Multiplicity(0, 1))
    }
)
ceiling127: BinaryAssociation = BinaryAssociation(
    name="ceiling127",
    ends={
        Property(name="NFP_Integer128", type=MARTE_GRM_MutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_MutualExclusionResource", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
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
schedParams132: BinaryAssociation = BinaryAssociation(
    name="schedParams132",
    ends={
        Property(name="MARTE_GRM_SchedulableResource", type=SchedParameters, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="SchedParameters", type=MARTE_GRM_SchedulableResource, multiplicity=Multiplicity(1, 1))
    }
)
dependentScheduler133: BinaryAssociation = BinaryAssociation(
    name="dependentScheduler133",
    ends={
        Property(name="MARTE_Foundations135", type=MARTE_GRM_SchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="GRM134", type=GRM_SecondaryScheduler, multiplicity=Multiplicity(0, 1))
    }
)
host136: BinaryAssociation = BinaryAssociation(
    name="host136",
    ends={
        Property(name="MARTE_Foundations138", type=MARTE_GRM_SchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="GRM137", type=GRM_Scheduler, multiplicity=Multiplicity(0, 1))
    }
)
virtualProcessingUnits139: BinaryAssociation = BinaryAssociation(
    name="virtualProcessingUnits139",
    ends={
        Property(name="MARTE_Foundations141", type=MARTE_GRM_SecondaryScheduler, multiplicity=Multiplicity(1, 1)),
        Property(name="GRM140", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 9999))
    }
)
elementSize142: BinaryAssociation = BinaryAssociation(
    name="elementSize142",
    ends={
        Property(name="NFP_Integer143", type=MARTE_GRM_CommunicationMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationMedia", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_Connector144: BinaryAssociation = BinaryAssociation(
    name="base_Connector144",
    ends={
        Property(name="GRM_MARTE_Connector", type=MARTE_GRM_CommunicationMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationMedia145", type=GRM_MARTE_Connector, multiplicity=Multiplicity(0, 1))
    }
)
scheduler129: BinaryAssociation = BinaryAssociation(
    name="scheduler129",
    ends={
        Property(name="MARTE_Foundations131", type=MARTE_GRM_MutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="GRM130", type=GRM_Scheduler, multiplicity=Multiplicity(0, 1))
    }
)
duration153: BinaryAssociation = BinaryAssociation(
    name="duration153",
    ends={
        Property(name="NFP_Duration154", type=MARTE_GRM_TimerResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_TimerResource", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner155: BinaryAssociation = BinaryAssociation(
    name="owner155",
    ends={
        Property(name="GRM_Resource", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)
base_ExecutionSpecification156: BinaryAssociation = BinaryAssociation(
    name="base_ExecutionSpecification156",
    ends={
        Property(name="GRM_MARTE_ExecutionSpecification", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService157", type=GRM_MARTE_ExecutionSpecification, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature158: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature158",
    ends={
        Property(name="GRM_MARTE_BehavioralFeature", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService159", type=GRM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
blockT146: BinaryAssociation = BinaryAssociation(
    name="blockT146",
    ends={
        Property(name="NFP_Duration", type=MARTE_GRM_CommunicationMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationMedia147", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packetT148: BinaryAssociation = BinaryAssociation(
    name="packetT148",
    ends={
        Property(name="NFP_Duration150", type=MARTE_GRM_CommunicationMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationMedia149", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capacity151: BinaryAssociation = BinaryAssociation(
    name="capacity151",
    ends={
        Property(name="NFP_DataTxRate", type=MARTE_GRM_CommunicationMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_CommunicationMedia152", type=NFP_DataTxRate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base_CollaborationUse164: BinaryAssociation = BinaryAssociation(
    name="base_CollaborationUse164",
    ends={
        Property(name="GRM_MARTE_CollaborationUse", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService165", type=GRM_MARTE_CollaborationUse, multiplicity=Multiplicity(1, 1))
    }
)
execTime166: BinaryAssociation = BinaryAssociation(
    name="execTime166",
    ends={
        Property(name="NFP_Duration167", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allocatedMemory168: BinaryAssociation = BinaryAssociation(
    name="allocatedMemory168",
    ends={
        Property(name="NFP_DataSize", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage169", type=NFP_DataSize, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedMemory170: BinaryAssociation = BinaryAssociation(
    name="usedMemory170",
    ends={
        Property(name="NFP_DataSize172", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage171", type=NFP_DataSize, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powerPeak173: BinaryAssociation = BinaryAssociation(
    name="powerPeak173",
    ends={
        Property(name="NFP_Power", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage174", type=NFP_Power, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
energy175: BinaryAssociation = BinaryAssociation(
    name="energy175",
    ends={
        Property(name="NFP_Energy", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage176", type=NFP_Energy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base_Behavior160: BinaryAssociation = BinaryAssociation(
    name="base_Behavior160",
    ends={
        Property(name="GRM_MARTE_Behavior", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService161", type=GRM_MARTE_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
base_Collaboration162: BinaryAssociation = BinaryAssociation(
    name="base_Collaboration162",
    ends={
        Property(name="GRM_MARTE_Collaboration", type=MARTE_GRM_GrService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_GrService163", type=GRM_MARTE_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
usedResources181: BinaryAssociation = BinaryAssociation(
    name="usedResources181",
    ends={
        Property(name="GRM_Resource183", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage182", type=GRM_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
msgSize184: BinaryAssociation = BinaryAssociation(
    name="msgSize184",
    ends={
        Property(name="NFP_DataSize186", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage185", type=NFP_DataSize, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base_Connector187: BinaryAssociation = BinaryAssociation(
    name="base_Connector187",
    ends={
        Property(name="RSM_MARTE_Connector", type=MARTE_RSM_LinkTopology, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_LinkTopology", type=RSM_MARTE_Connector, multiplicity=Multiplicity(1, 1))
    }
)
repetitionShapeDependence188: BinaryAssociation = BinaryAssociation(
    name="repetitionShapeDependence188",
    ends={
        Property(name="IntegerVector", type=MARTE_RSM_InterRepetition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_InterRepetition", type=IntegerVector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
base_NamedElement177: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement177",
    ends={
        Property(name="GRM_MARTE_NamedElement", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage178", type=GRM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
subUsage179: BinaryAssociation = BinaryAssociation(
    name="subUsage179",
    ends={
        Property(name="GRM_ResourceUsage", type=MARTE_GRM_ResourceUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GRM_ResourceUsage180", type=GRM_ResourceUsage, multiplicity=Multiplicity(0, 9999))
    }
)
fromTiler193: BinaryAssociation = BinaryAssociation(
    name="fromTiler193",
    ends={
        Property(name="MARTE_RSM_Distribute194", type=TilerSpecification, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="TilerSpecification", type=MARTE_RSM_Distribute, multiplicity=Multiplicity(1, 1))
    }
)
toTiler195: BinaryAssociation = BinaryAssociation(
    name="toTiler195",
    ends={
        Property(name="TilerSpecification197", type=MARTE_RSM_Distribute, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Distribute196", type=TilerSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
patternShape198: BinaryAssociation = BinaryAssociation(
    name="patternShape198",
    ends={
        Property(name="ShapeSpecification199", type=MARTE_RSM_Reshape, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Reshape", type=ShapeSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
repetitonShape200: BinaryAssociation = BinaryAssociation(
    name="repetitonShape200",
    ends={
        Property(name="ShapeSpecification202", type=MARTE_RSM_Reshape, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Reshape201", type=ShapeSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
origin203: BinaryAssociation = BinaryAssociation(
    name="origin203",
    ends={
        Property(name="IntegerVector204", type=MARTE_RSM_Tiler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Tiler", type=IntegerVector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paving205: BinaryAssociation = BinaryAssociation(
    name="paving205",
    ends={
        Property(name="IntegerMatrix", type=MARTE_RSM_Tiler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Tiler206", type=IntegerMatrix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
patternShape189: BinaryAssociation = BinaryAssociation(
    name="patternShape189",
    ends={
        Property(name="ShapeSpecification", type=MARTE_RSM_Distribute, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Distribute", type=ShapeSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
repetitionSpace190: BinaryAssociation = BinaryAssociation(
    name="repetitionSpace190",
    ends={
        Property(name="ShapeSpecification192", type=MARTE_RSM_Distribute, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Distribute191", type=ShapeSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
shape215: BinaryAssociation = BinaryAssociation(
    name="shape215",
    ends={
        Property(name="ShapeSpecification216", type=MARTE_RSM_Shaped, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Shaped", type=ShapeSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
base_MultiplicityElement217: BinaryAssociation = BinaryAssociation(
    name="base_MultiplicityElement217",
    ends={
        Property(name="RSM_MARTE_MultiplicityElement", type=MARTE_RSM_Shaped, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Shaped218", type=RSM_MARTE_MultiplicityElement, multiplicity=Multiplicity(1, 1))
    }
)
base_Property219: BinaryAssociation = BinaryAssociation(
    name="base_Property219",
    ends={
        Property(name="Variables_MARTE_Property", type=MARTE_Variables_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Variables_Var", type=Variables_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_NamedElement220: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement220",
    ends={
        Property(name="Variables_MARTE_NamedElement", type=MARTE_Variables_ExpressionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_Variables_ExpressionContext", type=Variables_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
fitting207: BinaryAssociation = BinaryAssociation(
    name="fitting207",
    ends={
        Property(name="IntegerMatrix209", type=MARTE_RSM_Tiler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Tiler208", type=IntegerMatrix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tiler210: BinaryAssociation = BinaryAssociation(
    name="tiler210",
    ends={
        Property(name="TilerSpecification212", type=MARTE_RSM_Tiler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Tiler211", type=TilerSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_ConnectorEnd213: BinaryAssociation = BinaryAssociation(
    name="base_ConnectorEnd213",
    ends={
        Property(name="RSM_MARTE_ConnectorEnd", type=MARTE_RSM_Tiler, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_RSM_Tiler214", type=RSM_MARTE_ConnectorEnd, multiplicity=Multiplicity(1, 1))
    }
)
base_DataType222: BinaryAssociation = BinaryAssociation(
    name="base_DataType222",
    ends={
        Property(name="DataTypes_MARTE_DataType", type=MARTE_DataTypes_BoundedSubtype, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_BoundedSubtype223", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
intervalAttrib224: BinaryAssociation = BinaryAssociation(
    name="intervalAttrib224",
    ends={
        Property(name="DataTypes_MARTE_Property225", type=MARTE_DataTypes_IntervalType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_IntervalType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_DataType226: BinaryAssociation = BinaryAssociation(
    name="base_DataType226",
    ends={
        Property(name="DataTypes_MARTE_DataType228", type=MARTE_DataTypes_IntervalType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_IntervalType227", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
collectionAttrib229: BinaryAssociation = BinaryAssociation(
    name="collectionAttrib229",
    ends={
        Property(name="DataTypes_MARTE_Property230", type=MARTE_DataTypes_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_CollectionType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_DataType231: BinaryAssociation = BinaryAssociation(
    name="base_DataType231",
    ends={
        Property(name="DataTypes_MARTE_DataType233", type=MARTE_DataTypes_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_CollectionType232", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
baseType221: BinaryAssociation = BinaryAssociation(
    name="baseType221",
    ends={
        Property(name="DataTypes_MARTE_Property", type=MARTE_DataTypes_BoundedSubtype, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_BoundedSubtype", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
defaultAttrib236: BinaryAssociation = BinaryAssociation(
    name="defaultAttrib236",
    ends={
        Property(name="MARTE_DataTypes_ChoiceType237", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(0, 1)),
        Property(name="DataTypes_MARTE_Property238", type=MARTE_DataTypes_ChoiceType, multiplicity=Multiplicity(1, 1))
    }
)
base_DataType239: BinaryAssociation = BinaryAssociation(
    name="base_DataType239",
    ends={
        Property(name="DataTypes_MARTE_DataType241", type=MARTE_DataTypes_ChoiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_ChoiceType240", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
tupleAttrib242: BinaryAssociation = BinaryAssociation(
    name="tupleAttrib242",
    ends={
        Property(name="DataTypes_MARTE_Property243", type=MARTE_DataTypes_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_TupleType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(0, 9999))
    }
)
base_DataType244: BinaryAssociation = BinaryAssociation(
    name="base_DataType244",
    ends={
        Property(name="DataTypes_MARTE_DataType246", type=MARTE_DataTypes_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_TupleType245", type=DataTypes_MARTE_DataType, multiplicity=Multiplicity(1, 1))
    }
)
choiceAttrib234: BinaryAssociation = BinaryAssociation(
    name="choiceAttrib234",
    ends={
        Property(name="DataTypes_MARTE_Property235", type=MARTE_DataTypes_ChoiceType, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_DataTypes_ChoiceType", type=DataTypes_MARTE_Property, multiplicity=Multiplicity(0, 9999))
    }
)
main251: BinaryAssociation = BinaryAssociation(
    name="main251",
    ends={
        Property(name="HLAM_MARTE_Operation", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit252", type=HLAM_MARTE_Operation, multiplicity=Multiplicity(0, 1))
    }
)
memorySize253: BinaryAssociation = BinaryAssociation(
    name="memorySize253",
    ends={
        Property(name="NFP_DataSize255", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit254", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_BehavioredClassifier256: BinaryAssociation = BinaryAssociation(
    name="base_BehavioredClassifier256",
    ends={
        Property(name="HLAM_MARTE_BehavioredClassifier", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit257", type=HLAM_MARTE_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
msgMaxSize258: BinaryAssociation = BinaryAssociation(
    name="msgMaxSize258",
    ends={
        Property(name="NFP_DataSize260", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit259", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
srPoolWaitingTime247: BinaryAssociation = BinaryAssociation(
    name="srPoolWaitingTime247",
    ends={
        Property(name="NFP_Duration248", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationalMode249: BinaryAssociation = BinaryAssociation(
    name="operationalMode249",
    ends={
        Property(name="HLAM_MARTE_Behavior", type=MARTE_HLAM_RtUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtUnit250", type=HLAM_MARTE_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
base_BehavioralFeature266: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature266",
    ends={
        Property(name="HLAM_MARTE_BehavioralFeature", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature", type=HLAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Message267: BinaryAssociation = BinaryAssociation(
    name="base_Message267",
    ends={
        Property(name="HLAM_MARTE_Message", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature268", type=HLAM_MARTE_Message, multiplicity=Multiplicity(1, 1))
    }
)
base_Signal269: BinaryAssociation = BinaryAssociation(
    name="base_Signal269",
    ends={
        Property(name="HLAM_MARTE_Signal", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature270", type=HLAM_MARTE_Signal, multiplicity=Multiplicity(1, 1))
    }
)
base_Port271: BinaryAssociation = BinaryAssociation(
    name="base_Port271",
    ends={
        Property(name="HLAM_MARTE_Port", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature272", type=HLAM_MARTE_Port, multiplicity=Multiplicity(1, 1))
    }
)
base_InvocationAction273: BinaryAssociation = BinaryAssociation(
    name="base_InvocationAction273",
    ends={
        Property(name="HLAM_MARTE_InvocationAction", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature274", type=HLAM_MARTE_InvocationAction, multiplicity=Multiplicity(1, 1))
    }
)
specification275: BinaryAssociation = BinaryAssociation(
    name="specification275",
    ends={
        Property(name="HLAM_RtSpecification", type=MARTE_HLAM_RtFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtFeature276", type=HLAM_RtSpecification, multiplicity=Multiplicity(1, 9999))
    }
)
memorySize261: BinaryAssociation = BinaryAssociation(
    name="memorySize261",
    ends={
        Property(name="NFP_DataSize262", type=MARTE_HLAM_PpUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_PpUnit", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_BehavioredClassifier263: BinaryAssociation = BinaryAssociation(
    name="base_BehavioredClassifier263",
    ends={
        Property(name="HLAM_MARTE_BehavioredClassifier265", type=MARTE_HLAM_PpUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_PpUnit264", type=HLAM_MARTE_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
tRef280: BinaryAssociation = BinaryAssociation(
    name="tRef280",
    ends={
        Property(name="Time_TimedInstantObservation", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification281", type=Time_TimedInstantObservation, multiplicity=Multiplicity(0, 1))
    }
)
relDl282: BinaryAssociation = BinaryAssociation(
    name="relDl282",
    ends={
        Property(name="NFP_Duration284", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification283", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
absDl285: BinaryAssociation = BinaryAssociation(
    name="absDl285",
    ends={
        Property(name="NFP_DateTime", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification286", type=NFP_DateTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boundDl287: BinaryAssociation = BinaryAssociation(
    name="boundDl287",
    ends={
        Property(name="NFP_Duration289", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification288", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rdTime290: BinaryAssociation = BinaryAssociation(
    name="rdTime290",
    ends={
        Property(name="NFP_Duration292", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification291", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
miss293: BinaryAssociation = BinaryAssociation(
    name="miss293",
    ends={
        Property(name="NFP_Percentage", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification294", type=NFP_Percentage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
priority295: BinaryAssociation = BinaryAssociation(
    name="priority295",
    ends={
        Property(name="NFP_Integer297", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification296", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
utility277: BinaryAssociation = BinaryAssociation(
    name="utility277",
    ends={
        Property(name="UtilityType", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification", type=UtilityType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
occKind278: BinaryAssociation = BinaryAssociation(
    name="occKind278",
    ends={
        Property(name="ArrivalPattern", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification279", type=ArrivalPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
msgSize300: BinaryAssociation = BinaryAssociation(
    name="msgSize300",
    ends={
        Property(name="NFP_DataSize301", type=MARTE_HLAM_RtAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtAction", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_BehavioralFeature302: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature302",
    ends={
        Property(name="HLAM_MARTE_BehavioralFeature304", type=MARTE_HLAM_RtAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtAction303", type=HLAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_InvocationAction305: BinaryAssociation = BinaryAssociation(
    name="base_InvocationAction305",
    ends={
        Property(name="HLAM_MARTE_InvocationAction307", type=MARTE_HLAM_RtAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtAction306", type=HLAM_MARTE_InvocationAction, multiplicity=Multiplicity(1, 1))
    }
)
base_Comment298: BinaryAssociation = BinaryAssociation(
    name="base_Comment298",
    ends={
        Property(name="HLAM_MARTE_Comment", type=MARTE_HLAM_RtSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtSpecification299", type=HLAM_MARTE_Comment, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature308: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature308",
    ends={
        Property(name="HLAM_MARTE_BehavioralFeature309", type=MARTE_HLAM_RtService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HLAM_RtService", type=HLAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
architecture314: BinaryAssociation = BinaryAssociation(
    name="architecture314",
    ends={
        Property(name="NFP_DataSize315", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor", type=NFP_DataSize, multiplicity=Multiplicity(0, 1))
    }
)
mips316: BinaryAssociation = BinaryAssociation(
    name="mips316",
    ends={
        Property(name="NFP_Natural318", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor317", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ipc319: BinaryAssociation = BinaryAssociation(
    name="ipc319",
    ends={
        Property(name="NFP_Real321", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor320", type=NFP_Real, multiplicity=Multiplicity(0, 1))
    }
)
nbCores322: BinaryAssociation = BinaryAssociation(
    name="nbCores322",
    ends={
        Property(name="NFP_Natural324", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor323", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbPipelines325: BinaryAssociation = BinaryAssociation(
    name="nbPipelines325",
    ends={
        Property(name="NFP_Natural327", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor326", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbStages328: BinaryAssociation = BinaryAssociation(
    name="nbStages328",
    ends={
        Property(name="NFP_Natural330", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor329", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbRows310: BinaryAssociation = BinaryAssociation(
    name="nbRows310",
    ends={
        Property(name="NFP_Integer311", type=MARTE_HwComputing_PLD_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_PLD_Organization", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbColumns312: BinaryAssociation = BinaryAssociation(
    name="nbColumns312",
    ends={
        Property(name="NFP_Natural", type=MARTE_HwComputing_PLD_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_PLD_Organization313", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedISAs337: BinaryAssociation = BinaryAssociation(
    name="ownedISAs337",
    ends={
        Property(name="HwComputing_HwISA", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor338", type=HwComputing_HwISA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predictors339: BinaryAssociation = BinaryAssociation(
    name="predictors339",
    ends={
        Property(name="HwComputing_HwBranchPredictor", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor340", type=HwComputing_HwBranchPredictor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caches341: BinaryAssociation = BinaryAssociation(
    name="caches341",
    ends={
        Property(name="HwMemory_HwCache", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor342", type=HwMemory_HwCache, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMMUs343: BinaryAssociation = BinaryAssociation(
    name="ownedMMUs343",
    ends={
        Property(name="HwStorageManager_HwMMU", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor344", type=HwStorageManager_HwMMU, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op_Frequencies345: BinaryAssociation = BinaryAssociation(
    name="op_Frequencies345",
    ends={
        Property(name="NFP_FrequencyInterval", type=MARTE_HwComputing_HwComputingResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwComputingResource", type=NFP_FrequencyInterval, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbALUs331: BinaryAssociation = BinaryAssociation(
    name="nbALUs331",
    ends={
        Property(name="NFP_Natural333", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor332", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbFPUs334: BinaryAssociation = BinaryAssociation(
    name="nbFPUs334",
    ends={
        Property(name="NFP_Natural336", type=MARTE_HwComputing_HwProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwProcessor335", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization350: BinaryAssociation = BinaryAssociation(
    name="organization350",
    ends={
        Property(name="HwComputing_PLD_Organization", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD", type=HwComputing_PLD_Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbLUTs351: BinaryAssociation = BinaryAssociation(
    name="nbLUTs351",
    ends={
        Property(name="NFP_Natural353", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD352", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ndLUT_Inputs354: BinaryAssociation = BinaryAssociation(
    name="ndLUT_Inputs354",
    ends={
        Property(name="NFP_Natural356", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD355", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbFlipFlops357: BinaryAssociation = BinaryAssociation(
    name="nbFlipFlops357",
    ends={
        Property(name="NFP_Natural359", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD358", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
family346: BinaryAssociation = BinaryAssociation(
    name="family346",
    ends={
        Property(name="NFP_String", type=MARTE_HwComputing_HwISA, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwISA", type=NFP_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inst_Width347: BinaryAssociation = BinaryAssociation(
    name="inst_Width347",
    ends={
        Property(name="NFP_DataSize349", type=MARTE_HwComputing_HwISA, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwISA348", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processor364: BinaryAssociation = BinaryAssociation(
    name="processor364",
    ends={
        Property(name="HwComputing_HwProcessor", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU", type=HwComputing_HwProcessor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
peripherals365: BinaryAssociation = BinaryAssociation(
    name="peripherals365",
    ends={
        Property(name="HwDevice_HwPeripheral", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU366", type=HwDevice_HwPeripheral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sfr367: BinaryAssociation = BinaryAssociation(
    name="sfr367",
    ends={
        Property(name="HwRegister_HwRegister", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU368", type=HwRegister_HwRegister, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages369: BinaryAssociation = BinaryAssociation(
    name="packages369",
    ends={
        Property(name="HwPackage_HwPackage", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU370", type=HwPackage_HwPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pins371: BinaryAssociation = BinaryAssociation(
    name="pins371",
    ends={
        Property(name="HwIO_HwPin", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU372", type=HwIO_HwPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports373: BinaryAssociation = BinaryAssociation(
    name="ports373",
    ends={
        Property(name="HwCommunication_HwPort", type=MARTE_HwComputing_HwMCU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwMCU374", type=HwCommunication_HwPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blocksRAM360: BinaryAssociation = BinaryAssociation(
    name="blocksRAM360",
    ends={
        Property(name="HwMemory_HwRAM", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD361", type=HwMemory_HwRAM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blocksComputing362: BinaryAssociation = BinaryAssociation(
    name="blocksComputing362",
    ends={
        Property(name="HwComputing_HwComputingResource", type=MARTE_HwComputing_HwPLD, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwComputing_HwPLD363", type=HwComputing_HwComputingResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bandWidth376: BinaryAssociation = BinaryAssociation(
    name="bandWidth376",
    ends={
        Property(name="NFP_DataTxRate377", type=MARTE_HwCommunication_HwMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwMedia", type=NFP_DataTxRate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arbiters378: BinaryAssociation = BinaryAssociation(
    name="arbiters378",
    ends={
        Property(name="MARTE_DesignModel380", type=MARTE_HwCommunication_HwMedia, multiplicity=Multiplicity(1, 1)),
        Property(name="HRM379", type=HwCommunication_HwArbiter, multiplicity=Multiplicity(0, 9999))
    }
)
adressWidth381: BinaryAssociation = BinaryAssociation(
    name="adressWidth381",
    ends={
        Property(name="NFP_DataSize382", type=MARTE_HwCommunication_HwBus, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwBus", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wordWidth383: BinaryAssociation = BinaryAssociation(
    name="wordWidth383",
    ends={
        Property(name="NFP_DataSize385", type=MARTE_HwCommunication_HwBus, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwBus384", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isSynchronous386: BinaryAssociation = BinaryAssociation(
    name="isSynchronous386",
    ends={
        Property(name="NFP_Boolean", type=MARTE_HwCommunication_HwBus, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwBus387", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
controlledMedias375: BinaryAssociation = BinaryAssociation(
    name="controlledMedias375",
    ends={
        Property(name="MARTE_DesignModel", type=MARTE_HwCommunication_HwArbiter, multiplicity=Multiplicity(1, 1)),
        Property(name="HRM", type=HwCommunication_HwMedia, multiplicity=Multiplicity(0, 9999))
    }
)
sides391: BinaryAssociation = BinaryAssociation(
    name="sides391",
    ends={
        Property(name="HwCommunication_HwMedia", type=MARTE_HwCommunication_HwBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwBridge", type=HwCommunication_HwMedia, multiplicity=Multiplicity(0, 9999))
    }
)
connectedTo392: BinaryAssociation = BinaryAssociation(
    name="connectedTo392",
    ends={
        Property(name="HwCommunication_HwMedia393", type=MARTE_HwCommunication_HwEndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwEndPoint", type=HwCommunication_HwMedia, multiplicity=Multiplicity(0, 9999))
    }
)
isSerial388: BinaryAssociation = BinaryAssociation(
    name="isSerial388",
    ends={
        Property(name="NFP_Boolean390", type=MARTE_HwCommunication_HwBus, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwBus389", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
protocols396: BinaryAssociation = BinaryAssociation(
    name="protocols396",
    ends={
        Property(name="HwProtocol_HwProtocol", type=MARTE_HwCommunication_HwConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwConnection", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999))
    }
)
managedMemories397: BinaryAssociation = BinaryAssociation(
    name="managedMemories397",
    ends={
        Property(name="HwMemory_HwMemory", type=MARTE_HwStorageManager_HwStorageManager, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwStorageManager", type=HwMemory_HwMemory, multiplicity=Multiplicity(0, 9999))
    }
)
pins394: BinaryAssociation = BinaryAssociation(
    name="pins394",
    ends={
        Property(name="HwIO_HwPin395", type=MARTE_HwCommunication_HwPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwCommunication_HwPort", type=HwIO_HwPin, multiplicity=Multiplicity(0, 9999))
    }
)
transferWidth400: BinaryAssociation = BinaryAssociation(
    name="transferWidth400",
    ends={
        Property(name="MARTE_HwStorageManager_HwDMA401", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="NFP_DataSize402", type=MARTE_HwStorageManager_HwDMA, multiplicity=Multiplicity(1, 1))
    }
)
drivenBy403: BinaryAssociation = BinaryAssociation(
    name="drivenBy403",
    ends={
        Property(name="HwComputing_HwProcessor405", type=MARTE_HwStorageManager_HwDMA, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwDMA404", type=HwComputing_HwProcessor, multiplicity=Multiplicity(0, 9999))
    }
)
virtualAddrSpace406: BinaryAssociation = BinaryAssociation(
    name="virtualAddrSpace406",
    ends={
        Property(name="NFP_DataSize407", type=MARTE_HwStorageManager_HwMMU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwMMU", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
physicalAddrSpace408: BinaryAssociation = BinaryAssociation(
    name="physicalAddrSpace408",
    ends={
        Property(name="NFP_DataSize410", type=MARTE_HwStorageManager_HwMMU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwMMU409", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbChannels398: BinaryAssociation = BinaryAssociation(
    name="nbChannels398",
    ends={
        Property(name="NFP_Natural399", type=MARTE_HwStorageManager_HwDMA, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwDMA", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbEntries414: BinaryAssociation = BinaryAssociation(
    name="nbEntries414",
    ends={
        Property(name="MARTE_HwStorageManager_HwMMU415", type=NFP_Natural, multiplicity=Multiplicity(0, 1)),
        Property(name="NFP_Natural416", type=MARTE_HwStorageManager_HwMMU, multiplicity=Multiplicity(1, 1))
    }
)
ownedTLBs417: BinaryAssociation = BinaryAssociation(
    name="ownedTLBs417",
    ends={
        Property(name="HwMemory_HwCache419", type=MARTE_HwStorageManager_HwMMU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwMMU418", type=HwMemory_HwCache, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memorySize420: BinaryAssociation = BinaryAssociation(
    name="memorySize420",
    ends={
        Property(name="NFP_DataSize421", type=MARTE_HwMemory_HwMemory, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwMemory", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
adressSize422: BinaryAssociation = BinaryAssociation(
    name="adressSize422",
    ends={
        Property(name="NFP_DataSize424", type=MARTE_HwMemory_HwMemory, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwMemory423", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memoryProtection411: BinaryAssociation = BinaryAssociation(
    name="memoryProtection411",
    ends={
        Property(name="NFP_Boolean413", type=MARTE_HwStorageManager_HwMMU, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwStorageManager_HwMMU412", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput427: BinaryAssociation = BinaryAssociation(
    name="throughput427",
    ends={
        Property(name="NFP_DataTxRate429", type=MARTE_HwMemory_HwMemory, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwMemory428", type=NFP_DataTxRate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
notation430: BinaryAssociation = BinaryAssociation(
    name="notation430",
    ends={
        Property(name="NFP_String431", type=MARTE_HwMemory_Timing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_Timing", type=NFP_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description432: BinaryAssociation = BinaryAssociation(
    name="description432",
    ends={
        Property(name="NFP_String434", type=MARTE_HwMemory_Timing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_Timing433", type=NFP_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value435: BinaryAssociation = BinaryAssociation(
    name="value435",
    ends={
        Property(name="NFP_Duration437", type=MARTE_HwMemory_Timing, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_Timing436", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timings425: BinaryAssociation = BinaryAssociation(
    name="timings425",
    ends={
        Property(name="HwMemory_Timing", type=MARTE_HwMemory_HwMemory, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwMemory426", type=HwMemory_Timing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nbSets438: BinaryAssociation = BinaryAssociation(
    name="nbSets438",
    ends={
        Property(name="NFP_Natural439", type=MARTE_HwMemory_CacheStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_CacheStructure", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blockSize440: BinaryAssociation = BinaryAssociation(
    name="blockSize440",
    ends={
        Property(name="NFP_DataSize442", type=MARTE_HwMemory_CacheStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_CacheStructure441", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
associativity443: BinaryAssociation = BinaryAssociation(
    name="associativity443",
    ends={
        Property(name="NFP_Natural445", type=MARTE_HwMemory_CacheStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_CacheStructure444", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbColumns448: BinaryAssociation = BinaryAssociation(
    name="nbColumns448",
    ends={
        Property(name="NFP_Natural450", type=MARTE_HwMemory_MemoryOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_MemoryOrganization449", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbBanks451: BinaryAssociation = BinaryAssociation(
    name="nbBanks451",
    ends={
        Property(name="NFP_Natural453", type=MARTE_HwMemory_MemoryOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_MemoryOrganization452", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wordSize454: BinaryAssociation = BinaryAssociation(
    name="wordSize454",
    ends={
        Property(name="NFP_DataSize456", type=MARTE_HwMemory_MemoryOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_MemoryOrganization455", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbRows446: BinaryAssociation = BinaryAssociation(
    name="nbRows446",
    ends={
        Property(name="NFP_Natural447", type=MARTE_HwMemory_MemoryOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_MemoryOrganization", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isStatic461: BinaryAssociation = BinaryAssociation(
    name="isStatic461",
    ends={
        Property(name="NFP_Boolean463", type=MARTE_HwMemory_HwRAM, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwRAM462", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isNonVolatile464: BinaryAssociation = BinaryAssociation(
    name="isNonVolatile464",
    ends={
        Property(name="NFP_Boolean466", type=MARTE_HwMemory_HwRAM, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwRAM465", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization467: BinaryAssociation = BinaryAssociation(
    name="organization467",
    ends={
        Property(name="HwMemory_MemoryOrganization468", type=MARTE_HwMemory_HwROM, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwROM", type=HwMemory_MemoryOrganization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization457: BinaryAssociation = BinaryAssociation(
    name="organization457",
    ends={
        Property(name="HwMemory_MemoryOrganization", type=MARTE_HwMemory_HwRAM, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwRAM", type=HwMemory_MemoryOrganization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isSynchronous458: BinaryAssociation = BinaryAssociation(
    name="isSynchronous458",
    ends={
        Property(name="NFP_Boolean460", type=MARTE_HwMemory_HwRAM, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwRAM459", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
level474: BinaryAssociation = BinaryAssociation(
    name="level474",
    ends={
        Property(name="NFP_Natural475", type=MARTE_HwMemory_HwCache, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwCache", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structure476: BinaryAssociation = BinaryAssociation(
    name="structure476",
    ends={
        Property(name="HwMemory_CacheStructure", type=MARTE_HwMemory_HwCache, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwCache477", type=HwMemory_CacheStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nbCounters478: BinaryAssociation = BinaryAssociation(
    name="nbCounters478",
    ends={
        Property(name="NFP_Natural479", type=MARTE_HwTiming_HwTimer, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwTiming_HwTimer", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sectorSize469: BinaryAssociation = BinaryAssociation(
    name="sectorSize469",
    ends={
        Property(name="NFP_DataSize470", type=MARTE_HwMemory_HwDrive, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwDrive", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buffer471: BinaryAssociation = BinaryAssociation(
    name="buffer471",
    ends={
        Property(name="HwMemory_HwRAM473", type=MARTE_HwMemory_HwDrive, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwMemory_HwDrive472", type=HwMemory_HwRAM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions485: BinaryAssociation = BinaryAssociation(
    name="functions485",
    ends={
        Property(name="HwDeviceFunction_HwDeviceFunction", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice", type=HwDeviceFunction_HwDeviceFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compliant486: BinaryAssociation = BinaryAssociation(
    name="compliant486",
    ends={
        Property(name="HwProtocol_HwProtocol488", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice487", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999))
    }
)
packages489: BinaryAssociation = BinaryAssociation(
    name="packages489",
    ends={
        Property(name="HwPackage_HwPackage491", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice490", type=HwPackage_HwPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pins492: BinaryAssociation = BinaryAssociation(
    name="pins492",
    ends={
        Property(name="HwIO_HwPin494", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice493", type=HwIO_HwPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
registers495: BinaryAssociation = BinaryAssociation(
    name="registers495",
    ends={
        Property(name="HwRegister_HwRegister497", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice496", type=HwRegister_HwRegister, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports498: BinaryAssociation = BinaryAssociation(
    name="ports498",
    ends={
        Property(name="HwCommunication_HwPort500", type=MARTE_HwDevice_HwDevice, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwDevice499", type=HwCommunication_HwPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
counterWidth480: BinaryAssociation = BinaryAssociation(
    name="counterWidth480",
    ends={
        Property(name="NFP_DataSize482", type=MARTE_HwTiming_HwTimer, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwTiming_HwTimer481", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputClock483: BinaryAssociation = BinaryAssociation(
    name="inputClock483",
    ends={
        Property(name="HwTiming_HwClock", type=MARTE_HwTiming_HwTimer, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwTiming_HwTimer484", type=HwTiming_HwClock, multiplicity=Multiplicity(0, 1))
    }
)
implements501: BinaryAssociation = BinaryAssociation(
    name="implements501",
    ends={
        Property(name="HwProtocol_HwProtocol502", type=MARTE_HwDevice_HwPeripheral, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwPeripheral", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999))
    }
)
operationimpls503: BinaryAssociation = BinaryAssociation(
    name="operationimpls503",
    ends={
        Property(name="HwPeripheral_OperationImpl", type=MARTE_HwDevice_HwPeripheral, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwPeripheral504", type=HwPeripheral_OperationImpl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refsfr505: BinaryAssociation = BinaryAssociation(
    name="refsfr505",
    ends={
        Property(name="HwRegister_HwRegister507", type=MARTE_HwDevice_HwPeripheral, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwPeripheral506", type=HwRegister_HwRegister, multiplicity=Multiplicity(0, 9999))
    }
)
refports508: BinaryAssociation = BinaryAssociation(
    name="refports508",
    ends={
        Property(name="HwCommunication_HwPort510", type=MARTE_HwDevice_HwPeripheral, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwPeripheral509", type=HwCommunication_HwPort, multiplicity=Multiplicity(0, 9999))
    }
)
peripheralActivities511: BinaryAssociation = BinaryAssociation(
    name="peripheralActivities511",
    ends={
        Property(name="HwPeripheral_PeripheralActivity", type=MARTE_HwDevice_HwPeripheral, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDevice_HwPeripheral512", type=HwPeripheral_PeripheralActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consumption513: BinaryAssociation = BinaryAssociation(
    name="consumption513",
    ends={
        Property(name="NFP_Power514", type=MARTE_HwGeneral_HwResourceService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResourceService", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
p_HW_Services520: BinaryAssociation = BinaryAssociation(
    name="p_HW_Services520",
    ends={
        Property(name="HwGeneral_HwResourceService", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource521", type=HwGeneral_HwResourceService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
r_HW_Services522: BinaryAssociation = BinaryAssociation(
    name="r_HW_Services522",
    ends={
        Property(name="HwGeneral_HwResourceService524", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource523", type=HwGeneral_HwResourceService, multiplicity=Multiplicity(0, 9999))
    }
)
ownedHW525: BinaryAssociation = BinaryAssociation(
    name="ownedHW525",
    ends={
        Property(name="HwGeneral_HwResource", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource526", type=HwGeneral_HwResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endPoints527: BinaryAssociation = BinaryAssociation(
    name="endPoints527",
    ends={
        Property(name="HwCommunication_HwEndPoint", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource528", type=HwCommunication_HwEndPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
frequency529: BinaryAssociation = BinaryAssociation(
    name="frequency529",
    ends={
        Property(name="NFP_Frequency", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource530", type=NFP_Frequency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operations531: BinaryAssociation = BinaryAssociation(
    name="operations531",
    ends={
        Property(name="HwGeneral_MARTE_Operation", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource532", type=HwGeneral_MARTE_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dissipation515: BinaryAssociation = BinaryAssociation(
    name="dissipation515",
    ends={
        Property(name="NFP_Power517", type=MARTE_HwGeneral_HwResourceService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResourceService516", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description518: BinaryAssociation = BinaryAssociation(
    name="description518",
    ends={
        Property(name="NFP_String519", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource", type=NFP_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimensions535: BinaryAssociation = BinaryAssociation(
    name="dimensions535",
    ends={
        Property(name="NFP_Length", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent", type=NFP_Length, multiplicity=Multiplicity(0, 3), is_composite=True)
    }
)
area536: BinaryAssociation = BinaryAssociation(
    name="area536",
    ends={
        Property(name="NFP_Area", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent537", type=NFP_Area, multiplicity=Multiplicity(0, 1))
    }
)
position538: BinaryAssociation = BinaryAssociation(
    name="position538",
    ends={
        Property(name="NFP_NaturalInterval", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent539", type=NFP_NaturalInterval, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
grid540: BinaryAssociation = BinaryAssociation(
    name="grid540",
    ends={
        Property(name="NFP_Natural542", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent541", type=NFP_Natural, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
nbPins543: BinaryAssociation = BinaryAssociation(
    name="nbPins543",
    ends={
        Property(name="NFP_Natural545", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent544", type=NFP_Natural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
weight546: BinaryAssociation = BinaryAssociation(
    name="weight546",
    ends={
        Property(name="NFP_Real548", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent547", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activities533: BinaryAssociation = BinaryAssociation(
    name="activities533",
    ends={
        Property(name="HwGeneral_MARTE_Activity", type=MARTE_HwGeneral_HwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwGeneral_HwResource534", type=HwGeneral_MARTE_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
poweredServices553: BinaryAssociation = BinaryAssociation(
    name="poweredServices553",
    ends={
        Property(name="HwGeneral_HwResourceService555", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent554", type=HwGeneral_HwResourceService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticConsumption556: BinaryAssociation = BinaryAssociation(
    name="staticConsumption556",
    ends={
        Property(name="NFP_Power558", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent557", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
staticDissipation559: BinaryAssociation = BinaryAssociation(
    name="staticDissipation559",
    ends={
        Property(name="NFP_Power561", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent560", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subComponents562: BinaryAssociation = BinaryAssociation(
    name="subComponents562",
    ends={
        Property(name="HwLayout_HwComponent", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent563", type=HwLayout_HwComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
price549: BinaryAssociation = BinaryAssociation(
    name="price549",
    ends={
        Property(name="NFP_Price", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent550", type=NFP_Price, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
r_Conditions551: BinaryAssociation = BinaryAssociation(
    name="r_Conditions551",
    ends={
        Property(name="HwLayout_Env_Condition", type=MARTE_HwLayout_HwComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_HwComponent552", type=HwLayout_Env_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
range566: BinaryAssociation = BinaryAssociation(
    name="range566",
    ends={
        Property(name="Realnterval", type=MARTE_HwLayout_Env_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_Env_Condition567", type=Realnterval, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suppliedPower568: BinaryAssociation = BinaryAssociation(
    name="suppliedPower568",
    ends={
        Property(name="NFP_Power569", type=MARTE_HwPower_HwPowerSupply, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPower_HwPowerSupply", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity570: BinaryAssociation = BinaryAssociation(
    name="capacity570",
    ends={
        Property(name="NFP_Energy572", type=MARTE_HwPower_HwPowerSupply, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPower_HwPowerSupply571", type=NFP_Energy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description564: BinaryAssociation = BinaryAssociation(
    name="description564",
    ends={
        Property(name="NFP_String565", type=MARTE_HwLayout_Env_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwLayout_Env_Condition", type=NFP_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
override575: BinaryAssociation = BinaryAssociation(
    name="override575",
    ends={
        Property(name="HwPeripheral_MARTE_Operation", type=MARTE_HwPeripheral_OperationImpl, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPeripheral_OperationImpl", type=HwPeripheral_MARTE_Operation, multiplicity=Multiplicity(0, 1))
    }
)
register576: BinaryAssociation = BinaryAssociation(
    name="register576",
    ends={
        Property(name="HwRegister_HwRegister577", type=MARTE_HwPeripheral_RegisterAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPeripheral_RegisterAction", type=HwRegister_HwRegister, multiplicity=Multiplicity(0, 1))
    }
)
value578: BinaryAssociation = BinaryAssociation(
    name="value578",
    ends={
        Property(name="HwPeripheral_MARTE_InputPin", type=MARTE_HwPeripheral_WriteRegisterAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPeripheral_WriteRegisterAction", type=HwPeripheral_MARTE_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result579: BinaryAssociation = BinaryAssociation(
    name="result579",
    ends={
        Property(name="HwPeripheral_MARTE_OutputPin", type=MARTE_HwPeripheral_ReadRegisterAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPeripheral_ReadRegisterAction", type=HwPeripheral_MARTE_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
registerActions580: BinaryAssociation = BinaryAssociation(
    name="registerActions580",
    ends={
        Property(name="HwPeripheral_RegisterAction", type=MARTE_HwPeripheral_PeripheralActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPeripheral_PeripheralActivity", type=HwPeripheral_RegisterAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coolingPower573: BinaryAssociation = BinaryAssociation(
    name="coolingPower573",
    ends={
        Property(name="NFP_Power574", type=MARTE_HwPower_HwCoolingSupply, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPower_HwCoolingSupply", type=NFP_Power, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pkgPin581: BinaryAssociation = BinaryAssociation(
    name="pkgPin581",
    ends={
        Property(name="HRM582", type=HwPackage_HwPackagePin, multiplicity=Multiplicity(0, 1)),
        Property(name="MARTE_DesignModel583", type=MARTE_HwIO_HwPin, multiplicity=Multiplicity(1, 1))
    }
)
lines584: BinaryAssociation = BinaryAssociation(
    name="lines584",
    ends={
        Property(name="HwIO_HwLine", type=MARTE_HwIO_HwPin, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwIO_HwPin", type=HwIO_HwLine, multiplicity=Multiplicity(0, 9999))
    }
)
components585: BinaryAssociation = BinaryAssociation(
    name="components585",
    ends={
        Property(name="HwGeneral_HwResource586", type=MARTE_HwDatasheet_HwDatasheet, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDatasheet_HwDatasheet", type=HwGeneral_HwResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocols587: BinaryAssociation = BinaryAssociation(
    name="protocols587",
    ends={
        Property(name="HwProtocol_HwProtocol589", type=MARTE_HwDatasheet_HwDatasheet, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDatasheet_HwDatasheet588", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refpin591: BinaryAssociation = BinaryAssociation(
    name="refpin591",
    ends={
        Property(name="MARTE_DesignModel593", type=MARTE_HwPackage_HwPackagePin, multiplicity=Multiplicity(1, 1)),
        Property(name="HRM592", type=HwIO_HwPin, multiplicity=Multiplicity(0, 9999))
    }
)
wire594: BinaryAssociation = BinaryAssociation(
    name="wire594",
    ends={
        Property(name="HwPackage_HwWire", type=MARTE_HwPackage_HwPackagePin, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPackage_HwPackagePin", type=HwPackage_HwWire, multiplicity=Multiplicity(0, 9999))
    }
)
operations595: BinaryAssociation = BinaryAssociation(
    name="operations595",
    ends={
        Property(name="HwProtocol_MARTE_Operation", type=MARTE_HwProtocol_HwProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwProtocol_HwProtocol", type=HwProtocol_MARTE_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pins590: BinaryAssociation = BinaryAssociation(
    name="pins590",
    ends={
        Property(name="HwPackage_HwPackagePin", type=MARTE_HwPackage_HwPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwPackage_HwPackage", type=HwPackage_HwPackagePin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components600: BinaryAssociation = BinaryAssociation(
    name="components600",
    ends={
        Property(name="HwGeneral_HwResource602", type=MARTE_HwDiagram_HwBlockDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwBlockDiagram601", type=HwGeneral_HwResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components603: BinaryAssociation = BinaryAssociation(
    name="components603",
    ends={
        Property(name="HwPackage_HwPackage604", type=MARTE_HwDiagram_HwCircuitDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwCircuitDiagram", type=HwPackage_HwPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wires605: BinaryAssociation = BinaryAssociation(
    name="wires605",
    ends={
        Property(name="HwPackage_HwWire607", type=MARTE_HwDiagram_HwCircuitDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwCircuitDiagram606", type=HwPackage_HwWire, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components608: BinaryAssociation = BinaryAssociation(
    name="components608",
    ends={
        Property(name="HwGeneral_HwResource609", type=MARTE_HwDiagram_HwHRMDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwHRMDiagram", type=HwGeneral_HwResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections610: BinaryAssociation = BinaryAssociation(
    name="connections610",
    ends={
        Property(name="HwCommunication_HwMedia612", type=MARTE_HwDiagram_HwHRMDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwHRMDiagram611", type=HwCommunication_HwMedia, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocols596: BinaryAssociation = BinaryAssociation(
    name="protocols596",
    ends={
        Property(name="HwProtocol_HwProtocol597", type=MARTE_HwDiagram_HwBlockDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwBlockDiagram", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections598: BinaryAssociation = BinaryAssociation(
    name="connections598",
    ends={
        Property(name="HwCommunication_HwConnection", type=MARTE_HwDiagram_HwBlockDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwBlockDiagram599", type=HwCommunication_HwConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypes616: BinaryAssociation = BinaryAssociation(
    name="datatypes616",
    ends={
        Property(name="MARTE_HwDiagram_HwHRMDiagram617", type=HwDiagram_MARTE_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="HwDiagram_MARTE_DataType", type=MARTE_HwDiagram_HwHRMDiagram, multiplicity=Multiplicity(1, 1))
    }
)
devices618: BinaryAssociation = BinaryAssociation(
    name="devices618",
    ends={
        Property(name="SW_Brokering_DeviceBroker", type=MARTE_HwDiagram_SRMDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_SRMDiagram", type=SW_Brokering_DeviceBroker, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hwcomponents619: BinaryAssociation = BinaryAssociation(
    name="hwcomponents619",
    ends={
        Property(name="HwGeneral_HwResource621", type=MARTE_HwDiagram_SRMDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_SRMDiagram620", type=HwGeneral_HwResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifierElements622: BinaryAssociation = BinaryAssociation(
    name="identifierElements622",
    ends={
        Property(name="SW_ResourceCore_MARTE_TypedElement", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource", type=SW_ResourceCore_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
stateElements623: BinaryAssociation = BinaryAssociation(
    name="stateElements623",
    ends={
        Property(name="SW_ResourceCore_MARTE_TypedElement625", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource624", type=SW_ResourceCore_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
memorySizeFootprint626: BinaryAssociation = BinaryAssociation(
    name="memorySizeFootprint626",
    ends={
        Property(name="SW_ResourceCore_MARTE_TypedElement628", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource627", type=SW_ResourceCore_MARTE_TypedElement, multiplicity=Multiplicity(0, 1))
    }
)
protocols613: BinaryAssociation = BinaryAssociation(
    name="protocols613",
    ends={
        Property(name="HwProtocol_HwProtocol615", type=MARTE_HwDiagram_HwHRMDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_HwDiagram_HwHRMDiagram614", type=HwProtocol_HwProtocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deleteServices631: BinaryAssociation = BinaryAssociation(
    name="deleteServices631",
    ends={
        Property(name="SW_ResourceCore_MARTE_BehavioralFeature633", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource632", type=SW_ResourceCore_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
initializeServices634: BinaryAssociation = BinaryAssociation(
    name="initializeServices634",
    ends={
        Property(name="SW_ResourceCore_MARTE_BehavioralFeature636", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource635", type=SW_ResourceCore_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
accessedElement637: BinaryAssociation = BinaryAssociation(
    name="accessedElement637",
    ends={
        Property(name="SW_ResourceCore_MARTE_Property", type=MARTE_SW_ResourceCore_SwAccessService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwAccessService", type=SW_ResourceCore_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
createServices629: BinaryAssociation = BinaryAssociation(
    name="createServices629",
    ends={
        Property(name="SW_ResourceCore_MARTE_BehavioralFeature", type=MARTE_SW_ResourceCore_SwResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_ResourceCore_SwResource630", type=SW_ResourceCore_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
type639: BinaryAssociation = BinaryAssociation(
    name="type639",
    ends={
        Property(name="ArrivalPattern640", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource", type=ArrivalPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryPoints641: BinaryAssociation = BinaryAssociation(
    name="entryPoints641",
    ends={
        Property(name="SW_Concurrency_MARTE_Element", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource642", type=SW_Concurrency_MARTE_Element, multiplicity=Multiplicity(0, 9999))
    }
)
adressSpace643: BinaryAssociation = BinaryAssociation(
    name="adressSpace643",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource644", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
periodElements645: BinaryAssociation = BinaryAssociation(
    name="periodElements645",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement647", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource646", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
priorityElements648: BinaryAssociation = BinaryAssociation(
    name="priorityElements648",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement650", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource649", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
stackSizeElements651: BinaryAssociation = BinaryAssociation(
    name="stackSizeElements651",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement653", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource652", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
routine638: BinaryAssociation = BinaryAssociation(
    name="routine638",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature", type=MARTE_SW_Concurrency_EntryPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_EntryPoint", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
enableConcurrencyServices657: BinaryAssociation = BinaryAssociation(
    name="enableConcurrencyServices657",
    ends={
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource658", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999)),
        Property(name="SW_Concurrency_MARTE_BehavioralFeature659", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1))
    }
)
resumeServices660: BinaryAssociation = BinaryAssociation(
    name="resumeServices660",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature662", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource661", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
suspendServices663: BinaryAssociation = BinaryAssociation(
    name="suspendServices663",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature665", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource664", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
terminateServices666: BinaryAssociation = BinaryAssociation(
    name="terminateServices666",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature668", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource667", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
disableConcurrencyServices669: BinaryAssociation = BinaryAssociation(
    name="disableConcurrencyServices669",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature671", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource670", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
shareDataResources672: BinaryAssociation = BinaryAssociation(
    name="shareDataResources672",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement674", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource673", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
messageResources675: BinaryAssociation = BinaryAssociation(
    name="messageResources675",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement677", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource676", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
mutualExclusionResources678: BinaryAssociation = BinaryAssociation(
    name="mutualExclusionResources678",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement680", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource679", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
activateServices654: BinaryAssociation = BinaryAssociation(
    name="activateServices654",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature656", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource655", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
heapSizeElements684: BinaryAssociation = BinaryAssociation(
    name="heapSizeElements684",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement686", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource685", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
vectorElements687: BinaryAssociation = BinaryAssociation(
    name="vectorElements687",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement688", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
maskElements689: BinaryAssociation = BinaryAssociation(
    name="maskElements689",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement691", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource690", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
routineConnectServices692: BinaryAssociation = BinaryAssociation(
    name="routineConnectServices692",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature694", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource693", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
routineDisconnectServices695: BinaryAssociation = BinaryAssociation(
    name="routineDisconnectServices695",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature697", type=MARTE_SW_Concurrency_InterruptResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_InterruptResource696", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
notificationResources681: BinaryAssociation = BinaryAssociation(
    name="notificationResources681",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement683", type=MARTE_SW_Concurrency_SwConcurrentResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwConcurrentResource682", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
schedulers698: BinaryAssociation = BinaryAssociation(
    name="schedulers698",
    ends={
        Property(name="SW_Concurrency_MARTE_NamedElement", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource", type=SW_Concurrency_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
deadlineElements699: BinaryAssociation = BinaryAssociation(
    name="deadlineElements699",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement701", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource700", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
deadlineTypeElements702: BinaryAssociation = BinaryAssociation(
    name="deadlineTypeElements702",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement704", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource703", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
timeSliceElements705: BinaryAssociation = BinaryAssociation(
    name="timeSliceElements705",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement707", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource706", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
delayServices708: BinaryAssociation = BinaryAssociation(
    name="delayServices708",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature710", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource709", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
joinServices711: BinaryAssociation = BinaryAssociation(
    name="joinServices711",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature713", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource712", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
yieldServices714: BinaryAssociation = BinaryAssociation(
    name="yieldServices714",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature716", type=MARTE_SW_Concurrency_SwSchedulableResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwSchedulableResource715", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
concurrentResources719: BinaryAssociation = BinaryAssociation(
    name="concurrentResources719",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement720", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
memorySpaces721: BinaryAssociation = BinaryAssociation(
    name="memorySpaces721",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement723", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition722", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
fork724: BinaryAssociation = BinaryAssociation(
    name="fork724",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature726", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition725", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
exit727: BinaryAssociation = BinaryAssociation(
    name="exit727",
    ends={
        Property(name="SW_Concurrency_MARTE_BehavioralFeature729", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition728", type=SW_Concurrency_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
base_Namespace730: BinaryAssociation = BinaryAssociation(
    name="base_Namespace730",
    ends={
        Property(name="SW_Concurrency_MARTE_Namespace", type=MARTE_SW_Concurrency_MemoryPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_MemoryPartition731", type=SW_Concurrency_MARTE_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
durationElements717: BinaryAssociation = BinaryAssociation(
    name="durationElements717",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement718", type=MARTE_SW_Concurrency_SwTimerResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_SwTimerResource", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 1))
    }
)
devices734: BinaryAssociation = BinaryAssociation(
    name="devices734",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
closeServices735: BinaryAssociation = BinaryAssociation(
    name="closeServices735",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker736", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
controlServices737: BinaryAssociation = BinaryAssociation(
    name="controlServices737",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature739", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker738", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
openServices740: BinaryAssociation = BinaryAssociation(
    name="openServices740",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature742", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker741", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
timers732: BinaryAssociation = BinaryAssociation(
    name="timers732",
    ends={
        Property(name="SW_Concurrency_MARTE_TypedElement733", type=MARTE_SW_Concurrency_Alarm, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Concurrency_Alarm", type=SW_Concurrency_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
writeServices746: BinaryAssociation = BinaryAssociation(
    name="writeServices746",
    ends={
        Property(name="MARTE_SW_Brokering_DeviceBroker747", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999)),
        Property(name="SW_Brokering_MARTE_BehavioralFeature748", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1))
    }
)
operations749: BinaryAssociation = BinaryAssociation(
    name="operations749",
    ends={
        Property(name="SW_Brokering_MARTE_Operation", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker750", type=SW_Brokering_MARTE_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities751: BinaryAssociation = BinaryAssociation(
    name="activities751",
    ends={
        Property(name="SW_Brokering_MARTE_Activity", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker752", type=SW_Brokering_MARTE_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memories753: BinaryAssociation = BinaryAssociation(
    name="memories753",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement754", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
memoryBlockAdressElements755: BinaryAssociation = BinaryAssociation(
    name="memoryBlockAdressElements755",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement757", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker756", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
memoryBlockSizeElements758: BinaryAssociation = BinaryAssociation(
    name="memoryBlockSizeElements758",
    ends={
        Property(name="SW_Brokering_MARTE_TypedElement760", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker759", type=SW_Brokering_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
readServices743: BinaryAssociation = BinaryAssociation(
    name="readServices743",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature745", type=MARTE_SW_Brokering_DeviceBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_DeviceBroker744", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
mapServices767: BinaryAssociation = BinaryAssociation(
    name="mapServices767",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature769", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker768", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
unMapServices770: BinaryAssociation = BinaryAssociation(
    name="unMapServices770",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature772", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker771", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
lockServices761: BinaryAssociation = BinaryAssociation(
    name="lockServices761",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature763", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker762", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
unlockServices764: BinaryAssociation = BinaryAssociation(
    name="unlockServices764",
    ends={
        Property(name="SW_Brokering_MARTE_BehavioralFeature766", type=MARTE_SW_Brokering_MemoryBroker, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Brokering_MemoryBroker765", type=SW_Brokering_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
waitingPolicyElements773: BinaryAssociation = BinaryAssociation(
    name="waitingPolicyElements773",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement", type=MARTE_SW_Interaction_SwInteractionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwInteractionResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
writeServices775: BinaryAssociation = BinaryAssociation(
    name="writeServices775",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature777", type=MARTE_SW_Interaction_SharedDataComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SharedDataComResource776", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
messageSizeElements778: BinaryAssociation = BinaryAssociation(
    name="messageSizeElements778",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement779", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
messageQueueCapacityElements780: BinaryAssociation = BinaryAssociation(
    name="messageQueueCapacityElements780",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement782", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource781", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
sendServices783: BinaryAssociation = BinaryAssociation(
    name="sendServices783",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature785", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource784", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
receiveServices786: BinaryAssociation = BinaryAssociation(
    name="receiveServices786",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature788", type=MARTE_SW_Interaction_MessageComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_MessageComResource787", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
readServices774: BinaryAssociation = BinaryAssociation(
    name="readServices774",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature", type=MARTE_SW_Interaction_SharedDataComResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SharedDataComResource", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
occurenceCountElements789: BinaryAssociation = BinaryAssociation(
    name="occurenceCountElements789",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement790", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
maskElements791: BinaryAssociation = BinaryAssociation(
    name="maskElements791",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement793", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource792", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
flushServices794: BinaryAssociation = BinaryAssociation(
    name="flushServices794",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature796", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource795", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
signalServices797: BinaryAssociation = BinaryAssociation(
    name="signalServices797",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature799", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource798", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
waitServices800: BinaryAssociation = BinaryAssociation(
    name="waitServices800",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature802", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource801", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
clearServices803: BinaryAssociation = BinaryAssociation(
    name="clearServices803",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature805", type=MARTE_SW_Interaction_NotificationResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_NotificationResource804", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
accessTokenElements806: BinaryAssociation = BinaryAssociation(
    name="accessTokenElements806",
    ends={
        Property(name="SW_Interaction_MARTE_TypedElement807", type=MARTE_SW_Interaction_SwMutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwMutualExclusionResource", type=SW_Interaction_MARTE_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
releaseServices808: BinaryAssociation = BinaryAssociation(
    name="releaseServices808",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature810", type=MARTE_SW_Interaction_SwMutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwMutualExclusionResource809", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
acquireServices811: BinaryAssociation = BinaryAssociation(
    name="acquireServices811",
    ends={
        Property(name="SW_Interaction_MARTE_BehavioralFeature813", type=MARTE_SW_Interaction_SwMutualExclusionResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SW_Interaction_SwMutualExclusionResource812", type=SW_Interaction_MARTE_BehavioralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
base_Property814: BinaryAssociation = BinaryAssociation(
    name="base_Property814",
    ends={
        Property(name="GCM_MARTE_Property", type=MARTE_GCM_FlowProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_FlowProperty", type=GCM_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_Port815: BinaryAssociation = BinaryAssociation(
    name="base_Port815",
    ends={
        Property(name="GCM_MARTE_Port", type=MARTE_GCM_FlowPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_FlowPort", type=GCM_MARTE_Port, multiplicity=Multiplicity(1, 1))
    }
)
base_Port816: BinaryAssociation = BinaryAssociation(
    name="base_Port816",
    ends={
        Property(name="GCM_MARTE_Port817", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort", type=GCM_MARTE_Port, multiplicity=Multiplicity(1, 1))
    }
)
provInterface818: BinaryAssociation = BinaryAssociation(
    name="provInterface818",
    ends={
        Property(name="GCM_MARTE_Interface", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort819", type=GCM_MARTE_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
reqInterface820: BinaryAssociation = BinaryAssociation(
    name="reqInterface820",
    ends={
        Property(name="GCM_MARTE_Interface822", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort821", type=GCM_MARTE_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
featuresSpec823: BinaryAssociation = BinaryAssociation(
    name="featuresSpec823",
    ends={
        Property(name="GCM_ClientServerSpecification", type=MARTE_GCM_ClientServerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerPort824", type=GCM_ClientServerSpecification, multiplicity=Multiplicity(0, 1))
    }
)
base_Interface825: BinaryAssociation = BinaryAssociation(
    name="base_Interface825",
    ends={
        Property(name="GCM_MARTE_Interface826", type=MARTE_GCM_ClientServerSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerSpecification", type=GCM_MARTE_Interface, multiplicity=Multiplicity(1, 1))
    }
)
base_Interface827: BinaryAssociation = BinaryAssociation(
    name="base_Interface827",
    ends={
        Property(name="GCM_MARTE_Interface828", type=MARTE_GCM_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_FlowSpecification", type=GCM_MARTE_Interface, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature829: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature829",
    ends={
        Property(name="GCM_MARTE_BehavioralFeature", type=MARTE_GCM_ClientServerFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_ClientServerFeature", type=GCM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Trigger830: BinaryAssociation = BinaryAssociation(
    name="base_Trigger830",
    ends={
        Property(name="GCM_MARTE_Trigger", type=MARTE_GCM_GCMTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMTrigger", type=GCM_MARTE_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
base_InvocationAction833: BinaryAssociation = BinaryAssociation(
    name="base_InvocationAction833",
    ends={
        Property(name="GCM_MARTE_InvocationAction", type=MARTE_GCM_GCMInvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMInvocationAction", type=GCM_MARTE_InvocationAction, multiplicity=Multiplicity(1, 1))
    }
)
onFeature834: BinaryAssociation = BinaryAssociation(
    name="onFeature834",
    ends={
        Property(name="GCM_MARTE_Feature836", type=MARTE_GCM_GCMInvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMInvocationAction835", type=GCM_MARTE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
base_AnyReceiveEvent837: BinaryAssociation = BinaryAssociation(
    name="base_AnyReceiveEvent837",
    ends={
        Property(name="GCM_MARTE_AnyReceiveEvent", type=MARTE_GCM_DataEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataEvent", type=GCM_MARTE_AnyReceiveEvent, multiplicity=Multiplicity(1, 1))
    }
)
classifier838: BinaryAssociation = BinaryAssociation(
    name="classifier838",
    ends={
        Property(name="GCM_MARTE_Classifier", type=MARTE_GCM_DataEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataEvent839", type=GCM_MARTE_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Property840: BinaryAssociation = BinaryAssociation(
    name="base_Property840",
    ends={
        Property(name="GCM_MARTE_Property841", type=MARTE_GCM_DataPool, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataPool", type=GCM_MARTE_Property, multiplicity=Multiplicity(1, 1))
    }
)
insertion842: BinaryAssociation = BinaryAssociation(
    name="insertion842",
    ends={
        Property(name="GCM_MARTE_Behavior", type=MARTE_GCM_DataPool, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataPool843", type=GCM_MARTE_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
feature831: BinaryAssociation = BinaryAssociation(
    name="feature831",
    ends={
        Property(name="GCM_MARTE_Feature", type=MARTE_GCM_GCMTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_GCMTrigger832", type=GCM_MARTE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
pop847: BinaryAssociation = BinaryAssociation(
    name="pop847",
    ends={
        Property(name="NFP_Integer848", type=MARTE_GQAM_GaWorkloadGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadGenerator", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_Behavior849: BinaryAssociation = BinaryAssociation(
    name="base_Behavior849",
    ends={
        Property(name="GQAM_MARTE_Behavior", type=MARTE_GQAM_GaWorkloadGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadGenerator850", type=GQAM_MARTE_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
generator854: BinaryAssociation = BinaryAssociation(
    name="generator854",
    ends={
        Property(name="GQAM_GaWorkloadGenerator", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent855", type=GQAM_GaWorkloadGenerator, multiplicity=Multiplicity(0, 1))
    }
)
trace856: BinaryAssociation = BinaryAssociation(
    name="trace856",
    ends={
        Property(name="GQAM_GaEventTrace", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent857", type=GQAM_GaEventTrace, multiplicity=Multiplicity(0, 1))
    }
)
effect858: BinaryAssociation = BinaryAssociation(
    name="effect858",
    ends={
        Property(name="GQAM_GaScenario", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent859", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 1))
    }
)
selection844: BinaryAssociation = BinaryAssociation(
    name="selection844",
    ends={
        Property(name="GCM_MARTE_Behavior846", type=MARTE_GCM_DataPool, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GCM_DataPool845", type=GCM_MARTE_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
timedEvent860: BinaryAssociation = BinaryAssociation(
    name="timedEvent860",
    ends={
        Property(name="GQAM_MARTE_TimeEvent", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent861", type=GQAM_MARTE_TimeEvent, multiplicity=Multiplicity(0, 1))
    }
)
base_NamedElement862: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement862",
    ends={
        Property(name="GQAM_MARTE_NamedElement864", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent863", type=GQAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
base_NamedElement851: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement851",
    ends={
        Property(name="GQAM_MARTE_NamedElement", type=MARTE_GQAM_GaEventTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaEventTrace", type=GQAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
pattern852: BinaryAssociation = BinaryAssociation(
    name="pattern852",
    ends={
        Property(name="ArrivalPattern853", type=MARTE_GQAM_GaWorkloadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadEvent", type=ArrivalPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interOccT872: BinaryAssociation = BinaryAssociation(
    name="interOccT872",
    ends={
        Property(name="NFP_Duration874", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario873", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
throughput875: BinaryAssociation = BinaryAssociation(
    name="throughput875",
    ends={
        Property(name="NFP_Frequency877", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario876", type=NFP_Frequency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
respT878: BinaryAssociation = BinaryAssociation(
    name="respT878",
    ends={
        Property(name="NFP_Duration880", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario879", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilization881: BinaryAssociation = BinaryAssociation(
    name="utilization881",
    ends={
        Property(name="NFP_Real883", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario882", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cause865: BinaryAssociation = BinaryAssociation(
    name="cause865",
    ends={
        Property(name="GQAM_GaWorkloadEvent", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario", type=GQAM_GaWorkloadEvent, multiplicity=Multiplicity(0, 1))
    }
)
hostDemand866: BinaryAssociation = BinaryAssociation(
    name="hostDemand866",
    ends={
        Property(name="NFP_Duration868", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario867", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hostDemandOps869: BinaryAssociation = BinaryAssociation(
    name="hostDemandOps869",
    ends={
        Property(name="NFP_Real871", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario870", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isAtomic891: BinaryAssociation = BinaryAssociation(
    name="isAtomic891",
    ends={
        Property(name="NFP_Boolean892", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blockT893: BinaryAssociation = BinaryAssociation(
    name="blockT893",
    ends={
        Property(name="NFP_Duration895", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep894", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rep896: BinaryAssociation = BinaryAssociation(
    name="rep896",
    ends={
        Property(name="NFP_Real898", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep897", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prob899: BinaryAssociation = BinaryAssociation(
    name="prob899",
    ends={
        Property(name="NFP_Real901", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep900", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
priority902: BinaryAssociation = BinaryAssociation(
    name="priority902",
    ends={
        Property(name="NFP_Integer904", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep903", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
utilizationOnHost884: BinaryAssociation = BinaryAssociation(
    name="utilizationOnHost884",
    ends={
        Property(name="NFP_Real886", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario885", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root887: BinaryAssociation = BinaryAssociation(
    name="root887",
    ends={
        Property(name="GQAM_GaStep", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario888", type=GQAM_GaStep, multiplicity=Multiplicity(0, 1))
    }
)
timing889: BinaryAssociation = BinaryAssociation(
    name="timing889",
    ends={
        Property(name="GQAM_GaTimedObs", type=MARTE_GQAM_GaScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaScenario890", type=GQAM_GaTimedObs, multiplicity=Multiplicity(0, 9999))
    }
)
behavior914: BinaryAssociation = BinaryAssociation(
    name="behavior914",
    ends={
        Property(name="GQAM_GaScenario916", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep915", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 1))
    }
)
selfDelay917: BinaryAssociation = BinaryAssociation(
    name="selfDelay917",
    ends={
        Property(name="NFP_Duration919", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep918", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commTxOvh920: BinaryAssociation = BinaryAssociation(
    name="commTxOvh920",
    ends={
        Property(name="NFP_Duration921", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concurRes905: BinaryAssociation = BinaryAssociation(
    name="concurRes905",
    ends={
        Property(name="GRM_SchedulableResource", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep906", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 1))
    }
)
host907: BinaryAssociation = BinaryAssociation(
    name="host907",
    ends={
        Property(name="GQAM_GaExecHost", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep908", type=GQAM_GaExecHost, multiplicity=Multiplicity(0, 1))
    }
)
servDemand909: BinaryAssociation = BinaryAssociation(
    name="servDemand909",
    ends={
        Property(name="GQAM_GaRequestedService", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep910", type=GQAM_GaRequestedService, multiplicity=Multiplicity(0, 9999))
    }
)
servCount911: BinaryAssociation = BinaryAssociation(
    name="servCount911",
    ends={
        Property(name="NFP_Real913", type=MARTE_GQAM_GaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaStep912", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memSize933: BinaryAssociation = BinaryAssociation(
    name="memSize933",
    ends={
        Property(name="NFP_DataSize935", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost934", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
utilization936: BinaryAssociation = BinaryAssociation(
    name="utilization936",
    ends={
        Property(name="NFP_Real938", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost937", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
throughput939: BinaryAssociation = BinaryAssociation(
    name="throughput939",
    ends={
        Property(name="NFP_Frequency941", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost940", type=NFP_Frequency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commRcvOvh922: BinaryAssociation = BinaryAssociation(
    name="commRcvOvh922",
    ends={
        Property(name="NFP_Duration924", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost923", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cntxtSwT925: BinaryAssociation = BinaryAssociation(
    name="cntxtSwT925",
    ends={
        Property(name="NFP_Duration927", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost926", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clockOvh928: BinaryAssociation = BinaryAssociation(
    name="clockOvh928",
    ends={
        Property(name="NFP_Duration930", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost929", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schedPriRange931: BinaryAssociation = BinaryAssociation(
    name="schedPriRange931",
    ends={
        Property(name="IntegerInterval", type=MARTE_GQAM_GaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaExecHost932", type=IntegerInterval, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
acqRes947: BinaryAssociation = BinaryAssociation(
    name="acqRes947",
    ends={
        Property(name="GRM_Resource948", type=MARTE_GQAM_GaAcqStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAcqStep", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resUnits949: BinaryAssociation = BinaryAssociation(
    name="resUnits949",
    ends={
        Property(name="NFP_Integer951", type=MARTE_GQAM_GaAcqStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAcqStep950", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_Operation942: BinaryAssociation = BinaryAssociation(
    name="base_Operation942",
    ends={
        Property(name="GQAM_MARTE_Operation", type=MARTE_GQAM_GaRequestedService, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaRequestedService", type=GQAM_MARTE_Operation, multiplicity=Multiplicity(1, 1))
    }
)
startObs943: BinaryAssociation = BinaryAssociation(
    name="startObs943",
    ends={
        Property(name="GQAM_MARTE_TimeObservation", type=MARTE_GQAM_GaTimedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaTimedObs", type=GQAM_MARTE_TimeObservation, multiplicity=Multiplicity(0, 9999))
    }
)
endObs944: BinaryAssociation = BinaryAssociation(
    name="endObs944",
    ends={
        Property(name="GQAM_MARTE_TimeObservation946", type=MARTE_GQAM_GaTimedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaTimedObs945", type=GQAM_MARTE_TimeObservation, multiplicity=Multiplicity(0, 9999))
    }
)
utility962: BinaryAssociation = BinaryAssociation(
    name="utility962",
    ends={
        Property(name="UtilityType964", type=MARTE_GQAM_GaLatencyObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaLatencyObs963", type=UtilityType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maxJitter965: BinaryAssociation = BinaryAssociation(
    name="maxJitter965",
    ends={
        Property(name="NFP_Duration967", type=MARTE_GQAM_GaLatencyObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaLatencyObs966", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
throughput968: BinaryAssociation = BinaryAssociation(
    name="throughput968",
    ends={
        Property(name="NFP_Frequency969", type=MARTE_GQAM_GaCommHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaCommHost", type=NFP_Frequency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilization970: BinaryAssociation = BinaryAssociation(
    name="utilization970",
    ends={
        Property(name="NFP_Real972", type=MARTE_GQAM_GaCommHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaCommHost971", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relRes952: BinaryAssociation = BinaryAssociation(
    name="relRes952",
    ends={
        Property(name="GRM_Resource953", type=MARTE_GQAM_GaRelStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaRelStep", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resUnits954: BinaryAssociation = BinaryAssociation(
    name="resUnits954",
    ends={
        Property(name="NFP_Integer956", type=MARTE_GQAM_GaRelStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaRelStep955", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
latency957: BinaryAssociation = BinaryAssociation(
    name="latency957",
    ends={
        Property(name="NFP_Duration958", type=MARTE_GQAM_GaLatencyObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaLatencyObs", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
miss959: BinaryAssociation = BinaryAssociation(
    name="miss959",
    ends={
        Property(name="NFP_Real961", type=MARTE_GQAM_GaLatencyObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaLatencyObs960", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
demand980: BinaryAssociation = BinaryAssociation(
    name="demand980",
    ends={
        Property(name="GQAM_GaWorkloadEvent982", type=MARTE_GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadBehavior981", type=GQAM_GaWorkloadEvent, multiplicity=Multiplicity(0, 9999))
    }
)
base_NamedElement983: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement983",
    ends={
        Property(name="GQAM_MARTE_NamedElement985", type=MARTE_GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadBehavior984", type=GQAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
context986: BinaryAssociation = BinaryAssociation(
    name="context986",
    ends={
        Property(name="NFP_String987", type=MARTE_GQAM_GaAnalysisContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAnalysisContext", type=NFP_String, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packetSize973: BinaryAssociation = BinaryAssociation(
    name="packetSize973",
    ends={
        Property(name="NFP_DataSize974", type=MARTE_GQAM_GaCommChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaCommChannel", type=NFP_DataSize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
utlization975: BinaryAssociation = BinaryAssociation(
    name="utlization975",
    ends={
        Property(name="NFP_Real977", type=MARTE_GQAM_GaCommChannel, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaCommChannel976", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behavior978: BinaryAssociation = BinaryAssociation(
    name="behavior978",
    ends={
        Property(name="GQAM_GaScenario979", type=MARTE_GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaWorkloadBehavior", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 9999))
    }
)
isSched996: BinaryAssociation = BinaryAssociation(
    name="isSched996",
    ends={
        Property(name="NFP_Boolean997", type=MARTE_SAM_SaAnalysisContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaAnalysisContext", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
workload988: BinaryAssociation = BinaryAssociation(
    name="workload988",
    ends={
        Property(name="GQAM_GaWorkloadBehavior", type=MARTE_GQAM_GaAnalysisContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAnalysisContext989", type=GQAM_GaWorkloadBehavior, multiplicity=Multiplicity(1, 9999))
    }
)
platform990: BinaryAssociation = BinaryAssociation(
    name="platform990",
    ends={
        Property(name="GQAM_GaResourcesPlatform", type=MARTE_GQAM_GaAnalysisContext, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaAnalysisContext991", type=GQAM_GaResourcesPlatform, multiplicity=Multiplicity(1, 9999))
    }
)
resources992: BinaryAssociation = BinaryAssociation(
    name="resources992",
    ends={
        Property(name="GRM_Resource993", type=MARTE_GQAM_GaResourcesPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaResourcesPlatform", type=GRM_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
base_Classifier994: BinaryAssociation = BinaryAssociation(
    name="base_Classifier994",
    ends={
        Property(name="GQAM_MARTE_Classifier", type=MARTE_GQAM_GaResourcesPlatform, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_GQAM_GaResourcesPlatform995", type=GQAM_MARTE_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
timing1009: BinaryAssociation = BinaryAssociation(
    name="timing1009",
    ends={
        Property(name="MARTE_SAM_SaEndtoEndFlow1010", type=GQAM_GaTimedObs, multiplicity=Multiplicity(0, 9999)),
        Property(name="GQAM_GaTimedObs1011", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1))
    }
)
base_NamedElement1012: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement1012",
    ends={
        Property(name="SAM_MARTE_NamedElement", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow1013", type=SAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
deadline1014: BinaryAssociation = BinaryAssociation(
    name="deadline1014",
    ends={
        Property(name="NFP_Duration1015", type=MARTE_SAM_SaCommStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommStep", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spareCap1016: BinaryAssociation = BinaryAssociation(
    name="spareCap1016",
    ends={
        Property(name="NFP_Duration1018", type=MARTE_SAM_SaCommStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommStep1017", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isSched998: BinaryAssociation = BinaryAssociation(
    name="isSched998",
    ends={
        Property(name="NFP_Boolean999", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schSlack1000: BinaryAssociation = BinaryAssociation(
    name="schSlack1000",
    ends={
        Property(name="NFP_Real1002", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow1001", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end2EndT1003: BinaryAssociation = BinaryAssociation(
    name="end2EndT1003",
    ends={
        Property(name="NFP_Duration1005", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow1004", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end2EndD1006: BinaryAssociation = BinaryAssociation(
    name="end2EndD1006",
    ends={
        Property(name="NFP_Duration1008", type=MARTE_SAM_SaEndtoEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaEndtoEndFlow1007", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spareCap1029: BinaryAssociation = BinaryAssociation(
    name="spareCap1029",
    ends={
        Property(name="NFP_Duration1031", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1030", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schSlack1032: BinaryAssociation = BinaryAssociation(
    name="schSlack1032",
    ends={
        Property(name="NFP_Real1034", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1033", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preemptT1035: BinaryAssociation = BinaryAssociation(
    name="preemptT1035",
    ends={
        Property(name="NFP_Duration1037", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1036", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schSlack1019: BinaryAssociation = BinaryAssociation(
    name="schSlack1019",
    ends={
        Property(name="NFP_Real1021", type=MARTE_SAM_SaCommStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommStep1020", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_BehavioralFeature1022: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature1022",
    ends={
        Property(name="SAM_MARTE_BehavioralFeature", type=MARTE_SAM_SaCommStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommStep1023", type=SAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature1024: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature1024",
    ends={
        Property(name="SAM_MARTE_BehavioralFeature1025", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep", type=SAM_MARTE_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
deadline1026: BinaryAssociation = BinaryAssociation(
    name="deadline1026",
    ends={
        Property(name="NFP_Duration1028", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1027", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
numberSelfSuspensions1049: BinaryAssociation = BinaryAssociation(
    name="numberSelfSuspensions1049",
    ends={
        Property(name="NFP_Integer1051", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1050", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacity1052: BinaryAssociation = BinaryAssociation(
    name="capacity1052",
    ends={
        Property(name="NFP_Integer1053", type=MARTE_SAM_SaSharedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSharedResource", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isPreemp1054: BinaryAssociation = BinaryAssociation(
    name="isPreemp1054",
    ends={
        Property(name="NFP_Boolean1056", type=MARTE_SAM_SaSharedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSharedResource1055", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
readyT1038: BinaryAssociation = BinaryAssociation(
    name="readyT1038",
    ends={
        Property(name="NFP_Duration1040", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1039", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nonpreemptionBlocking1041: BinaryAssociation = BinaryAssociation(
    name="nonpreemptionBlocking1041",
    ends={
        Property(name="NFP_Duration1043", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1042", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sharedRes1044: BinaryAssociation = BinaryAssociation(
    name="sharedRes1044",
    ends={
        Property(name="SAM_SaSharedResource", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1045", type=SAM_SaSharedResource, multiplicity=Multiplicity(0, 9999))
    }
)
selfSuspensionBlocking1046: BinaryAssociation = BinaryAssociation(
    name="selfSuspensionBlocking1046",
    ends={
        Property(name="NFP_Duration1048", type=MARTE_SAM_SaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaStep1047", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blockT1068: BinaryAssociation = BinaryAssociation(
    name="blockT1068",
    ends={
        Property(name="NFP_Duration1070", type=MARTE_SAM_SaSchedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSchedObs1069", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overlaps1071: BinaryAssociation = BinaryAssociation(
    name="overlaps1071",
    ends={
        Property(name="NFP_Integer1073", type=MARTE_SAM_SaSchedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSchedObs1072", type=NFP_Integer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isSched1074: BinaryAssociation = BinaryAssociation(
    name="isSched1074",
    ends={
        Property(name="NFP_Boolean1075", type=MARTE_SAM_SaCommHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommHost", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isConsum1057: BinaryAssociation = BinaryAssociation(
    name="isConsum1057",
    ends={
        Property(name="NFP_Boolean1059", type=MARTE_SAM_SaSharedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSharedResource1058", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
acquisT1060: BinaryAssociation = BinaryAssociation(
    name="acquisT1060",
    ends={
        Property(name="NFP_Duration1062", type=MARTE_SAM_SaSharedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSharedResource1061", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
releaseT1063: BinaryAssociation = BinaryAssociation(
    name="releaseT1063",
    ends={
        Property(name="NFP_Duration1065", type=MARTE_SAM_SaSharedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSharedResource1064", type=NFP_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
suspentions1066: BinaryAssociation = BinaryAssociation(
    name="suspentions1066",
    ends={
        Property(name="NFP_Integer1067", type=MARTE_SAM_SaSchedObs, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaSchedObs", type=NFP_Integer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ISRswitchT1087: BinaryAssociation = BinaryAssociation(
    name="ISRswitchT1087",
    ends={
        Property(name="NFP_Duration1089", type=MARTE_SAM_SaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaExecHost1088", type=NFP_Duration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ISRprioRange1090: BinaryAssociation = BinaryAssociation(
    name="ISRprioRange1090",
    ends={
        Property(name="IntegerInterval1092", type=MARTE_SAM_SaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaExecHost1091", type=IntegerInterval, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noSync1093: BinaryAssociation = BinaryAssociation(
    name="noSync1093",
    ends={
        Property(name="NFP_Boolean1094", type=MARTE_PAM_PaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaStep", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schSlack1076: BinaryAssociation = BinaryAssociation(
    name="schSlack1076",
    ends={
        Property(name="NFP_Real1078", type=MARTE_SAM_SaCommHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaCommHost1077", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isSched1079: BinaryAssociation = BinaryAssociation(
    name="isSched1079",
    ends={
        Property(name="NFP_Boolean1080", type=MARTE_SAM_SaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaExecHost", type=NFP_Boolean, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schSlack1081: BinaryAssociation = BinaryAssociation(
    name="schSlack1081",
    ends={
        Property(name="NFP_Real1083", type=MARTE_SAM_SaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaExecHost1082", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schedUtiliz1084: BinaryAssociation = BinaryAssociation(
    name="schedUtiliz1084",
    ends={
        Property(name="NFP_Real1086", type=MARTE_SAM_SaExecHost, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_SAM_SaExecHost1085", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resource1104: BinaryAssociation = BinaryAssociation(
    name="resource1104",
    ends={
        Property(name="GRM_Resource1105", type=MARTE_PAM_PaResPassStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaResPassStep", type=GRM_Resource, multiplicity=Multiplicity(0, 1))
    }
)
resUnits1106: BinaryAssociation = BinaryAssociation(
    name="resUnits1106",
    ends={
        Property(name="NFP_Integer1108", type=MARTE_PAM_PaResPassStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaResPassStep1107", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extOpCount1095: BinaryAssociation = BinaryAssociation(
    name="extOpCount1095",
    ends={
        Property(name="NFP_Real1097", type=MARTE_PAM_PaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaStep1096", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behavDemand1098: BinaryAssociation = BinaryAssociation(
    name="behavDemand1098",
    ends={
        Property(name="GQAM_GaScenario1100", type=MARTE_PAM_PaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaStep1099", type=GQAM_GaScenario, multiplicity=Multiplicity(0, 9999))
    }
)
behavCount1101: BinaryAssociation = BinaryAssociation(
    name="behavCount1101",
    ends={
        Property(name="NFP_Real1103", type=MARTE_PAM_PaStep, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaStep1102", type=NFP_Real, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance1119: BinaryAssociation = BinaryAssociation(
    name="instance1119",
    ends={
        Property(name="GRM_SchedulableResource1121", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance1120", type=GRM_SchedulableResource, multiplicity=Multiplicity(0, 1))
    }
)
host1122: BinaryAssociation = BinaryAssociation(
    name="host1122",
    ends={
        Property(name="GQAM_GaExecHost1124", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance1123", type=GQAM_GaExecHost, multiplicity=Multiplicity(0, 1))
    }
)
utilization1109: BinaryAssociation = BinaryAssociation(
    name="utilization1109",
    ends={
        Property(name="NFP_Real1110", type=MARTE_PAM_PaLogicalResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaLogicalResource", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput1111: BinaryAssociation = BinaryAssociation(
    name="throughput1111",
    ends={
        Property(name="NFP_Frequency1113", type=MARTE_PAM_PaLogicalResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaLogicalResource1112", type=NFP_Frequency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
poolSize1114: BinaryAssociation = BinaryAssociation(
    name="poolSize1114",
    ends={
        Property(name="NFP_Integer1116", type=MARTE_PAM_PaLogicalResource, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaLogicalResource1115", type=NFP_Integer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
poolSize1117: BinaryAssociation = BinaryAssociation(
    name="poolSize1117",
    ends={
        Property(name="NFP_Integer1118", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance", type=NFP_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
utilization1125: BinaryAssociation = BinaryAssociation(
    name="utilization1125",
    ends={
        Property(name="NFP_Real1127", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance1126", type=NFP_Real, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throughput1128: BinaryAssociation = BinaryAssociation(
    name="throughput1128",
    ends={
        Property(name="NFP_Frequency1130", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance1129", type=NFP_Frequency, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base_NamedElement1131: BinaryAssociation = BinaryAssociation(
    name="base_NamedElement1131",
    ends={
        Property(name="PAM_MARTE_NamedElement", type=MARTE_PAM_PaRunTInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="MARTE_PAM_PaRunTInstance1132", type=PAM_MARTE_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_MARTE_NFPs_NfpType_TupleType = Generalization(general=TupleType, specific=MARTE_NFPs_NfpType)
gen_MARTE_Time_TimedValueSpecification_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedValueSpecification)
gen_MARTE_Time_TimedConstraint_NFPs_NfpConstraint = Generalization(general=NFPs_NfpConstraint, specific=MARTE_Time_TimedConstraint)
gen_MARTE_Time_TimedConstraint_Time_TimedElement = Generalization(general=Time_TimedElement, specific=MARTE_Time_TimedConstraint)
gen_MARTE_Time_ClockConstraint_NFPs_NfpConstraint = Generalization(general=NFPs_NfpConstraint, specific=MARTE_Time_ClockConstraint)
gen_MARTE_Time_ClockConstraint_Time_TimedElement = Generalization(general=Time_TimedElement, specific=MARTE_Time_ClockConstraint)
gen_MARTE_Time_TimedDurationObservation_TimedObservation = Generalization(general=TimedObservation, specific=MARTE_Time_TimedDurationObservation)
gen_MARTE_Time_TimedEvent_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedEvent)
gen_MARTE_Time_TimedProcessing_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedProcessing)
gen_MARTE_Time_TimedObservation_TimedElement = Generalization(general=TimedElement, specific=MARTE_Time_TimedObservation)
gen_MARTE_Time_TimedInstantObservation_TimedObservation = Generalization(general=TimedObservation, specific=MARTE_Time_TimedInstantObservation)
gen_MARTE_GRM_CommunicationEndPoint_Resource = Generalization(general=Resource, specific=MARTE_GRM_CommunicationEndPoint)
gen_MARTE_GRM_SynchronizationResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_SynchronizationResource)
gen_MARTE_GRM_ConcurrencyResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_ConcurrencyResource)
gen_MARTE_GRM_Scheduler_Resource = Generalization(general=Resource, specific=MARTE_GRM_Scheduler)
gen_MARTE_GRM_StorageResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_StorageResource)
gen_MARTE_GRM_ProcessingResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_ProcessingResource)
gen_MARTE_GRM_ComputingResource_ProcessingResource = Generalization(general=ProcessingResource, specific=MARTE_GRM_ComputingResource)
gen_MARTE_GRM_MutualExclusionResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_MutualExclusionResource)
gen_MARTE_GRM_SecondaryScheduler_Scheduler = Generalization(general=Scheduler, specific=MARTE_GRM_SecondaryScheduler)
gen_MARTE_GRM_CommunicationMedia_ProcessingResource = Generalization(general=ProcessingResource, specific=MARTE_GRM_CommunicationMedia)
gen_MARTE_GRM_SchedulableResource_Resource = Generalization(general=Resource, specific=MARTE_GRM_SchedulableResource)
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
gen_MARTE_HwComputing_HwComputingResource_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwComputing_HwComputingResource)
gen_MARTE_HwComputing_HwComputingResource_GRM_ComputingResource = Generalization(general=GRM_ComputingResource, specific=MARTE_HwComputing_HwComputingResource)
gen_MARTE_HwComputing_HwBranchPredictor_HwResource = Generalization(general=HwResource, specific=MARTE_HwComputing_HwBranchPredictor)
gen_MARTE_HwComputing_HwASIC_HwComputingResource = Generalization(general=HwComputingResource, specific=MARTE_HwComputing_HwASIC)
gen_MARTE_HwComputing_HwPLD_HwComputingResource = Generalization(general=HwComputingResource, specific=MARTE_HwComputing_HwPLD)
gen_MARTE_HwComputing_HwISA_HwResource = Generalization(general=HwResource, specific=MARTE_HwComputing_HwISA)
gen_MARTE_HwComputing_HwMCU_HwComputingResource = Generalization(general=HwComputingResource, specific=MARTE_HwComputing_HwMCU)
gen_MARTE_HwCommunication_HwMedia_GRM_CommunicationMedia = Generalization(general=GRM_CommunicationMedia, specific=MARTE_HwCommunication_HwMedia)
gen_MARTE_HwCommunication_HwMedia_HwCommunication_HwCommunicationResource = Generalization(general=HwCommunication_HwCommunicationResource, specific=MARTE_HwCommunication_HwMedia)
gen_MARTE_HwCommunication_HwBus_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwCommunication_HwBus)
gen_MARTE_HwCommunication_HwCommunicationResource_HwResource = Generalization(general=HwResource, specific=MARTE_HwCommunication_HwCommunicationResource)
gen_MARTE_HwCommunication_HwArbiter_HwCommunicationResource = Generalization(general=HwCommunicationResource, specific=MARTE_HwCommunication_HwArbiter)
gen_MARTE_HwCommunication_HwBridge_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwCommunication_HwBridge)
gen_MARTE_HwCommunication_HwEndPoint_HwCommunication_HwCommunicationResource = Generalization(general=HwCommunication_HwCommunicationResource, specific=MARTE_HwCommunication_HwEndPoint)
gen_MARTE_HwCommunication_HwEndPoint_GRM_CommunicationEndPoint = Generalization(general=GRM_CommunicationEndPoint, specific=MARTE_HwCommunication_HwEndPoint)
gen_MARTE_HwCommunication_HwPort_HwEndPoint = Generalization(general=HwEndPoint, specific=MARTE_HwCommunication_HwPort)
gen_MARTE_HwStorageManager_HwStorageManager_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwStorageManager_HwStorageManager)
gen_MARTE_HwStorageManager_HwStorageManager_GRM_StorageResource = Generalization(general=GRM_StorageResource, specific=MARTE_HwStorageManager_HwStorageManager)
gen_MARTE_HwStorageManager_HwDMA_HwStorageManager_HwStorageManager = Generalization(general=HwStorageManager_HwStorageManager, specific=MARTE_HwStorageManager_HwDMA)
gen_MARTE_HwStorageManager_HwDMA_HwCommunication_HwArbiter = Generalization(general=HwCommunication_HwArbiter, specific=MARTE_HwStorageManager_HwDMA)
gen_MARTE_HwCommunication_HwConnection_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwCommunication_HwConnection)
gen_MARTE_HwStorageManager_HwMMU_HwStorageManager = Generalization(general=HwStorageManager, specific=MARTE_HwStorageManager_HwMMU)
gen_MARTE_HwMemory_HwMemory_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwMemory_HwMemory)
gen_MARTE_HwMemory_HwMemory_GRM_StorageResource = Generalization(general=GRM_StorageResource, specific=MARTE_HwMemory_HwMemory)
gen_MARTE_HwMemory_HwRAM_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwRAM)
gen_MARTE_HwMemory_HwROM_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwROM)
gen_MARTE_HwMemory_HwDrive_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwDrive)
gen_MARTE_HwTiming_HwTimingResource_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwTiming_HwTimingResource)
gen_MARTE_HwTiming_HwTimingResource_GRM_TimingResource = Generalization(general=GRM_TimingResource, specific=MARTE_HwTiming_HwTimingResource)
gen_MARTE_HwTiming_HwClock_HwTimingResource = Generalization(general=HwTimingResource, specific=MARTE_HwTiming_HwClock)
gen_MARTE_HwTiming_HwTimer_HwTimingResource = Generalization(general=HwTimingResource, specific=MARTE_HwTiming_HwTimer)
gen_MARTE_HwMemory_HwCache_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwMemory_HwCache)
gen_MARTE_HwDevice_HwDevice_HwGeneral_HwResource = Generalization(general=HwGeneral_HwResource, specific=MARTE_HwDevice_HwDevice)
gen_MARTE_HwDevice_HwDevice_GRM_DeviceResource = Generalization(general=GRM_DeviceResource, specific=MARTE_HwDevice_HwDevice)
gen_MARTE_HwDevice_HwI_O_HwDevice = Generalization(general=HwDevice, specific=MARTE_HwDevice_HwI_O)
gen_MARTE_HwGeneral_HwResourceService_GrService = Generalization(general=GrService, specific=MARTE_HwGeneral_HwResourceService)
gen_MARTE_HwDevice_HwSupport_HwDevice = Generalization(general=HwDevice, specific=MARTE_HwDevice_HwSupport)
gen_MARTE_HwDevice_HWActuator_HwI_O = Generalization(general=HwI_O, specific=MARTE_HwDevice_HWActuator)
gen_MARTE_HwDevice_HWSensor_HwI_O = Generalization(general=HwI_O, specific=MARTE_HwDevice_HWSensor)
gen_MARTE_HwDevice_HwPeripheral_HwDevice = Generalization(general=HwDevice, specific=MARTE_HwDevice_HwPeripheral)
gen_MARTE_HwGeneral_HwResource_Resource = Generalization(general=Resource, specific=MARTE_HwGeneral_HwResource)
gen_MARTE_HwLayout_HwComponent_HwResource = Generalization(general=HwResource, specific=MARTE_HwLayout_HwComponent)
gen_MARTE_HwPower_HwPowerSupply_HwComponent = Generalization(general=HwComponent, specific=MARTE_HwPower_HwPowerSupply)
gen_MARTE_HwPeripheral_OperationImpl_Operation = Generalization(general=Operation, specific=MARTE_HwPeripheral_OperationImpl)
gen_MARTE_HwPeripheral_RegisterAction_Action = Generalization(general=Action, specific=MARTE_HwPeripheral_RegisterAction)
gen_MARTE_HwPeripheral_WriteRegisterAction_RegisterAction = Generalization(general=RegisterAction, specific=MARTE_HwPeripheral_WriteRegisterAction)
gen_MARTE_HwPeripheral_ReadRegisterAction_RegisterAction = Generalization(general=RegisterAction, specific=MARTE_HwPeripheral_ReadRegisterAction)
gen_MARTE_HwPeripheral_PeripheralActivity_Activity = Generalization(general=Activity, specific=MARTE_HwPeripheral_PeripheralActivity)
gen_MARTE_HwPower_HwCoolingSupply_HwComponent = Generalization(general=HwComponent, specific=MARTE_HwPower_HwCoolingSupply)
gen_MARTE_HwIO_HwLine_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwIO_HwLine)
gen_MARTE_HwRegister_HwRegister_HwMemory = Generalization(general=HwMemory, specific=MARTE_HwRegister_HwRegister)
gen_MARTE_HwDeviceFunction_HwDeviceFunction_Operation = Generalization(general=Operation, specific=MARTE_HwDeviceFunction_HwDeviceFunction)
gen_MARTE_HwIO_HwPin_HwEndPoint = Generalization(general=HwEndPoint, specific=MARTE_HwIO_HwPin)
gen_MARTE_HwPackage_HwPackagePin_HwEndPoint = Generalization(general=HwEndPoint, specific=MARTE_HwPackage_HwPackagePin)
gen_MARTE_HwPackage_HwWire_HwMedia = Generalization(general=HwMedia, specific=MARTE_HwPackage_HwWire)
gen_MARTE_SW_ResourceCore_SwResource_Resource = Generalization(general=Resource, specific=MARTE_SW_ResourceCore_SwResource)
gen_MARTE_SW_ResourceCore_SwAccessService_GrService = Generalization(general=GrService, specific=MARTE_SW_ResourceCore_SwAccessService)
gen_MARTE_SW_Concurrency_SwConcurrentResource_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Concurrency_SwConcurrentResource)
gen_MARTE_SW_Concurrency_EntryPoint_Allocate = Generalization(general=Allocate, specific=MARTE_SW_Concurrency_EntryPoint)
gen_MARTE_SW_Concurrency_InterruptResource_SwConcurrentResource = Generalization(general=SwConcurrentResource, specific=MARTE_SW_Concurrency_InterruptResource)
gen_MARTE_SW_Concurrency_SwSchedulableResource_SW_Concurrency_SwConcurrentResource = Generalization(general=SW_Concurrency_SwConcurrentResource, specific=MARTE_SW_Concurrency_SwSchedulableResource)
gen_MARTE_SW_Concurrency_SwSchedulableResource_GRM_SchedulableResource = Generalization(general=GRM_SchedulableResource, specific=MARTE_SW_Concurrency_SwSchedulableResource)
gen_MARTE_SW_Concurrency_MemoryPartition_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Concurrency_MemoryPartition)
gen_MARTE_SW_Concurrency_Alarm_InterruptResource = Generalization(general=InterruptResource, specific=MARTE_SW_Concurrency_Alarm)
gen_MARTE_SW_Concurrency_SwTimerResource_TimerResource = Generalization(general=TimerResource, specific=MARTE_SW_Concurrency_SwTimerResource)
gen_MARTE_SW_Brokering_DeviceBroker_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Brokering_DeviceBroker)
gen_MARTE_SW_Brokering_MemoryBroker_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Brokering_MemoryBroker)
gen_MARTE_SW_Interaction_SwInteractionResource_SwResource = Generalization(general=SwResource, specific=MARTE_SW_Interaction_SwInteractionResource)
gen_MARTE_SW_Interaction_SwCommunicationResource_SW_Interaction_SwInteractionResource = Generalization(general=SW_Interaction_SwInteractionResource, specific=MARTE_SW_Interaction_SwCommunicationResource)
gen_MARTE_SW_Interaction_SwCommunicationResource_GRM_CommunicationMedia = Generalization(general=GRM_CommunicationMedia, specific=MARTE_SW_Interaction_SwCommunicationResource)
gen_MARTE_SW_Interaction_SwSynchronizationResource_SW_Interaction_SwInteractionResource = Generalization(general=SW_Interaction_SwInteractionResource, specific=MARTE_SW_Interaction_SwSynchronizationResource)
gen_MARTE_SW_Interaction_SwSynchronizationResource_GRM_SynchronizationResource = Generalization(general=GRM_SynchronizationResource, specific=MARTE_SW_Interaction_SwSynchronizationResource)
gen_MARTE_SW_Interaction_MessageComResource_SwCommunicationResource = Generalization(general=SwCommunicationResource, specific=MARTE_SW_Interaction_MessageComResource)
gen_MARTE_SW_Interaction_NotificationResource_SwSynchronizationResource = Generalization(general=SwSynchronizationResource, specific=MARTE_SW_Interaction_NotificationResource)
gen_MARTE_SW_Interaction_SharedDataComResource_SwCommunicationResource = Generalization(general=SwCommunicationResource, specific=MARTE_SW_Interaction_SharedDataComResource)
gen_MARTE_SW_Interaction_SwMutualExclusionResource_SW_Interaction_SwSynchronizationResource = Generalization(general=SW_Interaction_SwSynchronizationResource, specific=MARTE_SW_Interaction_SwMutualExclusionResource)
gen_MARTE_SW_Interaction_SwMutualExclusionResource_GRM_MutualExclusionResource = Generalization(general=GRM_MutualExclusionResource, specific=MARTE_SW_Interaction_SwMutualExclusionResource)
gen_MARTE_GQAM_GaScenario_GRM_ResourceUsage = Generalization(general=GRM_ResourceUsage, specific=MARTE_GQAM_GaScenario)
gen_MARTE_GQAM_GaScenario_Time_TimedProcessing = Generalization(general=Time_TimedProcessing, specific=MARTE_GQAM_GaScenario)
gen_MARTE_GQAM_GaStep_GaScenario = Generalization(general=GaScenario, specific=MARTE_GQAM_GaStep)
gen_MARTE_GQAM_GaExecHost_GRM_Scheduler = Generalization(general=GRM_Scheduler, specific=MARTE_GQAM_GaExecHost)
gen_MARTE_GQAM_GaExecHost_GRM_ComputingResource = Generalization(general=GRM_ComputingResource, specific=MARTE_GQAM_GaExecHost)
gen_MARTE_GQAM_GaRequestedService_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaRequestedService)
gen_MARTE_GQAM_GaCommStep_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaCommStep)
gen_MARTE_GQAM_GaAcqStep_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaAcqStep)
gen_MARTE_GQAM_GaRelStep_GaStep = Generalization(general=GaStep, specific=MARTE_GQAM_GaRelStep)
gen_MARTE_GQAM_GaTimedObs_NfpConstraint = Generalization(general=NfpConstraint, specific=MARTE_GQAM_GaTimedObs)
gen_MARTE_GQAM_GaCommHost_GRM_CommunicationMedia = Generalization(general=GRM_CommunicationMedia, specific=MARTE_GQAM_GaCommHost)
gen_MARTE_GQAM_GaCommHost_GRM_Scheduler = Generalization(general=GRM_Scheduler, specific=MARTE_GQAM_GaCommHost)
gen_MARTE_GQAM_GaLatencyObs_GaTimedObs = Generalization(general=GaTimedObs, specific=MARTE_GQAM_GaLatencyObs)
gen_MARTE_GQAM_GaAnalysisContext_CoreElements_Configuration = Generalization(general=CoreElements_Configuration, specific=MARTE_GQAM_GaAnalysisContext)
gen_MARTE_GQAM_GaAnalysisContext_Variables_ExpressionContext = Generalization(general=Variables_ExpressionContext, specific=MARTE_GQAM_GaAnalysisContext)
gen_MARTE_GQAM_GaCommChannel_SchedulableResource = Generalization(general=SchedulableResource, specific=MARTE_GQAM_GaCommChannel)
gen_MARTE_SAM_SaAnalysisContext_GaAnalysisContext = Generalization(general=GaAnalysisContext, specific=MARTE_SAM_SaAnalysisContext)
gen_MARTE_SAM_SaCommStep_GaCommStep = Generalization(general=GaCommStep, specific=MARTE_SAM_SaCommStep)
gen_MARTE_SAM_SaStep_GaStep = Generalization(general=GaStep, specific=MARTE_SAM_SaStep)
gen_MARTE_SAM_SaSharedResource_MutualExclusionResource = Generalization(general=MutualExclusionResource, specific=MARTE_SAM_SaSharedResource)
gen_MARTE_SAM_SaCommHost_GaCommHost = Generalization(general=GaCommHost, specific=MARTE_SAM_SaCommHost)
gen_MARTE_SAM_SaSchedObs_GaTimedObs = Generalization(general=GaTimedObs, specific=MARTE_SAM_SaSchedObs)
gen_MARTE_PAM_PaStep_GaStep = Generalization(general=GaStep, specific=MARTE_PAM_PaStep)
gen_MARTE_SAM_SaExecHost_GaExecHost = Generalization(general=GaExecHost, specific=MARTE_SAM_SaExecHost)
gen_MARTE_PAM_PaCommStep_PAM_PaStep = Generalization(general=PAM_PaStep, specific=MARTE_PAM_PaCommStep)
gen_MARTE_PAM_PaCommStep_GQAM_GaCommStep = Generalization(general=GQAM_GaCommStep, specific=MARTE_PAM_PaCommStep)
gen_MARTE_PAM_PaResPassStep_GaStep = Generalization(general=GaStep, specific=MARTE_PAM_PaResPassStep)
gen_MARTE_PAM_PaLogicalResource_Resource = Generalization(general=Resource, specific=MARTE_PAM_PaLogicalResource)
gen_MARTE_PAM_PaRequestedStep_PAM_PaStep = Generalization(general=PAM_PaStep, specific=MARTE_PAM_PaRequestedStep)
gen_MARTE_PAM_PaRequestedStep_GQAM_GaRequestedService = Generalization(general=GQAM_GaRequestedService, specific=MARTE_PAM_PaRequestedStep)

# Domain Model
domain_model = DomainModel(
    name="MARTE",
    types={MARTE_NFPs_Nfp, NFPs_MARTE_Property, NFPs_Unit, NFPs_MARTE_EnumerationLiteral, MARTE_NFPs_NfpConstraint, MARTE_NFPs_Unit, MARTE_NFPs_NfpType, TupleType, MARTE_NFPs_Dimension, NFPs_Dimension, NFPs_MARTE_Enumeration, NFPs_MARTE_Constraint, CoreElements_Mode, MARTE_CoreElements_Configuration, CoreElements_MARTE_StructuredClassifier, CoreElements_MARTE_Package, MARTE_CoreElements_Mode, CoreElements_MARTE_State, MARTE_Alloc_Allocated, Alloc_MARTE_NamedElement, MARTE_CoreElements_ModeTransition, CoreElements_MARTE_Transition, MARTE_CoreElements_ModeBehavior, CoreElements_MARTE_StateMachine, MARTE_Alloc_AllocateActivityGroup, Alloc_MARTE_ActivityPartition, MARTE_Alloc_NfpRefine, Alloc_MARTE_Dependency, NFPs_NfpConstraint, MARTE_Alloc_Assign, Alloc_MARTE_Element, Alloc_Allocated, MARTE_Alloc_Allocate, Alloc_MARTE_Abstraction, MARTE_Time_TimedDomain, Time_MARTE_Namespace, MARTE_Time_Clock, Time_MARTE_InstanceSpecification, Alloc_MARTE_Comment, MARTE_Time_ClockType, Time_MARTE_Enumeration, Time_MARTE_Operation, Time_ClockType, Time_MARTE_Property, Time_Clock, MARTE_Time_TimedValueSpecification, TimedElement, Time_MARTE_ValueSpecification, MARTE_Time_TimedConstraint, Time_TimedElement, MARTE_Time_ClockConstraint, Time_MARTE_Class, MARTE_Time_TimedElement, MARTE_Time_TimedDurationObservation, Time_MARTE_DurationObservation, MARTE_Time_TimedEvent, Time_MARTE_TimeEvent, MARTE_Time_TimedProcessing, Time_MARTE_Action, Time_MARTE_Behavior, MARTE_Time_TimedObservation, MARTE_Time_TimedInstantObservation, TimedObservation, Time_MARTE_TimeObservation, Time_MARTE_Event, MARTE_GRM_Resource, NFP_Integer, GRM_MARTE_Property, GRM_MARTE_InstanceSpecification, GRM_MARTE_Classifier, GRM_MARTE_Lifeline, Time_MARTE_Message, MARTE_GRM_CommunicationEndPoint, MARTE_GRM_SynchronizationResource, MARTE_GRM_ConcurrencyResource, MARTE_GRM_Scheduler, GRM_MARTE_OpaqueExpression, GRM_ProcessingResource, GRM_MARTE_ConnectableElement, MARTE_GRM_StorageResource, Resource, GRM_MutualExclusionResource, GRM_SchedulableResource, MARTE_GRM_ProcessingResource, NFP_Real, GRM_Scheduler, MARTE_GRM_ComputingResource, ProcessingResource, MARTE_GRM_MutualExclusionResource, GRM_ComputingResource, GRM_SecondaryScheduler, MARTE_GRM_SecondaryScheduler, Scheduler, MARTE_GRM_CommunicationMedia, GRM_MARTE_Connector, MARTE_GRM_SchedulableResource, SchedParameters, MARTE_GRM_DeviceResource, MARTE_GRM_TimingResource, MARTE_GRM_ClockResource, TimingResource, MARTE_GRM_TimerResource, MARTE_GRM_GrService, GRM_Resource, GRM_MARTE_ExecutionSpecification, GRM_MARTE_BehavioralFeature, NFP_Duration, NFP_DataTxRate, MARTE_GRM_Release, GrService, MARTE_GRM_Acquire, MARTE_GRM_ResourceUsage, NFP_DataSize, NFP_Power, NFP_Energy, GRM_MARTE_Behavior, GRM_MARTE_Collaboration, GRM_MARTE_CollaborationUse, MARTE_RSM_LinkTopology, RSM_MARTE_Connector, MARTE_RSM_DefaultLink, LinkTopology, MARTE_RSM_InterRepetition, IntegerVector, MARTE_RSM_Distribute, Allocate, GRM_MARTE_NamedElement, GRM_ResourceUsage, MARTE_RSM_Reshape, MARTE_RSM_Tiler, IntegerMatrix, ShapeSpecification, TilerSpecification, MARTE_RSM_Shaped, RSM_MARTE_MultiplicityElement, MARTE_Variables_Var, Variables_MARTE_Property, MARTE_Variables_ExpressionContext, Variables_MARTE_NamedElement, RSM_MARTE_ConnectorEnd, DataTypes_MARTE_DataType, MARTE_DataTypes_IntervalType, MARTE_DataTypes_CollectionType, MARTE_DataTypes_BoundedSubtype, DataTypes_MARTE_Property, MARTE_DataTypes_TupleType, MARTE_HLAM_RtUnit, MARTE_DataTypes_ChoiceType, HLAM_MARTE_BehavioredClassifier, MARTE_HLAM_PpUnit, HLAM_MARTE_Behavior, HLAM_MARTE_Operation, MARTE_HLAM_RtFeature, HLAM_MARTE_BehavioralFeature, HLAM_MARTE_Message, HLAM_MARTE_Signal, HLAM_MARTE_Port, HLAM_MARTE_InvocationAction, HLAM_RtSpecification, Time_TimedInstantObservation, NFP_DateTime, NFP_Percentage, MARTE_HLAM_RtSpecification, UtilityType, ArrivalPattern, MARTE_HLAM_RtAction, HLAM_MARTE_Comment, MARTE_HLAM_RtService, MARTE_HwComputing_HwProcessor, HwComputingResource, MARTE_HwComputing_PLD_Organization, NFP_Natural, HwComputing_HwISA, HwComputing_HwBranchPredictor, HwMemory_HwCache, HwStorageManager_HwMMU, MARTE_HwComputing_HwComputingResource, HwGeneral_HwResource, NFP_FrequencyInterval, MARTE_HwComputing_HwBranchPredictor, MARTE_HwComputing_HwASIC, MARTE_HwComputing_HwPLD, HwComputing_PLD_Organization, MARTE_HwComputing_HwISA, HwResource, NFP_String, MARTE_HwComputing_HwMCU, HwComputing_HwProcessor, HwDevice_HwPeripheral, HwRegister_HwRegister, HwPackage_HwPackage, HwIO_HwPin, HwCommunication_HwPort, HwMemory_HwRAM, HwComputing_HwComputingResource, MARTE_HwCommunication_HwMedia, GRM_CommunicationMedia, HwCommunication_HwCommunicationResource, HwCommunication_HwArbiter, MARTE_HwCommunication_HwBus, HwMedia, NFP_Boolean, MARTE_HwCommunication_HwCommunicationResource, MARTE_HwCommunication_HwArbiter, HwCommunicationResource, HwCommunication_HwMedia, MARTE_HwCommunication_HwBridge, MARTE_HwCommunication_HwEndPoint, GRM_CommunicationEndPoint, MARTE_HwCommunication_HwPort, HwEndPoint, HwProtocol_HwProtocol, MARTE_HwStorageManager_HwStorageManager, GRM_StorageResource, HwMemory_HwMemory, MARTE_HwStorageManager_HwDMA, HwStorageManager_HwStorageManager, MARTE_HwCommunication_HwConnection, MARTE_HwStorageManager_HwMMU, HwStorageManager, MARTE_HwMemory_HwMemory, MARTE_HwMemory_Timing, HwMemory_Timing, MARTE_HwMemory_CacheStructure, MARTE_HwMemory_MemoryOrganization, MARTE_HwMemory_HwRAM, HwMemory, HwMemory_MemoryOrganization, MARTE_HwMemory_HwROM, MARTE_HwMemory_HwDrive, HwMemory_CacheStructure, MARTE_HwTiming_HwTimingResource, GRM_TimingResource, MARTE_HwTiming_HwClock, HwTimingResource, MARTE_HwTiming_HwTimer, MARTE_HwMemory_HwCache, MARTE_HwDevice_HwDevice, GRM_DeviceResource, HwDeviceFunction_HwDeviceFunction, MARTE_HwDevice_HwI_O, HwDevice, MARTE_HwDevice_HwSupport, HwTiming_HwClock, HwPeripheral_OperationImpl, HwPeripheral_PeripheralActivity, MARTE_HwGeneral_HwResourceService, MARTE_HwDevice_HWActuator, HwI_O, MARTE_HwDevice_HWSensor, MARTE_HwDevice_HwPeripheral, HwGeneral_HwResourceService, HwCommunication_HwEndPoint, NFP_Frequency, HwGeneral_MARTE_Operation, HwGeneral_MARTE_Activity, MARTE_HwGeneral_HwResource, NFP_Length, NFP_Area, NFP_NaturalInterval, MARTE_HwLayout_HwComponent, HwLayout_HwComponent, MARTE_HwLayout_Env_Condition, NFP_Price, HwLayout_Env_Condition, MARTE_HwPower_HwPowerSupply, HwComponent, Realnterval, Operation, HwPeripheral_MARTE_Operation, MARTE_HwPeripheral_RegisterAction, Action, MARTE_HwPeripheral_WriteRegisterAction, RegisterAction, HwPeripheral_MARTE_InputPin, MARTE_HwPeripheral_ReadRegisterAction, HwPeripheral_MARTE_OutputPin, MARTE_HwPeripheral_PeripheralActivity, Activity, HwPeripheral_RegisterAction, MARTE_HwPower_HwCoolingSupply, MARTE_HwPeripheral_OperationImpl, HwIO_HwLine, MARTE_HwIO_HwLine, MARTE_HwRegister_HwRegister, MARTE_HwDatasheet_HwDatasheet, MARTE_HwDeviceFunction_HwDeviceFunction, MARTE_HwIO_HwPin, HwPackage_HwPackagePin, MARTE_HwPackage_HwPackagePin, HwPackage_HwWire, MARTE_HwPackage_HwWire, MARTE_HwProtocol_HwProtocol, HwProtocol_MARTE_Operation, MARTE_HwDiagram_HwBlockDiagram, MARTE_HwPackage_HwPackage, MARTE_HwDiagram_HwCircuitDiagram, MARTE_HwDiagram_HwHRMDiagram, HwCommunication_HwConnection, MARTE_HwDiagram_SRMDiagram, SW_Brokering_DeviceBroker, MARTE_SW_ResourceCore_SwResource, SW_ResourceCore_MARTE_TypedElement, HwDiagram_MARTE_DataType, MARTE_SW_ResourceCore_SwAccessService, SW_ResourceCore_MARTE_Property, MARTE_SW_Concurrency_EntryPoint, SW_ResourceCore_MARTE_BehavioralFeature, MARTE_SW_Concurrency_SwConcurrentResource, SwResource, SW_Concurrency_MARTE_Element, SW_Concurrency_MARTE_TypedElement, SW_Concurrency_MARTE_BehavioralFeature, MARTE_SW_Concurrency_InterruptResource, SwConcurrentResource, MARTE_SW_Concurrency_SwSchedulableResource, SW_Concurrency_SwConcurrentResource, SW_Concurrency_MARTE_NamedElement, MARTE_SW_Concurrency_MemoryPartition, SW_Concurrency_MARTE_Namespace, MARTE_SW_Concurrency_Alarm, InterruptResource, MARTE_SW_Concurrency_SwTimerResource, TimerResource, MARTE_SW_Brokering_DeviceBroker, SW_Brokering_MARTE_TypedElement, SW_Brokering_MARTE_BehavioralFeature, SW_Brokering_MARTE_Operation, SW_Brokering_MARTE_Activity, MARTE_SW_Brokering_MemoryBroker, MARTE_SW_Interaction_SwInteractionResource, SW_Interaction_MARTE_TypedElement, MARTE_SW_Interaction_SwCommunicationResource, SW_Interaction_SwInteractionResource, MARTE_SW_Interaction_SwSynchronizationResource, GRM_SynchronizationResource, MARTE_SW_Interaction_SharedDataComResource, SwCommunicationResource, MARTE_SW_Interaction_MessageComResource, MARTE_SW_Interaction_NotificationResource, SwSynchronizationResource, SW_Interaction_MARTE_BehavioralFeature, MARTE_SW_Interaction_SwMutualExclusionResource, SW_Interaction_SwSynchronizationResource, MARTE_GCM_FlowProperty, GCM_MARTE_Property, MARTE_GCM_FlowPort, MARTE_GCM_ClientServerPort, GCM_MARTE_Interface, GCM_ClientServerSpecification, GCM_MARTE_Port, MARTE_GCM_ClientServerSpecification, MARTE_GCM_FlowSpecification, MARTE_GCM_ClientServerFeature, GCM_MARTE_BehavioralFeature, MARTE_GCM_GCMTrigger, GCM_MARTE_Trigger, GCM_MARTE_InvocationAction, MARTE_GCM_DataEvent, GCM_MARTE_AnyReceiveEvent, GCM_MARTE_Classifier, MARTE_GCM_DataPool, GCM_MARTE_Behavior, GCM_MARTE_Feature, MARTE_GCM_GCMInvocationAction, MARTE_GQAM_GaWorkloadGenerator, GQAM_MARTE_Behavior, GQAM_GaEventTrace, GQAM_GaScenario, GQAM_MARTE_TimeEvent, MARTE_GQAM_GaEventTrace, GQAM_MARTE_NamedElement, MARTE_GQAM_GaWorkloadEvent, GQAM_GaWorkloadGenerator, MARTE_GQAM_GaScenario, Time_TimedProcessing, GQAM_GaWorkloadEvent, GQAM_GaStep, GQAM_GaTimedObs, MARTE_GQAM_GaStep, GaScenario, MARTE_GQAM_GaExecHost, GQAM_GaExecHost, GQAM_GaRequestedService, MARTE_GQAM_GaRequestedService, GaStep, IntegerInterval, MARTE_GQAM_GaCommStep, MARTE_GQAM_GaAcqStep, MARTE_GQAM_GaRelStep, GQAM_MARTE_Operation, MARTE_GQAM_GaTimedObs, NfpConstraint, GQAM_MARTE_TimeObservation, MARTE_GQAM_GaCommHost, MARTE_GQAM_GaLatencyObs, GaTimedObs, MARTE_GQAM_GaAnalysisContext, CoreElements_Configuration, Variables_ExpressionContext, MARTE_GQAM_GaCommChannel, SchedulableResource, MARTE_GQAM_GaWorkloadBehavior, MARTE_SAM_SaAnalysisContext, GaAnalysisContext, MARTE_SAM_SaEndtoEndFlow, GQAM_GaWorkloadBehavior, GQAM_GaResourcesPlatform, MARTE_GQAM_GaResourcesPlatform, GQAM_MARTE_Classifier, SAM_MARTE_NamedElement, MARTE_SAM_SaCommStep, GaCommStep, SAM_MARTE_BehavioralFeature, MARTE_SAM_SaStep, MARTE_SAM_SaSharedResource, MutualExclusionResource, SAM_SaSharedResource, MARTE_SAM_SaCommHost, GaCommHost, MARTE_SAM_SaSchedObs, MARTE_PAM_PaStep, MARTE_SAM_SaExecHost, GaExecHost, MARTE_PAM_PaCommStep, GQAM_GaCommStep, MARTE_PAM_PaResPassStep, MARTE_PAM_PaLogicalResource, MARTE_PAM_PaRequestedStep, PAM_PaStep, MARTE_PAM_PaRunTInstance, PAM_MARTE_NamedElement, ConstraintKind, AllocationNature, AllocationKind, AllocationEndKind, AssignmentNature, AssignmentKind, VariableDirectionKind, PoolMgtPolicyKind, CallConcurrencyKind, ExecutionKind, ConcurrencyKind, SynchronizationKind, ISA_Type, PLD_Technology, PLD_Class, WritePolicy, CacheType, ROM_Type, Repl_Policy, ComponentKind, ConditionType, ComponentState, InterruptKind, AccessPolicyKind, QueuePolicyKind, MessageResourceKind, NotificationKind, NotificationResourceKind, ConcurrentAccessProtocolKind, MutualExclusionResourceKind, FlowDirectionKind, ClientServerKind, PortSpecificationKind, DataPoolOrderingKind, LaxityKind, OptimallityCriterionKind},
    associations={base_Property0, baseUnit1, base_EnumerationLiteral2, valueAttrib7, unitAttrib9, exprAttrib12, baseDimension15, base_Enumeration16, base_Constraint4, mode5, base_StructuredClassifier20, base_Package21, mode23, base_State26, base_NamedElement27, base_Transition18, base_StateMachine19, base_ActivityPartition33, base_Dependency34, constraint35, impliedConstraint37, from39, allocatedTo28, allocatedFrom30, base_Abstraction46, impliedConstraint47, base_Namespace50, base_InstanceSpecification51, to41, base_Comment44, base_Property57, unitType59, resolAttr60, maxValAttr63, offsetAttr66, getTime69, setTime71, type52, unit54, on79, base_ValueSpecification80, indexToValue74, base_Class77, base_DurationObservation82, base_TimeEvent83, every84, base_Action87, base_TimeObservation81, start95, finish97, resMult100, base_Property101, base_InstanceSpecification103, base_Classifier105, base_Behavior88, base_Message90, duration92, elementSize111, packetSize113, schedule115, base_Lifeline107, base_ConnectableElement109, protectedSharedRsources120, schedulableResources121, speedFactor124, mainScheduler125, ceiling127, processingUnits116, host118, schedParams132, dependentScheduler133, host136, virtualProcessingUnits139, elementSize142, base_Connector144, scheduler129, duration153, owner155, base_ExecutionSpecification156, base_BehavioralFeature158, blockT146, packetT148, capacity151, base_CollaborationUse164, execTime166, allocatedMemory168, usedMemory170, powerPeak173, energy175, base_Behavior160, base_Collaboration162, usedResources181, msgSize184, base_Connector187, repetitionShapeDependence188, base_NamedElement177, subUsage179, fromTiler193, toTiler195, patternShape198, repetitonShape200, origin203, paving205, patternShape189, repetitionSpace190, shape215, base_MultiplicityElement217, base_Property219, base_NamedElement220, fitting207, tiler210, base_ConnectorEnd213, base_DataType222, intervalAttrib224, base_DataType226, collectionAttrib229, base_DataType231, baseType221, defaultAttrib236, base_DataType239, tupleAttrib242, base_DataType244, choiceAttrib234, main251, memorySize253, base_BehavioredClassifier256, msgMaxSize258, srPoolWaitingTime247, operationalMode249, base_BehavioralFeature266, base_Message267, base_Signal269, base_Port271, base_InvocationAction273, specification275, memorySize261, base_BehavioredClassifier263, tRef280, relDl282, absDl285, boundDl287, rdTime290, miss293, priority295, utility277, occKind278, msgSize300, base_BehavioralFeature302, base_InvocationAction305, base_Comment298, base_BehavioralFeature308, architecture314, mips316, ipc319, nbCores322, nbPipelines325, nbStages328, nbRows310, nbColumns312, ownedISAs337, predictors339, caches341, ownedMMUs343, op_Frequencies345, nbALUs331, nbFPUs334, organization350, nbLUTs351, ndLUT_Inputs354, nbFlipFlops357, family346, inst_Width347, processor364, peripherals365, sfr367, packages369, pins371, ports373, blocksRAM360, blocksComputing362, bandWidth376, arbiters378, adressWidth381, wordWidth383, isSynchronous386, controlledMedias375, sides391, connectedTo392, isSerial388, protocols396, managedMemories397, pins394, transferWidth400, drivenBy403, virtualAddrSpace406, physicalAddrSpace408, nbChannels398, nbEntries414, ownedTLBs417, memorySize420, adressSize422, memoryProtection411, throughput427, notation430, description432, value435, timings425, nbSets438, blockSize440, associativity443, nbColumns448, nbBanks451, wordSize454, nbRows446, isStatic461, isNonVolatile464, organization467, organization457, isSynchronous458, level474, structure476, nbCounters478, sectorSize469, buffer471, functions485, compliant486, packages489, pins492, registers495, ports498, counterWidth480, inputClock483, implements501, operationimpls503, refsfr505, refports508, peripheralActivities511, consumption513, p_HW_Services520, r_HW_Services522, ownedHW525, endPoints527, frequency529, operations531, dissipation515, description518, dimensions535, area536, position538, grid540, nbPins543, weight546, activities533, poweredServices553, staticConsumption556, staticDissipation559, subComponents562, price549, r_Conditions551, range566, suppliedPower568, capacity570, description564, override575, register576, value578, result579, registerActions580, coolingPower573, pkgPin581, lines584, components585, protocols587, refpin591, wire594, operations595, pins590, components600, components603, wires605, components608, connections610, protocols596, connections598, datatypes616, devices618, hwcomponents619, identifierElements622, stateElements623, memorySizeFootprint626, protocols613, deleteServices631, initializeServices634, accessedElement637, createServices629, type639, entryPoints641, adressSpace643, periodElements645, priorityElements648, stackSizeElements651, routine638, enableConcurrencyServices657, resumeServices660, suspendServices663, terminateServices666, disableConcurrencyServices669, shareDataResources672, messageResources675, mutualExclusionResources678, activateServices654, heapSizeElements684, vectorElements687, maskElements689, routineConnectServices692, routineDisconnectServices695, notificationResources681, schedulers698, deadlineElements699, deadlineTypeElements702, timeSliceElements705, delayServices708, joinServices711, yieldServices714, concurrentResources719, memorySpaces721, fork724, exit727, base_Namespace730, durationElements717, devices734, closeServices735, controlServices737, openServices740, timers732, writeServices746, operations749, activities751, memories753, memoryBlockAdressElements755, memoryBlockSizeElements758, readServices743, mapServices767, unMapServices770, lockServices761, unlockServices764, waitingPolicyElements773, writeServices775, messageSizeElements778, messageQueueCapacityElements780, sendServices783, receiveServices786, readServices774, occurenceCountElements789, maskElements791, flushServices794, signalServices797, waitServices800, clearServices803, accessTokenElements806, releaseServices808, acquireServices811, base_Property814, base_Port815, base_Port816, provInterface818, reqInterface820, featuresSpec823, base_Interface825, base_Interface827, base_BehavioralFeature829, base_Trigger830, base_InvocationAction833, onFeature834, base_AnyReceiveEvent837, classifier838, base_Property840, insertion842, feature831, pop847, base_Behavior849, generator854, trace856, effect858, selection844, timedEvent860, base_NamedElement862, base_NamedElement851, pattern852, interOccT872, throughput875, respT878, utilization881, cause865, hostDemand866, hostDemandOps869, isAtomic891, blockT893, rep896, prob899, priority902, utilizationOnHost884, root887, timing889, behavior914, selfDelay917, commTxOvh920, concurRes905, host907, servDemand909, servCount911, memSize933, utilization936, throughput939, commRcvOvh922, cntxtSwT925, clockOvh928, schedPriRange931, acqRes947, resUnits949, base_Operation942, startObs943, endObs944, utility962, maxJitter965, throughput968, utilization970, relRes952, resUnits954, latency957, miss959, demand980, base_NamedElement983, context986, packetSize973, utlization975, behavior978, isSched996, workload988, platform990, resources992, base_Classifier994, timing1009, base_NamedElement1012, deadline1014, spareCap1016, isSched998, schSlack1000, end2EndT1003, end2EndD1006, spareCap1029, schSlack1032, preemptT1035, schSlack1019, base_BehavioralFeature1022, base_BehavioralFeature1024, deadline1026, numberSelfSuspensions1049, capacity1052, isPreemp1054, readyT1038, nonpreemptionBlocking1041, sharedRes1044, selfSuspensionBlocking1046, blockT1068, overlaps1071, isSched1074, isConsum1057, acquisT1060, releaseT1063, suspentions1066, ISRswitchT1087, ISRprioRange1090, noSync1093, schSlack1076, isSched1079, schSlack1081, schedUtiliz1084, resource1104, resUnits1106, extOpCount1095, behavDemand1098, behavCount1101, instance1119, host1122, utilization1109, throughput1111, poolSize1114, poolSize1117, utilization1125, throughput1128, base_NamedElement1131},
    generalizations={gen_MARTE_NFPs_NfpType_TupleType, gen_MARTE_Time_TimedValueSpecification_TimedElement, gen_MARTE_Time_TimedConstraint_NFPs_NfpConstraint, gen_MARTE_Time_TimedConstraint_Time_TimedElement, gen_MARTE_Time_ClockConstraint_NFPs_NfpConstraint, gen_MARTE_Time_ClockConstraint_Time_TimedElement, gen_MARTE_Time_TimedDurationObservation_TimedObservation, gen_MARTE_Time_TimedEvent_TimedElement, gen_MARTE_Time_TimedProcessing_TimedElement, gen_MARTE_Time_TimedObservation_TimedElement, gen_MARTE_Time_TimedInstantObservation_TimedObservation, gen_MARTE_GRM_CommunicationEndPoint_Resource, gen_MARTE_GRM_SynchronizationResource_Resource, gen_MARTE_GRM_ConcurrencyResource_Resource, gen_MARTE_GRM_Scheduler_Resource, gen_MARTE_GRM_StorageResource_Resource, gen_MARTE_GRM_ProcessingResource_Resource, gen_MARTE_GRM_ComputingResource_ProcessingResource, gen_MARTE_GRM_MutualExclusionResource_Resource, gen_MARTE_GRM_SecondaryScheduler_Scheduler, gen_MARTE_GRM_CommunicationMedia_ProcessingResource, gen_MARTE_GRM_SchedulableResource_Resource, gen_MARTE_GRM_DeviceResource_ProcessingResource, gen_MARTE_GRM_TimingResource_Resource, gen_MARTE_GRM_ClockResource_TimingResource, gen_MARTE_GRM_TimerResource_TimingResource, gen_MARTE_GRM_Release_GrService, gen_MARTE_GRM_Acquire_GrService, gen_MARTE_RSM_DefaultLink_LinkTopology, gen_MARTE_RSM_InterRepetition_LinkTopology, gen_MARTE_RSM_Distribute_Allocate, gen_MARTE_RSM_Reshape_LinkTopology, gen_MARTE_RSM_Tiler_LinkTopology, gen_MARTE_HwComputing_HwProcessor_HwComputingResource, gen_MARTE_HwComputing_HwComputingResource_HwGeneral_HwResource, gen_MARTE_HwComputing_HwComputingResource_GRM_ComputingResource, gen_MARTE_HwComputing_HwBranchPredictor_HwResource, gen_MARTE_HwComputing_HwASIC_HwComputingResource, gen_MARTE_HwComputing_HwPLD_HwComputingResource, gen_MARTE_HwComputing_HwISA_HwResource, gen_MARTE_HwComputing_HwMCU_HwComputingResource, gen_MARTE_HwCommunication_HwMedia_GRM_CommunicationMedia, gen_MARTE_HwCommunication_HwMedia_HwCommunication_HwCommunicationResource, gen_MARTE_HwCommunication_HwBus_HwMedia, gen_MARTE_HwCommunication_HwCommunicationResource_HwResource, gen_MARTE_HwCommunication_HwArbiter_HwCommunicationResource, gen_MARTE_HwCommunication_HwBridge_HwMedia, gen_MARTE_HwCommunication_HwEndPoint_HwCommunication_HwCommunicationResource, gen_MARTE_HwCommunication_HwEndPoint_GRM_CommunicationEndPoint, gen_MARTE_HwCommunication_HwPort_HwEndPoint, gen_MARTE_HwStorageManager_HwStorageManager_HwGeneral_HwResource, gen_MARTE_HwStorageManager_HwStorageManager_GRM_StorageResource, gen_MARTE_HwStorageManager_HwDMA_HwStorageManager_HwStorageManager, gen_MARTE_HwStorageManager_HwDMA_HwCommunication_HwArbiter, gen_MARTE_HwCommunication_HwConnection_HwMedia, gen_MARTE_HwStorageManager_HwMMU_HwStorageManager, gen_MARTE_HwMemory_HwMemory_HwGeneral_HwResource, gen_MARTE_HwMemory_HwMemory_GRM_StorageResource, gen_MARTE_HwMemory_HwRAM_HwMemory, gen_MARTE_HwMemory_HwROM_HwMemory, gen_MARTE_HwMemory_HwDrive_HwMemory, gen_MARTE_HwTiming_HwTimingResource_HwGeneral_HwResource, gen_MARTE_HwTiming_HwTimingResource_GRM_TimingResource, gen_MARTE_HwTiming_HwClock_HwTimingResource, gen_MARTE_HwTiming_HwTimer_HwTimingResource, gen_MARTE_HwMemory_HwCache_HwMemory, gen_MARTE_HwDevice_HwDevice_HwGeneral_HwResource, gen_MARTE_HwDevice_HwDevice_GRM_DeviceResource, gen_MARTE_HwDevice_HwI_O_HwDevice, gen_MARTE_HwGeneral_HwResourceService_GrService, gen_MARTE_HwDevice_HwSupport_HwDevice, gen_MARTE_HwDevice_HWActuator_HwI_O, gen_MARTE_HwDevice_HWSensor_HwI_O, gen_MARTE_HwDevice_HwPeripheral_HwDevice, gen_MARTE_HwGeneral_HwResource_Resource, gen_MARTE_HwLayout_HwComponent_HwResource, gen_MARTE_HwPower_HwPowerSupply_HwComponent, gen_MARTE_HwPeripheral_OperationImpl_Operation, gen_MARTE_HwPeripheral_RegisterAction_Action, gen_MARTE_HwPeripheral_WriteRegisterAction_RegisterAction, gen_MARTE_HwPeripheral_ReadRegisterAction_RegisterAction, gen_MARTE_HwPeripheral_PeripheralActivity_Activity, gen_MARTE_HwPower_HwCoolingSupply_HwComponent, gen_MARTE_HwIO_HwLine_HwMedia, gen_MARTE_HwRegister_HwRegister_HwMemory, gen_MARTE_HwDeviceFunction_HwDeviceFunction_Operation, gen_MARTE_HwIO_HwPin_HwEndPoint, gen_MARTE_HwPackage_HwPackagePin_HwEndPoint, gen_MARTE_HwPackage_HwWire_HwMedia, gen_MARTE_SW_ResourceCore_SwResource_Resource, gen_MARTE_SW_ResourceCore_SwAccessService_GrService, gen_MARTE_SW_Concurrency_SwConcurrentResource_SwResource, gen_MARTE_SW_Concurrency_EntryPoint_Allocate, gen_MARTE_SW_Concurrency_InterruptResource_SwConcurrentResource, gen_MARTE_SW_Concurrency_SwSchedulableResource_SW_Concurrency_SwConcurrentResource, gen_MARTE_SW_Concurrency_SwSchedulableResource_GRM_SchedulableResource, gen_MARTE_SW_Concurrency_MemoryPartition_SwResource, gen_MARTE_SW_Concurrency_Alarm_InterruptResource, gen_MARTE_SW_Concurrency_SwTimerResource_TimerResource, gen_MARTE_SW_Brokering_DeviceBroker_SwResource, gen_MARTE_SW_Brokering_MemoryBroker_SwResource, gen_MARTE_SW_Interaction_SwInteractionResource_SwResource, gen_MARTE_SW_Interaction_SwCommunicationResource_SW_Interaction_SwInteractionResource, gen_MARTE_SW_Interaction_SwCommunicationResource_GRM_CommunicationMedia, gen_MARTE_SW_Interaction_SwSynchronizationResource_SW_Interaction_SwInteractionResource, gen_MARTE_SW_Interaction_SwSynchronizationResource_GRM_SynchronizationResource, gen_MARTE_SW_Interaction_MessageComResource_SwCommunicationResource, gen_MARTE_SW_Interaction_NotificationResource_SwSynchronizationResource, gen_MARTE_SW_Interaction_SharedDataComResource_SwCommunicationResource, gen_MARTE_SW_Interaction_SwMutualExclusionResource_SW_Interaction_SwSynchronizationResource, gen_MARTE_SW_Interaction_SwMutualExclusionResource_GRM_MutualExclusionResource, gen_MARTE_GQAM_GaScenario_GRM_ResourceUsage, gen_MARTE_GQAM_GaScenario_Time_TimedProcessing, gen_MARTE_GQAM_GaStep_GaScenario, gen_MARTE_GQAM_GaExecHost_GRM_Scheduler, gen_MARTE_GQAM_GaExecHost_GRM_ComputingResource, gen_MARTE_GQAM_GaRequestedService_GaStep, gen_MARTE_GQAM_GaCommStep_GaStep, gen_MARTE_GQAM_GaAcqStep_GaStep, gen_MARTE_GQAM_GaRelStep_GaStep, gen_MARTE_GQAM_GaTimedObs_NfpConstraint, gen_MARTE_GQAM_GaCommHost_GRM_CommunicationMedia, gen_MARTE_GQAM_GaCommHost_GRM_Scheduler, gen_MARTE_GQAM_GaLatencyObs_GaTimedObs, gen_MARTE_GQAM_GaAnalysisContext_CoreElements_Configuration, gen_MARTE_GQAM_GaAnalysisContext_Variables_ExpressionContext, gen_MARTE_GQAM_GaCommChannel_SchedulableResource, gen_MARTE_SAM_SaAnalysisContext_GaAnalysisContext, gen_MARTE_SAM_SaCommStep_GaCommStep, gen_MARTE_SAM_SaStep_GaStep, gen_MARTE_SAM_SaSharedResource_MutualExclusionResource, gen_MARTE_SAM_SaCommHost_GaCommHost, gen_MARTE_SAM_SaSchedObs_GaTimedObs, gen_MARTE_PAM_PaStep_GaStep, gen_MARTE_SAM_SaExecHost_GaExecHost, gen_MARTE_PAM_PaCommStep_PAM_PaStep, gen_MARTE_PAM_PaCommStep_GQAM_GaCommStep, gen_MARTE_PAM_PaResPassStep_GaStep, gen_MARTE_PAM_PaLogicalResource_Resource, gen_MARTE_PAM_PaRequestedStep_PAM_PaStep, gen_MARTE_PAM_PaRequestedStep_GQAM_GaRequestedService},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)