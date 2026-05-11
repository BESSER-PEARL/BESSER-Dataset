import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    GQAM::GaCommStep,
    PAM::PaStep,
    MARTE::PAM::PaCommStep,
    MARTE::PAM::PaRunTInstance,
    GaExecHost,
    MARTE::SAM::SaExecHost,
    MutualExclusionResource,
    MARTE::SAM::SaSharedResource,
    GaCommHost,
    MARTE::SAM::SaCommHost,
    SAM::MARTE::BehavioralFeature,
    SAM::SaSharedResource,
    GaAnalysisContext,
    MARTE::SAM::SaAnalysisContext,
    GQAM::MARTE::Classifier,
    GaCommStep,
    MARTE::SAM::SaCommStep,
    SAM::MARTE::NamedElement,
    MARTE::SAM::SaEndtoEndFlow,
    SchedulableResource,
    MARTE::GQAM::GaCommChannel,
    MARTE::GQAM::GaResourcesPlatform,
    GQAM::GaResourcesPlatform,
    GQAM::GaWorkloadBehavior,
    Variables::ExpressionContext,
    CoreElements::Configuration,
    MARTE::GQAM::GaAnalysisContext,
    MARTE::GQAM::GaWorkloadBehavior,
    GaTimedObs,
    MARTE::SAM::SaSchedObs,
    MARTE::GQAM::GaLatencyObs,
    GQAM::MARTE::TimeObservation,
    NfpConstraint,
    MARTE::GQAM::GaTimedObs,
    GQAM::MARTE::Operation,
    GaStep,
    MARTE::SAM::SaStep,
    MARTE::GQAM::GaCommStep,
    MARTE::GQAM::GaRelStep,
    MARTE::GQAM::GaAcqStep,
    MARTE::PAM::PaStep,
    MARTE::GQAM::GaRequestedService,
    IntegerInterval,
    GaScenario,
    MARTE::GQAM::GaStep,
    GQAM::GaTimedObs,
    GQAM::GaStep,
    GQAM::GaRequestedService,
    MARTE::PAM::PaRequestedStep,
    GQAM::GaExecHost,
    GQAM::GaWorkloadEvent,
    Time::TimedProcessing,
    MARTE::GQAM::GaWorkloadGenerator,
    GCM::MARTE::Behavior,
    GQAM::MARTE::TimeEvent,
    GQAM::GaScenario,
    GQAM::GaEventTrace,
    GQAM::GaWorkloadGenerator,
    MARTE::GQAM::GaWorkloadEvent,
    GQAM::MARTE::NamedElement,
    MARTE::GQAM::GaEventTrace,
    GQAM::MARTE::Behavior,
    MARTE::GCM::FlowSpecification,
    MARTE::GCM::ClientServerSpecification,
    MARTE::GCM::DataPool,
    GCM::MARTE::Classifier,
    GCM::MARTE::AnyReceiveEvent,
    MARTE::GCM::DataEvent,
    GCM::MARTE::InvocationAction,
    MARTE::GCM::GCMInvocationAction,
    GCM::MARTE::Feature,
    GCM::MARTE::Trigger,
    MARTE::GCM::GCMTrigger,
    GCM::MARTE::BehavioralFeature,
    MARTE::GCM::ClientServerFeature,
    GCM::MARTE::Property,
    MARTE::GCM::FlowProperty,
    GCM::ClientServerSpecification,
    GCM::MARTE::Interface,
    MARTE::GCM::ClientServerPort,
    GCM::MARTE::Port,
    MARTE::GCM::FlowPort,
    SwSynchronizationResource,
    MARTE::SW::Interaction::NotificationResource,
    SW::Interaction::SwSynchronizationResource,
    SW::Interaction::MARTE::BehavioralFeature,
    SwCommunicationResource,
    MARTE::SW::Interaction::MessageComResource,
    MARTE::SW::Interaction::SharedDataComResource,
    GRM::SynchronizationResource,
    SW::Interaction::SwInteractionResource,
    MARTE::SW::Interaction::SwSynchronizationResource,
    SW::Interaction::MARTE::TypedElement,
    SW::Brokering::MARTE::Activity,
    SW::Brokering::MARTE::Operation,
    SW::Brokering::MARTE::BehavioralFeature,
    SW::Brokering::MARTE::TypedElement,
    InterruptResource,
    MARTE::SW::Concurrency::Alarm,
    SW::Concurrency::MARTE::Namespace,
    TimerResource,
    MARTE::SW::Concurrency::SwTimerResource,
    SW::Concurrency::MARTE::NamedElement,
    SW::Concurrency::SwConcurrentResource,
    SwConcurrentResource,
    MARTE::SW::Concurrency::InterruptResource,
    SW::Concurrency::MARTE::TypedElement,
    SW::Concurrency::MARTE::Element,
    SwResource,
    MARTE::SW::Interaction::SwInteractionResource,
    MARTE::SW::Brokering::MemoryBroker,
    MARTE::SW::Concurrency::MemoryPartition,
    MARTE::SW::Brokering::DeviceBroker,
    MARTE::SW::Concurrency::SwConcurrentResource,
    SW::ResourceCore::MARTE::BehavioralFeature,
    SW::ResourceCore::MARTE::TypedElement,
    SW::Concurrency::MARTE::BehavioralFeature,
    SW::Brokering::DeviceBroker,
    MARTE::HwDiagram::SRMDiagram,
    SW::ResourceCore::MARTE::Property,
    HwDiagram::MARTE::DataType,
    MARTE::HwDiagram::HwCircuitDiagram,
    HwCommunication::HwConnection,
    MARTE::HwDiagram::HwHRMDiagram,
    HwPackage::HwWire,
    PAM::MARTE::NamedElement,
    MARTE::PAM::PaResPassStep,
    MARTE::HwPackage::HwPackage,
    MARTE::HwDatasheet::HwDatasheet,
    MARTE::HwDiagram::HwBlockDiagram,
    HwProtocol::MARTE::Operation,
    MARTE::HwProtocol::HwProtocol,
    HwPeripheral::RegisterAction,
    Activity,
    MARTE::HwPeripheral::PeripheralActivity,
    HwPeripheral::MARTE::OutputPin,
    HwPeripheral::MARTE::InputPin,
    RegisterAction,
    MARTE::HwPeripheral::ReadRegisterAction,
    MARTE::HwPeripheral::WriteRegisterAction,
    Action,
    MARTE::HwPeripheral::RegisterAction,
    HwPeripheral::MARTE::Operation,
    Operation,
    MARTE::HwDeviceFunction::HwDeviceFunction,
    MARTE::HwPeripheral::OperationImpl,
    HwIO::HwLine,
    HwPackage::HwPackagePin,
    HwComponent,
    MARTE::HwPower::HwPowerSupply,
    MARTE::HwPower::HwCoolingSupply,
    MARTE::HwLayout::Env::Condition,
    HwLayout::HwComponent,
    HwLayout::Env::Condition,
    NFP::Price,
    Realnterval,
    NFP::Length,
    HwGeneral::MARTE::Activity,
    HwGeneral::MARTE::Operation,
    NFP::Frequency,
    HwCommunication::HwEndPoint,
    HwGeneral::HwResourceService,
    NFP::NaturalInterval,
    NFP::Area,
    HwPeripheral::PeripheralActivity,
    HwPeripheral::OperationImpl,
    HwI::O,
    MARTE::HwDevice::HWSensor,
    MARTE::HwDevice::HWActuator,
    HwDevice,
    MARTE::HwDevice::HwPeripheral,
    MARTE::HwDevice::HwSupport,
    MARTE::HwDevice::HwI::O,
    HwTimingResource,
    MARTE::HwTiming::HwTimer,
    MARTE::HwTiming::HwClock,
    GRM::TimingResource,
    HwMemory::CacheStructure,
    HwDeviceFunction::HwDeviceFunction,
    GRM::DeviceResource,
    HwTiming::HwClock,
    HwMemory::MemoryOrganization,
    HwMemory,
    MARTE::HwMemory::HwDrive,
    MARTE::HwMemory::HwCache,
    MARTE::HwRegister::HwRegister,
    MARTE::HwMemory::HwRAM,
    MARTE::HwMemory::MemoryOrganization,
    MARTE::HwMemory::CacheStructure,
    MARTE::HwMemory::HwROM,
    MARTE::HwMemory::Timing,
    HwMemory::Timing,
    HwStorageManager::HwStorageManager,
    HwMemory::HwMemory,
    GRM::StorageResource,
    HwProtocol::HwProtocol,
    HwEndPoint,
    MARTE::HwIO::HwPin,
    MARTE::HwPackage::HwPackagePin,
    MARTE::HwCommunication::HwPort,
    GRM::CommunicationEndPoint,
    NFP::Boolean,
    HwStorageManager,
    MARTE::HwStorageManager::HwMMU,
    HwCommunication::HwCommunicationResource,
    MARTE::HwCommunication::HwEndPoint,
    GRM::CommunicationMedia,
    MARTE::SW::Interaction::SwCommunicationResource,
    MARTE::HwCommunication::HwMedia,
    HwCommunication::HwMedia,
    HwCommunicationResource,
    MARTE::HwCommunication::HwArbiter,
    HwCommunication::HwPort,
    HwIO::HwPin,
    HwPackage::HwPackage,
    HwRegister::HwRegister,
    HwDevice::HwPeripheral,
    HwComputing::HwProcessor,
    HwComputing::HwComputingResource,
    HwMedia,
    MARTE::HwCommunication::HwConnection,
    MARTE::HwPackage::HwWire,
    MARTE::HwIO::HwLine,
    MARTE::HwCommunication::HwBridge,
    MARTE::HwCommunication::HwBus,
    HwCommunication::HwArbiter,
    MARTE::HwStorageManager::HwDMA,
    HwComputing::PLD::Organization,
    NFP::String,
    HwResource,
    MARTE::HwCommunication::HwCommunicationResource,
    MARTE::HwComputing::HwBranchPredictor,
    MARTE::HwLayout::HwComponent,
    MARTE::HwComputing::HwISA,
    NFP::FrequencyInterval,
    HwGeneral::HwResource,
    MARTE::HwStorageManager::HwStorageManager,
    MARTE::HwMemory::HwMemory,
    MARTE::HwTiming::HwTimingResource,
    MARTE::HwDevice::HwDevice,
    HwStorageManager::HwMMU,
    HwMemory::HwCache,
    HwComputing::HwBranchPredictor,
    HwMemory::HwRAM,
    HwComputingResource,
    MARTE::HwComputing::HwASIC,
    MARTE::HwComputing::HwMCU,
    MARTE::HwComputing::HwPLD,
    MARTE::HwComputing::HwProcessor,
    NFP::Natural,
    MARTE::HwComputing::PLD::Organization,
    HwComputing::HwISA,
    MARTE::HLAM::RtService,
    MARTE::HLAM::RtAction,
    NFP::DateTime,
    HLAM::MARTE::Comment,
    NFP::Percentage,
    HLAM::RtSpecification,
    HLAM::MARTE::InvocationAction,
    HLAM::MARTE::Port,
    HLAM::MARTE::Signal,
    HLAM::MARTE::Message,
    HLAM::MARTE::BehavioralFeature,
    MARTE::HLAM::RtFeature,
    MARTE::HLAM::PpUnit,
    Time::TimedInstantObservation,
    ArrivalPattern,
    UtilityType,
    MARTE::HLAM::RtSpecification,
    HLAM::MARTE::Operation,
    HLAM::MARTE::Behavior,
    MARTE::HLAM::RtUnit,
    MARTE::DataTypes::TupleType,
    MARTE::DataTypes::ChoiceType,
    HLAM::MARTE::BehavioredClassifier,
    DataTypes::MARTE::Property,
    MARTE::DataTypes::BoundedSubtype,
    Variables::MARTE::NamedElement,
    MARTE::Variables::ExpressionContext,
    Variables::MARTE::Property,
    MARTE::Variables::Var,
    RSM::MARTE::MultiplicityElement,
    MARTE::RSM::Shaped,
    RSM::MARTE::ConnectorEnd,
    MARTE::DataTypes::CollectionType,
    MARTE::DataTypes::IntervalType,
    DataTypes::MARTE::DataType,
    TilerSpecification,
    ShapeSpecification,
    Allocate,
    MARTE::SW::Concurrency::EntryPoint,
    MARTE::CoreElements::ModeTransition,
    NFPs::MARTE::Enumeration,
    NFPs::Dimension,
    MARTE::NFPs::Dimension,
    TupleType,
    MARTE::NFPs::NfpType,
    CoreElements::Mode,
    NFPs::MARTE::Constraint,
    MARTE::NFPs::NfpConstraint,
    NFPs::MARTE::EnumerationLiteral,
    CoreElements::MARTE::Package,
    CoreElements::MARTE::StructuredClassifier,
    MARTE::CoreElements::Configuration,
    CoreElements::MARTE::StateMachine,
    MARTE::CoreElements::ModeBehavior,
    MARTE::NFPs::Nfp,
    NFPs::Unit,
    MARTE::NFPs::Unit,
    NFPs::MARTE::Property,
    MARTE::RSM::Distribute,
    IntegerVector,
    LinkTopology,
    MARTE::RSM::Reshape,
    MARTE::RSM::InterRepetition,
    MARTE::RSM::DefaultLink,
    RSM::MARTE::Connector,
    MARTE::RSM::LinkTopology,
    IntegerMatrix,
    MARTE::RSM::Tiler,
    NFP::Energy,
    NFP::Power,
    NFP::DataSize,
    MARTE::GRM::ResourceUsage,
    GrService,
    MARTE::HwGeneral::HwResourceService,
    MARTE::SW::ResourceCore::SwAccessService,
    MARTE::GRM::Acquire,
    MARTE::GRM::Release,
    GRM::MARTE::CollaborationUse,
    GRM::MARTE::Collaboration,
    GRM::MARTE::Behavior,
    GRM::MARTE::BehavioralFeature,
    GRM::MARTE::ExecutionSpecification,
    GRM::Resource,
    MARTE::GRM::GrService,
    GRM::ResourceUsage,
    MARTE::GQAM::GaScenario,
    GRM::MARTE::NamedElement,
    NFP::DataTxRate,
    NFP::Duration,
    GRM::MARTE::Connector,
    Scheduler,
    MARTE::GRM::SecondaryScheduler,
    GRM::SecondaryScheduler,
    SchedParameters,
    TimingResource,
    MARTE::GRM::TimerResource,
    MARTE::GRM::ClockResource,
    GRM::Scheduler,
    MARTE::GQAM::GaCommHost,
    NFP::Real,
    GRM::SchedulableResource,
    MARTE::SW::Concurrency::SwSchedulableResource,
    GRM::MutualExclusionResource,
    MARTE::SW::Interaction::SwMutualExclusionResource,
    GRM::ComputingResource,
    MARTE::GQAM::GaExecHost,
    MARTE::HwComputing::HwComputingResource,
    GRM::ProcessingResource,
    GRM::MARTE::OpaqueExpression,
    ProcessingResource,
    MARTE::GRM::CommunicationMedia,
    MARTE::GRM::DeviceResource,
    MARTE::GRM::ComputingResource,
    GRM::MARTE::InstanceSpecification,
    GRM::MARTE::Property,
    NFP::Integer,
    MARTE::GRM::Resource,
    Time::MARTE::Event,
    Time::MARTE::Message,
    Time::MARTE::Behavior,
    Time::MARTE::Action,
    Time::MARTE::TimeEvent,
    Resource,
    MARTE::GRM::Scheduler,
    MARTE::PAM::PaLogicalResource,
    MARTE::GRM::SynchronizationResource,
    MARTE::GRM::MutualExclusionResource,
    MARTE::GRM::CommunicationEndPoint,
    MARTE::HwGeneral::HwResource,
    MARTE::GRM::SchedulableResource,
    MARTE::GRM::ConcurrencyResource,
    MARTE::SW::ResourceCore::SwResource,
    MARTE::GRM::TimingResource,
    MARTE::GRM::ProcessingResource,
    MARTE::GRM::StorageResource,
    GRM::MARTE::ConnectableElement,
    GRM::MARTE::Lifeline,
    GRM::MARTE::Classifier,
    TimedObservation,
    MARTE::Time::TimedInstantObservation,
    Time::TimedElement,
    Time::MARTE::ValueSpecification,
    TimedElement,
    MARTE::Time::TimedObservation,
    MARTE::Time::TimedProcessing,
    MARTE::Time::TimedValueSpecification,
    Time::Clock,
    MARTE::Time::TimedElement,
    Time::MARTE::Class,
    MARTE::Time::TimedEvent,
    Time::MARTE::DurationObservation,
    MARTE::Time::TimedDurationObservation,
    Time::MARTE::TimeObservation,
    Time::MARTE::Enumeration,
    MARTE::Time::ClockType,
    Time::MARTE::Property,
    Time::ClockType,
    Time::MARTE::InstanceSpecification,
    MARTE::Time::Clock,
    Time::MARTE::Namespace,
    MARTE::Time::TimedDomain,
    Alloc::MARTE::Abstraction,
    MARTE::Alloc::Allocate,
    Time::MARTE::Operation,
    MARTE::Alloc::Assign,
    NFPs::NfpConstraint,
    MARTE::Time::ClockConstraint,
    MARTE::Time::TimedConstraint,
    Alloc::MARTE::Dependency,
    MARTE::Alloc::NfpRefine,
    Alloc::MARTE::ActivityPartition,
    MARTE::Alloc::AllocateActivityGroup,
    Alloc::Allocated,
    Alloc::MARTE::NamedElement,
    MARTE::Alloc::Allocated,
    CoreElements::MARTE::State,
    MARTE::CoreElements::Mode,
    Alloc::MARTE::Comment,
    Alloc::MARTE::Element,
    CoreElements::MARTE::Transition,
    DataPoolOrderingKind,
    LaxityKind,
    ConstraintKind,
    AllocationNature,
    PoolMgtPolicyKind,
    ComponentState,
    SynchronizationKind,
    AllocationEndKind,
    ConcurrencyKind,
    OptimallityCriterionKind,
    PLD_Technology,
    ROM_Type,
    NotificationResourceKind,
    ISA_Type,
    Repl_Policy,
    ClientServerKind,
    ConcurrentAccessProtocolKind,
    InterruptKind,
    AssignmentNature,
    NotificationKind,
    AccessPolicyKind,
    WritePolicy,
    ExecutionKind,
    AssignmentKind,
    FlowDirectionKind,
    ConditionType,
    PortSpecificationKind,
    VariableDirectionKind,
    MutualExclusionResourceKind,
    MessageResourceKind,
    AllocationKind,
    QueuePolicyKind,
    ComponentKind,
    CacheType,
    PLD_Class,
    CallConcurrencyKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gqam::gacommstep_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaCommStep)


def test_gqam::gacommstep_constructor_exists():
    assert callable(GQAM::GaCommStep.__init__)


def test_gqam::gacommstep_constructor_args():
    sig = inspect.signature(GQAM::GaCommStep.__init__)
    params = list(sig.parameters.keys())



def test_pam::pastep_is_not_abstract():
    assert not inspect.isabstract(PAM::PaStep)


def test_pam::pastep_constructor_exists():
    assert callable(PAM::PaStep.__init__)


def test_pam::pastep_constructor_args():
    sig = inspect.signature(PAM::PaStep.__init__)
    params = list(sig.parameters.keys())



def test_marte::pam::pacommstep_is_not_abstract():
    assert not inspect.isabstract(MARTE::PAM::PaCommStep)


def test_marte::pam::pacommstep_constructor_exists():
    assert callable(MARTE::PAM::PaCommStep.__init__)


def test_marte::pam::pacommstep_constructor_args():
    sig = inspect.signature(MARTE::PAM::PaCommStep.__init__)
    params = list(sig.parameters.keys())



def test_marte::pam::paruntinstance_is_not_abstract():
    assert not inspect.isabstract(MARTE::PAM::PaRunTInstance)


def test_marte::pam::paruntinstance_constructor_exists():
    assert callable(MARTE::PAM::PaRunTInstance.__init__)


def test_marte::pam::paruntinstance_constructor_args():
    sig = inspect.signature(MARTE::PAM::PaRunTInstance.__init__)
    params = list(sig.parameters.keys())
    assert "unbddPool" in params, "Missing parameter 'unbddPool'"

def test_marte::pam::paruntinstance_has_unbddPool():
    assert hasattr(MARTE::PAM::PaRunTInstance, "unbddPool")
    descriptor = None
    for klass in MARTE::PAM::PaRunTInstance.__mro__:
        if "unbddPool" in klass.__dict__:
            descriptor = klass.__dict__["unbddPool"]
            break
    assert isinstance(descriptor, property)



def test_gaexechost_is_not_abstract():
    assert not inspect.isabstract(GaExecHost)


def test_gaexechost_constructor_exists():
    assert callable(GaExecHost.__init__)


def test_gaexechost_constructor_args():
    sig = inspect.signature(GaExecHost.__init__)
    params = list(sig.parameters.keys())



def test_marte::sam::saexechost_is_not_abstract():
    assert not inspect.isabstract(MARTE::SAM::SaExecHost)


def test_marte::sam::saexechost_constructor_exists():
    assert callable(MARTE::SAM::SaExecHost.__init__)


def test_marte::sam::saexechost_constructor_args():
    sig = inspect.signature(MARTE::SAM::SaExecHost.__init__)
    params = list(sig.parameters.keys())



def test_mutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(MutualExclusionResource)


def test_mutualexclusionresource_constructor_exists():
    assert callable(MutualExclusionResource.__init__)


def test_mutualexclusionresource_constructor_args():
    sig = inspect.signature(MutualExclusionResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sam::sasharedresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SAM::SaSharedResource)


def test_marte::sam::sasharedresource_constructor_exists():
    assert callable(MARTE::SAM::SaSharedResource.__init__)


def test_marte::sam::sasharedresource_constructor_args():
    sig = inspect.signature(MARTE::SAM::SaSharedResource.__init__)
    params = list(sig.parameters.keys())



def test_gacommhost_is_not_abstract():
    assert not inspect.isabstract(GaCommHost)


def test_gacommhost_constructor_exists():
    assert callable(GaCommHost.__init__)


def test_gacommhost_constructor_args():
    sig = inspect.signature(GaCommHost.__init__)
    params = list(sig.parameters.keys())



def test_marte::sam::sacommhost_is_not_abstract():
    assert not inspect.isabstract(MARTE::SAM::SaCommHost)


def test_marte::sam::sacommhost_constructor_exists():
    assert callable(MARTE::SAM::SaCommHost.__init__)


def test_marte::sam::sacommhost_constructor_args():
    sig = inspect.signature(MARTE::SAM::SaCommHost.__init__)
    params = list(sig.parameters.keys())



def test_sam::marte::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SAM::MARTE::BehavioralFeature)


def test_sam::marte::behavioralfeature_constructor_exists():
    assert callable(SAM::MARTE::BehavioralFeature.__init__)


def test_sam::marte::behavioralfeature_constructor_args():
    sig = inspect.signature(SAM::MARTE::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_sam::sasharedresource_is_not_abstract():
    assert not inspect.isabstract(SAM::SaSharedResource)


def test_sam::sasharedresource_constructor_exists():
    assert callable(SAM::SaSharedResource.__init__)


def test_sam::sasharedresource_constructor_args():
    sig = inspect.signature(SAM::SaSharedResource.__init__)
    params = list(sig.parameters.keys())



def test_gaanalysiscontext_is_not_abstract():
    assert not inspect.isabstract(GaAnalysisContext)


def test_gaanalysiscontext_constructor_exists():
    assert callable(GaAnalysisContext.__init__)


def test_gaanalysiscontext_constructor_args():
    sig = inspect.signature(GaAnalysisContext.__init__)
    params = list(sig.parameters.keys())



def test_marte::sam::saanalysiscontext_is_not_abstract():
    assert not inspect.isabstract(MARTE::SAM::SaAnalysisContext)


def test_marte::sam::saanalysiscontext_constructor_exists():
    assert callable(MARTE::SAM::SaAnalysisContext.__init__)


def test_marte::sam::saanalysiscontext_constructor_args():
    sig = inspect.signature(MARTE::SAM::SaAnalysisContext.__init__)
    params = list(sig.parameters.keys())
    assert "optCriterion" in params, "Missing parameter 'optCriterion'"

def test_marte::sam::saanalysiscontext_has_optCriterion():
    assert hasattr(MARTE::SAM::SaAnalysisContext, "optCriterion")
    descriptor = None
    for klass in MARTE::SAM::SaAnalysisContext.__mro__:
        if "optCriterion" in klass.__dict__:
            descriptor = klass.__dict__["optCriterion"]
            break
    assert isinstance(descriptor, property)



def test_gqam::marte::classifier_is_not_abstract():
    assert not inspect.isabstract(GQAM::MARTE::Classifier)


def test_gqam::marte::classifier_constructor_exists():
    assert callable(GQAM::MARTE::Classifier.__init__)


def test_gqam::marte::classifier_constructor_args():
    sig = inspect.signature(GQAM::MARTE::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_gacommstep_is_not_abstract():
    assert not inspect.isabstract(GaCommStep)


def test_gacommstep_constructor_exists():
    assert callable(GaCommStep.__init__)


def test_gacommstep_constructor_args():
    sig = inspect.signature(GaCommStep.__init__)
    params = list(sig.parameters.keys())



def test_marte::sam::sacommstep_is_not_abstract():
    assert not inspect.isabstract(MARTE::SAM::SaCommStep)


def test_marte::sam::sacommstep_constructor_exists():
    assert callable(MARTE::SAM::SaCommStep.__init__)


def test_marte::sam::sacommstep_constructor_args():
    sig = inspect.signature(MARTE::SAM::SaCommStep.__init__)
    params = list(sig.parameters.keys())



def test_sam::marte::namedelement_is_not_abstract():
    assert not inspect.isabstract(SAM::MARTE::NamedElement)


def test_sam::marte::namedelement_constructor_exists():
    assert callable(SAM::MARTE::NamedElement.__init__)


def test_sam::marte::namedelement_constructor_args():
    sig = inspect.signature(SAM::MARTE::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte::sam::saendtoendflow_is_not_abstract():
    assert not inspect.isabstract(MARTE::SAM::SaEndtoEndFlow)


def test_marte::sam::saendtoendflow_constructor_exists():
    assert callable(MARTE::SAM::SaEndtoEndFlow.__init__)


def test_marte::sam::saendtoendflow_constructor_args():
    sig = inspect.signature(MARTE::SAM::SaEndtoEndFlow.__init__)
    params = list(sig.parameters.keys())



def test_schedulableresource_is_not_abstract():
    assert not inspect.isabstract(SchedulableResource)


def test_schedulableresource_constructor_exists():
    assert callable(SchedulableResource.__init__)


def test_schedulableresource_constructor_args():
    sig = inspect.signature(SchedulableResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gacommchannel_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaCommChannel)


def test_marte::gqam::gacommchannel_constructor_exists():
    assert callable(MARTE::GQAM::GaCommChannel.__init__)


def test_marte::gqam::gacommchannel_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaCommChannel.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::garesourcesplatform_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaResourcesPlatform)


def test_marte::gqam::garesourcesplatform_constructor_exists():
    assert callable(MARTE::GQAM::GaResourcesPlatform.__init__)


def test_marte::gqam::garesourcesplatform_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaResourcesPlatform.__init__)
    params = list(sig.parameters.keys())



def test_gqam::garesourcesplatform_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaResourcesPlatform)


def test_gqam::garesourcesplatform_constructor_exists():
    assert callable(GQAM::GaResourcesPlatform.__init__)


def test_gqam::garesourcesplatform_constructor_args():
    sig = inspect.signature(GQAM::GaResourcesPlatform.__init__)
    params = list(sig.parameters.keys())



def test_gqam::gaworkloadbehavior_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaWorkloadBehavior)


def test_gqam::gaworkloadbehavior_constructor_exists():
    assert callable(GQAM::GaWorkloadBehavior.__init__)


def test_gqam::gaworkloadbehavior_constructor_args():
    sig = inspect.signature(GQAM::GaWorkloadBehavior.__init__)
    params = list(sig.parameters.keys())



def test_variables::expressioncontext_is_not_abstract():
    assert not inspect.isabstract(Variables::ExpressionContext)


def test_variables::expressioncontext_constructor_exists():
    assert callable(Variables::ExpressionContext.__init__)


def test_variables::expressioncontext_constructor_args():
    sig = inspect.signature(Variables::ExpressionContext.__init__)
    params = list(sig.parameters.keys())



def test_coreelements::configuration_is_not_abstract():
    assert not inspect.isabstract(CoreElements::Configuration)


def test_coreelements::configuration_constructor_exists():
    assert callable(CoreElements::Configuration.__init__)


def test_coreelements::configuration_constructor_args():
    sig = inspect.signature(CoreElements::Configuration.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gaanalysiscontext_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaAnalysisContext)


def test_marte::gqam::gaanalysiscontext_constructor_exists():
    assert callable(MARTE::GQAM::GaAnalysisContext.__init__)


def test_marte::gqam::gaanalysiscontext_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaAnalysisContext.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gaworkloadbehavior_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaWorkloadBehavior)


def test_marte::gqam::gaworkloadbehavior_constructor_exists():
    assert callable(MARTE::GQAM::GaWorkloadBehavior.__init__)


def test_marte::gqam::gaworkloadbehavior_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaWorkloadBehavior.__init__)
    params = list(sig.parameters.keys())



def test_gatimedobs_is_not_abstract():
    assert not inspect.isabstract(GaTimedObs)


def test_gatimedobs_constructor_exists():
    assert callable(GaTimedObs.__init__)


def test_gatimedobs_constructor_args():
    sig = inspect.signature(GaTimedObs.__init__)
    params = list(sig.parameters.keys())



def test_marte::sam::saschedobs_is_not_abstract():
    assert not inspect.isabstract(MARTE::SAM::SaSchedObs)


def test_marte::sam::saschedobs_constructor_exists():
    assert callable(MARTE::SAM::SaSchedObs.__init__)


def test_marte::sam::saschedobs_constructor_args():
    sig = inspect.signature(MARTE::SAM::SaSchedObs.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::galatencyobs_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaLatencyObs)


def test_marte::gqam::galatencyobs_constructor_exists():
    assert callable(MARTE::GQAM::GaLatencyObs.__init__)


def test_marte::gqam::galatencyobs_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaLatencyObs.__init__)
    params = list(sig.parameters.keys())



def test_gqam::marte::timeobservation_is_not_abstract():
    assert not inspect.isabstract(GQAM::MARTE::TimeObservation)


def test_gqam::marte::timeobservation_constructor_exists():
    assert callable(GQAM::MARTE::TimeObservation.__init__)


def test_gqam::marte::timeobservation_constructor_args():
    sig = inspect.signature(GQAM::MARTE::TimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_nfpconstraint_is_not_abstract():
    assert not inspect.isabstract(NfpConstraint)


def test_nfpconstraint_constructor_exists():
    assert callable(NfpConstraint.__init__)


def test_nfpconstraint_constructor_args():
    sig = inspect.signature(NfpConstraint.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gatimedobs_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaTimedObs)


def test_marte::gqam::gatimedobs_constructor_exists():
    assert callable(MARTE::GQAM::GaTimedObs.__init__)


def test_marte::gqam::gatimedobs_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaTimedObs.__init__)
    params = list(sig.parameters.keys())
    assert "laxity" in params, "Missing parameter 'laxity'"

def test_marte::gqam::gatimedobs_has_laxity():
    assert hasattr(MARTE::GQAM::GaTimedObs, "laxity")
    descriptor = None
    for klass in MARTE::GQAM::GaTimedObs.__mro__:
        if "laxity" in klass.__dict__:
            descriptor = klass.__dict__["laxity"]
            break
    assert isinstance(descriptor, property)



def test_gqam::marte::operation_is_not_abstract():
    assert not inspect.isabstract(GQAM::MARTE::Operation)


def test_gqam::marte::operation_constructor_exists():
    assert callable(GQAM::MARTE::Operation.__init__)


def test_gqam::marte::operation_constructor_args():
    sig = inspect.signature(GQAM::MARTE::Operation.__init__)
    params = list(sig.parameters.keys())



def test_gastep_is_not_abstract():
    assert not inspect.isabstract(GaStep)


def test_gastep_constructor_exists():
    assert callable(GaStep.__init__)


def test_gastep_constructor_args():
    sig = inspect.signature(GaStep.__init__)
    params = list(sig.parameters.keys())



def test_marte::sam::sastep_is_not_abstract():
    assert not inspect.isabstract(MARTE::SAM::SaStep)


def test_marte::sam::sastep_constructor_exists():
    assert callable(MARTE::SAM::SaStep.__init__)


def test_marte::sam::sastep_constructor_args():
    sig = inspect.signature(MARTE::SAM::SaStep.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gacommstep_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaCommStep)


def test_marte::gqam::gacommstep_constructor_exists():
    assert callable(MARTE::GQAM::GaCommStep.__init__)


def test_marte::gqam::gacommstep_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaCommStep.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::garelstep_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaRelStep)


def test_marte::gqam::garelstep_constructor_exists():
    assert callable(MARTE::GQAM::GaRelStep.__init__)


def test_marte::gqam::garelstep_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaRelStep.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gaacqstep_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaAcqStep)


def test_marte::gqam::gaacqstep_constructor_exists():
    assert callable(MARTE::GQAM::GaAcqStep.__init__)


def test_marte::gqam::gaacqstep_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaAcqStep.__init__)
    params = list(sig.parameters.keys())



def test_marte::pam::pastep_is_not_abstract():
    assert not inspect.isabstract(MARTE::PAM::PaStep)


def test_marte::pam::pastep_constructor_exists():
    assert callable(MARTE::PAM::PaStep.__init__)


def test_marte::pam::pastep_constructor_args():
    sig = inspect.signature(MARTE::PAM::PaStep.__init__)
    params = list(sig.parameters.keys())
    assert "extOpDemand" in params, "Missing parameter 'extOpDemand'"

def test_marte::pam::pastep_has_extOpDemand():
    assert hasattr(MARTE::PAM::PaStep, "extOpDemand")
    descriptor = None
    for klass in MARTE::PAM::PaStep.__mro__:
        if "extOpDemand" in klass.__dict__:
            descriptor = klass.__dict__["extOpDemand"]
            break
    assert isinstance(descriptor, property)



def test_marte::gqam::garequestedservice_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaRequestedService)


def test_marte::gqam::garequestedservice_constructor_exists():
    assert callable(MARTE::GQAM::GaRequestedService.__init__)


def test_marte::gqam::garequestedservice_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaRequestedService.__init__)
    params = list(sig.parameters.keys())



def test_integerinterval_is_not_abstract():
    assert not inspect.isabstract(IntegerInterval)


def test_integerinterval_constructor_exists():
    assert callable(IntegerInterval.__init__)


def test_integerinterval_constructor_args():
    sig = inspect.signature(IntegerInterval.__init__)
    params = list(sig.parameters.keys())



def test_gascenario_is_not_abstract():
    assert not inspect.isabstract(GaScenario)


def test_gascenario_constructor_exists():
    assert callable(GaScenario.__init__)


def test_gascenario_constructor_args():
    sig = inspect.signature(GaScenario.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gastep_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaStep)


def test_marte::gqam::gastep_constructor_exists():
    assert callable(MARTE::GQAM::GaStep.__init__)


def test_marte::gqam::gastep_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaStep.__init__)
    params = list(sig.parameters.keys())



def test_gqam::gatimedobs_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaTimedObs)


def test_gqam::gatimedobs_constructor_exists():
    assert callable(GQAM::GaTimedObs.__init__)


def test_gqam::gatimedobs_constructor_args():
    sig = inspect.signature(GQAM::GaTimedObs.__init__)
    params = list(sig.parameters.keys())



def test_gqam::gastep_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaStep)


def test_gqam::gastep_constructor_exists():
    assert callable(GQAM::GaStep.__init__)


def test_gqam::gastep_constructor_args():
    sig = inspect.signature(GQAM::GaStep.__init__)
    params = list(sig.parameters.keys())



def test_gqam::garequestedservice_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaRequestedService)


def test_gqam::garequestedservice_constructor_exists():
    assert callable(GQAM::GaRequestedService.__init__)


def test_gqam::garequestedservice_constructor_args():
    sig = inspect.signature(GQAM::GaRequestedService.__init__)
    params = list(sig.parameters.keys())



def test_marte::pam::parequestedstep_is_not_abstract():
    assert not inspect.isabstract(MARTE::PAM::PaRequestedStep)


def test_marte::pam::parequestedstep_constructor_exists():
    assert callable(MARTE::PAM::PaRequestedStep.__init__)


def test_marte::pam::parequestedstep_constructor_args():
    sig = inspect.signature(MARTE::PAM::PaRequestedStep.__init__)
    params = list(sig.parameters.keys())



def test_gqam::gaexechost_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaExecHost)


def test_gqam::gaexechost_constructor_exists():
    assert callable(GQAM::GaExecHost.__init__)


def test_gqam::gaexechost_constructor_args():
    sig = inspect.signature(GQAM::GaExecHost.__init__)
    params = list(sig.parameters.keys())



def test_gqam::gaworkloadevent_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaWorkloadEvent)


def test_gqam::gaworkloadevent_constructor_exists():
    assert callable(GQAM::GaWorkloadEvent.__init__)


def test_gqam::gaworkloadevent_constructor_args():
    sig = inspect.signature(GQAM::GaWorkloadEvent.__init__)
    params = list(sig.parameters.keys())



def test_time::timedprocessing_is_not_abstract():
    assert not inspect.isabstract(Time::TimedProcessing)


def test_time::timedprocessing_constructor_exists():
    assert callable(Time::TimedProcessing.__init__)


def test_time::timedprocessing_constructor_args():
    sig = inspect.signature(Time::TimedProcessing.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gaworkloadgenerator_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaWorkloadGenerator)


def test_marte::gqam::gaworkloadgenerator_constructor_exists():
    assert callable(MARTE::GQAM::GaWorkloadGenerator.__init__)


def test_marte::gqam::gaworkloadgenerator_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaWorkloadGenerator.__init__)
    params = list(sig.parameters.keys())



def test_gcm::marte::behavior_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::Behavior)


def test_gcm::marte::behavior_constructor_exists():
    assert callable(GCM::MARTE::Behavior.__init__)


def test_gcm::marte::behavior_constructor_args():
    sig = inspect.signature(GCM::MARTE::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_gqam::marte::timeevent_is_not_abstract():
    assert not inspect.isabstract(GQAM::MARTE::TimeEvent)


def test_gqam::marte::timeevent_constructor_exists():
    assert callable(GQAM::MARTE::TimeEvent.__init__)


def test_gqam::marte::timeevent_constructor_args():
    sig = inspect.signature(GQAM::MARTE::TimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_gqam::gascenario_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaScenario)


def test_gqam::gascenario_constructor_exists():
    assert callable(GQAM::GaScenario.__init__)


def test_gqam::gascenario_constructor_args():
    sig = inspect.signature(GQAM::GaScenario.__init__)
    params = list(sig.parameters.keys())



def test_gqam::gaeventtrace_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaEventTrace)


def test_gqam::gaeventtrace_constructor_exists():
    assert callable(GQAM::GaEventTrace.__init__)


def test_gqam::gaeventtrace_constructor_args():
    sig = inspect.signature(GQAM::GaEventTrace.__init__)
    params = list(sig.parameters.keys())



def test_gqam::gaworkloadgenerator_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaWorkloadGenerator)


def test_gqam::gaworkloadgenerator_constructor_exists():
    assert callable(GQAM::GaWorkloadGenerator.__init__)


def test_gqam::gaworkloadgenerator_constructor_args():
    sig = inspect.signature(GQAM::GaWorkloadGenerator.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gaworkloadevent_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaWorkloadEvent)


def test_marte::gqam::gaworkloadevent_constructor_exists():
    assert callable(MARTE::GQAM::GaWorkloadEvent.__init__)


def test_marte::gqam::gaworkloadevent_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaWorkloadEvent.__init__)
    params = list(sig.parameters.keys())



def test_gqam::marte::namedelement_is_not_abstract():
    assert not inspect.isabstract(GQAM::MARTE::NamedElement)


def test_gqam::marte::namedelement_constructor_exists():
    assert callable(GQAM::MARTE::NamedElement.__init__)


def test_gqam::marte::namedelement_constructor_args():
    sig = inspect.signature(GQAM::MARTE::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gaeventtrace_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaEventTrace)


def test_marte::gqam::gaeventtrace_constructor_exists():
    assert callable(MARTE::GQAM::GaEventTrace.__init__)


def test_marte::gqam::gaeventtrace_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaEventTrace.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "location" in params, "Missing parameter 'location'"
    assert "content" in params, "Missing parameter 'content'"

def test_marte::gqam::gaeventtrace_has_format():
    assert hasattr(MARTE::GQAM::GaEventTrace, "format")
    descriptor = None
    for klass in MARTE::GQAM::GaEventTrace.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gaeventtrace_has_location():
    assert hasattr(MARTE::GQAM::GaEventTrace, "location")
    descriptor = None
    for klass in MARTE::GQAM::GaEventTrace.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gaeventtrace_has_content():
    assert hasattr(MARTE::GQAM::GaEventTrace, "content")
    descriptor = None
    for klass in MARTE::GQAM::GaEventTrace.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_gqam::marte::behavior_is_not_abstract():
    assert not inspect.isabstract(GQAM::MARTE::Behavior)


def test_gqam::marte::behavior_constructor_exists():
    assert callable(GQAM::MARTE::Behavior.__init__)


def test_gqam::marte::behavior_constructor_args():
    sig = inspect.signature(GQAM::MARTE::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_marte::gcm::flowspecification_is_not_abstract():
    assert not inspect.isabstract(MARTE::GCM::FlowSpecification)


def test_marte::gcm::flowspecification_constructor_exists():
    assert callable(MARTE::GCM::FlowSpecification.__init__)


def test_marte::gcm::flowspecification_constructor_args():
    sig = inspect.signature(MARTE::GCM::FlowSpecification.__init__)
    params = list(sig.parameters.keys())



def test_marte::gcm::clientserverspecification_is_not_abstract():
    assert not inspect.isabstract(MARTE::GCM::ClientServerSpecification)


def test_marte::gcm::clientserverspecification_constructor_exists():
    assert callable(MARTE::GCM::ClientServerSpecification.__init__)


def test_marte::gcm::clientserverspecification_constructor_args():
    sig = inspect.signature(MARTE::GCM::ClientServerSpecification.__init__)
    params = list(sig.parameters.keys())



def test_marte::gcm::datapool_is_not_abstract():
    assert not inspect.isabstract(MARTE::GCM::DataPool)


def test_marte::gcm::datapool_constructor_exists():
    assert callable(MARTE::GCM::DataPool.__init__)


def test_marte::gcm::datapool_constructor_args():
    sig = inspect.signature(MARTE::GCM::DataPool.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"

def test_marte::gcm::datapool_has_ordering():
    assert hasattr(MARTE::GCM::DataPool, "ordering")
    descriptor = None
    for klass in MARTE::GCM::DataPool.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)



def test_gcm::marte::classifier_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::Classifier)


def test_gcm::marte::classifier_constructor_exists():
    assert callable(GCM::MARTE::Classifier.__init__)


def test_gcm::marte::classifier_constructor_args():
    sig = inspect.signature(GCM::MARTE::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_gcm::marte::anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::AnyReceiveEvent)


def test_gcm::marte::anyreceiveevent_constructor_exists():
    assert callable(GCM::MARTE::AnyReceiveEvent.__init__)


def test_gcm::marte::anyreceiveevent_constructor_args():
    sig = inspect.signature(GCM::MARTE::AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_marte::gcm::dataevent_is_not_abstract():
    assert not inspect.isabstract(MARTE::GCM::DataEvent)


def test_marte::gcm::dataevent_constructor_exists():
    assert callable(MARTE::GCM::DataEvent.__init__)


def test_marte::gcm::dataevent_constructor_args():
    sig = inspect.signature(MARTE::GCM::DataEvent.__init__)
    params = list(sig.parameters.keys())



def test_gcm::marte::invocationaction_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::InvocationAction)


def test_gcm::marte::invocationaction_constructor_exists():
    assert callable(GCM::MARTE::InvocationAction.__init__)


def test_gcm::marte::invocationaction_constructor_args():
    sig = inspect.signature(GCM::MARTE::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_marte::gcm::gcminvocationaction_is_not_abstract():
    assert not inspect.isabstract(MARTE::GCM::GCMInvocationAction)


def test_marte::gcm::gcminvocationaction_constructor_exists():
    assert callable(MARTE::GCM::GCMInvocationAction.__init__)


def test_marte::gcm::gcminvocationaction_constructor_args():
    sig = inspect.signature(MARTE::GCM::GCMInvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_gcm::marte::feature_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::Feature)


def test_gcm::marte::feature_constructor_exists():
    assert callable(GCM::MARTE::Feature.__init__)


def test_gcm::marte::feature_constructor_args():
    sig = inspect.signature(GCM::MARTE::Feature.__init__)
    params = list(sig.parameters.keys())



def test_gcm::marte::trigger_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::Trigger)


def test_gcm::marte::trigger_constructor_exists():
    assert callable(GCM::MARTE::Trigger.__init__)


def test_gcm::marte::trigger_constructor_args():
    sig = inspect.signature(GCM::MARTE::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_marte::gcm::gcmtrigger_is_not_abstract():
    assert not inspect.isabstract(MARTE::GCM::GCMTrigger)


def test_marte::gcm::gcmtrigger_constructor_exists():
    assert callable(MARTE::GCM::GCMTrigger.__init__)


def test_marte::gcm::gcmtrigger_constructor_args():
    sig = inspect.signature(MARTE::GCM::GCMTrigger.__init__)
    params = list(sig.parameters.keys())



def test_gcm::marte::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::BehavioralFeature)


def test_gcm::marte::behavioralfeature_constructor_exists():
    assert callable(GCM::MARTE::BehavioralFeature.__init__)


def test_gcm::marte::behavioralfeature_constructor_args():
    sig = inspect.signature(GCM::MARTE::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_marte::gcm::clientserverfeature_is_not_abstract():
    assert not inspect.isabstract(MARTE::GCM::ClientServerFeature)


def test_marte::gcm::clientserverfeature_constructor_exists():
    assert callable(MARTE::GCM::ClientServerFeature.__init__)


def test_marte::gcm::clientserverfeature_constructor_args():
    sig = inspect.signature(MARTE::GCM::ClientServerFeature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte::gcm::clientserverfeature_has_kind():
    assert hasattr(MARTE::GCM::ClientServerFeature, "kind")
    descriptor = None
    for klass in MARTE::GCM::ClientServerFeature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_gcm::marte::property_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::Property)


def test_gcm::marte::property_constructor_exists():
    assert callable(GCM::MARTE::Property.__init__)


def test_gcm::marte::property_constructor_args():
    sig = inspect.signature(GCM::MARTE::Property.__init__)
    params = list(sig.parameters.keys())



def test_marte::gcm::flowproperty_is_not_abstract():
    assert not inspect.isabstract(MARTE::GCM::FlowProperty)


def test_marte::gcm::flowproperty_constructor_exists():
    assert callable(MARTE::GCM::FlowProperty.__init__)


def test_marte::gcm::flowproperty_constructor_args():
    sig = inspect.signature(MARTE::GCM::FlowProperty.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_marte::gcm::flowproperty_has_direction():
    assert hasattr(MARTE::GCM::FlowProperty, "direction")
    descriptor = None
    for klass in MARTE::GCM::FlowProperty.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_gcm::clientserverspecification_is_not_abstract():
    assert not inspect.isabstract(GCM::ClientServerSpecification)


def test_gcm::clientserverspecification_constructor_exists():
    assert callable(GCM::ClientServerSpecification.__init__)


def test_gcm::clientserverspecification_constructor_args():
    sig = inspect.signature(GCM::ClientServerSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gcm::marte::interface_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::Interface)


def test_gcm::marte::interface_constructor_exists():
    assert callable(GCM::MARTE::Interface.__init__)


def test_gcm::marte::interface_constructor_args():
    sig = inspect.signature(GCM::MARTE::Interface.__init__)
    params = list(sig.parameters.keys())



def test_marte::gcm::clientserverport_is_not_abstract():
    assert not inspect.isabstract(MARTE::GCM::ClientServerPort)


def test_marte::gcm::clientserverport_constructor_exists():
    assert callable(MARTE::GCM::ClientServerPort.__init__)


def test_marte::gcm::clientserverport_constructor_args():
    sig = inspect.signature(MARTE::GCM::ClientServerPort.__init__)
    params = list(sig.parameters.keys())
    assert "specificationKind" in params, "Missing parameter 'specificationKind'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "isConjugated" in params, "Missing parameter 'isConjugated'"

def test_marte::gcm::clientserverport_has_specificationKind():
    assert hasattr(MARTE::GCM::ClientServerPort, "specificationKind")
    descriptor = None
    for klass in MARTE::GCM::ClientServerPort.__mro__:
        if "specificationKind" in klass.__dict__:
            descriptor = klass.__dict__["specificationKind"]
            break
    assert isinstance(descriptor, property)

def test_marte::gcm::clientserverport_has_kind():
    assert hasattr(MARTE::GCM::ClientServerPort, "kind")
    descriptor = None
    for klass in MARTE::GCM::ClientServerPort.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_marte::gcm::clientserverport_has_isConjugated():
    assert hasattr(MARTE::GCM::ClientServerPort, "isConjugated")
    descriptor = None
    for klass in MARTE::GCM::ClientServerPort.__mro__:
        if "isConjugated" in klass.__dict__:
            descriptor = klass.__dict__["isConjugated"]
            break
    assert isinstance(descriptor, property)



def test_gcm::marte::port_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::Port)


def test_gcm::marte::port_constructor_exists():
    assert callable(GCM::MARTE::Port.__init__)


def test_gcm::marte::port_constructor_args():
    sig = inspect.signature(GCM::MARTE::Port.__init__)
    params = list(sig.parameters.keys())



def test_marte::gcm::flowport_is_not_abstract():
    assert not inspect.isabstract(MARTE::GCM::FlowPort)


def test_marte::gcm::flowport_constructor_exists():
    assert callable(MARTE::GCM::FlowPort.__init__)


def test_marte::gcm::flowport_constructor_args():
    sig = inspect.signature(MARTE::GCM::FlowPort.__init__)
    params = list(sig.parameters.keys())
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"
    assert "isConjugated" in params, "Missing parameter 'isConjugated'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_marte::gcm::flowport_has_isAtomic():
    assert hasattr(MARTE::GCM::FlowPort, "isAtomic")
    descriptor = None
    for klass in MARTE::GCM::FlowPort.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)

def test_marte::gcm::flowport_has_isConjugated():
    assert hasattr(MARTE::GCM::FlowPort, "isConjugated")
    descriptor = None
    for klass in MARTE::GCM::FlowPort.__mro__:
        if "isConjugated" in klass.__dict__:
            descriptor = klass.__dict__["isConjugated"]
            break
    assert isinstance(descriptor, property)

def test_marte::gcm::flowport_has_direction():
    assert hasattr(MARTE::GCM::FlowPort, "direction")
    descriptor = None
    for klass in MARTE::GCM::FlowPort.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_swsynchronizationresource_is_not_abstract():
    assert not inspect.isabstract(SwSynchronizationResource)


def test_swsynchronizationresource_constructor_exists():
    assert callable(SwSynchronizationResource.__init__)


def test_swsynchronizationresource_constructor_args():
    sig = inspect.signature(SwSynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::interaction::notificationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Interaction::NotificationResource)


def test_marte::sw::interaction::notificationresource_constructor_exists():
    assert callable(MARTE::SW::Interaction::NotificationResource.__init__)


def test_marte::sw::interaction::notificationresource_constructor_args():
    sig = inspect.signature(MARTE::SW::Interaction::NotificationResource.__init__)
    params = list(sig.parameters.keys())
    assert "occurence" in params, "Missing parameter 'occurence'"
    assert "mechanism" in params, "Missing parameter 'mechanism'"

def test_marte::sw::interaction::notificationresource_has_occurence():
    assert hasattr(MARTE::SW::Interaction::NotificationResource, "occurence")
    descriptor = None
    for klass in MARTE::SW::Interaction::NotificationResource.__mro__:
        if "occurence" in klass.__dict__:
            descriptor = klass.__dict__["occurence"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::interaction::notificationresource_has_mechanism():
    assert hasattr(MARTE::SW::Interaction::NotificationResource, "mechanism")
    descriptor = None
    for klass in MARTE::SW::Interaction::NotificationResource.__mro__:
        if "mechanism" in klass.__dict__:
            descriptor = klass.__dict__["mechanism"]
            break
    assert isinstance(descriptor, property)



def test_sw::interaction::swsynchronizationresource_is_not_abstract():
    assert not inspect.isabstract(SW::Interaction::SwSynchronizationResource)


def test_sw::interaction::swsynchronizationresource_constructor_exists():
    assert callable(SW::Interaction::SwSynchronizationResource.__init__)


def test_sw::interaction::swsynchronizationresource_constructor_args():
    sig = inspect.signature(SW::Interaction::SwSynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_sw::interaction::marte::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SW::Interaction::MARTE::BehavioralFeature)


def test_sw::interaction::marte::behavioralfeature_constructor_exists():
    assert callable(SW::Interaction::MARTE::BehavioralFeature.__init__)


def test_sw::interaction::marte::behavioralfeature_constructor_args():
    sig = inspect.signature(SW::Interaction::MARTE::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_swcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(SwCommunicationResource)


def test_swcommunicationresource_constructor_exists():
    assert callable(SwCommunicationResource.__init__)


def test_swcommunicationresource_constructor_args():
    sig = inspect.signature(SwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::interaction::messagecomresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Interaction::MessageComResource)


def test_marte::sw::interaction::messagecomresource_constructor_exists():
    assert callable(MARTE::SW::Interaction::MessageComResource.__init__)


def test_marte::sw::interaction::messagecomresource_constructor_args():
    sig = inspect.signature(MARTE::SW::Interaction::MessageComResource.__init__)
    params = list(sig.parameters.keys())
    assert "mechanism" in params, "Missing parameter 'mechanism'"
    assert "isFixedMessageSize" in params, "Missing parameter 'isFixedMessageSize'"
    assert "messageQueuePolicy" in params, "Missing parameter 'messageQueuePolicy'"

def test_marte::sw::interaction::messagecomresource_has_mechanism():
    assert hasattr(MARTE::SW::Interaction::MessageComResource, "mechanism")
    descriptor = None
    for klass in MARTE::SW::Interaction::MessageComResource.__mro__:
        if "mechanism" in klass.__dict__:
            descriptor = klass.__dict__["mechanism"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::interaction::messagecomresource_has_isFixedMessageSize():
    assert hasattr(MARTE::SW::Interaction::MessageComResource, "isFixedMessageSize")
    descriptor = None
    for klass in MARTE::SW::Interaction::MessageComResource.__mro__:
        if "isFixedMessageSize" in klass.__dict__:
            descriptor = klass.__dict__["isFixedMessageSize"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::interaction::messagecomresource_has_messageQueuePolicy():
    assert hasattr(MARTE::SW::Interaction::MessageComResource, "messageQueuePolicy")
    descriptor = None
    for klass in MARTE::SW::Interaction::MessageComResource.__mro__:
        if "messageQueuePolicy" in klass.__dict__:
            descriptor = klass.__dict__["messageQueuePolicy"]
            break
    assert isinstance(descriptor, property)



def test_marte::sw::interaction::shareddatacomresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Interaction::SharedDataComResource)


def test_marte::sw::interaction::shareddatacomresource_constructor_exists():
    assert callable(MARTE::SW::Interaction::SharedDataComResource.__init__)


def test_marte::sw::interaction::shareddatacomresource_constructor_args():
    sig = inspect.signature(MARTE::SW::Interaction::SharedDataComResource.__init__)
    params = list(sig.parameters.keys())



def test_grm::synchronizationresource_is_not_abstract():
    assert not inspect.isabstract(GRM::SynchronizationResource)


def test_grm::synchronizationresource_constructor_exists():
    assert callable(GRM::SynchronizationResource.__init__)


def test_grm::synchronizationresource_constructor_args():
    sig = inspect.signature(GRM::SynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_sw::interaction::swinteractionresource_is_not_abstract():
    assert not inspect.isabstract(SW::Interaction::SwInteractionResource)


def test_sw::interaction::swinteractionresource_constructor_exists():
    assert callable(SW::Interaction::SwInteractionResource.__init__)


def test_sw::interaction::swinteractionresource_constructor_args():
    sig = inspect.signature(SW::Interaction::SwInteractionResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::interaction::swsynchronizationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Interaction::SwSynchronizationResource)


def test_marte::sw::interaction::swsynchronizationresource_constructor_exists():
    assert callable(MARTE::SW::Interaction::SwSynchronizationResource.__init__)


def test_marte::sw::interaction::swsynchronizationresource_constructor_args():
    sig = inspect.signature(MARTE::SW::Interaction::SwSynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_sw::interaction::marte::typedelement_is_not_abstract():
    assert not inspect.isabstract(SW::Interaction::MARTE::TypedElement)


def test_sw::interaction::marte::typedelement_constructor_exists():
    assert callable(SW::Interaction::MARTE::TypedElement.__init__)


def test_sw::interaction::marte::typedelement_constructor_args():
    sig = inspect.signature(SW::Interaction::MARTE::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_sw::brokering::marte::activity_is_not_abstract():
    assert not inspect.isabstract(SW::Brokering::MARTE::Activity)


def test_sw::brokering::marte::activity_constructor_exists():
    assert callable(SW::Brokering::MARTE::Activity.__init__)


def test_sw::brokering::marte::activity_constructor_args():
    sig = inspect.signature(SW::Brokering::MARTE::Activity.__init__)
    params = list(sig.parameters.keys())



def test_sw::brokering::marte::operation_is_not_abstract():
    assert not inspect.isabstract(SW::Brokering::MARTE::Operation)


def test_sw::brokering::marte::operation_constructor_exists():
    assert callable(SW::Brokering::MARTE::Operation.__init__)


def test_sw::brokering::marte::operation_constructor_args():
    sig = inspect.signature(SW::Brokering::MARTE::Operation.__init__)
    params = list(sig.parameters.keys())



def test_sw::brokering::marte::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SW::Brokering::MARTE::BehavioralFeature)


def test_sw::brokering::marte::behavioralfeature_constructor_exists():
    assert callable(SW::Brokering::MARTE::BehavioralFeature.__init__)


def test_sw::brokering::marte::behavioralfeature_constructor_args():
    sig = inspect.signature(SW::Brokering::MARTE::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_sw::brokering::marte::typedelement_is_not_abstract():
    assert not inspect.isabstract(SW::Brokering::MARTE::TypedElement)


def test_sw::brokering::marte::typedelement_constructor_exists():
    assert callable(SW::Brokering::MARTE::TypedElement.__init__)


def test_sw::brokering::marte::typedelement_constructor_args():
    sig = inspect.signature(SW::Brokering::MARTE::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_interruptresource_is_not_abstract():
    assert not inspect.isabstract(InterruptResource)


def test_interruptresource_constructor_exists():
    assert callable(InterruptResource.__init__)


def test_interruptresource_constructor_args():
    sig = inspect.signature(InterruptResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::concurrency::alarm_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Concurrency::Alarm)


def test_marte::sw::concurrency::alarm_constructor_exists():
    assert callable(MARTE::SW::Concurrency::Alarm.__init__)


def test_marte::sw::concurrency::alarm_constructor_args():
    sig = inspect.signature(MARTE::SW::Concurrency::Alarm.__init__)
    params = list(sig.parameters.keys())
    assert "isWatchdog" in params, "Missing parameter 'isWatchdog'"

def test_marte::sw::concurrency::alarm_has_isWatchdog():
    assert hasattr(MARTE::SW::Concurrency::Alarm, "isWatchdog")
    descriptor = None
    for klass in MARTE::SW::Concurrency::Alarm.__mro__:
        if "isWatchdog" in klass.__dict__:
            descriptor = klass.__dict__["isWatchdog"]
            break
    assert isinstance(descriptor, property)



def test_sw::concurrency::marte::namespace_is_not_abstract():
    assert not inspect.isabstract(SW::Concurrency::MARTE::Namespace)


def test_sw::concurrency::marte::namespace_constructor_exists():
    assert callable(SW::Concurrency::MARTE::Namespace.__init__)


def test_sw::concurrency::marte::namespace_constructor_args():
    sig = inspect.signature(SW::Concurrency::MARTE::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_timerresource_is_not_abstract():
    assert not inspect.isabstract(TimerResource)


def test_timerresource_constructor_exists():
    assert callable(TimerResource.__init__)


def test_timerresource_constructor_args():
    sig = inspect.signature(TimerResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::concurrency::swtimerresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Concurrency::SwTimerResource)


def test_marte::sw::concurrency::swtimerresource_constructor_exists():
    assert callable(MARTE::SW::Concurrency::SwTimerResource.__init__)


def test_marte::sw::concurrency::swtimerresource_constructor_args():
    sig = inspect.signature(MARTE::SW::Concurrency::SwTimerResource.__init__)
    params = list(sig.parameters.keys())



def test_sw::concurrency::marte::namedelement_is_not_abstract():
    assert not inspect.isabstract(SW::Concurrency::MARTE::NamedElement)


def test_sw::concurrency::marte::namedelement_constructor_exists():
    assert callable(SW::Concurrency::MARTE::NamedElement.__init__)


def test_sw::concurrency::marte::namedelement_constructor_args():
    sig = inspect.signature(SW::Concurrency::MARTE::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_sw::concurrency::swconcurrentresource_is_not_abstract():
    assert not inspect.isabstract(SW::Concurrency::SwConcurrentResource)


def test_sw::concurrency::swconcurrentresource_constructor_exists():
    assert callable(SW::Concurrency::SwConcurrentResource.__init__)


def test_sw::concurrency::swconcurrentresource_constructor_args():
    sig = inspect.signature(SW::Concurrency::SwConcurrentResource.__init__)
    params = list(sig.parameters.keys())



def test_swconcurrentresource_is_not_abstract():
    assert not inspect.isabstract(SwConcurrentResource)


def test_swconcurrentresource_constructor_exists():
    assert callable(SwConcurrentResource.__init__)


def test_swconcurrentresource_constructor_args():
    sig = inspect.signature(SwConcurrentResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::concurrency::interruptresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Concurrency::InterruptResource)


def test_marte::sw::concurrency::interruptresource_constructor_exists():
    assert callable(MARTE::SW::Concurrency::InterruptResource.__init__)


def test_marte::sw::concurrency::interruptresource_constructor_args():
    sig = inspect.signature(MARTE::SW::Concurrency::InterruptResource.__init__)
    params = list(sig.parameters.keys())
    assert "isMaskable" in params, "Missing parameter 'isMaskable'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte::sw::concurrency::interruptresource_has_isMaskable():
    assert hasattr(MARTE::SW::Concurrency::InterruptResource, "isMaskable")
    descriptor = None
    for klass in MARTE::SW::Concurrency::InterruptResource.__mro__:
        if "isMaskable" in klass.__dict__:
            descriptor = klass.__dict__["isMaskable"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::concurrency::interruptresource_has_kind():
    assert hasattr(MARTE::SW::Concurrency::InterruptResource, "kind")
    descriptor = None
    for klass in MARTE::SW::Concurrency::InterruptResource.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_sw::concurrency::marte::typedelement_is_not_abstract():
    assert not inspect.isabstract(SW::Concurrency::MARTE::TypedElement)


def test_sw::concurrency::marte::typedelement_constructor_exists():
    assert callable(SW::Concurrency::MARTE::TypedElement.__init__)


def test_sw::concurrency::marte::typedelement_constructor_args():
    sig = inspect.signature(SW::Concurrency::MARTE::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_sw::concurrency::marte::element_is_not_abstract():
    assert not inspect.isabstract(SW::Concurrency::MARTE::Element)


def test_sw::concurrency::marte::element_constructor_exists():
    assert callable(SW::Concurrency::MARTE::Element.__init__)


def test_sw::concurrency::marte::element_constructor_args():
    sig = inspect.signature(SW::Concurrency::MARTE::Element.__init__)
    params = list(sig.parameters.keys())



def test_swresource_is_not_abstract():
    assert not inspect.isabstract(SwResource)


def test_swresource_constructor_exists():
    assert callable(SwResource.__init__)


def test_swresource_constructor_args():
    sig = inspect.signature(SwResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::interaction::swinteractionresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Interaction::SwInteractionResource)


def test_marte::sw::interaction::swinteractionresource_constructor_exists():
    assert callable(MARTE::SW::Interaction::SwInteractionResource.__init__)


def test_marte::sw::interaction::swinteractionresource_constructor_args():
    sig = inspect.signature(MARTE::SW::Interaction::SwInteractionResource.__init__)
    params = list(sig.parameters.keys())
    assert "waitingQueueCapacity" in params, "Missing parameter 'waitingQueueCapacity'"
    assert "waitingQueuePolicy" in params, "Missing parameter 'waitingQueuePolicy'"
    assert "isIntraMemoryPartitionInteraction" in params, "Missing parameter 'isIntraMemoryPartitionInteraction'"

def test_marte::sw::interaction::swinteractionresource_has_waitingQueueCapacity():
    assert hasattr(MARTE::SW::Interaction::SwInteractionResource, "waitingQueueCapacity")
    descriptor = None
    for klass in MARTE::SW::Interaction::SwInteractionResource.__mro__:
        if "waitingQueueCapacity" in klass.__dict__:
            descriptor = klass.__dict__["waitingQueueCapacity"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::interaction::swinteractionresource_has_waitingQueuePolicy():
    assert hasattr(MARTE::SW::Interaction::SwInteractionResource, "waitingQueuePolicy")
    descriptor = None
    for klass in MARTE::SW::Interaction::SwInteractionResource.__mro__:
        if "waitingQueuePolicy" in klass.__dict__:
            descriptor = klass.__dict__["waitingQueuePolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::interaction::swinteractionresource_has_isIntraMemoryPartitionInteraction():
    assert hasattr(MARTE::SW::Interaction::SwInteractionResource, "isIntraMemoryPartitionInteraction")
    descriptor = None
    for klass in MARTE::SW::Interaction::SwInteractionResource.__mro__:
        if "isIntraMemoryPartitionInteraction" in klass.__dict__:
            descriptor = klass.__dict__["isIntraMemoryPartitionInteraction"]
            break
    assert isinstance(descriptor, property)



def test_marte::sw::brokering::memorybroker_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Brokering::MemoryBroker)


def test_marte::sw::brokering::memorybroker_constructor_exists():
    assert callable(MARTE::SW::Brokering::MemoryBroker.__init__)


def test_marte::sw::brokering::memorybroker_constructor_args():
    sig = inspect.signature(MARTE::SW::Brokering::MemoryBroker.__init__)
    params = list(sig.parameters.keys())
    assert "accessPolicy" in params, "Missing parameter 'accessPolicy'"

def test_marte::sw::brokering::memorybroker_has_accessPolicy():
    assert hasattr(MARTE::SW::Brokering::MemoryBroker, "accessPolicy")
    descriptor = None
    for klass in MARTE::SW::Brokering::MemoryBroker.__mro__:
        if "accessPolicy" in klass.__dict__:
            descriptor = klass.__dict__["accessPolicy"]
            break
    assert isinstance(descriptor, property)



def test_marte::sw::concurrency::memorypartition_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Concurrency::MemoryPartition)


def test_marte::sw::concurrency::memorypartition_constructor_exists():
    assert callable(MARTE::SW::Concurrency::MemoryPartition.__init__)


def test_marte::sw::concurrency::memorypartition_constructor_args():
    sig = inspect.signature(MARTE::SW::Concurrency::MemoryPartition.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::brokering::devicebroker_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Brokering::DeviceBroker)


def test_marte::sw::brokering::devicebroker_constructor_exists():
    assert callable(MARTE::SW::Brokering::DeviceBroker.__init__)


def test_marte::sw::brokering::devicebroker_constructor_args():
    sig = inspect.signature(MARTE::SW::Brokering::DeviceBroker.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accessPolicy" in params, "Missing parameter 'accessPolicy'"
    assert "isBuffered" in params, "Missing parameter 'isBuffered'"

def test_marte::sw::brokering::devicebroker_has_name():
    assert hasattr(MARTE::SW::Brokering::DeviceBroker, "name")
    descriptor = None
    for klass in MARTE::SW::Brokering::DeviceBroker.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::brokering::devicebroker_has_accessPolicy():
    assert hasattr(MARTE::SW::Brokering::DeviceBroker, "accessPolicy")
    descriptor = None
    for klass in MARTE::SW::Brokering::DeviceBroker.__mro__:
        if "accessPolicy" in klass.__dict__:
            descriptor = klass.__dict__["accessPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::brokering::devicebroker_has_isBuffered():
    assert hasattr(MARTE::SW::Brokering::DeviceBroker, "isBuffered")
    descriptor = None
    for klass in MARTE::SW::Brokering::DeviceBroker.__mro__:
        if "isBuffered" in klass.__dict__:
            descriptor = klass.__dict__["isBuffered"]
            break
    assert isinstance(descriptor, property)



def test_marte::sw::concurrency::swconcurrentresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Concurrency::SwConcurrentResource)


def test_marte::sw::concurrency::swconcurrentresource_constructor_exists():
    assert callable(MARTE::SW::Concurrency::SwConcurrentResource.__init__)


def test_marte::sw::concurrency::swconcurrentresource_constructor_args():
    sig = inspect.signature(MARTE::SW::Concurrency::SwConcurrentResource.__init__)
    params = list(sig.parameters.keys())
    assert "activationCapacity" in params, "Missing parameter 'activationCapacity'"

def test_marte::sw::concurrency::swconcurrentresource_has_activationCapacity():
    assert hasattr(MARTE::SW::Concurrency::SwConcurrentResource, "activationCapacity")
    descriptor = None
    for klass in MARTE::SW::Concurrency::SwConcurrentResource.__mro__:
        if "activationCapacity" in klass.__dict__:
            descriptor = klass.__dict__["activationCapacity"]
            break
    assert isinstance(descriptor, property)



def test_sw::resourcecore::marte::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SW::ResourceCore::MARTE::BehavioralFeature)


def test_sw::resourcecore::marte::behavioralfeature_constructor_exists():
    assert callable(SW::ResourceCore::MARTE::BehavioralFeature.__init__)


def test_sw::resourcecore::marte::behavioralfeature_constructor_args():
    sig = inspect.signature(SW::ResourceCore::MARTE::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_sw::resourcecore::marte::typedelement_is_not_abstract():
    assert not inspect.isabstract(SW::ResourceCore::MARTE::TypedElement)


def test_sw::resourcecore::marte::typedelement_constructor_exists():
    assert callable(SW::ResourceCore::MARTE::TypedElement.__init__)


def test_sw::resourcecore::marte::typedelement_constructor_args():
    sig = inspect.signature(SW::ResourceCore::MARTE::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_sw::concurrency::marte::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SW::Concurrency::MARTE::BehavioralFeature)


def test_sw::concurrency::marte::behavioralfeature_constructor_exists():
    assert callable(SW::Concurrency::MARTE::BehavioralFeature.__init__)


def test_sw::concurrency::marte::behavioralfeature_constructor_args():
    sig = inspect.signature(SW::Concurrency::MARTE::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_sw::brokering::devicebroker_is_not_abstract():
    assert not inspect.isabstract(SW::Brokering::DeviceBroker)


def test_sw::brokering::devicebroker_constructor_exists():
    assert callable(SW::Brokering::DeviceBroker.__init__)


def test_sw::brokering::devicebroker_constructor_args():
    sig = inspect.signature(SW::Brokering::DeviceBroker.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwdiagram::srmdiagram_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDiagram::SRMDiagram)


def test_marte::hwdiagram::srmdiagram_constructor_exists():
    assert callable(MARTE::HwDiagram::SRMDiagram.__init__)


def test_marte::hwdiagram::srmdiagram_constructor_args():
    sig = inspect.signature(MARTE::HwDiagram::SRMDiagram.__init__)
    params = list(sig.parameters.keys())



def test_sw::resourcecore::marte::property_is_not_abstract():
    assert not inspect.isabstract(SW::ResourceCore::MARTE::Property)


def test_sw::resourcecore::marte::property_constructor_exists():
    assert callable(SW::ResourceCore::MARTE::Property.__init__)


def test_sw::resourcecore::marte::property_constructor_args():
    sig = inspect.signature(SW::ResourceCore::MARTE::Property.__init__)
    params = list(sig.parameters.keys())



def test_hwdiagram::marte::datatype_is_not_abstract():
    assert not inspect.isabstract(HwDiagram::MARTE::DataType)


def test_hwdiagram::marte::datatype_constructor_exists():
    assert callable(HwDiagram::MARTE::DataType.__init__)


def test_hwdiagram::marte::datatype_constructor_args():
    sig = inspect.signature(HwDiagram::MARTE::DataType.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwdiagram::hwcircuitdiagram_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDiagram::HwCircuitDiagram)


def test_marte::hwdiagram::hwcircuitdiagram_constructor_exists():
    assert callable(MARTE::HwDiagram::HwCircuitDiagram.__init__)


def test_marte::hwdiagram::hwcircuitdiagram_constructor_args():
    sig = inspect.signature(MARTE::HwDiagram::HwCircuitDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_marte::hwdiagram::hwcircuitdiagram_has_name():
    assert hasattr(MARTE::HwDiagram::HwCircuitDiagram, "name")
    descriptor = None
    for klass in MARTE::HwDiagram::HwCircuitDiagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hwcommunication::hwconnection_is_not_abstract():
    assert not inspect.isabstract(HwCommunication::HwConnection)


def test_hwcommunication::hwconnection_constructor_exists():
    assert callable(HwCommunication::HwConnection.__init__)


def test_hwcommunication::hwconnection_constructor_args():
    sig = inspect.signature(HwCommunication::HwConnection.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwdiagram::hwhrmdiagram_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDiagram::HwHRMDiagram)


def test_marte::hwdiagram::hwhrmdiagram_constructor_exists():
    assert callable(MARTE::HwDiagram::HwHRMDiagram.__init__)


def test_marte::hwdiagram::hwhrmdiagram_constructor_args():
    sig = inspect.signature(MARTE::HwDiagram::HwHRMDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_marte::hwdiagram::hwhrmdiagram_has_name():
    assert hasattr(MARTE::HwDiagram::HwHRMDiagram, "name")
    descriptor = None
    for klass in MARTE::HwDiagram::HwHRMDiagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hwpackage::hwwire_is_not_abstract():
    assert not inspect.isabstract(HwPackage::HwWire)


def test_hwpackage::hwwire_constructor_exists():
    assert callable(HwPackage::HwWire.__init__)


def test_hwpackage::hwwire_constructor_args():
    sig = inspect.signature(HwPackage::HwWire.__init__)
    params = list(sig.parameters.keys())



def test_pam::marte::namedelement_is_not_abstract():
    assert not inspect.isabstract(PAM::MARTE::NamedElement)


def test_pam::marte::namedelement_constructor_exists():
    assert callable(PAM::MARTE::NamedElement.__init__)


def test_pam::marte::namedelement_constructor_args():
    sig = inspect.signature(PAM::MARTE::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte::pam::parespassstep_is_not_abstract():
    assert not inspect.isabstract(MARTE::PAM::PaResPassStep)


def test_marte::pam::parespassstep_constructor_exists():
    assert callable(MARTE::PAM::PaResPassStep.__init__)


def test_marte::pam::parespassstep_constructor_args():
    sig = inspect.signature(MARTE::PAM::PaResPassStep.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwpackage::hwpackage_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPackage::HwPackage)


def test_marte::hwpackage::hwpackage_constructor_exists():
    assert callable(MARTE::HwPackage::HwPackage.__init__)


def test_marte::hwpackage::hwpackage_constructor_args():
    sig = inspect.signature(MARTE::HwPackage::HwPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pinNum" in params, "Missing parameter 'pinNum'"
    assert "packageType" in params, "Missing parameter 'packageType'"

def test_marte::hwpackage::hwpackage_has_name():
    assert hasattr(MARTE::HwPackage::HwPackage, "name")
    descriptor = None
    for klass in MARTE::HwPackage::HwPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwpackage::hwpackage_has_pinNum():
    assert hasattr(MARTE::HwPackage::HwPackage, "pinNum")
    descriptor = None
    for klass in MARTE::HwPackage::HwPackage.__mro__:
        if "pinNum" in klass.__dict__:
            descriptor = klass.__dict__["pinNum"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwpackage::hwpackage_has_packageType():
    assert hasattr(MARTE::HwPackage::HwPackage, "packageType")
    descriptor = None
    for klass in MARTE::HwPackage::HwPackage.__mro__:
        if "packageType" in klass.__dict__:
            descriptor = klass.__dict__["packageType"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwdatasheet::hwdatasheet_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDatasheet::HwDatasheet)


def test_marte::hwdatasheet::hwdatasheet_constructor_exists():
    assert callable(MARTE::HwDatasheet::HwDatasheet.__init__)


def test_marte::hwdatasheet::hwdatasheet_constructor_args():
    sig = inspect.signature(MARTE::HwDatasheet::HwDatasheet.__init__)
    params = list(sig.parameters.keys())
    assert "revision" in params, "Missing parameter 'revision'"
    assert "name" in params, "Missing parameter 'name'"

def test_marte::hwdatasheet::hwdatasheet_has_revision():
    assert hasattr(MARTE::HwDatasheet::HwDatasheet, "revision")
    descriptor = None
    for klass in MARTE::HwDatasheet::HwDatasheet.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwdatasheet::hwdatasheet_has_name():
    assert hasattr(MARTE::HwDatasheet::HwDatasheet, "name")
    descriptor = None
    for klass in MARTE::HwDatasheet::HwDatasheet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwdiagram::hwblockdiagram_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDiagram::HwBlockDiagram)


def test_marte::hwdiagram::hwblockdiagram_constructor_exists():
    assert callable(MARTE::HwDiagram::HwBlockDiagram.__init__)


def test_marte::hwdiagram::hwblockdiagram_constructor_args():
    sig = inspect.signature(MARTE::HwDiagram::HwBlockDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_marte::hwdiagram::hwblockdiagram_has_name():
    assert hasattr(MARTE::HwDiagram::HwBlockDiagram, "name")
    descriptor = None
    for klass in MARTE::HwDiagram::HwBlockDiagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hwprotocol::marte::operation_is_not_abstract():
    assert not inspect.isabstract(HwProtocol::MARTE::Operation)


def test_hwprotocol::marte::operation_constructor_exists():
    assert callable(HwProtocol::MARTE::Operation.__init__)


def test_hwprotocol::marte::operation_constructor_args():
    sig = inspect.signature(HwProtocol::MARTE::Operation.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwprotocol::hwprotocol_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwProtocol::HwProtocol)


def test_marte::hwprotocol::hwprotocol_constructor_exists():
    assert callable(MARTE::HwProtocol::HwProtocol.__init__)


def test_marte::hwprotocol::hwprotocol_constructor_args():
    sig = inspect.signature(MARTE::HwProtocol::HwProtocol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_marte::hwprotocol::hwprotocol_has_name():
    assert hasattr(MARTE::HwProtocol::HwProtocol, "name")
    descriptor = None
    for klass in MARTE::HwProtocol::HwProtocol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hwperipheral::registeraction_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral::RegisterAction)


def test_hwperipheral::registeraction_constructor_exists():
    assert callable(HwPeripheral::RegisterAction.__init__)


def test_hwperipheral::registeraction_constructor_args():
    sig = inspect.signature(HwPeripheral::RegisterAction.__init__)
    params = list(sig.parameters.keys())



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwperipheral::peripheralactivity_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPeripheral::PeripheralActivity)


def test_marte::hwperipheral::peripheralactivity_constructor_exists():
    assert callable(MARTE::HwPeripheral::PeripheralActivity.__init__)


def test_marte::hwperipheral::peripheralactivity_constructor_args():
    sig = inspect.signature(MARTE::HwPeripheral::PeripheralActivity.__init__)
    params = list(sig.parameters.keys())



def test_hwperipheral::marte::outputpin_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral::MARTE::OutputPin)


def test_hwperipheral::marte::outputpin_constructor_exists():
    assert callable(HwPeripheral::MARTE::OutputPin.__init__)


def test_hwperipheral::marte::outputpin_constructor_args():
    sig = inspect.signature(HwPeripheral::MARTE::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_hwperipheral::marte::inputpin_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral::MARTE::InputPin)


def test_hwperipheral::marte::inputpin_constructor_exists():
    assert callable(HwPeripheral::MARTE::InputPin.__init__)


def test_hwperipheral::marte::inputpin_constructor_args():
    sig = inspect.signature(HwPeripheral::MARTE::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_registeraction_is_not_abstract():
    assert not inspect.isabstract(RegisterAction)


def test_registeraction_constructor_exists():
    assert callable(RegisterAction.__init__)


def test_registeraction_constructor_args():
    sig = inspect.signature(RegisterAction.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwperipheral::readregisteraction_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPeripheral::ReadRegisterAction)


def test_marte::hwperipheral::readregisteraction_constructor_exists():
    assert callable(MARTE::HwPeripheral::ReadRegisterAction.__init__)


def test_marte::hwperipheral::readregisteraction_constructor_args():
    sig = inspect.signature(MARTE::HwPeripheral::ReadRegisterAction.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwperipheral::writeregisteraction_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPeripheral::WriteRegisterAction)


def test_marte::hwperipheral::writeregisteraction_constructor_exists():
    assert callable(MARTE::HwPeripheral::WriteRegisterAction.__init__)


def test_marte::hwperipheral::writeregisteraction_constructor_args():
    sig = inspect.signature(MARTE::HwPeripheral::WriteRegisterAction.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwperipheral::registeraction_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPeripheral::RegisterAction)


def test_marte::hwperipheral::registeraction_constructor_exists():
    assert callable(MARTE::HwPeripheral::RegisterAction.__init__)


def test_marte::hwperipheral::registeraction_constructor_args():
    sig = inspect.signature(MARTE::HwPeripheral::RegisterAction.__init__)
    params = list(sig.parameters.keys())



def test_hwperipheral::marte::operation_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral::MARTE::Operation)


def test_hwperipheral::marte::operation_constructor_exists():
    assert callable(HwPeripheral::MARTE::Operation.__init__)


def test_hwperipheral::marte::operation_constructor_args():
    sig = inspect.signature(HwPeripheral::MARTE::Operation.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwdevicefunction::hwdevicefunction_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDeviceFunction::HwDeviceFunction)


def test_marte::hwdevicefunction::hwdevicefunction_constructor_exists():
    assert callable(MARTE::HwDeviceFunction::HwDeviceFunction.__init__)


def test_marte::hwdevicefunction::hwdevicefunction_constructor_args():
    sig = inspect.signature(MARTE::HwDeviceFunction::HwDeviceFunction.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwperipheral::operationimpl_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPeripheral::OperationImpl)


def test_marte::hwperipheral::operationimpl_constructor_exists():
    assert callable(MARTE::HwPeripheral::OperationImpl.__init__)


def test_marte::hwperipheral::operationimpl_constructor_args():
    sig = inspect.signature(MARTE::HwPeripheral::OperationImpl.__init__)
    params = list(sig.parameters.keys())



def test_hwio::hwline_is_not_abstract():
    assert not inspect.isabstract(HwIO::HwLine)


def test_hwio::hwline_constructor_exists():
    assert callable(HwIO::HwLine.__init__)


def test_hwio::hwline_constructor_args():
    sig = inspect.signature(HwIO::HwLine.__init__)
    params = list(sig.parameters.keys())



def test_hwpackage::hwpackagepin_is_not_abstract():
    assert not inspect.isabstract(HwPackage::HwPackagePin)


def test_hwpackage::hwpackagepin_constructor_exists():
    assert callable(HwPackage::HwPackagePin.__init__)


def test_hwpackage::hwpackagepin_constructor_args():
    sig = inspect.signature(HwPackage::HwPackagePin.__init__)
    params = list(sig.parameters.keys())



def test_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HwComponent)


def test_hwcomponent_constructor_exists():
    assert callable(HwComponent.__init__)


def test_hwcomponent_constructor_args():
    sig = inspect.signature(HwComponent.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwpower::hwpowersupply_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPower::HwPowerSupply)


def test_marte::hwpower::hwpowersupply_constructor_exists():
    assert callable(MARTE::HwPower::HwPowerSupply.__init__)


def test_marte::hwpower::hwpowersupply_constructor_args():
    sig = inspect.signature(MARTE::HwPower::HwPowerSupply.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwpower::hwcoolingsupply_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPower::HwCoolingSupply)


def test_marte::hwpower::hwcoolingsupply_constructor_exists():
    assert callable(MARTE::HwPower::HwCoolingSupply.__init__)


def test_marte::hwpower::hwcoolingsupply_constructor_args():
    sig = inspect.signature(MARTE::HwPower::HwCoolingSupply.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwlayout::env::condition_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwLayout::Env::Condition)


def test_marte::hwlayout::env::condition_constructor_exists():
    assert callable(MARTE::HwLayout::Env::Condition.__init__)


def test_marte::hwlayout::env::condition_constructor_args():
    sig = inspect.signature(MARTE::HwLayout::Env::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "status" in params, "Missing parameter 'status'"

def test_marte::hwlayout::env::condition_has_type():
    assert hasattr(MARTE::HwLayout::Env::Condition, "type")
    descriptor = None
    for klass in MARTE::HwLayout::Env::Condition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwlayout::env::condition_has_status():
    assert hasattr(MARTE::HwLayout::Env::Condition, "status")
    descriptor = None
    for klass in MARTE::HwLayout::Env::Condition.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_hwlayout::hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HwLayout::HwComponent)


def test_hwlayout::hwcomponent_constructor_exists():
    assert callable(HwLayout::HwComponent.__init__)


def test_hwlayout::hwcomponent_constructor_args():
    sig = inspect.signature(HwLayout::HwComponent.__init__)
    params = list(sig.parameters.keys())



def test_hwlayout::env::condition_is_not_abstract():
    assert not inspect.isabstract(HwLayout::Env::Condition)


def test_hwlayout::env::condition_constructor_exists():
    assert callable(HwLayout::Env::Condition.__init__)


def test_hwlayout::env::condition_constructor_args():
    sig = inspect.signature(HwLayout::Env::Condition.__init__)
    params = list(sig.parameters.keys())



def test_nfp::price_is_not_abstract():
    assert not inspect.isabstract(NFP::Price)


def test_nfp::price_constructor_exists():
    assert callable(NFP::Price.__init__)


def test_nfp::price_constructor_args():
    sig = inspect.signature(NFP::Price.__init__)
    params = list(sig.parameters.keys())



def test_realnterval_is_not_abstract():
    assert not inspect.isabstract(Realnterval)


def test_realnterval_constructor_exists():
    assert callable(Realnterval.__init__)


def test_realnterval_constructor_args():
    sig = inspect.signature(Realnterval.__init__)
    params = list(sig.parameters.keys())



def test_nfp::length_is_not_abstract():
    assert not inspect.isabstract(NFP::Length)


def test_nfp::length_constructor_exists():
    assert callable(NFP::Length.__init__)


def test_nfp::length_constructor_args():
    sig = inspect.signature(NFP::Length.__init__)
    params = list(sig.parameters.keys())



def test_hwgeneral::marte::activity_is_not_abstract():
    assert not inspect.isabstract(HwGeneral::MARTE::Activity)


def test_hwgeneral::marte::activity_constructor_exists():
    assert callable(HwGeneral::MARTE::Activity.__init__)


def test_hwgeneral::marte::activity_constructor_args():
    sig = inspect.signature(HwGeneral::MARTE::Activity.__init__)
    params = list(sig.parameters.keys())



def test_hwgeneral::marte::operation_is_not_abstract():
    assert not inspect.isabstract(HwGeneral::MARTE::Operation)


def test_hwgeneral::marte::operation_constructor_exists():
    assert callable(HwGeneral::MARTE::Operation.__init__)


def test_hwgeneral::marte::operation_constructor_args():
    sig = inspect.signature(HwGeneral::MARTE::Operation.__init__)
    params = list(sig.parameters.keys())



def test_nfp::frequency_is_not_abstract():
    assert not inspect.isabstract(NFP::Frequency)


def test_nfp::frequency_constructor_exists():
    assert callable(NFP::Frequency.__init__)


def test_nfp::frequency_constructor_args():
    sig = inspect.signature(NFP::Frequency.__init__)
    params = list(sig.parameters.keys())



def test_hwcommunication::hwendpoint_is_not_abstract():
    assert not inspect.isabstract(HwCommunication::HwEndPoint)


def test_hwcommunication::hwendpoint_constructor_exists():
    assert callable(HwCommunication::HwEndPoint.__init__)


def test_hwcommunication::hwendpoint_constructor_args():
    sig = inspect.signature(HwCommunication::HwEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_hwgeneral::hwresourceservice_is_not_abstract():
    assert not inspect.isabstract(HwGeneral::HwResourceService)


def test_hwgeneral::hwresourceservice_constructor_exists():
    assert callable(HwGeneral::HwResourceService.__init__)


def test_hwgeneral::hwresourceservice_constructor_args():
    sig = inspect.signature(HwGeneral::HwResourceService.__init__)
    params = list(sig.parameters.keys())



def test_nfp::naturalinterval_is_not_abstract():
    assert not inspect.isabstract(NFP::NaturalInterval)


def test_nfp::naturalinterval_constructor_exists():
    assert callable(NFP::NaturalInterval.__init__)


def test_nfp::naturalinterval_constructor_args():
    sig = inspect.signature(NFP::NaturalInterval.__init__)
    params = list(sig.parameters.keys())



def test_nfp::area_is_not_abstract():
    assert not inspect.isabstract(NFP::Area)


def test_nfp::area_constructor_exists():
    assert callable(NFP::Area.__init__)


def test_nfp::area_constructor_args():
    sig = inspect.signature(NFP::Area.__init__)
    params = list(sig.parameters.keys())



def test_hwperipheral::peripheralactivity_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral::PeripheralActivity)


def test_hwperipheral::peripheralactivity_constructor_exists():
    assert callable(HwPeripheral::PeripheralActivity.__init__)


def test_hwperipheral::peripheralactivity_constructor_args():
    sig = inspect.signature(HwPeripheral::PeripheralActivity.__init__)
    params = list(sig.parameters.keys())



def test_hwperipheral::operationimpl_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral::OperationImpl)


def test_hwperipheral::operationimpl_constructor_exists():
    assert callable(HwPeripheral::OperationImpl.__init__)


def test_hwperipheral::operationimpl_constructor_args():
    sig = inspect.signature(HwPeripheral::OperationImpl.__init__)
    params = list(sig.parameters.keys())



def test_hwi::o_is_not_abstract():
    assert not inspect.isabstract(HwI::O)


def test_hwi::o_constructor_exists():
    assert callable(HwI::O.__init__)


def test_hwi::o_constructor_args():
    sig = inspect.signature(HwI::O.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwdevice::hwsensor_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDevice::HWSensor)


def test_marte::hwdevice::hwsensor_constructor_exists():
    assert callable(MARTE::HwDevice::HWSensor.__init__)


def test_marte::hwdevice::hwsensor_constructor_args():
    sig = inspect.signature(MARTE::HwDevice::HWSensor.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwdevice::hwactuator_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDevice::HWActuator)


def test_marte::hwdevice::hwactuator_constructor_exists():
    assert callable(MARTE::HwDevice::HWActuator.__init__)


def test_marte::hwdevice::hwactuator_constructor_args():
    sig = inspect.signature(MARTE::HwDevice::HWActuator.__init__)
    params = list(sig.parameters.keys())



def test_hwdevice_is_not_abstract():
    assert not inspect.isabstract(HwDevice)


def test_hwdevice_constructor_exists():
    assert callable(HwDevice.__init__)


def test_hwdevice_constructor_args():
    sig = inspect.signature(HwDevice.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwdevice::hwperipheral_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDevice::HwPeripheral)


def test_marte::hwdevice::hwperipheral_constructor_exists():
    assert callable(MARTE::HwDevice::HwPeripheral.__init__)


def test_marte::hwdevice::hwperipheral_constructor_args():
    sig = inspect.signature(MARTE::HwDevice::HwPeripheral.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwdevice::hwsupport_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDevice::HwSupport)


def test_marte::hwdevice::hwsupport_constructor_exists():
    assert callable(MARTE::HwDevice::HwSupport.__init__)


def test_marte::hwdevice::hwsupport_constructor_args():
    sig = inspect.signature(MARTE::HwDevice::HwSupport.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwdevice::hwi::o_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDevice::HwI::O)


def test_marte::hwdevice::hwi::o_constructor_exists():
    assert callable(MARTE::HwDevice::HwI::O.__init__)


def test_marte::hwdevice::hwi::o_constructor_args():
    sig = inspect.signature(MARTE::HwDevice::HwI::O.__init__)
    params = list(sig.parameters.keys())



def test_hwtimingresource_is_not_abstract():
    assert not inspect.isabstract(HwTimingResource)


def test_hwtimingresource_constructor_exists():
    assert callable(HwTimingResource.__init__)


def test_hwtimingresource_constructor_args():
    sig = inspect.signature(HwTimingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwtiming::hwtimer_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwTiming::HwTimer)


def test_marte::hwtiming::hwtimer_constructor_exists():
    assert callable(MARTE::HwTiming::HwTimer.__init__)


def test_marte::hwtiming::hwtimer_constructor_args():
    sig = inspect.signature(MARTE::HwTiming::HwTimer.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwtiming::hwclock_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwTiming::HwClock)


def test_marte::hwtiming::hwclock_constructor_exists():
    assert callable(MARTE::HwTiming::HwClock.__init__)


def test_marte::hwtiming::hwclock_constructor_args():
    sig = inspect.signature(MARTE::HwTiming::HwClock.__init__)
    params = list(sig.parameters.keys())



def test_grm::timingresource_is_not_abstract():
    assert not inspect.isabstract(GRM::TimingResource)


def test_grm::timingresource_constructor_exists():
    assert callable(GRM::TimingResource.__init__)


def test_grm::timingresource_constructor_args():
    sig = inspect.signature(GRM::TimingResource.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory::cachestructure_is_not_abstract():
    assert not inspect.isabstract(HwMemory::CacheStructure)


def test_hwmemory::cachestructure_constructor_exists():
    assert callable(HwMemory::CacheStructure.__init__)


def test_hwmemory::cachestructure_constructor_args():
    sig = inspect.signature(HwMemory::CacheStructure.__init__)
    params = list(sig.parameters.keys())



def test_hwdevicefunction::hwdevicefunction_is_not_abstract():
    assert not inspect.isabstract(HwDeviceFunction::HwDeviceFunction)


def test_hwdevicefunction::hwdevicefunction_constructor_exists():
    assert callable(HwDeviceFunction::HwDeviceFunction.__init__)


def test_hwdevicefunction::hwdevicefunction_constructor_args():
    sig = inspect.signature(HwDeviceFunction::HwDeviceFunction.__init__)
    params = list(sig.parameters.keys())



def test_grm::deviceresource_is_not_abstract():
    assert not inspect.isabstract(GRM::DeviceResource)


def test_grm::deviceresource_constructor_exists():
    assert callable(GRM::DeviceResource.__init__)


def test_grm::deviceresource_constructor_args():
    sig = inspect.signature(GRM::DeviceResource.__init__)
    params = list(sig.parameters.keys())



def test_hwtiming::hwclock_is_not_abstract():
    assert not inspect.isabstract(HwTiming::HwClock)


def test_hwtiming::hwclock_constructor_exists():
    assert callable(HwTiming::HwClock.__init__)


def test_hwtiming::hwclock_constructor_args():
    sig = inspect.signature(HwTiming::HwClock.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory::memoryorganization_is_not_abstract():
    assert not inspect.isabstract(HwMemory::MemoryOrganization)


def test_hwmemory::memoryorganization_constructor_exists():
    assert callable(HwMemory::MemoryOrganization.__init__)


def test_hwmemory::memoryorganization_constructor_args():
    sig = inspect.signature(HwMemory::MemoryOrganization.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory_is_not_abstract():
    assert not inspect.isabstract(HwMemory)


def test_hwmemory_constructor_exists():
    assert callable(HwMemory.__init__)


def test_hwmemory_constructor_args():
    sig = inspect.signature(HwMemory.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwmemory::hwdrive_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::HwDrive)


def test_marte::hwmemory::hwdrive_constructor_exists():
    assert callable(MARTE::HwMemory::HwDrive.__init__)


def test_marte::hwmemory::hwdrive_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::HwDrive.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwmemory::hwcache_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::HwCache)


def test_marte::hwmemory::hwcache_constructor_exists():
    assert callable(MARTE::HwMemory::HwCache.__init__)


def test_marte::hwmemory::hwcache_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::HwCache.__init__)
    params = list(sig.parameters.keys())
    assert "writePolicy" in params, "Missing parameter 'writePolicy'"
    assert "repl_Policy" in params, "Missing parameter 'repl_Policy'"
    assert "type" in params, "Missing parameter 'type'"

def test_marte::hwmemory::hwcache_has_writePolicy():
    assert hasattr(MARTE::HwMemory::HwCache, "writePolicy")
    descriptor = None
    for klass in MARTE::HwMemory::HwCache.__mro__:
        if "writePolicy" in klass.__dict__:
            descriptor = klass.__dict__["writePolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwmemory::hwcache_has_repl_Policy():
    assert hasattr(MARTE::HwMemory::HwCache, "repl_Policy")
    descriptor = None
    for klass in MARTE::HwMemory::HwCache.__mro__:
        if "repl_Policy" in klass.__dict__:
            descriptor = klass.__dict__["repl_Policy"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwmemory::hwcache_has_type():
    assert hasattr(MARTE::HwMemory::HwCache, "type")
    descriptor = None
    for klass in MARTE::HwMemory::HwCache.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwregister::hwregister_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwRegister::HwRegister)


def test_marte::hwregister::hwregister_constructor_exists():
    assert callable(MARTE::HwRegister::HwRegister.__init__)


def test_marte::hwregister::hwregister_constructor_args():
    sig = inspect.signature(MARTE::HwRegister::HwRegister.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_marte::hwregister::hwregister_has_address():
    assert hasattr(MARTE::HwRegister::HwRegister, "address")
    descriptor = None
    for klass in MARTE::HwRegister::HwRegister.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwmemory::hwram_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::HwRAM)


def test_marte::hwmemory::hwram_constructor_exists():
    assert callable(MARTE::HwMemory::HwRAM.__init__)


def test_marte::hwmemory::hwram_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::HwRAM.__init__)
    params = list(sig.parameters.keys())
    assert "repl_Policy" in params, "Missing parameter 'repl_Policy'"
    assert "writePolicy" in params, "Missing parameter 'writePolicy'"

def test_marte::hwmemory::hwram_has_repl_Policy():
    assert hasattr(MARTE::HwMemory::HwRAM, "repl_Policy")
    descriptor = None
    for klass in MARTE::HwMemory::HwRAM.__mro__:
        if "repl_Policy" in klass.__dict__:
            descriptor = klass.__dict__["repl_Policy"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwmemory::hwram_has_writePolicy():
    assert hasattr(MARTE::HwMemory::HwRAM, "writePolicy")
    descriptor = None
    for klass in MARTE::HwMemory::HwRAM.__mro__:
        if "writePolicy" in klass.__dict__:
            descriptor = klass.__dict__["writePolicy"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwmemory::memoryorganization_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::MemoryOrganization)


def test_marte::hwmemory::memoryorganization_constructor_exists():
    assert callable(MARTE::HwMemory::MemoryOrganization.__init__)


def test_marte::hwmemory::memoryorganization_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::MemoryOrganization.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwmemory::cachestructure_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::CacheStructure)


def test_marte::hwmemory::cachestructure_constructor_exists():
    assert callable(MARTE::HwMemory::CacheStructure.__init__)


def test_marte::hwmemory::cachestructure_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::CacheStructure.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwmemory::hwrom_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::HwROM)


def test_marte::hwmemory::hwrom_constructor_exists():
    assert callable(MARTE::HwMemory::HwROM.__init__)


def test_marte::hwmemory::hwrom_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::HwROM.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_marte::hwmemory::hwrom_has_type():
    assert hasattr(MARTE::HwMemory::HwROM, "type")
    descriptor = None
    for klass in MARTE::HwMemory::HwROM.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwmemory::timing_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::Timing)


def test_marte::hwmemory::timing_constructor_exists():
    assert callable(MARTE::HwMemory::Timing.__init__)


def test_marte::hwmemory::timing_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::Timing.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory::timing_is_not_abstract():
    assert not inspect.isabstract(HwMemory::Timing)


def test_hwmemory::timing_constructor_exists():
    assert callable(HwMemory::Timing.__init__)


def test_hwmemory::timing_constructor_args():
    sig = inspect.signature(HwMemory::Timing.__init__)
    params = list(sig.parameters.keys())



def test_hwstoragemanager::hwstoragemanager_is_not_abstract():
    assert not inspect.isabstract(HwStorageManager::HwStorageManager)


def test_hwstoragemanager::hwstoragemanager_constructor_exists():
    assert callable(HwStorageManager::HwStorageManager.__init__)


def test_hwstoragemanager::hwstoragemanager_constructor_args():
    sig = inspect.signature(HwStorageManager::HwStorageManager.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory::hwmemory_is_not_abstract():
    assert not inspect.isabstract(HwMemory::HwMemory)


def test_hwmemory::hwmemory_constructor_exists():
    assert callable(HwMemory::HwMemory.__init__)


def test_hwmemory::hwmemory_constructor_args():
    sig = inspect.signature(HwMemory::HwMemory.__init__)
    params = list(sig.parameters.keys())



def test_grm::storageresource_is_not_abstract():
    assert not inspect.isabstract(GRM::StorageResource)


def test_grm::storageresource_constructor_exists():
    assert callable(GRM::StorageResource.__init__)


def test_grm::storageresource_constructor_args():
    sig = inspect.signature(GRM::StorageResource.__init__)
    params = list(sig.parameters.keys())



def test_hwprotocol::hwprotocol_is_not_abstract():
    assert not inspect.isabstract(HwProtocol::HwProtocol)


def test_hwprotocol::hwprotocol_constructor_exists():
    assert callable(HwProtocol::HwProtocol.__init__)


def test_hwprotocol::hwprotocol_constructor_args():
    sig = inspect.signature(HwProtocol::HwProtocol.__init__)
    params = list(sig.parameters.keys())



def test_hwendpoint_is_not_abstract():
    assert not inspect.isabstract(HwEndPoint)


def test_hwendpoint_constructor_exists():
    assert callable(HwEndPoint.__init__)


def test_hwendpoint_constructor_args():
    sig = inspect.signature(HwEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwio::hwpin_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwIO::HwPin)


def test_marte::hwio::hwpin_constructor_exists():
    assert callable(MARTE::HwIO::HwPin.__init__)


def test_marte::hwio::hwpin_constructor_args():
    sig = inspect.signature(MARTE::HwIO::HwPin.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwpackage::hwpackagepin_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPackage::HwPackagePin)


def test_marte::hwpackage::hwpackagepin_constructor_exists():
    assert callable(MARTE::HwPackage::HwPackagePin.__init__)


def test_marte::hwpackage::hwpackagepin_constructor_args():
    sig = inspect.signature(MARTE::HwPackage::HwPackagePin.__init__)
    params = list(sig.parameters.keys())
    assert "pinNo" in params, "Missing parameter 'pinNo'"
    assert "altNames" in params, "Missing parameter 'altNames'"

def test_marte::hwpackage::hwpackagepin_has_pinNo():
    assert hasattr(MARTE::HwPackage::HwPackagePin, "pinNo")
    descriptor = None
    for klass in MARTE::HwPackage::HwPackagePin.__mro__:
        if "pinNo" in klass.__dict__:
            descriptor = klass.__dict__["pinNo"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwpackage::hwpackagepin_has_altNames():
    assert hasattr(MARTE::HwPackage::HwPackagePin, "altNames")
    descriptor = None
    for klass in MARTE::HwPackage::HwPackagePin.__mro__:
        if "altNames" in klass.__dict__:
            descriptor = klass.__dict__["altNames"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwcommunication::hwport_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwCommunication::HwPort)


def test_marte::hwcommunication::hwport_constructor_exists():
    assert callable(MARTE::HwCommunication::HwPort.__init__)


def test_marte::hwcommunication::hwport_constructor_args():
    sig = inspect.signature(MARTE::HwCommunication::HwPort.__init__)
    params = list(sig.parameters.keys())



def test_grm::communicationendpoint_is_not_abstract():
    assert not inspect.isabstract(GRM::CommunicationEndPoint)


def test_grm::communicationendpoint_constructor_exists():
    assert callable(GRM::CommunicationEndPoint.__init__)


def test_grm::communicationendpoint_constructor_args():
    sig = inspect.signature(GRM::CommunicationEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_nfp::boolean_is_not_abstract():
    assert not inspect.isabstract(NFP::Boolean)


def test_nfp::boolean_constructor_exists():
    assert callable(NFP::Boolean.__init__)


def test_nfp::boolean_constructor_args():
    sig = inspect.signature(NFP::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_hwstoragemanager_is_not_abstract():
    assert not inspect.isabstract(HwStorageManager)


def test_hwstoragemanager_constructor_exists():
    assert callable(HwStorageManager.__init__)


def test_hwstoragemanager_constructor_args():
    sig = inspect.signature(HwStorageManager.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwstoragemanager::hwmmu_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwStorageManager::HwMMU)


def test_marte::hwstoragemanager::hwmmu_constructor_exists():
    assert callable(MARTE::HwStorageManager::HwMMU.__init__)


def test_marte::hwstoragemanager::hwmmu_constructor_args():
    sig = inspect.signature(MARTE::HwStorageManager::HwMMU.__init__)
    params = list(sig.parameters.keys())



def test_hwcommunication::hwcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(HwCommunication::HwCommunicationResource)


def test_hwcommunication::hwcommunicationresource_constructor_exists():
    assert callable(HwCommunication::HwCommunicationResource.__init__)


def test_hwcommunication::hwcommunicationresource_constructor_args():
    sig = inspect.signature(HwCommunication::HwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcommunication::hwendpoint_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwCommunication::HwEndPoint)


def test_marte::hwcommunication::hwendpoint_constructor_exists():
    assert callable(MARTE::HwCommunication::HwEndPoint.__init__)


def test_marte::hwcommunication::hwendpoint_constructor_args():
    sig = inspect.signature(MARTE::HwCommunication::HwEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_grm::communicationmedia_is_not_abstract():
    assert not inspect.isabstract(GRM::CommunicationMedia)


def test_grm::communicationmedia_constructor_exists():
    assert callable(GRM::CommunicationMedia.__init__)


def test_grm::communicationmedia_constructor_args():
    sig = inspect.signature(GRM::CommunicationMedia.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::interaction::swcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Interaction::SwCommunicationResource)


def test_marte::sw::interaction::swcommunicationresource_constructor_exists():
    assert callable(MARTE::SW::Interaction::SwCommunicationResource.__init__)


def test_marte::sw::interaction::swcommunicationresource_constructor_args():
    sig = inspect.signature(MARTE::SW::Interaction::SwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcommunication::hwmedia_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwCommunication::HwMedia)


def test_marte::hwcommunication::hwmedia_constructor_exists():
    assert callable(MARTE::HwCommunication::HwMedia.__init__)


def test_marte::hwcommunication::hwmedia_constructor_args():
    sig = inspect.signature(MARTE::HwCommunication::HwMedia.__init__)
    params = list(sig.parameters.keys())



def test_hwcommunication::hwmedia_is_not_abstract():
    assert not inspect.isabstract(HwCommunication::HwMedia)


def test_hwcommunication::hwmedia_constructor_exists():
    assert callable(HwCommunication::HwMedia.__init__)


def test_hwcommunication::hwmedia_constructor_args():
    sig = inspect.signature(HwCommunication::HwMedia.__init__)
    params = list(sig.parameters.keys())



def test_hwcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(HwCommunicationResource)


def test_hwcommunicationresource_constructor_exists():
    assert callable(HwCommunicationResource.__init__)


def test_hwcommunicationresource_constructor_args():
    sig = inspect.signature(HwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcommunication::hwarbiter_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwCommunication::HwArbiter)


def test_marte::hwcommunication::hwarbiter_constructor_exists():
    assert callable(MARTE::HwCommunication::HwArbiter.__init__)


def test_marte::hwcommunication::hwarbiter_constructor_args():
    sig = inspect.signature(MARTE::HwCommunication::HwArbiter.__init__)
    params = list(sig.parameters.keys())



def test_hwcommunication::hwport_is_not_abstract():
    assert not inspect.isabstract(HwCommunication::HwPort)


def test_hwcommunication::hwport_constructor_exists():
    assert callable(HwCommunication::HwPort.__init__)


def test_hwcommunication::hwport_constructor_args():
    sig = inspect.signature(HwCommunication::HwPort.__init__)
    params = list(sig.parameters.keys())



def test_hwio::hwpin_is_not_abstract():
    assert not inspect.isabstract(HwIO::HwPin)


def test_hwio::hwpin_constructor_exists():
    assert callable(HwIO::HwPin.__init__)


def test_hwio::hwpin_constructor_args():
    sig = inspect.signature(HwIO::HwPin.__init__)
    params = list(sig.parameters.keys())



def test_hwpackage::hwpackage_is_not_abstract():
    assert not inspect.isabstract(HwPackage::HwPackage)


def test_hwpackage::hwpackage_constructor_exists():
    assert callable(HwPackage::HwPackage.__init__)


def test_hwpackage::hwpackage_constructor_args():
    sig = inspect.signature(HwPackage::HwPackage.__init__)
    params = list(sig.parameters.keys())



def test_hwregister::hwregister_is_not_abstract():
    assert not inspect.isabstract(HwRegister::HwRegister)


def test_hwregister::hwregister_constructor_exists():
    assert callable(HwRegister::HwRegister.__init__)


def test_hwregister::hwregister_constructor_args():
    sig = inspect.signature(HwRegister::HwRegister.__init__)
    params = list(sig.parameters.keys())



def test_hwdevice::hwperipheral_is_not_abstract():
    assert not inspect.isabstract(HwDevice::HwPeripheral)


def test_hwdevice::hwperipheral_constructor_exists():
    assert callable(HwDevice::HwPeripheral.__init__)


def test_hwdevice::hwperipheral_constructor_args():
    sig = inspect.signature(HwDevice::HwPeripheral.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputing::hwprocessor_is_not_abstract():
    assert not inspect.isabstract(HwComputing::HwProcessor)


def test_hwcomputing::hwprocessor_constructor_exists():
    assert callable(HwComputing::HwProcessor.__init__)


def test_hwcomputing::hwprocessor_constructor_args():
    sig = inspect.signature(HwComputing::HwProcessor.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputing::hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(HwComputing::HwComputingResource)


def test_hwcomputing::hwcomputingresource_constructor_exists():
    assert callable(HwComputing::HwComputingResource.__init__)


def test_hwcomputing::hwcomputingresource_constructor_args():
    sig = inspect.signature(HwComputing::HwComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_hwmedia_is_not_abstract():
    assert not inspect.isabstract(HwMedia)


def test_hwmedia_constructor_exists():
    assert callable(HwMedia.__init__)


def test_hwmedia_constructor_args():
    sig = inspect.signature(HwMedia.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcommunication::hwconnection_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwCommunication::HwConnection)


def test_marte::hwcommunication::hwconnection_constructor_exists():
    assert callable(MARTE::HwCommunication::HwConnection.__init__)


def test_marte::hwcommunication::hwconnection_constructor_args():
    sig = inspect.signature(MARTE::HwCommunication::HwConnection.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwpackage::hwwire_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPackage::HwWire)


def test_marte::hwpackage::hwwire_constructor_exists():
    assert callable(MARTE::HwPackage::HwWire.__init__)


def test_marte::hwpackage::hwwire_constructor_args():
    sig = inspect.signature(MARTE::HwPackage::HwWire.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwio::hwline_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwIO::HwLine)


def test_marte::hwio::hwline_constructor_exists():
    assert callable(MARTE::HwIO::HwLine.__init__)


def test_marte::hwio::hwline_constructor_args():
    sig = inspect.signature(MARTE::HwIO::HwLine.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcommunication::hwbridge_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwCommunication::HwBridge)


def test_marte::hwcommunication::hwbridge_constructor_exists():
    assert callable(MARTE::HwCommunication::HwBridge.__init__)


def test_marte::hwcommunication::hwbridge_constructor_args():
    sig = inspect.signature(MARTE::HwCommunication::HwBridge.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcommunication::hwbus_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwCommunication::HwBus)


def test_marte::hwcommunication::hwbus_constructor_exists():
    assert callable(MARTE::HwCommunication::HwBus.__init__)


def test_marte::hwcommunication::hwbus_constructor_args():
    sig = inspect.signature(MARTE::HwCommunication::HwBus.__init__)
    params = list(sig.parameters.keys())



def test_hwcommunication::hwarbiter_is_not_abstract():
    assert not inspect.isabstract(HwCommunication::HwArbiter)


def test_hwcommunication::hwarbiter_constructor_exists():
    assert callable(HwCommunication::HwArbiter.__init__)


def test_hwcommunication::hwarbiter_constructor_args():
    sig = inspect.signature(HwCommunication::HwArbiter.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwstoragemanager::hwdma_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwStorageManager::HwDMA)


def test_marte::hwstoragemanager::hwdma_constructor_exists():
    assert callable(MARTE::HwStorageManager::HwDMA.__init__)


def test_marte::hwstoragemanager::hwdma_constructor_args():
    sig = inspect.signature(MARTE::HwStorageManager::HwDMA.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputing::pld::organization_is_not_abstract():
    assert not inspect.isabstract(HwComputing::PLD::Organization)


def test_hwcomputing::pld::organization_constructor_exists():
    assert callable(HwComputing::PLD::Organization.__init__)


def test_hwcomputing::pld::organization_constructor_args():
    sig = inspect.signature(HwComputing::PLD::Organization.__init__)
    params = list(sig.parameters.keys())



def test_nfp::string_is_not_abstract():
    assert not inspect.isabstract(NFP::String)


def test_nfp::string_constructor_exists():
    assert callable(NFP::String.__init__)


def test_nfp::string_constructor_args():
    sig = inspect.signature(NFP::String.__init__)
    params = list(sig.parameters.keys())



def test_hwresource_is_not_abstract():
    assert not inspect.isabstract(HwResource)


def test_hwresource_constructor_exists():
    assert callable(HwResource.__init__)


def test_hwresource_constructor_args():
    sig = inspect.signature(HwResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcommunication::hwcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwCommunication::HwCommunicationResource)


def test_marte::hwcommunication::hwcommunicationresource_constructor_exists():
    assert callable(MARTE::HwCommunication::HwCommunicationResource.__init__)


def test_marte::hwcommunication::hwcommunicationresource_constructor_args():
    sig = inspect.signature(MARTE::HwCommunication::HwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcomputing::hwbranchpredictor_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwBranchPredictor)


def test_marte::hwcomputing::hwbranchpredictor_constructor_exists():
    assert callable(MARTE::HwComputing::HwBranchPredictor.__init__)


def test_marte::hwcomputing::hwbranchpredictor_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwBranchPredictor.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwlayout::hwcomponent_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwLayout::HwComponent)


def test_marte::hwlayout::hwcomponent_constructor_exists():
    assert callable(MARTE::HwLayout::HwComponent.__init__)


def test_marte::hwlayout::hwcomponent_constructor_args():
    sig = inspect.signature(MARTE::HwLayout::HwComponent.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte::hwlayout::hwcomponent_has_kind():
    assert hasattr(MARTE::HwLayout::HwComponent, "kind")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwcomputing::hwisa_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwISA)


def test_marte::hwcomputing::hwisa_constructor_exists():
    assert callable(MARTE::HwComputing::HwISA.__init__)


def test_marte::hwcomputing::hwisa_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwISA.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_marte::hwcomputing::hwisa_has_type():
    assert hasattr(MARTE::HwComputing::HwISA, "type")
    descriptor = None
    for klass in MARTE::HwComputing::HwISA.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_nfp::frequencyinterval_is_not_abstract():
    assert not inspect.isabstract(NFP::FrequencyInterval)


def test_nfp::frequencyinterval_constructor_exists():
    assert callable(NFP::FrequencyInterval.__init__)


def test_nfp::frequencyinterval_constructor_args():
    sig = inspect.signature(NFP::FrequencyInterval.__init__)
    params = list(sig.parameters.keys())



def test_hwgeneral::hwresource_is_not_abstract():
    assert not inspect.isabstract(HwGeneral::HwResource)


def test_hwgeneral::hwresource_constructor_exists():
    assert callable(HwGeneral::HwResource.__init__)


def test_hwgeneral::hwresource_constructor_args():
    sig = inspect.signature(HwGeneral::HwResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwstoragemanager::hwstoragemanager_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwStorageManager::HwStorageManager)


def test_marte::hwstoragemanager::hwstoragemanager_constructor_exists():
    assert callable(MARTE::HwStorageManager::HwStorageManager.__init__)


def test_marte::hwstoragemanager::hwstoragemanager_constructor_args():
    sig = inspect.signature(MARTE::HwStorageManager::HwStorageManager.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwmemory::hwmemory_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::HwMemory)


def test_marte::hwmemory::hwmemory_constructor_exists():
    assert callable(MARTE::HwMemory::HwMemory.__init__)


def test_marte::hwmemory::hwmemory_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::HwMemory.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwtiming::hwtimingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwTiming::HwTimingResource)


def test_marte::hwtiming::hwtimingresource_constructor_exists():
    assert callable(MARTE::HwTiming::HwTimingResource.__init__)


def test_marte::hwtiming::hwtimingresource_constructor_args():
    sig = inspect.signature(MARTE::HwTiming::HwTimingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwdevice::hwdevice_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwDevice::HwDevice)


def test_marte::hwdevice::hwdevice_constructor_exists():
    assert callable(MARTE::HwDevice::HwDevice.__init__)


def test_marte::hwdevice::hwdevice_constructor_args():
    sig = inspect.signature(MARTE::HwDevice::HwDevice.__init__)
    params = list(sig.parameters.keys())



def test_hwstoragemanager::hwmmu_is_not_abstract():
    assert not inspect.isabstract(HwStorageManager::HwMMU)


def test_hwstoragemanager::hwmmu_constructor_exists():
    assert callable(HwStorageManager::HwMMU.__init__)


def test_hwstoragemanager::hwmmu_constructor_args():
    sig = inspect.signature(HwStorageManager::HwMMU.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory::hwcache_is_not_abstract():
    assert not inspect.isabstract(HwMemory::HwCache)


def test_hwmemory::hwcache_constructor_exists():
    assert callable(HwMemory::HwCache.__init__)


def test_hwmemory::hwcache_constructor_args():
    sig = inspect.signature(HwMemory::HwCache.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputing::hwbranchpredictor_is_not_abstract():
    assert not inspect.isabstract(HwComputing::HwBranchPredictor)


def test_hwcomputing::hwbranchpredictor_constructor_exists():
    assert callable(HwComputing::HwBranchPredictor.__init__)


def test_hwcomputing::hwbranchpredictor_constructor_args():
    sig = inspect.signature(HwComputing::HwBranchPredictor.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory::hwram_is_not_abstract():
    assert not inspect.isabstract(HwMemory::HwRAM)


def test_hwmemory::hwram_constructor_exists():
    assert callable(HwMemory::HwRAM.__init__)


def test_hwmemory::hwram_constructor_args():
    sig = inspect.signature(HwMemory::HwRAM.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(HwComputingResource)


def test_hwcomputingresource_constructor_exists():
    assert callable(HwComputingResource.__init__)


def test_hwcomputingresource_constructor_args():
    sig = inspect.signature(HwComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcomputing::hwasic_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwASIC)


def test_marte::hwcomputing::hwasic_constructor_exists():
    assert callable(MARTE::HwComputing::HwASIC.__init__)


def test_marte::hwcomputing::hwasic_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwASIC.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcomputing::hwmcu_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwMCU)


def test_marte::hwcomputing::hwmcu_constructor_exists():
    assert callable(MARTE::HwComputing::HwMCU.__init__)


def test_marte::hwcomputing::hwmcu_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwMCU.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcomputing::hwpld_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwPLD)


def test_marte::hwcomputing::hwpld_constructor_exists():
    assert callable(MARTE::HwComputing::HwPLD.__init__)


def test_marte::hwcomputing::hwpld_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwPLD.__init__)
    params = list(sig.parameters.keys())
    assert "technology" in params, "Missing parameter 'technology'"

def test_marte::hwcomputing::hwpld_has_technology():
    assert hasattr(MARTE::HwComputing::HwPLD, "technology")
    descriptor = None
    for klass in MARTE::HwComputing::HwPLD.__mro__:
        if "technology" in klass.__dict__:
            descriptor = klass.__dict__["technology"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwcomputing::hwprocessor_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwProcessor)


def test_marte::hwcomputing::hwprocessor_constructor_exists():
    assert callable(MARTE::HwComputing::HwProcessor.__init__)


def test_marte::hwcomputing::hwprocessor_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwProcessor.__init__)
    params = list(sig.parameters.keys())



def test_nfp::natural_is_not_abstract():
    assert not inspect.isabstract(NFP::Natural)


def test_nfp::natural_constructor_exists():
    assert callable(NFP::Natural.__init__)


def test_nfp::natural_constructor_args():
    sig = inspect.signature(NFP::Natural.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcomputing::pld::organization_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::PLD::Organization)


def test_marte::hwcomputing::pld::organization_constructor_exists():
    assert callable(MARTE::HwComputing::PLD::Organization.__init__)


def test_marte::hwcomputing::pld::organization_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::PLD::Organization.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"

def test_marte::hwcomputing::pld::organization_has_class_():
    assert hasattr(MARTE::HwComputing::PLD::Organization, "class_")
    descriptor = None
    for klass in MARTE::HwComputing::PLD::Organization.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_hwcomputing::hwisa_is_not_abstract():
    assert not inspect.isabstract(HwComputing::HwISA)


def test_hwcomputing::hwisa_constructor_exists():
    assert callable(HwComputing::HwISA.__init__)


def test_hwcomputing::hwisa_constructor_args():
    sig = inspect.signature(HwComputing::HwISA.__init__)
    params = list(sig.parameters.keys())



def test_marte::hlam::rtservice_is_not_abstract():
    assert not inspect.isabstract(MARTE::HLAM::RtService)


def test_marte::hlam::rtservice_constructor_exists():
    assert callable(MARTE::HLAM::RtService.__init__)


def test_marte::hlam::rtservice_constructor_args():
    sig = inspect.signature(MARTE::HLAM::RtService.__init__)
    params = list(sig.parameters.keys())
    assert "exeKind" in params, "Missing parameter 'exeKind'"
    assert "concPolicy" in params, "Missing parameter 'concPolicy'"
    assert "synchKind" in params, "Missing parameter 'synchKind'"
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"

def test_marte::hlam::rtservice_has_exeKind():
    assert hasattr(MARTE::HLAM::RtService, "exeKind")
    descriptor = None
    for klass in MARTE::HLAM::RtService.__mro__:
        if "exeKind" in klass.__dict__:
            descriptor = klass.__dict__["exeKind"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtservice_has_concPolicy():
    assert hasattr(MARTE::HLAM::RtService, "concPolicy")
    descriptor = None
    for klass in MARTE::HLAM::RtService.__mro__:
        if "concPolicy" in klass.__dict__:
            descriptor = klass.__dict__["concPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtservice_has_synchKind():
    assert hasattr(MARTE::HLAM::RtService, "synchKind")
    descriptor = None
    for klass in MARTE::HLAM::RtService.__mro__:
        if "synchKind" in klass.__dict__:
            descriptor = klass.__dict__["synchKind"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtservice_has_isAtomic():
    assert hasattr(MARTE::HLAM::RtService, "isAtomic")
    descriptor = None
    for klass in MARTE::HLAM::RtService.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)



def test_marte::hlam::rtaction_is_not_abstract():
    assert not inspect.isabstract(MARTE::HLAM::RtAction)


def test_marte::hlam::rtaction_constructor_exists():
    assert callable(MARTE::HLAM::RtAction.__init__)


def test_marte::hlam::rtaction_constructor_args():
    sig = inspect.signature(MARTE::HLAM::RtAction.__init__)
    params = list(sig.parameters.keys())
    assert "synchKind" in params, "Missing parameter 'synchKind'"
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"

def test_marte::hlam::rtaction_has_synchKind():
    assert hasattr(MARTE::HLAM::RtAction, "synchKind")
    descriptor = None
    for klass in MARTE::HLAM::RtAction.__mro__:
        if "synchKind" in klass.__dict__:
            descriptor = klass.__dict__["synchKind"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtaction_has_isAtomic():
    assert hasattr(MARTE::HLAM::RtAction, "isAtomic")
    descriptor = None
    for klass in MARTE::HLAM::RtAction.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)



def test_nfp::datetime_is_not_abstract():
    assert not inspect.isabstract(NFP::DateTime)


def test_nfp::datetime_constructor_exists():
    assert callable(NFP::DateTime.__init__)


def test_nfp::datetime_constructor_args():
    sig = inspect.signature(NFP::DateTime.__init__)
    params = list(sig.parameters.keys())



def test_hlam::marte::comment_is_not_abstract():
    assert not inspect.isabstract(HLAM::MARTE::Comment)


def test_hlam::marte::comment_constructor_exists():
    assert callable(HLAM::MARTE::Comment.__init__)


def test_hlam::marte::comment_constructor_args():
    sig = inspect.signature(HLAM::MARTE::Comment.__init__)
    params = list(sig.parameters.keys())



def test_nfp::percentage_is_not_abstract():
    assert not inspect.isabstract(NFP::Percentage)


def test_nfp::percentage_constructor_exists():
    assert callable(NFP::Percentage.__init__)


def test_nfp::percentage_constructor_args():
    sig = inspect.signature(NFP::Percentage.__init__)
    params = list(sig.parameters.keys())



def test_hlam::rtspecification_is_not_abstract():
    assert not inspect.isabstract(HLAM::RtSpecification)


def test_hlam::rtspecification_constructor_exists():
    assert callable(HLAM::RtSpecification.__init__)


def test_hlam::rtspecification_constructor_args():
    sig = inspect.signature(HLAM::RtSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hlam::marte::invocationaction_is_not_abstract():
    assert not inspect.isabstract(HLAM::MARTE::InvocationAction)


def test_hlam::marte::invocationaction_constructor_exists():
    assert callable(HLAM::MARTE::InvocationAction.__init__)


def test_hlam::marte::invocationaction_constructor_args():
    sig = inspect.signature(HLAM::MARTE::InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_hlam::marte::port_is_not_abstract():
    assert not inspect.isabstract(HLAM::MARTE::Port)


def test_hlam::marte::port_constructor_exists():
    assert callable(HLAM::MARTE::Port.__init__)


def test_hlam::marte::port_constructor_args():
    sig = inspect.signature(HLAM::MARTE::Port.__init__)
    params = list(sig.parameters.keys())



def test_hlam::marte::signal_is_not_abstract():
    assert not inspect.isabstract(HLAM::MARTE::Signal)


def test_hlam::marte::signal_constructor_exists():
    assert callable(HLAM::MARTE::Signal.__init__)


def test_hlam::marte::signal_constructor_args():
    sig = inspect.signature(HLAM::MARTE::Signal.__init__)
    params = list(sig.parameters.keys())



def test_hlam::marte::message_is_not_abstract():
    assert not inspect.isabstract(HLAM::MARTE::Message)


def test_hlam::marte::message_constructor_exists():
    assert callable(HLAM::MARTE::Message.__init__)


def test_hlam::marte::message_constructor_args():
    sig = inspect.signature(HLAM::MARTE::Message.__init__)
    params = list(sig.parameters.keys())



def test_hlam::marte::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(HLAM::MARTE::BehavioralFeature)


def test_hlam::marte::behavioralfeature_constructor_exists():
    assert callable(HLAM::MARTE::BehavioralFeature.__init__)


def test_hlam::marte::behavioralfeature_constructor_args():
    sig = inspect.signature(HLAM::MARTE::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_marte::hlam::rtfeature_is_not_abstract():
    assert not inspect.isabstract(MARTE::HLAM::RtFeature)


def test_marte::hlam::rtfeature_constructor_exists():
    assert callable(MARTE::HLAM::RtFeature.__init__)


def test_marte::hlam::rtfeature_constructor_args():
    sig = inspect.signature(MARTE::HLAM::RtFeature.__init__)
    params = list(sig.parameters.keys())



def test_marte::hlam::ppunit_is_not_abstract():
    assert not inspect.isabstract(MARTE::HLAM::PpUnit)


def test_marte::hlam::ppunit_constructor_exists():
    assert callable(MARTE::HLAM::PpUnit.__init__)


def test_marte::hlam::ppunit_constructor_args():
    sig = inspect.signature(MARTE::HLAM::PpUnit.__init__)
    params = list(sig.parameters.keys())
    assert "concPolicy" in params, "Missing parameter 'concPolicy'"

def test_marte::hlam::ppunit_has_concPolicy():
    assert hasattr(MARTE::HLAM::PpUnit, "concPolicy")
    descriptor = None
    for klass in MARTE::HLAM::PpUnit.__mro__:
        if "concPolicy" in klass.__dict__:
            descriptor = klass.__dict__["concPolicy"]
            break
    assert isinstance(descriptor, property)



def test_time::timedinstantobservation_is_not_abstract():
    assert not inspect.isabstract(Time::TimedInstantObservation)


def test_time::timedinstantobservation_constructor_exists():
    assert callable(Time::TimedInstantObservation.__init__)


def test_time::timedinstantobservation_constructor_args():
    sig = inspect.signature(Time::TimedInstantObservation.__init__)
    params = list(sig.parameters.keys())



def test_arrivalpattern_is_not_abstract():
    assert not inspect.isabstract(ArrivalPattern)


def test_arrivalpattern_constructor_exists():
    assert callable(ArrivalPattern.__init__)


def test_arrivalpattern_constructor_args():
    sig = inspect.signature(ArrivalPattern.__init__)
    params = list(sig.parameters.keys())



def test_utilitytype_is_not_abstract():
    assert not inspect.isabstract(UtilityType)


def test_utilitytype_constructor_exists():
    assert callable(UtilityType.__init__)


def test_utilitytype_constructor_args():
    sig = inspect.signature(UtilityType.__init__)
    params = list(sig.parameters.keys())



def test_marte::hlam::rtspecification_is_not_abstract():
    assert not inspect.isabstract(MARTE::HLAM::RtSpecification)


def test_marte::hlam::rtspecification_constructor_exists():
    assert callable(MARTE::HLAM::RtSpecification.__init__)


def test_marte::hlam::rtspecification_constructor_args():
    sig = inspect.signature(MARTE::HLAM::RtSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hlam::marte::operation_is_not_abstract():
    assert not inspect.isabstract(HLAM::MARTE::Operation)


def test_hlam::marte::operation_constructor_exists():
    assert callable(HLAM::MARTE::Operation.__init__)


def test_hlam::marte::operation_constructor_args():
    sig = inspect.signature(HLAM::MARTE::Operation.__init__)
    params = list(sig.parameters.keys())



def test_hlam::marte::behavior_is_not_abstract():
    assert not inspect.isabstract(HLAM::MARTE::Behavior)


def test_hlam::marte::behavior_constructor_exists():
    assert callable(HLAM::MARTE::Behavior.__init__)


def test_hlam::marte::behavior_constructor_args():
    sig = inspect.signature(HLAM::MARTE::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_marte::hlam::rtunit_is_not_abstract():
    assert not inspect.isabstract(MARTE::HLAM::RtUnit)


def test_marte::hlam::rtunit_constructor_exists():
    assert callable(MARTE::HLAM::RtUnit.__init__)


def test_marte::hlam::rtunit_constructor_args():
    sig = inspect.signature(MARTE::HLAM::RtUnit.__init__)
    params = list(sig.parameters.keys())
    assert "srPoolSize" in params, "Missing parameter 'srPoolSize'"
    assert "isMain" in params, "Missing parameter 'isMain'"
    assert "srPoolPolicy" in params, "Missing parameter 'srPoolPolicy'"
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"
    assert "queueSchedPolicy" in params, "Missing parameter 'queueSchedPolicy'"
    assert "queueSize" in params, "Missing parameter 'queueSize'"

def test_marte::hlam::rtunit_has_srPoolSize():
    assert hasattr(MARTE::HLAM::RtUnit, "srPoolSize")
    descriptor = None
    for klass in MARTE::HLAM::RtUnit.__mro__:
        if "srPoolSize" in klass.__dict__:
            descriptor = klass.__dict__["srPoolSize"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtunit_has_isMain():
    assert hasattr(MARTE::HLAM::RtUnit, "isMain")
    descriptor = None
    for klass in MARTE::HLAM::RtUnit.__mro__:
        if "isMain" in klass.__dict__:
            descriptor = klass.__dict__["isMain"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtunit_has_srPoolPolicy():
    assert hasattr(MARTE::HLAM::RtUnit, "srPoolPolicy")
    descriptor = None
    for klass in MARTE::HLAM::RtUnit.__mro__:
        if "srPoolPolicy" in klass.__dict__:
            descriptor = klass.__dict__["srPoolPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtunit_has_isDynamic():
    assert hasattr(MARTE::HLAM::RtUnit, "isDynamic")
    descriptor = None
    for klass in MARTE::HLAM::RtUnit.__mro__:
        if "isDynamic" in klass.__dict__:
            descriptor = klass.__dict__["isDynamic"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtunit_has_queueSchedPolicy():
    assert hasattr(MARTE::HLAM::RtUnit, "queueSchedPolicy")
    descriptor = None
    for klass in MARTE::HLAM::RtUnit.__mro__:
        if "queueSchedPolicy" in klass.__dict__:
            descriptor = klass.__dict__["queueSchedPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtunit_has_queueSize():
    assert hasattr(MARTE::HLAM::RtUnit, "queueSize")
    descriptor = None
    for klass in MARTE::HLAM::RtUnit.__mro__:
        if "queueSize" in klass.__dict__:
            descriptor = klass.__dict__["queueSize"]
            break
    assert isinstance(descriptor, property)



def test_marte::datatypes::tupletype_is_not_abstract():
    assert not inspect.isabstract(MARTE::DataTypes::TupleType)


def test_marte::datatypes::tupletype_constructor_exists():
    assert callable(MARTE::DataTypes::TupleType.__init__)


def test_marte::datatypes::tupletype_constructor_args():
    sig = inspect.signature(MARTE::DataTypes::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_marte::datatypes::choicetype_is_not_abstract():
    assert not inspect.isabstract(MARTE::DataTypes::ChoiceType)


def test_marte::datatypes::choicetype_constructor_exists():
    assert callable(MARTE::DataTypes::ChoiceType.__init__)


def test_marte::datatypes::choicetype_constructor_args():
    sig = inspect.signature(MARTE::DataTypes::ChoiceType.__init__)
    params = list(sig.parameters.keys())



def test_hlam::marte::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(HLAM::MARTE::BehavioredClassifier)


def test_hlam::marte::behavioredclassifier_constructor_exists():
    assert callable(HLAM::MARTE::BehavioredClassifier.__init__)


def test_hlam::marte::behavioredclassifier_constructor_args():
    sig = inspect.signature(HLAM::MARTE::BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::marte::property_is_not_abstract():
    assert not inspect.isabstract(DataTypes::MARTE::Property)


def test_datatypes::marte::property_constructor_exists():
    assert callable(DataTypes::MARTE::Property.__init__)


def test_datatypes::marte::property_constructor_args():
    sig = inspect.signature(DataTypes::MARTE::Property.__init__)
    params = list(sig.parameters.keys())



def test_marte::datatypes::boundedsubtype_is_not_abstract():
    assert not inspect.isabstract(MARTE::DataTypes::BoundedSubtype)


def test_marte::datatypes::boundedsubtype_constructor_exists():
    assert callable(MARTE::DataTypes::BoundedSubtype.__init__)


def test_marte::datatypes::boundedsubtype_constructor_args():
    sig = inspect.signature(MARTE::DataTypes::BoundedSubtype.__init__)
    params = list(sig.parameters.keys())
    assert "isMinOpen" in params, "Missing parameter 'isMinOpen'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "isMaxOpen" in params, "Missing parameter 'isMaxOpen'"
    assert "minValue" in params, "Missing parameter 'minValue'"

def test_marte::datatypes::boundedsubtype_has_isMinOpen():
    assert hasattr(MARTE::DataTypes::BoundedSubtype, "isMinOpen")
    descriptor = None
    for klass in MARTE::DataTypes::BoundedSubtype.__mro__:
        if "isMinOpen" in klass.__dict__:
            descriptor = klass.__dict__["isMinOpen"]
            break
    assert isinstance(descriptor, property)

def test_marte::datatypes::boundedsubtype_has_maxValue():
    assert hasattr(MARTE::DataTypes::BoundedSubtype, "maxValue")
    descriptor = None
    for klass in MARTE::DataTypes::BoundedSubtype.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_marte::datatypes::boundedsubtype_has_isMaxOpen():
    assert hasattr(MARTE::DataTypes::BoundedSubtype, "isMaxOpen")
    descriptor = None
    for klass in MARTE::DataTypes::BoundedSubtype.__mro__:
        if "isMaxOpen" in klass.__dict__:
            descriptor = klass.__dict__["isMaxOpen"]
            break
    assert isinstance(descriptor, property)

def test_marte::datatypes::boundedsubtype_has_minValue():
    assert hasattr(MARTE::DataTypes::BoundedSubtype, "minValue")
    descriptor = None
    for klass in MARTE::DataTypes::BoundedSubtype.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)



def test_variables::marte::namedelement_is_not_abstract():
    assert not inspect.isabstract(Variables::MARTE::NamedElement)


def test_variables::marte::namedelement_constructor_exists():
    assert callable(Variables::MARTE::NamedElement.__init__)


def test_variables::marte::namedelement_constructor_args():
    sig = inspect.signature(Variables::MARTE::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte::variables::expressioncontext_is_not_abstract():
    assert not inspect.isabstract(MARTE::Variables::ExpressionContext)


def test_marte::variables::expressioncontext_constructor_exists():
    assert callable(MARTE::Variables::ExpressionContext.__init__)


def test_marte::variables::expressioncontext_constructor_args():
    sig = inspect.signature(MARTE::Variables::ExpressionContext.__init__)
    params = list(sig.parameters.keys())



def test_variables::marte::property_is_not_abstract():
    assert not inspect.isabstract(Variables::MARTE::Property)


def test_variables::marte::property_constructor_exists():
    assert callable(Variables::MARTE::Property.__init__)


def test_variables::marte::property_constructor_args():
    sig = inspect.signature(Variables::MARTE::Property.__init__)
    params = list(sig.parameters.keys())



def test_marte::variables::var_is_not_abstract():
    assert not inspect.isabstract(MARTE::Variables::Var)


def test_marte::variables::var_constructor_exists():
    assert callable(MARTE::Variables::Var.__init__)


def test_marte::variables::var_constructor_args():
    sig = inspect.signature(MARTE::Variables::Var.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_marte::variables::var_has_dir():
    assert hasattr(MARTE::Variables::Var, "dir")
    descriptor = None
    for klass in MARTE::Variables::Var.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_rsm::marte::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(RSM::MARTE::MultiplicityElement)


def test_rsm::marte::multiplicityelement_constructor_exists():
    assert callable(RSM::MARTE::MultiplicityElement.__init__)


def test_rsm::marte::multiplicityelement_constructor_args():
    sig = inspect.signature(RSM::MARTE::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_marte::rsm::shaped_is_not_abstract():
    assert not inspect.isabstract(MARTE::RSM::Shaped)


def test_marte::rsm::shaped_constructor_exists():
    assert callable(MARTE::RSM::Shaped.__init__)


def test_marte::rsm::shaped_constructor_args():
    sig = inspect.signature(MARTE::RSM::Shaped.__init__)
    params = list(sig.parameters.keys())



def test_rsm::marte::connectorend_is_not_abstract():
    assert not inspect.isabstract(RSM::MARTE::ConnectorEnd)


def test_rsm::marte::connectorend_constructor_exists():
    assert callable(RSM::MARTE::ConnectorEnd.__init__)


def test_rsm::marte::connectorend_constructor_args():
    sig = inspect.signature(RSM::MARTE::ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_marte::datatypes::collectiontype_is_not_abstract():
    assert not inspect.isabstract(MARTE::DataTypes::CollectionType)


def test_marte::datatypes::collectiontype_constructor_exists():
    assert callable(MARTE::DataTypes::CollectionType.__init__)


def test_marte::datatypes::collectiontype_constructor_args():
    sig = inspect.signature(MARTE::DataTypes::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_marte::datatypes::intervaltype_is_not_abstract():
    assert not inspect.isabstract(MARTE::DataTypes::IntervalType)


def test_marte::datatypes::intervaltype_constructor_exists():
    assert callable(MARTE::DataTypes::IntervalType.__init__)


def test_marte::datatypes::intervaltype_constructor_args():
    sig = inspect.signature(MARTE::DataTypes::IntervalType.__init__)
    params = list(sig.parameters.keys())



def test_datatypes::marte::datatype_is_not_abstract():
    assert not inspect.isabstract(DataTypes::MARTE::DataType)


def test_datatypes::marte::datatype_constructor_exists():
    assert callable(DataTypes::MARTE::DataType.__init__)


def test_datatypes::marte::datatype_constructor_args():
    sig = inspect.signature(DataTypes::MARTE::DataType.__init__)
    params = list(sig.parameters.keys())



def test_tilerspecification_is_not_abstract():
    assert not inspect.isabstract(TilerSpecification)


def test_tilerspecification_constructor_exists():
    assert callable(TilerSpecification.__init__)


def test_tilerspecification_constructor_args():
    sig = inspect.signature(TilerSpecification.__init__)
    params = list(sig.parameters.keys())



def test_shapespecification_is_not_abstract():
    assert not inspect.isabstract(ShapeSpecification)


def test_shapespecification_constructor_exists():
    assert callable(ShapeSpecification.__init__)


def test_shapespecification_constructor_args():
    sig = inspect.signature(ShapeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_allocate_is_not_abstract():
    assert not inspect.isabstract(Allocate)


def test_allocate_constructor_exists():
    assert callable(Allocate.__init__)


def test_allocate_constructor_args():
    sig = inspect.signature(Allocate.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::concurrency::entrypoint_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Concurrency::EntryPoint)


def test_marte::sw::concurrency::entrypoint_constructor_exists():
    assert callable(MARTE::SW::Concurrency::EntryPoint.__init__)


def test_marte::sw::concurrency::entrypoint_constructor_args():
    sig = inspect.signature(MARTE::SW::Concurrency::EntryPoint.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"

def test_marte::sw::concurrency::entrypoint_has_isReentrant():
    assert hasattr(MARTE::SW::Concurrency::EntryPoint, "isReentrant")
    descriptor = None
    for klass in MARTE::SW::Concurrency::EntryPoint.__mro__:
        if "isReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isReentrant"]
            break
    assert isinstance(descriptor, property)



def test_marte::coreelements::modetransition_is_not_abstract():
    assert not inspect.isabstract(MARTE::CoreElements::ModeTransition)


def test_marte::coreelements::modetransition_constructor_exists():
    assert callable(MARTE::CoreElements::ModeTransition.__init__)


def test_marte::coreelements::modetransition_constructor_args():
    sig = inspect.signature(MARTE::CoreElements::ModeTransition.__init__)
    params = list(sig.parameters.keys())



def test_nfps::marte::enumeration_is_not_abstract():
    assert not inspect.isabstract(NFPs::MARTE::Enumeration)


def test_nfps::marte::enumeration_constructor_exists():
    assert callable(NFPs::MARTE::Enumeration.__init__)


def test_nfps::marte::enumeration_constructor_args():
    sig = inspect.signature(NFPs::MARTE::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_nfps::dimension_is_not_abstract():
    assert not inspect.isabstract(NFPs::Dimension)


def test_nfps::dimension_constructor_exists():
    assert callable(NFPs::Dimension.__init__)


def test_nfps::dimension_constructor_args():
    sig = inspect.signature(NFPs::Dimension.__init__)
    params = list(sig.parameters.keys())



def test_marte::nfps::dimension_is_not_abstract():
    assert not inspect.isabstract(MARTE::NFPs::Dimension)


def test_marte::nfps::dimension_constructor_exists():
    assert callable(MARTE::NFPs::Dimension.__init__)


def test_marte::nfps::dimension_constructor_args():
    sig = inspect.signature(MARTE::NFPs::Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "baseExponent" in params, "Missing parameter 'baseExponent'"

def test_marte::nfps::dimension_has_symbol():
    assert hasattr(MARTE::NFPs::Dimension, "symbol")
    descriptor = None
    for klass in MARTE::NFPs::Dimension.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_marte::nfps::dimension_has_baseExponent():
    assert hasattr(MARTE::NFPs::Dimension, "baseExponent")
    descriptor = None
    for klass in MARTE::NFPs::Dimension.__mro__:
        if "baseExponent" in klass.__dict__:
            descriptor = klass.__dict__["baseExponent"]
            break
    assert isinstance(descriptor, property)



def test_tupletype_is_not_abstract():
    assert not inspect.isabstract(TupleType)


def test_tupletype_constructor_exists():
    assert callable(TupleType.__init__)


def test_tupletype_constructor_args():
    sig = inspect.signature(TupleType.__init__)
    params = list(sig.parameters.keys())



def test_marte::nfps::nfptype_is_not_abstract():
    assert not inspect.isabstract(MARTE::NFPs::NfpType)


def test_marte::nfps::nfptype_constructor_exists():
    assert callable(MARTE::NFPs::NfpType.__init__)


def test_marte::nfps::nfptype_constructor_args():
    sig = inspect.signature(MARTE::NFPs::NfpType.__init__)
    params = list(sig.parameters.keys())



def test_coreelements::mode_is_not_abstract():
    assert not inspect.isabstract(CoreElements::Mode)


def test_coreelements::mode_constructor_exists():
    assert callable(CoreElements::Mode.__init__)


def test_coreelements::mode_constructor_args():
    sig = inspect.signature(CoreElements::Mode.__init__)
    params = list(sig.parameters.keys())



def test_nfps::marte::constraint_is_not_abstract():
    assert not inspect.isabstract(NFPs::MARTE::Constraint)


def test_nfps::marte::constraint_constructor_exists():
    assert callable(NFPs::MARTE::Constraint.__init__)


def test_nfps::marte::constraint_constructor_args():
    sig = inspect.signature(NFPs::MARTE::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_marte::nfps::nfpconstraint_is_not_abstract():
    assert not inspect.isabstract(MARTE::NFPs::NfpConstraint)


def test_marte::nfps::nfpconstraint_constructor_exists():
    assert callable(MARTE::NFPs::NfpConstraint.__init__)


def test_marte::nfps::nfpconstraint_constructor_args():
    sig = inspect.signature(MARTE::NFPs::NfpConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte::nfps::nfpconstraint_has_kind():
    assert hasattr(MARTE::NFPs::NfpConstraint, "kind")
    descriptor = None
    for klass in MARTE::NFPs::NfpConstraint.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_nfps::marte::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(NFPs::MARTE::EnumerationLiteral)


def test_nfps::marte::enumerationliteral_constructor_exists():
    assert callable(NFPs::MARTE::EnumerationLiteral.__init__)


def test_nfps::marte::enumerationliteral_constructor_args():
    sig = inspect.signature(NFPs::MARTE::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_coreelements::marte::package_is_not_abstract():
    assert not inspect.isabstract(CoreElements::MARTE::Package)


def test_coreelements::marte::package_constructor_exists():
    assert callable(CoreElements::MARTE::Package.__init__)


def test_coreelements::marte::package_constructor_args():
    sig = inspect.signature(CoreElements::MARTE::Package.__init__)
    params = list(sig.parameters.keys())



def test_coreelements::marte::structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(CoreElements::MARTE::StructuredClassifier)


def test_coreelements::marte::structuredclassifier_constructor_exists():
    assert callable(CoreElements::MARTE::StructuredClassifier.__init__)


def test_coreelements::marte::structuredclassifier_constructor_args():
    sig = inspect.signature(CoreElements::MARTE::StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_marte::coreelements::configuration_is_not_abstract():
    assert not inspect.isabstract(MARTE::CoreElements::Configuration)


def test_marte::coreelements::configuration_constructor_exists():
    assert callable(MARTE::CoreElements::Configuration.__init__)


def test_marte::coreelements::configuration_constructor_args():
    sig = inspect.signature(MARTE::CoreElements::Configuration.__init__)
    params = list(sig.parameters.keys())



def test_coreelements::marte::statemachine_is_not_abstract():
    assert not inspect.isabstract(CoreElements::MARTE::StateMachine)


def test_coreelements::marte::statemachine_constructor_exists():
    assert callable(CoreElements::MARTE::StateMachine.__init__)


def test_coreelements::marte::statemachine_constructor_args():
    sig = inspect.signature(CoreElements::MARTE::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_marte::coreelements::modebehavior_is_not_abstract():
    assert not inspect.isabstract(MARTE::CoreElements::ModeBehavior)


def test_marte::coreelements::modebehavior_constructor_exists():
    assert callable(MARTE::CoreElements::ModeBehavior.__init__)


def test_marte::coreelements::modebehavior_constructor_args():
    sig = inspect.signature(MARTE::CoreElements::ModeBehavior.__init__)
    params = list(sig.parameters.keys())



def test_marte::nfps::nfp_is_not_abstract():
    assert not inspect.isabstract(MARTE::NFPs::Nfp)


def test_marte::nfps::nfp_constructor_exists():
    assert callable(MARTE::NFPs::Nfp.__init__)


def test_marte::nfps::nfp_constructor_args():
    sig = inspect.signature(MARTE::NFPs::Nfp.__init__)
    params = list(sig.parameters.keys())



def test_nfps::unit_is_not_abstract():
    assert not inspect.isabstract(NFPs::Unit)


def test_nfps::unit_constructor_exists():
    assert callable(NFPs::Unit.__init__)


def test_nfps::unit_constructor_args():
    sig = inspect.signature(NFPs::Unit.__init__)
    params = list(sig.parameters.keys())



def test_marte::nfps::unit_is_not_abstract():
    assert not inspect.isabstract(MARTE::NFPs::Unit)


def test_marte::nfps::unit_constructor_exists():
    assert callable(MARTE::NFPs::Unit.__init__)


def test_marte::nfps::unit_constructor_args():
    sig = inspect.signature(MARTE::NFPs::Unit.__init__)
    params = list(sig.parameters.keys())
    assert "convFactor" in params, "Missing parameter 'convFactor'"
    assert "offsetFactor" in params, "Missing parameter 'offsetFactor'"

def test_marte::nfps::unit_has_convFactor():
    assert hasattr(MARTE::NFPs::Unit, "convFactor")
    descriptor = None
    for klass in MARTE::NFPs::Unit.__mro__:
        if "convFactor" in klass.__dict__:
            descriptor = klass.__dict__["convFactor"]
            break
    assert isinstance(descriptor, property)

def test_marte::nfps::unit_has_offsetFactor():
    assert hasattr(MARTE::NFPs::Unit, "offsetFactor")
    descriptor = None
    for klass in MARTE::NFPs::Unit.__mro__:
        if "offsetFactor" in klass.__dict__:
            descriptor = klass.__dict__["offsetFactor"]
            break
    assert isinstance(descriptor, property)



def test_nfps::marte::property_is_not_abstract():
    assert not inspect.isabstract(NFPs::MARTE::Property)


def test_nfps::marte::property_constructor_exists():
    assert callable(NFPs::MARTE::Property.__init__)


def test_nfps::marte::property_constructor_args():
    sig = inspect.signature(NFPs::MARTE::Property.__init__)
    params = list(sig.parameters.keys())



def test_marte::rsm::distribute_is_not_abstract():
    assert not inspect.isabstract(MARTE::RSM::Distribute)


def test_marte::rsm::distribute_constructor_exists():
    assert callable(MARTE::RSM::Distribute.__init__)


def test_marte::rsm::distribute_constructor_args():
    sig = inspect.signature(MARTE::RSM::Distribute.__init__)
    params = list(sig.parameters.keys())



def test_integervector_is_not_abstract():
    assert not inspect.isabstract(IntegerVector)


def test_integervector_constructor_exists():
    assert callable(IntegerVector.__init__)


def test_integervector_constructor_args():
    sig = inspect.signature(IntegerVector.__init__)
    params = list(sig.parameters.keys())



def test_linktopology_is_not_abstract():
    assert not inspect.isabstract(LinkTopology)


def test_linktopology_constructor_exists():
    assert callable(LinkTopology.__init__)


def test_linktopology_constructor_args():
    sig = inspect.signature(LinkTopology.__init__)
    params = list(sig.parameters.keys())



def test_marte::rsm::reshape_is_not_abstract():
    assert not inspect.isabstract(MARTE::RSM::Reshape)


def test_marte::rsm::reshape_constructor_exists():
    assert callable(MARTE::RSM::Reshape.__init__)


def test_marte::rsm::reshape_constructor_args():
    sig = inspect.signature(MARTE::RSM::Reshape.__init__)
    params = list(sig.parameters.keys())



def test_marte::rsm::interrepetition_is_not_abstract():
    assert not inspect.isabstract(MARTE::RSM::InterRepetition)


def test_marte::rsm::interrepetition_constructor_exists():
    assert callable(MARTE::RSM::InterRepetition.__init__)


def test_marte::rsm::interrepetition_constructor_args():
    sig = inspect.signature(MARTE::RSM::InterRepetition.__init__)
    params = list(sig.parameters.keys())
    assert "isModulo" in params, "Missing parameter 'isModulo'"

def test_marte::rsm::interrepetition_has_isModulo():
    assert hasattr(MARTE::RSM::InterRepetition, "isModulo")
    descriptor = None
    for klass in MARTE::RSM::InterRepetition.__mro__:
        if "isModulo" in klass.__dict__:
            descriptor = klass.__dict__["isModulo"]
            break
    assert isinstance(descriptor, property)



def test_marte::rsm::defaultlink_is_not_abstract():
    assert not inspect.isabstract(MARTE::RSM::DefaultLink)


def test_marte::rsm::defaultlink_constructor_exists():
    assert callable(MARTE::RSM::DefaultLink.__init__)


def test_marte::rsm::defaultlink_constructor_args():
    sig = inspect.signature(MARTE::RSM::DefaultLink.__init__)
    params = list(sig.parameters.keys())



def test_rsm::marte::connector_is_not_abstract():
    assert not inspect.isabstract(RSM::MARTE::Connector)


def test_rsm::marte::connector_constructor_exists():
    assert callable(RSM::MARTE::Connector.__init__)


def test_rsm::marte::connector_constructor_args():
    sig = inspect.signature(RSM::MARTE::Connector.__init__)
    params = list(sig.parameters.keys())



def test_marte::rsm::linktopology_is_not_abstract():
    assert not inspect.isabstract(MARTE::RSM::LinkTopology)


def test_marte::rsm::linktopology_constructor_exists():
    assert callable(MARTE::RSM::LinkTopology.__init__)


def test_marte::rsm::linktopology_constructor_args():
    sig = inspect.signature(MARTE::RSM::LinkTopology.__init__)
    params = list(sig.parameters.keys())



def test_integermatrix_is_not_abstract():
    assert not inspect.isabstract(IntegerMatrix)


def test_integermatrix_constructor_exists():
    assert callable(IntegerMatrix.__init__)


def test_integermatrix_constructor_args():
    sig = inspect.signature(IntegerMatrix.__init__)
    params = list(sig.parameters.keys())



def test_marte::rsm::tiler_is_not_abstract():
    assert not inspect.isabstract(MARTE::RSM::Tiler)


def test_marte::rsm::tiler_constructor_exists():
    assert callable(MARTE::RSM::Tiler.__init__)


def test_marte::rsm::tiler_constructor_args():
    sig = inspect.signature(MARTE::RSM::Tiler.__init__)
    params = list(sig.parameters.keys())



def test_nfp::energy_is_not_abstract():
    assert not inspect.isabstract(NFP::Energy)


def test_nfp::energy_constructor_exists():
    assert callable(NFP::Energy.__init__)


def test_nfp::energy_constructor_args():
    sig = inspect.signature(NFP::Energy.__init__)
    params = list(sig.parameters.keys())



def test_nfp::power_is_not_abstract():
    assert not inspect.isabstract(NFP::Power)


def test_nfp::power_constructor_exists():
    assert callable(NFP::Power.__init__)


def test_nfp::power_constructor_args():
    sig = inspect.signature(NFP::Power.__init__)
    params = list(sig.parameters.keys())



def test_nfp::datasize_is_not_abstract():
    assert not inspect.isabstract(NFP::DataSize)


def test_nfp::datasize_constructor_exists():
    assert callable(NFP::DataSize.__init__)


def test_nfp::datasize_constructor_args():
    sig = inspect.signature(NFP::DataSize.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::resourceusage_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::ResourceUsage)


def test_marte::grm::resourceusage_constructor_exists():
    assert callable(MARTE::GRM::ResourceUsage.__init__)


def test_marte::grm::resourceusage_constructor_args():
    sig = inspect.signature(MARTE::GRM::ResourceUsage.__init__)
    params = list(sig.parameters.keys())



def test_grservice_is_not_abstract():
    assert not inspect.isabstract(GrService)


def test_grservice_constructor_exists():
    assert callable(GrService.__init__)


def test_grservice_constructor_args():
    sig = inspect.signature(GrService.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwgeneral::hwresourceservice_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwGeneral::HwResourceService)


def test_marte::hwgeneral::hwresourceservice_constructor_exists():
    assert callable(MARTE::HwGeneral::HwResourceService.__init__)


def test_marte::hwgeneral::hwresourceservice_constructor_args():
    sig = inspect.signature(MARTE::HwGeneral::HwResourceService.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::resourcecore::swaccessservice_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::ResourceCore::SwAccessService)


def test_marte::sw::resourcecore::swaccessservice_constructor_exists():
    assert callable(MARTE::SW::ResourceCore::SwAccessService.__init__)


def test_marte::sw::resourcecore::swaccessservice_constructor_args():
    sig = inspect.signature(MARTE::SW::ResourceCore::SwAccessService.__init__)
    params = list(sig.parameters.keys())
    assert "isModifier" in params, "Missing parameter 'isModifier'"

def test_marte::sw::resourcecore::swaccessservice_has_isModifier():
    assert hasattr(MARTE::SW::ResourceCore::SwAccessService, "isModifier")
    descriptor = None
    for klass in MARTE::SW::ResourceCore::SwAccessService.__mro__:
        if "isModifier" in klass.__dict__:
            descriptor = klass.__dict__["isModifier"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::acquire_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::Acquire)


def test_marte::grm::acquire_constructor_exists():
    assert callable(MARTE::GRM::Acquire.__init__)


def test_marte::grm::acquire_constructor_args():
    sig = inspect.signature(MARTE::GRM::Acquire.__init__)
    params = list(sig.parameters.keys())
    assert "isBlocking" in params, "Missing parameter 'isBlocking'"

def test_marte::grm::acquire_has_isBlocking():
    assert hasattr(MARTE::GRM::Acquire, "isBlocking")
    descriptor = None
    for klass in MARTE::GRM::Acquire.__mro__:
        if "isBlocking" in klass.__dict__:
            descriptor = klass.__dict__["isBlocking"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::release_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::Release)


def test_marte::grm::release_constructor_exists():
    assert callable(MARTE::GRM::Release.__init__)


def test_marte::grm::release_constructor_args():
    sig = inspect.signature(MARTE::GRM::Release.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::collaborationuse_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::CollaborationUse)


def test_grm::marte::collaborationuse_constructor_exists():
    assert callable(GRM::MARTE::CollaborationUse.__init__)


def test_grm::marte::collaborationuse_constructor_args():
    sig = inspect.signature(GRM::MARTE::CollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::collaboration_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::Collaboration)


def test_grm::marte::collaboration_constructor_exists():
    assert callable(GRM::MARTE::Collaboration.__init__)


def test_grm::marte::collaboration_constructor_args():
    sig = inspect.signature(GRM::MARTE::Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::behavior_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::Behavior)


def test_grm::marte::behavior_constructor_exists():
    assert callable(GRM::MARTE::Behavior.__init__)


def test_grm::marte::behavior_constructor_args():
    sig = inspect.signature(GRM::MARTE::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::BehavioralFeature)


def test_grm::marte::behavioralfeature_constructor_exists():
    assert callable(GRM::MARTE::BehavioralFeature.__init__)


def test_grm::marte::behavioralfeature_constructor_args():
    sig = inspect.signature(GRM::MARTE::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::executionspecification_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::ExecutionSpecification)


def test_grm::marte::executionspecification_constructor_exists():
    assert callable(GRM::MARTE::ExecutionSpecification.__init__)


def test_grm::marte::executionspecification_constructor_args():
    sig = inspect.signature(GRM::MARTE::ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_grm::resource_is_not_abstract():
    assert not inspect.isabstract(GRM::Resource)


def test_grm::resource_constructor_exists():
    assert callable(GRM::Resource.__init__)


def test_grm::resource_constructor_args():
    sig = inspect.signature(GRM::Resource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::grservice_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::GrService)


def test_marte::grm::grservice_constructor_exists():
    assert callable(MARTE::GRM::GrService.__init__)


def test_marte::grm::grservice_constructor_args():
    sig = inspect.signature(MARTE::GRM::GrService.__init__)
    params = list(sig.parameters.keys())



def test_grm::resourceusage_is_not_abstract():
    assert not inspect.isabstract(GRM::ResourceUsage)


def test_grm::resourceusage_constructor_exists():
    assert callable(GRM::ResourceUsage.__init__)


def test_grm::resourceusage_constructor_args():
    sig = inspect.signature(GRM::ResourceUsage.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gascenario_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaScenario)


def test_marte::gqam::gascenario_constructor_exists():
    assert callable(MARTE::GQAM::GaScenario.__init__)


def test_marte::gqam::gascenario_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaScenario.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::namedelement_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::NamedElement)


def test_grm::marte::namedelement_constructor_exists():
    assert callable(GRM::MARTE::NamedElement.__init__)


def test_grm::marte::namedelement_constructor_args():
    sig = inspect.signature(GRM::MARTE::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_nfp::datatxrate_is_not_abstract():
    assert not inspect.isabstract(NFP::DataTxRate)


def test_nfp::datatxrate_constructor_exists():
    assert callable(NFP::DataTxRate.__init__)


def test_nfp::datatxrate_constructor_args():
    sig = inspect.signature(NFP::DataTxRate.__init__)
    params = list(sig.parameters.keys())



def test_nfp::duration_is_not_abstract():
    assert not inspect.isabstract(NFP::Duration)


def test_nfp::duration_constructor_exists():
    assert callable(NFP::Duration.__init__)


def test_nfp::duration_constructor_args():
    sig = inspect.signature(NFP::Duration.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::connector_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::Connector)


def test_grm::marte::connector_constructor_exists():
    assert callable(GRM::MARTE::Connector.__init__)


def test_grm::marte::connector_constructor_args():
    sig = inspect.signature(GRM::MARTE::Connector.__init__)
    params = list(sig.parameters.keys())



def test_scheduler_is_not_abstract():
    assert not inspect.isabstract(Scheduler)


def test_scheduler_constructor_exists():
    assert callable(Scheduler.__init__)


def test_scheduler_constructor_args():
    sig = inspect.signature(Scheduler.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::secondaryscheduler_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::SecondaryScheduler)


def test_marte::grm::secondaryscheduler_constructor_exists():
    assert callable(MARTE::GRM::SecondaryScheduler.__init__)


def test_marte::grm::secondaryscheduler_constructor_args():
    sig = inspect.signature(MARTE::GRM::SecondaryScheduler.__init__)
    params = list(sig.parameters.keys())



def test_grm::secondaryscheduler_is_not_abstract():
    assert not inspect.isabstract(GRM::SecondaryScheduler)


def test_grm::secondaryscheduler_constructor_exists():
    assert callable(GRM::SecondaryScheduler.__init__)


def test_grm::secondaryscheduler_constructor_args():
    sig = inspect.signature(GRM::SecondaryScheduler.__init__)
    params = list(sig.parameters.keys())



def test_schedparameters_is_not_abstract():
    assert not inspect.isabstract(SchedParameters)


def test_schedparameters_constructor_exists():
    assert callable(SchedParameters.__init__)


def test_schedparameters_constructor_args():
    sig = inspect.signature(SchedParameters.__init__)
    params = list(sig.parameters.keys())



def test_timingresource_is_not_abstract():
    assert not inspect.isabstract(TimingResource)


def test_timingresource_constructor_exists():
    assert callable(TimingResource.__init__)


def test_timingresource_constructor_args():
    sig = inspect.signature(TimingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::timerresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::TimerResource)


def test_marte::grm::timerresource_constructor_exists():
    assert callable(MARTE::GRM::TimerResource.__init__)


def test_marte::grm::timerresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::TimerResource.__init__)
    params = list(sig.parameters.keys())
    assert "isPeriodic" in params, "Missing parameter 'isPeriodic'"

def test_marte::grm::timerresource_has_isPeriodic():
    assert hasattr(MARTE::GRM::TimerResource, "isPeriodic")
    descriptor = None
    for klass in MARTE::GRM::TimerResource.__mro__:
        if "isPeriodic" in klass.__dict__:
            descriptor = klass.__dict__["isPeriodic"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::clockresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::ClockResource)


def test_marte::grm::clockresource_constructor_exists():
    assert callable(MARTE::GRM::ClockResource.__init__)


def test_marte::grm::clockresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::ClockResource.__init__)
    params = list(sig.parameters.keys())



def test_grm::scheduler_is_not_abstract():
    assert not inspect.isabstract(GRM::Scheduler)


def test_grm::scheduler_constructor_exists():
    assert callable(GRM::Scheduler.__init__)


def test_grm::scheduler_constructor_args():
    sig = inspect.signature(GRM::Scheduler.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gacommhost_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaCommHost)


def test_marte::gqam::gacommhost_constructor_exists():
    assert callable(MARTE::GQAM::GaCommHost.__init__)


def test_marte::gqam::gacommhost_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaCommHost.__init__)
    params = list(sig.parameters.keys())



def test_nfp::real_is_not_abstract():
    assert not inspect.isabstract(NFP::Real)


def test_nfp::real_constructor_exists():
    assert callable(NFP::Real.__init__)


def test_nfp::real_constructor_args():
    sig = inspect.signature(NFP::Real.__init__)
    params = list(sig.parameters.keys())



def test_grm::schedulableresource_is_not_abstract():
    assert not inspect.isabstract(GRM::SchedulableResource)


def test_grm::schedulableresource_constructor_exists():
    assert callable(GRM::SchedulableResource.__init__)


def test_grm::schedulableresource_constructor_args():
    sig = inspect.signature(GRM::SchedulableResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::concurrency::swschedulableresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Concurrency::SwSchedulableResource)


def test_marte::sw::concurrency::swschedulableresource_constructor_exists():
    assert callable(MARTE::SW::Concurrency::SwSchedulableResource.__init__)


def test_marte::sw::concurrency::swschedulableresource_constructor_args():
    sig = inspect.signature(MARTE::SW::Concurrency::SwSchedulableResource.__init__)
    params = list(sig.parameters.keys())
    assert "isPreemptable" in params, "Missing parameter 'isPreemptable'"
    assert "isStaticSchedulingFeature" in params, "Missing parameter 'isStaticSchedulingFeature'"

def test_marte::sw::concurrency::swschedulableresource_has_isPreemptable():
    assert hasattr(MARTE::SW::Concurrency::SwSchedulableResource, "isPreemptable")
    descriptor = None
    for klass in MARTE::SW::Concurrency::SwSchedulableResource.__mro__:
        if "isPreemptable" in klass.__dict__:
            descriptor = klass.__dict__["isPreemptable"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::concurrency::swschedulableresource_has_isStaticSchedulingFeature():
    assert hasattr(MARTE::SW::Concurrency::SwSchedulableResource, "isStaticSchedulingFeature")
    descriptor = None
    for klass in MARTE::SW::Concurrency::SwSchedulableResource.__mro__:
        if "isStaticSchedulingFeature" in klass.__dict__:
            descriptor = klass.__dict__["isStaticSchedulingFeature"]
            break
    assert isinstance(descriptor, property)



def test_grm::mutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(GRM::MutualExclusionResource)


def test_grm::mutualexclusionresource_constructor_exists():
    assert callable(GRM::MutualExclusionResource.__init__)


def test_grm::mutualexclusionresource_constructor_args():
    sig = inspect.signature(GRM::MutualExclusionResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::interaction::swmutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::Interaction::SwMutualExclusionResource)


def test_marte::sw::interaction::swmutualexclusionresource_constructor_exists():
    assert callable(MARTE::SW::Interaction::SwMutualExclusionResource.__init__)


def test_marte::sw::interaction::swmutualexclusionresource_constructor_args():
    sig = inspect.signature(MARTE::SW::Interaction::SwMutualExclusionResource.__init__)
    params = list(sig.parameters.keys())
    assert "concurrentAccessProtocol" in params, "Missing parameter 'concurrentAccessProtocol'"
    assert "mechanism" in params, "Missing parameter 'mechanism'"

def test_marte::sw::interaction::swmutualexclusionresource_has_concurrentAccessProtocol():
    assert hasattr(MARTE::SW::Interaction::SwMutualExclusionResource, "concurrentAccessProtocol")
    descriptor = None
    for klass in MARTE::SW::Interaction::SwMutualExclusionResource.__mro__:
        if "concurrentAccessProtocol" in klass.__dict__:
            descriptor = klass.__dict__["concurrentAccessProtocol"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::interaction::swmutualexclusionresource_has_mechanism():
    assert hasattr(MARTE::SW::Interaction::SwMutualExclusionResource, "mechanism")
    descriptor = None
    for klass in MARTE::SW::Interaction::SwMutualExclusionResource.__mro__:
        if "mechanism" in klass.__dict__:
            descriptor = klass.__dict__["mechanism"]
            break
    assert isinstance(descriptor, property)



def test_grm::computingresource_is_not_abstract():
    assert not inspect.isabstract(GRM::ComputingResource)


def test_grm::computingresource_constructor_exists():
    assert callable(GRM::ComputingResource.__init__)


def test_grm::computingresource_constructor_args():
    sig = inspect.signature(GRM::ComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gaexechost_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaExecHost)


def test_marte::gqam::gaexechost_constructor_exists():
    assert callable(MARTE::GQAM::GaExecHost.__init__)


def test_marte::gqam::gaexechost_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaExecHost.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcomputing::hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwComputingResource)


def test_marte::hwcomputing::hwcomputingresource_constructor_exists():
    assert callable(MARTE::HwComputing::HwComputingResource.__init__)


def test_marte::hwcomputing::hwcomputingresource_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_grm::processingresource_is_not_abstract():
    assert not inspect.isabstract(GRM::ProcessingResource)


def test_grm::processingresource_constructor_exists():
    assert callable(GRM::ProcessingResource.__init__)


def test_grm::processingresource_constructor_args():
    sig = inspect.signature(GRM::ProcessingResource.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::OpaqueExpression)


def test_grm::marte::opaqueexpression_constructor_exists():
    assert callable(GRM::MARTE::OpaqueExpression.__init__)


def test_grm::marte::opaqueexpression_constructor_args():
    sig = inspect.signature(GRM::MARTE::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_processingresource_is_not_abstract():
    assert not inspect.isabstract(ProcessingResource)


def test_processingresource_constructor_exists():
    assert callable(ProcessingResource.__init__)


def test_processingresource_constructor_args():
    sig = inspect.signature(ProcessingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::communicationmedia_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::CommunicationMedia)


def test_marte::grm::communicationmedia_constructor_exists():
    assert callable(MARTE::GRM::CommunicationMedia.__init__)


def test_marte::grm::communicationmedia_constructor_args():
    sig = inspect.signature(MARTE::GRM::CommunicationMedia.__init__)
    params = list(sig.parameters.keys())
    assert "transmMode" in params, "Missing parameter 'transmMode'"

def test_marte::grm::communicationmedia_has_transmMode():
    assert hasattr(MARTE::GRM::CommunicationMedia, "transmMode")
    descriptor = None
    for klass in MARTE::GRM::CommunicationMedia.__mro__:
        if "transmMode" in klass.__dict__:
            descriptor = klass.__dict__["transmMode"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::deviceresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::DeviceResource)


def test_marte::grm::deviceresource_constructor_exists():
    assert callable(MARTE::GRM::DeviceResource.__init__)


def test_marte::grm::deviceresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::DeviceResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::computingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::ComputingResource)


def test_marte::grm::computingresource_constructor_exists():
    assert callable(MARTE::GRM::ComputingResource.__init__)


def test_marte::grm::computingresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::ComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::instancespecification_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::InstanceSpecification)


def test_grm::marte::instancespecification_constructor_exists():
    assert callable(GRM::MARTE::InstanceSpecification.__init__)


def test_grm::marte::instancespecification_constructor_args():
    sig = inspect.signature(GRM::MARTE::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::property_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::Property)


def test_grm::marte::property_constructor_exists():
    assert callable(GRM::MARTE::Property.__init__)


def test_grm::marte::property_constructor_args():
    sig = inspect.signature(GRM::MARTE::Property.__init__)
    params = list(sig.parameters.keys())



def test_nfp::integer_is_not_abstract():
    assert not inspect.isabstract(NFP::Integer)


def test_nfp::integer_constructor_exists():
    assert callable(NFP::Integer.__init__)


def test_nfp::integer_constructor_args():
    sig = inspect.signature(NFP::Integer.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::resource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::Resource)


def test_marte::grm::resource_constructor_exists():
    assert callable(MARTE::GRM::Resource.__init__)


def test_marte::grm::resource_constructor_args():
    sig = inspect.signature(MARTE::GRM::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "isProtected" in params, "Missing parameter 'isProtected'"

def test_marte::grm::resource_has_isProtected():
    assert hasattr(MARTE::GRM::Resource, "isProtected")
    descriptor = None
    for klass in MARTE::GRM::Resource.__mro__:
        if "isProtected" in klass.__dict__:
            descriptor = klass.__dict__["isProtected"]
            break
    assert isinstance(descriptor, property)



def test_time::marte::event_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Event)


def test_time::marte::event_constructor_exists():
    assert callable(Time::MARTE::Event.__init__)


def test_time::marte::event_constructor_args():
    sig = inspect.signature(Time::MARTE::Event.__init__)
    params = list(sig.parameters.keys())



def test_time::marte::message_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Message)


def test_time::marte::message_constructor_exists():
    assert callable(Time::MARTE::Message.__init__)


def test_time::marte::message_constructor_args():
    sig = inspect.signature(Time::MARTE::Message.__init__)
    params = list(sig.parameters.keys())



def test_time::marte::behavior_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Behavior)


def test_time::marte::behavior_constructor_exists():
    assert callable(Time::MARTE::Behavior.__init__)


def test_time::marte::behavior_constructor_args():
    sig = inspect.signature(Time::MARTE::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_time::marte::action_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Action)


def test_time::marte::action_constructor_exists():
    assert callable(Time::MARTE::Action.__init__)


def test_time::marte::action_constructor_args():
    sig = inspect.signature(Time::MARTE::Action.__init__)
    params = list(sig.parameters.keys())



def test_time::marte::timeevent_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::TimeEvent)


def test_time::marte::timeevent_constructor_exists():
    assert callable(Time::MARTE::TimeEvent.__init__)


def test_time::marte::timeevent_constructor_args():
    sig = inspect.signature(Time::MARTE::TimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::scheduler_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::Scheduler)


def test_marte::grm::scheduler_constructor_exists():
    assert callable(MARTE::GRM::Scheduler.__init__)


def test_marte::grm::scheduler_constructor_args():
    sig = inspect.signature(MARTE::GRM::Scheduler.__init__)
    params = list(sig.parameters.keys())
    assert "isPreemptible" in params, "Missing parameter 'isPreemptible'"
    assert "schedPolicy" in params, "Missing parameter 'schedPolicy'"
    assert "otherSchedPolicy" in params, "Missing parameter 'otherSchedPolicy'"

def test_marte::grm::scheduler_has_isPreemptible():
    assert hasattr(MARTE::GRM::Scheduler, "isPreemptible")
    descriptor = None
    for klass in MARTE::GRM::Scheduler.__mro__:
        if "isPreemptible" in klass.__dict__:
            descriptor = klass.__dict__["isPreemptible"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::scheduler_has_schedPolicy():
    assert hasattr(MARTE::GRM::Scheduler, "schedPolicy")
    descriptor = None
    for klass in MARTE::GRM::Scheduler.__mro__:
        if "schedPolicy" in klass.__dict__:
            descriptor = klass.__dict__["schedPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::scheduler_has_otherSchedPolicy():
    assert hasattr(MARTE::GRM::Scheduler, "otherSchedPolicy")
    descriptor = None
    for klass in MARTE::GRM::Scheduler.__mro__:
        if "otherSchedPolicy" in klass.__dict__:
            descriptor = klass.__dict__["otherSchedPolicy"]
            break
    assert isinstance(descriptor, property)



def test_marte::pam::palogicalresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::PAM::PaLogicalResource)


def test_marte::pam::palogicalresource_constructor_exists():
    assert callable(MARTE::PAM::PaLogicalResource.__init__)


def test_marte::pam::palogicalresource_constructor_args():
    sig = inspect.signature(MARTE::PAM::PaLogicalResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::synchronizationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::SynchronizationResource)


def test_marte::grm::synchronizationresource_constructor_exists():
    assert callable(MARTE::GRM::SynchronizationResource.__init__)


def test_marte::grm::synchronizationresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::SynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::mutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::MutualExclusionResource)


def test_marte::grm::mutualexclusionresource_constructor_exists():
    assert callable(MARTE::GRM::MutualExclusionResource.__init__)


def test_marte::grm::mutualexclusionresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::MutualExclusionResource.__init__)
    params = list(sig.parameters.keys())
    assert "protectKind" in params, "Missing parameter 'protectKind'"
    assert "otherProtectProtocol" in params, "Missing parameter 'otherProtectProtocol'"

def test_marte::grm::mutualexclusionresource_has_protectKind():
    assert hasattr(MARTE::GRM::MutualExclusionResource, "protectKind")
    descriptor = None
    for klass in MARTE::GRM::MutualExclusionResource.__mro__:
        if "protectKind" in klass.__dict__:
            descriptor = klass.__dict__["protectKind"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::mutualexclusionresource_has_otherProtectProtocol():
    assert hasattr(MARTE::GRM::MutualExclusionResource, "otherProtectProtocol")
    descriptor = None
    for klass in MARTE::GRM::MutualExclusionResource.__mro__:
        if "otherProtectProtocol" in klass.__dict__:
            descriptor = klass.__dict__["otherProtectProtocol"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::communicationendpoint_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::CommunicationEndPoint)


def test_marte::grm::communicationendpoint_constructor_exists():
    assert callable(MARTE::GRM::CommunicationEndPoint.__init__)


def test_marte::grm::communicationendpoint_constructor_args():
    sig = inspect.signature(MARTE::GRM::CommunicationEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwgeneral::hwresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwGeneral::HwResource)


def test_marte::hwgeneral::hwresource_constructor_exists():
    assert callable(MARTE::HwGeneral::HwResource.__init__)


def test_marte::hwgeneral::hwresource_constructor_args():
    sig = inspect.signature(MARTE::HwGeneral::HwResource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_marte::hwgeneral::hwresource_has_name():
    assert hasattr(MARTE::HwGeneral::HwResource, "name")
    descriptor = None
    for klass in MARTE::HwGeneral::HwResource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::schedulableresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::SchedulableResource)


def test_marte::grm::schedulableresource_constructor_exists():
    assert callable(MARTE::GRM::SchedulableResource.__init__)


def test_marte::grm::schedulableresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::SchedulableResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::concurrencyresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::ConcurrencyResource)


def test_marte::grm::concurrencyresource_constructor_exists():
    assert callable(MARTE::GRM::ConcurrencyResource.__init__)


def test_marte::grm::concurrencyresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::ConcurrencyResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::resourcecore::swresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::ResourceCore::SwResource)


def test_marte::sw::resourcecore::swresource_constructor_exists():
    assert callable(MARTE::SW::ResourceCore::SwResource.__init__)


def test_marte::sw::resourcecore::swresource_constructor_args():
    sig = inspect.signature(MARTE::SW::ResourceCore::SwResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::timingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::TimingResource)


def test_marte::grm::timingresource_constructor_exists():
    assert callable(MARTE::GRM::TimingResource.__init__)


def test_marte::grm::timingresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::TimingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::processingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::ProcessingResource)


def test_marte::grm::processingresource_constructor_exists():
    assert callable(MARTE::GRM::ProcessingResource.__init__)


def test_marte::grm::processingresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::ProcessingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::storageresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::StorageResource)


def test_marte::grm::storageresource_constructor_exists():
    assert callable(MARTE::GRM::StorageResource.__init__)


def test_marte::grm::storageresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::StorageResource.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::connectableelement_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::ConnectableElement)


def test_grm::marte::connectableelement_constructor_exists():
    assert callable(GRM::MARTE::ConnectableElement.__init__)


def test_grm::marte::connectableelement_constructor_args():
    sig = inspect.signature(GRM::MARTE::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::lifeline_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::Lifeline)


def test_grm::marte::lifeline_constructor_exists():
    assert callable(GRM::MARTE::Lifeline.__init__)


def test_grm::marte::lifeline_constructor_args():
    sig = inspect.signature(GRM::MARTE::Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_grm::marte::classifier_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::Classifier)


def test_grm::marte::classifier_constructor_exists():
    assert callable(GRM::MARTE::Classifier.__init__)


def test_grm::marte::classifier_constructor_args():
    sig = inspect.signature(GRM::MARTE::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_timedobservation_is_not_abstract():
    assert not inspect.isabstract(TimedObservation)


def test_timedobservation_constructor_exists():
    assert callable(TimedObservation.__init__)


def test_timedobservation_constructor_args():
    sig = inspect.signature(TimedObservation.__init__)
    params = list(sig.parameters.keys())



def test_marte::time::timedinstantobservation_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::TimedInstantObservation)


def test_marte::time::timedinstantobservation_constructor_exists():
    assert callable(MARTE::Time::TimedInstantObservation.__init__)


def test_marte::time::timedinstantobservation_constructor_args():
    sig = inspect.signature(MARTE::Time::TimedInstantObservation.__init__)
    params = list(sig.parameters.keys())
    assert "obsKind" in params, "Missing parameter 'obsKind'"

def test_marte::time::timedinstantobservation_has_obsKind():
    assert hasattr(MARTE::Time::TimedInstantObservation, "obsKind")
    descriptor = None
    for klass in MARTE::Time::TimedInstantObservation.__mro__:
        if "obsKind" in klass.__dict__:
            descriptor = klass.__dict__["obsKind"]
            break
    assert isinstance(descriptor, property)



def test_time::timedelement_is_not_abstract():
    assert not inspect.isabstract(Time::TimedElement)


def test_time::timedelement_constructor_exists():
    assert callable(Time::TimedElement.__init__)


def test_time::timedelement_constructor_args():
    sig = inspect.signature(Time::TimedElement.__init__)
    params = list(sig.parameters.keys())



def test_time::marte::valuespecification_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::ValueSpecification)


def test_time::marte::valuespecification_constructor_exists():
    assert callable(Time::MARTE::ValueSpecification.__init__)


def test_time::marte::valuespecification_constructor_args():
    sig = inspect.signature(Time::MARTE::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_timedelement_is_not_abstract():
    assert not inspect.isabstract(TimedElement)


def test_timedelement_constructor_exists():
    assert callable(TimedElement.__init__)


def test_timedelement_constructor_args():
    sig = inspect.signature(TimedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte::time::timedobservation_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::TimedObservation)


def test_marte::time::timedobservation_constructor_exists():
    assert callable(MARTE::Time::TimedObservation.__init__)


def test_marte::time::timedobservation_constructor_args():
    sig = inspect.signature(MARTE::Time::TimedObservation.__init__)
    params = list(sig.parameters.keys())



def test_marte::time::timedprocessing_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::TimedProcessing)


def test_marte::time::timedprocessing_constructor_exists():
    assert callable(MARTE::Time::TimedProcessing.__init__)


def test_marte::time::timedprocessing_constructor_args():
    sig = inspect.signature(MARTE::Time::TimedProcessing.__init__)
    params = list(sig.parameters.keys())



def test_marte::time::timedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::TimedValueSpecification)


def test_marte::time::timedvaluespecification_constructor_exists():
    assert callable(MARTE::Time::TimedValueSpecification.__init__)


def test_marte::time::timedvaluespecification_constructor_args():
    sig = inspect.signature(MARTE::Time::TimedValueSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "interpretation" in params, "Missing parameter 'interpretation'"

def test_marte::time::timedvaluespecification_has_interpretation():
    assert hasattr(MARTE::Time::TimedValueSpecification, "interpretation")
    descriptor = None
    for klass in MARTE::Time::TimedValueSpecification.__mro__:
        if "interpretation" in klass.__dict__:
            descriptor = klass.__dict__["interpretation"]
            break
    assert isinstance(descriptor, property)



def test_time::clock_is_not_abstract():
    assert not inspect.isabstract(Time::Clock)


def test_time::clock_constructor_exists():
    assert callable(Time::Clock.__init__)


def test_time::clock_constructor_args():
    sig = inspect.signature(Time::Clock.__init__)
    params = list(sig.parameters.keys())



def test_marte::time::timedelement_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::TimedElement)


def test_marte::time::timedelement_constructor_exists():
    assert callable(MARTE::Time::TimedElement.__init__)


def test_marte::time::timedelement_constructor_args():
    sig = inspect.signature(MARTE::Time::TimedElement.__init__)
    params = list(sig.parameters.keys())



def test_time::marte::class_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Class)


def test_time::marte::class_constructor_exists():
    assert callable(Time::MARTE::Class.__init__)


def test_time::marte::class_constructor_args():
    sig = inspect.signature(Time::MARTE::Class.__init__)
    params = list(sig.parameters.keys())



def test_marte::time::timedevent_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::TimedEvent)


def test_marte::time::timedevent_constructor_exists():
    assert callable(MARTE::Time::TimedEvent.__init__)


def test_marte::time::timedevent_constructor_args():
    sig = inspect.signature(MARTE::Time::TimedEvent.__init__)
    params = list(sig.parameters.keys())
    assert "repetition" in params, "Missing parameter 'repetition'"

def test_marte::time::timedevent_has_repetition():
    assert hasattr(MARTE::Time::TimedEvent, "repetition")
    descriptor = None
    for klass in MARTE::Time::TimedEvent.__mro__:
        if "repetition" in klass.__dict__:
            descriptor = klass.__dict__["repetition"]
            break
    assert isinstance(descriptor, property)



def test_time::marte::durationobservation_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::DurationObservation)


def test_time::marte::durationobservation_constructor_exists():
    assert callable(Time::MARTE::DurationObservation.__init__)


def test_time::marte::durationobservation_constructor_args():
    sig = inspect.signature(Time::MARTE::DurationObservation.__init__)
    params = list(sig.parameters.keys())



def test_marte::time::timeddurationobservation_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::TimedDurationObservation)


def test_marte::time::timeddurationobservation_constructor_exists():
    assert callable(MARTE::Time::TimedDurationObservation.__init__)


def test_marte::time::timeddurationobservation_constructor_args():
    sig = inspect.signature(MARTE::Time::TimedDurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "obsKind" in params, "Missing parameter 'obsKind'"

def test_marte::time::timeddurationobservation_has_obsKind():
    assert hasattr(MARTE::Time::TimedDurationObservation, "obsKind")
    descriptor = None
    for klass in MARTE::Time::TimedDurationObservation.__mro__:
        if "obsKind" in klass.__dict__:
            descriptor = klass.__dict__["obsKind"]
            break
    assert isinstance(descriptor, property)



def test_time::marte::timeobservation_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::TimeObservation)


def test_time::marte::timeobservation_constructor_exists():
    assert callable(Time::MARTE::TimeObservation.__init__)


def test_time::marte::timeobservation_constructor_args():
    sig = inspect.signature(Time::MARTE::TimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_time::marte::enumeration_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Enumeration)


def test_time::marte::enumeration_constructor_exists():
    assert callable(Time::MARTE::Enumeration.__init__)


def test_time::marte::enumeration_constructor_args():
    sig = inspect.signature(Time::MARTE::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_marte::time::clocktype_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::ClockType)


def test_marte::time::clocktype_constructor_exists():
    assert callable(MARTE::Time::ClockType.__init__)


def test_marte::time::clocktype_constructor_args():
    sig = inspect.signature(MARTE::Time::ClockType.__init__)
    params = list(sig.parameters.keys())
    assert "isLogical" in params, "Missing parameter 'isLogical'"
    assert "nature" in params, "Missing parameter 'nature'"

def test_marte::time::clocktype_has_isLogical():
    assert hasattr(MARTE::Time::ClockType, "isLogical")
    descriptor = None
    for klass in MARTE::Time::ClockType.__mro__:
        if "isLogical" in klass.__dict__:
            descriptor = klass.__dict__["isLogical"]
            break
    assert isinstance(descriptor, property)

def test_marte::time::clocktype_has_nature():
    assert hasattr(MARTE::Time::ClockType, "nature")
    descriptor = None
    for klass in MARTE::Time::ClockType.__mro__:
        if "nature" in klass.__dict__:
            descriptor = klass.__dict__["nature"]
            break
    assert isinstance(descriptor, property)



def test_time::marte::property_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Property)


def test_time::marte::property_constructor_exists():
    assert callable(Time::MARTE::Property.__init__)


def test_time::marte::property_constructor_args():
    sig = inspect.signature(Time::MARTE::Property.__init__)
    params = list(sig.parameters.keys())



def test_time::clocktype_is_not_abstract():
    assert not inspect.isabstract(Time::ClockType)


def test_time::clocktype_constructor_exists():
    assert callable(Time::ClockType.__init__)


def test_time::clocktype_constructor_args():
    sig = inspect.signature(Time::ClockType.__init__)
    params = list(sig.parameters.keys())



def test_time::marte::instancespecification_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::InstanceSpecification)


def test_time::marte::instancespecification_constructor_exists():
    assert callable(Time::MARTE::InstanceSpecification.__init__)


def test_time::marte::instancespecification_constructor_args():
    sig = inspect.signature(Time::MARTE::InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_marte::time::clock_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::Clock)


def test_marte::time::clock_constructor_exists():
    assert callable(MARTE::Time::Clock.__init__)


def test_marte::time::clock_constructor_args():
    sig = inspect.signature(MARTE::Time::Clock.__init__)
    params = list(sig.parameters.keys())
    assert "standard" in params, "Missing parameter 'standard'"

def test_marte::time::clock_has_standard():
    assert hasattr(MARTE::Time::Clock, "standard")
    descriptor = None
    for klass in MARTE::Time::Clock.__mro__:
        if "standard" in klass.__dict__:
            descriptor = klass.__dict__["standard"]
            break
    assert isinstance(descriptor, property)



def test_time::marte::namespace_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Namespace)


def test_time::marte::namespace_constructor_exists():
    assert callable(Time::MARTE::Namespace.__init__)


def test_time::marte::namespace_constructor_args():
    sig = inspect.signature(Time::MARTE::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_marte::time::timeddomain_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::TimedDomain)


def test_marte::time::timeddomain_constructor_exists():
    assert callable(MARTE::Time::TimedDomain.__init__)


def test_marte::time::timeddomain_constructor_args():
    sig = inspect.signature(MARTE::Time::TimedDomain.__init__)
    params = list(sig.parameters.keys())



def test_alloc::marte::abstraction_is_not_abstract():
    assert not inspect.isabstract(Alloc::MARTE::Abstraction)


def test_alloc::marte::abstraction_constructor_exists():
    assert callable(Alloc::MARTE::Abstraction.__init__)


def test_alloc::marte::abstraction_constructor_args():
    sig = inspect.signature(Alloc::MARTE::Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_marte::alloc::allocate_is_not_abstract():
    assert not inspect.isabstract(MARTE::Alloc::Allocate)


def test_marte::alloc::allocate_constructor_exists():
    assert callable(MARTE::Alloc::Allocate.__init__)


def test_marte::alloc::allocate_constructor_args():
    sig = inspect.signature(MARTE::Alloc::Allocate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "nature" in params, "Missing parameter 'nature'"

def test_marte::alloc::allocate_has_kind():
    assert hasattr(MARTE::Alloc::Allocate, "kind")
    descriptor = None
    for klass in MARTE::Alloc::Allocate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_marte::alloc::allocate_has_nature():
    assert hasattr(MARTE::Alloc::Allocate, "nature")
    descriptor = None
    for klass in MARTE::Alloc::Allocate.__mro__:
        if "nature" in klass.__dict__:
            descriptor = klass.__dict__["nature"]
            break
    assert isinstance(descriptor, property)



def test_time::marte::operation_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Operation)


def test_time::marte::operation_constructor_exists():
    assert callable(Time::MARTE::Operation.__init__)


def test_time::marte::operation_constructor_args():
    sig = inspect.signature(Time::MARTE::Operation.__init__)
    params = list(sig.parameters.keys())



def test_marte::alloc::assign_is_not_abstract():
    assert not inspect.isabstract(MARTE::Alloc::Assign)


def test_marte::alloc::assign_constructor_exists():
    assert callable(MARTE::Alloc::Assign.__init__)


def test_marte::alloc::assign_constructor_args():
    sig = inspect.signature(MARTE::Alloc::Assign.__init__)
    params = list(sig.parameters.keys())



def test_nfps::nfpconstraint_is_not_abstract():
    assert not inspect.isabstract(NFPs::NfpConstraint)


def test_nfps::nfpconstraint_constructor_exists():
    assert callable(NFPs::NfpConstraint.__init__)


def test_nfps::nfpconstraint_constructor_args():
    sig = inspect.signature(NFPs::NfpConstraint.__init__)
    params = list(sig.parameters.keys())



def test_marte::time::clockconstraint_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::ClockConstraint)


def test_marte::time::clockconstraint_constructor_exists():
    assert callable(MARTE::Time::ClockConstraint.__init__)


def test_marte::time::clockconstraint_constructor_args():
    sig = inspect.signature(MARTE::Time::ClockConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "isChronometricBased" in params, "Missing parameter 'isChronometricBased'"
    assert "isCoincidenceBased" in params, "Missing parameter 'isCoincidenceBased'"
    assert "isPrecedenceBased" in params, "Missing parameter 'isPrecedenceBased'"

def test_marte::time::clockconstraint_has_isChronometricBased():
    assert hasattr(MARTE::Time::ClockConstraint, "isChronometricBased")
    descriptor = None
    for klass in MARTE::Time::ClockConstraint.__mro__:
        if "isChronometricBased" in klass.__dict__:
            descriptor = klass.__dict__["isChronometricBased"]
            break
    assert isinstance(descriptor, property)

def test_marte::time::clockconstraint_has_isCoincidenceBased():
    assert hasattr(MARTE::Time::ClockConstraint, "isCoincidenceBased")
    descriptor = None
    for klass in MARTE::Time::ClockConstraint.__mro__:
        if "isCoincidenceBased" in klass.__dict__:
            descriptor = klass.__dict__["isCoincidenceBased"]
            break
    assert isinstance(descriptor, property)

def test_marte::time::clockconstraint_has_isPrecedenceBased():
    assert hasattr(MARTE::Time::ClockConstraint, "isPrecedenceBased")
    descriptor = None
    for klass in MARTE::Time::ClockConstraint.__mro__:
        if "isPrecedenceBased" in klass.__dict__:
            descriptor = klass.__dict__["isPrecedenceBased"]
            break
    assert isinstance(descriptor, property)



def test_marte::time::timedconstraint_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::TimedConstraint)


def test_marte::time::timedconstraint_constructor_exists():
    assert callable(MARTE::Time::TimedConstraint.__init__)


def test_marte::time::timedconstraint_constructor_args():
    sig = inspect.signature(MARTE::Time::TimedConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "interpretation" in params, "Missing parameter 'interpretation'"

def test_marte::time::timedconstraint_has_interpretation():
    assert hasattr(MARTE::Time::TimedConstraint, "interpretation")
    descriptor = None
    for klass in MARTE::Time::TimedConstraint.__mro__:
        if "interpretation" in klass.__dict__:
            descriptor = klass.__dict__["interpretation"]
            break
    assert isinstance(descriptor, property)



def test_alloc::marte::dependency_is_not_abstract():
    assert not inspect.isabstract(Alloc::MARTE::Dependency)


def test_alloc::marte::dependency_constructor_exists():
    assert callable(Alloc::MARTE::Dependency.__init__)


def test_alloc::marte::dependency_constructor_args():
    sig = inspect.signature(Alloc::MARTE::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_marte::alloc::nfprefine_is_not_abstract():
    assert not inspect.isabstract(MARTE::Alloc::NfpRefine)


def test_marte::alloc::nfprefine_constructor_exists():
    assert callable(MARTE::Alloc::NfpRefine.__init__)


def test_marte::alloc::nfprefine_constructor_args():
    sig = inspect.signature(MARTE::Alloc::NfpRefine.__init__)
    params = list(sig.parameters.keys())



def test_alloc::marte::activitypartition_is_not_abstract():
    assert not inspect.isabstract(Alloc::MARTE::ActivityPartition)


def test_alloc::marte::activitypartition_constructor_exists():
    assert callable(Alloc::MARTE::ActivityPartition.__init__)


def test_alloc::marte::activitypartition_constructor_args():
    sig = inspect.signature(Alloc::MARTE::ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_marte::alloc::allocateactivitygroup_is_not_abstract():
    assert not inspect.isabstract(MARTE::Alloc::AllocateActivityGroup)


def test_marte::alloc::allocateactivitygroup_constructor_exists():
    assert callable(MARTE::Alloc::AllocateActivityGroup.__init__)


def test_marte::alloc::allocateactivitygroup_constructor_args():
    sig = inspect.signature(MARTE::Alloc::AllocateActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_alloc::allocated_is_not_abstract():
    assert not inspect.isabstract(Alloc::Allocated)


def test_alloc::allocated_constructor_exists():
    assert callable(Alloc::Allocated.__init__)


def test_alloc::allocated_constructor_args():
    sig = inspect.signature(Alloc::Allocated.__init__)
    params = list(sig.parameters.keys())



def test_alloc::marte::namedelement_is_not_abstract():
    assert not inspect.isabstract(Alloc::MARTE::NamedElement)


def test_alloc::marte::namedelement_constructor_exists():
    assert callable(Alloc::MARTE::NamedElement.__init__)


def test_alloc::marte::namedelement_constructor_args():
    sig = inspect.signature(Alloc::MARTE::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte::alloc::allocated_is_not_abstract():
    assert not inspect.isabstract(MARTE::Alloc::Allocated)


def test_marte::alloc::allocated_constructor_exists():
    assert callable(MARTE::Alloc::Allocated.__init__)


def test_marte::alloc::allocated_constructor_args():
    sig = inspect.signature(MARTE::Alloc::Allocated.__init__)
    params = list(sig.parameters.keys())



def test_coreelements::marte::state_is_not_abstract():
    assert not inspect.isabstract(CoreElements::MARTE::State)


def test_coreelements::marte::state_constructor_exists():
    assert callable(CoreElements::MARTE::State.__init__)


def test_coreelements::marte::state_constructor_args():
    sig = inspect.signature(CoreElements::MARTE::State.__init__)
    params = list(sig.parameters.keys())



def test_marte::coreelements::mode_is_not_abstract():
    assert not inspect.isabstract(MARTE::CoreElements::Mode)


def test_marte::coreelements::mode_constructor_exists():
    assert callable(MARTE::CoreElements::Mode.__init__)


def test_marte::coreelements::mode_constructor_args():
    sig = inspect.signature(MARTE::CoreElements::Mode.__init__)
    params = list(sig.parameters.keys())



def test_alloc::marte::comment_is_not_abstract():
    assert not inspect.isabstract(Alloc::MARTE::Comment)


def test_alloc::marte::comment_constructor_exists():
    assert callable(Alloc::MARTE::Comment.__init__)


def test_alloc::marte::comment_constructor_args():
    sig = inspect.signature(Alloc::MARTE::Comment.__init__)
    params = list(sig.parameters.keys())



def test_alloc::marte::element_is_not_abstract():
    assert not inspect.isabstract(Alloc::MARTE::Element)


def test_alloc::marte::element_constructor_exists():
    assert callable(Alloc::MARTE::Element.__init__)


def test_alloc::marte::element_constructor_args():
    sig = inspect.signature(Alloc::MARTE::Element.__init__)
    params = list(sig.parameters.keys())



def test_coreelements::marte::transition_is_not_abstract():
    assert not inspect.isabstract(CoreElements::MARTE::Transition)


def test_coreelements::marte::transition_constructor_exists():
    assert callable(CoreElements::MARTE::Transition.__init__)


def test_coreelements::marte::transition_constructor_args():
    sig = inspect.signature(CoreElements::MARTE::Transition.__init__)
    params = list(sig.parameters.keys())

def test_datapoolorderingkind_exists():
    # Check that the Enumeration exists
    assert DataPoolOrderingKind is not None

def test_datapoolorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataPoolOrderingKind]
    expected_literals = [
        "FIFO",
        "LIFO",
        "UserDefined",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataPoolOrderingKind"

def test_laxitykind_exists():
    # Check that the Enumeration exists
    assert LaxityKind is not None

def test_laxitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LaxityKind]
    expected_literals = [
        "other",
        "soft",
        "hard",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LaxityKind"

def test_constraintkind_exists():
    # Check that the Enumeration exists
    assert ConstraintKind is not None

def test_constraintkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintKind]
    expected_literals = [
        "offered",
        "required",
        "contract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintKind"

def test_allocationnature_exists():
    # Check that the Enumeration exists
    assert AllocationNature is not None

def test_allocationnature_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AllocationNature]
    expected_literals = [
        "spatialDistribution",
        "timeScheduling",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AllocationNature"

def test_poolmgtpolicykind_exists():
    # Check that the Enumeration exists
    assert PoolMgtPolicyKind is not None

def test_poolmgtpolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PoolMgtPolicyKind]
    expected_literals = [
        "dynamic",
        "infiniteWait",
        "other",
        "exception",
        "timedWait",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PoolMgtPolicyKind"

def test_componentstate_exists():
    # Check that the Enumeration exists
    assert ComponentState is not None

def test_componentstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentState]
    expected_literals = [
        "storage",
        "operating",
        "undef",
        "other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentState"

def test_synchronizationkind_exists():
    # Check that the Enumeration exists
    assert SynchronizationKind is not None

def test_synchronizationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SynchronizationKind]
    expected_literals = [
        "asynchronous",
        "synchronous",
        "rendezVous",
        "other",
        "delayedSynchronous",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SynchronizationKind"

def test_allocationendkind_exists():
    # Check that the Enumeration exists
    assert AllocationEndKind is not None

def test_allocationendkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AllocationEndKind]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AllocationEndKind"

def test_concurrencykind_exists():
    # Check that the Enumeration exists
    assert ConcurrencyKind is not None

def test_concurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConcurrencyKind]
    expected_literals = [
        "parallel",
        "writer",
        "reader",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConcurrencyKind"

def test_optimallitycriterionkind_exists():
    # Check that the Enumeration exists
    assert OptimallityCriterionKind is not None

def test_optimallitycriterionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptimallityCriterionKind]
    expected_literals = [
        "other",
        "minimizedMeanTardiness",
        "minimizeMissedDeadlines",
        "meetHardDeadlines",
        "undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptimallityCriterionKind"

def test_pld_technology_exists():
    # Check that the Enumeration exists
    assert PLD_Technology is not None

def test_pld_technology_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PLD_Technology]
    expected_literals = [
        "antifuse",
        "SRAM",
        "other",
        "undef",
        "flash",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PLD_Technology"

def test_rom_type_exists():
    # Check that the Enumeration exists
    assert ROM_Type is not None

def test_rom_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ROM_Type]
    expected_literals = [
        "other",
        "EPROM",
        "EEPROM",
        "maskedROM",
        "Flash",
        "undef",
        "OTP_EPROM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ROM_Type"

def test_notificationresourcekind_exists():
    # Check that the Enumeration exists
    assert NotificationResourceKind is not None

def test_notificationresourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NotificationResourceKind]
    expected_literals = [
        "Other",
        "Barrier",
        "Event",
        "Undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NotificationResourceKind"

def test_isa_type_exists():
    # Check that the Enumeration exists
    assert ISA_Type is not None

def test_isa_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ISA_Type]
    expected_literals = [
        "RISC",
        "CISC",
        "SIMD",
        "undef",
        "VLIW",
        "other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ISA_Type"

def test_repl_policy_exists():
    # Check that the Enumeration exists
    assert Repl_Policy is not None

def test_repl_policy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Repl_Policy]
    expected_literals = [
        "NFU",
        "random",
        "FIFO",
        "undef",
        "other",
        "LRU",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Repl_Policy"

def test_clientserverkind_exists():
    # Check that the Enumeration exists
    assert ClientServerKind is not None

def test_clientserverkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClientServerKind]
    expected_literals = [
        "proreq",
        "provided",
        "required",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClientServerKind"

def test_concurrentaccessprotocolkind_exists():
    # Check that the Enumeration exists
    assert ConcurrentAccessProtocolKind is not None

def test_concurrentaccessprotocolkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConcurrentAccessProtocolKind]
    expected_literals = [
        "PCP",
        "Undef",
        "NoPreemption",
        "PIP",
        "Other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConcurrentAccessProtocolKind"

def test_interruptkind_exists():
    # Check that the Enumeration exists
    assert InterruptKind is not None

def test_interruptkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InterruptKind]
    expected_literals = [
        "Other",
        "Undef",
        "HardwareInterruption",
        "ProcessorDetectedException",
        "ProgrammedException",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InterruptKind"

def test_assignmentnature_exists():
    # Check that the Enumeration exists
    assert AssignmentNature is not None

def test_assignmentnature_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentNature]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentNature"

def test_notificationkind_exists():
    # Check that the Enumeration exists
    assert NotificationKind is not None

def test_notificationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NotificationKind]
    expected_literals = [
        "Other",
        "Memorized",
        "Undef",
        "Bounded",
        "Memoryless",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NotificationKind"

def test_accesspolicykind_exists():
    # Check that the Enumeration exists
    assert AccessPolicyKind is not None

def test_accesspolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessPolicyKind]
    expected_literals = [
        "ReadWrite",
        "Undef",
        "Other",
        "Read",
        "Write",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessPolicyKind"

def test_writepolicy_exists():
    # Check that the Enumeration exists
    assert WritePolicy is not None

def test_writepolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WritePolicy]
    expected_literals = [
        "writeBack",
        "writeThrough",
        "undef",
        "other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WritePolicy"

def test_executionkind_exists():
    # Check that the Enumeration exists
    assert ExecutionKind is not None

def test_executionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExecutionKind]
    expected_literals = [
        "localImmediate",
        "remoteImmediate",
        "deferred",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExecutionKind"

def test_assignmentkind_exists():
    # Check that the Enumeration exists
    assert AssignmentKind is not None

def test_assignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentKind]
    expected_literals = [
        "structural",
        "behavioral",
        "hybrid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentKind"

def test_flowdirectionkind_exists():
    # Check that the Enumeration exists
    assert FlowDirectionKind is not None

def test_flowdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowDirectionKind]
    expected_literals = [
        "inout",
        "out",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlowDirectionKind"

def test_conditiontype_exists():
    # Check that the Enumeration exists
    assert ConditionType is not None

def test_conditiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionType]
    expected_literals = [
        "altitude",
        "undef",
        "temperature",
        "other",
        "humidity",
        "shock",
        "vibration",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionType"

def test_portspecificationkind_exists():
    # Check that the Enumeration exists
    assert PortSpecificationKind is not None

def test_portspecificationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PortSpecificationKind]
    expected_literals = [
        "atomic",
        "featureBased",
        "interfaceBased",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PortSpecificationKind"

def test_variabledirectionkind_exists():
    # Check that the Enumeration exists
    assert VariableDirectionKind is not None

def test_variabledirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableDirectionKind]
    expected_literals = [
        "inout",
        "in_",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariableDirectionKind"

def test_mutualexclusionresourcekind_exists():
    # Check that the Enumeration exists
    assert MutualExclusionResourceKind is not None

def test_mutualexclusionresourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MutualExclusionResourceKind]
    expected_literals = [
        "BooleanSemaphore",
        "Undef",
        "Other",
        "CountSemaphore",
        "Mutex",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MutualExclusionResourceKind"

def test_messageresourcekind_exists():
    # Check that the Enumeration exists
    assert MessageResourceKind is not None

def test_messageresourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageResourceKind]
    expected_literals = [
        "MessageQueue",
        "Undef",
        "Blackboard",
        "Pipe",
        "Other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageResourceKind"

def test_allocationkind_exists():
    # Check that the Enumeration exists
    assert AllocationKind is not None

def test_allocationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AllocationKind]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AllocationKind"

def test_queuepolicykind_exists():
    # Check that the Enumeration exists
    assert QueuePolicyKind is not None

def test_queuepolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QueuePolicyKind]
    expected_literals = [
        "Priority",
        "FIFO",
        "LIFO",
        "Other",
        "Undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QueuePolicyKind"

def test_componentkind_exists():
    # Check that the Enumeration exists
    assert ComponentKind is not None

def test_componentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentKind]
    expected_literals = [
        "other",
        "unit",
        "port",
        "undef",
        "chip",
        "channel",
        "card",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentKind"

def test_cachetype_exists():
    # Check that the Enumeration exists
    assert CacheType is not None

def test_cachetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CacheType]
    expected_literals = [
        "undef",
        "unified",
        "data",
        "instruction",
        "other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CacheType"

def test_pld_class_exists():
    # Check that the Enumeration exists
    assert PLD_Class is not None

def test_pld_class_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PLD_Class]
    expected_literals = [
        "other",
        "seaOfGates",
        "symetricalArray",
        "rowBased",
        "undef",
        "hierarchicalPLD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PLD_Class"

def test_callconcurrencykind_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyKind is not None

def test_callconcurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyKind]
    expected_literals = [
        "sequential",
        "guarded",
        "concurrent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyKind"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
GQAM::GaCommStep_strategy = st.builds(
    GQAM::GaCommStep,
)
PAM::PaStep_strategy = st.builds(
    PAM::PaStep,
)
MARTE::PAM::PaCommStep_strategy = st.builds(
    MARTE::PAM::PaCommStep,
)
MARTE::PAM::PaRunTInstance_strategy = st.builds(
    MARTE::PAM::PaRunTInstance,
    unbddPool=
        safe_text
)
GaExecHost_strategy = st.builds(
    GaExecHost,
)
MARTE::SAM::SaExecHost_strategy = st.builds(
    MARTE::SAM::SaExecHost,
)
MutualExclusionResource_strategy = st.builds(
    MutualExclusionResource,
)
MARTE::SAM::SaSharedResource_strategy = st.builds(
    MARTE::SAM::SaSharedResource,
)
GaCommHost_strategy = st.builds(
    GaCommHost,
)
MARTE::SAM::SaCommHost_strategy = st.builds(
    MARTE::SAM::SaCommHost,
)
SAM::MARTE::BehavioralFeature_strategy = st.builds(
    SAM::MARTE::BehavioralFeature,
)
SAM::SaSharedResource_strategy = st.builds(
    SAM::SaSharedResource,
)
GaAnalysisContext_strategy = st.builds(
    GaAnalysisContext,
)
MARTE::SAM::SaAnalysisContext_strategy = st.builds(
    MARTE::SAM::SaAnalysisContext,
    optCriterion=
        safe_text
)
GQAM::MARTE::Classifier_strategy = st.builds(
    GQAM::MARTE::Classifier,
)
GaCommStep_strategy = st.builds(
    GaCommStep,
)
MARTE::SAM::SaCommStep_strategy = st.builds(
    MARTE::SAM::SaCommStep,
)
SAM::MARTE::NamedElement_strategy = st.builds(
    SAM::MARTE::NamedElement,
)
MARTE::SAM::SaEndtoEndFlow_strategy = st.builds(
    MARTE::SAM::SaEndtoEndFlow,
)
SchedulableResource_strategy = st.builds(
    SchedulableResource,
)
MARTE::GQAM::GaCommChannel_strategy = st.builds(
    MARTE::GQAM::GaCommChannel,
)
MARTE::GQAM::GaResourcesPlatform_strategy = st.builds(
    MARTE::GQAM::GaResourcesPlatform,
)
GQAM::GaResourcesPlatform_strategy = st.builds(
    GQAM::GaResourcesPlatform,
)
GQAM::GaWorkloadBehavior_strategy = st.builds(
    GQAM::GaWorkloadBehavior,
)
Variables::ExpressionContext_strategy = st.builds(
    Variables::ExpressionContext,
)
CoreElements::Configuration_strategy = st.builds(
    CoreElements::Configuration,
)
MARTE::GQAM::GaAnalysisContext_strategy = st.builds(
    MARTE::GQAM::GaAnalysisContext,
)
MARTE::GQAM::GaWorkloadBehavior_strategy = st.builds(
    MARTE::GQAM::GaWorkloadBehavior,
)
GaTimedObs_strategy = st.builds(
    GaTimedObs,
)
MARTE::SAM::SaSchedObs_strategy = st.builds(
    MARTE::SAM::SaSchedObs,
)
MARTE::GQAM::GaLatencyObs_strategy = st.builds(
    MARTE::GQAM::GaLatencyObs,
)
GQAM::MARTE::TimeObservation_strategy = st.builds(
    GQAM::MARTE::TimeObservation,
)
NfpConstraint_strategy = st.builds(
    NfpConstraint,
)
MARTE::GQAM::GaTimedObs_strategy = st.builds(
    MARTE::GQAM::GaTimedObs,
    laxity=
        safe_text
)
GQAM::MARTE::Operation_strategy = st.builds(
    GQAM::MARTE::Operation,
)
GaStep_strategy = st.builds(
    GaStep,
)
MARTE::SAM::SaStep_strategy = st.builds(
    MARTE::SAM::SaStep,
)
MARTE::GQAM::GaCommStep_strategy = st.builds(
    MARTE::GQAM::GaCommStep,
)
MARTE::GQAM::GaRelStep_strategy = st.builds(
    MARTE::GQAM::GaRelStep,
)
MARTE::GQAM::GaAcqStep_strategy = st.builds(
    MARTE::GQAM::GaAcqStep,
)
MARTE::PAM::PaStep_strategy = st.builds(
    MARTE::PAM::PaStep,
    extOpDemand=
        safe_text
)
MARTE::GQAM::GaRequestedService_strategy = st.builds(
    MARTE::GQAM::GaRequestedService,
)
IntegerInterval_strategy = st.builds(
    IntegerInterval,
)
GaScenario_strategy = st.builds(
    GaScenario,
)
MARTE::GQAM::GaStep_strategy = st.builds(
    MARTE::GQAM::GaStep,
)
GQAM::GaTimedObs_strategy = st.builds(
    GQAM::GaTimedObs,
)
GQAM::GaStep_strategy = st.builds(
    GQAM::GaStep,
)
GQAM::GaRequestedService_strategy = st.builds(
    GQAM::GaRequestedService,
)
MARTE::PAM::PaRequestedStep_strategy = st.builds(
    MARTE::PAM::PaRequestedStep,
)
GQAM::GaExecHost_strategy = st.builds(
    GQAM::GaExecHost,
)
GQAM::GaWorkloadEvent_strategy = st.builds(
    GQAM::GaWorkloadEvent,
)
Time::TimedProcessing_strategy = st.builds(
    Time::TimedProcessing,
)
MARTE::GQAM::GaWorkloadGenerator_strategy = st.builds(
    MARTE::GQAM::GaWorkloadGenerator,
)
GCM::MARTE::Behavior_strategy = st.builds(
    GCM::MARTE::Behavior,
)
GQAM::MARTE::TimeEvent_strategy = st.builds(
    GQAM::MARTE::TimeEvent,
)
GQAM::GaScenario_strategy = st.builds(
    GQAM::GaScenario,
)
GQAM::GaEventTrace_strategy = st.builds(
    GQAM::GaEventTrace,
)
GQAM::GaWorkloadGenerator_strategy = st.builds(
    GQAM::GaWorkloadGenerator,
)
MARTE::GQAM::GaWorkloadEvent_strategy = st.builds(
    MARTE::GQAM::GaWorkloadEvent,
)
GQAM::MARTE::NamedElement_strategy = st.builds(
    GQAM::MARTE::NamedElement,
)
MARTE::GQAM::GaEventTrace_strategy = st.builds(
    MARTE::GQAM::GaEventTrace,
    format=
        safe_text,
    location=
        safe_text,
    content=
        safe_text
)
GQAM::MARTE::Behavior_strategy = st.builds(
    GQAM::MARTE::Behavior,
)
MARTE::GCM::FlowSpecification_strategy = st.builds(
    MARTE::GCM::FlowSpecification,
)
MARTE::GCM::ClientServerSpecification_strategy = st.builds(
    MARTE::GCM::ClientServerSpecification,
)
MARTE::GCM::DataPool_strategy = st.builds(
    MARTE::GCM::DataPool,
    ordering=
        safe_text
)
GCM::MARTE::Classifier_strategy = st.builds(
    GCM::MARTE::Classifier,
)
GCM::MARTE::AnyReceiveEvent_strategy = st.builds(
    GCM::MARTE::AnyReceiveEvent,
)
MARTE::GCM::DataEvent_strategy = st.builds(
    MARTE::GCM::DataEvent,
)
GCM::MARTE::InvocationAction_strategy = st.builds(
    GCM::MARTE::InvocationAction,
)
MARTE::GCM::GCMInvocationAction_strategy = st.builds(
    MARTE::GCM::GCMInvocationAction,
)
GCM::MARTE::Feature_strategy = st.builds(
    GCM::MARTE::Feature,
)
GCM::MARTE::Trigger_strategy = st.builds(
    GCM::MARTE::Trigger,
)
MARTE::GCM::GCMTrigger_strategy = st.builds(
    MARTE::GCM::GCMTrigger,
)
GCM::MARTE::BehavioralFeature_strategy = st.builds(
    GCM::MARTE::BehavioralFeature,
)
MARTE::GCM::ClientServerFeature_strategy = st.builds(
    MARTE::GCM::ClientServerFeature,
    kind=
        safe_text
)
GCM::MARTE::Property_strategy = st.builds(
    GCM::MARTE::Property,
)
MARTE::GCM::FlowProperty_strategy = st.builds(
    MARTE::GCM::FlowProperty,
    direction=
        safe_text
)
GCM::ClientServerSpecification_strategy = st.builds(
    GCM::ClientServerSpecification,
)
GCM::MARTE::Interface_strategy = st.builds(
    GCM::MARTE::Interface,
)
MARTE::GCM::ClientServerPort_strategy = st.builds(
    MARTE::GCM::ClientServerPort,
    specificationKind=
        safe_text,
    kind=
        safe_text,
    isConjugated=
        safe_text
)
GCM::MARTE::Port_strategy = st.builds(
    GCM::MARTE::Port,
)
MARTE::GCM::FlowPort_strategy = st.builds(
    MARTE::GCM::FlowPort,
    isAtomic=
        safe_text,
    isConjugated=
        safe_text,
    direction=
        safe_text
)
SwSynchronizationResource_strategy = st.builds(
    SwSynchronizationResource,
)
MARTE::SW::Interaction::NotificationResource_strategy = st.builds(
    MARTE::SW::Interaction::NotificationResource,
    occurence=
        safe_text,
    mechanism=
        safe_text
)
SW::Interaction::SwSynchronizationResource_strategy = st.builds(
    SW::Interaction::SwSynchronizationResource,
)
SW::Interaction::MARTE::BehavioralFeature_strategy = st.builds(
    SW::Interaction::MARTE::BehavioralFeature,
)
SwCommunicationResource_strategy = st.builds(
    SwCommunicationResource,
)
MARTE::SW::Interaction::MessageComResource_strategy = st.builds(
    MARTE::SW::Interaction::MessageComResource,
    mechanism=
        safe_text,
    isFixedMessageSize=
        safe_text,
    messageQueuePolicy=
        safe_text
)
MARTE::SW::Interaction::SharedDataComResource_strategy = st.builds(
    MARTE::SW::Interaction::SharedDataComResource,
)
GRM::SynchronizationResource_strategy = st.builds(
    GRM::SynchronizationResource,
)
SW::Interaction::SwInteractionResource_strategy = st.builds(
    SW::Interaction::SwInteractionResource,
)
MARTE::SW::Interaction::SwSynchronizationResource_strategy = st.builds(
    MARTE::SW::Interaction::SwSynchronizationResource,
)
SW::Interaction::MARTE::TypedElement_strategy = st.builds(
    SW::Interaction::MARTE::TypedElement,
)
SW::Brokering::MARTE::Activity_strategy = st.builds(
    SW::Brokering::MARTE::Activity,
)
SW::Brokering::MARTE::Operation_strategy = st.builds(
    SW::Brokering::MARTE::Operation,
)
SW::Brokering::MARTE::BehavioralFeature_strategy = st.builds(
    SW::Brokering::MARTE::BehavioralFeature,
)
SW::Brokering::MARTE::TypedElement_strategy = st.builds(
    SW::Brokering::MARTE::TypedElement,
)
InterruptResource_strategy = st.builds(
    InterruptResource,
)
MARTE::SW::Concurrency::Alarm_strategy = st.builds(
    MARTE::SW::Concurrency::Alarm,
    isWatchdog=
        safe_text
)
SW::Concurrency::MARTE::Namespace_strategy = st.builds(
    SW::Concurrency::MARTE::Namespace,
)
TimerResource_strategy = st.builds(
    TimerResource,
)
MARTE::SW::Concurrency::SwTimerResource_strategy = st.builds(
    MARTE::SW::Concurrency::SwTimerResource,
)
SW::Concurrency::MARTE::NamedElement_strategy = st.builds(
    SW::Concurrency::MARTE::NamedElement,
)
SW::Concurrency::SwConcurrentResource_strategy = st.builds(
    SW::Concurrency::SwConcurrentResource,
)
SwConcurrentResource_strategy = st.builds(
    SwConcurrentResource,
)
MARTE::SW::Concurrency::InterruptResource_strategy = st.builds(
    MARTE::SW::Concurrency::InterruptResource,
    isMaskable=
        safe_text,
    kind=
        safe_text
)
SW::Concurrency::MARTE::TypedElement_strategy = st.builds(
    SW::Concurrency::MARTE::TypedElement,
)
SW::Concurrency::MARTE::Element_strategy = st.builds(
    SW::Concurrency::MARTE::Element,
)
SwResource_strategy = st.builds(
    SwResource,
)
MARTE::SW::Interaction::SwInteractionResource_strategy = st.builds(
    MARTE::SW::Interaction::SwInteractionResource,
    waitingQueueCapacity=
        safe_text,
    waitingQueuePolicy=
        safe_text,
    isIntraMemoryPartitionInteraction=
        st.booleans()
)
MARTE::SW::Brokering::MemoryBroker_strategy = st.builds(
    MARTE::SW::Brokering::MemoryBroker,
    accessPolicy=
        safe_text
)
MARTE::SW::Concurrency::MemoryPartition_strategy = st.builds(
    MARTE::SW::Concurrency::MemoryPartition,
)
MARTE::SW::Brokering::DeviceBroker_strategy = st.builds(
    MARTE::SW::Brokering::DeviceBroker,
    name=
        safe_text,
    accessPolicy=
        safe_text,
    isBuffered=
        safe_text
)
MARTE::SW::Concurrency::SwConcurrentResource_strategy = st.builds(
    MARTE::SW::Concurrency::SwConcurrentResource,
    activationCapacity=
        safe_text
)
SW::ResourceCore::MARTE::BehavioralFeature_strategy = st.builds(
    SW::ResourceCore::MARTE::BehavioralFeature,
)
SW::ResourceCore::MARTE::TypedElement_strategy = st.builds(
    SW::ResourceCore::MARTE::TypedElement,
)
SW::Concurrency::MARTE::BehavioralFeature_strategy = st.builds(
    SW::Concurrency::MARTE::BehavioralFeature,
)
SW::Brokering::DeviceBroker_strategy = st.builds(
    SW::Brokering::DeviceBroker,
)
MARTE::HwDiagram::SRMDiagram_strategy = st.builds(
    MARTE::HwDiagram::SRMDiagram,
)
SW::ResourceCore::MARTE::Property_strategy = st.builds(
    SW::ResourceCore::MARTE::Property,
)
HwDiagram::MARTE::DataType_strategy = st.builds(
    HwDiagram::MARTE::DataType,
)
MARTE::HwDiagram::HwCircuitDiagram_strategy = st.builds(
    MARTE::HwDiagram::HwCircuitDiagram,
    name=
        safe_text
)
HwCommunication::HwConnection_strategy = st.builds(
    HwCommunication::HwConnection,
)
MARTE::HwDiagram::HwHRMDiagram_strategy = st.builds(
    MARTE::HwDiagram::HwHRMDiagram,
    name=
        safe_text
)
HwPackage::HwWire_strategy = st.builds(
    HwPackage::HwWire,
)
PAM::MARTE::NamedElement_strategy = st.builds(
    PAM::MARTE::NamedElement,
)
MARTE::PAM::PaResPassStep_strategy = st.builds(
    MARTE::PAM::PaResPassStep,
)
MARTE::HwPackage::HwPackage_strategy = st.builds(
    MARTE::HwPackage::HwPackage,
    name=
        safe_text,
    pinNum=
        st.integers(),
    packageType=
        safe_text
)
MARTE::HwDatasheet::HwDatasheet_strategy = st.builds(
    MARTE::HwDatasheet::HwDatasheet,
    revision=
        safe_text,
    name=
        safe_text
)
MARTE::HwDiagram::HwBlockDiagram_strategy = st.builds(
    MARTE::HwDiagram::HwBlockDiagram,
    name=
        safe_text
)
HwProtocol::MARTE::Operation_strategy = st.builds(
    HwProtocol::MARTE::Operation,
)
MARTE::HwProtocol::HwProtocol_strategy = st.builds(
    MARTE::HwProtocol::HwProtocol,
    name=
        safe_text
)
HwPeripheral::RegisterAction_strategy = st.builds(
    HwPeripheral::RegisterAction,
)
Activity_strategy = st.builds(
    Activity,
)
MARTE::HwPeripheral::PeripheralActivity_strategy = st.builds(
    MARTE::HwPeripheral::PeripheralActivity,
)
HwPeripheral::MARTE::OutputPin_strategy = st.builds(
    HwPeripheral::MARTE::OutputPin,
)
HwPeripheral::MARTE::InputPin_strategy = st.builds(
    HwPeripheral::MARTE::InputPin,
)
RegisterAction_strategy = st.builds(
    RegisterAction,
)
MARTE::HwPeripheral::ReadRegisterAction_strategy = st.builds(
    MARTE::HwPeripheral::ReadRegisterAction,
)
MARTE::HwPeripheral::WriteRegisterAction_strategy = st.builds(
    MARTE::HwPeripheral::WriteRegisterAction,
)
Action_strategy = st.builds(
    Action,
)
MARTE::HwPeripheral::RegisterAction_strategy = st.builds(
    MARTE::HwPeripheral::RegisterAction,
)
HwPeripheral::MARTE::Operation_strategy = st.builds(
    HwPeripheral::MARTE::Operation,
)
Operation_strategy = st.builds(
    Operation,
)
MARTE::HwDeviceFunction::HwDeviceFunction_strategy = st.builds(
    MARTE::HwDeviceFunction::HwDeviceFunction,
)
MARTE::HwPeripheral::OperationImpl_strategy = st.builds(
    MARTE::HwPeripheral::OperationImpl,
)
HwIO::HwLine_strategy = st.builds(
    HwIO::HwLine,
)
HwPackage::HwPackagePin_strategy = st.builds(
    HwPackage::HwPackagePin,
)
HwComponent_strategy = st.builds(
    HwComponent,
)
MARTE::HwPower::HwPowerSupply_strategy = st.builds(
    MARTE::HwPower::HwPowerSupply,
)
MARTE::HwPower::HwCoolingSupply_strategy = st.builds(
    MARTE::HwPower::HwCoolingSupply,
)
MARTE::HwLayout::Env::Condition_strategy = st.builds(
    MARTE::HwLayout::Env::Condition,
    type=
        safe_text,
    status=
        safe_text
)
HwLayout::HwComponent_strategy = st.builds(
    HwLayout::HwComponent,
)
HwLayout::Env::Condition_strategy = st.builds(
    HwLayout::Env::Condition,
)
NFP::Price_strategy = st.builds(
    NFP::Price,
)
Realnterval_strategy = st.builds(
    Realnterval,
)
NFP::Length_strategy = st.builds(
    NFP::Length,
)
HwGeneral::MARTE::Activity_strategy = st.builds(
    HwGeneral::MARTE::Activity,
)
HwGeneral::MARTE::Operation_strategy = st.builds(
    HwGeneral::MARTE::Operation,
)
NFP::Frequency_strategy = st.builds(
    NFP::Frequency,
)
HwCommunication::HwEndPoint_strategy = st.builds(
    HwCommunication::HwEndPoint,
)
HwGeneral::HwResourceService_strategy = st.builds(
    HwGeneral::HwResourceService,
)
NFP::NaturalInterval_strategy = st.builds(
    NFP::NaturalInterval,
)
NFP::Area_strategy = st.builds(
    NFP::Area,
)
HwPeripheral::PeripheralActivity_strategy = st.builds(
    HwPeripheral::PeripheralActivity,
)
HwPeripheral::OperationImpl_strategy = st.builds(
    HwPeripheral::OperationImpl,
)
HwI::O_strategy = st.builds(
    HwI::O,
)
MARTE::HwDevice::HWSensor_strategy = st.builds(
    MARTE::HwDevice::HWSensor,
)
MARTE::HwDevice::HWActuator_strategy = st.builds(
    MARTE::HwDevice::HWActuator,
)
HwDevice_strategy = st.builds(
    HwDevice,
)
MARTE::HwDevice::HwPeripheral_strategy = st.builds(
    MARTE::HwDevice::HwPeripheral,
)
MARTE::HwDevice::HwSupport_strategy = st.builds(
    MARTE::HwDevice::HwSupport,
)
MARTE::HwDevice::HwI::O_strategy = st.builds(
    MARTE::HwDevice::HwI::O,
)
HwTimingResource_strategy = st.builds(
    HwTimingResource,
)
MARTE::HwTiming::HwTimer_strategy = st.builds(
    MARTE::HwTiming::HwTimer,
)
MARTE::HwTiming::HwClock_strategy = st.builds(
    MARTE::HwTiming::HwClock,
)
GRM::TimingResource_strategy = st.builds(
    GRM::TimingResource,
)
HwMemory::CacheStructure_strategy = st.builds(
    HwMemory::CacheStructure,
)
HwDeviceFunction::HwDeviceFunction_strategy = st.builds(
    HwDeviceFunction::HwDeviceFunction,
)
GRM::DeviceResource_strategy = st.builds(
    GRM::DeviceResource,
)
HwTiming::HwClock_strategy = st.builds(
    HwTiming::HwClock,
)
HwMemory::MemoryOrganization_strategy = st.builds(
    HwMemory::MemoryOrganization,
)
HwMemory_strategy = st.builds(
    HwMemory,
)
MARTE::HwMemory::HwDrive_strategy = st.builds(
    MARTE::HwMemory::HwDrive,
)
MARTE::HwMemory::HwCache_strategy = st.builds(
    MARTE::HwMemory::HwCache,
    writePolicy=
        safe_text,
    repl_Policy=
        safe_text,
    type=
        safe_text
)
MARTE::HwRegister::HwRegister_strategy = st.builds(
    MARTE::HwRegister::HwRegister,
    address=
        safe_text
)
MARTE::HwMemory::HwRAM_strategy = st.builds(
    MARTE::HwMemory::HwRAM,
    repl_Policy=
        safe_text,
    writePolicy=
        safe_text
)
MARTE::HwMemory::MemoryOrganization_strategy = st.builds(
    MARTE::HwMemory::MemoryOrganization,
)
MARTE::HwMemory::CacheStructure_strategy = st.builds(
    MARTE::HwMemory::CacheStructure,
)
MARTE::HwMemory::HwROM_strategy = st.builds(
    MARTE::HwMemory::HwROM,
    type=
        safe_text
)
MARTE::HwMemory::Timing_strategy = st.builds(
    MARTE::HwMemory::Timing,
)
HwMemory::Timing_strategy = st.builds(
    HwMemory::Timing,
)
HwStorageManager::HwStorageManager_strategy = st.builds(
    HwStorageManager::HwStorageManager,
)
HwMemory::HwMemory_strategy = st.builds(
    HwMemory::HwMemory,
)
GRM::StorageResource_strategy = st.builds(
    GRM::StorageResource,
)
HwProtocol::HwProtocol_strategy = st.builds(
    HwProtocol::HwProtocol,
)
HwEndPoint_strategy = st.builds(
    HwEndPoint,
)
MARTE::HwIO::HwPin_strategy = st.builds(
    MARTE::HwIO::HwPin,
)
MARTE::HwPackage::HwPackagePin_strategy = st.builds(
    MARTE::HwPackage::HwPackagePin,
    pinNo=
        safe_text,
    altNames=
        safe_text
)
MARTE::HwCommunication::HwPort_strategy = st.builds(
    MARTE::HwCommunication::HwPort,
)
GRM::CommunicationEndPoint_strategy = st.builds(
    GRM::CommunicationEndPoint,
)
NFP::Boolean_strategy = st.builds(
    NFP::Boolean,
)
HwStorageManager_strategy = st.builds(
    HwStorageManager,
)
MARTE::HwStorageManager::HwMMU_strategy = st.builds(
    MARTE::HwStorageManager::HwMMU,
)
HwCommunication::HwCommunicationResource_strategy = st.builds(
    HwCommunication::HwCommunicationResource,
)
MARTE::HwCommunication::HwEndPoint_strategy = st.builds(
    MARTE::HwCommunication::HwEndPoint,
)
GRM::CommunicationMedia_strategy = st.builds(
    GRM::CommunicationMedia,
)
MARTE::SW::Interaction::SwCommunicationResource_strategy = st.builds(
    MARTE::SW::Interaction::SwCommunicationResource,
)
MARTE::HwCommunication::HwMedia_strategy = st.builds(
    MARTE::HwCommunication::HwMedia,
)
HwCommunication::HwMedia_strategy = st.builds(
    HwCommunication::HwMedia,
)
HwCommunicationResource_strategy = st.builds(
    HwCommunicationResource,
)
MARTE::HwCommunication::HwArbiter_strategy = st.builds(
    MARTE::HwCommunication::HwArbiter,
)
HwCommunication::HwPort_strategy = st.builds(
    HwCommunication::HwPort,
)
HwIO::HwPin_strategy = st.builds(
    HwIO::HwPin,
)
HwPackage::HwPackage_strategy = st.builds(
    HwPackage::HwPackage,
)
HwRegister::HwRegister_strategy = st.builds(
    HwRegister::HwRegister,
)
HwDevice::HwPeripheral_strategy = st.builds(
    HwDevice::HwPeripheral,
)
HwComputing::HwProcessor_strategy = st.builds(
    HwComputing::HwProcessor,
)
HwComputing::HwComputingResource_strategy = st.builds(
    HwComputing::HwComputingResource,
)
HwMedia_strategy = st.builds(
    HwMedia,
)
MARTE::HwCommunication::HwConnection_strategy = st.builds(
    MARTE::HwCommunication::HwConnection,
)
MARTE::HwPackage::HwWire_strategy = st.builds(
    MARTE::HwPackage::HwWire,
)
MARTE::HwIO::HwLine_strategy = st.builds(
    MARTE::HwIO::HwLine,
)
MARTE::HwCommunication::HwBridge_strategy = st.builds(
    MARTE::HwCommunication::HwBridge,
)
MARTE::HwCommunication::HwBus_strategy = st.builds(
    MARTE::HwCommunication::HwBus,
)
HwCommunication::HwArbiter_strategy = st.builds(
    HwCommunication::HwArbiter,
)
MARTE::HwStorageManager::HwDMA_strategy = st.builds(
    MARTE::HwStorageManager::HwDMA,
)
HwComputing::PLD::Organization_strategy = st.builds(
    HwComputing::PLD::Organization,
)
NFP::String_strategy = st.builds(
    NFP::String,
)
HwResource_strategy = st.builds(
    HwResource,
)
MARTE::HwCommunication::HwCommunicationResource_strategy = st.builds(
    MARTE::HwCommunication::HwCommunicationResource,
)
MARTE::HwComputing::HwBranchPredictor_strategy = st.builds(
    MARTE::HwComputing::HwBranchPredictor,
)
MARTE::HwLayout::HwComponent_strategy = st.builds(
    MARTE::HwLayout::HwComponent,
    kind=
        safe_text
)
MARTE::HwComputing::HwISA_strategy = st.builds(
    MARTE::HwComputing::HwISA,
    type=
        safe_text
)
NFP::FrequencyInterval_strategy = st.builds(
    NFP::FrequencyInterval,
)
HwGeneral::HwResource_strategy = st.builds(
    HwGeneral::HwResource,
)
MARTE::HwStorageManager::HwStorageManager_strategy = st.builds(
    MARTE::HwStorageManager::HwStorageManager,
)
MARTE::HwMemory::HwMemory_strategy = st.builds(
    MARTE::HwMemory::HwMemory,
)
MARTE::HwTiming::HwTimingResource_strategy = st.builds(
    MARTE::HwTiming::HwTimingResource,
)
MARTE::HwDevice::HwDevice_strategy = st.builds(
    MARTE::HwDevice::HwDevice,
)
HwStorageManager::HwMMU_strategy = st.builds(
    HwStorageManager::HwMMU,
)
HwMemory::HwCache_strategy = st.builds(
    HwMemory::HwCache,
)
HwComputing::HwBranchPredictor_strategy = st.builds(
    HwComputing::HwBranchPredictor,
)
HwMemory::HwRAM_strategy = st.builds(
    HwMemory::HwRAM,
)
HwComputingResource_strategy = st.builds(
    HwComputingResource,
)
MARTE::HwComputing::HwASIC_strategy = st.builds(
    MARTE::HwComputing::HwASIC,
)
MARTE::HwComputing::HwMCU_strategy = st.builds(
    MARTE::HwComputing::HwMCU,
)
MARTE::HwComputing::HwPLD_strategy = st.builds(
    MARTE::HwComputing::HwPLD,
    technology=
        safe_text
)
MARTE::HwComputing::HwProcessor_strategy = st.builds(
    MARTE::HwComputing::HwProcessor,
)
NFP::Natural_strategy = st.builds(
    NFP::Natural,
)
MARTE::HwComputing::PLD::Organization_strategy = st.builds(
    MARTE::HwComputing::PLD::Organization,
    class_=
        safe_text
)
HwComputing::HwISA_strategy = st.builds(
    HwComputing::HwISA,
)
MARTE::HLAM::RtService_strategy = st.builds(
    MARTE::HLAM::RtService,
    exeKind=
        safe_text,
    concPolicy=
        safe_text,
    synchKind=
        safe_text,
    isAtomic=
        safe_text
)
MARTE::HLAM::RtAction_strategy = st.builds(
    MARTE::HLAM::RtAction,
    synchKind=
        safe_text,
    isAtomic=
        safe_text
)
NFP::DateTime_strategy = st.builds(
    NFP::DateTime,
)
HLAM::MARTE::Comment_strategy = st.builds(
    HLAM::MARTE::Comment,
)
NFP::Percentage_strategy = st.builds(
    NFP::Percentage,
)
HLAM::RtSpecification_strategy = st.builds(
    HLAM::RtSpecification,
)
HLAM::MARTE::InvocationAction_strategy = st.builds(
    HLAM::MARTE::InvocationAction,
)
HLAM::MARTE::Port_strategy = st.builds(
    HLAM::MARTE::Port,
)
HLAM::MARTE::Signal_strategy = st.builds(
    HLAM::MARTE::Signal,
)
HLAM::MARTE::Message_strategy = st.builds(
    HLAM::MARTE::Message,
)
HLAM::MARTE::BehavioralFeature_strategy = st.builds(
    HLAM::MARTE::BehavioralFeature,
)
MARTE::HLAM::RtFeature_strategy = st.builds(
    MARTE::HLAM::RtFeature,
)
MARTE::HLAM::PpUnit_strategy = st.builds(
    MARTE::HLAM::PpUnit,
    concPolicy=
        safe_text
)
Time::TimedInstantObservation_strategy = st.builds(
    Time::TimedInstantObservation,
)
ArrivalPattern_strategy = st.builds(
    ArrivalPattern,
)
UtilityType_strategy = st.builds(
    UtilityType,
)
MARTE::HLAM::RtSpecification_strategy = st.builds(
    MARTE::HLAM::RtSpecification,
)
HLAM::MARTE::Operation_strategy = st.builds(
    HLAM::MARTE::Operation,
)
HLAM::MARTE::Behavior_strategy = st.builds(
    HLAM::MARTE::Behavior,
)
MARTE::HLAM::RtUnit_strategy = st.builds(
    MARTE::HLAM::RtUnit,
    srPoolSize=
        safe_text,
    isMain=
        safe_text,
    srPoolPolicy=
        safe_text,
    isDynamic=
        safe_text,
    queueSchedPolicy=
        safe_text,
    queueSize=
        safe_text
)
MARTE::DataTypes::TupleType_strategy = st.builds(
    MARTE::DataTypes::TupleType,
)
MARTE::DataTypes::ChoiceType_strategy = st.builds(
    MARTE::DataTypes::ChoiceType,
)
HLAM::MARTE::BehavioredClassifier_strategy = st.builds(
    HLAM::MARTE::BehavioredClassifier,
)
DataTypes::MARTE::Property_strategy = st.builds(
    DataTypes::MARTE::Property,
)
MARTE::DataTypes::BoundedSubtype_strategy = st.builds(
    MARTE::DataTypes::BoundedSubtype,
    isMinOpen=
        st.booleans(),
    maxValue=
        safe_text,
    isMaxOpen=
        st.booleans(),
    minValue=
        safe_text
)
Variables::MARTE::NamedElement_strategy = st.builds(
    Variables::MARTE::NamedElement,
)
MARTE::Variables::ExpressionContext_strategy = st.builds(
    MARTE::Variables::ExpressionContext,
)
Variables::MARTE::Property_strategy = st.builds(
    Variables::MARTE::Property,
)
MARTE::Variables::Var_strategy = st.builds(
    MARTE::Variables::Var,
    dir=
        safe_text
)
RSM::MARTE::MultiplicityElement_strategy = st.builds(
    RSM::MARTE::MultiplicityElement,
)
MARTE::RSM::Shaped_strategy = st.builds(
    MARTE::RSM::Shaped,
)
RSM::MARTE::ConnectorEnd_strategy = st.builds(
    RSM::MARTE::ConnectorEnd,
)
MARTE::DataTypes::CollectionType_strategy = st.builds(
    MARTE::DataTypes::CollectionType,
)
MARTE::DataTypes::IntervalType_strategy = st.builds(
    MARTE::DataTypes::IntervalType,
)
DataTypes::MARTE::DataType_strategy = st.builds(
    DataTypes::MARTE::DataType,
)
TilerSpecification_strategy = st.builds(
    TilerSpecification,
)
ShapeSpecification_strategy = st.builds(
    ShapeSpecification,
)
Allocate_strategy = st.builds(
    Allocate,
)
MARTE::SW::Concurrency::EntryPoint_strategy = st.builds(
    MARTE::SW::Concurrency::EntryPoint,
    isReentrant=
        safe_text
)
MARTE::CoreElements::ModeTransition_strategy = st.builds(
    MARTE::CoreElements::ModeTransition,
)
NFPs::MARTE::Enumeration_strategy = st.builds(
    NFPs::MARTE::Enumeration,
)
NFPs::Dimension_strategy = st.builds(
    NFPs::Dimension,
)
MARTE::NFPs::Dimension_strategy = st.builds(
    MARTE::NFPs::Dimension,
    symbol=
        safe_text,
    baseExponent=
        st.integers()
)
TupleType_strategy = st.builds(
    TupleType,
)
MARTE::NFPs::NfpType_strategy = st.builds(
    MARTE::NFPs::NfpType,
)
CoreElements::Mode_strategy = st.builds(
    CoreElements::Mode,
)
NFPs::MARTE::Constraint_strategy = st.builds(
    NFPs::MARTE::Constraint,
)
MARTE::NFPs::NfpConstraint_strategy = st.builds(
    MARTE::NFPs::NfpConstraint,
    kind=
        safe_text
)
NFPs::MARTE::EnumerationLiteral_strategy = st.builds(
    NFPs::MARTE::EnumerationLiteral,
)
CoreElements::MARTE::Package_strategy = st.builds(
    CoreElements::MARTE::Package,
)
CoreElements::MARTE::StructuredClassifier_strategy = st.builds(
    CoreElements::MARTE::StructuredClassifier,
)
MARTE::CoreElements::Configuration_strategy = st.builds(
    MARTE::CoreElements::Configuration,
)
CoreElements::MARTE::StateMachine_strategy = st.builds(
    CoreElements::MARTE::StateMachine,
)
MARTE::CoreElements::ModeBehavior_strategy = st.builds(
    MARTE::CoreElements::ModeBehavior,
)
MARTE::NFPs::Nfp_strategy = st.builds(
    MARTE::NFPs::Nfp,
)
NFPs::Unit_strategy = st.builds(
    NFPs::Unit,
)
MARTE::NFPs::Unit_strategy = st.builds(
    MARTE::NFPs::Unit,
    convFactor=
        safe_text,
    offsetFactor=
        safe_text
)
NFPs::MARTE::Property_strategy = st.builds(
    NFPs::MARTE::Property,
)
MARTE::RSM::Distribute_strategy = st.builds(
    MARTE::RSM::Distribute,
)
IntegerVector_strategy = st.builds(
    IntegerVector,
)
LinkTopology_strategy = st.builds(
    LinkTopology,
)
MARTE::RSM::Reshape_strategy = st.builds(
    MARTE::RSM::Reshape,
)
MARTE::RSM::InterRepetition_strategy = st.builds(
    MARTE::RSM::InterRepetition,
    isModulo=
        safe_text
)
MARTE::RSM::DefaultLink_strategy = st.builds(
    MARTE::RSM::DefaultLink,
)
RSM::MARTE::Connector_strategy = st.builds(
    RSM::MARTE::Connector,
)
MARTE::RSM::LinkTopology_strategy = st.builds(
    MARTE::RSM::LinkTopology,
)
IntegerMatrix_strategy = st.builds(
    IntegerMatrix,
)
MARTE::RSM::Tiler_strategy = st.builds(
    MARTE::RSM::Tiler,
)
NFP::Energy_strategy = st.builds(
    NFP::Energy,
)
NFP::Power_strategy = st.builds(
    NFP::Power,
)
NFP::DataSize_strategy = st.builds(
    NFP::DataSize,
)
MARTE::GRM::ResourceUsage_strategy = st.builds(
    MARTE::GRM::ResourceUsage,
)
GrService_strategy = st.builds(
    GrService,
)
MARTE::HwGeneral::HwResourceService_strategy = st.builds(
    MARTE::HwGeneral::HwResourceService,
)
MARTE::SW::ResourceCore::SwAccessService_strategy = st.builds(
    MARTE::SW::ResourceCore::SwAccessService,
    isModifier=
        safe_text
)
MARTE::GRM::Acquire_strategy = st.builds(
    MARTE::GRM::Acquire,
    isBlocking=
        safe_text
)
MARTE::GRM::Release_strategy = st.builds(
    MARTE::GRM::Release,
)
GRM::MARTE::CollaborationUse_strategy = st.builds(
    GRM::MARTE::CollaborationUse,
)
GRM::MARTE::Collaboration_strategy = st.builds(
    GRM::MARTE::Collaboration,
)
GRM::MARTE::Behavior_strategy = st.builds(
    GRM::MARTE::Behavior,
)
GRM::MARTE::BehavioralFeature_strategy = st.builds(
    GRM::MARTE::BehavioralFeature,
)
GRM::MARTE::ExecutionSpecification_strategy = st.builds(
    GRM::MARTE::ExecutionSpecification,
)
GRM::Resource_strategy = st.builds(
    GRM::Resource,
)
MARTE::GRM::GrService_strategy = st.builds(
    MARTE::GRM::GrService,
)
GRM::ResourceUsage_strategy = st.builds(
    GRM::ResourceUsage,
)
MARTE::GQAM::GaScenario_strategy = st.builds(
    MARTE::GQAM::GaScenario,
)
GRM::MARTE::NamedElement_strategy = st.builds(
    GRM::MARTE::NamedElement,
)
NFP::DataTxRate_strategy = st.builds(
    NFP::DataTxRate,
)
NFP::Duration_strategy = st.builds(
    NFP::Duration,
)
GRM::MARTE::Connector_strategy = st.builds(
    GRM::MARTE::Connector,
)
Scheduler_strategy = st.builds(
    Scheduler,
)
MARTE::GRM::SecondaryScheduler_strategy = st.builds(
    MARTE::GRM::SecondaryScheduler,
)
GRM::SecondaryScheduler_strategy = st.builds(
    GRM::SecondaryScheduler,
)
SchedParameters_strategy = st.builds(
    SchedParameters,
)
TimingResource_strategy = st.builds(
    TimingResource,
)
MARTE::GRM::TimerResource_strategy = st.builds(
    MARTE::GRM::TimerResource,
    isPeriodic=
        safe_text
)
MARTE::GRM::ClockResource_strategy = st.builds(
    MARTE::GRM::ClockResource,
)
GRM::Scheduler_strategy = st.builds(
    GRM::Scheduler,
)
MARTE::GQAM::GaCommHost_strategy = st.builds(
    MARTE::GQAM::GaCommHost,
)
NFP::Real_strategy = st.builds(
    NFP::Real,
)
GRM::SchedulableResource_strategy = st.builds(
    GRM::SchedulableResource,
)
MARTE::SW::Concurrency::SwSchedulableResource_strategy = st.builds(
    MARTE::SW::Concurrency::SwSchedulableResource,
    isPreemptable=
        safe_text,
    isStaticSchedulingFeature=
        safe_text
)
GRM::MutualExclusionResource_strategy = st.builds(
    GRM::MutualExclusionResource,
)
MARTE::SW::Interaction::SwMutualExclusionResource_strategy = st.builds(
    MARTE::SW::Interaction::SwMutualExclusionResource,
    concurrentAccessProtocol=
        safe_text,
    mechanism=
        safe_text
)
GRM::ComputingResource_strategy = st.builds(
    GRM::ComputingResource,
)
MARTE::GQAM::GaExecHost_strategy = st.builds(
    MARTE::GQAM::GaExecHost,
)
MARTE::HwComputing::HwComputingResource_strategy = st.builds(
    MARTE::HwComputing::HwComputingResource,
)
GRM::ProcessingResource_strategy = st.builds(
    GRM::ProcessingResource,
)
GRM::MARTE::OpaqueExpression_strategy = st.builds(
    GRM::MARTE::OpaqueExpression,
)
ProcessingResource_strategy = st.builds(
    ProcessingResource,
)
MARTE::GRM::CommunicationMedia_strategy = st.builds(
    MARTE::GRM::CommunicationMedia,
    transmMode=
        safe_text
)
MARTE::GRM::DeviceResource_strategy = st.builds(
    MARTE::GRM::DeviceResource,
)
MARTE::GRM::ComputingResource_strategy = st.builds(
    MARTE::GRM::ComputingResource,
)
GRM::MARTE::InstanceSpecification_strategy = st.builds(
    GRM::MARTE::InstanceSpecification,
)
GRM::MARTE::Property_strategy = st.builds(
    GRM::MARTE::Property,
)
NFP::Integer_strategy = st.builds(
    NFP::Integer,
)
MARTE::GRM::Resource_strategy = st.builds(
    MARTE::GRM::Resource,
    isProtected=
        safe_text
)
Time::MARTE::Event_strategy = st.builds(
    Time::MARTE::Event,
)
Time::MARTE::Message_strategy = st.builds(
    Time::MARTE::Message,
)
Time::MARTE::Behavior_strategy = st.builds(
    Time::MARTE::Behavior,
)
Time::MARTE::Action_strategy = st.builds(
    Time::MARTE::Action,
)
Time::MARTE::TimeEvent_strategy = st.builds(
    Time::MARTE::TimeEvent,
)
Resource_strategy = st.builds(
    Resource,
)
MARTE::GRM::Scheduler_strategy = st.builds(
    MARTE::GRM::Scheduler,
    isPreemptible=
        safe_text,
    schedPolicy=
        safe_text,
    otherSchedPolicy=
        safe_text
)
MARTE::PAM::PaLogicalResource_strategy = st.builds(
    MARTE::PAM::PaLogicalResource,
)
MARTE::GRM::SynchronizationResource_strategy = st.builds(
    MARTE::GRM::SynchronizationResource,
)
MARTE::GRM::MutualExclusionResource_strategy = st.builds(
    MARTE::GRM::MutualExclusionResource,
    protectKind=
        safe_text,
    otherProtectProtocol=
        safe_text
)
MARTE::GRM::CommunicationEndPoint_strategy = st.builds(
    MARTE::GRM::CommunicationEndPoint,
)
MARTE::HwGeneral::HwResource_strategy = st.builds(
    MARTE::HwGeneral::HwResource,
    name=
        safe_text
)
MARTE::GRM::SchedulableResource_strategy = st.builds(
    MARTE::GRM::SchedulableResource,
)
MARTE::GRM::ConcurrencyResource_strategy = st.builds(
    MARTE::GRM::ConcurrencyResource,
)
MARTE::SW::ResourceCore::SwResource_strategy = st.builds(
    MARTE::SW::ResourceCore::SwResource,
)
MARTE::GRM::TimingResource_strategy = st.builds(
    MARTE::GRM::TimingResource,
)
MARTE::GRM::ProcessingResource_strategy = st.builds(
    MARTE::GRM::ProcessingResource,
)
MARTE::GRM::StorageResource_strategy = st.builds(
    MARTE::GRM::StorageResource,
)
GRM::MARTE::ConnectableElement_strategy = st.builds(
    GRM::MARTE::ConnectableElement,
)
GRM::MARTE::Lifeline_strategy = st.builds(
    GRM::MARTE::Lifeline,
)
GRM::MARTE::Classifier_strategy = st.builds(
    GRM::MARTE::Classifier,
)
TimedObservation_strategy = st.builds(
    TimedObservation,
)
MARTE::Time::TimedInstantObservation_strategy = st.builds(
    MARTE::Time::TimedInstantObservation,
    obsKind=
        safe_text
)
Time::TimedElement_strategy = st.builds(
    Time::TimedElement,
)
Time::MARTE::ValueSpecification_strategy = st.builds(
    Time::MARTE::ValueSpecification,
)
TimedElement_strategy = st.builds(
    TimedElement,
)
MARTE::Time::TimedObservation_strategy = st.builds(
    MARTE::Time::TimedObservation,
)
MARTE::Time::TimedProcessing_strategy = st.builds(
    MARTE::Time::TimedProcessing,
)
MARTE::Time::TimedValueSpecification_strategy = st.builds(
    MARTE::Time::TimedValueSpecification,
    interpretation=
        safe_text
)
Time::Clock_strategy = st.builds(
    Time::Clock,
)
MARTE::Time::TimedElement_strategy = st.builds(
    MARTE::Time::TimedElement,
)
Time::MARTE::Class_strategy = st.builds(
    Time::MARTE::Class,
)
MARTE::Time::TimedEvent_strategy = st.builds(
    MARTE::Time::TimedEvent,
    repetition=
        safe_text
)
Time::MARTE::DurationObservation_strategy = st.builds(
    Time::MARTE::DurationObservation,
)
MARTE::Time::TimedDurationObservation_strategy = st.builds(
    MARTE::Time::TimedDurationObservation,
    obsKind=
        safe_text
)
Time::MARTE::TimeObservation_strategy = st.builds(
    Time::MARTE::TimeObservation,
)
Time::MARTE::Enumeration_strategy = st.builds(
    Time::MARTE::Enumeration,
)
MARTE::Time::ClockType_strategy = st.builds(
    MARTE::Time::ClockType,
    isLogical=
        safe_text,
    nature=
        safe_text
)
Time::MARTE::Property_strategy = st.builds(
    Time::MARTE::Property,
)
Time::ClockType_strategy = st.builds(
    Time::ClockType,
)
Time::MARTE::InstanceSpecification_strategy = st.builds(
    Time::MARTE::InstanceSpecification,
)
MARTE::Time::Clock_strategy = st.builds(
    MARTE::Time::Clock,
    standard=
        safe_text
)
Time::MARTE::Namespace_strategy = st.builds(
    Time::MARTE::Namespace,
)
MARTE::Time::TimedDomain_strategy = st.builds(
    MARTE::Time::TimedDomain,
)
Alloc::MARTE::Abstraction_strategy = st.builds(
    Alloc::MARTE::Abstraction,
)
MARTE::Alloc::Allocate_strategy = st.builds(
    MARTE::Alloc::Allocate,
    kind=
        safe_text,
    nature=
        safe_text
)
Time::MARTE::Operation_strategy = st.builds(
    Time::MARTE::Operation,
)
MARTE::Alloc::Assign_strategy = st.builds(
    MARTE::Alloc::Assign,
)
NFPs::NfpConstraint_strategy = st.builds(
    NFPs::NfpConstraint,
)
MARTE::Time::ClockConstraint_strategy = st.builds(
    MARTE::Time::ClockConstraint,
    isChronometricBased=
        safe_text,
    isCoincidenceBased=
        safe_text,
    isPrecedenceBased=
        st.booleans()
)
MARTE::Time::TimedConstraint_strategy = st.builds(
    MARTE::Time::TimedConstraint,
    interpretation=
        safe_text
)
Alloc::MARTE::Dependency_strategy = st.builds(
    Alloc::MARTE::Dependency,
)
MARTE::Alloc::NfpRefine_strategy = st.builds(
    MARTE::Alloc::NfpRefine,
)
Alloc::MARTE::ActivityPartition_strategy = st.builds(
    Alloc::MARTE::ActivityPartition,
)
MARTE::Alloc::AllocateActivityGroup_strategy = st.builds(
    MARTE::Alloc::AllocateActivityGroup,
)
Alloc::Allocated_strategy = st.builds(
    Alloc::Allocated,
)
Alloc::MARTE::NamedElement_strategy = st.builds(
    Alloc::MARTE::NamedElement,
)
MARTE::Alloc::Allocated_strategy = st.builds(
    MARTE::Alloc::Allocated,
)
CoreElements::MARTE::State_strategy = st.builds(
    CoreElements::MARTE::State,
)
MARTE::CoreElements::Mode_strategy = st.builds(
    MARTE::CoreElements::Mode,
)
Alloc::MARTE::Comment_strategy = st.builds(
    Alloc::MARTE::Comment,
)
Alloc::MARTE::Element_strategy = st.builds(
    Alloc::MARTE::Element,
)
CoreElements::MARTE::Transition_strategy = st.builds(
    CoreElements::MARTE::Transition,
)

@given(instance=GQAM::GaCommStep_strategy)
@settings(max_examples=50)
def test_gqam::gacommstep_instantiation(instance):
    assert isinstance(instance, GQAM::GaCommStep)

@given(instance=PAM::PaStep_strategy)
@settings(max_examples=50)
def test_pam::pastep_instantiation(instance):
    assert isinstance(instance, PAM::PaStep)

@given(instance=MARTE::PAM::PaCommStep_strategy)
@settings(max_examples=50)
def test_marte::pam::pacommstep_instantiation(instance):
    assert isinstance(instance, MARTE::PAM::PaCommStep)

@given(instance=MARTE::PAM::PaRunTInstance_strategy)
@settings(max_examples=50)
def test_marte::pam::paruntinstance_instantiation(instance):
    assert isinstance(instance, MARTE::PAM::PaRunTInstance)

@given(instance=MARTE::PAM::PaRunTInstance_strategy)
def test_marte::pam::paruntinstance_unbddPool_type(instance):
    assert isinstance(instance.unbddPool, str)


@given(instance=MARTE::PAM::PaRunTInstance_strategy)
def test_marte::pam::paruntinstance_unbddPool_setter(instance):
    original = instance.unbddPool
    instance.unbddPool = original
    assert instance.unbddPool == original

@given(instance=GaExecHost_strategy)
@settings(max_examples=50)
def test_gaexechost_instantiation(instance):
    assert isinstance(instance, GaExecHost)

@given(instance=MARTE::SAM::SaExecHost_strategy)
@settings(max_examples=50)
def test_marte::sam::saexechost_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaExecHost)

@given(instance=MutualExclusionResource_strategy)
@settings(max_examples=50)
def test_mutualexclusionresource_instantiation(instance):
    assert isinstance(instance, MutualExclusionResource)

@given(instance=MARTE::SAM::SaSharedResource_strategy)
@settings(max_examples=50)
def test_marte::sam::sasharedresource_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaSharedResource)

@given(instance=GaCommHost_strategy)
@settings(max_examples=50)
def test_gacommhost_instantiation(instance):
    assert isinstance(instance, GaCommHost)

@given(instance=MARTE::SAM::SaCommHost_strategy)
@settings(max_examples=50)
def test_marte::sam::sacommhost_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaCommHost)

@given(instance=SAM::MARTE::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sam::marte::behavioralfeature_instantiation(instance):
    assert isinstance(instance, SAM::MARTE::BehavioralFeature)

@given(instance=SAM::SaSharedResource_strategy)
@settings(max_examples=50)
def test_sam::sasharedresource_instantiation(instance):
    assert isinstance(instance, SAM::SaSharedResource)

@given(instance=GaAnalysisContext_strategy)
@settings(max_examples=50)
def test_gaanalysiscontext_instantiation(instance):
    assert isinstance(instance, GaAnalysisContext)

@given(instance=MARTE::SAM::SaAnalysisContext_strategy)
@settings(max_examples=50)
def test_marte::sam::saanalysiscontext_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaAnalysisContext)

@given(instance=MARTE::SAM::SaAnalysisContext_strategy)
def test_marte::sam::saanalysiscontext_optCriterion_type(instance):
    assert isinstance(instance.optCriterion, str)


@given(instance=MARTE::SAM::SaAnalysisContext_strategy)
def test_marte::sam::saanalysiscontext_optCriterion_setter(instance):
    original = instance.optCriterion
    instance.optCriterion = original
    assert instance.optCriterion == original

@given(instance=GQAM::MARTE::Classifier_strategy)
@settings(max_examples=50)
def test_gqam::marte::classifier_instantiation(instance):
    assert isinstance(instance, GQAM::MARTE::Classifier)

@given(instance=GaCommStep_strategy)
@settings(max_examples=50)
def test_gacommstep_instantiation(instance):
    assert isinstance(instance, GaCommStep)

@given(instance=MARTE::SAM::SaCommStep_strategy)
@settings(max_examples=50)
def test_marte::sam::sacommstep_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaCommStep)

@given(instance=SAM::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_sam::marte::namedelement_instantiation(instance):
    assert isinstance(instance, SAM::MARTE::NamedElement)

@given(instance=MARTE::SAM::SaEndtoEndFlow_strategy)
@settings(max_examples=50)
def test_marte::sam::saendtoendflow_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaEndtoEndFlow)

@given(instance=SchedulableResource_strategy)
@settings(max_examples=50)
def test_schedulableresource_instantiation(instance):
    assert isinstance(instance, SchedulableResource)

@given(instance=MARTE::GQAM::GaCommChannel_strategy)
@settings(max_examples=50)
def test_marte::gqam::gacommchannel_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaCommChannel)

@given(instance=MARTE::GQAM::GaResourcesPlatform_strategy)
@settings(max_examples=50)
def test_marte::gqam::garesourcesplatform_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaResourcesPlatform)

@given(instance=GQAM::GaResourcesPlatform_strategy)
@settings(max_examples=50)
def test_gqam::garesourcesplatform_instantiation(instance):
    assert isinstance(instance, GQAM::GaResourcesPlatform)

@given(instance=GQAM::GaWorkloadBehavior_strategy)
@settings(max_examples=50)
def test_gqam::gaworkloadbehavior_instantiation(instance):
    assert isinstance(instance, GQAM::GaWorkloadBehavior)

@given(instance=Variables::ExpressionContext_strategy)
@settings(max_examples=50)
def test_variables::expressioncontext_instantiation(instance):
    assert isinstance(instance, Variables::ExpressionContext)

@given(instance=CoreElements::Configuration_strategy)
@settings(max_examples=50)
def test_coreelements::configuration_instantiation(instance):
    assert isinstance(instance, CoreElements::Configuration)

@given(instance=MARTE::GQAM::GaAnalysisContext_strategy)
@settings(max_examples=50)
def test_marte::gqam::gaanalysiscontext_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaAnalysisContext)

@given(instance=MARTE::GQAM::GaWorkloadBehavior_strategy)
@settings(max_examples=50)
def test_marte::gqam::gaworkloadbehavior_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaWorkloadBehavior)

@given(instance=GaTimedObs_strategy)
@settings(max_examples=50)
def test_gatimedobs_instantiation(instance):
    assert isinstance(instance, GaTimedObs)

@given(instance=MARTE::SAM::SaSchedObs_strategy)
@settings(max_examples=50)
def test_marte::sam::saschedobs_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaSchedObs)

@given(instance=MARTE::GQAM::GaLatencyObs_strategy)
@settings(max_examples=50)
def test_marte::gqam::galatencyobs_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaLatencyObs)

@given(instance=GQAM::MARTE::TimeObservation_strategy)
@settings(max_examples=50)
def test_gqam::marte::timeobservation_instantiation(instance):
    assert isinstance(instance, GQAM::MARTE::TimeObservation)

@given(instance=NfpConstraint_strategy)
@settings(max_examples=50)
def test_nfpconstraint_instantiation(instance):
    assert isinstance(instance, NfpConstraint)

@given(instance=MARTE::GQAM::GaTimedObs_strategy)
@settings(max_examples=50)
def test_marte::gqam::gatimedobs_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaTimedObs)

@given(instance=MARTE::GQAM::GaTimedObs_strategy)
def test_marte::gqam::gatimedobs_laxity_type(instance):
    assert isinstance(instance.laxity, str)


@given(instance=MARTE::GQAM::GaTimedObs_strategy)
def test_marte::gqam::gatimedobs_laxity_setter(instance):
    original = instance.laxity
    instance.laxity = original
    assert instance.laxity == original

@given(instance=GQAM::MARTE::Operation_strategy)
@settings(max_examples=50)
def test_gqam::marte::operation_instantiation(instance):
    assert isinstance(instance, GQAM::MARTE::Operation)

@given(instance=GaStep_strategy)
@settings(max_examples=50)
def test_gastep_instantiation(instance):
    assert isinstance(instance, GaStep)

@given(instance=MARTE::SAM::SaStep_strategy)
@settings(max_examples=50)
def test_marte::sam::sastep_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaStep)

@given(instance=MARTE::GQAM::GaCommStep_strategy)
@settings(max_examples=50)
def test_marte::gqam::gacommstep_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaCommStep)

@given(instance=MARTE::GQAM::GaRelStep_strategy)
@settings(max_examples=50)
def test_marte::gqam::garelstep_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaRelStep)

@given(instance=MARTE::GQAM::GaAcqStep_strategy)
@settings(max_examples=50)
def test_marte::gqam::gaacqstep_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaAcqStep)

@given(instance=MARTE::PAM::PaStep_strategy)
@settings(max_examples=50)
def test_marte::pam::pastep_instantiation(instance):
    assert isinstance(instance, MARTE::PAM::PaStep)

@given(instance=MARTE::PAM::PaStep_strategy)
def test_marte::pam::pastep_extOpDemand_type(instance):
    assert isinstance(instance.extOpDemand, str)


@given(instance=MARTE::PAM::PaStep_strategy)
def test_marte::pam::pastep_extOpDemand_setter(instance):
    original = instance.extOpDemand
    instance.extOpDemand = original
    assert instance.extOpDemand == original

@given(instance=MARTE::GQAM::GaRequestedService_strategy)
@settings(max_examples=50)
def test_marte::gqam::garequestedservice_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaRequestedService)

@given(instance=IntegerInterval_strategy)
@settings(max_examples=50)
def test_integerinterval_instantiation(instance):
    assert isinstance(instance, IntegerInterval)

@given(instance=GaScenario_strategy)
@settings(max_examples=50)
def test_gascenario_instantiation(instance):
    assert isinstance(instance, GaScenario)

@given(instance=MARTE::GQAM::GaStep_strategy)
@settings(max_examples=50)
def test_marte::gqam::gastep_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaStep)

@given(instance=GQAM::GaTimedObs_strategy)
@settings(max_examples=50)
def test_gqam::gatimedobs_instantiation(instance):
    assert isinstance(instance, GQAM::GaTimedObs)

@given(instance=GQAM::GaStep_strategy)
@settings(max_examples=50)
def test_gqam::gastep_instantiation(instance):
    assert isinstance(instance, GQAM::GaStep)

@given(instance=GQAM::GaRequestedService_strategy)
@settings(max_examples=50)
def test_gqam::garequestedservice_instantiation(instance):
    assert isinstance(instance, GQAM::GaRequestedService)

@given(instance=MARTE::PAM::PaRequestedStep_strategy)
@settings(max_examples=50)
def test_marte::pam::parequestedstep_instantiation(instance):
    assert isinstance(instance, MARTE::PAM::PaRequestedStep)

@given(instance=GQAM::GaExecHost_strategy)
@settings(max_examples=50)
def test_gqam::gaexechost_instantiation(instance):
    assert isinstance(instance, GQAM::GaExecHost)

@given(instance=GQAM::GaWorkloadEvent_strategy)
@settings(max_examples=50)
def test_gqam::gaworkloadevent_instantiation(instance):
    assert isinstance(instance, GQAM::GaWorkloadEvent)

@given(instance=Time::TimedProcessing_strategy)
@settings(max_examples=50)
def test_time::timedprocessing_instantiation(instance):
    assert isinstance(instance, Time::TimedProcessing)

@given(instance=MARTE::GQAM::GaWorkloadGenerator_strategy)
@settings(max_examples=50)
def test_marte::gqam::gaworkloadgenerator_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaWorkloadGenerator)

@given(instance=GCM::MARTE::Behavior_strategy)
@settings(max_examples=50)
def test_gcm::marte::behavior_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Behavior)

@given(instance=GQAM::MARTE::TimeEvent_strategy)
@settings(max_examples=50)
def test_gqam::marte::timeevent_instantiation(instance):
    assert isinstance(instance, GQAM::MARTE::TimeEvent)

@given(instance=GQAM::GaScenario_strategy)
@settings(max_examples=50)
def test_gqam::gascenario_instantiation(instance):
    assert isinstance(instance, GQAM::GaScenario)

@given(instance=GQAM::GaEventTrace_strategy)
@settings(max_examples=50)
def test_gqam::gaeventtrace_instantiation(instance):
    assert isinstance(instance, GQAM::GaEventTrace)

@given(instance=GQAM::GaWorkloadGenerator_strategy)
@settings(max_examples=50)
def test_gqam::gaworkloadgenerator_instantiation(instance):
    assert isinstance(instance, GQAM::GaWorkloadGenerator)

@given(instance=MARTE::GQAM::GaWorkloadEvent_strategy)
@settings(max_examples=50)
def test_marte::gqam::gaworkloadevent_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaWorkloadEvent)

@given(instance=GQAM::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_gqam::marte::namedelement_instantiation(instance):
    assert isinstance(instance, GQAM::MARTE::NamedElement)

@given(instance=MARTE::GQAM::GaEventTrace_strategy)
@settings(max_examples=50)
def test_marte::gqam::gaeventtrace_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaEventTrace)

@given(instance=MARTE::GQAM::GaEventTrace_strategy)
def test_marte::gqam::gaeventtrace_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=MARTE::GQAM::GaEventTrace_strategy)
def test_marte::gqam::gaeventtrace_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=MARTE::GQAM::GaEventTrace_strategy)
def test_marte::gqam::gaeventtrace_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=MARTE::GQAM::GaEventTrace_strategy)
def test_marte::gqam::gaeventtrace_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=MARTE::GQAM::GaEventTrace_strategy)
def test_marte::gqam::gaeventtrace_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=MARTE::GQAM::GaEventTrace_strategy)
def test_marte::gqam::gaeventtrace_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=GQAM::MARTE::Behavior_strategy)
@settings(max_examples=50)
def test_gqam::marte::behavior_instantiation(instance):
    assert isinstance(instance, GQAM::MARTE::Behavior)

@given(instance=MARTE::GCM::FlowSpecification_strategy)
@settings(max_examples=50)
def test_marte::gcm::flowspecification_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::FlowSpecification)

@given(instance=MARTE::GCM::ClientServerSpecification_strategy)
@settings(max_examples=50)
def test_marte::gcm::clientserverspecification_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::ClientServerSpecification)

@given(instance=MARTE::GCM::DataPool_strategy)
@settings(max_examples=50)
def test_marte::gcm::datapool_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::DataPool)

@given(instance=MARTE::GCM::DataPool_strategy)
def test_marte::gcm::datapool_ordering_type(instance):
    assert isinstance(instance.ordering, str)


@given(instance=MARTE::GCM::DataPool_strategy)
def test_marte::gcm::datapool_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=GCM::MARTE::Classifier_strategy)
@settings(max_examples=50)
def test_gcm::marte::classifier_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Classifier)

@given(instance=GCM::MARTE::AnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_gcm::marte::anyreceiveevent_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::AnyReceiveEvent)

@given(instance=MARTE::GCM::DataEvent_strategy)
@settings(max_examples=50)
def test_marte::gcm::dataevent_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::DataEvent)

@given(instance=GCM::MARTE::InvocationAction_strategy)
@settings(max_examples=50)
def test_gcm::marte::invocationaction_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::InvocationAction)

@given(instance=MARTE::GCM::GCMInvocationAction_strategy)
@settings(max_examples=50)
def test_marte::gcm::gcminvocationaction_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::GCMInvocationAction)

@given(instance=GCM::MARTE::Feature_strategy)
@settings(max_examples=50)
def test_gcm::marte::feature_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Feature)

@given(instance=GCM::MARTE::Trigger_strategy)
@settings(max_examples=50)
def test_gcm::marte::trigger_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Trigger)

@given(instance=MARTE::GCM::GCMTrigger_strategy)
@settings(max_examples=50)
def test_marte::gcm::gcmtrigger_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::GCMTrigger)

@given(instance=GCM::MARTE::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_gcm::marte::behavioralfeature_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::BehavioralFeature)

@given(instance=MARTE::GCM::ClientServerFeature_strategy)
@settings(max_examples=50)
def test_marte::gcm::clientserverfeature_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::ClientServerFeature)

@given(instance=MARTE::GCM::ClientServerFeature_strategy)
def test_marte::gcm::clientserverfeature_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::GCM::ClientServerFeature_strategy)
def test_marte::gcm::clientserverfeature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=GCM::MARTE::Property_strategy)
@settings(max_examples=50)
def test_gcm::marte::property_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Property)

@given(instance=MARTE::GCM::FlowProperty_strategy)
@settings(max_examples=50)
def test_marte::gcm::flowproperty_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::FlowProperty)

@given(instance=MARTE::GCM::FlowProperty_strategy)
def test_marte::gcm::flowproperty_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=MARTE::GCM::FlowProperty_strategy)
def test_marte::gcm::flowproperty_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=GCM::ClientServerSpecification_strategy)
@settings(max_examples=50)
def test_gcm::clientserverspecification_instantiation(instance):
    assert isinstance(instance, GCM::ClientServerSpecification)

@given(instance=GCM::MARTE::Interface_strategy)
@settings(max_examples=50)
def test_gcm::marte::interface_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Interface)

@given(instance=MARTE::GCM::ClientServerPort_strategy)
@settings(max_examples=50)
def test_marte::gcm::clientserverport_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::ClientServerPort)

@given(instance=MARTE::GCM::ClientServerPort_strategy)
def test_marte::gcm::clientserverport_specificationKind_type(instance):
    assert isinstance(instance.specificationKind, str)


@given(instance=MARTE::GCM::ClientServerPort_strategy)
def test_marte::gcm::clientserverport_specificationKind_setter(instance):
    original = instance.specificationKind
    instance.specificationKind = original
    assert instance.specificationKind == original

@given(instance=MARTE::GCM::ClientServerPort_strategy)
def test_marte::gcm::clientserverport_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::GCM::ClientServerPort_strategy)
def test_marte::gcm::clientserverport_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MARTE::GCM::ClientServerPort_strategy)
def test_marte::gcm::clientserverport_isConjugated_type(instance):
    assert isinstance(instance.isConjugated, str)


@given(instance=MARTE::GCM::ClientServerPort_strategy)
def test_marte::gcm::clientserverport_isConjugated_setter(instance):
    original = instance.isConjugated
    instance.isConjugated = original
    assert instance.isConjugated == original

@given(instance=GCM::MARTE::Port_strategy)
@settings(max_examples=50)
def test_gcm::marte::port_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Port)

@given(instance=MARTE::GCM::FlowPort_strategy)
@settings(max_examples=50)
def test_marte::gcm::flowport_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::FlowPort)

@given(instance=MARTE::GCM::FlowPort_strategy)
def test_marte::gcm::flowport_isAtomic_type(instance):
    assert isinstance(instance.isAtomic, str)


@given(instance=MARTE::GCM::FlowPort_strategy)
def test_marte::gcm::flowport_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original

@given(instance=MARTE::GCM::FlowPort_strategy)
def test_marte::gcm::flowport_isConjugated_type(instance):
    assert isinstance(instance.isConjugated, str)


@given(instance=MARTE::GCM::FlowPort_strategy)
def test_marte::gcm::flowport_isConjugated_setter(instance):
    original = instance.isConjugated
    instance.isConjugated = original
    assert instance.isConjugated == original

@given(instance=MARTE::GCM::FlowPort_strategy)
def test_marte::gcm::flowport_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=MARTE::GCM::FlowPort_strategy)
def test_marte::gcm::flowport_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=SwSynchronizationResource_strategy)
@settings(max_examples=50)
def test_swsynchronizationresource_instantiation(instance):
    assert isinstance(instance, SwSynchronizationResource)

@given(instance=MARTE::SW::Interaction::NotificationResource_strategy)
@settings(max_examples=50)
def test_marte::sw::interaction::notificationresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Interaction::NotificationResource)

@given(instance=MARTE::SW::Interaction::NotificationResource_strategy)
def test_marte::sw::interaction::notificationresource_occurence_type(instance):
    assert isinstance(instance.occurence, str)


@given(instance=MARTE::SW::Interaction::NotificationResource_strategy)
def test_marte::sw::interaction::notificationresource_occurence_setter(instance):
    original = instance.occurence
    instance.occurence = original
    assert instance.occurence == original

@given(instance=MARTE::SW::Interaction::NotificationResource_strategy)
def test_marte::sw::interaction::notificationresource_mechanism_type(instance):
    assert isinstance(instance.mechanism, str)


@given(instance=MARTE::SW::Interaction::NotificationResource_strategy)
def test_marte::sw::interaction::notificationresource_mechanism_setter(instance):
    original = instance.mechanism
    instance.mechanism = original
    assert instance.mechanism == original

@given(instance=SW::Interaction::SwSynchronizationResource_strategy)
@settings(max_examples=50)
def test_sw::interaction::swsynchronizationresource_instantiation(instance):
    assert isinstance(instance, SW::Interaction::SwSynchronizationResource)

@given(instance=SW::Interaction::MARTE::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw::interaction::marte::behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW::Interaction::MARTE::BehavioralFeature)

@given(instance=SwCommunicationResource_strategy)
@settings(max_examples=50)
def test_swcommunicationresource_instantiation(instance):
    assert isinstance(instance, SwCommunicationResource)

@given(instance=MARTE::SW::Interaction::MessageComResource_strategy)
@settings(max_examples=50)
def test_marte::sw::interaction::messagecomresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Interaction::MessageComResource)

@given(instance=MARTE::SW::Interaction::MessageComResource_strategy)
def test_marte::sw::interaction::messagecomresource_mechanism_type(instance):
    assert isinstance(instance.mechanism, str)


@given(instance=MARTE::SW::Interaction::MessageComResource_strategy)
def test_marte::sw::interaction::messagecomresource_mechanism_setter(instance):
    original = instance.mechanism
    instance.mechanism = original
    assert instance.mechanism == original

@given(instance=MARTE::SW::Interaction::MessageComResource_strategy)
def test_marte::sw::interaction::messagecomresource_isFixedMessageSize_type(instance):
    assert isinstance(instance.isFixedMessageSize, str)


@given(instance=MARTE::SW::Interaction::MessageComResource_strategy)
def test_marte::sw::interaction::messagecomresource_isFixedMessageSize_setter(instance):
    original = instance.isFixedMessageSize
    instance.isFixedMessageSize = original
    assert instance.isFixedMessageSize == original

@given(instance=MARTE::SW::Interaction::MessageComResource_strategy)
def test_marte::sw::interaction::messagecomresource_messageQueuePolicy_type(instance):
    assert isinstance(instance.messageQueuePolicy, str)


@given(instance=MARTE::SW::Interaction::MessageComResource_strategy)
def test_marte::sw::interaction::messagecomresource_messageQueuePolicy_setter(instance):
    original = instance.messageQueuePolicy
    instance.messageQueuePolicy = original
    assert instance.messageQueuePolicy == original

@given(instance=MARTE::SW::Interaction::SharedDataComResource_strategy)
@settings(max_examples=50)
def test_marte::sw::interaction::shareddatacomresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Interaction::SharedDataComResource)

@given(instance=GRM::SynchronizationResource_strategy)
@settings(max_examples=50)
def test_grm::synchronizationresource_instantiation(instance):
    assert isinstance(instance, GRM::SynchronizationResource)

@given(instance=SW::Interaction::SwInteractionResource_strategy)
@settings(max_examples=50)
def test_sw::interaction::swinteractionresource_instantiation(instance):
    assert isinstance(instance, SW::Interaction::SwInteractionResource)

@given(instance=MARTE::SW::Interaction::SwSynchronizationResource_strategy)
@settings(max_examples=50)
def test_marte::sw::interaction::swsynchronizationresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Interaction::SwSynchronizationResource)

@given(instance=SW::Interaction::MARTE::TypedElement_strategy)
@settings(max_examples=50)
def test_sw::interaction::marte::typedelement_instantiation(instance):
    assert isinstance(instance, SW::Interaction::MARTE::TypedElement)

@given(instance=SW::Brokering::MARTE::Activity_strategy)
@settings(max_examples=50)
def test_sw::brokering::marte::activity_instantiation(instance):
    assert isinstance(instance, SW::Brokering::MARTE::Activity)

@given(instance=SW::Brokering::MARTE::Operation_strategy)
@settings(max_examples=50)
def test_sw::brokering::marte::operation_instantiation(instance):
    assert isinstance(instance, SW::Brokering::MARTE::Operation)

@given(instance=SW::Brokering::MARTE::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw::brokering::marte::behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW::Brokering::MARTE::BehavioralFeature)

@given(instance=SW::Brokering::MARTE::TypedElement_strategy)
@settings(max_examples=50)
def test_sw::brokering::marte::typedelement_instantiation(instance):
    assert isinstance(instance, SW::Brokering::MARTE::TypedElement)

@given(instance=InterruptResource_strategy)
@settings(max_examples=50)
def test_interruptresource_instantiation(instance):
    assert isinstance(instance, InterruptResource)

@given(instance=MARTE::SW::Concurrency::Alarm_strategy)
@settings(max_examples=50)
def test_marte::sw::concurrency::alarm_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Concurrency::Alarm)

@given(instance=MARTE::SW::Concurrency::Alarm_strategy)
def test_marte::sw::concurrency::alarm_isWatchdog_type(instance):
    assert isinstance(instance.isWatchdog, str)


@given(instance=MARTE::SW::Concurrency::Alarm_strategy)
def test_marte::sw::concurrency::alarm_isWatchdog_setter(instance):
    original = instance.isWatchdog
    instance.isWatchdog = original
    assert instance.isWatchdog == original

@given(instance=SW::Concurrency::MARTE::Namespace_strategy)
@settings(max_examples=50)
def test_sw::concurrency::marte::namespace_instantiation(instance):
    assert isinstance(instance, SW::Concurrency::MARTE::Namespace)

@given(instance=TimerResource_strategy)
@settings(max_examples=50)
def test_timerresource_instantiation(instance):
    assert isinstance(instance, TimerResource)

@given(instance=MARTE::SW::Concurrency::SwTimerResource_strategy)
@settings(max_examples=50)
def test_marte::sw::concurrency::swtimerresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Concurrency::SwTimerResource)

@given(instance=SW::Concurrency::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_sw::concurrency::marte::namedelement_instantiation(instance):
    assert isinstance(instance, SW::Concurrency::MARTE::NamedElement)

@given(instance=SW::Concurrency::SwConcurrentResource_strategy)
@settings(max_examples=50)
def test_sw::concurrency::swconcurrentresource_instantiation(instance):
    assert isinstance(instance, SW::Concurrency::SwConcurrentResource)

@given(instance=SwConcurrentResource_strategy)
@settings(max_examples=50)
def test_swconcurrentresource_instantiation(instance):
    assert isinstance(instance, SwConcurrentResource)

@given(instance=MARTE::SW::Concurrency::InterruptResource_strategy)
@settings(max_examples=50)
def test_marte::sw::concurrency::interruptresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Concurrency::InterruptResource)

@given(instance=MARTE::SW::Concurrency::InterruptResource_strategy)
def test_marte::sw::concurrency::interruptresource_isMaskable_type(instance):
    assert isinstance(instance.isMaskable, str)


@given(instance=MARTE::SW::Concurrency::InterruptResource_strategy)
def test_marte::sw::concurrency::interruptresource_isMaskable_setter(instance):
    original = instance.isMaskable
    instance.isMaskable = original
    assert instance.isMaskable == original

@given(instance=MARTE::SW::Concurrency::InterruptResource_strategy)
def test_marte::sw::concurrency::interruptresource_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::SW::Concurrency::InterruptResource_strategy)
def test_marte::sw::concurrency::interruptresource_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=SW::Concurrency::MARTE::TypedElement_strategy)
@settings(max_examples=50)
def test_sw::concurrency::marte::typedelement_instantiation(instance):
    assert isinstance(instance, SW::Concurrency::MARTE::TypedElement)

@given(instance=SW::Concurrency::MARTE::Element_strategy)
@settings(max_examples=50)
def test_sw::concurrency::marte::element_instantiation(instance):
    assert isinstance(instance, SW::Concurrency::MARTE::Element)

@given(instance=SwResource_strategy)
@settings(max_examples=50)
def test_swresource_instantiation(instance):
    assert isinstance(instance, SwResource)

@given(instance=MARTE::SW::Interaction::SwInteractionResource_strategy)
@settings(max_examples=50)
def test_marte::sw::interaction::swinteractionresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Interaction::SwInteractionResource)

@given(instance=MARTE::SW::Interaction::SwInteractionResource_strategy)
def test_marte::sw::interaction::swinteractionresource_waitingQueueCapacity_type(instance):
    assert isinstance(instance.waitingQueueCapacity, str)


@given(instance=MARTE::SW::Interaction::SwInteractionResource_strategy)
def test_marte::sw::interaction::swinteractionresource_waitingQueueCapacity_setter(instance):
    original = instance.waitingQueueCapacity
    instance.waitingQueueCapacity = original
    assert instance.waitingQueueCapacity == original

@given(instance=MARTE::SW::Interaction::SwInteractionResource_strategy)
def test_marte::sw::interaction::swinteractionresource_waitingQueuePolicy_type(instance):
    assert isinstance(instance.waitingQueuePolicy, str)


@given(instance=MARTE::SW::Interaction::SwInteractionResource_strategy)
def test_marte::sw::interaction::swinteractionresource_waitingQueuePolicy_setter(instance):
    original = instance.waitingQueuePolicy
    instance.waitingQueuePolicy = original
    assert instance.waitingQueuePolicy == original

@given(instance=MARTE::SW::Interaction::SwInteractionResource_strategy)
def test_marte::sw::interaction::swinteractionresource_isIntraMemoryPartitionInteraction_type(instance):
    assert isinstance(instance.isIntraMemoryPartitionInteraction, bool)


@given(instance=MARTE::SW::Interaction::SwInteractionResource_strategy)
def test_marte::sw::interaction::swinteractionresource_isIntraMemoryPartitionInteraction_setter(instance):
    original = instance.isIntraMemoryPartitionInteraction
    instance.isIntraMemoryPartitionInteraction = original
    assert instance.isIntraMemoryPartitionInteraction == original

@given(instance=MARTE::SW::Brokering::MemoryBroker_strategy)
@settings(max_examples=50)
def test_marte::sw::brokering::memorybroker_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Brokering::MemoryBroker)

@given(instance=MARTE::SW::Brokering::MemoryBroker_strategy)
def test_marte::sw::brokering::memorybroker_accessPolicy_type(instance):
    assert isinstance(instance.accessPolicy, str)


@given(instance=MARTE::SW::Brokering::MemoryBroker_strategy)
def test_marte::sw::brokering::memorybroker_accessPolicy_setter(instance):
    original = instance.accessPolicy
    instance.accessPolicy = original
    assert instance.accessPolicy == original

@given(instance=MARTE::SW::Concurrency::MemoryPartition_strategy)
@settings(max_examples=50)
def test_marte::sw::concurrency::memorypartition_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Concurrency::MemoryPartition)

@given(instance=MARTE::SW::Brokering::DeviceBroker_strategy)
@settings(max_examples=50)
def test_marte::sw::brokering::devicebroker_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Brokering::DeviceBroker)

@given(instance=MARTE::SW::Brokering::DeviceBroker_strategy)
def test_marte::sw::brokering::devicebroker_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MARTE::SW::Brokering::DeviceBroker_strategy)
def test_marte::sw::brokering::devicebroker_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MARTE::SW::Brokering::DeviceBroker_strategy)
def test_marte::sw::brokering::devicebroker_accessPolicy_type(instance):
    assert isinstance(instance.accessPolicy, str)


@given(instance=MARTE::SW::Brokering::DeviceBroker_strategy)
def test_marte::sw::brokering::devicebroker_accessPolicy_setter(instance):
    original = instance.accessPolicy
    instance.accessPolicy = original
    assert instance.accessPolicy == original

@given(instance=MARTE::SW::Brokering::DeviceBroker_strategy)
def test_marte::sw::brokering::devicebroker_isBuffered_type(instance):
    assert isinstance(instance.isBuffered, str)


@given(instance=MARTE::SW::Brokering::DeviceBroker_strategy)
def test_marte::sw::brokering::devicebroker_isBuffered_setter(instance):
    original = instance.isBuffered
    instance.isBuffered = original
    assert instance.isBuffered == original

@given(instance=MARTE::SW::Concurrency::SwConcurrentResource_strategy)
@settings(max_examples=50)
def test_marte::sw::concurrency::swconcurrentresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Concurrency::SwConcurrentResource)

@given(instance=MARTE::SW::Concurrency::SwConcurrentResource_strategy)
def test_marte::sw::concurrency::swconcurrentresource_activationCapacity_type(instance):
    assert isinstance(instance.activationCapacity, str)


@given(instance=MARTE::SW::Concurrency::SwConcurrentResource_strategy)
def test_marte::sw::concurrency::swconcurrentresource_activationCapacity_setter(instance):
    original = instance.activationCapacity
    instance.activationCapacity = original
    assert instance.activationCapacity == original

@given(instance=SW::ResourceCore::MARTE::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw::resourcecore::marte::behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW::ResourceCore::MARTE::BehavioralFeature)

@given(instance=SW::ResourceCore::MARTE::TypedElement_strategy)
@settings(max_examples=50)
def test_sw::resourcecore::marte::typedelement_instantiation(instance):
    assert isinstance(instance, SW::ResourceCore::MARTE::TypedElement)

@given(instance=SW::Concurrency::MARTE::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw::concurrency::marte::behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW::Concurrency::MARTE::BehavioralFeature)

@given(instance=SW::Brokering::DeviceBroker_strategy)
@settings(max_examples=50)
def test_sw::brokering::devicebroker_instantiation(instance):
    assert isinstance(instance, SW::Brokering::DeviceBroker)

@given(instance=MARTE::HwDiagram::SRMDiagram_strategy)
@settings(max_examples=50)
def test_marte::hwdiagram::srmdiagram_instantiation(instance):
    assert isinstance(instance, MARTE::HwDiagram::SRMDiagram)

@given(instance=SW::ResourceCore::MARTE::Property_strategy)
@settings(max_examples=50)
def test_sw::resourcecore::marte::property_instantiation(instance):
    assert isinstance(instance, SW::ResourceCore::MARTE::Property)

@given(instance=HwDiagram::MARTE::DataType_strategy)
@settings(max_examples=50)
def test_hwdiagram::marte::datatype_instantiation(instance):
    assert isinstance(instance, HwDiagram::MARTE::DataType)

@given(instance=MARTE::HwDiagram::HwCircuitDiagram_strategy)
@settings(max_examples=50)
def test_marte::hwdiagram::hwcircuitdiagram_instantiation(instance):
    assert isinstance(instance, MARTE::HwDiagram::HwCircuitDiagram)

@given(instance=MARTE::HwDiagram::HwCircuitDiagram_strategy)
def test_marte::hwdiagram::hwcircuitdiagram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MARTE::HwDiagram::HwCircuitDiagram_strategy)
def test_marte::hwdiagram::hwcircuitdiagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HwCommunication::HwConnection_strategy)
@settings(max_examples=50)
def test_hwcommunication::hwconnection_instantiation(instance):
    assert isinstance(instance, HwCommunication::HwConnection)

@given(instance=MARTE::HwDiagram::HwHRMDiagram_strategy)
@settings(max_examples=50)
def test_marte::hwdiagram::hwhrmdiagram_instantiation(instance):
    assert isinstance(instance, MARTE::HwDiagram::HwHRMDiagram)

@given(instance=MARTE::HwDiagram::HwHRMDiagram_strategy)
def test_marte::hwdiagram::hwhrmdiagram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MARTE::HwDiagram::HwHRMDiagram_strategy)
def test_marte::hwdiagram::hwhrmdiagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HwPackage::HwWire_strategy)
@settings(max_examples=50)
def test_hwpackage::hwwire_instantiation(instance):
    assert isinstance(instance, HwPackage::HwWire)

@given(instance=PAM::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_pam::marte::namedelement_instantiation(instance):
    assert isinstance(instance, PAM::MARTE::NamedElement)

@given(instance=MARTE::PAM::PaResPassStep_strategy)
@settings(max_examples=50)
def test_marte::pam::parespassstep_instantiation(instance):
    assert isinstance(instance, MARTE::PAM::PaResPassStep)

@given(instance=MARTE::HwPackage::HwPackage_strategy)
@settings(max_examples=50)
def test_marte::hwpackage::hwpackage_instantiation(instance):
    assert isinstance(instance, MARTE::HwPackage::HwPackage)

@given(instance=MARTE::HwPackage::HwPackage_strategy)
def test_marte::hwpackage::hwpackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MARTE::HwPackage::HwPackage_strategy)
def test_marte::hwpackage::hwpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MARTE::HwPackage::HwPackage_strategy)
def test_marte::hwpackage::hwpackage_pinNum_type(instance):
    assert isinstance(instance.pinNum, int)


@given(instance=MARTE::HwPackage::HwPackage_strategy)
def test_marte::hwpackage::hwpackage_pinNum_setter(instance):
    original = instance.pinNum
    instance.pinNum = original
    assert instance.pinNum == original

@given(instance=MARTE::HwPackage::HwPackage_strategy)
def test_marte::hwpackage::hwpackage_packageType_type(instance):
    assert isinstance(instance.packageType, str)


@given(instance=MARTE::HwPackage::HwPackage_strategy)
def test_marte::hwpackage::hwpackage_packageType_setter(instance):
    original = instance.packageType
    instance.packageType = original
    assert instance.packageType == original

@given(instance=MARTE::HwDatasheet::HwDatasheet_strategy)
@settings(max_examples=50)
def test_marte::hwdatasheet::hwdatasheet_instantiation(instance):
    assert isinstance(instance, MARTE::HwDatasheet::HwDatasheet)

@given(instance=MARTE::HwDatasheet::HwDatasheet_strategy)
def test_marte::hwdatasheet::hwdatasheet_revision_type(instance):
    assert isinstance(instance.revision, str)


@given(instance=MARTE::HwDatasheet::HwDatasheet_strategy)
def test_marte::hwdatasheet::hwdatasheet_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original

@given(instance=MARTE::HwDatasheet::HwDatasheet_strategy)
def test_marte::hwdatasheet::hwdatasheet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MARTE::HwDatasheet::HwDatasheet_strategy)
def test_marte::hwdatasheet::hwdatasheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MARTE::HwDiagram::HwBlockDiagram_strategy)
@settings(max_examples=50)
def test_marte::hwdiagram::hwblockdiagram_instantiation(instance):
    assert isinstance(instance, MARTE::HwDiagram::HwBlockDiagram)

@given(instance=MARTE::HwDiagram::HwBlockDiagram_strategy)
def test_marte::hwdiagram::hwblockdiagram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MARTE::HwDiagram::HwBlockDiagram_strategy)
def test_marte::hwdiagram::hwblockdiagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HwProtocol::MARTE::Operation_strategy)
@settings(max_examples=50)
def test_hwprotocol::marte::operation_instantiation(instance):
    assert isinstance(instance, HwProtocol::MARTE::Operation)

@given(instance=MARTE::HwProtocol::HwProtocol_strategy)
@settings(max_examples=50)
def test_marte::hwprotocol::hwprotocol_instantiation(instance):
    assert isinstance(instance, MARTE::HwProtocol::HwProtocol)

@given(instance=MARTE::HwProtocol::HwProtocol_strategy)
def test_marte::hwprotocol::hwprotocol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MARTE::HwProtocol::HwProtocol_strategy)
def test_marte::hwprotocol::hwprotocol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HwPeripheral::RegisterAction_strategy)
@settings(max_examples=50)
def test_hwperipheral::registeraction_instantiation(instance):
    assert isinstance(instance, HwPeripheral::RegisterAction)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=MARTE::HwPeripheral::PeripheralActivity_strategy)
@settings(max_examples=50)
def test_marte::hwperipheral::peripheralactivity_instantiation(instance):
    assert isinstance(instance, MARTE::HwPeripheral::PeripheralActivity)

@given(instance=HwPeripheral::MARTE::OutputPin_strategy)
@settings(max_examples=50)
def test_hwperipheral::marte::outputpin_instantiation(instance):
    assert isinstance(instance, HwPeripheral::MARTE::OutputPin)

@given(instance=HwPeripheral::MARTE::InputPin_strategy)
@settings(max_examples=50)
def test_hwperipheral::marte::inputpin_instantiation(instance):
    assert isinstance(instance, HwPeripheral::MARTE::InputPin)

@given(instance=RegisterAction_strategy)
@settings(max_examples=50)
def test_registeraction_instantiation(instance):
    assert isinstance(instance, RegisterAction)

@given(instance=MARTE::HwPeripheral::ReadRegisterAction_strategy)
@settings(max_examples=50)
def test_marte::hwperipheral::readregisteraction_instantiation(instance):
    assert isinstance(instance, MARTE::HwPeripheral::ReadRegisterAction)

@given(instance=MARTE::HwPeripheral::WriteRegisterAction_strategy)
@settings(max_examples=50)
def test_marte::hwperipheral::writeregisteraction_instantiation(instance):
    assert isinstance(instance, MARTE::HwPeripheral::WriteRegisterAction)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=MARTE::HwPeripheral::RegisterAction_strategy)
@settings(max_examples=50)
def test_marte::hwperipheral::registeraction_instantiation(instance):
    assert isinstance(instance, MARTE::HwPeripheral::RegisterAction)

@given(instance=HwPeripheral::MARTE::Operation_strategy)
@settings(max_examples=50)
def test_hwperipheral::marte::operation_instantiation(instance):
    assert isinstance(instance, HwPeripheral::MARTE::Operation)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=MARTE::HwDeviceFunction::HwDeviceFunction_strategy)
@settings(max_examples=50)
def test_marte::hwdevicefunction::hwdevicefunction_instantiation(instance):
    assert isinstance(instance, MARTE::HwDeviceFunction::HwDeviceFunction)

@given(instance=MARTE::HwPeripheral::OperationImpl_strategy)
@settings(max_examples=50)
def test_marte::hwperipheral::operationimpl_instantiation(instance):
    assert isinstance(instance, MARTE::HwPeripheral::OperationImpl)

@given(instance=HwIO::HwLine_strategy)
@settings(max_examples=50)
def test_hwio::hwline_instantiation(instance):
    assert isinstance(instance, HwIO::HwLine)

@given(instance=HwPackage::HwPackagePin_strategy)
@settings(max_examples=50)
def test_hwpackage::hwpackagepin_instantiation(instance):
    assert isinstance(instance, HwPackage::HwPackagePin)

@given(instance=HwComponent_strategy)
@settings(max_examples=50)
def test_hwcomponent_instantiation(instance):
    assert isinstance(instance, HwComponent)

@given(instance=MARTE::HwPower::HwPowerSupply_strategy)
@settings(max_examples=50)
def test_marte::hwpower::hwpowersupply_instantiation(instance):
    assert isinstance(instance, MARTE::HwPower::HwPowerSupply)

@given(instance=MARTE::HwPower::HwCoolingSupply_strategy)
@settings(max_examples=50)
def test_marte::hwpower::hwcoolingsupply_instantiation(instance):
    assert isinstance(instance, MARTE::HwPower::HwCoolingSupply)

@given(instance=MARTE::HwLayout::Env::Condition_strategy)
@settings(max_examples=50)
def test_marte::hwlayout::env::condition_instantiation(instance):
    assert isinstance(instance, MARTE::HwLayout::Env::Condition)

@given(instance=MARTE::HwLayout::Env::Condition_strategy)
def test_marte::hwlayout::env::condition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MARTE::HwLayout::Env::Condition_strategy)
def test_marte::hwlayout::env::condition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MARTE::HwLayout::Env::Condition_strategy)
def test_marte::hwlayout::env::condition_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=MARTE::HwLayout::Env::Condition_strategy)
def test_marte::hwlayout::env::condition_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=HwLayout::HwComponent_strategy)
@settings(max_examples=50)
def test_hwlayout::hwcomponent_instantiation(instance):
    assert isinstance(instance, HwLayout::HwComponent)

@given(instance=HwLayout::Env::Condition_strategy)
@settings(max_examples=50)
def test_hwlayout::env::condition_instantiation(instance):
    assert isinstance(instance, HwLayout::Env::Condition)

@given(instance=NFP::Price_strategy)
@settings(max_examples=50)
def test_nfp::price_instantiation(instance):
    assert isinstance(instance, NFP::Price)

@given(instance=Realnterval_strategy)
@settings(max_examples=50)
def test_realnterval_instantiation(instance):
    assert isinstance(instance, Realnterval)

@given(instance=NFP::Length_strategy)
@settings(max_examples=50)
def test_nfp::length_instantiation(instance):
    assert isinstance(instance, NFP::Length)

@given(instance=HwGeneral::MARTE::Activity_strategy)
@settings(max_examples=50)
def test_hwgeneral::marte::activity_instantiation(instance):
    assert isinstance(instance, HwGeneral::MARTE::Activity)

@given(instance=HwGeneral::MARTE::Operation_strategy)
@settings(max_examples=50)
def test_hwgeneral::marte::operation_instantiation(instance):
    assert isinstance(instance, HwGeneral::MARTE::Operation)

@given(instance=NFP::Frequency_strategy)
@settings(max_examples=50)
def test_nfp::frequency_instantiation(instance):
    assert isinstance(instance, NFP::Frequency)

@given(instance=HwCommunication::HwEndPoint_strategy)
@settings(max_examples=50)
def test_hwcommunication::hwendpoint_instantiation(instance):
    assert isinstance(instance, HwCommunication::HwEndPoint)

@given(instance=HwGeneral::HwResourceService_strategy)
@settings(max_examples=50)
def test_hwgeneral::hwresourceservice_instantiation(instance):
    assert isinstance(instance, HwGeneral::HwResourceService)

@given(instance=NFP::NaturalInterval_strategy)
@settings(max_examples=50)
def test_nfp::naturalinterval_instantiation(instance):
    assert isinstance(instance, NFP::NaturalInterval)

@given(instance=NFP::Area_strategy)
@settings(max_examples=50)
def test_nfp::area_instantiation(instance):
    assert isinstance(instance, NFP::Area)

@given(instance=HwPeripheral::PeripheralActivity_strategy)
@settings(max_examples=50)
def test_hwperipheral::peripheralactivity_instantiation(instance):
    assert isinstance(instance, HwPeripheral::PeripheralActivity)

@given(instance=HwPeripheral::OperationImpl_strategy)
@settings(max_examples=50)
def test_hwperipheral::operationimpl_instantiation(instance):
    assert isinstance(instance, HwPeripheral::OperationImpl)

@given(instance=HwI::O_strategy)
@settings(max_examples=50)
def test_hwi::o_instantiation(instance):
    assert isinstance(instance, HwI::O)

@given(instance=MARTE::HwDevice::HWSensor_strategy)
@settings(max_examples=50)
def test_marte::hwdevice::hwsensor_instantiation(instance):
    assert isinstance(instance, MARTE::HwDevice::HWSensor)

@given(instance=MARTE::HwDevice::HWActuator_strategy)
@settings(max_examples=50)
def test_marte::hwdevice::hwactuator_instantiation(instance):
    assert isinstance(instance, MARTE::HwDevice::HWActuator)

@given(instance=HwDevice_strategy)
@settings(max_examples=50)
def test_hwdevice_instantiation(instance):
    assert isinstance(instance, HwDevice)

@given(instance=MARTE::HwDevice::HwPeripheral_strategy)
@settings(max_examples=50)
def test_marte::hwdevice::hwperipheral_instantiation(instance):
    assert isinstance(instance, MARTE::HwDevice::HwPeripheral)

@given(instance=MARTE::HwDevice::HwSupport_strategy)
@settings(max_examples=50)
def test_marte::hwdevice::hwsupport_instantiation(instance):
    assert isinstance(instance, MARTE::HwDevice::HwSupport)

@given(instance=MARTE::HwDevice::HwI::O_strategy)
@settings(max_examples=50)
def test_marte::hwdevice::hwi::o_instantiation(instance):
    assert isinstance(instance, MARTE::HwDevice::HwI::O)

@given(instance=HwTimingResource_strategy)
@settings(max_examples=50)
def test_hwtimingresource_instantiation(instance):
    assert isinstance(instance, HwTimingResource)

@given(instance=MARTE::HwTiming::HwTimer_strategy)
@settings(max_examples=50)
def test_marte::hwtiming::hwtimer_instantiation(instance):
    assert isinstance(instance, MARTE::HwTiming::HwTimer)

@given(instance=MARTE::HwTiming::HwClock_strategy)
@settings(max_examples=50)
def test_marte::hwtiming::hwclock_instantiation(instance):
    assert isinstance(instance, MARTE::HwTiming::HwClock)

@given(instance=GRM::TimingResource_strategy)
@settings(max_examples=50)
def test_grm::timingresource_instantiation(instance):
    assert isinstance(instance, GRM::TimingResource)

@given(instance=HwMemory::CacheStructure_strategy)
@settings(max_examples=50)
def test_hwmemory::cachestructure_instantiation(instance):
    assert isinstance(instance, HwMemory::CacheStructure)

@given(instance=HwDeviceFunction::HwDeviceFunction_strategy)
@settings(max_examples=50)
def test_hwdevicefunction::hwdevicefunction_instantiation(instance):
    assert isinstance(instance, HwDeviceFunction::HwDeviceFunction)

@given(instance=GRM::DeviceResource_strategy)
@settings(max_examples=50)
def test_grm::deviceresource_instantiation(instance):
    assert isinstance(instance, GRM::DeviceResource)

@given(instance=HwTiming::HwClock_strategy)
@settings(max_examples=50)
def test_hwtiming::hwclock_instantiation(instance):
    assert isinstance(instance, HwTiming::HwClock)

@given(instance=HwMemory::MemoryOrganization_strategy)
@settings(max_examples=50)
def test_hwmemory::memoryorganization_instantiation(instance):
    assert isinstance(instance, HwMemory::MemoryOrganization)

@given(instance=HwMemory_strategy)
@settings(max_examples=50)
def test_hwmemory_instantiation(instance):
    assert isinstance(instance, HwMemory)

@given(instance=MARTE::HwMemory::HwDrive_strategy)
@settings(max_examples=50)
def test_marte::hwmemory::hwdrive_instantiation(instance):
    assert isinstance(instance, MARTE::HwMemory::HwDrive)

@given(instance=MARTE::HwMemory::HwCache_strategy)
@settings(max_examples=50)
def test_marte::hwmemory::hwcache_instantiation(instance):
    assert isinstance(instance, MARTE::HwMemory::HwCache)

@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_writePolicy_type(instance):
    assert isinstance(instance.writePolicy, str)


@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_writePolicy_setter(instance):
    original = instance.writePolicy
    instance.writePolicy = original
    assert instance.writePolicy == original

@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_repl_Policy_type(instance):
    assert isinstance(instance.repl_Policy, str)


@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_repl_Policy_setter(instance):
    original = instance.repl_Policy
    instance.repl_Policy = original
    assert instance.repl_Policy == original

@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MARTE::HwRegister::HwRegister_strategy)
@settings(max_examples=50)
def test_marte::hwregister::hwregister_instantiation(instance):
    assert isinstance(instance, MARTE::HwRegister::HwRegister)

@given(instance=MARTE::HwRegister::HwRegister_strategy)
def test_marte::hwregister::hwregister_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=MARTE::HwRegister::HwRegister_strategy)
def test_marte::hwregister::hwregister_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=MARTE::HwMemory::HwRAM_strategy)
@settings(max_examples=50)
def test_marte::hwmemory::hwram_instantiation(instance):
    assert isinstance(instance, MARTE::HwMemory::HwRAM)

@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_repl_Policy_type(instance):
    assert isinstance(instance.repl_Policy, str)


@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_repl_Policy_setter(instance):
    original = instance.repl_Policy
    instance.repl_Policy = original
    assert instance.repl_Policy == original

@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_writePolicy_type(instance):
    assert isinstance(instance.writePolicy, str)


@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_writePolicy_setter(instance):
    original = instance.writePolicy
    instance.writePolicy = original
    assert instance.writePolicy == original

@given(instance=MARTE::HwMemory::MemoryOrganization_strategy)
@settings(max_examples=50)
def test_marte::hwmemory::memoryorganization_instantiation(instance):
    assert isinstance(instance, MARTE::HwMemory::MemoryOrganization)

@given(instance=MARTE::HwMemory::CacheStructure_strategy)
@settings(max_examples=50)
def test_marte::hwmemory::cachestructure_instantiation(instance):
    assert isinstance(instance, MARTE::HwMemory::CacheStructure)

@given(instance=MARTE::HwMemory::HwROM_strategy)
@settings(max_examples=50)
def test_marte::hwmemory::hwrom_instantiation(instance):
    assert isinstance(instance, MARTE::HwMemory::HwROM)

@given(instance=MARTE::HwMemory::HwROM_strategy)
def test_marte::hwmemory::hwrom_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MARTE::HwMemory::HwROM_strategy)
def test_marte::hwmemory::hwrom_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MARTE::HwMemory::Timing_strategy)
@settings(max_examples=50)
def test_marte::hwmemory::timing_instantiation(instance):
    assert isinstance(instance, MARTE::HwMemory::Timing)

@given(instance=HwMemory::Timing_strategy)
@settings(max_examples=50)
def test_hwmemory::timing_instantiation(instance):
    assert isinstance(instance, HwMemory::Timing)

@given(instance=HwStorageManager::HwStorageManager_strategy)
@settings(max_examples=50)
def test_hwstoragemanager::hwstoragemanager_instantiation(instance):
    assert isinstance(instance, HwStorageManager::HwStorageManager)

@given(instance=HwMemory::HwMemory_strategy)
@settings(max_examples=50)
def test_hwmemory::hwmemory_instantiation(instance):
    assert isinstance(instance, HwMemory::HwMemory)

@given(instance=GRM::StorageResource_strategy)
@settings(max_examples=50)
def test_grm::storageresource_instantiation(instance):
    assert isinstance(instance, GRM::StorageResource)

@given(instance=HwProtocol::HwProtocol_strategy)
@settings(max_examples=50)
def test_hwprotocol::hwprotocol_instantiation(instance):
    assert isinstance(instance, HwProtocol::HwProtocol)

@given(instance=HwEndPoint_strategy)
@settings(max_examples=50)
def test_hwendpoint_instantiation(instance):
    assert isinstance(instance, HwEndPoint)

@given(instance=MARTE::HwIO::HwPin_strategy)
@settings(max_examples=50)
def test_marte::hwio::hwpin_instantiation(instance):
    assert isinstance(instance, MARTE::HwIO::HwPin)

@given(instance=MARTE::HwPackage::HwPackagePin_strategy)
@settings(max_examples=50)
def test_marte::hwpackage::hwpackagepin_instantiation(instance):
    assert isinstance(instance, MARTE::HwPackage::HwPackagePin)

@given(instance=MARTE::HwPackage::HwPackagePin_strategy)
def test_marte::hwpackage::hwpackagepin_pinNo_type(instance):
    assert isinstance(instance.pinNo, str)


@given(instance=MARTE::HwPackage::HwPackagePin_strategy)
def test_marte::hwpackage::hwpackagepin_pinNo_setter(instance):
    original = instance.pinNo
    instance.pinNo = original
    assert instance.pinNo == original

@given(instance=MARTE::HwPackage::HwPackagePin_strategy)
def test_marte::hwpackage::hwpackagepin_altNames_type(instance):
    assert isinstance(instance.altNames, str)


@given(instance=MARTE::HwPackage::HwPackagePin_strategy)
def test_marte::hwpackage::hwpackagepin_altNames_setter(instance):
    original = instance.altNames
    instance.altNames = original
    assert instance.altNames == original

@given(instance=MARTE::HwCommunication::HwPort_strategy)
@settings(max_examples=50)
def test_marte::hwcommunication::hwport_instantiation(instance):
    assert isinstance(instance, MARTE::HwCommunication::HwPort)

@given(instance=GRM::CommunicationEndPoint_strategy)
@settings(max_examples=50)
def test_grm::communicationendpoint_instantiation(instance):
    assert isinstance(instance, GRM::CommunicationEndPoint)

@given(instance=NFP::Boolean_strategy)
@settings(max_examples=50)
def test_nfp::boolean_instantiation(instance):
    assert isinstance(instance, NFP::Boolean)

@given(instance=HwStorageManager_strategy)
@settings(max_examples=50)
def test_hwstoragemanager_instantiation(instance):
    assert isinstance(instance, HwStorageManager)

@given(instance=MARTE::HwStorageManager::HwMMU_strategy)
@settings(max_examples=50)
def test_marte::hwstoragemanager::hwmmu_instantiation(instance):
    assert isinstance(instance, MARTE::HwStorageManager::HwMMU)

@given(instance=HwCommunication::HwCommunicationResource_strategy)
@settings(max_examples=50)
def test_hwcommunication::hwcommunicationresource_instantiation(instance):
    assert isinstance(instance, HwCommunication::HwCommunicationResource)

@given(instance=MARTE::HwCommunication::HwEndPoint_strategy)
@settings(max_examples=50)
def test_marte::hwcommunication::hwendpoint_instantiation(instance):
    assert isinstance(instance, MARTE::HwCommunication::HwEndPoint)

@given(instance=GRM::CommunicationMedia_strategy)
@settings(max_examples=50)
def test_grm::communicationmedia_instantiation(instance):
    assert isinstance(instance, GRM::CommunicationMedia)

@given(instance=MARTE::SW::Interaction::SwCommunicationResource_strategy)
@settings(max_examples=50)
def test_marte::sw::interaction::swcommunicationresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Interaction::SwCommunicationResource)

@given(instance=MARTE::HwCommunication::HwMedia_strategy)
@settings(max_examples=50)
def test_marte::hwcommunication::hwmedia_instantiation(instance):
    assert isinstance(instance, MARTE::HwCommunication::HwMedia)

@given(instance=HwCommunication::HwMedia_strategy)
@settings(max_examples=50)
def test_hwcommunication::hwmedia_instantiation(instance):
    assert isinstance(instance, HwCommunication::HwMedia)

@given(instance=HwCommunicationResource_strategy)
@settings(max_examples=50)
def test_hwcommunicationresource_instantiation(instance):
    assert isinstance(instance, HwCommunicationResource)

@given(instance=MARTE::HwCommunication::HwArbiter_strategy)
@settings(max_examples=50)
def test_marte::hwcommunication::hwarbiter_instantiation(instance):
    assert isinstance(instance, MARTE::HwCommunication::HwArbiter)

@given(instance=HwCommunication::HwPort_strategy)
@settings(max_examples=50)
def test_hwcommunication::hwport_instantiation(instance):
    assert isinstance(instance, HwCommunication::HwPort)

@given(instance=HwIO::HwPin_strategy)
@settings(max_examples=50)
def test_hwio::hwpin_instantiation(instance):
    assert isinstance(instance, HwIO::HwPin)

@given(instance=HwPackage::HwPackage_strategy)
@settings(max_examples=50)
def test_hwpackage::hwpackage_instantiation(instance):
    assert isinstance(instance, HwPackage::HwPackage)

@given(instance=HwRegister::HwRegister_strategy)
@settings(max_examples=50)
def test_hwregister::hwregister_instantiation(instance):
    assert isinstance(instance, HwRegister::HwRegister)

@given(instance=HwDevice::HwPeripheral_strategy)
@settings(max_examples=50)
def test_hwdevice::hwperipheral_instantiation(instance):
    assert isinstance(instance, HwDevice::HwPeripheral)

@given(instance=HwComputing::HwProcessor_strategy)
@settings(max_examples=50)
def test_hwcomputing::hwprocessor_instantiation(instance):
    assert isinstance(instance, HwComputing::HwProcessor)

@given(instance=HwComputing::HwComputingResource_strategy)
@settings(max_examples=50)
def test_hwcomputing::hwcomputingresource_instantiation(instance):
    assert isinstance(instance, HwComputing::HwComputingResource)

@given(instance=HwMedia_strategy)
@settings(max_examples=50)
def test_hwmedia_instantiation(instance):
    assert isinstance(instance, HwMedia)

@given(instance=MARTE::HwCommunication::HwConnection_strategy)
@settings(max_examples=50)
def test_marte::hwcommunication::hwconnection_instantiation(instance):
    assert isinstance(instance, MARTE::HwCommunication::HwConnection)

@given(instance=MARTE::HwPackage::HwWire_strategy)
@settings(max_examples=50)
def test_marte::hwpackage::hwwire_instantiation(instance):
    assert isinstance(instance, MARTE::HwPackage::HwWire)

@given(instance=MARTE::HwIO::HwLine_strategy)
@settings(max_examples=50)
def test_marte::hwio::hwline_instantiation(instance):
    assert isinstance(instance, MARTE::HwIO::HwLine)

@given(instance=MARTE::HwCommunication::HwBridge_strategy)
@settings(max_examples=50)
def test_marte::hwcommunication::hwbridge_instantiation(instance):
    assert isinstance(instance, MARTE::HwCommunication::HwBridge)

@given(instance=MARTE::HwCommunication::HwBus_strategy)
@settings(max_examples=50)
def test_marte::hwcommunication::hwbus_instantiation(instance):
    assert isinstance(instance, MARTE::HwCommunication::HwBus)

@given(instance=HwCommunication::HwArbiter_strategy)
@settings(max_examples=50)
def test_hwcommunication::hwarbiter_instantiation(instance):
    assert isinstance(instance, HwCommunication::HwArbiter)

@given(instance=MARTE::HwStorageManager::HwDMA_strategy)
@settings(max_examples=50)
def test_marte::hwstoragemanager::hwdma_instantiation(instance):
    assert isinstance(instance, MARTE::HwStorageManager::HwDMA)

@given(instance=HwComputing::PLD::Organization_strategy)
@settings(max_examples=50)
def test_hwcomputing::pld::organization_instantiation(instance):
    assert isinstance(instance, HwComputing::PLD::Organization)

@given(instance=NFP::String_strategy)
@settings(max_examples=50)
def test_nfp::string_instantiation(instance):
    assert isinstance(instance, NFP::String)

@given(instance=HwResource_strategy)
@settings(max_examples=50)
def test_hwresource_instantiation(instance):
    assert isinstance(instance, HwResource)

@given(instance=MARTE::HwCommunication::HwCommunicationResource_strategy)
@settings(max_examples=50)
def test_marte::hwcommunication::hwcommunicationresource_instantiation(instance):
    assert isinstance(instance, MARTE::HwCommunication::HwCommunicationResource)

@given(instance=MARTE::HwComputing::HwBranchPredictor_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwbranchpredictor_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwBranchPredictor)

@given(instance=MARTE::HwLayout::HwComponent_strategy)
@settings(max_examples=50)
def test_marte::hwlayout::hwcomponent_instantiation(instance):
    assert isinstance(instance, MARTE::HwLayout::HwComponent)

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MARTE::HwComputing::HwISA_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwisa_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwISA)

@given(instance=MARTE::HwComputing::HwISA_strategy)
def test_marte::hwcomputing::hwisa_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MARTE::HwComputing::HwISA_strategy)
def test_marte::hwcomputing::hwisa_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=NFP::FrequencyInterval_strategy)
@settings(max_examples=50)
def test_nfp::frequencyinterval_instantiation(instance):
    assert isinstance(instance, NFP::FrequencyInterval)

@given(instance=HwGeneral::HwResource_strategy)
@settings(max_examples=50)
def test_hwgeneral::hwresource_instantiation(instance):
    assert isinstance(instance, HwGeneral::HwResource)

@given(instance=MARTE::HwStorageManager::HwStorageManager_strategy)
@settings(max_examples=50)
def test_marte::hwstoragemanager::hwstoragemanager_instantiation(instance):
    assert isinstance(instance, MARTE::HwStorageManager::HwStorageManager)

@given(instance=MARTE::HwMemory::HwMemory_strategy)
@settings(max_examples=50)
def test_marte::hwmemory::hwmemory_instantiation(instance):
    assert isinstance(instance, MARTE::HwMemory::HwMemory)

@given(instance=MARTE::HwTiming::HwTimingResource_strategy)
@settings(max_examples=50)
def test_marte::hwtiming::hwtimingresource_instantiation(instance):
    assert isinstance(instance, MARTE::HwTiming::HwTimingResource)

@given(instance=MARTE::HwDevice::HwDevice_strategy)
@settings(max_examples=50)
def test_marte::hwdevice::hwdevice_instantiation(instance):
    assert isinstance(instance, MARTE::HwDevice::HwDevice)

@given(instance=HwStorageManager::HwMMU_strategy)
@settings(max_examples=50)
def test_hwstoragemanager::hwmmu_instantiation(instance):
    assert isinstance(instance, HwStorageManager::HwMMU)

@given(instance=HwMemory::HwCache_strategy)
@settings(max_examples=50)
def test_hwmemory::hwcache_instantiation(instance):
    assert isinstance(instance, HwMemory::HwCache)

@given(instance=HwComputing::HwBranchPredictor_strategy)
@settings(max_examples=50)
def test_hwcomputing::hwbranchpredictor_instantiation(instance):
    assert isinstance(instance, HwComputing::HwBranchPredictor)

@given(instance=HwMemory::HwRAM_strategy)
@settings(max_examples=50)
def test_hwmemory::hwram_instantiation(instance):
    assert isinstance(instance, HwMemory::HwRAM)

@given(instance=HwComputingResource_strategy)
@settings(max_examples=50)
def test_hwcomputingresource_instantiation(instance):
    assert isinstance(instance, HwComputingResource)

@given(instance=MARTE::HwComputing::HwASIC_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwasic_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwASIC)

@given(instance=MARTE::HwComputing::HwMCU_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwmcu_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwMCU)

@given(instance=MARTE::HwComputing::HwPLD_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwpld_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwPLD)

@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_technology_type(instance):
    assert isinstance(instance.technology, str)


@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_technology_setter(instance):
    original = instance.technology
    instance.technology = original
    assert instance.technology == original

@given(instance=MARTE::HwComputing::HwProcessor_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwprocessor_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwProcessor)

@given(instance=NFP::Natural_strategy)
@settings(max_examples=50)
def test_nfp::natural_instantiation(instance):
    assert isinstance(instance, NFP::Natural)

@given(instance=MARTE::HwComputing::PLD::Organization_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::pld::organization_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::PLD::Organization)

@given(instance=MARTE::HwComputing::PLD::Organization_strategy)
def test_marte::hwcomputing::pld::organization_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=MARTE::HwComputing::PLD::Organization_strategy)
def test_marte::hwcomputing::pld::organization_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=HwComputing::HwISA_strategy)
@settings(max_examples=50)
def test_hwcomputing::hwisa_instantiation(instance):
    assert isinstance(instance, HwComputing::HwISA)

@given(instance=MARTE::HLAM::RtService_strategy)
@settings(max_examples=50)
def test_marte::hlam::rtservice_instantiation(instance):
    assert isinstance(instance, MARTE::HLAM::RtService)

@given(instance=MARTE::HLAM::RtService_strategy)
def test_marte::hlam::rtservice_exeKind_type(instance):
    assert isinstance(instance.exeKind, str)


@given(instance=MARTE::HLAM::RtService_strategy)
def test_marte::hlam::rtservice_exeKind_setter(instance):
    original = instance.exeKind
    instance.exeKind = original
    assert instance.exeKind == original

@given(instance=MARTE::HLAM::RtService_strategy)
def test_marte::hlam::rtservice_concPolicy_type(instance):
    assert isinstance(instance.concPolicy, str)


@given(instance=MARTE::HLAM::RtService_strategy)
def test_marte::hlam::rtservice_concPolicy_setter(instance):
    original = instance.concPolicy
    instance.concPolicy = original
    assert instance.concPolicy == original

@given(instance=MARTE::HLAM::RtService_strategy)
def test_marte::hlam::rtservice_synchKind_type(instance):
    assert isinstance(instance.synchKind, str)


@given(instance=MARTE::HLAM::RtService_strategy)
def test_marte::hlam::rtservice_synchKind_setter(instance):
    original = instance.synchKind
    instance.synchKind = original
    assert instance.synchKind == original

@given(instance=MARTE::HLAM::RtService_strategy)
def test_marte::hlam::rtservice_isAtomic_type(instance):
    assert isinstance(instance.isAtomic, str)


@given(instance=MARTE::HLAM::RtService_strategy)
def test_marte::hlam::rtservice_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original

@given(instance=MARTE::HLAM::RtAction_strategy)
@settings(max_examples=50)
def test_marte::hlam::rtaction_instantiation(instance):
    assert isinstance(instance, MARTE::HLAM::RtAction)

@given(instance=MARTE::HLAM::RtAction_strategy)
def test_marte::hlam::rtaction_synchKind_type(instance):
    assert isinstance(instance.synchKind, str)


@given(instance=MARTE::HLAM::RtAction_strategy)
def test_marte::hlam::rtaction_synchKind_setter(instance):
    original = instance.synchKind
    instance.synchKind = original
    assert instance.synchKind == original

@given(instance=MARTE::HLAM::RtAction_strategy)
def test_marte::hlam::rtaction_isAtomic_type(instance):
    assert isinstance(instance.isAtomic, str)


@given(instance=MARTE::HLAM::RtAction_strategy)
def test_marte::hlam::rtaction_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original

@given(instance=NFP::DateTime_strategy)
@settings(max_examples=50)
def test_nfp::datetime_instantiation(instance):
    assert isinstance(instance, NFP::DateTime)

@given(instance=HLAM::MARTE::Comment_strategy)
@settings(max_examples=50)
def test_hlam::marte::comment_instantiation(instance):
    assert isinstance(instance, HLAM::MARTE::Comment)

@given(instance=NFP::Percentage_strategy)
@settings(max_examples=50)
def test_nfp::percentage_instantiation(instance):
    assert isinstance(instance, NFP::Percentage)

@given(instance=HLAM::RtSpecification_strategy)
@settings(max_examples=50)
def test_hlam::rtspecification_instantiation(instance):
    assert isinstance(instance, HLAM::RtSpecification)

@given(instance=HLAM::MARTE::InvocationAction_strategy)
@settings(max_examples=50)
def test_hlam::marte::invocationaction_instantiation(instance):
    assert isinstance(instance, HLAM::MARTE::InvocationAction)

@given(instance=HLAM::MARTE::Port_strategy)
@settings(max_examples=50)
def test_hlam::marte::port_instantiation(instance):
    assert isinstance(instance, HLAM::MARTE::Port)

@given(instance=HLAM::MARTE::Signal_strategy)
@settings(max_examples=50)
def test_hlam::marte::signal_instantiation(instance):
    assert isinstance(instance, HLAM::MARTE::Signal)

@given(instance=HLAM::MARTE::Message_strategy)
@settings(max_examples=50)
def test_hlam::marte::message_instantiation(instance):
    assert isinstance(instance, HLAM::MARTE::Message)

@given(instance=HLAM::MARTE::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_hlam::marte::behavioralfeature_instantiation(instance):
    assert isinstance(instance, HLAM::MARTE::BehavioralFeature)

@given(instance=MARTE::HLAM::RtFeature_strategy)
@settings(max_examples=50)
def test_marte::hlam::rtfeature_instantiation(instance):
    assert isinstance(instance, MARTE::HLAM::RtFeature)

@given(instance=MARTE::HLAM::PpUnit_strategy)
@settings(max_examples=50)
def test_marte::hlam::ppunit_instantiation(instance):
    assert isinstance(instance, MARTE::HLAM::PpUnit)

@given(instance=MARTE::HLAM::PpUnit_strategy)
def test_marte::hlam::ppunit_concPolicy_type(instance):
    assert isinstance(instance.concPolicy, str)


@given(instance=MARTE::HLAM::PpUnit_strategy)
def test_marte::hlam::ppunit_concPolicy_setter(instance):
    original = instance.concPolicy
    instance.concPolicy = original
    assert instance.concPolicy == original

@given(instance=Time::TimedInstantObservation_strategy)
@settings(max_examples=50)
def test_time::timedinstantobservation_instantiation(instance):
    assert isinstance(instance, Time::TimedInstantObservation)

@given(instance=ArrivalPattern_strategy)
@settings(max_examples=50)
def test_arrivalpattern_instantiation(instance):
    assert isinstance(instance, ArrivalPattern)

@given(instance=UtilityType_strategy)
@settings(max_examples=50)
def test_utilitytype_instantiation(instance):
    assert isinstance(instance, UtilityType)

@given(instance=MARTE::HLAM::RtSpecification_strategy)
@settings(max_examples=50)
def test_marte::hlam::rtspecification_instantiation(instance):
    assert isinstance(instance, MARTE::HLAM::RtSpecification)

@given(instance=HLAM::MARTE::Operation_strategy)
@settings(max_examples=50)
def test_hlam::marte::operation_instantiation(instance):
    assert isinstance(instance, HLAM::MARTE::Operation)

@given(instance=HLAM::MARTE::Behavior_strategy)
@settings(max_examples=50)
def test_hlam::marte::behavior_instantiation(instance):
    assert isinstance(instance, HLAM::MARTE::Behavior)

@given(instance=MARTE::HLAM::RtUnit_strategy)
@settings(max_examples=50)
def test_marte::hlam::rtunit_instantiation(instance):
    assert isinstance(instance, MARTE::HLAM::RtUnit)

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_srPoolSize_type(instance):
    assert isinstance(instance.srPoolSize, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_srPoolSize_setter(instance):
    original = instance.srPoolSize
    instance.srPoolSize = original
    assert instance.srPoolSize == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_isMain_type(instance):
    assert isinstance(instance.isMain, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_isMain_setter(instance):
    original = instance.isMain
    instance.isMain = original
    assert instance.isMain == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_srPoolPolicy_type(instance):
    assert isinstance(instance.srPoolPolicy, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_srPoolPolicy_setter(instance):
    original = instance.srPoolPolicy
    instance.srPoolPolicy = original
    assert instance.srPoolPolicy == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_isDynamic_type(instance):
    assert isinstance(instance.isDynamic, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_queueSchedPolicy_type(instance):
    assert isinstance(instance.queueSchedPolicy, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_queueSchedPolicy_setter(instance):
    original = instance.queueSchedPolicy
    instance.queueSchedPolicy = original
    assert instance.queueSchedPolicy == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_queueSize_type(instance):
    assert isinstance(instance.queueSize, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_queueSize_setter(instance):
    original = instance.queueSize
    instance.queueSize = original
    assert instance.queueSize == original

@given(instance=MARTE::DataTypes::TupleType_strategy)
@settings(max_examples=50)
def test_marte::datatypes::tupletype_instantiation(instance):
    assert isinstance(instance, MARTE::DataTypes::TupleType)

@given(instance=MARTE::DataTypes::ChoiceType_strategy)
@settings(max_examples=50)
def test_marte::datatypes::choicetype_instantiation(instance):
    assert isinstance(instance, MARTE::DataTypes::ChoiceType)

@given(instance=HLAM::MARTE::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_hlam::marte::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, HLAM::MARTE::BehavioredClassifier)

@given(instance=DataTypes::MARTE::Property_strategy)
@settings(max_examples=50)
def test_datatypes::marte::property_instantiation(instance):
    assert isinstance(instance, DataTypes::MARTE::Property)

@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
@settings(max_examples=50)
def test_marte::datatypes::boundedsubtype_instantiation(instance):
    assert isinstance(instance, MARTE::DataTypes::BoundedSubtype)

@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_isMinOpen_type(instance):
    assert isinstance(instance.isMinOpen, bool)


@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_isMinOpen_setter(instance):
    original = instance.isMinOpen
    instance.isMinOpen = original
    assert instance.isMinOpen == original

@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_maxValue_type(instance):
    assert isinstance(instance.maxValue, str)


@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original

@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_isMaxOpen_type(instance):
    assert isinstance(instance.isMaxOpen, bool)


@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_isMaxOpen_setter(instance):
    original = instance.isMaxOpen
    instance.isMaxOpen = original
    assert instance.isMaxOpen == original

@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_minValue_type(instance):
    assert isinstance(instance.minValue, str)


@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original

@given(instance=Variables::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_variables::marte::namedelement_instantiation(instance):
    assert isinstance(instance, Variables::MARTE::NamedElement)

@given(instance=MARTE::Variables::ExpressionContext_strategy)
@settings(max_examples=50)
def test_marte::variables::expressioncontext_instantiation(instance):
    assert isinstance(instance, MARTE::Variables::ExpressionContext)

@given(instance=Variables::MARTE::Property_strategy)
@settings(max_examples=50)
def test_variables::marte::property_instantiation(instance):
    assert isinstance(instance, Variables::MARTE::Property)

@given(instance=MARTE::Variables::Var_strategy)
@settings(max_examples=50)
def test_marte::variables::var_instantiation(instance):
    assert isinstance(instance, MARTE::Variables::Var)

@given(instance=MARTE::Variables::Var_strategy)
def test_marte::variables::var_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=MARTE::Variables::Var_strategy)
def test_marte::variables::var_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=RSM::MARTE::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_rsm::marte::multiplicityelement_instantiation(instance):
    assert isinstance(instance, RSM::MARTE::MultiplicityElement)

@given(instance=MARTE::RSM::Shaped_strategy)
@settings(max_examples=50)
def test_marte::rsm::shaped_instantiation(instance):
    assert isinstance(instance, MARTE::RSM::Shaped)

@given(instance=RSM::MARTE::ConnectorEnd_strategy)
@settings(max_examples=50)
def test_rsm::marte::connectorend_instantiation(instance):
    assert isinstance(instance, RSM::MARTE::ConnectorEnd)

@given(instance=MARTE::DataTypes::CollectionType_strategy)
@settings(max_examples=50)
def test_marte::datatypes::collectiontype_instantiation(instance):
    assert isinstance(instance, MARTE::DataTypes::CollectionType)

@given(instance=MARTE::DataTypes::IntervalType_strategy)
@settings(max_examples=50)
def test_marte::datatypes::intervaltype_instantiation(instance):
    assert isinstance(instance, MARTE::DataTypes::IntervalType)

@given(instance=DataTypes::MARTE::DataType_strategy)
@settings(max_examples=50)
def test_datatypes::marte::datatype_instantiation(instance):
    assert isinstance(instance, DataTypes::MARTE::DataType)

@given(instance=TilerSpecification_strategy)
@settings(max_examples=50)
def test_tilerspecification_instantiation(instance):
    assert isinstance(instance, TilerSpecification)

@given(instance=ShapeSpecification_strategy)
@settings(max_examples=50)
def test_shapespecification_instantiation(instance):
    assert isinstance(instance, ShapeSpecification)

@given(instance=Allocate_strategy)
@settings(max_examples=50)
def test_allocate_instantiation(instance):
    assert isinstance(instance, Allocate)

@given(instance=MARTE::SW::Concurrency::EntryPoint_strategy)
@settings(max_examples=50)
def test_marte::sw::concurrency::entrypoint_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Concurrency::EntryPoint)

@given(instance=MARTE::SW::Concurrency::EntryPoint_strategy)
def test_marte::sw::concurrency::entrypoint_isReentrant_type(instance):
    assert isinstance(instance.isReentrant, str)


@given(instance=MARTE::SW::Concurrency::EntryPoint_strategy)
def test_marte::sw::concurrency::entrypoint_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original

@given(instance=MARTE::CoreElements::ModeTransition_strategy)
@settings(max_examples=50)
def test_marte::coreelements::modetransition_instantiation(instance):
    assert isinstance(instance, MARTE::CoreElements::ModeTransition)

@given(instance=NFPs::MARTE::Enumeration_strategy)
@settings(max_examples=50)
def test_nfps::marte::enumeration_instantiation(instance):
    assert isinstance(instance, NFPs::MARTE::Enumeration)

@given(instance=NFPs::Dimension_strategy)
@settings(max_examples=50)
def test_nfps::dimension_instantiation(instance):
    assert isinstance(instance, NFPs::Dimension)

@given(instance=MARTE::NFPs::Dimension_strategy)
@settings(max_examples=50)
def test_marte::nfps::dimension_instantiation(instance):
    assert isinstance(instance, MARTE::NFPs::Dimension)

@given(instance=MARTE::NFPs::Dimension_strategy)
def test_marte::nfps::dimension_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=MARTE::NFPs::Dimension_strategy)
def test_marte::nfps::dimension_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=MARTE::NFPs::Dimension_strategy)
def test_marte::nfps::dimension_baseExponent_type(instance):
    assert isinstance(instance.baseExponent, int)


@given(instance=MARTE::NFPs::Dimension_strategy)
def test_marte::nfps::dimension_baseExponent_setter(instance):
    original = instance.baseExponent
    instance.baseExponent = original
    assert instance.baseExponent == original

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=MARTE::NFPs::NfpType_strategy)
@settings(max_examples=50)
def test_marte::nfps::nfptype_instantiation(instance):
    assert isinstance(instance, MARTE::NFPs::NfpType)

@given(instance=CoreElements::Mode_strategy)
@settings(max_examples=50)
def test_coreelements::mode_instantiation(instance):
    assert isinstance(instance, CoreElements::Mode)

@given(instance=NFPs::MARTE::Constraint_strategy)
@settings(max_examples=50)
def test_nfps::marte::constraint_instantiation(instance):
    assert isinstance(instance, NFPs::MARTE::Constraint)

@given(instance=MARTE::NFPs::NfpConstraint_strategy)
@settings(max_examples=50)
def test_marte::nfps::nfpconstraint_instantiation(instance):
    assert isinstance(instance, MARTE::NFPs::NfpConstraint)

@given(instance=MARTE::NFPs::NfpConstraint_strategy)
def test_marte::nfps::nfpconstraint_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::NFPs::NfpConstraint_strategy)
def test_marte::nfps::nfpconstraint_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=NFPs::MARTE::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_nfps::marte::enumerationliteral_instantiation(instance):
    assert isinstance(instance, NFPs::MARTE::EnumerationLiteral)

@given(instance=CoreElements::MARTE::Package_strategy)
@settings(max_examples=50)
def test_coreelements::marte::package_instantiation(instance):
    assert isinstance(instance, CoreElements::MARTE::Package)

@given(instance=CoreElements::MARTE::StructuredClassifier_strategy)
@settings(max_examples=50)
def test_coreelements::marte::structuredclassifier_instantiation(instance):
    assert isinstance(instance, CoreElements::MARTE::StructuredClassifier)

@given(instance=MARTE::CoreElements::Configuration_strategy)
@settings(max_examples=50)
def test_marte::coreelements::configuration_instantiation(instance):
    assert isinstance(instance, MARTE::CoreElements::Configuration)

@given(instance=CoreElements::MARTE::StateMachine_strategy)
@settings(max_examples=50)
def test_coreelements::marte::statemachine_instantiation(instance):
    assert isinstance(instance, CoreElements::MARTE::StateMachine)

@given(instance=MARTE::CoreElements::ModeBehavior_strategy)
@settings(max_examples=50)
def test_marte::coreelements::modebehavior_instantiation(instance):
    assert isinstance(instance, MARTE::CoreElements::ModeBehavior)

@given(instance=MARTE::NFPs::Nfp_strategy)
@settings(max_examples=50)
def test_marte::nfps::nfp_instantiation(instance):
    assert isinstance(instance, MARTE::NFPs::Nfp)

@given(instance=NFPs::Unit_strategy)
@settings(max_examples=50)
def test_nfps::unit_instantiation(instance):
    assert isinstance(instance, NFPs::Unit)

@given(instance=MARTE::NFPs::Unit_strategy)
@settings(max_examples=50)
def test_marte::nfps::unit_instantiation(instance):
    assert isinstance(instance, MARTE::NFPs::Unit)

@given(instance=MARTE::NFPs::Unit_strategy)
def test_marte::nfps::unit_convFactor_type(instance):
    assert isinstance(instance.convFactor, str)


@given(instance=MARTE::NFPs::Unit_strategy)
def test_marte::nfps::unit_convFactor_setter(instance):
    original = instance.convFactor
    instance.convFactor = original
    assert instance.convFactor == original

@given(instance=MARTE::NFPs::Unit_strategy)
def test_marte::nfps::unit_offsetFactor_type(instance):
    assert isinstance(instance.offsetFactor, str)


@given(instance=MARTE::NFPs::Unit_strategy)
def test_marte::nfps::unit_offsetFactor_setter(instance):
    original = instance.offsetFactor
    instance.offsetFactor = original
    assert instance.offsetFactor == original

@given(instance=NFPs::MARTE::Property_strategy)
@settings(max_examples=50)
def test_nfps::marte::property_instantiation(instance):
    assert isinstance(instance, NFPs::MARTE::Property)

@given(instance=MARTE::RSM::Distribute_strategy)
@settings(max_examples=50)
def test_marte::rsm::distribute_instantiation(instance):
    assert isinstance(instance, MARTE::RSM::Distribute)

@given(instance=IntegerVector_strategy)
@settings(max_examples=50)
def test_integervector_instantiation(instance):
    assert isinstance(instance, IntegerVector)

@given(instance=LinkTopology_strategy)
@settings(max_examples=50)
def test_linktopology_instantiation(instance):
    assert isinstance(instance, LinkTopology)

@given(instance=MARTE::RSM::Reshape_strategy)
@settings(max_examples=50)
def test_marte::rsm::reshape_instantiation(instance):
    assert isinstance(instance, MARTE::RSM::Reshape)

@given(instance=MARTE::RSM::InterRepetition_strategy)
@settings(max_examples=50)
def test_marte::rsm::interrepetition_instantiation(instance):
    assert isinstance(instance, MARTE::RSM::InterRepetition)

@given(instance=MARTE::RSM::InterRepetition_strategy)
def test_marte::rsm::interrepetition_isModulo_type(instance):
    assert isinstance(instance.isModulo, str)


@given(instance=MARTE::RSM::InterRepetition_strategy)
def test_marte::rsm::interrepetition_isModulo_setter(instance):
    original = instance.isModulo
    instance.isModulo = original
    assert instance.isModulo == original

@given(instance=MARTE::RSM::DefaultLink_strategy)
@settings(max_examples=50)
def test_marte::rsm::defaultlink_instantiation(instance):
    assert isinstance(instance, MARTE::RSM::DefaultLink)

@given(instance=RSM::MARTE::Connector_strategy)
@settings(max_examples=50)
def test_rsm::marte::connector_instantiation(instance):
    assert isinstance(instance, RSM::MARTE::Connector)

@given(instance=MARTE::RSM::LinkTopology_strategy)
@settings(max_examples=50)
def test_marte::rsm::linktopology_instantiation(instance):
    assert isinstance(instance, MARTE::RSM::LinkTopology)

@given(instance=IntegerMatrix_strategy)
@settings(max_examples=50)
def test_integermatrix_instantiation(instance):
    assert isinstance(instance, IntegerMatrix)

@given(instance=MARTE::RSM::Tiler_strategy)
@settings(max_examples=50)
def test_marte::rsm::tiler_instantiation(instance):
    assert isinstance(instance, MARTE::RSM::Tiler)

@given(instance=NFP::Energy_strategy)
@settings(max_examples=50)
def test_nfp::energy_instantiation(instance):
    assert isinstance(instance, NFP::Energy)

@given(instance=NFP::Power_strategy)
@settings(max_examples=50)
def test_nfp::power_instantiation(instance):
    assert isinstance(instance, NFP::Power)

@given(instance=NFP::DataSize_strategy)
@settings(max_examples=50)
def test_nfp::datasize_instantiation(instance):
    assert isinstance(instance, NFP::DataSize)

@given(instance=MARTE::GRM::ResourceUsage_strategy)
@settings(max_examples=50)
def test_marte::grm::resourceusage_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::ResourceUsage)

@given(instance=GrService_strategy)
@settings(max_examples=50)
def test_grservice_instantiation(instance):
    assert isinstance(instance, GrService)

@given(instance=MARTE::HwGeneral::HwResourceService_strategy)
@settings(max_examples=50)
def test_marte::hwgeneral::hwresourceservice_instantiation(instance):
    assert isinstance(instance, MARTE::HwGeneral::HwResourceService)

@given(instance=MARTE::SW::ResourceCore::SwAccessService_strategy)
@settings(max_examples=50)
def test_marte::sw::resourcecore::swaccessservice_instantiation(instance):
    assert isinstance(instance, MARTE::SW::ResourceCore::SwAccessService)

@given(instance=MARTE::SW::ResourceCore::SwAccessService_strategy)
def test_marte::sw::resourcecore::swaccessservice_isModifier_type(instance):
    assert isinstance(instance.isModifier, str)


@given(instance=MARTE::SW::ResourceCore::SwAccessService_strategy)
def test_marte::sw::resourcecore::swaccessservice_isModifier_setter(instance):
    original = instance.isModifier
    instance.isModifier = original
    assert instance.isModifier == original

@given(instance=MARTE::GRM::Acquire_strategy)
@settings(max_examples=50)
def test_marte::grm::acquire_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::Acquire)

@given(instance=MARTE::GRM::Acquire_strategy)
def test_marte::grm::acquire_isBlocking_type(instance):
    assert isinstance(instance.isBlocking, str)


@given(instance=MARTE::GRM::Acquire_strategy)
def test_marte::grm::acquire_isBlocking_setter(instance):
    original = instance.isBlocking
    instance.isBlocking = original
    assert instance.isBlocking == original

@given(instance=MARTE::GRM::Release_strategy)
@settings(max_examples=50)
def test_marte::grm::release_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::Release)

@given(instance=GRM::MARTE::CollaborationUse_strategy)
@settings(max_examples=50)
def test_grm::marte::collaborationuse_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::CollaborationUse)

@given(instance=GRM::MARTE::Collaboration_strategy)
@settings(max_examples=50)
def test_grm::marte::collaboration_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::Collaboration)

@given(instance=GRM::MARTE::Behavior_strategy)
@settings(max_examples=50)
def test_grm::marte::behavior_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::Behavior)

@given(instance=GRM::MARTE::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_grm::marte::behavioralfeature_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::BehavioralFeature)

@given(instance=GRM::MARTE::ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_grm::marte::executionspecification_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::ExecutionSpecification)

@given(instance=GRM::Resource_strategy)
@settings(max_examples=50)
def test_grm::resource_instantiation(instance):
    assert isinstance(instance, GRM::Resource)

@given(instance=MARTE::GRM::GrService_strategy)
@settings(max_examples=50)
def test_marte::grm::grservice_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::GrService)

@given(instance=GRM::ResourceUsage_strategy)
@settings(max_examples=50)
def test_grm::resourceusage_instantiation(instance):
    assert isinstance(instance, GRM::ResourceUsage)

@given(instance=MARTE::GQAM::GaScenario_strategy)
@settings(max_examples=50)
def test_marte::gqam::gascenario_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaScenario)

@given(instance=GRM::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_grm::marte::namedelement_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::NamedElement)

@given(instance=NFP::DataTxRate_strategy)
@settings(max_examples=50)
def test_nfp::datatxrate_instantiation(instance):
    assert isinstance(instance, NFP::DataTxRate)

@given(instance=NFP::Duration_strategy)
@settings(max_examples=50)
def test_nfp::duration_instantiation(instance):
    assert isinstance(instance, NFP::Duration)

@given(instance=GRM::MARTE::Connector_strategy)
@settings(max_examples=50)
def test_grm::marte::connector_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::Connector)

@given(instance=Scheduler_strategy)
@settings(max_examples=50)
def test_scheduler_instantiation(instance):
    assert isinstance(instance, Scheduler)

@given(instance=MARTE::GRM::SecondaryScheduler_strategy)
@settings(max_examples=50)
def test_marte::grm::secondaryscheduler_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::SecondaryScheduler)

@given(instance=GRM::SecondaryScheduler_strategy)
@settings(max_examples=50)
def test_grm::secondaryscheduler_instantiation(instance):
    assert isinstance(instance, GRM::SecondaryScheduler)

@given(instance=SchedParameters_strategy)
@settings(max_examples=50)
def test_schedparameters_instantiation(instance):
    assert isinstance(instance, SchedParameters)

@given(instance=TimingResource_strategy)
@settings(max_examples=50)
def test_timingresource_instantiation(instance):
    assert isinstance(instance, TimingResource)

@given(instance=MARTE::GRM::TimerResource_strategy)
@settings(max_examples=50)
def test_marte::grm::timerresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::TimerResource)

@given(instance=MARTE::GRM::TimerResource_strategy)
def test_marte::grm::timerresource_isPeriodic_type(instance):
    assert isinstance(instance.isPeriodic, str)


@given(instance=MARTE::GRM::TimerResource_strategy)
def test_marte::grm::timerresource_isPeriodic_setter(instance):
    original = instance.isPeriodic
    instance.isPeriodic = original
    assert instance.isPeriodic == original

@given(instance=MARTE::GRM::ClockResource_strategy)
@settings(max_examples=50)
def test_marte::grm::clockresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::ClockResource)

@given(instance=GRM::Scheduler_strategy)
@settings(max_examples=50)
def test_grm::scheduler_instantiation(instance):
    assert isinstance(instance, GRM::Scheduler)

@given(instance=MARTE::GQAM::GaCommHost_strategy)
@settings(max_examples=50)
def test_marte::gqam::gacommhost_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaCommHost)

@given(instance=NFP::Real_strategy)
@settings(max_examples=50)
def test_nfp::real_instantiation(instance):
    assert isinstance(instance, NFP::Real)

@given(instance=GRM::SchedulableResource_strategy)
@settings(max_examples=50)
def test_grm::schedulableresource_instantiation(instance):
    assert isinstance(instance, GRM::SchedulableResource)

@given(instance=MARTE::SW::Concurrency::SwSchedulableResource_strategy)
@settings(max_examples=50)
def test_marte::sw::concurrency::swschedulableresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Concurrency::SwSchedulableResource)

@given(instance=MARTE::SW::Concurrency::SwSchedulableResource_strategy)
def test_marte::sw::concurrency::swschedulableresource_isPreemptable_type(instance):
    assert isinstance(instance.isPreemptable, str)


@given(instance=MARTE::SW::Concurrency::SwSchedulableResource_strategy)
def test_marte::sw::concurrency::swschedulableresource_isPreemptable_setter(instance):
    original = instance.isPreemptable
    instance.isPreemptable = original
    assert instance.isPreemptable == original

@given(instance=MARTE::SW::Concurrency::SwSchedulableResource_strategy)
def test_marte::sw::concurrency::swschedulableresource_isStaticSchedulingFeature_type(instance):
    assert isinstance(instance.isStaticSchedulingFeature, str)


@given(instance=MARTE::SW::Concurrency::SwSchedulableResource_strategy)
def test_marte::sw::concurrency::swschedulableresource_isStaticSchedulingFeature_setter(instance):
    original = instance.isStaticSchedulingFeature
    instance.isStaticSchedulingFeature = original
    assert instance.isStaticSchedulingFeature == original

@given(instance=GRM::MutualExclusionResource_strategy)
@settings(max_examples=50)
def test_grm::mutualexclusionresource_instantiation(instance):
    assert isinstance(instance, GRM::MutualExclusionResource)

@given(instance=MARTE::SW::Interaction::SwMutualExclusionResource_strategy)
@settings(max_examples=50)
def test_marte::sw::interaction::swmutualexclusionresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Interaction::SwMutualExclusionResource)

@given(instance=MARTE::SW::Interaction::SwMutualExclusionResource_strategy)
def test_marte::sw::interaction::swmutualexclusionresource_concurrentAccessProtocol_type(instance):
    assert isinstance(instance.concurrentAccessProtocol, str)


@given(instance=MARTE::SW::Interaction::SwMutualExclusionResource_strategy)
def test_marte::sw::interaction::swmutualexclusionresource_concurrentAccessProtocol_setter(instance):
    original = instance.concurrentAccessProtocol
    instance.concurrentAccessProtocol = original
    assert instance.concurrentAccessProtocol == original

@given(instance=MARTE::SW::Interaction::SwMutualExclusionResource_strategy)
def test_marte::sw::interaction::swmutualexclusionresource_mechanism_type(instance):
    assert isinstance(instance.mechanism, str)


@given(instance=MARTE::SW::Interaction::SwMutualExclusionResource_strategy)
def test_marte::sw::interaction::swmutualexclusionresource_mechanism_setter(instance):
    original = instance.mechanism
    instance.mechanism = original
    assert instance.mechanism == original

@given(instance=GRM::ComputingResource_strategy)
@settings(max_examples=50)
def test_grm::computingresource_instantiation(instance):
    assert isinstance(instance, GRM::ComputingResource)

@given(instance=MARTE::GQAM::GaExecHost_strategy)
@settings(max_examples=50)
def test_marte::gqam::gaexechost_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaExecHost)

@given(instance=MARTE::HwComputing::HwComputingResource_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwcomputingresource_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwComputingResource)

@given(instance=GRM::ProcessingResource_strategy)
@settings(max_examples=50)
def test_grm::processingresource_instantiation(instance):
    assert isinstance(instance, GRM::ProcessingResource)

@given(instance=GRM::MARTE::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_grm::marte::opaqueexpression_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::OpaqueExpression)

@given(instance=ProcessingResource_strategy)
@settings(max_examples=50)
def test_processingresource_instantiation(instance):
    assert isinstance(instance, ProcessingResource)

@given(instance=MARTE::GRM::CommunicationMedia_strategy)
@settings(max_examples=50)
def test_marte::grm::communicationmedia_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::CommunicationMedia)

@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_transmMode_type(instance):
    assert isinstance(instance.transmMode, str)


@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_transmMode_setter(instance):
    original = instance.transmMode
    instance.transmMode = original
    assert instance.transmMode == original

@given(instance=MARTE::GRM::DeviceResource_strategy)
@settings(max_examples=50)
def test_marte::grm::deviceresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::DeviceResource)

@given(instance=MARTE::GRM::ComputingResource_strategy)
@settings(max_examples=50)
def test_marte::grm::computingresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::ComputingResource)

@given(instance=GRM::MARTE::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_grm::marte::instancespecification_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::InstanceSpecification)

@given(instance=GRM::MARTE::Property_strategy)
@settings(max_examples=50)
def test_grm::marte::property_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::Property)

@given(instance=NFP::Integer_strategy)
@settings(max_examples=50)
def test_nfp::integer_instantiation(instance):
    assert isinstance(instance, NFP::Integer)

@given(instance=MARTE::GRM::Resource_strategy)
@settings(max_examples=50)
def test_marte::grm::resource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::Resource)

@given(instance=MARTE::GRM::Resource_strategy)
def test_marte::grm::resource_isProtected_type(instance):
    assert isinstance(instance.isProtected, str)


@given(instance=MARTE::GRM::Resource_strategy)
def test_marte::grm::resource_isProtected_setter(instance):
    original = instance.isProtected
    instance.isProtected = original
    assert instance.isProtected == original

@given(instance=Time::MARTE::Event_strategy)
@settings(max_examples=50)
def test_time::marte::event_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Event)

@given(instance=Time::MARTE::Message_strategy)
@settings(max_examples=50)
def test_time::marte::message_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Message)

@given(instance=Time::MARTE::Behavior_strategy)
@settings(max_examples=50)
def test_time::marte::behavior_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Behavior)

@given(instance=Time::MARTE::Action_strategy)
@settings(max_examples=50)
def test_time::marte::action_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Action)

@given(instance=Time::MARTE::TimeEvent_strategy)
@settings(max_examples=50)
def test_time::marte::timeevent_instantiation(instance):
    assert isinstance(instance, Time::MARTE::TimeEvent)

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=MARTE::GRM::Scheduler_strategy)
@settings(max_examples=50)
def test_marte::grm::scheduler_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::Scheduler)

@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_isPreemptible_type(instance):
    assert isinstance(instance.isPreemptible, str)


@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_isPreemptible_setter(instance):
    original = instance.isPreemptible
    instance.isPreemptible = original
    assert instance.isPreemptible == original

@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_schedPolicy_type(instance):
    assert isinstance(instance.schedPolicy, str)


@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_schedPolicy_setter(instance):
    original = instance.schedPolicy
    instance.schedPolicy = original
    assert instance.schedPolicy == original

@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_otherSchedPolicy_type(instance):
    assert isinstance(instance.otherSchedPolicy, str)


@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_otherSchedPolicy_setter(instance):
    original = instance.otherSchedPolicy
    instance.otherSchedPolicy = original
    assert instance.otherSchedPolicy == original

@given(instance=MARTE::PAM::PaLogicalResource_strategy)
@settings(max_examples=50)
def test_marte::pam::palogicalresource_instantiation(instance):
    assert isinstance(instance, MARTE::PAM::PaLogicalResource)

@given(instance=MARTE::GRM::SynchronizationResource_strategy)
@settings(max_examples=50)
def test_marte::grm::synchronizationresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::SynchronizationResource)

@given(instance=MARTE::GRM::MutualExclusionResource_strategy)
@settings(max_examples=50)
def test_marte::grm::mutualexclusionresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::MutualExclusionResource)

@given(instance=MARTE::GRM::MutualExclusionResource_strategy)
def test_marte::grm::mutualexclusionresource_protectKind_type(instance):
    assert isinstance(instance.protectKind, str)


@given(instance=MARTE::GRM::MutualExclusionResource_strategy)
def test_marte::grm::mutualexclusionresource_protectKind_setter(instance):
    original = instance.protectKind
    instance.protectKind = original
    assert instance.protectKind == original

@given(instance=MARTE::GRM::MutualExclusionResource_strategy)
def test_marte::grm::mutualexclusionresource_otherProtectProtocol_type(instance):
    assert isinstance(instance.otherProtectProtocol, str)


@given(instance=MARTE::GRM::MutualExclusionResource_strategy)
def test_marte::grm::mutualexclusionresource_otherProtectProtocol_setter(instance):
    original = instance.otherProtectProtocol
    instance.otherProtectProtocol = original
    assert instance.otherProtectProtocol == original

@given(instance=MARTE::GRM::CommunicationEndPoint_strategy)
@settings(max_examples=50)
def test_marte::grm::communicationendpoint_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::CommunicationEndPoint)

@given(instance=MARTE::HwGeneral::HwResource_strategy)
@settings(max_examples=50)
def test_marte::hwgeneral::hwresource_instantiation(instance):
    assert isinstance(instance, MARTE::HwGeneral::HwResource)

@given(instance=MARTE::HwGeneral::HwResource_strategy)
def test_marte::hwgeneral::hwresource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MARTE::HwGeneral::HwResource_strategy)
def test_marte::hwgeneral::hwresource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MARTE::GRM::SchedulableResource_strategy)
@settings(max_examples=50)
def test_marte::grm::schedulableresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::SchedulableResource)

@given(instance=MARTE::GRM::ConcurrencyResource_strategy)
@settings(max_examples=50)
def test_marte::grm::concurrencyresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::ConcurrencyResource)

@given(instance=MARTE::SW::ResourceCore::SwResource_strategy)
@settings(max_examples=50)
def test_marte::sw::resourcecore::swresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::ResourceCore::SwResource)

@given(instance=MARTE::GRM::TimingResource_strategy)
@settings(max_examples=50)
def test_marte::grm::timingresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::TimingResource)

@given(instance=MARTE::GRM::ProcessingResource_strategy)
@settings(max_examples=50)
def test_marte::grm::processingresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::ProcessingResource)

@given(instance=MARTE::GRM::StorageResource_strategy)
@settings(max_examples=50)
def test_marte::grm::storageresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::StorageResource)

@given(instance=GRM::MARTE::ConnectableElement_strategy)
@settings(max_examples=50)
def test_grm::marte::connectableelement_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::ConnectableElement)

@given(instance=GRM::MARTE::Lifeline_strategy)
@settings(max_examples=50)
def test_grm::marte::lifeline_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::Lifeline)

@given(instance=GRM::MARTE::Classifier_strategy)
@settings(max_examples=50)
def test_grm::marte::classifier_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::Classifier)

@given(instance=TimedObservation_strategy)
@settings(max_examples=50)
def test_timedobservation_instantiation(instance):
    assert isinstance(instance, TimedObservation)

@given(instance=MARTE::Time::TimedInstantObservation_strategy)
@settings(max_examples=50)
def test_marte::time::timedinstantobservation_instantiation(instance):
    assert isinstance(instance, MARTE::Time::TimedInstantObservation)

@given(instance=MARTE::Time::TimedInstantObservation_strategy)
def test_marte::time::timedinstantobservation_obsKind_type(instance):
    assert isinstance(instance.obsKind, str)


@given(instance=MARTE::Time::TimedInstantObservation_strategy)
def test_marte::time::timedinstantobservation_obsKind_setter(instance):
    original = instance.obsKind
    instance.obsKind = original
    assert instance.obsKind == original

@given(instance=Time::TimedElement_strategy)
@settings(max_examples=50)
def test_time::timedelement_instantiation(instance):
    assert isinstance(instance, Time::TimedElement)

@given(instance=Time::MARTE::ValueSpecification_strategy)
@settings(max_examples=50)
def test_time::marte::valuespecification_instantiation(instance):
    assert isinstance(instance, Time::MARTE::ValueSpecification)

@given(instance=TimedElement_strategy)
@settings(max_examples=50)
def test_timedelement_instantiation(instance):
    assert isinstance(instance, TimedElement)

@given(instance=MARTE::Time::TimedObservation_strategy)
@settings(max_examples=50)
def test_marte::time::timedobservation_instantiation(instance):
    assert isinstance(instance, MARTE::Time::TimedObservation)

@given(instance=MARTE::Time::TimedProcessing_strategy)
@settings(max_examples=50)
def test_marte::time::timedprocessing_instantiation(instance):
    assert isinstance(instance, MARTE::Time::TimedProcessing)

@given(instance=MARTE::Time::TimedValueSpecification_strategy)
@settings(max_examples=50)
def test_marte::time::timedvaluespecification_instantiation(instance):
    assert isinstance(instance, MARTE::Time::TimedValueSpecification)

@given(instance=MARTE::Time::TimedValueSpecification_strategy)
def test_marte::time::timedvaluespecification_interpretation_type(instance):
    assert isinstance(instance.interpretation, str)


@given(instance=MARTE::Time::TimedValueSpecification_strategy)
def test_marte::time::timedvaluespecification_interpretation_setter(instance):
    original = instance.interpretation
    instance.interpretation = original
    assert instance.interpretation == original

@given(instance=Time::Clock_strategy)
@settings(max_examples=50)
def test_time::clock_instantiation(instance):
    assert isinstance(instance, Time::Clock)

@given(instance=MARTE::Time::TimedElement_strategy)
@settings(max_examples=50)
def test_marte::time::timedelement_instantiation(instance):
    assert isinstance(instance, MARTE::Time::TimedElement)

@given(instance=Time::MARTE::Class_strategy)
@settings(max_examples=50)
def test_time::marte::class_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Class)

@given(instance=MARTE::Time::TimedEvent_strategy)
@settings(max_examples=50)
def test_marte::time::timedevent_instantiation(instance):
    assert isinstance(instance, MARTE::Time::TimedEvent)

@given(instance=MARTE::Time::TimedEvent_strategy)
def test_marte::time::timedevent_repetition_type(instance):
    assert isinstance(instance.repetition, str)


@given(instance=MARTE::Time::TimedEvent_strategy)
def test_marte::time::timedevent_repetition_setter(instance):
    original = instance.repetition
    instance.repetition = original
    assert instance.repetition == original

@given(instance=Time::MARTE::DurationObservation_strategy)
@settings(max_examples=50)
def test_time::marte::durationobservation_instantiation(instance):
    assert isinstance(instance, Time::MARTE::DurationObservation)

@given(instance=MARTE::Time::TimedDurationObservation_strategy)
@settings(max_examples=50)
def test_marte::time::timeddurationobservation_instantiation(instance):
    assert isinstance(instance, MARTE::Time::TimedDurationObservation)

@given(instance=MARTE::Time::TimedDurationObservation_strategy)
def test_marte::time::timeddurationobservation_obsKind_type(instance):
    assert isinstance(instance.obsKind, str)


@given(instance=MARTE::Time::TimedDurationObservation_strategy)
def test_marte::time::timeddurationobservation_obsKind_setter(instance):
    original = instance.obsKind
    instance.obsKind = original
    assert instance.obsKind == original

@given(instance=Time::MARTE::TimeObservation_strategy)
@settings(max_examples=50)
def test_time::marte::timeobservation_instantiation(instance):
    assert isinstance(instance, Time::MARTE::TimeObservation)

@given(instance=Time::MARTE::Enumeration_strategy)
@settings(max_examples=50)
def test_time::marte::enumeration_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Enumeration)

@given(instance=MARTE::Time::ClockType_strategy)
@settings(max_examples=50)
def test_marte::time::clocktype_instantiation(instance):
    assert isinstance(instance, MARTE::Time::ClockType)

@given(instance=MARTE::Time::ClockType_strategy)
def test_marte::time::clocktype_isLogical_type(instance):
    assert isinstance(instance.isLogical, str)


@given(instance=MARTE::Time::ClockType_strategy)
def test_marte::time::clocktype_isLogical_setter(instance):
    original = instance.isLogical
    instance.isLogical = original
    assert instance.isLogical == original

@given(instance=MARTE::Time::ClockType_strategy)
def test_marte::time::clocktype_nature_type(instance):
    assert isinstance(instance.nature, str)


@given(instance=MARTE::Time::ClockType_strategy)
def test_marte::time::clocktype_nature_setter(instance):
    original = instance.nature
    instance.nature = original
    assert instance.nature == original

@given(instance=Time::MARTE::Property_strategy)
@settings(max_examples=50)
def test_time::marte::property_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Property)

@given(instance=Time::ClockType_strategy)
@settings(max_examples=50)
def test_time::clocktype_instantiation(instance):
    assert isinstance(instance, Time::ClockType)

@given(instance=Time::MARTE::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_time::marte::instancespecification_instantiation(instance):
    assert isinstance(instance, Time::MARTE::InstanceSpecification)

@given(instance=MARTE::Time::Clock_strategy)
@settings(max_examples=50)
def test_marte::time::clock_instantiation(instance):
    assert isinstance(instance, MARTE::Time::Clock)

@given(instance=MARTE::Time::Clock_strategy)
def test_marte::time::clock_standard_type(instance):
    assert isinstance(instance.standard, str)


@given(instance=MARTE::Time::Clock_strategy)
def test_marte::time::clock_standard_setter(instance):
    original = instance.standard
    instance.standard = original
    assert instance.standard == original

@given(instance=Time::MARTE::Namespace_strategy)
@settings(max_examples=50)
def test_time::marte::namespace_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Namespace)

@given(instance=MARTE::Time::TimedDomain_strategy)
@settings(max_examples=50)
def test_marte::time::timeddomain_instantiation(instance):
    assert isinstance(instance, MARTE::Time::TimedDomain)

@given(instance=Alloc::MARTE::Abstraction_strategy)
@settings(max_examples=50)
def test_alloc::marte::abstraction_instantiation(instance):
    assert isinstance(instance, Alloc::MARTE::Abstraction)

@given(instance=MARTE::Alloc::Allocate_strategy)
@settings(max_examples=50)
def test_marte::alloc::allocate_instantiation(instance):
    assert isinstance(instance, MARTE::Alloc::Allocate)

@given(instance=MARTE::Alloc::Allocate_strategy)
def test_marte::alloc::allocate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::Alloc::Allocate_strategy)
def test_marte::alloc::allocate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MARTE::Alloc::Allocate_strategy)
def test_marte::alloc::allocate_nature_type(instance):
    assert isinstance(instance.nature, str)


@given(instance=MARTE::Alloc::Allocate_strategy)
def test_marte::alloc::allocate_nature_setter(instance):
    original = instance.nature
    instance.nature = original
    assert instance.nature == original

@given(instance=Time::MARTE::Operation_strategy)
@settings(max_examples=50)
def test_time::marte::operation_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Operation)

@given(instance=MARTE::Alloc::Assign_strategy)
@settings(max_examples=50)
def test_marte::alloc::assign_instantiation(instance):
    assert isinstance(instance, MARTE::Alloc::Assign)

@given(instance=NFPs::NfpConstraint_strategy)
@settings(max_examples=50)
def test_nfps::nfpconstraint_instantiation(instance):
    assert isinstance(instance, NFPs::NfpConstraint)

@given(instance=MARTE::Time::ClockConstraint_strategy)
@settings(max_examples=50)
def test_marte::time::clockconstraint_instantiation(instance):
    assert isinstance(instance, MARTE::Time::ClockConstraint)

@given(instance=MARTE::Time::ClockConstraint_strategy)
def test_marte::time::clockconstraint_isChronometricBased_type(instance):
    assert isinstance(instance.isChronometricBased, str)


@given(instance=MARTE::Time::ClockConstraint_strategy)
def test_marte::time::clockconstraint_isChronometricBased_setter(instance):
    original = instance.isChronometricBased
    instance.isChronometricBased = original
    assert instance.isChronometricBased == original

@given(instance=MARTE::Time::ClockConstraint_strategy)
def test_marte::time::clockconstraint_isCoincidenceBased_type(instance):
    assert isinstance(instance.isCoincidenceBased, str)


@given(instance=MARTE::Time::ClockConstraint_strategy)
def test_marte::time::clockconstraint_isCoincidenceBased_setter(instance):
    original = instance.isCoincidenceBased
    instance.isCoincidenceBased = original
    assert instance.isCoincidenceBased == original

@given(instance=MARTE::Time::ClockConstraint_strategy)
def test_marte::time::clockconstraint_isPrecedenceBased_type(instance):
    assert isinstance(instance.isPrecedenceBased, bool)


@given(instance=MARTE::Time::ClockConstraint_strategy)
def test_marte::time::clockconstraint_isPrecedenceBased_setter(instance):
    original = instance.isPrecedenceBased
    instance.isPrecedenceBased = original
    assert instance.isPrecedenceBased == original

@given(instance=MARTE::Time::TimedConstraint_strategy)
@settings(max_examples=50)
def test_marte::time::timedconstraint_instantiation(instance):
    assert isinstance(instance, MARTE::Time::TimedConstraint)

@given(instance=MARTE::Time::TimedConstraint_strategy)
def test_marte::time::timedconstraint_interpretation_type(instance):
    assert isinstance(instance.interpretation, str)


@given(instance=MARTE::Time::TimedConstraint_strategy)
def test_marte::time::timedconstraint_interpretation_setter(instance):
    original = instance.interpretation
    instance.interpretation = original
    assert instance.interpretation == original

@given(instance=Alloc::MARTE::Dependency_strategy)
@settings(max_examples=50)
def test_alloc::marte::dependency_instantiation(instance):
    assert isinstance(instance, Alloc::MARTE::Dependency)

@given(instance=MARTE::Alloc::NfpRefine_strategy)
@settings(max_examples=50)
def test_marte::alloc::nfprefine_instantiation(instance):
    assert isinstance(instance, MARTE::Alloc::NfpRefine)

@given(instance=Alloc::MARTE::ActivityPartition_strategy)
@settings(max_examples=50)
def test_alloc::marte::activitypartition_instantiation(instance):
    assert isinstance(instance, Alloc::MARTE::ActivityPartition)

@given(instance=MARTE::Alloc::AllocateActivityGroup_strategy)
@settings(max_examples=50)
def test_marte::alloc::allocateactivitygroup_instantiation(instance):
    assert isinstance(instance, MARTE::Alloc::AllocateActivityGroup)

@given(instance=Alloc::Allocated_strategy)
@settings(max_examples=50)
def test_alloc::allocated_instantiation(instance):
    assert isinstance(instance, Alloc::Allocated)

@given(instance=Alloc::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_alloc::marte::namedelement_instantiation(instance):
    assert isinstance(instance, Alloc::MARTE::NamedElement)

@given(instance=MARTE::Alloc::Allocated_strategy)
@settings(max_examples=50)
def test_marte::alloc::allocated_instantiation(instance):
    assert isinstance(instance, MARTE::Alloc::Allocated)

@given(instance=CoreElements::MARTE::State_strategy)
@settings(max_examples=50)
def test_coreelements::marte::state_instantiation(instance):
    assert isinstance(instance, CoreElements::MARTE::State)

@given(instance=MARTE::CoreElements::Mode_strategy)
@settings(max_examples=50)
def test_marte::coreelements::mode_instantiation(instance):
    assert isinstance(instance, MARTE::CoreElements::Mode)

@given(instance=Alloc::MARTE::Comment_strategy)
@settings(max_examples=50)
def test_alloc::marte::comment_instantiation(instance):
    assert isinstance(instance, Alloc::MARTE::Comment)

@given(instance=Alloc::MARTE::Element_strategy)
@settings(max_examples=50)
def test_alloc::marte::element_instantiation(instance):
    assert isinstance(instance, Alloc::MARTE::Element)

@given(instance=CoreElements::MARTE::Transition_strategy)
@settings(max_examples=50)
def test_coreelements::marte::transition_instantiation(instance):
    assert isinstance(instance, CoreElements::MARTE::Transition)
