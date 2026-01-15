from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class afmmm_EClass0:

    pass
class Relation:

    pass
class afmmm_XOr(Relation):

    pass
class afmmm_Or(Relation):

    pass
class afmmm_Optional(Relation):

    pass
class afmmm_Mutex(Relation):

    pass
class afmmm_Mandatory(Relation):

    pass
class afmmm_AttributedFeatureModel:

    pass
class Domain:

    pass
class afmmm_Enum(Domain):

    def __init__(self, literals: str):
        self.literals = literals
        
    @property
    def literals(self) -> str:
        return self.__literals

    @literals.setter
    def literals(self, literals: str):
        self.__literals = literals

class afmmm_Real(Domain):

    pass
class afmmm_Integer(Domain):

    pass
class afmmm_Boolean(Domain):

    pass
class afmmm_Domain(ABC):

    pass
class afmmm_Feature:

    def __init__(self, name: str, afmmm_Feature3: "afmmm_AttributedFeatureDiagram" = None, afmmm_Feature9: set["afmmm_Attribute"] = None, afmmm_Feature: "afmmm_AttributedFeatureDiagram" = None, afmmm_Feature12: "afmmm_Relation" = None, afmmm_Feature15: "afmmm_Relation" = None):
        self.name = name
        self.afmmm_Feature3 = afmmm_Feature3
        self.afmmm_Feature9 = afmmm_Feature9 if afmmm_Feature9 is not None else set()
        self.afmmm_Feature = afmmm_Feature
        self.afmmm_Feature12 = afmmm_Feature12
        self.afmmm_Feature15 = afmmm_Feature15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def afmmm_Feature15(self):
        return self.__afmmm_Feature15

    @afmmm_Feature15.setter
    def afmmm_Feature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afmmm_Feature__afmmm_Feature15", None)
        self.__afmmm_Feature15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afmmm_Relation14"):
                opp_val = getattr(old_value, "afmmm_Relation14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afmmm_Relation14"):
                opp_val = getattr(value, "afmmm_Relation14", None)
                if opp_val is None:
                    setattr(value, "afmmm_Relation14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def afmmm_Feature9(self):
        return self.__afmmm_Feature9

    @afmmm_Feature9.setter
    def afmmm_Feature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afmmm_Feature__afmmm_Feature9", None)
        self.__afmmm_Feature9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afmmm_Attribute"):
                    opp_val = getattr(item, "afmmm_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "afmmm_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afmmm_Attribute"):
                    opp_val = getattr(item, "afmmm_Attribute", None)
                    
                    setattr(item, "afmmm_Attribute", self)
                    

    @property
    def afmmm_Feature3(self):
        return self.__afmmm_Feature3

    @afmmm_Feature3.setter
    def afmmm_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afmmm_Feature__afmmm_Feature3", None)
        self.__afmmm_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afmmm_AttributedFeatureDiagram2"):
                opp_val = getattr(old_value, "afmmm_AttributedFeatureDiagram2", None)
                if opp_val == self:
                    setattr(old_value, "afmmm_AttributedFeatureDiagram2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afmmm_AttributedFeatureDiagram2"):
                opp_val = getattr(value, "afmmm_AttributedFeatureDiagram2", None)
                setattr(value, "afmmm_AttributedFeatureDiagram2", self)

    @property
    def afmmm_Feature12(self):
        return self.__afmmm_Feature12

    @afmmm_Feature12.setter
    def afmmm_Feature12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afmmm_Feature__afmmm_Feature12", None)
        self.__afmmm_Feature12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afmmm_Relation11"):
                opp_val = getattr(old_value, "afmmm_Relation11", None)
                if opp_val == self:
                    setattr(old_value, "afmmm_Relation11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afmmm_Relation11"):
                opp_val = getattr(value, "afmmm_Relation11", None)
                setattr(value, "afmmm_Relation11", self)

    @property
    def afmmm_Feature(self):
        return self.__afmmm_Feature

    @afmmm_Feature.setter
    def afmmm_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afmmm_Feature__afmmm_Feature", None)
        self.__afmmm_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afmmm_AttributedFeatureDiagram"):
                opp_val = getattr(old_value, "afmmm_AttributedFeatureDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afmmm_AttributedFeatureDiagram"):
                opp_val = getattr(value, "afmmm_AttributedFeatureDiagram", None)
                if opp_val is None:
                    setattr(value, "afmmm_AttributedFeatureDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afmmm_AttributedFeatureDiagram:

    pass
class afmmm_Attribute:

    def __init__(self, name: str, afmmm_Attribute: "afmmm_Feature" = None, afmmm_Attribute24: "afmmm_Domain" = None):
        self.name = name
        self.afmmm_Attribute = afmmm_Attribute
        self.afmmm_Attribute24 = afmmm_Attribute24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def afmmm_Attribute24(self):
        return self.__afmmm_Attribute24

    @afmmm_Attribute24.setter
    def afmmm_Attribute24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afmmm_Attribute__afmmm_Attribute24", None)
        self.__afmmm_Attribute24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afmmm_Domain25"):
                opp_val = getattr(old_value, "afmmm_Domain25", None)
                if opp_val == self:
                    setattr(old_value, "afmmm_Domain25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afmmm_Domain25"):
                opp_val = getattr(value, "afmmm_Domain25", None)
                setattr(value, "afmmm_Domain25", self)

    @property
    def afmmm_Attribute(self):
        return self.__afmmm_Attribute

    @afmmm_Attribute.setter
    def afmmm_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_afmmm_Attribute__afmmm_Attribute", None)
        self.__afmmm_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "afmmm_Feature9"):
                opp_val = getattr(old_value, "afmmm_Feature9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "afmmm_Feature9"):
                opp_val = getattr(value, "afmmm_Feature9", None)
                if opp_val is None:
                    setattr(value, "afmmm_Feature9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class afmmm_Relation(ABC):

    pass
class afmmm_CrossTreeConstraint:

    pass