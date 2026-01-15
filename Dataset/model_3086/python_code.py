from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ComponentState(Enum):
    operating = "operating"
    storage = "storage"
    other = "other"
    undef = "undef"
class FlowDirectionKind(Enum):
    in = "in"
    out = "out"
    inout = "inout"
class OptimallityCriterionKind(Enum):
    meetHardDeadlines = "meetHardDeadlines"
    minimizeMissedDeadlines = "minimizeMissedDeadlines"
    minimizedMeanTardiness = "minimizedMeanTardiness"
    undef = "undef"
    other = "other"
class ExecutionKind(Enum):
    deferred = "deferred"
    remoteImmediate = "remoteImmediate"
    localImmediate = "localImmediate"
class AccessPolicyKind(Enum):
    Read = "Read"
    Write = "Write"
    ReadWrite = "ReadWrite"
    Undef = "Undef"
    Other = "Other"
class WritePolicy(Enum):
    writeBack = "writeBack"
    writeThrough = "writeThrough"
    other = "other"
    undef = "undef"
class ConcurrencyKind(Enum):
    reader = "reader"
    writer = "writer"
    parallel = "parallel"
class InterruptKind(Enum):
    HardwareInterruption = "HardwareInterruption"
    ProcessorDetectedException = "ProcessorDetectedException"
    ProgrammedException = "ProgrammedException"
    Undef = "Undef"
    Other = "Other"
class SynchronizationKind(Enum):
    other = "other"
    synchronous = "synchronous"
    asynchronous = "asynchronous"
    delayedSynchronous = "delayedSynchronous"
    rendezVous = "rendezVous"
class AssignmentKind(Enum):
    hybrid = "hybrid"
    structural = "structural"
    behavioral = "behavioral"
class CacheType(Enum):
    data = "data"
    instruction = "instruction"
    unified = "unified"
    other = "other"
    undef = "undef"
class Repl_Policy(Enum):
    NFU = "NFU"
    FIFO = "FIFO"
    random = "random"
    other = "other"
    undef = "undef"
    LRU = "LRU"
class NotificationKind(Enum):
    Memorized = "Memorized"
    Bounded = "Bounded"
    Memoryless = "Memoryless"
    Undef = "Undef"
    Other = "Other"
class AssignmentNature(Enum):
class VariableDirectionKind(Enum):
    in = "in"
    out = "out"
    inout = "inout"
class LaxityKind(Enum):
    other = "other"
    hard = "hard"
    soft = "soft"
class ClientServerKind(Enum):
    required = "required"
    provided = "provided"
    proreq = "proreq"
class AllocationEndKind(Enum):
class PortSpecificationKind(Enum):
    featureBased = "featureBased"
    atomic = "atomic"
    interfaceBased = "interfaceBased"
class MutualExclusionResourceKind(Enum):
    CountSemaphore = "CountSemaphore"
    Mutex = "Mutex"
    Undef = "Undef"
    Other = "Other"
    BooleanSemaphore = "BooleanSemaphore"
class ComponentKind(Enum):
    card = "card"
    channel = "channel"
    chip = "chip"
    port = "port"
    unit = "unit"
    other = "other"
    undef = "undef"
class PLD_Class(Enum):
    symetricalArray = "symetricalArray"
    rowBased = "rowBased"
    seaOfGates = "seaOfGates"
    hierarchicalPLD = "hierarchicalPLD"
    other = "other"
    undef = "undef"
class ConcurrentAccessProtocolKind(Enum):
    PIP = "PIP"
    PCP = "PCP"
    NoPreemption = "NoPreemption"
    Undef = "Undef"
    Other = "Other"
class DataPoolOrderingKind(Enum):
    LIFO = "LIFO"
    UserDefined = "UserDefined"
    FIFO = "FIFO"
class ROM_Type(Enum):
    other = "other"
    undef = "undef"
    maskedROM = "maskedROM"
    EPROM = "EPROM"
    OTP_EPROM = "OTP_EPROM"
    EEPROM = "EEPROM"
    Flash = "Flash"
class MessageResourceKind(Enum):
    MessageQueue = "MessageQueue"
    Pipe = "Pipe"
    Blackboard = "Blackboard"
    Undef = "Undef"
    Other = "Other"
class ConditionType(Enum):
    temperature = "temperature"
    humidity = "humidity"
    altitude = "altitude"
    vibration = "vibration"
    shock = "shock"
    other = "other"
    undef = "undef"
class AllocationNature(Enum):
    spatialDistribution = "spatialDistribution"
    timeScheduling = "timeScheduling"
class ConstraintKind(Enum):
    required = "required"
    offered = "offered"
    contract = "contract"
class QueuePolicyKind(Enum):
    FIFO = "FIFO"
    LIFO = "LIFO"
    Priority = "Priority"
    Undef = "Undef"
    Other = "Other"
class AllocationKind(Enum):
class PLD_Technology(Enum):
    SRAM = "SRAM"
    antifuse = "antifuse"
    flash = "flash"
    other = "other"
    undef = "undef"
class PoolMgtPolicyKind(Enum):
    infiniteWait = "infiniteWait"
    timedWait = "timedWait"
    dynamic = "dynamic"
    exception = "exception"
    other = "other"
class NotificationResourceKind(Enum):
    Event = "Event"
    Barrier = "Barrier"
    Undef = "Undef"
    Other = "Other"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"
class ISA_Type(Enum):
    RISC = "RISC"
    CISC = "CISC"
    VLIW = "VLIW"
    SIMD = "SIMD"
    other = "other"
    undef = "undef"


############################################
# Definition of Classes
############################################

class PAM_MARTE_NamedElement:

    pass
