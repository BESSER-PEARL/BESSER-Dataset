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
class OptimallityCriterionKind(Enum):
    meetHardDeadlines = "meetHardDeadlines"
    minimizeMissedDeadlines = "minimizeMissedDeadlines"
    minimizedMeanTardiness = "minimizedMeanTardiness"
    undef = "undef"
    other = "other"
class AssignmentNature(Enum):
    spatialDistribution = "spatialDistribution"
    timeScheduling = "timeScheduling"
class QueuePolicyKind(Enum):
    FIFO = "FIFO"
    LIFO = "LIFO"
    Priority = "Priority"
    Undef = "Undef"
    Other = "Other"
class PoolMgtPolicyKind(Enum):
    infiniteWait = "infiniteWait"
    timedWait = "timedWait"
    dynamic = "dynamic"
    exception = "exception"
    other = "other"
class PortSpecificationKind(Enum):
    atomic = "atomic"
    interfaceBased = "interfaceBased"
    featureBased = "featureBased"
class WritePolicy(Enum):
    writeBack = "writeBack"
    writeThrough = "writeThrough"
    other = "other"
    undef = "undef"
class AllocationEndKind(Enum):
    undef = "undef"
    application = "application"
    executionPlatform = "executionPlatform"
    both = "both"
class AllocationKind(Enum):
    structural = "structural"
    behavioral = "behavioral"
    hybrid = "hybrid"
class PLD_Class(Enum):
    symetricalArray = "symetricalArray"
    rowBased = "rowBased"
    seaOfGates = "seaOfGates"
    hierarchicalPLD = "hierarchicalPLD"
    other = "other"
    undef = "undef"
class AssignmentKind(Enum):
    structural = "structural"
    behavioral = "behavioral"
    hybrid = "hybrid"
class InterruptKind(Enum):
    HardwareInterruption = "HardwareInterruption"
    ProcessorDetectedException = "ProcessorDetectedException"
    ProgrammedException = "ProgrammedException"
    Undef = "Undef"
    Other = "Other"
class ComponentState(Enum):
    operating = "operating"
    storage = "storage"
    other = "other"
    undef = "undef"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"
class PLD_Technology(Enum):
    SRAM = "SRAM"
    antifuse = "antifuse"
    flash = "flash"
    other = "other"
    undef = "undef"
class ConcurrencyKind(Enum):
    reader = "reader"
    writer = "writer"
    parallel = "parallel"
class ISA_Type(Enum):
    RISC = "RISC"
    CISC = "CISC"
    VLIW = "VLIW"
    SIMD = "SIMD"
    other = "other"
    undef = "undef"
class ConstraintKind(Enum):
    required = "required"
    offered = "offered"
    contract = "contract"
class MessageResourceKind(Enum):
    MessageQueue = "MessageQueue"
    Pipe = "Pipe"
    Blackboard = "Blackboard"
    Undef = "Undef"
    Other = "Other"
class AllocationNature(Enum):
    spatialDistribution = "spatialDistribution"
    timeScheduling = "timeScheduling"
class LaxityKind(Enum):
    hard = "hard"
    soft = "soft"
    other = "other"
class ComponentKind(Enum):
    port = "port"
    unit = "unit"
    other = "other"
    undef = "undef"
    card = "card"
    channel = "channel"
    chip = "chip"
class MutualExclusionResourceKind(Enum):
    BooleanSemaphore = "BooleanSemaphore"
    CountSemaphore = "CountSemaphore"
    Mutex = "Mutex"
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
class ClientServerKind(Enum):
    required = "required"
    provided = "provided"
    proreq = "proreq"
class SynchronizationKind(Enum):
    synchronous = "synchronous"
    asynchronous = "asynchronous"
    delayedSynchronous = "delayedSynchronous"
    rendezVous = "rendezVous"
    other = "other"
class ExecutionKind(Enum):
    deferred = "deferred"
    remoteImmediate = "remoteImmediate"
    localImmediate = "localImmediate"
class NotificationResourceKind(Enum):
    Undef = "Undef"
    Other = "Other"
    Event = "Event"
    Barrier = "Barrier"
class AccessPolicyKind(Enum):
    Read = "Read"
    Write = "Write"
    ReadWrite = "ReadWrite"
    Undef = "Undef"
    Other = "Other"
class FlowDirectionKind(Enum):
    in = "in"
    out = "out"
    inout = "inout"
class CacheType(Enum):
    data = "data"
    instruction = "instruction"
    unified = "unified"
    other = "other"
    undef = "undef"
class dummy(Enum):
class ConcurrentAccessProtocolKind(Enum):
    PIP = "PIP"
    PCP = "PCP"
    NoPreemption = "NoPreemption"
    Undef = "Undef"
    Other = "Other"
class DataPoolOrderingKind(Enum):
    FIFO = "FIFO"
    LIFO = "LIFO"
    UserDefined = "UserDefined"
class NotificationKind(Enum):
    Memorized = "Memorized"
    Bounded = "Bounded"
    Memoryless = "Memoryless"
    Undef = "Undef"
    Other = "Other"
class Repl_Policy(Enum):
    LRU = "LRU"
    NFU = "NFU"
    FIFO = "FIFO"
    random = "random"
    other = "other"
    undef = "undef"
class VariableDirectionKind(Enum):
    in = "in"
    out = "out"
    inout = "inout"


############################################
# Definition of Classes
############################################

class PAM_MARTE_NamedElement:

    pass
class GQAM_GaCommStep:

    pass
class PAM_PaStep:

    pass
class MARTE_PAM_PaCommStep(PAM_PaStep, GQAM_GaCommStep):

    pass
