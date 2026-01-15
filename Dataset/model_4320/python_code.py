from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class metrics_RuleSetMetrics:

    def __init__(self, numberOfRules: int, totalNumberOfNodes: int, totalNumberOfEdges: int, totalNumberOfAttributes: int, metrics_RuleSetMetrics: set["metrics_RuleMetrics"] = None, metrics_RuleSetMetrics2: set["metrics_Rule"] = None):
        self.numberOfRules = numberOfRules
        self.totalNumberOfNodes = totalNumberOfNodes
        self.totalNumberOfEdges = totalNumberOfEdges
        self.totalNumberOfAttributes = totalNumberOfAttributes
        self.metrics_RuleSetMetrics = metrics_RuleSetMetrics if metrics_RuleSetMetrics is not None else set()
        self.metrics_RuleSetMetrics2 = metrics_RuleSetMetrics2 if metrics_RuleSetMetrics2 is not None else set()
        
    @property
    def numberOfRules(self) -> int:
        return self.__numberOfRules

    @numberOfRules.setter
    def numberOfRules(self, numberOfRules: int):
        self.__numberOfRules = numberOfRules

    @property
    def totalNumberOfAttributes(self) -> int:
        return self.__totalNumberOfAttributes

    @totalNumberOfAttributes.setter
    def totalNumberOfAttributes(self, totalNumberOfAttributes: int):
        self.__totalNumberOfAttributes = totalNumberOfAttributes

    @property
    def totalNumberOfNodes(self) -> int:
        return self.__totalNumberOfNodes

    @totalNumberOfNodes.setter
    def totalNumberOfNodes(self, totalNumberOfNodes: int):
        self.__totalNumberOfNodes = totalNumberOfNodes

    @property
    def totalNumberOfEdges(self) -> int:
        return self.__totalNumberOfEdges

    @totalNumberOfEdges.setter
    def totalNumberOfEdges(self, totalNumberOfEdges: int):
        self.__totalNumberOfEdges = totalNumberOfEdges

    @property
    def metrics_RuleSetMetrics(self):
        return self.__metrics_RuleSetMetrics

    @metrics_RuleSetMetrics.setter
    def metrics_RuleSetMetrics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_RuleSetMetrics__metrics_RuleSetMetrics", None)
        self.__metrics_RuleSetMetrics = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_RuleMetrics"):
                    opp_val = getattr(item, "metrics_RuleMetrics", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_RuleMetrics", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_RuleMetrics"):
                    opp_val = getattr(item, "metrics_RuleMetrics", None)
                    
                    setattr(item, "metrics_RuleMetrics", self)
                    

    @property
    def metrics_RuleSetMetrics2(self):
        return self.__metrics_RuleSetMetrics2

    @metrics_RuleSetMetrics2.setter
    def metrics_RuleSetMetrics2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_RuleSetMetrics__metrics_RuleSetMetrics2", None)
        self.__metrics_RuleSetMetrics2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics_Rule"):
                    opp_val = getattr(item, "metrics_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "metrics_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics_Rule"):
                    opp_val = getattr(item, "metrics_Rule", None)
                    
                    setattr(item, "metrics_Rule", self)
                    

    def createPresentationString(self) -> str:
        # TODO: Implement createPresentationString method
        pass

    def findRuleMetrics(self, rule: str) -> str:
        # TODO: Implement findRuleMetrics method
        pass

class metrics_Rule:

    pass
class metrics_RuleMetrics:

    def __init__(self, numberOfNodes: int, numberOfEdges: int, numberOfAttributes: int, metrics_RuleMetrics: "metrics_RuleSetMetrics" = None, metrics_RuleMetrics4: "metrics_Rule" = None):
        self.numberOfNodes = numberOfNodes
        self.numberOfEdges = numberOfEdges
        self.numberOfAttributes = numberOfAttributes
        self.metrics_RuleMetrics = metrics_RuleMetrics
        self.metrics_RuleMetrics4 = metrics_RuleMetrics4
        
    @property
    def numberOfAttributes(self) -> int:
        return self.__numberOfAttributes

    @numberOfAttributes.setter
    def numberOfAttributes(self, numberOfAttributes: int):
        self.__numberOfAttributes = numberOfAttributes

    @property
    def numberOfEdges(self) -> int:
        return self.__numberOfEdges

    @numberOfEdges.setter
    def numberOfEdges(self, numberOfEdges: int):
        self.__numberOfEdges = numberOfEdges

    @property
    def numberOfNodes(self) -> int:
        return self.__numberOfNodes

    @numberOfNodes.setter
    def numberOfNodes(self, numberOfNodes: int):
        self.__numberOfNodes = numberOfNodes

    @property
    def metrics_RuleMetrics(self):
        return self.__metrics_RuleMetrics

    @metrics_RuleMetrics.setter
    def metrics_RuleMetrics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_RuleMetrics__metrics_RuleMetrics", None)
        self.__metrics_RuleMetrics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_RuleSetMetrics"):
                opp_val = getattr(old_value, "metrics_RuleSetMetrics", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_RuleSetMetrics"):
                opp_val = getattr(value, "metrics_RuleSetMetrics", None)
                if opp_val is None:
                    setattr(value, "metrics_RuleSetMetrics", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metrics_RuleMetrics4(self):
        return self.__metrics_RuleMetrics4

    @metrics_RuleMetrics4.setter
    def metrics_RuleMetrics4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metrics_RuleMetrics__metrics_RuleMetrics4", None)
        self.__metrics_RuleMetrics4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metrics_Rule5"):
                opp_val = getattr(old_value, "metrics_Rule5", None)
                if opp_val == self:
                    setattr(old_value, "metrics_Rule5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metrics_Rule5"):
                opp_val = getattr(value, "metrics_Rule5", None)
                setattr(value, "metrics_Rule5", self)
