from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PeriodicServerKind(Enum):
    Sporadic = "Sporadic"
    Deferrable = "Deferrable"
    Undef = "Undef"
    Other = "Other"
class TimeInterpretationKind(Enum):
    duration = "duration"
    instant = "instant"
class TransmModeKind(Enum):
    simplex = "simplex"
    halfDuplex = "halfDuplex"
    fullDuplex = "fullDuplex"
class FrequencyUnitKind(Enum):
    Hz = "Hz"
    KHz = "KHz"
    MHz = "MHz"
    GHz = "GHz"
    rpm = "rpm"
class LogicalTimeUnit(Enum):
    tick = "tick"
class TimeUnitKind(Enum):
    s = "s"
    ms = "ms"
    us = "us"
    ns = "ns"
    min = "min"
    hrs = "hrs"
    day = "day"
class DataTxRateUnitKind(Enum):
    b_per_s = "b_per_s"
    Kb_per_s = "Kb_per_s"
    Mb_per_s = "Mb_per_s"
class SourceKind(Enum):
    est = "est"
    meas = "meas"
    calc = "calc"
    req = "req"
class DataSizeUnitKind(Enum):
    bit = "bit"
    Byte = "Byte"
    KB = "KB"
    MB = "MB"
    GB = "GB"
class WeightUnitKind(Enum):
    g = "g"
    mg = "mg"
    kg = "kg"
class TimeNatureKind(Enum):
    discrete = "discrete"
    dense = "dense"
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
class PowerUnitKind(Enum):
    W = "W"
    mW = "mW"
    KW = "KW"
class SchedPolicyKind(Enum):
    EarliestDeadlineFirst = "EarliestDeadlineFirst"
    FIFO = "FIFO"
    FixedPriority = "FixedPriority"
    LeastLaxityFirst = "LeastLaxityFirst"
    RoundRobin = "RoundRobin"
    TimeTableDriven = "TimeTableDriven"
    Undef = "Undef"
    Other = "Other"
class TimeStandardKind(Enum):
    TAI = "TAI"
    UT0 = "UT0"
    UT1 = "UT1"
    UTC = "UTC"
    Local = "Local"
    TT = "TT"
    TBD = "TBD"
    TCG = "TCG"
    TCB = "TCB"
    Sidereal = "Sidereal"
    GPS = "GPS"
class LengthUnitKind(Enum):
    m = "m"
    cm = "cm"
    mm = "mm"
class AreaUnitKind(Enum):
    mm2 = "mm2"
    um2 = "um2"
class EventKind(Enum):
    start = "start"
    finish = "finish"
    send = "send"
    receive = "receive"
    consume = "consume"
class TUK(Enum):
class ProtectProtocolKind(Enum):
    PriorityCeiling = "PriorityCeiling"
    PriorityInheritance = "PriorityInheritance"
    StackBased = "StackBased"
    Undef = "Undef"
    Other = "Other"
    FIFO = "FIFO"
    NoPreemption = "NoPreemption"
class DirectionKind(Enum):
    incr = "incr"
    decr = "decr"
class EnergyUnitKind(Enum):
    J = "J"
    KJ = "KJ"
    Wh = "Wh"
    KWh = "KWh"
    mWh = "mWh"


############################################
# Definition of Classes
############################################

class MARTE_Library_RS_Library_ShapeSpecification:

    def __init__(self, size: str):
        self.size = size
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


class IntegerMatrix:

    pass
class MARTE_Library_RS_Library_TilerSpecification:

    pass
class MARTE_Library_TimeLibrary_IdealClock:

    def __init__(self):
        
        pass
    def currentTime(self) :
        # TODO: Implement currentTime method
        pass

class MARTE_Library_MARTE_DataTypes_RealMatrix:

    def __init__(self, matrixElem: str):
        self.matrixElem = matrixElem
        
        pass
    @property
    def matrixElem(self):
        return self.__matrixElem

    @matrixElem.setter
    def matrixElem(self, matrixElem: str):
        self.__matrixElem = matrixElem


    def at(self, MARTE_Library_p, MARTE_Library_i):
        # TODO: Implement at method
        pass

