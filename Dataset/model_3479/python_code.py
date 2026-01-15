from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class feature_Group:

    def __init__(self, minCardinality: int, maxCardinality: int, parentGroup: set["feature_Feature"] = None, Group: "feature_Feature" = None, Group11: "feature_Feature" = None, groups: "feature_Feature" = None):
        self.minCardinality = minCardinality
        self.maxCardinality = maxCardinality
        self.parentGroup = parentGroup if parentGroup is not None else set()
        self.Group = Group
        self.Group11 = Group11
        self.groups = groups
        
    @property
    def minCardinality(self) -> int:
        return self.__minCardinality

    @minCardinality.setter
    def minCardinality(self, minCardinality: int):
        self.__minCardinality = minCardinality

    @property
    def maxCardinality(self) -> int:
        return self.__maxCardinality

    @maxCardinality.setter
    def maxCardinality(self, maxCardinality: int):
        self.__maxCardinality = maxCardinality

    @property
    def Group(self):
        return self.__Group

    @Group.setter
    def Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Group__Group", None)
        self.__Group = value
        
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
    def groups(self):
        return self.__groups

    @groups.setter
    def groups(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Group__groups", None)
        self.__groups = value
        
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
    def Group11(self):
        return self.__Group11

    @Group11.setter
    def Group11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Group__Group11", None)
        self.__Group11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childFeatures"):
                opp_val = getattr(old_value, "childFeatures", None)
                if opp_val == self:
                    setattr(old_value, "childFeatures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childFeatures"):
                opp_val = getattr(value, "childFeatures", None)
                setattr(value, "childFeatures", self)

    @property
    def parentGroup(self):
        return self.__parentGroup

    @parentGroup.setter
    def parentGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Group__parentGroup", None)
        self.__parentGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature14"):
                    opp_val = getattr(item, "Feature14", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature14"):
                    opp_val = getattr(item, "Feature14", None)
                    
                    setattr(item, "Feature14", self)
                    

class feature_Attribute:

    def __init__(self, name: str, type: str, value: str, Attribute: "feature_Feature" = None, attributes: "feature_Feature" = None):
        self.name = name
        self.type = type
        self.value = value
        self.Attribute = Attribute
        self.attributes = attributes
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Attribute__Attribute", None)
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

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature16"):
                opp_val = getattr(old_value, "Feature16", None)
                if opp_val == self:
                    setattr(old_value, "Feature16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature16"):
                opp_val = getattr(value, "Feature16", None)
                setattr(value, "Feature16", self)

class feature_Feature:

    def __init__(self, name: str, minCardinality: int, maxCardinality: int, feature_Feature: "feature_FeatureModel" = None, Feature14: "feature_Group" = None, feature: set["feature_Attribute"] = None, parentFeature: set["feature_Group"] = None, childFeatures: "feature_Group" = None, Feature: "feature_Group" = None, Feature16: "feature_Attribute" = None):
        self.name = name
        self.minCardinality = minCardinality
        self.maxCardinality = maxCardinality
        self.feature_Feature = feature_Feature
        self.Feature14 = Feature14
        self.feature = feature if feature is not None else set()
        self.parentFeature = parentFeature if parentFeature is not None else set()
        self.childFeatures = childFeatures
        self.Feature = Feature
        self.Feature16 = Feature16
        
    @property
    def minCardinality(self) -> int:
        return self.__minCardinality

    @minCardinality.setter
    def minCardinality(self, minCardinality: int):
        self.__minCardinality = minCardinality

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def maxCardinality(self) -> int:
        return self.__maxCardinality

    @maxCardinality.setter
    def maxCardinality(self, maxCardinality: int):
        self.__maxCardinality = maxCardinality

    @property
    def childFeatures(self):
        return self.__childFeatures

    @childFeatures.setter
    def childFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__childFeatures", None)
        self.__childFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Group11"):
                opp_val = getattr(old_value, "Group11", None)
                if opp_val == self:
                    setattr(old_value, "Group11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Group11"):
                opp_val = getattr(value, "Group11", None)
                setattr(value, "Group11", self)

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
            if hasattr(old_value, "feature_FeatureModel2"):
                opp_val = getattr(old_value, "feature_FeatureModel2", None)
                if opp_val == self:
                    setattr(old_value, "feature_FeatureModel2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_FeatureModel2"):
                opp_val = getattr(value, "feature_FeatureModel2", None)
                setattr(value, "feature_FeatureModel2", self)

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature", None)
        self.__Feature = value
        
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
    def parentFeature(self):
        return self.__parentFeature

    @parentFeature.setter
    def parentFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__parentFeature", None)
        self.__parentFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    if opp_val == self:
                        setattr(item, "Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    setattr(item, "Group", self)
                    

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature", None)
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
                    

    @property
    def Feature16(self):
        return self.__Feature16

    @Feature16.setter
    def Feature16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature16", None)
        self.__Feature16 = value
        
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
    def Feature14(self):
        return self.__Feature14

    @Feature14.setter
    def Feature14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature14", None)
        self.__Feature14 = value
        
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

    def isMandatory(self) -> bool:
        # TODO: Implement isMandatory method
        pass

class feature_Constraint:

    def __init__(self, language: str, expression: str, feature_Constraint: "feature_FeatureModel" = None):
        self.language = language
        self.expression = expression
        self.feature_Constraint = feature_Constraint
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def feature_Constraint(self):
        return self.__feature_Constraint

    @feature_Constraint.setter
    def feature_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Constraint__feature_Constraint", None)
        self.__feature_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_FeatureModel"):
                opp_val = getattr(old_value, "feature_FeatureModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_FeatureModel"):
                opp_val = getattr(value, "feature_FeatureModel", None)
                if opp_val is None:
                    setattr(value, "feature_FeatureModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class feature_FeatureModel:

    def __init__(self, name: str, feature_FeatureModel: set["feature_Constraint"] = None, feature_FeatureModel2: "feature_Feature" = None, FeatureModel: "feature_FeatureModel" = None, parent: set["feature_FeatureModel"] = None, FeatureModel7: "feature_FeatureModel" = None, children: "feature_FeatureModel" = None):
        self.name = name
        self.feature_FeatureModel = feature_FeatureModel if feature_FeatureModel is not None else set()
        self.feature_FeatureModel2 = feature_FeatureModel2
        self.FeatureModel = FeatureModel
        self.parent = parent if parent is not None else set()
        self.FeatureModel7 = FeatureModel7
        self.children = children
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_FeatureModel__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureModel"):
                    opp_val = getattr(item, "FeatureModel", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureModel"):
                    opp_val = getattr(item, "FeatureModel", None)
                    
                    setattr(item, "FeatureModel", self)
                    

    @property
    def FeatureModel7(self):
        return self.__FeatureModel7

    @FeatureModel7.setter
    def FeatureModel7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_FeatureModel__FeatureModel7", None)
        self.__FeatureModel7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_FeatureModel__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel7"):
                opp_val = getattr(old_value, "FeatureModel7", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel7"):
                opp_val = getattr(value, "FeatureModel7", None)
                setattr(value, "FeatureModel7", self)

    @property
    def feature_FeatureModel(self):
        return self.__feature_FeatureModel

    @feature_FeatureModel.setter
    def feature_FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_FeatureModel__feature_FeatureModel", None)
        self.__feature_FeatureModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "feature_Constraint"):
                    opp_val = getattr(item, "feature_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "feature_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "feature_Constraint"):
                    opp_val = getattr(item, "feature_Constraint", None)
                    
                    setattr(item, "feature_Constraint", self)
                    

    @property
    def feature_FeatureModel2(self):
        return self.__feature_FeatureModel2

    @feature_FeatureModel2.setter
    def feature_FeatureModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_FeatureModel__feature_FeatureModel2", None)
        self.__feature_FeatureModel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_Feature"):
                opp_val = getattr(old_value, "feature_Feature", None)
                if opp_val == self:
                    setattr(old_value, "feature_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_Feature"):
                opp_val = getattr(value, "feature_Feature", None)
                setattr(value, "feature_Feature", self)

    @property
    def FeatureModel(self):
        return self.__FeatureModel

    @FeatureModel.setter
    def FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_FeatureModel__FeatureModel", None)
        self.__FeatureModel = value
        
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

    def getMandatoryFeatures(self) -> str:
        # TODO: Implement getMandatoryFeatures method
        pass

    def getAllFeatures(self) -> str:
        # TODO: Implement getAllFeatures method
        pass
