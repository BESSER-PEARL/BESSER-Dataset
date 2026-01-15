from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EType(Enum):
    integer = "integer"
    string = "string"
class EVisibility(Enum):
    public = "public"
    protected = "protected"
    private = "private"
class EReturnType(Enum):
    void = "void"
    integer = "integer"
    string = "string"


############################################
# Definition of Classes
############################################

class myumlclassdiagram_NamedElement(ABC):

    def __init__(self, Name: str):
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

class NamedElement:

    pass
class myumlclassdiagram_Class(NamedElement):

    def __init__(self, Visibility: str, myumlclassdiagram_Class: "myumlclassdiagram_Package" = None, Owner: set["myumlclassdiagram_Attribute"] = None, Owner3: set["myumlclassdiagram_Method"] = None, Class: "myumlclassdiagram_Attribute" = None, Class8: "myumlclassdiagram_Method" = None):
        self.Visibility = Visibility
        self.myumlclassdiagram_Class = myumlclassdiagram_Class
        self.Owner = Owner if Owner is not None else set()
        self.Owner3 = Owner3 if Owner3 is not None else set()
        self.Class = Class
        self.Class8 = Class8
        
    @property
    def Visibility(self) -> str:
        return self.__Visibility

    @Visibility.setter
    def Visibility(self, Visibility: str):
        self.__Visibility = Visibility

    @property
    def myumlclassdiagram_Class(self):
        return self.__myumlclassdiagram_Class

    @myumlclassdiagram_Class.setter
    def myumlclassdiagram_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Class__myumlclassdiagram_Class", None)
        self.__myumlclassdiagram_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myumlclassdiagram_Package"):
                opp_val = getattr(old_value, "myumlclassdiagram_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myumlclassdiagram_Package"):
                opp_val = getattr(value, "myumlclassdiagram_Package", None)
                if opp_val is None:
                    setattr(value, "myumlclassdiagram_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Owner3(self):
        return self.__Owner3

    @Owner3.setter
    def Owner3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Class__Owner3", None)
        self.__Owner3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    setattr(item, "Method", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attributes"):
                opp_val = getattr(old_value, "Attributes", None)
                if opp_val == self:
                    setattr(old_value, "Attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attributes"):
                opp_val = getattr(value, "Attributes", None)
                setattr(value, "Attributes", self)

    @property
    def Class8(self):
        return self.__Class8

    @Class8.setter
    def Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Class__Class8", None)
        self.__Class8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Methods"):
                opp_val = getattr(old_value, "Methods", None)
                if opp_val == self:
                    setattr(old_value, "Methods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Methods"):
                opp_val = getattr(value, "Methods", None)
                setattr(value, "Methods", self)

    @property
    def Owner(self):
        return self.__Owner

    @Owner.setter
    def Owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Class__Owner", None)
        self.__Owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

class myumlclassdiagram_Method(NamedElement):

    def __init__(self, Returns: str, Visibility: str, Method: "myumlclassdiagram_Class" = None, Owner6: set["myumlclassdiagram_Parameter"] = None, Methods: "myumlclassdiagram_Class" = None, Method10: "myumlclassdiagram_Parameter" = None):
        self.Returns = Returns
        self.Visibility = Visibility
        self.Method = Method
        self.Owner6 = Owner6 if Owner6 is not None else set()
        self.Methods = Methods
        self.Method10 = Method10
        
    @property
    def Visibility(self) -> str:
        return self.__Visibility

    @Visibility.setter
    def Visibility(self, Visibility: str):
        self.__Visibility = Visibility

    @property
    def Returns(self) -> str:
        return self.__Returns

    @Returns.setter
    def Returns(self, Returns: str):
        self.__Returns = Returns

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Method__Method", None)
        self.__Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Owner3"):
                opp_val = getattr(old_value, "Owner3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Owner3"):
                opp_val = getattr(value, "Owner3", None)
                if opp_val is None:
                    setattr(value, "Owner3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Method10(self):
        return self.__Method10

    @Method10.setter
    def Method10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Method__Method10", None)
        self.__Method10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameters"):
                opp_val = getattr(old_value, "Parameters", None)
                if opp_val == self:
                    setattr(old_value, "Parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameters"):
                opp_val = getattr(value, "Parameters", None)
                setattr(value, "Parameters", self)

    @property
    def Owner6(self):
        return self.__Owner6

    @Owner6.setter
    def Owner6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Method__Owner6", None)
        self.__Owner6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def Methods(self):
        return self.__Methods

    @Methods.setter
    def Methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Method__Methods", None)
        self.__Methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class8"):
                opp_val = getattr(old_value, "Class8", None)
                if opp_val == self:
                    setattr(old_value, "Class8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class8"):
                opp_val = getattr(value, "Class8", None)
                setattr(value, "Class8", self)

class myumlclassdiagram_Parameter(NamedElement):

    def __init__(self, Type: str, Parameter: "myumlclassdiagram_Method" = None, Parameters: "myumlclassdiagram_Method" = None):
        self.Type = Type
        self.Parameter = Parameter
        self.Parameters = Parameters
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Owner6"):
                opp_val = getattr(old_value, "Owner6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Owner6"):
                opp_val = getattr(value, "Owner6", None)
                if opp_val is None:
                    setattr(value, "Owner6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Parameters(self):
        return self.__Parameters

    @Parameters.setter
    def Parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Parameter__Parameters", None)
        self.__Parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Method10"):
                opp_val = getattr(old_value, "Method10", None)
                if opp_val == self:
                    setattr(old_value, "Method10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Method10"):
                opp_val = getattr(value, "Method10", None)
                setattr(value, "Method10", self)

class myumlclassdiagram_Attribute(NamedElement):

    def __init__(self, Type: str, Visibility: str, Attribute: "myumlclassdiagram_Class" = None, Attributes: "myumlclassdiagram_Class" = None):
        self.Type = Type
        self.Visibility = Visibility
        self.Attribute = Attribute
        self.Attributes = Attributes
        
    @property
    def Visibility(self) -> str:
        return self.__Visibility

    @Visibility.setter
    def Visibility(self, Visibility: str):
        self.__Visibility = Visibility

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Owner"):
                opp_val = getattr(old_value, "Owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Owner"):
                opp_val = getattr(value, "Owner", None)
                if opp_val is None:
                    setattr(value, "Owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Attributes(self):
        return self.__Attributes

    @Attributes.setter
    def Attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myumlclassdiagram_Attribute__Attributes", None)
        self.__Attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

class myumlclassdiagram_Package(NamedElement):

    pass