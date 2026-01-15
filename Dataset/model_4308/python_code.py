from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simple_metrics_Metric:

    def __init__(self, name: str, value: str, simple_metrics_Metric: "simple_metrics_MetricsSet" = None):
        self.name = name
        self.value = value
        self.simple_metrics_Metric = simple_metrics_Metric
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def simple_metrics_Metric(self):
        return self.__simple_metrics_Metric

    @simple_metrics_Metric.setter
    def simple_metrics_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_metrics_Metric__simple_metrics_Metric", None)
        self.__simple_metrics_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple_metrics_MetricsSet"):
                opp_val = getattr(old_value, "simple_metrics_MetricsSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple_metrics_MetricsSet"):
                opp_val = getattr(value, "simple_metrics_MetricsSet", None)
                if opp_val is None:
                    setattr(value, "simple_metrics_MetricsSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simple_metrics_MetricsSet:

    def __init__(self, name: str, simple_metrics_MetricsSet: set["simple_metrics_Metric"] = None):
        self.name = name
        self.simple_metrics_MetricsSet = simple_metrics_MetricsSet if simple_metrics_MetricsSet is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simple_metrics_MetricsSet(self):
        return self.__simple_metrics_MetricsSet

    @simple_metrics_MetricsSet.setter
    def simple_metrics_MetricsSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_metrics_MetricsSet__simple_metrics_MetricsSet", None)
        self.__simple_metrics_MetricsSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simple_metrics_Metric"):
                    opp_val = getattr(item, "simple_metrics_Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "simple_metrics_Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simple_metrics_Metric"):
                    opp_val = getattr(item, "simple_metrics_Metric", None)
                    
                    setattr(item, "simple_metrics_Metric", self)
                    
