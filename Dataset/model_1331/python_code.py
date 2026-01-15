from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElementCS:

    pass
class classescs_PropertyCS(NamedElementCS):

    pass
class classescs_ArgumentCS(NamedElementCS):

    pass
class classescs_ClassCS(NamedElementCS):

    pass
class classescs_PackageCS(NamedElementCS):

    pass
class classescs_PathElementCS(NamedElementCS):

    pass
class classescs_OperationCS(NamedElementCS):

    def __init__(self, params: str, classescs_OperationCS: "classescs_ClassCS" = None, classescs_OperationCS19: set["classescs_NameExpCS"] = None, classescs_OperationCS21: "classescs_PathNameCS" = None):
        self.params = params
        self.classescs_OperationCS = classescs_OperationCS
        self.classescs_OperationCS19 = classescs_OperationCS19 if classescs_OperationCS19 is not None else set()
        self.classescs_OperationCS21 = classescs_OperationCS21
        
    @property
    def params(self) -> str:
        return self.__params

    @params.setter
    def params(self, params: str):
        self.__params = params

    @property
    def classescs_OperationCS19(self):
        return self.__classescs_OperationCS19

    @classescs_OperationCS19.setter
    def classescs_OperationCS19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classescs_OperationCS__classescs_OperationCS19", None)
        self.__classescs_OperationCS19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classescs_NameExpCS"):
                    opp_val = getattr(item, "classescs_NameExpCS", None)
                    
                    if opp_val == self:
                        setattr(item, "classescs_NameExpCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classescs_NameExpCS"):
                    opp_val = getattr(item, "classescs_NameExpCS", None)
                    
                    setattr(item, "classescs_NameExpCS", self)
                    

    @property
    def classescs_OperationCS(self):
        return self.__classescs_OperationCS

    @classescs_OperationCS.setter
    def classescs_OperationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classescs_OperationCS__classescs_OperationCS", None)
        self.__classescs_OperationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classescs_ClassCS10"):
                opp_val = getattr(old_value, "classescs_ClassCS10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classescs_ClassCS10"):
                opp_val = getattr(value, "classescs_ClassCS10", None)
                if opp_val is None:
                    setattr(value, "classescs_ClassCS10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classescs_OperationCS21(self):
        return self.__classescs_OperationCS21

    @classescs_OperationCS21.setter
    def classescs_OperationCS21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classescs_OperationCS__classescs_OperationCS21", None)
        self.__classescs_OperationCS21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classescs_PathNameCS22"):
                opp_val = getattr(old_value, "classescs_PathNameCS22", None)
                if opp_val == self:
                    setattr(old_value, "classescs_PathNameCS22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classescs_PathNameCS22"):
                opp_val = getattr(value, "classescs_PathNameCS22", None)
                setattr(value, "classescs_PathNameCS22", self)

class ElementCS:

    pass
class classescs_PathNameCS(ElementCS):

    pass
class classescs_RootCS(ElementCS):

    pass
class classescs_NameExpCS(ElementCS):

    pass
class classescs_RoundedBracketClause(ElementCS):

    pass
class classescs_NamedElementCS(ElementCS):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class classescs_EObject:

    pass
class classescs_ElementCS(ABC):

    pass