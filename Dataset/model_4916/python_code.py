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
class service_ConstantReference(Variable):

    def __init__(self, name: str, service_ConstantReference: "service_Constant" = None):
        self.name = name
        self.service_ConstantReference = service_ConstantReference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def service_ConstantReference(self):
        return self.__service_ConstantReference

    @service_ConstantReference.setter
    def service_ConstantReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_ConstantReference__service_ConstantReference", None)
        self.__service_ConstantReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_Constant33"):
                opp_val = getattr(old_value, "service_Constant33", None)
                if opp_val == self:
                    setattr(old_value, "service_Constant33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_Constant33"):
                opp_val = getattr(value, "service_Constant33", None)
                setattr(value, "service_Constant33", self)

class service_Variable:

    pass
class service_EntityAssociation:

    pass
class service_Order(ABC):

    pass
class NamedDisplayElement:

    pass
class Order:

    pass
class service_Desc(Order):

    pass
class service_Asc(Order):

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
            if hasattr(old_value, "service_Feature35"):
                opp_val = getattr(old_value, "service_Feature35", None)
                if opp_val == self:
                    setattr(old_value, "service_Feature35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_Feature35"):
                opp_val = getattr(value, "service_Feature35", None)
                setattr(value, "service_Feature35", self)

class service_EntityOrView:

    pass
class NamedElement:

    pass
class service_Constant(NamedElement):

    pass
class service_Service(NamedElement):

    pass
class service_Predicate:

    pass
class service_Association:

    pass
class service_Feature:

    pass
class FormalParameterList:

    pass
