from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MetricKind(Enum):
    FILE = "FILE"
    RDMS = "RDMS"


############################################
# Definition of Classes
############################################

class metrics_MetricSource:

    def __init__(self, lastContact: str, lastPurge: str, mappingFile: str, metrickind: str, metricLocation: str, name: str, metricSource: set["metrics_Metric"] = None, metrics_MetricSource: "metrics_MetricLibrary" = None):
        self.lastContact = lastContact
        self.lastPurge = lastPurge
        self.mappingFile = mappingFile
        self.metrickind = metrickind
        self.metricLocation = metricLocation
        self.name = name
        self.metricSource = metricSource if metricSource is not None else set()
        self.metrics_MetricSource = metrics_MetricSource
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mappingFile(self) -> str:
        return self.__mappingFile

    @mappingFile.setter
    def mappingFile(self, mappingFile: str):
        self.__mappingFile = mappingFile

    @property
    def lastPurge(self) -> str:
        return self.__lastPurge

    @lastPurge.setter
    def lastPurge(self, lastPurge: str):
        self.__lastPurge = lastPurge

    @property
    def metrickind(self) -> str:
        return self.__metrickind

    @metrickind.setter
    def metrickind(self, metrickind: str):
        self.__metrickind = metrickind

    @property
    def lastContact(self) -> str:
        return self.__lastContact

    @lastContact.setter
    def lastContact(self, lastContact: str):
        self.__lastContact = lastContact

    @property
    def metricLocation(self) -> str:
        return self.__metricLocation

    @metricLocation.setter
    def metricLocation(self, metricLocation: str):
        self.__metricLocation = metricLocation

    @property
    def metricSource(self):
        return self.__metricSource

    @metricSource.setter
    def metricSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metricSource", None)
        self.__metricSource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "networks.ecoreMetric"):
                    opp_val = getattr(item, "networks.ecoreMetric", None)
                    
                    if opp_val == self:
                        setattr(item, "networks.ecoreMetric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "networks.ecoreMetric"):
                    opp_val = getattr(item, "networks.ecoreMetric", None)
                    
                    setattr(item, "networks.ecoreMetric", self)
                    

    @property
    def metrics_MetricSource(self):
        return self.__metrics_MetricSource

    @metrics_MetricSource.setter
    def metrics_MetricSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metrics_MetricSource", None)
        self.__metrics_MetricSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricLibrary"):
                opp_val = getattr(old_value, "metrics_MetricLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricLibrary"):
                opp_val = getattr(value, "metrics_MetricLibrary", None)
                if opp_val is None:
                    setattr(value, "metrics_MetricLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metrics_MetricLibrary:

    def __init__(self, name: str, metrics_MetricLibrary: set["metrics_MetricSource"] = None):
        self.name = name
        self.metrics_MetricLibrary = metrics_MetricLibrary if metrics_MetricLibrary is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metrics_MetricLibrary(self):
        return self.__metrics_MetricLibrary

    @metrics_MetricLibrary.setter
    def metrics_MetricLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricLibrary__metrics_MetricLibrary", None)
        self.__metrics_MetricLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_MetricSource"):
                    opp_val = getattr(item, "metrics_MetricSource", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_MetricSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_MetricSource"):
                    opp_val = getattr(item, "metrics_MetricSource", None)
                    
                    setattr(item, "metrics_MetricSource", self)
                    

class metrics_Metric:

    pass