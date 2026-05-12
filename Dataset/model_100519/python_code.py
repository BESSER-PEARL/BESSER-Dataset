from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Tenses(Enum):
    both = "both"
    present = "present"
class ActionTypeStatus(Enum):
    resolved = "resolved"
    unresolved = "unresolved"


############################################
# Definition of Classes
############################################

class NameContainer:

    pass
class schema_ActionLike(ABC):

    def __init__(self, tenses: str, pastTense: str, pluralPastTense: str, presentTense: str, pluralPresentTense: str, imperativeTense: str):
        self.tenses = tenses
        self.pastTense = pastTense
        self.pluralPastTense = pluralPastTense
        self.presentTense = presentTense
        self.pluralPresentTense = pluralPresentTense
        self.imperativeTense = imperativeTense
        
        pass
    @property
    def pluralPastTense(self):
        return self.__pluralPastTense

    @pluralPastTense.setter
    def pluralPastTense(self, pluralPastTense: str):
        self.__pluralPastTense = pluralPastTense


    @property
    def tenses(self):
        return self.__tenses

    @tenses.setter
    def tenses(self, tenses: str):
        self.__tenses = tenses


    @property
    def pastTense(self):
        return self.__pastTense

    @pastTense.setter
    def pastTense(self, pastTense: str):
        self.__pastTense = pastTense


    @property
    def pluralPresentTense(self):
        return self.__pluralPresentTense

    @pluralPresentTense.setter
    def pluralPresentTense(self, pluralPresentTense: str):
        self.__pluralPresentTense = pluralPresentTense


    @property
    def presentTense(self):
        return self.__presentTense

    @presentTense.setter
    def presentTense(self, presentTense: str):
        self.__presentTense = presentTense


    @property
    def imperativeTense(self):
        return self.__imperativeTense

    @imperativeTense.setter
    def imperativeTense(self, imperativeTense: str):
        self.__imperativeTense = imperativeTense


class schema_EFactory:

    pass
class schema_EPackage:

    pass
class schema_TargetType:

    pass
