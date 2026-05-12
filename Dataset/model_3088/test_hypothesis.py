import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GQAM_GaCommStep,
    PAM_PaStep,
    MARTE_PAM_PaCommStep,
    PAM_MARTE_NamedElement,
    MARTE_PAM_PaRunTInstance,
    GaExecHost,
    MARTE_SAM_SaExecHost,
    GaCommHost,
    MARTE_SAM_SaCommHost,
    MutualExclusionResource,
    GRM_SecondaryScheduler,
    ProcessingResource,
    MARTE_GRM_ComputingResource,
    GRM_Scheduler,
    GRM_SchedulableResource,
    GRM_MutualExclusionResource,
    GRM_ComputingResource,
    GRM_ProcessingResource,
    Resource,
    MARTE_PAM_PaLogicalResource,
    MARTE_GRM_SynchronizationResource,
    MARTE_GRM_ConcurrencyResource,
    MARTE_GRM_Scheduler,
    MARTE_GRM_SchedulableResource,
    MARTE_GRM_CommunicationEndPoint,
    MARTE_GRM_ProcessingResource,
    MARTE_GRM_MutualExclusionResource,
    MARTE_GRM_StorageResource,
    GRM_MARTE_Lifeline,
    GRM_MARTE_Classifier,
    GRM_MARTE_InstanceSpecification,
    GRM_MARTE_Property,
    MARTE_GRM_Resource,
    Time_MARTE_Message,
    Time_MARTE_Behavior,
    GRM_MARTE_ConnectableElement,
    Time_MARTE_Action,
    Time_MARTE_TimeEvent,
    Time_MARTE_DurationObservation,
    Time_MARTE_TimeObservation,
    Time_TimedElement,
    Time_MARTE_ValueSpecification,
    TimedElement,
    MARTE_Time_TimedProcessing,
    MARTE_Time_TimedEvent,
    MARTE_Time_TimedDurationObservation,
    MARTE_Time_TimedInstantObservation,
    MARTE_Time_TimedValueSpecification,
    Time_Clock,
    MARTE_Time_TimedElement,
    Time_MARTE_Class,
    Time_MARTE_Operation,
    MARTE_Time_ClockType,
    Time_MARTE_Event,
    Time_MARTE_Property,
    Time_ClockType,
    Time_MARTE_InstanceSpecification,
    MARTE_Time_Clock,
    Time_MARTE_Namespace,
    MARTE_Time_TimedDomain,
    Alloc_MARTE_Abstraction,
    Time_MARTE_Enumeration,
    Alloc_MARTE_Comment,
    Alloc_MARTE_Element,
    MARTE_Alloc_Assign,
    NFPs_NfpConstraint,
    MARTE_Time_TimedConstraint,
    MARTE_Time_ClockConstraint,
    MARTE_Alloc_Allocate,
    MARTE_Alloc_NfpRefine,
    Alloc_Allocated,
    Alloc_MARTE_ActivityPartition,
    MARTE_Alloc_AllocateActivityGroup,
    Alloc_MARTE_Dependency,
    TupleType,
    MARTE_NFPs_NfpType,
    CoreElements_Mode,
    Alloc_MARTE_NamedElement,
    MARTE_SAM_SaSharedResource,
    SAM_SaSharedResource,
    SAM_MARTE_BehavioralFeature,
    MARTE_SAM_SaEndtoEndFlow,
    GaAnalysisContext,
    MARTE_SAM_SaAnalysisContext,
    GQAM_MARTE_Classifier,
    MARTE_GQAM_GaResourcesPlatform,
    GQAM_GaResourcesPlatform,
    GQAM_GaWorkloadBehavior,
    Variables_ExpressionContext,
    CoreElements_Configuration,
    MARTE_GQAM_GaAnalysisContext,
    GaCommStep,
    MARTE_SAM_SaCommStep,
    SAM_MARTE_NamedElement,
    MARTE_GQAM_GaWorkloadBehavior,
    SchedulableResource,
    MARTE_GQAM_GaCommChannel,
    GaTimedObs,
    MARTE_SAM_SaSchedObs,
    MARTE_GQAM_GaLatencyObs,
    GQAM_MARTE_TimeObservation,
    NfpConstraint,
    MARTE_GQAM_GaTimedObs,
    GQAM_MARTE_Operation,
    GaStep,
    MARTE_PAM_PaResPassStep,
    MARTE_GQAM_GaCommStep,
    MARTE_PAM_PaStep,
    MARTE_GQAM_GaAcqStep,
    MARTE_GQAM_GaRelStep,
    MARTE_SAM_SaStep,
    MARTE_GQAM_GaRequestedService,
    MARTE_GQAM_GaExecHost,
    GQAM_GaExecHost,
    GaScenario,
    MARTE_GQAM_GaStep,
    GQAM_GaTimedObs,
    GQAM_GaRequestedService,
    MARTE_PAM_PaRequestedStep,
    GQAM_GaWorkloadEvent,
    Time_TimedProcessing,
    GQAM_MARTE_TimeEvent,
    GQAM_GaScenario,
    GQAM_GaEventTrace,
    GQAM_GaWorkloadGenerator,
    MARTE_GQAM_GaWorkloadEvent,
    GQAM_MARTE_NamedElement,
    GQAM_GaStep,
    MARTE_GQAM_GaWorkloadGenerator,
    MARTE_GCM_GCMInvocatingBehavior,
    GCM_MARTE_Behavior,
    MARTE_GCM_DataPool,
    GCM_MARTE_Classifier,
    GCM_MARTE_AnyReceiveEvent,
    MARTE_GCM_DataEvent,
    GCM_MARTE_InvocationAction,
    MARTE_GCM_GCMInvocationAction,
    GCM_MARTE_Feature,
    MARTE_GQAM_GaEventTrace,
    GQAM_MARTE_Behavior,
    GCM_MARTE_BehavioralFeature,
    MARTE_GCM_ClientServerFeature,
    MARTE_GCM_FlowSpecification,
    MARTE_GCM_ClientServerSpecification,
    GCM_ClientServerSpecification,
    GCM_MARTE_Interface,
    MARTE_GCM_ClientServerPort,
    GCM_MARTE_Port,
    MARTE_GCM_FlowPort,
    GCM_MARTE_Trigger,
    MARTE_GCM_GCMTrigger,
    MARTE_GCM_FlowProperty,
    SW_Interaction_SwSynchronizationResource,
    MARTE_SW_Interaction_SwMutualExclusionResource,
    SwSynchronizationResource,
    MARTE_SW_Interaction_NotificationResource,
    GCM_MARTE_Property,
    SW_Interaction_MARTE_BehavioralFeature,
    SwCommunicationResource,
    MARTE_SW_Interaction_MessageComResource,
    MARTE_SW_Interaction_SharedDataComResource,
    GRM_SynchronizationResource,
    SW_Interaction_SwInteractionResource,
    MARTE_SW_Interaction_SwSynchronizationResource,
    SW_Interaction_MARTE_TypedElement,
    SW_Brokering_MARTE_BehavioralFeature,
    SW_Brokering_MARTE_TypedElement,
    InterruptResource,
    MARTE_SW_Concurrency_Alarm,
    SW_Concurrency_MARTE_Namespace,
    TimerResource,
    MARTE_SW_Concurrency_SwTimerResource,
    SW_Concurrency_MARTE_NamedElement,
    SW_Concurrency_SwConcurrentResource,
    MARTE_SW_Concurrency_SwSchedulableResource,
    SwConcurrentResource,
    MARTE_SW_Concurrency_InterruptResource,
    SW_Concurrency_MARTE_Element,
    SwResource,
    MARTE_SW_Interaction_SwInteractionResource,
    MARTE_SW_Brokering_MemoryBroker,
    MARTE_SW_Brokering_DeviceBroker,
    MARTE_SW_Concurrency_MemoryPartition,
    MARTE_SW_Concurrency_SwConcurrentResource,
    SW_Concurrency_MARTE_BehavioralFeature,
    SW_ResourceCore_MARTE_Property,
    SW_ResourceCore_MARTE_BehavioralFeature,
    SW_ResourceCore_MARTE_TypedElement,
    SW_Concurrency_MARTE_TypedElement,
    HwComponent,
    MARTE_HwPower_HwCoolingSupply,
    MARTE_HwPower_HwPowerSupply,
    HwLayout_HwComponent,
    MARTE_SW_ResourceCore_SwResource,
    HwCommunication_HwEndPoint,
    HwGeneral_HwResourceService,
    MARTE_HwGeneral_HwResource,
    HwI_O,
    MARTE_HwDevice_HWSensor,
    MARTE_HwDevice_HWActuator,
    HwTiming_HwClock,
    HwTimingResource,
    MARTE_HwTiming_HwTimer,
    MARTE_HwTiming_HwClock,
    GRM_TimingResource,
    HwDevice,
    MARTE_HwDevice_HwSupport,
    MARTE_HwDevice_HwI_O,
    GRM_DeviceResource,
    HwMemory,
    MARTE_HwMemory_HwROM,
    MARTE_HwMemory_HwDrive,
    MARTE_HwMemory_HwCache,
    MARTE_HwMemory_HwRAM,
    HwComputing_HwProcessor,
    HwStorageManager_HwStorageManager,
    HwMemory_HwMemory,
    GRM_StorageResource,
    GRM_CommunicationEndPoint,
    HwMedia,
    MARTE_HwCommunication_HwBridge,
    MARTE_HwCommunication_HwBus,
    HwCommunication_HwArbiter,
    MARTE_HwStorageManager_HwDMA,
    HwCommunication_HwCommunicationResource,
    MARTE_HwCommunication_HwEndPoint,
    GRM_CommunicationMedia,
    MARTE_GQAM_GaCommHost,
    MARTE_SW_Interaction_SwCommunicationResource,
    MARTE_HwCommunication_HwMedia,
    HwStorageManager,
    MARTE_HwStorageManager_HwMMU,
    HwComputing_HwComputingResource,
    HwMemory_HwRAM,
    HwResource,
    MARTE_HwComputing_HwBranchPredictor,
    MARTE_HwLayout_HwComponent,
    MARTE_HwCommunication_HwCommunicationResource,
    MARTE_HwComputing_HwISA,
    HwGeneral_HwResource,
    MARTE_HwMemory_HwMemory,
    MARTE_HwStorageManager_HwStorageManager,
    MARTE_HwDevice_HwDevice,
    MARTE_HwTiming_HwTimingResource,
    MARTE_HwComputing_HwComputingResource,
    HwCommunication_HwMedia,
    HwCommunicationResource,
    MARTE_HwCommunication_HwArbiter,
    HwMemory_HwCache,
    HwComputing_HwBranchPredictor,
    HwComputing_HwISA,
    HwComputingResource,
    MARTE_HwComputing_HwPLD,
    MARTE_HwComputing_HwASIC,
    MARTE_HwComputing_HwProcessor,
    HwStorageManager_HwMMU,
    MARTE_HLAM_RtService,
    MARTE_HLAM_RtAction,
    HLAM_MARTE_Comment,
    Time_TimedInstantObservation,
    MARTE_HLAM_RtSpecification,
    HLAM_RtSpecification,
    HLAM_MARTE_InvocationAction,
    HLAM_MARTE_Port,
    HLAM_MARTE_Signal,
    HLAM_MARTE_Message,
    HLAM_MARTE_BehavioralFeature,
    MARTE_HLAM_RtFeature,
    MARTE_HLAM_PpUnit,
    HLAM_MARTE_Operation,
    HLAM_MARTE_Behavior,
    MARTE_HLAM_RtUnit,
    MARTE_DataTypes_TupleType,
    MARTE_DataTypes_ChoiceType,
    MARTE_DataTypes_CollectionType,
    HLAM_MARTE_BehavioredClassifier,
    MARTE_DataTypes_IntervalType,
    DataTypes_MARTE_DataType,
    MARTE_DataTypes_BoundedSubtype,
    Operators_MARTE_Behavior,
    MARTE_Operators_Operator,
    Variables_MARTE_NamedElement,
    MARTE_Variables_ExpressionContext,
    Variables_MARTE_Property,
    MARTE_Variables_Var,
    RSM_MARTE_MultiplicityElement,
    MARTE_RSM_Shaped,
    DataTypes_MARTE_Property,
    Allocate,
    MARTE_SW_Concurrency_EntryPoint,
    MARTE_RSM_Distribute,
    LinkTopology,
    MARTE_RSM_Tiler,
    MARTE_RSM_InterRepetition,
    MARTE_RSM_Reshape,
    MARTE_RSM_DefaultLink,
    RSM_MARTE_Connector,
    MARTE_RSM_LinkTopology,
    GRM_ResourceUsage,
    MARTE_GQAM_GaScenario,
    GRM_MARTE_NamedElement,
    RSM_MARTE_ConnectorEnd,
    GrService,
    MARTE_HwGeneral_HwResourceService,
    MARTE_SW_ResourceCore_SwAccessService,
    MARTE_GRM_Acquire,
    MARTE_GRM_Release,
    GRM_MARTE_CollaborationUse,
    GRM_MARTE_Collaboration,
    GRM_MARTE_Behavior,
    GRM_MARTE_BehavioralFeature,
    GRM_MARTE_ExecutionSpecification,
    GRM_Resource,
    MARTE_GRM_GrService,
    TimingResource,
    MARTE_GRM_TimerResource,
    MARTE_GRM_ClockResource,
    MARTE_GRM_TimingResource,
    MARTE_GRM_DeviceResource,
    MARTE_GRM_ResourceUsage,
    GRM_MARTE_Connector,
    MARTE_GRM_CommunicationMedia,
    Scheduler,
    MARTE_GRM_SecondaryScheduler,
    MARTE_Alloc_Allocated,
    CoreElements_MARTE_State,
    MARTE_CoreElements_Mode,
    CoreElements_MARTE_Package,
    CoreElements_MARTE_StructuredClassifier,
    MARTE_CoreElements_Configuration,
    CoreElements_MARTE_StateMachine,
    MARTE_CoreElements_ModeBehavior,
    CoreElements_MARTE_Transition,
    MARTE_CoreElements_ModeTransition,
    NFPs_MARTE_Enumeration,
    NFPs_Dimension,
    MARTE_NFPs_Dimension,
    NFPs_MARTE_Constraint,
    MARTE_NFPs_NfpConstraint,
    NFPs_MARTE_EnumerationLiteral,
    NFPs_Unit,
    MARTE_NFPs_Unit,
    NFPs_MARTE_Property,
    MARTE_NFPs_Nfp,
    MessageResourceKind,
    Repl_Policy,
    OptimallityCriterionKind,
    MutualExclusionResourceKind,
    NotificationKind,
    AssignmentNature,
    PortSpecificationKind,
    CacheType,
    LaxityKind,
    dummy,
    ComponentState,
    ConcurrentAccessProtocolKind,
    ROM_Type,
    ISA_Type,
    AllocationKind,
    AllocationEndKind,
    PLD_Technology,
    FlowDirectionKind,
    PLD_Class,
    AllocationNature,
    ExecutionKind,
    VariableDirectionKind,
    SynchronizationKind,
    InterruptKind,
    DataPoolOrderingKind,
    NotificationResourceKind,
    AssignmentKind,
    CallConcurrencyKind,
    WritePolicy,
    PoolMgtPolicyKind,
    ConstraintKind,
    ConditionType,
    ClientServerKind,
    ComponentKind,
    QueuePolicyKind,
    AccessPolicyKind,
    ConcurrencyKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gqam_gacommstep_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaCommStep)


def test_gqam_gacommstep_constructor_exists():
    assert callable(GQAM_GaCommStep.__init__)


def test_gqam_gacommstep_constructor_args():
    sig = inspect.signature(GQAM_GaCommStep.__init__)
    params = list(sig.parameters.keys())



def test_pam_pastep_is_not_abstract():
    assert not inspect.isabstract(PAM_PaStep)


def test_pam_pastep_constructor_exists():
    assert callable(PAM_PaStep.__init__)


def test_pam_pastep_constructor_args():
    sig = inspect.signature(PAM_PaStep.__init__)
    params = list(sig.parameters.keys())



def test_marte_pam_pacommstep_is_not_abstract():
    assert not inspect.isabstract(MARTE_PAM_PaCommStep)


def test_marte_pam_pacommstep_constructor_exists():
    assert callable(MARTE_PAM_PaCommStep.__init__)


def test_marte_pam_pacommstep_constructor_args():
    sig = inspect.signature(MARTE_PAM_PaCommStep.__init__)
    params = list(sig.parameters.keys())



def test_pam_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(PAM_MARTE_NamedElement)


def test_pam_marte_namedelement_constructor_exists():
    assert callable(PAM_MARTE_NamedElement.__init__)


def test_pam_marte_namedelement_constructor_args():
    sig = inspect.signature(PAM_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte_pam_paruntinstance_is_not_abstract():
    assert not inspect.isabstract(MARTE_PAM_PaRunTInstance)


def test_marte_pam_paruntinstance_constructor_exists():
    assert callable(MARTE_PAM_PaRunTInstance.__init__)


def test_marte_pam_paruntinstance_constructor_args():
    sig = inspect.signature(MARTE_PAM_PaRunTInstance.__init__)
    params = list(sig.parameters.keys())
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "utilization" in params, "Missing parameter 'utilization'"
    assert "unbddPool" in params, "Missing parameter 'unbddPool'"
    assert "poolSize" in params, "Missing parameter 'poolSize'"

def test_marte_pam_paruntinstance_has_throughput():
    assert hasattr(MARTE_PAM_PaRunTInstance, "throughput")
    descriptor = None
    for klass in MARTE_PAM_PaRunTInstance.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
            break
    assert isinstance(descriptor, property)

def test_marte_pam_paruntinstance_has_utilization():
    assert hasattr(MARTE_PAM_PaRunTInstance, "utilization")
    descriptor = None
    for klass in MARTE_PAM_PaRunTInstance.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)

def test_marte_pam_paruntinstance_has_unbddPool():
    assert hasattr(MARTE_PAM_PaRunTInstance, "unbddPool")
    descriptor = None
    for klass in MARTE_PAM_PaRunTInstance.__mro__:
        if "unbddPool" in klass.__dict__:
            descriptor = klass.__dict__["unbddPool"]
            break
    assert isinstance(descriptor, property)

def test_marte_pam_paruntinstance_has_poolSize():
    assert hasattr(MARTE_PAM_PaRunTInstance, "poolSize")
    descriptor = None
    for klass in MARTE_PAM_PaRunTInstance.__mro__:
        if "poolSize" in klass.__dict__:
            descriptor = klass.__dict__["poolSize"]
            break
    assert isinstance(descriptor, property)



def test_gaexechost_is_not_abstract():
    assert not inspect.isabstract(GaExecHost)


def test_gaexechost_constructor_exists():
    assert callable(GaExecHost.__init__)


def test_gaexechost_constructor_args():
    sig = inspect.signature(GaExecHost.__init__)
    params = list(sig.parameters.keys())



def test_marte_sam_saexechost_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaExecHost)


def test_marte_sam_saexechost_constructor_exists():
    assert callable(MARTE_SAM_SaExecHost.__init__)


def test_marte_sam_saexechost_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaExecHost.__init__)
    params = list(sig.parameters.keys())
    assert "isSched" in params, "Missing parameter 'isSched'"
    assert "schedUtiliz" in params, "Missing parameter 'schedUtiliz'"
    assert "schSlack" in params, "Missing parameter 'schSlack'"
    assert "ISRswitchT" in params, "Missing parameter 'ISRswitchT'"
    assert "ISRprioRange" in params, "Missing parameter 'ISRprioRange'"

def test_marte_sam_saexechost_has_isSched():
    assert hasattr(MARTE_SAM_SaExecHost, "isSched")
    descriptor = None
    for klass in MARTE_SAM_SaExecHost.__mro__:
        if "isSched" in klass.__dict__:
            descriptor = klass.__dict__["isSched"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_saexechost_has_schedUtiliz():
    assert hasattr(MARTE_SAM_SaExecHost, "schedUtiliz")
    descriptor = None
    for klass in MARTE_SAM_SaExecHost.__mro__:
        if "schedUtiliz" in klass.__dict__:
            descriptor = klass.__dict__["schedUtiliz"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_saexechost_has_schSlack():
    assert hasattr(MARTE_SAM_SaExecHost, "schSlack")
    descriptor = None
    for klass in MARTE_SAM_SaExecHost.__mro__:
        if "schSlack" in klass.__dict__:
            descriptor = klass.__dict__["schSlack"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_saexechost_has_ISRswitchT():
    assert hasattr(MARTE_SAM_SaExecHost, "ISRswitchT")
    descriptor = None
    for klass in MARTE_SAM_SaExecHost.__mro__:
        if "ISRswitchT" in klass.__dict__:
            descriptor = klass.__dict__["ISRswitchT"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_saexechost_has_ISRprioRange():
    assert hasattr(MARTE_SAM_SaExecHost, "ISRprioRange")
    descriptor = None
    for klass in MARTE_SAM_SaExecHost.__mro__:
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



def test_marte_sam_sacommhost_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaCommHost)


def test_marte_sam_sacommhost_constructor_exists():
    assert callable(MARTE_SAM_SaCommHost.__init__)


def test_marte_sam_sacommhost_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaCommHost.__init__)
    params = list(sig.parameters.keys())
    assert "schSlack" in params, "Missing parameter 'schSlack'"
    assert "isSched" in params, "Missing parameter 'isSched'"

def test_marte_sam_sacommhost_has_schSlack():
    assert hasattr(MARTE_SAM_SaCommHost, "schSlack")
    descriptor = None
    for klass in MARTE_SAM_SaCommHost.__mro__:
        if "schSlack" in klass.__dict__:
            descriptor = klass.__dict__["schSlack"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sacommhost_has_isSched():
    assert hasattr(MARTE_SAM_SaCommHost, "isSched")
    descriptor = None
    for klass in MARTE_SAM_SaCommHost.__mro__:
        if "isSched" in klass.__dict__:
            descriptor = klass.__dict__["isSched"]
            break
    assert isinstance(descriptor, property)



def test_mutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(MutualExclusionResource)


def test_mutualexclusionresource_constructor_exists():
    assert callable(MutualExclusionResource.__init__)


def test_mutualexclusionresource_constructor_args():
    sig = inspect.signature(MutualExclusionResource.__init__)
    params = list(sig.parameters.keys())



def test_grm_secondaryscheduler_is_not_abstract():
    assert not inspect.isabstract(GRM_SecondaryScheduler)


def test_grm_secondaryscheduler_constructor_exists():
    assert callable(GRM_SecondaryScheduler.__init__)


def test_grm_secondaryscheduler_constructor_args():
    sig = inspect.signature(GRM_SecondaryScheduler.__init__)
    params = list(sig.parameters.keys())



def test_processingresource_is_not_abstract():
    assert not inspect.isabstract(ProcessingResource)


def test_processingresource_constructor_exists():
    assert callable(ProcessingResource.__init__)


def test_processingresource_constructor_args():
    sig = inspect.signature(ProcessingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_computingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_ComputingResource)


def test_marte_grm_computingresource_constructor_exists():
    assert callable(MARTE_GRM_ComputingResource.__init__)


def test_marte_grm_computingresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_ComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_grm_scheduler_is_not_abstract():
    assert not inspect.isabstract(GRM_Scheduler)


def test_grm_scheduler_constructor_exists():
    assert callable(GRM_Scheduler.__init__)


def test_grm_scheduler_constructor_args():
    sig = inspect.signature(GRM_Scheduler.__init__)
    params = list(sig.parameters.keys())



def test_grm_schedulableresource_is_not_abstract():
    assert not inspect.isabstract(GRM_SchedulableResource)


def test_grm_schedulableresource_constructor_exists():
    assert callable(GRM_SchedulableResource.__init__)


def test_grm_schedulableresource_constructor_args():
    sig = inspect.signature(GRM_SchedulableResource.__init__)
    params = list(sig.parameters.keys())



def test_grm_mutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(GRM_MutualExclusionResource)


def test_grm_mutualexclusionresource_constructor_exists():
    assert callable(GRM_MutualExclusionResource.__init__)


def test_grm_mutualexclusionresource_constructor_args():
    sig = inspect.signature(GRM_MutualExclusionResource.__init__)
    params = list(sig.parameters.keys())



def test_grm_computingresource_is_not_abstract():
    assert not inspect.isabstract(GRM_ComputingResource)


def test_grm_computingresource_constructor_exists():
    assert callable(GRM_ComputingResource.__init__)


def test_grm_computingresource_constructor_args():
    sig = inspect.signature(GRM_ComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_grm_processingresource_is_not_abstract():
    assert not inspect.isabstract(GRM_ProcessingResource)


def test_grm_processingresource_constructor_exists():
    assert callable(GRM_ProcessingResource.__init__)


def test_grm_processingresource_constructor_args():
    sig = inspect.signature(GRM_ProcessingResource.__init__)
    params = list(sig.parameters.keys())



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_marte_pam_palogicalresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_PAM_PaLogicalResource)


def test_marte_pam_palogicalresource_constructor_exists():
    assert callable(MARTE_PAM_PaLogicalResource.__init__)


def test_marte_pam_palogicalresource_constructor_args():
    sig = inspect.signature(MARTE_PAM_PaLogicalResource.__init__)
    params = list(sig.parameters.keys())
    assert "utilization" in params, "Missing parameter 'utilization'"
    assert "poolSize" in params, "Missing parameter 'poolSize'"
    assert "throughput" in params, "Missing parameter 'throughput'"

def test_marte_pam_palogicalresource_has_utilization():
    assert hasattr(MARTE_PAM_PaLogicalResource, "utilization")
    descriptor = None
    for klass in MARTE_PAM_PaLogicalResource.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)

def test_marte_pam_palogicalresource_has_poolSize():
    assert hasattr(MARTE_PAM_PaLogicalResource, "poolSize")
    descriptor = None
    for klass in MARTE_PAM_PaLogicalResource.__mro__:
        if "poolSize" in klass.__dict__:
            descriptor = klass.__dict__["poolSize"]
            break
    assert isinstance(descriptor, property)

def test_marte_pam_palogicalresource_has_throughput():
    assert hasattr(MARTE_PAM_PaLogicalResource, "throughput")
    descriptor = None
    for klass in MARTE_PAM_PaLogicalResource.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
            break
    assert isinstance(descriptor, property)



def test_marte_grm_synchronizationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_SynchronizationResource)


def test_marte_grm_synchronizationresource_constructor_exists():
    assert callable(MARTE_GRM_SynchronizationResource.__init__)


def test_marte_grm_synchronizationresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_SynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_concurrencyresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_ConcurrencyResource)


def test_marte_grm_concurrencyresource_constructor_exists():
    assert callable(MARTE_GRM_ConcurrencyResource.__init__)


def test_marte_grm_concurrencyresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_ConcurrencyResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_scheduler_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_Scheduler)


def test_marte_grm_scheduler_constructor_exists():
    assert callable(MARTE_GRM_Scheduler.__init__)


def test_marte_grm_scheduler_constructor_args():
    sig = inspect.signature(MARTE_GRM_Scheduler.__init__)
    params = list(sig.parameters.keys())
    assert "schedPolicy" in params, "Missing parameter 'schedPolicy'"
    assert "schedule" in params, "Missing parameter 'schedule'"
    assert "otherSchedPolicy" in params, "Missing parameter 'otherSchedPolicy'"
    assert "isPreemptible" in params, "Missing parameter 'isPreemptible'"

def test_marte_grm_scheduler_has_schedPolicy():
    assert hasattr(MARTE_GRM_Scheduler, "schedPolicy")
    descriptor = None
    for klass in MARTE_GRM_Scheduler.__mro__:
        if "schedPolicy" in klass.__dict__:
            descriptor = klass.__dict__["schedPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_scheduler_has_schedule():
    assert hasattr(MARTE_GRM_Scheduler, "schedule")
    descriptor = None
    for klass in MARTE_GRM_Scheduler.__mro__:
        if "schedule" in klass.__dict__:
            descriptor = klass.__dict__["schedule"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_scheduler_has_otherSchedPolicy():
    assert hasattr(MARTE_GRM_Scheduler, "otherSchedPolicy")
    descriptor = None
    for klass in MARTE_GRM_Scheduler.__mro__:
        if "otherSchedPolicy" in klass.__dict__:
            descriptor = klass.__dict__["otherSchedPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_scheduler_has_isPreemptible():
    assert hasattr(MARTE_GRM_Scheduler, "isPreemptible")
    descriptor = None
    for klass in MARTE_GRM_Scheduler.__mro__:
        if "isPreemptible" in klass.__dict__:
            descriptor = klass.__dict__["isPreemptible"]
            break
    assert isinstance(descriptor, property)



def test_marte_grm_schedulableresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_SchedulableResource)


def test_marte_grm_schedulableresource_constructor_exists():
    assert callable(MARTE_GRM_SchedulableResource.__init__)


def test_marte_grm_schedulableresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_SchedulableResource.__init__)
    params = list(sig.parameters.keys())
    assert "schedParams" in params, "Missing parameter 'schedParams'"

def test_marte_grm_schedulableresource_has_schedParams():
    assert hasattr(MARTE_GRM_SchedulableResource, "schedParams")
    descriptor = None
    for klass in MARTE_GRM_SchedulableResource.__mro__:
        if "schedParams" in klass.__dict__:
            descriptor = klass.__dict__["schedParams"]
            break
    assert isinstance(descriptor, property)



def test_marte_grm_communicationendpoint_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_CommunicationEndPoint)


def test_marte_grm_communicationendpoint_constructor_exists():
    assert callable(MARTE_GRM_CommunicationEndPoint.__init__)


def test_marte_grm_communicationendpoint_constructor_args():
    sig = inspect.signature(MARTE_GRM_CommunicationEndPoint.__init__)
    params = list(sig.parameters.keys())
    assert "packetSize" in params, "Missing parameter 'packetSize'"

def test_marte_grm_communicationendpoint_has_packetSize():
    assert hasattr(MARTE_GRM_CommunicationEndPoint, "packetSize")
    descriptor = None
    for klass in MARTE_GRM_CommunicationEndPoint.__mro__:
        if "packetSize" in klass.__dict__:
            descriptor = klass.__dict__["packetSize"]
            break
    assert isinstance(descriptor, property)



def test_marte_grm_processingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_ProcessingResource)


def test_marte_grm_processingresource_constructor_exists():
    assert callable(MARTE_GRM_ProcessingResource.__init__)


def test_marte_grm_processingresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_ProcessingResource.__init__)
    params = list(sig.parameters.keys())
    assert "speedFactor" in params, "Missing parameter 'speedFactor'"

def test_marte_grm_processingresource_has_speedFactor():
    assert hasattr(MARTE_GRM_ProcessingResource, "speedFactor")
    descriptor = None
    for klass in MARTE_GRM_ProcessingResource.__mro__:
        if "speedFactor" in klass.__dict__:
            descriptor = klass.__dict__["speedFactor"]
            break
    assert isinstance(descriptor, property)



def test_marte_grm_mutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_MutualExclusionResource)


def test_marte_grm_mutualexclusionresource_constructor_exists():
    assert callable(MARTE_GRM_MutualExclusionResource.__init__)


def test_marte_grm_mutualexclusionresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_MutualExclusionResource.__init__)
    params = list(sig.parameters.keys())
    assert "otherProtectProtocol" in params, "Missing parameter 'otherProtectProtocol'"
    assert "ceiling" in params, "Missing parameter 'ceiling'"
    assert "protectKind" in params, "Missing parameter 'protectKind'"

def test_marte_grm_mutualexclusionresource_has_otherProtectProtocol():
    assert hasattr(MARTE_GRM_MutualExclusionResource, "otherProtectProtocol")
    descriptor = None
    for klass in MARTE_GRM_MutualExclusionResource.__mro__:
        if "otherProtectProtocol" in klass.__dict__:
            descriptor = klass.__dict__["otherProtectProtocol"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_mutualexclusionresource_has_ceiling():
    assert hasattr(MARTE_GRM_MutualExclusionResource, "ceiling")
    descriptor = None
    for klass in MARTE_GRM_MutualExclusionResource.__mro__:
        if "ceiling" in klass.__dict__:
            descriptor = klass.__dict__["ceiling"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_mutualexclusionresource_has_protectKind():
    assert hasattr(MARTE_GRM_MutualExclusionResource, "protectKind")
    descriptor = None
    for klass in MARTE_GRM_MutualExclusionResource.__mro__:
        if "protectKind" in klass.__dict__:
            descriptor = klass.__dict__["protectKind"]
            break
    assert isinstance(descriptor, property)



def test_marte_grm_storageresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_StorageResource)


def test_marte_grm_storageresource_constructor_exists():
    assert callable(MARTE_GRM_StorageResource.__init__)


def test_marte_grm_storageresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_StorageResource.__init__)
    params = list(sig.parameters.keys())
    assert "elementSize" in params, "Missing parameter 'elementSize'"

def test_marte_grm_storageresource_has_elementSize():
    assert hasattr(MARTE_GRM_StorageResource, "elementSize")
    descriptor = None
    for klass in MARTE_GRM_StorageResource.__mro__:
        if "elementSize" in klass.__dict__:
            descriptor = klass.__dict__["elementSize"]
            break
    assert isinstance(descriptor, property)



def test_grm_marte_lifeline_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_Lifeline)


def test_grm_marte_lifeline_constructor_exists():
    assert callable(GRM_MARTE_Lifeline.__init__)


def test_grm_marte_lifeline_constructor_args():
    sig = inspect.signature(GRM_MARTE_Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_grm_marte_classifier_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_Classifier)


def test_grm_marte_classifier_constructor_exists():
    assert callable(GRM_MARTE_Classifier.__init__)


def test_grm_marte_classifier_constructor_args():
    sig = inspect.signature(GRM_MARTE_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_grm_marte_instancespecification_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_InstanceSpecification)


def test_grm_marte_instancespecification_constructor_exists():
    assert callable(GRM_MARTE_InstanceSpecification.__init__)


def test_grm_marte_instancespecification_constructor_args():
    sig = inspect.signature(GRM_MARTE_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_grm_marte_property_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_Property)


def test_grm_marte_property_constructor_exists():
    assert callable(GRM_MARTE_Property.__init__)


def test_grm_marte_property_constructor_args():
    sig = inspect.signature(GRM_MARTE_Property.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_resource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_Resource)


def test_marte_grm_resource_constructor_exists():
    assert callable(MARTE_GRM_Resource.__init__)


def test_marte_grm_resource_constructor_args():
    sig = inspect.signature(MARTE_GRM_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "isProtected" in params, "Missing parameter 'isProtected'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "resMult" in params, "Missing parameter 'resMult'"

def test_marte_grm_resource_has_isProtected():
    assert hasattr(MARTE_GRM_Resource, "isProtected")
    descriptor = None
    for klass in MARTE_GRM_Resource.__mro__:
        if "isProtected" in klass.__dict__:
            descriptor = klass.__dict__["isProtected"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_resource_has_isActive():
    assert hasattr(MARTE_GRM_Resource, "isActive")
    descriptor = None
    for klass in MARTE_GRM_Resource.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_resource_has_resMult():
    assert hasattr(MARTE_GRM_Resource, "resMult")
    descriptor = None
    for klass in MARTE_GRM_Resource.__mro__:
        if "resMult" in klass.__dict__:
            descriptor = klass.__dict__["resMult"]
            break
    assert isinstance(descriptor, property)



def test_time_marte_message_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Message)


def test_time_marte_message_constructor_exists():
    assert callable(Time_MARTE_Message.__init__)


def test_time_marte_message_constructor_args():
    sig = inspect.signature(Time_MARTE_Message.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_behavior_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Behavior)


def test_time_marte_behavior_constructor_exists():
    assert callable(Time_MARTE_Behavior.__init__)


def test_time_marte_behavior_constructor_args():
    sig = inspect.signature(Time_MARTE_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_grm_marte_connectableelement_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_ConnectableElement)


def test_grm_marte_connectableelement_constructor_exists():
    assert callable(GRM_MARTE_ConnectableElement.__init__)


def test_grm_marte_connectableelement_constructor_args():
    sig = inspect.signature(GRM_MARTE_ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_action_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Action)


def test_time_marte_action_constructor_exists():
    assert callable(Time_MARTE_Action.__init__)


def test_time_marte_action_constructor_args():
    sig = inspect.signature(Time_MARTE_Action.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_timeevent_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_TimeEvent)


def test_time_marte_timeevent_constructor_exists():
    assert callable(Time_MARTE_TimeEvent.__init__)


def test_time_marte_timeevent_constructor_args():
    sig = inspect.signature(Time_MARTE_TimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_durationobservation_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_DurationObservation)


def test_time_marte_durationobservation_constructor_exists():
    assert callable(Time_MARTE_DurationObservation.__init__)


def test_time_marte_durationobservation_constructor_args():
    sig = inspect.signature(Time_MARTE_DurationObservation.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_timeobservation_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_TimeObservation)


def test_time_marte_timeobservation_constructor_exists():
    assert callable(Time_MARTE_TimeObservation.__init__)


def test_time_marte_timeobservation_constructor_args():
    sig = inspect.signature(Time_MARTE_TimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_time_timedelement_is_not_abstract():
    assert not inspect.isabstract(Time_TimedElement)


def test_time_timedelement_constructor_exists():
    assert callable(Time_TimedElement.__init__)


def test_time_timedelement_constructor_args():
    sig = inspect.signature(Time_TimedElement.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_valuespecification_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_ValueSpecification)


def test_time_marte_valuespecification_constructor_exists():
    assert callable(Time_MARTE_ValueSpecification.__init__)


def test_time_marte_valuespecification_constructor_args():
    sig = inspect.signature(Time_MARTE_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_timedelement_is_not_abstract():
    assert not inspect.isabstract(TimedElement)


def test_timedelement_constructor_exists():
    assert callable(TimedElement.__init__)


def test_timedelement_constructor_args():
    sig = inspect.signature(TimedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte_time_timedprocessing_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_TimedProcessing)


def test_marte_time_timedprocessing_constructor_exists():
    assert callable(MARTE_Time_TimedProcessing.__init__)


def test_marte_time_timedprocessing_constructor_args():
    sig = inspect.signature(MARTE_Time_TimedProcessing.__init__)
    params = list(sig.parameters.keys())



def test_marte_time_timedevent_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_TimedEvent)


def test_marte_time_timedevent_constructor_exists():
    assert callable(MARTE_Time_TimedEvent.__init__)


def test_marte_time_timedevent_constructor_args():
    sig = inspect.signature(MARTE_Time_TimedEvent.__init__)
    params = list(sig.parameters.keys())
    assert "repetition" in params, "Missing parameter 'repetition'"

def test_marte_time_timedevent_has_repetition():
    assert hasattr(MARTE_Time_TimedEvent, "repetition")
    descriptor = None
    for klass in MARTE_Time_TimedEvent.__mro__:
        if "repetition" in klass.__dict__:
            descriptor = klass.__dict__["repetition"]
            break
    assert isinstance(descriptor, property)



def test_marte_time_timeddurationobservation_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_TimedDurationObservation)


def test_marte_time_timeddurationobservation_constructor_exists():
    assert callable(MARTE_Time_TimedDurationObservation.__init__)


def test_marte_time_timeddurationobservation_constructor_args():
    sig = inspect.signature(MARTE_Time_TimedDurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "obsKind" in params, "Missing parameter 'obsKind'"

def test_marte_time_timeddurationobservation_has_obsKind():
    assert hasattr(MARTE_Time_TimedDurationObservation, "obsKind")
    descriptor = None
    for klass in MARTE_Time_TimedDurationObservation.__mro__:
        if "obsKind" in klass.__dict__:
            descriptor = klass.__dict__["obsKind"]
            break
    assert isinstance(descriptor, property)



def test_marte_time_timedinstantobservation_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_TimedInstantObservation)


def test_marte_time_timedinstantobservation_constructor_exists():
    assert callable(MARTE_Time_TimedInstantObservation.__init__)


def test_marte_time_timedinstantobservation_constructor_args():
    sig = inspect.signature(MARTE_Time_TimedInstantObservation.__init__)
    params = list(sig.parameters.keys())
    assert "obsKind" in params, "Missing parameter 'obsKind'"

def test_marte_time_timedinstantobservation_has_obsKind():
    assert hasattr(MARTE_Time_TimedInstantObservation, "obsKind")
    descriptor = None
    for klass in MARTE_Time_TimedInstantObservation.__mro__:
        if "obsKind" in klass.__dict__:
            descriptor = klass.__dict__["obsKind"]
            break
    assert isinstance(descriptor, property)



def test_marte_time_timedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_TimedValueSpecification)


def test_marte_time_timedvaluespecification_constructor_exists():
    assert callable(MARTE_Time_TimedValueSpecification.__init__)


def test_marte_time_timedvaluespecification_constructor_args():
    sig = inspect.signature(MARTE_Time_TimedValueSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "interpretation" in params, "Missing parameter 'interpretation'"

def test_marte_time_timedvaluespecification_has_interpretation():
    assert hasattr(MARTE_Time_TimedValueSpecification, "interpretation")
    descriptor = None
    for klass in MARTE_Time_TimedValueSpecification.__mro__:
        if "interpretation" in klass.__dict__:
            descriptor = klass.__dict__["interpretation"]
            break
    assert isinstance(descriptor, property)



def test_time_clock_is_not_abstract():
    assert not inspect.isabstract(Time_Clock)


def test_time_clock_constructor_exists():
    assert callable(Time_Clock.__init__)


def test_time_clock_constructor_args():
    sig = inspect.signature(Time_Clock.__init__)
    params = list(sig.parameters.keys())



def test_marte_time_timedelement_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_TimedElement)


def test_marte_time_timedelement_constructor_exists():
    assert callable(MARTE_Time_TimedElement.__init__)


def test_marte_time_timedelement_constructor_args():
    sig = inspect.signature(MARTE_Time_TimedElement.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_class_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Class)


def test_time_marte_class_constructor_exists():
    assert callable(Time_MARTE_Class.__init__)


def test_time_marte_class_constructor_args():
    sig = inspect.signature(Time_MARTE_Class.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_operation_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Operation)


def test_time_marte_operation_constructor_exists():
    assert callable(Time_MARTE_Operation.__init__)


def test_time_marte_operation_constructor_args():
    sig = inspect.signature(Time_MARTE_Operation.__init__)
    params = list(sig.parameters.keys())



def test_marte_time_clocktype_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_ClockType)


def test_marte_time_clocktype_constructor_exists():
    assert callable(MARTE_Time_ClockType.__init__)


def test_marte_time_clocktype_constructor_args():
    sig = inspect.signature(MARTE_Time_ClockType.__init__)
    params = list(sig.parameters.keys())
    assert "nature" in params, "Missing parameter 'nature'"
    assert "isLogical" in params, "Missing parameter 'isLogical'"

def test_marte_time_clocktype_has_nature():
    assert hasattr(MARTE_Time_ClockType, "nature")
    descriptor = None
    for klass in MARTE_Time_ClockType.__mro__:
        if "nature" in klass.__dict__:
            descriptor = klass.__dict__["nature"]
            break
    assert isinstance(descriptor, property)

def test_marte_time_clocktype_has_isLogical():
    assert hasattr(MARTE_Time_ClockType, "isLogical")
    descriptor = None
    for klass in MARTE_Time_ClockType.__mro__:
        if "isLogical" in klass.__dict__:
            descriptor = klass.__dict__["isLogical"]
            break
    assert isinstance(descriptor, property)



def test_time_marte_event_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Event)


def test_time_marte_event_constructor_exists():
    assert callable(Time_MARTE_Event.__init__)


def test_time_marte_event_constructor_args():
    sig = inspect.signature(Time_MARTE_Event.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_property_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Property)


def test_time_marte_property_constructor_exists():
    assert callable(Time_MARTE_Property.__init__)


def test_time_marte_property_constructor_args():
    sig = inspect.signature(Time_MARTE_Property.__init__)
    params = list(sig.parameters.keys())



def test_time_clocktype_is_not_abstract():
    assert not inspect.isabstract(Time_ClockType)


def test_time_clocktype_constructor_exists():
    assert callable(Time_ClockType.__init__)


def test_time_clocktype_constructor_args():
    sig = inspect.signature(Time_ClockType.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_instancespecification_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_InstanceSpecification)


def test_time_marte_instancespecification_constructor_exists():
    assert callable(Time_MARTE_InstanceSpecification.__init__)


def test_time_marte_instancespecification_constructor_args():
    sig = inspect.signature(Time_MARTE_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_marte_time_clock_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_Clock)


def test_marte_time_clock_constructor_exists():
    assert callable(MARTE_Time_Clock.__init__)


def test_marte_time_clock_constructor_args():
    sig = inspect.signature(MARTE_Time_Clock.__init__)
    params = list(sig.parameters.keys())
    assert "standard" in params, "Missing parameter 'standard'"

def test_marte_time_clock_has_standard():
    assert hasattr(MARTE_Time_Clock, "standard")
    descriptor = None
    for klass in MARTE_Time_Clock.__mro__:
        if "standard" in klass.__dict__:
            descriptor = klass.__dict__["standard"]
            break
    assert isinstance(descriptor, property)



def test_time_marte_namespace_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Namespace)


def test_time_marte_namespace_constructor_exists():
    assert callable(Time_MARTE_Namespace.__init__)


def test_time_marte_namespace_constructor_args():
    sig = inspect.signature(Time_MARTE_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_marte_time_timeddomain_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_TimedDomain)


def test_marte_time_timeddomain_constructor_exists():
    assert callable(MARTE_Time_TimedDomain.__init__)


def test_marte_time_timeddomain_constructor_args():
    sig = inspect.signature(MARTE_Time_TimedDomain.__init__)
    params = list(sig.parameters.keys())



def test_alloc_marte_abstraction_is_not_abstract():
    assert not inspect.isabstract(Alloc_MARTE_Abstraction)


def test_alloc_marte_abstraction_constructor_exists():
    assert callable(Alloc_MARTE_Abstraction.__init__)


def test_alloc_marte_abstraction_constructor_args():
    sig = inspect.signature(Alloc_MARTE_Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_enumeration_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Enumeration)


def test_time_marte_enumeration_constructor_exists():
    assert callable(Time_MARTE_Enumeration.__init__)


def test_time_marte_enumeration_constructor_args():
    sig = inspect.signature(Time_MARTE_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_alloc_marte_comment_is_not_abstract():
    assert not inspect.isabstract(Alloc_MARTE_Comment)


def test_alloc_marte_comment_constructor_exists():
    assert callable(Alloc_MARTE_Comment.__init__)


def test_alloc_marte_comment_constructor_args():
    sig = inspect.signature(Alloc_MARTE_Comment.__init__)
    params = list(sig.parameters.keys())



def test_alloc_marte_element_is_not_abstract():
    assert not inspect.isabstract(Alloc_MARTE_Element)


def test_alloc_marte_element_constructor_exists():
    assert callable(Alloc_MARTE_Element.__init__)


def test_alloc_marte_element_constructor_args():
    sig = inspect.signature(Alloc_MARTE_Element.__init__)
    params = list(sig.parameters.keys())



def test_marte_alloc_assign_is_not_abstract():
    assert not inspect.isabstract(MARTE_Alloc_Assign)


def test_marte_alloc_assign_constructor_exists():
    assert callable(MARTE_Alloc_Assign.__init__)


def test_marte_alloc_assign_constructor_args():
    sig = inspect.signature(MARTE_Alloc_Assign.__init__)
    params = list(sig.parameters.keys())
    assert "nature" in params, "Missing parameter 'nature'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte_alloc_assign_has_nature():
    assert hasattr(MARTE_Alloc_Assign, "nature")
    descriptor = None
    for klass in MARTE_Alloc_Assign.__mro__:
        if "nature" in klass.__dict__:
            descriptor = klass.__dict__["nature"]
            break
    assert isinstance(descriptor, property)

def test_marte_alloc_assign_has_kind():
    assert hasattr(MARTE_Alloc_Assign, "kind")
    descriptor = None
    for klass in MARTE_Alloc_Assign.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_nfps_nfpconstraint_is_not_abstract():
    assert not inspect.isabstract(NFPs_NfpConstraint)


def test_nfps_nfpconstraint_constructor_exists():
    assert callable(NFPs_NfpConstraint.__init__)


def test_nfps_nfpconstraint_constructor_args():
    sig = inspect.signature(NFPs_NfpConstraint.__init__)
    params = list(sig.parameters.keys())



def test_marte_time_timedconstraint_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_TimedConstraint)


def test_marte_time_timedconstraint_constructor_exists():
    assert callable(MARTE_Time_TimedConstraint.__init__)


def test_marte_time_timedconstraint_constructor_args():
    sig = inspect.signature(MARTE_Time_TimedConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "interpretation" in params, "Missing parameter 'interpretation'"

def test_marte_time_timedconstraint_has_interpretation():
    assert hasattr(MARTE_Time_TimedConstraint, "interpretation")
    descriptor = None
    for klass in MARTE_Time_TimedConstraint.__mro__:
        if "interpretation" in klass.__dict__:
            descriptor = klass.__dict__["interpretation"]
            break
    assert isinstance(descriptor, property)



def test_marte_time_clockconstraint_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_ClockConstraint)


def test_marte_time_clockconstraint_constructor_exists():
    assert callable(MARTE_Time_ClockConstraint.__init__)


def test_marte_time_clockconstraint_constructor_args():
    sig = inspect.signature(MARTE_Time_ClockConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "isChronometricBased" in params, "Missing parameter 'isChronometricBased'"
    assert "isPrecedenceBased" in params, "Missing parameter 'isPrecedenceBased'"
    assert "isCoincidenceBased" in params, "Missing parameter 'isCoincidenceBased'"

def test_marte_time_clockconstraint_has_isChronometricBased():
    assert hasattr(MARTE_Time_ClockConstraint, "isChronometricBased")
    descriptor = None
    for klass in MARTE_Time_ClockConstraint.__mro__:
        if "isChronometricBased" in klass.__dict__:
            descriptor = klass.__dict__["isChronometricBased"]
            break
    assert isinstance(descriptor, property)

def test_marte_time_clockconstraint_has_isPrecedenceBased():
    assert hasattr(MARTE_Time_ClockConstraint, "isPrecedenceBased")
    descriptor = None
    for klass in MARTE_Time_ClockConstraint.__mro__:
        if "isPrecedenceBased" in klass.__dict__:
            descriptor = klass.__dict__["isPrecedenceBased"]
            break
    assert isinstance(descriptor, property)

def test_marte_time_clockconstraint_has_isCoincidenceBased():
    assert hasattr(MARTE_Time_ClockConstraint, "isCoincidenceBased")
    descriptor = None
    for klass in MARTE_Time_ClockConstraint.__mro__:
        if "isCoincidenceBased" in klass.__dict__:
            descriptor = klass.__dict__["isCoincidenceBased"]
            break
    assert isinstance(descriptor, property)



def test_marte_alloc_allocate_is_not_abstract():
    assert not inspect.isabstract(MARTE_Alloc_Allocate)


def test_marte_alloc_allocate_constructor_exists():
    assert callable(MARTE_Alloc_Allocate.__init__)


def test_marte_alloc_allocate_constructor_args():
    sig = inspect.signature(MARTE_Alloc_Allocate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "nature" in params, "Missing parameter 'nature'"

def test_marte_alloc_allocate_has_kind():
    assert hasattr(MARTE_Alloc_Allocate, "kind")
    descriptor = None
    for klass in MARTE_Alloc_Allocate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_marte_alloc_allocate_has_nature():
    assert hasattr(MARTE_Alloc_Allocate, "nature")
    descriptor = None
    for klass in MARTE_Alloc_Allocate.__mro__:
        if "nature" in klass.__dict__:
            descriptor = klass.__dict__["nature"]
            break
    assert isinstance(descriptor, property)



def test_marte_alloc_nfprefine_is_not_abstract():
    assert not inspect.isabstract(MARTE_Alloc_NfpRefine)


def test_marte_alloc_nfprefine_constructor_exists():
    assert callable(MARTE_Alloc_NfpRefine.__init__)


def test_marte_alloc_nfprefine_constructor_args():
    sig = inspect.signature(MARTE_Alloc_NfpRefine.__init__)
    params = list(sig.parameters.keys())



def test_alloc_allocated_is_not_abstract():
    assert not inspect.isabstract(Alloc_Allocated)


def test_alloc_allocated_constructor_exists():
    assert callable(Alloc_Allocated.__init__)


def test_alloc_allocated_constructor_args():
    sig = inspect.signature(Alloc_Allocated.__init__)
    params = list(sig.parameters.keys())



def test_alloc_marte_activitypartition_is_not_abstract():
    assert not inspect.isabstract(Alloc_MARTE_ActivityPartition)


def test_alloc_marte_activitypartition_constructor_exists():
    assert callable(Alloc_MARTE_ActivityPartition.__init__)


def test_alloc_marte_activitypartition_constructor_args():
    sig = inspect.signature(Alloc_MARTE_ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_marte_alloc_allocateactivitygroup_is_not_abstract():
    assert not inspect.isabstract(MARTE_Alloc_AllocateActivityGroup)


def test_marte_alloc_allocateactivitygroup_constructor_exists():
    assert callable(MARTE_Alloc_AllocateActivityGroup.__init__)


def test_marte_alloc_allocateactivitygroup_constructor_args():
    sig = inspect.signature(MARTE_Alloc_AllocateActivityGroup.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_marte_alloc_allocateactivitygroup_has_isUnique():
    assert hasattr(MARTE_Alloc_AllocateActivityGroup, "isUnique")
    descriptor = None
    for klass in MARTE_Alloc_AllocateActivityGroup.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_alloc_marte_dependency_is_not_abstract():
    assert not inspect.isabstract(Alloc_MARTE_Dependency)


def test_alloc_marte_dependency_constructor_exists():
    assert callable(Alloc_MARTE_Dependency.__init__)


def test_alloc_marte_dependency_constructor_args():
    sig = inspect.signature(Alloc_MARTE_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_tupletype_is_not_abstract():
    assert not inspect.isabstract(TupleType)


def test_tupletype_constructor_exists():
    assert callable(TupleType.__init__)


def test_tupletype_constructor_args():
    sig = inspect.signature(TupleType.__init__)
    params = list(sig.parameters.keys())



def test_marte_nfps_nfptype_is_not_abstract():
    assert not inspect.isabstract(MARTE_NFPs_NfpType)


def test_marte_nfps_nfptype_constructor_exists():
    assert callable(MARTE_NFPs_NfpType.__init__)


def test_marte_nfps_nfptype_constructor_args():
    sig = inspect.signature(MARTE_NFPs_NfpType.__init__)
    params = list(sig.parameters.keys())



def test_coreelements_mode_is_not_abstract():
    assert not inspect.isabstract(CoreElements_Mode)


def test_coreelements_mode_constructor_exists():
    assert callable(CoreElements_Mode.__init__)


def test_coreelements_mode_constructor_args():
    sig = inspect.signature(CoreElements_Mode.__init__)
    params = list(sig.parameters.keys())



def test_alloc_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(Alloc_MARTE_NamedElement)


def test_alloc_marte_namedelement_constructor_exists():
    assert callable(Alloc_MARTE_NamedElement.__init__)


def test_alloc_marte_namedelement_constructor_args():
    sig = inspect.signature(Alloc_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte_sam_sasharedresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaSharedResource)


def test_marte_sam_sasharedresource_constructor_exists():
    assert callable(MARTE_SAM_SaSharedResource.__init__)


def test_marte_sam_sasharedresource_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaSharedResource.__init__)
    params = list(sig.parameters.keys())
    assert "isPreemp" in params, "Missing parameter 'isPreemp'"
    assert "releaseT" in params, "Missing parameter 'releaseT'"
    assert "isConsum" in params, "Missing parameter 'isConsum'"
    assert "acquisT" in params, "Missing parameter 'acquisT'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_marte_sam_sasharedresource_has_isPreemp():
    assert hasattr(MARTE_SAM_SaSharedResource, "isPreemp")
    descriptor = None
    for klass in MARTE_SAM_SaSharedResource.__mro__:
        if "isPreemp" in klass.__dict__:
            descriptor = klass.__dict__["isPreemp"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sasharedresource_has_releaseT():
    assert hasattr(MARTE_SAM_SaSharedResource, "releaseT")
    descriptor = None
    for klass in MARTE_SAM_SaSharedResource.__mro__:
        if "releaseT" in klass.__dict__:
            descriptor = klass.__dict__["releaseT"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sasharedresource_has_isConsum():
    assert hasattr(MARTE_SAM_SaSharedResource, "isConsum")
    descriptor = None
    for klass in MARTE_SAM_SaSharedResource.__mro__:
        if "isConsum" in klass.__dict__:
            descriptor = klass.__dict__["isConsum"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sasharedresource_has_acquisT():
    assert hasattr(MARTE_SAM_SaSharedResource, "acquisT")
    descriptor = None
    for klass in MARTE_SAM_SaSharedResource.__mro__:
        if "acquisT" in klass.__dict__:
            descriptor = klass.__dict__["acquisT"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sasharedresource_has_capacity():
    assert hasattr(MARTE_SAM_SaSharedResource, "capacity")
    descriptor = None
    for klass in MARTE_SAM_SaSharedResource.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_sam_sasharedresource_is_not_abstract():
    assert not inspect.isabstract(SAM_SaSharedResource)


def test_sam_sasharedresource_constructor_exists():
    assert callable(SAM_SaSharedResource.__init__)


def test_sam_sasharedresource_constructor_args():
    sig = inspect.signature(SAM_SaSharedResource.__init__)
    params = list(sig.parameters.keys())



def test_sam_marte_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SAM_MARTE_BehavioralFeature)


def test_sam_marte_behavioralfeature_constructor_exists():
    assert callable(SAM_MARTE_BehavioralFeature.__init__)


def test_sam_marte_behavioralfeature_constructor_args():
    sig = inspect.signature(SAM_MARTE_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_marte_sam_saendtoendflow_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaEndtoEndFlow)


def test_marte_sam_saendtoendflow_constructor_exists():
    assert callable(MARTE_SAM_SaEndtoEndFlow.__init__)


def test_marte_sam_saendtoendflow_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaEndtoEndFlow.__init__)
    params = list(sig.parameters.keys())
    assert "end2EndT" in params, "Missing parameter 'end2EndT'"
    assert "end2EndD" in params, "Missing parameter 'end2EndD'"
    assert "isSched" in params, "Missing parameter 'isSched'"
    assert "schSlack" in params, "Missing parameter 'schSlack'"

def test_marte_sam_saendtoendflow_has_end2EndT():
    assert hasattr(MARTE_SAM_SaEndtoEndFlow, "end2EndT")
    descriptor = None
    for klass in MARTE_SAM_SaEndtoEndFlow.__mro__:
        if "end2EndT" in klass.__dict__:
            descriptor = klass.__dict__["end2EndT"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_saendtoendflow_has_end2EndD():
    assert hasattr(MARTE_SAM_SaEndtoEndFlow, "end2EndD")
    descriptor = None
    for klass in MARTE_SAM_SaEndtoEndFlow.__mro__:
        if "end2EndD" in klass.__dict__:
            descriptor = klass.__dict__["end2EndD"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_saendtoendflow_has_isSched():
    assert hasattr(MARTE_SAM_SaEndtoEndFlow, "isSched")
    descriptor = None
    for klass in MARTE_SAM_SaEndtoEndFlow.__mro__:
        if "isSched" in klass.__dict__:
            descriptor = klass.__dict__["isSched"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_saendtoendflow_has_schSlack():
    assert hasattr(MARTE_SAM_SaEndtoEndFlow, "schSlack")
    descriptor = None
    for klass in MARTE_SAM_SaEndtoEndFlow.__mro__:
        if "schSlack" in klass.__dict__:
            descriptor = klass.__dict__["schSlack"]
            break
    assert isinstance(descriptor, property)



def test_gaanalysiscontext_is_not_abstract():
    assert not inspect.isabstract(GaAnalysisContext)


def test_gaanalysiscontext_constructor_exists():
    assert callable(GaAnalysisContext.__init__)


def test_gaanalysiscontext_constructor_args():
    sig = inspect.signature(GaAnalysisContext.__init__)
    params = list(sig.parameters.keys())



def test_marte_sam_saanalysiscontext_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaAnalysisContext)


def test_marte_sam_saanalysiscontext_constructor_exists():
    assert callable(MARTE_SAM_SaAnalysisContext.__init__)


def test_marte_sam_saanalysiscontext_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaAnalysisContext.__init__)
    params = list(sig.parameters.keys())
    assert "isSched" in params, "Missing parameter 'isSched'"
    assert "optCriterion" in params, "Missing parameter 'optCriterion'"

def test_marte_sam_saanalysiscontext_has_isSched():
    assert hasattr(MARTE_SAM_SaAnalysisContext, "isSched")
    descriptor = None
    for klass in MARTE_SAM_SaAnalysisContext.__mro__:
        if "isSched" in klass.__dict__:
            descriptor = klass.__dict__["isSched"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_saanalysiscontext_has_optCriterion():
    assert hasattr(MARTE_SAM_SaAnalysisContext, "optCriterion")
    descriptor = None
    for klass in MARTE_SAM_SaAnalysisContext.__mro__:
        if "optCriterion" in klass.__dict__:
            descriptor = klass.__dict__["optCriterion"]
            break
    assert isinstance(descriptor, property)



def test_gqam_marte_classifier_is_not_abstract():
    assert not inspect.isabstract(GQAM_MARTE_Classifier)


def test_gqam_marte_classifier_constructor_exists():
    assert callable(GQAM_MARTE_Classifier.__init__)


def test_gqam_marte_classifier_constructor_args():
    sig = inspect.signature(GQAM_MARTE_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_garesourcesplatform_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaResourcesPlatform)


def test_marte_gqam_garesourcesplatform_constructor_exists():
    assert callable(MARTE_GQAM_GaResourcesPlatform.__init__)


def test_marte_gqam_garesourcesplatform_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaResourcesPlatform.__init__)
    params = list(sig.parameters.keys())



def test_gqam_garesourcesplatform_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaResourcesPlatform)


def test_gqam_garesourcesplatform_constructor_exists():
    assert callable(GQAM_GaResourcesPlatform.__init__)


def test_gqam_garesourcesplatform_constructor_args():
    sig = inspect.signature(GQAM_GaResourcesPlatform.__init__)
    params = list(sig.parameters.keys())



def test_gqam_gaworkloadbehavior_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaWorkloadBehavior)


def test_gqam_gaworkloadbehavior_constructor_exists():
    assert callable(GQAM_GaWorkloadBehavior.__init__)


def test_gqam_gaworkloadbehavior_constructor_args():
    sig = inspect.signature(GQAM_GaWorkloadBehavior.__init__)
    params = list(sig.parameters.keys())



def test_variables_expressioncontext_is_not_abstract():
    assert not inspect.isabstract(Variables_ExpressionContext)


def test_variables_expressioncontext_constructor_exists():
    assert callable(Variables_ExpressionContext.__init__)


def test_variables_expressioncontext_constructor_args():
    sig = inspect.signature(Variables_ExpressionContext.__init__)
    params = list(sig.parameters.keys())



def test_coreelements_configuration_is_not_abstract():
    assert not inspect.isabstract(CoreElements_Configuration)


def test_coreelements_configuration_constructor_exists():
    assert callable(CoreElements_Configuration.__init__)


def test_coreelements_configuration_constructor_args():
    sig = inspect.signature(CoreElements_Configuration.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gaanalysiscontext_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaAnalysisContext)


def test_marte_gqam_gaanalysiscontext_constructor_exists():
    assert callable(MARTE_GQAM_GaAnalysisContext.__init__)


def test_marte_gqam_gaanalysiscontext_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaAnalysisContext.__init__)
    params = list(sig.parameters.keys())
    assert "context" in params, "Missing parameter 'context'"

def test_marte_gqam_gaanalysiscontext_has_context():
    assert hasattr(MARTE_GQAM_GaAnalysisContext, "context")
    descriptor = None
    for klass in MARTE_GQAM_GaAnalysisContext.__mro__:
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



def test_marte_sam_sacommstep_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaCommStep)


def test_marte_sam_sacommstep_constructor_exists():
    assert callable(MARTE_SAM_SaCommStep.__init__)


def test_marte_sam_sacommstep_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaCommStep.__init__)
    params = list(sig.parameters.keys())
    assert "deadline" in params, "Missing parameter 'deadline'"
    assert "schSlack" in params, "Missing parameter 'schSlack'"
    assert "spareCap" in params, "Missing parameter 'spareCap'"

def test_marte_sam_sacommstep_has_deadline():
    assert hasattr(MARTE_SAM_SaCommStep, "deadline")
    descriptor = None
    for klass in MARTE_SAM_SaCommStep.__mro__:
        if "deadline" in klass.__dict__:
            descriptor = klass.__dict__["deadline"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sacommstep_has_schSlack():
    assert hasattr(MARTE_SAM_SaCommStep, "schSlack")
    descriptor = None
    for klass in MARTE_SAM_SaCommStep.__mro__:
        if "schSlack" in klass.__dict__:
            descriptor = klass.__dict__["schSlack"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sacommstep_has_spareCap():
    assert hasattr(MARTE_SAM_SaCommStep, "spareCap")
    descriptor = None
    for klass in MARTE_SAM_SaCommStep.__mro__:
        if "spareCap" in klass.__dict__:
            descriptor = klass.__dict__["spareCap"]
            break
    assert isinstance(descriptor, property)



def test_sam_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(SAM_MARTE_NamedElement)


def test_sam_marte_namedelement_constructor_exists():
    assert callable(SAM_MARTE_NamedElement.__init__)


def test_sam_marte_namedelement_constructor_args():
    sig = inspect.signature(SAM_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gaworkloadbehavior_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaWorkloadBehavior)


def test_marte_gqam_gaworkloadbehavior_constructor_exists():
    assert callable(MARTE_GQAM_GaWorkloadBehavior.__init__)


def test_marte_gqam_gaworkloadbehavior_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaWorkloadBehavior.__init__)
    params = list(sig.parameters.keys())



def test_schedulableresource_is_not_abstract():
    assert not inspect.isabstract(SchedulableResource)


def test_schedulableresource_constructor_exists():
    assert callable(SchedulableResource.__init__)


def test_schedulableresource_constructor_args():
    sig = inspect.signature(SchedulableResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gacommchannel_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaCommChannel)


def test_marte_gqam_gacommchannel_constructor_exists():
    assert callable(MARTE_GQAM_GaCommChannel.__init__)


def test_marte_gqam_gacommchannel_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaCommChannel.__init__)
    params = list(sig.parameters.keys())
    assert "utilization" in params, "Missing parameter 'utilization'"
    assert "packetSize" in params, "Missing parameter 'packetSize'"

def test_marte_gqam_gacommchannel_has_utilization():
    assert hasattr(MARTE_GQAM_GaCommChannel, "utilization")
    descriptor = None
    for klass in MARTE_GQAM_GaCommChannel.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gacommchannel_has_packetSize():
    assert hasattr(MARTE_GQAM_GaCommChannel, "packetSize")
    descriptor = None
    for klass in MARTE_GQAM_GaCommChannel.__mro__:
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



def test_marte_sam_saschedobs_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaSchedObs)


def test_marte_sam_saschedobs_constructor_exists():
    assert callable(MARTE_SAM_SaSchedObs.__init__)


def test_marte_sam_saschedobs_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaSchedObs.__init__)
    params = list(sig.parameters.keys())
    assert "blockT" in params, "Missing parameter 'blockT'"
    assert "suspentions" in params, "Missing parameter 'suspentions'"
    assert "overlaps" in params, "Missing parameter 'overlaps'"

def test_marte_sam_saschedobs_has_blockT():
    assert hasattr(MARTE_SAM_SaSchedObs, "blockT")
    descriptor = None
    for klass in MARTE_SAM_SaSchedObs.__mro__:
        if "blockT" in klass.__dict__:
            descriptor = klass.__dict__["blockT"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_saschedobs_has_suspentions():
    assert hasattr(MARTE_SAM_SaSchedObs, "suspentions")
    descriptor = None
    for klass in MARTE_SAM_SaSchedObs.__mro__:
        if "suspentions" in klass.__dict__:
            descriptor = klass.__dict__["suspentions"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_saschedobs_has_overlaps():
    assert hasattr(MARTE_SAM_SaSchedObs, "overlaps")
    descriptor = None
    for klass in MARTE_SAM_SaSchedObs.__mro__:
        if "overlaps" in klass.__dict__:
            descriptor = klass.__dict__["overlaps"]
            break
    assert isinstance(descriptor, property)



def test_marte_gqam_galatencyobs_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaLatencyObs)


def test_marte_gqam_galatencyobs_constructor_exists():
    assert callable(MARTE_GQAM_GaLatencyObs.__init__)


def test_marte_gqam_galatencyobs_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaLatencyObs.__init__)
    params = list(sig.parameters.keys())
    assert "miss" in params, "Missing parameter 'miss'"
    assert "latency" in params, "Missing parameter 'latency'"
    assert "utility" in params, "Missing parameter 'utility'"
    assert "maxJitter" in params, "Missing parameter 'maxJitter'"

def test_marte_gqam_galatencyobs_has_miss():
    assert hasattr(MARTE_GQAM_GaLatencyObs, "miss")
    descriptor = None
    for klass in MARTE_GQAM_GaLatencyObs.__mro__:
        if "miss" in klass.__dict__:
            descriptor = klass.__dict__["miss"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_galatencyobs_has_latency():
    assert hasattr(MARTE_GQAM_GaLatencyObs, "latency")
    descriptor = None
    for klass in MARTE_GQAM_GaLatencyObs.__mro__:
        if "latency" in klass.__dict__:
            descriptor = klass.__dict__["latency"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_galatencyobs_has_utility():
    assert hasattr(MARTE_GQAM_GaLatencyObs, "utility")
    descriptor = None
    for klass in MARTE_GQAM_GaLatencyObs.__mro__:
        if "utility" in klass.__dict__:
            descriptor = klass.__dict__["utility"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_galatencyobs_has_maxJitter():
    assert hasattr(MARTE_GQAM_GaLatencyObs, "maxJitter")
    descriptor = None
    for klass in MARTE_GQAM_GaLatencyObs.__mro__:
        if "maxJitter" in klass.__dict__:
            descriptor = klass.__dict__["maxJitter"]
            break
    assert isinstance(descriptor, property)



def test_gqam_marte_timeobservation_is_not_abstract():
    assert not inspect.isabstract(GQAM_MARTE_TimeObservation)


def test_gqam_marte_timeobservation_constructor_exists():
    assert callable(GQAM_MARTE_TimeObservation.__init__)


def test_gqam_marte_timeobservation_constructor_args():
    sig = inspect.signature(GQAM_MARTE_TimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_nfpconstraint_is_not_abstract():
    assert not inspect.isabstract(NfpConstraint)


def test_nfpconstraint_constructor_exists():
    assert callable(NfpConstraint.__init__)


def test_nfpconstraint_constructor_args():
    sig = inspect.signature(NfpConstraint.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gatimedobs_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaTimedObs)


def test_marte_gqam_gatimedobs_constructor_exists():
    assert callable(MARTE_GQAM_GaTimedObs.__init__)


def test_marte_gqam_gatimedobs_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaTimedObs.__init__)
    params = list(sig.parameters.keys())
    assert "laxity" in params, "Missing parameter 'laxity'"

def test_marte_gqam_gatimedobs_has_laxity():
    assert hasattr(MARTE_GQAM_GaTimedObs, "laxity")
    descriptor = None
    for klass in MARTE_GQAM_GaTimedObs.__mro__:
        if "laxity" in klass.__dict__:
            descriptor = klass.__dict__["laxity"]
            break
    assert isinstance(descriptor, property)



def test_gqam_marte_operation_is_not_abstract():
    assert not inspect.isabstract(GQAM_MARTE_Operation)


def test_gqam_marte_operation_constructor_exists():
    assert callable(GQAM_MARTE_Operation.__init__)


def test_gqam_marte_operation_constructor_args():
    sig = inspect.signature(GQAM_MARTE_Operation.__init__)
    params = list(sig.parameters.keys())



def test_gastep_is_not_abstract():
    assert not inspect.isabstract(GaStep)


def test_gastep_constructor_exists():
    assert callable(GaStep.__init__)


def test_gastep_constructor_args():
    sig = inspect.signature(GaStep.__init__)
    params = list(sig.parameters.keys())



def test_marte_pam_parespassstep_is_not_abstract():
    assert not inspect.isabstract(MARTE_PAM_PaResPassStep)


def test_marte_pam_parespassstep_constructor_exists():
    assert callable(MARTE_PAM_PaResPassStep.__init__)


def test_marte_pam_parespassstep_constructor_args():
    sig = inspect.signature(MARTE_PAM_PaResPassStep.__init__)
    params = list(sig.parameters.keys())
    assert "resUnits" in params, "Missing parameter 'resUnits'"

def test_marte_pam_parespassstep_has_resUnits():
    assert hasattr(MARTE_PAM_PaResPassStep, "resUnits")
    descriptor = None
    for klass in MARTE_PAM_PaResPassStep.__mro__:
        if "resUnits" in klass.__dict__:
            descriptor = klass.__dict__["resUnits"]
            break
    assert isinstance(descriptor, property)



def test_marte_gqam_gacommstep_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaCommStep)


def test_marte_gqam_gacommstep_constructor_exists():
    assert callable(MARTE_GQAM_GaCommStep.__init__)


def test_marte_gqam_gacommstep_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaCommStep.__init__)
    params = list(sig.parameters.keys())



def test_marte_pam_pastep_is_not_abstract():
    assert not inspect.isabstract(MARTE_PAM_PaStep)


def test_marte_pam_pastep_constructor_exists():
    assert callable(MARTE_PAM_PaStep.__init__)


def test_marte_pam_pastep_constructor_args():
    sig = inspect.signature(MARTE_PAM_PaStep.__init__)
    params = list(sig.parameters.keys())
    assert "extOpCount" in params, "Missing parameter 'extOpCount'"
    assert "behavCount" in params, "Missing parameter 'behavCount'"
    assert "noSync" in params, "Missing parameter 'noSync'"
    assert "extOpDemand" in params, "Missing parameter 'extOpDemand'"

def test_marte_pam_pastep_has_extOpCount():
    assert hasattr(MARTE_PAM_PaStep, "extOpCount")
    descriptor = None
    for klass in MARTE_PAM_PaStep.__mro__:
        if "extOpCount" in klass.__dict__:
            descriptor = klass.__dict__["extOpCount"]
            break
    assert isinstance(descriptor, property)

def test_marte_pam_pastep_has_behavCount():
    assert hasattr(MARTE_PAM_PaStep, "behavCount")
    descriptor = None
    for klass in MARTE_PAM_PaStep.__mro__:
        if "behavCount" in klass.__dict__:
            descriptor = klass.__dict__["behavCount"]
            break
    assert isinstance(descriptor, property)

def test_marte_pam_pastep_has_noSync():
    assert hasattr(MARTE_PAM_PaStep, "noSync")
    descriptor = None
    for klass in MARTE_PAM_PaStep.__mro__:
        if "noSync" in klass.__dict__:
            descriptor = klass.__dict__["noSync"]
            break
    assert isinstance(descriptor, property)

def test_marte_pam_pastep_has_extOpDemand():
    assert hasattr(MARTE_PAM_PaStep, "extOpDemand")
    descriptor = None
    for klass in MARTE_PAM_PaStep.__mro__:
        if "extOpDemand" in klass.__dict__:
            descriptor = klass.__dict__["extOpDemand"]
            break
    assert isinstance(descriptor, property)



def test_marte_gqam_gaacqstep_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaAcqStep)


def test_marte_gqam_gaacqstep_constructor_exists():
    assert callable(MARTE_GQAM_GaAcqStep.__init__)


def test_marte_gqam_gaacqstep_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaAcqStep.__init__)
    params = list(sig.parameters.keys())
    assert "resUnits" in params, "Missing parameter 'resUnits'"

def test_marte_gqam_gaacqstep_has_resUnits():
    assert hasattr(MARTE_GQAM_GaAcqStep, "resUnits")
    descriptor = None
    for klass in MARTE_GQAM_GaAcqStep.__mro__:
        if "resUnits" in klass.__dict__:
            descriptor = klass.__dict__["resUnits"]
            break
    assert isinstance(descriptor, property)



def test_marte_gqam_garelstep_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaRelStep)


def test_marte_gqam_garelstep_constructor_exists():
    assert callable(MARTE_GQAM_GaRelStep.__init__)


def test_marte_gqam_garelstep_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaRelStep.__init__)
    params = list(sig.parameters.keys())
    assert "resUnits" in params, "Missing parameter 'resUnits'"

def test_marte_gqam_garelstep_has_resUnits():
    assert hasattr(MARTE_GQAM_GaRelStep, "resUnits")
    descriptor = None
    for klass in MARTE_GQAM_GaRelStep.__mro__:
        if "resUnits" in klass.__dict__:
            descriptor = klass.__dict__["resUnits"]
            break
    assert isinstance(descriptor, property)



def test_marte_sam_sastep_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaStep)


def test_marte_sam_sastep_constructor_exists():
    assert callable(MARTE_SAM_SaStep.__init__)


def test_marte_sam_sastep_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaStep.__init__)
    params = list(sig.parameters.keys())
    assert "schSlack" in params, "Missing parameter 'schSlack'"
    assert "deadline" in params, "Missing parameter 'deadline'"
    assert "nonpreemptionBlocking" in params, "Missing parameter 'nonpreemptionBlocking'"
    assert "readyT" in params, "Missing parameter 'readyT'"
    assert "selfSuspensionBlocking" in params, "Missing parameter 'selfSuspensionBlocking'"
    assert "numberSelfSuspensions" in params, "Missing parameter 'numberSelfSuspensions'"
    assert "spareCap" in params, "Missing parameter 'spareCap'"
    assert "preemptT" in params, "Missing parameter 'preemptT'"

def test_marte_sam_sastep_has_schSlack():
    assert hasattr(MARTE_SAM_SaStep, "schSlack")
    descriptor = None
    for klass in MARTE_SAM_SaStep.__mro__:
        if "schSlack" in klass.__dict__:
            descriptor = klass.__dict__["schSlack"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sastep_has_deadline():
    assert hasattr(MARTE_SAM_SaStep, "deadline")
    descriptor = None
    for klass in MARTE_SAM_SaStep.__mro__:
        if "deadline" in klass.__dict__:
            descriptor = klass.__dict__["deadline"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sastep_has_nonpreemptionBlocking():
    assert hasattr(MARTE_SAM_SaStep, "nonpreemptionBlocking")
    descriptor = None
    for klass in MARTE_SAM_SaStep.__mro__:
        if "nonpreemptionBlocking" in klass.__dict__:
            descriptor = klass.__dict__["nonpreemptionBlocking"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sastep_has_readyT():
    assert hasattr(MARTE_SAM_SaStep, "readyT")
    descriptor = None
    for klass in MARTE_SAM_SaStep.__mro__:
        if "readyT" in klass.__dict__:
            descriptor = klass.__dict__["readyT"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sastep_has_selfSuspensionBlocking():
    assert hasattr(MARTE_SAM_SaStep, "selfSuspensionBlocking")
    descriptor = None
    for klass in MARTE_SAM_SaStep.__mro__:
        if "selfSuspensionBlocking" in klass.__dict__:
            descriptor = klass.__dict__["selfSuspensionBlocking"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sastep_has_numberSelfSuspensions():
    assert hasattr(MARTE_SAM_SaStep, "numberSelfSuspensions")
    descriptor = None
    for klass in MARTE_SAM_SaStep.__mro__:
        if "numberSelfSuspensions" in klass.__dict__:
            descriptor = klass.__dict__["numberSelfSuspensions"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sastep_has_spareCap():
    assert hasattr(MARTE_SAM_SaStep, "spareCap")
    descriptor = None
    for klass in MARTE_SAM_SaStep.__mro__:
        if "spareCap" in klass.__dict__:
            descriptor = klass.__dict__["spareCap"]
            break
    assert isinstance(descriptor, property)

def test_marte_sam_sastep_has_preemptT():
    assert hasattr(MARTE_SAM_SaStep, "preemptT")
    descriptor = None
    for klass in MARTE_SAM_SaStep.__mro__:
        if "preemptT" in klass.__dict__:
            descriptor = klass.__dict__["preemptT"]
            break
    assert isinstance(descriptor, property)



def test_marte_gqam_garequestedservice_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaRequestedService)


def test_marte_gqam_garequestedservice_constructor_exists():
    assert callable(MARTE_GQAM_GaRequestedService.__init__)


def test_marte_gqam_garequestedservice_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaRequestedService.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gaexechost_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaExecHost)


def test_marte_gqam_gaexechost_constructor_exists():
    assert callable(MARTE_GQAM_GaExecHost.__init__)


def test_marte_gqam_gaexechost_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaExecHost.__init__)
    params = list(sig.parameters.keys())
    assert "schedPriRange" in params, "Missing parameter 'schedPriRange'"
    assert "utilization" in params, "Missing parameter 'utilization'"
    assert "memSize" in params, "Missing parameter 'memSize'"
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "clockOvh" in params, "Missing parameter 'clockOvh'"
    assert "commRcvOvh" in params, "Missing parameter 'commRcvOvh'"
    assert "cntxtSwT" in params, "Missing parameter 'cntxtSwT'"
    assert "commTxOvh" in params, "Missing parameter 'commTxOvh'"

def test_marte_gqam_gaexechost_has_schedPriRange():
    assert hasattr(MARTE_GQAM_GaExecHost, "schedPriRange")
    descriptor = None
    for klass in MARTE_GQAM_GaExecHost.__mro__:
        if "schedPriRange" in klass.__dict__:
            descriptor = klass.__dict__["schedPriRange"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gaexechost_has_utilization():
    assert hasattr(MARTE_GQAM_GaExecHost, "utilization")
    descriptor = None
    for klass in MARTE_GQAM_GaExecHost.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gaexechost_has_memSize():
    assert hasattr(MARTE_GQAM_GaExecHost, "memSize")
    descriptor = None
    for klass in MARTE_GQAM_GaExecHost.__mro__:
        if "memSize" in klass.__dict__:
            descriptor = klass.__dict__["memSize"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gaexechost_has_throughput():
    assert hasattr(MARTE_GQAM_GaExecHost, "throughput")
    descriptor = None
    for klass in MARTE_GQAM_GaExecHost.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gaexechost_has_clockOvh():
    assert hasattr(MARTE_GQAM_GaExecHost, "clockOvh")
    descriptor = None
    for klass in MARTE_GQAM_GaExecHost.__mro__:
        if "clockOvh" in klass.__dict__:
            descriptor = klass.__dict__["clockOvh"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gaexechost_has_commRcvOvh():
    assert hasattr(MARTE_GQAM_GaExecHost, "commRcvOvh")
    descriptor = None
    for klass in MARTE_GQAM_GaExecHost.__mro__:
        if "commRcvOvh" in klass.__dict__:
            descriptor = klass.__dict__["commRcvOvh"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gaexechost_has_cntxtSwT():
    assert hasattr(MARTE_GQAM_GaExecHost, "cntxtSwT")
    descriptor = None
    for klass in MARTE_GQAM_GaExecHost.__mro__:
        if "cntxtSwT" in klass.__dict__:
            descriptor = klass.__dict__["cntxtSwT"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gaexechost_has_commTxOvh():
    assert hasattr(MARTE_GQAM_GaExecHost, "commTxOvh")
    descriptor = None
    for klass in MARTE_GQAM_GaExecHost.__mro__:
        if "commTxOvh" in klass.__dict__:
            descriptor = klass.__dict__["commTxOvh"]
            break
    assert isinstance(descriptor, property)



def test_gqam_gaexechost_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaExecHost)


def test_gqam_gaexechost_constructor_exists():
    assert callable(GQAM_GaExecHost.__init__)


def test_gqam_gaexechost_constructor_args():
    sig = inspect.signature(GQAM_GaExecHost.__init__)
    params = list(sig.parameters.keys())



def test_gascenario_is_not_abstract():
    assert not inspect.isabstract(GaScenario)


def test_gascenario_constructor_exists():
    assert callable(GaScenario.__init__)


def test_gascenario_constructor_args():
    sig = inspect.signature(GaScenario.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gastep_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaStep)


def test_marte_gqam_gastep_constructor_exists():
    assert callable(MARTE_GQAM_GaStep.__init__)


def test_marte_gqam_gastep_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaStep.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"
    assert "rep" in params, "Missing parameter 'rep'"
    assert "selfDelay" in params, "Missing parameter 'selfDelay'"
    assert "blockT" in params, "Missing parameter 'blockT'"
    assert "servCount" in params, "Missing parameter 'servCount'"
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"
    assert "prob" in params, "Missing parameter 'prob'"

def test_marte_gqam_gastep_has_priority():
    assert hasattr(MARTE_GQAM_GaStep, "priority")
    descriptor = None
    for klass in MARTE_GQAM_GaStep.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gastep_has_rep():
    assert hasattr(MARTE_GQAM_GaStep, "rep")
    descriptor = None
    for klass in MARTE_GQAM_GaStep.__mro__:
        if "rep" in klass.__dict__:
            descriptor = klass.__dict__["rep"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gastep_has_selfDelay():
    assert hasattr(MARTE_GQAM_GaStep, "selfDelay")
    descriptor = None
    for klass in MARTE_GQAM_GaStep.__mro__:
        if "selfDelay" in klass.__dict__:
            descriptor = klass.__dict__["selfDelay"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gastep_has_blockT():
    assert hasattr(MARTE_GQAM_GaStep, "blockT")
    descriptor = None
    for klass in MARTE_GQAM_GaStep.__mro__:
        if "blockT" in klass.__dict__:
            descriptor = klass.__dict__["blockT"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gastep_has_servCount():
    assert hasattr(MARTE_GQAM_GaStep, "servCount")
    descriptor = None
    for klass in MARTE_GQAM_GaStep.__mro__:
        if "servCount" in klass.__dict__:
            descriptor = klass.__dict__["servCount"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gastep_has_isAtomic():
    assert hasattr(MARTE_GQAM_GaStep, "isAtomic")
    descriptor = None
    for klass in MARTE_GQAM_GaStep.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gastep_has_prob():
    assert hasattr(MARTE_GQAM_GaStep, "prob")
    descriptor = None
    for klass in MARTE_GQAM_GaStep.__mro__:
        if "prob" in klass.__dict__:
            descriptor = klass.__dict__["prob"]
            break
    assert isinstance(descriptor, property)



def test_gqam_gatimedobs_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaTimedObs)


def test_gqam_gatimedobs_constructor_exists():
    assert callable(GQAM_GaTimedObs.__init__)


def test_gqam_gatimedobs_constructor_args():
    sig = inspect.signature(GQAM_GaTimedObs.__init__)
    params = list(sig.parameters.keys())



def test_gqam_garequestedservice_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaRequestedService)


def test_gqam_garequestedservice_constructor_exists():
    assert callable(GQAM_GaRequestedService.__init__)


def test_gqam_garequestedservice_constructor_args():
    sig = inspect.signature(GQAM_GaRequestedService.__init__)
    params = list(sig.parameters.keys())



def test_marte_pam_parequestedstep_is_not_abstract():
    assert not inspect.isabstract(MARTE_PAM_PaRequestedStep)


def test_marte_pam_parequestedstep_constructor_exists():
    assert callable(MARTE_PAM_PaRequestedStep.__init__)


def test_marte_pam_parequestedstep_constructor_args():
    sig = inspect.signature(MARTE_PAM_PaRequestedStep.__init__)
    params = list(sig.parameters.keys())



def test_gqam_gaworkloadevent_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaWorkloadEvent)


def test_gqam_gaworkloadevent_constructor_exists():
    assert callable(GQAM_GaWorkloadEvent.__init__)


def test_gqam_gaworkloadevent_constructor_args():
    sig = inspect.signature(GQAM_GaWorkloadEvent.__init__)
    params = list(sig.parameters.keys())



def test_time_timedprocessing_is_not_abstract():
    assert not inspect.isabstract(Time_TimedProcessing)


def test_time_timedprocessing_constructor_exists():
    assert callable(Time_TimedProcessing.__init__)


def test_time_timedprocessing_constructor_args():
    sig = inspect.signature(Time_TimedProcessing.__init__)
    params = list(sig.parameters.keys())



def test_gqam_marte_timeevent_is_not_abstract():
    assert not inspect.isabstract(GQAM_MARTE_TimeEvent)


def test_gqam_marte_timeevent_constructor_exists():
    assert callable(GQAM_MARTE_TimeEvent.__init__)


def test_gqam_marte_timeevent_constructor_args():
    sig = inspect.signature(GQAM_MARTE_TimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_gqam_gascenario_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaScenario)


def test_gqam_gascenario_constructor_exists():
    assert callable(GQAM_GaScenario.__init__)


def test_gqam_gascenario_constructor_args():
    sig = inspect.signature(GQAM_GaScenario.__init__)
    params = list(sig.parameters.keys())



def test_gqam_gaeventtrace_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaEventTrace)


def test_gqam_gaeventtrace_constructor_exists():
    assert callable(GQAM_GaEventTrace.__init__)


def test_gqam_gaeventtrace_constructor_args():
    sig = inspect.signature(GQAM_GaEventTrace.__init__)
    params = list(sig.parameters.keys())



def test_gqam_gaworkloadgenerator_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaWorkloadGenerator)


def test_gqam_gaworkloadgenerator_constructor_exists():
    assert callable(GQAM_GaWorkloadGenerator.__init__)


def test_gqam_gaworkloadgenerator_constructor_args():
    sig = inspect.signature(GQAM_GaWorkloadGenerator.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gaworkloadevent_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaWorkloadEvent)


def test_marte_gqam_gaworkloadevent_constructor_exists():
    assert callable(MARTE_GQAM_GaWorkloadEvent.__init__)


def test_marte_gqam_gaworkloadevent_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaWorkloadEvent.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"

def test_marte_gqam_gaworkloadevent_has_pattern():
    assert hasattr(MARTE_GQAM_GaWorkloadEvent, "pattern")
    descriptor = None
    for klass in MARTE_GQAM_GaWorkloadEvent.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)



def test_gqam_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(GQAM_MARTE_NamedElement)


def test_gqam_marte_namedelement_constructor_exists():
    assert callable(GQAM_MARTE_NamedElement.__init__)


def test_gqam_marte_namedelement_constructor_args():
    sig = inspect.signature(GQAM_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_gqam_gastep_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaStep)


def test_gqam_gastep_constructor_exists():
    assert callable(GQAM_GaStep.__init__)


def test_gqam_gastep_constructor_args():
    sig = inspect.signature(GQAM_GaStep.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gaworkloadgenerator_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaWorkloadGenerator)


def test_marte_gqam_gaworkloadgenerator_constructor_exists():
    assert callable(MARTE_GQAM_GaWorkloadGenerator.__init__)


def test_marte_gqam_gaworkloadgenerator_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaWorkloadGenerator.__init__)
    params = list(sig.parameters.keys())
    assert "pop" in params, "Missing parameter 'pop'"

def test_marte_gqam_gaworkloadgenerator_has_pop():
    assert hasattr(MARTE_GQAM_GaWorkloadGenerator, "pop")
    descriptor = None
    for klass in MARTE_GQAM_GaWorkloadGenerator.__mro__:
        if "pop" in klass.__dict__:
            descriptor = klass.__dict__["pop"]
            break
    assert isinstance(descriptor, property)



def test_marte_gcm_gcminvocatingbehavior_is_not_abstract():
    assert not inspect.isabstract(MARTE_GCM_GCMInvocatingBehavior)


def test_marte_gcm_gcminvocatingbehavior_constructor_exists():
    assert callable(MARTE_GCM_GCMInvocatingBehavior.__init__)


def test_marte_gcm_gcminvocatingbehavior_constructor_args():
    sig = inspect.signature(MARTE_GCM_GCMInvocatingBehavior.__init__)
    params = list(sig.parameters.keys())



def test_gcm_marte_behavior_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_Behavior)


def test_gcm_marte_behavior_constructor_exists():
    assert callable(GCM_MARTE_Behavior.__init__)


def test_gcm_marte_behavior_constructor_args():
    sig = inspect.signature(GCM_MARTE_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_marte_gcm_datapool_is_not_abstract():
    assert not inspect.isabstract(MARTE_GCM_DataPool)


def test_marte_gcm_datapool_constructor_exists():
    assert callable(MARTE_GCM_DataPool.__init__)


def test_marte_gcm_datapool_constructor_args():
    sig = inspect.signature(MARTE_GCM_DataPool.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"

def test_marte_gcm_datapool_has_ordering():
    assert hasattr(MARTE_GCM_DataPool, "ordering")
    descriptor = None
    for klass in MARTE_GCM_DataPool.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)



def test_gcm_marte_classifier_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_Classifier)


def test_gcm_marte_classifier_constructor_exists():
    assert callable(GCM_MARTE_Classifier.__init__)


def test_gcm_marte_classifier_constructor_args():
    sig = inspect.signature(GCM_MARTE_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_gcm_marte_anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_AnyReceiveEvent)


def test_gcm_marte_anyreceiveevent_constructor_exists():
    assert callable(GCM_MARTE_AnyReceiveEvent.__init__)


def test_gcm_marte_anyreceiveevent_constructor_args():
    sig = inspect.signature(GCM_MARTE_AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_marte_gcm_dataevent_is_not_abstract():
    assert not inspect.isabstract(MARTE_GCM_DataEvent)


def test_marte_gcm_dataevent_constructor_exists():
    assert callable(MARTE_GCM_DataEvent.__init__)


def test_marte_gcm_dataevent_constructor_args():
    sig = inspect.signature(MARTE_GCM_DataEvent.__init__)
    params = list(sig.parameters.keys())



def test_gcm_marte_invocationaction_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_InvocationAction)


def test_gcm_marte_invocationaction_constructor_exists():
    assert callable(GCM_MARTE_InvocationAction.__init__)


def test_gcm_marte_invocationaction_constructor_args():
    sig = inspect.signature(GCM_MARTE_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_marte_gcm_gcminvocationaction_is_not_abstract():
    assert not inspect.isabstract(MARTE_GCM_GCMInvocationAction)


def test_marte_gcm_gcminvocationaction_constructor_exists():
    assert callable(MARTE_GCM_GCMInvocationAction.__init__)


def test_marte_gcm_gcminvocationaction_constructor_args():
    sig = inspect.signature(MARTE_GCM_GCMInvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_gcm_marte_feature_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_Feature)


def test_gcm_marte_feature_constructor_exists():
    assert callable(GCM_MARTE_Feature.__init__)


def test_gcm_marte_feature_constructor_args():
    sig = inspect.signature(GCM_MARTE_Feature.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gaeventtrace_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaEventTrace)


def test_marte_gqam_gaeventtrace_constructor_exists():
    assert callable(MARTE_GQAM_GaEventTrace.__init__)


def test_marte_gqam_gaeventtrace_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaEventTrace.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "location" in params, "Missing parameter 'location'"
    assert "format" in params, "Missing parameter 'format'"

def test_marte_gqam_gaeventtrace_has_content():
    assert hasattr(MARTE_GQAM_GaEventTrace, "content")
    descriptor = None
    for klass in MARTE_GQAM_GaEventTrace.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gaeventtrace_has_location():
    assert hasattr(MARTE_GQAM_GaEventTrace, "location")
    descriptor = None
    for klass in MARTE_GQAM_GaEventTrace.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gaeventtrace_has_format():
    assert hasattr(MARTE_GQAM_GaEventTrace, "format")
    descriptor = None
    for klass in MARTE_GQAM_GaEventTrace.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_gqam_marte_behavior_is_not_abstract():
    assert not inspect.isabstract(GQAM_MARTE_Behavior)


def test_gqam_marte_behavior_constructor_exists():
    assert callable(GQAM_MARTE_Behavior.__init__)


def test_gqam_marte_behavior_constructor_args():
    sig = inspect.signature(GQAM_MARTE_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_gcm_marte_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_BehavioralFeature)


def test_gcm_marte_behavioralfeature_constructor_exists():
    assert callable(GCM_MARTE_BehavioralFeature.__init__)


def test_gcm_marte_behavioralfeature_constructor_args():
    sig = inspect.signature(GCM_MARTE_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_marte_gcm_clientserverfeature_is_not_abstract():
    assert not inspect.isabstract(MARTE_GCM_ClientServerFeature)


def test_marte_gcm_clientserverfeature_constructor_exists():
    assert callable(MARTE_GCM_ClientServerFeature.__init__)


def test_marte_gcm_clientserverfeature_constructor_args():
    sig = inspect.signature(MARTE_GCM_ClientServerFeature.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte_gcm_clientserverfeature_has_kind():
    assert hasattr(MARTE_GCM_ClientServerFeature, "kind")
    descriptor = None
    for klass in MARTE_GCM_ClientServerFeature.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_marte_gcm_flowspecification_is_not_abstract():
    assert not inspect.isabstract(MARTE_GCM_FlowSpecification)


def test_marte_gcm_flowspecification_constructor_exists():
    assert callable(MARTE_GCM_FlowSpecification.__init__)


def test_marte_gcm_flowspecification_constructor_args():
    sig = inspect.signature(MARTE_GCM_FlowSpecification.__init__)
    params = list(sig.parameters.keys())



def test_marte_gcm_clientserverspecification_is_not_abstract():
    assert not inspect.isabstract(MARTE_GCM_ClientServerSpecification)


def test_marte_gcm_clientserverspecification_constructor_exists():
    assert callable(MARTE_GCM_ClientServerSpecification.__init__)


def test_marte_gcm_clientserverspecification_constructor_args():
    sig = inspect.signature(MARTE_GCM_ClientServerSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gcm_clientserverspecification_is_not_abstract():
    assert not inspect.isabstract(GCM_ClientServerSpecification)


def test_gcm_clientserverspecification_constructor_exists():
    assert callable(GCM_ClientServerSpecification.__init__)


def test_gcm_clientserverspecification_constructor_args():
    sig = inspect.signature(GCM_ClientServerSpecification.__init__)
    params = list(sig.parameters.keys())



def test_gcm_marte_interface_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_Interface)


def test_gcm_marte_interface_constructor_exists():
    assert callable(GCM_MARTE_Interface.__init__)


def test_gcm_marte_interface_constructor_args():
    sig = inspect.signature(GCM_MARTE_Interface.__init__)
    params = list(sig.parameters.keys())



def test_marte_gcm_clientserverport_is_not_abstract():
    assert not inspect.isabstract(MARTE_GCM_ClientServerPort)


def test_marte_gcm_clientserverport_constructor_exists():
    assert callable(MARTE_GCM_ClientServerPort.__init__)


def test_marte_gcm_clientserverport_constructor_args():
    sig = inspect.signature(MARTE_GCM_ClientServerPort.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "specificationKind" in params, "Missing parameter 'specificationKind'"

def test_marte_gcm_clientserverport_has_kind():
    assert hasattr(MARTE_GCM_ClientServerPort, "kind")
    descriptor = None
    for klass in MARTE_GCM_ClientServerPort.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_marte_gcm_clientserverport_has_specificationKind():
    assert hasattr(MARTE_GCM_ClientServerPort, "specificationKind")
    descriptor = None
    for klass in MARTE_GCM_ClientServerPort.__mro__:
        if "specificationKind" in klass.__dict__:
            descriptor = klass.__dict__["specificationKind"]
            break
    assert isinstance(descriptor, property)



def test_gcm_marte_port_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_Port)


def test_gcm_marte_port_constructor_exists():
    assert callable(GCM_MARTE_Port.__init__)


def test_gcm_marte_port_constructor_args():
    sig = inspect.signature(GCM_MARTE_Port.__init__)
    params = list(sig.parameters.keys())



def test_marte_gcm_flowport_is_not_abstract():
    assert not inspect.isabstract(MARTE_GCM_FlowPort)


def test_marte_gcm_flowport_constructor_exists():
    assert callable(MARTE_GCM_FlowPort.__init__)


def test_marte_gcm_flowport_constructor_args():
    sig = inspect.signature(MARTE_GCM_FlowPort.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"

def test_marte_gcm_flowport_has_direction():
    assert hasattr(MARTE_GCM_FlowPort, "direction")
    descriptor = None
    for klass in MARTE_GCM_FlowPort.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_marte_gcm_flowport_has_isAtomic():
    assert hasattr(MARTE_GCM_FlowPort, "isAtomic")
    descriptor = None
    for klass in MARTE_GCM_FlowPort.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)



def test_gcm_marte_trigger_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_Trigger)


def test_gcm_marte_trigger_constructor_exists():
    assert callable(GCM_MARTE_Trigger.__init__)


def test_gcm_marte_trigger_constructor_args():
    sig = inspect.signature(GCM_MARTE_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_marte_gcm_gcmtrigger_is_not_abstract():
    assert not inspect.isabstract(MARTE_GCM_GCMTrigger)


def test_marte_gcm_gcmtrigger_constructor_exists():
    assert callable(MARTE_GCM_GCMTrigger.__init__)


def test_marte_gcm_gcmtrigger_constructor_args():
    sig = inspect.signature(MARTE_GCM_GCMTrigger.__init__)
    params = list(sig.parameters.keys())



def test_marte_gcm_flowproperty_is_not_abstract():
    assert not inspect.isabstract(MARTE_GCM_FlowProperty)


def test_marte_gcm_flowproperty_constructor_exists():
    assert callable(MARTE_GCM_FlowProperty.__init__)


def test_marte_gcm_flowproperty_constructor_args():
    sig = inspect.signature(MARTE_GCM_FlowProperty.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_marte_gcm_flowproperty_has_direction():
    assert hasattr(MARTE_GCM_FlowProperty, "direction")
    descriptor = None
    for klass in MARTE_GCM_FlowProperty.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_sw_interaction_swsynchronizationresource_is_not_abstract():
    assert not inspect.isabstract(SW_Interaction_SwSynchronizationResource)


def test_sw_interaction_swsynchronizationresource_constructor_exists():
    assert callable(SW_Interaction_SwSynchronizationResource.__init__)


def test_sw_interaction_swsynchronizationresource_constructor_args():
    sig = inspect.signature(SW_Interaction_SwSynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_interaction_swmutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Interaction_SwMutualExclusionResource)


def test_marte_sw_interaction_swmutualexclusionresource_constructor_exists():
    assert callable(MARTE_SW_Interaction_SwMutualExclusionResource.__init__)


def test_marte_sw_interaction_swmutualexclusionresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Interaction_SwMutualExclusionResource.__init__)
    params = list(sig.parameters.keys())
    assert "mechanism" in params, "Missing parameter 'mechanism'"
    assert "concurrentAccessProtocol" in params, "Missing parameter 'concurrentAccessProtocol'"

def test_marte_sw_interaction_swmutualexclusionresource_has_mechanism():
    assert hasattr(MARTE_SW_Interaction_SwMutualExclusionResource, "mechanism")
    descriptor = None
    for klass in MARTE_SW_Interaction_SwMutualExclusionResource.__mro__:
        if "mechanism" in klass.__dict__:
            descriptor = klass.__dict__["mechanism"]
            break
    assert isinstance(descriptor, property)

def test_marte_sw_interaction_swmutualexclusionresource_has_concurrentAccessProtocol():
    assert hasattr(MARTE_SW_Interaction_SwMutualExclusionResource, "concurrentAccessProtocol")
    descriptor = None
    for klass in MARTE_SW_Interaction_SwMutualExclusionResource.__mro__:
        if "concurrentAccessProtocol" in klass.__dict__:
            descriptor = klass.__dict__["concurrentAccessProtocol"]
            break
    assert isinstance(descriptor, property)



def test_swsynchronizationresource_is_not_abstract():
    assert not inspect.isabstract(SwSynchronizationResource)


def test_swsynchronizationresource_constructor_exists():
    assert callable(SwSynchronizationResource.__init__)


def test_swsynchronizationresource_constructor_args():
    sig = inspect.signature(SwSynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_interaction_notificationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Interaction_NotificationResource)


def test_marte_sw_interaction_notificationresource_constructor_exists():
    assert callable(MARTE_SW_Interaction_NotificationResource.__init__)


def test_marte_sw_interaction_notificationresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Interaction_NotificationResource.__init__)
    params = list(sig.parameters.keys())
    assert "occurence" in params, "Missing parameter 'occurence'"
    assert "mechanism" in params, "Missing parameter 'mechanism'"

def test_marte_sw_interaction_notificationresource_has_occurence():
    assert hasattr(MARTE_SW_Interaction_NotificationResource, "occurence")
    descriptor = None
    for klass in MARTE_SW_Interaction_NotificationResource.__mro__:
        if "occurence" in klass.__dict__:
            descriptor = klass.__dict__["occurence"]
            break
    assert isinstance(descriptor, property)

def test_marte_sw_interaction_notificationresource_has_mechanism():
    assert hasattr(MARTE_SW_Interaction_NotificationResource, "mechanism")
    descriptor = None
    for klass in MARTE_SW_Interaction_NotificationResource.__mro__:
        if "mechanism" in klass.__dict__:
            descriptor = klass.__dict__["mechanism"]
            break
    assert isinstance(descriptor, property)



def test_gcm_marte_property_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_Property)


def test_gcm_marte_property_constructor_exists():
    assert callable(GCM_MARTE_Property.__init__)


def test_gcm_marte_property_constructor_args():
    sig = inspect.signature(GCM_MARTE_Property.__init__)
    params = list(sig.parameters.keys())



def test_sw_interaction_marte_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SW_Interaction_MARTE_BehavioralFeature)


def test_sw_interaction_marte_behavioralfeature_constructor_exists():
    assert callable(SW_Interaction_MARTE_BehavioralFeature.__init__)


def test_sw_interaction_marte_behavioralfeature_constructor_args():
    sig = inspect.signature(SW_Interaction_MARTE_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_swcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(SwCommunicationResource)


def test_swcommunicationresource_constructor_exists():
    assert callable(SwCommunicationResource.__init__)


def test_swcommunicationresource_constructor_args():
    sig = inspect.signature(SwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_interaction_messagecomresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Interaction_MessageComResource)


def test_marte_sw_interaction_messagecomresource_constructor_exists():
    assert callable(MARTE_SW_Interaction_MessageComResource.__init__)


def test_marte_sw_interaction_messagecomresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Interaction_MessageComResource.__init__)
    params = list(sig.parameters.keys())
    assert "messageQueuePolicy" in params, "Missing parameter 'messageQueuePolicy'"
    assert "isFixedMessageSize" in params, "Missing parameter 'isFixedMessageSize'"
    assert "mechanism" in params, "Missing parameter 'mechanism'"

def test_marte_sw_interaction_messagecomresource_has_messageQueuePolicy():
    assert hasattr(MARTE_SW_Interaction_MessageComResource, "messageQueuePolicy")
    descriptor = None
    for klass in MARTE_SW_Interaction_MessageComResource.__mro__:
        if "messageQueuePolicy" in klass.__dict__:
            descriptor = klass.__dict__["messageQueuePolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte_sw_interaction_messagecomresource_has_isFixedMessageSize():
    assert hasattr(MARTE_SW_Interaction_MessageComResource, "isFixedMessageSize")
    descriptor = None
    for klass in MARTE_SW_Interaction_MessageComResource.__mro__:
        if "isFixedMessageSize" in klass.__dict__:
            descriptor = klass.__dict__["isFixedMessageSize"]
            break
    assert isinstance(descriptor, property)

def test_marte_sw_interaction_messagecomresource_has_mechanism():
    assert hasattr(MARTE_SW_Interaction_MessageComResource, "mechanism")
    descriptor = None
    for klass in MARTE_SW_Interaction_MessageComResource.__mro__:
        if "mechanism" in klass.__dict__:
            descriptor = klass.__dict__["mechanism"]
            break
    assert isinstance(descriptor, property)



def test_marte_sw_interaction_shareddatacomresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Interaction_SharedDataComResource)


def test_marte_sw_interaction_shareddatacomresource_constructor_exists():
    assert callable(MARTE_SW_Interaction_SharedDataComResource.__init__)


def test_marte_sw_interaction_shareddatacomresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Interaction_SharedDataComResource.__init__)
    params = list(sig.parameters.keys())



def test_grm_synchronizationresource_is_not_abstract():
    assert not inspect.isabstract(GRM_SynchronizationResource)


def test_grm_synchronizationresource_constructor_exists():
    assert callable(GRM_SynchronizationResource.__init__)


def test_grm_synchronizationresource_constructor_args():
    sig = inspect.signature(GRM_SynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_sw_interaction_swinteractionresource_is_not_abstract():
    assert not inspect.isabstract(SW_Interaction_SwInteractionResource)


def test_sw_interaction_swinteractionresource_constructor_exists():
    assert callable(SW_Interaction_SwInteractionResource.__init__)


def test_sw_interaction_swinteractionresource_constructor_args():
    sig = inspect.signature(SW_Interaction_SwInteractionResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_interaction_swsynchronizationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Interaction_SwSynchronizationResource)


def test_marte_sw_interaction_swsynchronizationresource_constructor_exists():
    assert callable(MARTE_SW_Interaction_SwSynchronizationResource.__init__)


def test_marte_sw_interaction_swsynchronizationresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Interaction_SwSynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_sw_interaction_marte_typedelement_is_not_abstract():
    assert not inspect.isabstract(SW_Interaction_MARTE_TypedElement)


def test_sw_interaction_marte_typedelement_constructor_exists():
    assert callable(SW_Interaction_MARTE_TypedElement.__init__)


def test_sw_interaction_marte_typedelement_constructor_args():
    sig = inspect.signature(SW_Interaction_MARTE_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_sw_brokering_marte_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SW_Brokering_MARTE_BehavioralFeature)


def test_sw_brokering_marte_behavioralfeature_constructor_exists():
    assert callable(SW_Brokering_MARTE_BehavioralFeature.__init__)


def test_sw_brokering_marte_behavioralfeature_constructor_args():
    sig = inspect.signature(SW_Brokering_MARTE_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_sw_brokering_marte_typedelement_is_not_abstract():
    assert not inspect.isabstract(SW_Brokering_MARTE_TypedElement)


def test_sw_brokering_marte_typedelement_constructor_exists():
    assert callable(SW_Brokering_MARTE_TypedElement.__init__)


def test_sw_brokering_marte_typedelement_constructor_args():
    sig = inspect.signature(SW_Brokering_MARTE_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_interruptresource_is_not_abstract():
    assert not inspect.isabstract(InterruptResource)


def test_interruptresource_constructor_exists():
    assert callable(InterruptResource.__init__)


def test_interruptresource_constructor_args():
    sig = inspect.signature(InterruptResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_concurrency_alarm_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Concurrency_Alarm)


def test_marte_sw_concurrency_alarm_constructor_exists():
    assert callable(MARTE_SW_Concurrency_Alarm.__init__)


def test_marte_sw_concurrency_alarm_constructor_args():
    sig = inspect.signature(MARTE_SW_Concurrency_Alarm.__init__)
    params = list(sig.parameters.keys())
    assert "isWatchdog" in params, "Missing parameter 'isWatchdog'"

def test_marte_sw_concurrency_alarm_has_isWatchdog():
    assert hasattr(MARTE_SW_Concurrency_Alarm, "isWatchdog")
    descriptor = None
    for klass in MARTE_SW_Concurrency_Alarm.__mro__:
        if "isWatchdog" in klass.__dict__:
            descriptor = klass.__dict__["isWatchdog"]
            break
    assert isinstance(descriptor, property)



def test_sw_concurrency_marte_namespace_is_not_abstract():
    assert not inspect.isabstract(SW_Concurrency_MARTE_Namespace)


def test_sw_concurrency_marte_namespace_constructor_exists():
    assert callable(SW_Concurrency_MARTE_Namespace.__init__)


def test_sw_concurrency_marte_namespace_constructor_args():
    sig = inspect.signature(SW_Concurrency_MARTE_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_timerresource_is_not_abstract():
    assert not inspect.isabstract(TimerResource)


def test_timerresource_constructor_exists():
    assert callable(TimerResource.__init__)


def test_timerresource_constructor_args():
    sig = inspect.signature(TimerResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_concurrency_swtimerresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Concurrency_SwTimerResource)


def test_marte_sw_concurrency_swtimerresource_constructor_exists():
    assert callable(MARTE_SW_Concurrency_SwTimerResource.__init__)


def test_marte_sw_concurrency_swtimerresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Concurrency_SwTimerResource.__init__)
    params = list(sig.parameters.keys())



def test_sw_concurrency_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(SW_Concurrency_MARTE_NamedElement)


def test_sw_concurrency_marte_namedelement_constructor_exists():
    assert callable(SW_Concurrency_MARTE_NamedElement.__init__)


def test_sw_concurrency_marte_namedelement_constructor_args():
    sig = inspect.signature(SW_Concurrency_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_sw_concurrency_swconcurrentresource_is_not_abstract():
    assert not inspect.isabstract(SW_Concurrency_SwConcurrentResource)


def test_sw_concurrency_swconcurrentresource_constructor_exists():
    assert callable(SW_Concurrency_SwConcurrentResource.__init__)


def test_sw_concurrency_swconcurrentresource_constructor_args():
    sig = inspect.signature(SW_Concurrency_SwConcurrentResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_concurrency_swschedulableresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Concurrency_SwSchedulableResource)


def test_marte_sw_concurrency_swschedulableresource_constructor_exists():
    assert callable(MARTE_SW_Concurrency_SwSchedulableResource.__init__)


def test_marte_sw_concurrency_swschedulableresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Concurrency_SwSchedulableResource.__init__)
    params = list(sig.parameters.keys())
    assert "isPreemptable" in params, "Missing parameter 'isPreemptable'"
    assert "isStaticSchedulingFeature" in params, "Missing parameter 'isStaticSchedulingFeature'"

def test_marte_sw_concurrency_swschedulableresource_has_isPreemptable():
    assert hasattr(MARTE_SW_Concurrency_SwSchedulableResource, "isPreemptable")
    descriptor = None
    for klass in MARTE_SW_Concurrency_SwSchedulableResource.__mro__:
        if "isPreemptable" in klass.__dict__:
            descriptor = klass.__dict__["isPreemptable"]
            break
    assert isinstance(descriptor, property)

def test_marte_sw_concurrency_swschedulableresource_has_isStaticSchedulingFeature():
    assert hasattr(MARTE_SW_Concurrency_SwSchedulableResource, "isStaticSchedulingFeature")
    descriptor = None
    for klass in MARTE_SW_Concurrency_SwSchedulableResource.__mro__:
        if "isStaticSchedulingFeature" in klass.__dict__:
            descriptor = klass.__dict__["isStaticSchedulingFeature"]
            break
    assert isinstance(descriptor, property)



def test_swconcurrentresource_is_not_abstract():
    assert not inspect.isabstract(SwConcurrentResource)


def test_swconcurrentresource_constructor_exists():
    assert callable(SwConcurrentResource.__init__)


def test_swconcurrentresource_constructor_args():
    sig = inspect.signature(SwConcurrentResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_concurrency_interruptresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Concurrency_InterruptResource)


def test_marte_sw_concurrency_interruptresource_constructor_exists():
    assert callable(MARTE_SW_Concurrency_InterruptResource.__init__)


def test_marte_sw_concurrency_interruptresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Concurrency_InterruptResource.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "isMaskable" in params, "Missing parameter 'isMaskable'"

def test_marte_sw_concurrency_interruptresource_has_kind():
    assert hasattr(MARTE_SW_Concurrency_InterruptResource, "kind")
    descriptor = None
    for klass in MARTE_SW_Concurrency_InterruptResource.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_marte_sw_concurrency_interruptresource_has_isMaskable():
    assert hasattr(MARTE_SW_Concurrency_InterruptResource, "isMaskable")
    descriptor = None
    for klass in MARTE_SW_Concurrency_InterruptResource.__mro__:
        if "isMaskable" in klass.__dict__:
            descriptor = klass.__dict__["isMaskable"]
            break
    assert isinstance(descriptor, property)



def test_sw_concurrency_marte_element_is_not_abstract():
    assert not inspect.isabstract(SW_Concurrency_MARTE_Element)


def test_sw_concurrency_marte_element_constructor_exists():
    assert callable(SW_Concurrency_MARTE_Element.__init__)


def test_sw_concurrency_marte_element_constructor_args():
    sig = inspect.signature(SW_Concurrency_MARTE_Element.__init__)
    params = list(sig.parameters.keys())



def test_swresource_is_not_abstract():
    assert not inspect.isabstract(SwResource)


def test_swresource_constructor_exists():
    assert callable(SwResource.__init__)


def test_swresource_constructor_args():
    sig = inspect.signature(SwResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_interaction_swinteractionresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Interaction_SwInteractionResource)


def test_marte_sw_interaction_swinteractionresource_constructor_exists():
    assert callable(MARTE_SW_Interaction_SwInteractionResource.__init__)


def test_marte_sw_interaction_swinteractionresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Interaction_SwInteractionResource.__init__)
    params = list(sig.parameters.keys())
    assert "waitingQueuePolicy" in params, "Missing parameter 'waitingQueuePolicy'"
    assert "waitingQueueCapacity" in params, "Missing parameter 'waitingQueueCapacity'"
    assert "isIntraMemoryPartitionInteraction" in params, "Missing parameter 'isIntraMemoryPartitionInteraction'"

def test_marte_sw_interaction_swinteractionresource_has_waitingQueuePolicy():
    assert hasattr(MARTE_SW_Interaction_SwInteractionResource, "waitingQueuePolicy")
    descriptor = None
    for klass in MARTE_SW_Interaction_SwInteractionResource.__mro__:
        if "waitingQueuePolicy" in klass.__dict__:
            descriptor = klass.__dict__["waitingQueuePolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte_sw_interaction_swinteractionresource_has_waitingQueueCapacity():
    assert hasattr(MARTE_SW_Interaction_SwInteractionResource, "waitingQueueCapacity")
    descriptor = None
    for klass in MARTE_SW_Interaction_SwInteractionResource.__mro__:
        if "waitingQueueCapacity" in klass.__dict__:
            descriptor = klass.__dict__["waitingQueueCapacity"]
            break
    assert isinstance(descriptor, property)

def test_marte_sw_interaction_swinteractionresource_has_isIntraMemoryPartitionInteraction():
    assert hasattr(MARTE_SW_Interaction_SwInteractionResource, "isIntraMemoryPartitionInteraction")
    descriptor = None
    for klass in MARTE_SW_Interaction_SwInteractionResource.__mro__:
        if "isIntraMemoryPartitionInteraction" in klass.__dict__:
            descriptor = klass.__dict__["isIntraMemoryPartitionInteraction"]
            break
    assert isinstance(descriptor, property)



def test_marte_sw_brokering_memorybroker_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Brokering_MemoryBroker)


def test_marte_sw_brokering_memorybroker_constructor_exists():
    assert callable(MARTE_SW_Brokering_MemoryBroker.__init__)


def test_marte_sw_brokering_memorybroker_constructor_args():
    sig = inspect.signature(MARTE_SW_Brokering_MemoryBroker.__init__)
    params = list(sig.parameters.keys())
    assert "accessPolicy" in params, "Missing parameter 'accessPolicy'"

def test_marte_sw_brokering_memorybroker_has_accessPolicy():
    assert hasattr(MARTE_SW_Brokering_MemoryBroker, "accessPolicy")
    descriptor = None
    for klass in MARTE_SW_Brokering_MemoryBroker.__mro__:
        if "accessPolicy" in klass.__dict__:
            descriptor = klass.__dict__["accessPolicy"]
            break
    assert isinstance(descriptor, property)



def test_marte_sw_brokering_devicebroker_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Brokering_DeviceBroker)


def test_marte_sw_brokering_devicebroker_constructor_exists():
    assert callable(MARTE_SW_Brokering_DeviceBroker.__init__)


def test_marte_sw_brokering_devicebroker_constructor_args():
    sig = inspect.signature(MARTE_SW_Brokering_DeviceBroker.__init__)
    params = list(sig.parameters.keys())
    assert "accessPolicy" in params, "Missing parameter 'accessPolicy'"
    assert "isBuffered" in params, "Missing parameter 'isBuffered'"

def test_marte_sw_brokering_devicebroker_has_accessPolicy():
    assert hasattr(MARTE_SW_Brokering_DeviceBroker, "accessPolicy")
    descriptor = None
    for klass in MARTE_SW_Brokering_DeviceBroker.__mro__:
        if "accessPolicy" in klass.__dict__:
            descriptor = klass.__dict__["accessPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte_sw_brokering_devicebroker_has_isBuffered():
    assert hasattr(MARTE_SW_Brokering_DeviceBroker, "isBuffered")
    descriptor = None
    for klass in MARTE_SW_Brokering_DeviceBroker.__mro__:
        if "isBuffered" in klass.__dict__:
            descriptor = klass.__dict__["isBuffered"]
            break
    assert isinstance(descriptor, property)



def test_marte_sw_concurrency_memorypartition_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Concurrency_MemoryPartition)


def test_marte_sw_concurrency_memorypartition_constructor_exists():
    assert callable(MARTE_SW_Concurrency_MemoryPartition.__init__)


def test_marte_sw_concurrency_memorypartition_constructor_args():
    sig = inspect.signature(MARTE_SW_Concurrency_MemoryPartition.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_concurrency_swconcurrentresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Concurrency_SwConcurrentResource)


def test_marte_sw_concurrency_swconcurrentresource_constructor_exists():
    assert callable(MARTE_SW_Concurrency_SwConcurrentResource.__init__)


def test_marte_sw_concurrency_swconcurrentresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Concurrency_SwConcurrentResource.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "activationCapacity" in params, "Missing parameter 'activationCapacity'"

def test_marte_sw_concurrency_swconcurrentresource_has_type():
    assert hasattr(MARTE_SW_Concurrency_SwConcurrentResource, "type")
    descriptor = None
    for klass in MARTE_SW_Concurrency_SwConcurrentResource.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_marte_sw_concurrency_swconcurrentresource_has_activationCapacity():
    assert hasattr(MARTE_SW_Concurrency_SwConcurrentResource, "activationCapacity")
    descriptor = None
    for klass in MARTE_SW_Concurrency_SwConcurrentResource.__mro__:
        if "activationCapacity" in klass.__dict__:
            descriptor = klass.__dict__["activationCapacity"]
            break
    assert isinstance(descriptor, property)



def test_sw_concurrency_marte_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SW_Concurrency_MARTE_BehavioralFeature)


def test_sw_concurrency_marte_behavioralfeature_constructor_exists():
    assert callable(SW_Concurrency_MARTE_BehavioralFeature.__init__)


def test_sw_concurrency_marte_behavioralfeature_constructor_args():
    sig = inspect.signature(SW_Concurrency_MARTE_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_sw_resourcecore_marte_property_is_not_abstract():
    assert not inspect.isabstract(SW_ResourceCore_MARTE_Property)


def test_sw_resourcecore_marte_property_constructor_exists():
    assert callable(SW_ResourceCore_MARTE_Property.__init__)


def test_sw_resourcecore_marte_property_constructor_args():
    sig = inspect.signature(SW_ResourceCore_MARTE_Property.__init__)
    params = list(sig.parameters.keys())



def test_sw_resourcecore_marte_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SW_ResourceCore_MARTE_BehavioralFeature)


def test_sw_resourcecore_marte_behavioralfeature_constructor_exists():
    assert callable(SW_ResourceCore_MARTE_BehavioralFeature.__init__)


def test_sw_resourcecore_marte_behavioralfeature_constructor_args():
    sig = inspect.signature(SW_ResourceCore_MARTE_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_sw_resourcecore_marte_typedelement_is_not_abstract():
    assert not inspect.isabstract(SW_ResourceCore_MARTE_TypedElement)


def test_sw_resourcecore_marte_typedelement_constructor_exists():
    assert callable(SW_ResourceCore_MARTE_TypedElement.__init__)


def test_sw_resourcecore_marte_typedelement_constructor_args():
    sig = inspect.signature(SW_ResourceCore_MARTE_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_sw_concurrency_marte_typedelement_is_not_abstract():
    assert not inspect.isabstract(SW_Concurrency_MARTE_TypedElement)


def test_sw_concurrency_marte_typedelement_constructor_exists():
    assert callable(SW_Concurrency_MARTE_TypedElement.__init__)


def test_sw_concurrency_marte_typedelement_constructor_args():
    sig = inspect.signature(SW_Concurrency_MARTE_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HwComponent)


def test_hwcomponent_constructor_exists():
    assert callable(HwComponent.__init__)


def test_hwcomponent_constructor_args():
    sig = inspect.signature(HwComponent.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwpower_hwcoolingsupply_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPower_HwCoolingSupply)


def test_marte_hwpower_hwcoolingsupply_constructor_exists():
    assert callable(MARTE_HwPower_HwCoolingSupply.__init__)


def test_marte_hwpower_hwcoolingsupply_constructor_args():
    sig = inspect.signature(MARTE_HwPower_HwCoolingSupply.__init__)
    params = list(sig.parameters.keys())
    assert "coolingPower" in params, "Missing parameter 'coolingPower'"

def test_marte_hwpower_hwcoolingsupply_has_coolingPower():
    assert hasattr(MARTE_HwPower_HwCoolingSupply, "coolingPower")
    descriptor = None
    for klass in MARTE_HwPower_HwCoolingSupply.__mro__:
        if "coolingPower" in klass.__dict__:
            descriptor = klass.__dict__["coolingPower"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwpower_hwpowersupply_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPower_HwPowerSupply)


def test_marte_hwpower_hwpowersupply_constructor_exists():
    assert callable(MARTE_HwPower_HwPowerSupply.__init__)


def test_marte_hwpower_hwpowersupply_constructor_args():
    sig = inspect.signature(MARTE_HwPower_HwPowerSupply.__init__)
    params = list(sig.parameters.keys())
    assert "suppliedPower" in params, "Missing parameter 'suppliedPower'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_marte_hwpower_hwpowersupply_has_suppliedPower():
    assert hasattr(MARTE_HwPower_HwPowerSupply, "suppliedPower")
    descriptor = None
    for klass in MARTE_HwPower_HwPowerSupply.__mro__:
        if "suppliedPower" in klass.__dict__:
            descriptor = klass.__dict__["suppliedPower"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwpower_hwpowersupply_has_capacity():
    assert hasattr(MARTE_HwPower_HwPowerSupply, "capacity")
    descriptor = None
    for klass in MARTE_HwPower_HwPowerSupply.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_hwlayout_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HwLayout_HwComponent)


def test_hwlayout_hwcomponent_constructor_exists():
    assert callable(HwLayout_HwComponent.__init__)


def test_hwlayout_hwcomponent_constructor_args():
    sig = inspect.signature(HwLayout_HwComponent.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_resourcecore_swresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_ResourceCore_SwResource)


def test_marte_sw_resourcecore_swresource_constructor_exists():
    assert callable(MARTE_SW_ResourceCore_SwResource.__init__)


def test_marte_sw_resourcecore_swresource_constructor_args():
    sig = inspect.signature(MARTE_SW_ResourceCore_SwResource.__init__)
    params = list(sig.parameters.keys())



def test_hwcommunication_hwendpoint_is_not_abstract():
    assert not inspect.isabstract(HwCommunication_HwEndPoint)


def test_hwcommunication_hwendpoint_constructor_exists():
    assert callable(HwCommunication_HwEndPoint.__init__)


def test_hwcommunication_hwendpoint_constructor_args():
    sig = inspect.signature(HwCommunication_HwEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_hwgeneral_hwresourceservice_is_not_abstract():
    assert not inspect.isabstract(HwGeneral_HwResourceService)


def test_hwgeneral_hwresourceservice_constructor_exists():
    assert callable(HwGeneral_HwResourceService.__init__)


def test_hwgeneral_hwresourceservice_constructor_args():
    sig = inspect.signature(HwGeneral_HwResourceService.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwgeneral_hwresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwGeneral_HwResource)


def test_marte_hwgeneral_hwresource_constructor_exists():
    assert callable(MARTE_HwGeneral_HwResource.__init__)


def test_marte_hwgeneral_hwresource_constructor_args():
    sig = inspect.signature(MARTE_HwGeneral_HwResource.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "frequency" in params, "Missing parameter 'frequency'"

def test_marte_hwgeneral_hwresource_has_description():
    assert hasattr(MARTE_HwGeneral_HwResource, "description")
    descriptor = None
    for klass in MARTE_HwGeneral_HwResource.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwgeneral_hwresource_has_frequency():
    assert hasattr(MARTE_HwGeneral_HwResource, "frequency")
    descriptor = None
    for klass in MARTE_HwGeneral_HwResource.__mro__:
        if "frequency" in klass.__dict__:
            descriptor = klass.__dict__["frequency"]
            break
    assert isinstance(descriptor, property)



def test_hwi_o_is_not_abstract():
    assert not inspect.isabstract(HwI_O)


def test_hwi_o_constructor_exists():
    assert callable(HwI_O.__init__)


def test_hwi_o_constructor_args():
    sig = inspect.signature(HwI_O.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwdevice_hwsensor_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDevice_HWSensor)


def test_marte_hwdevice_hwsensor_constructor_exists():
    assert callable(MARTE_HwDevice_HWSensor.__init__)


def test_marte_hwdevice_hwsensor_constructor_args():
    sig = inspect.signature(MARTE_HwDevice_HWSensor.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwdevice_hwactuator_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDevice_HWActuator)


def test_marte_hwdevice_hwactuator_constructor_exists():
    assert callable(MARTE_HwDevice_HWActuator.__init__)


def test_marte_hwdevice_hwactuator_constructor_args():
    sig = inspect.signature(MARTE_HwDevice_HWActuator.__init__)
    params = list(sig.parameters.keys())



def test_hwtiming_hwclock_is_not_abstract():
    assert not inspect.isabstract(HwTiming_HwClock)


def test_hwtiming_hwclock_constructor_exists():
    assert callable(HwTiming_HwClock.__init__)


def test_hwtiming_hwclock_constructor_args():
    sig = inspect.signature(HwTiming_HwClock.__init__)
    params = list(sig.parameters.keys())



def test_hwtimingresource_is_not_abstract():
    assert not inspect.isabstract(HwTimingResource)


def test_hwtimingresource_constructor_exists():
    assert callable(HwTimingResource.__init__)


def test_hwtimingresource_constructor_args():
    sig = inspect.signature(HwTimingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwtiming_hwtimer_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwTiming_HwTimer)


def test_marte_hwtiming_hwtimer_constructor_exists():
    assert callable(MARTE_HwTiming_HwTimer.__init__)


def test_marte_hwtiming_hwtimer_constructor_args():
    sig = inspect.signature(MARTE_HwTiming_HwTimer.__init__)
    params = list(sig.parameters.keys())
    assert "counterWidth" in params, "Missing parameter 'counterWidth'"
    assert "nbCounters" in params, "Missing parameter 'nbCounters'"

def test_marte_hwtiming_hwtimer_has_counterWidth():
    assert hasattr(MARTE_HwTiming_HwTimer, "counterWidth")
    descriptor = None
    for klass in MARTE_HwTiming_HwTimer.__mro__:
        if "counterWidth" in klass.__dict__:
            descriptor = klass.__dict__["counterWidth"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwtiming_hwtimer_has_nbCounters():
    assert hasattr(MARTE_HwTiming_HwTimer, "nbCounters")
    descriptor = None
    for klass in MARTE_HwTiming_HwTimer.__mro__:
        if "nbCounters" in klass.__dict__:
            descriptor = klass.__dict__["nbCounters"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwtiming_hwclock_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwTiming_HwClock)


def test_marte_hwtiming_hwclock_constructor_exists():
    assert callable(MARTE_HwTiming_HwClock.__init__)


def test_marte_hwtiming_hwclock_constructor_args():
    sig = inspect.signature(MARTE_HwTiming_HwClock.__init__)
    params = list(sig.parameters.keys())



def test_grm_timingresource_is_not_abstract():
    assert not inspect.isabstract(GRM_TimingResource)


def test_grm_timingresource_constructor_exists():
    assert callable(GRM_TimingResource.__init__)


def test_grm_timingresource_constructor_args():
    sig = inspect.signature(GRM_TimingResource.__init__)
    params = list(sig.parameters.keys())



def test_hwdevice_is_not_abstract():
    assert not inspect.isabstract(HwDevice)


def test_hwdevice_constructor_exists():
    assert callable(HwDevice.__init__)


def test_hwdevice_constructor_args():
    sig = inspect.signature(HwDevice.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwdevice_hwsupport_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDevice_HwSupport)


def test_marte_hwdevice_hwsupport_constructor_exists():
    assert callable(MARTE_HwDevice_HwSupport.__init__)


def test_marte_hwdevice_hwsupport_constructor_args():
    sig = inspect.signature(MARTE_HwDevice_HwSupport.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwdevice_hwi_o_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDevice_HwI_O)


def test_marte_hwdevice_hwi_o_constructor_exists():
    assert callable(MARTE_HwDevice_HwI_O.__init__)


def test_marte_hwdevice_hwi_o_constructor_args():
    sig = inspect.signature(MARTE_HwDevice_HwI_O.__init__)
    params = list(sig.parameters.keys())



def test_grm_deviceresource_is_not_abstract():
    assert not inspect.isabstract(GRM_DeviceResource)


def test_grm_deviceresource_constructor_exists():
    assert callable(GRM_DeviceResource.__init__)


def test_grm_deviceresource_constructor_args():
    sig = inspect.signature(GRM_DeviceResource.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory_is_not_abstract():
    assert not inspect.isabstract(HwMemory)


def test_hwmemory_constructor_exists():
    assert callable(HwMemory.__init__)


def test_hwmemory_constructor_args():
    sig = inspect.signature(HwMemory.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwmemory_hwrom_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_HwROM)


def test_marte_hwmemory_hwrom_constructor_exists():
    assert callable(MARTE_HwMemory_HwROM.__init__)


def test_marte_hwmemory_hwrom_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_HwROM.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "organization" in params, "Missing parameter 'organization'"

def test_marte_hwmemory_hwrom_has_type():
    assert hasattr(MARTE_HwMemory_HwROM, "type")
    descriptor = None
    for klass in MARTE_HwMemory_HwROM.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwrom_has_organization():
    assert hasattr(MARTE_HwMemory_HwROM, "organization")
    descriptor = None
    for klass in MARTE_HwMemory_HwROM.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwmemory_hwdrive_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_HwDrive)


def test_marte_hwmemory_hwdrive_constructor_exists():
    assert callable(MARTE_HwMemory_HwDrive.__init__)


def test_marte_hwmemory_hwdrive_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_HwDrive.__init__)
    params = list(sig.parameters.keys())
    assert "sectorSize" in params, "Missing parameter 'sectorSize'"

def test_marte_hwmemory_hwdrive_has_sectorSize():
    assert hasattr(MARTE_HwMemory_HwDrive, "sectorSize")
    descriptor = None
    for klass in MARTE_HwMemory_HwDrive.__mro__:
        if "sectorSize" in klass.__dict__:
            descriptor = klass.__dict__["sectorSize"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwmemory_hwcache_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_HwCache)


def test_marte_hwmemory_hwcache_constructor_exists():
    assert callable(MARTE_HwMemory_HwCache.__init__)


def test_marte_hwmemory_hwcache_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_HwCache.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "writePolicy" in params, "Missing parameter 'writePolicy'"
    assert "level" in params, "Missing parameter 'level'"
    assert "repl_Policy" in params, "Missing parameter 'repl_Policy'"
    assert "structure" in params, "Missing parameter 'structure'"

def test_marte_hwmemory_hwcache_has_type():
    assert hasattr(MARTE_HwMemory_HwCache, "type")
    descriptor = None
    for klass in MARTE_HwMemory_HwCache.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwcache_has_writePolicy():
    assert hasattr(MARTE_HwMemory_HwCache, "writePolicy")
    descriptor = None
    for klass in MARTE_HwMemory_HwCache.__mro__:
        if "writePolicy" in klass.__dict__:
            descriptor = klass.__dict__["writePolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwcache_has_level():
    assert hasattr(MARTE_HwMemory_HwCache, "level")
    descriptor = None
    for klass in MARTE_HwMemory_HwCache.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwcache_has_repl_Policy():
    assert hasattr(MARTE_HwMemory_HwCache, "repl_Policy")
    descriptor = None
    for klass in MARTE_HwMemory_HwCache.__mro__:
        if "repl_Policy" in klass.__dict__:
            descriptor = klass.__dict__["repl_Policy"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwcache_has_structure():
    assert hasattr(MARTE_HwMemory_HwCache, "structure")
    descriptor = None
    for klass in MARTE_HwMemory_HwCache.__mro__:
        if "structure" in klass.__dict__:
            descriptor = klass.__dict__["structure"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwmemory_hwram_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_HwRAM)


def test_marte_hwmemory_hwram_constructor_exists():
    assert callable(MARTE_HwMemory_HwRAM.__init__)


def test_marte_hwmemory_hwram_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_HwRAM.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"
    assert "writePolicy" in params, "Missing parameter 'writePolicy'"
    assert "repl_Policy" in params, "Missing parameter 'repl_Policy'"
    assert "isNonVolatile" in params, "Missing parameter 'isNonVolatile'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_marte_hwmemory_hwram_has_isSynchronous():
    assert hasattr(MARTE_HwMemory_HwRAM, "isSynchronous")
    descriptor = None
    for klass in MARTE_HwMemory_HwRAM.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwram_has_writePolicy():
    assert hasattr(MARTE_HwMemory_HwRAM, "writePolicy")
    descriptor = None
    for klass in MARTE_HwMemory_HwRAM.__mro__:
        if "writePolicy" in klass.__dict__:
            descriptor = klass.__dict__["writePolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwram_has_repl_Policy():
    assert hasattr(MARTE_HwMemory_HwRAM, "repl_Policy")
    descriptor = None
    for klass in MARTE_HwMemory_HwRAM.__mro__:
        if "repl_Policy" in klass.__dict__:
            descriptor = klass.__dict__["repl_Policy"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwram_has_isNonVolatile():
    assert hasattr(MARTE_HwMemory_HwRAM, "isNonVolatile")
    descriptor = None
    for klass in MARTE_HwMemory_HwRAM.__mro__:
        if "isNonVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isNonVolatile"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwram_has_organization():
    assert hasattr(MARTE_HwMemory_HwRAM, "organization")
    descriptor = None
    for klass in MARTE_HwMemory_HwRAM.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwram_has_isStatic():
    assert hasattr(MARTE_HwMemory_HwRAM, "isStatic")
    descriptor = None
    for klass in MARTE_HwMemory_HwRAM.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_hwcomputing_hwprocessor_is_not_abstract():
    assert not inspect.isabstract(HwComputing_HwProcessor)


def test_hwcomputing_hwprocessor_constructor_exists():
    assert callable(HwComputing_HwProcessor.__init__)


def test_hwcomputing_hwprocessor_constructor_args():
    sig = inspect.signature(HwComputing_HwProcessor.__init__)
    params = list(sig.parameters.keys())



def test_hwstoragemanager_hwstoragemanager_is_not_abstract():
    assert not inspect.isabstract(HwStorageManager_HwStorageManager)


def test_hwstoragemanager_hwstoragemanager_constructor_exists():
    assert callable(HwStorageManager_HwStorageManager.__init__)


def test_hwstoragemanager_hwstoragemanager_constructor_args():
    sig = inspect.signature(HwStorageManager_HwStorageManager.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory_hwmemory_is_not_abstract():
    assert not inspect.isabstract(HwMemory_HwMemory)


def test_hwmemory_hwmemory_constructor_exists():
    assert callable(HwMemory_HwMemory.__init__)


def test_hwmemory_hwmemory_constructor_args():
    sig = inspect.signature(HwMemory_HwMemory.__init__)
    params = list(sig.parameters.keys())



def test_grm_storageresource_is_not_abstract():
    assert not inspect.isabstract(GRM_StorageResource)


def test_grm_storageresource_constructor_exists():
    assert callable(GRM_StorageResource.__init__)


def test_grm_storageresource_constructor_args():
    sig = inspect.signature(GRM_StorageResource.__init__)
    params = list(sig.parameters.keys())



def test_grm_communicationendpoint_is_not_abstract():
    assert not inspect.isabstract(GRM_CommunicationEndPoint)


def test_grm_communicationendpoint_constructor_exists():
    assert callable(GRM_CommunicationEndPoint.__init__)


def test_grm_communicationendpoint_constructor_args():
    sig = inspect.signature(GRM_CommunicationEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_hwmedia_is_not_abstract():
    assert not inspect.isabstract(HwMedia)


def test_hwmedia_constructor_exists():
    assert callable(HwMedia.__init__)


def test_hwmedia_constructor_args():
    sig = inspect.signature(HwMedia.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcommunication_hwbridge_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwBridge)


def test_marte_hwcommunication_hwbridge_constructor_exists():
    assert callable(MARTE_HwCommunication_HwBridge.__init__)


def test_marte_hwcommunication_hwbridge_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwBridge.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcommunication_hwbus_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwBus)


def test_marte_hwcommunication_hwbus_constructor_exists():
    assert callable(MARTE_HwCommunication_HwBus.__init__)


def test_marte_hwcommunication_hwbus_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwBus.__init__)
    params = list(sig.parameters.keys())
    assert "wordWidth" in params, "Missing parameter 'wordWidth'"
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"
    assert "adressWidth" in params, "Missing parameter 'adressWidth'"
    assert "isSerial" in params, "Missing parameter 'isSerial'"

def test_marte_hwcommunication_hwbus_has_wordWidth():
    assert hasattr(MARTE_HwCommunication_HwBus, "wordWidth")
    descriptor = None
    for klass in MARTE_HwCommunication_HwBus.__mro__:
        if "wordWidth" in klass.__dict__:
            descriptor = klass.__dict__["wordWidth"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcommunication_hwbus_has_isSynchronous():
    assert hasattr(MARTE_HwCommunication_HwBus, "isSynchronous")
    descriptor = None
    for klass in MARTE_HwCommunication_HwBus.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcommunication_hwbus_has_adressWidth():
    assert hasattr(MARTE_HwCommunication_HwBus, "adressWidth")
    descriptor = None
    for klass in MARTE_HwCommunication_HwBus.__mro__:
        if "adressWidth" in klass.__dict__:
            descriptor = klass.__dict__["adressWidth"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcommunication_hwbus_has_isSerial():
    assert hasattr(MARTE_HwCommunication_HwBus, "isSerial")
    descriptor = None
    for klass in MARTE_HwCommunication_HwBus.__mro__:
        if "isSerial" in klass.__dict__:
            descriptor = klass.__dict__["isSerial"]
            break
    assert isinstance(descriptor, property)



def test_hwcommunication_hwarbiter_is_not_abstract():
    assert not inspect.isabstract(HwCommunication_HwArbiter)


def test_hwcommunication_hwarbiter_constructor_exists():
    assert callable(HwCommunication_HwArbiter.__init__)


def test_hwcommunication_hwarbiter_constructor_args():
    sig = inspect.signature(HwCommunication_HwArbiter.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwstoragemanager_hwdma_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwStorageManager_HwDMA)


def test_marte_hwstoragemanager_hwdma_constructor_exists():
    assert callable(MARTE_HwStorageManager_HwDMA.__init__)


def test_marte_hwstoragemanager_hwdma_constructor_args():
    sig = inspect.signature(MARTE_HwStorageManager_HwDMA.__init__)
    params = list(sig.parameters.keys())
    assert "transferWidth" in params, "Missing parameter 'transferWidth'"
    assert "nbChannels" in params, "Missing parameter 'nbChannels'"

def test_marte_hwstoragemanager_hwdma_has_transferWidth():
    assert hasattr(MARTE_HwStorageManager_HwDMA, "transferWidth")
    descriptor = None
    for klass in MARTE_HwStorageManager_HwDMA.__mro__:
        if "transferWidth" in klass.__dict__:
            descriptor = klass.__dict__["transferWidth"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwstoragemanager_hwdma_has_nbChannels():
    assert hasattr(MARTE_HwStorageManager_HwDMA, "nbChannels")
    descriptor = None
    for klass in MARTE_HwStorageManager_HwDMA.__mro__:
        if "nbChannels" in klass.__dict__:
            descriptor = klass.__dict__["nbChannels"]
            break
    assert isinstance(descriptor, property)



def test_hwcommunication_hwcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(HwCommunication_HwCommunicationResource)


def test_hwcommunication_hwcommunicationresource_constructor_exists():
    assert callable(HwCommunication_HwCommunicationResource.__init__)


def test_hwcommunication_hwcommunicationresource_constructor_args():
    sig = inspect.signature(HwCommunication_HwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcommunication_hwendpoint_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwEndPoint)


def test_marte_hwcommunication_hwendpoint_constructor_exists():
    assert callable(MARTE_HwCommunication_HwEndPoint.__init__)


def test_marte_hwcommunication_hwendpoint_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_grm_communicationmedia_is_not_abstract():
    assert not inspect.isabstract(GRM_CommunicationMedia)


def test_grm_communicationmedia_constructor_exists():
    assert callable(GRM_CommunicationMedia.__init__)


def test_grm_communicationmedia_constructor_args():
    sig = inspect.signature(GRM_CommunicationMedia.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gacommhost_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaCommHost)


def test_marte_gqam_gacommhost_constructor_exists():
    assert callable(MARTE_GQAM_GaCommHost.__init__)


def test_marte_gqam_gacommhost_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaCommHost.__init__)
    params = list(sig.parameters.keys())
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "utilization" in params, "Missing parameter 'utilization'"

def test_marte_gqam_gacommhost_has_throughput():
    assert hasattr(MARTE_GQAM_GaCommHost, "throughput")
    descriptor = None
    for klass in MARTE_GQAM_GaCommHost.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gacommhost_has_utilization():
    assert hasattr(MARTE_GQAM_GaCommHost, "utilization")
    descriptor = None
    for klass in MARTE_GQAM_GaCommHost.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)



def test_marte_sw_interaction_swcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Interaction_SwCommunicationResource)


def test_marte_sw_interaction_swcommunicationresource_constructor_exists():
    assert callable(MARTE_SW_Interaction_SwCommunicationResource.__init__)


def test_marte_sw_interaction_swcommunicationresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Interaction_SwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcommunication_hwmedia_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwMedia)


def test_marte_hwcommunication_hwmedia_constructor_exists():
    assert callable(MARTE_HwCommunication_HwMedia.__init__)


def test_marte_hwcommunication_hwmedia_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwMedia.__init__)
    params = list(sig.parameters.keys())
    assert "bandWidth" in params, "Missing parameter 'bandWidth'"

def test_marte_hwcommunication_hwmedia_has_bandWidth():
    assert hasattr(MARTE_HwCommunication_HwMedia, "bandWidth")
    descriptor = None
    for klass in MARTE_HwCommunication_HwMedia.__mro__:
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



def test_marte_hwstoragemanager_hwmmu_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwStorageManager_HwMMU)


def test_marte_hwstoragemanager_hwmmu_constructor_exists():
    assert callable(MARTE_HwStorageManager_HwMMU.__init__)


def test_marte_hwstoragemanager_hwmmu_constructor_args():
    sig = inspect.signature(MARTE_HwStorageManager_HwMMU.__init__)
    params = list(sig.parameters.keys())
    assert "nbEntries" in params, "Missing parameter 'nbEntries'"
    assert "physicalAddrSpace" in params, "Missing parameter 'physicalAddrSpace'"
    assert "memoryProtection" in params, "Missing parameter 'memoryProtection'"
    assert "virtualAddrSpace" in params, "Missing parameter 'virtualAddrSpace'"

def test_marte_hwstoragemanager_hwmmu_has_nbEntries():
    assert hasattr(MARTE_HwStorageManager_HwMMU, "nbEntries")
    descriptor = None
    for klass in MARTE_HwStorageManager_HwMMU.__mro__:
        if "nbEntries" in klass.__dict__:
            descriptor = klass.__dict__["nbEntries"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwstoragemanager_hwmmu_has_physicalAddrSpace():
    assert hasattr(MARTE_HwStorageManager_HwMMU, "physicalAddrSpace")
    descriptor = None
    for klass in MARTE_HwStorageManager_HwMMU.__mro__:
        if "physicalAddrSpace" in klass.__dict__:
            descriptor = klass.__dict__["physicalAddrSpace"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwstoragemanager_hwmmu_has_memoryProtection():
    assert hasattr(MARTE_HwStorageManager_HwMMU, "memoryProtection")
    descriptor = None
    for klass in MARTE_HwStorageManager_HwMMU.__mro__:
        if "memoryProtection" in klass.__dict__:
            descriptor = klass.__dict__["memoryProtection"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwstoragemanager_hwmmu_has_virtualAddrSpace():
    assert hasattr(MARTE_HwStorageManager_HwMMU, "virtualAddrSpace")
    descriptor = None
    for klass in MARTE_HwStorageManager_HwMMU.__mro__:
        if "virtualAddrSpace" in klass.__dict__:
            descriptor = klass.__dict__["virtualAddrSpace"]
            break
    assert isinstance(descriptor, property)



def test_hwcomputing_hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(HwComputing_HwComputingResource)


def test_hwcomputing_hwcomputingresource_constructor_exists():
    assert callable(HwComputing_HwComputingResource.__init__)


def test_hwcomputing_hwcomputingresource_constructor_args():
    sig = inspect.signature(HwComputing_HwComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory_hwram_is_not_abstract():
    assert not inspect.isabstract(HwMemory_HwRAM)


def test_hwmemory_hwram_constructor_exists():
    assert callable(HwMemory_HwRAM.__init__)


def test_hwmemory_hwram_constructor_args():
    sig = inspect.signature(HwMemory_HwRAM.__init__)
    params = list(sig.parameters.keys())



def test_hwresource_is_not_abstract():
    assert not inspect.isabstract(HwResource)


def test_hwresource_constructor_exists():
    assert callable(HwResource.__init__)


def test_hwresource_constructor_args():
    sig = inspect.signature(HwResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcomputing_hwbranchpredictor_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwComputing_HwBranchPredictor)


def test_marte_hwcomputing_hwbranchpredictor_constructor_exists():
    assert callable(MARTE_HwComputing_HwBranchPredictor.__init__)


def test_marte_hwcomputing_hwbranchpredictor_constructor_args():
    sig = inspect.signature(MARTE_HwComputing_HwBranchPredictor.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwlayout_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwLayout_HwComponent)


def test_marte_hwlayout_hwcomponent_constructor_exists():
    assert callable(MARTE_HwLayout_HwComponent.__init__)


def test_marte_hwlayout_hwcomponent_constructor_args():
    sig = inspect.signature(MARTE_HwLayout_HwComponent.__init__)
    params = list(sig.parameters.keys())
    assert "nbPins" in params, "Missing parameter 'nbPins'"
    assert "position" in params, "Missing parameter 'position'"
    assert "staticDissipation" in params, "Missing parameter 'staticDissipation'"
    assert "price" in params, "Missing parameter 'price'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "area" in params, "Missing parameter 'area'"
    assert "grid" in params, "Missing parameter 'grid'"
    assert "dimensions" in params, "Missing parameter 'dimensions'"
    assert "staticConsumption" in params, "Missing parameter 'staticConsumption'"
    assert "r_Conditions" in params, "Missing parameter 'r_Conditions'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte_hwlayout_hwcomponent_has_nbPins():
    assert hasattr(MARTE_HwLayout_HwComponent, "nbPins")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "nbPins" in klass.__dict__:
            descriptor = klass.__dict__["nbPins"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwlayout_hwcomponent_has_position():
    assert hasattr(MARTE_HwLayout_HwComponent, "position")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwlayout_hwcomponent_has_staticDissipation():
    assert hasattr(MARTE_HwLayout_HwComponent, "staticDissipation")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "staticDissipation" in klass.__dict__:
            descriptor = klass.__dict__["staticDissipation"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwlayout_hwcomponent_has_price():
    assert hasattr(MARTE_HwLayout_HwComponent, "price")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwlayout_hwcomponent_has_weight():
    assert hasattr(MARTE_HwLayout_HwComponent, "weight")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwlayout_hwcomponent_has_area():
    assert hasattr(MARTE_HwLayout_HwComponent, "area")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "area" in klass.__dict__:
            descriptor = klass.__dict__["area"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwlayout_hwcomponent_has_grid():
    assert hasattr(MARTE_HwLayout_HwComponent, "grid")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "grid" in klass.__dict__:
            descriptor = klass.__dict__["grid"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwlayout_hwcomponent_has_dimensions():
    assert hasattr(MARTE_HwLayout_HwComponent, "dimensions")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "dimensions" in klass.__dict__:
            descriptor = klass.__dict__["dimensions"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwlayout_hwcomponent_has_staticConsumption():
    assert hasattr(MARTE_HwLayout_HwComponent, "staticConsumption")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "staticConsumption" in klass.__dict__:
            descriptor = klass.__dict__["staticConsumption"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwlayout_hwcomponent_has_r_Conditions():
    assert hasattr(MARTE_HwLayout_HwComponent, "r_Conditions")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "r_Conditions" in klass.__dict__:
            descriptor = klass.__dict__["r_Conditions"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwlayout_hwcomponent_has_kind():
    assert hasattr(MARTE_HwLayout_HwComponent, "kind")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwcommunication_hwcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwCommunicationResource)


def test_marte_hwcommunication_hwcommunicationresource_constructor_exists():
    assert callable(MARTE_HwCommunication_HwCommunicationResource.__init__)


def test_marte_hwcommunication_hwcommunicationresource_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcomputing_hwisa_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwComputing_HwISA)


def test_marte_hwcomputing_hwisa_constructor_exists():
    assert callable(MARTE_HwComputing_HwISA.__init__)


def test_marte_hwcomputing_hwisa_constructor_args():
    sig = inspect.signature(MARTE_HwComputing_HwISA.__init__)
    params = list(sig.parameters.keys())
    assert "family" in params, "Missing parameter 'family'"
    assert "type" in params, "Missing parameter 'type'"
    assert "inst_Width" in params, "Missing parameter 'inst_Width'"

def test_marte_hwcomputing_hwisa_has_family():
    assert hasattr(MARTE_HwComputing_HwISA, "family")
    descriptor = None
    for klass in MARTE_HwComputing_HwISA.__mro__:
        if "family" in klass.__dict__:
            descriptor = klass.__dict__["family"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwisa_has_type():
    assert hasattr(MARTE_HwComputing_HwISA, "type")
    descriptor = None
    for klass in MARTE_HwComputing_HwISA.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwisa_has_inst_Width():
    assert hasattr(MARTE_HwComputing_HwISA, "inst_Width")
    descriptor = None
    for klass in MARTE_HwComputing_HwISA.__mro__:
        if "inst_Width" in klass.__dict__:
            descriptor = klass.__dict__["inst_Width"]
            break
    assert isinstance(descriptor, property)



def test_hwgeneral_hwresource_is_not_abstract():
    assert not inspect.isabstract(HwGeneral_HwResource)


def test_hwgeneral_hwresource_constructor_exists():
    assert callable(HwGeneral_HwResource.__init__)


def test_hwgeneral_hwresource_constructor_args():
    sig = inspect.signature(HwGeneral_HwResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwmemory_hwmemory_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_HwMemory)


def test_marte_hwmemory_hwmemory_constructor_exists():
    assert callable(MARTE_HwMemory_HwMemory.__init__)


def test_marte_hwmemory_hwmemory_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_HwMemory.__init__)
    params = list(sig.parameters.keys())
    assert "adressSize" in params, "Missing parameter 'adressSize'"
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "timings" in params, "Missing parameter 'timings'"
    assert "memorySize" in params, "Missing parameter 'memorySize'"

def test_marte_hwmemory_hwmemory_has_adressSize():
    assert hasattr(MARTE_HwMemory_HwMemory, "adressSize")
    descriptor = None
    for klass in MARTE_HwMemory_HwMemory.__mro__:
        if "adressSize" in klass.__dict__:
            descriptor = klass.__dict__["adressSize"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwmemory_has_throughput():
    assert hasattr(MARTE_HwMemory_HwMemory, "throughput")
    descriptor = None
    for klass in MARTE_HwMemory_HwMemory.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwmemory_has_timings():
    assert hasattr(MARTE_HwMemory_HwMemory, "timings")
    descriptor = None
    for klass in MARTE_HwMemory_HwMemory.__mro__:
        if "timings" in klass.__dict__:
            descriptor = klass.__dict__["timings"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwmemory_hwmemory_has_memorySize():
    assert hasattr(MARTE_HwMemory_HwMemory, "memorySize")
    descriptor = None
    for klass in MARTE_HwMemory_HwMemory.__mro__:
        if "memorySize" in klass.__dict__:
            descriptor = klass.__dict__["memorySize"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwstoragemanager_hwstoragemanager_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwStorageManager_HwStorageManager)


def test_marte_hwstoragemanager_hwstoragemanager_constructor_exists():
    assert callable(MARTE_HwStorageManager_HwStorageManager.__init__)


def test_marte_hwstoragemanager_hwstoragemanager_constructor_args():
    sig = inspect.signature(MARTE_HwStorageManager_HwStorageManager.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwdevice_hwdevice_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDevice_HwDevice)


def test_marte_hwdevice_hwdevice_constructor_exists():
    assert callable(MARTE_HwDevice_HwDevice.__init__)


def test_marte_hwdevice_hwdevice_constructor_args():
    sig = inspect.signature(MARTE_HwDevice_HwDevice.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwtiming_hwtimingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwTiming_HwTimingResource)


def test_marte_hwtiming_hwtimingresource_constructor_exists():
    assert callable(MARTE_HwTiming_HwTimingResource.__init__)


def test_marte_hwtiming_hwtimingresource_constructor_args():
    sig = inspect.signature(MARTE_HwTiming_HwTimingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcomputing_hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwComputing_HwComputingResource)


def test_marte_hwcomputing_hwcomputingresource_constructor_exists():
    assert callable(MARTE_HwComputing_HwComputingResource.__init__)


def test_marte_hwcomputing_hwcomputingresource_constructor_args():
    sig = inspect.signature(MARTE_HwComputing_HwComputingResource.__init__)
    params = list(sig.parameters.keys())
    assert "op_Frequencies" in params, "Missing parameter 'op_Frequencies'"

def test_marte_hwcomputing_hwcomputingresource_has_op_Frequencies():
    assert hasattr(MARTE_HwComputing_HwComputingResource, "op_Frequencies")
    descriptor = None
    for klass in MARTE_HwComputing_HwComputingResource.__mro__:
        if "op_Frequencies" in klass.__dict__:
            descriptor = klass.__dict__["op_Frequencies"]
            break
    assert isinstance(descriptor, property)



def test_hwcommunication_hwmedia_is_not_abstract():
    assert not inspect.isabstract(HwCommunication_HwMedia)


def test_hwcommunication_hwmedia_constructor_exists():
    assert callable(HwCommunication_HwMedia.__init__)


def test_hwcommunication_hwmedia_constructor_args():
    sig = inspect.signature(HwCommunication_HwMedia.__init__)
    params = list(sig.parameters.keys())



def test_hwcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(HwCommunicationResource)


def test_hwcommunicationresource_constructor_exists():
    assert callable(HwCommunicationResource.__init__)


def test_hwcommunicationresource_constructor_args():
    sig = inspect.signature(HwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcommunication_hwarbiter_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwArbiter)


def test_marte_hwcommunication_hwarbiter_constructor_exists():
    assert callable(MARTE_HwCommunication_HwArbiter.__init__)


def test_marte_hwcommunication_hwarbiter_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwArbiter.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory_hwcache_is_not_abstract():
    assert not inspect.isabstract(HwMemory_HwCache)


def test_hwmemory_hwcache_constructor_exists():
    assert callable(HwMemory_HwCache.__init__)


def test_hwmemory_hwcache_constructor_args():
    sig = inspect.signature(HwMemory_HwCache.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputing_hwbranchpredictor_is_not_abstract():
    assert not inspect.isabstract(HwComputing_HwBranchPredictor)


def test_hwcomputing_hwbranchpredictor_constructor_exists():
    assert callable(HwComputing_HwBranchPredictor.__init__)


def test_hwcomputing_hwbranchpredictor_constructor_args():
    sig = inspect.signature(HwComputing_HwBranchPredictor.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputing_hwisa_is_not_abstract():
    assert not inspect.isabstract(HwComputing_HwISA)


def test_hwcomputing_hwisa_constructor_exists():
    assert callable(HwComputing_HwISA.__init__)


def test_hwcomputing_hwisa_constructor_args():
    sig = inspect.signature(HwComputing_HwISA.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(HwComputingResource)


def test_hwcomputingresource_constructor_exists():
    assert callable(HwComputingResource.__init__)


def test_hwcomputingresource_constructor_args():
    sig = inspect.signature(HwComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcomputing_hwpld_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwComputing_HwPLD)


def test_marte_hwcomputing_hwpld_constructor_exists():
    assert callable(MARTE_HwComputing_HwPLD.__init__)


def test_marte_hwcomputing_hwpld_constructor_args():
    sig = inspect.signature(MARTE_HwComputing_HwPLD.__init__)
    params = list(sig.parameters.keys())
    assert "organization" in params, "Missing parameter 'organization'"
    assert "nbFlipFlops" in params, "Missing parameter 'nbFlipFlops'"
    assert "technology" in params, "Missing parameter 'technology'"
    assert "nbLUTs" in params, "Missing parameter 'nbLUTs'"
    assert "ndLUT_Inputs" in params, "Missing parameter 'ndLUT_Inputs'"

def test_marte_hwcomputing_hwpld_has_organization():
    assert hasattr(MARTE_HwComputing_HwPLD, "organization")
    descriptor = None
    for klass in MARTE_HwComputing_HwPLD.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwpld_has_nbFlipFlops():
    assert hasattr(MARTE_HwComputing_HwPLD, "nbFlipFlops")
    descriptor = None
    for klass in MARTE_HwComputing_HwPLD.__mro__:
        if "nbFlipFlops" in klass.__dict__:
            descriptor = klass.__dict__["nbFlipFlops"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwpld_has_technology():
    assert hasattr(MARTE_HwComputing_HwPLD, "technology")
    descriptor = None
    for klass in MARTE_HwComputing_HwPLD.__mro__:
        if "technology" in klass.__dict__:
            descriptor = klass.__dict__["technology"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwpld_has_nbLUTs():
    assert hasattr(MARTE_HwComputing_HwPLD, "nbLUTs")
    descriptor = None
    for klass in MARTE_HwComputing_HwPLD.__mro__:
        if "nbLUTs" in klass.__dict__:
            descriptor = klass.__dict__["nbLUTs"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwpld_has_ndLUT_Inputs():
    assert hasattr(MARTE_HwComputing_HwPLD, "ndLUT_Inputs")
    descriptor = None
    for klass in MARTE_HwComputing_HwPLD.__mro__:
        if "ndLUT_Inputs" in klass.__dict__:
            descriptor = klass.__dict__["ndLUT_Inputs"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwcomputing_hwasic_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwComputing_HwASIC)


def test_marte_hwcomputing_hwasic_constructor_exists():
    assert callable(MARTE_HwComputing_HwASIC.__init__)


def test_marte_hwcomputing_hwasic_constructor_args():
    sig = inspect.signature(MARTE_HwComputing_HwASIC.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcomputing_hwprocessor_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwComputing_HwProcessor)


def test_marte_hwcomputing_hwprocessor_constructor_exists():
    assert callable(MARTE_HwComputing_HwProcessor.__init__)


def test_marte_hwcomputing_hwprocessor_constructor_args():
    sig = inspect.signature(MARTE_HwComputing_HwProcessor.__init__)
    params = list(sig.parameters.keys())
    assert "ipc" in params, "Missing parameter 'ipc'"
    assert "nbStages" in params, "Missing parameter 'nbStages'"
    assert "nbALUs" in params, "Missing parameter 'nbALUs'"
    assert "mips" in params, "Missing parameter 'mips'"
    assert "nbCores" in params, "Missing parameter 'nbCores'"
    assert "architecture" in params, "Missing parameter 'architecture'"
    assert "nbFPUs" in params, "Missing parameter 'nbFPUs'"
    assert "nbPipelines" in params, "Missing parameter 'nbPipelines'"

def test_marte_hwcomputing_hwprocessor_has_ipc():
    assert hasattr(MARTE_HwComputing_HwProcessor, "ipc")
    descriptor = None
    for klass in MARTE_HwComputing_HwProcessor.__mro__:
        if "ipc" in klass.__dict__:
            descriptor = klass.__dict__["ipc"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwprocessor_has_nbStages():
    assert hasattr(MARTE_HwComputing_HwProcessor, "nbStages")
    descriptor = None
    for klass in MARTE_HwComputing_HwProcessor.__mro__:
        if "nbStages" in klass.__dict__:
            descriptor = klass.__dict__["nbStages"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwprocessor_has_nbALUs():
    assert hasattr(MARTE_HwComputing_HwProcessor, "nbALUs")
    descriptor = None
    for klass in MARTE_HwComputing_HwProcessor.__mro__:
        if "nbALUs" in klass.__dict__:
            descriptor = klass.__dict__["nbALUs"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwprocessor_has_mips():
    assert hasattr(MARTE_HwComputing_HwProcessor, "mips")
    descriptor = None
    for klass in MARTE_HwComputing_HwProcessor.__mro__:
        if "mips" in klass.__dict__:
            descriptor = klass.__dict__["mips"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwprocessor_has_nbCores():
    assert hasattr(MARTE_HwComputing_HwProcessor, "nbCores")
    descriptor = None
    for klass in MARTE_HwComputing_HwProcessor.__mro__:
        if "nbCores" in klass.__dict__:
            descriptor = klass.__dict__["nbCores"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwprocessor_has_architecture():
    assert hasattr(MARTE_HwComputing_HwProcessor, "architecture")
    descriptor = None
    for klass in MARTE_HwComputing_HwProcessor.__mro__:
        if "architecture" in klass.__dict__:
            descriptor = klass.__dict__["architecture"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwprocessor_has_nbFPUs():
    assert hasattr(MARTE_HwComputing_HwProcessor, "nbFPUs")
    descriptor = None
    for klass in MARTE_HwComputing_HwProcessor.__mro__:
        if "nbFPUs" in klass.__dict__:
            descriptor = klass.__dict__["nbFPUs"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwcomputing_hwprocessor_has_nbPipelines():
    assert hasattr(MARTE_HwComputing_HwProcessor, "nbPipelines")
    descriptor = None
    for klass in MARTE_HwComputing_HwProcessor.__mro__:
        if "nbPipelines" in klass.__dict__:
            descriptor = klass.__dict__["nbPipelines"]
            break
    assert isinstance(descriptor, property)



def test_hwstoragemanager_hwmmu_is_not_abstract():
    assert not inspect.isabstract(HwStorageManager_HwMMU)


def test_hwstoragemanager_hwmmu_constructor_exists():
    assert callable(HwStorageManager_HwMMU.__init__)


def test_hwstoragemanager_hwmmu_constructor_args():
    sig = inspect.signature(HwStorageManager_HwMMU.__init__)
    params = list(sig.parameters.keys())



def test_marte_hlam_rtservice_is_not_abstract():
    assert not inspect.isabstract(MARTE_HLAM_RtService)


def test_marte_hlam_rtservice_constructor_exists():
    assert callable(MARTE_HLAM_RtService.__init__)


def test_marte_hlam_rtservice_constructor_args():
    sig = inspect.signature(MARTE_HLAM_RtService.__init__)
    params = list(sig.parameters.keys())
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"
    assert "concPolicy" in params, "Missing parameter 'concPolicy'"
    assert "synchKind" in params, "Missing parameter 'synchKind'"
    assert "exeKind" in params, "Missing parameter 'exeKind'"

def test_marte_hlam_rtservice_has_isAtomic():
    assert hasattr(MARTE_HLAM_RtService, "isAtomic")
    descriptor = None
    for klass in MARTE_HLAM_RtService.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtservice_has_concPolicy():
    assert hasattr(MARTE_HLAM_RtService, "concPolicy")
    descriptor = None
    for klass in MARTE_HLAM_RtService.__mro__:
        if "concPolicy" in klass.__dict__:
            descriptor = klass.__dict__["concPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtservice_has_synchKind():
    assert hasattr(MARTE_HLAM_RtService, "synchKind")
    descriptor = None
    for klass in MARTE_HLAM_RtService.__mro__:
        if "synchKind" in klass.__dict__:
            descriptor = klass.__dict__["synchKind"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtservice_has_exeKind():
    assert hasattr(MARTE_HLAM_RtService, "exeKind")
    descriptor = None
    for klass in MARTE_HLAM_RtService.__mro__:
        if "exeKind" in klass.__dict__:
            descriptor = klass.__dict__["exeKind"]
            break
    assert isinstance(descriptor, property)



def test_marte_hlam_rtaction_is_not_abstract():
    assert not inspect.isabstract(MARTE_HLAM_RtAction)


def test_marte_hlam_rtaction_constructor_exists():
    assert callable(MARTE_HLAM_RtAction.__init__)


def test_marte_hlam_rtaction_constructor_args():
    sig = inspect.signature(MARTE_HLAM_RtAction.__init__)
    params = list(sig.parameters.keys())
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"
    assert "msgSize" in params, "Missing parameter 'msgSize'"
    assert "synchKind" in params, "Missing parameter 'synchKind'"

def test_marte_hlam_rtaction_has_isAtomic():
    assert hasattr(MARTE_HLAM_RtAction, "isAtomic")
    descriptor = None
    for klass in MARTE_HLAM_RtAction.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtaction_has_msgSize():
    assert hasattr(MARTE_HLAM_RtAction, "msgSize")
    descriptor = None
    for klass in MARTE_HLAM_RtAction.__mro__:
        if "msgSize" in klass.__dict__:
            descriptor = klass.__dict__["msgSize"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtaction_has_synchKind():
    assert hasattr(MARTE_HLAM_RtAction, "synchKind")
    descriptor = None
    for klass in MARTE_HLAM_RtAction.__mro__:
        if "synchKind" in klass.__dict__:
            descriptor = klass.__dict__["synchKind"]
            break
    assert isinstance(descriptor, property)



def test_hlam_marte_comment_is_not_abstract():
    assert not inspect.isabstract(HLAM_MARTE_Comment)


def test_hlam_marte_comment_constructor_exists():
    assert callable(HLAM_MARTE_Comment.__init__)


def test_hlam_marte_comment_constructor_args():
    sig = inspect.signature(HLAM_MARTE_Comment.__init__)
    params = list(sig.parameters.keys())



def test_time_timedinstantobservation_is_not_abstract():
    assert not inspect.isabstract(Time_TimedInstantObservation)


def test_time_timedinstantobservation_constructor_exists():
    assert callable(Time_TimedInstantObservation.__init__)


def test_time_timedinstantobservation_constructor_args():
    sig = inspect.signature(Time_TimedInstantObservation.__init__)
    params = list(sig.parameters.keys())



def test_marte_hlam_rtspecification_is_not_abstract():
    assert not inspect.isabstract(MARTE_HLAM_RtSpecification)


def test_marte_hlam_rtspecification_constructor_exists():
    assert callable(MARTE_HLAM_RtSpecification.__init__)


def test_marte_hlam_rtspecification_constructor_args():
    sig = inspect.signature(MARTE_HLAM_RtSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "absDl" in params, "Missing parameter 'absDl'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "miss" in params, "Missing parameter 'miss'"
    assert "relDl" in params, "Missing parameter 'relDl'"
    assert "occKind" in params, "Missing parameter 'occKind'"
    assert "utility" in params, "Missing parameter 'utility'"
    assert "rdTime" in params, "Missing parameter 'rdTime'"
    assert "boundDl" in params, "Missing parameter 'boundDl'"

def test_marte_hlam_rtspecification_has_absDl():
    assert hasattr(MARTE_HLAM_RtSpecification, "absDl")
    descriptor = None
    for klass in MARTE_HLAM_RtSpecification.__mro__:
        if "absDl" in klass.__dict__:
            descriptor = klass.__dict__["absDl"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtspecification_has_priority():
    assert hasattr(MARTE_HLAM_RtSpecification, "priority")
    descriptor = None
    for klass in MARTE_HLAM_RtSpecification.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtspecification_has_miss():
    assert hasattr(MARTE_HLAM_RtSpecification, "miss")
    descriptor = None
    for klass in MARTE_HLAM_RtSpecification.__mro__:
        if "miss" in klass.__dict__:
            descriptor = klass.__dict__["miss"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtspecification_has_relDl():
    assert hasattr(MARTE_HLAM_RtSpecification, "relDl")
    descriptor = None
    for klass in MARTE_HLAM_RtSpecification.__mro__:
        if "relDl" in klass.__dict__:
            descriptor = klass.__dict__["relDl"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtspecification_has_occKind():
    assert hasattr(MARTE_HLAM_RtSpecification, "occKind")
    descriptor = None
    for klass in MARTE_HLAM_RtSpecification.__mro__:
        if "occKind" in klass.__dict__:
            descriptor = klass.__dict__["occKind"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtspecification_has_utility():
    assert hasattr(MARTE_HLAM_RtSpecification, "utility")
    descriptor = None
    for klass in MARTE_HLAM_RtSpecification.__mro__:
        if "utility" in klass.__dict__:
            descriptor = klass.__dict__["utility"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtspecification_has_rdTime():
    assert hasattr(MARTE_HLAM_RtSpecification, "rdTime")
    descriptor = None
    for klass in MARTE_HLAM_RtSpecification.__mro__:
        if "rdTime" in klass.__dict__:
            descriptor = klass.__dict__["rdTime"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtspecification_has_boundDl():
    assert hasattr(MARTE_HLAM_RtSpecification, "boundDl")
    descriptor = None
    for klass in MARTE_HLAM_RtSpecification.__mro__:
        if "boundDl" in klass.__dict__:
            descriptor = klass.__dict__["boundDl"]
            break
    assert isinstance(descriptor, property)



def test_hlam_rtspecification_is_not_abstract():
    assert not inspect.isabstract(HLAM_RtSpecification)


def test_hlam_rtspecification_constructor_exists():
    assert callable(HLAM_RtSpecification.__init__)


def test_hlam_rtspecification_constructor_args():
    sig = inspect.signature(HLAM_RtSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hlam_marte_invocationaction_is_not_abstract():
    assert not inspect.isabstract(HLAM_MARTE_InvocationAction)


def test_hlam_marte_invocationaction_constructor_exists():
    assert callable(HLAM_MARTE_InvocationAction.__init__)


def test_hlam_marte_invocationaction_constructor_args():
    sig = inspect.signature(HLAM_MARTE_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_hlam_marte_port_is_not_abstract():
    assert not inspect.isabstract(HLAM_MARTE_Port)


def test_hlam_marte_port_constructor_exists():
    assert callable(HLAM_MARTE_Port.__init__)


def test_hlam_marte_port_constructor_args():
    sig = inspect.signature(HLAM_MARTE_Port.__init__)
    params = list(sig.parameters.keys())



def test_hlam_marte_signal_is_not_abstract():
    assert not inspect.isabstract(HLAM_MARTE_Signal)


def test_hlam_marte_signal_constructor_exists():
    assert callable(HLAM_MARTE_Signal.__init__)


def test_hlam_marte_signal_constructor_args():
    sig = inspect.signature(HLAM_MARTE_Signal.__init__)
    params = list(sig.parameters.keys())



def test_hlam_marte_message_is_not_abstract():
    assert not inspect.isabstract(HLAM_MARTE_Message)


def test_hlam_marte_message_constructor_exists():
    assert callable(HLAM_MARTE_Message.__init__)


def test_hlam_marte_message_constructor_args():
    sig = inspect.signature(HLAM_MARTE_Message.__init__)
    params = list(sig.parameters.keys())



def test_hlam_marte_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(HLAM_MARTE_BehavioralFeature)


def test_hlam_marte_behavioralfeature_constructor_exists():
    assert callable(HLAM_MARTE_BehavioralFeature.__init__)


def test_hlam_marte_behavioralfeature_constructor_args():
    sig = inspect.signature(HLAM_MARTE_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_marte_hlam_rtfeature_is_not_abstract():
    assert not inspect.isabstract(MARTE_HLAM_RtFeature)


def test_marte_hlam_rtfeature_constructor_exists():
    assert callable(MARTE_HLAM_RtFeature.__init__)


def test_marte_hlam_rtfeature_constructor_args():
    sig = inspect.signature(MARTE_HLAM_RtFeature.__init__)
    params = list(sig.parameters.keys())



def test_marte_hlam_ppunit_is_not_abstract():
    assert not inspect.isabstract(MARTE_HLAM_PpUnit)


def test_marte_hlam_ppunit_constructor_exists():
    assert callable(MARTE_HLAM_PpUnit.__init__)


def test_marte_hlam_ppunit_constructor_args():
    sig = inspect.signature(MARTE_HLAM_PpUnit.__init__)
    params = list(sig.parameters.keys())
    assert "concPolicy" in params, "Missing parameter 'concPolicy'"
    assert "memorySize" in params, "Missing parameter 'memorySize'"

def test_marte_hlam_ppunit_has_concPolicy():
    assert hasattr(MARTE_HLAM_PpUnit, "concPolicy")
    descriptor = None
    for klass in MARTE_HLAM_PpUnit.__mro__:
        if "concPolicy" in klass.__dict__:
            descriptor = klass.__dict__["concPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_ppunit_has_memorySize():
    assert hasattr(MARTE_HLAM_PpUnit, "memorySize")
    descriptor = None
    for klass in MARTE_HLAM_PpUnit.__mro__:
        if "memorySize" in klass.__dict__:
            descriptor = klass.__dict__["memorySize"]
            break
    assert isinstance(descriptor, property)



def test_hlam_marte_operation_is_not_abstract():
    assert not inspect.isabstract(HLAM_MARTE_Operation)


def test_hlam_marte_operation_constructor_exists():
    assert callable(HLAM_MARTE_Operation.__init__)


def test_hlam_marte_operation_constructor_args():
    sig = inspect.signature(HLAM_MARTE_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hlam_marte_behavior_is_not_abstract():
    assert not inspect.isabstract(HLAM_MARTE_Behavior)


def test_hlam_marte_behavior_constructor_exists():
    assert callable(HLAM_MARTE_Behavior.__init__)


def test_hlam_marte_behavior_constructor_args():
    sig = inspect.signature(HLAM_MARTE_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_marte_hlam_rtunit_is_not_abstract():
    assert not inspect.isabstract(MARTE_HLAM_RtUnit)


def test_marte_hlam_rtunit_constructor_exists():
    assert callable(MARTE_HLAM_RtUnit.__init__)


def test_marte_hlam_rtunit_constructor_args():
    sig = inspect.signature(MARTE_HLAM_RtUnit.__init__)
    params = list(sig.parameters.keys())
    assert "queueSize" in params, "Missing parameter 'queueSize'"
    assert "srPoolWaitingTime" in params, "Missing parameter 'srPoolWaitingTime'"
    assert "srPoolSize" in params, "Missing parameter 'srPoolSize'"
    assert "srPoolPolicy" in params, "Missing parameter 'srPoolPolicy'"
    assert "isMain" in params, "Missing parameter 'isMain'"
    assert "msgMaxSize" in params, "Missing parameter 'msgMaxSize'"
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"
    assert "memorySize" in params, "Missing parameter 'memorySize'"
    assert "queueSchedPolicy" in params, "Missing parameter 'queueSchedPolicy'"

def test_marte_hlam_rtunit_has_queueSize():
    assert hasattr(MARTE_HLAM_RtUnit, "queueSize")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "queueSize" in klass.__dict__:
            descriptor = klass.__dict__["queueSize"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtunit_has_srPoolWaitingTime():
    assert hasattr(MARTE_HLAM_RtUnit, "srPoolWaitingTime")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "srPoolWaitingTime" in klass.__dict__:
            descriptor = klass.__dict__["srPoolWaitingTime"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtunit_has_srPoolSize():
    assert hasattr(MARTE_HLAM_RtUnit, "srPoolSize")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "srPoolSize" in klass.__dict__:
            descriptor = klass.__dict__["srPoolSize"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtunit_has_srPoolPolicy():
    assert hasattr(MARTE_HLAM_RtUnit, "srPoolPolicy")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "srPoolPolicy" in klass.__dict__:
            descriptor = klass.__dict__["srPoolPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtunit_has_isMain():
    assert hasattr(MARTE_HLAM_RtUnit, "isMain")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "isMain" in klass.__dict__:
            descriptor = klass.__dict__["isMain"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtunit_has_msgMaxSize():
    assert hasattr(MARTE_HLAM_RtUnit, "msgMaxSize")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "msgMaxSize" in klass.__dict__:
            descriptor = klass.__dict__["msgMaxSize"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtunit_has_isDynamic():
    assert hasattr(MARTE_HLAM_RtUnit, "isDynamic")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "isDynamic" in klass.__dict__:
            descriptor = klass.__dict__["isDynamic"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtunit_has_memorySize():
    assert hasattr(MARTE_HLAM_RtUnit, "memorySize")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "memorySize" in klass.__dict__:
            descriptor = klass.__dict__["memorySize"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtunit_has_queueSchedPolicy():
    assert hasattr(MARTE_HLAM_RtUnit, "queueSchedPolicy")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "queueSchedPolicy" in klass.__dict__:
            descriptor = klass.__dict__["queueSchedPolicy"]
            break
    assert isinstance(descriptor, property)



def test_marte_datatypes_tupletype_is_not_abstract():
    assert not inspect.isabstract(MARTE_DataTypes_TupleType)


def test_marte_datatypes_tupletype_constructor_exists():
    assert callable(MARTE_DataTypes_TupleType.__init__)


def test_marte_datatypes_tupletype_constructor_args():
    sig = inspect.signature(MARTE_DataTypes_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_marte_datatypes_choicetype_is_not_abstract():
    assert not inspect.isabstract(MARTE_DataTypes_ChoiceType)


def test_marte_datatypes_choicetype_constructor_exists():
    assert callable(MARTE_DataTypes_ChoiceType.__init__)


def test_marte_datatypes_choicetype_constructor_args():
    sig = inspect.signature(MARTE_DataTypes_ChoiceType.__init__)
    params = list(sig.parameters.keys())



def test_marte_datatypes_collectiontype_is_not_abstract():
    assert not inspect.isabstract(MARTE_DataTypes_CollectionType)


def test_marte_datatypes_collectiontype_constructor_exists():
    assert callable(MARTE_DataTypes_CollectionType.__init__)


def test_marte_datatypes_collectiontype_constructor_args():
    sig = inspect.signature(MARTE_DataTypes_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_hlam_marte_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(HLAM_MARTE_BehavioredClassifier)


def test_hlam_marte_behavioredclassifier_constructor_exists():
    assert callable(HLAM_MARTE_BehavioredClassifier.__init__)


def test_hlam_marte_behavioredclassifier_constructor_args():
    sig = inspect.signature(HLAM_MARTE_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_marte_datatypes_intervaltype_is_not_abstract():
    assert not inspect.isabstract(MARTE_DataTypes_IntervalType)


def test_marte_datatypes_intervaltype_constructor_exists():
    assert callable(MARTE_DataTypes_IntervalType.__init__)


def test_marte_datatypes_intervaltype_constructor_args():
    sig = inspect.signature(MARTE_DataTypes_IntervalType.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_marte_datatype_is_not_abstract():
    assert not inspect.isabstract(DataTypes_MARTE_DataType)


def test_datatypes_marte_datatype_constructor_exists():
    assert callable(DataTypes_MARTE_DataType.__init__)


def test_datatypes_marte_datatype_constructor_args():
    sig = inspect.signature(DataTypes_MARTE_DataType.__init__)
    params = list(sig.parameters.keys())



def test_marte_datatypes_boundedsubtype_is_not_abstract():
    assert not inspect.isabstract(MARTE_DataTypes_BoundedSubtype)


def test_marte_datatypes_boundedsubtype_constructor_exists():
    assert callable(MARTE_DataTypes_BoundedSubtype.__init__)


def test_marte_datatypes_boundedsubtype_constructor_args():
    sig = inspect.signature(MARTE_DataTypes_BoundedSubtype.__init__)
    params = list(sig.parameters.keys())
    assert "isMaxOpen" in params, "Missing parameter 'isMaxOpen'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "minValue" in params, "Missing parameter 'minValue'"
    assert "isMinOpen" in params, "Missing parameter 'isMinOpen'"

def test_marte_datatypes_boundedsubtype_has_isMaxOpen():
    assert hasattr(MARTE_DataTypes_BoundedSubtype, "isMaxOpen")
    descriptor = None
    for klass in MARTE_DataTypes_BoundedSubtype.__mro__:
        if "isMaxOpen" in klass.__dict__:
            descriptor = klass.__dict__["isMaxOpen"]
            break
    assert isinstance(descriptor, property)

def test_marte_datatypes_boundedsubtype_has_maxValue():
    assert hasattr(MARTE_DataTypes_BoundedSubtype, "maxValue")
    descriptor = None
    for klass in MARTE_DataTypes_BoundedSubtype.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_marte_datatypes_boundedsubtype_has_minValue():
    assert hasattr(MARTE_DataTypes_BoundedSubtype, "minValue")
    descriptor = None
    for klass in MARTE_DataTypes_BoundedSubtype.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)

def test_marte_datatypes_boundedsubtype_has_isMinOpen():
    assert hasattr(MARTE_DataTypes_BoundedSubtype, "isMinOpen")
    descriptor = None
    for klass in MARTE_DataTypes_BoundedSubtype.__mro__:
        if "isMinOpen" in klass.__dict__:
            descriptor = klass.__dict__["isMinOpen"]
            break
    assert isinstance(descriptor, property)



def test_operators_marte_behavior_is_not_abstract():
    assert not inspect.isabstract(Operators_MARTE_Behavior)


def test_operators_marte_behavior_constructor_exists():
    assert callable(Operators_MARTE_Behavior.__init__)


def test_operators_marte_behavior_constructor_args():
    sig = inspect.signature(Operators_MARTE_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_marte_operators_operator_is_not_abstract():
    assert not inspect.isabstract(MARTE_Operators_Operator)


def test_marte_operators_operator_constructor_exists():
    assert callable(MARTE_Operators_Operator.__init__)


def test_marte_operators_operator_constructor_args():
    sig = inspect.signature(MARTE_Operators_Operator.__init__)
    params = list(sig.parameters.keys())
    assert "arity" in params, "Missing parameter 'arity'"
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_marte_operators_operator_has_arity():
    assert hasattr(MARTE_Operators_Operator, "arity")
    descriptor = None
    for klass in MARTE_Operators_Operator.__mro__:
        if "arity" in klass.__dict__:
            descriptor = klass.__dict__["arity"]
            break
    assert isinstance(descriptor, property)

def test_marte_operators_operator_has_symbol():
    assert hasattr(MARTE_Operators_Operator, "symbol")
    descriptor = None
    for klass in MARTE_Operators_Operator.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_variables_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(Variables_MARTE_NamedElement)


def test_variables_marte_namedelement_constructor_exists():
    assert callable(Variables_MARTE_NamedElement.__init__)


def test_variables_marte_namedelement_constructor_args():
    sig = inspect.signature(Variables_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte_variables_expressioncontext_is_not_abstract():
    assert not inspect.isabstract(MARTE_Variables_ExpressionContext)


def test_marte_variables_expressioncontext_constructor_exists():
    assert callable(MARTE_Variables_ExpressionContext.__init__)


def test_marte_variables_expressioncontext_constructor_args():
    sig = inspect.signature(MARTE_Variables_ExpressionContext.__init__)
    params = list(sig.parameters.keys())



def test_variables_marte_property_is_not_abstract():
    assert not inspect.isabstract(Variables_MARTE_Property)


def test_variables_marte_property_constructor_exists():
    assert callable(Variables_MARTE_Property.__init__)


def test_variables_marte_property_constructor_args():
    sig = inspect.signature(Variables_MARTE_Property.__init__)
    params = list(sig.parameters.keys())



def test_marte_variables_var_is_not_abstract():
    assert not inspect.isabstract(MARTE_Variables_Var)


def test_marte_variables_var_constructor_exists():
    assert callable(MARTE_Variables_Var.__init__)


def test_marte_variables_var_constructor_args():
    sig = inspect.signature(MARTE_Variables_Var.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_marte_variables_var_has_dir():
    assert hasattr(MARTE_Variables_Var, "dir")
    descriptor = None
    for klass in MARTE_Variables_Var.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_rsm_marte_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(RSM_MARTE_MultiplicityElement)


def test_rsm_marte_multiplicityelement_constructor_exists():
    assert callable(RSM_MARTE_MultiplicityElement.__init__)


def test_rsm_marte_multiplicityelement_constructor_args():
    sig = inspect.signature(RSM_MARTE_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_marte_rsm_shaped_is_not_abstract():
    assert not inspect.isabstract(MARTE_RSM_Shaped)


def test_marte_rsm_shaped_constructor_exists():
    assert callable(MARTE_RSM_Shaped.__init__)


def test_marte_rsm_shaped_constructor_args():
    sig = inspect.signature(MARTE_RSM_Shaped.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_marte_rsm_shaped_has_shape():
    assert hasattr(MARTE_RSM_Shaped, "shape")
    descriptor = None
    for klass in MARTE_RSM_Shaped.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_datatypes_marte_property_is_not_abstract():
    assert not inspect.isabstract(DataTypes_MARTE_Property)


def test_datatypes_marte_property_constructor_exists():
    assert callable(DataTypes_MARTE_Property.__init__)


def test_datatypes_marte_property_constructor_args():
    sig = inspect.signature(DataTypes_MARTE_Property.__init__)
    params = list(sig.parameters.keys())



def test_allocate_is_not_abstract():
    assert not inspect.isabstract(Allocate)


def test_allocate_constructor_exists():
    assert callable(Allocate.__init__)


def test_allocate_constructor_args():
    sig = inspect.signature(Allocate.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_concurrency_entrypoint_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Concurrency_EntryPoint)


def test_marte_sw_concurrency_entrypoint_constructor_exists():
    assert callable(MARTE_SW_Concurrency_EntryPoint.__init__)


def test_marte_sw_concurrency_entrypoint_constructor_args():
    sig = inspect.signature(MARTE_SW_Concurrency_EntryPoint.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"

def test_marte_sw_concurrency_entrypoint_has_isReentrant():
    assert hasattr(MARTE_SW_Concurrency_EntryPoint, "isReentrant")
    descriptor = None
    for klass in MARTE_SW_Concurrency_EntryPoint.__mro__:
        if "isReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isReentrant"]
            break
    assert isinstance(descriptor, property)



def test_marte_rsm_distribute_is_not_abstract():
    assert not inspect.isabstract(MARTE_RSM_Distribute)


def test_marte_rsm_distribute_constructor_exists():
    assert callable(MARTE_RSM_Distribute.__init__)


def test_marte_rsm_distribute_constructor_args():
    sig = inspect.signature(MARTE_RSM_Distribute.__init__)
    params = list(sig.parameters.keys())
    assert "toTiler" in params, "Missing parameter 'toTiler'"
    assert "repetitionSpace" in params, "Missing parameter 'repetitionSpace'"
    assert "patternShape" in params, "Missing parameter 'patternShape'"
    assert "fromTiler" in params, "Missing parameter 'fromTiler'"

def test_marte_rsm_distribute_has_toTiler():
    assert hasattr(MARTE_RSM_Distribute, "toTiler")
    descriptor = None
    for klass in MARTE_RSM_Distribute.__mro__:
        if "toTiler" in klass.__dict__:
            descriptor = klass.__dict__["toTiler"]
            break
    assert isinstance(descriptor, property)

def test_marte_rsm_distribute_has_repetitionSpace():
    assert hasattr(MARTE_RSM_Distribute, "repetitionSpace")
    descriptor = None
    for klass in MARTE_RSM_Distribute.__mro__:
        if "repetitionSpace" in klass.__dict__:
            descriptor = klass.__dict__["repetitionSpace"]
            break
    assert isinstance(descriptor, property)

def test_marte_rsm_distribute_has_patternShape():
    assert hasattr(MARTE_RSM_Distribute, "patternShape")
    descriptor = None
    for klass in MARTE_RSM_Distribute.__mro__:
        if "patternShape" in klass.__dict__:
            descriptor = klass.__dict__["patternShape"]
            break
    assert isinstance(descriptor, property)

def test_marte_rsm_distribute_has_fromTiler():
    assert hasattr(MARTE_RSM_Distribute, "fromTiler")
    descriptor = None
    for klass in MARTE_RSM_Distribute.__mro__:
        if "fromTiler" in klass.__dict__:
            descriptor = klass.__dict__["fromTiler"]
            break
    assert isinstance(descriptor, property)



def test_linktopology_is_not_abstract():
    assert not inspect.isabstract(LinkTopology)


def test_linktopology_constructor_exists():
    assert callable(LinkTopology.__init__)


def test_linktopology_constructor_args():
    sig = inspect.signature(LinkTopology.__init__)
    params = list(sig.parameters.keys())



def test_marte_rsm_tiler_is_not_abstract():
    assert not inspect.isabstract(MARTE_RSM_Tiler)


def test_marte_rsm_tiler_constructor_exists():
    assert callable(MARTE_RSM_Tiler.__init__)


def test_marte_rsm_tiler_constructor_args():
    sig = inspect.signature(MARTE_RSM_Tiler.__init__)
    params = list(sig.parameters.keys())
    assert "origin" in params, "Missing parameter 'origin'"
    assert "fitting" in params, "Missing parameter 'fitting'"
    assert "tiler" in params, "Missing parameter 'tiler'"
    assert "paving" in params, "Missing parameter 'paving'"

def test_marte_rsm_tiler_has_origin():
    assert hasattr(MARTE_RSM_Tiler, "origin")
    descriptor = None
    for klass in MARTE_RSM_Tiler.__mro__:
        if "origin" in klass.__dict__:
            descriptor = klass.__dict__["origin"]
            break
    assert isinstance(descriptor, property)

def test_marte_rsm_tiler_has_fitting():
    assert hasattr(MARTE_RSM_Tiler, "fitting")
    descriptor = None
    for klass in MARTE_RSM_Tiler.__mro__:
        if "fitting" in klass.__dict__:
            descriptor = klass.__dict__["fitting"]
            break
    assert isinstance(descriptor, property)

def test_marte_rsm_tiler_has_tiler():
    assert hasattr(MARTE_RSM_Tiler, "tiler")
    descriptor = None
    for klass in MARTE_RSM_Tiler.__mro__:
        if "tiler" in klass.__dict__:
            descriptor = klass.__dict__["tiler"]
            break
    assert isinstance(descriptor, property)

def test_marte_rsm_tiler_has_paving():
    assert hasattr(MARTE_RSM_Tiler, "paving")
    descriptor = None
    for klass in MARTE_RSM_Tiler.__mro__:
        if "paving" in klass.__dict__:
            descriptor = klass.__dict__["paving"]
            break
    assert isinstance(descriptor, property)



def test_marte_rsm_interrepetition_is_not_abstract():
    assert not inspect.isabstract(MARTE_RSM_InterRepetition)


def test_marte_rsm_interrepetition_constructor_exists():
    assert callable(MARTE_RSM_InterRepetition.__init__)


def test_marte_rsm_interrepetition_constructor_args():
    sig = inspect.signature(MARTE_RSM_InterRepetition.__init__)
    params = list(sig.parameters.keys())
    assert "isModulo" in params, "Missing parameter 'isModulo'"
    assert "repetitionShapeDependence" in params, "Missing parameter 'repetitionShapeDependence'"

def test_marte_rsm_interrepetition_has_isModulo():
    assert hasattr(MARTE_RSM_InterRepetition, "isModulo")
    descriptor = None
    for klass in MARTE_RSM_InterRepetition.__mro__:
        if "isModulo" in klass.__dict__:
            descriptor = klass.__dict__["isModulo"]
            break
    assert isinstance(descriptor, property)

def test_marte_rsm_interrepetition_has_repetitionShapeDependence():
    assert hasattr(MARTE_RSM_InterRepetition, "repetitionShapeDependence")
    descriptor = None
    for klass in MARTE_RSM_InterRepetition.__mro__:
        if "repetitionShapeDependence" in klass.__dict__:
            descriptor = klass.__dict__["repetitionShapeDependence"]
            break
    assert isinstance(descriptor, property)



def test_marte_rsm_reshape_is_not_abstract():
    assert not inspect.isabstract(MARTE_RSM_Reshape)


def test_marte_rsm_reshape_constructor_exists():
    assert callable(MARTE_RSM_Reshape.__init__)


def test_marte_rsm_reshape_constructor_args():
    sig = inspect.signature(MARTE_RSM_Reshape.__init__)
    params = list(sig.parameters.keys())
    assert "patternShape" in params, "Missing parameter 'patternShape'"
    assert "repetitonShape" in params, "Missing parameter 'repetitonShape'"

def test_marte_rsm_reshape_has_patternShape():
    assert hasattr(MARTE_RSM_Reshape, "patternShape")
    descriptor = None
    for klass in MARTE_RSM_Reshape.__mro__:
        if "patternShape" in klass.__dict__:
            descriptor = klass.__dict__["patternShape"]
            break
    assert isinstance(descriptor, property)

def test_marte_rsm_reshape_has_repetitonShape():
    assert hasattr(MARTE_RSM_Reshape, "repetitonShape")
    descriptor = None
    for klass in MARTE_RSM_Reshape.__mro__:
        if "repetitonShape" in klass.__dict__:
            descriptor = klass.__dict__["repetitonShape"]
            break
    assert isinstance(descriptor, property)



def test_marte_rsm_defaultlink_is_not_abstract():
    assert not inspect.isabstract(MARTE_RSM_DefaultLink)


def test_marte_rsm_defaultlink_constructor_exists():
    assert callable(MARTE_RSM_DefaultLink.__init__)


def test_marte_rsm_defaultlink_constructor_args():
    sig = inspect.signature(MARTE_RSM_DefaultLink.__init__)
    params = list(sig.parameters.keys())



def test_rsm_marte_connector_is_not_abstract():
    assert not inspect.isabstract(RSM_MARTE_Connector)


def test_rsm_marte_connector_constructor_exists():
    assert callable(RSM_MARTE_Connector.__init__)


def test_rsm_marte_connector_constructor_args():
    sig = inspect.signature(RSM_MARTE_Connector.__init__)
    params = list(sig.parameters.keys())



def test_marte_rsm_linktopology_is_not_abstract():
    assert not inspect.isabstract(MARTE_RSM_LinkTopology)


def test_marte_rsm_linktopology_constructor_exists():
    assert callable(MARTE_RSM_LinkTopology.__init__)


def test_marte_rsm_linktopology_constructor_args():
    sig = inspect.signature(MARTE_RSM_LinkTopology.__init__)
    params = list(sig.parameters.keys())



def test_grm_resourceusage_is_not_abstract():
    assert not inspect.isabstract(GRM_ResourceUsage)


def test_grm_resourceusage_constructor_exists():
    assert callable(GRM_ResourceUsage.__init__)


def test_grm_resourceusage_constructor_args():
    sig = inspect.signature(GRM_ResourceUsage.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gascenario_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaScenario)


def test_marte_gqam_gascenario_constructor_exists():
    assert callable(MARTE_GQAM_GaScenario.__init__)


def test_marte_gqam_gascenario_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaScenario.__init__)
    params = list(sig.parameters.keys())
    assert "utilizationOnHost" in params, "Missing parameter 'utilizationOnHost'"
    assert "hostDemand" in params, "Missing parameter 'hostDemand'"
    assert "utilization" in params, "Missing parameter 'utilization'"
    assert "throughput" in params, "Missing parameter 'throughput'"
    assert "respT" in params, "Missing parameter 'respT'"
    assert "interOccT" in params, "Missing parameter 'interOccT'"
    assert "hostDemandOps" in params, "Missing parameter 'hostDemandOps'"

def test_marte_gqam_gascenario_has_utilizationOnHost():
    assert hasattr(MARTE_GQAM_GaScenario, "utilizationOnHost")
    descriptor = None
    for klass in MARTE_GQAM_GaScenario.__mro__:
        if "utilizationOnHost" in klass.__dict__:
            descriptor = klass.__dict__["utilizationOnHost"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gascenario_has_hostDemand():
    assert hasattr(MARTE_GQAM_GaScenario, "hostDemand")
    descriptor = None
    for klass in MARTE_GQAM_GaScenario.__mro__:
        if "hostDemand" in klass.__dict__:
            descriptor = klass.__dict__["hostDemand"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gascenario_has_utilization():
    assert hasattr(MARTE_GQAM_GaScenario, "utilization")
    descriptor = None
    for klass in MARTE_GQAM_GaScenario.__mro__:
        if "utilization" in klass.__dict__:
            descriptor = klass.__dict__["utilization"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gascenario_has_throughput():
    assert hasattr(MARTE_GQAM_GaScenario, "throughput")
    descriptor = None
    for klass in MARTE_GQAM_GaScenario.__mro__:
        if "throughput" in klass.__dict__:
            descriptor = klass.__dict__["throughput"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gascenario_has_respT():
    assert hasattr(MARTE_GQAM_GaScenario, "respT")
    descriptor = None
    for klass in MARTE_GQAM_GaScenario.__mro__:
        if "respT" in klass.__dict__:
            descriptor = klass.__dict__["respT"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gascenario_has_interOccT():
    assert hasattr(MARTE_GQAM_GaScenario, "interOccT")
    descriptor = None
    for klass in MARTE_GQAM_GaScenario.__mro__:
        if "interOccT" in klass.__dict__:
            descriptor = klass.__dict__["interOccT"]
            break
    assert isinstance(descriptor, property)

def test_marte_gqam_gascenario_has_hostDemandOps():
    assert hasattr(MARTE_GQAM_GaScenario, "hostDemandOps")
    descriptor = None
    for klass in MARTE_GQAM_GaScenario.__mro__:
        if "hostDemandOps" in klass.__dict__:
            descriptor = klass.__dict__["hostDemandOps"]
            break
    assert isinstance(descriptor, property)



def test_grm_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_NamedElement)


def test_grm_marte_namedelement_constructor_exists():
    assert callable(GRM_MARTE_NamedElement.__init__)


def test_grm_marte_namedelement_constructor_args():
    sig = inspect.signature(GRM_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_rsm_marte_connectorend_is_not_abstract():
    assert not inspect.isabstract(RSM_MARTE_ConnectorEnd)


def test_rsm_marte_connectorend_constructor_exists():
    assert callable(RSM_MARTE_ConnectorEnd.__init__)


def test_rsm_marte_connectorend_constructor_args():
    sig = inspect.signature(RSM_MARTE_ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_grservice_is_not_abstract():
    assert not inspect.isabstract(GrService)


def test_grservice_constructor_exists():
    assert callable(GrService.__init__)


def test_grservice_constructor_args():
    sig = inspect.signature(GrService.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwgeneral_hwresourceservice_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwGeneral_HwResourceService)


def test_marte_hwgeneral_hwresourceservice_constructor_exists():
    assert callable(MARTE_HwGeneral_HwResourceService.__init__)


def test_marte_hwgeneral_hwresourceservice_constructor_args():
    sig = inspect.signature(MARTE_HwGeneral_HwResourceService.__init__)
    params = list(sig.parameters.keys())
    assert "consumption" in params, "Missing parameter 'consumption'"
    assert "dissipation" in params, "Missing parameter 'dissipation'"

def test_marte_hwgeneral_hwresourceservice_has_consumption():
    assert hasattr(MARTE_HwGeneral_HwResourceService, "consumption")
    descriptor = None
    for klass in MARTE_HwGeneral_HwResourceService.__mro__:
        if "consumption" in klass.__dict__:
            descriptor = klass.__dict__["consumption"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwgeneral_hwresourceservice_has_dissipation():
    assert hasattr(MARTE_HwGeneral_HwResourceService, "dissipation")
    descriptor = None
    for klass in MARTE_HwGeneral_HwResourceService.__mro__:
        if "dissipation" in klass.__dict__:
            descriptor = klass.__dict__["dissipation"]
            break
    assert isinstance(descriptor, property)



def test_marte_sw_resourcecore_swaccessservice_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_ResourceCore_SwAccessService)


def test_marte_sw_resourcecore_swaccessservice_constructor_exists():
    assert callable(MARTE_SW_ResourceCore_SwAccessService.__init__)


def test_marte_sw_resourcecore_swaccessservice_constructor_args():
    sig = inspect.signature(MARTE_SW_ResourceCore_SwAccessService.__init__)
    params = list(sig.parameters.keys())
    assert "isModifier" in params, "Missing parameter 'isModifier'"

def test_marte_sw_resourcecore_swaccessservice_has_isModifier():
    assert hasattr(MARTE_SW_ResourceCore_SwAccessService, "isModifier")
    descriptor = None
    for klass in MARTE_SW_ResourceCore_SwAccessService.__mro__:
        if "isModifier" in klass.__dict__:
            descriptor = klass.__dict__["isModifier"]
            break
    assert isinstance(descriptor, property)



def test_marte_grm_acquire_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_Acquire)


def test_marte_grm_acquire_constructor_exists():
    assert callable(MARTE_GRM_Acquire.__init__)


def test_marte_grm_acquire_constructor_args():
    sig = inspect.signature(MARTE_GRM_Acquire.__init__)
    params = list(sig.parameters.keys())
    assert "isBlocking" in params, "Missing parameter 'isBlocking'"

def test_marte_grm_acquire_has_isBlocking():
    assert hasattr(MARTE_GRM_Acquire, "isBlocking")
    descriptor = None
    for klass in MARTE_GRM_Acquire.__mro__:
        if "isBlocking" in klass.__dict__:
            descriptor = klass.__dict__["isBlocking"]
            break
    assert isinstance(descriptor, property)



def test_marte_grm_release_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_Release)


def test_marte_grm_release_constructor_exists():
    assert callable(MARTE_GRM_Release.__init__)


def test_marte_grm_release_constructor_args():
    sig = inspect.signature(MARTE_GRM_Release.__init__)
    params = list(sig.parameters.keys())



def test_grm_marte_collaborationuse_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_CollaborationUse)


def test_grm_marte_collaborationuse_constructor_exists():
    assert callable(GRM_MARTE_CollaborationUse.__init__)


def test_grm_marte_collaborationuse_constructor_args():
    sig = inspect.signature(GRM_MARTE_CollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_grm_marte_collaboration_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_Collaboration)


def test_grm_marte_collaboration_constructor_exists():
    assert callable(GRM_MARTE_Collaboration.__init__)


def test_grm_marte_collaboration_constructor_args():
    sig = inspect.signature(GRM_MARTE_Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_grm_marte_behavior_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_Behavior)


def test_grm_marte_behavior_constructor_exists():
    assert callable(GRM_MARTE_Behavior.__init__)


def test_grm_marte_behavior_constructor_args():
    sig = inspect.signature(GRM_MARTE_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_grm_marte_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_BehavioralFeature)


def test_grm_marte_behavioralfeature_constructor_exists():
    assert callable(GRM_MARTE_BehavioralFeature.__init__)


def test_grm_marte_behavioralfeature_constructor_args():
    sig = inspect.signature(GRM_MARTE_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_grm_marte_executionspecification_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_ExecutionSpecification)


def test_grm_marte_executionspecification_constructor_exists():
    assert callable(GRM_MARTE_ExecutionSpecification.__init__)


def test_grm_marte_executionspecification_constructor_args():
    sig = inspect.signature(GRM_MARTE_ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_grm_resource_is_not_abstract():
    assert not inspect.isabstract(GRM_Resource)


def test_grm_resource_constructor_exists():
    assert callable(GRM_Resource.__init__)


def test_grm_resource_constructor_args():
    sig = inspect.signature(GRM_Resource.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_grservice_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_GrService)


def test_marte_grm_grservice_constructor_exists():
    assert callable(MARTE_GRM_GrService.__init__)


def test_marte_grm_grservice_constructor_args():
    sig = inspect.signature(MARTE_GRM_GrService.__init__)
    params = list(sig.parameters.keys())



def test_timingresource_is_not_abstract():
    assert not inspect.isabstract(TimingResource)


def test_timingresource_constructor_exists():
    assert callable(TimingResource.__init__)


def test_timingresource_constructor_args():
    sig = inspect.signature(TimingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_timerresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_TimerResource)


def test_marte_grm_timerresource_constructor_exists():
    assert callable(MARTE_GRM_TimerResource.__init__)


def test_marte_grm_timerresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_TimerResource.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "isPeriodic" in params, "Missing parameter 'isPeriodic'"

def test_marte_grm_timerresource_has_duration():
    assert hasattr(MARTE_GRM_TimerResource, "duration")
    descriptor = None
    for klass in MARTE_GRM_TimerResource.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_timerresource_has_isPeriodic():
    assert hasattr(MARTE_GRM_TimerResource, "isPeriodic")
    descriptor = None
    for klass in MARTE_GRM_TimerResource.__mro__:
        if "isPeriodic" in klass.__dict__:
            descriptor = klass.__dict__["isPeriodic"]
            break
    assert isinstance(descriptor, property)



def test_marte_grm_clockresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_ClockResource)


def test_marte_grm_clockresource_constructor_exists():
    assert callable(MARTE_GRM_ClockResource.__init__)


def test_marte_grm_clockresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_ClockResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_timingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_TimingResource)


def test_marte_grm_timingresource_constructor_exists():
    assert callable(MARTE_GRM_TimingResource.__init__)


def test_marte_grm_timingresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_TimingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_deviceresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_DeviceResource)


def test_marte_grm_deviceresource_constructor_exists():
    assert callable(MARTE_GRM_DeviceResource.__init__)


def test_marte_grm_deviceresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_DeviceResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_resourceusage_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_ResourceUsage)


def test_marte_grm_resourceusage_constructor_exists():
    assert callable(MARTE_GRM_ResourceUsage.__init__)


def test_marte_grm_resourceusage_constructor_args():
    sig = inspect.signature(MARTE_GRM_ResourceUsage.__init__)
    params = list(sig.parameters.keys())
    assert "usedMemory" in params, "Missing parameter 'usedMemory'"
    assert "energy" in params, "Missing parameter 'energy'"
    assert "msgSize" in params, "Missing parameter 'msgSize'"
    assert "execTime" in params, "Missing parameter 'execTime'"
    assert "allocatedMemory" in params, "Missing parameter 'allocatedMemory'"
    assert "powerPeak" in params, "Missing parameter 'powerPeak'"

def test_marte_grm_resourceusage_has_usedMemory():
    assert hasattr(MARTE_GRM_ResourceUsage, "usedMemory")
    descriptor = None
    for klass in MARTE_GRM_ResourceUsage.__mro__:
        if "usedMemory" in klass.__dict__:
            descriptor = klass.__dict__["usedMemory"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_resourceusage_has_energy():
    assert hasattr(MARTE_GRM_ResourceUsage, "energy")
    descriptor = None
    for klass in MARTE_GRM_ResourceUsage.__mro__:
        if "energy" in klass.__dict__:
            descriptor = klass.__dict__["energy"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_resourceusage_has_msgSize():
    assert hasattr(MARTE_GRM_ResourceUsage, "msgSize")
    descriptor = None
    for klass in MARTE_GRM_ResourceUsage.__mro__:
        if "msgSize" in klass.__dict__:
            descriptor = klass.__dict__["msgSize"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_resourceusage_has_execTime():
    assert hasattr(MARTE_GRM_ResourceUsage, "execTime")
    descriptor = None
    for klass in MARTE_GRM_ResourceUsage.__mro__:
        if "execTime" in klass.__dict__:
            descriptor = klass.__dict__["execTime"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_resourceusage_has_allocatedMemory():
    assert hasattr(MARTE_GRM_ResourceUsage, "allocatedMemory")
    descriptor = None
    for klass in MARTE_GRM_ResourceUsage.__mro__:
        if "allocatedMemory" in klass.__dict__:
            descriptor = klass.__dict__["allocatedMemory"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_resourceusage_has_powerPeak():
    assert hasattr(MARTE_GRM_ResourceUsage, "powerPeak")
    descriptor = None
    for klass in MARTE_GRM_ResourceUsage.__mro__:
        if "powerPeak" in klass.__dict__:
            descriptor = klass.__dict__["powerPeak"]
            break
    assert isinstance(descriptor, property)



def test_grm_marte_connector_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_Connector)


def test_grm_marte_connector_constructor_exists():
    assert callable(GRM_MARTE_Connector.__init__)


def test_grm_marte_connector_constructor_args():
    sig = inspect.signature(GRM_MARTE_Connector.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_communicationmedia_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_CommunicationMedia)


def test_marte_grm_communicationmedia_constructor_exists():
    assert callable(MARTE_GRM_CommunicationMedia.__init__)


def test_marte_grm_communicationmedia_constructor_args():
    sig = inspect.signature(MARTE_GRM_CommunicationMedia.__init__)
    params = list(sig.parameters.keys())
    assert "packetT" in params, "Missing parameter 'packetT'"
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "transmMode" in params, "Missing parameter 'transmMode'"
    assert "elementSize" in params, "Missing parameter 'elementSize'"
    assert "blockT" in params, "Missing parameter 'blockT'"

def test_marte_grm_communicationmedia_has_packetT():
    assert hasattr(MARTE_GRM_CommunicationMedia, "packetT")
    descriptor = None
    for klass in MARTE_GRM_CommunicationMedia.__mro__:
        if "packetT" in klass.__dict__:
            descriptor = klass.__dict__["packetT"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_communicationmedia_has_capacity():
    assert hasattr(MARTE_GRM_CommunicationMedia, "capacity")
    descriptor = None
    for klass in MARTE_GRM_CommunicationMedia.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_communicationmedia_has_transmMode():
    assert hasattr(MARTE_GRM_CommunicationMedia, "transmMode")
    descriptor = None
    for klass in MARTE_GRM_CommunicationMedia.__mro__:
        if "transmMode" in klass.__dict__:
            descriptor = klass.__dict__["transmMode"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_communicationmedia_has_elementSize():
    assert hasattr(MARTE_GRM_CommunicationMedia, "elementSize")
    descriptor = None
    for klass in MARTE_GRM_CommunicationMedia.__mro__:
        if "elementSize" in klass.__dict__:
            descriptor = klass.__dict__["elementSize"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_communicationmedia_has_blockT():
    assert hasattr(MARTE_GRM_CommunicationMedia, "blockT")
    descriptor = None
    for klass in MARTE_GRM_CommunicationMedia.__mro__:
        if "blockT" in klass.__dict__:
            descriptor = klass.__dict__["blockT"]
            break
    assert isinstance(descriptor, property)



def test_scheduler_is_not_abstract():
    assert not inspect.isabstract(Scheduler)


def test_scheduler_constructor_exists():
    assert callable(Scheduler.__init__)


def test_scheduler_constructor_args():
    sig = inspect.signature(Scheduler.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_secondaryscheduler_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_SecondaryScheduler)


def test_marte_grm_secondaryscheduler_constructor_exists():
    assert callable(MARTE_GRM_SecondaryScheduler.__init__)


def test_marte_grm_secondaryscheduler_constructor_args():
    sig = inspect.signature(MARTE_GRM_SecondaryScheduler.__init__)
    params = list(sig.parameters.keys())



def test_marte_alloc_allocated_is_not_abstract():
    assert not inspect.isabstract(MARTE_Alloc_Allocated)


def test_marte_alloc_allocated_constructor_exists():
    assert callable(MARTE_Alloc_Allocated.__init__)


def test_marte_alloc_allocated_constructor_args():
    sig = inspect.signature(MARTE_Alloc_Allocated.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte_alloc_allocated_has_kind():
    assert hasattr(MARTE_Alloc_Allocated, "kind")
    descriptor = None
    for klass in MARTE_Alloc_Allocated.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_coreelements_marte_state_is_not_abstract():
    assert not inspect.isabstract(CoreElements_MARTE_State)


def test_coreelements_marte_state_constructor_exists():
    assert callable(CoreElements_MARTE_State.__init__)


def test_coreelements_marte_state_constructor_args():
    sig = inspect.signature(CoreElements_MARTE_State.__init__)
    params = list(sig.parameters.keys())



def test_marte_coreelements_mode_is_not_abstract():
    assert not inspect.isabstract(MARTE_CoreElements_Mode)


def test_marte_coreelements_mode_constructor_exists():
    assert callable(MARTE_CoreElements_Mode.__init__)


def test_marte_coreelements_mode_constructor_args():
    sig = inspect.signature(MARTE_CoreElements_Mode.__init__)
    params = list(sig.parameters.keys())



def test_coreelements_marte_package_is_not_abstract():
    assert not inspect.isabstract(CoreElements_MARTE_Package)


def test_coreelements_marte_package_constructor_exists():
    assert callable(CoreElements_MARTE_Package.__init__)


def test_coreelements_marte_package_constructor_args():
    sig = inspect.signature(CoreElements_MARTE_Package.__init__)
    params = list(sig.parameters.keys())



def test_coreelements_marte_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(CoreElements_MARTE_StructuredClassifier)


def test_coreelements_marte_structuredclassifier_constructor_exists():
    assert callable(CoreElements_MARTE_StructuredClassifier.__init__)


def test_coreelements_marte_structuredclassifier_constructor_args():
    sig = inspect.signature(CoreElements_MARTE_StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_marte_coreelements_configuration_is_not_abstract():
    assert not inspect.isabstract(MARTE_CoreElements_Configuration)


def test_marte_coreelements_configuration_constructor_exists():
    assert callable(MARTE_CoreElements_Configuration.__init__)


def test_marte_coreelements_configuration_constructor_args():
    sig = inspect.signature(MARTE_CoreElements_Configuration.__init__)
    params = list(sig.parameters.keys())



def test_coreelements_marte_statemachine_is_not_abstract():
    assert not inspect.isabstract(CoreElements_MARTE_StateMachine)


def test_coreelements_marte_statemachine_constructor_exists():
    assert callable(CoreElements_MARTE_StateMachine.__init__)


def test_coreelements_marte_statemachine_constructor_args():
    sig = inspect.signature(CoreElements_MARTE_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_marte_coreelements_modebehavior_is_not_abstract():
    assert not inspect.isabstract(MARTE_CoreElements_ModeBehavior)


def test_marte_coreelements_modebehavior_constructor_exists():
    assert callable(MARTE_CoreElements_ModeBehavior.__init__)


def test_marte_coreelements_modebehavior_constructor_args():
    sig = inspect.signature(MARTE_CoreElements_ModeBehavior.__init__)
    params = list(sig.parameters.keys())



def test_coreelements_marte_transition_is_not_abstract():
    assert not inspect.isabstract(CoreElements_MARTE_Transition)


def test_coreelements_marte_transition_constructor_exists():
    assert callable(CoreElements_MARTE_Transition.__init__)


def test_coreelements_marte_transition_constructor_args():
    sig = inspect.signature(CoreElements_MARTE_Transition.__init__)
    params = list(sig.parameters.keys())



def test_marte_coreelements_modetransition_is_not_abstract():
    assert not inspect.isabstract(MARTE_CoreElements_ModeTransition)


def test_marte_coreelements_modetransition_constructor_exists():
    assert callable(MARTE_CoreElements_ModeTransition.__init__)


def test_marte_coreelements_modetransition_constructor_args():
    sig = inspect.signature(MARTE_CoreElements_ModeTransition.__init__)
    params = list(sig.parameters.keys())



def test_nfps_marte_enumeration_is_not_abstract():
    assert not inspect.isabstract(NFPs_MARTE_Enumeration)


def test_nfps_marte_enumeration_constructor_exists():
    assert callable(NFPs_MARTE_Enumeration.__init__)


def test_nfps_marte_enumeration_constructor_args():
    sig = inspect.signature(NFPs_MARTE_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_nfps_dimension_is_not_abstract():
    assert not inspect.isabstract(NFPs_Dimension)


def test_nfps_dimension_constructor_exists():
    assert callable(NFPs_Dimension.__init__)


def test_nfps_dimension_constructor_args():
    sig = inspect.signature(NFPs_Dimension.__init__)
    params = list(sig.parameters.keys())



def test_marte_nfps_dimension_is_not_abstract():
    assert not inspect.isabstract(MARTE_NFPs_Dimension)


def test_marte_nfps_dimension_constructor_exists():
    assert callable(MARTE_NFPs_Dimension.__init__)


def test_marte_nfps_dimension_constructor_args():
    sig = inspect.signature(MARTE_NFPs_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "baseExponent" in params, "Missing parameter 'baseExponent'"
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_marte_nfps_dimension_has_baseExponent():
    assert hasattr(MARTE_NFPs_Dimension, "baseExponent")
    descriptor = None
    for klass in MARTE_NFPs_Dimension.__mro__:
        if "baseExponent" in klass.__dict__:
            descriptor = klass.__dict__["baseExponent"]
            break
    assert isinstance(descriptor, property)

def test_marte_nfps_dimension_has_symbol():
    assert hasattr(MARTE_NFPs_Dimension, "symbol")
    descriptor = None
    for klass in MARTE_NFPs_Dimension.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_nfps_marte_constraint_is_not_abstract():
    assert not inspect.isabstract(NFPs_MARTE_Constraint)


def test_nfps_marte_constraint_constructor_exists():
    assert callable(NFPs_MARTE_Constraint.__init__)


def test_nfps_marte_constraint_constructor_args():
    sig = inspect.signature(NFPs_MARTE_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_marte_nfps_nfpconstraint_is_not_abstract():
    assert not inspect.isabstract(MARTE_NFPs_NfpConstraint)


def test_marte_nfps_nfpconstraint_constructor_exists():
    assert callable(MARTE_NFPs_NfpConstraint.__init__)


def test_marte_nfps_nfpconstraint_constructor_args():
    sig = inspect.signature(MARTE_NFPs_NfpConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte_nfps_nfpconstraint_has_kind():
    assert hasattr(MARTE_NFPs_NfpConstraint, "kind")
    descriptor = None
    for klass in MARTE_NFPs_NfpConstraint.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_nfps_marte_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(NFPs_MARTE_EnumerationLiteral)


def test_nfps_marte_enumerationliteral_constructor_exists():
    assert callable(NFPs_MARTE_EnumerationLiteral.__init__)


def test_nfps_marte_enumerationliteral_constructor_args():
    sig = inspect.signature(NFPs_MARTE_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_nfps_unit_is_not_abstract():
    assert not inspect.isabstract(NFPs_Unit)


def test_nfps_unit_constructor_exists():
    assert callable(NFPs_Unit.__init__)


def test_nfps_unit_constructor_args():
    sig = inspect.signature(NFPs_Unit.__init__)
    params = list(sig.parameters.keys())



def test_marte_nfps_unit_is_not_abstract():
    assert not inspect.isabstract(MARTE_NFPs_Unit)


def test_marte_nfps_unit_constructor_exists():
    assert callable(MARTE_NFPs_Unit.__init__)


def test_marte_nfps_unit_constructor_args():
    sig = inspect.signature(MARTE_NFPs_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "convOffset" in params, "Missing parameter 'convOffset'"
    assert "convFactor" in params, "Missing parameter 'convFactor'"

def test_marte_nfps_unit_has_convOffset():
    assert hasattr(MARTE_NFPs_Unit, "convOffset")
    descriptor = None
    for klass in MARTE_NFPs_Unit.__mro__:
        if "convOffset" in klass.__dict__:
            descriptor = klass.__dict__["convOffset"]
            break
    assert isinstance(descriptor, property)

def test_marte_nfps_unit_has_convFactor():
    assert hasattr(MARTE_NFPs_Unit, "convFactor")
    descriptor = None
    for klass in MARTE_NFPs_Unit.__mro__:
        if "convFactor" in klass.__dict__:
            descriptor = klass.__dict__["convFactor"]
            break
    assert isinstance(descriptor, property)



def test_nfps_marte_property_is_not_abstract():
    assert not inspect.isabstract(NFPs_MARTE_Property)


def test_nfps_marte_property_constructor_exists():
    assert callable(NFPs_MARTE_Property.__init__)


def test_nfps_marte_property_constructor_args():
    sig = inspect.signature(NFPs_MARTE_Property.__init__)
    params = list(sig.parameters.keys())



def test_marte_nfps_nfp_is_not_abstract():
    assert not inspect.isabstract(MARTE_NFPs_Nfp)


def test_marte_nfps_nfp_constructor_exists():
    assert callable(MARTE_NFPs_Nfp.__init__)


def test_marte_nfps_nfp_constructor_args():
    sig = inspect.signature(MARTE_NFPs_Nfp.__init__)
    params = list(sig.parameters.keys())

def test_messageresourcekind_exists():
    # Check that the Enumeration exists
    assert MessageResourceKind is not None

def test_messageresourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageResourceKind]
    expected_literals = [
        "MessageQueue",
        "Blackboard",
        "Pipe",
        "Other",
        "Undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageResourceKind"

def test_repl_policy_exists():
    # Check that the Enumeration exists
    assert Repl_Policy is not None

def test_repl_policy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Repl_Policy]
    expected_literals = [
        "NFU",
        "other",
        "FIFO",
        "undef",
        "random",
        "LRU",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Repl_Policy"

def test_optimallitycriterionkind_exists():
    # Check that the Enumeration exists
    assert OptimallityCriterionKind is not None

def test_optimallitycriterionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptimallityCriterionKind]
    expected_literals = [
        "minimizeMissedDeadlines",
        "other",
        "undef",
        "minimizedMeanTardiness",
        "meetHardDeadlines",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptimallityCriterionKind"

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

def test_notificationkind_exists():
    # Check that the Enumeration exists
    assert NotificationKind is not None

def test_notificationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NotificationKind]
    expected_literals = [
        "Other",
        "Undef",
        "Bounded",
        "Memorized",
        "Memoryless",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NotificationKind"

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

def test_portspecificationkind_exists():
    # Check that the Enumeration exists
    assert PortSpecificationKind is not None

def test_portspecificationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PortSpecificationKind]
    expected_literals = [
        "featureBased",
        "interfaceBased",
        "atomic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PortSpecificationKind"

def test_cachetype_exists():
    # Check that the Enumeration exists
    assert CacheType is not None

def test_cachetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CacheType]
    expected_literals = [
        "undef",
        "unified",
        "instruction",
        "data",
        "other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CacheType"

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

def test_componentstate_exists():
    # Check that the Enumeration exists
    assert ComponentState is not None

def test_componentstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentState]
    expected_literals = [
        "operating",
        "undef",
        "storage",
        "other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentState"

def test_concurrentaccessprotocolkind_exists():
    # Check that the Enumeration exists
    assert ConcurrentAccessProtocolKind is not None

def test_concurrentaccessprotocolkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConcurrentAccessProtocolKind]
    expected_literals = [
        "PIP",
        "Undef",
        "Other",
        "PCP",
        "NoPreemption",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConcurrentAccessProtocolKind"

def test_rom_type_exists():
    # Check that the Enumeration exists
    assert ROM_Type is not None

def test_rom_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ROM_Type]
    expected_literals = [
        "EPROM",
        "EEPROM",
        "other",
        "undef",
        "maskedROM",
        "Flash",
        "OTP_EPROM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ROM_Type"

def test_isa_type_exists():
    # Check that the Enumeration exists
    assert ISA_Type is not None

def test_isa_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ISA_Type]
    expected_literals = [
        "RISC",
        "SIMD",
        "CISC",
        "other",
        "VLIW",
        "undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ISA_Type"

def test_allocationkind_exists():
    # Check that the Enumeration exists
    assert AllocationKind is not None

def test_allocationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AllocationKind]
    expected_literals = [
        "hybrid",
        "structural",
        "behavioral",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AllocationKind"

def test_allocationendkind_exists():
    # Check that the Enumeration exists
    assert AllocationEndKind is not None

def test_allocationendkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AllocationEndKind]
    expected_literals = [
        "executionPlatform",
        "both",
        "application",
        "undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AllocationEndKind"

def test_pld_technology_exists():
    # Check that the Enumeration exists
    assert PLD_Technology is not None

def test_pld_technology_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PLD_Technology]
    expected_literals = [
        "flash",
        "other",
        "SRAM",
        "undef",
        "antifuse",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PLD_Technology"

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

def test_pld_class_exists():
    # Check that the Enumeration exists
    assert PLD_Class is not None

def test_pld_class_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PLD_Class]
    expected_literals = [
        "undef",
        "symetricalArray",
        "seaOfGates",
        "rowBased",
        "hierarchicalPLD",
        "other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PLD_Class"

def test_allocationnature_exists():
    # Check that the Enumeration exists
    assert AllocationNature is not None

def test_allocationnature_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AllocationNature]
    expected_literals = [
        "timeScheduling",
        "spatialDistribution",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AllocationNature"

def test_executionkind_exists():
    # Check that the Enumeration exists
    assert ExecutionKind is not None

def test_executionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExecutionKind]
    expected_literals = [
        "localImmediate",
        "deferred",
        "remoteImmediate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExecutionKind"

def test_variabledirectionkind_exists():
    # Check that the Enumeration exists
    assert VariableDirectionKind is not None

def test_variabledirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableDirectionKind]
    expected_literals = [
        "out",
        "in_",
        "inout",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariableDirectionKind"

def test_synchronizationkind_exists():
    # Check that the Enumeration exists
    assert SynchronizationKind is not None

def test_synchronizationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SynchronizationKind]
    expected_literals = [
        "synchronous",
        "rendezVous",
        "other",
        "delayedSynchronous",
        "asynchronous",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SynchronizationKind"

def test_interruptkind_exists():
    # Check that the Enumeration exists
    assert InterruptKind is not None

def test_interruptkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InterruptKind]
    expected_literals = [
        "HardwareInterruption",
        "ProgrammedException",
        "Undef",
        "ProcessorDetectedException",
        "Other",
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
        "UserDefined",
        "LIFO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataPoolOrderingKind"

def test_notificationresourcekind_exists():
    # Check that the Enumeration exists
    assert NotificationResourceKind is not None

def test_notificationresourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NotificationResourceKind]
    expected_literals = [
        "Barrier",
        "Other",
        "Undef",
        "Event",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NotificationResourceKind"

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

def test_callconcurrencykind_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyKind is not None

def test_callconcurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyKind]
    expected_literals = [
        "guarded",
        "concurrent",
        "sequential",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyKind"

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

def test_poolmgtpolicykind_exists():
    # Check that the Enumeration exists
    assert PoolMgtPolicyKind is not None

def test_poolmgtpolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PoolMgtPolicyKind]
    expected_literals = [
        "exception",
        "timedWait",
        "infiniteWait",
        "other",
        "dynamic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PoolMgtPolicyKind"

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

def test_conditiontype_exists():
    # Check that the Enumeration exists
    assert ConditionType is not None

def test_conditiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionType]
    expected_literals = [
        "other",
        "altitude",
        "temperature",
        "vibration",
        "humidity",
        "undef",
        "shock",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionType"

def test_clientserverkind_exists():
    # Check that the Enumeration exists
    assert ClientServerKind is not None

def test_clientserverkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClientServerKind]
    expected_literals = [
        "provided",
        "required",
        "proreq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClientServerKind"

def test_componentkind_exists():
    # Check that the Enumeration exists
    assert ComponentKind is not None

def test_componentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentKind]
    expected_literals = [
        "channel",
        "other",
        "port",
        "card",
        "chip",
        "undef",
        "unit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentKind"

def test_queuepolicykind_exists():
    # Check that the Enumeration exists
    assert QueuePolicyKind is not None

def test_queuepolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QueuePolicyKind]
    expected_literals = [
        "Undef",
        "LIFO",
        "Other",
        "FIFO",
        "Priority",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QueuePolicyKind"

def test_accesspolicykind_exists():
    # Check that the Enumeration exists
    assert AccessPolicyKind is not None

def test_accesspolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessPolicyKind]
    expected_literals = [
        "Other",
        "ReadWrite",
        "Read",
        "Undef",
        "Write",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessPolicyKind"

def test_concurrencykind_exists():
    # Check that the Enumeration exists
    assert ConcurrencyKind is not None

def test_concurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConcurrencyKind]
    expected_literals = [
        "reader",
        "writer",
        "parallel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConcurrencyKind"


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
GQAM_GaCommStep_strategy = st.builds(
    GQAM_GaCommStep,
)
PAM_PaStep_strategy = st.builds(
    PAM_PaStep,
)
MARTE_PAM_PaCommStep_strategy = st.builds(
    MARTE_PAM_PaCommStep,
)
PAM_MARTE_NamedElement_strategy = st.builds(
    PAM_MARTE_NamedElement,
)
MARTE_PAM_PaRunTInstance_strategy = st.builds(
    MARTE_PAM_PaRunTInstance,
    throughput=
        safe_text,
    utilization=
        safe_text,
    unbddPool=
        safe_text,
    poolSize=
        safe_text
)
GaExecHost_strategy = st.builds(
    GaExecHost,
)
MARTE_SAM_SaExecHost_strategy = st.builds(
    MARTE_SAM_SaExecHost,
    isSched=
        safe_text,
    schedUtiliz=
        safe_text,
    schSlack=
        safe_text,
    ISRswitchT=
        safe_text,
    ISRprioRange=
        safe_text
)
GaCommHost_strategy = st.builds(
    GaCommHost,
)
MARTE_SAM_SaCommHost_strategy = st.builds(
    MARTE_SAM_SaCommHost,
    schSlack=
        safe_text,
    isSched=
        safe_text
)
MutualExclusionResource_strategy = st.builds(
    MutualExclusionResource,
)
GRM_SecondaryScheduler_strategy = st.builds(
    GRM_SecondaryScheduler,
)
ProcessingResource_strategy = st.builds(
    ProcessingResource,
)
MARTE_GRM_ComputingResource_strategy = st.builds(
    MARTE_GRM_ComputingResource,
)
GRM_Scheduler_strategy = st.builds(
    GRM_Scheduler,
)
GRM_SchedulableResource_strategy = st.builds(
    GRM_SchedulableResource,
)
GRM_MutualExclusionResource_strategy = st.builds(
    GRM_MutualExclusionResource,
)
GRM_ComputingResource_strategy = st.builds(
    GRM_ComputingResource,
)
GRM_ProcessingResource_strategy = st.builds(
    GRM_ProcessingResource,
)
Resource_strategy = st.builds(
    Resource,
)
MARTE_PAM_PaLogicalResource_strategy = st.builds(
    MARTE_PAM_PaLogicalResource,
    utilization=
        safe_text,
    poolSize=
        safe_text,
    throughput=
        safe_text
)
MARTE_GRM_SynchronizationResource_strategy = st.builds(
    MARTE_GRM_SynchronizationResource,
)
MARTE_GRM_ConcurrencyResource_strategy = st.builds(
    MARTE_GRM_ConcurrencyResource,
)
MARTE_GRM_Scheduler_strategy = st.builds(
    MARTE_GRM_Scheduler,
    schedPolicy=
        safe_text,
    schedule=
        safe_text,
    otherSchedPolicy=
        safe_text,
    isPreemptible=
        safe_text
)
MARTE_GRM_SchedulableResource_strategy = st.builds(
    MARTE_GRM_SchedulableResource,
    schedParams=
        safe_text
)
MARTE_GRM_CommunicationEndPoint_strategy = st.builds(
    MARTE_GRM_CommunicationEndPoint,
    packetSize=
        safe_text
)
MARTE_GRM_ProcessingResource_strategy = st.builds(
    MARTE_GRM_ProcessingResource,
    speedFactor=
        safe_text
)
MARTE_GRM_MutualExclusionResource_strategy = st.builds(
    MARTE_GRM_MutualExclusionResource,
    otherProtectProtocol=
        safe_text,
    ceiling=
        safe_text,
    protectKind=
        safe_text
)
MARTE_GRM_StorageResource_strategy = st.builds(
    MARTE_GRM_StorageResource,
    elementSize=
        safe_text
)
GRM_MARTE_Lifeline_strategy = st.builds(
    GRM_MARTE_Lifeline,
)
GRM_MARTE_Classifier_strategy = st.builds(
    GRM_MARTE_Classifier,
)
GRM_MARTE_InstanceSpecification_strategy = st.builds(
    GRM_MARTE_InstanceSpecification,
)
GRM_MARTE_Property_strategy = st.builds(
    GRM_MARTE_Property,
)
MARTE_GRM_Resource_strategy = st.builds(
    MARTE_GRM_Resource,
    isProtected=
        safe_text,
    isActive=
        safe_text,
    resMult=
        safe_text
)
Time_MARTE_Message_strategy = st.builds(
    Time_MARTE_Message,
)
Time_MARTE_Behavior_strategy = st.builds(
    Time_MARTE_Behavior,
)
GRM_MARTE_ConnectableElement_strategy = st.builds(
    GRM_MARTE_ConnectableElement,
)
Time_MARTE_Action_strategy = st.builds(
    Time_MARTE_Action,
)
Time_MARTE_TimeEvent_strategy = st.builds(
    Time_MARTE_TimeEvent,
)
Time_MARTE_DurationObservation_strategy = st.builds(
    Time_MARTE_DurationObservation,
)
Time_MARTE_TimeObservation_strategy = st.builds(
    Time_MARTE_TimeObservation,
)
Time_TimedElement_strategy = st.builds(
    Time_TimedElement,
)
Time_MARTE_ValueSpecification_strategy = st.builds(
    Time_MARTE_ValueSpecification,
)
TimedElement_strategy = st.builds(
    TimedElement,
)
MARTE_Time_TimedProcessing_strategy = st.builds(
    MARTE_Time_TimedProcessing,
)
MARTE_Time_TimedEvent_strategy = st.builds(
    MARTE_Time_TimedEvent,
    repetition=
        safe_text
)
MARTE_Time_TimedDurationObservation_strategy = st.builds(
    MARTE_Time_TimedDurationObservation,
    obsKind=
        safe_text
)
MARTE_Time_TimedInstantObservation_strategy = st.builds(
    MARTE_Time_TimedInstantObservation,
    obsKind=
        safe_text
)
MARTE_Time_TimedValueSpecification_strategy = st.builds(
    MARTE_Time_TimedValueSpecification,
    interpretation=
        safe_text
)
Time_Clock_strategy = st.builds(
    Time_Clock,
)
MARTE_Time_TimedElement_strategy = st.builds(
    MARTE_Time_TimedElement,
)
Time_MARTE_Class_strategy = st.builds(
    Time_MARTE_Class,
)
Time_MARTE_Operation_strategy = st.builds(
    Time_MARTE_Operation,
)
MARTE_Time_ClockType_strategy = st.builds(
    MARTE_Time_ClockType,
    nature=
        safe_text,
    isLogical=
        safe_text
)
Time_MARTE_Event_strategy = st.builds(
    Time_MARTE_Event,
)
Time_MARTE_Property_strategy = st.builds(
    Time_MARTE_Property,
)
Time_ClockType_strategy = st.builds(
    Time_ClockType,
)
Time_MARTE_InstanceSpecification_strategy = st.builds(
    Time_MARTE_InstanceSpecification,
)
MARTE_Time_Clock_strategy = st.builds(
    MARTE_Time_Clock,
    standard=
        safe_text
)
Time_MARTE_Namespace_strategy = st.builds(
    Time_MARTE_Namespace,
)
MARTE_Time_TimedDomain_strategy = st.builds(
    MARTE_Time_TimedDomain,
)
Alloc_MARTE_Abstraction_strategy = st.builds(
    Alloc_MARTE_Abstraction,
)
Time_MARTE_Enumeration_strategy = st.builds(
    Time_MARTE_Enumeration,
)
Alloc_MARTE_Comment_strategy = st.builds(
    Alloc_MARTE_Comment,
)
Alloc_MARTE_Element_strategy = st.builds(
    Alloc_MARTE_Element,
)
MARTE_Alloc_Assign_strategy = st.builds(
    MARTE_Alloc_Assign,
    nature=
        safe_text,
    kind=
        safe_text
)
NFPs_NfpConstraint_strategy = st.builds(
    NFPs_NfpConstraint,
)
MARTE_Time_TimedConstraint_strategy = st.builds(
    MARTE_Time_TimedConstraint,
    interpretation=
        safe_text
)
MARTE_Time_ClockConstraint_strategy = st.builds(
    MARTE_Time_ClockConstraint,
    isChronometricBased=
        safe_text,
    isPrecedenceBased=
        st.booleans(),
    isCoincidenceBased=
        safe_text
)
MARTE_Alloc_Allocate_strategy = st.builds(
    MARTE_Alloc_Allocate,
    kind=
        safe_text,
    nature=
        safe_text
)
MARTE_Alloc_NfpRefine_strategy = st.builds(
    MARTE_Alloc_NfpRefine,
)
Alloc_Allocated_strategy = st.builds(
    Alloc_Allocated,
)
Alloc_MARTE_ActivityPartition_strategy = st.builds(
    Alloc_MARTE_ActivityPartition,
)
MARTE_Alloc_AllocateActivityGroup_strategy = st.builds(
    MARTE_Alloc_AllocateActivityGroup,
    isUnique=
        safe_text
)
Alloc_MARTE_Dependency_strategy = st.builds(
    Alloc_MARTE_Dependency,
)
TupleType_strategy = st.builds(
    TupleType,
)
MARTE_NFPs_NfpType_strategy = st.builds(
    MARTE_NFPs_NfpType,
)
CoreElements_Mode_strategy = st.builds(
    CoreElements_Mode,
)
Alloc_MARTE_NamedElement_strategy = st.builds(
    Alloc_MARTE_NamedElement,
)
MARTE_SAM_SaSharedResource_strategy = st.builds(
    MARTE_SAM_SaSharedResource,
    isPreemp=
        safe_text,
    releaseT=
        safe_text,
    isConsum=
        safe_text,
    acquisT=
        safe_text,
    capacity=
        safe_text
)
SAM_SaSharedResource_strategy = st.builds(
    SAM_SaSharedResource,
)
SAM_MARTE_BehavioralFeature_strategy = st.builds(
    SAM_MARTE_BehavioralFeature,
)
MARTE_SAM_SaEndtoEndFlow_strategy = st.builds(
    MARTE_SAM_SaEndtoEndFlow,
    end2EndT=
        safe_text,
    end2EndD=
        safe_text,
    isSched=
        safe_text,
    schSlack=
        safe_text
)
GaAnalysisContext_strategy = st.builds(
    GaAnalysisContext,
)
MARTE_SAM_SaAnalysisContext_strategy = st.builds(
    MARTE_SAM_SaAnalysisContext,
    isSched=
        safe_text,
    optCriterion=
        safe_text
)
GQAM_MARTE_Classifier_strategy = st.builds(
    GQAM_MARTE_Classifier,
)
MARTE_GQAM_GaResourcesPlatform_strategy = st.builds(
    MARTE_GQAM_GaResourcesPlatform,
)
GQAM_GaResourcesPlatform_strategy = st.builds(
    GQAM_GaResourcesPlatform,
)
GQAM_GaWorkloadBehavior_strategy = st.builds(
    GQAM_GaWorkloadBehavior,
)
Variables_ExpressionContext_strategy = st.builds(
    Variables_ExpressionContext,
)
CoreElements_Configuration_strategy = st.builds(
    CoreElements_Configuration,
)
MARTE_GQAM_GaAnalysisContext_strategy = st.builds(
    MARTE_GQAM_GaAnalysisContext,
    context=
        safe_text
)
GaCommStep_strategy = st.builds(
    GaCommStep,
)
MARTE_SAM_SaCommStep_strategy = st.builds(
    MARTE_SAM_SaCommStep,
    deadline=
        safe_text,
    schSlack=
        safe_text,
    spareCap=
        safe_text
)
SAM_MARTE_NamedElement_strategy = st.builds(
    SAM_MARTE_NamedElement,
)
MARTE_GQAM_GaWorkloadBehavior_strategy = st.builds(
    MARTE_GQAM_GaWorkloadBehavior,
)
SchedulableResource_strategy = st.builds(
    SchedulableResource,
)
MARTE_GQAM_GaCommChannel_strategy = st.builds(
    MARTE_GQAM_GaCommChannel,
    utilization=
        safe_text,
    packetSize=
        safe_text
)
GaTimedObs_strategy = st.builds(
    GaTimedObs,
)
MARTE_SAM_SaSchedObs_strategy = st.builds(
    MARTE_SAM_SaSchedObs,
    blockT=
        safe_text,
    suspentions=
        safe_text,
    overlaps=
        safe_text
)
MARTE_GQAM_GaLatencyObs_strategy = st.builds(
    MARTE_GQAM_GaLatencyObs,
    miss=
        safe_text,
    latency=
        safe_text,
    utility=
        safe_text,
    maxJitter=
        safe_text
)
GQAM_MARTE_TimeObservation_strategy = st.builds(
    GQAM_MARTE_TimeObservation,
)
NfpConstraint_strategy = st.builds(
    NfpConstraint,
)
MARTE_GQAM_GaTimedObs_strategy = st.builds(
    MARTE_GQAM_GaTimedObs,
    laxity=
        safe_text
)
GQAM_MARTE_Operation_strategy = st.builds(
    GQAM_MARTE_Operation,
)
GaStep_strategy = st.builds(
    GaStep,
)
MARTE_PAM_PaResPassStep_strategy = st.builds(
    MARTE_PAM_PaResPassStep,
    resUnits=
        safe_text
)
MARTE_GQAM_GaCommStep_strategy = st.builds(
    MARTE_GQAM_GaCommStep,
)
MARTE_PAM_PaStep_strategy = st.builds(
    MARTE_PAM_PaStep,
    extOpCount=
        safe_text,
    behavCount=
        safe_text,
    noSync=
        safe_text,
    extOpDemand=
        safe_text
)
MARTE_GQAM_GaAcqStep_strategy = st.builds(
    MARTE_GQAM_GaAcqStep,
    resUnits=
        safe_text
)
MARTE_GQAM_GaRelStep_strategy = st.builds(
    MARTE_GQAM_GaRelStep,
    resUnits=
        safe_text
)
MARTE_SAM_SaStep_strategy = st.builds(
    MARTE_SAM_SaStep,
    schSlack=
        safe_text,
    deadline=
        safe_text,
    nonpreemptionBlocking=
        safe_text,
    readyT=
        safe_text,
    selfSuspensionBlocking=
        safe_text,
    numberSelfSuspensions=
        safe_text,
    spareCap=
        safe_text,
    preemptT=
        safe_text
)
MARTE_GQAM_GaRequestedService_strategy = st.builds(
    MARTE_GQAM_GaRequestedService,
)
MARTE_GQAM_GaExecHost_strategy = st.builds(
    MARTE_GQAM_GaExecHost,
    schedPriRange=
        safe_text,
    utilization=
        safe_text,
    memSize=
        safe_text,
    throughput=
        safe_text,
    clockOvh=
        safe_text,
    commRcvOvh=
        safe_text,
    cntxtSwT=
        safe_text,
    commTxOvh=
        safe_text
)
GQAM_GaExecHost_strategy = st.builds(
    GQAM_GaExecHost,
)
GaScenario_strategy = st.builds(
    GaScenario,
)
MARTE_GQAM_GaStep_strategy = st.builds(
    MARTE_GQAM_GaStep,
    priority=
        safe_text,
    rep=
        safe_text,
    selfDelay=
        safe_text,
    blockT=
        safe_text,
    servCount=
        safe_text,
    isAtomic=
        safe_text,
    prob=
        safe_text
)
GQAM_GaTimedObs_strategy = st.builds(
    GQAM_GaTimedObs,
)
GQAM_GaRequestedService_strategy = st.builds(
    GQAM_GaRequestedService,
)
MARTE_PAM_PaRequestedStep_strategy = st.builds(
    MARTE_PAM_PaRequestedStep,
)
GQAM_GaWorkloadEvent_strategy = st.builds(
    GQAM_GaWorkloadEvent,
)
Time_TimedProcessing_strategy = st.builds(
    Time_TimedProcessing,
)
GQAM_MARTE_TimeEvent_strategy = st.builds(
    GQAM_MARTE_TimeEvent,
)
GQAM_GaScenario_strategy = st.builds(
    GQAM_GaScenario,
)
GQAM_GaEventTrace_strategy = st.builds(
    GQAM_GaEventTrace,
)
GQAM_GaWorkloadGenerator_strategy = st.builds(
    GQAM_GaWorkloadGenerator,
)
MARTE_GQAM_GaWorkloadEvent_strategy = st.builds(
    MARTE_GQAM_GaWorkloadEvent,
    pattern=
        safe_text
)
GQAM_MARTE_NamedElement_strategy = st.builds(
    GQAM_MARTE_NamedElement,
)
GQAM_GaStep_strategy = st.builds(
    GQAM_GaStep,
)
MARTE_GQAM_GaWorkloadGenerator_strategy = st.builds(
    MARTE_GQAM_GaWorkloadGenerator,
    pop=
        safe_text
)
MARTE_GCM_GCMInvocatingBehavior_strategy = st.builds(
    MARTE_GCM_GCMInvocatingBehavior,
)
GCM_MARTE_Behavior_strategy = st.builds(
    GCM_MARTE_Behavior,
)
MARTE_GCM_DataPool_strategy = st.builds(
    MARTE_GCM_DataPool,
    ordering=
        safe_text
)
GCM_MARTE_Classifier_strategy = st.builds(
    GCM_MARTE_Classifier,
)
GCM_MARTE_AnyReceiveEvent_strategy = st.builds(
    GCM_MARTE_AnyReceiveEvent,
)
MARTE_GCM_DataEvent_strategy = st.builds(
    MARTE_GCM_DataEvent,
)
GCM_MARTE_InvocationAction_strategy = st.builds(
    GCM_MARTE_InvocationAction,
)
MARTE_GCM_GCMInvocationAction_strategy = st.builds(
    MARTE_GCM_GCMInvocationAction,
)
GCM_MARTE_Feature_strategy = st.builds(
    GCM_MARTE_Feature,
)
MARTE_GQAM_GaEventTrace_strategy = st.builds(
    MARTE_GQAM_GaEventTrace,
    content=
        safe_text,
    location=
        safe_text,
    format=
        safe_text
)
GQAM_MARTE_Behavior_strategy = st.builds(
    GQAM_MARTE_Behavior,
)
GCM_MARTE_BehavioralFeature_strategy = st.builds(
    GCM_MARTE_BehavioralFeature,
)
MARTE_GCM_ClientServerFeature_strategy = st.builds(
    MARTE_GCM_ClientServerFeature,
    kind=
        safe_text
)
MARTE_GCM_FlowSpecification_strategy = st.builds(
    MARTE_GCM_FlowSpecification,
)
MARTE_GCM_ClientServerSpecification_strategy = st.builds(
    MARTE_GCM_ClientServerSpecification,
)
GCM_ClientServerSpecification_strategy = st.builds(
    GCM_ClientServerSpecification,
)
GCM_MARTE_Interface_strategy = st.builds(
    GCM_MARTE_Interface,
)
MARTE_GCM_ClientServerPort_strategy = st.builds(
    MARTE_GCM_ClientServerPort,
    kind=
        safe_text,
    specificationKind=
        safe_text
)
GCM_MARTE_Port_strategy = st.builds(
    GCM_MARTE_Port,
)
MARTE_GCM_FlowPort_strategy = st.builds(
    MARTE_GCM_FlowPort,
    direction=
        safe_text,
    isAtomic=
        safe_text
)
GCM_MARTE_Trigger_strategy = st.builds(
    GCM_MARTE_Trigger,
)
MARTE_GCM_GCMTrigger_strategy = st.builds(
    MARTE_GCM_GCMTrigger,
)
MARTE_GCM_FlowProperty_strategy = st.builds(
    MARTE_GCM_FlowProperty,
    direction=
        safe_text
)
SW_Interaction_SwSynchronizationResource_strategy = st.builds(
    SW_Interaction_SwSynchronizationResource,
)
MARTE_SW_Interaction_SwMutualExclusionResource_strategy = st.builds(
    MARTE_SW_Interaction_SwMutualExclusionResource,
    mechanism=
        safe_text,
    concurrentAccessProtocol=
        safe_text
)
SwSynchronizationResource_strategy = st.builds(
    SwSynchronizationResource,
)
MARTE_SW_Interaction_NotificationResource_strategy = st.builds(
    MARTE_SW_Interaction_NotificationResource,
    occurence=
        safe_text,
    mechanism=
        safe_text
)
GCM_MARTE_Property_strategy = st.builds(
    GCM_MARTE_Property,
)
SW_Interaction_MARTE_BehavioralFeature_strategy = st.builds(
    SW_Interaction_MARTE_BehavioralFeature,
)
SwCommunicationResource_strategy = st.builds(
    SwCommunicationResource,
)
MARTE_SW_Interaction_MessageComResource_strategy = st.builds(
    MARTE_SW_Interaction_MessageComResource,
    messageQueuePolicy=
        safe_text,
    isFixedMessageSize=
        safe_text,
    mechanism=
        safe_text
)
MARTE_SW_Interaction_SharedDataComResource_strategy = st.builds(
    MARTE_SW_Interaction_SharedDataComResource,
)
GRM_SynchronizationResource_strategy = st.builds(
    GRM_SynchronizationResource,
)
SW_Interaction_SwInteractionResource_strategy = st.builds(
    SW_Interaction_SwInteractionResource,
)
MARTE_SW_Interaction_SwSynchronizationResource_strategy = st.builds(
    MARTE_SW_Interaction_SwSynchronizationResource,
)
SW_Interaction_MARTE_TypedElement_strategy = st.builds(
    SW_Interaction_MARTE_TypedElement,
)
SW_Brokering_MARTE_BehavioralFeature_strategy = st.builds(
    SW_Brokering_MARTE_BehavioralFeature,
)
SW_Brokering_MARTE_TypedElement_strategy = st.builds(
    SW_Brokering_MARTE_TypedElement,
)
InterruptResource_strategy = st.builds(
    InterruptResource,
)
MARTE_SW_Concurrency_Alarm_strategy = st.builds(
    MARTE_SW_Concurrency_Alarm,
    isWatchdog=
        safe_text
)
SW_Concurrency_MARTE_Namespace_strategy = st.builds(
    SW_Concurrency_MARTE_Namespace,
)
TimerResource_strategy = st.builds(
    TimerResource,
)
MARTE_SW_Concurrency_SwTimerResource_strategy = st.builds(
    MARTE_SW_Concurrency_SwTimerResource,
)
SW_Concurrency_MARTE_NamedElement_strategy = st.builds(
    SW_Concurrency_MARTE_NamedElement,
)
SW_Concurrency_SwConcurrentResource_strategy = st.builds(
    SW_Concurrency_SwConcurrentResource,
)
MARTE_SW_Concurrency_SwSchedulableResource_strategy = st.builds(
    MARTE_SW_Concurrency_SwSchedulableResource,
    isPreemptable=
        safe_text,
    isStaticSchedulingFeature=
        safe_text
)
SwConcurrentResource_strategy = st.builds(
    SwConcurrentResource,
)
MARTE_SW_Concurrency_InterruptResource_strategy = st.builds(
    MARTE_SW_Concurrency_InterruptResource,
    kind=
        safe_text,
    isMaskable=
        safe_text
)
SW_Concurrency_MARTE_Element_strategy = st.builds(
    SW_Concurrency_MARTE_Element,
)
SwResource_strategy = st.builds(
    SwResource,
)
MARTE_SW_Interaction_SwInteractionResource_strategy = st.builds(
    MARTE_SW_Interaction_SwInteractionResource,
    waitingQueuePolicy=
        safe_text,
    waitingQueueCapacity=
        safe_text,
    isIntraMemoryPartitionInteraction=
        st.booleans()
)
MARTE_SW_Brokering_MemoryBroker_strategy = st.builds(
    MARTE_SW_Brokering_MemoryBroker,
    accessPolicy=
        safe_text
)
MARTE_SW_Brokering_DeviceBroker_strategy = st.builds(
    MARTE_SW_Brokering_DeviceBroker,
    accessPolicy=
        safe_text,
    isBuffered=
        safe_text
)
MARTE_SW_Concurrency_MemoryPartition_strategy = st.builds(
    MARTE_SW_Concurrency_MemoryPartition,
)
MARTE_SW_Concurrency_SwConcurrentResource_strategy = st.builds(
    MARTE_SW_Concurrency_SwConcurrentResource,
    type=
        safe_text,
    activationCapacity=
        safe_text
)
SW_Concurrency_MARTE_BehavioralFeature_strategy = st.builds(
    SW_Concurrency_MARTE_BehavioralFeature,
)
SW_ResourceCore_MARTE_Property_strategy = st.builds(
    SW_ResourceCore_MARTE_Property,
)
SW_ResourceCore_MARTE_BehavioralFeature_strategy = st.builds(
    SW_ResourceCore_MARTE_BehavioralFeature,
)
SW_ResourceCore_MARTE_TypedElement_strategy = st.builds(
    SW_ResourceCore_MARTE_TypedElement,
)
SW_Concurrency_MARTE_TypedElement_strategy = st.builds(
    SW_Concurrency_MARTE_TypedElement,
)
HwComponent_strategy = st.builds(
    HwComponent,
)
MARTE_HwPower_HwCoolingSupply_strategy = st.builds(
    MARTE_HwPower_HwCoolingSupply,
    coolingPower=
        safe_text
)
MARTE_HwPower_HwPowerSupply_strategy = st.builds(
    MARTE_HwPower_HwPowerSupply,
    suppliedPower=
        safe_text,
    capacity=
        safe_text
)
HwLayout_HwComponent_strategy = st.builds(
    HwLayout_HwComponent,
)
MARTE_SW_ResourceCore_SwResource_strategy = st.builds(
    MARTE_SW_ResourceCore_SwResource,
)
HwCommunication_HwEndPoint_strategy = st.builds(
    HwCommunication_HwEndPoint,
)
HwGeneral_HwResourceService_strategy = st.builds(
    HwGeneral_HwResourceService,
)
MARTE_HwGeneral_HwResource_strategy = st.builds(
    MARTE_HwGeneral_HwResource,
    description=
        safe_text,
    frequency=
        safe_text
)
HwI_O_strategy = st.builds(
    HwI_O,
)
MARTE_HwDevice_HWSensor_strategy = st.builds(
    MARTE_HwDevice_HWSensor,
)
MARTE_HwDevice_HWActuator_strategy = st.builds(
    MARTE_HwDevice_HWActuator,
)
HwTiming_HwClock_strategy = st.builds(
    HwTiming_HwClock,
)
HwTimingResource_strategy = st.builds(
    HwTimingResource,
)
MARTE_HwTiming_HwTimer_strategy = st.builds(
    MARTE_HwTiming_HwTimer,
    counterWidth=
        safe_text,
    nbCounters=
        safe_text
)
MARTE_HwTiming_HwClock_strategy = st.builds(
    MARTE_HwTiming_HwClock,
)
GRM_TimingResource_strategy = st.builds(
    GRM_TimingResource,
)
HwDevice_strategy = st.builds(
    HwDevice,
)
MARTE_HwDevice_HwSupport_strategy = st.builds(
    MARTE_HwDevice_HwSupport,
)
MARTE_HwDevice_HwI_O_strategy = st.builds(
    MARTE_HwDevice_HwI_O,
)
GRM_DeviceResource_strategy = st.builds(
    GRM_DeviceResource,
)
HwMemory_strategy = st.builds(
    HwMemory,
)
MARTE_HwMemory_HwROM_strategy = st.builds(
    MARTE_HwMemory_HwROM,
    type=
        safe_text,
    organization=
        safe_text
)
MARTE_HwMemory_HwDrive_strategy = st.builds(
    MARTE_HwMemory_HwDrive,
    sectorSize=
        safe_text
)
MARTE_HwMemory_HwCache_strategy = st.builds(
    MARTE_HwMemory_HwCache,
    type=
        safe_text,
    writePolicy=
        safe_text,
    level=
        safe_text,
    repl_Policy=
        safe_text,
    structure=
        safe_text
)
MARTE_HwMemory_HwRAM_strategy = st.builds(
    MARTE_HwMemory_HwRAM,
    isSynchronous=
        safe_text,
    writePolicy=
        safe_text,
    repl_Policy=
        safe_text,
    isNonVolatile=
        safe_text,
    organization=
        safe_text,
    isStatic=
        safe_text
)
HwComputing_HwProcessor_strategy = st.builds(
    HwComputing_HwProcessor,
)
HwStorageManager_HwStorageManager_strategy = st.builds(
    HwStorageManager_HwStorageManager,
)
HwMemory_HwMemory_strategy = st.builds(
    HwMemory_HwMemory,
)
GRM_StorageResource_strategy = st.builds(
    GRM_StorageResource,
)
GRM_CommunicationEndPoint_strategy = st.builds(
    GRM_CommunicationEndPoint,
)
HwMedia_strategy = st.builds(
    HwMedia,
)
MARTE_HwCommunication_HwBridge_strategy = st.builds(
    MARTE_HwCommunication_HwBridge,
)
MARTE_HwCommunication_HwBus_strategy = st.builds(
    MARTE_HwCommunication_HwBus,
    wordWidth=
        safe_text,
    isSynchronous=
        safe_text,
    adressWidth=
        safe_text,
    isSerial=
        safe_text
)
HwCommunication_HwArbiter_strategy = st.builds(
    HwCommunication_HwArbiter,
)
MARTE_HwStorageManager_HwDMA_strategy = st.builds(
    MARTE_HwStorageManager_HwDMA,
    transferWidth=
        safe_text,
    nbChannels=
        safe_text
)
HwCommunication_HwCommunicationResource_strategy = st.builds(
    HwCommunication_HwCommunicationResource,
)
MARTE_HwCommunication_HwEndPoint_strategy = st.builds(
    MARTE_HwCommunication_HwEndPoint,
)
GRM_CommunicationMedia_strategy = st.builds(
    GRM_CommunicationMedia,
)
MARTE_GQAM_GaCommHost_strategy = st.builds(
    MARTE_GQAM_GaCommHost,
    throughput=
        safe_text,
    utilization=
        safe_text
)
MARTE_SW_Interaction_SwCommunicationResource_strategy = st.builds(
    MARTE_SW_Interaction_SwCommunicationResource,
)
MARTE_HwCommunication_HwMedia_strategy = st.builds(
    MARTE_HwCommunication_HwMedia,
    bandWidth=
        safe_text
)
HwStorageManager_strategy = st.builds(
    HwStorageManager,
)
MARTE_HwStorageManager_HwMMU_strategy = st.builds(
    MARTE_HwStorageManager_HwMMU,
    nbEntries=
        safe_text,
    physicalAddrSpace=
        safe_text,
    memoryProtection=
        safe_text,
    virtualAddrSpace=
        safe_text
)
HwComputing_HwComputingResource_strategy = st.builds(
    HwComputing_HwComputingResource,
)
HwMemory_HwRAM_strategy = st.builds(
    HwMemory_HwRAM,
)
HwResource_strategy = st.builds(
    HwResource,
)
MARTE_HwComputing_HwBranchPredictor_strategy = st.builds(
    MARTE_HwComputing_HwBranchPredictor,
)
MARTE_HwLayout_HwComponent_strategy = st.builds(
    MARTE_HwLayout_HwComponent,
    nbPins=
        safe_text,
    position=
        safe_text,
    staticDissipation=
        safe_text,
    price=
        safe_text,
    weight=
        safe_text,
    area=
        safe_text,
    grid=
        safe_text,
    dimensions=
        safe_text,
    staticConsumption=
        safe_text,
    r_Conditions=
        safe_text,
    kind=
        safe_text
)
MARTE_HwCommunication_HwCommunicationResource_strategy = st.builds(
    MARTE_HwCommunication_HwCommunicationResource,
)
MARTE_HwComputing_HwISA_strategy = st.builds(
    MARTE_HwComputing_HwISA,
    family=
        safe_text,
    type=
        safe_text,
    inst_Width=
        safe_text
)
HwGeneral_HwResource_strategy = st.builds(
    HwGeneral_HwResource,
)
MARTE_HwMemory_HwMemory_strategy = st.builds(
    MARTE_HwMemory_HwMemory,
    adressSize=
        safe_text,
    throughput=
        safe_text,
    timings=
        safe_text,
    memorySize=
        safe_text
)
MARTE_HwStorageManager_HwStorageManager_strategy = st.builds(
    MARTE_HwStorageManager_HwStorageManager,
)
MARTE_HwDevice_HwDevice_strategy = st.builds(
    MARTE_HwDevice_HwDevice,
)
MARTE_HwTiming_HwTimingResource_strategy = st.builds(
    MARTE_HwTiming_HwTimingResource,
)
MARTE_HwComputing_HwComputingResource_strategy = st.builds(
    MARTE_HwComputing_HwComputingResource,
    op_Frequencies=
        safe_text
)
HwCommunication_HwMedia_strategy = st.builds(
    HwCommunication_HwMedia,
)
HwCommunicationResource_strategy = st.builds(
    HwCommunicationResource,
)
MARTE_HwCommunication_HwArbiter_strategy = st.builds(
    MARTE_HwCommunication_HwArbiter,
)
HwMemory_HwCache_strategy = st.builds(
    HwMemory_HwCache,
)
HwComputing_HwBranchPredictor_strategy = st.builds(
    HwComputing_HwBranchPredictor,
)
HwComputing_HwISA_strategy = st.builds(
    HwComputing_HwISA,
)
HwComputingResource_strategy = st.builds(
    HwComputingResource,
)
MARTE_HwComputing_HwPLD_strategy = st.builds(
    MARTE_HwComputing_HwPLD,
    organization=
        safe_text,
    nbFlipFlops=
        safe_text,
    technology=
        safe_text,
    nbLUTs=
        safe_text,
    ndLUT_Inputs=
        safe_text
)
MARTE_HwComputing_HwASIC_strategy = st.builds(
    MARTE_HwComputing_HwASIC,
)
MARTE_HwComputing_HwProcessor_strategy = st.builds(
    MARTE_HwComputing_HwProcessor,
    ipc=
        safe_text,
    nbStages=
        safe_text,
    nbALUs=
        safe_text,
    mips=
        safe_text,
    nbCores=
        safe_text,
    architecture=
        safe_text,
    nbFPUs=
        safe_text,
    nbPipelines=
        safe_text
)
HwStorageManager_HwMMU_strategy = st.builds(
    HwStorageManager_HwMMU,
)
MARTE_HLAM_RtService_strategy = st.builds(
    MARTE_HLAM_RtService,
    isAtomic=
        safe_text,
    concPolicy=
        safe_text,
    synchKind=
        safe_text,
    exeKind=
        safe_text
)
MARTE_HLAM_RtAction_strategy = st.builds(
    MARTE_HLAM_RtAction,
    isAtomic=
        safe_text,
    msgSize=
        safe_text,
    synchKind=
        safe_text
)
HLAM_MARTE_Comment_strategy = st.builds(
    HLAM_MARTE_Comment,
)
Time_TimedInstantObservation_strategy = st.builds(
    Time_TimedInstantObservation,
)
MARTE_HLAM_RtSpecification_strategy = st.builds(
    MARTE_HLAM_RtSpecification,
    absDl=
        safe_text,
    priority=
        safe_text,
    miss=
        safe_text,
    relDl=
        safe_text,
    occKind=
        safe_text,
    utility=
        safe_text,
    rdTime=
        safe_text,
    boundDl=
        safe_text
)
HLAM_RtSpecification_strategy = st.builds(
    HLAM_RtSpecification,
)
HLAM_MARTE_InvocationAction_strategy = st.builds(
    HLAM_MARTE_InvocationAction,
)
HLAM_MARTE_Port_strategy = st.builds(
    HLAM_MARTE_Port,
)
HLAM_MARTE_Signal_strategy = st.builds(
    HLAM_MARTE_Signal,
)
HLAM_MARTE_Message_strategy = st.builds(
    HLAM_MARTE_Message,
)
HLAM_MARTE_BehavioralFeature_strategy = st.builds(
    HLAM_MARTE_BehavioralFeature,
)
MARTE_HLAM_RtFeature_strategy = st.builds(
    MARTE_HLAM_RtFeature,
)
MARTE_HLAM_PpUnit_strategy = st.builds(
    MARTE_HLAM_PpUnit,
    concPolicy=
        safe_text,
    memorySize=
        safe_text
)
HLAM_MARTE_Operation_strategy = st.builds(
    HLAM_MARTE_Operation,
)
HLAM_MARTE_Behavior_strategy = st.builds(
    HLAM_MARTE_Behavior,
)
MARTE_HLAM_RtUnit_strategy = st.builds(
    MARTE_HLAM_RtUnit,
    queueSize=
        safe_text,
    srPoolWaitingTime=
        safe_text,
    srPoolSize=
        safe_text,
    srPoolPolicy=
        safe_text,
    isMain=
        safe_text,
    msgMaxSize=
        safe_text,
    isDynamic=
        safe_text,
    memorySize=
        safe_text,
    queueSchedPolicy=
        safe_text
)
MARTE_DataTypes_TupleType_strategy = st.builds(
    MARTE_DataTypes_TupleType,
)
MARTE_DataTypes_ChoiceType_strategy = st.builds(
    MARTE_DataTypes_ChoiceType,
)
MARTE_DataTypes_CollectionType_strategy = st.builds(
    MARTE_DataTypes_CollectionType,
)
HLAM_MARTE_BehavioredClassifier_strategy = st.builds(
    HLAM_MARTE_BehavioredClassifier,
)
MARTE_DataTypes_IntervalType_strategy = st.builds(
    MARTE_DataTypes_IntervalType,
)
DataTypes_MARTE_DataType_strategy = st.builds(
    DataTypes_MARTE_DataType,
)
MARTE_DataTypes_BoundedSubtype_strategy = st.builds(
    MARTE_DataTypes_BoundedSubtype,
    isMaxOpen=
        st.booleans(),
    maxValue=
        safe_text,
    minValue=
        safe_text,
    isMinOpen=
        st.booleans()
)
Operators_MARTE_Behavior_strategy = st.builds(
    Operators_MARTE_Behavior,
)
MARTE_Operators_Operator_strategy = st.builds(
    MARTE_Operators_Operator,
    arity=
        safe_text,
    symbol=
        safe_text
)
Variables_MARTE_NamedElement_strategy = st.builds(
    Variables_MARTE_NamedElement,
)
MARTE_Variables_ExpressionContext_strategy = st.builds(
    MARTE_Variables_ExpressionContext,
)
Variables_MARTE_Property_strategy = st.builds(
    Variables_MARTE_Property,
)
MARTE_Variables_Var_strategy = st.builds(
    MARTE_Variables_Var,
    dir=
        safe_text
)
RSM_MARTE_MultiplicityElement_strategy = st.builds(
    RSM_MARTE_MultiplicityElement,
)
MARTE_RSM_Shaped_strategy = st.builds(
    MARTE_RSM_Shaped,
    shape=
        safe_text
)
DataTypes_MARTE_Property_strategy = st.builds(
    DataTypes_MARTE_Property,
)
Allocate_strategy = st.builds(
    Allocate,
)
MARTE_SW_Concurrency_EntryPoint_strategy = st.builds(
    MARTE_SW_Concurrency_EntryPoint,
    isReentrant=
        safe_text
)
MARTE_RSM_Distribute_strategy = st.builds(
    MARTE_RSM_Distribute,
    toTiler=
        safe_text,
    repetitionSpace=
        safe_text,
    patternShape=
        safe_text,
    fromTiler=
        safe_text
)
LinkTopology_strategy = st.builds(
    LinkTopology,
)
MARTE_RSM_Tiler_strategy = st.builds(
    MARTE_RSM_Tiler,
    origin=
        safe_text,
    fitting=
        safe_text,
    tiler=
        safe_text,
    paving=
        safe_text
)
MARTE_RSM_InterRepetition_strategy = st.builds(
    MARTE_RSM_InterRepetition,
    isModulo=
        safe_text,
    repetitionShapeDependence=
        safe_text
)
MARTE_RSM_Reshape_strategy = st.builds(
    MARTE_RSM_Reshape,
    patternShape=
        safe_text,
    repetitonShape=
        safe_text
)
MARTE_RSM_DefaultLink_strategy = st.builds(
    MARTE_RSM_DefaultLink,
)
RSM_MARTE_Connector_strategy = st.builds(
    RSM_MARTE_Connector,
)
MARTE_RSM_LinkTopology_strategy = st.builds(
    MARTE_RSM_LinkTopology,
)
GRM_ResourceUsage_strategy = st.builds(
    GRM_ResourceUsage,
)
MARTE_GQAM_GaScenario_strategy = st.builds(
    MARTE_GQAM_GaScenario,
    utilizationOnHost=
        safe_text,
    hostDemand=
        safe_text,
    utilization=
        safe_text,
    throughput=
        safe_text,
    respT=
        safe_text,
    interOccT=
        safe_text,
    hostDemandOps=
        safe_text
)
GRM_MARTE_NamedElement_strategy = st.builds(
    GRM_MARTE_NamedElement,
)
RSM_MARTE_ConnectorEnd_strategy = st.builds(
    RSM_MARTE_ConnectorEnd,
)
GrService_strategy = st.builds(
    GrService,
)
MARTE_HwGeneral_HwResourceService_strategy = st.builds(
    MARTE_HwGeneral_HwResourceService,
    consumption=
        safe_text,
    dissipation=
        safe_text
)
MARTE_SW_ResourceCore_SwAccessService_strategy = st.builds(
    MARTE_SW_ResourceCore_SwAccessService,
    isModifier=
        safe_text
)
MARTE_GRM_Acquire_strategy = st.builds(
    MARTE_GRM_Acquire,
    isBlocking=
        safe_text
)
MARTE_GRM_Release_strategy = st.builds(
    MARTE_GRM_Release,
)
GRM_MARTE_CollaborationUse_strategy = st.builds(
    GRM_MARTE_CollaborationUse,
)
GRM_MARTE_Collaboration_strategy = st.builds(
    GRM_MARTE_Collaboration,
)
GRM_MARTE_Behavior_strategy = st.builds(
    GRM_MARTE_Behavior,
)
GRM_MARTE_BehavioralFeature_strategy = st.builds(
    GRM_MARTE_BehavioralFeature,
)
GRM_MARTE_ExecutionSpecification_strategy = st.builds(
    GRM_MARTE_ExecutionSpecification,
)
GRM_Resource_strategy = st.builds(
    GRM_Resource,
)
MARTE_GRM_GrService_strategy = st.builds(
    MARTE_GRM_GrService,
)
TimingResource_strategy = st.builds(
    TimingResource,
)
MARTE_GRM_TimerResource_strategy = st.builds(
    MARTE_GRM_TimerResource,
    duration=
        safe_text,
    isPeriodic=
        safe_text
)
MARTE_GRM_ClockResource_strategy = st.builds(
    MARTE_GRM_ClockResource,
)
MARTE_GRM_TimingResource_strategy = st.builds(
    MARTE_GRM_TimingResource,
)
MARTE_GRM_DeviceResource_strategy = st.builds(
    MARTE_GRM_DeviceResource,
)
MARTE_GRM_ResourceUsage_strategy = st.builds(
    MARTE_GRM_ResourceUsage,
    usedMemory=
        safe_text,
    energy=
        safe_text,
    msgSize=
        safe_text,
    execTime=
        safe_text,
    allocatedMemory=
        safe_text,
    powerPeak=
        safe_text
)
GRM_MARTE_Connector_strategy = st.builds(
    GRM_MARTE_Connector,
)
MARTE_GRM_CommunicationMedia_strategy = st.builds(
    MARTE_GRM_CommunicationMedia,
    packetT=
        safe_text,
    capacity=
        safe_text,
    transmMode=
        safe_text,
    elementSize=
        safe_text,
    blockT=
        safe_text
)
Scheduler_strategy = st.builds(
    Scheduler,
)
MARTE_GRM_SecondaryScheduler_strategy = st.builds(
    MARTE_GRM_SecondaryScheduler,
)
MARTE_Alloc_Allocated_strategy = st.builds(
    MARTE_Alloc_Allocated,
    kind=
        safe_text
)
CoreElements_MARTE_State_strategy = st.builds(
    CoreElements_MARTE_State,
)
MARTE_CoreElements_Mode_strategy = st.builds(
    MARTE_CoreElements_Mode,
)
CoreElements_MARTE_Package_strategy = st.builds(
    CoreElements_MARTE_Package,
)
CoreElements_MARTE_StructuredClassifier_strategy = st.builds(
    CoreElements_MARTE_StructuredClassifier,
)
MARTE_CoreElements_Configuration_strategy = st.builds(
    MARTE_CoreElements_Configuration,
)
CoreElements_MARTE_StateMachine_strategy = st.builds(
    CoreElements_MARTE_StateMachine,
)
MARTE_CoreElements_ModeBehavior_strategy = st.builds(
    MARTE_CoreElements_ModeBehavior,
)
CoreElements_MARTE_Transition_strategy = st.builds(
    CoreElements_MARTE_Transition,
)
MARTE_CoreElements_ModeTransition_strategy = st.builds(
    MARTE_CoreElements_ModeTransition,
)
NFPs_MARTE_Enumeration_strategy = st.builds(
    NFPs_MARTE_Enumeration,
)
NFPs_Dimension_strategy = st.builds(
    NFPs_Dimension,
)
MARTE_NFPs_Dimension_strategy = st.builds(
    MARTE_NFPs_Dimension,
    baseExponent=
        st.integers(),
    symbol=
        safe_text
)
NFPs_MARTE_Constraint_strategy = st.builds(
    NFPs_MARTE_Constraint,
)
MARTE_NFPs_NfpConstraint_strategy = st.builds(
    MARTE_NFPs_NfpConstraint,
    kind=
        safe_text
)
NFPs_MARTE_EnumerationLiteral_strategy = st.builds(
    NFPs_MARTE_EnumerationLiteral,
)
NFPs_Unit_strategy = st.builds(
    NFPs_Unit,
)
MARTE_NFPs_Unit_strategy = st.builds(
    MARTE_NFPs_Unit,
    convOffset=
        safe_text,
    convFactor=
        safe_text
)
NFPs_MARTE_Property_strategy = st.builds(
    NFPs_MARTE_Property,
)
MARTE_NFPs_Nfp_strategy = st.builds(
    MARTE_NFPs_Nfp,
)

@given(instance=GQAM_GaCommStep_strategy)
@settings(max_examples=50)
def test_gqam_gacommstep_instantiation(instance):
    assert isinstance(instance, GQAM_GaCommStep)

@given(instance=PAM_PaStep_strategy)
@settings(max_examples=50)
def test_pam_pastep_instantiation(instance):
    assert isinstance(instance, PAM_PaStep)

@given(instance=MARTE_PAM_PaCommStep_strategy)
@settings(max_examples=50)
def test_marte_pam_pacommstep_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaCommStep)

@given(instance=PAM_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_pam_marte_namedelement_instantiation(instance):
    assert isinstance(instance, PAM_MARTE_NamedElement)

@given(instance=MARTE_PAM_PaRunTInstance_strategy)
@settings(max_examples=50)
def test_marte_pam_paruntinstance_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaRunTInstance)



@given(instance=MARTE_PAM_PaRunTInstance_strategy)
def test_marte_pam_paruntinstance_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original



@given(instance=MARTE_PAM_PaRunTInstance_strategy)
def test_marte_pam_paruntinstance_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original



@given(instance=MARTE_PAM_PaRunTInstance_strategy)
def test_marte_pam_paruntinstance_unbddPool_setter(instance):
    original = instance.unbddPool
    instance.unbddPool = original
    assert instance.unbddPool == original



@given(instance=MARTE_PAM_PaRunTInstance_strategy)
def test_marte_pam_paruntinstance_poolSize_setter(instance):
    original = instance.poolSize
    instance.poolSize = original
    assert instance.poolSize == original

@given(instance=GaExecHost_strategy)
@settings(max_examples=50)
def test_gaexechost_instantiation(instance):
    assert isinstance(instance, GaExecHost)

@given(instance=MARTE_SAM_SaExecHost_strategy)
@settings(max_examples=50)
def test_marte_sam_saexechost_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaExecHost)



@given(instance=MARTE_SAM_SaExecHost_strategy)
def test_marte_sam_saexechost_isSched_setter(instance):
    original = instance.isSched
    instance.isSched = original
    assert instance.isSched == original



@given(instance=MARTE_SAM_SaExecHost_strategy)
def test_marte_sam_saexechost_schedUtiliz_setter(instance):
    original = instance.schedUtiliz
    instance.schedUtiliz = original
    assert instance.schedUtiliz == original



@given(instance=MARTE_SAM_SaExecHost_strategy)
def test_marte_sam_saexechost_schSlack_setter(instance):
    original = instance.schSlack
    instance.schSlack = original
    assert instance.schSlack == original



@given(instance=MARTE_SAM_SaExecHost_strategy)
def test_marte_sam_saexechost_ISRswitchT_setter(instance):
    original = instance.ISRswitchT
    instance.ISRswitchT = original
    assert instance.ISRswitchT == original



@given(instance=MARTE_SAM_SaExecHost_strategy)
def test_marte_sam_saexechost_ISRprioRange_setter(instance):
    original = instance.ISRprioRange
    instance.ISRprioRange = original
    assert instance.ISRprioRange == original

@given(instance=GaCommHost_strategy)
@settings(max_examples=50)
def test_gacommhost_instantiation(instance):
    assert isinstance(instance, GaCommHost)

@given(instance=MARTE_SAM_SaCommHost_strategy)
@settings(max_examples=50)
def test_marte_sam_sacommhost_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaCommHost)



@given(instance=MARTE_SAM_SaCommHost_strategy)
def test_marte_sam_sacommhost_schSlack_setter(instance):
    original = instance.schSlack
    instance.schSlack = original
    assert instance.schSlack == original



@given(instance=MARTE_SAM_SaCommHost_strategy)
def test_marte_sam_sacommhost_isSched_setter(instance):
    original = instance.isSched
    instance.isSched = original
    assert instance.isSched == original

@given(instance=MutualExclusionResource_strategy)
@settings(max_examples=50)
def test_mutualexclusionresource_instantiation(instance):
    assert isinstance(instance, MutualExclusionResource)

@given(instance=GRM_SecondaryScheduler_strategy)
@settings(max_examples=50)
def test_grm_secondaryscheduler_instantiation(instance):
    assert isinstance(instance, GRM_SecondaryScheduler)

@given(instance=ProcessingResource_strategy)
@settings(max_examples=50)
def test_processingresource_instantiation(instance):
    assert isinstance(instance, ProcessingResource)

@given(instance=MARTE_GRM_ComputingResource_strategy)
@settings(max_examples=50)
def test_marte_grm_computingresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ComputingResource)

@given(instance=GRM_Scheduler_strategy)
@settings(max_examples=50)
def test_grm_scheduler_instantiation(instance):
    assert isinstance(instance, GRM_Scheduler)

@given(instance=GRM_SchedulableResource_strategy)
@settings(max_examples=50)
def test_grm_schedulableresource_instantiation(instance):
    assert isinstance(instance, GRM_SchedulableResource)

@given(instance=GRM_MutualExclusionResource_strategy)
@settings(max_examples=50)
def test_grm_mutualexclusionresource_instantiation(instance):
    assert isinstance(instance, GRM_MutualExclusionResource)

@given(instance=GRM_ComputingResource_strategy)
@settings(max_examples=50)
def test_grm_computingresource_instantiation(instance):
    assert isinstance(instance, GRM_ComputingResource)

@given(instance=GRM_ProcessingResource_strategy)
@settings(max_examples=50)
def test_grm_processingresource_instantiation(instance):
    assert isinstance(instance, GRM_ProcessingResource)

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=MARTE_PAM_PaLogicalResource_strategy)
@settings(max_examples=50)
def test_marte_pam_palogicalresource_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaLogicalResource)



@given(instance=MARTE_PAM_PaLogicalResource_strategy)
def test_marte_pam_palogicalresource_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original



@given(instance=MARTE_PAM_PaLogicalResource_strategy)
def test_marte_pam_palogicalresource_poolSize_setter(instance):
    original = instance.poolSize
    instance.poolSize = original
    assert instance.poolSize == original



@given(instance=MARTE_PAM_PaLogicalResource_strategy)
def test_marte_pam_palogicalresource_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original

@given(instance=MARTE_GRM_SynchronizationResource_strategy)
@settings(max_examples=50)
def test_marte_grm_synchronizationresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_SynchronizationResource)

@given(instance=MARTE_GRM_ConcurrencyResource_strategy)
@settings(max_examples=50)
def test_marte_grm_concurrencyresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ConcurrencyResource)

@given(instance=MARTE_GRM_Scheduler_strategy)
@settings(max_examples=50)
def test_marte_grm_scheduler_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_Scheduler)



@given(instance=MARTE_GRM_Scheduler_strategy)
def test_marte_grm_scheduler_schedPolicy_setter(instance):
    original = instance.schedPolicy
    instance.schedPolicy = original
    assert instance.schedPolicy == original



@given(instance=MARTE_GRM_Scheduler_strategy)
def test_marte_grm_scheduler_schedule_setter(instance):
    original = instance.schedule
    instance.schedule = original
    assert instance.schedule == original



@given(instance=MARTE_GRM_Scheduler_strategy)
def test_marte_grm_scheduler_otherSchedPolicy_setter(instance):
    original = instance.otherSchedPolicy
    instance.otherSchedPolicy = original
    assert instance.otherSchedPolicy == original



@given(instance=MARTE_GRM_Scheduler_strategy)
def test_marte_grm_scheduler_isPreemptible_setter(instance):
    original = instance.isPreemptible
    instance.isPreemptible = original
    assert instance.isPreemptible == original

@given(instance=MARTE_GRM_SchedulableResource_strategy)
@settings(max_examples=50)
def test_marte_grm_schedulableresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_SchedulableResource)



@given(instance=MARTE_GRM_SchedulableResource_strategy)
def test_marte_grm_schedulableresource_schedParams_setter(instance):
    original = instance.schedParams
    instance.schedParams = original
    assert instance.schedParams == original

@given(instance=MARTE_GRM_CommunicationEndPoint_strategy)
@settings(max_examples=50)
def test_marte_grm_communicationendpoint_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_CommunicationEndPoint)



@given(instance=MARTE_GRM_CommunicationEndPoint_strategy)
def test_marte_grm_communicationendpoint_packetSize_setter(instance):
    original = instance.packetSize
    instance.packetSize = original
    assert instance.packetSize == original

@given(instance=MARTE_GRM_ProcessingResource_strategy)
@settings(max_examples=50)
def test_marte_grm_processingresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ProcessingResource)



@given(instance=MARTE_GRM_ProcessingResource_strategy)
def test_marte_grm_processingresource_speedFactor_setter(instance):
    original = instance.speedFactor
    instance.speedFactor = original
    assert instance.speedFactor == original

@given(instance=MARTE_GRM_MutualExclusionResource_strategy)
@settings(max_examples=50)
def test_marte_grm_mutualexclusionresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_MutualExclusionResource)



@given(instance=MARTE_GRM_MutualExclusionResource_strategy)
def test_marte_grm_mutualexclusionresource_otherProtectProtocol_setter(instance):
    original = instance.otherProtectProtocol
    instance.otherProtectProtocol = original
    assert instance.otherProtectProtocol == original



@given(instance=MARTE_GRM_MutualExclusionResource_strategy)
def test_marte_grm_mutualexclusionresource_ceiling_setter(instance):
    original = instance.ceiling
    instance.ceiling = original
    assert instance.ceiling == original



@given(instance=MARTE_GRM_MutualExclusionResource_strategy)
def test_marte_grm_mutualexclusionresource_protectKind_setter(instance):
    original = instance.protectKind
    instance.protectKind = original
    assert instance.protectKind == original

@given(instance=MARTE_GRM_StorageResource_strategy)
@settings(max_examples=50)
def test_marte_grm_storageresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_StorageResource)



@given(instance=MARTE_GRM_StorageResource_strategy)
def test_marte_grm_storageresource_elementSize_setter(instance):
    original = instance.elementSize
    instance.elementSize = original
    assert instance.elementSize == original

@given(instance=GRM_MARTE_Lifeline_strategy)
@settings(max_examples=50)
def test_grm_marte_lifeline_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Lifeline)

@given(instance=GRM_MARTE_Classifier_strategy)
@settings(max_examples=50)
def test_grm_marte_classifier_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Classifier)

@given(instance=GRM_MARTE_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_grm_marte_instancespecification_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_InstanceSpecification)

@given(instance=GRM_MARTE_Property_strategy)
@settings(max_examples=50)
def test_grm_marte_property_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Property)

@given(instance=MARTE_GRM_Resource_strategy)
@settings(max_examples=50)
def test_marte_grm_resource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_Resource)



@given(instance=MARTE_GRM_Resource_strategy)
def test_marte_grm_resource_isProtected_setter(instance):
    original = instance.isProtected
    instance.isProtected = original
    assert instance.isProtected == original



@given(instance=MARTE_GRM_Resource_strategy)
def test_marte_grm_resource_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original



@given(instance=MARTE_GRM_Resource_strategy)
def test_marte_grm_resource_resMult_setter(instance):
    original = instance.resMult
    instance.resMult = original
    assert instance.resMult == original

@given(instance=Time_MARTE_Message_strategy)
@settings(max_examples=50)
def test_time_marte_message_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Message)

@given(instance=Time_MARTE_Behavior_strategy)
@settings(max_examples=50)
def test_time_marte_behavior_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Behavior)

@given(instance=GRM_MARTE_ConnectableElement_strategy)
@settings(max_examples=50)
def test_grm_marte_connectableelement_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_ConnectableElement)

@given(instance=Time_MARTE_Action_strategy)
@settings(max_examples=50)
def test_time_marte_action_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Action)

@given(instance=Time_MARTE_TimeEvent_strategy)
@settings(max_examples=50)
def test_time_marte_timeevent_instantiation(instance):
    assert isinstance(instance, Time_MARTE_TimeEvent)

@given(instance=Time_MARTE_DurationObservation_strategy)
@settings(max_examples=50)
def test_time_marte_durationobservation_instantiation(instance):
    assert isinstance(instance, Time_MARTE_DurationObservation)

@given(instance=Time_MARTE_TimeObservation_strategy)
@settings(max_examples=50)
def test_time_marte_timeobservation_instantiation(instance):
    assert isinstance(instance, Time_MARTE_TimeObservation)

@given(instance=Time_TimedElement_strategy)
@settings(max_examples=50)
def test_time_timedelement_instantiation(instance):
    assert isinstance(instance, Time_TimedElement)

@given(instance=Time_MARTE_ValueSpecification_strategy)
@settings(max_examples=50)
def test_time_marte_valuespecification_instantiation(instance):
    assert isinstance(instance, Time_MARTE_ValueSpecification)

@given(instance=TimedElement_strategy)
@settings(max_examples=50)
def test_timedelement_instantiation(instance):
    assert isinstance(instance, TimedElement)

@given(instance=MARTE_Time_TimedProcessing_strategy)
@settings(max_examples=50)
def test_marte_time_timedprocessing_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedProcessing)

@given(instance=MARTE_Time_TimedEvent_strategy)
@settings(max_examples=50)
def test_marte_time_timedevent_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedEvent)



@given(instance=MARTE_Time_TimedEvent_strategy)
def test_marte_time_timedevent_repetition_setter(instance):
    original = instance.repetition
    instance.repetition = original
    assert instance.repetition == original

@given(instance=MARTE_Time_TimedDurationObservation_strategy)
@settings(max_examples=50)
def test_marte_time_timeddurationobservation_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedDurationObservation)



@given(instance=MARTE_Time_TimedDurationObservation_strategy)
def test_marte_time_timeddurationobservation_obsKind_setter(instance):
    original = instance.obsKind
    instance.obsKind = original
    assert instance.obsKind == original

@given(instance=MARTE_Time_TimedInstantObservation_strategy)
@settings(max_examples=50)
def test_marte_time_timedinstantobservation_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedInstantObservation)



@given(instance=MARTE_Time_TimedInstantObservation_strategy)
def test_marte_time_timedinstantobservation_obsKind_setter(instance):
    original = instance.obsKind
    instance.obsKind = original
    assert instance.obsKind == original

@given(instance=MARTE_Time_TimedValueSpecification_strategy)
@settings(max_examples=50)
def test_marte_time_timedvaluespecification_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedValueSpecification)



@given(instance=MARTE_Time_TimedValueSpecification_strategy)
def test_marte_time_timedvaluespecification_interpretation_setter(instance):
    original = instance.interpretation
    instance.interpretation = original
    assert instance.interpretation == original

@given(instance=Time_Clock_strategy)
@settings(max_examples=50)
def test_time_clock_instantiation(instance):
    assert isinstance(instance, Time_Clock)

@given(instance=MARTE_Time_TimedElement_strategy)
@settings(max_examples=50)
def test_marte_time_timedelement_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedElement)

@given(instance=Time_MARTE_Class_strategy)
@settings(max_examples=50)
def test_time_marte_class_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Class)

@given(instance=Time_MARTE_Operation_strategy)
@settings(max_examples=50)
def test_time_marte_operation_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Operation)

@given(instance=MARTE_Time_ClockType_strategy)
@settings(max_examples=50)
def test_marte_time_clocktype_instantiation(instance):
    assert isinstance(instance, MARTE_Time_ClockType)



@given(instance=MARTE_Time_ClockType_strategy)
def test_marte_time_clocktype_nature_setter(instance):
    original = instance.nature
    instance.nature = original
    assert instance.nature == original



@given(instance=MARTE_Time_ClockType_strategy)
def test_marte_time_clocktype_isLogical_setter(instance):
    original = instance.isLogical
    instance.isLogical = original
    assert instance.isLogical == original

@given(instance=Time_MARTE_Event_strategy)
@settings(max_examples=50)
def test_time_marte_event_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Event)

@given(instance=Time_MARTE_Property_strategy)
@settings(max_examples=50)
def test_time_marte_property_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Property)

@given(instance=Time_ClockType_strategy)
@settings(max_examples=50)
def test_time_clocktype_instantiation(instance):
    assert isinstance(instance, Time_ClockType)

@given(instance=Time_MARTE_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_time_marte_instancespecification_instantiation(instance):
    assert isinstance(instance, Time_MARTE_InstanceSpecification)

@given(instance=MARTE_Time_Clock_strategy)
@settings(max_examples=50)
def test_marte_time_clock_instantiation(instance):
    assert isinstance(instance, MARTE_Time_Clock)



@given(instance=MARTE_Time_Clock_strategy)
def test_marte_time_clock_standard_setter(instance):
    original = instance.standard
    instance.standard = original
    assert instance.standard == original

@given(instance=Time_MARTE_Namespace_strategy)
@settings(max_examples=50)
def test_time_marte_namespace_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Namespace)

@given(instance=MARTE_Time_TimedDomain_strategy)
@settings(max_examples=50)
def test_marte_time_timeddomain_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedDomain)

@given(instance=Alloc_MARTE_Abstraction_strategy)
@settings(max_examples=50)
def test_alloc_marte_abstraction_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_Abstraction)

@given(instance=Time_MARTE_Enumeration_strategy)
@settings(max_examples=50)
def test_time_marte_enumeration_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Enumeration)

@given(instance=Alloc_MARTE_Comment_strategy)
@settings(max_examples=50)
def test_alloc_marte_comment_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_Comment)

@given(instance=Alloc_MARTE_Element_strategy)
@settings(max_examples=50)
def test_alloc_marte_element_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_Element)

@given(instance=MARTE_Alloc_Assign_strategy)
@settings(max_examples=50)
def test_marte_alloc_assign_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_Assign)



@given(instance=MARTE_Alloc_Assign_strategy)
def test_marte_alloc_assign_nature_setter(instance):
    original = instance.nature
    instance.nature = original
    assert instance.nature == original



@given(instance=MARTE_Alloc_Assign_strategy)
def test_marte_alloc_assign_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=NFPs_NfpConstraint_strategy)
@settings(max_examples=50)
def test_nfps_nfpconstraint_instantiation(instance):
    assert isinstance(instance, NFPs_NfpConstraint)

@given(instance=MARTE_Time_TimedConstraint_strategy)
@settings(max_examples=50)
def test_marte_time_timedconstraint_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedConstraint)



@given(instance=MARTE_Time_TimedConstraint_strategy)
def test_marte_time_timedconstraint_interpretation_setter(instance):
    original = instance.interpretation
    instance.interpretation = original
    assert instance.interpretation == original

@given(instance=MARTE_Time_ClockConstraint_strategy)
@settings(max_examples=50)
def test_marte_time_clockconstraint_instantiation(instance):
    assert isinstance(instance, MARTE_Time_ClockConstraint)



@given(instance=MARTE_Time_ClockConstraint_strategy)
def test_marte_time_clockconstraint_isChronometricBased_setter(instance):
    original = instance.isChronometricBased
    instance.isChronometricBased = original
    assert instance.isChronometricBased == original



@given(instance=MARTE_Time_ClockConstraint_strategy)
def test_marte_time_clockconstraint_isPrecedenceBased_setter(instance):
    original = instance.isPrecedenceBased
    instance.isPrecedenceBased = original
    assert instance.isPrecedenceBased == original



@given(instance=MARTE_Time_ClockConstraint_strategy)
def test_marte_time_clockconstraint_isCoincidenceBased_setter(instance):
    original = instance.isCoincidenceBased
    instance.isCoincidenceBased = original
    assert instance.isCoincidenceBased == original

@given(instance=MARTE_Alloc_Allocate_strategy)
@settings(max_examples=50)
def test_marte_alloc_allocate_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_Allocate)



@given(instance=MARTE_Alloc_Allocate_strategy)
def test_marte_alloc_allocate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=MARTE_Alloc_Allocate_strategy)
def test_marte_alloc_allocate_nature_setter(instance):
    original = instance.nature
    instance.nature = original
    assert instance.nature == original

@given(instance=MARTE_Alloc_NfpRefine_strategy)
@settings(max_examples=50)
def test_marte_alloc_nfprefine_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_NfpRefine)

@given(instance=Alloc_Allocated_strategy)
@settings(max_examples=50)
def test_alloc_allocated_instantiation(instance):
    assert isinstance(instance, Alloc_Allocated)

@given(instance=Alloc_MARTE_ActivityPartition_strategy)
@settings(max_examples=50)
def test_alloc_marte_activitypartition_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_ActivityPartition)

@given(instance=MARTE_Alloc_AllocateActivityGroup_strategy)
@settings(max_examples=50)
def test_marte_alloc_allocateactivitygroup_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_AllocateActivityGroup)



@given(instance=MARTE_Alloc_AllocateActivityGroup_strategy)
def test_marte_alloc_allocateactivitygroup_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=Alloc_MARTE_Dependency_strategy)
@settings(max_examples=50)
def test_alloc_marte_dependency_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_Dependency)

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=MARTE_NFPs_NfpType_strategy)
@settings(max_examples=50)
def test_marte_nfps_nfptype_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_NfpType)

@given(instance=CoreElements_Mode_strategy)
@settings(max_examples=50)
def test_coreelements_mode_instantiation(instance):
    assert isinstance(instance, CoreElements_Mode)

@given(instance=Alloc_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_alloc_marte_namedelement_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_NamedElement)

@given(instance=MARTE_SAM_SaSharedResource_strategy)
@settings(max_examples=50)
def test_marte_sam_sasharedresource_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaSharedResource)



@given(instance=MARTE_SAM_SaSharedResource_strategy)
def test_marte_sam_sasharedresource_isPreemp_setter(instance):
    original = instance.isPreemp
    instance.isPreemp = original
    assert instance.isPreemp == original



@given(instance=MARTE_SAM_SaSharedResource_strategy)
def test_marte_sam_sasharedresource_releaseT_setter(instance):
    original = instance.releaseT
    instance.releaseT = original
    assert instance.releaseT == original



@given(instance=MARTE_SAM_SaSharedResource_strategy)
def test_marte_sam_sasharedresource_isConsum_setter(instance):
    original = instance.isConsum
    instance.isConsum = original
    assert instance.isConsum == original



@given(instance=MARTE_SAM_SaSharedResource_strategy)
def test_marte_sam_sasharedresource_acquisT_setter(instance):
    original = instance.acquisT
    instance.acquisT = original
    assert instance.acquisT == original



@given(instance=MARTE_SAM_SaSharedResource_strategy)
def test_marte_sam_sasharedresource_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=SAM_SaSharedResource_strategy)
@settings(max_examples=50)
def test_sam_sasharedresource_instantiation(instance):
    assert isinstance(instance, SAM_SaSharedResource)

@given(instance=SAM_MARTE_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sam_marte_behavioralfeature_instantiation(instance):
    assert isinstance(instance, SAM_MARTE_BehavioralFeature)

@given(instance=MARTE_SAM_SaEndtoEndFlow_strategy)
@settings(max_examples=50)
def test_marte_sam_saendtoendflow_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaEndtoEndFlow)



@given(instance=MARTE_SAM_SaEndtoEndFlow_strategy)
def test_marte_sam_saendtoendflow_end2EndT_setter(instance):
    original = instance.end2EndT
    instance.end2EndT = original
    assert instance.end2EndT == original



@given(instance=MARTE_SAM_SaEndtoEndFlow_strategy)
def test_marte_sam_saendtoendflow_end2EndD_setter(instance):
    original = instance.end2EndD
    instance.end2EndD = original
    assert instance.end2EndD == original



@given(instance=MARTE_SAM_SaEndtoEndFlow_strategy)
def test_marte_sam_saendtoendflow_isSched_setter(instance):
    original = instance.isSched
    instance.isSched = original
    assert instance.isSched == original



@given(instance=MARTE_SAM_SaEndtoEndFlow_strategy)
def test_marte_sam_saendtoendflow_schSlack_setter(instance):
    original = instance.schSlack
    instance.schSlack = original
    assert instance.schSlack == original

@given(instance=GaAnalysisContext_strategy)
@settings(max_examples=50)
def test_gaanalysiscontext_instantiation(instance):
    assert isinstance(instance, GaAnalysisContext)

@given(instance=MARTE_SAM_SaAnalysisContext_strategy)
@settings(max_examples=50)
def test_marte_sam_saanalysiscontext_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaAnalysisContext)



@given(instance=MARTE_SAM_SaAnalysisContext_strategy)
def test_marte_sam_saanalysiscontext_isSched_setter(instance):
    original = instance.isSched
    instance.isSched = original
    assert instance.isSched == original



@given(instance=MARTE_SAM_SaAnalysisContext_strategy)
def test_marte_sam_saanalysiscontext_optCriterion_setter(instance):
    original = instance.optCriterion
    instance.optCriterion = original
    assert instance.optCriterion == original

@given(instance=GQAM_MARTE_Classifier_strategy)
@settings(max_examples=50)
def test_gqam_marte_classifier_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_Classifier)

@given(instance=MARTE_GQAM_GaResourcesPlatform_strategy)
@settings(max_examples=50)
def test_marte_gqam_garesourcesplatform_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaResourcesPlatform)

@given(instance=GQAM_GaResourcesPlatform_strategy)
@settings(max_examples=50)
def test_gqam_garesourcesplatform_instantiation(instance):
    assert isinstance(instance, GQAM_GaResourcesPlatform)

@given(instance=GQAM_GaWorkloadBehavior_strategy)
@settings(max_examples=50)
def test_gqam_gaworkloadbehavior_instantiation(instance):
    assert isinstance(instance, GQAM_GaWorkloadBehavior)

@given(instance=Variables_ExpressionContext_strategy)
@settings(max_examples=50)
def test_variables_expressioncontext_instantiation(instance):
    assert isinstance(instance, Variables_ExpressionContext)

@given(instance=CoreElements_Configuration_strategy)
@settings(max_examples=50)
def test_coreelements_configuration_instantiation(instance):
    assert isinstance(instance, CoreElements_Configuration)

@given(instance=MARTE_GQAM_GaAnalysisContext_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaanalysiscontext_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaAnalysisContext)



@given(instance=MARTE_GQAM_GaAnalysisContext_strategy)
def test_marte_gqam_gaanalysiscontext_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=GaCommStep_strategy)
@settings(max_examples=50)
def test_gacommstep_instantiation(instance):
    assert isinstance(instance, GaCommStep)

@given(instance=MARTE_SAM_SaCommStep_strategy)
@settings(max_examples=50)
def test_marte_sam_sacommstep_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaCommStep)



@given(instance=MARTE_SAM_SaCommStep_strategy)
def test_marte_sam_sacommstep_deadline_setter(instance):
    original = instance.deadline
    instance.deadline = original
    assert instance.deadline == original



@given(instance=MARTE_SAM_SaCommStep_strategy)
def test_marte_sam_sacommstep_schSlack_setter(instance):
    original = instance.schSlack
    instance.schSlack = original
    assert instance.schSlack == original



@given(instance=MARTE_SAM_SaCommStep_strategy)
def test_marte_sam_sacommstep_spareCap_setter(instance):
    original = instance.spareCap
    instance.spareCap = original
    assert instance.spareCap == original

@given(instance=SAM_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_sam_marte_namedelement_instantiation(instance):
    assert isinstance(instance, SAM_MARTE_NamedElement)

@given(instance=MARTE_GQAM_GaWorkloadBehavior_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaworkloadbehavior_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaWorkloadBehavior)

@given(instance=SchedulableResource_strategy)
@settings(max_examples=50)
def test_schedulableresource_instantiation(instance):
    assert isinstance(instance, SchedulableResource)

@given(instance=MARTE_GQAM_GaCommChannel_strategy)
@settings(max_examples=50)
def test_marte_gqam_gacommchannel_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaCommChannel)



@given(instance=MARTE_GQAM_GaCommChannel_strategy)
def test_marte_gqam_gacommchannel_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original



@given(instance=MARTE_GQAM_GaCommChannel_strategy)
def test_marte_gqam_gacommchannel_packetSize_setter(instance):
    original = instance.packetSize
    instance.packetSize = original
    assert instance.packetSize == original

@given(instance=GaTimedObs_strategy)
@settings(max_examples=50)
def test_gatimedobs_instantiation(instance):
    assert isinstance(instance, GaTimedObs)

@given(instance=MARTE_SAM_SaSchedObs_strategy)
@settings(max_examples=50)
def test_marte_sam_saschedobs_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaSchedObs)



@given(instance=MARTE_SAM_SaSchedObs_strategy)
def test_marte_sam_saschedobs_blockT_setter(instance):
    original = instance.blockT
    instance.blockT = original
    assert instance.blockT == original



@given(instance=MARTE_SAM_SaSchedObs_strategy)
def test_marte_sam_saschedobs_suspentions_setter(instance):
    original = instance.suspentions
    instance.suspentions = original
    assert instance.suspentions == original



@given(instance=MARTE_SAM_SaSchedObs_strategy)
def test_marte_sam_saschedobs_overlaps_setter(instance):
    original = instance.overlaps
    instance.overlaps = original
    assert instance.overlaps == original

@given(instance=MARTE_GQAM_GaLatencyObs_strategy)
@settings(max_examples=50)
def test_marte_gqam_galatencyobs_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaLatencyObs)



@given(instance=MARTE_GQAM_GaLatencyObs_strategy)
def test_marte_gqam_galatencyobs_miss_setter(instance):
    original = instance.miss
    instance.miss = original
    assert instance.miss == original



@given(instance=MARTE_GQAM_GaLatencyObs_strategy)
def test_marte_gqam_galatencyobs_latency_setter(instance):
    original = instance.latency
    instance.latency = original
    assert instance.latency == original



@given(instance=MARTE_GQAM_GaLatencyObs_strategy)
def test_marte_gqam_galatencyobs_utility_setter(instance):
    original = instance.utility
    instance.utility = original
    assert instance.utility == original



@given(instance=MARTE_GQAM_GaLatencyObs_strategy)
def test_marte_gqam_galatencyobs_maxJitter_setter(instance):
    original = instance.maxJitter
    instance.maxJitter = original
    assert instance.maxJitter == original

@given(instance=GQAM_MARTE_TimeObservation_strategy)
@settings(max_examples=50)
def test_gqam_marte_timeobservation_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_TimeObservation)

@given(instance=NfpConstraint_strategy)
@settings(max_examples=50)
def test_nfpconstraint_instantiation(instance):
    assert isinstance(instance, NfpConstraint)

@given(instance=MARTE_GQAM_GaTimedObs_strategy)
@settings(max_examples=50)
def test_marte_gqam_gatimedobs_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaTimedObs)



@given(instance=MARTE_GQAM_GaTimedObs_strategy)
def test_marte_gqam_gatimedobs_laxity_setter(instance):
    original = instance.laxity
    instance.laxity = original
    assert instance.laxity == original

@given(instance=GQAM_MARTE_Operation_strategy)
@settings(max_examples=50)
def test_gqam_marte_operation_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_Operation)

@given(instance=GaStep_strategy)
@settings(max_examples=50)
def test_gastep_instantiation(instance):
    assert isinstance(instance, GaStep)

@given(instance=MARTE_PAM_PaResPassStep_strategy)
@settings(max_examples=50)
def test_marte_pam_parespassstep_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaResPassStep)



@given(instance=MARTE_PAM_PaResPassStep_strategy)
def test_marte_pam_parespassstep_resUnits_setter(instance):
    original = instance.resUnits
    instance.resUnits = original
    assert instance.resUnits == original

@given(instance=MARTE_GQAM_GaCommStep_strategy)
@settings(max_examples=50)
def test_marte_gqam_gacommstep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaCommStep)

@given(instance=MARTE_PAM_PaStep_strategy)
@settings(max_examples=50)
def test_marte_pam_pastep_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaStep)



@given(instance=MARTE_PAM_PaStep_strategy)
def test_marte_pam_pastep_extOpCount_setter(instance):
    original = instance.extOpCount
    instance.extOpCount = original
    assert instance.extOpCount == original



@given(instance=MARTE_PAM_PaStep_strategy)
def test_marte_pam_pastep_behavCount_setter(instance):
    original = instance.behavCount
    instance.behavCount = original
    assert instance.behavCount == original



@given(instance=MARTE_PAM_PaStep_strategy)
def test_marte_pam_pastep_noSync_setter(instance):
    original = instance.noSync
    instance.noSync = original
    assert instance.noSync == original



@given(instance=MARTE_PAM_PaStep_strategy)
def test_marte_pam_pastep_extOpDemand_setter(instance):
    original = instance.extOpDemand
    instance.extOpDemand = original
    assert instance.extOpDemand == original

@given(instance=MARTE_GQAM_GaAcqStep_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaacqstep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaAcqStep)



@given(instance=MARTE_GQAM_GaAcqStep_strategy)
def test_marte_gqam_gaacqstep_resUnits_setter(instance):
    original = instance.resUnits
    instance.resUnits = original
    assert instance.resUnits == original

@given(instance=MARTE_GQAM_GaRelStep_strategy)
@settings(max_examples=50)
def test_marte_gqam_garelstep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaRelStep)



@given(instance=MARTE_GQAM_GaRelStep_strategy)
def test_marte_gqam_garelstep_resUnits_setter(instance):
    original = instance.resUnits
    instance.resUnits = original
    assert instance.resUnits == original

@given(instance=MARTE_SAM_SaStep_strategy)
@settings(max_examples=50)
def test_marte_sam_sastep_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaStep)



@given(instance=MARTE_SAM_SaStep_strategy)
def test_marte_sam_sastep_schSlack_setter(instance):
    original = instance.schSlack
    instance.schSlack = original
    assert instance.schSlack == original



@given(instance=MARTE_SAM_SaStep_strategy)
def test_marte_sam_sastep_deadline_setter(instance):
    original = instance.deadline
    instance.deadline = original
    assert instance.deadline == original



@given(instance=MARTE_SAM_SaStep_strategy)
def test_marte_sam_sastep_nonpreemptionBlocking_setter(instance):
    original = instance.nonpreemptionBlocking
    instance.nonpreemptionBlocking = original
    assert instance.nonpreemptionBlocking == original



@given(instance=MARTE_SAM_SaStep_strategy)
def test_marte_sam_sastep_readyT_setter(instance):
    original = instance.readyT
    instance.readyT = original
    assert instance.readyT == original



@given(instance=MARTE_SAM_SaStep_strategy)
def test_marte_sam_sastep_selfSuspensionBlocking_setter(instance):
    original = instance.selfSuspensionBlocking
    instance.selfSuspensionBlocking = original
    assert instance.selfSuspensionBlocking == original



@given(instance=MARTE_SAM_SaStep_strategy)
def test_marte_sam_sastep_numberSelfSuspensions_setter(instance):
    original = instance.numberSelfSuspensions
    instance.numberSelfSuspensions = original
    assert instance.numberSelfSuspensions == original



@given(instance=MARTE_SAM_SaStep_strategy)
def test_marte_sam_sastep_spareCap_setter(instance):
    original = instance.spareCap
    instance.spareCap = original
    assert instance.spareCap == original



@given(instance=MARTE_SAM_SaStep_strategy)
def test_marte_sam_sastep_preemptT_setter(instance):
    original = instance.preemptT
    instance.preemptT = original
    assert instance.preemptT == original

@given(instance=MARTE_GQAM_GaRequestedService_strategy)
@settings(max_examples=50)
def test_marte_gqam_garequestedservice_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaRequestedService)

@given(instance=MARTE_GQAM_GaExecHost_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaexechost_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaExecHost)



@given(instance=MARTE_GQAM_GaExecHost_strategy)
def test_marte_gqam_gaexechost_schedPriRange_setter(instance):
    original = instance.schedPriRange
    instance.schedPriRange = original
    assert instance.schedPriRange == original



@given(instance=MARTE_GQAM_GaExecHost_strategy)
def test_marte_gqam_gaexechost_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original



@given(instance=MARTE_GQAM_GaExecHost_strategy)
def test_marte_gqam_gaexechost_memSize_setter(instance):
    original = instance.memSize
    instance.memSize = original
    assert instance.memSize == original



@given(instance=MARTE_GQAM_GaExecHost_strategy)
def test_marte_gqam_gaexechost_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original



@given(instance=MARTE_GQAM_GaExecHost_strategy)
def test_marte_gqam_gaexechost_clockOvh_setter(instance):
    original = instance.clockOvh
    instance.clockOvh = original
    assert instance.clockOvh == original



@given(instance=MARTE_GQAM_GaExecHost_strategy)
def test_marte_gqam_gaexechost_commRcvOvh_setter(instance):
    original = instance.commRcvOvh
    instance.commRcvOvh = original
    assert instance.commRcvOvh == original



@given(instance=MARTE_GQAM_GaExecHost_strategy)
def test_marte_gqam_gaexechost_cntxtSwT_setter(instance):
    original = instance.cntxtSwT
    instance.cntxtSwT = original
    assert instance.cntxtSwT == original



@given(instance=MARTE_GQAM_GaExecHost_strategy)
def test_marte_gqam_gaexechost_commTxOvh_setter(instance):
    original = instance.commTxOvh
    instance.commTxOvh = original
    assert instance.commTxOvh == original

@given(instance=GQAM_GaExecHost_strategy)
@settings(max_examples=50)
def test_gqam_gaexechost_instantiation(instance):
    assert isinstance(instance, GQAM_GaExecHost)

@given(instance=GaScenario_strategy)
@settings(max_examples=50)
def test_gascenario_instantiation(instance):
    assert isinstance(instance, GaScenario)

@given(instance=MARTE_GQAM_GaStep_strategy)
@settings(max_examples=50)
def test_marte_gqam_gastep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaStep)



@given(instance=MARTE_GQAM_GaStep_strategy)
def test_marte_gqam_gastep_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=MARTE_GQAM_GaStep_strategy)
def test_marte_gqam_gastep_rep_setter(instance):
    original = instance.rep
    instance.rep = original
    assert instance.rep == original



@given(instance=MARTE_GQAM_GaStep_strategy)
def test_marte_gqam_gastep_selfDelay_setter(instance):
    original = instance.selfDelay
    instance.selfDelay = original
    assert instance.selfDelay == original



@given(instance=MARTE_GQAM_GaStep_strategy)
def test_marte_gqam_gastep_blockT_setter(instance):
    original = instance.blockT
    instance.blockT = original
    assert instance.blockT == original



@given(instance=MARTE_GQAM_GaStep_strategy)
def test_marte_gqam_gastep_servCount_setter(instance):
    original = instance.servCount
    instance.servCount = original
    assert instance.servCount == original



@given(instance=MARTE_GQAM_GaStep_strategy)
def test_marte_gqam_gastep_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original



@given(instance=MARTE_GQAM_GaStep_strategy)
def test_marte_gqam_gastep_prob_setter(instance):
    original = instance.prob
    instance.prob = original
    assert instance.prob == original

@given(instance=GQAM_GaTimedObs_strategy)
@settings(max_examples=50)
def test_gqam_gatimedobs_instantiation(instance):
    assert isinstance(instance, GQAM_GaTimedObs)

@given(instance=GQAM_GaRequestedService_strategy)
@settings(max_examples=50)
def test_gqam_garequestedservice_instantiation(instance):
    assert isinstance(instance, GQAM_GaRequestedService)

@given(instance=MARTE_PAM_PaRequestedStep_strategy)
@settings(max_examples=50)
def test_marte_pam_parequestedstep_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaRequestedStep)

@given(instance=GQAM_GaWorkloadEvent_strategy)
@settings(max_examples=50)
def test_gqam_gaworkloadevent_instantiation(instance):
    assert isinstance(instance, GQAM_GaWorkloadEvent)

@given(instance=Time_TimedProcessing_strategy)
@settings(max_examples=50)
def test_time_timedprocessing_instantiation(instance):
    assert isinstance(instance, Time_TimedProcessing)

@given(instance=GQAM_MARTE_TimeEvent_strategy)
@settings(max_examples=50)
def test_gqam_marte_timeevent_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_TimeEvent)

@given(instance=GQAM_GaScenario_strategy)
@settings(max_examples=50)
def test_gqam_gascenario_instantiation(instance):
    assert isinstance(instance, GQAM_GaScenario)

@given(instance=GQAM_GaEventTrace_strategy)
@settings(max_examples=50)
def test_gqam_gaeventtrace_instantiation(instance):
    assert isinstance(instance, GQAM_GaEventTrace)

@given(instance=GQAM_GaWorkloadGenerator_strategy)
@settings(max_examples=50)
def test_gqam_gaworkloadgenerator_instantiation(instance):
    assert isinstance(instance, GQAM_GaWorkloadGenerator)

@given(instance=MARTE_GQAM_GaWorkloadEvent_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaworkloadevent_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaWorkloadEvent)



@given(instance=MARTE_GQAM_GaWorkloadEvent_strategy)
def test_marte_gqam_gaworkloadevent_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=GQAM_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_gqam_marte_namedelement_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_NamedElement)

@given(instance=GQAM_GaStep_strategy)
@settings(max_examples=50)
def test_gqam_gastep_instantiation(instance):
    assert isinstance(instance, GQAM_GaStep)

@given(instance=MARTE_GQAM_GaWorkloadGenerator_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaworkloadgenerator_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaWorkloadGenerator)



@given(instance=MARTE_GQAM_GaWorkloadGenerator_strategy)
def test_marte_gqam_gaworkloadgenerator_pop_setter(instance):
    original = instance.pop
    instance.pop = original
    assert instance.pop == original

@given(instance=MARTE_GCM_GCMInvocatingBehavior_strategy)
@settings(max_examples=50)
def test_marte_gcm_gcminvocatingbehavior_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_GCMInvocatingBehavior)

@given(instance=GCM_MARTE_Behavior_strategy)
@settings(max_examples=50)
def test_gcm_marte_behavior_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Behavior)

@given(instance=MARTE_GCM_DataPool_strategy)
@settings(max_examples=50)
def test_marte_gcm_datapool_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_DataPool)



@given(instance=MARTE_GCM_DataPool_strategy)
def test_marte_gcm_datapool_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=GCM_MARTE_Classifier_strategy)
@settings(max_examples=50)
def test_gcm_marte_classifier_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Classifier)

@given(instance=GCM_MARTE_AnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_gcm_marte_anyreceiveevent_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_AnyReceiveEvent)

@given(instance=MARTE_GCM_DataEvent_strategy)
@settings(max_examples=50)
def test_marte_gcm_dataevent_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_DataEvent)

@given(instance=GCM_MARTE_InvocationAction_strategy)
@settings(max_examples=50)
def test_gcm_marte_invocationaction_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_InvocationAction)

@given(instance=MARTE_GCM_GCMInvocationAction_strategy)
@settings(max_examples=50)
def test_marte_gcm_gcminvocationaction_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_GCMInvocationAction)

@given(instance=GCM_MARTE_Feature_strategy)
@settings(max_examples=50)
def test_gcm_marte_feature_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Feature)

@given(instance=MARTE_GQAM_GaEventTrace_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaeventtrace_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaEventTrace)



@given(instance=MARTE_GQAM_GaEventTrace_strategy)
def test_marte_gqam_gaeventtrace_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=MARTE_GQAM_GaEventTrace_strategy)
def test_marte_gqam_gaeventtrace_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=MARTE_GQAM_GaEventTrace_strategy)
def test_marte_gqam_gaeventtrace_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=GQAM_MARTE_Behavior_strategy)
@settings(max_examples=50)
def test_gqam_marte_behavior_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_Behavior)

@given(instance=GCM_MARTE_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_gcm_marte_behavioralfeature_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_BehavioralFeature)

@given(instance=MARTE_GCM_ClientServerFeature_strategy)
@settings(max_examples=50)
def test_marte_gcm_clientserverfeature_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_ClientServerFeature)



@given(instance=MARTE_GCM_ClientServerFeature_strategy)
def test_marte_gcm_clientserverfeature_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MARTE_GCM_FlowSpecification_strategy)
@settings(max_examples=50)
def test_marte_gcm_flowspecification_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_FlowSpecification)

@given(instance=MARTE_GCM_ClientServerSpecification_strategy)
@settings(max_examples=50)
def test_marte_gcm_clientserverspecification_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_ClientServerSpecification)

@given(instance=GCM_ClientServerSpecification_strategy)
@settings(max_examples=50)
def test_gcm_clientserverspecification_instantiation(instance):
    assert isinstance(instance, GCM_ClientServerSpecification)

@given(instance=GCM_MARTE_Interface_strategy)
@settings(max_examples=50)
def test_gcm_marte_interface_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Interface)

@given(instance=MARTE_GCM_ClientServerPort_strategy)
@settings(max_examples=50)
def test_marte_gcm_clientserverport_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_ClientServerPort)



@given(instance=MARTE_GCM_ClientServerPort_strategy)
def test_marte_gcm_clientserverport_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=MARTE_GCM_ClientServerPort_strategy)
def test_marte_gcm_clientserverport_specificationKind_setter(instance):
    original = instance.specificationKind
    instance.specificationKind = original
    assert instance.specificationKind == original

@given(instance=GCM_MARTE_Port_strategy)
@settings(max_examples=50)
def test_gcm_marte_port_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Port)

@given(instance=MARTE_GCM_FlowPort_strategy)
@settings(max_examples=50)
def test_marte_gcm_flowport_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_FlowPort)



@given(instance=MARTE_GCM_FlowPort_strategy)
def test_marte_gcm_flowport_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=MARTE_GCM_FlowPort_strategy)
def test_marte_gcm_flowport_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original

@given(instance=GCM_MARTE_Trigger_strategy)
@settings(max_examples=50)
def test_gcm_marte_trigger_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Trigger)

@given(instance=MARTE_GCM_GCMTrigger_strategy)
@settings(max_examples=50)
def test_marte_gcm_gcmtrigger_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_GCMTrigger)

@given(instance=MARTE_GCM_FlowProperty_strategy)
@settings(max_examples=50)
def test_marte_gcm_flowproperty_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_FlowProperty)



@given(instance=MARTE_GCM_FlowProperty_strategy)
def test_marte_gcm_flowproperty_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=SW_Interaction_SwSynchronizationResource_strategy)
@settings(max_examples=50)
def test_sw_interaction_swsynchronizationresource_instantiation(instance):
    assert isinstance(instance, SW_Interaction_SwSynchronizationResource)

@given(instance=MARTE_SW_Interaction_SwMutualExclusionResource_strategy)
@settings(max_examples=50)
def test_marte_sw_interaction_swmutualexclusionresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_SwMutualExclusionResource)



@given(instance=MARTE_SW_Interaction_SwMutualExclusionResource_strategy)
def test_marte_sw_interaction_swmutualexclusionresource_mechanism_setter(instance):
    original = instance.mechanism
    instance.mechanism = original
    assert instance.mechanism == original



@given(instance=MARTE_SW_Interaction_SwMutualExclusionResource_strategy)
def test_marte_sw_interaction_swmutualexclusionresource_concurrentAccessProtocol_setter(instance):
    original = instance.concurrentAccessProtocol
    instance.concurrentAccessProtocol = original
    assert instance.concurrentAccessProtocol == original

@given(instance=SwSynchronizationResource_strategy)
@settings(max_examples=50)
def test_swsynchronizationresource_instantiation(instance):
    assert isinstance(instance, SwSynchronizationResource)

@given(instance=MARTE_SW_Interaction_NotificationResource_strategy)
@settings(max_examples=50)
def test_marte_sw_interaction_notificationresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_NotificationResource)



@given(instance=MARTE_SW_Interaction_NotificationResource_strategy)
def test_marte_sw_interaction_notificationresource_occurence_setter(instance):
    original = instance.occurence
    instance.occurence = original
    assert instance.occurence == original



@given(instance=MARTE_SW_Interaction_NotificationResource_strategy)
def test_marte_sw_interaction_notificationresource_mechanism_setter(instance):
    original = instance.mechanism
    instance.mechanism = original
    assert instance.mechanism == original

@given(instance=GCM_MARTE_Property_strategy)
@settings(max_examples=50)
def test_gcm_marte_property_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Property)

@given(instance=SW_Interaction_MARTE_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw_interaction_marte_behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW_Interaction_MARTE_BehavioralFeature)

@given(instance=SwCommunicationResource_strategy)
@settings(max_examples=50)
def test_swcommunicationresource_instantiation(instance):
    assert isinstance(instance, SwCommunicationResource)

@given(instance=MARTE_SW_Interaction_MessageComResource_strategy)
@settings(max_examples=50)
def test_marte_sw_interaction_messagecomresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_MessageComResource)



@given(instance=MARTE_SW_Interaction_MessageComResource_strategy)
def test_marte_sw_interaction_messagecomresource_messageQueuePolicy_setter(instance):
    original = instance.messageQueuePolicy
    instance.messageQueuePolicy = original
    assert instance.messageQueuePolicy == original



@given(instance=MARTE_SW_Interaction_MessageComResource_strategy)
def test_marte_sw_interaction_messagecomresource_isFixedMessageSize_setter(instance):
    original = instance.isFixedMessageSize
    instance.isFixedMessageSize = original
    assert instance.isFixedMessageSize == original



@given(instance=MARTE_SW_Interaction_MessageComResource_strategy)
def test_marte_sw_interaction_messagecomresource_mechanism_setter(instance):
    original = instance.mechanism
    instance.mechanism = original
    assert instance.mechanism == original

@given(instance=MARTE_SW_Interaction_SharedDataComResource_strategy)
@settings(max_examples=50)
def test_marte_sw_interaction_shareddatacomresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_SharedDataComResource)

@given(instance=GRM_SynchronizationResource_strategy)
@settings(max_examples=50)
def test_grm_synchronizationresource_instantiation(instance):
    assert isinstance(instance, GRM_SynchronizationResource)

@given(instance=SW_Interaction_SwInteractionResource_strategy)
@settings(max_examples=50)
def test_sw_interaction_swinteractionresource_instantiation(instance):
    assert isinstance(instance, SW_Interaction_SwInteractionResource)

@given(instance=MARTE_SW_Interaction_SwSynchronizationResource_strategy)
@settings(max_examples=50)
def test_marte_sw_interaction_swsynchronizationresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_SwSynchronizationResource)

@given(instance=SW_Interaction_MARTE_TypedElement_strategy)
@settings(max_examples=50)
def test_sw_interaction_marte_typedelement_instantiation(instance):
    assert isinstance(instance, SW_Interaction_MARTE_TypedElement)

@given(instance=SW_Brokering_MARTE_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw_brokering_marte_behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW_Brokering_MARTE_BehavioralFeature)

@given(instance=SW_Brokering_MARTE_TypedElement_strategy)
@settings(max_examples=50)
def test_sw_brokering_marte_typedelement_instantiation(instance):
    assert isinstance(instance, SW_Brokering_MARTE_TypedElement)

@given(instance=InterruptResource_strategy)
@settings(max_examples=50)
def test_interruptresource_instantiation(instance):
    assert isinstance(instance, InterruptResource)

@given(instance=MARTE_SW_Concurrency_Alarm_strategy)
@settings(max_examples=50)
def test_marte_sw_concurrency_alarm_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_Alarm)



@given(instance=MARTE_SW_Concurrency_Alarm_strategy)
def test_marte_sw_concurrency_alarm_isWatchdog_setter(instance):
    original = instance.isWatchdog
    instance.isWatchdog = original
    assert instance.isWatchdog == original

@given(instance=SW_Concurrency_MARTE_Namespace_strategy)
@settings(max_examples=50)
def test_sw_concurrency_marte_namespace_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_Namespace)

@given(instance=TimerResource_strategy)
@settings(max_examples=50)
def test_timerresource_instantiation(instance):
    assert isinstance(instance, TimerResource)

@given(instance=MARTE_SW_Concurrency_SwTimerResource_strategy)
@settings(max_examples=50)
def test_marte_sw_concurrency_swtimerresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_SwTimerResource)

@given(instance=SW_Concurrency_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_sw_concurrency_marte_namedelement_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_NamedElement)

@given(instance=SW_Concurrency_SwConcurrentResource_strategy)
@settings(max_examples=50)
def test_sw_concurrency_swconcurrentresource_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_SwConcurrentResource)

@given(instance=MARTE_SW_Concurrency_SwSchedulableResource_strategy)
@settings(max_examples=50)
def test_marte_sw_concurrency_swschedulableresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_SwSchedulableResource)



@given(instance=MARTE_SW_Concurrency_SwSchedulableResource_strategy)
def test_marte_sw_concurrency_swschedulableresource_isPreemptable_setter(instance):
    original = instance.isPreemptable
    instance.isPreemptable = original
    assert instance.isPreemptable == original



@given(instance=MARTE_SW_Concurrency_SwSchedulableResource_strategy)
def test_marte_sw_concurrency_swschedulableresource_isStaticSchedulingFeature_setter(instance):
    original = instance.isStaticSchedulingFeature
    instance.isStaticSchedulingFeature = original
    assert instance.isStaticSchedulingFeature == original

@given(instance=SwConcurrentResource_strategy)
@settings(max_examples=50)
def test_swconcurrentresource_instantiation(instance):
    assert isinstance(instance, SwConcurrentResource)

@given(instance=MARTE_SW_Concurrency_InterruptResource_strategy)
@settings(max_examples=50)
def test_marte_sw_concurrency_interruptresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_InterruptResource)



@given(instance=MARTE_SW_Concurrency_InterruptResource_strategy)
def test_marte_sw_concurrency_interruptresource_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=MARTE_SW_Concurrency_InterruptResource_strategy)
def test_marte_sw_concurrency_interruptresource_isMaskable_setter(instance):
    original = instance.isMaskable
    instance.isMaskable = original
    assert instance.isMaskable == original

@given(instance=SW_Concurrency_MARTE_Element_strategy)
@settings(max_examples=50)
def test_sw_concurrency_marte_element_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_Element)

@given(instance=SwResource_strategy)
@settings(max_examples=50)
def test_swresource_instantiation(instance):
    assert isinstance(instance, SwResource)

@given(instance=MARTE_SW_Interaction_SwInteractionResource_strategy)
@settings(max_examples=50)
def test_marte_sw_interaction_swinteractionresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_SwInteractionResource)



@given(instance=MARTE_SW_Interaction_SwInteractionResource_strategy)
def test_marte_sw_interaction_swinteractionresource_waitingQueuePolicy_setter(instance):
    original = instance.waitingQueuePolicy
    instance.waitingQueuePolicy = original
    assert instance.waitingQueuePolicy == original



@given(instance=MARTE_SW_Interaction_SwInteractionResource_strategy)
def test_marte_sw_interaction_swinteractionresource_waitingQueueCapacity_setter(instance):
    original = instance.waitingQueueCapacity
    instance.waitingQueueCapacity = original
    assert instance.waitingQueueCapacity == original



@given(instance=MARTE_SW_Interaction_SwInteractionResource_strategy)
def test_marte_sw_interaction_swinteractionresource_isIntraMemoryPartitionInteraction_setter(instance):
    original = instance.isIntraMemoryPartitionInteraction
    instance.isIntraMemoryPartitionInteraction = original
    assert instance.isIntraMemoryPartitionInteraction == original

@given(instance=MARTE_SW_Brokering_MemoryBroker_strategy)
@settings(max_examples=50)
def test_marte_sw_brokering_memorybroker_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Brokering_MemoryBroker)



@given(instance=MARTE_SW_Brokering_MemoryBroker_strategy)
def test_marte_sw_brokering_memorybroker_accessPolicy_setter(instance):
    original = instance.accessPolicy
    instance.accessPolicy = original
    assert instance.accessPolicy == original

@given(instance=MARTE_SW_Brokering_DeviceBroker_strategy)
@settings(max_examples=50)
def test_marte_sw_brokering_devicebroker_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Brokering_DeviceBroker)



@given(instance=MARTE_SW_Brokering_DeviceBroker_strategy)
def test_marte_sw_brokering_devicebroker_accessPolicy_setter(instance):
    original = instance.accessPolicy
    instance.accessPolicy = original
    assert instance.accessPolicy == original



@given(instance=MARTE_SW_Brokering_DeviceBroker_strategy)
def test_marte_sw_brokering_devicebroker_isBuffered_setter(instance):
    original = instance.isBuffered
    instance.isBuffered = original
    assert instance.isBuffered == original

@given(instance=MARTE_SW_Concurrency_MemoryPartition_strategy)
@settings(max_examples=50)
def test_marte_sw_concurrency_memorypartition_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_MemoryPartition)

@given(instance=MARTE_SW_Concurrency_SwConcurrentResource_strategy)
@settings(max_examples=50)
def test_marte_sw_concurrency_swconcurrentresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_SwConcurrentResource)



@given(instance=MARTE_SW_Concurrency_SwConcurrentResource_strategy)
def test_marte_sw_concurrency_swconcurrentresource_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MARTE_SW_Concurrency_SwConcurrentResource_strategy)
def test_marte_sw_concurrency_swconcurrentresource_activationCapacity_setter(instance):
    original = instance.activationCapacity
    instance.activationCapacity = original
    assert instance.activationCapacity == original

@given(instance=SW_Concurrency_MARTE_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw_concurrency_marte_behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_BehavioralFeature)

@given(instance=SW_ResourceCore_MARTE_Property_strategy)
@settings(max_examples=50)
def test_sw_resourcecore_marte_property_instantiation(instance):
    assert isinstance(instance, SW_ResourceCore_MARTE_Property)

@given(instance=SW_ResourceCore_MARTE_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw_resourcecore_marte_behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW_ResourceCore_MARTE_BehavioralFeature)

@given(instance=SW_ResourceCore_MARTE_TypedElement_strategy)
@settings(max_examples=50)
def test_sw_resourcecore_marte_typedelement_instantiation(instance):
    assert isinstance(instance, SW_ResourceCore_MARTE_TypedElement)

@given(instance=SW_Concurrency_MARTE_TypedElement_strategy)
@settings(max_examples=50)
def test_sw_concurrency_marte_typedelement_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_TypedElement)

@given(instance=HwComponent_strategy)
@settings(max_examples=50)
def test_hwcomponent_instantiation(instance):
    assert isinstance(instance, HwComponent)

@given(instance=MARTE_HwPower_HwCoolingSupply_strategy)
@settings(max_examples=50)
def test_marte_hwpower_hwcoolingsupply_instantiation(instance):
    assert isinstance(instance, MARTE_HwPower_HwCoolingSupply)



@given(instance=MARTE_HwPower_HwCoolingSupply_strategy)
def test_marte_hwpower_hwcoolingsupply_coolingPower_setter(instance):
    original = instance.coolingPower
    instance.coolingPower = original
    assert instance.coolingPower == original

@given(instance=MARTE_HwPower_HwPowerSupply_strategy)
@settings(max_examples=50)
def test_marte_hwpower_hwpowersupply_instantiation(instance):
    assert isinstance(instance, MARTE_HwPower_HwPowerSupply)



@given(instance=MARTE_HwPower_HwPowerSupply_strategy)
def test_marte_hwpower_hwpowersupply_suppliedPower_setter(instance):
    original = instance.suppliedPower
    instance.suppliedPower = original
    assert instance.suppliedPower == original



@given(instance=MARTE_HwPower_HwPowerSupply_strategy)
def test_marte_hwpower_hwpowersupply_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=HwLayout_HwComponent_strategy)
@settings(max_examples=50)
def test_hwlayout_hwcomponent_instantiation(instance):
    assert isinstance(instance, HwLayout_HwComponent)

@given(instance=MARTE_SW_ResourceCore_SwResource_strategy)
@settings(max_examples=50)
def test_marte_sw_resourcecore_swresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_ResourceCore_SwResource)

@given(instance=HwCommunication_HwEndPoint_strategy)
@settings(max_examples=50)
def test_hwcommunication_hwendpoint_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwEndPoint)

@given(instance=HwGeneral_HwResourceService_strategy)
@settings(max_examples=50)
def test_hwgeneral_hwresourceservice_instantiation(instance):
    assert isinstance(instance, HwGeneral_HwResourceService)

@given(instance=MARTE_HwGeneral_HwResource_strategy)
@settings(max_examples=50)
def test_marte_hwgeneral_hwresource_instantiation(instance):
    assert isinstance(instance, MARTE_HwGeneral_HwResource)



@given(instance=MARTE_HwGeneral_HwResource_strategy)
def test_marte_hwgeneral_hwresource_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=MARTE_HwGeneral_HwResource_strategy)
def test_marte_hwgeneral_hwresource_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original

@given(instance=HwI_O_strategy)
@settings(max_examples=50)
def test_hwi_o_instantiation(instance):
    assert isinstance(instance, HwI_O)

@given(instance=MARTE_HwDevice_HWSensor_strategy)
@settings(max_examples=50)
def test_marte_hwdevice_hwsensor_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HWSensor)

@given(instance=MARTE_HwDevice_HWActuator_strategy)
@settings(max_examples=50)
def test_marte_hwdevice_hwactuator_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HWActuator)

@given(instance=HwTiming_HwClock_strategy)
@settings(max_examples=50)
def test_hwtiming_hwclock_instantiation(instance):
    assert isinstance(instance, HwTiming_HwClock)

@given(instance=HwTimingResource_strategy)
@settings(max_examples=50)
def test_hwtimingresource_instantiation(instance):
    assert isinstance(instance, HwTimingResource)

@given(instance=MARTE_HwTiming_HwTimer_strategy)
@settings(max_examples=50)
def test_marte_hwtiming_hwtimer_instantiation(instance):
    assert isinstance(instance, MARTE_HwTiming_HwTimer)



@given(instance=MARTE_HwTiming_HwTimer_strategy)
def test_marte_hwtiming_hwtimer_counterWidth_setter(instance):
    original = instance.counterWidth
    instance.counterWidth = original
    assert instance.counterWidth == original



@given(instance=MARTE_HwTiming_HwTimer_strategy)
def test_marte_hwtiming_hwtimer_nbCounters_setter(instance):
    original = instance.nbCounters
    instance.nbCounters = original
    assert instance.nbCounters == original

@given(instance=MARTE_HwTiming_HwClock_strategy)
@settings(max_examples=50)
def test_marte_hwtiming_hwclock_instantiation(instance):
    assert isinstance(instance, MARTE_HwTiming_HwClock)

@given(instance=GRM_TimingResource_strategy)
@settings(max_examples=50)
def test_grm_timingresource_instantiation(instance):
    assert isinstance(instance, GRM_TimingResource)

@given(instance=HwDevice_strategy)
@settings(max_examples=50)
def test_hwdevice_instantiation(instance):
    assert isinstance(instance, HwDevice)

@given(instance=MARTE_HwDevice_HwSupport_strategy)
@settings(max_examples=50)
def test_marte_hwdevice_hwsupport_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HwSupport)

@given(instance=MARTE_HwDevice_HwI_O_strategy)
@settings(max_examples=50)
def test_marte_hwdevice_hwi_o_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HwI_O)

@given(instance=GRM_DeviceResource_strategy)
@settings(max_examples=50)
def test_grm_deviceresource_instantiation(instance):
    assert isinstance(instance, GRM_DeviceResource)

@given(instance=HwMemory_strategy)
@settings(max_examples=50)
def test_hwmemory_instantiation(instance):
    assert isinstance(instance, HwMemory)

@given(instance=MARTE_HwMemory_HwROM_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_hwrom_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwROM)



@given(instance=MARTE_HwMemory_HwROM_strategy)
def test_marte_hwmemory_hwrom_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MARTE_HwMemory_HwROM_strategy)
def test_marte_hwmemory_hwrom_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=MARTE_HwMemory_HwDrive_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_hwdrive_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwDrive)



@given(instance=MARTE_HwMemory_HwDrive_strategy)
def test_marte_hwmemory_hwdrive_sectorSize_setter(instance):
    original = instance.sectorSize
    instance.sectorSize = original
    assert instance.sectorSize == original

@given(instance=MARTE_HwMemory_HwCache_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_hwcache_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwCache)



@given(instance=MARTE_HwMemory_HwCache_strategy)
def test_marte_hwmemory_hwcache_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MARTE_HwMemory_HwCache_strategy)
def test_marte_hwmemory_hwcache_writePolicy_setter(instance):
    original = instance.writePolicy
    instance.writePolicy = original
    assert instance.writePolicy == original



@given(instance=MARTE_HwMemory_HwCache_strategy)
def test_marte_hwmemory_hwcache_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=MARTE_HwMemory_HwCache_strategy)
def test_marte_hwmemory_hwcache_repl_Policy_setter(instance):
    original = instance.repl_Policy
    instance.repl_Policy = original
    assert instance.repl_Policy == original



@given(instance=MARTE_HwMemory_HwCache_strategy)
def test_marte_hwmemory_hwcache_structure_setter(instance):
    original = instance.structure
    instance.structure = original
    assert instance.structure == original

@given(instance=MARTE_HwMemory_HwRAM_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_hwram_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwRAM)



@given(instance=MARTE_HwMemory_HwRAM_strategy)
def test_marte_hwmemory_hwram_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original



@given(instance=MARTE_HwMemory_HwRAM_strategy)
def test_marte_hwmemory_hwram_writePolicy_setter(instance):
    original = instance.writePolicy
    instance.writePolicy = original
    assert instance.writePolicy == original



@given(instance=MARTE_HwMemory_HwRAM_strategy)
def test_marte_hwmemory_hwram_repl_Policy_setter(instance):
    original = instance.repl_Policy
    instance.repl_Policy = original
    assert instance.repl_Policy == original



@given(instance=MARTE_HwMemory_HwRAM_strategy)
def test_marte_hwmemory_hwram_isNonVolatile_setter(instance):
    original = instance.isNonVolatile
    instance.isNonVolatile = original
    assert instance.isNonVolatile == original



@given(instance=MARTE_HwMemory_HwRAM_strategy)
def test_marte_hwmemory_hwram_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original



@given(instance=MARTE_HwMemory_HwRAM_strategy)
def test_marte_hwmemory_hwram_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=HwComputing_HwProcessor_strategy)
@settings(max_examples=50)
def test_hwcomputing_hwprocessor_instantiation(instance):
    assert isinstance(instance, HwComputing_HwProcessor)

@given(instance=HwStorageManager_HwStorageManager_strategy)
@settings(max_examples=50)
def test_hwstoragemanager_hwstoragemanager_instantiation(instance):
    assert isinstance(instance, HwStorageManager_HwStorageManager)

@given(instance=HwMemory_HwMemory_strategy)
@settings(max_examples=50)
def test_hwmemory_hwmemory_instantiation(instance):
    assert isinstance(instance, HwMemory_HwMemory)

@given(instance=GRM_StorageResource_strategy)
@settings(max_examples=50)
def test_grm_storageresource_instantiation(instance):
    assert isinstance(instance, GRM_StorageResource)

@given(instance=GRM_CommunicationEndPoint_strategy)
@settings(max_examples=50)
def test_grm_communicationendpoint_instantiation(instance):
    assert isinstance(instance, GRM_CommunicationEndPoint)

@given(instance=HwMedia_strategy)
@settings(max_examples=50)
def test_hwmedia_instantiation(instance):
    assert isinstance(instance, HwMedia)

@given(instance=MARTE_HwCommunication_HwBridge_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwbridge_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwBridge)

@given(instance=MARTE_HwCommunication_HwBus_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwbus_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwBus)



@given(instance=MARTE_HwCommunication_HwBus_strategy)
def test_marte_hwcommunication_hwbus_wordWidth_setter(instance):
    original = instance.wordWidth
    instance.wordWidth = original
    assert instance.wordWidth == original



@given(instance=MARTE_HwCommunication_HwBus_strategy)
def test_marte_hwcommunication_hwbus_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original



@given(instance=MARTE_HwCommunication_HwBus_strategy)
def test_marte_hwcommunication_hwbus_adressWidth_setter(instance):
    original = instance.adressWidth
    instance.adressWidth = original
    assert instance.adressWidth == original



@given(instance=MARTE_HwCommunication_HwBus_strategy)
def test_marte_hwcommunication_hwbus_isSerial_setter(instance):
    original = instance.isSerial
    instance.isSerial = original
    assert instance.isSerial == original

@given(instance=HwCommunication_HwArbiter_strategy)
@settings(max_examples=50)
def test_hwcommunication_hwarbiter_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwArbiter)

@given(instance=MARTE_HwStorageManager_HwDMA_strategy)
@settings(max_examples=50)
def test_marte_hwstoragemanager_hwdma_instantiation(instance):
    assert isinstance(instance, MARTE_HwStorageManager_HwDMA)



@given(instance=MARTE_HwStorageManager_HwDMA_strategy)
def test_marte_hwstoragemanager_hwdma_transferWidth_setter(instance):
    original = instance.transferWidth
    instance.transferWidth = original
    assert instance.transferWidth == original



@given(instance=MARTE_HwStorageManager_HwDMA_strategy)
def test_marte_hwstoragemanager_hwdma_nbChannels_setter(instance):
    original = instance.nbChannels
    instance.nbChannels = original
    assert instance.nbChannels == original

@given(instance=HwCommunication_HwCommunicationResource_strategy)
@settings(max_examples=50)
def test_hwcommunication_hwcommunicationresource_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwCommunicationResource)

@given(instance=MARTE_HwCommunication_HwEndPoint_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwendpoint_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwEndPoint)

@given(instance=GRM_CommunicationMedia_strategy)
@settings(max_examples=50)
def test_grm_communicationmedia_instantiation(instance):
    assert isinstance(instance, GRM_CommunicationMedia)

@given(instance=MARTE_GQAM_GaCommHost_strategy)
@settings(max_examples=50)
def test_marte_gqam_gacommhost_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaCommHost)



@given(instance=MARTE_GQAM_GaCommHost_strategy)
def test_marte_gqam_gacommhost_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original



@given(instance=MARTE_GQAM_GaCommHost_strategy)
def test_marte_gqam_gacommhost_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original

@given(instance=MARTE_SW_Interaction_SwCommunicationResource_strategy)
@settings(max_examples=50)
def test_marte_sw_interaction_swcommunicationresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_SwCommunicationResource)

@given(instance=MARTE_HwCommunication_HwMedia_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwmedia_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwMedia)



@given(instance=MARTE_HwCommunication_HwMedia_strategy)
def test_marte_hwcommunication_hwmedia_bandWidth_setter(instance):
    original = instance.bandWidth
    instance.bandWidth = original
    assert instance.bandWidth == original

@given(instance=HwStorageManager_strategy)
@settings(max_examples=50)
def test_hwstoragemanager_instantiation(instance):
    assert isinstance(instance, HwStorageManager)

@given(instance=MARTE_HwStorageManager_HwMMU_strategy)
@settings(max_examples=50)
def test_marte_hwstoragemanager_hwmmu_instantiation(instance):
    assert isinstance(instance, MARTE_HwStorageManager_HwMMU)



@given(instance=MARTE_HwStorageManager_HwMMU_strategy)
def test_marte_hwstoragemanager_hwmmu_nbEntries_setter(instance):
    original = instance.nbEntries
    instance.nbEntries = original
    assert instance.nbEntries == original



@given(instance=MARTE_HwStorageManager_HwMMU_strategy)
def test_marte_hwstoragemanager_hwmmu_physicalAddrSpace_setter(instance):
    original = instance.physicalAddrSpace
    instance.physicalAddrSpace = original
    assert instance.physicalAddrSpace == original



@given(instance=MARTE_HwStorageManager_HwMMU_strategy)
def test_marte_hwstoragemanager_hwmmu_memoryProtection_setter(instance):
    original = instance.memoryProtection
    instance.memoryProtection = original
    assert instance.memoryProtection == original



@given(instance=MARTE_HwStorageManager_HwMMU_strategy)
def test_marte_hwstoragemanager_hwmmu_virtualAddrSpace_setter(instance):
    original = instance.virtualAddrSpace
    instance.virtualAddrSpace = original
    assert instance.virtualAddrSpace == original

@given(instance=HwComputing_HwComputingResource_strategy)
@settings(max_examples=50)
def test_hwcomputing_hwcomputingresource_instantiation(instance):
    assert isinstance(instance, HwComputing_HwComputingResource)

@given(instance=HwMemory_HwRAM_strategy)
@settings(max_examples=50)
def test_hwmemory_hwram_instantiation(instance):
    assert isinstance(instance, HwMemory_HwRAM)

@given(instance=HwResource_strategy)
@settings(max_examples=50)
def test_hwresource_instantiation(instance):
    assert isinstance(instance, HwResource)

@given(instance=MARTE_HwComputing_HwBranchPredictor_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwbranchpredictor_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwBranchPredictor)

@given(instance=MARTE_HwLayout_HwComponent_strategy)
@settings(max_examples=50)
def test_marte_hwlayout_hwcomponent_instantiation(instance):
    assert isinstance(instance, MARTE_HwLayout_HwComponent)



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_nbPins_setter(instance):
    original = instance.nbPins
    instance.nbPins = original
    assert instance.nbPins == original



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_staticDissipation_setter(instance):
    original = instance.staticDissipation
    instance.staticDissipation = original
    assert instance.staticDissipation == original



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_area_setter(instance):
    original = instance.area
    instance.area = original
    assert instance.area == original



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_grid_setter(instance):
    original = instance.grid
    instance.grid = original
    assert instance.grid == original



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_dimensions_setter(instance):
    original = instance.dimensions
    instance.dimensions = original
    assert instance.dimensions == original



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_staticConsumption_setter(instance):
    original = instance.staticConsumption
    instance.staticConsumption = original
    assert instance.staticConsumption == original



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_r_Conditions_setter(instance):
    original = instance.r_Conditions
    instance.r_Conditions = original
    assert instance.r_Conditions == original



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MARTE_HwCommunication_HwCommunicationResource_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwcommunicationresource_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwCommunicationResource)

@given(instance=MARTE_HwComputing_HwISA_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwisa_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwISA)



@given(instance=MARTE_HwComputing_HwISA_strategy)
def test_marte_hwcomputing_hwisa_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original



@given(instance=MARTE_HwComputing_HwISA_strategy)
def test_marte_hwcomputing_hwisa_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MARTE_HwComputing_HwISA_strategy)
def test_marte_hwcomputing_hwisa_inst_Width_setter(instance):
    original = instance.inst_Width
    instance.inst_Width = original
    assert instance.inst_Width == original

@given(instance=HwGeneral_HwResource_strategy)
@settings(max_examples=50)
def test_hwgeneral_hwresource_instantiation(instance):
    assert isinstance(instance, HwGeneral_HwResource)

@given(instance=MARTE_HwMemory_HwMemory_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_hwmemory_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwMemory)



@given(instance=MARTE_HwMemory_HwMemory_strategy)
def test_marte_hwmemory_hwmemory_adressSize_setter(instance):
    original = instance.adressSize
    instance.adressSize = original
    assert instance.adressSize == original



@given(instance=MARTE_HwMemory_HwMemory_strategy)
def test_marte_hwmemory_hwmemory_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original



@given(instance=MARTE_HwMemory_HwMemory_strategy)
def test_marte_hwmemory_hwmemory_timings_setter(instance):
    original = instance.timings
    instance.timings = original
    assert instance.timings == original



@given(instance=MARTE_HwMemory_HwMemory_strategy)
def test_marte_hwmemory_hwmemory_memorySize_setter(instance):
    original = instance.memorySize
    instance.memorySize = original
    assert instance.memorySize == original

@given(instance=MARTE_HwStorageManager_HwStorageManager_strategy)
@settings(max_examples=50)
def test_marte_hwstoragemanager_hwstoragemanager_instantiation(instance):
    assert isinstance(instance, MARTE_HwStorageManager_HwStorageManager)

@given(instance=MARTE_HwDevice_HwDevice_strategy)
@settings(max_examples=50)
def test_marte_hwdevice_hwdevice_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HwDevice)

@given(instance=MARTE_HwTiming_HwTimingResource_strategy)
@settings(max_examples=50)
def test_marte_hwtiming_hwtimingresource_instantiation(instance):
    assert isinstance(instance, MARTE_HwTiming_HwTimingResource)

@given(instance=MARTE_HwComputing_HwComputingResource_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwcomputingresource_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwComputingResource)



@given(instance=MARTE_HwComputing_HwComputingResource_strategy)
def test_marte_hwcomputing_hwcomputingresource_op_Frequencies_setter(instance):
    original = instance.op_Frequencies
    instance.op_Frequencies = original
    assert instance.op_Frequencies == original

@given(instance=HwCommunication_HwMedia_strategy)
@settings(max_examples=50)
def test_hwcommunication_hwmedia_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwMedia)

@given(instance=HwCommunicationResource_strategy)
@settings(max_examples=50)
def test_hwcommunicationresource_instantiation(instance):
    assert isinstance(instance, HwCommunicationResource)

@given(instance=MARTE_HwCommunication_HwArbiter_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwarbiter_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwArbiter)

@given(instance=HwMemory_HwCache_strategy)
@settings(max_examples=50)
def test_hwmemory_hwcache_instantiation(instance):
    assert isinstance(instance, HwMemory_HwCache)

@given(instance=HwComputing_HwBranchPredictor_strategy)
@settings(max_examples=50)
def test_hwcomputing_hwbranchpredictor_instantiation(instance):
    assert isinstance(instance, HwComputing_HwBranchPredictor)

@given(instance=HwComputing_HwISA_strategy)
@settings(max_examples=50)
def test_hwcomputing_hwisa_instantiation(instance):
    assert isinstance(instance, HwComputing_HwISA)

@given(instance=HwComputingResource_strategy)
@settings(max_examples=50)
def test_hwcomputingresource_instantiation(instance):
    assert isinstance(instance, HwComputingResource)

@given(instance=MARTE_HwComputing_HwPLD_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwpld_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwPLD)



@given(instance=MARTE_HwComputing_HwPLD_strategy)
def test_marte_hwcomputing_hwpld_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original



@given(instance=MARTE_HwComputing_HwPLD_strategy)
def test_marte_hwcomputing_hwpld_nbFlipFlops_setter(instance):
    original = instance.nbFlipFlops
    instance.nbFlipFlops = original
    assert instance.nbFlipFlops == original



@given(instance=MARTE_HwComputing_HwPLD_strategy)
def test_marte_hwcomputing_hwpld_technology_setter(instance):
    original = instance.technology
    instance.technology = original
    assert instance.technology == original



@given(instance=MARTE_HwComputing_HwPLD_strategy)
def test_marte_hwcomputing_hwpld_nbLUTs_setter(instance):
    original = instance.nbLUTs
    instance.nbLUTs = original
    assert instance.nbLUTs == original



@given(instance=MARTE_HwComputing_HwPLD_strategy)
def test_marte_hwcomputing_hwpld_ndLUT_Inputs_setter(instance):
    original = instance.ndLUT_Inputs
    instance.ndLUT_Inputs = original
    assert instance.ndLUT_Inputs == original

@given(instance=MARTE_HwComputing_HwASIC_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwasic_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwASIC)

@given(instance=MARTE_HwComputing_HwProcessor_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwprocessor_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwProcessor)



@given(instance=MARTE_HwComputing_HwProcessor_strategy)
def test_marte_hwcomputing_hwprocessor_ipc_setter(instance):
    original = instance.ipc
    instance.ipc = original
    assert instance.ipc == original



@given(instance=MARTE_HwComputing_HwProcessor_strategy)
def test_marte_hwcomputing_hwprocessor_nbStages_setter(instance):
    original = instance.nbStages
    instance.nbStages = original
    assert instance.nbStages == original



@given(instance=MARTE_HwComputing_HwProcessor_strategy)
def test_marte_hwcomputing_hwprocessor_nbALUs_setter(instance):
    original = instance.nbALUs
    instance.nbALUs = original
    assert instance.nbALUs == original



@given(instance=MARTE_HwComputing_HwProcessor_strategy)
def test_marte_hwcomputing_hwprocessor_mips_setter(instance):
    original = instance.mips
    instance.mips = original
    assert instance.mips == original



@given(instance=MARTE_HwComputing_HwProcessor_strategy)
def test_marte_hwcomputing_hwprocessor_nbCores_setter(instance):
    original = instance.nbCores
    instance.nbCores = original
    assert instance.nbCores == original



@given(instance=MARTE_HwComputing_HwProcessor_strategy)
def test_marte_hwcomputing_hwprocessor_architecture_setter(instance):
    original = instance.architecture
    instance.architecture = original
    assert instance.architecture == original



@given(instance=MARTE_HwComputing_HwProcessor_strategy)
def test_marte_hwcomputing_hwprocessor_nbFPUs_setter(instance):
    original = instance.nbFPUs
    instance.nbFPUs = original
    assert instance.nbFPUs == original



@given(instance=MARTE_HwComputing_HwProcessor_strategy)
def test_marte_hwcomputing_hwprocessor_nbPipelines_setter(instance):
    original = instance.nbPipelines
    instance.nbPipelines = original
    assert instance.nbPipelines == original

@given(instance=HwStorageManager_HwMMU_strategy)
@settings(max_examples=50)
def test_hwstoragemanager_hwmmu_instantiation(instance):
    assert isinstance(instance, HwStorageManager_HwMMU)

@given(instance=MARTE_HLAM_RtService_strategy)
@settings(max_examples=50)
def test_marte_hlam_rtservice_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtService)



@given(instance=MARTE_HLAM_RtService_strategy)
def test_marte_hlam_rtservice_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original



@given(instance=MARTE_HLAM_RtService_strategy)
def test_marte_hlam_rtservice_concPolicy_setter(instance):
    original = instance.concPolicy
    instance.concPolicy = original
    assert instance.concPolicy == original



@given(instance=MARTE_HLAM_RtService_strategy)
def test_marte_hlam_rtservice_synchKind_setter(instance):
    original = instance.synchKind
    instance.synchKind = original
    assert instance.synchKind == original



@given(instance=MARTE_HLAM_RtService_strategy)
def test_marte_hlam_rtservice_exeKind_setter(instance):
    original = instance.exeKind
    instance.exeKind = original
    assert instance.exeKind == original

@given(instance=MARTE_HLAM_RtAction_strategy)
@settings(max_examples=50)
def test_marte_hlam_rtaction_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtAction)



@given(instance=MARTE_HLAM_RtAction_strategy)
def test_marte_hlam_rtaction_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original



@given(instance=MARTE_HLAM_RtAction_strategy)
def test_marte_hlam_rtaction_msgSize_setter(instance):
    original = instance.msgSize
    instance.msgSize = original
    assert instance.msgSize == original



@given(instance=MARTE_HLAM_RtAction_strategy)
def test_marte_hlam_rtaction_synchKind_setter(instance):
    original = instance.synchKind
    instance.synchKind = original
    assert instance.synchKind == original

@given(instance=HLAM_MARTE_Comment_strategy)
@settings(max_examples=50)
def test_hlam_marte_comment_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Comment)

@given(instance=Time_TimedInstantObservation_strategy)
@settings(max_examples=50)
def test_time_timedinstantobservation_instantiation(instance):
    assert isinstance(instance, Time_TimedInstantObservation)

@given(instance=MARTE_HLAM_RtSpecification_strategy)
@settings(max_examples=50)
def test_marte_hlam_rtspecification_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtSpecification)



@given(instance=MARTE_HLAM_RtSpecification_strategy)
def test_marte_hlam_rtspecification_absDl_setter(instance):
    original = instance.absDl
    instance.absDl = original
    assert instance.absDl == original



@given(instance=MARTE_HLAM_RtSpecification_strategy)
def test_marte_hlam_rtspecification_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=MARTE_HLAM_RtSpecification_strategy)
def test_marte_hlam_rtspecification_miss_setter(instance):
    original = instance.miss
    instance.miss = original
    assert instance.miss == original



@given(instance=MARTE_HLAM_RtSpecification_strategy)
def test_marte_hlam_rtspecification_relDl_setter(instance):
    original = instance.relDl
    instance.relDl = original
    assert instance.relDl == original



@given(instance=MARTE_HLAM_RtSpecification_strategy)
def test_marte_hlam_rtspecification_occKind_setter(instance):
    original = instance.occKind
    instance.occKind = original
    assert instance.occKind == original



@given(instance=MARTE_HLAM_RtSpecification_strategy)
def test_marte_hlam_rtspecification_utility_setter(instance):
    original = instance.utility
    instance.utility = original
    assert instance.utility == original



@given(instance=MARTE_HLAM_RtSpecification_strategy)
def test_marte_hlam_rtspecification_rdTime_setter(instance):
    original = instance.rdTime
    instance.rdTime = original
    assert instance.rdTime == original



@given(instance=MARTE_HLAM_RtSpecification_strategy)
def test_marte_hlam_rtspecification_boundDl_setter(instance):
    original = instance.boundDl
    instance.boundDl = original
    assert instance.boundDl == original

@given(instance=HLAM_RtSpecification_strategy)
@settings(max_examples=50)
def test_hlam_rtspecification_instantiation(instance):
    assert isinstance(instance, HLAM_RtSpecification)

@given(instance=HLAM_MARTE_InvocationAction_strategy)
@settings(max_examples=50)
def test_hlam_marte_invocationaction_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_InvocationAction)

@given(instance=HLAM_MARTE_Port_strategy)
@settings(max_examples=50)
def test_hlam_marte_port_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Port)

@given(instance=HLAM_MARTE_Signal_strategy)
@settings(max_examples=50)
def test_hlam_marte_signal_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Signal)

@given(instance=HLAM_MARTE_Message_strategy)
@settings(max_examples=50)
def test_hlam_marte_message_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Message)

@given(instance=HLAM_MARTE_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_hlam_marte_behavioralfeature_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_BehavioralFeature)

@given(instance=MARTE_HLAM_RtFeature_strategy)
@settings(max_examples=50)
def test_marte_hlam_rtfeature_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtFeature)

@given(instance=MARTE_HLAM_PpUnit_strategy)
@settings(max_examples=50)
def test_marte_hlam_ppunit_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_PpUnit)



@given(instance=MARTE_HLAM_PpUnit_strategy)
def test_marte_hlam_ppunit_concPolicy_setter(instance):
    original = instance.concPolicy
    instance.concPolicy = original
    assert instance.concPolicy == original



@given(instance=MARTE_HLAM_PpUnit_strategy)
def test_marte_hlam_ppunit_memorySize_setter(instance):
    original = instance.memorySize
    instance.memorySize = original
    assert instance.memorySize == original

@given(instance=HLAM_MARTE_Operation_strategy)
@settings(max_examples=50)
def test_hlam_marte_operation_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Operation)

@given(instance=HLAM_MARTE_Behavior_strategy)
@settings(max_examples=50)
def test_hlam_marte_behavior_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Behavior)

@given(instance=MARTE_HLAM_RtUnit_strategy)
@settings(max_examples=50)
def test_marte_hlam_rtunit_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtUnit)



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_queueSize_setter(instance):
    original = instance.queueSize
    instance.queueSize = original
    assert instance.queueSize == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_srPoolWaitingTime_setter(instance):
    original = instance.srPoolWaitingTime
    instance.srPoolWaitingTime = original
    assert instance.srPoolWaitingTime == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_srPoolSize_setter(instance):
    original = instance.srPoolSize
    instance.srPoolSize = original
    assert instance.srPoolSize == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_srPoolPolicy_setter(instance):
    original = instance.srPoolPolicy
    instance.srPoolPolicy = original
    assert instance.srPoolPolicy == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_isMain_setter(instance):
    original = instance.isMain
    instance.isMain = original
    assert instance.isMain == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_msgMaxSize_setter(instance):
    original = instance.msgMaxSize
    instance.msgMaxSize = original
    assert instance.msgMaxSize == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_memorySize_setter(instance):
    original = instance.memorySize
    instance.memorySize = original
    assert instance.memorySize == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_queueSchedPolicy_setter(instance):
    original = instance.queueSchedPolicy
    instance.queueSchedPolicy = original
    assert instance.queueSchedPolicy == original

@given(instance=MARTE_DataTypes_TupleType_strategy)
@settings(max_examples=50)
def test_marte_datatypes_tupletype_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_TupleType)

@given(instance=MARTE_DataTypes_ChoiceType_strategy)
@settings(max_examples=50)
def test_marte_datatypes_choicetype_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_ChoiceType)

@given(instance=MARTE_DataTypes_CollectionType_strategy)
@settings(max_examples=50)
def test_marte_datatypes_collectiontype_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_CollectionType)

@given(instance=HLAM_MARTE_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_hlam_marte_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_BehavioredClassifier)

@given(instance=MARTE_DataTypes_IntervalType_strategy)
@settings(max_examples=50)
def test_marte_datatypes_intervaltype_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_IntervalType)

@given(instance=DataTypes_MARTE_DataType_strategy)
@settings(max_examples=50)
def test_datatypes_marte_datatype_instantiation(instance):
    assert isinstance(instance, DataTypes_MARTE_DataType)

@given(instance=MARTE_DataTypes_BoundedSubtype_strategy)
@settings(max_examples=50)
def test_marte_datatypes_boundedsubtype_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_BoundedSubtype)



@given(instance=MARTE_DataTypes_BoundedSubtype_strategy)
def test_marte_datatypes_boundedsubtype_isMaxOpen_setter(instance):
    original = instance.isMaxOpen
    instance.isMaxOpen = original
    assert instance.isMaxOpen == original



@given(instance=MARTE_DataTypes_BoundedSubtype_strategy)
def test_marte_datatypes_boundedsubtype_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=MARTE_DataTypes_BoundedSubtype_strategy)
def test_marte_datatypes_boundedsubtype_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original



@given(instance=MARTE_DataTypes_BoundedSubtype_strategy)
def test_marte_datatypes_boundedsubtype_isMinOpen_setter(instance):
    original = instance.isMinOpen
    instance.isMinOpen = original
    assert instance.isMinOpen == original

@given(instance=Operators_MARTE_Behavior_strategy)
@settings(max_examples=50)
def test_operators_marte_behavior_instantiation(instance):
    assert isinstance(instance, Operators_MARTE_Behavior)

@given(instance=MARTE_Operators_Operator_strategy)
@settings(max_examples=50)
def test_marte_operators_operator_instantiation(instance):
    assert isinstance(instance, MARTE_Operators_Operator)



@given(instance=MARTE_Operators_Operator_strategy)
def test_marte_operators_operator_arity_setter(instance):
    original = instance.arity
    instance.arity = original
    assert instance.arity == original



@given(instance=MARTE_Operators_Operator_strategy)
def test_marte_operators_operator_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=Variables_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_variables_marte_namedelement_instantiation(instance):
    assert isinstance(instance, Variables_MARTE_NamedElement)

@given(instance=MARTE_Variables_ExpressionContext_strategy)
@settings(max_examples=50)
def test_marte_variables_expressioncontext_instantiation(instance):
    assert isinstance(instance, MARTE_Variables_ExpressionContext)

@given(instance=Variables_MARTE_Property_strategy)
@settings(max_examples=50)
def test_variables_marte_property_instantiation(instance):
    assert isinstance(instance, Variables_MARTE_Property)

@given(instance=MARTE_Variables_Var_strategy)
@settings(max_examples=50)
def test_marte_variables_var_instantiation(instance):
    assert isinstance(instance, MARTE_Variables_Var)



@given(instance=MARTE_Variables_Var_strategy)
def test_marte_variables_var_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=RSM_MARTE_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_rsm_marte_multiplicityelement_instantiation(instance):
    assert isinstance(instance, RSM_MARTE_MultiplicityElement)

@given(instance=MARTE_RSM_Shaped_strategy)
@settings(max_examples=50)
def test_marte_rsm_shaped_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_Shaped)



@given(instance=MARTE_RSM_Shaped_strategy)
def test_marte_rsm_shaped_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=DataTypes_MARTE_Property_strategy)
@settings(max_examples=50)
def test_datatypes_marte_property_instantiation(instance):
    assert isinstance(instance, DataTypes_MARTE_Property)

@given(instance=Allocate_strategy)
@settings(max_examples=50)
def test_allocate_instantiation(instance):
    assert isinstance(instance, Allocate)

@given(instance=MARTE_SW_Concurrency_EntryPoint_strategy)
@settings(max_examples=50)
def test_marte_sw_concurrency_entrypoint_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_EntryPoint)



@given(instance=MARTE_SW_Concurrency_EntryPoint_strategy)
def test_marte_sw_concurrency_entrypoint_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original

@given(instance=MARTE_RSM_Distribute_strategy)
@settings(max_examples=50)
def test_marte_rsm_distribute_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_Distribute)



@given(instance=MARTE_RSM_Distribute_strategy)
def test_marte_rsm_distribute_toTiler_setter(instance):
    original = instance.toTiler
    instance.toTiler = original
    assert instance.toTiler == original



@given(instance=MARTE_RSM_Distribute_strategy)
def test_marte_rsm_distribute_repetitionSpace_setter(instance):
    original = instance.repetitionSpace
    instance.repetitionSpace = original
    assert instance.repetitionSpace == original



@given(instance=MARTE_RSM_Distribute_strategy)
def test_marte_rsm_distribute_patternShape_setter(instance):
    original = instance.patternShape
    instance.patternShape = original
    assert instance.patternShape == original



@given(instance=MARTE_RSM_Distribute_strategy)
def test_marte_rsm_distribute_fromTiler_setter(instance):
    original = instance.fromTiler
    instance.fromTiler = original
    assert instance.fromTiler == original

@given(instance=LinkTopology_strategy)
@settings(max_examples=50)
def test_linktopology_instantiation(instance):
    assert isinstance(instance, LinkTopology)

@given(instance=MARTE_RSM_Tiler_strategy)
@settings(max_examples=50)
def test_marte_rsm_tiler_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_Tiler)



@given(instance=MARTE_RSM_Tiler_strategy)
def test_marte_rsm_tiler_origin_setter(instance):
    original = instance.origin
    instance.origin = original
    assert instance.origin == original



@given(instance=MARTE_RSM_Tiler_strategy)
def test_marte_rsm_tiler_fitting_setter(instance):
    original = instance.fitting
    instance.fitting = original
    assert instance.fitting == original



@given(instance=MARTE_RSM_Tiler_strategy)
def test_marte_rsm_tiler_tiler_setter(instance):
    original = instance.tiler
    instance.tiler = original
    assert instance.tiler == original



@given(instance=MARTE_RSM_Tiler_strategy)
def test_marte_rsm_tiler_paving_setter(instance):
    original = instance.paving
    instance.paving = original
    assert instance.paving == original

@given(instance=MARTE_RSM_InterRepetition_strategy)
@settings(max_examples=50)
def test_marte_rsm_interrepetition_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_InterRepetition)



@given(instance=MARTE_RSM_InterRepetition_strategy)
def test_marte_rsm_interrepetition_isModulo_setter(instance):
    original = instance.isModulo
    instance.isModulo = original
    assert instance.isModulo == original



@given(instance=MARTE_RSM_InterRepetition_strategy)
def test_marte_rsm_interrepetition_repetitionShapeDependence_setter(instance):
    original = instance.repetitionShapeDependence
    instance.repetitionShapeDependence = original
    assert instance.repetitionShapeDependence == original

@given(instance=MARTE_RSM_Reshape_strategy)
@settings(max_examples=50)
def test_marte_rsm_reshape_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_Reshape)



@given(instance=MARTE_RSM_Reshape_strategy)
def test_marte_rsm_reshape_patternShape_setter(instance):
    original = instance.patternShape
    instance.patternShape = original
    assert instance.patternShape == original



@given(instance=MARTE_RSM_Reshape_strategy)
def test_marte_rsm_reshape_repetitonShape_setter(instance):
    original = instance.repetitonShape
    instance.repetitonShape = original
    assert instance.repetitonShape == original

@given(instance=MARTE_RSM_DefaultLink_strategy)
@settings(max_examples=50)
def test_marte_rsm_defaultlink_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_DefaultLink)

@given(instance=RSM_MARTE_Connector_strategy)
@settings(max_examples=50)
def test_rsm_marte_connector_instantiation(instance):
    assert isinstance(instance, RSM_MARTE_Connector)

@given(instance=MARTE_RSM_LinkTopology_strategy)
@settings(max_examples=50)
def test_marte_rsm_linktopology_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_LinkTopology)

@given(instance=GRM_ResourceUsage_strategy)
@settings(max_examples=50)
def test_grm_resourceusage_instantiation(instance):
    assert isinstance(instance, GRM_ResourceUsage)

@given(instance=MARTE_GQAM_GaScenario_strategy)
@settings(max_examples=50)
def test_marte_gqam_gascenario_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaScenario)



@given(instance=MARTE_GQAM_GaScenario_strategy)
def test_marte_gqam_gascenario_utilizationOnHost_setter(instance):
    original = instance.utilizationOnHost
    instance.utilizationOnHost = original
    assert instance.utilizationOnHost == original



@given(instance=MARTE_GQAM_GaScenario_strategy)
def test_marte_gqam_gascenario_hostDemand_setter(instance):
    original = instance.hostDemand
    instance.hostDemand = original
    assert instance.hostDemand == original



@given(instance=MARTE_GQAM_GaScenario_strategy)
def test_marte_gqam_gascenario_utilization_setter(instance):
    original = instance.utilization
    instance.utilization = original
    assert instance.utilization == original



@given(instance=MARTE_GQAM_GaScenario_strategy)
def test_marte_gqam_gascenario_throughput_setter(instance):
    original = instance.throughput
    instance.throughput = original
    assert instance.throughput == original



@given(instance=MARTE_GQAM_GaScenario_strategy)
def test_marte_gqam_gascenario_respT_setter(instance):
    original = instance.respT
    instance.respT = original
    assert instance.respT == original



@given(instance=MARTE_GQAM_GaScenario_strategy)
def test_marte_gqam_gascenario_interOccT_setter(instance):
    original = instance.interOccT
    instance.interOccT = original
    assert instance.interOccT == original



@given(instance=MARTE_GQAM_GaScenario_strategy)
def test_marte_gqam_gascenario_hostDemandOps_setter(instance):
    original = instance.hostDemandOps
    instance.hostDemandOps = original
    assert instance.hostDemandOps == original

@given(instance=GRM_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_grm_marte_namedelement_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_NamedElement)

@given(instance=RSM_MARTE_ConnectorEnd_strategy)
@settings(max_examples=50)
def test_rsm_marte_connectorend_instantiation(instance):
    assert isinstance(instance, RSM_MARTE_ConnectorEnd)

@given(instance=GrService_strategy)
@settings(max_examples=50)
def test_grservice_instantiation(instance):
    assert isinstance(instance, GrService)

@given(instance=MARTE_HwGeneral_HwResourceService_strategy)
@settings(max_examples=50)
def test_marte_hwgeneral_hwresourceservice_instantiation(instance):
    assert isinstance(instance, MARTE_HwGeneral_HwResourceService)



@given(instance=MARTE_HwGeneral_HwResourceService_strategy)
def test_marte_hwgeneral_hwresourceservice_consumption_setter(instance):
    original = instance.consumption
    instance.consumption = original
    assert instance.consumption == original



@given(instance=MARTE_HwGeneral_HwResourceService_strategy)
def test_marte_hwgeneral_hwresourceservice_dissipation_setter(instance):
    original = instance.dissipation
    instance.dissipation = original
    assert instance.dissipation == original

@given(instance=MARTE_SW_ResourceCore_SwAccessService_strategy)
@settings(max_examples=50)
def test_marte_sw_resourcecore_swaccessservice_instantiation(instance):
    assert isinstance(instance, MARTE_SW_ResourceCore_SwAccessService)



@given(instance=MARTE_SW_ResourceCore_SwAccessService_strategy)
def test_marte_sw_resourcecore_swaccessservice_isModifier_setter(instance):
    original = instance.isModifier
    instance.isModifier = original
    assert instance.isModifier == original

@given(instance=MARTE_GRM_Acquire_strategy)
@settings(max_examples=50)
def test_marte_grm_acquire_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_Acquire)



@given(instance=MARTE_GRM_Acquire_strategy)
def test_marte_grm_acquire_isBlocking_setter(instance):
    original = instance.isBlocking
    instance.isBlocking = original
    assert instance.isBlocking == original

@given(instance=MARTE_GRM_Release_strategy)
@settings(max_examples=50)
def test_marte_grm_release_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_Release)

@given(instance=GRM_MARTE_CollaborationUse_strategy)
@settings(max_examples=50)
def test_grm_marte_collaborationuse_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_CollaborationUse)

@given(instance=GRM_MARTE_Collaboration_strategy)
@settings(max_examples=50)
def test_grm_marte_collaboration_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Collaboration)

@given(instance=GRM_MARTE_Behavior_strategy)
@settings(max_examples=50)
def test_grm_marte_behavior_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Behavior)

@given(instance=GRM_MARTE_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_grm_marte_behavioralfeature_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_BehavioralFeature)

@given(instance=GRM_MARTE_ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_grm_marte_executionspecification_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_ExecutionSpecification)

@given(instance=GRM_Resource_strategy)
@settings(max_examples=50)
def test_grm_resource_instantiation(instance):
    assert isinstance(instance, GRM_Resource)

@given(instance=MARTE_GRM_GrService_strategy)
@settings(max_examples=50)
def test_marte_grm_grservice_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_GrService)

@given(instance=TimingResource_strategy)
@settings(max_examples=50)
def test_timingresource_instantiation(instance):
    assert isinstance(instance, TimingResource)

@given(instance=MARTE_GRM_TimerResource_strategy)
@settings(max_examples=50)
def test_marte_grm_timerresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_TimerResource)



@given(instance=MARTE_GRM_TimerResource_strategy)
def test_marte_grm_timerresource_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=MARTE_GRM_TimerResource_strategy)
def test_marte_grm_timerresource_isPeriodic_setter(instance):
    original = instance.isPeriodic
    instance.isPeriodic = original
    assert instance.isPeriodic == original

@given(instance=MARTE_GRM_ClockResource_strategy)
@settings(max_examples=50)
def test_marte_grm_clockresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ClockResource)

@given(instance=MARTE_GRM_TimingResource_strategy)
@settings(max_examples=50)
def test_marte_grm_timingresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_TimingResource)

@given(instance=MARTE_GRM_DeviceResource_strategy)
@settings(max_examples=50)
def test_marte_grm_deviceresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_DeviceResource)

@given(instance=MARTE_GRM_ResourceUsage_strategy)
@settings(max_examples=50)
def test_marte_grm_resourceusage_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ResourceUsage)



@given(instance=MARTE_GRM_ResourceUsage_strategy)
def test_marte_grm_resourceusage_usedMemory_setter(instance):
    original = instance.usedMemory
    instance.usedMemory = original
    assert instance.usedMemory == original



@given(instance=MARTE_GRM_ResourceUsage_strategy)
def test_marte_grm_resourceusage_energy_setter(instance):
    original = instance.energy
    instance.energy = original
    assert instance.energy == original



@given(instance=MARTE_GRM_ResourceUsage_strategy)
def test_marte_grm_resourceusage_msgSize_setter(instance):
    original = instance.msgSize
    instance.msgSize = original
    assert instance.msgSize == original



@given(instance=MARTE_GRM_ResourceUsage_strategy)
def test_marte_grm_resourceusage_execTime_setter(instance):
    original = instance.execTime
    instance.execTime = original
    assert instance.execTime == original



@given(instance=MARTE_GRM_ResourceUsage_strategy)
def test_marte_grm_resourceusage_allocatedMemory_setter(instance):
    original = instance.allocatedMemory
    instance.allocatedMemory = original
    assert instance.allocatedMemory == original



@given(instance=MARTE_GRM_ResourceUsage_strategy)
def test_marte_grm_resourceusage_powerPeak_setter(instance):
    original = instance.powerPeak
    instance.powerPeak = original
    assert instance.powerPeak == original

@given(instance=GRM_MARTE_Connector_strategy)
@settings(max_examples=50)
def test_grm_marte_connector_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Connector)

@given(instance=MARTE_GRM_CommunicationMedia_strategy)
@settings(max_examples=50)
def test_marte_grm_communicationmedia_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_CommunicationMedia)



@given(instance=MARTE_GRM_CommunicationMedia_strategy)
def test_marte_grm_communicationmedia_packetT_setter(instance):
    original = instance.packetT
    instance.packetT = original
    assert instance.packetT == original



@given(instance=MARTE_GRM_CommunicationMedia_strategy)
def test_marte_grm_communicationmedia_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=MARTE_GRM_CommunicationMedia_strategy)
def test_marte_grm_communicationmedia_transmMode_setter(instance):
    original = instance.transmMode
    instance.transmMode = original
    assert instance.transmMode == original



@given(instance=MARTE_GRM_CommunicationMedia_strategy)
def test_marte_grm_communicationmedia_elementSize_setter(instance):
    original = instance.elementSize
    instance.elementSize = original
    assert instance.elementSize == original



@given(instance=MARTE_GRM_CommunicationMedia_strategy)
def test_marte_grm_communicationmedia_blockT_setter(instance):
    original = instance.blockT
    instance.blockT = original
    assert instance.blockT == original

@given(instance=Scheduler_strategy)
@settings(max_examples=50)
def test_scheduler_instantiation(instance):
    assert isinstance(instance, Scheduler)

@given(instance=MARTE_GRM_SecondaryScheduler_strategy)
@settings(max_examples=50)
def test_marte_grm_secondaryscheduler_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_SecondaryScheduler)

@given(instance=MARTE_Alloc_Allocated_strategy)
@settings(max_examples=50)
def test_marte_alloc_allocated_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_Allocated)



@given(instance=MARTE_Alloc_Allocated_strategy)
def test_marte_alloc_allocated_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CoreElements_MARTE_State_strategy)
@settings(max_examples=50)
def test_coreelements_marte_state_instantiation(instance):
    assert isinstance(instance, CoreElements_MARTE_State)

@given(instance=MARTE_CoreElements_Mode_strategy)
@settings(max_examples=50)
def test_marte_coreelements_mode_instantiation(instance):
    assert isinstance(instance, MARTE_CoreElements_Mode)

@given(instance=CoreElements_MARTE_Package_strategy)
@settings(max_examples=50)
def test_coreelements_marte_package_instantiation(instance):
    assert isinstance(instance, CoreElements_MARTE_Package)

@given(instance=CoreElements_MARTE_StructuredClassifier_strategy)
@settings(max_examples=50)
def test_coreelements_marte_structuredclassifier_instantiation(instance):
    assert isinstance(instance, CoreElements_MARTE_StructuredClassifier)

@given(instance=MARTE_CoreElements_Configuration_strategy)
@settings(max_examples=50)
def test_marte_coreelements_configuration_instantiation(instance):
    assert isinstance(instance, MARTE_CoreElements_Configuration)

@given(instance=CoreElements_MARTE_StateMachine_strategy)
@settings(max_examples=50)
def test_coreelements_marte_statemachine_instantiation(instance):
    assert isinstance(instance, CoreElements_MARTE_StateMachine)

@given(instance=MARTE_CoreElements_ModeBehavior_strategy)
@settings(max_examples=50)
def test_marte_coreelements_modebehavior_instantiation(instance):
    assert isinstance(instance, MARTE_CoreElements_ModeBehavior)

@given(instance=CoreElements_MARTE_Transition_strategy)
@settings(max_examples=50)
def test_coreelements_marte_transition_instantiation(instance):
    assert isinstance(instance, CoreElements_MARTE_Transition)

@given(instance=MARTE_CoreElements_ModeTransition_strategy)
@settings(max_examples=50)
def test_marte_coreelements_modetransition_instantiation(instance):
    assert isinstance(instance, MARTE_CoreElements_ModeTransition)

@given(instance=NFPs_MARTE_Enumeration_strategy)
@settings(max_examples=50)
def test_nfps_marte_enumeration_instantiation(instance):
    assert isinstance(instance, NFPs_MARTE_Enumeration)

@given(instance=NFPs_Dimension_strategy)
@settings(max_examples=50)
def test_nfps_dimension_instantiation(instance):
    assert isinstance(instance, NFPs_Dimension)

@given(instance=MARTE_NFPs_Dimension_strategy)
@settings(max_examples=50)
def test_marte_nfps_dimension_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_Dimension)



@given(instance=MARTE_NFPs_Dimension_strategy)
def test_marte_nfps_dimension_baseExponent_setter(instance):
    original = instance.baseExponent
    instance.baseExponent = original
    assert instance.baseExponent == original



@given(instance=MARTE_NFPs_Dimension_strategy)
def test_marte_nfps_dimension_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=NFPs_MARTE_Constraint_strategy)
@settings(max_examples=50)
def test_nfps_marte_constraint_instantiation(instance):
    assert isinstance(instance, NFPs_MARTE_Constraint)

@given(instance=MARTE_NFPs_NfpConstraint_strategy)
@settings(max_examples=50)
def test_marte_nfps_nfpconstraint_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_NfpConstraint)



@given(instance=MARTE_NFPs_NfpConstraint_strategy)
def test_marte_nfps_nfpconstraint_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=NFPs_MARTE_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_nfps_marte_enumerationliteral_instantiation(instance):
    assert isinstance(instance, NFPs_MARTE_EnumerationLiteral)

@given(instance=NFPs_Unit_strategy)
@settings(max_examples=50)
def test_nfps_unit_instantiation(instance):
    assert isinstance(instance, NFPs_Unit)

@given(instance=MARTE_NFPs_Unit_strategy)
@settings(max_examples=50)
def test_marte_nfps_unit_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_Unit)



@given(instance=MARTE_NFPs_Unit_strategy)
def test_marte_nfps_unit_convOffset_setter(instance):
    original = instance.convOffset
    instance.convOffset = original
    assert instance.convOffset == original



@given(instance=MARTE_NFPs_Unit_strategy)
def test_marte_nfps_unit_convFactor_setter(instance):
    original = instance.convFactor
    instance.convFactor = original
    assert instance.convFactor == original

@given(instance=NFPs_MARTE_Property_strategy)
@settings(max_examples=50)
def test_nfps_marte_property_instantiation(instance):
    assert isinstance(instance, NFPs_MARTE_Property)

@given(instance=MARTE_NFPs_Nfp_strategy)
@settings(max_examples=50)
def test_marte_nfps_nfp_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_Nfp)
