from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AssociationType(Enum):
    simpleAssociation = "simpleAssociation"
    aggregation = "aggregation"
    composition = "composition"
class Visibility(Enum):
    unspecified = "unspecified"
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"


############################################
# Definition of Classes
############################################

class ClassMember:

    pass
class yuml_ClassMember(ABC):

    def __init__(self, visibility: str, name: str):
        self.visibility = visibility
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

class yuml_Cardinality:

    def __init__(self, lowerBound: str, upperBound: str, yuml_Cardinality11: "yuml_Association" = None, yuml_Cardinality: "yuml_Association" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.yuml_Cardinality11 = yuml_Cardinality11
        self.yuml_Cardinality = yuml_Cardinality
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

    @property
    def yuml_Cardinality(self):
        return self.__yuml_Cardinality

    @yuml_Cardinality.setter
    def yuml_Cardinality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Cardinality__yuml_Cardinality", None)
        self.__yuml_Cardinality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yuml_Association"):
                opp_val = getattr(old_value, "yuml_Association", None)
                if opp_val == self:
                    setattr(old_value, "yuml_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yuml_Association"):
                opp_val = getattr(value, "yuml_Association", None)
                setattr(value, "yuml_Association", self)

    @property
    def yuml_Cardinality11(self):
        return self.__yuml_Cardinality11

    @yuml_Cardinality11.setter
    def yuml_Cardinality11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Cardinality__yuml_Cardinality11", None)
        self.__yuml_Cardinality11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yuml_Association10"):
                opp_val = getattr(old_value, "yuml_Association10", None)
                if opp_val == self:
                    setattr(old_value, "yuml_Association10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yuml_Association10"):
                opp_val = getattr(value, "yuml_Association10", None)
                setattr(value, "yuml_Association10", self)

class Relationship:

    pass
class yuml_Equivalence(Relationship):

    pass
class yuml_NoteAssociation(Relationship):

    pass
class yuml_Association(Relationship):

    def __init__(self, sourceVisibility: str, navigableTarget: bool, targetVisibility: str, type: str, navigableSource: bool, yuml_Association10: "yuml_Cardinality" = None, yuml_Association: "yuml_Cardinality" = None):
        self.sourceVisibility = sourceVisibility
        self.navigableTarget = navigableTarget
        self.targetVisibility = targetVisibility
        self.type = type
        self.navigableSource = navigableSource
        self.yuml_Association10 = yuml_Association10
        self.yuml_Association = yuml_Association
        
    @property
    def navigableTarget(self) -> bool:
        return self.__navigableTarget

    @navigableTarget.setter
    def navigableTarget(self, navigableTarget: bool):
        self.__navigableTarget = navigableTarget

    @property
    def navigableSource(self) -> bool:
        return self.__navigableSource

    @navigableSource.setter
    def navigableSource(self, navigableSource: bool):
        self.__navigableSource = navigableSource

    @property
    def targetVisibility(self) -> str:
        return self.__targetVisibility

    @targetVisibility.setter
    def targetVisibility(self, targetVisibility: str):
        self.__targetVisibility = targetVisibility

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sourceVisibility(self) -> str:
        return self.__sourceVisibility

    @sourceVisibility.setter
    def sourceVisibility(self, sourceVisibility: str):
        self.__sourceVisibility = sourceVisibility

    @property
    def yuml_Association10(self):
        return self.__yuml_Association10

    @yuml_Association10.setter
    def yuml_Association10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Association__yuml_Association10", None)
        self.__yuml_Association10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yuml_Cardinality11"):
                opp_val = getattr(old_value, "yuml_Cardinality11", None)
                if opp_val == self:
                    setattr(old_value, "yuml_Cardinality11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yuml_Cardinality11"):
                opp_val = getattr(value, "yuml_Cardinality11", None)
                setattr(value, "yuml_Cardinality11", self)

    @property
    def yuml_Association(self):
        return self.__yuml_Association

    @yuml_Association.setter
    def yuml_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Association__yuml_Association", None)
        self.__yuml_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yuml_Cardinality"):
                opp_val = getattr(old_value, "yuml_Cardinality", None)
                if opp_val == self:
                    setattr(old_value, "yuml_Cardinality", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yuml_Cardinality"):
                opp_val = getattr(value, "yuml_Cardinality", None)
                setattr(value, "yuml_Cardinality", self)

class yuml_Method(ClassMember):

    def __init__(self, arguments: str, yuml_Method: "yuml_Class" = None):
        self.arguments = arguments
        self.yuml_Method = yuml_Method
        
    @property
    def arguments(self) -> str:
        return self.__arguments

    @arguments.setter
    def arguments(self, arguments: str):
        self.__arguments = arguments

    @property
    def yuml_Method(self):
        return self.__yuml_Method

    @yuml_Method.setter
    def yuml_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Method__yuml_Method", None)
        self.__yuml_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yuml_Class3"):
                opp_val = getattr(old_value, "yuml_Class3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yuml_Class3"):
                opp_val = getattr(value, "yuml_Class3", None)
                if opp_val is None:
                    setattr(value, "yuml_Class3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class yuml_Attribute(ClassMember):

    def __init__(self, stereotype: str, type: str, yuml_Attribute: "yuml_Class" = None):
        self.stereotype = stereotype
        self.type = type
        self.yuml_Attribute = yuml_Attribute
        
    @property
    def stereotype(self) -> str:
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def yuml_Attribute(self):
        return self.__yuml_Attribute

    @yuml_Attribute.setter
    def yuml_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Attribute__yuml_Attribute", None)
        self.__yuml_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yuml_Class"):
                opp_val = getattr(old_value, "yuml_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yuml_Class"):
                opp_val = getattr(value, "yuml_Class", None)
                if opp_val is None:
                    setattr(value, "yuml_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ColorableElement:

    pass
class yuml_Note(ColorableElement):

    def __init__(self, text: str, yuml_Note: "yuml_NoteAssociation" = None):
        self.text = text
        self.yuml_Note = yuml_Note
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def yuml_Note(self):
        return self.__yuml_Note

    @yuml_Note.setter
    def yuml_Note(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Note__yuml_Note", None)
        self.__yuml_Note = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yuml_NoteAssociation"):
                opp_val = getattr(old_value, "yuml_NoteAssociation", None)
                if opp_val == self:
                    setattr(old_value, "yuml_NoteAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yuml_NoteAssociation"):
                opp_val = getattr(value, "yuml_NoteAssociation", None)
                setattr(value, "yuml_NoteAssociation", self)

class yuml_Class(ColorableElement):

    def __init__(self, stereotype: str, name: str, yuml_Class: set["yuml_Attribute"] = None, yuml_Class3: set["yuml_Method"] = None, yuml_Class5: "yuml_Relationship" = None):
        self.stereotype = stereotype
        self.name = name
        self.yuml_Class = yuml_Class if yuml_Class is not None else set()
        self.yuml_Class3 = yuml_Class3 if yuml_Class3 is not None else set()
        self.yuml_Class5 = yuml_Class5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stereotype(self) -> str:
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype

    @property
    def yuml_Class(self):
        return self.__yuml_Class

    @yuml_Class.setter
    def yuml_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Class__yuml_Class", None)
        self.__yuml_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yuml_Attribute"):
                    opp_val = getattr(item, "yuml_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "yuml_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yuml_Attribute"):
                    opp_val = getattr(item, "yuml_Attribute", None)
                    
                    setattr(item, "yuml_Attribute", self)
                    

    @property
    def yuml_Class5(self):
        return self.__yuml_Class5

    @yuml_Class5.setter
    def yuml_Class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Class__yuml_Class5", None)
        self.__yuml_Class5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yuml_Relationship"):
                opp_val = getattr(old_value, "yuml_Relationship", None)
                if opp_val == self:
                    setattr(old_value, "yuml_Relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yuml_Relationship"):
                opp_val = getattr(value, "yuml_Relationship", None)
                setattr(value, "yuml_Relationship", self)

    @property
    def yuml_Class3(self):
        return self.__yuml_Class3

    @yuml_Class3.setter
    def yuml_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Class__yuml_Class3", None)
        self.__yuml_Class3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "yuml_Method"):
                    opp_val = getattr(item, "yuml_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "yuml_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "yuml_Method"):
                    opp_val = getattr(item, "yuml_Method", None)
                    
                    setattr(item, "yuml_Method", self)
                    

class yuml_Inheritance(Relationship):

    pass
class ModelElement:

    pass
class yuml_Relationship(ModelElement):

    def __init__(self, sourceLabel: str, targetLabel: str, yuml_Relationship: "yuml_Class" = None, yuml_Relationship7: "yuml_ColorableElement" = None):
        self.sourceLabel = sourceLabel
        self.targetLabel = targetLabel
        self.yuml_Relationship = yuml_Relationship
        self.yuml_Relationship7 = yuml_Relationship7
        
    @property
    def targetLabel(self) -> str:
        return self.__targetLabel

    @targetLabel.setter
    def targetLabel(self, targetLabel: str):
        self.__targetLabel = targetLabel

    @property
    def sourceLabel(self) -> str:
        return self.__sourceLabel

    @sourceLabel.setter
    def sourceLabel(self, sourceLabel: str):
        self.__sourceLabel = sourceLabel

    @property
    def yuml_Relationship7(self):
        return self.__yuml_Relationship7

    @yuml_Relationship7.setter
    def yuml_Relationship7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Relationship__yuml_Relationship7", None)
        self.__yuml_Relationship7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yuml_ColorableElement"):
                opp_val = getattr(old_value, "yuml_ColorableElement", None)
                if opp_val == self:
                    setattr(old_value, "yuml_ColorableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yuml_ColorableElement"):
                opp_val = getattr(value, "yuml_ColorableElement", None)
                setattr(value, "yuml_ColorableElement", self)

    @property
    def yuml_Relationship(self):
        return self.__yuml_Relationship

    @yuml_Relationship.setter
    def yuml_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_Relationship__yuml_Relationship", None)
        self.__yuml_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yuml_Class5"):
                opp_val = getattr(old_value, "yuml_Class5", None)
                if opp_val == self:
                    setattr(old_value, "yuml_Class5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yuml_Class5"):
                opp_val = getattr(value, "yuml_Class5", None)
                setattr(value, "yuml_Class5", self)

class yuml_ColorableElement(ModelElement):

    def __init__(self, color: str, yuml_ColorableElement: "yuml_Relationship" = None):
        self.color = color
        self.yuml_ColorableElement = yuml_ColorableElement
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def yuml_ColorableElement(self):
        return self.__yuml_ColorableElement

    @yuml_ColorableElement.setter
    def yuml_ColorableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_yuml_ColorableElement__yuml_ColorableElement", None)
        self.__yuml_ColorableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "yuml_Relationship7"):
                opp_val = getattr(old_value, "yuml_Relationship7", None)
                if opp_val == self:
                    setattr(old_value, "yuml_Relationship7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "yuml_Relationship7"):
                opp_val = getattr(value, "yuml_Relationship7", None)
                setattr(value, "yuml_Relationship7", self)

class yuml_ModelElement(ABC):

    pass
class yuml_Model:

    pass