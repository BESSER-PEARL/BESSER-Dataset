from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SimpleUML_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class SimpleUML_Feature(NamedElement):

    def __init__(self, isMultivalued: bool, SimpleUML_Feature: "SimpleUML_Class" = None, SimpleUML_Feature4: "SimpleUML_Class" = None):
        self.isMultivalued = isMultivalued
        self.SimpleUML_Feature = SimpleUML_Feature
        self.SimpleUML_Feature4 = SimpleUML_Feature4
        
    @property
    def isMultivalued(self) -> bool:
        return self.__isMultivalued

    @isMultivalued.setter
    def isMultivalued(self, isMultivalued: bool):
        self.__isMultivalued = isMultivalued

    @property
    def SimpleUML_Feature4(self):
        return self.__SimpleUML_Feature4

    @SimpleUML_Feature4.setter
    def SimpleUML_Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleUML_Feature__SimpleUML_Feature4", None)
        self.__SimpleUML_Feature4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleUML_Class5"):
                opp_val = getattr(old_value, "SimpleUML_Class5", None)
                if opp_val == self:
                    setattr(old_value, "SimpleUML_Class5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleUML_Class5"):
                opp_val = getattr(value, "SimpleUML_Class5", None)
                setattr(value, "SimpleUML_Class5", self)

    @property
    def SimpleUML_Feature(self):
        return self.__SimpleUML_Feature

    @SimpleUML_Feature.setter
    def SimpleUML_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleUML_Feature__SimpleUML_Feature", None)
        self.__SimpleUML_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleUML_Class"):
                opp_val = getattr(old_value, "SimpleUML_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleUML_Class"):
                opp_val = getattr(value, "SimpleUML_Class", None)
                if opp_val is None:
                    setattr(value, "SimpleUML_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SimpleUML_Class(NamedElement):

    pass
class SimpleUML_Package:

    pass