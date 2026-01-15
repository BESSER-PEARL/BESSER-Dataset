from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dSLPolicies_GraphElement:

    def __init__(self, name: str, dSLPolicies_GraphElement: "dSLPolicies_StopCondition" = None):
        self.name = name
        self.dSLPolicies_GraphElement = dSLPolicies_GraphElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dSLPolicies_GraphElement(self):
        return self.__dSLPolicies_GraphElement

    @dSLPolicies_GraphElement.setter
    def dSLPolicies_GraphElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSLPolicies_GraphElement__dSLPolicies_GraphElement", None)
        self.__dSLPolicies_GraphElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSLPolicies_StopCondition15"):
                opp_val = getattr(old_value, "dSLPolicies_StopCondition15", None)
                if opp_val == self:
                    setattr(old_value, "dSLPolicies_StopCondition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSLPolicies_StopCondition15"):
                opp_val = getattr(value, "dSLPolicies_StopCondition15", None)
                setattr(value, "dSLPolicies_StopCondition15", self)

class dSLPolicies_StopCondition:

    def __init__(self, pathtype: str, value: int, percentage: str, dSLPolicies_StopCondition15: "dSLPolicies_GraphElement" = None, dSLPolicies_StopCondition: "dSLPolicies_PathGeneratorStopCondition" = None, dSLPolicies_StopCondition13: "dSLPolicies_PathGeneratorStopCondition" = None):
        self.pathtype = pathtype
        self.value = value
        self.percentage = percentage
        self.dSLPolicies_StopCondition15 = dSLPolicies_StopCondition15
        self.dSLPolicies_StopCondition = dSLPolicies_StopCondition
        self.dSLPolicies_StopCondition13 = dSLPolicies_StopCondition13
        
    @property
    def pathtype(self) -> str:
        return self.__pathtype

    @pathtype.setter
    def pathtype(self, pathtype: str):
        self.__pathtype = pathtype

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def percentage(self) -> str:
        return self.__percentage

    @percentage.setter
    def percentage(self, percentage: str):
        self.__percentage = percentage

    @property
    def dSLPolicies_StopCondition(self):
        return self.__dSLPolicies_StopCondition

    @dSLPolicies_StopCondition.setter
    def dSLPolicies_StopCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSLPolicies_StopCondition__dSLPolicies_StopCondition", None)
        self.__dSLPolicies_StopCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSLPolicies_PathGeneratorStopCondition10"):
                opp_val = getattr(old_value, "dSLPolicies_PathGeneratorStopCondition10", None)
                if opp_val == self:
                    setattr(old_value, "dSLPolicies_PathGeneratorStopCondition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSLPolicies_PathGeneratorStopCondition10"):
                opp_val = getattr(value, "dSLPolicies_PathGeneratorStopCondition10", None)
                setattr(value, "dSLPolicies_PathGeneratorStopCondition10", self)

    @property
    def dSLPolicies_StopCondition13(self):
        return self.__dSLPolicies_StopCondition13

    @dSLPolicies_StopCondition13.setter
    def dSLPolicies_StopCondition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSLPolicies_StopCondition__dSLPolicies_StopCondition13", None)
        self.__dSLPolicies_StopCondition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSLPolicies_PathGeneratorStopCondition12"):
                opp_val = getattr(old_value, "dSLPolicies_PathGeneratorStopCondition12", None)
                if opp_val == self:
                    setattr(old_value, "dSLPolicies_PathGeneratorStopCondition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSLPolicies_PathGeneratorStopCondition12"):
                opp_val = getattr(value, "dSLPolicies_PathGeneratorStopCondition12", None)
                setattr(value, "dSLPolicies_PathGeneratorStopCondition12", self)

    @property
    def dSLPolicies_StopCondition15(self):
        return self.__dSLPolicies_StopCondition15

    @dSLPolicies_StopCondition15.setter
    def dSLPolicies_StopCondition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSLPolicies_StopCondition__dSLPolicies_StopCondition15", None)
        self.__dSLPolicies_StopCondition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSLPolicies_GraphElement"):
                opp_val = getattr(old_value, "dSLPolicies_GraphElement", None)
                if opp_val == self:
                    setattr(old_value, "dSLPolicies_GraphElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSLPolicies_GraphElement"):
                opp_val = getattr(value, "dSLPolicies_GraphElement", None)
                setattr(value, "dSLPolicies_GraphElement", self)

