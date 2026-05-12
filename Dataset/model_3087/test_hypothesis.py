import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PAM_MARTE_NamedElement,
    GQAM_GaCommStep,
    PAM_PaStep,
    MARTE_PAM_PaCommStep,
    MARTE_PAM_PaRunTInstance,
    GaExecHost,
    MARTE_SAM_SaExecHost,
    MutualExclusionResource,
    MARTE_SAM_SaSharedResource,
    GaCommHost,
    MARTE_SAM_SaCommHost,
    SAM_MARTE_BehavioralFeature,
    SAM_SaSharedResource,
    GaAnalysisContext,
    MARTE_SAM_SaAnalysisContext,
    GQAM_MARTE_Classifier,
    GaCommStep,
    MARTE_SAM_SaCommStep,
    SAM_MARTE_NamedElement,
    MARTE_SAM_SaEndtoEndFlow,
    SchedulableResource,
    MARTE_GQAM_GaCommChannel,
    MARTE_GQAM_GaResourcesPlatform,
    GQAM_GaResourcesPlatform,
    GQAM_GaWorkloadBehavior,
    Variables_ExpressionContext,
    CoreElements_Configuration,
    MARTE_GQAM_GaAnalysisContext,
    MARTE_GQAM_GaWorkloadBehavior,
    GaTimedObs,
    MARTE_SAM_SaSchedObs,
    MARTE_GQAM_GaLatencyObs,
    GQAM_MARTE_TimeObservation,
    NfpConstraint,
    MARTE_GQAM_GaTimedObs,
    GQAM_MARTE_Operation,
    GaStep,
    MARTE_GQAM_GaCommStep,
    MARTE_PAM_PaResPassStep,
    MARTE_PAM_PaStep,
    MARTE_SAM_SaStep,
    MARTE_GQAM_GaAcqStep,
    MARTE_GQAM_GaRelStep,
    MARTE_GQAM_GaRequestedService,
    IntegerInterval,
    GaScenario,
    MARTE_GQAM_GaStep,
    GQAM_GaTimedObs,
    GQAM_GaStep,
    GQAM_GaRequestedService,
    MARTE_PAM_PaRequestedStep,
    GQAM_GaExecHost,
    GQAM_GaWorkloadEvent,
    Time_TimedProcessing,
    MARTE_GQAM_GaWorkloadGenerator,
    GCM_MARTE_Behavior,
    GQAM_MARTE_TimeEvent,
    GQAM_GaScenario,
    GQAM_GaEventTrace,
    GQAM_GaWorkloadGenerator,
    MARTE_GQAM_GaWorkloadEvent,
    GQAM_MARTE_NamedElement,
    MARTE_GQAM_GaEventTrace,
    GQAM_MARTE_Behavior,
    MARTE_GCM_FlowSpecification,
    MARTE_GCM_ClientServerSpecification,
    MARTE_GCM_DataPool,
    GCM_MARTE_Classifier,
    GCM_MARTE_AnyReceiveEvent,
    MARTE_GCM_DataEvent,
    GCM_MARTE_InvocationAction,
    MARTE_GCM_GCMInvocationAction,
    GCM_MARTE_Feature,
    GCM_MARTE_Trigger,
    MARTE_GCM_GCMTrigger,
    HwPeripheral_RegisterAction,
    Activity,
    MARTE_HwPeripheral_PeripheralActivity,
    HwPeripheral_MARTE_OutputPin,
    HwPeripheral_MARTE_InputPin,
    RegisterAction,
    MARTE_HwPeripheral_ReadRegisterAction,
    MARTE_HwPeripheral_WriteRegisterAction,
    Action,
    MARTE_HwPeripheral_RegisterAction,
    HwPeripheral_MARTE_Operation,
    Operation,
    MARTE_HwPeripheral_OperationImpl,
    HwIO_HwLine,
    HwPackage_HwPackagePin,
    HwComponent,
    MARTE_HwPower_HwPowerSupply,
    MARTE_HwPower_HwCoolingSupply,
    MARTE_HwLayout_Env_Condition,
    HwLayout_HwComponent,
    HwLayout_Env_Condition,
    NFP_Price,
    Realnterval,
    NFP_Length,
    HwGeneral_MARTE_Activity,
    HwGeneral_MARTE_Operation,
    NFP_Frequency,
    HwCommunication_HwEndPoint,
    HwGeneral_HwResourceService,
    NFP_NaturalInterval,
    NFP_Area,
    HwPeripheral_PeripheralActivity,
    HwPeripheral_OperationImpl,
    HwI_O,
    MARTE_HwDevice_HWSensor,
    MARTE_HwDevice_HWActuator,
    HwDevice,
    MARTE_HwDevice_HwSupport,
    MARTE_HwDevice_HwPeripheral,
    MARTE_HwDevice_HwI_O,
    HwTimingResource,
    MARTE_HwTiming_HwTimer,
    MARTE_HwTiming_HwClock,
    GRM_TimingResource,
    HwMemory_CacheStructure,
    HwDeviceFunction_HwDeviceFunction,
    GRM_DeviceResource,
    HwTiming_HwClock,
    HwMemory_MemoryOrganization,
    HwMemory,
    MARTE_HwMemory_HwCache,
    MARTE_HwMemory_HwDrive,
    MARTE_HwMemory_HwRAM,
    MARTE_HwMemory_MemoryOrganization,
    MARTE_HwMemory_CacheStructure,
    MARTE_HwMemory_HwROM,
    MARTE_HwMemory_Timing,
    HwMemory_Timing,
    HwStorageManager_HwStorageManager,
    HwMemory_HwMemory,
    GRM_StorageResource,
    HwProtocol_HwProtocol,
    HwEndPoint,
    MARTE_HwCommunication_HwPort,
    GRM_CommunicationEndPoint,
    NFP_Boolean,
    HwStorageManager,
    MARTE_HwStorageManager_HwMMU,
    HwCommunication_HwCommunicationResource,
    MARTE_HwCommunication_HwEndPoint,
    GRM_CommunicationMedia,
    MARTE_HwCommunication_HwMedia,
    HwCommunication_HwMedia,
    HwCommunicationResource,
    MARTE_HwCommunication_HwArbiter,
    HwCommunication_HwPort,
    HwIO_HwPin,
    HwPackage_HwPackage,
    HwRegister_HwRegister,
    HwDevice_HwPeripheral,
    HwComputing_HwProcessor,
    HwComputing_HwComputingResource,
    HwMedia,
    MARTE_HwIO_HwLine,
    MARTE_HwCommunication_HwBridge,
    MARTE_HwCommunication_HwConnection,
    MARTE_HwCommunication_HwBus,
    HwCommunication_HwArbiter,
    MARTE_HwStorageManager_HwDMA,
    HwComputing_PLD_Organization,
    NFP_String,
    HwResource,
    MARTE_HwComputing_HwBranchPredictor,
    MARTE_HwCommunication_HwCommunicationResource,
    MARTE_HwLayout_HwComponent,
    MARTE_HwComputing_HwISA,
    NFP_FrequencyInterval,
    HwGeneral_HwResource,
    MARTE_HwTiming_HwTimingResource,
    MARTE_HwMemory_HwMemory,
    MARTE_HwDevice_HwDevice,
    MARTE_HwStorageManager_HwStorageManager,
    HwStorageManager_HwMMU,
    HwMemory_HwCache,
    HwComputing_HwBranchPredictor,
    HwMemory_HwRAM,
    HwComputingResource,
    MARTE_HwComputing_HwMCU,
    MARTE_HwComputing_HwPLD,
    MARTE_HwComputing_HwASIC,
    MARTE_HwComputing_HwProcessor,
    NFP_Natural,
    MARTE_HwComputing_PLD_Organization,
    HwComputing_HwISA,
    MARTE_HLAM_RtService,
    MARTE_HLAM_RtAction,
    NFP_DateTime,
    HLAM_MARTE_Comment,
    NFP_Percentage,
    HLAM_RtSpecification,
    HLAM_MARTE_InvocationAction,
    HLAM_MARTE_Port,
    HLAM_MARTE_Signal,
    HLAM_MARTE_Message,
    HLAM_MARTE_BehavioralFeature,
    MARTE_HLAM_RtFeature,
    MARTE_HLAM_PpUnit,
    Time_TimedInstantObservation,
    ArrivalPattern,
    UtilityType,
    MARTE_HLAM_RtSpecification,
    HLAM_MARTE_Operation,
    HLAM_MARTE_Behavior,
    MARTE_HLAM_RtUnit,
    GCM_MARTE_BehavioralFeature,
    MARTE_GCM_ClientServerFeature,
    GCM_MARTE_Property,
    MARTE_GCM_FlowProperty,
    GCM_ClientServerSpecification,
    GCM_MARTE_Interface,
    MARTE_GCM_ClientServerPort,
    GCM_MARTE_Port,
    MARTE_GCM_FlowPort,
    SwSynchronizationResource,
    MARTE_SW_Interaction_NotificationResource,
    SW_Interaction_SwSynchronizationResource,
    SW_Interaction_MARTE_BehavioralFeature,
    SwCommunicationResource,
    MARTE_SW_Interaction_MessageComResource,
    MARTE_SW_Interaction_SharedDataComResource,
    GRM_SynchronizationResource,
    SW_Interaction_SwInteractionResource,
    MARTE_SW_Interaction_SwSynchronizationResource,
    MARTE_SW_Interaction_SwCommunicationResource,
    SW_Interaction_MARTE_TypedElement,
    SW_Brokering_MARTE_Activity,
    SW_Brokering_MARTE_Operation,
    SW_Brokering_MARTE_BehavioralFeature,
    SW_Brokering_MARTE_TypedElement,
    InterruptResource,
    MARTE_SW_Concurrency_Alarm,
    SW_Concurrency_MARTE_Namespace,
    TimerResource,
    MARTE_SW_Concurrency_SwTimerResource,
    SW_Concurrency_MARTE_NamedElement,
    SW_Concurrency_SwConcurrentResource,
    SwConcurrentResource,
    MARTE_SW_Concurrency_InterruptResource,
    SW_Concurrency_MARTE_TypedElement,
    SW_Concurrency_MARTE_Element,
    SwResource,
    MARTE_SW_Brokering_DeviceBroker,
    MARTE_SW_Concurrency_MemoryPartition,
    MARTE_SW_Interaction_SwInteractionResource,
    MARTE_SW_Brokering_MemoryBroker,
    MARTE_SW_Concurrency_SwConcurrentResource,
    SW_ResourceCore_MARTE_BehavioralFeature,
    SW_ResourceCore_MARTE_TypedElement,
    SW_Concurrency_MARTE_BehavioralFeature,
    SW_Brokering_DeviceBroker,
    MARTE_HwDiagram_SRMDiagram,
    SW_ResourceCore_MARTE_Property,
    HwDiagram_MARTE_DataType,
    MARTE_HwDiagram_HwCircuitDiagram,
    HwCommunication_HwConnection,
    MARTE_HwDiagram_HwHRMDiagram,
    HwPackage_HwWire,
    MARTE_HwPackage_HwPackagePin,
    MARTE_HwPackage_HwPackage,
    MARTE_HwDatasheet_HwDatasheet,
    MARTE_HwRegister_HwRegister,
    MARTE_HwDiagram_HwBlockDiagram,
    HwProtocol_MARTE_Operation,
    MARTE_HwProtocol_HwProtocol,
    MARTE_HwPackage_HwWire,
    MARTE_HwIO_HwPin,
    MARTE_HwDeviceFunction_HwDeviceFunction,
    GRM_MARTE_OpaqueExpression,
    ProcessingResource,
    MARTE_GRM_ComputingResource,
    GRM_MARTE_InstanceSpecification,
    GRM_MARTE_Property,
    NFP_Integer,
    MARTE_GRM_Resource,
    Time_MARTE_Event,
    Time_MARTE_Message,
    Time_MARTE_Behavior,
    Time_MARTE_Action,
    Time_MARTE_TimeEvent,
    Resource,
    MARTE_SW_ResourceCore_SwResource,
    MARTE_GRM_Scheduler,
    MARTE_GRM_SynchronizationResource,
    MARTE_GRM_CommunicationEndPoint,
    MARTE_PAM_PaLogicalResource,
    MARTE_HwGeneral_HwResource,
    MARTE_GRM_ConcurrencyResource,
    MARTE_GRM_MutualExclusionResource,
    MARTE_GRM_StorageResource,
    GRM_MARTE_ConnectableElement,
    GRM_MARTE_Lifeline,
    GRM_MARTE_Classifier,
    TimedObservation,
    MARTE_Time_TimedInstantObservation,
    Time_TimedElement,
    Time_MARTE_ValueSpecification,
    TimedElement,
    MARTE_Time_TimedObservation,
    MARTE_Time_TimedProcessing,
    MARTE_Time_TimedValueSpecification,
    Time_Clock,
    MARTE_Time_TimedElement,
    Time_MARTE_Class,
    MARTE_Time_TimedEvent,
    Time_MARTE_DurationObservation,
    MARTE_Time_TimedDurationObservation,
    Time_MARTE_TimeObservation,
    Time_MARTE_Enumeration,
    MARTE_Time_ClockType,
    Time_MARTE_Property,
    Time_ClockType,
    Time_MARTE_InstanceSpecification,
    MARTE_Time_Clock,
    Time_MARTE_Namespace,
    MARTE_Time_TimedDomain,
    Alloc_MARTE_Abstraction,
    MARTE_Alloc_Allocate,
    Time_MARTE_Operation,
    MARTE_Alloc_Assign,
    NFPs_NfpConstraint,
    MARTE_Time_TimedConstraint,
    MARTE_Time_ClockConstraint,
    Alloc_MARTE_Dependency,
    MARTE_Alloc_NfpRefine,
    Alloc_MARTE_ActivityPartition,
    MARTE_Alloc_AllocateActivityGroup,
    Alloc_Allocated,
    Alloc_MARTE_NamedElement,
    MARTE_Alloc_Allocated,
    CoreElements_MARTE_State,
    MARTE_CoreElements_Mode,
    Alloc_MARTE_Comment,
    Alloc_MARTE_Element,
    CoreElements_MARTE_Transition,
    MARTE_CoreElements_ModeTransition,
    NFPs_MARTE_Enumeration,
    NFPs_Dimension,
    MARTE_NFPs_Dimension,
    TupleType,
    MARTE_NFPs_NfpType,
    CoreElements_Mode,
    NFPs_MARTE_Constraint,
    MARTE_NFPs_NfpConstraint,
    NFPs_MARTE_EnumerationLiteral,
    CoreElements_MARTE_Package,
    CoreElements_MARTE_StructuredClassifier,
    MARTE_CoreElements_Configuration,
    CoreElements_MARTE_StateMachine,
    MARTE_CoreElements_ModeBehavior,
    MARTE_NFPs_Nfp,
    NFPs_Unit,
    MARTE_NFPs_Unit,
    NFPs_MARTE_Property,
    MARTE_DataTypes_TupleType,
    MARTE_DataTypes_ChoiceType,
    HLAM_MARTE_BehavioredClassifier,
    DataTypes_MARTE_Property,
    MARTE_DataTypes_BoundedSubtype,
    Variables_MARTE_NamedElement,
    MARTE_Variables_ExpressionContext,
    Variables_MARTE_Property,
    MARTE_Variables_Var,
    RSM_MARTE_MultiplicityElement,
    MARTE_RSM_Shaped,
    RSM_MARTE_ConnectorEnd,
    MARTE_DataTypes_CollectionType,
    MARTE_DataTypes_IntervalType,
    DataTypes_MARTE_DataType,
    TilerSpecification,
    ShapeSpecification,
    Allocate,
    MARTE_SW_Concurrency_EntryPoint,
    MARTE_RSM_Distribute,
    IntegerVector,
    LinkTopology,
    MARTE_RSM_Reshape,
    MARTE_RSM_InterRepetition,
    MARTE_RSM_DefaultLink,
    RSM_MARTE_Connector,
    MARTE_RSM_LinkTopology,
    IntegerMatrix,
    MARTE_RSM_Tiler,
    NFP_Energy,
    NFP_Power,
    NFP_DataSize,
    MARTE_GRM_ResourceUsage,
    GrService,
    MARTE_SW_ResourceCore_SwAccessService,
    MARTE_GRM_Acquire,
    MARTE_HwGeneral_HwResourceService,
    MARTE_GRM_Release,
    GRM_MARTE_CollaborationUse,
    GRM_MARTE_Collaboration,
    GRM_MARTE_Behavior,
    GRM_MARTE_BehavioralFeature,
    GRM_MARTE_ExecutionSpecification,
    GRM_Resource,
    MARTE_GRM_GrService,
    GRM_ResourceUsage,
    MARTE_GQAM_GaScenario,
    GRM_MARTE_NamedElement,
    MARTE_GRM_DeviceResource,
    NFP_DataTxRate,
    NFP_Duration,
    GRM_MARTE_Connector,
    MARTE_GRM_CommunicationMedia,
    Scheduler,
    MARTE_GRM_SecondaryScheduler,
    GRM_SecondaryScheduler,
    SchedParameters,
    MARTE_GRM_SchedulableResource,
    TimingResource,
    MARTE_GRM_TimerResource,
    MARTE_GRM_ClockResource,
    MARTE_GRM_TimingResource,
    GRM_Scheduler,
    MARTE_GQAM_GaCommHost,
    NFP_Real,
    MARTE_GRM_ProcessingResource,
    GRM_SchedulableResource,
    MARTE_SW_Concurrency_SwSchedulableResource,
    GRM_MutualExclusionResource,
    MARTE_SW_Interaction_SwMutualExclusionResource,
    GRM_ComputingResource,
    MARTE_HwComputing_HwComputingResource,
    MARTE_GQAM_GaExecHost,
    GRM_ProcessingResource,
    ConcurrentAccessProtocolKind,
    PortSpecificationKind,
    ROM_Type,
    PLD_Technology,
    PoolMgtPolicyKind,
    FlowDirectionKind,
    NotificationResourceKind,
    ConditionType,
    PLD_Class,
    ComponentState,
    CallConcurrencyKind,
    ConcurrencyKind,
    ISA_Type,
    LaxityKind,
    WritePolicy,
    SynchronizationKind,
    AllocationEndKind,
    QueuePolicyKind,
    InterruptKind,
    MutualExclusionResourceKind,
    VariableDirectionKind,
    ExecutionKind,
    CacheType,
    AssignmentNature,
    ComponentKind,
    NotificationKind,
    Repl_Policy,
    ConstraintKind,
    AccessPolicyKind,
    AllocationNature,
    AssignmentKind,
    AllocationKind,
    MessageResourceKind,
    DataPoolOrderingKind,
    ClientServerKind,
    OptimallityCriterionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pam_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(PAM_MARTE_NamedElement)


def test_pam_marte_namedelement_constructor_exists():
    assert callable(PAM_MARTE_NamedElement.__init__)


def test_pam_marte_namedelement_constructor_args():
    sig = inspect.signature(PAM_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



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



def test_marte_pam_paruntinstance_is_not_abstract():
    assert not inspect.isabstract(MARTE_PAM_PaRunTInstance)


def test_marte_pam_paruntinstance_constructor_exists():
    assert callable(MARTE_PAM_PaRunTInstance.__init__)


def test_marte_pam_paruntinstance_constructor_args():
    sig = inspect.signature(MARTE_PAM_PaRunTInstance.__init__)
    params = list(sig.parameters.keys())
    assert "unbddPool" in params, "Missing parameter 'unbddPool'"

def test_marte_pam_paruntinstance_has_unbddPool():
    assert hasattr(MARTE_PAM_PaRunTInstance, "unbddPool")
    descriptor = None
    for klass in MARTE_PAM_PaRunTInstance.__mro__:
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



def test_marte_sam_saexechost_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaExecHost)


def test_marte_sam_saexechost_constructor_exists():
    assert callable(MARTE_SAM_SaExecHost.__init__)


def test_marte_sam_saexechost_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaExecHost.__init__)
    params = list(sig.parameters.keys())



def test_mutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(MutualExclusionResource)


def test_mutualexclusionresource_constructor_exists():
    assert callable(MutualExclusionResource.__init__)


def test_mutualexclusionresource_constructor_args():
    sig = inspect.signature(MutualExclusionResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_sam_sasharedresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaSharedResource)


def test_marte_sam_sasharedresource_constructor_exists():
    assert callable(MARTE_SAM_SaSharedResource.__init__)


def test_marte_sam_sasharedresource_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaSharedResource.__init__)
    params = list(sig.parameters.keys())



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



def test_sam_marte_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SAM_MARTE_BehavioralFeature)


def test_sam_marte_behavioralfeature_constructor_exists():
    assert callable(SAM_MARTE_BehavioralFeature.__init__)


def test_sam_marte_behavioralfeature_constructor_args():
    sig = inspect.signature(SAM_MARTE_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_sam_sasharedresource_is_not_abstract():
    assert not inspect.isabstract(SAM_SaSharedResource)


def test_sam_sasharedresource_constructor_exists():
    assert callable(SAM_SaSharedResource.__init__)


def test_sam_sasharedresource_constructor_args():
    sig = inspect.signature(SAM_SaSharedResource.__init__)
    params = list(sig.parameters.keys())



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
    assert "optCriterion" in params, "Missing parameter 'optCriterion'"

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



def test_sam_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(SAM_MARTE_NamedElement)


def test_sam_marte_namedelement_constructor_exists():
    assert callable(SAM_MARTE_NamedElement.__init__)


def test_sam_marte_namedelement_constructor_args():
    sig = inspect.signature(SAM_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte_sam_saendtoendflow_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaEndtoEndFlow)


def test_marte_sam_saendtoendflow_constructor_exists():
    assert callable(MARTE_SAM_SaEndtoEndFlow.__init__)


def test_marte_sam_saendtoendflow_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaEndtoEndFlow.__init__)
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



def test_marte_gqam_gaworkloadbehavior_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaWorkloadBehavior)


def test_marte_gqam_gaworkloadbehavior_constructor_exists():
    assert callable(MARTE_GQAM_GaWorkloadBehavior.__init__)


def test_marte_gqam_gaworkloadbehavior_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaWorkloadBehavior.__init__)
    params = list(sig.parameters.keys())



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



def test_marte_gqam_galatencyobs_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaLatencyObs)


def test_marte_gqam_galatencyobs_constructor_exists():
    assert callable(MARTE_GQAM_GaLatencyObs.__init__)


def test_marte_gqam_galatencyobs_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaLatencyObs.__init__)
    params = list(sig.parameters.keys())



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



def test_marte_gqam_gacommstep_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaCommStep)


def test_marte_gqam_gacommstep_constructor_exists():
    assert callable(MARTE_GQAM_GaCommStep.__init__)


def test_marte_gqam_gacommstep_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaCommStep.__init__)
    params = list(sig.parameters.keys())



def test_marte_pam_parespassstep_is_not_abstract():
    assert not inspect.isabstract(MARTE_PAM_PaResPassStep)


def test_marte_pam_parespassstep_constructor_exists():
    assert callable(MARTE_PAM_PaResPassStep.__init__)


def test_marte_pam_parespassstep_constructor_args():
    sig = inspect.signature(MARTE_PAM_PaResPassStep.__init__)
    params = list(sig.parameters.keys())



def test_marte_pam_pastep_is_not_abstract():
    assert not inspect.isabstract(MARTE_PAM_PaStep)


def test_marte_pam_pastep_constructor_exists():
    assert callable(MARTE_PAM_PaStep.__init__)


def test_marte_pam_pastep_constructor_args():
    sig = inspect.signature(MARTE_PAM_PaStep.__init__)
    params = list(sig.parameters.keys())
    assert "extOpDemand" in params, "Missing parameter 'extOpDemand'"

def test_marte_pam_pastep_has_extOpDemand():
    assert hasattr(MARTE_PAM_PaStep, "extOpDemand")
    descriptor = None
    for klass in MARTE_PAM_PaStep.__mro__:
        if "extOpDemand" in klass.__dict__:
            descriptor = klass.__dict__["extOpDemand"]
            break
    assert isinstance(descriptor, property)



def test_marte_sam_sastep_is_not_abstract():
    assert not inspect.isabstract(MARTE_SAM_SaStep)


def test_marte_sam_sastep_constructor_exists():
    assert callable(MARTE_SAM_SaStep.__init__)


def test_marte_sam_sastep_constructor_args():
    sig = inspect.signature(MARTE_SAM_SaStep.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gaacqstep_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaAcqStep)


def test_marte_gqam_gaacqstep_constructor_exists():
    assert callable(MARTE_GQAM_GaAcqStep.__init__)


def test_marte_gqam_gaacqstep_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaAcqStep.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_garelstep_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaRelStep)


def test_marte_gqam_garelstep_constructor_exists():
    assert callable(MARTE_GQAM_GaRelStep.__init__)


def test_marte_gqam_garelstep_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaRelStep.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_garequestedservice_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaRequestedService)


def test_marte_gqam_garequestedservice_constructor_exists():
    assert callable(MARTE_GQAM_GaRequestedService.__init__)


def test_marte_gqam_garequestedservice_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaRequestedService.__init__)
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



def test_marte_gqam_gastep_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaStep)


def test_marte_gqam_gastep_constructor_exists():
    assert callable(MARTE_GQAM_GaStep.__init__)


def test_marte_gqam_gastep_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaStep.__init__)
    params = list(sig.parameters.keys())



def test_gqam_gatimedobs_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaTimedObs)


def test_gqam_gatimedobs_constructor_exists():
    assert callable(GQAM_GaTimedObs.__init__)


def test_gqam_gatimedobs_constructor_args():
    sig = inspect.signature(GQAM_GaTimedObs.__init__)
    params = list(sig.parameters.keys())



def test_gqam_gastep_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaStep)


def test_gqam_gastep_constructor_exists():
    assert callable(GQAM_GaStep.__init__)


def test_gqam_gastep_constructor_args():
    sig = inspect.signature(GQAM_GaStep.__init__)
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



def test_gqam_gaexechost_is_not_abstract():
    assert not inspect.isabstract(GQAM_GaExecHost)


def test_gqam_gaexechost_constructor_exists():
    assert callable(GQAM_GaExecHost.__init__)


def test_gqam_gaexechost_constructor_args():
    sig = inspect.signature(GQAM_GaExecHost.__init__)
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



def test_marte_gqam_gaworkloadgenerator_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaWorkloadGenerator)


def test_marte_gqam_gaworkloadgenerator_constructor_exists():
    assert callable(MARTE_GQAM_GaWorkloadGenerator.__init__)


def test_marte_gqam_gaworkloadgenerator_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaWorkloadGenerator.__init__)
    params = list(sig.parameters.keys())



def test_gcm_marte_behavior_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_Behavior)


def test_gcm_marte_behavior_constructor_exists():
    assert callable(GCM_MARTE_Behavior.__init__)


def test_gcm_marte_behavior_constructor_args():
    sig = inspect.signature(GCM_MARTE_Behavior.__init__)
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



def test_gqam_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(GQAM_MARTE_NamedElement)


def test_gqam_marte_namedelement_constructor_exists():
    assert callable(GQAM_MARTE_NamedElement.__init__)


def test_gqam_marte_namedelement_constructor_args():
    sig = inspect.signature(GQAM_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gaeventtrace_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaEventTrace)


def test_marte_gqam_gaeventtrace_constructor_exists():
    assert callable(MARTE_GQAM_GaEventTrace.__init__)


def test_marte_gqam_gaeventtrace_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaEventTrace.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"
    assert "location" in params, "Missing parameter 'location'"
    assert "content" in params, "Missing parameter 'content'"

