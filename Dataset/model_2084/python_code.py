from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DecisionType(Enum):
    manual = "manual"
    propagated = "propagated"
    autocompleted = "autocompleted"


############################################
# Definition of Classes
############################################

class sxfm_FeatureChoice:

    def __init__(self, selected: bool, decisionType: str, decisionStep: int, sxfm_FeatureChoice: "sxfm_FeatureModelConfiguaration" = None, sxfm_FeatureChoice27: "sxfm_Feature" = None):
        self.selected = selected
        self.decisionType = decisionType
        self.decisionStep = decisionStep
        self.sxfm_FeatureChoice = sxfm_FeatureChoice
        self.sxfm_FeatureChoice27 = sxfm_FeatureChoice27
        
    @property
    def decisionType(self) -> str:
        return self.__decisionType

    @decisionType.setter
    def decisionType(self, decisionType: str):
        self.__decisionType = decisionType

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def decisionStep(self) -> int:
        return self.__decisionStep

    @decisionStep.setter
    def decisionStep(self, decisionStep: int):
        self.__decisionStep = decisionStep

    @property
    def sxfm_FeatureChoice27(self):
        return self.__sxfm_FeatureChoice27

    @sxfm_FeatureChoice27.setter
    def sxfm_FeatureChoice27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_FeatureChoice__sxfm_FeatureChoice27", None)
        self.__sxfm_FeatureChoice27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sxfm_Feature28"):
                opp_val = getattr(old_value, "sxfm_Feature28", None)
                if opp_val == self:
                    setattr(old_value, "sxfm_Feature28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sxfm_Feature28"):
                opp_val = getattr(value, "sxfm_Feature28", None)
                setattr(value, "sxfm_Feature28", self)

    @property
    def sxfm_FeatureChoice(self):
        return self.__sxfm_FeatureChoice

    @sxfm_FeatureChoice.setter
    def sxfm_FeatureChoice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_FeatureChoice__sxfm_FeatureChoice", None)
        self.__sxfm_FeatureChoice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sxfm_FeatureModelConfiguaration25"):
                opp_val = getattr(old_value, "sxfm_FeatureModelConfiguaration25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sxfm_FeatureModelConfiguaration25"):
                opp_val = getattr(value, "sxfm_FeatureModelConfiguaration25", None)
                if opp_val is None:
                    setattr(value, "sxfm_FeatureModelConfiguaration25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sxfm_CommonFeature(ABC):

    pass
class sxfm_VariableFeature(ABC):

    pass
class sxfm_Literal(ABC):

    pass
class Literal:

    pass
class sxfm_Atom(Literal):

    pass
class sxfm_Not(Literal):

    pass
class sxfm_ConstraintableElement(ABC):

    pass
class sxfm_ContainableElement(ABC):

    pass
class sxfm_ContainerElement(ABC):

    pass
class sxfm_Data:

    def __init__(self, name: str, value: str, sxfm_Data: "sxfm_MetadataSet" = None):
        self.name = name
        self.value = value
        self.sxfm_Data = sxfm_Data
        
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
    def sxfm_Data(self):
        return self.__sxfm_Data

    @sxfm_Data.setter
    def sxfm_Data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_Data__sxfm_Data", None)
        self.__sxfm_Data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sxfm_MetadataSet23"):
                opp_val = getattr(old_value, "sxfm_MetadataSet23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sxfm_MetadataSet23"):
                opp_val = getattr(value, "sxfm_MetadataSet23", None)
                if opp_val is None:
                    setattr(value, "sxfm_MetadataSet23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sxfm_FeatureModelConfiguaration:

    pass
class sxfm_MetadataSet:

    pass
class sxfm_FeatureTree:

    pass
class sxfm_ConstraintsSet:

    pass
class sxfm_CardinalizedElement(ABC):

    def __init__(self, minCardinality: int, maxCardinality: int):
        self.minCardinality = minCardinality
        self.maxCardinality = maxCardinality
        
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

class sxfm_Or:

    pass
class sxfm_Constraint:

    def __init__(self, id: int, sxfm_Constraint: "sxfm_Or" = None, sxfm_Constraint15: "sxfm_ConstraintsSet" = None):
        self.id = id
        self.sxfm_Constraint = sxfm_Constraint
        self.sxfm_Constraint15 = sxfm_Constraint15
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def sxfm_Constraint(self):
        return self.__sxfm_Constraint

    @sxfm_Constraint.setter
    def sxfm_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_Constraint__sxfm_Constraint", None)
        self.__sxfm_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sxfm_Or"):
                opp_val = getattr(old_value, "sxfm_Or", None)
                if opp_val == self:
                    setattr(old_value, "sxfm_Or", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sxfm_Or"):
                opp_val = getattr(value, "sxfm_Or", None)
                setattr(value, "sxfm_Or", self)

    @property
    def sxfm_Constraint15(self):
        return self.__sxfm_Constraint15

    @sxfm_Constraint15.setter
    def sxfm_Constraint15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_Constraint__sxfm_Constraint15", None)
        self.__sxfm_Constraint15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sxfm_ConstraintsSet14"):
                opp_val = getattr(old_value, "sxfm_ConstraintsSet14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sxfm_ConstraintsSet14"):
                opp_val = getattr(value, "sxfm_ConstraintsSet14", None)
                if opp_val is None:
                    setattr(value, "sxfm_ConstraintsSet14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CardinalizedElement:

    pass
class sxfm_FeatureModel:

    def __init__(self, name: str, sxfm_FeatureModel: "sxfm_ConstraintsSet" = None, sxfm_FeatureModel6: "sxfm_FeatureTree" = None, sxfm_FeatureModel8: "sxfm_MetadataSet" = None, sxfm_FeatureModel10: set["sxfm_FeatureModelConfiguaration"] = None):
        self.name = name
        self.sxfm_FeatureModel = sxfm_FeatureModel
        self.sxfm_FeatureModel6 = sxfm_FeatureModel6
        self.sxfm_FeatureModel8 = sxfm_FeatureModel8
        self.sxfm_FeatureModel10 = sxfm_FeatureModel10 if sxfm_FeatureModel10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sxfm_FeatureModel6(self):
        return self.__sxfm_FeatureModel6

    @sxfm_FeatureModel6.setter
    def sxfm_FeatureModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_FeatureModel__sxfm_FeatureModel6", None)
        self.__sxfm_FeatureModel6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sxfm_FeatureTree"):
                opp_val = getattr(old_value, "sxfm_FeatureTree", None)
                if opp_val == self:
                    setattr(old_value, "sxfm_FeatureTree", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sxfm_FeatureTree"):
                opp_val = getattr(value, "sxfm_FeatureTree", None)
                setattr(value, "sxfm_FeatureTree", self)

    @property
    def sxfm_FeatureModel10(self):
        return self.__sxfm_FeatureModel10

    @sxfm_FeatureModel10.setter
    def sxfm_FeatureModel10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_FeatureModel__sxfm_FeatureModel10", None)
        self.__sxfm_FeatureModel10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sxfm_FeatureModelConfiguaration"):
                    opp_val = getattr(item, "sxfm_FeatureModelConfiguaration", None)
                    
                    if opp_val == self:
                        setattr(item, "sxfm_FeatureModelConfiguaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sxfm_FeatureModelConfiguaration"):
                    opp_val = getattr(item, "sxfm_FeatureModelConfiguaration", None)
                    
                    setattr(item, "sxfm_FeatureModelConfiguaration", self)
                    

    @property
    def sxfm_FeatureModel(self):
        return self.__sxfm_FeatureModel

    @sxfm_FeatureModel.setter
    def sxfm_FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_FeatureModel__sxfm_FeatureModel", None)
        self.__sxfm_FeatureModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sxfm_ConstraintsSet"):
                opp_val = getattr(old_value, "sxfm_ConstraintsSet", None)
                if opp_val == self:
                    setattr(old_value, "sxfm_ConstraintsSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sxfm_ConstraintsSet"):
                opp_val = getattr(value, "sxfm_ConstraintsSet", None)
                setattr(value, "sxfm_ConstraintsSet", self)

    @property
    def sxfm_FeatureModel8(self):
        return self.__sxfm_FeatureModel8

    @sxfm_FeatureModel8.setter
    def sxfm_FeatureModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_FeatureModel__sxfm_FeatureModel8", None)
        self.__sxfm_FeatureModel8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sxfm_MetadataSet"):
                opp_val = getattr(old_value, "sxfm_MetadataSet", None)
                if opp_val == self:
                    setattr(old_value, "sxfm_MetadataSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sxfm_MetadataSet"):
                opp_val = getattr(value, "sxfm_MetadataSet", None)
                setattr(value, "sxfm_MetadataSet", self)

class VariableFeature:

    pass
class CommonFeature:

    pass
class ConstraintableElement:

    pass
class Feature:

    pass
class ContainableElement:

    pass
class ContainerElement:

    pass
class sxfm_GroupedFeature(VariableFeature, Feature, ConstraintableElement, ContainerElement):

    pass
class sxfm_Optional(ContainableElement, VariableFeature, ConstraintableElement, Feature, ContainerElement):

    pass
class sxfm_Root(Feature, CommonFeature, ContainerElement):

    pass
class sxfm_Mandatory(ContainableElement, ConstraintableElement, CommonFeature, Feature, ContainerElement):

    pass
class sxfm_Feature(ABC):

    def __init__(self, name: str, id: str, treeLevel: int, description: str, sxfm_Feature: set["sxfm_Group"] = None, sxfm_Feature28: "sxfm_FeatureChoice" = None):
        self.name = name
        self.id = id
        self.treeLevel = treeLevel
        self.description = description
        self.sxfm_Feature = sxfm_Feature if sxfm_Feature is not None else set()
        self.sxfm_Feature28 = sxfm_Feature28
        
    @property
    def treeLevel(self) -> int:
        return self.__treeLevel

    @treeLevel.setter
    def treeLevel(self, treeLevel: int):
        self.__treeLevel = treeLevel

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def sxfm_Feature28(self):
        return self.__sxfm_Feature28

    @sxfm_Feature28.setter
    def sxfm_Feature28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_Feature__sxfm_Feature28", None)
        self.__sxfm_Feature28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sxfm_FeatureChoice27"):
                opp_val = getattr(old_value, "sxfm_FeatureChoice27", None)
                if opp_val == self:
                    setattr(old_value, "sxfm_FeatureChoice27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sxfm_FeatureChoice27"):
                opp_val = getattr(value, "sxfm_FeatureChoice27", None)
                setattr(value, "sxfm_FeatureChoice27", self)

    @property
    def sxfm_Feature(self):
        return self.__sxfm_Feature

    @sxfm_Feature.setter
    def sxfm_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_Feature__sxfm_Feature", None)
        self.__sxfm_Feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sxfm_Group"):
                    opp_val = getattr(item, "sxfm_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "sxfm_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sxfm_Group"):
                    opp_val = getattr(item, "sxfm_Group", None)
                    
                    setattr(item, "sxfm_Group", self)
                    

class sxfm_Group(CardinalizedElement):

    def __init__(self, id: str, sxfm_Group: "sxfm_Feature" = None, sxfm_Group2: set["sxfm_GroupedFeature"] = None):
        self.id = id
        self.sxfm_Group = sxfm_Group
        self.sxfm_Group2 = sxfm_Group2 if sxfm_Group2 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def sxfm_Group2(self):
        return self.__sxfm_Group2

    @sxfm_Group2.setter
    def sxfm_Group2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_Group__sxfm_Group2", None)
        self.__sxfm_Group2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sxfm_GroupedFeature"):
                    opp_val = getattr(item, "sxfm_GroupedFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "sxfm_GroupedFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sxfm_GroupedFeature"):
                    opp_val = getattr(item, "sxfm_GroupedFeature", None)
                    
                    setattr(item, "sxfm_GroupedFeature", self)
                    

    @property
    def sxfm_Group(self):
        return self.__sxfm_Group

    @sxfm_Group.setter
    def sxfm_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sxfm_Group__sxfm_Group", None)
        self.__sxfm_Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sxfm_Feature"):
                opp_val = getattr(old_value, "sxfm_Feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sxfm_Feature"):
                opp_val = getattr(value, "sxfm_Feature", None)
                if opp_val is None:
                    setattr(value, "sxfm_Feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
