from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TextOrientationStyle(Enum):
    LEFT_TO_RIGHT = "LEFT_TO_RIGHT"
    RIGHT_TO_LEFT = "RIGHT_TO_LEFT"
class HorizontalAlignmentStyle(Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"
    FILL = "FILL"
class FormAttachmentAlignment(Enum):
    DEFAULT = "DEFAULT"
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    CENTER = "CENTER"
class ButtonStyle(Enum):
    TOGGLE = "TOGGLE"
    PUSH = "PUSH"
    RADIO = "RADIO"
    CHECK = "CHECK"
    ARROW = "ARROW"
class TrimStyle(Enum):
    NOT_TRIM = "NOT_TRIM"
    SHELL_TRIM = "SHELL_TRIM"
    DIALOG_TRIM = "DIALOG_TRIM"
class ProgressState(Enum):
    NORMAL = "NORMAL"
    PAUSED = "PAUSED"
    ERROR = "ERROR"
class BorderStyle(Enum):
    NONE = "NONE"
    BORDER = "BORDER"
class OrientationStyle(Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
class ComboStyle(Enum):
    DROP_DOWN = "DROP_DOWN"
    READ_ONLY = "READ_ONLY"
    SIMPLE = "SIMPLE"
class ArrowStyle(Enum):
    NONE = "NONE"
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class FontStyle(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
class SortDirection(Enum):
    NONE = "NONE"
    UP = "UP"
    DOWN = "DOWN"
class CapStyle(Enum):
    FLAT = "FLAT"
    ROUND = "ROUND"
    SQUARE = "SQUARE"
class ModalStyle(Enum):
    SYSTEM_MODAL = "SYSTEM_MODAL"
    APPLICATION_MODAL = "APPLICATION_MODAL"
    PRIMARY_MODAL = "PRIMARY_MODAL"
class JoinStyle(Enum):
    MITER = "MITER"
    ROUND = "ROUND"
    BEVEL = "BEVEL"
class VerticalAlignmentStyle(Enum):
    CENTER = "CENTER"
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    FILL = "FILL"
class MenuItemStyle(Enum):
    RADIO = "RADIO"
    SEPARATOR = "SEPARATOR"
    PUSH = "PUSH"
    CASCADE = "CASCADE"
    CHECK = "CHECK"
class MenuStyle(Enum):
    POP_UP = "POP_UP"
    DROP_DOWN = "DROP_DOWN"
class MultiplicityStyle(Enum):
    SINGLE = "SINGLE"
    MULTI = "MULTI"
class SystemColors(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
class LineStyle(Enum):
    CUSTOM = "CUSTOM"
    DASH = "DASH"
    DASHDOT = "DASHDOT"
    DASHDOTDOT = "DASHDOTDOT"
    DOT = "DOT"
    SOLID = "SOLID"


############################################
# Definition of Classes
############################################

class swt_Viewer(ABC):

    def __init__(self, input: str):
        self.input = input
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

class swt_TreeViewer:

    pass
class swt_LineAttributes:

    def __init__(self, width: float, style: str, cap: str, join: str, dash: float, dashOffset: float, miterLimit: float):
        self.width = width
        self.style = style
        self.cap = cap
        self.join = join
        self.dash = dash
        self.dashOffset = dashOffset
        self.miterLimit = miterLimit
        
    @property
    def miterLimit(self) -> float:
        return self.__miterLimit

    @miterLimit.setter
    def miterLimit(self, miterLimit: float):
        self.__miterLimit = miterLimit

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def cap(self) -> str:
        return self.__cap

    @cap.setter
    def cap(self, cap: str):
        self.__cap = cap

    @property
    def dash(self) -> float:
        return self.__dash

    @dash.setter
    def dash(self, dash: float):
        self.__dash = dash

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def dashOffset(self) -> float:
        return self.__dashOffset

    @dashOffset.setter
    def dashOffset(self, dashOffset: float):
        self.__dashOffset = dashOffset

    @property
    def join(self) -> str:
        return self.__join

    @join.setter
    def join(self, join: str):
        self.__join = join

class swt_FormAttachment:

    def __init__(self, alignment: str, denominator: int, numerator: int, offset: int, swt_FormAttachment: "swt_FormData" = None, swt_FormAttachment27: "swt_FormData" = None, swt_FormAttachment30: "swt_FormData" = None, swt_FormAttachment33: "swt_FormData" = None, swt_FormAttachment35: "swt_Control" = None):
        self.alignment = alignment
        self.denominator = denominator
        self.numerator = numerator
        self.offset = offset
        self.swt_FormAttachment = swt_FormAttachment
        self.swt_FormAttachment27 = swt_FormAttachment27
        self.swt_FormAttachment30 = swt_FormAttachment30
        self.swt_FormAttachment33 = swt_FormAttachment33
        self.swt_FormAttachment35 = swt_FormAttachment35
        
    @property
    def numerator(self) -> int:
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator: int):
        self.__numerator = numerator

    @property
    def offset(self) -> int:
        return self.__offset

    @offset.setter
    def offset(self, offset: int):
        self.__offset = offset

    @property
    def denominator(self) -> int:
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator: int):
        self.__denominator = denominator

    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def swt_FormAttachment30(self):
        return self.__swt_FormAttachment30

    @swt_FormAttachment30.setter
    def swt_FormAttachment30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormAttachment__swt_FormAttachment30", None)
        self.__swt_FormAttachment30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormData29"):
                opp_val = getattr(old_value, "swt_FormData29", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormData29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormData29"):
                opp_val = getattr(value, "swt_FormData29", None)
                setattr(value, "swt_FormData29", self)

    @property
    def swt_FormAttachment(self):
        return self.__swt_FormAttachment

    @swt_FormAttachment.setter
    def swt_FormAttachment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormAttachment__swt_FormAttachment", None)
        self.__swt_FormAttachment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormData"):
                opp_val = getattr(old_value, "swt_FormData", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormData"):
                opp_val = getattr(value, "swt_FormData", None)
                setattr(value, "swt_FormData", self)

    @property
    def swt_FormAttachment33(self):
        return self.__swt_FormAttachment33

    @swt_FormAttachment33.setter
    def swt_FormAttachment33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormAttachment__swt_FormAttachment33", None)
        self.__swt_FormAttachment33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormData32"):
                opp_val = getattr(old_value, "swt_FormData32", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormData32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormData32"):
                opp_val = getattr(value, "swt_FormData32", None)
                setattr(value, "swt_FormData32", self)

    @property
    def swt_FormAttachment35(self):
        return self.__swt_FormAttachment35

    @swt_FormAttachment35.setter
    def swt_FormAttachment35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormAttachment__swt_FormAttachment35", None)
        self.__swt_FormAttachment35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Control36"):
                opp_val = getattr(old_value, "swt_Control36", None)
                if opp_val == self:
                    setattr(old_value, "swt_Control36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Control36"):
                opp_val = getattr(value, "swt_Control36", None)
                setattr(value, "swt_Control36", self)

    @property
    def swt_FormAttachment27(self):
        return self.__swt_FormAttachment27

    @swt_FormAttachment27.setter
    def swt_FormAttachment27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormAttachment__swt_FormAttachment27", None)
        self.__swt_FormAttachment27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormData26"):
                opp_val = getattr(old_value, "swt_FormData26", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormData26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormData26"):
                opp_val = getattr(value, "swt_FormData26", None)
                setattr(value, "swt_FormData26", self)

class swt_FormLayout:

    def __init__(self, marginWidth: int, marginHeight: int, spacing: int, marginLeft: int, marginTop: int, marginRight: int, marginBottom: int):
        self.marginWidth = marginWidth
        self.marginHeight = marginHeight
        self.spacing = spacing
        self.marginLeft = marginLeft
        self.marginTop = marginTop
        self.marginRight = marginRight
        self.marginBottom = marginBottom
        
    @property
    def marginRight(self) -> int:
        return self.__marginRight

    @marginRight.setter
    def marginRight(self, marginRight: int):
        self.__marginRight = marginRight

    @property
    def marginWidth(self) -> int:
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: int):
        self.__marginWidth = marginWidth

    @property
    def marginTop(self) -> int:
        return self.__marginTop

    @marginTop.setter
    def marginTop(self, marginTop: int):
        self.__marginTop = marginTop

    @property
    def marginBottom(self) -> int:
        return self.__marginBottom

    @marginBottom.setter
    def marginBottom(self, marginBottom: int):
        self.__marginBottom = marginBottom

    @property
    def marginHeight(self) -> int:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: int):
        self.__marginHeight = marginHeight

    @property
    def marginLeft(self) -> int:
        return self.__marginLeft

    @marginLeft.setter
    def marginLeft(self, marginLeft: int):
        self.__marginLeft = marginLeft

    @property
    def spacing(self) -> int:
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: int):
        self.__spacing = spacing

class swt_GridLayout:

    def __init__(self, numColumns: int, makeColumnsEqualWidth: bool, marginWidth: int, marginHeight: int, marginLeft: int, marginTop: int, marginRight: int, marginBottom: int, horizontalSpacing: int, verticalSpacing: int):
        self.numColumns = numColumns
        self.makeColumnsEqualWidth = makeColumnsEqualWidth
        self.marginWidth = marginWidth
        self.marginHeight = marginHeight
        self.marginLeft = marginLeft
        self.marginTop = marginTop
        self.marginRight = marginRight
        self.marginBottom = marginBottom
        self.horizontalSpacing = horizontalSpacing
        self.verticalSpacing = verticalSpacing
        
    @property
    def marginHeight(self) -> int:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: int):
        self.__marginHeight = marginHeight

    @property
    def makeColumnsEqualWidth(self) -> bool:
        return self.__makeColumnsEqualWidth

    @makeColumnsEqualWidth.setter
    def makeColumnsEqualWidth(self, makeColumnsEqualWidth: bool):
        self.__makeColumnsEqualWidth = makeColumnsEqualWidth

    @property
    def marginLeft(self) -> int:
        return self.__marginLeft

    @marginLeft.setter
    def marginLeft(self, marginLeft: int):
        self.__marginLeft = marginLeft

    @property
    def marginRight(self) -> int:
        return self.__marginRight

    @marginRight.setter
    def marginRight(self, marginRight: int):
        self.__marginRight = marginRight

    @property
    def marginWidth(self) -> int:
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: int):
        self.__marginWidth = marginWidth

    @property
    def numColumns(self) -> int:
        return self.__numColumns

    @numColumns.setter
    def numColumns(self, numColumns: int):
        self.__numColumns = numColumns

    @property
    def verticalSpacing(self) -> int:
        return self.__verticalSpacing

    @verticalSpacing.setter
    def verticalSpacing(self, verticalSpacing: int):
        self.__verticalSpacing = verticalSpacing

    @property
    def marginBottom(self) -> int:
        return self.__marginBottom

    @marginBottom.setter
    def marginBottom(self, marginBottom: int):
        self.__marginBottom = marginBottom

    @property
    def horizontalSpacing(self) -> int:
        return self.__horizontalSpacing

    @horizontalSpacing.setter
    def horizontalSpacing(self, horizontalSpacing: int):
        self.__horizontalSpacing = horizontalSpacing

    @property
    def marginTop(self) -> int:
        return self.__marginTop

    @marginTop.setter
    def marginTop(self, marginTop: int):
        self.__marginTop = marginTop

class swt_RowLayout:

    def __init__(self, justify: bool, marginLeft: int, marginTop: int, marginRight: int, marginBottom: int, orientationStyle: str, marginWidth: int, marginHeight: int, spacing: int, wrap: bool, pack: bool, fill: bool, center: bool):
        self.justify = justify
        self.marginLeft = marginLeft
        self.marginTop = marginTop
        self.marginRight = marginRight
        self.marginBottom = marginBottom
        self.orientationStyle = orientationStyle
        self.marginWidth = marginWidth
        self.marginHeight = marginHeight
        self.spacing = spacing
        self.wrap = wrap
        self.pack = pack
        self.fill = fill
        self.center = center
        
    @property
    def marginRight(self) -> int:
        return self.__marginRight

    @marginRight.setter
    def marginRight(self, marginRight: int):
        self.__marginRight = marginRight

    @property
    def orientationStyle(self) -> str:
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle

    @property
    def marginWidth(self) -> int:
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: int):
        self.__marginWidth = marginWidth

    @property
    def marginBottom(self) -> int:
        return self.__marginBottom

    @marginBottom.setter
    def marginBottom(self, marginBottom: int):
        self.__marginBottom = marginBottom

    @property
    def marginLeft(self) -> int:
        return self.__marginLeft

    @marginLeft.setter
    def marginLeft(self, marginLeft: int):
        self.__marginLeft = marginLeft

    @property
    def center(self) -> bool:
        return self.__center

    @center.setter
    def center(self, center: bool):
        self.__center = center

    @property
    def marginTop(self) -> int:
        return self.__marginTop

    @marginTop.setter
    def marginTop(self, marginTop: int):
        self.__marginTop = marginTop

    @property
    def pack(self) -> bool:
        return self.__pack

    @pack.setter
    def pack(self, pack: bool):
        self.__pack = pack

    @property
    def justify(self) -> bool:
        return self.__justify

    @justify.setter
    def justify(self, justify: bool):
        self.__justify = justify

    @property
    def spacing(self) -> int:
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: int):
        self.__spacing = spacing

    @property
    def marginHeight(self) -> int:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: int):
        self.__marginHeight = marginHeight

    @property
    def wrap(self) -> bool:
        return self.__wrap

    @wrap.setter
    def wrap(self, wrap: bool):
        self.__wrap = wrap

    @property
    def fill(self) -> bool:
        return self.__fill

    @fill.setter
    def fill(self, fill: bool):
        self.__fill = fill