def test_marte_gqam_gaeventtrace_has_format():
    assert hasattr(MARTE_GQAM_GaEventTrace, "format")
    descriptor = None
    for klass in MARTE_GQAM_GaEventTrace.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
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

def test_marte_gqam_gaeventtrace_has_content():
    assert hasattr(MARTE_GQAM_GaEventTrace, "content")
    descriptor = None
    for klass in MARTE_GQAM_GaEventTrace.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_gqam_marte_behavior_is_not_abstract():
    assert not inspect.isabstract(GQAM_MARTE_Behavior)


def test_gqam_marte_behavior_constructor_exists():
    assert callable(GQAM_MARTE_Behavior.__init__)


def test_gqam_marte_behavior_constructor_args():
    sig = inspect.signature(GQAM_MARTE_Behavior.__init__)
    params = list(sig.parameters.keys())



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



def test_hwperipheral_registeraction_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral_RegisterAction)


def test_hwperipheral_registeraction_constructor_exists():
    assert callable(HwPeripheral_RegisterAction.__init__)


def test_hwperipheral_registeraction_constructor_args():
    sig = inspect.signature(HwPeripheral_RegisterAction.__init__)
    params = list(sig.parameters.keys())



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwperipheral_peripheralactivity_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPeripheral_PeripheralActivity)


def test_marte_hwperipheral_peripheralactivity_constructor_exists():
    assert callable(MARTE_HwPeripheral_PeripheralActivity.__init__)


def test_marte_hwperipheral_peripheralactivity_constructor_args():
    sig = inspect.signature(MARTE_HwPeripheral_PeripheralActivity.__init__)
    params = list(sig.parameters.keys())



def test_hwperipheral_marte_outputpin_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral_MARTE_OutputPin)


def test_hwperipheral_marte_outputpin_constructor_exists():
    assert callable(HwPeripheral_MARTE_OutputPin.__init__)


def test_hwperipheral_marte_outputpin_constructor_args():
    sig = inspect.signature(HwPeripheral_MARTE_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_hwperipheral_marte_inputpin_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral_MARTE_InputPin)


def test_hwperipheral_marte_inputpin_constructor_exists():
    assert callable(HwPeripheral_MARTE_InputPin.__init__)


def test_hwperipheral_marte_inputpin_constructor_args():
    sig = inspect.signature(HwPeripheral_MARTE_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_registeraction_is_not_abstract():
    assert not inspect.isabstract(RegisterAction)


def test_registeraction_constructor_exists():
    assert callable(RegisterAction.__init__)


def test_registeraction_constructor_args():
    sig = inspect.signature(RegisterAction.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwperipheral_readregisteraction_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPeripheral_ReadRegisterAction)


def test_marte_hwperipheral_readregisteraction_constructor_exists():
    assert callable(MARTE_HwPeripheral_ReadRegisterAction.__init__)


def test_marte_hwperipheral_readregisteraction_constructor_args():
    sig = inspect.signature(MARTE_HwPeripheral_ReadRegisterAction.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwperipheral_writeregisteraction_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPeripheral_WriteRegisterAction)


def test_marte_hwperipheral_writeregisteraction_constructor_exists():
    assert callable(MARTE_HwPeripheral_WriteRegisterAction.__init__)


def test_marte_hwperipheral_writeregisteraction_constructor_args():
    sig = inspect.signature(MARTE_HwPeripheral_WriteRegisterAction.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwperipheral_registeraction_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPeripheral_RegisterAction)


def test_marte_hwperipheral_registeraction_constructor_exists():
    assert callable(MARTE_HwPeripheral_RegisterAction.__init__)


def test_marte_hwperipheral_registeraction_constructor_args():
    sig = inspect.signature(MARTE_HwPeripheral_RegisterAction.__init__)
    params = list(sig.parameters.keys())



def test_hwperipheral_marte_operation_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral_MARTE_Operation)


def test_hwperipheral_marte_operation_constructor_exists():
    assert callable(HwPeripheral_MARTE_Operation.__init__)


def test_hwperipheral_marte_operation_constructor_args():
    sig = inspect.signature(HwPeripheral_MARTE_Operation.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwperipheral_operationimpl_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPeripheral_OperationImpl)


def test_marte_hwperipheral_operationimpl_constructor_exists():
    assert callable(MARTE_HwPeripheral_OperationImpl.__init__)


def test_marte_hwperipheral_operationimpl_constructor_args():
    sig = inspect.signature(MARTE_HwPeripheral_OperationImpl.__init__)
    params = list(sig.parameters.keys())



def test_hwio_hwline_is_not_abstract():
    assert not inspect.isabstract(HwIO_HwLine)


def test_hwio_hwline_constructor_exists():
    assert callable(HwIO_HwLine.__init__)


def test_hwio_hwline_constructor_args():
    sig = inspect.signature(HwIO_HwLine.__init__)
    params = list(sig.parameters.keys())



def test_hwpackage_hwpackagepin_is_not_abstract():
    assert not inspect.isabstract(HwPackage_HwPackagePin)


def test_hwpackage_hwpackagepin_constructor_exists():
    assert callable(HwPackage_HwPackagePin.__init__)


def test_hwpackage_hwpackagepin_constructor_args():
    sig = inspect.signature(HwPackage_HwPackagePin.__init__)
    params = list(sig.parameters.keys())



def test_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HwComponent)


def test_hwcomponent_constructor_exists():
    assert callable(HwComponent.__init__)


def test_hwcomponent_constructor_args():
    sig = inspect.signature(HwComponent.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwpower_hwpowersupply_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPower_HwPowerSupply)


def test_marte_hwpower_hwpowersupply_constructor_exists():
    assert callable(MARTE_HwPower_HwPowerSupply.__init__)


def test_marte_hwpower_hwpowersupply_constructor_args():
    sig = inspect.signature(MARTE_HwPower_HwPowerSupply.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwpower_hwcoolingsupply_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPower_HwCoolingSupply)


def test_marte_hwpower_hwcoolingsupply_constructor_exists():
    assert callable(MARTE_HwPower_HwCoolingSupply.__init__)


def test_marte_hwpower_hwcoolingsupply_constructor_args():
    sig = inspect.signature(MARTE_HwPower_HwCoolingSupply.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwlayout_env_condition_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwLayout_Env_Condition)


def test_marte_hwlayout_env_condition_constructor_exists():
    assert callable(MARTE_HwLayout_Env_Condition.__init__)


def test_marte_hwlayout_env_condition_constructor_args():
    sig = inspect.signature(MARTE_HwLayout_Env_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "status" in params, "Missing parameter 'status'"

def test_marte_hwlayout_env_condition_has_type():
    assert hasattr(MARTE_HwLayout_Env_Condition, "type")
    descriptor = None
    for klass in MARTE_HwLayout_Env_Condition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwlayout_env_condition_has_status():
    assert hasattr(MARTE_HwLayout_Env_Condition, "status")
    descriptor = None
    for klass in MARTE_HwLayout_Env_Condition.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_hwlayout_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(HwLayout_HwComponent)


def test_hwlayout_hwcomponent_constructor_exists():
    assert callable(HwLayout_HwComponent.__init__)


def test_hwlayout_hwcomponent_constructor_args():
    sig = inspect.signature(HwLayout_HwComponent.__init__)
    params = list(sig.parameters.keys())



def test_hwlayout_env_condition_is_not_abstract():
    assert not inspect.isabstract(HwLayout_Env_Condition)


def test_hwlayout_env_condition_constructor_exists():
    assert callable(HwLayout_Env_Condition.__init__)


def test_hwlayout_env_condition_constructor_args():
    sig = inspect.signature(HwLayout_Env_Condition.__init__)
    params = list(sig.parameters.keys())



def test_nfp_price_is_not_abstract():
    assert not inspect.isabstract(NFP_Price)


def test_nfp_price_constructor_exists():
    assert callable(NFP_Price.__init__)


def test_nfp_price_constructor_args():
    sig = inspect.signature(NFP_Price.__init__)
    params = list(sig.parameters.keys())



def test_realnterval_is_not_abstract():
    assert not inspect.isabstract(Realnterval)


def test_realnterval_constructor_exists():
    assert callable(Realnterval.__init__)


def test_realnterval_constructor_args():
    sig = inspect.signature(Realnterval.__init__)
    params = list(sig.parameters.keys())



def test_nfp_length_is_not_abstract():
    assert not inspect.isabstract(NFP_Length)


def test_nfp_length_constructor_exists():
    assert callable(NFP_Length.__init__)


def test_nfp_length_constructor_args():
    sig = inspect.signature(NFP_Length.__init__)
    params = list(sig.parameters.keys())



def test_hwgeneral_marte_activity_is_not_abstract():
    assert not inspect.isabstract(HwGeneral_MARTE_Activity)


def test_hwgeneral_marte_activity_constructor_exists():
    assert callable(HwGeneral_MARTE_Activity.__init__)


def test_hwgeneral_marte_activity_constructor_args():
    sig = inspect.signature(HwGeneral_MARTE_Activity.__init__)
    params = list(sig.parameters.keys())



def test_hwgeneral_marte_operation_is_not_abstract():
    assert not inspect.isabstract(HwGeneral_MARTE_Operation)


def test_hwgeneral_marte_operation_constructor_exists():
    assert callable(HwGeneral_MARTE_Operation.__init__)


def test_hwgeneral_marte_operation_constructor_args():
    sig = inspect.signature(HwGeneral_MARTE_Operation.__init__)
    params = list(sig.parameters.keys())



def test_nfp_frequency_is_not_abstract():
    assert not inspect.isabstract(NFP_Frequency)


def test_nfp_frequency_constructor_exists():
    assert callable(NFP_Frequency.__init__)


def test_nfp_frequency_constructor_args():
    sig = inspect.signature(NFP_Frequency.__init__)
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



def test_nfp_naturalinterval_is_not_abstract():
    assert not inspect.isabstract(NFP_NaturalInterval)


def test_nfp_naturalinterval_constructor_exists():
    assert callable(NFP_NaturalInterval.__init__)


def test_nfp_naturalinterval_constructor_args():
    sig = inspect.signature(NFP_NaturalInterval.__init__)
    params = list(sig.parameters.keys())



def test_nfp_area_is_not_abstract():
    assert not inspect.isabstract(NFP_Area)


def test_nfp_area_constructor_exists():
    assert callable(NFP_Area.__init__)


def test_nfp_area_constructor_args():
    sig = inspect.signature(NFP_Area.__init__)
    params = list(sig.parameters.keys())



def test_hwperipheral_peripheralactivity_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral_PeripheralActivity)


def test_hwperipheral_peripheralactivity_constructor_exists():
    assert callable(HwPeripheral_PeripheralActivity.__init__)


def test_hwperipheral_peripheralactivity_constructor_args():
    sig = inspect.signature(HwPeripheral_PeripheralActivity.__init__)
    params = list(sig.parameters.keys())



def test_hwperipheral_operationimpl_is_not_abstract():
    assert not inspect.isabstract(HwPeripheral_OperationImpl)


def test_hwperipheral_operationimpl_constructor_exists():
    assert callable(HwPeripheral_OperationImpl.__init__)


def test_hwperipheral_operationimpl_constructor_args():
    sig = inspect.signature(HwPeripheral_OperationImpl.__init__)
    params = list(sig.parameters.keys())



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



def test_marte_hwdevice_hwperipheral_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDevice_HwPeripheral)


def test_marte_hwdevice_hwperipheral_constructor_exists():
    assert callable(MARTE_HwDevice_HwPeripheral.__init__)


def test_marte_hwdevice_hwperipheral_constructor_args():
    sig = inspect.signature(MARTE_HwDevice_HwPeripheral.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwdevice_hwi_o_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDevice_HwI_O)


def test_marte_hwdevice_hwi_o_constructor_exists():
    assert callable(MARTE_HwDevice_HwI_O.__init__)


def test_marte_hwdevice_hwi_o_constructor_args():
    sig = inspect.signature(MARTE_HwDevice_HwI_O.__init__)
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



def test_hwmemory_cachestructure_is_not_abstract():
    assert not inspect.isabstract(HwMemory_CacheStructure)


def test_hwmemory_cachestructure_constructor_exists():
    assert callable(HwMemory_CacheStructure.__init__)


def test_hwmemory_cachestructure_constructor_args():
    sig = inspect.signature(HwMemory_CacheStructure.__init__)
    params = list(sig.parameters.keys())



def test_hwdevicefunction_hwdevicefunction_is_not_abstract():
    assert not inspect.isabstract(HwDeviceFunction_HwDeviceFunction)


def test_hwdevicefunction_hwdevicefunction_constructor_exists():
    assert callable(HwDeviceFunction_HwDeviceFunction.__init__)


def test_hwdevicefunction_hwdevicefunction_constructor_args():
    sig = inspect.signature(HwDeviceFunction_HwDeviceFunction.__init__)
    params = list(sig.parameters.keys())



def test_grm_deviceresource_is_not_abstract():
    assert not inspect.isabstract(GRM_DeviceResource)


def test_grm_deviceresource_constructor_exists():
    assert callable(GRM_DeviceResource.__init__)


def test_grm_deviceresource_constructor_args():
    sig = inspect.signature(GRM_DeviceResource.__init__)
    params = list(sig.parameters.keys())



def test_hwtiming_hwclock_is_not_abstract():
    assert not inspect.isabstract(HwTiming_HwClock)


def test_hwtiming_hwclock_constructor_exists():
    assert callable(HwTiming_HwClock.__init__)


def test_hwtiming_hwclock_constructor_args():
    sig = inspect.signature(HwTiming_HwClock.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory_memoryorganization_is_not_abstract():
    assert not inspect.isabstract(HwMemory_MemoryOrganization)


def test_hwmemory_memoryorganization_constructor_exists():
    assert callable(HwMemory_MemoryOrganization.__init__)


def test_hwmemory_memoryorganization_constructor_args():
    sig = inspect.signature(HwMemory_MemoryOrganization.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory_is_not_abstract():
    assert not inspect.isabstract(HwMemory)


def test_hwmemory_constructor_exists():
    assert callable(HwMemory.__init__)


def test_hwmemory_constructor_args():
    sig = inspect.signature(HwMemory.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwmemory_hwcache_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_HwCache)


def test_marte_hwmemory_hwcache_constructor_exists():
    assert callable(MARTE_HwMemory_HwCache.__init__)


def test_marte_hwmemory_hwcache_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_HwCache.__init__)
    params = list(sig.parameters.keys())
    assert "repl_Policy" in params, "Missing parameter 'repl_Policy'"
    assert "writePolicy" in params, "Missing parameter 'writePolicy'"
    assert "type" in params, "Missing parameter 'type'"

def test_marte_hwmemory_hwcache_has_repl_Policy():
    assert hasattr(MARTE_HwMemory_HwCache, "repl_Policy")
    descriptor = None
    for klass in MARTE_HwMemory_HwCache.__mro__:
        if "repl_Policy" in klass.__dict__:
            descriptor = klass.__dict__["repl_Policy"]
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

def test_marte_hwmemory_hwcache_has_type():
    assert hasattr(MARTE_HwMemory_HwCache, "type")
    descriptor = None
    for klass in MARTE_HwMemory_HwCache.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwmemory_hwdrive_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_HwDrive)


def test_marte_hwmemory_hwdrive_constructor_exists():
    assert callable(MARTE_HwMemory_HwDrive.__init__)


def test_marte_hwmemory_hwdrive_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_HwDrive.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwmemory_hwram_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_HwRAM)


def test_marte_hwmemory_hwram_constructor_exists():
    assert callable(MARTE_HwMemory_HwRAM.__init__)


def test_marte_hwmemory_hwram_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_HwRAM.__init__)
    params = list(sig.parameters.keys())
    assert "repl_Policy" in params, "Missing parameter 'repl_Policy'"
    assert "writePolicy" in params, "Missing parameter 'writePolicy'"

def test_marte_hwmemory_hwram_has_repl_Policy():
    assert hasattr(MARTE_HwMemory_HwRAM, "repl_Policy")
    descriptor = None
    for klass in MARTE_HwMemory_HwRAM.__mro__:
        if "repl_Policy" in klass.__dict__:
            descriptor = klass.__dict__["repl_Policy"]
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



def test_marte_hwmemory_memoryorganization_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_MemoryOrganization)


def test_marte_hwmemory_memoryorganization_constructor_exists():
    assert callable(MARTE_HwMemory_MemoryOrganization.__init__)


def test_marte_hwmemory_memoryorganization_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_MemoryOrganization.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwmemory_cachestructure_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_CacheStructure)


def test_marte_hwmemory_cachestructure_constructor_exists():
    assert callable(MARTE_HwMemory_CacheStructure.__init__)


def test_marte_hwmemory_cachestructure_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_CacheStructure.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwmemory_hwrom_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_HwROM)


def test_marte_hwmemory_hwrom_constructor_exists():
    assert callable(MARTE_HwMemory_HwROM.__init__)


def test_marte_hwmemory_hwrom_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_HwROM.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_marte_hwmemory_hwrom_has_type():
    assert hasattr(MARTE_HwMemory_HwROM, "type")
    descriptor = None
    for klass in MARTE_HwMemory_HwROM.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwmemory_timing_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_Timing)


def test_marte_hwmemory_timing_constructor_exists():
    assert callable(MARTE_HwMemory_Timing.__init__)


def test_marte_hwmemory_timing_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_Timing.__init__)
    params = list(sig.parameters.keys())



def test_hwmemory_timing_is_not_abstract():
    assert not inspect.isabstract(HwMemory_Timing)


def test_hwmemory_timing_constructor_exists():
    assert callable(HwMemory_Timing.__init__)


def test_hwmemory_timing_constructor_args():
    sig = inspect.signature(HwMemory_Timing.__init__)
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



def test_hwprotocol_hwprotocol_is_not_abstract():
    assert not inspect.isabstract(HwProtocol_HwProtocol)


def test_hwprotocol_hwprotocol_constructor_exists():
    assert callable(HwProtocol_HwProtocol.__init__)


def test_hwprotocol_hwprotocol_constructor_args():
    sig = inspect.signature(HwProtocol_HwProtocol.__init__)
    params = list(sig.parameters.keys())



def test_hwendpoint_is_not_abstract():
    assert not inspect.isabstract(HwEndPoint)


def test_hwendpoint_constructor_exists():
    assert callable(HwEndPoint.__init__)


def test_hwendpoint_constructor_args():
    sig = inspect.signature(HwEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcommunication_hwport_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwPort)


def test_marte_hwcommunication_hwport_constructor_exists():
    assert callable(MARTE_HwCommunication_HwPort.__init__)


def test_marte_hwcommunication_hwport_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwPort.__init__)
    params = list(sig.parameters.keys())



def test_grm_communicationendpoint_is_not_abstract():
    assert not inspect.isabstract(GRM_CommunicationEndPoint)


def test_grm_communicationendpoint_constructor_exists():
    assert callable(GRM_CommunicationEndPoint.__init__)


def test_grm_communicationendpoint_constructor_args():
    sig = inspect.signature(GRM_CommunicationEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_nfp_boolean_is_not_abstract():
    assert not inspect.isabstract(NFP_Boolean)


def test_nfp_boolean_constructor_exists():
    assert callable(NFP_Boolean.__init__)


def test_nfp_boolean_constructor_args():
    sig = inspect.signature(NFP_Boolean.__init__)
    params = list(sig.parameters.keys())



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



def test_marte_hwcommunication_hwmedia_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwMedia)


def test_marte_hwcommunication_hwmedia_constructor_exists():
    assert callable(MARTE_HwCommunication_HwMedia.__init__)


def test_marte_hwcommunication_hwmedia_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwMedia.__init__)
    params = list(sig.parameters.keys())



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



def test_hwcommunication_hwport_is_not_abstract():
    assert not inspect.isabstract(HwCommunication_HwPort)


def test_hwcommunication_hwport_constructor_exists():
    assert callable(HwCommunication_HwPort.__init__)


def test_hwcommunication_hwport_constructor_args():
    sig = inspect.signature(HwCommunication_HwPort.__init__)
    params = list(sig.parameters.keys())



def test_hwio_hwpin_is_not_abstract():
    assert not inspect.isabstract(HwIO_HwPin)


def test_hwio_hwpin_constructor_exists():
    assert callable(HwIO_HwPin.__init__)


def test_hwio_hwpin_constructor_args():
    sig = inspect.signature(HwIO_HwPin.__init__)
    params = list(sig.parameters.keys())



def test_hwpackage_hwpackage_is_not_abstract():
    assert not inspect.isabstract(HwPackage_HwPackage)


def test_hwpackage_hwpackage_constructor_exists():
    assert callable(HwPackage_HwPackage.__init__)


def test_hwpackage_hwpackage_constructor_args():
    sig = inspect.signature(HwPackage_HwPackage.__init__)
    params = list(sig.parameters.keys())



def test_hwregister_hwregister_is_not_abstract():
    assert not inspect.isabstract(HwRegister_HwRegister)


def test_hwregister_hwregister_constructor_exists():
    assert callable(HwRegister_HwRegister.__init__)


def test_hwregister_hwregister_constructor_args():
    sig = inspect.signature(HwRegister_HwRegister.__init__)
    params = list(sig.parameters.keys())



def test_hwdevice_hwperipheral_is_not_abstract():
    assert not inspect.isabstract(HwDevice_HwPeripheral)


def test_hwdevice_hwperipheral_constructor_exists():
    assert callable(HwDevice_HwPeripheral.__init__)


def test_hwdevice_hwperipheral_constructor_args():
    sig = inspect.signature(HwDevice_HwPeripheral.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputing_hwprocessor_is_not_abstract():
    assert not inspect.isabstract(HwComputing_HwProcessor)


def test_hwcomputing_hwprocessor_constructor_exists():
    assert callable(HwComputing_HwProcessor.__init__)


def test_hwcomputing_hwprocessor_constructor_args():
    sig = inspect.signature(HwComputing_HwProcessor.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputing_hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(HwComputing_HwComputingResource)


def test_hwcomputing_hwcomputingresource_constructor_exists():
    assert callable(HwComputing_HwComputingResource.__init__)


def test_hwcomputing_hwcomputingresource_constructor_args():
    sig = inspect.signature(HwComputing_HwComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_hwmedia_is_not_abstract():
    assert not inspect.isabstract(HwMedia)


def test_hwmedia_constructor_exists():
    assert callable(HwMedia.__init__)


def test_hwmedia_constructor_args():
    sig = inspect.signature(HwMedia.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwio_hwline_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwIO_HwLine)


def test_marte_hwio_hwline_constructor_exists():
    assert callable(MARTE_HwIO_HwLine.__init__)


def test_marte_hwio_hwline_constructor_args():
    sig = inspect.signature(MARTE_HwIO_HwLine.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcommunication_hwbridge_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwBridge)


def test_marte_hwcommunication_hwbridge_constructor_exists():
    assert callable(MARTE_HwCommunication_HwBridge.__init__)


def test_marte_hwcommunication_hwbridge_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwBridge.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcommunication_hwconnection_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwConnection)


def test_marte_hwcommunication_hwconnection_constructor_exists():
    assert callable(MARTE_HwCommunication_HwConnection.__init__)


def test_marte_hwcommunication_hwconnection_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwConnection.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcommunication_hwbus_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwBus)


def test_marte_hwcommunication_hwbus_constructor_exists():
    assert callable(MARTE_HwCommunication_HwBus.__init__)


def test_marte_hwcommunication_hwbus_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwBus.__init__)
    params = list(sig.parameters.keys())



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



def test_hwcomputing_pld_organization_is_not_abstract():
    assert not inspect.isabstract(HwComputing_PLD_Organization)


def test_hwcomputing_pld_organization_constructor_exists():
    assert callable(HwComputing_PLD_Organization.__init__)


def test_hwcomputing_pld_organization_constructor_args():
    sig = inspect.signature(HwComputing_PLD_Organization.__init__)
    params = list(sig.parameters.keys())



def test_nfp_string_is_not_abstract():
    assert not inspect.isabstract(NFP_String)


def test_nfp_string_constructor_exists():
    assert callable(NFP_String.__init__)


def test_nfp_string_constructor_args():
    sig = inspect.signature(NFP_String.__init__)
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



def test_marte_hwcommunication_hwcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwCommunication_HwCommunicationResource)


def test_marte_hwcommunication_hwcommunicationresource_constructor_exists():
    assert callable(MARTE_HwCommunication_HwCommunicationResource.__init__)


def test_marte_hwcommunication_hwcommunicationresource_constructor_args():
    sig = inspect.signature(MARTE_HwCommunication_HwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwlayout_hwcomponent_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwLayout_HwComponent)


def test_marte_hwlayout_hwcomponent_constructor_exists():
    assert callable(MARTE_HwLayout_HwComponent.__init__)


def test_marte_hwlayout_hwcomponent_constructor_args():
    sig = inspect.signature(MARTE_HwLayout_HwComponent.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte_hwlayout_hwcomponent_has_kind():
    assert hasattr(MARTE_HwLayout_HwComponent, "kind")
    descriptor = None
    for klass in MARTE_HwLayout_HwComponent.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwcomputing_hwisa_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwComputing_HwISA)


def test_marte_hwcomputing_hwisa_constructor_exists():
    assert callable(MARTE_HwComputing_HwISA.__init__)


