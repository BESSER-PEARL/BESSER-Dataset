from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MaskType(Enum):
    CLIP = "CLIP"
    ALPHA = "ALPHA"
class TextRotation(Enum):
    auto = "auto"
    rotate0 = "rotate0"
    rotate90 = "rotate90"
    rotate180 = "rotate180"
    rotate270 = "rotate270"
class TextDecoration(Enum):
    NONE = "NONE"
    UNDERLINE = "UNDERLINE"
class AlignmentBaseline(Enum):
    auto = "auto"
    roman = "roman"
    ascent = "ascent"
    descent = "descent"
    ideographicTop = "ideographicTop"
    ideographicCenter = "ideographicCenter"
    ideographicBottom = "ideographicBottom"
    useDominantBaseline = "useDominantBaseline"
class DigitWidth(Enum):
    default = "default"
    proportional = "proportional"
    tabular = "tabular"
class DigitCase(Enum):
    default = "default"
    lining = "lining"
    oldStyle = "oldStyle"
class SpreadMethod(Enum):
    NOT_SET = "NOT_SET"
    pad = "pad"
    reflect = "reflect"
    repeat = "repeat"
class FontStyle(Enum):
    NORMAL = "NORMAL"
    ITALIC = "ITALIC"
class JustificationRule(Enum):
    auto = "auto"
    space = "space"
    eastAsian = "eastAsian"
class FillMode(Enum):
    SCALE = "SCALE"
    CLIP = "CLIP"
    REPEAT = "REPEAT"
class VerticalAlign(Enum):
    top = "top"
    middle = "middle"
    bottom = "bottom"
    justify = "justify"
    inherit = "inherit"
class TextJustify(Enum):
    interWord = "interWord"
    distribute = "distribute"
class InterpolationMethod(Enum):
    NOT_SET = "NOT_SET"
    rgb = "rgb"
    linearRGB = "linearRGB"
class TextAlign(Enum):
    start = "start"
    end = "end"
    left = "left"
    center = "center"
    right = "right"
    justify = "justify"
class LigatureLevel(Enum):
    minimum = "minimum"
    common = "common"
    uncommon = "uncommon"
    exotic = "exotic"
class LeadingModel(Enum):
    auto = "auto"
    romanUp = "romanUp"
    ideographicTopUp = "ideographicTopUp"
    ideographicCenterUp = "ideographicCenterUp"
    ascentDescentUp = "ascentDescentUp"
    ideographicTopDown = "ideographicTopDown"
    ideographicCenterDown = "ideographicCenterDown"
class ScaleMode(Enum):
    NORMAL = "NORMAL"
    NONE = "NONE"
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
class LineBreak(Enum):
    toFit = "toFit"
    explicit = "explicit"
class TypographicCase(Enum):
    default = "default"
    capsToSmallCaps = "capsToSmallCaps"
    uppercase = "uppercase"
    lowercase = "lowercase"
    lowercaseToSmallCaps = "lowercaseToSmallCaps"
class FontWeight(Enum):
    BOLD = "BOLD"
    NORMAL = "NORMAL"
class BevelFilterType(Enum):
    INNER = "INNER"
    OUTER = "OUTER"
    FULL = "FULL"
class Winding(Enum):
    NOT_SET = "NOT_SET"
    evenOdd = "evenOdd"
    nonZero = "nonZero"
class JustificationStyle(Enum):
    auto = "auto"
    prioritizeLeastAdjustment = "prioritizeLeastAdjustment"
    pushInKinsoku = "pushInKinsoku"
    pushOutOnly = "pushOutOnly"
class BlockProgression(Enum):
    tb = "tb"
    rl = "rl"
class Joint(Enum):
    ROUND = "ROUND"
    MITER = "MITER"
    BEVEL = "BEVEL"
class Cap(Enum):
    ROUND = "ROUND"
    SQUARE = "SQUARE"
    NONE = "NONE"
class DominantBaseline(Enum):
    auto = "auto"
    roman = "roman"
    ascent = "ascent"
    descent = "descent"
    ideographicTop = "ideographicTop"
    ideographicCenter = "ideographicCenter"
    ideographicBottom = "ideographicBottom"
class BlendMode(Enum):
    NOT_SET = "NOT_SET"
    add = "add"
    alpha = "alpha"
    darken = "darken"
    difference = "difference"
    erase = "erase"
    hardlight = "hardlight"
    invert = "invert"
    layer = "layer"
    lighten = "lighten"
    multiply = "multiply"
    normal = "normal"
    overlay = "overlay"
    screen = "screen"
    shader = "shader"
    subtract = "subtract"
class BreakOpportunity(Enum):
    auto = "auto"
    any = "any"
    none = "none"
    all = "all"
class Kerning(Enum):
    OFF = "OFF"
    AUTO = "AUTO"
    ON = "ON"
class WhitespaceCollapse(Enum):
    PRESERVE = "PRESERVE"
    COLLAPSE = "COLLAPSE"


############################################
# Definition of Classes
############################################

class fxg_FXGElement(ABC):

    pass
class fxg_GradientBevelFilter:

    def __init__(self, angle: str, blurX: str, blurY: str, distance: str, knockout: str, quality: str, strength: str, type: str):
        self.angle = angle
        self.blurX = blurX
        self.blurY = blurY
        self.distance = distance
        self.knockout = knockout
        self.quality = quality
        self.strength = strength
        self.type = type
        
        pass
    @property
    def knockout(self):
        return self.__knockout

    @knockout.setter
    def knockout(self, knockout: str):
        self.__knockout = knockout


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance


    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength: str):
        self.__strength = strength


    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle


    @property
    def blurX(self):
        return self.__blurX

    @blurX.setter
    def blurX(self, blurX: str):
        self.__blurX = blurX


    @property
    def blurY(self):
        return self.__blurY

    @blurY.setter
    def blurY(self, blurY: str):
        self.__blurY = blurY


    @property
    def quality(self):
        return self.__quality

    @quality.setter
    def quality(self, quality: str):
        self.__quality = quality


class fxg_GradientGlowFilter:

    def __init__(self, angle: str, blurX: str, blurY: str, distance: str, inner: str, knockout: str, quality: str, strength: str):
        self.angle = angle
        self.blurX = blurX
        self.blurY = blurY
        self.distance = distance
        self.inner = inner
        self.knockout = knockout
        self.quality = quality
        self.strength = strength
        
        pass
    @property
    def quality(self):
        return self.__quality

    @quality.setter
    def quality(self, quality: str):
        self.__quality = quality


    @property
    def blurX(self):
        return self.__blurX

    @blurX.setter
    def blurX(self, blurX: str):
        self.__blurX = blurX


    @property
    def inner(self):
        return self.__inner

    @inner.setter
    def inner(self, inner: str):
        self.__inner = inner


    @property
    def knockout(self):
        return self.__knockout

    @knockout.setter
    def knockout(self, knockout: str):
        self.__knockout = knockout


    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle


    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance


    @property
    def blurY(self):
        return self.__blurY

    @blurY.setter
    def blurY(self, blurY: str):
        self.__blurY = blurY


    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength: str):
        self.__strength = strength


class Filter:

    pass
class fxg_BevelFilter(Filter):

    def __init__(self, angle: str, blurX: str, blurY: str, highlightAlpha: str, highlightColor: str, distance: str, knockout: str, quality: str, shadowAlpha: str, shadowColor: str, strength: str, type: str):
        self.angle = angle
        self.blurX = blurX
        self.blurY = blurY
        self.highlightAlpha = highlightAlpha
        self.highlightColor = highlightColor
        self.distance = distance
        self.knockout = knockout
        self.quality = quality
        self.shadowAlpha = shadowAlpha
        self.shadowColor = shadowColor
        self.strength = strength
        self.type = type
        
        pass
    @property
    def blurY(self):
        return self.__blurY

    @blurY.setter
    def blurY(self, blurY: str):
        self.__blurY = blurY


    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength: str):
        self.__strength = strength


    @property
    def knockout(self):
        return self.__knockout

    @knockout.setter
    def knockout(self, knockout: str):
        self.__knockout = knockout


    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance


    @property
    def highlightAlpha(self):
        return self.__highlightAlpha

    @highlightAlpha.setter
    def highlightAlpha(self, highlightAlpha: str):
        self.__highlightAlpha = highlightAlpha


    @property
    def highlightColor(self):
        return self.__highlightColor

    @highlightColor.setter
    def highlightColor(self, highlightColor: str):
        self.__highlightColor = highlightColor


    @property
    def blurX(self):
        return self.__blurX

    @blurX.setter
    def blurX(self, blurX: str):
        self.__blurX = blurX


    @property
    def shadowColor(self):
        return self.__shadowColor

    @shadowColor.setter
    def shadowColor(self, shadowColor: str):
        self.__shadowColor = shadowColor


    @property
    def quality(self):
        return self.__quality

    @quality.setter
    def quality(self, quality: str):
        self.__quality = quality


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle


    @property
    def shadowAlpha(self):
        return self.__shadowAlpha

    @shadowAlpha.setter
    def shadowAlpha(self, shadowAlpha: str):
        self.__shadowAlpha = shadowAlpha


class fxg_ColorMatrixFilter(Filter):

    def __init__(self, matrix: str):
        self.matrix = matrix
        
        pass
    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, matrix: str):
        self.__matrix = matrix


