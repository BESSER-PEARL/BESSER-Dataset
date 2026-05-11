from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LinkFigure(Enum):
    Default = "Default"
    Arrow = "Arrow"
    ClosedArrow = "ClosedArrow"
    FilledClosedArrow = "FilledClosedArrow"
    Rhomb = "Rhomb"
    FilledRhomb = "FilledRhomb"
    Square = "Square"
    FilledSquare = "FilledSquare"
    None_ = "None_"
class Texture(Enum):
    Default = "Default"
    Dash = "Dash"
    Dot = "Dot"
    Solid = "Solid"
class Brightness(Enum):
    Default = "Default"
    Dark = "Dark"
    Light = "Light"
class Placement(Enum):
    External = "External"
    Internal = "Internal"
    None_ = "None_"
class NodeFigure(Enum):
    Default = "Default"
    Ellipse = "Ellipse"
    Polygon = "Polygon"
    Rectangle = "Rectangle"
    Rounded = "Rounded"
    SVG = "SVG"
    Image = "Image"
class LayoutCompartment(Enum):
    Free = "Free"
    List = "List"
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
class FontStyle(Enum):
    Default = "Default"
    Bold = "Bold"
    Italic = "Italic"


############################################
# Definition of Classes
############################################

class PersonalizedElement:

    pass
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
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness: str):
        self.__brightness = brightness


    @property
    def sourceDecoration(self):
        return self.__sourceDecoration

    @sourceDecoration.setter
    def sourceDecoration(self, sourceDecoration: str):
        self.__sourceDecoration = sourceDecoration


    @property
    def targetDecoration(self):
        return self.__targetDecoration

    @targetDecoration.setter
    def targetDecoration(self, targetDecoration: str):
        self.__targetDecoration = targetDecoration


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def texture(self):
        return self.__texture

    @texture.setter
    def texture(self, texture: str):
        self.__texture = texture


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def labelFontStyle(self):
        return self.__labelFontStyle

    @labelFontStyle.setter
    def labelFontStyle(self, labelFontStyle: str):
        self.__labelFontStyle = labelFontStyle


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
        
        pass
    @property
    def labelFontStyle(self):
        return self.__labelFontStyle

    @labelFontStyle.setter
    def labelFontStyle(self, labelFontStyle: str):
        self.__labelFontStyle = labelFontStyle


    @property
    def borderWidth(self):
        return self.__borderWidth

    @borderWidth.setter
    def borderWidth(self, borderWidth: int):
        self.__borderWidth = borderWidth


    @property
    def borderTexture(self):
        return self.__borderTexture

    @borderTexture.setter
    def borderTexture(self, borderTexture: str):
        self.__borderTexture = borderTexture


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def listPointsPolygon(self):
        return self.__listPointsPolygon

    @listPointsPolygon.setter
    def listPointsPolygon(self, listPointsPolygon: str):
        self.__listPointsPolygon = listPointsPolygon


    @property
    def backgroundColor(self):
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor


    @property
    def labelPlacement(self):
        return self.__labelPlacement

    @labelPlacement.setter
    def labelPlacement(self, labelPlacement: str):
        self.__labelPlacement = labelPlacement


    @property
    def resizable(self):
        return self.__resizable

    @resizable.setter
    def resizable(self, resizable: bool):
        self.__resizable = resizable


    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness: str):
        self.__brightness = brightness


    @property
    def borderColor(self):
        return self.__borderColor

    @borderColor.setter
    def borderColor(self, borderColor: str):
        self.__borderColor = borderColor


    @property
    def imagePath(self):
        return self.__imagePath

    @imagePath.setter
    def imagePath(self, imagePath: str):
        self.__imagePath = imagePath


    @property
    def figure(self):
        return self.__figure

    @figure.setter
    def figure(self, figure: str):
        self.__figure = figure


class cevinedit_PersonalizedElement(ABC):

    def __init__(self, name: str, icon: str, cevinedit_PersonalizedElement: "cevinedit_Diagram" = None):
        self.name = name
        self.icon = icon
        self.cevinedit_PersonalizedElement = cevinedit_PersonalizedElement
        
        pass
    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def modelExtension(self):
        return self.__modelExtension

    @modelExtension.setter
    def modelExtension(self, modelExtension: str):
        self.__modelExtension = modelExtension


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

class cevinedit_CEViNEditRoot:

    def __init__(self, sourceMM: str, cevinedit_CEViNEditRoot: "cevinedit_Diagram" = None):
        self.sourceMM = sourceMM
        self.cevinedit_CEViNEditRoot = cevinedit_CEViNEditRoot
        
        pass
    @property
    def sourceMM(self):
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

class cevinedit_LabelEAttribute(PersonalizedElement):

    pass
class cevinedit_AffixedEReferenceCont(PersonalizedElement):

    pass
class cevinedit_CompartmentEReferenceCont(PersonalizedElement):

    def __init__(self, collapsible: bool, layout: str):
        self.collapsible = collapsible
        self.layout = layout
        
        pass
    @property
    def collapsible(self):
        return self.__collapsible

    @collapsible.setter
    def collapsible(self, collapsible: bool):
        self.__collapsible = collapsible


    @property
    def layout(self):
        return self.__layout

    @layout.setter
    def layout(self, layout: str):
        self.__layout = layout


class Link:

    pass
class cevinedit_LinkEReferenceNonCont(Link, PersonalizedElement):

    pass
class cevinedit_LinkEClass(Link, PersonalizedElement):

    def __init__(self, source: str, target: str):
        self.source = source
        self.target = target
        
        pass
    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

