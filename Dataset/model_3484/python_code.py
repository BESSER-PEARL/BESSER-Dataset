from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SelectionState(Enum):
    selected = "selected"
    unselected = "unselected"
class VariabilityType(Enum):
    or = "or"
    optional = "optional"
    mandatory = "mandatory"
    alternative = "alternative"


############################################
# Definition of Classes
############################################

class featureModelMetamodel_ConfigurationModel:

    pass
class Selection:

    pass
class featureModelMetamodel_ClonableSelection(Selection):

    def __init__(self, instance: str):
        self.instance = instance
        
    @property
    def instance(self) -> str:
        return self.__instance

    @instance.setter
    def instance(self, instance: str):
        self.__instance = instance

class featureModelMetamodel_Selection:

    def __init__(self, state: str, name: str, featureModelMetamodel_Selection: "featureModelMetamodel_Feature" = None, featureModelMetamodel_Selection23: "featureModelMetamodel_ConfigurationModel" = None):
        self.state = state
        self.name = name
        self.featureModelMetamodel_Selection = featureModelMetamodel_Selection
        self.featureModelMetamodel_Selection23 = featureModelMetamodel_Selection23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def featureModelMetamodel_Selection(self):
        return self.__featureModelMetamodel_Selection

    @featureModelMetamodel_Selection.setter
    def featureModelMetamodel_Selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Selection__featureModelMetamodel_Selection", None)
        self.__featureModelMetamodel_Selection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_Feature21"):
                opp_val = getattr(old_value, "featureModelMetamodel_Feature21", None)
                if opp_val == self:
                    setattr(old_value, "featureModelMetamodel_Feature21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_Feature21"):
                opp_val = getattr(value, "featureModelMetamodel_Feature21", None)
                setattr(value, "featureModelMetamodel_Feature21", self)

    @property
    def featureModelMetamodel_Selection23(self):
        return self.__featureModelMetamodel_Selection23

    @featureModelMetamodel_Selection23.setter
    def featureModelMetamodel_Selection23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Selection__featureModelMetamodel_Selection23", None)
        self.__featureModelMetamodel_Selection23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_ConfigurationModel"):
                opp_val = getattr(old_value, "featureModelMetamodel_ConfigurationModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_ConfigurationModel"):
                opp_val = getattr(value, "featureModelMetamodel_ConfigurationModel", None)
                if opp_val is None:
                    setattr(value, "featureModelMetamodel_ConfigurationModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Multiplicity:

    pass
class featureModelMetamodel_FeatureModel:

    pass
class featureModelMetamodel_Constraint:

    def __init__(self, id: str, language: str, code: str, featureModelMetamodel_Constraint: "featureModelMetamodel_FeatureModel" = None):
        self.id = id
        self.language = language
        self.code = code
        self.featureModelMetamodel_Constraint = featureModelMetamodel_Constraint
        
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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def featureModelMetamodel_Constraint(self):
        return self.__featureModelMetamodel_Constraint

    @featureModelMetamodel_Constraint.setter
    def featureModelMetamodel_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Constraint__featureModelMetamodel_Constraint", None)
        self.__featureModelMetamodel_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_FeatureModel13"):
                opp_val = getattr(old_value, "featureModelMetamodel_FeatureModel13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_FeatureModel13"):
                opp_val = getattr(value, "featureModelMetamodel_FeatureModel13", None)
                if opp_val is None:
                    setattr(value, "featureModelMetamodel_FeatureModel13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class featureModelMetamodel_Attribute:

    pass
class featureModelMetamodel_Multiplicity:

    def __init__(self, lower: str, upper: str, featureModelMetamodel_Multiplicity: "featureModelMetamodel_ClonableFeature" = None):
        self.lower = lower
        self.upper = upper
        self.featureModelMetamodel_Multiplicity = featureModelMetamodel_Multiplicity
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def featureModelMetamodel_Multiplicity(self):
        return self.__featureModelMetamodel_Multiplicity

    @featureModelMetamodel_Multiplicity.setter
    def featureModelMetamodel_Multiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Multiplicity__featureModelMetamodel_Multiplicity", None)
        self.__featureModelMetamodel_Multiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_ClonableFeature"):
                opp_val = getattr(old_value, "featureModelMetamodel_ClonableFeature", None)
                if opp_val == self:
                    setattr(old_value, "featureModelMetamodel_ClonableFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_ClonableFeature"):
                opp_val = getattr(value, "featureModelMetamodel_ClonableFeature", None)
                setattr(value, "featureModelMetamodel_ClonableFeature", self)

class Feature:

    pass
class featureModelMetamodel_AbstractFeature(Feature):

    pass
class featureModelMetamodel_ClonableFeature(Feature):

    pass
class featureModelMetamodel_VariableFeature(Feature):

    pass
class featureModelMetamodel_GroupMultiplicity(Multiplicity):

    pass
class featureModelMetamodel_Feature:

    def __init__(self, variabilityType: str, name: str, id: str, featureModelMetamodel_Feature: "featureModelMetamodel_Feature" = None, featureModelMetamodel_Feature0: set["featureModelMetamodel_Feature"] = None, featureModelMetamodel_Feature3: "featureModelMetamodel_GroupMultiplicity" = None, featureModelMetamodel_Feature8: "featureModelMetamodel_Feature" = None, featureModelMetamodel_Feature6: "featureModelMetamodel_Feature" = None, featureModelMetamodel_Feature5: set["featureModelMetamodel_Attribute"] = None, featureModelMetamodel_Feature11: "featureModelMetamodel_FeatureModel" = None, featureModelMetamodel_Feature19: "featureModelMetamodel_GroupMultiplicity" = None, featureModelMetamodel_Feature21: "featureModelMetamodel_Selection" = None, featureModelMetamodel_Feature16: "featureModelMetamodel_FeatureModel" = None):
        self.variabilityType = variabilityType
        self.name = name
        self.id = id
        self.featureModelMetamodel_Feature = featureModelMetamodel_Feature
        self.featureModelMetamodel_Feature0 = featureModelMetamodel_Feature0 if featureModelMetamodel_Feature0 is not None else set()
        self.featureModelMetamodel_Feature3 = featureModelMetamodel_Feature3
        self.featureModelMetamodel_Feature8 = featureModelMetamodel_Feature8
        self.featureModelMetamodel_Feature6 = featureModelMetamodel_Feature6
        self.featureModelMetamodel_Feature5 = featureModelMetamodel_Feature5 if featureModelMetamodel_Feature5 is not None else set()
        self.featureModelMetamodel_Feature11 = featureModelMetamodel_Feature11
        self.featureModelMetamodel_Feature19 = featureModelMetamodel_Feature19
        self.featureModelMetamodel_Feature21 = featureModelMetamodel_Feature21
        self.featureModelMetamodel_Feature16 = featureModelMetamodel_Feature16
        
    @property
    def variabilityType(self) -> str:
        return self.__variabilityType

    @variabilityType.setter
    def variabilityType(self, variabilityType: str):
        self.__variabilityType = variabilityType

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
    def featureModelMetamodel_Feature19(self):
        return self.__featureModelMetamodel_Feature19

    @featureModelMetamodel_Feature19.setter
    def featureModelMetamodel_Feature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Feature__featureModelMetamodel_Feature19", None)
        self.__featureModelMetamodel_Feature19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_GroupMultiplicity18"):
                opp_val = getattr(old_value, "featureModelMetamodel_GroupMultiplicity18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_GroupMultiplicity18"):
                opp_val = getattr(value, "featureModelMetamodel_GroupMultiplicity18", None)
                if opp_val is None:
                    setattr(value, "featureModelMetamodel_GroupMultiplicity18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModelMetamodel_Feature6(self):
        return self.__featureModelMetamodel_Feature6

    @featureModelMetamodel_Feature6.setter
    def featureModelMetamodel_Feature6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Feature__featureModelMetamodel_Feature6", None)
        self.__featureModelMetamodel_Feature6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_Feature8"):
                opp_val = getattr(old_value, "featureModelMetamodel_Feature8", None)
                if opp_val == self:
                    setattr(old_value, "featureModelMetamodel_Feature8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_Feature8"):
                opp_val = getattr(value, "featureModelMetamodel_Feature8", None)
                setattr(value, "featureModelMetamodel_Feature8", self)

    @property
    def featureModelMetamodel_Feature(self):
        return self.__featureModelMetamodel_Feature

    @featureModelMetamodel_Feature.setter
    def featureModelMetamodel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Feature__featureModelMetamodel_Feature", None)
        self.__featureModelMetamodel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_Feature0"):
                opp_val = getattr(old_value, "featureModelMetamodel_Feature0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_Feature0"):
                opp_val = getattr(value, "featureModelMetamodel_Feature0", None)
                if opp_val is None:
                    setattr(value, "featureModelMetamodel_Feature0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModelMetamodel_Feature3(self):
        return self.__featureModelMetamodel_Feature3

    @featureModelMetamodel_Feature3.setter
    def featureModelMetamodel_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Feature__featureModelMetamodel_Feature3", None)
        self.__featureModelMetamodel_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_GroupMultiplicity"):
                opp_val = getattr(old_value, "featureModelMetamodel_GroupMultiplicity", None)
                if opp_val == self:
                    setattr(old_value, "featureModelMetamodel_GroupMultiplicity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_GroupMultiplicity"):
                opp_val = getattr(value, "featureModelMetamodel_GroupMultiplicity", None)
                setattr(value, "featureModelMetamodel_GroupMultiplicity", self)

    @property
    def featureModelMetamodel_Feature11(self):
        return self.__featureModelMetamodel_Feature11

    @featureModelMetamodel_Feature11.setter
    def featureModelMetamodel_Feature11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Feature__featureModelMetamodel_Feature11", None)
        self.__featureModelMetamodel_Feature11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_FeatureModel"):
                opp_val = getattr(old_value, "featureModelMetamodel_FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "featureModelMetamodel_FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_FeatureModel"):
                opp_val = getattr(value, "featureModelMetamodel_FeatureModel", None)
                setattr(value, "featureModelMetamodel_FeatureModel", self)

    @property
    def featureModelMetamodel_Feature8(self):
        return self.__featureModelMetamodel_Feature8

    @featureModelMetamodel_Feature8.setter
    def featureModelMetamodel_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Feature__featureModelMetamodel_Feature8", None)
        self.__featureModelMetamodel_Feature8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_Feature6"):
                opp_val = getattr(old_value, "featureModelMetamodel_Feature6", None)
                if opp_val == self:
                    setattr(old_value, "featureModelMetamodel_Feature6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_Feature6"):
                opp_val = getattr(value, "featureModelMetamodel_Feature6", None)
                setattr(value, "featureModelMetamodel_Feature6", self)

    @property
    def featureModelMetamodel_Feature16(self):
        return self.__featureModelMetamodel_Feature16

    @featureModelMetamodel_Feature16.setter
    def featureModelMetamodel_Feature16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Feature__featureModelMetamodel_Feature16", None)
        self.__featureModelMetamodel_Feature16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_FeatureModel15"):
                opp_val = getattr(old_value, "featureModelMetamodel_FeatureModel15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_FeatureModel15"):
                opp_val = getattr(value, "featureModelMetamodel_FeatureModel15", None)
                if opp_val is None:
                    setattr(value, "featureModelMetamodel_FeatureModel15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def featureModelMetamodel_Feature0(self):
        return self.__featureModelMetamodel_Feature0

    @featureModelMetamodel_Feature0.setter
    def featureModelMetamodel_Feature0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Feature__featureModelMetamodel_Feature0", None)
        self.__featureModelMetamodel_Feature0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModelMetamodel_Feature"):
                    opp_val = getattr(item, "featureModelMetamodel_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModelMetamodel_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModelMetamodel_Feature"):
                    opp_val = getattr(item, "featureModelMetamodel_Feature", None)
                    
                    setattr(item, "featureModelMetamodel_Feature", self)
                    

    @property
    def featureModelMetamodel_Feature21(self):
        return self.__featureModelMetamodel_Feature21

    @featureModelMetamodel_Feature21.setter
    def featureModelMetamodel_Feature21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Feature__featureModelMetamodel_Feature21", None)
        self.__featureModelMetamodel_Feature21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "featureModelMetamodel_Selection"):
                opp_val = getattr(old_value, "featureModelMetamodel_Selection", None)
                if opp_val == self:
                    setattr(old_value, "featureModelMetamodel_Selection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "featureModelMetamodel_Selection"):
                opp_val = getattr(value, "featureModelMetamodel_Selection", None)
                setattr(value, "featureModelMetamodel_Selection", self)

    @property
    def featureModelMetamodel_Feature5(self):
        return self.__featureModelMetamodel_Feature5

    @featureModelMetamodel_Feature5.setter
    def featureModelMetamodel_Feature5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_featureModelMetamodel_Feature__featureModelMetamodel_Feature5", None)
        self.__featureModelMetamodel_Feature5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "featureModelMetamodel_Attribute"):
                    opp_val = getattr(item, "featureModelMetamodel_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "featureModelMetamodel_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "featureModelMetamodel_Attribute"):
                    opp_val = getattr(item, "featureModelMetamodel_Attribute", None)
                    
                    setattr(item, "featureModelMetamodel_Attribute", self)
                    
