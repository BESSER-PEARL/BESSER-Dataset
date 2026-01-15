from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class kind(Enum):
    optional = "optional"
    mandatory = "mandatory"
class Type(Enum):
    require = "require"
    exclude = "exclude"


############################################
# Definition of Classes
############################################

class FeatureModel_Constraint(ABC):

    pass
class ConfigConstraint:

    pass
class FeatureModel_Or(ConfigConstraint):

    pass
class FeatureModel_Xor(ConfigConstraint):

    pass
class FeatureModel_And(ConfigConstraint):

    pass
class FeatureModel_Feature:

    def __init__(self, id: int, name: str, FeatureModel_Feature: "FeatureModel_FeatureConstraint" = None, ConfFeatures: "FeatureModel_ConfigConstraint" = None, Feature: "FeatureModel_ConfigConstraint" = None):
        self.id = id
        self.name = name
        self.FeatureModel_Feature = FeatureModel_Feature
        self.ConfFeatures = ConfFeatures
        self.Feature = Feature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def ConfFeatures(self):
        return self.__ConfFeatures

    @ConfFeatures.setter
    def ConfFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__ConfFeatures", None)
        self.__ConfFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfigConstraint"):
                opp_val = getattr(old_value, "ConfigConstraint", None)
                if opp_val == self:
                    setattr(old_value, "ConfigConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfigConstraint"):
                opp_val = getattr(value, "ConfigConstraint", None)
                setattr(value, "ConfigConstraint", self)

    @property
    def FeatureModel_Feature(self):
        return self.__FeatureModel_Feature

    @FeatureModel_Feature.setter
    def FeatureModel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__FeatureModel_Feature", None)
        self.__FeatureModel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel_FeatureConstraint6"):
                opp_val = getattr(old_value, "FeatureModel_FeatureConstraint6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel_FeatureConstraint6"):
                opp_val = getattr(value, "FeatureModel_FeatureConstraint6", None)
                if opp_val is None:
                    setattr(value, "FeatureModel_FeatureConstraint6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Config"):
                opp_val = getattr(old_value, "Config", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Config"):
                opp_val = getattr(value, "Config", None)
                if opp_val is None:
                    setattr(value, "Config", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Constraint:

    pass
class FeatureModel_ConfigConstraint(Constraint):

    def __init__(self, kind: str, FeatureModel_ConfigConstraint: "FeatureModel_RootFeature" = None, ConfigConstraint: "FeatureModel_Feature" = None, Config: set["FeatureModel_Feature"] = None):
        self.kind = kind
        self.FeatureModel_ConfigConstraint = FeatureModel_ConfigConstraint
        self.ConfigConstraint = ConfigConstraint
        self.Config = Config if Config is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ConfigConstraint(self):
        return self.__ConfigConstraint

    @ConfigConstraint.setter
    def ConfigConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_ConfigConstraint__ConfigConstraint", None)
        self.__ConfigConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfFeatures"):
                opp_val = getattr(old_value, "ConfFeatures", None)
                if opp_val == self:
                    setattr(old_value, "ConfFeatures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfFeatures"):
                opp_val = getattr(value, "ConfFeatures", None)
                setattr(value, "ConfFeatures", self)

    @property
    def Config(self):
        return self.__Config

    @Config.setter
    def Config(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_ConfigConstraint__Config", None)
        self.__Config = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def FeatureModel_ConfigConstraint(self):
        return self.__FeatureModel_ConfigConstraint

    @FeatureModel_ConfigConstraint.setter
    def FeatureModel_ConfigConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_ConfigConstraint__FeatureModel_ConfigConstraint", None)
        self.__FeatureModel_ConfigConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel_RootFeature4"):
                opp_val = getattr(old_value, "FeatureModel_RootFeature4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel_RootFeature4"):
                opp_val = getattr(value, "FeatureModel_RootFeature4", None)
                if opp_val is None:
                    setattr(value, "FeatureModel_RootFeature4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FeatureModel_FeatureConstraint(Constraint):

    def __init__(self, type: str, FeatureModel_FeatureConstraint: "FeatureModel_FeatureModel" = None, FeatureModel_FeatureConstraint6: set["FeatureModel_Feature"] = None):
        self.type = type
        self.FeatureModel_FeatureConstraint = FeatureModel_FeatureConstraint
        self.FeatureModel_FeatureConstraint6 = FeatureModel_FeatureConstraint6 if FeatureModel_FeatureConstraint6 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def FeatureModel_FeatureConstraint6(self):
        return self.__FeatureModel_FeatureConstraint6

    @FeatureModel_FeatureConstraint6.setter
    def FeatureModel_FeatureConstraint6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_FeatureConstraint__FeatureModel_FeatureConstraint6", None)
        self.__FeatureModel_FeatureConstraint6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureModel_Feature"):
                    opp_val = getattr(item, "FeatureModel_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureModel_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureModel_Feature"):
                    opp_val = getattr(item, "FeatureModel_Feature", None)
                    
                    setattr(item, "FeatureModel_Feature", self)
                    

    @property
    def FeatureModel_FeatureConstraint(self):
        return self.__FeatureModel_FeatureConstraint

    @FeatureModel_FeatureConstraint.setter
    def FeatureModel_FeatureConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_FeatureConstraint__FeatureModel_FeatureConstraint", None)
        self.__FeatureModel_FeatureConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel_FeatureModel2"):
                opp_val = getattr(old_value, "FeatureModel_FeatureModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel_FeatureModel2"):
                opp_val = getattr(value, "FeatureModel_FeatureModel2", None)
                if opp_val is None:
                    setattr(value, "FeatureModel_FeatureModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FeatureModel_RootFeature:

    pass
class FeatureModel_FeatureModel:

    pass