class MARTE_PAM_PaRunTInstance:

    def __init__(self, poolSize: str, unbddPool: str, utilization: str, throughput: str, MARTE_PAM_PaRunTInstance: "GRM_SchedulableResource" = None, MARTE_PAM_PaRunTInstance550: "GQAM_GaExecHost" = None, MARTE_PAM_PaRunTInstance553: "PAM_MARTE_NamedElement" = None):
        self.poolSize = poolSize
        self.unbddPool = unbddPool
        self.utilization = utilization
        self.throughput = throughput
        self.MARTE_PAM_PaRunTInstance = MARTE_PAM_PaRunTInstance
        self.MARTE_PAM_PaRunTInstance550 = MARTE_PAM_PaRunTInstance550
        self.MARTE_PAM_PaRunTInstance553 = MARTE_PAM_PaRunTInstance553
        
    @property
    def unbddPool(self) -> str:
        return self.__unbddPool

    @unbddPool.setter
    def unbddPool(self, unbddPool: str):
        self.__unbddPool = unbddPool

    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def poolSize(self) -> str:
        return self.__poolSize

    @poolSize.setter
    def poolSize(self, poolSize: str):
        self.__poolSize = poolSize

    @property
    def utilization(self) -> str:
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization

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
            if hasattr(old_value, "GRM_SchedulableResource548"):
                opp_val = getattr(old_value, "GRM_SchedulableResource548", None)
                if opp_val == self:
                    setattr(old_value, "GRM_SchedulableResource548", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_SchedulableResource548"):
                opp_val = getattr(value, "GRM_SchedulableResource548", None)
                setattr(value, "GRM_SchedulableResource548", self)

    @property
    def MARTE_PAM_PaRunTInstance553(self):
        return self.__MARTE_PAM_PaRunTInstance553

    @MARTE_PAM_PaRunTInstance553.setter
    def MARTE_PAM_PaRunTInstance553(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance553", None)
        self.__MARTE_PAM_PaRunTInstance553 = value
        
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
    def MARTE_PAM_PaRunTInstance550(self):
        return self.__MARTE_PAM_PaRunTInstance550

    @MARTE_PAM_PaRunTInstance550.setter
    def MARTE_PAM_PaRunTInstance550(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance550", None)
        self.__MARTE_PAM_PaRunTInstance550 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_GaExecHost551"):
                opp_val = getattr(old_value, "GQAM_GaExecHost551", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_GaExecHost551", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_GaExecHost551"):
                opp_val = getattr(value, "GQAM_GaExecHost551", None)
                setattr(value, "GQAM_GaExecHost551", self)

class GaCommHost:

    pass
class MARTE_SAM_SaCommHost(GaCommHost):

    def __init__(self, isSched: str, schSlack: str):
        self.isSched = isSched
        self.schSlack = schSlack
        
    @property
    def isSched(self) -> str:
        return self.__isSched

    @isSched.setter
    def isSched(self, isSched: str):
        self.__isSched = isSched

    @property
    def schSlack(self) -> str:
        return self.__schSlack

    @schSlack.setter
    def schSlack(self, schSlack: str):
        self.__schSlack = schSlack

class MutualExclusionResource:

    pass
class MARTE_SAM_SaSharedResource(MutualExclusionResource):

    def __init__(self, capacity: str, isPreemp: str, isConsum: str, acquisT: str, releaseT: str):
        self.capacity = capacity
        self.isPreemp = isPreemp
        self.isConsum = isConsum
        self.acquisT = acquisT
        self.releaseT = releaseT
        
    @property
    def isConsum(self) -> str:
        return self.__isConsum

    @isConsum.setter
    def isConsum(self, isConsum: str):
        self.__isConsum = isConsum

    @property
    def acquisT(self) -> str:
        return self.__acquisT

    @acquisT.setter
    def acquisT(self, acquisT: str):
        self.__acquisT = acquisT

    @property
    def releaseT(self) -> str:
        return self.__releaseT

    @releaseT.setter
    def releaseT(self, releaseT: str):
        self.__releaseT = releaseT

    @property
    def capacity(self) -> str:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity

    @property
    def isPreemp(self) -> str:
        return self.__isPreemp

    @isPreemp.setter
    def isPreemp(self, isPreemp: str):
        self.__isPreemp = isPreemp

class GaExecHost:

    pass
class MARTE_SAM_SaExecHost(GaExecHost):

    def __init__(self, isSched: str, schSlack: str, schedUtiliz: str, ISRswitchT: str, ISRprioRange: str):
        self.isSched = isSched
        self.schSlack = schSlack
        self.schedUtiliz = schedUtiliz
        self.ISRswitchT = ISRswitchT
        self.ISRprioRange = ISRprioRange
        
    @property
    def ISRprioRange(self) -> str:
        return self.__ISRprioRange

    @ISRprioRange.setter
    def ISRprioRange(self, ISRprioRange: str):
        self.__ISRprioRange = ISRprioRange

    @property
    def isSched(self) -> str:
        return self.__isSched

    @isSched.setter
    def isSched(self, isSched: str):
        self.__isSched = isSched

    @property
    def schSlack(self) -> str:
        return self.__schSlack

    @schSlack.setter
    def schSlack(self, schSlack: str):
        self.__schSlack = schSlack

    @property
    def ISRswitchT(self) -> str:
        return self.__ISRswitchT

    @ISRswitchT.setter
    def ISRswitchT(self, ISRswitchT: str):
        self.__ISRswitchT = ISRswitchT

    @property
    def schedUtiliz(self) -> str:
        return self.__schedUtiliz

    @schedUtiliz.setter
    def schedUtiliz(self, schedUtiliz: str):
        self.__schedUtiliz = schedUtiliz

class SAM_SaSharedResource:

    pass
class SAM_MARTE_NamedElement:

    pass
class SAM_MARTE_BehavioralFeature:

    pass
class GaCommStep:

    pass
class MARTE_SAM_SaCommStep(GaCommStep):

    def __init__(self, deadline: str, spareCap: str, schSlack: str, MARTE_SAM_SaCommStep: "SAM_MARTE_BehavioralFeature" = None):
        self.deadline = deadline
        self.spareCap = spareCap
        self.schSlack = schSlack
        self.MARTE_SAM_SaCommStep = MARTE_SAM_SaCommStep
        
    @property
    def spareCap(self) -> str:
        return self.__spareCap

    @spareCap.setter
    def spareCap(self, spareCap: str):
        self.__spareCap = spareCap

    @property
    def deadline(self) -> str:
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: str):
        self.__deadline = deadline

    @property
    def schSlack(self) -> str:
        return self.__schSlack

    @schSlack.setter
    def schSlack(self, schSlack: str):
        self.__schSlack = schSlack

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

class MARTE_SAM_SaEndtoEndFlow:

    def __init__(self, isSched: str, schSlack: str, end2EndT: str, end2EndD: str, MARTE_SAM_SaEndtoEndFlow: set["GQAM_GaTimedObs"] = None, MARTE_SAM_SaEndtoEndFlow537: "SAM_MARTE_NamedElement" = None):
        self.isSched = isSched
        self.schSlack = schSlack
        self.end2EndT = end2EndT
        self.end2EndD = end2EndD
        self.MARTE_SAM_SaEndtoEndFlow = MARTE_SAM_SaEndtoEndFlow if MARTE_SAM_SaEndtoEndFlow is not None else set()
        self.MARTE_SAM_SaEndtoEndFlow537 = MARTE_SAM_SaEndtoEndFlow537
        
    @property
    def isSched(self) -> str:
        return self.__isSched

    @isSched.setter
    def isSched(self, isSched: str):
        self.__isSched = isSched

    @property
    def end2EndD(self) -> str:
        return self.__end2EndD

    @end2EndD.setter
    def end2EndD(self, end2EndD: str):
        self.__end2EndD = end2EndD

    @property
    def schSlack(self) -> str:
        return self.__schSlack

    @schSlack.setter
    def schSlack(self, schSlack: str):
        self.__schSlack = schSlack

    @property
    def end2EndT(self) -> str:
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
                if hasattr(item, "GQAM_GaTimedObs535"):
                    opp_val = getattr(item, "GQAM_GaTimedObs535", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_GaTimedObs535", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_GaTimedObs535"):
                    opp_val = getattr(item, "GQAM_GaTimedObs535", None)
                    
                    setattr(item, "GQAM_GaTimedObs535", self)
                    

    @property
    def MARTE_SAM_SaEndtoEndFlow537(self):
        return self.__MARTE_SAM_SaEndtoEndFlow537

    @MARTE_SAM_SaEndtoEndFlow537.setter
    def MARTE_SAM_SaEndtoEndFlow537(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SAM_SaEndtoEndFlow__MARTE_SAM_SaEndtoEndFlow537", None)
        self.__MARTE_SAM_SaEndtoEndFlow537 = value
        
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
        
    @property
    def optCriterion(self) -> str:
        return self.__optCriterion

    @optCriterion.setter
    def optCriterion(self, optCriterion: str):
        self.__optCriterion = optCriterion

    @property
    def isSched(self) -> str:
        return self.__isSched

    @isSched.setter
    def isSched(self, isSched: str):
        self.__isSched = isSched

class GQAM_MARTE_Classifier:

    pass
class SchedulableResource:

    pass
class MARTE_GQAM_GaCommChannel(SchedulableResource):

    def __init__(self, packetSize: str, utilization: str):
        self.packetSize = packetSize
        self.utilization = utilization
        
    @property
    def utilization(self) -> str:
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization

    @property
    def packetSize(self) -> str:
        return self.__packetSize

    @packetSize.setter
    def packetSize(self, packetSize: str):
        self.__packetSize = packetSize

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

    def __init__(self, context: str, MARTE_GQAM_GaAnalysisContext: set["GQAM_GaWorkloadBehavior"] = None, MARTE_GQAM_GaAnalysisContext529: set["GQAM_GaResourcesPlatform"] = None):
        self.context = context
        self.MARTE_GQAM_GaAnalysisContext = MARTE_GQAM_GaAnalysisContext if MARTE_GQAM_GaAnalysisContext is not None else set()
        self.MARTE_GQAM_GaAnalysisContext529 = MARTE_GQAM_GaAnalysisContext529 if MARTE_GQAM_GaAnalysisContext529 is not None else set()
        
    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

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
                    

    @property
    def MARTE_GQAM_GaAnalysisContext529(self):
        return self.__MARTE_GQAM_GaAnalysisContext529

    @MARTE_GQAM_GaAnalysisContext529.setter
    def MARTE_GQAM_GaAnalysisContext529(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaAnalysisContext__MARTE_GQAM_GaAnalysisContext529", None)
        self.__MARTE_GQAM_GaAnalysisContext529 = value if value is not None else set()
        
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
                    

class MARTE_GQAM_GaWorkloadBehavior:

    pass
class GaTimedObs:

    pass
class MARTE_SAM_SaSchedObs(GaTimedObs):

    def __init__(self, suspentions: str, blockT: str, overlaps: str):
        self.suspentions = suspentions
        self.blockT = blockT
        self.overlaps = overlaps
        
    @property
    def overlaps(self) -> str:
        return self.__overlaps

    @overlaps.setter
    def overlaps(self, overlaps: str):
        self.__overlaps = overlaps

    @property
    def suspentions(self) -> str:
        return self.__suspentions

    @suspentions.setter
    def suspentions(self, suspentions: str):
        self.__suspentions = suspentions

    @property
    def blockT(self) -> str:
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
        
    @property
    def utility(self) -> str:
        return self.__utility

    @utility.setter
    def utility(self, utility: str):
        self.__utility = utility

    @property
    def latency(self) -> str:
        return self.__latency

    @latency.setter
    def latency(self, latency: str):
        self.__latency = latency

    @property
    def maxJitter(self) -> str:
        return self.__maxJitter

    @maxJitter.setter
    def maxJitter(self, maxJitter: str):
        self.__maxJitter = maxJitter

    @property
    def miss(self) -> str:
        return self.__miss

    @miss.setter
    def miss(self, miss: str):
        self.__miss = miss

class GQAM_MARTE_TimeObservation:

    pass
class NfpConstraint:

    pass
class MARTE_GQAM_GaTimedObs(NfpConstraint):

    def __init__(self, laxity: str, MARTE_GQAM_GaTimedObs: set["GQAM_MARTE_TimeObservation"] = None, MARTE_GQAM_GaTimedObs513: set["GQAM_MARTE_TimeObservation"] = None):
        self.laxity = laxity
        self.MARTE_GQAM_GaTimedObs = MARTE_GQAM_GaTimedObs if MARTE_GQAM_GaTimedObs is not None else set()
        self.MARTE_GQAM_GaTimedObs513 = MARTE_GQAM_GaTimedObs513 if MARTE_GQAM_GaTimedObs513 is not None else set()
        
    @property
    def laxity(self) -> str:
        return self.__laxity

    @laxity.setter
    def laxity(self, laxity: str):
        self.__laxity = laxity

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
                    

    @property
    def MARTE_GQAM_GaTimedObs513(self):
        return self.__MARTE_GQAM_GaTimedObs513

    @MARTE_GQAM_GaTimedObs513.setter
    def MARTE_GQAM_GaTimedObs513(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaTimedObs__MARTE_GQAM_GaTimedObs513", None)
        self.__MARTE_GQAM_GaTimedObs513 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_MARTE_TimeObservation514"):
                    opp_val = getattr(item, "GQAM_MARTE_TimeObservation514", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_MARTE_TimeObservation514", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_MARTE_TimeObservation514"):
                    opp_val = getattr(item, "GQAM_MARTE_TimeObservation514", None)
                    
                    setattr(item, "GQAM_MARTE_TimeObservation514", self)
                    

class GQAM_MARTE_Operation:

    pass
class GaStep:

    pass
class MARTE_SAM_SaStep(GaStep):

    def __init__(self, deadline: str, spareCap: str, nonpreemptionBlocking: str, schSlack: str, selfSuspensionBlocking: str, numberSelfSuspensions: str, preemptT: str, readyT: str, MARTE_SAM_SaStep: "SAM_MARTE_BehavioralFeature" = None, MARTE_SAM_SaStep542: set["SAM_SaSharedResource"] = None):
        self.deadline = deadline
        self.spareCap = spareCap
        self.nonpreemptionBlocking = nonpreemptionBlocking
        self.schSlack = schSlack
        self.selfSuspensionBlocking = selfSuspensionBlocking
        self.numberSelfSuspensions = numberSelfSuspensions
        self.preemptT = preemptT
        self.readyT = readyT
        self.MARTE_SAM_SaStep = MARTE_SAM_SaStep
        self.MARTE_SAM_SaStep542 = MARTE_SAM_SaStep542 if MARTE_SAM_SaStep542 is not None else set()
        
    @property
    def deadline(self) -> str:
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: str):
        self.__deadline = deadline

    @property
    def readyT(self) -> str:
        return self.__readyT

    @readyT.setter
    def readyT(self, readyT: str):
        self.__readyT = readyT

    @property
    def nonpreemptionBlocking(self) -> str:
        return self.__nonpreemptionBlocking

    @nonpreemptionBlocking.setter
    def nonpreemptionBlocking(self, nonpreemptionBlocking: str):
        self.__nonpreemptionBlocking = nonpreemptionBlocking

    @property
    def schSlack(self) -> str:
        return self.__schSlack

    @schSlack.setter
    def schSlack(self, schSlack: str):
        self.__schSlack = schSlack

    @property
    def numberSelfSuspensions(self) -> str:
        return self.__numberSelfSuspensions

    @numberSelfSuspensions.setter
    def numberSelfSuspensions(self, numberSelfSuspensions: str):
        self.__numberSelfSuspensions = numberSelfSuspensions

    @property
    def spareCap(self) -> str:
        return self.__spareCap

    @spareCap.setter
    def spareCap(self, spareCap: str):
        self.__spareCap = spareCap

    @property
    def preemptT(self) -> str:
        return self.__preemptT

    @preemptT.setter
    def preemptT(self, preemptT: str):
        self.__preemptT = preemptT

    @property
    def selfSuspensionBlocking(self) -> str:
        return self.__selfSuspensionBlocking

    @selfSuspensionBlocking.setter
    def selfSuspensionBlocking(self, selfSuspensionBlocking: str):
        self.__selfSuspensionBlocking = selfSuspensionBlocking

    @property
    def MARTE_SAM_SaStep542(self):
        return self.__MARTE_SAM_SaStep542

    @MARTE_SAM_SaStep542.setter
    def MARTE_SAM_SaStep542(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SAM_SaStep__MARTE_SAM_SaStep542", None)
        self.__MARTE_SAM_SaStep542 = value if value is not None else set()
        
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
            if hasattr(old_value, "SAM_MARTE_BehavioralFeature540"):
                opp_val = getattr(old_value, "SAM_MARTE_BehavioralFeature540", None)
                if opp_val == self:
                    setattr(old_value, "SAM_MARTE_BehavioralFeature540", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAM_MARTE_BehavioralFeature540"):
                opp_val = getattr(value, "SAM_MARTE_BehavioralFeature540", None)
                setattr(value, "SAM_MARTE_BehavioralFeature540", self)

class MARTE_GQAM_GaAcqStep(GaStep):

    def __init__(self, resUnits: str, MARTE_GQAM_GaAcqStep: "GRM_Resource" = None):
        self.resUnits = resUnits
        self.MARTE_GQAM_GaAcqStep = MARTE_GQAM_GaAcqStep
        
    @property
    def resUnits(self) -> str:
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
            if hasattr(old_value, "GRM_Resource516"):
                opp_val = getattr(old_value, "GRM_Resource516", None)
                if opp_val == self:
                    setattr(old_value, "GRM_Resource516", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_Resource516"):
                opp_val = getattr(value, "GRM_Resource516", None)
                setattr(value, "GRM_Resource516", self)

class MARTE_GQAM_GaCommStep(GaStep):

    pass
class MARTE_PAM_PaStep(GaStep):

    def __init__(self, noSync: str, extOpDemand: str, extOpCount: str, behavCount: str, MARTE_PAM_PaStep: set["GQAM_GaScenario"] = None):
        self.noSync = noSync
        self.extOpDemand = extOpDemand
        self.extOpCount = extOpCount
        self.behavCount = behavCount
        self.MARTE_PAM_PaStep = MARTE_PAM_PaStep if MARTE_PAM_PaStep is not None else set()
        
    @property
    def extOpDemand(self) -> str:
        return self.__extOpDemand

    @extOpDemand.setter
    def extOpDemand(self, extOpDemand: str):
        self.__extOpDemand = extOpDemand

    @property
    def noSync(self) -> str:
        return self.__noSync

    @noSync.setter
    def noSync(self, noSync: str):
        self.__noSync = noSync

    @property
    def behavCount(self) -> str:
        return self.__behavCount

    @behavCount.setter
    def behavCount(self, behavCount: str):
        self.__behavCount = behavCount

    @property
    def extOpCount(self) -> str:
        return self.__extOpCount

    @extOpCount.setter
    def extOpCount(self, extOpCount: str):
        self.__extOpCount = extOpCount

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
                if hasattr(item, "GQAM_GaScenario544"):
                    opp_val = getattr(item, "GQAM_GaScenario544", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_GaScenario544", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_GaScenario544"):
                    opp_val = getattr(item, "GQAM_GaScenario544", None)
                    
                    setattr(item, "GQAM_GaScenario544", self)
                    

class MARTE_GQAM_GaRelStep(GaStep):

    def __init__(self, resUnits: str, MARTE_GQAM_GaRelStep: "GRM_Resource" = None):
        self.resUnits = resUnits
        self.MARTE_GQAM_GaRelStep = MARTE_GQAM_GaRelStep
        
    @property
    def resUnits(self) -> str:
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
            if hasattr(old_value, "GRM_Resource518"):
                opp_val = getattr(old_value, "GRM_Resource518", None)
                if opp_val == self:
                    setattr(old_value, "GRM_Resource518", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_Resource518"):
                opp_val = getattr(value, "GRM_Resource518", None)
                setattr(value, "GRM_Resource518", self)

class MARTE_PAM_PaResPassStep(GaStep):

    def __init__(self, resUnits: str, MARTE_PAM_PaResPassStep: "GRM_Resource" = None):
        self.resUnits = resUnits
        self.MARTE_PAM_PaResPassStep = MARTE_PAM_PaResPassStep
        
    @property
    def resUnits(self) -> str:
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
            if hasattr(old_value, "GRM_Resource546"):
                opp_val = getattr(old_value, "GRM_Resource546", None)
                if opp_val == self:
                    setattr(old_value, "GRM_Resource546", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_Resource546"):
                opp_val = getattr(value, "GRM_Resource546", None)
                setattr(value, "GRM_Resource546", self)

class MARTE_GQAM_GaRequestedService(GaStep):

    pass
class GQAM_GaExecHost:

    pass
class GQAM_GaRequestedService:

    pass
class MARTE_PAM_PaRequestedStep(GQAM_GaRequestedService, PAM_PaStep):

    pass
class GQAM_GaStep:

    pass
class GaScenario:

    pass
class MARTE_GQAM_GaStep(GaScenario):

    def __init__(self, isAtomic: str, blockT: str, rep: str, prob: str, servCount: str, selfDelay: str, priority: str, MARTE_GQAM_GaStep503: set["GQAM_GaRequestedService"] = None, GQAM505: "GQAM_GaScenario" = None, GQAM508: "GQAM_GaScenario" = None, MARTE_GQAM_GaStep: "GRM_SchedulableResource" = None, MARTE_GQAM_GaStep501: "GQAM_GaExecHost" = None):
        self.isAtomic = isAtomic
        self.blockT = blockT
        self.rep = rep
        self.prob = prob
        self.servCount = servCount
        self.selfDelay = selfDelay
        self.priority = priority
        self.MARTE_GQAM_GaStep503 = MARTE_GQAM_GaStep503 if MARTE_GQAM_GaStep503 is not None else set()
        self.GQAM505 = GQAM505
        self.GQAM508 = GQAM508
        self.MARTE_GQAM_GaStep = MARTE_GQAM_GaStep
        self.MARTE_GQAM_GaStep501 = MARTE_GQAM_GaStep501
        
    @property
    def rep(self) -> str:
        return self.__rep

    @rep.setter
    def rep(self, rep: str):
        self.__rep = rep

    @property
    def isAtomic(self) -> str:
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic

    @property
    def selfDelay(self) -> str:
        return self.__selfDelay

    @selfDelay.setter
    def selfDelay(self, selfDelay: str):
        self.__selfDelay = selfDelay

    @property
    def servCount(self) -> str:
        return self.__servCount

    @servCount.setter
    def servCount(self, servCount: str):
        self.__servCount = servCount

    @property
    def prob(self) -> str:
        return self.__prob

    @prob.setter
    def prob(self, prob: str):
        self.__prob = prob

    @property
    def blockT(self) -> str:
        return self.__blockT

    @blockT.setter
    def blockT(self, blockT: str):
        self.__blockT = blockT

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def MARTE_GQAM_GaStep501(self):
        return self.__MARTE_GQAM_GaStep501

    @MARTE_GQAM_GaStep501.setter
    def MARTE_GQAM_GaStep501(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaStep__MARTE_GQAM_GaStep501", None)
        self.__MARTE_GQAM_GaStep501 = value
        
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

    @property
    def GQAM505(self):
        return self.__GQAM505

    @GQAM505.setter
    def GQAM505(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaStep__GQAM505", None)
        self.__GQAM505 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MARTE_AnalysisModel506"):
                opp_val = getattr(old_value, "MARTE_AnalysisModel506", None)
                if opp_val == self:
                    setattr(old_value, "MARTE_AnalysisModel506", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MARTE_AnalysisModel506"):
                opp_val = getattr(value, "MARTE_AnalysisModel506", None)
                setattr(value, "MARTE_AnalysisModel506", self)

    @property
    def MARTE_GQAM_GaStep503(self):
        return self.__MARTE_GQAM_GaStep503

    @MARTE_GQAM_GaStep503.setter
    def MARTE_GQAM_GaStep503(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaStep__MARTE_GQAM_GaStep503", None)
        self.__MARTE_GQAM_GaStep503 = value if value is not None else set()
        
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
    def GQAM508(self):
        return self.__GQAM508

    @GQAM508.setter
    def GQAM508(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaStep__GQAM508", None)
        self.__GQAM508 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MARTE_AnalysisModel509"):
                opp_val = getattr(old_value, "MARTE_AnalysisModel509", None)
                if opp_val == self:
                    setattr(old_value, "MARTE_AnalysisModel509", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MARTE_AnalysisModel509"):
                opp_val = getattr(value, "MARTE_AnalysisModel509", None)
                setattr(value, "MARTE_AnalysisModel509", self)

class GQAM_GaTimedObs:

    pass
class GQAM_MARTE_TimeEvent:

    pass
class GQAM_GaScenario:

    pass
class GQAM_GaWorkloadEvent:

    pass
class Time_TimedProcessing:

    pass
class GQAM_GaEventTrace:

    pass
class GQAM_GaWorkloadGenerator:

    pass
class MARTE_GQAM_GaWorkloadEvent:

    def __init__(self, pattern: str, MARTE_GQAM_GaWorkloadEvent: "GQAM_GaWorkloadGenerator" = None, MARTE_GQAM_GaWorkloadEvent486: "GQAM_MARTE_TimeEvent" = None, MARTE_GQAM_GaWorkloadEvent488: "GQAM_MARTE_NamedElement" = None, MARTE_GQAM_GaWorkloadEvent482: "GQAM_GaEventTrace" = None, MARTE_GQAM_GaWorkloadEvent484: "GQAM_GaScenario" = None):
        self.pattern = pattern
        self.MARTE_GQAM_GaWorkloadEvent = MARTE_GQAM_GaWorkloadEvent
        self.MARTE_GQAM_GaWorkloadEvent486 = MARTE_GQAM_GaWorkloadEvent486
        self.MARTE_GQAM_GaWorkloadEvent488 = MARTE_GQAM_GaWorkloadEvent488
        self.MARTE_GQAM_GaWorkloadEvent482 = MARTE_GQAM_GaWorkloadEvent482
        self.MARTE_GQAM_GaWorkloadEvent484 = MARTE_GQAM_GaWorkloadEvent484
        
    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

    @property
    def MARTE_GQAM_GaWorkloadEvent486(self):
        return self.__MARTE_GQAM_GaWorkloadEvent486

    @MARTE_GQAM_GaWorkloadEvent486.setter
    def MARTE_GQAM_GaWorkloadEvent486(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaWorkloadEvent__MARTE_GQAM_GaWorkloadEvent486", None)
        self.__MARTE_GQAM_GaWorkloadEvent486 = value
        
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
    def MARTE_GQAM_GaWorkloadEvent482(self):
        return self.__MARTE_GQAM_GaWorkloadEvent482

    @MARTE_GQAM_GaWorkloadEvent482.setter
    def MARTE_GQAM_GaWorkloadEvent482(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaWorkloadEvent__MARTE_GQAM_GaWorkloadEvent482", None)
        self.__MARTE_GQAM_GaWorkloadEvent482 = value
        
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

    @property
    def MARTE_GQAM_GaWorkloadEvent484(self):
        return self.__MARTE_GQAM_GaWorkloadEvent484

    @MARTE_GQAM_GaWorkloadEvent484.setter
    def MARTE_GQAM_GaWorkloadEvent484(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaWorkloadEvent__MARTE_GQAM_GaWorkloadEvent484", None)
        self.__MARTE_GQAM_GaWorkloadEvent484 = value
        
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
    def MARTE_GQAM_GaWorkloadEvent488(self):
        return self.__MARTE_GQAM_GaWorkloadEvent488

    @MARTE_GQAM_GaWorkloadEvent488.setter
    def MARTE_GQAM_GaWorkloadEvent488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaWorkloadEvent__MARTE_GQAM_GaWorkloadEvent488", None)
        self.__MARTE_GQAM_GaWorkloadEvent488 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_MARTE_NamedElement489"):
                opp_val = getattr(old_value, "GQAM_MARTE_NamedElement489", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_MARTE_NamedElement489", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_MARTE_NamedElement489"):
                opp_val = getattr(value, "GQAM_MARTE_NamedElement489", None)
                setattr(value, "GQAM_MARTE_NamedElement489", self)

class GQAM_MARTE_NamedElement:

    pass
class MARTE_GQAM_GaEventTrace:

    def __init__(self, content: str, format: str, location: str, MARTE_GQAM_GaEventTrace: "GQAM_MARTE_NamedElement" = None):
        self.content = content
        self.format = format
        self.location = location
        self.MARTE_GQAM_GaEventTrace = MARTE_GQAM_GaEventTrace
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

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
class MARTE_GQAM_GaWorkloadGenerator:

    def __init__(self, pop: str, MARTE_GQAM_GaWorkloadGenerator: "GQAM_MARTE_Behavior" = None):
        self.pop = pop
        self.MARTE_GQAM_GaWorkloadGenerator = MARTE_GQAM_GaWorkloadGenerator
        
    @property
    def pop(self) -> str:
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

class GCM_MARTE_Classifier:

    pass
class GCM_MARTE_AnyReceiveEvent:

    pass
class MARTE_GCM_GCMInvocatingBehavior:

    pass
class GCM_MARTE_Behavior:

    pass
class MARTE_GCM_DataPool:

    def __init__(self, ordering: str, MARTE_GCM_DataPool: "GCM_MARTE_Property" = None, MARTE_GCM_DataPool463: "GCM_MARTE_Behavior" = None, MARTE_GCM_DataPool465: "GCM_MARTE_Behavior" = None):
        self.ordering = ordering
        self.MARTE_GCM_DataPool = MARTE_GCM_DataPool
        self.MARTE_GCM_DataPool463 = MARTE_GCM_DataPool463
        self.MARTE_GCM_DataPool465 = MARTE_GCM_DataPool465
        
    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def MARTE_GCM_DataPool465(self):
        return self.__MARTE_GCM_DataPool465

    @MARTE_GCM_DataPool465.setter
    def MARTE_GCM_DataPool465(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_DataPool__MARTE_GCM_DataPool465", None)
        self.__MARTE_GCM_DataPool465 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_Behavior466"):
                opp_val = getattr(old_value, "GCM_MARTE_Behavior466", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Behavior466", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Behavior466"):
                opp_val = getattr(value, "GCM_MARTE_Behavior466", None)
                setattr(value, "GCM_MARTE_Behavior466", self)

    @property
    def MARTE_GCM_DataPool463(self):
        return self.__MARTE_GCM_DataPool463

    @MARTE_GCM_DataPool463.setter
    def MARTE_GCM_DataPool463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_DataPool__MARTE_GCM_DataPool463", None)
        self.__MARTE_GCM_DataPool463 = value
        
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
    def MARTE_GCM_DataPool(self):
        return self.__MARTE_GCM_DataPool

    @MARTE_GCM_DataPool.setter
    def MARTE_GCM_DataPool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_DataPool__MARTE_GCM_DataPool", None)
        self.__MARTE_GCM_DataPool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_Property461"):
                opp_val = getattr(old_value, "GCM_MARTE_Property461", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Property461", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Property461"):
                opp_val = getattr(value, "GCM_MARTE_Property461", None)
                setattr(value, "GCM_MARTE_Property461", self)

class MARTE_GCM_FlowSpecification:

    pass
class MARTE_GCM_DataEvent:

    pass
class GCM_MARTE_InvocationAction:

    pass
class MARTE_GCM_GCMInvocationAction:

    pass
class GCM_MARTE_Feature:

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

class MARTE_GCM_ClientServerPort:

    def __init__(self, specificationKind: str, kind: str, MARTE_GCM_ClientServerPort: "GCM_MARTE_Port" = None, MARTE_GCM_ClientServerPort439: set["GCM_MARTE_Interface"] = None, MARTE_GCM_ClientServerPort441: set["GCM_MARTE_Interface"] = None, MARTE_GCM_ClientServerPort444: "GCM_ClientServerSpecification" = None):
        self.specificationKind = specificationKind
        self.kind = kind
        self.MARTE_GCM_ClientServerPort = MARTE_GCM_ClientServerPort
        self.MARTE_GCM_ClientServerPort439 = MARTE_GCM_ClientServerPort439 if MARTE_GCM_ClientServerPort439 is not None else set()
        self.MARTE_GCM_ClientServerPort441 = MARTE_GCM_ClientServerPort441 if MARTE_GCM_ClientServerPort441 is not None else set()
        self.MARTE_GCM_ClientServerPort444 = MARTE_GCM_ClientServerPort444
        
    @property
    def specificationKind(self) -> str:
        return self.__specificationKind

    @specificationKind.setter
    def specificationKind(self, specificationKind: str):
        self.__specificationKind = specificationKind

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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
            if hasattr(old_value, "GCM_MARTE_Port437"):
                opp_val = getattr(old_value, "GCM_MARTE_Port437", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Port437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Port437"):
                opp_val = getattr(value, "GCM_MARTE_Port437", None)
                setattr(value, "GCM_MARTE_Port437", self)

    @property
    def MARTE_GCM_ClientServerPort439(self):
        return self.__MARTE_GCM_ClientServerPort439

    @MARTE_GCM_ClientServerPort439.setter
    def MARTE_GCM_ClientServerPort439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort439", None)
        self.__MARTE_GCM_ClientServerPort439 = value if value is not None else set()
        
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
    def MARTE_GCM_ClientServerPort444(self):
        return self.__MARTE_GCM_ClientServerPort444

    @MARTE_GCM_ClientServerPort444.setter
    def MARTE_GCM_ClientServerPort444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort444", None)
        self.__MARTE_GCM_ClientServerPort444 = value
        
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
    def MARTE_GCM_ClientServerPort441(self):
        return self.__MARTE_GCM_ClientServerPort441

    @MARTE_GCM_ClientServerPort441.setter
    def MARTE_GCM_ClientServerPort441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort441", None)
        self.__MARTE_GCM_ClientServerPort441 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GCM_MARTE_Interface442"):
                    opp_val = getattr(item, "GCM_MARTE_Interface442", None)
                    
                    if opp_val == self:
                        setattr(item, "GCM_MARTE_Interface442", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GCM_MARTE_Interface442"):
                    opp_val = getattr(item, "GCM_MARTE_Interface442", None)
                    
                    setattr(item, "GCM_MARTE_Interface442", self)
                    

class GCM_MARTE_Port:

    pass
class MARTE_GCM_ClientServerSpecification:

    pass
class GCM_ClientServerSpecification:

    pass
class GCM_MARTE_Interface:

    pass
class MARTE_GCM_FlowPort:

    def __init__(self, isAtomic: str, direction: str, MARTE_GCM_FlowPort: "GCM_MARTE_Port" = None):
        self.isAtomic = isAtomic
        self.direction = direction
        self.MARTE_GCM_FlowPort = MARTE_GCM_FlowPort
        
    @property
    def isAtomic(self) -> str:
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

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
class SwSynchronizationResource:

    pass
class MARTE_SW_Interaction_NotificationResource(SwSynchronizationResource):

    def __init__(self, occurence: str, mechanism: str, MARTE_SW_Interaction_NotificationResource: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_NotificationResource412: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_NotificationResource415: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource418: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource421: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource424: set["SW_Interaction_MARTE_BehavioralFeature"] = None):
        self.occurence = occurence
        self.mechanism = mechanism
        self.MARTE_SW_Interaction_NotificationResource = MARTE_SW_Interaction_NotificationResource if MARTE_SW_Interaction_NotificationResource is not None else set()
        self.MARTE_SW_Interaction_NotificationResource412 = MARTE_SW_Interaction_NotificationResource412 if MARTE_SW_Interaction_NotificationResource412 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource415 = MARTE_SW_Interaction_NotificationResource415 if MARTE_SW_Interaction_NotificationResource415 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource418 = MARTE_SW_Interaction_NotificationResource418 if MARTE_SW_Interaction_NotificationResource418 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource421 = MARTE_SW_Interaction_NotificationResource421 if MARTE_SW_Interaction_NotificationResource421 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource424 = MARTE_SW_Interaction_NotificationResource424 if MARTE_SW_Interaction_NotificationResource424 is not None else set()
        
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
    def MARTE_SW_Interaction_NotificationResource412(self):
        return self.__MARTE_SW_Interaction_NotificationResource412

    @MARTE_SW_Interaction_NotificationResource412.setter
    def MARTE_SW_Interaction_NotificationResource412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource412", None)
        self.__MARTE_SW_Interaction_NotificationResource412 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement413"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement413", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement413", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement413"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement413", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement413", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource418(self):
        return self.__MARTE_SW_Interaction_NotificationResource418

    @MARTE_SW_Interaction_NotificationResource418.setter
    def MARTE_SW_Interaction_NotificationResource418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource418", None)
        self.__MARTE_SW_Interaction_NotificationResource418 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature419"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature419", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature419", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature419"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature419", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature419", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource415(self):
        return self.__MARTE_SW_Interaction_NotificationResource415

    @MARTE_SW_Interaction_NotificationResource415.setter
    def MARTE_SW_Interaction_NotificationResource415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource415", None)
        self.__MARTE_SW_Interaction_NotificationResource415 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature416"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature416", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature416", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature416"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature416", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature416", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource421(self):
        return self.__MARTE_SW_Interaction_NotificationResource421

    @MARTE_SW_Interaction_NotificationResource421.setter
    def MARTE_SW_Interaction_NotificationResource421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource421", None)
        self.__MARTE_SW_Interaction_NotificationResource421 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature422"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature422", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature422", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature422"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature422", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature422", self)
                    

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
                if hasattr(item, "SW_Interaction_MARTE_TypedElement410"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement410", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement410", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement410"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement410", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement410", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource424(self):
        return self.__MARTE_SW_Interaction_NotificationResource424

    @MARTE_SW_Interaction_NotificationResource424.setter
    def MARTE_SW_Interaction_NotificationResource424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource424", None)
        self.__MARTE_SW_Interaction_NotificationResource424 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature425"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature425", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature425", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature425"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature425", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature425", self)
                    

class SW_Interaction_MARTE_BehavioralFeature:

    pass
class SwCommunicationResource:

    pass
class MARTE_SW_Interaction_MessageComResource(SwCommunicationResource):

    def __init__(self, messageQueuePolicy: str, isFixedMessageSize: str, mechanism: str, MARTE_SW_Interaction_MessageComResource: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_MessageComResource401: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_MessageComResource404: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_MessageComResource407: set["SW_Interaction_MARTE_BehavioralFeature"] = None):
        self.messageQueuePolicy = messageQueuePolicy
        self.isFixedMessageSize = isFixedMessageSize
        self.mechanism = mechanism
        self.MARTE_SW_Interaction_MessageComResource = MARTE_SW_Interaction_MessageComResource if MARTE_SW_Interaction_MessageComResource is not None else set()
        self.MARTE_SW_Interaction_MessageComResource401 = MARTE_SW_Interaction_MessageComResource401 if MARTE_SW_Interaction_MessageComResource401 is not None else set()
        self.MARTE_SW_Interaction_MessageComResource404 = MARTE_SW_Interaction_MessageComResource404 if MARTE_SW_Interaction_MessageComResource404 is not None else set()
        self.MARTE_SW_Interaction_MessageComResource407 = MARTE_SW_Interaction_MessageComResource407 if MARTE_SW_Interaction_MessageComResource407 is not None else set()
        
    @property
    def isFixedMessageSize(self) -> str:
        return self.__isFixedMessageSize

    @isFixedMessageSize.setter
    def isFixedMessageSize(self, isFixedMessageSize: str):
        self.__isFixedMessageSize = isFixedMessageSize

    @property
    def messageQueuePolicy(self) -> str:
        return self.__messageQueuePolicy

    @messageQueuePolicy.setter
    def messageQueuePolicy(self, messageQueuePolicy: str):
        self.__messageQueuePolicy = messageQueuePolicy

    @property
    def mechanism(self) -> str:
        return self.__mechanism

    @mechanism.setter
    def mechanism(self, mechanism: str):
        self.__mechanism = mechanism

    @property
    def MARTE_SW_Interaction_MessageComResource407(self):
        return self.__MARTE_SW_Interaction_MessageComResource407

    @MARTE_SW_Interaction_MessageComResource407.setter
    def MARTE_SW_Interaction_MessageComResource407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource407", None)
        self.__MARTE_SW_Interaction_MessageComResource407 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature408"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature408", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature408", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature408"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature408", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature408", self)
                    

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
                if hasattr(item, "SW_Interaction_MARTE_TypedElement399"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement399", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement399", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement399"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement399", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement399", self)
                    

    @property
    def MARTE_SW_Interaction_MessageComResource404(self):
        return self.__MARTE_SW_Interaction_MessageComResource404

    @MARTE_SW_Interaction_MessageComResource404.setter
    def MARTE_SW_Interaction_MessageComResource404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource404", None)
        self.__MARTE_SW_Interaction_MessageComResource404 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature405"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature405", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature405", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature405"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature405", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature405", self)
                    

    @property
    def MARTE_SW_Interaction_MessageComResource401(self):
        return self.__MARTE_SW_Interaction_MessageComResource401

    @MARTE_SW_Interaction_MessageComResource401.setter
    def MARTE_SW_Interaction_MessageComResource401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource401", None)
        self.__MARTE_SW_Interaction_MessageComResource401 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement402"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement402", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement402", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement402"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement402", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement402", self)
                    

class MARTE_SW_Interaction_SharedDataComResource(SwCommunicationResource):

    pass
class GRM_SynchronizationResource:

    pass
class SW_Interaction_SwInteractionResource:

    pass
class MARTE_SW_Interaction_SwSynchronizationResource(SW_Interaction_SwInteractionResource, GRM_SynchronizationResource):

    pass
class SW_Interaction_MARTE_TypedElement:

    pass
class SW_Brokering_MARTE_TypedElement:

    pass
class SW_Brokering_MARTE_BehavioralFeature:

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
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement357"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement357", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement357", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement357"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement357", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement357", self)
                    

class SW_Concurrency_MARTE_Namespace:

    pass
class SwConcurrentResource:

    pass
class MARTE_SW_Concurrency_InterruptResource(SwConcurrentResource):

    def __init__(self, kind: str, isMaskable: str, MARTE_SW_Concurrency_InterruptResource314: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_InterruptResource317: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_InterruptResource320: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_InterruptResource: set["SW_Concurrency_MARTE_TypedElement"] = None):
        self.kind = kind
        self.isMaskable = isMaskable
        self.MARTE_SW_Concurrency_InterruptResource314 = MARTE_SW_Concurrency_InterruptResource314 if MARTE_SW_Concurrency_InterruptResource314 is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource317 = MARTE_SW_Concurrency_InterruptResource317 if MARTE_SW_Concurrency_InterruptResource317 is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource320 = MARTE_SW_Concurrency_InterruptResource320 if MARTE_SW_Concurrency_InterruptResource320 is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource = MARTE_SW_Concurrency_InterruptResource if MARTE_SW_Concurrency_InterruptResource is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def isMaskable(self) -> str:
        return self.__isMaskable

    @isMaskable.setter
    def isMaskable(self, isMaskable: str):
        self.__isMaskable = isMaskable

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
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement312"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement312", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement312", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement312"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement312", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement312", self)
                    

    @property
    def MARTE_SW_Concurrency_InterruptResource320(self):
        return self.__MARTE_SW_Concurrency_InterruptResource320

    @MARTE_SW_Concurrency_InterruptResource320.setter
    def MARTE_SW_Concurrency_InterruptResource320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource320", None)
        self.__MARTE_SW_Concurrency_InterruptResource320 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature321"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature321", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature321"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature321", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature321", self)
                    

    @property
    def MARTE_SW_Concurrency_InterruptResource314(self):
        return self.__MARTE_SW_Concurrency_InterruptResource314

    @MARTE_SW_Concurrency_InterruptResource314.setter
    def MARTE_SW_Concurrency_InterruptResource314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource314", None)
        self.__MARTE_SW_Concurrency_InterruptResource314 = value if value is not None else set()
        
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
                    

    @property
    def MARTE_SW_Concurrency_InterruptResource317(self):
        return self.__MARTE_SW_Concurrency_InterruptResource317

    @MARTE_SW_Concurrency_InterruptResource317.setter
    def MARTE_SW_Concurrency_InterruptResource317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource317", None)
        self.__MARTE_SW_Concurrency_InterruptResource317 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature318"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature318", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature318", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature318"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature318", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature318", self)
                    

class TimerResource:

    pass
class MARTE_SW_Concurrency_SwTimerResource(TimerResource):

    pass
class SW_Concurrency_MARTE_NamedElement:

    pass
class SW_Concurrency_SwConcurrentResource:

    pass
class SW_Concurrency_MARTE_TypedElement:

    pass
class SW_ResourceCore_MARTE_BehavioralFeature:

    pass
class SW_ResourceCore_MARTE_TypedElement:

    pass
class SW_Concurrency_MARTE_Element:

    pass
class SwResource:

    pass
class MARTE_SW_Brokering_MemoryBroker(SwResource):

    def __init__(self, accessPolicy: str, MARTE_SW_Brokering_MemoryBroker: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_MemoryBroker382: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker385: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker388: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker391: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker376: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_MemoryBroker379: set["SW_Brokering_MARTE_TypedElement"] = None):
        self.accessPolicy = accessPolicy
        self.MARTE_SW_Brokering_MemoryBroker = MARTE_SW_Brokering_MemoryBroker if MARTE_SW_Brokering_MemoryBroker is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker382 = MARTE_SW_Brokering_MemoryBroker382 if MARTE_SW_Brokering_MemoryBroker382 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker385 = MARTE_SW_Brokering_MemoryBroker385 if MARTE_SW_Brokering_MemoryBroker385 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker388 = MARTE_SW_Brokering_MemoryBroker388 if MARTE_SW_Brokering_MemoryBroker388 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker391 = MARTE_SW_Brokering_MemoryBroker391 if MARTE_SW_Brokering_MemoryBroker391 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker376 = MARTE_SW_Brokering_MemoryBroker376 if MARTE_SW_Brokering_MemoryBroker376 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker379 = MARTE_SW_Brokering_MemoryBroker379 if MARTE_SW_Brokering_MemoryBroker379 is not None else set()
        
    @property
    def accessPolicy(self) -> str:
        return self.__accessPolicy

    @accessPolicy.setter
    def accessPolicy(self, accessPolicy: str):
        self.__accessPolicy = accessPolicy

    @property
    def MARTE_SW_Brokering_MemoryBroker382(self):
        return self.__MARTE_SW_Brokering_MemoryBroker382

    @MARTE_SW_Brokering_MemoryBroker382.setter
    def MARTE_SW_Brokering_MemoryBroker382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker382", None)
        self.__MARTE_SW_Brokering_MemoryBroker382 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature383"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature383", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature383", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature383"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature383", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature383", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker391(self):
        return self.__MARTE_SW_Brokering_MemoryBroker391

    @MARTE_SW_Brokering_MemoryBroker391.setter
    def MARTE_SW_Brokering_MemoryBroker391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker391", None)
        self.__MARTE_SW_Brokering_MemoryBroker391 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature392"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature392", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature392", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature392"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature392", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature392", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker379(self):
        return self.__MARTE_SW_Brokering_MemoryBroker379

    @MARTE_SW_Brokering_MemoryBroker379.setter
    def MARTE_SW_Brokering_MemoryBroker379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker379", None)
        self.__MARTE_SW_Brokering_MemoryBroker379 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement380"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement380", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement380", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement380"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement380", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement380", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker388(self):
        return self.__MARTE_SW_Brokering_MemoryBroker388

    @MARTE_SW_Brokering_MemoryBroker388.setter
    def MARTE_SW_Brokering_MemoryBroker388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker388", None)
        self.__MARTE_SW_Brokering_MemoryBroker388 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature389"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature389", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature389", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature389"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature389", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature389", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker376(self):
        return self.__MARTE_SW_Brokering_MemoryBroker376

    @MARTE_SW_Brokering_MemoryBroker376.setter
    def MARTE_SW_Brokering_MemoryBroker376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker376", None)
        self.__MARTE_SW_Brokering_MemoryBroker376 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement377"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement377", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement377", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement377"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement377", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement377", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker385(self):
        return self.__MARTE_SW_Brokering_MemoryBroker385

    @MARTE_SW_Brokering_MemoryBroker385.setter
    def MARTE_SW_Brokering_MemoryBroker385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker385", None)
        self.__MARTE_SW_Brokering_MemoryBroker385 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature386"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature386", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature386", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature386"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature386", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature386", self)
                    

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
                if hasattr(item, "SW_Brokering_MARTE_TypedElement374"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement374", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement374", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement374"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement374", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement374", self)
                    

class MARTE_SW_Concurrency_MemoryPartition(SwResource):

    pass
class MARTE_SW_Brokering_DeviceBroker(SwResource):

    def __init__(self, accessPolicy: str, isBuffered: str, MARTE_SW_Brokering_DeviceBroker360: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker362: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker365: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker368: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker371: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker: set["SW_Brokering_MARTE_TypedElement"] = None):
        self.accessPolicy = accessPolicy
        self.isBuffered = isBuffered
        self.MARTE_SW_Brokering_DeviceBroker360 = MARTE_SW_Brokering_DeviceBroker360 if MARTE_SW_Brokering_DeviceBroker360 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker362 = MARTE_SW_Brokering_DeviceBroker362 if MARTE_SW_Brokering_DeviceBroker362 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker365 = MARTE_SW_Brokering_DeviceBroker365 if MARTE_SW_Brokering_DeviceBroker365 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker368 = MARTE_SW_Brokering_DeviceBroker368 if MARTE_SW_Brokering_DeviceBroker368 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker371 = MARTE_SW_Brokering_DeviceBroker371 if MARTE_SW_Brokering_DeviceBroker371 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker = MARTE_SW_Brokering_DeviceBroker if MARTE_SW_Brokering_DeviceBroker is not None else set()
        
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
    def MARTE_SW_Brokering_DeviceBroker371(self):
        return self.__MARTE_SW_Brokering_DeviceBroker371

    @MARTE_SW_Brokering_DeviceBroker371.setter
    def MARTE_SW_Brokering_DeviceBroker371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker371", None)
        self.__MARTE_SW_Brokering_DeviceBroker371 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature372"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature372", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature372", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature372"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature372", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature372", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker365(self):
        return self.__MARTE_SW_Brokering_DeviceBroker365

    @MARTE_SW_Brokering_DeviceBroker365.setter
    def MARTE_SW_Brokering_DeviceBroker365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker365", None)
        self.__MARTE_SW_Brokering_DeviceBroker365 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature366"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature366", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature366", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature366"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature366", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature366", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker362(self):
        return self.__MARTE_SW_Brokering_DeviceBroker362

    @MARTE_SW_Brokering_DeviceBroker362.setter
    def MARTE_SW_Brokering_DeviceBroker362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker362", None)
        self.__MARTE_SW_Brokering_DeviceBroker362 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature363"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature363", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature363", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature363"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature363", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature363", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker368(self):
        return self.__MARTE_SW_Brokering_DeviceBroker368

    @MARTE_SW_Brokering_DeviceBroker368.setter
    def MARTE_SW_Brokering_DeviceBroker368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker368", None)
        self.__MARTE_SW_Brokering_DeviceBroker368 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature369"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature369", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature369", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature369"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature369", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature369", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker360(self):
        return self.__MARTE_SW_Brokering_DeviceBroker360

    @MARTE_SW_Brokering_DeviceBroker360.setter
    def MARTE_SW_Brokering_DeviceBroker360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker360", None)
        self.__MARTE_SW_Brokering_DeviceBroker360 = value if value is not None else set()
        
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
    def waitingQueuePolicy(self) -> str:
        return self.__waitingQueuePolicy

    @waitingQueuePolicy.setter
    def waitingQueuePolicy(self, waitingQueuePolicy: str):
        self.__waitingQueuePolicy = waitingQueuePolicy

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
                    

class MARTE_SW_Concurrency_SwConcurrentResource(SwResource):

    def __init__(self, type: str, activationCapacity: str, MARTE_SW_Concurrency_SwConcurrentResource: set["SW_Concurrency_MARTE_Element"] = None, MARTE_SW_Concurrency_SwConcurrentResource279: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource282: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource285: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource288: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource291: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource294: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource297: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource300: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource268: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource270: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource273: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource276: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource303: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource306: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource309: set["SW_Concurrency_MARTE_TypedElement"] = None):
        self.type = type
        self.activationCapacity = activationCapacity
        self.MARTE_SW_Concurrency_SwConcurrentResource = MARTE_SW_Concurrency_SwConcurrentResource if MARTE_SW_Concurrency_SwConcurrentResource is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource279 = MARTE_SW_Concurrency_SwConcurrentResource279 if MARTE_SW_Concurrency_SwConcurrentResource279 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource282 = MARTE_SW_Concurrency_SwConcurrentResource282 if MARTE_SW_Concurrency_SwConcurrentResource282 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource285 = MARTE_SW_Concurrency_SwConcurrentResource285 if MARTE_SW_Concurrency_SwConcurrentResource285 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource288 = MARTE_SW_Concurrency_SwConcurrentResource288 if MARTE_SW_Concurrency_SwConcurrentResource288 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource291 = MARTE_SW_Concurrency_SwConcurrentResource291 if MARTE_SW_Concurrency_SwConcurrentResource291 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource294 = MARTE_SW_Concurrency_SwConcurrentResource294 if MARTE_SW_Concurrency_SwConcurrentResource294 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource297 = MARTE_SW_Concurrency_SwConcurrentResource297 if MARTE_SW_Concurrency_SwConcurrentResource297 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource300 = MARTE_SW_Concurrency_SwConcurrentResource300 if MARTE_SW_Concurrency_SwConcurrentResource300 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource268 = MARTE_SW_Concurrency_SwConcurrentResource268 if MARTE_SW_Concurrency_SwConcurrentResource268 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource270 = MARTE_SW_Concurrency_SwConcurrentResource270 if MARTE_SW_Concurrency_SwConcurrentResource270 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource273 = MARTE_SW_Concurrency_SwConcurrentResource273 if MARTE_SW_Concurrency_SwConcurrentResource273 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource276 = MARTE_SW_Concurrency_SwConcurrentResource276 if MARTE_SW_Concurrency_SwConcurrentResource276 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource303 = MARTE_SW_Concurrency_SwConcurrentResource303 if MARTE_SW_Concurrency_SwConcurrentResource303 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource306 = MARTE_SW_Concurrency_SwConcurrentResource306 if MARTE_SW_Concurrency_SwConcurrentResource306 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource309 = MARTE_SW_Concurrency_SwConcurrentResource309 if MARTE_SW_Concurrency_SwConcurrentResource309 is not None else set()
        
    @property
    def activationCapacity(self) -> str:
        return self.__activationCapacity

    @activationCapacity.setter
    def activationCapacity(self, activationCapacity: str):
        self.__activationCapacity = activationCapacity

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource297(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource297

    @MARTE_SW_Concurrency_SwConcurrentResource297.setter
    def MARTE_SW_Concurrency_SwConcurrentResource297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource297", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource297 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement298"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement298", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement298"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement298", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement298", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource306(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource306

    @MARTE_SW_Concurrency_SwConcurrentResource306.setter
    def MARTE_SW_Concurrency_SwConcurrentResource306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource306", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource306 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement307"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement307", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement307"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement307", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement307", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource282(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource282

    @MARTE_SW_Concurrency_SwConcurrentResource282.setter
    def MARTE_SW_Concurrency_SwConcurrentResource282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource282", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature283"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature283", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature283", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature283"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature283", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature283", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource268(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource268

    @MARTE_SW_Concurrency_SwConcurrentResource268.setter
    def MARTE_SW_Concurrency_SwConcurrentResource268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource268", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource268 = value if value is not None else set()
        
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
    def MARTE_SW_Concurrency_SwConcurrentResource291(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource291

    @MARTE_SW_Concurrency_SwConcurrentResource291.setter
    def MARTE_SW_Concurrency_SwConcurrentResource291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource291", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource291 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature292"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature292", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature292", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature292"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature292", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature292", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource300(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource300

    @MARTE_SW_Concurrency_SwConcurrentResource300.setter
    def MARTE_SW_Concurrency_SwConcurrentResource300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource300", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource300 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement301"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement301", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement301", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement301"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement301", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement301", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource276(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource276

    @MARTE_SW_Concurrency_SwConcurrentResource276.setter
    def MARTE_SW_Concurrency_SwConcurrentResource276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource276", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource276 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement277"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement277", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement277"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement277", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement277", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource285(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource285

    @MARTE_SW_Concurrency_SwConcurrentResource285.setter
    def MARTE_SW_Concurrency_SwConcurrentResource285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource285", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource285 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature286"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature286", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature286", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature286"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature286", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature286", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource309(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource309

    @MARTE_SW_Concurrency_SwConcurrentResource309.setter
    def MARTE_SW_Concurrency_SwConcurrentResource309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource309", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource309 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement310"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement310", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement310", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement310"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement310", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement310", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource270(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource270

    @MARTE_SW_Concurrency_SwConcurrentResource270.setter
    def MARTE_SW_Concurrency_SwConcurrentResource270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource270", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource270 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement271"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement271", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement271", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement271"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement271", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement271", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource294(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource294

    @MARTE_SW_Concurrency_SwConcurrentResource294.setter
    def MARTE_SW_Concurrency_SwConcurrentResource294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource294", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource294 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature295"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature295", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature295"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature295", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature295", self)
                    

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
    def MARTE_SW_Concurrency_SwConcurrentResource279(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource279

    @MARTE_SW_Concurrency_SwConcurrentResource279.setter
    def MARTE_SW_Concurrency_SwConcurrentResource279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource279", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature280"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature280", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature280"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature280", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature280", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource303(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource303

    @MARTE_SW_Concurrency_SwConcurrentResource303.setter
    def MARTE_SW_Concurrency_SwConcurrentResource303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource303", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement304"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement304", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement304"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement304", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement304", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource288(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource288

    @MARTE_SW_Concurrency_SwConcurrentResource288.setter
    def MARTE_SW_Concurrency_SwConcurrentResource288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource288", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource288 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature289"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature289", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature289", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature289"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature289", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature289", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource273(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource273

    @MARTE_SW_Concurrency_SwConcurrentResource273.setter
    def MARTE_SW_Concurrency_SwConcurrentResource273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource273", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement274"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement274", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement274"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement274", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement274", self)
                    

class SW_Concurrency_MARTE_BehavioralFeature:

    pass
class SW_ResourceCore_MARTE_Property:

    pass
class HwLayout_HwComponent:

    pass
class HwComponent:

    pass
class MARTE_HwPower_HwCoolingSupply(HwComponent):

    def __init__(self, coolingPower: str):
        self.coolingPower = coolingPower
        
    @property
    def coolingPower(self) -> str:
        return self.__coolingPower

    @coolingPower.setter
    def coolingPower(self, coolingPower: str):
        self.__coolingPower = coolingPower

class MARTE_HwPower_HwPowerSupply(HwComponent):

    def __init__(self, suppliedPower: str, capacity: str):
        self.suppliedPower = suppliedPower
        self.capacity = capacity
        
    @property
    def suppliedPower(self) -> str:
        return self.__suppliedPower

    @suppliedPower.setter
    def suppliedPower(self, suppliedPower: str):
        self.__suppliedPower = suppliedPower

    @property
    def capacity(self) -> str:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity

class HwCommunication_HwEndPoint:

    pass
class HwI_O:

    pass
class MARTE_HwDevice_HWSensor(HwI_O):

    pass
class MARTE_HwDevice_HWActuator(HwI_O):

    pass
class HwDevice:

    pass
class MARTE_HwDevice_HwSupport(HwDevice):

    pass
class MARTE_HwDevice_HwI_O(HwDevice):

    pass
class GRM_DeviceResource:

    pass
class HwGeneral_HwResourceService:

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
        
    @property
    def counterWidth(self) -> str:
        return self.__counterWidth

    @counterWidth.setter
    def counterWidth(self, counterWidth: str):
        self.__counterWidth = counterWidth

    @property
    def nbCounters(self) -> str:
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
class HwMemory:

    pass
class MARTE_HwMemory_HwROM(HwMemory):

    def __init__(self, type: str, organization: str):
        self.type = type
        self.organization = organization
        
    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class MARTE_HwMemory_HwDrive(HwMemory):

    def __init__(self, sectorSize: str, MARTE_HwMemory_HwDrive: "HwMemory_HwRAM" = None):
        self.sectorSize = sectorSize
        self.MARTE_HwMemory_HwDrive = MARTE_HwMemory_HwDrive
        
    @property
    def sectorSize(self) -> str:
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
            if hasattr(old_value, "HwMemory_HwRAM235"):
                opp_val = getattr(old_value, "HwMemory_HwRAM235", None)
                if opp_val == self:
                    setattr(old_value, "HwMemory_HwRAM235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HwMemory_HwRAM235"):
                opp_val = getattr(value, "HwMemory_HwRAM235", None)
                setattr(value, "HwMemory_HwRAM235", self)

class MARTE_HwMemory_HwCache(HwMemory):

    def __init__(self, structure: str, repl_Policy: str, writePolicy: str, level: str, type: str):
        self.structure = structure
        self.repl_Policy = repl_Policy
        self.writePolicy = writePolicy
        self.level = level
        self.type = type
        
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
    def writePolicy(self) -> str:
        return self.__writePolicy

    @writePolicy.setter
    def writePolicy(self, writePolicy: str):
        self.__writePolicy = writePolicy

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def structure(self) -> str:
        return self.__structure

    @structure.setter
    def structure(self, structure: str):
        self.__structure = structure

class MARTE_HwMemory_HwRAM(HwMemory):

    def __init__(self, organization: str, isSynchronous: str, isStatic: str, isNonVolatile: str, repl_Policy: str, writePolicy: str):
        self.organization = organization
        self.isSynchronous = isSynchronous
        self.isStatic = isStatic
        self.isNonVolatile = isNonVolatile
        self.repl_Policy = repl_Policy
        self.writePolicy = writePolicy
        
    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

    @property
    def isSynchronous(self) -> str:
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: str):
        self.__isSynchronous = isSynchronous

    @property
    def isNonVolatile(self) -> str:
        return self.__isNonVolatile

    @isNonVolatile.setter
    def isNonVolatile(self, isNonVolatile: str):
        self.__isNonVolatile = isNonVolatile

    @property
    def repl_Policy(self) -> str:
        return self.__repl_Policy

    @repl_Policy.setter
    def repl_Policy(self, repl_Policy: str):
        self.__repl_Policy = repl_Policy

    @property
    def writePolicy(self) -> str:
        return self.__writePolicy

    @writePolicy.setter
    def writePolicy(self, writePolicy: str):
        self.__writePolicy = writePolicy

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

class HwStorageManager:

    pass
class MARTE_HwStorageManager_HwMMU(HwStorageManager):

    def __init__(self, virtualAddrSpace: str, physicalAddrSpace: str, memoryProtection: str, nbEntries: str, MARTE_HwStorageManager_HwMMU: set["HwMemory_HwCache"] = None):
        self.virtualAddrSpace = virtualAddrSpace
        self.physicalAddrSpace = physicalAddrSpace
        self.memoryProtection = memoryProtection
        self.nbEntries = nbEntries
        self.MARTE_HwStorageManager_HwMMU = MARTE_HwStorageManager_HwMMU if MARTE_HwStorageManager_HwMMU is not None else set()
        
    @property
    def virtualAddrSpace(self) -> str:
        return self.__virtualAddrSpace

    @virtualAddrSpace.setter
    def virtualAddrSpace(self, virtualAddrSpace: str):
        self.__virtualAddrSpace = virtualAddrSpace

    @property
    def nbEntries(self) -> str:
        return self.__nbEntries

    @nbEntries.setter
    def nbEntries(self, nbEntries: str):
        self.__nbEntries = nbEntries

    @property
    def memoryProtection(self) -> str:
        return self.__memoryProtection

    @memoryProtection.setter
    def memoryProtection(self, memoryProtection: str):
        self.__memoryProtection = memoryProtection

    @property
    def physicalAddrSpace(self) -> str:
        return self.__physicalAddrSpace

    @physicalAddrSpace.setter
    def physicalAddrSpace(self, physicalAddrSpace: str):
        self.__physicalAddrSpace = physicalAddrSpace

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
                if hasattr(item, "HwMemory_HwCache233"):
                    opp_val = getattr(item, "HwMemory_HwCache233", None)
                    
                    if opp_val == self:
                        setattr(item, "HwMemory_HwCache233", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwMemory_HwCache233"):
                    opp_val = getattr(item, "HwMemory_HwCache233", None)
                    
                    setattr(item, "HwMemory_HwCache233", self)
                    

class HwComputing_HwProcessor:

    pass
class HwStorageManager_HwStorageManager:

    pass
class GRM_CommunicationMedia:

    pass
class MARTE_SW_Interaction_SwCommunicationResource(GRM_CommunicationMedia, SW_Interaction_SwInteractionResource):

    pass
class HwCommunication_HwMedia:

    pass
class HwCommunicationResource:

    pass
class MARTE_HwCommunication_HwArbiter(HwCommunicationResource):

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
        
    @property
    def isSerial(self) -> str:
        return self.__isSerial

    @isSerial.setter
    def isSerial(self, isSerial: str):
        self.__isSerial = isSerial

    @property
    def wordWidth(self) -> str:
        return self.__wordWidth

    @wordWidth.setter
    def wordWidth(self, wordWidth: str):
        self.__wordWidth = wordWidth

    @property
    def adressWidth(self) -> str:
        return self.__adressWidth

    @adressWidth.setter
    def adressWidth(self, adressWidth: str):
        self.__adressWidth = adressWidth

    @property
    def isSynchronous(self) -> str:
        return self.__isSynchronous

    @isSynchronous.setter
    def isSynchronous(self, isSynchronous: str):
        self.__isSynchronous = isSynchronous

class HwCommunication_HwArbiter:

    pass
class MARTE_HwStorageManager_HwDMA(HwStorageManager_HwStorageManager, HwCommunication_HwArbiter):

    def __init__(self, nbChannels: str, transferWidth: str, MARTE_HwStorageManager_HwDMA: set["HwComputing_HwProcessor"] = None, MARTE_DesignModel226: "MARTE_HwCommunication_HwMedia"):
        self.nbChannels = nbChannels
        self.transferWidth = transferWidth
        self.MARTE_HwStorageManager_HwDMA = MARTE_HwStorageManager_HwDMA if MARTE_HwStorageManager_HwDMA is not None else set()
        
    @property
    def nbChannels(self) -> str:
        return self.__nbChannels

    @nbChannels.setter
    def nbChannels(self, nbChannels: str):
        self.__nbChannels = nbChannels

    @property
    def transferWidth(self) -> str:
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
class MARTE_HwCommunication_HwEndPoint(HwCommunication_HwCommunicationResource, GRM_CommunicationEndPoint):

    pass
class MARTE_HwCommunication_HwMedia(HwCommunication_HwCommunicationResource, GRM_CommunicationMedia):

    def __init__(self, bandWidth: str, HRM225: set["HwCommunication_HwArbiter"] = None):
        self.bandWidth = bandWidth
        self.HRM225 = HRM225 if HRM225 is not None else set()
        
    @property
    def bandWidth(self) -> str:
        return self.__bandWidth

    @bandWidth.setter
    def bandWidth(self, bandWidth: str):
        self.__bandWidth = bandWidth

    @property
    def HRM225(self):
        return self.__HRM225

    @HRM225.setter
    def HRM225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwCommunication_HwMedia__HRM225", None)
        self.__HRM225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MARTE_DesignModel226"):
                    opp_val = getattr(item, "MARTE_DesignModel226", None)
                    
                    if opp_val == self:
                        setattr(item, "MARTE_DesignModel226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MARTE_DesignModel226"):
                    opp_val = getattr(item, "MARTE_DesignModel226", None)
                    
                    setattr(item, "MARTE_DesignModel226", self)
                    

class HwComputing_HwComputingResource:

    pass
class HwMemory_HwRAM:

    pass
class HwComputing_HwISA:

    pass
class HwComputingResource:

    pass
class MARTE_HwComputing_HwProcessor(HwComputingResource):

    def __init__(self, architecture: str, mips: str, ipc: str, nbCores: str, nbPipelines: str, nbStages: str, nbALUs: str, nbFPUs: str, MARTE_HwComputing_HwProcessor: set["HwComputing_HwISA"] = None, MARTE_HwComputing_HwProcessor215: set["HwComputing_HwBranchPredictor"] = None, MARTE_HwComputing_HwProcessor217: set["HwMemory_HwCache"] = None, MARTE_HwComputing_HwProcessor219: set["HwStorageManager_HwMMU"] = None):
        self.architecture = architecture
        self.mips = mips
        self.ipc = ipc
        self.nbCores = nbCores
        self.nbPipelines = nbPipelines
        self.nbStages = nbStages
        self.nbALUs = nbALUs
        self.nbFPUs = nbFPUs
        self.MARTE_HwComputing_HwProcessor = MARTE_HwComputing_HwProcessor if MARTE_HwComputing_HwProcessor is not None else set()
        self.MARTE_HwComputing_HwProcessor215 = MARTE_HwComputing_HwProcessor215 if MARTE_HwComputing_HwProcessor215 is not None else set()
        self.MARTE_HwComputing_HwProcessor217 = MARTE_HwComputing_HwProcessor217 if MARTE_HwComputing_HwProcessor217 is not None else set()
        self.MARTE_HwComputing_HwProcessor219 = MARTE_HwComputing_HwProcessor219 if MARTE_HwComputing_HwProcessor219 is not None else set()
        
    @property
    def nbFPUs(self) -> str:
        return self.__nbFPUs

    @nbFPUs.setter
    def nbFPUs(self, nbFPUs: str):
        self.__nbFPUs = nbFPUs

    @property
    def nbStages(self) -> str:
        return self.__nbStages

    @nbStages.setter
    def nbStages(self, nbStages: str):
        self.__nbStages = nbStages

    @property
    def architecture(self) -> str:
        return self.__architecture

    @architecture.setter
    def architecture(self, architecture: str):
        self.__architecture = architecture

    @property
    def ipc(self) -> str:
        return self.__ipc

    @ipc.setter
    def ipc(self, ipc: str):
        self.__ipc = ipc

    @property
    def nbCores(self) -> str:
        return self.__nbCores

    @nbCores.setter
    def nbCores(self, nbCores: str):
        self.__nbCores = nbCores

    @property
    def nbALUs(self) -> str:
        return self.__nbALUs

    @nbALUs.setter
    def nbALUs(self, nbALUs: str):
        self.__nbALUs = nbALUs

    @property
    def nbPipelines(self) -> str:
        return self.__nbPipelines

    @nbPipelines.setter
    def nbPipelines(self, nbPipelines: str):
        self.__nbPipelines = nbPipelines

    @property
    def mips(self) -> str:
        return self.__mips

    @mips.setter
    def mips(self, mips: str):
        self.__mips = mips

    @property
    def MARTE_HwComputing_HwProcessor217(self):
        return self.__MARTE_HwComputing_HwProcessor217

    @MARTE_HwComputing_HwProcessor217.setter
    def MARTE_HwComputing_HwProcessor217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwProcessor__MARTE_HwComputing_HwProcessor217", None)
        self.__MARTE_HwComputing_HwProcessor217 = value if value is not None else set()
        
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
    def MARTE_HwComputing_HwProcessor219(self):
        return self.__MARTE_HwComputing_HwProcessor219

    @MARTE_HwComputing_HwProcessor219.setter
    def MARTE_HwComputing_HwProcessor219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwProcessor__MARTE_HwComputing_HwProcessor219", None)
        self.__MARTE_HwComputing_HwProcessor219 = value if value is not None else set()
        
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
    def MARTE_HwComputing_HwProcessor215(self):
        return self.__MARTE_HwComputing_HwProcessor215

    @MARTE_HwComputing_HwProcessor215.setter
    def MARTE_HwComputing_HwProcessor215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwProcessor__MARTE_HwComputing_HwProcessor215", None)
        self.__MARTE_HwComputing_HwProcessor215 = value if value is not None else set()
        
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
                    

class MARTE_HwComputing_HwPLD(HwComputingResource):

    def __init__(self, technology: str, organization: str, nbLUTs: str, ndLUT_Inputs: str, nbFlipFlops: str, MARTE_HwComputing_HwPLD: set["HwMemory_HwRAM"] = None, MARTE_HwComputing_HwPLD222: set["HwComputing_HwComputingResource"] = None):
        self.technology = technology
        self.organization = organization
        self.nbLUTs = nbLUTs
        self.ndLUT_Inputs = ndLUT_Inputs
        self.nbFlipFlops = nbFlipFlops
        self.MARTE_HwComputing_HwPLD = MARTE_HwComputing_HwPLD if MARTE_HwComputing_HwPLD is not None else set()
        self.MARTE_HwComputing_HwPLD222 = MARTE_HwComputing_HwPLD222 if MARTE_HwComputing_HwPLD222 is not None else set()
        
    @property
    def ndLUT_Inputs(self) -> str:
        return self.__ndLUT_Inputs

    @ndLUT_Inputs.setter
    def ndLUT_Inputs(self, ndLUT_Inputs: str):
        self.__ndLUT_Inputs = ndLUT_Inputs

    @property
    def technology(self) -> str:
        return self.__technology

    @technology.setter
    def technology(self, technology: str):
        self.__technology = technology

    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def nbLUTs(self) -> str:
        return self.__nbLUTs

    @nbLUTs.setter
    def nbLUTs(self, nbLUTs: str):
        self.__nbLUTs = nbLUTs

    @property
    def nbFlipFlops(self) -> str:
        return self.__nbFlipFlops

    @nbFlipFlops.setter
    def nbFlipFlops(self, nbFlipFlops: str):
        self.__nbFlipFlops = nbFlipFlops

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
                    

    @property
    def MARTE_HwComputing_HwPLD222(self):
        return self.__MARTE_HwComputing_HwPLD222

    @MARTE_HwComputing_HwPLD222.setter
    def MARTE_HwComputing_HwPLD222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD222", None)
        self.__MARTE_HwComputing_HwPLD222 = value if value is not None else set()
        
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
                    

class MARTE_HwComputing_HwASIC(HwComputingResource):

    pass
class HwResource:

    pass
class MARTE_HwLayout_HwComponent(HwResource):

    def __init__(self, dimensions: str, area: str, position: str, grid: str, nbPins: str, weight: str, price: str, r_Conditions: str, staticConsumption: str, kind: str, staticDissipation: str, MARTE_HwLayout_HwComponent: set["HwGeneral_HwResourceService"] = None, MARTE_HwLayout_HwComponent248: set["HwLayout_HwComponent"] = None):
        self.dimensions = dimensions
        self.area = area
        self.position = position
        self.grid = grid
        self.nbPins = nbPins
        self.weight = weight
        self.price = price
        self.r_Conditions = r_Conditions
        self.staticConsumption = staticConsumption
        self.kind = kind
        self.staticDissipation = staticDissipation
        self.MARTE_HwLayout_HwComponent = MARTE_HwLayout_HwComponent if MARTE_HwLayout_HwComponent is not None else set()
        self.MARTE_HwLayout_HwComponent248 = MARTE_HwLayout_HwComponent248 if MARTE_HwLayout_HwComponent248 is not None else set()
        
    @property
    def r_Conditions(self) -> str:
        return self.__r_Conditions

    @r_Conditions.setter
    def r_Conditions(self, r_Conditions: str):
        self.__r_Conditions = r_Conditions

    @property
    def area(self) -> str:
        return self.__area

    @area.setter
    def area(self, area: str):
        self.__area = area

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def dimensions(self) -> str:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

    @property
    def nbPins(self) -> str:
        return self.__nbPins

    @nbPins.setter
    def nbPins(self, nbPins: str):
        self.__nbPins = nbPins

    @property
    def staticDissipation(self) -> str:
        return self.__staticDissipation

    @staticDissipation.setter
    def staticDissipation(self, staticDissipation: str):
        self.__staticDissipation = staticDissipation

    @property
    def grid(self) -> str:
        return self.__grid

    @grid.setter
    def grid(self, grid: str):
        self.__grid = grid

    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def staticConsumption(self) -> str:
        return self.__staticConsumption

    @staticConsumption.setter
    def staticConsumption(self, staticConsumption: str):
        self.__staticConsumption = staticConsumption

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
                if hasattr(item, "HwGeneral_HwResourceService246"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService246", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResourceService246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResourceService246"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService246", None)
                    
                    setattr(item, "HwGeneral_HwResourceService246", self)
                    

    @property
    def MARTE_HwLayout_HwComponent248(self):
        return self.__MARTE_HwLayout_HwComponent248

    @MARTE_HwLayout_HwComponent248.setter
    def MARTE_HwLayout_HwComponent248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent248", None)
        self.__MARTE_HwLayout_HwComponent248 = value if value is not None else set()
        
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
                    

class MARTE_HwCommunication_HwCommunicationResource(HwResource):

    pass
class MARTE_HwComputing_HwBranchPredictor(HwResource):

    pass
class MARTE_HwComputing_HwISA(HwResource):

    def __init__(self, family: str, inst_Width: str, type: str):
        self.family = family
        self.inst_Width = inst_Width
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def family(self) -> str:
        return self.__family

    @family.setter
    def family(self, family: str):
        self.__family = family

    @property
    def inst_Width(self) -> str:
        return self.__inst_Width

    @inst_Width.setter
    def inst_Width(self, inst_Width: str):
        self.__inst_Width = inst_Width

class HwGeneral_HwResource:

    pass
class MARTE_HwDevice_HwDevice(GRM_DeviceResource, HwGeneral_HwResource):

    pass
class MARTE_HwMemory_HwMemory(GRM_StorageResource, HwGeneral_HwResource):

    def __init__(self, memorySize: str, adressSize: str, timings: str, throughput: str, HwGeneral_HwResource: "MARTE_HwGeneral_HwResource"):
        self.memorySize = memorySize
        self.adressSize = adressSize
        self.timings = timings
        self.throughput = throughput
        
    @property
    def adressSize(self) -> str:
        return self.__adressSize

    @adressSize.setter
    def adressSize(self, adressSize: str):
        self.__adressSize = adressSize

    @property
    def timings(self) -> str:
        return self.__timings

    @timings.setter
    def timings(self, timings: str):
        self.__timings = timings

    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def memorySize(self) -> str:
        return self.__memorySize

    @memorySize.setter
    def memorySize(self, memorySize: str):
        self.__memorySize = memorySize

class MARTE_HwTiming_HwTimingResource(GRM_TimingResource, HwGeneral_HwResource):

    pass
class MARTE_HwStorageManager_HwStorageManager(GRM_StorageResource, HwGeneral_HwResource):

    pass
class HwStorageManager_HwMMU:

    pass
class HwMemory_HwCache:

    pass
class HwComputing_HwBranchPredictor:

    pass
class MARTE_HLAM_RtAction:

    def __init__(self, isAtomic: str, synchKind: str, msgSize: str, MARTE_HLAM_RtAction: "HLAM_MARTE_BehavioralFeature" = None, MARTE_HLAM_RtAction209: "HLAM_MARTE_InvocationAction" = None):
        self.isAtomic = isAtomic
        self.synchKind = synchKind
        self.msgSize = msgSize
        self.MARTE_HLAM_RtAction = MARTE_HLAM_RtAction
        self.MARTE_HLAM_RtAction209 = MARTE_HLAM_RtAction209
        
    @property
    def msgSize(self) -> str:
        return self.__msgSize

    @msgSize.setter
    def msgSize(self, msgSize: str):
        self.__msgSize = msgSize

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
    def MARTE_HLAM_RtAction(self):
        return self.__MARTE_HLAM_RtAction

    @MARTE_HLAM_RtAction.setter
    def MARTE_HLAM_RtAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtAction__MARTE_HLAM_RtAction", None)
        self.__MARTE_HLAM_RtAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_BehavioralFeature207"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioralFeature207", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioralFeature207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioralFeature207"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioralFeature207", None)
                setattr(value, "HLAM_MARTE_BehavioralFeature207", self)

    @property
    def MARTE_HLAM_RtAction209(self):
        return self.__MARTE_HLAM_RtAction209

    @MARTE_HLAM_RtAction209.setter
    def MARTE_HLAM_RtAction209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtAction__MARTE_HLAM_RtAction209", None)
        self.__MARTE_HLAM_RtAction209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_InvocationAction210"):
                opp_val = getattr(old_value, "HLAM_MARTE_InvocationAction210", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_InvocationAction210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_InvocationAction210"):
                opp_val = getattr(value, "HLAM_MARTE_InvocationAction210", None)
                setattr(value, "HLAM_MARTE_InvocationAction210", self)

class HLAM_MARTE_Comment:

    pass
class MARTE_HLAM_RtService:

    def __init__(self, concPolicy: str, exeKind: str, isAtomic: str, synchKind: str, MARTE_HLAM_RtService: "HLAM_MARTE_BehavioralFeature" = None):
        self.concPolicy = concPolicy
        self.exeKind = exeKind
        self.isAtomic = isAtomic
        self.synchKind = synchKind
        self.MARTE_HLAM_RtService = MARTE_HLAM_RtService
        
    @property
    def isAtomic(self) -> str:
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic

    @property
    def concPolicy(self) -> str:
        return self.__concPolicy

    @concPolicy.setter
    def concPolicy(self, concPolicy: str):
        self.__concPolicy = concPolicy

    @property
    def exeKind(self) -> str:
        return self.__exeKind

    @exeKind.setter
    def exeKind(self, exeKind: str):
        self.__exeKind = exeKind

    @property
    def synchKind(self) -> str:
        return self.__synchKind

    @synchKind.setter
    def synchKind(self, synchKind: str):
        self.__synchKind = synchKind

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
            if hasattr(old_value, "HLAM_MARTE_BehavioralFeature212"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioralFeature212", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioralFeature212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioralFeature212"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioralFeature212", None)
                setattr(value, "HLAM_MARTE_BehavioralFeature212", self)

class MARTE_HLAM_RtFeature:

    pass
class MARTE_HLAM_PpUnit:

    def __init__(self, concPolicy: str, memorySize: str, MARTE_HLAM_PpUnit: "HLAM_MARTE_BehavioredClassifier" = None):
        self.concPolicy = concPolicy
        self.memorySize = memorySize
        self.MARTE_HLAM_PpUnit = MARTE_HLAM_PpUnit
        
    @property
    def memorySize(self) -> str:
        return self.__memorySize

    @memorySize.setter
    def memorySize(self, memorySize: str):
        self.__memorySize = memorySize

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
            if hasattr(old_value, "HLAM_MARTE_BehavioredClassifier188"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioredClassifier188", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioredClassifier188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioredClassifier188"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioredClassifier188", None)
                setattr(value, "HLAM_MARTE_BehavioredClassifier188", self)

class HLAM_MARTE_BehavioredClassifier:

    pass
class Time_TimedInstantObservation:

    pass
class MARTE_HLAM_RtSpecification:

    def __init__(self, utility: str, occKind: str, relDl: str, absDl: str, boundDl: str, rdTime: str, miss: str, priority: str, MARTE_HLAM_RtSpecification: "Time_TimedInstantObservation" = None, MARTE_HLAM_RtSpecification202: "HLAM_MARTE_Comment" = None, MARTE_HLAM_RtSpecification204: "HLAM_MARTE_BehavioralFeature" = None):
        self.utility = utility
        self.occKind = occKind
        self.relDl = relDl
        self.absDl = absDl
        self.boundDl = boundDl
        self.rdTime = rdTime
        self.miss = miss
        self.priority = priority
        self.MARTE_HLAM_RtSpecification = MARTE_HLAM_RtSpecification
        self.MARTE_HLAM_RtSpecification202 = MARTE_HLAM_RtSpecification202
        self.MARTE_HLAM_RtSpecification204 = MARTE_HLAM_RtSpecification204
        
    @property
    def utility(self) -> str:
        return self.__utility

    @utility.setter
    def utility(self, utility: str):
        self.__utility = utility

    @property
    def occKind(self) -> str:
        return self.__occKind

    @occKind.setter
    def occKind(self, occKind: str):
        self.__occKind = occKind

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def boundDl(self) -> str:
        return self.__boundDl

    @boundDl.setter
    def boundDl(self, boundDl: str):
        self.__boundDl = boundDl

    @property
    def rdTime(self) -> str:
        return self.__rdTime

    @rdTime.setter
    def rdTime(self, rdTime: str):
        self.__rdTime = rdTime

    @property
    def absDl(self) -> str:
        return self.__absDl

    @absDl.setter
    def absDl(self, absDl: str):
        self.__absDl = absDl

    @property
    def relDl(self) -> str:
        return self.__relDl

    @relDl.setter
    def relDl(self, relDl: str):
        self.__relDl = relDl

    @property
    def miss(self) -> str:
        return self.__miss

    @miss.setter
    def miss(self, miss: str):
        self.__miss = miss

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
    def MARTE_HLAM_RtSpecification202(self):
        return self.__MARTE_HLAM_RtSpecification202

    @MARTE_HLAM_RtSpecification202.setter
    def MARTE_HLAM_RtSpecification202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtSpecification__MARTE_HLAM_RtSpecification202", None)
        self.__MARTE_HLAM_RtSpecification202 = value
        
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
    def MARTE_HLAM_RtSpecification204(self):
        return self.__MARTE_HLAM_RtSpecification204

    @MARTE_HLAM_RtSpecification204.setter
    def MARTE_HLAM_RtSpecification204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtSpecification__MARTE_HLAM_RtSpecification204", None)
        self.__MARTE_HLAM_RtSpecification204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_BehavioralFeature205"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioralFeature205", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioralFeature205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioralFeature205"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioralFeature205", None)
                setattr(value, "HLAM_MARTE_BehavioralFeature205", self)

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
class MARTE_DataTypes_ChoiceType:

    pass
class MARTE_DataTypes_CollectionType:

    pass
class DataTypes_MARTE_Property:

    pass
class MARTE_DataTypes_IntervalType:

    pass
class HLAM_MARTE_Operation:

    pass
class HLAM_MARTE_Behavior:

    pass
class MARTE_HLAM_RtUnit:

    def __init__(self, isDynamic: str, isMain: str, srPoolSize: str, srPoolPolicy: str, srPoolWaitingTime: str, memorySize: str, queueSchedPolicy: str, queueSize: str, msgMaxSize: str, MARTE_HLAM_RtUnit: "HLAM_MARTE_Behavior" = None, MARTE_HLAM_RtUnit184: "HLAM_MARTE_Operation" = None, MARTE_HLAM_RtUnit186: "HLAM_MARTE_BehavioredClassifier" = None):
        self.isDynamic = isDynamic
        self.isMain = isMain
        self.srPoolSize = srPoolSize
        self.srPoolPolicy = srPoolPolicy
        self.srPoolWaitingTime = srPoolWaitingTime
        self.memorySize = memorySize
        self.queueSchedPolicy = queueSchedPolicy
        self.queueSize = queueSize
        self.msgMaxSize = msgMaxSize
        self.MARTE_HLAM_RtUnit = MARTE_HLAM_RtUnit
        self.MARTE_HLAM_RtUnit184 = MARTE_HLAM_RtUnit184
        self.MARTE_HLAM_RtUnit186 = MARTE_HLAM_RtUnit186
        
    @property
    def srPoolWaitingTime(self) -> str:
        return self.__srPoolWaitingTime

    @srPoolWaitingTime.setter
    def srPoolWaitingTime(self, srPoolWaitingTime: str):
        self.__srPoolWaitingTime = srPoolWaitingTime

    @property
    def isMain(self) -> str:
        return self.__isMain

    @isMain.setter
    def isMain(self, isMain: str):
        self.__isMain = isMain

    @property
    def msgMaxSize(self) -> str:
        return self.__msgMaxSize

    @msgMaxSize.setter
    def msgMaxSize(self, msgMaxSize: str):
        self.__msgMaxSize = msgMaxSize

    @property
    def srPoolPolicy(self) -> str:
        return self.__srPoolPolicy

    @srPoolPolicy.setter
    def srPoolPolicy(self, srPoolPolicy: str):
        self.__srPoolPolicy = srPoolPolicy

    @property
    def isDynamic(self) -> str:
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic

    @property
    def memorySize(self) -> str:
        return self.__memorySize

    @memorySize.setter
    def memorySize(self, memorySize: str):
        self.__memorySize = memorySize

    @property
    def queueSchedPolicy(self) -> str:
        return self.__queueSchedPolicy

    @queueSchedPolicy.setter
    def queueSchedPolicy(self, queueSchedPolicy: str):
        self.__queueSchedPolicy = queueSchedPolicy

    @property
    def queueSize(self) -> str:
        return self.__queueSize

    @queueSize.setter
    def queueSize(self, queueSize: str):
        self.__queueSize = queueSize

    @property
    def srPoolSize(self) -> str:
        return self.__srPoolSize

    @srPoolSize.setter
    def srPoolSize(self, srPoolSize: str):
        self.__srPoolSize = srPoolSize

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
    def MARTE_HLAM_RtUnit184(self):
        return self.__MARTE_HLAM_RtUnit184

    @MARTE_HLAM_RtUnit184.setter
    def MARTE_HLAM_RtUnit184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit184", None)
        self.__MARTE_HLAM_RtUnit184 = value
        
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
    def MARTE_HLAM_RtUnit186(self):
        return self.__MARTE_HLAM_RtUnit186

    @MARTE_HLAM_RtUnit186.setter
    def MARTE_HLAM_RtUnit186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit186", None)
        self.__MARTE_HLAM_RtUnit186 = value
        
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
class RSM_MARTE_MultiplicityElement:

    pass
class MARTE_RSM_Shaped:

    def __init__(self, shape: str, MARTE_RSM_Shaped: "RSM_MARTE_MultiplicityElement" = None):
        self.shape = shape
        self.MARTE_RSM_Shaped = MARTE_RSM_Shaped
        
    @property
    def shape(self) -> str:
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

class RSM_MARTE_ConnectorEnd:

    pass
class DataTypes_MARTE_DataType:

    pass
class MARTE_DataTypes_BoundedSubtype:

    def __init__(self, minValue: str, maxValue: str, isMinOpen: bool, isMaxOpen: bool, MARTE_DataTypes_BoundedSubtype: "DataTypes_MARTE_DataType" = None, MARTE_DataTypes_BoundedSubtype158: "DataTypes_MARTE_DataType" = None):
        self.minValue = minValue
        self.maxValue = maxValue
        self.isMinOpen = isMinOpen
        self.isMaxOpen = isMaxOpen
        self.MARTE_DataTypes_BoundedSubtype = MARTE_DataTypes_BoundedSubtype
        self.MARTE_DataTypes_BoundedSubtype158 = MARTE_DataTypes_BoundedSubtype158
        
    @property
    def isMinOpen(self) -> bool:
        return self.__isMinOpen

    @isMinOpen.setter
    def isMinOpen(self, isMinOpen: bool):
        self.__isMinOpen = isMinOpen

    @property
    def maxValue(self) -> str:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: str):
        self.__maxValue = maxValue

    @property
    def isMaxOpen(self) -> bool:
        return self.__isMaxOpen

    @isMaxOpen.setter
    def isMaxOpen(self, isMaxOpen: bool):
        self.__isMaxOpen = isMaxOpen

    @property
    def minValue(self) -> str:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: str):
        self.__minValue = minValue

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
    def MARTE_DataTypes_BoundedSubtype158(self):
        return self.__MARTE_DataTypes_BoundedSubtype158

    @MARTE_DataTypes_BoundedSubtype158.setter
    def MARTE_DataTypes_BoundedSubtype158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_DataTypes_BoundedSubtype__MARTE_DataTypes_BoundedSubtype158", None)
        self.__MARTE_DataTypes_BoundedSubtype158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataTypes_MARTE_DataType159"):
                opp_val = getattr(old_value, "DataTypes_MARTE_DataType159", None)
                if opp_val == self:
                    setattr(old_value, "DataTypes_MARTE_DataType159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataTypes_MARTE_DataType159"):
                opp_val = getattr(value, "DataTypes_MARTE_DataType159", None)
                setattr(value, "DataTypes_MARTE_DataType159", self)

class Operators_MARTE_Behavior:

    pass
class MARTE_Operators_Operator:

    def __init__(self, symbol: str, arity: str, MARTE_Operators_Operator: "Operators_MARTE_Behavior" = None):
        self.symbol = symbol
        self.arity = arity
        self.MARTE_Operators_Operator = MARTE_Operators_Operator
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def arity(self) -> str:
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
        
    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def isPeriodic(self) -> str:
        return self.__isPeriodic

    @isPeriodic.setter
    def isPeriodic(self, isPeriodic: str):
        self.__isPeriodic = isPeriodic

class MARTE_GRM_ClockResource(TimingResource):

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

    def __init__(self, patternShape: str, repetitionSpace: str, fromTiler: str, toTiler: str):
        self.patternShape = patternShape
        self.repetitionSpace = repetitionSpace
        self.fromTiler = fromTiler
        self.toTiler = toTiler
        
    @property
    def repetitionSpace(self) -> str:
        return self.__repetitionSpace

    @repetitionSpace.setter
    def repetitionSpace(self, repetitionSpace: str):
        self.__repetitionSpace = repetitionSpace

    @property
    def patternShape(self) -> str:
        return self.__patternShape

    @patternShape.setter
    def patternShape(self, patternShape: str):
        self.__patternShape = patternShape

    @property
    def toTiler(self) -> str:
        return self.__toTiler

    @toTiler.setter
    def toTiler(self, toTiler: str):
        self.__toTiler = toTiler

    @property
    def fromTiler(self) -> str:
        return self.__fromTiler

    @fromTiler.setter
    def fromTiler(self, fromTiler: str):
        self.__fromTiler = fromTiler

class LinkTopology:

    pass
class MARTE_RSM_InterRepetition(LinkTopology):

    def __init__(self, repetitionShapeDependence: str, isModulo: str):
        self.repetitionShapeDependence = repetitionShapeDependence
        self.isModulo = isModulo
        
    @property
    def repetitionShapeDependence(self) -> str:
        return self.__repetitionShapeDependence

    @repetitionShapeDependence.setter
    def repetitionShapeDependence(self, repetitionShapeDependence: str):
        self.__repetitionShapeDependence = repetitionShapeDependence

    @property
    def isModulo(self) -> str:
        return self.__isModulo

    @isModulo.setter
    def isModulo(self, isModulo: str):
        self.__isModulo = isModulo

class MARTE_RSM_Reshape(LinkTopology):

    def __init__(self, patternShape: str, repetitonShape: str):
        self.patternShape = patternShape
        self.repetitonShape = repetitonShape
        
    @property
    def repetitonShape(self) -> str:
        return self.__repetitonShape

    @repetitonShape.setter
    def repetitonShape(self, repetitonShape: str):
        self.__repetitonShape = repetitonShape

    @property
    def patternShape(self) -> str:
        return self.__patternShape

    @patternShape.setter
    def patternShape(self, patternShape: str):
        self.__patternShape = patternShape

class MARTE_RSM_Tiler(LinkTopology):

    def __init__(self, origin: str, paving: str, fitting: str, tiler: str, MARTE_RSM_Tiler: "RSM_MARTE_ConnectorEnd" = None):
        self.origin = origin
        self.paving = paving
        self.fitting = fitting
        self.tiler = tiler
        self.MARTE_RSM_Tiler = MARTE_RSM_Tiler
        
    @property
    def tiler(self) -> str:
        return self.__tiler

    @tiler.setter
    def tiler(self, tiler: str):
        self.__tiler = tiler

    @property
    def paving(self) -> str:
        return self.__paving

    @paving.setter
    def paving(self, paving: str):
        self.__paving = paving

    @property
    def fitting(self) -> str:
        return self.__fitting

    @fitting.setter
    def fitting(self, fitting: str):
        self.__fitting = fitting

    @property
    def origin(self) -> str:
        return self.__origin

    @origin.setter
    def origin(self, origin: str):
        self.__origin = origin

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

class MARTE_RSM_DefaultLink(LinkTopology):

    pass
class RSM_MARTE_Connector:

    pass
class MARTE_RSM_LinkTopology(ABC):

    pass
class GRM_ResourceUsage:

    pass
class MARTE_GQAM_GaScenario(GRM_ResourceUsage, Time_TimedProcessing):

    def __init__(self, hostDemand: str, hostDemandOps: str, interOccT: str, throughput: str, respT: str, utilization: str, utilizationOnHost: str, MARTE_GQAM_GaScenario: "GQAM_GaWorkloadEvent" = None, MARTE_GQAM_GaScenario492: "GQAM_GaStep" = None, GQAM: set["GQAM_GaStep"] = None, GQAM495: set["GQAM_GaStep"] = None, MARTE_GQAM_GaScenario498: set["GQAM_GaTimedObs"] = None, GRM_ResourceUsage: "MARTE_GRM_ResourceUsage"):
        self.hostDemand = hostDemand
        self.hostDemandOps = hostDemandOps
        self.interOccT = interOccT
        self.throughput = throughput
        self.respT = respT
        self.utilization = utilization
        self.utilizationOnHost = utilizationOnHost
        self.MARTE_GQAM_GaScenario = MARTE_GQAM_GaScenario
        self.MARTE_GQAM_GaScenario492 = MARTE_GQAM_GaScenario492
        self.GQAM = GQAM if GQAM is not None else set()
        self.GQAM495 = GQAM495 if GQAM495 is not None else set()
        self.MARTE_GQAM_GaScenario498 = MARTE_GQAM_GaScenario498 if MARTE_GQAM_GaScenario498 is not None else set()
        
    @property
    def respT(self) -> str:
        return self.__respT

    @respT.setter
    def respT(self, respT: str):
        self.__respT = respT

    @property
    def utilization(self) -> str:
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization

    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def interOccT(self) -> str:
        return self.__interOccT

    @interOccT.setter
    def interOccT(self, interOccT: str):
        self.__interOccT = interOccT

    @property
    def hostDemandOps(self) -> str:
        return self.__hostDemandOps

    @hostDemandOps.setter
    def hostDemandOps(self, hostDemandOps: str):
        self.__hostDemandOps = hostDemandOps

    @property
    def utilizationOnHost(self) -> str:
        return self.__utilizationOnHost

    @utilizationOnHost.setter
    def utilizationOnHost(self, utilizationOnHost: str):
        self.__utilizationOnHost = utilizationOnHost

    @property
    def hostDemand(self) -> str:
        return self.__hostDemand

    @hostDemand.setter
    def hostDemand(self, hostDemand: str):
        self.__hostDemand = hostDemand

    @property
    def MARTE_GQAM_GaScenario498(self):
        return self.__MARTE_GQAM_GaScenario498

    @MARTE_GQAM_GaScenario498.setter
    def MARTE_GQAM_GaScenario498(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaScenario__MARTE_GQAM_GaScenario498", None)
        self.__MARTE_GQAM_GaScenario498 = value if value is not None else set()
        
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
    def GQAM(self):
        return self.__GQAM

    @GQAM.setter
    def GQAM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaScenario__GQAM", None)
        self.__GQAM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MARTE_AnalysisModel"):
                    opp_val = getattr(item, "MARTE_AnalysisModel", None)
                    
                    if opp_val == self:
                        setattr(item, "MARTE_AnalysisModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MARTE_AnalysisModel"):
                    opp_val = getattr(item, "MARTE_AnalysisModel", None)
                    
                    setattr(item, "MARTE_AnalysisModel", self)
                    

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
    def MARTE_GQAM_GaScenario492(self):
        return self.__MARTE_GQAM_GaScenario492

    @MARTE_GQAM_GaScenario492.setter
    def MARTE_GQAM_GaScenario492(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaScenario__MARTE_GQAM_GaScenario492", None)
        self.__MARTE_GQAM_GaScenario492 = value
        
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
    def GQAM495(self):
        return self.__GQAM495

    @GQAM495.setter
    def GQAM495(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaScenario__GQAM495", None)
        self.__GQAM495 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MARTE_AnalysisModel496"):
                    opp_val = getattr(item, "MARTE_AnalysisModel496", None)
                    
                    if opp_val == self:
                        setattr(item, "MARTE_AnalysisModel496", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MARTE_AnalysisModel496"):
                    opp_val = getattr(item, "MARTE_AnalysisModel496", None)
                    
                    setattr(item, "MARTE_AnalysisModel496", self)
                    

class GRM_MARTE_NamedElement:

    pass
class MARTE_GRM_ResourceUsage:

    def __init__(self, execTime: str, allocatedMemory: str, usedMemory: str, powerPeak: str, energy: str, msgSize: str, MARTE_GRM_ResourceUsage: "GRM_MARTE_NamedElement" = None, MARTE_GRM_ResourceUsage146: set["GRM_ResourceUsage"] = None, MARTE_GRM_ResourceUsage148: set["GRM_Resource"] = None):
        self.execTime = execTime
        self.allocatedMemory = allocatedMemory
        self.usedMemory = usedMemory
        self.powerPeak = powerPeak
        self.energy = energy
        self.msgSize = msgSize
        self.MARTE_GRM_ResourceUsage = MARTE_GRM_ResourceUsage
        self.MARTE_GRM_ResourceUsage146 = MARTE_GRM_ResourceUsage146 if MARTE_GRM_ResourceUsage146 is not None else set()
        self.MARTE_GRM_ResourceUsage148 = MARTE_GRM_ResourceUsage148 if MARTE_GRM_ResourceUsage148 is not None else set()
        
    @property
    def msgSize(self) -> str:
        return self.__msgSize

    @msgSize.setter
    def msgSize(self, msgSize: str):
        self.__msgSize = msgSize

    @property
    def execTime(self) -> str:
        return self.__execTime

    @execTime.setter
    def execTime(self, execTime: str):
        self.__execTime = execTime

    @property
    def powerPeak(self) -> str:
        return self.__powerPeak

    @powerPeak.setter
    def powerPeak(self, powerPeak: str):
        self.__powerPeak = powerPeak

    @property
    def allocatedMemory(self) -> str:
        return self.__allocatedMemory

    @allocatedMemory.setter
    def allocatedMemory(self, allocatedMemory: str):
        self.__allocatedMemory = allocatedMemory

    @property
    def usedMemory(self) -> str:
        return self.__usedMemory

    @usedMemory.setter
    def usedMemory(self, usedMemory: str):
        self.__usedMemory = usedMemory

    @property
    def energy(self) -> str:
        return self.__energy

    @energy.setter
    def energy(self, energy: str):
        self.__energy = energy

    @property
    def MARTE_GRM_ResourceUsage146(self):
        return self.__MARTE_GRM_ResourceUsage146

    @MARTE_GRM_ResourceUsage146.setter
    def MARTE_GRM_ResourceUsage146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_ResourceUsage__MARTE_GRM_ResourceUsage146", None)
        self.__MARTE_GRM_ResourceUsage146 = value if value is not None else set()
        
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
    def MARTE_GRM_ResourceUsage148(self):
        return self.__MARTE_GRM_ResourceUsage148

    @MARTE_GRM_ResourceUsage148.setter
    def MARTE_GRM_ResourceUsage148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_ResourceUsage__MARTE_GRM_ResourceUsage148", None)
        self.__MARTE_GRM_ResourceUsage148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GRM_Resource149"):
                    opp_val = getattr(item, "GRM_Resource149", None)
                    
                    if opp_val == self:
                        setattr(item, "GRM_Resource149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GRM_Resource149"):
                    opp_val = getattr(item, "GRM_Resource149", None)
                    
                    setattr(item, "GRM_Resource149", self)
                    

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

class GrService:

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

class MARTE_GRM_Acquire(GrService):

    def __init__(self, isBlocking: str):
        self.isBlocking = isBlocking
        
    @property
    def isBlocking(self) -> str:
        return self.__isBlocking

    @isBlocking.setter
    def isBlocking(self, isBlocking: str):
        self.__isBlocking = isBlocking

class MARTE_GRM_Release(GrService):

    pass
class MARTE_HwGeneral_HwResourceService(GrService):

    def __init__(self, consumption: str, dissipation: str):
        self.consumption = consumption
        self.dissipation = dissipation
        
    @property
    def dissipation(self) -> str:
        return self.__dissipation

    @dissipation.setter
    def dissipation(self, dissipation: str):
        self.__dissipation = dissipation

    @property
    def consumption(self) -> str:
        return self.__consumption

    @consumption.setter
    def consumption(self, consumption: str):
        self.__consumption = consumption

class ProcessingResource:

    pass
class MARTE_GRM_ComputingResource(ProcessingResource):

    pass
class GRM_Scheduler:

    pass
class MARTE_GQAM_GaCommHost(GRM_CommunicationMedia, GRM_Scheduler):

    def __init__(self, throughput: str, utilization: str, GRM_Scheduler: "MARTE_GRM_ProcessingResource", MARTE_Foundations122: "MARTE_GRM_MutualExclusionResource", MARTE_Foundations128: "MARTE_GRM_SchedulableResource"):
        self.throughput = throughput
        self.utilization = utilization
        
    @property
    def utilization(self) -> str:
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization

    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

class GRM_SchedulableResource:

    pass
class MARTE_SW_Concurrency_SwSchedulableResource(GRM_SchedulableResource, SW_Concurrency_SwConcurrentResource):

    def __init__(self, isStaticSchedulingFeature: str, isPreemptable: str, MARTE_SW_Concurrency_SwSchedulableResource: "SW_Concurrency_MARTE_NamedElement" = None, MARTE_SW_Concurrency_SwSchedulableResource324: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwSchedulableResource327: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwSchedulableResource330: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwSchedulableResource333: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwSchedulableResource336: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwSchedulableResource339: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_Foundations131: "MARTE_GRM_SecondaryScheduler", MARTE_Foundations118: "MARTE_GRM_Scheduler", GRM_SchedulableResource: "MARTE_GQAM_GaStep", GRM_SchedulableResource548: "MARTE_PAM_PaRunTInstance"):
        self.isStaticSchedulingFeature = isStaticSchedulingFeature
        self.isPreemptable = isPreemptable
        self.MARTE_SW_Concurrency_SwSchedulableResource = MARTE_SW_Concurrency_SwSchedulableResource
        self.MARTE_SW_Concurrency_SwSchedulableResource324 = MARTE_SW_Concurrency_SwSchedulableResource324 if MARTE_SW_Concurrency_SwSchedulableResource324 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource327 = MARTE_SW_Concurrency_SwSchedulableResource327 if MARTE_SW_Concurrency_SwSchedulableResource327 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource330 = MARTE_SW_Concurrency_SwSchedulableResource330 if MARTE_SW_Concurrency_SwSchedulableResource330 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource333 = MARTE_SW_Concurrency_SwSchedulableResource333 if MARTE_SW_Concurrency_SwSchedulableResource333 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource336 = MARTE_SW_Concurrency_SwSchedulableResource336 if MARTE_SW_Concurrency_SwSchedulableResource336 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource339 = MARTE_SW_Concurrency_SwSchedulableResource339 if MARTE_SW_Concurrency_SwSchedulableResource339 is not None else set()
        
    @property
    def isPreemptable(self) -> str:
        return self.__isPreemptable

    @isPreemptable.setter
    def isPreemptable(self, isPreemptable: str):
        self.__isPreemptable = isPreemptable

    @property
    def isStaticSchedulingFeature(self) -> str:
        return self.__isStaticSchedulingFeature

    @isStaticSchedulingFeature.setter
    def isStaticSchedulingFeature(self, isStaticSchedulingFeature: str):
        self.__isStaticSchedulingFeature = isStaticSchedulingFeature

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource324(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource324

    @MARTE_SW_Concurrency_SwSchedulableResource324.setter
    def MARTE_SW_Concurrency_SwSchedulableResource324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource324", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource324 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement325"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement325", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement325", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement325"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement325", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement325", self)
                    

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
    def MARTE_SW_Concurrency_SwSchedulableResource333(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource333

    @MARTE_SW_Concurrency_SwSchedulableResource333.setter
    def MARTE_SW_Concurrency_SwSchedulableResource333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource333", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource333 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature334"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature334", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature334", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature334"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature334", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature334", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource330(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource330

    @MARTE_SW_Concurrency_SwSchedulableResource330.setter
    def MARTE_SW_Concurrency_SwSchedulableResource330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource330", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource330 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement331"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement331", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement331", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement331"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement331", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement331", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource327(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource327

    @MARTE_SW_Concurrency_SwSchedulableResource327.setter
    def MARTE_SW_Concurrency_SwSchedulableResource327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource327", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource327 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement328"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement328", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement328", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement328"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement328", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement328", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource339(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource339

    @MARTE_SW_Concurrency_SwSchedulableResource339.setter
    def MARTE_SW_Concurrency_SwSchedulableResource339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource339", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource339 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature340"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature340", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature340", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature340"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature340", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature340", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource336(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource336

    @MARTE_SW_Concurrency_SwSchedulableResource336.setter
    def MARTE_SW_Concurrency_SwSchedulableResource336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource336", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource336 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature337"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature337", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature337", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature337"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature337", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature337", self)
                    

class GRM_MutualExclusionResource:

    pass
class MARTE_SW_Interaction_SwMutualExclusionResource(SW_Interaction_SwSynchronizationResource, GRM_MutualExclusionResource):

    def __init__(self, mechanism: str, concurrentAccessProtocol: str, MARTE_SW_Interaction_SwMutualExclusionResource429: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_SwMutualExclusionResource432: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_SwMutualExclusionResource: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_Foundations: "MARTE_GRM_Scheduler"):
        self.mechanism = mechanism
        self.concurrentAccessProtocol = concurrentAccessProtocol
        self.MARTE_SW_Interaction_SwMutualExclusionResource429 = MARTE_SW_Interaction_SwMutualExclusionResource429 if MARTE_SW_Interaction_SwMutualExclusionResource429 is not None else set()
        self.MARTE_SW_Interaction_SwMutualExclusionResource432 = MARTE_SW_Interaction_SwMutualExclusionResource432 if MARTE_SW_Interaction_SwMutualExclusionResource432 is not None else set()
        self.MARTE_SW_Interaction_SwMutualExclusionResource = MARTE_SW_Interaction_SwMutualExclusionResource if MARTE_SW_Interaction_SwMutualExclusionResource is not None else set()
        
    @property
    def concurrentAccessProtocol(self) -> str:
        return self.__concurrentAccessProtocol

    @concurrentAccessProtocol.setter
    def concurrentAccessProtocol(self, concurrentAccessProtocol: str):
        self.__concurrentAccessProtocol = concurrentAccessProtocol

    @property
    def mechanism(self) -> str:
        return self.__mechanism

    @mechanism.setter
    def mechanism(self, mechanism: str):
        self.__mechanism = mechanism

    @property
    def MARTE_SW_Interaction_SwMutualExclusionResource429(self):
        return self.__MARTE_SW_Interaction_SwMutualExclusionResource429

    @MARTE_SW_Interaction_SwMutualExclusionResource429.setter
    def MARTE_SW_Interaction_SwMutualExclusionResource429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_SwMutualExclusionResource__MARTE_SW_Interaction_SwMutualExclusionResource429", None)
        self.__MARTE_SW_Interaction_SwMutualExclusionResource429 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature430"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature430", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature430", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature430"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature430", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature430", self)
                    

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
                if hasattr(item, "SW_Interaction_MARTE_TypedElement427"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement427", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement427", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement427"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement427", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement427", self)
                    

    @property
    def MARTE_SW_Interaction_SwMutualExclusionResource432(self):
        return self.__MARTE_SW_Interaction_SwMutualExclusionResource432

    @MARTE_SW_Interaction_SwMutualExclusionResource432.setter
    def MARTE_SW_Interaction_SwMutualExclusionResource432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_SwMutualExclusionResource__MARTE_SW_Interaction_SwMutualExclusionResource432", None)
        self.__MARTE_SW_Interaction_SwMutualExclusionResource432 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature433"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature433", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature433", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature433"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature433", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature433", self)
                    

class GRM_ComputingResource:

    pass
class MARTE_HwComputing_HwComputingResource(GRM_ComputingResource, HwGeneral_HwResource):

    def __init__(self, op_Frequencies: str, GRM_ComputingResource: "MARTE_GRM_Scheduler", HwGeneral_HwResource: "MARTE_HwGeneral_HwResource"):
        self.op_Frequencies = op_Frequencies
        
    @property
    def op_Frequencies(self) -> str:
        return self.__op_Frequencies

    @op_Frequencies.setter
    def op_Frequencies(self, op_Frequencies: str):
        self.__op_Frequencies = op_Frequencies

class MARTE_GQAM_GaExecHost(GRM_ComputingResource, GRM_Scheduler):

    def __init__(self, commTxOvh: str, commRcvOvh: str, cntxtSwT: str, memSize: str, utilization: str, throughput: str, clockOvh: str, schedPriRange: str, GRM_ComputingResource: "MARTE_GRM_Scheduler", GRM_Scheduler: "MARTE_GRM_ProcessingResource", MARTE_Foundations122: "MARTE_GRM_MutualExclusionResource", MARTE_Foundations128: "MARTE_GRM_SchedulableResource"):
        self.commTxOvh = commTxOvh
        self.commRcvOvh = commRcvOvh
        self.cntxtSwT = cntxtSwT
        self.memSize = memSize
        self.utilization = utilization
        self.throughput = throughput
        self.clockOvh = clockOvh
        self.schedPriRange = schedPriRange
        
    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def commRcvOvh(self) -> str:
        return self.__commRcvOvh

    @commRcvOvh.setter
    def commRcvOvh(self, commRcvOvh: str):
        self.__commRcvOvh = commRcvOvh

    @property
    def utilization(self) -> str:
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization

    @property
    def clockOvh(self) -> str:
        return self.__clockOvh

    @clockOvh.setter
    def clockOvh(self, clockOvh: str):
        self.__clockOvh = clockOvh

    @property
    def schedPriRange(self) -> str:
        return self.__schedPriRange

    @schedPriRange.setter
    def schedPriRange(self, schedPriRange: str):
        self.__schedPriRange = schedPriRange

    @property
    def cntxtSwT(self) -> str:
        return self.__cntxtSwT

    @cntxtSwT.setter
    def cntxtSwT(self, cntxtSwT: str):
        self.__cntxtSwT = cntxtSwT

    @property
    def commTxOvh(self) -> str:
        return self.__commTxOvh

    @commTxOvh.setter
    def commTxOvh(self, commTxOvh: str):
        self.__commTxOvh = commTxOvh

    @property
    def memSize(self) -> str:
        return self.__memSize

    @memSize.setter
    def memSize(self, memSize: str):
        self.__memSize = memSize

class GRM_ProcessingResource:

    pass
class MARTE_GRM_DeviceResource(ProcessingResource):

    pass
class GRM_MARTE_Connector:

    pass
class MARTE_GRM_CommunicationMedia(ProcessingResource):

    def __init__(self, elementSize: str, transmMode: str, blockT: str, packetT: str, capacity: str, MARTE_GRM_CommunicationMedia: "GRM_MARTE_Connector" = None):
        self.elementSize = elementSize
        self.transmMode = transmMode
        self.blockT = blockT
        self.packetT = packetT
        self.capacity = capacity
        self.MARTE_GRM_CommunicationMedia = MARTE_GRM_CommunicationMedia
        
    @property
    def elementSize(self) -> str:
        return self.__elementSize

    @elementSize.setter
    def elementSize(self, elementSize: str):
        self.__elementSize = elementSize

    @property
    def packetT(self) -> str:
        return self.__packetT

    @packetT.setter
    def packetT(self, packetT: str):
        self.__packetT = packetT

    @property
    def transmMode(self) -> str:
        return self.__transmMode

    @transmMode.setter
    def transmMode(self, transmMode: str):
        self.__transmMode = transmMode

    @property
    def capacity(self) -> str:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity

    @property
    def blockT(self) -> str:
        return self.__blockT

    @blockT.setter
    def blockT(self, blockT: str):
        self.__blockT = blockT

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

class Scheduler:

    pass
class MARTE_GRM_SecondaryScheduler(Scheduler):

    pass
class GRM_SecondaryScheduler:

    pass
class GRM_MARTE_InstanceSpecification:

    pass
class GRM_MARTE_Property:

    pass
class MARTE_GRM_Resource:

    def __init__(self, resMult: str, isProtected: str, isActive: str, MARTE_GRM_Resource107: "GRM_MARTE_Classifier" = None, MARTE_GRM_Resource109: "GRM_MARTE_Lifeline" = None, MARTE_GRM_Resource111: "GRM_MARTE_ConnectableElement" = None, MARTE_GRM_Resource: "GRM_MARTE_Property" = None, MARTE_GRM_Resource105: "GRM_MARTE_InstanceSpecification" = None):
        self.resMult = resMult
        self.isProtected = isProtected
        self.isActive = isActive
        self.MARTE_GRM_Resource107 = MARTE_GRM_Resource107
        self.MARTE_GRM_Resource109 = MARTE_GRM_Resource109
        self.MARTE_GRM_Resource111 = MARTE_GRM_Resource111
        self.MARTE_GRM_Resource = MARTE_GRM_Resource
        self.MARTE_GRM_Resource105 = MARTE_GRM_Resource105
        
    @property
    def isProtected(self) -> str:
        return self.__isProtected

    @isProtected.setter
    def isProtected(self, isProtected: str):
        self.__isProtected = isProtected

    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

    @property
    def resMult(self) -> str:
        return self.__resMult

    @resMult.setter
    def resMult(self, resMult: str):
        self.__resMult = resMult

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

class Resource:

    pass
class MARTE_HwGeneral_HwResource(Resource):

    def __init__(self, description: str, frequency: str, MARTE_HwGeneral_HwResource: set["HwGeneral_HwResourceService"] = None, MARTE_HwGeneral_HwResource239: set["HwGeneral_HwResourceService"] = None, MARTE_HwGeneral_HwResource242: set["HwGeneral_HwResource"] = None, MARTE_HwGeneral_HwResource244: set["HwCommunication_HwEndPoint"] = None):
        self.description = description
        self.frequency = frequency
        self.MARTE_HwGeneral_HwResource = MARTE_HwGeneral_HwResource if MARTE_HwGeneral_HwResource is not None else set()
        self.MARTE_HwGeneral_HwResource239 = MARTE_HwGeneral_HwResource239 if MARTE_HwGeneral_HwResource239 is not None else set()
        self.MARTE_HwGeneral_HwResource242 = MARTE_HwGeneral_HwResource242 if MARTE_HwGeneral_HwResource242 is not None else set()
        self.MARTE_HwGeneral_HwResource244 = MARTE_HwGeneral_HwResource244 if MARTE_HwGeneral_HwResource244 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def frequency(self) -> str:
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: str):
        self.__frequency = frequency

    @property
    def MARTE_HwGeneral_HwResource244(self):
        return self.__MARTE_HwGeneral_HwResource244

    @MARTE_HwGeneral_HwResource244.setter
    def MARTE_HwGeneral_HwResource244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource244", None)
        self.__MARTE_HwGeneral_HwResource244 = value if value is not None else set()
        
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
    def MARTE_HwGeneral_HwResource242(self):
        return self.__MARTE_HwGeneral_HwResource242

    @MARTE_HwGeneral_HwResource242.setter
    def MARTE_HwGeneral_HwResource242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource242", None)
        self.__MARTE_HwGeneral_HwResource242 = value if value is not None else set()
        
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
    def MARTE_HwGeneral_HwResource239(self):
        return self.__MARTE_HwGeneral_HwResource239

    @MARTE_HwGeneral_HwResource239.setter
    def MARTE_HwGeneral_HwResource239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource239", None)
        self.__MARTE_HwGeneral_HwResource239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResourceService240"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService240", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResourceService240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResourceService240"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService240", None)
                    
                    setattr(item, "HwGeneral_HwResourceService240", self)
                    

class MARTE_SW_ResourceCore_SwResource(Resource):

    pass
class MARTE_GRM_Scheduler(Resource):

    def __init__(self, isPreemptible: str, schedPolicy: str, otherSchedPolicy: str, schedule: str, MARTE_GRM_Scheduler: set["GRM_ProcessingResource"] = None, MARTE_GRM_Scheduler114: "GRM_ComputingResource" = None, GRM: set["GRM_MutualExclusionResource"] = None, GRM117: set["GRM_SchedulableResource"] = None):
        self.isPreemptible = isPreemptible
        self.schedPolicy = schedPolicy
        self.otherSchedPolicy = otherSchedPolicy
        self.schedule = schedule
        self.MARTE_GRM_Scheduler = MARTE_GRM_Scheduler if MARTE_GRM_Scheduler is not None else set()
        self.MARTE_GRM_Scheduler114 = MARTE_GRM_Scheduler114
        self.GRM = GRM if GRM is not None else set()
        self.GRM117 = GRM117 if GRM117 is not None else set()
        
    @property
    def otherSchedPolicy(self) -> str:
        return self.__otherSchedPolicy

    @otherSchedPolicy.setter
    def otherSchedPolicy(self, otherSchedPolicy: str):
        self.__otherSchedPolicy = otherSchedPolicy

    @property
    def schedPolicy(self) -> str:
        return self.__schedPolicy

    @schedPolicy.setter
    def schedPolicy(self, schedPolicy: str):
        self.__schedPolicy = schedPolicy

    @property
    def schedule(self) -> str:
        return self.__schedule

    @schedule.setter
    def schedule(self, schedule: str):
        self.__schedule = schedule

    @property
    def isPreemptible(self) -> str:
        return self.__isPreemptible

    @isPreemptible.setter
    def isPreemptible(self, isPreemptible: str):
        self.__isPreemptible = isPreemptible

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
    def GRM117(self):
        return self.__GRM117

    @GRM117.setter
    def GRM117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_Scheduler__GRM117", None)
        self.__GRM117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MARTE_Foundations118"):
                    opp_val = getattr(item, "MARTE_Foundations118", None)
                    
                    if opp_val == self:
                        setattr(item, "MARTE_Foundations118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MARTE_Foundations118"):
                    opp_val = getattr(item, "MARTE_Foundations118", None)
                    
                    setattr(item, "MARTE_Foundations118", self)
                    

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
                    

class MARTE_GRM_MutualExclusionResource(Resource):

    def __init__(self, protectKind: str, ceiling: str, otherProtectProtocol: str, GRM121: "GRM_Scheduler" = None):
        self.protectKind = protectKind
        self.ceiling = ceiling
        self.otherProtectProtocol = otherProtectProtocol
        self.GRM121 = GRM121
        
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
    def ceiling(self) -> str:
        return self.__ceiling

    @ceiling.setter
    def ceiling(self, ceiling: str):
        self.__ceiling = ceiling

    @property
    def GRM121(self):
        return self.__GRM121

    @GRM121.setter
    def GRM121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_MutualExclusionResource__GRM121", None)
        self.__GRM121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MARTE_Foundations122"):
                opp_val = getattr(old_value, "MARTE_Foundations122", None)
                if opp_val == self:
                    setattr(old_value, "MARTE_Foundations122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MARTE_Foundations122"):
                opp_val = getattr(value, "MARTE_Foundations122", None)
                setattr(value, "MARTE_Foundations122", self)

class MARTE_GRM_CommunicationEndPoint(Resource):

    def __init__(self, packetSize: str):
        self.packetSize = packetSize
        
    @property
    def packetSize(self) -> str:
        return self.__packetSize

    @packetSize.setter
    def packetSize(self, packetSize: str):
        self.__packetSize = packetSize

class MARTE_GRM_SynchronizationResource(Resource):

    pass
class MARTE_PAM_PaLogicalResource(Resource):

    def __init__(self, utilization: str, throughput: str, poolSize: str):
        self.utilization = utilization
        self.throughput = throughput
        self.poolSize = poolSize
        
    @property
    def throughput(self) -> str:
        return self.__throughput

    @throughput.setter
    def throughput(self, throughput: str):
        self.__throughput = throughput

    @property
    def poolSize(self) -> str:
        return self.__poolSize

    @poolSize.setter
    def poolSize(self, poolSize: str):
        self.__poolSize = poolSize

    @property
    def utilization(self) -> str:
        return self.__utilization

    @utilization.setter
    def utilization(self, utilization: str):
        self.__utilization = utilization

class MARTE_GRM_ConcurrencyResource(Resource):

    pass
class MARTE_GRM_TimingResource(Resource):

    pass
class MARTE_GRM_SchedulableResource(Resource):

    def __init__(self, schedParams: str, GRM124: "GRM_SecondaryScheduler" = None, GRM127: "GRM_Scheduler" = None):
        self.schedParams = schedParams
        self.GRM124 = GRM124
        self.GRM127 = GRM127
        
    @property
    def schedParams(self) -> str:
        return self.__schedParams

    @schedParams.setter
    def schedParams(self, schedParams: str):
        self.__schedParams = schedParams

    @property
    def GRM127(self):
        return self.__GRM127

    @GRM127.setter
    def GRM127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_SchedulableResource__GRM127", None)
        self.__GRM127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MARTE_Foundations128"):
                opp_val = getattr(old_value, "MARTE_Foundations128", None)
                if opp_val == self:
                    setattr(old_value, "MARTE_Foundations128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MARTE_Foundations128"):
                opp_val = getattr(value, "MARTE_Foundations128", None)
                setattr(value, "MARTE_Foundations128", self)

    @property
    def GRM124(self):
        return self.__GRM124

    @GRM124.setter
    def GRM124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_SchedulableResource__GRM124", None)
        self.__GRM124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MARTE_Foundations125"):
                opp_val = getattr(old_value, "MARTE_Foundations125", None)
                if opp_val == self:
                    setattr(old_value, "MARTE_Foundations125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MARTE_Foundations125"):
                opp_val = getattr(value, "MARTE_Foundations125", None)
                setattr(value, "MARTE_Foundations125", self)

class MARTE_GRM_ProcessingResource(Resource):

    def __init__(self, speedFactor: str, MARTE_GRM_ProcessingResource: "GRM_Scheduler" = None):
        self.speedFactor = speedFactor
        self.MARTE_GRM_ProcessingResource = MARTE_GRM_ProcessingResource
        
    @property
    def speedFactor(self) -> str:
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

class MARTE_GRM_StorageResource(Resource):

    def __init__(self, elementSize: str):
        self.elementSize = elementSize
        
    @property
    def elementSize(self) -> str:
        return self.__elementSize

    @elementSize.setter
    def elementSize(self, elementSize: str):
        self.__elementSize = elementSize

class GRM_MARTE_ConnectableElement:

    pass
class GRM_MARTE_Lifeline:

    pass
class GRM_MARTE_Classifier:

    pass
class Time_TimedElement:

    pass
class Time_MARTE_ValueSpecification:

    pass
class TimedElement:

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
class MARTE_Time_TimedElement(ABC):

    pass
class Time_MARTE_Message:

    pass
class Time_MARTE_Behavior:

    pass
class Time_MARTE_Action:

    pass
class MARTE_Time_TimedProcessing(TimedElement):

    pass
class Time_MARTE_TimeEvent:

    pass
class MARTE_Time_TimedEvent(TimedElement):

    def __init__(self, repetition: str, MARTE_Time_TimedEvent: "Time_MARTE_TimeEvent" = None, MARTE_Time_TimedEvent87: "Time_MARTE_ValueSpecification" = None):
        self.repetition = repetition
        self.MARTE_Time_TimedEvent = MARTE_Time_TimedEvent
        self.MARTE_Time_TimedEvent87 = MARTE_Time_TimedEvent87
        
    @property
    def repetition(self) -> str:
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

class Time_MARTE_DurationObservation:

    pass
class MARTE_Time_TimedDurationObservation(TimedElement):

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

class Time_MARTE_TimeObservation:

    pass
class MARTE_Time_TimedInstantObservation(TimedElement):

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

class Time_ClockType:

    pass
class Time_MARTE_InstanceSpecification:

    pass
class MARTE_Time_Clock:

    def __init__(self, standard: str, MARTE_Time_Clock58: "Time_MARTE_Property" = None, MARTE_Time_Clock60: "Time_MARTE_Event" = None, MARTE_Time_Clock: "Time_MARTE_InstanceSpecification" = None, MARTE_Time_Clock53: "Time_ClockType" = None, MARTE_Time_Clock55: "NFPs_Unit" = None):
        self.standard = standard
        self.MARTE_Time_Clock58 = MARTE_Time_Clock58
        self.MARTE_Time_Clock60 = MARTE_Time_Clock60
        self.MARTE_Time_Clock = MARTE_Time_Clock
        self.MARTE_Time_Clock53 = MARTE_Time_Clock53
        self.MARTE_Time_Clock55 = MARTE_Time_Clock55
        
    @property
    def standard(self) -> str:
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

class Time_MARTE_Namespace:

    pass
class MARTE_Time_TimedDomain:

    pass
class Alloc_MARTE_Abstraction:

    pass
class Time_MARTE_Class:

    pass
class Time_MARTE_Operation:

    pass
class Time_MARTE_Enumeration:

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
class MARTE_Alloc_AllocateActivityGroup:

    def __init__(self, isUnique: str, MARTE_Alloc_AllocateActivityGroup: "Alloc_MARTE_ActivityPartition" = None):
        self.isUnique = isUnique
        self.MARTE_Alloc_AllocateActivityGroup = MARTE_Alloc_AllocateActivityGroup
        
    @property
    def isUnique(self) -> str:
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

class Alloc_Allocated:

    pass
class Alloc_MARTE_NamedElement:

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
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def nature(self) -> str:
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
                    

class NFPs_NfpConstraint:

    pass
class MARTE_Time_TimedConstraint(NFPs_NfpConstraint, Time_TimedElement):

    def __init__(self, interpretation: str, NFPs_NfpConstraint: "MARTE_Alloc_NfpRefine", NFPs_NfpConstraint38: "MARTE_Alloc_Assign", NFPs_NfpConstraint49: "MARTE_Alloc_Allocate"):
        self.interpretation = interpretation
        
    @property
    def interpretation(self) -> str:
        return self.__interpretation

    @interpretation.setter
    def interpretation(self, interpretation: str):
        self.__interpretation = interpretation

class MARTE_Time_ClockConstraint(NFPs_NfpConstraint, Time_TimedElement):

    def __init__(self, isCoincidenceBased: str, isPrecedenceBased: bool, isChronometricBased: str, NFPs_NfpConstraint: "MARTE_Alloc_NfpRefine", NFPs_NfpConstraint38: "MARTE_Alloc_Assign", NFPs_NfpConstraint49: "MARTE_Alloc_Allocate"):
        self.isCoincidenceBased = isCoincidenceBased
        self.isPrecedenceBased = isPrecedenceBased
        self.isChronometricBased = isChronometricBased
        
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

    @property
    def isCoincidenceBased(self) -> str:
        return self.__isCoincidenceBased

    @isCoincidenceBased.setter
    def isCoincidenceBased(self, isCoincidenceBased: str):
        self.__isCoincidenceBased = isCoincidenceBased

class Alloc_MARTE_Dependency:

    pass
class MARTE_Alloc_NfpRefine:

    pass
class Alloc_MARTE_ActivityPartition:

    pass
class TupleType:

    pass
class MARTE_NFPs_NfpType(TupleType):

    pass
class CoreElements_Mode:

    pass
class NFPs_MARTE_Constraint:

    pass
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

class MARTE_Alloc_Allocated:

    def __init__(self, kind: str, MARTE_Alloc_Allocated: "Alloc_MARTE_NamedElement" = None, MARTE_Alloc_Allocated29: set["Alloc_Allocated"] = None, MARTE_Alloc_Allocated31: set["Alloc_Allocated"] = None):
        self.kind = kind
        self.MARTE_Alloc_Allocated = MARTE_Alloc_Allocated
        self.MARTE_Alloc_Allocated29 = MARTE_Alloc_Allocated29 if MARTE_Alloc_Allocated29 is not None else set()
        self.MARTE_Alloc_Allocated31 = MARTE_Alloc_Allocated31 if MARTE_Alloc_Allocated31 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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
                    

class NFPs_MARTE_EnumerationLiteral:

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

class NFPs_Unit:

    pass
class MARTE_NFPs_Unit:

    def __init__(self, convFactor: str, convOffset: str, MARTE_NFPs_Unit: "NFPs_Unit" = None, MARTE_NFPs_Unit3: "NFPs_MARTE_EnumerationLiteral" = None):
        self.convFactor = convFactor
        self.convOffset = convOffset
        self.MARTE_NFPs_Unit = MARTE_NFPs_Unit
        self.MARTE_NFPs_Unit3 = MARTE_NFPs_Unit3
        
    @property
    def convFactor(self) -> str:
        return self.__convFactor

    @convFactor.setter
    def convFactor(self, convFactor: str):
        self.__convFactor = convFactor

    @property
    def convOffset(self) -> str:
        return self.__convOffset

    @convOffset.setter
    def convOffset(self, convOffset: str):
        self.__convOffset = convOffset

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

class NFPs_MARTE_Property:

    pass
class MARTE_NFPs_Nfp:

    pass