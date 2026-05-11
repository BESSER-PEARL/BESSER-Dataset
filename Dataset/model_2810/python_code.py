from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Arc(Enum):
    OPEN = "OPEN"
    CHORD = "CHORD"
    PIE = "PIE"
class LineCap(Enum):
    CAP_FLAT = "CAP_FLAT"
    CAP_ROUND = "CAP_ROUND"
    CAP_SQUARE = "CAP_SQUARE"
class LineJoin(Enum):
    JOIN_MITER = "JOIN_MITER"
    JOIN_ROUND = "JOIN_ROUND"
    JOIN_BEVEL = "JOIN_BEVEL"
class Underline(Enum):
    NONE = "NONE"
    SINGLE = "SINGLE"
    DOUBLE = "DOUBLE"
    ERROR = "ERROR"
    SQUIGGLE = "SQUIGGLE"
    LINK = "LINK"
class LineStyle(Enum):
    DASHDOTDOT = "DASHDOTDOT"
    CUSTOM = "CUSTOM"
    SOLID = "SOLID"
    DASH = "DASH"
    DOT = "DOT"
    DASHDOT = "DASHDOT"
class Trigger(Enum):
    SINGLECLICK = "SINGLECLICK"
    MIDDLE_SINGLE_OR_MULTICLICK = "MIDDLE_SINGLE_OR_MULTICLICK"
    DOUBLECLICK = "DOUBLECLICK"
    SINGLE_OR_MULTICLICK = "SINGLE_OR_MULTICLICK"
    MIDDLE_SINGLECLICK = "MIDDLE_SINGLECLICK"
    MIDDLE_DOUBLECLICK = "MIDDLE_DOUBLECLICK"
class VerticalAlignment(Enum):
    TOP = "TOP"
    CENTER = "CENTER"
    BOTTOM = "BOTTOM"
