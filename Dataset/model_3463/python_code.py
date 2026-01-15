from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConstraintType(Enum):
    EXCLUDES = "EXCLUDES"
    REQUIRES = "REQUIRES"


############################################
# Definition of Classes
############################################

class Attribute:

    pass
class featuremodels_SimpleAttribute(Attribute):

    def __init__(self, type: str, value: str):
        self.type = type
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class featuremodels_Instance:

    def __init__(self, id: str, descritpion: str, featuremodels_Instance: "featuremodels_FeatureModel" = None, featuremodels_Instance21: set["featuremodels_Feature"] = None):
        self.id = id
        self.descritpion = descritpion
        self.featuremodels_Instance = featuremodels_Instance
        self.featuremodels_Instance21 = featuremodels_Instance21 if featuremodels_Instance21 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def descritpion(self) -> str:
        return self.__descritpion

    @descritpion.setter
    def descritpion(self, descritpion: str):
        self.__descritpion = descritpion

    @property
    def featuremodels_Instance(self):
        return self.__featuremodels_Instance

    @featuremodels_Instance.setter
    def featuremodels_Instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Instance__featuremodels_Instance", None)
        self.__featuremodels_Instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodels_FeatureModel19"):
                opp_val = getattr(old_value, "featuremodels_FeatureModel19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodels_FeatureModel19"):
                opp_val = getattr(value, "featuremodels_FeatureModel19", None)
                if opp_val is None:
                    setattr(value, "featuremodels_FeatureModel19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featuremodels_Instance21(self):
        return self.__featuremodels_Instance21

    @featuremodels_Instance21.setter
    def featuremodels_Instance21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Instance__featuremodels_Instance21", None)
        self.__featuremodels_Instance21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featuremodels_Feature22"):
                    opp_val = getattr(item, "featuremodels_Feature22", None)
                    
                    if opp_val == self:
                        setattr(item, "featuremodels_Feature22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featuremodels_Feature22"):
                    opp_val = getattr(item, "featuremodels_Feature22", None)
                    
                    setattr(item, "featuremodels_Feature22", self)
                    

class featuremodels_Constraint:

    def __init__(self, type: str, rule: str, name: str, featuremodels_Constraint: "featuremodels_FeatureModel" = None):
        self.type = type
        self.rule = rule
        self.name = name
        self.featuremodels_Constraint = featuremodels_Constraint
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rule(self) -> str:
        return self.__rule

    @rule.setter
    def rule(self, rule: str):
        self.__rule = rule

    @property
    def featuremodels_Constraint(self):
        return self.__featuremodels_Constraint

    @featuremodels_Constraint.setter
    def featuremodels_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Constraint__featuremodels_Constraint", None)
        self.__featuremodels_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodels_FeatureModel17"):
                opp_val = getattr(old_value, "featuremodels_FeatureModel17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodels_FeatureModel17"):
                opp_val = getattr(value, "featuremodels_FeatureModel17", None)
                if opp_val is None:
                    setattr(value, "featuremodels_FeatureModel17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class featuremodels_Attribute(ABC):

    def __init__(self, name: str, featuremodels_Attribute: "featuremodels_Feature" = None):
        self.name = name
        self.featuremodels_Attribute = featuremodels_Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featuremodels_Attribute(self):
        return self.__featuremodels_Attribute

    @featuremodels_Attribute.setter
    def featuremodels_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Attribute__featuremodels_Attribute", None)
        self.__featuremodels_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodels_Feature"):
                opp_val = getattr(old_value, "featuremodels_Feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodels_Feature"):
                opp_val = getattr(value, "featuremodels_Feature", None)
                if opp_val is None:
                    setattr(value, "featuremodels_Feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class featuremodels_FeatureModel:

    def __init__(self, name: str, featuremodels_FeatureModel: "featuremodels_Feature" = None, featuremodels_FeatureModel17: set["featuremodels_Constraint"] = None, featuremodels_FeatureModel19: set["featuremodels_Instance"] = None):
        self.name = name
        self.featuremodels_FeatureModel = featuremodels_FeatureModel
        self.featuremodels_FeatureModel17 = featuremodels_FeatureModel17 if featuremodels_FeatureModel17 is not None else set()
        self.featuremodels_FeatureModel19 = featuremodels_FeatureModel19 if featuremodels_FeatureModel19 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featuremodels_FeatureModel(self):
        return self.__featuremodels_FeatureModel

    @featuremodels_FeatureModel.setter
    def featuremodels_FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_FeatureModel__featuremodels_FeatureModel", None)
        self.__featuremodels_FeatureModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodels_Feature15"):
                opp_val = getattr(old_value, "featuremodels_Feature15", None)
                if opp_val == self:
                    setattr(old_value, "featuremodels_Feature15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodels_Feature15"):
                opp_val = getattr(value, "featuremodels_Feature15", None)
                setattr(value, "featuremodels_Feature15", self)

    @property
    def featuremodels_FeatureModel19(self):
        return self.__featuremodels_FeatureModel19

    @featuremodels_FeatureModel19.setter
    def featuremodels_FeatureModel19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_FeatureModel__featuremodels_FeatureModel19", None)
        self.__featuremodels_FeatureModel19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featuremodels_Instance"):
                    opp_val = getattr(item, "featuremodels_Instance", None)
                    
                    if opp_val == self:
                        setattr(item, "featuremodels_Instance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featuremodels_Instance"):
                    opp_val = getattr(item, "featuremodels_Instance", None)
                    
                    setattr(item, "featuremodels_Instance", self)
                    

    @property
    def featuremodels_FeatureModel17(self):
        return self.__featuremodels_FeatureModel17

    @featuremodels_FeatureModel17.setter
    def featuremodels_FeatureModel17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_FeatureModel__featuremodels_FeatureModel17", None)
        self.__featuremodels_FeatureModel17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featuremodels_Constraint"):
                    opp_val = getattr(item, "featuremodels_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "featuremodels_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featuremodels_Constraint"):
                    opp_val = getattr(item, "featuremodels_Constraint", None)
                    
                    setattr(item, "featuremodels_Constraint", self)
                    

class featuremodels_ContainmentAssociation:

    def __init__(self, upperBound: int, lowerBound: int, ContainmentAssociation: "featuremodels_Feature" = None, ContainmentAssociation8: "featuremodels_Feature" = None, containerParent: set["featuremodels_Feature"] = None, containers: "featuremodels_Feature" = None):
        self.upperBound = upperBound
        self.lowerBound = lowerBound
        self.ContainmentAssociation = ContainmentAssociation
        self.ContainmentAssociation8 = ContainmentAssociation8
        self.containerParent = containerParent if containerParent is not None else set()
        self.containers = containers
        
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
    def ContainmentAssociation(self):
        return self.__ContainmentAssociation

    @ContainmentAssociation.setter
    def ContainmentAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_ContainmentAssociation__ContainmentAssociation", None)
        self.__ContainmentAssociation = value
        
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
    def containers(self):
        return self.__containers

    @containers.setter
    def containers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_ContainmentAssociation__containers", None)
        self.__containers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature13"):
                opp_val = getattr(old_value, "Feature13", None)
                if opp_val == self:
                    setattr(old_value, "Feature13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature13"):
                opp_val = getattr(value, "Feature13", None)
                setattr(value, "Feature13", self)

    @property
    def containerParent(self):
        return self.__containerParent

    @containerParent.setter
    def containerParent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_ContainmentAssociation__containerParent", None)
        self.__containerParent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature11"):
                    opp_val = getattr(item, "Feature11", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature11"):
                    opp_val = getattr(item, "Feature11", None)
                    
                    setattr(item, "Feature11", self)
                    

    @property
    def ContainmentAssociation8(self):
        return self.__ContainmentAssociation8

    @ContainmentAssociation8.setter
    def ContainmentAssociation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_ContainmentAssociation__ContainmentAssociation8", None)
        self.__ContainmentAssociation8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subFeatures7"):
                opp_val = getattr(old_value, "subFeatures7", None)
                if opp_val == self:
                    setattr(old_value, "subFeatures7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subFeatures7"):
                opp_val = getattr(value, "subFeatures7", None)
                setattr(value, "subFeatures7", self)

class featuremodels_Feature:

    def __init__(self, lowerBound: int, name: str, root: bool, required: bool, upperBound: int, parent: set["featuremodels_ContainmentAssociation"] = None, subFeatures7: "featuremodels_ContainmentAssociation" = None, Feature: "featuremodels_Feature" = None, featureParent: set["featuremodels_Feature"] = None, Feature4: "featuremodels_Feature" = None, subFeatures: "featuremodels_Feature" = None, featuremodels_Feature15: "featuremodels_FeatureModel" = None, featuremodels_Feature: set["featuremodels_Attribute"] = None, Feature11: "featuremodels_ContainmentAssociation" = None, Feature13: "featuremodels_ContainmentAssociation" = None, featuremodels_Feature22: "featuremodels_Instance" = None):
        self.lowerBound = lowerBound
        self.name = name
        self.root = root
        self.required = required
        self.upperBound = upperBound
        self.parent = parent if parent is not None else set()
        self.subFeatures7 = subFeatures7
        self.Feature = Feature
        self.featureParent = featureParent if featureParent is not None else set()
        self.Feature4 = Feature4
        self.subFeatures = subFeatures
        self.featuremodels_Feature15 = featuremodels_Feature15
        self.featuremodels_Feature = featuremodels_Feature if featuremodels_Feature is not None else set()
        self.Feature11 = Feature11
        self.Feature13 = Feature13
        self.featuremodels_Feature22 = featuremodels_Feature22
        
    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def root(self) -> bool:
        return self.__root

    @root.setter
    def root(self, root: bool):
        self.__root = root

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featuremodels_Feature22(self):
        return self.__featuremodels_Feature22

    @featuremodels_Feature22.setter
    def featuremodels_Feature22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Feature__featuremodels_Feature22", None)
        self.__featuremodels_Feature22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodels_Instance21"):
                opp_val = getattr(old_value, "featuremodels_Instance21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodels_Instance21"):
                opp_val = getattr(value, "featuremodels_Instance21", None)
                if opp_val is None:
                    setattr(value, "featuremodels_Instance21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureParent"):
                opp_val = getattr(old_value, "featureParent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureParent"):
                opp_val = getattr(value, "featureParent", None)
                if opp_val is None:
                    setattr(value, "featureParent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureParent(self):
        return self.__featureParent

    @featureParent.setter
    def featureParent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Feature__featureParent", None)
        self.__featureParent = value if value is not None else set()
        
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
    def featuremodels_Feature(self):
        return self.__featuremodels_Feature

    @featuremodels_Feature.setter
    def featuremodels_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Feature__featuremodels_Feature", None)
        self.__featuremodels_Feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featuremodels_Attribute"):
                    opp_val = getattr(item, "featuremodels_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "featuremodels_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featuremodels_Attribute"):
                    opp_val = getattr(item, "featuremodels_Attribute", None)
                    
                    setattr(item, "featuremodels_Attribute", self)
                    

    @property
    def Feature13(self):
        return self.__Feature13

    @Feature13.setter
    def Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Feature__Feature13", None)
        self.__Feature13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containers"):
                opp_val = getattr(old_value, "containers", None)
                if opp_val == self:
                    setattr(old_value, "containers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containers"):
                opp_val = getattr(value, "containers", None)
                setattr(value, "containers", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Feature__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainmentAssociation"):
                    opp_val = getattr(item, "ContainmentAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainmentAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainmentAssociation"):
                    opp_val = getattr(item, "ContainmentAssociation", None)
                    
                    setattr(item, "ContainmentAssociation", self)
                    

    @property
    def subFeatures7(self):
        return self.__subFeatures7

    @subFeatures7.setter
    def subFeatures7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Feature__subFeatures7", None)
        self.__subFeatures7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContainmentAssociation8"):
                opp_val = getattr(old_value, "ContainmentAssociation8", None)
                if opp_val == self:
                    setattr(old_value, "ContainmentAssociation8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContainmentAssociation8"):
                opp_val = getattr(value, "ContainmentAssociation8", None)
                setattr(value, "ContainmentAssociation8", self)

    @property
    def Feature11(self):
        return self.__Feature11

    @Feature11.setter
    def Feature11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Feature__Feature11", None)
        self.__Feature11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerParent"):
                opp_val = getattr(old_value, "containerParent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerParent"):
                opp_val = getattr(value, "containerParent", None)
                if opp_val is None:
                    setattr(value, "containerParent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featuremodels_Feature15(self):
        return self.__featuremodels_Feature15

    @featuremodels_Feature15.setter
    def featuremodels_Feature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Feature__featuremodels_Feature15", None)
        self.__featuremodels_Feature15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featuremodels_FeatureModel"):
                opp_val = getattr(old_value, "featuremodels_FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "featuremodels_FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featuremodels_FeatureModel"):
                opp_val = getattr(value, "featuremodels_FeatureModel", None)
                setattr(value, "featuremodels_FeatureModel", self)

    @property
    def Feature4(self):
        return self.__Feature4

    @Feature4.setter
    def Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Feature__Feature4", None)
        self.__Feature4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subFeatures"):
                opp_val = getattr(old_value, "subFeatures", None)
                if opp_val == self:
                    setattr(old_value, "subFeatures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subFeatures"):
                opp_val = getattr(value, "subFeatures", None)
                setattr(value, "subFeatures", self)

    @property
    def subFeatures(self):
        return self.__subFeatures

    @subFeatures.setter
    def subFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featuremodels_Feature__subFeatures", None)
        self.__subFeatures = value
        
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
