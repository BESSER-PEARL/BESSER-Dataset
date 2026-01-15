from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AttributeComparisonOperator(Enum):
    equal = "equal"
    unequal = "unequal"
    greaterThan = "greaterThan"
    greaterThanOrEqual = "greaterThanOrEqual"
    lessThan = "lessThan"
    lessThanOrEqual = "lessThanOrEqual"
class SelectedState(Enum):
    selected = "selected"
    deselected = "deselected"
    undetermined = "undetermined"


############################################
# Definition of Classes
############################################

class BinaryExpression:

    pass
class feature_OrExpression(BinaryExpression):

    pass
class feature_ImpliesExpression(BinaryExpression):

    pass
class feature_AndExpression(BinaryExpression):

    pass
class AttributeOperand:

    pass
class feature_AttributeValueLiteral(AttributeOperand):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class feature_AttributeReference(AttributeOperand):

    pass
class feature_ExcludesExpression(BinaryExpression):

    pass
class feature_AttributeOperand(ABC):

    pass
class feature_Identifiable(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class feature_Interval:

    def __init__(self, lowerBound: int, upperBound: int, feature_Interval: "feature_ContinuousDomain" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.feature_Interval = feature_Interval
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def feature_Interval(self):
        return self.__feature_Interval

    @feature_Interval.setter
    def feature_Interval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Interval__feature_Interval", None)
        self.__feature_Interval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_ContinuousDomain"):
                opp_val = getattr(old_value, "feature_ContinuousDomain", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_ContinuousDomain"):
                opp_val = getattr(value, "feature_ContinuousDomain", None)
                if opp_val is None:
                    setattr(value, "feature_ContinuousDomain", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UnaryExpression:

    pass
class feature_NestedExpression(UnaryExpression):

    pass
class feature_NotExpression(UnaryExpression):

    pass
class AtomicExpression:

    pass
class feature_AttributeComparisonExpression(AtomicExpression):

    def __init__(self, operator: str, feature_AttributeComparisonExpression: "feature_AttributeOperand" = None, feature_AttributeComparisonExpression36: "feature_AttributeOperand" = None):
        self.operator = operator
        self.feature_AttributeComparisonExpression = feature_AttributeComparisonExpression
        self.feature_AttributeComparisonExpression36 = feature_AttributeComparisonExpression36
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def feature_AttributeComparisonExpression(self):
        return self.__feature_AttributeComparisonExpression

    @feature_AttributeComparisonExpression.setter
    def feature_AttributeComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_AttributeComparisonExpression__feature_AttributeComparisonExpression", None)
        self.__feature_AttributeComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_AttributeOperand"):
                opp_val = getattr(old_value, "feature_AttributeOperand", None)
                if opp_val == self:
                    setattr(old_value, "feature_AttributeOperand", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_AttributeOperand"):
                opp_val = getattr(value, "feature_AttributeOperand", None)
                setattr(value, "feature_AttributeOperand", self)

    @property
    def feature_AttributeComparisonExpression36(self):
        return self.__feature_AttributeComparisonExpression36

    @feature_AttributeComparisonExpression36.setter
    def feature_AttributeComparisonExpression36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_AttributeComparisonExpression__feature_AttributeComparisonExpression36", None)
        self.__feature_AttributeComparisonExpression36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_AttributeOperand37"):
                opp_val = getattr(old_value, "feature_AttributeOperand37", None)
                if opp_val == self:
                    setattr(old_value, "feature_AttributeOperand37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_AttributeOperand37"):
                opp_val = getattr(value, "feature_AttributeOperand37", None)
                setattr(value, "feature_AttributeOperand37", self)

class feature_FeatureReference(AtomicExpression):

    pass
class Expression:

    pass
class feature_AtomicExpression(Expression):

    pass
class feature_BinaryExpression(Expression):

    pass
class feature_UnaryExpression(Expression):

    pass
class Domain:

    pass
class feature_ContinuousDomain(Domain):

    pass
class feature_EnumDomain(Domain):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class feature_Domain(ABC):

    pass
class feature_Expression(ABC):

    pass
class Identifiable:

    pass
class feature_Constraint(Identifiable):

    pass
class feature_Annotation:

    pass
class feature_Group(Identifiable):

    def __init__(self, minCardinality: int, maxCardinality: int, Group: "feature_Feature" = None, Group11: "feature_Feature" = None, groups: "feature_Feature" = None, parentGroup: set["feature_Feature"] = None):
        self.minCardinality = minCardinality
        self.maxCardinality = maxCardinality
        self.Group = Group
        self.Group11 = Group11
        self.groups = groups
        self.parentGroup = parentGroup if parentGroup is not None else set()
        
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
                if hasattr(item, "Feature16"):
                    opp_val = getattr(item, "Feature16", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature16"):
                    opp_val = getattr(item, "Feature16", None)
                    
                    setattr(item, "Feature16", self)
                    

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

class feature_Attribute:

    def __init__(self, name: str, value: str, Attribute: "feature_Feature" = None, attributes: "feature_Feature" = None, feature_Attribute: "feature_Domain" = None, feature_Attribute39: "feature_AttributeReference" = None):
        self.name = name
        self.value = value
        self.Attribute = Attribute
        self.attributes = attributes
        self.feature_Attribute = feature_Attribute
        self.feature_Attribute39 = feature_Attribute39
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def feature_Attribute39(self):
        return self.__feature_Attribute39

    @feature_Attribute39.setter
    def feature_Attribute39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Attribute__feature_Attribute39", None)
        self.__feature_Attribute39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_AttributeReference"):
                opp_val = getattr(old_value, "feature_AttributeReference", None)
                if opp_val == self:
                    setattr(old_value, "feature_AttributeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_AttributeReference"):
                opp_val = getattr(value, "feature_AttributeReference", None)
                setattr(value, "feature_AttributeReference", self)

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
            if hasattr(old_value, "Feature20"):
                opp_val = getattr(old_value, "Feature20", None)
                if opp_val == self:
                    setattr(old_value, "Feature20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature20"):
                opp_val = getattr(value, "Feature20", None)
                setattr(value, "Feature20", self)

    @property
    def feature_Attribute(self):
        return self.__feature_Attribute

    @feature_Attribute.setter
    def feature_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Attribute__feature_Attribute", None)
        self.__feature_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_Domain"):
                opp_val = getattr(old_value, "feature_Domain", None)
                if opp_val == self:
                    setattr(old_value, "feature_Domain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_Domain"):
                opp_val = getattr(value, "feature_Domain", None)
                setattr(value, "feature_Domain", self)

class feature_Feature(Identifiable):

    def __init__(self, selected: str, name: str, feature_Feature: "feature_FeatureModel" = None, feature: set["feature_Attribute"] = None, parentFeature: set["feature_Group"] = None, childFeatures: "feature_Group" = None, feature13: set["feature_Annotation"] = None, Feature: "feature_Group" = None, Feature16: "feature_Group" = None, Feature20: "feature_Attribute" = None, Feature23: "feature_Annotation" = None, feature_Feature33: "feature_FeatureReference" = None):
        self.selected = selected
        self.name = name
        self.feature_Feature = feature_Feature
        self.feature = feature if feature is not None else set()
        self.parentFeature = parentFeature if parentFeature is not None else set()
        self.childFeatures = childFeatures
        self.feature13 = feature13 if feature13 is not None else set()
        self.Feature = Feature
        self.Feature16 = Feature16
        self.Feature20 = Feature20
        self.Feature23 = Feature23
        self.feature_Feature33 = feature_Feature33
        
    @property
    def selected(self) -> str:
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def feature_Feature(self):
        return self.__feature_Feature

    @feature_Feature.setter
    def feature_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature", None)
        self.__feature_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_FeatureModel"):
                opp_val = getattr(old_value, "feature_FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "feature_FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_FeatureModel"):
                opp_val = getattr(value, "feature_FeatureModel", None)
                setattr(value, "feature_FeatureModel", self)

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
    def Feature23(self):
        return self.__Feature23

    @Feature23.setter
    def Feature23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature23", None)
        self.__Feature23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotations"):
                opp_val = getattr(old_value, "annotations", None)
                if opp_val == self:
                    setattr(old_value, "annotations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotations"):
                opp_val = getattr(value, "annotations", None)
                setattr(value, "annotations", self)

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
    def feature_Feature33(self):
        return self.__feature_Feature33

    @feature_Feature33.setter
    def feature_Feature33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature33", None)
        self.__feature_Feature33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_FeatureReference"):
                opp_val = getattr(old_value, "feature_FeatureReference", None)
                if opp_val == self:
                    setattr(old_value, "feature_FeatureReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_FeatureReference"):
                opp_val = getattr(value, "feature_FeatureReference", None)
                setattr(value, "feature_FeatureReference", self)

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
    def feature13(self):
        return self.__feature13

    @feature13.setter
    def feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature13", None)
        self.__feature13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Annotation"):
                    opp_val = getattr(item, "Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Annotation"):
                    opp_val = getattr(item, "Annotation", None)
                    
                    setattr(item, "Annotation", self)
                    

    @property
    def Feature20(self):
        return self.__Feature20

    @Feature20.setter
    def Feature20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature20", None)
        self.__Feature20 = value
        
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

class feature_FeatureModel:

    def __init__(self, name: str, FeatureModel: "feature_FeatureModel" = None, children: "feature_FeatureModel" = None, FeatureModel4: "feature_FeatureModel" = None, parent: set["feature_FeatureModel"] = None, feature_FeatureModel: "feature_Feature" = None, feature_FeatureModel7: set["feature_Constraint"] = None):
        self.name = name
        self.FeatureModel = FeatureModel
        self.children = children
        self.FeatureModel4 = FeatureModel4
        self.parent = parent if parent is not None else set()
        self.feature_FeatureModel = feature_FeatureModel
        self.feature_FeatureModel7 = feature_FeatureModel7 if feature_FeatureModel7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "FeatureModel"):
                opp_val = getattr(old_value, "FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel"):
                opp_val = getattr(value, "FeatureModel", None)
                setattr(value, "FeatureModel", self)

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
                if hasattr(item, "FeatureModel4"):
                    opp_val = getattr(item, "FeatureModel4", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureModel4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureModel4"):
                    opp_val = getattr(item, "FeatureModel4", None)
                    
                    setattr(item, "FeatureModel4", self)
                    

    @property
    def feature_FeatureModel7(self):
        return self.__feature_FeatureModel7

    @feature_FeatureModel7.setter
    def feature_FeatureModel7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_FeatureModel__feature_FeatureModel7", None)
        self.__feature_FeatureModel7 = value if value is not None else set()
        
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
    def FeatureModel4(self):
        return self.__FeatureModel4

    @FeatureModel4.setter
    def FeatureModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_FeatureModel__FeatureModel4", None)
        self.__FeatureModel4 = value
        
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
    def feature_FeatureModel(self):
        return self.__feature_FeatureModel

    @feature_FeatureModel.setter
    def feature_FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_FeatureModel__feature_FeatureModel", None)
        self.__feature_FeatureModel = value
        
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