class service_Selection(NamedElement, FormalParameterList):

    def __init__(self, distinct: bool, limit: int, methodName: str, selections: "service_Service" = None, service_Selection20: set["service_Feature"] = None, service_Selection22: set["service_Association"] = None, service_Selection24: "service_Predicate" = None, Selection: "service_Service" = None, service_Selection: "service_Service" = None, service_Selection9: "service_Service" = None, selection: set["service_Filter"] = None, service_Selection27: set["service_Order"] = None, service_Selection29: set["service_EntityAssociation"] = None, Selection41: "service_Filter" = None):
        self.distinct = distinct
        self.limit = limit
        self.methodName = methodName
        self.selections = selections
        self.service_Selection20 = service_Selection20 if service_Selection20 is not None else set()
        self.service_Selection22 = service_Selection22 if service_Selection22 is not None else set()
        self.service_Selection24 = service_Selection24
        self.Selection = Selection
        self.service_Selection = service_Selection
        self.service_Selection9 = service_Selection9
        self.selection = selection if selection is not None else set()
        self.service_Selection27 = service_Selection27 if service_Selection27 is not None else set()
        self.service_Selection29 = service_Selection29 if service_Selection29 is not None else set()
        self.Selection41 = Selection41
        
    @property
    def limit(self) -> int:
        return self.__limit

    @limit.setter
    def limit(self, limit: int):
        self.__limit = limit

    @property
    def methodName(self) -> str:
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName

    @property
    def distinct(self) -> bool:
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: bool):
        self.__distinct = distinct

    @property
    def service_Selection24(self):
        return self.__service_Selection24

    @service_Selection24.setter
    def service_Selection24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__service_Selection24", None)
        self.__service_Selection24 = value
        
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
    def service_Selection27(self):
        return self.__service_Selection27

    @service_Selection27.setter
    def service_Selection27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__service_Selection27", None)
        self.__service_Selection27 = value if value is not None else set()
        
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
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__selection", None)
        self.__selection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Filter"):
                    opp_val = getattr(item, "Filter", None)
                    
                    if opp_val == self:
                        setattr(item, "Filter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Filter"):
                    opp_val = getattr(item, "Filter", None)
                    
                    setattr(item, "Filter", self)
                    

    @property
    def service_Selection20(self):
        return self.__service_Selection20

    @service_Selection20.setter
    def service_Selection20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__service_Selection20", None)
        self.__service_Selection20 = value if value is not None else set()
        
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
                    

    @property
    def service_Selection29(self):
        return self.__service_Selection29

    @service_Selection29.setter
    def service_Selection29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__service_Selection29", None)
        self.__service_Selection29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service_EntityAssociation"):
                    opp_val = getattr(item, "service_EntityAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "service_EntityAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service_EntityAssociation"):
                    opp_val = getattr(item, "service_EntityAssociation", None)
                    
                    setattr(item, "service_EntityAssociation", self)
                    

    @property
    def service_Selection(self):
        return self.__service_Selection

    @service_Selection.setter
    def service_Selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__service_Selection", None)
        self.__service_Selection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_Service6"):
                opp_val = getattr(old_value, "service_Service6", None)
                if opp_val == self:
                    setattr(old_value, "service_Service6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_Service6"):
                opp_val = getattr(value, "service_Service6", None)
                setattr(value, "service_Service6", self)

    @property
    def service_Selection22(self):
        return self.__service_Selection22

    @service_Selection22.setter
    def service_Selection22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__service_Selection22", None)
        self.__service_Selection22 = value if value is not None else set()
        
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
    def Selection41(self):
        return self.__Selection41

    @Selection41.setter
    def Selection41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__Selection41", None)
        self.__Selection41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "filters"):
                opp_val = getattr(old_value, "filters", None)
                if opp_val == self:
                    setattr(old_value, "filters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "filters"):
                opp_val = getattr(value, "filters", None)
                setattr(value, "filters", self)

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
            if hasattr(old_value, "Service18"):
                opp_val = getattr(old_value, "Service18", None)
                if opp_val == self:
                    setattr(old_value, "Service18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service18"):
                opp_val = getattr(value, "Service18", None)
                setattr(value, "Service18", self)

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
    def service_Selection9(self):
        return self.__service_Selection9

    @service_Selection9.setter
    def service_Selection9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Selection__service_Selection9", None)
        self.__service_Selection9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_Service8"):
                opp_val = getattr(old_value, "service_Service8", None)
                if opp_val == self:
                    setattr(old_value, "service_Service8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_Service8"):
                opp_val = getattr(value, "service_Service8", None)
                setattr(value, "service_Service8", self)

class service_Filter(NamedDisplayElement, FormalParameterList):

    def __init__(self, methodName: str, Filter: "service_Selection" = None, filters: "service_Selection" = None, service_Filter: "service_Predicate" = None):
        self.methodName = methodName
        self.Filter = Filter
        self.filters = filters
        self.service_Filter = service_Filter
        
    @property
    def methodName(self) -> str:
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName

    @property
    def filters(self):
        return self.__filters

    @filters.setter
    def filters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Filter__filters", None)
        self.__filters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Selection41"):
                opp_val = getattr(old_value, "Selection41", None)
                if opp_val == self:
                    setattr(old_value, "Selection41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Selection41"):
                opp_val = getattr(value, "Selection41", None)
                setattr(value, "Selection41", self)

    @property
    def Filter(self):
        return self.__Filter

    @Filter.setter
    def Filter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Filter__Filter", None)
        self.__Filter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selection"):
                opp_val = getattr(old_value, "selection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selection"):
                opp_val = getattr(value, "selection", None)
                if opp_val is None:
                    setattr(value, "selection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def service_Filter(self):
        return self.__service_Filter

    @service_Filter.setter
    def service_Filter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Filter__service_Filter", None)
        self.__service_Filter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_Predicate43"):
                opp_val = getattr(old_value, "service_Predicate43", None)
                if opp_val == self:
                    setattr(old_value, "service_Predicate43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_Predicate43"):
                opp_val = getattr(value, "service_Predicate43", None)
                setattr(value, "service_Predicate43", self)

class service_BusinessOperation(NamedElement, FormalParameterList):

    def __init__(self, resultType: str, resultMimeType: str, BusinessOperation: "service_Service" = None, operations: "service_Service" = None, service_BusinessOperation: set["service_Service"] = None):
        self.resultType = resultType
        self.resultMimeType = resultMimeType
        self.BusinessOperation = BusinessOperation
        self.operations = operations
        self.service_BusinessOperation = service_BusinessOperation if service_BusinessOperation is not None else set()
        
    @property
    def resultType(self) -> str:
        return self.__resultType

    @resultType.setter
    def resultType(self, resultType: str):
        self.__resultType = resultType

    @property
    def resultMimeType(self) -> str:
        return self.__resultMimeType

    @resultMimeType.setter
    def resultMimeType(self, resultMimeType: str):
        self.__resultMimeType = resultMimeType

    @property
    def BusinessOperation(self):
        return self.__BusinessOperation

    @BusinessOperation.setter
    def BusinessOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_BusinessOperation__BusinessOperation", None)
        self.__BusinessOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "definedBy11"):
                opp_val = getattr(old_value, "definedBy11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "definedBy11"):
                opp_val = getattr(value, "definedBy11", None)
                if opp_val is None:
                    setattr(value, "definedBy11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def service_BusinessOperation(self):
        return self.__service_BusinessOperation

    @service_BusinessOperation.setter
    def service_BusinessOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_BusinessOperation__service_BusinessOperation", None)
        self.__service_BusinessOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service_Service39"):
                    opp_val = getattr(item, "service_Service39", None)
                    
                    if opp_val == self:
                        setattr(item, "service_Service39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service_Service39"):
                    opp_val = getattr(item, "service_Service39", None)
                    
                    setattr(item, "service_Service39", self)
                    

    @property
    def operations(self):
        return self.__operations

    @operations.setter
    def operations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_BusinessOperation__operations", None)
        self.__operations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Service37"):
                opp_val = getattr(old_value, "Service37", None)
                if opp_val == self:
                    setattr(old_value, "Service37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service37"):
                opp_val = getattr(value, "Service37", None)
                setattr(value, "Service37", self)

class service_Expression:

    pass
class service_Services:

    pass