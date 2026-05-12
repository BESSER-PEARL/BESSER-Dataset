from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AttributesType(Enum):
    Text = "Text"
    Object = "Object"
    Allocate = "Allocate"
    Link = "Link"


############################################
# Definition of Classes
############################################

class Attribute:

    pass
class requirement_ObjectAttribute(Attribute):

    pass
class requirement_TextAttribute(Attribute):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpecialChapter:

    pass
class requirement_TrashChapter(SpecialChapter):

    pass
class requirement_ProblemChapter(SpecialChapter):

    pass
class requirement_DeletedChapter(SpecialChapter):

    pass
class requirement_UntracedChapter(SpecialChapter):

    pass
class ObjectAttribute:

    pass
class requirement_AttributeAllocate(ObjectAttribute):

    pass
class requirement_AttributeLink(ObjectAttribute):

    def __init__(self, partial: str):
        self.partial = partial
        
        pass
    @property
    def partial(self):
        return self.__partial

    @partial.setter
    def partial(self, partial: str):
        self.__partial = partial


class Project:

    pass
class requirement_AttributeValue:

    def __init__(self, value: str, requirement_AttributeValue24: "requirement_DefaultAttributeValue" = None, requirement_AttributeValue: "requirement_ConfiguratedAttribute" = None):
        self.value = value
        self.requirement_AttributeValue24 = requirement_AttributeValue24
        self.requirement_AttributeValue = requirement_AttributeValue
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def requirement_AttributeValue(self):
        return self.__requirement_AttributeValue

    @requirement_AttributeValue.setter
    def requirement_AttributeValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_AttributeValue__requirement_AttributeValue", None)
        self.__requirement_AttributeValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_ConfiguratedAttribute21"):
                opp_val = getattr(old_value, "requirement_ConfiguratedAttribute21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_ConfiguratedAttribute21"):
                opp_val = getattr(value, "requirement_ConfiguratedAttribute21", None)
                if opp_val is None:
                    setattr(value, "requirement_ConfiguratedAttribute21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirement_AttributeValue24(self):
        return self.__requirement_AttributeValue24

    @requirement_AttributeValue24.setter
    def requirement_AttributeValue24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_AttributeValue__requirement_AttributeValue24", None)
        self.__requirement_AttributeValue24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_DefaultAttributeValue23"):
                opp_val = getattr(old_value, "requirement_DefaultAttributeValue23", None)
                if opp_val == self:
                    setattr(old_value, "requirement_DefaultAttributeValue23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_DefaultAttributeValue23"):
                opp_val = getattr(value, "requirement_DefaultAttributeValue23", None)
                setattr(value, "requirement_DefaultAttributeValue23", self)

class requirement_DefaultAttributeValue:

    pass
class requirement_ConfiguratedAttribute:

    def __init__(self, type: str, name: str, requirement_ConfiguratedAttribute: "requirement_AttributeConfiguration" = None, requirement_ConfiguratedAttribute19: "requirement_DefaultAttributeValue" = None, requirement_ConfiguratedAttribute21: set["requirement_AttributeValue"] = None):
        self.type = type
        self.name = name
        self.requirement_ConfiguratedAttribute = requirement_ConfiguratedAttribute
        self.requirement_ConfiguratedAttribute19 = requirement_ConfiguratedAttribute19
        self.requirement_ConfiguratedAttribute21 = requirement_ConfiguratedAttribute21 if requirement_ConfiguratedAttribute21 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def requirement_ConfiguratedAttribute19(self):
        return self.__requirement_ConfiguratedAttribute19

    @requirement_ConfiguratedAttribute19.setter
    def requirement_ConfiguratedAttribute19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_ConfiguratedAttribute__requirement_ConfiguratedAttribute19", None)
        self.__requirement_ConfiguratedAttribute19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_DefaultAttributeValue"):
                opp_val = getattr(old_value, "requirement_DefaultAttributeValue", None)
                if opp_val == self:
                    setattr(old_value, "requirement_DefaultAttributeValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_DefaultAttributeValue"):
                opp_val = getattr(value, "requirement_DefaultAttributeValue", None)
                setattr(value, "requirement_DefaultAttributeValue", self)

    @property
    def requirement_ConfiguratedAttribute21(self):
        return self.__requirement_ConfiguratedAttribute21

    @requirement_ConfiguratedAttribute21.setter
    def requirement_ConfiguratedAttribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_ConfiguratedAttribute__requirement_ConfiguratedAttribute21", None)
        self.__requirement_ConfiguratedAttribute21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirement_AttributeValue"):
                    opp_val = getattr(item, "requirement_AttributeValue", None)
                    
                    if opp_val == self:
                        setattr(item, "requirement_AttributeValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirement_AttributeValue"):
                    opp_val = getattr(item, "requirement_AttributeValue", None)
                    
                    setattr(item, "requirement_AttributeValue", self)
                    

    @property
    def requirement_ConfiguratedAttribute(self):
        return self.__requirement_ConfiguratedAttribute

    @requirement_ConfiguratedAttribute.setter
    def requirement_ConfiguratedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_ConfiguratedAttribute__requirement_ConfiguratedAttribute", None)
        self.__requirement_ConfiguratedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_AttributeConfiguration17"):
                opp_val = getattr(old_value, "requirement_AttributeConfiguration17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_AttributeConfiguration17"):
                opp_val = getattr(value, "requirement_AttributeConfiguration17", None)
                if opp_val is None:
                    setattr(value, "requirement_AttributeConfiguration17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EModelElement:

    pass
class requirement_IdentifiedElement(EModelElement):

    def __init__(self, identifier: str, shortDescription: str):
        self.identifier = identifier
        self.shortDescription = shortDescription
        
        pass
    @property
    def shortDescription(self):
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription


    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


class requirement_Attribute(EModelElement):

    def __init__(self, name: str, requirement_Attribute: "requirement_Requirement" = None):
        self.name = name
        self.requirement_Attribute = requirement_Attribute
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def requirement_Attribute(self):
        return self.__requirement_Attribute

    @requirement_Attribute.setter
    def requirement_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Attribute__requirement_Attribute", None)
        self.__requirement_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_Requirement34"):
                opp_val = getattr(old_value, "requirement_Requirement34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_Requirement34"):
                opp_val = getattr(value, "requirement_Requirement34", None)
                if opp_val is None:
                    setattr(value, "requirement_Requirement34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Requirement:

    pass
class requirement_AnonymousRequirement(Requirement):

    pass
class requirement_CurrentRequirement(Requirement):

    def __init__(self, impacted: bool):
        self.impacted = impacted
        
        pass
    @property
    def impacted(self):
        return self.__impacted

    @impacted.setter
    def impacted(self, impacted: bool):
        self.__impacted = impacted


class requirement_EObject:

    pass
class requirement_UpstreamModel(Project):

    pass
class requirement_SpecialChapter(ABC):

    pass
class requirement_AttributeConfiguration:

    pass
class IdentifiedElement:

    pass
class requirement_HierarchicalElement(IdentifiedElement):

    def __init__(self, nextReqIndex: str, requirement_HierarchicalElement8: "requirement_EObject" = None, HierarchicalElement: "requirement_HierarchicalElement" = None, parent: set["requirement_HierarchicalElement"] = None, HierarchicalElement13: "requirement_HierarchicalElement" = None, children: "requirement_HierarchicalElement" = None, requirement_HierarchicalElement: "requirement_RequirementProject" = None, requirement_HierarchicalElement15: set["requirement_Requirement"] = None, requirement_HierarchicalElement27: "requirement_SpecialChapter" = None):
        self.nextReqIndex = nextReqIndex
        self.requirement_HierarchicalElement8 = requirement_HierarchicalElement8
        self.HierarchicalElement = HierarchicalElement
        self.parent = parent if parent is not None else set()
        self.HierarchicalElement13 = HierarchicalElement13
        self.children = children
        self.requirement_HierarchicalElement = requirement_HierarchicalElement
        self.requirement_HierarchicalElement15 = requirement_HierarchicalElement15 if requirement_HierarchicalElement15 is not None else set()
        self.requirement_HierarchicalElement27 = requirement_HierarchicalElement27
        
        pass
    @property
    def nextReqIndex(self):
        return self.__nextReqIndex

    @nextReqIndex.setter
    def nextReqIndex(self, nextReqIndex: str):
        self.__nextReqIndex = nextReqIndex


    @property
    def HierarchicalElement13(self):
        return self.__HierarchicalElement13

    @HierarchicalElement13.setter
    def HierarchicalElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_HierarchicalElement__HierarchicalElement13", None)
        self.__HierarchicalElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def HierarchicalElement(self):
        return self.__HierarchicalElement

    @HierarchicalElement.setter
    def HierarchicalElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_HierarchicalElement__HierarchicalElement", None)
        self.__HierarchicalElement = value
        
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
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_HierarchicalElement__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HierarchicalElement"):
                    opp_val = getattr(item, "HierarchicalElement", None)
                    
                    if opp_val == self:
                        setattr(item, "HierarchicalElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HierarchicalElement"):
                    opp_val = getattr(item, "HierarchicalElement", None)
                    
                    setattr(item, "HierarchicalElement", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_HierarchicalElement__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HierarchicalElement13"):
                opp_val = getattr(old_value, "HierarchicalElement13", None)
                if opp_val == self:
                    setattr(old_value, "HierarchicalElement13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HierarchicalElement13"):
                opp_val = getattr(value, "HierarchicalElement13", None)
                setattr(value, "HierarchicalElement13", self)

    @property
    def requirement_HierarchicalElement(self):
        return self.__requirement_HierarchicalElement

    @requirement_HierarchicalElement.setter
    def requirement_HierarchicalElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_HierarchicalElement__requirement_HierarchicalElement", None)
        self.__requirement_HierarchicalElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_RequirementProject"):
                opp_val = getattr(old_value, "requirement_RequirementProject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_RequirementProject"):
                opp_val = getattr(value, "requirement_RequirementProject", None)
                if opp_val is None:
                    setattr(value, "requirement_RequirementProject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirement_HierarchicalElement15(self):
        return self.__requirement_HierarchicalElement15

    @requirement_HierarchicalElement15.setter
    def requirement_HierarchicalElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_HierarchicalElement__requirement_HierarchicalElement15", None)
        self.__requirement_HierarchicalElement15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirement_Requirement"):
                    opp_val = getattr(item, "requirement_Requirement", None)
                    
                    if opp_val == self:
                        setattr(item, "requirement_Requirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirement_Requirement"):
                    opp_val = getattr(item, "requirement_Requirement", None)
                    
                    setattr(item, "requirement_Requirement", self)
                    

    @property
    def requirement_HierarchicalElement27(self):
        return self.__requirement_HierarchicalElement27

    @requirement_HierarchicalElement27.setter
    def requirement_HierarchicalElement27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_HierarchicalElement__requirement_HierarchicalElement27", None)
        self.__requirement_HierarchicalElement27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_SpecialChapter26"):
                opp_val = getattr(old_value, "requirement_SpecialChapter26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_SpecialChapter26"):
                opp_val = getattr(value, "requirement_SpecialChapter26", None)
                if opp_val is None:
                    setattr(value, "requirement_SpecialChapter26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirement_HierarchicalElement8(self):
        return self.__requirement_HierarchicalElement8

    @requirement_HierarchicalElement8.setter
    def requirement_HierarchicalElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_HierarchicalElement__requirement_HierarchicalElement8", None)
        self.__requirement_HierarchicalElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_EObject"):
                opp_val = getattr(old_value, "requirement_EObject", None)
                if opp_val == self:
                    setattr(old_value, "requirement_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_EObject"):
                opp_val = getattr(value, "requirement_EObject", None)
                setattr(value, "requirement_EObject", self)

class requirement_RequirementProject(IdentifiedElement):

    pass
class requirement_Requirement(IdentifiedElement):

    def __init__(self, externalResources: str, requirement_Requirement: "requirement_HierarchicalElement" = None, requirement_Requirement30: "requirement_SpecialChapter" = None, requirement_Requirement34: set["requirement_Attribute"] = None):
        self.externalResources = externalResources
        self.requirement_Requirement = requirement_Requirement
        self.requirement_Requirement30 = requirement_Requirement30
        self.requirement_Requirement34 = requirement_Requirement34 if requirement_Requirement34 is not None else set()
        
        pass
    @property
    def externalResources(self):
        return self.__externalResources

    @externalResources.setter
    def externalResources(self, externalResources: str):
        self.__externalResources = externalResources


    @property
    def requirement_Requirement(self):
        return self.__requirement_Requirement

    @requirement_Requirement.setter
    def requirement_Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Requirement__requirement_Requirement", None)
        self.__requirement_Requirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_HierarchicalElement15"):
                opp_val = getattr(old_value, "requirement_HierarchicalElement15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_HierarchicalElement15"):
                opp_val = getattr(value, "requirement_HierarchicalElement15", None)
                if opp_val is None:
                    setattr(value, "requirement_HierarchicalElement15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirement_Requirement30(self):
        return self.__requirement_Requirement30

    @requirement_Requirement30.setter
    def requirement_Requirement30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Requirement__requirement_Requirement30", None)
        self.__requirement_Requirement30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_SpecialChapter29"):
                opp_val = getattr(old_value, "requirement_SpecialChapter29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_SpecialChapter29"):
                opp_val = getattr(value, "requirement_SpecialChapter29", None)
                if opp_val is None:
                    setattr(value, "requirement_SpecialChapter29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirement_Requirement34(self):
        return self.__requirement_Requirement34

    @requirement_Requirement34.setter
    def requirement_Requirement34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirement_Requirement__requirement_Requirement34", None)
        self.__requirement_Requirement34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirement_Attribute"):
                    opp_val = getattr(item, "requirement_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "requirement_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirement_Attribute"):
                    opp_val = getattr(item, "requirement_Attribute", None)
                    
                    setattr(item, "requirement_Attribute", self)
                    
