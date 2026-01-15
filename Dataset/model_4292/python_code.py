from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Metrics_MetricValue(ABC):

    def __init__(self, tag: str):
        self.tag = tag
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

class MetricValue:

    pass
class Metrics_DoubleMetricValue(MetricValue):

    def __init__(self, value: str, MetricValue: "Metrics_Metric"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Metrics_StringMetricValue(MetricValue):

    def __init__(self, value: str, MetricValue: "Metrics_Metric"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Metrics_BooleanMetricValue(MetricValue):

    def __init__(self, value: str, MetricValue: "Metrics_Metric"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Metrics_IntegerMetricValue(MetricValue):

    def __init__(self, value: str, MetricValue: "Metrics_Metric"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Metrics_Metric:

    def __init__(self, name: str, Metrics_Metric: set["MetricValue"] = None):
        self.name = name
        self.Metrics_Metric = Metrics_Metric if Metrics_Metric is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Metrics_Metric(self):
        return self.__Metrics_Metric

    @Metrics_Metric.setter
    def Metrics_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metrics_Metric__Metrics_Metric", None)
        self.__Metrics_Metric = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetricValue"):
                    opp_val = getattr(item, "MetricValue", None)
                    
                    if opp_val == self:
                        setattr(item, "MetricValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetricValue"):
                    opp_val = getattr(item, "MetricValue", None)
                    
                    setattr(item, "MetricValue", self)
                    