class MARTE_PAM_PaRunTInstance:

    def __init__(self, unbddPool: str, MARTE_PAM_PaRunTInstance1120: "GRM_SchedulableResource" = None, MARTE_PAM_PaRunTInstance1123: "GQAM_GaExecHost" = None, MARTE_PAM_PaRunTInstance: "NFP_Integer" = None, MARTE_PAM_PaRunTInstance1126: "NFP_Real" = None, MARTE_PAM_PaRunTInstance1129: "NFP_Frequency" = None, MARTE_PAM_PaRunTInstance1132: "PAM_MARTE_NamedElement" = None):
        self.unbddPool = unbddPool
        self.MARTE_PAM_PaRunTInstance1120 = MARTE_PAM_PaRunTInstance1120
        self.MARTE_PAM_PaRunTInstance1123 = MARTE_PAM_PaRunTInstance1123
        self.MARTE_PAM_PaRunTInstance = MARTE_PAM_PaRunTInstance
        self.MARTE_PAM_PaRunTInstance1126 = MARTE_PAM_PaRunTInstance1126
        self.MARTE_PAM_PaRunTInstance1129 = MARTE_PAM_PaRunTInstance1129
        self.MARTE_PAM_PaRunTInstance1132 = MARTE_PAM_PaRunTInstance1132
        
    @property
    def unbddPool(self) -> str:
        return self.__unbddPool

    @unbddPool.setter
    def unbddPool(self, unbddPool: str):
        self.__unbddPool = unbddPool

    @property
    def MARTE_PAM_PaRunTInstance1123(self):
        return self.__MARTE_PAM_PaRunTInstance1123

    @MARTE_PAM_PaRunTInstance1123.setter
    def MARTE_PAM_PaRunTInstance1123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance1123", None)
        self.__MARTE_PAM_PaRunTInstance1123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_GaExecHost1124"):
                opp_val = getattr(old_value, "GQAM_GaExecHost1124", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_GaExecHost1124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_GaExecHost1124"):
                opp_val = getattr(value, "GQAM_GaExecHost1124", None)
                setattr(value, "GQAM_GaExecHost1124", self)

    @property
    def MARTE_PAM_PaRunTInstance1120(self):
        return self.__MARTE_PAM_PaRunTInstance1120

    @MARTE_PAM_PaRunTInstance1120.setter
    def MARTE_PAM_PaRunTInstance1120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance1120", None)
        self.__MARTE_PAM_PaRunTInstance1120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_SchedulableResource1121"):
                opp_val = getattr(old_value, "GRM_SchedulableResource1121", None)
                if opp_val == self:
                    setattr(old_value, "GRM_SchedulableResource1121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_SchedulableResource1121"):
                opp_val = getattr(value, "GRM_SchedulableResource1121", None)
                setattr(value, "GRM_SchedulableResource1121", self)

    @property
    def MARTE_PAM_PaRunTInstance1129(self):
        return self.__MARTE_PAM_PaRunTInstance1129

    @MARTE_PAM_PaRunTInstance1129.setter
    def MARTE_PAM_PaRunTInstance1129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance1129", None)
        self.__MARTE_PAM_PaRunTInstance1129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Frequency1130"):
                opp_val = getattr(old_value, "NFP_Frequency1130", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Frequency1130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Frequency1130"):
                opp_val = getattr(value, "NFP_Frequency1130", None)
                setattr(value, "NFP_Frequency1130", self)

    @property
    def MARTE_PAM_PaRunTInstance1126(self):
        return self.__MARTE_PAM_PaRunTInstance1126

    @MARTE_PAM_PaRunTInstance1126.setter
    def MARTE_PAM_PaRunTInstance1126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance1126", None)
        self.__MARTE_PAM_PaRunTInstance1126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Real1127"):
                opp_val = getattr(old_value, "NFP_Real1127", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Real1127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Real1127"):
                opp_val = getattr(value, "NFP_Real1127", None)
                setattr(value, "NFP_Real1127", self)

    @property
    def MARTE_PAM_PaRunTInstance1132(self):
        return self.__MARTE_PAM_PaRunTInstance1132

    @MARTE_PAM_PaRunTInstance1132.setter
    def MARTE_PAM_PaRunTInstance1132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance1132", None)
        self.__MARTE_PAM_PaRunTInstance1132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PAM_MARTE_NamedElement"):
                opp_val = getattr(old_value, "PAM_MARTE_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "PAM_MARTE_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PAM_MARTE_NamedElement"):
                opp_val = getattr(value, "PAM_MARTE_NamedElement", None)
                setattr(value, "PAM_MARTE_NamedElement", self)

    @property
    def MARTE_PAM_PaRunTInstance(self):
        return self.__MARTE_PAM_PaRunTInstance

    @MARTE_PAM_PaRunTInstance.setter
    def MARTE_PAM_PaRunTInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance", None)
        self.__MARTE_PAM_PaRunTInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Integer1118"):
                opp_val = getattr(old_value, "NFP_Integer1118", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Integer1118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Integer1118"):
                opp_val = getattr(value, "NFP_Integer1118", None)
                setattr(value, "NFP_Integer1118", self)

class PAM_PaStep:

    pass
class GQAM_GaCommStep:

    pass
class MARTE_PAM_PaCommStep(GQAM_GaCommStep, PAM_PaStep):

    pass
class GaExecHost:

    pass
class MARTE_SAM_SaExecHost(GaExecHost):

    pass
class GaCommHost:

    pass
class MARTE_SAM_SaCommHost(GaCommHost):

    pass
class SAM_SaSharedResource:

    pass
class MutualExclusionResource:

    pass
class MARTE_SAM_SaSharedResource(MutualExclusionResource):

    pass
class SAM_MARTE_BehavioralFeature:

    pass
class GaCommStep:

    pass
class MARTE_SAM_SaCommStep(GaCommStep):

    pass
class SAM_MARTE_NamedElement:

    pass
class GQAM_MARTE_Classifier:

    pass
class MARTE_GQAM_GaResourcesPlatform:

    pass
class GQAM_GaResourcesPlatform:

    pass
class GQAM_GaWorkloadBehavior:

    pass
class MARTE_SAM_SaEndtoEndFlow:

    pass
class GaAnalysisContext:

    pass
class MARTE_SAM_SaAnalysisContext(GaAnalysisContext):

    def __init__(self, optCriterion: str, MARTE_SAM_SaAnalysisContext: "NFP_Boolean" = None):
        self.optCriterion = optCriterion
        self.MARTE_SAM_SaAnalysisContext = MARTE_SAM_SaAnalysisContext
        
    @property
    def optCriterion(self) -> str:
        return self.__optCriterion

    @optCriterion.setter
    def optCriterion(self, optCriterion: str):
        self.__optCriterion = optCriterion

    @property
    def MARTE_SAM_SaAnalysisContext(self):
        return self.__MARTE_SAM_SaAnalysisContext

    @MARTE_SAM_SaAnalysisContext.setter
    def MARTE_SAM_SaAnalysisContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SAM_SaAnalysisContext__MARTE_SAM_SaAnalysisContext", None)
        self.__MARTE_SAM_SaAnalysisContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Boolean997"):
                opp_val = getattr(old_value, "NFP_Boolean997", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Boolean997", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Boolean997"):
                opp_val = getattr(value, "NFP_Boolean997", None)
                setattr(value, "NFP_Boolean997", self)

class MARTE_GQAM_GaWorkloadBehavior:

    pass
class SchedulableResource:

    pass
class MARTE_GQAM_GaCommChannel(SchedulableResource):

    pass
class Variables_ExpressionContext:

    pass
class CoreElements_Configuration:

    pass
class MARTE_GQAM_GaAnalysisContext(CoreElements_Configuration, Variables_ExpressionContext):

    pass
class GaTimedObs:

    pass
class MARTE_SAM_SaSchedObs(GaTimedObs):

    pass
class MARTE_GQAM_GaLatencyObs(GaTimedObs):

    pass
class GQAM_MARTE_TimeObservation:

    pass
class NfpConstraint:

    pass
class MARTE_GQAM_GaTimedObs(NfpConstraint):

    def __init__(self, laxity: str, MARTE_GQAM_GaTimedObs: set["GQAM_MARTE_TimeObservation"] = None, MARTE_GQAM_GaTimedObs945: set["GQAM_MARTE_TimeObservation"] = None):
        self.laxity = laxity
        self.MARTE_GQAM_GaTimedObs = MARTE_GQAM_GaTimedObs if MARTE_GQAM_GaTimedObs is not None else set()
        self.MARTE_GQAM_GaTimedObs945 = MARTE_GQAM_GaTimedObs945 if MARTE_GQAM_GaTimedObs945 is not None else set()
        
    @property
    def laxity(self) -> str:
        return self.__laxity

    @laxity.setter
    def laxity(self, laxity: str):
        self.__laxity = laxity

    @property
    def MARTE_GQAM_GaTimedObs945(self):
        return self.__MARTE_GQAM_GaTimedObs945

    @MARTE_GQAM_GaTimedObs945.setter
    def MARTE_GQAM_GaTimedObs945(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaTimedObs__MARTE_GQAM_GaTimedObs945", None)
        self.__MARTE_GQAM_GaTimedObs945 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_MARTE_TimeObservation946"):
                    opp_val = getattr(item, "GQAM_MARTE_TimeObservation946", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_MARTE_TimeObservation946", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_MARTE_TimeObservation946"):
                    opp_val = getattr(item, "GQAM_MARTE_TimeObservation946", None)
                    
                    setattr(item, "GQAM_MARTE_TimeObservation946", self)
                    

    @property
    def MARTE_GQAM_GaTimedObs(self):
        return self.__MARTE_GQAM_GaTimedObs

    @MARTE_GQAM_GaTimedObs.setter
    def MARTE_GQAM_GaTimedObs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaTimedObs__MARTE_GQAM_GaTimedObs", None)
        self.__MARTE_GQAM_GaTimedObs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_MARTE_TimeObservation"):
                    opp_val = getattr(item, "GQAM_MARTE_TimeObservation", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_MARTE_TimeObservation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_MARTE_TimeObservation"):
                    opp_val = getattr(item, "GQAM_MARTE_TimeObservation", None)
                    
                    setattr(item, "GQAM_MARTE_TimeObservation", self)
                    

class GQAM_MARTE_Operation:

    pass
class IntegerInterval:

    pass
class GaStep:

    pass
class MARTE_SAM_SaStep(GaStep):

    pass
class MARTE_GQAM_GaAcqStep(GaStep):

    pass
class MARTE_PAM_PaResPassStep(GaStep):

    pass
class MARTE_PAM_PaStep(GaStep):

    def __init__(self, extOpDemand: str, MARTE_PAM_PaStep: "NFP_Boolean" = None, MARTE_PAM_PaStep1096: set["NFP_Real"] = None, MARTE_PAM_PaStep1099: set["GQAM_GaScenario"] = None, MARTE_PAM_PaStep1102: set["NFP_Real"] = None):
        self.extOpDemand = extOpDemand
        self.MARTE_PAM_PaStep = MARTE_PAM_PaStep
        self.MARTE_PAM_PaStep1096 = MARTE_PAM_PaStep1096 if MARTE_PAM_PaStep1096 is not None else set()
        self.MARTE_PAM_PaStep1099 = MARTE_PAM_PaStep1099 if MARTE_PAM_PaStep1099 is not None else set()
        self.MARTE_PAM_PaStep1102 = MARTE_PAM_PaStep1102 if MARTE_PAM_PaStep1102 is not None else set()
        
    @property
    def extOpDemand(self) -> str:
        return self.__extOpDemand

    @extOpDemand.setter
    def extOpDemand(self, extOpDemand: str):
        self.__extOpDemand = extOpDemand

    @property
    def MARTE_PAM_PaStep1102(self):
        return self.__MARTE_PAM_PaStep1102

    @MARTE_PAM_PaStep1102.setter
    def MARTE_PAM_PaStep1102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaStep__MARTE_PAM_PaStep1102", None)
        self.__MARTE_PAM_PaStep1102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_Real1103"):
                    opp_val = getattr(item, "NFP_Real1103", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_Real1103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_Real1103"):
                    opp_val = getattr(item, "NFP_Real1103", None)
                    
                    setattr(item, "NFP_Real1103", self)
                    

    @property
    def MARTE_PAM_PaStep1099(self):
        return self.__MARTE_PAM_PaStep1099

    @MARTE_PAM_PaStep1099.setter
    def MARTE_PAM_PaStep1099(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaStep__MARTE_PAM_PaStep1099", None)
        self.__MARTE_PAM_PaStep1099 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_GaScenario1100"):
                    opp_val = getattr(item, "GQAM_GaScenario1100", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_GaScenario1100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_GaScenario1100"):
                    opp_val = getattr(item, "GQAM_GaScenario1100", None)
                    
                    setattr(item, "GQAM_GaScenario1100", self)
                    

    @property
    def MARTE_PAM_PaStep1096(self):
        return self.__MARTE_PAM_PaStep1096

    @MARTE_PAM_PaStep1096.setter
    def MARTE_PAM_PaStep1096(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaStep__MARTE_PAM_PaStep1096", None)
        self.__MARTE_PAM_PaStep1096 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_Real1097"):
                    opp_val = getattr(item, "NFP_Real1097", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_Real1097", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_Real1097"):
                    opp_val = getattr(item, "NFP_Real1097", None)
                    
                    setattr(item, "NFP_Real1097", self)
                    

    @property
    def MARTE_PAM_PaStep(self):
        return self.__MARTE_PAM_PaStep

    @MARTE_PAM_PaStep.setter
    def MARTE_PAM_PaStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaStep__MARTE_PAM_PaStep", None)
        self.__MARTE_PAM_PaStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Boolean1094"):
                opp_val = getattr(old_value, "NFP_Boolean1094", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Boolean1094", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Boolean1094"):
                opp_val = getattr(value, "NFP_Boolean1094", None)
                setattr(value, "NFP_Boolean1094", self)

class MARTE_GQAM_GaRelStep(GaStep):

    pass
class MARTE_GQAM_GaCommStep(GaStep):

    pass
class MARTE_GQAM_GaRequestedService(GaStep):

    pass
class GQAM_GaRequestedService:

    pass
class MARTE_PAM_PaRequestedStep(GQAM_GaRequestedService, PAM_PaStep):

    pass
class GQAM_GaExecHost:

    pass
class GaScenario:

    pass
class MARTE_GQAM_GaStep(GaScenario):

    pass
class GQAM_GaTimedObs:

    pass
class GQAM_GaStep:

    pass
class GQAM_GaWorkloadEvent:

    pass
class Time_TimedProcessing:

    pass
class GQAM_GaWorkloadGenerator:

    pass
class MARTE_GQAM_GaWorkloadEvent:

    pass
class GQAM_MARTE_NamedElement:

    pass
class MARTE_GQAM_GaEventTrace:

    def __init__(self, content: str, format: str, location: str, MARTE_GQAM_GaEventTrace: "GQAM_MARTE_NamedElement" = None):
        self.content = content
        self.format = format
        self.location = location
        self.MARTE_GQAM_GaEventTrace = MARTE_GQAM_GaEventTrace
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def MARTE_GQAM_GaEventTrace(self):
        return self.__MARTE_GQAM_GaEventTrace

    @MARTE_GQAM_GaEventTrace.setter
    def MARTE_GQAM_GaEventTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaEventTrace__MARTE_GQAM_GaEventTrace", None)
        self.__MARTE_GQAM_GaEventTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_MARTE_NamedElement"):
                opp_val = getattr(old_value, "GQAM_MARTE_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_MARTE_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_MARTE_NamedElement"):
                opp_val = getattr(value, "GQAM_MARTE_NamedElement", None)
                setattr(value, "GQAM_MARTE_NamedElement", self)

class GQAM_MARTE_TimeEvent:

    pass
class GQAM_GaScenario:

    pass
class GQAM_GaEventTrace:

    pass
class GQAM_MARTE_Behavior:

    pass
class MARTE_GQAM_GaWorkloadGenerator:

    pass
class MARTE_GCM_GCMInvocationAction:

    pass
class GCM_MARTE_Feature:

    pass
class GCM_MARTE_Behavior:

    pass
class MARTE_GCM_DataPool:

    def __init__(self, ordering: str, MARTE_GCM_DataPool: "GCM_MARTE_Property" = None, MARTE_GCM_DataPool843: "GCM_MARTE_Behavior" = None, MARTE_GCM_DataPool845: "GCM_MARTE_Behavior" = None):
        self.ordering = ordering
        self.MARTE_GCM_DataPool = MARTE_GCM_DataPool
        self.MARTE_GCM_DataPool843 = MARTE_GCM_DataPool843
        self.MARTE_GCM_DataPool845 = MARTE_GCM_DataPool845
        
    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def MARTE_GCM_DataPool(self):
        return self.__MARTE_GCM_DataPool

    @MARTE_GCM_DataPool.setter
    def MARTE_GCM_DataPool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_DataPool__MARTE_GCM_DataPool", None)
        self.__MARTE_GCM_DataPool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_Property841"):
                opp_val = getattr(old_value, "GCM_MARTE_Property841", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Property841", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Property841"):
                opp_val = getattr(value, "GCM_MARTE_Property841", None)
                setattr(value, "GCM_MARTE_Property841", self)

    @property
    def MARTE_GCM_DataPool843(self):
        return self.__MARTE_GCM_DataPool843

    @MARTE_GCM_DataPool843.setter
    def MARTE_GCM_DataPool843(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_DataPool__MARTE_GCM_DataPool843", None)
        self.__MARTE_GCM_DataPool843 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_Behavior"):
                opp_val = getattr(old_value, "GCM_MARTE_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Behavior"):
                opp_val = getattr(value, "GCM_MARTE_Behavior", None)
                setattr(value, "GCM_MARTE_Behavior", self)

    @property
    def MARTE_GCM_DataPool845(self):
        return self.__MARTE_GCM_DataPool845

    @MARTE_GCM_DataPool845.setter
    def MARTE_GCM_DataPool845(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_DataPool__MARTE_GCM_DataPool845", None)
        self.__MARTE_GCM_DataPool845 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_Behavior846"):
                opp_val = getattr(old_value, "GCM_MARTE_Behavior846", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Behavior846", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Behavior846"):
                opp_val = getattr(value, "GCM_MARTE_Behavior846", None)
                setattr(value, "GCM_MARTE_Behavior846", self)

class GCM_MARTE_Classifier:

    pass
class GCM_MARTE_AnyReceiveEvent:

    pass
class MARTE_GCM_DataEvent:

    pass
class GCM_MARTE_InvocationAction:

    pass
class GCM_MARTE_Trigger:

    pass
class MARTE_GCM_GCMTrigger:

    pass
class GCM_MARTE_BehavioralFeature:

    pass
class MARTE_GCM_ClientServerFeature:

    def __init__(self, kind: str, MARTE_GCM_ClientServerFeature: "GCM_MARTE_BehavioralFeature" = None):
        self.kind = kind
        self.MARTE_GCM_ClientServerFeature = MARTE_GCM_ClientServerFeature
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def MARTE_GCM_ClientServerFeature(self):
        return self.__MARTE_GCM_ClientServerFeature

    @MARTE_GCM_ClientServerFeature.setter
    def MARTE_GCM_ClientServerFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerFeature__MARTE_GCM_ClientServerFeature", None)
        self.__MARTE_GCM_ClientServerFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_BehavioralFeature"):
                opp_val = getattr(old_value, "GCM_MARTE_BehavioralFeature", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_BehavioralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_BehavioralFeature"):
                opp_val = getattr(value, "GCM_MARTE_BehavioralFeature", None)
                setattr(value, "GCM_MARTE_BehavioralFeature", self)

class MARTE_GCM_FlowSpecification:

    pass
class MARTE_GCM_ClientServerSpecification:

    pass
class GCM_MARTE_Port:

    pass
class GCM_ClientServerSpecification:

    pass
class GCM_MARTE_Interface:

    pass
class MARTE_GCM_ClientServerPort:

    def __init__(self, specificationKind: str, isConjugated: str, kind: str, MARTE_GCM_ClientServerPort: "GCM_MARTE_Port" = None, MARTE_GCM_ClientServerPort819: set["GCM_MARTE_Interface"] = None, MARTE_GCM_ClientServerPort821: set["GCM_MARTE_Interface"] = None, MARTE_GCM_ClientServerPort824: "GCM_ClientServerSpecification" = None):
        self.specificationKind = specificationKind
        self.isConjugated = isConjugated
        self.kind = kind
        self.MARTE_GCM_ClientServerPort = MARTE_GCM_ClientServerPort
        self.MARTE_GCM_ClientServerPort819 = MARTE_GCM_ClientServerPort819 if MARTE_GCM_ClientServerPort819 is not None else set()
        self.MARTE_GCM_ClientServerPort821 = MARTE_GCM_ClientServerPort821 if MARTE_GCM_ClientServerPort821 is not None else set()
        self.MARTE_GCM_ClientServerPort824 = MARTE_GCM_ClientServerPort824
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def specificationKind(self) -> str:
        return self.__specificationKind

    @specificationKind.setter
    def specificationKind(self, specificationKind: str):
        self.__specificationKind = specificationKind

    @property
    def isConjugated(self) -> str:
        return self.__isConjugated

    @isConjugated.setter
    def isConjugated(self, isConjugated: str):
        self.__isConjugated = isConjugated

    @property
    def MARTE_GCM_ClientServerPort(self):
        return self.__MARTE_GCM_ClientServerPort

    @MARTE_GCM_ClientServerPort.setter
    def MARTE_GCM_ClientServerPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort", None)
        self.__MARTE_GCM_ClientServerPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_Port817"):
                opp_val = getattr(old_value, "GCM_MARTE_Port817", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Port817", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Port817"):
                opp_val = getattr(value, "GCM_MARTE_Port817", None)
                setattr(value, "GCM_MARTE_Port817", self)

    @property
    def MARTE_GCM_ClientServerPort821(self):
        return self.__MARTE_GCM_ClientServerPort821

    @MARTE_GCM_ClientServerPort821.setter
    def MARTE_GCM_ClientServerPort821(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort821", None)
        self.__MARTE_GCM_ClientServerPort821 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GCM_MARTE_Interface822"):
                    opp_val = getattr(item, "GCM_MARTE_Interface822", None)
                    
                    if opp_val == self:
                        setattr(item, "GCM_MARTE_Interface822", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GCM_MARTE_Interface822"):
                    opp_val = getattr(item, "GCM_MARTE_Interface822", None)
                    
                    setattr(item, "GCM_MARTE_Interface822", self)
                    

    @property
    def MARTE_GCM_ClientServerPort824(self):
        return self.__MARTE_GCM_ClientServerPort824

    @MARTE_GCM_ClientServerPort824.setter
    def MARTE_GCM_ClientServerPort824(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort824", None)
        self.__MARTE_GCM_ClientServerPort824 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_ClientServerSpecification"):
                opp_val = getattr(old_value, "GCM_ClientServerSpecification", None)
                if opp_val == self:
                    setattr(old_value, "GCM_ClientServerSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_ClientServerSpecification"):
                opp_val = getattr(value, "GCM_ClientServerSpecification", None)
                setattr(value, "GCM_ClientServerSpecification", self)

    @property
    def MARTE_GCM_ClientServerPort819(self):
        return self.__MARTE_GCM_ClientServerPort819

    @MARTE_GCM_ClientServerPort819.setter
    def MARTE_GCM_ClientServerPort819(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort819", None)
        self.__MARTE_GCM_ClientServerPort819 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GCM_MARTE_Interface"):
                    opp_val = getattr(item, "GCM_MARTE_Interface", None)
                    
                    if opp_val == self:
                        setattr(item, "GCM_MARTE_Interface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GCM_MARTE_Interface"):
                    opp_val = getattr(item, "GCM_MARTE_Interface", None)
                    
                    setattr(item, "GCM_MARTE_Interface", self)
                    

class MARTE_GCM_FlowPort:

    def __init__(self, isAtomic: str, isConjugated: str, direction: str, MARTE_GCM_FlowPort: "GCM_MARTE_Port" = None):
        self.isAtomic = isAtomic
        self.isConjugated = isConjugated
        self.direction = direction
        self.MARTE_GCM_FlowPort = MARTE_GCM_FlowPort
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def isConjugated(self) -> str:
        return self.__isConjugated

    @isConjugated.setter
    def isConjugated(self, isConjugated: str):
        self.__isConjugated = isConjugated

    @property
    def isAtomic(self) -> str:
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic

    @property
    def MARTE_GCM_FlowPort(self):
        return self.__MARTE_GCM_FlowPort

    @MARTE_GCM_FlowPort.setter
    def MARTE_GCM_FlowPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_FlowPort__MARTE_GCM_FlowPort", None)
        self.__MARTE_GCM_FlowPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_Port"):
                opp_val = getattr(old_value, "GCM_MARTE_Port", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Port"):
                opp_val = getattr(value, "GCM_MARTE_Port", None)
                setattr(value, "GCM_MARTE_Port", self)

class GCM_MARTE_Property:

    pass
class MARTE_GCM_FlowProperty:

    def __init__(self, direction: str, MARTE_GCM_FlowProperty: "GCM_MARTE_Property" = None):
        self.direction = direction
        self.MARTE_GCM_FlowProperty = MARTE_GCM_FlowProperty
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def MARTE_GCM_FlowProperty(self):
        return self.__MARTE_GCM_FlowProperty

    @MARTE_GCM_FlowProperty.setter
    def MARTE_GCM_FlowProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_FlowProperty__MARTE_GCM_FlowProperty", None)
        self.__MARTE_GCM_FlowProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_Property"):
                opp_val = getattr(old_value, "GCM_MARTE_Property", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Property"):
                opp_val = getattr(value, "GCM_MARTE_Property", None)
                setattr(value, "GCM_MARTE_Property", self)

class SW_Interaction_SwSynchronizationResource:

    pass
class SW_Interaction_MARTE_BehavioralFeature:

    pass
class SwSynchronizationResource:

    pass
class MARTE_SW_Interaction_NotificationResource(SwSynchronizationResource):

    def __init__(self, mechanism: str, occurence: str, MARTE_SW_Interaction_NotificationResource: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_NotificationResource792: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_NotificationResource795: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource798: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource801: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource804: set["SW_Interaction_MARTE_BehavioralFeature"] = None):
        self.mechanism = mechanism
        self.occurence = occurence
        self.MARTE_SW_Interaction_NotificationResource = MARTE_SW_Interaction_NotificationResource if MARTE_SW_Interaction_NotificationResource is not None else set()
        self.MARTE_SW_Interaction_NotificationResource792 = MARTE_SW_Interaction_NotificationResource792 if MARTE_SW_Interaction_NotificationResource792 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource795 = MARTE_SW_Interaction_NotificationResource795 if MARTE_SW_Interaction_NotificationResource795 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource798 = MARTE_SW_Interaction_NotificationResource798 if MARTE_SW_Interaction_NotificationResource798 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource801 = MARTE_SW_Interaction_NotificationResource801 if MARTE_SW_Interaction_NotificationResource801 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource804 = MARTE_SW_Interaction_NotificationResource804 if MARTE_SW_Interaction_NotificationResource804 is not None else set()
        
    @property
    def occurence(self) -> str:
        return self.__occurence

    @occurence.setter
    def occurence(self, occurence: str):
        self.__occurence = occurence

    @property
    def mechanism(self) -> str:
        return self.__mechanism

    @mechanism.setter
    def mechanism(self, mechanism: str):
        self.__mechanism = mechanism

    @property
    def MARTE_SW_Interaction_NotificationResource795(self):
        return self.__MARTE_SW_Interaction_NotificationResource795

    @MARTE_SW_Interaction_NotificationResource795.setter
    def MARTE_SW_Interaction_NotificationResource795(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource795", None)
        self.__MARTE_SW_Interaction_NotificationResource795 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature796"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature796", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature796", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature796"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature796", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature796", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource801(self):
        return self.__MARTE_SW_Interaction_NotificationResource801

    @MARTE_SW_Interaction_NotificationResource801.setter
    def MARTE_SW_Interaction_NotificationResource801(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource801", None)
        self.__MARTE_SW_Interaction_NotificationResource801 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature802"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature802", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature802", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature802"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature802", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature802", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource(self):
        return self.__MARTE_SW_Interaction_NotificationResource

    @MARTE_SW_Interaction_NotificationResource.setter
    def MARTE_SW_Interaction_NotificationResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource", None)
        self.__MARTE_SW_Interaction_NotificationResource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement790"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement790", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement790", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement790"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement790", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement790", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource798(self):
        return self.__MARTE_SW_Interaction_NotificationResource798

    @MARTE_SW_Interaction_NotificationResource798.setter
    def MARTE_SW_Interaction_NotificationResource798(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource798", None)
        self.__MARTE_SW_Interaction_NotificationResource798 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature799"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature799", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature799", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature799"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature799", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature799", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource792(self):
        return self.__MARTE_SW_Interaction_NotificationResource792

    @MARTE_SW_Interaction_NotificationResource792.setter
    def MARTE_SW_Interaction_NotificationResource792(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource792", None)
        self.__MARTE_SW_Interaction_NotificationResource792 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement793"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement793", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement793", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement793"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement793", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement793", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource804(self):
        return self.__MARTE_SW_Interaction_NotificationResource804

    @MARTE_SW_Interaction_NotificationResource804.setter
    def MARTE_SW_Interaction_NotificationResource804(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource804", None)
        self.__MARTE_SW_Interaction_NotificationResource804 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature805"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature805", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature805", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature805"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature805", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature805", self)
                    

class SwCommunicationResource:

    pass
class MARTE_SW_Interaction_MessageComResource(SwCommunicationResource):

    def __init__(self, isFixedMessageSize: str, mechanism: str, messageQueuePolicy: str, MARTE_SW_Interaction_MessageComResource: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_MessageComResource781: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_MessageComResource784: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_MessageComResource787: set["SW_Interaction_MARTE_BehavioralFeature"] = None):
        self.isFixedMessageSize = isFixedMessageSize
        self.mechanism = mechanism
        self.messageQueuePolicy = messageQueuePolicy
        self.MARTE_SW_Interaction_MessageComResource = MARTE_SW_Interaction_MessageComResource if MARTE_SW_Interaction_MessageComResource is not None else set()
        self.MARTE_SW_Interaction_MessageComResource781 = MARTE_SW_Interaction_MessageComResource781 if MARTE_SW_Interaction_MessageComResource781 is not None else set()
        self.MARTE_SW_Interaction_MessageComResource784 = MARTE_SW_Interaction_MessageComResource784 if MARTE_SW_Interaction_MessageComResource784 is not None else set()
        self.MARTE_SW_Interaction_MessageComResource787 = MARTE_SW_Interaction_MessageComResource787 if MARTE_SW_Interaction_MessageComResource787 is not None else set()
        
    @property
    def messageQueuePolicy(self) -> str:
        return self.__messageQueuePolicy

    @messageQueuePolicy.setter
    def messageQueuePolicy(self, messageQueuePolicy: str):
        self.__messageQueuePolicy = messageQueuePolicy

    @property
    def isFixedMessageSize(self) -> str:
        return self.__isFixedMessageSize

    @isFixedMessageSize.setter
    def isFixedMessageSize(self, isFixedMessageSize: str):
        self.__isFixedMessageSize = isFixedMessageSize

    @property
    def mechanism(self) -> str:
        return self.__mechanism

    @mechanism.setter
    def mechanism(self, mechanism: str):
        self.__mechanism = mechanism

    @property
    def MARTE_SW_Interaction_MessageComResource784(self):
        return self.__MARTE_SW_Interaction_MessageComResource784

    @MARTE_SW_Interaction_MessageComResource784.setter
    def MARTE_SW_Interaction_MessageComResource784(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource784", None)
        self.__MARTE_SW_Interaction_MessageComResource784 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature785"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature785", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature785", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature785"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature785", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature785", self)
                    

    @property
    def MARTE_SW_Interaction_MessageComResource(self):
        return self.__MARTE_SW_Interaction_MessageComResource

    @MARTE_SW_Interaction_MessageComResource.setter
    def MARTE_SW_Interaction_MessageComResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource", None)
        self.__MARTE_SW_Interaction_MessageComResource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement779"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement779", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement779", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement779"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement779", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement779", self)
                    

    @property
    def MARTE_SW_Interaction_MessageComResource787(self):
        return self.__MARTE_SW_Interaction_MessageComResource787

    @MARTE_SW_Interaction_MessageComResource787.setter
    def MARTE_SW_Interaction_MessageComResource787(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource787", None)
        self.__MARTE_SW_Interaction_MessageComResource787 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature788"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature788", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature788", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature788"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature788", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature788", self)
                    

    @property
    def MARTE_SW_Interaction_MessageComResource781(self):
        return self.__MARTE_SW_Interaction_MessageComResource781

    @MARTE_SW_Interaction_MessageComResource781.setter
    def MARTE_SW_Interaction_MessageComResource781(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource781", None)
        self.__MARTE_SW_Interaction_MessageComResource781 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement782"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement782", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement782", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement782"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement782", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement782", self)
                    

class MARTE_SW_Interaction_SharedDataComResource(SwCommunicationResource):

    pass
class GRM_SynchronizationResource:

    pass
class SW_Interaction_SwInteractionResource:

    pass
class MARTE_SW_Interaction_SwSynchronizationResource(GRM_SynchronizationResource, SW_Interaction_SwInteractionResource):

    pass
class SW_Interaction_MARTE_TypedElement:

    pass
class SW_Brokering_MARTE_Activity:

    pass
class SW_Brokering_MARTE_Operation:

    pass
class SW_Brokering_MARTE_BehavioralFeature:

    pass
class SW_Brokering_MARTE_TypedElement:

    pass
class TimerResource:

    pass
class MARTE_SW_Concurrency_SwTimerResource(TimerResource):

    pass
class InterruptResource:

    pass
class MARTE_SW_Concurrency_Alarm(InterruptResource):

    def __init__(self, isWatchdog: str, MARTE_SW_Concurrency_Alarm: set["SW_Concurrency_MARTE_TypedElement"] = None):
        self.isWatchdog = isWatchdog
        self.MARTE_SW_Concurrency_Alarm = MARTE_SW_Concurrency_Alarm if MARTE_SW_Concurrency_Alarm is not None else set()
        
    @property
    def isWatchdog(self) -> str:
        return self.__isWatchdog

    @isWatchdog.setter
    def isWatchdog(self, isWatchdog: str):
        self.__isWatchdog = isWatchdog

    @property
    def MARTE_SW_Concurrency_Alarm(self):
        return self.__MARTE_SW_Concurrency_Alarm

    @MARTE_SW_Concurrency_Alarm.setter
    def MARTE_SW_Concurrency_Alarm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_Alarm__MARTE_SW_Concurrency_Alarm", None)
        self.__MARTE_SW_Concurrency_Alarm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement733"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement733", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement733", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement733"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement733", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement733", self)
                    

class SW_Concurrency_MARTE_Namespace:

    pass
class SW_Concurrency_MARTE_NamedElement:

    pass
class SW_Concurrency_SwConcurrentResource:

    pass
class SwConcurrentResource:

    pass
class MARTE_SW_Concurrency_InterruptResource(SwConcurrentResource):

    def __init__(self, kind: str, isMaskable: str, MARTE_SW_Concurrency_InterruptResource: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_InterruptResource690: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_InterruptResource693: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_InterruptResource696: set["SW_Concurrency_MARTE_BehavioralFeature"] = None):
        self.kind = kind
        self.isMaskable = isMaskable
        self.MARTE_SW_Concurrency_InterruptResource = MARTE_SW_Concurrency_InterruptResource if MARTE_SW_Concurrency_InterruptResource is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource690 = MARTE_SW_Concurrency_InterruptResource690 if MARTE_SW_Concurrency_InterruptResource690 is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource693 = MARTE_SW_Concurrency_InterruptResource693 if MARTE_SW_Concurrency_InterruptResource693 is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource696 = MARTE_SW_Concurrency_InterruptResource696 if MARTE_SW_Concurrency_InterruptResource696 is not None else set()
        
    @property
    def isMaskable(self) -> str:
        return self.__isMaskable

    @isMaskable.setter
    def isMaskable(self, isMaskable: str):
        self.__isMaskable = isMaskable

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def MARTE_SW_Concurrency_InterruptResource693(self):
        return self.__MARTE_SW_Concurrency_InterruptResource693

    @MARTE_SW_Concurrency_InterruptResource693.setter
    def MARTE_SW_Concurrency_InterruptResource693(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource693", None)
        self.__MARTE_SW_Concurrency_InterruptResource693 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature694"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature694", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature694", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature694"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature694", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature694", self)
                    

    @property
    def MARTE_SW_Concurrency_InterruptResource696(self):
        return self.__MARTE_SW_Concurrency_InterruptResource696

    @MARTE_SW_Concurrency_InterruptResource696.setter
    def MARTE_SW_Concurrency_InterruptResource696(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource696", None)
        self.__MARTE_SW_Concurrency_InterruptResource696 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature697"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature697", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature697", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature697"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature697", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature697", self)
                    

    @property
    def MARTE_SW_Concurrency_InterruptResource690(self):
        return self.__MARTE_SW_Concurrency_InterruptResource690

    @MARTE_SW_Concurrency_InterruptResource690.setter
    def MARTE_SW_Concurrency_InterruptResource690(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource690", None)
        self.__MARTE_SW_Concurrency_InterruptResource690 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement691"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement691", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement691", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement691"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement691", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement691", self)
                    

    @property
    def MARTE_SW_Concurrency_InterruptResource(self):
        return self.__MARTE_SW_Concurrency_InterruptResource

    @MARTE_SW_Concurrency_InterruptResource.setter
    def MARTE_SW_Concurrency_InterruptResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource", None)
        self.__MARTE_SW_Concurrency_InterruptResource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement688"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement688", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement688", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement688"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement688", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement688", self)
                    

class SW_Concurrency_MARTE_BehavioralFeature:

    pass
class SW_Concurrency_MARTE_TypedElement:

    pass
class SW_Concurrency_MARTE_Element:

    pass
class SwResource:

    pass
class MARTE_SW_Brokering_DeviceBroker(SwResource):

    def __init__(self, accessPolicy: str, isBuffered: str, name: str, MARTE_SW_Brokering_DeviceBroker: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_DeviceBroker736: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker738: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker741: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker747: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker750: set["SW_Brokering_MARTE_Operation"] = None, MARTE_SW_Brokering_DeviceBroker752: set["SW_Brokering_MARTE_Activity"] = None, MARTE_SW_Brokering_DeviceBroker744: set["SW_Brokering_MARTE_BehavioralFeature"] = None):
        self.accessPolicy = accessPolicy
        self.isBuffered = isBuffered
        self.name = name
        self.MARTE_SW_Brokering_DeviceBroker = MARTE_SW_Brokering_DeviceBroker if MARTE_SW_Brokering_DeviceBroker is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker736 = MARTE_SW_Brokering_DeviceBroker736 if MARTE_SW_Brokering_DeviceBroker736 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker738 = MARTE_SW_Brokering_DeviceBroker738 if MARTE_SW_Brokering_DeviceBroker738 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker741 = MARTE_SW_Brokering_DeviceBroker741 if MARTE_SW_Brokering_DeviceBroker741 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker747 = MARTE_SW_Brokering_DeviceBroker747 if MARTE_SW_Brokering_DeviceBroker747 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker750 = MARTE_SW_Brokering_DeviceBroker750 if MARTE_SW_Brokering_DeviceBroker750 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker752 = MARTE_SW_Brokering_DeviceBroker752 if MARTE_SW_Brokering_DeviceBroker752 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker744 = MARTE_SW_Brokering_DeviceBroker744 if MARTE_SW_Brokering_DeviceBroker744 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isBuffered(self) -> str:
        return self.__isBuffered

    @isBuffered.setter
    def isBuffered(self, isBuffered: str):
        self.__isBuffered = isBuffered

    @property
    def accessPolicy(self) -> str:
        return self.__accessPolicy

    @accessPolicy.setter
    def accessPolicy(self, accessPolicy: str):
        self.__accessPolicy = accessPolicy

    @property
    def MARTE_SW_Brokering_DeviceBroker747(self):
        return self.__MARTE_SW_Brokering_DeviceBroker747

    @MARTE_SW_Brokering_DeviceBroker747.setter
    def MARTE_SW_Brokering_DeviceBroker747(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker747", None)
        self.__MARTE_SW_Brokering_DeviceBroker747 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature748"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature748", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature748", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature748"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature748", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature748", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker752(self):
        return self.__MARTE_SW_Brokering_DeviceBroker752

    @MARTE_SW_Brokering_DeviceBroker752.setter
    def MARTE_SW_Brokering_DeviceBroker752(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker752", None)
        self.__MARTE_SW_Brokering_DeviceBroker752 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_Activity"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_Activity", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_Activity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_Activity"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_Activity", None)
                    
                    setattr(item, "SW_Brokering_MARTE_Activity", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker750(self):
        return self.__MARTE_SW_Brokering_DeviceBroker750

    @MARTE_SW_Brokering_DeviceBroker750.setter
    def MARTE_SW_Brokering_DeviceBroker750(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker750", None)
        self.__MARTE_SW_Brokering_DeviceBroker750 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_Operation"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_Operation"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_Operation", None)
                    
                    setattr(item, "SW_Brokering_MARTE_Operation", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker(self):
        return self.__MARTE_SW_Brokering_DeviceBroker

    @MARTE_SW_Brokering_DeviceBroker.setter
    def MARTE_SW_Brokering_DeviceBroker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker", None)
        self.__MARTE_SW_Brokering_DeviceBroker = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker744(self):
        return self.__MARTE_SW_Brokering_DeviceBroker744

    @MARTE_SW_Brokering_DeviceBroker744.setter
    def MARTE_SW_Brokering_DeviceBroker744(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker744", None)
        self.__MARTE_SW_Brokering_DeviceBroker744 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature745"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature745", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature745", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature745"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature745", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature745", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker741(self):
        return self.__MARTE_SW_Brokering_DeviceBroker741

    @MARTE_SW_Brokering_DeviceBroker741.setter
    def MARTE_SW_Brokering_DeviceBroker741(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker741", None)
        self.__MARTE_SW_Brokering_DeviceBroker741 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature742"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature742", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature742", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature742"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature742", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature742", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker738(self):
        return self.__MARTE_SW_Brokering_DeviceBroker738

    @MARTE_SW_Brokering_DeviceBroker738.setter
    def MARTE_SW_Brokering_DeviceBroker738(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker738", None)
        self.__MARTE_SW_Brokering_DeviceBroker738 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature739"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature739", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature739", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature739"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature739", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature739", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker736(self):
        return self.__MARTE_SW_Brokering_DeviceBroker736

    @MARTE_SW_Brokering_DeviceBroker736.setter
    def MARTE_SW_Brokering_DeviceBroker736(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker736", None)
        self.__MARTE_SW_Brokering_DeviceBroker736 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature", self)
                    

class MARTE_SW_Interaction_SwInteractionResource(SwResource):

    def __init__(self, isIntraMemoryPartitionInteraction: bool, waitingQueuePolicy: str, waitingQueueCapacity: str, MARTE_SW_Interaction_SwInteractionResource: set["SW_Interaction_MARTE_TypedElement"] = None):
        self.isIntraMemoryPartitionInteraction = isIntraMemoryPartitionInteraction
        self.waitingQueuePolicy = waitingQueuePolicy
        self.waitingQueueCapacity = waitingQueueCapacity
        self.MARTE_SW_Interaction_SwInteractionResource = MARTE_SW_Interaction_SwInteractionResource if MARTE_SW_Interaction_SwInteractionResource is not None else set()
        
    @property
    def isIntraMemoryPartitionInteraction(self) -> bool:
        return self.__isIntraMemoryPartitionInteraction

    @isIntraMemoryPartitionInteraction.setter
    def isIntraMemoryPartitionInteraction(self, isIntraMemoryPartitionInteraction: bool):
        self.__isIntraMemoryPartitionInteraction = isIntraMemoryPartitionInteraction

    @property
    def waitingQueueCapacity(self) -> str:
        return self.__waitingQueueCapacity

    @waitingQueueCapacity.setter
    def waitingQueueCapacity(self, waitingQueueCapacity: str):
        self.__waitingQueueCapacity = waitingQueueCapacity

    @property
    def waitingQueuePolicy(self) -> str:
        return self.__waitingQueuePolicy

    @waitingQueuePolicy.setter
    def waitingQueuePolicy(self, waitingQueuePolicy: str):
        self.__waitingQueuePolicy = waitingQueuePolicy

    @property
    def MARTE_SW_Interaction_SwInteractionResource(self):
        return self.__MARTE_SW_Interaction_SwInteractionResource

    @MARTE_SW_Interaction_SwInteractionResource.setter
    def MARTE_SW_Interaction_SwInteractionResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_SwInteractionResource__MARTE_SW_Interaction_SwInteractionResource", None)
        self.__MARTE_SW_Interaction_SwInteractionResource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement", self)
                    

class MARTE_SW_Brokering_MemoryBroker(SwResource):

    def __init__(self, accessPolicy: str, MARTE_SW_Brokering_MemoryBroker: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_MemoryBroker756: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_MemoryBroker759: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_MemoryBroker768: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker771: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker762: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker765: set["SW_Brokering_MARTE_BehavioralFeature"] = None):
        self.accessPolicy = accessPolicy
        self.MARTE_SW_Brokering_MemoryBroker = MARTE_SW_Brokering_MemoryBroker if MARTE_SW_Brokering_MemoryBroker is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker756 = MARTE_SW_Brokering_MemoryBroker756 if MARTE_SW_Brokering_MemoryBroker756 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker759 = MARTE_SW_Brokering_MemoryBroker759 if MARTE_SW_Brokering_MemoryBroker759 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker768 = MARTE_SW_Brokering_MemoryBroker768 if MARTE_SW_Brokering_MemoryBroker768 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker771 = MARTE_SW_Brokering_MemoryBroker771 if MARTE_SW_Brokering_MemoryBroker771 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker762 = MARTE_SW_Brokering_MemoryBroker762 if MARTE_SW_Brokering_MemoryBroker762 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker765 = MARTE_SW_Brokering_MemoryBroker765 if MARTE_SW_Brokering_MemoryBroker765 is not None else set()
        
    @property
    def accessPolicy(self) -> str:
        return self.__accessPolicy

    @accessPolicy.setter
    def accessPolicy(self, accessPolicy: str):
        self.__accessPolicy = accessPolicy

    @property
    def MARTE_SW_Brokering_MemoryBroker756(self):
        return self.__MARTE_SW_Brokering_MemoryBroker756

    @MARTE_SW_Brokering_MemoryBroker756.setter
    def MARTE_SW_Brokering_MemoryBroker756(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker756", None)
        self.__MARTE_SW_Brokering_MemoryBroker756 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement757"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement757", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement757", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement757"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement757", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement757", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker768(self):
        return self.__MARTE_SW_Brokering_MemoryBroker768

    @MARTE_SW_Brokering_MemoryBroker768.setter
    def MARTE_SW_Brokering_MemoryBroker768(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker768", None)
        self.__MARTE_SW_Brokering_MemoryBroker768 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature769"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature769", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature769", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature769"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature769", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature769", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker765(self):
        return self.__MARTE_SW_Brokering_MemoryBroker765

    @MARTE_SW_Brokering_MemoryBroker765.setter
    def MARTE_SW_Brokering_MemoryBroker765(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker765", None)
        self.__MARTE_SW_Brokering_MemoryBroker765 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature766"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature766", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature766", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature766"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature766", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature766", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker759(self):
        return self.__MARTE_SW_Brokering_MemoryBroker759

    @MARTE_SW_Brokering_MemoryBroker759.setter
    def MARTE_SW_Brokering_MemoryBroker759(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker759", None)
        self.__MARTE_SW_Brokering_MemoryBroker759 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement760"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement760", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement760", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement760"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement760", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement760", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker(self):
        return self.__MARTE_SW_Brokering_MemoryBroker

    @MARTE_SW_Brokering_MemoryBroker.setter
    def MARTE_SW_Brokering_MemoryBroker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker", None)
        self.__MARTE_SW_Brokering_MemoryBroker = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement754"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement754", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement754", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement754"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement754", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement754", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker762(self):
        return self.__MARTE_SW_Brokering_MemoryBroker762

    @MARTE_SW_Brokering_MemoryBroker762.setter
    def MARTE_SW_Brokering_MemoryBroker762(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker762", None)
        self.__MARTE_SW_Brokering_MemoryBroker762 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature763"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature763", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature763", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature763"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature763", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature763", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker771(self):
        return self.__MARTE_SW_Brokering_MemoryBroker771

    @MARTE_SW_Brokering_MemoryBroker771.setter
    def MARTE_SW_Brokering_MemoryBroker771(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker771", None)
        self.__MARTE_SW_Brokering_MemoryBroker771 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature772"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature772", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature772", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature772"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature772", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature772", self)
                    

class MARTE_SW_Concurrency_MemoryPartition(SwResource):

    pass
class MARTE_SW_Concurrency_SwConcurrentResource(SwResource):

    def __init__(self, activationCapacity: str, MARTE_SW_Concurrency_SwConcurrentResource: "ArrivalPattern" = None, MARTE_SW_Concurrency_SwConcurrentResource642: set["SW_Concurrency_MARTE_Element"] = None, MARTE_SW_Concurrency_SwConcurrentResource644: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource646: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource649: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource652: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource658: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource661: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource664: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource667: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource670: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource673: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource676: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource679: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource655: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource685: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource682: set["SW_Concurrency_MARTE_TypedElement"] = None):
        self.activationCapacity = activationCapacity
        self.MARTE_SW_Concurrency_SwConcurrentResource = MARTE_SW_Concurrency_SwConcurrentResource
        self.MARTE_SW_Concurrency_SwConcurrentResource642 = MARTE_SW_Concurrency_SwConcurrentResource642 if MARTE_SW_Concurrency_SwConcurrentResource642 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource644 = MARTE_SW_Concurrency_SwConcurrentResource644 if MARTE_SW_Concurrency_SwConcurrentResource644 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource646 = MARTE_SW_Concurrency_SwConcurrentResource646 if MARTE_SW_Concurrency_SwConcurrentResource646 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource649 = MARTE_SW_Concurrency_SwConcurrentResource649 if MARTE_SW_Concurrency_SwConcurrentResource649 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource652 = MARTE_SW_Concurrency_SwConcurrentResource652 if MARTE_SW_Concurrency_SwConcurrentResource652 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource658 = MARTE_SW_Concurrency_SwConcurrentResource658 if MARTE_SW_Concurrency_SwConcurrentResource658 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource661 = MARTE_SW_Concurrency_SwConcurrentResource661 if MARTE_SW_Concurrency_SwConcurrentResource661 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource664 = MARTE_SW_Concurrency_SwConcurrentResource664 if MARTE_SW_Concurrency_SwConcurrentResource664 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource667 = MARTE_SW_Concurrency_SwConcurrentResource667 if MARTE_SW_Concurrency_SwConcurrentResource667 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource670 = MARTE_SW_Concurrency_SwConcurrentResource670 if MARTE_SW_Concurrency_SwConcurrentResource670 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource673 = MARTE_SW_Concurrency_SwConcurrentResource673 if MARTE_SW_Concurrency_SwConcurrentResource673 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource676 = MARTE_SW_Concurrency_SwConcurrentResource676 if MARTE_SW_Concurrency_SwConcurrentResource676 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource679 = MARTE_SW_Concurrency_SwConcurrentResource679 if MARTE_SW_Concurrency_SwConcurrentResource679 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource655 = MARTE_SW_Concurrency_SwConcurrentResource655 if MARTE_SW_Concurrency_SwConcurrentResource655 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource685 = MARTE_SW_Concurrency_SwConcurrentResource685 if MARTE_SW_Concurrency_SwConcurrentResource685 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource682 = MARTE_SW_Concurrency_SwConcurrentResource682 if MARTE_SW_Concurrency_SwConcurrentResource682 is not None else set()
        
    @property
    def activationCapacity(self) -> str:
        return self.__activationCapacity

    @activationCapacity.setter
    def activationCapacity(self, activationCapacity: str):
        self.__activationCapacity = activationCapacity

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource652(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource652

    @MARTE_SW_Concurrency_SwConcurrentResource652.setter
    def MARTE_SW_Concurrency_SwConcurrentResource652(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource652", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource652 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement653"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement653", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement653", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement653"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement653", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement653", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource655(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource655

    @MARTE_SW_Concurrency_SwConcurrentResource655.setter
    def MARTE_SW_Concurrency_SwConcurrentResource655(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource655", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource655 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature656"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature656", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature656", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature656"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature656", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature656", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource

    @MARTE_SW_Concurrency_SwConcurrentResource.setter
    def MARTE_SW_Concurrency_SwConcurrentResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrivalPattern640"):
                opp_val = getattr(old_value, "ArrivalPattern640", None)
                if opp_val == self:
                    setattr(old_value, "ArrivalPattern640", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrivalPattern640"):
                opp_val = getattr(value, "ArrivalPattern640", None)
                setattr(value, "ArrivalPattern640", self)

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource644(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource644

    @MARTE_SW_Concurrency_SwConcurrentResource644.setter
    def MARTE_SW_Concurrency_SwConcurrentResource644(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource644", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource644 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource670(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource670

    @MARTE_SW_Concurrency_SwConcurrentResource670.setter
    def MARTE_SW_Concurrency_SwConcurrentResource670(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource670", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource670 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature671"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature671", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature671", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature671"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature671", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature671", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource649(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource649

    @MARTE_SW_Concurrency_SwConcurrentResource649.setter
    def MARTE_SW_Concurrency_SwConcurrentResource649(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource649", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource649 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement650"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement650", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement650", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement650"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement650", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement650", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource685(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource685

    @MARTE_SW_Concurrency_SwConcurrentResource685.setter
    def MARTE_SW_Concurrency_SwConcurrentResource685(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource685", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource685 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement686"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement686", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement686", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement686"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement686", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement686", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource658(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource658

    @MARTE_SW_Concurrency_SwConcurrentResource658.setter
    def MARTE_SW_Concurrency_SwConcurrentResource658(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource658", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource658 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature659"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature659", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature659", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature659"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature659", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature659", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource664(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource664

    @MARTE_SW_Concurrency_SwConcurrentResource664.setter
    def MARTE_SW_Concurrency_SwConcurrentResource664(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource664", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource664 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature665"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature665", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature665", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature665"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature665", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature665", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource646(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource646

    @MARTE_SW_Concurrency_SwConcurrentResource646.setter
    def MARTE_SW_Concurrency_SwConcurrentResource646(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource646", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource646 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement647"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement647", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement647", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement647"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement647", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement647", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource661(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource661

    @MARTE_SW_Concurrency_SwConcurrentResource661.setter
    def MARTE_SW_Concurrency_SwConcurrentResource661(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource661", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource661 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature662"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature662", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature662", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature662"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature662", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature662", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource667(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource667

    @MARTE_SW_Concurrency_SwConcurrentResource667.setter
    def MARTE_SW_Concurrency_SwConcurrentResource667(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource667", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource667 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature668"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature668", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature668", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature668"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature668", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature668", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource676(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource676

    @MARTE_SW_Concurrency_SwConcurrentResource676.setter
    def MARTE_SW_Concurrency_SwConcurrentResource676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource676", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource676 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement677"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement677", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement677", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement677"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement677", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement677", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource673(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource673

    @MARTE_SW_Concurrency_SwConcurrentResource673.setter
    def MARTE_SW_Concurrency_SwConcurrentResource673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource673", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource673 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement674"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement674", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement674", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement674"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement674", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement674", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource679(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource679

    @MARTE_SW_Concurrency_SwConcurrentResource679.setter
    def MARTE_SW_Concurrency_SwConcurrentResource679(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource679", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource679 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement680"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement680", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement680", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement680"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement680", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement680", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource682(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource682

    @MARTE_SW_Concurrency_SwConcurrentResource682.setter
    def MARTE_SW_Concurrency_SwConcurrentResource682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource682", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource682 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement683"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement683", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement683", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement683"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement683", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement683", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource642(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource642

    @MARTE_SW_Concurrency_SwConcurrentResource642.setter
    def MARTE_SW_Concurrency_SwConcurrentResource642(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource642", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource642 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_Element"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_Element"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_Element", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_Element", self)
                    

class SW_ResourceCore_MARTE_BehavioralFeature:

    pass
class SW_ResourceCore_MARTE_Property:

    pass
class HwDiagram_MARTE_DataType:

    pass
class SW_ResourceCore_MARTE_TypedElement:

    pass
class SW_Brokering_DeviceBroker:

    pass
class MARTE_HwDiagram_SRMDiagram:

    pass
class HwCommunication_HwConnection:

    pass
class MARTE_HwDiagram_HwHRMDiagram:

    def __init__(self, name: str, MARTE_HwDiagram_HwHRMDiagram: set["HwGeneral_HwResource"] = None, MARTE_HwDiagram_HwHRMDiagram611: set["HwCommunication_HwMedia"] = None, MARTE_HwDiagram_HwHRMDiagram617: set["HwDiagram_MARTE_DataType"] = None, MARTE_HwDiagram_HwHRMDiagram614: set["HwProtocol_HwProtocol"] = None):
        self.name = name
        self.MARTE_HwDiagram_HwHRMDiagram = MARTE_HwDiagram_HwHRMDiagram if MARTE_HwDiagram_HwHRMDiagram is not None else set()
        self.MARTE_HwDiagram_HwHRMDiagram611 = MARTE_HwDiagram_HwHRMDiagram611 if MARTE_HwDiagram_HwHRMDiagram611 is not None else set()
        self.MARTE_HwDiagram_HwHRMDiagram617 = MARTE_HwDiagram_HwHRMDiagram617 if MARTE_HwDiagram_HwHRMDiagram617 is not None else set()
        self.MARTE_HwDiagram_HwHRMDiagram614 = MARTE_HwDiagram_HwHRMDiagram614 if MARTE_HwDiagram_HwHRMDiagram614 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MARTE_HwDiagram_HwHRMDiagram617(self):
        return self.__MARTE_HwDiagram_HwHRMDiagram617

    @MARTE_HwDiagram_HwHRMDiagram617.setter
    def MARTE_HwDiagram_HwHRMDiagram617(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwHRMDiagram__MARTE_HwDiagram_HwHRMDiagram617", None)
        self.__MARTE_HwDiagram_HwHRMDiagram617 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwDiagram_MARTE_DataType"):
                    opp_val = getattr(item, "HwDiagram_MARTE_DataType", None)
                    
                    if opp_val == self:
                        setattr(item, "HwDiagram_MARTE_DataType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwDiagram_MARTE_DataType"):
                    opp_val = getattr(item, "HwDiagram_MARTE_DataType", None)
                    
                    setattr(item, "HwDiagram_MARTE_DataType", self)
                    

    @property
    def MARTE_HwDiagram_HwHRMDiagram614(self):
        return self.__MARTE_HwDiagram_HwHRMDiagram614

    @MARTE_HwDiagram_HwHRMDiagram614.setter
    def MARTE_HwDiagram_HwHRMDiagram614(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwHRMDiagram__MARTE_HwDiagram_HwHRMDiagram614", None)
        self.__MARTE_HwDiagram_HwHRMDiagram614 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwProtocol_HwProtocol615"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol615", None)
                    
                    if opp_val == self:
                        setattr(item, "HwProtocol_HwProtocol615", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwProtocol_HwProtocol615"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol615", None)
                    
                    setattr(item, "HwProtocol_HwProtocol615", self)
                    

    @property
    def MARTE_HwDiagram_HwHRMDiagram(self):
        return self.__MARTE_HwDiagram_HwHRMDiagram

    @MARTE_HwDiagram_HwHRMDiagram.setter
    def MARTE_HwDiagram_HwHRMDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwHRMDiagram__MARTE_HwDiagram_HwHRMDiagram", None)
        self.__MARTE_HwDiagram_HwHRMDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResource609"):
                    opp_val = getattr(item, "HwGeneral_HwResource609", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResource609", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResource609"):
                    opp_val = getattr(item, "HwGeneral_HwResource609", None)
                    
                    setattr(item, "HwGeneral_HwResource609", self)
                    

    @property
    def MARTE_HwDiagram_HwHRMDiagram611(self):
        return self.__MARTE_HwDiagram_HwHRMDiagram611

    @MARTE_HwDiagram_HwHRMDiagram611.setter
    def MARTE_HwDiagram_HwHRMDiagram611(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwHRMDiagram__MARTE_HwDiagram_HwHRMDiagram611", None)
        self.__MARTE_HwDiagram_HwHRMDiagram611 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwCommunication_HwMedia612"):
                    opp_val = getattr(item, "HwCommunication_HwMedia612", None)
                    
                    if opp_val == self:
                        setattr(item, "HwCommunication_HwMedia612", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwCommunication_HwMedia612"):
                    opp_val = getattr(item, "HwCommunication_HwMedia612", None)
                    
                    setattr(item, "HwCommunication_HwMedia612", self)
                    

class MARTE_HwDiagram_HwCircuitDiagram:

    def __init__(self, name: str, MARTE_HwDiagram_HwCircuitDiagram: set["HwPackage_HwPackage"] = None, MARTE_HwDiagram_HwCircuitDiagram606: set["HwPackage_HwWire"] = None):
        self.name = name
        self.MARTE_HwDiagram_HwCircuitDiagram = MARTE_HwDiagram_HwCircuitDiagram if MARTE_HwDiagram_HwCircuitDiagram is not None else set()
        self.MARTE_HwDiagram_HwCircuitDiagram606 = MARTE_HwDiagram_HwCircuitDiagram606 if MARTE_HwDiagram_HwCircuitDiagram606 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MARTE_HwDiagram_HwCircuitDiagram606(self):
        return self.__MARTE_HwDiagram_HwCircuitDiagram606

    @MARTE_HwDiagram_HwCircuitDiagram606.setter
    def MARTE_HwDiagram_HwCircuitDiagram606(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwCircuitDiagram__MARTE_HwDiagram_HwCircuitDiagram606", None)
        self.__MARTE_HwDiagram_HwCircuitDiagram606 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwPackage_HwWire607"):
                    opp_val = getattr(item, "HwPackage_HwWire607", None)
                    
                    if opp_val == self:
                        setattr(item, "HwPackage_HwWire607", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwPackage_HwWire607"):
                    opp_val = getattr(item, "HwPackage_HwWire607", None)
                    
                    setattr(item, "HwPackage_HwWire607", self)
                    

    @property
    def MARTE_HwDiagram_HwCircuitDiagram(self):
        return self.__MARTE_HwDiagram_HwCircuitDiagram

    @MARTE_HwDiagram_HwCircuitDiagram.setter
    def MARTE_HwDiagram_HwCircuitDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwCircuitDiagram__MARTE_HwDiagram_HwCircuitDiagram", None)
        self.__MARTE_HwDiagram_HwCircuitDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwPackage_HwPackage604"):
                    opp_val = getattr(item, "HwPackage_HwPackage604", None)
                    
                    if opp_val == self:
                        setattr(item, "HwPackage_HwPackage604", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwPackage_HwPackage604"):
                    opp_val = getattr(item, "HwPackage_HwPackage604", None)
                    
                    setattr(item, "HwPackage_HwPackage604", self)
                    

class MARTE_HwPackage_HwPackage:

    def __init__(self, name: str, pinNum: int, packageType: str, MARTE_HwPackage_HwPackage: set["HwPackage_HwPackagePin"] = None):
        self.name = name
        self.pinNum = pinNum
        self.packageType = packageType
        self.MARTE_HwPackage_HwPackage = MARTE_HwPackage_HwPackage if MARTE_HwPackage_HwPackage is not None else set()
        
    @property
    def pinNum(self) -> int:
        return self.__pinNum

    @pinNum.setter
    def pinNum(self, pinNum: int):
        self.__pinNum = pinNum

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def packageType(self) -> str:
        return self.__packageType

    @packageType.setter
    def packageType(self, packageType: str):
        self.__packageType = packageType

    @property
    def MARTE_HwPackage_HwPackage(self):
        return self.__MARTE_HwPackage_HwPackage

    @MARTE_HwPackage_HwPackage.setter
    def MARTE_HwPackage_HwPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwPackage_HwPackage__MARTE_HwPackage_HwPackage", None)
        self.__MARTE_HwPackage_HwPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwPackage_HwPackagePin"):
                    opp_val = getattr(item, "HwPackage_HwPackagePin", None)
                    
                    if opp_val == self:
                        setattr(item, "HwPackage_HwPackagePin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwPackage_HwPackagePin"):
                    opp_val = getattr(item, "HwPackage_HwPackagePin", None)
                    
                    setattr(item, "HwPackage_HwPackagePin", self)
                    

class MARTE_HwDiagram_HwBlockDiagram:

    def __init__(self, name: str, MARTE_HwDiagram_HwBlockDiagram601: set["HwGeneral_HwResource"] = None, MARTE_HwDiagram_HwBlockDiagram: set["HwProtocol_HwProtocol"] = None, MARTE_HwDiagram_HwBlockDiagram599: set["HwCommunication_HwConnection"] = None):
        self.name = name
        self.MARTE_HwDiagram_HwBlockDiagram601 = MARTE_HwDiagram_HwBlockDiagram601 if MARTE_HwDiagram_HwBlockDiagram601 is not None else set()
        self.MARTE_HwDiagram_HwBlockDiagram = MARTE_HwDiagram_HwBlockDiagram if MARTE_HwDiagram_HwBlockDiagram is not None else set()
        self.MARTE_HwDiagram_HwBlockDiagram599 = MARTE_HwDiagram_HwBlockDiagram599 if MARTE_HwDiagram_HwBlockDiagram599 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MARTE_HwDiagram_HwBlockDiagram601(self):
        return self.__MARTE_HwDiagram_HwBlockDiagram601

    @MARTE_HwDiagram_HwBlockDiagram601.setter
    def MARTE_HwDiagram_HwBlockDiagram601(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwBlockDiagram__MARTE_HwDiagram_HwBlockDiagram601", None)
        self.__MARTE_HwDiagram_HwBlockDiagram601 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResource602"):
                    opp_val = getattr(item, "HwGeneral_HwResource602", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResource602", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResource602"):
                    opp_val = getattr(item, "HwGeneral_HwResource602", None)
                    
                    setattr(item, "HwGeneral_HwResource602", self)
                    

    @property
    def MARTE_HwDiagram_HwBlockDiagram(self):
        return self.__MARTE_HwDiagram_HwBlockDiagram

    @MARTE_HwDiagram_HwBlockDiagram.setter
    def MARTE_HwDiagram_HwBlockDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwBlockDiagram__MARTE_HwDiagram_HwBlockDiagram", None)
        self.__MARTE_HwDiagram_HwBlockDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwProtocol_HwProtocol597"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol597", None)
                    
                    if opp_val == self:
                        setattr(item, "HwProtocol_HwProtocol597", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwProtocol_HwProtocol597"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol597", None)
                    
                    setattr(item, "HwProtocol_HwProtocol597", self)
                    

    @property
    def MARTE_HwDiagram_HwBlockDiagram599(self):
        return self.__MARTE_HwDiagram_HwBlockDiagram599

    @MARTE_HwDiagram_HwBlockDiagram599.setter
    def MARTE_HwDiagram_HwBlockDiagram599(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwBlockDiagram__MARTE_HwDiagram_HwBlockDiagram599", None)
        self.__MARTE_HwDiagram_HwBlockDiagram599 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwCommunication_HwConnection"):
                    opp_val = getattr(item, "HwCommunication_HwConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "HwCommunication_HwConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwCommunication_HwConnection"):
                    opp_val = getattr(item, "HwCommunication_HwConnection", None)
                    
                    setattr(item, "HwCommunication_HwConnection", self)
                    

class HwProtocol_MARTE_Operation:

    pass
class MARTE_HwProtocol_HwProtocol:

    def __init__(self, name: str, MARTE_HwProtocol_HwProtocol: set["HwProtocol_MARTE_Operation"] = None):
        self.name = name
        self.MARTE_HwProtocol_HwProtocol = MARTE_HwProtocol_HwProtocol if MARTE_HwProtocol_HwProtocol is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MARTE_HwProtocol_HwProtocol(self):
        return self.__MARTE_HwProtocol_HwProtocol

    @MARTE_HwProtocol_HwProtocol.setter
    def MARTE_HwProtocol_HwProtocol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwProtocol_HwProtocol__MARTE_HwProtocol_HwProtocol", None)
        self.__MARTE_HwProtocol_HwProtocol = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwProtocol_MARTE_Operation"):
                    opp_val = getattr(item, "HwProtocol_MARTE_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "HwProtocol_MARTE_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwProtocol_MARTE_Operation"):
                    opp_val = getattr(item, "HwProtocol_MARTE_Operation", None)
                    
                    setattr(item, "HwProtocol_MARTE_Operation", self)
                    

class HwPackage_HwWire:

    pass
class HwPackage_HwPackagePin:

    pass
class MARTE_HwDatasheet_HwDatasheet:

    def __init__(self, revision: str, name: str, MARTE_HwDatasheet_HwDatasheet: set["HwGeneral_HwResource"] = None, MARTE_HwDatasheet_HwDatasheet588: set["HwProtocol_HwProtocol"] = None):
        self.revision = revision
        self.name = name
        self.MARTE_HwDatasheet_HwDatasheet = MARTE_HwDatasheet_HwDatasheet if MARTE_HwDatasheet_HwDatasheet is not None else set()
        self.MARTE_HwDatasheet_HwDatasheet588 = MARTE_HwDatasheet_HwDatasheet588 if MARTE_HwDatasheet_HwDatasheet588 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def revision(self) -> str:
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision

    @property
    def MARTE_HwDatasheet_HwDatasheet588(self):
        return self.__MARTE_HwDatasheet_HwDatasheet588

    @MARTE_HwDatasheet_HwDatasheet588.setter
    def MARTE_HwDatasheet_HwDatasheet588(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDatasheet_HwDatasheet__MARTE_HwDatasheet_HwDatasheet588", None)
        self.__MARTE_HwDatasheet_HwDatasheet588 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwProtocol_HwProtocol589"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol589", None)
                    
                    if opp_val == self:
                        setattr(item, "HwProtocol_HwProtocol589", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwProtocol_HwProtocol589"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol589", None)
                    
                    setattr(item, "HwProtocol_HwProtocol589", self)
                    

    @property
    def MARTE_HwDatasheet_HwDatasheet(self):
        return self.__MARTE_HwDatasheet_HwDatasheet

    @MARTE_HwDatasheet_HwDatasheet.setter
    def MARTE_HwDatasheet_HwDatasheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDatasheet_HwDatasheet__MARTE_HwDatasheet_HwDatasheet", None)
        self.__MARTE_HwDatasheet_HwDatasheet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResource586"):
                    opp_val = getattr(item, "HwGeneral_HwResource586", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResource586", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResource586"):
                    opp_val = getattr(item, "HwGeneral_HwResource586", None)
                    
                    setattr(item, "HwGeneral_HwResource586", self)
                    

class HwIO_HwLine:

    pass
class HwPeripheral_RegisterAction:

    pass
class Activity:

    pass
class MARTE_HwPeripheral_PeripheralActivity(Activity):

    pass
class HwPeripheral_MARTE_OutputPin:

    pass
class HwPeripheral_MARTE_InputPin:

    pass
class RegisterAction:

    pass
class MARTE_HwPeripheral_ReadRegisterAction(RegisterAction):

    pass
class MARTE_HwPeripheral_WriteRegisterAction(RegisterAction):

    pass
class Action:

    pass
class MARTE_HwPeripheral_RegisterAction(Action):

    pass
class HwPeripheral_MARTE_Operation:

    pass
class Operation:

    pass
class MARTE_HwDeviceFunction_HwDeviceFunction(Operation):

    pass
class MARTE_HwPeripheral_OperationImpl(Operation):

    pass
class Realnterval:

    pass
class HwComponent:

    pass
class MARTE_HwPower_HwCoolingSupply(HwComponent):

    pass
class MARTE_HwPower_HwPowerSupply(HwComponent):

    pass
class HwLayout_Env_Condition:

    pass
class NFP_Price:

    pass
class MARTE_HwLayout_Env_Condition:

    def __init__(self, type: str, status: str, MARTE_HwLayout_Env_Condition567: "Realnterval" = None, MARTE_HwLayout_Env_Condition: "NFP_String" = None):
        self.type = type
        self.status = status
        self.MARTE_HwLayout_Env_Condition567 = MARTE_HwLayout_Env_Condition567
        self.MARTE_HwLayout_Env_Condition = MARTE_HwLayout_Env_Condition
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def MARTE_HwLayout_Env_Condition567(self):
        return self.__MARTE_HwLayout_Env_Condition567

    @MARTE_HwLayout_Env_Condition567.setter
    def MARTE_HwLayout_Env_Condition567(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_Env_Condition__MARTE_HwLayout_Env_Condition567", None)
        self.__MARTE_HwLayout_Env_Condition567 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Realnterval"):
                opp_val = getattr(old_value, "Realnterval", None)
                if opp_val == self:
                    setattr(old_value, "Realnterval", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Realnterval"):
                opp_val = getattr(value, "Realnterval", None)
                setattr(value, "Realnterval", self)

    @property
    def MARTE_HwLayout_Env_Condition(self):
        return self.__MARTE_HwLayout_Env_Condition

    @MARTE_HwLayout_Env_Condition.setter
    def MARTE_HwLayout_Env_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_Env_Condition__MARTE_HwLayout_Env_Condition", None)
        self.__MARTE_HwLayout_Env_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_String565"):
                opp_val = getattr(old_value, "NFP_String565", None)
                if opp_val == self:
                    setattr(old_value, "NFP_String565", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_String565"):
                opp_val = getattr(value, "NFP_String565", None)
                setattr(value, "NFP_String565", self)

class HwLayout_HwComponent:

    pass
class NFP_NaturalInterval:

    pass
class NFP_Area:

    pass
class NFP_Length:

    pass
class HwGeneral_MARTE_Activity:

    pass
class HwGeneral_MARTE_Operation:

    pass
class NFP_Frequency:

    pass
class HwCommunication_HwEndPoint:

    pass
class HwGeneral_HwResourceService:

    pass
class HwI_O:

    pass
class MARTE_HwDevice_HWSensor(HwI_O):

    pass
class MARTE_HwDevice_HWActuator(HwI_O):

    pass
class HwPeripheral_PeripheralActivity:

    pass
class HwPeripheral_OperationImpl:

    pass
class HwTiming_HwClock:

    pass
class HwDevice:

    pass
class MARTE_HwDevice_HwPeripheral(HwDevice):

    pass
class MARTE_HwDevice_HwSupport(HwDevice):

    pass
class MARTE_HwDevice_HwI_O(HwDevice):

    pass
class HwDeviceFunction_HwDeviceFunction:

    pass
class GRM_DeviceResource:

    pass
class HwTimingResource:

    pass
class MARTE_HwTiming_HwTimer(HwTimingResource):

    pass
class MARTE_HwTiming_HwClock(HwTimingResource):

    pass
class GRM_TimingResource:

    pass
class HwMemory_CacheStructure:

    pass
class HwMemory_MemoryOrganization:

    pass
class HwMemory:

    pass
class MARTE_HwRegister_HwRegister(HwMemory):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class MARTE_HwMemory_HwCache(HwMemory):

    def __init__(self, type: str, repl_Policy: str, writePolicy: str, MARTE_HwMemory_HwCache: "NFP_Natural" = None, MARTE_HwMemory_HwCache477: "HwMemory_CacheStructure" = None):
        self.type = type
        self.repl_Policy = repl_Policy
        self.writePolicy = writePolicy
        self.MARTE_HwMemory_HwCache = MARTE_HwMemory_HwCache
        self.MARTE_HwMemory_HwCache477 = MARTE_HwMemory_HwCache477
        
    @property
    def writePolicy(self) -> str:
        return self.__writePolicy

    @writePolicy.setter
    def writePolicy(self, writePolicy: str):
        self.__writePolicy = writePolicy

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def repl_Policy(self) -> str:
        return self.__repl_Policy

    @repl_Policy.setter
    def repl_Policy(self, repl_Policy: str):
        self.__repl_Policy = repl_Policy

    @property
    def MARTE_HwMemory_HwCache477(self):
        return self.__MARTE_HwMemory_HwCache477

    @MARTE_HwMemory_HwCache477.setter
    def MARTE_HwMemory_HwCache477(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwCache__MARTE_HwMemory_HwCache477", None)
        self.__MARTE_HwMemory_HwCache477 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HwMemory_CacheStructure"):
                opp_val = getattr(old_value, "HwMemory_CacheStructure", None)
                if opp_val == self:
                    setattr(old_value, "HwMemory_CacheStructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HwMemory_CacheStructure"):
                opp_val = getattr(value, "HwMemory_CacheStructure", None)
                setattr(value, "HwMemory_CacheStructure", self)

    @property
    def MARTE_HwMemory_HwCache(self):
        return self.__MARTE_HwMemory_HwCache

    @MARTE_HwMemory_HwCache.setter
    def MARTE_HwMemory_HwCache(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwCache__MARTE_HwMemory_HwCache", None)
        self.__MARTE_HwMemory_HwCache = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Natural475"):
                opp_val = getattr(old_value, "NFP_Natural475", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Natural475", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Natural475"):
                opp_val = getattr(value, "NFP_Natural475", None)
                setattr(value, "NFP_Natural475", self)

class MARTE_HwMemory_HwROM(HwMemory):

    def __init__(self, type: str, MARTE_HwMemory_HwROM: "HwMemory_MemoryOrganization" = None):
        self.type = type
        self.MARTE_HwMemory_HwROM = MARTE_HwMemory_HwROM
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def MARTE_HwMemory_HwROM(self):
        return self.__MARTE_HwMemory_HwROM

    @MARTE_HwMemory_HwROM.setter
    def MARTE_HwMemory_HwROM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwROM__MARTE_HwMemory_HwROM", None)
        self.__MARTE_HwMemory_HwROM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HwMemory_MemoryOrganization468"):
                opp_val = getattr(old_value, "HwMemory_MemoryOrganization468", None)
                if opp_val == self:
                    setattr(old_value, "HwMemory_MemoryOrganization468", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HwMemory_MemoryOrganization468"):
                opp_val = getattr(value, "HwMemory_MemoryOrganization468", None)
                setattr(value, "HwMemory_MemoryOrganization468", self)

class MARTE_HwMemory_HwDrive(HwMemory):

    pass
class MARTE_HwMemory_HwRAM(HwMemory):

    def __init__(self, repl_Policy: str, writePolicy: str, MARTE_HwMemory_HwRAM462: "NFP_Boolean" = None, MARTE_HwMemory_HwRAM465: "NFP_Boolean" = None, MARTE_HwMemory_HwRAM: "HwMemory_MemoryOrganization" = None, MARTE_HwMemory_HwRAM459: "NFP_Boolean" = None):
        self.repl_Policy = repl_Policy
        self.writePolicy = writePolicy
        self.MARTE_HwMemory_HwRAM462 = MARTE_HwMemory_HwRAM462
        self.MARTE_HwMemory_HwRAM465 = MARTE_HwMemory_HwRAM465
        self.MARTE_HwMemory_HwRAM = MARTE_HwMemory_HwRAM
        self.MARTE_HwMemory_HwRAM459 = MARTE_HwMemory_HwRAM459
        
    @property
    def writePolicy(self) -> str:
        return self.__writePolicy

    @writePolicy.setter
    def writePolicy(self, writePolicy: str):
        self.__writePolicy = writePolicy

    @property
    def repl_Policy(self) -> str:
        return self.__repl_Policy

    @repl_Policy.setter
    def repl_Policy(self, repl_Policy: str):
        self.__repl_Policy = repl_Policy

    @property
    def MARTE_HwMemory_HwRAM465(self):
        return self.__MARTE_HwMemory_HwRAM465

    @MARTE_HwMemory_HwRAM465.setter
    def MARTE_HwMemory_HwRAM465(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwRAM__MARTE_HwMemory_HwRAM465", None)
        self.__MARTE_HwMemory_HwRAM465 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Boolean466"):
                opp_val = getattr(old_value, "NFP_Boolean466", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Boolean466", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Boolean466"):
                opp_val = getattr(value, "NFP_Boolean466", None)
                setattr(value, "NFP_Boolean466", self)

    @property
    def MARTE_HwMemory_HwRAM459(self):
        return self.__MARTE_HwMemory_HwRAM459

    @MARTE_HwMemory_HwRAM459.setter
    def MARTE_HwMemory_HwRAM459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwRAM__MARTE_HwMemory_HwRAM459", None)
        self.__MARTE_HwMemory_HwRAM459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Boolean460"):
                opp_val = getattr(old_value, "NFP_Boolean460", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Boolean460", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Boolean460"):
                opp_val = getattr(value, "NFP_Boolean460", None)
                setattr(value, "NFP_Boolean460", self)

    @property
    def MARTE_HwMemory_HwRAM(self):
        return self.__MARTE_HwMemory_HwRAM

    @MARTE_HwMemory_HwRAM.setter
    def MARTE_HwMemory_HwRAM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwRAM__MARTE_HwMemory_HwRAM", None)
        self.__MARTE_HwMemory_HwRAM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HwMemory_MemoryOrganization"):
                opp_val = getattr(old_value, "HwMemory_MemoryOrganization", None)
                if opp_val == self:
                    setattr(old_value, "HwMemory_MemoryOrganization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HwMemory_MemoryOrganization"):
                opp_val = getattr(value, "HwMemory_MemoryOrganization", None)
                setattr(value, "HwMemory_MemoryOrganization", self)

    @property
    def MARTE_HwMemory_HwRAM462(self):
        return self.__MARTE_HwMemory_HwRAM462

    @MARTE_HwMemory_HwRAM462.setter
    def MARTE_HwMemory_HwRAM462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwRAM__MARTE_HwMemory_HwRAM462", None)
        self.__MARTE_HwMemory_HwRAM462 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Boolean463"):
                opp_val = getattr(old_value, "NFP_Boolean463", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Boolean463", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Boolean463"):
                opp_val = getattr(value, "NFP_Boolean463", None)
                setattr(value, "NFP_Boolean463", self)

class MARTE_HwMemory_MemoryOrganization:

    pass
class MARTE_HwMemory_CacheStructure:

    pass
class HwMemory_Timing:

    pass
class MARTE_HwMemory_Timing:

    pass
class HwStorageManager:

    pass
class MARTE_HwStorageManager_HwMMU(HwStorageManager):

    pass
class HwStorageManager_HwStorageManager:

    pass
class HwMemory_HwMemory:

    pass
class GRM_StorageResource:

    pass
class HwProtocol_HwProtocol:

    pass
class HwEndPoint:

    pass
class MARTE_HwIO_HwPin(HwEndPoint):

    pass
class MARTE_HwPackage_HwPackagePin(HwEndPoint):

    def __init__(self, pinNo: str, altNames: str, HRM592: set["HwIO_HwPin"] = None, MARTE_HwPackage_HwPackagePin: set["HwPackage_HwWire"] = None):
        self.pinNo = pinNo
        self.altNames = altNames
        self.HRM592 = HRM592 if HRM592 is not None else set()
        self.MARTE_HwPackage_HwPackagePin = MARTE_HwPackage_HwPackagePin if MARTE_HwPackage_HwPackagePin is not None else set()
        
    @property
    def pinNo(self) -> str:
        return self.__pinNo

    @pinNo.setter
    def pinNo(self, pinNo: str):
        self.__pinNo = pinNo

    @property
    def altNames(self) -> str:
        return self.__altNames

    @altNames.setter
    def altNames(self, altNames: str):
        self.__altNames = altNames

    @property
    def HRM592(self):
        return self.__HRM592

    @HRM592.setter
    def HRM592(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwPackage_HwPackagePin__HRM592", None)
        self.__HRM592 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MARTE_DesignModel593"):
                    opp_val = getattr(item, "MARTE_DesignModel593", None)
                    
                    if opp_val == self:
                        setattr(item, "MARTE_DesignModel593", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MARTE_DesignModel593"):
                    opp_val = getattr(item, "MARTE_DesignModel593", None)
                    
                    setattr(item, "MARTE_DesignModel593", self)
                    

    @property
    def MARTE_HwPackage_HwPackagePin(self):
        return self.__MARTE_HwPackage_HwPackagePin

    @MARTE_HwPackage_HwPackagePin.setter
    def MARTE_HwPackage_HwPackagePin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwPackage_HwPackagePin__MARTE_HwPackage_HwPackagePin", None)
        self.__MARTE_HwPackage_HwPackagePin = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwPackage_HwWire"):
                    opp_val = getattr(item, "HwPackage_HwWire", None)
                    
                    if opp_val == self:
                        setattr(item, "HwPackage_HwWire", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwPackage_HwWire"):
                    opp_val = getattr(item, "HwPackage_HwWire", None)
                    
                    setattr(item, "HwPackage_HwWire", self)
                    

class MARTE_HwCommunication_HwPort(HwEndPoint):

    pass
class GRM_CommunicationEndPoint:

    pass
class HwCommunication_HwMedia:

    pass
class HwCommunicationResource:

    pass
class MARTE_HwCommunication_HwArbiter(HwCommunicationResource):

    pass
class NFP_Boolean:

    pass
class HwMedia:

    pass
class MARTE_HwPackage_HwWire(HwMedia):

    pass
class MARTE_HwCommunication_HwConnection(HwMedia):

    pass
class MARTE_HwCommunication_HwBridge(HwMedia):

    pass
class MARTE_HwIO_HwLine(HwMedia):

    pass
class MARTE_HwCommunication_HwBus(HwMedia):

    pass
class HwCommunication_HwArbiter:

    pass
class MARTE_HwStorageManager_HwDMA(HwStorageManager_HwStorageManager, HwCommunication_HwArbiter):

    pass
class HwCommunication_HwCommunicationResource:

    pass
class MARTE_HwCommunication_HwEndPoint(HwCommunication_HwCommunicationResource, GRM_CommunicationEndPoint):

    pass
class GRM_CommunicationMedia:

    pass
class MARTE_SW_Interaction_SwCommunicationResource(GRM_CommunicationMedia, SW_Interaction_SwInteractionResource):

    pass
class MARTE_HwCommunication_HwMedia(HwCommunication_HwCommunicationResource, GRM_CommunicationMedia):

    pass
class HwComputing_HwComputingResource:

    pass
class HwMemory_HwRAM:

    pass
class HwCommunication_HwPort:

    pass
class HwIO_HwPin:

    pass
class HwPackage_HwPackage:

    pass
class HwRegister_HwRegister:

    pass
class HwDevice_HwPeripheral:

    pass
class HwComputing_HwProcessor:

    pass
class NFP_String:

    pass
class HwResource:

    pass
class MARTE_HwLayout_HwComponent(HwResource):

    def __init__(self, kind: str, MARTE_HwLayout_HwComponent: set["NFP_Length"] = None, MARTE_HwLayout_HwComponent537: "NFP_Area" = None, MARTE_HwLayout_HwComponent539: set["NFP_NaturalInterval"] = None, MARTE_HwLayout_HwComponent541: set["NFP_Natural"] = None, MARTE_HwLayout_HwComponent544: "NFP_Natural" = None, MARTE_HwLayout_HwComponent547: "NFP_Real" = None, MARTE_HwLayout_HwComponent554: set["HwGeneral_HwResourceService"] = None, MARTE_HwLayout_HwComponent557: "NFP_Power" = None, MARTE_HwLayout_HwComponent560: "NFP_Power" = None, MARTE_HwLayout_HwComponent563: set["HwLayout_HwComponent"] = None, MARTE_HwLayout_HwComponent550: "NFP_Price" = None, MARTE_HwLayout_HwComponent552: set["HwLayout_Env_Condition"] = None):
        self.kind = kind
        self.MARTE_HwLayout_HwComponent = MARTE_HwLayout_HwComponent if MARTE_HwLayout_HwComponent is not None else set()
        self.MARTE_HwLayout_HwComponent537 = MARTE_HwLayout_HwComponent537
        self.MARTE_HwLayout_HwComponent539 = MARTE_HwLayout_HwComponent539 if MARTE_HwLayout_HwComponent539 is not None else set()
        self.MARTE_HwLayout_HwComponent541 = MARTE_HwLayout_HwComponent541 if MARTE_HwLayout_HwComponent541 is not None else set()
        self.MARTE_HwLayout_HwComponent544 = MARTE_HwLayout_HwComponent544
        self.MARTE_HwLayout_HwComponent547 = MARTE_HwLayout_HwComponent547
        self.MARTE_HwLayout_HwComponent554 = MARTE_HwLayout_HwComponent554 if MARTE_HwLayout_HwComponent554 is not None else set()
        self.MARTE_HwLayout_HwComponent557 = MARTE_HwLayout_HwComponent557
        self.MARTE_HwLayout_HwComponent560 = MARTE_HwLayout_HwComponent560
        self.MARTE_HwLayout_HwComponent563 = MARTE_HwLayout_HwComponent563 if MARTE_HwLayout_HwComponent563 is not None else set()
        self.MARTE_HwLayout_HwComponent550 = MARTE_HwLayout_HwComponent550
        self.MARTE_HwLayout_HwComponent552 = MARTE_HwLayout_HwComponent552 if MARTE_HwLayout_HwComponent552 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def MARTE_HwLayout_HwComponent537(self):
        return self.__MARTE_HwLayout_HwComponent537

    @MARTE_HwLayout_HwComponent537.setter
    def MARTE_HwLayout_HwComponent537(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent537", None)
        self.__MARTE_HwLayout_HwComponent537 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Area"):
                opp_val = getattr(old_value, "NFP_Area", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Area", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Area"):
                opp_val = getattr(value, "NFP_Area", None)
                setattr(value, "NFP_Area", self)

    @property
    def MARTE_HwLayout_HwComponent563(self):
        return self.__MARTE_HwLayout_HwComponent563

    @MARTE_HwLayout_HwComponent563.setter
    def MARTE_HwLayout_HwComponent563(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent563", None)
        self.__MARTE_HwLayout_HwComponent563 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwLayout_HwComponent"):
                    opp_val = getattr(item, "HwLayout_HwComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "HwLayout_HwComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwLayout_HwComponent"):
                    opp_val = getattr(item, "HwLayout_HwComponent", None)
                    
                    setattr(item, "HwLayout_HwComponent", self)
                    

    @property
    def MARTE_HwLayout_HwComponent552(self):
        return self.__MARTE_HwLayout_HwComponent552

    @MARTE_HwLayout_HwComponent552.setter
    def MARTE_HwLayout_HwComponent552(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent552", None)
        self.__MARTE_HwLayout_HwComponent552 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwLayout_Env_Condition"):
                    opp_val = getattr(item, "HwLayout_Env_Condition", None)
                    
                    if opp_val == self:
                        setattr(item, "HwLayout_Env_Condition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwLayout_Env_Condition"):
                    opp_val = getattr(item, "HwLayout_Env_Condition", None)
                    
                    setattr(item, "HwLayout_Env_Condition", self)
                    

    @property
    def MARTE_HwLayout_HwComponent554(self):
        return self.__MARTE_HwLayout_HwComponent554

    @MARTE_HwLayout_HwComponent554.setter
    def MARTE_HwLayout_HwComponent554(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent554", None)
        self.__MARTE_HwLayout_HwComponent554 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResourceService555"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService555", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResourceService555", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResourceService555"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService555", None)
                    
                    setattr(item, "HwGeneral_HwResourceService555", self)
                    

    @property
    def MARTE_HwLayout_HwComponent557(self):
        return self.__MARTE_HwLayout_HwComponent557

    @MARTE_HwLayout_HwComponent557.setter
    def MARTE_HwLayout_HwComponent557(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent557", None)
        self.__MARTE_HwLayout_HwComponent557 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Power558"):
                opp_val = getattr(old_value, "NFP_Power558", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Power558", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Power558"):
                opp_val = getattr(value, "NFP_Power558", None)
                setattr(value, "NFP_Power558", self)

    @property
    def MARTE_HwLayout_HwComponent539(self):
        return self.__MARTE_HwLayout_HwComponent539

    @MARTE_HwLayout_HwComponent539.setter
    def MARTE_HwLayout_HwComponent539(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent539", None)
        self.__MARTE_HwLayout_HwComponent539 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_NaturalInterval"):
                    opp_val = getattr(item, "NFP_NaturalInterval", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_NaturalInterval", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_NaturalInterval"):
                    opp_val = getattr(item, "NFP_NaturalInterval", None)
                    
                    setattr(item, "NFP_NaturalInterval", self)
                    

    @property
    def MARTE_HwLayout_HwComponent547(self):
        return self.__MARTE_HwLayout_HwComponent547

    @MARTE_HwLayout_HwComponent547.setter
    def MARTE_HwLayout_HwComponent547(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent547", None)
        self.__MARTE_HwLayout_HwComponent547 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Real548"):
                opp_val = getattr(old_value, "NFP_Real548", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Real548", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Real548"):
                opp_val = getattr(value, "NFP_Real548", None)
                setattr(value, "NFP_Real548", self)

    @property
    def MARTE_HwLayout_HwComponent(self):
        return self.__MARTE_HwLayout_HwComponent

    @MARTE_HwLayout_HwComponent.setter
    def MARTE_HwLayout_HwComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent", None)
        self.__MARTE_HwLayout_HwComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_Length"):
                    opp_val = getattr(item, "NFP_Length", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_Length", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_Length"):
                    opp_val = getattr(item, "NFP_Length", None)
                    
                    setattr(item, "NFP_Length", self)
                    

    @property
    def MARTE_HwLayout_HwComponent541(self):
        return self.__MARTE_HwLayout_HwComponent541

    @MARTE_HwLayout_HwComponent541.setter
    def MARTE_HwLayout_HwComponent541(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent541", None)
        self.__MARTE_HwLayout_HwComponent541 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_Natural542"):
                    opp_val = getattr(item, "NFP_Natural542", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_Natural542", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_Natural542"):
                    opp_val = getattr(item, "NFP_Natural542", None)
                    
                    setattr(item, "NFP_Natural542", self)
                    

    @property
    def MARTE_HwLayout_HwComponent560(self):
        return self.__MARTE_HwLayout_HwComponent560

    @MARTE_HwLayout_HwComponent560.setter
    def MARTE_HwLayout_HwComponent560(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent560", None)
        self.__MARTE_HwLayout_HwComponent560 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Power561"):
                opp_val = getattr(old_value, "NFP_Power561", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Power561", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Power561"):
                opp_val = getattr(value, "NFP_Power561", None)
                setattr(value, "NFP_Power561", self)

    @property
    def MARTE_HwLayout_HwComponent544(self):
        return self.__MARTE_HwLayout_HwComponent544

    @MARTE_HwLayout_HwComponent544.setter
    def MARTE_HwLayout_HwComponent544(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent544", None)
        self.__MARTE_HwLayout_HwComponent544 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Natural545"):
                opp_val = getattr(old_value, "NFP_Natural545", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Natural545", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Natural545"):
                opp_val = getattr(value, "NFP_Natural545", None)
                setattr(value, "NFP_Natural545", self)

    @property
    def MARTE_HwLayout_HwComponent550(self):
        return self.__MARTE_HwLayout_HwComponent550

    @MARTE_HwLayout_HwComponent550.setter
    def MARTE_HwLayout_HwComponent550(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent550", None)
        self.__MARTE_HwLayout_HwComponent550 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Price"):
                opp_val = getattr(old_value, "NFP_Price", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Price", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Price"):
                opp_val = getattr(value, "NFP_Price", None)
                setattr(value, "NFP_Price", self)

class MARTE_HwCommunication_HwCommunicationResource(HwResource):

    pass
class MARTE_HwComputing_HwISA(HwResource):

    def __init__(self, type: str, MARTE_HwComputing_HwISA: "NFP_String" = None, MARTE_HwComputing_HwISA348: "NFP_DataSize" = None):
        self.type = type
        self.MARTE_HwComputing_HwISA = MARTE_HwComputing_HwISA
        self.MARTE_HwComputing_HwISA348 = MARTE_HwComputing_HwISA348
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def MARTE_HwComputing_HwISA(self):
        return self.__MARTE_HwComputing_HwISA

    @MARTE_HwComputing_HwISA.setter
    def MARTE_HwComputing_HwISA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwISA__MARTE_HwComputing_HwISA", None)
        self.__MARTE_HwComputing_HwISA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_String"):
                opp_val = getattr(old_value, "NFP_String", None)
                if opp_val == self:
                    setattr(old_value, "NFP_String", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_String"):
                opp_val = getattr(value, "NFP_String", None)
                setattr(value, "NFP_String", self)

    @property
    def MARTE_HwComputing_HwISA348(self):
        return self.__MARTE_HwComputing_HwISA348

    @MARTE_HwComputing_HwISA348.setter
    def MARTE_HwComputing_HwISA348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwISA__MARTE_HwComputing_HwISA348", None)
        self.__MARTE_HwComputing_HwISA348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_DataSize349"):
                opp_val = getattr(old_value, "NFP_DataSize349", None)
                if opp_val == self:
                    setattr(old_value, "NFP_DataSize349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_DataSize349"):
                opp_val = getattr(value, "NFP_DataSize349", None)
                setattr(value, "NFP_DataSize349", self)

class HwComputing_PLD_Organization:

    pass
class MARTE_HwComputing_HwBranchPredictor(HwResource):

    pass
class NFP_FrequencyInterval:

    pass
class HwGeneral_HwResource:

    pass
class MARTE_HwTiming_HwTimingResource(GRM_TimingResource, HwGeneral_HwResource):

    pass
class MARTE_HwDevice_HwDevice(HwGeneral_HwResource, GRM_DeviceResource):

    pass
class MARTE_HwStorageManager_HwStorageManager(GRM_StorageResource, HwGeneral_HwResource):

    pass
class MARTE_HwMemory_HwMemory(GRM_StorageResource, HwGeneral_HwResource):

    pass
class HwStorageManager_HwMMU:

    pass
class HwMemory_HwCache:

    pass
class HwComputing_HwBranchPredictor:

    pass
class HwComputing_HwISA:

    pass
class NFP_Natural:

    pass
class MARTE_HwComputing_PLD_Organization:

    def __init__(self, class: str, MARTE_HwComputing_PLD_Organization: "NFP_Integer" = None, MARTE_HwComputing_PLD_Organization313: "NFP_Natural" = None):
        self.class = class
        self.MARTE_HwComputing_PLD_Organization = MARTE_HwComputing_PLD_Organization
        self.MARTE_HwComputing_PLD_Organization313 = MARTE_HwComputing_PLD_Organization313
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def MARTE_HwComputing_PLD_Organization313(self):
        return self.__MARTE_HwComputing_PLD_Organization313

    @MARTE_HwComputing_PLD_Organization313.setter
    def MARTE_HwComputing_PLD_Organization313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_PLD_Organization__MARTE_HwComputing_PLD_Organization313", None)
        self.__MARTE_HwComputing_PLD_Organization313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Natural"):
                opp_val = getattr(old_value, "NFP_Natural", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Natural", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Natural"):
                opp_val = getattr(value, "NFP_Natural", None)
                setattr(value, "NFP_Natural", self)

    @property
    def MARTE_HwComputing_PLD_Organization(self):
        return self.__MARTE_HwComputing_PLD_Organization

    @MARTE_HwComputing_PLD_Organization.setter
    def MARTE_HwComputing_PLD_Organization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_PLD_Organization__MARTE_HwComputing_PLD_Organization", None)
        self.__MARTE_HwComputing_PLD_Organization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Integer311"):
                opp_val = getattr(old_value, "NFP_Integer311", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Integer311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Integer311"):
                opp_val = getattr(value, "NFP_Integer311", None)
                setattr(value, "NFP_Integer311", self)

class HwComputingResource:

    pass
class MARTE_HwComputing_HwPLD(HwComputingResource):

    def __init__(self, technology: str, MARTE_HwComputing_HwPLD: "HwComputing_PLD_Organization" = None, MARTE_HwComputing_HwPLD352: "NFP_Natural" = None, MARTE_HwComputing_HwPLD355: "NFP_Natural" = None, MARTE_HwComputing_HwPLD358: "NFP_Natural" = None, MARTE_HwComputing_HwPLD361: set["HwMemory_HwRAM"] = None, MARTE_HwComputing_HwPLD363: set["HwComputing_HwComputingResource"] = None):
        self.technology = technology
        self.MARTE_HwComputing_HwPLD = MARTE_HwComputing_HwPLD
        self.MARTE_HwComputing_HwPLD352 = MARTE_HwComputing_HwPLD352
        self.MARTE_HwComputing_HwPLD355 = MARTE_HwComputing_HwPLD355
        self.MARTE_HwComputing_HwPLD358 = MARTE_HwComputing_HwPLD358
        self.MARTE_HwComputing_HwPLD361 = MARTE_HwComputing_HwPLD361 if MARTE_HwComputing_HwPLD361 is not None else set()
        self.MARTE_HwComputing_HwPLD363 = MARTE_HwComputing_HwPLD363 if MARTE_HwComputing_HwPLD363 is not None else set()
        
    @property
    def technology(self) -> str:
        return self.__technology

    @technology.setter
    def technology(self, technology: str):
        self.__technology = technology

    @property
    def MARTE_HwComputing_HwPLD358(self):
        return self.__MARTE_HwComputing_HwPLD358

    @MARTE_HwComputing_HwPLD358.setter
    def MARTE_HwComputing_HwPLD358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD358", None)
        self.__MARTE_HwComputing_HwPLD358 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Natural359"):
                opp_val = getattr(old_value, "NFP_Natural359", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Natural359", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Natural359"):
                opp_val = getattr(value, "NFP_Natural359", None)
                setattr(value, "NFP_Natural359", self)

    @property
    def MARTE_HwComputing_HwPLD(self):
        return self.__MARTE_HwComputing_HwPLD

    @MARTE_HwComputing_HwPLD.setter
    def MARTE_HwComputing_HwPLD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD", None)
        self.__MARTE_HwComputing_HwPLD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HwComputing_PLD_Organization"):
                opp_val = getattr(old_value, "HwComputing_PLD_Organization", None)
                if opp_val == self:
                    setattr(old_value, "HwComputing_PLD_Organization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HwComputing_PLD_Organization"):
                opp_val = getattr(value, "HwComputing_PLD_Organization", None)
                setattr(value, "HwComputing_PLD_Organization", self)

    @property
    def MARTE_HwComputing_HwPLD361(self):
        return self.__MARTE_HwComputing_HwPLD361

    @MARTE_HwComputing_HwPLD361.setter
    def MARTE_HwComputing_HwPLD361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD361", None)
        self.__MARTE_HwComputing_HwPLD361 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwMemory_HwRAM"):
                    opp_val = getattr(item, "HwMemory_HwRAM", None)
                    
                    if opp_val == self:
                        setattr(item, "HwMemory_HwRAM", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwMemory_HwRAM"):
                    opp_val = getattr(item, "HwMemory_HwRAM", None)
                    
                    setattr(item, "HwMemory_HwRAM", self)
                    

    @property
    def MARTE_HwComputing_HwPLD363(self):
        return self.__MARTE_HwComputing_HwPLD363

    @MARTE_HwComputing_HwPLD363.setter
    def MARTE_HwComputing_HwPLD363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD363", None)
        self.__MARTE_HwComputing_HwPLD363 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwComputing_HwComputingResource"):
                    opp_val = getattr(item, "HwComputing_HwComputingResource", None)
                    
                    if opp_val == self:
                        setattr(item, "HwComputing_HwComputingResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwComputing_HwComputingResource"):
                    opp_val = getattr(item, "HwComputing_HwComputingResource", None)
                    
                    setattr(item, "HwComputing_HwComputingResource", self)
                    

    @property
    def MARTE_HwComputing_HwPLD355(self):
        return self.__MARTE_HwComputing_HwPLD355

    @MARTE_HwComputing_HwPLD355.setter
    def MARTE_HwComputing_HwPLD355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD355", None)
        self.__MARTE_HwComputing_HwPLD355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Natural356"):
                opp_val = getattr(old_value, "NFP_Natural356", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Natural356", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Natural356"):
                opp_val = getattr(value, "NFP_Natural356", None)
                setattr(value, "NFP_Natural356", self)

    @property
    def MARTE_HwComputing_HwPLD352(self):
        return self.__MARTE_HwComputing_HwPLD352

    @MARTE_HwComputing_HwPLD352.setter
    def MARTE_HwComputing_HwPLD352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD352", None)
        self.__MARTE_HwComputing_HwPLD352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Natural353"):
                opp_val = getattr(old_value, "NFP_Natural353", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Natural353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Natural353"):
                opp_val = getattr(value, "NFP_Natural353", None)
                setattr(value, "NFP_Natural353", self)

class MARTE_HwComputing_HwASIC(HwComputingResource):

    pass
class MARTE_HwComputing_HwMCU(HwComputingResource):

    pass
class MARTE_HwComputing_HwProcessor(HwComputingResource):

    pass
class MARTE_HLAM_RtService:

    def __init__(self, concPolicy: str, exeKind: str, isAtomic: str, synchKind: str, MARTE_HLAM_RtService: "HLAM_MARTE_BehavioralFeature" = None):
        self.concPolicy = concPolicy
        self.exeKind = exeKind
        self.isAtomic = isAtomic
        self.synchKind = synchKind
        self.MARTE_HLAM_RtService = MARTE_HLAM_RtService
        
    @property
    def concPolicy(self) -> str:
        return self.__concPolicy

    @concPolicy.setter
    def concPolicy(self, concPolicy: str):
        self.__concPolicy = concPolicy

    @property
    def isAtomic(self) -> str:
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic

    @property
    def synchKind(self) -> str:
        return self.__synchKind

    @synchKind.setter
    def synchKind(self, synchKind: str):
        self.__synchKind = synchKind

    @property
    def exeKind(self) -> str:
        return self.__exeKind

    @exeKind.setter
    def exeKind(self, exeKind: str):
        self.__exeKind = exeKind

    @property
    def MARTE_HLAM_RtService(self):
        return self.__MARTE_HLAM_RtService

    @MARTE_HLAM_RtService.setter
    def MARTE_HLAM_RtService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtService__MARTE_HLAM_RtService", None)
        self.__MARTE_HLAM_RtService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_BehavioralFeature309"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioralFeature309", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioralFeature309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioralFeature309"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioralFeature309", None)
                setattr(value, "HLAM_MARTE_BehavioralFeature309", self)

class HLAM_MARTE_Comment:

    pass
class MARTE_HLAM_RtAction:

    def __init__(self, isAtomic: str, synchKind: str, MARTE_HLAM_RtAction: "NFP_DataSize" = None, MARTE_HLAM_RtAction303: "HLAM_MARTE_BehavioralFeature" = None, MARTE_HLAM_RtAction306: "HLAM_MARTE_InvocationAction" = None):
        self.isAtomic = isAtomic
        self.synchKind = synchKind
        self.MARTE_HLAM_RtAction = MARTE_HLAM_RtAction
        self.MARTE_HLAM_RtAction303 = MARTE_HLAM_RtAction303
        self.MARTE_HLAM_RtAction306 = MARTE_HLAM_RtAction306
        
    @property
    def synchKind(self) -> str:
        return self.__synchKind

    @synchKind.setter
    def synchKind(self, synchKind: str):
        self.__synchKind = synchKind

    @property
    def isAtomic(self) -> str:
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic

    @property
    def MARTE_HLAM_RtAction306(self):
        return self.__MARTE_HLAM_RtAction306

    @MARTE_HLAM_RtAction306.setter
    def MARTE_HLAM_RtAction306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtAction__MARTE_HLAM_RtAction306", None)
        self.__MARTE_HLAM_RtAction306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_InvocationAction307"):
                opp_val = getattr(old_value, "HLAM_MARTE_InvocationAction307", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_InvocationAction307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_InvocationAction307"):
                opp_val = getattr(value, "HLAM_MARTE_InvocationAction307", None)
                setattr(value, "HLAM_MARTE_InvocationAction307", self)

    @property
    def MARTE_HLAM_RtAction(self):
        return self.__MARTE_HLAM_RtAction

    @MARTE_HLAM_RtAction.setter
    def MARTE_HLAM_RtAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtAction__MARTE_HLAM_RtAction", None)
        self.__MARTE_HLAM_RtAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_DataSize301"):
                opp_val = getattr(old_value, "NFP_DataSize301", None)
                if opp_val == self:
                    setattr(old_value, "NFP_DataSize301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_DataSize301"):
                opp_val = getattr(value, "NFP_DataSize301", None)
                setattr(value, "NFP_DataSize301", self)

    @property
    def MARTE_HLAM_RtAction303(self):
        return self.__MARTE_HLAM_RtAction303

    @MARTE_HLAM_RtAction303.setter
    def MARTE_HLAM_RtAction303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtAction__MARTE_HLAM_RtAction303", None)
        self.__MARTE_HLAM_RtAction303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_BehavioralFeature304"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioralFeature304", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioralFeature304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioralFeature304"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioralFeature304", None)
                setattr(value, "HLAM_MARTE_BehavioralFeature304", self)

class ArrivalPattern:

    pass
class UtilityType:

    pass
class MARTE_HLAM_RtSpecification:

    pass
class NFP_Percentage:

    pass
class NFP_DateTime:

    pass
class Time_TimedInstantObservation:

    pass
class HLAM_RtSpecification:

    pass
class HLAM_MARTE_InvocationAction:

    pass
class HLAM_MARTE_Port:

    pass
class HLAM_MARTE_Signal:

    pass
class HLAM_MARTE_Message:

    pass
class HLAM_MARTE_BehavioralFeature:

    pass
class MARTE_HLAM_RtFeature:

    pass
class HLAM_MARTE_Operation:

    pass
class HLAM_MARTE_Behavior:

    pass
class MARTE_HLAM_PpUnit:

    def __init__(self, concPolicy: str, MARTE_HLAM_PpUnit: "NFP_DataSize" = None, MARTE_HLAM_PpUnit264: "HLAM_MARTE_BehavioredClassifier" = None):
        self.concPolicy = concPolicy
        self.MARTE_HLAM_PpUnit = MARTE_HLAM_PpUnit
        self.MARTE_HLAM_PpUnit264 = MARTE_HLAM_PpUnit264
        
    @property
    def concPolicy(self) -> str:
        return self.__concPolicy

    @concPolicy.setter
    def concPolicy(self, concPolicy: str):
        self.__concPolicy = concPolicy

    @property
    def MARTE_HLAM_PpUnit(self):
        return self.__MARTE_HLAM_PpUnit

    @MARTE_HLAM_PpUnit.setter
    def MARTE_HLAM_PpUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_PpUnit__MARTE_HLAM_PpUnit", None)
        self.__MARTE_HLAM_PpUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_DataSize262"):
                opp_val = getattr(old_value, "NFP_DataSize262", None)
                if opp_val == self:
                    setattr(old_value, "NFP_DataSize262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_DataSize262"):
                opp_val = getattr(value, "NFP_DataSize262", None)
                setattr(value, "NFP_DataSize262", self)

    @property
    def MARTE_HLAM_PpUnit264(self):
        return self.__MARTE_HLAM_PpUnit264

    @MARTE_HLAM_PpUnit264.setter
    def MARTE_HLAM_PpUnit264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_PpUnit__MARTE_HLAM_PpUnit264", None)
        self.__MARTE_HLAM_PpUnit264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_BehavioredClassifier265"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioredClassifier265", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioredClassifier265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioredClassifier265"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioredClassifier265", None)
                setattr(value, "HLAM_MARTE_BehavioredClassifier265", self)

class HLAM_MARTE_BehavioredClassifier:

    pass
class MARTE_DataTypes_ChoiceType:

    pass
class MARTE_HLAM_RtUnit:

    def __init__(self, isDynamic: str, isMain: str, srPoolSize: str, queueSchedPolicy: str, queueSize: str, srPoolPolicy: str, MARTE_HLAM_RtUnit252: "HLAM_MARTE_Operation" = None, MARTE_HLAM_RtUnit254: "NFP_DataSize" = None, MARTE_HLAM_RtUnit257: "HLAM_MARTE_BehavioredClassifier" = None, MARTE_HLAM_RtUnit259: "NFP_DataSize" = None, MARTE_HLAM_RtUnit: "NFP_Duration" = None, MARTE_HLAM_RtUnit250: "HLAM_MARTE_Behavior" = None):
        self.isDynamic = isDynamic
        self.isMain = isMain
        self.srPoolSize = srPoolSize
        self.queueSchedPolicy = queueSchedPolicy
        self.queueSize = queueSize
        self.srPoolPolicy = srPoolPolicy
        self.MARTE_HLAM_RtUnit252 = MARTE_HLAM_RtUnit252
        self.MARTE_HLAM_RtUnit254 = MARTE_HLAM_RtUnit254
        self.MARTE_HLAM_RtUnit257 = MARTE_HLAM_RtUnit257
        self.MARTE_HLAM_RtUnit259 = MARTE_HLAM_RtUnit259
        self.MARTE_HLAM_RtUnit = MARTE_HLAM_RtUnit
        self.MARTE_HLAM_RtUnit250 = MARTE_HLAM_RtUnit250
        
    @property
    def queueSchedPolicy(self) -> str:
        return self.__queueSchedPolicy

    @queueSchedPolicy.setter
    def queueSchedPolicy(self, queueSchedPolicy: str):
        self.__queueSchedPolicy = queueSchedPolicy

    @property
    def isDynamic(self) -> str:
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic

    @property
    def srPoolPolicy(self) -> str:
        return self.__srPoolPolicy

    @srPoolPolicy.setter
    def srPoolPolicy(self, srPoolPolicy: str):
        self.__srPoolPolicy = srPoolPolicy

    @property
    def srPoolSize(self) -> str:
        return self.__srPoolSize

    @srPoolSize.setter
    def srPoolSize(self, srPoolSize: str):
        self.__srPoolSize = srPoolSize

    @property
    def isMain(self) -> str:
        return self.__isMain

    @isMain.setter
    def isMain(self, isMain: str):
        self.__isMain = isMain

    @property
    def queueSize(self) -> str:
        return self.__queueSize

    @queueSize.setter
    def queueSize(self, queueSize: str):
        self.__queueSize = queueSize

    @property
    def MARTE_HLAM_RtUnit252(self):
        return self.__MARTE_HLAM_RtUnit252

    @MARTE_HLAM_RtUnit252.setter
    def MARTE_HLAM_RtUnit252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit252", None)
        self.__MARTE_HLAM_RtUnit252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_Operation"):
                opp_val = getattr(old_value, "HLAM_MARTE_Operation", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_Operation"):
                opp_val = getattr(value, "HLAM_MARTE_Operation", None)
                setattr(value, "HLAM_MARTE_Operation", self)

    @property
    def MARTE_HLAM_RtUnit(self):
        return self.__MARTE_HLAM_RtUnit

    @MARTE_HLAM_RtUnit.setter
    def MARTE_HLAM_RtUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit", None)
        self.__MARTE_HLAM_RtUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Duration248"):
                opp_val = getattr(old_value, "NFP_Duration248", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Duration248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Duration248"):
                opp_val = getattr(value, "NFP_Duration248", None)
                setattr(value, "NFP_Duration248", self)

    @property
    def MARTE_HLAM_RtUnit257(self):
        return self.__MARTE_HLAM_RtUnit257

    @MARTE_HLAM_RtUnit257.setter
    def MARTE_HLAM_RtUnit257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit257", None)
        self.__MARTE_HLAM_RtUnit257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_BehavioredClassifier"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioredClassifier", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioredClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioredClassifier"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioredClassifier", None)
                setattr(value, "HLAM_MARTE_BehavioredClassifier", self)

    @property
    def MARTE_HLAM_RtUnit259(self):
        return self.__MARTE_HLAM_RtUnit259

    @MARTE_HLAM_RtUnit259.setter
    def MARTE_HLAM_RtUnit259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit259", None)
        self.__MARTE_HLAM_RtUnit259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_DataSize260"):
                opp_val = getattr(old_value, "NFP_DataSize260", None)
                if opp_val == self:
                    setattr(old_value, "NFP_DataSize260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_DataSize260"):
                opp_val = getattr(value, "NFP_DataSize260", None)
                setattr(value, "NFP_DataSize260", self)

    @property
    def MARTE_HLAM_RtUnit254(self):
        return self.__MARTE_HLAM_RtUnit254

    @MARTE_HLAM_RtUnit254.setter
    def MARTE_HLAM_RtUnit254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit254", None)
        self.__MARTE_HLAM_RtUnit254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_DataSize255"):
                opp_val = getattr(old_value, "NFP_DataSize255", None)
                if opp_val == self:
                    setattr(old_value, "NFP_DataSize255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_DataSize255"):
                opp_val = getattr(value, "NFP_DataSize255", None)
                setattr(value, "NFP_DataSize255", self)

    @property
    def MARTE_HLAM_RtUnit250(self):
        return self.__MARTE_HLAM_RtUnit250

    @MARTE_HLAM_RtUnit250.setter
    def MARTE_HLAM_RtUnit250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit250", None)
        self.__MARTE_HLAM_RtUnit250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_Behavior"):
                opp_val = getattr(old_value, "HLAM_MARTE_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_Behavior"):
                opp_val = getattr(value, "HLAM_MARTE_Behavior", None)
                setattr(value, "HLAM_MARTE_Behavior", self)

class MARTE_DataTypes_TupleType:

    pass
class DataTypes_MARTE_Property:

    pass
class MARTE_DataTypes_BoundedSubtype:

    def __init__(self, maxValue: str, isMinOpen: bool, isMaxOpen: bool, minValue: str, MARTE_DataTypes_BoundedSubtype223: "DataTypes_MARTE_DataType" = None, MARTE_DataTypes_BoundedSubtype: "DataTypes_MARTE_Property" = None):
        self.maxValue = maxValue
        self.isMinOpen = isMinOpen
        self.isMaxOpen = isMaxOpen
        self.minValue = minValue
        self.MARTE_DataTypes_BoundedSubtype223 = MARTE_DataTypes_BoundedSubtype223
        self.MARTE_DataTypes_BoundedSubtype = MARTE_DataTypes_BoundedSubtype
        
    @property
    def isMinOpen(self) -> bool:
        return self.__isMinOpen

    @isMinOpen.setter
    def isMinOpen(self, isMinOpen: bool):
        self.__isMinOpen = isMinOpen

    @property
    def minValue(self) -> str:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: str):
        self.__minValue = minValue

    @property
    def isMaxOpen(self) -> bool:
        return self.__isMaxOpen

    @isMaxOpen.setter
    def isMaxOpen(self, isMaxOpen: bool):
        self.__isMaxOpen = isMaxOpen

    @property
    def maxValue(self) -> str:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: str):
        self.__maxValue = maxValue

    @property
    def MARTE_DataTypes_BoundedSubtype223(self):
        return self.__MARTE_DataTypes_BoundedSubtype223

    @MARTE_DataTypes_BoundedSubtype223.setter
    def MARTE_DataTypes_BoundedSubtype223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_DataTypes_BoundedSubtype__MARTE_DataTypes_BoundedSubtype223", None)
        self.__MARTE_DataTypes_BoundedSubtype223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataTypes_MARTE_DataType"):
                opp_val = getattr(old_value, "DataTypes_MARTE_DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataTypes_MARTE_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataTypes_MARTE_DataType"):
                opp_val = getattr(value, "DataTypes_MARTE_DataType", None)
                setattr(value, "DataTypes_MARTE_DataType", self)

    @property
    def MARTE_DataTypes_BoundedSubtype(self):
        return self.__MARTE_DataTypes_BoundedSubtype

    @MARTE_DataTypes_BoundedSubtype.setter
    def MARTE_DataTypes_BoundedSubtype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_DataTypes_BoundedSubtype__MARTE_DataTypes_BoundedSubtype", None)
        self.__MARTE_DataTypes_BoundedSubtype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataTypes_MARTE_Property"):
                opp_val = getattr(old_value, "DataTypes_MARTE_Property", None)
                if opp_val == self:
                    setattr(old_value, "DataTypes_MARTE_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataTypes_MARTE_Property"):
                opp_val = getattr(value, "DataTypes_MARTE_Property", None)
                setattr(value, "DataTypes_MARTE_Property", self)

class MARTE_DataTypes_CollectionType:

    pass
class MARTE_DataTypes_IntervalType:

    pass
class DataTypes_MARTE_DataType:

    pass
class RSM_MARTE_ConnectorEnd:

    pass
class Variables_MARTE_NamedElement:

    pass
class MARTE_Variables_ExpressionContext:

    pass
class Variables_MARTE_Property:

    pass
class MARTE_Variables_Var:

    def __init__(self, dir: str, MARTE_Variables_Var: "Variables_MARTE_Property" = None):
        self.dir = dir
        self.MARTE_Variables_Var = MARTE_Variables_Var
        
    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def MARTE_Variables_Var(self):
        return self.__MARTE_Variables_Var

    @MARTE_Variables_Var.setter
    def MARTE_Variables_Var(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Variables_Var__MARTE_Variables_Var", None)
        self.__MARTE_Variables_Var = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variables_MARTE_Property"):
                opp_val = getattr(old_value, "Variables_MARTE_Property", None)
                if opp_val == self:
                    setattr(old_value, "Variables_MARTE_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variables_MARTE_Property"):
                opp_val = getattr(value, "Variables_MARTE_Property", None)
                setattr(value, "Variables_MARTE_Property", self)

class RSM_MARTE_MultiplicityElement:

    pass
class MARTE_RSM_Shaped:

    pass
class TilerSpecification:

    pass
class ShapeSpecification:

    pass
class IntegerMatrix:

    pass
class GRM_ResourceUsage:

    pass
class MARTE_GQAM_GaScenario(GRM_ResourceUsage, Time_TimedProcessing):

    pass
class GRM_MARTE_NamedElement:

    pass
class Allocate:

    pass
class MARTE_SW_Concurrency_EntryPoint(Allocate):

    def __init__(self, isReentrant: str, MARTE_SW_Concurrency_EntryPoint: "SW_Concurrency_MARTE_BehavioralFeature" = None):
        self.isReentrant = isReentrant
        self.MARTE_SW_Concurrency_EntryPoint = MARTE_SW_Concurrency_EntryPoint
        
    @property
    def isReentrant(self) -> str:
        return self.__isReentrant

    @isReentrant.setter
    def isReentrant(self, isReentrant: str):
        self.__isReentrant = isReentrant

    @property
    def MARTE_SW_Concurrency_EntryPoint(self):
        return self.__MARTE_SW_Concurrency_EntryPoint

    @MARTE_SW_Concurrency_EntryPoint.setter
    def MARTE_SW_Concurrency_EntryPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_EntryPoint__MARTE_SW_Concurrency_EntryPoint", None)
        self.__MARTE_SW_Concurrency_EntryPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SW_Concurrency_MARTE_BehavioralFeature"):
                opp_val = getattr(old_value, "SW_Concurrency_MARTE_BehavioralFeature", None)
                if opp_val == self:
                    setattr(old_value, "SW_Concurrency_MARTE_BehavioralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SW_Concurrency_MARTE_BehavioralFeature"):
                opp_val = getattr(value, "SW_Concurrency_MARTE_BehavioralFeature", None)
                setattr(value, "SW_Concurrency_MARTE_BehavioralFeature", self)

class MARTE_RSM_Distribute(Allocate):

    pass
class IntegerVector:

    pass
class LinkTopology:

    pass
class MARTE_RSM_InterRepetition(LinkTopology):

    def __init__(self, isModulo: str, MARTE_RSM_InterRepetition: "IntegerVector" = None):
        self.isModulo = isModulo
        self.MARTE_RSM_InterRepetition = MARTE_RSM_InterRepetition
        
    @property
    def isModulo(self) -> str:
        return self.__isModulo

    @isModulo.setter
    def isModulo(self, isModulo: str):
        self.__isModulo = isModulo

    @property
    def MARTE_RSM_InterRepetition(self):
        return self.__MARTE_RSM_InterRepetition

    @MARTE_RSM_InterRepetition.setter
    def MARTE_RSM_InterRepetition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_RSM_InterRepetition__MARTE_RSM_InterRepetition", None)
        self.__MARTE_RSM_InterRepetition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IntegerVector"):
                opp_val = getattr(old_value, "IntegerVector", None)
                if opp_val == self:
                    setattr(old_value, "IntegerVector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IntegerVector"):
                opp_val = getattr(value, "IntegerVector", None)
                setattr(value, "IntegerVector", self)

class MARTE_RSM_Reshape(LinkTopology):

    pass
class MARTE_RSM_Tiler(LinkTopology):

    pass
class MARTE_RSM_DefaultLink(LinkTopology):

    pass
class RSM_MARTE_Connector:

    pass
class MARTE_RSM_LinkTopology(ABC):

    pass
class GRM_MARTE_CollaborationUse:

    pass
class GRM_MARTE_Collaboration:

    pass
class GRM_MARTE_Behavior:

    pass
class NFP_Energy:

    pass
class NFP_Power:

    pass
class NFP_DataSize:

    pass
class MARTE_GRM_ResourceUsage:

    pass
class GrService:

    pass
class MARTE_GRM_Acquire(GrService):

    def __init__(self, isBlocking: str):
        self.isBlocking = isBlocking
        
    @property
    def isBlocking(self) -> str:
        return self.__isBlocking

    @isBlocking.setter
    def isBlocking(self, isBlocking: str):
        self.__isBlocking = isBlocking

class MARTE_HwGeneral_HwResourceService(GrService):

    pass
class MARTE_SW_ResourceCore_SwAccessService(GrService):

    def __init__(self, isModifier: str, MARTE_SW_ResourceCore_SwAccessService: "SW_ResourceCore_MARTE_Property" = None):
        self.isModifier = isModifier
        self.MARTE_SW_ResourceCore_SwAccessService = MARTE_SW_ResourceCore_SwAccessService
        
    @property
    def isModifier(self) -> str:
        return self.__isModifier

    @isModifier.setter
    def isModifier(self, isModifier: str):
        self.__isModifier = isModifier

    @property
    def MARTE_SW_ResourceCore_SwAccessService(self):
        return self.__MARTE_SW_ResourceCore_SwAccessService

    @MARTE_SW_ResourceCore_SwAccessService.setter
    def MARTE_SW_ResourceCore_SwAccessService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_ResourceCore_SwAccessService__MARTE_SW_ResourceCore_SwAccessService", None)
        self.__MARTE_SW_ResourceCore_SwAccessService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SW_ResourceCore_MARTE_Property"):
                opp_val = getattr(old_value, "SW_ResourceCore_MARTE_Property", None)
                if opp_val == self:
                    setattr(old_value, "SW_ResourceCore_MARTE_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SW_ResourceCore_MARTE_Property"):
                opp_val = getattr(value, "SW_ResourceCore_MARTE_Property", None)
                setattr(value, "SW_ResourceCore_MARTE_Property", self)

class MARTE_GRM_Release(GrService):

    pass
class NFP_DataTxRate:

    pass
class NFP_Duration:

    pass
class GRM_MARTE_BehavioralFeature:

    pass
class GRM_MARTE_ExecutionSpecification:

    pass
class GRM_Resource:

    pass
class MARTE_GRM_GrService:

    pass
class TimingResource:

    pass
class MARTE_GRM_TimerResource(TimingResource):

    def __init__(self, isPeriodic: str, MARTE_GRM_TimerResource: "NFP_Duration" = None):
        self.isPeriodic = isPeriodic
        self.MARTE_GRM_TimerResource = MARTE_GRM_TimerResource
        
    @property
    def isPeriodic(self) -> str:
        return self.__isPeriodic

    @isPeriodic.setter
    def isPeriodic(self, isPeriodic: str):
        self.__isPeriodic = isPeriodic

    @property
    def MARTE_GRM_TimerResource(self):
        return self.__MARTE_GRM_TimerResource

    @MARTE_GRM_TimerResource.setter
    def MARTE_GRM_TimerResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_TimerResource__MARTE_GRM_TimerResource", None)
        self.__MARTE_GRM_TimerResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Duration154"):
                opp_val = getattr(old_value, "NFP_Duration154", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Duration154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Duration154"):
                opp_val = getattr(value, "NFP_Duration154", None)
                setattr(value, "NFP_Duration154", self)

class MARTE_GRM_ClockResource(TimingResource):

    pass
class SchedParameters:

    pass
class GRM_MARTE_Connector:

    pass
class Scheduler:

    pass
class MARTE_GRM_SecondaryScheduler(Scheduler):

    pass
class GRM_SecondaryScheduler:

    pass
class GRM_ComputingResource:

    pass
class MARTE_HwComputing_HwComputingResource(HwGeneral_HwResource, GRM_ComputingResource):

    pass
class ProcessingResource:

    pass
class MARTE_GRM_DeviceResource(ProcessingResource):

    pass
class MARTE_GRM_CommunicationMedia(ProcessingResource):

    def __init__(self, transmMode: str, MARTE_GRM_CommunicationMedia: "NFP_Integer" = None, MARTE_GRM_CommunicationMedia145: "GRM_MARTE_Connector" = None, MARTE_GRM_CommunicationMedia147: set["NFP_Duration"] = None, MARTE_GRM_CommunicationMedia149: set["NFP_Duration"] = None, MARTE_GRM_CommunicationMedia152: set["NFP_DataTxRate"] = None):
        self.transmMode = transmMode
        self.MARTE_GRM_CommunicationMedia = MARTE_GRM_CommunicationMedia
        self.MARTE_GRM_CommunicationMedia145 = MARTE_GRM_CommunicationMedia145
        self.MARTE_GRM_CommunicationMedia147 = MARTE_GRM_CommunicationMedia147 if MARTE_GRM_CommunicationMedia147 is not None else set()
        self.MARTE_GRM_CommunicationMedia149 = MARTE_GRM_CommunicationMedia149 if MARTE_GRM_CommunicationMedia149 is not None else set()
        self.MARTE_GRM_CommunicationMedia152 = MARTE_GRM_CommunicationMedia152 if MARTE_GRM_CommunicationMedia152 is not None else set()
        
    @property
    def transmMode(self) -> str:
        return self.__transmMode

    @transmMode.setter
    def transmMode(self, transmMode: str):
        self.__transmMode = transmMode

    @property
    def MARTE_GRM_CommunicationMedia145(self):
        return self.__MARTE_GRM_CommunicationMedia145

    @MARTE_GRM_CommunicationMedia145.setter
    def MARTE_GRM_CommunicationMedia145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_CommunicationMedia__MARTE_GRM_CommunicationMedia145", None)
        self.__MARTE_GRM_CommunicationMedia145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_MARTE_Connector"):
                opp_val = getattr(old_value, "GRM_MARTE_Connector", None)
                if opp_val == self:
                    setattr(old_value, "GRM_MARTE_Connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_MARTE_Connector"):
                opp_val = getattr(value, "GRM_MARTE_Connector", None)
                setattr(value, "GRM_MARTE_Connector", self)

    @property
    def MARTE_GRM_CommunicationMedia(self):
        return self.__MARTE_GRM_CommunicationMedia

    @MARTE_GRM_CommunicationMedia.setter
    def MARTE_GRM_CommunicationMedia(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_CommunicationMedia__MARTE_GRM_CommunicationMedia", None)
        self.__MARTE_GRM_CommunicationMedia = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Integer143"):
                opp_val = getattr(old_value, "NFP_Integer143", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Integer143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Integer143"):
                opp_val = getattr(value, "NFP_Integer143", None)
                setattr(value, "NFP_Integer143", self)

    @property
    def MARTE_GRM_CommunicationMedia149(self):
        return self.__MARTE_GRM_CommunicationMedia149

    @MARTE_GRM_CommunicationMedia149.setter
    def MARTE_GRM_CommunicationMedia149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_CommunicationMedia__MARTE_GRM_CommunicationMedia149", None)
        self.__MARTE_GRM_CommunicationMedia149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_Duration150"):
                    opp_val = getattr(item, "NFP_Duration150", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_Duration150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_Duration150"):
                    opp_val = getattr(item, "NFP_Duration150", None)
                    
                    setattr(item, "NFP_Duration150", self)
                    

    @property
    def MARTE_GRM_CommunicationMedia147(self):
        return self.__MARTE_GRM_CommunicationMedia147

    @MARTE_GRM_CommunicationMedia147.setter
    def MARTE_GRM_CommunicationMedia147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_CommunicationMedia__MARTE_GRM_CommunicationMedia147", None)
        self.__MARTE_GRM_CommunicationMedia147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_Duration"):
                    opp_val = getattr(item, "NFP_Duration", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_Duration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_Duration"):
                    opp_val = getattr(item, "NFP_Duration", None)
                    
                    setattr(item, "NFP_Duration", self)
                    

    @property
    def MARTE_GRM_CommunicationMedia152(self):
        return self.__MARTE_GRM_CommunicationMedia152

    @MARTE_GRM_CommunicationMedia152.setter
    def MARTE_GRM_CommunicationMedia152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_CommunicationMedia__MARTE_GRM_CommunicationMedia152", None)
        self.__MARTE_GRM_CommunicationMedia152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_DataTxRate"):
                    opp_val = getattr(item, "NFP_DataTxRate", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_DataTxRate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_DataTxRate"):
                    opp_val = getattr(item, "NFP_DataTxRate", None)
                    
                    setattr(item, "NFP_DataTxRate", self)
                    

class MARTE_GRM_ComputingResource(ProcessingResource):

    pass
class GRM_Scheduler:

    pass
class MARTE_GQAM_GaCommHost(GRM_Scheduler, GRM_CommunicationMedia):

    pass
class MARTE_GQAM_GaExecHost(GRM_Scheduler, GRM_ComputingResource):

    pass
class NFP_Real:

    pass
class GRM_SchedulableResource:

    pass
class MARTE_SW_Concurrency_SwSchedulableResource(GRM_SchedulableResource, SW_Concurrency_SwConcurrentResource):

    def __init__(self, isStaticSchedulingFeature: str, isPreemptable: str, MARTE_SW_Concurrency_SwSchedulableResource: "SW_Concurrency_MARTE_NamedElement" = None, MARTE_SW_Concurrency_SwSchedulableResource700: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwSchedulableResource703: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwSchedulableResource706: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwSchedulableResource709: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwSchedulableResource712: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwSchedulableResource715: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_Foundations123: "MARTE_GRM_Scheduler", GRM_SchedulableResource: "MARTE_GQAM_GaStep", MARTE_Foundations141: "MARTE_GRM_SecondaryScheduler", GRM_SchedulableResource1121: "MARTE_PAM_PaRunTInstance"):
        self.isStaticSchedulingFeature = isStaticSchedulingFeature
        self.isPreemptable = isPreemptable
        self.MARTE_SW_Concurrency_SwSchedulableResource = MARTE_SW_Concurrency_SwSchedulableResource
        self.MARTE_SW_Concurrency_SwSchedulableResource700 = MARTE_SW_Concurrency_SwSchedulableResource700 if MARTE_SW_Concurrency_SwSchedulableResource700 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource703 = MARTE_SW_Concurrency_SwSchedulableResource703 if MARTE_SW_Concurrency_SwSchedulableResource703 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource706 = MARTE_SW_Concurrency_SwSchedulableResource706 if MARTE_SW_Concurrency_SwSchedulableResource706 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource709 = MARTE_SW_Concurrency_SwSchedulableResource709 if MARTE_SW_Concurrency_SwSchedulableResource709 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource712 = MARTE_SW_Concurrency_SwSchedulableResource712 if MARTE_SW_Concurrency_SwSchedulableResource712 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource715 = MARTE_SW_Concurrency_SwSchedulableResource715 if MARTE_SW_Concurrency_SwSchedulableResource715 is not None else set()
        
    @property
    def isStaticSchedulingFeature(self) -> str:
        return self.__isStaticSchedulingFeature

    @isStaticSchedulingFeature.setter
    def isStaticSchedulingFeature(self, isStaticSchedulingFeature: str):
        self.__isStaticSchedulingFeature = isStaticSchedulingFeature

    @property
    def isPreemptable(self) -> str:
        return self.__isPreemptable

    @isPreemptable.setter
    def isPreemptable(self, isPreemptable: str):
        self.__isPreemptable = isPreemptable

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource700(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource700

    @MARTE_SW_Concurrency_SwSchedulableResource700.setter
    def MARTE_SW_Concurrency_SwSchedulableResource700(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource700", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource700 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement701"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement701", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement701", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement701"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement701", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement701", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource

    @MARTE_SW_Concurrency_SwSchedulableResource.setter
    def MARTE_SW_Concurrency_SwSchedulableResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SW_Concurrency_MARTE_NamedElement"):
                opp_val = getattr(old_value, "SW_Concurrency_MARTE_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "SW_Concurrency_MARTE_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SW_Concurrency_MARTE_NamedElement"):
                opp_val = getattr(value, "SW_Concurrency_MARTE_NamedElement", None)
                setattr(value, "SW_Concurrency_MARTE_NamedElement", self)

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource715(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource715

    @MARTE_SW_Concurrency_SwSchedulableResource715.setter
    def MARTE_SW_Concurrency_SwSchedulableResource715(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource715", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource715 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature716"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature716", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature716", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature716"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature716", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature716", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource709(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource709

    @MARTE_SW_Concurrency_SwSchedulableResource709.setter
    def MARTE_SW_Concurrency_SwSchedulableResource709(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource709", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource709 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature710"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature710", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature710", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature710"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature710", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature710", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource706(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource706

    @MARTE_SW_Concurrency_SwSchedulableResource706.setter
    def MARTE_SW_Concurrency_SwSchedulableResource706(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource706", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource706 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement707"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement707", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement707", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement707"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement707", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement707", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource712(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource712

    @MARTE_SW_Concurrency_SwSchedulableResource712.setter
    def MARTE_SW_Concurrency_SwSchedulableResource712(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource712", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource712 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature713"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature713", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature713", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature713"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature713", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature713", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource703(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource703

    @MARTE_SW_Concurrency_SwSchedulableResource703.setter
    def MARTE_SW_Concurrency_SwSchedulableResource703(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource703", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource703 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement704"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement704", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement704", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement704"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement704", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement704", self)
                    

class GRM_MutualExclusionResource:

    pass
class MARTE_SW_Interaction_SwMutualExclusionResource(SW_Interaction_SwSynchronizationResource, GRM_MutualExclusionResource):

    def __init__(self, mechanism: str, concurrentAccessProtocol: str, MARTE_SW_Interaction_SwMutualExclusionResource: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_SwMutualExclusionResource809: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_SwMutualExclusionResource812: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_Foundations: "MARTE_GRM_Scheduler"):
        self.mechanism = mechanism
        self.concurrentAccessProtocol = concurrentAccessProtocol
        self.MARTE_SW_Interaction_SwMutualExclusionResource = MARTE_SW_Interaction_SwMutualExclusionResource if MARTE_SW_Interaction_SwMutualExclusionResource is not None else set()
        self.MARTE_SW_Interaction_SwMutualExclusionResource809 = MARTE_SW_Interaction_SwMutualExclusionResource809 if MARTE_SW_Interaction_SwMutualExclusionResource809 is not None else set()
        self.MARTE_SW_Interaction_SwMutualExclusionResource812 = MARTE_SW_Interaction_SwMutualExclusionResource812 if MARTE_SW_Interaction_SwMutualExclusionResource812 is not None else set()
        
    @property
    def mechanism(self) -> str:
        return self.__mechanism

    @mechanism.setter
    def mechanism(self, mechanism: str):
        self.__mechanism = mechanism

    @property
    def concurrentAccessProtocol(self) -> str:
        return self.__concurrentAccessProtocol

    @concurrentAccessProtocol.setter
    def concurrentAccessProtocol(self, concurrentAccessProtocol: str):
        self.__concurrentAccessProtocol = concurrentAccessProtocol

    @property
    def MARTE_SW_Interaction_SwMutualExclusionResource809(self):
        return self.__MARTE_SW_Interaction_SwMutualExclusionResource809

    @MARTE_SW_Interaction_SwMutualExclusionResource809.setter
    def MARTE_SW_Interaction_SwMutualExclusionResource809(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_SwMutualExclusionResource__MARTE_SW_Interaction_SwMutualExclusionResource809", None)
        self.__MARTE_SW_Interaction_SwMutualExclusionResource809 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature810"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature810", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature810", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature810"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature810", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature810", self)
                    

    @property
    def MARTE_SW_Interaction_SwMutualExclusionResource(self):
        return self.__MARTE_SW_Interaction_SwMutualExclusionResource

    @MARTE_SW_Interaction_SwMutualExclusionResource.setter
    def MARTE_SW_Interaction_SwMutualExclusionResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_SwMutualExclusionResource__MARTE_SW_Interaction_SwMutualExclusionResource", None)
        self.__MARTE_SW_Interaction_SwMutualExclusionResource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement807"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement807", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement807", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement807"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement807", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement807", self)
                    

    @property
    def MARTE_SW_Interaction_SwMutualExclusionResource812(self):
        return self.__MARTE_SW_Interaction_SwMutualExclusionResource812

    @MARTE_SW_Interaction_SwMutualExclusionResource812.setter
    def MARTE_SW_Interaction_SwMutualExclusionResource812(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_SwMutualExclusionResource__MARTE_SW_Interaction_SwMutualExclusionResource812", None)
        self.__MARTE_SW_Interaction_SwMutualExclusionResource812 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature813"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature813", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature813", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature813"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature813", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature813", self)
                    

class Resource:

    pass
class MARTE_PAM_PaLogicalResource(Resource):

    pass
class MARTE_SW_ResourceCore_SwResource(Resource):

    pass
class MARTE_GRM_SchedulableResource(Resource):

    pass
class MARTE_GRM_TimingResource(Resource):

    pass
class MARTE_GRM_MutualExclusionResource(Resource):

    def __init__(self, protectKind: str, otherProtectProtocol: str, MARTE_GRM_MutualExclusionResource: "NFP_Integer" = None, GRM130: "GRM_Scheduler" = None):
        self.protectKind = protectKind
        self.otherProtectProtocol = otherProtectProtocol
        self.MARTE_GRM_MutualExclusionResource = MARTE_GRM_MutualExclusionResource
        self.GRM130 = GRM130
        
    @property
    def otherProtectProtocol(self) -> str:
        return self.__otherProtectProtocol

    @otherProtectProtocol.setter
    def otherProtectProtocol(self, otherProtectProtocol: str):
        self.__otherProtectProtocol = otherProtectProtocol

    @property
    def protectKind(self) -> str:
        return self.__protectKind

    @protectKind.setter
    def protectKind(self, protectKind: str):
        self.__protectKind = protectKind

    @property
    def MARTE_GRM_MutualExclusionResource(self):
        return self.__MARTE_GRM_MutualExclusionResource

    @MARTE_GRM_MutualExclusionResource.setter
    def MARTE_GRM_MutualExclusionResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_MutualExclusionResource__MARTE_GRM_MutualExclusionResource", None)
        self.__MARTE_GRM_MutualExclusionResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Integer128"):
                opp_val = getattr(old_value, "NFP_Integer128", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Integer128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Integer128"):
                opp_val = getattr(value, "NFP_Integer128", None)
                setattr(value, "NFP_Integer128", self)

    @property
    def GRM130(self):
        return self.__GRM130

    @GRM130.setter
    def GRM130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_MutualExclusionResource__GRM130", None)
        self.__GRM130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MARTE_Foundations131"):
                opp_val = getattr(old_value, "MARTE_Foundations131", None)
                if opp_val == self:
                    setattr(old_value, "MARTE_Foundations131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MARTE_Foundations131"):
                opp_val = getattr(value, "MARTE_Foundations131", None)
                setattr(value, "MARTE_Foundations131", self)

class MARTE_HwGeneral_HwResource(Resource):

    def __init__(self, name: str, MARTE_HwGeneral_HwResource521: set["HwGeneral_HwResourceService"] = None, MARTE_HwGeneral_HwResource523: set["HwGeneral_HwResourceService"] = None, MARTE_HwGeneral_HwResource526: set["HwGeneral_HwResource"] = None, MARTE_HwGeneral_HwResource528: set["HwCommunication_HwEndPoint"] = None, MARTE_HwGeneral_HwResource530: "NFP_Frequency" = None, MARTE_HwGeneral_HwResource532: set["HwGeneral_MARTE_Operation"] = None, MARTE_HwGeneral_HwResource: "NFP_String" = None, MARTE_HwGeneral_HwResource534: set["HwGeneral_MARTE_Activity"] = None):
        self.name = name
        self.MARTE_HwGeneral_HwResource521 = MARTE_HwGeneral_HwResource521 if MARTE_HwGeneral_HwResource521 is not None else set()
        self.MARTE_HwGeneral_HwResource523 = MARTE_HwGeneral_HwResource523 if MARTE_HwGeneral_HwResource523 is not None else set()
        self.MARTE_HwGeneral_HwResource526 = MARTE_HwGeneral_HwResource526 if MARTE_HwGeneral_HwResource526 is not None else set()
        self.MARTE_HwGeneral_HwResource528 = MARTE_HwGeneral_HwResource528 if MARTE_HwGeneral_HwResource528 is not None else set()
        self.MARTE_HwGeneral_HwResource530 = MARTE_HwGeneral_HwResource530
        self.MARTE_HwGeneral_HwResource532 = MARTE_HwGeneral_HwResource532 if MARTE_HwGeneral_HwResource532 is not None else set()
        self.MARTE_HwGeneral_HwResource = MARTE_HwGeneral_HwResource
        self.MARTE_HwGeneral_HwResource534 = MARTE_HwGeneral_HwResource534 if MARTE_HwGeneral_HwResource534 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MARTE_HwGeneral_HwResource528(self):
        return self.__MARTE_HwGeneral_HwResource528

    @MARTE_HwGeneral_HwResource528.setter
    def MARTE_HwGeneral_HwResource528(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource528", None)
        self.__MARTE_HwGeneral_HwResource528 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwCommunication_HwEndPoint"):
                    opp_val = getattr(item, "HwCommunication_HwEndPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "HwCommunication_HwEndPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwCommunication_HwEndPoint"):
                    opp_val = getattr(item, "HwCommunication_HwEndPoint", None)
                    
                    setattr(item, "HwCommunication_HwEndPoint", self)
                    

    @property
    def MARTE_HwGeneral_HwResource526(self):
        return self.__MARTE_HwGeneral_HwResource526

    @MARTE_HwGeneral_HwResource526.setter
    def MARTE_HwGeneral_HwResource526(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource526", None)
        self.__MARTE_HwGeneral_HwResource526 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResource"):
                    opp_val = getattr(item, "HwGeneral_HwResource", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResource"):
                    opp_val = getattr(item, "HwGeneral_HwResource", None)
                    
                    setattr(item, "HwGeneral_HwResource", self)
                    

    @property
    def MARTE_HwGeneral_HwResource523(self):
        return self.__MARTE_HwGeneral_HwResource523

    @MARTE_HwGeneral_HwResource523.setter
    def MARTE_HwGeneral_HwResource523(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource523", None)
        self.__MARTE_HwGeneral_HwResource523 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResourceService524"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService524", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResourceService524", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResourceService524"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService524", None)
                    
                    setattr(item, "HwGeneral_HwResourceService524", self)
                    

    @property
    def MARTE_HwGeneral_HwResource532(self):
        return self.__MARTE_HwGeneral_HwResource532

    @MARTE_HwGeneral_HwResource532.setter
    def MARTE_HwGeneral_HwResource532(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource532", None)
        self.__MARTE_HwGeneral_HwResource532 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_MARTE_Operation"):
                    opp_val = getattr(item, "HwGeneral_MARTE_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_MARTE_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_MARTE_Operation"):
                    opp_val = getattr(item, "HwGeneral_MARTE_Operation", None)
                    
                    setattr(item, "HwGeneral_MARTE_Operation", self)
                    

    @property
    def MARTE_HwGeneral_HwResource521(self):
        return self.__MARTE_HwGeneral_HwResource521

    @MARTE_HwGeneral_HwResource521.setter
    def MARTE_HwGeneral_HwResource521(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource521", None)
        self.__MARTE_HwGeneral_HwResource521 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResourceService"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResourceService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResourceService"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService", None)
                    
                    setattr(item, "HwGeneral_HwResourceService", self)
                    

    @property
    def MARTE_HwGeneral_HwResource(self):
        return self.__MARTE_HwGeneral_HwResource

    @MARTE_HwGeneral_HwResource.setter
    def MARTE_HwGeneral_HwResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource", None)
        self.__MARTE_HwGeneral_HwResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_String519"):
                opp_val = getattr(old_value, "NFP_String519", None)
                if opp_val == self:
                    setattr(old_value, "NFP_String519", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_String519"):
                opp_val = getattr(value, "NFP_String519", None)
                setattr(value, "NFP_String519", self)

    @property
    def MARTE_HwGeneral_HwResource534(self):
        return self.__MARTE_HwGeneral_HwResource534

    @MARTE_HwGeneral_HwResource534.setter
    def MARTE_HwGeneral_HwResource534(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource534", None)
        self.__MARTE_HwGeneral_HwResource534 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_MARTE_Activity"):
                    opp_val = getattr(item, "HwGeneral_MARTE_Activity", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_MARTE_Activity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_MARTE_Activity"):
                    opp_val = getattr(item, "HwGeneral_MARTE_Activity", None)
                    
                    setattr(item, "HwGeneral_MARTE_Activity", self)
                    

    @property
    def MARTE_HwGeneral_HwResource530(self):
        return self.__MARTE_HwGeneral_HwResource530

    @MARTE_HwGeneral_HwResource530.setter
    def MARTE_HwGeneral_HwResource530(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource530", None)
        self.__MARTE_HwGeneral_HwResource530 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Frequency"):
                opp_val = getattr(old_value, "NFP_Frequency", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Frequency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Frequency"):
                opp_val = getattr(value, "NFP_Frequency", None)
                setattr(value, "NFP_Frequency", self)

class MARTE_GRM_ProcessingResource(Resource):

    pass
class MARTE_GRM_StorageResource(Resource):

    pass
class GRM_MARTE_ConnectableElement:

    pass
class GRM_ProcessingResource:

    pass
class GRM_MARTE_OpaqueExpression:

    pass
class MARTE_GRM_Scheduler(Resource):

    def __init__(self, isPreemptible: str, schedPolicy: str, otherSchedPolicy: str, MARTE_GRM_Scheduler: "GRM_MARTE_OpaqueExpression" = None, GRM: set["GRM_MutualExclusionResource"] = None, GRM122: set["GRM_SchedulableResource"] = None, MARTE_GRM_Scheduler117: set["GRM_ProcessingResource"] = None, MARTE_GRM_Scheduler119: "GRM_ComputingResource" = None):
        self.isPreemptible = isPreemptible
        self.schedPolicy = schedPolicy
        self.otherSchedPolicy = otherSchedPolicy
        self.MARTE_GRM_Scheduler = MARTE_GRM_Scheduler
        self.GRM = GRM if GRM is not None else set()
        self.GRM122 = GRM122 if GRM122 is not None else set()
        self.MARTE_GRM_Scheduler117 = MARTE_GRM_Scheduler117 if MARTE_GRM_Scheduler117 is not None else set()
        self.MARTE_GRM_Scheduler119 = MARTE_GRM_Scheduler119
        
    @property
    def schedPolicy(self) -> str:
        return self.__schedPolicy

    @schedPolicy.setter
    def schedPolicy(self, schedPolicy: str):
        self.__schedPolicy = schedPolicy

    @property
    def otherSchedPolicy(self) -> str:
        return self.__otherSchedPolicy

    @otherSchedPolicy.setter
    def otherSchedPolicy(self, otherSchedPolicy: str):
        self.__otherSchedPolicy = otherSchedPolicy

    @property
    def isPreemptible(self) -> str:
        return self.__isPreemptible

    @isPreemptible.setter
    def isPreemptible(self, isPreemptible: str):
        self.__isPreemptible = isPreemptible

    @property
    def MARTE_GRM_Scheduler(self):
        return self.__MARTE_GRM_Scheduler

    @MARTE_GRM_Scheduler.setter
    def MARTE_GRM_Scheduler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Scheduler__MARTE_GRM_Scheduler", None)
        self.__MARTE_GRM_Scheduler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_MARTE_OpaqueExpression"):
                opp_val = getattr(old_value, "GRM_MARTE_OpaqueExpression", None)
                if opp_val == self:
                    setattr(old_value, "GRM_MARTE_OpaqueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_MARTE_OpaqueExpression"):
                opp_val = getattr(value, "GRM_MARTE_OpaqueExpression", None)
                setattr(value, "GRM_MARTE_OpaqueExpression", self)

    @property
    def GRM122(self):
        return self.__GRM122

    @GRM122.setter
    def GRM122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Scheduler__GRM122", None)
        self.__GRM122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MARTE_Foundations123"):
                    opp_val = getattr(item, "MARTE_Foundations123", None)
                    
                    if opp_val == self:
                        setattr(item, "MARTE_Foundations123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MARTE_Foundations123"):
                    opp_val = getattr(item, "MARTE_Foundations123", None)
                    
                    setattr(item, "MARTE_Foundations123", self)
                    

    @property
    def MARTE_GRM_Scheduler117(self):
        return self.__MARTE_GRM_Scheduler117

    @MARTE_GRM_Scheduler117.setter
    def MARTE_GRM_Scheduler117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Scheduler__MARTE_GRM_Scheduler117", None)
        self.__MARTE_GRM_Scheduler117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GRM_ProcessingResource"):
                    opp_val = getattr(item, "GRM_ProcessingResource", None)
                    
                    if opp_val == self:
                        setattr(item, "GRM_ProcessingResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GRM_ProcessingResource"):
                    opp_val = getattr(item, "GRM_ProcessingResource", None)
                    
                    setattr(item, "GRM_ProcessingResource", self)
                    

    @property
    def MARTE_GRM_Scheduler119(self):
        return self.__MARTE_GRM_Scheduler119

    @MARTE_GRM_Scheduler119.setter
    def MARTE_GRM_Scheduler119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Scheduler__MARTE_GRM_Scheduler119", None)
        self.__MARTE_GRM_Scheduler119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_ComputingResource"):
                opp_val = getattr(old_value, "GRM_ComputingResource", None)
                if opp_val == self:
                    setattr(old_value, "GRM_ComputingResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_ComputingResource"):
                opp_val = getattr(value, "GRM_ComputingResource", None)
                setattr(value, "GRM_ComputingResource", self)

    @property
    def GRM(self):
        return self.__GRM

    @GRM.setter
    def GRM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Scheduler__GRM", None)
        self.__GRM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MARTE_Foundations"):
                    opp_val = getattr(item, "MARTE_Foundations", None)
                    
                    if opp_val == self:
                        setattr(item, "MARTE_Foundations", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MARTE_Foundations"):
                    opp_val = getattr(item, "MARTE_Foundations", None)
                    
                    setattr(item, "MARTE_Foundations", self)
                    

class MARTE_GRM_ConcurrencyResource(Resource):

    pass
class MARTE_GRM_SynchronizationResource(Resource):

    pass
class MARTE_GRM_CommunicationEndPoint(Resource):

    pass
class Time_MARTE_Message:

    pass
class GRM_MARTE_Lifeline:

    pass
class GRM_MARTE_Classifier:

    pass
class GRM_MARTE_InstanceSpecification:

    pass
class GRM_MARTE_Property:

    pass
class NFP_Integer:

    pass
class MARTE_GRM_Resource:

    def __init__(self, isProtected: str, MARTE_GRM_Resource: "NFP_Integer" = None, MARTE_GRM_Resource102: "GRM_MARTE_Property" = None, MARTE_GRM_Resource104: "GRM_MARTE_InstanceSpecification" = None, MARTE_GRM_Resource106: "GRM_MARTE_Classifier" = None, MARTE_GRM_Resource108: "GRM_MARTE_Lifeline" = None, MARTE_GRM_Resource110: "GRM_MARTE_ConnectableElement" = None):
        self.isProtected = isProtected
        self.MARTE_GRM_Resource = MARTE_GRM_Resource
        self.MARTE_GRM_Resource102 = MARTE_GRM_Resource102
        self.MARTE_GRM_Resource104 = MARTE_GRM_Resource104
        self.MARTE_GRM_Resource106 = MARTE_GRM_Resource106
        self.MARTE_GRM_Resource108 = MARTE_GRM_Resource108
        self.MARTE_GRM_Resource110 = MARTE_GRM_Resource110
        
    @property
    def isProtected(self) -> str:
        return self.__isProtected

    @isProtected.setter
    def isProtected(self, isProtected: str):
        self.__isProtected = isProtected

    @property
    def MARTE_GRM_Resource108(self):
        return self.__MARTE_GRM_Resource108

    @MARTE_GRM_Resource108.setter
    def MARTE_GRM_Resource108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Resource__MARTE_GRM_Resource108", None)
        self.__MARTE_GRM_Resource108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_MARTE_Lifeline"):
                opp_val = getattr(old_value, "GRM_MARTE_Lifeline", None)
                if opp_val == self:
                    setattr(old_value, "GRM_MARTE_Lifeline", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_MARTE_Lifeline"):
                opp_val = getattr(value, "GRM_MARTE_Lifeline", None)
                setattr(value, "GRM_MARTE_Lifeline", self)

    @property
    def MARTE_GRM_Resource(self):
        return self.__MARTE_GRM_Resource

    @MARTE_GRM_Resource.setter
    def MARTE_GRM_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Resource__MARTE_GRM_Resource", None)
        self.__MARTE_GRM_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Integer"):
                opp_val = getattr(old_value, "NFP_Integer", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Integer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Integer"):
                opp_val = getattr(value, "NFP_Integer", None)
                setattr(value, "NFP_Integer", self)

    @property
    def MARTE_GRM_Resource106(self):
        return self.__MARTE_GRM_Resource106

    @MARTE_GRM_Resource106.setter
    def MARTE_GRM_Resource106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Resource__MARTE_GRM_Resource106", None)
        self.__MARTE_GRM_Resource106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_MARTE_Classifier"):
                opp_val = getattr(old_value, "GRM_MARTE_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "GRM_MARTE_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_MARTE_Classifier"):
                opp_val = getattr(value, "GRM_MARTE_Classifier", None)
                setattr(value, "GRM_MARTE_Classifier", self)

    @property
    def MARTE_GRM_Resource104(self):
        return self.__MARTE_GRM_Resource104

    @MARTE_GRM_Resource104.setter
    def MARTE_GRM_Resource104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Resource__MARTE_GRM_Resource104", None)
        self.__MARTE_GRM_Resource104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_MARTE_InstanceSpecification"):
                opp_val = getattr(old_value, "GRM_MARTE_InstanceSpecification", None)
                if opp_val == self:
                    setattr(old_value, "GRM_MARTE_InstanceSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_MARTE_InstanceSpecification"):
                opp_val = getattr(value, "GRM_MARTE_InstanceSpecification", None)
                setattr(value, "GRM_MARTE_InstanceSpecification", self)

    @property
    def MARTE_GRM_Resource110(self):
        return self.__MARTE_GRM_Resource110

    @MARTE_GRM_Resource110.setter
    def MARTE_GRM_Resource110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Resource__MARTE_GRM_Resource110", None)
        self.__MARTE_GRM_Resource110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_MARTE_ConnectableElement"):
                opp_val = getattr(old_value, "GRM_MARTE_ConnectableElement", None)
                if opp_val == self:
                    setattr(old_value, "GRM_MARTE_ConnectableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_MARTE_ConnectableElement"):
                opp_val = getattr(value, "GRM_MARTE_ConnectableElement", None)
                setattr(value, "GRM_MARTE_ConnectableElement", self)

    @property
    def MARTE_GRM_Resource102(self):
        return self.__MARTE_GRM_Resource102

    @MARTE_GRM_Resource102.setter
    def MARTE_GRM_Resource102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Resource__MARTE_GRM_Resource102", None)
        self.__MARTE_GRM_Resource102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_MARTE_Property"):
                opp_val = getattr(old_value, "GRM_MARTE_Property", None)
                if opp_val == self:
                    setattr(old_value, "GRM_MARTE_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_MARTE_Property"):
                opp_val = getattr(value, "GRM_MARTE_Property", None)
                setattr(value, "GRM_MARTE_Property", self)

class Time_MARTE_Event:

    pass
class Time_MARTE_TimeObservation:

    pass
class TimedObservation:

    pass
class MARTE_Time_TimedInstantObservation(TimedObservation):

    def __init__(self, obsKind: str, MARTE_Time_TimedInstantObservation: "Time_MARTE_TimeObservation" = None):
        self.obsKind = obsKind
        self.MARTE_Time_TimedInstantObservation = MARTE_Time_TimedInstantObservation
        
    @property
    def obsKind(self) -> str:
        return self.__obsKind

    @obsKind.setter
    def obsKind(self, obsKind: str):
        self.__obsKind = obsKind

    @property
    def MARTE_Time_TimedInstantObservation(self):
        return self.__MARTE_Time_TimedInstantObservation

    @MARTE_Time_TimedInstantObservation.setter
    def MARTE_Time_TimedInstantObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_TimedInstantObservation__MARTE_Time_TimedInstantObservation", None)
        self.__MARTE_Time_TimedInstantObservation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_TimeObservation"):
                opp_val = getattr(old_value, "Time_MARTE_TimeObservation", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_TimeObservation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_TimeObservation"):
                opp_val = getattr(value, "Time_MARTE_TimeObservation", None)
                setattr(value, "Time_MARTE_TimeObservation", self)

class Time_MARTE_Behavior:

    pass
class Time_MARTE_Action:

    pass
class Time_MARTE_TimeEvent:

    pass
class Time_MARTE_DurationObservation:

    pass
class MARTE_Time_TimedDurationObservation(TimedObservation):

    def __init__(self, obsKind: str, MARTE_Time_TimedDurationObservation: "Time_MARTE_DurationObservation" = None):
        self.obsKind = obsKind
        self.MARTE_Time_TimedDurationObservation = MARTE_Time_TimedDurationObservation
        
    @property
    def obsKind(self) -> str:
        return self.__obsKind

    @obsKind.setter
    def obsKind(self, obsKind: str):
        self.__obsKind = obsKind

    @property
    def MARTE_Time_TimedDurationObservation(self):
        return self.__MARTE_Time_TimedDurationObservation

    @MARTE_Time_TimedDurationObservation.setter
    def MARTE_Time_TimedDurationObservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_TimedDurationObservation__MARTE_Time_TimedDurationObservation", None)
        self.__MARTE_Time_TimedDurationObservation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_DurationObservation"):
                opp_val = getattr(old_value, "Time_MARTE_DurationObservation", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_DurationObservation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_DurationObservation"):
                opp_val = getattr(value, "Time_MARTE_DurationObservation", None)
                setattr(value, "Time_MARTE_DurationObservation", self)

class MARTE_Time_TimedElement(ABC):

    pass
class Time_MARTE_Class:

    pass
class Time_TimedElement:

    pass
class Time_MARTE_ValueSpecification:

    pass
class TimedElement:

    pass
class MARTE_Time_TimedEvent(TimedElement):

    def __init__(self, repetition: str, MARTE_Time_TimedEvent: "Time_MARTE_TimeEvent" = None, MARTE_Time_TimedEvent85: "Time_MARTE_ValueSpecification" = None):
        self.repetition = repetition
        self.MARTE_Time_TimedEvent = MARTE_Time_TimedEvent
        self.MARTE_Time_TimedEvent85 = MARTE_Time_TimedEvent85
        
    @property
    def repetition(self) -> str:
        return self.__repetition

    @repetition.setter
    def repetition(self, repetition: str):
        self.__repetition = repetition

    @property
    def MARTE_Time_TimedEvent85(self):
        return self.__MARTE_Time_TimedEvent85

    @MARTE_Time_TimedEvent85.setter
    def MARTE_Time_TimedEvent85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_TimedEvent__MARTE_Time_TimedEvent85", None)
        self.__MARTE_Time_TimedEvent85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_ValueSpecification86"):
                opp_val = getattr(old_value, "Time_MARTE_ValueSpecification86", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_ValueSpecification86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_ValueSpecification86"):
                opp_val = getattr(value, "Time_MARTE_ValueSpecification86", None)
                setattr(value, "Time_MARTE_ValueSpecification86", self)

    @property
    def MARTE_Time_TimedEvent(self):
        return self.__MARTE_Time_TimedEvent

    @MARTE_Time_TimedEvent.setter
    def MARTE_Time_TimedEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_TimedEvent__MARTE_Time_TimedEvent", None)
        self.__MARTE_Time_TimedEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_TimeEvent"):
                opp_val = getattr(old_value, "Time_MARTE_TimeEvent", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_TimeEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_TimeEvent"):
                opp_val = getattr(value, "Time_MARTE_TimeEvent", None)
                setattr(value, "Time_MARTE_TimeEvent", self)

class MARTE_Time_TimedProcessing(TimedElement):

    pass
class MARTE_Time_TimedObservation(TimedElement):

    pass
class MARTE_Time_TimedValueSpecification(TimedElement):

    def __init__(self, interpretation: str, MARTE_Time_TimedValueSpecification: "Time_MARTE_ValueSpecification" = None):
        self.interpretation = interpretation
        self.MARTE_Time_TimedValueSpecification = MARTE_Time_TimedValueSpecification
        
    @property
    def interpretation(self) -> str:
        return self.__interpretation

    @interpretation.setter
    def interpretation(self, interpretation: str):
        self.__interpretation = interpretation

    @property
    def MARTE_Time_TimedValueSpecification(self):
        return self.__MARTE_Time_TimedValueSpecification

    @MARTE_Time_TimedValueSpecification.setter
    def MARTE_Time_TimedValueSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_TimedValueSpecification__MARTE_Time_TimedValueSpecification", None)
        self.__MARTE_Time_TimedValueSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_ValueSpecification"):
                opp_val = getattr(old_value, "Time_MARTE_ValueSpecification", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_ValueSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_ValueSpecification"):
                opp_val = getattr(value, "Time_MARTE_ValueSpecification", None)
                setattr(value, "Time_MARTE_ValueSpecification", self)

class Time_Clock:

    pass
class Time_MARTE_Property:

    pass
class Time_ClockType:

    pass
class Time_MARTE_Operation:

    pass
class Time_MARTE_Enumeration:

    pass
class MARTE_Time_ClockType:

    def __init__(self, nature: str, isLogical: str, MARTE_Time_ClockType: "Time_MARTE_Enumeration" = None, MARTE_Time_ClockType61: "Time_MARTE_Property" = None, MARTE_Time_ClockType64: "Time_MARTE_Property" = None, MARTE_Time_ClockType67: "Time_MARTE_Property" = None, MARTE_Time_ClockType70: "Time_MARTE_Operation" = None, MARTE_Time_ClockType72: "Time_MARTE_Operation" = None, MARTE_Time_ClockType75: "Time_MARTE_Operation" = None, MARTE_Time_ClockType78: "Time_MARTE_Class" = None):
        self.nature = nature
        self.isLogical = isLogical
        self.MARTE_Time_ClockType = MARTE_Time_ClockType
        self.MARTE_Time_ClockType61 = MARTE_Time_ClockType61
        self.MARTE_Time_ClockType64 = MARTE_Time_ClockType64
        self.MARTE_Time_ClockType67 = MARTE_Time_ClockType67
        self.MARTE_Time_ClockType70 = MARTE_Time_ClockType70
        self.MARTE_Time_ClockType72 = MARTE_Time_ClockType72
        self.MARTE_Time_ClockType75 = MARTE_Time_ClockType75
        self.MARTE_Time_ClockType78 = MARTE_Time_ClockType78
        
    @property
    def isLogical(self) -> str:
        return self.__isLogical

    @isLogical.setter
    def isLogical(self, isLogical: str):
        self.__isLogical = isLogical

    @property
    def nature(self) -> str:
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature

    @property
    def MARTE_Time_ClockType72(self):
        return self.__MARTE_Time_ClockType72

    @MARTE_Time_ClockType72.setter
    def MARTE_Time_ClockType72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType72", None)
        self.__MARTE_Time_ClockType72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Operation73"):
                opp_val = getattr(old_value, "Time_MARTE_Operation73", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Operation73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Operation73"):
                opp_val = getattr(value, "Time_MARTE_Operation73", None)
                setattr(value, "Time_MARTE_Operation73", self)

    @property
    def MARTE_Time_ClockType61(self):
        return self.__MARTE_Time_ClockType61

    @MARTE_Time_ClockType61.setter
    def MARTE_Time_ClockType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType61", None)
        self.__MARTE_Time_ClockType61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Property62"):
                opp_val = getattr(old_value, "Time_MARTE_Property62", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Property62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Property62"):
                opp_val = getattr(value, "Time_MARTE_Property62", None)
                setattr(value, "Time_MARTE_Property62", self)

    @property
    def MARTE_Time_ClockType(self):
        return self.__MARTE_Time_ClockType

    @MARTE_Time_ClockType.setter
    def MARTE_Time_ClockType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType", None)
        self.__MARTE_Time_ClockType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Enumeration"):
                opp_val = getattr(old_value, "Time_MARTE_Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Enumeration"):
                opp_val = getattr(value, "Time_MARTE_Enumeration", None)
                setattr(value, "Time_MARTE_Enumeration", self)

    @property
    def MARTE_Time_ClockType75(self):
        return self.__MARTE_Time_ClockType75

    @MARTE_Time_ClockType75.setter
    def MARTE_Time_ClockType75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType75", None)
        self.__MARTE_Time_ClockType75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Operation76"):
                opp_val = getattr(old_value, "Time_MARTE_Operation76", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Operation76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Operation76"):
                opp_val = getattr(value, "Time_MARTE_Operation76", None)
                setattr(value, "Time_MARTE_Operation76", self)

    @property
    def MARTE_Time_ClockType67(self):
        return self.__MARTE_Time_ClockType67

    @MARTE_Time_ClockType67.setter
    def MARTE_Time_ClockType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType67", None)
        self.__MARTE_Time_ClockType67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Property68"):
                opp_val = getattr(old_value, "Time_MARTE_Property68", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Property68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Property68"):
                opp_val = getattr(value, "Time_MARTE_Property68", None)
                setattr(value, "Time_MARTE_Property68", self)

    @property
    def MARTE_Time_ClockType78(self):
        return self.__MARTE_Time_ClockType78

    @MARTE_Time_ClockType78.setter
    def MARTE_Time_ClockType78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType78", None)
        self.__MARTE_Time_ClockType78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Class"):
                opp_val = getattr(old_value, "Time_MARTE_Class", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Class"):
                opp_val = getattr(value, "Time_MARTE_Class", None)
                setattr(value, "Time_MARTE_Class", self)

    @property
    def MARTE_Time_ClockType64(self):
        return self.__MARTE_Time_ClockType64

    @MARTE_Time_ClockType64.setter
    def MARTE_Time_ClockType64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType64", None)
        self.__MARTE_Time_ClockType64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Property65"):
                opp_val = getattr(old_value, "Time_MARTE_Property65", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Property65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Property65"):
                opp_val = getattr(value, "Time_MARTE_Property65", None)
                setattr(value, "Time_MARTE_Property65", self)

    @property
    def MARTE_Time_ClockType70(self):
        return self.__MARTE_Time_ClockType70

    @MARTE_Time_ClockType70.setter
    def MARTE_Time_ClockType70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType70", None)
        self.__MARTE_Time_ClockType70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Operation"):
                opp_val = getattr(old_value, "Time_MARTE_Operation", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Operation"):
                opp_val = getattr(value, "Time_MARTE_Operation", None)
                setattr(value, "Time_MARTE_Operation", self)

class Alloc_MARTE_Comment:

    pass
class Time_MARTE_InstanceSpecification:

    pass
class MARTE_Time_Clock:

    def __init__(self, standard: str, MARTE_Time_Clock: "Time_MARTE_InstanceSpecification" = None, MARTE_Time_Clock58: "Time_MARTE_Property" = None, MARTE_Time_Clock53: "Time_ClockType" = None, MARTE_Time_Clock55: "NFPs_Unit" = None):
        self.standard = standard
        self.MARTE_Time_Clock = MARTE_Time_Clock
        self.MARTE_Time_Clock58 = MARTE_Time_Clock58
        self.MARTE_Time_Clock53 = MARTE_Time_Clock53
        self.MARTE_Time_Clock55 = MARTE_Time_Clock55
        
    @property
    def standard(self) -> str:
        return self.__standard

    @standard.setter
    def standard(self, standard: str):
        self.__standard = standard

    @property
    def MARTE_Time_Clock53(self):
        return self.__MARTE_Time_Clock53

    @MARTE_Time_Clock53.setter
    def MARTE_Time_Clock53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_Clock__MARTE_Time_Clock53", None)
        self.__MARTE_Time_Clock53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_ClockType"):
                opp_val = getattr(old_value, "Time_ClockType", None)
                if opp_val == self:
                    setattr(old_value, "Time_ClockType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_ClockType"):
                opp_val = getattr(value, "Time_ClockType", None)
                setattr(value, "Time_ClockType", self)

    @property
    def MARTE_Time_Clock58(self):
        return self.__MARTE_Time_Clock58

    @MARTE_Time_Clock58.setter
    def MARTE_Time_Clock58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_Clock__MARTE_Time_Clock58", None)
        self.__MARTE_Time_Clock58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Property"):
                opp_val = getattr(old_value, "Time_MARTE_Property", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Property"):
                opp_val = getattr(value, "Time_MARTE_Property", None)
                setattr(value, "Time_MARTE_Property", self)

    @property
    def MARTE_Time_Clock55(self):
        return self.__MARTE_Time_Clock55

    @MARTE_Time_Clock55.setter
    def MARTE_Time_Clock55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_Clock__MARTE_Time_Clock55", None)
        self.__MARTE_Time_Clock55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFPs_Unit56"):
                opp_val = getattr(old_value, "NFPs_Unit56", None)
                if opp_val == self:
                    setattr(old_value, "NFPs_Unit56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFPs_Unit56"):
                opp_val = getattr(value, "NFPs_Unit56", None)
                setattr(value, "NFPs_Unit56", self)

    @property
    def MARTE_Time_Clock(self):
        return self.__MARTE_Time_Clock

    @MARTE_Time_Clock.setter
    def MARTE_Time_Clock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_Clock__MARTE_Time_Clock", None)
        self.__MARTE_Time_Clock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_InstanceSpecification"):
                opp_val = getattr(old_value, "Time_MARTE_InstanceSpecification", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_InstanceSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_InstanceSpecification"):
                opp_val = getattr(value, "Time_MARTE_InstanceSpecification", None)
                setattr(value, "Time_MARTE_InstanceSpecification", self)

class Time_MARTE_Namespace:

    pass
class MARTE_Time_TimedDomain:

    pass
class Alloc_MARTE_Abstraction:

    pass
class MARTE_Alloc_Allocate:

    def __init__(self, kind: str, nature: str, MARTE_Alloc_Allocate: "Alloc_MARTE_Abstraction" = None, MARTE_Alloc_Allocate48: set["NFPs_NfpConstraint"] = None):
        self.kind = kind
        self.nature = nature
        self.MARTE_Alloc_Allocate = MARTE_Alloc_Allocate
        self.MARTE_Alloc_Allocate48 = MARTE_Alloc_Allocate48 if MARTE_Alloc_Allocate48 is not None else set()
        
    @property
    def nature(self) -> str:
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def MARTE_Alloc_Allocate48(self):
        return self.__MARTE_Alloc_Allocate48

    @MARTE_Alloc_Allocate48.setter
    def MARTE_Alloc_Allocate48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Alloc_Allocate__MARTE_Alloc_Allocate48", None)
        self.__MARTE_Alloc_Allocate48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFPs_NfpConstraint49"):
                    opp_val = getattr(item, "NFPs_NfpConstraint49", None)
                    
                    if opp_val == self:
                        setattr(item, "NFPs_NfpConstraint49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFPs_NfpConstraint49"):
                    opp_val = getattr(item, "NFPs_NfpConstraint49", None)
                    
                    setattr(item, "NFPs_NfpConstraint49", self)
                    

    @property
    def MARTE_Alloc_Allocate(self):
        return self.__MARTE_Alloc_Allocate

    @MARTE_Alloc_Allocate.setter
    def MARTE_Alloc_Allocate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Alloc_Allocate__MARTE_Alloc_Allocate", None)
        self.__MARTE_Alloc_Allocate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Alloc_MARTE_Abstraction"):
                opp_val = getattr(old_value, "Alloc_MARTE_Abstraction", None)
                if opp_val == self:
                    setattr(old_value, "Alloc_MARTE_Abstraction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Alloc_MARTE_Abstraction"):
                opp_val = getattr(value, "Alloc_MARTE_Abstraction", None)
                setattr(value, "Alloc_MARTE_Abstraction", self)

class Alloc_Allocated:

    pass
class Alloc_MARTE_Element:

    pass
class MARTE_Alloc_Assign:

    pass
class NFPs_NfpConstraint:

    pass
class MARTE_Time_ClockConstraint(Time_TimedElement, NFPs_NfpConstraint):

    def __init__(self, isCoincidenceBased: str, isPrecedenceBased: bool, isChronometricBased: str, NFPs_NfpConstraint49: "MARTE_Alloc_Allocate", NFPs_NfpConstraint38: "MARTE_Alloc_Assign", NFPs_NfpConstraint: "MARTE_Alloc_NfpRefine"):
        self.isCoincidenceBased = isCoincidenceBased
        self.isPrecedenceBased = isPrecedenceBased
        self.isChronometricBased = isChronometricBased
        
    @property
    def isCoincidenceBased(self) -> str:
        return self.__isCoincidenceBased

    @isCoincidenceBased.setter
    def isCoincidenceBased(self, isCoincidenceBased: str):
        self.__isCoincidenceBased = isCoincidenceBased

    @property
    def isPrecedenceBased(self) -> bool:
        return self.__isPrecedenceBased

    @isPrecedenceBased.setter
    def isPrecedenceBased(self, isPrecedenceBased: bool):
        self.__isPrecedenceBased = isPrecedenceBased

    @property
    def isChronometricBased(self) -> str:
        return self.__isChronometricBased

    @isChronometricBased.setter
    def isChronometricBased(self, isChronometricBased: str):
        self.__isChronometricBased = isChronometricBased

class MARTE_Time_TimedConstraint(Time_TimedElement, NFPs_NfpConstraint):

    def __init__(self, interpretation: str, NFPs_NfpConstraint49: "MARTE_Alloc_Allocate", NFPs_NfpConstraint38: "MARTE_Alloc_Assign", NFPs_NfpConstraint: "MARTE_Alloc_NfpRefine"):
        self.interpretation = interpretation
        
    @property
    def interpretation(self) -> str:
        return self.__interpretation

    @interpretation.setter
    def interpretation(self, interpretation: str):
        self.__interpretation = interpretation

class Alloc_MARTE_Dependency:

    pass
class MARTE_Alloc_NfpRefine:

    pass
class Alloc_MARTE_ActivityPartition:

    pass
class MARTE_Alloc_AllocateActivityGroup:

    pass
class CoreElements_MARTE_StateMachine:

    pass
class MARTE_CoreElements_ModeBehavior:

    pass
class CoreElements_MARTE_Transition:

    pass
class MARTE_CoreElements_ModeTransition:

    pass
class Alloc_MARTE_NamedElement:

    pass
class MARTE_Alloc_Allocated:

    pass
class CoreElements_MARTE_State:

    pass
class MARTE_CoreElements_Mode:

    pass
class CoreElements_MARTE_Package:

    pass
class CoreElements_MARTE_StructuredClassifier:

    pass
class MARTE_CoreElements_Configuration:

    pass
class CoreElements_Mode:

    pass
class NFPs_MARTE_Constraint:

    pass
class NFPs_MARTE_Enumeration:

    pass
class NFPs_Dimension:

    pass
class MARTE_NFPs_Dimension:

    def __init__(self, symbol: str, baseExponent: int, MARTE_NFPs_Dimension: set["NFPs_Dimension"] = None, MARTE_NFPs_Dimension17: "NFPs_MARTE_Enumeration" = None):
        self.symbol = symbol
        self.baseExponent = baseExponent
        self.MARTE_NFPs_Dimension = MARTE_NFPs_Dimension if MARTE_NFPs_Dimension is not None else set()
        self.MARTE_NFPs_Dimension17 = MARTE_NFPs_Dimension17
        
    @property
    def baseExponent(self) -> int:
        return self.__baseExponent

    @baseExponent.setter
    def baseExponent(self, baseExponent: int):
        self.__baseExponent = baseExponent

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def MARTE_NFPs_Dimension(self):
        return self.__MARTE_NFPs_Dimension

    @MARTE_NFPs_Dimension.setter
    def MARTE_NFPs_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_NFPs_Dimension__MARTE_NFPs_Dimension", None)
        self.__MARTE_NFPs_Dimension = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFPs_Dimension"):
                    opp_val = getattr(item, "NFPs_Dimension", None)
                    
                    if opp_val == self:
                        setattr(item, "NFPs_Dimension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFPs_Dimension"):
                    opp_val = getattr(item, "NFPs_Dimension", None)
                    
                    setattr(item, "NFPs_Dimension", self)
                    

    @property
    def MARTE_NFPs_Dimension17(self):
        return self.__MARTE_NFPs_Dimension17

    @MARTE_NFPs_Dimension17.setter
    def MARTE_NFPs_Dimension17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_NFPs_Dimension__MARTE_NFPs_Dimension17", None)
        self.__MARTE_NFPs_Dimension17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFPs_MARTE_Enumeration"):
                opp_val = getattr(old_value, "NFPs_MARTE_Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "NFPs_MARTE_Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFPs_MARTE_Enumeration"):
                opp_val = getattr(value, "NFPs_MARTE_Enumeration", None)
                setattr(value, "NFPs_MARTE_Enumeration", self)

class TupleType:

    pass
class MARTE_NFPs_NfpType(TupleType):

    pass
class MARTE_NFPs_Unit:

    def __init__(self, offsetFactor: str, convFactor: str, MARTE_NFPs_Unit: "NFPs_Unit" = None, MARTE_NFPs_Unit3: "NFPs_MARTE_EnumerationLiteral" = None):
        self.offsetFactor = offsetFactor
        self.convFactor = convFactor
        self.MARTE_NFPs_Unit = MARTE_NFPs_Unit
        self.MARTE_NFPs_Unit3 = MARTE_NFPs_Unit3
        
    @property
    def convFactor(self) -> str:
        return self.__convFactor

    @convFactor.setter
    def convFactor(self, convFactor: str):
        self.__convFactor = convFactor

    @property
    def offsetFactor(self) -> str:
        return self.__offsetFactor

    @offsetFactor.setter
    def offsetFactor(self, offsetFactor: str):
        self.__offsetFactor = offsetFactor

    @property
    def MARTE_NFPs_Unit(self):
        return self.__MARTE_NFPs_Unit

    @MARTE_NFPs_Unit.setter
    def MARTE_NFPs_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_NFPs_Unit__MARTE_NFPs_Unit", None)
        self.__MARTE_NFPs_Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFPs_Unit"):
                opp_val = getattr(old_value, "NFPs_Unit", None)
                if opp_val == self:
                    setattr(old_value, "NFPs_Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFPs_Unit"):
                opp_val = getattr(value, "NFPs_Unit", None)
                setattr(value, "NFPs_Unit", self)

    @property
    def MARTE_NFPs_Unit3(self):
        return self.__MARTE_NFPs_Unit3

    @MARTE_NFPs_Unit3.setter
    def MARTE_NFPs_Unit3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_NFPs_Unit__MARTE_NFPs_Unit3", None)
        self.__MARTE_NFPs_Unit3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFPs_MARTE_EnumerationLiteral"):
                opp_val = getattr(old_value, "NFPs_MARTE_EnumerationLiteral", None)
                if opp_val == self:
                    setattr(old_value, "NFPs_MARTE_EnumerationLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFPs_MARTE_EnumerationLiteral"):
                opp_val = getattr(value, "NFPs_MARTE_EnumerationLiteral", None)
                setattr(value, "NFPs_MARTE_EnumerationLiteral", self)

class MARTE_NFPs_NfpConstraint:

    def __init__(self, kind: str, MARTE_NFPs_NfpConstraint: "NFPs_MARTE_Constraint" = None, MARTE_NFPs_NfpConstraint6: set["CoreElements_Mode"] = None):
        self.kind = kind
        self.MARTE_NFPs_NfpConstraint = MARTE_NFPs_NfpConstraint
        self.MARTE_NFPs_NfpConstraint6 = MARTE_NFPs_NfpConstraint6 if MARTE_NFPs_NfpConstraint6 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def MARTE_NFPs_NfpConstraint(self):
        return self.__MARTE_NFPs_NfpConstraint

    @MARTE_NFPs_NfpConstraint.setter
    def MARTE_NFPs_NfpConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_NFPs_NfpConstraint__MARTE_NFPs_NfpConstraint", None)
        self.__MARTE_NFPs_NfpConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFPs_MARTE_Constraint"):
                opp_val = getattr(old_value, "NFPs_MARTE_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "NFPs_MARTE_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFPs_MARTE_Constraint"):
                opp_val = getattr(value, "NFPs_MARTE_Constraint", None)
                setattr(value, "NFPs_MARTE_Constraint", self)

    @property
    def MARTE_NFPs_NfpConstraint6(self):
        return self.__MARTE_NFPs_NfpConstraint6

    @MARTE_NFPs_NfpConstraint6.setter
    def MARTE_NFPs_NfpConstraint6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_NFPs_NfpConstraint__MARTE_NFPs_NfpConstraint6", None)
        self.__MARTE_NFPs_NfpConstraint6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CoreElements_Mode"):
                    opp_val = getattr(item, "CoreElements_Mode", None)
                    
                    if opp_val == self:
                        setattr(item, "CoreElements_Mode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CoreElements_Mode"):
                    opp_val = getattr(item, "CoreElements_Mode", None)
                    
                    setattr(item, "CoreElements_Mode", self)
                    

class NFPs_MARTE_EnumerationLiteral:

    pass
class NFPs_Unit:

    pass
class NFPs_MARTE_Property:

    pass
class MARTE_NFPs_Nfp:

    pass