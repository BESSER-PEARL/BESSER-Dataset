from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class QuantifierType(Enum):
    ANY = "ANY"
    ALL = "ALL"
    SOME = "SOME"
class SecurityLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
class UnitDimensionType(Enum):
    TIME_INTERVAL = "TIME_INTERVAL"
    STORAGE = "STORAGE"
    COST = "COST"
    THROUGHPUT = "THROUGHPUT"
    REQUEST_NUM = "REQUEST_NUM"
    TRANSACTION_NUM = "TRANSACTION_NUM"
    DIMENSIONLESS = "DIMENSIONLESS"
    CORE_NUM = "CORE_NUM"
class StatusType(Enum):
    WARNING = "WARNING"
    SUCCESS = "SUCCESS"
    FATAL = "FATAL"
    CRITICAL = "CRITICAL"
class ComparisonOperatorType(Enum):
    GREATER_THAN = "GREATER_THAN"
    GREATER_EQUAL_THAN = "GREATER_EQUAL_THAN"
    LESS_THAN = "LESS_THAN"
    LESS_EQUAL_THAN = "LESS_EQUAL_THAN"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
class WindowType(Enum):
    FIXED = "FIXED"
    SLIDING = "SLIDING"
class CommunicationType(Enum):
    ANY = "ANY"
    LOCAL = "LOCAL"
    REMOTE = "REMOTE"
class OptimisationFunctionType(Enum):
    MINIMISE = "MINIMISE"
    MAXIMISE = "MAXIMISE"
class TypeEnum(Enum):
    IntType = "IntType"
    StringType = "StringType"
    BooleanType = "BooleanType"
    FloatType = "FloatType"
    DoubleType = "DoubleType"
class MetricFunctionArityType(Enum):
    UNARY = "UNARY"
    BINARY = "BINARY"
    N_ARY = "N_ARY"
class FunctionPatternType(Enum):
    MAP = "MAP"
    REDUCE = "REDUCE"
class ResourcePattern(Enum):
    EXACT = "EXACT"
    TREE = "TREE"
class Operator(Enum):
    select = "select"
    add = "add"
    remove = "remove"
    multiply = "multiply"
    divide = "divide"
class ScheduleType(Enum):
    FIXED_RATE = "FIXED_RATE"
    FIXED_DELAY = "FIXED_DELAY"
    SINGLE_EVENT = "SINGLE_EVENT"
