from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    PROTECTED = "PROTECTED"
    PACKAGE_PRIVATE = "PACKAGE_PRIVATE"


############################################
# Definition of Classes
############################################

class classmodel_Reference:

    pass
class classmodel_Array:

    pass
class classmodel_Multiplicity:

    def __init__(self, lower: str, upper: str, classmodel_Multiplicity30: "classmodel_Aggregation" = None, classmodel_Multiplicity33: "classmodel_Aggregation" = None, classmodel_Multiplicity35: "classmodel_Composition" = None, classmodel_Multiplicity38: "classmodel_Composition" = None, classmodel_Multiplicity: "classmodel_Association" = None, classmodel_Multiplicity28: "classmodel_Association" = None, classmodel_Multiplicity54: "classmodel_Array" = None):
        self.lower = lower
        self.upper = upper
        self.classmodel_Multiplicity30 = classmodel_Multiplicity30
        self.classmodel_Multiplicity33 = classmodel_Multiplicity33
        self.classmodel_Multiplicity35 = classmodel_Multiplicity35
        self.classmodel_Multiplicity38 = classmodel_Multiplicity38
        self.classmodel_Multiplicity = classmodel_Multiplicity
        self.classmodel_Multiplicity28 = classmodel_Multiplicity28
        self.classmodel_Multiplicity54 = classmodel_Multiplicity54
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def classmodel_Multiplicity38(self):
        return self.__classmodel_Multiplicity38

    @classmodel_Multiplicity38.setter
    def classmodel_Multiplicity38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Multiplicity__classmodel_Multiplicity38", None)
        self.__classmodel_Multiplicity38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Composition37"):
                opp_val = getattr(old_value, "classmodel_Composition37", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Composition37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Composition37"):
                opp_val = getattr(value, "classmodel_Composition37", None)
                setattr(value, "classmodel_Composition37", self)

    @property
    def classmodel_Multiplicity54(self):
        return self.__classmodel_Multiplicity54

    @classmodel_Multiplicity54.setter
    def classmodel_Multiplicity54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Multiplicity__classmodel_Multiplicity54", None)
        self.__classmodel_Multiplicity54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Array53"):
                opp_val = getattr(old_value, "classmodel_Array53", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Array53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Array53"):
                opp_val = getattr(value, "classmodel_Array53", None)
                setattr(value, "classmodel_Array53", self)

    @property
    def classmodel_Multiplicity(self):
        return self.__classmodel_Multiplicity

    @classmodel_Multiplicity.setter
    def classmodel_Multiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Multiplicity__classmodel_Multiplicity", None)
        self.__classmodel_Multiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Association"):
                opp_val = getattr(old_value, "classmodel_Association", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Association"):
                opp_val = getattr(value, "classmodel_Association", None)
                setattr(value, "classmodel_Association", self)

    @property
    def classmodel_Multiplicity33(self):
        return self.__classmodel_Multiplicity33

    @classmodel_Multiplicity33.setter
    def classmodel_Multiplicity33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Multiplicity__classmodel_Multiplicity33", None)
        self.__classmodel_Multiplicity33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Aggregation32"):
                opp_val = getattr(old_value, "classmodel_Aggregation32", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Aggregation32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Aggregation32"):
                opp_val = getattr(value, "classmodel_Aggregation32", None)
                setattr(value, "classmodel_Aggregation32", self)

    @property
    def classmodel_Multiplicity28(self):
        return self.__classmodel_Multiplicity28

    @classmodel_Multiplicity28.setter
    def classmodel_Multiplicity28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Multiplicity__classmodel_Multiplicity28", None)
        self.__classmodel_Multiplicity28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Association27"):
                opp_val = getattr(old_value, "classmodel_Association27", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Association27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Association27"):
                opp_val = getattr(value, "classmodel_Association27", None)
                setattr(value, "classmodel_Association27", self)

    @property
    def classmodel_Multiplicity35(self):
        return self.__classmodel_Multiplicity35

    @classmodel_Multiplicity35.setter
    def classmodel_Multiplicity35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Multiplicity__classmodel_Multiplicity35", None)
        self.__classmodel_Multiplicity35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Composition"):
                opp_val = getattr(old_value, "classmodel_Composition", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Composition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Composition"):
                opp_val = getattr(value, "classmodel_Composition", None)
                setattr(value, "classmodel_Composition", self)

    @property
    def classmodel_Multiplicity30(self):
        return self.__classmodel_Multiplicity30

    @classmodel_Multiplicity30.setter
    def classmodel_Multiplicity30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Multiplicity__classmodel_Multiplicity30", None)
        self.__classmodel_Multiplicity30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Aggregation"):
                opp_val = getattr(old_value, "classmodel_Aggregation", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Aggregation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Aggregation"):
                opp_val = getattr(value, "classmodel_Aggregation", None)
                setattr(value, "classmodel_Aggregation", self)

class classmodel_Parameter:

    def __init__(self, name: str, implicit: str, classmodel_Parameter: "classmodel_Operation" = None, classmodel_Parameter43: "classmodel_Reference" = None):
        self.name = name
        self.implicit = implicit
        self.classmodel_Parameter = classmodel_Parameter
        self.classmodel_Parameter43 = classmodel_Parameter43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def implicit(self) -> str:
        return self.__implicit

    @implicit.setter
    def implicit(self, implicit: str):
        self.__implicit = implicit

    @property
    def classmodel_Parameter43(self):
        return self.__classmodel_Parameter43

    @classmodel_Parameter43.setter
    def classmodel_Parameter43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Parameter__classmodel_Parameter43", None)
        self.__classmodel_Parameter43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Reference44"):
                opp_val = getattr(old_value, "classmodel_Reference44", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Reference44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Reference44"):
                opp_val = getattr(value, "classmodel_Reference44", None)
                setattr(value, "classmodel_Reference44", self)

    @property
    def classmodel_Parameter(self):
        return self.__classmodel_Parameter

    @classmodel_Parameter.setter
    def classmodel_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Parameter__classmodel_Parameter", None)
        self.__classmodel_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Operation"):
                opp_val = getattr(old_value, "classmodel_Operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Operation"):
                opp_val = getattr(value, "classmodel_Operation", None)
                if opp_val is None:
                    setattr(value, "classmodel_Operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Feature:

    pass
class classmodel_Attribute(Feature):

    def __init__(self, implicit: str, static: bool, classmodel_Attribute: "classmodel_Reference" = None):
        self.implicit = implicit
        self.static = static
        self.classmodel_Attribute = classmodel_Attribute
        
    @property
    def implicit(self) -> str:
        return self.__implicit

    @implicit.setter
    def implicit(self, implicit: str):
        self.__implicit = implicit

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def classmodel_Attribute(self):
        return self.__classmodel_Attribute

    @classmodel_Attribute.setter
    def classmodel_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Attribute__classmodel_Attribute", None)
        self.__classmodel_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Reference46"):
                opp_val = getattr(old_value, "classmodel_Reference46", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Reference46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Reference46"):
                opp_val = getattr(value, "classmodel_Reference46", None)
                setattr(value, "classmodel_Reference46", self)

class classmodel_Operation(Feature):

    def __init__(self, static: bool, body: str, classmodel_Operation: set["classmodel_Parameter"] = None, classmodel_Operation41: "classmodel_Reference" = None):
        self.static = static
        self.body = body
        self.classmodel_Operation = classmodel_Operation if classmodel_Operation is not None else set()
        self.classmodel_Operation41 = classmodel_Operation41
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def classmodel_Operation41(self):
        return self.__classmodel_Operation41

    @classmodel_Operation41.setter
    def classmodel_Operation41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Operation__classmodel_Operation41", None)
        self.__classmodel_Operation41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Reference"):
                opp_val = getattr(old_value, "classmodel_Reference", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Reference"):
                opp_val = getattr(value, "classmodel_Reference", None)
                setattr(value, "classmodel_Reference", self)

    @property
    def classmodel_Operation(self):
        return self.__classmodel_Operation

    @classmodel_Operation.setter
    def classmodel_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Operation__classmodel_Operation", None)
        self.__classmodel_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classmodel_Parameter"):
                    opp_val = getattr(item, "classmodel_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "classmodel_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classmodel_Parameter"):
                    opp_val = getattr(item, "classmodel_Parameter", None)
                    
                    setattr(item, "classmodel_Parameter", self)
                    

class classmodel_Constant(Feature):

    pass
class Relationship:

    pass
class classmodel_Dependency(Relationship):

    pass
class classmodel_Realization(Relationship):

    pass
class classmodel_Generalization(Relationship):

    pass
class classmodel_Composition(Relationship):

    def __init__(self, headNavigable: bool, headVisibility: str, headLabel: str, tailNavigable: bool, tailVisibility: str, tailLabel: str, classmodel_Composition: "classmodel_Multiplicity" = None, classmodel_Composition37: "classmodel_Multiplicity" = None):
        self.headNavigable = headNavigable
        self.headVisibility = headVisibility
        self.headLabel = headLabel
        self.tailNavigable = tailNavigable
        self.tailVisibility = tailVisibility
        self.tailLabel = tailLabel
        self.classmodel_Composition = classmodel_Composition
        self.classmodel_Composition37 = classmodel_Composition37
        
    @property
    def headNavigable(self) -> bool:
        return self.__headNavigable

    @headNavigable.setter
    def headNavigable(self, headNavigable: bool):
        self.__headNavigable = headNavigable

    @property
    def tailLabel(self) -> str:
        return self.__tailLabel

    @tailLabel.setter
    def tailLabel(self, tailLabel: str):
        self.__tailLabel = tailLabel

    @property
    def headVisibility(self) -> str:
        return self.__headVisibility

    @headVisibility.setter
    def headVisibility(self, headVisibility: str):
        self.__headVisibility = headVisibility

    @property
    def tailVisibility(self) -> str:
        return self.__tailVisibility

    @tailVisibility.setter
    def tailVisibility(self, tailVisibility: str):
        self.__tailVisibility = tailVisibility

    @property
    def headLabel(self) -> str:
        return self.__headLabel

    @headLabel.setter
    def headLabel(self, headLabel: str):
        self.__headLabel = headLabel

    @property
    def tailNavigable(self) -> bool:
        return self.__tailNavigable

    @tailNavigable.setter
    def tailNavigable(self, tailNavigable: bool):
        self.__tailNavigable = tailNavigable

    @property
    def classmodel_Composition(self):
        return self.__classmodel_Composition

    @classmodel_Composition.setter
    def classmodel_Composition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Composition__classmodel_Composition", None)
        self.__classmodel_Composition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Multiplicity35"):
                opp_val = getattr(old_value, "classmodel_Multiplicity35", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Multiplicity35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Multiplicity35"):
                opp_val = getattr(value, "classmodel_Multiplicity35", None)
                setattr(value, "classmodel_Multiplicity35", self)

    @property
    def classmodel_Composition37(self):
        return self.__classmodel_Composition37

    @classmodel_Composition37.setter
    def classmodel_Composition37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Composition__classmodel_Composition37", None)
        self.__classmodel_Composition37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Multiplicity38"):
                opp_val = getattr(old_value, "classmodel_Multiplicity38", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Multiplicity38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Multiplicity38"):
                opp_val = getattr(value, "classmodel_Multiplicity38", None)
                setattr(value, "classmodel_Multiplicity38", self)

class classmodel_Aggregation(Relationship):

    def __init__(self, headLabel: str, tailNavigable: bool, tailVisibility: str, tailLabel: str, headNavigable: bool, headVisibility: str, classmodel_Aggregation: "classmodel_Multiplicity" = None, classmodel_Aggregation32: "classmodel_Multiplicity" = None):
        self.headLabel = headLabel
        self.tailNavigable = tailNavigable
        self.tailVisibility = tailVisibility
        self.tailLabel = tailLabel
        self.headNavigable = headNavigable
        self.headVisibility = headVisibility
        self.classmodel_Aggregation = classmodel_Aggregation
        self.classmodel_Aggregation32 = classmodel_Aggregation32
        
    @property
    def headVisibility(self) -> str:
        return self.__headVisibility

    @headVisibility.setter
    def headVisibility(self, headVisibility: str):
        self.__headVisibility = headVisibility

    @property
    def tailVisibility(self) -> str:
        return self.__tailVisibility

    @tailVisibility.setter
    def tailVisibility(self, tailVisibility: str):
        self.__tailVisibility = tailVisibility

    @property
    def headLabel(self) -> str:
        return self.__headLabel

    @headLabel.setter
    def headLabel(self, headLabel: str):
        self.__headLabel = headLabel

    @property
    def headNavigable(self) -> bool:
        return self.__headNavigable

    @headNavigable.setter
    def headNavigable(self, headNavigable: bool):
        self.__headNavigable = headNavigable

    @property
    def tailLabel(self) -> str:
        return self.__tailLabel

    @tailLabel.setter
    def tailLabel(self, tailLabel: str):
        self.__tailLabel = tailLabel

    @property
    def tailNavigable(self) -> bool:
        return self.__tailNavigable

    @tailNavigable.setter
    def tailNavigable(self, tailNavigable: bool):
        self.__tailNavigable = tailNavigable

    @property
    def classmodel_Aggregation(self):
        return self.__classmodel_Aggregation

    @classmodel_Aggregation.setter
    def classmodel_Aggregation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Aggregation__classmodel_Aggregation", None)
        self.__classmodel_Aggregation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Multiplicity30"):
                opp_val = getattr(old_value, "classmodel_Multiplicity30", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Multiplicity30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Multiplicity30"):
                opp_val = getattr(value, "classmodel_Multiplicity30", None)
                setattr(value, "classmodel_Multiplicity30", self)

    @property
    def classmodel_Aggregation32(self):
        return self.__classmodel_Aggregation32

    @classmodel_Aggregation32.setter
    def classmodel_Aggregation32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Aggregation__classmodel_Aggregation32", None)
        self.__classmodel_Aggregation32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Multiplicity33"):
                opp_val = getattr(old_value, "classmodel_Multiplicity33", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Multiplicity33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Multiplicity33"):
                opp_val = getattr(value, "classmodel_Multiplicity33", None)
                setattr(value, "classmodel_Multiplicity33", self)

class classmodel_Association(Relationship):

    def __init__(self, headNavigable: bool, headVisibility: str, headLabel: str, tailNavigable: bool, tailVisibility: str, tailLabel: str, classmodel_Association: "classmodel_Multiplicity" = None, classmodel_Association27: "classmodel_Multiplicity" = None):
        self.headNavigable = headNavigable
        self.headVisibility = headVisibility
        self.headLabel = headLabel
        self.tailNavigable = tailNavigable
        self.tailVisibility = tailVisibility
        self.tailLabel = tailLabel
        self.classmodel_Association = classmodel_Association
        self.classmodel_Association27 = classmodel_Association27
        
    @property
    def tailVisibility(self) -> str:
        return self.__tailVisibility

    @tailVisibility.setter
    def tailVisibility(self, tailVisibility: str):
        self.__tailVisibility = tailVisibility

    @property
    def tailNavigable(self) -> bool:
        return self.__tailNavigable

    @tailNavigable.setter
    def tailNavigable(self, tailNavigable: bool):
        self.__tailNavigable = tailNavigable

    @property
    def headNavigable(self) -> bool:
        return self.__headNavigable

    @headNavigable.setter
    def headNavigable(self, headNavigable: bool):
        self.__headNavigable = headNavigable

    @property
    def headVisibility(self) -> str:
        return self.__headVisibility

    @headVisibility.setter
    def headVisibility(self, headVisibility: str):
        self.__headVisibility = headVisibility

    @property
    def headLabel(self) -> str:
        return self.__headLabel

    @headLabel.setter
    def headLabel(self, headLabel: str):
        self.__headLabel = headLabel

    @property
    def tailLabel(self) -> str:
        return self.__tailLabel

    @tailLabel.setter
    def tailLabel(self, tailLabel: str):
        self.__tailLabel = tailLabel

    @property
    def classmodel_Association27(self):
        return self.__classmodel_Association27

    @classmodel_Association27.setter
    def classmodel_Association27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Association__classmodel_Association27", None)
        self.__classmodel_Association27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Multiplicity28"):
                opp_val = getattr(old_value, "classmodel_Multiplicity28", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Multiplicity28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Multiplicity28"):
                opp_val = getattr(value, "classmodel_Multiplicity28", None)
                setattr(value, "classmodel_Multiplicity28", self)

    @property
    def classmodel_Association(self):
        return self.__classmodel_Association

    @classmodel_Association.setter
    def classmodel_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Association__classmodel_Association", None)
        self.__classmodel_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Multiplicity"):
                opp_val = getattr(old_value, "classmodel_Multiplicity", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Multiplicity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Multiplicity"):
                opp_val = getattr(value, "classmodel_Multiplicity", None)
                setattr(value, "classmodel_Multiplicity", self)

class classmodel_Type:

    def __init__(self, visibility: str, classmodel_Type14: "classmodel_Entity" = None, classmodel_Type: "classmodel_Classifier" = None, classmodel_Type10: "classmodel_Classifier" = None, classmodel_Type16: "classmodel_Enumeration" = None):
        self.visibility = visibility
        self.classmodel_Type14 = classmodel_Type14
        self.classmodel_Type = classmodel_Type
        self.classmodel_Type10 = classmodel_Type10
        self.classmodel_Type16 = classmodel_Type16
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def classmodel_Type10(self):
        return self.__classmodel_Type10

    @classmodel_Type10.setter
    def classmodel_Type10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Type__classmodel_Type10", None)
        self.__classmodel_Type10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Classifier9"):
                opp_val = getattr(old_value, "classmodel_Classifier9", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Classifier9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Classifier9"):
                opp_val = getattr(value, "classmodel_Classifier9", None)
                setattr(value, "classmodel_Classifier9", self)

    @property
    def classmodel_Type16(self):
        return self.__classmodel_Type16

    @classmodel_Type16.setter
    def classmodel_Type16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Type__classmodel_Type16", None)
        self.__classmodel_Type16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Enumeration"):
                opp_val = getattr(old_value, "classmodel_Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Enumeration"):
                opp_val = getattr(value, "classmodel_Enumeration", None)
                setattr(value, "classmodel_Enumeration", self)

    @property
    def classmodel_Type(self):
        return self.__classmodel_Type

    @classmodel_Type.setter
    def classmodel_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Type__classmodel_Type", None)
        self.__classmodel_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Classifier"):
                opp_val = getattr(old_value, "classmodel_Classifier", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Classifier"):
                opp_val = getattr(value, "classmodel_Classifier", None)
                if opp_val is None:
                    setattr(value, "classmodel_Classifier", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classmodel_Type14(self):
        return self.__classmodel_Type14

    @classmodel_Type14.setter
    def classmodel_Type14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Type__classmodel_Type14", None)
        self.__classmodel_Type14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Entity"):
                opp_val = getattr(old_value, "classmodel_Entity", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Entity"):
                opp_val = getattr(value, "classmodel_Entity", None)
                setattr(value, "classmodel_Entity", self)

class Entity:

    pass
class classmodel_Classifier(Entity):

    def __init__(self, constraint: str, classmodel_Classifier9: "classmodel_Type" = None, classmodel_Classifier12: set["classmodel_Feature"] = None, classmodel_Classifier: set["classmodel_Type"] = None):
        self.constraint = constraint
        self.classmodel_Classifier9 = classmodel_Classifier9
        self.classmodel_Classifier12 = classmodel_Classifier12 if classmodel_Classifier12 is not None else set()
        self.classmodel_Classifier = classmodel_Classifier if classmodel_Classifier is not None else set()
        
    @property
    def constraint(self) -> str:
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint: str):
        self.__constraint = constraint

    @property
    def classmodel_Classifier12(self):
        return self.__classmodel_Classifier12

    @classmodel_Classifier12.setter
    def classmodel_Classifier12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Classifier__classmodel_Classifier12", None)
        self.__classmodel_Classifier12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classmodel_Feature"):
                    opp_val = getattr(item, "classmodel_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "classmodel_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classmodel_Feature"):
                    opp_val = getattr(item, "classmodel_Feature", None)
                    
                    setattr(item, "classmodel_Feature", self)
                    

    @property
    def classmodel_Classifier(self):
        return self.__classmodel_Classifier

    @classmodel_Classifier.setter
    def classmodel_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Classifier__classmodel_Classifier", None)
        self.__classmodel_Classifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classmodel_Type"):
                    opp_val = getattr(item, "classmodel_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "classmodel_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classmodel_Type"):
                    opp_val = getattr(item, "classmodel_Type", None)
                    
                    setattr(item, "classmodel_Type", self)
                    

    @property
    def classmodel_Classifier9(self):
        return self.__classmodel_Classifier9

    @classmodel_Classifier9.setter
    def classmodel_Classifier9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Classifier__classmodel_Classifier9", None)
        self.__classmodel_Classifier9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Type10"):
                opp_val = getattr(old_value, "classmodel_Type10", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Type10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Type10"):
                opp_val = getattr(value, "classmodel_Type10", None)
                setattr(value, "classmodel_Type10", self)

class classmodel_Enumeration(Entity):

    def __init__(self, constraint: str, classmodel_Enumeration: "classmodel_Type" = None, classmodel_Enumeration18: set["classmodel_Feature"] = None):
        self.constraint = constraint
        self.classmodel_Enumeration = classmodel_Enumeration
        self.classmodel_Enumeration18 = classmodel_Enumeration18 if classmodel_Enumeration18 is not None else set()
        
    @property
    def constraint(self) -> str:
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint: str):
        self.__constraint = constraint

    @property
    def classmodel_Enumeration(self):
        return self.__classmodel_Enumeration

    @classmodel_Enumeration.setter
    def classmodel_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Enumeration__classmodel_Enumeration", None)
        self.__classmodel_Enumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Type16"):
                opp_val = getattr(old_value, "classmodel_Type16", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Type16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Type16"):
                opp_val = getattr(value, "classmodel_Type16", None)
                setattr(value, "classmodel_Type16", self)

    @property
    def classmodel_Enumeration18(self):
        return self.__classmodel_Enumeration18

    @classmodel_Enumeration18.setter
    def classmodel_Enumeration18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Enumeration__classmodel_Enumeration18", None)
        self.__classmodel_Enumeration18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classmodel_Feature19"):
                    opp_val = getattr(item, "classmodel_Feature19", None)
                    
                    if opp_val == self:
                        setattr(item, "classmodel_Feature19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classmodel_Feature19"):
                    opp_val = getattr(item, "classmodel_Feature19", None)
                    
                    setattr(item, "classmodel_Feature19", self)
                    

class classmodel_Datatype(Entity):

    pass
class Element:

    pass
class classmodel_Package(Element):

    def __init__(self, name: str, classmodel_Package: set["classmodel_Element"] = None):
        self.name = name
        self.classmodel_Package = classmodel_Package if classmodel_Package is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classmodel_Package(self):
        return self.__classmodel_Package

    @classmodel_Package.setter
    def classmodel_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Package__classmodel_Package", None)
        self.__classmodel_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classmodel_Element6"):
                    opp_val = getattr(item, "classmodel_Element6", None)
                    
                    if opp_val == self:
                        setattr(item, "classmodel_Element6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classmodel_Element6"):
                    opp_val = getattr(item, "classmodel_Element6", None)
                    
                    setattr(item, "classmodel_Element6", self)
                    

class classmodel_Relationship(Element):

    def __init__(self, label: str, classmodel_Relationship: "classmodel_Entity" = None, classmodel_Relationship23: "classmodel_Entity" = None):
        self.label = label
        self.classmodel_Relationship = classmodel_Relationship
        self.classmodel_Relationship23 = classmodel_Relationship23
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def classmodel_Relationship(self):
        return self.__classmodel_Relationship

    @classmodel_Relationship.setter
    def classmodel_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Relationship__classmodel_Relationship", None)
        self.__classmodel_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Entity21"):
                opp_val = getattr(old_value, "classmodel_Entity21", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Entity21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Entity21"):
                opp_val = getattr(value, "classmodel_Entity21", None)
                setattr(value, "classmodel_Entity21", self)

    @property
    def classmodel_Relationship23(self):
        return self.__classmodel_Relationship23

    @classmodel_Relationship23.setter
    def classmodel_Relationship23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Relationship__classmodel_Relationship23", None)
        self.__classmodel_Relationship23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Entity24"):
                opp_val = getattr(old_value, "classmodel_Entity24", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Entity24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Entity24"):
                opp_val = getattr(value, "classmodel_Entity24", None)
                setattr(value, "classmodel_Entity24", self)

class classmodel_Entity(Element):

    def __init__(self, name: str, classmodel_Entity: "classmodel_Type" = None, classmodel_Entity21: "classmodel_Relationship" = None, classmodel_Entity24: "classmodel_Relationship" = None, classmodel_Entity49: "classmodel_Reference" = None):
        self.name = name
        self.classmodel_Entity = classmodel_Entity
        self.classmodel_Entity21 = classmodel_Entity21
        self.classmodel_Entity24 = classmodel_Entity24
        self.classmodel_Entity49 = classmodel_Entity49
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classmodel_Entity24(self):
        return self.__classmodel_Entity24

    @classmodel_Entity24.setter
    def classmodel_Entity24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Entity__classmodel_Entity24", None)
        self.__classmodel_Entity24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Relationship23"):
                opp_val = getattr(old_value, "classmodel_Relationship23", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Relationship23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Relationship23"):
                opp_val = getattr(value, "classmodel_Relationship23", None)
                setattr(value, "classmodel_Relationship23", self)

    @property
    def classmodel_Entity(self):
        return self.__classmodel_Entity

    @classmodel_Entity.setter
    def classmodel_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Entity__classmodel_Entity", None)
        self.__classmodel_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Type14"):
                opp_val = getattr(old_value, "classmodel_Type14", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Type14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Type14"):
                opp_val = getattr(value, "classmodel_Type14", None)
                setattr(value, "classmodel_Type14", self)

    @property
    def classmodel_Entity49(self):
        return self.__classmodel_Entity49

    @classmodel_Entity49.setter
    def classmodel_Entity49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Entity__classmodel_Entity49", None)
        self.__classmodel_Entity49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Reference48"):
                opp_val = getattr(old_value, "classmodel_Reference48", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Reference48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Reference48"):
                opp_val = getattr(value, "classmodel_Reference48", None)
                setattr(value, "classmodel_Reference48", self)

    @property
    def classmodel_Entity21(self):
        return self.__classmodel_Entity21

    @classmodel_Entity21.setter
    def classmodel_Entity21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Entity__classmodel_Entity21", None)
        self.__classmodel_Entity21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Relationship"):
                opp_val = getattr(old_value, "classmodel_Relationship", None)
                if opp_val == self:
                    setattr(old_value, "classmodel_Relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Relationship"):
                opp_val = getattr(value, "classmodel_Relationship", None)
                setattr(value, "classmodel_Relationship", self)

class classmodel_Annotation:

    pass
class classmodel_Element:

    pass
class classmodel_Import:

    def __init__(self, importURI: str, classmodel_Import: "classmodel_Model" = None):
        self.importURI = importURI
        self.classmodel_Import = classmodel_Import
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def classmodel_Import(self):
        return self.__classmodel_Import

    @classmodel_Import.setter
    def classmodel_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Import__classmodel_Import", None)
        self.__classmodel_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Model"):
                opp_val = getattr(old_value, "classmodel_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Model"):
                opp_val = getattr(value, "classmodel_Model", None)
                if opp_val is None:
                    setattr(value, "classmodel_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classmodel_Model:

    pass
class classmodel_Feature:

    def __init__(self, name: str, value: str, constraint: str, visibility: str, classmodel_Feature: "classmodel_Classifier" = None, classmodel_Feature19: "classmodel_Enumeration" = None):
        self.name = name
        self.value = value
        self.constraint = constraint
        self.visibility = visibility
        self.classmodel_Feature = classmodel_Feature
        self.classmodel_Feature19 = classmodel_Feature19
        
    @property
    def constraint(self) -> str:
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint: str):
        self.__constraint = constraint

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

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
    def classmodel_Feature19(self):
        return self.__classmodel_Feature19

    @classmodel_Feature19.setter
    def classmodel_Feature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Feature__classmodel_Feature19", None)
        self.__classmodel_Feature19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Enumeration18"):
                opp_val = getattr(old_value, "classmodel_Enumeration18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Enumeration18"):
                opp_val = getattr(value, "classmodel_Enumeration18", None)
                if opp_val is None:
                    setattr(value, "classmodel_Enumeration18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classmodel_Feature(self):
        return self.__classmodel_Feature

    @classmodel_Feature.setter
    def classmodel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmodel_Feature__classmodel_Feature", None)
        self.__classmodel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmodel_Classifier12"):
                opp_val = getattr(old_value, "classmodel_Classifier12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmodel_Classifier12"):
                opp_val = getattr(value, "classmodel_Classifier12", None)
                if opp_val is None:
                    setattr(value, "classmodel_Classifier12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
