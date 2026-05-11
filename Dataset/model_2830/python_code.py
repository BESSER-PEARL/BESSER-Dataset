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

class mm_styles_TextStyle:

    def __init__(self, underline: bool, underlineStyle: str, strikeout: bool, mm_styles_TextStyle: "styles_Font" = None, mm_styles_TextStyle73: "styles_Color" = None, mm_styles_TextStyle76: "styles_Color" = None, mm_styles_TextStyle79: "styles_Color" = None, mm_styles_TextStyle82: "styles_Color" = None):
        self.underline = underline
        self.underlineStyle = underlineStyle
        self.strikeout = strikeout
        self.mm_styles_TextStyle = mm_styles_TextStyle
        self.mm_styles_TextStyle73 = mm_styles_TextStyle73
        self.mm_styles_TextStyle76 = mm_styles_TextStyle76
        self.mm_styles_TextStyle79 = mm_styles_TextStyle79
        self.mm_styles_TextStyle82 = mm_styles_TextStyle82
        
        pass
    @property
    def underlineStyle(self):
        return self.__underlineStyle

    @underlineStyle.setter
    def underlineStyle(self, underlineStyle: str):
        self.__underlineStyle = underlineStyle


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
    def mm_styles_TextStyle79(self):
        return self.__mm_styles_TextStyle79

    @mm_styles_TextStyle79.setter
    def mm_styles_TextStyle79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle79", None)
        self.__mm_styles_TextStyle79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color80"):
                opp_val = getattr(old_value, "styles_Color80", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color80"):
                opp_val = getattr(value, "styles_Color80", None)
                setattr(value, "styles_Color80", self)

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
            if hasattr(old_value, "styles_Font71"):
                opp_val = getattr(old_value, "styles_Font71", None)
                if opp_val == self:
                    setattr(old_value, "styles_Font71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Font71"):
                opp_val = getattr(value, "styles_Font71", None)
                setattr(value, "styles_Font71", self)

    @property
    def mm_styles_TextStyle73(self):
        return self.__mm_styles_TextStyle73

    @mm_styles_TextStyle73.setter
    def mm_styles_TextStyle73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle73", None)
        self.__mm_styles_TextStyle73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color74"):
                opp_val = getattr(old_value, "styles_Color74", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color74"):
                opp_val = getattr(value, "styles_Color74", None)
                setattr(value, "styles_Color74", self)

    @property
    def mm_styles_TextStyle82(self):
        return self.__mm_styles_TextStyle82

    @mm_styles_TextStyle82.setter
    def mm_styles_TextStyle82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle82", None)
        self.__mm_styles_TextStyle82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color83"):
                opp_val = getattr(old_value, "styles_Color83", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color83"):
                opp_val = getattr(value, "styles_Color83", None)
                setattr(value, "styles_Color83", self)

    @property
    def mm_styles_TextStyle76(self):
        return self.__mm_styles_TextStyle76

    @mm_styles_TextStyle76.setter
    def mm_styles_TextStyle76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_TextStyle__mm_styles_TextStyle76", None)
        self.__mm_styles_TextStyle76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color77"):
                opp_val = getattr(old_value, "styles_Color77", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color77"):
                opp_val = getattr(value, "styles_Color77", None)
                setattr(value, "styles_Color77", self)

class mm_styles_PrecisionPoint:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y


class mm_styles_Color:

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue
        
        pass
    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue


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


class mm_styles_Point:

    def __init__(self, x: int, y: int, before: int, after: int):
        self.x = x
        self.y = y
        self.before = before
        self.after = after
        
        pass
    @property
    def before(self):
        return self.__before

    @before.setter
    def before(self, before: int):
        self.__before = before


    @property
    def after(self):
        return self.__after

    @after.setter
    def after(self, after: int):
        self.__after = after


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

class mm_styles_AbstractStyle(ABC):

    def __init__(self, lineVisible: str, transparency: str, lineWidth: str, lineStyle: str, filled: str, mm_styles_AbstractStyle61: "styles_RenderingStyle" = None, mm_styles_AbstractStyle: "styles_Color" = None, mm_styles_AbstractStyle58: "styles_Color" = None):
        self.lineVisible = lineVisible
        self.transparency = transparency
        self.lineWidth = lineWidth
        self.lineStyle = lineStyle
        self.filled = filled
        self.mm_styles_AbstractStyle61 = mm_styles_AbstractStyle61
        self.mm_styles_AbstractStyle = mm_styles_AbstractStyle
        self.mm_styles_AbstractStyle58 = mm_styles_AbstractStyle58
        
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
    def transparency(self):
        return self.__transparency

    @transparency.setter
    def transparency(self, transparency: str):
        self.__transparency = transparency


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
    def mm_styles_AbstractStyle(self):
        return self.__mm_styles_AbstractStyle

    @mm_styles_AbstractStyle.setter
    def mm_styles_AbstractStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_AbstractStyle__mm_styles_AbstractStyle", None)
        self.__mm_styles_AbstractStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color56"):
                opp_val = getattr(old_value, "styles_Color56", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color56"):
                opp_val = getattr(value, "styles_Color56", None)
                setattr(value, "styles_Color56", self)

    @property
    def mm_styles_AbstractStyle58(self):
        return self.__mm_styles_AbstractStyle58

    @mm_styles_AbstractStyle58.setter
    def mm_styles_AbstractStyle58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_AbstractStyle__mm_styles_AbstractStyle58", None)
        self.__mm_styles_AbstractStyle58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color59"):
                opp_val = getattr(old_value, "styles_Color59", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color59"):
                opp_val = getattr(value, "styles_Color59", None)
                setattr(value, "styles_Color59", self)

    @property
    def mm_styles_AbstractStyle61(self):
        return self.__mm_styles_AbstractStyle61

    @mm_styles_AbstractStyle61.setter
    def mm_styles_AbstractStyle61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_AbstractStyle__mm_styles_AbstractStyle61", None)
        self.__mm_styles_AbstractStyle61 = value
        
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
class mm_styles_Font:

    def __init__(self, bold: bool, name: str, size: int, italic: bool):
        self.bold = bold
        self.name = name
        self.size = size
        self.italic = italic
        
        pass
    @property
    def bold(self):
        return self.__bold

    @bold.setter
    def bold(self, bold: bool):
        self.__bold = bold


    @property
    def italic(self):
        return self.__italic

    @italic.setter
    def italic(self, italic: bool):
        self.__italic = italic


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size


class styles_GradientColoredAreas:

    pass
class mm_styles_AdaptedGradientColoredAreas:

    def __init__(self, definedStyleId: str, gradientType: str, mm_styles_AdaptedGradientColoredAreas: set["styles_GradientColoredAreas"] = None):
        self.definedStyleId = definedStyleId
        self.gradientType = gradientType
        self.mm_styles_AdaptedGradientColoredAreas = mm_styles_AdaptedGradientColoredAreas if mm_styles_AdaptedGradientColoredAreas is not None else set()
        
        pass
    @property
    def definedStyleId(self):
        return self.__definedStyleId

    @definedStyleId.setter
    def definedStyleId(self, definedStyleId: str):
        self.__definedStyleId = definedStyleId


    @property
    def gradientType(self):
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
class mm_styles_GradientColoredLocation:

    def __init__(self, locationType: str, locationValue: str, mm_styles_GradientColoredLocation: "styles_Color" = None):
        self.locationType = locationType
        self.locationValue = locationValue
        self.mm_styles_GradientColoredLocation = mm_styles_GradientColoredLocation
        
        pass
    @property
    def locationValue(self):
        return self.__locationValue

    @locationValue.setter
    def locationValue(self, locationValue: str):
        self.__locationValue = locationValue


    @property
    def locationType(self):
        return self.__locationType

    @locationType.setter
    def locationType(self, locationType: str):
        self.__locationType = locationType


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
            if hasattr(old_value, "styles_Color63"):
                opp_val = getattr(old_value, "styles_Color63", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color63"):
                opp_val = getattr(value, "styles_Color63", None)
                setattr(value, "styles_Color63", self)

class styles_RenderingStyle:

    pass
class styles_TextStyleRegion:

    pass
class styles_AdaptedGradientColoredAreas:

    pass
class mm_styles_RenderingStyle:

    pass
class styles_AbstractStyle:

    pass
class CurvedConnection:

    pass
class styles_PrecisionPoint:

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
class pictograms_mm_EObject:

    pass
class mm_pictograms_BoxRelativeAnchor(AdvancedAnchor):

    def __init__(self, relativeWidth: float, relativeHeight: float):
        self.relativeWidth = relativeWidth
        self.relativeHeight = relativeHeight
        
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


class styles_Font:

    pass
class styles_Color:

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
class mm_styles_Style(StyleContainer, styles_AbstractStyle):

    def __init__(self, id: str, description: str, horizontalAlignment: str, verticalAlignment: str, angle: str, stretchH: str, stretchV: str, proportional: str, rotation: str, mm_styles_Style: "styles_Font" = None, styles: "styles_mm_StyleContainer" = None):
        self.id = id
        self.description = description
        self.horizontalAlignment = horizontalAlignment
        self.verticalAlignment = verticalAlignment
        self.angle = angle
        self.stretchH = stretchH
        self.stretchV = stretchV
        self.proportional = proportional
        self.rotation = rotation
        self.mm_styles_Style = mm_styles_Style
        self.styles = styles
        
        pass
    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle


    @property
    def stretchH(self):
        return self.__stretchH

    @stretchH.setter
    def stretchH(self, stretchH: str):
        self.__stretchH = stretchH


    @property
    def proportional(self):
        return self.__proportional

    @proportional.setter
    def proportional(self, proportional: str):
        self.__proportional = proportional


    @property
    def horizontalAlignment(self):
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def stretchV(self):
        return self.__stretchV

    @stretchV.setter
    def stretchV(self, stretchV: str):
        self.__stretchV = stretchV


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def verticalAlignment(self):
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


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
            if hasattr(old_value, "styles_Font53"):
                opp_val = getattr(old_value, "styles_Font53", None)
                if opp_val == self:
                    setattr(old_value, "styles_Font53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Font53"):
                opp_val = getattr(value, "styles_Font53", None)
                setattr(value, "styles_Font53", self)

    @property
    def styles(self):
        return self.__styles

    @styles.setter
    def styles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_styles_Style__styles", None)
        self.__styles = value
        
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

class pictograms_ContainerShape:

    pass
class mm_pictograms_Diagram(StyleContainer, pictograms_ContainerShape):

    def __init__(self, verticalGridUnit: int, version: str, gridUnit: int, diagramTypeId: str, name: str, snapToGrid: bool, showGuides: bool, mm_pictograms_Diagram9: set["PictogramLink"] = None, parent: set["Connection"] = None, mm_pictograms_Diagram: set["styles_Color"] = None, mm_pictograms_Diagram7: set["styles_Font"] = None):
        self.verticalGridUnit = verticalGridUnit
        self.version = version
        self.gridUnit = gridUnit
        self.diagramTypeId = diagramTypeId
        self.name = name
        self.snapToGrid = snapToGrid
        self.showGuides = showGuides
        self.mm_pictograms_Diagram9 = mm_pictograms_Diagram9 if mm_pictograms_Diagram9 is not None else set()
        self.parent = parent if parent is not None else set()
        self.mm_pictograms_Diagram = mm_pictograms_Diagram if mm_pictograms_Diagram is not None else set()
        self.mm_pictograms_Diagram7 = mm_pictograms_Diagram7 if mm_pictograms_Diagram7 is not None else set()
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def verticalGridUnit(self):
        return self.__verticalGridUnit

    @verticalGridUnit.setter
    def verticalGridUnit(self, verticalGridUnit: int):
        self.__verticalGridUnit = verticalGridUnit


    @property
    def showGuides(self):
        return self.__showGuides

    @showGuides.setter
    def showGuides(self, showGuides: bool):
        self.__showGuides = showGuides


    @property
    def diagramTypeId(self):
        return self.__diagramTypeId

    @diagramTypeId.setter
    def diagramTypeId(self, diagramTypeId: str):
        self.__diagramTypeId = diagramTypeId


    @property
    def snapToGrid(self):
        return self.__snapToGrid

    @snapToGrid.setter
    def snapToGrid(self, snapToGrid: bool):
        self.__snapToGrid = snapToGrid


    @property
    def gridUnit(self):
        return self.__gridUnit

    @gridUnit.setter
    def gridUnit(self, gridUnit: int):
        self.__gridUnit = gridUnit


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
                    

class Diagram:

    pass
class Anchor:

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


class mm_pictograms_ChopboxAnchor(Anchor):

    pass
class GraphicsAlgorithm:

    pass
class mm_algorithms_Image(GraphicsAlgorithm):

    def __init__(self, id: str, stretchH: str, stretchV: str, proportional: str, GraphicsAlgorithm39: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm25: "mm_pictograms_Anchor" = None, GraphicsAlgorithm: "mm_pictograms_PictogramElement" = None, GraphicsAlgorithm41: "mm_algorithms_GraphicsAlgorithm" = None):
        self.id = id
        self.stretchH = stretchH
        self.stretchV = stretchV
        self.proportional = proportional
        
        pass
    @property
    def proportional(self):
        return self.__proportional

    @proportional.setter
    def proportional(self, proportional: str):
        self.__proportional = proportional


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
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class mm_algorithms_Rectangle(GraphicsAlgorithm):

    pass
class mm_algorithms_AbstractText(GraphicsAlgorithm):

    def __init__(self, rotation: str, horizontalAlignment: str, verticalAlignment: str, angle: str, value: str, mm_algorithms_AbstractText: "styles_Font" = None, mm_algorithms_AbstractText50: set["styles_TextStyleRegion"] = None, GraphicsAlgorithm39: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm25: "mm_pictograms_Anchor" = None, GraphicsAlgorithm: "mm_pictograms_PictogramElement" = None, GraphicsAlgorithm41: "mm_algorithms_GraphicsAlgorithm" = None):
        self.rotation = rotation
        self.horizontalAlignment = horizontalAlignment
        self.verticalAlignment = verticalAlignment
        self.angle = angle
        self.value = value
        self.mm_algorithms_AbstractText = mm_algorithms_AbstractText
        self.mm_algorithms_AbstractText50 = mm_algorithms_AbstractText50 if mm_algorithms_AbstractText50 is not None else set()
        
        pass
    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


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
    def verticalAlignment(self):
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment


    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle


    @property
    def mm_algorithms_AbstractText50(self):
        return self.__mm_algorithms_AbstractText50

    @mm_algorithms_AbstractText50.setter
    def mm_algorithms_AbstractText50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm_algorithms_AbstractText__mm_algorithms_AbstractText50", None)
        self.__mm_algorithms_AbstractText50 = value if value is not None else set()
        
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
            if hasattr(old_value, "styles_Font48"):
                opp_val = getattr(old_value, "styles_Font48", None)
                if opp_val == self:
                    setattr(old_value, "styles_Font48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Font48"):
                opp_val = getattr(value, "styles_Font48", None)
                setattr(value, "styles_Font48", self)

class mm_algorithms_Ellipse(GraphicsAlgorithm):

    pass
class mm_algorithms_PlatformGraphicsAlgorithm(GraphicsAlgorithm):

    def __init__(self, id: str, GraphicsAlgorithm39: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm25: "mm_pictograms_Anchor" = None, GraphicsAlgorithm: "mm_pictograms_PictogramElement" = None, GraphicsAlgorithm41: "mm_algorithms_GraphicsAlgorithm" = None):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class mm_algorithms_Polyline(GraphicsAlgorithm):

    pass
class mm_algorithms_RoundedRectangle(GraphicsAlgorithm):

    def __init__(self, cornerHeight: int, cornerWidth: int, GraphicsAlgorithm39: "mm_algorithms_GraphicsAlgorithm" = None, GraphicsAlgorithm25: "mm_pictograms_Anchor" = None, GraphicsAlgorithm: "mm_pictograms_PictogramElement" = None, GraphicsAlgorithm41: "mm_algorithms_GraphicsAlgorithm" = None):
        self.cornerHeight = cornerHeight
        self.cornerWidth = cornerWidth
        
        pass
    @property
    def cornerWidth(self):
        return self.__cornerWidth

    @cornerWidth.setter
    def cornerWidth(self, cornerWidth: int):
        self.__cornerWidth = cornerWidth


    @property
    def cornerHeight(self):
        return self.__cornerHeight

    @cornerHeight.setter
    def cornerHeight(self, cornerHeight: int):
        self.__cornerHeight = cornerHeight


class GraphicsAlgorithmContainer:

    pass
class mm_algorithms_GraphicsAlgorithm(GraphicsAlgorithmContainer, styles_AbstractStyle):

    def __init__(self, width: int, height: int, x: int, y: int, mm_algorithms_GraphicsAlgorithm: "styles_Style" = None, parentGraphicsAlgorithm: set["GraphicsAlgorithm"] = None, graphicsAlgorithmChildren: "GraphicsAlgorithm" = None, graphicsAlgorithm: "PictogramElement" = None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.mm_algorithms_GraphicsAlgorithm = mm_algorithms_GraphicsAlgorithm
        self.parentGraphicsAlgorithm = parentGraphicsAlgorithm if parentGraphicsAlgorithm is not None else set()
        self.graphicsAlgorithmChildren = graphicsAlgorithmChildren
        self.graphicsAlgorithm = graphicsAlgorithm
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


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

class PictogramLink:

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

class Shape:

    pass
class mm_pictograms_ConnectionDecorator(Shape):

    def __init__(self, locationRelative: bool, location: float, connectionDecorators: "Connection" = None, Shape: "mm_pictograms_ContainerShape" = None):
        self.locationRelative = locationRelative
        self.location = location
        self.connectionDecorators = connectionDecorators
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: float):
        self.__location = location


    @property
    def locationRelative(self):
        return self.__locationRelative

    @locationRelative.setter
    def locationRelative(self, locationRelative: bool):
        self.__locationRelative = locationRelative


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