from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LocationType(Enum):
    LOCATION_TYPE_RELATIVE = "LOCATION_TYPE_RELATIVE"
    LOCATION_TYPE_ABSOLUTE_START = "LOCATION_TYPE_ABSOLUTE_START"
    LOCATION_TYPE_ABSOLUTE_END = "LOCATION_TYPE_ABSOLUTE_END"
class LineStyle(Enum):
    UNSPECIFIED = "UNSPECIFIED"
    SOLID = "SOLID"
    DASH = "DASH"
    DASHDOT = "DASHDOT"
    DASHDOTDOT = "DASHDOTDOT"
    DOT = "DOT"
class UnderlineStyle(Enum):
    UNDERLINE_SINGLE = "UNDERLINE_SINGLE"
    UNDERLINE_DOUBLE = "UNDERLINE_DOUBLE"
    UNDERLINE_ERROR = "UNDERLINE_ERROR"
    UNDERLINE_SQUIGGLE = "UNDERLINE_SQUIGGLE"
class Orientation(Enum):
    ALIGNMENT_CENTER = "ALIGNMENT_CENTER"
    ALIGNMENT_LEFT = "ALIGNMENT_LEFT"
    ALIGNMENT_TOP = "ALIGNMENT_TOP"
    ALIGNMENT_RIGHT = "ALIGNMENT_RIGHT"
    ALIGNMENT_BOTTOM = "ALIGNMENT_BOTTOM"
    ALIGNMENT_MIDDLE = "ALIGNMENT_MIDDLE"
    UNSPECIFIED = "UNSPECIFIED"


############################################
# Definition of Classes
############################################