def test_marte_hwcomputing_hwisa_constructor_args():
    sig = inspect.signature(MARTE_HwComputing_HwISA.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_marte_hwcomputing_hwisa_has_type():
    assert hasattr(MARTE_HwComputing_HwISA, "type")
    descriptor = None
    for klass in MARTE_HwComputing_HwISA.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_nfp_frequencyinterval_is_not_abstract():
    assert not inspect.isabstract(NFP_FrequencyInterval)


def test_nfp_frequencyinterval_constructor_exists():
    assert callable(NFP_FrequencyInterval.__init__)


def test_nfp_frequencyinterval_constructor_args():
    sig = inspect.signature(NFP_FrequencyInterval.__init__)
    params = list(sig.parameters.keys())



def test_hwgeneral_hwresource_is_not_abstract():
    assert not inspect.isabstract(HwGeneral_HwResource)


def test_hwgeneral_hwresource_constructor_exists():
    assert callable(HwGeneral_HwResource.__init__)


def test_hwgeneral_hwresource_constructor_args():
    sig = inspect.signature(HwGeneral_HwResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwtiming_hwtimingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwTiming_HwTimingResource)


def test_marte_hwtiming_hwtimingresource_constructor_exists():
    assert callable(MARTE_HwTiming_HwTimingResource.__init__)


def test_marte_hwtiming_hwtimingresource_constructor_args():
    sig = inspect.signature(MARTE_HwTiming_HwTimingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwmemory_hwmemory_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwMemory_HwMemory)


def test_marte_hwmemory_hwmemory_constructor_exists():
    assert callable(MARTE_HwMemory_HwMemory.__init__)


def test_marte_hwmemory_hwmemory_constructor_args():
    sig = inspect.signature(MARTE_HwMemory_HwMemory.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwdevice_hwdevice_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDevice_HwDevice)


def test_marte_hwdevice_hwdevice_constructor_exists():
    assert callable(MARTE_HwDevice_HwDevice.__init__)


def test_marte_hwdevice_hwdevice_constructor_args():
    sig = inspect.signature(MARTE_HwDevice_HwDevice.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwstoragemanager_hwstoragemanager_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwStorageManager_HwStorageManager)


def test_marte_hwstoragemanager_hwstoragemanager_constructor_exists():
    assert callable(MARTE_HwStorageManager_HwStorageManager.__init__)


def test_marte_hwstoragemanager_hwstoragemanager_constructor_args():
    sig = inspect.signature(MARTE_HwStorageManager_HwStorageManager.__init__)
    params = list(sig.parameters.keys())



def test_hwstoragemanager_hwmmu_is_not_abstract():
    assert not inspect.isabstract(HwStorageManager_HwMMU)


def test_hwstoragemanager_hwmmu_constructor_exists():
    assert callable(HwStorageManager_HwMMU.__init__)


def test_hwstoragemanager_hwmmu_constructor_args():
    sig = inspect.signature(HwStorageManager_HwMMU.__init__)
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



def test_hwmemory_hwram_is_not_abstract():
    assert not inspect.isabstract(HwMemory_HwRAM)


def test_hwmemory_hwram_constructor_exists():
    assert callable(HwMemory_HwRAM.__init__)


def test_hwmemory_hwram_constructor_args():
    sig = inspect.signature(HwMemory_HwRAM.__init__)
    params = list(sig.parameters.keys())



def test_hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(HwComputingResource)


def test_hwcomputingresource_constructor_exists():
    assert callable(HwComputingResource.__init__)


def test_hwcomputingresource_constructor_args():
    sig = inspect.signature(HwComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcomputing_hwmcu_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwComputing_HwMCU)


def test_marte_hwcomputing_hwmcu_constructor_exists():
    assert callable(MARTE_HwComputing_HwMCU.__init__)


def test_marte_hwcomputing_hwmcu_constructor_args():
    sig = inspect.signature(MARTE_HwComputing_HwMCU.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcomputing_hwpld_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwComputing_HwPLD)


def test_marte_hwcomputing_hwpld_constructor_exists():
    assert callable(MARTE_HwComputing_HwPLD.__init__)


def test_marte_hwcomputing_hwpld_constructor_args():
    sig = inspect.signature(MARTE_HwComputing_HwPLD.__init__)
    params = list(sig.parameters.keys())
    assert "technology" in params, "Missing parameter 'technology'"

def test_marte_hwcomputing_hwpld_has_technology():
    assert hasattr(MARTE_HwComputing_HwPLD, "technology")
    descriptor = None
    for klass in MARTE_HwComputing_HwPLD.__mro__:
        if "technology" in klass.__dict__:
            descriptor = klass.__dict__["technology"]
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



def test_nfp_natural_is_not_abstract():
    assert not inspect.isabstract(NFP_Natural)


def test_nfp_natural_constructor_exists():
    assert callable(NFP_Natural.__init__)


def test_nfp_natural_constructor_args():
    sig = inspect.signature(NFP_Natural.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcomputing_pld_organization_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwComputing_PLD_Organization)


def test_marte_hwcomputing_pld_organization_constructor_exists():
    assert callable(MARTE_HwComputing_PLD_Organization.__init__)


def test_marte_hwcomputing_pld_organization_constructor_args():
    sig = inspect.signature(MARTE_HwComputing_PLD_Organization.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"

def test_marte_hwcomputing_pld_organization_has_class_():
    assert hasattr(MARTE_HwComputing_PLD_Organization, "class_")
    descriptor = None
    for klass in MARTE_HwComputing_PLD_Organization.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_hwcomputing_hwisa_is_not_abstract():
    assert not inspect.isabstract(HwComputing_HwISA)


def test_hwcomputing_hwisa_constructor_exists():
    assert callable(HwComputing_HwISA.__init__)


def test_hwcomputing_hwisa_constructor_args():
    sig = inspect.signature(HwComputing_HwISA.__init__)
    params = list(sig.parameters.keys())



def test_marte_hlam_rtservice_is_not_abstract():
    assert not inspect.isabstract(MARTE_HLAM_RtService)


def test_marte_hlam_rtservice_constructor_exists():
    assert callable(MARTE_HLAM_RtService.__init__)


def test_marte_hlam_rtservice_constructor_args():
    sig = inspect.signature(MARTE_HLAM_RtService.__init__)
    params = list(sig.parameters.keys())
    assert "concPolicy" in params, "Missing parameter 'concPolicy'"
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"
    assert "synchKind" in params, "Missing parameter 'synchKind'"
    assert "exeKind" in params, "Missing parameter 'exeKind'"

def test_marte_hlam_rtservice_has_concPolicy():
    assert hasattr(MARTE_HLAM_RtService, "concPolicy")
    descriptor = None
    for klass in MARTE_HLAM_RtService.__mro__:
        if "concPolicy" in klass.__dict__:
            descriptor = klass.__dict__["concPolicy"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtservice_has_isAtomic():
    assert hasattr(MARTE_HLAM_RtService, "isAtomic")
    descriptor = None
    for klass in MARTE_HLAM_RtService.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
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
    assert "synchKind" in params, "Missing parameter 'synchKind'"

def test_marte_hlam_rtaction_has_isAtomic():
    assert hasattr(MARTE_HLAM_RtAction, "isAtomic")
    descriptor = None
    for klass in MARTE_HLAM_RtAction.__mro__:
        if "isAtomic" in klass.__dict__:
            descriptor = klass.__dict__["isAtomic"]
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



def test_nfp_datetime_is_not_abstract():
    assert not inspect.isabstract(NFP_DateTime)


def test_nfp_datetime_constructor_exists():
    assert callable(NFP_DateTime.__init__)


def test_nfp_datetime_constructor_args():
    sig = inspect.signature(NFP_DateTime.__init__)
    params = list(sig.parameters.keys())



def test_hlam_marte_comment_is_not_abstract():
    assert not inspect.isabstract(HLAM_MARTE_Comment)


def test_hlam_marte_comment_constructor_exists():
    assert callable(HLAM_MARTE_Comment.__init__)


def test_hlam_marte_comment_constructor_args():
    sig = inspect.signature(HLAM_MARTE_Comment.__init__)
    params = list(sig.parameters.keys())



def test_nfp_percentage_is_not_abstract():
    assert not inspect.isabstract(NFP_Percentage)


def test_nfp_percentage_constructor_exists():
    assert callable(NFP_Percentage.__init__)


def test_nfp_percentage_constructor_args():
    sig = inspect.signature(NFP_Percentage.__init__)
    params = list(sig.parameters.keys())



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

def test_marte_hlam_ppunit_has_concPolicy():
    assert hasattr(MARTE_HLAM_PpUnit, "concPolicy")
    descriptor = None
    for klass in MARTE_HLAM_PpUnit.__mro__:
        if "concPolicy" in klass.__dict__:
            descriptor = klass.__dict__["concPolicy"]
            break
    assert isinstance(descriptor, property)



def test_time_timedinstantobservation_is_not_abstract():
    assert not inspect.isabstract(Time_TimedInstantObservation)


def test_time_timedinstantobservation_constructor_exists():
    assert callable(Time_TimedInstantObservation.__init__)


def test_time_timedinstantobservation_constructor_args():
    sig = inspect.signature(Time_TimedInstantObservation.__init__)
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



def test_marte_hlam_rtspecification_is_not_abstract():
    assert not inspect.isabstract(MARTE_HLAM_RtSpecification)


def test_marte_hlam_rtspecification_constructor_exists():
    assert callable(MARTE_HLAM_RtSpecification.__init__)


def test_marte_hlam_rtspecification_constructor_args():
    sig = inspect.signature(MARTE_HLAM_RtSpecification.__init__)
    params = list(sig.parameters.keys())



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
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"
    assert "queueSize" in params, "Missing parameter 'queueSize'"
    assert "isMain" in params, "Missing parameter 'isMain'"
    assert "srPoolPolicy" in params, "Missing parameter 'srPoolPolicy'"
    assert "queueSchedPolicy" in params, "Missing parameter 'queueSchedPolicy'"
    assert "srPoolSize" in params, "Missing parameter 'srPoolSize'"

def test_marte_hlam_rtunit_has_isDynamic():
    assert hasattr(MARTE_HLAM_RtUnit, "isDynamic")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "isDynamic" in klass.__dict__:
            descriptor = klass.__dict__["isDynamic"]
            break
    assert isinstance(descriptor, property)

def test_marte_hlam_rtunit_has_queueSize():
    assert hasattr(MARTE_HLAM_RtUnit, "queueSize")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "queueSize" in klass.__dict__:
            descriptor = klass.__dict__["queueSize"]
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

def test_marte_hlam_rtunit_has_srPoolPolicy():
    assert hasattr(MARTE_HLAM_RtUnit, "srPoolPolicy")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "srPoolPolicy" in klass.__dict__:
            descriptor = klass.__dict__["srPoolPolicy"]
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

def test_marte_hlam_rtunit_has_srPoolSize():
    assert hasattr(MARTE_HLAM_RtUnit, "srPoolSize")
    descriptor = None
    for klass in MARTE_HLAM_RtUnit.__mro__:
        if "srPoolSize" in klass.__dict__:
            descriptor = klass.__dict__["srPoolSize"]
            break
    assert isinstance(descriptor, property)



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



def test_gcm_marte_property_is_not_abstract():
    assert not inspect.isabstract(GCM_MARTE_Property)


def test_gcm_marte_property_constructor_exists():
    assert callable(GCM_MARTE_Property.__init__)


def test_gcm_marte_property_constructor_args():
    sig = inspect.signature(GCM_MARTE_Property.__init__)
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
    assert "isConjugated" in params, "Missing parameter 'isConjugated'"
    assert "specificationKind" in params, "Missing parameter 'specificationKind'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte_gcm_clientserverport_has_isConjugated():
    assert hasattr(MARTE_GCM_ClientServerPort, "isConjugated")
    descriptor = None
    for klass in MARTE_GCM_ClientServerPort.__mro__:
        if "isConjugated" in klass.__dict__:
            descriptor = klass.__dict__["isConjugated"]
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

def test_marte_gcm_clientserverport_has_kind():
    assert hasattr(MARTE_GCM_ClientServerPort, "kind")
    descriptor = None
    for klass in MARTE_GCM_ClientServerPort.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
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
    assert "isConjugated" in params, "Missing parameter 'isConjugated'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "isAtomic" in params, "Missing parameter 'isAtomic'"

def test_marte_gcm_flowport_has_isConjugated():
    assert hasattr(MARTE_GCM_FlowPort, "isConjugated")
    descriptor = None
    for klass in MARTE_GCM_FlowPort.__mro__:
        if "isConjugated" in klass.__dict__:
            descriptor = klass.__dict__["isConjugated"]
            break
    assert isinstance(descriptor, property)

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
    assert "mechanism" in params, "Missing parameter 'mechanism'"
    assert "occurence" in params, "Missing parameter 'occurence'"

def test_marte_sw_interaction_notificationresource_has_mechanism():
    assert hasattr(MARTE_SW_Interaction_NotificationResource, "mechanism")
    descriptor = None
    for klass in MARTE_SW_Interaction_NotificationResource.__mro__:
        if "mechanism" in klass.__dict__:
            descriptor = klass.__dict__["mechanism"]
            break
    assert isinstance(descriptor, property)

def test_marte_sw_interaction_notificationresource_has_occurence():
    assert hasattr(MARTE_SW_Interaction_NotificationResource, "occurence")
    descriptor = None
    for klass in MARTE_SW_Interaction_NotificationResource.__mro__:
        if "occurence" in klass.__dict__:
            descriptor = klass.__dict__["occurence"]
            break
    assert isinstance(descriptor, property)



def test_sw_interaction_swsynchronizationresource_is_not_abstract():
    assert not inspect.isabstract(SW_Interaction_SwSynchronizationResource)


def test_sw_interaction_swsynchronizationresource_constructor_exists():
    assert callable(SW_Interaction_SwSynchronizationResource.__init__)


def test_sw_interaction_swsynchronizationresource_constructor_args():
    sig = inspect.signature(SW_Interaction_SwSynchronizationResource.__init__)
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
    assert "mechanism" in params, "Missing parameter 'mechanism'"
    assert "messageQueuePolicy" in params, "Missing parameter 'messageQueuePolicy'"
    assert "isFixedMessageSize" in params, "Missing parameter 'isFixedMessageSize'"

def test_marte_sw_interaction_messagecomresource_has_mechanism():
    assert hasattr(MARTE_SW_Interaction_MessageComResource, "mechanism")
    descriptor = None
    for klass in MARTE_SW_Interaction_MessageComResource.__mro__:
        if "mechanism" in klass.__dict__:
            descriptor = klass.__dict__["mechanism"]
            break
    assert isinstance(descriptor, property)

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



def test_marte_sw_interaction_swcommunicationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Interaction_SwCommunicationResource)


def test_marte_sw_interaction_swcommunicationresource_constructor_exists():
    assert callable(MARTE_SW_Interaction_SwCommunicationResource.__init__)


def test_marte_sw_interaction_swcommunicationresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Interaction_SwCommunicationResource.__init__)
    params = list(sig.parameters.keys())



def test_sw_interaction_marte_typedelement_is_not_abstract():
    assert not inspect.isabstract(SW_Interaction_MARTE_TypedElement)


def test_sw_interaction_marte_typedelement_constructor_exists():
    assert callable(SW_Interaction_MARTE_TypedElement.__init__)


def test_sw_interaction_marte_typedelement_constructor_args():
    sig = inspect.signature(SW_Interaction_MARTE_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_sw_brokering_marte_activity_is_not_abstract():
    assert not inspect.isabstract(SW_Brokering_MARTE_Activity)


def test_sw_brokering_marte_activity_constructor_exists():
    assert callable(SW_Brokering_MARTE_Activity.__init__)


def test_sw_brokering_marte_activity_constructor_args():
    sig = inspect.signature(SW_Brokering_MARTE_Activity.__init__)
    params = list(sig.parameters.keys())



def test_sw_brokering_marte_operation_is_not_abstract():
    assert not inspect.isabstract(SW_Brokering_MARTE_Operation)


def test_sw_brokering_marte_operation_constructor_exists():
    assert callable(SW_Brokering_MARTE_Operation.__init__)


def test_sw_brokering_marte_operation_constructor_args():
    sig = inspect.signature(SW_Brokering_MARTE_Operation.__init__)
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



def test_sw_concurrency_marte_typedelement_is_not_abstract():
    assert not inspect.isabstract(SW_Concurrency_MARTE_TypedElement)


def test_sw_concurrency_marte_typedelement_constructor_exists():
    assert callable(SW_Concurrency_MARTE_TypedElement.__init__)


def test_sw_concurrency_marte_typedelement_constructor_args():
    sig = inspect.signature(SW_Concurrency_MARTE_TypedElement.__init__)
    params = list(sig.parameters.keys())



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



def test_marte_sw_brokering_devicebroker_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Brokering_DeviceBroker)


def test_marte_sw_brokering_devicebroker_constructor_exists():
    assert callable(MARTE_SW_Brokering_DeviceBroker.__init__)


def test_marte_sw_brokering_devicebroker_constructor_args():
    sig = inspect.signature(MARTE_SW_Brokering_DeviceBroker.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accessPolicy" in params, "Missing parameter 'accessPolicy'"
    assert "isBuffered" in params, "Missing parameter 'isBuffered'"

def test_marte_sw_brokering_devicebroker_has_name():
    assert hasattr(MARTE_SW_Brokering_DeviceBroker, "name")
    descriptor = None
    for klass in MARTE_SW_Brokering_DeviceBroker.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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



def test_marte_sw_interaction_swinteractionresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Interaction_SwInteractionResource)


def test_marte_sw_interaction_swinteractionresource_constructor_exists():
    assert callable(MARTE_SW_Interaction_SwInteractionResource.__init__)


def test_marte_sw_interaction_swinteractionresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Interaction_SwInteractionResource.__init__)
    params = list(sig.parameters.keys())
    assert "waitingQueuePolicy" in params, "Missing parameter 'waitingQueuePolicy'"
    assert "isIntraMemoryPartitionInteraction" in params, "Missing parameter 'isIntraMemoryPartitionInteraction'"
    assert "waitingQueueCapacity" in params, "Missing parameter 'waitingQueueCapacity'"

def test_marte_sw_interaction_swinteractionresource_has_waitingQueuePolicy():
    assert hasattr(MARTE_SW_Interaction_SwInteractionResource, "waitingQueuePolicy")
    descriptor = None
    for klass in MARTE_SW_Interaction_SwInteractionResource.__mro__:
        if "waitingQueuePolicy" in klass.__dict__:
            descriptor = klass.__dict__["waitingQueuePolicy"]
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

def test_marte_sw_interaction_swinteractionresource_has_waitingQueueCapacity():
    assert hasattr(MARTE_SW_Interaction_SwInteractionResource, "waitingQueueCapacity")
    descriptor = None
    for klass in MARTE_SW_Interaction_SwInteractionResource.__mro__:
        if "waitingQueueCapacity" in klass.__dict__:
            descriptor = klass.__dict__["waitingQueueCapacity"]
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



def test_marte_sw_concurrency_swconcurrentresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_Concurrency_SwConcurrentResource)


def test_marte_sw_concurrency_swconcurrentresource_constructor_exists():
    assert callable(MARTE_SW_Concurrency_SwConcurrentResource.__init__)


def test_marte_sw_concurrency_swconcurrentresource_constructor_args():
    sig = inspect.signature(MARTE_SW_Concurrency_SwConcurrentResource.__init__)
    params = list(sig.parameters.keys())
    assert "activationCapacity" in params, "Missing parameter 'activationCapacity'"

def test_marte_sw_concurrency_swconcurrentresource_has_activationCapacity():
    assert hasattr(MARTE_SW_Concurrency_SwConcurrentResource, "activationCapacity")
    descriptor = None
    for klass in MARTE_SW_Concurrency_SwConcurrentResource.__mro__:
        if "activationCapacity" in klass.__dict__:
            descriptor = klass.__dict__["activationCapacity"]
            break
    assert isinstance(descriptor, property)



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



def test_sw_concurrency_marte_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(SW_Concurrency_MARTE_BehavioralFeature)


def test_sw_concurrency_marte_behavioralfeature_constructor_exists():
    assert callable(SW_Concurrency_MARTE_BehavioralFeature.__init__)


def test_sw_concurrency_marte_behavioralfeature_constructor_args():
    sig = inspect.signature(SW_Concurrency_MARTE_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_sw_brokering_devicebroker_is_not_abstract():
    assert not inspect.isabstract(SW_Brokering_DeviceBroker)


def test_sw_brokering_devicebroker_constructor_exists():
    assert callable(SW_Brokering_DeviceBroker.__init__)


def test_sw_brokering_devicebroker_constructor_args():
    sig = inspect.signature(SW_Brokering_DeviceBroker.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwdiagram_srmdiagram_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDiagram_SRMDiagram)


def test_marte_hwdiagram_srmdiagram_constructor_exists():
    assert callable(MARTE_HwDiagram_SRMDiagram.__init__)


def test_marte_hwdiagram_srmdiagram_constructor_args():
    sig = inspect.signature(MARTE_HwDiagram_SRMDiagram.__init__)
    params = list(sig.parameters.keys())



def test_sw_resourcecore_marte_property_is_not_abstract():
    assert not inspect.isabstract(SW_ResourceCore_MARTE_Property)


def test_sw_resourcecore_marte_property_constructor_exists():
    assert callable(SW_ResourceCore_MARTE_Property.__init__)


def test_sw_resourcecore_marte_property_constructor_args():
    sig = inspect.signature(SW_ResourceCore_MARTE_Property.__init__)
    params = list(sig.parameters.keys())



def test_hwdiagram_marte_datatype_is_not_abstract():
    assert not inspect.isabstract(HwDiagram_MARTE_DataType)


def test_hwdiagram_marte_datatype_constructor_exists():
    assert callable(HwDiagram_MARTE_DataType.__init__)


def test_hwdiagram_marte_datatype_constructor_args():
    sig = inspect.signature(HwDiagram_MARTE_DataType.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwdiagram_hwcircuitdiagram_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDiagram_HwCircuitDiagram)


def test_marte_hwdiagram_hwcircuitdiagram_constructor_exists():
    assert callable(MARTE_HwDiagram_HwCircuitDiagram.__init__)


def test_marte_hwdiagram_hwcircuitdiagram_constructor_args():
    sig = inspect.signature(MARTE_HwDiagram_HwCircuitDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_marte_hwdiagram_hwcircuitdiagram_has_name():
    assert hasattr(MARTE_HwDiagram_HwCircuitDiagram, "name")
    descriptor = None
    for klass in MARTE_HwDiagram_HwCircuitDiagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hwcommunication_hwconnection_is_not_abstract():
    assert not inspect.isabstract(HwCommunication_HwConnection)


def test_hwcommunication_hwconnection_constructor_exists():
    assert callable(HwCommunication_HwConnection.__init__)


def test_hwcommunication_hwconnection_constructor_args():
    sig = inspect.signature(HwCommunication_HwConnection.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwdiagram_hwhrmdiagram_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDiagram_HwHRMDiagram)


def test_marte_hwdiagram_hwhrmdiagram_constructor_exists():
    assert callable(MARTE_HwDiagram_HwHRMDiagram.__init__)


def test_marte_hwdiagram_hwhrmdiagram_constructor_args():
    sig = inspect.signature(MARTE_HwDiagram_HwHRMDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_marte_hwdiagram_hwhrmdiagram_has_name():
    assert hasattr(MARTE_HwDiagram_HwHRMDiagram, "name")
    descriptor = None
    for klass in MARTE_HwDiagram_HwHRMDiagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hwpackage_hwwire_is_not_abstract():
    assert not inspect.isabstract(HwPackage_HwWire)


def test_hwpackage_hwwire_constructor_exists():
    assert callable(HwPackage_HwWire.__init__)


def test_hwpackage_hwwire_constructor_args():
    sig = inspect.signature(HwPackage_HwWire.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwpackage_hwpackagepin_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPackage_HwPackagePin)


def test_marte_hwpackage_hwpackagepin_constructor_exists():
    assert callable(MARTE_HwPackage_HwPackagePin.__init__)


def test_marte_hwpackage_hwpackagepin_constructor_args():
    sig = inspect.signature(MARTE_HwPackage_HwPackagePin.__init__)
    params = list(sig.parameters.keys())
    assert "altNames" in params, "Missing parameter 'altNames'"
    assert "pinNo" in params, "Missing parameter 'pinNo'"

def test_marte_hwpackage_hwpackagepin_has_altNames():
    assert hasattr(MARTE_HwPackage_HwPackagePin, "altNames")
    descriptor = None
    for klass in MARTE_HwPackage_HwPackagePin.__mro__:
        if "altNames" in klass.__dict__:
            descriptor = klass.__dict__["altNames"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwpackage_hwpackagepin_has_pinNo():
    assert hasattr(MARTE_HwPackage_HwPackagePin, "pinNo")
    descriptor = None
    for klass in MARTE_HwPackage_HwPackagePin.__mro__:
        if "pinNo" in klass.__dict__:
            descriptor = klass.__dict__["pinNo"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwpackage_hwpackage_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPackage_HwPackage)


def test_marte_hwpackage_hwpackage_constructor_exists():
    assert callable(MARTE_HwPackage_HwPackage.__init__)


def test_marte_hwpackage_hwpackage_constructor_args():
    sig = inspect.signature(MARTE_HwPackage_HwPackage.__init__)
    params = list(sig.parameters.keys())
    assert "pinNum" in params, "Missing parameter 'pinNum'"
    assert "name" in params, "Missing parameter 'name'"
    assert "packageType" in params, "Missing parameter 'packageType'"

def test_marte_hwpackage_hwpackage_has_pinNum():
    assert hasattr(MARTE_HwPackage_HwPackage, "pinNum")
    descriptor = None
    for klass in MARTE_HwPackage_HwPackage.__mro__:
        if "pinNum" in klass.__dict__:
            descriptor = klass.__dict__["pinNum"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwpackage_hwpackage_has_name():
    assert hasattr(MARTE_HwPackage_HwPackage, "name")
    descriptor = None
    for klass in MARTE_HwPackage_HwPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwpackage_hwpackage_has_packageType():
    assert hasattr(MARTE_HwPackage_HwPackage, "packageType")
    descriptor = None
    for klass in MARTE_HwPackage_HwPackage.__mro__:
        if "packageType" in klass.__dict__:
            descriptor = klass.__dict__["packageType"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwdatasheet_hwdatasheet_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDatasheet_HwDatasheet)


def test_marte_hwdatasheet_hwdatasheet_constructor_exists():
    assert callable(MARTE_HwDatasheet_HwDatasheet.__init__)


def test_marte_hwdatasheet_hwdatasheet_constructor_args():
    sig = inspect.signature(MARTE_HwDatasheet_HwDatasheet.__init__)
    params = list(sig.parameters.keys())
    assert "revision" in params, "Missing parameter 'revision'"
    assert "name" in params, "Missing parameter 'name'"

def test_marte_hwdatasheet_hwdatasheet_has_revision():
    assert hasattr(MARTE_HwDatasheet_HwDatasheet, "revision")
    descriptor = None
    for klass in MARTE_HwDatasheet_HwDatasheet.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_marte_hwdatasheet_hwdatasheet_has_name():
    assert hasattr(MARTE_HwDatasheet_HwDatasheet, "name")
    descriptor = None
    for klass in MARTE_HwDatasheet_HwDatasheet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwregister_hwregister_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwRegister_HwRegister)


def test_marte_hwregister_hwregister_constructor_exists():
    assert callable(MARTE_HwRegister_HwRegister.__init__)


def test_marte_hwregister_hwregister_constructor_args():
    sig = inspect.signature(MARTE_HwRegister_HwRegister.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_marte_hwregister_hwregister_has_address():
    assert hasattr(MARTE_HwRegister_HwRegister, "address")
    descriptor = None
    for klass in MARTE_HwRegister_HwRegister.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwdiagram_hwblockdiagram_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDiagram_HwBlockDiagram)


def test_marte_hwdiagram_hwblockdiagram_constructor_exists():
    assert callable(MARTE_HwDiagram_HwBlockDiagram.__init__)


def test_marte_hwdiagram_hwblockdiagram_constructor_args():
    sig = inspect.signature(MARTE_HwDiagram_HwBlockDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_marte_hwdiagram_hwblockdiagram_has_name():
    assert hasattr(MARTE_HwDiagram_HwBlockDiagram, "name")
    descriptor = None
    for klass in MARTE_HwDiagram_HwBlockDiagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hwprotocol_marte_operation_is_not_abstract():
    assert not inspect.isabstract(HwProtocol_MARTE_Operation)


def test_hwprotocol_marte_operation_constructor_exists():
    assert callable(HwProtocol_MARTE_Operation.__init__)


def test_hwprotocol_marte_operation_constructor_args():
    sig = inspect.signature(HwProtocol_MARTE_Operation.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwprotocol_hwprotocol_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwProtocol_HwProtocol)


def test_marte_hwprotocol_hwprotocol_constructor_exists():
    assert callable(MARTE_HwProtocol_HwProtocol.__init__)


def test_marte_hwprotocol_hwprotocol_constructor_args():
    sig = inspect.signature(MARTE_HwProtocol_HwProtocol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_marte_hwprotocol_hwprotocol_has_name():
    assert hasattr(MARTE_HwProtocol_HwProtocol, "name")
    descriptor = None
    for klass in MARTE_HwProtocol_HwProtocol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_marte_hwpackage_hwwire_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwPackage_HwWire)


def test_marte_hwpackage_hwwire_constructor_exists():
    assert callable(MARTE_HwPackage_HwWire.__init__)


def test_marte_hwpackage_hwwire_constructor_args():
    sig = inspect.signature(MARTE_HwPackage_HwWire.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwio_hwpin_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwIO_HwPin)


def test_marte_hwio_hwpin_constructor_exists():
    assert callable(MARTE_HwIO_HwPin.__init__)


def test_marte_hwio_hwpin_constructor_args():
    sig = inspect.signature(MARTE_HwIO_HwPin.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwdevicefunction_hwdevicefunction_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwDeviceFunction_HwDeviceFunction)


def test_marte_hwdevicefunction_hwdevicefunction_constructor_exists():
    assert callable(MARTE_HwDeviceFunction_HwDeviceFunction.__init__)


def test_marte_hwdevicefunction_hwdevicefunction_constructor_args():
    sig = inspect.signature(MARTE_HwDeviceFunction_HwDeviceFunction.__init__)
    params = list(sig.parameters.keys())



def test_grm_marte_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_OpaqueExpression)


def test_grm_marte_opaqueexpression_constructor_exists():
    assert callable(GRM_MARTE_OpaqueExpression.__init__)


def test_grm_marte_opaqueexpression_constructor_args():
    sig = inspect.signature(GRM_MARTE_OpaqueExpression.__init__)
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



def test_nfp_integer_is_not_abstract():
    assert not inspect.isabstract(NFP_Integer)


def test_nfp_integer_constructor_exists():
    assert callable(NFP_Integer.__init__)


def test_nfp_integer_constructor_args():
    sig = inspect.signature(NFP_Integer.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_resource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_Resource)


def test_marte_grm_resource_constructor_exists():
    assert callable(MARTE_GRM_Resource.__init__)


def test_marte_grm_resource_constructor_args():
    sig = inspect.signature(MARTE_GRM_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "isProtected" in params, "Missing parameter 'isProtected'"

def test_marte_grm_resource_has_isProtected():
    assert hasattr(MARTE_GRM_Resource, "isProtected")
    descriptor = None
    for klass in MARTE_GRM_Resource.__mro__:
        if "isProtected" in klass.__dict__:
            descriptor = klass.__dict__["isProtected"]
            break
    assert isinstance(descriptor, property)



def test_time_marte_event_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Event)


def test_time_marte_event_constructor_exists():
    assert callable(Time_MARTE_Event.__init__)


def test_time_marte_event_constructor_args():
    sig = inspect.signature(Time_MARTE_Event.__init__)
    params = list(sig.parameters.keys())



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



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_marte_sw_resourcecore_swresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_SW_ResourceCore_SwResource)


def test_marte_sw_resourcecore_swresource_constructor_exists():
    assert callable(MARTE_SW_ResourceCore_SwResource.__init__)


def test_marte_sw_resourcecore_swresource_constructor_args():
    sig = inspect.signature(MARTE_SW_ResourceCore_SwResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_scheduler_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_Scheduler)


def test_marte_grm_scheduler_constructor_exists():
    assert callable(MARTE_GRM_Scheduler.__init__)


def test_marte_grm_scheduler_constructor_args():
    sig = inspect.signature(MARTE_GRM_Scheduler.__init__)
    params = list(sig.parameters.keys())
    assert "isPreemptible" in params, "Missing parameter 'isPreemptible'"
    assert "schedPolicy" in params, "Missing parameter 'schedPolicy'"
    assert "otherSchedPolicy" in params, "Missing parameter 'otherSchedPolicy'"

def test_marte_grm_scheduler_has_isPreemptible():
    assert hasattr(MARTE_GRM_Scheduler, "isPreemptible")
    descriptor = None
    for klass in MARTE_GRM_Scheduler.__mro__:
        if "isPreemptible" in klass.__dict__:
            descriptor = klass.__dict__["isPreemptible"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_scheduler_has_schedPolicy():
    assert hasattr(MARTE_GRM_Scheduler, "schedPolicy")
    descriptor = None
    for klass in MARTE_GRM_Scheduler.__mro__:
        if "schedPolicy" in klass.__dict__:
            descriptor = klass.__dict__["schedPolicy"]
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



def test_marte_grm_synchronizationresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_SynchronizationResource)


def test_marte_grm_synchronizationresource_constructor_exists():
    assert callable(MARTE_GRM_SynchronizationResource.__init__)


def test_marte_grm_synchronizationresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_SynchronizationResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_communicationendpoint_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_CommunicationEndPoint)


def test_marte_grm_communicationendpoint_constructor_exists():
    assert callable(MARTE_GRM_CommunicationEndPoint.__init__)


def test_marte_grm_communicationendpoint_constructor_args():
    sig = inspect.signature(MARTE_GRM_CommunicationEndPoint.__init__)
    params = list(sig.parameters.keys())



def test_marte_pam_palogicalresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_PAM_PaLogicalResource)


def test_marte_pam_palogicalresource_constructor_exists():
    assert callable(MARTE_PAM_PaLogicalResource.__init__)


def test_marte_pam_palogicalresource_constructor_args():
    sig = inspect.signature(MARTE_PAM_PaLogicalResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwgeneral_hwresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwGeneral_HwResource)


def test_marte_hwgeneral_hwresource_constructor_exists():
    assert callable(MARTE_HwGeneral_HwResource.__init__)


def test_marte_hwgeneral_hwresource_constructor_args():
    sig = inspect.signature(MARTE_HwGeneral_HwResource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_marte_hwgeneral_hwresource_has_name():
    assert hasattr(MARTE_HwGeneral_HwResource, "name")
    descriptor = None
    for klass in MARTE_HwGeneral_HwResource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_marte_grm_concurrencyresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_ConcurrencyResource)


def test_marte_grm_concurrencyresource_constructor_exists():
    assert callable(MARTE_GRM_ConcurrencyResource.__init__)


def test_marte_grm_concurrencyresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_ConcurrencyResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_mutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_MutualExclusionResource)


