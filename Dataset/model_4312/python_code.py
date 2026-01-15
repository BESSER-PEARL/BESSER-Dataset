from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Metric:

    pass
class QualityMetrics_Metric(ABC):

    def __init__(self, Metric: str):
        self.Metric = Metric
        
    @property
    def Metric(self) -> str:
        return self.__Metric

    @Metric.setter
    def Metric(self, Metric: str):
        self.__Metric = Metric

class QualityMetrics_AggregatedRealMetric(Metric):

    def __init__(self, Minimum: float, Maximum: float, Median: float, Average: float, StandardDeviation: float, QualityMetrics_AggregatedRealMetric: "QualityMetrics_Metrics" = None):
        self.Minimum = Minimum
        self.Maximum = Maximum
        self.Median = Median
        self.Average = Average
        self.StandardDeviation = StandardDeviation
        self.QualityMetrics_AggregatedRealMetric = QualityMetrics_AggregatedRealMetric
        
    @property
    def Minimum(self) -> float:
        return self.__Minimum

    @Minimum.setter
    def Minimum(self, Minimum: float):
        self.__Minimum = Minimum

    @property
    def Average(self) -> float:
        return self.__Average

    @Average.setter
    def Average(self, Average: float):
        self.__Average = Average

    @property
    def Maximum(self) -> float:
        return self.__Maximum

    @Maximum.setter
    def Maximum(self, Maximum: float):
        self.__Maximum = Maximum

    @property
    def Median(self) -> float:
        return self.__Median

    @Median.setter
    def Median(self, Median: float):
        self.__Median = Median

    @property
    def StandardDeviation(self) -> float:
        return self.__StandardDeviation

    @StandardDeviation.setter
    def StandardDeviation(self, StandardDeviation: float):
        self.__StandardDeviation = StandardDeviation

    @property
    def QualityMetrics_AggregatedRealMetric(self):
        return self.__QualityMetrics_AggregatedRealMetric

    @QualityMetrics_AggregatedRealMetric.setter
    def QualityMetrics_AggregatedRealMetric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetrics_AggregatedRealMetric__QualityMetrics_AggregatedRealMetric", None)
        self.__QualityMetrics_AggregatedRealMetric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetrics_Metrics4"):
                opp_val = getattr(old_value, "QualityMetrics_Metrics4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetrics_Metrics4"):
                opp_val = getattr(value, "QualityMetrics_Metrics4", None)
                if opp_val is None:
                    setattr(value, "QualityMetrics_Metrics4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class QualityMetrics_AggregatedIntegerMetric(Metric):

    def __init__(self, Minimum: int, Maximum: int, Median: int, Average: float, StandardDeviation: float, QualityMetrics_AggregatedIntegerMetric: "QualityMetrics_Metrics" = None):
        self.Minimum = Minimum
        self.Maximum = Maximum
        self.Median = Median
        self.Average = Average
        self.StandardDeviation = StandardDeviation
        self.QualityMetrics_AggregatedIntegerMetric = QualityMetrics_AggregatedIntegerMetric
        
    @property
    def Minimum(self) -> int:
        return self.__Minimum

    @Minimum.setter
    def Minimum(self, Minimum: int):
        self.__Minimum = Minimum

    @property
    def Average(self) -> float:
        return self.__Average

    @Average.setter
    def Average(self, Average: float):
        self.__Average = Average

    @property
    def Maximum(self) -> int:
        return self.__Maximum

    @Maximum.setter
    def Maximum(self, Maximum: int):
        self.__Maximum = Maximum

    @property
    def Median(self) -> int:
        return self.__Median

    @Median.setter
    def Median(self, Median: int):
        self.__Median = Median

    @property
    def StandardDeviation(self) -> float:
        return self.__StandardDeviation

    @StandardDeviation.setter
    def StandardDeviation(self, StandardDeviation: float):
        self.__StandardDeviation = StandardDeviation

    @property
    def QualityMetrics_AggregatedIntegerMetric(self):
        return self.__QualityMetrics_AggregatedIntegerMetric

    @QualityMetrics_AggregatedIntegerMetric.setter
    def QualityMetrics_AggregatedIntegerMetric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetrics_AggregatedIntegerMetric__QualityMetrics_AggregatedIntegerMetric", None)
        self.__QualityMetrics_AggregatedIntegerMetric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetrics_Metrics2"):
                opp_val = getattr(old_value, "QualityMetrics_Metrics2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetrics_Metrics2"):
                opp_val = getattr(value, "QualityMetrics_Metrics2", None)
                if opp_val is None:
                    setattr(value, "QualityMetrics_Metrics2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class QualityMetrics_Metrics:

    def __init__(self, TrafoName: str, QualityMetrics_Metrics: set["QualityMetrics_SimpleMetric"] = None, QualityMetrics_Metrics2: set["QualityMetrics_AggregatedIntegerMetric"] = None, QualityMetrics_Metrics4: set["QualityMetrics_AggregatedRealMetric"] = None):
        self.TrafoName = TrafoName
        self.QualityMetrics_Metrics = QualityMetrics_Metrics if QualityMetrics_Metrics is not None else set()
        self.QualityMetrics_Metrics2 = QualityMetrics_Metrics2 if QualityMetrics_Metrics2 is not None else set()
        self.QualityMetrics_Metrics4 = QualityMetrics_Metrics4 if QualityMetrics_Metrics4 is not None else set()
        
    @property
    def TrafoName(self) -> str:
        return self.__TrafoName

    @TrafoName.setter
    def TrafoName(self, TrafoName: str):
        self.__TrafoName = TrafoName

    @property
    def QualityMetrics_Metrics(self):
        return self.__QualityMetrics_Metrics

    @QualityMetrics_Metrics.setter
    def QualityMetrics_Metrics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetrics_Metrics__QualityMetrics_Metrics", None)
        self.__QualityMetrics_Metrics = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QualityMetrics_SimpleMetric"):
                    opp_val = getattr(item, "QualityMetrics_SimpleMetric", None)
                    
                    if opp_val == self:
                        setattr(item, "QualityMetrics_SimpleMetric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QualityMetrics_SimpleMetric"):
                    opp_val = getattr(item, "QualityMetrics_SimpleMetric", None)
                    
                    setattr(item, "QualityMetrics_SimpleMetric", self)
                    

    @property
    def QualityMetrics_Metrics4(self):
        return self.__QualityMetrics_Metrics4

    @QualityMetrics_Metrics4.setter
    def QualityMetrics_Metrics4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetrics_Metrics__QualityMetrics_Metrics4", None)
        self.__QualityMetrics_Metrics4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QualityMetrics_AggregatedRealMetric"):
                    opp_val = getattr(item, "QualityMetrics_AggregatedRealMetric", None)
                    
                    if opp_val == self:
                        setattr(item, "QualityMetrics_AggregatedRealMetric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QualityMetrics_AggregatedRealMetric"):
                    opp_val = getattr(item, "QualityMetrics_AggregatedRealMetric", None)
                    
                    setattr(item, "QualityMetrics_AggregatedRealMetric", self)
                    

    @property
    def QualityMetrics_Metrics2(self):
        return self.__QualityMetrics_Metrics2

    @QualityMetrics_Metrics2.setter
    def QualityMetrics_Metrics2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetrics_Metrics__QualityMetrics_Metrics2", None)
        self.__QualityMetrics_Metrics2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QualityMetrics_AggregatedIntegerMetric"):
                    opp_val = getattr(item, "QualityMetrics_AggregatedIntegerMetric", None)
                    
                    if opp_val == self:
                        setattr(item, "QualityMetrics_AggregatedIntegerMetric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QualityMetrics_AggregatedIntegerMetric"):
                    opp_val = getattr(item, "QualityMetrics_AggregatedIntegerMetric", None)
                    
                    setattr(item, "QualityMetrics_AggregatedIntegerMetric", self)
                    

class QualityMetrics_SimpleMetric(Metric):

    def __init__(self, Value: int, QualityMetrics_SimpleMetric: "QualityMetrics_Metrics" = None):
        self.Value = Value
        self.QualityMetrics_SimpleMetric = QualityMetrics_SimpleMetric
        
    @property
    def Value(self) -> int:
        return self.__Value

    @Value.setter
    def Value(self, Value: int):
        self.__Value = Value

    @property
    def QualityMetrics_SimpleMetric(self):
        return self.__QualityMetrics_SimpleMetric

    @QualityMetrics_SimpleMetric.setter
    def QualityMetrics_SimpleMetric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QualityMetrics_SimpleMetric__QualityMetrics_SimpleMetric", None)
        self.__QualityMetrics_SimpleMetric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityMetrics_Metrics"):
                opp_val = getattr(old_value, "QualityMetrics_Metrics", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityMetrics_Metrics"):
                opp_val = getattr(value, "QualityMetrics_Metrics", None)
                if opp_val is None:
                    setattr(value, "QualityMetrics_Metrics", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
