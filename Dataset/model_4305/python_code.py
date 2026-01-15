from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class metrics_Value:

    pass
class metrics_MetricSource:

    def __init__(self, lastContact: str, lastPurge: str, location: str, metrickind: str, name: str, metrics_MetricSource: set["metrics_Value"] = None):
        self.lastContact = lastContact
        self.lastPurge = lastPurge
        self.location = location
        self.metrickind = metrickind
        self.name = name
        self.metrics_MetricSource = metrics_MetricSource if metrics_MetricSource is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metrickind(self) -> str:
        return self.__metrickind

    @metrickind.setter
    def metrickind(self, metrickind: str):
        self.__metrickind = metrickind

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def lastPurge(self) -> str:
        return self.__lastPurge

    @lastPurge.setter
    def lastPurge(self, lastPurge: str):
        self.__lastPurge = lastPurge

    @property
    def lastContact(self) -> str:
        return self.__lastContact

    @lastContact.setter
    def lastContact(self, lastContact: str):
        self.__lastContact = lastContact

    @property
    def metrics_MetricSource(self):
        return self.__metrics_MetricSource

    @metrics_MetricSource.setter
    def metrics_MetricSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metrics_MetricSource", None)
        self.__metrics_MetricSource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_Value"):
                    opp_val = getattr(item, "metrics_Value", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_Value", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_Value"):
                    opp_val = getattr(item, "metrics_Value", None)
                    
                    setattr(item, "metrics_Value", self)
                    
