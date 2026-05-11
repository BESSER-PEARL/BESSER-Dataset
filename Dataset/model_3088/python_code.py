from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ROM_Type(Enum):
    maskedROM = "maskedROM"
    EPROM = "EPROM"
    OTP_EPROM = "OTP_EPROM"
    EEPROM = "EEPROM"
    Flash = "Flash"
    other = "other"
    undef = "undef"
class ConstraintKind(Enum):
    offered = "offered"
    contract = "contract"
    required = "required"
class AssignmentNature(Enum):
    timeScheduling = "timeScheduling"
    spatialDistribution = "spatialDistribution"
class AllocationNature(Enum):
    spatialDistribution = "spatialDistribution"
    timeScheduling = "timeScheduling"
class PLD_Technology(Enum):
    SRAM = "SRAM"
    antifuse = "antifuse"
    flash = "flash"
    other = "other"
    undef = "undef"
class ISA_Type(Enum):
    RISC = "RISC"
    CISC = "CISC"
    VLIW = "VLIW"
    SIMD = "SIMD"
    other = "other"
    undef = "undef"
class AssignmentKind(Enum):
    structural = "structural"
    behavioral = "behavioral"
    hybrid = "hybrid"
class ConditionType(Enum):
    temperature = "temperature"
    humidity = "humidity"
    altitude = "altitude"
    vibration = "vibration"
    shock = "shock"
    other = "other"
    undef = "undef"
class ConcurrencyKind(Enum):
    reader = "reader"
    writer = "writer"
    parallel = "parallel"
class AccessPolicyKind(Enum):
    Read = "Read"
    Write = "Write"
    ReadWrite = "ReadWrite"
    Undef = "Undef"
    Other = "Other"
class InterruptKind(Enum):
    HardwareInterruption = "HardwareInterruption"
    ProcessorDetectedException = "ProcessorDetectedException"
    ProgrammedException = "ProgrammedException"
    Undef = "Undef"
    Other = "Other"
class ExecutionKind(Enum):
    deferred = "deferred"
    remoteImmediate = "remoteImmediate"
    localImmediate = "localImmediate"
class ClientServerKind(Enum):
    required = "required"
    provided = "provided"
    proreq = "proreq"
class LaxityKind(Enum):
    hard = "hard"
    soft = "soft"
    other = "other"
class ConcurrentAccessProtocolKind(Enum):
    PIP = "PIP"
    PCP = "PCP"
    NoPreemption = "NoPreemption"
    Undef = "Undef"
    Other = "Other"
class NotificationResourceKind(Enum):
    Event = "Event"
    Barrier = "Barrier"
    Undef = "Undef"
    Other = "Other"
class MutualExclusionResourceKind(Enum):
    BooleanSemaphore = "BooleanSemaphore"
    CountSemaphore = "CountSemaphore"
    Mutex = "Mutex"
    Undef = "Undef"
    Other = "Other"
class PLD_Class(Enum):
    symetricalArray = "symetricalArray"
    rowBased = "rowBased"
    seaOfGates = "seaOfGates"
    hierarchicalPLD = "hierarchicalPLD"
    other = "other"
    undef = "undef"
class AllocationEndKind(Enum):
    undef = "undef"
    application = "application"
    executionPlatform = "executionPlatform"
    both = "both"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"
class QueuePolicyKind(Enum):
    FIFO = "FIFO"
    LIFO = "LIFO"
    Priority = "Priority"
    Undef = "Undef"
    Other = "Other"
class PortSpecificationKind(Enum):
    atomic = "atomic"
    interfaceBased = "interfaceBased"
    featureBased = "featureBased"
class Repl_Policy(Enum):
    LRU = "LRU"
    NFU = "NFU"
    FIFO = "FIFO"
    random = "random"
    other = "other"
    undef = "undef"
class PoolMgtPolicyKind(Enum):
    infiniteWait = "infiniteWait"
    timedWait = "timedWait"
    dynamic = "dynamic"
    exception = "exception"
    other = "other"
class OptimallityCriterionKind(Enum):
    meetHardDeadlines = "meetHardDeadlines"
    minimizeMissedDeadlines = "minimizeMissedDeadlines"
    minimizedMeanTardiness = "minimizedMeanTardiness"
    undef = "undef"
    other = "other"
class WritePolicy(Enum):
    writeBack = "writeBack"
    writeThrough = "writeThrough"
    other = "other"
    undef = "undef"
class ComponentKind(Enum):
    card = "card"
    channel = "channel"
    chip = "chip"
    port = "port"
    unit = "unit"
    other = "other"
    undef = "undef"
class CacheType(Enum):
    data = "data"
    instruction = "instruction"
    unified = "unified"
    other = "other"
    undef = "undef"
class AllocationKind(Enum):
    structural = "structural"
    behavioral = "behavioral"
    hybrid = "hybrid"
class NotificationKind(Enum):
    Memorized = "Memorized"
    Bounded = "Bounded"
    Memoryless = "Memoryless"
    Undef = "Undef"
    Other = "Other"
class SynchronizationKind(Enum):
    synchronous = "synchronous"
    asynchronous = "asynchronous"
    delayedSynchronous = "delayedSynchronous"
    rendezVous = "rendezVous"
    other = "other"
class DataPoolOrderingKind(Enum):
    FIFO = "FIFO"
    LIFO = "LIFO"
    UserDefined = "UserDefined"
class MessageResourceKind(Enum):
    MessageQueue = "MessageQueue"
    Pipe = "Pipe"
    Blackboard = "Blackboard"
    Undef = "Undef"
    Other = "Other"
class dummy(Enum):
    pass
class VariableDirectionKind(Enum):
    in_ = "in_"
    out = "out"
    inout = "inout"
class FlowDirectionKind(Enum):
    in_ = "in_"
    out = "out"
    inout = "inout"
class ComponentState(Enum):
    operating = "operating"
    storage = "storage"
    other = "other"
    undef = "undef"


############################################
# Definition of Classes
############################################

class GQAM_GaCommStep:

    pass
class PAM_PaStep:

    pass
class MARTE_PAM_PaCommStep(GQAM_GaCommStep, PAM_PaStep):

    pass
class PAM_MARTE_NamedElement:

    pass