def test_marte_grm_mutualexclusionresource_constructor_exists():
    assert callable(MARTE_GRM_MutualExclusionResource.__init__)


def test_marte_grm_mutualexclusionresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_MutualExclusionResource.__init__)
    params = list(sig.parameters.keys())
    assert "protectKind" in params, "Missing parameter 'protectKind'"
    assert "otherProtectProtocol" in params, "Missing parameter 'otherProtectProtocol'"

def test_marte_grm_mutualexclusionresource_has_protectKind():
    assert hasattr(MARTE_GRM_MutualExclusionResource, "protectKind")
    descriptor = None
    for klass in MARTE_GRM_MutualExclusionResource.__mro__:
        if "protectKind" in klass.__dict__:
            descriptor = klass.__dict__["protectKind"]
            break
    assert isinstance(descriptor, property)

def test_marte_grm_mutualexclusionresource_has_otherProtectProtocol():
    assert hasattr(MARTE_GRM_MutualExclusionResource, "otherProtectProtocol")
    descriptor = None
    for klass in MARTE_GRM_MutualExclusionResource.__mro__:
        if "otherProtectProtocol" in klass.__dict__:
            descriptor = klass.__dict__["otherProtectProtocol"]
            break
    assert isinstance(descriptor, property)



def test_marte_grm_storageresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_StorageResource)


def test_marte_grm_storageresource_constructor_exists():
    assert callable(MARTE_GRM_StorageResource.__init__)


def test_marte_grm_storageresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_StorageResource.__init__)
    params = list(sig.parameters.keys())



def test_grm_marte_connectableelement_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_ConnectableElement)


def test_grm_marte_connectableelement_constructor_exists():
    assert callable(GRM_MARTE_ConnectableElement.__init__)


def test_grm_marte_connectableelement_constructor_args():
    sig = inspect.signature(GRM_MARTE_ConnectableElement.__init__)
    params = list(sig.parameters.keys())



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



def test_timedobservation_is_not_abstract():
    assert not inspect.isabstract(TimedObservation)


def test_timedobservation_constructor_exists():
    assert callable(TimedObservation.__init__)


def test_timedobservation_constructor_args():
    sig = inspect.signature(TimedObservation.__init__)
    params = list(sig.parameters.keys())



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



def test_marte_time_timedobservation_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_TimedObservation)


def test_marte_time_timedobservation_constructor_exists():
    assert callable(MARTE_Time_TimedObservation.__init__)


def test_marte_time_timedobservation_constructor_args():
    sig = inspect.signature(MARTE_Time_TimedObservation.__init__)
    params = list(sig.parameters.keys())



def test_marte_time_timedprocessing_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_TimedProcessing)


def test_marte_time_timedprocessing_constructor_exists():
    assert callable(MARTE_Time_TimedProcessing.__init__)


def test_marte_time_timedprocessing_constructor_args():
    sig = inspect.signature(MARTE_Time_TimedProcessing.__init__)
    params = list(sig.parameters.keys())



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



def test_time_marte_durationobservation_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_DurationObservation)


def test_time_marte_durationobservation_constructor_exists():
    assert callable(Time_MARTE_DurationObservation.__init__)


def test_time_marte_durationobservation_constructor_args():
    sig = inspect.signature(Time_MARTE_DurationObservation.__init__)
    params = list(sig.parameters.keys())



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



def test_time_marte_timeobservation_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_TimeObservation)


def test_time_marte_timeobservation_constructor_exists():
    assert callable(Time_MARTE_TimeObservation.__init__)


def test_time_marte_timeobservation_constructor_args():
    sig = inspect.signature(Time_MARTE_TimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_time_marte_enumeration_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Enumeration)


def test_time_marte_enumeration_constructor_exists():
    assert callable(Time_MARTE_Enumeration.__init__)


def test_time_marte_enumeration_constructor_args():
    sig = inspect.signature(Time_MARTE_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_marte_time_clocktype_is_not_abstract():
    assert not inspect.isabstract(MARTE_Time_ClockType)


def test_marte_time_clocktype_constructor_exists():
    assert callable(MARTE_Time_ClockType.__init__)


def test_marte_time_clocktype_constructor_args():
    sig = inspect.signature(MARTE_Time_ClockType.__init__)
    params = list(sig.parameters.keys())
    assert "isLogical" in params, "Missing parameter 'isLogical'"
    assert "nature" in params, "Missing parameter 'nature'"

def test_marte_time_clocktype_has_isLogical():
    assert hasattr(MARTE_Time_ClockType, "isLogical")
    descriptor = None
    for klass in MARTE_Time_ClockType.__mro__:
        if "isLogical" in klass.__dict__:
            descriptor = klass.__dict__["isLogical"]
            break
    assert isinstance(descriptor, property)

def test_marte_time_clocktype_has_nature():
    assert hasattr(MARTE_Time_ClockType, "nature")
    descriptor = None
    for klass in MARTE_Time_ClockType.__mro__:
        if "nature" in klass.__dict__:
            descriptor = klass.__dict__["nature"]
            break
    assert isinstance(descriptor, property)



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



def test_time_marte_operation_is_not_abstract():
    assert not inspect.isabstract(Time_MARTE_Operation)


def test_time_marte_operation_constructor_exists():
    assert callable(Time_MARTE_Operation.__init__)


def test_time_marte_operation_constructor_args():
    sig = inspect.signature(Time_MARTE_Operation.__init__)
    params = list(sig.parameters.keys())



def test_marte_alloc_assign_is_not_abstract():
    assert not inspect.isabstract(MARTE_Alloc_Assign)


def test_marte_alloc_assign_constructor_exists():
    assert callable(MARTE_Alloc_Assign.__init__)


def test_marte_alloc_assign_constructor_args():
    sig = inspect.signature(MARTE_Alloc_Assign.__init__)
    params = list(sig.parameters.keys())



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
    assert "isPrecedenceBased" in params, "Missing parameter 'isPrecedenceBased'"
    assert "isCoincidenceBased" in params, "Missing parameter 'isCoincidenceBased'"
    assert "isChronometricBased" in params, "Missing parameter 'isChronometricBased'"

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

def test_marte_time_clockconstraint_has_isChronometricBased():
    assert hasattr(MARTE_Time_ClockConstraint, "isChronometricBased")
    descriptor = None
    for klass in MARTE_Time_ClockConstraint.__mro__:
        if "isChronometricBased" in klass.__dict__:
            descriptor = klass.__dict__["isChronometricBased"]
            break
    assert isinstance(descriptor, property)



def test_alloc_marte_dependency_is_not_abstract():
    assert not inspect.isabstract(Alloc_MARTE_Dependency)


def test_alloc_marte_dependency_constructor_exists():
    assert callable(Alloc_MARTE_Dependency.__init__)


def test_alloc_marte_dependency_constructor_args():
    sig = inspect.signature(Alloc_MARTE_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_marte_alloc_nfprefine_is_not_abstract():
    assert not inspect.isabstract(MARTE_Alloc_NfpRefine)


def test_marte_alloc_nfprefine_constructor_exists():
    assert callable(MARTE_Alloc_NfpRefine.__init__)


def test_marte_alloc_nfprefine_constructor_args():
    sig = inspect.signature(MARTE_Alloc_NfpRefine.__init__)
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



def test_alloc_allocated_is_not_abstract():
    assert not inspect.isabstract(Alloc_Allocated)


def test_alloc_allocated_constructor_exists():
    assert callable(Alloc_Allocated.__init__)


def test_alloc_allocated_constructor_args():
    sig = inspect.signature(Alloc_Allocated.__init__)
    params = list(sig.parameters.keys())



def test_alloc_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(Alloc_MARTE_NamedElement)


def test_alloc_marte_namedelement_constructor_exists():
    assert callable(Alloc_MARTE_NamedElement.__init__)


def test_alloc_marte_namedelement_constructor_args():
    sig = inspect.signature(Alloc_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte_alloc_allocated_is_not_abstract():
    assert not inspect.isabstract(MARTE_Alloc_Allocated)


def test_marte_alloc_allocated_constructor_exists():
    assert callable(MARTE_Alloc_Allocated.__init__)


def test_marte_alloc_allocated_constructor_args():
    sig = inspect.signature(MARTE_Alloc_Allocated.__init__)
    params = list(sig.parameters.keys())



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
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "baseExponent" in params, "Missing parameter 'baseExponent'"

def test_marte_nfps_dimension_has_symbol():
    assert hasattr(MARTE_NFPs_Dimension, "symbol")
    descriptor = None
    for klass in MARTE_NFPs_Dimension.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_marte_nfps_dimension_has_baseExponent():
    assert hasattr(MARTE_NFPs_Dimension, "baseExponent")
    descriptor = None
    for klass in MARTE_NFPs_Dimension.__mro__:
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



def test_marte_nfps_nfp_is_not_abstract():
    assert not inspect.isabstract(MARTE_NFPs_Nfp)


def test_marte_nfps_nfp_constructor_exists():
    assert callable(MARTE_NFPs_Nfp.__init__)


def test_marte_nfps_nfp_constructor_args():
    sig = inspect.signature(MARTE_NFPs_Nfp.__init__)
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
    assert "convFactor" in params, "Missing parameter 'convFactor'"
    assert "offsetFactor" in params, "Missing parameter 'offsetFactor'"

def test_marte_nfps_unit_has_convFactor():
    assert hasattr(MARTE_NFPs_Unit, "convFactor")
    descriptor = None
    for klass in MARTE_NFPs_Unit.__mro__:
        if "convFactor" in klass.__dict__:
            descriptor = klass.__dict__["convFactor"]
            break
    assert isinstance(descriptor, property)

def test_marte_nfps_unit_has_offsetFactor():
    assert hasattr(MARTE_NFPs_Unit, "offsetFactor")
    descriptor = None
    for klass in MARTE_NFPs_Unit.__mro__:
        if "offsetFactor" in klass.__dict__:
            descriptor = klass.__dict__["offsetFactor"]
            break
    assert isinstance(descriptor, property)



def test_nfps_marte_property_is_not_abstract():
    assert not inspect.isabstract(NFPs_MARTE_Property)


def test_nfps_marte_property_constructor_exists():
    assert callable(NFPs_MARTE_Property.__init__)


def test_nfps_marte_property_constructor_args():
    sig = inspect.signature(NFPs_MARTE_Property.__init__)
    params = list(sig.parameters.keys())



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



def test_hlam_marte_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(HLAM_MARTE_BehavioredClassifier)


def test_hlam_marte_behavioredclassifier_constructor_exists():
    assert callable(HLAM_MARTE_BehavioredClassifier.__init__)


def test_hlam_marte_behavioredclassifier_constructor_args():
    sig = inspect.signature(HLAM_MARTE_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_datatypes_marte_property_is_not_abstract():
    assert not inspect.isabstract(DataTypes_MARTE_Property)


def test_datatypes_marte_property_constructor_exists():
    assert callable(DataTypes_MARTE_Property.__init__)


def test_datatypes_marte_property_constructor_args():
    sig = inspect.signature(DataTypes_MARTE_Property.__init__)
    params = list(sig.parameters.keys())



def test_marte_datatypes_boundedsubtype_is_not_abstract():
    assert not inspect.isabstract(MARTE_DataTypes_BoundedSubtype)


def test_marte_datatypes_boundedsubtype_constructor_exists():
    assert callable(MARTE_DataTypes_BoundedSubtype.__init__)


def test_marte_datatypes_boundedsubtype_constructor_args():
    sig = inspect.signature(MARTE_DataTypes_BoundedSubtype.__init__)
    params = list(sig.parameters.keys())
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "isMinOpen" in params, "Missing parameter 'isMinOpen'"
    assert "isMaxOpen" in params, "Missing parameter 'isMaxOpen'"
    assert "minValue" in params, "Missing parameter 'minValue'"

def test_marte_datatypes_boundedsubtype_has_maxValue():
    assert hasattr(MARTE_DataTypes_BoundedSubtype, "maxValue")
    descriptor = None
    for klass in MARTE_DataTypes_BoundedSubtype.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
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

def test_marte_datatypes_boundedsubtype_has_isMaxOpen():
    assert hasattr(MARTE_DataTypes_BoundedSubtype, "isMaxOpen")
    descriptor = None
    for klass in MARTE_DataTypes_BoundedSubtype.__mro__:
        if "isMaxOpen" in klass.__dict__:
            descriptor = klass.__dict__["isMaxOpen"]
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



def test_rsm_marte_connectorend_is_not_abstract():
    assert not inspect.isabstract(RSM_MARTE_ConnectorEnd)


def test_rsm_marte_connectorend_constructor_exists():
    assert callable(RSM_MARTE_ConnectorEnd.__init__)


def test_rsm_marte_connectorend_constructor_args():
    sig = inspect.signature(RSM_MARTE_ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_marte_datatypes_collectiontype_is_not_abstract():
    assert not inspect.isabstract(MARTE_DataTypes_CollectionType)


def test_marte_datatypes_collectiontype_constructor_exists():
    assert callable(MARTE_DataTypes_CollectionType.__init__)


def test_marte_datatypes_collectiontype_constructor_args():
    sig = inspect.signature(MARTE_DataTypes_CollectionType.__init__)
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



def test_marte_rsm_reshape_is_not_abstract():
    assert not inspect.isabstract(MARTE_RSM_Reshape)


def test_marte_rsm_reshape_constructor_exists():
    assert callable(MARTE_RSM_Reshape.__init__)


def test_marte_rsm_reshape_constructor_args():
    sig = inspect.signature(MARTE_RSM_Reshape.__init__)
    params = list(sig.parameters.keys())



def test_marte_rsm_interrepetition_is_not_abstract():
    assert not inspect.isabstract(MARTE_RSM_InterRepetition)


def test_marte_rsm_interrepetition_constructor_exists():
    assert callable(MARTE_RSM_InterRepetition.__init__)


def test_marte_rsm_interrepetition_constructor_args():
    sig = inspect.signature(MARTE_RSM_InterRepetition.__init__)
    params = list(sig.parameters.keys())
    assert "isModulo" in params, "Missing parameter 'isModulo'"

def test_marte_rsm_interrepetition_has_isModulo():
    assert hasattr(MARTE_RSM_InterRepetition, "isModulo")
    descriptor = None
    for klass in MARTE_RSM_InterRepetition.__mro__:
        if "isModulo" in klass.__dict__:
            descriptor = klass.__dict__["isModulo"]
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



def test_integermatrix_is_not_abstract():
    assert not inspect.isabstract(IntegerMatrix)


def test_integermatrix_constructor_exists():
    assert callable(IntegerMatrix.__init__)


def test_integermatrix_constructor_args():
    sig = inspect.signature(IntegerMatrix.__init__)
    params = list(sig.parameters.keys())



def test_marte_rsm_tiler_is_not_abstract():
    assert not inspect.isabstract(MARTE_RSM_Tiler)


def test_marte_rsm_tiler_constructor_exists():
    assert callable(MARTE_RSM_Tiler.__init__)


def test_marte_rsm_tiler_constructor_args():
    sig = inspect.signature(MARTE_RSM_Tiler.__init__)
    params = list(sig.parameters.keys())



def test_nfp_energy_is_not_abstract():
    assert not inspect.isabstract(NFP_Energy)


def test_nfp_energy_constructor_exists():
    assert callable(NFP_Energy.__init__)


def test_nfp_energy_constructor_args():
    sig = inspect.signature(NFP_Energy.__init__)
    params = list(sig.parameters.keys())



def test_nfp_power_is_not_abstract():
    assert not inspect.isabstract(NFP_Power)


def test_nfp_power_constructor_exists():
    assert callable(NFP_Power.__init__)


def test_nfp_power_constructor_args():
    sig = inspect.signature(NFP_Power.__init__)
    params = list(sig.parameters.keys())



def test_nfp_datasize_is_not_abstract():
    assert not inspect.isabstract(NFP_DataSize)


def test_nfp_datasize_constructor_exists():
    assert callable(NFP_DataSize.__init__)


def test_nfp_datasize_constructor_args():
    sig = inspect.signature(NFP_DataSize.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_resourceusage_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_ResourceUsage)


def test_marte_grm_resourceusage_constructor_exists():
    assert callable(MARTE_GRM_ResourceUsage.__init__)


def test_marte_grm_resourceusage_constructor_args():
    sig = inspect.signature(MARTE_GRM_ResourceUsage.__init__)
    params = list(sig.parameters.keys())



def test_grservice_is_not_abstract():
    assert not inspect.isabstract(GrService)


def test_grservice_constructor_exists():
    assert callable(GrService.__init__)


def test_grservice_constructor_args():
    sig = inspect.signature(GrService.__init__)
    params = list(sig.parameters.keys())



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



def test_marte_hwgeneral_hwresourceservice_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwGeneral_HwResourceService)


def test_marte_hwgeneral_hwresourceservice_constructor_exists():
    assert callable(MARTE_HwGeneral_HwResourceService.__init__)


def test_marte_hwgeneral_hwresourceservice_constructor_args():
    sig = inspect.signature(MARTE_HwGeneral_HwResourceService.__init__)
    params = list(sig.parameters.keys())



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



def test_grm_marte_namedelement_is_not_abstract():
    assert not inspect.isabstract(GRM_MARTE_NamedElement)


def test_grm_marte_namedelement_constructor_exists():
    assert callable(GRM_MARTE_NamedElement.__init__)


def test_grm_marte_namedelement_constructor_args():
    sig = inspect.signature(GRM_MARTE_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_deviceresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_DeviceResource)


def test_marte_grm_deviceresource_constructor_exists():
    assert callable(MARTE_GRM_DeviceResource.__init__)


def test_marte_grm_deviceresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_DeviceResource.__init__)
    params = list(sig.parameters.keys())



def test_nfp_datatxrate_is_not_abstract():
    assert not inspect.isabstract(NFP_DataTxRate)


def test_nfp_datatxrate_constructor_exists():
    assert callable(NFP_DataTxRate.__init__)


def test_nfp_datatxrate_constructor_args():
    sig = inspect.signature(NFP_DataTxRate.__init__)
    params = list(sig.parameters.keys())



def test_nfp_duration_is_not_abstract():
    assert not inspect.isabstract(NFP_Duration)


def test_nfp_duration_constructor_exists():
    assert callable(NFP_Duration.__init__)


def test_nfp_duration_constructor_args():
    sig = inspect.signature(NFP_Duration.__init__)
    params = list(sig.parameters.keys())



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
    assert "transmMode" in params, "Missing parameter 'transmMode'"

def test_marte_grm_communicationmedia_has_transmMode():
    assert hasattr(MARTE_GRM_CommunicationMedia, "transmMode")
    descriptor = None
    for klass in MARTE_GRM_CommunicationMedia.__mro__:
        if "transmMode" in klass.__dict__:
            descriptor = klass.__dict__["transmMode"]
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



def test_grm_secondaryscheduler_is_not_abstract():
    assert not inspect.isabstract(GRM_SecondaryScheduler)


def test_grm_secondaryscheduler_constructor_exists():
    assert callable(GRM_SecondaryScheduler.__init__)


def test_grm_secondaryscheduler_constructor_args():
    sig = inspect.signature(GRM_SecondaryScheduler.__init__)
    params = list(sig.parameters.keys())



def test_schedparameters_is_not_abstract():
    assert not inspect.isabstract(SchedParameters)


def test_schedparameters_constructor_exists():
    assert callable(SchedParameters.__init__)


def test_schedparameters_constructor_args():
    sig = inspect.signature(SchedParameters.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_schedulableresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_SchedulableResource)


def test_marte_grm_schedulableresource_constructor_exists():
    assert callable(MARTE_GRM_SchedulableResource.__init__)


def test_marte_grm_schedulableresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_SchedulableResource.__init__)
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
    assert "isPeriodic" in params, "Missing parameter 'isPeriodic'"

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



def test_grm_scheduler_is_not_abstract():
    assert not inspect.isabstract(GRM_Scheduler)


def test_grm_scheduler_constructor_exists():
    assert callable(GRM_Scheduler.__init__)


def test_grm_scheduler_constructor_args():
    sig = inspect.signature(GRM_Scheduler.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gacommhost_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaCommHost)


def test_marte_gqam_gacommhost_constructor_exists():
    assert callable(MARTE_GQAM_GaCommHost.__init__)


def test_marte_gqam_gacommhost_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaCommHost.__init__)
    params = list(sig.parameters.keys())



def test_nfp_real_is_not_abstract():
    assert not inspect.isabstract(NFP_Real)


def test_nfp_real_constructor_exists():
    assert callable(NFP_Real.__init__)


def test_nfp_real_constructor_args():
    sig = inspect.signature(NFP_Real.__init__)
    params = list(sig.parameters.keys())



def test_marte_grm_processingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_GRM_ProcessingResource)


def test_marte_grm_processingresource_constructor_exists():
    assert callable(MARTE_GRM_ProcessingResource.__init__)


def test_marte_grm_processingresource_constructor_args():
    sig = inspect.signature(MARTE_GRM_ProcessingResource.__init__)
    params = list(sig.parameters.keys())



def test_grm_schedulableresource_is_not_abstract():
    assert not inspect.isabstract(GRM_SchedulableResource)


def test_grm_schedulableresource_constructor_exists():
    assert callable(GRM_SchedulableResource.__init__)


def test_grm_schedulableresource_constructor_args():
    sig = inspect.signature(GRM_SchedulableResource.__init__)
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



def test_grm_mutualexclusionresource_is_not_abstract():
    assert not inspect.isabstract(GRM_MutualExclusionResource)


def test_grm_mutualexclusionresource_constructor_exists():
    assert callable(GRM_MutualExclusionResource.__init__)


def test_grm_mutualexclusionresource_constructor_args():
    sig = inspect.signature(GRM_MutualExclusionResource.__init__)
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



def test_grm_computingresource_is_not_abstract():
    assert not inspect.isabstract(GRM_ComputingResource)