class MARTE_Library_MARTE_DataTypes_RealVector:

    def __init__(self, vectorElem: str):
        self.vectorElem = vectorElem
        
        pass
    @property
    def vectorElem(self):
        return self.__vectorElem

    @vectorElem.setter
    def vectorElem(self, vectorElem: str):
        self.__vectorElem = vectorElem


    def at(self, MARTE_Library_i) :
        # TODO: Implement at method
        pass

class NFP_Natural:

    pass
class MARTE_Library_MARTE_DataTypes_NFP_NaturalInterval:

    pass
class MARTE_Library_MARTE_DataTypes_NFP_FrequencyInterval:

    pass
class MARTE_Library_MARTE_DataTypes_Realnterval:

    def __init__(self, bound: str):
        self.bound = bound
        
        pass
    @property
    def bound(self):
        return self.__bound

    @bound.setter
    def bound(self, bound: str):
        self.__bound = bound


class MARTE_Library_MARTE_DataTypes_Interval:

    pass
class MARTE_Library_MARTE_DataTypes_Array:

    def __init__(self):
        
        pass
    def at(self, MARTE_Library_i):
        # TODO: Implement at method
        pass

class MARTE_Library_TimeLibrary_TimedValueType:

    def __init__(self, unit: str, value: str, expr: str, onClock: str):
        self.unit = unit
        self.value = value
        self.expr = expr
        self.onClock = onClock
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def expr(self):
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def onClock(self):
        return self.__onClock

    @onClock.setter
    def onClock(self, onClock: str):
        self.__onClock = onClock


class MARTE_Library_MARTE_DataTypes_IntegerMatrix:

    def __init__(self, MARTE_Library_MARTE_DataTypes_IntegerMatrix: set["IntegerVector"] = None):
        self.MARTE_Library_MARTE_DataTypes_IntegerMatrix = MARTE_Library_MARTE_DataTypes_IntegerMatrix if MARTE_Library_MARTE_DataTypes_IntegerMatrix is not None else set()
        
        pass
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
                    

    def at(self, MARTE_Library_i) :
        # TODO: Implement at method
        pass

class MARTE_Library_MARTE_DataTypes_IntegerVector:

    def __init__(self, vectorElem: str):
        self.vectorElem = vectorElem
        
        pass
    @property
    def vectorElem(self):
        return self.__vectorElem

    @vectorElem.setter
    def vectorElem(self, vectorElem: str):
        self.__vectorElem = vectorElem


    def at(self, MARTE_Library_i) :
        # TODO: Implement at method
        pass

class MARTE_Library_MARTE_DataTypes_UtilityType:

    def __init__(self):
        
        pass
    def le(self, MARTE_Library_u) :
        # TODO: Implement le method
        pass

    def gt(self, MARTE_Library_u) :
        # TODO: Implement gt method
        pass

    def lt(self, MARTE_Library_u) :
        # TODO: Implement lt method
        pass

    def eq(self, MARTE_Library_u) :
        # TODO: Implement eq method
        pass

    def ge(self, MARTE_Library_u) :
        # TODO: Implement ge method
        pass

    def ne(self, MARTE_Library_u) :
        # TODO: Implement ne method
        pass

class MARTE_Library_MARTE_DataTypes_IntegerInterval:

    def __init__(self, bound: str):
        self.bound = bound
        
        pass
    @property
    def bound(self):
        return self.__bound

    @bound.setter
    def bound(self, bound: str):
        self.__bound = bound


class IntegerVector:

    pass
class MARTE_Library_BasicNFP_Types_AperiodicPattern:

    pass
class MARTE_Library_BasicNFP_Types_PeriodicPattern:

    pass
class OpenPattern:

    pass
class NFP_Frequency:

    pass
