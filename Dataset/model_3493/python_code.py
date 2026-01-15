from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class features_modeling_NOT:

    pass
class features_modeling_AND:

    pass
class features_modeling_Group(ABC):

    pass
class features_modeling_Constraint(ABC):

    pass
class Constraint:

    pass
class features_modeling_EX(Constraint):

    pass
class features_modeling_I(Constraint):

    pass
class features_modeling_PropositionOR:

    pass
class features_modeling_PropFormulaCNF:

    pass
class features_modeling_Constraints:

    pass
class features_modeling_Edge:

    pass
class Group:

    pass
class features_modeling_GOR(Group):

    pass
class features_modeling_GXOR(Group):

    pass
class E:

    pass
class features_modeling_EMAND(E):

    pass
class features_modeling_E:

    pass
class features_modeling_G:

    pass
class features_modeling_F:

    pass
class features_modeling_Feature:

    def __init__(self, ID: str, features_modeling_Feature: "features_modeling_Feature" = None, features_modeling_Feature1: set["features_modeling_Feature"] = None, features_modeling_Feature4: "features_modeling_F" = None, features_modeling_Feature9: "features_modeling_Edge" = None, features_modeling_Feature15: "features_modeling_Group" = None, features_modeling_Feature13: "features_modeling_Constraint" = None, features_modeling_Feature21: "features_modeling_PropositionOR" = None, features_modeling_Feature26: "features_modeling_NOT" = None):
        self.ID = ID
        self.features_modeling_Feature = features_modeling_Feature
        self.features_modeling_Feature1 = features_modeling_Feature1 if features_modeling_Feature1 is not None else set()
        self.features_modeling_Feature4 = features_modeling_Feature4
        self.features_modeling_Feature9 = features_modeling_Feature9
        self.features_modeling_Feature15 = features_modeling_Feature15
        self.features_modeling_Feature13 = features_modeling_Feature13
        self.features_modeling_Feature21 = features_modeling_Feature21
        self.features_modeling_Feature26 = features_modeling_Feature26
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def features_modeling_Feature9(self):
        return self.__features_modeling_Feature9

    @features_modeling_Feature9.setter
    def features_modeling_Feature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_modeling_Feature__features_modeling_Feature9", None)
        self.__features_modeling_Feature9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_modeling_Edge"):
                opp_val = getattr(old_value, "features_modeling_Edge", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_modeling_Edge"):
                opp_val = getattr(value, "features_modeling_Edge", None)
                if opp_val is None:
                    setattr(value, "features_modeling_Edge", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features_modeling_Feature15(self):
        return self.__features_modeling_Feature15

    @features_modeling_Feature15.setter
    def features_modeling_Feature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_modeling_Feature__features_modeling_Feature15", None)
        self.__features_modeling_Feature15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_modeling_Group"):
                opp_val = getattr(old_value, "features_modeling_Group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_modeling_Group"):
                opp_val = getattr(value, "features_modeling_Group", None)
                if opp_val is None:
                    setattr(value, "features_modeling_Group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features_modeling_Feature1(self):
        return self.__features_modeling_Feature1

    @features_modeling_Feature1.setter
    def features_modeling_Feature1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_modeling_Feature__features_modeling_Feature1", None)
        self.__features_modeling_Feature1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "features_modeling_Feature"):
                    opp_val = getattr(item, "features_modeling_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "features_modeling_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "features_modeling_Feature"):
                    opp_val = getattr(item, "features_modeling_Feature", None)
                    
                    setattr(item, "features_modeling_Feature", self)
                    

    @property
    def features_modeling_Feature4(self):
        return self.__features_modeling_Feature4

    @features_modeling_Feature4.setter
    def features_modeling_Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_modeling_Feature__features_modeling_Feature4", None)
        self.__features_modeling_Feature4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_modeling_F"):
                opp_val = getattr(old_value, "features_modeling_F", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_modeling_F"):
                opp_val = getattr(value, "features_modeling_F", None)
                if opp_val is None:
                    setattr(value, "features_modeling_F", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features_modeling_Feature(self):
        return self.__features_modeling_Feature

    @features_modeling_Feature.setter
    def features_modeling_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_modeling_Feature__features_modeling_Feature", None)
        self.__features_modeling_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_modeling_Feature1"):
                opp_val = getattr(old_value, "features_modeling_Feature1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_modeling_Feature1"):
                opp_val = getattr(value, "features_modeling_Feature1", None)
                if opp_val is None:
                    setattr(value, "features_modeling_Feature1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features_modeling_Feature13(self):
        return self.__features_modeling_Feature13

    @features_modeling_Feature13.setter
    def features_modeling_Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_modeling_Feature__features_modeling_Feature13", None)
        self.__features_modeling_Feature13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_modeling_Constraint"):
                opp_val = getattr(old_value, "features_modeling_Constraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_modeling_Constraint"):
                opp_val = getattr(value, "features_modeling_Constraint", None)
                if opp_val is None:
                    setattr(value, "features_modeling_Constraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features_modeling_Feature21(self):
        return self.__features_modeling_Feature21

    @features_modeling_Feature21.setter
    def features_modeling_Feature21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_modeling_Feature__features_modeling_Feature21", None)
        self.__features_modeling_Feature21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_modeling_PropositionOR20"):
                opp_val = getattr(old_value, "features_modeling_PropositionOR20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_modeling_PropositionOR20"):
                opp_val = getattr(value, "features_modeling_PropositionOR20", None)
                if opp_val is None:
                    setattr(value, "features_modeling_PropositionOR20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features_modeling_Feature26(self):
        return self.__features_modeling_Feature26

    @features_modeling_Feature26.setter
    def features_modeling_Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_modeling_Feature__features_modeling_Feature26", None)
        self.__features_modeling_Feature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_modeling_NOT25"):
                opp_val = getattr(old_value, "features_modeling_NOT25", None)
                if opp_val == self:
                    setattr(old_value, "features_modeling_NOT25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_modeling_NOT25"):
                opp_val = getattr(value, "features_modeling_NOT25", None)
                setattr(value, "features_modeling_NOT25", self)

class Feature:

    pass
class features_modeling_R(Feature):

    pass