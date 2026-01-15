from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FeatureVersionDescriptor:

    pass
class features_FeatureVersion(FeatureVersionDescriptor):

    def __init__(self, version: str, news: str, featureVersions: "features_Feature" = None, FeatureVersion: "features_Feature" = None):
        self.version = version
        self.news = news
        self.featureVersions = featureVersions
        self.FeatureVersion = FeatureVersion
        
    @property
    def news(self) -> str:
        return self.__news

    @news.setter
    def news(self, news: str):
        self.__news = news

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def FeatureVersion(self):
        return self.__FeatureVersion

    @FeatureVersion.setter
    def FeatureVersion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_FeatureVersion__FeatureVersion", None)
        self.__FeatureVersion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature"):
                opp_val = getattr(old_value, "feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature"):
                opp_val = getattr(value, "feature", None)
                if opp_val is None:
                    setattr(value, "feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureVersions(self):
        return self.__featureVersions

    @featureVersions.setter
    def featureVersions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_FeatureVersion__featureVersions", None)
        self.__featureVersions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature4"):
                opp_val = getattr(old_value, "Feature4", None)
                if opp_val == self:
                    setattr(old_value, "Feature4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature4"):
                opp_val = getattr(value, "Feature4", None)
                setattr(value, "Feature4", self)

class FeatureDescriptor:

    pass
class features_Feature(FeatureDescriptor):

    def __init__(self, identifier: str, provider: str, name: str, description: str, Feature4: "features_FeatureVersion" = None, Feature: "features_FeatureSet" = None, features: "features_FeatureSet" = None, feature: set["features_FeatureVersion"] = None):
        self.identifier = identifier
        self.provider = provider
        self.name = name
        self.description = description
        self.Feature4 = Feature4
        self.Feature = Feature
        self.features = features
        self.feature = feature if feature is not None else set()
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def provider(self) -> str:
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureSet"):
                opp_val = getattr(old_value, "FeatureSet", None)
                if opp_val == self:
                    setattr(old_value, "FeatureSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureSet"):
                opp_val = getattr(value, "FeatureSet", None)
                setattr(value, "FeatureSet", self)

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureSet"):
                opp_val = getattr(old_value, "featureSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureSet"):
                opp_val = getattr(value, "featureSet", None)
                if opp_val is None:
                    setattr(value, "featureSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Feature4(self):
        return self.__Feature4

    @Feature4.setter
    def Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__Feature4", None)
        self.__Feature4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureVersions"):
                opp_val = getattr(old_value, "featureVersions", None)
                if opp_val == self:
                    setattr(old_value, "featureVersions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureVersions"):
                opp_val = getattr(value, "featureVersions", None)
                setattr(value, "featureVersions", self)

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureVersion"):
                    opp_val = getattr(item, "FeatureVersion", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureVersion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureVersion"):
                    opp_val = getattr(item, "FeatureVersion", None)
                    
                    setattr(item, "FeatureVersion", self)
                    

class features_FeatureVersionDescriptor(ABC):

    pass
class features_FeatureDescriptor(ABC):

    pass
class features_FeatureSetDescriptor(ABC):

    pass
class FeatureSetDescriptor:

    pass
class features_FeatureSet(FeatureSetDescriptor):

    def __init__(self, identifier: str, name: str, description: str, featureSet: set["features_Feature"] = None, FeatureSet: "features_Feature" = None):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.featureSet = featureSet if featureSet is not None else set()
        self.FeatureSet = FeatureSet
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featureSet(self):
        return self.__featureSet

    @featureSet.setter
    def featureSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_FeatureSet__featureSet", None)
        self.__featureSet = value if value is not None else set()
        
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
    def FeatureSet(self):
        return self.__FeatureSet

    @FeatureSet.setter
    def FeatureSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_FeatureSet__FeatureSet", None)
        self.__FeatureSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features"):
                opp_val = getattr(old_value, "features", None)
                if opp_val == self:
                    setattr(old_value, "features", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features"):
                opp_val = getattr(value, "features", None)
                setattr(value, "features", self)
