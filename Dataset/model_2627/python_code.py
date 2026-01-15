from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class NodeFigure(Enum):
    Default = "Default"
    Ellipse = "Ellipse"
    Polygon = "Polygon"
    Rectangle = "Rectangle"
    Rounded = "Rounded"
    SVG = "SVG"
    Image = "Image"
class FontStyle(Enum):
    Default = "Default"
    Bold = "Bold"
    Italic = "Italic"
class Brightness(Enum):
    Default = "Default"
    Dark = "Dark"
    Light = "Light"
class LayoutCompartment(Enum):
    Free = "Free"
    List = "List"
class Placement(Enum):
    External = "External"
    Internal = "Internal"
    None = "None"
class Color(Enum):
    Default = "Default"
    Black = "Black"
    Blue = "Blue"
    Cyan = "Cyan"
    Gray = "Gray"
    Green = "Green"
    Orange = "Orange"
    Red = "Red"
    White = "White"
    Yellow = "Yellow"
class Texture(Enum):
    Solid = "Solid"
    Default = "Default"
    Dash = "Dash"
    Dot = "Dot"
class LinkFigure(Enum):
    Default = "Default"
    Arrow = "Arrow"
    ClosedArrow = "ClosedArrow"
    FilledClosedArrow = "FilledClosedArrow"
    Rhomb = "Rhomb"
    FilledRhomb = "FilledRhomb"
    Square = "Square"
    FilledSquare = "FilledSquare"
    None = "None"


############################################
# Definition of Classes
############################################

class PersonalizedElement:

    pass
class cevinedit_NodeEClass(PersonalizedElement):

    def __init__(self, labelPlacement: str, labelFontStyle: str, label: str, imagePath: str, listPointsPolygon: str, backgroundColor: str, borderColor: str, borderTexture: str, borderWidth: int, brightness: str, figure: str, resizable: bool, size: str):
        self.labelPlacement = labelPlacement
        self.labelFontStyle = labelFontStyle
        self.label = label
        self.imagePath = imagePath
        self.listPointsPolygon = listPointsPolygon
        self.backgroundColor = backgroundColor
        self.borderColor = borderColor
        self.borderTexture = borderTexture
        self.borderWidth = borderWidth
        self.brightness = brightness
        self.figure = figure
        self.resizable = resizable
        self.size = size
        
    @property
    def resizable(self) -> bool:
        return self.__resizable

    @resizable.setter
    def resizable(self, resizable: bool):
        self.__resizable = resizable

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def brightness(self) -> str:
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness: str):
        self.__brightness = brightness

    @property
    def labelPlacement(self) -> str:
        return self.__labelPlacement

    @labelPlacement.setter
    def labelPlacement(self, labelPlacement: str):
        self.__labelPlacement = labelPlacement

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def borderWidth(self) -> int:
        return self.__borderWidth

    @borderWidth.setter
    def borderWidth(self, borderWidth: int):
        self.__borderWidth = borderWidth

    @property
    def figure(self) -> str:
        return self.__figure

    @figure.setter
    def figure(self, figure: str):
        self.__figure = figure

    @property
    def borderTexture(self) -> str:
        return self.__borderTexture

    @borderTexture.setter
    def borderTexture(self, borderTexture: str):
        self.__borderTexture = borderTexture

    @property
    def labelFontStyle(self) -> str:
        return self.__labelFontStyle

    @labelFontStyle.setter
    def labelFontStyle(self, labelFontStyle: str):
        self.__labelFontStyle = labelFontStyle

    @property
    def listPointsPolygon(self) -> str:
        return self.__listPointsPolygon

    @listPointsPolygon.setter
    def listPointsPolygon(self, listPointsPolygon: str):
        self.__listPointsPolygon = listPointsPolygon

    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

    @property
    def borderColor(self) -> str:
        return self.__borderColor

    @borderColor.setter
    def borderColor(self, borderColor: str):
        self.__borderColor = borderColor

    @property
    def imagePath(self) -> str:
        return self.__imagePath

    @imagePath.setter
    def imagePath(self, imagePath: str):
        self.__imagePath = imagePath

class cevinedit_Link(PersonalizedElement):

    def __init__(self, brightness: str, color: str, labelFontStyle: str, sourceDecoration: str, targetDecoration: str, texture: str, width: int, label: str):
        self.brightness = brightness
        self.color = color
        self.labelFontStyle = labelFontStyle
        self.sourceDecoration = sourceDecoration
        self.targetDecoration = targetDecoration
        self.texture = texture
        self.width = width
        self.label = label
        
    @property
    def brightness(self) -> str:
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness: str):
        self.__brightness = brightness

    @property
    def texture(self) -> str:
        return self.__texture

    @texture.setter
    def texture(self, texture: str):
        self.__texture = texture

    @property
    def labelFontStyle(self) -> str:
        return self.__labelFontStyle

    @labelFontStyle.setter
    def labelFontStyle(self, labelFontStyle: str):
        self.__labelFontStyle = labelFontStyle

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def sourceDecoration(self) -> str:
        return self.__sourceDecoration

    @sourceDecoration.setter
    def sourceDecoration(self, sourceDecoration: str):
        self.__sourceDecoration = sourceDecoration

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def targetDecoration(self) -> str:
        return self.__targetDecoration

    @targetDecoration.setter
    def targetDecoration(self, targetDecoration: str):
        self.__targetDecoration = targetDecoration

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

