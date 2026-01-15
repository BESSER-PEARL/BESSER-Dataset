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

class feature_AttributeOperand(ABC):

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
class AtomicExpression:

    pass
class feature_FeatureReference(AtomicExpression):

    pass
class feature_AttributeComparisonExpression(AtomicExpression):

    def __init__(self, operator: str, feature_AttributeComparisonExpression: "feature_AttributeOperand" = None, feature_AttributeComparisonExpression28: "feature_AttributeOperand" = None):
        self.operator = operator
        self.feature_AttributeComparisonExpression = feature_AttributeComparisonExpression
        self.feature_AttributeComparisonExpression28 = feature_AttributeComparisonExpression28
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def feature_AttributeComparisonExpression28(self):
        return self.__feature_AttributeComparisonExpression28

    @feature_AttributeComparisonExpression28.setter
    def feature_AttributeComparisonExpression28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_AttributeComparisonExpression__feature_AttributeComparisonExpression28", None)
        self.__feature_AttributeComparisonExpression28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_AttributeOperand29"):
                opp_val = getattr(old_value, "feature_AttributeOperand29", None)
                if opp_val == self:
                    setattr(old_value, "feature_AttributeOperand29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_AttributeOperand29"):
                opp_val = getattr(value, "feature_AttributeOperand29", None)
                setattr(value, "feature_AttributeOperand29", self)

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

class BinaryExpression:

    pass
class feature_ImpliesExpression(BinaryExpression):

    pass
class feature_OrExpression(BinaryExpression):

    pass
class feature_ExcludesExpression(BinaryExpression):

    pass
class feature_AndExpression(BinaryExpression):

    pass
class UnaryExpression:

    pass
class feature_NestedExpression(UnaryExpression):

    pass
class feature_NotExpression(UnaryExpression):

    pass
class Expression:

    pass
class feature_BinaryExpression(Expression):

    pass
class feature_AtomicExpression(Expression):

    pass
class feature_UnaryExpression(Expression):

    pass
class feature_Expression(ABC):

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

class feature_Attribute:

    def __init__(self, name: str, value: str, attributes: "feature_Feature" = None, feature_Attribute: "feature_Domain" = None, Attribute: "feature_Feature" = None, feature_Attribute31: "feature_AttributeReference" = None):
        self.name = name
        self.value = value
        self.attributes = attributes
        self.feature_Attribute = feature_Attribute
        self.Attribute = Attribute
        self.feature_Attribute31 = feature_Attribute31
        
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
    def feature_Attribute(self):
        return self.__feature_Attribute

    @feature_Attribute.setter
    def feature_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Attribute__feature_Attribute", None)
        self.__feature_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_Domain13"):
                opp_val = getattr(old_value, "feature_Domain13", None)
                if opp_val == self:
                    setattr(old_value, "feature_Domain13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_Domain13"):
                opp_val = getattr(value, "feature_Domain13", None)
                setattr(value, "feature_Domain13", self)

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
    def feature_Attribute31(self):
        return self.__feature_Attribute31

    @feature_Attribute31.setter
    def feature_Attribute31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Attribute__feature_Attribute31", None)
        self.__feature_Attribute31 = value
        
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
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Attribute__attributes", None)
        self.__attributes = value
        
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

class Domain:

    pass
class feature_ContinuousDomain(Domain):

    pass
class feature_DiscreteDomain(Domain):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class Identifiable:

    pass