class MARTE_Library_BasicNFP_Types_OpenPattern:

    def __init__(self, arrivalProcess: str, MARTE_Library_BasicNFP_Types_OpenPattern82: "NFP_Frequency" = None, MARTE_Library_BasicNFP_Types_OpenPattern: "NFP_Duration" = None):
        self.arrivalProcess = arrivalProcess
        self.MARTE_Library_BasicNFP_Types_OpenPattern82 = MARTE_Library_BasicNFP_Types_OpenPattern82
        self.MARTE_Library_BasicNFP_Types_OpenPattern = MARTE_Library_BasicNFP_Types_OpenPattern
        
        pass
    @property
    def arrivalProcess(self):
        return self.__arrivalProcess

    @arrivalProcess.setter
    def arrivalProcess(self, arrivalProcess: str):
        self.__arrivalProcess = arrivalProcess


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

class MARTE_Library_BasicNFP_Types_ClosedPattern:

    pass
class SporadicPattern:

    pass
class ClosedPattern:

    pass
class IrregularPattern:

    pass
class BurstPattern:

    pass
class AperiodicPattern:

    pass
class MARTE_Library_BasicNFP_Types_SporadicPattern(AperiodicPattern):

    pass
class MARTE_Library_BasicNFP_Types_BurstPattern(AperiodicPattern):

    pass
class MARTE_Library_BasicNFP_Types_IrregularPattern(AperiodicPattern):

    pass
class PeriodicPattern:

    pass
class MARTE_Library_BasicNFP_Types_ArrivalPattern:

    pass
class MARTE_Library_BasicNFP_Types_NFP_CommonType:

    def __init__(self, expr: str, source: str, statQ: str, dir: str, mode: str):
        self.expr = expr
        self.source = source
        self.statQ = statQ
        self.dir = dir
        self.mode = mode
        
        pass
    @property
    def expr(self):
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def statQ(self):
        return self.__statQ

    @statQ.setter
    def statQ(self, statQ: str):
        self.__statQ = statQ


    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode


    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    def normal(self, MARTE_Library_standDev, MARTE_Library_mean):
        # TODO: Implement normal method
        pass

    def uniform(self, MARTE_Library_max, MARTE_Library_min):
        # TODO: Implement uniform method
        pass

    def triangular(self, MARTE_Library_min, MARTE_Library_max, MARTE_Library_mode):
        # TODO: Implement triangular method
        pass

    def exp(self, MARTE_Library_mean):
        # TODO: Implement exp method
        pass

    def bernoulli(self, MARTE_Library_prob):
        # TODO: Implement bernoulli method
        pass

    def gamma(self, MARTE_Library_mean, MARTE_Library_k):
        # TODO: Implement gamma method
        pass

    def poisson(self, MARTE_Library_mean):
        # TODO: Implement poisson method
        pass

    def binomial(self, MARTE_Library_trials, MARTE_Library_prob):
        # TODO: Implement binomial method
        pass

    def geometric(self, MARTE_Library_p):
        # TODO: Implement geometric method
        pass

    def logarithmic(self, MARTE_Library_theta):
        # TODO: Implement logarithmic method
        pass

class NFP_CommonType:

    pass
