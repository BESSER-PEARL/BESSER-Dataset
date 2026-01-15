from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class FixedMetricRetentionPeriod(Enum):
    Always = "Always"
    OneYear = "OneYear"
    OneMonth = "OneMonth"
    OneWeek = "OneWeek"


############################################
# Definition of Classes
############################################

class metrics_MetricRetentionPeriods:

    def __init__(self, metricRetentionPeriods: str):
        self.metricRetentionPeriods = metricRetentionPeriods
        
    @property
    def metricRetentionPeriods(self) -> str:
        return self.__metricRetentionPeriods

    @metricRetentionPeriods.setter
    def metricRetentionPeriods(self, metricRetentionPeriods: str):
        self.__metricRetentionPeriods = metricRetentionPeriods

class metrics_EObject:

    pass
class Rule:

    pass
class metrics_MetricRetentionRule(Rule):

    def __init__(self, intervalHint: str, period: str, metrics_MetricRetentionRule: "metrics_MetricRetentionRules" = None):
        self.intervalHint = intervalHint
        self.period = period
        self.metrics_MetricRetentionRule = metrics_MetricRetentionRule
        
    @property
    def period(self) -> str:
        return self.__period

    @period.setter
    def period(self, period: str):
        self.__period = period

    @property
    def intervalHint(self) -> str:
        return self.__intervalHint

    @intervalHint.setter
    def intervalHint(self, intervalHint: str):
        self.__intervalHint = intervalHint

    @property
    def metrics_MetricRetentionRule(self):
        return self.__metrics_MetricRetentionRule

    @metrics_MetricRetentionRule.setter
    def metrics_MetricRetentionRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricRetentionRule__metrics_MetricRetentionRule", None)
        self.__metrics_MetricRetentionRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricRetentionRules18"):
                opp_val = getattr(old_value, "metrics_MetricRetentionRules18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricRetentionRules18"):
                opp_val = getattr(value, "metrics_MetricRetentionRules18", None)
                if opp_val is None:
                    setattr(value, "metrics_MetricRetentionRules18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metrics_MetricAggregationRule(Rule):

    def __init__(self, intervalHint: str, period: str, metrics_MetricAggregationRule: "metrics_EObject" = None, metrics_MetricAggregationRule16: "metrics_MetricAggregationRules" = None):
        self.intervalHint = intervalHint
        self.period = period
        self.metrics_MetricAggregationRule = metrics_MetricAggregationRule
        self.metrics_MetricAggregationRule16 = metrics_MetricAggregationRule16
        
    @property
    def intervalHint(self) -> str:
        return self.__intervalHint

    @intervalHint.setter
    def intervalHint(self, intervalHint: str):
        self.__intervalHint = intervalHint

    @property
    def period(self) -> str:
        return self.__period

    @period.setter
    def period(self, period: str):
        self.__period = period

    @property
    def metrics_MetricAggregationRule16(self):
        return self.__metrics_MetricAggregationRule16

    @metrics_MetricAggregationRule16.setter
    def metrics_MetricAggregationRule16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricAggregationRule__metrics_MetricAggregationRule16", None)
        self.__metrics_MetricAggregationRule16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricAggregationRules15"):
                opp_val = getattr(old_value, "metrics_MetricAggregationRules15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricAggregationRules15"):
                opp_val = getattr(value, "metrics_MetricAggregationRules15", None)
                if opp_val is None:
                    setattr(value, "metrics_MetricAggregationRules15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metrics_MetricAggregationRule(self):
        return self.__metrics_MetricAggregationRule

    @metrics_MetricAggregationRule.setter
    def metrics_MetricAggregationRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricAggregationRule__metrics_MetricAggregationRule", None)
        self.__metrics_MetricAggregationRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_EObject"):
                opp_val = getattr(old_value, "metrics_EObject", None)
                if opp_val == self:
                    setattr(old_value, "metrics_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_EObject"):
                opp_val = getattr(value, "metrics_EObject", None)
                setattr(value, "metrics_EObject", self)

class Base:

    pass
class metrics_MetricAggregationRules:

    pass
class metrics_MetricRetentionRules:

    pass
class metrics_MetricSource(Base):

    def __init__(self, name: str, metrics_MetricSource: "metrics_Addon" = None, metrics_MetricSource20: "metrics_MetricAggregationRules" = None, metrics_MetricSource23: "metrics_MetricRetentionRules" = None):
        self.name = name
        self.metrics_MetricSource = metrics_MetricSource
        self.metrics_MetricSource20 = metrics_MetricSource20
        self.metrics_MetricSource23 = metrics_MetricSource23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metrics_MetricSource20(self):
        return self.__metrics_MetricSource20

    @metrics_MetricSource20.setter
    def metrics_MetricSource20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metrics_MetricSource20", None)
        self.__metrics_MetricSource20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricAggregationRules21"):
                opp_val = getattr(old_value, "metrics_MetricAggregationRules21", None)
                if opp_val == self:
                    setattr(old_value, "metrics_MetricAggregationRules21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricAggregationRules21"):
                opp_val = getattr(value, "metrics_MetricAggregationRules21", None)
                setattr(value, "metrics_MetricAggregationRules21", self)

    @property
    def metrics_MetricSource23(self):
        return self.__metrics_MetricSource23

    @metrics_MetricSource23.setter
    def metrics_MetricSource23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_MetricSource__metrics_MetricSource23", None)
        self.__metrics_MetricSource23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricRetentionRules24"):
                opp_val = getattr(old_value, "metrics_MetricRetentionRules24", None)
                if opp_val == self:
                    setattr(old_value, "metrics_MetricRetentionRules24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricRetentionRules24"):
                opp_val = getattr(value, "metrics_MetricRetentionRules24", None)
                setattr(value, "metrics_MetricRetentionRules24", self)

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
            if hasattr(old_value, "metrics_Addon2"):
                opp_val = getattr(old_value, "metrics_Addon2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Addon2"):
                opp_val = getattr(value, "metrics_Addon2", None)
                if opp_val is None:
                    setattr(value, "metrics_Addon2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metrics_Metric(Base):

    def __init__(self, name: str, metrics_Metric: "metrics_Addon" = None, metrics_Metric8: "metrics_MetricAggregationRules" = None, metrics_Metric11: "metrics_MetricRetentionRules" = None):
        self.name = name
        self.metrics_Metric = metrics_Metric
        self.metrics_Metric8 = metrics_Metric8
        self.metrics_Metric11 = metrics_Metric11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metrics_Metric8(self):
        return self.__metrics_Metric8

    @metrics_Metric8.setter
    def metrics_Metric8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric8", None)
        self.__metrics_Metric8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricAggregationRules9"):
                opp_val = getattr(old_value, "metrics_MetricAggregationRules9", None)
                if opp_val == self:
                    setattr(old_value, "metrics_MetricAggregationRules9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricAggregationRules9"):
                opp_val = getattr(value, "metrics_MetricAggregationRules9", None)
                setattr(value, "metrics_MetricAggregationRules9", self)

    @property
    def metrics_Metric11(self):
        return self.__metrics_Metric11

    @metrics_Metric11.setter
    def metrics_Metric11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_Metric__metrics_Metric11", None)
        self.__metrics_Metric11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_MetricRetentionRules12"):
                opp_val = getattr(old_value, "metrics_MetricRetentionRules12", None)
                if opp_val == self:
                    setattr(old_value, "metrics_MetricRetentionRules12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_MetricRetentionRules12"):
                opp_val = getattr(value, "metrics_MetricRetentionRules12", None)
                setattr(value, "metrics_MetricRetentionRules12", self)

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
            if hasattr(old_value, "metrics_Addon"):
                opp_val = getattr(old_value, "metrics_Addon", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Addon"):
                opp_val = getattr(value, "metrics_Addon", None)
                if opp_val is None:
                    setattr(value, "metrics_Addon", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metrics_Addon:

    pass