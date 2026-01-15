from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GroupType(Enum):
    OR = "OR"
    ALT = "ALT"


############################################
# Definition of Classes
############################################

class Constraint:

    pass
class FeatureModel_ExcludeConstraint(Constraint):

    pass
class FeatureModel_RequireConstraint(Constraint):

    pass
class NamedElement:

    pass
class FeatureModel_Comment(NamedElement):

    def __init__(self, text: str, FeatureModel_Comment8: "FeatureModel_NamedElement" = None, FeatureModel_Comment: "FeatureModel_FeatureModel" = None):
        self.text = text
        self.FeatureModel_Comment8 = FeatureModel_Comment8
        self.FeatureModel_Comment = FeatureModel_Comment
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def FeatureModel_Comment(self):
        return self.__FeatureModel_Comment

    @FeatureModel_Comment.setter
    def FeatureModel_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Comment__FeatureModel_Comment", None)
        self.__FeatureModel_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel_FeatureModel"):
                opp_val = getattr(old_value, "FeatureModel_FeatureModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel_FeatureModel"):
                opp_val = getattr(value, "FeatureModel_FeatureModel", None)
                if opp_val is None:
                    setattr(value, "FeatureModel_FeatureModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FeatureModel_Comment8(self):
        return self.__FeatureModel_Comment8

    @FeatureModel_Comment8.setter
    def FeatureModel_Comment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Comment__FeatureModel_Comment8", None)
        self.__FeatureModel_Comment8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel_NamedElement"):
                opp_val = getattr(old_value, "FeatureModel_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel_NamedElement"):
                opp_val = getattr(value, "FeatureModel_NamedElement", None)
                setattr(value, "FeatureModel_NamedElement", self)

class FeatureModel_Constraint(NamedElement):

    def __init__(self, language: str, code: str, FeatureModel_Constraint: "FeatureModel_FeatureModel" = None):
        self.language = language
        self.code = code
        self.FeatureModel_Constraint = FeatureModel_Constraint
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def FeatureModel_Constraint(self):
        return self.__FeatureModel_Constraint

    @FeatureModel_Constraint.setter
    def FeatureModel_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Constraint__FeatureModel_Constraint", None)
        self.__FeatureModel_Constraint = value
        
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

class FeatureModel_Feature(NamedElement):

    def __init__(self, abstract: bool, mandatory: bool, FeatureModel_Feature: "FeatureModel_FeatureModel" = None, FeatureModel_Feature11: "FeatureModel_Feature" = None, FeatureModel_Feature9: set["FeatureModel_Feature"] = None, requiredFeature: set["FeatureModel_RequireConstraint"] = None, feature: set["FeatureModel_RequireConstraint"] = None, features: "FeatureModel_Group" = None, Feature21: "FeatureModel_RequireConstraint" = None, Feature23: "FeatureModel_ExcludeConstraint" = None, Feature25: "FeatureModel_ExcludeConstraint" = None, Feature27: "FeatureModel_Group" = None, excludedFeatureA: set["FeatureModel_ExcludeConstraint"] = None, excludedFeatureB: set["FeatureModel_ExcludeConstraint"] = None, Feature: "FeatureModel_RequireConstraint" = None):
        self.abstract = abstract
        self.mandatory = mandatory
        self.FeatureModel_Feature = FeatureModel_Feature
        self.FeatureModel_Feature11 = FeatureModel_Feature11
        self.FeatureModel_Feature9 = FeatureModel_Feature9 if FeatureModel_Feature9 is not None else set()
        self.requiredFeature = requiredFeature if requiredFeature is not None else set()
        self.feature = feature if feature is not None else set()
        self.features = features
        self.Feature21 = Feature21
        self.Feature23 = Feature23
        self.Feature25 = Feature25
        self.Feature27 = Feature27
        self.excludedFeatureA = excludedFeatureA if excludedFeatureA is not None else set()
        self.excludedFeatureB = excludedFeatureB if excludedFeatureB is not None else set()
        self.Feature = Feature
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequireConstraint14"):
                    opp_val = getattr(item, "RequireConstraint14", None)
                    
                    if opp_val == self:
                        setattr(item, "RequireConstraint14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequireConstraint14"):
                    opp_val = getattr(item, "RequireConstraint14", None)
                    
                    setattr(item, "RequireConstraint14", self)
                    

    @property
    def Feature25(self):
        return self.__Feature25

    @Feature25.setter
    def Feature25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__Feature25", None)
        self.__Feature25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "excludeConstraintsB"):
                opp_val = getattr(old_value, "excludeConstraintsB", None)
                if opp_val == self:
                    setattr(old_value, "excludeConstraintsB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "excludeConstraintsB"):
                opp_val = getattr(value, "excludeConstraintsB", None)
                setattr(value, "excludeConstraintsB", self)

    @property
    def Feature27(self):
        return self.__Feature27

    @Feature27.setter
    def Feature27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__Feature27", None)
        self.__Feature27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group"):
                opp_val = getattr(old_value, "group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group"):
                opp_val = getattr(value, "group", None)
                if opp_val is None:
                    setattr(value, "group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "FeatureModel_FeatureModel4"):
                opp_val = getattr(old_value, "FeatureModel_FeatureModel4", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel_FeatureModel4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel_FeatureModel4"):
                opp_val = getattr(value, "FeatureModel_FeatureModel4", None)
                setattr(value, "FeatureModel_FeatureModel4", self)

    @property
    def FeatureModel_Feature9(self):
        return self.__FeatureModel_Feature9

    @FeatureModel_Feature9.setter
    def FeatureModel_Feature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__FeatureModel_Feature9", None)
        self.__FeatureModel_Feature9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureModel_Feature11"):
                    opp_val = getattr(item, "FeatureModel_Feature11", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureModel_Feature11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureModel_Feature11"):
                    opp_val = getattr(item, "FeatureModel_Feature11", None)
                    
                    setattr(item, "FeatureModel_Feature11", self)
                    

    @property
    def FeatureModel_Feature11(self):
        return self.__FeatureModel_Feature11

    @FeatureModel_Feature11.setter
    def FeatureModel_Feature11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__FeatureModel_Feature11", None)
        self.__FeatureModel_Feature11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel_Feature9"):
                opp_val = getattr(old_value, "FeatureModel_Feature9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel_Feature9"):
                opp_val = getattr(value, "FeatureModel_Feature9", None)
                if opp_val is None:
                    setattr(value, "FeatureModel_Feature9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Feature21(self):
        return self.__Feature21

    @Feature21.setter
    def Feature21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__Feature21", None)
        self.__Feature21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requireConstraints"):
                opp_val = getattr(old_value, "requireConstraints", None)
                if opp_val == self:
                    setattr(old_value, "requireConstraints", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requireConstraints"):
                opp_val = getattr(value, "requireConstraints", None)
                setattr(value, "requireConstraints", self)

    @property
    def excludedFeatureA(self):
        return self.__excludedFeatureA

    @excludedFeatureA.setter
    def excludedFeatureA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__excludedFeatureA", None)
        self.__excludedFeatureA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExcludeConstraint"):
                    opp_val = getattr(item, "ExcludeConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "ExcludeConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExcludeConstraint"):
                    opp_val = getattr(item, "ExcludeConstraint", None)
                    
                    setattr(item, "ExcludeConstraint", self)
                    

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Group"):
                opp_val = getattr(old_value, "Group", None)
                if opp_val == self:
                    setattr(old_value, "Group", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Group"):
                opp_val = getattr(value, "Group", None)
                setattr(value, "Group", self)

    @property
    def excludedFeatureB(self):
        return self.__excludedFeatureB

    @excludedFeatureB.setter
    def excludedFeatureB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__excludedFeatureB", None)
        self.__excludedFeatureB = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExcludeConstraint18"):
                    opp_val = getattr(item, "ExcludeConstraint18", None)
                    
                    if opp_val == self:
                        setattr(item, "ExcludeConstraint18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExcludeConstraint18"):
                    opp_val = getattr(item, "ExcludeConstraint18", None)
                    
                    setattr(item, "ExcludeConstraint18", self)
                    

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
            if hasattr(old_value, "requiredConstraints"):
                opp_val = getattr(old_value, "requiredConstraints", None)
                if opp_val == self:
                    setattr(old_value, "requiredConstraints", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requiredConstraints"):
                opp_val = getattr(value, "requiredConstraints", None)
                setattr(value, "requiredConstraints", self)

    @property
    def requiredFeature(self):
        return self.__requiredFeature

    @requiredFeature.setter
    def requiredFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__requiredFeature", None)
        self.__requiredFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequireConstraint"):
                    opp_val = getattr(item, "RequireConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "RequireConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequireConstraint"):
                    opp_val = getattr(item, "RequireConstraint", None)
                    
                    setattr(item, "RequireConstraint", self)
                    

    @property
    def Feature23(self):
        return self.__Feature23

    @Feature23.setter
    def Feature23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Feature__Feature23", None)
        self.__Feature23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "excludeConstraintsA"):
                opp_val = getattr(old_value, "excludeConstraintsA", None)
                if opp_val == self:
                    setattr(old_value, "excludeConstraintsA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "excludeConstraintsA"):
                opp_val = getattr(value, "excludeConstraintsA", None)
                setattr(value, "excludeConstraintsA", self)

    def atMostInOneGroup(self, chain: str, context: str) -> bool:
        # TODO: Implement atMostInOneGroup method
        pass

class FeatureModel_NamedElement(ABC):

    def __init__(self, name: str, FeatureModel_NamedElement: "FeatureModel_Comment" = None):
        self.name = name
        self.FeatureModel_NamedElement = FeatureModel_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FeatureModel_NamedElement(self):
        return self.__FeatureModel_NamedElement

    @FeatureModel_NamedElement.setter
    def FeatureModel_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_NamedElement__FeatureModel_NamedElement", None)
        self.__FeatureModel_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel_Comment8"):
                opp_val = getattr(old_value, "FeatureModel_Comment8", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel_Comment8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel_Comment8"):
                opp_val = getattr(value, "FeatureModel_Comment8", None)
                setattr(value, "FeatureModel_Comment8", self)

class FeatureModel_Group(NamedElement):

    def __init__(self, groupType: str, FeatureModel_Group: "FeatureModel_FeatureModel" = None, Group: "FeatureModel_Feature" = None, group: set["FeatureModel_Feature"] = None):
        self.groupType = groupType
        self.FeatureModel_Group = FeatureModel_Group
        self.Group = Group
        self.group = group if group is not None else set()
        
    @property
    def groupType(self) -> str:
        return self.__groupType

    @groupType.setter
    def groupType(self, groupType: str):
        self.__groupType = groupType

    @property
    def FeatureModel_Group(self):
        return self.__FeatureModel_Group

    @FeatureModel_Group.setter
    def FeatureModel_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Group__FeatureModel_Group", None)
        self.__FeatureModel_Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel_FeatureModel6"):
                opp_val = getattr(old_value, "FeatureModel_FeatureModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel_FeatureModel6"):
                opp_val = getattr(value, "FeatureModel_FeatureModel6", None)
                if opp_val is None:
                    setattr(value, "FeatureModel_FeatureModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Group__group", None)
        self.__group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature27"):
                    opp_val = getattr(item, "Feature27", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature27"):
                    opp_val = getattr(item, "Feature27", None)
                    
                    setattr(item, "Feature27", self)
                    

    @property
    def Group(self):
        return self.__Group

    @Group.setter
    def Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_Group__Group", None)
        self.__Group = value
        
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

class FeatureModel_FeatureModel(NamedElement):

    def __init__(self, version: float, FeatureModel_FeatureModel6: set["FeatureModel_Group"] = None, FeatureModel_FeatureModel: set["FeatureModel_Comment"] = None, FeatureModel_FeatureModel2: set["FeatureModel_Constraint"] = None, FeatureModel_FeatureModel4: "FeatureModel_Feature" = None):
        self.version = version
        self.FeatureModel_FeatureModel6 = FeatureModel_FeatureModel6 if FeatureModel_FeatureModel6 is not None else set()
        self.FeatureModel_FeatureModel = FeatureModel_FeatureModel if FeatureModel_FeatureModel is not None else set()
        self.FeatureModel_FeatureModel2 = FeatureModel_FeatureModel2 if FeatureModel_FeatureModel2 is not None else set()
        self.FeatureModel_FeatureModel4 = FeatureModel_FeatureModel4
        
    @property
    def version(self) -> float:
        return self.__version

    @version.setter
    def version(self, version: float):
        self.__version = version

    @property
    def FeatureModel_FeatureModel6(self):
        return self.__FeatureModel_FeatureModel6

    @FeatureModel_FeatureModel6.setter
    def FeatureModel_FeatureModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_FeatureModel__FeatureModel_FeatureModel6", None)
        self.__FeatureModel_FeatureModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureModel_Group"):
                    opp_val = getattr(item, "FeatureModel_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureModel_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureModel_Group"):
                    opp_val = getattr(item, "FeatureModel_Group", None)
                    
                    setattr(item, "FeatureModel_Group", self)
                    

    @property
    def FeatureModel_FeatureModel4(self):
        return self.__FeatureModel_FeatureModel4

    @FeatureModel_FeatureModel4.setter
    def FeatureModel_FeatureModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_FeatureModel__FeatureModel_FeatureModel4", None)
        self.__FeatureModel_FeatureModel4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel_Feature"):
                opp_val = getattr(old_value, "FeatureModel_Feature", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel_Feature"):
                opp_val = getattr(value, "FeatureModel_Feature", None)
                setattr(value, "FeatureModel_Feature", self)

    @property
    def FeatureModel_FeatureModel2(self):
        return self.__FeatureModel_FeatureModel2

    @FeatureModel_FeatureModel2.setter
    def FeatureModel_FeatureModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_FeatureModel__FeatureModel_FeatureModel2", None)
        self.__FeatureModel_FeatureModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureModel_Constraint"):
                    opp_val = getattr(item, "FeatureModel_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureModel_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureModel_Constraint"):
                    opp_val = getattr(item, "FeatureModel_Constraint", None)
                    
                    setattr(item, "FeatureModel_Constraint", self)
                    

    @property
    def FeatureModel_FeatureModel(self):
        return self.__FeatureModel_FeatureModel

    @FeatureModel_FeatureModel.setter
    def FeatureModel_FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FeatureModel_FeatureModel__FeatureModel_FeatureModel", None)
        self.__FeatureModel_FeatureModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureModel_Comment"):
                    opp_val = getattr(item, "FeatureModel_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureModel_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureModel_Comment"):
                    opp_val = getattr(item, "FeatureModel_Comment", None)
                    
                    setattr(item, "FeatureModel_Comment", self)
                    