def test_grm_computingresource_constructor_exists():
    assert callable(GRM_ComputingResource.__init__)


def test_grm_computingresource_constructor_args():
    sig = inspect.signature(GRM_ComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_hwcomputing_hwcomputingresource_is_not_abstract():
    assert not inspect.isabstract(MARTE_HwComputing_HwComputingResource)


def test_marte_hwcomputing_hwcomputingresource_constructor_exists():
    assert callable(MARTE_HwComputing_HwComputingResource.__init__)


def test_marte_hwcomputing_hwcomputingresource_constructor_args():
    sig = inspect.signature(MARTE_HwComputing_HwComputingResource.__init__)
    params = list(sig.parameters.keys())



def test_marte_gqam_gaexechost_is_not_abstract():
    assert not inspect.isabstract(MARTE_GQAM_GaExecHost)


def test_marte_gqam_gaexechost_constructor_exists():
    assert callable(MARTE_GQAM_GaExecHost.__init__)


def test_marte_gqam_gaexechost_constructor_args():
    sig = inspect.signature(MARTE_GQAM_GaExecHost.__init__)
    params = list(sig.parameters.keys())



def test_grm_processingresource_is_not_abstract():
    assert not inspect.isabstract(GRM_ProcessingResource)


def test_grm_processingresource_constructor_exists():
    assert callable(GRM_ProcessingResource.__init__)


def test_grm_processingresource_constructor_args():
    sig = inspect.signature(GRM_ProcessingResource.__init__)
    params = list(sig.parameters.keys())

def test_concurrentaccessprotocolkind_exists():
    # Check that the Enumeration exists
    assert ConcurrentAccessProtocolKind is not None

def test_concurrentaccessprotocolkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConcurrentAccessProtocolKind]
    expected_literals = [
        "Undef",
        "PIP",
        "PCP",
        "Other",
        "NoPreemption",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConcurrentAccessProtocolKind"

def test_portspecificationkind_exists():
    # Check that the Enumeration exists
    assert PortSpecificationKind is not None

def test_portspecificationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PortSpecificationKind]
    expected_literals = [
        "featureBased",
        "atomic",
        "interfaceBased",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PortSpecificationKind"

def test_rom_type_exists():
    # Check that the Enumeration exists
    assert ROM_Type is not None

def test_rom_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ROM_Type]
    expected_literals = [
        "EEPROM",
        "undef",
        "other",
        "maskedROM",
        "EPROM",
        "OTP_EPROM",
        "Flash",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ROM_Type"

def test_pld_technology_exists():
    # Check that the Enumeration exists
    assert PLD_Technology is not None

def test_pld_technology_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PLD_Technology]
    expected_literals = [
        "antifuse",
        "undef",
        "other",
        "flash",
        "SRAM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PLD_Technology"

def test_poolmgtpolicykind_exists():
    # Check that the Enumeration exists
    assert PoolMgtPolicyKind is not None

def test_poolmgtpolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PoolMgtPolicyKind]
    expected_literals = [
        "other",
        "dynamic",
        "infiniteWait",
        "timedWait",
        "exception",
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
        "in_",
        "inout",
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
        "Event",
        "Barrier",
        "Other",
        "Undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NotificationResourceKind"

def test_conditiontype_exists():
    # Check that the Enumeration exists
    assert ConditionType is not None

def test_conditiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionType]
    expected_literals = [
        "altitude",
        "temperature",
        "shock",
        "vibration",
        "other",
        "humidity",
        "undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionType"

def test_pld_class_exists():
    # Check that the Enumeration exists
    assert PLD_Class is not None

def test_pld_class_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PLD_Class]
    expected_literals = [
        "other",
        "hierarchicalPLD",
        "seaOfGates",
        "rowBased",
        "undef",
        "symetricalArray",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PLD_Class"

def test_componentstate_exists():
    # Check that the Enumeration exists
    assert ComponentState is not None

def test_componentstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentState]
    expected_literals = [
        "other",
        "storage",
        "undef",
        "operating",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentState"

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

def test_concurrencykind_exists():
    # Check that the Enumeration exists
    assert ConcurrencyKind is not None

def test_concurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConcurrencyKind]
    expected_literals = [
        "writer",
        "reader",
        "parallel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConcurrencyKind"

def test_isa_type_exists():
    # Check that the Enumeration exists
    assert ISA_Type is not None

def test_isa_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ISA_Type]
    expected_literals = [
        "other",
        "SIMD",
        "RISC",
        "CISC",
        "VLIW",
        "undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ISA_Type"

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

def test_writepolicy_exists():
    # Check that the Enumeration exists
    assert WritePolicy is not None

def test_writepolicy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WritePolicy]
    expected_literals = [
        "writeBack",
        "other",
        "writeThrough",
        "undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WritePolicy"

def test_synchronizationkind_exists():
    # Check that the Enumeration exists
    assert SynchronizationKind is not None

def test_synchronizationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SynchronizationKind]
    expected_literals = [
        "other",
        "synchronous",
        "delayedSynchronous",
        "asynchronous",
        "rendezVous",
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

def test_queuepolicykind_exists():
    # Check that the Enumeration exists
    assert QueuePolicyKind is not None

def test_queuepolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QueuePolicyKind]
    expected_literals = [
        "Priority",
        "FIFO",
        "Undef",
        "Other",
        "LIFO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QueuePolicyKind"

def test_interruptkind_exists():
    # Check that the Enumeration exists
    assert InterruptKind is not None

def test_interruptkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InterruptKind]
    expected_literals = [
        "HardwareInterruption",
        "ProgrammedException",
        "ProcessorDetectedException",
        "Undef",
        "Other",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InterruptKind"

def test_mutualexclusionresourcekind_exists():
    # Check that the Enumeration exists
    assert MutualExclusionResourceKind is not None

def test_mutualexclusionresourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MutualExclusionResourceKind]
    expected_literals = [
        "CountSemaphore",
        "BooleanSemaphore",
        "Other",
        "Mutex",
        "Undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MutualExclusionResourceKind"

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

def test_cachetype_exists():
    # Check that the Enumeration exists
    assert CacheType is not None

def test_cachetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CacheType]
    expected_literals = [
        "instruction",
        "other",
        "data",
        "unified",
        "undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CacheType"

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

def test_componentkind_exists():
    # Check that the Enumeration exists
    assert ComponentKind is not None

def test_componentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentKind]
    expected_literals = [
        "card",
        "undef",
        "channel",
        "other",
        "chip",
        "unit",
        "port",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentKind"

def test_notificationkind_exists():
    # Check that the Enumeration exists
    assert NotificationKind is not None

def test_notificationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NotificationKind]
    expected_literals = [
        "Memoryless",
        "Undef",
        "Bounded",
        "Other",
        "Memorized",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NotificationKind"

def test_repl_policy_exists():
    # Check that the Enumeration exists
    assert Repl_Policy is not None

def test_repl_policy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Repl_Policy]
    expected_literals = [
        "NFU",
        "LRU",
        "FIFO",
        "other",
        "undef",
        "random",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Repl_Policy"

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

def test_accesspolicykind_exists():
    # Check that the Enumeration exists
    assert AccessPolicyKind is not None

def test_accesspolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessPolicyKind]
    expected_literals = [
        "Other",
        "ReadWrite",
        "Write",
        "Undef",
        "Read",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessPolicyKind"

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

def test_messageresourcekind_exists():
    # Check that the Enumeration exists
    assert MessageResourceKind is not None

def test_messageresourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageResourceKind]
    expected_literals = [
        "Blackboard",
        "Pipe",
        "Undef",
        "Other",
        "MessageQueue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageResourceKind"

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

def test_clientserverkind_exists():
    # Check that the Enumeration exists
    assert ClientServerKind is not None

def test_clientserverkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClientServerKind]
    expected_literals = [
        "proreq",
        "required",
        "provided",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClientServerKind"

def test_optimallitycriterionkind_exists():
    # Check that the Enumeration exists
    assert OptimallityCriterionKind is not None

def test_optimallitycriterionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptimallityCriterionKind]
    expected_literals = [
        "minimizedMeanTardiness",
        "meetHardDeadlines",
        "other",
        "undef",
        "minimizeMissedDeadlines",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptimallityCriterionKind"


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
PAM_MARTE_NamedElement_strategy = st.builds(
    PAM_MARTE_NamedElement,
)
GQAM_GaCommStep_strategy = st.builds(
    GQAM_GaCommStep,
)
PAM_PaStep_strategy = st.builds(
    PAM_PaStep,
)
MARTE_PAM_PaCommStep_strategy = st.builds(
    MARTE_PAM_PaCommStep,
)
MARTE_PAM_PaRunTInstance_strategy = st.builds(
    MARTE_PAM_PaRunTInstance,
    unbddPool=
        safe_text
)
GaExecHost_strategy = st.builds(
    GaExecHost,
)
MARTE_SAM_SaExecHost_strategy = st.builds(
    MARTE_SAM_SaExecHost,
)
MutualExclusionResource_strategy = st.builds(
    MutualExclusionResource,
)
MARTE_SAM_SaSharedResource_strategy = st.builds(
    MARTE_SAM_SaSharedResource,
)
GaCommHost_strategy = st.builds(
    GaCommHost,
)
MARTE_SAM_SaCommHost_strategy = st.builds(
    MARTE_SAM_SaCommHost,
)
SAM_MARTE_BehavioralFeature_strategy = st.builds(
    SAM_MARTE_BehavioralFeature,
)
SAM_SaSharedResource_strategy = st.builds(
    SAM_SaSharedResource,
)
GaAnalysisContext_strategy = st.builds(
    GaAnalysisContext,
)
MARTE_SAM_SaAnalysisContext_strategy = st.builds(
    MARTE_SAM_SaAnalysisContext,
    optCriterion=
        safe_text
)
GQAM_MARTE_Classifier_strategy = st.builds(
    GQAM_MARTE_Classifier,
)
GaCommStep_strategy = st.builds(
    GaCommStep,
)
MARTE_SAM_SaCommStep_strategy = st.builds(
    MARTE_SAM_SaCommStep,
)
SAM_MARTE_NamedElement_strategy = st.builds(
    SAM_MARTE_NamedElement,
)
MARTE_SAM_SaEndtoEndFlow_strategy = st.builds(
    MARTE_SAM_SaEndtoEndFlow,
)
SchedulableResource_strategy = st.builds(
    SchedulableResource,
)
MARTE_GQAM_GaCommChannel_strategy = st.builds(
    MARTE_GQAM_GaCommChannel,
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
)
MARTE_GQAM_GaWorkloadBehavior_strategy = st.builds(
    MARTE_GQAM_GaWorkloadBehavior,
)
GaTimedObs_strategy = st.builds(
    GaTimedObs,
)
MARTE_SAM_SaSchedObs_strategy = st.builds(
    MARTE_SAM_SaSchedObs,
)
MARTE_GQAM_GaLatencyObs_strategy = st.builds(
    MARTE_GQAM_GaLatencyObs,
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
MARTE_GQAM_GaCommStep_strategy = st.builds(
    MARTE_GQAM_GaCommStep,
)
MARTE_PAM_PaResPassStep_strategy = st.builds(
    MARTE_PAM_PaResPassStep,
)
MARTE_PAM_PaStep_strategy = st.builds(
    MARTE_PAM_PaStep,
    extOpDemand=
        safe_text
)
MARTE_SAM_SaStep_strategy = st.builds(
    MARTE_SAM_SaStep,
)
MARTE_GQAM_GaAcqStep_strategy = st.builds(
    MARTE_GQAM_GaAcqStep,
)
MARTE_GQAM_GaRelStep_strategy = st.builds(
    MARTE_GQAM_GaRelStep,
)
MARTE_GQAM_GaRequestedService_strategy = st.builds(
    MARTE_GQAM_GaRequestedService,
)
IntegerInterval_strategy = st.builds(
    IntegerInterval,
)
GaScenario_strategy = st.builds(
    GaScenario,
)
MARTE_GQAM_GaStep_strategy = st.builds(
    MARTE_GQAM_GaStep,
)
GQAM_GaTimedObs_strategy = st.builds(
    GQAM_GaTimedObs,
)
GQAM_GaStep_strategy = st.builds(
    GQAM_GaStep,
)
GQAM_GaRequestedService_strategy = st.builds(
    GQAM_GaRequestedService,
)
MARTE_PAM_PaRequestedStep_strategy = st.builds(
    MARTE_PAM_PaRequestedStep,
)
GQAM_GaExecHost_strategy = st.builds(
    GQAM_GaExecHost,
)
GQAM_GaWorkloadEvent_strategy = st.builds(
    GQAM_GaWorkloadEvent,
)
Time_TimedProcessing_strategy = st.builds(
    Time_TimedProcessing,
)
MARTE_GQAM_GaWorkloadGenerator_strategy = st.builds(
    MARTE_GQAM_GaWorkloadGenerator,
)
GCM_MARTE_Behavior_strategy = st.builds(
    GCM_MARTE_Behavior,
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
)
GQAM_MARTE_NamedElement_strategy = st.builds(
    GQAM_MARTE_NamedElement,
)
MARTE_GQAM_GaEventTrace_strategy = st.builds(
    MARTE_GQAM_GaEventTrace,
    format=
        safe_text,
    location=
        safe_text,
    content=
        safe_text
)
GQAM_MARTE_Behavior_strategy = st.builds(
    GQAM_MARTE_Behavior,
)
MARTE_GCM_FlowSpecification_strategy = st.builds(
    MARTE_GCM_FlowSpecification,
)
MARTE_GCM_ClientServerSpecification_strategy = st.builds(
    MARTE_GCM_ClientServerSpecification,
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
GCM_MARTE_Trigger_strategy = st.builds(
    GCM_MARTE_Trigger,
)
MARTE_GCM_GCMTrigger_strategy = st.builds(
    MARTE_GCM_GCMTrigger,
)
HwPeripheral_RegisterAction_strategy = st.builds(
    HwPeripheral_RegisterAction,
)
Activity_strategy = st.builds(
    Activity,
)
MARTE_HwPeripheral_PeripheralActivity_strategy = st.builds(
    MARTE_HwPeripheral_PeripheralActivity,
)
HwPeripheral_MARTE_OutputPin_strategy = st.builds(
    HwPeripheral_MARTE_OutputPin,
)
HwPeripheral_MARTE_InputPin_strategy = st.builds(
    HwPeripheral_MARTE_InputPin,
)
RegisterAction_strategy = st.builds(
    RegisterAction,
)
MARTE_HwPeripheral_ReadRegisterAction_strategy = st.builds(
    MARTE_HwPeripheral_ReadRegisterAction,
)
MARTE_HwPeripheral_WriteRegisterAction_strategy = st.builds(
    MARTE_HwPeripheral_WriteRegisterAction,
)
Action_strategy = st.builds(
    Action,
)
MARTE_HwPeripheral_RegisterAction_strategy = st.builds(
    MARTE_HwPeripheral_RegisterAction,
)
HwPeripheral_MARTE_Operation_strategy = st.builds(
    HwPeripheral_MARTE_Operation,
)
Operation_strategy = st.builds(
    Operation,
)
MARTE_HwPeripheral_OperationImpl_strategy = st.builds(
    MARTE_HwPeripheral_OperationImpl,
)
HwIO_HwLine_strategy = st.builds(
    HwIO_HwLine,
)
HwPackage_HwPackagePin_strategy = st.builds(
    HwPackage_HwPackagePin,
)
HwComponent_strategy = st.builds(
    HwComponent,
)
MARTE_HwPower_HwPowerSupply_strategy = st.builds(
    MARTE_HwPower_HwPowerSupply,
)
MARTE_HwPower_HwCoolingSupply_strategy = st.builds(
    MARTE_HwPower_HwCoolingSupply,
)
MARTE_HwLayout_Env_Condition_strategy = st.builds(
    MARTE_HwLayout_Env_Condition,
    type=
        safe_text,
    status=
        safe_text
)
HwLayout_HwComponent_strategy = st.builds(
    HwLayout_HwComponent,
)
HwLayout_Env_Condition_strategy = st.builds(
    HwLayout_Env_Condition,
)
NFP_Price_strategy = st.builds(
    NFP_Price,
)
Realnterval_strategy = st.builds(
    Realnterval,
)
NFP_Length_strategy = st.builds(
    NFP_Length,
)
HwGeneral_MARTE_Activity_strategy = st.builds(
    HwGeneral_MARTE_Activity,
)
HwGeneral_MARTE_Operation_strategy = st.builds(
    HwGeneral_MARTE_Operation,
)
NFP_Frequency_strategy = st.builds(
    NFP_Frequency,
)
HwCommunication_HwEndPoint_strategy = st.builds(
    HwCommunication_HwEndPoint,
)
HwGeneral_HwResourceService_strategy = st.builds(
    HwGeneral_HwResourceService,
)
NFP_NaturalInterval_strategy = st.builds(
    NFP_NaturalInterval,
)
NFP_Area_strategy = st.builds(
    NFP_Area,
)
HwPeripheral_PeripheralActivity_strategy = st.builds(
    HwPeripheral_PeripheralActivity,
)
HwPeripheral_OperationImpl_strategy = st.builds(
    HwPeripheral_OperationImpl,
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
HwDevice_strategy = st.builds(
    HwDevice,
)
MARTE_HwDevice_HwSupport_strategy = st.builds(
    MARTE_HwDevice_HwSupport,
)
MARTE_HwDevice_HwPeripheral_strategy = st.builds(
    MARTE_HwDevice_HwPeripheral,
)
MARTE_HwDevice_HwI_O_strategy = st.builds(
    MARTE_HwDevice_HwI_O,
)
HwTimingResource_strategy = st.builds(
    HwTimingResource,
)
MARTE_HwTiming_HwTimer_strategy = st.builds(
    MARTE_HwTiming_HwTimer,
)
MARTE_HwTiming_HwClock_strategy = st.builds(
    MARTE_HwTiming_HwClock,
)
GRM_TimingResource_strategy = st.builds(
    GRM_TimingResource,
)
HwMemory_CacheStructure_strategy = st.builds(
    HwMemory_CacheStructure,
)
HwDeviceFunction_HwDeviceFunction_strategy = st.builds(
    HwDeviceFunction_HwDeviceFunction,
)
GRM_DeviceResource_strategy = st.builds(
    GRM_DeviceResource,
)
HwTiming_HwClock_strategy = st.builds(
    HwTiming_HwClock,
)
HwMemory_MemoryOrganization_strategy = st.builds(
    HwMemory_MemoryOrganization,
)
HwMemory_strategy = st.builds(
    HwMemory,
)
MARTE_HwMemory_HwCache_strategy = st.builds(
    MARTE_HwMemory_HwCache,
    repl_Policy=
        safe_text,
    writePolicy=
        safe_text,
    type=
        safe_text
)
MARTE_HwMemory_HwDrive_strategy = st.builds(
    MARTE_HwMemory_HwDrive,
)
MARTE_HwMemory_HwRAM_strategy = st.builds(
    MARTE_HwMemory_HwRAM,
    repl_Policy=
        safe_text,
    writePolicy=
        safe_text
)
MARTE_HwMemory_MemoryOrganization_strategy = st.builds(
    MARTE_HwMemory_MemoryOrganization,
)
MARTE_HwMemory_CacheStructure_strategy = st.builds(
    MARTE_HwMemory_CacheStructure,
)
MARTE_HwMemory_HwROM_strategy = st.builds(
    MARTE_HwMemory_HwROM,
    type=
        safe_text
)
MARTE_HwMemory_Timing_strategy = st.builds(
    MARTE_HwMemory_Timing,
)
HwMemory_Timing_strategy = st.builds(
    HwMemory_Timing,
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
HwProtocol_HwProtocol_strategy = st.builds(
    HwProtocol_HwProtocol,
)
HwEndPoint_strategy = st.builds(
    HwEndPoint,
)
MARTE_HwCommunication_HwPort_strategy = st.builds(
    MARTE_HwCommunication_HwPort,
)
GRM_CommunicationEndPoint_strategy = st.builds(
    GRM_CommunicationEndPoint,
)
NFP_Boolean_strategy = st.builds(
    NFP_Boolean,
)
HwStorageManager_strategy = st.builds(
    HwStorageManager,
)
MARTE_HwStorageManager_HwMMU_strategy = st.builds(
    MARTE_HwStorageManager_HwMMU,
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
MARTE_HwCommunication_HwMedia_strategy = st.builds(
    MARTE_HwCommunication_HwMedia,
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
HwCommunication_HwPort_strategy = st.builds(
    HwCommunication_HwPort,
)
HwIO_HwPin_strategy = st.builds(
    HwIO_HwPin,
)
HwPackage_HwPackage_strategy = st.builds(
    HwPackage_HwPackage,
)
HwRegister_HwRegister_strategy = st.builds(
    HwRegister_HwRegister,
)
HwDevice_HwPeripheral_strategy = st.builds(
    HwDevice_HwPeripheral,
)
HwComputing_HwProcessor_strategy = st.builds(
    HwComputing_HwProcessor,
)
HwComputing_HwComputingResource_strategy = st.builds(
    HwComputing_HwComputingResource,
)
HwMedia_strategy = st.builds(
    HwMedia,
)
MARTE_HwIO_HwLine_strategy = st.builds(
    MARTE_HwIO_HwLine,
)
MARTE_HwCommunication_HwBridge_strategy = st.builds(
    MARTE_HwCommunication_HwBridge,
)
MARTE_HwCommunication_HwConnection_strategy = st.builds(
    MARTE_HwCommunication_HwConnection,
)
MARTE_HwCommunication_HwBus_strategy = st.builds(
    MARTE_HwCommunication_HwBus,
)
HwCommunication_HwArbiter_strategy = st.builds(
    HwCommunication_HwArbiter,
)
MARTE_HwStorageManager_HwDMA_strategy = st.builds(
    MARTE_HwStorageManager_HwDMA,
)
HwComputing_PLD_Organization_strategy = st.builds(
    HwComputing_PLD_Organization,
)
NFP_String_strategy = st.builds(
    NFP_String,
)
HwResource_strategy = st.builds(
    HwResource,
)
MARTE_HwComputing_HwBranchPredictor_strategy = st.builds(
    MARTE_HwComputing_HwBranchPredictor,
)
MARTE_HwCommunication_HwCommunicationResource_strategy = st.builds(
    MARTE_HwCommunication_HwCommunicationResource,
)
MARTE_HwLayout_HwComponent_strategy = st.builds(
    MARTE_HwLayout_HwComponent,
    kind=
        safe_text
)
MARTE_HwComputing_HwISA_strategy = st.builds(
    MARTE_HwComputing_HwISA,
    type=
        safe_text
)
NFP_FrequencyInterval_strategy = st.builds(
    NFP_FrequencyInterval,
)
HwGeneral_HwResource_strategy = st.builds(
    HwGeneral_HwResource,
)
MARTE_HwTiming_HwTimingResource_strategy = st.builds(
    MARTE_HwTiming_HwTimingResource,
)
MARTE_HwMemory_HwMemory_strategy = st.builds(
    MARTE_HwMemory_HwMemory,
)
MARTE_HwDevice_HwDevice_strategy = st.builds(
    MARTE_HwDevice_HwDevice,
)
MARTE_HwStorageManager_HwStorageManager_strategy = st.builds(
    MARTE_HwStorageManager_HwStorageManager,
)
HwStorageManager_HwMMU_strategy = st.builds(
    HwStorageManager_HwMMU,
)
HwMemory_HwCache_strategy = st.builds(
    HwMemory_HwCache,
)
HwComputing_HwBranchPredictor_strategy = st.builds(
    HwComputing_HwBranchPredictor,
)
HwMemory_HwRAM_strategy = st.builds(
    HwMemory_HwRAM,
)
HwComputingResource_strategy = st.builds(
    HwComputingResource,
)
MARTE_HwComputing_HwMCU_strategy = st.builds(
    MARTE_HwComputing_HwMCU,
)
MARTE_HwComputing_HwPLD_strategy = st.builds(
    MARTE_HwComputing_HwPLD,
    technology=
        safe_text
)
MARTE_HwComputing_HwASIC_strategy = st.builds(
    MARTE_HwComputing_HwASIC,
)
MARTE_HwComputing_HwProcessor_strategy = st.builds(
    MARTE_HwComputing_HwProcessor,
)
NFP_Natural_strategy = st.builds(
    NFP_Natural,
)
MARTE_HwComputing_PLD_Organization_strategy = st.builds(
    MARTE_HwComputing_PLD_Organization,
    class_=
        safe_text
)
HwComputing_HwISA_strategy = st.builds(
    HwComputing_HwISA,
)
MARTE_HLAM_RtService_strategy = st.builds(
    MARTE_HLAM_RtService,
    concPolicy=
        safe_text,
    isAtomic=
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
    synchKind=
        safe_text
)
NFP_DateTime_strategy = st.builds(
    NFP_DateTime,
)
HLAM_MARTE_Comment_strategy = st.builds(
    HLAM_MARTE_Comment,
)
NFP_Percentage_strategy = st.builds(
    NFP_Percentage,
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
        safe_text
)
Time_TimedInstantObservation_strategy = st.builds(
    Time_TimedInstantObservation,
)
ArrivalPattern_strategy = st.builds(
    ArrivalPattern,
)
UtilityType_strategy = st.builds(
    UtilityType,
)
MARTE_HLAM_RtSpecification_strategy = st.builds(
    MARTE_HLAM_RtSpecification,
)
HLAM_MARTE_Operation_strategy = st.builds(
    HLAM_MARTE_Operation,
)
HLAM_MARTE_Behavior_strategy = st.builds(
    HLAM_MARTE_Behavior,
)
MARTE_HLAM_RtUnit_strategy = st.builds(
    MARTE_HLAM_RtUnit,
    isDynamic=
        safe_text,
    queueSize=
        safe_text,
    isMain=
        safe_text,
    srPoolPolicy=
        safe_text,
    queueSchedPolicy=
        safe_text,
    srPoolSize=
        safe_text
)
GCM_MARTE_BehavioralFeature_strategy = st.builds(
    GCM_MARTE_BehavioralFeature,
)
MARTE_GCM_ClientServerFeature_strategy = st.builds(
    MARTE_GCM_ClientServerFeature,
    kind=
        safe_text
)
GCM_MARTE_Property_strategy = st.builds(
    GCM_MARTE_Property,
)
MARTE_GCM_FlowProperty_strategy = st.builds(
    MARTE_GCM_FlowProperty,
    direction=
        safe_text
)
GCM_ClientServerSpecification_strategy = st.builds(
    GCM_ClientServerSpecification,
)
GCM_MARTE_Interface_strategy = st.builds(
    GCM_MARTE_Interface,
)
MARTE_GCM_ClientServerPort_strategy = st.builds(
    MARTE_GCM_ClientServerPort,
    isConjugated=
        safe_text,
    specificationKind=
        safe_text,
    kind=
        safe_text
)
GCM_MARTE_Port_strategy = st.builds(
    GCM_MARTE_Port,
)
MARTE_GCM_FlowPort_strategy = st.builds(
    MARTE_GCM_FlowPort,
    isConjugated=
        safe_text,
    direction=
        safe_text,
    isAtomic=
        safe_text
)
SwSynchronizationResource_strategy = st.builds(
    SwSynchronizationResource,
)
MARTE_SW_Interaction_NotificationResource_strategy = st.builds(
    MARTE_SW_Interaction_NotificationResource,
    mechanism=
        safe_text,
    occurence=
        safe_text
)
SW_Interaction_SwSynchronizationResource_strategy = st.builds(
    SW_Interaction_SwSynchronizationResource,
)
SW_Interaction_MARTE_BehavioralFeature_strategy = st.builds(
    SW_Interaction_MARTE_BehavioralFeature,
)
SwCommunicationResource_strategy = st.builds(
    SwCommunicationResource,
)
MARTE_SW_Interaction_MessageComResource_strategy = st.builds(
    MARTE_SW_Interaction_MessageComResource,
    mechanism=
        safe_text,
    messageQueuePolicy=
        safe_text,
    isFixedMessageSize=
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
MARTE_SW_Interaction_SwCommunicationResource_strategy = st.builds(
    MARTE_SW_Interaction_SwCommunicationResource,
)
SW_Interaction_MARTE_TypedElement_strategy = st.builds(
    SW_Interaction_MARTE_TypedElement,
)
SW_Brokering_MARTE_Activity_strategy = st.builds(
    SW_Brokering_MARTE_Activity,
)
SW_Brokering_MARTE_Operation_strategy = st.builds(
    SW_Brokering_MARTE_Operation,
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
SW_Concurrency_MARTE_TypedElement_strategy = st.builds(
    SW_Concurrency_MARTE_TypedElement,
)
SW_Concurrency_MARTE_Element_strategy = st.builds(
    SW_Concurrency_MARTE_Element,
)
SwResource_strategy = st.builds(
    SwResource,
)
MARTE_SW_Brokering_DeviceBroker_strategy = st.builds(
    MARTE_SW_Brokering_DeviceBroker,
    name=
        safe_text,
    accessPolicy=
        safe_text,
    isBuffered=
        safe_text
)
MARTE_SW_Concurrency_MemoryPartition_strategy = st.builds(
    MARTE_SW_Concurrency_MemoryPartition,
)
MARTE_SW_Interaction_SwInteractionResource_strategy = st.builds(
    MARTE_SW_Interaction_SwInteractionResource,
    waitingQueuePolicy=
        safe_text,
    isIntraMemoryPartitionInteraction=
        st.booleans(),
    waitingQueueCapacity=
        safe_text
)
MARTE_SW_Brokering_MemoryBroker_strategy = st.builds(
    MARTE_SW_Brokering_MemoryBroker,
    accessPolicy=
        safe_text
)
MARTE_SW_Concurrency_SwConcurrentResource_strategy = st.builds(
    MARTE_SW_Concurrency_SwConcurrentResource,
    activationCapacity=
        safe_text
)
SW_ResourceCore_MARTE_BehavioralFeature_strategy = st.builds(
    SW_ResourceCore_MARTE_BehavioralFeature,
)
SW_ResourceCore_MARTE_TypedElement_strategy = st.builds(
    SW_ResourceCore_MARTE_TypedElement,
)
SW_Concurrency_MARTE_BehavioralFeature_strategy = st.builds(
    SW_Concurrency_MARTE_BehavioralFeature,
)
SW_Brokering_DeviceBroker_strategy = st.builds(
    SW_Brokering_DeviceBroker,
)
MARTE_HwDiagram_SRMDiagram_strategy = st.builds(
    MARTE_HwDiagram_SRMDiagram,
)
SW_ResourceCore_MARTE_Property_strategy = st.builds(
    SW_ResourceCore_MARTE_Property,
)
HwDiagram_MARTE_DataType_strategy = st.builds(
    HwDiagram_MARTE_DataType,
)
MARTE_HwDiagram_HwCircuitDiagram_strategy = st.builds(
    MARTE_HwDiagram_HwCircuitDiagram,
    name=
        safe_text
)
HwCommunication_HwConnection_strategy = st.builds(
    HwCommunication_HwConnection,
)
MARTE_HwDiagram_HwHRMDiagram_strategy = st.builds(
    MARTE_HwDiagram_HwHRMDiagram,
    name=
        safe_text
)
HwPackage_HwWire_strategy = st.builds(
    HwPackage_HwWire,
)
MARTE_HwPackage_HwPackagePin_strategy = st.builds(
    MARTE_HwPackage_HwPackagePin,
    altNames=
        safe_text,
    pinNo=
        safe_text
)
MARTE_HwPackage_HwPackage_strategy = st.builds(
    MARTE_HwPackage_HwPackage,
    pinNum=
        st.integers(),
    name=
        safe_text,
    packageType=
        safe_text
)
MARTE_HwDatasheet_HwDatasheet_strategy = st.builds(
    MARTE_HwDatasheet_HwDatasheet,
    revision=
        safe_text,
    name=
        safe_text
)
MARTE_HwRegister_HwRegister_strategy = st.builds(
    MARTE_HwRegister_HwRegister,
    address=
        safe_text
)
MARTE_HwDiagram_HwBlockDiagram_strategy = st.builds(
    MARTE_HwDiagram_HwBlockDiagram,
    name=
        safe_text
)
HwProtocol_MARTE_Operation_strategy = st.builds(
    HwProtocol_MARTE_Operation,
)
MARTE_HwProtocol_HwProtocol_strategy = st.builds(
    MARTE_HwProtocol_HwProtocol,
    name=
        safe_text
)
MARTE_HwPackage_HwWire_strategy = st.builds(
    MARTE_HwPackage_HwWire,
)
MARTE_HwIO_HwPin_strategy = st.builds(
    MARTE_HwIO_HwPin,
)
MARTE_HwDeviceFunction_HwDeviceFunction_strategy = st.builds(
    MARTE_HwDeviceFunction_HwDeviceFunction,
)
GRM_MARTE_OpaqueExpression_strategy = st.builds(
    GRM_MARTE_OpaqueExpression,
)
ProcessingResource_strategy = st.builds(
    ProcessingResource,
)
MARTE_GRM_ComputingResource_strategy = st.builds(
    MARTE_GRM_ComputingResource,
)
GRM_MARTE_InstanceSpecification_strategy = st.builds(
    GRM_MARTE_InstanceSpecification,
)
GRM_MARTE_Property_strategy = st.builds(
    GRM_MARTE_Property,
)
NFP_Integer_strategy = st.builds(
    NFP_Integer,
)
MARTE_GRM_Resource_strategy = st.builds(
    MARTE_GRM_Resource,
    isProtected=
        safe_text
)
Time_MARTE_Event_strategy = st.builds(
    Time_MARTE_Event,
)
Time_MARTE_Message_strategy = st.builds(
    Time_MARTE_Message,
)
Time_MARTE_Behavior_strategy = st.builds(
    Time_MARTE_Behavior,
)
Time_MARTE_Action_strategy = st.builds(
    Time_MARTE_Action,
)
Time_MARTE_TimeEvent_strategy = st.builds(
    Time_MARTE_TimeEvent,
)
Resource_strategy = st.builds(
    Resource,
)
MARTE_SW_ResourceCore_SwResource_strategy = st.builds(
    MARTE_SW_ResourceCore_SwResource,
)
MARTE_GRM_Scheduler_strategy = st.builds(
    MARTE_GRM_Scheduler,
    isPreemptible=
        safe_text,
    schedPolicy=
        safe_text,
    otherSchedPolicy=
        safe_text
)
MARTE_GRM_SynchronizationResource_strategy = st.builds(
    MARTE_GRM_SynchronizationResource,
)
MARTE_GRM_CommunicationEndPoint_strategy = st.builds(
    MARTE_GRM_CommunicationEndPoint,
)
MARTE_PAM_PaLogicalResource_strategy = st.builds(
    MARTE_PAM_PaLogicalResource,
)
MARTE_HwGeneral_HwResource_strategy = st.builds(
    MARTE_HwGeneral_HwResource,
    name=
        safe_text
)
MARTE_GRM_ConcurrencyResource_strategy = st.builds(
    MARTE_GRM_ConcurrencyResource,
)
MARTE_GRM_MutualExclusionResource_strategy = st.builds(
    MARTE_GRM_MutualExclusionResource,
    protectKind=
        safe_text,
    otherProtectProtocol=
        safe_text
)
MARTE_GRM_StorageResource_strategy = st.builds(
    MARTE_GRM_StorageResource,
)
GRM_MARTE_ConnectableElement_strategy = st.builds(
    GRM_MARTE_ConnectableElement,
)
GRM_MARTE_Lifeline_strategy = st.builds(
    GRM_MARTE_Lifeline,
)
GRM_MARTE_Classifier_strategy = st.builds(
    GRM_MARTE_Classifier,
)
TimedObservation_strategy = st.builds(
    TimedObservation,
)
MARTE_Time_TimedInstantObservation_strategy = st.builds(
    MARTE_Time_TimedInstantObservation,
    obsKind=
        safe_text
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
MARTE_Time_TimedObservation_strategy = st.builds(
    MARTE_Time_TimedObservation,
)
MARTE_Time_TimedProcessing_strategy = st.builds(
    MARTE_Time_TimedProcessing,
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
MARTE_Time_TimedEvent_strategy = st.builds(
    MARTE_Time_TimedEvent,
    repetition=
        safe_text
)
Time_MARTE_DurationObservation_strategy = st.builds(
    Time_MARTE_DurationObservation,
)
MARTE_Time_TimedDurationObservation_strategy = st.builds(
    MARTE_Time_TimedDurationObservation,
    obsKind=
        safe_text
)
Time_MARTE_TimeObservation_strategy = st.builds(
    Time_MARTE_TimeObservation,
)
Time_MARTE_Enumeration_strategy = st.builds(
    Time_MARTE_Enumeration,
)
MARTE_Time_ClockType_strategy = st.builds(
    MARTE_Time_ClockType,
    isLogical=
        safe_text,
    nature=
        safe_text
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
MARTE_Alloc_Allocate_strategy = st.builds(
    MARTE_Alloc_Allocate,
    kind=
        safe_text,
    nature=
        safe_text
)
Time_MARTE_Operation_strategy = st.builds(
    Time_MARTE_Operation,
)
MARTE_Alloc_Assign_strategy = st.builds(
    MARTE_Alloc_Assign,
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
    isPrecedenceBased=
        st.booleans(),
    isCoincidenceBased=
        safe_text,
    isChronometricBased=
        safe_text
)
Alloc_MARTE_Dependency_strategy = st.builds(
    Alloc_MARTE_Dependency,
)
MARTE_Alloc_NfpRefine_strategy = st.builds(
    MARTE_Alloc_NfpRefine,
)
Alloc_MARTE_ActivityPartition_strategy = st.builds(
    Alloc_MARTE_ActivityPartition,
)
MARTE_Alloc_AllocateActivityGroup_strategy = st.builds(
    MARTE_Alloc_AllocateActivityGroup,
)
Alloc_Allocated_strategy = st.builds(
    Alloc_Allocated,
)
Alloc_MARTE_NamedElement_strategy = st.builds(
    Alloc_MARTE_NamedElement,
)
MARTE_Alloc_Allocated_strategy = st.builds(
    MARTE_Alloc_Allocated,
)
CoreElements_MARTE_State_strategy = st.builds(
    CoreElements_MARTE_State,
)
MARTE_CoreElements_Mode_strategy = st.builds(
    MARTE_CoreElements_Mode,
)
Alloc_MARTE_Comment_strategy = st.builds(
    Alloc_MARTE_Comment,
)
Alloc_MARTE_Element_strategy = st.builds(
    Alloc_MARTE_Element,
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
    symbol=
        safe_text,
    baseExponent=
        st.integers()
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
MARTE_NFPs_Nfp_strategy = st.builds(
    MARTE_NFPs_Nfp,
)
NFPs_Unit_strategy = st.builds(
    NFPs_Unit,
)
MARTE_NFPs_Unit_strategy = st.builds(
    MARTE_NFPs_Unit,
    convFactor=
        safe_text,
    offsetFactor=
        safe_text
)
NFPs_MARTE_Property_strategy = st.builds(
    NFPs_MARTE_Property,
)
MARTE_DataTypes_TupleType_strategy = st.builds(
    MARTE_DataTypes_TupleType,
)
MARTE_DataTypes_ChoiceType_strategy = st.builds(
    MARTE_DataTypes_ChoiceType,
)
HLAM_MARTE_BehavioredClassifier_strategy = st.builds(
    HLAM_MARTE_BehavioredClassifier,
)
DataTypes_MARTE_Property_strategy = st.builds(
    DataTypes_MARTE_Property,
)
MARTE_DataTypes_BoundedSubtype_strategy = st.builds(
    MARTE_DataTypes_BoundedSubtype,
    maxValue=
        safe_text,
    isMinOpen=
        st.booleans(),
    isMaxOpen=
        st.booleans(),
    minValue=
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
)
RSM_MARTE_ConnectorEnd_strategy = st.builds(
    RSM_MARTE_ConnectorEnd,
)
MARTE_DataTypes_CollectionType_strategy = st.builds(
    MARTE_DataTypes_CollectionType,
)
MARTE_DataTypes_IntervalType_strategy = st.builds(
    MARTE_DataTypes_IntervalType,
)
DataTypes_MARTE_DataType_strategy = st.builds(
    DataTypes_MARTE_DataType,
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
MARTE_SW_Concurrency_EntryPoint_strategy = st.builds(
    MARTE_SW_Concurrency_EntryPoint,
    isReentrant=
        safe_text
)
MARTE_RSM_Distribute_strategy = st.builds(
    MARTE_RSM_Distribute,
)
IntegerVector_strategy = st.builds(
    IntegerVector,
)
LinkTopology_strategy = st.builds(
    LinkTopology,
)
MARTE_RSM_Reshape_strategy = st.builds(
    MARTE_RSM_Reshape,
)
MARTE_RSM_InterRepetition_strategy = st.builds(
    MARTE_RSM_InterRepetition,
    isModulo=
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
IntegerMatrix_strategy = st.builds(
    IntegerMatrix,
)
MARTE_RSM_Tiler_strategy = st.builds(
    MARTE_RSM_Tiler,
)
NFP_Energy_strategy = st.builds(
    NFP_Energy,
)
NFP_Power_strategy = st.builds(
    NFP_Power,
)
NFP_DataSize_strategy = st.builds(
    NFP_DataSize,
)
MARTE_GRM_ResourceUsage_strategy = st.builds(
    MARTE_GRM_ResourceUsage,
)
GrService_strategy = st.builds(
    GrService,
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
MARTE_HwGeneral_HwResourceService_strategy = st.builds(
    MARTE_HwGeneral_HwResourceService,
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
GRM_ResourceUsage_strategy = st.builds(
    GRM_ResourceUsage,
)
MARTE_GQAM_GaScenario_strategy = st.builds(
    MARTE_GQAM_GaScenario,
)
GRM_MARTE_NamedElement_strategy = st.builds(
    GRM_MARTE_NamedElement,
)
MARTE_GRM_DeviceResource_strategy = st.builds(
    MARTE_GRM_DeviceResource,
)
NFP_DataTxRate_strategy = st.builds(
    NFP_DataTxRate,
)
NFP_Duration_strategy = st.builds(
    NFP_Duration,
)
GRM_MARTE_Connector_strategy = st.builds(
    GRM_MARTE_Connector,
)
MARTE_GRM_CommunicationMedia_strategy = st.builds(
    MARTE_GRM_CommunicationMedia,
    transmMode=
        safe_text
)
Scheduler_strategy = st.builds(
    Scheduler,
)
MARTE_GRM_SecondaryScheduler_strategy = st.builds(
    MARTE_GRM_SecondaryScheduler,
)
GRM_SecondaryScheduler_strategy = st.builds(
    GRM_SecondaryScheduler,
)
SchedParameters_strategy = st.builds(
    SchedParameters,
)
MARTE_GRM_SchedulableResource_strategy = st.builds(
    MARTE_GRM_SchedulableResource,
)
TimingResource_strategy = st.builds(
    TimingResource,
)
MARTE_GRM_TimerResource_strategy = st.builds(
    MARTE_GRM_TimerResource,
    isPeriodic=
        safe_text
)
MARTE_GRM_ClockResource_strategy = st.builds(
    MARTE_GRM_ClockResource,
)
MARTE_GRM_TimingResource_strategy = st.builds(
    MARTE_GRM_TimingResource,
)
GRM_Scheduler_strategy = st.builds(
    GRM_Scheduler,
)
MARTE_GQAM_GaCommHost_strategy = st.builds(
    MARTE_GQAM_GaCommHost,
)
NFP_Real_strategy = st.builds(
    NFP_Real,
)
MARTE_GRM_ProcessingResource_strategy = st.builds(
    MARTE_GRM_ProcessingResource,
)
GRM_SchedulableResource_strategy = st.builds(
    GRM_SchedulableResource,
)
MARTE_SW_Concurrency_SwSchedulableResource_strategy = st.builds(
    MARTE_SW_Concurrency_SwSchedulableResource,
    isPreemptable=
        safe_text,
    isStaticSchedulingFeature=
        safe_text
)
GRM_MutualExclusionResource_strategy = st.builds(
    GRM_MutualExclusionResource,
)
MARTE_SW_Interaction_SwMutualExclusionResource_strategy = st.builds(
    MARTE_SW_Interaction_SwMutualExclusionResource,
    mechanism=
        safe_text,
    concurrentAccessProtocol=
        safe_text
)
GRM_ComputingResource_strategy = st.builds(
    GRM_ComputingResource,
)
MARTE_HwComputing_HwComputingResource_strategy = st.builds(
    MARTE_HwComputing_HwComputingResource,
)
MARTE_GQAM_GaExecHost_strategy = st.builds(
    MARTE_GQAM_GaExecHost,
)
GRM_ProcessingResource_strategy = st.builds(
    GRM_ProcessingResource,
)

@given(instance=PAM_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_pam_marte_namedelement_instantiation(instance):
    assert isinstance(instance, PAM_MARTE_NamedElement)

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

@given(instance=MARTE_PAM_PaRunTInstance_strategy)
@settings(max_examples=50)
def test_marte_pam_paruntinstance_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaRunTInstance)



@given(instance=MARTE_PAM_PaRunTInstance_strategy)
def test_marte_pam_paruntinstance_unbddPool_setter(instance):
    original = instance.unbddPool
    instance.unbddPool = original
    assert instance.unbddPool == original

@given(instance=GaExecHost_strategy)
@settings(max_examples=50)
def test_gaexechost_instantiation(instance):
    assert isinstance(instance, GaExecHost)

@given(instance=MARTE_SAM_SaExecHost_strategy)
@settings(max_examples=50)
def test_marte_sam_saexechost_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaExecHost)

@given(instance=MutualExclusionResource_strategy)
@settings(max_examples=50)
def test_mutualexclusionresource_instantiation(instance):
    assert isinstance(instance, MutualExclusionResource)

@given(instance=MARTE_SAM_SaSharedResource_strategy)
@settings(max_examples=50)
def test_marte_sam_sasharedresource_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaSharedResource)

@given(instance=GaCommHost_strategy)
@settings(max_examples=50)
def test_gacommhost_instantiation(instance):
    assert isinstance(instance, GaCommHost)

@given(instance=MARTE_SAM_SaCommHost_strategy)
@settings(max_examples=50)
def test_marte_sam_sacommhost_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaCommHost)

@given(instance=SAM_MARTE_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sam_marte_behavioralfeature_instantiation(instance):
    assert isinstance(instance, SAM_MARTE_BehavioralFeature)

@given(instance=SAM_SaSharedResource_strategy)
@settings(max_examples=50)
def test_sam_sasharedresource_instantiation(instance):
    assert isinstance(instance, SAM_SaSharedResource)

@given(instance=GaAnalysisContext_strategy)
@settings(max_examples=50)
def test_gaanalysiscontext_instantiation(instance):
    assert isinstance(instance, GaAnalysisContext)

@given(instance=MARTE_SAM_SaAnalysisContext_strategy)
@settings(max_examples=50)
def test_marte_sam_saanalysiscontext_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaAnalysisContext)



@given(instance=MARTE_SAM_SaAnalysisContext_strategy)
def test_marte_sam_saanalysiscontext_optCriterion_setter(instance):
    original = instance.optCriterion
    instance.optCriterion = original
    assert instance.optCriterion == original

@given(instance=GQAM_MARTE_Classifier_strategy)
@settings(max_examples=50)
def test_gqam_marte_classifier_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_Classifier)

@given(instance=GaCommStep_strategy)
@settings(max_examples=50)
def test_gacommstep_instantiation(instance):
    assert isinstance(instance, GaCommStep)

@given(instance=MARTE_SAM_SaCommStep_strategy)
@settings(max_examples=50)
def test_marte_sam_sacommstep_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaCommStep)

@given(instance=SAM_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_sam_marte_namedelement_instantiation(instance):
    assert isinstance(instance, SAM_MARTE_NamedElement)

@given(instance=MARTE_SAM_SaEndtoEndFlow_strategy)
@settings(max_examples=50)
def test_marte_sam_saendtoendflow_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaEndtoEndFlow)

@given(instance=SchedulableResource_strategy)
@settings(max_examples=50)
def test_schedulableresource_instantiation(instance):
    assert isinstance(instance, SchedulableResource)

@given(instance=MARTE_GQAM_GaCommChannel_strategy)
@settings(max_examples=50)
def test_marte_gqam_gacommchannel_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaCommChannel)

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

@given(instance=MARTE_GQAM_GaWorkloadBehavior_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaworkloadbehavior_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaWorkloadBehavior)

@given(instance=GaTimedObs_strategy)
@settings(max_examples=50)
def test_gatimedobs_instantiation(instance):
    assert isinstance(instance, GaTimedObs)

@given(instance=MARTE_SAM_SaSchedObs_strategy)
@settings(max_examples=50)
def test_marte_sam_saschedobs_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaSchedObs)

@given(instance=MARTE_GQAM_GaLatencyObs_strategy)
@settings(max_examples=50)
def test_marte_gqam_galatencyobs_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaLatencyObs)

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

@given(instance=MARTE_GQAM_GaCommStep_strategy)
@settings(max_examples=50)
def test_marte_gqam_gacommstep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaCommStep)

@given(instance=MARTE_PAM_PaResPassStep_strategy)
@settings(max_examples=50)
def test_marte_pam_parespassstep_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaResPassStep)

@given(instance=MARTE_PAM_PaStep_strategy)
@settings(max_examples=50)
def test_marte_pam_pastep_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaStep)



@given(instance=MARTE_PAM_PaStep_strategy)
def test_marte_pam_pastep_extOpDemand_setter(instance):
    original = instance.extOpDemand
    instance.extOpDemand = original
    assert instance.extOpDemand == original

@given(instance=MARTE_SAM_SaStep_strategy)
@settings(max_examples=50)
def test_marte_sam_sastep_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaStep)

@given(instance=MARTE_GQAM_GaAcqStep_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaacqstep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaAcqStep)

@given(instance=MARTE_GQAM_GaRelStep_strategy)
@settings(max_examples=50)
def test_marte_gqam_garelstep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaRelStep)

@given(instance=MARTE_GQAM_GaRequestedService_strategy)
@settings(max_examples=50)
def test_marte_gqam_garequestedservice_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaRequestedService)

@given(instance=IntegerInterval_strategy)
@settings(max_examples=50)
def test_integerinterval_instantiation(instance):
    assert isinstance(instance, IntegerInterval)

@given(instance=GaScenario_strategy)
@settings(max_examples=50)
def test_gascenario_instantiation(instance):
    assert isinstance(instance, GaScenario)

@given(instance=MARTE_GQAM_GaStep_strategy)
@settings(max_examples=50)
def test_marte_gqam_gastep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaStep)

@given(instance=GQAM_GaTimedObs_strategy)
@settings(max_examples=50)
def test_gqam_gatimedobs_instantiation(instance):
    assert isinstance(instance, GQAM_GaTimedObs)

@given(instance=GQAM_GaStep_strategy)
@settings(max_examples=50)
def test_gqam_gastep_instantiation(instance):
    assert isinstance(instance, GQAM_GaStep)

@given(instance=GQAM_GaRequestedService_strategy)
@settings(max_examples=50)
def test_gqam_garequestedservice_instantiation(instance):
    assert isinstance(instance, GQAM_GaRequestedService)

@given(instance=MARTE_PAM_PaRequestedStep_strategy)
@settings(max_examples=50)
def test_marte_pam_parequestedstep_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaRequestedStep)

@given(instance=GQAM_GaExecHost_strategy)
@settings(max_examples=50)
def test_gqam_gaexechost_instantiation(instance):
    assert isinstance(instance, GQAM_GaExecHost)

@given(instance=GQAM_GaWorkloadEvent_strategy)
@settings(max_examples=50)
def test_gqam_gaworkloadevent_instantiation(instance):
    assert isinstance(instance, GQAM_GaWorkloadEvent)

@given(instance=Time_TimedProcessing_strategy)
@settings(max_examples=50)
def test_time_timedprocessing_instantiation(instance):
    assert isinstance(instance, Time_TimedProcessing)

@given(instance=MARTE_GQAM_GaWorkloadGenerator_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaworkloadgenerator_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaWorkloadGenerator)

@given(instance=GCM_MARTE_Behavior_strategy)
@settings(max_examples=50)
def test_gcm_marte_behavior_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Behavior)

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

