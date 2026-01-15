from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Relop(Enum):
    equal = "equal"
    unequal = "unequal"
    greaterThan = "greaterThan"
    greaterThanOrEqual = "greaterThanOrEqual"
    lessThan = "lessThan"
    lessThanOrEqual = "lessThanOrEqual"
class FeatureState(Enum):
    unbound = "unbound"
    selected = "selected"
    deselected = "deselected"


############################################
# Definition of Classes
############################################

class FeatureConstraint:

    pass
class feature_Exclude(FeatureConstraint):

    pass
class feature_Imply(FeatureConstraint):

    pass
class feature_AttributeOperand(ABC):

    pass
class Constraint:

    pass
class feature_FeatureConstraint(Constraint):

    pass
class feature_AttributeConstraint(Constraint):

    def __init__(self, operator: str, feature_AttributeConstraint: "feature_AttributeOperand" = None, feature_AttributeConstraint18: "feature_AttributeOperand" = None):
        self.operator = operator
        self.feature_AttributeConstraint = feature_AttributeConstraint
        self.feature_AttributeConstraint18 = feature_AttributeConstraint18
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def feature_AttributeConstraint(self):
        return self.__feature_AttributeConstraint

    @feature_AttributeConstraint.setter
    def feature_AttributeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_AttributeConstraint__feature_AttributeConstraint", None)
        self.__feature_AttributeConstraint = value
        
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
    def feature_AttributeConstraint18(self):
        return self.__feature_AttributeConstraint18

    @feature_AttributeConstraint18.setter
    def feature_AttributeConstraint18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_AttributeConstraint__feature_AttributeConstraint18", None)
        self.__feature_AttributeConstraint18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_AttributeOperand19"):
                opp_val = getattr(old_value, "feature_AttributeOperand19", None)
                if opp_val == self:
                    setattr(old_value, "feature_AttributeOperand19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_AttributeOperand19"):
                opp_val = getattr(value, "feature_AttributeOperand19", None)
                setattr(value, "feature_AttributeOperand19", self)

class AttributeOperand:

    pass
class feature_AttributeValue(AttributeOperand):

    def __init__(self, name: str, int: int):
        self.name = name
        self.int = int
        
    @property
    def int(self) -> int:
        return self.__int

    @int.setter
    def int(self, int: int):
        self.__int = int

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class feature_AttributeReference(AttributeOperand):

    pass