class MARTE_PAM_PaRunTInstance:

    def __init__(self, poolSize: str, unbddPool: str, utilization: str, throughput: str, MARTE_PAM_PaRunTInstance: "GRM_SchedulableResource" = None, MARTE_PAM_PaRunTInstance536: "GQAM_GaExecHost" = None, MARTE_PAM_PaRunTInstance539: "PAM_MARTE_NamedElement" = None):
        self.poolSize = poolSize
        self.unbddPool = unbddPool
        self.utilization = utilization
        self.throughput = throughput
        self.MARTE_PAM_PaRunTInstance = MARTE_PAM_PaRunTInstance
        self.MARTE_PAM_PaRunTInstance536 = MARTE_PAM_PaRunTInstance536
        self.MARTE_PAM_PaRunTInstance539 = MARTE_PAM_PaRunTInstance539
        
        pass
    @property
    def throughput(self):
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput


    @property
    def unbddPool(self):
        return self.__unbddPool

    @unbddPool.setter
    def unbddPool(self, unbddPool: str):
        self.__unbddPool = unbddPool


    @property
    def poolSize(self):
        return self.__poolSize

    @poolSize.setter
    def poolSize(self, poolSize: str):
        self.__poolSize = poolSize


    @property
    def utilization(self):
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization


    @property
    def MARTE_PAM_PaRunTInstance536(self):
        return self.__MARTE_PAM_PaRunTInstance536

    @MARTE_PAM_PaRunTInstance536.setter
    def MARTE_PAM_PaRunTInstance536(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance536", None)
        self.__MARTE_PAM_PaRunTInstance536 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_GaExecHost537"):
                opp_val = getattr(old_value, "GQAM_GaExecHost537", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_GaExecHost537", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_GaExecHost537"):
                opp_val = getattr(value, "GQAM_GaExecHost537", None)
                setattr(value, "GQAM_GaExecHost537", self)

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
            if hasattr(old_value, "GRM_SchedulableResource534"):
                opp_val = getattr(old_value, "GRM_SchedulableResource534", None)
                if opp_val == self:
                    setattr(old_value, "GRM_SchedulableResource534", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_SchedulableResource534"):
                opp_val = getattr(value, "GRM_SchedulableResource534", None)
                setattr(value, "GRM_SchedulableResource534", self)

    @property
    def MARTE_PAM_PaRunTInstance539(self):
        return self.__MARTE_PAM_PaRunTInstance539

    @MARTE_PAM_PaRunTInstance539.setter
    def MARTE_PAM_PaRunTInstance539(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance539", None)
        self.__MARTE_PAM_PaRunTInstance539 = value
        
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

class GaExecHost:

    pass
class MARTE_SAM_SaExecHost(GaExecHost):

    def __init__(self, isSched: str, schSlack: str, schedUtiliz: str, ISRswitchT: str, ISRprioRange: str):
        self.isSched = isSched
        self.schSlack = schSlack
        self.schedUtiliz = schedUtiliz
        self.ISRswitchT = ISRswitchT
        self.ISRprioRange = ISRprioRange
        
        pass
    @property
    def ISRprioRange(self):
        return self.__ISRprioRange

    @ISRprioRange.setter
    def ISRprioRange(self, ISRprioRange: str):
        self.__ISRprioRange = ISRprioRange


    @property
    def isSched(self):
        return self.__isSched

    @isSched.setter
    def isSched(self, isSched: str):
        self.__isSched = isSched


    @property
    def schSlack(self):
        return self.__schSlack

    @schSlack.setter
    def schSlack(self, schSlack: str):
        self.__schSlack = schSlack


    @property
    def schedUtiliz(self):
        return self.__schedUtiliz

    @schedUtiliz.setter
    def schedUtiliz(self, schedUtiliz: str):
        self.__schedUtiliz = schedUtiliz


    @property
    def ISRswitchT(self):
        return self.__ISRswitchT

    @ISRswitchT.setter
    def ISRswitchT(self, ISRswitchT: str):
        self.__ISRswitchT = ISRswitchT


class GaCommHost:

    pass
class MARTE_SAM_SaCommHost(GaCommHost):

    def __init__(self, isSched: str, schSlack: str):
        self.isSched = isSched
        self.schSlack = schSlack
        
        pass
    @property
    def isSched(self):
        return self.__isSched

    @isSched.setter
    def isSched(self, isSched: str):
        self.__isSched = isSched


    @property
    def schSlack(self):
        return self.__schSlack

    @schSlack.setter
    def schSlack(self, schSlack: str):
        self.__schSlack = schSlack


class MutualExclusionResource:

    pass
class MARTE_SAM_SaSharedResource(MutualExclusionResource):

    def __init__(self, releaseT: str, capacity: str, isPreemp: str, isConsum: str, acquisT: str):
        self.releaseT = releaseT
        self.capacity = capacity
        self.isPreemp = isPreemp
        self.isConsum = isConsum
        self.acquisT = acquisT
        
        pass
    @property
    def acquisT(self):
        return self.__acquisT

    @acquisT.setter
    def acquisT(self, acquisT: str):
        self.__acquisT = acquisT


    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity


    @property
    def isConsum(self):
        return self.__isConsum

    @isConsum.setter
    def isConsum(self, isConsum: str):
        self.__isConsum = isConsum


    @property
    def releaseT(self):
        return self.__releaseT

    @releaseT.setter
    def releaseT(self, releaseT: str):
        self.__releaseT = releaseT


    @property
    def isPreemp(self):
        return self.__isPreemp

    @isPreemp.setter
    def isPreemp(self, isPreemp: str):
        self.__isPreemp = isPreemp


class SAM_SaSharedResource:

    pass
class SAM_MARTE_BehavioralFeature:

    pass
class MARTE_SAM_SaEndtoEndFlow:

    def __init__(self, isSched: str, schSlack: str, end2EndT: str, end2EndD: str, MARTE_SAM_SaEndtoEndFlow523: "SAM_MARTE_NamedElement" = None, MARTE_SAM_SaEndtoEndFlow: set["GQAM_GaTimedObs"] = None):
        self.isSched = isSched
        self.schSlack = schSlack
        self.end2EndT = end2EndT
        self.end2EndD = end2EndD
        self.MARTE_SAM_SaEndtoEndFlow523 = MARTE_SAM_SaEndtoEndFlow523
        self.MARTE_SAM_SaEndtoEndFlow = MARTE_SAM_SaEndtoEndFlow if MARTE_SAM_SaEndtoEndFlow is not None else set()
        
        pass
    @property
    def schSlack(self):
        return self.__schSlack

    @schSlack.setter
    def schSlack(self, schSlack: str):
        self.__schSlack = schSlack


    @property
    def end2EndD(self):
        return self.__end2EndD

    @end2EndD.setter
    def end2EndD(self, end2EndD: str):
        self.__end2EndD = end2EndD


    @property
    def isSched(self):
        return self.__isSched

    @isSched.setter
    def isSched(self, isSched: str):
        self.__isSched = isSched


    @property
    def end2EndT(self):
        return self.__end2EndT

    @end2EndT.setter
    def end2EndT(self, end2EndT: str):
        self.__end2EndT = end2EndT


    @property
    def MARTE_SAM_SaEndtoEndFlow(self):
        return self.__MARTE_SAM_SaEndtoEndFlow

    @MARTE_SAM_SaEndtoEndFlow.setter
    def MARTE_SAM_SaEndtoEndFlow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SAM_SaEndtoEndFlow__MARTE_SAM_SaEndtoEndFlow", None)
        self.__MARTE_SAM_SaEndtoEndFlow = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_GaTimedObs521"):
                    opp_val = getattr(item, "GQAM_GaTimedObs521", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_GaTimedObs521", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_GaTimedObs521"):
                    opp_val = getattr(item, "GQAM_GaTimedObs521", None)
                    
                    setattr(item, "GQAM_GaTimedObs521", self)
                    

    @property
    def MARTE_SAM_SaEndtoEndFlow523(self):
        return self.__MARTE_SAM_SaEndtoEndFlow523

    @MARTE_SAM_SaEndtoEndFlow523.setter
    def MARTE_SAM_SaEndtoEndFlow523(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SAM_SaEndtoEndFlow__MARTE_SAM_SaEndtoEndFlow523", None)
        self.__MARTE_SAM_SaEndtoEndFlow523 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SAM_MARTE_NamedElement"):
                opp_val = getattr(old_value, "SAM_MARTE_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "SAM_MARTE_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAM_MARTE_NamedElement"):
                opp_val = getattr(value, "SAM_MARTE_NamedElement", None)
                setattr(value, "SAM_MARTE_NamedElement", self)

class GaAnalysisContext:

    pass
class MARTE_SAM_SaAnalysisContext(GaAnalysisContext):

    def __init__(self, isSched: str, optCriterion: str):
        self.isSched = isSched
        self.optCriterion = optCriterion
        
        pass
    @property
    def isSched(self):
        return self.__isSched

    @isSched.setter
    def isSched(self, isSched: str):
        self.__isSched = isSched


    @property
    def optCriterion(self):
        return self.__optCriterion

    @optCriterion.setter
    def optCriterion(self, optCriterion: str):
        self.__optCriterion = optCriterion


class GQAM_MARTE_Classifier:

    pass
class MARTE_GQAM_GaResourcesPlatform:

    pass
class GQAM_GaResourcesPlatform:

    pass
class GQAM_GaWorkloadBehavior:

    pass
class Variables_ExpressionContext:

    pass
class CoreElements_Configuration:

    pass
class MARTE_GQAM_GaAnalysisContext(CoreElements_Configuration, Variables_ExpressionContext):

    def __init__(self, context: str, MARTE_GQAM_GaAnalysisContext: set["GQAM_GaWorkloadBehavior"] = None, MARTE_GQAM_GaAnalysisContext515: set["GQAM_GaResourcesPlatform"] = None):
        self.context = context
        self.MARTE_GQAM_GaAnalysisContext = MARTE_GQAM_GaAnalysisContext if MARTE_GQAM_GaAnalysisContext is not None else set()
        self.MARTE_GQAM_GaAnalysisContext515 = MARTE_GQAM_GaAnalysisContext515 if MARTE_GQAM_GaAnalysisContext515 is not None else set()
        
        pass
    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context


    @property
    def MARTE_GQAM_GaAnalysisContext515(self):
        return self.__MARTE_GQAM_GaAnalysisContext515

    @MARTE_GQAM_GaAnalysisContext515.setter
    def MARTE_GQAM_GaAnalysisContext515(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaAnalysisContext__MARTE_GQAM_GaAnalysisContext515", None)
        self.__MARTE_GQAM_GaAnalysisContext515 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_GaResourcesPlatform"):
                    opp_val = getattr(item, "GQAM_GaResourcesPlatform", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_GaResourcesPlatform", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_GaResourcesPlatform"):
                    opp_val = getattr(item, "GQAM_GaResourcesPlatform", None)
                    
                    setattr(item, "GQAM_GaResourcesPlatform", self)
                    

    @property
    def MARTE_GQAM_GaAnalysisContext(self):
        return self.__MARTE_GQAM_GaAnalysisContext

    @MARTE_GQAM_GaAnalysisContext.setter
    def MARTE_GQAM_GaAnalysisContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaAnalysisContext__MARTE_GQAM_GaAnalysisContext", None)
        self.__MARTE_GQAM_GaAnalysisContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_GaWorkloadBehavior"):
                    opp_val = getattr(item, "GQAM_GaWorkloadBehavior", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_GaWorkloadBehavior", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_GaWorkloadBehavior"):
                    opp_val = getattr(item, "GQAM_GaWorkloadBehavior", None)
                    
                    setattr(item, "GQAM_GaWorkloadBehavior", self)
                    

class GaCommStep:

    pass
class MARTE_SAM_SaCommStep(GaCommStep):

    def __init__(self, deadline: str, spareCap: str, schSlack: str, MARTE_SAM_SaCommStep: "SAM_MARTE_BehavioralFeature" = None):
        self.deadline = deadline
        self.spareCap = spareCap
        self.schSlack = schSlack
        self.MARTE_SAM_SaCommStep = MARTE_SAM_SaCommStep
        
        pass
    @property
    def schSlack(self):
        return self.__schSlack

    @schSlack.setter
    def schSlack(self, schSlack: str):
        self.__schSlack = schSlack


    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: str):
        self.__deadline = deadline


    @property
    def spareCap(self):
        return self.__spareCap

    @spareCap.setter
    def spareCap(self, spareCap: str):
        self.__spareCap = spareCap


    @property
    def MARTE_SAM_SaCommStep(self):
        return self.__MARTE_SAM_SaCommStep

    @MARTE_SAM_SaCommStep.setter
    def MARTE_SAM_SaCommStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SAM_SaCommStep__MARTE_SAM_SaCommStep", None)
        self.__MARTE_SAM_SaCommStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SAM_MARTE_BehavioralFeature"):
                opp_val = getattr(old_value, "SAM_MARTE_BehavioralFeature", None)
                if opp_val == self:
                    setattr(old_value, "SAM_MARTE_BehavioralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAM_MARTE_BehavioralFeature"):
                opp_val = getattr(value, "SAM_MARTE_BehavioralFeature", None)
                setattr(value, "SAM_MARTE_BehavioralFeature", self)

class SAM_MARTE_NamedElement:

    pass
class MARTE_GQAM_GaWorkloadBehavior:

    pass
class SchedulableResource:

    pass
class MARTE_GQAM_GaCommChannel(SchedulableResource):

    def __init__(self, packetSize: str, utilization: str):
        self.packetSize = packetSize
        self.utilization = utilization
        
        pass
    @property
    def utilization(self):
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization


    @property
    def packetSize(self):
        return self.__packetSize

    @packetSize.setter
    def packetSize(self, packetSize: str):
        self.__packetSize = packetSize


class GaTimedObs:

    pass
class MARTE_SAM_SaSchedObs(GaTimedObs):

    def __init__(self, suspentions: str, blockT: str, overlaps: str):
        self.suspentions = suspentions
        self.blockT = blockT
        self.overlaps = overlaps
        
        pass
    @property
    def overlaps(self):
        return self.__overlaps

    @overlaps.setter
    def overlaps(self, overlaps: str):
        self.__overlaps = overlaps


    @property
    def suspentions(self):
        return self.__suspentions

    @suspentions.setter
    def suspentions(self, suspentions: str):
        self.__suspentions = suspentions


    @property
    def blockT(self):
        return self.__blockT

    @blockT.setter
    def blockT(self, blockT: str):
        self.__blockT = blockT


class MARTE_GQAM_GaLatencyObs(GaTimedObs):

    def __init__(self, latency: str, miss: str, utility: str, maxJitter: str):
        self.latency = latency
        self.miss = miss
        self.utility = utility
        self.maxJitter = maxJitter
        
        pass
    @property
    def miss(self):
        return self.__miss

    @miss.setter
    def miss(self, miss: str):
        self.__miss = miss


    @property
    def maxJitter(self):
        return self.__maxJitter

    @maxJitter.setter
    def maxJitter(self, maxJitter: str):
        self.__maxJitter = maxJitter


    @property
    def utility(self):
        return self.__utility

    @utility.setter
    def utility(self, utility: str):
        self.__utility = utility


    @property
    def latency(self):
        return self.__latency

    @latency.setter
    def latency(self, latency: str):
        self.__latency = latency


class GQAM_MARTE_TimeObservation:

    pass
class NfpConstraint:

    pass
class MARTE_GQAM_GaTimedObs(NfpConstraint):

    def __init__(self, laxity: str, MARTE_GQAM_GaTimedObs499: set["GQAM_MARTE_TimeObservation"] = None, MARTE_GQAM_GaTimedObs: set["GQAM_MARTE_TimeObservation"] = None):
        self.laxity = laxity
        self.MARTE_GQAM_GaTimedObs499 = MARTE_GQAM_GaTimedObs499 if MARTE_GQAM_GaTimedObs499 is not None else set()
        self.MARTE_GQAM_GaTimedObs = MARTE_GQAM_GaTimedObs if MARTE_GQAM_GaTimedObs is not None else set()
        
        pass
    @property
    def laxity(self):
        return self.__laxity

    @laxity.setter
    def laxity(self, laxity: str):
        self.__laxity = laxity


    @property
    def MARTE_GQAM_GaTimedObs499(self):
        return self.__MARTE_GQAM_GaTimedObs499

    @MARTE_GQAM_GaTimedObs499.setter
    def MARTE_GQAM_GaTimedObs499(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaTimedObs__MARTE_GQAM_GaTimedObs499", None)
        self.__MARTE_GQAM_GaTimedObs499 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_MARTE_TimeObservation500"):
                    opp_val = getattr(item, "GQAM_MARTE_TimeObservation500", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_MARTE_TimeObservation500", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_MARTE_TimeObservation500"):
                    opp_val = getattr(item, "GQAM_MARTE_TimeObservation500", None)
                    
                    setattr(item, "GQAM_MARTE_TimeObservation500", self)
                    

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
class GaStep:

    pass
class MARTE_GQAM_GaCommStep(GaStep):

    pass
class MARTE_GQAM_GaAcqStep(GaStep):

    def __init__(self, resUnits: str, MARTE_GQAM_GaAcqStep: "GRM_Resource" = None):
        self.resUnits = resUnits
        self.MARTE_GQAM_GaAcqStep = MARTE_GQAM_GaAcqStep
        
        pass
    @property
    def resUnits(self):
        return self.__resUnits

    @resUnits.setter
    def resUnits(self, resUnits: str):
        self.__resUnits = resUnits


    @property
    def MARTE_GQAM_GaAcqStep(self):
        return self.__MARTE_GQAM_GaAcqStep

    @MARTE_GQAM_GaAcqStep.setter
    def MARTE_GQAM_GaAcqStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaAcqStep__MARTE_GQAM_GaAcqStep", None)
        self.__MARTE_GQAM_GaAcqStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_Resource502"):
                opp_val = getattr(old_value, "GRM_Resource502", None)
                if opp_val == self:
                    setattr(old_value, "GRM_Resource502", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_Resource502"):
                opp_val = getattr(value, "GRM_Resource502", None)
                setattr(value, "GRM_Resource502", self)

class MARTE_SAM_SaStep(GaStep):

    def __init__(self, deadline: str, spareCap: str, schSlack: str, preemptT: str, readyT: str, nonpreemptionBlocking: str, selfSuspensionBlocking: str, numberSelfSuspensions: str, MARTE_SAM_SaStep: "SAM_MARTE_BehavioralFeature" = None, MARTE_SAM_SaStep528: set["SAM_SaSharedResource"] = None):
        self.deadline = deadline
        self.spareCap = spareCap
        self.schSlack = schSlack
        self.preemptT = preemptT
        self.readyT = readyT
        self.nonpreemptionBlocking = nonpreemptionBlocking
        self.selfSuspensionBlocking = selfSuspensionBlocking
        self.numberSelfSuspensions = numberSelfSuspensions
        self.MARTE_SAM_SaStep = MARTE_SAM_SaStep
        self.MARTE_SAM_SaStep528 = MARTE_SAM_SaStep528 if MARTE_SAM_SaStep528 is not None else set()
        
        pass
    @property
    def schSlack(self):
        return self.__schSlack

    @schSlack.setter
    def schSlack(self, schSlack: str):
        self.__schSlack = schSlack


    @property
    def preemptT(self):
        return self.__preemptT

    @preemptT.setter
    def preemptT(self, preemptT: str):
        self.__preemptT = preemptT


    @property
    def readyT(self):
        return self.__readyT

    @readyT.setter
    def readyT(self, readyT: str):
        self.__readyT = readyT


    @property
    def numberSelfSuspensions(self):
        return self.__numberSelfSuspensions

    @numberSelfSuspensions.setter
    def numberSelfSuspensions(self, numberSelfSuspensions: str):
        self.__numberSelfSuspensions = numberSelfSuspensions


    @property
    def selfSuspensionBlocking(self):
        return self.__selfSuspensionBlocking

    @selfSuspensionBlocking.setter
    def selfSuspensionBlocking(self, selfSuspensionBlocking: str):
        self.__selfSuspensionBlocking = selfSuspensionBlocking


    @property
    def nonpreemptionBlocking(self):
        return self.__nonpreemptionBlocking

    @nonpreemptionBlocking.setter
    def nonpreemptionBlocking(self, nonpreemptionBlocking: str):
        self.__nonpreemptionBlocking = nonpreemptionBlocking


    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: str):
        self.__deadline = deadline


    @property
    def spareCap(self):
        return self.__spareCap

    @spareCap.setter
    def spareCap(self, spareCap: str):
        self.__spareCap = spareCap


    @property
    def MARTE_SAM_SaStep528(self):
        return self.__MARTE_SAM_SaStep528

    @MARTE_SAM_SaStep528.setter
    def MARTE_SAM_SaStep528(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SAM_SaStep__MARTE_SAM_SaStep528", None)
        self.__MARTE_SAM_SaStep528 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAM_SaSharedResource"):
                    opp_val = getattr(item, "SAM_SaSharedResource", None)
                    
                    if opp_val == self:
                        setattr(item, "SAM_SaSharedResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAM_SaSharedResource"):
                    opp_val = getattr(item, "SAM_SaSharedResource", None)
                    
                    setattr(item, "SAM_SaSharedResource", self)
                    

    @property
    def MARTE_SAM_SaStep(self):
        return self.__MARTE_SAM_SaStep

    @MARTE_SAM_SaStep.setter
    def MARTE_SAM_SaStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SAM_SaStep__MARTE_SAM_SaStep", None)
        self.__MARTE_SAM_SaStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SAM_MARTE_BehavioralFeature526"):
                opp_val = getattr(old_value, "SAM_MARTE_BehavioralFeature526", None)
                if opp_val == self:
                    setattr(old_value, "SAM_MARTE_BehavioralFeature526", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAM_MARTE_BehavioralFeature526"):
                opp_val = getattr(value, "SAM_MARTE_BehavioralFeature526", None)
                setattr(value, "SAM_MARTE_BehavioralFeature526", self)

class MARTE_GQAM_GaRelStep(GaStep):

    def __init__(self, resUnits: str, MARTE_GQAM_GaRelStep: "GRM_Resource" = None):
        self.resUnits = resUnits
        self.MARTE_GQAM_GaRelStep = MARTE_GQAM_GaRelStep
        
        pass
    @property
    def resUnits(self):
        return self.__resUnits

    @resUnits.setter
    def resUnits(self, resUnits: str):
        self.__resUnits = resUnits


    @property
    def MARTE_GQAM_GaRelStep(self):
        return self.__MARTE_GQAM_GaRelStep

    @MARTE_GQAM_GaRelStep.setter
    def MARTE_GQAM_GaRelStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaRelStep__MARTE_GQAM_GaRelStep", None)
        self.__MARTE_GQAM_GaRelStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_Resource504"):
                opp_val = getattr(old_value, "GRM_Resource504", None)
                if opp_val == self:
                    setattr(old_value, "GRM_Resource504", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_Resource504"):
                opp_val = getattr(value, "GRM_Resource504", None)
                setattr(value, "GRM_Resource504", self)

class MARTE_PAM_PaResPassStep(GaStep):

    def __init__(self, resUnits: str, MARTE_PAM_PaResPassStep: "GRM_Resource" = None):
        self.resUnits = resUnits
        self.MARTE_PAM_PaResPassStep = MARTE_PAM_PaResPassStep
        
        pass
    @property
    def resUnits(self):
        return self.__resUnits

    @resUnits.setter
    def resUnits(self, resUnits: str):
        self.__resUnits = resUnits


    @property
    def MARTE_PAM_PaResPassStep(self):
        return self.__MARTE_PAM_PaResPassStep

    @MARTE_PAM_PaResPassStep.setter
    def MARTE_PAM_PaResPassStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaResPassStep__MARTE_PAM_PaResPassStep", None)
        self.__MARTE_PAM_PaResPassStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_Resource532"):
                opp_val = getattr(old_value, "GRM_Resource532", None)
                if opp_val == self:
                    setattr(old_value, "GRM_Resource532", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_Resource532"):
                opp_val = getattr(value, "GRM_Resource532", None)
                setattr(value, "GRM_Resource532", self)

class MARTE_PAM_PaStep(GaStep):

    def __init__(self, noSync: str, extOpDemand: str, extOpCount: str, behavCount: str, MARTE_PAM_PaStep: set["GQAM_GaScenario"] = None):
        self.noSync = noSync
        self.extOpDemand = extOpDemand
        self.extOpCount = extOpCount
        self.behavCount = behavCount
        self.MARTE_PAM_PaStep = MARTE_PAM_PaStep if MARTE_PAM_PaStep is not None else set()
        
        pass
    @property
    def noSync(self):
        return self.__noSync

    @noSync.setter
    def noSync(self, noSync: str):
        self.__noSync = noSync


    @property
    def extOpCount(self):
        return self.__extOpCount

    @extOpCount.setter
    def extOpCount(self, extOpCount: str):
        self.__extOpCount = extOpCount


    @property
    def extOpDemand(self):
        return self.__extOpDemand

    @extOpDemand.setter
    def extOpDemand(self, extOpDemand: str):
        self.__extOpDemand = extOpDemand


    @property
    def behavCount(self):
        return self.__behavCount

    @behavCount.setter
    def behavCount(self, behavCount: str):
        self.__behavCount = behavCount


    @property
    def MARTE_PAM_PaStep(self):
        return self.__MARTE_PAM_PaStep

    @MARTE_PAM_PaStep.setter
    def MARTE_PAM_PaStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaStep__MARTE_PAM_PaStep", None)
        self.__MARTE_PAM_PaStep = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_GaScenario530"):
                    opp_val = getattr(item, "GQAM_GaScenario530", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_GaScenario530", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_GaScenario530"):
                    opp_val = getattr(item, "GQAM_GaScenario530", None)
                    
                    setattr(item, "GQAM_GaScenario530", self)
                    

class MARTE_GQAM_GaRequestedService(GaStep):

    pass
class GQAM_GaExecHost:

    pass
class GaScenario:

    pass
class MARTE_GQAM_GaStep(GaScenario):

    def __init__(self, isAtomic: str, blockT: str, rep: str, prob: str, priority: str, servCount: str, selfDelay: str, MARTE_GQAM_GaStep492: set["GQAM_GaRequestedService"] = None, MARTE_GQAM_GaStep: "GRM_SchedulableResource" = None, MARTE_GQAM_GaStep490: "GQAM_GaExecHost" = None, steps: "GQAM_GaScenario" = None, parentStep: "GQAM_GaScenario" = None):
        self.isAtomic = isAtomic
        self.blockT = blockT
        self.rep = rep
        self.prob = prob
        self.priority = priority
        self.servCount = servCount
        self.selfDelay = selfDelay
        self.MARTE_GQAM_GaStep492 = MARTE_GQAM_GaStep492 if MARTE_GQAM_GaStep492 is not None else set()
        self.MARTE_GQAM_GaStep = MARTE_GQAM_GaStep
        self.MARTE_GQAM_GaStep490 = MARTE_GQAM_GaStep490
        self.steps = steps
        self.parentStep = parentStep
        
        pass
    @property
    def prob(self):
        return self.__prob

    @prob.setter
    def prob(self, prob: str):
        self.__prob = prob


    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority


    @property
    def servCount(self):
        return self.__servCount

    @servCount.setter
    def servCount(self, servCount: str):
        self.__servCount = servCount


    @property
    def blockT(self):
        return self.__blockT

    @blockT.setter
    def blockT(self, blockT: str):
        self.__blockT = blockT


    @property
    def rep(self):
        return self.__rep

    @rep.setter
    def rep(self, rep: str):
        self.__rep = rep


    @property
    def isAtomic(self):
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic


    @property
    def selfDelay(self):
        return self.__selfDelay

    @selfDelay.setter
    def selfDelay(self, selfDelay: str):
        self.__selfDelay = selfDelay


    @property
    def MARTE_GQAM_GaStep492(self):
        return self.__MARTE_GQAM_GaStep492

    @MARTE_GQAM_GaStep492.setter
    def MARTE_GQAM_GaStep492(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaStep__MARTE_GQAM_GaStep492", None)
        self.__MARTE_GQAM_GaStep492 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_GaRequestedService"):
                    opp_val = getattr(item, "GQAM_GaRequestedService", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_GaRequestedService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_GaRequestedService"):
                    opp_val = getattr(item, "GQAM_GaRequestedService", None)
                    
                    setattr(item, "GQAM_GaRequestedService", self)
                    

    @property
    def MARTE_GQAM_GaStep(self):
        return self.__MARTE_GQAM_GaStep

    @MARTE_GQAM_GaStep.setter
    def MARTE_GQAM_GaStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaStep__MARTE_GQAM_GaStep", None)
        self.__MARTE_GQAM_GaStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_SchedulableResource"):
                opp_val = getattr(old_value, "GRM_SchedulableResource", None)
                if opp_val == self:
                    setattr(old_value, "GRM_SchedulableResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_SchedulableResource"):
                opp_val = getattr(value, "GRM_SchedulableResource", None)
                setattr(value, "GRM_SchedulableResource", self)

    @property
    def steps(self):
        return self.__steps

    @steps.setter
    def steps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaStep__steps", None)
        self.__steps = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GaScenario"):
                opp_val = getattr(old_value, "GaScenario", None)
                if opp_val == self:
                    setattr(old_value, "GaScenario", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GaScenario"):
                opp_val = getattr(value, "GaScenario", None)
                setattr(value, "GaScenario", self)

    @property
    def parentStep(self):
        return self.__parentStep

    @parentStep.setter
    def parentStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaStep__parentStep", None)
        self.__parentStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GaScenario495"):
                opp_val = getattr(old_value, "GaScenario495", None)
                if opp_val == self:
                    setattr(old_value, "GaScenario495", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GaScenario495"):
                opp_val = getattr(value, "GaScenario495", None)
                setattr(value, "GaScenario495", self)

    @property
    def MARTE_GQAM_GaStep490(self):
        return self.__MARTE_GQAM_GaStep490

    @MARTE_GQAM_GaStep490.setter
    def MARTE_GQAM_GaStep490(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaStep__MARTE_GQAM_GaStep490", None)
        self.__MARTE_GQAM_GaStep490 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_GaExecHost"):
                opp_val = getattr(old_value, "GQAM_GaExecHost", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_GaExecHost", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_GaExecHost"):
                opp_val = getattr(value, "GQAM_GaExecHost", None)
                setattr(value, "GQAM_GaExecHost", self)

class GQAM_GaTimedObs:

    pass
class GQAM_GaRequestedService:

    pass
class MARTE_PAM_PaRequestedStep(GQAM_GaRequestedService, PAM_PaStep):

    pass
class GQAM_GaWorkloadEvent:

    pass
class Time_TimedProcessing:

    pass
class GQAM_MARTE_TimeEvent:

    pass
class GQAM_GaScenario:

    pass
class GQAM_GaEventTrace:

    pass
class GQAM_GaWorkloadGenerator:

    pass
class MARTE_GQAM_GaWorkloadEvent:

    def __init__(self, pattern: str, MARTE_GQAM_GaWorkloadEvent: "GQAM_GaWorkloadGenerator" = None, MARTE_GQAM_GaWorkloadEvent472: "GQAM_GaEventTrace" = None, MARTE_GQAM_GaWorkloadEvent474: "GQAM_GaScenario" = None, MARTE_GQAM_GaWorkloadEvent476: "GQAM_MARTE_TimeEvent" = None, MARTE_GQAM_GaWorkloadEvent478: "GQAM_MARTE_NamedElement" = None):
        self.pattern = pattern
        self.MARTE_GQAM_GaWorkloadEvent = MARTE_GQAM_GaWorkloadEvent
        self.MARTE_GQAM_GaWorkloadEvent472 = MARTE_GQAM_GaWorkloadEvent472
        self.MARTE_GQAM_GaWorkloadEvent474 = MARTE_GQAM_GaWorkloadEvent474
        self.MARTE_GQAM_GaWorkloadEvent476 = MARTE_GQAM_GaWorkloadEvent476
        self.MARTE_GQAM_GaWorkloadEvent478 = MARTE_GQAM_GaWorkloadEvent478
        
        pass
    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern


    @property
    def MARTE_GQAM_GaWorkloadEvent474(self):
        return self.__MARTE_GQAM_GaWorkloadEvent474

    @MARTE_GQAM_GaWorkloadEvent474.setter
    def MARTE_GQAM_GaWorkloadEvent474(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaWorkloadEvent__MARTE_GQAM_GaWorkloadEvent474", None)
        self.__MARTE_GQAM_GaWorkloadEvent474 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_GaScenario"):
                opp_val = getattr(old_value, "GQAM_GaScenario", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_GaScenario", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_GaScenario"):
                opp_val = getattr(value, "GQAM_GaScenario", None)
                setattr(value, "GQAM_GaScenario", self)

    @property
    def MARTE_GQAM_GaWorkloadEvent476(self):
        return self.__MARTE_GQAM_GaWorkloadEvent476

    @MARTE_GQAM_GaWorkloadEvent476.setter
    def MARTE_GQAM_GaWorkloadEvent476(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaWorkloadEvent__MARTE_GQAM_GaWorkloadEvent476", None)
        self.__MARTE_GQAM_GaWorkloadEvent476 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_MARTE_TimeEvent"):
                opp_val = getattr(old_value, "GQAM_MARTE_TimeEvent", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_MARTE_TimeEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_MARTE_TimeEvent"):
                opp_val = getattr(value, "GQAM_MARTE_TimeEvent", None)
                setattr(value, "GQAM_MARTE_TimeEvent", self)

    @property
    def MARTE_GQAM_GaWorkloadEvent478(self):
        return self.__MARTE_GQAM_GaWorkloadEvent478

    @MARTE_GQAM_GaWorkloadEvent478.setter
    def MARTE_GQAM_GaWorkloadEvent478(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaWorkloadEvent__MARTE_GQAM_GaWorkloadEvent478", None)
        self.__MARTE_GQAM_GaWorkloadEvent478 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_MARTE_NamedElement479"):
                opp_val = getattr(old_value, "GQAM_MARTE_NamedElement479", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_MARTE_NamedElement479", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_MARTE_NamedElement479"):
                opp_val = getattr(value, "GQAM_MARTE_NamedElement479", None)
                setattr(value, "GQAM_MARTE_NamedElement479", self)

    @property
    def MARTE_GQAM_GaWorkloadEvent(self):
        return self.__MARTE_GQAM_GaWorkloadEvent

    @MARTE_GQAM_GaWorkloadEvent.setter
    def MARTE_GQAM_GaWorkloadEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaWorkloadEvent__MARTE_GQAM_GaWorkloadEvent", None)
        self.__MARTE_GQAM_GaWorkloadEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_GaWorkloadGenerator"):
                opp_val = getattr(old_value, "GQAM_GaWorkloadGenerator", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_GaWorkloadGenerator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_GaWorkloadGenerator"):
                opp_val = getattr(value, "GQAM_GaWorkloadGenerator", None)
                setattr(value, "GQAM_GaWorkloadGenerator", self)

    @property
    def MARTE_GQAM_GaWorkloadEvent472(self):
        return self.__MARTE_GQAM_GaWorkloadEvent472

    @MARTE_GQAM_GaWorkloadEvent472.setter
    def MARTE_GQAM_GaWorkloadEvent472(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaWorkloadEvent__MARTE_GQAM_GaWorkloadEvent472", None)
        self.__MARTE_GQAM_GaWorkloadEvent472 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_GaEventTrace"):
                opp_val = getattr(old_value, "GQAM_GaEventTrace", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_GaEventTrace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_GaEventTrace"):
                opp_val = getattr(value, "GQAM_GaEventTrace", None)
                setattr(value, "GQAM_GaEventTrace", self)

class GQAM_MARTE_NamedElement:

    pass
class GQAM_GaStep:

    pass
class MARTE_GQAM_GaWorkloadGenerator:

    def __init__(self, pop: str, MARTE_GQAM_GaWorkloadGenerator: "GQAM_MARTE_Behavior" = None):
        self.pop = pop
        self.MARTE_GQAM_GaWorkloadGenerator = MARTE_GQAM_GaWorkloadGenerator
        
        pass
    @property
    def pop(self):
        return self.__pop

    @pop.setter
    def pop(self, pop: str):
        self.__pop = pop


    @property
    def MARTE_GQAM_GaWorkloadGenerator(self):
        return self.__MARTE_GQAM_GaWorkloadGenerator

    @MARTE_GQAM_GaWorkloadGenerator.setter
    def MARTE_GQAM_GaWorkloadGenerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaWorkloadGenerator__MARTE_GQAM_GaWorkloadGenerator", None)
        self.__MARTE_GQAM_GaWorkloadGenerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_MARTE_Behavior"):
                opp_val = getattr(old_value, "GQAM_MARTE_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_MARTE_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_MARTE_Behavior"):
                opp_val = getattr(value, "GQAM_MARTE_Behavior", None)
                setattr(value, "GQAM_MARTE_Behavior", self)

class MARTE_GCM_GCMInvocatingBehavior:

    pass
class GCM_MARTE_Behavior:

    pass
class MARTE_GCM_DataPool:

    def __init__(self, ordering: str, MARTE_GCM_DataPool: "GCM_MARTE_Property" = None, MARTE_GCM_DataPool453: "GCM_MARTE_Behavior" = None, MARTE_GCM_DataPool455: "GCM_MARTE_Behavior" = None):
        self.ordering = ordering
        self.MARTE_GCM_DataPool = MARTE_GCM_DataPool
        self.MARTE_GCM_DataPool453 = MARTE_GCM_DataPool453
        self.MARTE_GCM_DataPool455 = MARTE_GCM_DataPool455
        
        pass
    @property
    def ordering(self):
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering


    @property
    def MARTE_GCM_DataPool453(self):
        return self.__MARTE_GCM_DataPool453

    @MARTE_GCM_DataPool453.setter
    def MARTE_GCM_DataPool453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_DataPool__MARTE_GCM_DataPool453", None)
        self.__MARTE_GCM_DataPool453 = value
        
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
    def MARTE_GCM_DataPool455(self):
        return self.__MARTE_GCM_DataPool455

    @MARTE_GCM_DataPool455.setter
    def MARTE_GCM_DataPool455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_DataPool__MARTE_GCM_DataPool455", None)
        self.__MARTE_GCM_DataPool455 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_Behavior456"):
                opp_val = getattr(old_value, "GCM_MARTE_Behavior456", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Behavior456", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Behavior456"):
                opp_val = getattr(value, "GCM_MARTE_Behavior456", None)
                setattr(value, "GCM_MARTE_Behavior456", self)

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
            if hasattr(old_value, "GCM_MARTE_Property451"):
                opp_val = getattr(old_value, "GCM_MARTE_Property451", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Property451", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Property451"):
                opp_val = getattr(value, "GCM_MARTE_Property451", None)
                setattr(value, "GCM_MARTE_Property451", self)

class GCM_MARTE_Classifier:

    pass
class GCM_MARTE_AnyReceiveEvent:

    pass
class MARTE_GCM_DataEvent:

    pass
class GCM_MARTE_InvocationAction:

    pass
class MARTE_GCM_GCMInvocationAction:

    pass
class GCM_MARTE_Feature:

    pass
class MARTE_GQAM_GaEventTrace:

    def __init__(self, content: str, format: str, location: str, MARTE_GQAM_GaEventTrace: "GQAM_MARTE_NamedElement" = None):
        self.content = content
        self.format = format
        self.location = location
        self.MARTE_GQAM_GaEventTrace = MARTE_GQAM_GaEventTrace
        
        pass
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format


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

class GQAM_MARTE_Behavior:

    pass
class GCM_MARTE_BehavioralFeature:

    pass
class MARTE_GCM_ClientServerFeature:

    def __init__(self, kind: str, MARTE_GCM_ClientServerFeature: "GCM_MARTE_BehavioralFeature" = None):
        self.kind = kind
        self.MARTE_GCM_ClientServerFeature = MARTE_GCM_ClientServerFeature
        
        pass
    @property
    def kind(self):
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
class GCM_ClientServerSpecification:

    pass
class GCM_MARTE_Interface:

    pass
class MARTE_GCM_ClientServerPort:

    def __init__(self, specificationKind: str, kind: str, MARTE_GCM_ClientServerPort: "GCM_MARTE_Port" = None, MARTE_GCM_ClientServerPort429: set["GCM_MARTE_Interface"] = None, MARTE_GCM_ClientServerPort431: set["GCM_MARTE_Interface"] = None, MARTE_GCM_ClientServerPort434: "GCM_ClientServerSpecification" = None):
        self.specificationKind = specificationKind
        self.kind = kind
        self.MARTE_GCM_ClientServerPort = MARTE_GCM_ClientServerPort
        self.MARTE_GCM_ClientServerPort429 = MARTE_GCM_ClientServerPort429 if MARTE_GCM_ClientServerPort429 is not None else set()
        self.MARTE_GCM_ClientServerPort431 = MARTE_GCM_ClientServerPort431 if MARTE_GCM_ClientServerPort431 is not None else set()
        self.MARTE_GCM_ClientServerPort434 = MARTE_GCM_ClientServerPort434
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def specificationKind(self):
        return self.__specificationKind

    @specificationKind.setter
    def specificationKind(self, specificationKind: str):
        self.__specificationKind = specificationKind


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
            if hasattr(old_value, "GCM_MARTE_Port427"):
                opp_val = getattr(old_value, "GCM_MARTE_Port427", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Port427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Port427"):
                opp_val = getattr(value, "GCM_MARTE_Port427", None)
                setattr(value, "GCM_MARTE_Port427", self)

    @property
    def MARTE_GCM_ClientServerPort429(self):
        return self.__MARTE_GCM_ClientServerPort429

    @MARTE_GCM_ClientServerPort429.setter
    def MARTE_GCM_ClientServerPort429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort429", None)
        self.__MARTE_GCM_ClientServerPort429 = value if value is not None else set()
        
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
                    

    @property
    def MARTE_GCM_ClientServerPort434(self):
        return self.__MARTE_GCM_ClientServerPort434

    @MARTE_GCM_ClientServerPort434.setter
    def MARTE_GCM_ClientServerPort434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort434", None)
        self.__MARTE_GCM_ClientServerPort434 = value
        
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
    def MARTE_GCM_ClientServerPort431(self):
        return self.__MARTE_GCM_ClientServerPort431

    @MARTE_GCM_ClientServerPort431.setter
    def MARTE_GCM_ClientServerPort431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort431", None)
        self.__MARTE_GCM_ClientServerPort431 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GCM_MARTE_Interface432"):
                    opp_val = getattr(item, "GCM_MARTE_Interface432", None)
                    
                    if opp_val == self:
                        setattr(item, "GCM_MARTE_Interface432", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GCM_MARTE_Interface432"):
                    opp_val = getattr(item, "GCM_MARTE_Interface432", None)
                    
                    setattr(item, "GCM_MARTE_Interface432", self)
                    

class GCM_MARTE_Port:

    pass
class MARTE_GCM_FlowPort:

    def __init__(self, isAtomic: str, direction: str, MARTE_GCM_FlowPort: "GCM_MARTE_Port" = None):
        self.isAtomic = isAtomic
        self.direction = direction
        self.MARTE_GCM_FlowPort = MARTE_GCM_FlowPort
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def isAtomic(self):
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

class GCM_MARTE_Trigger:

    pass
class MARTE_GCM_GCMTrigger:

    pass
class MARTE_GCM_FlowProperty:

    def __init__(self, direction: str, MARTE_GCM_FlowProperty: "GCM_MARTE_Property" = None):
        self.direction = direction
        self.MARTE_GCM_FlowProperty = MARTE_GCM_FlowProperty
        
        pass
    @property
    def direction(self):
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
class SwSynchronizationResource:

    pass
class MARTE_SW_Interaction_NotificationResource(SwSynchronizationResource):

    def __init__(self, occurence: str, mechanism: str, MARTE_SW_Interaction_NotificationResource: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_NotificationResource402: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_NotificationResource405: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource408: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource411: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource414: set["SW_Interaction_MARTE_BehavioralFeature"] = None):
        self.occurence = occurence
        self.mechanism = mechanism
        self.MARTE_SW_Interaction_NotificationResource = MARTE_SW_Interaction_NotificationResource if MARTE_SW_Interaction_NotificationResource is not None else set()
        self.MARTE_SW_Interaction_NotificationResource402 = MARTE_SW_Interaction_NotificationResource402 if MARTE_SW_Interaction_NotificationResource402 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource405 = MARTE_SW_Interaction_NotificationResource405 if MARTE_SW_Interaction_NotificationResource405 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource408 = MARTE_SW_Interaction_NotificationResource408 if MARTE_SW_Interaction_NotificationResource408 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource411 = MARTE_SW_Interaction_NotificationResource411 if MARTE_SW_Interaction_NotificationResource411 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource414 = MARTE_SW_Interaction_NotificationResource414 if MARTE_SW_Interaction_NotificationResource414 is not None else set()
        
        pass
    @property
    def occurence(self):
        return self.__occurence

    @occurence.setter
    def occurence(self, occurence: str):
        self.__occurence = occurence


    @property
    def mechanism(self):
        return self.__mechanism

    @mechanism.setter
    def mechanism(self, mechanism: str):
        self.__mechanism = mechanism


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
                if hasattr(item, "SW_Interaction_MARTE_TypedElement400"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement400", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement400", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement400"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement400", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement400", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource414(self):
        return self.__MARTE_SW_Interaction_NotificationResource414

    @MARTE_SW_Interaction_NotificationResource414.setter
    def MARTE_SW_Interaction_NotificationResource414(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource414", None)
        self.__MARTE_SW_Interaction_NotificationResource414 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature415"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature415", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature415", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature415"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature415", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature415", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource408(self):
        return self.__MARTE_SW_Interaction_NotificationResource408

    @MARTE_SW_Interaction_NotificationResource408.setter
    def MARTE_SW_Interaction_NotificationResource408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource408", None)
        self.__MARTE_SW_Interaction_NotificationResource408 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature409"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature409", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature409", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature409"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature409", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature409", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource405(self):
        return self.__MARTE_SW_Interaction_NotificationResource405

    @MARTE_SW_Interaction_NotificationResource405.setter
    def MARTE_SW_Interaction_NotificationResource405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource405", None)
        self.__MARTE_SW_Interaction_NotificationResource405 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature406"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature406", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature406", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature406"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature406", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature406", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource402(self):
        return self.__MARTE_SW_Interaction_NotificationResource402

    @MARTE_SW_Interaction_NotificationResource402.setter
    def MARTE_SW_Interaction_NotificationResource402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource402", None)
        self.__MARTE_SW_Interaction_NotificationResource402 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement403"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement403", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement403", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement403"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement403", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement403", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource411(self):
        return self.__MARTE_SW_Interaction_NotificationResource411

    @MARTE_SW_Interaction_NotificationResource411.setter
    def MARTE_SW_Interaction_NotificationResource411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource411", None)
        self.__MARTE_SW_Interaction_NotificationResource411 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature412"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature412", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature412", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature412"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature412", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature412", self)
                    

class GCM_MARTE_Property:

    pass
class SW_Interaction_MARTE_BehavioralFeature:

    pass
class SwCommunicationResource:

    pass
class MARTE_SW_Interaction_MessageComResource(SwCommunicationResource):

    def __init__(self, isFixedMessageSize: str, mechanism: str, messageQueuePolicy: str, MARTE_SW_Interaction_MessageComResource394: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_MessageComResource: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_MessageComResource391: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_MessageComResource397: set["SW_Interaction_MARTE_BehavioralFeature"] = None):
        self.isFixedMessageSize = isFixedMessageSize
        self.mechanism = mechanism
        self.messageQueuePolicy = messageQueuePolicy
        self.MARTE_SW_Interaction_MessageComResource394 = MARTE_SW_Interaction_MessageComResource394 if MARTE_SW_Interaction_MessageComResource394 is not None else set()
        self.MARTE_SW_Interaction_MessageComResource = MARTE_SW_Interaction_MessageComResource if MARTE_SW_Interaction_MessageComResource is not None else set()
        self.MARTE_SW_Interaction_MessageComResource391 = MARTE_SW_Interaction_MessageComResource391 if MARTE_SW_Interaction_MessageComResource391 is not None else set()
        self.MARTE_SW_Interaction_MessageComResource397 = MARTE_SW_Interaction_MessageComResource397 if MARTE_SW_Interaction_MessageComResource397 is not None else set()
        
        pass
    @property
    def mechanism(self):
        return self.__mechanism

    @mechanism.setter
    def mechanism(self, mechanism: str):
        self.__mechanism = mechanism


    @property
    def messageQueuePolicy(self):
        return self.__messageQueuePolicy

    @messageQueuePolicy.setter
    def messageQueuePolicy(self, messageQueuePolicy: str):
        self.__messageQueuePolicy = messageQueuePolicy


    @property
    def isFixedMessageSize(self):
        return self.__isFixedMessageSize

    @isFixedMessageSize.setter
    def isFixedMessageSize(self, isFixedMessageSize: str):
        self.__isFixedMessageSize = isFixedMessageSize


    @property
    def MARTE_SW_Interaction_MessageComResource391(self):
        return self.__MARTE_SW_Interaction_MessageComResource391

    @MARTE_SW_Interaction_MessageComResource391.setter
    def MARTE_SW_Interaction_MessageComResource391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource391", None)
        self.__MARTE_SW_Interaction_MessageComResource391 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement392"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement392", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement392", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement392"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement392", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement392", self)
                    

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
                if hasattr(item, "SW_Interaction_MARTE_TypedElement389"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement389", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement389", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement389"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement389", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement389", self)
                    

    @property
    def MARTE_SW_Interaction_MessageComResource394(self):
        return self.__MARTE_SW_Interaction_MessageComResource394

    @MARTE_SW_Interaction_MessageComResource394.setter
    def MARTE_SW_Interaction_MessageComResource394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource394", None)
        self.__MARTE_SW_Interaction_MessageComResource394 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature395"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature395", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature395", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature395"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature395", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature395", self)
                    

    @property
    def MARTE_SW_Interaction_MessageComResource397(self):
        return self.__MARTE_SW_Interaction_MessageComResource397

    @MARTE_SW_Interaction_MessageComResource397.setter
    def MARTE_SW_Interaction_MessageComResource397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource397", None)
        self.__MARTE_SW_Interaction_MessageComResource397 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature398"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature398", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature398", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature398"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature398", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature398", self)
                    

class MARTE_SW_Interaction_SharedDataComResource(SwCommunicationResource):

    pass
class GRM_SynchronizationResource:

    pass
class MARTE_DataTypes_BoundedSubtype:

    def __init__(self, minValue: str, maxValue: str, isMinOpen: bool, isMaxOpen: bool, MARTE_DataTypes_BoundedSubtype: "DataTypes_MARTE_DataType" = None, MARTE_DataTypes_BoundedSubtype150: "DataTypes_MARTE_DataType" = None):
        self.minValue = minValue
        self.maxValue = maxValue
        self.isMinOpen = isMinOpen
        self.isMaxOpen = isMaxOpen
        self.MARTE_DataTypes_BoundedSubtype = MARTE_DataTypes_BoundedSubtype
        self.MARTE_DataTypes_BoundedSubtype150 = MARTE_DataTypes_BoundedSubtype150
        
        pass
    @property
    def isMinOpen(self):
        return self.__isMinOpen

    @isMinOpen.setter
    def isMinOpen(self, isMinOpen: bool):
        self.__isMinOpen = isMinOpen


    @property
    def minValue(self):
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: str):
        self.__minValue = minValue


    @property
    def maxValue(self):
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: str):
        self.__maxValue = maxValue


    @property
    def isMaxOpen(self):
        return self.__isMaxOpen

    @isMaxOpen.setter
    def isMaxOpen(self, isMaxOpen: bool):
        self.__isMaxOpen = isMaxOpen


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
    def MARTE_DataTypes_BoundedSubtype150(self):
        return self.__MARTE_DataTypes_BoundedSubtype150

    @MARTE_DataTypes_BoundedSubtype150.setter
    def MARTE_DataTypes_BoundedSubtype150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_DataTypes_BoundedSubtype__MARTE_DataTypes_BoundedSubtype150", None)
        self.__MARTE_DataTypes_BoundedSubtype150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataTypes_MARTE_DataType151"):
                opp_val = getattr(old_value, "DataTypes_MARTE_DataType151", None)
                if opp_val == self:
                    setattr(old_value, "DataTypes_MARTE_DataType151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataTypes_MARTE_DataType151"):
                opp_val = getattr(value, "DataTypes_MARTE_DataType151", None)
                setattr(value, "DataTypes_MARTE_DataType151", self)

class Operators_MARTE_Behavior:

    pass
class MARTE_Operators_Operator:

    def __init__(self, symbol: str, arity: str, MARTE_Operators_Operator: "Operators_MARTE_Behavior" = None):
        self.symbol = symbol
        self.arity = arity
        self.MARTE_Operators_Operator = MARTE_Operators_Operator
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


    @property
    def arity(self):
        return self.__arity

    @arity.setter
    def arity(self, arity: str):
        self.__arity = arity


    @property
    def MARTE_Operators_Operator(self):
        return self.__MARTE_Operators_Operator

    @MARTE_Operators_Operator.setter
    def MARTE_Operators_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Operators_Operator__MARTE_Operators_Operator", None)
        self.__MARTE_Operators_Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operators_MARTE_Behavior"):
                opp_val = getattr(old_value, "Operators_MARTE_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "Operators_MARTE_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operators_MARTE_Behavior"):
                opp_val = getattr(value, "Operators_MARTE_Behavior", None)
                setattr(value, "Operators_MARTE_Behavior", self)

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
        
        pass
    @property
    def dir(self):
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

    def __init__(self, shape: str, MARTE_RSM_Shaped: "RSM_MARTE_MultiplicityElement" = None):
        self.shape = shape
        self.MARTE_RSM_Shaped = MARTE_RSM_Shaped
        
        pass
    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


    @property
    def MARTE_RSM_Shaped(self):
        return self.__MARTE_RSM_Shaped

    @MARTE_RSM_Shaped.setter
    def MARTE_RSM_Shaped(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_RSM_Shaped__MARTE_RSM_Shaped", None)
        self.__MARTE_RSM_Shaped = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RSM_MARTE_MultiplicityElement"):
                opp_val = getattr(old_value, "RSM_MARTE_MultiplicityElement", None)
                if opp_val == self:
                    setattr(old_value, "RSM_MARTE_MultiplicityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RSM_MARTE_MultiplicityElement"):
                opp_val = getattr(value, "RSM_MARTE_MultiplicityElement", None)
                setattr(value, "RSM_MARTE_MultiplicityElement", self)

class DataTypes_MARTE_Property:

    pass
class Allocate:

    pass
class MARTE_RSM_Distribute(Allocate):

    def __init__(self, patternShape: str, repetitionSpace: str, fromTiler: str, toTiler: str):
        self.patternShape = patternShape
        self.repetitionSpace = repetitionSpace
        self.fromTiler = fromTiler
        self.toTiler = toTiler
        
        pass
    @property
    def patternShape(self):
        return self.__patternShape

    @patternShape.setter
    def patternShape(self, patternShape: str):
        self.__patternShape = patternShape


    @property
    def fromTiler(self):
        return self.__fromTiler

    @fromTiler.setter
    def fromTiler(self, fromTiler: str):
        self.__fromTiler = fromTiler


    @property
    def toTiler(self):
        return self.__toTiler

    @toTiler.setter
    def toTiler(self, toTiler: str):
        self.__toTiler = toTiler


    @property
    def repetitionSpace(self):
        return self.__repetitionSpace

    @repetitionSpace.setter
    def repetitionSpace(self, repetitionSpace: str):
        self.__repetitionSpace = repetitionSpace


class LinkTopology:

    pass
class MARTE_RSM_InterRepetition(LinkTopology):

    def __init__(self, repetitionShapeDependence: str, isModulo: str):
        self.repetitionShapeDependence = repetitionShapeDependence
        self.isModulo = isModulo
        
        pass
    @property
    def repetitionShapeDependence(self):
        return self.__repetitionShapeDependence

    @repetitionShapeDependence.setter
    def repetitionShapeDependence(self, repetitionShapeDependence: str):
        self.__repetitionShapeDependence = repetitionShapeDependence


    @property
    def isModulo(self):
        return self.__isModulo

    @isModulo.setter
    def isModulo(self, isModulo: str):
        self.__isModulo = isModulo


class MARTE_RSM_Tiler(LinkTopology):

    def __init__(self, fitting: str, tiler: str, origin: str, paving: str, MARTE_RSM_Tiler: "RSM_MARTE_ConnectorEnd" = None):
        self.fitting = fitting
        self.tiler = tiler
        self.origin = origin
        self.paving = paving
        self.MARTE_RSM_Tiler = MARTE_RSM_Tiler
        
        pass
    @property
    def paving(self):
        return self.__paving

    @paving.setter
    def paving(self, paving: str):
        self.__paving = paving


    @property
    def fitting(self):
        return self.__fitting

    @fitting.setter
    def fitting(self, fitting: str):
        self.__fitting = fitting


    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, origin: str):
        self.__origin = origin


    @property
    def tiler(self):
        return self.__tiler

    @tiler.setter
    def tiler(self, tiler: str):
        self.__tiler = tiler


    @property
    def MARTE_RSM_Tiler(self):
        return self.__MARTE_RSM_Tiler

    @MARTE_RSM_Tiler.setter
    def MARTE_RSM_Tiler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_RSM_Tiler__MARTE_RSM_Tiler", None)
        self.__MARTE_RSM_Tiler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RSM_MARTE_ConnectorEnd"):
                opp_val = getattr(old_value, "RSM_MARTE_ConnectorEnd", None)
                if opp_val == self:
                    setattr(old_value, "RSM_MARTE_ConnectorEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RSM_MARTE_ConnectorEnd"):
                opp_val = getattr(value, "RSM_MARTE_ConnectorEnd", None)
                setattr(value, "RSM_MARTE_ConnectorEnd", self)

class MARTE_RSM_Reshape(LinkTopology):

    def __init__(self, patternShape: str, repetitonShape: str):
        self.patternShape = patternShape
        self.repetitonShape = repetitonShape
        
        pass
    @property
    def patternShape(self):
        return self.__patternShape

    @patternShape.setter
    def patternShape(self, patternShape: str):
        self.__patternShape = patternShape


    @property
    def repetitonShape(self):
        return self.__repetitonShape

    @repetitonShape.setter
    def repetitonShape(self, repetitonShape: str):
        self.__repetitonShape = repetitonShape


class MARTE_RSM_DefaultLink(LinkTopology):

    pass
class RSM_MARTE_Connector:

    pass
class MARTE_RSM_LinkTopology(ABC):

    pass
class GRM_ResourceUsage:

    pass
class MARTE_GQAM_GaScenario(GRM_ResourceUsage, Time_TimedProcessing):

    def __init__(self, throughput: str, respT: str, utilization: str, utilizationOnHost: str, hostDemand: str, hostDemandOps: str, interOccT: str, MARTE_GQAM_GaScenario: "GQAM_GaWorkloadEvent" = None, scenario: set["GQAM_GaStep"] = None, childScenario: set["GQAM_GaStep"] = None, MARTE_GQAM_GaScenario487: set["GQAM_GaTimedObs"] = None, MARTE_GQAM_GaScenario482: "GQAM_GaStep" = None, GRM_ResourceUsage: "MARTE_GRM_ResourceUsage" = None):
        self.throughput = throughput
        self.respT = respT
        self.utilization = utilization
        self.utilizationOnHost = utilizationOnHost
        self.hostDemand = hostDemand
        self.hostDemandOps = hostDemandOps
        self.interOccT = interOccT
        self.MARTE_GQAM_GaScenario = MARTE_GQAM_GaScenario
        self.scenario = scenario if scenario is not None else set()
        self.childScenario = childScenario if childScenario is not None else set()
        self.MARTE_GQAM_GaScenario487 = MARTE_GQAM_GaScenario487 if MARTE_GQAM_GaScenario487 is not None else set()
        self.MARTE_GQAM_GaScenario482 = MARTE_GQAM_GaScenario482
        
        pass
    @property
    def respT(self):
        return self.__respT

    @respT.setter
    def respT(self, respT: str):
        self.__respT = respT


    @property
    def throughput(self):
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput


    @property
    def utilization(self):
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization


    @property
    def utilizationOnHost(self):
        return self.__utilizationOnHost

    @utilizationOnHost.setter
    def utilizationOnHost(self, utilizationOnHost: str):
        self.__utilizationOnHost = utilizationOnHost


    @property
    def hostDemandOps(self):
        return self.__hostDemandOps

    @hostDemandOps.setter
    def hostDemandOps(self, hostDemandOps: str):
        self.__hostDemandOps = hostDemandOps


    @property
    def interOccT(self):
        return self.__interOccT

    @interOccT.setter
    def interOccT(self, interOccT: str):
        self.__interOccT = interOccT


    @property
    def hostDemand(self):
        return self.__hostDemand

    @hostDemand.setter
    def hostDemand(self, hostDemand: str):
        self.__hostDemand = hostDemand


    @property
    def scenario(self):
        return self.__scenario

    @scenario.setter
    def scenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaScenario__scenario", None)
        self.__scenario = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GaStep"):
                    opp_val = getattr(item, "GaStep", None)
                    
                    if opp_val == self:
                        setattr(item, "GaStep", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GaStep"):
                    opp_val = getattr(item, "GaStep", None)
                    
                    setattr(item, "GaStep", self)
                    

    @property
    def MARTE_GQAM_GaScenario487(self):
        return self.__MARTE_GQAM_GaScenario487

    @MARTE_GQAM_GaScenario487.setter
    def MARTE_GQAM_GaScenario487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaScenario__MARTE_GQAM_GaScenario487", None)
        self.__MARTE_GQAM_GaScenario487 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_GaTimedObs"):
                    opp_val = getattr(item, "GQAM_GaTimedObs", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_GaTimedObs", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_GaTimedObs"):
                    opp_val = getattr(item, "GQAM_GaTimedObs", None)
                    
                    setattr(item, "GQAM_GaTimedObs", self)
                    

    @property
    def MARTE_GQAM_GaScenario482(self):
        return self.__MARTE_GQAM_GaScenario482

    @MARTE_GQAM_GaScenario482.setter
    def MARTE_GQAM_GaScenario482(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaScenario__MARTE_GQAM_GaScenario482", None)
        self.__MARTE_GQAM_GaScenario482 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_GaStep"):
                opp_val = getattr(old_value, "GQAM_GaStep", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_GaStep", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_GaStep"):
                opp_val = getattr(value, "GQAM_GaStep", None)
                setattr(value, "GQAM_GaStep", self)

    @property
    def MARTE_GQAM_GaScenario(self):
        return self.__MARTE_GQAM_GaScenario

    @MARTE_GQAM_GaScenario.setter
    def MARTE_GQAM_GaScenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaScenario__MARTE_GQAM_GaScenario", None)
        self.__MARTE_GQAM_GaScenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_GaWorkloadEvent"):
                opp_val = getattr(old_value, "GQAM_GaWorkloadEvent", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_GaWorkloadEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_GaWorkloadEvent"):
                opp_val = getattr(value, "GQAM_GaWorkloadEvent", None)
                setattr(value, "GQAM_GaWorkloadEvent", self)

    @property
    def childScenario(self):
        return self.__childScenario

    @childScenario.setter
    def childScenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaScenario__childScenario", None)
        self.__childScenario = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GaStep485"):
                    opp_val = getattr(item, "GaStep485", None)
                    
                    if opp_val == self:
                        setattr(item, "GaStep485", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GaStep485"):
                    opp_val = getattr(item, "GaStep485", None)
                    
                    setattr(item, "GaStep485", self)
                    

class GRM_MARTE_NamedElement:

    pass
class RSM_MARTE_ConnectorEnd:

    pass
class GrService:

    pass
class MARTE_GRM_Acquire(GrService):

    def __init__(self, isBlocking: str):
        self.isBlocking = isBlocking
        
        pass
    @property
    def isBlocking(self):
        return self.__isBlocking

    @isBlocking.setter
    def isBlocking(self, isBlocking: str):
        self.__isBlocking = isBlocking


class MARTE_GRM_Release(GrService):

    pass
class GRM_MARTE_CollaborationUse:

    pass
class GRM_MARTE_Collaboration:

    pass
class GRM_MARTE_Behavior:

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

    def __init__(self, duration: str, isPeriodic: str):
        self.duration = duration
        self.isPeriodic = isPeriodic
        
        pass
    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration


    @property
    def isPeriodic(self):
        return self.__isPeriodic

    @isPeriodic.setter
    def isPeriodic(self, isPeriodic: str):
        self.__isPeriodic = isPeriodic


class MARTE_GRM_ClockResource(TimingResource):

    pass
class MARTE_GRM_ResourceUsage:

    def __init__(self, execTime: str, allocatedMemory: str, usedMemory: str, powerPeak: str, energy: str, msgSize: str, MARTE_GRM_ResourceUsage: "GRM_MARTE_NamedElement" = None, MARTE_GRM_ResourceUsage138: set["GRM_ResourceUsage"] = None, MARTE_GRM_ResourceUsage140: set["GRM_Resource"] = None):
        self.execTime = execTime
        self.allocatedMemory = allocatedMemory
        self.usedMemory = usedMemory
        self.powerPeak = powerPeak
        self.energy = energy
        self.msgSize = msgSize
        self.MARTE_GRM_ResourceUsage = MARTE_GRM_ResourceUsage
        self.MARTE_GRM_ResourceUsage138 = MARTE_GRM_ResourceUsage138 if MARTE_GRM_ResourceUsage138 is not None else set()
        self.MARTE_GRM_ResourceUsage140 = MARTE_GRM_ResourceUsage140 if MARTE_GRM_ResourceUsage140 is not None else set()
        
        pass
    @property
    def allocatedMemory(self):
        return self.__allocatedMemory

    @allocatedMemory.setter
    def allocatedMemory(self, allocatedMemory: str):
        self.__allocatedMemory = allocatedMemory


    @property
    def execTime(self):
        return self.__execTime

    @execTime.setter
    def execTime(self, execTime: str):
        self.__execTime = execTime


    @property
    def usedMemory(self):
        return self.__usedMemory

    @usedMemory.setter
    def usedMemory(self, usedMemory: str):
        self.__usedMemory = usedMemory


    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, energy: str):
        self.__energy = energy


    @property
    def msgSize(self):
        return self.__msgSize

    @msgSize.setter
    def msgSize(self, msgSize: str):
        self.__msgSize = msgSize


    @property
    def powerPeak(self):
        return self.__powerPeak

    @powerPeak.setter
    def powerPeak(self, powerPeak: str):
        self.__powerPeak = powerPeak


    @property
    def MARTE_GRM_ResourceUsage(self):
        return self.__MARTE_GRM_ResourceUsage

    @MARTE_GRM_ResourceUsage.setter
    def MARTE_GRM_ResourceUsage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_ResourceUsage__MARTE_GRM_ResourceUsage", None)
        self.__MARTE_GRM_ResourceUsage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_MARTE_NamedElement"):
                opp_val = getattr(old_value, "GRM_MARTE_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "GRM_MARTE_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_MARTE_NamedElement"):
                opp_val = getattr(value, "GRM_MARTE_NamedElement", None)
                setattr(value, "GRM_MARTE_NamedElement", self)

    @property
    def MARTE_GRM_ResourceUsage138(self):
        return self.__MARTE_GRM_ResourceUsage138

    @MARTE_GRM_ResourceUsage138.setter
    def MARTE_GRM_ResourceUsage138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_ResourceUsage__MARTE_GRM_ResourceUsage138", None)
        self.__MARTE_GRM_ResourceUsage138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GRM_ResourceUsage"):
                    opp_val = getattr(item, "GRM_ResourceUsage", None)
                    
                    if opp_val == self:
                        setattr(item, "GRM_ResourceUsage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GRM_ResourceUsage"):
                    opp_val = getattr(item, "GRM_ResourceUsage", None)
                    
                    setattr(item, "GRM_ResourceUsage", self)
                    

    @property
    def MARTE_GRM_ResourceUsage140(self):
        return self.__MARTE_GRM_ResourceUsage140

    @MARTE_GRM_ResourceUsage140.setter
    def MARTE_GRM_ResourceUsage140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_ResourceUsage__MARTE_GRM_ResourceUsage140", None)
        self.__MARTE_GRM_ResourceUsage140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GRM_Resource141"):
                    opp_val = getattr(item, "GRM_Resource141", None)
                    
                    if opp_val == self:
                        setattr(item, "GRM_Resource141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GRM_Resource141"):
                    opp_val = getattr(item, "GRM_Resource141", None)
                    
                    setattr(item, "GRM_Resource141", self)
                    

class GRM_MARTE_Connector:

    pass
class Scheduler:

    pass
class MARTE_GRM_SecondaryScheduler(Scheduler):

    pass
class GRM_SecondaryScheduler:

    pass
class ProcessingResource:

    pass
class MARTE_GRM_DeviceResource(ProcessingResource):

    pass
class MARTE_GRM_CommunicationMedia(ProcessingResource):

    def __init__(self, transmMode: str, blockT: str, elementSize: str, packetT: str, capacity: str, MARTE_GRM_CommunicationMedia: "GRM_MARTE_Connector" = None):
        self.transmMode = transmMode
        self.blockT = blockT
        self.elementSize = elementSize
        self.packetT = packetT
        self.capacity = capacity
        self.MARTE_GRM_CommunicationMedia = MARTE_GRM_CommunicationMedia
        
        pass
    @property
    def transmMode(self):
        return self.__transmMode

    @transmMode.setter
    def transmMode(self, transmMode: str):
        self.__transmMode = transmMode


    @property
    def elementSize(self):
        return self.__elementSize

    @elementSize.setter
    def elementSize(self, elementSize: str):
        self.__elementSize = elementSize


    @property
    def packetT(self):
        return self.__packetT

    @packetT.setter
    def packetT(self, packetT: str):
        self.__packetT = packetT


    @property
    def blockT(self):
        return self.__blockT

    @blockT.setter
    def blockT(self, blockT: str):
        self.__blockT = blockT


    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity


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
            if hasattr(old_value, "GRM_MARTE_Connector"):
                opp_val = getattr(old_value, "GRM_MARTE_Connector", None)
                if opp_val == self:
                    setattr(old_value, "GRM_MARTE_Connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_MARTE_Connector"):
                opp_val = getattr(value, "GRM_MARTE_Connector", None)
                setattr(value, "GRM_MARTE_Connector", self)

class MARTE_GRM_ComputingResource(ProcessingResource):

    pass
class GRM_Scheduler:

    pass
class GRM_SchedulableResource:

    pass
class GRM_MutualExclusionResource:

    pass
class MARTE_SW_Interaction_SwMutualExclusionResource(GRM_MutualExclusionResource, SW_Interaction_SwSynchronizationResource):

    def __init__(self, mechanism: str, concurrentAccessProtocol: str, MARTE_SW_Interaction_SwMutualExclusionResource: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_SwMutualExclusionResource419: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_SwMutualExclusionResource422: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MutualExclusionResource: "MARTE_GRM_Scheduler" = None):
        self.mechanism = mechanism
        self.concurrentAccessProtocol = concurrentAccessProtocol
        self.MARTE_SW_Interaction_SwMutualExclusionResource = MARTE_SW_Interaction_SwMutualExclusionResource if MARTE_SW_Interaction_SwMutualExclusionResource is not None else set()
        self.MARTE_SW_Interaction_SwMutualExclusionResource419 = MARTE_SW_Interaction_SwMutualExclusionResource419 if MARTE_SW_Interaction_SwMutualExclusionResource419 is not None else set()
        self.MARTE_SW_Interaction_SwMutualExclusionResource422 = MARTE_SW_Interaction_SwMutualExclusionResource422 if MARTE_SW_Interaction_SwMutualExclusionResource422 is not None else set()
        
        pass
    @property
    def concurrentAccessProtocol(self):
        return self.__concurrentAccessProtocol

    @concurrentAccessProtocol.setter
    def concurrentAccessProtocol(self, concurrentAccessProtocol: str):
        self.__concurrentAccessProtocol = concurrentAccessProtocol


    @property
    def mechanism(self):
        return self.__mechanism

    @mechanism.setter
    def mechanism(self, mechanism: str):
        self.__mechanism = mechanism


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
                if hasattr(item, "SW_Interaction_MARTE_TypedElement417"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement417", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement417", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement417"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement417", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement417", self)
                    

    @property
    def MARTE_SW_Interaction_SwMutualExclusionResource419(self):
        return self.__MARTE_SW_Interaction_SwMutualExclusionResource419

    @MARTE_SW_Interaction_SwMutualExclusionResource419.setter
    def MARTE_SW_Interaction_SwMutualExclusionResource419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_SwMutualExclusionResource__MARTE_SW_Interaction_SwMutualExclusionResource419", None)
        self.__MARTE_SW_Interaction_SwMutualExclusionResource419 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature420"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature420", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature420", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature420"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature420", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature420", self)
                    

    @property
    def MARTE_SW_Interaction_SwMutualExclusionResource422(self):
        return self.__MARTE_SW_Interaction_SwMutualExclusionResource422

    @MARTE_SW_Interaction_SwMutualExclusionResource422.setter
    def MARTE_SW_Interaction_SwMutualExclusionResource422(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_SwMutualExclusionResource__MARTE_SW_Interaction_SwMutualExclusionResource422", None)
        self.__MARTE_SW_Interaction_SwMutualExclusionResource422 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature423"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature423", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature423", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature423"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature423", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature423", self)
                    

class GRM_ComputingResource:

    pass
class MARTE_GQAM_GaExecHost(GRM_Scheduler, GRM_ComputingResource):

    def __init__(self, commTxOvh: str, commRcvOvh: str, cntxtSwT: str, clockOvh: str, schedPriRange: str, memSize: str, utilization: str, throughput: str, GRM_ComputingResource: "MARTE_GRM_Scheduler" = None, GRM_Scheduler: "MARTE_GRM_ProcessingResource" = None, Scheduler121: "MARTE_GRM_SchedulableResource" = None, Scheduler: "MARTE_GRM_MutualExclusionResource" = None):
        self.commTxOvh = commTxOvh
        self.commRcvOvh = commRcvOvh
        self.cntxtSwT = cntxtSwT
        self.clockOvh = clockOvh
        self.schedPriRange = schedPriRange
        self.memSize = memSize
        self.utilization = utilization
        self.throughput = throughput
        
        pass
    @property
    def commRcvOvh(self):
        return self.__commRcvOvh

    @commRcvOvh.setter
    def commRcvOvh(self, commRcvOvh: str):
        self.__commRcvOvh = commRcvOvh


    @property
    def commTxOvh(self):
        return self.__commTxOvh

    @commTxOvh.setter
    def commTxOvh(self, commTxOvh: str):
        self.__commTxOvh = commTxOvh


    @property
    def schedPriRange(self):
        return self.__schedPriRange

    @schedPriRange.setter
    def schedPriRange(self, schedPriRange: str):
        self.__schedPriRange = schedPriRange


    @property
    def utilization(self):
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization


    @property
    def clockOvh(self):
        return self.__clockOvh

    @clockOvh.setter
    def clockOvh(self, clockOvh: str):
        self.__clockOvh = clockOvh


    @property
    def cntxtSwT(self):
        return self.__cntxtSwT

    @cntxtSwT.setter
    def cntxtSwT(self, cntxtSwT: str):
        self.__cntxtSwT = cntxtSwT


    @property
    def memSize(self):
        return self.__memSize

    @memSize.setter
    def memSize(self, memSize: str):
        self.__memSize = memSize


    @property
    def throughput(self):
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput


class GRM_ProcessingResource:

    pass
class Resource:

    pass
class MARTE_GRM_ProcessingResource(Resource):

    def __init__(self, speedFactor: str, MARTE_GRM_ProcessingResource: "GRM_Scheduler" = None):
        self.speedFactor = speedFactor
        self.MARTE_GRM_ProcessingResource = MARTE_GRM_ProcessingResource
        
        pass
    @property
    def speedFactor(self):
        return self.__speedFactor

    @speedFactor.setter
    def speedFactor(self, speedFactor: str):
        self.__speedFactor = speedFactor


    @property
    def MARTE_GRM_ProcessingResource(self):
        return self.__MARTE_GRM_ProcessingResource

    @MARTE_GRM_ProcessingResource.setter
    def MARTE_GRM_ProcessingResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_ProcessingResource__MARTE_GRM_ProcessingResource", None)
        self.__MARTE_GRM_ProcessingResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_Scheduler"):
                opp_val = getattr(old_value, "GRM_Scheduler", None)
                if opp_val == self:
                    setattr(old_value, "GRM_Scheduler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_Scheduler"):
                opp_val = getattr(value, "GRM_Scheduler", None)
                setattr(value, "GRM_Scheduler", self)

class MARTE_GRM_CommunicationEndPoint(Resource):

    def __init__(self, packetSize: str):
        self.packetSize = packetSize
        
        pass
    @property
    def packetSize(self):
        return self.__packetSize

    @packetSize.setter
    def packetSize(self, packetSize: str):
        self.__packetSize = packetSize


class MARTE_GRM_SchedulableResource(Resource):

    def __init__(self, schedParams: str, virtualProcessingUnits: "GRM_SecondaryScheduler" = None, schedulableResources: "GRM_Scheduler" = None):
        self.schedParams = schedParams
        self.virtualProcessingUnits = virtualProcessingUnits
        self.schedulableResources = schedulableResources
        
        pass
    @property
    def schedParams(self):
        return self.__schedParams

    @schedParams.setter
    def schedParams(self, schedParams: str):
        self.__schedParams = schedParams


    @property
    def schedulableResources(self):
        return self.__schedulableResources

    @schedulableResources.setter
    def schedulableResources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_SchedulableResource__schedulableResources", None)
        self.__schedulableResources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Scheduler121"):
                opp_val = getattr(old_value, "Scheduler121", None)
                if opp_val == self:
                    setattr(old_value, "Scheduler121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Scheduler121"):
                opp_val = getattr(value, "Scheduler121", None)
                setattr(value, "Scheduler121", self)

    @property
    def virtualProcessingUnits(self):
        return self.__virtualProcessingUnits

    @virtualProcessingUnits.setter
    def virtualProcessingUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_SchedulableResource__virtualProcessingUnits", None)
        self.__virtualProcessingUnits = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecondaryScheduler"):
                opp_val = getattr(old_value, "SecondaryScheduler", None)
                if opp_val == self:
                    setattr(old_value, "SecondaryScheduler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecondaryScheduler"):
                opp_val = getattr(value, "SecondaryScheduler", None)
                setattr(value, "SecondaryScheduler", self)

class MARTE_GRM_SynchronizationResource(Resource):

    pass
class MARTE_GRM_MutualExclusionResource(Resource):

    def __init__(self, protectKind: str, ceiling: str, otherProtectProtocol: str, protectedSharedResources: "GRM_Scheduler" = None):
        self.protectKind = protectKind
        self.ceiling = ceiling
        self.otherProtectProtocol = otherProtectProtocol
        self.protectedSharedResources = protectedSharedResources
        
        pass
    @property
    def ceiling(self):
        return self.__ceiling

    @ceiling.setter
    def ceiling(self, ceiling: str):
        self.__ceiling = ceiling


    @property
    def protectKind(self):
        return self.__protectKind

    @protectKind.setter
    def protectKind(self, protectKind: str):
        self.__protectKind = protectKind


    @property
    def otherProtectProtocol(self):
        return self.__otherProtectProtocol

    @otherProtectProtocol.setter
    def otherProtectProtocol(self, otherProtectProtocol: str):
        self.__otherProtectProtocol = otherProtectProtocol


    @property
    def protectedSharedResources(self):
        return self.__protectedSharedResources

    @protectedSharedResources.setter
    def protectedSharedResources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_MutualExclusionResource__protectedSharedResources", None)
        self.__protectedSharedResources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Scheduler"):
                opp_val = getattr(old_value, "Scheduler", None)
                if opp_val == self:
                    setattr(old_value, "Scheduler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Scheduler"):
                opp_val = getattr(value, "Scheduler", None)
                setattr(value, "Scheduler", self)

class MARTE_GRM_ConcurrencyResource(Resource):

    pass
class MARTE_GRM_Scheduler(Resource):

    def __init__(self, isPreemptible: str, schedPolicy: str, otherSchedPolicy: str, schedule: str, MARTE_GRM_Scheduler: set["GRM_ProcessingResource"] = None, MARTE_GRM_Scheduler114: "GRM_ComputingResource" = None, scheduler: set["GRM_MutualExclusionResource"] = None, host: set["GRM_SchedulableResource"] = None):
        self.isPreemptible = isPreemptible
        self.schedPolicy = schedPolicy
        self.otherSchedPolicy = otherSchedPolicy
        self.schedule = schedule
        self.MARTE_GRM_Scheduler = MARTE_GRM_Scheduler if MARTE_GRM_Scheduler is not None else set()
        self.MARTE_GRM_Scheduler114 = MARTE_GRM_Scheduler114
        self.scheduler = scheduler if scheduler is not None else set()
        self.host = host if host is not None else set()
        
        pass
    @property
    def schedPolicy(self):
        return self.__schedPolicy

    @schedPolicy.setter
    def schedPolicy(self, schedPolicy: str):
        self.__schedPolicy = schedPolicy


    @property
    def otherSchedPolicy(self):
        return self.__otherSchedPolicy

    @otherSchedPolicy.setter
    def otherSchedPolicy(self, otherSchedPolicy: str):
        self.__otherSchedPolicy = otherSchedPolicy


    @property
    def isPreemptible(self):
        return self.__isPreemptible

    @isPreemptible.setter
    def isPreemptible(self, isPreemptible: str):
        self.__isPreemptible = isPreemptible


    @property
    def schedule(self):
        return self.__schedule

    @schedule.setter
    def schedule(self, schedule: str):
        self.__schedule = schedule


    @property
    def MARTE_GRM_Scheduler114(self):
        return self.__MARTE_GRM_Scheduler114

    @MARTE_GRM_Scheduler114.setter
    def MARTE_GRM_Scheduler114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Scheduler__MARTE_GRM_Scheduler114", None)
        self.__MARTE_GRM_Scheduler114 = value
        
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
    def scheduler(self):
        return self.__scheduler

    @scheduler.setter
    def scheduler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Scheduler__scheduler", None)
        self.__scheduler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MutualExclusionResource"):
                    opp_val = getattr(item, "MutualExclusionResource", None)
                    
                    if opp_val == self:
                        setattr(item, "MutualExclusionResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MutualExclusionResource"):
                    opp_val = getattr(item, "MutualExclusionResource", None)
                    
                    setattr(item, "MutualExclusionResource", self)
                    

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Scheduler__host", None)
        self.__host = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SchedulableResource"):
                    opp_val = getattr(item, "SchedulableResource", None)
                    
                    if opp_val == self:
                        setattr(item, "SchedulableResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SchedulableResource"):
                    opp_val = getattr(item, "SchedulableResource", None)
                    
                    setattr(item, "SchedulableResource", self)
                    

    @property
    def MARTE_GRM_Scheduler(self):
        return self.__MARTE_GRM_Scheduler

    @MARTE_GRM_Scheduler.setter
    def MARTE_GRM_Scheduler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Scheduler__MARTE_GRM_Scheduler", None)
        self.__MARTE_GRM_Scheduler = value if value is not None else set()
        
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
                    

class MARTE_PAM_PaLogicalResource(Resource):

    def __init__(self, utilization: str, throughput: str, poolSize: str):
        self.utilization = utilization
        self.throughput = throughput
        self.poolSize = poolSize
        
        pass
    @property
    def utilization(self):
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization


    @property
    def poolSize(self):
        return self.__poolSize

    @poolSize.setter
    def poolSize(self, poolSize: str):
        self.__poolSize = poolSize


    @property
    def throughput(self):
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput


class MARTE_GRM_TimingResource(Resource):

    pass
class MARTE_GRM_StorageResource(Resource):

    def __init__(self, elementSize: str):
        self.elementSize = elementSize
        
        pass
    @property
    def elementSize(self):
        return self.__elementSize

    @elementSize.setter
    def elementSize(self, elementSize: str):
        self.__elementSize = elementSize


class GRM_MARTE_Lifeline:

    pass
class GRM_MARTE_Classifier:

    pass
class GRM_MARTE_InstanceSpecification:

    pass
class GRM_MARTE_Property:

    pass
class MARTE_GRM_Resource:

    def __init__(self, resMult: str, isProtected: str, isActive: str, MARTE_GRM_Resource: "GRM_MARTE_Property" = None, MARTE_GRM_Resource105: "GRM_MARTE_InstanceSpecification" = None, MARTE_GRM_Resource107: "GRM_MARTE_Classifier" = None, MARTE_GRM_Resource109: "GRM_MARTE_Lifeline" = None, MARTE_GRM_Resource111: "GRM_MARTE_ConnectableElement" = None):
        self.resMult = resMult
        self.isProtected = isProtected
        self.isActive = isActive
        self.MARTE_GRM_Resource = MARTE_GRM_Resource
        self.MARTE_GRM_Resource105 = MARTE_GRM_Resource105
        self.MARTE_GRM_Resource107 = MARTE_GRM_Resource107
        self.MARTE_GRM_Resource109 = MARTE_GRM_Resource109
        self.MARTE_GRM_Resource111 = MARTE_GRM_Resource111
        
        pass
    @property
    def resMult(self):
        return self.__resMult

    @resMult.setter
    def resMult(self, resMult: str):
        self.__resMult = resMult


    @property
    def isProtected(self):
        return self.__isProtected

    @isProtected.setter
    def isProtected(self, isProtected: str):
        self.__isProtected = isProtected


    @property
    def isActive(self):
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive


    @property
    def MARTE_GRM_Resource107(self):
        return self.__MARTE_GRM_Resource107

    @MARTE_GRM_Resource107.setter
    def MARTE_GRM_Resource107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Resource__MARTE_GRM_Resource107", None)
        self.__MARTE_GRM_Resource107 = value
        
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
    def MARTE_GRM_Resource105(self):
        return self.__MARTE_GRM_Resource105

    @MARTE_GRM_Resource105.setter
    def MARTE_GRM_Resource105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Resource__MARTE_GRM_Resource105", None)
        self.__MARTE_GRM_Resource105 = value
        
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
    def MARTE_GRM_Resource111(self):
        return self.__MARTE_GRM_Resource111

    @MARTE_GRM_Resource111.setter
    def MARTE_GRM_Resource111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Resource__MARTE_GRM_Resource111", None)
        self.__MARTE_GRM_Resource111 = value
        
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
    def MARTE_GRM_Resource109(self):
        return self.__MARTE_GRM_Resource109

    @MARTE_GRM_Resource109.setter
    def MARTE_GRM_Resource109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Resource__MARTE_GRM_Resource109", None)
        self.__MARTE_GRM_Resource109 = value
        
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
            if hasattr(old_value, "GRM_MARTE_Property"):
                opp_val = getattr(old_value, "GRM_MARTE_Property", None)
                if opp_val == self:
                    setattr(old_value, "GRM_MARTE_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_MARTE_Property"):
                opp_val = getattr(value, "GRM_MARTE_Property", None)
                setattr(value, "GRM_MARTE_Property", self)

class Time_MARTE_Message:

    pass
class Time_MARTE_Behavior:

    pass
class GRM_MARTE_ConnectableElement:

    pass
class Time_MARTE_Action:

    pass
class Time_MARTE_TimeEvent:

    pass
class Time_MARTE_DurationObservation:

    pass
class Time_MARTE_TimeObservation:

    pass
class Time_TimedElement:

    pass
class Time_MARTE_ValueSpecification:

    pass
class TimedElement:

    pass
class MARTE_Time_TimedProcessing(TimedElement):

    pass
class MARTE_Time_TimedDurationObservation(TimedElement):

    def __init__(self, obsKind: str, MARTE_Time_TimedDurationObservation: "Time_MARTE_DurationObservation" = None):
        self.obsKind = obsKind
        self.MARTE_Time_TimedDurationObservation = MARTE_Time_TimedDurationObservation
        
        pass
    @property
    def obsKind(self):
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

class MARTE_Time_TimedInstantObservation(TimedElement):

    def __init__(self, obsKind: str, MARTE_Time_TimedInstantObservation: "Time_MARTE_TimeObservation" = None):
        self.obsKind = obsKind
        self.MARTE_Time_TimedInstantObservation = MARTE_Time_TimedInstantObservation
        
        pass
    @property
    def obsKind(self):
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

class MARTE_Time_TimedEvent(TimedElement):

    def __init__(self, repetition: str, MARTE_Time_TimedEvent: "Time_MARTE_TimeEvent" = None, MARTE_Time_TimedEvent87: "Time_MARTE_ValueSpecification" = None):
        self.repetition = repetition
        self.MARTE_Time_TimedEvent = MARTE_Time_TimedEvent
        self.MARTE_Time_TimedEvent87 = MARTE_Time_TimedEvent87
        
        pass
    @property
    def repetition(self):
        return self.__repetition

    @repetition.setter
    def repetition(self, repetition: str):
        self.__repetition = repetition


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

    @property
    def MARTE_Time_TimedEvent87(self):
        return self.__MARTE_Time_TimedEvent87

    @MARTE_Time_TimedEvent87.setter
    def MARTE_Time_TimedEvent87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_TimedEvent__MARTE_Time_TimedEvent87", None)
        self.__MARTE_Time_TimedEvent87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_ValueSpecification88"):
                opp_val = getattr(old_value, "Time_MARTE_ValueSpecification88", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_ValueSpecification88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_ValueSpecification88"):
                opp_val = getattr(value, "Time_MARTE_ValueSpecification88", None)
                setattr(value, "Time_MARTE_ValueSpecification88", self)

class MARTE_Time_TimedValueSpecification(TimedElement):

    def __init__(self, interpretation: str, MARTE_Time_TimedValueSpecification: "Time_MARTE_ValueSpecification" = None):
        self.interpretation = interpretation
        self.MARTE_Time_TimedValueSpecification = MARTE_Time_TimedValueSpecification
        
        pass
    @property
    def interpretation(self):
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
class MARTE_Time_TimedElement(ABC):

    pass
class Time_MARTE_Class:

    pass
class Time_MARTE_Operation:

    pass
class MARTE_Time_ClockType:

    def __init__(self, nature: str, isLogical: str, MARTE_Time_ClockType: "Time_MARTE_Enumeration" = None, MARTE_Time_ClockType63: "Time_MARTE_Property" = None, MARTE_Time_ClockType66: "Time_MARTE_Property" = None, MARTE_Time_ClockType69: "Time_MARTE_Property" = None, MARTE_Time_ClockType72: "Time_MARTE_Operation" = None, MARTE_Time_ClockType74: "Time_MARTE_Operation" = None, MARTE_Time_ClockType77: "Time_MARTE_Operation" = None, MARTE_Time_ClockType80: "Time_MARTE_Class" = None):
        self.nature = nature
        self.isLogical = isLogical
        self.MARTE_Time_ClockType = MARTE_Time_ClockType
        self.MARTE_Time_ClockType63 = MARTE_Time_ClockType63
        self.MARTE_Time_ClockType66 = MARTE_Time_ClockType66
        self.MARTE_Time_ClockType69 = MARTE_Time_ClockType69
        self.MARTE_Time_ClockType72 = MARTE_Time_ClockType72
        self.MARTE_Time_ClockType74 = MARTE_Time_ClockType74
        self.MARTE_Time_ClockType77 = MARTE_Time_ClockType77
        self.MARTE_Time_ClockType80 = MARTE_Time_ClockType80
        
        pass
    @property
    def isLogical(self):
        return self.__isLogical

    @isLogical.setter
    def isLogical(self, isLogical: str):
        self.__isLogical = isLogical


    @property
    def nature(self):
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature


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
    def MARTE_Time_ClockType72(self):
        return self.__MARTE_Time_ClockType72

    @MARTE_Time_ClockType72.setter
    def MARTE_Time_ClockType72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType72", None)
        self.__MARTE_Time_ClockType72 = value
        
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

    @property
    def MARTE_Time_ClockType63(self):
        return self.__MARTE_Time_ClockType63

    @MARTE_Time_ClockType63.setter
    def MARTE_Time_ClockType63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType63", None)
        self.__MARTE_Time_ClockType63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Property64"):
                opp_val = getattr(old_value, "Time_MARTE_Property64", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Property64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Property64"):
                opp_val = getattr(value, "Time_MARTE_Property64", None)
                setattr(value, "Time_MARTE_Property64", self)

    @property
    def MARTE_Time_ClockType77(self):
        return self.__MARTE_Time_ClockType77

    @MARTE_Time_ClockType77.setter
    def MARTE_Time_ClockType77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType77", None)
        self.__MARTE_Time_ClockType77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Operation78"):
                opp_val = getattr(old_value, "Time_MARTE_Operation78", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Operation78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Operation78"):
                opp_val = getattr(value, "Time_MARTE_Operation78", None)
                setattr(value, "Time_MARTE_Operation78", self)

    @property
    def MARTE_Time_ClockType66(self):
        return self.__MARTE_Time_ClockType66

    @MARTE_Time_ClockType66.setter
    def MARTE_Time_ClockType66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType66", None)
        self.__MARTE_Time_ClockType66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Property67"):
                opp_val = getattr(old_value, "Time_MARTE_Property67", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Property67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Property67"):
                opp_val = getattr(value, "Time_MARTE_Property67", None)
                setattr(value, "Time_MARTE_Property67", self)

    @property
    def MARTE_Time_ClockType69(self):
        return self.__MARTE_Time_ClockType69

    @MARTE_Time_ClockType69.setter
    def MARTE_Time_ClockType69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType69", None)
        self.__MARTE_Time_ClockType69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Property70"):
                opp_val = getattr(old_value, "Time_MARTE_Property70", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Property70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Property70"):
                opp_val = getattr(value, "Time_MARTE_Property70", None)
                setattr(value, "Time_MARTE_Property70", self)

    @property
    def MARTE_Time_ClockType74(self):
        return self.__MARTE_Time_ClockType74

    @MARTE_Time_ClockType74.setter
    def MARTE_Time_ClockType74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType74", None)
        self.__MARTE_Time_ClockType74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Operation75"):
                opp_val = getattr(old_value, "Time_MARTE_Operation75", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Operation75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Operation75"):
                opp_val = getattr(value, "Time_MARTE_Operation75", None)
                setattr(value, "Time_MARTE_Operation75", self)

    @property
    def MARTE_Time_ClockType80(self):
        return self.__MARTE_Time_ClockType80

    @MARTE_Time_ClockType80.setter
    def MARTE_Time_ClockType80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_ClockType__MARTE_Time_ClockType80", None)
        self.__MARTE_Time_ClockType80 = value
        
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

class Time_MARTE_Event:

    pass
class Time_MARTE_Property:

    pass
class Time_ClockType:

    pass
class Time_MARTE_InstanceSpecification:

    pass
class MARTE_Time_Clock:

    def __init__(self, standard: str, MARTE_Time_Clock: "Time_MARTE_InstanceSpecification" = None, MARTE_Time_Clock53: "Time_ClockType" = None, MARTE_Time_Clock55: "NFPs_Unit" = None, MARTE_Time_Clock58: "Time_MARTE_Property" = None, MARTE_Time_Clock60: "Time_MARTE_Event" = None):
        self.standard = standard
        self.MARTE_Time_Clock = MARTE_Time_Clock
        self.MARTE_Time_Clock53 = MARTE_Time_Clock53
        self.MARTE_Time_Clock55 = MARTE_Time_Clock55
        self.MARTE_Time_Clock58 = MARTE_Time_Clock58
        self.MARTE_Time_Clock60 = MARTE_Time_Clock60
        
        pass
    @property
    def standard(self):
        return self.__standard

    @standard.setter
    def standard(self, standard: str):
        self.__standard = standard


    @property
    def MARTE_Time_Clock60(self):
        return self.__MARTE_Time_Clock60

    @MARTE_Time_Clock60.setter
    def MARTE_Time_Clock60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Time_Clock__MARTE_Time_Clock60", None)
        self.__MARTE_Time_Clock60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_MARTE_Event"):
                opp_val = getattr(old_value, "Time_MARTE_Event", None)
                if opp_val == self:
                    setattr(old_value, "Time_MARTE_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_MARTE_Event"):
                opp_val = getattr(value, "Time_MARTE_Event", None)
                setattr(value, "Time_MARTE_Event", self)

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

class Time_MARTE_Namespace:

    pass
class MARTE_Time_TimedDomain:

    pass
class Alloc_MARTE_Abstraction:

    pass
class Time_MARTE_Enumeration:

    pass
class Alloc_MARTE_Comment:

    pass
class Alloc_MARTE_Element:

    pass
class MARTE_Alloc_Assign:

    def __init__(self, kind: str, nature: str, MARTE_Alloc_Assign: set["NFPs_NfpConstraint"] = None, MARTE_Alloc_Assign40: set["Alloc_MARTE_Element"] = None, MARTE_Alloc_Assign42: set["Alloc_MARTE_Element"] = None, MARTE_Alloc_Assign45: "Alloc_MARTE_Comment" = None):
        self.kind = kind
        self.nature = nature
        self.MARTE_Alloc_Assign = MARTE_Alloc_Assign if MARTE_Alloc_Assign is not None else set()
        self.MARTE_Alloc_Assign40 = MARTE_Alloc_Assign40 if MARTE_Alloc_Assign40 is not None else set()
        self.MARTE_Alloc_Assign42 = MARTE_Alloc_Assign42 if MARTE_Alloc_Assign42 is not None else set()
        self.MARTE_Alloc_Assign45 = MARTE_Alloc_Assign45
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def nature(self):
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature


    @property
    def MARTE_Alloc_Assign45(self):
        return self.__MARTE_Alloc_Assign45

    @MARTE_Alloc_Assign45.setter
    def MARTE_Alloc_Assign45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Alloc_Assign__MARTE_Alloc_Assign45", None)
        self.__MARTE_Alloc_Assign45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Alloc_MARTE_Comment"):
                opp_val = getattr(old_value, "Alloc_MARTE_Comment", None)
                if opp_val == self:
                    setattr(old_value, "Alloc_MARTE_Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Alloc_MARTE_Comment"):
                opp_val = getattr(value, "Alloc_MARTE_Comment", None)
                setattr(value, "Alloc_MARTE_Comment", self)

    @property
    def MARTE_Alloc_Assign42(self):
        return self.__MARTE_Alloc_Assign42

    @MARTE_Alloc_Assign42.setter
    def MARTE_Alloc_Assign42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Alloc_Assign__MARTE_Alloc_Assign42", None)
        self.__MARTE_Alloc_Assign42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Alloc_MARTE_Element43"):
                    opp_val = getattr(item, "Alloc_MARTE_Element43", None)
                    
                    if opp_val == self:
                        setattr(item, "Alloc_MARTE_Element43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Alloc_MARTE_Element43"):
                    opp_val = getattr(item, "Alloc_MARTE_Element43", None)
                    
                    setattr(item, "Alloc_MARTE_Element43", self)
                    

    @property
    def MARTE_Alloc_Assign40(self):
        return self.__MARTE_Alloc_Assign40

    @MARTE_Alloc_Assign40.setter
    def MARTE_Alloc_Assign40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Alloc_Assign__MARTE_Alloc_Assign40", None)
        self.__MARTE_Alloc_Assign40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Alloc_MARTE_Element"):
                    opp_val = getattr(item, "Alloc_MARTE_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Alloc_MARTE_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Alloc_MARTE_Element"):
                    opp_val = getattr(item, "Alloc_MARTE_Element", None)
                    
                    setattr(item, "Alloc_MARTE_Element", self)
                    

    @property
    def MARTE_Alloc_Assign(self):
        return self.__MARTE_Alloc_Assign

    @MARTE_Alloc_Assign.setter
    def MARTE_Alloc_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Alloc_Assign__MARTE_Alloc_Assign", None)
        self.__MARTE_Alloc_Assign = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFPs_NfpConstraint38"):
                    opp_val = getattr(item, "NFPs_NfpConstraint38", None)
                    
                    if opp_val == self:
                        setattr(item, "NFPs_NfpConstraint38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFPs_NfpConstraint38"):
                    opp_val = getattr(item, "NFPs_NfpConstraint38", None)
                    
                    setattr(item, "NFPs_NfpConstraint38", self)
                    

class NFPs_NfpConstraint:

    pass
class MARTE_Time_ClockConstraint(Time_TimedElement, NFPs_NfpConstraint):

    def __init__(self, isCoincidenceBased: str, isPrecedenceBased: bool, isChronometricBased: str, NFPs_NfpConstraint38: "MARTE_Alloc_Assign" = None, NFPs_NfpConstraint: "MARTE_Alloc_NfpRefine" = None, NFPs_NfpConstraint49: "MARTE_Alloc_Allocate" = None):
        self.isCoincidenceBased = isCoincidenceBased
        self.isPrecedenceBased = isPrecedenceBased
        self.isChronometricBased = isChronometricBased
        
        pass
    @property
    def isChronometricBased(self):
        return self.__isChronometricBased

    @isChronometricBased.setter
    def isChronometricBased(self, isChronometricBased: str):
        self.__isChronometricBased = isChronometricBased


    @property
    def isPrecedenceBased(self):
        return self.__isPrecedenceBased

    @isPrecedenceBased.setter
    def isPrecedenceBased(self, isPrecedenceBased: bool):
        self.__isPrecedenceBased = isPrecedenceBased


    @property
    def isCoincidenceBased(self):
        return self.__isCoincidenceBased

    @isCoincidenceBased.setter
    def isCoincidenceBased(self, isCoincidenceBased: str):
        self.__isCoincidenceBased = isCoincidenceBased


class MARTE_Time_TimedConstraint(Time_TimedElement, NFPs_NfpConstraint):

    def __init__(self, interpretation: str, NFPs_NfpConstraint38: "MARTE_Alloc_Assign" = None, NFPs_NfpConstraint: "MARTE_Alloc_NfpRefine" = None, NFPs_NfpConstraint49: "MARTE_Alloc_Allocate" = None):
        self.interpretation = interpretation
        
        pass
    @property
    def interpretation(self):
        return self.__interpretation

    @interpretation.setter
    def interpretation(self, interpretation: str):
        self.__interpretation = interpretation


class MARTE_Alloc_Allocate:

    def __init__(self, kind: str, nature: str, MARTE_Alloc_Allocate: "Alloc_MARTE_Abstraction" = None, MARTE_Alloc_Allocate48: set["NFPs_NfpConstraint"] = None):
        self.kind = kind
        self.nature = nature
        self.MARTE_Alloc_Allocate = MARTE_Alloc_Allocate
        self.MARTE_Alloc_Allocate48 = MARTE_Alloc_Allocate48 if MARTE_Alloc_Allocate48 is not None else set()
        
        pass
    @property
    def nature(self):
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature


    @property
    def kind(self):
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

class MARTE_Alloc_NfpRefine:

    pass
class Alloc_Allocated:

    pass
class Alloc_MARTE_ActivityPartition:

    pass
class MARTE_Alloc_AllocateActivityGroup:

    def __init__(self, isUnique: str, MARTE_Alloc_AllocateActivityGroup: "Alloc_MARTE_ActivityPartition" = None):
        self.isUnique = isUnique
        self.MARTE_Alloc_AllocateActivityGroup = MARTE_Alloc_AllocateActivityGroup
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


    @property
    def MARTE_Alloc_AllocateActivityGroup(self):
        return self.__MARTE_Alloc_AllocateActivityGroup

    @MARTE_Alloc_AllocateActivityGroup.setter
    def MARTE_Alloc_AllocateActivityGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Alloc_AllocateActivityGroup__MARTE_Alloc_AllocateActivityGroup", None)
        self.__MARTE_Alloc_AllocateActivityGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Alloc_MARTE_ActivityPartition"):
                opp_val = getattr(old_value, "Alloc_MARTE_ActivityPartition", None)
                if opp_val == self:
                    setattr(old_value, "Alloc_MARTE_ActivityPartition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Alloc_MARTE_ActivityPartition"):
                opp_val = getattr(value, "Alloc_MARTE_ActivityPartition", None)
                setattr(value, "Alloc_MARTE_ActivityPartition", self)

class Alloc_MARTE_Dependency:

    pass
class TupleType:

    pass
class MARTE_NFPs_NfpType(TupleType):

    pass
class CoreElements_Mode:

    pass
class Alloc_MARTE_NamedElement:

    pass
class MARTE_Alloc_Allocated:

    def __init__(self, kind: str, MARTE_Alloc_Allocated: "Alloc_MARTE_NamedElement" = None, MARTE_Alloc_Allocated31: set["Alloc_Allocated"] = None, MARTE_Alloc_Allocated29: set["Alloc_Allocated"] = None):
        self.kind = kind
        self.MARTE_Alloc_Allocated = MARTE_Alloc_Allocated
        self.MARTE_Alloc_Allocated31 = MARTE_Alloc_Allocated31 if MARTE_Alloc_Allocated31 is not None else set()
        self.MARTE_Alloc_Allocated29 = MARTE_Alloc_Allocated29 if MARTE_Alloc_Allocated29 is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def MARTE_Alloc_Allocated31(self):
        return self.__MARTE_Alloc_Allocated31

    @MARTE_Alloc_Allocated31.setter
    def MARTE_Alloc_Allocated31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Alloc_Allocated__MARTE_Alloc_Allocated31", None)
        self.__MARTE_Alloc_Allocated31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Alloc_Allocated32"):
                    opp_val = getattr(item, "Alloc_Allocated32", None)
                    
                    if opp_val == self:
                        setattr(item, "Alloc_Allocated32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Alloc_Allocated32"):
                    opp_val = getattr(item, "Alloc_Allocated32", None)
                    
                    setattr(item, "Alloc_Allocated32", self)
                    

    @property
    def MARTE_Alloc_Allocated(self):
        return self.__MARTE_Alloc_Allocated

    @MARTE_Alloc_Allocated.setter
    def MARTE_Alloc_Allocated(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Alloc_Allocated__MARTE_Alloc_Allocated", None)
        self.__MARTE_Alloc_Allocated = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Alloc_MARTE_NamedElement"):
                opp_val = getattr(old_value, "Alloc_MARTE_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "Alloc_MARTE_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Alloc_MARTE_NamedElement"):
                opp_val = getattr(value, "Alloc_MARTE_NamedElement", None)
                setattr(value, "Alloc_MARTE_NamedElement", self)

    @property
    def MARTE_Alloc_Allocated29(self):
        return self.__MARTE_Alloc_Allocated29

    @MARTE_Alloc_Allocated29.setter
    def MARTE_Alloc_Allocated29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Alloc_Allocated__MARTE_Alloc_Allocated29", None)
        self.__MARTE_Alloc_Allocated29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Alloc_Allocated"):
                    opp_val = getattr(item, "Alloc_Allocated", None)
                    
                    if opp_val == self:
                        setattr(item, "Alloc_Allocated", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Alloc_Allocated"):
                    opp_val = getattr(item, "Alloc_Allocated", None)
                    
                    setattr(item, "Alloc_Allocated", self)
                    

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
class CoreElements_MARTE_StateMachine:

    pass
class MARTE_CoreElements_ModeBehavior:

    pass
class CoreElements_MARTE_Transition:

    pass
class MARTE_CoreElements_ModeTransition:

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
        
        pass
    @property
    def baseExponent(self):
        return self.__baseExponent

    @baseExponent.setter
    def baseExponent(self, baseExponent: int):
        self.__baseExponent = baseExponent


    @property
    def symbol(self):
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

class NFPs_MARTE_Constraint:

    pass
class MARTE_NFPs_NfpConstraint:

    def __init__(self, kind: str, MARTE_NFPs_NfpConstraint: "NFPs_MARTE_Constraint" = None, MARTE_NFPs_NfpConstraint6: set["CoreElements_Mode"] = None):
        self.kind = kind
        self.MARTE_NFPs_NfpConstraint = MARTE_NFPs_NfpConstraint
        self.MARTE_NFPs_NfpConstraint6 = MARTE_NFPs_NfpConstraint6 if MARTE_NFPs_NfpConstraint6 is not None else set()
        
        pass
    @property
    def kind(self):
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
class MARTE_NFPs_Unit:

    def __init__(self, convFactor: str, convOffset: str, MARTE_NFPs_Unit: "NFPs_Unit" = None, MARTE_NFPs_Unit3: "NFPs_MARTE_EnumerationLiteral" = None):
        self.convFactor = convFactor
        self.convOffset = convOffset
        self.MARTE_NFPs_Unit = MARTE_NFPs_Unit
        self.MARTE_NFPs_Unit3 = MARTE_NFPs_Unit3
        
        pass
    @property
    def convFactor(self):
        return self.__convFactor

    @convFactor.setter
    def convFactor(self, convFactor: str):
        self.__convFactor = convFactor


    @property
    def convOffset(self):
        return self.__convOffset

    @convOffset.setter
    def convOffset(self, convOffset: str):
        self.__convOffset = convOffset


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

class NFPs_MARTE_Property:

    pass
class MARTE_NFPs_Nfp:

    pass
class SW_Interaction_SwInteractionResource:

    pass
class MARTE_SW_Interaction_SwSynchronizationResource(SW_Interaction_SwInteractionResource, GRM_SynchronizationResource):

    pass
class SW_Interaction_MARTE_TypedElement:

    pass
class SW_Brokering_MARTE_BehavioralFeature:

    pass
class SW_Brokering_MARTE_TypedElement:

    pass
class InterruptResource:

    pass
class MARTE_SW_Concurrency_Alarm(InterruptResource):

    def __init__(self, isWatchdog: str, MARTE_SW_Concurrency_Alarm: set["SW_Concurrency_MARTE_TypedElement"] = None):
        self.isWatchdog = isWatchdog
        self.MARTE_SW_Concurrency_Alarm = MARTE_SW_Concurrency_Alarm if MARTE_SW_Concurrency_Alarm is not None else set()
        
        pass
    @property
    def isWatchdog(self):
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
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement347"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement347", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement347", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement347"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement347", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement347", self)
                    

class SW_Concurrency_MARTE_Namespace:

    pass
class TimerResource:

    pass
class MARTE_SW_Concurrency_SwTimerResource(TimerResource):

    pass
class SW_Concurrency_MARTE_NamedElement:

    pass
class SW_Concurrency_SwConcurrentResource:

    pass
class MARTE_SW_Concurrency_SwSchedulableResource(SW_Concurrency_SwConcurrentResource, GRM_SchedulableResource):

    def __init__(self, isStaticSchedulingFeature: str, isPreemptable: str, MARTE_SW_Concurrency_SwSchedulableResource: "SW_Concurrency_MARTE_NamedElement" = None, MARTE_SW_Concurrency_SwSchedulableResource314: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwSchedulableResource317: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwSchedulableResource320: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwSchedulableResource323: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwSchedulableResource326: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwSchedulableResource329: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, SchedulableResource123: "MARTE_GRM_SecondaryScheduler" = None, GRM_SchedulableResource534: "MARTE_PAM_PaRunTInstance" = None, GRM_SchedulableResource: "MARTE_GQAM_GaStep" = None, SchedulableResource: "MARTE_GRM_Scheduler" = None):
        self.isStaticSchedulingFeature = isStaticSchedulingFeature
        self.isPreemptable = isPreemptable
        self.MARTE_SW_Concurrency_SwSchedulableResource = MARTE_SW_Concurrency_SwSchedulableResource
        self.MARTE_SW_Concurrency_SwSchedulableResource314 = MARTE_SW_Concurrency_SwSchedulableResource314 if MARTE_SW_Concurrency_SwSchedulableResource314 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource317 = MARTE_SW_Concurrency_SwSchedulableResource317 if MARTE_SW_Concurrency_SwSchedulableResource317 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource320 = MARTE_SW_Concurrency_SwSchedulableResource320 if MARTE_SW_Concurrency_SwSchedulableResource320 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource323 = MARTE_SW_Concurrency_SwSchedulableResource323 if MARTE_SW_Concurrency_SwSchedulableResource323 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource326 = MARTE_SW_Concurrency_SwSchedulableResource326 if MARTE_SW_Concurrency_SwSchedulableResource326 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource329 = MARTE_SW_Concurrency_SwSchedulableResource329 if MARTE_SW_Concurrency_SwSchedulableResource329 is not None else set()
        
        pass
    @property
    def isStaticSchedulingFeature(self):
        return self.__isStaticSchedulingFeature

    @isStaticSchedulingFeature.setter
    def isStaticSchedulingFeature(self, isStaticSchedulingFeature: str):
        self.__isStaticSchedulingFeature = isStaticSchedulingFeature


    @property
    def isPreemptable(self):
        return self.__isPreemptable

    @isPreemptable.setter
    def isPreemptable(self, isPreemptable: str):
        self.__isPreemptable = isPreemptable


    @property
    def MARTE_SW_Concurrency_SwSchedulableResource317(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource317

    @MARTE_SW_Concurrency_SwSchedulableResource317.setter
    def MARTE_SW_Concurrency_SwSchedulableResource317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource317", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource317 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement318"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement318", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement318", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement318"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement318", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement318", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource329(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource329

    @MARTE_SW_Concurrency_SwSchedulableResource329.setter
    def MARTE_SW_Concurrency_SwSchedulableResource329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource329", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource329 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature330"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature330", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature330", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature330"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature330", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature330", self)
                    

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
    def MARTE_SW_Concurrency_SwSchedulableResource323(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource323

    @MARTE_SW_Concurrency_SwSchedulableResource323.setter
    def MARTE_SW_Concurrency_SwSchedulableResource323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource323", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource323 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature324"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature324", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature324", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature324"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature324", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature324", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource326(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource326

    @MARTE_SW_Concurrency_SwSchedulableResource326.setter
    def MARTE_SW_Concurrency_SwSchedulableResource326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource326", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource326 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature327"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature327", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature327", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature327"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature327", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature327", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource320(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource320

    @MARTE_SW_Concurrency_SwSchedulableResource320.setter
    def MARTE_SW_Concurrency_SwSchedulableResource320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource320", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource320 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement321"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement321", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement321"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement321", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement321", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource314(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource314

    @MARTE_SW_Concurrency_SwSchedulableResource314.setter
    def MARTE_SW_Concurrency_SwSchedulableResource314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource314", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource314 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement315"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement315", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement315"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement315", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement315", self)
                    

class SwConcurrentResource:

    pass
class MARTE_SW_Concurrency_InterruptResource(SwConcurrentResource):

    def __init__(self, kind: str, isMaskable: str, MARTE_SW_Concurrency_InterruptResource: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_InterruptResource304: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_InterruptResource307: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_InterruptResource310: set["SW_Concurrency_MARTE_BehavioralFeature"] = None):
        self.kind = kind
        self.isMaskable = isMaskable
        self.MARTE_SW_Concurrency_InterruptResource = MARTE_SW_Concurrency_InterruptResource if MARTE_SW_Concurrency_InterruptResource is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource304 = MARTE_SW_Concurrency_InterruptResource304 if MARTE_SW_Concurrency_InterruptResource304 is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource307 = MARTE_SW_Concurrency_InterruptResource307 if MARTE_SW_Concurrency_InterruptResource307 is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource310 = MARTE_SW_Concurrency_InterruptResource310 if MARTE_SW_Concurrency_InterruptResource310 is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def isMaskable(self):
        return self.__isMaskable

    @isMaskable.setter
    def isMaskable(self, isMaskable: str):
        self.__isMaskable = isMaskable


    @property
    def MARTE_SW_Concurrency_InterruptResource310(self):
        return self.__MARTE_SW_Concurrency_InterruptResource310

    @MARTE_SW_Concurrency_InterruptResource310.setter
    def MARTE_SW_Concurrency_InterruptResource310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource310", None)
        self.__MARTE_SW_Concurrency_InterruptResource310 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature311"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature311", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature311", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature311"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature311", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature311", self)
                    

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
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement302"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement302", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement302", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement302"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement302", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement302", self)
                    

    @property
    def MARTE_SW_Concurrency_InterruptResource307(self):
        return self.__MARTE_SW_Concurrency_InterruptResource307

    @MARTE_SW_Concurrency_InterruptResource307.setter
    def MARTE_SW_Concurrency_InterruptResource307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource307", None)
        self.__MARTE_SW_Concurrency_InterruptResource307 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature308"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature308", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature308", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature308"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature308", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature308", self)
                    

    @property
    def MARTE_SW_Concurrency_InterruptResource304(self):
        return self.__MARTE_SW_Concurrency_InterruptResource304

    @MARTE_SW_Concurrency_InterruptResource304.setter
    def MARTE_SW_Concurrency_InterruptResource304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource304", None)
        self.__MARTE_SW_Concurrency_InterruptResource304 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement305"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement305", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement305", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement305"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement305", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement305", self)
                    

class SW_Concurrency_MARTE_Element:

    pass
class SwResource:

    pass
class MARTE_SW_Interaction_SwInteractionResource(SwResource):

    def __init__(self, isIntraMemoryPartitionInteraction: bool, waitingQueuePolicy: str, waitingQueueCapacity: str, MARTE_SW_Interaction_SwInteractionResource: set["SW_Interaction_MARTE_TypedElement"] = None):
        self.isIntraMemoryPartitionInteraction = isIntraMemoryPartitionInteraction
        self.waitingQueuePolicy = waitingQueuePolicy
        self.waitingQueueCapacity = waitingQueueCapacity
        self.MARTE_SW_Interaction_SwInteractionResource = MARTE_SW_Interaction_SwInteractionResource if MARTE_SW_Interaction_SwInteractionResource is not None else set()
        
        pass
    @property
    def isIntraMemoryPartitionInteraction(self):
        return self.__isIntraMemoryPartitionInteraction

    @isIntraMemoryPartitionInteraction.setter
    def isIntraMemoryPartitionInteraction(self, isIntraMemoryPartitionInteraction: bool):
        self.__isIntraMemoryPartitionInteraction = isIntraMemoryPartitionInteraction


    @property
    def waitingQueuePolicy(self):
        return self.__waitingQueuePolicy

    @waitingQueuePolicy.setter
    def waitingQueuePolicy(self, waitingQueuePolicy: str):
        self.__waitingQueuePolicy = waitingQueuePolicy


    @property
    def waitingQueueCapacity(self):
        return self.__waitingQueueCapacity

    @waitingQueueCapacity.setter
    def waitingQueueCapacity(self, waitingQueueCapacity: str):
        self.__waitingQueueCapacity = waitingQueueCapacity


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
                    

class MARTE_SW_Brokering_DeviceBroker(SwResource):

    def __init__(self, accessPolicy: str, isBuffered: str, MARTE_SW_Brokering_DeviceBroker: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_DeviceBroker350: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker352: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker355: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker358: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker361: set["SW_Brokering_MARTE_BehavioralFeature"] = None):
        self.accessPolicy = accessPolicy
        self.isBuffered = isBuffered
        self.MARTE_SW_Brokering_DeviceBroker = MARTE_SW_Brokering_DeviceBroker if MARTE_SW_Brokering_DeviceBroker is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker350 = MARTE_SW_Brokering_DeviceBroker350 if MARTE_SW_Brokering_DeviceBroker350 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker352 = MARTE_SW_Brokering_DeviceBroker352 if MARTE_SW_Brokering_DeviceBroker352 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker355 = MARTE_SW_Brokering_DeviceBroker355 if MARTE_SW_Brokering_DeviceBroker355 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker358 = MARTE_SW_Brokering_DeviceBroker358 if MARTE_SW_Brokering_DeviceBroker358 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker361 = MARTE_SW_Brokering_DeviceBroker361 if MARTE_SW_Brokering_DeviceBroker361 is not None else set()
        
        pass
    @property
    def accessPolicy(self):
        return self.__accessPolicy

    @accessPolicy.setter
    def accessPolicy(self, accessPolicy: str):
        self.__accessPolicy = accessPolicy


    @property
    def isBuffered(self):
        return self.__isBuffered

    @isBuffered.setter
    def isBuffered(self, isBuffered: str):
        self.__isBuffered = isBuffered


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
    def MARTE_SW_Brokering_DeviceBroker358(self):
        return self.__MARTE_SW_Brokering_DeviceBroker358

    @MARTE_SW_Brokering_DeviceBroker358.setter
    def MARTE_SW_Brokering_DeviceBroker358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker358", None)
        self.__MARTE_SW_Brokering_DeviceBroker358 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature359"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature359", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature359", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature359"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature359", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature359", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker352(self):
        return self.__MARTE_SW_Brokering_DeviceBroker352

    @MARTE_SW_Brokering_DeviceBroker352.setter
    def MARTE_SW_Brokering_DeviceBroker352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker352", None)
        self.__MARTE_SW_Brokering_DeviceBroker352 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature353"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature353", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature353", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature353"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature353", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature353", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker350(self):
        return self.__MARTE_SW_Brokering_DeviceBroker350

    @MARTE_SW_Brokering_DeviceBroker350.setter
    def MARTE_SW_Brokering_DeviceBroker350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker350", None)
        self.__MARTE_SW_Brokering_DeviceBroker350 = value if value is not None else set()
        
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
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker355(self):
        return self.__MARTE_SW_Brokering_DeviceBroker355

    @MARTE_SW_Brokering_DeviceBroker355.setter
    def MARTE_SW_Brokering_DeviceBroker355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker355", None)
        self.__MARTE_SW_Brokering_DeviceBroker355 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature356"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature356", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature356", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature356"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature356", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature356", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker361(self):
        return self.__MARTE_SW_Brokering_DeviceBroker361

    @MARTE_SW_Brokering_DeviceBroker361.setter
    def MARTE_SW_Brokering_DeviceBroker361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker361", None)
        self.__MARTE_SW_Brokering_DeviceBroker361 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature362"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature362", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature362", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature362"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature362", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature362", self)
                    

class MARTE_SW_Brokering_MemoryBroker(SwResource):

    def __init__(self, accessPolicy: str, MARTE_SW_Brokering_MemoryBroker: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_MemoryBroker366: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_MemoryBroker369: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_MemoryBroker372: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker375: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker378: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker381: set["SW_Brokering_MARTE_BehavioralFeature"] = None):
        self.accessPolicy = accessPolicy
        self.MARTE_SW_Brokering_MemoryBroker = MARTE_SW_Brokering_MemoryBroker if MARTE_SW_Brokering_MemoryBroker is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker366 = MARTE_SW_Brokering_MemoryBroker366 if MARTE_SW_Brokering_MemoryBroker366 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker369 = MARTE_SW_Brokering_MemoryBroker369 if MARTE_SW_Brokering_MemoryBroker369 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker372 = MARTE_SW_Brokering_MemoryBroker372 if MARTE_SW_Brokering_MemoryBroker372 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker375 = MARTE_SW_Brokering_MemoryBroker375 if MARTE_SW_Brokering_MemoryBroker375 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker378 = MARTE_SW_Brokering_MemoryBroker378 if MARTE_SW_Brokering_MemoryBroker378 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker381 = MARTE_SW_Brokering_MemoryBroker381 if MARTE_SW_Brokering_MemoryBroker381 is not None else set()
        
        pass
    @property
    def accessPolicy(self):
        return self.__accessPolicy

    @accessPolicy.setter
    def accessPolicy(self, accessPolicy: str):
        self.__accessPolicy = accessPolicy


    @property
    def MARTE_SW_Brokering_MemoryBroker369(self):
        return self.__MARTE_SW_Brokering_MemoryBroker369

    @MARTE_SW_Brokering_MemoryBroker369.setter
    def MARTE_SW_Brokering_MemoryBroker369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker369", None)
        self.__MARTE_SW_Brokering_MemoryBroker369 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement370"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement370", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement370", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement370"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement370", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement370", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker372(self):
        return self.__MARTE_SW_Brokering_MemoryBroker372

    @MARTE_SW_Brokering_MemoryBroker372.setter
    def MARTE_SW_Brokering_MemoryBroker372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker372", None)
        self.__MARTE_SW_Brokering_MemoryBroker372 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature373"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature373", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature373", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature373"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature373", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature373", self)
                    

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
                if hasattr(item, "SW_Brokering_MARTE_TypedElement364"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement364", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement364", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement364"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement364", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement364", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker375(self):
        return self.__MARTE_SW_Brokering_MemoryBroker375

    @MARTE_SW_Brokering_MemoryBroker375.setter
    def MARTE_SW_Brokering_MemoryBroker375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker375", None)
        self.__MARTE_SW_Brokering_MemoryBroker375 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature376"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature376", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature376", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature376"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature376", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature376", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker378(self):
        return self.__MARTE_SW_Brokering_MemoryBroker378

    @MARTE_SW_Brokering_MemoryBroker378.setter
    def MARTE_SW_Brokering_MemoryBroker378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker378", None)
        self.__MARTE_SW_Brokering_MemoryBroker378 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature379"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature379", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature379", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature379"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature379", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature379", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker381(self):
        return self.__MARTE_SW_Brokering_MemoryBroker381

    @MARTE_SW_Brokering_MemoryBroker381.setter
    def MARTE_SW_Brokering_MemoryBroker381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker381", None)
        self.__MARTE_SW_Brokering_MemoryBroker381 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature382"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature382", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature382", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature382"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature382", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature382", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker366(self):
        return self.__MARTE_SW_Brokering_MemoryBroker366

    @MARTE_SW_Brokering_MemoryBroker366.setter
    def MARTE_SW_Brokering_MemoryBroker366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker366", None)
        self.__MARTE_SW_Brokering_MemoryBroker366 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement367"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement367", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement367", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement367"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement367", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement367", self)
                    

class MARTE_SW_Concurrency_MemoryPartition(SwResource):

    pass
class MARTE_SW_Concurrency_SwConcurrentResource(SwResource):

    def __init__(self, type: str, activationCapacity: str, MARTE_SW_Concurrency_SwConcurrentResource258: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource: set["SW_Concurrency_MARTE_Element"] = None, MARTE_SW_Concurrency_SwConcurrentResource260: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource263: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource266: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource269: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource272: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource275: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource278: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource281: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource284: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource287: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource290: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource293: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource296: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource299: set["SW_Concurrency_MARTE_TypedElement"] = None):
        self.type = type
        self.activationCapacity = activationCapacity
        self.MARTE_SW_Concurrency_SwConcurrentResource258 = MARTE_SW_Concurrency_SwConcurrentResource258 if MARTE_SW_Concurrency_SwConcurrentResource258 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource = MARTE_SW_Concurrency_SwConcurrentResource if MARTE_SW_Concurrency_SwConcurrentResource is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource260 = MARTE_SW_Concurrency_SwConcurrentResource260 if MARTE_SW_Concurrency_SwConcurrentResource260 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource263 = MARTE_SW_Concurrency_SwConcurrentResource263 if MARTE_SW_Concurrency_SwConcurrentResource263 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource266 = MARTE_SW_Concurrency_SwConcurrentResource266 if MARTE_SW_Concurrency_SwConcurrentResource266 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource269 = MARTE_SW_Concurrency_SwConcurrentResource269 if MARTE_SW_Concurrency_SwConcurrentResource269 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource272 = MARTE_SW_Concurrency_SwConcurrentResource272 if MARTE_SW_Concurrency_SwConcurrentResource272 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource275 = MARTE_SW_Concurrency_SwConcurrentResource275 if MARTE_SW_Concurrency_SwConcurrentResource275 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource278 = MARTE_SW_Concurrency_SwConcurrentResource278 if MARTE_SW_Concurrency_SwConcurrentResource278 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource281 = MARTE_SW_Concurrency_SwConcurrentResource281 if MARTE_SW_Concurrency_SwConcurrentResource281 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource284 = MARTE_SW_Concurrency_SwConcurrentResource284 if MARTE_SW_Concurrency_SwConcurrentResource284 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource287 = MARTE_SW_Concurrency_SwConcurrentResource287 if MARTE_SW_Concurrency_SwConcurrentResource287 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource290 = MARTE_SW_Concurrency_SwConcurrentResource290 if MARTE_SW_Concurrency_SwConcurrentResource290 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource293 = MARTE_SW_Concurrency_SwConcurrentResource293 if MARTE_SW_Concurrency_SwConcurrentResource293 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource296 = MARTE_SW_Concurrency_SwConcurrentResource296 if MARTE_SW_Concurrency_SwConcurrentResource296 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource299 = MARTE_SW_Concurrency_SwConcurrentResource299 if MARTE_SW_Concurrency_SwConcurrentResource299 is not None else set()
        
        pass
    @property
    def activationCapacity(self):
        return self.__activationCapacity

    @activationCapacity.setter
    def activationCapacity(self, activationCapacity: str):
        self.__activationCapacity = activationCapacity


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def MARTE_SW_Concurrency_SwConcurrentResource258(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource258

    @MARTE_SW_Concurrency_SwConcurrentResource258.setter
    def MARTE_SW_Concurrency_SwConcurrentResource258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource258", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource258 = value if value is not None else set()
        
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
    def MARTE_SW_Concurrency_SwConcurrentResource275(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource275

    @MARTE_SW_Concurrency_SwConcurrentResource275.setter
    def MARTE_SW_Concurrency_SwConcurrentResource275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource275", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource275 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature276"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature276", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature276", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature276"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature276", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature276", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource281(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource281

    @MARTE_SW_Concurrency_SwConcurrentResource281.setter
    def MARTE_SW_Concurrency_SwConcurrentResource281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource281", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature282"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature282", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature282"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature282", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature282", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource293(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource293

    @MARTE_SW_Concurrency_SwConcurrentResource293.setter
    def MARTE_SW_Concurrency_SwConcurrentResource293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource293", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource293 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement294"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement294", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement294", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement294"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement294", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement294", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource290(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource290

    @MARTE_SW_Concurrency_SwConcurrentResource290.setter
    def MARTE_SW_Concurrency_SwConcurrentResource290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource290", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource290 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement291"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement291", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement291", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement291"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement291", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement291", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource272(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource272

    @MARTE_SW_Concurrency_SwConcurrentResource272.setter
    def MARTE_SW_Concurrency_SwConcurrentResource272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource272", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature273"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature273", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature273", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature273"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature273", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature273", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource296(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource296

    @MARTE_SW_Concurrency_SwConcurrentResource296.setter
    def MARTE_SW_Concurrency_SwConcurrentResource296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource296", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource296 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement297"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement297", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement297", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement297"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement297", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement297", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource269(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource269

    @MARTE_SW_Concurrency_SwConcurrentResource269.setter
    def MARTE_SW_Concurrency_SwConcurrentResource269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource269", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource269 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature270"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature270", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature270"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature270", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature270", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource299(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource299

    @MARTE_SW_Concurrency_SwConcurrentResource299.setter
    def MARTE_SW_Concurrency_SwConcurrentResource299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource299", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource299 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement300"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement300", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement300"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement300", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement300", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource266(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource266

    @MARTE_SW_Concurrency_SwConcurrentResource266.setter
    def MARTE_SW_Concurrency_SwConcurrentResource266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource266", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement267"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement267", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement267", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement267"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement267", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement267", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource287(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource287

    @MARTE_SW_Concurrency_SwConcurrentResource287.setter
    def MARTE_SW_Concurrency_SwConcurrentResource287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource287", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement288"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement288", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement288", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement288"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement288", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement288", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource278(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource278

    @MARTE_SW_Concurrency_SwConcurrentResource278.setter
    def MARTE_SW_Concurrency_SwConcurrentResource278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource278", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource278 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature279"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature279", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature279", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature279"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature279", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature279", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource263(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource263

    @MARTE_SW_Concurrency_SwConcurrentResource263.setter
    def MARTE_SW_Concurrency_SwConcurrentResource263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource263", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource263 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement264"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement264", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement264", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement264"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement264", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement264", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource260(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource260

    @MARTE_SW_Concurrency_SwConcurrentResource260.setter
    def MARTE_SW_Concurrency_SwConcurrentResource260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource260", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource260 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement261"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement261", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement261", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement261"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement261", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement261", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource

    @MARTE_SW_Concurrency_SwConcurrentResource.setter
    def MARTE_SW_Concurrency_SwConcurrentResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource = value if value is not None else set()
        
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
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource284(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource284

    @MARTE_SW_Concurrency_SwConcurrentResource284.setter
    def MARTE_SW_Concurrency_SwConcurrentResource284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource284", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource284 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature285"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature285", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature285", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature285"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature285", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature285", self)
                    

class SW_Concurrency_MARTE_BehavioralFeature:

    pass
class MARTE_SW_Concurrency_EntryPoint(Allocate):

    def __init__(self, isReentrant: str, MARTE_SW_Concurrency_EntryPoint: "SW_Concurrency_MARTE_BehavioralFeature" = None):
        self.isReentrant = isReentrant
        self.MARTE_SW_Concurrency_EntryPoint = MARTE_SW_Concurrency_EntryPoint
        
        pass
    @property
    def isReentrant(self):
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

class SW_ResourceCore_MARTE_Property:

    pass
class MARTE_SW_ResourceCore_SwAccessService(GrService):

    def __init__(self, isModifier: str, MARTE_SW_ResourceCore_SwAccessService: "SW_ResourceCore_MARTE_Property" = None):
        self.isModifier = isModifier
        self.MARTE_SW_ResourceCore_SwAccessService = MARTE_SW_ResourceCore_SwAccessService
        
        pass
    @property
    def isModifier(self):
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

class SW_ResourceCore_MARTE_BehavioralFeature:

    pass
class SW_ResourceCore_MARTE_TypedElement:

    pass
class SW_Concurrency_MARTE_TypedElement:

    pass
class HwComponent:

    pass
class MARTE_HwPower_HwCoolingSupply(HwComponent):

    def __init__(self, coolingPower: str):
        self.coolingPower = coolingPower
        
        pass
    @property
    def coolingPower(self):
        return self.__coolingPower

    @coolingPower.setter
    def coolingPower(self, coolingPower: str):
        self.__coolingPower = coolingPower


class MARTE_HwPower_HwPowerSupply(HwComponent):

    def __init__(self, suppliedPower: str, capacity: str):
        self.suppliedPower = suppliedPower
        self.capacity = capacity
        
        pass
    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity


    @property
    def suppliedPower(self):
        return self.__suppliedPower

    @suppliedPower.setter
    def suppliedPower(self, suppliedPower: str):
        self.__suppliedPower = suppliedPower


class HwLayout_HwComponent:

    pass
class MARTE_SW_ResourceCore_SwResource(Resource):

    pass
class HwCommunication_HwEndPoint:

    pass
class HwGeneral_HwResourceService:

    pass
class MARTE_HwGeneral_HwResource(Resource):

    def __init__(self, description: str, frequency: str, MARTE_HwGeneral_HwResource: set["HwGeneral_HwResourceService"] = None, MARTE_HwGeneral_HwResource229: set["HwGeneral_HwResourceService"] = None, MARTE_HwGeneral_HwResource232: set["HwGeneral_HwResource"] = None, MARTE_HwGeneral_HwResource234: set["HwCommunication_HwEndPoint"] = None):
        self.description = description
        self.frequency = frequency
        self.MARTE_HwGeneral_HwResource = MARTE_HwGeneral_HwResource if MARTE_HwGeneral_HwResource is not None else set()
        self.MARTE_HwGeneral_HwResource229 = MARTE_HwGeneral_HwResource229 if MARTE_HwGeneral_HwResource229 is not None else set()
        self.MARTE_HwGeneral_HwResource232 = MARTE_HwGeneral_HwResource232 if MARTE_HwGeneral_HwResource232 is not None else set()
        self.MARTE_HwGeneral_HwResource234 = MARTE_HwGeneral_HwResource234 if MARTE_HwGeneral_HwResource234 is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: str):
        self.__frequency = frequency


    @property
    def MARTE_HwGeneral_HwResource234(self):
        return self.__MARTE_HwGeneral_HwResource234

    @MARTE_HwGeneral_HwResource234.setter
    def MARTE_HwGeneral_HwResource234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource234", None)
        self.__MARTE_HwGeneral_HwResource234 = value if value is not None else set()
        
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
    def MARTE_HwGeneral_HwResource232(self):
        return self.__MARTE_HwGeneral_HwResource232

    @MARTE_HwGeneral_HwResource232.setter
    def MARTE_HwGeneral_HwResource232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource232", None)
        self.__MARTE_HwGeneral_HwResource232 = value if value is not None else set()
        
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
    def MARTE_HwGeneral_HwResource(self):
        return self.__MARTE_HwGeneral_HwResource

    @MARTE_HwGeneral_HwResource.setter
    def MARTE_HwGeneral_HwResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource", None)
        self.__MARTE_HwGeneral_HwResource = value if value is not None else set()
        
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
    def MARTE_HwGeneral_HwResource229(self):
        return self.__MARTE_HwGeneral_HwResource229

    @MARTE_HwGeneral_HwResource229.setter
    def MARTE_HwGeneral_HwResource229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource229", None)
        self.__MARTE_HwGeneral_HwResource229 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResourceService230"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService230", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResourceService230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResourceService230"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService230", None)
                    
                    setattr(item, "HwGeneral_HwResourceService230", self)
                    

class MARTE_HwGeneral_HwResourceService(GrService):

    def __init__(self, consumption: str, dissipation: str):
        self.consumption = consumption
        self.dissipation = dissipation
        
        pass
    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, consumption: str):
        self.__consumption = consumption


    @property
    def dissipation(self):
        return self.__dissipation

    @dissipation.setter
    def dissipation(self, dissipation: str):
        self.__dissipation = dissipation


class HwI_O:

    pass
class MARTE_HwDevice_HWSensor(HwI_O):

    pass
class MARTE_HwDevice_HWActuator(HwI_O):

    pass
class HwTiming_HwClock:

    pass
class HwTimingResource:

    pass
class MARTE_HwTiming_HwTimer(HwTimingResource):

    def __init__(self, nbCounters: str, counterWidth: str, MARTE_HwTiming_HwTimer: "HwTiming_HwClock" = None):
        self.nbCounters = nbCounters
        self.counterWidth = counterWidth
        self.MARTE_HwTiming_HwTimer = MARTE_HwTiming_HwTimer
        
        pass
    @property
    def counterWidth(self):
        return self.__counterWidth

    @counterWidth.setter
    def counterWidth(self, counterWidth: str):
        self.__counterWidth = counterWidth


    @property
    def nbCounters(self):
        return self.__nbCounters

    @nbCounters.setter
    def nbCounters(self, nbCounters: str):
        self.__nbCounters = nbCounters


    @property
    def MARTE_HwTiming_HwTimer(self):
        return self.__MARTE_HwTiming_HwTimer

    @MARTE_HwTiming_HwTimer.setter
    def MARTE_HwTiming_HwTimer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwTiming_HwTimer__MARTE_HwTiming_HwTimer", None)
        self.__MARTE_HwTiming_HwTimer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HwTiming_HwClock"):
                opp_val = getattr(old_value, "HwTiming_HwClock", None)
                if opp_val == self:
                    setattr(old_value, "HwTiming_HwClock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HwTiming_HwClock"):
                opp_val = getattr(value, "HwTiming_HwClock", None)
                setattr(value, "HwTiming_HwClock", self)

class MARTE_HwTiming_HwClock(HwTimingResource):

    pass
class GRM_TimingResource:

    pass
class HwDevice:

    pass
class MARTE_HwDevice_HwSupport(HwDevice):

    pass
class MARTE_HwDevice_HwI_O(HwDevice):

    pass
class GRM_DeviceResource:

    pass
class HwMemory:

    pass
class MARTE_HwMemory_HwROM(HwMemory):

    def __init__(self, type: str, organization: str):
        self.type = type
        self.organization = organization
        
        pass
    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class MARTE_HwMemory_HwDrive(HwMemory):

    def __init__(self, sectorSize: str, MARTE_HwMemory_HwDrive: "HwMemory_HwRAM" = None):
        self.sectorSize = sectorSize
        self.MARTE_HwMemory_HwDrive = MARTE_HwMemory_HwDrive
        
        pass
    @property
    def sectorSize(self):
        return self.__sectorSize

    @sectorSize.setter
    def sectorSize(self, sectorSize: str):
        self.__sectorSize = sectorSize


    @property
    def MARTE_HwMemory_HwDrive(self):
        return self.__MARTE_HwMemory_HwDrive

    @MARTE_HwMemory_HwDrive.setter
    def MARTE_HwMemory_HwDrive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwDrive__MARTE_HwMemory_HwDrive", None)
        self.__MARTE_HwMemory_HwDrive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HwMemory_HwRAM225"):
                opp_val = getattr(old_value, "HwMemory_HwRAM225", None)
                if opp_val == self:
                    setattr(old_value, "HwMemory_HwRAM225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HwMemory_HwRAM225"):
                opp_val = getattr(value, "HwMemory_HwRAM225", None)
                setattr(value, "HwMemory_HwRAM225", self)

class MARTE_HwMemory_HwCache(HwMemory):

    def __init__(self, level: str, type: str, structure: str, repl_Policy: str, writePolicy: str):
        self.level = level
        self.type = type
        self.structure = structure
        self.repl_Policy = repl_Policy
        self.writePolicy = writePolicy
        
        pass
    @property
    def writePolicy(self):
        return self.__writePolicy

    @writePolicy.setter
    def writePolicy(self, writePolicy: str):
        self.__writePolicy = writePolicy


    @property
    def structure(self):
        return self.__structure

    @structure.setter
    def structure(self, structure: str):
        self.__structure = structure


    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level


    @property
    def repl_Policy(self):
        return self.__repl_Policy

    @repl_Policy.setter
    def repl_Policy(self, repl_Policy: str):
        self.__repl_Policy = repl_Policy


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class MARTE_HwMemory_HwRAM(HwMemory):

    def __init__(self, isSynchronous: str, isStatic: str, isNonVolatile: str, organization: str, repl_Policy: str, writePolicy: str):
        self.isSynchronous = isSynchronous
        self.isStatic = isStatic
        self.isNonVolatile = isNonVolatile
        self.organization = organization
        self.repl_Policy = repl_Policy
        self.writePolicy = writePolicy
        
        pass
    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization


    @property
    def isStatic(self):
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic


    @property
    def isNonVolatile(self):
        return self.__isNonVolatile

    @isNonVolatile.setter
    def isNonVolatile(self, isNonVolatile: str):
        self.__isNonVolatile = isNonVolatile


    @property
    def writePolicy(self):
        return self.__writePolicy

    @writePolicy.setter
    def writePolicy(self, writePolicy: str):
        self.__writePolicy = writePolicy


    @property
    def repl_Policy(self):
        return self.__repl_Policy

    @repl_Policy.setter
    def repl_Policy(self, repl_Policy: str):
        self.__repl_Policy = repl_Policy


    @property
    def isSynchronous(self):
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: str):
        self.__isSynchronous = isSynchronous


class HwComputing_HwProcessor:

    pass
class HwStorageManager_HwStorageManager:

    pass
class HwMemory_HwMemory:

    pass
class GRM_StorageResource:

    pass
class GRM_CommunicationEndPoint:

    pass
class HwMedia:

    pass
class MARTE_HwCommunication_HwBridge(HwMedia):

    pass
class MARTE_HwCommunication_HwBus(HwMedia):

    def __init__(self, adressWidth: str, wordWidth: str, isSynchronous: str, isSerial: str):
        self.adressWidth = adressWidth
        self.wordWidth = wordWidth
        self.isSynchronous = isSynchronous
        self.isSerial = isSerial
        
        pass
    @property
    def wordWidth(self):
        return self.__wordWidth

    @wordWidth.setter
    def wordWidth(self, wordWidth: str):
        self.__wordWidth = wordWidth


    @property
    def isSynchronous(self):
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: str):
        self.__isSynchronous = isSynchronous


    @property
    def isSerial(self):
        return self.__isSerial

    @isSerial.setter
    def isSerial(self, isSerial: str):
        self.__isSerial = isSerial


    @property
    def adressWidth(self):
        return self.__adressWidth

    @adressWidth.setter
    def adressWidth(self, adressWidth: str):
        self.__adressWidth = adressWidth


class HwCommunication_HwArbiter:

    pass
class MARTE_HwStorageManager_HwDMA(HwCommunication_HwArbiter, HwStorageManager_HwStorageManager):

    def __init__(self, nbChannels: str, transferWidth: str, MARTE_HwStorageManager_HwDMA: set["HwComputing_HwProcessor"] = None, HwArbiter: "MARTE_HwCommunication_HwMedia" = None):
        self.nbChannels = nbChannels
        self.transferWidth = transferWidth
        self.MARTE_HwStorageManager_HwDMA = MARTE_HwStorageManager_HwDMA if MARTE_HwStorageManager_HwDMA is not None else set()
        
        pass
    @property
    def nbChannels(self):
        return self.__nbChannels

    @nbChannels.setter
    def nbChannels(self, nbChannels: str):
        self.__nbChannels = nbChannels


    @property
    def transferWidth(self):
        return self.__transferWidth

    @transferWidth.setter
    def transferWidth(self, transferWidth: str):
        self.__transferWidth = transferWidth


    @property
    def MARTE_HwStorageManager_HwDMA(self):
        return self.__MARTE_HwStorageManager_HwDMA

    @MARTE_HwStorageManager_HwDMA.setter
    def MARTE_HwStorageManager_HwDMA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwStorageManager_HwDMA__MARTE_HwStorageManager_HwDMA", None)
        self.__MARTE_HwStorageManager_HwDMA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwComputing_HwProcessor"):
                    opp_val = getattr(item, "HwComputing_HwProcessor", None)
                    
                    if opp_val == self:
                        setattr(item, "HwComputing_HwProcessor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwComputing_HwProcessor"):
                    opp_val = getattr(item, "HwComputing_HwProcessor", None)
                    
                    setattr(item, "HwComputing_HwProcessor", self)
                    

class HwCommunication_HwCommunicationResource:

    pass
class MARTE_HwCommunication_HwEndPoint(GRM_CommunicationEndPoint, HwCommunication_HwCommunicationResource):

    pass
class GRM_CommunicationMedia:

    pass
class MARTE_SW_Interaction_SwCommunicationResource(SW_Interaction_SwInteractionResource, GRM_CommunicationMedia):

    pass
class MARTE_GQAM_GaCommHost(GRM_Scheduler, GRM_CommunicationMedia):

    def __init__(self, throughput: str, utilization: str, GRM_Scheduler: "MARTE_GRM_ProcessingResource" = None, Scheduler121: "MARTE_GRM_SchedulableResource" = None, Scheduler: "MARTE_GRM_MutualExclusionResource" = None):
        self.throughput = throughput
        self.utilization = utilization
        
        pass
    @property
    def throughput(self):
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput


    @property
    def utilization(self):
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization


class MARTE_HwCommunication_HwMedia(HwCommunication_HwCommunicationResource, GRM_CommunicationMedia):

    def __init__(self, bandWidth: str, controlledMedias: set["HwCommunication_HwArbiter"] = None):
        self.bandWidth = bandWidth
        self.controlledMedias = controlledMedias if controlledMedias is not None else set()
        
        pass
    @property
    def bandWidth(self):
        return self.__bandWidth

    @bandWidth.setter
    def bandWidth(self, bandWidth: str):
        self.__bandWidth = bandWidth


    @property
    def controlledMedias(self):
        return self.__controlledMedias

    @controlledMedias.setter
    def controlledMedias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwCommunication_HwMedia__controlledMedias", None)
        self.__controlledMedias = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwArbiter"):
                    opp_val = getattr(item, "HwArbiter", None)
                    
                    if opp_val == self:
                        setattr(item, "HwArbiter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwArbiter"):
                    opp_val = getattr(item, "HwArbiter", None)
                    
                    setattr(item, "HwArbiter", self)
                    

class HwStorageManager:

    pass
class MARTE_HwStorageManager_HwMMU(HwStorageManager):

    def __init__(self, virtualAddrSpace: str, physicalAddrSpace: str, memoryProtection: str, nbEntries: str, MARTE_HwStorageManager_HwMMU: set["HwMemory_HwCache"] = None):
        self.virtualAddrSpace = virtualAddrSpace
        self.physicalAddrSpace = physicalAddrSpace
        self.memoryProtection = memoryProtection
        self.nbEntries = nbEntries
        self.MARTE_HwStorageManager_HwMMU = MARTE_HwStorageManager_HwMMU if MARTE_HwStorageManager_HwMMU is not None else set()
        
        pass
    @property
    def virtualAddrSpace(self):
        return self.__virtualAddrSpace

    @virtualAddrSpace.setter
    def virtualAddrSpace(self, virtualAddrSpace: str):
        self.__virtualAddrSpace = virtualAddrSpace


    @property
    def memoryProtection(self):
        return self.__memoryProtection

    @memoryProtection.setter
    def memoryProtection(self, memoryProtection: str):
        self.__memoryProtection = memoryProtection


    @property
    def physicalAddrSpace(self):
        return self.__physicalAddrSpace

    @physicalAddrSpace.setter
    def physicalAddrSpace(self, physicalAddrSpace: str):
        self.__physicalAddrSpace = physicalAddrSpace


    @property
    def nbEntries(self):
        return self.__nbEntries

    @nbEntries.setter
    def nbEntries(self, nbEntries: str):
        self.__nbEntries = nbEntries


    @property
    def MARTE_HwStorageManager_HwMMU(self):
        return self.__MARTE_HwStorageManager_HwMMU

    @MARTE_HwStorageManager_HwMMU.setter
    def MARTE_HwStorageManager_HwMMU(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwStorageManager_HwMMU__MARTE_HwStorageManager_HwMMU", None)
        self.__MARTE_HwStorageManager_HwMMU = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwMemory_HwCache223"):
                    opp_val = getattr(item, "HwMemory_HwCache223", None)
                    
                    if opp_val == self:
                        setattr(item, "HwMemory_HwCache223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwMemory_HwCache223"):
                    opp_val = getattr(item, "HwMemory_HwCache223", None)
                    
                    setattr(item, "HwMemory_HwCache223", self)
                    

class HwComputing_HwComputingResource:

    pass
class HwMemory_HwRAM:

    pass
class HwResource:

    pass
class MARTE_HwComputing_HwBranchPredictor(HwResource):

    pass
class MARTE_HwCommunication_HwCommunicationResource(HwResource):

    pass
class MARTE_HwLayout_HwComponent(HwResource):

    def __init__(self, grid: str, nbPins: str, weight: str, kind: str, dimensions: str, area: str, position: str, price: str, r_Conditions: str, staticConsumption: str, staticDissipation: str, MARTE_HwLayout_HwComponent: set["HwGeneral_HwResourceService"] = None, MARTE_HwLayout_HwComponent238: set["HwLayout_HwComponent"] = None):
        self.grid = grid
        self.nbPins = nbPins
        self.weight = weight
        self.kind = kind
        self.dimensions = dimensions
        self.area = area
        self.position = position
        self.price = price
        self.r_Conditions = r_Conditions
        self.staticConsumption = staticConsumption
        self.staticDissipation = staticDissipation
        self.MARTE_HwLayout_HwComponent = MARTE_HwLayout_HwComponent if MARTE_HwLayout_HwComponent is not None else set()
        self.MARTE_HwLayout_HwComponent238 = MARTE_HwLayout_HwComponent238 if MARTE_HwLayout_HwComponent238 is not None else set()
        
        pass
    @property
    def r_Conditions(self):
        return self.__r_Conditions

    @r_Conditions.setter
    def r_Conditions(self, r_Conditions: str):
        self.__r_Conditions = r_Conditions


    @property
    def grid(self):
        return self.__grid

    @grid.setter
    def grid(self, grid: str):
        self.__grid = grid


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def staticDissipation(self):
        return self.__staticDissipation

    @staticDissipation.setter
    def staticDissipation(self, staticDissipation: str):
        self.__staticDissipation = staticDissipation


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def nbPins(self):
        return self.__nbPins

    @nbPins.setter
    def nbPins(self, nbPins: str):
        self.__nbPins = nbPins


    @property
    def staticConsumption(self):
        return self.__staticConsumption

    @staticConsumption.setter
    def staticConsumption(self, staticConsumption: str):
        self.__staticConsumption = staticConsumption


    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area: str):
        self.__area = area


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price


    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions


    @property
    def MARTE_HwLayout_HwComponent238(self):
        return self.__MARTE_HwLayout_HwComponent238

    @MARTE_HwLayout_HwComponent238.setter
    def MARTE_HwLayout_HwComponent238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent238", None)
        self.__MARTE_HwLayout_HwComponent238 = value if value is not None else set()
        
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
                if hasattr(item, "HwGeneral_HwResourceService236"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService236", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResourceService236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResourceService236"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService236", None)
                    
                    setattr(item, "HwGeneral_HwResourceService236", self)
                    

class MARTE_HwComputing_HwISA(HwResource):

    def __init__(self, family: str, inst_Width: str, type: str):
        self.family = family
        self.inst_Width = inst_Width
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family: str):
        self.__family = family


    @property
    def inst_Width(self):
        return self.__inst_Width

    @inst_Width.setter
    def inst_Width(self, inst_Width: str):
        self.__inst_Width = inst_Width


class HwGeneral_HwResource:

    pass
class MARTE_HwTiming_HwTimingResource(GRM_TimingResource, HwGeneral_HwResource):

    pass
class MARTE_HwStorageManager_HwStorageManager(HwGeneral_HwResource, GRM_StorageResource):

    pass
class MARTE_HwDevice_HwDevice(HwGeneral_HwResource, GRM_DeviceResource):

    pass
class MARTE_HwMemory_HwMemory(HwGeneral_HwResource, GRM_StorageResource):

    def __init__(self, memorySize: str, adressSize: str, timings: str, throughput: str, HwGeneral_HwResource: "MARTE_HwGeneral_HwResource" = None):
        self.memorySize = memorySize
        self.adressSize = adressSize
        self.timings = timings
        self.throughput = throughput
        
        pass
    @property
    def throughput(self):
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput


    @property
    def timings(self):
        return self.__timings

    @timings.setter
    def timings(self, timings: str):
        self.__timings = timings


    @property
    def adressSize(self):
        return self.__adressSize

    @adressSize.setter
    def adressSize(self, adressSize: str):
        self.__adressSize = adressSize


    @property
    def memorySize(self):
        return self.__memorySize

    @memorySize.setter
    def memorySize(self, memorySize: str):
        self.__memorySize = memorySize


class MARTE_HwComputing_HwComputingResource(HwGeneral_HwResource, GRM_ComputingResource):

    def __init__(self, op_Frequencies: str, HwGeneral_HwResource: "MARTE_HwGeneral_HwResource" = None, GRM_ComputingResource: "MARTE_GRM_Scheduler" = None):
        self.op_Frequencies = op_Frequencies
        
        pass
    @property
    def op_Frequencies(self):
        return self.__op_Frequencies

    @op_Frequencies.setter
    def op_Frequencies(self, op_Frequencies: str):
        self.__op_Frequencies = op_Frequencies


class HwCommunication_HwMedia:

    pass
class HwCommunicationResource:

    pass
class MARTE_HwCommunication_HwArbiter(HwCommunicationResource):

    pass
class HwMemory_HwCache:

    pass
class HwComputing_HwBranchPredictor:

    pass
class HwComputing_HwISA:

    pass
class HwComputingResource:

    pass
class MARTE_HwComputing_HwPLD(HwComputingResource):

    def __init__(self, technology: str, organization: str, nbLUTs: str, ndLUT_Inputs: str, nbFlipFlops: str, MARTE_HwComputing_HwPLD: set["HwMemory_HwRAM"] = None, MARTE_HwComputing_HwPLD214: set["HwComputing_HwComputingResource"] = None):
        self.technology = technology
        self.organization = organization
        self.nbLUTs = nbLUTs
        self.ndLUT_Inputs = ndLUT_Inputs
        self.nbFlipFlops = nbFlipFlops
        self.MARTE_HwComputing_HwPLD = MARTE_HwComputing_HwPLD if MARTE_HwComputing_HwPLD is not None else set()
        self.MARTE_HwComputing_HwPLD214 = MARTE_HwComputing_HwPLD214 if MARTE_HwComputing_HwPLD214 is not None else set()
        
        pass
    @property
    def ndLUT_Inputs(self):
        return self.__ndLUT_Inputs

    @ndLUT_Inputs.setter
    def ndLUT_Inputs(self, ndLUT_Inputs: str):
        self.__ndLUT_Inputs = ndLUT_Inputs


    @property
    def technology(self):
        return self.__technology

    @technology.setter
    def technology(self, technology: str):
        self.__technology = technology


    @property
    def nbFlipFlops(self):
        return self.__nbFlipFlops

    @nbFlipFlops.setter
    def nbFlipFlops(self, nbFlipFlops: str):
        self.__nbFlipFlops = nbFlipFlops


    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization


    @property
    def nbLUTs(self):
        return self.__nbLUTs

    @nbLUTs.setter
    def nbLUTs(self, nbLUTs: str):
        self.__nbLUTs = nbLUTs


    @property
    def MARTE_HwComputing_HwPLD214(self):
        return self.__MARTE_HwComputing_HwPLD214

    @MARTE_HwComputing_HwPLD214.setter
    def MARTE_HwComputing_HwPLD214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD214", None)
        self.__MARTE_HwComputing_HwPLD214 = value if value is not None else set()
        
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
    def MARTE_HwComputing_HwPLD(self):
        return self.__MARTE_HwComputing_HwPLD

    @MARTE_HwComputing_HwPLD.setter
    def MARTE_HwComputing_HwPLD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD", None)
        self.__MARTE_HwComputing_HwPLD = value if value is not None else set()
        
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
                    

class MARTE_HwComputing_HwASIC(HwComputingResource):

    pass
class MARTE_HwComputing_HwProcessor(HwComputingResource):

    def __init__(self, architecture: str, mips: str, ipc: str, nbCores: str, nbPipelines: str, nbStages: str, nbALUs: str, nbFPUs: str, MARTE_HwComputing_HwProcessor207: set["HwComputing_HwBranchPredictor"] = None, MARTE_HwComputing_HwProcessor209: set["HwMemory_HwCache"] = None, MARTE_HwComputing_HwProcessor211: set["HwStorageManager_HwMMU"] = None, MARTE_HwComputing_HwProcessor: set["HwComputing_HwISA"] = None):
        self.architecture = architecture
        self.mips = mips
        self.ipc = ipc
        self.nbCores = nbCores
        self.nbPipelines = nbPipelines
        self.nbStages = nbStages
        self.nbALUs = nbALUs
        self.nbFPUs = nbFPUs
        self.MARTE_HwComputing_HwProcessor207 = MARTE_HwComputing_HwProcessor207 if MARTE_HwComputing_HwProcessor207 is not None else set()
        self.MARTE_HwComputing_HwProcessor209 = MARTE_HwComputing_HwProcessor209 if MARTE_HwComputing_HwProcessor209 is not None else set()
        self.MARTE_HwComputing_HwProcessor211 = MARTE_HwComputing_HwProcessor211 if MARTE_HwComputing_HwProcessor211 is not None else set()
        self.MARTE_HwComputing_HwProcessor = MARTE_HwComputing_HwProcessor if MARTE_HwComputing_HwProcessor is not None else set()
        
        pass
    @property
    def mips(self):
        return self.__mips

    @mips.setter
    def mips(self, mips: str):
        self.__mips = mips


    @property
    def nbFPUs(self):
        return self.__nbFPUs

    @nbFPUs.setter
    def nbFPUs(self, nbFPUs: str):
        self.__nbFPUs = nbFPUs


    @property
    def ipc(self):
        return self.__ipc

    @ipc.setter
    def ipc(self, ipc: str):
        self.__ipc = ipc


    @property
    def nbALUs(self):
        return self.__nbALUs

    @nbALUs.setter
    def nbALUs(self, nbALUs: str):
        self.__nbALUs = nbALUs


    @property
    def nbCores(self):
        return self.__nbCores

    @nbCores.setter
    def nbCores(self, nbCores: str):
        self.__nbCores = nbCores


    @property
    def nbStages(self):
        return self.__nbStages

    @nbStages.setter
    def nbStages(self, nbStages: str):
        self.__nbStages = nbStages


    @property
    def architecture(self):
        return self.__architecture

    @architecture.setter
    def architecture(self, architecture: str):
        self.__architecture = architecture


    @property
    def nbPipelines(self):
        return self.__nbPipelines

    @nbPipelines.setter
    def nbPipelines(self, nbPipelines: str):
        self.__nbPipelines = nbPipelines


    @property
    def MARTE_HwComputing_HwProcessor(self):
        return self.__MARTE_HwComputing_HwProcessor

    @MARTE_HwComputing_HwProcessor.setter
    def MARTE_HwComputing_HwProcessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwProcessor__MARTE_HwComputing_HwProcessor", None)
        self.__MARTE_HwComputing_HwProcessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwComputing_HwISA"):
                    opp_val = getattr(item, "HwComputing_HwISA", None)
                    
                    if opp_val == self:
                        setattr(item, "HwComputing_HwISA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwComputing_HwISA"):
                    opp_val = getattr(item, "HwComputing_HwISA", None)
                    
                    setattr(item, "HwComputing_HwISA", self)
                    

    @property
    def MARTE_HwComputing_HwProcessor211(self):
        return self.__MARTE_HwComputing_HwProcessor211

    @MARTE_HwComputing_HwProcessor211.setter
    def MARTE_HwComputing_HwProcessor211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwProcessor__MARTE_HwComputing_HwProcessor211", None)
        self.__MARTE_HwComputing_HwProcessor211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwStorageManager_HwMMU"):
                    opp_val = getattr(item, "HwStorageManager_HwMMU", None)
                    
                    if opp_val == self:
                        setattr(item, "HwStorageManager_HwMMU", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwStorageManager_HwMMU"):
                    opp_val = getattr(item, "HwStorageManager_HwMMU", None)
                    
                    setattr(item, "HwStorageManager_HwMMU", self)
                    

    @property
    def MARTE_HwComputing_HwProcessor209(self):
        return self.__MARTE_HwComputing_HwProcessor209

    @MARTE_HwComputing_HwProcessor209.setter
    def MARTE_HwComputing_HwProcessor209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwProcessor__MARTE_HwComputing_HwProcessor209", None)
        self.__MARTE_HwComputing_HwProcessor209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwMemory_HwCache"):
                    opp_val = getattr(item, "HwMemory_HwCache", None)
                    
                    if opp_val == self:
                        setattr(item, "HwMemory_HwCache", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwMemory_HwCache"):
                    opp_val = getattr(item, "HwMemory_HwCache", None)
                    
                    setattr(item, "HwMemory_HwCache", self)
                    

    @property
    def MARTE_HwComputing_HwProcessor207(self):
        return self.__MARTE_HwComputing_HwProcessor207

    @MARTE_HwComputing_HwProcessor207.setter
    def MARTE_HwComputing_HwProcessor207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwProcessor__MARTE_HwComputing_HwProcessor207", None)
        self.__MARTE_HwComputing_HwProcessor207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwComputing_HwBranchPredictor"):
                    opp_val = getattr(item, "HwComputing_HwBranchPredictor", None)
                    
                    if opp_val == self:
                        setattr(item, "HwComputing_HwBranchPredictor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwComputing_HwBranchPredictor"):
                    opp_val = getattr(item, "HwComputing_HwBranchPredictor", None)
                    
                    setattr(item, "HwComputing_HwBranchPredictor", self)
                    

class HwStorageManager_HwMMU:

    pass
class MARTE_HLAM_RtService:

    def __init__(self, concPolicy: str, exeKind: str, isAtomic: str, synchKind: str, MARTE_HLAM_RtService: "HLAM_MARTE_BehavioralFeature" = None):
        self.concPolicy = concPolicy
        self.exeKind = exeKind
        self.isAtomic = isAtomic
        self.synchKind = synchKind
        self.MARTE_HLAM_RtService = MARTE_HLAM_RtService
        
        pass
    @property
    def synchKind(self):
        return self.__synchKind

    @synchKind.setter
    def synchKind(self, synchKind: str):
        self.__synchKind = synchKind


    @property
    def isAtomic(self):
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic


    @property
    def concPolicy(self):
        return self.__concPolicy

    @concPolicy.setter
    def concPolicy(self, concPolicy: str):
        self.__concPolicy = concPolicy


    @property
    def exeKind(self):
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
            if hasattr(old_value, "HLAM_MARTE_BehavioralFeature204"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioralFeature204", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioralFeature204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioralFeature204"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioralFeature204", None)
                setattr(value, "HLAM_MARTE_BehavioralFeature204", self)

class MARTE_HLAM_RtAction:

    def __init__(self, isAtomic: str, synchKind: str, msgSize: str, MARTE_HLAM_RtAction: "HLAM_MARTE_BehavioralFeature" = None, MARTE_HLAM_RtAction201: "HLAM_MARTE_InvocationAction" = None):
        self.isAtomic = isAtomic
        self.synchKind = synchKind
        self.msgSize = msgSize
        self.MARTE_HLAM_RtAction = MARTE_HLAM_RtAction
        self.MARTE_HLAM_RtAction201 = MARTE_HLAM_RtAction201
        
        pass
    @property
    def synchKind(self):
        return self.__synchKind

    @synchKind.setter
    def synchKind(self, synchKind: str):
        self.__synchKind = synchKind


    @property
    def isAtomic(self):
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic


    @property
    def msgSize(self):
        return self.__msgSize

    @msgSize.setter
    def msgSize(self, msgSize: str):
        self.__msgSize = msgSize


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
            if hasattr(old_value, "HLAM_MARTE_BehavioralFeature199"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioralFeature199", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioralFeature199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioralFeature199"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioralFeature199", None)
                setattr(value, "HLAM_MARTE_BehavioralFeature199", self)

    @property
    def MARTE_HLAM_RtAction201(self):
        return self.__MARTE_HLAM_RtAction201

    @MARTE_HLAM_RtAction201.setter
    def MARTE_HLAM_RtAction201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtAction__MARTE_HLAM_RtAction201", None)
        self.__MARTE_HLAM_RtAction201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_InvocationAction202"):
                opp_val = getattr(old_value, "HLAM_MARTE_InvocationAction202", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_InvocationAction202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_InvocationAction202"):
                opp_val = getattr(value, "HLAM_MARTE_InvocationAction202", None)
                setattr(value, "HLAM_MARTE_InvocationAction202", self)

class HLAM_MARTE_Comment:

    pass
class Time_TimedInstantObservation:

    pass
class MARTE_HLAM_RtSpecification:

    def __init__(self, relDl: str, absDl: str, utility: str, occKind: str, boundDl: str, rdTime: str, miss: str, priority: str, MARTE_HLAM_RtSpecification: "Time_TimedInstantObservation" = None, MARTE_HLAM_RtSpecification194: "HLAM_MARTE_Comment" = None, MARTE_HLAM_RtSpecification196: "HLAM_MARTE_BehavioralFeature" = None):
        self.relDl = relDl
        self.absDl = absDl
        self.utility = utility
        self.occKind = occKind
        self.boundDl = boundDl
        self.rdTime = rdTime
        self.miss = miss
        self.priority = priority
        self.MARTE_HLAM_RtSpecification = MARTE_HLAM_RtSpecification
        self.MARTE_HLAM_RtSpecification194 = MARTE_HLAM_RtSpecification194
        self.MARTE_HLAM_RtSpecification196 = MARTE_HLAM_RtSpecification196
        
        pass
    @property
    def absDl(self):
        return self.__absDl

    @absDl.setter
    def absDl(self, absDl: str):
        self.__absDl = absDl


    @property
    def rdTime(self):
        return self.__rdTime

    @rdTime.setter
    def rdTime(self, rdTime: str):
        self.__rdTime = rdTime


    @property
    def utility(self):
        return self.__utility

    @utility.setter
    def utility(self, utility: str):
        self.__utility = utility


    @property
    def relDl(self):
        return self.__relDl

    @relDl.setter
    def relDl(self, relDl: str):
        self.__relDl = relDl


    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority


    @property
    def miss(self):
        return self.__miss

    @miss.setter
    def miss(self, miss: str):
        self.__miss = miss


    @property
    def occKind(self):
        return self.__occKind

    @occKind.setter
    def occKind(self, occKind: str):
        self.__occKind = occKind


    @property
    def boundDl(self):
        return self.__boundDl

    @boundDl.setter
    def boundDl(self, boundDl: str):
        self.__boundDl = boundDl


    @property
    def MARTE_HLAM_RtSpecification194(self):
        return self.__MARTE_HLAM_RtSpecification194

    @MARTE_HLAM_RtSpecification194.setter
    def MARTE_HLAM_RtSpecification194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtSpecification__MARTE_HLAM_RtSpecification194", None)
        self.__MARTE_HLAM_RtSpecification194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_Comment"):
                opp_val = getattr(old_value, "HLAM_MARTE_Comment", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_Comment"):
                opp_val = getattr(value, "HLAM_MARTE_Comment", None)
                setattr(value, "HLAM_MARTE_Comment", self)

    @property
    def MARTE_HLAM_RtSpecification(self):
        return self.__MARTE_HLAM_RtSpecification

    @MARTE_HLAM_RtSpecification.setter
    def MARTE_HLAM_RtSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtSpecification__MARTE_HLAM_RtSpecification", None)
        self.__MARTE_HLAM_RtSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time_TimedInstantObservation"):
                opp_val = getattr(old_value, "Time_TimedInstantObservation", None)
                if opp_val == self:
                    setattr(old_value, "Time_TimedInstantObservation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time_TimedInstantObservation"):
                opp_val = getattr(value, "Time_TimedInstantObservation", None)
                setattr(value, "Time_TimedInstantObservation", self)

    @property
    def MARTE_HLAM_RtSpecification196(self):
        return self.__MARTE_HLAM_RtSpecification196

    @MARTE_HLAM_RtSpecification196.setter
    def MARTE_HLAM_RtSpecification196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtSpecification__MARTE_HLAM_RtSpecification196", None)
        self.__MARTE_HLAM_RtSpecification196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_BehavioralFeature197"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioralFeature197", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioralFeature197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioralFeature197"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioralFeature197", None)
                setattr(value, "HLAM_MARTE_BehavioralFeature197", self)

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
class MARTE_HLAM_PpUnit:

    def __init__(self, concPolicy: str, memorySize: str, MARTE_HLAM_PpUnit: "HLAM_MARTE_BehavioredClassifier" = None):
        self.concPolicy = concPolicy
        self.memorySize = memorySize
        self.MARTE_HLAM_PpUnit = MARTE_HLAM_PpUnit
        
        pass
    @property
    def concPolicy(self):
        return self.__concPolicy

    @concPolicy.setter
    def concPolicy(self, concPolicy: str):
        self.__concPolicy = concPolicy


    @property
    def memorySize(self):
        return self.__memorySize

    @memorySize.setter
    def memorySize(self, memorySize: str):
        self.__memorySize = memorySize


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
            if hasattr(old_value, "HLAM_MARTE_BehavioredClassifier180"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioredClassifier180", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioredClassifier180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioredClassifier180"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioredClassifier180", None)
                setattr(value, "HLAM_MARTE_BehavioredClassifier180", self)

class HLAM_MARTE_Operation:

    pass
class HLAM_MARTE_Behavior:

    pass
class MARTE_HLAM_RtUnit:

    def __init__(self, queueSchedPolicy: str, isDynamic: str, isMain: str, srPoolSize: str, srPoolPolicy: str, srPoolWaitingTime: str, memorySize: str, queueSize: str, msgMaxSize: str, MARTE_HLAM_RtUnit178: "HLAM_MARTE_BehavioredClassifier" = None, MARTE_HLAM_RtUnit: "HLAM_MARTE_Behavior" = None, MARTE_HLAM_RtUnit176: "HLAM_MARTE_Operation" = None):
        self.queueSchedPolicy = queueSchedPolicy
        self.isDynamic = isDynamic
        self.isMain = isMain
        self.srPoolSize = srPoolSize
        self.srPoolPolicy = srPoolPolicy
        self.srPoolWaitingTime = srPoolWaitingTime
        self.memorySize = memorySize
        self.queueSize = queueSize
        self.msgMaxSize = msgMaxSize
        self.MARTE_HLAM_RtUnit178 = MARTE_HLAM_RtUnit178
        self.MARTE_HLAM_RtUnit = MARTE_HLAM_RtUnit
        self.MARTE_HLAM_RtUnit176 = MARTE_HLAM_RtUnit176
        
        pass
    @property
    def srPoolPolicy(self):
        return self.__srPoolPolicy

    @srPoolPolicy.setter
    def srPoolPolicy(self, srPoolPolicy: str):
        self.__srPoolPolicy = srPoolPolicy


    @property
    def srPoolSize(self):
        return self.__srPoolSize

    @srPoolSize.setter
    def srPoolSize(self, srPoolSize: str):
        self.__srPoolSize = srPoolSize


    @property
    def msgMaxSize(self):
        return self.__msgMaxSize

    @msgMaxSize.setter
    def msgMaxSize(self, msgMaxSize: str):
        self.__msgMaxSize = msgMaxSize


    @property
    def isDynamic(self):
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic


    @property
    def queueSize(self):
        return self.__queueSize

    @queueSize.setter
    def queueSize(self, queueSize: str):
        self.__queueSize = queueSize


    @property
    def queueSchedPolicy(self):
        return self.__queueSchedPolicy

    @queueSchedPolicy.setter
    def queueSchedPolicy(self, queueSchedPolicy: str):
        self.__queueSchedPolicy = queueSchedPolicy


    @property
    def isMain(self):
        return self.__isMain

    @isMain.setter
    def isMain(self, isMain: str):
        self.__isMain = isMain


    @property
    def memorySize(self):
        return self.__memorySize

    @memorySize.setter
    def memorySize(self, memorySize: str):
        self.__memorySize = memorySize


    @property
    def srPoolWaitingTime(self):
        return self.__srPoolWaitingTime

    @srPoolWaitingTime.setter
    def srPoolWaitingTime(self, srPoolWaitingTime: str):
        self.__srPoolWaitingTime = srPoolWaitingTime


    @property
    def MARTE_HLAM_RtUnit176(self):
        return self.__MARTE_HLAM_RtUnit176

    @MARTE_HLAM_RtUnit176.setter
    def MARTE_HLAM_RtUnit176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit176", None)
        self.__MARTE_HLAM_RtUnit176 = value
        
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
            if hasattr(old_value, "HLAM_MARTE_Behavior"):
                opp_val = getattr(old_value, "HLAM_MARTE_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_Behavior"):
                opp_val = getattr(value, "HLAM_MARTE_Behavior", None)
                setattr(value, "HLAM_MARTE_Behavior", self)

    @property
    def MARTE_HLAM_RtUnit178(self):
        return self.__MARTE_HLAM_RtUnit178

    @MARTE_HLAM_RtUnit178.setter
    def MARTE_HLAM_RtUnit178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit178", None)
        self.__MARTE_HLAM_RtUnit178 = value
        
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

class MARTE_DataTypes_TupleType:

    pass
class MARTE_DataTypes_ChoiceType:

    pass
class MARTE_DataTypes_CollectionType:

    pass
class HLAM_MARTE_BehavioredClassifier:

    pass
class MARTE_DataTypes_IntervalType:

    pass
class DataTypes_MARTE_DataType:

    pass