class BinaryPatternOperatorType(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"
    PRECEDES = "PRECEDES"
    REPEAT_UNTIL = "REPEAT_UNTIL"
class LayerType(Enum):
    SaaS = "SaaS"
    PaaS = "PaaS"
    IaaS = "IaaS"
    BPM = "BPM"
    SCC = "SCC"
class UnaryPatternOperatorType(Enum):
    EVERY = "EVERY"
    NOT = "NOT"
    REPEAT = "REPEAT"
    WHEN = "WHEN"
class TimerType(Enum):
    WITHIN = "WITHIN"
    WITHIN_MAX = "WITHIN_MAX"
    INTERVAL = "INTERVAL"
class PropertyType(Enum):
    ABSTRACT = "ABSTRACT"
    MEASURABLE = "MEASURABLE"
class ActionType(Enum):
    EVENT_CREATION = "EVENT_CREATION"
    SCALE_IN = "SCALE_IN"
    SCALE_OUT = "SCALE_OUT"
    SCALE_UP = "SCALE_UP"
    SCALE_DOWN = "SCALE_DOWN"
    READ = "READ"
    WRITE = "WRITE"
class UnitType(Enum):
    KILOBYTES = "KILOBYTES"
    MEGABYTES = "MEGABYTES"
    GIGABYTES = "GIGABYTES"
    MILLISECONDS = "MILLISECONDS"
    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"
    WEEKS = "WEEKS"
    MONTHS = "MONTHS"
    REQUESTS = "REQUESTS"
    REQUESTS_PER_SECOND = "REQUESTS_PER_SECOND"
    TRANSACTIONS = "TRANSACTIONS"
    TRANSACTIONS_PER_SECOND = "TRANSACTIONS_PER_SECOND"
    CORES = "CORES"
    PERCENTAGE = "PERCENTAGE"
    EUROS = "EUROS"
    POUNDS = "POUNDS"
    DOLLARS = "DOLLARS"
    BYTES = "BYTES"
    BYTES_PER_SECOND = "BYTES_PER_SECOND"
class WindowSizeType(Enum):
    MEASUREMENTS_ONLY = "MEASUREMENTS_ONLY"
    TIME_ONLY = "TIME_ONLY"
    FIRST_MATCH = "FIRST_MATCH"
    BOTH_MATCH = "BOTH_MATCH"
class MetricFunctionType(Enum):
    MEDIAN = "MEDIAN"
    PLUS = "PLUS"
    MINUS = "MINUS"
    TIMES = "TIMES"
    DIV = "DIV"
    MODULO = "MODULO"
    MEAN = "MEAN"
    STD = "STD"
    COUNT = "COUNT"
    MIN = "MIN"
    MAX = "MAX"
    PERCENTILE = "PERCENTILE"
    DERIVATIVE = "DERIVATIVE"
    MODE = "MODE"
class RequirementOperatorType(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"


############################################
# Definition of Classes
############################################

class Limit:

    pass
class camel_unit_Unit(ABC):

    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def checkUnit(self) -> bool:
        # TODO: Implement checkUnit method
        pass

class Range:

    pass
class camel_type_ValueType(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class EnumerateValue:

    pass
class CompositeMetricInstance:

    pass
class camel_security_CompositeSecurityMetricInstance(CompositeMetricInstance):

    pass
class CompositeMetric:

    pass
class camel_security_CompositeSecurityMetric(CompositeMetric):

    pass
class camel_type_SingleValue(ABC):

    def __init__(self):
        
    def valueEquals(self, v: str) -> bool:
        # TODO: Implement valueEquals method
        pass

class NumericValue:

    pass
class camel_type_FloatsValue(NumericValue):

    def __init__(self, value: float, NumericValue528: "camel_type_ValueToIncrease", NumericValue: "camel_type_Limit"):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class camel_type_PositiveInf(NumericValue):

    pass
class camel_type_DoublePrecisionValue(NumericValue):

    def __init__(self, value: float, NumericValue528: "camel_type_ValueToIncrease", NumericValue: "camel_type_Limit"):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class camel_type_ValueToIncrease(NumericValue):

    pass
class camel_type_IntegerValue(NumericValue):

    def __init__(self, value: int, NumericValue528: "camel_type_ValueToIncrease", NumericValue: "camel_type_Limit"):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class camel_type_NegativeInf(NumericValue):

    pass
class camel_type_Limit:

    def __init__(self, included: bool, camel_type_Limit: "NumericValue" = None):
        self.included = included
        self.camel_type_Limit = camel_type_Limit
        
    @property
    def included(self) -> bool:
        return self.__included

    @included.setter
    def included(self, included: bool):
        self.__included = included

    @property
    def camel_type_Limit(self):
        return self.__camel_type_Limit

    @camel_type_Limit.setter
    def camel_type_Limit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_type_Limit__camel_type_Limit", None)
        self.__camel_type_Limit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NumericValue"):
                opp_val = getattr(old_value, "NumericValue", None)
                if opp_val == self:
                    setattr(old_value, "NumericValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NumericValue"):
                opp_val = getattr(value, "NumericValue", None)
                setattr(value, "NumericValue", self)

class camel_security_SecurityControl:

    def __init__(self, name: str, specification: str, camel_security_SecurityControl506: set["SecurityProperty"] = None, camel_security_SecurityControl509: set["RawSecurityMetric"] = None, camel_security_SecurityControl512: set["CompositeSecurityMetric"] = None, camel_security_SecurityControl: "SecurityDomain" = None, camel_security_SecurityControl503: "SecurityDomain" = None):
        self.name = name
        self.specification = specification
        self.camel_security_SecurityControl506 = camel_security_SecurityControl506 if camel_security_SecurityControl506 is not None else set()
        self.camel_security_SecurityControl509 = camel_security_SecurityControl509 if camel_security_SecurityControl509 is not None else set()
        self.camel_security_SecurityControl512 = camel_security_SecurityControl512 if camel_security_SecurityControl512 is not None else set()
        self.camel_security_SecurityControl = camel_security_SecurityControl
        self.camel_security_SecurityControl503 = camel_security_SecurityControl503
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

    @property
    def camel_security_SecurityControl503(self):
        return self.__camel_security_SecurityControl503

    @camel_security_SecurityControl503.setter
    def camel_security_SecurityControl503(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_security_SecurityControl__camel_security_SecurityControl503", None)
        self.__camel_security_SecurityControl503 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecurityDomain504"):
                opp_val = getattr(old_value, "SecurityDomain504", None)
                if opp_val == self:
                    setattr(old_value, "SecurityDomain504", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecurityDomain504"):
                opp_val = getattr(value, "SecurityDomain504", None)
                setattr(value, "SecurityDomain504", self)

    @property
    def camel_security_SecurityControl512(self):
        return self.__camel_security_SecurityControl512

    @camel_security_SecurityControl512.setter
    def camel_security_SecurityControl512(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_security_SecurityControl__camel_security_SecurityControl512", None)
        self.__camel_security_SecurityControl512 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompositeSecurityMetric513"):
                    opp_val = getattr(item, "CompositeSecurityMetric513", None)
                    
                    if opp_val == self:
                        setattr(item, "CompositeSecurityMetric513", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompositeSecurityMetric513"):
                    opp_val = getattr(item, "CompositeSecurityMetric513", None)
                    
                    setattr(item, "CompositeSecurityMetric513", self)
                    

    @property
    def camel_security_SecurityControl506(self):
        return self.__camel_security_SecurityControl506

    @camel_security_SecurityControl506.setter
    def camel_security_SecurityControl506(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_security_SecurityControl__camel_security_SecurityControl506", None)
        self.__camel_security_SecurityControl506 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecurityProperty507"):
                    opp_val = getattr(item, "SecurityProperty507", None)
                    
                    if opp_val == self:
                        setattr(item, "SecurityProperty507", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecurityProperty507"):
                    opp_val = getattr(item, "SecurityProperty507", None)
                    
                    setattr(item, "SecurityProperty507", self)
                    

    @property
    def camel_security_SecurityControl(self):
        return self.__camel_security_SecurityControl

    @camel_security_SecurityControl.setter
    def camel_security_SecurityControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_security_SecurityControl__camel_security_SecurityControl", None)
        self.__camel_security_SecurityControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecurityDomain501"):
                opp_val = getattr(old_value, "SecurityDomain501", None)
                if opp_val == self:
                    setattr(old_value, "SecurityDomain501", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecurityDomain501"):
                opp_val = getattr(value, "SecurityDomain501", None)
                setattr(value, "SecurityDomain501", self)

    @property
    def camel_security_SecurityControl509(self):
        return self.__camel_security_SecurityControl509

    @camel_security_SecurityControl509.setter
    def camel_security_SecurityControl509(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_security_SecurityControl__camel_security_SecurityControl509", None)
        self.__camel_security_SecurityControl509 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RawSecurityMetric510"):
                    opp_val = getattr(item, "RawSecurityMetric510", None)
                    
                    if opp_val == self:
                        setattr(item, "RawSecurityMetric510", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RawSecurityMetric510"):
                    opp_val = getattr(item, "RawSecurityMetric510", None)
                    
                    setattr(item, "RawSecurityMetric510", self)
                    

class camel_security_SecurityCapability:

    def __init__(self, name: str, camel_security_SecurityCapability: set["SecurityControl"] = None, camel_security_SecurityCapability519: "DataCenter" = None):
        self.name = name
        self.camel_security_SecurityCapability = camel_security_SecurityCapability if camel_security_SecurityCapability is not None else set()
        self.camel_security_SecurityCapability519 = camel_security_SecurityCapability519
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_security_SecurityCapability(self):
        return self.__camel_security_SecurityCapability

    @camel_security_SecurityCapability.setter
    def camel_security_SecurityCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_security_SecurityCapability__camel_security_SecurityCapability", None)
        self.__camel_security_SecurityCapability = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecurityControl517"):
                    opp_val = getattr(item, "SecurityControl517", None)
                    
                    if opp_val == self:
                        setattr(item, "SecurityControl517", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecurityControl517"):
                    opp_val = getattr(item, "SecurityControl517", None)
                    
                    setattr(item, "SecurityControl517", self)
                    

    @property
    def camel_security_SecurityCapability519(self):
        return self.__camel_security_SecurityCapability519

    @camel_security_SecurityCapability519.setter
    def camel_security_SecurityCapability519(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_security_SecurityCapability__camel_security_SecurityCapability519", None)
        self.__camel_security_SecurityCapability519 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataCenter520"):
                opp_val = getattr(old_value, "DataCenter520", None)
                if opp_val == self:
                    setattr(old_value, "DataCenter520", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataCenter520"):
                opp_val = getattr(value, "DataCenter520", None)
                setattr(value, "DataCenter520", self)

class RawMetric:

    pass
class camel_security_RawSecurityMetric(RawMetric):

    pass
class RawMetricInstance:

    pass
class camel_security_RawSecurityMetricInstance(RawMetricInstance):

    pass
class RawSecurityMetricInstance:

    pass
class CompositeSecurityMetric:

    pass
class camel_security_SecurityDomain:

    def __init__(self, id: str, name: str, camel_security_SecurityDomain: set["SecurityDomain"] = None):
        self.id = id
        self.name = name
        self.camel_security_SecurityDomain = camel_security_SecurityDomain if camel_security_SecurityDomain is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_security_SecurityDomain(self):
        return self.__camel_security_SecurityDomain

    @camel_security_SecurityDomain.setter
    def camel_security_SecurityDomain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_security_SecurityDomain__camel_security_SecurityDomain", None)
        self.__camel_security_SecurityDomain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecurityDomain499"):
                    opp_val = getattr(item, "SecurityDomain499", None)
                    
                    if opp_val == self:
                        setattr(item, "SecurityDomain499", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecurityDomain499"):
                    opp_val = getattr(item, "SecurityDomain499", None)
                    
                    setattr(item, "SecurityDomain499", self)
                    

class SecuritySLO:

    pass
class SecurityDomain:

    pass
class CompositeSecurityMetricInstance:

    pass
class RawSecurityMetric:

    pass
class SecurityProperty:

    pass
class camel_security_Certifiable(SecurityProperty):

    pass
class SecurityRequirement:

    pass
class camel_scalability_Timer:

    def __init__(self, name: str, type: str, timeValue: int, maxOccurrenceNum: int, camel_scalability_Timer: "TimeIntervalUnit" = None):
        self.name = name
        self.type = type
        self.timeValue = timeValue
        self.maxOccurrenceNum = maxOccurrenceNum
        self.camel_scalability_Timer = camel_scalability_Timer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def timeValue(self) -> int:
        return self.__timeValue

    @timeValue.setter
    def timeValue(self, timeValue: int):
        self.__timeValue = timeValue

    @property
    def maxOccurrenceNum(self) -> int:
        return self.__maxOccurrenceNum

    @maxOccurrenceNum.setter
    def maxOccurrenceNum(self, maxOccurrenceNum: int):
        self.__maxOccurrenceNum = maxOccurrenceNum

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def camel_scalability_Timer(self):
        return self.__camel_scalability_Timer

    @camel_scalability_Timer.setter
    def camel_scalability_Timer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_Timer__camel_scalability_Timer", None)
        self.__camel_scalability_Timer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TimeIntervalUnit476"):
                opp_val = getattr(old_value, "TimeIntervalUnit476", None)
                if opp_val == self:
                    setattr(old_value, "TimeIntervalUnit476", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TimeIntervalUnit476"):
                opp_val = getattr(value, "TimeIntervalUnit476", None)
                setattr(value, "TimeIntervalUnit476", self)

class camel_scalability_ScalabilityRule:

    def __init__(self, name: str, camel_scalability_ScalabilityRule: "Event" = None, camel_scalability_ScalabilityRule464: set["scalability_camel_Action"] = None, camel_scalability_ScalabilityRule466: set["Entity"] = None, camel_scalability_ScalabilityRule469: set["ScaleRequirement"] = None):
        self.name = name
        self.camel_scalability_ScalabilityRule = camel_scalability_ScalabilityRule
        self.camel_scalability_ScalabilityRule464 = camel_scalability_ScalabilityRule464 if camel_scalability_ScalabilityRule464 is not None else set()
        self.camel_scalability_ScalabilityRule466 = camel_scalability_ScalabilityRule466 if camel_scalability_ScalabilityRule466 is not None else set()
        self.camel_scalability_ScalabilityRule469 = camel_scalability_ScalabilityRule469 if camel_scalability_ScalabilityRule469 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_scalability_ScalabilityRule464(self):
        return self.__camel_scalability_ScalabilityRule464

    @camel_scalability_ScalabilityRule464.setter
    def camel_scalability_ScalabilityRule464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_ScalabilityRule__camel_scalability_ScalabilityRule464", None)
        self.__camel_scalability_ScalabilityRule464 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scalability_camel_Action"):
                    opp_val = getattr(item, "scalability_camel_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "scalability_camel_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scalability_camel_Action"):
                    opp_val = getattr(item, "scalability_camel_Action", None)
                    
                    setattr(item, "scalability_camel_Action", self)
                    

    @property
    def camel_scalability_ScalabilityRule469(self):
        return self.__camel_scalability_ScalabilityRule469

    @camel_scalability_ScalabilityRule469.setter
    def camel_scalability_ScalabilityRule469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_ScalabilityRule__camel_scalability_ScalabilityRule469", None)
        self.__camel_scalability_ScalabilityRule469 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ScaleRequirement470"):
                    opp_val = getattr(item, "ScaleRequirement470", None)
                    
                    if opp_val == self:
                        setattr(item, "ScaleRequirement470", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ScaleRequirement470"):
                    opp_val = getattr(item, "ScaleRequirement470", None)
                    
                    setattr(item, "ScaleRequirement470", self)
                    

    @property
    def camel_scalability_ScalabilityRule466(self):
        return self.__camel_scalability_ScalabilityRule466

    @camel_scalability_ScalabilityRule466.setter
    def camel_scalability_ScalabilityRule466(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_ScalabilityRule__camel_scalability_ScalabilityRule466", None)
        self.__camel_scalability_ScalabilityRule466 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Entity467"):
                    opp_val = getattr(item, "Entity467", None)
                    
                    if opp_val == self:
                        setattr(item, "Entity467", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Entity467"):
                    opp_val = getattr(item, "Entity467", None)
                    
                    setattr(item, "Entity467", self)
                    

    @property
    def camel_scalability_ScalabilityRule(self):
        return self.__camel_scalability_ScalabilityRule

    @camel_scalability_ScalabilityRule.setter
    def camel_scalability_ScalabilityRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_ScalabilityRule__camel_scalability_ScalabilityRule", None)
        self.__camel_scalability_ScalabilityRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Event462"):
                opp_val = getattr(old_value, "Event462", None)
                if opp_val == self:
                    setattr(old_value, "Event462", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Event462"):
                opp_val = getattr(value, "Event462", None)
                setattr(value, "Event462", self)

class Action:

    pass
class camel_scalability_ScalingAction(Action):

    pass
class scalability_camel_Action:

    pass
class SimpleEvent:

    pass
class camel_scalability_NonFunctionalEvent(SimpleEvent):

    def __init__(self, isViolation: bool, camel_scalability_NonFunctionalEvent: "MetricCondition" = None, SimpleEvent: "camel_scalability_EventInstance"):
        self.isViolation = isViolation
        self.camel_scalability_NonFunctionalEvent = camel_scalability_NonFunctionalEvent
        
    @property
    def isViolation(self) -> bool:
        return self.__isViolation

    @isViolation.setter
    def isViolation(self, isViolation: bool):
        self.__isViolation = isViolation

    @property
    def camel_scalability_NonFunctionalEvent(self):
        return self.__camel_scalability_NonFunctionalEvent

    @camel_scalability_NonFunctionalEvent.setter
    def camel_scalability_NonFunctionalEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_NonFunctionalEvent__camel_scalability_NonFunctionalEvent", None)
        self.__camel_scalability_NonFunctionalEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetricCondition"):
                opp_val = getattr(old_value, "MetricCondition", None)
                if opp_val == self:
                    setattr(old_value, "MetricCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetricCondition"):
                opp_val = getattr(value, "MetricCondition", None)
                setattr(value, "MetricCondition", self)

class camel_scalability_FunctionalEvent(SimpleEvent):

    def __init__(self, functionalType: str, SimpleEvent: "camel_scalability_EventInstance"):
        self.functionalType = functionalType
        
    @property
    def functionalType(self) -> str:
        return self.__functionalType

    @functionalType.setter
    def functionalType(self, functionalType: str):
        self.__functionalType = functionalType

class camel_scalability_EventInstance:

    def __init__(self, name: str, status: str, layer: str, camel_scalability_EventInstance: "SimpleEvent" = None, camel_scalability_EventInstance459: "MetricInstance" = None):
        self.name = name
        self.status = status
        self.layer = layer
        self.camel_scalability_EventInstance = camel_scalability_EventInstance
        self.camel_scalability_EventInstance459 = camel_scalability_EventInstance459
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def layer(self) -> str:
        return self.__layer

    @layer.setter
    def layer(self, layer: str):
        self.__layer = layer

    @property
    def camel_scalability_EventInstance459(self):
        return self.__camel_scalability_EventInstance459

    @camel_scalability_EventInstance459.setter
    def camel_scalability_EventInstance459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_EventInstance__camel_scalability_EventInstance459", None)
        self.__camel_scalability_EventInstance459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetricInstance460"):
                opp_val = getattr(old_value, "MetricInstance460", None)
                if opp_val == self:
                    setattr(old_value, "MetricInstance460", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetricInstance460"):
                opp_val = getattr(value, "MetricInstance460", None)
                setattr(value, "MetricInstance460", self)

    @property
    def camel_scalability_EventInstance(self):
        return self.__camel_scalability_EventInstance

    @camel_scalability_EventInstance.setter
    def camel_scalability_EventInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_EventInstance__camel_scalability_EventInstance", None)
        self.__camel_scalability_EventInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleEvent"):
                opp_val = getattr(old_value, "SimpleEvent", None)
                if opp_val == self:
                    setattr(old_value, "SimpleEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleEvent"):
                opp_val = getattr(value, "SimpleEvent", None)
                setattr(value, "SimpleEvent", self)

    def equalLayer(self, l1: str, l2: str) -> bool:
        # TODO: Implement equalLayer method
        pass

class MetricCondition:

    pass
class Timer:

    pass
class EventPattern:

    pass
class camel_scalability_UnaryEventPattern(EventPattern):

    def __init__(self, occurrenceNum: int, operator: str, camel_scalability_UnaryEventPattern: "Event" = None, EventPattern: "camel_scalability_ScalabilityModel"):
        self.occurrenceNum = occurrenceNum
        self.operator = operator
        self.camel_scalability_UnaryEventPattern = camel_scalability_UnaryEventPattern
        
    @property
    def occurrenceNum(self) -> int:
        return self.__occurrenceNum

    @occurrenceNum.setter
    def occurrenceNum(self, occurrenceNum: int):
        self.__occurrenceNum = occurrenceNum

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def camel_scalability_UnaryEventPattern(self):
        return self.__camel_scalability_UnaryEventPattern

    @camel_scalability_UnaryEventPattern.setter
    def camel_scalability_UnaryEventPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_UnaryEventPattern__camel_scalability_UnaryEventPattern", None)
        self.__camel_scalability_UnaryEventPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Event455"):
                opp_val = getattr(old_value, "Event455", None)
                if opp_val == self:
                    setattr(old_value, "Event455", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Event455"):
                opp_val = getattr(value, "Event455", None)
                setattr(value, "Event455", self)

class camel_scalability_BinaryEventPattern(EventPattern):

    def __init__(self, lowerOccurrenceBound: int, upperOccurrenceBound: int, operator: str, camel_scalability_BinaryEventPattern: "Event" = None, camel_scalability_BinaryEventPattern452: "Event" = None, EventPattern: "camel_scalability_ScalabilityModel"):
        self.lowerOccurrenceBound = lowerOccurrenceBound
        self.upperOccurrenceBound = upperOccurrenceBound
        self.operator = operator
        self.camel_scalability_BinaryEventPattern = camel_scalability_BinaryEventPattern
        self.camel_scalability_BinaryEventPattern452 = camel_scalability_BinaryEventPattern452
        
    @property
    def lowerOccurrenceBound(self) -> int:
        return self.__lowerOccurrenceBound

    @lowerOccurrenceBound.setter
    def lowerOccurrenceBound(self, lowerOccurrenceBound: int):
        self.__lowerOccurrenceBound = lowerOccurrenceBound

    @property
    def upperOccurrenceBound(self) -> int:
        return self.__upperOccurrenceBound

    @upperOccurrenceBound.setter
    def upperOccurrenceBound(self, upperOccurrenceBound: int):
        self.__upperOccurrenceBound = upperOccurrenceBound

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def camel_scalability_BinaryEventPattern(self):
        return self.__camel_scalability_BinaryEventPattern

    @camel_scalability_BinaryEventPattern.setter
    def camel_scalability_BinaryEventPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_BinaryEventPattern__camel_scalability_BinaryEventPattern", None)
        self.__camel_scalability_BinaryEventPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Event450"):
                opp_val = getattr(old_value, "Event450", None)
                if opp_val == self:
                    setattr(old_value, "Event450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Event450"):
                opp_val = getattr(value, "Event450", None)
                setattr(value, "Event450", self)

    @property
    def camel_scalability_BinaryEventPattern452(self):
        return self.__camel_scalability_BinaryEventPattern452

    @camel_scalability_BinaryEventPattern452.setter
    def camel_scalability_BinaryEventPattern452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_BinaryEventPattern__camel_scalability_BinaryEventPattern452", None)
        self.__camel_scalability_BinaryEventPattern452 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Event453"):
                opp_val = getattr(old_value, "Event453", None)
                if opp_val == self:
                    setattr(old_value, "Event453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Event453"):
                opp_val = getattr(value, "Event453", None)
                setattr(value, "Event453", self)

class camel_scalability_Event:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ScalingAction:

    pass
class camel_scalability_VerticalScalingAction(ScalingAction):

    def __init__(self, memoryUpdate: int, CPUUpdate: float, coreUpdate: int, storageUpdate: int, ioUpdate: int, networkUpdate: int, ScalingAction: "camel_scalability_ScalabilityModel"):
        self.memoryUpdate = memoryUpdate
        self.CPUUpdate = CPUUpdate
        self.coreUpdate = coreUpdate
        self.storageUpdate = storageUpdate
        self.ioUpdate = ioUpdate
        self.networkUpdate = networkUpdate
        
    @property
    def ioUpdate(self) -> int:
        return self.__ioUpdate

    @ioUpdate.setter
    def ioUpdate(self, ioUpdate: int):
        self.__ioUpdate = ioUpdate

    @property
    def networkUpdate(self) -> int:
        return self.__networkUpdate

    @networkUpdate.setter
    def networkUpdate(self, networkUpdate: int):
        self.__networkUpdate = networkUpdate

    @property
    def memoryUpdate(self) -> int:
        return self.__memoryUpdate

    @memoryUpdate.setter
    def memoryUpdate(self, memoryUpdate: int):
        self.__memoryUpdate = memoryUpdate

    @property
    def coreUpdate(self) -> int:
        return self.__coreUpdate

    @coreUpdate.setter
    def coreUpdate(self, coreUpdate: int):
        self.__coreUpdate = coreUpdate

    @property
    def storageUpdate(self) -> int:
        return self.__storageUpdate

    @storageUpdate.setter
    def storageUpdate(self, storageUpdate: int):
        self.__storageUpdate = storageUpdate

    @property
    def CPUUpdate(self) -> float:
        return self.__CPUUpdate

    @CPUUpdate.setter
    def CPUUpdate(self, CPUUpdate: float):
        self.__CPUUpdate = CPUUpdate

class camel_scalability_HorizontalScalingAction(ScalingAction):

    def __init__(self, count: int, camel_scalability_HorizontalScalingAction: "InternalComponent" = None, ScalingAction: "camel_scalability_ScalabilityModel"):
        self.count = count
        self.camel_scalability_HorizontalScalingAction = camel_scalability_HorizontalScalingAction
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def camel_scalability_HorizontalScalingAction(self):
        return self.__camel_scalability_HorizontalScalingAction

    @camel_scalability_HorizontalScalingAction.setter
    def camel_scalability_HorizontalScalingAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_HorizontalScalingAction__camel_scalability_HorizontalScalingAction", None)
        self.__camel_scalability_HorizontalScalingAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InternalComponent474"):
                opp_val = getattr(old_value, "InternalComponent474", None)
                if opp_val == self:
                    setattr(old_value, "InternalComponent474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InternalComponent474"):
                opp_val = getattr(value, "InternalComponent474", None)
                setattr(value, "InternalComponent474", self)

class Event:

    pass
class camel_scalability_SimpleEvent(Event):

    pass
class camel_scalability_EventPattern(Event):

    def __init__(self, camel_scalability_EventPattern: "Timer" = None, Event462: "camel_scalability_ScalabilityRule", Event: "camel_scalability_ScalabilityModel", Event455: "camel_scalability_UnaryEventPattern", Event453: "camel_scalability_BinaryEventPattern", Event450: "camel_scalability_BinaryEventPattern"):
        self.camel_scalability_EventPattern = camel_scalability_EventPattern
        
    @property
    def camel_scalability_EventPattern(self):
        return self.__camel_scalability_EventPattern

    @camel_scalability_EventPattern.setter
    def camel_scalability_EventPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_scalability_EventPattern__camel_scalability_EventPattern", None)
        self.__camel_scalability_EventPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Timer448"):
                opp_val = getattr(old_value, "Timer448", None)
                if opp_val == self:
                    setattr(old_value, "Timer448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Timer448"):
                opp_val = getattr(value, "Timer448", None)
                setattr(value, "Timer448", self)

    def includesRightEvent(self, e: str) -> bool:
        # TODO: Implement includesRightEvent method
        pass

    def includesLeftEvent(self, e: str) -> bool:
        # TODO: Implement includesLeftEvent method
        pass

    def includesEvent(self, e: str) -> bool:
        # TODO: Implement includesEvent method
        pass

class ScaleRequirement:

    pass
class camel_requirement_VerticalScaleRequirement(ScaleRequirement):

    def __init__(self, minCPU: float, maxCPU: float, minCores: int, maxCores: int, minRAM: int, maxRAM: int, minStorage: int, maxStorage: int, camel_requirement_VerticalScaleRequirement: "VM" = None, ScaleRequirement470: "camel_scalability_ScalabilityRule", ScaleRequirement: "camel_scalability_ScalabilityModel"):
        self.minCPU = minCPU
        self.maxCPU = maxCPU
        self.minCores = minCores
        self.maxCores = maxCores
        self.minRAM = minRAM
        self.maxRAM = maxRAM
        self.minStorage = minStorage
        self.maxStorage = maxStorage
        self.camel_requirement_VerticalScaleRequirement = camel_requirement_VerticalScaleRequirement
        
    @property
    def minStorage(self) -> int:
        return self.__minStorage

    @minStorage.setter
    def minStorage(self, minStorage: int):
        self.__minStorage = minStorage

    @property
    def minRAM(self) -> int:
        return self.__minRAM

    @minRAM.setter
    def minRAM(self, minRAM: int):
        self.__minRAM = minRAM

    @property
    def maxRAM(self) -> int:
        return self.__maxRAM

    @maxRAM.setter
    def maxRAM(self, maxRAM: int):
        self.__maxRAM = maxRAM

    @property
    def maxCores(self) -> int:
        return self.__maxCores

    @maxCores.setter
    def maxCores(self, maxCores: int):
        self.__maxCores = maxCores

    @property
    def maxCPU(self) -> float:
        return self.__maxCPU

    @maxCPU.setter
    def maxCPU(self, maxCPU: float):
        self.__maxCPU = maxCPU

    @property
    def maxStorage(self) -> int:
        return self.__maxStorage

    @maxStorage.setter
    def maxStorage(self, maxStorage: int):
        self.__maxStorage = maxStorage

    @property
    def minCores(self) -> int:
        return self.__minCores

    @minCores.setter
    def minCores(self, minCores: int):
        self.__minCores = minCores

    @property
    def minCPU(self) -> float:
        return self.__minCPU

    @minCPU.setter
    def minCPU(self, minCPU: float):
        self.__minCPU = minCPU

    @property
    def camel_requirement_VerticalScaleRequirement(self):
        return self.__camel_requirement_VerticalScaleRequirement

    @camel_requirement_VerticalScaleRequirement.setter
    def camel_requirement_VerticalScaleRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_requirement_VerticalScaleRequirement__camel_requirement_VerticalScaleRequirement", None)
        self.__camel_requirement_VerticalScaleRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VM431"):
                opp_val = getattr(old_value, "VM431", None)
                if opp_val == self:
                    setattr(old_value, "VM431", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VM431"):
                opp_val = getattr(value, "VM431", None)
                setattr(value, "VM431", self)

class camel_requirement_HorizontalScaleRequirement(ScaleRequirement):

    def __init__(self, minInstances: int, maxInstances: int, camel_requirement_HorizontalScaleRequirement: "InternalComponent" = None, ScaleRequirement470: "camel_scalability_ScalabilityRule", ScaleRequirement: "camel_scalability_ScalabilityModel"):
        self.minInstances = minInstances
        self.maxInstances = maxInstances
        self.camel_requirement_HorizontalScaleRequirement = camel_requirement_HorizontalScaleRequirement
        
    @property
    def maxInstances(self) -> int:
        return self.__maxInstances

    @maxInstances.setter
    def maxInstances(self, maxInstances: int):
        self.__maxInstances = maxInstances

    @property
    def minInstances(self) -> int:
        return self.__minInstances

    @minInstances.setter
    def minInstances(self, minInstances: int):
        self.__minInstances = minInstances

    @property
    def camel_requirement_HorizontalScaleRequirement(self):
        return self.__camel_requirement_HorizontalScaleRequirement

    @camel_requirement_HorizontalScaleRequirement.setter
    def camel_requirement_HorizontalScaleRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_requirement_HorizontalScaleRequirement__camel_requirement_HorizontalScaleRequirement", None)
        self.__camel_requirement_HorizontalScaleRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InternalComponent429"):
                opp_val = getattr(old_value, "InternalComponent429", None)
                if opp_val == self:
                    setattr(old_value, "InternalComponent429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InternalComponent429"):
                opp_val = getattr(value, "InternalComponent429", None)
                setattr(value, "InternalComponent429", self)

class SecurityControl:

    pass
class HardwareRequirement:

    pass
class camel_requirement_QuantitativeHardwareRequirement(HardwareRequirement):

    def __init__(self, minRAM: int, maxRAM: int, minStorage: int, maxStorage: int, minCPU: float, maxCPU: float, minCores: int, maxCores: int):
        self.minRAM = minRAM
        self.maxRAM = maxRAM
        self.minStorage = minStorage
        self.maxStorage = maxStorage
        self.minCPU = minCPU
        self.maxCPU = maxCPU
        self.minCores = minCores
        self.maxCores = maxCores
        
    @property
    def minCores(self) -> int:
        return self.__minCores

    @minCores.setter
    def minCores(self, minCores: int):
        self.__minCores = minCores

    @property
    def maxRAM(self) -> int:
        return self.__maxRAM

    @maxRAM.setter
    def maxRAM(self, maxRAM: int):
        self.__maxRAM = maxRAM

    @property
    def minCPU(self) -> float:
        return self.__minCPU

    @minCPU.setter
    def minCPU(self, minCPU: float):
        self.__minCPU = minCPU

    @property
    def maxCores(self) -> int:
        return self.__maxCores

    @maxCores.setter
    def maxCores(self, maxCores: int):
        self.__maxCores = maxCores

    @property
    def maxCPU(self) -> float:
        return self.__maxCPU

    @maxCPU.setter
    def maxCPU(self, maxCPU: float):
        self.__maxCPU = maxCPU

    @property
    def minStorage(self) -> int:
        return self.__minStorage

    @minStorage.setter
    def minStorage(self, minStorage: int):
        self.__minStorage = minStorage

    @property
    def maxStorage(self) -> int:
        return self.__maxStorage

    @maxStorage.setter
    def maxStorage(self, maxStorage: int):
        self.__maxStorage = maxStorage

    @property
    def minRAM(self) -> int:
        return self.__minRAM

    @minRAM.setter
    def minRAM(self, minRAM: int):
        self.__minRAM = minRAM

class camel_requirement_QualitativeHardwareRequirement(HardwareRequirement):

    def __init__(self, minBenchmark: float, maxBenchmark: float):
        self.minBenchmark = minBenchmark
        self.maxBenchmark = maxBenchmark
        
    @property
    def maxBenchmark(self) -> float:
        return self.__maxBenchmark

    @maxBenchmark.setter
    def maxBenchmark(self, maxBenchmark: float):
        self.__maxBenchmark = maxBenchmark

    @property
    def minBenchmark(self) -> float:
        return self.__minBenchmark

    @minBenchmark.setter
    def minBenchmark(self, minBenchmark: float):
        self.__minBenchmark = minBenchmark

class SoftRequirement:

    pass
class camel_requirement_OptimisationRequirement(SoftRequirement):

    def __init__(self, optimisationFunction: str, camel_requirement_OptimisationRequirement: "Metric" = None, camel_requirement_OptimisationRequirement415: "MetricContext" = None, camel_requirement_OptimisationRequirement406: "Property" = None, camel_requirement_OptimisationRequirement409: "requirement_camel_Application" = None, camel_requirement_OptimisationRequirement412: "Component" = None):
        self.optimisationFunction = optimisationFunction
        self.camel_requirement_OptimisationRequirement = camel_requirement_OptimisationRequirement
        self.camel_requirement_OptimisationRequirement415 = camel_requirement_OptimisationRequirement415
        self.camel_requirement_OptimisationRequirement406 = camel_requirement_OptimisationRequirement406
        self.camel_requirement_OptimisationRequirement409 = camel_requirement_OptimisationRequirement409
        self.camel_requirement_OptimisationRequirement412 = camel_requirement_OptimisationRequirement412
        
    @property
    def optimisationFunction(self) -> str:
        return self.__optimisationFunction

    @optimisationFunction.setter
    def optimisationFunction(self, optimisationFunction: str):
        self.__optimisationFunction = optimisationFunction

    @property
    def camel_requirement_OptimisationRequirement412(self):
        return self.__camel_requirement_OptimisationRequirement412

    @camel_requirement_OptimisationRequirement412.setter
    def camel_requirement_OptimisationRequirement412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_requirement_OptimisationRequirement__camel_requirement_OptimisationRequirement412", None)
        self.__camel_requirement_OptimisationRequirement412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Component413"):
                opp_val = getattr(old_value, "Component413", None)
                if opp_val == self:
                    setattr(old_value, "Component413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component413"):
                opp_val = getattr(value, "Component413", None)
                setattr(value, "Component413", self)

    @property
    def camel_requirement_OptimisationRequirement406(self):
        return self.__camel_requirement_OptimisationRequirement406

    @camel_requirement_OptimisationRequirement406.setter
    def camel_requirement_OptimisationRequirement406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_requirement_OptimisationRequirement__camel_requirement_OptimisationRequirement406", None)
        self.__camel_requirement_OptimisationRequirement406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property407"):
                opp_val = getattr(old_value, "Property407", None)
                if opp_val == self:
                    setattr(old_value, "Property407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property407"):
                opp_val = getattr(value, "Property407", None)
                setattr(value, "Property407", self)

    @property
    def camel_requirement_OptimisationRequirement409(self):
        return self.__camel_requirement_OptimisationRequirement409

    @camel_requirement_OptimisationRequirement409.setter
    def camel_requirement_OptimisationRequirement409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_requirement_OptimisationRequirement__camel_requirement_OptimisationRequirement409", None)
        self.__camel_requirement_OptimisationRequirement409 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_camel_Application410"):
                opp_val = getattr(old_value, "requirement_camel_Application410", None)
                if opp_val == self:
                    setattr(old_value, "requirement_camel_Application410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_camel_Application410"):
                opp_val = getattr(value, "requirement_camel_Application410", None)
                setattr(value, "requirement_camel_Application410", self)

    @property
    def camel_requirement_OptimisationRequirement415(self):
        return self.__camel_requirement_OptimisationRequirement415

    @camel_requirement_OptimisationRequirement415.setter
    def camel_requirement_OptimisationRequirement415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_requirement_OptimisationRequirement__camel_requirement_OptimisationRequirement415", None)
        self.__camel_requirement_OptimisationRequirement415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetricContext416"):
                opp_val = getattr(old_value, "MetricContext416", None)
                if opp_val == self:
                    setattr(old_value, "MetricContext416", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetricContext416"):
                opp_val = getattr(value, "MetricContext416", None)
                setattr(value, "MetricContext416", self)

    @property
    def camel_requirement_OptimisationRequirement(self):
        return self.__camel_requirement_OptimisationRequirement

    @camel_requirement_OptimisationRequirement.setter
    def camel_requirement_OptimisationRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_requirement_OptimisationRequirement__camel_requirement_OptimisationRequirement", None)
        self.__camel_requirement_OptimisationRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Metric404"):
                opp_val = getattr(old_value, "Metric404", None)
                if opp_val == self:
                    setattr(old_value, "Metric404", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Metric404"):
                opp_val = getattr(value, "Metric404", None)
                setattr(value, "Metric404", self)

class HardRequirement:

    pass
class camel_requirement_HardwareRequirement(HardRequirement):

    pass
class camel_requirement_SecurityRequirement(HardRequirement):

    pass
class camel_requirement_LocationRequirement(HardRequirement):

    pass
class camel_requirement_OSOrImageRequirement(HardRequirement):

    pass
class camel_requirement_ProviderRequirement(HardRequirement):

    pass
class camel_requirement_ScaleRequirement(HardRequirement):

    pass
class camel_requirement_ServiceLevelObjective(HardRequirement):

    pass
class requirement_camel_Application:

    pass
class GroupCardinality:

    pass
class camel_requirement_Requirement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Requirement:

    pass
class camel_requirement_HardRequirement(Requirement):

    pass
class camel_requirement_RequirementGroup(Requirement):

    def __init__(self, requirementOperator: str, camel_requirement_RequirementGroup: set["Requirement"] = None, camel_requirement_RequirementGroup400: set["requirement_camel_Application"] = None, Requirement: "camel_requirement_RequirementModel", Requirement398: "camel_requirement_RequirementGroup"):
        self.requirementOperator = requirementOperator
        self.camel_requirement_RequirementGroup = camel_requirement_RequirementGroup if camel_requirement_RequirementGroup is not None else set()
        self.camel_requirement_RequirementGroup400 = camel_requirement_RequirementGroup400 if camel_requirement_RequirementGroup400 is not None else set()
        
    @property
    def requirementOperator(self) -> str:
        return self.__requirementOperator

    @requirementOperator.setter
    def requirementOperator(self, requirementOperator: str):
        self.__requirementOperator = requirementOperator

    @property
    def camel_requirement_RequirementGroup(self):
        return self.__camel_requirement_RequirementGroup

    @camel_requirement_RequirementGroup.setter
    def camel_requirement_RequirementGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_requirement_RequirementGroup__camel_requirement_RequirementGroup", None)
        self.__camel_requirement_RequirementGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Requirement398"):
                    opp_val = getattr(item, "Requirement398", None)
                    
                    if opp_val == self:
                        setattr(item, "Requirement398", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Requirement398"):
                    opp_val = getattr(item, "Requirement398", None)
                    
                    setattr(item, "Requirement398", self)
                    

    @property
    def camel_requirement_RequirementGroup400(self):
        return self.__camel_requirement_RequirementGroup400

    @camel_requirement_RequirementGroup400.setter
    def camel_requirement_RequirementGroup400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_requirement_RequirementGroup__camel_requirement_RequirementGroup400", None)
        self.__camel_requirement_RequirementGroup400 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirement_camel_Application"):
                    opp_val = getattr(item, "requirement_camel_Application", None)
                    
                    if opp_val == self:
                        setattr(item, "requirement_camel_Application", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirement_camel_Application"):
                    opp_val = getattr(item, "requirement_camel_Application", None)
                    
                    setattr(item, "requirement_camel_Application", self)
                    

    def checkRecursiveness(self, context: str, rg1: str, r: str, resources: bool) -> bool:
        # TODO: Implement checkRecursiveness method
        pass

class camel_requirement_SoftRequirement(Requirement):

    def __init__(self, priority: float, Requirement: "camel_requirement_RequirementModel", Requirement398: "camel_requirement_RequirementGroup"):
        self.priority = priority
        
    @property
    def priority(self) -> float:
        return self.__priority

    @priority.setter
    def priority(self, priority: float):
        self.__priority = priority

class camel_provider_Scope(ABC):

    pass
class Alternative:

    pass
class camel_provider_Exclusive(Alternative):

    pass
class AttributeConstraint:

    pass
class camel_provider_Feature:

    def __init__(self, name: str, camel_provider_Feature: set["Attribute"] = None, camel_provider_Feature382: set["Feature"] = None, camel_provider_Feature385: "FeatCardinality" = None, camel_provider_Feature388: set["Clone"] = None):
        self.name = name
        self.camel_provider_Feature = camel_provider_Feature if camel_provider_Feature is not None else set()
        self.camel_provider_Feature382 = camel_provider_Feature382 if camel_provider_Feature382 is not None else set()
        self.camel_provider_Feature385 = camel_provider_Feature385
        self.camel_provider_Feature388 = camel_provider_Feature388 if camel_provider_Feature388 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_provider_Feature385(self):
        return self.__camel_provider_Feature385

    @camel_provider_Feature385.setter
    def camel_provider_Feature385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_Feature__camel_provider_Feature385", None)
        self.__camel_provider_Feature385 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatCardinality386"):
                opp_val = getattr(old_value, "FeatCardinality386", None)
                if opp_val == self:
                    setattr(old_value, "FeatCardinality386", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatCardinality386"):
                opp_val = getattr(value, "FeatCardinality386", None)
                setattr(value, "FeatCardinality386", self)

    @property
    def camel_provider_Feature(self):
        return self.__camel_provider_Feature

    @camel_provider_Feature.setter
    def camel_provider_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_Feature__camel_provider_Feature", None)
        self.__camel_provider_Feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute380"):
                    opp_val = getattr(item, "Attribute380", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute380", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute380"):
                    opp_val = getattr(item, "Attribute380", None)
                    
                    setattr(item, "Attribute380", self)
                    

    @property
    def camel_provider_Feature382(self):
        return self.__camel_provider_Feature382

    @camel_provider_Feature382.setter
    def camel_provider_Feature382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_Feature__camel_provider_Feature382", None)
        self.__camel_provider_Feature382 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature383"):
                    opp_val = getattr(item, "Feature383", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature383", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature383"):
                    opp_val = getattr(item, "Feature383", None)
                    
                    setattr(item, "Feature383", self)
                    

    @property
    def camel_provider_Feature388(self):
        return self.__camel_provider_Feature388

    @camel_provider_Feature388.setter
    def camel_provider_Feature388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_Feature__camel_provider_Feature388", None)
        self.__camel_provider_Feature388 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Clone389"):
                    opp_val = getattr(item, "Clone389", None)
                    
                    if opp_val == self:
                        setattr(item, "Clone389", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Clone389"):
                    opp_val = getattr(item, "Clone389", None)
                    
                    setattr(item, "Clone389", self)
                    

class Requires:

    pass
class camel_provider_Functional(Requires):

    def __init__(self, type: str, order: int, value: int):
        self.type = type
        self.order = order
        self.value = value
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class FeatCardinality:

    pass
class Scope:

    pass
class camel_provider_Instance(Scope):

    pass
class camel_provider_Product(Scope):

    pass
class camel_provider_Cardinality(ABC):

    def __init__(self, cardinalityMin: int, cardinalityMax: int):
        self.cardinalityMin = cardinalityMin
        self.cardinalityMax = cardinalityMax
        
    @property
    def cardinalityMin(self) -> int:
        return self.__cardinalityMin

    @cardinalityMin.setter
    def cardinalityMin(self, cardinalityMin: int):
        self.__cardinalityMin = cardinalityMin

    @property
    def cardinalityMax(self) -> int:
        return self.__cardinalityMax

    @cardinalityMax.setter
    def cardinalityMax(self, cardinalityMax: int):
        self.__cardinalityMax = cardinalityMax

class camel_provider_AttributeConstraint:

    def __init__(self, name: str, camel_provider_AttributeConstraint: "Attribute" = None, camel_provider_AttributeConstraint354: "Attribute" = None, camel_provider_AttributeConstraint357: "SingleValue" = None, camel_provider_AttributeConstraint360: "SingleValue" = None):
        self.name = name
        self.camel_provider_AttributeConstraint = camel_provider_AttributeConstraint
        self.camel_provider_AttributeConstraint354 = camel_provider_AttributeConstraint354
        self.camel_provider_AttributeConstraint357 = camel_provider_AttributeConstraint357
        self.camel_provider_AttributeConstraint360 = camel_provider_AttributeConstraint360
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_provider_AttributeConstraint360(self):
        return self.__camel_provider_AttributeConstraint360

    @camel_provider_AttributeConstraint360.setter
    def camel_provider_AttributeConstraint360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_AttributeConstraint__camel_provider_AttributeConstraint360", None)
        self.__camel_provider_AttributeConstraint360 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleValue361"):
                opp_val = getattr(old_value, "SingleValue361", None)
                if opp_val == self:
                    setattr(old_value, "SingleValue361", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleValue361"):
                opp_val = getattr(value, "SingleValue361", None)
                setattr(value, "SingleValue361", self)

    @property
    def camel_provider_AttributeConstraint357(self):
        return self.__camel_provider_AttributeConstraint357

    @camel_provider_AttributeConstraint357.setter
    def camel_provider_AttributeConstraint357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_AttributeConstraint__camel_provider_AttributeConstraint357", None)
        self.__camel_provider_AttributeConstraint357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleValue358"):
                opp_val = getattr(old_value, "SingleValue358", None)
                if opp_val == self:
                    setattr(old_value, "SingleValue358", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleValue358"):
                opp_val = getattr(value, "SingleValue358", None)
                setattr(value, "SingleValue358", self)

    @property
    def camel_provider_AttributeConstraint(self):
        return self.__camel_provider_AttributeConstraint

    @camel_provider_AttributeConstraint.setter
    def camel_provider_AttributeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_AttributeConstraint__camel_provider_AttributeConstraint", None)
        self.__camel_provider_AttributeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute352"):
                opp_val = getattr(old_value, "Attribute352", None)
                if opp_val == self:
                    setattr(old_value, "Attribute352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute352"):
                opp_val = getattr(value, "Attribute352", None)
                setattr(value, "Attribute352", self)

    @property
    def camel_provider_AttributeConstraint354(self):
        return self.__camel_provider_AttributeConstraint354

    @camel_provider_AttributeConstraint354.setter
    def camel_provider_AttributeConstraint354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_AttributeConstraint__camel_provider_AttributeConstraint354", None)
        self.__camel_provider_AttributeConstraint354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute355"):
                opp_val = getattr(old_value, "Attribute355", None)
                if opp_val == self:
                    setattr(old_value, "Attribute355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute355"):
                opp_val = getattr(value, "Attribute355", None)
                setattr(value, "Attribute355", self)

class camel_provider_Constraint(ABC):

    def __init__(self, name: str, camel_provider_Constraint: "Feature" = None, camel_provider_Constraint366: "Feature" = None, camel_provider_Constraint369: set["AttributeConstraint"] = None):
        self.name = name
        self.camel_provider_Constraint = camel_provider_Constraint
        self.camel_provider_Constraint366 = camel_provider_Constraint366
        self.camel_provider_Constraint369 = camel_provider_Constraint369 if camel_provider_Constraint369 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_provider_Constraint366(self):
        return self.__camel_provider_Constraint366

    @camel_provider_Constraint366.setter
    def camel_provider_Constraint366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_Constraint__camel_provider_Constraint366", None)
        self.__camel_provider_Constraint366 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature367"):
                opp_val = getattr(old_value, "Feature367", None)
                if opp_val == self:
                    setattr(old_value, "Feature367", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature367"):
                opp_val = getattr(value, "Feature367", None)
                setattr(value, "Feature367", self)

    @property
    def camel_provider_Constraint369(self):
        return self.__camel_provider_Constraint369

    @camel_provider_Constraint369.setter
    def camel_provider_Constraint369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_Constraint__camel_provider_Constraint369", None)
        self.__camel_provider_Constraint369 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeConstraint"):
                    opp_val = getattr(item, "AttributeConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeConstraint"):
                    opp_val = getattr(item, "AttributeConstraint", None)
                    
                    setattr(item, "AttributeConstraint", self)
                    

    @property
    def camel_provider_Constraint(self):
        return self.__camel_provider_Constraint

    @camel_provider_Constraint.setter
    def camel_provider_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_Constraint__camel_provider_Constraint", None)
        self.__camel_provider_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature364"):
                opp_val = getattr(old_value, "Feature364", None)
                if opp_val == self:
                    setattr(old_value, "Feature364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature364"):
                opp_val = getattr(value, "Feature364", None)
                setattr(value, "Feature364", self)

class Clone:

    pass
class camel_provider_Clone:

    def __init__(self, name: str, camel_provider_Clone: set["Clone"] = None):
        self.name = name
        self.camel_provider_Clone = camel_provider_Clone if camel_provider_Clone is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_provider_Clone(self):
        return self.__camel_provider_Clone

    @camel_provider_Clone.setter
    def camel_provider_Clone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_Clone__camel_provider_Clone", None)
        self.__camel_provider_Clone = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Clone"):
                    opp_val = getattr(item, "Clone", None)
                    
                    if opp_val == self:
                        setattr(item, "Clone", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Clone"):
                    opp_val = getattr(item, "Clone", None)
                    
                    setattr(item, "Clone", self)
                    

class Cardinality:

    pass
class camel_provider_GroupCardinality(Cardinality):

    pass
class camel_provider_FeatCardinality(Cardinality):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class camel_organisation_UserGroup:

    def __init__(self, name: str, camel_organisation_UserGroup: set["User"] = None):
        self.name = name
        self.camel_organisation_UserGroup = camel_organisation_UserGroup if camel_organisation_UserGroup is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_organisation_UserGroup(self):
        return self.__camel_organisation_UserGroup

    @camel_organisation_UserGroup.setter
    def camel_organisation_UserGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_UserGroup__camel_organisation_UserGroup", None)
        self.__camel_organisation_UserGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User342"):
                    opp_val = getattr(item, "User342", None)
                    
                    if opp_val == self:
                        setattr(item, "User342", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User342"):
                    opp_val = getattr(item, "User342", None)
                    
                    setattr(item, "User342", self)
                    

class camel_provider_Attribute:

    def __init__(self, name: str, unitType: str, camel_provider_Attribute: "SingleValue" = None, camel_provider_Attribute349: "ValueType" = None):
        self.name = name
        self.unitType = unitType
        self.camel_provider_Attribute = camel_provider_Attribute
        self.camel_provider_Attribute349 = camel_provider_Attribute349
        
    @property
    def unitType(self) -> str:
        return self.__unitType

    @unitType.setter
    def unitType(self, unitType: str):
        self.__unitType = unitType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_provider_Attribute(self):
        return self.__camel_provider_Attribute

    @camel_provider_Attribute.setter
    def camel_provider_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_Attribute__camel_provider_Attribute", None)
        self.__camel_provider_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleValue347"):
                opp_val = getattr(old_value, "SingleValue347", None)
                if opp_val == self:
                    setattr(old_value, "SingleValue347", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleValue347"):
                opp_val = getattr(value, "SingleValue347", None)
                setattr(value, "SingleValue347", self)

    @property
    def camel_provider_Attribute349(self):
        return self.__camel_provider_Attribute349

    @camel_provider_Attribute349.setter
    def camel_provider_Attribute349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_provider_Attribute__camel_provider_Attribute349", None)
        self.__camel_provider_Attribute349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueType350"):
                opp_val = getattr(old_value, "ValueType350", None)
                if opp_val == self:
                    setattr(old_value, "ValueType350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueType350"):
                opp_val = getattr(value, "ValueType350", None)
                setattr(value, "ValueType350", self)

    def checkValue(self, v: str, diff: bool) -> bool:
        # TODO: Implement checkValue method
        pass

class Feature:

    pass
class camel_provider_Alternative(Feature):

    pass
class Constraint:

    pass
class camel_provider_Requires(Constraint):

    pass
class camel_provider_Excludes(Constraint):

    pass
class camel_provider_Implies(Constraint):

    pass
class camel_organisation_Permission:

    def __init__(self, name: str, startTime: date, endTime: date, action: str, camel_organisation_Permission: "Role" = None, camel_organisation_Permission331: "ResourceFilter" = None):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.action = action
        self.camel_organisation_Permission = camel_organisation_Permission
        self.camel_organisation_Permission331 = camel_organisation_Permission331
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def startTime(self) -> date:
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime: date):
        self.__startTime = startTime

    @property
    def endTime(self) -> date:
        return self.__endTime

    @endTime.setter
    def endTime(self, endTime: date):
        self.__endTime = endTime

    @property
    def camel_organisation_Permission331(self):
        return self.__camel_organisation_Permission331

    @camel_organisation_Permission331.setter
    def camel_organisation_Permission331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_Permission__camel_organisation_Permission331", None)
        self.__camel_organisation_Permission331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceFilter332"):
                opp_val = getattr(old_value, "ResourceFilter332", None)
                if opp_val == self:
                    setattr(old_value, "ResourceFilter332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceFilter332"):
                opp_val = getattr(value, "ResourceFilter332", None)
                setattr(value, "ResourceFilter332", self)

    @property
    def camel_organisation_Permission(self):
        return self.__camel_organisation_Permission

    @camel_organisation_Permission.setter
    def camel_organisation_Permission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_Permission__camel_organisation_Permission", None)
        self.__camel_organisation_Permission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role329"):
                opp_val = getattr(old_value, "Role329", None)
                if opp_val == self:
                    setattr(old_value, "Role329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role329"):
                opp_val = getattr(value, "Role329", None)
                setattr(value, "Role329", self)

    def checkStartEndDates(self, this: str) -> bool:
        # TODO: Implement checkStartEndDates method
        pass

class camel_organisation_RoleAssignment:

    def __init__(self, name: str, startTime: date, endTime: date, assignmentTime: date, camel_organisation_RoleAssignment: "User" = None, camel_organisation_RoleAssignment336: "Role" = None, camel_organisation_RoleAssignment339: "UserGroup" = None):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.assignmentTime = assignmentTime
        self.camel_organisation_RoleAssignment = camel_organisation_RoleAssignment
        self.camel_organisation_RoleAssignment336 = camel_organisation_RoleAssignment336
        self.camel_organisation_RoleAssignment339 = camel_organisation_RoleAssignment339
        
    @property
    def startTime(self) -> date:
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime: date):
        self.__startTime = startTime

    @property
    def endTime(self) -> date:
        return self.__endTime

    @endTime.setter
    def endTime(self, endTime: date):
        self.__endTime = endTime

    @property
    def assignmentTime(self) -> date:
        return self.__assignmentTime

    @assignmentTime.setter
    def assignmentTime(self, assignmentTime: date):
        self.__assignmentTime = assignmentTime

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_organisation_RoleAssignment339(self):
        return self.__camel_organisation_RoleAssignment339

    @camel_organisation_RoleAssignment339.setter
    def camel_organisation_RoleAssignment339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_RoleAssignment__camel_organisation_RoleAssignment339", None)
        self.__camel_organisation_RoleAssignment339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserGroup340"):
                opp_val = getattr(old_value, "UserGroup340", None)
                if opp_val == self:
                    setattr(old_value, "UserGroup340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserGroup340"):
                opp_val = getattr(value, "UserGroup340", None)
                setattr(value, "UserGroup340", self)

    @property
    def camel_organisation_RoleAssignment(self):
        return self.__camel_organisation_RoleAssignment

    @camel_organisation_RoleAssignment.setter
    def camel_organisation_RoleAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_RoleAssignment__camel_organisation_RoleAssignment", None)
        self.__camel_organisation_RoleAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User334"):
                opp_val = getattr(old_value, "User334", None)
                if opp_val == self:
                    setattr(old_value, "User334", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User334"):
                opp_val = getattr(value, "User334", None)
                setattr(value, "User334", self)

    @property
    def camel_organisation_RoleAssignment336(self):
        return self.__camel_organisation_RoleAssignment336

    @camel_organisation_RoleAssignment336.setter
    def camel_organisation_RoleAssignment336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_RoleAssignment__camel_organisation_RoleAssignment336", None)
        self.__camel_organisation_RoleAssignment336 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role337"):
                opp_val = getattr(old_value, "Role337", None)
                if opp_val == self:
                    setattr(old_value, "Role337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role337"):
                opp_val = getattr(value, "Role337", None)
                setattr(value, "Role337", self)

    def checkStartEndDates(self, this: str) -> bool:
        # TODO: Implement checkStartEndDates method
        pass

    def checkAssignedOnDates(self, this: str) -> bool:
        # TODO: Implement checkAssignedOnDates method
        pass

class camel_organisation_Role:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class camel_organisation_ResourceFilter(ABC):

    def __init__(self, name: str, resourcePattern: str):
        self.name = name
        self.resourcePattern = resourcePattern
        
    @property
    def resourcePattern(self) -> str:
        return self.__resourcePattern

    @resourcePattern.setter
    def resourcePattern(self, resourcePattern: str):
        self.__resourcePattern = resourcePattern

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class camel_organisation_Entity:

    pass
class camel_organisation_DataCenter:

    def __init__(self, name: str, codeName: str, camel_organisation_DataCenter: "Location" = None):
        self.name = name
        self.codeName = codeName
        self.camel_organisation_DataCenter = camel_organisation_DataCenter
        
    @property
    def codeName(self) -> str:
        return self.__codeName

    @codeName.setter
    def codeName(self, codeName: str):
        self.__codeName = codeName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_organisation_DataCenter(self):
        return self.__camel_organisation_DataCenter

    @camel_organisation_DataCenter.setter
    def camel_organisation_DataCenter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_DataCenter__camel_organisation_DataCenter", None)
        self.__camel_organisation_DataCenter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location"):
                opp_val = getattr(old_value, "Location", None)
                if opp_val == self:
                    setattr(old_value, "Location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location"):
                opp_val = getattr(value, "Location", None)
                setattr(value, "Location", self)

class camel_organisation_ExternalIdentifier:

    def __init__(self, identifier: str, description: str):
        self.identifier = identifier
        self.description = description
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class PaaSageCredentials:

    pass
class CloudCredentials:

    pass
class SecurityCapability:

    pass
class UserGroup:

    pass
class User:

    pass
class ExternalIdentifier:

    pass
class CloudProvider:

    pass
class Organisation:

    pass
class camel_organisation_CloudProvider(Organisation):

    def __init__(self, PaaS: bool, IaaS: bool, public: bool, SaaS: bool, camel_organisation_CloudProvider: "ProviderModel" = None, camel_organisation_CloudProvider315: set["SecurityCapability"] = None, Organisation: "camel_organisation_OrganisationModel"):
        self.PaaS = PaaS
        self.IaaS = IaaS
        self.public = public
        self.SaaS = SaaS
        self.camel_organisation_CloudProvider = camel_organisation_CloudProvider
        self.camel_organisation_CloudProvider315 = camel_organisation_CloudProvider315 if camel_organisation_CloudProvider315 is not None else set()
        
    @property
    def IaaS(self) -> bool:
        return self.__IaaS

    @IaaS.setter
    def IaaS(self, IaaS: bool):
        self.__IaaS = IaaS

    @property
    def SaaS(self) -> bool:
        return self.__SaaS

    @SaaS.setter
    def SaaS(self, SaaS: bool):
        self.__SaaS = SaaS

    @property
    def public(self) -> bool:
        return self.__public

    @public.setter
    def public(self, public: bool):
        self.__public = public

    @property
    def PaaS(self) -> bool:
        return self.__PaaS

    @PaaS.setter
    def PaaS(self, PaaS: bool):
        self.__PaaS = PaaS

    @property
    def camel_organisation_CloudProvider315(self):
        return self.__camel_organisation_CloudProvider315

    @camel_organisation_CloudProvider315.setter
    def camel_organisation_CloudProvider315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_CloudProvider__camel_organisation_CloudProvider315", None)
        self.__camel_organisation_CloudProvider315 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecurityCapability"):
                    opp_val = getattr(item, "SecurityCapability", None)
                    
                    if opp_val == self:
                        setattr(item, "SecurityCapability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecurityCapability"):
                    opp_val = getattr(item, "SecurityCapability", None)
                    
                    setattr(item, "SecurityCapability", self)
                    

    @property
    def camel_organisation_CloudProvider(self):
        return self.__camel_organisation_CloudProvider

    @camel_organisation_CloudProvider.setter
    def camel_organisation_CloudProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_CloudProvider__camel_organisation_CloudProvider", None)
        self.__camel_organisation_CloudProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProviderModel313"):
                opp_val = getattr(old_value, "ProviderModel313", None)
                if opp_val == self:
                    setattr(old_value, "ProviderModel313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProviderModel313"):
                opp_val = getattr(value, "ProviderModel313", None)
                setattr(value, "ProviderModel313", self)

class Credentials:

    pass
class camel_organisation_PaaSageCredentials(Credentials):

    def __init__(self, password: str):
        self.password = password
        
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

class camel_organisation_CloudCredentials(Credentials):

    def __init__(self, name: str, securityGroup: str, publicSSHKey: str, privateSSHKey: str, username: str, password: str, camel_organisation_CloudCredentials: "CloudProvider" = None):
        self.name = name
        self.securityGroup = securityGroup
        self.publicSSHKey = publicSSHKey
        self.privateSSHKey = privateSSHKey
        self.username = username
        self.password = password
        self.camel_organisation_CloudCredentials = camel_organisation_CloudCredentials
        
    @property
    def publicSSHKey(self) -> str:
        return self.__publicSSHKey

    @publicSSHKey.setter
    def publicSSHKey(self, publicSSHKey: str):
        self.__publicSSHKey = publicSSHKey

    @property
    def privateSSHKey(self) -> str:
        return self.__privateSSHKey

    @privateSSHKey.setter
    def privateSSHKey(self, privateSSHKey: str):
        self.__privateSSHKey = privateSSHKey

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def securityGroup(self) -> str:
        return self.__securityGroup

    @securityGroup.setter
    def securityGroup(self, securityGroup: str):
        self.__securityGroup = securityGroup

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_organisation_CloudCredentials(self):
        return self.__camel_organisation_CloudCredentials

    @camel_organisation_CloudCredentials.setter
    def camel_organisation_CloudCredentials(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_CloudCredentials__camel_organisation_CloudCredentials", None)
        self.__camel_organisation_CloudCredentials = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CloudProvider310"):
                opp_val = getattr(old_value, "CloudProvider310", None)
                if opp_val == self:
                    setattr(old_value, "CloudProvider310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CloudProvider310"):
                opp_val = getattr(value, "CloudProvider310", None)
                setattr(value, "CloudProvider310", self)

class camel_organisation_Credentials(ABC):

    pass
class ResourceFilter:

    pass
class camel_organisation_InformationResourceFilter(ResourceFilter):

    def __init__(self, informationResourcePath: str, everyInformationResource: bool, ResourceFilter332: "camel_organisation_Permission", ResourceFilter: "camel_organisation_OrganisationModel"):
        self.informationResourcePath = informationResourcePath
        self.everyInformationResource = everyInformationResource
        
    @property
    def informationResourcePath(self) -> str:
        return self.__informationResourcePath

    @informationResourcePath.setter
    def informationResourcePath(self, informationResourcePath: str):
        self.__informationResourcePath = informationResourcePath

    @property
    def everyInformationResource(self) -> bool:
        return self.__everyInformationResource

    @everyInformationResource.setter
    def everyInformationResource(self, everyInformationResource: bool):
        self.__everyInformationResource = everyInformationResource

class camel_organisation_ServiceResourceFilter(ResourceFilter):

    def __init__(self, serviceURL: str, everyService: bool, ResourceFilter332: "camel_organisation_Permission", ResourceFilter: "camel_organisation_OrganisationModel"):
        self.serviceURL = serviceURL
        self.everyService = everyService
        
    @property
    def serviceURL(self) -> str:
        return self.__serviceURL

    @serviceURL.setter
    def serviceURL(self, serviceURL: str):
        self.__serviceURL = serviceURL

    @property
    def everyService(self) -> bool:
        return self.__everyService

    @everyService.setter
    def everyService(self, everyService: bool):
        self.__everyService = everyService

class Permission:

    pass
class RoleAssignment:

    pass
class Role:

    pass
class DataCenter:

    pass
class camel_metric_ConditionContext(ABC):

    def __init__(self, quantifier: str, minQuantity: float, maxQuantity: float, isRelative: bool, name: str, camel_metric_ConditionContext: "Component" = None, camel_metric_ConditionContext245: "metric_camel_Application" = None):
        self.quantifier = quantifier
        self.minQuantity = minQuantity
        self.maxQuantity = maxQuantity
        self.isRelative = isRelative
        self.name = name
        self.camel_metric_ConditionContext = camel_metric_ConditionContext
        self.camel_metric_ConditionContext245 = camel_metric_ConditionContext245
        
    @property
    def maxQuantity(self) -> float:
        return self.__maxQuantity

    @maxQuantity.setter
    def maxQuantity(self, maxQuantity: float):
        self.__maxQuantity = maxQuantity

    @property
    def quantifier(self) -> str:
        return self.__quantifier

    @quantifier.setter
    def quantifier(self, quantifier: str):
        self.__quantifier = quantifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isRelative(self) -> bool:
        return self.__isRelative

    @isRelative.setter
    def isRelative(self, isRelative: bool):
        self.__isRelative = isRelative

    @property
    def minQuantity(self) -> float:
        return self.__minQuantity

    @minQuantity.setter
    def minQuantity(self, minQuantity: float):
        self.__minQuantity = minQuantity

    @property
    def camel_metric_ConditionContext245(self):
        return self.__camel_metric_ConditionContext245

    @camel_metric_ConditionContext245.setter
    def camel_metric_ConditionContext245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_ConditionContext__camel_metric_ConditionContext245", None)
        self.__camel_metric_ConditionContext245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metric_camel_Application"):
                opp_val = getattr(old_value, "metric_camel_Application", None)
                if opp_val == self:
                    setattr(old_value, "metric_camel_Application", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metric_camel_Application"):
                opp_val = getattr(value, "metric_camel_Application", None)
                setattr(value, "metric_camel_Application", self)

    @property
    def camel_metric_ConditionContext(self):
        return self.__camel_metric_ConditionContext

    @camel_metric_ConditionContext.setter
    def camel_metric_ConditionContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_ConditionContext__camel_metric_ConditionContext", None)
        self.__camel_metric_ConditionContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Component243"):
                opp_val = getattr(old_value, "Component243", None)
                if opp_val == self:
                    setattr(old_value, "Component243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component243"):
                opp_val = getattr(value, "Component243", None)
                setattr(value, "Component243", self)

class ConditionContext:

    pass
class camel_metric_PropertyContext(ConditionContext):

    pass
class camel_metric_MetricContext(ConditionContext):

    pass
class metric_camel_Application:

    pass
class camel_metric_Schedule:

    def __init__(self, start: date, end: date, type: str, repetitions: int, interval: str, name: str, camel_metric_Schedule: "TimeIntervalUnit" = None):
        self.start = start
        self.end = end
        self.type = type
        self.repetitions = repetitions
        self.interval = interval
        self.name = name
        self.camel_metric_Schedule = camel_metric_Schedule
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def repetitions(self) -> int:
        return self.__repetitions

    @repetitions.setter
    def repetitions(self, repetitions: int):
        self.__repetitions = repetitions

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def interval(self) -> str:
        return self.__interval

    @interval.setter
    def interval(self, interval: str):
        self.__interval = interval

    @property
    def start(self) -> date:
        return self.__start

    @start.setter
    def start(self, start: date):
        self.__start = start

    @property
    def end(self) -> date:
        return self.__end

    @end.setter
    def end(self, end: date):
        self.__end = end

    @property
    def camel_metric_Schedule(self):
        return self.__camel_metric_Schedule

    @camel_metric_Schedule.setter
    def camel_metric_Schedule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_Schedule__camel_metric_Schedule", None)
        self.__camel_metric_Schedule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TimeIntervalUnit239"):
                opp_val = getattr(old_value, "TimeIntervalUnit239", None)
                if opp_val == self:
                    setattr(old_value, "TimeIntervalUnit239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TimeIntervalUnit239"):
                opp_val = getattr(value, "TimeIntervalUnit239", None)
                setattr(value, "TimeIntervalUnit239", self)

    def checkStartEndDates(self, this: str) -> bool:
        # TODO: Implement checkStartEndDates method
        pass

    def checkIntervalRepetitions(self, s: str) -> bool:
        # TODO: Implement checkIntervalRepetitions method
        pass

class camel_metric_Window:

    def __init__(self, name: str, windowType: str, sizeType: str, measurementSize: str, timeSize: str, camel_metric_Window: "TimeIntervalUnit" = None):
        self.name = name
        self.windowType = windowType
        self.sizeType = sizeType
        self.measurementSize = measurementSize
        self.timeSize = timeSize
        self.camel_metric_Window = camel_metric_Window
        
    @property
    def windowType(self) -> str:
        return self.__windowType

    @windowType.setter
    def windowType(self, windowType: str):
        self.__windowType = windowType

    @property
    def timeSize(self) -> str:
        return self.__timeSize

    @timeSize.setter
    def timeSize(self, timeSize: str):
        self.__timeSize = timeSize

    @property
    def sizeType(self) -> str:
        return self.__sizeType

    @sizeType.setter
    def sizeType(self, sizeType: str):
        self.__sizeType = sizeType

    @property
    def measurementSize(self) -> str:
        return self.__measurementSize

    @measurementSize.setter
    def measurementSize(self, measurementSize: str):
        self.__measurementSize = measurementSize

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_metric_Window(self):
        return self.__camel_metric_Window

    @camel_metric_Window.setter
    def camel_metric_Window(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_Window__camel_metric_Window", None)
        self.__camel_metric_Window = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TimeIntervalUnit241"):
                opp_val = getattr(old_value, "TimeIntervalUnit241", None)
                if opp_val == self:
                    setattr(old_value, "TimeIntervalUnit241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TimeIntervalUnit241"):
                opp_val = getattr(value, "TimeIntervalUnit241", None)
                setattr(value, "TimeIntervalUnit241", self)

class camel_metric_Sensor:

    def __init__(self, name: str, configuration: str, isPush: bool):
        self.name = name
        self.configuration = configuration
        self.isPush = isPush
        
    @property
    def isPush(self) -> bool:
        return self.__isPush

    @isPush.setter
    def isPush(self, isPush: bool):
        self.__isPush = isPush

    @property
    def configuration(self) -> str:
        return self.__configuration

    @configuration.setter
    def configuration(self, configuration: str):
        self.__configuration = configuration

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class MetricFormula:

    pass
class camel_metric_Property:

    def __init__(self, name: str, description: str, type: str, camel_metric_Property: set["Property"] = None, camel_metric_Property236: set["Sensor"] = None):
        self.name = name
        self.description = description
        self.type = type
        self.camel_metric_Property = camel_metric_Property if camel_metric_Property is not None else set()
        self.camel_metric_Property236 = camel_metric_Property236 if camel_metric_Property236 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_metric_Property236(self):
        return self.__camel_metric_Property236

    @camel_metric_Property236.setter
    def camel_metric_Property236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_Property__camel_metric_Property236", None)
        self.__camel_metric_Property236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Sensor237"):
                    opp_val = getattr(item, "Sensor237", None)
                    
                    if opp_val == self:
                        setattr(item, "Sensor237", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Sensor237"):
                    opp_val = getattr(item, "Sensor237", None)
                    
                    setattr(item, "Sensor237", self)
                    

    @property
    def camel_metric_Property(self):
        return self.__camel_metric_Property

    @camel_metric_Property.setter
    def camel_metric_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_Property__camel_metric_Property", None)
        self.__camel_metric_Property = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property234"):
                    opp_val = getattr(item, "Property234", None)
                    
                    if opp_val == self:
                        setattr(item, "Property234", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property234"):
                    opp_val = getattr(item, "Property234", None)
                    
                    setattr(item, "Property234", self)
                    

class camel_metric_MetricObjectBinding(ABC):

    def __init__(self, name: str, camel_metric_MetricObjectBinding: "ExecutionContext" = None):
        self.name = name
        self.camel_metric_MetricObjectBinding = camel_metric_MetricObjectBinding
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_metric_MetricObjectBinding(self):
        return self.__camel_metric_MetricObjectBinding

    @camel_metric_MetricObjectBinding.setter
    def camel_metric_MetricObjectBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_MetricObjectBinding__camel_metric_MetricObjectBinding", None)
        self.__camel_metric_MetricObjectBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExecutionContext226"):
                opp_val = getattr(old_value, "ExecutionContext226", None)
                if opp_val == self:
                    setattr(old_value, "ExecutionContext226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExecutionContext226"):
                opp_val = getattr(value, "ExecutionContext226", None)
                setattr(value, "ExecutionContext226", self)

class MetricFormulaParameter:

    pass
class camel_metric_Metric(MetricFormulaParameter):

    def __init__(self, description: str, valueDirection: str, layer: str, isVariable: bool, camel_metric_Metric: "ValueType" = None, camel_metric_Metric221: "Unit" = None, camel_metric_Metric223: "Property" = None, MetricFormulaParameter: "camel_metric_MetricFormula", MetricFormulaParameter269: "camel_metric_MetricModel"):
        self.description = description
        self.valueDirection = valueDirection
        self.layer = layer
        self.isVariable = isVariable
        self.camel_metric_Metric = camel_metric_Metric
        self.camel_metric_Metric221 = camel_metric_Metric221
        self.camel_metric_Metric223 = camel_metric_Metric223
        
    @property
    def valueDirection(self) -> str:
        return self.__valueDirection

    @valueDirection.setter
    def valueDirection(self, valueDirection: str):
        self.__valueDirection = valueDirection

    @property
    def isVariable(self) -> bool:
        return self.__isVariable

    @isVariable.setter
    def isVariable(self, isVariable: bool):
        self.__isVariable = isVariable

    @property
    def layer(self) -> str:
        return self.__layer

    @layer.setter
    def layer(self, layer: str):
        self.__layer = layer

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def camel_metric_Metric(self):
        return self.__camel_metric_Metric

    @camel_metric_Metric.setter
    def camel_metric_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_Metric__camel_metric_Metric", None)
        self.__camel_metric_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueType"):
                opp_val = getattr(old_value, "ValueType", None)
                if opp_val == self:
                    setattr(old_value, "ValueType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueType"):
                opp_val = getattr(value, "ValueType", None)
                setattr(value, "ValueType", self)

    @property
    def camel_metric_Metric223(self):
        return self.__camel_metric_Metric223

    @camel_metric_Metric223.setter
    def camel_metric_Metric223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_Metric__camel_metric_Metric223", None)
        self.__camel_metric_Metric223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property"):
                opp_val = getattr(old_value, "Property", None)
                if opp_val == self:
                    setattr(old_value, "Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property"):
                opp_val = getattr(value, "Property", None)
                setattr(value, "Property", self)

    @property
    def camel_metric_Metric221(self):
        return self.__camel_metric_Metric221

    @camel_metric_Metric221.setter
    def camel_metric_Metric221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_Metric__camel_metric_Metric221", None)
        self.__camel_metric_Metric221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Unit"):
                opp_val = getattr(old_value, "Unit", None)
                if opp_val == self:
                    setattr(old_value, "Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Unit"):
                opp_val = getattr(value, "Unit", None)
                setattr(value, "Unit", self)

    def checkRecursiveness(self, mt2: str, mt1: str) -> bool:
        # TODO: Implement checkRecursiveness method
        pass

class camel_metric_MetricFormula(MetricFormulaParameter):

    def __init__(self, function: str, functionArity: str, functionPattern: str, camel_metric_MetricFormula: set["MetricFormulaParameter"] = None, MetricFormulaParameter: "camel_metric_MetricFormula", MetricFormulaParameter269: "camel_metric_MetricModel"):
        self.function = function
        self.functionArity = functionArity
        self.functionPattern = functionPattern
        self.camel_metric_MetricFormula = camel_metric_MetricFormula if camel_metric_MetricFormula is not None else set()
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def functionArity(self) -> str:
        return self.__functionArity

    @functionArity.setter
    def functionArity(self, functionArity: str):
        self.__functionArity = functionArity

    @property
    def functionPattern(self) -> str:
        return self.__functionPattern

    @functionPattern.setter
    def functionPattern(self, functionPattern: str):
        self.__functionPattern = functionPattern

    @property
    def camel_metric_MetricFormula(self):
        return self.__camel_metric_MetricFormula

    @camel_metric_MetricFormula.setter
    def camel_metric_MetricFormula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_MetricFormula__camel_metric_MetricFormula", None)
        self.__camel_metric_MetricFormula = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetricFormulaParameter"):
                    opp_val = getattr(item, "MetricFormulaParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "MetricFormulaParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetricFormulaParameter"):
                    opp_val = getattr(item, "MetricFormulaParameter", None)
                    
                    setattr(item, "MetricFormulaParameter", self)
                    

    def containsMetric(self, m: str) -> bool:
        # TODO: Implement containsMetric method
        pass

    def hasMetric(self) -> bool:
        # TODO: Implement hasMetric method
        pass

class Property:

    pass
class camel_security_SecurityProperty(Property):

    pass
class Unit:

    pass
class camel_unit_TimeIntervalUnit(Unit):

    pass
class camel_unit_MonetaryUnit(Unit):

    pass
class camel_unit_ThroughputUnit(Unit):

    pass
class camel_unit_Dimensionless(Unit):

    pass
class camel_unit_RequestUnit(Unit):

    pass
class camel_unit_TransactionUnit(Unit):

    pass
class camel_unit_StorageUnit(Unit):

    pass
class camel_unit_CoreUnit(Unit):

    pass
class ValueType:

    pass
class camel_type_StringValueType(ValueType):

    def __init__(self, primitiveType: str, ValueType534: "camel_type_List", ValueType: "camel_metric_Metric", ValueType350: "camel_provider_Attribute", ValueType522: "camel_type_TypeModel"):
        self.primitiveType = primitiveType
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

class camel_type_Range(ValueType):

    def __init__(self, primitiveType: str, camel_type_Range537: "Limit" = None, camel_type_Range: "Limit" = None, ValueType534: "camel_type_List", ValueType: "camel_metric_Metric", ValueType350: "camel_provider_Attribute", ValueType522: "camel_type_TypeModel"):
        self.primitiveType = primitiveType
        self.camel_type_Range537 = camel_type_Range537
        self.camel_type_Range = camel_type_Range
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

    @property
    def camel_type_Range(self):
        return self.__camel_type_Range

    @camel_type_Range.setter
    def camel_type_Range(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_type_Range__camel_type_Range", None)
        self.__camel_type_Range = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Limit"):
                opp_val = getattr(old_value, "Limit", None)
                if opp_val == self:
                    setattr(old_value, "Limit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Limit"):
                opp_val = getattr(value, "Limit", None)
                setattr(value, "Limit", self)

    @property
    def camel_type_Range537(self):
        return self.__camel_type_Range537

    @camel_type_Range537.setter
    def camel_type_Range537(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_type_Range__camel_type_Range537", None)
        self.__camel_type_Range537 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Limit538"):
                opp_val = getattr(old_value, "Limit538", None)
                if opp_val == self:
                    setattr(old_value, "Limit538", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Limit538"):
                opp_val = getattr(value, "Limit538", None)
                setattr(value, "Limit538", self)

    def checkType(self, lower: bool, type: str, l: str) -> bool:
        # TODO: Implement checkType method
        pass

    def includesValue(self, n: float) -> bool:
        # TODO: Implement includesValue method
        pass

class camel_type_BooleanValueType(ValueType):

    def __init__(self, primitiveType: str, ValueType534: "camel_type_List", ValueType: "camel_metric_Metric", ValueType350: "camel_provider_Attribute", ValueType522: "camel_type_TypeModel"):
        self.primitiveType = primitiveType
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

class camel_type_List(ValueType):

    def __init__(self, primitiveType: str, camel_type_List: set["SingleValue"] = None, camel_type_List533: "ValueType" = None, ValueType534: "camel_type_List", ValueType: "camel_metric_Metric", ValueType350: "camel_provider_Attribute", ValueType522: "camel_type_TypeModel"):
        self.primitiveType = primitiveType
        self.camel_type_List = camel_type_List if camel_type_List is not None else set()
        self.camel_type_List533 = camel_type_List533
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

    @property
    def camel_type_List(self):
        return self.__camel_type_List

    @camel_type_List.setter
    def camel_type_List(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_type_List__camel_type_List", None)
        self.__camel_type_List = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SingleValue531"):
                    opp_val = getattr(item, "SingleValue531", None)
                    
                    if opp_val == self:
                        setattr(item, "SingleValue531", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SingleValue531"):
                    opp_val = getattr(item, "SingleValue531", None)
                    
                    setattr(item, "SingleValue531", self)
                    

    @property
    def camel_type_List533(self):
        return self.__camel_type_List533

    @camel_type_List533.setter
    def camel_type_List533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_type_List__camel_type_List533", None)
        self.__camel_type_List533 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueType534"):
                opp_val = getattr(old_value, "ValueType534", None)
                if opp_val == self:
                    setattr(old_value, "ValueType534", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueType534"):
                opp_val = getattr(value, "ValueType534", None)
                setattr(value, "ValueType534", self)

    def includesValue(self, v: str) -> bool:
        # TODO: Implement includesValue method
        pass

    def checkValueType(self, p: str) -> bool:
        # TODO: Implement checkValueType method
        pass

class camel_type_RangeUnion(ValueType):

    def __init__(self, primitiveType: str, camel_type_RangeUnion: set["Range"] = None, ValueType534: "camel_type_List", ValueType: "camel_metric_Metric", ValueType350: "camel_provider_Attribute", ValueType522: "camel_type_TypeModel"):
        self.primitiveType = primitiveType
        self.camel_type_RangeUnion = camel_type_RangeUnion if camel_type_RangeUnion is not None else set()
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

    @property
    def camel_type_RangeUnion(self):
        return self.__camel_type_RangeUnion

    @camel_type_RangeUnion.setter
    def camel_type_RangeUnion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_type_RangeUnion__camel_type_RangeUnion", None)
        self.__camel_type_RangeUnion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Range"):
                    opp_val = getattr(item, "Range", None)
                    
                    if opp_val == self:
                        setattr(item, "Range", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Range"):
                    opp_val = getattr(item, "Range", None)
                    
                    setattr(item, "Range", self)
                    

    def includesValue(self, n: float) -> bool:
        # TODO: Implement includesValue method
        pass

    def invalidRangeSequence(self, ru: str) -> bool:
        # TODO: Implement invalidRangeSequence method
        pass

class camel_type_Enumeration(ValueType):

    def __init__(self, camel_type_Enumeration: set["EnumerateValue"] = None, ValueType534: "camel_type_List", ValueType: "camel_metric_Metric", ValueType350: "camel_provider_Attribute", ValueType522: "camel_type_TypeModel"):
        self.camel_type_Enumeration = camel_type_Enumeration if camel_type_Enumeration is not None else set()
        
    @property
    def camel_type_Enumeration(self):
        return self.__camel_type_Enumeration

    @camel_type_Enumeration.setter
    def camel_type_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_type_Enumeration__camel_type_Enumeration", None)
        self.__camel_type_Enumeration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnumerateValue"):
                    opp_val = getattr(item, "EnumerateValue", None)
                    
                    if opp_val == self:
                        setattr(item, "EnumerateValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnumerateValue"):
                    opp_val = getattr(item, "EnumerateValue", None)
                    
                    setattr(item, "EnumerateValue", self)
                    

    def includesName(self, name: str) -> bool:
        # TODO: Implement includesName method
        pass

    def includesValue(self, value: int) -> bool:
        # TODO: Implement includesValue method
        pass

class Window:

    pass
class Schedule:

    pass
class Metric:

    pass
class camel_metric_RawMetric(Metric):

    pass
class camel_metric_CompositeMetric(Metric):

    def __init__(self, camel_metric_CompositeMetric: "MetricFormula" = None, Metric277: "camel_metric_MetricContext", Metric249: "camel_metric_MetricModel", Metric404: "camel_requirement_OptimisationRequirement", Metric: "camel_metric_MetricInstance"):
        self.camel_metric_CompositeMetric = camel_metric_CompositeMetric
        
    @property
    def camel_metric_CompositeMetric(self):
        return self.__camel_metric_CompositeMetric

    @camel_metric_CompositeMetric.setter
    def camel_metric_CompositeMetric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_CompositeMetric__camel_metric_CompositeMetric", None)
        self.__camel_metric_CompositeMetric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetricFormula"):
                opp_val = getattr(old_value, "MetricFormula", None)
                if opp_val == self:
                    setattr(old_value, "MetricFormula", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetricFormula"):
                opp_val = getattr(value, "MetricFormula", None)
                setattr(value, "MetricFormula", self)

    def greaterEqualThanLayer(self, l1: str, l2: str) -> bool:
        # TODO: Implement greaterEqualThanLayer method
        pass

class camel_metric_MetricFormulaParameter:

    def __init__(self, name: str, camel_metric_MetricFormulaParameter: "SingleValue" = None):
        self.name = name
        self.camel_metric_MetricFormulaParameter = camel_metric_MetricFormulaParameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_metric_MetricFormulaParameter(self):
        return self.__camel_metric_MetricFormulaParameter

    @camel_metric_MetricFormulaParameter.setter
    def camel_metric_MetricFormulaParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_MetricFormulaParameter__camel_metric_MetricFormulaParameter", None)
        self.__camel_metric_MetricFormulaParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleValue217"):
                opp_val = getattr(old_value, "SingleValue217", None)
                if opp_val == self:
                    setattr(old_value, "SingleValue217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleValue217"):
                opp_val = getattr(value, "SingleValue217", None)
                setattr(value, "SingleValue217", self)

class Sensor:

    pass
class MetricObjectBinding:

    pass
class camel_metric_MetricComponentBinding(MetricObjectBinding):

    pass
class camel_metric_MetricVMBinding(MetricObjectBinding):

    pass
class camel_metric_MetricApplicationBinding(MetricObjectBinding):

    pass
class Condition:

    pass
class camel_metric_MetricCondition(Condition):

    pass
class camel_metric_Condition(ABC):

    def __init__(self, name: str, comparisonOperator: str, threshold: float, validity: date):
        self.name = name
        self.comparisonOperator = comparisonOperator
        self.threshold = threshold
        self.validity = validity
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comparisonOperator(self) -> str:
        return self.__comparisonOperator

    @comparisonOperator.setter
    def comparisonOperator(self, comparisonOperator: str):
        self.__comparisonOperator = comparisonOperator

    @property
    def validity(self) -> date:
        return self.__validity

    @validity.setter
    def validity(self, validity: date):
        self.__validity = validity

    @property
    def threshold(self) -> float:
        return self.__threshold

    @threshold.setter
    def threshold(self, threshold: float):
        self.__threshold = threshold

class camel_metric_MetricInstance(ABC):

    def __init__(self, name: str, camel_metric_MetricInstance209: "MetricObjectBinding" = None, camel_metric_MetricInstance211: "MetricContext" = None, camel_metric_MetricInstance: "Metric" = None, camel_metric_MetricInstance205: "Schedule" = None, camel_metric_MetricInstance207: "Window" = None):
        self.name = name
        self.camel_metric_MetricInstance209 = camel_metric_MetricInstance209
        self.camel_metric_MetricInstance211 = camel_metric_MetricInstance211
        self.camel_metric_MetricInstance = camel_metric_MetricInstance
        self.camel_metric_MetricInstance205 = camel_metric_MetricInstance205
        self.camel_metric_MetricInstance207 = camel_metric_MetricInstance207
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_metric_MetricInstance209(self):
        return self.__camel_metric_MetricInstance209

    @camel_metric_MetricInstance209.setter
    def camel_metric_MetricInstance209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_MetricInstance__camel_metric_MetricInstance209", None)
        self.__camel_metric_MetricInstance209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetricObjectBinding"):
                opp_val = getattr(old_value, "MetricObjectBinding", None)
                if opp_val == self:
                    setattr(old_value, "MetricObjectBinding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetricObjectBinding"):
                opp_val = getattr(value, "MetricObjectBinding", None)
                setattr(value, "MetricObjectBinding", self)

    @property
    def camel_metric_MetricInstance211(self):
        return self.__camel_metric_MetricInstance211

    @camel_metric_MetricInstance211.setter
    def camel_metric_MetricInstance211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_MetricInstance__camel_metric_MetricInstance211", None)
        self.__camel_metric_MetricInstance211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetricContext212"):
                opp_val = getattr(old_value, "MetricContext212", None)
                if opp_val == self:
                    setattr(old_value, "MetricContext212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetricContext212"):
                opp_val = getattr(value, "MetricContext212", None)
                setattr(value, "MetricContext212", self)

    @property
    def camel_metric_MetricInstance207(self):
        return self.__camel_metric_MetricInstance207

    @camel_metric_MetricInstance207.setter
    def camel_metric_MetricInstance207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_MetricInstance__camel_metric_MetricInstance207", None)
        self.__camel_metric_MetricInstance207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Window"):
                opp_val = getattr(old_value, "Window", None)
                if opp_val == self:
                    setattr(old_value, "Window", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Window"):
                opp_val = getattr(value, "Window", None)
                setattr(value, "Window", self)

    @property
    def camel_metric_MetricInstance(self):
        return self.__camel_metric_MetricInstance

    @camel_metric_MetricInstance.setter
    def camel_metric_MetricInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_MetricInstance__camel_metric_MetricInstance", None)
        self.__camel_metric_MetricInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Metric"):
                opp_val = getattr(old_value, "Metric", None)
                if opp_val == self:
                    setattr(old_value, "Metric", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Metric"):
                opp_val = getattr(value, "Metric", None)
                setattr(value, "Metric", self)

    @property
    def camel_metric_MetricInstance205(self):
        return self.__camel_metric_MetricInstance205

    @camel_metric_MetricInstance205.setter
    def camel_metric_MetricInstance205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_metric_MetricInstance__camel_metric_MetricInstance205", None)
        self.__camel_metric_MetricInstance205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schedule"):
                opp_val = getattr(old_value, "Schedule", None)
                if opp_val == self:
                    setattr(old_value, "Schedule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schedule"):
                opp_val = getattr(value, "Schedule", None)
                setattr(value, "Schedule", self)

    def checkRecursiveness(self, m1: str, m2: str) -> bool:
        # TODO: Implement checkRecursiveness method
        pass

class TimeIntervalUnit:

    pass
class PropertyContext:

    pass
class camel_metric_PropertyCondition(Condition):

    pass
class MetricContext:

    pass
class camel_metric_CompositeMetricContext(MetricContext):

    pass
class camel_metric_RawMetricContext(MetricContext):

    pass
class Location:

    pass
class camel_location_CloudLocation(Location):

    def __init__(self, isAssignable: bool, camel_location_CloudLocation: set["CloudLocation"] = None, camel_location_CloudLocation189: "CloudLocation" = None, camel_location_CloudLocation192: "GeographicalRegion" = None, Location: "camel_organisation_DataCenter", Location427: "camel_requirement_LocationRequirement"):
        self.isAssignable = isAssignable
        self.camel_location_CloudLocation = camel_location_CloudLocation if camel_location_CloudLocation is not None else set()
        self.camel_location_CloudLocation189 = camel_location_CloudLocation189
        self.camel_location_CloudLocation192 = camel_location_CloudLocation192
        
    @property
    def isAssignable(self) -> bool:
        return self.__isAssignable

    @isAssignable.setter
    def isAssignable(self, isAssignable: bool):
        self.__isAssignable = isAssignable

    @property
    def camel_location_CloudLocation192(self):
        return self.__camel_location_CloudLocation192

    @camel_location_CloudLocation192.setter
    def camel_location_CloudLocation192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_location_CloudLocation__camel_location_CloudLocation192", None)
        self.__camel_location_CloudLocation192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GeographicalRegion193"):
                opp_val = getattr(old_value, "GeographicalRegion193", None)
                if opp_val == self:
                    setattr(old_value, "GeographicalRegion193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GeographicalRegion193"):
                opp_val = getattr(value, "GeographicalRegion193", None)
                setattr(value, "GeographicalRegion193", self)

    @property
    def camel_location_CloudLocation(self):
        return self.__camel_location_CloudLocation

    @camel_location_CloudLocation.setter
    def camel_location_CloudLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_location_CloudLocation__camel_location_CloudLocation", None)
        self.__camel_location_CloudLocation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CloudLocation187"):
                    opp_val = getattr(item, "CloudLocation187", None)
                    
                    if opp_val == self:
                        setattr(item, "CloudLocation187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CloudLocation187"):
                    opp_val = getattr(item, "CloudLocation187", None)
                    
                    setattr(item, "CloudLocation187", self)
                    

    @property
    def camel_location_CloudLocation189(self):
        return self.__camel_location_CloudLocation189

    @camel_location_CloudLocation189.setter
    def camel_location_CloudLocation189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_location_CloudLocation__camel_location_CloudLocation189", None)
        self.__camel_location_CloudLocation189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CloudLocation190"):
                opp_val = getattr(old_value, "CloudLocation190", None)
                if opp_val == self:
                    setattr(old_value, "CloudLocation190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CloudLocation190"):
                opp_val = getattr(value, "CloudLocation190", None)
                setattr(value, "CloudLocation190", self)

    def checkRecursiveness(self, cl2: str, cl1: str) -> bool:
        # TODO: Implement checkRecursiveness method
        pass

class camel_location_Location(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class GeographicalRegion:

    pass
class camel_location_Country(GeographicalRegion):

    pass
class camel_location_GeographicalRegion(Location):

    def __init__(self, name: str, alternativeNames: str, camel_location_GeographicalRegion: set["GeographicalRegion"] = None, Location: "camel_organisation_DataCenter", Location427: "camel_requirement_LocationRequirement"):
        self.name = name
        self.alternativeNames = alternativeNames
        self.camel_location_GeographicalRegion = camel_location_GeographicalRegion if camel_location_GeographicalRegion is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alternativeNames(self) -> str:
        return self.__alternativeNames

    @alternativeNames.setter
    def alternativeNames(self, alternativeNames: str):
        self.__alternativeNames = alternativeNames

    @property
    def camel_location_GeographicalRegion(self):
        return self.__camel_location_GeographicalRegion

    @camel_location_GeographicalRegion.setter
    def camel_location_GeographicalRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_location_GeographicalRegion__camel_location_GeographicalRegion", None)
        self.__camel_location_GeographicalRegion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GeographicalRegion195"):
                    opp_val = getattr(item, "GeographicalRegion195", None)
                    
                    if opp_val == self:
                        setattr(item, "GeographicalRegion195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GeographicalRegion195"):
                    opp_val = getattr(item, "GeographicalRegion195", None)
                    
                    setattr(item, "GeographicalRegion195", self)
                    

class camel_execution_RuleTrigger:

    def __init__(self, name: str, trigerringTime: date, camel_execution_RuleTrigger: "ScalabilityRule" = None, camel_execution_RuleTrigger173: set["EventInstance"] = None, camel_execution_RuleTrigger176: set["ActionRealisation"] = None, camel_execution_RuleTrigger179: "ExecutionContext" = None):
        self.name = name
        self.trigerringTime = trigerringTime
        self.camel_execution_RuleTrigger = camel_execution_RuleTrigger
        self.camel_execution_RuleTrigger173 = camel_execution_RuleTrigger173 if camel_execution_RuleTrigger173 is not None else set()
        self.camel_execution_RuleTrigger176 = camel_execution_RuleTrigger176 if camel_execution_RuleTrigger176 is not None else set()
        self.camel_execution_RuleTrigger179 = camel_execution_RuleTrigger179
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trigerringTime(self) -> date:
        return self.__trigerringTime

    @trigerringTime.setter
    def trigerringTime(self, trigerringTime: date):
        self.__trigerringTime = trigerringTime

    @property
    def camel_execution_RuleTrigger173(self):
        return self.__camel_execution_RuleTrigger173

    @camel_execution_RuleTrigger173.setter
    def camel_execution_RuleTrigger173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_RuleTrigger__camel_execution_RuleTrigger173", None)
        self.__camel_execution_RuleTrigger173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EventInstance174"):
                    opp_val = getattr(item, "EventInstance174", None)
                    
                    if opp_val == self:
                        setattr(item, "EventInstance174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EventInstance174"):
                    opp_val = getattr(item, "EventInstance174", None)
                    
                    setattr(item, "EventInstance174", self)
                    

    @property
    def camel_execution_RuleTrigger(self):
        return self.__camel_execution_RuleTrigger

    @camel_execution_RuleTrigger.setter
    def camel_execution_RuleTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_RuleTrigger__camel_execution_RuleTrigger", None)
        self.__camel_execution_RuleTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScalabilityRule"):
                opp_val = getattr(old_value, "ScalabilityRule", None)
                if opp_val == self:
                    setattr(old_value, "ScalabilityRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScalabilityRule"):
                opp_val = getattr(value, "ScalabilityRule", None)
                setattr(value, "ScalabilityRule", self)

    @property
    def camel_execution_RuleTrigger179(self):
        return self.__camel_execution_RuleTrigger179

    @camel_execution_RuleTrigger179.setter
    def camel_execution_RuleTrigger179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_RuleTrigger__camel_execution_RuleTrigger179", None)
        self.__camel_execution_RuleTrigger179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExecutionContext180"):
                opp_val = getattr(old_value, "ExecutionContext180", None)
                if opp_val == self:
                    setattr(old_value, "ExecutionContext180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExecutionContext180"):
                opp_val = getattr(value, "ExecutionContext180", None)
                setattr(value, "ExecutionContext180", self)

    @property
    def camel_execution_RuleTrigger176(self):
        return self.__camel_execution_RuleTrigger176

    @camel_execution_RuleTrigger176.setter
    def camel_execution_RuleTrigger176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_RuleTrigger__camel_execution_RuleTrigger176", None)
        self.__camel_execution_RuleTrigger176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionRealisation177"):
                    opp_val = getattr(item, "ActionRealisation177", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionRealisation177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionRealisation177"):
                    opp_val = getattr(item, "ActionRealisation177", None)
                    
                    setattr(item, "ActionRealisation177", self)
                    

class Country:

    pass
class CloudLocation:

    pass
class ScalabilityRule:

    pass
class ServiceLevelObjective:

    pass
class camel_security_SecuritySLO(ServiceLevelObjective):

    pass
class MetricInstance:

    pass
class camel_metric_CompositeMetricInstance(MetricInstance):

    pass
class camel_metric_RawMetricInstance(MetricInstance):

    pass
class camel_execution_SLOAssessment:

    def __init__(self, name: str, assessment: bool, assessmentTime: date, camel_execution_SLOAssessment: "ServiceLevelObjective" = None, camel_execution_SLOAssessment166: "ExecutionContext" = None, camel_execution_SLOAssessment169: "Measurement" = None):
        self.name = name
        self.assessment = assessment
        self.assessmentTime = assessmentTime
        self.camel_execution_SLOAssessment = camel_execution_SLOAssessment
        self.camel_execution_SLOAssessment166 = camel_execution_SLOAssessment166
        self.camel_execution_SLOAssessment169 = camel_execution_SLOAssessment169
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def assessment(self) -> bool:
        return self.__assessment

    @assessment.setter
    def assessment(self, assessment: bool):
        self.__assessment = assessment

    @property
    def assessmentTime(self) -> date:
        return self.__assessmentTime

    @assessmentTime.setter
    def assessmentTime(self, assessmentTime: date):
        self.__assessmentTime = assessmentTime

    @property
    def camel_execution_SLOAssessment169(self):
        return self.__camel_execution_SLOAssessment169

    @camel_execution_SLOAssessment169.setter
    def camel_execution_SLOAssessment169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_SLOAssessment__camel_execution_SLOAssessment169", None)
        self.__camel_execution_SLOAssessment169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Measurement170"):
                opp_val = getattr(old_value, "Measurement170", None)
                if opp_val == self:
                    setattr(old_value, "Measurement170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Measurement170"):
                opp_val = getattr(value, "Measurement170", None)
                setattr(value, "Measurement170", self)

    @property
    def camel_execution_SLOAssessment166(self):
        return self.__camel_execution_SLOAssessment166

    @camel_execution_SLOAssessment166.setter
    def camel_execution_SLOAssessment166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_SLOAssessment__camel_execution_SLOAssessment166", None)
        self.__camel_execution_SLOAssessment166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExecutionContext167"):
                opp_val = getattr(old_value, "ExecutionContext167", None)
                if opp_val == self:
                    setattr(old_value, "ExecutionContext167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExecutionContext167"):
                opp_val = getattr(value, "ExecutionContext167", None)
                setattr(value, "ExecutionContext167", self)

    @property
    def camel_execution_SLOAssessment(self):
        return self.__camel_execution_SLOAssessment

    @camel_execution_SLOAssessment.setter
    def camel_execution_SLOAssessment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_SLOAssessment__camel_execution_SLOAssessment", None)
        self.__camel_execution_SLOAssessment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ServiceLevelObjective164"):
                opp_val = getattr(old_value, "ServiceLevelObjective164", None)
                if opp_val == self:
                    setattr(old_value, "ServiceLevelObjective164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ServiceLevelObjective164"):
                opp_val = getattr(value, "ServiceLevelObjective164", None)
                setattr(value, "ServiceLevelObjective164", self)

class execution_camel_Action:

    pass
class camel_execution_ActionRealisation:

    def __init__(self, lowLevelActions: str, name: str, startTime: date, endTime: date, camel_execution_ActionRealisation: "execution_camel_Action" = None):
        self.lowLevelActions = lowLevelActions
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.camel_execution_ActionRealisation = camel_execution_ActionRealisation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lowLevelActions(self) -> str:
        return self.__lowLevelActions

    @lowLevelActions.setter
    def lowLevelActions(self, lowLevelActions: str):
        self.__lowLevelActions = lowLevelActions

    @property
    def startTime(self) -> date:
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime: date):
        self.__startTime = startTime

    @property
    def endTime(self) -> date:
        return self.__endTime

    @endTime.setter
    def endTime(self, endTime: date):
        self.__endTime = endTime

    @property
    def camel_execution_ActionRealisation(self):
        return self.__camel_execution_ActionRealisation

    @camel_execution_ActionRealisation.setter
    def camel_execution_ActionRealisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_ActionRealisation__camel_execution_ActionRealisation", None)
        self.__camel_execution_ActionRealisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execution_camel_Action"):
                opp_val = getattr(old_value, "execution_camel_Action", None)
                if opp_val == self:
                    setattr(old_value, "execution_camel_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execution_camel_Action"):
                opp_val = getattr(value, "execution_camel_Action", None)
                setattr(value, "execution_camel_Action", self)

class RuleTrigger:

    pass
class SLOAssessment:

    pass
class Measurement:

    pass
class camel_execution_InternalComponentMeasurement(Measurement):

    pass
class camel_execution_VMMeasurement(Measurement):

    pass
class camel_execution_CommunicationMeasurement(Measurement):

    pass
class camel_execution_ApplicationMeasurement(Measurement):

    pass
class ExecutionContext:

    pass
class EventInstance:

    pass
class ActionRealisation:

    pass
class camel_execution_Measurement:

    def __init__(self, name: str, value: float, rawData: str, measurementTime: date, camel_execution_Measurement: "ExecutionContext" = None, camel_execution_Measurement146: "MetricInstance" = None, camel_execution_Measurement148: "ServiceLevelObjective" = None, camel_execution_Measurement150: "EventInstance" = None):
        self.name = name
        self.value = value
        self.rawData = rawData
        self.measurementTime = measurementTime
        self.camel_execution_Measurement = camel_execution_Measurement
        self.camel_execution_Measurement146 = camel_execution_Measurement146
        self.camel_execution_Measurement148 = camel_execution_Measurement148
        self.camel_execution_Measurement150 = camel_execution_Measurement150
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rawData(self) -> str:
        return self.__rawData

    @rawData.setter
    def rawData(self, rawData: str):
        self.__rawData = rawData

    @property
    def measurementTime(self) -> date:
        return self.__measurementTime

    @measurementTime.setter
    def measurementTime(self, measurementTime: date):
        self.__measurementTime = measurementTime

    @property
    def camel_execution_Measurement148(self):
        return self.__camel_execution_Measurement148

    @camel_execution_Measurement148.setter
    def camel_execution_Measurement148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_Measurement__camel_execution_Measurement148", None)
        self.__camel_execution_Measurement148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ServiceLevelObjective"):
                opp_val = getattr(old_value, "ServiceLevelObjective", None)
                if opp_val == self:
                    setattr(old_value, "ServiceLevelObjective", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ServiceLevelObjective"):
                opp_val = getattr(value, "ServiceLevelObjective", None)
                setattr(value, "ServiceLevelObjective", self)

    @property
    def camel_execution_Measurement146(self):
        return self.__camel_execution_Measurement146

    @camel_execution_Measurement146.setter
    def camel_execution_Measurement146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_Measurement__camel_execution_Measurement146", None)
        self.__camel_execution_Measurement146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetricInstance"):
                opp_val = getattr(old_value, "MetricInstance", None)
                if opp_val == self:
                    setattr(old_value, "MetricInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetricInstance"):
                opp_val = getattr(value, "MetricInstance", None)
                setattr(value, "MetricInstance", self)

    @property
    def camel_execution_Measurement150(self):
        return self.__camel_execution_Measurement150

    @camel_execution_Measurement150.setter
    def camel_execution_Measurement150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_Measurement__camel_execution_Measurement150", None)
        self.__camel_execution_Measurement150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventInstance151"):
                opp_val = getattr(old_value, "EventInstance151", None)
                if opp_val == self:
                    setattr(old_value, "EventInstance151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventInstance151"):
                opp_val = getattr(value, "EventInstance151", None)
                setattr(value, "EventInstance151", self)

    @property
    def camel_execution_Measurement(self):
        return self.__camel_execution_Measurement

    @camel_execution_Measurement.setter
    def camel_execution_Measurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_Measurement__camel_execution_Measurement", None)
        self.__camel_execution_Measurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExecutionContext144"):
                opp_val = getattr(old_value, "ExecutionContext144", None)
                if opp_val == self:
                    setattr(old_value, "ExecutionContext144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExecutionContext144"):
                opp_val = getattr(value, "ExecutionContext144", None)
                setattr(value, "ExecutionContext144", self)

class RequirementGroup:

    pass
class MonetaryUnit:

    pass
class execution_camel_Application:

    pass
class camel_execution_ExecutionContext:

    def __init__(self, name: str, startTime: date, endTime: date, totalCost: float, camel_execution_ExecutionContext: "execution_camel_Application" = None, camel_execution_ExecutionContext137: "MonetaryUnit" = None, camel_execution_ExecutionContext139: "DeploymentModel" = None, camel_execution_ExecutionContext142: "RequirementGroup" = None):
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.totalCost = totalCost
        self.camel_execution_ExecutionContext = camel_execution_ExecutionContext
        self.camel_execution_ExecutionContext137 = camel_execution_ExecutionContext137
        self.camel_execution_ExecutionContext139 = camel_execution_ExecutionContext139
        self.camel_execution_ExecutionContext142 = camel_execution_ExecutionContext142
        
    @property
    def endTime(self) -> date:
        return self.__endTime

    @endTime.setter
    def endTime(self, endTime: date):
        self.__endTime = endTime

    @property
    def totalCost(self) -> float:
        return self.__totalCost

    @totalCost.setter
    def totalCost(self, totalCost: float):
        self.__totalCost = totalCost

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def startTime(self) -> date:
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime: date):
        self.__startTime = startTime

    @property
    def camel_execution_ExecutionContext139(self):
        return self.__camel_execution_ExecutionContext139

    @camel_execution_ExecutionContext139.setter
    def camel_execution_ExecutionContext139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_ExecutionContext__camel_execution_ExecutionContext139", None)
        self.__camel_execution_ExecutionContext139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeploymentModel140"):
                opp_val = getattr(old_value, "DeploymentModel140", None)
                if opp_val == self:
                    setattr(old_value, "DeploymentModel140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeploymentModel140"):
                opp_val = getattr(value, "DeploymentModel140", None)
                setattr(value, "DeploymentModel140", self)

    @property
    def camel_execution_ExecutionContext(self):
        return self.__camel_execution_ExecutionContext

    @camel_execution_ExecutionContext.setter
    def camel_execution_ExecutionContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_ExecutionContext__camel_execution_ExecutionContext", None)
        self.__camel_execution_ExecutionContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "execution_camel_Application"):
                opp_val = getattr(old_value, "execution_camel_Application", None)
                if opp_val == self:
                    setattr(old_value, "execution_camel_Application", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "execution_camel_Application"):
                opp_val = getattr(value, "execution_camel_Application", None)
                setattr(value, "execution_camel_Application", self)

    @property
    def camel_execution_ExecutionContext142(self):
        return self.__camel_execution_ExecutionContext142

    @camel_execution_ExecutionContext142.setter
    def camel_execution_ExecutionContext142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_ExecutionContext__camel_execution_ExecutionContext142", None)
        self.__camel_execution_ExecutionContext142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequirementGroup"):
                opp_val = getattr(old_value, "RequirementGroup", None)
                if opp_val == self:
                    setattr(old_value, "RequirementGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequirementGroup"):
                opp_val = getattr(value, "RequirementGroup", None)
                setattr(value, "RequirementGroup", self)

    @property
    def camel_execution_ExecutionContext137(self):
        return self.__camel_execution_ExecutionContext137

    @camel_execution_ExecutionContext137.setter
    def camel_execution_ExecutionContext137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_execution_ExecutionContext__camel_execution_ExecutionContext137", None)
        self.__camel_execution_ExecutionContext137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MonetaryUnit"):
                opp_val = getattr(old_value, "MonetaryUnit", None)
                if opp_val == self:
                    setattr(old_value, "MonetaryUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MonetaryUnit"):
                opp_val = getattr(value, "MonetaryUnit", None)
                setattr(value, "MonetaryUnit", self)

class SingleValue:

    pass
class camel_type_StringsValue(SingleValue):

    def __init__(self, value: str, SingleValue: "camel_deployment_VMInstance", SingleValue217: "camel_metric_MetricFormulaParameter", SingleValue531: "camel_type_List", SingleValue358: "camel_provider_AttributeConstraint", SingleValue347: "camel_provider_Attribute", SingleValue361: "camel_provider_AttributeConstraint", SingleValue525: "camel_type_TypeModel"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class camel_type_EnumerateValue(SingleValue):

    def __init__(self, name: str, value: int, SingleValue: "camel_deployment_VMInstance", SingleValue217: "camel_metric_MetricFormulaParameter", SingleValue531: "camel_type_List", SingleValue358: "camel_provider_AttributeConstraint", SingleValue347: "camel_provider_Attribute", SingleValue361: "camel_provider_AttributeConstraint", SingleValue525: "camel_type_TypeModel"):
        self.name = name
        self.value = value
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class camel_type_NumericValue(SingleValue):

    pass
class camel_type_BoolValue(SingleValue):

    def __init__(self, value: bool, SingleValue: "camel_deployment_VMInstance", SingleValue217: "camel_metric_MetricFormulaParameter", SingleValue531: "camel_type_List", SingleValue358: "camel_provider_AttributeConstraint", SingleValue347: "camel_provider_Attribute", SingleValue361: "camel_provider_AttributeConstraint", SingleValue525: "camel_type_TypeModel"):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class Attribute:

    pass
class HostingPortInstance:

    pass
class camel_deployment_RequiredHostInstance(HostingPortInstance):

    pass
class camel_deployment_ProvidedHostInstance(HostingPortInstance):

    pass
class CommunicationPortInstance:

    pass
class camel_deployment_RequiredCommunicationInstance(CommunicationPortInstance):

    pass
class camel_deployment_ProvidedCommunicationInstance(CommunicationPortInstance):

    pass
class ProvidedHostInstance:

    pass
class ProvidedCommunicationInstance:

    pass
class RequiredHostInstance:

    pass
class RequiredCommunicationInstance:

    pass
class ComponentInstance:

    pass
class camel_deployment_VMInstance(ComponentInstance):

    def __init__(self, ip: str, camel_deployment_VMInstance: "Attribute" = None, camel_deployment_VMInstance104: "SingleValue" = None, ComponentInstance: "camel_metric_MetricComponentBinding"):
        self.ip = ip
        self.camel_deployment_VMInstance = camel_deployment_VMInstance
        self.camel_deployment_VMInstance104 = camel_deployment_VMInstance104
        
    @property
    def ip(self) -> str:
        return self.__ip

    @ip.setter
    def ip(self, ip: str):
        self.__ip = ip

    @property
    def camel_deployment_VMInstance104(self):
        return self.__camel_deployment_VMInstance104

    @camel_deployment_VMInstance104.setter
    def camel_deployment_VMInstance104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_VMInstance__camel_deployment_VMInstance104", None)
        self.__camel_deployment_VMInstance104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleValue"):
                opp_val = getattr(old_value, "SingleValue", None)
                if opp_val == self:
                    setattr(old_value, "SingleValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleValue"):
                opp_val = getattr(value, "SingleValue", None)
                setattr(value, "SingleValue", self)

    @property
    def camel_deployment_VMInstance(self):
        return self.__camel_deployment_VMInstance

    @camel_deployment_VMInstance.setter
    def camel_deployment_VMInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_VMInstance__camel_deployment_VMInstance", None)
        self.__camel_deployment_VMInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute"):
                opp_val = getattr(old_value, "Attribute", None)
                if opp_val == self:
                    setattr(old_value, "Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute"):
                opp_val = getattr(value, "Attribute", None)
                setattr(value, "Attribute", self)

    def checkDates(self, vm: str) -> bool:
        # TODO: Implement checkDates method
        pass

class camel_deployment_InternalComponentInstance(ComponentInstance):

    pass
class HostingPort:

    pass
class camel_deployment_RequiredHost(HostingPort):

    pass
class camel_deployment_ProvidedHost(HostingPort):

    pass
class CommunicationPort:

    pass
class camel_deployment_RequiredCommunication(CommunicationPort):

    def __init__(self, isMandatory: bool, CommunicationPort: "camel_deployment_CommunicationPortInstance"):
        self.isMandatory = isMandatory
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

class camel_deployment_ProvidedCommunication(CommunicationPort):

    pass
class camel_deployment_VMRequirementSet:

    def __init__(self, name: str, camel_deployment_VMRequirementSet: "LocationRequirement" = None, camel_deployment_VMRequirementSet65: "ProviderRequirement" = None, camel_deployment_VMRequirementSet67: "QualitativeHardwareRequirement" = None, camel_deployment_VMRequirementSet69: "QuantitativeHardwareRequirement" = None, camel_deployment_VMRequirementSet71: "OSOrImageRequirement" = None):
        self.name = name
        self.camel_deployment_VMRequirementSet = camel_deployment_VMRequirementSet
        self.camel_deployment_VMRequirementSet65 = camel_deployment_VMRequirementSet65
        self.camel_deployment_VMRequirementSet67 = camel_deployment_VMRequirementSet67
        self.camel_deployment_VMRequirementSet69 = camel_deployment_VMRequirementSet69
        self.camel_deployment_VMRequirementSet71 = camel_deployment_VMRequirementSet71
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_deployment_VMRequirementSet67(self):
        return self.__camel_deployment_VMRequirementSet67

    @camel_deployment_VMRequirementSet67.setter
    def camel_deployment_VMRequirementSet67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_VMRequirementSet__camel_deployment_VMRequirementSet67", None)
        self.__camel_deployment_VMRequirementSet67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualitativeHardwareRequirement"):
                opp_val = getattr(old_value, "QualitativeHardwareRequirement", None)
                if opp_val == self:
                    setattr(old_value, "QualitativeHardwareRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualitativeHardwareRequirement"):
                opp_val = getattr(value, "QualitativeHardwareRequirement", None)
                setattr(value, "QualitativeHardwareRequirement", self)

    @property
    def camel_deployment_VMRequirementSet69(self):
        return self.__camel_deployment_VMRequirementSet69

    @camel_deployment_VMRequirementSet69.setter
    def camel_deployment_VMRequirementSet69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_VMRequirementSet__camel_deployment_VMRequirementSet69", None)
        self.__camel_deployment_VMRequirementSet69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QuantitativeHardwareRequirement"):
                opp_val = getattr(old_value, "QuantitativeHardwareRequirement", None)
                if opp_val == self:
                    setattr(old_value, "QuantitativeHardwareRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QuantitativeHardwareRequirement"):
                opp_val = getattr(value, "QuantitativeHardwareRequirement", None)
                setattr(value, "QuantitativeHardwareRequirement", self)

    @property
    def camel_deployment_VMRequirementSet(self):
        return self.__camel_deployment_VMRequirementSet

    @camel_deployment_VMRequirementSet.setter
    def camel_deployment_VMRequirementSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_VMRequirementSet__camel_deployment_VMRequirementSet", None)
        self.__camel_deployment_VMRequirementSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LocationRequirement"):
                opp_val = getattr(old_value, "LocationRequirement", None)
                if opp_val == self:
                    setattr(old_value, "LocationRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LocationRequirement"):
                opp_val = getattr(value, "LocationRequirement", None)
                setattr(value, "LocationRequirement", self)

    @property
    def camel_deployment_VMRequirementSet71(self):
        return self.__camel_deployment_VMRequirementSet71

    @camel_deployment_VMRequirementSet71.setter
    def camel_deployment_VMRequirementSet71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_VMRequirementSet__camel_deployment_VMRequirementSet71", None)
        self.__camel_deployment_VMRequirementSet71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OSOrImageRequirement"):
                opp_val = getattr(old_value, "OSOrImageRequirement", None)
                if opp_val == self:
                    setattr(old_value, "OSOrImageRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OSOrImageRequirement"):
                opp_val = getattr(value, "OSOrImageRequirement", None)
                setattr(value, "OSOrImageRequirement", self)

    @property
    def camel_deployment_VMRequirementSet65(self):
        return self.__camel_deployment_VMRequirementSet65

    @camel_deployment_VMRequirementSet65.setter
    def camel_deployment_VMRequirementSet65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_VMRequirementSet__camel_deployment_VMRequirementSet65", None)
        self.__camel_deployment_VMRequirementSet65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProviderRequirement"):
                opp_val = getattr(old_value, "ProviderRequirement", None)
                if opp_val == self:
                    setattr(old_value, "ProviderRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProviderRequirement"):
                opp_val = getattr(value, "ProviderRequirement", None)
                setattr(value, "ProviderRequirement", self)

class RequiredHost:

    pass
class OSOrImageRequirement:

    pass
class camel_requirement_OSRequirement(OSOrImageRequirement):

    def __init__(self, os: str, is64os: bool, OSOrImageRequirement: "camel_deployment_VMRequirementSet"):
        self.os = os
        self.is64os = is64os
        
    @property
    def os(self) -> str:
        return self.__os

    @os.setter
    def os(self, os: str):
        self.__os = os

    @property
    def is64os(self) -> bool:
        return self.__is64os

    @is64os.setter
    def is64os(self, is64os: bool):
        self.__is64os = is64os

class camel_requirement_ImageRequirement(OSOrImageRequirement):

    def __init__(self, imageId: str, OSOrImageRequirement: "camel_deployment_VMRequirementSet"):
        self.imageId = imageId
        
    @property
    def imageId(self) -> str:
        return self.__imageId

    @imageId.setter
    def imageId(self, imageId: str):
        self.__imageId = imageId

class QuantitativeHardwareRequirement:

    pass
class QualitativeHardwareRequirement:

    pass
class ProviderRequirement:

    pass
class LocationRequirement:

    pass
class Configuration:

    pass
class ProvidedHost:

    pass
class ProvidedCommunication:

    pass
class DeploymentElement:

    pass
class camel_deployment_HostingPortInstance(DeploymentElement):

    pass
class camel_deployment_Communication(DeploymentElement):

    def __init__(self, type: str, camel_deployment_Communication81: "Configuration" = None, camel_deployment_Communication: "ProvidedCommunication" = None, camel_deployment_Communication75: "RequiredCommunication" = None, camel_deployment_Communication78: "Configuration" = None):
        self.type = type
        self.camel_deployment_Communication81 = camel_deployment_Communication81
        self.camel_deployment_Communication = camel_deployment_Communication
        self.camel_deployment_Communication75 = camel_deployment_Communication75
        self.camel_deployment_Communication78 = camel_deployment_Communication78
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def camel_deployment_Communication81(self):
        return self.__camel_deployment_Communication81

    @camel_deployment_Communication81.setter
    def camel_deployment_Communication81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_Communication__camel_deployment_Communication81", None)
        self.__camel_deployment_Communication81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Configuration82"):
                opp_val = getattr(old_value, "Configuration82", None)
                if opp_val == self:
                    setattr(old_value, "Configuration82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Configuration82"):
                opp_val = getattr(value, "Configuration82", None)
                setattr(value, "Configuration82", self)

    @property
    def camel_deployment_Communication75(self):
        return self.__camel_deployment_Communication75

    @camel_deployment_Communication75.setter
    def camel_deployment_Communication75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_Communication__camel_deployment_Communication75", None)
        self.__camel_deployment_Communication75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredCommunication76"):
                opp_val = getattr(old_value, "RequiredCommunication76", None)
                if opp_val == self:
                    setattr(old_value, "RequiredCommunication76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredCommunication76"):
                opp_val = getattr(value, "RequiredCommunication76", None)
                setattr(value, "RequiredCommunication76", self)

    @property
    def camel_deployment_Communication78(self):
        return self.__camel_deployment_Communication78

    @camel_deployment_Communication78.setter
    def camel_deployment_Communication78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_Communication__camel_deployment_Communication78", None)
        self.__camel_deployment_Communication78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Configuration79"):
                opp_val = getattr(old_value, "Configuration79", None)
                if opp_val == self:
                    setattr(old_value, "Configuration79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Configuration79"):
                opp_val = getattr(value, "Configuration79", None)
                setattr(value, "Configuration79", self)

    @property
    def camel_deployment_Communication(self):
        return self.__camel_deployment_Communication

    @camel_deployment_Communication.setter
    def camel_deployment_Communication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_Communication__camel_deployment_Communication", None)
        self.__camel_deployment_Communication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedCommunication73"):
                opp_val = getattr(old_value, "ProvidedCommunication73", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedCommunication73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedCommunication73"):
                opp_val = getattr(value, "ProvidedCommunication73", None)
                setattr(value, "ProvidedCommunication73", self)

class camel_deployment_CommunicationPortInstance(DeploymentElement):

    pass
class camel_deployment_CommunicationInstance(DeploymentElement):

    pass
class camel_deployment_CommunicationPort(DeploymentElement):

    def __init__(self, portNumber: int):
        self.portNumber = portNumber
        
    @property
    def portNumber(self) -> int:
        return self.__portNumber

    @portNumber.setter
    def portNumber(self, portNumber: int):
        self.__portNumber = portNumber

class camel_deployment_ComponentInstance(DeploymentElement):

    def __init__(self, instantiatedOn: date, destroyedOn: date, camel_deployment_ComponentInstance: "Component" = None, camel_deployment_ComponentInstance96: set["ProvidedCommunicationInstance"] = None, camel_deployment_ComponentInstance98: set["ProvidedHostInstance"] = None):
        self.instantiatedOn = instantiatedOn
        self.destroyedOn = destroyedOn
        self.camel_deployment_ComponentInstance = camel_deployment_ComponentInstance
        self.camel_deployment_ComponentInstance96 = camel_deployment_ComponentInstance96 if camel_deployment_ComponentInstance96 is not None else set()
        self.camel_deployment_ComponentInstance98 = camel_deployment_ComponentInstance98 if camel_deployment_ComponentInstance98 is not None else set()
        
    @property
    def destroyedOn(self) -> date:
        return self.__destroyedOn

    @destroyedOn.setter
    def destroyedOn(self, destroyedOn: date):
        self.__destroyedOn = destroyedOn

    @property
    def instantiatedOn(self) -> date:
        return self.__instantiatedOn

    @instantiatedOn.setter
    def instantiatedOn(self, instantiatedOn: date):
        self.__instantiatedOn = instantiatedOn

    @property
    def camel_deployment_ComponentInstance98(self):
        return self.__camel_deployment_ComponentInstance98

    @camel_deployment_ComponentInstance98.setter
    def camel_deployment_ComponentInstance98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_ComponentInstance__camel_deployment_ComponentInstance98", None)
        self.__camel_deployment_ComponentInstance98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProvidedHostInstance"):
                    opp_val = getattr(item, "ProvidedHostInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "ProvidedHostInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProvidedHostInstance"):
                    opp_val = getattr(item, "ProvidedHostInstance", None)
                    
                    setattr(item, "ProvidedHostInstance", self)
                    

    @property
    def camel_deployment_ComponentInstance(self):
        return self.__camel_deployment_ComponentInstance

    @camel_deployment_ComponentInstance.setter
    def camel_deployment_ComponentInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_ComponentInstance__camel_deployment_ComponentInstance", None)
        self.__camel_deployment_ComponentInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Component"):
                opp_val = getattr(old_value, "Component", None)
                if opp_val == self:
                    setattr(old_value, "Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component"):
                opp_val = getattr(value, "Component", None)
                setattr(value, "Component", self)

    @property
    def camel_deployment_ComponentInstance96(self):
        return self.__camel_deployment_ComponentInstance96

    @camel_deployment_ComponentInstance96.setter
    def camel_deployment_ComponentInstance96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_ComponentInstance__camel_deployment_ComponentInstance96", None)
        self.__camel_deployment_ComponentInstance96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProvidedCommunicationInstance"):
                    opp_val = getattr(item, "ProvidedCommunicationInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "ProvidedCommunicationInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProvidedCommunicationInstance"):
                    opp_val = getattr(item, "ProvidedCommunicationInstance", None)
                    
                    setattr(item, "ProvidedCommunicationInstance", self)
                    

class camel_deployment_Configuration(DeploymentElement):

    def __init__(self, downloadCommand: str, uploadCommand: str, installCommand: str, configureCommand: str, startCommand: str, stopCommand: str):
        self.downloadCommand = downloadCommand
        self.uploadCommand = uploadCommand
        self.installCommand = installCommand
        self.configureCommand = configureCommand
        self.startCommand = startCommand
        self.stopCommand = stopCommand
        
    @property
    def downloadCommand(self) -> str:
        return self.__downloadCommand

    @downloadCommand.setter
    def downloadCommand(self, downloadCommand: str):
        self.__downloadCommand = downloadCommand

    @property
    def configureCommand(self) -> str:
        return self.__configureCommand

    @configureCommand.setter
    def configureCommand(self, configureCommand: str):
        self.__configureCommand = configureCommand

    @property
    def uploadCommand(self) -> str:
        return self.__uploadCommand

    @uploadCommand.setter
    def uploadCommand(self, uploadCommand: str):
        self.__uploadCommand = uploadCommand

    @property
    def startCommand(self) -> str:
        return self.__startCommand

    @startCommand.setter
    def startCommand(self, startCommand: str):
        self.__startCommand = startCommand

    @property
    def stopCommand(self) -> str:
        return self.__stopCommand

    @stopCommand.setter
    def stopCommand(self, stopCommand: str):
        self.__stopCommand = stopCommand

    @property
    def installCommand(self) -> str:
        return self.__installCommand

    @installCommand.setter
    def installCommand(self, installCommand: str):
        self.__installCommand = installCommand

class camel_deployment_HostingPort(DeploymentElement):

    pass
class camel_deployment_Hosting(DeploymentElement):

    pass
class camel_deployment_HostingInstance(DeploymentElement):

    pass
class camel_deployment_Component(DeploymentElement):

    pass
class VMRequirementSet:

    pass
class HostingInstance:

    pass
class RequiredCommunication:

    pass
class Hosting:

    pass
class Component:

    pass
class camel_deployment_VM(Component):

    pass
class camel_deployment_InternalComponent(Component):

    def __init__(self, version: str, camel_deployment_InternalComponent: set["InternalComponent"] = None, camel_deployment_InternalComponent58: set["RequiredCommunication"] = None, camel_deployment_InternalComponent60: "RequiredHost" = None, Component: "camel_deployment_ComponentInstance", Component413: "camel_requirement_OptimisationRequirement", Component243: "camel_metric_ConditionContext"):
        self.version = version
        self.camel_deployment_InternalComponent = camel_deployment_InternalComponent if camel_deployment_InternalComponent is not None else set()
        self.camel_deployment_InternalComponent58 = camel_deployment_InternalComponent58 if camel_deployment_InternalComponent58 is not None else set()
        self.camel_deployment_InternalComponent60 = camel_deployment_InternalComponent60
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def camel_deployment_InternalComponent58(self):
        return self.__camel_deployment_InternalComponent58

    @camel_deployment_InternalComponent58.setter
    def camel_deployment_InternalComponent58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_InternalComponent__camel_deployment_InternalComponent58", None)
        self.__camel_deployment_InternalComponent58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequiredCommunication"):
                    opp_val = getattr(item, "RequiredCommunication", None)
                    
                    if opp_val == self:
                        setattr(item, "RequiredCommunication", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequiredCommunication"):
                    opp_val = getattr(item, "RequiredCommunication", None)
                    
                    setattr(item, "RequiredCommunication", self)
                    

    @property
    def camel_deployment_InternalComponent60(self):
        return self.__camel_deployment_InternalComponent60

    @camel_deployment_InternalComponent60.setter
    def camel_deployment_InternalComponent60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_InternalComponent__camel_deployment_InternalComponent60", None)
        self.__camel_deployment_InternalComponent60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredHost"):
                opp_val = getattr(old_value, "RequiredHost", None)
                if opp_val == self:
                    setattr(old_value, "RequiredHost", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredHost"):
                opp_val = getattr(value, "RequiredHost", None)
                setattr(value, "RequiredHost", self)

    @property
    def camel_deployment_InternalComponent(self):
        return self.__camel_deployment_InternalComponent

    @camel_deployment_InternalComponent.setter
    def camel_deployment_InternalComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_deployment_InternalComponent__camel_deployment_InternalComponent", None)
        self.__camel_deployment_InternalComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InternalComponent56"):
                    opp_val = getattr(item, "InternalComponent56", None)
                    
                    if opp_val == self:
                        setattr(item, "InternalComponent56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InternalComponent56"):
                    opp_val = getattr(item, "InternalComponent56", None)
                    
                    setattr(item, "InternalComponent56", self)
                    

    def contains(self, ic: str, rc: str) -> bool:
        # TODO: Implement contains method
        pass

class InternalComponentInstance:

    pass
class InternalComponent:

    pass
class camel_deployment_DeploymentElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class CommunicationInstance:

    pass
class Communication:

    pass
class VMInstance:

    pass
class Entity:

    pass
class camel_organisation_User(Entity):

    def __init__(self, name: str, email: str, firstName: str, lastName: str, www: str, camel_organisation_User: set["ExternalIdentifier"] = None, camel_organisation_User319: set["RequirementModel"] = None, camel_organisation_User322: set["CloudCredentials"] = None, camel_organisation_User324: set["DeploymentModel"] = None, camel_organisation_User327: "PaaSageCredentials" = None, Entity: "camel_Application", Entity467: "camel_scalability_ScalabilityRule"):
        self.name = name
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.www = www
        self.camel_organisation_User = camel_organisation_User if camel_organisation_User is not None else set()
        self.camel_organisation_User319 = camel_organisation_User319 if camel_organisation_User319 is not None else set()
        self.camel_organisation_User322 = camel_organisation_User322 if camel_organisation_User322 is not None else set()
        self.camel_organisation_User324 = camel_organisation_User324 if camel_organisation_User324 is not None else set()
        self.camel_organisation_User327 = camel_organisation_User327
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def www(self) -> str:
        return self.__www

    @www.setter
    def www(self, www: str):
        self.__www = www

    @property
    def camel_organisation_User324(self):
        return self.__camel_organisation_User324

    @camel_organisation_User324.setter
    def camel_organisation_User324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_User__camel_organisation_User324", None)
        self.__camel_organisation_User324 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DeploymentModel325"):
                    opp_val = getattr(item, "DeploymentModel325", None)
                    
                    if opp_val == self:
                        setattr(item, "DeploymentModel325", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DeploymentModel325"):
                    opp_val = getattr(item, "DeploymentModel325", None)
                    
                    setattr(item, "DeploymentModel325", self)
                    

    @property
    def camel_organisation_User(self):
        return self.__camel_organisation_User

    @camel_organisation_User.setter
    def camel_organisation_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_User__camel_organisation_User", None)
        self.__camel_organisation_User = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExternalIdentifier317"):
                    opp_val = getattr(item, "ExternalIdentifier317", None)
                    
                    if opp_val == self:
                        setattr(item, "ExternalIdentifier317", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExternalIdentifier317"):
                    opp_val = getattr(item, "ExternalIdentifier317", None)
                    
                    setattr(item, "ExternalIdentifier317", self)
                    

    @property
    def camel_organisation_User319(self):
        return self.__camel_organisation_User319

    @camel_organisation_User319.setter
    def camel_organisation_User319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_User__camel_organisation_User319", None)
        self.__camel_organisation_User319 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequirementModel320"):
                    opp_val = getattr(item, "RequirementModel320", None)
                    
                    if opp_val == self:
                        setattr(item, "RequirementModel320", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequirementModel320"):
                    opp_val = getattr(item, "RequirementModel320", None)
                    
                    setattr(item, "RequirementModel320", self)
                    

    @property
    def camel_organisation_User322(self):
        return self.__camel_organisation_User322

    @camel_organisation_User322.setter
    def camel_organisation_User322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_User__camel_organisation_User322", None)
        self.__camel_organisation_User322 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CloudCredentials"):
                    opp_val = getattr(item, "CloudCredentials", None)
                    
                    if opp_val == self:
                        setattr(item, "CloudCredentials", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CloudCredentials"):
                    opp_val = getattr(item, "CloudCredentials", None)
                    
                    setattr(item, "CloudCredentials", self)
                    

    @property
    def camel_organisation_User327(self):
        return self.__camel_organisation_User327

    @camel_organisation_User327.setter
    def camel_organisation_User327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_User__camel_organisation_User327", None)
        self.__camel_organisation_User327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PaaSageCredentials"):
                opp_val = getattr(old_value, "PaaSageCredentials", None)
                if opp_val == self:
                    setattr(old_value, "PaaSageCredentials", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PaaSageCredentials"):
                opp_val = getattr(value, "PaaSageCredentials", None)
                setattr(value, "PaaSageCredentials", self)

class camel_organisation_Organisation(Entity):

    def __init__(self, name: str, www: str, postalAddress: str, email: str, Entity: "camel_Application", Entity467: "camel_scalability_ScalabilityRule"):
        self.name = name
        self.www = www
        self.postalAddress = postalAddress
        self.email = email
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def www(self) -> str:
        return self.__www

    @www.setter
    def www(self, www: str):
        self.__www = www

    @property
    def postalAddress(self) -> str:
        return self.__postalAddress

    @postalAddress.setter
    def postalAddress(self, postalAddress: str):
        self.__postalAddress = postalAddress

class VM:

    pass
class UnitModel:

    pass
class TypeModel:

    pass
class DeploymentModel:

    pass
class SecurityModel:

    pass
class ScalabilityModel:

    pass
class RequirementModel:

    pass
class ProviderModel:

    pass
class OrganisationModel:

    pass
class MetricModel:

    pass
class LocationModel:

    pass
class ExecutionModel:

    pass
class camel_Application:

    def __init__(self, name: str, version: str, description: str, camel_Application: "camel_CamelModel" = None, camel_Application26: "Entity" = None, camel_Application28: set["DeploymentModel"] = None):
        self.name = name
        self.version = version
        self.description = description
        self.camel_Application = camel_Application
        self.camel_Application26 = camel_Application26
        self.camel_Application28 = camel_Application28 if camel_Application28 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def camel_Application28(self):
        return self.__camel_Application28

    @camel_Application28.setter
    def camel_Application28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_Application__camel_Application28", None)
        self.__camel_Application28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DeploymentModel29"):
                    opp_val = getattr(item, "DeploymentModel29", None)
                    
                    if opp_val == self:
                        setattr(item, "DeploymentModel29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DeploymentModel29"):
                    opp_val = getattr(item, "DeploymentModel29", None)
                    
                    setattr(item, "DeploymentModel29", self)
                    

    @property
    def camel_Application26(self):
        return self.__camel_Application26

    @camel_Application26.setter
    def camel_Application26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_Application__camel_Application26", None)
        self.__camel_Application26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity"):
                opp_val = getattr(old_value, "Entity", None)
                if opp_val == self:
                    setattr(old_value, "Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity"):
                opp_val = getattr(value, "Entity", None)
                setattr(value, "Entity", self)

    @property
    def camel_Application(self):
        return self.__camel_Application

    @camel_Application.setter
    def camel_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_Application__camel_Application", None)
        self.__camel_Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "camel_CamelModel2"):
                opp_val = getattr(old_value, "camel_CamelModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "camel_CamelModel2"):
                opp_val = getattr(value, "camel_CamelModel2", None)
                if opp_val is None:
                    setattr(value, "camel_CamelModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class camel_Action:

    def __init__(self, name: str, type: str, camel_Action: "camel_CamelModel" = None):
        self.name = name
        self.type = type
        self.camel_Action = camel_Action
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def camel_Action(self):
        return self.__camel_Action

    @camel_Action.setter
    def camel_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_Action__camel_Action", None)
        self.__camel_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "camel_CamelModel"):
                opp_val = getattr(old_value, "camel_CamelModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "camel_CamelModel"):
                opp_val = getattr(value, "camel_CamelModel", None)
                if opp_val is None:
                    setattr(value, "camel_CamelModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Model:

    pass
class camel_metric_MetricModel(Model):

    pass
class camel_location_LocationModel(Model):

    pass
class camel_scalability_ScalabilityModel(Model):

    pass
class camel_requirement_RequirementModel(Model):

    pass
class camel_type_TypeModel(Model):

    pass
class camel_provider_ProviderModel(Model):

    pass
class camel_security_SecurityModel(Model):

    pass
class camel_organisation_OrganisationModel(Model):

    def __init__(self, securityLevel: str, camel_organisation_OrganisationModel300: set["DataCenter"] = None, camel_organisation_OrganisationModel302: set["Role"] = None, camel_organisation_OrganisationModel304: set["RoleAssignment"] = None, camel_organisation_OrganisationModel306: set["Permission"] = None, camel_organisation_OrganisationModel308: set["ResourceFilter"] = None, camel_organisation_OrganisationModel: "Organisation" = None, camel_organisation_OrganisationModel292: "CloudProvider" = None, camel_organisation_OrganisationModel294: set["ExternalIdentifier"] = None, camel_organisation_OrganisationModel296: set["User"] = None, camel_organisation_OrganisationModel298: set["UserGroup"] = None):
        self.securityLevel = securityLevel
        self.camel_organisation_OrganisationModel300 = camel_organisation_OrganisationModel300 if camel_organisation_OrganisationModel300 is not None else set()
        self.camel_organisation_OrganisationModel302 = camel_organisation_OrganisationModel302 if camel_organisation_OrganisationModel302 is not None else set()
        self.camel_organisation_OrganisationModel304 = camel_organisation_OrganisationModel304 if camel_organisation_OrganisationModel304 is not None else set()
        self.camel_organisation_OrganisationModel306 = camel_organisation_OrganisationModel306 if camel_organisation_OrganisationModel306 is not None else set()
        self.camel_organisation_OrganisationModel308 = camel_organisation_OrganisationModel308 if camel_organisation_OrganisationModel308 is not None else set()
        self.camel_organisation_OrganisationModel = camel_organisation_OrganisationModel
        self.camel_organisation_OrganisationModel292 = camel_organisation_OrganisationModel292
        self.camel_organisation_OrganisationModel294 = camel_organisation_OrganisationModel294 if camel_organisation_OrganisationModel294 is not None else set()
        self.camel_organisation_OrganisationModel296 = camel_organisation_OrganisationModel296 if camel_organisation_OrganisationModel296 is not None else set()
        self.camel_organisation_OrganisationModel298 = camel_organisation_OrganisationModel298 if camel_organisation_OrganisationModel298 is not None else set()
        
    @property
    def securityLevel(self) -> str:
        return self.__securityLevel

    @securityLevel.setter
    def securityLevel(self, securityLevel: str):
        self.__securityLevel = securityLevel

    @property
    def camel_organisation_OrganisationModel298(self):
        return self.__camel_organisation_OrganisationModel298

    @camel_organisation_OrganisationModel298.setter
    def camel_organisation_OrganisationModel298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_OrganisationModel__camel_organisation_OrganisationModel298", None)
        self.__camel_organisation_OrganisationModel298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UserGroup"):
                    opp_val = getattr(item, "UserGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "UserGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UserGroup"):
                    opp_val = getattr(item, "UserGroup", None)
                    
                    setattr(item, "UserGroup", self)
                    

    @property
    def camel_organisation_OrganisationModel294(self):
        return self.__camel_organisation_OrganisationModel294

    @camel_organisation_OrganisationModel294.setter
    def camel_organisation_OrganisationModel294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_OrganisationModel__camel_organisation_OrganisationModel294", None)
        self.__camel_organisation_OrganisationModel294 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExternalIdentifier"):
                    opp_val = getattr(item, "ExternalIdentifier", None)
                    
                    if opp_val == self:
                        setattr(item, "ExternalIdentifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExternalIdentifier"):
                    opp_val = getattr(item, "ExternalIdentifier", None)
                    
                    setattr(item, "ExternalIdentifier", self)
                    

    @property
    def camel_organisation_OrganisationModel302(self):
        return self.__camel_organisation_OrganisationModel302

    @camel_organisation_OrganisationModel302.setter
    def camel_organisation_OrganisationModel302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_OrganisationModel__camel_organisation_OrganisationModel302", None)
        self.__camel_organisation_OrganisationModel302 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role"):
                    opp_val = getattr(item, "Role", None)
                    
                    if opp_val == self:
                        setattr(item, "Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role"):
                    opp_val = getattr(item, "Role", None)
                    
                    setattr(item, "Role", self)
                    

    @property
    def camel_organisation_OrganisationModel292(self):
        return self.__camel_organisation_OrganisationModel292

    @camel_organisation_OrganisationModel292.setter
    def camel_organisation_OrganisationModel292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_OrganisationModel__camel_organisation_OrganisationModel292", None)
        self.__camel_organisation_OrganisationModel292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CloudProvider"):
                opp_val = getattr(old_value, "CloudProvider", None)
                if opp_val == self:
                    setattr(old_value, "CloudProvider", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CloudProvider"):
                opp_val = getattr(value, "CloudProvider", None)
                setattr(value, "CloudProvider", self)

    @property
    def camel_organisation_OrganisationModel(self):
        return self.__camel_organisation_OrganisationModel

    @camel_organisation_OrganisationModel.setter
    def camel_organisation_OrganisationModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_OrganisationModel__camel_organisation_OrganisationModel", None)
        self.__camel_organisation_OrganisationModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organisation"):
                opp_val = getattr(old_value, "Organisation", None)
                if opp_val == self:
                    setattr(old_value, "Organisation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organisation"):
                opp_val = getattr(value, "Organisation", None)
                setattr(value, "Organisation", self)

    @property
    def camel_organisation_OrganisationModel308(self):
        return self.__camel_organisation_OrganisationModel308

    @camel_organisation_OrganisationModel308.setter
    def camel_organisation_OrganisationModel308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_OrganisationModel__camel_organisation_OrganisationModel308", None)
        self.__camel_organisation_OrganisationModel308 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceFilter"):
                    opp_val = getattr(item, "ResourceFilter", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceFilter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceFilter"):
                    opp_val = getattr(item, "ResourceFilter", None)
                    
                    setattr(item, "ResourceFilter", self)
                    

    @property
    def camel_organisation_OrganisationModel306(self):
        return self.__camel_organisation_OrganisationModel306

    @camel_organisation_OrganisationModel306.setter
    def camel_organisation_OrganisationModel306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_OrganisationModel__camel_organisation_OrganisationModel306", None)
        self.__camel_organisation_OrganisationModel306 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Permission"):
                    opp_val = getattr(item, "Permission", None)
                    
                    if opp_val == self:
                        setattr(item, "Permission", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Permission"):
                    opp_val = getattr(item, "Permission", None)
                    
                    setattr(item, "Permission", self)
                    

    @property
    def camel_organisation_OrganisationModel304(self):
        return self.__camel_organisation_OrganisationModel304

    @camel_organisation_OrganisationModel304.setter
    def camel_organisation_OrganisationModel304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_OrganisationModel__camel_organisation_OrganisationModel304", None)
        self.__camel_organisation_OrganisationModel304 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RoleAssignment"):
                    opp_val = getattr(item, "RoleAssignment", None)
                    
                    if opp_val == self:
                        setattr(item, "RoleAssignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RoleAssignment"):
                    opp_val = getattr(item, "RoleAssignment", None)
                    
                    setattr(item, "RoleAssignment", self)
                    

    @property
    def camel_organisation_OrganisationModel300(self):
        return self.__camel_organisation_OrganisationModel300

    @camel_organisation_OrganisationModel300.setter
    def camel_organisation_OrganisationModel300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_OrganisationModel__camel_organisation_OrganisationModel300", None)
        self.__camel_organisation_OrganisationModel300 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataCenter"):
                    opp_val = getattr(item, "DataCenter", None)
                    
                    if opp_val == self:
                        setattr(item, "DataCenter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataCenter"):
                    opp_val = getattr(item, "DataCenter", None)
                    
                    setattr(item, "DataCenter", self)
                    

    @property
    def camel_organisation_OrganisationModel296(self):
        return self.__camel_organisation_OrganisationModel296

    @camel_organisation_OrganisationModel296.setter
    def camel_organisation_OrganisationModel296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camel_organisation_OrganisationModel__camel_organisation_OrganisationModel296", None)
        self.__camel_organisation_OrganisationModel296 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User"):
                    opp_val = getattr(item, "User", None)
                    
                    if opp_val == self:
                        setattr(item, "User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User"):
                    opp_val = getattr(item, "User", None)
                    
                    setattr(item, "User", self)
                    

class camel_execution_ExecutionModel(Model):

    pass
class camel_unit_UnitModel(Model):

    pass
class camel_deployment_DeploymentModel(Model):

    pass
class camel_CamelModel(Model):

    pass
class camel_Model(ABC):

    def __init__(self, name: str, importURI: str):
        self.name = name
        self.importURI = importURI
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