class mm_styles_TextStyle:

    def __init__(self, underline: bool, underlineStyle: str, strikeout: bool, mm_styles_TextStyle75: "styles_Color" = None, mm_styles_TextStyle78: "styles_Color" = None, mm_styles_TextStyle81: "styles_Color" = None, mm_styles_TextStyle84: "styles_Color" = None, mm_styles_TextStyle: "styles_Font" = None):
        self.underline = underline
        self.underlineStyle = underlineStyle
        self.strikeout = strikeout
        self.mm_styles_TextStyle75 = mm_styles_TextStyle75
        self.mm_styles_TextStyle78 = mm_styles_TextStyle78
        self.mm_styles_TextStyle81 = mm_styles_TextStyle81
        self.mm_styles_TextStyle84 = mm_styles_TextStyle84
        self.mm_styles_TextStyle = mm_styles_TextStyle
        
        pass
    @property
    def underline(self):
        return self.__underline

    @underline.setter
    def underline(self, underline: bool):
        self.__underline = underline


    @property
    def strikeout(self):
        return self.__strikeout

    @strikeout.setter
    def strikeout(self, strikeout: bool):
        self.__strikeout = strikeout


    @property
    def underlineStyle(self):
        return self.__underlineStyle

    @underlineStyle.setter
    def underlineStyle(self, underlineStyle: str):
        self.__underlineStyle = underlineStyle


    @property
    def mm_styles_TextStyle81(self):
        return self.__mm_styles_TextStyle81

    @mm_styles_TextStyle81.setter
    def mm_styles_TextStyle81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle81", None)
        self.__mm_styles_TextStyle81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color82"):
                opp_val = getattr(old_value, "styles_Color82", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color82"):
                opp_val = getattr(value, "styles_Color82", None)
                setattr(value, "styles_Color82", self)

    @property
    def mm_styles_TextStyle(self):
        return self.__mm_styles_TextStyle

    @mm_styles_TextStyle.setter
    def mm_styles_TextStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle", None)
        self.__mm_styles_TextStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Font73"):
                opp_val = getattr(old_value, "styles_Font73", None)
                if opp_val == self:
                    setattr(old_value, "styles_Font73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Font73"):
                opp_val = getattr(value, "styles_Font73", None)
                setattr(value, "styles_Font73", self)

    @property
    def mm_styles_TextStyle75(self):
        return self.__mm_styles_TextStyle75

    @mm_styles_TextStyle75.setter
    def mm_styles_TextStyle75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle75", None)
        self.__mm_styles_TextStyle75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color76"):
                opp_val = getattr(old_value, "styles_Color76", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color76"):
                opp_val = getattr(value, "styles_Color76", None)
                setattr(value, "styles_Color76", self)

    @property
    def mm_styles_TextStyle78(self):
        return self.__mm_styles_TextStyle78

    @mm_styles_TextStyle78.setter
    def mm_styles_TextStyle78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle78", None)
        self.__mm_styles_TextStyle78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color79"):
                opp_val = getattr(old_value, "styles_Color79", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color79"):
                opp_val = getattr(value, "styles_Color79", None)
                setattr(value, "styles_Color79", self)

    @property
    def mm_styles_TextStyle84(self):
        return self.__mm_styles_TextStyle84

    @mm_styles_TextStyle84.setter
    def mm_styles_TextStyle84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle84", None)
        self.__mm_styles_TextStyle84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color85"):
                opp_val = getattr(old_value, "styles_Color85", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color85"):
                opp_val = getattr(value, "styles_Color85", None)
                setattr(value, "styles_Color85", self)

class mm_styles_PrecisionPoint:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
        pass
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x


class styles_TextStyle:

    pass
class mm_styles_TextStyleRegion:

    def __init__(self, start: int, end: int, mm_styles_TextStyleRegion: "styles_TextStyle" = None):
        self.start = start
        self.end = end
        self.mm_styles_TextStyleRegion = mm_styles_TextStyleRegion
        
        pass
    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end: int):
        self.__end = end


    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start: int):
        self.__start = start


    @property
    def mm_styles_TextStyleRegion(self):
        return self.__mm_styles_TextStyleRegion

    @mm_styles_TextStyleRegion.setter
    def mm_styles_TextStyleRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyleRegion__mm_styles_TextStyleRegion", None)
        self.__mm_styles_TextStyleRegion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_TextStyle"):
                opp_val = getattr(old_value, "styles_TextStyle", None)
                if opp_val == self:
                    setattr(old_value, "styles_TextStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_TextStyle"):
                opp_val = getattr(value, "styles_TextStyle", None)
                setattr(value, "styles_TextStyle", self)

class mm_styles_GradientColoredLocation:

    def __init__(self, locationType: str, locationValue: str, mm_styles_GradientColoredLocation: "styles_Color" = None):
        self.locationType = locationType
        self.locationValue = locationValue
        self.mm_styles_GradientColoredLocation = mm_styles_GradientColoredLocation
        
        pass
    @property
    def locationType(self):
        return self.__locationType

    @locationType.setter
    def locationType(self, locationType: str):
        self.__locationType = locationType


    @property
    def locationValue(self):
        return self.__locationValue

    @locationValue.setter
    def locationValue(self, locationValue: str):
        self.__locationValue = locationValue


    @property
    def mm_styles_GradientColoredLocation(self):
        return self.__mm_styles_GradientColoredLocation

    @mm_styles_GradientColoredLocation.setter
    def mm_styles_GradientColoredLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_GradientColoredLocation__mm_styles_GradientColoredLocation", None)
        self.__mm_styles_GradientColoredLocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color65"):
                opp_val = getattr(old_value, "styles_Color65", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color65"):
                opp_val = getattr(value, "styles_Color65", None)
                setattr(value, "styles_Color65", self)

class styles_RenderingStyle:

    pass
class mm_styles_Color:

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue
        
        pass
    @property
    def green(self):
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green


    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red


    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue


class mm_styles_Point:

    def __init__(self, x: int, y: int, before: int, after: int):
        self.x = x
        self.y = y
        self.before = before
        self.after = after
        
        pass
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def after(self):
        return self.__after

    @after.setter
    def after(self, after: int):
        self.__after = after


    @property
    def before(self):
        return self.__before

    @before.setter
    def before(self, before: int):
        self.__before = before


class mm_styles_Font:

    def __init__(self, name: str, size: int, italic: bool, bold: bool):
        self.name = name
        self.size = size
        self.italic = italic
        self.bold = bold
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def italic(self):
        return self.__italic

    @italic.setter
    def italic(self, italic: bool):
        self.__italic = italic


    @property
    def bold(self):
        return self.__bold

    @bold.setter
    def bold(self, bold: bool):
        self.__bold = bold


class styles_GradientColoredAreas:

    pass
class mm_styles_AdaptedGradientColoredAreas:

    def __init__(self, definedStyleId: str, gradientType: str, mm_styles_AdaptedGradientColoredAreas: set["styles_GradientColoredAreas"] = None):
        self.definedStyleId = definedStyleId
        self.gradientType = gradientType
        self.mm_styles_AdaptedGradientColoredAreas = mm_styles_AdaptedGradientColoredAreas if mm_styles_AdaptedGradientColoredAreas is not None else set()
        
        pass
    @property
    def gradientType(self):
        return self.__gradientType

    @gradientType.setter
    def gradientType(self, gradientType: str):
        self.__gradientType = gradientType


    @property
    def definedStyleId(self):
        return self.__definedStyleId

    @definedStyleId.setter
    def definedStyleId(self, definedStyleId: str):
        self.__definedStyleId = definedStyleId


    @property
    def mm_styles_AdaptedGradientColoredAreas(self):
        return self.__mm_styles_AdaptedGradientColoredAreas

    @mm_styles_AdaptedGradientColoredAreas.setter
    def mm_styles_AdaptedGradientColoredAreas(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_AdaptedGradientColoredAreas__mm_styles_AdaptedGradientColoredAreas", None)
        self.__mm_styles_AdaptedGradientColoredAreas = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "styles_GradientColoredAreas"):
                    opp_val = getattr(item, "styles_GradientColoredAreas", None)
                    
                    if opp_val == self:
                        setattr(item, "styles_GradientColoredAreas", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "styles_GradientColoredAreas"):
                    opp_val = getattr(item, "styles_GradientColoredAreas", None)
                    
                    setattr(item, "styles_GradientColoredAreas", self)
                    

class styles_GradientColoredArea:

    pass
class mm_styles_GradientColoredAreas:

    def __init__(self, styleAdaption: str, mm_styles_GradientColoredAreas: set["styles_GradientColoredArea"] = None):
        self.styleAdaption = styleAdaption
        self.mm_styles_GradientColoredAreas = mm_styles_GradientColoredAreas if mm_styles_GradientColoredAreas is not None else set()
        
        pass
    @property
    def styleAdaption(self):
        return self.__styleAdaption

    @styleAdaption.setter
    def styleAdaption(self, styleAdaption: str):
        self.__styleAdaption = styleAdaption


    @property
    def mm_styles_GradientColoredAreas(self):
        return self.__mm_styles_GradientColoredAreas

    @mm_styles_GradientColoredAreas.setter
    def mm_styles_GradientColoredAreas(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_GradientColoredAreas__mm_styles_GradientColoredAreas", None)
        self.__mm_styles_GradientColoredAreas = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "styles_GradientColoredArea"):
                    opp_val = getattr(item, "styles_GradientColoredArea", None)
                    
                    if opp_val == self:
                        setattr(item, "styles_GradientColoredArea", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "styles_GradientColoredArea"):
                    opp_val = getattr(item, "styles_GradientColoredArea", None)
                    
                    setattr(item, "styles_GradientColoredArea", self)
                    

class styles_GradientColoredLocation:

    pass
class mm_styles_GradientColoredArea:

    pass
class styles_TextStyleRegion:

    pass
class mm_styles_AbstractStyle(ABC):

    def __init__(self, lineWidth: str, lineStyle: str, filled: str, lineVisible: str, transparency: str, mm_styles_AbstractStyle: "styles_Color" = None, mm_styles_AbstractStyle60: "styles_Color" = None, mm_styles_AbstractStyle63: "styles_RenderingStyle" = None):
        self.lineWidth = lineWidth
        self.lineStyle = lineStyle
        self.filled = filled
        self.lineVisible = lineVisible
        self.transparency = transparency
        self.mm_styles_AbstractStyle = mm_styles_AbstractStyle
        self.mm_styles_AbstractStyle60 = mm_styles_AbstractStyle60
        self.mm_styles_AbstractStyle63 = mm_styles_AbstractStyle63
        
        pass
    @property
    def lineVisible(self):
        return self.__lineVisible

    @lineVisible.setter
    def lineVisible(self, lineVisible: str):
        self.__lineVisible = lineVisible


    @property
    def lineWidth(self):
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: str):
        self.__lineWidth = lineWidth


    @property
    def filled(self):
        return self.__filled

    @filled.setter
    def filled(self, filled: str):
        self.__filled = filled


    @property
    def lineStyle(self):
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle


    @property
    def transparency(self):
        return self.__transparency

    @transparency.setter
    def transparency(self, transparency: str):
        self.__transparency = transparency


    @property
    def mm_styles_AbstractStyle(self):
        return self.__mm_styles_AbstractStyle

    @mm_styles_AbstractStyle.setter
    def mm_styles_AbstractStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_AbstractStyle__mm_styles_AbstractStyle", None)
        self.__mm_styles_AbstractStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color58"):
                opp_val = getattr(old_value, "styles_Color58", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color58"):
                opp_val = getattr(value, "styles_Color58", None)
                setattr(value, "styles_Color58", self)

    @property
    def mm_styles_AbstractStyle60(self):
        return self.__mm_styles_AbstractStyle60

    @mm_styles_AbstractStyle60.setter
    def mm_styles_AbstractStyle60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_AbstractStyle__mm_styles_AbstractStyle60", None)
        self.__mm_styles_AbstractStyle60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color61"):
                opp_val = getattr(old_value, "styles_Color61", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color61"):
                opp_val = getattr(value, "styles_Color61", None)
                setattr(value, "styles_Color61", self)

    @property
    def mm_styles_AbstractStyle63(self):
        return self.__mm_styles_AbstractStyle63

    @mm_styles_AbstractStyle63.setter
    def mm_styles_AbstractStyle63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_AbstractStyle__mm_styles_AbstractStyle63", None)
        self.__mm_styles_AbstractStyle63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_RenderingStyle"):
                opp_val = getattr(old_value, "styles_RenderingStyle", None)
                if opp_val == self:
                    setattr(old_value, "styles_RenderingStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_RenderingStyle"):
                opp_val = getattr(value, "styles_RenderingStyle", None)
                setattr(value, "styles_RenderingStyle", self)

class styles_mm_StyleContainer:

    pass
class styles_AdaptedGradientColoredAreas:

    pass
class mm_styles_RenderingStyle:

    pass
class styles_AbstractStyle:

    pass
class Polyline:

    pass
class mm_algorithms_Polygon(Polyline):

    pass
class AbstractText:

    pass
class mm_algorithms_MultiText(AbstractText):

    pass
class mm_algorithms_Text(AbstractText):

    pass
class styles_Point:

    pass
class AdvancedAnchor:

    pass
class mm_pictograms_BoxRelativeAnchor(AdvancedAnchor):

    def __init__(self, relativeHeight: float, relativeWidth: float):
        self.relativeHeight = relativeHeight
        self.relativeWidth = relativeWidth
        
        pass
    @property
    def relativeHeight(self):
        return self.__relativeHeight

    @relativeHeight.setter
    def relativeHeight(self, relativeHeight: float):
        self.__relativeHeight = relativeHeight


    @property
    def relativeWidth(self):
        return self.__relativeWidth

    @relativeWidth.setter
    def relativeWidth(self, relativeWidth: float):
        self.__relativeWidth = relativeWidth


class mm_pictograms_FixPointAnchor(AdvancedAnchor):

    pass
class CurvedConnection:

    pass
class styles_PrecisionPoint:

    pass
class pictograms_mm_EObject:

    pass
class PictogramLink:

    pass
class styles_Font:

    pass
class styles_Color:

    pass
class PictogramElement:

    pass
class mm_pictograms_AnchorContainer(PictogramElement):

    pass
class mm_pictograms_Anchor(PictogramElement):

    pass
class ConnectionDecorator:

    pass
class Diagram:

    pass
class Anchor:

    pass
class mm_pictograms_ChopboxAnchor(Anchor):

    pass
class mm_pictograms_AdvancedAnchor(Anchor):

    def __init__(self, useAnchorLocationAsConnectionEndpoint: bool, Anchor16: "mm_pictograms_Connection" = None, Anchor: "mm_pictograms_Connection" = None, Anchor28: "mm_pictograms_AnchorContainer" = None):
        self.useAnchorLocationAsConnectionEndpoint = useAnchorLocationAsConnectionEndpoint
        
        pass
    @property
    def useAnchorLocationAsConnectionEndpoint(self):
        return self.__useAnchorLocationAsConnectionEndpoint

    @useAnchorLocationAsConnectionEndpoint.setter
    def useAnchorLocationAsConnectionEndpoint(self, useAnchorLocationAsConnectionEndpoint: bool):
        self.__useAnchorLocationAsConnectionEndpoint = useAnchorLocationAsConnectionEndpoint


class GraphicsAlgorithm:

    pass
class mm_algorithms_AbstractText(GraphicsAlgorithm):

    def __init__(self, horizontalAlignment: str, verticalAlignment: str, angle: str, value: str, mm_algorithms_AbstractText: "styles_Font" = None, mm_algorithms_AbstractText51: set["styles_TextStyleRegion"] = None, GraphicsAlgorithm39: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm41: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm25: "mm_pictograms_Anchor" = None, GraphicsAlgorithm: "mm_pictograms_PictogramElement" = None):
        self.horizontalAlignment = horizontalAlignment
        self.verticalAlignment = verticalAlignment
        self.angle = angle
        self.value = value
        self.mm_algorithms_AbstractText = mm_algorithms_AbstractText
        self.mm_algorithms_AbstractText51 = mm_algorithms_AbstractText51 if mm_algorithms_AbstractText51 is not None else set()
        
        pass
    @property
    def verticalAlignment(self):
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def horizontalAlignment(self):
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment


    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle


    @property
    def mm_algorithms_AbstractText51(self):
        return self.__mm_algorithms_AbstractText51

    @mm_algorithms_AbstractText51.setter
    def mm_algorithms_AbstractText51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_algorithms_AbstractText__mm_algorithms_AbstractText51", None)
        self.__mm_algorithms_AbstractText51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "styles_TextStyleRegion"):
                    opp_val = getattr(item, "styles_TextStyleRegion", None)
                    
                    if opp_val == self:
                        setattr(item, "styles_TextStyleRegion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "styles_TextStyleRegion"):
                    opp_val = getattr(item, "styles_TextStyleRegion", None)
                    
                    setattr(item, "styles_TextStyleRegion", self)
                    

    @property
    def mm_algorithms_AbstractText(self):
        return self.__mm_algorithms_AbstractText

    @mm_algorithms_AbstractText.setter
    def mm_algorithms_AbstractText(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_algorithms_AbstractText__mm_algorithms_AbstractText", None)
        self.__mm_algorithms_AbstractText = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Font49"):
                opp_val = getattr(old_value, "styles_Font49", None)
                if opp_val == self:
                    setattr(old_value, "styles_Font49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Font49"):
                opp_val = getattr(value, "styles_Font49", None)
                setattr(value, "styles_Font49", self)

class mm_algorithms_PlatformGraphicsAlgorithm(GraphicsAlgorithm):

    def __init__(self, id: str, GraphicsAlgorithm39: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm41: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm25: "mm_pictograms_Anchor" = None, GraphicsAlgorithm: "mm_pictograms_PictogramElement" = None):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class mm_algorithms_Image(GraphicsAlgorithm):

    def __init__(self, id: str, stretchH: str, stretchV: str, proportional: str, GraphicsAlgorithm39: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm41: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm25: "mm_pictograms_Anchor" = None, GraphicsAlgorithm: "mm_pictograms_PictogramElement" = None):
        self.id = id
        self.stretchH = stretchH
        self.stretchV = stretchV
        self.proportional = proportional
        
        pass
    @property
    def stretchH(self):
        return self.__stretchH

    @stretchH.setter
    def stretchH(self, stretchH: str):
        self.__stretchH = stretchH


    @property
    def stretchV(self):
        return self.__stretchV

    @stretchV.setter
    def stretchV(self, stretchV: str):
        self.__stretchV = stretchV


    @property
    def proportional(self):
        return self.__proportional

    @proportional.setter
    def proportional(self, proportional: str):
        self.__proportional = proportional


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class mm_algorithms_Polyline(GraphicsAlgorithm):

    pass
class mm_algorithms_RoundedRectangle(GraphicsAlgorithm):

    def __init__(self, cornerHeight: int, cornerWidth: int, GraphicsAlgorithm39: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm41: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm25: "mm_pictograms_Anchor" = None, GraphicsAlgorithm: "mm_pictograms_PictogramElement" = None):
        self.cornerHeight = cornerHeight
        self.cornerWidth = cornerWidth
        
        pass
    @property
    def cornerHeight(self):
        return self.__cornerHeight

    @cornerHeight.setter
    def cornerHeight(self, cornerHeight: int):
        self.__cornerHeight = cornerHeight


    @property
    def cornerWidth(self):
        return self.__cornerWidth

    @cornerWidth.setter
    def cornerWidth(self, cornerWidth: int):
        self.__cornerWidth = cornerWidth


class mm_algorithms_Ellipse(GraphicsAlgorithm):

    pass
class mm_algorithms_Rectangle(GraphicsAlgorithm):

    pass
class GraphicsAlgorithmContainer:

    pass
class mm_algorithms_GraphicsAlgorithm(styles_AbstractStyle, GraphicsAlgorithmContainer):

    def __init__(self, width: int, height: int, x: int, y: int, graphicsAlgorithm: "PictogramElement" = None, mm_algorithms_GraphicsAlgorithm: "styles_Style" = None, parentGraphicsAlgorithm: set["GraphicsAlgorithm"] = None, graphicsAlgorithmChildren: "GraphicsAlgorithm" = None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.graphicsAlgorithm = graphicsAlgorithm
        self.mm_algorithms_GraphicsAlgorithm = mm_algorithms_GraphicsAlgorithm
        self.parentGraphicsAlgorithm = parentGraphicsAlgorithm if parentGraphicsAlgorithm is not None else set()
        self.graphicsAlgorithmChildren = graphicsAlgorithmChildren
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


    @property
    def graphicsAlgorithm(self):
        return self.__graphicsAlgorithm

    @graphicsAlgorithm.setter
    def graphicsAlgorithm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_algorithms_GraphicsAlgorithm__graphicsAlgorithm", None)
        self.__graphicsAlgorithm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PictogramElement43"):
                opp_val = getattr(old_value, "PictogramElement43", None)
                if opp_val == self:
                    setattr(old_value, "PictogramElement43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PictogramElement43"):
                opp_val = getattr(value, "PictogramElement43", None)
                setattr(value, "PictogramElement43", self)

    @property
    def parentGraphicsAlgorithm(self):
        return self.__parentGraphicsAlgorithm

    @parentGraphicsAlgorithm.setter
    def parentGraphicsAlgorithm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_algorithms_GraphicsAlgorithm__parentGraphicsAlgorithm", None)
        self.__parentGraphicsAlgorithm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphicsAlgorithm39"):
                    opp_val = getattr(item, "GraphicsAlgorithm39", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphicsAlgorithm39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphicsAlgorithm39"):
                    opp_val = getattr(item, "GraphicsAlgorithm39", None)
                    
                    setattr(item, "GraphicsAlgorithm39", self)
                    

    @property
    def mm_algorithms_GraphicsAlgorithm(self):
        return self.__mm_algorithms_GraphicsAlgorithm

    @mm_algorithms_GraphicsAlgorithm.setter
    def mm_algorithms_GraphicsAlgorithm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_algorithms_GraphicsAlgorithm__mm_algorithms_GraphicsAlgorithm", None)
        self.__mm_algorithms_GraphicsAlgorithm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Style45"):
                opp_val = getattr(old_value, "styles_Style45", None)
                if opp_val == self:
                    setattr(old_value, "styles_Style45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Style45"):
                opp_val = getattr(value, "styles_Style45", None)
                setattr(value, "styles_Style45", self)

    @property
    def graphicsAlgorithmChildren(self):
        return self.__graphicsAlgorithmChildren

    @graphicsAlgorithmChildren.setter
    def graphicsAlgorithmChildren(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_algorithms_GraphicsAlgorithm__graphicsAlgorithmChildren", None)
        self.__graphicsAlgorithmChildren = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphicsAlgorithm41"):
                opp_val = getattr(old_value, "GraphicsAlgorithm41", None)
                if opp_val == self:
                    setattr(old_value, "GraphicsAlgorithm41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphicsAlgorithm41"):
                opp_val = getattr(value, "GraphicsAlgorithm41", None)
                setattr(value, "GraphicsAlgorithm41", self)

class mm_pictograms_PictogramElement(GraphicsAlgorithmContainer):

    def __init__(self, visible: bool, active: bool, pictogramElement: "GraphicsAlgorithm" = None, pictogramElement12: "PictogramLink" = None):
        self.visible = visible
        self.active = active
        self.pictogramElement = pictogramElement
        self.pictogramElement12 = pictogramElement12
        
        pass
    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible


    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active


    @property
    def pictogramElement(self):
        return self.__pictogramElement

    @pictogramElement.setter
    def pictogramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_PictogramElement__pictogramElement", None)
        self.__pictogramElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphicsAlgorithm"):
                opp_val = getattr(old_value, "GraphicsAlgorithm", None)
                if opp_val == self:
                    setattr(old_value, "GraphicsAlgorithm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphicsAlgorithm"):
                opp_val = getattr(value, "GraphicsAlgorithm", None)
                setattr(value, "GraphicsAlgorithm", self)

    @property
    def pictogramElement12(self):
        return self.__pictogramElement12

    @pictogramElement12.setter
    def pictogramElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_PictogramElement__pictogramElement12", None)
        self.__pictogramElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PictogramLink13"):
                opp_val = getattr(old_value, "PictogramLink13", None)
                if opp_val == self:
                    setattr(old_value, "PictogramLink13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PictogramLink13"):
                opp_val = getattr(value, "PictogramLink13", None)
                setattr(value, "PictogramLink13", self)

class Connection:

    pass
class mm_pictograms_FreeFormConnection(Connection):

    pass
class mm_pictograms_CompositeConnection(Connection):

    pass
class mm_pictograms_CurvedConnection(Connection):

    pass
class mm_pictograms_ManhattanConnection(Connection):

    pass
class StyleContainer:

    pass
class mm_styles_Style(styles_AbstractStyle, StyleContainer):

    def __init__(self, id: str, description: str, horizontalAlignment: str, verticalAlignment: str, angle: str, stretchH: str, stretchV: str, proportional: str, mm_styles_Style: "styles_Font" = None, mm_styles_Style56: "styles_mm_StyleContainer" = None):
        self.id = id
        self.description = description
        self.horizontalAlignment = horizontalAlignment
        self.verticalAlignment = verticalAlignment
        self.angle = angle
        self.stretchH = stretchH
        self.stretchV = stretchV
        self.proportional = proportional
        self.mm_styles_Style = mm_styles_Style
        self.mm_styles_Style56 = mm_styles_Style56
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle


    @property
    def stretchV(self):
        return self.__stretchV

    @stretchV.setter
    def stretchV(self, stretchV: str):
        self.__stretchV = stretchV


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def horizontalAlignment(self):
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment


    @property
    def stretchH(self):
        return self.__stretchH

    @stretchH.setter
    def stretchH(self, stretchH: str):
        self.__stretchH = stretchH


    @property
    def verticalAlignment(self):
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment


    @property
    def proportional(self):
        return self.__proportional

    @proportional.setter
    def proportional(self, proportional: str):
        self.__proportional = proportional


    @property
    def mm_styles_Style56(self):
        return self.__mm_styles_Style56

    @mm_styles_Style56.setter
    def mm_styles_Style56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_Style__mm_styles_Style56", None)
        self.__mm_styles_Style56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_mm_StyleContainer"):
                opp_val = getattr(old_value, "styles_mm_StyleContainer", None)
                if opp_val == self:
                    setattr(old_value, "styles_mm_StyleContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_mm_StyleContainer"):
                opp_val = getattr(value, "styles_mm_StyleContainer", None)
                setattr(value, "styles_mm_StyleContainer", self)

    @property
    def mm_styles_Style(self):
        return self.__mm_styles_Style

    @mm_styles_Style.setter
    def mm_styles_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_Style__mm_styles_Style", None)
        self.__mm_styles_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Font54"):
                opp_val = getattr(old_value, "styles_Font54", None)
                if opp_val == self:
                    setattr(old_value, "styles_Font54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Font54"):
                opp_val = getattr(value, "styles_Font54", None)
                setattr(value, "styles_Font54", self)

class pictograms_ContainerShape:

    pass
class mm_pictograms_Diagram(pictograms_ContainerShape, StyleContainer):

    def __init__(self, gridUnit: int, diagramTypeId: str, name: str, snapToGrid: bool, showGuides: bool, verticalGridUnit: int, version: str, parent: set["Connection"] = None, mm_pictograms_Diagram: set["styles_Color"] = None, mm_pictograms_Diagram7: set["styles_Font"] = None, mm_pictograms_Diagram9: set["PictogramLink"] = None):
        self.gridUnit = gridUnit
        self.diagramTypeId = diagramTypeId
        self.name = name
        self.snapToGrid = snapToGrid
        self.showGuides = showGuides
        self.verticalGridUnit = verticalGridUnit
        self.version = version
        self.parent = parent if parent is not None else set()
        self.mm_pictograms_Diagram = mm_pictograms_Diagram if mm_pictograms_Diagram is not None else set()
        self.mm_pictograms_Diagram7 = mm_pictograms_Diagram7 if mm_pictograms_Diagram7 is not None else set()
        self.mm_pictograms_Diagram9 = mm_pictograms_Diagram9 if mm_pictograms_Diagram9 is not None else set()
        
        pass
    @property
    def snapToGrid(self):
        return self.__snapToGrid

    @snapToGrid.setter
    def snapToGrid(self, snapToGrid: bool):
        self.__snapToGrid = snapToGrid


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def diagramTypeId(self):
        return self.__diagramTypeId

    @diagramTypeId.setter
    def diagramTypeId(self, diagramTypeId: str):
        self.__diagramTypeId = diagramTypeId


    @property
    def showGuides(self):
        return self.__showGuides

    @showGuides.setter
    def showGuides(self, showGuides: bool):
        self.__showGuides = showGuides


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def gridUnit(self):
        return self.__gridUnit

    @gridUnit.setter
    def gridUnit(self, gridUnit: int):
        self.__gridUnit = gridUnit


    @property
    def verticalGridUnit(self):
        return self.__verticalGridUnit

    @verticalGridUnit.setter
    def verticalGridUnit(self, verticalGridUnit: int):
        self.__verticalGridUnit = verticalGridUnit


    @property
    def mm_pictograms_Diagram9(self):
        return self.__mm_pictograms_Diagram9

    @mm_pictograms_Diagram9.setter
    def mm_pictograms_Diagram9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_Diagram__mm_pictograms_Diagram9", None)
        self.__mm_pictograms_Diagram9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PictogramLink"):
                    opp_val = getattr(item, "PictogramLink", None)
                    
                    if opp_val == self:
                        setattr(item, "PictogramLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PictogramLink"):
                    opp_val = getattr(item, "PictogramLink", None)
                    
                    setattr(item, "PictogramLink", self)
                    

    @property
    def mm_pictograms_Diagram(self):
        return self.__mm_pictograms_Diagram

    @mm_pictograms_Diagram.setter
    def mm_pictograms_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_Diagram__mm_pictograms_Diagram", None)
        self.__mm_pictograms_Diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "styles_Color"):
                    opp_val = getattr(item, "styles_Color", None)
                    
                    if opp_val == self:
                        setattr(item, "styles_Color", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "styles_Color"):
                    opp_val = getattr(item, "styles_Color", None)
                    
                    setattr(item, "styles_Color", self)
                    

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_Diagram__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection"):
                    opp_val = getattr(item, "Connection", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection"):
                    opp_val = getattr(item, "Connection", None)
                    
                    setattr(item, "Connection", self)
                    

    @property
    def mm_pictograms_Diagram7(self):
        return self.__mm_pictograms_Diagram7

    @mm_pictograms_Diagram7.setter
    def mm_pictograms_Diagram7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_Diagram__mm_pictograms_Diagram7", None)
        self.__mm_pictograms_Diagram7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "styles_Font"):
                    opp_val = getattr(item, "styles_Font", None)
                    
                    if opp_val == self:
                        setattr(item, "styles_Font", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "styles_Font"):
                    opp_val = getattr(item, "styles_Font", None)
                    
                    setattr(item, "styles_Font", self)
                    

class Shape:

    pass
class mm_pictograms_ConnectionDecorator(Shape):

    def __init__(self, locationRelative: bool, location: float, connectionDecorators: "Connection" = None, Shape: "mm_pictograms_ContainerShape" = None):
        self.locationRelative = locationRelative
        self.location = location
        self.connectionDecorators = connectionDecorators
        
        pass
    @property
    def locationRelative(self):
        return self.__locationRelative

    @locationRelative.setter
    def locationRelative(self, locationRelative: bool):
        self.__locationRelative = locationRelative


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: float):
        self.__location = location


    @property
    def connectionDecorators(self):
        return self.__connectionDecorators

    @connectionDecorators.setter
    def connectionDecorators(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_ConnectionDecorator__connectionDecorators", None)
        self.__connectionDecorators = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Connection31"):
                opp_val = getattr(old_value, "Connection31", None)
                if opp_val == self:
                    setattr(old_value, "Connection31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Connection31"):
                opp_val = getattr(value, "Connection31", None)
                setattr(value, "Connection31", self)

class mm_pictograms_ContainerShape(Shape):

    pass
class ContainerShape:

    pass
class AnchorContainer:

    pass
class mm_pictograms_Connection(AnchorContainer):

    pass
class mm_pictograms_Shape(AnchorContainer):

    pass
class styles_Style:

    pass
class mm_StyleContainer(ABC):

    pass
class PropertyContainer:

    pass
class mm_pictograms_PictogramLink(PropertyContainer):

    pass
class mm_GraphicsAlgorithmContainer(PropertyContainer):

    pass
class mm_PropertyContainer(ABC):

    pass
class mm_Property:

    def __init__(self, key: str, value: str, mm_Property: "mm_PropertyContainer" = None):
        self.key = key
        self.value = value
        self.mm_Property = mm_Property
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def mm_Property(self):
        return self.__mm_Property

    @mm_Property.setter
    def mm_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_Property__mm_Property", None)
        self.__mm_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm_PropertyContainer"):
                opp_val = getattr(old_value, "mm_PropertyContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm_PropertyContainer"):
                opp_val = getattr(value, "mm_PropertyContainer", None)
                if opp_val is None:
                    setattr(value, "mm_PropertyContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
