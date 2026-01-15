from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Trace_BaseLine(Enum):
    NEGATIVE_INFINITY = "NEGATIVE_INFINITY"
    ZERO = "ZERO"
    POSITIVE_INFINITY = "POSITIVE_INFINITY"
class LinearScale_Orientation(Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
class Trace_PointStyle(Enum):
    NONE = "NONE"
    POINT = "POINT"
    CIRCLE = "CIRCLE"
    TRIANGLE = "TRIANGLE"
    FILLED_TRIANGLE = "FILLED_TRIANGLE"
    SQUARE = "SQUARE"
    FILLED_SQUARE = "FILLED_SQUARE"
    DIAMOND = "DIAMOND"
    FILLED_DIAMOND = "FILLED_DIAMOND"
    XCROSS = "XCROSS"
    CROSS = "CROSS"
    BAR = "BAR"
class Trace_ErrorBarType(Enum):
    NONE = "NONE"
    PLUS = "PLUS"
    MINUS = "MINUS"
    BOTH = "BOTH"
class Trace_TraceType(Enum):
    DOT_LINE = "DOT_LINE"
    SOLID_LINE = "SOLID_LINE"
    DASH_LINE = "DASH_LINE"
    POINT = "POINT"
    BAR = "BAR"
    AREA = "AREA"
    LINE_AREA = "LINE_AREA"
    STEP_VERTICALLY = "STEP_VERTICALLY"
    STEP_HORIZONTALLY = "STEP_HORIZONTALLY"
    DASHDOT_LINE = "DASHDOT_LINE"
    DASHDOTDOT_LINE = "DASHDOTDOT_LINE"
class ZoomType(Enum):
    NONE = "NONE"
    RUBBERBAND_ZOOM = "RUBBERBAND_ZOOM"
    DYNAMIC_ZOOM = "DYNAMIC_ZOOM"
    HORIZONTAL_ZOOM = "HORIZONTAL_ZOOM"
    VERTICAL_ZOOM = "VERTICAL_ZOOM"
    ZOOM_IN = "ZOOM_IN"
    ZOOM_OUT = "ZOOM_OUT"
    ZOOM_IN_HORIZONTALLY = "ZOOM_IN_HORIZONTALLY"
    ZOOM_OUT_HORIZONTALLY = "ZOOM_OUT_HORIZONTALLY"
    ZOOM_IN_VERTICALLY = "ZOOM_IN_VERTICALLY"
    ZOOM_OUT_VERTICALLY = "ZOOM_OUT_VERTICALLY"
    PANNING = "PANNING"


############################################
# Definition of Classes
############################################

class xygraph_FontDescriptor:

    def __init__(self, name: str, size: int, style: int, xygraph_FontDescriptor: "xygraph_XYGraphDescriptor" = None, xygraph_FontDescriptor32: "xygraph_AxisDescriptor" = None, xygraph_FontDescriptor35: "xygraph_AxisDescriptor" = None):
        self.name = name
        self.size = size
        self.style = style
        self.xygraph_FontDescriptor = xygraph_FontDescriptor
        self.xygraph_FontDescriptor32 = xygraph_FontDescriptor32
        self.xygraph_FontDescriptor35 = xygraph_FontDescriptor35
        
    @property
    def style(self) -> int:
        return self.__style

    @style.setter
    def style(self, style: int):
        self.__style = style

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
    def xygraph_FontDescriptor(self):
        return self.__xygraph_FontDescriptor

    @xygraph_FontDescriptor.setter
    def xygraph_FontDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_FontDescriptor__xygraph_FontDescriptor", None)
        self.__xygraph_FontDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_XYGraphDescriptor9"):
                opp_val = getattr(old_value, "xygraph_XYGraphDescriptor9", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_XYGraphDescriptor9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_XYGraphDescriptor9"):
                opp_val = getattr(value, "xygraph_XYGraphDescriptor9", None)
                setattr(value, "xygraph_XYGraphDescriptor9", self)

    @property
    def xygraph_FontDescriptor35(self):
        return self.__xygraph_FontDescriptor35

    @xygraph_FontDescriptor35.setter
    def xygraph_FontDescriptor35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_FontDescriptor__xygraph_FontDescriptor35", None)
        self.__xygraph_FontDescriptor35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_AxisDescriptor34"):
                opp_val = getattr(old_value, "xygraph_AxisDescriptor34", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_AxisDescriptor34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_AxisDescriptor34"):
                opp_val = getattr(value, "xygraph_AxisDescriptor34", None)
                setattr(value, "xygraph_AxisDescriptor34", self)

    @property
    def xygraph_FontDescriptor32(self):
        return self.__xygraph_FontDescriptor32

    @xygraph_FontDescriptor32.setter
    def xygraph_FontDescriptor32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_FontDescriptor__xygraph_FontDescriptor32", None)
        self.__xygraph_FontDescriptor32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_AxisDescriptor31"):
                opp_val = getattr(old_value, "xygraph_AxisDescriptor31", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_AxisDescriptor31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_AxisDescriptor31"):
                opp_val = getattr(value, "xygraph_AxisDescriptor31", None)
                setattr(value, "xygraph_AxisDescriptor31", self)

class xygraph_TraceDescriptor:

    def __init__(self, baseLine: str, drawYErrorInArea: bool, errorBarCapWidth: int, errorBarEnabled: bool, lineWidth: int, name: str, pointSize: int, pointStyle: str, antiAliasing: bool, areaAlpha: int, traceType: str, xErrorBarType: str, yErrorBarType: str, xygraph_TraceDescriptor17: "xygraph_XYGraphDescriptor" = None, xygraph_TraceDescriptor: "xygraph_XYGraphDescriptor" = None, xygraph_TraceDescriptor37: "xygraph_ColorDescriptor" = None, xygraph_TraceDescriptor40: "xygraph_ColorDescriptor" = None, xygraph_TraceDescriptor43: "xygraph_AxisDescriptor" = None, xygraph_TraceDescriptor46: "xygraph_AxisDescriptor" = None, xygraph_TraceDescriptor49: "xygraph_EObject" = None):
        self.baseLine = baseLine
        self.drawYErrorInArea = drawYErrorInArea
        self.errorBarCapWidth = errorBarCapWidth
        self.errorBarEnabled = errorBarEnabled
        self.lineWidth = lineWidth
        self.name = name
        self.pointSize = pointSize
        self.pointStyle = pointStyle
        self.antiAliasing = antiAliasing
        self.areaAlpha = areaAlpha
        self.traceType = traceType
        self.xErrorBarType = xErrorBarType
        self.yErrorBarType = yErrorBarType
        self.xygraph_TraceDescriptor17 = xygraph_TraceDescriptor17
        self.xygraph_TraceDescriptor = xygraph_TraceDescriptor
        self.xygraph_TraceDescriptor37 = xygraph_TraceDescriptor37
        self.xygraph_TraceDescriptor40 = xygraph_TraceDescriptor40
        self.xygraph_TraceDescriptor43 = xygraph_TraceDescriptor43
        self.xygraph_TraceDescriptor46 = xygraph_TraceDescriptor46
        self.xygraph_TraceDescriptor49 = xygraph_TraceDescriptor49
        
    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

    @property
    def traceType(self) -> str:
        return self.__traceType

    @traceType.setter
    def traceType(self, traceType: str):
        self.__traceType = traceType

    @property
    def drawYErrorInArea(self) -> bool:
        return self.__drawYErrorInArea

    @drawYErrorInArea.setter
    def drawYErrorInArea(self, drawYErrorInArea: bool):
        self.__drawYErrorInArea = drawYErrorInArea

    @property
    def antiAliasing(self) -> bool:
        return self.__antiAliasing

    @antiAliasing.setter
    def antiAliasing(self, antiAliasing: bool):
        self.__antiAliasing = antiAliasing

    @property
    def errorBarEnabled(self) -> bool:
        return self.__errorBarEnabled

    @errorBarEnabled.setter
    def errorBarEnabled(self, errorBarEnabled: bool):
        self.__errorBarEnabled = errorBarEnabled

    @property
    def baseLine(self) -> str:
        return self.__baseLine

    @baseLine.setter
    def baseLine(self, baseLine: str):
        self.__baseLine = baseLine

    @property
    def errorBarCapWidth(self) -> int:
        return self.__errorBarCapWidth

    @errorBarCapWidth.setter
    def errorBarCapWidth(self, errorBarCapWidth: int):
        self.__errorBarCapWidth = errorBarCapWidth

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def yErrorBarType(self) -> str:
        return self.__yErrorBarType

    @yErrorBarType.setter
    def yErrorBarType(self, yErrorBarType: str):
        self.__yErrorBarType = yErrorBarType

    @property
    def areaAlpha(self) -> int:
        return self.__areaAlpha

    @areaAlpha.setter
    def areaAlpha(self, areaAlpha: int):
        self.__areaAlpha = areaAlpha

    @property
    def xErrorBarType(self) -> str:
        return self.__xErrorBarType

    @xErrorBarType.setter
    def xErrorBarType(self, xErrorBarType: str):
        self.__xErrorBarType = xErrorBarType

    @property
    def pointStyle(self) -> str:
        return self.__pointStyle

    @pointStyle.setter
    def pointStyle(self, pointStyle: str):
        self.__pointStyle = pointStyle

    @property
    def pointSize(self) -> int:
        return self.__pointSize

    @pointSize.setter
    def pointSize(self, pointSize: int):
        self.__pointSize = pointSize

    @property
    def xygraph_TraceDescriptor37(self):
        return self.__xygraph_TraceDescriptor37

    @xygraph_TraceDescriptor37.setter
    def xygraph_TraceDescriptor37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_TraceDescriptor__xygraph_TraceDescriptor37", None)
        self.__xygraph_TraceDescriptor37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_ColorDescriptor38"):
                opp_val = getattr(old_value, "xygraph_ColorDescriptor38", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_ColorDescriptor38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_ColorDescriptor38"):
                opp_val = getattr(value, "xygraph_ColorDescriptor38", None)
                setattr(value, "xygraph_ColorDescriptor38", self)

    @property
    def xygraph_TraceDescriptor(self):
        return self.__xygraph_TraceDescriptor

    @xygraph_TraceDescriptor.setter
    def xygraph_TraceDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_TraceDescriptor__xygraph_TraceDescriptor", None)
        self.__xygraph_TraceDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_XYGraphDescriptor4"):
                opp_val = getattr(old_value, "xygraph_XYGraphDescriptor4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_XYGraphDescriptor4"):
                opp_val = getattr(value, "xygraph_XYGraphDescriptor4", None)
                if opp_val is None:
                    setattr(value, "xygraph_XYGraphDescriptor4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xygraph_TraceDescriptor17(self):
        return self.__xygraph_TraceDescriptor17

    @xygraph_TraceDescriptor17.setter
    def xygraph_TraceDescriptor17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_TraceDescriptor__xygraph_TraceDescriptor17", None)
        self.__xygraph_TraceDescriptor17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_XYGraphDescriptor16"):
                opp_val = getattr(old_value, "xygraph_XYGraphDescriptor16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_XYGraphDescriptor16"):
                opp_val = getattr(value, "xygraph_XYGraphDescriptor16", None)
                if opp_val is None:
                    setattr(value, "xygraph_XYGraphDescriptor16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xygraph_TraceDescriptor43(self):
        return self.__xygraph_TraceDescriptor43

    @xygraph_TraceDescriptor43.setter
    def xygraph_TraceDescriptor43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_TraceDescriptor__xygraph_TraceDescriptor43", None)
        self.__xygraph_TraceDescriptor43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_AxisDescriptor44"):
                opp_val = getattr(old_value, "xygraph_AxisDescriptor44", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_AxisDescriptor44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_AxisDescriptor44"):
                opp_val = getattr(value, "xygraph_AxisDescriptor44", None)
                setattr(value, "xygraph_AxisDescriptor44", self)

    @property
    def xygraph_TraceDescriptor40(self):
        return self.__xygraph_TraceDescriptor40

    @xygraph_TraceDescriptor40.setter
    def xygraph_TraceDescriptor40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_TraceDescriptor__xygraph_TraceDescriptor40", None)
        self.__xygraph_TraceDescriptor40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_ColorDescriptor41"):
                opp_val = getattr(old_value, "xygraph_ColorDescriptor41", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_ColorDescriptor41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_ColorDescriptor41"):
                opp_val = getattr(value, "xygraph_ColorDescriptor41", None)
                setattr(value, "xygraph_ColorDescriptor41", self)

    @property
    def xygraph_TraceDescriptor49(self):
        return self.__xygraph_TraceDescriptor49

    @xygraph_TraceDescriptor49.setter
    def xygraph_TraceDescriptor49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_TraceDescriptor__xygraph_TraceDescriptor49", None)
        self.__xygraph_TraceDescriptor49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_EObject50"):
                opp_val = getattr(old_value, "xygraph_EObject50", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_EObject50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_EObject50"):
                opp_val = getattr(value, "xygraph_EObject50", None)
                setattr(value, "xygraph_EObject50", self)

    @property
    def xygraph_TraceDescriptor46(self):
        return self.__xygraph_TraceDescriptor46

    @xygraph_TraceDescriptor46.setter
    def xygraph_TraceDescriptor46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_TraceDescriptor__xygraph_TraceDescriptor46", None)
        self.__xygraph_TraceDescriptor46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_AxisDescriptor47"):
                opp_val = getattr(old_value, "xygraph_AxisDescriptor47", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_AxisDescriptor47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_AxisDescriptor47"):
                opp_val = getattr(value, "xygraph_AxisDescriptor47", None)
                setattr(value, "xygraph_AxisDescriptor47", self)

class xygraph_AxisDescriptor:

    def __init__(self, orientation: str, autoScale: bool, minorTicksVisible: bool, primarySide: bool, rangeLower: float, rangeUpper: float, showMajorGrid: bool, showMinorGrid: bool, title: str, zoomType: str, autoScaleThreshold: float, dashGridLine: bool, logScale: bool, autoFormat: bool, dateEnabled: bool, formatPattern: str, xygraph_AxisDescriptor: "xygraph_XYGraphDescriptor" = None, xygraph_AxisDescriptor28: "xygraph_ColorDescriptor" = None, xygraph_AxisDescriptor19: "xygraph_ColorDescriptor" = None, xygraph_AxisDescriptor22: "xygraph_ColorDescriptor" = None, xygraph_AxisDescriptor25: "xygraph_ColorDescriptor" = None, xygraph_AxisDescriptor31: "xygraph_FontDescriptor" = None, xygraph_AxisDescriptor34: "xygraph_FontDescriptor" = None, xygraph_AxisDescriptor44: "xygraph_TraceDescriptor" = None, xygraph_AxisDescriptor47: "xygraph_TraceDescriptor" = None):
        self.orientation = orientation
        self.autoScale = autoScale
        self.minorTicksVisible = minorTicksVisible
        self.primarySide = primarySide
        self.rangeLower = rangeLower
        self.rangeUpper = rangeUpper
        self.showMajorGrid = showMajorGrid
        self.showMinorGrid = showMinorGrid
        self.title = title
        self.zoomType = zoomType
        self.autoScaleThreshold = autoScaleThreshold
        self.dashGridLine = dashGridLine
        self.logScale = logScale
        self.autoFormat = autoFormat
        self.dateEnabled = dateEnabled
        self.formatPattern = formatPattern
        self.xygraph_AxisDescriptor = xygraph_AxisDescriptor
        self.xygraph_AxisDescriptor28 = xygraph_AxisDescriptor28
        self.xygraph_AxisDescriptor19 = xygraph_AxisDescriptor19
        self.xygraph_AxisDescriptor22 = xygraph_AxisDescriptor22
        self.xygraph_AxisDescriptor25 = xygraph_AxisDescriptor25
        self.xygraph_AxisDescriptor31 = xygraph_AxisDescriptor31
        self.xygraph_AxisDescriptor34 = xygraph_AxisDescriptor34
        self.xygraph_AxisDescriptor44 = xygraph_AxisDescriptor44
        self.xygraph_AxisDescriptor47 = xygraph_AxisDescriptor47
        
    @property
    def formatPattern(self) -> str:
        return self.__formatPattern

    @formatPattern.setter
    def formatPattern(self, formatPattern: str):
        self.__formatPattern = formatPattern

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def autoScale(self) -> bool:
        return self.__autoScale

    @autoScale.setter
    def autoScale(self, autoScale: bool):
        self.__autoScale = autoScale

    @property
    def autoScaleThreshold(self) -> float:
        return self.__autoScaleThreshold

    @autoScaleThreshold.setter
    def autoScaleThreshold(self, autoScaleThreshold: float):
        self.__autoScaleThreshold = autoScaleThreshold

    @property
    def rangeLower(self) -> float:
        return self.__rangeLower

    @rangeLower.setter
    def rangeLower(self, rangeLower: float):
        self.__rangeLower = rangeLower

    @property
    def zoomType(self) -> str:
        return self.__zoomType

    @zoomType.setter
    def zoomType(self, zoomType: str):
        self.__zoomType = zoomType

    @property
    def logScale(self) -> bool:
        return self.__logScale

    @logScale.setter
    def logScale(self, logScale: bool):
        self.__logScale = logScale

    @property
    def showMajorGrid(self) -> bool:
        return self.__showMajorGrid

    @showMajorGrid.setter
    def showMajorGrid(self, showMajorGrid: bool):
        self.__showMajorGrid = showMajorGrid

    @property
    def showMinorGrid(self) -> bool:
        return self.__showMinorGrid

    @showMinorGrid.setter
    def showMinorGrid(self, showMinorGrid: bool):
        self.__showMinorGrid = showMinorGrid

    @property
    def primarySide(self) -> bool:
        return self.__primarySide

    @primarySide.setter
    def primarySide(self, primarySide: bool):
        self.__primarySide = primarySide

    @property
    def rangeUpper(self) -> float:
        return self.__rangeUpper

    @rangeUpper.setter
    def rangeUpper(self, rangeUpper: float):
        self.__rangeUpper = rangeUpper

    @property
    def dashGridLine(self) -> bool:
        return self.__dashGridLine

    @dashGridLine.setter
    def dashGridLine(self, dashGridLine: bool):
        self.__dashGridLine = dashGridLine

    @property
    def dateEnabled(self) -> bool:
        return self.__dateEnabled

    @dateEnabled.setter
    def dateEnabled(self, dateEnabled: bool):
        self.__dateEnabled = dateEnabled

    @property
    def minorTicksVisible(self) -> bool:
        return self.__minorTicksVisible

    @minorTicksVisible.setter
    def minorTicksVisible(self, minorTicksVisible: bool):
        self.__minorTicksVisible = minorTicksVisible

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def autoFormat(self) -> bool:
        return self.__autoFormat

    @autoFormat.setter
    def autoFormat(self, autoFormat: bool):
        self.__autoFormat = autoFormat

    @property
    def xygraph_AxisDescriptor34(self):
        return self.__xygraph_AxisDescriptor34

    @xygraph_AxisDescriptor34.setter
    def xygraph_AxisDescriptor34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_AxisDescriptor__xygraph_AxisDescriptor34", None)
        self.__xygraph_AxisDescriptor34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_FontDescriptor35"):
                opp_val = getattr(old_value, "xygraph_FontDescriptor35", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_FontDescriptor35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_FontDescriptor35"):
                opp_val = getattr(value, "xygraph_FontDescriptor35", None)
                setattr(value, "xygraph_FontDescriptor35", self)

    @property
    def xygraph_AxisDescriptor44(self):
        return self.__xygraph_AxisDescriptor44

    @xygraph_AxisDescriptor44.setter
    def xygraph_AxisDescriptor44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_AxisDescriptor__xygraph_AxisDescriptor44", None)
        self.__xygraph_AxisDescriptor44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_TraceDescriptor43"):
                opp_val = getattr(old_value, "xygraph_TraceDescriptor43", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_TraceDescriptor43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_TraceDescriptor43"):
                opp_val = getattr(value, "xygraph_TraceDescriptor43", None)
                setattr(value, "xygraph_TraceDescriptor43", self)

    @property
    def xygraph_AxisDescriptor25(self):
        return self.__xygraph_AxisDescriptor25

    @xygraph_AxisDescriptor25.setter
    def xygraph_AxisDescriptor25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_AxisDescriptor__xygraph_AxisDescriptor25", None)
        self.__xygraph_AxisDescriptor25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_ColorDescriptor26"):
                opp_val = getattr(old_value, "xygraph_ColorDescriptor26", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_ColorDescriptor26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_ColorDescriptor26"):
                opp_val = getattr(value, "xygraph_ColorDescriptor26", None)
                setattr(value, "xygraph_ColorDescriptor26", self)

    @property
    def xygraph_AxisDescriptor(self):
        return self.__xygraph_AxisDescriptor

    @xygraph_AxisDescriptor.setter
    def xygraph_AxisDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_AxisDescriptor__xygraph_AxisDescriptor", None)
        self.__xygraph_AxisDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_XYGraphDescriptor2"):
                opp_val = getattr(old_value, "xygraph_XYGraphDescriptor2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_XYGraphDescriptor2"):
                opp_val = getattr(value, "xygraph_XYGraphDescriptor2", None)
                if opp_val is None:
                    setattr(value, "xygraph_XYGraphDescriptor2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xygraph_AxisDescriptor19(self):
        return self.__xygraph_AxisDescriptor19

    @xygraph_AxisDescriptor19.setter
    def xygraph_AxisDescriptor19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_AxisDescriptor__xygraph_AxisDescriptor19", None)
        self.__xygraph_AxisDescriptor19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_ColorDescriptor20"):
                opp_val = getattr(old_value, "xygraph_ColorDescriptor20", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_ColorDescriptor20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_ColorDescriptor20"):
                opp_val = getattr(value, "xygraph_ColorDescriptor20", None)
                setattr(value, "xygraph_ColorDescriptor20", self)

    @property
    def xygraph_AxisDescriptor22(self):
        return self.__xygraph_AxisDescriptor22

    @xygraph_AxisDescriptor22.setter
    def xygraph_AxisDescriptor22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_AxisDescriptor__xygraph_AxisDescriptor22", None)
        self.__xygraph_AxisDescriptor22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_ColorDescriptor23"):
                opp_val = getattr(old_value, "xygraph_ColorDescriptor23", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_ColorDescriptor23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_ColorDescriptor23"):
                opp_val = getattr(value, "xygraph_ColorDescriptor23", None)
                setattr(value, "xygraph_ColorDescriptor23", self)

    @property
    def xygraph_AxisDescriptor28(self):
        return self.__xygraph_AxisDescriptor28

    @xygraph_AxisDescriptor28.setter
    def xygraph_AxisDescriptor28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_AxisDescriptor__xygraph_AxisDescriptor28", None)
        self.__xygraph_AxisDescriptor28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_ColorDescriptor29"):
                opp_val = getattr(old_value, "xygraph_ColorDescriptor29", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_ColorDescriptor29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_ColorDescriptor29"):
                opp_val = getattr(value, "xygraph_ColorDescriptor29", None)
                setattr(value, "xygraph_ColorDescriptor29", self)

    @property
    def xygraph_AxisDescriptor31(self):
        return self.__xygraph_AxisDescriptor31

    @xygraph_AxisDescriptor31.setter
    def xygraph_AxisDescriptor31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_AxisDescriptor__xygraph_AxisDescriptor31", None)
        self.__xygraph_AxisDescriptor31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_FontDescriptor32"):
                opp_val = getattr(old_value, "xygraph_FontDescriptor32", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_FontDescriptor32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_FontDescriptor32"):
                opp_val = getattr(value, "xygraph_FontDescriptor32", None)
                setattr(value, "xygraph_FontDescriptor32", self)

    @property
    def xygraph_AxisDescriptor47(self):
        return self.__xygraph_AxisDescriptor47

    @xygraph_AxisDescriptor47.setter
    def xygraph_AxisDescriptor47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_AxisDescriptor__xygraph_AxisDescriptor47", None)
        self.__xygraph_AxisDescriptor47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_TraceDescriptor46"):
                opp_val = getattr(old_value, "xygraph_TraceDescriptor46", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_TraceDescriptor46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_TraceDescriptor46"):
                opp_val = getattr(value, "xygraph_TraceDescriptor46", None)
                setattr(value, "xygraph_TraceDescriptor46", self)

class xygraph_EObject:

    pass
class xygraph_ColorDescriptor:

    def __init__(self, r: int, g: int, b: int, xygraph_ColorDescriptor: "xygraph_XYGraphDescriptor" = None, xygraph_ColorDescriptor7: "xygraph_XYGraphDescriptor" = None, xygraph_ColorDescriptor29: "xygraph_AxisDescriptor" = None, xygraph_ColorDescriptor20: "xygraph_AxisDescriptor" = None, xygraph_ColorDescriptor23: "xygraph_AxisDescriptor" = None, xygraph_ColorDescriptor26: "xygraph_AxisDescriptor" = None, xygraph_ColorDescriptor38: "xygraph_TraceDescriptor" = None, xygraph_ColorDescriptor41: "xygraph_TraceDescriptor" = None):
        self.r = r
        self.g = g
        self.b = b
        self.xygraph_ColorDescriptor = xygraph_ColorDescriptor
        self.xygraph_ColorDescriptor7 = xygraph_ColorDescriptor7
        self.xygraph_ColorDescriptor29 = xygraph_ColorDescriptor29
        self.xygraph_ColorDescriptor20 = xygraph_ColorDescriptor20
        self.xygraph_ColorDescriptor23 = xygraph_ColorDescriptor23
        self.xygraph_ColorDescriptor26 = xygraph_ColorDescriptor26
        self.xygraph_ColorDescriptor38 = xygraph_ColorDescriptor38
        self.xygraph_ColorDescriptor41 = xygraph_ColorDescriptor41
        
    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def g(self) -> int:
        return self.__g

    @g.setter
    def g(self, g: int):
        self.__g = g

    @property
    def r(self) -> int:
        return self.__r

    @r.setter
    def r(self, r: int):
        self.__r = r

    @property
    def xygraph_ColorDescriptor23(self):
        return self.__xygraph_ColorDescriptor23

    @xygraph_ColorDescriptor23.setter
    def xygraph_ColorDescriptor23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_ColorDescriptor__xygraph_ColorDescriptor23", None)
        self.__xygraph_ColorDescriptor23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_AxisDescriptor22"):
                opp_val = getattr(old_value, "xygraph_AxisDescriptor22", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_AxisDescriptor22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_AxisDescriptor22"):
                opp_val = getattr(value, "xygraph_AxisDescriptor22", None)
                setattr(value, "xygraph_AxisDescriptor22", self)

    @property
    def xygraph_ColorDescriptor(self):
        return self.__xygraph_ColorDescriptor

    @xygraph_ColorDescriptor.setter
    def xygraph_ColorDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_ColorDescriptor__xygraph_ColorDescriptor", None)
        self.__xygraph_ColorDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_XYGraphDescriptor"):
                opp_val = getattr(old_value, "xygraph_XYGraphDescriptor", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_XYGraphDescriptor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_XYGraphDescriptor"):
                opp_val = getattr(value, "xygraph_XYGraphDescriptor", None)
                setattr(value, "xygraph_XYGraphDescriptor", self)

    @property
    def xygraph_ColorDescriptor20(self):
        return self.__xygraph_ColorDescriptor20

    @xygraph_ColorDescriptor20.setter
    def xygraph_ColorDescriptor20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_ColorDescriptor__xygraph_ColorDescriptor20", None)
        self.__xygraph_ColorDescriptor20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_AxisDescriptor19"):
                opp_val = getattr(old_value, "xygraph_AxisDescriptor19", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_AxisDescriptor19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_AxisDescriptor19"):
                opp_val = getattr(value, "xygraph_AxisDescriptor19", None)
                setattr(value, "xygraph_AxisDescriptor19", self)

    @property
    def xygraph_ColorDescriptor26(self):
        return self.__xygraph_ColorDescriptor26

    @xygraph_ColorDescriptor26.setter
    def xygraph_ColorDescriptor26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_ColorDescriptor__xygraph_ColorDescriptor26", None)
        self.__xygraph_ColorDescriptor26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_AxisDescriptor25"):
                opp_val = getattr(old_value, "xygraph_AxisDescriptor25", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_AxisDescriptor25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_AxisDescriptor25"):
                opp_val = getattr(value, "xygraph_AxisDescriptor25", None)
                setattr(value, "xygraph_AxisDescriptor25", self)

    @property
    def xygraph_ColorDescriptor41(self):
        return self.__xygraph_ColorDescriptor41

    @xygraph_ColorDescriptor41.setter
    def xygraph_ColorDescriptor41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_ColorDescriptor__xygraph_ColorDescriptor41", None)
        self.__xygraph_ColorDescriptor41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_TraceDescriptor40"):
                opp_val = getattr(old_value, "xygraph_TraceDescriptor40", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_TraceDescriptor40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_TraceDescriptor40"):
                opp_val = getattr(value, "xygraph_TraceDescriptor40", None)
                setattr(value, "xygraph_TraceDescriptor40", self)

    @property
    def xygraph_ColorDescriptor7(self):
        return self.__xygraph_ColorDescriptor7

    @xygraph_ColorDescriptor7.setter
    def xygraph_ColorDescriptor7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_ColorDescriptor__xygraph_ColorDescriptor7", None)
        self.__xygraph_ColorDescriptor7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_XYGraphDescriptor6"):
                opp_val = getattr(old_value, "xygraph_XYGraphDescriptor6", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_XYGraphDescriptor6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_XYGraphDescriptor6"):
                opp_val = getattr(value, "xygraph_XYGraphDescriptor6", None)
                setattr(value, "xygraph_XYGraphDescriptor6", self)

    @property
    def xygraph_ColorDescriptor29(self):
        return self.__xygraph_ColorDescriptor29

    @xygraph_ColorDescriptor29.setter
    def xygraph_ColorDescriptor29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_ColorDescriptor__xygraph_ColorDescriptor29", None)
        self.__xygraph_ColorDescriptor29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_AxisDescriptor28"):
                opp_val = getattr(old_value, "xygraph_AxisDescriptor28", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_AxisDescriptor28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_AxisDescriptor28"):
                opp_val = getattr(value, "xygraph_AxisDescriptor28", None)
                setattr(value, "xygraph_AxisDescriptor28", self)

    @property
    def xygraph_ColorDescriptor38(self):
        return self.__xygraph_ColorDescriptor38

    @xygraph_ColorDescriptor38.setter
    def xygraph_ColorDescriptor38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_ColorDescriptor__xygraph_ColorDescriptor38", None)
        self.__xygraph_ColorDescriptor38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_TraceDescriptor37"):
                opp_val = getattr(old_value, "xygraph_TraceDescriptor37", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_TraceDescriptor37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_TraceDescriptor37"):
                opp_val = getattr(value, "xygraph_TraceDescriptor37", None)
                setattr(value, "xygraph_TraceDescriptor37", self)

class xygraph_XYGraphDescriptor:

    def __init__(self, title: str, showLegend: bool, showTitle: bool, transparent: bool, zoomType: str, showPlotAreaBorder: bool, xygraph_XYGraphDescriptor: "xygraph_ColorDescriptor" = None, xygraph_XYGraphDescriptor9: "xygraph_FontDescriptor" = None, xygraph_XYGraphDescriptor11: "xygraph_EObject" = None, xygraph_XYGraphDescriptor13: "xygraph_EObject" = None, xygraph_XYGraphDescriptor16: set["xygraph_TraceDescriptor"] = None, xygraph_XYGraphDescriptor2: set["xygraph_AxisDescriptor"] = None, xygraph_XYGraphDescriptor4: set["xygraph_TraceDescriptor"] = None, xygraph_XYGraphDescriptor6: "xygraph_ColorDescriptor" = None):
        self.title = title
        self.showLegend = showLegend
        self.showTitle = showTitle
        self.transparent = transparent
        self.zoomType = zoomType
        self.showPlotAreaBorder = showPlotAreaBorder
        self.xygraph_XYGraphDescriptor = xygraph_XYGraphDescriptor
        self.xygraph_XYGraphDescriptor9 = xygraph_XYGraphDescriptor9
        self.xygraph_XYGraphDescriptor11 = xygraph_XYGraphDescriptor11
        self.xygraph_XYGraphDescriptor13 = xygraph_XYGraphDescriptor13
        self.xygraph_XYGraphDescriptor16 = xygraph_XYGraphDescriptor16 if xygraph_XYGraphDescriptor16 is not None else set()
        self.xygraph_XYGraphDescriptor2 = xygraph_XYGraphDescriptor2 if xygraph_XYGraphDescriptor2 is not None else set()
        self.xygraph_XYGraphDescriptor4 = xygraph_XYGraphDescriptor4 if xygraph_XYGraphDescriptor4 is not None else set()
        self.xygraph_XYGraphDescriptor6 = xygraph_XYGraphDescriptor6
        
    @property
    def zoomType(self) -> str:
        return self.__zoomType

    @zoomType.setter
    def zoomType(self, zoomType: str):
        self.__zoomType = zoomType

    @property
    def showPlotAreaBorder(self) -> bool:
        return self.__showPlotAreaBorder

    @showPlotAreaBorder.setter
    def showPlotAreaBorder(self, showPlotAreaBorder: bool):
        self.__showPlotAreaBorder = showPlotAreaBorder

    @property
    def showTitle(self) -> bool:
        return self.__showTitle

    @showTitle.setter
    def showTitle(self, showTitle: bool):
        self.__showTitle = showTitle

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def transparent(self) -> bool:
        return self.__transparent

    @transparent.setter
    def transparent(self, transparent: bool):
        self.__transparent = transparent

    @property
    def showLegend(self) -> bool:
        return self.__showLegend

    @showLegend.setter
    def showLegend(self, showLegend: bool):
        self.__showLegend = showLegend

    @property
    def xygraph_XYGraphDescriptor11(self):
        return self.__xygraph_XYGraphDescriptor11

    @xygraph_XYGraphDescriptor11.setter
    def xygraph_XYGraphDescriptor11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_XYGraphDescriptor__xygraph_XYGraphDescriptor11", None)
        self.__xygraph_XYGraphDescriptor11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_EObject"):
                opp_val = getattr(old_value, "xygraph_EObject", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_EObject"):
                opp_val = getattr(value, "xygraph_EObject", None)
                setattr(value, "xygraph_EObject", self)

    @property
    def xygraph_XYGraphDescriptor6(self):
        return self.__xygraph_XYGraphDescriptor6

    @xygraph_XYGraphDescriptor6.setter
    def xygraph_XYGraphDescriptor6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_XYGraphDescriptor__xygraph_XYGraphDescriptor6", None)
        self.__xygraph_XYGraphDescriptor6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_ColorDescriptor7"):
                opp_val = getattr(old_value, "xygraph_ColorDescriptor7", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_ColorDescriptor7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_ColorDescriptor7"):
                opp_val = getattr(value, "xygraph_ColorDescriptor7", None)
                setattr(value, "xygraph_ColorDescriptor7", self)

    @property
    def xygraph_XYGraphDescriptor(self):
        return self.__xygraph_XYGraphDescriptor

    @xygraph_XYGraphDescriptor.setter
    def xygraph_XYGraphDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_XYGraphDescriptor__xygraph_XYGraphDescriptor", None)
        self.__xygraph_XYGraphDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_ColorDescriptor"):
                opp_val = getattr(old_value, "xygraph_ColorDescriptor", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_ColorDescriptor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_ColorDescriptor"):
                opp_val = getattr(value, "xygraph_ColorDescriptor", None)
                setattr(value, "xygraph_ColorDescriptor", self)

    @property
    def xygraph_XYGraphDescriptor13(self):
        return self.__xygraph_XYGraphDescriptor13

    @xygraph_XYGraphDescriptor13.setter
    def xygraph_XYGraphDescriptor13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_XYGraphDescriptor__xygraph_XYGraphDescriptor13", None)
        self.__xygraph_XYGraphDescriptor13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_EObject14"):
                opp_val = getattr(old_value, "xygraph_EObject14", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_EObject14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_EObject14"):
                opp_val = getattr(value, "xygraph_EObject14", None)
                setattr(value, "xygraph_EObject14", self)

    @property
    def xygraph_XYGraphDescriptor2(self):
        return self.__xygraph_XYGraphDescriptor2

    @xygraph_XYGraphDescriptor2.setter
    def xygraph_XYGraphDescriptor2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_XYGraphDescriptor__xygraph_XYGraphDescriptor2", None)
        self.__xygraph_XYGraphDescriptor2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xygraph_AxisDescriptor"):
                    opp_val = getattr(item, "xygraph_AxisDescriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "xygraph_AxisDescriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xygraph_AxisDescriptor"):
                    opp_val = getattr(item, "xygraph_AxisDescriptor", None)
                    
                    setattr(item, "xygraph_AxisDescriptor", self)
                    

    @property
    def xygraph_XYGraphDescriptor9(self):
        return self.__xygraph_XYGraphDescriptor9

    @xygraph_XYGraphDescriptor9.setter
    def xygraph_XYGraphDescriptor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_XYGraphDescriptor__xygraph_XYGraphDescriptor9", None)
        self.__xygraph_XYGraphDescriptor9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xygraph_FontDescriptor"):
                opp_val = getattr(old_value, "xygraph_FontDescriptor", None)
                if opp_val == self:
                    setattr(old_value, "xygraph_FontDescriptor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xygraph_FontDescriptor"):
                opp_val = getattr(value, "xygraph_FontDescriptor", None)
                setattr(value, "xygraph_FontDescriptor", self)

    @property
    def xygraph_XYGraphDescriptor16(self):
        return self.__xygraph_XYGraphDescriptor16

    @xygraph_XYGraphDescriptor16.setter
    def xygraph_XYGraphDescriptor16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_XYGraphDescriptor__xygraph_XYGraphDescriptor16", None)
        self.__xygraph_XYGraphDescriptor16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xygraph_TraceDescriptor17"):
                    opp_val = getattr(item, "xygraph_TraceDescriptor17", None)
                    
                    if opp_val == self:
                        setattr(item, "xygraph_TraceDescriptor17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xygraph_TraceDescriptor17"):
                    opp_val = getattr(item, "xygraph_TraceDescriptor17", None)
                    
                    setattr(item, "xygraph_TraceDescriptor17", self)
                    

    @property
    def xygraph_XYGraphDescriptor4(self):
        return self.__xygraph_XYGraphDescriptor4

    @xygraph_XYGraphDescriptor4.setter
    def xygraph_XYGraphDescriptor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xygraph_XYGraphDescriptor__xygraph_XYGraphDescriptor4", None)
        self.__xygraph_XYGraphDescriptor4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xygraph_TraceDescriptor"):
                    opp_val = getattr(item, "xygraph_TraceDescriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "xygraph_TraceDescriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xygraph_TraceDescriptor"):
                    opp_val = getattr(item, "xygraph_TraceDescriptor", None)
                    
                    setattr(item, "xygraph_TraceDescriptor", self)
                    
