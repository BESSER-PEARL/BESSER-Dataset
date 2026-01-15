from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class metricDSL_BoundAndWeight:

    pass
class metricDSL_MetricAndWeight:

    pass
class MetricDefinition:

    pass
class metricDSL_RatioMetric(MetricDefinition):

    pass
class metricDSL_StepwiseMetric(MetricDefinition):

    pass
class metricDSL_WeightedMetric(MetricDefinition):

    pass
class Number:

    pass
class metricDSL_Constant(Number):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class metricDSL_Parameter(Number):

    def __init__(self, shortname: str, description: str, defaultValue: float):
        self.shortname = shortname
        self.description = description
        self.defaultValue = defaultValue
        
    @property
    def shortname(self) -> str:
        return self.__shortname

    @shortname.setter
    def shortname(self, shortname: str):
        self.__shortname = shortname

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def defaultValue(self) -> float:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: float):
        self.__defaultValue = defaultValue

class metricDSL_MetricDefinition:

    pass
class metricDSL_Number:

    def __init__(self, name: str, metricDSL_Number: "metricDSL_InternalMetric" = None, metricDSL_Number16: "metricDSL_BoundAndWeight" = None, metricDSL_Number19: "metricDSL_BoundAndWeight" = None, metricDSL_Number25: "metricDSL_MetricAndWeight" = None):
        self.name = name
        self.metricDSL_Number = metricDSL_Number
        self.metricDSL_Number16 = metricDSL_Number16
        self.metricDSL_Number19 = metricDSL_Number19
        self.metricDSL_Number25 = metricDSL_Number25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metricDSL_Number16(self):
        return self.__metricDSL_Number16

    @metricDSL_Number16.setter
    def metricDSL_Number16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_Number__metricDSL_Number16", None)
        self.__metricDSL_Number16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricDSL_BoundAndWeight15"):
                opp_val = getattr(old_value, "metricDSL_BoundAndWeight15", None)
                if opp_val == self:
                    setattr(old_value, "metricDSL_BoundAndWeight15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricDSL_BoundAndWeight15"):
                opp_val = getattr(value, "metricDSL_BoundAndWeight15", None)
                setattr(value, "metricDSL_BoundAndWeight15", self)

    @property
    def metricDSL_Number25(self):
        return self.__metricDSL_Number25

    @metricDSL_Number25.setter
    def metricDSL_Number25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_Number__metricDSL_Number25", None)
        self.__metricDSL_Number25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricDSL_MetricAndWeight24"):
                opp_val = getattr(old_value, "metricDSL_MetricAndWeight24", None)
                if opp_val == self:
                    setattr(old_value, "metricDSL_MetricAndWeight24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricDSL_MetricAndWeight24"):
                opp_val = getattr(value, "metricDSL_MetricAndWeight24", None)
                setattr(value, "metricDSL_MetricAndWeight24", self)

    @property
    def metricDSL_Number(self):
        return self.__metricDSL_Number

    @metricDSL_Number.setter
    def metricDSL_Number(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_Number__metricDSL_Number", None)
        self.__metricDSL_Number = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricDSL_InternalMetric"):
                opp_val = getattr(old_value, "metricDSL_InternalMetric", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricDSL_InternalMetric"):
                opp_val = getattr(value, "metricDSL_InternalMetric", None)
                if opp_val is None:
                    setattr(value, "metricDSL_InternalMetric", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metricDSL_Number19(self):
        return self.__metricDSL_Number19

    @metricDSL_Number19.setter
    def metricDSL_Number19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_Number__metricDSL_Number19", None)
        self.__metricDSL_Number19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricDSL_BoundAndWeight18"):
                opp_val = getattr(old_value, "metricDSL_BoundAndWeight18", None)
                if opp_val == self:
                    setattr(old_value, "metricDSL_BoundAndWeight18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricDSL_BoundAndWeight18"):
                opp_val = getattr(value, "metricDSL_BoundAndWeight18", None)
                setattr(value, "metricDSL_BoundAndWeight18", self)

class Metric:

    pass
class metricDSL_InternalMetric(Metric):

    def __init__(self, shortName: str, description: str, metricDSL_InternalMetric: set["metricDSL_Number"] = None, metricDSL_InternalMetric3: "metricDSL_MetricDefinition" = None):
        self.shortName = shortName
        self.description = description
        self.metricDSL_InternalMetric = metricDSL_InternalMetric if metricDSL_InternalMetric is not None else set()
        self.metricDSL_InternalMetric3 = metricDSL_InternalMetric3
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def shortName(self) -> str:
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName

    @property
    def metricDSL_InternalMetric(self):
        return self.__metricDSL_InternalMetric

    @metricDSL_InternalMetric.setter
    def metricDSL_InternalMetric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_InternalMetric__metricDSL_InternalMetric", None)
        self.__metricDSL_InternalMetric = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metricDSL_Number"):
                    opp_val = getattr(item, "metricDSL_Number", None)
                    
                    if opp_val == self:
                        setattr(item, "metricDSL_Number", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metricDSL_Number"):
                    opp_val = getattr(item, "metricDSL_Number", None)
                    
                    setattr(item, "metricDSL_Number", self)
                    

    @property
    def metricDSL_InternalMetric3(self):
        return self.__metricDSL_InternalMetric3

    @metricDSL_InternalMetric3.setter
    def metricDSL_InternalMetric3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_InternalMetric__metricDSL_InternalMetric3", None)
        self.__metricDSL_InternalMetric3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricDSL_MetricDefinition"):
                opp_val = getattr(old_value, "metricDSL_MetricDefinition", None)
                if opp_val == self:
                    setattr(old_value, "metricDSL_MetricDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricDSL_MetricDefinition"):
                opp_val = getattr(value, "metricDSL_MetricDefinition", None)
                setattr(value, "metricDSL_MetricDefinition", self)

class metricDSL_ExternalMetric(Metric):

    pass
class metricDSL_Metric:

    def __init__(self, name: str, metricDSL_Metric: "metricDSL_MetricModel" = None, metricDSL_Metric6: "metricDSL_StepwiseMetric" = None, metricDSL_Metric10: "metricDSL_RatioMetric" = None, metricDSL_Metric13: "metricDSL_RatioMetric" = None, metricDSL_Metric22: "metricDSL_MetricAndWeight" = None):
        self.name = name
        self.metricDSL_Metric = metricDSL_Metric
        self.metricDSL_Metric6 = metricDSL_Metric6
        self.metricDSL_Metric10 = metricDSL_Metric10
        self.metricDSL_Metric13 = metricDSL_Metric13
        self.metricDSL_Metric22 = metricDSL_Metric22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metricDSL_Metric(self):
        return self.__metricDSL_Metric

    @metricDSL_Metric.setter
    def metricDSL_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_Metric__metricDSL_Metric", None)
        self.__metricDSL_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricDSL_MetricModel"):
                opp_val = getattr(old_value, "metricDSL_MetricModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricDSL_MetricModel"):
                opp_val = getattr(value, "metricDSL_MetricModel", None)
                if opp_val is None:
                    setattr(value, "metricDSL_MetricModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metricDSL_Metric22(self):
        return self.__metricDSL_Metric22

    @metricDSL_Metric22.setter
    def metricDSL_Metric22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_Metric__metricDSL_Metric22", None)
        self.__metricDSL_Metric22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricDSL_MetricAndWeight21"):
                opp_val = getattr(old_value, "metricDSL_MetricAndWeight21", None)
                if opp_val == self:
                    setattr(old_value, "metricDSL_MetricAndWeight21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricDSL_MetricAndWeight21"):
                opp_val = getattr(value, "metricDSL_MetricAndWeight21", None)
                setattr(value, "metricDSL_MetricAndWeight21", self)

    @property
    def metricDSL_Metric10(self):
        return self.__metricDSL_Metric10

    @metricDSL_Metric10.setter
    def metricDSL_Metric10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_Metric__metricDSL_Metric10", None)
        self.__metricDSL_Metric10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricDSL_RatioMetric"):
                opp_val = getattr(old_value, "metricDSL_RatioMetric", None)
                if opp_val == self:
                    setattr(old_value, "metricDSL_RatioMetric", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricDSL_RatioMetric"):
                opp_val = getattr(value, "metricDSL_RatioMetric", None)
                setattr(value, "metricDSL_RatioMetric", self)

    @property
    def metricDSL_Metric13(self):
        return self.__metricDSL_Metric13

    @metricDSL_Metric13.setter
    def metricDSL_Metric13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_Metric__metricDSL_Metric13", None)
        self.__metricDSL_Metric13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricDSL_RatioMetric12"):
                opp_val = getattr(old_value, "metricDSL_RatioMetric12", None)
                if opp_val == self:
                    setattr(old_value, "metricDSL_RatioMetric12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricDSL_RatioMetric12"):
                opp_val = getattr(value, "metricDSL_RatioMetric12", None)
                setattr(value, "metricDSL_RatioMetric12", self)

    @property
    def metricDSL_Metric6(self):
        return self.__metricDSL_Metric6

    @metricDSL_Metric6.setter
    def metricDSL_Metric6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_Metric__metricDSL_Metric6", None)
        self.__metricDSL_Metric6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metricDSL_StepwiseMetric"):
                opp_val = getattr(old_value, "metricDSL_StepwiseMetric", None)
                if opp_val == self:
                    setattr(old_value, "metricDSL_StepwiseMetric", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metricDSL_StepwiseMetric"):
                opp_val = getattr(value, "metricDSL_StepwiseMetric", None)
                setattr(value, "metricDSL_StepwiseMetric", self)

class metricDSL_MetricModel:

    def __init__(self, importURI: str, metricDSL_MetricModel: set["metricDSL_Metric"] = None):
        self.importURI = importURI
        self.metricDSL_MetricModel = metricDSL_MetricModel if metricDSL_MetricModel is not None else set()
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def metricDSL_MetricModel(self):
        return self.__metricDSL_MetricModel

    @metricDSL_MetricModel.setter
    def metricDSL_MetricModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metricDSL_MetricModel__metricDSL_MetricModel", None)
        self.__metricDSL_MetricModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metricDSL_Metric"):
                    opp_val = getattr(item, "metricDSL_Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "metricDSL_Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metricDSL_Metric"):
                    opp_val = getattr(item, "metricDSL_Metric", None)
                    
                    setattr(item, "metricDSL_Metric", self)
                    