class fxg_DropShadowFilter(Filter):

    def __init__(self, alpha: str, angle: str, blurX: str, blurY: str, color: str, distance: str, inner: str, hideObject: str, knockout: str, quality: str, strength: str):
        self.alpha = alpha
        self.angle = angle
        self.blurX = blurX
        self.blurY = blurY
        self.color = color
        self.distance = distance
        self.inner = inner
        self.hideObject = hideObject
        self.knockout = knockout
        self.quality = quality
        self.strength = strength
        
        pass
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle


    @property
    def knockout(self):
        return self.__knockout

    @knockout.setter
    def knockout(self, knockout: str):
        self.__knockout = knockout


    @property
    def quality(self):
        return self.__quality

    @quality.setter
    def quality(self, quality: str):
        self.__quality = quality


    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength: str):
        self.__strength = strength


    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha


    @property
    def blurX(self):
        return self.__blurX

    @blurX.setter
    def blurX(self, blurX: str):
        self.__blurX = blurX


    @property
    def hideObject(self):
        return self.__hideObject

    @hideObject.setter
    def hideObject(self, hideObject: str):
        self.__hideObject = hideObject


    @property
    def inner(self):
        return self.__inner

    @inner.setter
    def inner(self, inner: str):
        self.__inner = inner


    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance


    @property
    def blurY(self):
        return self.__blurY

    @blurY.setter
    def blurY(self, blurY: str):
        self.__blurY = blurY


class fxg_BlurFilter(Filter):

    def __init__(self, blurX: str, blurY: str, quality: str):
        self.blurX = blurX
        self.blurY = blurY
        self.quality = quality
        
        pass
    @property
    def quality(self):
        return self.__quality

    @quality.setter
    def quality(self, quality: str):
        self.__quality = quality


    @property
    def blurY(self):
        return self.__blurY

    @blurY.setter
    def blurY(self, blurY: str):
        self.__blurY = blurY


    @property
    def blurX(self):
        return self.__blurX

    @blurX.setter
    def blurX(self, blurX: str):
        self.__blurX = blurX