class HorizontalAlignment(Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"


############################################
# Definition of Classes
############################################

class krendering_KBackground:

    pass
class krendering_KForeground:

    pass
class krendering_KYPosition(ABC):

    def __init__(self, absolute: float, relative: float):
        self.absolute = absolute
        self.relative = relative
        
        pass
    @property
    def relative(self):
        return self.__relative

    @relative.setter
    def relative(self, relative: float):
        self.__relative = relative


    @property
    def absolute(self):
        return self.__absolute

    @absolute.setter
    def absolute(self, absolute: float):
        self.__absolute = absolute


    def setPosition(self, krendering_relative, krendering_absolute):
        # TODO: Implement setPosition method
        pass

    def equals(self, krendering_other) :
        # TODO: Implement equals method
        pass

class krendering_KBottomPosition:

    pass
class krendering_KTopPosition:

    pass
class krendering_KRightPosition:

    pass
class krendering_KLeftPosition:

    pass
class krendering_KXPosition(ABC):

    def __init__(self, absolute: float, relative: float):
        self.absolute = absolute
        self.relative = relative
        
        pass
    @property
    def absolute(self):
        return self.__absolute

    @absolute.setter
    def absolute(self, absolute: float):
        self.__absolute = absolute


    @property
    def relative(self):
        return self.__relative

    @relative.setter
    def relative(self, relative: float):
        self.__relative = relative


    def setPosition(self, krendering_absolute, krendering_relative):
        # TODO: Implement setPosition method
        pass

    def equals(self, krendering_other) :
        # TODO: Implement equals method
        pass

class krendering_KColor:

    def __init__(self, red: int, green: int, blue: int, krendering_KColor: "krendering_KColoring" = None, krendering_KColor28: "krendering_KColoring" = None, krendering_KColor36: "krendering_KShadow" = None, krendering_KColor38: "krendering_KTextUnderline" = None, krendering_KColor42: "krendering_KTextStrikeout" = None):
        self.red = red
        self.green = green
        self.blue = blue
        self.krendering_KColor = krendering_KColor
        self.krendering_KColor28 = krendering_KColor28
        self.krendering_KColor36 = krendering_KColor36
        self.krendering_KColor38 = krendering_KColor38
        self.krendering_KColor42 = krendering_KColor42
        
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


    @property
    def krendering_KColor36(self):
        return self.__krendering_KColor36

    @krendering_KColor36.setter
    def krendering_KColor36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KColor__krendering_KColor36", None)
        self.__krendering_KColor36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KShadow"):
                opp_val = getattr(old_value, "krendering_KShadow", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KShadow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KShadow"):
                opp_val = getattr(value, "krendering_KShadow", None)
                setattr(value, "krendering_KShadow", self)

    @property
    def krendering_KColor38(self):
        return self.__krendering_KColor38

    @krendering_KColor38.setter
    def krendering_KColor38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KColor__krendering_KColor38", None)
        self.__krendering_KColor38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KTextUnderline"):
                opp_val = getattr(old_value, "krendering_KTextUnderline", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KTextUnderline", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KTextUnderline"):
                opp_val = getattr(value, "krendering_KTextUnderline", None)
                setattr(value, "krendering_KTextUnderline", self)

    @property
    def krendering_KColor(self):
        return self.__krendering_KColor

    @krendering_KColor.setter
    def krendering_KColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KColor__krendering_KColor", None)
        self.__krendering_KColor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KColoring"):
                opp_val = getattr(old_value, "krendering_KColoring", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KColoring", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KColoring"):
                opp_val = getattr(value, "krendering_KColoring", None)
                setattr(value, "krendering_KColoring", self)

    @property
    def krendering_KColor42(self):
        return self.__krendering_KColor42

    @krendering_KColor42.setter
    def krendering_KColor42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KColor__krendering_KColor42", None)
        self.__krendering_KColor42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KTextStrikeout"):
                opp_val = getattr(old_value, "krendering_KTextStrikeout", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KTextStrikeout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KTextStrikeout"):
                opp_val = getattr(value, "krendering_KTextStrikeout", None)
                setattr(value, "krendering_KTextStrikeout", self)

    @property
    def krendering_KColor28(self):
        return self.__krendering_KColor28

    @krendering_KColor28.setter
    def krendering_KColor28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KColor__krendering_KColor28", None)
        self.__krendering_KColor28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KColoring27"):
                opp_val = getattr(old_value, "krendering_KColoring27", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KColoring27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KColoring27"):
                opp_val = getattr(value, "krendering_KColoring27", None)
                setattr(value, "krendering_KColoring27", self)

    def equals(self, krendering_other) :
        # TODO: Implement equals method
        pass

    def setColor(self, krendering_kColor) :
        # TODO: Implement setColor method
        pass

class KStyle:

    pass
class krendering_KRotation(KStyle):

    def __init__(self, rotation: float, krendering_KRotation: "krendering_KPosition" = None):
        self.rotation = rotation
        self.krendering_KRotation = krendering_KRotation
        
        pass
    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: float):
        self.__rotation = rotation


    @property
    def krendering_KRotation(self):
        return self.__krendering_KRotation

    @krendering_KRotation.setter
    def krendering_KRotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KRotation__krendering_KRotation", None)
        self.__krendering_KRotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KPosition30"):
                opp_val = getattr(old_value, "krendering_KPosition30", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KPosition30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KPosition30"):
                opp_val = getattr(value, "krendering_KPosition30", None)
                setattr(value, "krendering_KPosition30", self)

class krendering_KInvisibility(KStyle):

    def __init__(self, invisible: bool):
        self.invisible = invisible
        
        pass
    @property
    def invisible(self):
        return self.__invisible

    @invisible.setter
    def invisible(self, invisible: bool):
        self.__invisible = invisible


class krendering_KColoring(KStyle):

    def __init__(self, alpha: int, targetAlpha: int, gradientAngle: float, krendering_KColoring: "krendering_KColor" = None, krendering_KColoring27: "krendering_KColor" = None):
        self.alpha = alpha
        self.targetAlpha = targetAlpha
        self.gradientAngle = gradientAngle
        self.krendering_KColoring = krendering_KColoring
        self.krendering_KColoring27 = krendering_KColoring27
        
        pass
    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: int):
        self.__alpha = alpha


    @property
    def gradientAngle(self):
        return self.__gradientAngle

    @gradientAngle.setter
    def gradientAngle(self, gradientAngle: float):
        self.__gradientAngle = gradientAngle


    @property
    def targetAlpha(self):
        return self.__targetAlpha

    @targetAlpha.setter
    def targetAlpha(self, targetAlpha: int):
        self.__targetAlpha = targetAlpha


    @property
    def krendering_KColoring(self):
        return self.__krendering_KColoring

    @krendering_KColoring.setter
    def krendering_KColoring(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KColoring__krendering_KColoring", None)
        self.__krendering_KColoring = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KColor"):
                opp_val = getattr(old_value, "krendering_KColor", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KColor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KColor"):
                opp_val = getattr(value, "krendering_KColor", None)
                setattr(value, "krendering_KColor", self)

    @property
    def krendering_KColoring27(self):
        return self.__krendering_KColoring27

    @krendering_KColoring27.setter
    def krendering_KColoring27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KColoring__krendering_KColoring27", None)
        self.__krendering_KColoring27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KColor28"):
                opp_val = getattr(old_value, "krendering_KColor28", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KColor28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KColor28"):
                opp_val = getattr(value, "krendering_KColor28", None)
                setattr(value, "krendering_KColor28", self)

    def setColorsCopiedFrom(self, krendering_coloring):
        # TODO: Implement setColorsCopiedFrom method
        pass

    def setColorCopyOf(self, krendering_kColor, krendering_alpha):
        # TODO: Implement setColorCopyOf method
        pass

    def setTargetColor(self, krendering_blue, krendering_green, krendering_red):
        # TODO: Implement setTargetColor method
        pass

    def setTargetColorCopyOf(self, krendering_targetColor, krendering_targetAlpha):
        # TODO: Implement setTargetColorCopyOf method
        pass

    def setColorCopiedFrom(self, krendering_coloring):
        # TODO: Implement setColorCopiedFrom method
        pass

    def setColor2(self, krendering_color):
        # TODO: Implement setColor2 method
        pass

    def setTargetColorAndAlphaCopiedFrom(self, krendering_coloring):
        # TODO: Implement setTargetColorAndAlphaCopiedFrom method
        pass

    def setColorsAlphasGradientAngleCopiedFrom(self, krendering_coloring):
        # TODO: Implement setColorsAlphasGradientAngleCopiedFrom method
        pass

    def setColorAndAlphaCopiedFrom(self, krendering_coloring):
        # TODO: Implement setColorAndAlphaCopiedFrom method
        pass

    def setTargetColorCopiedFrom(self, krendering_coloring):
        # TODO: Implement setTargetColorCopiedFrom method
        pass

    def setTargetColor2(self, krendering_targetColor, krendering_targetAlpha):
        # TODO: Implement setTargetColor2 method
        pass

    def setColors(self, krendering_color, krendering_angle, krendering_alpha, krendering_targetAlpha, krendering_targetColor):
        # TODO: Implement setColors method
        pass

    def equals(self, krendering_other) :
        # TODO: Implement equals method
        pass

    def setColorsCopiesOf(self, krendering_alpha, krendering_angle, krendering_targetColor, krendering_color, krendering_targetAlpha):
        # TODO: Implement setColorsCopiesOf method
        pass

    def setColor(self, krendering_alpha, krendering_color):
        # TODO: Implement setColor method
        pass

    def setGradientAngle2(self, krendering_angle):
        # TODO: Implement setGradientAngle2 method
        pass

class krendering_KLineJoin(KStyle):

    def __init__(self, lineJoin: str, miterLimit: float):
        self.lineJoin = lineJoin
        self.miterLimit = miterLimit
        
        pass
    @property
    def lineJoin(self):
        return self.__lineJoin

    @lineJoin.setter
    def lineJoin(self, lineJoin: str):
        self.__lineJoin = lineJoin


    @property
    def miterLimit(self):
        return self.__miterLimit

    @miterLimit.setter
    def miterLimit(self, miterLimit: float):
        self.__miterLimit = miterLimit


class krendering_KLineStyle(KStyle):

    def __init__(self, lineStyle: str, dashPattern: float, dashOffset: float):
        self.lineStyle = lineStyle
        self.dashPattern = dashPattern
        self.dashOffset = dashOffset
        
        pass
    @property
    def dashOffset(self):
        return self.__dashOffset

    @dashOffset.setter
    def dashOffset(self, dashOffset: float):
        self.__dashOffset = dashOffset


    @property
    def dashPattern(self):
        return self.__dashPattern

    @dashPattern.setter
    def dashPattern(self, dashPattern: float):
        self.__dashPattern = dashPattern


    @property
    def lineStyle(self):
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle


class krendering_KTextStrikeout(KStyle):

    def __init__(self, struckOut: str, krendering_KTextStrikeout: "krendering_KColor" = None):
        self.struckOut = struckOut
        self.krendering_KTextStrikeout = krendering_KTextStrikeout
        
        pass
    @property
    def struckOut(self):
        return self.__struckOut

    @struckOut.setter
    def struckOut(self, struckOut: str):
        self.__struckOut = struckOut


    @property
    def krendering_KTextStrikeout(self):
        return self.__krendering_KTextStrikeout

    @krendering_KTextStrikeout.setter
    def krendering_KTextStrikeout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KTextStrikeout__krendering_KTextStrikeout", None)
        self.__krendering_KTextStrikeout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KColor42"):
                opp_val = getattr(old_value, "krendering_KColor42", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KColor42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KColor42"):
                opp_val = getattr(value, "krendering_KColor42", None)
                setattr(value, "krendering_KColor42", self)

class krendering_KShadow(KStyle):

    def __init__(self, xOffset: float, yOffset: float, blur: float, krendering_KShadow: "krendering_KColor" = None):
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.blur = blur
        self.krendering_KShadow = krendering_KShadow
        
        pass
    @property
    def yOffset(self):
        return self.__yOffset

    @yOffset.setter
    def yOffset(self, yOffset: float):
        self.__yOffset = yOffset


    @property
    def xOffset(self):
        return self.__xOffset

    @xOffset.setter
    def xOffset(self, xOffset: float):
        self.__xOffset = xOffset


    @property
    def blur(self):
        return self.__blur

    @blur.setter
    def blur(self, blur: float):
        self.__blur = blur


    @property
    def krendering_KShadow(self):
        return self.__krendering_KShadow

    @krendering_KShadow.setter
    def krendering_KShadow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KShadow__krendering_KShadow", None)
        self.__krendering_KShadow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KColor36"):
                opp_val = getattr(old_value, "krendering_KColor36", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KColor36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KColor36"):
                opp_val = getattr(value, "krendering_KColor36", None)
                setattr(value, "krendering_KColor36", self)

class krendering_KVerticalAlignment(KStyle):

    def __init__(self, verticalAlignment: str):
        self.verticalAlignment = verticalAlignment
        
        pass
    @property
    def verticalAlignment(self):
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment


class krendering_KFontItalic(KStyle):

    def __init__(self, italic: bool):
        self.italic = italic
        
        pass
    @property
    def italic(self):
        return self.__italic

    @italic.setter
    def italic(self, italic: bool):
        self.__italic = italic


class krendering_KFontBold(KStyle):

    def __init__(self, bold: bool):
        self.bold = bold
        
        pass
    @property
    def bold(self):
        return self.__bold

    @bold.setter
    def bold(self, bold: bool):
        self.__bold = bold


class krendering_KHorizontalAlignment(KStyle):

    def __init__(self, horizontalAlignment: str):
        self.horizontalAlignment = horizontalAlignment
        
        pass
    @property
    def horizontalAlignment(self):
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment


class krendering_KFontName(KStyle):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class krendering_KTextUnderline(KStyle):

    def __init__(self, underline: str, krendering_KTextUnderline: "krendering_KColor" = None):
        self.underline = underline
        self.krendering_KTextUnderline = krendering_KTextUnderline
        
        pass
    @property
    def underline(self):
        return self.__underline

    @underline.setter
    def underline(self, underline: str):
        self.__underline = underline


    @property
    def krendering_KTextUnderline(self):
        return self.__krendering_KTextUnderline

    @krendering_KTextUnderline.setter
    def krendering_KTextUnderline(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KTextUnderline__krendering_KTextUnderline", None)
        self.__krendering_KTextUnderline = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KColor38"):
                opp_val = getattr(old_value, "krendering_KColor38", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KColor38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KColor38"):
                opp_val = getattr(value, "krendering_KColor38", None)
                setattr(value, "krendering_KColor38", self)

class krendering_KLineCap(KStyle):

    def __init__(self, lineCap: str):
        self.lineCap = lineCap
        
        pass
    @property
    def lineCap(self):
        return self.__lineCap

    @lineCap.setter
    def lineCap(self, lineCap: str):
        self.__lineCap = lineCap


class krendering_KFontSize(KStyle):

    def __init__(self, size: int, scaleWithZoom: bool):
        self.size = size
        self.scaleWithZoom = scaleWithZoom
        
        pass
    @property
    def scaleWithZoom(self):
        return self.__scaleWithZoom

    @scaleWithZoom.setter
    def scaleWithZoom(self, scaleWithZoom: bool):
        self.__scaleWithZoom = scaleWithZoom


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size


class krendering_KStyleRef(KStyle):

    def __init__(self, referencedTypes: str, krendering_KStyleRef: "krendering_KStyleHolder" = None):
        self.referencedTypes = referencedTypes
        self.krendering_KStyleRef = krendering_KStyleRef
        
        pass
    @property
    def referencedTypes(self):
        return self.__referencedTypes

    @referencedTypes.setter
    def referencedTypes(self, referencedTypes: str):
        self.__referencedTypes = referencedTypes


    @property
    def krendering_KStyleRef(self):
        return self.__krendering_KStyleRef

    @krendering_KStyleRef.setter
    def krendering_KStyleRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KStyleRef__krendering_KStyleRef", None)
        self.__krendering_KStyleRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KStyleHolder40"):
                opp_val = getattr(old_value, "krendering_KStyleHolder40", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KStyleHolder40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KStyleHolder40"):
                opp_val = getattr(value, "krendering_KStyleHolder40", None)
                setattr(value, "krendering_KStyleHolder40", self)

class krendering_KLineWidth(KStyle):

    def __init__(self, lineWidth: float):
        self.lineWidth = lineWidth
        
        pass
    @property
    def lineWidth(self):
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: float):
        self.__lineWidth = lineWidth


class KAreaPlacementData:

    pass
class krendering_KGridPlacementData(KAreaPlacementData):

    def __init__(self, minCellWidth: float, minCellHeight: float, flexibleWidth: str, flexibleHeight: str):
        self.minCellWidth = minCellWidth
        self.minCellHeight = minCellHeight
        self.flexibleWidth = flexibleWidth
        self.flexibleHeight = flexibleHeight
        
        pass
    @property
    def minCellWidth(self):
        return self.__minCellWidth

    @minCellWidth.setter
    def minCellWidth(self, minCellWidth: float):
        self.__minCellWidth = minCellWidth


    @property
    def flexibleWidth(self):
        return self.__flexibleWidth

    @flexibleWidth.setter
    def flexibleWidth(self, flexibleWidth: str):
        self.__flexibleWidth = flexibleWidth


    @property
    def minCellHeight(self):
        return self.__minCellHeight

    @minCellHeight.setter
    def minCellHeight(self, minCellHeight: float):
        self.__minCellHeight = minCellHeight


    @property
    def flexibleHeight(self):
        return self.__flexibleHeight

    @flexibleHeight.setter
    def flexibleHeight(self, flexibleHeight: str):
        self.__flexibleHeight = flexibleHeight


class KPlacement:

    pass
class krendering_KGridPlacement(KPlacement):

    def __init__(self, numColumns: int, krendering_KGridPlacement: "krendering_KPosition" = None, krendering_KGridPlacement18: "krendering_KPosition" = None):
        self.numColumns = numColumns
        self.krendering_KGridPlacement = krendering_KGridPlacement
        self.krendering_KGridPlacement18 = krendering_KGridPlacement18
        
        pass
    @property
    def numColumns(self):
        return self.__numColumns

    @numColumns.setter
    def numColumns(self, numColumns: int):
        self.__numColumns = numColumns


    @property
    def krendering_KGridPlacement18(self):
        return self.__krendering_KGridPlacement18

    @krendering_KGridPlacement18.setter
    def krendering_KGridPlacement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KGridPlacement__krendering_KGridPlacement18", None)
        self.__krendering_KGridPlacement18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KPosition19"):
                opp_val = getattr(old_value, "krendering_KPosition19", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KPosition19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KPosition19"):
                opp_val = getattr(value, "krendering_KPosition19", None)
                setattr(value, "krendering_KPosition19", self)

    @property
    def krendering_KGridPlacement(self):
        return self.__krendering_KGridPlacement

    @krendering_KGridPlacement.setter
    def krendering_KGridPlacement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KGridPlacement__krendering_KGridPlacement", None)
        self.__krendering_KGridPlacement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KPosition16"):
                opp_val = getattr(old_value, "krendering_KPosition16", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KPosition16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KPosition16"):
                opp_val = getattr(value, "krendering_KPosition16", None)
                setattr(value, "krendering_KPosition16", self)

class krendering_KPlacement(ABC):

    pass
class krendering_KStyleHolder:

    def __init__(self, id: str, krendering_KStyleHolder: "krendering_KRenderingLibrary" = None, krendering_KStyleHolder34: set["krendering_KStyle"] = None, krendering_KStyleHolder40: "krendering_KStyleRef" = None):
        self.id = id
        self.krendering_KStyleHolder = krendering_KStyleHolder
        self.krendering_KStyleHolder34 = krendering_KStyleHolder34 if krendering_KStyleHolder34 is not None else set()
        self.krendering_KStyleHolder40 = krendering_KStyleHolder40
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def krendering_KStyleHolder40(self):
        return self.__krendering_KStyleHolder40

    @krendering_KStyleHolder40.setter
    def krendering_KStyleHolder40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KStyleHolder__krendering_KStyleHolder40", None)
        self.__krendering_KStyleHolder40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KStyleRef"):
                opp_val = getattr(old_value, "krendering_KStyleRef", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KStyleRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KStyleRef"):
                opp_val = getattr(value, "krendering_KStyleRef", None)
                setattr(value, "krendering_KStyleRef", self)

    @property
    def krendering_KStyleHolder34(self):
        return self.__krendering_KStyleHolder34

    @krendering_KStyleHolder34.setter
    def krendering_KStyleHolder34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KStyleHolder__krendering_KStyleHolder34", None)
        self.__krendering_KStyleHolder34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "krendering_KStyle"):
                    opp_val = getattr(item, "krendering_KStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "krendering_KStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "krendering_KStyle"):
                    opp_val = getattr(item, "krendering_KStyle", None)
                    
                    setattr(item, "krendering_KStyle", self)
                    

    @property
    def krendering_KStyleHolder(self):
        return self.__krendering_KStyleHolder

    @krendering_KStyleHolder.setter
    def krendering_KStyleHolder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KStyleHolder__krendering_KStyleHolder", None)
        self.__krendering_KStyleHolder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KRenderingLibrary"):
                opp_val = getattr(old_value, "krendering_KRenderingLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KRenderingLibrary"):
                opp_val = getattr(value, "krendering_KRenderingLibrary", None)
                if opp_val is None:
                    setattr(value, "krendering_KRenderingLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EMapPropertyHolder:

    pass
class krendering_KStyle(EMapPropertyHolder):

    def __init__(self, propagateToChildren: bool, modifierId: str, selection: bool, krendering_KStyle: "krendering_KStyleHolder" = None):
        self.propagateToChildren = propagateToChildren
        self.modifierId = modifierId
        self.selection = selection
        self.krendering_KStyle = krendering_KStyle
        
        pass
    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, selection: bool):
        self.__selection = selection


    @property
    def modifierId(self):
        return self.__modifierId

    @modifierId.setter
    def modifierId(self, modifierId: str):
        self.__modifierId = modifierId


    @property
    def propagateToChildren(self):
        return self.__propagateToChildren

    @propagateToChildren.setter
    def propagateToChildren(self, propagateToChildren: bool):
        self.__propagateToChildren = propagateToChildren


    @property
    def krendering_KStyle(self):
        return self.__krendering_KStyle

    @krendering_KStyle.setter
    def krendering_KStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KStyle__krendering_KStyle", None)
        self.__krendering_KStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KStyleHolder34"):
                opp_val = getattr(old_value, "krendering_KStyleHolder34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KStyleHolder34"):
                opp_val = getattr(value, "krendering_KStyleHolder34", None)
                if opp_val is None:
                    setattr(value, "krendering_KStyleHolder34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class KPolyline:

    pass
class krendering_KSpline(KPolyline):

    pass
class krendering_KRoundedBendsPolyline(KPolyline):

    def __init__(self, bendRadius: float):
        self.bendRadius = bendRadius
        
        pass
    @property
    def bendRadius(self):
        return self.__bendRadius

    @bendRadius.setter
    def bendRadius(self, bendRadius: float):
        self.__bendRadius = bendRadius


class krendering_KPolygon(KPolyline):

    pass
class KRendering:

    pass
class krendering_KText(KRendering):

    def __init__(self, text: str, cursorSelectable: bool, editable: bool):
        self.text = text
        self.cursorSelectable = cursorSelectable
        self.editable = editable
        
        pass
    @property
    def cursorSelectable(self):
        return self.__cursorSelectable

    @cursorSelectable.setter
    def cursorSelectable(self, cursorSelectable: bool):
        self.__cursorSelectable = cursorSelectable


    @property
    def editable(self):
        return self.__editable

    @editable.setter
    def editable(self, editable: bool):
        self.__editable = editable


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class krendering_KChildArea(KRendering):

    pass
class krendering_KRenderingRef(KRendering):

    pass
class KPlacementData:

    pass
class krendering_KPointPlacementData(KPlacementData):

    def __init__(self, horizontalAlignment: str, verticalAlignment: str, horizontalMargin: float, verticalMargin: float, minWidth: float, minHeight: float, krendering_KPointPlacementData: "krendering_KPosition" = None):
        self.horizontalAlignment = horizontalAlignment
        self.verticalAlignment = verticalAlignment
        self.horizontalMargin = horizontalMargin
        self.verticalMargin = verticalMargin
        self.minWidth = minWidth
        self.minHeight = minHeight
        self.krendering_KPointPlacementData = krendering_KPointPlacementData
        
        pass
    @property
    def horizontalAlignment(self):
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment


    @property
    def minHeight(self):
        return self.__minHeight

    @minHeight.setter
    def minHeight(self, minHeight: float):
        self.__minHeight = minHeight


    @property
    def verticalAlignment(self):
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment


    @property
    def horizontalMargin(self):
        return self.__horizontalMargin

    @horizontalMargin.setter
    def horizontalMargin(self, horizontalMargin: float):
        self.__horizontalMargin = horizontalMargin


    @property
    def verticalMargin(self):
        return self.__verticalMargin

    @verticalMargin.setter
    def verticalMargin(self, verticalMargin: float):
        self.__verticalMargin = verticalMargin


    @property
    def minWidth(self):
        return self.__minWidth

    @minWidth.setter
    def minWidth(self, minWidth: float):
        self.__minWidth = minWidth


    @property
    def krendering_KPointPlacementData(self):
        return self.__krendering_KPointPlacementData

    @krendering_KPointPlacementData.setter
    def krendering_KPointPlacementData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KPointPlacementData__krendering_KPointPlacementData", None)
        self.__krendering_KPointPlacementData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KPosition32"):
                opp_val = getattr(old_value, "krendering_KPosition32", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KPosition32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KPosition32"):
                opp_val = getattr(value, "krendering_KPosition32", None)
                setattr(value, "krendering_KPosition32", self)

class krendering_KAreaPlacementData(KPlacementData):

    pass
class krendering_KDecoratorPlacementData(KPlacementData):

    def __init__(self, absolute: float, xOffset: float, yOffset: float, rotateWithLine: bool, width: float, height: float, relative: float):
        self.absolute = absolute
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.rotateWithLine = rotateWithLine
        self.width = width
        self.height = height
        self.relative = relative
        
        pass
    @property
    def absolute(self):
        return self.__absolute

    @absolute.setter
    def absolute(self, absolute: float):
        self.__absolute = absolute


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width


    @property
    def xOffset(self):
        return self.__xOffset

    @xOffset.setter
    def xOffset(self, xOffset: float):
        self.__xOffset = xOffset


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height


    @property
    def yOffset(self):
        return self.__yOffset

    @yOffset.setter
    def yOffset(self, yOffset: float):
        self.__yOffset = yOffset


    @property
    def relative(self):
        return self.__relative

    @relative.setter
    def relative(self, relative: float):
        self.__relative = relative


    @property
    def rotateWithLine(self):
        return self.__rotateWithLine

    @rotateWithLine.setter
    def rotateWithLine(self, rotateWithLine: bool):
        self.__rotateWithLine = rotateWithLine


class krendering_KContainerRendering(KRendering):

    pass
class KStyleHolder:

    pass
class KGraphData:

    pass
class krendering_KRenderingLibrary(KGraphData):

    pass
class krendering_KRendering(KStyleHolder, KGraphData):

    pass
class KContainerRendering:

    pass
class krendering_KRoundedRectangle(KContainerRendering):

    def __init__(self, cornerWidth: float, cornerHeight: float):
        self.cornerWidth = cornerWidth
        self.cornerHeight = cornerHeight
        
        pass
    @property
    def cornerWidth(self):
        return self.__cornerWidth

    @cornerWidth.setter
    def cornerWidth(self, cornerWidth: float):
        self.__cornerWidth = cornerWidth


    @property
    def cornerHeight(self):
        return self.__cornerHeight

    @cornerHeight.setter
    def cornerHeight(self, cornerHeight: float):
        self.__cornerHeight = cornerHeight


class krendering_KCustomRendering(KContainerRendering):

    def __init__(self, className: str, bundleName: str, figureObject: str):
        self.className = className
        self.bundleName = bundleName
        self.figureObject = figureObject
        
        pass
    @property
    def className(self):
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className


    @property
    def bundleName(self):
        return self.__bundleName

    @bundleName.setter
    def bundleName(self, bundleName: str):
        self.__bundleName = bundleName


    @property
    def figureObject(self):
        return self.__figureObject

    @figureObject.setter
    def figureObject(self, figureObject: str):
        self.__figureObject = figureObject


class krendering_KPolyline(KContainerRendering):

    pass
class krendering_KImage(KContainerRendering):

    def __init__(self, bundleName: str, imagePath: str, imageObject: str, krendering_KImage: "krendering_KRendering" = None):
        self.bundleName = bundleName
        self.imagePath = imagePath
        self.imageObject = imageObject
        self.krendering_KImage = krendering_KImage
        
        pass
    @property
    def imagePath(self):
        return self.__imagePath

    @imagePath.setter
    def imagePath(self, imagePath: str):
        self.__imagePath = imagePath


    @property
    def bundleName(self):
        return self.__bundleName

    @bundleName.setter
    def bundleName(self, bundleName: str):
        self.__bundleName = bundleName


    @property
    def imageObject(self):
        return self.__imageObject

    @imageObject.setter
    def imageObject(self, imageObject: str):
        self.__imageObject = imageObject


    @property
    def krendering_KImage(self):
        return self.__krendering_KImage

    @krendering_KImage.setter
    def krendering_KImage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KImage__krendering_KImage", None)
        self.__krendering_KImage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KRendering9"):
                opp_val = getattr(old_value, "krendering_KRendering9", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KRendering9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KRendering9"):
                opp_val = getattr(value, "krendering_KRendering9", None)
                setattr(value, "krendering_KRendering9", self)

class krendering_KArc(KContainerRendering):

    def __init__(self, startAngle: float, arcAngle: float, arcType: str):
        self.startAngle = startAngle
        self.arcAngle = arcAngle
        self.arcType = arcType
        
        pass
    @property
    def arcType(self):
        return self.__arcType

    @arcType.setter
    def arcType(self, arcType: str):
        self.__arcType = arcType


    @property
    def arcAngle(self):
        return self.__arcAngle

    @arcAngle.setter
    def arcAngle(self, arcAngle: float):
        self.__arcAngle = arcAngle


    @property
    def startAngle(self):
        return self.__startAngle

    @startAngle.setter
    def startAngle(self, startAngle: float):
        self.__startAngle = startAngle


class krendering_KRectangle(KContainerRendering):

    pass
class krendering_KEllipse(KContainerRendering):

    pass
class krendering_KAction:

    def __init__(self, actionId: str, trigger: str, altPressed: bool, ctrlCmdPressed: bool, shiftPressed: bool, krendering_KAction: "krendering_KRendering" = None):
        self.actionId = actionId
        self.trigger = trigger
        self.altPressed = altPressed
        self.ctrlCmdPressed = ctrlCmdPressed
        self.shiftPressed = shiftPressed
        self.krendering_KAction = krendering_KAction
        
        pass
    @property
    def trigger(self):
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger


    @property
    def shiftPressed(self):
        return self.__shiftPressed

    @shiftPressed.setter
    def shiftPressed(self, shiftPressed: bool):
        self.__shiftPressed = shiftPressed


    @property
    def altPressed(self):
        return self.__altPressed

    @altPressed.setter
    def altPressed(self, altPressed: bool):
        self.__altPressed = altPressed


    @property
    def ctrlCmdPressed(self):
        return self.__ctrlCmdPressed

    @ctrlCmdPressed.setter
    def ctrlCmdPressed(self, ctrlCmdPressed: bool):
        self.__ctrlCmdPressed = ctrlCmdPressed


    @property
    def actionId(self):
        return self.__actionId

    @actionId.setter
    def actionId(self, actionId: str):
        self.__actionId = actionId


    @property
    def krendering_KAction(self):
        return self.__krendering_KAction

    @krendering_KAction.setter
    def krendering_KAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KAction__krendering_KAction", None)
        self.__krendering_KAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KRendering3"):
                opp_val = getattr(old_value, "krendering_KRendering3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KRendering3"):
                opp_val = getattr(value, "krendering_KRendering3", None)
                if opp_val is None:
                    setattr(value, "krendering_KRendering3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class krendering_KPlacementData(ABC):

    pass
class krendering_KPosition:

    def __init__(self, krendering_KPosition: "krendering_KPolyline" = None, krendering_KPosition16: "krendering_KGridPlacement" = None, krendering_KPosition19: "krendering_KGridPlacement" = None, krendering_KPosition21: "krendering_KAreaPlacementData" = None, krendering_KPosition24: "krendering_KAreaPlacementData" = None, krendering_KPosition30: "krendering_KRotation" = None, krendering_KPosition32: "krendering_KPointPlacementData" = None):
        self.krendering_KPosition = krendering_KPosition
        self.krendering_KPosition16 = krendering_KPosition16
        self.krendering_KPosition19 = krendering_KPosition19
        self.krendering_KPosition21 = krendering_KPosition21
        self.krendering_KPosition24 = krendering_KPosition24
        self.krendering_KPosition30 = krendering_KPosition30
        self.krendering_KPosition32 = krendering_KPosition32
        
        pass
    @property
    def krendering_KPosition30(self):
        return self.__krendering_KPosition30

    @krendering_KPosition30.setter
    def krendering_KPosition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KPosition__krendering_KPosition30", None)
        self.__krendering_KPosition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KRotation"):
                opp_val = getattr(old_value, "krendering_KRotation", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KRotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KRotation"):
                opp_val = getattr(value, "krendering_KRotation", None)
                setattr(value, "krendering_KRotation", self)

    @property
    def krendering_KPosition(self):
        return self.__krendering_KPosition

    @krendering_KPosition.setter
    def krendering_KPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KPosition__krendering_KPosition", None)
        self.__krendering_KPosition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KPolyline"):
                opp_val = getattr(old_value, "krendering_KPolyline", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KPolyline"):
                opp_val = getattr(value, "krendering_KPolyline", None)
                if opp_val is None:
                    setattr(value, "krendering_KPolyline", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def krendering_KPosition32(self):
        return self.__krendering_KPosition32

    @krendering_KPosition32.setter
    def krendering_KPosition32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KPosition__krendering_KPosition32", None)
        self.__krendering_KPosition32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KPointPlacementData"):
                opp_val = getattr(old_value, "krendering_KPointPlacementData", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KPointPlacementData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KPointPlacementData"):
                opp_val = getattr(value, "krendering_KPointPlacementData", None)
                setattr(value, "krendering_KPointPlacementData", self)

    @property
    def krendering_KPosition24(self):
        return self.__krendering_KPosition24

    @krendering_KPosition24.setter
    def krendering_KPosition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KPosition__krendering_KPosition24", None)
        self.__krendering_KPosition24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KAreaPlacementData23"):
                opp_val = getattr(old_value, "krendering_KAreaPlacementData23", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KAreaPlacementData23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KAreaPlacementData23"):
                opp_val = getattr(value, "krendering_KAreaPlacementData23", None)
                setattr(value, "krendering_KAreaPlacementData23", self)

    @property
    def krendering_KPosition21(self):
        return self.__krendering_KPosition21

    @krendering_KPosition21.setter
    def krendering_KPosition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KPosition__krendering_KPosition21", None)
        self.__krendering_KPosition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KAreaPlacementData"):
                opp_val = getattr(old_value, "krendering_KAreaPlacementData", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KAreaPlacementData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KAreaPlacementData"):
                opp_val = getattr(value, "krendering_KAreaPlacementData", None)
                setattr(value, "krendering_KAreaPlacementData", self)

    @property
    def krendering_KPosition19(self):
        return self.__krendering_KPosition19

    @krendering_KPosition19.setter
    def krendering_KPosition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KPosition__krendering_KPosition19", None)
        self.__krendering_KPosition19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KGridPlacement18"):
                opp_val = getattr(old_value, "krendering_KGridPlacement18", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KGridPlacement18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KGridPlacement18"):
                opp_val = getattr(value, "krendering_KGridPlacement18", None)
                setattr(value, "krendering_KGridPlacement18", self)

    @property
    def krendering_KPosition16(self):
        return self.__krendering_KPosition16

    @krendering_KPosition16.setter
    def krendering_KPosition16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_krendering_KPosition__krendering_KPosition16", None)
        self.__krendering_KPosition16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "krendering_KGridPlacement"):
                opp_val = getattr(old_value, "krendering_KGridPlacement", None)
                if opp_val == self:
                    setattr(old_value, "krendering_KGridPlacement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "krendering_KGridPlacement"):
                opp_val = getattr(value, "krendering_KGridPlacement", None)
                setattr(value, "krendering_KGridPlacement", self)

    def equals(self, krendering_other) :
        # TODO: Implement equals method
        pass

    def setPositions(self, krendering_x, krendering_y) :
        # TODO: Implement setPositions method
        pass
