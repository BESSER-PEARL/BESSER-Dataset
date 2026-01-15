from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SourceKind(Enum):
    est = "est"
    meas = "meas"
    calc = "calc"
    req = "req"
class PowerUnitKind(Enum):
    W = "W"
    mW = "mW"
    KW = "KW"
class FrequencyUnitKind(Enum):
    Hz = "Hz"
    KHz = "KHz"
    MHz = "MHz"
    GHz = "GHz"
    rpm = "rpm"
class LengthUnitKind(Enum):
    m = "m"
    cm = "cm"
    mm = "mm"
class TUK(Enum):
class WeightUnitKind(Enum):
    g = "g"
    mg = "mg"
    kg = "kg"
class DataSizeUnitKind(Enum):
    bit = "bit"
    Byte = "Byte"
    KB = "KB"
    MB = "MB"
    GB = "GB"
class TimeStandardKind(Enum):
    UTC = "UTC"
    Local = "Local"
    TAI = "TAI"
    UT0 = "UT0"
    UT1 = "UT1"
    TT = "TT"
    TBD = "TBD"
    TCG = "TCG"
    TCB = "TCB"
    Sidereal = "Sidereal"
    GPS = "GPS"
class TimeUnitKind(Enum):
    s = "s"
    ms = "ms"
    us = "us"
    ns = "ns"
    min = "min"
    hrs = "hrs"
    day = "day"
class EnergyUnitKind(Enum):
    J = "J"
    KJ = "KJ"
    Wh = "Wh"
    KWh = "KWh"
    mWh = "mWh"
class TimeInterpretationKind(Enum):
    duration = "duration"
    instant = "instant"
class StatisticalQualifierKind(Enum):
    max = "max"
    min = "min"
    mean = "mean"
    range = "range"
    percent = "percent"
    distrib = "distrib"
    determ = "determ"
    other = "other"
    variance = "variance"
class TimeNatureKind(Enum):
    discrete = "discrete"
    dense = "dense"
class EventKind(Enum):
    start = "start"
    finish = "finish"
    send = "send"
    receive = "receive"
    consume = "consume"
class LogicalTimeUnit(Enum):
    tick = "tick"
class AreaUnitKind(Enum):
    mm2 = "mm2"
    um2 = "um2"
class DataTxRateUnitKind(Enum):
    b_per_s = "b_per_s"
    Kb_per_s = "Kb_per_s"
    Mb_per_s = "Mb_per_s"
class TransmModeKind(Enum):
    simplex = "simplex"
    halfDuplex = "halfDuplex"
    fullDuplex = "fullDuplex"
class DirectionKind(Enum):
    incr = "incr"
    decr = "decr"
class SchedPolicyKind(Enum):
    EarliestDeadlineFirst = "EarliestDeadlineFirst"
    FIFO = "FIFO"
    FixedPriority = "FixedPriority"
    LeastLaxityFirst = "LeastLaxityFirst"
    RoundRobin = "RoundRobin"
    TimeTableDriven = "TimeTableDriven"
    Undef = "Undef"
    Other = "Other"
class ProtectProtocolKind(Enum):
    FIFO = "FIFO"
    NoPreemption = "NoPreemption"
    PriorityCeiling = "PriorityCeiling"
    PriorityInheritance = "PriorityInheritance"
    StackBased = "StackBased"
    Undef = "Undef"
    Other = "Other"
class PeriodicServerKind(Enum):
    Sporadic = "Sporadic"
    Deferrable = "Deferrable"
    Undef = "Undef"
    Other = "Other"


############################################
# Definition of Classes
############################################

class MARTE_Library_RS_Library_ShapeSpecification:

    def __init__(self, size: str):
        self.size = size
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

class IntegerMatrix:

    pass
class MARTE_Library_TimeLibrary_IdealClock:

    def __init__(self):
        
    def currentTime(self) -> str:
        # TODO: Implement currentTime method
        pass

class MARTE_Library_RS_Library_TilerSpecification:

    pass
class MARTE_Library_TimeLibrary_TimedValueType:

    def __init__(self, onClock: str, unit: str, value: str, expr: str):
        self.onClock = onClock
        self.unit = unit
        self.value = value
        self.expr = expr
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def onClock(self) -> str:
        return self.__onClock

    @onClock.setter
    def onClock(self, onClock: str):
        self.__onClock = onClock

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class MARTE_Library_MARTE_DataTypes_RealMatrix:

    def __init__(self, matrixElem: str):
        self.matrixElem = matrixElem
        
    @property
    def matrixElem(self) -> str:
        return self.__matrixElem

    @matrixElem.setter
    def matrixElem(self, matrixElem: str):
        self.__matrixElem = matrixElem

    def at(self, i: int, p: str):
        # TODO: Implement at method
        pass