class feature_DomainValue:

    def __init__(self, int: int, name: str, feature_DomainValue: "feature_DiscreteDomain" = None):
        self.int = int
        self.name = name
        self.feature_DomainValue = feature_DomainValue
        
    @property
    def int(self) -> int:
        return self.__int

    @int.setter
    def int(self, int: int):
        self.__int = int

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def feature_DomainValue(self):
        return self.__feature_DomainValue

    @feature_DomainValue.setter
    def feature_DomainValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_DomainValue__feature_DomainValue", None)
        self.__feature_DomainValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_DiscreteDomain"):
                opp_val = getattr(old_value, "feature_DiscreteDomain", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_DiscreteDomain"):
                opp_val = getattr(value, "feature_DiscreteDomain", None)
                if opp_val is None:
                    setattr(value, "feature_DiscreteDomain", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Domain:

    pass
class feature_DiscreteDomain(Domain):

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

    def __init__(self, lowerBound: int, upperBound: int, feature_Interval: "feature_NumericalDomain" = None):
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
            if hasattr(old_value, "feature_NumericalDomain"):
                opp_val = getattr(old_value, "feature_NumericalDomain", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_NumericalDomain"):
                opp_val = getattr(value, "feature_NumericalDomain", None)
                if opp_val is None:
                    setattr(value, "feature_NumericalDomain", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class feature_NumericalDomain(Domain):

    pass
class feature_Attribute:

    def __init__(self, name: str, value: str, deselectedDomainValues: str, attributes: "feature_Feature" = None, feature_Attribute: "feature_Domain" = None, Attribute: "feature_Feature" = None, feature_Attribute21: "feature_AttributeReference" = None):
        self.name = name
        self.value = value
        self.deselectedDomainValues = deselectedDomainValues
        self.attributes = attributes
        self.feature_Attribute = feature_Attribute
        self.Attribute = Attribute
        self.feature_Attribute21 = feature_Attribute21
        
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
    def deselectedDomainValues(self) -> str:
        return self.__deselectedDomainValues

    @deselectedDomainValues.setter
    def deselectedDomainValues(self, deselectedDomainValues: str):
        self.__deselectedDomainValues = deselectedDomainValues

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
    def feature_Attribute21(self):
        return self.__feature_Attribute21

    @feature_Attribute21.setter
    def feature_Attribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Attribute__feature_Attribute21", None)
        self.__feature_Attribute21 = value
        
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

class Identifiable:

    pass
class feature_Group(Identifiable):

    def __init__(self, minCardinality: int, maxCardinality: int, feature_Group: "feature_Feature" = None, feature_Group9: set["feature_Feature"] = None):
        self.minCardinality = minCardinality
        self.maxCardinality = maxCardinality
        self.feature_Group = feature_Group
        self.feature_Group9 = feature_Group9 if feature_Group9 is not None else set()
        
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

    def __init__(self, name: str, configurationState: str, feature_Feature: "feature_FeatureModel" = None, feature_Feature7: set["feature_Group"] = None, feature_Feature10: "feature_Group" = None, Feature: "feature_Attribute" = None, feature: set["feature_Attribute"] = None, feature_Feature24: "feature_AttributeReference" = None, feature_Feature26: "feature_FeatureConstraint" = None, feature_Feature29: "feature_FeatureConstraint" = None):
        self.name = name
        self.configurationState = configurationState
        self.feature_Feature = feature_Feature
        self.feature_Feature7 = feature_Feature7 if feature_Feature7 is not None else set()
        self.feature_Feature10 = feature_Feature10
        self.Feature = Feature
        self.feature = feature if feature is not None else set()
        self.feature_Feature24 = feature_Feature24
        self.feature_Feature26 = feature_Feature26
        self.feature_Feature29 = feature_Feature29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def configurationState(self) -> str:
        return self.__configurationState

    @configurationState.setter
    def configurationState(self, configurationState: str):
        self.__configurationState = configurationState

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
    def feature_Feature29(self):
        return self.__feature_Feature29

    @feature_Feature29.setter
    def feature_Feature29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature29", None)
        self.__feature_Feature29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_FeatureConstraint28"):
                opp_val = getattr(old_value, "feature_FeatureConstraint28", None)
                if opp_val == self:
                    setattr(old_value, "feature_FeatureConstraint28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_FeatureConstraint28"):
                opp_val = getattr(value, "feature_FeatureConstraint28", None)
                setattr(value, "feature_FeatureConstraint28", self)

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
    def feature_Feature26(self):
        return self.__feature_Feature26

    @feature_Feature26.setter
    def feature_Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature26", None)
        self.__feature_Feature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_FeatureConstraint"):
                opp_val = getattr(old_value, "feature_FeatureConstraint", None)
                if opp_val == self:
                    setattr(old_value, "feature_FeatureConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_FeatureConstraint"):
                opp_val = getattr(value, "feature_FeatureConstraint", None)
                setattr(value, "feature_FeatureConstraint", self)

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
    def feature_Feature24(self):
        return self.__feature_Feature24

    @feature_Feature24.setter
    def feature_Feature24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_feature_Feature__feature_Feature24", None)
        self.__feature_Feature24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feature_AttributeReference23"):
                opp_val = getattr(old_value, "feature_AttributeReference23", None)
                if opp_val == self:
                    setattr(old_value, "feature_AttributeReference23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feature_AttributeReference23"):
                opp_val = getattr(value, "feature_AttributeReference23", None)
                setattr(value, "feature_AttributeReference23", self)

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
