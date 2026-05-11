from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class feature_Model:

    def __init__(self, features: str):
        self.features = features
        
        pass
    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, features: str):
        self.__features = features


class feature_Feature:

    def __init__(self, name: str, attribute: str, max: int, min: int, isSelected: bool, feature_Feature: "feature_Feature" = None, feature_Feature0: set["feature_Feature"] = None):
        self.name = name
        self.attribute = attribute
        self.max = max
        self.min = min
        self.isSelected = isSelected
        self.feature_Feature = feature_Feature
        self.feature_Feature0 = feature_Feature0 if feature_Feature0 is not None else set()
        
        pass
    @property
    def isSelected(self):
        return self.__isSelected

    @isSelected.setter
    def isSelected(self, isSelected: bool):
        self.__isSelected = isSelected


    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min


    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max


    @property
    def feature_Feature(self):
        return self.__feature_Feature

    @feature_Feature.setter
    def feature_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature", None)
        self.__feature_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_Feature0"):
                opp_val = getattr(old_value, "feature_Feature0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_Feature0"):
                opp_val = getattr(value, "feature_Feature0", None)
                if opp_val is None:
                    setattr(value, "feature_Feature0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def feature_Feature0(self):
        return self.__feature_Feature0

    @feature_Feature0.setter
    def feature_Feature0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature0", None)
        self.__feature_Feature0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "feature_Feature"):
                    opp_val = getattr(item, "feature_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "feature_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "feature_Feature"):
                    opp_val = getattr(item, "feature_Feature", None)
                    
                    setattr(item, "feature_Feature", self)
                    