@given(instance=GQAM_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_gqam_marte_namedelement_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_NamedElement)

@given(instance=MARTE_GQAM_GaEventTrace_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaeventtrace_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaEventTrace)



@given(instance=MARTE_GQAM_GaEventTrace_strategy)
def test_marte_gqam_gaeventtrace_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original



@given(instance=MARTE_GQAM_GaEventTrace_strategy)
def test_marte_gqam_gaeventtrace_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=MARTE_GQAM_GaEventTrace_strategy)
def test_marte_gqam_gaeventtrace_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=GQAM_MARTE_Behavior_strategy)
@settings(max_examples=50)
def test_gqam_marte_behavior_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_Behavior)

@given(instance=MARTE_GCM_FlowSpecification_strategy)
@settings(max_examples=50)
def test_marte_gcm_flowspecification_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_FlowSpecification)

@given(instance=MARTE_GCM_ClientServerSpecification_strategy)
@settings(max_examples=50)
def test_marte_gcm_clientserverspecification_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_ClientServerSpecification)

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

@given(instance=GCM_MARTE_Trigger_strategy)
@settings(max_examples=50)
def test_gcm_marte_trigger_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Trigger)

@given(instance=MARTE_GCM_GCMTrigger_strategy)
@settings(max_examples=50)
def test_marte_gcm_gcmtrigger_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_GCMTrigger)

@given(instance=HwPeripheral_RegisterAction_strategy)
@settings(max_examples=50)
def test_hwperipheral_registeraction_instantiation(instance):
    assert isinstance(instance, HwPeripheral_RegisterAction)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=MARTE_HwPeripheral_PeripheralActivity_strategy)
@settings(max_examples=50)
def test_marte_hwperipheral_peripheralactivity_instantiation(instance):
    assert isinstance(instance, MARTE_HwPeripheral_PeripheralActivity)

@given(instance=HwPeripheral_MARTE_OutputPin_strategy)
@settings(max_examples=50)
def test_hwperipheral_marte_outputpin_instantiation(instance):
    assert isinstance(instance, HwPeripheral_MARTE_OutputPin)

@given(instance=HwPeripheral_MARTE_InputPin_strategy)
@settings(max_examples=50)
def test_hwperipheral_marte_inputpin_instantiation(instance):
    assert isinstance(instance, HwPeripheral_MARTE_InputPin)

@given(instance=RegisterAction_strategy)
@settings(max_examples=50)
def test_registeraction_instantiation(instance):
    assert isinstance(instance, RegisterAction)