class MARTE_Library_MARTE_DataTypes_RealVector:

    def __init__(self, vectorElem: str):
        self.vectorElem = vectorElem
        
    @property
    def vectorElem(self) -> str:
        return self.__vectorElem

    @vectorElem.setter
    def vectorElem(self, vectorElem: str):
        self.__vectorElem = vectorElem

    def at(self, i: int) -> str:
        # TODO: Implement at method
        pass

class NFP_Natural:

    pass
class MARTE_Library_MARTE_DataTypes_NFP_FrequencyInterval:

    pass
class MARTE_Library_MARTE_DataTypes_Realnterval:

    def __init__(self, bound: str):
        self.bound = bound
        
    @property
    def bound(self) -> str:
        return self.__bound

    @bound.setter
    def bound(self, bound: str):
        self.__bound = bound

class MARTE_Library_MARTE_DataTypes_Interval:

    pass
class MARTE_Library_MARTE_DataTypes_Array:

    def __init__(self):
        
    def at(self, i: int):
        # TODO: Implement at method
        pass

class MARTE_Library_MARTE_DataTypes_NFP_NaturalInterval:

    pass
class MARTE_Library_MARTE_DataTypes_UtilityType:

    def __init__(self):
        
    def le(self, u: str) -> str:
        # TODO: Implement le method
        pass

    def lt(self, u: str) -> str:
        # TODO: Implement lt method
        pass

    def gt(self, u: str) -> str:
        # TODO: Implement gt method
        pass

    def ne(self, u: str) -> str:
        # TODO: Implement ne method
        pass

    def ge(self, u: str) -> str:
        # TODO: Implement ge method
        pass

    def eq(self, u: str) -> str:
        # TODO: Implement eq method
        pass

class MARTE_Library_MARTE_DataTypes_IntegerInterval:

    def __init__(self, bound: str):
        self.bound = bound
        
    @property
    def bound(self) -> str:
        return self.__bound

    @bound.setter
    def bound(self, bound: str):
        self.__bound = bound

class IntegerVector:

    pass
class MARTE_Library_MARTE_DataTypes_IntegerMatrix:

    def __init__(self, MARTE_Library_MARTE_DataTypes_IntegerMatrix: set["IntegerVector"] = None):
        self.MARTE_Library_MARTE_DataTypes_IntegerMatrix = MARTE_Library_MARTE_DataTypes_IntegerMatrix if MARTE_Library_MARTE_DataTypes_IntegerMatrix is not None else set()
        
    @property
    def MARTE_Library_MARTE_DataTypes_IntegerMatrix(self):
        return self.__MARTE_Library_MARTE_DataTypes_IntegerMatrix

    @MARTE_Library_MARTE_DataTypes_IntegerMatrix.setter
    def MARTE_Library_MARTE_DataTypes_IntegerMatrix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Library_MARTE_DataTypes_IntegerMatrix__MARTE_Library_MARTE_DataTypes_IntegerMatrix", None)
        self.__MARTE_Library_MARTE_DataTypes_IntegerMatrix = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IntegerVector"):
                    opp_val = getattr(item, "IntegerVector", None)
                    
                    if opp_val == self:
                        setattr(item, "IntegerVector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IntegerVector"):
                    opp_val = getattr(item, "IntegerVector", None)
                    
                    setattr(item, "IntegerVector", self)
                    

    def at(self, i: int) -> str:
        # TODO: Implement at method
        pass

class MARTE_Library_MARTE_DataTypes_IntegerVector:

    def __init__(self, vectorElem: str):
        self.vectorElem = vectorElem
        
    @property
    def vectorElem(self) -> str:
        return self.__vectorElem

    @vectorElem.setter
    def vectorElem(self, vectorElem: str):
        self.__vectorElem = vectorElem

    def at(self, i: str) -> str:
        # TODO: Implement at method
        pass

class NFP_Frequency:

    pass
