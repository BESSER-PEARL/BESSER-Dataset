from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class metrics_Observation:

    pass
class ModelElement:

    pass
class Measurement:

    pass
class metrics_LinkMeasurement(Measurement):

    pass
class metrics_ComplexMeasurement(Measurement):

    pass
class metrics_ValueMeasurement(Measurement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class metrics_Measurement(ABC):

    def __init__(self, tag: str, name: str, error: str, metrics_Measurement: "metrics_ComplexMeasurement" = None, metrics_Measurement3: "metrics_Observation" = None):
        self.tag = tag
        self.name = name
        self.error = error
        self.metrics_Measurement = metrics_Measurement
        self.metrics_Measurement3 = metrics_Measurement3
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def error(self) -> str:
        return self.__error

    @error.setter
    def error(self, error: str):
        self.__error = error

    @property
    def metrics_Measurement(self):
        return self.__metrics_Measurement

    @metrics_Measurement.setter
    def metrics_Measurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Measurement__metrics_Measurement", None)
        self.__metrics_Measurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_ComplexMeasurement"):
                opp_val = getattr(old_value, "metrics_ComplexMeasurement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_ComplexMeasurement"):
                opp_val = getattr(value, "metrics_ComplexMeasurement", None)
                if opp_val is None:
                    setattr(value, "metrics_ComplexMeasurement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metrics_Measurement3(self):
        return self.__metrics_Measurement3

    @metrics_Measurement3.setter
    def metrics_Measurement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Measurement__metrics_Measurement3", None)
        self.__metrics_Measurement3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Observation"):
                opp_val = getattr(old_value, "metrics_Observation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Observation"):
                opp_val = getattr(value, "metrics_Observation", None)
                if opp_val is None:
                    setattr(value, "metrics_Observation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
