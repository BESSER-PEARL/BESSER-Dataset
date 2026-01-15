from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class metrics_Metric:

    def __init__(self, name: str, value: str, metrics_Metric: "metrics_MetricsSet" = None):
        self.name = name
        self.value = value
        self.metrics_Metric = metrics_Metric
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metrics_Metric(self):
        return self.__metrics_Metric

    @metrics_Metric.setter
    def metrics_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric", None)
        self.__metrics_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricsSet"):
                opp_val = getattr(old_value, "metrics_MetricsSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricsSet"):
                opp_val = getattr(value, "metrics_MetricsSet", None)
                if opp_val is None:
                    setattr(value, "metrics_MetricsSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metrics_MetricsSet:

    def __init__(self, name: str, metrics_MetricsSet: set["metrics_Metric"] = None):
        self.name = name
        self.metrics_MetricsSet = metrics_MetricsSet if metrics_MetricsSet is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metrics_MetricsSet(self):
        return self.__metrics_MetricsSet

    @metrics_MetricsSet.setter
    def metrics_MetricsSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricsSet__metrics_MetricsSet", None)
        self.__metrics_MetricsSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_Metric"):
                    opp_val = getattr(item, "metrics_Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_Metric"):
                    opp_val = getattr(item, "metrics_Metric", None)
                    
                    setattr(item, "metrics_Metric", self)
                    