class MARTE_Library_BasicNFP_Types_OpenPattern:

    def __init__(self, arrivalProcess: str, MARTE_Library_BasicNFP_Types_OpenPattern: "NFP_Duration" = None, MARTE_Library_BasicNFP_Types_OpenPattern82: "NFP_Frequency" = None):
        self.arrivalProcess = arrivalProcess
        self.MARTE_Library_BasicNFP_Types_OpenPattern = MARTE_Library_BasicNFP_Types_OpenPattern
        self.MARTE_Library_BasicNFP_Types_OpenPattern82 = MARTE_Library_BasicNFP_Types_OpenPattern82
        
    @property
    def arrivalProcess(self) -> str:
        return self.__arrivalProcess

    @arrivalProcess.setter
    def arrivalProcess(self, arrivalProcess: str):
        self.__arrivalProcess = arrivalProcess

    @property
    def MARTE_Library_BasicNFP_Types_OpenPattern(self):
        return self.__MARTE_Library_BasicNFP_Types_OpenPattern

    @MARTE_Library_BasicNFP_Types_OpenPattern.setter
    def MARTE_Library_BasicNFP_Types_OpenPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Library_BasicNFP_Types_OpenPattern__MARTE_Library_BasicNFP_Types_OpenPattern", None)
        self.__MARTE_Library_BasicNFP_Types_OpenPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Duration80"):
                opp_val = getattr(old_value, "NFP_Duration80", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Duration80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Duration80"):
                opp_val = getattr(value, "NFP_Duration80", None)
                setattr(value, "NFP_Duration80", self)

    @property
    def MARTE_Library_BasicNFP_Types_OpenPattern82(self):
        return self.__MARTE_Library_BasicNFP_Types_OpenPattern82

    @MARTE_Library_BasicNFP_Types_OpenPattern82.setter
    def MARTE_Library_BasicNFP_Types_OpenPattern82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Library_BasicNFP_Types_OpenPattern__MARTE_Library_BasicNFP_Types_OpenPattern82", None)
        self.__MARTE_Library_BasicNFP_Types_OpenPattern82 = value
        
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

class MARTE_Library_BasicNFP_Types_ClosedPattern:

    pass
class MARTE_Library_BasicNFP_Types_AperiodicPattern:

    pass
class MARTE_Library_BasicNFP_Types_PeriodicPattern:

    pass
class OpenPattern:

    pass
class ClosedPattern:

    pass
class IrregularPattern:

    pass
class BurstPattern:

    pass
class AperiodicPattern:

    pass
class MARTE_Library_BasicNFP_Types_IrregularPattern(AperiodicPattern):

    pass
class MARTE_Library_BasicNFP_Types_SporadicPattern(AperiodicPattern):

    pass
class MARTE_Library_BasicNFP_Types_BurstPattern(AperiodicPattern):

    pass
class PeriodicPattern:

    pass
class MARTE_Library_BasicNFP_Types_ArrivalPattern:

    pass
class SporadicPattern:

    pass
class NFP_CommonType:

    pass
class MARTE_Library_BasicNFP_Types_NFP_String(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class MARTE_Library_BasicNFP_Types_NFP_DateTime(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class MARTE_Library_BasicNFP_Types_NFP_Integer(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class MARTE_Library_BasicNFP_Types_NFP_Natural(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class MARTE_Library_BasicNFP_Types_NFP_Real(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class NFP_Real:

    pass
class MARTE_Library_BasicNFP_Types_NFP_DataSize(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class MARTE_Library_BasicNFP_Types_NFP_Duration(NFP_Real):

    def __init__(self, unit: str, clock: str, precision: str, worst: str, best: str):
        self.unit = unit
        self.clock = clock
        self.precision = precision
        self.worst = worst
        self.best = best
        
    @property
    def clock(self) -> str:
        return self.__clock

    @clock.setter
    def clock(self, clock: str):
        self.__clock = clock

    @property
    def worst(self) -> str:
        return self.__worst

    @worst.setter
    def worst(self, worst: str):
        self.__worst = worst

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def best(self) -> str:
        return self.__best

    @best.setter
    def best(self, best: str):
        self.__best = best

    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class MARTE_Library_BasicNFP_Types_NFP_Price(NFP_Real):

    def __init__(self, unit: str):
        self.unit = unit
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class MARTE_Library_BasicNFP_Types_NFP_Length(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class MARTE_Library_BasicNFP_Types_NFP_Power(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class MARTE_Library_BasicNFP_Types_NFP_Area(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class MARTE_Library_BasicNFP_Types_NFP_Percentage(NFP_Real):

    def __init__(self, unit: str):
        self.unit = unit
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class MARTE_Library_BasicNFP_Types_NFP_Weight(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class MARTE_Library_BasicNFP_Types_NFP_Energy(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class MARTE_Library_BasicNFP_Types_NFP_DataTxRate(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class MARTE_Library_BasicNFP_Types_NFP_Frequency(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class MARTE_Library_BasicNFP_Types_NFP_Boolean(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class MARTE_Library_BasicNFP_Types_NFP_CommonType:

    def __init__(self, expr: str, source: str, statQ: str, dir: str, mode: str):
        self.expr = expr
        self.source = source
        self.statQ = statQ
        self.dir = dir
        self.mode = mode
        
    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def statQ(self) -> str:
        return self.__statQ

    @statQ.setter
    def statQ(self, statQ: str):
        self.__statQ = statQ

    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    def exp(self, mean: str):
        # TODO: Implement exp method
        pass

    def gamma(self, mean: str, k: int):
        # TODO: Implement gamma method
        pass

    def triangular(self, max: str, min: str, mode: str):
        # TODO: Implement triangular method
        pass

    def bernoulli(self, prob: str):
        # TODO: Implement bernoulli method
        pass

    def uniform(self, max: str, min: str):
        # TODO: Implement uniform method
        pass

    def geometric(self, p: str):
        # TODO: Implement geometric method
        pass

    def normal(self, mean: str, standDev: str):
        # TODO: Implement normal method
        pass

    def gamma(self, k: str, mean: str):
        # TODO: Implement gamma method
        pass

    def binomial(self, trials: str, prob: str):
        # TODO: Implement binomial method
        pass

    def poisson(self, mean: str):
        # TODO: Implement poisson method
        pass

    def logarithmic(self, theta: str):
        # TODO: Implement logarithmic method
        pass

class NFP_Integer:

    pass
class MARTE_Library_GRM_BasicTypes_FixedPriorityParameters:

    pass
class PeriodicServerParameters:

    pass
class FixedPriorityParameters:

    pass
class MARTE_Library_GRM_BasicTypes_PoolingParameters(FixedPriorityParameters):

    pass
class MARTE_Library_GRM_BasicTypes_PeriodicServerParameters(FixedPriorityParameters):

    def __init__(self, kind: str, backgroundPriority: str, MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17: "NFP_Duration" = None, MARTE_Library_GRM_BasicTypes_PeriodicServerParameters: "NFP_Duration" = None, MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20: "NFP_Integer" = None, FixedPriorityParameters: "MARTE_Library_GRM_BasicTypes_SchedParameters"):
        self.kind = kind
        self.backgroundPriority = backgroundPriority
        self.MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17 = MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17
        self.MARTE_Library_GRM_BasicTypes_PeriodicServerParameters = MARTE_Library_GRM_BasicTypes_PeriodicServerParameters
        self.MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20 = MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20
        
    @property
    def backgroundPriority(self) -> str:
        return self.__backgroundPriority

    @backgroundPriority.setter
    def backgroundPriority(self, backgroundPriority: str):
        self.__backgroundPriority = backgroundPriority

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17(self):
        return self.__MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17

    @MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17.setter
    def MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Library_GRM_BasicTypes_PeriodicServerParameters__MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17", None)
        self.__MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Duration18"):
                opp_val = getattr(old_value, "NFP_Duration18", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Duration18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Duration18"):
                opp_val = getattr(value, "NFP_Duration18", None)
                setattr(value, "NFP_Duration18", self)

    @property
    def MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20(self):
        return self.__MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20

    @MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20.setter
    def MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Library_GRM_BasicTypes_PeriodicServerParameters__MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20", None)
        self.__MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Integer21"):
                opp_val = getattr(old_value, "NFP_Integer21", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Integer21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Integer21"):
                opp_val = getattr(value, "NFP_Integer21", None)
                setattr(value, "NFP_Integer21", self)

    @property
    def MARTE_Library_GRM_BasicTypes_PeriodicServerParameters(self):
        return self.__MARTE_Library_GRM_BasicTypes_PeriodicServerParameters

    @MARTE_Library_GRM_BasicTypes_PeriodicServerParameters.setter
    def MARTE_Library_GRM_BasicTypes_PeriodicServerParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Library_GRM_BasicTypes_PeriodicServerParameters__MARTE_Library_GRM_BasicTypes_PeriodicServerParameters", None)
        self.__MARTE_Library_GRM_BasicTypes_PeriodicServerParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NFP_Duration15"):
                opp_val = getattr(old_value, "NFP_Duration15", None)
                if opp_val == self:
                    setattr(old_value, "NFP_Duration15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NFP_Duration15"):
                opp_val = getattr(value, "NFP_Duration15", None)
                setattr(value, "NFP_Duration15", self)

class EDF_Parameters:

    pass
class MARTE_Library_GRM_BasicTypes_SchedParameters:

    def __init__(self, tableEntry: str, MARTE_Library_GRM_BasicTypes_SchedParameters: "EDF_Parameters" = None, MARTE_Library_GRM_BasicTypes_SchedParameters3: "FixedPriorityParameters" = None, MARTE_Library_GRM_BasicTypes_SchedParameters5: "PoolingParameters" = None, MARTE_Library_GRM_BasicTypes_SchedParameters7: "PeriodicServerParameters" = None):
        self.tableEntry = tableEntry
        self.MARTE_Library_GRM_BasicTypes_SchedParameters = MARTE_Library_GRM_BasicTypes_SchedParameters
        self.MARTE_Library_GRM_BasicTypes_SchedParameters3 = MARTE_Library_GRM_BasicTypes_SchedParameters3
        self.MARTE_Library_GRM_BasicTypes_SchedParameters5 = MARTE_Library_GRM_BasicTypes_SchedParameters5
        self.MARTE_Library_GRM_BasicTypes_SchedParameters7 = MARTE_Library_GRM_BasicTypes_SchedParameters7
        
    @property
    def tableEntry(self) -> str:
        return self.__tableEntry

    @tableEntry.setter
    def tableEntry(self, tableEntry: str):
        self.__tableEntry = tableEntry

    @property
    def MARTE_Library_GRM_BasicTypes_SchedParameters3(self):
        return self.__MARTE_Library_GRM_BasicTypes_SchedParameters3

    @MARTE_Library_GRM_BasicTypes_SchedParameters3.setter
    def MARTE_Library_GRM_BasicTypes_SchedParameters3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Library_GRM_BasicTypes_SchedParameters__MARTE_Library_GRM_BasicTypes_SchedParameters3", None)
        self.__MARTE_Library_GRM_BasicTypes_SchedParameters3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FixedPriorityParameters"):
                opp_val = getattr(old_value, "FixedPriorityParameters", None)
                if opp_val == self:
                    setattr(old_value, "FixedPriorityParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FixedPriorityParameters"):
                opp_val = getattr(value, "FixedPriorityParameters", None)
                setattr(value, "FixedPriorityParameters", self)

    @property
    def MARTE_Library_GRM_BasicTypes_SchedParameters7(self):
        return self.__MARTE_Library_GRM_BasicTypes_SchedParameters7

    @MARTE_Library_GRM_BasicTypes_SchedParameters7.setter
    def MARTE_Library_GRM_BasicTypes_SchedParameters7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Library_GRM_BasicTypes_SchedParameters__MARTE_Library_GRM_BasicTypes_SchedParameters7", None)
        self.__MARTE_Library_GRM_BasicTypes_SchedParameters7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PeriodicServerParameters"):
                opp_val = getattr(old_value, "PeriodicServerParameters", None)
                if opp_val == self:
                    setattr(old_value, "PeriodicServerParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PeriodicServerParameters"):
                opp_val = getattr(value, "PeriodicServerParameters", None)
                setattr(value, "PeriodicServerParameters", self)

    @property
    def MARTE_Library_GRM_BasicTypes_SchedParameters5(self):
        return self.__MARTE_Library_GRM_BasicTypes_SchedParameters5

    @MARTE_Library_GRM_BasicTypes_SchedParameters5.setter
    def MARTE_Library_GRM_BasicTypes_SchedParameters5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Library_GRM_BasicTypes_SchedParameters__MARTE_Library_GRM_BasicTypes_SchedParameters5", None)
        self.__MARTE_Library_GRM_BasicTypes_SchedParameters5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PoolingParameters"):
                opp_val = getattr(old_value, "PoolingParameters", None)
                if opp_val == self:
                    setattr(old_value, "PoolingParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PoolingParameters"):
                opp_val = getattr(value, "PoolingParameters", None)
                setattr(value, "PoolingParameters", self)

    @property
    def MARTE_Library_GRM_BasicTypes_SchedParameters(self):
        return self.__MARTE_Library_GRM_BasicTypes_SchedParameters

    @MARTE_Library_GRM_BasicTypes_SchedParameters.setter
    def MARTE_Library_GRM_BasicTypes_SchedParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MARTE_Library_GRM_BasicTypes_SchedParameters__MARTE_Library_GRM_BasicTypes_SchedParameters", None)
        self.__MARTE_Library_GRM_BasicTypes_SchedParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EDF_Parameters"):
                opp_val = getattr(old_value, "EDF_Parameters", None)
                if opp_val == self:
                    setattr(old_value, "EDF_Parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EDF_Parameters"):
                opp_val = getattr(value, "EDF_Parameters", None)
                setattr(value, "EDF_Parameters", self)

class PoolingParameters:

    pass
class NFP_Duration:

    pass
class MARTE_Library_GRM_BasicTypes_EDF_Parameters:

    pass