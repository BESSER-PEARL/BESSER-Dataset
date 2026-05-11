import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    GQAM::MARTE::Behavior,
    GCM::MARTE::BehavioralFeature,
    MARTE::GCM::ClientServerFeature,
    MARTE::GCM::FlowSpecification,
    MARTE::GCM::ClientServerSpecification,
    GCM::ClientServerSpecification,
    GQAM::GaCommStep,
    PAM::PaStep,
    MARTE::PAM::PaCommStep,
    PAM::MARTE::NamedElement,
    MARTE::PAM::PaRunTInstance,
    GaExecHost,
    MARTE::SAM::SaExecHost,
    GaCommHost,
    MARTE::SAM::SaCommHost,
    MutualExclusionResource,
    MARTE::SAM::SaSharedResource,
    SAM::SaSharedResource,
    SAM::MARTE::BehavioralFeature,
    MARTE::SAM::SaEndtoEndFlow,
    GaAnalysisContext,
    MARTE::SAM::SaAnalysisContext,
    GQAM::MARTE::Classifier,
    MARTE::GQAM::GaResourcesPlatform,
    GQAM::GaResourcesPlatform,
    GQAM::GaWorkloadBehavior,
    Variables::ExpressionContext,
    CoreElements::Configuration,
    MARTE::GQAM::GaAnalysisContext,
    GaCommStep,
    MARTE::SAM::SaCommStep,
    SAM::MARTE::NamedElement,
    MARTE::GQAM::GaWorkloadBehavior,
    SchedulableResource,
    MARTE::GQAM::GaCommChannel,
    GaTimedObs,
    MARTE::SAM::SaSchedObs,
    MARTE::GQAM::GaLatencyObs,
    GQAM::MARTE::TimeObservation,
    NfpConstraint,
    MARTE::GQAM::GaTimedObs,
    GQAM::MARTE::Operation,
    GaStep,
    MARTE::PAM::PaResPassStep,
    MARTE::GQAM::GaCommStep,
    MARTE::GQAM::GaRelStep,
    MARTE::SAM::SaStep,
    MARTE::GQAM::GaAcqStep,
    MARTE::PAM::PaStep,
    MARTE::GQAM::GaRequestedService,
    GQAM::GaExecHost,
    GaScenario,
    MARTE::GQAM::GaStep,
    GQAM::GaTimedObs,
    GQAM::GaRequestedService,
    MARTE::PAM::PaRequestedStep,
    GQAM::GaWorkloadEvent,
    Time::TimedProcessing,
    GQAM::MARTE::TimeEvent,
    GQAM::GaScenario,
    GQAM::GaEventTrace,
    GQAM::GaWorkloadGenerator,
    MARTE::GQAM::GaWorkloadEvent,
    GQAM::MARTE::NamedElement,
    GQAM::GaStep,
    MARTE::GQAM::GaWorkloadGenerator,
    MARTE::GCM::GCMInvocatingBehavior,
    GCM::MARTE::Behavior,
    MARTE::GCM::DataPool,
    GCM::MARTE::Classifier,
    GCM::MARTE::AnyReceiveEvent,
    MARTE::GCM::DataEvent,
    GCM::MARTE::InvocationAction,
    MARTE::GCM::GCMInvocationAction,
    GCM::MARTE::Feature,
    MARTE::GQAM::GaEventTrace,
    MARTE::NFPs::Nfp,
    GCM::MARTE::Interface,
    MARTE::GCM::ClientServerPort,
    GCM::MARTE::Port,
    MARTE::GCM::FlowPort,
    GCM::MARTE::Trigger,
    MARTE::GCM::GCMTrigger,
    MARTE::GCM::FlowProperty,
    SW::Interaction::SwSynchronizationResource,
    SwSynchronizationResource,
    MARTE::SW::Interaction::NotificationResource,
    GCM::MARTE::Property,
    SW::Interaction::MARTE::BehavioralFeature,
    SwCommunicationResource,
    MARTE::SW::Interaction::MessageComResource,
    MARTE::SW::Interaction::SharedDataComResource,
    GRM::SynchronizationResource,
    SW::Interaction::SwInteractionResource,
    MARTE::SW::Interaction::SwSynchronizationResource,
    SW::Interaction::MARTE::TypedElement,
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
    SW::Concurrency::MARTE::Element,
    SwResource,
    MARTE::SW::Interaction::SwInteractionResource,
    MARTE::SW::Brokering::MemoryBroker,
    MARTE::SW::Concurrency::MemoryPartition,
    MARTE::SW::Brokering::DeviceBroker,
    MARTE::SW::Concurrency::SwConcurrentResource,
    SW::Concurrency::MARTE::BehavioralFeature,
    SW::ResourceCore::MARTE::Property,
    SW::ResourceCore::MARTE::BehavioralFeature,
    SW::ResourceCore::MARTE::TypedElement,
    SW::Concurrency::MARTE::TypedElement,
    HwComponent,
    MARTE::HwPower::HwCoolingSupply,
    MARTE::HwPower::HwPowerSupply,
    HwLayout::HwComponent,
    HwCommunication::HwEndPoint,
    HwGeneral::HwResourceService,
    HwI::O,
    MARTE::HwDevice::HWSensor,
    MARTE::HwDevice::HWActuator,
    HwTiming::HwClock,
    HwTimingResource,
    MARTE::HwTiming::HwTimer,
    MARTE::HwTiming::HwClock,
    GRM::TimingResource,
    HwDevice,
    MARTE::HwDevice::HwSupport,
    MARTE::HwDevice::HwI::O,
    GRM::DeviceResource,
    HwMemory,
    MARTE::HwMemory::HwCache,
    MARTE::HwMemory::HwDrive,
    MARTE::HwMemory::HwROM,
    MARTE::HwMemory::HwRAM,
    HwComputing::HwProcessor,
    HwStorageManager::HwStorageManager,
    HwMemory::HwMemory,
    GRM::StorageResource,
    GRM::CommunicationEndPoint,
    HwMedia,
    MARTE::HwCommunication::HwBridge,
    MARTE::HwCommunication::HwBus,
    HwCommunication::HwArbiter,
    MARTE::HwStorageManager::HwDMA,
    HwCommunication::HwCommunicationResource,
    MARTE::HwCommunication::HwEndPoint,
    GRM::CommunicationMedia,
    MARTE::SW::Interaction::SwCommunicationResource,
    MARTE::HwCommunication::HwMedia,
    HwStorageManager,
    MARTE::HwStorageManager::HwMMU,
    HwComputing::HwComputingResource,
    HwMemory::HwRAM,
    HwResource,
    MARTE::HwCommunication::HwCommunicationResource,
    MARTE::HwLayout::HwComponent,
    MARTE::HwComputing::HwBranchPredictor,
    MARTE::HwComputing::HwISA,
    HwGeneral::HwResource,
    MARTE::HwStorageManager::HwStorageManager,
    MARTE::HwTiming::HwTimingResource,
    MARTE::HwDevice::HwDevice,
    MARTE::HwMemory::HwMemory,
    HwCommunication::HwMedia,
    HwCommunicationResource,
    MARTE::HwCommunication::HwArbiter,
    HwMemory::HwCache,
    HwComputing::HwBranchPredictor,
    HwComputing::HwISA,
    HwComputingResource,
    MARTE::HwComputing::HwPLD,
    MARTE::HwComputing::HwASIC,
    MARTE::HwComputing::HwProcessor,
    HwStorageManager::HwMMU,
    MARTE::HLAM::RtService,
    MARTE::HLAM::RtAction,
    HLAM::MARTE::Comment,
    Time::TimedInstantObservation,
    MARTE::HLAM::RtSpecification,
    HLAM::RtSpecification,
    HLAM::MARTE::InvocationAction,
    HLAM::MARTE::Port,
    HLAM::MARTE::Signal,
    HLAM::MARTE::Message,
    HLAM::MARTE::BehavioralFeature,
    MARTE::HLAM::RtFeature,
    MARTE::HLAM::PpUnit,
    HLAM::MARTE::Operation,
    HLAM::MARTE::Behavior,
    MARTE::HLAM::RtUnit,
    MARTE::DataTypes::TupleType,
    MARTE::DataTypes::ChoiceType,
    MARTE::DataTypes::CollectionType,
    HLAM::MARTE::BehavioredClassifier,
    MARTE::DataTypes::IntervalType,
    DataTypes::MARTE::DataType,
    MARTE::DataTypes::BoundedSubtype,
    Operators::MARTE::Behavior,
    MARTE::Operators::Operator,
    Variables::MARTE::NamedElement,
    MARTE::Variables::ExpressionContext,
    Variables::MARTE::Property,
    MARTE::Variables::Var,
    RSM::MARTE::MultiplicityElement,
    MARTE::RSM::Shaped,
    DataTypes::MARTE::Property,
    Allocate,
    MARTE::SW::Concurrency::EntryPoint,
    MARTE::RSM::Distribute,
    LinkTopology,
    MARTE::RSM::Reshape,
    MARTE::RSM::InterRepetition,
    MARTE::RSM::Tiler,
    MARTE::RSM::DefaultLink,
    RSM::MARTE::Connector,
    MARTE::RSM::LinkTopology,
    GRM::ResourceUsage,
    MARTE::GQAM::GaScenario,
    GRM::MARTE::NamedElement,
    RSM::MARTE::ConnectorEnd,
    GrService,
    MARTE::HwGeneral::HwResourceService,
    MARTE::GRM::Acquire,
    MARTE::SW::ResourceCore::SwAccessService,
    MARTE::GRM::Release,
    GRM::MARTE::CollaborationUse,
    GRM::MARTE::Collaboration,
    GRM::MARTE::Behavior,
    GRM::MARTE::BehavioralFeature,
    GRM::MARTE::ExecutionSpecification,
    GRM::Resource,
    MARTE::GRM::GrService,
    TimingResource,
    MARTE::GRM::TimerResource,
    MARTE::GRM::ClockResource,
    MARTE::GRM::ResourceUsage,
    GRM::MARTE::Connector,
    Scheduler,
    MARTE::GRM::SecondaryScheduler,
    GRM::SecondaryScheduler,
    ProcessingResource,
    MARTE::GRM::DeviceResource,
    MARTE::GRM::CommunicationMedia,
    MARTE::GRM::ComputingResource,
    GRM::Scheduler,
    MARTE::GQAM::GaCommHost,
    GRM::SchedulableResource,
    MARTE::SW::Concurrency::SwSchedulableResource,
    GRM::MutualExclusionResource,
    MARTE::SW::Interaction::SwMutualExclusionResource,
    GRM::ComputingResource,
    MARTE::GQAM::GaExecHost,
    MARTE::HwComputing::HwComputingResource,
    GRM::ProcessingResource,
    Resource,
    MARTE::SW::ResourceCore::SwResource,
    MARTE::GRM::ProcessingResource,
    MARTE::GRM::CommunicationEndPoint,
    MARTE::PAM::PaLogicalResource,
    MARTE::GRM::SchedulableResource,
    MARTE::GRM::MutualExclusionResource,
    MARTE::GRM::TimingResource,
    MARTE::GRM::ConcurrencyResource,
    MARTE::GRM::SynchronizationResource,
    MARTE::GRM::Scheduler,
    MARTE::HwGeneral::HwResource,
    MARTE::GRM::StorageResource,
    GRM::MARTE::Lifeline,
    GRM::MARTE::Classifier,
    GRM::MARTE::InstanceSpecification,
    GRM::MARTE::Property,
    MARTE::GRM::Resource,
    Time::MARTE::Message,
    Time::MARTE::Behavior,
    GRM::MARTE::ConnectableElement,
    Time::MARTE::Action,
    Time::MARTE::TimeEvent,
    Time::MARTE::DurationObservation,
    Time::MARTE::TimeObservation,
    Time::TimedElement,
    Time::MARTE::ValueSpecification,
    TimedElement,
    MARTE::Time::TimedDurationObservation,
    MARTE::Time::TimedEvent,
    MARTE::Time::TimedProcessing,
    MARTE::Time::TimedInstantObservation,
    MARTE::Time::TimedValueSpecification,
    Time::Clock,
    MARTE::Time::TimedElement,
    Time::MARTE::Class,
    Time::MARTE::Operation,
    MARTE::Time::ClockType,
    Time::MARTE::Event,
    Time::MARTE::Property,
    Time::ClockType,
    Time::MARTE::InstanceSpecification,
    MARTE::Time::Clock,
    Time::MARTE::Namespace,
    MARTE::Time::TimedDomain,
    Alloc::MARTE::Abstraction,
    Time::MARTE::Enumeration,
    Alloc::MARTE::Comment,
    Alloc::MARTE::Element,
    MARTE::Alloc::Assign,
    NFPs::NfpConstraint,
    MARTE::Time::TimedConstraint,
    MARTE::Time::ClockConstraint,
    MARTE::Alloc::Allocate,
    MARTE::Alloc::NfpRefine,
    Alloc::Allocated,
    Alloc::MARTE::ActivityPartition,
    MARTE::Alloc::AllocateActivityGroup,
    Alloc::MARTE::Dependency,
    TupleType,
    MARTE::NFPs::NfpType,
    CoreElements::Mode,
    Alloc::MARTE::NamedElement,
    MARTE::Alloc::Allocated,
    CoreElements::MARTE::State,
    MARTE::CoreElements::Mode,
    CoreElements::MARTE::Package,
    CoreElements::MARTE::StructuredClassifier,
    MARTE::CoreElements::Configuration,
    CoreElements::MARTE::StateMachine,
    MARTE::CoreElements::ModeBehavior,
    CoreElements::MARTE::Transition,
    MARTE::CoreElements::ModeTransition,
    NFPs::MARTE::Enumeration,
    NFPs::Dimension,
    MARTE::NFPs::Dimension,
    NFPs::MARTE::Constraint,
    MARTE::NFPs::NfpConstraint,
    NFPs::MARTE::EnumerationLiteral,
    NFPs::Unit,
    MARTE::NFPs::Unit,
    NFPs::MARTE::Property,
    CacheType,
    ConcurrencyKind,
    CallConcurrencyKind,
    ClientServerKind,
    MessageResourceKind,
    PortSpecificationKind,
    PLD_Class,
    WritePolicy,
    LaxityKind,
    AssignmentNature,
    ConcurrentAccessProtocolKind,
    dummy,
    VariableDirectionKind,
    AssignmentKind,
    ComponentKind,
    Repl_Policy,
    QueuePolicyKind,
    ROM_Type,
    NotificationKind,
    AllocationKind,
    ExecutionKind,
    PLD_Technology,
    AccessPolicyKind,
    AllocationEndKind,
    InterruptKind,
    DataPoolOrderingKind,
    ComponentState,
    PoolMgtPolicyKind,
    FlowDirectionKind,
    NotificationResourceKind,
    ConstraintKind,
    ISA_Type,
    MutualExclusionResourceKind,
    OptimallityCriterionKind,
    SynchronizationKind,
    AllocationNature,
    ConditionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gqam::marte::behavior_is_not_abstract():
    assert not inspect.isabstract(GQAM::MARTE::Behavior)


def test_gqam::marte::behavior_constructor_exists():
    assert callable(GQAM::MARTE::Behavior.__init__)


def test_gqam::marte::behavior_constructor_args():
    sig = inspect.signature(GQAM::MARTE::Behavior.__init__)
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



def test_gcm::clientserverspecification_is_not_abstract():
    assert not inspect.isabstract(GCM::ClientServerSpecification)


def test_gcm::clientserverspecification_constructor_exists():
    assert callable(GCM::ClientServerSpecification.__init__)


def test_gcm::clientserverspecification_constructor_args():
    sig = inspect.signature(GCM::ClientServerSpecification.__init__)
    params = list(sig.parameters.keys())



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



def test_pam::marte::namedelement_is_not_abstract():
    assert not inspect.isabstract(PAM::MARTE::NamedElement)


def test_pam::marte::namedelement_constructor_exists():
    assert callable(PAM::MARTE::NamedElement.__init__)


def test_pam::marte::namedelement_constructor_args():
    sig = inspect.signature(PAM::MARTE::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte::pam::paruntinstance_is_not_abstract():
    assert not inspect.isabstract(MARTE::PAM::PaRunTInstance)


def test_marte::pam::paruntinstance_constructor_exists():
    assert callable(MARTE::PAM::PaRunTInstance.__init__)


def test_marte::pam::paruntinstance_constructor_args():
    sig = inspect.signature(MARTE::PAM::PaRunTInstance.__init__)
    params = list(sig.parameters.keys())
    assert "utilization" in params, "Missing parameter 'utilization'"
    assert "poolSize" in params, "Missing parameter 'poolSize'"
    assert "unbddPool" in params, "Missing parameter 'unbddPool'"
    assert "throughput" in params, "Missing parameter 'throughput'"

def test_marte::pam::paruntinstance_has_utilization():
    assert hasattr(MARTE::PAM::PaRunTInstance, "utilization")
    descriptor = None
    for klass in MARTE::PAM::PaRunTInstance.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)

def test_marte::pam::paruntinstance_has_poolSize():
    assert hasattr(MARTE::PAM::PaRunTInstance, "poolSize")
    descriptor = None
    for klass in MARTE::PAM::PaRunTInstance.__mro__:
        if "poolSize" in klass.__dict__:
            descriptor = klass.__dict__["poolSize"]
            break
    assert isinstance(descriptor, property)

def test_marte::pam::paruntinstance_has_unbddPool():
    assert hasattr(MARTE::PAM::PaRunTInstance, "unbddPool")
    descriptor = None
    for klass in MARTE::PAM::PaRunTInstance.__mro__:
        if "unbddPool" in klass.__dict__:
            descriptor = klass.__dict__["unbddPool"]
            break
    assert isinstance(descriptor, property)

def test_marte::pam::paruntinstance_has_throughput():
    assert hasattr(MARTE::PAM::PaRunTInstance, "throughput")
    descriptor = None
    for klass in MARTE::PAM::PaRunTInstance.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
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
    assert "schSlack" in params, "Missing parameter 'schSlack'"
    assert "isSched" in params, "Missing parameter 'isSched'"
    assert "ISRswitchT" in params, "Missing parameter 'ISRswitchT'"
    assert "schedUtiliz" in params, "Missing parameter 'schedUtiliz'"
    assert "ISRprioRange" in params, "Missing parameter 'ISRprioRange'"

