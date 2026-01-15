from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class HyGroupTypeEnum(Enum):
    AND = "AND"
    OR = "OR"
    ALTERNATIVE = "ALTERNATIVE"
class HyFeatureTypeEnum(Enum):
    OPTIONAL = "OPTIONAL"
    MANDATORY = "MANDATORY"


############################################
# Definition of Classes
############################################

class HyLinearTemporalElement:

    pass
class feature_HyEnumLiteral:

    pass
class HyFeatureAttribute:

    pass
class feature_HyEnumAttribute(HyFeatureAttribute):

    pass
class feature_HyBooleanAttribute(HyFeatureAttribute):

    def __init__(self, default: bool):
        self.default = default
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

class feature_HyStringAttribute(HyFeatureAttribute):

    def __init__(self, default: str):
        self.default = default
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

class feature_HyNumberAttribute(HyFeatureAttribute):

    def __init__(self, min: int, max: int, default: int):
        self.min = min
        self.max = max
        self.default = default
        
    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def default(self) -> int:
        return self.__default

    @default.setter
    def default(self, default: int):
        self.__default = default

class feature_HyFeatureType(HyLinearTemporalElement):

    def __init__(self, type: str, feature_HyFeatureType: "feature_HyFeature" = None):
        self.type = type
        self.feature_HyFeatureType = feature_HyFeatureType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def feature_HyFeatureType(self):
        return self.__feature_HyFeatureType

    @feature_HyFeatureType.setter
    def feature_HyFeatureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeatureType__feature_HyFeatureType", None)
        self.__feature_HyFeatureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_HyFeature"):
                opp_val = getattr(old_value, "feature_HyFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_HyFeature"):
                opp_val = getattr(value, "feature_HyFeature", None)
                if opp_val is None:
                    setattr(value, "feature_HyFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class feature_HyGroupType(HyLinearTemporalElement):

    def __init__(self, type: str, feature_HyGroupType: "feature_HyGroup" = None):
        self.type = type
        self.feature_HyGroupType = feature_HyGroupType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def feature_HyGroupType(self):
        return self.__feature_HyGroupType

    @feature_HyGroupType.setter
    def feature_HyGroupType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyGroupType__feature_HyGroupType", None)
        self.__feature_HyGroupType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_HyGroup"):
                opp_val = getattr(old_value, "feature_HyGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_HyGroup"):
                opp_val = getattr(value, "feature_HyGroup", None)
                if opp_val is None:
                    setattr(value, "feature_HyGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class feature_HyFeatureChild(HyLinearTemporalElement):

    pass
class feature_HyGroupComposition(HyLinearTemporalElement):

    pass
class HyNamedElement:

    pass
class HyTemporalElement:

    pass
class feature_HyGroup(HyTemporalElement):

    def __init__(self, HyGroup: "feature_HyFeatureModel" = None, compositionOf: set["feature_HyGroupComposition"] = None, childGroup: set["feature_HyFeatureChild"] = None, feature_HyGroup: set["feature_HyGroupType"] = None, groups: "feature_HyFeatureModel" = None, HyGroup41: "feature_HyGroupComposition" = None, HyGroup48: "feature_HyFeatureChild" = None):
        self.HyGroup = HyGroup
        self.compositionOf = compositionOf if compositionOf is not None else set()
        self.childGroup = childGroup if childGroup is not None else set()
        self.feature_HyGroup = feature_HyGroup if feature_HyGroup is not None else set()
        self.groups = groups
        self.HyGroup41 = HyGroup41
        self.HyGroup48 = HyGroup48
        
    @property
    def HyGroup(self):
        return self.__HyGroup

    @HyGroup.setter
    def HyGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyGroup__HyGroup", None)
        self.__HyGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel3"):
                opp_val = getattr(old_value, "featureModel3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel3"):
                opp_val = getattr(value, "featureModel3", None)
                if opp_val is None:
                    setattr(value, "featureModel3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def feature_HyGroup(self):
        return self.__feature_HyGroup

    @feature_HyGroup.setter
    def feature_HyGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyGroup__feature_HyGroup", None)
        self.__feature_HyGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "feature_HyGroupType"):
                    opp_val = getattr(item, "feature_HyGroupType", None)
                    
                    if opp_val == self:
                        setattr(item, "feature_HyGroupType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "feature_HyGroupType"):
                    opp_val = getattr(item, "feature_HyGroupType", None)
                    
                    setattr(item, "feature_HyGroupType", self)
                    

    @property
    def compositionOf(self):
        return self.__compositionOf

    @compositionOf.setter
    def compositionOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyGroup__compositionOf", None)
        self.__compositionOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HyGroupComposition17"):
                    opp_val = getattr(item, "HyGroupComposition17", None)
                    
                    if opp_val == self:
                        setattr(item, "HyGroupComposition17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HyGroupComposition17"):
                    opp_val = getattr(item, "HyGroupComposition17", None)
                    
                    setattr(item, "HyGroupComposition17", self)
                    

    @property
    def childGroup(self):
        return self.__childGroup

    @childGroup.setter
    def childGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyGroup__childGroup", None)
        self.__childGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HyFeatureChild19"):
                    opp_val = getattr(item, "HyFeatureChild19", None)
                    
                    if opp_val == self:
                        setattr(item, "HyFeatureChild19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HyFeatureChild19"):
                    opp_val = getattr(item, "HyFeatureChild19", None)
                    
                    setattr(item, "HyFeatureChild19", self)
                    

    @property
    def groups(self):
        return self.__groups

    @groups.setter
    def groups(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyGroup__groups", None)
        self.__groups = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HyFeatureModel22"):
                opp_val = getattr(old_value, "HyFeatureModel22", None)
                if opp_val == self:
                    setattr(old_value, "HyFeatureModel22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HyFeatureModel22"):
                opp_val = getattr(value, "HyFeatureModel22", None)
                setattr(value, "HyFeatureModel22", self)

    @property
    def HyGroup41(self):
        return self.__HyGroup41

    @HyGroup41.setter
    def HyGroup41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyGroup__HyGroup41", None)
        self.__HyGroup41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentOf"):
                opp_val = getattr(old_value, "parentOf", None)
                if opp_val == self:
                    setattr(old_value, "parentOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentOf"):
                opp_val = getattr(value, "parentOf", None)
                setattr(value, "parentOf", self)

    @property
    def HyGroup48(self):
        return self.__HyGroup48

    @HyGroup48.setter
    def HyGroup48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyGroup__HyGroup48", None)
        self.__HyGroup48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childOf"):
                opp_val = getattr(old_value, "childOf", None)
                if opp_val == self:
                    setattr(old_value, "childOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childOf"):
                opp_val = getattr(value, "childOf", None)
                setattr(value, "childOf", self)

    def isOr(self, date: date) -> bool:
        # TODO: Implement isOr method
        pass

    def isAlternative(self, date: date) -> bool:
        # TODO: Implement isAlternative method
        pass

    def isAnd(self, date: date) -> bool:
        # TODO: Implement isAnd method
        pass

class feature_HyVersion(HyTemporalElement):

    def __init__(self, number: str, HyVersion: "feature_HyFeature" = None, HyVersion27: "feature_HyVersion" = None, supersededVersion: set["feature_HyVersion"] = None, HyVersion30: "feature_HyVersion" = None, supersedingVersions: "feature_HyVersion" = None, versions: "feature_HyFeature" = None):
        self.number = number
        self.HyVersion = HyVersion
        self.HyVersion27 = HyVersion27
        self.supersededVersion = supersededVersion if supersededVersion is not None else set()
        self.HyVersion30 = HyVersion30
        self.supersedingVersions = supersedingVersions
        self.versions = versions
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def HyVersion27(self):
        return self.__HyVersion27

    @HyVersion27.setter
    def HyVersion27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyVersion__HyVersion27", None)
        self.__HyVersion27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supersededVersion"):
                opp_val = getattr(old_value, "supersededVersion", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supersededVersion"):
                opp_val = getattr(value, "supersededVersion", None)
                if opp_val is None:
                    setattr(value, "supersededVersion", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def versions(self):
        return self.__versions

    @versions.setter
    def versions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyVersion__versions", None)
        self.__versions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HyFeature24"):
                opp_val = getattr(old_value, "HyFeature24", None)
                if opp_val == self:
                    setattr(old_value, "HyFeature24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HyFeature24"):
                opp_val = getattr(value, "HyFeature24", None)
                setattr(value, "HyFeature24", self)

    @property
    def supersedingVersions(self):
        return self.__supersedingVersions

    @supersedingVersions.setter
    def supersedingVersions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyVersion__supersedingVersions", None)
        self.__supersedingVersions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HyVersion30"):
                opp_val = getattr(old_value, "HyVersion30", None)
                if opp_val == self:
                    setattr(old_value, "HyVersion30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HyVersion30"):
                opp_val = getattr(value, "HyVersion30", None)
                setattr(value, "HyVersion30", self)

    @property
    def supersededVersion(self):
        return self.__supersededVersion

    @supersededVersion.setter
    def supersededVersion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyVersion__supersededVersion", None)
        self.__supersededVersion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HyVersion27"):
                    opp_val = getattr(item, "HyVersion27", None)
                    
                    if opp_val == self:
                        setattr(item, "HyVersion27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HyVersion27"):
                    opp_val = getattr(item, "HyVersion27", None)
                    
                    setattr(item, "HyVersion27", self)
                    

    @property
    def HyVersion30(self):
        return self.__HyVersion30

    @HyVersion30.setter
    def HyVersion30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyVersion__HyVersion30", None)
        self.__HyVersion30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supersedingVersions"):
                opp_val = getattr(old_value, "supersedingVersions", None)
                if opp_val == self:
                    setattr(old_value, "supersedingVersions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supersedingVersions"):
                opp_val = getattr(value, "supersedingVersions", None)
                setattr(value, "supersedingVersions", self)

    @property
    def HyVersion(self):
        return self.__HyVersion

    @HyVersion.setter
    def HyVersion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyVersion__HyVersion", None)
        self.__HyVersion = value
        
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

class feature_HyFeatureAttribute(HyTemporalElement, HyNamedElement):

    pass
class feature_HyContextModel:

    pass
class feature_HyEnum:

    pass
class feature_HyFeature(HyTemporalElement, HyNamedElement):

    def __init__(self, deprecatedSince: date, HyFeature: "feature_HyFeatureModel" = None, feature: set["feature_HyVersion"] = None, features: set["feature_HyGroupComposition"] = None, parent: set["feature_HyFeatureChild"] = None, feature12: set["feature_HyFeatureAttribute"] = None, feature_HyFeature: set["feature_HyFeatureType"] = None, features15: "feature_HyFeatureModel" = None, HyFeature24: "feature_HyVersion" = None, feature_HyFeature39: "feature_HyRootFeature" = None, HyFeature43: "feature_HyGroupComposition" = None, HyFeature46: "feature_HyFeatureChild" = None, HyFeature36: "feature_HyFeatureAttribute" = None):
        self.deprecatedSince = deprecatedSince
        self.HyFeature = HyFeature
        self.feature = feature if feature is not None else set()
        self.features = features if features is not None else set()
        self.parent = parent if parent is not None else set()
        self.feature12 = feature12 if feature12 is not None else set()
        self.feature_HyFeature = feature_HyFeature if feature_HyFeature is not None else set()
        self.features15 = features15
        self.HyFeature24 = HyFeature24
        self.feature_HyFeature39 = feature_HyFeature39
        self.HyFeature43 = HyFeature43
        self.HyFeature46 = HyFeature46
        self.HyFeature36 = HyFeature36
        
    @property
    def deprecatedSince(self) -> date:
        return self.__deprecatedSince

    @deprecatedSince.setter
    def deprecatedSince(self, deprecatedSince: date):
        self.__deprecatedSince = deprecatedSince

    @property
    def HyFeature24(self):
        return self.__HyFeature24

    @HyFeature24.setter
    def HyFeature24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__HyFeature24", None)
        self.__HyFeature24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "versions"):
                opp_val = getattr(old_value, "versions", None)
                if opp_val == self:
                    setattr(old_value, "versions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "versions"):
                opp_val = getattr(value, "versions", None)
                setattr(value, "versions", self)

    @property
    def HyFeature36(self):
        return self.__HyFeature36

    @HyFeature36.setter
    def HyFeature36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__HyFeature36", None)
        self.__HyFeature36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes"):
                opp_val = getattr(old_value, "attributes", None)
                if opp_val == self:
                    setattr(old_value, "attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes"):
                opp_val = getattr(value, "attributes", None)
                setattr(value, "attributes", self)

    @property
    def features15(self):
        return self.__features15

    @features15.setter
    def features15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__features15", None)
        self.__features15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HyFeatureModel"):
                opp_val = getattr(old_value, "HyFeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "HyFeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HyFeatureModel"):
                opp_val = getattr(value, "HyFeatureModel", None)
                setattr(value, "HyFeatureModel", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HyFeatureChild"):
                    opp_val = getattr(item, "HyFeatureChild", None)
                    
                    if opp_val == self:
                        setattr(item, "HyFeatureChild", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HyFeatureChild"):
                    opp_val = getattr(item, "HyFeatureChild", None)
                    
                    setattr(item, "HyFeatureChild", self)
                    

    @property
    def feature12(self):
        return self.__feature12

    @feature12.setter
    def feature12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__feature12", None)
        self.__feature12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HyFeatureAttribute"):
                    opp_val = getattr(item, "HyFeatureAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "HyFeatureAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HyFeatureAttribute"):
                    opp_val = getattr(item, "HyFeatureAttribute", None)
                    
                    setattr(item, "HyFeatureAttribute", self)
                    

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__features", None)
        self.__features = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HyGroupComposition"):
                    opp_val = getattr(item, "HyGroupComposition", None)
                    
                    if opp_val == self:
                        setattr(item, "HyGroupComposition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HyGroupComposition"):
                    opp_val = getattr(item, "HyGroupComposition", None)
                    
                    setattr(item, "HyGroupComposition", self)
                    

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HyVersion"):
                    opp_val = getattr(item, "HyVersion", None)
                    
                    if opp_val == self:
                        setattr(item, "HyVersion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HyVersion"):
                    opp_val = getattr(item, "HyVersion", None)
                    
                    setattr(item, "HyVersion", self)
                    

    @property
    def HyFeature(self):
        return self.__HyFeature

    @HyFeature.setter
    def HyFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__HyFeature", None)
        self.__HyFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel"):
                opp_val = getattr(old_value, "featureModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel"):
                opp_val = getattr(value, "featureModel", None)
                if opp_val is None:
                    setattr(value, "featureModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def feature_HyFeature(self):
        return self.__feature_HyFeature

    @feature_HyFeature.setter
    def feature_HyFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__feature_HyFeature", None)
        self.__feature_HyFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "feature_HyFeatureType"):
                    opp_val = getattr(item, "feature_HyFeatureType", None)
                    
                    if opp_val == self:
                        setattr(item, "feature_HyFeatureType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "feature_HyFeatureType"):
                    opp_val = getattr(item, "feature_HyFeatureType", None)
                    
                    setattr(item, "feature_HyFeatureType", self)
                    

    @property
    def feature_HyFeature39(self):
        return self.__feature_HyFeature39

    @feature_HyFeature39.setter
    def feature_HyFeature39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__feature_HyFeature39", None)
        self.__feature_HyFeature39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_HyRootFeature38"):
                opp_val = getattr(old_value, "feature_HyRootFeature38", None)
                if opp_val == self:
                    setattr(old_value, "feature_HyRootFeature38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_HyRootFeature38"):
                opp_val = getattr(value, "feature_HyRootFeature38", None)
                setattr(value, "feature_HyRootFeature38", self)

    @property
    def HyFeature46(self):
        return self.__HyFeature46

    @HyFeature46.setter
    def HyFeature46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__HyFeature46", None)
        self.__HyFeature46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentOf45"):
                opp_val = getattr(old_value, "parentOf45", None)
                if opp_val == self:
                    setattr(old_value, "parentOf45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentOf45"):
                opp_val = getattr(value, "parentOf45", None)
                setattr(value, "parentOf45", self)

    @property
    def HyFeature43(self):
        return self.__HyFeature43

    @HyFeature43.setter
    def HyFeature43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_HyFeature__HyFeature43", None)
        self.__HyFeature43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groupMembership"):
                opp_val = getattr(old_value, "groupMembership", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groupMembership"):
                opp_val = getattr(value, "groupMembership", None)
                if opp_val is None:
                    setattr(value, "groupMembership", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isMandatory(self, date: date) -> bool:
        # TODO: Implement isMandatory method
        pass

    def isOptional(self, date: date) -> bool:
        # TODO: Implement isOptional method
        pass

class feature_HyRootFeature(HyLinearTemporalElement):

    pass
class feature_HyFeatureModel:

    pass