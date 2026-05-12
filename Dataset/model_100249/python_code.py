from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ColorConstants(Enum):
    WHITE = "WHITE"
    LIGHT_LIGHT_GRAY = "LIGHT_LIGHT_GRAY"
    LIGHT_GRAY = "LIGHT_GRAY"
    GRAY = "GRAY"
    DARK_GRAY = "DARK_GRAY"
    BLACK = "BLACK"
    BLUE = "BLUE"
    DARK_BLUE = "DARK_BLUE"
    RED = "RED"
    LIGHT_ORANGE = "LIGHT_ORANGE"
    ORANGE = "ORANGE"
    DARK_ORANGE = "DARK_ORANGE"
    YELLOW = "YELLOW"
    GREEN = "GREEN"
    LIGHT_GREEN = "LIGHT_GREEN"
    DARK_GREEN = "DARK_GREEN"
    CYAN = "CYAN"
    LIGHT_BLUE = "LIGHT_BLUE"
    NULL = "NULL"
class YesNoBool(Enum):
    YES = "YES"
    NO = "NO"
    NULL = "NULL"
class LineStyle(Enum):
    SOLID = "SOLID"
    DOT = "DOT"
    DASH = "DASH"
    DASHDOT = "DASHDOT"
    DASHDOTDOT = "DASHDOTDOT"
    NULL = "NULL"
class GradientAllignment(Enum):
    VERTICAL = "VERTICAL"
    NULL = "NULL"
    HORIZONTAL = "HORIZONTAL"


############################################
# Definition of Classes
############################################

class Color:

    pass
class styles_ColorConstantRef(Color):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class styles_RGBColor(Color):

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue
        
        pass
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


    @property
    def green(self):
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green


class ColorWithTransparency:

    pass
class ColorOrGradient:

    pass
class styles_GradientRef(ColorOrGradient):

    pass
class styles_Transparent(ColorOrGradient, ColorWithTransparency):

    def __init__(self, transparent: bool):
        self.transparent = transparent
        
        pass
    @property
    def transparent(self):
        return self.__transparent

    @transparent.setter
    def transparent(self, transparent: bool):
        self.__transparent = transparent


class styles_Color(ColorOrGradient, ColorWithTransparency):

    pass
class styles_ColorWithTransparency:

    pass
