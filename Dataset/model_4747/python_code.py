from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    String = "String"
    Float = "Float"
    Integer = "Integer"
    Boolean = "Boolean"


############################################
# Definition of Classes
############################################

class EntityPage:

    pass
class solution_EditablePage(EntityPage):

    pass
class Link:

    pass
class solution_ContextualLink(Link):

    pass
class EditablePage:

    pass
class solution_UpdatePage(EditablePage):

    pass
class solution_DeletePage(EditablePage):

    pass
class solution_CreatePage(EditablePage):

    pass
class DynamicPage:

    pass
class solution_IndexPage(DynamicPage):

    pass
class solution_EntityPage(DynamicPage):

    pass
class WebPage:

    pass
class solution_DynamicPage(WebPage):

    pass
class solution_NonContextualLink(Link):

    pass
class solution_Link(ABC):

    def __init__(self, name: str, solution_Link: "solution_WebPage" = None, solution_Link26: "solution_WebPage" = None):
        self.name = name
        self.solution_Link = solution_Link
        self.solution_Link26 = solution_Link26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def solution_Link(self):
        return self.__solution_Link

    @solution_Link.setter
    def solution_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Link__solution_Link", None)
        self.__solution_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_WebPage18"):
                opp_val = getattr(old_value, "solution_WebPage18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_WebPage18"):
                opp_val = getattr(value, "solution_WebPage18", None)
                if opp_val is None:
                    setattr(value, "solution_WebPage18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def solution_Link26(self):
        return self.__solution_Link26

    @solution_Link26.setter
    def solution_Link26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Link__solution_Link26", None)
        self.__solution_Link26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_WebPage27"):
                opp_val = getattr(old_value, "solution_WebPage27", None)
                if opp_val == self:
                    setattr(old_value, "solution_WebPage27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_WebPage27"):
                opp_val = getattr(value, "solution_WebPage27", None)
                setattr(value, "solution_WebPage27", self)

class solution_Relationship:

    def __init__(self, roleName: str, lowerBound: int, upperBound: int, Relationship: "solution_Entity" = None, relationships: "solution_Entity" = None, solution_Relationship: "solution_Entity" = None, solution_Relationship16: "solution_Relationship" = None, solution_Relationship14: "solution_Relationship" = None):
        self.roleName = roleName
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.Relationship = Relationship
        self.relationships = relationships
        self.solution_Relationship = solution_Relationship
        self.solution_Relationship16 = solution_Relationship16
        self.solution_Relationship14 = solution_Relationship14
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def roleName(self) -> str:
        return self.__roleName

    @roleName.setter
    def roleName(self, roleName: str):
        self.__roleName = roleName

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def Relationship(self):
        return self.__Relationship

    @Relationship.setter
    def Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Relationship__Relationship", None)
        self.__Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def solution_Relationship(self):
        return self.__solution_Relationship

    @solution_Relationship.setter
    def solution_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Relationship__solution_Relationship", None)
        self.__solution_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_Entity13"):
                opp_val = getattr(old_value, "solution_Entity13", None)
                if opp_val == self:
                    setattr(old_value, "solution_Entity13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_Entity13"):
                opp_val = getattr(value, "solution_Entity13", None)
                setattr(value, "solution_Entity13", self)

    @property
    def solution_Relationship14(self):
        return self.__solution_Relationship14

    @solution_Relationship14.setter
    def solution_Relationship14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Relationship__solution_Relationship14", None)
        self.__solution_Relationship14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_Relationship16"):
                opp_val = getattr(old_value, "solution_Relationship16", None)
                if opp_val == self:
                    setattr(old_value, "solution_Relationship16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_Relationship16"):
                opp_val = getattr(value, "solution_Relationship16", None)
                setattr(value, "solution_Relationship16", self)

    @property
    def solution_Relationship16(self):
        return self.__solution_Relationship16

    @solution_Relationship16.setter
    def solution_Relationship16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Relationship__solution_Relationship16", None)
        self.__solution_Relationship16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_Relationship14"):
                opp_val = getattr(old_value, "solution_Relationship14", None)
                if opp_val == self:
                    setattr(old_value, "solution_Relationship14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_Relationship14"):
                opp_val = getattr(value, "solution_Relationship14", None)
                setattr(value, "solution_Relationship14", self)

    @property
    def relationships(self):
        return self.__relationships

    @relationships.setter
    def relationships(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Relationship__relationships", None)
        self.__relationships = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity"):
                opp_val = getattr(old_value, "Entity", None)
                if opp_val == self:
                    setattr(old_value, "Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity"):
                opp_val = getattr(value, "Entity", None)
                setattr(value, "Entity", self)

class solution_Attribute:

    def __init__(self, name: str, dataType: str, solution_Attribute: "solution_Entity" = None, solution_Attribute9: "solution_Entity" = None):
        self.name = name
        self.dataType = dataType
        self.solution_Attribute = solution_Attribute
        self.solution_Attribute9 = solution_Attribute9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def solution_Attribute(self):
        return self.__solution_Attribute

    @solution_Attribute.setter
    def solution_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Attribute__solution_Attribute", None)
        self.__solution_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_Entity6"):
                opp_val = getattr(old_value, "solution_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_Entity6"):
                opp_val = getattr(value, "solution_Entity6", None)
                if opp_val is None:
                    setattr(value, "solution_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def solution_Attribute9(self):
        return self.__solution_Attribute9

    @solution_Attribute9.setter
    def solution_Attribute9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Attribute__solution_Attribute9", None)
        self.__solution_Attribute9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_Entity8"):
                opp_val = getattr(old_value, "solution_Entity8", None)
                if opp_val == self:
                    setattr(old_value, "solution_Entity8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_Entity8"):
                opp_val = getattr(value, "solution_Entity8", None)
                setattr(value, "solution_Entity8", self)

class solution_StaticPage(WebPage):

    pass
class solution_WebPage(ABC):

    def __init__(self, name: str, relativeUrl: str, solution_WebPage: "solution_WebApplication" = None, solution_WebPage18: set["solution_Link"] = None, solution_WebPage20: "solution_NonContextualLink" = None, solution_WebPage27: "solution_Link" = None):
        self.name = name
        self.relativeUrl = relativeUrl
        self.solution_WebPage = solution_WebPage
        self.solution_WebPage18 = solution_WebPage18 if solution_WebPage18 is not None else set()
        self.solution_WebPage20 = solution_WebPage20
        self.solution_WebPage27 = solution_WebPage27
        
    @property
    def relativeUrl(self) -> str:
        return self.__relativeUrl

    @relativeUrl.setter
    def relativeUrl(self, relativeUrl: str):
        self.__relativeUrl = relativeUrl

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def solution_WebPage20(self):
        return self.__solution_WebPage20

    @solution_WebPage20.setter
    def solution_WebPage20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_WebPage__solution_WebPage20", None)
        self.__solution_WebPage20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_NonContextualLink"):
                opp_val = getattr(old_value, "solution_NonContextualLink", None)
                if opp_val == self:
                    setattr(old_value, "solution_NonContextualLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_NonContextualLink"):
                opp_val = getattr(value, "solution_NonContextualLink", None)
                setattr(value, "solution_NonContextualLink", self)

    @property
    def solution_WebPage27(self):
        return self.__solution_WebPage27

    @solution_WebPage27.setter
    def solution_WebPage27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_WebPage__solution_WebPage27", None)
        self.__solution_WebPage27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_Link26"):
                opp_val = getattr(old_value, "solution_Link26", None)
                if opp_val == self:
                    setattr(old_value, "solution_Link26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_Link26"):
                opp_val = getattr(value, "solution_Link26", None)
                setattr(value, "solution_Link26", self)

    @property
    def solution_WebPage(self):
        return self.__solution_WebPage

    @solution_WebPage.setter
    def solution_WebPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_WebPage__solution_WebPage", None)
        self.__solution_WebPage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_WebApplication2"):
                opp_val = getattr(old_value, "solution_WebApplication2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_WebApplication2"):
                opp_val = getattr(value, "solution_WebApplication2", None)
                if opp_val is None:
                    setattr(value, "solution_WebApplication2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def solution_WebPage18(self):
        return self.__solution_WebPage18

    @solution_WebPage18.setter
    def solution_WebPage18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_WebPage__solution_WebPage18", None)
        self.__solution_WebPage18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solution_Link"):
                    opp_val = getattr(item, "solution_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "solution_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solution_Link"):
                    opp_val = getattr(item, "solution_Link", None)
                    
                    setattr(item, "solution_Link", self)
                    

class solution_Entity:

    def __init__(self, name: str, solution_Entity: "solution_WebApplication" = None, solution_Entity6: set["solution_Attribute"] = None, solution_Entity8: "solution_Attribute" = None, source: set["solution_Relationship"] = None, Entity: "solution_Relationship" = None, solution_Entity13: "solution_Relationship" = None, solution_Entity22: "solution_DynamicPage" = None, solution_Entity29: "solution_ContextualLink" = None):
        self.name = name
        self.solution_Entity = solution_Entity
        self.solution_Entity6 = solution_Entity6 if solution_Entity6 is not None else set()
        self.solution_Entity8 = solution_Entity8
        self.source = source if source is not None else set()
        self.Entity = Entity
        self.solution_Entity13 = solution_Entity13
        self.solution_Entity22 = solution_Entity22
        self.solution_Entity29 = solution_Entity29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Entity(self):
        return self.__Entity

    @Entity.setter
    def Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Entity__Entity", None)
        self.__Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationships"):
                opp_val = getattr(old_value, "relationships", None)
                if opp_val == self:
                    setattr(old_value, "relationships", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationships"):
                opp_val = getattr(value, "relationships", None)
                setattr(value, "relationships", self)

    @property
    def solution_Entity22(self):
        return self.__solution_Entity22

    @solution_Entity22.setter
    def solution_Entity22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Entity__solution_Entity22", None)
        self.__solution_Entity22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_DynamicPage"):
                opp_val = getattr(old_value, "solution_DynamicPage", None)
                if opp_val == self:
                    setattr(old_value, "solution_DynamicPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_DynamicPage"):
                opp_val = getattr(value, "solution_DynamicPage", None)
                setattr(value, "solution_DynamicPage", self)

    @property
    def solution_Entity6(self):
        return self.__solution_Entity6

    @solution_Entity6.setter
    def solution_Entity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Entity__solution_Entity6", None)
        self.__solution_Entity6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solution_Attribute"):
                    opp_val = getattr(item, "solution_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "solution_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solution_Attribute"):
                    opp_val = getattr(item, "solution_Attribute", None)
                    
                    setattr(item, "solution_Attribute", self)
                    

    @property
    def solution_Entity29(self):
        return self.__solution_Entity29

    @solution_Entity29.setter
    def solution_Entity29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Entity__solution_Entity29", None)
        self.__solution_Entity29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_ContextualLink"):
                opp_val = getattr(old_value, "solution_ContextualLink", None)
                if opp_val == self:
                    setattr(old_value, "solution_ContextualLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_ContextualLink"):
                opp_val = getattr(value, "solution_ContextualLink", None)
                setattr(value, "solution_ContextualLink", self)

    @property
    def solution_Entity8(self):
        return self.__solution_Entity8

    @solution_Entity8.setter
    def solution_Entity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Entity__solution_Entity8", None)
        self.__solution_Entity8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_Attribute9"):
                opp_val = getattr(old_value, "solution_Attribute9", None)
                if opp_val == self:
                    setattr(old_value, "solution_Attribute9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_Attribute9"):
                opp_val = getattr(value, "solution_Attribute9", None)
                setattr(value, "solution_Attribute9", self)

    @property
    def solution_Entity13(self):
        return self.__solution_Entity13

    @solution_Entity13.setter
    def solution_Entity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Entity__solution_Entity13", None)
        self.__solution_Entity13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_Relationship"):
                opp_val = getattr(old_value, "solution_Relationship", None)
                if opp_val == self:
                    setattr(old_value, "solution_Relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_Relationship"):
                opp_val = getattr(value, "solution_Relationship", None)
                setattr(value, "solution_Relationship", self)

    @property
    def solution_Entity(self):
        return self.__solution_Entity

    @solution_Entity.setter
    def solution_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Entity__solution_Entity", None)
        self.__solution_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_WebApplication"):
                opp_val = getattr(old_value, "solution_WebApplication", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_WebApplication"):
                opp_val = getattr(value, "solution_WebApplication", None)
                if opp_val is None:
                    setattr(value, "solution_WebApplication", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_Entity__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    setattr(item, "Relationship", self)
                    

class solution_WebApplication:

    def __init__(self, name: str, solution_WebApplication: set["solution_Entity"] = None, solution_WebApplication2: set["solution_WebPage"] = None, solution_WebApplication4: "solution_StaticPage" = None):
        self.name = name
        self.solution_WebApplication = solution_WebApplication if solution_WebApplication is not None else set()
        self.solution_WebApplication2 = solution_WebApplication2 if solution_WebApplication2 is not None else set()
        self.solution_WebApplication4 = solution_WebApplication4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def solution_WebApplication4(self):
        return self.__solution_WebApplication4

    @solution_WebApplication4.setter
    def solution_WebApplication4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_WebApplication__solution_WebApplication4", None)
        self.__solution_WebApplication4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solution_StaticPage"):
                opp_val = getattr(old_value, "solution_StaticPage", None)
                if opp_val == self:
                    setattr(old_value, "solution_StaticPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solution_StaticPage"):
                opp_val = getattr(value, "solution_StaticPage", None)
                setattr(value, "solution_StaticPage", self)

    @property
    def solution_WebApplication(self):
        return self.__solution_WebApplication

    @solution_WebApplication.setter
    def solution_WebApplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_WebApplication__solution_WebApplication", None)
        self.__solution_WebApplication = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solution_Entity"):
                    opp_val = getattr(item, "solution_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "solution_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solution_Entity"):
                    opp_val = getattr(item, "solution_Entity", None)
                    
                    setattr(item, "solution_Entity", self)
                    

    @property
    def solution_WebApplication2(self):
        return self.__solution_WebApplication2

    @solution_WebApplication2.setter
    def solution_WebApplication2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solution_WebApplication__solution_WebApplication2", None)
        self.__solution_WebApplication2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solution_WebPage"):
                    opp_val = getattr(item, "solution_WebPage", None)
                    
                    if opp_val == self:
                        setattr(item, "solution_WebPage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solution_WebPage"):
                    opp_val = getattr(item, "solution_WebPage", None)
                    
                    setattr(item, "solution_WebPage", self)
                    

    def creationDateBeforeGoLive(self) -> bool:
        # TODO: Implement creationDateBeforeGoLive method
        pass
