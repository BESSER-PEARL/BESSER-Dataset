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
class AllocationEndKind(Enum):
    pass
class WritePolicy(Enum): 
    writeBack = "writeBack"
    writeThrough = "writeThrough"
    other = "other"
    undef = "undef"
class FlowDirectionKind(Enum):
    inout = "inout"
    in_ = "in_"
    out = "out"
class VariableDirectionKind(Enum):
    in_ = "in_"
    out = "out"
    inout = "inout"
class ClientServerKind(Enum):
    required = "required"
    provided = "provided"
    proreq = "proreq"
class PLD_Class(Enum):
    symetricalArray = "symetricalArray"
    rowBased = "rowBased"
    seaOfGates = "seaOfGates"
    hierarchicalPLD = "hierarchicalPLD"
    other = "other"
    undef = "undef"
class ROM_Type(Enum):
    maskedROM = "maskedROM"
    EPROM = "EPROM"
    OTP_EPROM = "OTP_EPROM"
    EEPROM = "EEPROM"
    Flash = "Flash"
    other = "other"
    undef = "undef"
class NotificationResourceKind(Enum):
    Event = "Event"
    Barrier = "Barrier"
    Undef = "Undef"
    Other = "Other"
class ExecutionKind(Enum):
    deferred = "deferred"
    remoteImmediate = "remoteImmediate"
    localImmediate = "localImmediate"
class InterruptKind(Enum):
    HardwareInterruption = "HardwareInterruption"
    ProcessorDetectedException = "ProcessorDetectedException"
    ProgrammedException = "ProgrammedException"
    Undef = "Undef"
    Other = "Other"
class QueuePolicyKind(Enum):
    FIFO = "FIFO"
    LIFO = "LIFO"
    Priority = "Priority"
    Undef = "Undef"
    Other = "Other"
class AllocationNature(Enum):
    spatialDistribution = "spatialDistribution"
    timeScheduling = "timeScheduling"
class ConstraintKind(Enum):
    required = "required"
    offered = "offered"
    contract = "contract"
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
class MutualExclusionResourceKind(Enum):
    BooleanSemaphore = "BooleanSemaphore"
    CountSemaphore = "CountSemaphore"
    Mutex = "Mutex"
    Undef = "Undef"
    Other = "Other"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"
class AllocationKind(Enum): 
	pass
class AssignmentNature(Enum): 
	pass
class PLD_Technology(Enum):
    SRAM = "SRAM"
    antifuse = "antifuse"
    flash = "flash"
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
class PortSpecificationKind(Enum):
    atomic = "atomic"
    interfaceBased = "interfaceBased"
    featureBased = "featureBased"
class OptimallityCriterionKind(Enum):
    meetHardDeadlines = "meetHardDeadlines"
    minimizeMissedDeadlines = "minimizeMissedDeadlines"
    minimizedMeanTardiness = "minimizedMeanTardiness"
    undef = "undef"
    other = "other"
class SynchronizationKind(Enum):
    synchronous = "synchronous"
    asynchronous = "asynchronous"
    delayedSynchronous = "delayedSynchronous"
    rendezVous = "rendezVous"
    other = "other"
class ConditionType(Enum):
    temperature = "temperature"
    humidity = "humidity"
    altitude = "altitude"
    vibration = "vibration"
    shock = "shock"
    other = "other"
    undef = "undef"
class AssignmentKind(Enum):
    structural = "structural"
    behavioral = "behavioral"
    hybrid = "hybrid"
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
class NotificationKind(Enum):
    Memorized = "Memorized"
    Bounded = "Bounded"
    Memoryless = "Memoryless"
    Undef = "Undef"
    Other = "Other"
class PoolMgtPolicyKind(Enum):
    infiniteWait = "infiniteWait"
    timedWait = "timedWait"
    dynamic = "dynamic"
    exception = "exception"
    other = "other"
class AccessPolicyKind(Enum):
    Read = "Read"
    Write = "Write"
    ReadWrite = "ReadWrite"
    Undef = "Undef"
    Other = "Other"
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
class CacheType(Enum):
    data = "data"
    instruction = "instruction"
    unified = "unified"
    other = "other"
    undef = "undef"
class Repl_Policy(Enum):
    LRU = "LRU"
    NFU = "NFU"
    FIFO = "FIFO"
    random = "random"
    other = "other"
    undef = "undef"


############################################
# Definition of Classes
############################################

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
class HwDeviceFunction_HwDeviceFunction:

    pass
class GRM_DeviceResource:

    pass
class HwTiming_HwClock:

    pass
class HwMemory_MemoryOrganization:

    pass
class HwMemory:

    pass
class MARTE_HwMemory_HwDrive(HwMemory):

    pass
class MARTE_HwMemory_HwCache(HwMemory):

    def __init__(self, type: str, repl_Policy: str, writePolicy: str, MARTE_HwMemory_HwCache: "NFP_Natural" = None, MARTE_HwMemory_HwCache467: "HwMemory_CacheStructure" = None):
        self.type = type
        self.repl_Policy = repl_Policy
        self.writePolicy = writePolicy
        self.MARTE_HwMemory_HwCache = MARTE_HwMemory_HwCache
        self.MARTE_HwMemory_HwCache467 = MARTE_HwMemory_HwCache467
        
        pass
    @property
    def writePolicy(self):
        return self.__writePolicy

    @writePolicy.setter
    def writePolicy(self, writePolicy: str):
        self.__writePolicy = writePolicy


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def repl_Policy(self):
        return self.__repl_Policy

    @repl_Policy.setter
    def repl_Policy(self, repl_Policy: str):
        self.__repl_Policy = repl_Policy


    @property
    def MARTE_HwMemory_HwCache467(self):
        return self.__MARTE_HwMemory_HwCache467

    @MARTE_HwMemory_HwCache467.setter
    def MARTE_HwMemory_HwCache467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwCache__MARTE_HwMemory_HwCache467", None)
        self.__MARTE_HwMemory_HwCache467 = value
        
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
            if hasattr(old_value, "NFP_Natural465"):
                opp_val = getattr(old_value, "NFP_Natural465", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Natural465", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Natural465"):
                opp_val = getattr(value, "NFP_Natural465", None)
                setattr(value, "NFP_Natural465", self)