class MARTE_Library_BasicNFP_Types_NFP_Boolean(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class MARTE_Library_BasicNFP_Types_NFP_String(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class MARTE_Library_BasicNFP_Types_NFP_Natural(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class MARTE_Library_BasicNFP_Types_NFP_Integer(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class MARTE_Library_BasicNFP_Types_NFP_DateTime(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class MARTE_Library_BasicNFP_Types_NFP_Real(NFP_CommonType):

    def __init__(self, value: str, NFP_CommonType: "MARTE_Library_BasicNFP_Types_AperiodicPattern" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class NFP_Real:

    pass
class MARTE_Library_BasicNFP_Types_NFP_Weight(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


class MARTE_Library_BasicNFP_Types_NFP_Percentage(NFP_Real):

    def __init__(self, unit: str):
        self.unit = unit
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


class MARTE_Library_BasicNFP_Types_NFP_Energy(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


class MARTE_Library_BasicNFP_Types_NFP_DataTxRate(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


class MARTE_Library_BasicNFP_Types_NFP_Area(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


class MARTE_Library_BasicNFP_Types_NFP_Length(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


class MARTE_Library_BasicNFP_Types_NFP_Duration(NFP_Real):

    def __init__(self, unit: str, clock: str, precision: str, worst: str, best: str):
        self.unit = unit
        self.clock = clock
        self.precision = precision
        self.worst = worst
        self.best = best
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


    @property
    def clock(self):
        return self.__clock

    @clock.setter
    def clock(self, clock: str):
        self.__clock = clock


    @property
    def best(self):
        return self.__best

    @best.setter
    def best(self, best: str):
        self.__best = best


    @property
    def worst(self):
        return self.__worst

    @worst.setter
    def worst(self, worst: str):
        self.__worst = worst


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


class MARTE_Library_BasicNFP_Types_NFP_Power(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


class MARTE_Library_BasicNFP_Types_NFP_Price(NFP_Real):

    def __init__(self, unit: str):
        self.unit = unit
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


class MARTE_Library_BasicNFP_Types_NFP_DataSize(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


class MARTE_Library_BasicNFP_Types_NFP_Frequency(NFP_Real):

    def __init__(self, unit: str, precision: str):
        self.unit = unit
        self.precision = precision
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


class NFP_Integer:

    pass
class MARTE_Library_GRM_BasicTypes_FixedPriorityParameters:

    pass
class PeriodicServerParameters:

    pass
class PoolingParameters:

    pass
class NFP_Duration:

    pass
class MARTE_Library_GRM_BasicTypes_EDF_Parameters:

    pass
class FixedPriorityParameters:

    pass
class MARTE_Library_GRM_BasicTypes_PeriodicServerParameters(FixedPriorityParameters):

    def __init__(self, kind: str, backgroundPriority: str, MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20: "NFP_Integer" = None, MARTE_Library_GRM_BasicTypes_PeriodicServerParameters: "NFP_Duration" = None, MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17: "NFP_Duration" = None, FixedPriorityParameters: "MARTE_Library_GRM_BasicTypes_SchedParameters" = None):
        self.kind = kind
        self.backgroundPriority = backgroundPriority
        self.MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20 = MARTE_Library_GRM_BasicTypes_PeriodicServerParameters20
        self.MARTE_Library_GRM_BasicTypes_PeriodicServerParameters = MARTE_Library_GRM_BasicTypes_PeriodicServerParameters
        self.MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17 = MARTE_Library_GRM_BasicTypes_PeriodicServerParameters17
        
        pass
    @property
    def backgroundPriority(self):
        return self.__backgroundPriority

    @backgroundPriority.setter
    def backgroundPriority(self, backgroundPriority: str):
        self.__backgroundPriority = backgroundPriority


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


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

class MARTE_Library_GRM_BasicTypes_PoolingParameters(FixedPriorityParameters):

    pass
class EDF_Parameters:

    pass
class MARTE_Library_GRM_BasicTypes_SchedParameters:

    def __init__(self, tableEntry: str, MARTE_Library_GRM_BasicTypes_SchedParameters: "EDF_Parameters" = None, MARTE_Library_GRM_BasicTypes_SchedParameters3: "FixedPriorityParameters" = None, MARTE_Library_GRM_BasicTypes_SchedParameters5: "PoolingParameters" = None, MARTE_Library_GRM_BasicTypes_SchedParameters7: "PeriodicServerParameters" = None):
        self.tableEntry = tableEntry
        self.MARTE_Library_GRM_BasicTypes_SchedParameters = MARTE_Library_GRM_BasicTypes_SchedParameters
        self.MARTE_Library_GRM_BasicTypes_SchedParameters3 = MARTE_Library_GRM_BasicTypes_SchedParameters3
        self.MARTE_Library_GRM_BasicTypes_SchedParameters5 = MARTE_Library_GRM_BasicTypes_SchedParameters5
        self.MARTE_Library_GRM_BasicTypes_SchedParameters7 = MARTE_Library_GRM_BasicTypes_SchedParameters7
        
        pass
    @property
    def tableEntry(self):
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
