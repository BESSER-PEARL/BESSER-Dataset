from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class metric_Metric(ABC):

    def __init__(self, description: str, code: str, name: str, metric_Metric: "metric_Container" = None):
        self.description = description
        self.code = code
        self.name = name
        self.metric_Metric = metric_Metric
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def metric_Metric(self):
        return self.__metric_Metric

    @metric_Metric.setter
    def metric_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metric_Metric__metric_Metric", None)
        self.__metric_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metric_Container"):
                opp_val = getattr(old_value, "metric_Container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metric_Container"):
                opp_val = getattr(value, "metric_Container", None)
                if opp_val is None:
                    setattr(value, "metric_Container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metric_Container:

    pass
class Metric:

    pass
class metric_SimpleMetric(Metric):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class metric_AggregatedRealMetric(Metric):

    def __init__(self, minimum: float, maximum: float, median: float, average: float, standardDeviation: float):
        self.minimum = minimum
        self.maximum = maximum
        self.median = median
        self.average = average
        self.standardDeviation = standardDeviation
        
    @property
    def median(self) -> float:
        return self.__median

    @median.setter
    def median(self, median: float):
        self.__median = median

    @property
    def average(self) -> float:
        return self.__average

    @average.setter
    def average(self, average: float):
        self.__average = average

    @property
    def maximum(self) -> float:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: float):
        self.__maximum = maximum

    @property
    def minimum(self) -> float:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: float):
        self.__minimum = minimum

    @property
    def standardDeviation(self) -> float:
        return self.__standardDeviation

    @standardDeviation.setter
    def standardDeviation(self, standardDeviation: float):
        self.__standardDeviation = standardDeviation

class metric_AggregatedIntegerMetric(Metric):

    def __init__(self, minimum: str, maximum: str, median: str, average: float, standardDeviation: float):
        self.minimum = minimum
        self.maximum = maximum
        self.median = median
        self.average = average
        self.standardDeviation = standardDeviation
        
    @property
    def standardDeviation(self) -> float:
        return self.__standardDeviation

    @standardDeviation.setter
    def standardDeviation(self, standardDeviation: float):
        self.__standardDeviation = standardDeviation

    @property
    def average(self) -> float:
        return self.__average

    @average.setter
    def average(self, average: float):
        self.__average = average

    @property
    def minimum(self) -> str:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: str):
        self.__minimum = minimum

    @property
    def maximum(self) -> str:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: str):
        self.__maximum = maximum

    @property
    def median(self) -> str:
        return self.__median

    @median.setter
    def median(self, median: str):
        self.__median = median
