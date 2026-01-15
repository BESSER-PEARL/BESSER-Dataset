from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ColectType(Enum):
    intercalated = "intercalated"
    continuous = "continuous"
class BaseElement(Enum):
    Task = "Task"
    Activity = "Activity"
class MetricUnit(Enum):
    minutes = "minutes"
    uc = "uc"
class MetricType(Enum):
    hardData = "hardData"
    softData = "softData"
    normalizedData = "normalizedData"


############################################
# Definition of Classes
############################################

class MetricModel_Metric:

    def __init__(self, name: str, description: str, type: str, form: str, id: str, unit: str, MetricModel_Metric: "MetricModel_MetricPlanModel" = None):
        self.name = name
        self.description = description
        self.type = type
        self.form = form
        self.id = id
        self.unit = unit
        self.MetricModel_Metric = MetricModel_Metric
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def form(self) -> str:
        return self.__form

    @form.setter
    def form(self, form: str):
        self.__form = form

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def MetricModel_Metric(self):
        return self.__MetricModel_Metric

    @MetricModel_Metric.setter
    def MetricModel_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetricModel_Metric__MetricModel_Metric", None)
        self.__MetricModel_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetricModel_MetricPlanModel"):
                opp_val = getattr(old_value, "MetricModel_MetricPlanModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetricModel_MetricPlanModel"):
                opp_val = getattr(value, "MetricModel_MetricPlanModel", None)
                if opp_val is None:
                    setattr(value, "MetricModel_MetricPlanModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MetricModel_MetricPlanModel:

    def __init__(self, name: str, MetricModel_MetricPlanModel: set["MetricModel_Metric"] = None):
        self.name = name
        self.MetricModel_MetricPlanModel = MetricModel_MetricPlanModel if MetricModel_MetricPlanModel is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MetricModel_MetricPlanModel(self):
        return self.__MetricModel_MetricPlanModel

    @MetricModel_MetricPlanModel.setter
    def MetricModel_MetricPlanModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetricModel_MetricPlanModel__MetricModel_MetricPlanModel", None)
        self.__MetricModel_MetricPlanModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetricModel_Metric"):
                    opp_val = getattr(item, "MetricModel_Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "MetricModel_Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetricModel_Metric"):
                    opp_val = getattr(item, "MetricModel_Metric", None)
                    
                    setattr(item, "MetricModel_Metric", self)
                    

class Metric:

    pass
class MetricModel_TaskMetric(Metric):

    def __init__(self, tasksBase: str):
        self.tasksBase = tasksBase
        
    @property
    def tasksBase(self) -> str:
        return self.__tasksBase

    @tasksBase.setter
    def tasksBase(self, tasksBase: str):
        self.__tasksBase = tasksBase

class MetricModel_ActivityMetric(Metric):

    def __init__(self, activityBegin: str, activityEnd: str):
        self.activityBegin = activityBegin
        self.activityEnd = activityEnd
        
    @property
    def activityBegin(self) -> str:
        return self.__activityBegin

    @activityBegin.setter
    def activityBegin(self, activityBegin: str):
        self.__activityBegin = activityBegin

    @property
    def activityEnd(self) -> str:
        return self.__activityEnd

    @activityEnd.setter
    def activityEnd(self, activityEnd: str):
        self.__activityEnd = activityEnd
