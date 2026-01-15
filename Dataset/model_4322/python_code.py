from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Metric:

    pass
class metric_Constraint:

    pass
class metric_ConstraintMetric(Metric):

    def __init__(self, calledOperations: str, calledProperties: str, numberOfIfExpressions: int, numberOfLetExpressions: int, usedIterators: str, usedLiterals: str, expressionCount: int, expressionDepth: int, metric_ConstraintMetric4: "metric_Constraint" = None, metric_ConstraintMetric: "metric_ConstraintMetrics" = None):
        self.calledOperations = calledOperations
        self.calledProperties = calledProperties
        self.numberOfIfExpressions = numberOfIfExpressions
        self.numberOfLetExpressions = numberOfLetExpressions
        self.usedIterators = usedIterators
        self.usedLiterals = usedLiterals
        self.expressionCount = expressionCount
        self.expressionDepth = expressionDepth
        self.metric_ConstraintMetric4 = metric_ConstraintMetric4
        self.metric_ConstraintMetric = metric_ConstraintMetric
        
    @property
    def numberOfLetExpressions(self) -> int:
        return self.__numberOfLetExpressions

    @numberOfLetExpressions.setter
    def numberOfLetExpressions(self, numberOfLetExpressions: int):
        self.__numberOfLetExpressions = numberOfLetExpressions

    @property
    def calledOperations(self) -> str:
        return self.__calledOperations

    @calledOperations.setter
    def calledOperations(self, calledOperations: str):
        self.__calledOperations = calledOperations

    @property
    def expressionDepth(self) -> int:
        return self.__expressionDepth

    @expressionDepth.setter
    def expressionDepth(self, expressionDepth: int):
        self.__expressionDepth = expressionDepth

    @property
    def numberOfIfExpressions(self) -> int:
        return self.__numberOfIfExpressions

    @numberOfIfExpressions.setter
    def numberOfIfExpressions(self, numberOfIfExpressions: int):
        self.__numberOfIfExpressions = numberOfIfExpressions

    @property
    def calledProperties(self) -> str:
        return self.__calledProperties

    @calledProperties.setter
    def calledProperties(self, calledProperties: str):
        self.__calledProperties = calledProperties

    @property
    def expressionCount(self) -> int:
        return self.__expressionCount

    @expressionCount.setter
    def expressionCount(self, expressionCount: int):
        self.__expressionCount = expressionCount

    @property
    def usedIterators(self) -> str:
        return self.__usedIterators

    @usedIterators.setter
    def usedIterators(self, usedIterators: str):
        self.__usedIterators = usedIterators

    @property
    def usedLiterals(self) -> str:
        return self.__usedLiterals

    @usedLiterals.setter
    def usedLiterals(self, usedLiterals: str):
        self.__usedLiterals = usedLiterals

    @property
    def metric_ConstraintMetric(self):
        return self.__metric_ConstraintMetric

    @metric_ConstraintMetric.setter
    def metric_ConstraintMetric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metric_ConstraintMetric__metric_ConstraintMetric", None)
        self.__metric_ConstraintMetric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metric_ConstraintMetrics"):
                opp_val = getattr(old_value, "metric_ConstraintMetrics", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metric_ConstraintMetrics"):
                opp_val = getattr(value, "metric_ConstraintMetrics", None)
                if opp_val is None:
                    setattr(value, "metric_ConstraintMetrics", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metric_ConstraintMetric4(self):
        return self.__metric_ConstraintMetric4

    @metric_ConstraintMetric4.setter
    def metric_ConstraintMetric4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metric_ConstraintMetric__metric_ConstraintMetric4", None)
        self.__metric_ConstraintMetric4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metric_Constraint5"):
                opp_val = getattr(old_value, "metric_Constraint5", None)
                if opp_val == self:
                    setattr(old_value, "metric_Constraint5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metric_Constraint5"):
                opp_val = getattr(value, "metric_Constraint5", None)
                setattr(value, "metric_Constraint5", self)

class ConstraintMetric:

    pass
class metric_ConstraintMetrics(ConstraintMetric):

    def __init__(self, numberOfConstraintsByKind: str, metric_ConstraintMetrics: set["metric_ConstraintMetric"] = None, metric_ConstraintMetrics2: set["metric_Constraint"] = None):
        self.numberOfConstraintsByKind = numberOfConstraintsByKind
        self.metric_ConstraintMetrics = metric_ConstraintMetrics if metric_ConstraintMetrics is not None else set()
        self.metric_ConstraintMetrics2 = metric_ConstraintMetrics2 if metric_ConstraintMetrics2 is not None else set()
        
    @property
    def numberOfConstraintsByKind(self) -> str:
        return self.__numberOfConstraintsByKind

    @numberOfConstraintsByKind.setter
    def numberOfConstraintsByKind(self, numberOfConstraintsByKind: str):
        self.__numberOfConstraintsByKind = numberOfConstraintsByKind

    @property
    def metric_ConstraintMetrics(self):
        return self.__metric_ConstraintMetrics

    @metric_ConstraintMetrics.setter
    def metric_ConstraintMetrics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metric_ConstraintMetrics__metric_ConstraintMetrics", None)
        self.__metric_ConstraintMetrics = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metric_ConstraintMetric"):
                    opp_val = getattr(item, "metric_ConstraintMetric", None)
                    
                    if opp_val == self:
                        setattr(item, "metric_ConstraintMetric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metric_ConstraintMetric"):
                    opp_val = getattr(item, "metric_ConstraintMetric", None)
                    
                    setattr(item, "metric_ConstraintMetric", self)
                    

    @property
    def metric_ConstraintMetrics2(self):
        return self.__metric_ConstraintMetrics2

    @metric_ConstraintMetrics2.setter
    def metric_ConstraintMetrics2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metric_ConstraintMetrics__metric_ConstraintMetrics2", None)
        self.__metric_ConstraintMetrics2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metric_Constraint"):
                    opp_val = getattr(item, "metric_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "metric_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metric_Constraint"):
                    opp_val = getattr(item, "metric_Constraint", None)
                    
                    setattr(item, "metric_Constraint", self)
                    

    def getMinExpressionCount(self) -> int:
        # TODO: Implement getMinExpressionCount method
        pass

    def getMinExpressionDepth(self) -> int:
        # TODO: Implement getMinExpressionDepth method
        pass

    def getMaxExpressionCount(self) -> int:
        # TODO: Implement getMaxExpressionCount method
        pass

    def getMaxExpressionDepth(self) -> int:
        # TODO: Implement getMaxExpressionDepth method
        pass

    def getAvgExpressionDepth(self) -> float:
        # TODO: Implement getAvgExpressionDepth method
        pass

    def getAvgExpressionCount(self) -> float:
        # TODO: Implement getAvgExpressionCount method
        pass

    def getMeanExpressionDepth(self) -> int:
        # TODO: Implement getMeanExpressionDepth method
        pass

    def getMeanExpressionCount(self) -> int:
        # TODO: Implement getMeanExpressionCount method
        pass

    def getExpressionCount(self) -> int:
        # TODO: Implement getExpressionCount method
        pass

    def getConstraintCount(self) -> int:
        # TODO: Implement getConstraintCount method
        pass

class metric_Metric:

    def __init__(self):
        
    def getReport(self) -> str:
        # TODO: Implement getReport method
        pass