@given(instance=MARTE_HwPeripheral_ReadRegisterAction_strategy)
@settings(max_examples=50)
def test_marte_hwperipheral_readregisteraction_instantiation(instance):
    assert isinstance(instance, MARTE_HwPeripheral_ReadRegisterAction)

@given(instance=MARTE_HwPeripheral_WriteRegisterAction_strategy)
@settings(max_examples=50)
def test_marte_hwperipheral_writeregisteraction_instantiation(instance):
    assert isinstance(instance, MARTE_HwPeripheral_WriteRegisterAction)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=MARTE_HwPeripheral_RegisterAction_strategy)
@settings(max_examples=50)
def test_marte_hwperipheral_registeraction_instantiation(instance):
    assert isinstance(instance, MARTE_HwPeripheral_RegisterAction)

@given(instance=HwPeripheral_MARTE_Operation_strategy)
@settings(max_examples=50)
def test_hwperipheral_marte_operation_instantiation(instance):
    assert isinstance(instance, HwPeripheral_MARTE_Operation)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=MARTE_HwPeripheral_OperationImpl_strategy)
@settings(max_examples=50)
def test_marte_hwperipheral_operationimpl_instantiation(instance):
    assert isinstance(instance, MARTE_HwPeripheral_OperationImpl)

@given(instance=HwIO_HwLine_strategy)
@settings(max_examples=50)
def test_hwio_hwline_instantiation(instance):
    assert isinstance(instance, HwIO_HwLine)

@given(instance=HwPackage_HwPackagePin_strategy)
@settings(max_examples=50)
def test_hwpackage_hwpackagepin_instantiation(instance):
    assert isinstance(instance, HwPackage_HwPackagePin)

@given(instance=HwComponent_strategy)
@settings(max_examples=50)
def test_hwcomponent_instantiation(instance):
    assert isinstance(instance, HwComponent)

@given(instance=MARTE_HwPower_HwPowerSupply_strategy)
@settings(max_examples=50)
def test_marte_hwpower_hwpowersupply_instantiation(instance):
    assert isinstance(instance, MARTE_HwPower_HwPowerSupply)

@given(instance=MARTE_HwPower_HwCoolingSupply_strategy)
@settings(max_examples=50)
def test_marte_hwpower_hwcoolingsupply_instantiation(instance):
    assert isinstance(instance, MARTE_HwPower_HwCoolingSupply)

@given(instance=MARTE_HwLayout_Env_Condition_strategy)
@settings(max_examples=50)
def test_marte_hwlayout_env_condition_instantiation(instance):
    assert isinstance(instance, MARTE_HwLayout_Env_Condition)



@given(instance=MARTE_HwLayout_Env_Condition_strategy)
def test_marte_hwlayout_env_condition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MARTE_HwLayout_Env_Condition_strategy)
def test_marte_hwlayout_env_condition_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=HwLayout_HwComponent_strategy)
@settings(max_examples=50)
def test_hwlayout_hwcomponent_instantiation(instance):
    assert isinstance(instance, HwLayout_HwComponent)

@given(instance=HwLayout_Env_Condition_strategy)
@settings(max_examples=50)
def test_hwlayout_env_condition_instantiation(instance):
    assert isinstance(instance, HwLayout_Env_Condition)

@given(instance=NFP_Price_strategy)
@settings(max_examples=50)
def test_nfp_price_instantiation(instance):
    assert isinstance(instance, NFP_Price)

@given(instance=Realnterval_strategy)
@settings(max_examples=50)
def test_realnterval_instantiation(instance):
    assert isinstance(instance, Realnterval)

@given(instance=NFP_Length_strategy)
@settings(max_examples=50)
def test_nfp_length_instantiation(instance):
    assert isinstance(instance, NFP_Length)

@given(instance=HwGeneral_MARTE_Activity_strategy)
@settings(max_examples=50)
def test_hwgeneral_marte_activity_instantiation(instance):
    assert isinstance(instance, HwGeneral_MARTE_Activity)

@given(instance=HwGeneral_MARTE_Operation_strategy)
@settings(max_examples=50)
def test_hwgeneral_marte_operation_instantiation(instance):
    assert isinstance(instance, HwGeneral_MARTE_Operation)

@given(instance=NFP_Frequency_strategy)
@settings(max_examples=50)
def test_nfp_frequency_instantiation(instance):
    assert isinstance(instance, NFP_Frequency)

@given(instance=HwCommunication_HwEndPoint_strategy)
@settings(max_examples=50)
def test_hwcommunication_hwendpoint_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwEndPoint)

@given(instance=HwGeneral_HwResourceService_strategy)
@settings(max_examples=50)
def test_hwgeneral_hwresourceservice_instantiation(instance):
    assert isinstance(instance, HwGeneral_HwResourceService)

@given(instance=NFP_NaturalInterval_strategy)
@settings(max_examples=50)
def test_nfp_naturalinterval_instantiation(instance):
    assert isinstance(instance, NFP_NaturalInterval)

@given(instance=NFP_Area_strategy)
@settings(max_examples=50)
def test_nfp_area_instantiation(instance):
    assert isinstance(instance, NFP_Area)

@given(instance=HwPeripheral_PeripheralActivity_strategy)
@settings(max_examples=50)
def test_hwperipheral_peripheralactivity_instantiation(instance):
    assert isinstance(instance, HwPeripheral_PeripheralActivity)

@given(instance=HwPeripheral_OperationImpl_strategy)
@settings(max_examples=50)
def test_hwperipheral_operationimpl_instantiation(instance):
    assert isinstance(instance, HwPeripheral_OperationImpl)

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

@given(instance=HwDevice_strategy)
@settings(max_examples=50)
def test_hwdevice_instantiation(instance):
    assert isinstance(instance, HwDevice)

@given(instance=MARTE_HwDevice_HwSupport_strategy)
@settings(max_examples=50)
def test_marte_hwdevice_hwsupport_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HwSupport)

@given(instance=MARTE_HwDevice_HwPeripheral_strategy)
@settings(max_examples=50)
def test_marte_hwdevice_hwperipheral_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HwPeripheral)

@given(instance=MARTE_HwDevice_HwI_O_strategy)
@settings(max_examples=50)
def test_marte_hwdevice_hwi_o_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HwI_O)

@given(instance=HwTimingResource_strategy)
@settings(max_examples=50)
def test_hwtimingresource_instantiation(instance):
    assert isinstance(instance, HwTimingResource)

@given(instance=MARTE_HwTiming_HwTimer_strategy)
@settings(max_examples=50)
def test_marte_hwtiming_hwtimer_instantiation(instance):
    assert isinstance(instance, MARTE_HwTiming_HwTimer)

@given(instance=MARTE_HwTiming_HwClock_strategy)
@settings(max_examples=50)
def test_marte_hwtiming_hwclock_instantiation(instance):
    assert isinstance(instance, MARTE_HwTiming_HwClock)

@given(instance=GRM_TimingResource_strategy)
@settings(max_examples=50)
def test_grm_timingresource_instantiation(instance):
    assert isinstance(instance, GRM_TimingResource)

@given(instance=HwMemory_CacheStructure_strategy)
@settings(max_examples=50)
def test_hwmemory_cachestructure_instantiation(instance):
    assert isinstance(instance, HwMemory_CacheStructure)

@given(instance=HwDeviceFunction_HwDeviceFunction_strategy)
@settings(max_examples=50)
def test_hwdevicefunction_hwdevicefunction_instantiation(instance):
    assert isinstance(instance, HwDeviceFunction_HwDeviceFunction)

@given(instance=GRM_DeviceResource_strategy)
@settings(max_examples=50)
def test_grm_deviceresource_instantiation(instance):
    assert isinstance(instance, GRM_DeviceResource)

@given(instance=HwTiming_HwClock_strategy)
@settings(max_examples=50)
def test_hwtiming_hwclock_instantiation(instance):
    assert isinstance(instance, HwTiming_HwClock)

@given(instance=HwMemory_MemoryOrganization_strategy)
@settings(max_examples=50)
def test_hwmemory_memoryorganization_instantiation(instance):
    assert isinstance(instance, HwMemory_MemoryOrganization)

@given(instance=HwMemory_strategy)
@settings(max_examples=50)
def test_hwmemory_instantiation(instance):
    assert isinstance(instance, HwMemory)

@given(instance=MARTE_HwMemory_HwCache_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_hwcache_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwCache)



@given(instance=MARTE_HwMemory_HwCache_strategy)
def test_marte_hwmemory_hwcache_repl_Policy_setter(instance):
    original = instance.repl_Policy
    instance.repl_Policy = original
    assert instance.repl_Policy == original



@given(instance=MARTE_HwMemory_HwCache_strategy)
def test_marte_hwmemory_hwcache_writePolicy_setter(instance):
    original = instance.writePolicy
    instance.writePolicy = original
    assert instance.writePolicy == original



@given(instance=MARTE_HwMemory_HwCache_strategy)
def test_marte_hwmemory_hwcache_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MARTE_HwMemory_HwDrive_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_hwdrive_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwDrive)

@given(instance=MARTE_HwMemory_HwRAM_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_hwram_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwRAM)



@given(instance=MARTE_HwMemory_HwRAM_strategy)
def test_marte_hwmemory_hwram_repl_Policy_setter(instance):
    original = instance.repl_Policy
    instance.repl_Policy = original
    assert instance.repl_Policy == original



@given(instance=MARTE_HwMemory_HwRAM_strategy)
def test_marte_hwmemory_hwram_writePolicy_setter(instance):
    original = instance.writePolicy
    instance.writePolicy = original
    assert instance.writePolicy == original

@given(instance=MARTE_HwMemory_MemoryOrganization_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_memoryorganization_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_MemoryOrganization)

@given(instance=MARTE_HwMemory_CacheStructure_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_cachestructure_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_CacheStructure)

@given(instance=MARTE_HwMemory_HwROM_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_hwrom_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwROM)



@given(instance=MARTE_HwMemory_HwROM_strategy)
def test_marte_hwmemory_hwrom_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MARTE_HwMemory_Timing_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_timing_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_Timing)

@given(instance=HwMemory_Timing_strategy)
@settings(max_examples=50)
def test_hwmemory_timing_instantiation(instance):
    assert isinstance(instance, HwMemory_Timing)

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

@given(instance=HwProtocol_HwProtocol_strategy)
@settings(max_examples=50)
def test_hwprotocol_hwprotocol_instantiation(instance):
    assert isinstance(instance, HwProtocol_HwProtocol)

@given(instance=HwEndPoint_strategy)
@settings(max_examples=50)
def test_hwendpoint_instantiation(instance):
    assert isinstance(instance, HwEndPoint)

@given(instance=MARTE_HwCommunication_HwPort_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwport_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwPort)

@given(instance=GRM_CommunicationEndPoint_strategy)
@settings(max_examples=50)
def test_grm_communicationendpoint_instantiation(instance):
    assert isinstance(instance, GRM_CommunicationEndPoint)

@given(instance=NFP_Boolean_strategy)
@settings(max_examples=50)
def test_nfp_boolean_instantiation(instance):
    assert isinstance(instance, NFP_Boolean)

@given(instance=HwStorageManager_strategy)
@settings(max_examples=50)
def test_hwstoragemanager_instantiation(instance):
    assert isinstance(instance, HwStorageManager)

@given(instance=MARTE_HwStorageManager_HwMMU_strategy)
@settings(max_examples=50)
def test_marte_hwstoragemanager_hwmmu_instantiation(instance):
    assert isinstance(instance, MARTE_HwStorageManager_HwMMU)

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

@given(instance=MARTE_HwCommunication_HwMedia_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwmedia_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwMedia)

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

@given(instance=HwCommunication_HwPort_strategy)
@settings(max_examples=50)
def test_hwcommunication_hwport_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwPort)

@given(instance=HwIO_HwPin_strategy)
@settings(max_examples=50)
def test_hwio_hwpin_instantiation(instance):
    assert isinstance(instance, HwIO_HwPin)

@given(instance=HwPackage_HwPackage_strategy)
@settings(max_examples=50)
def test_hwpackage_hwpackage_instantiation(instance):
    assert isinstance(instance, HwPackage_HwPackage)

@given(instance=HwRegister_HwRegister_strategy)
@settings(max_examples=50)
def test_hwregister_hwregister_instantiation(instance):
    assert isinstance(instance, HwRegister_HwRegister)

@given(instance=HwDevice_HwPeripheral_strategy)
@settings(max_examples=50)
def test_hwdevice_hwperipheral_instantiation(instance):
    assert isinstance(instance, HwDevice_HwPeripheral)

@given(instance=HwComputing_HwProcessor_strategy)
@settings(max_examples=50)
def test_hwcomputing_hwprocessor_instantiation(instance):
    assert isinstance(instance, HwComputing_HwProcessor)

@given(instance=HwComputing_HwComputingResource_strategy)
@settings(max_examples=50)
def test_hwcomputing_hwcomputingresource_instantiation(instance):
    assert isinstance(instance, HwComputing_HwComputingResource)

@given(instance=HwMedia_strategy)
@settings(max_examples=50)
def test_hwmedia_instantiation(instance):
    assert isinstance(instance, HwMedia)

@given(instance=MARTE_HwIO_HwLine_strategy)
@settings(max_examples=50)
def test_marte_hwio_hwline_instantiation(instance):
    assert isinstance(instance, MARTE_HwIO_HwLine)

@given(instance=MARTE_HwCommunication_HwBridge_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwbridge_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwBridge)

@given(instance=MARTE_HwCommunication_HwConnection_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwconnection_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwConnection)

@given(instance=MARTE_HwCommunication_HwBus_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwbus_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwBus)

@given(instance=HwCommunication_HwArbiter_strategy)
@settings(max_examples=50)
def test_hwcommunication_hwarbiter_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwArbiter)

@given(instance=MARTE_HwStorageManager_HwDMA_strategy)
@settings(max_examples=50)
def test_marte_hwstoragemanager_hwdma_instantiation(instance):
    assert isinstance(instance, MARTE_HwStorageManager_HwDMA)

@given(instance=HwComputing_PLD_Organization_strategy)
@settings(max_examples=50)
def test_hwcomputing_pld_organization_instantiation(instance):
    assert isinstance(instance, HwComputing_PLD_Organization)

@given(instance=NFP_String_strategy)
@settings(max_examples=50)
def test_nfp_string_instantiation(instance):
    assert isinstance(instance, NFP_String)

@given(instance=HwResource_strategy)
@settings(max_examples=50)
def test_hwresource_instantiation(instance):
    assert isinstance(instance, HwResource)

@given(instance=MARTE_HwComputing_HwBranchPredictor_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwbranchpredictor_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwBranchPredictor)

@given(instance=MARTE_HwCommunication_HwCommunicationResource_strategy)
@settings(max_examples=50)
def test_marte_hwcommunication_hwcommunicationresource_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwCommunicationResource)

@given(instance=MARTE_HwLayout_HwComponent_strategy)
@settings(max_examples=50)
def test_marte_hwlayout_hwcomponent_instantiation(instance):
    assert isinstance(instance, MARTE_HwLayout_HwComponent)



@given(instance=MARTE_HwLayout_HwComponent_strategy)
def test_marte_hwlayout_hwcomponent_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MARTE_HwComputing_HwISA_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwisa_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwISA)



@given(instance=MARTE_HwComputing_HwISA_strategy)
def test_marte_hwcomputing_hwisa_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=NFP_FrequencyInterval_strategy)
@settings(max_examples=50)
def test_nfp_frequencyinterval_instantiation(instance):
    assert isinstance(instance, NFP_FrequencyInterval)

@given(instance=HwGeneral_HwResource_strategy)
@settings(max_examples=50)
def test_hwgeneral_hwresource_instantiation(instance):
    assert isinstance(instance, HwGeneral_HwResource)

@given(instance=MARTE_HwTiming_HwTimingResource_strategy)
@settings(max_examples=50)
def test_marte_hwtiming_hwtimingresource_instantiation(instance):
    assert isinstance(instance, MARTE_HwTiming_HwTimingResource)

@given(instance=MARTE_HwMemory_HwMemory_strategy)
@settings(max_examples=50)
def test_marte_hwmemory_hwmemory_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwMemory)

@given(instance=MARTE_HwDevice_HwDevice_strategy)
@settings(max_examples=50)
def test_marte_hwdevice_hwdevice_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HwDevice)

@given(instance=MARTE_HwStorageManager_HwStorageManager_strategy)
@settings(max_examples=50)
def test_marte_hwstoragemanager_hwstoragemanager_instantiation(instance):
    assert isinstance(instance, MARTE_HwStorageManager_HwStorageManager)

@given(instance=HwStorageManager_HwMMU_strategy)
@settings(max_examples=50)
def test_hwstoragemanager_hwmmu_instantiation(instance):
    assert isinstance(instance, HwStorageManager_HwMMU)

@given(instance=HwMemory_HwCache_strategy)
@settings(max_examples=50)
def test_hwmemory_hwcache_instantiation(instance):
    assert isinstance(instance, HwMemory_HwCache)

@given(instance=HwComputing_HwBranchPredictor_strategy)
@settings(max_examples=50)
def test_hwcomputing_hwbranchpredictor_instantiation(instance):
    assert isinstance(instance, HwComputing_HwBranchPredictor)

@given(instance=HwMemory_HwRAM_strategy)
@settings(max_examples=50)
def test_hwmemory_hwram_instantiation(instance):
    assert isinstance(instance, HwMemory_HwRAM)

@given(instance=HwComputingResource_strategy)
@settings(max_examples=50)
def test_hwcomputingresource_instantiation(instance):
    assert isinstance(instance, HwComputingResource)

@given(instance=MARTE_HwComputing_HwMCU_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwmcu_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwMCU)

@given(instance=MARTE_HwComputing_HwPLD_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwpld_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwPLD)



@given(instance=MARTE_HwComputing_HwPLD_strategy)
def test_marte_hwcomputing_hwpld_technology_setter(instance):
    original = instance.technology
    instance.technology = original
    assert instance.technology == original

@given(instance=MARTE_HwComputing_HwASIC_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwasic_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwASIC)

@given(instance=MARTE_HwComputing_HwProcessor_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwprocessor_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwProcessor)

@given(instance=NFP_Natural_strategy)
@settings(max_examples=50)
def test_nfp_natural_instantiation(instance):
    assert isinstance(instance, NFP_Natural)

@given(instance=MARTE_HwComputing_PLD_Organization_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_pld_organization_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_PLD_Organization)



@given(instance=MARTE_HwComputing_PLD_Organization_strategy)
def test_marte_hwcomputing_pld_organization_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=HwComputing_HwISA_strategy)
@settings(max_examples=50)
def test_hwcomputing_hwisa_instantiation(instance):
    assert isinstance(instance, HwComputing_HwISA)

@given(instance=MARTE_HLAM_RtService_strategy)
@settings(max_examples=50)
def test_marte_hlam_rtservice_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtService)



@given(instance=MARTE_HLAM_RtService_strategy)
def test_marte_hlam_rtservice_concPolicy_setter(instance):
    original = instance.concPolicy
    instance.concPolicy = original
    assert instance.concPolicy == original



@given(instance=MARTE_HLAM_RtService_strategy)
def test_marte_hlam_rtservice_isAtomic_setter(instance):
    original = instance.isAtomic
    instance.isAtomic = original
    assert instance.isAtomic == original



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
def test_marte_hlam_rtaction_synchKind_setter(instance):
    original = instance.synchKind
    instance.synchKind = original
    assert instance.synchKind == original

@given(instance=NFP_DateTime_strategy)
@settings(max_examples=50)
def test_nfp_datetime_instantiation(instance):
    assert isinstance(instance, NFP_DateTime)

@given(instance=HLAM_MARTE_Comment_strategy)
@settings(max_examples=50)
def test_hlam_marte_comment_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Comment)

@given(instance=NFP_Percentage_strategy)
@settings(max_examples=50)
def test_nfp_percentage_instantiation(instance):
    assert isinstance(instance, NFP_Percentage)

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

@given(instance=Time_TimedInstantObservation_strategy)
@settings(max_examples=50)
def test_time_timedinstantobservation_instantiation(instance):
    assert isinstance(instance, Time_TimedInstantObservation)

@given(instance=ArrivalPattern_strategy)
@settings(max_examples=50)
def test_arrivalpattern_instantiation(instance):
    assert isinstance(instance, ArrivalPattern)

@given(instance=UtilityType_strategy)
@settings(max_examples=50)
def test_utilitytype_instantiation(instance):
    assert isinstance(instance, UtilityType)

@given(instance=MARTE_HLAM_RtSpecification_strategy)
@settings(max_examples=50)
def test_marte_hlam_rtspecification_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtSpecification)

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
def test_marte_hlam_rtunit_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_queueSize_setter(instance):
    original = instance.queueSize
    instance.queueSize = original
    assert instance.queueSize == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_isMain_setter(instance):
    original = instance.isMain
    instance.isMain = original
    assert instance.isMain == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_srPoolPolicy_setter(instance):
    original = instance.srPoolPolicy
    instance.srPoolPolicy = original
    assert instance.srPoolPolicy == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_queueSchedPolicy_setter(instance):
    original = instance.queueSchedPolicy
    instance.queueSchedPolicy = original
    assert instance.queueSchedPolicy == original



@given(instance=MARTE_HLAM_RtUnit_strategy)
def test_marte_hlam_rtunit_srPoolSize_setter(instance):
    original = instance.srPoolSize
    instance.srPoolSize = original
    assert instance.srPoolSize == original

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

@given(instance=GCM_MARTE_Property_strategy)
@settings(max_examples=50)
def test_gcm_marte_property_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Property)

@given(instance=MARTE_GCM_FlowProperty_strategy)
@settings(max_examples=50)
def test_marte_gcm_flowproperty_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_FlowProperty)



@given(instance=MARTE_GCM_FlowProperty_strategy)
def test_marte_gcm_flowproperty_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

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
def test_marte_gcm_clientserverport_isConjugated_setter(instance):
    original = instance.isConjugated
    instance.isConjugated = original
    assert instance.isConjugated == original



@given(instance=MARTE_GCM_ClientServerPort_strategy)
def test_marte_gcm_clientserverport_specificationKind_setter(instance):
    original = instance.specificationKind
    instance.specificationKind = original
    assert instance.specificationKind == original



@given(instance=MARTE_GCM_ClientServerPort_strategy)
def test_marte_gcm_clientserverport_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=GCM_MARTE_Port_strategy)
@settings(max_examples=50)
def test_gcm_marte_port_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Port)

@given(instance=MARTE_GCM_FlowPort_strategy)
@settings(max_examples=50)
def test_marte_gcm_flowport_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_FlowPort)



@given(instance=MARTE_GCM_FlowPort_strategy)
def test_marte_gcm_flowport_isConjugated_setter(instance):
    original = instance.isConjugated
    instance.isConjugated = original
    assert instance.isConjugated == original



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

@given(instance=SwSynchronizationResource_strategy)
@settings(max_examples=50)
def test_swsynchronizationresource_instantiation(instance):
    assert isinstance(instance, SwSynchronizationResource)

@given(instance=MARTE_SW_Interaction_NotificationResource_strategy)
@settings(max_examples=50)
def test_marte_sw_interaction_notificationresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_NotificationResource)



@given(instance=MARTE_SW_Interaction_NotificationResource_strategy)
def test_marte_sw_interaction_notificationresource_mechanism_setter(instance):
    original = instance.mechanism
    instance.mechanism = original
    assert instance.mechanism == original



@given(instance=MARTE_SW_Interaction_NotificationResource_strategy)
def test_marte_sw_interaction_notificationresource_occurence_setter(instance):
    original = instance.occurence
    instance.occurence = original
    assert instance.occurence == original

@given(instance=SW_Interaction_SwSynchronizationResource_strategy)
@settings(max_examples=50)
def test_sw_interaction_swsynchronizationresource_instantiation(instance):
    assert isinstance(instance, SW_Interaction_SwSynchronizationResource)

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
def test_marte_sw_interaction_messagecomresource_mechanism_setter(instance):
    original = instance.mechanism
    instance.mechanism = original
    assert instance.mechanism == original



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

@given(instance=MARTE_SW_Interaction_SwCommunicationResource_strategy)
@settings(max_examples=50)
def test_marte_sw_interaction_swcommunicationresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_SwCommunicationResource)

@given(instance=SW_Interaction_MARTE_TypedElement_strategy)
@settings(max_examples=50)
def test_sw_interaction_marte_typedelement_instantiation(instance):
    assert isinstance(instance, SW_Interaction_MARTE_TypedElement)

@given(instance=SW_Brokering_MARTE_Activity_strategy)
@settings(max_examples=50)
def test_sw_brokering_marte_activity_instantiation(instance):
    assert isinstance(instance, SW_Brokering_MARTE_Activity)

@given(instance=SW_Brokering_MARTE_Operation_strategy)
@settings(max_examples=50)
def test_sw_brokering_marte_operation_instantiation(instance):
    assert isinstance(instance, SW_Brokering_MARTE_Operation)

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

@given(instance=SW_Concurrency_MARTE_TypedElement_strategy)
@settings(max_examples=50)
def test_sw_concurrency_marte_typedelement_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_TypedElement)

@given(instance=SW_Concurrency_MARTE_Element_strategy)
@settings(max_examples=50)
def test_sw_concurrency_marte_element_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_Element)

@given(instance=SwResource_strategy)
@settings(max_examples=50)
def test_swresource_instantiation(instance):
    assert isinstance(instance, SwResource)

@given(instance=MARTE_SW_Brokering_DeviceBroker_strategy)
@settings(max_examples=50)
def test_marte_sw_brokering_devicebroker_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Brokering_DeviceBroker)



@given(instance=MARTE_SW_Brokering_DeviceBroker_strategy)
def test_marte_sw_brokering_devicebroker_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



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
def test_marte_sw_interaction_swinteractionresource_isIntraMemoryPartitionInteraction_setter(instance):
    original = instance.isIntraMemoryPartitionInteraction
    instance.isIntraMemoryPartitionInteraction = original
    assert instance.isIntraMemoryPartitionInteraction == original



@given(instance=MARTE_SW_Interaction_SwInteractionResource_strategy)
def test_marte_sw_interaction_swinteractionresource_waitingQueueCapacity_setter(instance):
    original = instance.waitingQueueCapacity
    instance.waitingQueueCapacity = original
    assert instance.waitingQueueCapacity == original

@given(instance=MARTE_SW_Brokering_MemoryBroker_strategy)
@settings(max_examples=50)
def test_marte_sw_brokering_memorybroker_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Brokering_MemoryBroker)



@given(instance=MARTE_SW_Brokering_MemoryBroker_strategy)
def test_marte_sw_brokering_memorybroker_accessPolicy_setter(instance):
    original = instance.accessPolicy
    instance.accessPolicy = original
    assert instance.accessPolicy == original

@given(instance=MARTE_SW_Concurrency_SwConcurrentResource_strategy)
@settings(max_examples=50)
def test_marte_sw_concurrency_swconcurrentresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_SwConcurrentResource)



@given(instance=MARTE_SW_Concurrency_SwConcurrentResource_strategy)
def test_marte_sw_concurrency_swconcurrentresource_activationCapacity_setter(instance):
    original = instance.activationCapacity
    instance.activationCapacity = original
    assert instance.activationCapacity == original

@given(instance=SW_ResourceCore_MARTE_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw_resourcecore_marte_behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW_ResourceCore_MARTE_BehavioralFeature)