def test_marte::sam::saexechost_has_schSlack():
    assert hasattr(MARTE::SAM::SaExecHost, "schSlack")
    descriptor = None
    for klass in MARTE::SAM::SaExecHost.__mro__:
        if "schSlack" in klass.__dict__:
            descriptor = klass.__dict__["schSlack"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::saexechost_has_isSched():
    assert hasattr(MARTE::SAM::SaExecHost, "isSched")
    descriptor = None
    for klass in MARTE::SAM::SaExecHost.__mro__:
        if "isSched" in klass.__dict__:
            descriptor = klass.__dict__["isSched"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::saexechost_has_ISRswitchT():
    assert hasattr(MARTE::SAM::SaExecHost, "ISRswitchT")
    descriptor = None
    for klass in MARTE::SAM::SaExecHost.__mro__:
        if "ISRswitchT" in klass.__dict__:
            descriptor = klass.__dict__["ISRswitchT"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::saexechost_has_schedUtiliz():
    assert hasattr(MARTE::SAM::SaExecHost, "schedUtiliz")
    descriptor = None
    for klass in MARTE::SAM::SaExecHost.__mro__:
        if "schedUtiliz" in klass.__dict__:
            descriptor = klass.__dict__["schedUtiliz"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::saexechost_has_ISRprioRange():
    assert hasattr(MARTE::SAM::SaExecHost, "ISRprioRange")
    descriptor = None
    for klass in MARTE::SAM::SaExecHost.__mro__:
        if "ISRprioRange" in klass.__dict__:
            descriptor = klass.__dict__["ISRprioRange"]
            break
    assert isinstance(descriptor, property)



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
    assert "isSched" in params, "Missing parameter 'isSched'"
    assert "schSlack" in params, "Missing parameter 'schSlack'"

def test_marte::sam::sacommhost_has_isSched():
    assert hasattr(MARTE::SAM::SaCommHost, "isSched")
    descriptor = None
    for klass in MARTE::SAM::SaCommHost.__mro__:
        if "isSched" in klass.__dict__:
            descriptor = klass.__dict__["isSched"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sacommhost_has_schSlack():
    assert hasattr(MARTE::SAM::SaCommHost, "schSlack")
    descriptor = None
    for klass in MARTE::SAM::SaCommHost.__mro__:
        if "schSlack" in klass.__dict__:
            descriptor = klass.__dict__["schSlack"]
            break
    assert isinstance(descriptor, property)



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
    assert "releaseT" in params, "Missing parameter 'releaseT'"
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "isConsum" in params, "Missing parameter 'isConsum'"
    assert "acquisT" in params, "Missing parameter 'acquisT'"
    assert "isPreemp" in params, "Missing parameter 'isPreemp'"

def test_marte::sam::sasharedresource_has_releaseT():
    assert hasattr(MARTE::SAM::SaSharedResource, "releaseT")
    descriptor = None
    for klass in MARTE::SAM::SaSharedResource.__mro__:
        if "releaseT" in klass.__dict__:
            descriptor = klass.__dict__["releaseT"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sasharedresource_has_capacity():
    assert hasattr(MARTE::SAM::SaSharedResource, "capacity")
    descriptor = None
    for klass in MARTE::SAM::SaSharedResource.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sasharedresource_has_isConsum():
    assert hasattr(MARTE::SAM::SaSharedResource, "isConsum")
    descriptor = None
    for klass in MARTE::SAM::SaSharedResource.__mro__:
        if "isConsum" in klass.__dict__:
            descriptor = klass.__dict__["isConsum"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sasharedresource_has_acquisT():
    assert hasattr(MARTE::SAM::SaSharedResource, "acquisT")
    descriptor = None
    for klass in MARTE::SAM::SaSharedResource.__mro__:
        if "acquisT" in klass.__dict__:
            descriptor = klass.__dict__["acquisT"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sasharedresource_has_isPreemp():
    assert hasattr(MARTE::SAM::SaSharedResource, "isPreemp")
    descriptor = None
    for klass in MARTE::SAM::SaSharedResource.__mro__:
        if "isPreemp" in klass.__dict__:
            descriptor = klass.__dict__["isPreemp"]
            break
    assert isinstance(descriptor, property)



def test_sam::sasharedresource_is_not_abstract():
    assert not inspect.isabstract(SAM::SaSharedResource)


def test_sam::sasharedresource_constructor_exists():
    assert callable(SAM::SaSharedResource.__init__)


def test_sam::sasharedresource_constructor_args():
    sig = inspect.signature(SAM::SaSharedResource.__init__)
    params = list(sig.parameters.keys())



def test_sam::marte::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SAM::MARTE::BehavioralFeature)


def test_sam::marte::behavioralfeature_constructor_exists():
    assert callable(SAM::MARTE::BehavioralFeature.__init__)


def test_sam::marte::behavioralfeature_constructor_args():
    sig = inspect.signature(SAM::MARTE::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_marte::sam::saendtoendflow_is_not_abstract():
    assert not inspect.isabstract(MARTE::SAM::SaEndtoEndFlow)


def test_marte::sam::saendtoendflow_constructor_exists():
    assert callable(MARTE::SAM::SaEndtoEndFlow.__init__)


def test_marte::sam::saendtoendflow_constructor_args():
    sig = inspect.signature(MARTE::SAM::SaEndtoEndFlow.__init__)
    params = list(sig.parameters.keys())
    assert "end2EndT" in params, "Missing parameter 'end2EndT'"
    assert "schSlack" in params, "Missing parameter 'schSlack'"
    assert "end2EndD" in params, "Missing parameter 'end2EndD'"
    assert "isSched" in params, "Missing parameter 'isSched'"

def test_marte::sam::saendtoendflow_has_end2EndT():
    assert hasattr(MARTE::SAM::SaEndtoEndFlow, "end2EndT")
    descriptor = None
    for klass in MARTE::SAM::SaEndtoEndFlow.__mro__:
        if "end2EndT" in klass.__dict__:
            descriptor = klass.__dict__["end2EndT"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::saendtoendflow_has_schSlack():
    assert hasattr(MARTE::SAM::SaEndtoEndFlow, "schSlack")
    descriptor = None
    for klass in MARTE::SAM::SaEndtoEndFlow.__mro__:
        if "schSlack" in klass.__dict__:
            descriptor = klass.__dict__["schSlack"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::saendtoendflow_has_end2EndD():
    assert hasattr(MARTE::SAM::SaEndtoEndFlow, "end2EndD")
    descriptor = None
    for klass in MARTE::SAM::SaEndtoEndFlow.__mro__:
        if "end2EndD" in klass.__dict__:
            descriptor = klass.__dict__["end2EndD"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::saendtoendflow_has_isSched():
    assert hasattr(MARTE::SAM::SaEndtoEndFlow, "isSched")
    descriptor = None
    for klass in MARTE::SAM::SaEndtoEndFlow.__mro__:
        if "isSched" in klass.__dict__:
            descriptor = klass.__dict__["isSched"]
            break
    assert isinstance(descriptor, property)



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
    assert "isSched" in params, "Missing parameter 'isSched'"
    assert "optCriterion" in params, "Missing parameter 'optCriterion'"

def test_marte::sam::saanalysiscontext_has_isSched():
    assert hasattr(MARTE::SAM::SaAnalysisContext, "isSched")
    descriptor = None
    for klass in MARTE::SAM::SaAnalysisContext.__mro__:
        if "isSched" in klass.__dict__:
            descriptor = klass.__dict__["isSched"]
            break
    assert isinstance(descriptor, property)

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
    assert "context" in params, "Missing parameter 'context'"

def test_marte::gqam::gaanalysiscontext_has_context():
    assert hasattr(MARTE::GQAM::GaAnalysisContext, "context")
    descriptor = None
    for klass in MARTE::GQAM::GaAnalysisContext.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



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
    assert "deadline" in params, "Missing parameter 'deadline'"
    assert "spareCap" in params, "Missing parameter 'spareCap'"
    assert "schSlack" in params, "Missing parameter 'schSlack'"

def test_marte::sam::sacommstep_has_deadline():
    assert hasattr(MARTE::SAM::SaCommStep, "deadline")
    descriptor = None
    for klass in MARTE::SAM::SaCommStep.__mro__:
        if "deadline" in klass.__dict__:
            descriptor = klass.__dict__["deadline"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sacommstep_has_spareCap():
    assert hasattr(MARTE::SAM::SaCommStep, "spareCap")
    descriptor = None
    for klass in MARTE::SAM::SaCommStep.__mro__:
        if "spareCap" in klass.__dict__:
            descriptor = klass.__dict__["spareCap"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sacommstep_has_schSlack():
    assert hasattr(MARTE::SAM::SaCommStep, "schSlack")
    descriptor = None
    for klass in MARTE::SAM::SaCommStep.__mro__:
        if "schSlack" in klass.__dict__:
            descriptor = klass.__dict__["schSlack"]
            break
    assert isinstance(descriptor, property)



def test_sam::marte::namedelement_is_not_abstract():
    assert not inspect.isabstract(SAM::MARTE::NamedElement)


def test_sam::marte::namedelement_constructor_exists():
    assert callable(SAM::MARTE::NamedElement.__init__)


def test_sam::marte::namedelement_constructor_args():
    sig = inspect.signature(SAM::MARTE::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gaworkloadbehavior_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaWorkloadBehavior)


def test_marte::gqam::gaworkloadbehavior_constructor_exists():
    assert callable(MARTE::GQAM::GaWorkloadBehavior.__init__)


def test_marte::gqam::gaworkloadbehavior_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaWorkloadBehavior.__init__)
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
    assert "utilization" in params, "Missing parameter 'utilization'"
    assert "packetSize" in params, "Missing parameter 'packetSize'"

def test_marte::gqam::gacommchannel_has_utilization():
    assert hasattr(MARTE::GQAM::GaCommChannel, "utilization")
    descriptor = None
    for klass in MARTE::GQAM::GaCommChannel.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gacommchannel_has_packetSize():
    assert hasattr(MARTE::GQAM::GaCommChannel, "packetSize")
    descriptor = None
    for klass in MARTE::GQAM::GaCommChannel.__mro__:
        if "packetSize" in klass.__dict__:
            descriptor = klass.__dict__["packetSize"]
            break
    assert isinstance(descriptor, property)



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
    assert "suspentions" in params, "Missing parameter 'suspentions'"
    assert "overlaps" in params, "Missing parameter 'overlaps'"
    assert "blockT" in params, "Missing parameter 'blockT'"

def test_marte::sam::saschedobs_has_suspentions():
    assert hasattr(MARTE::SAM::SaSchedObs, "suspentions")
    descriptor = None
    for klass in MARTE::SAM::SaSchedObs.__mro__:
        if "suspentions" in klass.__dict__:
            descriptor = klass.__dict__["suspentions"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::saschedobs_has_overlaps():
    assert hasattr(MARTE::SAM::SaSchedObs, "overlaps")
    descriptor = None
    for klass in MARTE::SAM::SaSchedObs.__mro__:
        if "overlaps" in klass.__dict__:
            descriptor = klass.__dict__["overlaps"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::saschedobs_has_blockT():
    assert hasattr(MARTE::SAM::SaSchedObs, "blockT")
    descriptor = None
    for klass in MARTE::SAM::SaSchedObs.__mro__:
        if "blockT" in klass.__dict__:
            descriptor = klass.__dict__["blockT"]
            break
    assert isinstance(descriptor, property)



def test_marte::gqam::galatencyobs_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaLatencyObs)


def test_marte::gqam::galatencyobs_constructor_exists():
    assert callable(MARTE::GQAM::GaLatencyObs.__init__)


def test_marte::gqam::galatencyobs_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaLatencyObs.__init__)
    params = list(sig.parameters.keys())
    assert "utility" in params, "Missing parameter 'utility'"
    assert "latency" in params, "Missing parameter 'latency'"
    assert "miss" in params, "Missing parameter 'miss'"
    assert "maxJitter" in params, "Missing parameter 'maxJitter'"

def test_marte::gqam::galatencyobs_has_utility():
    assert hasattr(MARTE::GQAM::GaLatencyObs, "utility")
    descriptor = None
    for klass in MARTE::GQAM::GaLatencyObs.__mro__:
        if "utility" in klass.__dict__:
            descriptor = klass.__dict__["utility"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::galatencyobs_has_latency():
    assert hasattr(MARTE::GQAM::GaLatencyObs, "latency")
    descriptor = None
    for klass in MARTE::GQAM::GaLatencyObs.__mro__:
        if "latency" in klass.__dict__:
            descriptor = klass.__dict__["latency"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::galatencyobs_has_miss():
    assert hasattr(MARTE::GQAM::GaLatencyObs, "miss")
    descriptor = None
    for klass in MARTE::GQAM::GaLatencyObs.__mro__:
        if "miss" in klass.__dict__:
            descriptor = klass.__dict__["miss"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::galatencyobs_has_maxJitter():
    assert hasattr(MARTE::GQAM::GaLatencyObs, "maxJitter")
    descriptor = None
    for klass in MARTE::GQAM::GaLatencyObs.__mro__:
        if "maxJitter" in klass.__dict__:
            descriptor = klass.__dict__["maxJitter"]
            break
    assert isinstance(descriptor, property)



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



def test_marte::pam::parespassstep_is_not_abstract():
    assert not inspect.isabstract(MARTE::PAM::PaResPassStep)


def test_marte::pam::parespassstep_constructor_exists():
    assert callable(MARTE::PAM::PaResPassStep.__init__)


def test_marte::pam::parespassstep_constructor_args():
    sig = inspect.signature(MARTE::PAM::PaResPassStep.__init__)
    params = list(sig.parameters.keys())
    assert "resUnits" in params, "Missing parameter 'resUnits'"

def test_marte::pam::parespassstep_has_resUnits():
    assert hasattr(MARTE::PAM::PaResPassStep, "resUnits")
    descriptor = None
    for klass in MARTE::PAM::PaResPassStep.__mro__:
        if "resUnits" in klass.__dict__:
            descriptor = klass.__dict__["resUnits"]
            break
    assert isinstance(descriptor, property)



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
    assert "resUnits" in params, "Missing parameter 'resUnits'"

def test_marte::gqam::garelstep_has_resUnits():
    assert hasattr(MARTE::GQAM::GaRelStep, "resUnits")
    descriptor = None
    for klass in MARTE::GQAM::GaRelStep.__mro__:
        if "resUnits" in klass.__dict__:
            descriptor = klass.__dict__["resUnits"]
            break
    assert isinstance(descriptor, property)



def test_marte::sam::sastep_is_not_abstract():
    assert not inspect.isabstract(MARTE::SAM::SaStep)


def test_marte::sam::sastep_constructor_exists():
    assert callable(MARTE::SAM::SaStep.__init__)


def test_marte::sam::sastep_constructor_args():
    sig = inspect.signature(MARTE::SAM::SaStep.__init__)
    params = list(sig.parameters.keys())
    assert "schSlack" in params, "Missing parameter 'schSlack'"
    assert "selfSuspensionBlocking" in params, "Missing parameter 'selfSuspensionBlocking'"
    assert "deadline" in params, "Missing parameter 'deadline'"
    assert "spareCap" in params, "Missing parameter 'spareCap'"
    assert "readyT" in params, "Missing parameter 'readyT'"
    assert "numberSelfSuspensions" in params, "Missing parameter 'numberSelfSuspensions'"
    assert "nonpreemptionBlocking" in params, "Missing parameter 'nonpreemptionBlocking'"
    assert "preemptT" in params, "Missing parameter 'preemptT'"

def test_marte::sam::sastep_has_schSlack():
    assert hasattr(MARTE::SAM::SaStep, "schSlack")
    descriptor = None
    for klass in MARTE::SAM::SaStep.__mro__:
        if "schSlack" in klass.__dict__:
            descriptor = klass.__dict__["schSlack"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sastep_has_selfSuspensionBlocking():
    assert hasattr(MARTE::SAM::SaStep, "selfSuspensionBlocking")
    descriptor = None
    for klass in MARTE::SAM::SaStep.__mro__:
        if "selfSuspensionBlocking" in klass.__dict__:
            descriptor = klass.__dict__["selfSuspensionBlocking"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sastep_has_deadline():
    assert hasattr(MARTE::SAM::SaStep, "deadline")
    descriptor = None
    for klass in MARTE::SAM::SaStep.__mro__:
        if "deadline" in klass.__dict__:
            descriptor = klass.__dict__["deadline"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sastep_has_spareCap():
    assert hasattr(MARTE::SAM::SaStep, "spareCap")
    descriptor = None
    for klass in MARTE::SAM::SaStep.__mro__:
        if "spareCap" in klass.__dict__:
            descriptor = klass.__dict__["spareCap"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sastep_has_readyT():
    assert hasattr(MARTE::SAM::SaStep, "readyT")
    descriptor = None
    for klass in MARTE::SAM::SaStep.__mro__:
        if "readyT" in klass.__dict__:
            descriptor = klass.__dict__["readyT"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sastep_has_numberSelfSuspensions():
    assert hasattr(MARTE::SAM::SaStep, "numberSelfSuspensions")
    descriptor = None
    for klass in MARTE::SAM::SaStep.__mro__:
        if "numberSelfSuspensions" in klass.__dict__:
            descriptor = klass.__dict__["numberSelfSuspensions"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sastep_has_nonpreemptionBlocking():
    assert hasattr(MARTE::SAM::SaStep, "nonpreemptionBlocking")
    descriptor = None
    for klass in MARTE::SAM::SaStep.__mro__:
        if "nonpreemptionBlocking" in klass.__dict__:
            descriptor = klass.__dict__["nonpreemptionBlocking"]
            break
    assert isinstance(descriptor, property)

def test_marte::sam::sastep_has_preemptT():
    assert hasattr(MARTE::SAM::SaStep, "preemptT")
    descriptor = None
    for klass in MARTE::SAM::SaStep.__mro__:
        if "preemptT" in klass.__dict__:
            descriptor = klass.__dict__["preemptT"]
            break
    assert isinstance(descriptor, property)



def test_marte::gqam::gaacqstep_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaAcqStep)


def test_marte::gqam::gaacqstep_constructor_exists():
    assert callable(MARTE::GQAM::GaAcqStep.__init__)


def test_marte::gqam::gaacqstep_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaAcqStep.__init__)
    params = list(sig.parameters.keys())
    assert "resUnits" in params, "Missing parameter 'resUnits'"

def test_marte::gqam::gaacqstep_has_resUnits():
    assert hasattr(MARTE::GQAM::GaAcqStep, "resUnits")
    descriptor = None
    for klass in MARTE::GQAM::GaAcqStep.__mro__:
        if "resUnits" in klass.__dict__:
            descriptor = klass.__dict__["resUnits"]
            break
    assert isinstance(descriptor, property)



def test_marte::pam::pastep_is_not_abstract():
    assert not inspect.isabstract(MARTE::PAM::PaStep)


def test_marte::pam::pastep_constructor_exists():
    assert callable(MARTE::PAM::PaStep.__init__)


def test_marte::pam::pastep_constructor_args():
    sig = inspect.signature(MARTE::PAM::PaStep.__init__)
    params = list(sig.parameters.keys())
    assert "noSync" in params, "Missing parameter 'noSync'"
    assert "extOpCount" in params, "Missing parameter 'extOpCount'"
    assert "behavCount" in params, "Missing parameter 'behavCount'"
    assert "extOpDemand" in params, "Missing parameter 'extOpDemand'"

def test_marte::pam::pastep_has_noSync():
    assert hasattr(MARTE::PAM::PaStep, "noSync")
    descriptor = None
    for klass in MARTE::PAM::PaStep.__mro__:
        if "noSync" in klass.__dict__:
            descriptor = klass.__dict__["noSync"]
            break
    assert isinstance(descriptor, property)

def test_marte::pam::pastep_has_extOpCount():
    assert hasattr(MARTE::PAM::PaStep, "extOpCount")
    descriptor = None
    for klass in MARTE::PAM::PaStep.__mro__:
        if "extOpCount" in klass.__dict__:
            descriptor = klass.__dict__["extOpCount"]
            break
    assert isinstance(descriptor, property)

def test_marte::pam::pastep_has_behavCount():
    assert hasattr(MARTE::PAM::PaStep, "behavCount")
    descriptor = None
    for klass in MARTE::PAM::PaStep.__mro__:
        if "behavCount" in klass.__dict__:
            descriptor = klass.__dict__["behavCount"]
            break
    assert isinstance(descriptor, property)

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



def test_gqam::gaexechost_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaExecHost)


def test_gqam::gaexechost_constructor_exists():
    assert callable(GQAM::GaExecHost.__init__)


def test_gqam::gaexechost_constructor_args():
    sig = inspect.signature(GQAM::GaExecHost.__init__)
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
    assert "blockT" in params, "Missing parameter 'blockT'"
    assert "selfDelay" in params, "Missing parameter 'selfDelay'"
    assert "prob" in params, "Missing parameter 'prob'"
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"
    assert "rep" in params, "Missing parameter 'rep'"
    assert "servCount" in params, "Missing parameter 'servCount'"
    assert "priority" in params, "Missing parameter 'priority'"

def test_marte::gqam::gastep_has_blockT():
    assert hasattr(MARTE::GQAM::GaStep, "blockT")
    descriptor = None
    for klass in MARTE::GQAM::GaStep.__mro__:
        if "blockT" in klass.__dict__:
            descriptor = klass.__dict__["blockT"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gastep_has_selfDelay():
    assert hasattr(MARTE::GQAM::GaStep, "selfDelay")
    descriptor = None
    for klass in MARTE::GQAM::GaStep.__mro__:
        if "selfDelay" in klass.__dict__:
            descriptor = klass.__dict__["selfDelay"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gastep_has_prob():
    assert hasattr(MARTE::GQAM::GaStep, "prob")
    descriptor = None
    for klass in MARTE::GQAM::GaStep.__mro__:
        if "prob" in klass.__dict__:
            descriptor = klass.__dict__["prob"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gastep_has_isAtomic():
    assert hasattr(MARTE::GQAM::GaStep, "isAtomic")
    descriptor = None
    for klass in MARTE::GQAM::GaStep.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gastep_has_rep():
    assert hasattr(MARTE::GQAM::GaStep, "rep")
    descriptor = None
    for klass in MARTE::GQAM::GaStep.__mro__:
        if "rep" in klass.__dict__:
            descriptor = klass.__dict__["rep"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gastep_has_servCount():
    assert hasattr(MARTE::GQAM::GaStep, "servCount")
    descriptor = None
    for klass in MARTE::GQAM::GaStep.__mro__:
        if "servCount" in klass.__dict__:
            descriptor = klass.__dict__["servCount"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gastep_has_priority():
    assert hasattr(MARTE::GQAM::GaStep, "priority")
    descriptor = None
    for klass in MARTE::GQAM::GaStep.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_gqam::gatimedobs_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaTimedObs)


def test_gqam::gatimedobs_constructor_exists():
    assert callable(GQAM::GaTimedObs.__init__)


def test_gqam::gatimedobs_constructor_args():
    sig = inspect.signature(GQAM::GaTimedObs.__init__)
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
    assert "pattern" in params, "Missing parameter 'pattern'"

def test_marte::gqam::gaworkloadevent_has_pattern():
    assert hasattr(MARTE::GQAM::GaWorkloadEvent, "pattern")
    descriptor = None
    for klass in MARTE::GQAM::GaWorkloadEvent.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)



def test_gqam::marte::namedelement_is_not_abstract():
    assert not inspect.isabstract(GQAM::MARTE::NamedElement)


def test_gqam::marte::namedelement_constructor_exists():
    assert callable(GQAM::MARTE::NamedElement.__init__)


def test_gqam::marte::namedelement_constructor_args():
    sig = inspect.signature(GQAM::MARTE::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_gqam::gastep_is_not_abstract():
    assert not inspect.isabstract(GQAM::GaStep)


def test_gqam::gastep_constructor_exists():
    assert callable(GQAM::GaStep.__init__)


def test_gqam::gastep_constructor_args():
    sig = inspect.signature(GQAM::GaStep.__init__)
    params = list(sig.parameters.keys())



def test_marte::gqam::gaworkloadgenerator_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaWorkloadGenerator)


def test_marte::gqam::gaworkloadgenerator_constructor_exists():
    assert callable(MARTE::GQAM::GaWorkloadGenerator.__init__)


def test_marte::gqam::gaworkloadgenerator_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaWorkloadGenerator.__init__)
    params = list(sig.parameters.keys())
    assert "pop" in params, "Missing parameter 'pop'"

def test_marte::gqam::gaworkloadgenerator_has_pop():
    assert hasattr(MARTE::GQAM::GaWorkloadGenerator, "pop")
    descriptor = None
    for klass in MARTE::GQAM::GaWorkloadGenerator.__mro__:
        if "pop" in klass.__dict__:
            descriptor = klass.__dict__["pop"]
            break
    assert isinstance(descriptor, property)



def test_marte::gcm::gcminvocatingbehavior_is_not_abstract():
    assert not inspect.isabstract(MARTE::GCM::GCMInvocatingBehavior)


def test_marte::gcm::gcminvocatingbehavior_constructor_exists():
    assert callable(MARTE::GCM::GCMInvocatingBehavior.__init__)


def test_marte::gcm::gcminvocatingbehavior_constructor_args():
    sig = inspect.signature(MARTE::GCM::GCMInvocatingBehavior.__init__)
    params = list(sig.parameters.keys())



def test_gcm::marte::behavior_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::Behavior)


def test_gcm::marte::behavior_constructor_exists():
    assert callable(GCM::MARTE::Behavior.__init__)


def test_gcm::marte::behavior_constructor_args():
    sig = inspect.signature(GCM::MARTE::Behavior.__init__)
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



def test_marte::gqam::gaeventtrace_is_not_abstract():
    assert not inspect.isabstract(MARTE::GQAM::GaEventTrace)


def test_marte::gqam::gaeventtrace_constructor_exists():
    assert callable(MARTE::GQAM::GaEventTrace.__init__)


def test_marte::gqam::gaeventtrace_constructor_args():
    sig = inspect.signature(MARTE::GQAM::GaEventTrace.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "format" in params, "Missing parameter 'format'"
    assert "location" in params, "Missing parameter 'location'"

def test_marte::gqam::gaeventtrace_has_content():
    assert hasattr(MARTE::GQAM::GaEventTrace, "content")
    descriptor = None
    for klass in MARTE::GQAM::GaEventTrace.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

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



def test_marte::nfps::nfp_is_not_abstract():
    assert not inspect.isabstract(MARTE::NFPs::Nfp)


def test_marte::nfps::nfp_constructor_exists():
    assert callable(MARTE::NFPs::Nfp.__init__)


def test_marte::nfps::nfp_constructor_args():
    sig = inspect.signature(MARTE::NFPs::Nfp.__init__)
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
    assert "kind" in params, "Missing parameter 'kind'"
    assert "specificationKind" in params, "Missing parameter 'specificationKind'"

def test_marte::gcm::clientserverport_has_kind():
    assert hasattr(MARTE::GCM::ClientServerPort, "kind")
    descriptor = None
    for klass in MARTE::GCM::ClientServerPort.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_marte::gcm::clientserverport_has_specificationKind():
    assert hasattr(MARTE::GCM::ClientServerPort, "specificationKind")
    descriptor = None
    for klass in MARTE::GCM::ClientServerPort.__mro__:
        if "specificationKind" in klass.__dict__:
            descriptor = klass.__dict__["specificationKind"]
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
    assert "direction" in params, "Missing parameter 'direction'"
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"

def test_marte::gcm::flowport_has_direction():
    assert hasattr(MARTE::GCM::FlowPort, "direction")
    descriptor = None
    for klass in MARTE::GCM::FlowPort.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_marte::gcm::flowport_has_isAtomic():
    assert hasattr(MARTE::GCM::FlowPort, "isAtomic")
    descriptor = None
    for klass in MARTE::GCM::FlowPort.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)



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



def test_sw::interaction::swsynchronizationresource_is_not_abstract():
    assert not inspect.isabstract(SW::Interaction::SwSynchronizationResource)


def test_sw::interaction::swsynchronizationresource_constructor_exists():
    assert callable(SW::Interaction::SwSynchronizationResource.__init__)


def test_sw::interaction::swsynchronizationresource_constructor_args():
    sig = inspect.signature(SW::Interaction::SwSynchronizationResource.__init__)
    params = list(sig.parameters.keys())



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



def test_gcm::marte::property_is_not_abstract():
    assert not inspect.isabstract(GCM::MARTE::Property)


def test_gcm::marte::property_constructor_exists():
    assert callable(GCM::MARTE::Property.__init__)


def test_gcm::marte::property_constructor_args():
    sig = inspect.signature(GCM::MARTE::Property.__init__)
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
    assert "messageQueuePolicy" in params, "Missing parameter 'messageQueuePolicy'"
    assert "mechanism" in params, "Missing parameter 'mechanism'"
    assert "isFixedMessageSize" in params, "Missing parameter 'isFixedMessageSize'"

def test_marte::sw::interaction::messagecomresource_has_messageQueuePolicy():
    assert hasattr(MARTE::SW::Interaction::MessageComResource, "messageQueuePolicy")
    descriptor = None
    for klass in MARTE::SW::Interaction::MessageComResource.__mro__:
        if "messageQueuePolicy" in klass.__dict__:
            descriptor = klass.__dict__["messageQueuePolicy"]
            break
    assert isinstance(descriptor, property)

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
    assert "kind" in params, "Missing parameter 'kind'"
    assert "isMaskable" in params, "Missing parameter 'isMaskable'"

def test_marte::sw::concurrency::interruptresource_has_kind():
    assert hasattr(MARTE::SW::Concurrency::InterruptResource, "kind")
    descriptor = None
    for klass in MARTE::SW::Concurrency::InterruptResource.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::concurrency::interruptresource_has_isMaskable():
    assert hasattr(MARTE::SW::Concurrency::InterruptResource, "isMaskable")
    descriptor = None
    for klass in MARTE::SW::Concurrency::InterruptResource.__mro__:
        if "isMaskable" in klass.__dict__:
            descriptor = klass.__dict__["isMaskable"]
            break
    assert isinstance(descriptor, property)



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
    assert "isIntraMemoryPartitionInteraction" in params, "Missing parameter 'isIntraMemoryPartitionInteraction'"
    assert "waitingQueuePolicy" in params, "Missing parameter 'waitingQueuePolicy'"

def test_marte::sw::interaction::swinteractionresource_has_waitingQueueCapacity():
    assert hasattr(MARTE::SW::Interaction::SwInteractionResource, "waitingQueueCapacity")
    descriptor = None
    for klass in MARTE::SW::Interaction::SwInteractionResource.__mro__:
        if "waitingQueueCapacity" in klass.__dict__:
            descriptor = klass.__dict__["waitingQueueCapacity"]
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

def test_marte::sw::interaction::swinteractionresource_has_waitingQueuePolicy():
    assert hasattr(MARTE::SW::Interaction::SwInteractionResource, "waitingQueuePolicy")
    descriptor = None
    for klass in MARTE::SW::Interaction::SwInteractionResource.__mro__:
        if "waitingQueuePolicy" in klass.__dict__:
            descriptor = klass.__dict__["waitingQueuePolicy"]
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
    assert "accessPolicy" in params, "Missing parameter 'accessPolicy'"
    assert "isBuffered" in params, "Missing parameter 'isBuffered'"

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
    assert "type" in params, "Missing parameter 'type'"
    assert "activationCapacity" in params, "Missing parameter 'activationCapacity'"

def test_marte::sw::concurrency::swconcurrentresource_has_type():
    assert hasattr(MARTE::SW::Concurrency::SwConcurrentResource, "type")
    descriptor = None
    for klass in MARTE::SW::Concurrency::SwConcurrentResource.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::concurrency::swconcurrentresource_has_activationCapacity():
    assert hasattr(MARTE::SW::Concurrency::SwConcurrentResource, "activationCapacity")
    descriptor = None
    for klass in MARTE::SW::Concurrency::SwConcurrentResource.__mro__:
        if "activationCapacity" in klass.__dict__:
            descriptor = klass.__dict__["activationCapacity"]
            break
    assert isinstance(descriptor, property)



def test_sw::concurrency::marte::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SW::Concurrency::MARTE::BehavioralFeature)


def test_sw::concurrency::marte::behavioralfeature_constructor_exists():
    assert callable(SW::Concurrency::MARTE::BehavioralFeature.__init__)


def test_sw::concurrency::marte::behavioralfeature_constructor_args():
    sig = inspect.signature(SW::Concurrency::MARTE::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_sw::resourcecore::marte::property_is_not_abstract():
    assert not inspect.isabstract(SW::ResourceCore::MARTE::Property)


def test_sw::resourcecore::marte::property_constructor_exists():
    assert callable(SW::ResourceCore::MARTE::Property.__init__)


def test_sw::resourcecore::marte::property_constructor_args():
    sig = inspect.signature(SW::ResourceCore::MARTE::Property.__init__)
    params = list(sig.parameters.keys())



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



def test_sw::concurrency::marte::typedelement_is_not_abstract():
    assert not inspect.isabstract(SW::Concurrency::MARTE::TypedElement)


def test_sw::concurrency::marte::typedelement_constructor_exists():
    assert callable(SW::Concurrency::MARTE::TypedElement.__init__)


def test_sw::concurrency::marte::typedelement_constructor_args():
    sig = inspect.signature(SW::Concurrency::MARTE::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HwComponent)


def test_hwcomponent_constructor_exists():
    assert callable(HwComponent.__init__)


def test_hwcomponent_constructor_args():
    sig = inspect.signature(HwComponent.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwpower::hwcoolingsupply_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPower::HwCoolingSupply)


def test_marte::hwpower::hwcoolingsupply_constructor_exists():
    assert callable(MARTE::HwPower::HwCoolingSupply.__init__)


def test_marte::hwpower::hwcoolingsupply_constructor_args():
    sig = inspect.signature(MARTE::HwPower::HwCoolingSupply.__init__)
    params = list(sig.parameters.keys())
    assert "coolingPower" in params, "Missing parameter 'coolingPower'"

def test_marte::hwpower::hwcoolingsupply_has_coolingPower():
    assert hasattr(MARTE::HwPower::HwCoolingSupply, "coolingPower")
    descriptor = None
    for klass in MARTE::HwPower::HwCoolingSupply.__mro__:
        if "coolingPower" in klass.__dict__:
            descriptor = klass.__dict__["coolingPower"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwpower::hwpowersupply_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwPower::HwPowerSupply)


def test_marte::hwpower::hwpowersupply_constructor_exists():
    assert callable(MARTE::HwPower::HwPowerSupply.__init__)


def test_marte::hwpower::hwpowersupply_constructor_args():
    sig = inspect.signature(MARTE::HwPower::HwPowerSupply.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "suppliedPower" in params, "Missing parameter 'suppliedPower'"

def test_marte::hwpower::hwpowersupply_has_capacity():
    assert hasattr(MARTE::HwPower::HwPowerSupply, "capacity")
    descriptor = None
    for klass in MARTE::HwPower::HwPowerSupply.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwpower::hwpowersupply_has_suppliedPower():
    assert hasattr(MARTE::HwPower::HwPowerSupply, "suppliedPower")
    descriptor = None
    for klass in MARTE::HwPower::HwPowerSupply.__mro__:
        if "suppliedPower" in klass.__dict__:
            descriptor = klass.__dict__["suppliedPower"]
            break
    assert isinstance(descriptor, property)



def test_hwlayout::hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HwLayout::HwComponent)


def test_hwlayout::hwcomponent_constructor_exists():
    assert callable(HwLayout::HwComponent.__init__)


def test_hwlayout::hwcomponent_constructor_args():
    sig = inspect.signature(HwLayout::HwComponent.__init__)
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



def test_hwtiming::hwclock_is_not_abstract():
    assert not inspect.isabstract(HwTiming::HwClock)


def test_hwtiming::hwclock_constructor_exists():
    assert callable(HwTiming::HwClock.__init__)


def test_hwtiming::hwclock_constructor_args():
    sig = inspect.signature(HwTiming::HwClock.__init__)
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
    assert "counterWidth" in params, "Missing parameter 'counterWidth'"
    assert "nbCounters" in params, "Missing parameter 'nbCounters'"

def test_marte::hwtiming::hwtimer_has_counterWidth():
    assert hasattr(MARTE::HwTiming::HwTimer, "counterWidth")
    descriptor = None
    for klass in MARTE::HwTiming::HwTimer.__mro__:
        if "counterWidth" in klass.__dict__:
            descriptor = klass.__dict__["counterWidth"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwtiming::hwtimer_has_nbCounters():
    assert hasattr(MARTE::HwTiming::HwTimer, "nbCounters")
    descriptor = None
    for klass in MARTE::HwTiming::HwTimer.__mro__:
        if "nbCounters" in klass.__dict__:
            descriptor = klass.__dict__["nbCounters"]
            break
    assert isinstance(descriptor, property)



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



def test_hwdevice_is_not_abstract():
    assert not inspect.isabstract(HwDevice)


def test_hwdevice_constructor_exists():
    assert callable(HwDevice.__init__)


def test_hwdevice_constructor_args():
    sig = inspect.signature(HwDevice.__init__)
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



def test_grm::deviceresource_is_not_abstract():
    assert not inspect.isabstract(GRM::DeviceResource)


def test_grm::deviceresource_constructor_exists():
    assert callable(GRM::DeviceResource.__init__)


def test_grm::deviceresource_constructor_args():
    sig = inspect.signature(GRM::DeviceResource.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory_is_not_abstract():
    assert not inspect.isabstract(HwMemory)


def test_hwmemory_constructor_exists():
    assert callable(HwMemory.__init__)


def test_hwmemory_constructor_args():
    sig = inspect.signature(HwMemory.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwmemory::hwcache_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::HwCache)


def test_marte::hwmemory::hwcache_constructor_exists():
    assert callable(MARTE::HwMemory::HwCache.__init__)


def test_marte::hwmemory::hwcache_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::HwCache.__init__)
    params = list(sig.parameters.keys())
    assert "writePolicy" in params, "Missing parameter 'writePolicy'"
    assert "structure" in params, "Missing parameter 'structure'"
    assert "repl_Policy" in params, "Missing parameter 'repl_Policy'"
    assert "level" in params, "Missing parameter 'level'"
    assert "type" in params, "Missing parameter 'type'"

def test_marte::hwmemory::hwcache_has_writePolicy():
    assert hasattr(MARTE::HwMemory::HwCache, "writePolicy")
    descriptor = None
    for klass in MARTE::HwMemory::HwCache.__mro__:
        if "writePolicy" in klass.__dict__:
            descriptor = klass.__dict__["writePolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwmemory::hwcache_has_structure():
    assert hasattr(MARTE::HwMemory::HwCache, "structure")
    descriptor = None
    for klass in MARTE::HwMemory::HwCache.__mro__:
        if "structure" in klass.__dict__:
            descriptor = klass.__dict__["structure"]
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

def test_marte::hwmemory::hwcache_has_level():
    assert hasattr(MARTE::HwMemory::HwCache, "level")
    descriptor = None
    for klass in MARTE::HwMemory::HwCache.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
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



def test_marte::hwmemory::hwdrive_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::HwDrive)


def test_marte::hwmemory::hwdrive_constructor_exists():
    assert callable(MARTE::HwMemory::HwDrive.__init__)


def test_marte::hwmemory::hwdrive_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::HwDrive.__init__)
    params = list(sig.parameters.keys())
    assert "sectorSize" in params, "Missing parameter 'sectorSize'"

def test_marte::hwmemory::hwdrive_has_sectorSize():
    assert hasattr(MARTE::HwMemory::HwDrive, "sectorSize")
    descriptor = None
    for klass in MARTE::HwMemory::HwDrive.__mro__:
        if "sectorSize" in klass.__dict__:
            descriptor = klass.__dict__["sectorSize"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwmemory::hwrom_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::HwROM)


def test_marte::hwmemory::hwrom_constructor_exists():
    assert callable(MARTE::HwMemory::HwROM.__init__)


def test_marte::hwmemory::hwrom_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::HwROM.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "organization" in params, "Missing parameter 'organization'"

def test_marte::hwmemory::hwrom_has_type():
    assert hasattr(MARTE::HwMemory::HwROM, "type")
    descriptor = None
    for klass in MARTE::HwMemory::HwROM.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwmemory::hwrom_has_organization():
    assert hasattr(MARTE::HwMemory::HwROM, "organization")
    descriptor = None
    for klass in MARTE::HwMemory::HwROM.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwmemory::hwram_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::HwRAM)


def test_marte::hwmemory::hwram_constructor_exists():
    assert callable(MARTE::HwMemory::HwRAM.__init__)


def test_marte::hwmemory::hwram_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::HwRAM.__init__)
    params = list(sig.parameters.keys())
    assert "isNonVolatile" in params, "Missing parameter 'isNonVolatile'"
    assert "repl_Policy" in params, "Missing parameter 'repl_Policy'"
    assert "writePolicy" in params, "Missing parameter 'writePolicy'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_marte::hwmemory::hwram_has_isNonVolatile():
    assert hasattr(MARTE::HwMemory::HwRAM, "isNonVolatile")
    descriptor = None
    for klass in MARTE::HwMemory::HwRAM.__mro__:
        if "isNonVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isNonVolatile"]
            break
    assert isinstance(descriptor, property)

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

def test_marte::hwmemory::hwram_has_organization():
    assert hasattr(MARTE::HwMemory::HwRAM, "organization")
    descriptor = None
    for klass in MARTE::HwMemory::HwRAM.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwmemory::hwram_has_isSynchronous():
    assert hasattr(MARTE::HwMemory::HwRAM, "isSynchronous")
    descriptor = None
    for klass in MARTE::HwMemory::HwRAM.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwmemory::hwram_has_isStatic():
    assert hasattr(MARTE::HwMemory::HwRAM, "isStatic")
    descriptor = None
    for klass in MARTE::HwMemory::HwRAM.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_hwcomputing::hwprocessor_is_not_abstract():
    assert not inspect.isabstract(HwComputing::HwProcessor)


def test_hwcomputing::hwprocessor_constructor_exists():
    assert callable(HwComputing::HwProcessor.__init__)


def test_hwcomputing::hwprocessor_constructor_args():
    sig = inspect.signature(HwComputing::HwProcessor.__init__)
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



def test_grm::communicationendpoint_is_not_abstract():
    assert not inspect.isabstract(GRM::CommunicationEndPoint)


def test_grm::communicationendpoint_constructor_exists():
    assert callable(GRM::CommunicationEndPoint.__init__)


def test_grm::communicationendpoint_constructor_args():
    sig = inspect.signature(GRM::CommunicationEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_hwmedia_is_not_abstract():
    assert not inspect.isabstract(HwMedia)


def test_hwmedia_constructor_exists():
    assert callable(HwMedia.__init__)


def test_hwmedia_constructor_args():
    sig = inspect.signature(HwMedia.__init__)
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
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"
    assert "isSerial" in params, "Missing parameter 'isSerial'"
    assert "adressWidth" in params, "Missing parameter 'adressWidth'"
    assert "wordWidth" in params, "Missing parameter 'wordWidth'"

def test_marte::hwcommunication::hwbus_has_isSynchronous():
    assert hasattr(MARTE::HwCommunication::HwBus, "isSynchronous")
    descriptor = None
    for klass in MARTE::HwCommunication::HwBus.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcommunication::hwbus_has_isSerial():
    assert hasattr(MARTE::HwCommunication::HwBus, "isSerial")
    descriptor = None
    for klass in MARTE::HwCommunication::HwBus.__mro__:
        if "isSerial" in klass.__dict__:
            descriptor = klass.__dict__["isSerial"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcommunication::hwbus_has_adressWidth():
    assert hasattr(MARTE::HwCommunication::HwBus, "adressWidth")
    descriptor = None
    for klass in MARTE::HwCommunication::HwBus.__mro__:
        if "adressWidth" in klass.__dict__:
            descriptor = klass.__dict__["adressWidth"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcommunication::hwbus_has_wordWidth():
    assert hasattr(MARTE::HwCommunication::HwBus, "wordWidth")
    descriptor = None
    for klass in MARTE::HwCommunication::HwBus.__mro__:
        if "wordWidth" in klass.__dict__:
            descriptor = klass.__dict__["wordWidth"]
            break
    assert isinstance(descriptor, property)



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
    assert "transferWidth" in params, "Missing parameter 'transferWidth'"
    assert "nbChannels" in params, "Missing parameter 'nbChannels'"

def test_marte::hwstoragemanager::hwdma_has_transferWidth():
    assert hasattr(MARTE::HwStorageManager::HwDMA, "transferWidth")
    descriptor = None
    for klass in MARTE::HwStorageManager::HwDMA.__mro__:
        if "transferWidth" in klass.__dict__:
            descriptor = klass.__dict__["transferWidth"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwstoragemanager::hwdma_has_nbChannels():
    assert hasattr(MARTE::HwStorageManager::HwDMA, "nbChannels")
    descriptor = None
    for klass in MARTE::HwStorageManager::HwDMA.__mro__:
        if "nbChannels" in klass.__dict__:
            descriptor = klass.__dict__["nbChannels"]
            break
    assert isinstance(descriptor, property)



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
    assert "bandWidth" in params, "Missing parameter 'bandWidth'"

def test_marte::hwcommunication::hwmedia_has_bandWidth():
    assert hasattr(MARTE::HwCommunication::HwMedia, "bandWidth")
    descriptor = None
    for klass in MARTE::HwCommunication::HwMedia.__mro__:
        if "bandWidth" in klass.__dict__:
            descriptor = klass.__dict__["bandWidth"]
            break
    assert isinstance(descriptor, property)



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
    assert "virtualAddrSpace" in params, "Missing parameter 'virtualAddrSpace'"
    assert "memoryProtection" in params, "Missing parameter 'memoryProtection'"
    assert "nbEntries" in params, "Missing parameter 'nbEntries'"
    assert "physicalAddrSpace" in params, "Missing parameter 'physicalAddrSpace'"

def test_marte::hwstoragemanager::hwmmu_has_virtualAddrSpace():
    assert hasattr(MARTE::HwStorageManager::HwMMU, "virtualAddrSpace")
    descriptor = None
    for klass in MARTE::HwStorageManager::HwMMU.__mro__:
        if "virtualAddrSpace" in klass.__dict__:
            descriptor = klass.__dict__["virtualAddrSpace"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwstoragemanager::hwmmu_has_memoryProtection():
    assert hasattr(MARTE::HwStorageManager::HwMMU, "memoryProtection")
    descriptor = None
    for klass in MARTE::HwStorageManager::HwMMU.__mro__:
        if "memoryProtection" in klass.__dict__:
            descriptor = klass.__dict__["memoryProtection"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwstoragemanager::hwmmu_has_nbEntries():
    assert hasattr(MARTE::HwStorageManager::HwMMU, "nbEntries")
    descriptor = None
    for klass in MARTE::HwStorageManager::HwMMU.__mro__:
        if "nbEntries" in klass.__dict__:
            descriptor = klass.__dict__["nbEntries"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwstoragemanager::hwmmu_has_physicalAddrSpace():
    assert hasattr(MARTE::HwStorageManager::HwMMU, "physicalAddrSpace")
    descriptor = None
    for klass in MARTE::HwStorageManager::HwMMU.__mro__:
        if "physicalAddrSpace" in klass.__dict__:
            descriptor = klass.__dict__["physicalAddrSpace"]
            break
    assert isinstance(descriptor, property)



def test_hwcomputing::hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(HwComputing::HwComputingResource)


def test_hwcomputing::hwcomputingresource_constructor_exists():
    assert callable(HwComputing::HwComputingResource.__init__)


def test_hwcomputing::hwcomputingresource_constructor_args():
    sig = inspect.signature(HwComputing::HwComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory::hwram_is_not_abstract():
    assert not inspect.isabstract(HwMemory::HwRAM)


def test_hwmemory::hwram_constructor_exists():
    assert callable(HwMemory::HwRAM.__init__)


def test_hwmemory::hwram_constructor_args():
    sig = inspect.signature(HwMemory::HwRAM.__init__)
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



def test_marte::hwlayout::hwcomponent_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwLayout::HwComponent)


def test_marte::hwlayout::hwcomponent_constructor_exists():
    assert callable(MARTE::HwLayout::HwComponent.__init__)


def test_marte::hwlayout::hwcomponent_constructor_args():
    sig = inspect.signature(MARTE::HwLayout::HwComponent.__init__)
    params = list(sig.parameters.keys())
    assert "grid" in params, "Missing parameter 'grid'"
    assert "position" in params, "Missing parameter 'position'"
    assert "dimensions" in params, "Missing parameter 'dimensions'"
    assert "r_Conditions" in params, "Missing parameter 'r_Conditions'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "price" in params, "Missing parameter 'price'"
    assert "nbPins" in params, "Missing parameter 'nbPins'"
    assert "staticConsumption" in params, "Missing parameter 'staticConsumption'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "area" in params, "Missing parameter 'area'"
    assert "staticDissipation" in params, "Missing parameter 'staticDissipation'"

def test_marte::hwlayout::hwcomponent_has_grid():
    assert hasattr(MARTE::HwLayout::HwComponent, "grid")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "grid" in klass.__dict__:
            descriptor = klass.__dict__["grid"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwlayout::hwcomponent_has_position():
    assert hasattr(MARTE::HwLayout::HwComponent, "position")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwlayout::hwcomponent_has_dimensions():
    assert hasattr(MARTE::HwLayout::HwComponent, "dimensions")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwlayout::hwcomponent_has_r_Conditions():
    assert hasattr(MARTE::HwLayout::HwComponent, "r_Conditions")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "r_Conditions" in klass.__dict__:
            descriptor = klass.__dict__["r_Conditions"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwlayout::hwcomponent_has_weight():
    assert hasattr(MARTE::HwLayout::HwComponent, "weight")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwlayout::hwcomponent_has_price():
    assert hasattr(MARTE::HwLayout::HwComponent, "price")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwlayout::hwcomponent_has_nbPins():
    assert hasattr(MARTE::HwLayout::HwComponent, "nbPins")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "nbPins" in klass.__dict__:
            descriptor = klass.__dict__["nbPins"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwlayout::hwcomponent_has_staticConsumption():
    assert hasattr(MARTE::HwLayout::HwComponent, "staticConsumption")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "staticConsumption" in klass.__dict__:
            descriptor = klass.__dict__["staticConsumption"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwlayout::hwcomponent_has_kind():
    assert hasattr(MARTE::HwLayout::HwComponent, "kind")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwlayout::hwcomponent_has_area():
    assert hasattr(MARTE::HwLayout::HwComponent, "area")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "area" in klass.__dict__:
            descriptor = klass.__dict__["area"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwlayout::hwcomponent_has_staticDissipation():
    assert hasattr(MARTE::HwLayout::HwComponent, "staticDissipation")
    descriptor = None
    for klass in MARTE::HwLayout::HwComponent.__mro__:
        if "staticDissipation" in klass.__dict__:
            descriptor = klass.__dict__["staticDissipation"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwcomputing::hwbranchpredictor_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwBranchPredictor)


def test_marte::hwcomputing::hwbranchpredictor_constructor_exists():
    assert callable(MARTE::HwComputing::HwBranchPredictor.__init__)


def test_marte::hwcomputing::hwbranchpredictor_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwBranchPredictor.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcomputing::hwisa_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwISA)


def test_marte::hwcomputing::hwisa_constructor_exists():
    assert callable(MARTE::HwComputing::HwISA.__init__)


def test_marte::hwcomputing::hwisa_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwISA.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "family" in params, "Missing parameter 'family'"
    assert "inst_Width" in params, "Missing parameter 'inst_Width'"

def test_marte::hwcomputing::hwisa_has_type():
    assert hasattr(MARTE::HwComputing::HwISA, "type")
    descriptor = None
    for klass in MARTE::HwComputing::HwISA.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwisa_has_family():
    assert hasattr(MARTE::HwComputing::HwISA, "family")
    descriptor = None
    for klass in MARTE::HwComputing::HwISA.__mro__:
        if "family" in klass.__dict__:
            descriptor = klass.__dict__["family"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwisa_has_inst_Width():
    assert hasattr(MARTE::HwComputing::HwISA, "inst_Width")
    descriptor = None
    for klass in MARTE::HwComputing::HwISA.__mro__:
        if "inst_Width" in klass.__dict__:
            descriptor = klass.__dict__["inst_Width"]
            break
    assert isinstance(descriptor, property)



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



def test_marte::hwmemory::hwmemory_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwMemory::HwMemory)


def test_marte::hwmemory::hwmemory_constructor_exists():
    assert callable(MARTE::HwMemory::HwMemory.__init__)


def test_marte::hwmemory::hwmemory_constructor_args():
    sig = inspect.signature(MARTE::HwMemory::HwMemory.__init__)
    params = list(sig.parameters.keys())
    assert "adressSize" in params, "Missing parameter 'adressSize'"
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "timings" in params, "Missing parameter 'timings'"
    assert "memorySize" in params, "Missing parameter 'memorySize'"

def test_marte::hwmemory::hwmemory_has_adressSize():
    assert hasattr(MARTE::HwMemory::HwMemory, "adressSize")
    descriptor = None
    for klass in MARTE::HwMemory::HwMemory.__mro__:
        if "adressSize" in klass.__dict__:
            descriptor = klass.__dict__["adressSize"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwmemory::hwmemory_has_throughput():
    assert hasattr(MARTE::HwMemory::HwMemory, "throughput")
    descriptor = None
    for klass in MARTE::HwMemory::HwMemory.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwmemory::hwmemory_has_timings():
    assert hasattr(MARTE::HwMemory::HwMemory, "timings")
    descriptor = None
    for klass in MARTE::HwMemory::HwMemory.__mro__:
        if "timings" in klass.__dict__:
            descriptor = klass.__dict__["timings"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwmemory::hwmemory_has_memorySize():
    assert hasattr(MARTE::HwMemory::HwMemory, "memorySize")
    descriptor = None
    for klass in MARTE::HwMemory::HwMemory.__mro__:
        if "memorySize" in klass.__dict__:
            descriptor = klass.__dict__["memorySize"]
            break
    assert isinstance(descriptor, property)



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



def test_hwcomputing::hwisa_is_not_abstract():
    assert not inspect.isabstract(HwComputing::HwISA)


def test_hwcomputing::hwisa_constructor_exists():
    assert callable(HwComputing::HwISA.__init__)


def test_hwcomputing::hwisa_constructor_args():
    sig = inspect.signature(HwComputing::HwISA.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(HwComputingResource)


def test_hwcomputingresource_constructor_exists():
    assert callable(HwComputingResource.__init__)


def test_hwcomputingresource_constructor_args():
    sig = inspect.signature(HwComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcomputing::hwpld_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwPLD)


def test_marte::hwcomputing::hwpld_constructor_exists():
    assert callable(MARTE::HwComputing::HwPLD.__init__)


def test_marte::hwcomputing::hwpld_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwPLD.__init__)
    params = list(sig.parameters.keys())
    assert "ndLUT_Inputs" in params, "Missing parameter 'ndLUT_Inputs'"
    assert "technology" in params, "Missing parameter 'technology'"
    assert "nbFlipFlops" in params, "Missing parameter 'nbFlipFlops'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "nbLUTs" in params, "Missing parameter 'nbLUTs'"

def test_marte::hwcomputing::hwpld_has_ndLUT_Inputs():
    assert hasattr(MARTE::HwComputing::HwPLD, "ndLUT_Inputs")
    descriptor = None
    for klass in MARTE::HwComputing::HwPLD.__mro__:
        if "ndLUT_Inputs" in klass.__dict__:
            descriptor = klass.__dict__["ndLUT_Inputs"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwpld_has_technology():
    assert hasattr(MARTE::HwComputing::HwPLD, "technology")
    descriptor = None
    for klass in MARTE::HwComputing::HwPLD.__mro__:
        if "technology" in klass.__dict__:
            descriptor = klass.__dict__["technology"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwpld_has_nbFlipFlops():
    assert hasattr(MARTE::HwComputing::HwPLD, "nbFlipFlops")
    descriptor = None
    for klass in MARTE::HwComputing::HwPLD.__mro__:
        if "nbFlipFlops" in klass.__dict__:
            descriptor = klass.__dict__["nbFlipFlops"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwpld_has_organization():
    assert hasattr(MARTE::HwComputing::HwPLD, "organization")
    descriptor = None
    for klass in MARTE::HwComputing::HwPLD.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwpld_has_nbLUTs():
    assert hasattr(MARTE::HwComputing::HwPLD, "nbLUTs")
    descriptor = None
    for klass in MARTE::HwComputing::HwPLD.__mro__:
        if "nbLUTs" in klass.__dict__:
            descriptor = klass.__dict__["nbLUTs"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwcomputing::hwasic_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwASIC)


def test_marte::hwcomputing::hwasic_constructor_exists():
    assert callable(MARTE::HwComputing::HwASIC.__init__)


def test_marte::hwcomputing::hwasic_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwASIC.__init__)
    params = list(sig.parameters.keys())



def test_marte::hwcomputing::hwprocessor_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwProcessor)


def test_marte::hwcomputing::hwprocessor_constructor_exists():
    assert callable(MARTE::HwComputing::HwProcessor.__init__)


def test_marte::hwcomputing::hwprocessor_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwProcessor.__init__)
    params = list(sig.parameters.keys())
    assert "architecture" in params, "Missing parameter 'architecture'"
    assert "nbPipelines" in params, "Missing parameter 'nbPipelines'"
    assert "nbCores" in params, "Missing parameter 'nbCores'"
    assert "nbALUs" in params, "Missing parameter 'nbALUs'"
    assert "mips" in params, "Missing parameter 'mips'"
    assert "nbFPUs" in params, "Missing parameter 'nbFPUs'"
    assert "ipc" in params, "Missing parameter 'ipc'"
    assert "nbStages" in params, "Missing parameter 'nbStages'"

def test_marte::hwcomputing::hwprocessor_has_architecture():
    assert hasattr(MARTE::HwComputing::HwProcessor, "architecture")
    descriptor = None
    for klass in MARTE::HwComputing::HwProcessor.__mro__:
        if "architecture" in klass.__dict__:
            descriptor = klass.__dict__["architecture"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwprocessor_has_nbPipelines():
    assert hasattr(MARTE::HwComputing::HwProcessor, "nbPipelines")
    descriptor = None
    for klass in MARTE::HwComputing::HwProcessor.__mro__:
        if "nbPipelines" in klass.__dict__:
            descriptor = klass.__dict__["nbPipelines"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwprocessor_has_nbCores():
    assert hasattr(MARTE::HwComputing::HwProcessor, "nbCores")
    descriptor = None
    for klass in MARTE::HwComputing::HwProcessor.__mro__:
        if "nbCores" in klass.__dict__:
            descriptor = klass.__dict__["nbCores"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwprocessor_has_nbALUs():
    assert hasattr(MARTE::HwComputing::HwProcessor, "nbALUs")
    descriptor = None
    for klass in MARTE::HwComputing::HwProcessor.__mro__:
        if "nbALUs" in klass.__dict__:
            descriptor = klass.__dict__["nbALUs"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwprocessor_has_mips():
    assert hasattr(MARTE::HwComputing::HwProcessor, "mips")
    descriptor = None
    for klass in MARTE::HwComputing::HwProcessor.__mro__:
        if "mips" in klass.__dict__:
            descriptor = klass.__dict__["mips"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwprocessor_has_nbFPUs():
    assert hasattr(MARTE::HwComputing::HwProcessor, "nbFPUs")
    descriptor = None
    for klass in MARTE::HwComputing::HwProcessor.__mro__:
        if "nbFPUs" in klass.__dict__:
            descriptor = klass.__dict__["nbFPUs"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwprocessor_has_ipc():
    assert hasattr(MARTE::HwComputing::HwProcessor, "ipc")
    descriptor = None
    for klass in MARTE::HwComputing::HwProcessor.__mro__:
        if "ipc" in klass.__dict__:
            descriptor = klass.__dict__["ipc"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwcomputing::hwprocessor_has_nbStages():
    assert hasattr(MARTE::HwComputing::HwProcessor, "nbStages")
    descriptor = None
    for klass in MARTE::HwComputing::HwProcessor.__mro__:
        if "nbStages" in klass.__dict__:
            descriptor = klass.__dict__["nbStages"]
            break
    assert isinstance(descriptor, property)



def test_hwstoragemanager::hwmmu_is_not_abstract():
    assert not inspect.isabstract(HwStorageManager::HwMMU)


def test_hwstoragemanager::hwmmu_constructor_exists():
    assert callable(HwStorageManager::HwMMU.__init__)


def test_hwstoragemanager::hwmmu_constructor_args():
    sig = inspect.signature(HwStorageManager::HwMMU.__init__)
    params = list(sig.parameters.keys())



def test_marte::hlam::rtservice_is_not_abstract():
    assert not inspect.isabstract(MARTE::HLAM::RtService)


def test_marte::hlam::rtservice_constructor_exists():
    assert callable(MARTE::HLAM::RtService.__init__)


def test_marte::hlam::rtservice_constructor_args():
    sig = inspect.signature(MARTE::HLAM::RtService.__init__)
    params = list(sig.parameters.keys())
    assert "exeKind" in params, "Missing parameter 'exeKind'"
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"
    assert "concPolicy" in params, "Missing parameter 'concPolicy'"
    assert "synchKind" in params, "Missing parameter 'synchKind'"

def test_marte::hlam::rtservice_has_exeKind():
    assert hasattr(MARTE::HLAM::RtService, "exeKind")
    descriptor = None
    for klass in MARTE::HLAM::RtService.__mro__:
        if "exeKind" in klass.__dict__:
            descriptor = klass.__dict__["exeKind"]
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



def test_marte::hlam::rtaction_is_not_abstract():
    assert not inspect.isabstract(MARTE::HLAM::RtAction)


def test_marte::hlam::rtaction_constructor_exists():
    assert callable(MARTE::HLAM::RtAction.__init__)


def test_marte::hlam::rtaction_constructor_args():
    sig = inspect.signature(MARTE::HLAM::RtAction.__init__)
    params = list(sig.parameters.keys())
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"
    assert "msgSize" in params, "Missing parameter 'msgSize'"
    assert "synchKind" in params, "Missing parameter 'synchKind'"

def test_marte::hlam::rtaction_has_isAtomic():
    assert hasattr(MARTE::HLAM::RtAction, "isAtomic")
    descriptor = None
    for klass in MARTE::HLAM::RtAction.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtaction_has_msgSize():
    assert hasattr(MARTE::HLAM::RtAction, "msgSize")
    descriptor = None
    for klass in MARTE::HLAM::RtAction.__mro__:
        if "msgSize" in klass.__dict__:
            descriptor = klass.__dict__["msgSize"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtaction_has_synchKind():
    assert hasattr(MARTE::HLAM::RtAction, "synchKind")
    descriptor = None
    for klass in MARTE::HLAM::RtAction.__mro__:
        if "synchKind" in klass.__dict__:
            descriptor = klass.__dict__["synchKind"]
            break
    assert isinstance(descriptor, property)



def test_hlam::marte::comment_is_not_abstract():
    assert not inspect.isabstract(HLAM::MARTE::Comment)


def test_hlam::marte::comment_constructor_exists():
    assert callable(HLAM::MARTE::Comment.__init__)


def test_hlam::marte::comment_constructor_args():
    sig = inspect.signature(HLAM::MARTE::Comment.__init__)
    params = list(sig.parameters.keys())



def test_time::timedinstantobservation_is_not_abstract():
    assert not inspect.isabstract(Time::TimedInstantObservation)


def test_time::timedinstantobservation_constructor_exists():
    assert callable(Time::TimedInstantObservation.__init__)


def test_time::timedinstantobservation_constructor_args():
    sig = inspect.signature(Time::TimedInstantObservation.__init__)
    params = list(sig.parameters.keys())



def test_marte::hlam::rtspecification_is_not_abstract():
    assert not inspect.isabstract(MARTE::HLAM::RtSpecification)


def test_marte::hlam::rtspecification_constructor_exists():
    assert callable(MARTE::HLAM::RtSpecification.__init__)


def test_marte::hlam::rtspecification_constructor_args():
    sig = inspect.signature(MARTE::HLAM::RtSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "boundDl" in params, "Missing parameter 'boundDl'"
    assert "relDl" in params, "Missing parameter 'relDl'"
    assert "utility" in params, "Missing parameter 'utility'"
    assert "rdTime" in params, "Missing parameter 'rdTime'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "absDl" in params, "Missing parameter 'absDl'"
    assert "occKind" in params, "Missing parameter 'occKind'"
    assert "miss" in params, "Missing parameter 'miss'"

def test_marte::hlam::rtspecification_has_boundDl():
    assert hasattr(MARTE::HLAM::RtSpecification, "boundDl")
    descriptor = None
    for klass in MARTE::HLAM::RtSpecification.__mro__:
        if "boundDl" in klass.__dict__:
            descriptor = klass.__dict__["boundDl"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtspecification_has_relDl():
    assert hasattr(MARTE::HLAM::RtSpecification, "relDl")
    descriptor = None
    for klass in MARTE::HLAM::RtSpecification.__mro__:
        if "relDl" in klass.__dict__:
            descriptor = klass.__dict__["relDl"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtspecification_has_utility():
    assert hasattr(MARTE::HLAM::RtSpecification, "utility")
    descriptor = None
    for klass in MARTE::HLAM::RtSpecification.__mro__:
        if "utility" in klass.__dict__:
            descriptor = klass.__dict__["utility"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtspecification_has_rdTime():
    assert hasattr(MARTE::HLAM::RtSpecification, "rdTime")
    descriptor = None
    for klass in MARTE::HLAM::RtSpecification.__mro__:
        if "rdTime" in klass.__dict__:
            descriptor = klass.__dict__["rdTime"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtspecification_has_priority():
    assert hasattr(MARTE::HLAM::RtSpecification, "priority")
    descriptor = None
    for klass in MARTE::HLAM::RtSpecification.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtspecification_has_absDl():
    assert hasattr(MARTE::HLAM::RtSpecification, "absDl")
    descriptor = None
    for klass in MARTE::HLAM::RtSpecification.__mro__:
        if "absDl" in klass.__dict__:
            descriptor = klass.__dict__["absDl"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtspecification_has_occKind():
    assert hasattr(MARTE::HLAM::RtSpecification, "occKind")
    descriptor = None
    for klass in MARTE::HLAM::RtSpecification.__mro__:
        if "occKind" in klass.__dict__:
            descriptor = klass.__dict__["occKind"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::rtspecification_has_miss():
    assert hasattr(MARTE::HLAM::RtSpecification, "miss")
    descriptor = None
    for klass in MARTE::HLAM::RtSpecification.__mro__:
        if "miss" in klass.__dict__:
            descriptor = klass.__dict__["miss"]
            break
    assert isinstance(descriptor, property)



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
    assert "memorySize" in params, "Missing parameter 'memorySize'"
    assert "concPolicy" in params, "Missing parameter 'concPolicy'"

def test_marte::hlam::ppunit_has_memorySize():
    assert hasattr(MARTE::HLAM::PpUnit, "memorySize")
    descriptor = None
    for klass in MARTE::HLAM::PpUnit.__mro__:
        if "memorySize" in klass.__dict__:
            descriptor = klass.__dict__["memorySize"]
            break
    assert isinstance(descriptor, property)

def test_marte::hlam::ppunit_has_concPolicy():
    assert hasattr(MARTE::HLAM::PpUnit, "concPolicy")
    descriptor = None
    for klass in MARTE::HLAM::PpUnit.__mro__:
        if "concPolicy" in klass.__dict__:
            descriptor = klass.__dict__["concPolicy"]
            break
    assert isinstance(descriptor, property)



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
    assert "msgMaxSize" in params, "Missing parameter 'msgMaxSize'"
    assert "queueSchedPolicy" in params, "Missing parameter 'queueSchedPolicy'"
    assert "memorySize" in params, "Missing parameter 'memorySize'"
    assert "isMain" in params, "Missing parameter 'isMain'"
    assert "queueSize" in params, "Missing parameter 'queueSize'"
    assert "srPoolPolicy" in params, "Missing parameter 'srPoolPolicy'"
    assert "srPoolSize" in params, "Missing parameter 'srPoolSize'"
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"
    assert "srPoolWaitingTime" in params, "Missing parameter 'srPoolWaitingTime'"

def test_marte::hlam::rtunit_has_msgMaxSize():
    assert hasattr(MARTE::HLAM::RtUnit, "msgMaxSize")
    descriptor = None
    for klass in MARTE::HLAM::RtUnit.__mro__:
        if "msgMaxSize" in klass.__dict__:
            descriptor = klass.__dict__["msgMaxSize"]
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

def test_marte::hlam::rtunit_has_memorySize():
    assert hasattr(MARTE::HLAM::RtUnit, "memorySize")
    descriptor = None
    for klass in MARTE::HLAM::RtUnit.__mro__:
        if "memorySize" in klass.__dict__:
            descriptor = klass.__dict__["memorySize"]
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

def test_marte::hlam::rtunit_has_queueSize():
    assert hasattr(MARTE::HLAM::RtUnit, "queueSize")
    descriptor = None
    for klass in MARTE::HLAM::RtUnit.__mro__:
        if "queueSize" in klass.__dict__:
            descriptor = klass.__dict__["queueSize"]
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

def test_marte::hlam::rtunit_has_srPoolSize():
    assert hasattr(MARTE::HLAM::RtUnit, "srPoolSize")
    descriptor = None
    for klass in MARTE::HLAM::RtUnit.__mro__:
        if "srPoolSize" in klass.__dict__:
            descriptor = klass.__dict__["srPoolSize"]
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

def test_marte::hlam::rtunit_has_srPoolWaitingTime():
    assert hasattr(MARTE::HLAM::RtUnit, "srPoolWaitingTime")
    descriptor = None
    for klass in MARTE::HLAM::RtUnit.__mro__:
        if "srPoolWaitingTime" in klass.__dict__:
            descriptor = klass.__dict__["srPoolWaitingTime"]
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



def test_marte::datatypes::collectiontype_is_not_abstract():
    assert not inspect.isabstract(MARTE::DataTypes::CollectionType)


def test_marte::datatypes::collectiontype_constructor_exists():
    assert callable(MARTE::DataTypes::CollectionType.__init__)


def test_marte::datatypes::collectiontype_constructor_args():
    sig = inspect.signature(MARTE::DataTypes::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hlam::marte::behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(HLAM::MARTE::BehavioredClassifier)


def test_hlam::marte::behavioredclassifier_constructor_exists():
    assert callable(HLAM::MARTE::BehavioredClassifier.__init__)


def test_hlam::marte::behavioredclassifier_constructor_args():
    sig = inspect.signature(HLAM::MARTE::BehavioredClassifier.__init__)
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



def test_marte::datatypes::boundedsubtype_is_not_abstract():
    assert not inspect.isabstract(MARTE::DataTypes::BoundedSubtype)


def test_marte::datatypes::boundedsubtype_constructor_exists():
    assert callable(MARTE::DataTypes::BoundedSubtype.__init__)


def test_marte::datatypes::boundedsubtype_constructor_args():
    sig = inspect.signature(MARTE::DataTypes::BoundedSubtype.__init__)
    params = list(sig.parameters.keys())
    assert "isMaxOpen" in params, "Missing parameter 'isMaxOpen'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "minValue" in params, "Missing parameter 'minValue'"
    assert "isMinOpen" in params, "Missing parameter 'isMinOpen'"

def test_marte::datatypes::boundedsubtype_has_isMaxOpen():
    assert hasattr(MARTE::DataTypes::BoundedSubtype, "isMaxOpen")
    descriptor = None
    for klass in MARTE::DataTypes::BoundedSubtype.__mro__:
        if "isMaxOpen" in klass.__dict__:
            descriptor = klass.__dict__["isMaxOpen"]
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

def test_marte::datatypes::boundedsubtype_has_minValue():
    assert hasattr(MARTE::DataTypes::BoundedSubtype, "minValue")
    descriptor = None
    for klass in MARTE::DataTypes::BoundedSubtype.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)

def test_marte::datatypes::boundedsubtype_has_isMinOpen():
    assert hasattr(MARTE::DataTypes::BoundedSubtype, "isMinOpen")
    descriptor = None
    for klass in MARTE::DataTypes::BoundedSubtype.__mro__:
        if "isMinOpen" in klass.__dict__:
            descriptor = klass.__dict__["isMinOpen"]
            break
    assert isinstance(descriptor, property)



def test_operators::marte::behavior_is_not_abstract():
    assert not inspect.isabstract(Operators::MARTE::Behavior)


def test_operators::marte::behavior_constructor_exists():
    assert callable(Operators::MARTE::Behavior.__init__)


def test_operators::marte::behavior_constructor_args():
    sig = inspect.signature(Operators::MARTE::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_marte::operators::operator_is_not_abstract():
    assert not inspect.isabstract(MARTE::Operators::Operator)


def test_marte::operators::operator_constructor_exists():
    assert callable(MARTE::Operators::Operator.__init__)


def test_marte::operators::operator_constructor_args():
    sig = inspect.signature(MARTE::Operators::Operator.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "arity" in params, "Missing parameter 'arity'"

def test_marte::operators::operator_has_symbol():
    assert hasattr(MARTE::Operators::Operator, "symbol")
    descriptor = None
    for klass in MARTE::Operators::Operator.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_marte::operators::operator_has_arity():
    assert hasattr(MARTE::Operators::Operator, "arity")
    descriptor = None
    for klass in MARTE::Operators::Operator.__mro__:
        if "arity" in klass.__dict__:
            descriptor = klass.__dict__["arity"]
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
    assert "shape" in params, "Missing parameter 'shape'"

def test_marte::rsm::shaped_has_shape():
    assert hasattr(MARTE::RSM::Shaped, "shape")
    descriptor = None
    for klass in MARTE::RSM::Shaped.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_datatypes::marte::property_is_not_abstract():
    assert not inspect.isabstract(DataTypes::MARTE::Property)


def test_datatypes::marte::property_constructor_exists():
    assert callable(DataTypes::MARTE::Property.__init__)


def test_datatypes::marte::property_constructor_args():
    sig = inspect.signature(DataTypes::MARTE::Property.__init__)
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



def test_marte::rsm::distribute_is_not_abstract():
    assert not inspect.isabstract(MARTE::RSM::Distribute)


def test_marte::rsm::distribute_constructor_exists():
    assert callable(MARTE::RSM::Distribute.__init__)


def test_marte::rsm::distribute_constructor_args():
    sig = inspect.signature(MARTE::RSM::Distribute.__init__)
    params = list(sig.parameters.keys())
    assert "repetitionSpace" in params, "Missing parameter 'repetitionSpace'"
    assert "fromTiler" in params, "Missing parameter 'fromTiler'"
    assert "toTiler" in params, "Missing parameter 'toTiler'"
    assert "patternShape" in params, "Missing parameter 'patternShape'"

def test_marte::rsm::distribute_has_repetitionSpace():
    assert hasattr(MARTE::RSM::Distribute, "repetitionSpace")
    descriptor = None
    for klass in MARTE::RSM::Distribute.__mro__:
        if "repetitionSpace" in klass.__dict__:
            descriptor = klass.__dict__["repetitionSpace"]
            break
    assert isinstance(descriptor, property)

def test_marte::rsm::distribute_has_fromTiler():
    assert hasattr(MARTE::RSM::Distribute, "fromTiler")
    descriptor = None
    for klass in MARTE::RSM::Distribute.__mro__:
        if "fromTiler" in klass.__dict__:
            descriptor = klass.__dict__["fromTiler"]
            break
    assert isinstance(descriptor, property)

def test_marte::rsm::distribute_has_toTiler():
    assert hasattr(MARTE::RSM::Distribute, "toTiler")
    descriptor = None
    for klass in MARTE::RSM::Distribute.__mro__:
        if "toTiler" in klass.__dict__:
            descriptor = klass.__dict__["toTiler"]
            break
    assert isinstance(descriptor, property)

def test_marte::rsm::distribute_has_patternShape():
    assert hasattr(MARTE::RSM::Distribute, "patternShape")
    descriptor = None
    for klass in MARTE::RSM::Distribute.__mro__:
        if "patternShape" in klass.__dict__:
            descriptor = klass.__dict__["patternShape"]
            break
    assert isinstance(descriptor, property)



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
    assert "patternShape" in params, "Missing parameter 'patternShape'"
    assert "repetitonShape" in params, "Missing parameter 'repetitonShape'"

def test_marte::rsm::reshape_has_patternShape():
    assert hasattr(MARTE::RSM::Reshape, "patternShape")
    descriptor = None
    for klass in MARTE::RSM::Reshape.__mro__:
        if "patternShape" in klass.__dict__:
            descriptor = klass.__dict__["patternShape"]
            break
    assert isinstance(descriptor, property)

def test_marte::rsm::reshape_has_repetitonShape():
    assert hasattr(MARTE::RSM::Reshape, "repetitonShape")
    descriptor = None
    for klass in MARTE::RSM::Reshape.__mro__:
        if "repetitonShape" in klass.__dict__:
            descriptor = klass.__dict__["repetitonShape"]
            break
    assert isinstance(descriptor, property)



def test_marte::rsm::interrepetition_is_not_abstract():
    assert not inspect.isabstract(MARTE::RSM::InterRepetition)


def test_marte::rsm::interrepetition_constructor_exists():
    assert callable(MARTE::RSM::InterRepetition.__init__)


def test_marte::rsm::interrepetition_constructor_args():
    sig = inspect.signature(MARTE::RSM::InterRepetition.__init__)
    params = list(sig.parameters.keys())
    assert "repetitionShapeDependence" in params, "Missing parameter 'repetitionShapeDependence'"
    assert "isModulo" in params, "Missing parameter 'isModulo'"

def test_marte::rsm::interrepetition_has_repetitionShapeDependence():
    assert hasattr(MARTE::RSM::InterRepetition, "repetitionShapeDependence")
    descriptor = None
    for klass in MARTE::RSM::InterRepetition.__mro__:
        if "repetitionShapeDependence" in klass.__dict__:
            descriptor = klass.__dict__["repetitionShapeDependence"]
            break
    assert isinstance(descriptor, property)

def test_marte::rsm::interrepetition_has_isModulo():
    assert hasattr(MARTE::RSM::InterRepetition, "isModulo")
    descriptor = None
    for klass in MARTE::RSM::InterRepetition.__mro__:
        if "isModulo" in klass.__dict__:
            descriptor = klass.__dict__["isModulo"]
            break
    assert isinstance(descriptor, property)



def test_marte::rsm::tiler_is_not_abstract():
    assert not inspect.isabstract(MARTE::RSM::Tiler)


def test_marte::rsm::tiler_constructor_exists():
    assert callable(MARTE::RSM::Tiler.__init__)


def test_marte::rsm::tiler_constructor_args():
    sig = inspect.signature(MARTE::RSM::Tiler.__init__)
    params = list(sig.parameters.keys())
    assert "fitting" in params, "Missing parameter 'fitting'"
    assert "tiler" in params, "Missing parameter 'tiler'"
    assert "paving" in params, "Missing parameter 'paving'"
    assert "origin" in params, "Missing parameter 'origin'"

def test_marte::rsm::tiler_has_fitting():
    assert hasattr(MARTE::RSM::Tiler, "fitting")
    descriptor = None
    for klass in MARTE::RSM::Tiler.__mro__:
        if "fitting" in klass.__dict__:
            descriptor = klass.__dict__["fitting"]
            break
    assert isinstance(descriptor, property)

def test_marte::rsm::tiler_has_tiler():
    assert hasattr(MARTE::RSM::Tiler, "tiler")
    descriptor = None
    for klass in MARTE::RSM::Tiler.__mro__:
        if "tiler" in klass.__dict__:
            descriptor = klass.__dict__["tiler"]
            break
    assert isinstance(descriptor, property)

def test_marte::rsm::tiler_has_paving():
    assert hasattr(MARTE::RSM::Tiler, "paving")
    descriptor = None
    for klass in MARTE::RSM::Tiler.__mro__:
        if "paving" in klass.__dict__:
            descriptor = klass.__dict__["paving"]
            break
    assert isinstance(descriptor, property)

def test_marte::rsm::tiler_has_origin():
    assert hasattr(MARTE::RSM::Tiler, "origin")
    descriptor = None
    for klass in MARTE::RSM::Tiler.__mro__:
        if "origin" in klass.__dict__:
            descriptor = klass.__dict__["origin"]
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
    assert "utilizationOnHost" in params, "Missing parameter 'utilizationOnHost'"
    assert "interOccT" in params, "Missing parameter 'interOccT'"
    assert "respT" in params, "Missing parameter 'respT'"
    assert "utilization" in params, "Missing parameter 'utilization'"
    assert "hostDemand" in params, "Missing parameter 'hostDemand'"
    assert "hostDemandOps" in params, "Missing parameter 'hostDemandOps'"
    assert "throughput" in params, "Missing parameter 'throughput'"

def test_marte::gqam::gascenario_has_utilizationOnHost():
    assert hasattr(MARTE::GQAM::GaScenario, "utilizationOnHost")
    descriptor = None
    for klass in MARTE::GQAM::GaScenario.__mro__:
        if "utilizationOnHost" in klass.__dict__:
            descriptor = klass.__dict__["utilizationOnHost"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gascenario_has_interOccT():
    assert hasattr(MARTE::GQAM::GaScenario, "interOccT")
    descriptor = None
    for klass in MARTE::GQAM::GaScenario.__mro__:
        if "interOccT" in klass.__dict__:
            descriptor = klass.__dict__["interOccT"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gascenario_has_respT():
    assert hasattr(MARTE::GQAM::GaScenario, "respT")
    descriptor = None
    for klass in MARTE::GQAM::GaScenario.__mro__:
        if "respT" in klass.__dict__:
            descriptor = klass.__dict__["respT"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gascenario_has_utilization():
    assert hasattr(MARTE::GQAM::GaScenario, "utilization")
    descriptor = None
    for klass in MARTE::GQAM::GaScenario.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gascenario_has_hostDemand():
    assert hasattr(MARTE::GQAM::GaScenario, "hostDemand")
    descriptor = None
    for klass in MARTE::GQAM::GaScenario.__mro__:
        if "hostDemand" in klass.__dict__:
            descriptor = klass.__dict__["hostDemand"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gascenario_has_hostDemandOps():
    assert hasattr(MARTE::GQAM::GaScenario, "hostDemandOps")
    descriptor = None
    for klass in MARTE::GQAM::GaScenario.__mro__:
        if "hostDemandOps" in klass.__dict__:
            descriptor = klass.__dict__["hostDemandOps"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gascenario_has_throughput():
    assert hasattr(MARTE::GQAM::GaScenario, "throughput")
    descriptor = None
    for klass in MARTE::GQAM::GaScenario.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
            break
    assert isinstance(descriptor, property)



def test_grm::marte::namedelement_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::NamedElement)


def test_grm::marte::namedelement_constructor_exists():
    assert callable(GRM::MARTE::NamedElement.__init__)


def test_grm::marte::namedelement_constructor_args():
    sig = inspect.signature(GRM::MARTE::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_rsm::marte::connectorend_is_not_abstract():
    assert not inspect.isabstract(RSM::MARTE::ConnectorEnd)


def test_rsm::marte::connectorend_constructor_exists():
    assert callable(RSM::MARTE::ConnectorEnd.__init__)


def test_rsm::marte::connectorend_constructor_args():
    sig = inspect.signature(RSM::MARTE::ConnectorEnd.__init__)
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
    assert "dissipation" in params, "Missing parameter 'dissipation'"
    assert "consumption" in params, "Missing parameter 'consumption'"

def test_marte::hwgeneral::hwresourceservice_has_dissipation():
    assert hasattr(MARTE::HwGeneral::HwResourceService, "dissipation")
    descriptor = None
    for klass in MARTE::HwGeneral::HwResourceService.__mro__:
        if "dissipation" in klass.__dict__:
            descriptor = klass.__dict__["dissipation"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwgeneral::hwresourceservice_has_consumption():
    assert hasattr(MARTE::HwGeneral::HwResourceService, "consumption")
    descriptor = None
    for klass in MARTE::HwGeneral::HwResourceService.__mro__:
        if "consumption" in klass.__dict__:
            descriptor = klass.__dict__["consumption"]
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
    assert "duration" in params, "Missing parameter 'duration'"

def test_marte::grm::timerresource_has_isPeriodic():
    assert hasattr(MARTE::GRM::TimerResource, "isPeriodic")
    descriptor = None
    for klass in MARTE::GRM::TimerResource.__mro__:
        if "isPeriodic" in klass.__dict__:
            descriptor = klass.__dict__["isPeriodic"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::timerresource_has_duration():
    assert hasattr(MARTE::GRM::TimerResource, "duration")
    descriptor = None
    for klass in MARTE::GRM::TimerResource.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::clockresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::ClockResource)


def test_marte::grm::clockresource_constructor_exists():
    assert callable(MARTE::GRM::ClockResource.__init__)


def test_marte::grm::clockresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::ClockResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::resourceusage_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::ResourceUsage)


def test_marte::grm::resourceusage_constructor_exists():
    assert callable(MARTE::GRM::ResourceUsage.__init__)


def test_marte::grm::resourceusage_constructor_args():
    sig = inspect.signature(MARTE::GRM::ResourceUsage.__init__)
    params = list(sig.parameters.keys())
    assert "powerPeak" in params, "Missing parameter 'powerPeak'"
    assert "execTime" in params, "Missing parameter 'execTime'"
    assert "energy" in params, "Missing parameter 'energy'"
    assert "usedMemory" in params, "Missing parameter 'usedMemory'"
    assert "allocatedMemory" in params, "Missing parameter 'allocatedMemory'"
    assert "msgSize" in params, "Missing parameter 'msgSize'"

def test_marte::grm::resourceusage_has_powerPeak():
    assert hasattr(MARTE::GRM::ResourceUsage, "powerPeak")
    descriptor = None
    for klass in MARTE::GRM::ResourceUsage.__mro__:
        if "powerPeak" in klass.__dict__:
            descriptor = klass.__dict__["powerPeak"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::resourceusage_has_execTime():
    assert hasattr(MARTE::GRM::ResourceUsage, "execTime")
    descriptor = None
    for klass in MARTE::GRM::ResourceUsage.__mro__:
        if "execTime" in klass.__dict__:
            descriptor = klass.__dict__["execTime"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::resourceusage_has_energy():
    assert hasattr(MARTE::GRM::ResourceUsage, "energy")
    descriptor = None
    for klass in MARTE::GRM::ResourceUsage.__mro__:
        if "energy" in klass.__dict__:
            descriptor = klass.__dict__["energy"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::resourceusage_has_usedMemory():
    assert hasattr(MARTE::GRM::ResourceUsage, "usedMemory")
    descriptor = None
    for klass in MARTE::GRM::ResourceUsage.__mro__:
        if "usedMemory" in klass.__dict__:
            descriptor = klass.__dict__["usedMemory"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::resourceusage_has_allocatedMemory():
    assert hasattr(MARTE::GRM::ResourceUsage, "allocatedMemory")
    descriptor = None
    for klass in MARTE::GRM::ResourceUsage.__mro__:
        if "allocatedMemory" in klass.__dict__:
            descriptor = klass.__dict__["allocatedMemory"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::resourceusage_has_msgSize():
    assert hasattr(MARTE::GRM::ResourceUsage, "msgSize")
    descriptor = None
    for klass in MARTE::GRM::ResourceUsage.__mro__:
        if "msgSize" in klass.__dict__:
            descriptor = klass.__dict__["msgSize"]
            break
    assert isinstance(descriptor, property)



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



def test_processingresource_is_not_abstract():
    assert not inspect.isabstract(ProcessingResource)


def test_processingresource_constructor_exists():
    assert callable(ProcessingResource.__init__)


def test_processingresource_constructor_args():
    sig = inspect.signature(ProcessingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::deviceresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::DeviceResource)


def test_marte::grm::deviceresource_constructor_exists():
    assert callable(MARTE::GRM::DeviceResource.__init__)


def test_marte::grm::deviceresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::DeviceResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::communicationmedia_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::CommunicationMedia)


def test_marte::grm::communicationmedia_constructor_exists():
    assert callable(MARTE::GRM::CommunicationMedia.__init__)


def test_marte::grm::communicationmedia_constructor_args():
    sig = inspect.signature(MARTE::GRM::CommunicationMedia.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "transmMode" in params, "Missing parameter 'transmMode'"
    assert "blockT" in params, "Missing parameter 'blockT'"
    assert "elementSize" in params, "Missing parameter 'elementSize'"
    assert "packetT" in params, "Missing parameter 'packetT'"

def test_marte::grm::communicationmedia_has_capacity():
    assert hasattr(MARTE::GRM::CommunicationMedia, "capacity")
    descriptor = None
    for klass in MARTE::GRM::CommunicationMedia.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::communicationmedia_has_transmMode():
    assert hasattr(MARTE::GRM::CommunicationMedia, "transmMode")
    descriptor = None
    for klass in MARTE::GRM::CommunicationMedia.__mro__:
        if "transmMode" in klass.__dict__:
            descriptor = klass.__dict__["transmMode"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::communicationmedia_has_blockT():
    assert hasattr(MARTE::GRM::CommunicationMedia, "blockT")
    descriptor = None
    for klass in MARTE::GRM::CommunicationMedia.__mro__:
        if "blockT" in klass.__dict__:
            descriptor = klass.__dict__["blockT"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::communicationmedia_has_elementSize():
    assert hasattr(MARTE::GRM::CommunicationMedia, "elementSize")
    descriptor = None
    for klass in MARTE::GRM::CommunicationMedia.__mro__:
        if "elementSize" in klass.__dict__:
            descriptor = klass.__dict__["elementSize"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::communicationmedia_has_packetT():
    assert hasattr(MARTE::GRM::CommunicationMedia, "packetT")
    descriptor = None
    for klass in MARTE::GRM::CommunicationMedia.__mro__:
        if "packetT" in klass.__dict__:
            descriptor = klass.__dict__["packetT"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::computingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::ComputingResource)


def test_marte::grm::computingresource_constructor_exists():
    assert callable(MARTE::GRM::ComputingResource.__init__)


def test_marte::grm::computingresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::ComputingResource.__init__)
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
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "utilization" in params, "Missing parameter 'utilization'"

def test_marte::gqam::gacommhost_has_throughput():
    assert hasattr(MARTE::GQAM::GaCommHost, "throughput")
    descriptor = None
    for klass in MARTE::GQAM::GaCommHost.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gacommhost_has_utilization():
    assert hasattr(MARTE::GQAM::GaCommHost, "utilization")
    descriptor = None
    for klass in MARTE::GQAM::GaCommHost.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)



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
    assert "isStaticSchedulingFeature" in params, "Missing parameter 'isStaticSchedulingFeature'"
    assert "isPreemptable" in params, "Missing parameter 'isPreemptable'"

def test_marte::sw::concurrency::swschedulableresource_has_isStaticSchedulingFeature():
    assert hasattr(MARTE::SW::Concurrency::SwSchedulableResource, "isStaticSchedulingFeature")
    descriptor = None
    for klass in MARTE::SW::Concurrency::SwSchedulableResource.__mro__:
        if "isStaticSchedulingFeature" in klass.__dict__:
            descriptor = klass.__dict__["isStaticSchedulingFeature"]
            break
    assert isinstance(descriptor, property)

def test_marte::sw::concurrency::swschedulableresource_has_isPreemptable():
    assert hasattr(MARTE::SW::Concurrency::SwSchedulableResource, "isPreemptable")
    descriptor = None
    for klass in MARTE::SW::Concurrency::SwSchedulableResource.__mro__:
        if "isPreemptable" in klass.__dict__:
            descriptor = klass.__dict__["isPreemptable"]
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
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "schedPriRange" in params, "Missing parameter 'schedPriRange'"
    assert "cntxtSwT" in params, "Missing parameter 'cntxtSwT'"
    assert "clockOvh" in params, "Missing parameter 'clockOvh'"
    assert "utilization" in params, "Missing parameter 'utilization'"
    assert "memSize" in params, "Missing parameter 'memSize'"
    assert "commTxOvh" in params, "Missing parameter 'commTxOvh'"
    assert "commRcvOvh" in params, "Missing parameter 'commRcvOvh'"

def test_marte::gqam::gaexechost_has_throughput():
    assert hasattr(MARTE::GQAM::GaExecHost, "throughput")
    descriptor = None
    for klass in MARTE::GQAM::GaExecHost.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gaexechost_has_schedPriRange():
    assert hasattr(MARTE::GQAM::GaExecHost, "schedPriRange")
    descriptor = None
    for klass in MARTE::GQAM::GaExecHost.__mro__:
        if "schedPriRange" in klass.__dict__:
            descriptor = klass.__dict__["schedPriRange"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gaexechost_has_cntxtSwT():
    assert hasattr(MARTE::GQAM::GaExecHost, "cntxtSwT")
    descriptor = None
    for klass in MARTE::GQAM::GaExecHost.__mro__:
        if "cntxtSwT" in klass.__dict__:
            descriptor = klass.__dict__["cntxtSwT"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gaexechost_has_clockOvh():
    assert hasattr(MARTE::GQAM::GaExecHost, "clockOvh")
    descriptor = None
    for klass in MARTE::GQAM::GaExecHost.__mro__:
        if "clockOvh" in klass.__dict__:
            descriptor = klass.__dict__["clockOvh"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gaexechost_has_utilization():
    assert hasattr(MARTE::GQAM::GaExecHost, "utilization")
    descriptor = None
    for klass in MARTE::GQAM::GaExecHost.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gaexechost_has_memSize():
    assert hasattr(MARTE::GQAM::GaExecHost, "memSize")
    descriptor = None
    for klass in MARTE::GQAM::GaExecHost.__mro__:
        if "memSize" in klass.__dict__:
            descriptor = klass.__dict__["memSize"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gaexechost_has_commTxOvh():
    assert hasattr(MARTE::GQAM::GaExecHost, "commTxOvh")
    descriptor = None
    for klass in MARTE::GQAM::GaExecHost.__mro__:
        if "commTxOvh" in klass.__dict__:
            descriptor = klass.__dict__["commTxOvh"]
            break
    assert isinstance(descriptor, property)

def test_marte::gqam::gaexechost_has_commRcvOvh():
    assert hasattr(MARTE::GQAM::GaExecHost, "commRcvOvh")
    descriptor = None
    for klass in MARTE::GQAM::GaExecHost.__mro__:
        if "commRcvOvh" in klass.__dict__:
            descriptor = klass.__dict__["commRcvOvh"]
            break
    assert isinstance(descriptor, property)



def test_marte::hwcomputing::hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwComputing::HwComputingResource)


def test_marte::hwcomputing::hwcomputingresource_constructor_exists():
    assert callable(MARTE::HwComputing::HwComputingResource.__init__)


def test_marte::hwcomputing::hwcomputingresource_constructor_args():
    sig = inspect.signature(MARTE::HwComputing::HwComputingResource.__init__)
    params = list(sig.parameters.keys())
    assert "op_Frequencies" in params, "Missing parameter 'op_Frequencies'"

def test_marte::hwcomputing::hwcomputingresource_has_op_Frequencies():
    assert hasattr(MARTE::HwComputing::HwComputingResource, "op_Frequencies")
    descriptor = None
    for klass in MARTE::HwComputing::HwComputingResource.__mro__:
        if "op_Frequencies" in klass.__dict__:
            descriptor = klass.__dict__["op_Frequencies"]
            break
    assert isinstance(descriptor, property)



def test_grm::processingresource_is_not_abstract():
    assert not inspect.isabstract(GRM::ProcessingResource)


def test_grm::processingresource_constructor_exists():
    assert callable(GRM::ProcessingResource.__init__)


def test_grm::processingresource_constructor_args():
    sig = inspect.signature(GRM::ProcessingResource.__init__)
    params = list(sig.parameters.keys())



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_marte::sw::resourcecore::swresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::SW::ResourceCore::SwResource)


def test_marte::sw::resourcecore::swresource_constructor_exists():
    assert callable(MARTE::SW::ResourceCore::SwResource.__init__)


def test_marte::sw::resourcecore::swresource_constructor_args():
    sig = inspect.signature(MARTE::SW::ResourceCore::SwResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::processingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::ProcessingResource)


def test_marte::grm::processingresource_constructor_exists():
    assert callable(MARTE::GRM::ProcessingResource.__init__)


def test_marte::grm::processingresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::ProcessingResource.__init__)
    params = list(sig.parameters.keys())
    assert "speedFactor" in params, "Missing parameter 'speedFactor'"

def test_marte::grm::processingresource_has_speedFactor():
    assert hasattr(MARTE::GRM::ProcessingResource, "speedFactor")
    descriptor = None
    for klass in MARTE::GRM::ProcessingResource.__mro__:
        if "speedFactor" in klass.__dict__:
            descriptor = klass.__dict__["speedFactor"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::communicationendpoint_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::CommunicationEndPoint)


def test_marte::grm::communicationendpoint_constructor_exists():
    assert callable(MARTE::GRM::CommunicationEndPoint.__init__)


def test_marte::grm::communicationendpoint_constructor_args():
    sig = inspect.signature(MARTE::GRM::CommunicationEndPoint.__init__)
    params = list(sig.parameters.keys())
    assert "packetSize" in params, "Missing parameter 'packetSize'"

def test_marte::grm::communicationendpoint_has_packetSize():
    assert hasattr(MARTE::GRM::CommunicationEndPoint, "packetSize")
    descriptor = None
    for klass in MARTE::GRM::CommunicationEndPoint.__mro__:
        if "packetSize" in klass.__dict__:
            descriptor = klass.__dict__["packetSize"]
            break
    assert isinstance(descriptor, property)



def test_marte::pam::palogicalresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::PAM::PaLogicalResource)


def test_marte::pam::palogicalresource_constructor_exists():
    assert callable(MARTE::PAM::PaLogicalResource.__init__)


def test_marte::pam::palogicalresource_constructor_args():
    sig = inspect.signature(MARTE::PAM::PaLogicalResource.__init__)
    params = list(sig.parameters.keys())
    assert "poolSize" in params, "Missing parameter 'poolSize'"
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "utilization" in params, "Missing parameter 'utilization'"

def test_marte::pam::palogicalresource_has_poolSize():
    assert hasattr(MARTE::PAM::PaLogicalResource, "poolSize")
    descriptor = None
    for klass in MARTE::PAM::PaLogicalResource.__mro__:
        if "poolSize" in klass.__dict__:
            descriptor = klass.__dict__["poolSize"]
            break
    assert isinstance(descriptor, property)

def test_marte::pam::palogicalresource_has_throughput():
    assert hasattr(MARTE::PAM::PaLogicalResource, "throughput")
    descriptor = None
    for klass in MARTE::PAM::PaLogicalResource.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
            break
    assert isinstance(descriptor, property)

def test_marte::pam::palogicalresource_has_utilization():
    assert hasattr(MARTE::PAM::PaLogicalResource, "utilization")
    descriptor = None
    for klass in MARTE::PAM::PaLogicalResource.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::schedulableresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::SchedulableResource)


def test_marte::grm::schedulableresource_constructor_exists():
    assert callable(MARTE::GRM::SchedulableResource.__init__)


def test_marte::grm::schedulableresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::SchedulableResource.__init__)
    params = list(sig.parameters.keys())
    assert "schedParams" in params, "Missing parameter 'schedParams'"

def test_marte::grm::schedulableresource_has_schedParams():
    assert hasattr(MARTE::GRM::SchedulableResource, "schedParams")
    descriptor = None
    for klass in MARTE::GRM::SchedulableResource.__mro__:
        if "schedParams" in klass.__dict__:
            descriptor = klass.__dict__["schedParams"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::mutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::MutualExclusionResource)


def test_marte::grm::mutualexclusionresource_constructor_exists():
    assert callable(MARTE::GRM::MutualExclusionResource.__init__)


def test_marte::grm::mutualexclusionresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::MutualExclusionResource.__init__)
    params = list(sig.parameters.keys())
    assert "ceiling" in params, "Missing parameter 'ceiling'"
    assert "protectKind" in params, "Missing parameter 'protectKind'"
    assert "otherProtectProtocol" in params, "Missing parameter 'otherProtectProtocol'"

def test_marte::grm::mutualexclusionresource_has_ceiling():
    assert hasattr(MARTE::GRM::MutualExclusionResource, "ceiling")
    descriptor = None
    for klass in MARTE::GRM::MutualExclusionResource.__mro__:
        if "ceiling" in klass.__dict__:
            descriptor = klass.__dict__["ceiling"]
            break
    assert isinstance(descriptor, property)

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



def test_marte::grm::timingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::TimingResource)


def test_marte::grm::timingresource_constructor_exists():
    assert callable(MARTE::GRM::TimingResource.__init__)


def test_marte::grm::timingresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::TimingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::concurrencyresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::ConcurrencyResource)


def test_marte::grm::concurrencyresource_constructor_exists():
    assert callable(MARTE::GRM::ConcurrencyResource.__init__)


def test_marte::grm::concurrencyresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::ConcurrencyResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::synchronizationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::SynchronizationResource)


def test_marte::grm::synchronizationresource_constructor_exists():
    assert callable(MARTE::GRM::SynchronizationResource.__init__)


def test_marte::grm::synchronizationresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::SynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte::grm::scheduler_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::Scheduler)


def test_marte::grm::scheduler_constructor_exists():
    assert callable(MARTE::GRM::Scheduler.__init__)


def test_marte::grm::scheduler_constructor_args():
    sig = inspect.signature(MARTE::GRM::Scheduler.__init__)
    params = list(sig.parameters.keys())
    assert "otherSchedPolicy" in params, "Missing parameter 'otherSchedPolicy'"
    assert "isPreemptible" in params, "Missing parameter 'isPreemptible'"
    assert "schedule" in params, "Missing parameter 'schedule'"
    assert "schedPolicy" in params, "Missing parameter 'schedPolicy'"

def test_marte::grm::scheduler_has_otherSchedPolicy():
    assert hasattr(MARTE::GRM::Scheduler, "otherSchedPolicy")
    descriptor = None
    for klass in MARTE::GRM::Scheduler.__mro__:
        if "otherSchedPolicy" in klass.__dict__:
            descriptor = klass.__dict__["otherSchedPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::scheduler_has_isPreemptible():
    assert hasattr(MARTE::GRM::Scheduler, "isPreemptible")
    descriptor = None
    for klass in MARTE::GRM::Scheduler.__mro__:
        if "isPreemptible" in klass.__dict__:
            descriptor = klass.__dict__["isPreemptible"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::scheduler_has_schedule():
    assert hasattr(MARTE::GRM::Scheduler, "schedule")
    descriptor = None
    for klass in MARTE::GRM::Scheduler.__mro__:
        if "schedule" in klass.__dict__:
            descriptor = klass.__dict__["schedule"]
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



def test_marte::hwgeneral::hwresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::HwGeneral::HwResource)


def test_marte::hwgeneral::hwresource_constructor_exists():
    assert callable(MARTE::HwGeneral::HwResource.__init__)


def test_marte::hwgeneral::hwresource_constructor_args():
    sig = inspect.signature(MARTE::HwGeneral::HwResource.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_marte::hwgeneral::hwresource_has_description():
    assert hasattr(MARTE::HwGeneral::HwResource, "description")
    descriptor = None
    for klass in MARTE::HwGeneral::HwResource.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_marte::hwgeneral::hwresource_has_frequency():
    assert hasattr(MARTE::HwGeneral::HwResource, "frequency")
    descriptor = None
    for klass in MARTE::HwGeneral::HwResource.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)



def test_marte::grm::storageresource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::StorageResource)


def test_marte::grm::storageresource_constructor_exists():
    assert callable(MARTE::GRM::StorageResource.__init__)


def test_marte::grm::storageresource_constructor_args():
    sig = inspect.signature(MARTE::GRM::StorageResource.__init__)
    params = list(sig.parameters.keys())
    assert "elementSize" in params, "Missing parameter 'elementSize'"

def test_marte::grm::storageresource_has_elementSize():
    assert hasattr(MARTE::GRM::StorageResource, "elementSize")
    descriptor = None
    for klass in MARTE::GRM::StorageResource.__mro__:
        if "elementSize" in klass.__dict__:
            descriptor = klass.__dict__["elementSize"]
            break
    assert isinstance(descriptor, property)



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



def test_marte::grm::resource_is_not_abstract():
    assert not inspect.isabstract(MARTE::GRM::Resource)


def test_marte::grm::resource_constructor_exists():
    assert callable(MARTE::GRM::Resource.__init__)


def test_marte::grm::resource_constructor_args():
    sig = inspect.signature(MARTE::GRM::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "isProtected" in params, "Missing parameter 'isProtected'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "resMult" in params, "Missing parameter 'resMult'"

def test_marte::grm::resource_has_isProtected():
    assert hasattr(MARTE::GRM::Resource, "isProtected")
    descriptor = None
    for klass in MARTE::GRM::Resource.__mro__:
        if "isProtected" in klass.__dict__:
            descriptor = klass.__dict__["isProtected"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::resource_has_isActive():
    assert hasattr(MARTE::GRM::Resource, "isActive")
    descriptor = None
    for klass in MARTE::GRM::Resource.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_marte::grm::resource_has_resMult():
    assert hasattr(MARTE::GRM::Resource, "resMult")
    descriptor = None
    for klass in MARTE::GRM::Resource.__mro__:
        if "resMult" in klass.__dict__:
            descriptor = klass.__dict__["resMult"]
            break
    assert isinstance(descriptor, property)



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



def test_grm::marte::connectableelement_is_not_abstract():
    assert not inspect.isabstract(GRM::MARTE::ConnectableElement)


def test_grm::marte::connectableelement_constructor_exists():
    assert callable(GRM::MARTE::ConnectableElement.__init__)


def test_grm::marte::connectableelement_constructor_args():
    sig = inspect.signature(GRM::MARTE::ConnectableElement.__init__)
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



def test_time::marte::durationobservation_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::DurationObservation)


def test_time::marte::durationobservation_constructor_exists():
    assert callable(Time::MARTE::DurationObservation.__init__)


def test_time::marte::durationobservation_constructor_args():
    sig = inspect.signature(Time::MARTE::DurationObservation.__init__)
    params = list(sig.parameters.keys())



def test_time::marte::timeobservation_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::TimeObservation)


def test_time::marte::timeobservation_constructor_exists():
    assert callable(Time::MARTE::TimeObservation.__init__)


def test_time::marte::timeobservation_constructor_args():
    sig = inspect.signature(Time::MARTE::TimeObservation.__init__)
    params = list(sig.parameters.keys())



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



def test_marte::time::timedprocessing_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::TimedProcessing)


def test_marte::time::timedprocessing_constructor_exists():
    assert callable(MARTE::Time::TimedProcessing.__init__)


def test_marte::time::timedprocessing_constructor_args():
    sig = inspect.signature(MARTE::Time::TimedProcessing.__init__)
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



def test_time::marte::operation_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Operation)


def test_time::marte::operation_constructor_exists():
    assert callable(Time::MARTE::Operation.__init__)


def test_time::marte::operation_constructor_args():
    sig = inspect.signature(Time::MARTE::Operation.__init__)
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



def test_time::marte::event_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Event)


def test_time::marte::event_constructor_exists():
    assert callable(Time::MARTE::Event.__init__)


def test_time::marte::event_constructor_args():
    sig = inspect.signature(Time::MARTE::Event.__init__)
    params = list(sig.parameters.keys())



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



def test_time::marte::enumeration_is_not_abstract():
    assert not inspect.isabstract(Time::MARTE::Enumeration)


def test_time::marte::enumeration_constructor_exists():
    assert callable(Time::MARTE::Enumeration.__init__)


def test_time::marte::enumeration_constructor_args():
    sig = inspect.signature(Time::MARTE::Enumeration.__init__)
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



def test_marte::alloc::assign_is_not_abstract():
    assert not inspect.isabstract(MARTE::Alloc::Assign)


def test_marte::alloc::assign_constructor_exists():
    assert callable(MARTE::Alloc::Assign.__init__)


def test_marte::alloc::assign_constructor_args():
    sig = inspect.signature(MARTE::Alloc::Assign.__init__)
    params = list(sig.parameters.keys())
    assert "nature" in params, "Missing parameter 'nature'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte::alloc::assign_has_nature():
    assert hasattr(MARTE::Alloc::Assign, "nature")
    descriptor = None
    for klass in MARTE::Alloc::Assign.__mro__:
        if "nature" in klass.__dict__:
            descriptor = klass.__dict__["nature"]
            break
    assert isinstance(descriptor, property)

def test_marte::alloc::assign_has_kind():
    assert hasattr(MARTE::Alloc::Assign, "kind")
    descriptor = None
    for klass in MARTE::Alloc::Assign.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_nfps::nfpconstraint_is_not_abstract():
    assert not inspect.isabstract(NFPs::NfpConstraint)


def test_nfps::nfpconstraint_constructor_exists():
    assert callable(NFPs::NfpConstraint.__init__)


def test_nfps::nfpconstraint_constructor_args():
    sig = inspect.signature(NFPs::NfpConstraint.__init__)
    params = list(sig.parameters.keys())



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



def test_marte::time::clockconstraint_is_not_abstract():
    assert not inspect.isabstract(MARTE::Time::ClockConstraint)


def test_marte::time::clockconstraint_constructor_exists():
    assert callable(MARTE::Time::ClockConstraint.__init__)


def test_marte::time::clockconstraint_constructor_args():
    sig = inspect.signature(MARTE::Time::ClockConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "isPrecedenceBased" in params, "Missing parameter 'isPrecedenceBased'"
    assert "isChronometricBased" in params, "Missing parameter 'isChronometricBased'"
    assert "isCoincidenceBased" in params, "Missing parameter 'isCoincidenceBased'"

def test_marte::time::clockconstraint_has_isPrecedenceBased():
    assert hasattr(MARTE::Time::ClockConstraint, "isPrecedenceBased")
    descriptor = None
    for klass in MARTE::Time::ClockConstraint.__mro__:
        if "isPrecedenceBased" in klass.__dict__:
            descriptor = klass.__dict__["isPrecedenceBased"]
            break
    assert isinstance(descriptor, property)

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



def test_marte::alloc::allocate_is_not_abstract():
    assert not inspect.isabstract(MARTE::Alloc::Allocate)


def test_marte::alloc::allocate_constructor_exists():
    assert callable(MARTE::Alloc::Allocate.__init__)


def test_marte::alloc::allocate_constructor_args():
    sig = inspect.signature(MARTE::Alloc::Allocate.__init__)
    params = list(sig.parameters.keys())
    assert "nature" in params, "Missing parameter 'nature'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte::alloc::allocate_has_nature():
    assert hasattr(MARTE::Alloc::Allocate, "nature")
    descriptor = None
    for klass in MARTE::Alloc::Allocate.__mro__:
        if "nature" in klass.__dict__:
            descriptor = klass.__dict__["nature"]
            break
    assert isinstance(descriptor, property)

def test_marte::alloc::allocate_has_kind():
    assert hasattr(MARTE::Alloc::Allocate, "kind")
    descriptor = None
    for klass in MARTE::Alloc::Allocate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_marte::alloc::nfprefine_is_not_abstract():
    assert not inspect.isabstract(MARTE::Alloc::NfpRefine)


def test_marte::alloc::nfprefine_constructor_exists():
    assert callable(MARTE::Alloc::NfpRefine.__init__)


def test_marte::alloc::nfprefine_constructor_args():
    sig = inspect.signature(MARTE::Alloc::NfpRefine.__init__)
    params = list(sig.parameters.keys())



def test_alloc::allocated_is_not_abstract():
    assert not inspect.isabstract(Alloc::Allocated)


def test_alloc::allocated_constructor_exists():
    assert callable(Alloc::Allocated.__init__)


def test_alloc::allocated_constructor_args():
    sig = inspect.signature(Alloc::Allocated.__init__)
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
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_marte::alloc::allocateactivitygroup_has_isUnique():
    assert hasattr(MARTE::Alloc::AllocateActivityGroup, "isUnique")
    descriptor = None
    for klass in MARTE::Alloc::AllocateActivityGroup.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_alloc::marte::dependency_is_not_abstract():
    assert not inspect.isabstract(Alloc::MARTE::Dependency)


def test_alloc::marte::dependency_constructor_exists():
    assert callable(Alloc::MARTE::Dependency.__init__)


def test_alloc::marte::dependency_constructor_args():
    sig = inspect.signature(Alloc::MARTE::Dependency.__init__)
    params = list(sig.parameters.keys())



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
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte::alloc::allocated_has_kind():
    assert hasattr(MARTE::Alloc::Allocated, "kind")
    descriptor = None
    for klass in MARTE::Alloc::Allocated.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



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



def test_coreelements::marte::transition_is_not_abstract():
    assert not inspect.isabstract(CoreElements::MARTE::Transition)


def test_coreelements::marte::transition_constructor_exists():
    assert callable(CoreElements::MARTE::Transition.__init__)


def test_coreelements::marte::transition_constructor_args():
    sig = inspect.signature(CoreElements::MARTE::Transition.__init__)
    params = list(sig.parameters.keys())



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
    assert "baseExponent" in params, "Missing parameter 'baseExponent'"
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_marte::nfps::dimension_has_baseExponent():
    assert hasattr(MARTE::NFPs::Dimension, "baseExponent")
    descriptor = None
    for klass in MARTE::NFPs::Dimension.__mro__:
        if "baseExponent" in klass.__dict__:
            descriptor = klass.__dict__["baseExponent"]
            break
    assert isinstance(descriptor, property)

def test_marte::nfps::dimension_has_symbol():
    assert hasattr(MARTE::NFPs::Dimension, "symbol")
    descriptor = None
    for klass in MARTE::NFPs::Dimension.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



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
    assert "convOffset" in params, "Missing parameter 'convOffset'"

def test_marte::nfps::unit_has_convFactor():
    assert hasattr(MARTE::NFPs::Unit, "convFactor")
    descriptor = None
    for klass in MARTE::NFPs::Unit.__mro__:
        if "convFactor" in klass.__dict__:
            descriptor = klass.__dict__["convFactor"]
            break
    assert isinstance(descriptor, property)

def test_marte::nfps::unit_has_convOffset():
    assert hasattr(MARTE::NFPs::Unit, "convOffset")
    descriptor = None
    for klass in MARTE::NFPs::Unit.__mro__:
        if "convOffset" in klass.__dict__:
            descriptor = klass.__dict__["convOffset"]
            break
    assert isinstance(descriptor, property)



def test_nfps::marte::property_is_not_abstract():
    assert not inspect.isabstract(NFPs::MARTE::Property)


def test_nfps::marte::property_constructor_exists():
    assert callable(NFPs::MARTE::Property.__init__)


def test_nfps::marte::property_constructor_args():
    sig = inspect.signature(NFPs::MARTE::Property.__init__)
    params = list(sig.parameters.keys())

def test_cachetype_exists():
    # Check that the Enumeration exists
    assert CacheType is not None

def test_cachetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CacheType]
    expected_literals = [
        "unified",
        "data",
        "other",
        "undef",
        "instruction",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CacheType"

def test_concurrencykind_exists():
    # Check that the Enumeration exists
    assert ConcurrencyKind is not None

def test_concurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConcurrencyKind]
    expected_literals = [
        "writer",
        "parallel",
        "reader",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConcurrencyKind"

def test_callconcurrencykind_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyKind is not None

def test_callconcurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyKind]
    expected_literals = [
        "guarded",
        "sequential",
        "concurrent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyKind"

def test_clientserverkind_exists():
    # Check that the Enumeration exists
    assert ClientServerKind is not None

def test_clientserverkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClientServerKind]
    expected_literals = [
        "required",
        "proreq",
        "provided",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClientServerKind"

def test_messageresourcekind_exists():
    # Check that the Enumeration exists
    assert MessageResourceKind is not None

def test_messageresourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageResourceKind]
    expected_literals = [
        "MessageQueue",
        "Blackboard",
        "Undef",
        "Pipe",
        "Other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageResourceKind"

def test_portspecificationkind_exists():
    # Check that the Enumeration exists
    assert PortSpecificationKind is not None

def test_portspecificationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PortSpecificationKind]
    expected_literals = [
        "interfaceBased",
        "featureBased",
        "atomic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PortSpecificationKind"

def test_pld_class_exists():
    # Check that the Enumeration exists
    assert PLD_Class is not None

def test_pld_class_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PLD_Class]
    expected_literals = [
        "rowBased",
        "seaOfGates",
        "undef",
        "other",
        "hierarchicalPLD",
        "symetricalArray",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PLD_Class"

def test_writepolicy_exists():
    # Check that the Enumeration exists
    assert WritePolicy is not None

def test_writepolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WritePolicy]
    expected_literals = [
        "undef",
        "other",
        "writeBack",
        "writeThrough",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WritePolicy"

def test_laxitykind_exists():
    # Check that the Enumeration exists
    assert LaxityKind is not None

def test_laxitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LaxityKind]
    expected_literals = [
        "hard",
        "other",
        "soft",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LaxityKind"

def test_assignmentnature_exists():
    # Check that the Enumeration exists
    assert AssignmentNature is not None

def test_assignmentnature_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentNature]
    expected_literals = [
        "spatialDistribution",
        "timeScheduling",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentNature"

def test_concurrentaccessprotocolkind_exists():
    # Check that the Enumeration exists
    assert ConcurrentAccessProtocolKind is not None

def test_concurrentaccessprotocolkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConcurrentAccessProtocolKind]
    expected_literals = [
        "Other",
        "PIP",
        "PCP",
        "NoPreemption",
        "Undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConcurrentAccessProtocolKind"

def test_dummy_exists():
    # Check that the Enumeration exists
    assert dummy is not None

def test_dummy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in dummy]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in dummy"

def test_variabledirectionkind_exists():
    # Check that the Enumeration exists
    assert VariableDirectionKind is not None

def test_variabledirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableDirectionKind]
    expected_literals = [
        "in_",
        "inout",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariableDirectionKind"

def test_assignmentkind_exists():
    # Check that the Enumeration exists
    assert AssignmentKind is not None

def test_assignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentKind]
    expected_literals = [
        "hybrid",
        "behavioral",
        "structural",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentKind"

def test_componentkind_exists():
    # Check that the Enumeration exists
    assert ComponentKind is not None

def test_componentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentKind]
    expected_literals = [
        "other",
        "unit",
        "chip",
        "channel",
        "port",
        "undef",
        "card",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentKind"

def test_repl_policy_exists():
    # Check that the Enumeration exists
    assert Repl_Policy is not None

def test_repl_policy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Repl_Policy]
    expected_literals = [
        "FIFO",
        "undef",
        "random",
        "LRU",
        "other",
        "NFU",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Repl_Policy"

def test_queuepolicykind_exists():
    # Check that the Enumeration exists
    assert QueuePolicyKind is not None

def test_queuepolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QueuePolicyKind]
    expected_literals = [
        "Priority",
        "LIFO",
        "FIFO",
        "Other",
        "Undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QueuePolicyKind"

def test_rom_type_exists():
    # Check that the Enumeration exists
    assert ROM_Type is not None

def test_rom_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ROM_Type]
    expected_literals = [
        "Flash",
        "undef",
        "maskedROM",
        "EPROM",
        "EEPROM",
        "OTP_EPROM",
        "other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ROM_Type"

def test_notificationkind_exists():
    # Check that the Enumeration exists
    assert NotificationKind is not None

def test_notificationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NotificationKind]
    expected_literals = [
        "Memorized",
        "Undef",
        "Memoryless",
        "Bounded",
        "Other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NotificationKind"

def test_allocationkind_exists():
    # Check that the Enumeration exists
    assert AllocationKind is not None

def test_allocationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AllocationKind]
    expected_literals = [
        "structural",
        "behavioral",
        "hybrid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AllocationKind"

def test_executionkind_exists():
    # Check that the Enumeration exists
    assert ExecutionKind is not None

def test_executionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExecutionKind]
    expected_literals = [
        "remoteImmediate",
        "deferred",
        "localImmediate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExecutionKind"

def test_pld_technology_exists():
    # Check that the Enumeration exists
    assert PLD_Technology is not None

def test_pld_technology_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PLD_Technology]
    expected_literals = [
        "antifuse",
        "undef",
        "flash",
        "SRAM",
        "other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PLD_Technology"

def test_accesspolicykind_exists():
    # Check that the Enumeration exists
    assert AccessPolicyKind is not None

def test_accesspolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessPolicyKind]
    expected_literals = [
        "Other",
        "Read",
        "Write",
        "ReadWrite",
        "Undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessPolicyKind"

def test_allocationendkind_exists():
    # Check that the Enumeration exists
    assert AllocationEndKind is not None

def test_allocationendkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AllocationEndKind]
    expected_literals = [
        "both",
        "undef",
        "application",
        "executionPlatform",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AllocationEndKind"

def test_interruptkind_exists():
    # Check that the Enumeration exists
    assert InterruptKind is not None

def test_interruptkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InterruptKind]
    expected_literals = [
        "Other",
        "HardwareInterruption",
        "Undef",
        "ProgrammedException",
        "ProcessorDetectedException",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InterruptKind"

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

def test_componentstate_exists():
    # Check that the Enumeration exists
    assert ComponentState is not None

def test_componentstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentState]
    expected_literals = [
        "storage",
        "undef",
        "other",
        "operating",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentState"

def test_poolmgtpolicykind_exists():
    # Check that the Enumeration exists
    assert PoolMgtPolicyKind is not None

def test_poolmgtpolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PoolMgtPolicyKind]
    expected_literals = [
        "other",
        "exception",
        "infiniteWait",
        "dynamic",
        "timedWait",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PoolMgtPolicyKind"

def test_flowdirectionkind_exists():
    # Check that the Enumeration exists
    assert FlowDirectionKind is not None

def test_flowdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowDirectionKind]
    expected_literals = [
        "out",
        "inout",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlowDirectionKind"

def test_notificationresourcekind_exists():
    # Check that the Enumeration exists
    assert NotificationResourceKind is not None

def test_notificationresourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NotificationResourceKind]
    expected_literals = [
        "Undef",
        "Barrier",
        "Event",
        "Other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NotificationResourceKind"

def test_constraintkind_exists():
    # Check that the Enumeration exists
    assert ConstraintKind is not None

def test_constraintkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstraintKind]
    expected_literals = [
        "offered",
        "contract",
        "required",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstraintKind"

def test_isa_type_exists():
    # Check that the Enumeration exists
    assert ISA_Type is not None

def test_isa_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ISA_Type]
    expected_literals = [
        "other",
        "CISC",
        "SIMD",
        "VLIW",
        "RISC",
        "undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ISA_Type"

def test_mutualexclusionresourcekind_exists():
    # Check that the Enumeration exists
    assert MutualExclusionResourceKind is not None

def test_mutualexclusionresourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MutualExclusionResourceKind]
    expected_literals = [
        "Other",
        "BooleanSemaphore",
        "CountSemaphore",
        "Undef",
        "Mutex",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MutualExclusionResourceKind"

def test_optimallitycriterionkind_exists():
    # Check that the Enumeration exists
    assert OptimallityCriterionKind is not None

def test_optimallitycriterionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptimallityCriterionKind]
    expected_literals = [
        "meetHardDeadlines",
        "minimizedMeanTardiness",
        "other",
        "minimizeMissedDeadlines",
        "undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptimallityCriterionKind"

def test_synchronizationkind_exists():
    # Check that the Enumeration exists
    assert SynchronizationKind is not None

def test_synchronizationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SynchronizationKind]
    expected_literals = [
        "synchronous",
        "other",
        "rendezVous",
        "asynchronous",
        "delayedSynchronous",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SynchronizationKind"

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

def test_conditiontype_exists():
    # Check that the Enumeration exists
    assert ConditionType is not None

def test_conditiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionType]
    expected_literals = [
        "temperature",
        "humidity",
        "altitude",
        "undef",
        "shock",
        "vibration",
        "other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionType"


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
GQAM::MARTE::Behavior_strategy = st.builds(
    GQAM::MARTE::Behavior,
)
GCM::MARTE::BehavioralFeature_strategy = st.builds(
    GCM::MARTE::BehavioralFeature,
)
MARTE::GCM::ClientServerFeature_strategy = st.builds(
    MARTE::GCM::ClientServerFeature,
    kind=
        safe_text
)
MARTE::GCM::FlowSpecification_strategy = st.builds(
    MARTE::GCM::FlowSpecification,
)
MARTE::GCM::ClientServerSpecification_strategy = st.builds(
    MARTE::GCM::ClientServerSpecification,
)
GCM::ClientServerSpecification_strategy = st.builds(
    GCM::ClientServerSpecification,
)
GQAM::GaCommStep_strategy = st.builds(
    GQAM::GaCommStep,
)
PAM::PaStep_strategy = st.builds(
    PAM::PaStep,
)
MARTE::PAM::PaCommStep_strategy = st.builds(
    MARTE::PAM::PaCommStep,
)
PAM::MARTE::NamedElement_strategy = st.builds(
    PAM::MARTE::NamedElement,
)
MARTE::PAM::PaRunTInstance_strategy = st.builds(
    MARTE::PAM::PaRunTInstance,
    utilization=
        safe_text,
    poolSize=
        safe_text,
    unbddPool=
        safe_text,
    throughput=
        safe_text
)
GaExecHost_strategy = st.builds(
    GaExecHost,
)
MARTE::SAM::SaExecHost_strategy = st.builds(
    MARTE::SAM::SaExecHost,
    schSlack=
        safe_text,
    isSched=
        safe_text,
    ISRswitchT=
        safe_text,
    schedUtiliz=
        safe_text,
    ISRprioRange=
        safe_text
)
GaCommHost_strategy = st.builds(
    GaCommHost,
)
MARTE::SAM::SaCommHost_strategy = st.builds(
    MARTE::SAM::SaCommHost,
    isSched=
        safe_text,
    schSlack=
        safe_text
)
MutualExclusionResource_strategy = st.builds(
    MutualExclusionResource,
)
MARTE::SAM::SaSharedResource_strategy = st.builds(
    MARTE::SAM::SaSharedResource,
    releaseT=
        safe_text,
    capacity=
        safe_text,
    isConsum=
        safe_text,
    acquisT=
        safe_text,
    isPreemp=
        safe_text
)
SAM::SaSharedResource_strategy = st.builds(
    SAM::SaSharedResource,
)
SAM::MARTE::BehavioralFeature_strategy = st.builds(
    SAM::MARTE::BehavioralFeature,
)
MARTE::SAM::SaEndtoEndFlow_strategy = st.builds(
    MARTE::SAM::SaEndtoEndFlow,
    end2EndT=
        safe_text,
    schSlack=
        safe_text,
    end2EndD=
        safe_text,
    isSched=
        safe_text
)
GaAnalysisContext_strategy = st.builds(
    GaAnalysisContext,
)
MARTE::SAM::SaAnalysisContext_strategy = st.builds(
    MARTE::SAM::SaAnalysisContext,
    isSched=
        safe_text,
    optCriterion=
        safe_text
)
GQAM::MARTE::Classifier_strategy = st.builds(
    GQAM::MARTE::Classifier,
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
    context=
        safe_text
)
GaCommStep_strategy = st.builds(
    GaCommStep,
)
MARTE::SAM::SaCommStep_strategy = st.builds(
    MARTE::SAM::SaCommStep,
    deadline=
        safe_text,
    spareCap=
        safe_text,
    schSlack=
        safe_text
)
SAM::MARTE::NamedElement_strategy = st.builds(
    SAM::MARTE::NamedElement,
)
MARTE::GQAM::GaWorkloadBehavior_strategy = st.builds(
    MARTE::GQAM::GaWorkloadBehavior,
)
SchedulableResource_strategy = st.builds(
    SchedulableResource,
)
MARTE::GQAM::GaCommChannel_strategy = st.builds(
    MARTE::GQAM::GaCommChannel,
    utilization=
        safe_text,
    packetSize=
        safe_text
)
GaTimedObs_strategy = st.builds(
    GaTimedObs,
)
MARTE::SAM::SaSchedObs_strategy = st.builds(
    MARTE::SAM::SaSchedObs,
    suspentions=
        safe_text,
    overlaps=
        safe_text,
    blockT=
        safe_text
)
MARTE::GQAM::GaLatencyObs_strategy = st.builds(
    MARTE::GQAM::GaLatencyObs,
    utility=
        safe_text,
    latency=
        safe_text,
    miss=
        safe_text,
    maxJitter=
        safe_text
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
MARTE::PAM::PaResPassStep_strategy = st.builds(
    MARTE::PAM::PaResPassStep,
    resUnits=
        safe_text
)
MARTE::GQAM::GaCommStep_strategy = st.builds(
    MARTE::GQAM::GaCommStep,
)
MARTE::GQAM::GaRelStep_strategy = st.builds(
    MARTE::GQAM::GaRelStep,
    resUnits=
        safe_text
)
MARTE::SAM::SaStep_strategy = st.builds(
    MARTE::SAM::SaStep,
    schSlack=
        safe_text,
    selfSuspensionBlocking=
        safe_text,
    deadline=
        safe_text,
    spareCap=
        safe_text,
    readyT=
        safe_text,
    numberSelfSuspensions=
        safe_text,
    nonpreemptionBlocking=
        safe_text,
    preemptT=
        safe_text
)
MARTE::GQAM::GaAcqStep_strategy = st.builds(
    MARTE::GQAM::GaAcqStep,
    resUnits=
        safe_text
)
MARTE::PAM::PaStep_strategy = st.builds(
    MARTE::PAM::PaStep,
    noSync=
        safe_text,
    extOpCount=
        safe_text,
    behavCount=
        safe_text,
    extOpDemand=
        safe_text
)
MARTE::GQAM::GaRequestedService_strategy = st.builds(
    MARTE::GQAM::GaRequestedService,
)
GQAM::GaExecHost_strategy = st.builds(
    GQAM::GaExecHost,
)
GaScenario_strategy = st.builds(
    GaScenario,
)
MARTE::GQAM::GaStep_strategy = st.builds(
    MARTE::GQAM::GaStep,
    blockT=
        safe_text,
    selfDelay=
        safe_text,
    prob=
        safe_text,
    isAtomic=
        safe_text,
    rep=
        safe_text,
    servCount=
        safe_text,
    priority=
        safe_text
)
GQAM::GaTimedObs_strategy = st.builds(
    GQAM::GaTimedObs,
)
GQAM::GaRequestedService_strategy = st.builds(
    GQAM::GaRequestedService,
)
MARTE::PAM::PaRequestedStep_strategy = st.builds(
    MARTE::PAM::PaRequestedStep,
)
GQAM::GaWorkloadEvent_strategy = st.builds(
    GQAM::GaWorkloadEvent,
)
Time::TimedProcessing_strategy = st.builds(
    Time::TimedProcessing,
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
    pattern=
        safe_text
)
GQAM::MARTE::NamedElement_strategy = st.builds(
    GQAM::MARTE::NamedElement,
)
GQAM::GaStep_strategy = st.builds(
    GQAM::GaStep,
)
MARTE::GQAM::GaWorkloadGenerator_strategy = st.builds(
    MARTE::GQAM::GaWorkloadGenerator,
    pop=
        safe_text
)
MARTE::GCM::GCMInvocatingBehavior_strategy = st.builds(
    MARTE::GCM::GCMInvocatingBehavior,
)
GCM::MARTE::Behavior_strategy = st.builds(
    GCM::MARTE::Behavior,
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
MARTE::GQAM::GaEventTrace_strategy = st.builds(
    MARTE::GQAM::GaEventTrace,
    content=
        safe_text,
    format=
        safe_text,
    location=
        safe_text
)
MARTE::NFPs::Nfp_strategy = st.builds(
    MARTE::NFPs::Nfp,
)
GCM::MARTE::Interface_strategy = st.builds(
    GCM::MARTE::Interface,
)
MARTE::GCM::ClientServerPort_strategy = st.builds(
    MARTE::GCM::ClientServerPort,
    kind=
        safe_text,
    specificationKind=
        safe_text
)
GCM::MARTE::Port_strategy = st.builds(
    GCM::MARTE::Port,
)
MARTE::GCM::FlowPort_strategy = st.builds(
    MARTE::GCM::FlowPort,
    direction=
        safe_text,
    isAtomic=
        safe_text
)
GCM::MARTE::Trigger_strategy = st.builds(
    GCM::MARTE::Trigger,
)
MARTE::GCM::GCMTrigger_strategy = st.builds(
    MARTE::GCM::GCMTrigger,
)
MARTE::GCM::FlowProperty_strategy = st.builds(
    MARTE::GCM::FlowProperty,
    direction=
        safe_text
)
SW::Interaction::SwSynchronizationResource_strategy = st.builds(
    SW::Interaction::SwSynchronizationResource,
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
GCM::MARTE::Property_strategy = st.builds(
    GCM::MARTE::Property,
)
SW::Interaction::MARTE::BehavioralFeature_strategy = st.builds(
    SW::Interaction::MARTE::BehavioralFeature,
)
SwCommunicationResource_strategy = st.builds(
    SwCommunicationResource,
)
MARTE::SW::Interaction::MessageComResource_strategy = st.builds(
    MARTE::SW::Interaction::MessageComResource,
    messageQueuePolicy=
        safe_text,
    mechanism=
        safe_text,
    isFixedMessageSize=
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
    kind=
        safe_text,
    isMaskable=
        safe_text
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
    isIntraMemoryPartitionInteraction=
        st.booleans(),
    waitingQueuePolicy=
        safe_text
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
    accessPolicy=
        safe_text,
    isBuffered=
        safe_text
)
MARTE::SW::Concurrency::SwConcurrentResource_strategy = st.builds(
    MARTE::SW::Concurrency::SwConcurrentResource,
    type=
        safe_text,
    activationCapacity=
        safe_text
)
SW::Concurrency::MARTE::BehavioralFeature_strategy = st.builds(
    SW::Concurrency::MARTE::BehavioralFeature,
)
SW::ResourceCore::MARTE::Property_strategy = st.builds(
    SW::ResourceCore::MARTE::Property,
)
SW::ResourceCore::MARTE::BehavioralFeature_strategy = st.builds(
    SW::ResourceCore::MARTE::BehavioralFeature,
)
SW::ResourceCore::MARTE::TypedElement_strategy = st.builds(
    SW::ResourceCore::MARTE::TypedElement,
)
SW::Concurrency::MARTE::TypedElement_strategy = st.builds(
    SW::Concurrency::MARTE::TypedElement,
)
HwComponent_strategy = st.builds(
    HwComponent,
)
MARTE::HwPower::HwCoolingSupply_strategy = st.builds(
    MARTE::HwPower::HwCoolingSupply,
    coolingPower=
        safe_text
)
MARTE::HwPower::HwPowerSupply_strategy = st.builds(
    MARTE::HwPower::HwPowerSupply,
    capacity=
        safe_text,
    suppliedPower=
        safe_text
)
HwLayout::HwComponent_strategy = st.builds(
    HwLayout::HwComponent,
)
HwCommunication::HwEndPoint_strategy = st.builds(
    HwCommunication::HwEndPoint,
)
HwGeneral::HwResourceService_strategy = st.builds(
    HwGeneral::HwResourceService,
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
HwTiming::HwClock_strategy = st.builds(
    HwTiming::HwClock,
)
HwTimingResource_strategy = st.builds(
    HwTimingResource,
)
MARTE::HwTiming::HwTimer_strategy = st.builds(
    MARTE::HwTiming::HwTimer,
    counterWidth=
        safe_text,
    nbCounters=
        safe_text
)
MARTE::HwTiming::HwClock_strategy = st.builds(
    MARTE::HwTiming::HwClock,
)
GRM::TimingResource_strategy = st.builds(
    GRM::TimingResource,
)
HwDevice_strategy = st.builds(
    HwDevice,
)
MARTE::HwDevice::HwSupport_strategy = st.builds(
    MARTE::HwDevice::HwSupport,
)
MARTE::HwDevice::HwI::O_strategy = st.builds(
    MARTE::HwDevice::HwI::O,
)
GRM::DeviceResource_strategy = st.builds(
    GRM::DeviceResource,
)
HwMemory_strategy = st.builds(
    HwMemory,
)
MARTE::HwMemory::HwCache_strategy = st.builds(
    MARTE::HwMemory::HwCache,
    writePolicy=
        safe_text,
    structure=
        safe_text,
    repl_Policy=
        safe_text,
    level=
        safe_text,
    type=
        safe_text
)
MARTE::HwMemory::HwDrive_strategy = st.builds(
    MARTE::HwMemory::HwDrive,
    sectorSize=
        safe_text
)
MARTE::HwMemory::HwROM_strategy = st.builds(
    MARTE::HwMemory::HwROM,
    type=
        safe_text,
    organization=
        safe_text
)
MARTE::HwMemory::HwRAM_strategy = st.builds(
    MARTE::HwMemory::HwRAM,
    isNonVolatile=
        safe_text,
    repl_Policy=
        safe_text,
    writePolicy=
        safe_text,
    organization=
        safe_text,
    isSynchronous=
        safe_text,
    isStatic=
        safe_text
)
HwComputing::HwProcessor_strategy = st.builds(
    HwComputing::HwProcessor,
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
GRM::CommunicationEndPoint_strategy = st.builds(
    GRM::CommunicationEndPoint,
)
HwMedia_strategy = st.builds(
    HwMedia,
)
MARTE::HwCommunication::HwBridge_strategy = st.builds(
    MARTE::HwCommunication::HwBridge,
)
MARTE::HwCommunication::HwBus_strategy = st.builds(
    MARTE::HwCommunication::HwBus,
    isSynchronous=
        safe_text,
    isSerial=
        safe_text,
    adressWidth=
        safe_text,
    wordWidth=
        safe_text
)
HwCommunication::HwArbiter_strategy = st.builds(
    HwCommunication::HwArbiter,
)
MARTE::HwStorageManager::HwDMA_strategy = st.builds(
    MARTE::HwStorageManager::HwDMA,
    transferWidth=
        safe_text,
    nbChannels=
        safe_text
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
    bandWidth=
        safe_text
)
HwStorageManager_strategy = st.builds(
    HwStorageManager,
)
MARTE::HwStorageManager::HwMMU_strategy = st.builds(
    MARTE::HwStorageManager::HwMMU,
    virtualAddrSpace=
        safe_text,
    memoryProtection=
        safe_text,
    nbEntries=
        safe_text,
    physicalAddrSpace=
        safe_text
)
HwComputing::HwComputingResource_strategy = st.builds(
    HwComputing::HwComputingResource,
)
HwMemory::HwRAM_strategy = st.builds(
    HwMemory::HwRAM,
)
HwResource_strategy = st.builds(
    HwResource,
)
MARTE::HwCommunication::HwCommunicationResource_strategy = st.builds(
    MARTE::HwCommunication::HwCommunicationResource,
)
MARTE::HwLayout::HwComponent_strategy = st.builds(
    MARTE::HwLayout::HwComponent,
    grid=
        safe_text,
    position=
        safe_text,
    dimensions=
        safe_text,
    r_Conditions=
        safe_text,
    weight=
        safe_text,
    price=
        safe_text,
    nbPins=
        safe_text,
    staticConsumption=
        safe_text,
    kind=
        safe_text,
    area=
        safe_text,
    staticDissipation=
        safe_text
)
MARTE::HwComputing::HwBranchPredictor_strategy = st.builds(
    MARTE::HwComputing::HwBranchPredictor,
)
MARTE::HwComputing::HwISA_strategy = st.builds(
    MARTE::HwComputing::HwISA,
    type=
        safe_text,
    family=
        safe_text,
    inst_Width=
        safe_text
)
HwGeneral::HwResource_strategy = st.builds(
    HwGeneral::HwResource,
)
MARTE::HwStorageManager::HwStorageManager_strategy = st.builds(
    MARTE::HwStorageManager::HwStorageManager,
)
MARTE::HwTiming::HwTimingResource_strategy = st.builds(
    MARTE::HwTiming::HwTimingResource,
)
MARTE::HwDevice::HwDevice_strategy = st.builds(
    MARTE::HwDevice::HwDevice,
)
MARTE::HwMemory::HwMemory_strategy = st.builds(
    MARTE::HwMemory::HwMemory,
    adressSize=
        safe_text,
    throughput=
        safe_text,
    timings=
        safe_text,
    memorySize=
        safe_text
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
HwMemory::HwCache_strategy = st.builds(
    HwMemory::HwCache,
)
HwComputing::HwBranchPredictor_strategy = st.builds(
    HwComputing::HwBranchPredictor,
)
HwComputing::HwISA_strategy = st.builds(
    HwComputing::HwISA,
)
HwComputingResource_strategy = st.builds(
    HwComputingResource,
)
MARTE::HwComputing::HwPLD_strategy = st.builds(
    MARTE::HwComputing::HwPLD,
    ndLUT_Inputs=
        safe_text,
    technology=
        safe_text,
    nbFlipFlops=
        safe_text,
    organization=
        safe_text,
    nbLUTs=
        safe_text
)
MARTE::HwComputing::HwASIC_strategy = st.builds(
    MARTE::HwComputing::HwASIC,
)
MARTE::HwComputing::HwProcessor_strategy = st.builds(
    MARTE::HwComputing::HwProcessor,
    architecture=
        safe_text,
    nbPipelines=
        safe_text,
    nbCores=
        safe_text,
    nbALUs=
        safe_text,
    mips=
        safe_text,
    nbFPUs=
        safe_text,
    ipc=
        safe_text,
    nbStages=
        safe_text
)
HwStorageManager::HwMMU_strategy = st.builds(
    HwStorageManager::HwMMU,
)
MARTE::HLAM::RtService_strategy = st.builds(
    MARTE::HLAM::RtService,
    exeKind=
        safe_text,
    isAtomic=
        safe_text,
    concPolicy=
        safe_text,
    synchKind=
        safe_text
)
MARTE::HLAM::RtAction_strategy = st.builds(
    MARTE::HLAM::RtAction,
    isAtomic=
        safe_text,
    msgSize=
        safe_text,
    synchKind=
        safe_text
)
HLAM::MARTE::Comment_strategy = st.builds(
    HLAM::MARTE::Comment,
)
Time::TimedInstantObservation_strategy = st.builds(
    Time::TimedInstantObservation,
)
MARTE::HLAM::RtSpecification_strategy = st.builds(
    MARTE::HLAM::RtSpecification,
    boundDl=
        safe_text,
    relDl=
        safe_text,
    utility=
        safe_text,
    rdTime=
        safe_text,
    priority=
        safe_text,
    absDl=
        safe_text,
    occKind=
        safe_text,
    miss=
        safe_text
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
    memorySize=
        safe_text,
    concPolicy=
        safe_text
)
HLAM::MARTE::Operation_strategy = st.builds(
    HLAM::MARTE::Operation,
)
HLAM::MARTE::Behavior_strategy = st.builds(
    HLAM::MARTE::Behavior,
)
MARTE::HLAM::RtUnit_strategy = st.builds(
    MARTE::HLAM::RtUnit,
    msgMaxSize=
        safe_text,
    queueSchedPolicy=
        safe_text,
    memorySize=
        safe_text,
    isMain=
        safe_text,
    queueSize=
        safe_text,
    srPoolPolicy=
        safe_text,
    srPoolSize=
        safe_text,
    isDynamic=
        safe_text,
    srPoolWaitingTime=
        safe_text
)
MARTE::DataTypes::TupleType_strategy = st.builds(
    MARTE::DataTypes::TupleType,
)
MARTE::DataTypes::ChoiceType_strategy = st.builds(
    MARTE::DataTypes::ChoiceType,
)
MARTE::DataTypes::CollectionType_strategy = st.builds(
    MARTE::DataTypes::CollectionType,
)
HLAM::MARTE::BehavioredClassifier_strategy = st.builds(
    HLAM::MARTE::BehavioredClassifier,
)
MARTE::DataTypes::IntervalType_strategy = st.builds(
    MARTE::DataTypes::IntervalType,
)
DataTypes::MARTE::DataType_strategy = st.builds(
    DataTypes::MARTE::DataType,
)
MARTE::DataTypes::BoundedSubtype_strategy = st.builds(
    MARTE::DataTypes::BoundedSubtype,
    isMaxOpen=
        st.booleans(),
    maxValue=
        safe_text,
    minValue=
        safe_text,
    isMinOpen=
        st.booleans()
)
Operators::MARTE::Behavior_strategy = st.builds(
    Operators::MARTE::Behavior,
)
MARTE::Operators::Operator_strategy = st.builds(
    MARTE::Operators::Operator,
    symbol=
        safe_text,
    arity=
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
    shape=
        safe_text
)
DataTypes::MARTE::Property_strategy = st.builds(
    DataTypes::MARTE::Property,
)
Allocate_strategy = st.builds(
    Allocate,
)
MARTE::SW::Concurrency::EntryPoint_strategy = st.builds(
    MARTE::SW::Concurrency::EntryPoint,
    isReentrant=
        safe_text
)
MARTE::RSM::Distribute_strategy = st.builds(
    MARTE::RSM::Distribute,
    repetitionSpace=
        safe_text,
    fromTiler=
        safe_text,
    toTiler=
        safe_text,
    patternShape=
        safe_text
)
LinkTopology_strategy = st.builds(
    LinkTopology,
)
MARTE::RSM::Reshape_strategy = st.builds(
    MARTE::RSM::Reshape,
    patternShape=
        safe_text,
    repetitonShape=
        safe_text
)
MARTE::RSM::InterRepetition_strategy = st.builds(
    MARTE::RSM::InterRepetition,
    repetitionShapeDependence=
        safe_text,
    isModulo=
        safe_text
)
MARTE::RSM::Tiler_strategy = st.builds(
    MARTE::RSM::Tiler,
    fitting=
        safe_text,
    tiler=
        safe_text,
    paving=
        safe_text,
    origin=
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
GRM::ResourceUsage_strategy = st.builds(
    GRM::ResourceUsage,
)
MARTE::GQAM::GaScenario_strategy = st.builds(
    MARTE::GQAM::GaScenario,
    utilizationOnHost=
        safe_text,
    interOccT=
        safe_text,
    respT=
        safe_text,
    utilization=
        safe_text,
    hostDemand=
        safe_text,
    hostDemandOps=
        safe_text,
    throughput=
        safe_text
)
GRM::MARTE::NamedElement_strategy = st.builds(
    GRM::MARTE::NamedElement,
)
RSM::MARTE::ConnectorEnd_strategy = st.builds(
    RSM::MARTE::ConnectorEnd,
)
GrService_strategy = st.builds(
    GrService,
)
MARTE::HwGeneral::HwResourceService_strategy = st.builds(
    MARTE::HwGeneral::HwResourceService,
    dissipation=
        safe_text,
    consumption=
        safe_text
)
MARTE::GRM::Acquire_strategy = st.builds(
    MARTE::GRM::Acquire,
    isBlocking=
        safe_text
)
MARTE::SW::ResourceCore::SwAccessService_strategy = st.builds(
    MARTE::SW::ResourceCore::SwAccessService,
    isModifier=
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
TimingResource_strategy = st.builds(
    TimingResource,
)
MARTE::GRM::TimerResource_strategy = st.builds(
    MARTE::GRM::TimerResource,
    isPeriodic=
        safe_text,
    duration=
        safe_text
)
MARTE::GRM::ClockResource_strategy = st.builds(
    MARTE::GRM::ClockResource,
)
MARTE::GRM::ResourceUsage_strategy = st.builds(
    MARTE::GRM::ResourceUsage,
    powerPeak=
        safe_text,
    execTime=
        safe_text,
    energy=
        safe_text,
    usedMemory=
        safe_text,
    allocatedMemory=
        safe_text,
    msgSize=
        safe_text
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
ProcessingResource_strategy = st.builds(
    ProcessingResource,
)
MARTE::GRM::DeviceResource_strategy = st.builds(
    MARTE::GRM::DeviceResource,
)
MARTE::GRM::CommunicationMedia_strategy = st.builds(
    MARTE::GRM::CommunicationMedia,
    capacity=
        safe_text,
    transmMode=
        safe_text,
    blockT=
        safe_text,
    elementSize=
        safe_text,
    packetT=
        safe_text
)
MARTE::GRM::ComputingResource_strategy = st.builds(
    MARTE::GRM::ComputingResource,
)
GRM::Scheduler_strategy = st.builds(
    GRM::Scheduler,
)
MARTE::GQAM::GaCommHost_strategy = st.builds(
    MARTE::GQAM::GaCommHost,
    throughput=
        safe_text,
    utilization=
        safe_text
)
GRM::SchedulableResource_strategy = st.builds(
    GRM::SchedulableResource,
)
MARTE::SW::Concurrency::SwSchedulableResource_strategy = st.builds(
    MARTE::SW::Concurrency::SwSchedulableResource,
    isStaticSchedulingFeature=
        safe_text,
    isPreemptable=
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
    throughput=
        safe_text,
    schedPriRange=
        safe_text,
    cntxtSwT=
        safe_text,
    clockOvh=
        safe_text,
    utilization=
        safe_text,
    memSize=
        safe_text,
    commTxOvh=
        safe_text,
    commRcvOvh=
        safe_text
)
MARTE::HwComputing::HwComputingResource_strategy = st.builds(
    MARTE::HwComputing::HwComputingResource,
    op_Frequencies=
        safe_text
)
GRM::ProcessingResource_strategy = st.builds(
    GRM::ProcessingResource,
)
Resource_strategy = st.builds(
    Resource,
)
MARTE::SW::ResourceCore::SwResource_strategy = st.builds(
    MARTE::SW::ResourceCore::SwResource,
)
MARTE::GRM::ProcessingResource_strategy = st.builds(
    MARTE::GRM::ProcessingResource,
    speedFactor=
        safe_text
)
MARTE::GRM::CommunicationEndPoint_strategy = st.builds(
    MARTE::GRM::CommunicationEndPoint,
    packetSize=
        safe_text
)
MARTE::PAM::PaLogicalResource_strategy = st.builds(
    MARTE::PAM::PaLogicalResource,
    poolSize=
        safe_text,
    throughput=
        safe_text,
    utilization=
        safe_text
)
MARTE::GRM::SchedulableResource_strategy = st.builds(
    MARTE::GRM::SchedulableResource,
    schedParams=
        safe_text
)
MARTE::GRM::MutualExclusionResource_strategy = st.builds(
    MARTE::GRM::MutualExclusionResource,
    ceiling=
        safe_text,
    protectKind=
        safe_text,
    otherProtectProtocol=
        safe_text
)
MARTE::GRM::TimingResource_strategy = st.builds(
    MARTE::GRM::TimingResource,
)
MARTE::GRM::ConcurrencyResource_strategy = st.builds(
    MARTE::GRM::ConcurrencyResource,
)
MARTE::GRM::SynchronizationResource_strategy = st.builds(
    MARTE::GRM::SynchronizationResource,
)
MARTE::GRM::Scheduler_strategy = st.builds(
    MARTE::GRM::Scheduler,
    otherSchedPolicy=
        safe_text,
    isPreemptible=
        safe_text,
    schedule=
        safe_text,
    schedPolicy=
        safe_text
)
MARTE::HwGeneral::HwResource_strategy = st.builds(
    MARTE::HwGeneral::HwResource,
    description=
        safe_text,
    frequency=
        safe_text
)
MARTE::GRM::StorageResource_strategy = st.builds(
    MARTE::GRM::StorageResource,
    elementSize=
        safe_text
)
GRM::MARTE::Lifeline_strategy = st.builds(
    GRM::MARTE::Lifeline,
)
GRM::MARTE::Classifier_strategy = st.builds(
    GRM::MARTE::Classifier,
)
GRM::MARTE::InstanceSpecification_strategy = st.builds(
    GRM::MARTE::InstanceSpecification,
)
GRM::MARTE::Property_strategy = st.builds(
    GRM::MARTE::Property,
)
MARTE::GRM::Resource_strategy = st.builds(
    MARTE::GRM::Resource,
    isProtected=
        safe_text,
    isActive=
        safe_text,
    resMult=
        safe_text
)
Time::MARTE::Message_strategy = st.builds(
    Time::MARTE::Message,
)
Time::MARTE::Behavior_strategy = st.builds(
    Time::MARTE::Behavior,
)
GRM::MARTE::ConnectableElement_strategy = st.builds(
    GRM::MARTE::ConnectableElement,
)
Time::MARTE::Action_strategy = st.builds(
    Time::MARTE::Action,
)
Time::MARTE::TimeEvent_strategy = st.builds(
    Time::MARTE::TimeEvent,
)
Time::MARTE::DurationObservation_strategy = st.builds(
    Time::MARTE::DurationObservation,
)
Time::MARTE::TimeObservation_strategy = st.builds(
    Time::MARTE::TimeObservation,
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
MARTE::Time::TimedDurationObservation_strategy = st.builds(
    MARTE::Time::TimedDurationObservation,
    obsKind=
        safe_text
)
MARTE::Time::TimedEvent_strategy = st.builds(
    MARTE::Time::TimedEvent,
    repetition=
        safe_text
)
MARTE::Time::TimedProcessing_strategy = st.builds(
    MARTE::Time::TimedProcessing,
)
MARTE::Time::TimedInstantObservation_strategy = st.builds(
    MARTE::Time::TimedInstantObservation,
    obsKind=
        safe_text
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
Time::MARTE::Operation_strategy = st.builds(
    Time::MARTE::Operation,
)
MARTE::Time::ClockType_strategy = st.builds(
    MARTE::Time::ClockType,
    isLogical=
        safe_text,
    nature=
        safe_text
)
Time::MARTE::Event_strategy = st.builds(
    Time::MARTE::Event,
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
Time::MARTE::Enumeration_strategy = st.builds(
    Time::MARTE::Enumeration,
)
Alloc::MARTE::Comment_strategy = st.builds(
    Alloc::MARTE::Comment,
)
Alloc::MARTE::Element_strategy = st.builds(
    Alloc::MARTE::Element,
)
MARTE::Alloc::Assign_strategy = st.builds(
    MARTE::Alloc::Assign,
    nature=
        safe_text,
    kind=
        safe_text
)
NFPs::NfpConstraint_strategy = st.builds(
    NFPs::NfpConstraint,
)
MARTE::Time::TimedConstraint_strategy = st.builds(
    MARTE::Time::TimedConstraint,
    interpretation=
        safe_text
)
MARTE::Time::ClockConstraint_strategy = st.builds(
    MARTE::Time::ClockConstraint,
    isPrecedenceBased=
        st.booleans(),
    isChronometricBased=
        safe_text,
    isCoincidenceBased=
        safe_text
)
MARTE::Alloc::Allocate_strategy = st.builds(
    MARTE::Alloc::Allocate,
    nature=
        safe_text,
    kind=
        safe_text
)
MARTE::Alloc::NfpRefine_strategy = st.builds(
    MARTE::Alloc::NfpRefine,
)
Alloc::Allocated_strategy = st.builds(
    Alloc::Allocated,
)
Alloc::MARTE::ActivityPartition_strategy = st.builds(
    Alloc::MARTE::ActivityPartition,
)
MARTE::Alloc::AllocateActivityGroup_strategy = st.builds(
    MARTE::Alloc::AllocateActivityGroup,
    isUnique=
        safe_text
)
Alloc::MARTE::Dependency_strategy = st.builds(
    Alloc::MARTE::Dependency,
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
Alloc::MARTE::NamedElement_strategy = st.builds(
    Alloc::MARTE::NamedElement,
)
MARTE::Alloc::Allocated_strategy = st.builds(
    MARTE::Alloc::Allocated,
    kind=
        safe_text
)
CoreElements::MARTE::State_strategy = st.builds(
    CoreElements::MARTE::State,
)
MARTE::CoreElements::Mode_strategy = st.builds(
    MARTE::CoreElements::Mode,
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
CoreElements::MARTE::Transition_strategy = st.builds(
    CoreElements::MARTE::Transition,
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
    baseExponent=
        st.integers(),
    symbol=
        safe_text
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
NFPs::Unit_strategy = st.builds(
    NFPs::Unit,
)
MARTE::NFPs::Unit_strategy = st.builds(
    MARTE::NFPs::Unit,
    convFactor=
        safe_text,
    convOffset=
        safe_text
)
NFPs::MARTE::Property_strategy = st.builds(
    NFPs::MARTE::Property,
)

@given(instance=GQAM::MARTE::Behavior_strategy)
@settings(max_examples=50)
def test_gqam::marte::behavior_instantiation(instance):
    assert isinstance(instance, GQAM::MARTE::Behavior)

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

@given(instance=MARTE::GCM::FlowSpecification_strategy)
@settings(max_examples=50)
def test_marte::gcm::flowspecification_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::FlowSpecification)

@given(instance=MARTE::GCM::ClientServerSpecification_strategy)
@settings(max_examples=50)
def test_marte::gcm::clientserverspecification_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::ClientServerSpecification)

@given(instance=GCM::ClientServerSpecification_strategy)
@settings(max_examples=50)
def test_gcm::clientserverspecification_instantiation(instance):
    assert isinstance(instance, GCM::ClientServerSpecification)

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

@given(instance=PAM::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_pam::marte::namedelement_instantiation(instance):
    assert isinstance(instance, PAM::MARTE::NamedElement)

@given(instance=MARTE::PAM::PaRunTInstance_strategy)
@settings(max_examples=50)
def test_marte::pam::paruntinstance_instantiation(instance):
    assert isinstance(instance, MARTE::PAM::PaRunTInstance)

@given(instance=MARTE::PAM::PaRunTInstance_strategy)
def test_marte::pam::paruntinstance_utilization_type(instance):
    assert isinstance(instance.utilization, str)


@given(instance=MARTE::PAM::PaRunTInstance_strategy)
def test_marte::pam::paruntinstance_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original

@given(instance=MARTE::PAM::PaRunTInstance_strategy)
def test_marte::pam::paruntinstance_poolSize_type(instance):
    assert isinstance(instance.poolSize, str)


@given(instance=MARTE::PAM::PaRunTInstance_strategy)
def test_marte::pam::paruntinstance_poolSize_setter(instance):
    original = instance.poolSize
    instance.poolSize = original
    assert instance.poolSize == original

@given(instance=MARTE::PAM::PaRunTInstance_strategy)
def test_marte::pam::paruntinstance_unbddPool_type(instance):
    assert isinstance(instance.unbddPool, str)


@given(instance=MARTE::PAM::PaRunTInstance_strategy)
def test_marte::pam::paruntinstance_unbddPool_setter(instance):
    original = instance.unbddPool
    instance.unbddPool = original
    assert instance.unbddPool == original

@given(instance=MARTE::PAM::PaRunTInstance_strategy)
def test_marte::pam::paruntinstance_throughput_type(instance):
    assert isinstance(instance.throughput, str)


@given(instance=MARTE::PAM::PaRunTInstance_strategy)
def test_marte::pam::paruntinstance_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original

@given(instance=GaExecHost_strategy)
@settings(max_examples=50)
def test_gaexechost_instantiation(instance):
    assert isinstance(instance, GaExecHost)

@given(instance=MARTE::SAM::SaExecHost_strategy)
@settings(max_examples=50)
def test_marte::sam::saexechost_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaExecHost)

@given(instance=MARTE::SAM::SaExecHost_strategy)
def test_marte::sam::saexechost_schSlack_type(instance):
    assert isinstance(instance.schSlack, str)


@given(instance=MARTE::SAM::SaExecHost_strategy)
def test_marte::sam::saexechost_schSlack_setter(instance):
    original = instance.schSlack
    instance.schSlack = original
    assert instance.schSlack == original

@given(instance=MARTE::SAM::SaExecHost_strategy)
def test_marte::sam::saexechost_isSched_type(instance):
    assert isinstance(instance.isSched, str)


@given(instance=MARTE::SAM::SaExecHost_strategy)
def test_marte::sam::saexechost_isSched_setter(instance):
    original = instance.isSched
    instance.isSched = original
    assert instance.isSched == original

@given(instance=MARTE::SAM::SaExecHost_strategy)
def test_marte::sam::saexechost_ISRswitchT_type(instance):
    assert isinstance(instance.ISRswitchT, str)


@given(instance=MARTE::SAM::SaExecHost_strategy)
def test_marte::sam::saexechost_ISRswitchT_setter(instance):
    original = instance.ISRswitchT
    instance.ISRswitchT = original
    assert instance.ISRswitchT == original

@given(instance=MARTE::SAM::SaExecHost_strategy)
def test_marte::sam::saexechost_schedUtiliz_type(instance):
    assert isinstance(instance.schedUtiliz, str)


@given(instance=MARTE::SAM::SaExecHost_strategy)
def test_marte::sam::saexechost_schedUtiliz_setter(instance):
    original = instance.schedUtiliz
    instance.schedUtiliz = original
    assert instance.schedUtiliz == original

@given(instance=MARTE::SAM::SaExecHost_strategy)
def test_marte::sam::saexechost_ISRprioRange_type(instance):
    assert isinstance(instance.ISRprioRange, str)


@given(instance=MARTE::SAM::SaExecHost_strategy)
def test_marte::sam::saexechost_ISRprioRange_setter(instance):
    original = instance.ISRprioRange
    instance.ISRprioRange = original
    assert instance.ISRprioRange == original

@given(instance=GaCommHost_strategy)
@settings(max_examples=50)
def test_gacommhost_instantiation(instance):
    assert isinstance(instance, GaCommHost)

@given(instance=MARTE::SAM::SaCommHost_strategy)
@settings(max_examples=50)
def test_marte::sam::sacommhost_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaCommHost)

@given(instance=MARTE::SAM::SaCommHost_strategy)
def test_marte::sam::sacommhost_isSched_type(instance):
    assert isinstance(instance.isSched, str)


@given(instance=MARTE::SAM::SaCommHost_strategy)
def test_marte::sam::sacommhost_isSched_setter(instance):
    original = instance.isSched
    instance.isSched = original
    assert instance.isSched == original

@given(instance=MARTE::SAM::SaCommHost_strategy)
def test_marte::sam::sacommhost_schSlack_type(instance):
    assert isinstance(instance.schSlack, str)


@given(instance=MARTE::SAM::SaCommHost_strategy)
def test_marte::sam::sacommhost_schSlack_setter(instance):
    original = instance.schSlack
    instance.schSlack = original
    assert instance.schSlack == original

@given(instance=MutualExclusionResource_strategy)
@settings(max_examples=50)
def test_mutualexclusionresource_instantiation(instance):
    assert isinstance(instance, MutualExclusionResource)

@given(instance=MARTE::SAM::SaSharedResource_strategy)
@settings(max_examples=50)
def test_marte::sam::sasharedresource_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaSharedResource)

@given(instance=MARTE::SAM::SaSharedResource_strategy)
def test_marte::sam::sasharedresource_releaseT_type(instance):
    assert isinstance(instance.releaseT, str)


@given(instance=MARTE::SAM::SaSharedResource_strategy)
def test_marte::sam::sasharedresource_releaseT_setter(instance):
    original = instance.releaseT
    instance.releaseT = original
    assert instance.releaseT == original

@given(instance=MARTE::SAM::SaSharedResource_strategy)
def test_marte::sam::sasharedresource_capacity_type(instance):
    assert isinstance(instance.capacity, str)


@given(instance=MARTE::SAM::SaSharedResource_strategy)
def test_marte::sam::sasharedresource_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=MARTE::SAM::SaSharedResource_strategy)
def test_marte::sam::sasharedresource_isConsum_type(instance):
    assert isinstance(instance.isConsum, str)


@given(instance=MARTE::SAM::SaSharedResource_strategy)
def test_marte::sam::sasharedresource_isConsum_setter(instance):
    original = instance.isConsum
    instance.isConsum = original
    assert instance.isConsum == original

@given(instance=MARTE::SAM::SaSharedResource_strategy)
def test_marte::sam::sasharedresource_acquisT_type(instance):
    assert isinstance(instance.acquisT, str)


@given(instance=MARTE::SAM::SaSharedResource_strategy)
def test_marte::sam::sasharedresource_acquisT_setter(instance):
    original = instance.acquisT
    instance.acquisT = original
    assert instance.acquisT == original

@given(instance=MARTE::SAM::SaSharedResource_strategy)
def test_marte::sam::sasharedresource_isPreemp_type(instance):
    assert isinstance(instance.isPreemp, str)


@given(instance=MARTE::SAM::SaSharedResource_strategy)
def test_marte::sam::sasharedresource_isPreemp_setter(instance):
    original = instance.isPreemp
    instance.isPreemp = original
    assert instance.isPreemp == original

@given(instance=SAM::SaSharedResource_strategy)
@settings(max_examples=50)
def test_sam::sasharedresource_instantiation(instance):
    assert isinstance(instance, SAM::SaSharedResource)

@given(instance=SAM::MARTE::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sam::marte::behavioralfeature_instantiation(instance):
    assert isinstance(instance, SAM::MARTE::BehavioralFeature)

@given(instance=MARTE::SAM::SaEndtoEndFlow_strategy)
@settings(max_examples=50)
def test_marte::sam::saendtoendflow_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaEndtoEndFlow)

@given(instance=MARTE::SAM::SaEndtoEndFlow_strategy)
def test_marte::sam::saendtoendflow_end2EndT_type(instance):
    assert isinstance(instance.end2EndT, str)


@given(instance=MARTE::SAM::SaEndtoEndFlow_strategy)
def test_marte::sam::saendtoendflow_end2EndT_setter(instance):
    original = instance.end2EndT
    instance.end2EndT = original
    assert instance.end2EndT == original

@given(instance=MARTE::SAM::SaEndtoEndFlow_strategy)
def test_marte::sam::saendtoendflow_schSlack_type(instance):
    assert isinstance(instance.schSlack, str)


@given(instance=MARTE::SAM::SaEndtoEndFlow_strategy)
def test_marte::sam::saendtoendflow_schSlack_setter(instance):
    original = instance.schSlack
    instance.schSlack = original
    assert instance.schSlack == original

@given(instance=MARTE::SAM::SaEndtoEndFlow_strategy)
def test_marte::sam::saendtoendflow_end2EndD_type(instance):
    assert isinstance(instance.end2EndD, str)


@given(instance=MARTE::SAM::SaEndtoEndFlow_strategy)
def test_marte::sam::saendtoendflow_end2EndD_setter(instance):
    original = instance.end2EndD
    instance.end2EndD = original
    assert instance.end2EndD == original

@given(instance=MARTE::SAM::SaEndtoEndFlow_strategy)
def test_marte::sam::saendtoendflow_isSched_type(instance):
    assert isinstance(instance.isSched, str)


@given(instance=MARTE::SAM::SaEndtoEndFlow_strategy)
def test_marte::sam::saendtoendflow_isSched_setter(instance):
    original = instance.isSched
    instance.isSched = original
    assert instance.isSched == original

@given(instance=GaAnalysisContext_strategy)
@settings(max_examples=50)
def test_gaanalysiscontext_instantiation(instance):
    assert isinstance(instance, GaAnalysisContext)

@given(instance=MARTE::SAM::SaAnalysisContext_strategy)
@settings(max_examples=50)
def test_marte::sam::saanalysiscontext_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaAnalysisContext)

@given(instance=MARTE::SAM::SaAnalysisContext_strategy)
def test_marte::sam::saanalysiscontext_isSched_type(instance):
    assert isinstance(instance.isSched, str)


@given(instance=MARTE::SAM::SaAnalysisContext_strategy)
def test_marte::sam::saanalysiscontext_isSched_setter(instance):
    original = instance.isSched
    instance.isSched = original
    assert instance.isSched == original

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

@given(instance=MARTE::GQAM::GaAnalysisContext_strategy)
def test_marte::gqam::gaanalysiscontext_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=MARTE::GQAM::GaAnalysisContext_strategy)
def test_marte::gqam::gaanalysiscontext_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=GaCommStep_strategy)
@settings(max_examples=50)
def test_gacommstep_instantiation(instance):
    assert isinstance(instance, GaCommStep)

@given(instance=MARTE::SAM::SaCommStep_strategy)
@settings(max_examples=50)
def test_marte::sam::sacommstep_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaCommStep)

@given(instance=MARTE::SAM::SaCommStep_strategy)
def test_marte::sam::sacommstep_deadline_type(instance):
    assert isinstance(instance.deadline, str)


@given(instance=MARTE::SAM::SaCommStep_strategy)
def test_marte::sam::sacommstep_deadline_setter(instance):
    original = instance.deadline
    instance.deadline = original
    assert instance.deadline == original

@given(instance=MARTE::SAM::SaCommStep_strategy)
def test_marte::sam::sacommstep_spareCap_type(instance):
    assert isinstance(instance.spareCap, str)


@given(instance=MARTE::SAM::SaCommStep_strategy)
def test_marte::sam::sacommstep_spareCap_setter(instance):
    original = instance.spareCap
    instance.spareCap = original
    assert instance.spareCap == original

@given(instance=MARTE::SAM::SaCommStep_strategy)
def test_marte::sam::sacommstep_schSlack_type(instance):
    assert isinstance(instance.schSlack, str)


@given(instance=MARTE::SAM::SaCommStep_strategy)
def test_marte::sam::sacommstep_schSlack_setter(instance):
    original = instance.schSlack
    instance.schSlack = original
    assert instance.schSlack == original

@given(instance=SAM::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_sam::marte::namedelement_instantiation(instance):
    assert isinstance(instance, SAM::MARTE::NamedElement)

@given(instance=MARTE::GQAM::GaWorkloadBehavior_strategy)
@settings(max_examples=50)
def test_marte::gqam::gaworkloadbehavior_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaWorkloadBehavior)

@given(instance=SchedulableResource_strategy)
@settings(max_examples=50)
def test_schedulableresource_instantiation(instance):
    assert isinstance(instance, SchedulableResource)

@given(instance=MARTE::GQAM::GaCommChannel_strategy)
@settings(max_examples=50)
def test_marte::gqam::gacommchannel_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaCommChannel)

@given(instance=MARTE::GQAM::GaCommChannel_strategy)
def test_marte::gqam::gacommchannel_utilization_type(instance):
    assert isinstance(instance.utilization, str)


@given(instance=MARTE::GQAM::GaCommChannel_strategy)
def test_marte::gqam::gacommchannel_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original

@given(instance=MARTE::GQAM::GaCommChannel_strategy)
def test_marte::gqam::gacommchannel_packetSize_type(instance):
    assert isinstance(instance.packetSize, str)


@given(instance=MARTE::GQAM::GaCommChannel_strategy)
def test_marte::gqam::gacommchannel_packetSize_setter(instance):
    original = instance.packetSize
    instance.packetSize = original
    assert instance.packetSize == original

@given(instance=GaTimedObs_strategy)
@settings(max_examples=50)
def test_gatimedobs_instantiation(instance):
    assert isinstance(instance, GaTimedObs)

@given(instance=MARTE::SAM::SaSchedObs_strategy)
@settings(max_examples=50)
def test_marte::sam::saschedobs_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaSchedObs)

@given(instance=MARTE::SAM::SaSchedObs_strategy)
def test_marte::sam::saschedobs_suspentions_type(instance):
    assert isinstance(instance.suspentions, str)


@given(instance=MARTE::SAM::SaSchedObs_strategy)
def test_marte::sam::saschedobs_suspentions_setter(instance):
    original = instance.suspentions
    instance.suspentions = original
    assert instance.suspentions == original

@given(instance=MARTE::SAM::SaSchedObs_strategy)
def test_marte::sam::saschedobs_overlaps_type(instance):
    assert isinstance(instance.overlaps, str)


@given(instance=MARTE::SAM::SaSchedObs_strategy)
def test_marte::sam::saschedobs_overlaps_setter(instance):
    original = instance.overlaps
    instance.overlaps = original
    assert instance.overlaps == original

@given(instance=MARTE::SAM::SaSchedObs_strategy)
def test_marte::sam::saschedobs_blockT_type(instance):
    assert isinstance(instance.blockT, str)


@given(instance=MARTE::SAM::SaSchedObs_strategy)
def test_marte::sam::saschedobs_blockT_setter(instance):
    original = instance.blockT
    instance.blockT = original
    assert instance.blockT == original

@given(instance=MARTE::GQAM::GaLatencyObs_strategy)
@settings(max_examples=50)
def test_marte::gqam::galatencyobs_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaLatencyObs)

@given(instance=MARTE::GQAM::GaLatencyObs_strategy)
def test_marte::gqam::galatencyobs_utility_type(instance):
    assert isinstance(instance.utility, str)


@given(instance=MARTE::GQAM::GaLatencyObs_strategy)
def test_marte::gqam::galatencyobs_utility_setter(instance):
    original = instance.utility
    instance.utility = original
    assert instance.utility == original

@given(instance=MARTE::GQAM::GaLatencyObs_strategy)
def test_marte::gqam::galatencyobs_latency_type(instance):
    assert isinstance(instance.latency, str)


@given(instance=MARTE::GQAM::GaLatencyObs_strategy)
def test_marte::gqam::galatencyobs_latency_setter(instance):
    original = instance.latency
    instance.latency = original
    assert instance.latency == original

@given(instance=MARTE::GQAM::GaLatencyObs_strategy)
def test_marte::gqam::galatencyobs_miss_type(instance):
    assert isinstance(instance.miss, str)


@given(instance=MARTE::GQAM::GaLatencyObs_strategy)
def test_marte::gqam::galatencyobs_miss_setter(instance):
    original = instance.miss
    instance.miss = original
    assert instance.miss == original

@given(instance=MARTE::GQAM::GaLatencyObs_strategy)
def test_marte::gqam::galatencyobs_maxJitter_type(instance):
    assert isinstance(instance.maxJitter, str)


@given(instance=MARTE::GQAM::GaLatencyObs_strategy)
def test_marte::gqam::galatencyobs_maxJitter_setter(instance):
    original = instance.maxJitter
    instance.maxJitter = original
    assert instance.maxJitter == original

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

@given(instance=MARTE::PAM::PaResPassStep_strategy)
@settings(max_examples=50)
def test_marte::pam::parespassstep_instantiation(instance):
    assert isinstance(instance, MARTE::PAM::PaResPassStep)

@given(instance=MARTE::PAM::PaResPassStep_strategy)
def test_marte::pam::parespassstep_resUnits_type(instance):
    assert isinstance(instance.resUnits, str)


@given(instance=MARTE::PAM::PaResPassStep_strategy)
def test_marte::pam::parespassstep_resUnits_setter(instance):
    original = instance.resUnits
    instance.resUnits = original
    assert instance.resUnits == original

@given(instance=MARTE::GQAM::GaCommStep_strategy)
@settings(max_examples=50)
def test_marte::gqam::gacommstep_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaCommStep)

@given(instance=MARTE::GQAM::GaRelStep_strategy)
@settings(max_examples=50)
def test_marte::gqam::garelstep_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaRelStep)

@given(instance=MARTE::GQAM::GaRelStep_strategy)
def test_marte::gqam::garelstep_resUnits_type(instance):
    assert isinstance(instance.resUnits, str)


@given(instance=MARTE::GQAM::GaRelStep_strategy)
def test_marte::gqam::garelstep_resUnits_setter(instance):
    original = instance.resUnits
    instance.resUnits = original
    assert instance.resUnits == original

@given(instance=MARTE::SAM::SaStep_strategy)
@settings(max_examples=50)
def test_marte::sam::sastep_instantiation(instance):
    assert isinstance(instance, MARTE::SAM::SaStep)

@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_schSlack_type(instance):
    assert isinstance(instance.schSlack, str)


@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_schSlack_setter(instance):
    original = instance.schSlack
    instance.schSlack = original
    assert instance.schSlack == original

@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_selfSuspensionBlocking_type(instance):
    assert isinstance(instance.selfSuspensionBlocking, str)


@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_selfSuspensionBlocking_setter(instance):
    original = instance.selfSuspensionBlocking
    instance.selfSuspensionBlocking = original
    assert instance.selfSuspensionBlocking == original

@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_deadline_type(instance):
    assert isinstance(instance.deadline, str)


@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_deadline_setter(instance):
    original = instance.deadline
    instance.deadline = original
    assert instance.deadline == original

@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_spareCap_type(instance):
    assert isinstance(instance.spareCap, str)


@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_spareCap_setter(instance):
    original = instance.spareCap
    instance.spareCap = original
    assert instance.spareCap == original

@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_readyT_type(instance):
    assert isinstance(instance.readyT, str)


@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_readyT_setter(instance):
    original = instance.readyT
    instance.readyT = original
    assert instance.readyT == original

@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_numberSelfSuspensions_type(instance):
    assert isinstance(instance.numberSelfSuspensions, str)


@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_numberSelfSuspensions_setter(instance):
    original = instance.numberSelfSuspensions
    instance.numberSelfSuspensions = original
    assert instance.numberSelfSuspensions == original

@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_nonpreemptionBlocking_type(instance):
    assert isinstance(instance.nonpreemptionBlocking, str)


@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_nonpreemptionBlocking_setter(instance):
    original = instance.nonpreemptionBlocking
    instance.nonpreemptionBlocking = original
    assert instance.nonpreemptionBlocking == original

@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_preemptT_type(instance):
    assert isinstance(instance.preemptT, str)


@given(instance=MARTE::SAM::SaStep_strategy)
def test_marte::sam::sastep_preemptT_setter(instance):
    original = instance.preemptT
    instance.preemptT = original
    assert instance.preemptT == original

@given(instance=MARTE::GQAM::GaAcqStep_strategy)
@settings(max_examples=50)
def test_marte::gqam::gaacqstep_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaAcqStep)

@given(instance=MARTE::GQAM::GaAcqStep_strategy)
def test_marte::gqam::gaacqstep_resUnits_type(instance):
    assert isinstance(instance.resUnits, str)


@given(instance=MARTE::GQAM::GaAcqStep_strategy)
def test_marte::gqam::gaacqstep_resUnits_setter(instance):
    original = instance.resUnits
    instance.resUnits = original
    assert instance.resUnits == original

@given(instance=MARTE::PAM::PaStep_strategy)
@settings(max_examples=50)
def test_marte::pam::pastep_instantiation(instance):
    assert isinstance(instance, MARTE::PAM::PaStep)

@given(instance=MARTE::PAM::PaStep_strategy)
def test_marte::pam::pastep_noSync_type(instance):
    assert isinstance(instance.noSync, str)


@given(instance=MARTE::PAM::PaStep_strategy)
def test_marte::pam::pastep_noSync_setter(instance):
    original = instance.noSync
    instance.noSync = original
    assert instance.noSync == original

@given(instance=MARTE::PAM::PaStep_strategy)
def test_marte::pam::pastep_extOpCount_type(instance):
    assert isinstance(instance.extOpCount, str)


@given(instance=MARTE::PAM::PaStep_strategy)
def test_marte::pam::pastep_extOpCount_setter(instance):
    original = instance.extOpCount
    instance.extOpCount = original
    assert instance.extOpCount == original

@given(instance=MARTE::PAM::PaStep_strategy)
def test_marte::pam::pastep_behavCount_type(instance):
    assert isinstance(instance.behavCount, str)


@given(instance=MARTE::PAM::PaStep_strategy)
def test_marte::pam::pastep_behavCount_setter(instance):
    original = instance.behavCount
    instance.behavCount = original
    assert instance.behavCount == original

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

@given(instance=GQAM::GaExecHost_strategy)
@settings(max_examples=50)
def test_gqam::gaexechost_instantiation(instance):
    assert isinstance(instance, GQAM::GaExecHost)

@given(instance=GaScenario_strategy)
@settings(max_examples=50)
def test_gascenario_instantiation(instance):
    assert isinstance(instance, GaScenario)

@given(instance=MARTE::GQAM::GaStep_strategy)
@settings(max_examples=50)
def test_marte::gqam::gastep_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaStep)

@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_blockT_type(instance):
    assert isinstance(instance.blockT, str)


@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_blockT_setter(instance):
    original = instance.blockT
    instance.blockT = original
    assert instance.blockT == original

@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_selfDelay_type(instance):
    assert isinstance(instance.selfDelay, str)


@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_selfDelay_setter(instance):
    original = instance.selfDelay
    instance.selfDelay = original
    assert instance.selfDelay == original

@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_prob_type(instance):
    assert isinstance(instance.prob, str)


@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_prob_setter(instance):
    original = instance.prob
    instance.prob = original
    assert instance.prob == original

@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_isAtomic_type(instance):
    assert isinstance(instance.isAtomic, str)


@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original

@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_rep_type(instance):
    assert isinstance(instance.rep, str)


@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_rep_setter(instance):
    original = instance.rep
    instance.rep = original
    assert instance.rep == original

@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_servCount_type(instance):
    assert isinstance(instance.servCount, str)


@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_servCount_setter(instance):
    original = instance.servCount
    instance.servCount = original
    assert instance.servCount == original

@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=MARTE::GQAM::GaStep_strategy)
def test_marte::gqam::gastep_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=GQAM::GaTimedObs_strategy)
@settings(max_examples=50)
def test_gqam::gatimedobs_instantiation(instance):
    assert isinstance(instance, GQAM::GaTimedObs)

@given(instance=GQAM::GaRequestedService_strategy)
@settings(max_examples=50)
def test_gqam::garequestedservice_instantiation(instance):
    assert isinstance(instance, GQAM::GaRequestedService)

@given(instance=MARTE::PAM::PaRequestedStep_strategy)
@settings(max_examples=50)
def test_marte::pam::parequestedstep_instantiation(instance):
    assert isinstance(instance, MARTE::PAM::PaRequestedStep)

@given(instance=GQAM::GaWorkloadEvent_strategy)
@settings(max_examples=50)
def test_gqam::gaworkloadevent_instantiation(instance):
    assert isinstance(instance, GQAM::GaWorkloadEvent)

@given(instance=Time::TimedProcessing_strategy)
@settings(max_examples=50)
def test_time::timedprocessing_instantiation(instance):
    assert isinstance(instance, Time::TimedProcessing)

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

@given(instance=MARTE::GQAM::GaWorkloadEvent_strategy)
def test_marte::gqam::gaworkloadevent_pattern_type(instance):
    assert isinstance(instance.pattern, str)


@given(instance=MARTE::GQAM::GaWorkloadEvent_strategy)
def test_marte::gqam::gaworkloadevent_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=GQAM::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_gqam::marte::namedelement_instantiation(instance):
    assert isinstance(instance, GQAM::MARTE::NamedElement)

@given(instance=GQAM::GaStep_strategy)
@settings(max_examples=50)
def test_gqam::gastep_instantiation(instance):
    assert isinstance(instance, GQAM::GaStep)

@given(instance=MARTE::GQAM::GaWorkloadGenerator_strategy)
@settings(max_examples=50)
def test_marte::gqam::gaworkloadgenerator_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaWorkloadGenerator)

@given(instance=MARTE::GQAM::GaWorkloadGenerator_strategy)
def test_marte::gqam::gaworkloadgenerator_pop_type(instance):
    assert isinstance(instance.pop, str)


@given(instance=MARTE::GQAM::GaWorkloadGenerator_strategy)
def test_marte::gqam::gaworkloadgenerator_pop_setter(instance):
    original = instance.pop
    instance.pop = original
    assert instance.pop == original

@given(instance=MARTE::GCM::GCMInvocatingBehavior_strategy)
@settings(max_examples=50)
def test_marte::gcm::gcminvocatingbehavior_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::GCMInvocatingBehavior)

@given(instance=GCM::MARTE::Behavior_strategy)
@settings(max_examples=50)
def test_gcm::marte::behavior_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Behavior)

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

@given(instance=MARTE::GQAM::GaEventTrace_strategy)
@settings(max_examples=50)
def test_marte::gqam::gaeventtrace_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaEventTrace)

@given(instance=MARTE::GQAM::GaEventTrace_strategy)
def test_marte::gqam::gaeventtrace_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=MARTE::GQAM::GaEventTrace_strategy)
def test_marte::gqam::gaeventtrace_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

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

@given(instance=MARTE::NFPs::Nfp_strategy)
@settings(max_examples=50)
def test_marte::nfps::nfp_instantiation(instance):
    assert isinstance(instance, MARTE::NFPs::Nfp)

@given(instance=GCM::MARTE::Interface_strategy)
@settings(max_examples=50)
def test_gcm::marte::interface_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Interface)

@given(instance=MARTE::GCM::ClientServerPort_strategy)
@settings(max_examples=50)
def test_marte::gcm::clientserverport_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::ClientServerPort)

@given(instance=MARTE::GCM::ClientServerPort_strategy)
def test_marte::gcm::clientserverport_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::GCM::ClientServerPort_strategy)
def test_marte::gcm::clientserverport_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MARTE::GCM::ClientServerPort_strategy)
def test_marte::gcm::clientserverport_specificationKind_type(instance):
    assert isinstance(instance.specificationKind, str)


@given(instance=MARTE::GCM::ClientServerPort_strategy)
def test_marte::gcm::clientserverport_specificationKind_setter(instance):
    original = instance.specificationKind
    instance.specificationKind = original
    assert instance.specificationKind == original

@given(instance=GCM::MARTE::Port_strategy)
@settings(max_examples=50)
def test_gcm::marte::port_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Port)

@given(instance=MARTE::GCM::FlowPort_strategy)
@settings(max_examples=50)
def test_marte::gcm::flowport_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::FlowPort)

@given(instance=MARTE::GCM::FlowPort_strategy)
def test_marte::gcm::flowport_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=MARTE::GCM::FlowPort_strategy)
def test_marte::gcm::flowport_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=MARTE::GCM::FlowPort_strategy)
def test_marte::gcm::flowport_isAtomic_type(instance):
    assert isinstance(instance.isAtomic, str)


@given(instance=MARTE::GCM::FlowPort_strategy)
def test_marte::gcm::flowport_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original

@given(instance=GCM::MARTE::Trigger_strategy)
@settings(max_examples=50)
def test_gcm::marte::trigger_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Trigger)

@given(instance=MARTE::GCM::GCMTrigger_strategy)
@settings(max_examples=50)
def test_marte::gcm::gcmtrigger_instantiation(instance):
    assert isinstance(instance, MARTE::GCM::GCMTrigger)

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

@given(instance=SW::Interaction::SwSynchronizationResource_strategy)
@settings(max_examples=50)
def test_sw::interaction::swsynchronizationresource_instantiation(instance):
    assert isinstance(instance, SW::Interaction::SwSynchronizationResource)

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

@given(instance=GCM::MARTE::Property_strategy)
@settings(max_examples=50)
def test_gcm::marte::property_instantiation(instance):
    assert isinstance(instance, GCM::MARTE::Property)

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
def test_marte::sw::interaction::messagecomresource_messageQueuePolicy_type(instance):
    assert isinstance(instance.messageQueuePolicy, str)


@given(instance=MARTE::SW::Interaction::MessageComResource_strategy)
def test_marte::sw::interaction::messagecomresource_messageQueuePolicy_setter(instance):
    original = instance.messageQueuePolicy
    instance.messageQueuePolicy = original
    assert instance.messageQueuePolicy == original

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
def test_marte::sw::concurrency::interruptresource_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::SW::Concurrency::InterruptResource_strategy)
def test_marte::sw::concurrency::interruptresource_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MARTE::SW::Concurrency::InterruptResource_strategy)
def test_marte::sw::concurrency::interruptresource_isMaskable_type(instance):
    assert isinstance(instance.isMaskable, str)


@given(instance=MARTE::SW::Concurrency::InterruptResource_strategy)
def test_marte::sw::concurrency::interruptresource_isMaskable_setter(instance):
    original = instance.isMaskable
    instance.isMaskable = original
    assert instance.isMaskable == original

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
def test_marte::sw::interaction::swinteractionresource_isIntraMemoryPartitionInteraction_type(instance):
    assert isinstance(instance.isIntraMemoryPartitionInteraction, bool)


@given(instance=MARTE::SW::Interaction::SwInteractionResource_strategy)
def test_marte::sw::interaction::swinteractionresource_isIntraMemoryPartitionInteraction_setter(instance):
    original = instance.isIntraMemoryPartitionInteraction
    instance.isIntraMemoryPartitionInteraction = original
    assert instance.isIntraMemoryPartitionInteraction == original

@given(instance=MARTE::SW::Interaction::SwInteractionResource_strategy)
def test_marte::sw::interaction::swinteractionresource_waitingQueuePolicy_type(instance):
    assert isinstance(instance.waitingQueuePolicy, str)


@given(instance=MARTE::SW::Interaction::SwInteractionResource_strategy)
def test_marte::sw::interaction::swinteractionresource_waitingQueuePolicy_setter(instance):
    original = instance.waitingQueuePolicy
    instance.waitingQueuePolicy = original
    assert instance.waitingQueuePolicy == original

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
def test_marte::sw::concurrency::swconcurrentresource_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MARTE::SW::Concurrency::SwConcurrentResource_strategy)
def test_marte::sw::concurrency::swconcurrentresource_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MARTE::SW::Concurrency::SwConcurrentResource_strategy)
def test_marte::sw::concurrency::swconcurrentresource_activationCapacity_type(instance):
    assert isinstance(instance.activationCapacity, str)


@given(instance=MARTE::SW::Concurrency::SwConcurrentResource_strategy)
def test_marte::sw::concurrency::swconcurrentresource_activationCapacity_setter(instance):
    original = instance.activationCapacity
    instance.activationCapacity = original
    assert instance.activationCapacity == original

@given(instance=SW::Concurrency::MARTE::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw::concurrency::marte::behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW::Concurrency::MARTE::BehavioralFeature)

@given(instance=SW::ResourceCore::MARTE::Property_strategy)
@settings(max_examples=50)
def test_sw::resourcecore::marte::property_instantiation(instance):
    assert isinstance(instance, SW::ResourceCore::MARTE::Property)

@given(instance=SW::ResourceCore::MARTE::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw::resourcecore::marte::behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW::ResourceCore::MARTE::BehavioralFeature)

@given(instance=SW::ResourceCore::MARTE::TypedElement_strategy)
@settings(max_examples=50)
def test_sw::resourcecore::marte::typedelement_instantiation(instance):
    assert isinstance(instance, SW::ResourceCore::MARTE::TypedElement)

@given(instance=SW::Concurrency::MARTE::TypedElement_strategy)
@settings(max_examples=50)
def test_sw::concurrency::marte::typedelement_instantiation(instance):
    assert isinstance(instance, SW::Concurrency::MARTE::TypedElement)

@given(instance=HwComponent_strategy)
@settings(max_examples=50)
def test_hwcomponent_instantiation(instance):
    assert isinstance(instance, HwComponent)

@given(instance=MARTE::HwPower::HwCoolingSupply_strategy)
@settings(max_examples=50)
def test_marte::hwpower::hwcoolingsupply_instantiation(instance):
    assert isinstance(instance, MARTE::HwPower::HwCoolingSupply)

@given(instance=MARTE::HwPower::HwCoolingSupply_strategy)
def test_marte::hwpower::hwcoolingsupply_coolingPower_type(instance):
    assert isinstance(instance.coolingPower, str)


@given(instance=MARTE::HwPower::HwCoolingSupply_strategy)
def test_marte::hwpower::hwcoolingsupply_coolingPower_setter(instance):
    original = instance.coolingPower
    instance.coolingPower = original
    assert instance.coolingPower == original

@given(instance=MARTE::HwPower::HwPowerSupply_strategy)
@settings(max_examples=50)
def test_marte::hwpower::hwpowersupply_instantiation(instance):
    assert isinstance(instance, MARTE::HwPower::HwPowerSupply)

@given(instance=MARTE::HwPower::HwPowerSupply_strategy)
def test_marte::hwpower::hwpowersupply_capacity_type(instance):
    assert isinstance(instance.capacity, str)


@given(instance=MARTE::HwPower::HwPowerSupply_strategy)
def test_marte::hwpower::hwpowersupply_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=MARTE::HwPower::HwPowerSupply_strategy)
def test_marte::hwpower::hwpowersupply_suppliedPower_type(instance):
    assert isinstance(instance.suppliedPower, str)


@given(instance=MARTE::HwPower::HwPowerSupply_strategy)
def test_marte::hwpower::hwpowersupply_suppliedPower_setter(instance):
    original = instance.suppliedPower
    instance.suppliedPower = original
    assert instance.suppliedPower == original

@given(instance=HwLayout::HwComponent_strategy)
@settings(max_examples=50)
def test_hwlayout::hwcomponent_instantiation(instance):
    assert isinstance(instance, HwLayout::HwComponent)

@given(instance=HwCommunication::HwEndPoint_strategy)
@settings(max_examples=50)
def test_hwcommunication::hwendpoint_instantiation(instance):
    assert isinstance(instance, HwCommunication::HwEndPoint)

@given(instance=HwGeneral::HwResourceService_strategy)
@settings(max_examples=50)
def test_hwgeneral::hwresourceservice_instantiation(instance):
    assert isinstance(instance, HwGeneral::HwResourceService)

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

@given(instance=HwTiming::HwClock_strategy)
@settings(max_examples=50)
def test_hwtiming::hwclock_instantiation(instance):
    assert isinstance(instance, HwTiming::HwClock)

@given(instance=HwTimingResource_strategy)
@settings(max_examples=50)
def test_hwtimingresource_instantiation(instance):
    assert isinstance(instance, HwTimingResource)

@given(instance=MARTE::HwTiming::HwTimer_strategy)
@settings(max_examples=50)
def test_marte::hwtiming::hwtimer_instantiation(instance):
    assert isinstance(instance, MARTE::HwTiming::HwTimer)

@given(instance=MARTE::HwTiming::HwTimer_strategy)
def test_marte::hwtiming::hwtimer_counterWidth_type(instance):
    assert isinstance(instance.counterWidth, str)


@given(instance=MARTE::HwTiming::HwTimer_strategy)
def test_marte::hwtiming::hwtimer_counterWidth_setter(instance):
    original = instance.counterWidth
    instance.counterWidth = original
    assert instance.counterWidth == original

@given(instance=MARTE::HwTiming::HwTimer_strategy)
def test_marte::hwtiming::hwtimer_nbCounters_type(instance):
    assert isinstance(instance.nbCounters, str)


@given(instance=MARTE::HwTiming::HwTimer_strategy)
def test_marte::hwtiming::hwtimer_nbCounters_setter(instance):
    original = instance.nbCounters
    instance.nbCounters = original
    assert instance.nbCounters == original

@given(instance=MARTE::HwTiming::HwClock_strategy)
@settings(max_examples=50)
def test_marte::hwtiming::hwclock_instantiation(instance):
    assert isinstance(instance, MARTE::HwTiming::HwClock)

@given(instance=GRM::TimingResource_strategy)
@settings(max_examples=50)
def test_grm::timingresource_instantiation(instance):
    assert isinstance(instance, GRM::TimingResource)

@given(instance=HwDevice_strategy)
@settings(max_examples=50)
def test_hwdevice_instantiation(instance):
    assert isinstance(instance, HwDevice)

@given(instance=MARTE::HwDevice::HwSupport_strategy)
@settings(max_examples=50)
def test_marte::hwdevice::hwsupport_instantiation(instance):
    assert isinstance(instance, MARTE::HwDevice::HwSupport)

@given(instance=MARTE::HwDevice::HwI::O_strategy)
@settings(max_examples=50)
def test_marte::hwdevice::hwi::o_instantiation(instance):
    assert isinstance(instance, MARTE::HwDevice::HwI::O)

@given(instance=GRM::DeviceResource_strategy)
@settings(max_examples=50)
def test_grm::deviceresource_instantiation(instance):
    assert isinstance(instance, GRM::DeviceResource)

@given(instance=HwMemory_strategy)
@settings(max_examples=50)
def test_hwmemory_instantiation(instance):
    assert isinstance(instance, HwMemory)

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
def test_marte::hwmemory::hwcache_structure_type(instance):
    assert isinstance(instance.structure, str)


@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_structure_setter(instance):
    original = instance.structure
    instance.structure = original
    assert instance.structure == original

@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_repl_Policy_type(instance):
    assert isinstance(instance.repl_Policy, str)


@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_repl_Policy_setter(instance):
    original = instance.repl_Policy
    instance.repl_Policy = original
    assert instance.repl_Policy == original

@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MARTE::HwMemory::HwCache_strategy)
def test_marte::hwmemory::hwcache_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MARTE::HwMemory::HwDrive_strategy)
@settings(max_examples=50)
def test_marte::hwmemory::hwdrive_instantiation(instance):
    assert isinstance(instance, MARTE::HwMemory::HwDrive)

@given(instance=MARTE::HwMemory::HwDrive_strategy)
def test_marte::hwmemory::hwdrive_sectorSize_type(instance):
    assert isinstance(instance.sectorSize, str)


@given(instance=MARTE::HwMemory::HwDrive_strategy)
def test_marte::hwmemory::hwdrive_sectorSize_setter(instance):
    original = instance.sectorSize
    instance.sectorSize = original
    assert instance.sectorSize == original

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

@given(instance=MARTE::HwMemory::HwROM_strategy)
def test_marte::hwmemory::hwrom_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=MARTE::HwMemory::HwROM_strategy)
def test_marte::hwmemory::hwrom_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=MARTE::HwMemory::HwRAM_strategy)
@settings(max_examples=50)
def test_marte::hwmemory::hwram_instantiation(instance):
    assert isinstance(instance, MARTE::HwMemory::HwRAM)

@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_isNonVolatile_type(instance):
    assert isinstance(instance.isNonVolatile, str)


@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_isNonVolatile_setter(instance):
    original = instance.isNonVolatile
    instance.isNonVolatile = original
    assert instance.isNonVolatile == original

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

@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_isSynchronous_type(instance):
    assert isinstance(instance.isSynchronous, str)


@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_isStatic_type(instance):
    assert isinstance(instance.isStatic, str)


@given(instance=MARTE::HwMemory::HwRAM_strategy)
def test_marte::hwmemory::hwram_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=HwComputing::HwProcessor_strategy)
@settings(max_examples=50)
def test_hwcomputing::hwprocessor_instantiation(instance):
    assert isinstance(instance, HwComputing::HwProcessor)

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

@given(instance=GRM::CommunicationEndPoint_strategy)
@settings(max_examples=50)
def test_grm::communicationendpoint_instantiation(instance):
    assert isinstance(instance, GRM::CommunicationEndPoint)

@given(instance=HwMedia_strategy)
@settings(max_examples=50)
def test_hwmedia_instantiation(instance):
    assert isinstance(instance, HwMedia)

@given(instance=MARTE::HwCommunication::HwBridge_strategy)
@settings(max_examples=50)
def test_marte::hwcommunication::hwbridge_instantiation(instance):
    assert isinstance(instance, MARTE::HwCommunication::HwBridge)

@given(instance=MARTE::HwCommunication::HwBus_strategy)
@settings(max_examples=50)
def test_marte::hwcommunication::hwbus_instantiation(instance):
    assert isinstance(instance, MARTE::HwCommunication::HwBus)

@given(instance=MARTE::HwCommunication::HwBus_strategy)
def test_marte::hwcommunication::hwbus_isSynchronous_type(instance):
    assert isinstance(instance.isSynchronous, str)


@given(instance=MARTE::HwCommunication::HwBus_strategy)
def test_marte::hwcommunication::hwbus_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=MARTE::HwCommunication::HwBus_strategy)
def test_marte::hwcommunication::hwbus_isSerial_type(instance):
    assert isinstance(instance.isSerial, str)


@given(instance=MARTE::HwCommunication::HwBus_strategy)
def test_marte::hwcommunication::hwbus_isSerial_setter(instance):
    original = instance.isSerial
    instance.isSerial = original
    assert instance.isSerial == original

@given(instance=MARTE::HwCommunication::HwBus_strategy)
def test_marte::hwcommunication::hwbus_adressWidth_type(instance):
    assert isinstance(instance.adressWidth, str)


@given(instance=MARTE::HwCommunication::HwBus_strategy)
def test_marte::hwcommunication::hwbus_adressWidth_setter(instance):
    original = instance.adressWidth
    instance.adressWidth = original
    assert instance.adressWidth == original

@given(instance=MARTE::HwCommunication::HwBus_strategy)
def test_marte::hwcommunication::hwbus_wordWidth_type(instance):
    assert isinstance(instance.wordWidth, str)


@given(instance=MARTE::HwCommunication::HwBus_strategy)
def test_marte::hwcommunication::hwbus_wordWidth_setter(instance):
    original = instance.wordWidth
    instance.wordWidth = original
    assert instance.wordWidth == original

@given(instance=HwCommunication::HwArbiter_strategy)
@settings(max_examples=50)
def test_hwcommunication::hwarbiter_instantiation(instance):
    assert isinstance(instance, HwCommunication::HwArbiter)

@given(instance=MARTE::HwStorageManager::HwDMA_strategy)
@settings(max_examples=50)
def test_marte::hwstoragemanager::hwdma_instantiation(instance):
    assert isinstance(instance, MARTE::HwStorageManager::HwDMA)

@given(instance=MARTE::HwStorageManager::HwDMA_strategy)
def test_marte::hwstoragemanager::hwdma_transferWidth_type(instance):
    assert isinstance(instance.transferWidth, str)


@given(instance=MARTE::HwStorageManager::HwDMA_strategy)
def test_marte::hwstoragemanager::hwdma_transferWidth_setter(instance):
    original = instance.transferWidth
    instance.transferWidth = original
    assert instance.transferWidth == original

@given(instance=MARTE::HwStorageManager::HwDMA_strategy)
def test_marte::hwstoragemanager::hwdma_nbChannels_type(instance):
    assert isinstance(instance.nbChannels, str)


@given(instance=MARTE::HwStorageManager::HwDMA_strategy)
def test_marte::hwstoragemanager::hwdma_nbChannels_setter(instance):
    original = instance.nbChannels
    instance.nbChannels = original
    assert instance.nbChannels == original

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

@given(instance=MARTE::HwCommunication::HwMedia_strategy)
def test_marte::hwcommunication::hwmedia_bandWidth_type(instance):
    assert isinstance(instance.bandWidth, str)


@given(instance=MARTE::HwCommunication::HwMedia_strategy)
def test_marte::hwcommunication::hwmedia_bandWidth_setter(instance):
    original = instance.bandWidth
    instance.bandWidth = original
    assert instance.bandWidth == original

@given(instance=HwStorageManager_strategy)
@settings(max_examples=50)
def test_hwstoragemanager_instantiation(instance):
    assert isinstance(instance, HwStorageManager)

@given(instance=MARTE::HwStorageManager::HwMMU_strategy)
@settings(max_examples=50)
def test_marte::hwstoragemanager::hwmmu_instantiation(instance):
    assert isinstance(instance, MARTE::HwStorageManager::HwMMU)

@given(instance=MARTE::HwStorageManager::HwMMU_strategy)
def test_marte::hwstoragemanager::hwmmu_virtualAddrSpace_type(instance):
    assert isinstance(instance.virtualAddrSpace, str)


@given(instance=MARTE::HwStorageManager::HwMMU_strategy)
def test_marte::hwstoragemanager::hwmmu_virtualAddrSpace_setter(instance):
    original = instance.virtualAddrSpace
    instance.virtualAddrSpace = original
    assert instance.virtualAddrSpace == original

@given(instance=MARTE::HwStorageManager::HwMMU_strategy)
def test_marte::hwstoragemanager::hwmmu_memoryProtection_type(instance):
    assert isinstance(instance.memoryProtection, str)


@given(instance=MARTE::HwStorageManager::HwMMU_strategy)
def test_marte::hwstoragemanager::hwmmu_memoryProtection_setter(instance):
    original = instance.memoryProtection
    instance.memoryProtection = original
    assert instance.memoryProtection == original

@given(instance=MARTE::HwStorageManager::HwMMU_strategy)
def test_marte::hwstoragemanager::hwmmu_nbEntries_type(instance):
    assert isinstance(instance.nbEntries, str)


@given(instance=MARTE::HwStorageManager::HwMMU_strategy)
def test_marte::hwstoragemanager::hwmmu_nbEntries_setter(instance):
    original = instance.nbEntries
    instance.nbEntries = original
    assert instance.nbEntries == original

@given(instance=MARTE::HwStorageManager::HwMMU_strategy)
def test_marte::hwstoragemanager::hwmmu_physicalAddrSpace_type(instance):
    assert isinstance(instance.physicalAddrSpace, str)


@given(instance=MARTE::HwStorageManager::HwMMU_strategy)
def test_marte::hwstoragemanager::hwmmu_physicalAddrSpace_setter(instance):
    original = instance.physicalAddrSpace
    instance.physicalAddrSpace = original
    assert instance.physicalAddrSpace == original

@given(instance=HwComputing::HwComputingResource_strategy)
@settings(max_examples=50)
def test_hwcomputing::hwcomputingresource_instantiation(instance):
    assert isinstance(instance, HwComputing::HwComputingResource)

@given(instance=HwMemory::HwRAM_strategy)
@settings(max_examples=50)
def test_hwmemory::hwram_instantiation(instance):
    assert isinstance(instance, HwMemory::HwRAM)

@given(instance=HwResource_strategy)
@settings(max_examples=50)
def test_hwresource_instantiation(instance):
    assert isinstance(instance, HwResource)

@given(instance=MARTE::HwCommunication::HwCommunicationResource_strategy)
@settings(max_examples=50)
def test_marte::hwcommunication::hwcommunicationresource_instantiation(instance):
    assert isinstance(instance, MARTE::HwCommunication::HwCommunicationResource)

@given(instance=MARTE::HwLayout::HwComponent_strategy)
@settings(max_examples=50)
def test_marte::hwlayout::hwcomponent_instantiation(instance):
    assert isinstance(instance, MARTE::HwLayout::HwComponent)

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_grid_type(instance):
    assert isinstance(instance.grid, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_grid_setter(instance):
    original = instance.grid
    instance.grid = original
    assert instance.grid == original

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_dimensions_type(instance):
    assert isinstance(instance.dimensions, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_r_Conditions_type(instance):
    assert isinstance(instance.r_Conditions, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_r_Conditions_setter(instance):
    original = instance.r_Conditions
    instance.r_Conditions = original
    assert instance.r_Conditions == original

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_price_type(instance):
    assert isinstance(instance.price, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_nbPins_type(instance):
    assert isinstance(instance.nbPins, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_nbPins_setter(instance):
    original = instance.nbPins
    instance.nbPins = original
    assert instance.nbPins == original

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_staticConsumption_type(instance):
    assert isinstance(instance.staticConsumption, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_staticConsumption_setter(instance):
    original = instance.staticConsumption
    instance.staticConsumption = original
    assert instance.staticConsumption == original

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_area_type(instance):
    assert isinstance(instance.area, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_area_setter(instance):
    original = instance.area
    instance.area = original
    assert instance.area == original

@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_staticDissipation_type(instance):
    assert isinstance(instance.staticDissipation, str)


@given(instance=MARTE::HwLayout::HwComponent_strategy)
def test_marte::hwlayout::hwcomponent_staticDissipation_setter(instance):
    original = instance.staticDissipation
    instance.staticDissipation = original
    assert instance.staticDissipation == original

@given(instance=MARTE::HwComputing::HwBranchPredictor_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwbranchpredictor_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwBranchPredictor)

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

@given(instance=MARTE::HwComputing::HwISA_strategy)
def test_marte::hwcomputing::hwisa_family_type(instance):
    assert isinstance(instance.family, str)


@given(instance=MARTE::HwComputing::HwISA_strategy)
def test_marte::hwcomputing::hwisa_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original

@given(instance=MARTE::HwComputing::HwISA_strategy)
def test_marte::hwcomputing::hwisa_inst_Width_type(instance):
    assert isinstance(instance.inst_Width, str)


@given(instance=MARTE::HwComputing::HwISA_strategy)
def test_marte::hwcomputing::hwisa_inst_Width_setter(instance):
    original = instance.inst_Width
    instance.inst_Width = original
    assert instance.inst_Width == original

@given(instance=HwGeneral::HwResource_strategy)
@settings(max_examples=50)
def test_hwgeneral::hwresource_instantiation(instance):
    assert isinstance(instance, HwGeneral::HwResource)

@given(instance=MARTE::HwStorageManager::HwStorageManager_strategy)
@settings(max_examples=50)
def test_marte::hwstoragemanager::hwstoragemanager_instantiation(instance):
    assert isinstance(instance, MARTE::HwStorageManager::HwStorageManager)

@given(instance=MARTE::HwTiming::HwTimingResource_strategy)
@settings(max_examples=50)
def test_marte::hwtiming::hwtimingresource_instantiation(instance):
    assert isinstance(instance, MARTE::HwTiming::HwTimingResource)

@given(instance=MARTE::HwDevice::HwDevice_strategy)
@settings(max_examples=50)
def test_marte::hwdevice::hwdevice_instantiation(instance):
    assert isinstance(instance, MARTE::HwDevice::HwDevice)

@given(instance=MARTE::HwMemory::HwMemory_strategy)
@settings(max_examples=50)
def test_marte::hwmemory::hwmemory_instantiation(instance):
    assert isinstance(instance, MARTE::HwMemory::HwMemory)

@given(instance=MARTE::HwMemory::HwMemory_strategy)
def test_marte::hwmemory::hwmemory_adressSize_type(instance):
    assert isinstance(instance.adressSize, str)


@given(instance=MARTE::HwMemory::HwMemory_strategy)
def test_marte::hwmemory::hwmemory_adressSize_setter(instance):
    original = instance.adressSize
    instance.adressSize = original
    assert instance.adressSize == original

@given(instance=MARTE::HwMemory::HwMemory_strategy)
def test_marte::hwmemory::hwmemory_throughput_type(instance):
    assert isinstance(instance.throughput, str)


@given(instance=MARTE::HwMemory::HwMemory_strategy)
def test_marte::hwmemory::hwmemory_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original

@given(instance=MARTE::HwMemory::HwMemory_strategy)
def test_marte::hwmemory::hwmemory_timings_type(instance):
    assert isinstance(instance.timings, str)


@given(instance=MARTE::HwMemory::HwMemory_strategy)
def test_marte::hwmemory::hwmemory_timings_setter(instance):
    original = instance.timings
    instance.timings = original
    assert instance.timings == original

@given(instance=MARTE::HwMemory::HwMemory_strategy)
def test_marte::hwmemory::hwmemory_memorySize_type(instance):
    assert isinstance(instance.memorySize, str)


@given(instance=MARTE::HwMemory::HwMemory_strategy)
def test_marte::hwmemory::hwmemory_memorySize_setter(instance):
    original = instance.memorySize
    instance.memorySize = original
    assert instance.memorySize == original

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

@given(instance=HwMemory::HwCache_strategy)
@settings(max_examples=50)
def test_hwmemory::hwcache_instantiation(instance):
    assert isinstance(instance, HwMemory::HwCache)

@given(instance=HwComputing::HwBranchPredictor_strategy)
@settings(max_examples=50)
def test_hwcomputing::hwbranchpredictor_instantiation(instance):
    assert isinstance(instance, HwComputing::HwBranchPredictor)

@given(instance=HwComputing::HwISA_strategy)
@settings(max_examples=50)
def test_hwcomputing::hwisa_instantiation(instance):
    assert isinstance(instance, HwComputing::HwISA)

@given(instance=HwComputingResource_strategy)
@settings(max_examples=50)
def test_hwcomputingresource_instantiation(instance):
    assert isinstance(instance, HwComputingResource)

@given(instance=MARTE::HwComputing::HwPLD_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwpld_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwPLD)

@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_ndLUT_Inputs_type(instance):
    assert isinstance(instance.ndLUT_Inputs, str)


@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_ndLUT_Inputs_setter(instance):
    original = instance.ndLUT_Inputs
    instance.ndLUT_Inputs = original
    assert instance.ndLUT_Inputs == original

@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_technology_type(instance):
    assert isinstance(instance.technology, str)


@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_technology_setter(instance):
    original = instance.technology
    instance.technology = original
    assert instance.technology == original

@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_nbFlipFlops_type(instance):
    assert isinstance(instance.nbFlipFlops, str)


@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_nbFlipFlops_setter(instance):
    original = instance.nbFlipFlops
    instance.nbFlipFlops = original
    assert instance.nbFlipFlops == original

@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_nbLUTs_type(instance):
    assert isinstance(instance.nbLUTs, str)


@given(instance=MARTE::HwComputing::HwPLD_strategy)
def test_marte::hwcomputing::hwpld_nbLUTs_setter(instance):
    original = instance.nbLUTs
    instance.nbLUTs = original
    assert instance.nbLUTs == original

@given(instance=MARTE::HwComputing::HwASIC_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwasic_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwASIC)

@given(instance=MARTE::HwComputing::HwProcessor_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwprocessor_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwProcessor)

@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_architecture_type(instance):
    assert isinstance(instance.architecture, str)


@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_architecture_setter(instance):
    original = instance.architecture
    instance.architecture = original
    assert instance.architecture == original

@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_nbPipelines_type(instance):
    assert isinstance(instance.nbPipelines, str)


@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_nbPipelines_setter(instance):
    original = instance.nbPipelines
    instance.nbPipelines = original
    assert instance.nbPipelines == original

@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_nbCores_type(instance):
    assert isinstance(instance.nbCores, str)


@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_nbCores_setter(instance):
    original = instance.nbCores
    instance.nbCores = original
    assert instance.nbCores == original

@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_nbALUs_type(instance):
    assert isinstance(instance.nbALUs, str)


@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_nbALUs_setter(instance):
    original = instance.nbALUs
    instance.nbALUs = original
    assert instance.nbALUs == original

@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_mips_type(instance):
    assert isinstance(instance.mips, str)


@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_mips_setter(instance):
    original = instance.mips
    instance.mips = original
    assert instance.mips == original

@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_nbFPUs_type(instance):
    assert isinstance(instance.nbFPUs, str)


@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_nbFPUs_setter(instance):
    original = instance.nbFPUs
    instance.nbFPUs = original
    assert instance.nbFPUs == original

@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_ipc_type(instance):
    assert isinstance(instance.ipc, str)


@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_ipc_setter(instance):
    original = instance.ipc
    instance.ipc = original
    assert instance.ipc == original

@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_nbStages_type(instance):
    assert isinstance(instance.nbStages, str)


@given(instance=MARTE::HwComputing::HwProcessor_strategy)
def test_marte::hwcomputing::hwprocessor_nbStages_setter(instance):
    original = instance.nbStages
    instance.nbStages = original
    assert instance.nbStages == original

@given(instance=HwStorageManager::HwMMU_strategy)
@settings(max_examples=50)
def test_hwstoragemanager::hwmmu_instantiation(instance):
    assert isinstance(instance, HwStorageManager::HwMMU)

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
def test_marte::hlam::rtservice_isAtomic_type(instance):
    assert isinstance(instance.isAtomic, str)


@given(instance=MARTE::HLAM::RtService_strategy)
def test_marte::hlam::rtservice_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original

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

@given(instance=MARTE::HLAM::RtAction_strategy)
@settings(max_examples=50)
def test_marte::hlam::rtaction_instantiation(instance):
    assert isinstance(instance, MARTE::HLAM::RtAction)

@given(instance=MARTE::HLAM::RtAction_strategy)
def test_marte::hlam::rtaction_isAtomic_type(instance):
    assert isinstance(instance.isAtomic, str)


@given(instance=MARTE::HLAM::RtAction_strategy)
def test_marte::hlam::rtaction_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original

@given(instance=MARTE::HLAM::RtAction_strategy)
def test_marte::hlam::rtaction_msgSize_type(instance):
    assert isinstance(instance.msgSize, str)


@given(instance=MARTE::HLAM::RtAction_strategy)
def test_marte::hlam::rtaction_msgSize_setter(instance):
    original = instance.msgSize
    instance.msgSize = original
    assert instance.msgSize == original

@given(instance=MARTE::HLAM::RtAction_strategy)
def test_marte::hlam::rtaction_synchKind_type(instance):
    assert isinstance(instance.synchKind, str)


@given(instance=MARTE::HLAM::RtAction_strategy)
def test_marte::hlam::rtaction_synchKind_setter(instance):
    original = instance.synchKind
    instance.synchKind = original
    assert instance.synchKind == original

@given(instance=HLAM::MARTE::Comment_strategy)
@settings(max_examples=50)
def test_hlam::marte::comment_instantiation(instance):
    assert isinstance(instance, HLAM::MARTE::Comment)

@given(instance=Time::TimedInstantObservation_strategy)
@settings(max_examples=50)
def test_time::timedinstantobservation_instantiation(instance):
    assert isinstance(instance, Time::TimedInstantObservation)

@given(instance=MARTE::HLAM::RtSpecification_strategy)
@settings(max_examples=50)
def test_marte::hlam::rtspecification_instantiation(instance):
    assert isinstance(instance, MARTE::HLAM::RtSpecification)

@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_boundDl_type(instance):
    assert isinstance(instance.boundDl, str)


@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_boundDl_setter(instance):
    original = instance.boundDl
    instance.boundDl = original
    assert instance.boundDl == original

@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_relDl_type(instance):
    assert isinstance(instance.relDl, str)


@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_relDl_setter(instance):
    original = instance.relDl
    instance.relDl = original
    assert instance.relDl == original

@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_utility_type(instance):
    assert isinstance(instance.utility, str)


@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_utility_setter(instance):
    original = instance.utility
    instance.utility = original
    assert instance.utility == original

@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_rdTime_type(instance):
    assert isinstance(instance.rdTime, str)


@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_rdTime_setter(instance):
    original = instance.rdTime
    instance.rdTime = original
    assert instance.rdTime == original

@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_absDl_type(instance):
    assert isinstance(instance.absDl, str)


@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_absDl_setter(instance):
    original = instance.absDl
    instance.absDl = original
    assert instance.absDl == original

@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_occKind_type(instance):
    assert isinstance(instance.occKind, str)


@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_occKind_setter(instance):
    original = instance.occKind
    instance.occKind = original
    assert instance.occKind == original

@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_miss_type(instance):
    assert isinstance(instance.miss, str)


@given(instance=MARTE::HLAM::RtSpecification_strategy)
def test_marte::hlam::rtspecification_miss_setter(instance):
    original = instance.miss
    instance.miss = original
    assert instance.miss == original

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
def test_marte::hlam::ppunit_memorySize_type(instance):
    assert isinstance(instance.memorySize, str)


@given(instance=MARTE::HLAM::PpUnit_strategy)
def test_marte::hlam::ppunit_memorySize_setter(instance):
    original = instance.memorySize
    instance.memorySize = original
    assert instance.memorySize == original

@given(instance=MARTE::HLAM::PpUnit_strategy)
def test_marte::hlam::ppunit_concPolicy_type(instance):
    assert isinstance(instance.concPolicy, str)


@given(instance=MARTE::HLAM::PpUnit_strategy)
def test_marte::hlam::ppunit_concPolicy_setter(instance):
    original = instance.concPolicy
    instance.concPolicy = original
    assert instance.concPolicy == original

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
def test_marte::hlam::rtunit_msgMaxSize_type(instance):
    assert isinstance(instance.msgMaxSize, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_msgMaxSize_setter(instance):
    original = instance.msgMaxSize
    instance.msgMaxSize = original
    assert instance.msgMaxSize == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_queueSchedPolicy_type(instance):
    assert isinstance(instance.queueSchedPolicy, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_queueSchedPolicy_setter(instance):
    original = instance.queueSchedPolicy
    instance.queueSchedPolicy = original
    assert instance.queueSchedPolicy == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_memorySize_type(instance):
    assert isinstance(instance.memorySize, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_memorySize_setter(instance):
    original = instance.memorySize
    instance.memorySize = original
    assert instance.memorySize == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_isMain_type(instance):
    assert isinstance(instance.isMain, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_isMain_setter(instance):
    original = instance.isMain
    instance.isMain = original
    assert instance.isMain == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_queueSize_type(instance):
    assert isinstance(instance.queueSize, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_queueSize_setter(instance):
    original = instance.queueSize
    instance.queueSize = original
    assert instance.queueSize == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_srPoolPolicy_type(instance):
    assert isinstance(instance.srPoolPolicy, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_srPoolPolicy_setter(instance):
    original = instance.srPoolPolicy
    instance.srPoolPolicy = original
    assert instance.srPoolPolicy == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_srPoolSize_type(instance):
    assert isinstance(instance.srPoolSize, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_srPoolSize_setter(instance):
    original = instance.srPoolSize
    instance.srPoolSize = original
    assert instance.srPoolSize == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_isDynamic_type(instance):
    assert isinstance(instance.isDynamic, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original

@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_srPoolWaitingTime_type(instance):
    assert isinstance(instance.srPoolWaitingTime, str)


@given(instance=MARTE::HLAM::RtUnit_strategy)
def test_marte::hlam::rtunit_srPoolWaitingTime_setter(instance):
    original = instance.srPoolWaitingTime
    instance.srPoolWaitingTime = original
    assert instance.srPoolWaitingTime == original

@given(instance=MARTE::DataTypes::TupleType_strategy)
@settings(max_examples=50)
def test_marte::datatypes::tupletype_instantiation(instance):
    assert isinstance(instance, MARTE::DataTypes::TupleType)

@given(instance=MARTE::DataTypes::ChoiceType_strategy)
@settings(max_examples=50)
def test_marte::datatypes::choicetype_instantiation(instance):
    assert isinstance(instance, MARTE::DataTypes::ChoiceType)

@given(instance=MARTE::DataTypes::CollectionType_strategy)
@settings(max_examples=50)
def test_marte::datatypes::collectiontype_instantiation(instance):
    assert isinstance(instance, MARTE::DataTypes::CollectionType)

@given(instance=HLAM::MARTE::BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_hlam::marte::behavioredclassifier_instantiation(instance):
    assert isinstance(instance, HLAM::MARTE::BehavioredClassifier)

@given(instance=MARTE::DataTypes::IntervalType_strategy)
@settings(max_examples=50)
def test_marte::datatypes::intervaltype_instantiation(instance):
    assert isinstance(instance, MARTE::DataTypes::IntervalType)

@given(instance=DataTypes::MARTE::DataType_strategy)
@settings(max_examples=50)
def test_datatypes::marte::datatype_instantiation(instance):
    assert isinstance(instance, DataTypes::MARTE::DataType)

@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
@settings(max_examples=50)
def test_marte::datatypes::boundedsubtype_instantiation(instance):
    assert isinstance(instance, MARTE::DataTypes::BoundedSubtype)

@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_isMaxOpen_type(instance):
    assert isinstance(instance.isMaxOpen, bool)


@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_isMaxOpen_setter(instance):
    original = instance.isMaxOpen
    instance.isMaxOpen = original
    assert instance.isMaxOpen == original

@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_maxValue_type(instance):
    assert isinstance(instance.maxValue, str)


@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original

@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_minValue_type(instance):
    assert isinstance(instance.minValue, str)


@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original

@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_isMinOpen_type(instance):
    assert isinstance(instance.isMinOpen, bool)


@given(instance=MARTE::DataTypes::BoundedSubtype_strategy)
def test_marte::datatypes::boundedsubtype_isMinOpen_setter(instance):
    original = instance.isMinOpen
    instance.isMinOpen = original
    assert instance.isMinOpen == original

@given(instance=Operators::MARTE::Behavior_strategy)
@settings(max_examples=50)
def test_operators::marte::behavior_instantiation(instance):
    assert isinstance(instance, Operators::MARTE::Behavior)

@given(instance=MARTE::Operators::Operator_strategy)
@settings(max_examples=50)
def test_marte::operators::operator_instantiation(instance):
    assert isinstance(instance, MARTE::Operators::Operator)

@given(instance=MARTE::Operators::Operator_strategy)
def test_marte::operators::operator_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=MARTE::Operators::Operator_strategy)
def test_marte::operators::operator_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=MARTE::Operators::Operator_strategy)
def test_marte::operators::operator_arity_type(instance):
    assert isinstance(instance.arity, str)


@given(instance=MARTE::Operators::Operator_strategy)
def test_marte::operators::operator_arity_setter(instance):
    original = instance.arity
    instance.arity = original
    assert instance.arity == original

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

@given(instance=MARTE::RSM::Shaped_strategy)
def test_marte::rsm::shaped_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=MARTE::RSM::Shaped_strategy)
def test_marte::rsm::shaped_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=DataTypes::MARTE::Property_strategy)
@settings(max_examples=50)
def test_datatypes::marte::property_instantiation(instance):
    assert isinstance(instance, DataTypes::MARTE::Property)

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

@given(instance=MARTE::RSM::Distribute_strategy)
@settings(max_examples=50)
def test_marte::rsm::distribute_instantiation(instance):
    assert isinstance(instance, MARTE::RSM::Distribute)

@given(instance=MARTE::RSM::Distribute_strategy)
def test_marte::rsm::distribute_repetitionSpace_type(instance):
    assert isinstance(instance.repetitionSpace, str)


@given(instance=MARTE::RSM::Distribute_strategy)
def test_marte::rsm::distribute_repetitionSpace_setter(instance):
    original = instance.repetitionSpace
    instance.repetitionSpace = original
    assert instance.repetitionSpace == original

@given(instance=MARTE::RSM::Distribute_strategy)
def test_marte::rsm::distribute_fromTiler_type(instance):
    assert isinstance(instance.fromTiler, str)


@given(instance=MARTE::RSM::Distribute_strategy)
def test_marte::rsm::distribute_fromTiler_setter(instance):
    original = instance.fromTiler
    instance.fromTiler = original
    assert instance.fromTiler == original

@given(instance=MARTE::RSM::Distribute_strategy)
def test_marte::rsm::distribute_toTiler_type(instance):
    assert isinstance(instance.toTiler, str)


@given(instance=MARTE::RSM::Distribute_strategy)
def test_marte::rsm::distribute_toTiler_setter(instance):
    original = instance.toTiler
    instance.toTiler = original
    assert instance.toTiler == original

@given(instance=MARTE::RSM::Distribute_strategy)
def test_marte::rsm::distribute_patternShape_type(instance):
    assert isinstance(instance.patternShape, str)


@given(instance=MARTE::RSM::Distribute_strategy)
def test_marte::rsm::distribute_patternShape_setter(instance):
    original = instance.patternShape
    instance.patternShape = original
    assert instance.patternShape == original

@given(instance=LinkTopology_strategy)
@settings(max_examples=50)
def test_linktopology_instantiation(instance):
    assert isinstance(instance, LinkTopology)

@given(instance=MARTE::RSM::Reshape_strategy)
@settings(max_examples=50)
def test_marte::rsm::reshape_instantiation(instance):
    assert isinstance(instance, MARTE::RSM::Reshape)

@given(instance=MARTE::RSM::Reshape_strategy)
def test_marte::rsm::reshape_patternShape_type(instance):
    assert isinstance(instance.patternShape, str)


@given(instance=MARTE::RSM::Reshape_strategy)
def test_marte::rsm::reshape_patternShape_setter(instance):
    original = instance.patternShape
    instance.patternShape = original
    assert instance.patternShape == original

@given(instance=MARTE::RSM::Reshape_strategy)
def test_marte::rsm::reshape_repetitonShape_type(instance):
    assert isinstance(instance.repetitonShape, str)


@given(instance=MARTE::RSM::Reshape_strategy)
def test_marte::rsm::reshape_repetitonShape_setter(instance):
    original = instance.repetitonShape
    instance.repetitonShape = original
    assert instance.repetitonShape == original

@given(instance=MARTE::RSM::InterRepetition_strategy)
@settings(max_examples=50)
def test_marte::rsm::interrepetition_instantiation(instance):
    assert isinstance(instance, MARTE::RSM::InterRepetition)

@given(instance=MARTE::RSM::InterRepetition_strategy)
def test_marte::rsm::interrepetition_repetitionShapeDependence_type(instance):
    assert isinstance(instance.repetitionShapeDependence, str)


@given(instance=MARTE::RSM::InterRepetition_strategy)
def test_marte::rsm::interrepetition_repetitionShapeDependence_setter(instance):
    original = instance.repetitionShapeDependence
    instance.repetitionShapeDependence = original
    assert instance.repetitionShapeDependence == original

@given(instance=MARTE::RSM::InterRepetition_strategy)
def test_marte::rsm::interrepetition_isModulo_type(instance):
    assert isinstance(instance.isModulo, str)


@given(instance=MARTE::RSM::InterRepetition_strategy)
def test_marte::rsm::interrepetition_isModulo_setter(instance):
    original = instance.isModulo
    instance.isModulo = original
    assert instance.isModulo == original

@given(instance=MARTE::RSM::Tiler_strategy)
@settings(max_examples=50)
def test_marte::rsm::tiler_instantiation(instance):
    assert isinstance(instance, MARTE::RSM::Tiler)

@given(instance=MARTE::RSM::Tiler_strategy)
def test_marte::rsm::tiler_fitting_type(instance):
    assert isinstance(instance.fitting, str)


@given(instance=MARTE::RSM::Tiler_strategy)
def test_marte::rsm::tiler_fitting_setter(instance):
    original = instance.fitting
    instance.fitting = original
    assert instance.fitting == original

@given(instance=MARTE::RSM::Tiler_strategy)
def test_marte::rsm::tiler_tiler_type(instance):
    assert isinstance(instance.tiler, str)


@given(instance=MARTE::RSM::Tiler_strategy)
def test_marte::rsm::tiler_tiler_setter(instance):
    original = instance.tiler
    instance.tiler = original
    assert instance.tiler == original

@given(instance=MARTE::RSM::Tiler_strategy)
def test_marte::rsm::tiler_paving_type(instance):
    assert isinstance(instance.paving, str)


@given(instance=MARTE::RSM::Tiler_strategy)
def test_marte::rsm::tiler_paving_setter(instance):
    original = instance.paving
    instance.paving = original
    assert instance.paving == original

@given(instance=MARTE::RSM::Tiler_strategy)
def test_marte::rsm::tiler_origin_type(instance):
    assert isinstance(instance.origin, str)


@given(instance=MARTE::RSM::Tiler_strategy)
def test_marte::rsm::tiler_origin_setter(instance):
    original = instance.origin
    instance.origin = original
    assert instance.origin == original

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

@given(instance=GRM::ResourceUsage_strategy)
@settings(max_examples=50)
def test_grm::resourceusage_instantiation(instance):
    assert isinstance(instance, GRM::ResourceUsage)

@given(instance=MARTE::GQAM::GaScenario_strategy)
@settings(max_examples=50)
def test_marte::gqam::gascenario_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaScenario)

@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_utilizationOnHost_type(instance):
    assert isinstance(instance.utilizationOnHost, str)


@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_utilizationOnHost_setter(instance):
    original = instance.utilizationOnHost
    instance.utilizationOnHost = original
    assert instance.utilizationOnHost == original

@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_interOccT_type(instance):
    assert isinstance(instance.interOccT, str)


@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_interOccT_setter(instance):
    original = instance.interOccT
    instance.interOccT = original
    assert instance.interOccT == original

@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_respT_type(instance):
    assert isinstance(instance.respT, str)


@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_respT_setter(instance):
    original = instance.respT
    instance.respT = original
    assert instance.respT == original

@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_utilization_type(instance):
    assert isinstance(instance.utilization, str)


@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original

@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_hostDemand_type(instance):
    assert isinstance(instance.hostDemand, str)


@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_hostDemand_setter(instance):
    original = instance.hostDemand
    instance.hostDemand = original
    assert instance.hostDemand == original

@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_hostDemandOps_type(instance):
    assert isinstance(instance.hostDemandOps, str)


@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_hostDemandOps_setter(instance):
    original = instance.hostDemandOps
    instance.hostDemandOps = original
    assert instance.hostDemandOps == original

@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_throughput_type(instance):
    assert isinstance(instance.throughput, str)


@given(instance=MARTE::GQAM::GaScenario_strategy)
def test_marte::gqam::gascenario_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original

@given(instance=GRM::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_grm::marte::namedelement_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::NamedElement)

@given(instance=RSM::MARTE::ConnectorEnd_strategy)
@settings(max_examples=50)
def test_rsm::marte::connectorend_instantiation(instance):
    assert isinstance(instance, RSM::MARTE::ConnectorEnd)

@given(instance=GrService_strategy)
@settings(max_examples=50)
def test_grservice_instantiation(instance):
    assert isinstance(instance, GrService)

@given(instance=MARTE::HwGeneral::HwResourceService_strategy)
@settings(max_examples=50)
def test_marte::hwgeneral::hwresourceservice_instantiation(instance):
    assert isinstance(instance, MARTE::HwGeneral::HwResourceService)

@given(instance=MARTE::HwGeneral::HwResourceService_strategy)
def test_marte::hwgeneral::hwresourceservice_dissipation_type(instance):
    assert isinstance(instance.dissipation, str)


@given(instance=MARTE::HwGeneral::HwResourceService_strategy)
def test_marte::hwgeneral::hwresourceservice_dissipation_setter(instance):
    original = instance.dissipation
    instance.dissipation = original
    assert instance.dissipation == original

@given(instance=MARTE::HwGeneral::HwResourceService_strategy)
def test_marte::hwgeneral::hwresourceservice_consumption_type(instance):
    assert isinstance(instance.consumption, str)


@given(instance=MARTE::HwGeneral::HwResourceService_strategy)
def test_marte::hwgeneral::hwresourceservice_consumption_setter(instance):
    original = instance.consumption
    instance.consumption = original
    assert instance.consumption == original

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

@given(instance=MARTE::GRM::TimerResource_strategy)
def test_marte::grm::timerresource_duration_type(instance):
    assert isinstance(instance.duration, str)


@given(instance=MARTE::GRM::TimerResource_strategy)
def test_marte::grm::timerresource_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=MARTE::GRM::ClockResource_strategy)
@settings(max_examples=50)
def test_marte::grm::clockresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::ClockResource)

@given(instance=MARTE::GRM::ResourceUsage_strategy)
@settings(max_examples=50)
def test_marte::grm::resourceusage_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::ResourceUsage)

@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_powerPeak_type(instance):
    assert isinstance(instance.powerPeak, str)


@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_powerPeak_setter(instance):
    original = instance.powerPeak
    instance.powerPeak = original
    assert instance.powerPeak == original

@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_execTime_type(instance):
    assert isinstance(instance.execTime, str)


@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_execTime_setter(instance):
    original = instance.execTime
    instance.execTime = original
    assert instance.execTime == original

@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_energy_type(instance):
    assert isinstance(instance.energy, str)


@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_energy_setter(instance):
    original = instance.energy
    instance.energy = original
    assert instance.energy == original

@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_usedMemory_type(instance):
    assert isinstance(instance.usedMemory, str)


@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_usedMemory_setter(instance):
    original = instance.usedMemory
    instance.usedMemory = original
    assert instance.usedMemory == original

@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_allocatedMemory_type(instance):
    assert isinstance(instance.allocatedMemory, str)


@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_allocatedMemory_setter(instance):
    original = instance.allocatedMemory
    instance.allocatedMemory = original
    assert instance.allocatedMemory == original

@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_msgSize_type(instance):
    assert isinstance(instance.msgSize, str)


@given(instance=MARTE::GRM::ResourceUsage_strategy)
def test_marte::grm::resourceusage_msgSize_setter(instance):
    original = instance.msgSize
    instance.msgSize = original
    assert instance.msgSize == original

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

@given(instance=ProcessingResource_strategy)
@settings(max_examples=50)
def test_processingresource_instantiation(instance):
    assert isinstance(instance, ProcessingResource)

@given(instance=MARTE::GRM::DeviceResource_strategy)
@settings(max_examples=50)
def test_marte::grm::deviceresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::DeviceResource)

@given(instance=MARTE::GRM::CommunicationMedia_strategy)
@settings(max_examples=50)
def test_marte::grm::communicationmedia_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::CommunicationMedia)

@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_capacity_type(instance):
    assert isinstance(instance.capacity, str)


@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_transmMode_type(instance):
    assert isinstance(instance.transmMode, str)


@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_transmMode_setter(instance):
    original = instance.transmMode
    instance.transmMode = original
    assert instance.transmMode == original

@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_blockT_type(instance):
    assert isinstance(instance.blockT, str)


@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_blockT_setter(instance):
    original = instance.blockT
    instance.blockT = original
    assert instance.blockT == original

@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_elementSize_type(instance):
    assert isinstance(instance.elementSize, str)


@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_elementSize_setter(instance):
    original = instance.elementSize
    instance.elementSize = original
    assert instance.elementSize == original

@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_packetT_type(instance):
    assert isinstance(instance.packetT, str)


@given(instance=MARTE::GRM::CommunicationMedia_strategy)
def test_marte::grm::communicationmedia_packetT_setter(instance):
    original = instance.packetT
    instance.packetT = original
    assert instance.packetT == original

@given(instance=MARTE::GRM::ComputingResource_strategy)
@settings(max_examples=50)
def test_marte::grm::computingresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::ComputingResource)

@given(instance=GRM::Scheduler_strategy)
@settings(max_examples=50)
def test_grm::scheduler_instantiation(instance):
    assert isinstance(instance, GRM::Scheduler)

@given(instance=MARTE::GQAM::GaCommHost_strategy)
@settings(max_examples=50)
def test_marte::gqam::gacommhost_instantiation(instance):
    assert isinstance(instance, MARTE::GQAM::GaCommHost)

@given(instance=MARTE::GQAM::GaCommHost_strategy)
def test_marte::gqam::gacommhost_throughput_type(instance):
    assert isinstance(instance.throughput, str)


@given(instance=MARTE::GQAM::GaCommHost_strategy)
def test_marte::gqam::gacommhost_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original

@given(instance=MARTE::GQAM::GaCommHost_strategy)
def test_marte::gqam::gacommhost_utilization_type(instance):
    assert isinstance(instance.utilization, str)


@given(instance=MARTE::GQAM::GaCommHost_strategy)
def test_marte::gqam::gacommhost_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original

@given(instance=GRM::SchedulableResource_strategy)
@settings(max_examples=50)
def test_grm::schedulableresource_instantiation(instance):
    assert isinstance(instance, GRM::SchedulableResource)

@given(instance=MARTE::SW::Concurrency::SwSchedulableResource_strategy)
@settings(max_examples=50)
def test_marte::sw::concurrency::swschedulableresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::Concurrency::SwSchedulableResource)

@given(instance=MARTE::SW::Concurrency::SwSchedulableResource_strategy)
def test_marte::sw::concurrency::swschedulableresource_isStaticSchedulingFeature_type(instance):
    assert isinstance(instance.isStaticSchedulingFeature, str)


@given(instance=MARTE::SW::Concurrency::SwSchedulableResource_strategy)
def test_marte::sw::concurrency::swschedulableresource_isStaticSchedulingFeature_setter(instance):
    original = instance.isStaticSchedulingFeature
    instance.isStaticSchedulingFeature = original
    assert instance.isStaticSchedulingFeature == original

@given(instance=MARTE::SW::Concurrency::SwSchedulableResource_strategy)
def test_marte::sw::concurrency::swschedulableresource_isPreemptable_type(instance):
    assert isinstance(instance.isPreemptable, str)


@given(instance=MARTE::SW::Concurrency::SwSchedulableResource_strategy)
def test_marte::sw::concurrency::swschedulableresource_isPreemptable_setter(instance):
    original = instance.isPreemptable
    instance.isPreemptable = original
    assert instance.isPreemptable == original

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

@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_throughput_type(instance):
    assert isinstance(instance.throughput, str)


@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original

@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_schedPriRange_type(instance):
    assert isinstance(instance.schedPriRange, str)


@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_schedPriRange_setter(instance):
    original = instance.schedPriRange
    instance.schedPriRange = original
    assert instance.schedPriRange == original

@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_cntxtSwT_type(instance):
    assert isinstance(instance.cntxtSwT, str)


@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_cntxtSwT_setter(instance):
    original = instance.cntxtSwT
    instance.cntxtSwT = original
    assert instance.cntxtSwT == original

@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_clockOvh_type(instance):
    assert isinstance(instance.clockOvh, str)


@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_clockOvh_setter(instance):
    original = instance.clockOvh
    instance.clockOvh = original
    assert instance.clockOvh == original

@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_utilization_type(instance):
    assert isinstance(instance.utilization, str)


@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original

@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_memSize_type(instance):
    assert isinstance(instance.memSize, str)


@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_memSize_setter(instance):
    original = instance.memSize
    instance.memSize = original
    assert instance.memSize == original

@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_commTxOvh_type(instance):
    assert isinstance(instance.commTxOvh, str)


@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_commTxOvh_setter(instance):
    original = instance.commTxOvh
    instance.commTxOvh = original
    assert instance.commTxOvh == original

@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_commRcvOvh_type(instance):
    assert isinstance(instance.commRcvOvh, str)


@given(instance=MARTE::GQAM::GaExecHost_strategy)
def test_marte::gqam::gaexechost_commRcvOvh_setter(instance):
    original = instance.commRcvOvh
    instance.commRcvOvh = original
    assert instance.commRcvOvh == original

@given(instance=MARTE::HwComputing::HwComputingResource_strategy)
@settings(max_examples=50)
def test_marte::hwcomputing::hwcomputingresource_instantiation(instance):
    assert isinstance(instance, MARTE::HwComputing::HwComputingResource)

@given(instance=MARTE::HwComputing::HwComputingResource_strategy)
def test_marte::hwcomputing::hwcomputingresource_op_Frequencies_type(instance):
    assert isinstance(instance.op_Frequencies, str)


@given(instance=MARTE::HwComputing::HwComputingResource_strategy)
def test_marte::hwcomputing::hwcomputingresource_op_Frequencies_setter(instance):
    original = instance.op_Frequencies
    instance.op_Frequencies = original
    assert instance.op_Frequencies == original

@given(instance=GRM::ProcessingResource_strategy)
@settings(max_examples=50)
def test_grm::processingresource_instantiation(instance):
    assert isinstance(instance, GRM::ProcessingResource)

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=MARTE::SW::ResourceCore::SwResource_strategy)
@settings(max_examples=50)
def test_marte::sw::resourcecore::swresource_instantiation(instance):
    assert isinstance(instance, MARTE::SW::ResourceCore::SwResource)

@given(instance=MARTE::GRM::ProcessingResource_strategy)
@settings(max_examples=50)
def test_marte::grm::processingresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::ProcessingResource)

@given(instance=MARTE::GRM::ProcessingResource_strategy)
def test_marte::grm::processingresource_speedFactor_type(instance):
    assert isinstance(instance.speedFactor, str)


@given(instance=MARTE::GRM::ProcessingResource_strategy)
def test_marte::grm::processingresource_speedFactor_setter(instance):
    original = instance.speedFactor
    instance.speedFactor = original
    assert instance.speedFactor == original

@given(instance=MARTE::GRM::CommunicationEndPoint_strategy)
@settings(max_examples=50)
def test_marte::grm::communicationendpoint_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::CommunicationEndPoint)

@given(instance=MARTE::GRM::CommunicationEndPoint_strategy)
def test_marte::grm::communicationendpoint_packetSize_type(instance):
    assert isinstance(instance.packetSize, str)


@given(instance=MARTE::GRM::CommunicationEndPoint_strategy)
def test_marte::grm::communicationendpoint_packetSize_setter(instance):
    original = instance.packetSize
    instance.packetSize = original
    assert instance.packetSize == original

@given(instance=MARTE::PAM::PaLogicalResource_strategy)
@settings(max_examples=50)
def test_marte::pam::palogicalresource_instantiation(instance):
    assert isinstance(instance, MARTE::PAM::PaLogicalResource)

@given(instance=MARTE::PAM::PaLogicalResource_strategy)
def test_marte::pam::palogicalresource_poolSize_type(instance):
    assert isinstance(instance.poolSize, str)


@given(instance=MARTE::PAM::PaLogicalResource_strategy)
def test_marte::pam::palogicalresource_poolSize_setter(instance):
    original = instance.poolSize
    instance.poolSize = original
    assert instance.poolSize == original

@given(instance=MARTE::PAM::PaLogicalResource_strategy)
def test_marte::pam::palogicalresource_throughput_type(instance):
    assert isinstance(instance.throughput, str)


@given(instance=MARTE::PAM::PaLogicalResource_strategy)
def test_marte::pam::palogicalresource_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original

@given(instance=MARTE::PAM::PaLogicalResource_strategy)
def test_marte::pam::palogicalresource_utilization_type(instance):
    assert isinstance(instance.utilization, str)


@given(instance=MARTE::PAM::PaLogicalResource_strategy)
def test_marte::pam::palogicalresource_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original

@given(instance=MARTE::GRM::SchedulableResource_strategy)
@settings(max_examples=50)
def test_marte::grm::schedulableresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::SchedulableResource)

@given(instance=MARTE::GRM::SchedulableResource_strategy)
def test_marte::grm::schedulableresource_schedParams_type(instance):
    assert isinstance(instance.schedParams, str)


@given(instance=MARTE::GRM::SchedulableResource_strategy)
def test_marte::grm::schedulableresource_schedParams_setter(instance):
    original = instance.schedParams
    instance.schedParams = original
    assert instance.schedParams == original

@given(instance=MARTE::GRM::MutualExclusionResource_strategy)
@settings(max_examples=50)
def test_marte::grm::mutualexclusionresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::MutualExclusionResource)

@given(instance=MARTE::GRM::MutualExclusionResource_strategy)
def test_marte::grm::mutualexclusionresource_ceiling_type(instance):
    assert isinstance(instance.ceiling, str)


@given(instance=MARTE::GRM::MutualExclusionResource_strategy)
def test_marte::grm::mutualexclusionresource_ceiling_setter(instance):
    original = instance.ceiling
    instance.ceiling = original
    assert instance.ceiling == original

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

@given(instance=MARTE::GRM::TimingResource_strategy)
@settings(max_examples=50)
def test_marte::grm::timingresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::TimingResource)

@given(instance=MARTE::GRM::ConcurrencyResource_strategy)
@settings(max_examples=50)
def test_marte::grm::concurrencyresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::ConcurrencyResource)

@given(instance=MARTE::GRM::SynchronizationResource_strategy)
@settings(max_examples=50)
def test_marte::grm::synchronizationresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::SynchronizationResource)

@given(instance=MARTE::GRM::Scheduler_strategy)
@settings(max_examples=50)
def test_marte::grm::scheduler_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::Scheduler)

@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_otherSchedPolicy_type(instance):
    assert isinstance(instance.otherSchedPolicy, str)


@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_otherSchedPolicy_setter(instance):
    original = instance.otherSchedPolicy
    instance.otherSchedPolicy = original
    assert instance.otherSchedPolicy == original

@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_isPreemptible_type(instance):
    assert isinstance(instance.isPreemptible, str)


@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_isPreemptible_setter(instance):
    original = instance.isPreemptible
    instance.isPreemptible = original
    assert instance.isPreemptible == original

@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_schedule_type(instance):
    assert isinstance(instance.schedule, str)


@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_schedule_setter(instance):
    original = instance.schedule
    instance.schedule = original
    assert instance.schedule == original

@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_schedPolicy_type(instance):
    assert isinstance(instance.schedPolicy, str)


@given(instance=MARTE::GRM::Scheduler_strategy)
def test_marte::grm::scheduler_schedPolicy_setter(instance):
    original = instance.schedPolicy
    instance.schedPolicy = original
    assert instance.schedPolicy == original

@given(instance=MARTE::HwGeneral::HwResource_strategy)
@settings(max_examples=50)
def test_marte::hwgeneral::hwresource_instantiation(instance):
    assert isinstance(instance, MARTE::HwGeneral::HwResource)

@given(instance=MARTE::HwGeneral::HwResource_strategy)
def test_marte::hwgeneral::hwresource_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=MARTE::HwGeneral::HwResource_strategy)
def test_marte::hwgeneral::hwresource_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=MARTE::HwGeneral::HwResource_strategy)
def test_marte::hwgeneral::hwresource_frequency_type(instance):
    assert isinstance(instance.frequency, str)


@given(instance=MARTE::HwGeneral::HwResource_strategy)
def test_marte::hwgeneral::hwresource_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original

@given(instance=MARTE::GRM::StorageResource_strategy)
@settings(max_examples=50)
def test_marte::grm::storageresource_instantiation(instance):
    assert isinstance(instance, MARTE::GRM::StorageResource)

@given(instance=MARTE::GRM::StorageResource_strategy)
def test_marte::grm::storageresource_elementSize_type(instance):
    assert isinstance(instance.elementSize, str)


@given(instance=MARTE::GRM::StorageResource_strategy)
def test_marte::grm::storageresource_elementSize_setter(instance):
    original = instance.elementSize
    instance.elementSize = original
    assert instance.elementSize == original

@given(instance=GRM::MARTE::Lifeline_strategy)
@settings(max_examples=50)
def test_grm::marte::lifeline_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::Lifeline)

@given(instance=GRM::MARTE::Classifier_strategy)
@settings(max_examples=50)
def test_grm::marte::classifier_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::Classifier)

@given(instance=GRM::MARTE::InstanceSpecification_strategy)
@settings(max_examples=50)
def test_grm::marte::instancespecification_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::InstanceSpecification)

@given(instance=GRM::MARTE::Property_strategy)
@settings(max_examples=50)
def test_grm::marte::property_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::Property)

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

@given(instance=MARTE::GRM::Resource_strategy)
def test_marte::grm::resource_isActive_type(instance):
    assert isinstance(instance.isActive, str)


@given(instance=MARTE::GRM::Resource_strategy)
def test_marte::grm::resource_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=MARTE::GRM::Resource_strategy)
def test_marte::grm::resource_resMult_type(instance):
    assert isinstance(instance.resMult, str)


@given(instance=MARTE::GRM::Resource_strategy)
def test_marte::grm::resource_resMult_setter(instance):
    original = instance.resMult
    instance.resMult = original
    assert instance.resMult == original

@given(instance=Time::MARTE::Message_strategy)
@settings(max_examples=50)
def test_time::marte::message_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Message)

@given(instance=Time::MARTE::Behavior_strategy)
@settings(max_examples=50)
def test_time::marte::behavior_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Behavior)

@given(instance=GRM::MARTE::ConnectableElement_strategy)
@settings(max_examples=50)
def test_grm::marte::connectableelement_instantiation(instance):
    assert isinstance(instance, GRM::MARTE::ConnectableElement)

@given(instance=Time::MARTE::Action_strategy)
@settings(max_examples=50)
def test_time::marte::action_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Action)

@given(instance=Time::MARTE::TimeEvent_strategy)
@settings(max_examples=50)
def test_time::marte::timeevent_instantiation(instance):
    assert isinstance(instance, Time::MARTE::TimeEvent)

@given(instance=Time::MARTE::DurationObservation_strategy)
@settings(max_examples=50)
def test_time::marte::durationobservation_instantiation(instance):
    assert isinstance(instance, Time::MARTE::DurationObservation)

@given(instance=Time::MARTE::TimeObservation_strategy)
@settings(max_examples=50)
def test_time::marte::timeobservation_instantiation(instance):
    assert isinstance(instance, Time::MARTE::TimeObservation)

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

@given(instance=MARTE::Time::TimedProcessing_strategy)
@settings(max_examples=50)
def test_marte::time::timedprocessing_instantiation(instance):
    assert isinstance(instance, MARTE::Time::TimedProcessing)

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

@given(instance=Time::MARTE::Operation_strategy)
@settings(max_examples=50)
def test_time::marte::operation_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Operation)

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

@given(instance=Time::MARTE::Event_strategy)
@settings(max_examples=50)
def test_time::marte::event_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Event)

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

@given(instance=Time::MARTE::Enumeration_strategy)
@settings(max_examples=50)
def test_time::marte::enumeration_instantiation(instance):
    assert isinstance(instance, Time::MARTE::Enumeration)

@given(instance=Alloc::MARTE::Comment_strategy)
@settings(max_examples=50)
def test_alloc::marte::comment_instantiation(instance):
    assert isinstance(instance, Alloc::MARTE::Comment)

@given(instance=Alloc::MARTE::Element_strategy)
@settings(max_examples=50)
def test_alloc::marte::element_instantiation(instance):
    assert isinstance(instance, Alloc::MARTE::Element)

@given(instance=MARTE::Alloc::Assign_strategy)
@settings(max_examples=50)
def test_marte::alloc::assign_instantiation(instance):
    assert isinstance(instance, MARTE::Alloc::Assign)

@given(instance=MARTE::Alloc::Assign_strategy)
def test_marte::alloc::assign_nature_type(instance):
    assert isinstance(instance.nature, str)


@given(instance=MARTE::Alloc::Assign_strategy)
def test_marte::alloc::assign_nature_setter(instance):
    original = instance.nature
    instance.nature = original
    assert instance.nature == original

@given(instance=MARTE::Alloc::Assign_strategy)
def test_marte::alloc::assign_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::Alloc::Assign_strategy)
def test_marte::alloc::assign_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=NFPs::NfpConstraint_strategy)
@settings(max_examples=50)
def test_nfps::nfpconstraint_instantiation(instance):
    assert isinstance(instance, NFPs::NfpConstraint)

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