class LayoutData:

    pass
class swt_FormData(LayoutData):

    def __init__(self, width: int, height: int, swt_FormData: "swt_FormAttachment" = None, swt_FormData26: "swt_FormAttachment" = None, swt_FormData29: "swt_FormAttachment" = None, swt_FormData32: "swt_FormAttachment" = None):
        self.width = width
        self.height = height
        self.swt_FormData = swt_FormData
        self.swt_FormData26 = swt_FormData26
        self.swt_FormData29 = swt_FormData29
        self.swt_FormData32 = swt_FormData32
        
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
    def swt_FormData(self):
        return self.__swt_FormData

    @swt_FormData.setter
    def swt_FormData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormData__swt_FormData", None)
        self.__swt_FormData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormAttachment"):
                opp_val = getattr(old_value, "swt_FormAttachment", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormAttachment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormAttachment"):
                opp_val = getattr(value, "swt_FormAttachment", None)
                setattr(value, "swt_FormAttachment", self)

    @property
    def swt_FormData32(self):
        return self.__swt_FormData32

    @swt_FormData32.setter
    def swt_FormData32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormData__swt_FormData32", None)
        self.__swt_FormData32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormAttachment33"):
                opp_val = getattr(old_value, "swt_FormAttachment33", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormAttachment33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormAttachment33"):
                opp_val = getattr(value, "swt_FormAttachment33", None)
                setattr(value, "swt_FormAttachment33", self)

    @property
    def swt_FormData29(self):
        return self.__swt_FormData29

    @swt_FormData29.setter
    def swt_FormData29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormData__swt_FormData29", None)
        self.__swt_FormData29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormAttachment30"):
                opp_val = getattr(old_value, "swt_FormAttachment30", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormAttachment30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormAttachment30"):
                opp_val = getattr(value, "swt_FormAttachment30", None)
                setattr(value, "swt_FormAttachment30", self)

    @property
    def swt_FormData26(self):
        return self.__swt_FormData26

    @swt_FormData26.setter
    def swt_FormData26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormData__swt_FormData26", None)
        self.__swt_FormData26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormAttachment27"):
                opp_val = getattr(old_value, "swt_FormAttachment27", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormAttachment27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormAttachment27"):
                opp_val = getattr(value, "swt_FormAttachment27", None)
                setattr(value, "swt_FormAttachment27", self)

class swt_GridData(LayoutData):

    def __init__(self, verticalAlignment: str, horizontalAlignment: str, widthHint: int, heightHint: int, horizontalIndent: int, verticalIndent: int, horizontalSpan: int, verticalSpan: int, grabExcessHorizontalSpace: bool, grabExcessVerticalSpace: bool, minimumWidth: int, minimumHeight: int, exclude: bool):
        self.verticalAlignment = verticalAlignment
        self.horizontalAlignment = horizontalAlignment
        self.widthHint = widthHint
        self.heightHint = heightHint
        self.horizontalIndent = horizontalIndent
        self.verticalIndent = verticalIndent
        self.horizontalSpan = horizontalSpan
        self.verticalSpan = verticalSpan
        self.grabExcessHorizontalSpace = grabExcessHorizontalSpace
        self.grabExcessVerticalSpace = grabExcessVerticalSpace
        self.minimumWidth = minimumWidth
        self.minimumHeight = minimumHeight
        self.exclude = exclude
        
    @property
    def exclude(self) -> bool:
        return self.__exclude

    @exclude.setter
    def exclude(self, exclude: bool):
        self.__exclude = exclude

    @property
    def minimumWidth(self) -> int:
        return self.__minimumWidth

    @minimumWidth.setter
    def minimumWidth(self, minimumWidth: int):
        self.__minimumWidth = minimumWidth

    @property
    def verticalAlignment(self) -> str:
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment

    @property
    def heightHint(self) -> int:
        return self.__heightHint

    @heightHint.setter
    def heightHint(self, heightHint: int):
        self.__heightHint = heightHint

    @property
    def widthHint(self) -> int:
        return self.__widthHint

    @widthHint.setter
    def widthHint(self, widthHint: int):
        self.__widthHint = widthHint

    @property
    def grabExcessHorizontalSpace(self) -> bool:
        return self.__grabExcessHorizontalSpace

    @grabExcessHorizontalSpace.setter
    def grabExcessHorizontalSpace(self, grabExcessHorizontalSpace: bool):
        self.__grabExcessHorizontalSpace = grabExcessHorizontalSpace

    @property
    def horizontalSpan(self) -> int:
        return self.__horizontalSpan

    @horizontalSpan.setter
    def horizontalSpan(self, horizontalSpan: int):
        self.__horizontalSpan = horizontalSpan

    @property
    def horizontalIndent(self) -> int:
        return self.__horizontalIndent

    @horizontalIndent.setter
    def horizontalIndent(self, horizontalIndent: int):
        self.__horizontalIndent = horizontalIndent

    @property
    def grabExcessVerticalSpace(self) -> bool:
        return self.__grabExcessVerticalSpace

    @grabExcessVerticalSpace.setter
    def grabExcessVerticalSpace(self, grabExcessVerticalSpace: bool):
        self.__grabExcessVerticalSpace = grabExcessVerticalSpace

    @property
    def verticalSpan(self) -> int:
        return self.__verticalSpan

    @verticalSpan.setter
    def verticalSpan(self, verticalSpan: int):
        self.__verticalSpan = verticalSpan

    @property
    def minimumHeight(self) -> int:
        return self.__minimumHeight

    @minimumHeight.setter
    def minimumHeight(self, minimumHeight: int):
        self.__minimumHeight = minimumHeight

    @property
    def horizontalAlignment(self) -> str:
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment

    @property
    def verticalIndent(self) -> int:
        return self.__verticalIndent

    @verticalIndent.setter
    def verticalIndent(self, verticalIndent: int):
        self.__verticalIndent = verticalIndent

class swt_RowData(LayoutData):

    def __init__(self, width: int, height: int, exclude: bool):
        self.width = width
        self.height = height
        self.exclude = exclude
        
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
    def exclude(self) -> bool:
        return self.__exclude

    @exclude.setter
    def exclude(self, exclude: bool):
        self.__exclude = exclude

class Color:

    pass
class swt_RGBColor(Color):

    def __init__(self, blue: int, red: int, green: int):
        self.blue = blue
        self.red = red
        self.green = green
        
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

class swt_SystemColor(Color):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class swt_FillLayout:

    def __init__(self, orientationStyle: str, marginWidth: int, marginHeight: int, spacing: int):
        self.orientationStyle = orientationStyle
        self.marginWidth = marginWidth
        self.marginHeight = marginHeight
        self.spacing = spacing
        
    @property
    def marginWidth(self) -> int:
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: int):
        self.__marginWidth = marginWidth

    @property
    def marginHeight(self) -> int:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: int):
        self.__marginHeight = marginHeight

    @property
    def orientationStyle(self) -> str:
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle

    @property
    def spacing(self) -> int:
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: int):
        self.__spacing = spacing

class AbstractList:

    pass
class swt_List(AbstractList):

    def __init__(self, selectionIndices: int, selection: str, multiplicityStyle: str):
        self.selectionIndices = selectionIndices
        self.selection = selection
        self.multiplicityStyle = multiplicityStyle
        
    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def multiplicityStyle(self) -> str:
        return self.__multiplicityStyle

    @multiplicityStyle.setter
    def multiplicityStyle(self, multiplicityStyle: str):
        self.__multiplicityStyle = multiplicityStyle

    @property
    def selectionIndices(self) -> int:
        return self.__selectionIndices

    @selectionIndices.setter
    def selectionIndices(self, selectionIndices: int):
        self.__selectionIndices = selectionIndices

class swt_Combo(AbstractList):

    def __init__(self, text: str, textLimit: int):
        self.text = text
        self.textLimit = textLimit
        
    @property
    def textLimit(self) -> int:
        return self.__textLimit

    @textLimit.setter
    def textLimit(self, textLimit: int):
        self.__textLimit = textLimit

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class IntervalSelector:

    pass
class swt_Spinner(IntervalSelector):

    def __init__(self, digits: int, textLimit: int):
        self.digits = digits
        self.textLimit = textLimit
        
    @property
    def textLimit(self) -> int:
        return self.__textLimit

    @textLimit.setter
    def textLimit(self, textLimit: int):
        self.__textLimit = textLimit

    @property
    def digits(self) -> int:
        return self.__digits

    @digits.setter
    def digits(self, digits: int):
        self.__digits = digits

class swt_Slider(IntervalSelector):

    def __init__(self, thumb: int):
        self.thumb = thumb
        
    @property
    def thumb(self) -> int:
        return self.__thumb

    @thumb.setter
    def thumb(self, thumb: int):
        self.__thumb = thumb

class IntervalControl:

    pass
class swt_ProgressBar(IntervalControl):

    def __init__(self, state: str):
        self.state = state
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

class swt_IntervalSelector(IntervalControl):

    def __init__(self, orientationStyle: str, increment: int, pageIncrement: int):
        self.orientationStyle = orientationStyle
        self.increment = increment
        self.pageIncrement = pageIncrement
        
    @property
    def increment(self) -> int:
        return self.__increment

    @increment.setter
    def increment(self, increment: int):
        self.__increment = increment

    @property
    def pageIncrement(self) -> int:
        return self.__pageIncrement

    @pageIncrement.setter
    def pageIncrement(self, pageIncrement: int):
        self.__pageIncrement = pageIncrement

    @property
    def orientationStyle(self) -> str:
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle

class Text:

    pass
class swt_SearchText(Text):

    pass
class swt_PasswordText(Text):

    pass
class swt_CoolBar:

    def __init__(self, orientationStyle: str, parent15: set["swt_CoolItem"] = None, CoolBar: "swt_CoolItem" = None):
        self.orientationStyle = orientationStyle
        self.parent15 = parent15 if parent15 is not None else set()
        self.CoolBar = CoolBar
        
    @property
    def orientationStyle(self) -> str:
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle

    @property
    def CoolBar(self):
        return self.__CoolBar

    @CoolBar.setter
    def CoolBar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_CoolBar__CoolBar", None)
        self.__CoolBar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items17"):
                opp_val = getattr(old_value, "items17", None)
                if opp_val == self:
                    setattr(old_value, "items17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items17"):
                opp_val = getattr(value, "items17", None)
                setattr(value, "items17", self)

    @property
    def parent15(self):
        return self.__parent15

    @parent15.setter
    def parent15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_CoolBar__parent15", None)
        self.__parent15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CoolItem"):
                    opp_val = getattr(item, "CoolItem", None)
                    
                    if opp_val == self:
                        setattr(item, "CoolItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CoolItem"):
                    opp_val = getattr(item, "CoolItem", None)
                    
                    setattr(item, "CoolItem", self)
                    

class Item:

    pass
class swt_CoolItem(Item):

    def __init__(self, minimumSize: str, preferredSize: str, size: str, CoolItem: "swt_CoolBar" = None, items17: "swt_CoolBar" = None, swt_CoolItem: "swt_Control" = None):
        self.minimumSize = minimumSize
        self.preferredSize = preferredSize
        self.size = size
        self.CoolItem = CoolItem
        self.items17 = items17
        self.swt_CoolItem = swt_CoolItem
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def preferredSize(self) -> str:
        return self.__preferredSize

    @preferredSize.setter
    def preferredSize(self, preferredSize: str):
        self.__preferredSize = preferredSize

    @property
    def minimumSize(self) -> str:
        return self.__minimumSize

    @minimumSize.setter
    def minimumSize(self, minimumSize: str):
        self.__minimumSize = minimumSize

    @property
    def items17(self):
        return self.__items17

    @items17.setter
    def items17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_CoolItem__items17", None)
        self.__items17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CoolBar"):
                opp_val = getattr(old_value, "CoolBar", None)
                if opp_val == self:
                    setattr(old_value, "CoolBar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CoolBar"):
                opp_val = getattr(value, "CoolBar", None)
                setattr(value, "CoolBar", self)

    @property
    def swt_CoolItem(self):
        return self.__swt_CoolItem

    @swt_CoolItem.setter
    def swt_CoolItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_CoolItem__swt_CoolItem", None)
        self.__swt_CoolItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Control19"):
                opp_val = getattr(old_value, "swt_Control19", None)
                if opp_val == self:
                    setattr(old_value, "swt_Control19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Control19"):
                opp_val = getattr(value, "swt_Control19", None)
                setattr(value, "swt_Control19", self)

    @property
    def CoolItem(self):
        return self.__CoolItem

    @CoolItem.setter
    def CoolItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_CoolItem__CoolItem", None)
        self.__CoolItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent15"):
                opp_val = getattr(old_value, "parent15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent15"):
                opp_val = getattr(value, "parent15", None)
                if opp_val is None:
                    setattr(value, "parent15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swt_TreeColumn(Item):

    def __init__(self, toolTipText: str, displayText: str, swt_TreeColumn: "swt_Tree" = None, swt_TreeColumn40: "swt_Tree" = None):
        self.toolTipText = toolTipText
        self.displayText = displayText
        self.swt_TreeColumn = swt_TreeColumn
        self.swt_TreeColumn40 = swt_TreeColumn40
        
    @property
    def toolTipText(self) -> str:
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText

    @property
    def displayText(self) -> str:
        return self.__displayText

    @displayText.setter
    def displayText(self, displayText: str):
        self.__displayText = displayText

    @property
    def swt_TreeColumn40(self):
        return self.__swt_TreeColumn40

    @swt_TreeColumn40.setter
    def swt_TreeColumn40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_TreeColumn__swt_TreeColumn40", None)
        self.__swt_TreeColumn40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Tree39"):
                opp_val = getattr(old_value, "swt_Tree39", None)
                if opp_val == self:
                    setattr(old_value, "swt_Tree39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Tree39"):
                opp_val = getattr(value, "swt_Tree39", None)
                setattr(value, "swt_Tree39", self)

    @property
    def swt_TreeColumn(self):
        return self.__swt_TreeColumn

    @swt_TreeColumn.setter
    def swt_TreeColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_TreeColumn__swt_TreeColumn", None)
        self.__swt_TreeColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Tree"):
                opp_val = getattr(old_value, "swt_Tree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Tree"):
                opp_val = getattr(value, "swt_Tree", None)
                if opp_val is None:
                    setattr(value, "swt_Tree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swt_ToolItem(Item):

    def __init__(self, enabled: bool, hotImage: str, toolTipText: str, selection: bool, ToolItem: "swt_ToolBar" = None, items: "swt_ToolBar" = None):
        self.enabled = enabled
        self.hotImage = hotImage
        self.toolTipText = toolTipText
        self.selection = selection
        self.ToolItem = ToolItem
        self.items = items
        
    @property
    def toolTipText(self) -> str:
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText

    @property
    def hotImage(self) -> str:
        return self.__hotImage

    @hotImage.setter
    def hotImage(self, hotImage: str):
        self.__hotImage = hotImage

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def selection(self) -> bool:
        return self.__selection

    @selection.setter
    def selection(self, selection: bool):
        self.__selection = selection

    @property
    def ToolItem(self):
        return self.__ToolItem

    @ToolItem.setter
    def ToolItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_ToolItem__ToolItem", None)
        self.__ToolItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent12"):
                opp_val = getattr(old_value, "parent12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent12"):
                opp_val = getattr(value, "parent12", None)
                if opp_val is None:
                    setattr(value, "parent12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_ToolItem__items", None)
        self.__items = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ToolBar"):
                opp_val = getattr(old_value, "ToolBar", None)
                if opp_val == self:
                    setattr(old_value, "ToolBar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ToolBar"):
                opp_val = getattr(value, "ToolBar", None)
                setattr(value, "ToolBar", self)

class swt_TabItem(Item):

    def __init__(self, toolTipText: str, swt_TabItem: "swt_TabFolder" = None, swt_TabItem22: "swt_Control" = None):
        self.toolTipText = toolTipText
        self.swt_TabItem = swt_TabItem
        self.swt_TabItem22 = swt_TabItem22
        
    @property
    def toolTipText(self) -> str:
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText

    @property
    def swt_TabItem22(self):
        return self.__swt_TabItem22

    @swt_TabItem22.setter
    def swt_TabItem22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_TabItem__swt_TabItem22", None)
        self.__swt_TabItem22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Control23"):
                opp_val = getattr(old_value, "swt_Control23", None)
                if opp_val == self:
                    setattr(old_value, "swt_Control23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Control23"):
                opp_val = getattr(value, "swt_Control23", None)
                setattr(value, "swt_Control23", self)

    @property
    def swt_TabItem(self):
        return self.__swt_TabItem

    @swt_TabItem.setter
    def swt_TabItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_TabItem__swt_TabItem", None)
        self.__swt_TabItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_TabFolder"):
                opp_val = getattr(old_value, "swt_TabFolder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_TabFolder"):
                opp_val = getattr(value, "swt_TabFolder", None)
                if opp_val is None:
                    setattr(value, "swt_TabFolder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Labeled:

    pass
class swt_Labeled(ABC):

    def __init__(self, text: str, image: str):
        self.text = text
        self.image = image
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

class AbstractMenu:

    pass
class swt_Menu(AbstractMenu):

    def __init__(self, menuStyle: str, menu: "swt_MenuItem" = None, Menu: "swt_MenuItem" = None):
        self.menuStyle = menuStyle
        self.menu = menu
        self.Menu = Menu
        
    @property
    def menuStyle(self) -> str:
        return self.__menuStyle

    @menuStyle.setter
    def menuStyle(self, menuStyle: str):
        self.__menuStyle = menuStyle

    @property
    def Menu(self):
        return self.__Menu

    @Menu.setter
    def Menu(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Menu__Menu", None)
        self.__Menu = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentItem"):
                opp_val = getattr(old_value, "parentItem", None)
                if opp_val == self:
                    setattr(old_value, "parentItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentItem"):
                opp_val = getattr(value, "parentItem", None)
                setattr(value, "parentItem", self)

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Menu__menu", None)
        self.__menu = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MenuItem"):
                opp_val = getattr(old_value, "MenuItem", None)
                if opp_val == self:
                    setattr(old_value, "MenuItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MenuItem"):
                opp_val = getattr(value, "MenuItem", None)
                setattr(value, "MenuItem", self)

class swt_MenuItem(Item):

    def __init__(self, menuItemStyle: str, ID: int, accelerator: int, enabled: bool, selection: bool, swt_MenuItem: "swt_AbstractMenu" = None, MenuItem: "swt_Menu" = None, parentItem: "swt_Menu" = None):
        self.menuItemStyle = menuItemStyle
        self.ID = ID
        self.accelerator = accelerator
        self.enabled = enabled
        self.selection = selection
        self.swt_MenuItem = swt_MenuItem
        self.MenuItem = MenuItem
        self.parentItem = parentItem
        
    @property
    def menuItemStyle(self) -> str:
        return self.__menuItemStyle

    @menuItemStyle.setter
    def menuItemStyle(self, menuItemStyle: str):
        self.__menuItemStyle = menuItemStyle

    @property
    def selection(self) -> bool:
        return self.__selection

    @selection.setter
    def selection(self, selection: bool):
        self.__selection = selection

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def accelerator(self) -> int:
        return self.__accelerator

    @accelerator.setter
    def accelerator(self, accelerator: int):
        self.__accelerator = accelerator

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def MenuItem(self):
        return self.__MenuItem

    @MenuItem.setter
    def MenuItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_MenuItem__MenuItem", None)
        self.__MenuItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu"):
                opp_val = getattr(old_value, "menu", None)
                if opp_val == self:
                    setattr(old_value, "menu", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu"):
                opp_val = getattr(value, "menu", None)
                setattr(value, "menu", self)

    @property
    def swt_MenuItem(self):
        return self.__swt_MenuItem

    @swt_MenuItem.setter
    def swt_MenuItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_MenuItem__swt_MenuItem", None)
        self.__swt_MenuItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_AbstractMenu"):
                opp_val = getattr(old_value, "swt_AbstractMenu", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_AbstractMenu"):
                opp_val = getattr(value, "swt_AbstractMenu", None)
                if opp_val is None:
                    setattr(value, "swt_AbstractMenu", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parentItem(self):
        return self.__parentItem

    @parentItem.setter
    def parentItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_MenuItem__parentItem", None)
        self.__parentItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Menu"):
                opp_val = getattr(old_value, "Menu", None)
                if opp_val == self:
                    setattr(old_value, "Menu", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Menu"):
                opp_val = getattr(value, "Menu", None)
                setattr(value, "Menu", self)

class Decorations:

    pass
class swt_Shell(Decorations):

    def __init__(self, modalStyle: str, trimStyle: str, fullScreen: bool, alpha: int, swt_Shell: "swt_Button" = None):
        self.modalStyle = modalStyle
        self.trimStyle = trimStyle
        self.fullScreen = fullScreen
        self.alpha = alpha
        self.swt_Shell = swt_Shell
        
    @property
    def alpha(self) -> int:
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: int):
        self.__alpha = alpha

    @property
    def fullScreen(self) -> bool:
        return self.__fullScreen

    @fullScreen.setter
    def fullScreen(self, fullScreen: bool):
        self.__fullScreen = fullScreen

    @property
    def modalStyle(self) -> str:
        return self.__modalStyle

    @modalStyle.setter
    def modalStyle(self, modalStyle: str):
        self.__modalStyle = modalStyle

    @property
    def trimStyle(self) -> str:
        return self.__trimStyle

    @trimStyle.setter
    def trimStyle(self, trimStyle: str):
        self.__trimStyle = trimStyle

    @property
    def swt_Shell(self):
        return self.__swt_Shell

    @swt_Shell.setter
    def swt_Shell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Shell__swt_Shell", None)
        self.__swt_Shell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Button"):
                opp_val = getattr(old_value, "swt_Button", None)
                if opp_val == self:
                    setattr(old_value, "swt_Button", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Button"):
                opp_val = getattr(value, "swt_Button", None)
                setattr(value, "swt_Button", self)

class swt_MenuBar(AbstractMenu):

    pass
class Canvas:

    pass
class swt_Decorations(Canvas):

    def __init__(self, maximized: bool, minimized: bool, parent: "swt_MenuBar" = None, Decorations: "swt_MenuBar" = None):
        self.maximized = maximized
        self.minimized = minimized
        self.parent = parent
        self.Decorations = Decorations
        
    @property
    def minimized(self) -> bool:
        return self.__minimized

    @minimized.setter
    def minimized(self, minimized: bool):
        self.__minimized = minimized

    @property
    def maximized(self) -> bool:
        return self.__maximized

    @maximized.setter
    def maximized(self, maximized: bool):
        self.__maximized = maximized

    @property
    def Decorations(self):
        return self.__Decorations

    @Decorations.setter
    def Decorations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Decorations__Decorations", None)
        self.__Decorations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menuBar"):
                opp_val = getattr(old_value, "menuBar", None)
                if opp_val == self:
                    setattr(old_value, "menuBar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menuBar"):
                opp_val = getattr(value, "menuBar", None)
                setattr(value, "menuBar", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Decorations__parent", None)
        self.__parent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MenuBar"):
                opp_val = getattr(old_value, "MenuBar", None)
                if opp_val == self:
                    setattr(old_value, "MenuBar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MenuBar"):
                opp_val = getattr(value, "MenuBar", None)
                setattr(value, "MenuBar", self)

class Composite:

    pass
class swt_Canvas(Composite):

    pass
class swt_Group(Composite):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class swt_Composite:

    pass
class swt_Layout(ABC):

    pass
class Control:

    pass
class swt_Separator(Control):

    def __init__(self, orientationStyle: str):
        self.orientationStyle = orientationStyle
        
    @property
    def orientationStyle(self) -> str:
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle

class swt_AbstractList(Control):

    def __init__(self, items: str, selectionIndex: int):
        self.items = items
        self.selectionIndex = selectionIndex
        
    @property
    def selectionIndex(self) -> int:
        return self.__selectionIndex

    @selectionIndex.setter
    def selectionIndex(self, selectionIndex: int):
        self.__selectionIndex = selectionIndex

    @property
    def items(self) -> str:
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items

class swt_Button(Labeled, Control):

    def __init__(self, buttonStyle: str, arrowStyle: str, selection: bool, swt_Button: "swt_Shell" = None):
        self.buttonStyle = buttonStyle
        self.arrowStyle = arrowStyle
        self.selection = selection
        self.swt_Button = swt_Button
        
    @property
    def arrowStyle(self) -> str:
        return self.__arrowStyle

    @arrowStyle.setter
    def arrowStyle(self, arrowStyle: str):
        self.__arrowStyle = arrowStyle

    @property
    def selection(self) -> bool:
        return self.__selection

    @selection.setter
    def selection(self, selection: bool):
        self.__selection = selection

    @property
    def buttonStyle(self) -> str:
        return self.__buttonStyle

    @buttonStyle.setter
    def buttonStyle(self, buttonStyle: str):
        self.__buttonStyle = buttonStyle

    @property
    def swt_Button(self):
        return self.__swt_Button

    @swt_Button.setter
    def swt_Button(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Button__swt_Button", None)
        self.__swt_Button = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Shell"):
                opp_val = getattr(old_value, "swt_Shell", None)
                if opp_val == self:
                    setattr(old_value, "swt_Shell", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Shell"):
                opp_val = getattr(value, "swt_Shell", None)
                setattr(value, "swt_Shell", self)

class swt_Text(Control):

    def __init__(self, multiplicityStyle: str, text: str, selection: str, editable: bool, echoChar: str, tabs: int, textLimit: int, topIndex: int, message: str):
        self.multiplicityStyle = multiplicityStyle
        self.text = text
        self.selection = selection
        self.editable = editable
        self.echoChar = echoChar
        self.tabs = tabs
        self.textLimit = textLimit
        self.topIndex = topIndex
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def tabs(self) -> int:
        return self.__tabs

    @tabs.setter
    def tabs(self, tabs: int):
        self.__tabs = tabs

    @property
    def multiplicityStyle(self) -> str:
        return self.__multiplicityStyle

    @multiplicityStyle.setter
    def multiplicityStyle(self, multiplicityStyle: str):
        self.__multiplicityStyle = multiplicityStyle

    @property
    def textLimit(self) -> int:
        return self.__textLimit

    @textLimit.setter
    def textLimit(self, textLimit: int):
        self.__textLimit = textLimit

    @property
    def topIndex(self) -> int:
        return self.__topIndex

    @topIndex.setter
    def topIndex(self, topIndex: int):
        self.__topIndex = topIndex

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def editable(self) -> bool:
        return self.__editable

    @editable.setter
    def editable(self, editable: bool):
        self.__editable = editable

    @property
    def echoChar(self) -> str:
        return self.__echoChar

    @echoChar.setter
    def echoChar(self, echoChar: str):
        self.__echoChar = echoChar

class swt_Tree(Control):

    def __init__(self, headerVisible: bool, linesVisible: bool, sortDirection: str, swt_Tree: set["swt_TreeColumn"] = None, swt_Tree39: "swt_TreeColumn" = None, swt_Tree42: "swt_TreeViewer" = None):
        self.headerVisible = headerVisible
        self.linesVisible = linesVisible
        self.sortDirection = sortDirection
        self.swt_Tree = swt_Tree if swt_Tree is not None else set()
        self.swt_Tree39 = swt_Tree39
        self.swt_Tree42 = swt_Tree42
        
    @property
    def headerVisible(self) -> bool:
        return self.__headerVisible

    @headerVisible.setter
    def headerVisible(self, headerVisible: bool):
        self.__headerVisible = headerVisible

    @property
    def sortDirection(self) -> str:
        return self.__sortDirection

    @sortDirection.setter
    def sortDirection(self, sortDirection: str):
        self.__sortDirection = sortDirection

    @property
    def linesVisible(self) -> bool:
        return self.__linesVisible

    @linesVisible.setter
    def linesVisible(self, linesVisible: bool):
        self.__linesVisible = linesVisible

    @property
    def swt_Tree(self):
        return self.__swt_Tree

    @swt_Tree.setter
    def swt_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Tree__swt_Tree", None)
        self.__swt_Tree = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swt_TreeColumn"):
                    opp_val = getattr(item, "swt_TreeColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "swt_TreeColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swt_TreeColumn"):
                    opp_val = getattr(item, "swt_TreeColumn", None)
                    
                    setattr(item, "swt_TreeColumn", self)
                    

    @property
    def swt_Tree42(self):
        return self.__swt_Tree42

    @swt_Tree42.setter
    def swt_Tree42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Tree__swt_Tree42", None)
        self.__swt_Tree42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_TreeViewer"):
                opp_val = getattr(old_value, "swt_TreeViewer", None)
                if opp_val == self:
                    setattr(old_value, "swt_TreeViewer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_TreeViewer"):
                opp_val = getattr(value, "swt_TreeViewer", None)
                setattr(value, "swt_TreeViewer", self)

    @property
    def swt_Tree39(self):
        return self.__swt_Tree39

    @swt_Tree39.setter
    def swt_Tree39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Tree__swt_Tree39", None)
        self.__swt_Tree39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_TreeColumn40"):
                opp_val = getattr(old_value, "swt_TreeColumn40", None)
                if opp_val == self:
                    setattr(old_value, "swt_TreeColumn40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_TreeColumn40"):
                opp_val = getattr(value, "swt_TreeColumn40", None)
                setattr(value, "swt_TreeColumn40", self)

class swt_TabFolder(Control):

    pass
class swt_Browser(Control):

    def __init__(self, javascriptEnabled: bool, text: str, url: str):
        self.javascriptEnabled = javascriptEnabled
        self.text = text
        self.url = url
        
    @property
    def javascriptEnabled(self) -> bool:
        return self.__javascriptEnabled

    @javascriptEnabled.setter
    def javascriptEnabled(self, javascriptEnabled: bool):
        self.__javascriptEnabled = javascriptEnabled

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class swt_IntervalControl(Control):

    def __init__(self, minimum: int, maximum: int, selection: int):
        self.minimum = minimum
        self.maximum = maximum
        self.selection = selection
        
    @property
    def maximum(self) -> int:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: int):
        self.__maximum = maximum

    @property
    def minimum(self) -> int:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: int):
        self.__minimum = minimum

    @property
    def selection(self) -> int:
        return self.__selection

    @selection.setter
    def selection(self, selection: int):
        self.__selection = selection

class swt_Label(Labeled, Control):

    pass
class swt_DateTime(Control):

    def __init__(self, seconds: int, minutes: int, hours: int, day: int, month: int, year: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self.day = day
        self.month = month
        self.year = year
        
    @property
    def hours(self) -> int:
        return self.__hours

    @hours.setter
    def hours(self, hours: int):
        self.__hours = hours

    @property
    def minutes(self) -> int:
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: int):
        self.__minutes = minutes

    @property
    def month(self) -> int:
        return self.__month

    @month.setter
    def month(self, month: int):
        self.__month = month

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def seconds(self) -> int:
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds: int):
        self.__seconds = seconds

    @property
    def day(self) -> int:
        return self.__day

    @day.setter
    def day(self, day: int):
        self.__day = day

class swt_ToolBar(Control):

    def __init__(self, orientationStyle: str, parent12: set["swt_ToolItem"] = None, ToolBar: "swt_ToolItem" = None):
        self.orientationStyle = orientationStyle
        self.parent12 = parent12 if parent12 is not None else set()
        self.ToolBar = ToolBar
        
    @property
    def orientationStyle(self) -> str:
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle

    @property
    def parent12(self):
        return self.__parent12

    @parent12.setter
    def parent12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_ToolBar__parent12", None)
        self.__parent12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ToolItem"):
                    opp_val = getattr(item, "ToolItem", None)
                    
                    if opp_val == self:
                        setattr(item, "ToolItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ToolItem"):
                    opp_val = getattr(item, "ToolItem", None)
                    
                    setattr(item, "ToolItem", self)
                    

    @property
    def ToolBar(self):
        return self.__ToolBar

    @ToolBar.setter
    def ToolBar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_ToolBar__ToolBar", None)
        self.__ToolBar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items"):
                opp_val = getattr(old_value, "items", None)
                if opp_val == self:
                    setattr(old_value, "items", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items"):
                opp_val = getattr(value, "items", None)
                setattr(value, "items", self)

class swt_AbstractComposite(Control):

    pass
class swt_Font:

    def __init__(self, name: str, style: int, height: int, swt_Font: "swt_Control" = None):
        self.name = name
        self.style = style
        self.height = height
        self.swt_Font = swt_Font
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def style(self) -> int:
        return self.__style

    @style.setter
    def style(self, style: int):
        self.__style = style

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def swt_Font(self):
        return self.__swt_Font

    @swt_Font.setter
    def swt_Font(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Font__swt_Font", None)
        self.__swt_Font = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Control4"):
                opp_val = getattr(old_value, "swt_Control4", None)
                if opp_val == self:
                    setattr(old_value, "swt_Control4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Control4"):
                opp_val = getattr(value, "swt_Control4", None)
                setattr(value, "swt_Control4", self)

class swt_Color(ABC):

    pass
class Widget:

    pass
class swt_AbstractMenu(Widget):

    def __init__(self, textOrientationStyle: str, enabled: bool, visible: bool, swt_AbstractMenu: set["swt_MenuItem"] = None):
        self.textOrientationStyle = textOrientationStyle
        self.enabled = enabled
        self.visible = visible
        self.swt_AbstractMenu = swt_AbstractMenu if swt_AbstractMenu is not None else set()
        
    @property
    def textOrientationStyle(self) -> str:
        return self.__textOrientationStyle

    @textOrientationStyle.setter
    def textOrientationStyle(self, textOrientationStyle: str):
        self.__textOrientationStyle = textOrientationStyle

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def swt_AbstractMenu(self):
        return self.__swt_AbstractMenu

    @swt_AbstractMenu.setter
    def swt_AbstractMenu(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_AbstractMenu__swt_AbstractMenu", None)
        self.__swt_AbstractMenu = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swt_MenuItem"):
                    opp_val = getattr(item, "swt_MenuItem", None)
                    
                    if opp_val == self:
                        setattr(item, "swt_MenuItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swt_MenuItem"):
                    opp_val = getattr(item, "swt_MenuItem", None)
                    
                    setattr(item, "swt_MenuItem", self)
                    

class swt_Item(Labeled, Widget):

    pass
class swt_Control(Widget):

    def __init__(self, borderStyle: str, textOrientationStyle: str, enabled: bool, visible: bool, touchEnabled: bool, toolTipText: str, size: str, swt_Control: "swt_LayoutData" = None, swt_Control2: "swt_Color" = None, swt_Control4: "swt_Font" = None, swt_Control19: "swt_CoolItem" = None, swt_Control23: "swt_TabItem" = None, swt_Control36: "swt_FormAttachment" = None):
        self.borderStyle = borderStyle
        self.textOrientationStyle = textOrientationStyle
        self.enabled = enabled
        self.visible = visible
        self.touchEnabled = touchEnabled
        self.toolTipText = toolTipText
        self.size = size
        self.swt_Control = swt_Control
        self.swt_Control2 = swt_Control2
        self.swt_Control4 = swt_Control4
        self.swt_Control19 = swt_Control19
        self.swt_Control23 = swt_Control23
        self.swt_Control36 = swt_Control36
        
    @property
    def toolTipText(self) -> str:
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText

    @property
    def borderStyle(self) -> str:
        return self.__borderStyle

    @borderStyle.setter
    def borderStyle(self, borderStyle: str):
        self.__borderStyle = borderStyle

    @property
    def touchEnabled(self) -> bool:
        return self.__touchEnabled

    @touchEnabled.setter
    def touchEnabled(self, touchEnabled: bool):
        self.__touchEnabled = touchEnabled

    @property
    def textOrientationStyle(self) -> str:
        return self.__textOrientationStyle

    @textOrientationStyle.setter
    def textOrientationStyle(self, textOrientationStyle: str):
        self.__textOrientationStyle = textOrientationStyle

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def swt_Control19(self):
        return self.__swt_Control19

    @swt_Control19.setter
    def swt_Control19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control19", None)
        self.__swt_Control19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_CoolItem"):
                opp_val = getattr(old_value, "swt_CoolItem", None)
                if opp_val == self:
                    setattr(old_value, "swt_CoolItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_CoolItem"):
                opp_val = getattr(value, "swt_CoolItem", None)
                setattr(value, "swt_CoolItem", self)

    @property
    def swt_Control36(self):
        return self.__swt_Control36

    @swt_Control36.setter
    def swt_Control36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control36", None)
        self.__swt_Control36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormAttachment35"):
                opp_val = getattr(old_value, "swt_FormAttachment35", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormAttachment35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormAttachment35"):
                opp_val = getattr(value, "swt_FormAttachment35", None)
                setattr(value, "swt_FormAttachment35", self)

    @property
    def swt_Control2(self):
        return self.__swt_Control2

    @swt_Control2.setter
    def swt_Control2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control2", None)
        self.__swt_Control2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Color"):
                opp_val = getattr(old_value, "swt_Color", None)
                if opp_val == self:
                    setattr(old_value, "swt_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Color"):
                opp_val = getattr(value, "swt_Color", None)
                setattr(value, "swt_Color", self)

    @property
    def swt_Control4(self):
        return self.__swt_Control4

    @swt_Control4.setter
    def swt_Control4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control4", None)
        self.__swt_Control4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Font"):
                opp_val = getattr(old_value, "swt_Font", None)
                if opp_val == self:
                    setattr(old_value, "swt_Font", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Font"):
                opp_val = getattr(value, "swt_Font", None)
                setattr(value, "swt_Font", self)

    @property
    def swt_Control(self):
        return self.__swt_Control

    @swt_Control.setter
    def swt_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control", None)
        self.__swt_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_LayoutData"):
                opp_val = getattr(old_value, "swt_LayoutData", None)
                if opp_val == self:
                    setattr(old_value, "swt_LayoutData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_LayoutData"):
                opp_val = getattr(value, "swt_LayoutData", None)
                setattr(value, "swt_LayoutData", self)

    @property
    def swt_Control23(self):
        return self.__swt_Control23

    @swt_Control23.setter
    def swt_Control23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control23", None)
        self.__swt_Control23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_TabItem22"):
                opp_val = getattr(old_value, "swt_TabItem22", None)
                if opp_val == self:
                    setattr(old_value, "swt_TabItem22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_TabItem22"):
                opp_val = getattr(value, "swt_TabItem22", None)
                setattr(value, "swt_TabItem22", self)

class swt_LayoutData(ABC):

    pass
class swt_Widget(ABC):

    def __init__(self, style: int):
        self.style = style
        
    @property
    def style(self) -> int:
        return self.__style

    @style.setter
    def style(self, style: int):
        self.__style = style
