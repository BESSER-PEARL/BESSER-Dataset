from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SelectionOperator(Enum):
    deselect = "deselect"
    select = "select"
class ComparisonOperator(Enum):
    equal = "equal"
    geq = "geq"
    gt = "gt"
    leq = "leq"
    lt = "lt"


############################################
# Definition of Classes
############################################

class featureModel_IntValue:

    pass
class featureModel_VariabilityElement(ABC):

    pass
class featureModel_Condition:

    def __init__(self, type: str, featureModel_Condition: "featureModel_AdaptationRule" = None, featureModel_Condition21: "featureModel_Attribute" = None, featureModel_Condition24: "featureModel_IntValue" = None, featureModel_Condition26: "featureModel_Feature" = None):
        self.type = type
        self.featureModel_Condition = featureModel_Condition
        self.featureModel_Condition21 = featureModel_Condition21
        self.featureModel_Condition24 = featureModel_Condition24
        self.featureModel_Condition26 = featureModel_Condition26
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def featureModel_Condition26(self):
        return self.__featureModel_Condition26

    @featureModel_Condition26.setter
    def featureModel_Condition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Condition__featureModel_Condition26", None)
        self.__featureModel_Condition26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature27"):
                opp_val = getattr(old_value, "featureModel_Feature27", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Feature27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature27"):
                opp_val = getattr(value, "featureModel_Feature27", None)
                setattr(value, "featureModel_Feature27", self)

    @property
    def featureModel_Condition(self):
        return self.__featureModel_Condition

    @featureModel_Condition.setter
    def featureModel_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Condition__featureModel_Condition", None)
        self.__featureModel_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_AdaptationRule"):
                opp_val = getattr(old_value, "featureModel_AdaptationRule", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_AdaptationRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_AdaptationRule"):
                opp_val = getattr(value, "featureModel_AdaptationRule", None)
                setattr(value, "featureModel_AdaptationRule", self)

    @property
    def featureModel_Condition21(self):
        return self.__featureModel_Condition21

    @featureModel_Condition21.setter
    def featureModel_Condition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Condition__featureModel_Condition21", None)
        self.__featureModel_Condition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Attribute22"):
                opp_val = getattr(old_value, "featureModel_Attribute22", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Attribute22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Attribute22"):
                opp_val = getattr(value, "featureModel_Attribute22", None)
                setattr(value, "featureModel_Attribute22", self)

    @property
    def featureModel_Condition24(self):
        return self.__featureModel_Condition24

    @featureModel_Condition24.setter
    def featureModel_Condition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Condition__featureModel_Condition24", None)
        self.__featureModel_Condition24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_IntValue"):
                opp_val = getattr(old_value, "featureModel_IntValue", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_IntValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_IntValue"):
                opp_val = getattr(value, "featureModel_IntValue", None)
                setattr(value, "featureModel_IntValue", self)

class BooleanConstraint:

    pass
class featureModel_Excludes(BooleanConstraint):

    pass
class featureModel_Implies(BooleanConstraint):

    pass
class FMConstraint:

    pass
class featureModel_AdaptationRule(FMConstraint):

    pass
class featureModel_BooleanConstraint(FMConstraint):

    pass
class featureModel_Value:

    pass
class featureModel_Action:

    def __init__(self, type: str, featureModel_Action: "featureModel_AdaptationRule" = None, featureModel_Action29: "featureModel_Feature" = None):
        self.type = type
        self.featureModel_Action = featureModel_Action
        self.featureModel_Action29 = featureModel_Action29
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def featureModel_Action29(self):
        return self.__featureModel_Action29

    @featureModel_Action29.setter
    def featureModel_Action29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Action__featureModel_Action29", None)
        self.__featureModel_Action29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature30"):
                opp_val = getattr(old_value, "featureModel_Feature30", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Feature30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature30"):
                opp_val = getattr(value, "featureModel_Feature30", None)
                setattr(value, "featureModel_Feature30", self)

    @property
    def featureModel_Action(self):
        return self.__featureModel_Action

    @featureModel_Action.setter
    def featureModel_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Action__featureModel_Action", None)
        self.__featureModel_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_AdaptationRule19"):
                opp_val = getattr(old_value, "featureModel_AdaptationRule19", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_AdaptationRule19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_AdaptationRule19"):
                opp_val = getattr(value, "featureModel_AdaptationRule19", None)
                setattr(value, "featureModel_AdaptationRule19", self)

class Alternative:

    pass
class featureModel_Exclusive(Alternative):

    pass
class VariabilityElement:

    pass
class featureModel_Attribute(VariabilityElement):

    def __init__(self, name: str, runtime: bool, featureModel_Attribute: "featureModel_Feature" = None, featureModel_Attribute11: "featureModel_Value" = None, featureModel_Attribute22: "featureModel_Condition" = None):
        self.name = name
        self.runtime = runtime
        self.featureModel_Attribute = featureModel_Attribute
        self.featureModel_Attribute11 = featureModel_Attribute11
        self.featureModel_Attribute22 = featureModel_Attribute22
        
    @property
    def runtime(self) -> bool:
        return self.__runtime

    @runtime.setter
    def runtime(self, runtime: bool):
        self.__runtime = runtime

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def featureModel_Attribute(self):
        return self.__featureModel_Attribute

    @featureModel_Attribute.setter
    def featureModel_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Attribute__featureModel_Attribute", None)
        self.__featureModel_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature4"):
                opp_val = getattr(old_value, "featureModel_Feature4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature4"):
                opp_val = getattr(value, "featureModel_Feature4", None)
                if opp_val is None:
                    setattr(value, "featureModel_Feature4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModel_Attribute22(self):
        return self.__featureModel_Attribute22

    @featureModel_Attribute22.setter
    def featureModel_Attribute22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Attribute__featureModel_Attribute22", None)
        self.__featureModel_Attribute22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Condition21"):
                opp_val = getattr(old_value, "featureModel_Condition21", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Condition21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Condition21"):
                opp_val = getattr(value, "featureModel_Condition21", None)
                setattr(value, "featureModel_Condition21", self)

    @property
    def featureModel_Attribute11(self):
        return self.__featureModel_Attribute11

    @featureModel_Attribute11.setter
    def featureModel_Attribute11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Attribute__featureModel_Attribute11", None)
        self.__featureModel_Attribute11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Value"):
                opp_val = getattr(old_value, "featureModel_Value", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Value"):
                opp_val = getattr(value, "featureModel_Value", None)
                setattr(value, "featureModel_Value", self)

class featureModel_Feature(VariabilityElement):

    def __init__(self, name: str, selected: bool, unselected: bool, mandatory: bool, featureModel_Feature9: "featureModel_Alternative" = None, featureModel_Feature: "featureModel_FeatureModel" = None, featureModel_Feature4: set["featureModel_Attribute"] = None, featureModel_Feature7: "featureModel_Feature" = None, featureModel_Feature5: set["featureModel_Feature"] = None, featureModel_Feature13: "featureModel_BooleanConstraint" = None, featureModel_Feature16: "featureModel_BooleanConstraint" = None, featureModel_Feature27: "featureModel_Condition" = None, featureModel_Feature30: "featureModel_Action" = None):
        self.name = name
        self.selected = selected
        self.unselected = unselected
        self.mandatory = mandatory
        self.featureModel_Feature9 = featureModel_Feature9
        self.featureModel_Feature = featureModel_Feature
        self.featureModel_Feature4 = featureModel_Feature4 if featureModel_Feature4 is not None else set()
        self.featureModel_Feature7 = featureModel_Feature7
        self.featureModel_Feature5 = featureModel_Feature5 if featureModel_Feature5 is not None else set()
        self.featureModel_Feature13 = featureModel_Feature13
        self.featureModel_Feature16 = featureModel_Feature16
        self.featureModel_Feature27 = featureModel_Feature27
        self.featureModel_Feature30 = featureModel_Feature30
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def unselected(self) -> bool:
        return self.__unselected

    @unselected.setter
    def unselected(self, unselected: bool):
        self.__unselected = unselected

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def featureModel_Feature30(self):
        return self.__featureModel_Feature30

    @featureModel_Feature30.setter
    def featureModel_Feature30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature30", None)
        self.__featureModel_Feature30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Action29"):
                opp_val = getattr(old_value, "featureModel_Action29", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Action29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Action29"):
                opp_val = getattr(value, "featureModel_Action29", None)
                setattr(value, "featureModel_Action29", self)

    @property
    def featureModel_Feature9(self):
        return self.__featureModel_Feature9

    @featureModel_Feature9.setter
    def featureModel_Feature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature9", None)
        self.__featureModel_Feature9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Alternative"):
                opp_val = getattr(old_value, "featureModel_Alternative", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Alternative"):
                opp_val = getattr(value, "featureModel_Alternative", None)
                if opp_val is None:
                    setattr(value, "featureModel_Alternative", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModel_Feature5(self):
        return self.__featureModel_Feature5

    @featureModel_Feature5.setter
    def featureModel_Feature5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature5", None)
        self.__featureModel_Feature5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_Feature7"):
                    opp_val = getattr(item, "featureModel_Feature7", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_Feature7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_Feature7"):
                    opp_val = getattr(item, "featureModel_Feature7", None)
                    
                    setattr(item, "featureModel_Feature7", self)
                    

    @property
    def featureModel_Feature7(self):
        return self.__featureModel_Feature7

    @featureModel_Feature7.setter
    def featureModel_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature7", None)
        self.__featureModel_Feature7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Feature5"):
                opp_val = getattr(old_value, "featureModel_Feature5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Feature5"):
                opp_val = getattr(value, "featureModel_Feature5", None)
                if opp_val is None:
                    setattr(value, "featureModel_Feature5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModel_Feature16(self):
        return self.__featureModel_Feature16

    @featureModel_Feature16.setter
    def featureModel_Feature16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature16", None)
        self.__featureModel_Feature16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_BooleanConstraint15"):
                opp_val = getattr(old_value, "featureModel_BooleanConstraint15", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_BooleanConstraint15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_BooleanConstraint15"):
                opp_val = getattr(value, "featureModel_BooleanConstraint15", None)
                setattr(value, "featureModel_BooleanConstraint15", self)

    @property
    def featureModel_Feature4(self):
        return self.__featureModel_Feature4

    @featureModel_Feature4.setter
    def featureModel_Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature4", None)
        self.__featureModel_Feature4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModel_Attribute"):
                    opp_val = getattr(item, "featureModel_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModel_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModel_Attribute"):
                    opp_val = getattr(item, "featureModel_Attribute", None)
                    
                    setattr(item, "featureModel_Attribute", self)
                    

    @property
    def featureModel_Feature(self):
        return self.__featureModel_Feature

    @featureModel_Feature.setter
    def featureModel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature", None)
        self.__featureModel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_FeatureModel2"):
                opp_val = getattr(old_value, "featureModel_FeatureModel2", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_FeatureModel2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_FeatureModel2"):
                opp_val = getattr(value, "featureModel_FeatureModel2", None)
                setattr(value, "featureModel_FeatureModel2", self)

    @property
    def featureModel_Feature13(self):
        return self.__featureModel_Feature13

    @featureModel_Feature13.setter
    def featureModel_Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature13", None)
        self.__featureModel_Feature13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_BooleanConstraint"):
                opp_val = getattr(old_value, "featureModel_BooleanConstraint", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_BooleanConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_BooleanConstraint"):
                opp_val = getattr(value, "featureModel_BooleanConstraint", None)
                setattr(value, "featureModel_BooleanConstraint", self)

    @property
    def featureModel_Feature27(self):
        return self.__featureModel_Feature27

    @featureModel_Feature27.setter
    def featureModel_Feature27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModel_Feature__featureModel_Feature27", None)
        self.__featureModel_Feature27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModel_Condition26"):
                opp_val = getattr(old_value, "featureModel_Condition26", None)
                if opp_val == self:
                    setattr(old_value, "featureModel_Condition26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModel_Condition26"):
                opp_val = getattr(value, "featureModel_Condition26", None)
                setattr(value, "featureModel_Condition26", self)

class featureModel_FMConstraint(ABC):

    pass
class featureModel_FeatureModel:

    pass
class Feature:

    pass
class featureModel_Alternative(Feature):

    pass