class dSLPolicies_AlgorithmType:

    def __init__(self, type: str, dSLPolicies_AlgorithmType: "dSLPolicies_PathGeneratorStopCondition" = None):
        self.type = type
        self.dSLPolicies_AlgorithmType = dSLPolicies_AlgorithmType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dSLPolicies_AlgorithmType(self):
        return self.__dSLPolicies_AlgorithmType

    @dSLPolicies_AlgorithmType.setter
    def dSLPolicies_AlgorithmType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSLPolicies_AlgorithmType__dSLPolicies_AlgorithmType", None)
        self.__dSLPolicies_AlgorithmType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSLPolicies_PathGeneratorStopCondition8"):
                opp_val = getattr(old_value, "dSLPolicies_PathGeneratorStopCondition8", None)
                if opp_val == self:
                    setattr(old_value, "dSLPolicies_PathGeneratorStopCondition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSLPolicies_PathGeneratorStopCondition8"):
                opp_val = getattr(value, "dSLPolicies_PathGeneratorStopCondition8", None)
                setattr(value, "dSLPolicies_PathGeneratorStopCondition8", self)

class dSLPolicies_PathGeneratorStopCondition:

    pass
class dSLPolicies_Severity:

    def __init__(self, level: str, dSLPolicies_Severity: "dSLPolicies_Policies" = None):
        self.level = level
        self.dSLPolicies_Severity = dSLPolicies_Severity
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def dSLPolicies_Severity(self):
        return self.__dSLPolicies_Severity

    @dSLPolicies_Severity.setter
    def dSLPolicies_Severity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSLPolicies_Severity__dSLPolicies_Severity", None)
        self.__dSLPolicies_Severity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSLPolicies_Policies6"):
                opp_val = getattr(old_value, "dSLPolicies_Policies6", None)
                if opp_val == self:
                    setattr(old_value, "dSLPolicies_Policies6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSLPolicies_Policies6"):
                opp_val = getattr(value, "dSLPolicies_Policies6", None)
                setattr(value, "dSLPolicies_Policies6", self)