class schema_AggregationType:

    def __init__(self, schema_AggregationType: "schema_StorySchemaCatalog" = None):
        self.schema_AggregationType = schema_AggregationType
        
        pass
    @property
    def schema_AggregationType(self):
        return self.__schema_AggregationType

    @schema_AggregationType.setter
    def schema_AggregationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schema_AggregationType__schema_AggregationType", None)
        self.__schema_AggregationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema_StorySchemaCatalog4"):
                opp_val = getattr(old_value, "schema_StorySchemaCatalog4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema_StorySchemaCatalog4"):
                opp_val = getattr(value, "schema_StorySchemaCatalog4", None)
                if opp_val is None:
                    setattr(value, "schema_StorySchemaCatalog4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def create(self) :
        # TODO: Implement create method
        pass

class schema_ActionType:

    def __init__(self, status: str, schema_ActionType: "schema_StorySchemaCatalog" = None, schema_ActionType10: set["schema_TargetType"] = None, schema_ActionType12: set["schema_TargetTypeRef"] = None):
        self.status = status
        self.schema_ActionType = schema_ActionType
        self.schema_ActionType10 = schema_ActionType10 if schema_ActionType10 is not None else set()
        self.schema_ActionType12 = schema_ActionType12 if schema_ActionType12 is not None else set()
        
        pass
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def schema_ActionType(self):
        return self.__schema_ActionType

    @schema_ActionType.setter
    def schema_ActionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schema_ActionType__schema_ActionType", None)
        self.__schema_ActionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema_StorySchemaCatalog2"):
                opp_val = getattr(old_value, "schema_StorySchemaCatalog2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema_StorySchemaCatalog2"):
                opp_val = getattr(value, "schema_StorySchemaCatalog2", None)
                if opp_val is None:
                    setattr(value, "schema_StorySchemaCatalog2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def schema_ActionType10(self):
        return self.__schema_ActionType10

    @schema_ActionType10.setter
    def schema_ActionType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schema_ActionType__schema_ActionType10", None)
        self.__schema_ActionType10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schema_TargetType"):
                    opp_val = getattr(item, "schema_TargetType", None)
                    
                    if opp_val == self:
                        setattr(item, "schema_TargetType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schema_TargetType"):
                    opp_val = getattr(item, "schema_TargetType", None)
                    
                    setattr(item, "schema_TargetType", self)
                    

    @property
    def schema_ActionType12(self):
        return self.__schema_ActionType12

    @schema_ActionType12.setter
    def schema_ActionType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schema_ActionType__schema_ActionType12", None)
        self.__schema_ActionType12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schema_TargetTypeRef"):
                    opp_val = getattr(item, "schema_TargetTypeRef", None)
                    
                    if opp_val == self:
                        setattr(item, "schema_TargetTypeRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schema_TargetTypeRef"):
                    opp_val = getattr(item, "schema_TargetTypeRef", None)
                    
                    setattr(item, "schema_TargetTypeRef", self)
                    

    def create(self) :
        # TODO: Implement create method
        pass

class schema_StoryType:

    pass
class NsPrefixable:

    pass
class schema_TargetTypeRef(NsPrefixable, NameContainer):

    pass
class BundleAware:

    pass
class ResourceAware:

    pass
class schema_StorySchemaCatalog(NsPrefixable, ResourceAware, BundleAware):

    def __init__(self, generatedPackageName: str, xmiUrl: str, ecoreUrl: str, schema_StorySchemaCatalog4: set["schema_AggregationType"] = None, schema_StorySchemaCatalog: set["schema_StoryType"] = None, schema_StorySchemaCatalog2: set["schema_ActionType"] = None, schema_StorySchemaCatalog6: "schema_EPackage" = None, schema_StorySchemaCatalog8: "schema_EFactory" = None):
        self.generatedPackageName = generatedPackageName
        self.xmiUrl = xmiUrl
        self.ecoreUrl = ecoreUrl
        self.schema_StorySchemaCatalog4 = schema_StorySchemaCatalog4 if schema_StorySchemaCatalog4 is not None else set()
        self.schema_StorySchemaCatalog = schema_StorySchemaCatalog if schema_StorySchemaCatalog is not None else set()
        self.schema_StorySchemaCatalog2 = schema_StorySchemaCatalog2 if schema_StorySchemaCatalog2 is not None else set()
        self.schema_StorySchemaCatalog6 = schema_StorySchemaCatalog6
        self.schema_StorySchemaCatalog8 = schema_StorySchemaCatalog8
        
        pass
    @property
    def xmiUrl(self):
        return self.__xmiUrl

    @xmiUrl.setter
    def xmiUrl(self, xmiUrl: str):
        self.__xmiUrl = xmiUrl


    @property
    def ecoreUrl(self):
        return self.__ecoreUrl

    @ecoreUrl.setter
    def ecoreUrl(self, ecoreUrl: str):
        self.__ecoreUrl = ecoreUrl


    @property
    def generatedPackageName(self):
        return self.__generatedPackageName

    @generatedPackageName.setter
    def generatedPackageName(self, generatedPackageName: str):
        self.__generatedPackageName = generatedPackageName


    @property
    def schema_StorySchemaCatalog4(self):
        return self.__schema_StorySchemaCatalog4

    @schema_StorySchemaCatalog4.setter
    def schema_StorySchemaCatalog4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schema_StorySchemaCatalog__schema_StorySchemaCatalog4", None)
        self.__schema_StorySchemaCatalog4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schema_AggregationType"):
                    opp_val = getattr(item, "schema_AggregationType", None)
                    
                    if opp_val == self:
                        setattr(item, "schema_AggregationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schema_AggregationType"):
                    opp_val = getattr(item, "schema_AggregationType", None)
                    
                    setattr(item, "schema_AggregationType", self)
                    

    @property
    def schema_StorySchemaCatalog8(self):
        return self.__schema_StorySchemaCatalog8

    @schema_StorySchemaCatalog8.setter
    def schema_StorySchemaCatalog8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schema_StorySchemaCatalog__schema_StorySchemaCatalog8", None)
        self.__schema_StorySchemaCatalog8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema_EFactory"):
                opp_val = getattr(old_value, "schema_EFactory", None)
                if opp_val == self:
                    setattr(old_value, "schema_EFactory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema_EFactory"):
                opp_val = getattr(value, "schema_EFactory", None)
                setattr(value, "schema_EFactory", self)

    @property
    def schema_StorySchemaCatalog(self):
        return self.__schema_StorySchemaCatalog

    @schema_StorySchemaCatalog.setter
    def schema_StorySchemaCatalog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schema_StorySchemaCatalog__schema_StorySchemaCatalog", None)
        self.__schema_StorySchemaCatalog = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schema_StoryType"):
                    opp_val = getattr(item, "schema_StoryType", None)
                    
                    if opp_val == self:
                        setattr(item, "schema_StoryType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schema_StoryType"):
                    opp_val = getattr(item, "schema_StoryType", None)
                    
                    setattr(item, "schema_StoryType", self)
                    

    @property
    def schema_StorySchemaCatalog6(self):
        return self.__schema_StorySchemaCatalog6

    @schema_StorySchemaCatalog6.setter
    def schema_StorySchemaCatalog6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schema_StorySchemaCatalog__schema_StorySchemaCatalog6", None)
        self.__schema_StorySchemaCatalog6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema_EPackage"):
                opp_val = getattr(old_value, "schema_EPackage", None)
                if opp_val == self:
                    setattr(old_value, "schema_EPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema_EPackage"):
                opp_val = getattr(value, "schema_EPackage", None)
                setattr(value, "schema_EPackage", self)

    @property
    def schema_StorySchemaCatalog2(self):
        return self.__schema_StorySchemaCatalog2

    @schema_StorySchemaCatalog2.setter
    def schema_StorySchemaCatalog2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schema_StorySchemaCatalog__schema_StorySchemaCatalog2", None)
        self.__schema_StorySchemaCatalog2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schema_ActionType"):
                    opp_val = getattr(item, "schema_ActionType", None)
                    
                    if opp_val == self:
                        setattr(item, "schema_ActionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schema_ActionType"):
                    opp_val = getattr(item, "schema_ActionType", None)
                    
                    setattr(item, "schema_ActionType", self)
                    

    def createAction(self, schema_targetClass):
        # TODO: Implement createAction method
        pass