class fxg_LinearGradientStroke:

    def __init__(self, x: str, y: str, scaleX: str, rotation: str, spreadMethod: str, interpolationMethod: str, scaleMode: str, caps: str, joints: str, miterLimit: str, weight: str, pixelHinting: str, fxg_LinearGradientStroke: "fxg_Matrix" = None):
        self.x = x
        self.y = y
        self.scaleX = scaleX
        self.rotation = rotation
        self.spreadMethod = spreadMethod
        self.interpolationMethod = interpolationMethod
        self.scaleMode = scaleMode
        self.caps = caps
        self.joints = joints
        self.miterLimit = miterLimit
        self.weight = weight
        self.pixelHinting = pixelHinting
        self.fxg_LinearGradientStroke = fxg_LinearGradientStroke
        
        pass
    @property
    def interpolationMethod(self):
        return self.__interpolationMethod

    @interpolationMethod.setter
    def interpolationMethod(self, interpolationMethod: str):
        self.__interpolationMethod = interpolationMethod


    @property
    def miterLimit(self):
        return self.__miterLimit

    @miterLimit.setter
    def miterLimit(self, miterLimit: str):
        self.__miterLimit = miterLimit


    @property
    def scaleMode(self):
        return self.__scaleMode

    @scaleMode.setter
    def scaleMode(self, scaleMode: str):
        self.__scaleMode = scaleMode


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def spreadMethod(self):
        return self.__spreadMethod

    @spreadMethod.setter
    def spreadMethod(self, spreadMethod: str):
        self.__spreadMethod = spreadMethod


    @property
    def joints(self):
        return self.__joints

    @joints.setter
    def joints(self, joints: str):
        self.__joints = joints


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def pixelHinting(self):
        return self.__pixelHinting

    @pixelHinting.setter
    def pixelHinting(self, pixelHinting: str):
        self.__pixelHinting = pixelHinting


    @property
    def caps(self):
        return self.__caps

    @caps.setter
    def caps(self, caps: str):
        self.__caps = caps


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def fxg_LinearGradientStroke(self):
        return self.__fxg_LinearGradientStroke

    @fxg_LinearGradientStroke.setter
    def fxg_LinearGradientStroke(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_LinearGradientStroke__fxg_LinearGradientStroke", None)
        self.__fxg_LinearGradientStroke = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Matrix84"):
                opp_val = getattr(old_value, "fxg_Matrix84", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Matrix84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Matrix84"):
                opp_val = getattr(value, "fxg_Matrix84", None)
                setattr(value, "fxg_Matrix84", self)

class Stroke:

    pass
class fxg_SolidColorStroke(Stroke):

    def __init__(self, alpha: str, caps: str, color: str, joints: str, miterLimit: str, pixelHinting: str, scaleMode: str, weight: str):
        self.alpha = alpha
        self.caps = caps
        self.color = color
        self.joints = joints
        self.miterLimit = miterLimit
        self.pixelHinting = pixelHinting
        self.scaleMode = scaleMode
        self.weight = weight
        
        pass
    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def pixelHinting(self):
        return self.__pixelHinting

    @pixelHinting.setter
    def pixelHinting(self, pixelHinting: str):
        self.__pixelHinting = pixelHinting


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def scaleMode(self):
        return self.__scaleMode

    @scaleMode.setter
    def scaleMode(self, scaleMode: str):
        self.__scaleMode = scaleMode


    @property
    def joints(self):
        return self.__joints

    @joints.setter
    def joints(self, joints: str):
        self.__joints = joints


    @property
    def miterLimit(self):
        return self.__miterLimit

    @miterLimit.setter
    def miterLimit(self, miterLimit: str):
        self.__miterLimit = miterLimit


    @property
    def caps(self):
        return self.__caps

    @caps.setter
    def caps(self, caps: str):
        self.__caps = caps


class fxg_RadialGradientStroke:

    def __init__(self, x: str, y: str, scaleX: str, scaleY: str, rotation: str, spreadMethod: str, interpolationMethod: str, focalPointRatio: str, scaleMode: str, caps: str, joints: str, miterLimit: str, weight: str, pixelHinting: str, fxg_RadialGradientStroke: "fxg_Matrix" = None):
        self.x = x
        self.y = y
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.rotation = rotation
        self.spreadMethod = spreadMethod
        self.interpolationMethod = interpolationMethod
        self.focalPointRatio = focalPointRatio
        self.scaleMode = scaleMode
        self.caps = caps
        self.joints = joints
        self.miterLimit = miterLimit
        self.weight = weight
        self.pixelHinting = pixelHinting
        self.fxg_RadialGradientStroke = fxg_RadialGradientStroke
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def scaleY(self):
        return self.__scaleY

    @scaleY.setter
    def scaleY(self, scaleY: str):
        self.__scaleY = scaleY


    @property
    def pixelHinting(self):
        return self.__pixelHinting

    @pixelHinting.setter
    def pixelHinting(self, pixelHinting: str):
        self.__pixelHinting = pixelHinting


    @property
    def scaleMode(self):
        return self.__scaleMode

    @scaleMode.setter
    def scaleMode(self, scaleMode: str):
        self.__scaleMode = scaleMode


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def caps(self):
        return self.__caps

    @caps.setter
    def caps(self, caps: str):
        self.__caps = caps


    @property
    def interpolationMethod(self):
        return self.__interpolationMethod

    @interpolationMethod.setter
    def interpolationMethod(self, interpolationMethod: str):
        self.__interpolationMethod = interpolationMethod


    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def miterLimit(self):
        return self.__miterLimit

    @miterLimit.setter
    def miterLimit(self, miterLimit: str):
        self.__miterLimit = miterLimit


    @property
    def joints(self):
        return self.__joints

    @joints.setter
    def joints(self, joints: str):
        self.__joints = joints


    @property
    def focalPointRatio(self):
        return self.__focalPointRatio

    @focalPointRatio.setter
    def focalPointRatio(self, focalPointRatio: str):
        self.__focalPointRatio = focalPointRatio


    @property
    def spreadMethod(self):
        return self.__spreadMethod

    @spreadMethod.setter
    def spreadMethod(self, spreadMethod: str):
        self.__spreadMethod = spreadMethod


    @property
    def fxg_RadialGradientStroke(self):
        return self.__fxg_RadialGradientStroke

    @fxg_RadialGradientStroke.setter
    def fxg_RadialGradientStroke(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_RadialGradientStroke__fxg_RadialGradientStroke", None)
        self.__fxg_RadialGradientStroke = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Matrix86"):
                opp_val = getattr(old_value, "fxg_Matrix86", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Matrix86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Matrix86"):
                opp_val = getattr(value, "fxg_Matrix86", None)
                setattr(value, "fxg_Matrix86", self)

class fxg_RadialGradient:

    def __init__(self, spreadMethod: str, interpolationMethod: str, focalPointRatio: str, x: str, y: str, scaleX: str, scaleY: str, rotation: str, fxg_RadialGradient: "fxg_Matrix" = None):
        self.spreadMethod = spreadMethod
        self.interpolationMethod = interpolationMethod
        self.focalPointRatio = focalPointRatio
        self.x = x
        self.y = y
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.rotation = rotation
        self.fxg_RadialGradient = fxg_RadialGradient
        
        pass
    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def scaleY(self):
        return self.__scaleY

    @scaleY.setter
    def scaleY(self, scaleY: str):
        self.__scaleY = scaleY


    @property
    def spreadMethod(self):
        return self.__spreadMethod

    @spreadMethod.setter
    def spreadMethod(self, spreadMethod: str):
        self.__spreadMethod = spreadMethod


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def interpolationMethod(self):
        return self.__interpolationMethod

    @interpolationMethod.setter
    def interpolationMethod(self, interpolationMethod: str):
        self.__interpolationMethod = interpolationMethod


    @property
    def focalPointRatio(self):
        return self.__focalPointRatio

    @focalPointRatio.setter
    def focalPointRatio(self, focalPointRatio: str):
        self.__focalPointRatio = focalPointRatio


    @property
    def fxg_RadialGradient(self):
        return self.__fxg_RadialGradient

    @fxg_RadialGradient.setter
    def fxg_RadialGradient(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_RadialGradient__fxg_RadialGradient", None)
        self.__fxg_RadialGradient = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Matrix80"):
                opp_val = getattr(old_value, "fxg_Matrix80", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Matrix80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Matrix80"):
                opp_val = getattr(value, "fxg_Matrix80", None)
                setattr(value, "fxg_Matrix80", self)

class fxg_LinearGradient:

    def __init__(self, x: str, y: str, scaleX: str, rotation: str, spreadMethod: str, interpolationMethod: str, fxg_LinearGradient: "fxg_Matrix" = None):
        self.x = x
        self.y = y
        self.scaleX = scaleX
        self.rotation = rotation
        self.spreadMethod = spreadMethod
        self.interpolationMethod = interpolationMethod
        self.fxg_LinearGradient = fxg_LinearGradient
        
        pass
    @property
    def interpolationMethod(self):
        return self.__interpolationMethod

    @interpolationMethod.setter
    def interpolationMethod(self, interpolationMethod: str):
        self.__interpolationMethod = interpolationMethod


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def spreadMethod(self):
        return self.__spreadMethod

    @spreadMethod.setter
    def spreadMethod(self, spreadMethod: str):
        self.__spreadMethod = spreadMethod


    @property
    def fxg_LinearGradient(self):
        return self.__fxg_LinearGradient

    @fxg_LinearGradient.setter
    def fxg_LinearGradient(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_LinearGradient__fxg_LinearGradient", None)
        self.__fxg_LinearGradient = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Matrix78"):
                opp_val = getattr(old_value, "fxg_Matrix78", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Matrix78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Matrix78"):
                opp_val = getattr(value, "fxg_Matrix78", None)
                setattr(value, "fxg_Matrix78", self)

class Fill:

    pass
class fxg_SolidColor(Fill):

    def __init__(self, alpha: str, color: str):
        self.alpha = alpha
        self.color = color
        
        pass
    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


class fxg_linkActiveFormat:

    pass
class RichTextContentContainer:

    pass
class fxg_BitmapFill(Fill):

    def __init__(self, x: str, y: str, scaleX: str, scaleY: str, rotation: str, source: str, fillMode: str, fxg_BitmapFill: "fxg_Matrix" = None):
        self.x = x
        self.y = y
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.rotation = rotation
        self.source = source
        self.fillMode = fillMode
        self.fxg_BitmapFill = fxg_BitmapFill
        
        pass
    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def fillMode(self):
        return self.__fillMode

    @fillMode.setter
    def fillMode(self, fillMode: str):
        self.__fillMode = fillMode


    @property
    def scaleY(self):
        return self.__scaleY

    @scaleY.setter
    def scaleY(self, scaleY: str):
        self.__scaleY = scaleY


    @property
    def fxg_BitmapFill(self):
        return self.__fxg_BitmapFill

    @fxg_BitmapFill.setter
    def fxg_BitmapFill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_BitmapFill__fxg_BitmapFill", None)
        self.__fxg_BitmapFill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Matrix82"):
                opp_val = getattr(old_value, "fxg_Matrix82", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Matrix82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Matrix82"):
                opp_val = getattr(value, "fxg_Matrix82", None)
                setattr(value, "fxg_Matrix82", self)

class fxg_CharacterAttributes(ABC):

    def __init__(self, alignmentBaseline: str, ligatureLevel: str, locale: str, typographicCase: str, textRotation: str, trackingLeft: str, trackingRight: str, fontFamily: str, fontSize: str, fontStyle: str, fontWeight: str, lineHeight: str, textDecoration: str, lineThrough: str, color: str, textAlpha: str, whiteSpaceCollapse: str, kerning: str, backgroundAlpha: str, backgroundColor: str, baselineShift: str, breakOpportunity: str, digitCase: str, digitWidth: str, dominantBaseline: str):
        self.alignmentBaseline = alignmentBaseline
        self.ligatureLevel = ligatureLevel
        self.locale = locale
        self.typographicCase = typographicCase
        self.textRotation = textRotation
        self.trackingLeft = trackingLeft
        self.trackingRight = trackingRight
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.fontStyle = fontStyle
        self.fontWeight = fontWeight
        self.lineHeight = lineHeight
        self.textDecoration = textDecoration
        self.lineThrough = lineThrough
        self.color = color
        self.textAlpha = textAlpha
        self.whiteSpaceCollapse = whiteSpaceCollapse
        self.kerning = kerning
        self.backgroundAlpha = backgroundAlpha
        self.backgroundColor = backgroundColor
        self.baselineShift = baselineShift
        self.breakOpportunity = breakOpportunity
        self.digitCase = digitCase
        self.digitWidth = digitWidth
        self.dominantBaseline = dominantBaseline
        
        pass
    @property
    def fontStyle(self):
        return self.__fontStyle

    @fontStyle.setter
    def fontStyle(self, fontStyle: str):
        self.__fontStyle = fontStyle


    @property
    def lineThrough(self):
        return self.__lineThrough

    @lineThrough.setter
    def lineThrough(self, lineThrough: str):
        self.__lineThrough = lineThrough


    @property
    def textRotation(self):
        return self.__textRotation

    @textRotation.setter
    def textRotation(self, textRotation: str):
        self.__textRotation = textRotation


    @property
    def digitWidth(self):
        return self.__digitWidth

    @digitWidth.setter
    def digitWidth(self, digitWidth: str):
        self.__digitWidth = digitWidth


    @property
    def breakOpportunity(self):
        return self.__breakOpportunity

    @breakOpportunity.setter
    def breakOpportunity(self, breakOpportunity: str):
        self.__breakOpportunity = breakOpportunity


    @property
    def backgroundColor(self):
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor


    @property
    def whiteSpaceCollapse(self):
        return self.__whiteSpaceCollapse

    @whiteSpaceCollapse.setter
    def whiteSpaceCollapse(self, whiteSpaceCollapse: str):
        self.__whiteSpaceCollapse = whiteSpaceCollapse


    @property
    def alignmentBaseline(self):
        return self.__alignmentBaseline

    @alignmentBaseline.setter
    def alignmentBaseline(self, alignmentBaseline: str):
        self.__alignmentBaseline = alignmentBaseline


    @property
    def backgroundAlpha(self):
        return self.__backgroundAlpha

    @backgroundAlpha.setter
    def backgroundAlpha(self, backgroundAlpha: str):
        self.__backgroundAlpha = backgroundAlpha


    @property
    def ligatureLevel(self):
        return self.__ligatureLevel

    @ligatureLevel.setter
    def ligatureLevel(self, ligatureLevel: str):
        self.__ligatureLevel = ligatureLevel


    @property
    def textAlpha(self):
        return self.__textAlpha

    @textAlpha.setter
    def textAlpha(self, textAlpha: str):
        self.__textAlpha = textAlpha


    @property
    def baselineShift(self):
        return self.__baselineShift

    @baselineShift.setter
    def baselineShift(self, baselineShift: str):
        self.__baselineShift = baselineShift


    @property
    def trackingRight(self):
        return self.__trackingRight

    @trackingRight.setter
    def trackingRight(self, trackingRight: str):
        self.__trackingRight = trackingRight


    @property
    def textDecoration(self):
        return self.__textDecoration

    @textDecoration.setter
    def textDecoration(self, textDecoration: str):
        self.__textDecoration = textDecoration


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def fontSize(self):
        return self.__fontSize

    @fontSize.setter
    def fontSize(self, fontSize: str):
        self.__fontSize = fontSize


    @property
    def trackingLeft(self):
        return self.__trackingLeft

    @trackingLeft.setter
    def trackingLeft(self, trackingLeft: str):
        self.__trackingLeft = trackingLeft


    @property
    def fontFamily(self):
        return self.__fontFamily

    @fontFamily.setter
    def fontFamily(self, fontFamily: str):
        self.__fontFamily = fontFamily


    @property
    def typographicCase(self):
        return self.__typographicCase

    @typographicCase.setter
    def typographicCase(self, typographicCase: str):
        self.__typographicCase = typographicCase


    @property
    def digitCase(self):
        return self.__digitCase

    @digitCase.setter
    def digitCase(self, digitCase: str):
        self.__digitCase = digitCase


    @property
    def dominantBaseline(self):
        return self.__dominantBaseline

    @dominantBaseline.setter
    def dominantBaseline(self, dominantBaseline: str):
        self.__dominantBaseline = dominantBaseline


    @property
    def fontWeight(self):
        return self.__fontWeight

    @fontWeight.setter
    def fontWeight(self, fontWeight: str):
        self.__fontWeight = fontWeight


    @property
    def lineHeight(self):
        return self.__lineHeight

    @lineHeight.setter
    def lineHeight(self, lineHeight: str):
        self.__lineHeight = lineHeight


    @property
    def kerning(self):
        return self.__kerning

    @kerning.setter
    def kerning(self, kerning: str):
        self.__kerning = kerning


    @property
    def locale(self):
        return self.__locale

    @locale.setter
    def locale(self, locale: str):
        self.__locale = locale


class fxg_ContainerAttributes(ABC):

    def __init__(self, blockProgression: str, paddingLeft: str, paddingRight: str, paddingTop: str, paddingBottom: str, columnGap: str, columnCount: str, columnWidth: str, firstBaselineOffset: str, verticalAlign: str, lineBreak: str):
        self.blockProgression = blockProgression
        self.paddingLeft = paddingLeft
        self.paddingRight = paddingRight
        self.paddingTop = paddingTop
        self.paddingBottom = paddingBottom
        self.columnGap = columnGap
        self.columnCount = columnCount
        self.columnWidth = columnWidth
        self.firstBaselineOffset = firstBaselineOffset
        self.verticalAlign = verticalAlign
        self.lineBreak = lineBreak
        
        pass
    @property
    def columnCount(self):
        return self.__columnCount

    @columnCount.setter
    def columnCount(self, columnCount: str):
        self.__columnCount = columnCount


    @property
    def paddingTop(self):
        return self.__paddingTop

    @paddingTop.setter
    def paddingTop(self, paddingTop: str):
        self.__paddingTop = paddingTop


    @property
    def verticalAlign(self):
        return self.__verticalAlign

    @verticalAlign.setter
    def verticalAlign(self, verticalAlign: str):
        self.__verticalAlign = verticalAlign


    @property
    def paddingLeft(self):
        return self.__paddingLeft

    @paddingLeft.setter
    def paddingLeft(self, paddingLeft: str):
        self.__paddingLeft = paddingLeft


    @property
    def paddingRight(self):
        return self.__paddingRight

    @paddingRight.setter
    def paddingRight(self, paddingRight: str):
        self.__paddingRight = paddingRight


    @property
    def blockProgression(self):
        return self.__blockProgression

    @blockProgression.setter
    def blockProgression(self, blockProgression: str):
        self.__blockProgression = blockProgression


    @property
    def columnWidth(self):
        return self.__columnWidth

    @columnWidth.setter
    def columnWidth(self, columnWidth: str):
        self.__columnWidth = columnWidth


    @property
    def columnGap(self):
        return self.__columnGap

    @columnGap.setter
    def columnGap(self, columnGap: str):
        self.__columnGap = columnGap


    @property
    def paddingBottom(self):
        return self.__paddingBottom

    @paddingBottom.setter
    def paddingBottom(self, paddingBottom: str):
        self.__paddingBottom = paddingBottom


    @property
    def lineBreak(self):
        return self.__lineBreak

    @lineBreak.setter
    def lineBreak(self, lineBreak: str):
        self.__lineBreak = lineBreak


    @property
    def firstBaselineOffset(self):
        return self.__firstBaselineOffset

    @firstBaselineOffset.setter
    def firstBaselineOffset(self, firstBaselineOffset: str):
        self.__firstBaselineOffset = firstBaselineOffset


class fxg_ParagraphAttributes(ABC):

    def __init__(self, paragraphEndIndent: str, paragraphSpaceBefore: str, paragraphSpaceAfter: str, justificationRule: str, justificationStyle: str, textJustify: str, leadingModel: str, tabStops: str, textAlign: str, textAlignLast: str, textIndent: str, paragraphStartIndent: str):
        self.paragraphEndIndent = paragraphEndIndent
        self.paragraphSpaceBefore = paragraphSpaceBefore
        self.paragraphSpaceAfter = paragraphSpaceAfter
        self.justificationRule = justificationRule
        self.justificationStyle = justificationStyle
        self.textJustify = textJustify
        self.leadingModel = leadingModel
        self.tabStops = tabStops
        self.textAlign = textAlign
        self.textAlignLast = textAlignLast
        self.textIndent = textIndent
        self.paragraphStartIndent = paragraphStartIndent
        
        pass
    @property
    def tabStops(self):
        return self.__tabStops

    @tabStops.setter
    def tabStops(self, tabStops: str):
        self.__tabStops = tabStops


    @property
    def textAlignLast(self):
        return self.__textAlignLast

    @textAlignLast.setter
    def textAlignLast(self, textAlignLast: str):
        self.__textAlignLast = textAlignLast


    @property
    def textAlign(self):
        return self.__textAlign

    @textAlign.setter
    def textAlign(self, textAlign: str):
        self.__textAlign = textAlign


    @property
    def textIndent(self):
        return self.__textIndent

    @textIndent.setter
    def textIndent(self, textIndent: str):
        self.__textIndent = textIndent


    @property
    def justificationRule(self):
        return self.__justificationRule

    @justificationRule.setter
    def justificationRule(self, justificationRule: str):
        self.__justificationRule = justificationRule


    @property
    def paragraphEndIndent(self):
        return self.__paragraphEndIndent

    @paragraphEndIndent.setter
    def paragraphEndIndent(self, paragraphEndIndent: str):
        self.__paragraphEndIndent = paragraphEndIndent


    @property
    def paragraphSpaceBefore(self):
        return self.__paragraphSpaceBefore

    @paragraphSpaceBefore.setter
    def paragraphSpaceBefore(self, paragraphSpaceBefore: str):
        self.__paragraphSpaceBefore = paragraphSpaceBefore


    @property
    def justificationStyle(self):
        return self.__justificationStyle

    @justificationStyle.setter
    def justificationStyle(self, justificationStyle: str):
        self.__justificationStyle = justificationStyle


    @property
    def paragraphSpaceAfter(self):
        return self.__paragraphSpaceAfter

    @paragraphSpaceAfter.setter
    def paragraphSpaceAfter(self, paragraphSpaceAfter: str):
        self.__paragraphSpaceAfter = paragraphSpaceAfter


    @property
    def leadingModel(self):
        return self.__leadingModel

    @leadingModel.setter
    def leadingModel(self, leadingModel: str):
        self.__leadingModel = leadingModel


    @property
    def paragraphStartIndent(self):
        return self.__paragraphStartIndent

    @paragraphStartIndent.setter
    def paragraphStartIndent(self, paragraphStartIndent: str):
        self.__paragraphStartIndent = paragraphStartIndent


    @property
    def textJustify(self):
        return self.__textJustify

    @textJustify.setter
    def textJustify(self, textJustify: str):
        self.__textJustify = textJustify


class RichTextContent:

    pass
class fxg_span(RichTextContent, RichTextContentContainer):

    pass
class fxg_img(RichTextContent):

    pass
class fxg_a(RichTextContent, RichTextContentContainer):

    pass
class fxg_div(RichTextContentContainer, RichTextContent):

    pass
class fxg_linkHoverFormat(RichTextContent):

    pass
class fxg_tcy(RichTextContentContainer, RichTextContent):

    pass
class fxg_br(RichTextContent):

    pass
class fxg_linkNormalFormat(RichTextContent):

    pass
class fxg_tab(RichTextContent):

    pass
class fxg_rawtext(RichTextContent):

    def __init__(self, _text: str):
        self._text = _text
        
        pass
    @property
    def _text(self):
        return self.___text

    @_text.setter
    def _text(self, _text: str):
        self.___text = _text


class fxg_RichTextContentContainer(RichTextContent):

    pass
class fxg_RichTextContent(ABC):

    pass
class CharacterAttributes:

    pass
class ContainerAttributes:

    pass
class ParagraphAttributes:

    pass
class fxg_p(RichTextContentContainer, RichTextContent, ParagraphAttributes):

    pass
class Shape:

    pass
class fxg_Line(Shape):

    def __init__(self, yTo: str, x: str, y: str, rotation: str, scaleX: str, scaleY: str, blendMode: str, xFrom: str, yFrom: str, xTo: str, alpha: str, id: str, maskType: str, visible: str, fxg_Line69: "fxg_Stroke" = None, fxg_Line72: "fxg_Group" = None, fxg_Line: "fxg_Transform" = None, fxg_Line63: set["fxg_Filter"] = None, fxg_Line66: "fxg_Fill" = None):
        self.yTo = yTo
        self.x = x
        self.y = y
        self.rotation = rotation
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.blendMode = blendMode
        self.xFrom = xFrom
        self.yFrom = yFrom
        self.xTo = xTo
        self.alpha = alpha
        self.id = id
        self.maskType = maskType
        self.visible = visible
        self.fxg_Line69 = fxg_Line69
        self.fxg_Line72 = fxg_Line72
        self.fxg_Line = fxg_Line
        self.fxg_Line63 = fxg_Line63 if fxg_Line63 is not None else set()
        self.fxg_Line66 = fxg_Line66
        
        pass
    @property
    def blendMode(self):
        return self.__blendMode

    @blendMode.setter
    def blendMode(self, blendMode: str):
        self.__blendMode = blendMode


    @property
    def yFrom(self):
        return self.__yFrom

    @yFrom.setter
    def yFrom(self, yFrom: str):
        self.__yFrom = yFrom


    @property
    def xTo(self):
        return self.__xTo

    @xTo.setter
    def xTo(self, xTo: str):
        self.__xTo = xTo


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def yTo(self):
        return self.__yTo

    @yTo.setter
    def yTo(self, yTo: str):
        self.__yTo = yTo


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible


    @property
    def maskType(self):
        return self.__maskType

    @maskType.setter
    def maskType(self, maskType: str):
        self.__maskType = maskType


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def xFrom(self):
        return self.__xFrom

    @xFrom.setter
    def xFrom(self, xFrom: str):
        self.__xFrom = xFrom


    @property
    def scaleY(self):
        return self.__scaleY

    @scaleY.setter
    def scaleY(self, scaleY: str):
        self.__scaleY = scaleY


    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha


    @property
    def fxg_Line72(self):
        return self.__fxg_Line72

    @fxg_Line72.setter
    def fxg_Line72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Line__fxg_Line72", None)
        self.__fxg_Line72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Group73"):
                opp_val = getattr(old_value, "fxg_Group73", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Group73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Group73"):
                opp_val = getattr(value, "fxg_Group73", None)
                setattr(value, "fxg_Group73", self)

    @property
    def fxg_Line(self):
        return self.__fxg_Line

    @fxg_Line.setter
    def fxg_Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Line__fxg_Line", None)
        self.__fxg_Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Transform61"):
                opp_val = getattr(old_value, "fxg_Transform61", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Transform61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Transform61"):
                opp_val = getattr(value, "fxg_Transform61", None)
                setattr(value, "fxg_Transform61", self)

    @property
    def fxg_Line63(self):
        return self.__fxg_Line63

    @fxg_Line63.setter
    def fxg_Line63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Line__fxg_Line63", None)
        self.__fxg_Line63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fxg_Filter64"):
                    opp_val = getattr(item, "fxg_Filter64", None)
                    
                    if opp_val == self:
                        setattr(item, "fxg_Filter64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fxg_Filter64"):
                    opp_val = getattr(item, "fxg_Filter64", None)
                    
                    setattr(item, "fxg_Filter64", self)
                    

    @property
    def fxg_Line66(self):
        return self.__fxg_Line66

    @fxg_Line66.setter
    def fxg_Line66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Line__fxg_Line66", None)
        self.__fxg_Line66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Fill67"):
                opp_val = getattr(old_value, "fxg_Fill67", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Fill67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Fill67"):
                opp_val = getattr(value, "fxg_Fill67", None)
                setattr(value, "fxg_Fill67", self)

    @property
    def fxg_Line69(self):
        return self.__fxg_Line69

    @fxg_Line69.setter
    def fxg_Line69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Line__fxg_Line69", None)
        self.__fxg_Line69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Stroke70"):
                opp_val = getattr(old_value, "fxg_Stroke70", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Stroke70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Stroke70"):
                opp_val = getattr(value, "fxg_Stroke70", None)
                setattr(value, "fxg_Stroke70", self)

class fxg_Ellipse(Shape):

    def __init__(self, alpha: str, width: str, height: str, x: str, y: str, rotation: str, scaleX: str, scaleY: str, blendMode: str, visible: str, fxg_Ellipse: "fxg_Transform" = None, fxg_Ellipse49: set["fxg_Filter"] = None, fxg_Ellipse52: "fxg_Fill" = None, fxg_Ellipse55: "fxg_Stroke" = None, fxg_Ellipse58: "fxg_Group" = None):
        self.alpha = alpha
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rotation = rotation
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.blendMode = blendMode
        self.visible = visible
        self.fxg_Ellipse = fxg_Ellipse
        self.fxg_Ellipse49 = fxg_Ellipse49 if fxg_Ellipse49 is not None else set()
        self.fxg_Ellipse52 = fxg_Ellipse52
        self.fxg_Ellipse55 = fxg_Ellipse55
        self.fxg_Ellipse58 = fxg_Ellipse58
        
        pass
    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def blendMode(self):
        return self.__blendMode

    @blendMode.setter
    def blendMode(self, blendMode: str):
        self.__blendMode = blendMode


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def scaleY(self):
        return self.__scaleY

    @scaleY.setter
    def scaleY(self, scaleY: str):
        self.__scaleY = scaleY


    @property
    def fxg_Ellipse55(self):
        return self.__fxg_Ellipse55

    @fxg_Ellipse55.setter
    def fxg_Ellipse55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Ellipse__fxg_Ellipse55", None)
        self.__fxg_Ellipse55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Stroke56"):
                opp_val = getattr(old_value, "fxg_Stroke56", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Stroke56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Stroke56"):
                opp_val = getattr(value, "fxg_Stroke56", None)
                setattr(value, "fxg_Stroke56", self)

    @property
    def fxg_Ellipse52(self):
        return self.__fxg_Ellipse52

    @fxg_Ellipse52.setter
    def fxg_Ellipse52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Ellipse__fxg_Ellipse52", None)
        self.__fxg_Ellipse52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Fill53"):
                opp_val = getattr(old_value, "fxg_Fill53", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Fill53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Fill53"):
                opp_val = getattr(value, "fxg_Fill53", None)
                setattr(value, "fxg_Fill53", self)

    @property
    def fxg_Ellipse58(self):
        return self.__fxg_Ellipse58

    @fxg_Ellipse58.setter
    def fxg_Ellipse58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Ellipse__fxg_Ellipse58", None)
        self.__fxg_Ellipse58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Group59"):
                opp_val = getattr(old_value, "fxg_Group59", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Group59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Group59"):
                opp_val = getattr(value, "fxg_Group59", None)
                setattr(value, "fxg_Group59", self)

    @property
    def fxg_Ellipse49(self):
        return self.__fxg_Ellipse49

    @fxg_Ellipse49.setter
    def fxg_Ellipse49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Ellipse__fxg_Ellipse49", None)
        self.__fxg_Ellipse49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fxg_Filter50"):
                    opp_val = getattr(item, "fxg_Filter50", None)
                    
                    if opp_val == self:
                        setattr(item, "fxg_Filter50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fxg_Filter50"):
                    opp_val = getattr(item, "fxg_Filter50", None)
                    
                    setattr(item, "fxg_Filter50", self)
                    

    @property
    def fxg_Ellipse(self):
        return self.__fxg_Ellipse

    @fxg_Ellipse.setter
    def fxg_Ellipse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Ellipse__fxg_Ellipse", None)
        self.__fxg_Ellipse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Transform47"):
                opp_val = getattr(old_value, "fxg_Transform47", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Transform47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Transform47"):
                opp_val = getattr(value, "fxg_Transform47", None)
                setattr(value, "fxg_Transform47", self)

class fxg_Rect(Shape):

    def __init__(self, height: str, radiusX: str, radiusY: str, topLeftRadiusX: str, topLeftRadiusY: str, topRightRadiusX: str, topRightRadiusY: str, bottomLeftRadiusX: str, width: str, bottomLeftRadiusY: str, bottomRightRadiusX: str, bottomRightRadiusY: str, x: str, y: str, rotation: str, scaleX: str, scaleY: str, blendMode: str, visible: str, alpha: str, fxg_Rect: "fxg_Transform" = None, fxg_Rect35: set["fxg_Filter"] = None, fxg_Rect38: "fxg_Fill" = None, fxg_Rect41: "fxg_Stroke" = None, fxg_Rect44: "fxg_Group" = None):
        self.height = height
        self.radiusX = radiusX
        self.radiusY = radiusY
        self.topLeftRadiusX = topLeftRadiusX
        self.topLeftRadiusY = topLeftRadiusY
        self.topRightRadiusX = topRightRadiusX
        self.topRightRadiusY = topRightRadiusY
        self.bottomLeftRadiusX = bottomLeftRadiusX
        self.width = width
        self.bottomLeftRadiusY = bottomLeftRadiusY
        self.bottomRightRadiusX = bottomRightRadiusX
        self.bottomRightRadiusY = bottomRightRadiusY
        self.x = x
        self.y = y
        self.rotation = rotation
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.blendMode = blendMode
        self.visible = visible
        self.alpha = alpha
        self.fxg_Rect = fxg_Rect
        self.fxg_Rect35 = fxg_Rect35 if fxg_Rect35 is not None else set()
        self.fxg_Rect38 = fxg_Rect38
        self.fxg_Rect41 = fxg_Rect41
        self.fxg_Rect44 = fxg_Rect44
        
        pass
    @property
    def topRightRadiusY(self):
        return self.__topRightRadiusY

    @topRightRadiusY.setter
    def topRightRadiusY(self, topRightRadiusY: str):
        self.__topRightRadiusY = topRightRadiusY


    @property
    def radiusY(self):
        return self.__radiusY

    @radiusY.setter
    def radiusY(self, radiusY: str):
        self.__radiusY = radiusY


    @property
    def blendMode(self):
        return self.__blendMode

    @blendMode.setter
    def blendMode(self, blendMode: str):
        self.__blendMode = blendMode


    @property
    def topLeftRadiusY(self):
        return self.__topLeftRadiusY

    @topLeftRadiusY.setter
    def topLeftRadiusY(self, topLeftRadiusY: str):
        self.__topLeftRadiusY = topLeftRadiusY


    @property
    def radiusX(self):
        return self.__radiusX

    @radiusX.setter
    def radiusX(self, radiusX: str):
        self.__radiusX = radiusX


    @property
    def topLeftRadiusX(self):
        return self.__topLeftRadiusX

    @topLeftRadiusX.setter
    def topLeftRadiusX(self, topLeftRadiusX: str):
        self.__topLeftRadiusX = topLeftRadiusX


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def bottomRightRadiusX(self):
        return self.__bottomRightRadiusX

    @bottomRightRadiusX.setter
    def bottomRightRadiusX(self, bottomRightRadiusX: str):
        self.__bottomRightRadiusX = bottomRightRadiusX


    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha


    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def bottomLeftRadiusX(self):
        return self.__bottomLeftRadiusX

    @bottomLeftRadiusX.setter
    def bottomLeftRadiusX(self, bottomLeftRadiusX: str):
        self.__bottomLeftRadiusX = bottomLeftRadiusX


    @property
    def bottomRightRadiusY(self):
        return self.__bottomRightRadiusY

    @bottomRightRadiusY.setter
    def bottomRightRadiusY(self, bottomRightRadiusY: str):
        self.__bottomRightRadiusY = bottomRightRadiusY


    @property
    def bottomLeftRadiusY(self):
        return self.__bottomLeftRadiusY

    @bottomLeftRadiusY.setter
    def bottomLeftRadiusY(self, bottomLeftRadiusY: str):
        self.__bottomLeftRadiusY = bottomLeftRadiusY


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def topRightRadiusX(self):
        return self.__topRightRadiusX

    @topRightRadiusX.setter
    def topRightRadiusX(self, topRightRadiusX: str):
        self.__topRightRadiusX = topRightRadiusX


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible


    @property
    def scaleY(self):
        return self.__scaleY

    @scaleY.setter
    def scaleY(self, scaleY: str):
        self.__scaleY = scaleY


    @property
    def fxg_Rect38(self):
        return self.__fxg_Rect38

    @fxg_Rect38.setter
    def fxg_Rect38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Rect__fxg_Rect38", None)
        self.__fxg_Rect38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Fill39"):
                opp_val = getattr(old_value, "fxg_Fill39", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Fill39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Fill39"):
                opp_val = getattr(value, "fxg_Fill39", None)
                setattr(value, "fxg_Fill39", self)

    @property
    def fxg_Rect(self):
        return self.__fxg_Rect

    @fxg_Rect.setter
    def fxg_Rect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Rect__fxg_Rect", None)
        self.__fxg_Rect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Transform33"):
                opp_val = getattr(old_value, "fxg_Transform33", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Transform33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Transform33"):
                opp_val = getattr(value, "fxg_Transform33", None)
                setattr(value, "fxg_Transform33", self)

    @property
    def fxg_Rect35(self):
        return self.__fxg_Rect35

    @fxg_Rect35.setter
    def fxg_Rect35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Rect__fxg_Rect35", None)
        self.__fxg_Rect35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fxg_Filter36"):
                    opp_val = getattr(item, "fxg_Filter36", None)
                    
                    if opp_val == self:
                        setattr(item, "fxg_Filter36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fxg_Filter36"):
                    opp_val = getattr(item, "fxg_Filter36", None)
                    
                    setattr(item, "fxg_Filter36", self)
                    

    @property
    def fxg_Rect44(self):
        return self.__fxg_Rect44

    @fxg_Rect44.setter
    def fxg_Rect44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Rect__fxg_Rect44", None)
        self.__fxg_Rect44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Group45"):
                opp_val = getattr(old_value, "fxg_Group45", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Group45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Group45"):
                opp_val = getattr(value, "fxg_Group45", None)
                setattr(value, "fxg_Group45", self)

    @property
    def fxg_Rect41(self):
        return self.__fxg_Rect41

    @fxg_Rect41.setter
    def fxg_Rect41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Rect__fxg_Rect41", None)
        self.__fxg_Rect41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Stroke42"):
                opp_val = getattr(old_value, "fxg_Stroke42", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Stroke42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Stroke42"):
                opp_val = getattr(value, "fxg_Stroke42", None)
                setattr(value, "fxg_Stroke42", self)

class fxg_Definition:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class FXGElement:

    pass
class fxg_Stroke(FXGElement):

    pass
class fxg_GradientEntry(FXGElement):

    def __init__(self, color: str, alpha: str, ratio: str):
        self.color = color
        self.alpha = alpha
        self.ratio = ratio
        
        pass
    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha


    @property
    def ratio(self):
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: str):
        self.__ratio = ratio


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


class fxg_BitmapImage(FXGElement):

    def __init__(self, x: str, y: str, width: str, height: str, rotation: str, scaleX: str, scaleY: str, fillMode: str, source: str, visible: str, alpha: str, blendMode: str):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.fillMode = fillMode
        self.source = source
        self.visible = visible
        self.alpha = alpha
        self.blendMode = blendMode
        
        pass
    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def fillMode(self):
        return self.__fillMode

    @fillMode.setter
    def fillMode(self, fillMode: str):
        self.__fillMode = fillMode


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def scaleY(self):
        return self.__scaleY

    @scaleY.setter
    def scaleY(self, scaleY: str):
        self.__scaleY = scaleY


    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def blendMode(self):
        return self.__blendMode

    @blendMode.setter
    def blendMode(self, blendMode: str):
        self.__blendMode = blendMode


class fxg_Shape(FXGElement):

    pass
class fxg_Filter(FXGElement):

    pass
class fxg_PlaceObject(FXGElement):

    def __init__(self, id: str, fxg_PlaceObject: "fxg_Transform" = None, fxg_PlaceObject15: set["fxg_Filter"] = None, fxg_PlaceObject18: "fxg_Group" = None):
        self.id = id
        self.fxg_PlaceObject = fxg_PlaceObject
        self.fxg_PlaceObject15 = fxg_PlaceObject15 if fxg_PlaceObject15 is not None else set()
        self.fxg_PlaceObject18 = fxg_PlaceObject18
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def fxg_PlaceObject15(self):
        return self.__fxg_PlaceObject15

    @fxg_PlaceObject15.setter
    def fxg_PlaceObject15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_PlaceObject__fxg_PlaceObject15", None)
        self.__fxg_PlaceObject15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fxg_Filter16"):
                    opp_val = getattr(item, "fxg_Filter16", None)
                    
                    if opp_val == self:
                        setattr(item, "fxg_Filter16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fxg_Filter16"):
                    opp_val = getattr(item, "fxg_Filter16", None)
                    
                    setattr(item, "fxg_Filter16", self)
                    

    @property
    def fxg_PlaceObject(self):
        return self.__fxg_PlaceObject

    @fxg_PlaceObject.setter
    def fxg_PlaceObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_PlaceObject__fxg_PlaceObject", None)
        self.__fxg_PlaceObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Transform13"):
                opp_val = getattr(old_value, "fxg_Transform13", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Transform13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Transform13"):
                opp_val = getattr(value, "fxg_Transform13", None)
                setattr(value, "fxg_Transform13", self)

    @property
    def fxg_PlaceObject18(self):
        return self.__fxg_PlaceObject18

    @fxg_PlaceObject18.setter
    def fxg_PlaceObject18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_PlaceObject__fxg_PlaceObject18", None)
        self.__fxg_PlaceObject18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Group19"):
                opp_val = getattr(old_value, "fxg_Group19", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Group19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Group19"):
                opp_val = getattr(value, "fxg_Group19", None)
                setattr(value, "fxg_Group19", self)

class fxg_ContainerElement(FXGElement):

    pass
class fxg_Fill(FXGElement):

    pass
class fxg_Transform(FXGElement):

    pass
class fxg_RichText(CharacterAttributes, ParagraphAttributes, ContainerAttributes, FXGElement):

    def __init__(self, rotation: str, scaleX: str, scaleY: str, x: str, y: str, blendMode: str, alpha: str, id: str, maskType: str, visible: str, width: str, height: str, _tempcontent: str, fxg_RichText: set["fxg_RichTextContent"] = None):
        self.rotation = rotation
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.x = x
        self.y = y
        self.blendMode = blendMode
        self.alpha = alpha
        self.id = id
        self.maskType = maskType
        self.visible = visible
        self.width = width
        self.height = height
        self._tempcontent = _tempcontent
        self.fxg_RichText = fxg_RichText if fxg_RichText is not None else set()
        
        pass
    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha


    @property
    def scaleY(self):
        return self.__scaleY

    @scaleY.setter
    def scaleY(self, scaleY: str):
        self.__scaleY = scaleY


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def maskType(self):
        return self.__maskType

    @maskType.setter
    def maskType(self, maskType: str):
        self.__maskType = maskType


    @property
    def _tempcontent(self):
        return self.___tempcontent

    @_tempcontent.setter
    def _tempcontent(self, _tempcontent: str):
        self.___tempcontent = _tempcontent


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def blendMode(self):
        return self.__blendMode

    @blendMode.setter
    def blendMode(self, blendMode: str):
        self.__blendMode = blendMode


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible


    @property
    def fxg_RichText(self):
        return self.__fxg_RichText

    @fxg_RichText.setter
    def fxg_RichText(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_RichText__fxg_RichText", None)
        self.__fxg_RichText = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fxg_RichTextContent"):
                    opp_val = getattr(item, "fxg_RichTextContent", None)
                    
                    if opp_val == self:
                        setattr(item, "fxg_RichTextContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fxg_RichTextContent"):
                    opp_val = getattr(item, "fxg_RichTextContent", None)
                    
                    setattr(item, "fxg_RichTextContent", self)
                    

class fxg_Path(FXGElement):

    def __init__(self, data: str, x: str, y: str, rotation: str, scaleX: str, scaleY: str, blendMode: str, visible: str, alpha: str, winding: str, fxg_Path: "fxg_Fill" = None, fxg_Path22: "fxg_Stroke" = None, fxg_Path24: set["fxg_Filter"] = None, fxg_Path27: "fxg_Transform" = None, fxg_Path30: "fxg_Group" = None):
        self.data = data
        self.x = x
        self.y = y
        self.rotation = rotation
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.blendMode = blendMode
        self.visible = visible
        self.alpha = alpha
        self.winding = winding
        self.fxg_Path = fxg_Path
        self.fxg_Path22 = fxg_Path22
        self.fxg_Path24 = fxg_Path24 if fxg_Path24 is not None else set()
        self.fxg_Path27 = fxg_Path27
        self.fxg_Path30 = fxg_Path30
        
        pass
    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def blendMode(self):
        return self.__blendMode

    @blendMode.setter
    def blendMode(self, blendMode: str):
        self.__blendMode = blendMode


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def scaleY(self):
        return self.__scaleY

    @scaleY.setter
    def scaleY(self, scaleY: str):
        self.__scaleY = scaleY


    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def winding(self):
        return self.__winding

    @winding.setter
    def winding(self, winding: str):
        self.__winding = winding


    @property
    def fxg_Path22(self):
        return self.__fxg_Path22

    @fxg_Path22.setter
    def fxg_Path22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Path__fxg_Path22", None)
        self.__fxg_Path22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Stroke"):
                opp_val = getattr(old_value, "fxg_Stroke", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Stroke", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Stroke"):
                opp_val = getattr(value, "fxg_Stroke", None)
                setattr(value, "fxg_Stroke", self)

    @property
    def fxg_Path27(self):
        return self.__fxg_Path27

    @fxg_Path27.setter
    def fxg_Path27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Path__fxg_Path27", None)
        self.__fxg_Path27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Transform28"):
                opp_val = getattr(old_value, "fxg_Transform28", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Transform28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Transform28"):
                opp_val = getattr(value, "fxg_Transform28", None)
                setattr(value, "fxg_Transform28", self)

    @property
    def fxg_Path30(self):
        return self.__fxg_Path30

    @fxg_Path30.setter
    def fxg_Path30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Path__fxg_Path30", None)
        self.__fxg_Path30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Group31"):
                opp_val = getattr(old_value, "fxg_Group31", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Group31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Group31"):
                opp_val = getattr(value, "fxg_Group31", None)
                setattr(value, "fxg_Group31", self)

    @property
    def fxg_Path(self):
        return self.__fxg_Path

    @fxg_Path.setter
    def fxg_Path(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Path__fxg_Path", None)
        self.__fxg_Path = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Fill"):
                opp_val = getattr(old_value, "fxg_Fill", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Fill", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Fill"):
                opp_val = getattr(value, "fxg_Fill", None)
                setattr(value, "fxg_Fill", self)

    @property
    def fxg_Path24(self):
        return self.__fxg_Path24

    @fxg_Path24.setter
    def fxg_Path24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Path__fxg_Path24", None)
        self.__fxg_Path24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fxg_Filter25"):
                    opp_val = getattr(item, "fxg_Filter25", None)
                    
                    if opp_val == self:
                        setattr(item, "fxg_Filter25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fxg_Filter25"):
                    opp_val = getattr(item, "fxg_Filter25", None)
                    
                    setattr(item, "fxg_Filter25", self)
                    

class fxg_Private(FXGElement):

    pass
class fxg_Library:

    pass
class fxg_Group:

    def __init__(self, rotation: str, scaleX: str, scaleY: str, x: str, y: str, blendMode: str, alpha: str, id: str, transformX: str, transformY: str, maskType: str, visible: str, scaleGridLeft: str, scaleGridRight: str, scaleGridTop: str, scaleGridBottom: str, fxg_Group73: "fxg_Line" = None, fxg_Group: "fxg_Graphic" = None, fxg_Group2: "fxg_Transform" = None, fxg_Group4: set["fxg_Filter"] = None, fxg_Group7: "fxg_Group" = None, fxg_Group5: "fxg_Group" = None, fxg_Group19: "fxg_PlaceObject" = None, fxg_Group31: "fxg_Path" = None, fxg_Group45: "fxg_Rect" = None, fxg_Group59: "fxg_Ellipse" = None):
        self.rotation = rotation
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.x = x
        self.y = y
        self.blendMode = blendMode
        self.alpha = alpha
        self.id = id
        self.transformX = transformX
        self.transformY = transformY
        self.maskType = maskType
        self.visible = visible
        self.scaleGridLeft = scaleGridLeft
        self.scaleGridRight = scaleGridRight
        self.scaleGridTop = scaleGridTop
        self.scaleGridBottom = scaleGridBottom
        self.fxg_Group73 = fxg_Group73
        self.fxg_Group = fxg_Group
        self.fxg_Group2 = fxg_Group2
        self.fxg_Group4 = fxg_Group4 if fxg_Group4 is not None else set()
        self.fxg_Group7 = fxg_Group7
        self.fxg_Group5 = fxg_Group5
        self.fxg_Group19 = fxg_Group19
        self.fxg_Group31 = fxg_Group31
        self.fxg_Group45 = fxg_Group45
        self.fxg_Group59 = fxg_Group59
        
        pass
    @property
    def scaleX(self):
        return self.__scaleX

    @scaleX.setter
    def scaleX(self, scaleX: str):
        self.__scaleX = scaleX


    @property
    def scaleGridTop(self):
        return self.__scaleGridTop

    @scaleGridTop.setter
    def scaleGridTop(self, scaleGridTop: str):
        self.__scaleGridTop = scaleGridTop


    @property
    def scaleGridRight(self):
        return self.__scaleGridRight

    @scaleGridRight.setter
    def scaleGridRight(self, scaleGridRight: str):
        self.__scaleGridRight = scaleGridRight


    @property
    def transformY(self):
        return self.__transformY

    @transformY.setter
    def transformY(self, transformY: str):
        self.__transformY = transformY


    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha


    @property
    def transformX(self):
        return self.__transformX

    @transformX.setter
    def transformX(self, transformX: str):
        self.__transformX = transformX


    @property
    def scaleGridLeft(self):
        return self.__scaleGridLeft

    @scaleGridLeft.setter
    def scaleGridLeft(self, scaleGridLeft: str):
        self.__scaleGridLeft = scaleGridLeft


    @property
    def scaleGridBottom(self):
        return self.__scaleGridBottom

    @scaleGridBottom.setter
    def scaleGridBottom(self, scaleGridBottom: str):
        self.__scaleGridBottom = scaleGridBottom


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def scaleY(self):
        return self.__scaleY

    @scaleY.setter
    def scaleY(self, scaleY: str):
        self.__scaleY = scaleY


    @property
    def blendMode(self):
        return self.__blendMode

    @blendMode.setter
    def blendMode(self, blendMode: str):
        self.__blendMode = blendMode


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def maskType(self):
        return self.__maskType

    @maskType.setter
    def maskType(self, maskType: str):
        self.__maskType = maskType


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def fxg_Group19(self):
        return self.__fxg_Group19

    @fxg_Group19.setter
    def fxg_Group19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Group__fxg_Group19", None)
        self.__fxg_Group19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_PlaceObject18"):
                opp_val = getattr(old_value, "fxg_PlaceObject18", None)
                if opp_val == self:
                    setattr(old_value, "fxg_PlaceObject18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_PlaceObject18"):
                opp_val = getattr(value, "fxg_PlaceObject18", None)
                setattr(value, "fxg_PlaceObject18", self)

    @property
    def fxg_Group4(self):
        return self.__fxg_Group4

    @fxg_Group4.setter
    def fxg_Group4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Group__fxg_Group4", None)
        self.__fxg_Group4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fxg_Filter"):
                    opp_val = getattr(item, "fxg_Filter", None)
                    
                    if opp_val == self:
                        setattr(item, "fxg_Filter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fxg_Filter"):
                    opp_val = getattr(item, "fxg_Filter", None)
                    
                    setattr(item, "fxg_Filter", self)
                    

    @property
    def fxg_Group59(self):
        return self.__fxg_Group59

    @fxg_Group59.setter
    def fxg_Group59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Group__fxg_Group59", None)
        self.__fxg_Group59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Ellipse58"):
                opp_val = getattr(old_value, "fxg_Ellipse58", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Ellipse58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Ellipse58"):
                opp_val = getattr(value, "fxg_Ellipse58", None)
                setattr(value, "fxg_Ellipse58", self)

    @property
    def fxg_Group45(self):
        return self.__fxg_Group45

    @fxg_Group45.setter
    def fxg_Group45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Group__fxg_Group45", None)
        self.__fxg_Group45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Rect44"):
                opp_val = getattr(old_value, "fxg_Rect44", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Rect44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Rect44"):
                opp_val = getattr(value, "fxg_Rect44", None)
                setattr(value, "fxg_Rect44", self)

    @property
    def fxg_Group73(self):
        return self.__fxg_Group73

    @fxg_Group73.setter
    def fxg_Group73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Group__fxg_Group73", None)
        self.__fxg_Group73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Line72"):
                opp_val = getattr(old_value, "fxg_Line72", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Line72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Line72"):
                opp_val = getattr(value, "fxg_Line72", None)
                setattr(value, "fxg_Line72", self)

    @property
    def fxg_Group2(self):
        return self.__fxg_Group2

    @fxg_Group2.setter
    def fxg_Group2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Group__fxg_Group2", None)
        self.__fxg_Group2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Transform"):
                opp_val = getattr(old_value, "fxg_Transform", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Transform", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Transform"):
                opp_val = getattr(value, "fxg_Transform", None)
                setattr(value, "fxg_Transform", self)

    @property
    def fxg_Group5(self):
        return self.__fxg_Group5

    @fxg_Group5.setter
    def fxg_Group5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Group__fxg_Group5", None)
        self.__fxg_Group5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Group7"):
                opp_val = getattr(old_value, "fxg_Group7", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Group7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Group7"):
                opp_val = getattr(value, "fxg_Group7", None)
                setattr(value, "fxg_Group7", self)

    @property
    def fxg_Group(self):
        return self.__fxg_Group

    @fxg_Group.setter
    def fxg_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Group__fxg_Group", None)
        self.__fxg_Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Graphic"):
                opp_val = getattr(old_value, "fxg_Graphic", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Graphic", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Graphic"):
                opp_val = getattr(value, "fxg_Graphic", None)
                setattr(value, "fxg_Graphic", self)

    @property
    def fxg_Group7(self):
        return self.__fxg_Group7

    @fxg_Group7.setter
    def fxg_Group7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Group__fxg_Group7", None)
        self.__fxg_Group7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Group5"):
                opp_val = getattr(old_value, "fxg_Group5", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Group5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Group5"):
                opp_val = getattr(value, "fxg_Group5", None)
                setattr(value, "fxg_Group5", self)

    @property
    def fxg_Group31(self):
        return self.__fxg_Group31

    @fxg_Group31.setter
    def fxg_Group31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Group__fxg_Group31", None)
        self.__fxg_Group31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Path30"):
                opp_val = getattr(old_value, "fxg_Path30", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Path30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Path30"):
                opp_val = getattr(value, "fxg_Path30", None)
                setattr(value, "fxg_Path30", self)

class fxg_Graphic:

    def __init__(self, scaleGridLeft: str, scaleGridRight: str, scaleGridTop: str, scaleGridBottom: str, viewWidth: int, viewHeight: int, version: str, fxg_Graphic: "fxg_Group" = None):
        self.scaleGridLeft = scaleGridLeft
        self.scaleGridRight = scaleGridRight
        self.scaleGridTop = scaleGridTop
        self.scaleGridBottom = scaleGridBottom
        self.viewWidth = viewWidth
        self.viewHeight = viewHeight
        self.version = version
        self.fxg_Graphic = fxg_Graphic
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def scaleGridBottom(self):
        return self.__scaleGridBottom

    @scaleGridBottom.setter
    def scaleGridBottom(self, scaleGridBottom: str):
        self.__scaleGridBottom = scaleGridBottom


    @property
    def scaleGridLeft(self):
        return self.__scaleGridLeft

    @scaleGridLeft.setter
    def scaleGridLeft(self, scaleGridLeft: str):
        self.__scaleGridLeft = scaleGridLeft


    @property
    def scaleGridRight(self):
        return self.__scaleGridRight

    @scaleGridRight.setter
    def scaleGridRight(self, scaleGridRight: str):
        self.__scaleGridRight = scaleGridRight


    @property
    def viewHeight(self):
        return self.__viewHeight

    @viewHeight.setter
    def viewHeight(self, viewHeight: int):
        self.__viewHeight = viewHeight


    @property
    def viewWidth(self):
        return self.__viewWidth

    @viewWidth.setter
    def viewWidth(self, viewWidth: int):
        self.__viewWidth = viewWidth


    @property
    def scaleGridTop(self):
        return self.__scaleGridTop

    @scaleGridTop.setter
    def scaleGridTop(self, scaleGridTop: str):
        self.__scaleGridTop = scaleGridTop


    @property
    def fxg_Graphic(self):
        return self.__fxg_Graphic

    @fxg_Graphic.setter
    def fxg_Graphic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Graphic__fxg_Graphic", None)
        self.__fxg_Graphic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Group"):
                opp_val = getattr(old_value, "fxg_Group", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Group", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Group"):
                opp_val = getattr(value, "fxg_Group", None)
                setattr(value, "fxg_Group", self)

class fxg_ColorTransform(FXGElement):

    def __init__(self, alphaMultiplier: str, alphaOffset: str, blueMultiplier: str, blueOffset: str, greenMultiplier: str, greenOffset: str, redMultiplier: str, redOffset: str, fxg_ColorTransform: "fxg_Transform" = None):
        self.alphaMultiplier = alphaMultiplier
        self.alphaOffset = alphaOffset
        self.blueMultiplier = blueMultiplier
        self.blueOffset = blueOffset
        self.greenMultiplier = greenMultiplier
        self.greenOffset = greenOffset
        self.redMultiplier = redMultiplier
        self.redOffset = redOffset
        self.fxg_ColorTransform = fxg_ColorTransform
        
        pass
    @property
    def redMultiplier(self):
        return self.__redMultiplier

    @redMultiplier.setter
    def redMultiplier(self, redMultiplier: str):
        self.__redMultiplier = redMultiplier


    @property
    def redOffset(self):
        return self.__redOffset

    @redOffset.setter
    def redOffset(self, redOffset: str):
        self.__redOffset = redOffset


    @property
    def blueOffset(self):
        return self.__blueOffset

    @blueOffset.setter
    def blueOffset(self, blueOffset: str):
        self.__blueOffset = blueOffset


    @property
    def greenOffset(self):
        return self.__greenOffset

    @greenOffset.setter
    def greenOffset(self, greenOffset: str):
        self.__greenOffset = greenOffset


    @property
    def greenMultiplier(self):
        return self.__greenMultiplier

    @greenMultiplier.setter
    def greenMultiplier(self, greenMultiplier: str):
        self.__greenMultiplier = greenMultiplier


    @property
    def alphaOffset(self):
        return self.__alphaOffset

    @alphaOffset.setter
    def alphaOffset(self, alphaOffset: str):
        self.__alphaOffset = alphaOffset


    @property
    def alphaMultiplier(self):
        return self.__alphaMultiplier

    @alphaMultiplier.setter
    def alphaMultiplier(self, alphaMultiplier: str):
        self.__alphaMultiplier = alphaMultiplier


    @property
    def blueMultiplier(self):
        return self.__blueMultiplier

    @blueMultiplier.setter
    def blueMultiplier(self, blueMultiplier: str):
        self.__blueMultiplier = blueMultiplier


    @property
    def fxg_ColorTransform(self):
        return self.__fxg_ColorTransform

    @fxg_ColorTransform.setter
    def fxg_ColorTransform(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_ColorTransform__fxg_ColorTransform", None)
        self.__fxg_ColorTransform = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Transform11"):
                opp_val = getattr(old_value, "fxg_Transform11", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Transform11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Transform11"):
                opp_val = getattr(value, "fxg_Transform11", None)
                setattr(value, "fxg_Transform11", self)

class fxg_Matrix(FXGElement):

    def __init__(self, a: str, b: str, c: str, d: str, tx: str, ty: str, fxg_Matrix80: "fxg_RadialGradient" = None, fxg_Matrix78: "fxg_LinearGradient" = None, fxg_Matrix82: "fxg_BitmapFill" = None, fxg_Matrix: "fxg_Transform" = None, fxg_Matrix86: "fxg_RadialGradientStroke" = None, fxg_Matrix84: "fxg_LinearGradientStroke" = None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.tx = tx
        self.ty = ty
        self.fxg_Matrix80 = fxg_Matrix80
        self.fxg_Matrix78 = fxg_Matrix78
        self.fxg_Matrix82 = fxg_Matrix82
        self.fxg_Matrix = fxg_Matrix
        self.fxg_Matrix86 = fxg_Matrix86
        self.fxg_Matrix84 = fxg_Matrix84
        
        pass
    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b


    @property
    def ty(self):
        return self.__ty

    @ty.setter
    def ty(self, ty: str):
        self.__ty = ty


    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, d: str):
        self.__d = d


    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a


    @property
    def tx(self):
        return self.__tx

    @tx.setter
    def tx(self, tx: str):
        self.__tx = tx


    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c


    @property
    def fxg_Matrix78(self):
        return self.__fxg_Matrix78

    @fxg_Matrix78.setter
    def fxg_Matrix78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Matrix__fxg_Matrix78", None)
        self.__fxg_Matrix78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_LinearGradient"):
                opp_val = getattr(old_value, "fxg_LinearGradient", None)
                if opp_val == self:
                    setattr(old_value, "fxg_LinearGradient", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_LinearGradient"):
                opp_val = getattr(value, "fxg_LinearGradient", None)
                setattr(value, "fxg_LinearGradient", self)

    @property
    def fxg_Matrix82(self):
        return self.__fxg_Matrix82

    @fxg_Matrix82.setter
    def fxg_Matrix82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Matrix__fxg_Matrix82", None)
        self.__fxg_Matrix82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_BitmapFill"):
                opp_val = getattr(old_value, "fxg_BitmapFill", None)
                if opp_val == self:
                    setattr(old_value, "fxg_BitmapFill", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_BitmapFill"):
                opp_val = getattr(value, "fxg_BitmapFill", None)
                setattr(value, "fxg_BitmapFill", self)

    @property
    def fxg_Matrix80(self):
        return self.__fxg_Matrix80

    @fxg_Matrix80.setter
    def fxg_Matrix80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Matrix__fxg_Matrix80", None)
        self.__fxg_Matrix80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_RadialGradient"):
                opp_val = getattr(old_value, "fxg_RadialGradient", None)
                if opp_val == self:
                    setattr(old_value, "fxg_RadialGradient", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_RadialGradient"):
                opp_val = getattr(value, "fxg_RadialGradient", None)
                setattr(value, "fxg_RadialGradient", self)

    @property
    def fxg_Matrix86(self):
        return self.__fxg_Matrix86

    @fxg_Matrix86.setter
    def fxg_Matrix86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Matrix__fxg_Matrix86", None)
        self.__fxg_Matrix86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_RadialGradientStroke"):
                opp_val = getattr(old_value, "fxg_RadialGradientStroke", None)
                if opp_val == self:
                    setattr(old_value, "fxg_RadialGradientStroke", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_RadialGradientStroke"):
                opp_val = getattr(value, "fxg_RadialGradientStroke", None)
                setattr(value, "fxg_RadialGradientStroke", self)

    @property
    def fxg_Matrix84(self):
        return self.__fxg_Matrix84

    @fxg_Matrix84.setter
    def fxg_Matrix84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Matrix__fxg_Matrix84", None)
        self.__fxg_Matrix84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_LinearGradientStroke"):
                opp_val = getattr(old_value, "fxg_LinearGradientStroke", None)
                if opp_val == self:
                    setattr(old_value, "fxg_LinearGradientStroke", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_LinearGradientStroke"):
                opp_val = getattr(value, "fxg_LinearGradientStroke", None)
                setattr(value, "fxg_LinearGradientStroke", self)

    @property
    def fxg_Matrix(self):
        return self.__fxg_Matrix

    @fxg_Matrix.setter
    def fxg_Matrix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fxg_Matrix__fxg_Matrix", None)
        self.__fxg_Matrix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fxg_Transform9"):
                opp_val = getattr(old_value, "fxg_Transform9", None)
                if opp_val == self:
                    setattr(old_value, "fxg_Transform9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fxg_Transform9"):
                opp_val = getattr(value, "fxg_Transform9", None)
                setattr(value, "fxg_Transform9", self)
