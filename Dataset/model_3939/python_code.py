from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ButtonKind(Enum):
    createEdit = "createEdit"
    delete = "delete"
    cancel = "cancel"
class MultiplicityKind(Enum):
    Single = "Single"
    Multiple = "Multiple"
class AttributeType(Enum):
    Integer = "Integer"
    Date = "Date"
    String = "String"


############################################
# Definition of Classes
############################################

class UIElement:

    pass
class myDsl01_Button(UIElement):

    def __init__(self, kind: str, text: str):
        self.kind = kind
        self.text = text
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class myDsl01_Field(UIElement):

    pass
class myDsl01_Label(UIElement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class myDsl01_Bounds:

    def __init__(self, x: int, y: int, width: int, height: int, myDsl01_Bounds: "myDsl01_UIElement" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.myDsl01_Bounds = myDsl01_Bounds
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def myDsl01_Bounds(self):
        return self.__myDsl01_Bounds

    @myDsl01_Bounds.setter
    def myDsl01_Bounds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Bounds__myDsl01_Bounds", None)
        self.__myDsl01_Bounds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_UIElement20"):
                opp_val = getattr(old_value, "myDsl01_UIElement20", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_UIElement20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_UIElement20"):
                opp_val = getattr(value, "myDsl01_UIElement20", None)
                setattr(value, "myDsl01_UIElement20", self)

class myDsl01_UIElement:

    def __init__(self, name: str, myDsl01_UIElement: "myDsl01_EntryWindow" = None, myDsl01_UIElement20: "myDsl01_Bounds" = None):
        self.name = name
        self.myDsl01_UIElement = myDsl01_UIElement
        self.myDsl01_UIElement20 = myDsl01_UIElement20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl01_UIElement(self):
        return self.__myDsl01_UIElement

    @myDsl01_UIElement.setter
    def myDsl01_UIElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_UIElement__myDsl01_UIElement", None)
        self.__myDsl01_UIElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_EntryWindow"):
                opp_val = getattr(old_value, "myDsl01_EntryWindow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_EntryWindow"):
                opp_val = getattr(value, "myDsl01_EntryWindow", None)
                if opp_val is None:
                    setattr(value, "myDsl01_EntryWindow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl01_UIElement20(self):
        return self.__myDsl01_UIElement20

    @myDsl01_UIElement20.setter
    def myDsl01_UIElement20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_UIElement__myDsl01_UIElement20", None)
        self.__myDsl01_UIElement20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Bounds"):
                opp_val = getattr(old_value, "myDsl01_Bounds", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Bounds", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Bounds"):
                opp_val = getattr(value, "myDsl01_Bounds", None)
                setattr(value, "myDsl01_Bounds", self)

class Window:

    pass
class myDsl01_EntryWindow(Window):

    pass
class myDsl01_ListWindow(Window):

    pass
class myDsl01_Size:

    def __init__(self, width: int, height: int, myDsl01_Size: "myDsl01_Window" = None):
        self.width = width
        self.height = height
        self.myDsl01_Size = myDsl01_Size
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def myDsl01_Size(self):
        return self.__myDsl01_Size

    @myDsl01_Size.setter
    def myDsl01_Size(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Size__myDsl01_Size", None)
        self.__myDsl01_Size = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Window17"):
                opp_val = getattr(old_value, "myDsl01_Window17", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Window17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Window17"):
                opp_val = getattr(value, "myDsl01_Window17", None)
                setattr(value, "myDsl01_Window17", self)

class Property:

    pass
class myDsl01_Attribute(Property):

    def __init__(self, type: str, optional: bool):
        self.type = type
        self.optional = optional
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

class myDsl01_Property:

    def __init__(self, name: str, myDsl01_Property: "myDsl01_Entity" = None, myDsl01_Property22: "myDsl01_Field" = None):
        self.name = name
        self.myDsl01_Property = myDsl01_Property
        self.myDsl01_Property22 = myDsl01_Property22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl01_Property(self):
        return self.__myDsl01_Property

    @myDsl01_Property.setter
    def myDsl01_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Property__myDsl01_Property", None)
        self.__myDsl01_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Entity7"):
                opp_val = getattr(old_value, "myDsl01_Entity7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Entity7"):
                opp_val = getattr(value, "myDsl01_Entity7", None)
                if opp_val is None:
                    setattr(value, "myDsl01_Entity7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl01_Property22(self):
        return self.__myDsl01_Property22

    @myDsl01_Property22.setter
    def myDsl01_Property22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Property__myDsl01_Property22", None)
        self.__myDsl01_Property22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Field"):
                opp_val = getattr(old_value, "myDsl01_Field", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Field", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Field"):
                opp_val = getattr(value, "myDsl01_Field", None)
                setattr(value, "myDsl01_Field", self)

class myDsl01_Window:

    def __init__(self, name: str, title: str, myDsl01_Window: "myDsl01_Model" = None, myDsl01_Window14: "myDsl01_Entity" = None, myDsl01_Window17: "myDsl01_Size" = None):
        self.name = name
        self.title = title
        self.myDsl01_Window = myDsl01_Window
        self.myDsl01_Window14 = myDsl01_Window14
        self.myDsl01_Window17 = myDsl01_Window17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def myDsl01_Window14(self):
        return self.__myDsl01_Window14

    @myDsl01_Window14.setter
    def myDsl01_Window14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Window__myDsl01_Window14", None)
        self.__myDsl01_Window14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Entity15"):
                opp_val = getattr(old_value, "myDsl01_Entity15", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Entity15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Entity15"):
                opp_val = getattr(value, "myDsl01_Entity15", None)
                setattr(value, "myDsl01_Entity15", self)

    @property
    def myDsl01_Window(self):
        return self.__myDsl01_Window

    @myDsl01_Window.setter
    def myDsl01_Window(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Window__myDsl01_Window", None)
        self.__myDsl01_Window = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Model2"):
                opp_val = getattr(old_value, "myDsl01_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Model2"):
                opp_val = getattr(value, "myDsl01_Model2", None)
                if opp_val is None:
                    setattr(value, "myDsl01_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl01_Window17(self):
        return self.__myDsl01_Window17

    @myDsl01_Window17.setter
    def myDsl01_Window17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Window__myDsl01_Window17", None)
        self.__myDsl01_Window17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Size"):
                opp_val = getattr(old_value, "myDsl01_Size", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Size", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Size"):
                opp_val = getattr(value, "myDsl01_Size", None)
                setattr(value, "myDsl01_Size", self)

class myDsl01_Entity:

    def __init__(self, abstract: bool, name: str, myDsl01_Entity: "myDsl01_Model" = None, myDsl01_Entity5: "myDsl01_Entity" = None, myDsl01_Entity3: "myDsl01_Entity" = None, myDsl01_Entity7: set["myDsl01_Property"] = None, myDsl01_Entity9: "myDsl01_Reference" = None, myDsl01_Entity15: "myDsl01_Window" = None):
        self.abstract = abstract
        self.name = name
        self.myDsl01_Entity = myDsl01_Entity
        self.myDsl01_Entity5 = myDsl01_Entity5
        self.myDsl01_Entity3 = myDsl01_Entity3
        self.myDsl01_Entity7 = myDsl01_Entity7 if myDsl01_Entity7 is not None else set()
        self.myDsl01_Entity9 = myDsl01_Entity9
        self.myDsl01_Entity15 = myDsl01_Entity15
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl01_Entity9(self):
        return self.__myDsl01_Entity9

    @myDsl01_Entity9.setter
    def myDsl01_Entity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Entity__myDsl01_Entity9", None)
        self.__myDsl01_Entity9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Reference"):
                opp_val = getattr(old_value, "myDsl01_Reference", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Reference"):
                opp_val = getattr(value, "myDsl01_Reference", None)
                setattr(value, "myDsl01_Reference", self)

    @property
    def myDsl01_Entity7(self):
        return self.__myDsl01_Entity7

    @myDsl01_Entity7.setter
    def myDsl01_Entity7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Entity__myDsl01_Entity7", None)
        self.__myDsl01_Entity7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl01_Property"):
                    opp_val = getattr(item, "myDsl01_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl01_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl01_Property"):
                    opp_val = getattr(item, "myDsl01_Property", None)
                    
                    setattr(item, "myDsl01_Property", self)
                    

    @property
    def myDsl01_Entity5(self):
        return self.__myDsl01_Entity5

    @myDsl01_Entity5.setter
    def myDsl01_Entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Entity__myDsl01_Entity5", None)
        self.__myDsl01_Entity5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Entity3"):
                opp_val = getattr(old_value, "myDsl01_Entity3", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Entity3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Entity3"):
                opp_val = getattr(value, "myDsl01_Entity3", None)
                setattr(value, "myDsl01_Entity3", self)

    @property
    def myDsl01_Entity15(self):
        return self.__myDsl01_Entity15

    @myDsl01_Entity15.setter
    def myDsl01_Entity15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Entity__myDsl01_Entity15", None)
        self.__myDsl01_Entity15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Window14"):
                opp_val = getattr(old_value, "myDsl01_Window14", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Window14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Window14"):
                opp_val = getattr(value, "myDsl01_Window14", None)
                setattr(value, "myDsl01_Window14", self)

    @property
    def myDsl01_Entity(self):
        return self.__myDsl01_Entity

    @myDsl01_Entity.setter
    def myDsl01_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Entity__myDsl01_Entity", None)
        self.__myDsl01_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Model"):
                opp_val = getattr(old_value, "myDsl01_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Model"):
                opp_val = getattr(value, "myDsl01_Model", None)
                if opp_val is None:
                    setattr(value, "myDsl01_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl01_Entity3(self):
        return self.__myDsl01_Entity3

    @myDsl01_Entity3.setter
    def myDsl01_Entity3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Entity__myDsl01_Entity3", None)
        self.__myDsl01_Entity3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Entity5"):
                opp_val = getattr(old_value, "myDsl01_Entity5", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Entity5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Entity5"):
                opp_val = getattr(value, "myDsl01_Entity5", None)
                setattr(value, "myDsl01_Entity5", self)

class myDsl01_Model:

    pass
class myDsl01_Reference(Property):

    def __init__(self, multiplicity: str, myDsl01_Reference: "myDsl01_Entity" = None, myDsl01_Reference12: "myDsl01_Reference" = None, myDsl01_Reference10: "myDsl01_Reference" = None):
        self.multiplicity = multiplicity
        self.myDsl01_Reference = myDsl01_Reference
        self.myDsl01_Reference12 = myDsl01_Reference12
        self.myDsl01_Reference10 = myDsl01_Reference10
        
    @property
    def multiplicity(self) -> str:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: str):
        self.__multiplicity = multiplicity

    @property
    def myDsl01_Reference(self):
        return self.__myDsl01_Reference

    @myDsl01_Reference.setter
    def myDsl01_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Reference__myDsl01_Reference", None)
        self.__myDsl01_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Entity9"):
                opp_val = getattr(old_value, "myDsl01_Entity9", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Entity9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Entity9"):
                opp_val = getattr(value, "myDsl01_Entity9", None)
                setattr(value, "myDsl01_Entity9", self)

    @property
    def myDsl01_Reference10(self):
        return self.__myDsl01_Reference10

    @myDsl01_Reference10.setter
    def myDsl01_Reference10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Reference__myDsl01_Reference10", None)
        self.__myDsl01_Reference10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Reference12"):
                opp_val = getattr(old_value, "myDsl01_Reference12", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Reference12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Reference12"):
                opp_val = getattr(value, "myDsl01_Reference12", None)
                setattr(value, "myDsl01_Reference12", self)

    @property
    def myDsl01_Reference12(self):
        return self.__myDsl01_Reference12

    @myDsl01_Reference12.setter
    def myDsl01_Reference12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl01_Reference__myDsl01_Reference12", None)
        self.__myDsl01_Reference12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl01_Reference10"):
                opp_val = getattr(old_value, "myDsl01_Reference10", None)
                if opp_val == self:
                    setattr(old_value, "myDsl01_Reference10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl01_Reference10"):
                opp_val = getattr(value, "myDsl01_Reference10", None)
                setattr(value, "myDsl01_Reference10", self)