class feature_Group(Identifiable):

    def __init__(self, minCardinality: int, maxCardinality: int, feature_Group: "feature_Feature" = None, feature_Group9: set["feature_Feature"] = None):
        self.minCardinality = minCardinality
        self.maxCardinality = maxCardinality
        self.feature_Group = feature_Group
        self.feature_Group9 = feature_Group9 if feature_Group9 is not None else set()
        
    @property
    def maxCardinality(self) -> int:
        return self.__maxCardinality

    @maxCardinality.setter
    def maxCardinality(self, maxCardinality: int):
        self.__maxCardinality = maxCardinality

    @property
    def minCardinality(self) -> int:
        return self.__minCardinality

    @minCardinality.setter
    def minCardinality(self, minCardinality: int):
        self.__minCardinality = minCardinality

    @property
    def feature_Group9(self):
        return self.__feature_Group9

    @feature_Group9.setter
    def feature_Group9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Group__feature_Group9", None)
        self.__feature_Group9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "feature_Feature10"):
                    opp_val = getattr(item, "feature_Feature10", None)
                    
                    if opp_val == self:
                        setattr(item, "feature_Feature10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "feature_Feature10"):
                    opp_val = getattr(item, "feature_Feature10", None)
                    
                    setattr(item, "feature_Feature10", self)
                    

    @property
    def feature_Group(self):
        return self.__feature_Group

    @feature_Group.setter
    def feature_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Group__feature_Group", None)
        self.__feature_Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_Feature7"):
                opp_val = getattr(old_value, "feature_Feature7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_Feature7"):
                opp_val = getattr(value, "feature_Feature7", None)
                if opp_val is None:
                    setattr(value, "feature_Feature7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class feature_Constraint(Identifiable):

    pass
class feature_Domain(Identifiable):

    pass
class feature_Feature(Identifiable):

    def __init__(self, name: str, selected: str, feature_Feature: "feature_FeatureModel" = None, feature_Feature7: set["feature_Group"] = None, feature_Feature10: "feature_Group" = None, Feature: "feature_Attribute" = None, feature: set["feature_Attribute"] = None, feature_Feature25: "feature_FeatureReference" = None):
        self.name = name
        self.selected = selected
        self.feature_Feature = feature_Feature
        self.feature_Feature7 = feature_Feature7 if feature_Feature7 is not None else set()
        self.feature_Feature10 = feature_Feature10
        self.Feature = Feature
        self.feature = feature if feature is not None else set()
        self.feature_Feature25 = feature_Feature25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def selected(self) -> str:
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected

    @property
    def feature_Feature10(self):
        return self.__feature_Feature10

    @feature_Feature10.setter
    def feature_Feature10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature10", None)
        self.__feature_Feature10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_Group9"):
                opp_val = getattr(old_value, "feature_Group9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_Group9"):
                opp_val = getattr(value, "feature_Group9", None)
                if opp_val is None:
                    setattr(value, "feature_Group9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def feature_Feature7(self):
        return self.__feature_Feature7

    @feature_Feature7.setter
    def feature_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature7", None)
        self.__feature_Feature7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "feature_Group"):
                    opp_val = getattr(item, "feature_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "feature_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "feature_Group"):
                    opp_val = getattr(item, "feature_Group", None)
                    
                    setattr(item, "feature_Group", self)
                    

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
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__Feature", None)
        self.__Feature = value
        
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
    def feature_Feature25(self):
        return self.__feature_Feature25

    @feature_Feature25.setter
    def feature_Feature25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature25", None)
        self.__feature_Feature25 = value
        
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

class feature_FeatureModel:

    def __init__(self, name: str, feature_FeatureModel: "feature_Feature" = None, feature_FeatureModel2: set["feature_Domain"] = None, feature_FeatureModel4: set["feature_Constraint"] = None):
        self.name = name
        self.feature_FeatureModel = feature_FeatureModel
        self.feature_FeatureModel2 = feature_FeatureModel2 if feature_FeatureModel2 is not None else set()
        self.feature_FeatureModel4 = feature_FeatureModel4 if feature_FeatureModel4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def feature_FeatureModel4(self):
        return self.__feature_FeatureModel4

    @feature_FeatureModel4.setter
    def feature_FeatureModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_FeatureModel__feature_FeatureModel4", None)
        self.__feature_FeatureModel4 = value if value is not None else set()
        
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
        self.__feature_FeatureModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "feature_Domain"):
                    opp_val = getattr(item, "feature_Domain", None)
                    
                    if opp_val == self:
                        setattr(item, "feature_Domain", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "feature_Domain"):
                    opp_val = getattr(item, "feature_Domain", None)
                    
                    setattr(item, "feature_Domain", self)
                    

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