@given(instance=MARTE::Time::ClockConstraint_strategy)
@settings(max_examples=50)
def test_marte::time::clockconstraint_instantiation(instance):
    assert isinstance(instance, MARTE::Time::ClockConstraint)

@given(instance=MARTE::Time::ClockConstraint_strategy)
def test_marte::time::clockconstraint_isPrecedenceBased_type(instance):
    assert isinstance(instance.isPrecedenceBased, bool)


@given(instance=MARTE::Time::ClockConstraint_strategy)
def test_marte::time::clockconstraint_isPrecedenceBased_setter(instance):
    original = instance.isPrecedenceBased
    instance.isPrecedenceBased = original
    assert instance.isPrecedenceBased == original

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

@given(instance=MARTE::Alloc::Allocate_strategy)
@settings(max_examples=50)
def test_marte::alloc::allocate_instantiation(instance):
    assert isinstance(instance, MARTE::Alloc::Allocate)

@given(instance=MARTE::Alloc::Allocate_strategy)
def test_marte::alloc::allocate_nature_type(instance):
    assert isinstance(instance.nature, str)


@given(instance=MARTE::Alloc::Allocate_strategy)
def test_marte::alloc::allocate_nature_setter(instance):
    original = instance.nature
    instance.nature = original
    assert instance.nature == original