class styles_GradientColorArea:

    def __init__(self, offset: float, styles_GradientColorArea31: "styles_Color" = None, styles_GradientColorArea: "styles_GradientLayout" = None):
        self.offset = offset
        self.styles_GradientColorArea31 = styles_GradientColorArea31
        self.styles_GradientColorArea = styles_GradientColorArea
        
        pass
    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset: float):
        self.__offset = offset


    @property
    def styles_GradientColorArea(self):
        return self.__styles_GradientColorArea

    @styles_GradientColorArea.setter
    def styles_GradientColorArea(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_styles_GradientColorArea__styles_GradientColorArea", None)
        self.__styles_GradientColorArea = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_GradientLayout17"):
                opp_val = getattr(old_value, "styles_GradientLayout17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_GradientLayout17"):
                opp_val = getattr(value, "styles_GradientLayout17", None)
                if opp_val is None:
                    setattr(value, "styles_GradientLayout17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def styles_GradientColorArea31(self):
        return self.__styles_GradientColorArea31

    @styles_GradientColorArea31.setter
    def styles_GradientColorArea31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_styles_GradientColorArea__styles_GradientColorArea31", None)
        self.__styles_GradientColorArea31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color32"):
                opp_val = getattr(old_value, "styles_Color32", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color32"):
                opp_val = getattr(value, "styles_Color32", None)
                setattr(value, "styles_Color32", self)

class styles_GradientLayout:

    pass
class styles_StyleLayout:

    def __init__(self, transparency: float, gradient_orientation: str, lineWidth: int, lineStyle: str, fontName: str, fontSize: int, fontItalic: str, fontBold: str, styles_StyleLayout9: "styles_ColorOrGradient" = None, styles_StyleLayout: "styles_Style" = None, styles_StyleLayout11: "styles_HighlightingValues" = None, styles_StyleLayout13: "styles_ColorWithTransparency" = None, styles_StyleLayout15: "styles_Color" = None):
        self.transparency = transparency
        self.gradient_orientation = gradient_orientation
        self.lineWidth = lineWidth
        self.lineStyle = lineStyle
        self.fontName = fontName
        self.fontSize = fontSize
        self.fontItalic = fontItalic
        self.fontBold = fontBold
        self.styles_StyleLayout9 = styles_StyleLayout9
        self.styles_StyleLayout = styles_StyleLayout
        self.styles_StyleLayout11 = styles_StyleLayout11
        self.styles_StyleLayout13 = styles_StyleLayout13
        self.styles_StyleLayout15 = styles_StyleLayout15
        
        pass
    @property
    def fontName(self):
        return self.__fontName

    @fontName.setter
    def fontName(self, fontName: str):
        self.__fontName = fontName


    @property
    def transparency(self):
        return self.__transparency

    @transparency.setter
    def transparency(self, transparency: float):
        self.__transparency = transparency


    @property
    def fontSize(self):
        return self.__fontSize

    @fontSize.setter
    def fontSize(self, fontSize: int):
        self.__fontSize = fontSize


    @property
    def lineWidth(self):
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth


    @property
    def gradient_orientation(self):
        return self.__gradient_orientation

    @gradient_orientation.setter
    def gradient_orientation(self, gradient_orientation: str):
        self.__gradient_orientation = gradient_orientation


    @property
    def fontItalic(self):
        return self.__fontItalic

    @fontItalic.setter
    def fontItalic(self, fontItalic: str):
        self.__fontItalic = fontItalic


    @property
    def fontBold(self):
        return self.__fontBold

    @fontBold.setter
    def fontBold(self, fontBold: str):
        self.__fontBold = fontBold


    @property
    def lineStyle(self):
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle


    @property
    def styles_StyleLayout13(self):
        return self.__styles_StyleLayout13

    @styles_StyleLayout13.setter
    def styles_StyleLayout13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_styles_StyleLayout__styles_StyleLayout13", None)
        self.__styles_StyleLayout13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_ColorWithTransparency"):
                opp_val = getattr(old_value, "styles_ColorWithTransparency", None)
                if opp_val == self:
                    setattr(old_value, "styles_ColorWithTransparency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_ColorWithTransparency"):
                opp_val = getattr(value, "styles_ColorWithTransparency", None)
                setattr(value, "styles_ColorWithTransparency", self)

    @property
    def styles_StyleLayout9(self):
        return self.__styles_StyleLayout9

    @styles_StyleLayout9.setter
    def styles_StyleLayout9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_styles_StyleLayout__styles_StyleLayout9", None)
        self.__styles_StyleLayout9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_ColorOrGradient"):
                opp_val = getattr(old_value, "styles_ColorOrGradient", None)
                if opp_val == self:
                    setattr(old_value, "styles_ColorOrGradient", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_ColorOrGradient"):
                opp_val = getattr(value, "styles_ColorOrGradient", None)
                setattr(value, "styles_ColorOrGradient", self)

    @property
    def styles_StyleLayout(self):
        return self.__styles_StyleLayout

    @styles_StyleLayout.setter
    def styles_StyleLayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_styles_StyleLayout__styles_StyleLayout", None)
        self.__styles_StyleLayout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Style6"):
                opp_val = getattr(old_value, "styles_Style6", None)
                if opp_val == self:
                    setattr(old_value, "styles_Style6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Style6"):
                opp_val = getattr(value, "styles_Style6", None)
                setattr(value, "styles_Style6", self)

    @property
    def styles_StyleLayout15(self):
        return self.__styles_StyleLayout15

    @styles_StyleLayout15.setter
    def styles_StyleLayout15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_styles_StyleLayout__styles_StyleLayout15", None)
        self.__styles_StyleLayout15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_Color"):
                opp_val = getattr(old_value, "styles_Color", None)
                if opp_val == self:
                    setattr(old_value, "styles_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_Color"):
                opp_val = getattr(value, "styles_Color", None)
                setattr(value, "styles_Color", self)

    @property
    def styles_StyleLayout11(self):
        return self.__styles_StyleLayout11

    @styles_StyleLayout11.setter
    def styles_StyleLayout11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_styles_StyleLayout__styles_StyleLayout11", None)
        self.__styles_StyleLayout11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_HighlightingValues"):
                opp_val = getattr(old_value, "styles_HighlightingValues", None)
                if opp_val == self:
                    setattr(old_value, "styles_HighlightingValues", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_HighlightingValues"):
                opp_val = getattr(value, "styles_HighlightingValues", None)
                setattr(value, "styles_HighlightingValues", self)

class styles_JvmTypeReference:

    pass
class StyleContainerElement:

    pass
class styles_Gradient(StyleContainerElement):

    pass
class styles_HighlightingValues:

    pass
class styles_ColorOrGradient:

    pass
class styles_StyleContainerElement:

    def __init__(self, name: str, description: str, styles_StyleContainerElement: "styles_StyleContainer" = None):
        self.name = name
        self.description = description
        self.styles_StyleContainerElement = styles_StyleContainerElement
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def styles_StyleContainerElement(self):
        return self.__styles_StyleContainerElement

    @styles_StyleContainerElement.setter
    def styles_StyleContainerElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_styles_StyleContainerElement__styles_StyleContainerElement", None)
        self.__styles_StyleContainerElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "styles_StyleContainer"):
                opp_val = getattr(old_value, "styles_StyleContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "styles_StyleContainer"):
                opp_val = getattr(value, "styles_StyleContainer", None)
                if opp_val is None:
                    setattr(value, "styles_StyleContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class styles_StyleContainer:

    pass
class styles_Style(StyleContainerElement):

    pass