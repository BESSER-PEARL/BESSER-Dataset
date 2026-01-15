from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class webGui_Add(Expression):

    pass
class webGui_Subtract(Expression):

    pass
class webGui_Divide(Expression):

    pass
class webGui_Value(Expression):

    pass
class webGui_DomainPathTail:

    pass
class webGui_Multiply(Expression):

    pass
class PageElement:

    pass
class webGui_DisplayElement(PageElement):

    pass
class webGui_ActionElement(PageElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class webGui_PageElement:

    pass
class webGui_Page:

    def __init__(self, name: str, title: str, webGui_Page: "webGui_WebModel" = None, webGui_Page14: "webGui_Entity" = None, webGui_Page17: set["webGui_PageElement"] = None):
        self.name = name
        self.title = title
        self.webGui_Page = webGui_Page
        self.webGui_Page14 = webGui_Page14
        self.webGui_Page17 = webGui_Page17 if webGui_Page17 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def webGui_Page(self):
        return self.__webGui_Page

    @webGui_Page.setter
    def webGui_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Page__webGui_Page", None)
        self.__webGui_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webGui_WebModel12"):
                opp_val = getattr(old_value, "webGui_WebModel12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webGui_WebModel12"):
                opp_val = getattr(value, "webGui_WebModel12", None)
                if opp_val is None:
                    setattr(value, "webGui_WebModel12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webGui_Page14(self):
        return self.__webGui_Page14

    @webGui_Page14.setter
    def webGui_Page14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Page__webGui_Page14", None)
        self.__webGui_Page14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webGui_Entity15"):
                opp_val = getattr(old_value, "webGui_Entity15", None)
                if opp_val == self:
                    setattr(old_value, "webGui_Entity15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webGui_Entity15"):
                opp_val = getattr(value, "webGui_Entity15", None)
                setattr(value, "webGui_Entity15", self)

    @property
    def webGui_Page17(self):
        return self.__webGui_Page17

    @webGui_Page17.setter
    def webGui_Page17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Page__webGui_Page17", None)
        self.__webGui_Page17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webGui_PageElement"):
                    opp_val = getattr(item, "webGui_PageElement", None)
                    
                    if opp_val == self:
                        setattr(item, "webGui_PageElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webGui_PageElement"):
                    opp_val = getattr(item, "webGui_PageElement", None)
                    
                    setattr(item, "webGui_PageElement", self)
                    

class webGui_Expression:

    pass
class Value:

    pass
class webGui_NumberLiteral(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class webGui_DomainPath(Value):

    pass
class webGui_Feature:

    def __init__(self, name: str, multivalued: bool, webGui_Feature7: "webGui_Type" = None, webGui_Feature: "webGui_Entity" = None, webGui_Feature21: "webGui_DomainPath" = None, webGui_Feature10: "webGui_Expression" = None, webGui_Feature26: "webGui_DomainPathTail" = None):
        self.name = name
        self.multivalued = multivalued
        self.webGui_Feature7 = webGui_Feature7
        self.webGui_Feature = webGui_Feature
        self.webGui_Feature21 = webGui_Feature21
        self.webGui_Feature10 = webGui_Feature10
        self.webGui_Feature26 = webGui_Feature26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

    @property
    def webGui_Feature(self):
        return self.__webGui_Feature

    @webGui_Feature.setter
    def webGui_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Feature__webGui_Feature", None)
        self.__webGui_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webGui_Entity"):
                opp_val = getattr(old_value, "webGui_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webGui_Entity"):
                opp_val = getattr(value, "webGui_Entity", None)
                if opp_val is None:
                    setattr(value, "webGui_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webGui_Feature7(self):
        return self.__webGui_Feature7

    @webGui_Feature7.setter
    def webGui_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Feature__webGui_Feature7", None)
        self.__webGui_Feature7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webGui_Type8"):
                opp_val = getattr(old_value, "webGui_Type8", None)
                if opp_val == self:
                    setattr(old_value, "webGui_Type8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webGui_Type8"):
                opp_val = getattr(value, "webGui_Type8", None)
                setattr(value, "webGui_Type8", self)

    @property
    def webGui_Feature21(self):
        return self.__webGui_Feature21

    @webGui_Feature21.setter
    def webGui_Feature21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Feature__webGui_Feature21", None)
        self.__webGui_Feature21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webGui_DomainPath20"):
                opp_val = getattr(old_value, "webGui_DomainPath20", None)
                if opp_val == self:
                    setattr(old_value, "webGui_DomainPath20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webGui_DomainPath20"):
                opp_val = getattr(value, "webGui_DomainPath20", None)
                setattr(value, "webGui_DomainPath20", self)

    @property
    def webGui_Feature10(self):
        return self.__webGui_Feature10

    @webGui_Feature10.setter
    def webGui_Feature10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Feature__webGui_Feature10", None)
        self.__webGui_Feature10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webGui_Expression"):
                opp_val = getattr(old_value, "webGui_Expression", None)
                if opp_val == self:
                    setattr(old_value, "webGui_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webGui_Expression"):
                opp_val = getattr(value, "webGui_Expression", None)
                setattr(value, "webGui_Expression", self)

    @property
    def webGui_Feature26(self):
        return self.__webGui_Feature26

    @webGui_Feature26.setter
    def webGui_Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Feature__webGui_Feature26", None)
        self.__webGui_Feature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webGui_DomainPathTail25"):
                opp_val = getattr(old_value, "webGui_DomainPathTail25", None)
                if opp_val == self:
                    setattr(old_value, "webGui_DomainPathTail25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webGui_DomainPathTail25"):
                opp_val = getattr(value, "webGui_DomainPathTail25", None)
                setattr(value, "webGui_DomainPathTail25", self)

class Type:

    pass
class webGui_DataType(Type):

    pass
class webGui_Entity(Type):

    pass
class webGui_Type:

    def __init__(self, name: str, webGui_Type8: "webGui_Feature" = None, webGui_Type: "webGui_DomainModel" = None):
        self.name = name
        self.webGui_Type8 = webGui_Type8
        self.webGui_Type = webGui_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def webGui_Type8(self):
        return self.__webGui_Type8

    @webGui_Type8.setter
    def webGui_Type8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Type__webGui_Type8", None)
        self.__webGui_Type8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webGui_Feature7"):
                opp_val = getattr(old_value, "webGui_Feature7", None)
                if opp_val == self:
                    setattr(old_value, "webGui_Feature7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webGui_Feature7"):
                opp_val = getattr(value, "webGui_Feature7", None)
                setattr(value, "webGui_Feature7", self)

    @property
    def webGui_Type(self):
        return self.__webGui_Type

    @webGui_Type.setter
    def webGui_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Type__webGui_Type", None)
        self.__webGui_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webGui_DomainModel4"):
                opp_val = getattr(old_value, "webGui_DomainModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webGui_DomainModel4"):
                opp_val = getattr(value, "webGui_DomainModel4", None)
                if opp_val is None:
                    setattr(value, "webGui_DomainModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webGui_WebModel:

    pass
class webGui_DomainModel:

    pass
class webGui_Model:

    def __init__(self, name: str, webGui_Model: "webGui_DomainModel" = None, webGui_Model2: "webGui_WebModel" = None):
        self.name = name
        self.webGui_Model = webGui_Model
        self.webGui_Model2 = webGui_Model2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def webGui_Model(self):
        return self.__webGui_Model

    @webGui_Model.setter
    def webGui_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Model__webGui_Model", None)
        self.__webGui_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webGui_DomainModel"):
                opp_val = getattr(old_value, "webGui_DomainModel", None)
                if opp_val == self:
                    setattr(old_value, "webGui_DomainModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webGui_DomainModel"):
                opp_val = getattr(value, "webGui_DomainModel", None)
                setattr(value, "webGui_DomainModel", self)

    @property
    def webGui_Model2(self):
        return self.__webGui_Model2

    @webGui_Model2.setter
    def webGui_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webGui_Model__webGui_Model2", None)
        self.__webGui_Model2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webGui_WebModel"):
                opp_val = getattr(old_value, "webGui_WebModel", None)
                if opp_val == self:
                    setattr(old_value, "webGui_WebModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webGui_WebModel"):
                opp_val = getattr(value, "webGui_WebModel", None)
                setattr(value, "webGui_WebModel", self)