class MARTE_HwMemory_HwRAM(HwMemory):

    def __init__(self, repl_Policy: str, writePolicy: str, MARTE_HwMemory_HwRAM: "HwMemory_MemoryOrganization" = None, MARTE_HwMemory_HwRAM449: "NFP_Boolean" = None, MARTE_HwMemory_HwRAM452: "NFP_Boolean" = None, MARTE_HwMemory_HwRAM455: "NFP_Boolean" = None):
        self.repl_Policy = repl_Policy
        self.writePolicy = writePolicy
        self.MARTE_HwMemory_HwRAM = MARTE_HwMemory_HwRAM
        self.MARTE_HwMemory_HwRAM449 = MARTE_HwMemory_HwRAM449
        self.MARTE_HwMemory_HwRAM452 = MARTE_HwMemory_HwRAM452
        self.MARTE_HwMemory_HwRAM455 = MARTE_HwMemory_HwRAM455
        
        pass
    @property
    def repl_Policy(self):
        return self.__repl_Policy

    @repl_Policy.setter
    def repl_Policy(self, repl_Policy: str):
        self.__repl_Policy = repl_Policy


    @property
    def writePolicy(self):
        return self.__writePolicy

    @writePolicy.setter
    def writePolicy(self, writePolicy: str):
        self.__writePolicy = writePolicy


    @property
    def MARTE_HwMemory_HwRAM449(self):
        return self.__MARTE_HwMemory_HwRAM449

    @MARTE_HwMemory_HwRAM449.setter
    def MARTE_HwMemory_HwRAM449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwRAM__MARTE_HwMemory_HwRAM449", None)
        self.__MARTE_HwMemory_HwRAM449 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Boolean450"):
                opp_val = getattr(old_value, "NFP_Boolean450", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Boolean450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Boolean450"):
                opp_val = getattr(value, "NFP_Boolean450", None)
                setattr(value, "NFP_Boolean450", self)

    @property
    def MARTE_HwMemory_HwRAM452(self):
        return self.__MARTE_HwMemory_HwRAM452

    @MARTE_HwMemory_HwRAM452.setter
    def MARTE_HwMemory_HwRAM452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwRAM__MARTE_HwMemory_HwRAM452", None)
        self.__MARTE_HwMemory_HwRAM452 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Boolean453"):
                opp_val = getattr(old_value, "NFP_Boolean453", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Boolean453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Boolean453"):
                opp_val = getattr(value, "NFP_Boolean453", None)
                setattr(value, "NFP_Boolean453", self)

    @property
    def MARTE_HwMemory_HwRAM455(self):
        return self.__MARTE_HwMemory_HwRAM455

    @MARTE_HwMemory_HwRAM455.setter
    def MARTE_HwMemory_HwRAM455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwMemory_HwRAM__MARTE_HwMemory_HwRAM455", None)
        self.__MARTE_HwMemory_HwRAM455 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Boolean456"):
                opp_val = getattr(old_value, "NFP_Boolean456", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Boolean456", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Boolean456"):
                opp_val = getattr(value, "NFP_Boolean456", None)
                setattr(value, "NFP_Boolean456", self)

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

class MARTE_HwMemory_MemoryOrganization:

    pass
class MARTE_HwMemory_CacheStructure:

    pass
class MARTE_HwMemory_HwROM(HwMemory):

    def __init__(self, type: str, MARTE_HwMemory_HwROM: "HwMemory_MemoryOrganization" = None):
        self.type = type
        self.MARTE_HwMemory_HwROM = MARTE_HwMemory_HwROM
        
        pass
    @property
    def type(self):
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
            if hasattr(old_value, "HwMemory_MemoryOrganization458"):
                opp_val = getattr(old_value, "HwMemory_MemoryOrganization458", None)
                if opp_val == self:
                    setattr(old_value, "HwMemory_MemoryOrganization458", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HwMemory_MemoryOrganization458"):
                opp_val = getattr(value, "HwMemory_MemoryOrganization458", None)
                setattr(value, "HwMemory_MemoryOrganization458", self)

class MARTE_HwMemory_Timing:

    pass
class HwMemory_Timing:

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
class MARTE_HwCommunication_HwPort(HwEndPoint):

    pass
class GRM_CommunicationEndPoint:

    pass
class NFP_Boolean:

    pass
class HwStorageManager:

    pass
class MARTE_HwStorageManager_HwMMU(HwStorageManager):

    pass
class HwCommunication_HwCommunicationResource:

    pass
class MARTE_HwCommunication_HwEndPoint(HwCommunication_HwCommunicationResource, GRM_CommunicationEndPoint):

    pass
class GRM_CommunicationMedia:

    pass
class MARTE_HwCommunication_HwMedia(HwCommunication_HwCommunicationResource, GRM_CommunicationMedia):

    pass
class HwCommunication_HwMedia:

    pass
class HwCommunicationResource:

    pass
class MARTE_HwCommunication_HwArbiter(HwCommunicationResource):

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
class HwComputing_HwComputingResource:

    pass
class HwMedia:

    pass
class MARTE_HwCommunication_HwConnection(HwMedia):

    pass
class MARTE_HwCommunication_HwBridge(HwMedia):

    pass
class MARTE_HwCommunication_HwBus(HwMedia):

    pass
class HwCommunication_HwArbiter:

    pass
class MARTE_HwStorageManager_HwDMA(HwCommunication_HwArbiter, HwStorageManager_HwStorageManager):

    pass
class HwComputing_PLD_Organization:

    pass
class PAM_MARTE_NamedElement:

    pass
class GQAM_GaCommStep:

    pass
class PAM_PaStep:

    pass
class MARTE_PAM_PaCommStep(PAM_PaStep, GQAM_GaCommStep):

    pass
class MARTE_PAM_PaRunTInstance:

    def __init__(self, unbddPool: str, MARTE_PAM_PaRunTInstance: "NFP_Integer" = None, MARTE_PAM_PaRunTInstance1106: "GRM_SchedulableResource" = None, MARTE_PAM_PaRunTInstance1109: "GQAM_GaExecHost" = None, MARTE_PAM_PaRunTInstance1112: "NFP_Real" = None, MARTE_PAM_PaRunTInstance1115: "NFP_Frequency" = None, MARTE_PAM_PaRunTInstance1118: "PAM_MARTE_NamedElement" = None):
        self.unbddPool = unbddPool
        self.MARTE_PAM_PaRunTInstance = MARTE_PAM_PaRunTInstance
        self.MARTE_PAM_PaRunTInstance1106 = MARTE_PAM_PaRunTInstance1106
        self.MARTE_PAM_PaRunTInstance1109 = MARTE_PAM_PaRunTInstance1109
        self.MARTE_PAM_PaRunTInstance1112 = MARTE_PAM_PaRunTInstance1112
        self.MARTE_PAM_PaRunTInstance1115 = MARTE_PAM_PaRunTInstance1115
        self.MARTE_PAM_PaRunTInstance1118 = MARTE_PAM_PaRunTInstance1118
        
        pass
    @property
    def unbddPool(self):
        return self.__unbddPool

    @unbddPool.setter
    def unbddPool(self, unbddPool: str):
        self.__unbddPool = unbddPool


    @property
    def MARTE_PAM_PaRunTInstance1118(self):
        return self.__MARTE_PAM_PaRunTInstance1118

    @MARTE_PAM_PaRunTInstance1118.setter
    def MARTE_PAM_PaRunTInstance1118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance1118", None)
        self.__MARTE_PAM_PaRunTInstance1118 = value
        
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
    def MARTE_PAM_PaRunTInstance1115(self):
        return self.__MARTE_PAM_PaRunTInstance1115

    @MARTE_PAM_PaRunTInstance1115.setter
    def MARTE_PAM_PaRunTInstance1115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance1115", None)
        self.__MARTE_PAM_PaRunTInstance1115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Frequency1116"):
                opp_val = getattr(old_value, "NFP_Frequency1116", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Frequency1116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Frequency1116"):
                opp_val = getattr(value, "NFP_Frequency1116", None)
                setattr(value, "NFP_Frequency1116", self)

    @property
    def MARTE_PAM_PaRunTInstance1112(self):
        return self.__MARTE_PAM_PaRunTInstance1112

    @MARTE_PAM_PaRunTInstance1112.setter
    def MARTE_PAM_PaRunTInstance1112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance1112", None)
        self.__MARTE_PAM_PaRunTInstance1112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Real1113"):
                opp_val = getattr(old_value, "NFP_Real1113", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Real1113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Real1113"):
                opp_val = getattr(value, "NFP_Real1113", None)
                setattr(value, "NFP_Real1113", self)

    @property
    def MARTE_PAM_PaRunTInstance1106(self):
        return self.__MARTE_PAM_PaRunTInstance1106

    @MARTE_PAM_PaRunTInstance1106.setter
    def MARTE_PAM_PaRunTInstance1106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance1106", None)
        self.__MARTE_PAM_PaRunTInstance1106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GRM_SchedulableResource1107"):
                opp_val = getattr(old_value, "GRM_SchedulableResource1107", None)
                if opp_val == self:
                    setattr(old_value, "GRM_SchedulableResource1107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GRM_SchedulableResource1107"):
                opp_val = getattr(value, "GRM_SchedulableResource1107", None)
                setattr(value, "GRM_SchedulableResource1107", self)

    @property
    def MARTE_PAM_PaRunTInstance1109(self):
        return self.__MARTE_PAM_PaRunTInstance1109

    @MARTE_PAM_PaRunTInstance1109.setter
    def MARTE_PAM_PaRunTInstance1109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaRunTInstance__MARTE_PAM_PaRunTInstance1109", None)
        self.__MARTE_PAM_PaRunTInstance1109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GQAM_GaExecHost1110"):
                opp_val = getattr(old_value, "GQAM_GaExecHost1110", None)
                if opp_val == self:
                    setattr(old_value, "GQAM_GaExecHost1110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GQAM_GaExecHost1110"):
                opp_val = getattr(value, "GQAM_GaExecHost1110", None)
                setattr(value, "GQAM_GaExecHost1110", self)

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
            if hasattr(old_value, "NFP_Integer1104"):
                opp_val = getattr(old_value, "NFP_Integer1104", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Integer1104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Integer1104"):
                opp_val = getattr(value, "NFP_Integer1104", None)
                setattr(value, "NFP_Integer1104", self)

class GaExecHost:

    pass
class MARTE_SAM_SaExecHost(GaExecHost):

    pass
class MutualExclusionResource:

    pass
class MARTE_SAM_SaSharedResource(MutualExclusionResource):

    pass
class GaCommHost:

    pass
class MARTE_SAM_SaCommHost(GaCommHost):

    pass
class SAM_MARTE_BehavioralFeature:

    pass
class SAM_SaSharedResource:

    pass
class GaAnalysisContext:

    pass
class MARTE_SAM_SaAnalysisContext(GaAnalysisContext):

    def __init__(self, optCriterion: str, MARTE_SAM_SaAnalysisContext: "NFP_Boolean" = None):
        self.optCriterion = optCriterion
        self.MARTE_SAM_SaAnalysisContext = MARTE_SAM_SaAnalysisContext
        
        pass
    @property
    def optCriterion(self):
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
            if hasattr(old_value, "NFP_Boolean983"):
                opp_val = getattr(old_value, "NFP_Boolean983", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Boolean983", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Boolean983"):
                opp_val = getattr(value, "NFP_Boolean983", None)
                setattr(value, "NFP_Boolean983", self)

class GQAM_MARTE_Classifier:

    pass
class GaCommStep:

    pass
class MARTE_SAM_SaCommStep(GaCommStep):

    pass
class SAM_MARTE_NamedElement:

    pass
class MARTE_SAM_SaEndtoEndFlow:

    pass
class SchedulableResource:

    pass
class MARTE_GQAM_GaCommChannel(SchedulableResource):

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

    pass
class MARTE_GQAM_GaWorkloadBehavior:

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

    def __init__(self, laxity: str, MARTE_GQAM_GaTimedObs: set["GQAM_MARTE_TimeObservation"] = None, MARTE_GQAM_GaTimedObs931: set["GQAM_MARTE_TimeObservation"] = None):
        self.laxity = laxity
        self.MARTE_GQAM_GaTimedObs = MARTE_GQAM_GaTimedObs if MARTE_GQAM_GaTimedObs is not None else set()
        self.MARTE_GQAM_GaTimedObs931 = MARTE_GQAM_GaTimedObs931 if MARTE_GQAM_GaTimedObs931 is not None else set()
        
        pass
    @property
    def laxity(self):
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
    def MARTE_GQAM_GaTimedObs931(self):
        return self.__MARTE_GQAM_GaTimedObs931

    @MARTE_GQAM_GaTimedObs931.setter
    def MARTE_GQAM_GaTimedObs931(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GQAM_GaTimedObs__MARTE_GQAM_GaTimedObs931", None)
        self.__MARTE_GQAM_GaTimedObs931 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_MARTE_TimeObservation932"):
                    opp_val = getattr(item, "GQAM_MARTE_TimeObservation932", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_MARTE_TimeObservation932", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_MARTE_TimeObservation932"):
                    opp_val = getattr(item, "GQAM_MARTE_TimeObservation932", None)
                    
                    setattr(item, "GQAM_MARTE_TimeObservation932", self)
                    

class GQAM_MARTE_Operation:

    pass
class GaStep:

    pass
class MARTE_GQAM_GaCommStep(GaStep):

    pass
class MARTE_GQAM_GaAcqStep(GaStep):

    pass
class MARTE_GQAM_GaRelStep(GaStep):

    pass
class MARTE_PAM_PaStep(GaStep):

    def __init__(self, extOpDemand: str, MARTE_PAM_PaStep: "NFP_Boolean" = None, MARTE_PAM_PaStep1082: set["NFP_Real"] = None, MARTE_PAM_PaStep1085: set["GQAM_GaScenario"] = None, MARTE_PAM_PaStep1088: set["NFP_Real"] = None):
        self.extOpDemand = extOpDemand
        self.MARTE_PAM_PaStep = MARTE_PAM_PaStep
        self.MARTE_PAM_PaStep1082 = MARTE_PAM_PaStep1082 if MARTE_PAM_PaStep1082 is not None else set()
        self.MARTE_PAM_PaStep1085 = MARTE_PAM_PaStep1085 if MARTE_PAM_PaStep1085 is not None else set()
        self.MARTE_PAM_PaStep1088 = MARTE_PAM_PaStep1088 if MARTE_PAM_PaStep1088 is not None else set()
        
        pass
    @property
    def extOpDemand(self):
        return self.__extOpDemand

    @extOpDemand.setter
    def extOpDemand(self, extOpDemand: str):
        self.__extOpDemand = extOpDemand


    @property
    def MARTE_PAM_PaStep1082(self):
        return self.__MARTE_PAM_PaStep1082

    @MARTE_PAM_PaStep1082.setter
    def MARTE_PAM_PaStep1082(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaStep__MARTE_PAM_PaStep1082", None)
        self.__MARTE_PAM_PaStep1082 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_Real1083"):
                    opp_val = getattr(item, "NFP_Real1083", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_Real1083", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_Real1083"):
                    opp_val = getattr(item, "NFP_Real1083", None)
                    
                    setattr(item, "NFP_Real1083", self)
                    

    @property
    def MARTE_PAM_PaStep1085(self):
        return self.__MARTE_PAM_PaStep1085

    @MARTE_PAM_PaStep1085.setter
    def MARTE_PAM_PaStep1085(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaStep__MARTE_PAM_PaStep1085", None)
        self.__MARTE_PAM_PaStep1085 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GQAM_GaScenario1086"):
                    opp_val = getattr(item, "GQAM_GaScenario1086", None)
                    
                    if opp_val == self:
                        setattr(item, "GQAM_GaScenario1086", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GQAM_GaScenario1086"):
                    opp_val = getattr(item, "GQAM_GaScenario1086", None)
                    
                    setattr(item, "GQAM_GaScenario1086", self)
                    

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
            if hasattr(old_value, "NFP_Boolean1080"):
                opp_val = getattr(old_value, "NFP_Boolean1080", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Boolean1080", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Boolean1080"):
                opp_val = getattr(value, "NFP_Boolean1080", None)
                setattr(value, "NFP_Boolean1080", self)

    @property
    def MARTE_PAM_PaStep1088(self):
        return self.__MARTE_PAM_PaStep1088

    @MARTE_PAM_PaStep1088.setter
    def MARTE_PAM_PaStep1088(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_PAM_PaStep__MARTE_PAM_PaStep1088", None)
        self.__MARTE_PAM_PaStep1088 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_Real1089"):
                    opp_val = getattr(item, "NFP_Real1089", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_Real1089", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_Real1089"):
                    opp_val = getattr(item, "NFP_Real1089", None)
                    
                    setattr(item, "NFP_Real1089", self)
                    

class MARTE_SAM_SaStep(GaStep):

    pass
class MARTE_PAM_PaResPassStep(GaStep):

    pass
class MARTE_GQAM_GaRequestedService(GaStep):

    pass
class IntegerInterval:

    pass
class GaScenario:

    pass
class MARTE_GQAM_GaStep(GaScenario):

    pass
class GQAM_GaTimedObs:

    pass
class GQAM_GaStep:

    pass
class GQAM_GaRequestedService:

    pass
class MARTE_PAM_PaRequestedStep(PAM_PaStep, GQAM_GaRequestedService):

    pass
class GQAM_GaExecHost:

    pass
class GQAM_GaWorkloadEvent:

    pass
class Time_TimedProcessing:

    pass
class MARTE_GQAM_GaWorkloadGenerator:

    pass
class GCM_MARTE_Behavior:

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

    pass
class GQAM_MARTE_NamedElement:

    pass
class MARTE_GQAM_GaEventTrace:

    def __init__(self, content: str, format: str, location: str, MARTE_GQAM_GaEventTrace: "GQAM_MARTE_NamedElement" = None):
        self.content = content
        self.format = format
        self.location = location
        self.MARTE_GQAM_GaEventTrace = MARTE_GQAM_GaEventTrace
        
        pass
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
    def content(self):
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

class GQAM_MARTE_Behavior:

    pass
class MARTE_GCM_FlowSpecification:

    pass
class MARTE_GCM_ClientServerSpecification:

    pass
class MARTE_GCM_DataPool:

    def __init__(self, ordering: str, MARTE_GCM_DataPool829: "GCM_MARTE_Behavior" = None, MARTE_GCM_DataPool831: "GCM_MARTE_Behavior" = None, MARTE_GCM_DataPool: "GCM_MARTE_Property" = None):
        self.ordering = ordering
        self.MARTE_GCM_DataPool829 = MARTE_GCM_DataPool829
        self.MARTE_GCM_DataPool831 = MARTE_GCM_DataPool831
        self.MARTE_GCM_DataPool = MARTE_GCM_DataPool
        
        pass
    @property
    def ordering(self):
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering


    @property
    def MARTE_GCM_DataPool829(self):
        return self.__MARTE_GCM_DataPool829

    @MARTE_GCM_DataPool829.setter
    def MARTE_GCM_DataPool829(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_DataPool__MARTE_GCM_DataPool829", None)
        self.__MARTE_GCM_DataPool829 = value
        
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
            if hasattr(old_value, "GCM_MARTE_Property827"):
                opp_val = getattr(old_value, "GCM_MARTE_Property827", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Property827", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Property827"):
                opp_val = getattr(value, "GCM_MARTE_Property827", None)
                setattr(value, "GCM_MARTE_Property827", self)

    @property
    def MARTE_GCM_DataPool831(self):
        return self.__MARTE_GCM_DataPool831

    @MARTE_GCM_DataPool831.setter
    def MARTE_GCM_DataPool831(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_DataPool__MARTE_GCM_DataPool831", None)
        self.__MARTE_GCM_DataPool831 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_Behavior832"):
                opp_val = getattr(old_value, "GCM_MARTE_Behavior832", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Behavior832", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Behavior832"):
                opp_val = getattr(value, "GCM_MARTE_Behavior832", None)
                setattr(value, "GCM_MARTE_Behavior832", self)

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

class GCM_MARTE_Property:

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

class GCM_ClientServerSpecification:

    pass
class GCM_MARTE_Interface:

    pass
class MARTE_GCM_ClientServerPort:

    def __init__(self, specificationKind: str, isConjugated: str, kind: str, MARTE_GCM_ClientServerPort: "GCM_MARTE_Port" = None, MARTE_GCM_ClientServerPort805: set["GCM_MARTE_Interface"] = None, MARTE_GCM_ClientServerPort807: set["GCM_MARTE_Interface"] = None, MARTE_GCM_ClientServerPort810: "GCM_ClientServerSpecification" = None):
        self.specificationKind = specificationKind
        self.isConjugated = isConjugated
        self.kind = kind
        self.MARTE_GCM_ClientServerPort = MARTE_GCM_ClientServerPort
        self.MARTE_GCM_ClientServerPort805 = MARTE_GCM_ClientServerPort805 if MARTE_GCM_ClientServerPort805 is not None else set()
        self.MARTE_GCM_ClientServerPort807 = MARTE_GCM_ClientServerPort807 if MARTE_GCM_ClientServerPort807 is not None else set()
        self.MARTE_GCM_ClientServerPort810 = MARTE_GCM_ClientServerPort810
        
        pass
    @property
    def specificationKind(self):
        return self.__specificationKind

    @specificationKind.setter
    def specificationKind(self, specificationKind: str):
        self.__specificationKind = specificationKind


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def isConjugated(self):
        return self.__isConjugated

    @isConjugated.setter
    def isConjugated(self, isConjugated: str):
        self.__isConjugated = isConjugated


    @property
    def MARTE_GCM_ClientServerPort805(self):
        return self.__MARTE_GCM_ClientServerPort805

    @MARTE_GCM_ClientServerPort805.setter
    def MARTE_GCM_ClientServerPort805(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort805", None)
        self.__MARTE_GCM_ClientServerPort805 = value if value is not None else set()
        
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
    def MARTE_GCM_ClientServerPort807(self):
        return self.__MARTE_GCM_ClientServerPort807

    @MARTE_GCM_ClientServerPort807.setter
    def MARTE_GCM_ClientServerPort807(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort807", None)
        self.__MARTE_GCM_ClientServerPort807 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GCM_MARTE_Interface808"):
                    opp_val = getattr(item, "GCM_MARTE_Interface808", None)
                    
                    if opp_val == self:
                        setattr(item, "GCM_MARTE_Interface808", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GCM_MARTE_Interface808"):
                    opp_val = getattr(item, "GCM_MARTE_Interface808", None)
                    
                    setattr(item, "GCM_MARTE_Interface808", self)
                    

    @property
    def MARTE_GCM_ClientServerPort810(self):
        return self.__MARTE_GCM_ClientServerPort810

    @MARTE_GCM_ClientServerPort810.setter
    def MARTE_GCM_ClientServerPort810(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort810", None)
        self.__MARTE_GCM_ClientServerPort810 = value
        
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
    def MARTE_GCM_ClientServerPort(self):
        return self.__MARTE_GCM_ClientServerPort

    @MARTE_GCM_ClientServerPort.setter
    def MARTE_GCM_ClientServerPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GCM_ClientServerPort__MARTE_GCM_ClientServerPort", None)
        self.__MARTE_GCM_ClientServerPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GCM_MARTE_Port803"):
                opp_val = getattr(old_value, "GCM_MARTE_Port803", None)
                if opp_val == self:
                    setattr(old_value, "GCM_MARTE_Port803", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GCM_MARTE_Port803"):
                opp_val = getattr(value, "GCM_MARTE_Port803", None)
                setattr(value, "GCM_MARTE_Port803", self)

class GCM_MARTE_Port:

    pass
class MARTE_GCM_FlowPort:

    def __init__(self, isAtomic: str, isConjugated: str, direction: str, MARTE_GCM_FlowPort: "GCM_MARTE_Port" = None):
        self.isAtomic = isAtomic
        self.isConjugated = isConjugated
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
    def isConjugated(self):
        return self.__isConjugated

    @isConjugated.setter
    def isConjugated(self, isConjugated: str):
        self.__isConjugated = isConjugated


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

class SwSynchronizationResource:

    pass
class MARTE_SW_Interaction_NotificationResource(SwSynchronizationResource):

    def __init__(self, occurence: str, mechanism: str, MARTE_SW_Interaction_NotificationResource778: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_NotificationResource781: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource784: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource787: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource790: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_NotificationResource: set["SW_Interaction_MARTE_TypedElement"] = None):
        self.occurence = occurence
        self.mechanism = mechanism
        self.MARTE_SW_Interaction_NotificationResource778 = MARTE_SW_Interaction_NotificationResource778 if MARTE_SW_Interaction_NotificationResource778 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource781 = MARTE_SW_Interaction_NotificationResource781 if MARTE_SW_Interaction_NotificationResource781 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource784 = MARTE_SW_Interaction_NotificationResource784 if MARTE_SW_Interaction_NotificationResource784 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource787 = MARTE_SW_Interaction_NotificationResource787 if MARTE_SW_Interaction_NotificationResource787 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource790 = MARTE_SW_Interaction_NotificationResource790 if MARTE_SW_Interaction_NotificationResource790 is not None else set()
        self.MARTE_SW_Interaction_NotificationResource = MARTE_SW_Interaction_NotificationResource if MARTE_SW_Interaction_NotificationResource is not None else set()
        
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
    def MARTE_SW_Interaction_NotificationResource778(self):
        return self.__MARTE_SW_Interaction_NotificationResource778

    @MARTE_SW_Interaction_NotificationResource778.setter
    def MARTE_SW_Interaction_NotificationResource778(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource778", None)
        self.__MARTE_SW_Interaction_NotificationResource778 = value if value is not None else set()
        
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
    def MARTE_SW_Interaction_NotificationResource787(self):
        return self.__MARTE_SW_Interaction_NotificationResource787

    @MARTE_SW_Interaction_NotificationResource787.setter
    def MARTE_SW_Interaction_NotificationResource787(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource787", None)
        self.__MARTE_SW_Interaction_NotificationResource787 = value if value is not None else set()
        
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
    def MARTE_SW_Interaction_NotificationResource790(self):
        return self.__MARTE_SW_Interaction_NotificationResource790

    @MARTE_SW_Interaction_NotificationResource790.setter
    def MARTE_SW_Interaction_NotificationResource790(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource790", None)
        self.__MARTE_SW_Interaction_NotificationResource790 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature791"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature791", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature791", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature791"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature791", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature791", self)
                    

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
                if hasattr(item, "SW_Interaction_MARTE_TypedElement776"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement776", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement776", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement776"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement776", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement776", self)
                    

    @property
    def MARTE_SW_Interaction_NotificationResource784(self):
        return self.__MARTE_SW_Interaction_NotificationResource784

    @MARTE_SW_Interaction_NotificationResource784.setter
    def MARTE_SW_Interaction_NotificationResource784(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource784", None)
        self.__MARTE_SW_Interaction_NotificationResource784 = value if value is not None else set()
        
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
    def MARTE_SW_Interaction_NotificationResource781(self):
        return self.__MARTE_SW_Interaction_NotificationResource781

    @MARTE_SW_Interaction_NotificationResource781.setter
    def MARTE_SW_Interaction_NotificationResource781(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_NotificationResource__MARTE_SW_Interaction_NotificationResource781", None)
        self.__MARTE_SW_Interaction_NotificationResource781 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature782"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature782", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature782", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature782"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature782", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature782", self)
                    

class SW_Interaction_SwSynchronizationResource:

    pass
class SW_Interaction_MARTE_BehavioralFeature:

    pass
class SwCommunicationResource:

    pass
class MARTE_SW_Interaction_MessageComResource(SwCommunicationResource):

    def __init__(self, isFixedMessageSize: str, mechanism: str, messageQueuePolicy: str, MARTE_SW_Interaction_MessageComResource: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_MessageComResource767: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_MessageComResource770: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_MessageComResource773: set["SW_Interaction_MARTE_BehavioralFeature"] = None):
        self.isFixedMessageSize = isFixedMessageSize
        self.mechanism = mechanism
        self.messageQueuePolicy = messageQueuePolicy
        self.MARTE_SW_Interaction_MessageComResource = MARTE_SW_Interaction_MessageComResource if MARTE_SW_Interaction_MessageComResource is not None else set()
        self.MARTE_SW_Interaction_MessageComResource767 = MARTE_SW_Interaction_MessageComResource767 if MARTE_SW_Interaction_MessageComResource767 is not None else set()
        self.MARTE_SW_Interaction_MessageComResource770 = MARTE_SW_Interaction_MessageComResource770 if MARTE_SW_Interaction_MessageComResource770 is not None else set()
        self.MARTE_SW_Interaction_MessageComResource773 = MARTE_SW_Interaction_MessageComResource773 if MARTE_SW_Interaction_MessageComResource773 is not None else set()
        
        pass
    @property
    def messageQueuePolicy(self):
        return self.__messageQueuePolicy

    @messageQueuePolicy.setter
    def messageQueuePolicy(self, messageQueuePolicy: str):
        self.__messageQueuePolicy = messageQueuePolicy


    @property
    def mechanism(self):
        return self.__mechanism

    @mechanism.setter
    def mechanism(self, mechanism: str):
        self.__mechanism = mechanism


    @property
    def isFixedMessageSize(self):
        return self.__isFixedMessageSize

    @isFixedMessageSize.setter
    def isFixedMessageSize(self, isFixedMessageSize: str):
        self.__isFixedMessageSize = isFixedMessageSize


    @property
    def MARTE_SW_Interaction_MessageComResource770(self):
        return self.__MARTE_SW_Interaction_MessageComResource770

    @MARTE_SW_Interaction_MessageComResource770.setter
    def MARTE_SW_Interaction_MessageComResource770(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource770", None)
        self.__MARTE_SW_Interaction_MessageComResource770 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature771"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature771", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature771", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature771"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature771", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature771", self)
                    

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
                if hasattr(item, "SW_Interaction_MARTE_TypedElement765"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement765", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement765", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement765"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement765", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement765", self)
                    

    @property
    def MARTE_SW_Interaction_MessageComResource773(self):
        return self.__MARTE_SW_Interaction_MessageComResource773

    @MARTE_SW_Interaction_MessageComResource773.setter
    def MARTE_SW_Interaction_MessageComResource773(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource773", None)
        self.__MARTE_SW_Interaction_MessageComResource773 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature774"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature774", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_BehavioralFeature774", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_BehavioralFeature774"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_BehavioralFeature774", None)
                    
                    setattr(item, "SW_Interaction_MARTE_BehavioralFeature774", self)
                    

    @property
    def MARTE_SW_Interaction_MessageComResource767(self):
        return self.__MARTE_SW_Interaction_MessageComResource767

    @MARTE_SW_Interaction_MessageComResource767.setter
    def MARTE_SW_Interaction_MessageComResource767(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_MessageComResource__MARTE_SW_Interaction_MessageComResource767", None)
        self.__MARTE_SW_Interaction_MessageComResource767 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement768"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement768", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Interaction_MARTE_TypedElement768", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Interaction_MARTE_TypedElement768"):
                    opp_val = getattr(item, "SW_Interaction_MARTE_TypedElement768", None)
                    
                    setattr(item, "SW_Interaction_MARTE_TypedElement768", self)
                    

class MARTE_SW_Interaction_SharedDataComResource(SwCommunicationResource):

    pass
class GRM_SynchronizationResource:

    pass
class SW_Interaction_SwInteractionResource:

    pass
class MARTE_SW_Interaction_SwSynchronizationResource(SW_Interaction_SwInteractionResource, GRM_SynchronizationResource):

    pass
class MARTE_SW_Interaction_SwCommunicationResource(SW_Interaction_SwInteractionResource, GRM_CommunicationMedia):

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
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement719"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement719", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement719", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement719"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement719", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement719", self)
                    

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
class SwConcurrentResource:

    pass
class MARTE_SW_Concurrency_InterruptResource(SwConcurrentResource):

    def __init__(self, kind: str, isMaskable: str, MARTE_SW_Concurrency_InterruptResource: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_InterruptResource676: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_InterruptResource679: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_InterruptResource682: set["SW_Concurrency_MARTE_BehavioralFeature"] = None):
        self.kind = kind
        self.isMaskable = isMaskable
        self.MARTE_SW_Concurrency_InterruptResource = MARTE_SW_Concurrency_InterruptResource if MARTE_SW_Concurrency_InterruptResource is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource676 = MARTE_SW_Concurrency_InterruptResource676 if MARTE_SW_Concurrency_InterruptResource676 is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource679 = MARTE_SW_Concurrency_InterruptResource679 if MARTE_SW_Concurrency_InterruptResource679 is not None else set()
        self.MARTE_SW_Concurrency_InterruptResource682 = MARTE_SW_Concurrency_InterruptResource682 if MARTE_SW_Concurrency_InterruptResource682 is not None else set()
        
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
    def MARTE_SW_Concurrency_InterruptResource676(self):
        return self.__MARTE_SW_Concurrency_InterruptResource676

    @MARTE_SW_Concurrency_InterruptResource676.setter
    def MARTE_SW_Concurrency_InterruptResource676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource676", None)
        self.__MARTE_SW_Concurrency_InterruptResource676 = value if value is not None else set()
        
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
    def MARTE_SW_Concurrency_InterruptResource682(self):
        return self.__MARTE_SW_Concurrency_InterruptResource682

    @MARTE_SW_Concurrency_InterruptResource682.setter
    def MARTE_SW_Concurrency_InterruptResource682(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource682", None)
        self.__MARTE_SW_Concurrency_InterruptResource682 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature683"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature683", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature683", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature683"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature683", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature683", self)
                    

    @property
    def MARTE_SW_Concurrency_InterruptResource679(self):
        return self.__MARTE_SW_Concurrency_InterruptResource679

    @MARTE_SW_Concurrency_InterruptResource679.setter
    def MARTE_SW_Concurrency_InterruptResource679(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource679", None)
        self.__MARTE_SW_Concurrency_InterruptResource679 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature680"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature680", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature680", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature680"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature680", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature680", self)
                    

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
                    

class SW_Concurrency_MARTE_TypedElement:

    pass
class SW_Concurrency_MARTE_Element:

    pass
class SwResource:

    pass
class MARTE_SW_Brokering_MemoryBroker(SwResource):

    def __init__(self, accessPolicy: str, MARTE_SW_Brokering_MemoryBroker751: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker754: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker757: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_MemoryBroker: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_MemoryBroker742: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_MemoryBroker745: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_MemoryBroker748: set["SW_Brokering_MARTE_BehavioralFeature"] = None):
        self.accessPolicy = accessPolicy
        self.MARTE_SW_Brokering_MemoryBroker751 = MARTE_SW_Brokering_MemoryBroker751 if MARTE_SW_Brokering_MemoryBroker751 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker754 = MARTE_SW_Brokering_MemoryBroker754 if MARTE_SW_Brokering_MemoryBroker754 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker757 = MARTE_SW_Brokering_MemoryBroker757 if MARTE_SW_Brokering_MemoryBroker757 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker = MARTE_SW_Brokering_MemoryBroker if MARTE_SW_Brokering_MemoryBroker is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker742 = MARTE_SW_Brokering_MemoryBroker742 if MARTE_SW_Brokering_MemoryBroker742 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker745 = MARTE_SW_Brokering_MemoryBroker745 if MARTE_SW_Brokering_MemoryBroker745 is not None else set()
        self.MARTE_SW_Brokering_MemoryBroker748 = MARTE_SW_Brokering_MemoryBroker748 if MARTE_SW_Brokering_MemoryBroker748 is not None else set()
        
        pass
    @property
    def accessPolicy(self):
        return self.__accessPolicy

    @accessPolicy.setter
    def accessPolicy(self, accessPolicy: str):
        self.__accessPolicy = accessPolicy


    @property
    def MARTE_SW_Brokering_MemoryBroker751(self):
        return self.__MARTE_SW_Brokering_MemoryBroker751

    @MARTE_SW_Brokering_MemoryBroker751.setter
    def MARTE_SW_Brokering_MemoryBroker751(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker751", None)
        self.__MARTE_SW_Brokering_MemoryBroker751 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature752"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature752", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature752", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature752"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature752", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature752", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker748(self):
        return self.__MARTE_SW_Brokering_MemoryBroker748

    @MARTE_SW_Brokering_MemoryBroker748.setter
    def MARTE_SW_Brokering_MemoryBroker748(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker748", None)
        self.__MARTE_SW_Brokering_MemoryBroker748 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature749"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature749", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature749", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature749"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature749", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature749", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker754(self):
        return self.__MARTE_SW_Brokering_MemoryBroker754

    @MARTE_SW_Brokering_MemoryBroker754.setter
    def MARTE_SW_Brokering_MemoryBroker754(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker754", None)
        self.__MARTE_SW_Brokering_MemoryBroker754 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature755"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature755", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature755", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature755"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature755", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature755", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker742(self):
        return self.__MARTE_SW_Brokering_MemoryBroker742

    @MARTE_SW_Brokering_MemoryBroker742.setter
    def MARTE_SW_Brokering_MemoryBroker742(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker742", None)
        self.__MARTE_SW_Brokering_MemoryBroker742 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement743"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement743", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement743", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement743"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement743", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement743", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker745(self):
        return self.__MARTE_SW_Brokering_MemoryBroker745

    @MARTE_SW_Brokering_MemoryBroker745.setter
    def MARTE_SW_Brokering_MemoryBroker745(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker745", None)
        self.__MARTE_SW_Brokering_MemoryBroker745 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement746"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement746", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement746", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement746"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement746", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement746", self)
                    

    @property
    def MARTE_SW_Brokering_MemoryBroker757(self):
        return self.__MARTE_SW_Brokering_MemoryBroker757

    @MARTE_SW_Brokering_MemoryBroker757.setter
    def MARTE_SW_Brokering_MemoryBroker757(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker757", None)
        self.__MARTE_SW_Brokering_MemoryBroker757 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature758"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature758", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature758", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature758"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature758", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature758", self)
                    

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
                if hasattr(item, "SW_Brokering_MARTE_TypedElement740"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement740", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_TypedElement740", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_TypedElement740"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_TypedElement740", None)
                    
                    setattr(item, "SW_Brokering_MARTE_TypedElement740", self)
                    

class MARTE_SW_Concurrency_MemoryPartition(SwResource):

    pass
class MARTE_SW_Interaction_SwInteractionResource(SwResource):

    def __init__(self, waitingQueueCapacity: str, isIntraMemoryPartitionInteraction: bool, waitingQueuePolicy: str, MARTE_SW_Interaction_SwInteractionResource: set["SW_Interaction_MARTE_TypedElement"] = None):
        self.waitingQueueCapacity = waitingQueueCapacity
        self.isIntraMemoryPartitionInteraction = isIntraMemoryPartitionInteraction
        self.waitingQueuePolicy = waitingQueuePolicy
        self.MARTE_SW_Interaction_SwInteractionResource = MARTE_SW_Interaction_SwInteractionResource if MARTE_SW_Interaction_SwInteractionResource is not None else set()
        
        pass
    @property
    def waitingQueuePolicy(self):
        return self.__waitingQueuePolicy

    @waitingQueuePolicy.setter
    def waitingQueuePolicy(self, waitingQueuePolicy: str):
        self.__waitingQueuePolicy = waitingQueuePolicy


    @property
    def isIntraMemoryPartitionInteraction(self):
        return self.__isIntraMemoryPartitionInteraction

    @isIntraMemoryPartitionInteraction.setter
    def isIntraMemoryPartitionInteraction(self, isIntraMemoryPartitionInteraction: bool):
        self.__isIntraMemoryPartitionInteraction = isIntraMemoryPartitionInteraction


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

    def __init__(self, accessPolicy: str, isBuffered: str, name: str, MARTE_SW_Brokering_DeviceBroker: set["SW_Brokering_MARTE_TypedElement"] = None, MARTE_SW_Brokering_DeviceBroker722: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker724: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker727: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker730: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker733: set["SW_Brokering_MARTE_BehavioralFeature"] = None, MARTE_SW_Brokering_DeviceBroker736: set["SW_Brokering_MARTE_Operation"] = None, MARTE_SW_Brokering_DeviceBroker738: set["SW_Brokering_MARTE_Activity"] = None):
        self.accessPolicy = accessPolicy
        self.isBuffered = isBuffered
        self.name = name
        self.MARTE_SW_Brokering_DeviceBroker = MARTE_SW_Brokering_DeviceBroker if MARTE_SW_Brokering_DeviceBroker is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker722 = MARTE_SW_Brokering_DeviceBroker722 if MARTE_SW_Brokering_DeviceBroker722 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker724 = MARTE_SW_Brokering_DeviceBroker724 if MARTE_SW_Brokering_DeviceBroker724 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker727 = MARTE_SW_Brokering_DeviceBroker727 if MARTE_SW_Brokering_DeviceBroker727 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker730 = MARTE_SW_Brokering_DeviceBroker730 if MARTE_SW_Brokering_DeviceBroker730 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker733 = MARTE_SW_Brokering_DeviceBroker733 if MARTE_SW_Brokering_DeviceBroker733 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker736 = MARTE_SW_Brokering_DeviceBroker736 if MARTE_SW_Brokering_DeviceBroker736 is not None else set()
        self.MARTE_SW_Brokering_DeviceBroker738 = MARTE_SW_Brokering_DeviceBroker738 if MARTE_SW_Brokering_DeviceBroker738 is not None else set()
        
        pass
    @property
    def isBuffered(self):
        return self.__isBuffered

    @isBuffered.setter
    def isBuffered(self, isBuffered: str):
        self.__isBuffered = isBuffered


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def accessPolicy(self):
        return self.__accessPolicy

    @accessPolicy.setter
    def accessPolicy(self, accessPolicy: str):
        self.__accessPolicy = accessPolicy


    @property
    def MARTE_SW_Brokering_DeviceBroker724(self):
        return self.__MARTE_SW_Brokering_DeviceBroker724

    @MARTE_SW_Brokering_DeviceBroker724.setter
    def MARTE_SW_Brokering_DeviceBroker724(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker724", None)
        self.__MARTE_SW_Brokering_DeviceBroker724 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature725"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature725", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature725", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature725"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature725", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature725", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker730(self):
        return self.__MARTE_SW_Brokering_DeviceBroker730

    @MARTE_SW_Brokering_DeviceBroker730.setter
    def MARTE_SW_Brokering_DeviceBroker730(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker730", None)
        self.__MARTE_SW_Brokering_DeviceBroker730 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature731"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature731", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature731", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature731"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature731", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature731", self)
                    

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
    def MARTE_SW_Brokering_DeviceBroker733(self):
        return self.__MARTE_SW_Brokering_DeviceBroker733

    @MARTE_SW_Brokering_DeviceBroker733.setter
    def MARTE_SW_Brokering_DeviceBroker733(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker733", None)
        self.__MARTE_SW_Brokering_DeviceBroker733 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature734"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature734", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature734", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature734"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature734", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature734", self)
                    

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
    def MARTE_SW_Brokering_DeviceBroker727(self):
        return self.__MARTE_SW_Brokering_DeviceBroker727

    @MARTE_SW_Brokering_DeviceBroker727.setter
    def MARTE_SW_Brokering_DeviceBroker727(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker727", None)
        self.__MARTE_SW_Brokering_DeviceBroker727 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature728"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature728", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Brokering_MARTE_BehavioralFeature728", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Brokering_MARTE_BehavioralFeature728"):
                    opp_val = getattr(item, "SW_Brokering_MARTE_BehavioralFeature728", None)
                    
                    setattr(item, "SW_Brokering_MARTE_BehavioralFeature728", self)
                    

    @property
    def MARTE_SW_Brokering_DeviceBroker722(self):
        return self.__MARTE_SW_Brokering_DeviceBroker722

    @MARTE_SW_Brokering_DeviceBroker722.setter
    def MARTE_SW_Brokering_DeviceBroker722(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Brokering_DeviceBroker__MARTE_SW_Brokering_DeviceBroker722", None)
        self.__MARTE_SW_Brokering_DeviceBroker722 = value if value is not None else set()
        
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
                    

class MARTE_SW_Concurrency_SwConcurrentResource(SwResource):

    def __init__(self, activationCapacity: str, MARTE_SW_Concurrency_SwConcurrentResource632: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource635: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource638: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource641: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource644: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource647: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource650: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource653: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource656: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwConcurrentResource659: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource662: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource: "ArrivalPattern" = None, MARTE_SW_Concurrency_SwConcurrentResource628: set["SW_Concurrency_MARTE_Element"] = None, MARTE_SW_Concurrency_SwConcurrentResource630: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource665: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource668: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwConcurrentResource671: set["SW_Concurrency_MARTE_TypedElement"] = None):
        self.activationCapacity = activationCapacity
        self.MARTE_SW_Concurrency_SwConcurrentResource632 = MARTE_SW_Concurrency_SwConcurrentResource632 if MARTE_SW_Concurrency_SwConcurrentResource632 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource635 = MARTE_SW_Concurrency_SwConcurrentResource635 if MARTE_SW_Concurrency_SwConcurrentResource635 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource638 = MARTE_SW_Concurrency_SwConcurrentResource638 if MARTE_SW_Concurrency_SwConcurrentResource638 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource641 = MARTE_SW_Concurrency_SwConcurrentResource641 if MARTE_SW_Concurrency_SwConcurrentResource641 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource644 = MARTE_SW_Concurrency_SwConcurrentResource644 if MARTE_SW_Concurrency_SwConcurrentResource644 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource647 = MARTE_SW_Concurrency_SwConcurrentResource647 if MARTE_SW_Concurrency_SwConcurrentResource647 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource650 = MARTE_SW_Concurrency_SwConcurrentResource650 if MARTE_SW_Concurrency_SwConcurrentResource650 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource653 = MARTE_SW_Concurrency_SwConcurrentResource653 if MARTE_SW_Concurrency_SwConcurrentResource653 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource656 = MARTE_SW_Concurrency_SwConcurrentResource656 if MARTE_SW_Concurrency_SwConcurrentResource656 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource659 = MARTE_SW_Concurrency_SwConcurrentResource659 if MARTE_SW_Concurrency_SwConcurrentResource659 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource662 = MARTE_SW_Concurrency_SwConcurrentResource662 if MARTE_SW_Concurrency_SwConcurrentResource662 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource = MARTE_SW_Concurrency_SwConcurrentResource
        self.MARTE_SW_Concurrency_SwConcurrentResource628 = MARTE_SW_Concurrency_SwConcurrentResource628 if MARTE_SW_Concurrency_SwConcurrentResource628 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource630 = MARTE_SW_Concurrency_SwConcurrentResource630 if MARTE_SW_Concurrency_SwConcurrentResource630 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource665 = MARTE_SW_Concurrency_SwConcurrentResource665 if MARTE_SW_Concurrency_SwConcurrentResource665 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource668 = MARTE_SW_Concurrency_SwConcurrentResource668 if MARTE_SW_Concurrency_SwConcurrentResource668 is not None else set()
        self.MARTE_SW_Concurrency_SwConcurrentResource671 = MARTE_SW_Concurrency_SwConcurrentResource671 if MARTE_SW_Concurrency_SwConcurrentResource671 is not None else set()
        
        pass
    @property
    def activationCapacity(self):
        return self.__activationCapacity

    @activationCapacity.setter
    def activationCapacity(self, activationCapacity: str):
        self.__activationCapacity = activationCapacity


    @property
    def MARTE_SW_Concurrency_SwConcurrentResource653(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource653

    @MARTE_SW_Concurrency_SwConcurrentResource653.setter
    def MARTE_SW_Concurrency_SwConcurrentResource653(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource653", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource653 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature654"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature654", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature654", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature654"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature654", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature654", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource628(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource628

    @MARTE_SW_Concurrency_SwConcurrentResource628.setter
    def MARTE_SW_Concurrency_SwConcurrentResource628(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource628", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource628 = value if value is not None else set()
        
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
    def MARTE_SW_Concurrency_SwConcurrentResource659(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource659

    @MARTE_SW_Concurrency_SwConcurrentResource659.setter
    def MARTE_SW_Concurrency_SwConcurrentResource659(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource659", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource659 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement660"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement660", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement660", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement660"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement660", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement660", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource668(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource668

    @MARTE_SW_Concurrency_SwConcurrentResource668.setter
    def MARTE_SW_Concurrency_SwConcurrentResource668(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource668", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource668 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement669"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement669", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement669", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement669"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement669", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement669", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource662(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource662

    @MARTE_SW_Concurrency_SwConcurrentResource662.setter
    def MARTE_SW_Concurrency_SwConcurrentResource662(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource662", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource662 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement663"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement663", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement663", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement663"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement663", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement663", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource635(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource635

    @MARTE_SW_Concurrency_SwConcurrentResource635.setter
    def MARTE_SW_Concurrency_SwConcurrentResource635(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource635", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource635 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement636"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement636", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement636", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement636"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement636", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement636", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource656(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource656

    @MARTE_SW_Concurrency_SwConcurrentResource656.setter
    def MARTE_SW_Concurrency_SwConcurrentResource656(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource656", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource656 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature657"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature657", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature657", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature657"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature657", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature657", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource665(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource665

    @MARTE_SW_Concurrency_SwConcurrentResource665.setter
    def MARTE_SW_Concurrency_SwConcurrentResource665(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource665", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource665 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement666"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement666", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement666", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement666"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement666", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement666", self)
                    

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
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature645"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature645", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature645", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature645"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature645", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature645", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource671(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource671

    @MARTE_SW_Concurrency_SwConcurrentResource671.setter
    def MARTE_SW_Concurrency_SwConcurrentResource671(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource671", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource671 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement672"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement672", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement672", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement672"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement672", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement672", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource632(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource632

    @MARTE_SW_Concurrency_SwConcurrentResource632.setter
    def MARTE_SW_Concurrency_SwConcurrentResource632(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource632", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource632 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement633"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement633", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement633", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement633"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement633", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement633", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource630(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource630

    @MARTE_SW_Concurrency_SwConcurrentResource630.setter
    def MARTE_SW_Concurrency_SwConcurrentResource630(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource630", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource630 = value if value is not None else set()
        
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
    def MARTE_SW_Concurrency_SwConcurrentResource(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource

    @MARTE_SW_Concurrency_SwConcurrentResource.setter
    def MARTE_SW_Concurrency_SwConcurrentResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrivalPattern626"):
                opp_val = getattr(old_value, "ArrivalPattern626", None)
                if opp_val == self:
                    setattr(old_value, "ArrivalPattern626", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrivalPattern626"):
                opp_val = getattr(value, "ArrivalPattern626", None)
                setattr(value, "ArrivalPattern626", self)

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource641(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource641

    @MARTE_SW_Concurrency_SwConcurrentResource641.setter
    def MARTE_SW_Concurrency_SwConcurrentResource641(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource641", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource641 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature642"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature642", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature642", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature642"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature642", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature642", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource647(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource647

    @MARTE_SW_Concurrency_SwConcurrentResource647.setter
    def MARTE_SW_Concurrency_SwConcurrentResource647(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource647", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource647 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature648"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature648", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature648", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature648"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature648", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature648", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource650(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource650

    @MARTE_SW_Concurrency_SwConcurrentResource650.setter
    def MARTE_SW_Concurrency_SwConcurrentResource650(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource650", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource650 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature651"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature651", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature651", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature651"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature651", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature651", self)
                    

    @property
    def MARTE_SW_Concurrency_SwConcurrentResource638(self):
        return self.__MARTE_SW_Concurrency_SwConcurrentResource638

    @MARTE_SW_Concurrency_SwConcurrentResource638.setter
    def MARTE_SW_Concurrency_SwConcurrentResource638(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwConcurrentResource__MARTE_SW_Concurrency_SwConcurrentResource638", None)
        self.__MARTE_SW_Concurrency_SwConcurrentResource638 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement639"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement639", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement639", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement639"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement639", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement639", self)
                    

class SW_ResourceCore_MARTE_BehavioralFeature:

    pass
class SW_ResourceCore_MARTE_TypedElement:

    pass
class SW_Concurrency_MARTE_BehavioralFeature:

    pass
class SW_Brokering_DeviceBroker:

    pass
class MARTE_HwDiagram_SRMDiagram:

    pass
class SW_ResourceCore_MARTE_Property:

    pass
class HwDiagram_MARTE_DataType:

    pass
class MARTE_HwDiagram_HwCircuitDiagram:

    def __init__(self, name: str, MARTE_HwDiagram_HwCircuitDiagram: set["HwPackage_HwPackage"] = None, MARTE_HwDiagram_HwCircuitDiagram592: set["HwPackage_HwWire"] = None):
        self.name = name
        self.MARTE_HwDiagram_HwCircuitDiagram = MARTE_HwDiagram_HwCircuitDiagram if MARTE_HwDiagram_HwCircuitDiagram is not None else set()
        self.MARTE_HwDiagram_HwCircuitDiagram592 = MARTE_HwDiagram_HwCircuitDiagram592 if MARTE_HwDiagram_HwCircuitDiagram592 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
                if hasattr(item, "HwPackage_HwPackage590"):
                    opp_val = getattr(item, "HwPackage_HwPackage590", None)
                    
                    if opp_val == self:
                        setattr(item, "HwPackage_HwPackage590", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwPackage_HwPackage590"):
                    opp_val = getattr(item, "HwPackage_HwPackage590", None)
                    
                    setattr(item, "HwPackage_HwPackage590", self)
                    

    @property
    def MARTE_HwDiagram_HwCircuitDiagram592(self):
        return self.__MARTE_HwDiagram_HwCircuitDiagram592

    @MARTE_HwDiagram_HwCircuitDiagram592.setter
    def MARTE_HwDiagram_HwCircuitDiagram592(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwCircuitDiagram__MARTE_HwDiagram_HwCircuitDiagram592", None)
        self.__MARTE_HwDiagram_HwCircuitDiagram592 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwPackage_HwWire593"):
                    opp_val = getattr(item, "HwPackage_HwWire593", None)
                    
                    if opp_val == self:
                        setattr(item, "HwPackage_HwWire593", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwPackage_HwWire593"):
                    opp_val = getattr(item, "HwPackage_HwWire593", None)
                    
                    setattr(item, "HwPackage_HwWire593", self)
                    

class HwCommunication_HwConnection:

    pass
class MARTE_HwDiagram_HwHRMDiagram:

    def __init__(self, name: str, MARTE_HwDiagram_HwHRMDiagram: set["HwGeneral_HwResource"] = None, MARTE_HwDiagram_HwHRMDiagram597: set["HwCommunication_HwMedia"] = None, MARTE_HwDiagram_HwHRMDiagram600: set["HwProtocol_HwProtocol"] = None, MARTE_HwDiagram_HwHRMDiagram603: set["HwDiagram_MARTE_DataType"] = None):
        self.name = name
        self.MARTE_HwDiagram_HwHRMDiagram = MARTE_HwDiagram_HwHRMDiagram if MARTE_HwDiagram_HwHRMDiagram is not None else set()
        self.MARTE_HwDiagram_HwHRMDiagram597 = MARTE_HwDiagram_HwHRMDiagram597 if MARTE_HwDiagram_HwHRMDiagram597 is not None else set()
        self.MARTE_HwDiagram_HwHRMDiagram600 = MARTE_HwDiagram_HwHRMDiagram600 if MARTE_HwDiagram_HwHRMDiagram600 is not None else set()
        self.MARTE_HwDiagram_HwHRMDiagram603 = MARTE_HwDiagram_HwHRMDiagram603 if MARTE_HwDiagram_HwHRMDiagram603 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MARTE_HwDiagram_HwHRMDiagram603(self):
        return self.__MARTE_HwDiagram_HwHRMDiagram603

    @MARTE_HwDiagram_HwHRMDiagram603.setter
    def MARTE_HwDiagram_HwHRMDiagram603(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwHRMDiagram__MARTE_HwDiagram_HwHRMDiagram603", None)
        self.__MARTE_HwDiagram_HwHRMDiagram603 = value if value is not None else set()
        
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
    def MARTE_HwDiagram_HwHRMDiagram597(self):
        return self.__MARTE_HwDiagram_HwHRMDiagram597

    @MARTE_HwDiagram_HwHRMDiagram597.setter
    def MARTE_HwDiagram_HwHRMDiagram597(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwHRMDiagram__MARTE_HwDiagram_HwHRMDiagram597", None)
        self.__MARTE_HwDiagram_HwHRMDiagram597 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwCommunication_HwMedia598"):
                    opp_val = getattr(item, "HwCommunication_HwMedia598", None)
                    
                    if opp_val == self:
                        setattr(item, "HwCommunication_HwMedia598", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwCommunication_HwMedia598"):
                    opp_val = getattr(item, "HwCommunication_HwMedia598", None)
                    
                    setattr(item, "HwCommunication_HwMedia598", self)
                    

    @property
    def MARTE_HwDiagram_HwHRMDiagram600(self):
        return self.__MARTE_HwDiagram_HwHRMDiagram600

    @MARTE_HwDiagram_HwHRMDiagram600.setter
    def MARTE_HwDiagram_HwHRMDiagram600(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwHRMDiagram__MARTE_HwDiagram_HwHRMDiagram600", None)
        self.__MARTE_HwDiagram_HwHRMDiagram600 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwProtocol_HwProtocol601"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol601", None)
                    
                    if opp_val == self:
                        setattr(item, "HwProtocol_HwProtocol601", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwProtocol_HwProtocol601"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol601", None)
                    
                    setattr(item, "HwProtocol_HwProtocol601", self)
                    

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
                if hasattr(item, "HwGeneral_HwResource595"):
                    opp_val = getattr(item, "HwGeneral_HwResource595", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResource595", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResource595"):
                    opp_val = getattr(item, "HwGeneral_HwResource595", None)
                    
                    setattr(item, "HwGeneral_HwResource595", self)
                    

class HwPackage_HwWire:

    pass
class MARTE_HwPackage_HwPackagePin(HwEndPoint):

    def __init__(self, altNames: str, pinNo: str, pkgPin: set["HwIO_HwPin"] = None, MARTE_HwPackage_HwPackagePin: set["HwPackage_HwWire"] = None):
        self.altNames = altNames
        self.pinNo = pinNo
        self.pkgPin = pkgPin if pkgPin is not None else set()
        self.MARTE_HwPackage_HwPackagePin = MARTE_HwPackage_HwPackagePin if MARTE_HwPackage_HwPackagePin is not None else set()
        
        pass
    @property
    def pinNo(self):
        return self.__pinNo

    @pinNo.setter
    def pinNo(self, pinNo: str):
        self.__pinNo = pinNo


    @property
    def altNames(self):
        return self.__altNames

    @altNames.setter
    def altNames(self, altNames: str):
        self.__altNames = altNames


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
                    

    @property
    def pkgPin(self):
        return self.__pkgPin

    @pkgPin.setter
    def pkgPin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwPackage_HwPackagePin__pkgPin", None)
        self.__pkgPin = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwPin"):
                    opp_val = getattr(item, "HwPin", None)
                    
                    if opp_val == self:
                        setattr(item, "HwPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwPin"):
                    opp_val = getattr(item, "HwPin", None)
                    
                    setattr(item, "HwPin", self)
                    

class MARTE_HwPackage_HwPackage:

    def __init__(self, pinNum: int, packageType: str, name: str, MARTE_HwPackage_HwPackage: set["HwPackage_HwPackagePin"] = None):
        self.pinNum = pinNum
        self.packageType = packageType
        self.name = name
        self.MARTE_HwPackage_HwPackage = MARTE_HwPackage_HwPackage if MARTE_HwPackage_HwPackage is not None else set()
        
        pass
    @property
    def pinNum(self):
        return self.__pinNum

    @pinNum.setter
    def pinNum(self, pinNum: int):
        self.__pinNum = pinNum


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def packageType(self):
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
                    

class MARTE_HwDatasheet_HwDatasheet:

    def __init__(self, revision: str, name: str, MARTE_HwDatasheet_HwDatasheet: set["HwGeneral_HwResource"] = None, MARTE_HwDatasheet_HwDatasheet576: set["HwProtocol_HwProtocol"] = None):
        self.revision = revision
        self.name = name
        self.MARTE_HwDatasheet_HwDatasheet = MARTE_HwDatasheet_HwDatasheet if MARTE_HwDatasheet_HwDatasheet is not None else set()
        self.MARTE_HwDatasheet_HwDatasheet576 = MARTE_HwDatasheet_HwDatasheet576 if MARTE_HwDatasheet_HwDatasheet576 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def revision(self):
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision


    @property
    def MARTE_HwDatasheet_HwDatasheet576(self):
        return self.__MARTE_HwDatasheet_HwDatasheet576

    @MARTE_HwDatasheet_HwDatasheet576.setter
    def MARTE_HwDatasheet_HwDatasheet576(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDatasheet_HwDatasheet__MARTE_HwDatasheet_HwDatasheet576", None)
        self.__MARTE_HwDatasheet_HwDatasheet576 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwProtocol_HwProtocol577"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol577", None)
                    
                    if opp_val == self:
                        setattr(item, "HwProtocol_HwProtocol577", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwProtocol_HwProtocol577"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol577", None)
                    
                    setattr(item, "HwProtocol_HwProtocol577", self)
                    

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
                if hasattr(item, "HwGeneral_HwResource574"):
                    opp_val = getattr(item, "HwGeneral_HwResource574", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResource574", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResource574"):
                    opp_val = getattr(item, "HwGeneral_HwResource574", None)
                    
                    setattr(item, "HwGeneral_HwResource574", self)
                    

class MARTE_HwRegister_HwRegister(HwMemory):

    def __init__(self, address: str):
        self.address = address
        
        pass
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


class MARTE_HwDiagram_HwBlockDiagram:

    def __init__(self, name: str, MARTE_HwDiagram_HwBlockDiagram: set["HwProtocol_HwProtocol"] = None, MARTE_HwDiagram_HwBlockDiagram585: set["HwCommunication_HwConnection"] = None, MARTE_HwDiagram_HwBlockDiagram587: set["HwGeneral_HwResource"] = None):
        self.name = name
        self.MARTE_HwDiagram_HwBlockDiagram = MARTE_HwDiagram_HwBlockDiagram if MARTE_HwDiagram_HwBlockDiagram is not None else set()
        self.MARTE_HwDiagram_HwBlockDiagram585 = MARTE_HwDiagram_HwBlockDiagram585 if MARTE_HwDiagram_HwBlockDiagram585 is not None else set()
        self.MARTE_HwDiagram_HwBlockDiagram587 = MARTE_HwDiagram_HwBlockDiagram587 if MARTE_HwDiagram_HwBlockDiagram587 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MARTE_HwDiagram_HwBlockDiagram587(self):
        return self.__MARTE_HwDiagram_HwBlockDiagram587

    @MARTE_HwDiagram_HwBlockDiagram587.setter
    def MARTE_HwDiagram_HwBlockDiagram587(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwBlockDiagram__MARTE_HwDiagram_HwBlockDiagram587", None)
        self.__MARTE_HwDiagram_HwBlockDiagram587 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResource588"):
                    opp_val = getattr(item, "HwGeneral_HwResource588", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResource588", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResource588"):
                    opp_val = getattr(item, "HwGeneral_HwResource588", None)
                    
                    setattr(item, "HwGeneral_HwResource588", self)
                    

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
                if hasattr(item, "HwProtocol_HwProtocol583"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol583", None)
                    
                    if opp_val == self:
                        setattr(item, "HwProtocol_HwProtocol583", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwProtocol_HwProtocol583"):
                    opp_val = getattr(item, "HwProtocol_HwProtocol583", None)
                    
                    setattr(item, "HwProtocol_HwProtocol583", self)
                    

    @property
    def MARTE_HwDiagram_HwBlockDiagram585(self):
        return self.__MARTE_HwDiagram_HwBlockDiagram585

    @MARTE_HwDiagram_HwBlockDiagram585.setter
    def MARTE_HwDiagram_HwBlockDiagram585(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwDiagram_HwBlockDiagram__MARTE_HwDiagram_HwBlockDiagram585", None)
        self.__MARTE_HwDiagram_HwBlockDiagram585 = value if value is not None else set()
        
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
        
        pass
    @property
    def name(self):
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
                    

class MARTE_HwPackage_HwWire(HwMedia):

    pass
class MARTE_HwIO_HwPin(HwEndPoint):

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
class MARTE_HwIO_HwLine(HwMedia):

    pass
class HwIO_HwLine:

    pass
class HwPackage_HwPackagePin:

    pass
class HwComponent:

    pass
class MARTE_HwPower_HwPowerSupply(HwComponent):

    pass
class MARTE_HwPower_HwCoolingSupply(HwComponent):

    pass
class MARTE_HwLayout_Env_Condition:

    def __init__(self, type: str, status: str, MARTE_HwLayout_Env_Condition557: "Realnterval" = None, MARTE_HwLayout_Env_Condition: "NFP_String" = None):
        self.type = type
        self.status = status
        self.MARTE_HwLayout_Env_Condition557 = MARTE_HwLayout_Env_Condition557
        self.MARTE_HwLayout_Env_Condition = MARTE_HwLayout_Env_Condition
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


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
            if hasattr(old_value, "NFP_String555"):
                opp_val = getattr(old_value, "NFP_String555", None)
                if opp_val == self:
                    setattr(old_value, "NFP_String555", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_String555"):
                opp_val = getattr(value, "NFP_String555", None)
                setattr(value, "NFP_String555", self)

    @property
    def MARTE_HwLayout_Env_Condition557(self):
        return self.__MARTE_HwLayout_Env_Condition557

    @MARTE_HwLayout_Env_Condition557.setter
    def MARTE_HwLayout_Env_Condition557(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_Env_Condition__MARTE_HwLayout_Env_Condition557", None)
        self.__MARTE_HwLayout_Env_Condition557 = value
        
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

class HwLayout_HwComponent:

    pass
class HwLayout_Env_Condition:

    pass
class NFP_Price:

    pass
class Realnterval:

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
class NFP_NaturalInterval:

    pass
class NFP_Area:

    pass
class HwPeripheral_PeripheralActivity:

    pass
class HwPeripheral_OperationImpl:

    pass
class MARTE_HwDevice_HwPeripheral(HwDevice):

    pass
class NFP_String:

    pass
class HwResource:

    pass
class MARTE_HwCommunication_HwCommunicationResource(HwResource):

    pass
class MARTE_HwLayout_HwComponent(HwResource):

    def __init__(self, kind: str, MARTE_HwLayout_HwComponent527: "NFP_Area" = None, MARTE_HwLayout_HwComponent529: set["NFP_NaturalInterval"] = None, MARTE_HwLayout_HwComponent531: set["NFP_Natural"] = None, MARTE_HwLayout_HwComponent534: "NFP_Natural" = None, MARTE_HwLayout_HwComponent: set["NFP_Length"] = None, MARTE_HwLayout_HwComponent537: "NFP_Real" = None, MARTE_HwLayout_HwComponent540: "NFP_Price" = None, MARTE_HwLayout_HwComponent542: set["HwLayout_Env_Condition"] = None, MARTE_HwLayout_HwComponent544: set["HwGeneral_HwResourceService"] = None, MARTE_HwLayout_HwComponent547: "NFP_Power" = None, MARTE_HwLayout_HwComponent550: "NFP_Power" = None, MARTE_HwLayout_HwComponent553: set["HwLayout_HwComponent"] = None):
        self.kind = kind
        self.MARTE_HwLayout_HwComponent527 = MARTE_HwLayout_HwComponent527
        self.MARTE_HwLayout_HwComponent529 = MARTE_HwLayout_HwComponent529 if MARTE_HwLayout_HwComponent529 is not None else set()
        self.MARTE_HwLayout_HwComponent531 = MARTE_HwLayout_HwComponent531 if MARTE_HwLayout_HwComponent531 is not None else set()
        self.MARTE_HwLayout_HwComponent534 = MARTE_HwLayout_HwComponent534
        self.MARTE_HwLayout_HwComponent = MARTE_HwLayout_HwComponent if MARTE_HwLayout_HwComponent is not None else set()
        self.MARTE_HwLayout_HwComponent537 = MARTE_HwLayout_HwComponent537
        self.MARTE_HwLayout_HwComponent540 = MARTE_HwLayout_HwComponent540
        self.MARTE_HwLayout_HwComponent542 = MARTE_HwLayout_HwComponent542 if MARTE_HwLayout_HwComponent542 is not None else set()
        self.MARTE_HwLayout_HwComponent544 = MARTE_HwLayout_HwComponent544 if MARTE_HwLayout_HwComponent544 is not None else set()
        self.MARTE_HwLayout_HwComponent547 = MARTE_HwLayout_HwComponent547
        self.MARTE_HwLayout_HwComponent550 = MARTE_HwLayout_HwComponent550
        self.MARTE_HwLayout_HwComponent553 = MARTE_HwLayout_HwComponent553 if MARTE_HwLayout_HwComponent553 is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def MARTE_HwLayout_HwComponent534(self):
        return self.__MARTE_HwLayout_HwComponent534

    @MARTE_HwLayout_HwComponent534.setter
    def MARTE_HwLayout_HwComponent534(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent534", None)
        self.__MARTE_HwLayout_HwComponent534 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Natural535"):
                opp_val = getattr(old_value, "NFP_Natural535", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Natural535", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Natural535"):
                opp_val = getattr(value, "NFP_Natural535", None)
                setattr(value, "NFP_Natural535", self)

    @property
    def MARTE_HwLayout_HwComponent531(self):
        return self.__MARTE_HwLayout_HwComponent531

    @MARTE_HwLayout_HwComponent531.setter
    def MARTE_HwLayout_HwComponent531(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent531", None)
        self.__MARTE_HwLayout_HwComponent531 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_Natural532"):
                    opp_val = getattr(item, "NFP_Natural532", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_Natural532", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_Natural532"):
                    opp_val = getattr(item, "NFP_Natural532", None)
                    
                    setattr(item, "NFP_Natural532", self)
                    

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
    def MARTE_HwLayout_HwComponent537(self):
        return self.__MARTE_HwLayout_HwComponent537

    @MARTE_HwLayout_HwComponent537.setter
    def MARTE_HwLayout_HwComponent537(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent537", None)
        self.__MARTE_HwLayout_HwComponent537 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Real538"):
                opp_val = getattr(old_value, "NFP_Real538", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Real538", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Real538"):
                opp_val = getattr(value, "NFP_Real538", None)
                setattr(value, "NFP_Real538", self)

    @property
    def MARTE_HwLayout_HwComponent529(self):
        return self.__MARTE_HwLayout_HwComponent529

    @MARTE_HwLayout_HwComponent529.setter
    def MARTE_HwLayout_HwComponent529(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent529", None)
        self.__MARTE_HwLayout_HwComponent529 = value if value is not None else set()
        
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
            if hasattr(old_value, "NFP_Power548"):
                opp_val = getattr(old_value, "NFP_Power548", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Power548", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Power548"):
                opp_val = getattr(value, "NFP_Power548", None)
                setattr(value, "NFP_Power548", self)

    @property
    def MARTE_HwLayout_HwComponent542(self):
        return self.__MARTE_HwLayout_HwComponent542

    @MARTE_HwLayout_HwComponent542.setter
    def MARTE_HwLayout_HwComponent542(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent542", None)
        self.__MARTE_HwLayout_HwComponent542 = value if value is not None else set()
        
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
    def MARTE_HwLayout_HwComponent527(self):
        return self.__MARTE_HwLayout_HwComponent527

    @MARTE_HwLayout_HwComponent527.setter
    def MARTE_HwLayout_HwComponent527(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent527", None)
        self.__MARTE_HwLayout_HwComponent527 = value
        
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
    def MARTE_HwLayout_HwComponent550(self):
        return self.__MARTE_HwLayout_HwComponent550

    @MARTE_HwLayout_HwComponent550.setter
    def MARTE_HwLayout_HwComponent550(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent550", None)
        self.__MARTE_HwLayout_HwComponent550 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Power551"):
                opp_val = getattr(old_value, "NFP_Power551", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Power551", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Power551"):
                opp_val = getattr(value, "NFP_Power551", None)
                setattr(value, "NFP_Power551", self)

    @property
    def MARTE_HwLayout_HwComponent540(self):
        return self.__MARTE_HwLayout_HwComponent540

    @MARTE_HwLayout_HwComponent540.setter
    def MARTE_HwLayout_HwComponent540(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent540", None)
        self.__MARTE_HwLayout_HwComponent540 = value
        
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

    @property
    def MARTE_HwLayout_HwComponent553(self):
        return self.__MARTE_HwLayout_HwComponent553

    @MARTE_HwLayout_HwComponent553.setter
    def MARTE_HwLayout_HwComponent553(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent553", None)
        self.__MARTE_HwLayout_HwComponent553 = value if value is not None else set()
        
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
    def MARTE_HwLayout_HwComponent544(self):
        return self.__MARTE_HwLayout_HwComponent544

    @MARTE_HwLayout_HwComponent544.setter
    def MARTE_HwLayout_HwComponent544(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwLayout_HwComponent__MARTE_HwLayout_HwComponent544", None)
        self.__MARTE_HwLayout_HwComponent544 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResourceService545"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService545", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResourceService545", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResourceService545"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService545", None)
                    
                    setattr(item, "HwGeneral_HwResourceService545", self)
                    

class MARTE_HwComputing_HwBranchPredictor(HwResource):

    pass
class MARTE_HwComputing_HwISA(HwResource):

    def __init__(self, type: str, MARTE_HwComputing_HwISA: "NFP_String" = None, MARTE_HwComputing_HwISA340: "NFP_DataSize" = None):
        self.type = type
        self.MARTE_HwComputing_HwISA = MARTE_HwComputing_HwISA
        self.MARTE_HwComputing_HwISA340 = MARTE_HwComputing_HwISA340
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def MARTE_HwComputing_HwISA340(self):
        return self.__MARTE_HwComputing_HwISA340

    @MARTE_HwComputing_HwISA340.setter
    def MARTE_HwComputing_HwISA340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwISA__MARTE_HwComputing_HwISA340", None)
        self.__MARTE_HwComputing_HwISA340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_DataSize341"):
                opp_val = getattr(old_value, "NFP_DataSize341", None)
                if opp_val == self:
                    setattr(old_value, "NFP_DataSize341", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_DataSize341"):
                opp_val = getattr(value, "NFP_DataSize341", None)
                setattr(value, "NFP_DataSize341", self)

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

class NFP_FrequencyInterval:

    pass
class HwGeneral_HwResource:

    pass
class MARTE_HwTiming_HwTimingResource(GRM_TimingResource, HwGeneral_HwResource):

    pass
class MARTE_HwMemory_HwMemory(GRM_StorageResource, HwGeneral_HwResource):

    pass
class MARTE_HwDevice_HwDevice(GRM_DeviceResource, HwGeneral_HwResource):

    pass
class MARTE_HwStorageManager_HwStorageManager(GRM_StorageResource, HwGeneral_HwResource):

    pass
class HwStorageManager_HwMMU:

    pass
class HwMemory_HwCache:

    pass
class HwComputing_HwBranchPredictor:

    pass
class HwMemory_HwRAM:

    pass
class HwComputingResource:

    pass
class MARTE_HwComputing_HwMCU(HwComputingResource):

    pass
class MARTE_HwComputing_HwPLD(HwComputingResource):

    def __init__(self, technology: str, MARTE_HwComputing_HwPLD: "HwComputing_PLD_Organization" = None, MARTE_HwComputing_HwPLD344: "NFP_Natural" = None, MARTE_HwComputing_HwPLD347: "NFP_Natural" = None, MARTE_HwComputing_HwPLD350: "NFP_Natural" = None, MARTE_HwComputing_HwPLD353: set["HwMemory_HwRAM"] = None, MARTE_HwComputing_HwPLD355: set["HwComputing_HwComputingResource"] = None):
        self.technology = technology
        self.MARTE_HwComputing_HwPLD = MARTE_HwComputing_HwPLD
        self.MARTE_HwComputing_HwPLD344 = MARTE_HwComputing_HwPLD344
        self.MARTE_HwComputing_HwPLD347 = MARTE_HwComputing_HwPLD347
        self.MARTE_HwComputing_HwPLD350 = MARTE_HwComputing_HwPLD350
        self.MARTE_HwComputing_HwPLD353 = MARTE_HwComputing_HwPLD353 if MARTE_HwComputing_HwPLD353 is not None else set()
        self.MARTE_HwComputing_HwPLD355 = MARTE_HwComputing_HwPLD355 if MARTE_HwComputing_HwPLD355 is not None else set()
        
        pass
    @property
    def technology(self):
        return self.__technology

    @technology.setter
    def technology(self, technology: str):
        self.__technology = technology


    @property
    def MARTE_HwComputing_HwPLD353(self):
        return self.__MARTE_HwComputing_HwPLD353

    @MARTE_HwComputing_HwPLD353.setter
    def MARTE_HwComputing_HwPLD353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD353", None)
        self.__MARTE_HwComputing_HwPLD353 = value if value is not None else set()
        
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
    def MARTE_HwComputing_HwPLD347(self):
        return self.__MARTE_HwComputing_HwPLD347

    @MARTE_HwComputing_HwPLD347.setter
    def MARTE_HwComputing_HwPLD347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD347", None)
        self.__MARTE_HwComputing_HwPLD347 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Natural348"):
                opp_val = getattr(old_value, "NFP_Natural348", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Natural348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Natural348"):
                opp_val = getattr(value, "NFP_Natural348", None)
                setattr(value, "NFP_Natural348", self)

    @property
    def MARTE_HwComputing_HwPLD344(self):
        return self.__MARTE_HwComputing_HwPLD344

    @MARTE_HwComputing_HwPLD344.setter
    def MARTE_HwComputing_HwPLD344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD344", None)
        self.__MARTE_HwComputing_HwPLD344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Natural345"):
                opp_val = getattr(old_value, "NFP_Natural345", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Natural345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Natural345"):
                opp_val = getattr(value, "NFP_Natural345", None)
                setattr(value, "NFP_Natural345", self)

    @property
    def MARTE_HwComputing_HwPLD350(self):
        return self.__MARTE_HwComputing_HwPLD350

    @MARTE_HwComputing_HwPLD350.setter
    def MARTE_HwComputing_HwPLD350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD350", None)
        self.__MARTE_HwComputing_HwPLD350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Natural351"):
                opp_val = getattr(old_value, "NFP_Natural351", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Natural351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Natural351"):
                opp_val = getattr(value, "NFP_Natural351", None)
                setattr(value, "NFP_Natural351", self)

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
    def MARTE_HwComputing_HwPLD355(self):
        return self.__MARTE_HwComputing_HwPLD355

    @MARTE_HwComputing_HwPLD355.setter
    def MARTE_HwComputing_HwPLD355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_HwPLD__MARTE_HwComputing_HwPLD355", None)
        self.__MARTE_HwComputing_HwPLD355 = value if value is not None else set()
        
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
class MARTE_HwComputing_HwProcessor(HwComputingResource):

    pass
class NFP_Natural:

    pass
class MARTE_HwComputing_PLD_Organization:

    def __init__(self, class_: str, MARTE_HwComputing_PLD_Organization: "NFP_Integer" = None, MARTE_HwComputing_PLD_Organization305: "NFP_Natural" = None):
        self.class_ = class_
        self.MARTE_HwComputing_PLD_Organization = MARTE_HwComputing_PLD_Organization
        self.MARTE_HwComputing_PLD_Organization305 = MARTE_HwComputing_PLD_Organization305
        
        pass
    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_: str):
        self.__class_ = class_


    @property
    def MARTE_HwComputing_PLD_Organization305(self):
        return self.__MARTE_HwComputing_PLD_Organization305

    @MARTE_HwComputing_PLD_Organization305.setter
    def MARTE_HwComputing_PLD_Organization305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwComputing_PLD_Organization__MARTE_HwComputing_PLD_Organization305", None)
        self.__MARTE_HwComputing_PLD_Organization305 = value
        
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
            if hasattr(old_value, "NFP_Integer303"):
                opp_val = getattr(old_value, "NFP_Integer303", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Integer303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Integer303"):
                opp_val = getattr(value, "NFP_Integer303", None)
                setattr(value, "NFP_Integer303", self)

class HwComputing_HwISA:

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
    def isAtomic(self):
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic


    @property
    def synchKind(self):
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
            if hasattr(old_value, "HLAM_MARTE_BehavioralFeature301"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioralFeature301", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioralFeature301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioralFeature301"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioralFeature301", None)
                setattr(value, "HLAM_MARTE_BehavioralFeature301", self)

class MARTE_HLAM_RtAction:

    def __init__(self, isAtomic: str, synchKind: str, MARTE_HLAM_RtAction: "NFP_DataSize" = None, MARTE_HLAM_RtAction295: "HLAM_MARTE_BehavioralFeature" = None, MARTE_HLAM_RtAction298: "HLAM_MARTE_InvocationAction" = None):
        self.isAtomic = isAtomic
        self.synchKind = synchKind
        self.MARTE_HLAM_RtAction = MARTE_HLAM_RtAction
        self.MARTE_HLAM_RtAction295 = MARTE_HLAM_RtAction295
        self.MARTE_HLAM_RtAction298 = MARTE_HLAM_RtAction298
        
        pass
    @property
    def isAtomic(self):
        return self.__isAtomic

    @isAtomic.setter
    def isAtomic(self, isAtomic: str):
        self.__isAtomic = isAtomic


    @property
    def synchKind(self):
        return self.__synchKind

    @synchKind.setter
    def synchKind(self, synchKind: str):
        self.__synchKind = synchKind


    @property
    def MARTE_HLAM_RtAction295(self):
        return self.__MARTE_HLAM_RtAction295

    @MARTE_HLAM_RtAction295.setter
    def MARTE_HLAM_RtAction295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtAction__MARTE_HLAM_RtAction295", None)
        self.__MARTE_HLAM_RtAction295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_BehavioralFeature296"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioralFeature296", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioralFeature296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioralFeature296"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioralFeature296", None)
                setattr(value, "HLAM_MARTE_BehavioralFeature296", self)

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
            if hasattr(old_value, "NFP_DataSize293"):
                opp_val = getattr(old_value, "NFP_DataSize293", None)
                if opp_val == self:
                    setattr(old_value, "NFP_DataSize293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_DataSize293"):
                opp_val = getattr(value, "NFP_DataSize293", None)
                setattr(value, "NFP_DataSize293", self)

    @property
    def MARTE_HLAM_RtAction298(self):
        return self.__MARTE_HLAM_RtAction298

    @MARTE_HLAM_RtAction298.setter
    def MARTE_HLAM_RtAction298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtAction__MARTE_HLAM_RtAction298", None)
        self.__MARTE_HLAM_RtAction298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_InvocationAction299"):
                opp_val = getattr(old_value, "HLAM_MARTE_InvocationAction299", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_InvocationAction299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_InvocationAction299"):
                opp_val = getattr(value, "HLAM_MARTE_InvocationAction299", None)
                setattr(value, "HLAM_MARTE_InvocationAction299", self)

class NFP_DateTime:

    pass
class HLAM_MARTE_Comment:

    pass
class NFP_Percentage:

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
class MARTE_HLAM_PpUnit:

    def __init__(self, concPolicy: str, MARTE_HLAM_PpUnit: "NFP_DataSize" = None, MARTE_HLAM_PpUnit256: "HLAM_MARTE_BehavioredClassifier" = None):
        self.concPolicy = concPolicy
        self.MARTE_HLAM_PpUnit = MARTE_HLAM_PpUnit
        self.MARTE_HLAM_PpUnit256 = MARTE_HLAM_PpUnit256
        
        pass
    @property
    def concPolicy(self):
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
            if hasattr(old_value, "NFP_DataSize254"):
                opp_val = getattr(old_value, "NFP_DataSize254", None)
                if opp_val == self:
                    setattr(old_value, "NFP_DataSize254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_DataSize254"):
                opp_val = getattr(value, "NFP_DataSize254", None)
                setattr(value, "NFP_DataSize254", self)

    @property
    def MARTE_HLAM_PpUnit256(self):
        return self.__MARTE_HLAM_PpUnit256

    @MARTE_HLAM_PpUnit256.setter
    def MARTE_HLAM_PpUnit256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_PpUnit__MARTE_HLAM_PpUnit256", None)
        self.__MARTE_HLAM_PpUnit256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLAM_MARTE_BehavioredClassifier257"):
                opp_val = getattr(old_value, "HLAM_MARTE_BehavioredClassifier257", None)
                if opp_val == self:
                    setattr(old_value, "HLAM_MARTE_BehavioredClassifier257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLAM_MARTE_BehavioredClassifier257"):
                opp_val = getattr(value, "HLAM_MARTE_BehavioredClassifier257", None)
                setattr(value, "HLAM_MARTE_BehavioredClassifier257", self)

class Time_TimedInstantObservation:

    pass
class ArrivalPattern:

    pass
class UtilityType:

    pass
class MARTE_HLAM_RtSpecification:

    pass
class HLAM_MARTE_Operation:

    pass
class HLAM_MARTE_Behavior:

    pass
class MARTE_HLAM_RtUnit:

    def __init__(self, queueSchedPolicy: str, queueSize: str, isDynamic: str, isMain: str, srPoolSize: str, srPoolPolicy: str, MARTE_HLAM_RtUnit244: "HLAM_MARTE_Operation" = None, MARTE_HLAM_RtUnit246: "NFP_DataSize" = None, MARTE_HLAM_RtUnit251: "NFP_DataSize" = None, MARTE_HLAM_RtUnit249: "HLAM_MARTE_BehavioredClassifier" = None, MARTE_HLAM_RtUnit: "NFP_Duration" = None, MARTE_HLAM_RtUnit242: "HLAM_MARTE_Behavior" = None):
        self.queueSchedPolicy = queueSchedPolicy
        self.queueSize = queueSize
        self.isDynamic = isDynamic
        self.isMain = isMain
        self.srPoolSize = srPoolSize
        self.srPoolPolicy = srPoolPolicy
        self.MARTE_HLAM_RtUnit244 = MARTE_HLAM_RtUnit244
        self.MARTE_HLAM_RtUnit246 = MARTE_HLAM_RtUnit246
        self.MARTE_HLAM_RtUnit251 = MARTE_HLAM_RtUnit251
        self.MARTE_HLAM_RtUnit249 = MARTE_HLAM_RtUnit249
        self.MARTE_HLAM_RtUnit = MARTE_HLAM_RtUnit
        self.MARTE_HLAM_RtUnit242 = MARTE_HLAM_RtUnit242
        
        pass
    @property
    def queueSchedPolicy(self):
        return self.__queueSchedPolicy

    @queueSchedPolicy.setter
    def queueSchedPolicy(self, queueSchedPolicy: str):
        self.__queueSchedPolicy = queueSchedPolicy


    @property
    def queueSize(self):
        return self.__queueSize

    @queueSize.setter
    def queueSize(self, queueSize: str):
        self.__queueSize = queueSize


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
    def isMain(self):
        return self.__isMain

    @isMain.setter
    def isMain(self, isMain: str):
        self.__isMain = isMain


    @property
    def isDynamic(self):
        return self.__isDynamic

    @isDynamic.setter
    def isDynamic(self, isDynamic: str):
        self.__isDynamic = isDynamic


    @property
    def MARTE_HLAM_RtUnit251(self):
        return self.__MARTE_HLAM_RtUnit251

    @MARTE_HLAM_RtUnit251.setter
    def MARTE_HLAM_RtUnit251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit251", None)
        self.__MARTE_HLAM_RtUnit251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_DataSize252"):
                opp_val = getattr(old_value, "NFP_DataSize252", None)
                if opp_val == self:
                    setattr(old_value, "NFP_DataSize252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_DataSize252"):
                opp_val = getattr(value, "NFP_DataSize252", None)
                setattr(value, "NFP_DataSize252", self)

    @property
    def MARTE_HLAM_RtUnit249(self):
        return self.__MARTE_HLAM_RtUnit249

    @MARTE_HLAM_RtUnit249.setter
    def MARTE_HLAM_RtUnit249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit249", None)
        self.__MARTE_HLAM_RtUnit249 = value
        
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
    def MARTE_HLAM_RtUnit(self):
        return self.__MARTE_HLAM_RtUnit

    @MARTE_HLAM_RtUnit.setter
    def MARTE_HLAM_RtUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit", None)
        self.__MARTE_HLAM_RtUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Duration240"):
                opp_val = getattr(old_value, "NFP_Duration240", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Duration240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Duration240"):
                opp_val = getattr(value, "NFP_Duration240", None)
                setattr(value, "NFP_Duration240", self)

    @property
    def MARTE_HLAM_RtUnit246(self):
        return self.__MARTE_HLAM_RtUnit246

    @MARTE_HLAM_RtUnit246.setter
    def MARTE_HLAM_RtUnit246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit246", None)
        self.__MARTE_HLAM_RtUnit246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_DataSize247"):
                opp_val = getattr(old_value, "NFP_DataSize247", None)
                if opp_val == self:
                    setattr(old_value, "NFP_DataSize247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_DataSize247"):
                opp_val = getattr(value, "NFP_DataSize247", None)
                setattr(value, "NFP_DataSize247", self)

    @property
    def MARTE_HLAM_RtUnit244(self):
        return self.__MARTE_HLAM_RtUnit244

    @MARTE_HLAM_RtUnit244.setter
    def MARTE_HLAM_RtUnit244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit244", None)
        self.__MARTE_HLAM_RtUnit244 = value
        
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
    def MARTE_HLAM_RtUnit242(self):
        return self.__MARTE_HLAM_RtUnit242

    @MARTE_HLAM_RtUnit242.setter
    def MARTE_HLAM_RtUnit242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HLAM_RtUnit__MARTE_HLAM_RtUnit242", None)
        self.__MARTE_HLAM_RtUnit242 = value
        
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
class MARTE_DataTypes_ChoiceType:

    pass
class HLAM_MARTE_BehavioredClassifier:

    pass
class DataTypes_MARTE_Property:

    pass
class MARTE_DataTypes_BoundedSubtype:

    def __init__(self, minValue: str, maxValue: str, isMinOpen: bool, isMaxOpen: bool, MARTE_DataTypes_BoundedSubtype215: "DataTypes_MARTE_DataType" = None, MARTE_DataTypes_BoundedSubtype: "DataTypes_MARTE_Property" = None):
        self.minValue = minValue
        self.maxValue = maxValue
        self.isMinOpen = isMinOpen
        self.isMaxOpen = isMaxOpen
        self.MARTE_DataTypes_BoundedSubtype215 = MARTE_DataTypes_BoundedSubtype215
        self.MARTE_DataTypes_BoundedSubtype = MARTE_DataTypes_BoundedSubtype
        
        pass
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
    def isMinOpen(self):
        return self.__isMinOpen

    @isMinOpen.setter
    def isMinOpen(self, isMinOpen: bool):
        self.__isMinOpen = isMinOpen


    @property
    def MARTE_DataTypes_BoundedSubtype215(self):
        return self.__MARTE_DataTypes_BoundedSubtype215

    @MARTE_DataTypes_BoundedSubtype215.setter
    def MARTE_DataTypes_BoundedSubtype215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_DataTypes_BoundedSubtype__MARTE_DataTypes_BoundedSubtype215", None)
        self.__MARTE_DataTypes_BoundedSubtype215 = value
        
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

    pass
class RSM_MARTE_ConnectorEnd:

    pass
class MARTE_DataTypes_CollectionType:

    pass
class MARTE_DataTypes_IntervalType:

    pass
class DataTypes_MARTE_DataType:

    pass
class TilerSpecification:

    pass
class ShapeSpecification:

    pass
class Allocate:

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
        
        pass
    @property
    def isModulo(self):
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
class MARTE_RSM_DefaultLink(LinkTopology):

    pass
class RSM_MARTE_Connector:

    pass
class MARTE_RSM_LinkTopology(ABC):

    pass
class IntegerMatrix:

    pass
class MARTE_RSM_Tiler(LinkTopology):

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


class MARTE_HwGeneral_HwResourceService(GrService):

    pass
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
class GRM_ResourceUsage:

    pass
class MARTE_GQAM_GaScenario(GRM_ResourceUsage, Time_TimedProcessing):

    pass
class GRM_MARTE_NamedElement:

    pass
class NFP_DataTxRate:

    pass
class NFP_Duration:

    pass
class GRM_MARTE_Connector:

    pass
class Scheduler:

    pass
class MARTE_GRM_SecondaryScheduler(Scheduler):

    pass
class GRM_SecondaryScheduler:

    pass
class SchedParameters:

    pass
class TimingResource:

    pass
class MARTE_GRM_TimerResource(TimingResource):

    def __init__(self, isPeriodic: str, MARTE_GRM_TimerResource: "NFP_Duration" = None):
        self.isPeriodic = isPeriodic
        self.MARTE_GRM_TimerResource = MARTE_GRM_TimerResource
        
        pass
    @property
    def isPeriodic(self):
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
            if hasattr(old_value, "NFP_Duration146"):
                opp_val = getattr(old_value, "NFP_Duration146", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Duration146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Duration146"):
                opp_val = getattr(value, "NFP_Duration146", None)
                setattr(value, "NFP_Duration146", self)

class MARTE_GRM_ClockResource(TimingResource):

    pass
class GRM_Scheduler:

    pass
class MARTE_GQAM_GaCommHost(GRM_CommunicationMedia, GRM_Scheduler):

    pass
class NFP_Real:

    pass
class GRM_SchedulableResource:

    pass
class MARTE_SW_Concurrency_SwSchedulableResource(SW_Concurrency_SwConcurrentResource, GRM_SchedulableResource):

    def __init__(self, isStaticSchedulingFeature: str, isPreemptable: str, MARTE_SW_Concurrency_SwSchedulableResource: "SW_Concurrency_MARTE_NamedElement" = None, MARTE_SW_Concurrency_SwSchedulableResource686: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwSchedulableResource689: set["SW_Concurrency_MARTE_TypedElement"] = None, MARTE_SW_Concurrency_SwSchedulableResource701: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwSchedulableResource695: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwSchedulableResource698: set["SW_Concurrency_MARTE_BehavioralFeature"] = None, MARTE_SW_Concurrency_SwSchedulableResource692: set["SW_Concurrency_MARTE_TypedElement"] = None, GRM_SchedulableResource: "MARTE_GQAM_GaStep" = None, SchedulableResource: "MARTE_GRM_Scheduler" = None, GRM_SchedulableResource1107: "MARTE_PAM_PaRunTInstance" = None, SchedulableResource133: "MARTE_GRM_SecondaryScheduler" = None):
        self.isStaticSchedulingFeature = isStaticSchedulingFeature
        self.isPreemptable = isPreemptable
        self.MARTE_SW_Concurrency_SwSchedulableResource = MARTE_SW_Concurrency_SwSchedulableResource
        self.MARTE_SW_Concurrency_SwSchedulableResource686 = MARTE_SW_Concurrency_SwSchedulableResource686 if MARTE_SW_Concurrency_SwSchedulableResource686 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource689 = MARTE_SW_Concurrency_SwSchedulableResource689 if MARTE_SW_Concurrency_SwSchedulableResource689 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource701 = MARTE_SW_Concurrency_SwSchedulableResource701 if MARTE_SW_Concurrency_SwSchedulableResource701 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource695 = MARTE_SW_Concurrency_SwSchedulableResource695 if MARTE_SW_Concurrency_SwSchedulableResource695 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource698 = MARTE_SW_Concurrency_SwSchedulableResource698 if MARTE_SW_Concurrency_SwSchedulableResource698 is not None else set()
        self.MARTE_SW_Concurrency_SwSchedulableResource692 = MARTE_SW_Concurrency_SwSchedulableResource692 if MARTE_SW_Concurrency_SwSchedulableResource692 is not None else set()
        
        pass
    @property
    def isPreemptable(self):
        return self.__isPreemptable

    @isPreemptable.setter
    def isPreemptable(self, isPreemptable: str):
        self.__isPreemptable = isPreemptable


    @property
    def isStaticSchedulingFeature(self):
        return self.__isStaticSchedulingFeature

    @isStaticSchedulingFeature.setter
    def isStaticSchedulingFeature(self, isStaticSchedulingFeature: str):
        self.__isStaticSchedulingFeature = isStaticSchedulingFeature


    @property
    def MARTE_SW_Concurrency_SwSchedulableResource701(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource701

    @MARTE_SW_Concurrency_SwSchedulableResource701.setter
    def MARTE_SW_Concurrency_SwSchedulableResource701(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource701", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource701 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature702"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature702", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature702", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature702"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature702", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature702", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource698(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource698

    @MARTE_SW_Concurrency_SwSchedulableResource698.setter
    def MARTE_SW_Concurrency_SwSchedulableResource698(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource698", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource698 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature699"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature699", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature699", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature699"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature699", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature699", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource695(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource695

    @MARTE_SW_Concurrency_SwSchedulableResource695.setter
    def MARTE_SW_Concurrency_SwSchedulableResource695(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource695", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource695 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature696"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature696", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_BehavioralFeature696", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_BehavioralFeature696"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_BehavioralFeature696", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_BehavioralFeature696", self)
                    

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
    def MARTE_SW_Concurrency_SwSchedulableResource689(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource689

    @MARTE_SW_Concurrency_SwSchedulableResource689.setter
    def MARTE_SW_Concurrency_SwSchedulableResource689(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource689", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource689 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement690"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement690", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement690", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement690"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement690", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement690", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource692(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource692

    @MARTE_SW_Concurrency_SwSchedulableResource692.setter
    def MARTE_SW_Concurrency_SwSchedulableResource692(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource692", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource692 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement693"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement693", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement693", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement693"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement693", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement693", self)
                    

    @property
    def MARTE_SW_Concurrency_SwSchedulableResource686(self):
        return self.__MARTE_SW_Concurrency_SwSchedulableResource686

    @MARTE_SW_Concurrency_SwSchedulableResource686.setter
    def MARTE_SW_Concurrency_SwSchedulableResource686(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Concurrency_SwSchedulableResource__MARTE_SW_Concurrency_SwSchedulableResource686", None)
        self.__MARTE_SW_Concurrency_SwSchedulableResource686 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement687"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement687", None)
                    
                    if opp_val == self:
                        setattr(item, "SW_Concurrency_MARTE_TypedElement687", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SW_Concurrency_MARTE_TypedElement687"):
                    opp_val = getattr(item, "SW_Concurrency_MARTE_TypedElement687", None)
                    
                    setattr(item, "SW_Concurrency_MARTE_TypedElement687", self)
                    

class GRM_MutualExclusionResource:

    pass
class MARTE_SW_Interaction_SwMutualExclusionResource(GRM_MutualExclusionResource, SW_Interaction_SwSynchronizationResource):

    def __init__(self, mechanism: str, concurrentAccessProtocol: str, MARTE_SW_Interaction_SwMutualExclusionResource: set["SW_Interaction_MARTE_TypedElement"] = None, MARTE_SW_Interaction_SwMutualExclusionResource795: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MARTE_SW_Interaction_SwMutualExclusionResource798: set["SW_Interaction_MARTE_BehavioralFeature"] = None, MutualExclusionResource: "MARTE_GRM_Scheduler" = None):
        self.mechanism = mechanism
        self.concurrentAccessProtocol = concurrentAccessProtocol
        self.MARTE_SW_Interaction_SwMutualExclusionResource = MARTE_SW_Interaction_SwMutualExclusionResource if MARTE_SW_Interaction_SwMutualExclusionResource is not None else set()
        self.MARTE_SW_Interaction_SwMutualExclusionResource795 = MARTE_SW_Interaction_SwMutualExclusionResource795 if MARTE_SW_Interaction_SwMutualExclusionResource795 is not None else set()
        self.MARTE_SW_Interaction_SwMutualExclusionResource798 = MARTE_SW_Interaction_SwMutualExclusionResource798 if MARTE_SW_Interaction_SwMutualExclusionResource798 is not None else set()
        
        pass
    @property
    def mechanism(self):
        return self.__mechanism

    @mechanism.setter
    def mechanism(self, mechanism: str):
        self.__mechanism = mechanism


    @property
    def concurrentAccessProtocol(self):
        return self.__concurrentAccessProtocol

    @concurrentAccessProtocol.setter
    def concurrentAccessProtocol(self, concurrentAccessProtocol: str):
        self.__concurrentAccessProtocol = concurrentAccessProtocol


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
    def MARTE_SW_Interaction_SwMutualExclusionResource795(self):
        return self.__MARTE_SW_Interaction_SwMutualExclusionResource795

    @MARTE_SW_Interaction_SwMutualExclusionResource795.setter
    def MARTE_SW_Interaction_SwMutualExclusionResource795(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_SwMutualExclusionResource__MARTE_SW_Interaction_SwMutualExclusionResource795", None)
        self.__MARTE_SW_Interaction_SwMutualExclusionResource795 = value if value is not None else set()
        
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
    def MARTE_SW_Interaction_SwMutualExclusionResource798(self):
        return self.__MARTE_SW_Interaction_SwMutualExclusionResource798

    @MARTE_SW_Interaction_SwMutualExclusionResource798.setter
    def MARTE_SW_Interaction_SwMutualExclusionResource798(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_SW_Interaction_SwMutualExclusionResource__MARTE_SW_Interaction_SwMutualExclusionResource798", None)
        self.__MARTE_SW_Interaction_SwMutualExclusionResource798 = value if value is not None else set()
        
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
                    

class GRM_ComputingResource:

    pass
class MARTE_HwComputing_HwComputingResource(GRM_ComputingResource, HwGeneral_HwResource):

    pass
class MARTE_GQAM_GaExecHost(GRM_ComputingResource, GRM_Scheduler):

    pass
class GRM_ProcessingResource:

    pass
class GRM_MARTE_OpaqueExpression:

    pass
class ProcessingResource:

    pass
class MARTE_GRM_CommunicationMedia(ProcessingResource):

    def __init__(self, transmMode: str, MARTE_GRM_CommunicationMedia: "NFP_Integer" = None, MARTE_GRM_CommunicationMedia137: "GRM_MARTE_Connector" = None, MARTE_GRM_CommunicationMedia139: set["NFP_Duration"] = None, MARTE_GRM_CommunicationMedia141: set["NFP_Duration"] = None, MARTE_GRM_CommunicationMedia144: set["NFP_DataTxRate"] = None):
        self.transmMode = transmMode
        self.MARTE_GRM_CommunicationMedia = MARTE_GRM_CommunicationMedia
        self.MARTE_GRM_CommunicationMedia137 = MARTE_GRM_CommunicationMedia137
        self.MARTE_GRM_CommunicationMedia139 = MARTE_GRM_CommunicationMedia139 if MARTE_GRM_CommunicationMedia139 is not None else set()
        self.MARTE_GRM_CommunicationMedia141 = MARTE_GRM_CommunicationMedia141 if MARTE_GRM_CommunicationMedia141 is not None else set()
        self.MARTE_GRM_CommunicationMedia144 = MARTE_GRM_CommunicationMedia144 if MARTE_GRM_CommunicationMedia144 is not None else set()
        
        pass
    @property
    def transmMode(self):
        return self.__transmMode

    @transmMode.setter
    def transmMode(self, transmMode: str):
        self.__transmMode = transmMode


    @property
    def MARTE_GRM_CommunicationMedia137(self):
        return self.__MARTE_GRM_CommunicationMedia137

    @MARTE_GRM_CommunicationMedia137.setter
    def MARTE_GRM_CommunicationMedia137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_CommunicationMedia__MARTE_GRM_CommunicationMedia137", None)
        self.__MARTE_GRM_CommunicationMedia137 = value
        
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
    def MARTE_GRM_CommunicationMedia144(self):
        return self.__MARTE_GRM_CommunicationMedia144

    @MARTE_GRM_CommunicationMedia144.setter
    def MARTE_GRM_CommunicationMedia144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_CommunicationMedia__MARTE_GRM_CommunicationMedia144", None)
        self.__MARTE_GRM_CommunicationMedia144 = value if value is not None else set()
        
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
            if hasattr(old_value, "NFP_Integer135"):
                opp_val = getattr(old_value, "NFP_Integer135", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Integer135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Integer135"):
                opp_val = getattr(value, "NFP_Integer135", None)
                setattr(value, "NFP_Integer135", self)

    @property
    def MARTE_GRM_CommunicationMedia139(self):
        return self.__MARTE_GRM_CommunicationMedia139

    @MARTE_GRM_CommunicationMedia139.setter
    def MARTE_GRM_CommunicationMedia139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_CommunicationMedia__MARTE_GRM_CommunicationMedia139", None)
        self.__MARTE_GRM_CommunicationMedia139 = value if value is not None else set()
        
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
    def MARTE_GRM_CommunicationMedia141(self):
        return self.__MARTE_GRM_CommunicationMedia141

    @MARTE_GRM_CommunicationMedia141.setter
    def MARTE_GRM_CommunicationMedia141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_CommunicationMedia__MARTE_GRM_CommunicationMedia141", None)
        self.__MARTE_GRM_CommunicationMedia141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NFP_Duration142"):
                    opp_val = getattr(item, "NFP_Duration142", None)
                    
                    if opp_val == self:
                        setattr(item, "NFP_Duration142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NFP_Duration142"):
                    opp_val = getattr(item, "NFP_Duration142", None)
                    
                    setattr(item, "NFP_Duration142", self)
                    

class MARTE_GRM_DeviceResource(ProcessingResource):

    pass
class MARTE_GRM_ComputingResource(ProcessingResource):

    pass
class GRM_MARTE_InstanceSpecification:

    pass
class GRM_MARTE_Property:

    pass
class NFP_Integer:

    pass
class MARTE_GRM_Resource:

    def __init__(self, isProtected: str, MARTE_GRM_Resource106: "GRM_MARTE_Classifier" = None, MARTE_GRM_Resource108: "GRM_MARTE_Lifeline" = None, MARTE_GRM_Resource110: "GRM_MARTE_ConnectableElement" = None, MARTE_GRM_Resource: "NFP_Integer" = None, MARTE_GRM_Resource102: "GRM_MARTE_Property" = None, MARTE_GRM_Resource104: "GRM_MARTE_InstanceSpecification" = None):
        self.isProtected = isProtected
        self.MARTE_GRM_Resource106 = MARTE_GRM_Resource106
        self.MARTE_GRM_Resource108 = MARTE_GRM_Resource108
        self.MARTE_GRM_Resource110 = MARTE_GRM_Resource110
        self.MARTE_GRM_Resource = MARTE_GRM_Resource
        self.MARTE_GRM_Resource102 = MARTE_GRM_Resource102
        self.MARTE_GRM_Resource104 = MARTE_GRM_Resource104
        
        pass
    @property
    def isProtected(self):
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
class Time_MARTE_Message:

    pass
class Time_MARTE_Behavior:

    pass
class Time_MARTE_Action:

    pass
class Time_MARTE_TimeEvent:

    pass
class Resource:

    pass
class MARTE_GRM_SynchronizationResource(Resource):

    pass
class MARTE_GRM_CommunicationEndPoint(Resource):

    pass
class MARTE_GRM_SchedulableResource(Resource):

    pass
class MARTE_GRM_TimingResource(Resource):

    pass
class MARTE_HwGeneral_HwResource(Resource):

    def __init__(self, name: str, MARTE_HwGeneral_HwResource: "NFP_String" = None, MARTE_HwGeneral_HwResource511: set["HwGeneral_HwResourceService"] = None, MARTE_HwGeneral_HwResource513: set["HwGeneral_HwResourceService"] = None, MARTE_HwGeneral_HwResource516: set["HwGeneral_HwResource"] = None, MARTE_HwGeneral_HwResource518: set["HwCommunication_HwEndPoint"] = None, MARTE_HwGeneral_HwResource520: "NFP_Frequency" = None, MARTE_HwGeneral_HwResource522: set["HwGeneral_MARTE_Operation"] = None, MARTE_HwGeneral_HwResource524: set["HwGeneral_MARTE_Activity"] = None):
        self.name = name
        self.MARTE_HwGeneral_HwResource = MARTE_HwGeneral_HwResource
        self.MARTE_HwGeneral_HwResource511 = MARTE_HwGeneral_HwResource511 if MARTE_HwGeneral_HwResource511 is not None else set()
        self.MARTE_HwGeneral_HwResource513 = MARTE_HwGeneral_HwResource513 if MARTE_HwGeneral_HwResource513 is not None else set()
        self.MARTE_HwGeneral_HwResource516 = MARTE_HwGeneral_HwResource516 if MARTE_HwGeneral_HwResource516 is not None else set()
        self.MARTE_HwGeneral_HwResource518 = MARTE_HwGeneral_HwResource518 if MARTE_HwGeneral_HwResource518 is not None else set()
        self.MARTE_HwGeneral_HwResource520 = MARTE_HwGeneral_HwResource520
        self.MARTE_HwGeneral_HwResource522 = MARTE_HwGeneral_HwResource522 if MARTE_HwGeneral_HwResource522 is not None else set()
        self.MARTE_HwGeneral_HwResource524 = MARTE_HwGeneral_HwResource524 if MARTE_HwGeneral_HwResource524 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def MARTE_HwGeneral_HwResource518(self):
        return self.__MARTE_HwGeneral_HwResource518

    @MARTE_HwGeneral_HwResource518.setter
    def MARTE_HwGeneral_HwResource518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource518", None)
        self.__MARTE_HwGeneral_HwResource518 = value if value is not None else set()
        
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
    def MARTE_HwGeneral_HwResource516(self):
        return self.__MARTE_HwGeneral_HwResource516

    @MARTE_HwGeneral_HwResource516.setter
    def MARTE_HwGeneral_HwResource516(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource516", None)
        self.__MARTE_HwGeneral_HwResource516 = value if value is not None else set()
        
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
    def MARTE_HwGeneral_HwResource520(self):
        return self.__MARTE_HwGeneral_HwResource520

    @MARTE_HwGeneral_HwResource520.setter
    def MARTE_HwGeneral_HwResource520(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource520", None)
        self.__MARTE_HwGeneral_HwResource520 = value
        
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

    @property
    def MARTE_HwGeneral_HwResource522(self):
        return self.__MARTE_HwGeneral_HwResource522

    @MARTE_HwGeneral_HwResource522.setter
    def MARTE_HwGeneral_HwResource522(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource522", None)
        self.__MARTE_HwGeneral_HwResource522 = value if value is not None else set()
        
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
    def MARTE_HwGeneral_HwResource511(self):
        return self.__MARTE_HwGeneral_HwResource511

    @MARTE_HwGeneral_HwResource511.setter
    def MARTE_HwGeneral_HwResource511(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource511", None)
        self.__MARTE_HwGeneral_HwResource511 = value if value is not None else set()
        
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
    def MARTE_HwGeneral_HwResource524(self):
        return self.__MARTE_HwGeneral_HwResource524

    @MARTE_HwGeneral_HwResource524.setter
    def MARTE_HwGeneral_HwResource524(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource524", None)
        self.__MARTE_HwGeneral_HwResource524 = value if value is not None else set()
        
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
    def MARTE_HwGeneral_HwResource513(self):
        return self.__MARTE_HwGeneral_HwResource513

    @MARTE_HwGeneral_HwResource513.setter
    def MARTE_HwGeneral_HwResource513(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_HwGeneral_HwResource__MARTE_HwGeneral_HwResource513", None)
        self.__MARTE_HwGeneral_HwResource513 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HwGeneral_HwResourceService514"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService514", None)
                    
                    if opp_val == self:
                        setattr(item, "HwGeneral_HwResourceService514", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HwGeneral_HwResourceService514"):
                    opp_val = getattr(item, "HwGeneral_HwResourceService514", None)
                    
                    setattr(item, "HwGeneral_HwResourceService514", self)
                    

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
            if hasattr(old_value, "NFP_String509"):
                opp_val = getattr(old_value, "NFP_String509", None)
                if opp_val == self:
                    setattr(old_value, "NFP_String509", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_String509"):
                opp_val = getattr(value, "NFP_String509", None)
                setattr(value, "NFP_String509", self)

class MARTE_GRM_ProcessingResource(Resource):

    pass
class MARTE_GRM_Scheduler(Resource):

    def __init__(self, isPreemptible: str, schedPolicy: str, otherSchedPolicy: str, MARTE_GRM_Scheduler: "GRM_MARTE_OpaqueExpression" = None, MARTE_GRM_Scheduler117: set["GRM_ProcessingResource"] = None, MARTE_GRM_Scheduler119: "GRM_ComputingResource" = None, scheduler: set["GRM_MutualExclusionResource"] = None, host: set["GRM_SchedulableResource"] = None):
        self.isPreemptible = isPreemptible
        self.schedPolicy = schedPolicy
        self.otherSchedPolicy = otherSchedPolicy
        self.MARTE_GRM_Scheduler = MARTE_GRM_Scheduler
        self.MARTE_GRM_Scheduler117 = MARTE_GRM_Scheduler117 if MARTE_GRM_Scheduler117 is not None else set()
        self.MARTE_GRM_Scheduler119 = MARTE_GRM_Scheduler119
        self.scheduler = scheduler if scheduler is not None else set()
        self.host = host if host is not None else set()
        
        pass
    @property
    def isPreemptible(self):
        return self.__isPreemptible

    @isPreemptible.setter
    def isPreemptible(self, isPreemptible: str):
        self.__isPreemptible = isPreemptible


    @property
    def otherSchedPolicy(self):
        return self.__otherSchedPolicy

    @otherSchedPolicy.setter
    def otherSchedPolicy(self, otherSchedPolicy: str):
        self.__otherSchedPolicy = otherSchedPolicy


    @property
    def schedPolicy(self):
        return self.__schedPolicy

    @schedPolicy.setter
    def schedPolicy(self, schedPolicy: str):
        self.__schedPolicy = schedPolicy


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
                    

class MARTE_GRM_ConcurrencyResource(Resource):

    pass
class MARTE_GRM_MutualExclusionResource(Resource):

    def __init__(self, protectKind: str, otherProtectProtocol: str, MARTE_GRM_MutualExclusionResource: "NFP_Integer" = None, protectedSharedRsources: "GRM_Scheduler" = None):
        self.protectKind = protectKind
        self.otherProtectProtocol = otherProtectProtocol
        self.MARTE_GRM_MutualExclusionResource = MARTE_GRM_MutualExclusionResource
        self.protectedSharedRsources = protectedSharedRsources
        
        pass
    @property
    def otherProtectProtocol(self):
        return self.__otherProtectProtocol

    @otherProtectProtocol.setter
    def otherProtectProtocol(self, otherProtectProtocol: str):
        self.__otherProtectProtocol = otherProtectProtocol


    @property
    def protectKind(self):
        return self.__protectKind

    @protectKind.setter
    def protectKind(self, protectKind: str):
        self.__protectKind = protectKind


    @property
    def protectedSharedRsources(self):
        return self.__protectedSharedRsources

    @protectedSharedRsources.setter
    def protectedSharedRsources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_GRM_MutualExclusionResource__protectedSharedRsources", None)
        self.__protectedSharedRsources = value
        
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
            if hasattr(old_value, "NFP_Integer126"):
                opp_val = getattr(old_value, "NFP_Integer126", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Integer126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Integer126"):
                opp_val = getattr(value, "NFP_Integer126", None)
                setattr(value, "NFP_Integer126", self)

class MARTE_PAM_PaLogicalResource(Resource):

    pass
class MARTE_SW_ResourceCore_SwResource(Resource):

    pass
class MARTE_GRM_StorageResource(Resource):

    pass
class GRM_MARTE_ConnectableElement:

    pass
class GRM_MARTE_Lifeline:

    pass
class GRM_MARTE_Classifier:

    pass
class TimedObservation:

    pass
class MARTE_Time_TimedInstantObservation(TimedObservation):

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

class Time_TimedElement:

    pass
class Time_MARTE_ValueSpecification:

    pass
class TimedElement:

    pass
class MARTE_Time_TimedObservation(TimedElement):

    pass
class MARTE_Time_TimedProcessing(TimedElement):

    pass
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
class MARTE_Time_TimedEvent(TimedElement):

    def __init__(self, repetition: str, MARTE_Time_TimedEvent: "Time_MARTE_TimeEvent" = None, MARTE_Time_TimedEvent85: "Time_MARTE_ValueSpecification" = None):
        self.repetition = repetition
        self.MARTE_Time_TimedEvent = MARTE_Time_TimedEvent
        self.MARTE_Time_TimedEvent85 = MARTE_Time_TimedEvent85
        
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

class Time_MARTE_DurationObservation:

    pass
class MARTE_Time_TimedDurationObservation(TimedObservation):

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

class Time_MARTE_TimeObservation:

    pass
class Time_MARTE_Enumeration:

    pass
class MARTE_Time_ClockType:

    def __init__(self, isLogical: str, nature: str, MARTE_Time_ClockType: "Time_MARTE_Enumeration" = None, MARTE_Time_ClockType61: "Time_MARTE_Property" = None, MARTE_Time_ClockType64: "Time_MARTE_Property" = None, MARTE_Time_ClockType67: "Time_MARTE_Property" = None, MARTE_Time_ClockType70: "Time_MARTE_Operation" = None, MARTE_Time_ClockType72: "Time_MARTE_Operation" = None, MARTE_Time_ClockType75: "Time_MARTE_Operation" = None, MARTE_Time_ClockType78: "Time_MARTE_Class" = None):
        self.isLogical = isLogical
        self.nature = nature
        self.MARTE_Time_ClockType = MARTE_Time_ClockType
        self.MARTE_Time_ClockType61 = MARTE_Time_ClockType61
        self.MARTE_Time_ClockType64 = MARTE_Time_ClockType64
        self.MARTE_Time_ClockType67 = MARTE_Time_ClockType67
        self.MARTE_Time_ClockType70 = MARTE_Time_ClockType70
        self.MARTE_Time_ClockType72 = MARTE_Time_ClockType72
        self.MARTE_Time_ClockType75 = MARTE_Time_ClockType75
        self.MARTE_Time_ClockType78 = MARTE_Time_ClockType78
        
        pass
    @property
    def nature(self):
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature


    @property
    def isLogical(self):
        return self.__isLogical

    @isLogical.setter
    def isLogical(self, isLogical: str):
        self.__isLogical = isLogical


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

class Time_MARTE_Property:

    pass
class Time_ClockType:

    pass
class Time_MARTE_InstanceSpecification:

    pass
class MARTE_Time_Clock:

    def __init__(self, standard: str, MARTE_Time_Clock: "Time_MARTE_InstanceSpecification" = None, MARTE_Time_Clock53: "Time_ClockType" = None, MARTE_Time_Clock55: "NFPs_Unit" = None, MARTE_Time_Clock58: "Time_MARTE_Property" = None):
        self.standard = standard
        self.MARTE_Time_Clock = MARTE_Time_Clock
        self.MARTE_Time_Clock53 = MARTE_Time_Clock53
        self.MARTE_Time_Clock55 = MARTE_Time_Clock55
        self.MARTE_Time_Clock58 = MARTE_Time_Clock58
        
        pass
    @property
    def standard(self):
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

class Time_MARTE_Operation:

    pass
class MARTE_Alloc_Assign:

    pass
class NFPs_NfpConstraint:

    pass
class MARTE_Time_TimedConstraint(Time_TimedElement, NFPs_NfpConstraint):

    def __init__(self, interpretation: str, NFPs_NfpConstraint: "MARTE_Alloc_NfpRefine" = None, NFPs_NfpConstraint49: "MARTE_Alloc_Allocate" = None, NFPs_NfpConstraint38: "MARTE_Alloc_Assign" = None):
        self.interpretation = interpretation
        
        pass
    @property
    def interpretation(self):
        return self.__interpretation

    @interpretation.setter
    def interpretation(self, interpretation: str):
        self.__interpretation = interpretation


class MARTE_Time_ClockConstraint(Time_TimedElement, NFPs_NfpConstraint):

    def __init__(self, isCoincidenceBased: str, isPrecedenceBased: bool, isChronometricBased: str, NFPs_NfpConstraint: "MARTE_Alloc_NfpRefine" = None, NFPs_NfpConstraint49: "MARTE_Alloc_Allocate" = None, NFPs_NfpConstraint38: "MARTE_Alloc_Assign" = None):
        self.isCoincidenceBased = isCoincidenceBased
        self.isPrecedenceBased = isPrecedenceBased
        self.isChronometricBased = isChronometricBased
        
        pass
    @property
    def isCoincidenceBased(self):
        return self.__isCoincidenceBased

    @isCoincidenceBased.setter
    def isCoincidenceBased(self, isCoincidenceBased: str):
        self.__isCoincidenceBased = isCoincidenceBased


    @property
    def isPrecedenceBased(self):
        return self.__isPrecedenceBased

    @isPrecedenceBased.setter
    def isPrecedenceBased(self, isPrecedenceBased: bool):
        self.__isPrecedenceBased = isPrecedenceBased


    @property
    def isChronometricBased(self):
        return self.__isChronometricBased

    @isChronometricBased.setter
    def isChronometricBased(self, isChronometricBased: str):
        self.__isChronometricBased = isChronometricBased


class Alloc_MARTE_Dependency:

    pass
class MARTE_Alloc_NfpRefine:

    pass
class Alloc_MARTE_ActivityPartition:

    pass
class MARTE_Alloc_AllocateActivityGroup:

    pass
class Alloc_Allocated:

    pass
class Alloc_MARTE_NamedElement:

    pass
class MARTE_Alloc_Allocated:

    pass
class CoreElements_MARTE_State:

    pass
class MARTE_CoreElements_Mode:

    pass
class Alloc_MARTE_Comment:

    pass
class Alloc_MARTE_Element:

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
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


    @property
    def baseExponent(self):
        return self.__baseExponent

    @baseExponent.setter
    def baseExponent(self, baseExponent: int):
        self.__baseExponent = baseExponent


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
class CoreElements_Mode:

    pass
class NFPs_MARTE_Constraint:

    pass
class MARTE_NFPs_NfpConstraint:

    def __init__(self, kind: str, MARTE_NFPs_NfpConstraint6: set["CoreElements_Mode"] = None, MARTE_NFPs_NfpConstraint: "NFPs_MARTE_Constraint" = None):
        self.kind = kind
        self.MARTE_NFPs_NfpConstraint6 = MARTE_NFPs_NfpConstraint6 if MARTE_NFPs_NfpConstraint6 is not None else set()
        self.MARTE_NFPs_NfpConstraint = MARTE_NFPs_NfpConstraint
        
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
class MARTE_NFPs_Nfp:

    pass
class NFPs_Unit:

    pass
class MARTE_NFPs_Unit:

    def __init__(self, convFactor: str, offsetFactor: str, MARTE_NFPs_Unit: "NFPs_Unit" = None, MARTE_NFPs_Unit3: "NFPs_MARTE_EnumerationLiteral" = None):
        self.convFactor = convFactor
        self.offsetFactor = offsetFactor
        self.MARTE_NFPs_Unit = MARTE_NFPs_Unit
        self.MARTE_NFPs_Unit3 = MARTE_NFPs_Unit3
        
        pass
    @property
    def offsetFactor(self):
        return self.__offsetFactor

    @offsetFactor.setter
    def offsetFactor(self, offsetFactor: str):
        self.__offsetFactor = offsetFactor


    @property
    def convFactor(self):
        return self.__convFactor

    @convFactor.setter
    def convFactor(self, convFactor: str):
        self.__convFactor = convFactor


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