class cevinedit_LabelEAttribute(PersonalizedElement):

    pass
class cevinedit_AffixedEReferenceCont(PersonalizedElement):

    pass
class cevinedit_CompartmentEReferenceCont(PersonalizedElement):

    def __init__(self, collapsible: bool, layout: str):
        self.collapsible = collapsible
        self.layout = layout
        
    @property
    def layout(self) -> str:
        return self.__layout

    @layout.setter
    def layout(self, layout: str):
        self.__layout = layout

    @property
    def collapsible(self) -> bool:
        return self.__collapsible

    @collapsible.setter
    def collapsible(self, collapsible: bool):
        self.__collapsible = collapsible

class Link:

    pass
class cevinedit_LinkEReferenceNonCont(Link, PersonalizedElement):

    pass
class cevinedit_LinkEClass(Link, PersonalizedElement):

    def __init__(self, source: str, target: str):
        self.source = source
        self.target = target
        
    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

class cevinedit_PersonalizedElement(ABC):

    def __init__(self, name: str, icon: str, cevinedit_PersonalizedElement: "cevinedit_Diagram" = None):
        self.name = name
        self.icon = icon
        self.cevinedit_PersonalizedElement = cevinedit_PersonalizedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def cevinedit_PersonalizedElement(self):
        return self.__cevinedit_PersonalizedElement

    @cevinedit_PersonalizedElement.setter
    def cevinedit_PersonalizedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cevinedit_PersonalizedElement__cevinedit_PersonalizedElement", None)
        self.__cevinedit_PersonalizedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cevinedit_Diagram2"):
                opp_val = getattr(old_value, "cevinedit_Diagram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cevinedit_Diagram2"):
                opp_val = getattr(value, "cevinedit_Diagram2", None)
                if opp_val is None:
                    setattr(value, "cevinedit_Diagram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cevinedit_Diagram:

    def __init__(self, name: str, modelExtension: str, cevinedit_Diagram: "cevinedit_CEViNEditRoot" = None, cevinedit_Diagram2: set["cevinedit_PersonalizedElement"] = None):
        self.name = name
        self.modelExtension = modelExtension
        self.cevinedit_Diagram = cevinedit_Diagram
        self.cevinedit_Diagram2 = cevinedit_Diagram2 if cevinedit_Diagram2 is not None else set()
        
    @property
    def modelExtension(self) -> str:
        return self.__modelExtension

    @modelExtension.setter
    def modelExtension(self, modelExtension: str):
        self.__modelExtension = modelExtension

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cevinedit_Diagram(self):
        return self.__cevinedit_Diagram

    @cevinedit_Diagram.setter
    def cevinedit_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cevinedit_Diagram__cevinedit_Diagram", None)
        self.__cevinedit_Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cevinedit_CEViNEditRoot"):
                opp_val = getattr(old_value, "cevinedit_CEViNEditRoot", None)
                if opp_val == self:
                    setattr(old_value, "cevinedit_CEViNEditRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cevinedit_CEViNEditRoot"):
                opp_val = getattr(value, "cevinedit_CEViNEditRoot", None)
                setattr(value, "cevinedit_CEViNEditRoot", self)

    @property
    def cevinedit_Diagram2(self):
        return self.__cevinedit_Diagram2

    @cevinedit_Diagram2.setter
    def cevinedit_Diagram2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cevinedit_Diagram__cevinedit_Diagram2", None)
        self.__cevinedit_Diagram2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cevinedit_PersonalizedElement"):
                    opp_val = getattr(item, "cevinedit_PersonalizedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "cevinedit_PersonalizedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cevinedit_PersonalizedElement"):
                    opp_val = getattr(item, "cevinedit_PersonalizedElement", None)
                    
                    setattr(item, "cevinedit_PersonalizedElement", self)
                    

class cevinedit_CEViNEditRoot:

    def __init__(self, sourceMM: str, cevinedit_CEViNEditRoot: "cevinedit_Diagram" = None):
        self.sourceMM = sourceMM
        self.cevinedit_CEViNEditRoot = cevinedit_CEViNEditRoot
        
    @property
    def sourceMM(self) -> str:
        return self.__sourceMM

    @sourceMM.setter
    def sourceMM(self, sourceMM: str):
        self.__sourceMM = sourceMM

    @property
    def cevinedit_CEViNEditRoot(self):
        return self.__cevinedit_CEViNEditRoot

    @cevinedit_CEViNEditRoot.setter
    def cevinedit_CEViNEditRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cevinedit_CEViNEditRoot__cevinedit_CEViNEditRoot", None)
        self.__cevinedit_CEViNEditRoot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cevinedit_Diagram"):
                opp_val = getattr(old_value, "cevinedit_Diagram", None)
                if opp_val == self:
                    setattr(old_value, "cevinedit_Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cevinedit_Diagram"):
                opp_val = getattr(value, "cevinedit_Diagram", None)
                setattr(value, "cevinedit_Diagram", self)
