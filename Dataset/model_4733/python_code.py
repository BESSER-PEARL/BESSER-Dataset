from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Datentyp(Enum):
    Integer = "Integer"
    String = "String"
    Float = "Float"
    Boolean = "Boolean"
    Email = "Email"
    Date = "Date"
    Time = "Time"


############################################
# Definition of Classes
############################################

class Links:

    pass
class LinkKat1:

    pass
class LinkKat2:

    pass
class swml_ContextualLinks(LinkKat2):

    pass
class swml_NonContextualLinks(LinkKat2):

    pass
class swml_LinkParamater:

    def __init__(self, Parameter: str, swml_LinkParamater: "swml_Links" = None):
        self.Parameter = Parameter
        self.swml_LinkParamater = swml_LinkParamater
        
    @property
    def Parameter(self) -> str:
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, Parameter: str):
        self.__Parameter = Parameter

    @property
    def swml_LinkParamater(self):
        return self.__swml_LinkParamater

    @swml_LinkParamater.setter
    def swml_LinkParamater(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_LinkParamater__swml_LinkParamater", None)
        self.__swml_LinkParamater = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Links"):
                opp_val = getattr(old_value, "swml_Links", None)
                if opp_val == self:
                    setattr(old_value, "swml_Links", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Links"):
                opp_val = getattr(value, "swml_Links", None)
                setattr(value, "swml_Links", self)

class swml_Links(ABC):

    def __init__(self, Name: str, swml_Links: "swml_LinkParamater" = None, swml_Links53: "swml_WebPage" = None):
        self.Name = Name
        self.swml_Links = swml_Links
        self.swml_Links53 = swml_Links53
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def swml_Links(self):
        return self.__swml_Links

    @swml_Links.setter
    def swml_Links(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Links__swml_Links", None)
        self.__swml_Links = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_LinkParamater"):
                opp_val = getattr(old_value, "swml_LinkParamater", None)
                if opp_val == self:
                    setattr(old_value, "swml_LinkParamater", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_LinkParamater"):
                opp_val = getattr(value, "swml_LinkParamater", None)
                setattr(value, "swml_LinkParamater", self)

    @property
    def swml_Links53(self):
        return self.__swml_Links53

    @swml_Links53.setter
    def swml_Links53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Links__swml_Links53", None)
        self.__swml_Links53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_WebPage54"):
                opp_val = getattr(old_value, "swml_WebPage54", None)
                if opp_val == self:
                    setattr(old_value, "swml_WebPage54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_WebPage54"):
                opp_val = getattr(value, "swml_WebPage54", None)
                setattr(value, "swml_WebPage54", self)

class swml_KO(LinkKat1):

    pass
class swml_OK(LinkKat1):

    pass
class EntityPages:

    pass
class swml_CreatePage(EntityPages):

    pass
class swml_DeletePage(EntityPages):

    pass
class swml_UpdatePage(EntityPages):

    pass
class dynamicPage:

    pass
class swml_IndexPages(dynamicPage):

    pass
class swml_LinkKat1(Links):

    pass
class WebPage:

    pass
class swml_dynamicPage(WebPage):

    pass
class swml_LinkJoinNode(WebPage):

    pass
class swml_LinkKat2(Links):

    pass
class swml_staticPage(WebPage):

    pass
class swml_WebPage(ABC):

    def __init__(self, name: str, swml_WebPage: "swml_HypertextModel" = None, swml_WebPage32: set["swml_LinkKat2"] = None, swml_WebPage54: "swml_Links" = None):
        self.name = name
        self.swml_WebPage = swml_WebPage
        self.swml_WebPage32 = swml_WebPage32 if swml_WebPage32 is not None else set()
        self.swml_WebPage54 = swml_WebPage54
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_WebPage54(self):
        return self.__swml_WebPage54

    @swml_WebPage54.setter
    def swml_WebPage54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_WebPage__swml_WebPage54", None)
        self.__swml_WebPage54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Links53"):
                opp_val = getattr(old_value, "swml_Links53", None)
                if opp_val == self:
                    setattr(old_value, "swml_Links53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Links53"):
                opp_val = getattr(value, "swml_Links53", None)
                setattr(value, "swml_Links53", self)

    @property
    def swml_WebPage(self):
        return self.__swml_WebPage

    @swml_WebPage.setter
    def swml_WebPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_WebPage__swml_WebPage", None)
        self.__swml_WebPage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_HypertextModel28"):
                opp_val = getattr(old_value, "swml_HypertextModel28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_HypertextModel28"):
                opp_val = getattr(value, "swml_HypertextModel28", None)
                if opp_val is None:
                    setattr(value, "swml_HypertextModel28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_WebPage32(self):
        return self.__swml_WebPage32

    @swml_WebPage32.setter
    def swml_WebPage32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_WebPage__swml_WebPage32", None)
        self.__swml_WebPage32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_LinkKat2"):
                    opp_val = getattr(item, "swml_LinkKat2", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_LinkKat2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_LinkKat2"):
                    opp_val = getattr(item, "swml_LinkKat2", None)
                    
                    setattr(item, "swml_LinkKat2", self)
                    

class swml_Literals:

    def __init__(self, name: str, swml_Literals: "swml_Enumeration" = None):
        self.name = name
        self.swml_Literals = swml_Literals
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_Literals(self):
        return self.__swml_Literals

    @swml_Literals.setter
    def swml_Literals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Literals__swml_Literals", None)
        self.__swml_Literals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Enumeration26"):
                opp_val = getattr(old_value, "swml_Enumeration26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Enumeration26"):
                opp_val = getattr(value, "swml_Enumeration26", None)
                if opp_val is None:
                    setattr(value, "swml_Enumeration26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swml_EntityPages(dynamicPage):

    pass
class swml_Reference:

    def __init__(self, rolename: str, lowerBound: int, upperBound: int, swml_Reference: "swml_Entity" = None, swml_Reference21: "swml_Reference" = None, swml_Reference19: "swml_Reference" = None, swml_Reference23: "swml_Entity" = None):
        self.rolename = rolename
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.swml_Reference = swml_Reference
        self.swml_Reference21 = swml_Reference21
        self.swml_Reference19 = swml_Reference19
        self.swml_Reference23 = swml_Reference23
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def rolename(self) -> str:
        return self.__rolename

    @rolename.setter
    def rolename(self, rolename: str):
        self.__rolename = rolename

    @property
    def swml_Reference21(self):
        return self.__swml_Reference21

    @swml_Reference21.setter
    def swml_Reference21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Reference__swml_Reference21", None)
        self.__swml_Reference21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Reference19"):
                opp_val = getattr(old_value, "swml_Reference19", None)
                if opp_val == self:
                    setattr(old_value, "swml_Reference19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Reference19"):
                opp_val = getattr(value, "swml_Reference19", None)
                setattr(value, "swml_Reference19", self)

    @property
    def swml_Reference23(self):
        return self.__swml_Reference23

    @swml_Reference23.setter
    def swml_Reference23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Reference__swml_Reference23", None)
        self.__swml_Reference23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Entity24"):
                opp_val = getattr(old_value, "swml_Entity24", None)
                if opp_val == self:
                    setattr(old_value, "swml_Entity24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Entity24"):
                opp_val = getattr(value, "swml_Entity24", None)
                setattr(value, "swml_Entity24", self)

    @property
    def swml_Reference19(self):
        return self.__swml_Reference19

    @swml_Reference19.setter
    def swml_Reference19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Reference__swml_Reference19", None)
        self.__swml_Reference19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Reference21"):
                opp_val = getattr(old_value, "swml_Reference21", None)
                if opp_val == self:
                    setattr(old_value, "swml_Reference21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Reference21"):
                opp_val = getattr(value, "swml_Reference21", None)
                setattr(value, "swml_Reference21", self)

    @property
    def swml_Reference(self):
        return self.__swml_Reference

    @swml_Reference.setter
    def swml_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Reference__swml_Reference", None)
        self.__swml_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Entity12"):
                opp_val = getattr(old_value, "swml_Entity12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Entity12"):
                opp_val = getattr(value, "swml_Entity12", None)
                if opp_val is None:
                    setattr(value, "swml_Entity12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swml_Attribute:

    def __init__(self, name: str, Typ: str, swml_Attribute: "swml_Entity" = None):
        self.name = name
        self.Typ = Typ
        self.swml_Attribute = swml_Attribute
        
    @property
    def Typ(self) -> str:
        return self.__Typ

    @Typ.setter
    def Typ(self, Typ: str):
        self.__Typ = Typ

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_Attribute(self):
        return self.__swml_Attribute

    @swml_Attribute.setter
    def swml_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Attribute__swml_Attribute", None)
        self.__swml_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Entity10"):
                opp_val = getattr(old_value, "swml_Entity10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Entity10"):
                opp_val = getattr(value, "swml_Entity10", None)
                if opp_val is None:
                    setattr(value, "swml_Entity10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swml_EnumTyp:

    def __init__(self, name: str, swml_EnumTyp: "swml_Entity" = None, swml_EnumTyp17: "swml_Enumeration" = None):
        self.name = name
        self.swml_EnumTyp = swml_EnumTyp
        self.swml_EnumTyp17 = swml_EnumTyp17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_EnumTyp(self):
        return self.__swml_EnumTyp

    @swml_EnumTyp.setter
    def swml_EnumTyp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_EnumTyp__swml_EnumTyp", None)
        self.__swml_EnumTyp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Entity8"):
                opp_val = getattr(old_value, "swml_Entity8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Entity8"):
                opp_val = getattr(value, "swml_Entity8", None)
                if opp_val is None:
                    setattr(value, "swml_Entity8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_EnumTyp17(self):
        return self.__swml_EnumTyp17

    @swml_EnumTyp17.setter
    def swml_EnumTyp17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_EnumTyp__swml_EnumTyp17", None)
        self.__swml_EnumTyp17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Enumeration18"):
                opp_val = getattr(old_value, "swml_Enumeration18", None)
                if opp_val == self:
                    setattr(old_value, "swml_Enumeration18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Enumeration18"):
                opp_val = getattr(value, "swml_Enumeration18", None)
                setattr(value, "swml_Enumeration18", self)

class swml_Entity:

    def __init__(self, name: str, swml_Entity: "swml_ContentModel" = None, swml_Entity8: set["swml_EnumTyp"] = None, swml_Entity10: set["swml_Attribute"] = None, swml_Entity12: set["swml_Reference"] = None, swml_Entity15: "swml_Entity" = None, swml_Entity13: set["swml_Entity"] = None, swml_Entity24: "swml_Reference" = None, swml_Entity35: "swml_dynamicPage" = None):
        self.name = name
        self.swml_Entity = swml_Entity
        self.swml_Entity8 = swml_Entity8 if swml_Entity8 is not None else set()
        self.swml_Entity10 = swml_Entity10 if swml_Entity10 is not None else set()
        self.swml_Entity12 = swml_Entity12 if swml_Entity12 is not None else set()
        self.swml_Entity15 = swml_Entity15
        self.swml_Entity13 = swml_Entity13 if swml_Entity13 is not None else set()
        self.swml_Entity24 = swml_Entity24
        self.swml_Entity35 = swml_Entity35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_Entity24(self):
        return self.__swml_Entity24

    @swml_Entity24.setter
    def swml_Entity24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity24", None)
        self.__swml_Entity24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Reference23"):
                opp_val = getattr(old_value, "swml_Reference23", None)
                if opp_val == self:
                    setattr(old_value, "swml_Reference23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Reference23"):
                opp_val = getattr(value, "swml_Reference23", None)
                setattr(value, "swml_Reference23", self)

    @property
    def swml_Entity13(self):
        return self.__swml_Entity13

    @swml_Entity13.setter
    def swml_Entity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity13", None)
        self.__swml_Entity13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_Entity15"):
                    opp_val = getattr(item, "swml_Entity15", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_Entity15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_Entity15"):
                    opp_val = getattr(item, "swml_Entity15", None)
                    
                    setattr(item, "swml_Entity15", self)
                    

    @property
    def swml_Entity12(self):
        return self.__swml_Entity12

    @swml_Entity12.setter
    def swml_Entity12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity12", None)
        self.__swml_Entity12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_Reference"):
                    opp_val = getattr(item, "swml_Reference", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_Reference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_Reference"):
                    opp_val = getattr(item, "swml_Reference", None)
                    
                    setattr(item, "swml_Reference", self)
                    

    @property
    def swml_Entity35(self):
        return self.__swml_Entity35

    @swml_Entity35.setter
    def swml_Entity35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity35", None)
        self.__swml_Entity35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_dynamicPage"):
                opp_val = getattr(old_value, "swml_dynamicPage", None)
                if opp_val == self:
                    setattr(old_value, "swml_dynamicPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_dynamicPage"):
                opp_val = getattr(value, "swml_dynamicPage", None)
                setattr(value, "swml_dynamicPage", self)

    @property
    def swml_Entity10(self):
        return self.__swml_Entity10

    @swml_Entity10.setter
    def swml_Entity10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity10", None)
        self.__swml_Entity10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_Attribute"):
                    opp_val = getattr(item, "swml_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_Attribute"):
                    opp_val = getattr(item, "swml_Attribute", None)
                    
                    setattr(item, "swml_Attribute", self)
                    

    @property
    def swml_Entity8(self):
        return self.__swml_Entity8

    @swml_Entity8.setter
    def swml_Entity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity8", None)
        self.__swml_Entity8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_EnumTyp"):
                    opp_val = getattr(item, "swml_EnumTyp", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_EnumTyp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_EnumTyp"):
                    opp_val = getattr(item, "swml_EnumTyp", None)
                    
                    setattr(item, "swml_EnumTyp", self)
                    

    @property
    def swml_Entity15(self):
        return self.__swml_Entity15

    @swml_Entity15.setter
    def swml_Entity15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity15", None)
        self.__swml_Entity15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_Entity13"):
                opp_val = getattr(old_value, "swml_Entity13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_Entity13"):
                opp_val = getattr(value, "swml_Entity13", None)
                if opp_val is None:
                    setattr(value, "swml_Entity13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_Entity(self):
        return self.__swml_Entity

    @swml_Entity.setter
    def swml_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Entity__swml_Entity", None)
        self.__swml_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_ContentModel6"):
                opp_val = getattr(old_value, "swml_ContentModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_ContentModel6"):
                opp_val = getattr(value, "swml_ContentModel6", None)
                if opp_val is None:
                    setattr(value, "swml_ContentModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swml_Enumeration:

    def __init__(self, name: str, swml_Enumeration: "swml_ContentModel" = None, swml_Enumeration18: "swml_EnumTyp" = None, swml_Enumeration26: set["swml_Literals"] = None):
        self.name = name
        self.swml_Enumeration = swml_Enumeration
        self.swml_Enumeration18 = swml_Enumeration18
        self.swml_Enumeration26 = swml_Enumeration26 if swml_Enumeration26 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def swml_Enumeration26(self):
        return self.__swml_Enumeration26

    @swml_Enumeration26.setter
    def swml_Enumeration26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Enumeration__swml_Enumeration26", None)
        self.__swml_Enumeration26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swml_Literals"):
                    opp_val = getattr(item, "swml_Literals", None)
                    
                    if opp_val == self:
                        setattr(item, "swml_Literals", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swml_Literals"):
                    opp_val = getattr(item, "swml_Literals", None)
                    
                    setattr(item, "swml_Literals", self)
                    

    @property
    def swml_Enumeration(self):
        return self.__swml_Enumeration

    @swml_Enumeration.setter
    def swml_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Enumeration__swml_Enumeration", None)
        self.__swml_Enumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_ContentModel4"):
                opp_val = getattr(old_value, "swml_ContentModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_ContentModel4"):
                opp_val = getattr(value, "swml_ContentModel4", None)
                if opp_val is None:
                    setattr(value, "swml_ContentModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swml_Enumeration18(self):
        return self.__swml_Enumeration18

    @swml_Enumeration18.setter
    def swml_Enumeration18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swml_Enumeration__swml_Enumeration18", None)
        self.__swml_Enumeration18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swml_EnumTyp17"):
                opp_val = getattr(old_value, "swml_EnumTyp17", None)
                if opp_val == self:
                    setattr(old_value, "swml_EnumTyp17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swml_EnumTyp17"):
                opp_val = getattr(value, "swml_EnumTyp17", None)
                setattr(value, "swml_EnumTyp17", self)

class swml_ContentModel:

    pass
class swml_HypertextModel:

    pass
class swml_WebModel:

    pass