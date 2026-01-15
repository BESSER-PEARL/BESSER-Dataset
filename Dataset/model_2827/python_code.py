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
class Orientation(Enum):
    ALIGNMENT_CENTER = "ALIGNMENT_CENTER"
    ALIGNMENT_LEFT = "ALIGNMENT_LEFT"
    ALIGNMENT_TOP = "ALIGNMENT_TOP"
    ALIGNMENT_RIGHT = "ALIGNMENT_RIGHT"
    ALIGNMENT_BOTTOM = "ALIGNMENT_BOTTOM"
    ALIGNMENT_MIDDLE = "ALIGNMENT_MIDDLE"
    UNSPECIFIED = "UNSPECIFIED"
class UnderlineStyle(Enum):
    UNDERLINE_DOUBLE = "UNDERLINE_DOUBLE"
    UNDERLINE_ERROR = "UNDERLINE_ERROR"
    UNDERLINE_SQUIGGLE = "UNDERLINE_SQUIGGLE"
    UNDERLINE_SINGLE = "UNDERLINE_SINGLE"
class LineStyle(Enum):
    SOLID = "SOLID"
    DASH = "DASH"
    DASHDOT = "DASHDOT"
    DASHDOTDOT = "DASHDOTDOT"
    DOT = "DOT"
    UNSPECIFIED = "UNSPECIFIED"


############################################
# Definition of Classes
############################################

class styles_TextStyle:

    pass
class mm_styles_TextStyleRegion:

    def __init__(self, start: int, end: int, mm_styles_TextStyleRegion: "styles_TextStyle" = None):
        self.start = start
        self.end = end
        self.mm_styles_TextStyleRegion = mm_styles_TextStyleRegion
        
    @property
    def end(self) -> int:
        return self.__end

    @end.setter
    def end(self, end: int):
        self.__end = end

    @property
    def start(self) -> int:
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