@given(instance=SW_ResourceCore_MARTE_TypedElement_strategy)
@settings(max_examples=50)
def test_sw_resourcecore_marte_typedelement_instantiation(instance):
    assert isinstance(instance, SW_ResourceCore_MARTE_TypedElement)

@given(instance=SW_Concurrency_MARTE_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_sw_concurrency_marte_behavioralfeature_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_BehavioralFeature)

@given(instance=SW_Brokering_DeviceBroker_strategy)
@settings(max_examples=50)
def test_sw_brokering_devicebroker_instantiation(instance):
    assert isinstance(instance, SW_Brokering_DeviceBroker)

@given(instance=MARTE_HwDiagram_SRMDiagram_strategy)
@settings(max_examples=50)
def test_marte_hwdiagram_srmdiagram_instantiation(instance):
    assert isinstance(instance, MARTE_HwDiagram_SRMDiagram)

@given(instance=SW_ResourceCore_MARTE_Property_strategy)
@settings(max_examples=50)
def test_sw_resourcecore_marte_property_instantiation(instance):
    assert isinstance(instance, SW_ResourceCore_MARTE_Property)

@given(instance=HwDiagram_MARTE_DataType_strategy)
@settings(max_examples=50)
def test_hwdiagram_marte_datatype_instantiation(instance):
    assert isinstance(instance, HwDiagram_MARTE_DataType)

@given(instance=MARTE_HwDiagram_HwCircuitDiagram_strategy)
@settings(max_examples=50)
def test_marte_hwdiagram_hwcircuitdiagram_instantiation(instance):
    assert isinstance(instance, MARTE_HwDiagram_HwCircuitDiagram)



@given(instance=MARTE_HwDiagram_HwCircuitDiagram_strategy)
def test_marte_hwdiagram_hwcircuitdiagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HwCommunication_HwConnection_strategy)
@settings(max_examples=50)
def test_hwcommunication_hwconnection_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwConnection)

@given(instance=MARTE_HwDiagram_HwHRMDiagram_strategy)
@settings(max_examples=50)
def test_marte_hwdiagram_hwhrmdiagram_instantiation(instance):
    assert isinstance(instance, MARTE_HwDiagram_HwHRMDiagram)



@given(instance=MARTE_HwDiagram_HwHRMDiagram_strategy)
def test_marte_hwdiagram_hwhrmdiagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HwPackage_HwWire_strategy)
@settings(max_examples=50)
def test_hwpackage_hwwire_instantiation(instance):
    assert isinstance(instance, HwPackage_HwWire)

@given(instance=MARTE_HwPackage_HwPackagePin_strategy)
@settings(max_examples=50)
def test_marte_hwpackage_hwpackagepin_instantiation(instance):
    assert isinstance(instance, MARTE_HwPackage_HwPackagePin)



@given(instance=MARTE_HwPackage_HwPackagePin_strategy)
def test_marte_hwpackage_hwpackagepin_altNames_setter(instance):
    original = instance.altNames
    instance.altNames = original
    assert instance.altNames == original



@given(instance=MARTE_HwPackage_HwPackagePin_strategy)
def test_marte_hwpackage_hwpackagepin_pinNo_setter(instance):
    original = instance.pinNo
    instance.pinNo = original
    assert instance.pinNo == original

@given(instance=MARTE_HwPackage_HwPackage_strategy)
@settings(max_examples=50)
def test_marte_hwpackage_hwpackage_instantiation(instance):
    assert isinstance(instance, MARTE_HwPackage_HwPackage)



@given(instance=MARTE_HwPackage_HwPackage_strategy)
def test_marte_hwpackage_hwpackage_pinNum_setter(instance):
    original = instance.pinNum
    instance.pinNum = original
    assert instance.pinNum == original



@given(instance=MARTE_HwPackage_HwPackage_strategy)
def test_marte_hwpackage_hwpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MARTE_HwPackage_HwPackage_strategy)
def test_marte_hwpackage_hwpackage_packageType_setter(instance):
    original = instance.packageType
    instance.packageType = original
    assert instance.packageType == original

@given(instance=MARTE_HwDatasheet_HwDatasheet_strategy)
@settings(max_examples=50)
def test_marte_hwdatasheet_hwdatasheet_instantiation(instance):
    assert isinstance(instance, MARTE_HwDatasheet_HwDatasheet)



@given(instance=MARTE_HwDatasheet_HwDatasheet_strategy)
def test_marte_hwdatasheet_hwdatasheet_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original



@given(instance=MARTE_HwDatasheet_HwDatasheet_strategy)
def test_marte_hwdatasheet_hwdatasheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MARTE_HwRegister_HwRegister_strategy)
@settings(max_examples=50)
def test_marte_hwregister_hwregister_instantiation(instance):
    assert isinstance(instance, MARTE_HwRegister_HwRegister)



@given(instance=MARTE_HwRegister_HwRegister_strategy)
def test_marte_hwregister_hwregister_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=MARTE_HwDiagram_HwBlockDiagram_strategy)
@settings(max_examples=50)
def test_marte_hwdiagram_hwblockdiagram_instantiation(instance):
    assert isinstance(instance, MARTE_HwDiagram_HwBlockDiagram)



@given(instance=MARTE_HwDiagram_HwBlockDiagram_strategy)
def test_marte_hwdiagram_hwblockdiagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HwProtocol_MARTE_Operation_strategy)
@settings(max_examples=50)
def test_hwprotocol_marte_operation_instantiation(instance):
    assert isinstance(instance, HwProtocol_MARTE_Operation)

@given(instance=MARTE_HwProtocol_HwProtocol_strategy)
@settings(max_examples=50)
def test_marte_hwprotocol_hwprotocol_instantiation(instance):
    assert isinstance(instance, MARTE_HwProtocol_HwProtocol)



@given(instance=MARTE_HwProtocol_HwProtocol_strategy)
def test_marte_hwprotocol_hwprotocol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MARTE_HwPackage_HwWire_strategy)
@settings(max_examples=50)
def test_marte_hwpackage_hwwire_instantiation(instance):
    assert isinstance(instance, MARTE_HwPackage_HwWire)

@given(instance=MARTE_HwIO_HwPin_strategy)
@settings(max_examples=50)
def test_marte_hwio_hwpin_instantiation(instance):
    assert isinstance(instance, MARTE_HwIO_HwPin)

@given(instance=MARTE_HwDeviceFunction_HwDeviceFunction_strategy)
@settings(max_examples=50)
def test_marte_hwdevicefunction_hwdevicefunction_instantiation(instance):
    assert isinstance(instance, MARTE_HwDeviceFunction_HwDeviceFunction)

@given(instance=GRM_MARTE_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_grm_marte_opaqueexpression_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_OpaqueExpression)

@given(instance=ProcessingResource_strategy)
@settings(max_examples=50)
def test_processingresource_instantiation(instance):
    assert isinstance(instance, ProcessingResource)

@given(instance=MARTE_GRM_ComputingResource_strategy)
@settings(max_examples=50)
def test_marte_grm_computingresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ComputingResource)

@given(instance=GRM_MARTE_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_grm_marte_instancespecification_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_InstanceSpecification)

@given(instance=GRM_MARTE_Property_strategy)
@settings(max_examples=50)
def test_grm_marte_property_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Property)

@given(instance=NFP_Integer_strategy)
@settings(max_examples=50)
def test_nfp_integer_instantiation(instance):
    assert isinstance(instance, NFP_Integer)

@given(instance=MARTE_GRM_Resource_strategy)
@settings(max_examples=50)
def test_marte_grm_resource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_Resource)



@given(instance=MARTE_GRM_Resource_strategy)
def test_marte_grm_resource_isProtected_setter(instance):
    original = instance.isProtected
    instance.isProtected = original
    assert instance.isProtected == original

@given(instance=Time_MARTE_Event_strategy)
@settings(max_examples=50)
def test_time_marte_event_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Event)

@given(instance=Time_MARTE_Message_strategy)
@settings(max_examples=50)
def test_time_marte_message_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Message)

@given(instance=Time_MARTE_Behavior_strategy)
@settings(max_examples=50)
def test_time_marte_behavior_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Behavior)

@given(instance=Time_MARTE_Action_strategy)
@settings(max_examples=50)
def test_time_marte_action_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Action)

@given(instance=Time_MARTE_TimeEvent_strategy)
@settings(max_examples=50)
def test_time_marte_timeevent_instantiation(instance):
    assert isinstance(instance, Time_MARTE_TimeEvent)

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=MARTE_SW_ResourceCore_SwResource_strategy)
@settings(max_examples=50)
def test_marte_sw_resourcecore_swresource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_ResourceCore_SwResource)

@given(instance=MARTE_GRM_Scheduler_strategy)
@settings(max_examples=50)
def test_marte_grm_scheduler_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_Scheduler)



@given(instance=MARTE_GRM_Scheduler_strategy)
def test_marte_grm_scheduler_isPreemptible_setter(instance):
    original = instance.isPreemptible
    instance.isPreemptible = original
    assert instance.isPreemptible == original



@given(instance=MARTE_GRM_Scheduler_strategy)
def test_marte_grm_scheduler_schedPolicy_setter(instance):
    original = instance.schedPolicy
    instance.schedPolicy = original
    assert instance.schedPolicy == original



@given(instance=MARTE_GRM_Scheduler_strategy)
def test_marte_grm_scheduler_otherSchedPolicy_setter(instance):
    original = instance.otherSchedPolicy
    instance.otherSchedPolicy = original
    assert instance.otherSchedPolicy == original

@given(instance=MARTE_GRM_SynchronizationResource_strategy)
@settings(max_examples=50)
def test_marte_grm_synchronizationresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_SynchronizationResource)

@given(instance=MARTE_GRM_CommunicationEndPoint_strategy)
@settings(max_examples=50)
def test_marte_grm_communicationendpoint_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_CommunicationEndPoint)

@given(instance=MARTE_PAM_PaLogicalResource_strategy)
@settings(max_examples=50)
def test_marte_pam_palogicalresource_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaLogicalResource)

@given(instance=MARTE_HwGeneral_HwResource_strategy)
@settings(max_examples=50)
def test_marte_hwgeneral_hwresource_instantiation(instance):
    assert isinstance(instance, MARTE_HwGeneral_HwResource)



@given(instance=MARTE_HwGeneral_HwResource_strategy)
def test_marte_hwgeneral_hwresource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MARTE_GRM_ConcurrencyResource_strategy)
@settings(max_examples=50)
def test_marte_grm_concurrencyresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ConcurrencyResource)

@given(instance=MARTE_GRM_MutualExclusionResource_strategy)
@settings(max_examples=50)
def test_marte_grm_mutualexclusionresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_MutualExclusionResource)



@given(instance=MARTE_GRM_MutualExclusionResource_strategy)
def test_marte_grm_mutualexclusionresource_protectKind_setter(instance):
    original = instance.protectKind
    instance.protectKind = original
    assert instance.protectKind == original



@given(instance=MARTE_GRM_MutualExclusionResource_strategy)
def test_marte_grm_mutualexclusionresource_otherProtectProtocol_setter(instance):
    original = instance.otherProtectProtocol
    instance.otherProtectProtocol = original
    assert instance.otherProtectProtocol == original

@given(instance=MARTE_GRM_StorageResource_strategy)
@settings(max_examples=50)
def test_marte_grm_storageresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_StorageResource)

@given(instance=GRM_MARTE_ConnectableElement_strategy)
@settings(max_examples=50)
def test_grm_marte_connectableelement_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_ConnectableElement)

@given(instance=GRM_MARTE_Lifeline_strategy)
@settings(max_examples=50)
def test_grm_marte_lifeline_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Lifeline)

@given(instance=GRM_MARTE_Classifier_strategy)
@settings(max_examples=50)
def test_grm_marte_classifier_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Classifier)

@given(instance=TimedObservation_strategy)
@settings(max_examples=50)
def test_timedobservation_instantiation(instance):
    assert isinstance(instance, TimedObservation)

@given(instance=MARTE_Time_TimedInstantObservation_strategy)
@settings(max_examples=50)
def test_marte_time_timedinstantobservation_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedInstantObservation)



@given(instance=MARTE_Time_TimedInstantObservation_strategy)
def test_marte_time_timedinstantobservation_obsKind_setter(instance):
    original = instance.obsKind
    instance.obsKind = original
    assert instance.obsKind == original

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

@given(instance=MARTE_Time_TimedObservation_strategy)
@settings(max_examples=50)
def test_marte_time_timedobservation_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedObservation)

@given(instance=MARTE_Time_TimedProcessing_strategy)
@settings(max_examples=50)
def test_marte_time_timedprocessing_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedProcessing)

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

@given(instance=MARTE_Time_TimedEvent_strategy)
@settings(max_examples=50)
def test_marte_time_timedevent_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedEvent)



@given(instance=MARTE_Time_TimedEvent_strategy)
def test_marte_time_timedevent_repetition_setter(instance):
    original = instance.repetition
    instance.repetition = original
    assert instance.repetition == original

@given(instance=Time_MARTE_DurationObservation_strategy)
@settings(max_examples=50)
def test_time_marte_durationobservation_instantiation(instance):
    assert isinstance(instance, Time_MARTE_DurationObservation)

@given(instance=MARTE_Time_TimedDurationObservation_strategy)
@settings(max_examples=50)
def test_marte_time_timeddurationobservation_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedDurationObservation)



@given(instance=MARTE_Time_TimedDurationObservation_strategy)
def test_marte_time_timeddurationobservation_obsKind_setter(instance):
    original = instance.obsKind
    instance.obsKind = original
    assert instance.obsKind == original

@given(instance=Time_MARTE_TimeObservation_strategy)
@settings(max_examples=50)
def test_time_marte_timeobservation_instantiation(instance):
    assert isinstance(instance, Time_MARTE_TimeObservation)

@given(instance=Time_MARTE_Enumeration_strategy)
@settings(max_examples=50)
def test_time_marte_enumeration_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Enumeration)

@given(instance=MARTE_Time_ClockType_strategy)
@settings(max_examples=50)
def test_marte_time_clocktype_instantiation(instance):
    assert isinstance(instance, MARTE_Time_ClockType)



@given(instance=MARTE_Time_ClockType_strategy)
def test_marte_time_clocktype_isLogical_setter(instance):
    original = instance.isLogical
    instance.isLogical = original
    assert instance.isLogical == original



@given(instance=MARTE_Time_ClockType_strategy)
def test_marte_time_clocktype_nature_setter(instance):
    original = instance.nature
    instance.nature = original
    assert instance.nature == original

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

@given(instance=Time_MARTE_Operation_strategy)
@settings(max_examples=50)
def test_time_marte_operation_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Operation)

@given(instance=MARTE_Alloc_Assign_strategy)
@settings(max_examples=50)
def test_marte_alloc_assign_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_Assign)

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
def test_marte_time_clockconstraint_isPrecedenceBased_setter(instance):
    original = instance.isPrecedenceBased
    instance.isPrecedenceBased = original
    assert instance.isPrecedenceBased == original



@given(instance=MARTE_Time_ClockConstraint_strategy)
def test_marte_time_clockconstraint_isCoincidenceBased_setter(instance):
    original = instance.isCoincidenceBased
    instance.isCoincidenceBased = original
    assert instance.isCoincidenceBased == original



@given(instance=MARTE_Time_ClockConstraint_strategy)
def test_marte_time_clockconstraint_isChronometricBased_setter(instance):
    original = instance.isChronometricBased
    instance.isChronometricBased = original
    assert instance.isChronometricBased == original

@given(instance=Alloc_MARTE_Dependency_strategy)
@settings(max_examples=50)
def test_alloc_marte_dependency_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_Dependency)

@given(instance=MARTE_Alloc_NfpRefine_strategy)
@settings(max_examples=50)
def test_marte_alloc_nfprefine_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_NfpRefine)

@given(instance=Alloc_MARTE_ActivityPartition_strategy)
@settings(max_examples=50)
def test_alloc_marte_activitypartition_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_ActivityPartition)

@given(instance=MARTE_Alloc_AllocateActivityGroup_strategy)
@settings(max_examples=50)
def test_marte_alloc_allocateactivitygroup_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_AllocateActivityGroup)

@given(instance=Alloc_Allocated_strategy)
@settings(max_examples=50)
def test_alloc_allocated_instantiation(instance):
    assert isinstance(instance, Alloc_Allocated)

@given(instance=Alloc_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_alloc_marte_namedelement_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_NamedElement)

@given(instance=MARTE_Alloc_Allocated_strategy)
@settings(max_examples=50)
def test_marte_alloc_allocated_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_Allocated)

@given(instance=CoreElements_MARTE_State_strategy)
@settings(max_examples=50)
def test_coreelements_marte_state_instantiation(instance):
    assert isinstance(instance, CoreElements_MARTE_State)

@given(instance=MARTE_CoreElements_Mode_strategy)
@settings(max_examples=50)
def test_marte_coreelements_mode_instantiation(instance):
    assert isinstance(instance, MARTE_CoreElements_Mode)

@given(instance=Alloc_MARTE_Comment_strategy)
@settings(max_examples=50)
def test_alloc_marte_comment_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_Comment)

@given(instance=Alloc_MARTE_Element_strategy)
@settings(max_examples=50)
def test_alloc_marte_element_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_Element)

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
def test_marte_nfps_dimension_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original



@given(instance=MARTE_NFPs_Dimension_strategy)
def test_marte_nfps_dimension_baseExponent_setter(instance):
    original = instance.baseExponent
    instance.baseExponent = original
    assert instance.baseExponent == original

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

@given(instance=MARTE_NFPs_Nfp_strategy)
@settings(max_examples=50)
def test_marte_nfps_nfp_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_Nfp)

@given(instance=NFPs_Unit_strategy)
@settings(max_examples=50)
def test_nfps_unit_instantiation(instance):
    assert isinstance(instance, NFPs_Unit)

@given(instance=MARTE_NFPs_Unit_strategy)
@settings(max_examples=50)
def test_marte_nfps_unit_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_Unit)



@given(instance=MARTE_NFPs_Unit_strategy)
def test_marte_nfps_unit_convFactor_setter(instance):
    original = instance.convFactor
    instance.convFactor = original
    assert instance.convFactor == original



@given(instance=MARTE_NFPs_Unit_strategy)
def test_marte_nfps_unit_offsetFactor_setter(instance):
    original = instance.offsetFactor
    instance.offsetFactor = original
    assert instance.offsetFactor == original

@given(instance=NFPs_MARTE_Property_strategy)
@settings(max_examples=50)
def test_nfps_marte_property_instantiation(instance):
    assert isinstance(instance, NFPs_MARTE_Property)

@given(instance=MARTE_DataTypes_TupleType_strategy)
@settings(max_examples=50)
def test_marte_datatypes_tupletype_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_TupleType)

@given(instance=MARTE_DataTypes_ChoiceType_strategy)
@settings(max_examples=50)
def test_marte_datatypes_choicetype_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_ChoiceType)

@given(instance=HLAM_MARTE_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_hlam_marte_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_BehavioredClassifier)

@given(instance=DataTypes_MARTE_Property_strategy)
@settings(max_examples=50)
def test_datatypes_marte_property_instantiation(instance):
    assert isinstance(instance, DataTypes_MARTE_Property)

@given(instance=MARTE_DataTypes_BoundedSubtype_strategy)
@settings(max_examples=50)
def test_marte_datatypes_boundedsubtype_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_BoundedSubtype)



@given(instance=MARTE_DataTypes_BoundedSubtype_strategy)
def test_marte_datatypes_boundedsubtype_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=MARTE_DataTypes_BoundedSubtype_strategy)
def test_marte_datatypes_boundedsubtype_isMinOpen_setter(instance):
    original = instance.isMinOpen
    instance.isMinOpen = original
    assert instance.isMinOpen == original



@given(instance=MARTE_DataTypes_BoundedSubtype_strategy)
def test_marte_datatypes_boundedsubtype_isMaxOpen_setter(instance):
    original = instance.isMaxOpen
    instance.isMaxOpen = original
    assert instance.isMaxOpen == original



@given(instance=MARTE_DataTypes_BoundedSubtype_strategy)
def test_marte_datatypes_boundedsubtype_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original

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

@given(instance=RSM_MARTE_ConnectorEnd_strategy)
@settings(max_examples=50)
def test_rsm_marte_connectorend_instantiation(instance):
    assert isinstance(instance, RSM_MARTE_ConnectorEnd)

@given(instance=MARTE_DataTypes_CollectionType_strategy)
@settings(max_examples=50)
def test_marte_datatypes_collectiontype_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_CollectionType)

@given(instance=MARTE_DataTypes_IntervalType_strategy)
@settings(max_examples=50)
def test_marte_datatypes_intervaltype_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_IntervalType)

@given(instance=DataTypes_MARTE_DataType_strategy)
@settings(max_examples=50)
def test_datatypes_marte_datatype_instantiation(instance):
    assert isinstance(instance, DataTypes_MARTE_DataType)

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

@given(instance=IntegerVector_strategy)
@settings(max_examples=50)
def test_integervector_instantiation(instance):
    assert isinstance(instance, IntegerVector)

@given(instance=LinkTopology_strategy)
@settings(max_examples=50)
def test_linktopology_instantiation(instance):
    assert isinstance(instance, LinkTopology)

@given(instance=MARTE_RSM_Reshape_strategy)
@settings(max_examples=50)
def test_marte_rsm_reshape_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_Reshape)

@given(instance=MARTE_RSM_InterRepetition_strategy)
@settings(max_examples=50)
def test_marte_rsm_interrepetition_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_InterRepetition)



@given(instance=MARTE_RSM_InterRepetition_strategy)
def test_marte_rsm_interrepetition_isModulo_setter(instance):
    original = instance.isModulo
    instance.isModulo = original
    assert instance.isModulo == original

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

@given(instance=IntegerMatrix_strategy)
@settings(max_examples=50)
def test_integermatrix_instantiation(instance):
    assert isinstance(instance, IntegerMatrix)

@given(instance=MARTE_RSM_Tiler_strategy)
@settings(max_examples=50)
def test_marte_rsm_tiler_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_Tiler)

@given(instance=NFP_Energy_strategy)
@settings(max_examples=50)
def test_nfp_energy_instantiation(instance):
    assert isinstance(instance, NFP_Energy)

@given(instance=NFP_Power_strategy)
@settings(max_examples=50)
def test_nfp_power_instantiation(instance):
    assert isinstance(instance, NFP_Power)

@given(instance=NFP_DataSize_strategy)
@settings(max_examples=50)
def test_nfp_datasize_instantiation(instance):
    assert isinstance(instance, NFP_DataSize)

@given(instance=MARTE_GRM_ResourceUsage_strategy)
@settings(max_examples=50)
def test_marte_grm_resourceusage_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ResourceUsage)

@given(instance=GrService_strategy)
@settings(max_examples=50)
def test_grservice_instantiation(instance):
    assert isinstance(instance, GrService)

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

@given(instance=MARTE_HwGeneral_HwResourceService_strategy)
@settings(max_examples=50)
def test_marte_hwgeneral_hwresourceservice_instantiation(instance):
    assert isinstance(instance, MARTE_HwGeneral_HwResourceService)

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

@given(instance=GRM_ResourceUsage_strategy)
@settings(max_examples=50)
def test_grm_resourceusage_instantiation(instance):
    assert isinstance(instance, GRM_ResourceUsage)

@given(instance=MARTE_GQAM_GaScenario_strategy)
@settings(max_examples=50)
def test_marte_gqam_gascenario_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaScenario)

@given(instance=GRM_MARTE_NamedElement_strategy)
@settings(max_examples=50)
def test_grm_marte_namedelement_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_NamedElement)

@given(instance=MARTE_GRM_DeviceResource_strategy)
@settings(max_examples=50)
def test_marte_grm_deviceresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_DeviceResource)

@given(instance=NFP_DataTxRate_strategy)
@settings(max_examples=50)
def test_nfp_datatxrate_instantiation(instance):
    assert isinstance(instance, NFP_DataTxRate)

@given(instance=NFP_Duration_strategy)
@settings(max_examples=50)
def test_nfp_duration_instantiation(instance):
    assert isinstance(instance, NFP_Duration)

@given(instance=GRM_MARTE_Connector_strategy)
@settings(max_examples=50)
def test_grm_marte_connector_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Connector)

@given(instance=MARTE_GRM_CommunicationMedia_strategy)
@settings(max_examples=50)
def test_marte_grm_communicationmedia_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_CommunicationMedia)



@given(instance=MARTE_GRM_CommunicationMedia_strategy)
def test_marte_grm_communicationmedia_transmMode_setter(instance):
    original = instance.transmMode
    instance.transmMode = original
    assert instance.transmMode == original

@given(instance=Scheduler_strategy)
@settings(max_examples=50)
def test_scheduler_instantiation(instance):
    assert isinstance(instance, Scheduler)

@given(instance=MARTE_GRM_SecondaryScheduler_strategy)
@settings(max_examples=50)
def test_marte_grm_secondaryscheduler_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_SecondaryScheduler)

@given(instance=GRM_SecondaryScheduler_strategy)
@settings(max_examples=50)
def test_grm_secondaryscheduler_instantiation(instance):
    assert isinstance(instance, GRM_SecondaryScheduler)

@given(instance=SchedParameters_strategy)
@settings(max_examples=50)
def test_schedparameters_instantiation(instance):
    assert isinstance(instance, SchedParameters)

@given(instance=MARTE_GRM_SchedulableResource_strategy)
@settings(max_examples=50)
def test_marte_grm_schedulableresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_SchedulableResource)

@given(instance=TimingResource_strategy)
@settings(max_examples=50)
def test_timingresource_instantiation(instance):
    assert isinstance(instance, TimingResource)

@given(instance=MARTE_GRM_TimerResource_strategy)
@settings(max_examples=50)
def test_marte_grm_timerresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_TimerResource)



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

@given(instance=GRM_Scheduler_strategy)
@settings(max_examples=50)
def test_grm_scheduler_instantiation(instance):
    assert isinstance(instance, GRM_Scheduler)

@given(instance=MARTE_GQAM_GaCommHost_strategy)
@settings(max_examples=50)
def test_marte_gqam_gacommhost_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaCommHost)

@given(instance=NFP_Real_strategy)
@settings(max_examples=50)
def test_nfp_real_instantiation(instance):
    assert isinstance(instance, NFP_Real)

@given(instance=MARTE_GRM_ProcessingResource_strategy)
@settings(max_examples=50)
def test_marte_grm_processingresource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ProcessingResource)

@given(instance=GRM_SchedulableResource_strategy)
@settings(max_examples=50)
def test_grm_schedulableresource_instantiation(instance):
    assert isinstance(instance, GRM_SchedulableResource)

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

@given(instance=GRM_MutualExclusionResource_strategy)
@settings(max_examples=50)
def test_grm_mutualexclusionresource_instantiation(instance):
    assert isinstance(instance, GRM_MutualExclusionResource)

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

@given(instance=GRM_ComputingResource_strategy)
@settings(max_examples=50)
def test_grm_computingresource_instantiation(instance):
    assert isinstance(instance, GRM_ComputingResource)

@given(instance=MARTE_HwComputing_HwComputingResource_strategy)
@settings(max_examples=50)
def test_marte_hwcomputing_hwcomputingresource_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwComputingResource)

@given(instance=MARTE_GQAM_GaExecHost_strategy)
@settings(max_examples=50)
def test_marte_gqam_gaexechost_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaExecHost)

@given(instance=GRM_ProcessingResource_strategy)
@settings(max_examples=50)
def test_grm_processingresource_instantiation(instance):
    assert isinstance(instance, GRM_ProcessingResource)