class dSLPolicies_Policies:

    def __init__(self, nocheck: bool, sync: bool, dSLPolicies_Policies: "dSLPolicies_GraphPolicies" = None, dSLPolicies_Policies4: set["dSLPolicies_PathGeneratorStopCondition"] = None, dSLPolicies_Policies6: "dSLPolicies_Severity" = None):
        self.nocheck = nocheck
        self.sync = sync
        self.dSLPolicies_Policies = dSLPolicies_Policies
        self.dSLPolicies_Policies4 = dSLPolicies_Policies4 if dSLPolicies_Policies4 is not None else set()
        self.dSLPolicies_Policies6 = dSLPolicies_Policies6
        
    @property
    def nocheck(self) -> bool:
        return self.__nocheck

    @nocheck.setter
    def nocheck(self, nocheck: bool):
        self.__nocheck = nocheck

    @property
    def sync(self) -> bool:
        return self.__sync

    @sync.setter
    def sync(self, sync: bool):
        self.__sync = sync

    @property
    def dSLPolicies_Policies(self):
        return self.__dSLPolicies_Policies

    @dSLPolicies_Policies.setter
    def dSLPolicies_Policies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSLPolicies_Policies__dSLPolicies_Policies", None)
        self.__dSLPolicies_Policies = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSLPolicies_GraphPolicies2"):
                opp_val = getattr(old_value, "dSLPolicies_GraphPolicies2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSLPolicies_GraphPolicies2"):
                opp_val = getattr(value, "dSLPolicies_GraphPolicies2", None)
                if opp_val is None:
                    setattr(value, "dSLPolicies_GraphPolicies2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dSLPolicies_Policies6(self):
        return self.__dSLPolicies_Policies6

    @dSLPolicies_Policies6.setter
    def dSLPolicies_Policies6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSLPolicies_Policies__dSLPolicies_Policies6", None)
        self.__dSLPolicies_Policies6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSLPolicies_Severity"):
                opp_val = getattr(old_value, "dSLPolicies_Severity", None)
                if opp_val == self:
                    setattr(old_value, "dSLPolicies_Severity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSLPolicies_Severity"):
                opp_val = getattr(value, "dSLPolicies_Severity", None)
                setattr(value, "dSLPolicies_Severity", self)

    @property
    def dSLPolicies_Policies4(self):
        return self.__dSLPolicies_Policies4

    @dSLPolicies_Policies4.setter
    def dSLPolicies_Policies4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSLPolicies_Policies__dSLPolicies_Policies4", None)
        self.__dSLPolicies_Policies4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dSLPolicies_PathGeneratorStopCondition"):
                    opp_val = getattr(item, "dSLPolicies_PathGeneratorStopCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "dSLPolicies_PathGeneratorStopCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dSLPolicies_PathGeneratorStopCondition"):
                    opp_val = getattr(item, "dSLPolicies_PathGeneratorStopCondition", None)
                    
                    setattr(item, "dSLPolicies_PathGeneratorStopCondition", self)
                    

class dSLPolicies_GraphPolicies:

    def __init__(self, graphModelPolicies: str, dSLPolicies_GraphPolicies: "dSLPolicies_Model" = None, dSLPolicies_GraphPolicies2: set["dSLPolicies_Policies"] = None):
        self.graphModelPolicies = graphModelPolicies
        self.dSLPolicies_GraphPolicies = dSLPolicies_GraphPolicies
        self.dSLPolicies_GraphPolicies2 = dSLPolicies_GraphPolicies2 if dSLPolicies_GraphPolicies2 is not None else set()
        
    @property
    def graphModelPolicies(self) -> str:
        return self.__graphModelPolicies

    @graphModelPolicies.setter
    def graphModelPolicies(self, graphModelPolicies: str):
        self.__graphModelPolicies = graphModelPolicies

    @property
    def dSLPolicies_GraphPolicies2(self):
        return self.__dSLPolicies_GraphPolicies2

    @dSLPolicies_GraphPolicies2.setter
    def dSLPolicies_GraphPolicies2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSLPolicies_GraphPolicies__dSLPolicies_GraphPolicies2", None)
        self.__dSLPolicies_GraphPolicies2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dSLPolicies_Policies"):
                    opp_val = getattr(item, "dSLPolicies_Policies", None)
                    
                    if opp_val == self:
                        setattr(item, "dSLPolicies_Policies", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dSLPolicies_Policies"):
                    opp_val = getattr(item, "dSLPolicies_Policies", None)
                    
                    setattr(item, "dSLPolicies_Policies", self)
                    

    @property
    def dSLPolicies_GraphPolicies(self):
        return self.__dSLPolicies_GraphPolicies

    @dSLPolicies_GraphPolicies.setter
    def dSLPolicies_GraphPolicies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSLPolicies_GraphPolicies__dSLPolicies_GraphPolicies", None)
        self.__dSLPolicies_GraphPolicies = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSLPolicies_Model"):
                opp_val = getattr(old_value, "dSLPolicies_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSLPolicies_Model"):
                opp_val = getattr(value, "dSLPolicies_Model", None)
                if opp_val is None:
                    setattr(value, "dSLPolicies_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dSLPolicies_Model:

    pass