@given(instance=MARTE::Alloc::Allocate_strategy)
def test_marte::alloc::allocate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::Alloc::Allocate_strategy)
def test_marte::alloc::allocate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MARTE::Alloc::NfpRefine_strategy)
@settings(max_examples=50)
def test_marte::alloc::nfprefine_instantiation(instance):
    assert isinstance(instance, MARTE::Alloc::NfpRefine)

@given(instance=Alloc::Allocated_strategy)
@settings(max_examples=50)
def test_alloc::allocated_instantiation(instance):
    assert isinstance(instance, Alloc::Allocated)

@given(instance=Alloc::MARTE::ActivityPartition_strategy)
@settings(max_examples=50)
def test_alloc::marte::activitypartition_instantiation(instance):
    assert isinstance(instance, Alloc::MARTE::ActivityPartition)

@given(instance=MARTE::Alloc::AllocateActivityGroup_strategy)
@settings(max_examples=50)
def test_marte::alloc::allocateactivitygroup_instantiation(instance):
    assert isinstance(instance, MARTE::Alloc::AllocateActivityGroup)

@given(instance=MARTE::Alloc::AllocateActivityGroup_strategy)
def test_marte::alloc::allocateactivitygroup_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=MARTE::Alloc::AllocateActivityGroup_strategy)
def test_marte::alloc::allocateactivitygroup_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=Alloc::MARTE::Dependency_strategy)
@settings(max_examples=50)
def test_alloc::marte::dependency_instantiation(instance):
    assert isinstance(instance, Alloc::MARTE::Dependency)

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

