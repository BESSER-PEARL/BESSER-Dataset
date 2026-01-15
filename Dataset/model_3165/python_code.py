from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class gtrace_TTraceModel:

    def __init__(self, name: str, gtrace_TTraceModel: set["gtrace_TRequirementTrace"] = None, gtrace_TTraceModel2: set["gtrace_TScenarioTrace"] = None, gtrace_TTraceModel4: set["gtrace_TScenarioStepTrace"] = None):
        self.name = name
        self.gtrace_TTraceModel = gtrace_TTraceModel if gtrace_TTraceModel is not None else set()
        self.gtrace_TTraceModel2 = gtrace_TTraceModel2 if gtrace_TTraceModel2 is not None else set()
        self.gtrace_TTraceModel4 = gtrace_TTraceModel4 if gtrace_TTraceModel4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gtrace_TTraceModel4(self):
        return self.__gtrace_TTraceModel4

    @gtrace_TTraceModel4.setter
    def gtrace_TTraceModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gtrace_TTraceModel__gtrace_TTraceModel4", None)
        self.__gtrace_TTraceModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gtrace_TScenarioStepTrace"):
                    opp_val = getattr(item, "gtrace_TScenarioStepTrace", None)
                    
                    if opp_val == self:
                        setattr(item, "gtrace_TScenarioStepTrace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gtrace_TScenarioStepTrace"):
                    opp_val = getattr(item, "gtrace_TScenarioStepTrace", None)
                    
                    setattr(item, "gtrace_TScenarioStepTrace", self)
                    

    @property
    def gtrace_TTraceModel2(self):
        return self.__gtrace_TTraceModel2

    @gtrace_TTraceModel2.setter
    def gtrace_TTraceModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gtrace_TTraceModel__gtrace_TTraceModel2", None)
        self.__gtrace_TTraceModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gtrace_TScenarioTrace"):
                    opp_val = getattr(item, "gtrace_TScenarioTrace", None)
                    
                    if opp_val == self:
                        setattr(item, "gtrace_TScenarioTrace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gtrace_TScenarioTrace"):
                    opp_val = getattr(item, "gtrace_TScenarioTrace", None)
                    
                    setattr(item, "gtrace_TScenarioTrace", self)
                    

    @property
    def gtrace_TTraceModel(self):
        return self.__gtrace_TTraceModel

    @gtrace_TTraceModel.setter
    def gtrace_TTraceModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gtrace_TTraceModel__gtrace_TTraceModel", None)
        self.__gtrace_TTraceModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gtrace_TRequirementTrace"):
                    opp_val = getattr(item, "gtrace_TRequirementTrace", None)
                    
                    if opp_val == self:
                        setattr(item, "gtrace_TRequirementTrace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gtrace_TRequirementTrace"):
                    opp_val = getattr(item, "gtrace_TRequirementTrace", None)
                    
                    setattr(item, "gtrace_TRequirementTrace", self)
                    

class gtrace_MState:

    pass
class gtrace_MOperation:

    pass
class gtrace_RScenarioStep:

    pass
class gtrace_MStateMachine:

    pass
class gtrace_MClassifier:

    pass
class gtrace_RScenario:

    pass
class gtrace_MElement:

    pass
class gtrace_RRequirement:

    pass
class TTrace:

    pass
class gtrace_TTrace(ABC):

    def __init__(self, reviewed: str):
        self.reviewed = reviewed
        
    @property
    def reviewed(self) -> str:
        return self.__reviewed

    @reviewed.setter
    def reviewed(self, reviewed: str):
        self.__reviewed = reviewed

class gtrace_TScenarioStepTrace(TTrace):

    pass
class gtrace_TScenarioTrace(TTrace):

    pass
class gtrace_TRequirementTrace(TTrace):

    pass