class mm_styles_TextStyle:

    def __init__(self, underline: bool, underlineStyle: str, strikeout: bool, mm_styles_TextStyle: "styles_Font" = None, mm_styles_TextStyle89: "styles_Color" = None, mm_styles_TextStyle92: "styles_Color" = None, mm_styles_TextStyle98: "styles_Color" = None, mm_styles_TextStyle95: "styles_Color" = None):
        self.underline = underline
        self.underlineStyle = underlineStyle
        self.strikeout = strikeout
        self.mm_styles_TextStyle = mm_styles_TextStyle
        self.mm_styles_TextStyle89 = mm_styles_TextStyle89
        self.mm_styles_TextStyle92 = mm_styles_TextStyle92
        self.mm_styles_TextStyle98 = mm_styles_TextStyle98
        self.mm_styles_TextStyle95 = mm_styles_TextStyle95
        
    @property
    def strikeout(self) -> bool:
        return self.__strikeout

    @strikeout.setter
    def strikeout(self, strikeout: bool):
        self.__strikeout = strikeout

    @property
    def underlineStyle(self) -> str:
        return self.__underlineStyle

    @underlineStyle.setter
    def underlineStyle(self, underlineStyle: str):
        self.__underlineStyle = underlineStyle

    @property
    def underline(self) -> bool:
        return self.__underline

    @underline.setter
    def underline(self, underline: bool):
        self.__underline = underline

    @property
    def mm_styles_TextStyle95(self):
        return self.__mm_styles_TextStyle95

    @mm_styles_TextStyle95.setter
    def mm_styles_TextStyle95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle95", None)
        self.__mm_styles_TextStyle95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color96"):
                opp_val = getattr(old_value, "styles_Color96", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color96"):
                opp_val = getattr(value, "styles_Color96", None)
                setattr(value, "styles_Color96", self)

    @property
    def mm_styles_TextStyle92(self):
        return self.__mm_styles_TextStyle92

    @mm_styles_TextStyle92.setter
    def mm_styles_TextStyle92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle92", None)
        self.__mm_styles_TextStyle92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color93"):
                opp_val = getattr(old_value, "styles_Color93", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color93"):
                opp_val = getattr(value, "styles_Color93", None)
                setattr(value, "styles_Color93", self)

    @property
    def mm_styles_TextStyle98(self):
        return self.__mm_styles_TextStyle98

    @mm_styles_TextStyle98.setter
    def mm_styles_TextStyle98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle98", None)
        self.__mm_styles_TextStyle98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color99"):
                opp_val = getattr(old_value, "styles_Color99", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color99"):
                opp_val = getattr(value, "styles_Color99", None)
                setattr(value, "styles_Color99", self)

    @property
    def mm_styles_TextStyle89(self):
        return self.__mm_styles_TextStyle89

    @mm_styles_TextStyle89.setter
    def mm_styles_TextStyle89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle89", None)
        self.__mm_styles_TextStyle89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color90"):
                opp_val = getattr(old_value, "styles_Color90", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color90"):
                opp_val = getattr(value, "styles_Color90", None)
                setattr(value, "styles_Color90", self)

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
            if hasattr(old_value, "styles_Font87"):
                opp_val = getattr(old_value, "styles_Font87", None)
                if opp_val == self:
                    setattr(old_value, "styles_Font87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Font87"):
                opp_val = getattr(value, "styles_Font87", None)
                setattr(value, "styles_Font87", self)

class mm_styles_PrecisionPoint:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

class mm_styles_Color:

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue
        
    @property
    def green(self) -> int:
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green

    @property
    def blue(self) -> int:
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue

    @property
    def red(self) -> int:
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red

class mm_styles_Point:

    def __init__(self, after: int, x: int, y: int, before: int):
        self.after = after
        self.x = x
        self.y = y
        self.before = before
        
    @property
    def before(self) -> int:
        return self.__before

    @before.setter
    def before(self, before: int):
        self.__before = before

    @property
    def after(self) -> int:
        return self.__after

    @after.setter
    def after(self, after: int):
        self.__after = after

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

class mm_styles_Font:

    def __init__(self, name: str, size: int, italic: bool, bold: bool):
        self.name = name
        self.size = size
        self.italic = italic
        self.bold = bold
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bold(self) -> bool:
        return self.__bold

    @bold.setter
    def bold(self, bold: bool):
        self.__bold = bold

    @property
    def italic(self) -> bool:
        return self.__italic

    @italic.setter
    def italic(self, italic: bool):
        self.__italic = italic

class styles_GradientColoredAreas:

    pass
class mm_styles_AdaptedGradientColoredAreas:

    def __init__(self, definedStyleId: str, gradientType: str, mm_styles_AdaptedGradientColoredAreas: set["styles_GradientColoredAreas"] = None):
        self.definedStyleId = definedStyleId
        self.gradientType = gradientType
        self.mm_styles_AdaptedGradientColoredAreas = mm_styles_AdaptedGradientColoredAreas if mm_styles_AdaptedGradientColoredAreas is not None else set()
        
    @property
    def definedStyleId(self) -> str:
        return self.__definedStyleId

    @definedStyleId.setter
    def definedStyleId(self, definedStyleId: str):
        self.__definedStyleId = definedStyleId

    @property
    def gradientType(self) -> str:
        return self.__gradientType

    @gradientType.setter
    def gradientType(self, gradientType: str):
        self.__gradientType = gradientType

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
        
    @property
    def styleAdaption(self) -> str:
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
                    

class mm_styles_AbstractStyle(ABC):

    def __init__(self, lineWidth: str, lineStyle: str, filled: str, lineVisible: str, transparency: str, mm_styles_AbstractStyle: "styles_Color" = None, mm_styles_AbstractStyle74: "styles_Color" = None, mm_styles_AbstractStyle77: "styles_RenderingStyle" = None):
        self.lineWidth = lineWidth
        self.lineStyle = lineStyle
        self.filled = filled
        self.lineVisible = lineVisible
        self.transparency = transparency
        self.mm_styles_AbstractStyle = mm_styles_AbstractStyle
        self.mm_styles_AbstractStyle74 = mm_styles_AbstractStyle74
        self.mm_styles_AbstractStyle77 = mm_styles_AbstractStyle77
        
    @property
    def lineVisible(self) -> str:
        return self.__lineVisible

    @lineVisible.setter
    def lineVisible(self, lineVisible: str):
        self.__lineVisible = lineVisible

    @property
    def transparency(self) -> str:
        return self.__transparency

    @transparency.setter
    def transparency(self, transparency: str):
        self.__transparency = transparency

    @property
    def lineStyle(self) -> str:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle

    @property
    def lineWidth(self) -> str:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: str):
        self.__lineWidth = lineWidth

    @property
    def filled(self) -> str:
        return self.__filled

    @filled.setter
    def filled(self, filled: str):
        self.__filled = filled

    @property
    def mm_styles_AbstractStyle77(self):
        return self.__mm_styles_AbstractStyle77

    @mm_styles_AbstractStyle77.setter
    def mm_styles_AbstractStyle77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_AbstractStyle__mm_styles_AbstractStyle77", None)
        self.__mm_styles_AbstractStyle77 = value
        
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
            if hasattr(old_value, "styles_Color72"):
                opp_val = getattr(old_value, "styles_Color72", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color72"):
                opp_val = getattr(value, "styles_Color72", None)
                setattr(value, "styles_Color72", self)

    @property
    def mm_styles_AbstractStyle74(self):
        return self.__mm_styles_AbstractStyle74

    @mm_styles_AbstractStyle74.setter
    def mm_styles_AbstractStyle74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_AbstractStyle__mm_styles_AbstractStyle74", None)
        self.__mm_styles_AbstractStyle74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color75"):
                opp_val = getattr(old_value, "styles_Color75", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color75"):
                opp_val = getattr(value, "styles_Color75", None)
                setattr(value, "styles_Color75", self)

class styles_GradientColoredLocation:

    pass
class mm_styles_GradientColoredArea:

    pass
class mm_styles_GradientColoredLocation:

    def __init__(self, locationType: str, locationValue: str, mm_styles_GradientColoredLocation: "styles_Color" = None):
        self.locationType = locationType
        self.locationValue = locationValue
        self.mm_styles_GradientColoredLocation = mm_styles_GradientColoredLocation
        
    @property
    def locationType(self) -> str:
        return self.__locationType

    @locationType.setter
    def locationType(self, locationType: str):
        self.__locationType = locationType

    @property
    def locationValue(self) -> str:
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
            if hasattr(old_value, "styles_Color79"):
                opp_val = getattr(old_value, "styles_Color79", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color79"):
                opp_val = getattr(value, "styles_Color79", None)
                setattr(value, "styles_Color79", self)

class styles_RenderingStyle:

    pass
class styles_mm_StyleContainer:

    pass
class styles_AdaptedGradientColoredAreas:

    pass
class mm_styles_RenderingStyle:

    pass
class styles_TextStyleRegion:

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
class styles_PrecisionPoint:

    pass
class styles_AbstractStyle:

    pass
class CurvedConnection:

    pass
class pictograms_mm_EObject:

    pass
class styles_Point:

    pass
class AdvancedAnchor:

    pass
class mm_pictograms_BoxRelativeAnchor(AdvancedAnchor):

    def __init__(self, relativeWidth: float, relativeHeight: float):
        self.relativeWidth = relativeWidth
        self.relativeHeight = relativeHeight
        
    @property
    def relativeWidth(self) -> float:
        return self.__relativeWidth

    @relativeWidth.setter
    def relativeWidth(self, relativeWidth: float):
        self.__relativeWidth = relativeWidth

    @property
    def relativeHeight(self) -> float:
        return self.__relativeHeight

    @relativeHeight.setter
    def relativeHeight(self, relativeHeight: float):
        self.__relativeHeight = relativeHeight

class mm_pictograms_FixPointAnchor(AdvancedAnchor):

    pass
class PictogramElement:

    pass
class mm_pictograms_AnchorContainer(PictogramElement):

    pass
class mm_pictograms_Anchor(PictogramElement):

    pass
class ConnectionDecorator:

    pass
class styles_Font:

    pass
class Diagram:

    pass
class styles_Color:

    pass
class Anchor:

    pass
class mm_pictograms_ChopboxAnchor(Anchor):

    pass
class mm_pictograms_AdvancedAnchor(Anchor):

    def __init__(self, useAnchorLocationAsConnectionEndpoint: bool, pictograms21: "mm_pictograms_Connection", pictograms18: "mm_pictograms_Connection", pictograms38: "mm_pictograms_AnchorContainer"):
        self.useAnchorLocationAsConnectionEndpoint = useAnchorLocationAsConnectionEndpoint
        
    @property
    def useAnchorLocationAsConnectionEndpoint(self) -> bool:
        return self.__useAnchorLocationAsConnectionEndpoint

    @useAnchorLocationAsConnectionEndpoint.setter
    def useAnchorLocationAsConnectionEndpoint(self, useAnchorLocationAsConnectionEndpoint: bool):
        self.__useAnchorLocationAsConnectionEndpoint = useAnchorLocationAsConnectionEndpoint

class GraphicsAlgorithm:

    pass
class mm_algorithms_Image(GraphicsAlgorithm):

    def __init__(self, id: str, stretchH: str, stretchV: str, proportional: str, algorithms13: "mm_pictograms_PictogramElement", algorithms55: "mm_algorithms_GraphicsAlgorithm", algorithms52: "mm_algorithms_GraphicsAlgorithm", GraphicsAlgorithm35: "mm_pictograms_Anchor"):
        self.id = id
        self.stretchH = stretchH
        self.stretchV = stretchV
        self.proportional = proportional
        
    @property
    def proportional(self) -> str:
        return self.__proportional

    @proportional.setter
    def proportional(self, proportional: str):
        self.__proportional = proportional

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def stretchV(self) -> str:
        return self.__stretchV

    @stretchV.setter
    def stretchV(self, stretchV: str):
        self.__stretchV = stretchV

    @property
    def stretchH(self) -> str:
        return self.__stretchH

    @stretchH.setter
    def stretchH(self, stretchH: str):
        self.__stretchH = stretchH

class mm_algorithms_PlatformGraphicsAlgorithm(GraphicsAlgorithm):

    def __init__(self, id: str, algorithms13: "mm_pictograms_PictogramElement", algorithms55: "mm_algorithms_GraphicsAlgorithm", algorithms52: "mm_algorithms_GraphicsAlgorithm", GraphicsAlgorithm35: "mm_pictograms_Anchor"):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class mm_algorithms_RoundedRectangle(GraphicsAlgorithm):

    def __init__(self, cornerHeight: int, cornerWidth: int, algorithms13: "mm_pictograms_PictogramElement", algorithms55: "mm_algorithms_GraphicsAlgorithm", algorithms52: "mm_algorithms_GraphicsAlgorithm", GraphicsAlgorithm35: "mm_pictograms_Anchor"):
        self.cornerHeight = cornerHeight
        self.cornerWidth = cornerWidth
        
    @property
    def cornerWidth(self) -> int:
        return self.__cornerWidth

    @cornerWidth.setter
    def cornerWidth(self, cornerWidth: int):
        self.__cornerWidth = cornerWidth

    @property
    def cornerHeight(self) -> int:
        return self.__cornerHeight

    @cornerHeight.setter
    def cornerHeight(self, cornerHeight: int):
        self.__cornerHeight = cornerHeight

class mm_algorithms_Ellipse(GraphicsAlgorithm):

    pass
class mm_algorithms_AbstractText(GraphicsAlgorithm):

    def __init__(self, horizontalAlignment: str, verticalAlignment: str, angle: str, value: str, mm_algorithms_AbstractText65: set["styles_TextStyleRegion"] = None, mm_algorithms_AbstractText: "styles_Font" = None, algorithms13: "mm_pictograms_PictogramElement", algorithms55: "mm_algorithms_GraphicsAlgorithm", algorithms52: "mm_algorithms_GraphicsAlgorithm", GraphicsAlgorithm35: "mm_pictograms_Anchor"):
        self.horizontalAlignment = horizontalAlignment
        self.verticalAlignment = verticalAlignment
        self.angle = angle
        self.value = value
        self.mm_algorithms_AbstractText65 = mm_algorithms_AbstractText65 if mm_algorithms_AbstractText65 is not None else set()
        self.mm_algorithms_AbstractText = mm_algorithms_AbstractText
        
    @property
    def horizontalAlignment(self) -> str:
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment

    @property
    def verticalAlignment(self) -> str:
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment

    @property
    def angle(self) -> str:
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
            if hasattr(old_value, "styles_Font63"):
                opp_val = getattr(old_value, "styles_Font63", None)
                if opp_val == self:
                    setattr(old_value, "styles_Font63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Font63"):
                opp_val = getattr(value, "styles_Font63", None)
                setattr(value, "styles_Font63", self)

    @property
    def mm_algorithms_AbstractText65(self):
        return self.__mm_algorithms_AbstractText65

    @mm_algorithms_AbstractText65.setter
    def mm_algorithms_AbstractText65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_algorithms_AbstractText__mm_algorithms_AbstractText65", None)
        self.__mm_algorithms_AbstractText65 = value if value is not None else set()
        
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
                    

class mm_algorithms_Polyline(GraphicsAlgorithm):

    pass
class mm_algorithms_Rectangle(GraphicsAlgorithm):

    pass
class GraphicsAlgorithmContainer:

    pass
class mm_algorithms_GraphicsAlgorithm(styles_AbstractStyle, GraphicsAlgorithmContainer):

    def __init__(self, width: int, height: int, x: int, y: int, GraphicsAlgorithm51: set["GraphicsAlgorithm"] = None, GraphicsAlgorithm54: "GraphicsAlgorithm" = None, PictogramElement57: "PictogramElement" = None, mm_algorithms_GraphicsAlgorithm: "styles_Style" = None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.GraphicsAlgorithm51 = GraphicsAlgorithm51 if GraphicsAlgorithm51 is not None else set()
        self.GraphicsAlgorithm54 = GraphicsAlgorithm54
        self.PictogramElement57 = PictogramElement57
        self.mm_algorithms_GraphicsAlgorithm = mm_algorithms_GraphicsAlgorithm
        
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
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

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
            if hasattr(old_value, "styles_Style"):
                opp_val = getattr(old_value, "styles_Style", None)
                if opp_val == self:
                    setattr(old_value, "styles_Style", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Style"):
                opp_val = getattr(value, "styles_Style", None)
                setattr(value, "styles_Style", self)

    @property
    def GraphicsAlgorithm54(self):
        return self.__GraphicsAlgorithm54

    @GraphicsAlgorithm54.setter
    def GraphicsAlgorithm54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_algorithms_GraphicsAlgorithm__GraphicsAlgorithm54", None)
        self.__GraphicsAlgorithm54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "algorithms55"):
                opp_val = getattr(old_value, "algorithms55", None)
                if opp_val == self:
                    setattr(old_value, "algorithms55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "algorithms55"):
                opp_val = getattr(value, "algorithms55", None)
                setattr(value, "algorithms55", self)

    @property
    def GraphicsAlgorithm51(self):
        return self.__GraphicsAlgorithm51

    @GraphicsAlgorithm51.setter
    def GraphicsAlgorithm51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_algorithms_GraphicsAlgorithm__GraphicsAlgorithm51", None)
        self.__GraphicsAlgorithm51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "algorithms52"):
                    opp_val = getattr(item, "algorithms52", None)
                    
                    if opp_val == self:
                        setattr(item, "algorithms52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "algorithms52"):
                    opp_val = getattr(item, "algorithms52", None)
                    
                    setattr(item, "algorithms52", self)
                    

    @property
    def PictogramElement57(self):
        return self.__PictogramElement57

    @PictogramElement57.setter
    def PictogramElement57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_algorithms_GraphicsAlgorithm__PictogramElement57", None)
        self.__PictogramElement57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pictograms58"):
                opp_val = getattr(old_value, "pictograms58", None)
                if opp_val == self:
                    setattr(old_value, "pictograms58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pictograms58"):
                opp_val = getattr(value, "pictograms58", None)
                setattr(value, "pictograms58", self)

class mm_pictograms_PictogramElement(GraphicsAlgorithmContainer):

    def __init__(self, visible: bool, active: bool, GraphicsAlgorithm: "GraphicsAlgorithm" = None, PictogramLink15: "PictogramLink" = None):
        self.visible = visible
        self.active = active
        self.GraphicsAlgorithm = GraphicsAlgorithm
        self.PictogramLink15 = PictogramLink15
        
    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def PictogramLink15(self):
        return self.__PictogramLink15

    @PictogramLink15.setter
    def PictogramLink15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_PictogramElement__PictogramLink15", None)
        self.__PictogramLink15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pictograms16"):
                opp_val = getattr(old_value, "pictograms16", None)
                if opp_val == self:
                    setattr(old_value, "pictograms16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pictograms16"):
                opp_val = getattr(value, "pictograms16", None)
                setattr(value, "pictograms16", self)

    @property
    def GraphicsAlgorithm(self):
        return self.__GraphicsAlgorithm

    @GraphicsAlgorithm.setter
    def GraphicsAlgorithm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_PictogramElement__GraphicsAlgorithm", None)
        self.__GraphicsAlgorithm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "algorithms13"):
                opp_val = getattr(old_value, "algorithms13", None)
                if opp_val == self:
                    setattr(old_value, "algorithms13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "algorithms13"):
                opp_val = getattr(value, "algorithms13", None)
                setattr(value, "algorithms13", self)

class ContainerShape:

    pass
class PictogramLink:

    pass
class AnchorContainer:

    pass
class mm_pictograms_Connection(AnchorContainer):

    pass
class mm_pictograms_Shape(AnchorContainer):

    pass
class Connection:

    pass
class mm_pictograms_CurvedConnection(Connection):

    pass
class mm_pictograms_FreeFormConnection(Connection):

    pass
class mm_pictograms_CompositeConnection(Connection):

    pass
class mm_pictograms_ManhattanConnection(Connection):

    pass
class StyleContainer:

    pass
class mm_styles_Style(styles_AbstractStyle, StyleContainer):

    def __init__(self, id: str, description: str, horizontalAlignment: str, verticalAlignment: str, angle: str, stretchH: str, stretchV: str, proportional: str, mm_styles_Style: "styles_Font" = None, styles70: "styles_mm_StyleContainer" = None):
        self.id = id
        self.description = description
        self.horizontalAlignment = horizontalAlignment
        self.verticalAlignment = verticalAlignment
        self.angle = angle
        self.stretchH = stretchH
        self.stretchV = stretchV
        self.proportional = proportional
        self.mm_styles_Style = mm_styles_Style
        self.styles70 = styles70
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def stretchV(self) -> str:
        return self.__stretchV

    @stretchV.setter
    def stretchV(self, stretchV: str):
        self.__stretchV = stretchV

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def proportional(self) -> str:
        return self.__proportional

    @proportional.setter
    def proportional(self, proportional: str):
        self.__proportional = proportional

    @property
    def verticalAlignment(self) -> str:
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment

    @property
    def horizontalAlignment(self) -> str:
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment

    @property
    def angle(self) -> str:
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle

    @property
    def stretchH(self) -> str:
        return self.__stretchH

    @stretchH.setter
    def stretchH(self, stretchH: str):
        self.__stretchH = stretchH

    @property
    def styles70(self):
        return self.__styles70

    @styles70.setter
    def styles70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_Style__styles70", None)
        self.__styles70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleContainer"):
                opp_val = getattr(old_value, "StyleContainer", None)
                if opp_val == self:
                    setattr(old_value, "StyleContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleContainer"):
                opp_val = getattr(value, "StyleContainer", None)
                setattr(value, "StyleContainer", self)

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
            if hasattr(old_value, "styles_Font68"):
                opp_val = getattr(old_value, "styles_Font68", None)
                if opp_val == self:
                    setattr(old_value, "styles_Font68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Font68"):
                opp_val = getattr(value, "styles_Font68", None)
                setattr(value, "styles_Font68", self)

class pictograms_ContainerShape:

    pass
class mm_pictograms_Diagram(pictograms_ContainerShape, StyleContainer):

    def __init__(self, gridUnit: int, diagramTypeId: str, name: str, snapToGrid: bool, showGuides: bool, verticalGridUnit: int, version: str, Connection: set["Connection"] = None, mm_pictograms_Diagram11: set["PictogramLink"] = None, mm_pictograms_Diagram: set["styles_Color"] = None, mm_pictograms_Diagram9: set["styles_Font"] = None):
        self.gridUnit = gridUnit
        self.diagramTypeId = diagramTypeId
        self.name = name
        self.snapToGrid = snapToGrid
        self.showGuides = showGuides
        self.verticalGridUnit = verticalGridUnit
        self.version = version
        self.Connection = Connection if Connection is not None else set()
        self.mm_pictograms_Diagram11 = mm_pictograms_Diagram11 if mm_pictograms_Diagram11 is not None else set()
        self.mm_pictograms_Diagram = mm_pictograms_Diagram if mm_pictograms_Diagram is not None else set()
        self.mm_pictograms_Diagram9 = mm_pictograms_Diagram9 if mm_pictograms_Diagram9 is not None else set()
        
    @property
    def showGuides(self) -> bool:
        return self.__showGuides

    @showGuides.setter
    def showGuides(self, showGuides: bool):
        self.__showGuides = showGuides

    @property
    def gridUnit(self) -> int:
        return self.__gridUnit

    @gridUnit.setter
    def gridUnit(self, gridUnit: int):
        self.__gridUnit = gridUnit

    @property
    def verticalGridUnit(self) -> int:
        return self.__verticalGridUnit

    @verticalGridUnit.setter
    def verticalGridUnit(self, verticalGridUnit: int):
        self.__verticalGridUnit = verticalGridUnit

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def diagramTypeId(self) -> str:
        return self.__diagramTypeId

    @diagramTypeId.setter
    def diagramTypeId(self, diagramTypeId: str):
        self.__diagramTypeId = diagramTypeId

    @property
    def snapToGrid(self) -> bool:
        return self.__snapToGrid

    @snapToGrid.setter
    def snapToGrid(self, snapToGrid: bool):
        self.__snapToGrid = snapToGrid

    @property
    def Connection(self):
        return self.__Connection

    @Connection.setter
    def Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_Diagram__Connection", None)
        self.__Connection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pictograms6"):
                    opp_val = getattr(item, "pictograms6", None)
                    
                    if opp_val == self:
                        setattr(item, "pictograms6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pictograms6"):
                    opp_val = getattr(item, "pictograms6", None)
                    
                    setattr(item, "pictograms6", self)
                    

    @property
    def mm_pictograms_Diagram11(self):
        return self.__mm_pictograms_Diagram11

    @mm_pictograms_Diagram11.setter
    def mm_pictograms_Diagram11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_Diagram__mm_pictograms_Diagram11", None)
        self.__mm_pictograms_Diagram11 = value if value is not None else set()
        
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
                    

class Shape:

    pass
class mm_pictograms_ConnectionDecorator(Shape):

    def __init__(self, locationRelative: bool, location: float, Connection41: "Connection" = None, pictograms4: "mm_pictograms_ContainerShape"):
        self.locationRelative = locationRelative
        self.location = location
        self.Connection41 = Connection41
        
    @property
    def locationRelative(self) -> bool:
        return self.__locationRelative

    @locationRelative.setter
    def locationRelative(self, locationRelative: bool):
        self.__locationRelative = locationRelative

    @property
    def location(self) -> float:
        return self.__location

    @location.setter
    def location(self, location: float):
        self.__location = location

    @property
    def Connection41(self):
        return self.__Connection41

    @Connection41.setter
    def Connection41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_pictograms_ConnectionDecorator__Connection41", None)
        self.__Connection41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pictograms42"):
                opp_val = getattr(old_value, "pictograms42", None)
                if opp_val == self:
                    setattr(old_value, "pictograms42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pictograms42"):
                opp_val = getattr(value, "pictograms42", None)
                setattr(value, "pictograms42", self)

class mm_pictograms_ContainerShape(Shape):

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
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
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