@given(instance=Alloc::MARTE::NamedElement_strategy)
@settings(max_examples=50)
def test_alloc::marte::namedelement_instantiation(instance):
    assert isinstance(instance, Alloc::MARTE::NamedElement)

@given(instance=MARTE::Alloc::Allocated_strategy)
@settings(max_examples=50)
def test_marte::alloc::allocated_instantiation(instance):
    assert isinstance(instance, MARTE::Alloc::Allocated)

@given(instance=MARTE::Alloc::Allocated_strategy)
def test_marte::alloc::allocated_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::Alloc::Allocated_strategy)
def test_marte::alloc::allocated_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CoreElements::MARTE::State_strategy)
@settings(max_examples=50)
def test_coreelements::marte::state_instantiation(instance):
    assert isinstance(instance, CoreElements::MARTE::State)

@given(instance=MARTE::CoreElements::Mode_strategy)
@settings(max_examples=50)
def test_marte::coreelements::mode_instantiation(instance):
    assert isinstance(instance, MARTE::CoreElements::Mode)

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

@given(instance=CoreElements::MARTE::Transition_strategy)
@settings(max_examples=50)
def test_coreelements::marte::transition_instantiation(instance):
    assert isinstance(instance, CoreElements::MARTE::Transition)

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
def test_marte::nfps::dimension_baseExponent_type(instance):
    assert isinstance(instance.baseExponent, int)


@given(instance=MARTE::NFPs::Dimension_strategy)
def test_marte::nfps::dimension_baseExponent_setter(instance):
    original = instance.baseExponent
    instance.baseExponent = original
    assert instance.baseExponent == original

@given(instance=MARTE::NFPs::Dimension_strategy)
def test_marte::nfps::dimension_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=MARTE::NFPs::Dimension_strategy)
def test_marte::nfps::dimension_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

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
def test_marte::nfps::unit_convOffset_type(instance):
    assert isinstance(instance.convOffset, str)


@given(instance=MARTE::NFPs::Unit_strategy)
def test_marte::nfps::unit_convOffset_setter(instance):
    original = instance.convOffset
    instance.convOffset = original
    assert instance.convOffset == original

@given(instance=NFPs::MARTE::Property_strategy)
@settings(max_examples=50)
def test_nfps::marte::property_instantiation(instance):
    assert isinstance(instance, NFPs::MARTE::Property)
