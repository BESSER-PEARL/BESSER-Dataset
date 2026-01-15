from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AttributeType(Enum):
    BOOLEAN = "BOOLEAN"
    INTEGER = "INTEGER"
    DOUBLE = "DOUBLE"
    STRING = "STRING"


############################################
# Definition of Classes
############################################

class fm_Group:

    def __init__(self, lower: int, upper: int, description: str, comment: str, xor: bool, or: bool, Group17: "fm_Feature" = None, Group: "fm_Feature" = None, groups: "fm_Feature" = None, parentGroup: set["fm_Feature"] = None):
        self.lower = lower
        self.upper = upper
        self.description = description
        self.comment = comment
        self.xor = xor
        self.or = or
        self.Group17 = Group17
        self.Group = Group
        self.groups = groups
        self.parentGroup = parentGroup if parentGroup is not None else set()
        
    @property
    def or(self) -> bool:
        return self.__or

    @or.setter
    def or(self, or: bool):
        self.__or = or

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def xor(self) -> bool:
        return self.__xor

    @xor.setter
    def xor(self, xor: bool):
        self.__xor = xor

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def parentGroup(self):
        return self.__parentGroup

    @parentGroup.setter
    def parentGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Group__parentGroup", None)
        self.__parentGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature24"):
                    opp_val = getattr(item, "Feature24", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature24"):
                    opp_val = getattr(item, "Feature24", None)
                    
                    setattr(item, "Feature24", self)
                    

    @property
    def Group17(self):
        return self.__Group17

    @Group17.setter
    def Group17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Group__Group17", None)
        self.__Group17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Group(self):
        return self.__Group

    @Group.setter
    def Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Group__Group", None)
        self.__Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features11"):
                opp_val = getattr(old_value, "features11", None)
                if opp_val == self:
                    setattr(old_value, "features11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features11"):
                opp_val = getattr(value, "features11", None)
                setattr(value, "features11", self)

    @property
    def groups(self):
        return self.__groups

    @groups.setter
    def groups(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Group__groups", None)
        self.__groups = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature22"):
                opp_val = getattr(old_value, "Feature22", None)
                if opp_val == self:
                    setattr(old_value, "Feature22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature22"):
                opp_val = getattr(value, "Feature22", None)
                setattr(value, "Feature22", self)

class fm_Attribute:

    def __init__(self, id: str, name: str, type: str, value: str, description: str, comment: str, Attribute: "fm_Feature" = None, attributes: "fm_Feature" = None):
        self.id = id
        self.name = name
        self.type = type
        self.value = value
        self.description = description
        self.comment = comment
        self.Attribute = Attribute
        self.attributes = attributes
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature26"):
                opp_val = getattr(old_value, "Feature26", None)
                if opp_val == self:
                    setattr(old_value, "Feature26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature26"):
                opp_val = getattr(value, "Feature26", None)
                setattr(value, "Feature26", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Attribute__Attribute", None)
        self.__Attribute = value
        
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

class fm_Constraint:

    def __init__(self, value: str, language: str, description: str, comment: str, fm_Constraint: "fm_FeatureModel" = None, fm_Constraint28: "fm_FeatureModel" = None):
        self.value = value
        self.language = language
        self.description = description
        self.comment = comment
        self.fm_Constraint = fm_Constraint
        self.fm_Constraint28 = fm_Constraint28
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def fm_Constraint(self):
        return self.__fm_Constraint

    @fm_Constraint.setter
    def fm_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Constraint__fm_Constraint", None)
        self.__fm_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_FeatureModel5"):
                opp_val = getattr(old_value, "fm_FeatureModel5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_FeatureModel5"):
                opp_val = getattr(value, "fm_FeatureModel5", None)
                if opp_val is None:
                    setattr(value, "fm_FeatureModel5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fm_Constraint28(self):
        return self.__fm_Constraint28

    @fm_Constraint28.setter
    def fm_Constraint28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Constraint__fm_Constraint28", None)
        self.__fm_Constraint28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_FeatureModel29"):
                opp_val = getattr(old_value, "fm_FeatureModel29", None)
                if opp_val == self:
                    setattr(old_value, "fm_FeatureModel29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_FeatureModel29"):
                opp_val = getattr(value, "fm_FeatureModel29", None)
                setattr(value, "fm_FeatureModel29", self)

class fm_EObject:

    pass
class fm_Feature:

    def __init__(self, id: str, name: str, description: str, comment: str, lower: int, upper: int, root: bool, orphan: bool, optional: bool, mandatory: bool, cloneable: bool, fm_Feature: "fm_FeatureModel" = None, fm_Feature7: "fm_EObject" = None, fm_Feature3: "fm_FeatureModel" = None, feature: set["fm_Attribute"] = None, Feature15: "fm_Feature" = None, parentFeature: set["fm_Feature"] = None, parent: set["fm_Group"] = None, fm_Feature19: "fm_FeatureModel" = None, Feature: "fm_Feature" = None, features: "fm_Feature" = None, features11: "fm_Group" = None, Feature26: "fm_Attribute" = None, Feature22: "fm_Group" = None, Feature24: "fm_Group" = None):
        self.id = id
        self.name = name
        self.description = description
        self.comment = comment
        self.lower = lower
        self.upper = upper
        self.root = root
        self.orphan = orphan
        self.optional = optional
        self.mandatory = mandatory
        self.cloneable = cloneable
        self.fm_Feature = fm_Feature
        self.fm_Feature7 = fm_Feature7
        self.fm_Feature3 = fm_Feature3
        self.feature = feature if feature is not None else set()
        self.Feature15 = Feature15
        self.parentFeature = parentFeature if parentFeature is not None else set()
        self.parent = parent if parent is not None else set()
        self.fm_Feature19 = fm_Feature19
        self.Feature = Feature
        self.features = features
        self.features11 = features11
        self.Feature26 = Feature26
        self.Feature22 = Feature22
        self.Feature24 = Feature24
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def cloneable(self) -> bool:
        return self.__cloneable

    @cloneable.setter
    def cloneable(self, cloneable: bool):
        self.__cloneable = cloneable

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def orphan(self) -> bool:
        return self.__orphan

    @orphan.setter
    def orphan(self, orphan: bool):
        self.__orphan = orphan

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def root(self) -> bool:
        return self.__root

    @root.setter
    def root(self, root: bool):
        self.__root = root

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__Feature", None)
        self.__Feature = value
        
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

    @property
    def fm_Feature19(self):
        return self.__fm_Feature19

    @fm_Feature19.setter
    def fm_Feature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature19", None)
        self.__fm_Feature19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_FeatureModel20"):
                opp_val = getattr(old_value, "fm_FeatureModel20", None)
                if opp_val == self:
                    setattr(old_value, "fm_FeatureModel20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_FeatureModel20"):
                opp_val = getattr(value, "fm_FeatureModel20", None)
                setattr(value, "fm_FeatureModel20", self)

    @property
    def Feature22(self):
        return self.__Feature22

    @Feature22.setter
    def Feature22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__Feature22", None)
        self.__Feature22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groups"):
                opp_val = getattr(old_value, "groups", None)
                if opp_val == self:
                    setattr(old_value, "groups", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groups"):
                opp_val = getattr(value, "groups", None)
                setattr(value, "groups", self)

    @property
    def fm_Feature3(self):
        return self.__fm_Feature3

    @fm_Feature3.setter
    def fm_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature3", None)
        self.__fm_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_FeatureModel2"):
                opp_val = getattr(old_value, "fm_FeatureModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_FeatureModel2"):
                opp_val = getattr(value, "fm_FeatureModel2", None)
                if opp_val is None:
                    setattr(value, "fm_FeatureModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature"):
                opp_val = getattr(old_value, "Feature", None)
                if opp_val == self:
                    setattr(old_value, "Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature"):
                opp_val = getattr(value, "Feature", None)
                setattr(value, "Feature", self)

    @property
    def parentFeature(self):
        return self.__parentFeature

    @parentFeature.setter
    def parentFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__parentFeature", None)
        self.__parentFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature15"):
                    opp_val = getattr(item, "Feature15", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature15"):
                    opp_val = getattr(item, "Feature15", None)
                    
                    setattr(item, "Feature15", self)
                    

    @property
    def Feature15(self):
        return self.__Feature15

    @Feature15.setter
    def Feature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__Feature15", None)
        self.__Feature15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentFeature"):
                opp_val = getattr(old_value, "parentFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentFeature"):
                opp_val = getattr(value, "parentFeature", None)
                if opp_val is None:
                    setattr(value, "parentFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Feature24(self):
        return self.__Feature24

    @Feature24.setter
    def Feature24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__Feature24", None)
        self.__Feature24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentGroup"):
                opp_val = getattr(old_value, "parentGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentGroup"):
                opp_val = getattr(value, "parentGroup", None)
                if opp_val is None:
                    setattr(value, "parentGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group17"):
                    opp_val = getattr(item, "Group17", None)
                    
                    if opp_val == self:
                        setattr(item, "Group17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group17"):
                    opp_val = getattr(item, "Group17", None)
                    
                    setattr(item, "Group17", self)
                    

    @property
    def features11(self):
        return self.__features11

    @features11.setter
    def features11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__features11", None)
        self.__features11 = value
        
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
    def Feature26(self):
        return self.__Feature26

    @Feature26.setter
    def Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__Feature26", None)
        self.__Feature26 = value
        
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
    def fm_Feature7(self):
        return self.__fm_Feature7

    @fm_Feature7.setter
    def fm_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature7", None)
        self.__fm_Feature7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_EObject"):
                opp_val = getattr(old_value, "fm_EObject", None)
                if opp_val == self:
                    setattr(old_value, "fm_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_EObject"):
                opp_val = getattr(value, "fm_EObject", None)
                setattr(value, "fm_EObject", self)

    @property
    def fm_Feature(self):
        return self.__fm_Feature

    @fm_Feature.setter
    def fm_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature", None)
        self.__fm_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_FeatureModel"):
                opp_val = getattr(old_value, "fm_FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "fm_FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_FeatureModel"):
                opp_val = getattr(value, "fm_FeatureModel", None)
                setattr(value, "fm_FeatureModel", self)

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

class fm_FeatureModel:

    def __init__(self, name: str, version: str, description: str, comment: str, fm_FeatureModel5: set["fm_Constraint"] = None, fm_FeatureModel: "fm_Feature" = None, fm_FeatureModel2: set["fm_Feature"] = None, fm_FeatureModel20: "fm_Feature" = None, fm_FeatureModel29: "fm_Constraint" = None):
        self.name = name
        self.version = version
        self.description = description
        self.comment = comment
        self.fm_FeatureModel5 = fm_FeatureModel5 if fm_FeatureModel5 is not None else set()
        self.fm_FeatureModel = fm_FeatureModel
        self.fm_FeatureModel2 = fm_FeatureModel2 if fm_FeatureModel2 is not None else set()
        self.fm_FeatureModel20 = fm_FeatureModel20
        self.fm_FeatureModel29 = fm_FeatureModel29
        
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
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def fm_FeatureModel29(self):
        return self.__fm_FeatureModel29

    @fm_FeatureModel29.setter
    def fm_FeatureModel29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_FeatureModel__fm_FeatureModel29", None)
        self.__fm_FeatureModel29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_Constraint28"):
                opp_val = getattr(old_value, "fm_Constraint28", None)
                if opp_val == self:
                    setattr(old_value, "fm_Constraint28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_Constraint28"):
                opp_val = getattr(value, "fm_Constraint28", None)
                setattr(value, "fm_Constraint28", self)

    @property
    def fm_FeatureModel2(self):
        return self.__fm_FeatureModel2

    @fm_FeatureModel2.setter
    def fm_FeatureModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_FeatureModel__fm_FeatureModel2", None)
        self.__fm_FeatureModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fm_Feature3"):
                    opp_val = getattr(item, "fm_Feature3", None)
                    
                    if opp_val == self:
                        setattr(item, "fm_Feature3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fm_Feature3"):
                    opp_val = getattr(item, "fm_Feature3", None)
                    
                    setattr(item, "fm_Feature3", self)
                    

    @property
    def fm_FeatureModel(self):
        return self.__fm_FeatureModel

    @fm_FeatureModel.setter
    def fm_FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_FeatureModel__fm_FeatureModel", None)
        self.__fm_FeatureModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_Feature"):
                opp_val = getattr(old_value, "fm_Feature", None)
                if opp_val == self:
                    setattr(old_value, "fm_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_Feature"):
                opp_val = getattr(value, "fm_Feature", None)
                setattr(value, "fm_Feature", self)

    @property
    def fm_FeatureModel5(self):
        return self.__fm_FeatureModel5

    @fm_FeatureModel5.setter
    def fm_FeatureModel5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_FeatureModel__fm_FeatureModel5", None)
        self.__fm_FeatureModel5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fm_Constraint"):
                    opp_val = getattr(item, "fm_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "fm_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fm_Constraint"):
                    opp_val = getattr(item, "fm_Constraint", None)
                    
                    setattr(item, "fm_Constraint", self)
                    

    @property
    def fm_FeatureModel20(self):
        return self.__fm_FeatureModel20

    @fm_FeatureModel20.setter
    def fm_FeatureModel20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_FeatureModel__fm_FeatureModel20", None)
        self.__fm_FeatureModel20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_Feature19"):
                opp_val = getattr(old_value, "fm_Feature19", None)
                if opp_val == self:
                    setattr(old_value, "fm_Feature19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_Feature19"):
                opp_val = getattr(value, "fm_Feature19", None)
                setattr(value, "fm_Feature19", self)

    def getFeaturesById(self, id: str):
        # TODO: Implement getFeaturesById method
        pass
