from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class hello122_Child:

    def __init__(self, id: str, hello122_Child: "hello122_Top" = None):
        self.id = id
        self.hello122_Child = hello122_Child
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def hello122_Child(self):
        return self.__hello122_Child

    @hello122_Child.setter
    def hello122_Child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Child__hello122_Child", None)
        self.__hello122_Child = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Top37"):
                opp_val = getattr(old_value, "hello122_Top37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Top37"):
                opp_val = getattr(value, "hello122_Top37", None)
                if opp_val is None:
                    setattr(value, "hello122_Top37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hello122_Alias:

    def __init__(self, id: str, hello122_Alias: "hello122_NamedElement" = None):
        self.id = id
        self.hello122_Alias = hello122_Alias
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def hello122_Alias(self):
        return self.__hello122_Alias

    @hello122_Alias.setter
    def hello122_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Alias__hello122_Alias", None)
        self.__hello122_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_NamedElement"):
                opp_val = getattr(old_value, "hello122_NamedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_NamedElement"):
                opp_val = getattr(value, "hello122_NamedElement", None)
                if opp_val is None:
                    setattr(value, "hello122_NamedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hello122_NamedElement(ABC):

    def __init__(self, name: str, hello122_NamedElement: set["hello122_Alias"] = None):
        self.name = name
        self.hello122_NamedElement = hello122_NamedElement if hello122_NamedElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hello122_NamedElement(self):
        return self.__hello122_NamedElement

    @hello122_NamedElement.setter
    def hello122_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_NamedElement__hello122_NamedElement", None)
        self.__hello122_NamedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello122_Alias"):
                    opp_val = getattr(item, "hello122_Alias", None)
                    
                    if opp_val == self:
                        setattr(item, "hello122_Alias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello122_Alias"):
                    opp_val = getattr(item, "hello122_Alias", None)
                    
                    setattr(item, "hello122_Alias", self)
                    

class hello122_Third:

    def __init__(self, id: str, hello122_Third: "hello122_Thing" = None, hello122_Third23: "hello122_Classoc" = None, hello122_Third35: "hello122_Clazoc" = None):
        self.id = id
        self.hello122_Third = hello122_Third
        self.hello122_Third23 = hello122_Third23
        self.hello122_Third35 = hello122_Third35
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def hello122_Third23(self):
        return self.__hello122_Third23

    @hello122_Third23.setter
    def hello122_Third23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Third__hello122_Third23", None)
        self.__hello122_Third23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Classoc22"):
                opp_val = getattr(old_value, "hello122_Classoc22", None)
                if opp_val == self:
                    setattr(old_value, "hello122_Classoc22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Classoc22"):
                opp_val = getattr(value, "hello122_Classoc22", None)
                setattr(value, "hello122_Classoc22", self)

    @property
    def hello122_Third(self):
        return self.__hello122_Third

    @hello122_Third.setter
    def hello122_Third(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Third__hello122_Third", None)
        self.__hello122_Third = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Thing8"):
                opp_val = getattr(old_value, "hello122_Thing8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Thing8"):
                opp_val = getattr(value, "hello122_Thing8", None)
                if opp_val is None:
                    setattr(value, "hello122_Thing8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hello122_Third35(self):
        return self.__hello122_Third35

    @hello122_Third35.setter
    def hello122_Third35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Third__hello122_Third35", None)
        self.__hello122_Third35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Clazoc34"):
                opp_val = getattr(old_value, "hello122_Clazoc34", None)
                if opp_val == self:
                    setattr(old_value, "hello122_Clazoc34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Clazoc34"):
                opp_val = getattr(value, "hello122_Clazoc34", None)
                setattr(value, "hello122_Clazoc34", self)

class NamedElement:

    pass
class hello122_Clazoc(NamedElement):

    pass
class hello122_RelatedTo(NamedElement):

    def __init__(self, since: str, hello122_RelatedTo: "hello122_Thing" = None, hello122_RelatedTo16: "hello122_Thing" = None, hello122_RelatedTo19: "hello122_Thing" = None):
        self.since = since
        self.hello122_RelatedTo = hello122_RelatedTo
        self.hello122_RelatedTo16 = hello122_RelatedTo16
        self.hello122_RelatedTo19 = hello122_RelatedTo19
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def hello122_RelatedTo(self):
        return self.__hello122_RelatedTo

    @hello122_RelatedTo.setter
    def hello122_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_RelatedTo__hello122_RelatedTo", None)
        self.__hello122_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Thing13"):
                opp_val = getattr(old_value, "hello122_Thing13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Thing13"):
                opp_val = getattr(value, "hello122_Thing13", None)
                if opp_val is None:
                    setattr(value, "hello122_Thing13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hello122_RelatedTo19(self):
        return self.__hello122_RelatedTo19

    @hello122_RelatedTo19.setter
    def hello122_RelatedTo19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_RelatedTo__hello122_RelatedTo19", None)
        self.__hello122_RelatedTo19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Thing20"):
                opp_val = getattr(old_value, "hello122_Thing20", None)
                if opp_val == self:
                    setattr(old_value, "hello122_Thing20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Thing20"):
                opp_val = getattr(value, "hello122_Thing20", None)
                setattr(value, "hello122_Thing20", self)

    @property
    def hello122_RelatedTo16(self):
        return self.__hello122_RelatedTo16

    @hello122_RelatedTo16.setter
    def hello122_RelatedTo16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_RelatedTo__hello122_RelatedTo16", None)
        self.__hello122_RelatedTo16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Thing17"):
                opp_val = getattr(old_value, "hello122_Thing17", None)
                if opp_val == self:
                    setattr(old_value, "hello122_Thing17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Thing17"):
                opp_val = getattr(value, "hello122_Thing17", None)
                setattr(value, "hello122_Thing17", self)

class hello122_Top:

    def __init__(self, id: str, hello122_Top: "hello122_Base" = None, hello122_Top37: set["hello122_Child"] = None):
        self.id = id
        self.hello122_Top = hello122_Top
        self.hello122_Top37 = hello122_Top37 if hello122_Top37 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def hello122_Top(self):
        return self.__hello122_Top

    @hello122_Top.setter
    def hello122_Top(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Top__hello122_Top", None)
        self.__hello122_Top = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Base6"):
                opp_val = getattr(old_value, "hello122_Base6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Base6"):
                opp_val = getattr(value, "hello122_Base6", None)
                if opp_val is None:
                    setattr(value, "hello122_Base6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hello122_Top37(self):
        return self.__hello122_Top37

    @hello122_Top37.setter
    def hello122_Top37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Top__hello122_Top37", None)
        self.__hello122_Top37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello122_Child"):
                    opp_val = getattr(item, "hello122_Child", None)
                    
                    if opp_val == self:
                        setattr(item, "hello122_Child", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello122_Child"):
                    opp_val = getattr(item, "hello122_Child", None)
                    
                    setattr(item, "hello122_Child", self)
                    

class hello122_Classoc:

    def __init__(self, id: str, hello122_Classoc: "hello122_Base" = None, hello122_Classoc11: "hello122_Thing" = None, hello122_Classoc22: "hello122_Third" = None, hello122_Classoc25: "hello122_Base" = None, hello122_Classoc28: "hello122_Thing" = None):
        self.id = id
        self.hello122_Classoc = hello122_Classoc
        self.hello122_Classoc11 = hello122_Classoc11
        self.hello122_Classoc22 = hello122_Classoc22
        self.hello122_Classoc25 = hello122_Classoc25
        self.hello122_Classoc28 = hello122_Classoc28
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def hello122_Classoc11(self):
        return self.__hello122_Classoc11

    @hello122_Classoc11.setter
    def hello122_Classoc11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Classoc__hello122_Classoc11", None)
        self.__hello122_Classoc11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Thing10"):
                opp_val = getattr(old_value, "hello122_Thing10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Thing10"):
                opp_val = getattr(value, "hello122_Thing10", None)
                if opp_val is None:
                    setattr(value, "hello122_Thing10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hello122_Classoc25(self):
        return self.__hello122_Classoc25

    @hello122_Classoc25.setter
    def hello122_Classoc25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Classoc__hello122_Classoc25", None)
        self.__hello122_Classoc25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Base26"):
                opp_val = getattr(old_value, "hello122_Base26", None)
                if opp_val == self:
                    setattr(old_value, "hello122_Base26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Base26"):
                opp_val = getattr(value, "hello122_Base26", None)
                setattr(value, "hello122_Base26", self)

    @property
    def hello122_Classoc(self):
        return self.__hello122_Classoc

    @hello122_Classoc.setter
    def hello122_Classoc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Classoc__hello122_Classoc", None)
        self.__hello122_Classoc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Base2"):
                opp_val = getattr(old_value, "hello122_Base2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Base2"):
                opp_val = getattr(value, "hello122_Base2", None)
                if opp_val is None:
                    setattr(value, "hello122_Base2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hello122_Classoc22(self):
        return self.__hello122_Classoc22

    @hello122_Classoc22.setter
    def hello122_Classoc22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Classoc__hello122_Classoc22", None)
        self.__hello122_Classoc22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Third23"):
                opp_val = getattr(old_value, "hello122_Third23", None)
                if opp_val == self:
                    setattr(old_value, "hello122_Third23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Third23"):
                opp_val = getattr(value, "hello122_Third23", None)
                setattr(value, "hello122_Third23", self)

    @property
    def hello122_Classoc28(self):
        return self.__hello122_Classoc28

    @hello122_Classoc28.setter
    def hello122_Classoc28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Classoc__hello122_Classoc28", None)
        self.__hello122_Classoc28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Thing29"):
                opp_val = getattr(old_value, "hello122_Thing29", None)
                if opp_val == self:
                    setattr(old_value, "hello122_Thing29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Thing29"):
                opp_val = getattr(value, "hello122_Thing29", None)
                setattr(value, "hello122_Thing29", self)

class hello122_Thing(NamedElement):

    def __init__(self, id: int, hello122_Thing: "hello122_Base" = None, hello122_Thing8: set["hello122_Third"] = None, hello122_Thing10: set["hello122_Classoc"] = None, hello122_Thing13: set["hello122_RelatedTo"] = None, hello122_Thing17: "hello122_RelatedTo" = None, hello122_Thing20: "hello122_RelatedTo" = None, hello122_Thing29: "hello122_Classoc" = None, hello122_Thing32: "hello122_Clazoc" = None):
        self.id = id
        self.hello122_Thing = hello122_Thing
        self.hello122_Thing8 = hello122_Thing8 if hello122_Thing8 is not None else set()
        self.hello122_Thing10 = hello122_Thing10 if hello122_Thing10 is not None else set()
        self.hello122_Thing13 = hello122_Thing13 if hello122_Thing13 is not None else set()
        self.hello122_Thing17 = hello122_Thing17
        self.hello122_Thing20 = hello122_Thing20
        self.hello122_Thing29 = hello122_Thing29
        self.hello122_Thing32 = hello122_Thing32
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def hello122_Thing32(self):
        return self.__hello122_Thing32

    @hello122_Thing32.setter
    def hello122_Thing32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Thing__hello122_Thing32", None)
        self.__hello122_Thing32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Clazoc31"):
                opp_val = getattr(old_value, "hello122_Clazoc31", None)
                if opp_val == self:
                    setattr(old_value, "hello122_Clazoc31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Clazoc31"):
                opp_val = getattr(value, "hello122_Clazoc31", None)
                setattr(value, "hello122_Clazoc31", self)

    @property
    def hello122_Thing10(self):
        return self.__hello122_Thing10

    @hello122_Thing10.setter
    def hello122_Thing10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Thing__hello122_Thing10", None)
        self.__hello122_Thing10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello122_Classoc11"):
                    opp_val = getattr(item, "hello122_Classoc11", None)
                    
                    if opp_val == self:
                        setattr(item, "hello122_Classoc11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello122_Classoc11"):
                    opp_val = getattr(item, "hello122_Classoc11", None)
                    
                    setattr(item, "hello122_Classoc11", self)
                    

    @property
    def hello122_Thing(self):
        return self.__hello122_Thing

    @hello122_Thing.setter
    def hello122_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Thing__hello122_Thing", None)
        self.__hello122_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Base"):
                opp_val = getattr(old_value, "hello122_Base", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Base"):
                opp_val = getattr(value, "hello122_Base", None)
                if opp_val is None:
                    setattr(value, "hello122_Base", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hello122_Thing29(self):
        return self.__hello122_Thing29

    @hello122_Thing29.setter
    def hello122_Thing29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Thing__hello122_Thing29", None)
        self.__hello122_Thing29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_Classoc28"):
                opp_val = getattr(old_value, "hello122_Classoc28", None)
                if opp_val == self:
                    setattr(old_value, "hello122_Classoc28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_Classoc28"):
                opp_val = getattr(value, "hello122_Classoc28", None)
                setattr(value, "hello122_Classoc28", self)

    @property
    def hello122_Thing20(self):
        return self.__hello122_Thing20

    @hello122_Thing20.setter
    def hello122_Thing20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Thing__hello122_Thing20", None)
        self.__hello122_Thing20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_RelatedTo19"):
                opp_val = getattr(old_value, "hello122_RelatedTo19", None)
                if opp_val == self:
                    setattr(old_value, "hello122_RelatedTo19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_RelatedTo19"):
                opp_val = getattr(value, "hello122_RelatedTo19", None)
                setattr(value, "hello122_RelatedTo19", self)

    @property
    def hello122_Thing13(self):
        return self.__hello122_Thing13

    @hello122_Thing13.setter
    def hello122_Thing13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Thing__hello122_Thing13", None)
        self.__hello122_Thing13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello122_RelatedTo"):
                    opp_val = getattr(item, "hello122_RelatedTo", None)
                    
                    if opp_val == self:
                        setattr(item, "hello122_RelatedTo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello122_RelatedTo"):
                    opp_val = getattr(item, "hello122_RelatedTo", None)
                    
                    setattr(item, "hello122_RelatedTo", self)
                    

    @property
    def hello122_Thing17(self):
        return self.__hello122_Thing17

    @hello122_Thing17.setter
    def hello122_Thing17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Thing__hello122_Thing17", None)
        self.__hello122_Thing17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hello122_RelatedTo16"):
                opp_val = getattr(old_value, "hello122_RelatedTo16", None)
                if opp_val == self:
                    setattr(old_value, "hello122_RelatedTo16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hello122_RelatedTo16"):
                opp_val = getattr(value, "hello122_RelatedTo16", None)
                setattr(value, "hello122_RelatedTo16", self)

    @property
    def hello122_Thing8(self):
        return self.__hello122_Thing8

    @hello122_Thing8.setter
    def hello122_Thing8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hello122_Thing__hello122_Thing8", None)
        self.__hello122_Thing8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hello122_Third"):
                    opp_val = getattr(item, "hello122_Third", None)
                    
                    if opp_val == self:
                        setattr(item, "hello122_Third", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hello122_Third"):
                    opp_val = getattr(item, "hello122_Third", None)
                    
                    setattr(item, "hello122_Third", self)
                    

class hello122_Base:

    pass