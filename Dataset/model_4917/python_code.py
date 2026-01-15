from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OperationResultTypes(Enum):
    None = "None"
    File = "File"


############################################
# Definition of Classes
############################################

class Variable:

    pass
class service_ServiceFeatureReference(Variable):

    def __init__(self, name: str, service_ServiceFeatureReference: "service_Feature" = None):
        self.name = name
        self.service_ServiceFeatureReference = service_ServiceFeatureReference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def service_ServiceFeatureReference(self):
        return self.__service_ServiceFeatureReference

    @service_ServiceFeatureReference.setter
    def service_ServiceFeatureReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_ServiceFeatureReference__service_ServiceFeatureReference", None)
        self.__service_ServiceFeatureReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_Feature17"):
                opp_val = getattr(old_value, "service_Feature17", None)
                if opp_val == self:
                    setattr(old_value, "service_Feature17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_Feature17"):
                opp_val = getattr(value, "service_Feature17", None)
                setattr(value, "service_Feature17", self)

class Order:

    pass
class service_Desc(Order):

    pass
class service_Asc(Order):

    pass
class service_Variable:

    pass
class service_Order(ABC):

    pass
class service_Predicate:

    pass
class service_Association:

    pass
class service_Feature:

    pass
class FormalParameterList:

    pass
class service_EntityOrView:

    pass
class NamedElement:

    pass
class service_Selection(NamedElement, FormalParameterList):

    def __init__(self, limit: int, selected: bool, distinct: bool, Selection: "service_Service" = None, selections: "service_Service" = None, service_Selection: set["service_Feature"] = None, service_Selection9: set["service_Association"] = None, service_Selection11: "service_Predicate" = None, service_Selection13: set["service_Order"] = None):
        self.limit = limit
        self.selected = selected
        self.distinct = distinct
        self.Selection = Selection
        self.selections = selections
        self.service_Selection = service_Selection if service_Selection is not None else set()
        self.service_Selection9 = service_Selection9 if service_Selection9 is not None else set()
        self.service_Selection11 = service_Selection11
        self.service_Selection13 = service_Selection13 if service_Selection13 is not None else set()
        
    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def limit(self) -> int:
        return self.__limit

    @limit.setter
    def limit(self, limit: int):
        self.__limit = limit

    @property
    def distinct(self) -> bool:
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: bool):
        self.__distinct = distinct

    @property
    def selections(self):
        return self.__selections

    @selections.setter
    def selections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__selections", None)
        self.__selections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Service"):
                opp_val = getattr(old_value, "Service", None)
                if opp_val == self:
                    setattr(old_value, "Service", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service"):
                opp_val = getattr(value, "Service", None)
                setattr(value, "Service", self)

    @property
    def service_Selection9(self):
        return self.__service_Selection9

    @service_Selection9.setter
    def service_Selection9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__service_Selection9", None)
        self.__service_Selection9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service_Association"):
                    opp_val = getattr(item, "service_Association", None)
                    
                    if opp_val == self:
                        setattr(item, "service_Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service_Association"):
                    opp_val = getattr(item, "service_Association", None)
                    
                    setattr(item, "service_Association", self)
                    

    @property
    def service_Selection13(self):
        return self.__service_Selection13

    @service_Selection13.setter
    def service_Selection13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__service_Selection13", None)
        self.__service_Selection13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service_Order"):
                    opp_val = getattr(item, "service_Order", None)
                    
                    if opp_val == self:
                        setattr(item, "service_Order", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service_Order"):
                    opp_val = getattr(item, "service_Order", None)
                    
                    setattr(item, "service_Order", self)
                    

    @property
    def service_Selection11(self):
        return self.__service_Selection11

    @service_Selection11.setter
    def service_Selection11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__service_Selection11", None)
        self.__service_Selection11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_Predicate"):
                opp_val = getattr(old_value, "service_Predicate", None)
                if opp_val == self:
                    setattr(old_value, "service_Predicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_Predicate"):
                opp_val = getattr(value, "service_Predicate", None)
                setattr(value, "service_Predicate", self)

    @property
    def Selection(self):
        return self.__Selection

    @Selection.setter
    def Selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__Selection", None)
        self.__Selection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usedBy"):
                opp_val = getattr(old_value, "usedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usedBy"):
                opp_val = getattr(value, "usedBy", None)
                if opp_val is None:
                    setattr(value, "usedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def service_Selection(self):
        return self.__service_Selection

    @service_Selection.setter
    def service_Selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__service_Selection", None)
        self.__service_Selection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service_Feature"):
                    opp_val = getattr(item, "service_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "service_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service_Feature"):
                    opp_val = getattr(item, "service_Feature", None)
                    
                    setattr(item, "service_Feature", self)
                    

class service_BusinessOperation(NamedElement):

    def __init__(self, resultType: str, resultMimeType: str, service_BusinessOperation: "service_Service" = None, service_BusinessOperation19: set["service_Service"] = None):
        self.resultType = resultType
        self.resultMimeType = resultMimeType
        self.service_BusinessOperation = service_BusinessOperation
        self.service_BusinessOperation19 = service_BusinessOperation19 if service_BusinessOperation19 is not None else set()
        
    @property
    def resultMimeType(self) -> str:
        return self.__resultMimeType

    @resultMimeType.setter
    def resultMimeType(self, resultMimeType: str):
        self.__resultMimeType = resultMimeType

    @property
    def resultType(self) -> str:
        return self.__resultType

    @resultType.setter
    def resultType(self, resultType: str):
        self.__resultType = resultType

    @property
    def service_BusinessOperation19(self):
        return self.__service_BusinessOperation19

    @service_BusinessOperation19.setter
    def service_BusinessOperation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_BusinessOperation__service_BusinessOperation19", None)
        self.__service_BusinessOperation19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service_Service20"):
                    opp_val = getattr(item, "service_Service20", None)
                    
                    if opp_val == self:
                        setattr(item, "service_Service20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service_Service20"):
                    opp_val = getattr(item, "service_Service20", None)
                    
                    setattr(item, "service_Service20", self)
                    

    @property
    def service_BusinessOperation(self):
        return self.__service_BusinessOperation

    @service_BusinessOperation.setter
    def service_BusinessOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_BusinessOperation__service_BusinessOperation", None)
        self.__service_BusinessOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_Service5"):
                opp_val = getattr(old_value, "service_Service5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_Service5"):
                opp_val = getattr(value, "service_Service5", None)
                if opp_val is None:
                    setattr(value, "service_Service5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class service_Service(NamedElement):

    pass
class service_Services:

    pass