from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VerticalAlignType(Enum):
    vat_Superscript = "vat_Superscript"
    vat_None = "vat_None"
    vat_Subscript = "vat_Subscript"
class VerticalAlignementType(Enum):
    vat_Top = "vat_Top"
    vat_Bottom = "vat_Bottom"
    vat_Justify = "vat_Justify"
    vat_Distributed = "vat_Distributed"
    vat_Center = "vat_Center"
    vat_Automatic = "vat_Automatic"
    vat_JustifyDistributed = "vat_JustifyDistributed"
class CommentsLayoutType(Enum):
    clt_InPlace = "clt_InPlace"
    clt_PrintNone = "clt_PrintNone"
    clt_SheetEnd = "clt_SheetEnd"
class PositionType(Enum):
    pt_DiagonalRight = "pt_DiagonalRight"
    pt_Left = "pt_Left"
    pt_Top = "pt_Top"
    pt_Right = "pt_Right"
    pt_Bottom = "pt_Bottom"
    pt_DiagonalLeft = "pt_DiagonalLeft"
class HorizontalAlignementType(Enum):
    hat_CenterAcrossSelection = "hat_CenterAcrossSelection"
    hat_Fill = "hat_Fill"
    hat_Left = "hat_Left"
    hat_Right = "hat_Right"
    hat_Justify = "hat_Justify"
    hat_Distributed = "hat_Distributed"
    hat_Center = "hat_Center"
    hat_Automatic = "hat_Automatic"
    hat_JustifyDistributed = "hat_JustifyDistributed"
class CalculationWorkbookType(Enum):
    cwt_automaticCalculation = "cwt_automaticCalculation"
    cwt_manualCalculation = "cwt_manualCalculation"
    cwt_semiAutomaticCalculation = "cwt_semiAutomaticCalculation"
class EnableSelectionType(Enum):
    est_UnlockedCells = "est_UnlockedCells"
    est_NoSelection = "est_NoSelection"
class DisplayDrawingObjectsType(Enum):
    ddot_displayShapes = "ddot_displayShapes"
    ddot_placeHolders = "ddot_placeHolders"
    ddot_hideAll = "ddot_hideAll"
class ExcelWorksheetTypeType(Enum):
    ewt_Worksheet = "ewt_Worksheet"
    ewt_Chart = "ewt_Chart"
    ewt_Macro = "ewt_Macro"
    ewt_Dialog = "ewt_Dialog"
class UnderlineType(Enum):
    ut_None = "ut_None"
    ut_Single = "ut_Single"
    ut_Double = "ut_Double"
    ut_SingleAccounting = "ut_SingleAccounting"
    ut_DoubleAccounting = "ut_DoubleAccounting"
class OrientationType(Enum):
    ot_Landscape = "ot_Landscape"
    ot_Portrait = "ot_Portrait"
class ExcelNumberFormatType(Enum):
    enft_General_Date = "enft_General_Date"
    enft_Long_Date = "enft_Long_Date"
    enft_Medium_Date = "enft_Medium_Date"
    enft_General = "enft_General"
    enft_General_Number = "enft_General_Number"
    enft_Short_Date = "enft_Short_Date"
    enft_Long_Time = "enft_Long_Time"
    enft_Medium_Time = "enft_Medium_Time"
    enft_Short_Time = "enft_Short_Time"
    enft_Currency = "enft_Currency"
    enft_Euro_Currency = "enft_Euro_Currency"
    enft_Fixed = "enft_Fixed"
    enft_Standard = "enft_Standard"
    enft_Percent = "enft_Percent"
    enft_Scientific = "enft_Scientific"
    enft_Yes_No = "enft_Yes_No"
    enft_True_False = "enft_True_False"
    enft_On_Off = "enft_On_Off"
class ReadingOrderType(Enum):
    rot_RightToLeft = "rot_RightToLeft"
    rot_LeftToRight = "rot_LeftToRight"
    rot_Context = "rot_Context"
class PatternType(Enum):
    pt_HorzStripe = "pt_HorzStripe"
    pt_VertStripe = "pt_VertStripe"
    pt_ReverseDiagStripe = "pt_ReverseDiagStripe"
    pt_None = "pt_None"
    pt_Solid = "pt_Solid"
    pt_Gray75 = "pt_Gray75"
    pt_Gray50 = "pt_Gray50"
    pt_Gray25 = "pt_Gray25"
    pt_Gray125 = "pt_Gray125"
    pt_Gray0625 = "pt_Gray0625"
    pt_DiagStripe = "pt_DiagStripe"
    pt_DiagCross = "pt_DiagCross"
    pt_ThickDiagCross = "pt_ThickDiagCross"
    pt_ThinHorzStripe = "pt_ThinHorzStripe"
    pt_ThinVertStripe = "pt_ThinVertStripe"
    pt_ThinReverseDiagStripe = "pt_ThinReverseDiagStripe"
    pt_ThinDiagStripe = "pt_ThinDiagStripe"
    pt_ThinHorzCross = "pt_ThinHorzCross"
    pt_ThinDiagCross = "pt_ThinDiagCross"
class VisibleType(Enum):
    vt_SheetVisible = "vt_SheetVisible"
    vt_SheetHidden = "vt_SheetHidden"
    vt_SheetVeryHidden = "vt_SheetVeryHidden"
class LineStyleType(Enum):
    lst_None = "lst_None"
    lst_Continuous = "lst_Continuous"
    lst_Dash = "lst_Dash"
    lst_Dot = "lst_Dot"
    lst_DashDot = "lst_DashDot"
    lst_DashDotDot = "lst_DashDotDot"
    lst_SlantDashDot = "lst_SlantDashDot"
    lst_Double = "lst_Double"


############################################
# Definition of Classes
############################################

class SpreadsheetMLStyles_NamedRange:

    def __init__(self, name: str, refersTo: str, hidden: str, namedRanges: "NamesType" = None):
        self.name = name
        self.refersTo = refersTo
        self.hidden = hidden
        self.namedRanges = namedRanges
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: str):
        self.__hidden = hidden


    @property
    def refersTo(self):
        return self.__refersTo

    @refersTo.setter
    def refersTo(self, refersTo: str):
        self.__refersTo = refersTo


    @property
    def namedRanges(self):
        return self.__namedRanges

    @namedRanges.setter
    def namedRanges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_NamedRange__namedRanges", None)
        self.__namedRanges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NamesType122"):
                opp_val = getattr(old_value, "NamesType122", None)
                if opp_val == self:
                    setattr(old_value, "NamesType122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NamesType122"):
                opp_val = getattr(value, "NamesType122", None)
                setattr(value, "NamesType122", self)

class SpreadsheetMLStyles_NamesType:

    pass
class NamedRange:

    pass
class SpreadsheetMLStyles_NumberFormatType:

    def __init__(self, format: str, numberFormat: "StyleType" = None):
        self.format = format
        self.numberFormat = numberFormat
        
        pass
    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format


    @property
    def numberFormat(self):
        return self.__numberFormat

    @numberFormat.setter
    def numberFormat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_NumberFormatType__numberFormat", None)
        self.__numberFormat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleType117"):
                opp_val = getattr(old_value, "StyleType117", None)
                if opp_val == self:
                    setattr(old_value, "StyleType117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleType117"):
                opp_val = getattr(value, "StyleType117", None)
                setattr(value, "StyleType117", self)

class SpreadsheetMLStyles_InteriorType:

    def __init__(self, color: str, pattern: str, patternColor: str, interior: "StyleType" = None):
        self.color = color
        self.pattern = pattern
        self.patternColor = patternColor
        self.interior = interior
        
        pass
    @property
    def patternColor(self):
        return self.__patternColor

    @patternColor.setter
    def patternColor(self, patternColor: str):
        self.__patternColor = patternColor


    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def interior(self):
        return self.__interior

    @interior.setter
    def interior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_InteriorType__interior", None)
        self.__interior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleType115"):
                opp_val = getattr(old_value, "StyleType115", None)
                if opp_val == self:
                    setattr(old_value, "StyleType115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleType115"):
                opp_val = getattr(value, "StyleType115", None)
                setattr(value, "StyleType115", self)

class SpreadsheetMLStyles_FontType:

    def __init__(self, italic: str, outline: str, bold: str, color: str, fontName: str, shadow: str, size: str, strikeThrough: str, underline: str, verticalAlign: str, font: "StyleType" = None):
        self.italic = italic
        self.outline = outline
        self.bold = bold
        self.color = color
        self.fontName = fontName
        self.shadow = shadow
        self.size = size
        self.strikeThrough = strikeThrough
        self.underline = underline
        self.verticalAlign = verticalAlign
        self.font = font
        
        pass
    @property
    def verticalAlign(self):
        return self.__verticalAlign

    @verticalAlign.setter
    def verticalAlign(self, verticalAlign: str):
        self.__verticalAlign = verticalAlign


    @property
    def underline(self):
        return self.__underline

    @underline.setter
    def underline(self, underline: str):
        self.__underline = underline


    @property
    def bold(self):
        return self.__bold

    @bold.setter
    def bold(self, bold: str):
        self.__bold = bold


    @property
    def outline(self):
        return self.__outline

    @outline.setter
    def outline(self, outline: str):
        self.__outline = outline


    @property
    def shadow(self):
        return self.__shadow

    @shadow.setter
    def shadow(self, shadow: str):
        self.__shadow = shadow


    @property
    def fontName(self):
        return self.__fontName

    @fontName.setter
    def fontName(self, fontName: str):
        self.__fontName = fontName


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def italic(self):
        return self.__italic

    @italic.setter
    def italic(self, italic: str):
        self.__italic = italic


    @property
    def strikeThrough(self):
        return self.__strikeThrough

    @strikeThrough.setter
    def strikeThrough(self, strikeThrough: str):
        self.__strikeThrough = strikeThrough


    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_FontType__font", None)
        self.__font = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleType113"):
                opp_val = getattr(old_value, "StyleType113", None)
                if opp_val == self:
                    setattr(old_value, "StyleType113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleType113"):
                opp_val = getattr(value, "StyleType113", None)
                setattr(value, "StyleType113", self)

class BorderType:

    pass
class SpreadsheetMLStyles_BordersType:

    pass
class SpreadsheetMLStyles_BorderType:

    def __init__(self, position: str, color: str, lineStyle: str, weight: str, border: "BordersType" = None):
        self.position = position
        self.color = color
        self.lineStyle = lineStyle
        self.weight = weight
        self.border = border
        
        pass
    @property
    def lineStyle(self):
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_BorderType__border", None)
        self.__border = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BordersType111"):
                opp_val = getattr(old_value, "BordersType111", None)
                if opp_val == self:
                    setattr(old_value, "BordersType111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BordersType111"):
                opp_val = getattr(value, "BordersType111", None)
                setattr(value, "BordersType111", self)

class SpreadsheetMLStyles_AlignmentType:

    def __init__(self, horizontal: str, shrinkToFit: str, vertical: str, verticalText: str, wrapText: str, readingOrder: str, indent: str, rotate: str, alignment: "StyleType" = None):
        self.horizontal = horizontal
        self.shrinkToFit = shrinkToFit
        self.vertical = vertical
        self.verticalText = verticalText
        self.wrapText = wrapText
        self.readingOrder = readingOrder
        self.indent = indent
        self.rotate = rotate
        self.alignment = alignment
        
        pass
    @property
    def rotate(self):
        return self.__rotate

    @rotate.setter
    def rotate(self, rotate: str):
        self.__rotate = rotate


    @property
    def verticalText(self):
        return self.__verticalText

    @verticalText.setter
    def verticalText(self, verticalText: str):
        self.__verticalText = verticalText


    @property
    def readingOrder(self):
        return self.__readingOrder

    @readingOrder.setter
    def readingOrder(self, readingOrder: str):
        self.__readingOrder = readingOrder


    @property
    def indent(self):
        return self.__indent

    @indent.setter
    def indent(self, indent: str):
        self.__indent = indent


    @property
    def wrapText(self):
        return self.__wrapText

    @wrapText.setter
    def wrapText(self, wrapText: str):
        self.__wrapText = wrapText


    @property
    def horizontal(self):
        return self.__horizontal

    @horizontal.setter
    def horizontal(self, horizontal: str):
        self.__horizontal = horizontal


    @property
    def vertical(self):
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: str):
        self.__vertical = vertical


    @property
    def shrinkToFit(self):
        return self.__shrinkToFit

    @shrinkToFit.setter
    def shrinkToFit(self, shrinkToFit: str):
        self.__shrinkToFit = shrinkToFit


    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_AlignmentType__alignment", None)
        self.__alignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleType106"):
                opp_val = getattr(old_value, "StyleType106", None)
                if opp_val == self:
                    setattr(old_value, "StyleType106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleType106"):
                opp_val = getattr(value, "StyleType106", None)
                setattr(value, "StyleType106", self)

class FontType:

    pass
class SpreadsheetMLStyles_ProtectionType:

    def __init__(self, protected: str, protection: "StyleType" = None):
        self.protected = protected
        self.protection = protection
        
        pass
    @property
    def protected(self):
        return self.__protected

    @protected.setter
    def protected(self, protected: str):
        self.__protected = protected


    @property
    def protection(self):
        return self.__protection

    @protection.setter
    def protection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_ProtectionType__protection", None)
        self.__protection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleType104"):
                opp_val = getattr(old_value, "StyleType104", None)
                if opp_val == self:
                    setattr(old_value, "StyleType104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleType104"):
                opp_val = getattr(value, "StyleType104", None)
                setattr(value, "StyleType104", self)

class ProtectionType:

    pass
class NumberFormatType:

    pass
class InteriorType:

    pass
class BordersType:

    pass
class AlignmentType:

    pass
class SpreadsheetMLStyles_StyleType:

    def __init__(self, id: str, name: str, st_parent: "StyleType" = None, parent: "StyleType" = None, at_styleType: "AlignmentType" = None, style: "StylesCollection" = None, styleID: "StyledElement" = None, it_styleType: "InteriorType" = None, nft_styleType: "NumberFormatType" = None, pt_styleType: "ProtectionType" = None, bt_styleType: "BordersType" = None, ft_styleType: "FontType" = None):
        self.id = id
        self.name = name
        self.st_parent = st_parent
        self.parent = parent
        self.at_styleType = at_styleType
        self.style = style
        self.styleID = styleID
        self.it_styleType = it_styleType
        self.nft_styleType = nft_styleType
        self.pt_styleType = pt_styleType
        self.bt_styleType = bt_styleType
        self.ft_styleType = ft_styleType
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def at_styleType(self):
        return self.__at_styleType

    @at_styleType.setter
    def at_styleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_StyleType__at_styleType", None)
        self.__at_styleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AlignmentType"):
                opp_val = getattr(old_value, "AlignmentType", None)
                if opp_val == self:
                    setattr(old_value, "AlignmentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AlignmentType"):
                opp_val = getattr(value, "AlignmentType", None)
                setattr(value, "AlignmentType", self)

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_StyleType__style", None)
        self.__style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StylesCollection91"):
                opp_val = getattr(old_value, "StylesCollection91", None)
                if opp_val == self:
                    setattr(old_value, "StylesCollection91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StylesCollection91"):
                opp_val = getattr(value, "StylesCollection91", None)
                setattr(value, "StylesCollection91", self)

    @property
    def st_parent(self):
        return self.__st_parent

    @st_parent.setter
    def st_parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_StyleType__st_parent", None)
        self.__st_parent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleType94"):
                opp_val = getattr(old_value, "StyleType94", None)
                if opp_val == self:
                    setattr(old_value, "StyleType94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleType94"):
                opp_val = getattr(value, "StyleType94", None)
                setattr(value, "StyleType94", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_StyleType__parent", None)
        self.__parent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleType96"):
                opp_val = getattr(old_value, "StyleType96", None)
                if opp_val == self:
                    setattr(old_value, "StyleType96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleType96"):
                opp_val = getattr(value, "StyleType96", None)
                setattr(value, "StyleType96", self)

    @property
    def styleID(self):
        return self.__styleID

    @styleID.setter
    def styleID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_StyleType__styleID", None)
        self.__styleID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyledElement"):
                opp_val = getattr(old_value, "StyledElement", None)
                if opp_val == self:
                    setattr(old_value, "StyledElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyledElement"):
                opp_val = getattr(value, "StyledElement", None)
                setattr(value, "StyledElement", self)

    @property
    def it_styleType(self):
        return self.__it_styleType

    @it_styleType.setter
    def it_styleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_StyleType__it_styleType", None)
        self.__it_styleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InteriorType"):
                opp_val = getattr(old_value, "InteriorType", None)
                if opp_val == self:
                    setattr(old_value, "InteriorType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InteriorType"):
                opp_val = getattr(value, "InteriorType", None)
                setattr(value, "InteriorType", self)

    @property
    def nft_styleType(self):
        return self.__nft_styleType

    @nft_styleType.setter
    def nft_styleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_StyleType__nft_styleType", None)
        self.__nft_styleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NumberFormatType"):
                opp_val = getattr(old_value, "NumberFormatType", None)
                if opp_val == self:
                    setattr(old_value, "NumberFormatType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NumberFormatType"):
                opp_val = getattr(value, "NumberFormatType", None)
                setattr(value, "NumberFormatType", self)

    @property
    def pt_styleType(self):
        return self.__pt_styleType

    @pt_styleType.setter
    def pt_styleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_StyleType__pt_styleType", None)
        self.__pt_styleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProtectionType"):
                opp_val = getattr(old_value, "ProtectionType", None)
                if opp_val == self:
                    setattr(old_value, "ProtectionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProtectionType"):
                opp_val = getattr(value, "ProtectionType", None)
                setattr(value, "ProtectionType", self)

    @property
    def ft_styleType(self):
        return self.__ft_styleType

    @ft_styleType.setter
    def ft_styleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_StyleType__ft_styleType", None)
        self.__ft_styleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FontType"):
                opp_val = getattr(old_value, "FontType", None)
                if opp_val == self:
                    setattr(old_value, "FontType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FontType"):
                opp_val = getattr(value, "FontType", None)
                setattr(value, "FontType", self)

    @property
    def bt_styleType(self):
        return self.__bt_styleType

    @bt_styleType.setter
    def bt_styleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_StyleType__bt_styleType", None)
        self.__bt_styleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BordersType"):
                opp_val = getattr(old_value, "BordersType", None)
                if opp_val == self:
                    setattr(old_value, "BordersType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BordersType"):
                opp_val = getattr(value, "BordersType", None)
                setattr(value, "BordersType", self)

class SpreadsheetMLStyles_StylesCollection:

    pass
class SpreadsheetMLStyles_Print:

    def __init__(self, blackAndWhite: str, draftQuality: str, commentsLayout: str, scale: str, printErrors: str, validPrinterInfo: str, paperSizeIndex: str, horizontalResolution: str, fitWidth: str, fitHeight: str, leftToRight: str, verticalResolution: str, gridlines: str, numberOfCopies: str, rowColHeadings: str, wo_print: "WorksheetOptionsElt" = None):
        self.blackAndWhite = blackAndWhite
        self.draftQuality = draftQuality
        self.commentsLayout = commentsLayout
        self.scale = scale
        self.printErrors = printErrors
        self.validPrinterInfo = validPrinterInfo
        self.paperSizeIndex = paperSizeIndex
        self.horizontalResolution = horizontalResolution
        self.fitWidth = fitWidth
        self.fitHeight = fitHeight
        self.leftToRight = leftToRight
        self.verticalResolution = verticalResolution
        self.gridlines = gridlines
        self.numberOfCopies = numberOfCopies
        self.rowColHeadings = rowColHeadings
        self.wo_print = wo_print
        
        pass
    @property
    def rowColHeadings(self):
        return self.__rowColHeadings

    @rowColHeadings.setter
    def rowColHeadings(self, rowColHeadings: str):
        self.__rowColHeadings = rowColHeadings


    @property
    def validPrinterInfo(self):
        return self.__validPrinterInfo

    @validPrinterInfo.setter
    def validPrinterInfo(self, validPrinterInfo: str):
        self.__validPrinterInfo = validPrinterInfo


    @property
    def commentsLayout(self):
        return self.__commentsLayout

    @commentsLayout.setter
    def commentsLayout(self, commentsLayout: str):
        self.__commentsLayout = commentsLayout


    @property
    def blackAndWhite(self):
        return self.__blackAndWhite

    @blackAndWhite.setter
    def blackAndWhite(self, blackAndWhite: str):
        self.__blackAndWhite = blackAndWhite


    @property
    def fitHeight(self):
        return self.__fitHeight

    @fitHeight.setter
    def fitHeight(self, fitHeight: str):
        self.__fitHeight = fitHeight


    @property
    def printErrors(self):
        return self.__printErrors

    @printErrors.setter
    def printErrors(self, printErrors: str):
        self.__printErrors = printErrors


    @property
    def horizontalResolution(self):
        return self.__horizontalResolution

    @horizontalResolution.setter
    def horizontalResolution(self, horizontalResolution: str):
        self.__horizontalResolution = horizontalResolution


    @property
    def verticalResolution(self):
        return self.__verticalResolution

    @verticalResolution.setter
    def verticalResolution(self, verticalResolution: str):
        self.__verticalResolution = verticalResolution


    @property
    def paperSizeIndex(self):
        return self.__paperSizeIndex

    @paperSizeIndex.setter
    def paperSizeIndex(self, paperSizeIndex: str):
        self.__paperSizeIndex = paperSizeIndex


    @property
    def fitWidth(self):
        return self.__fitWidth

    @fitWidth.setter
    def fitWidth(self, fitWidth: str):
        self.__fitWidth = fitWidth


    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale


    @property
    def numberOfCopies(self):
        return self.__numberOfCopies

    @numberOfCopies.setter
    def numberOfCopies(self, numberOfCopies: str):
        self.__numberOfCopies = numberOfCopies


    @property
    def gridlines(self):
        return self.__gridlines

    @gridlines.setter
    def gridlines(self, gridlines: str):
        self.__gridlines = gridlines


    @property
    def leftToRight(self):
        return self.__leftToRight

    @leftToRight.setter
    def leftToRight(self, leftToRight: str):
        self.__leftToRight = leftToRight


    @property
    def draftQuality(self):
        return self.__draftQuality

    @draftQuality.setter
    def draftQuality(self, draftQuality: str):
        self.__draftQuality = draftQuality


    @property
    def wo_print(self):
        return self.__wo_print

    @wo_print.setter
    def wo_print(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Print__wo_print", None)
        self.__wo_print = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorksheetOptionsElt85"):
                opp_val = getattr(old_value, "WorksheetOptionsElt85", None)
                if opp_val == self:
                    setattr(old_value, "WorksheetOptionsElt85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorksheetOptionsElt85"):
                opp_val = getattr(value, "WorksheetOptionsElt85", None)
                setattr(value, "WorksheetOptionsElt85", self)

class SpreadsheetMLStyles_PageMarginsInfo:

    def __init__(self, left: str, right: str, top: str, bottom: str, ps_pageMargins: "PageSetup" = None):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.ps_pageMargins = ps_pageMargins
        
        pass
    @property
    def bottom(self):
        return self.__bottom

    @bottom.setter
    def bottom(self, bottom: str):
        self.__bottom = bottom


    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left: str):
        self.__left = left


    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right: str):
        self.__right = right


    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, top: str):
        self.__top = top


    @property
    def ps_pageMargins(self):
        return self.__ps_pageMargins

    @ps_pageMargins.setter
    def ps_pageMargins(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_PageMarginsInfo__ps_pageMargins", None)
        self.__ps_pageMargins = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PageSetup83"):
                opp_val = getattr(old_value, "PageSetup83", None)
                if opp_val == self:
                    setattr(old_value, "PageSetup83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PageSetup83"):
                opp_val = getattr(value, "PageSetup83", None)
                setattr(value, "PageSetup83", self)

class HeaderOrFooterElt:

    pass
class SpreadsheetMLStyles_Footer(HeaderOrFooterElt):

    pass
class SpreadsheetMLStyles_Header(HeaderOrFooterElt):

    pass
class SpreadsheetMLStyles_HeaderOrFooterElt(ABC):

    def __init__(self, margin: str, data: str):
        self.margin = margin
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


    @property
    def margin(self):
        return self.__margin

    @margin.setter
    def margin(self, margin: str):
        self.__margin = margin


class Layout:

    pass
class SpreadsheetMLStyles_PageSetup:

    pass
class SpreadsheetMLStyles_Layout:

    def __init__(self, orientation: str, centerHorizontal: str, centerVertical: str, startPageNumber: str, ps_layout: "PageSetup" = None):
        self.orientation = orientation
        self.centerHorizontal = centerHorizontal
        self.centerVertical = centerVertical
        self.startPageNumber = startPageNumber
        self.ps_layout = ps_layout
        
        pass
    @property
    def centerHorizontal(self):
        return self.__centerHorizontal

    @centerHorizontal.setter
    def centerHorizontal(self, centerHorizontal: str):
        self.__centerHorizontal = centerHorizontal


    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation


    @property
    def startPageNumber(self):
        return self.__startPageNumber

    @startPageNumber.setter
    def startPageNumber(self, startPageNumber: str):
        self.__startPageNumber = startPageNumber


    @property
    def centerVertical(self):
        return self.__centerVertical

    @centerVertical.setter
    def centerVertical(self, centerVertical: str):
        self.__centerVertical = centerVertical


    @property
    def ps_layout(self):
        return self.__ps_layout

    @ps_layout.setter
    def ps_layout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Layout__ps_layout", None)
        self.__ps_layout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PageSetup77"):
                opp_val = getattr(old_value, "PageSetup77", None)
                if opp_val == self:
                    setattr(old_value, "PageSetup77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PageSetup77"):
                opp_val = getattr(value, "PageSetup77", None)
                setattr(value, "PageSetup77", self)

class PageMarginsInfo:

    pass
class Footer:

    pass
class Header:

    pass
class Print:

    pass
class PageSetup:

    pass
class SpreadsheetMLStyles_WorksheetOptionsElt:

    def __init__(self, standardWidth: str, visible: str, leftColumnVisible: str, selected: str, codeName: str, displayPageBreak: str, transitionExpressionEvaluation: str, doNotDisplayHeadings: str, doNotDisplayOutline: str, applyAutomaticOutlineStyles: str, noSummaryRowsBelowDetail: str, noSummaryColumnsRightDetail: str, doNotDisplayZeros: str, activeRow: str, activeColumn: str, filterOn: str, displayRightToLeft: str, gridlineColorIndex: str, displayFormulas: str, doNotDisplayGridlines: str, leftColumnRightPane: str, activePane: str, splitHorizontal: str, splitVertical: str, freezePanes: str, frozenNoSplit: str, tabColorIndex: str, protectContentst: str, protectObjects: str, rangeSelection: str, topRowVisible: str, topRowBottomPane: str, allowSizeRows: str, allowInsertCols: str, allowInsertRows: str, allowInsertHyperlinks: str, allowDeleteCols: str, allowDeleteRows: str, allowSort: str, allowFilter: str, allowUsePivotTables: str, protectScenarios: str, enableSelection: str, allowFormatCells: str, allowSizeCols: str, fitToPage: str, doNotDisplayColHeaders: str, doNotDisplayRowHeaders: str, gridlineColor: str, name: str, excelWorksheetType: str, intlMacro: str, unsynced: str, transitionFormulaEntry: str, zoom: str, pageBreakZoom: str, showPageBreakZoom: str, defaultRowHeight: str, defaultColumnWidth: str, w_worksheetOptions: "Worksheet" = None, p_worksheetOptions: "Print" = None, ps_worksheetOptions: "PageSetup" = None):
        self.standardWidth = standardWidth
        self.visible = visible
        self.leftColumnVisible = leftColumnVisible
        self.selected = selected
        self.codeName = codeName
        self.displayPageBreak = displayPageBreak
        self.transitionExpressionEvaluation = transitionExpressionEvaluation
        self.doNotDisplayHeadings = doNotDisplayHeadings
        self.doNotDisplayOutline = doNotDisplayOutline
        self.applyAutomaticOutlineStyles = applyAutomaticOutlineStyles
        self.noSummaryRowsBelowDetail = noSummaryRowsBelowDetail
        self.noSummaryColumnsRightDetail = noSummaryColumnsRightDetail
        self.doNotDisplayZeros = doNotDisplayZeros
        self.activeRow = activeRow
        self.activeColumn = activeColumn
        self.filterOn = filterOn
        self.displayRightToLeft = displayRightToLeft
        self.gridlineColorIndex = gridlineColorIndex
        self.displayFormulas = displayFormulas
        self.doNotDisplayGridlines = doNotDisplayGridlines
        self.leftColumnRightPane = leftColumnRightPane
        self.activePane = activePane
        self.splitHorizontal = splitHorizontal
        self.splitVertical = splitVertical
        self.freezePanes = freezePanes
        self.frozenNoSplit = frozenNoSplit
        self.tabColorIndex = tabColorIndex
        self.protectContentst = protectContentst
        self.protectObjects = protectObjects
        self.rangeSelection = rangeSelection
        self.topRowVisible = topRowVisible
        self.topRowBottomPane = topRowBottomPane
        self.allowSizeRows = allowSizeRows
        self.allowInsertCols = allowInsertCols
        self.allowInsertRows = allowInsertRows
        self.allowInsertHyperlinks = allowInsertHyperlinks
        self.allowDeleteCols = allowDeleteCols
        self.allowDeleteRows = allowDeleteRows
        self.allowSort = allowSort
        self.allowFilter = allowFilter
        self.allowUsePivotTables = allowUsePivotTables
        self.protectScenarios = protectScenarios
        self.enableSelection = enableSelection
        self.allowFormatCells = allowFormatCells
        self.allowSizeCols = allowSizeCols
        self.fitToPage = fitToPage
        self.doNotDisplayColHeaders = doNotDisplayColHeaders
        self.doNotDisplayRowHeaders = doNotDisplayRowHeaders
        self.gridlineColor = gridlineColor
        self.name = name
        self.excelWorksheetType = excelWorksheetType
        self.intlMacro = intlMacro
        self.unsynced = unsynced
        self.transitionFormulaEntry = transitionFormulaEntry
        self.zoom = zoom
        self.pageBreakZoom = pageBreakZoom
        self.showPageBreakZoom = showPageBreakZoom
        self.defaultRowHeight = defaultRowHeight
        self.defaultColumnWidth = defaultColumnWidth
        self.w_worksheetOptions = w_worksheetOptions
        self.p_worksheetOptions = p_worksheetOptions
        self.ps_worksheetOptions = ps_worksheetOptions
        
        pass
    @property
    def topRowBottomPane(self):
        return self.__topRowBottomPane

    @topRowBottomPane.setter
    def topRowBottomPane(self, topRowBottomPane: str):
        self.__topRowBottomPane = topRowBottomPane


    @property
    def doNotDisplayHeadings(self):
        return self.__doNotDisplayHeadings

    @doNotDisplayHeadings.setter
    def doNotDisplayHeadings(self, doNotDisplayHeadings: str):
        self.__doNotDisplayHeadings = doNotDisplayHeadings


    @property
    def protectObjects(self):
        return self.__protectObjects

    @protectObjects.setter
    def protectObjects(self, protectObjects: str):
        self.__protectObjects = protectObjects


    @property
    def allowSizeCols(self):
        return self.__allowSizeCols

    @allowSizeCols.setter
    def allowSizeCols(self, allowSizeCols: str):
        self.__allowSizeCols = allowSizeCols


    @property
    def intlMacro(self):
        return self.__intlMacro

    @intlMacro.setter
    def intlMacro(self, intlMacro: str):
        self.__intlMacro = intlMacro


    @property
    def noSummaryColumnsRightDetail(self):
        return self.__noSummaryColumnsRightDetail

    @noSummaryColumnsRightDetail.setter
    def noSummaryColumnsRightDetail(self, noSummaryColumnsRightDetail: str):
        self.__noSummaryColumnsRightDetail = noSummaryColumnsRightDetail


    @property
    def applyAutomaticOutlineStyles(self):
        return self.__applyAutomaticOutlineStyles

    @applyAutomaticOutlineStyles.setter
    def applyAutomaticOutlineStyles(self, applyAutomaticOutlineStyles: str):
        self.__applyAutomaticOutlineStyles = applyAutomaticOutlineStyles


    @property
    def gridlineColor(self):
        return self.__gridlineColor

    @gridlineColor.setter
    def gridlineColor(self, gridlineColor: str):
        self.__gridlineColor = gridlineColor


    @property
    def splitHorizontal(self):
        return self.__splitHorizontal

    @splitHorizontal.setter
    def splitHorizontal(self, splitHorizontal: str):
        self.__splitHorizontal = splitHorizontal


    @property
    def zoom(self):
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom


    @property
    def tabColorIndex(self):
        return self.__tabColorIndex

    @tabColorIndex.setter
    def tabColorIndex(self, tabColorIndex: str):
        self.__tabColorIndex = tabColorIndex


    @property
    def filterOn(self):
        return self.__filterOn

    @filterOn.setter
    def filterOn(self, filterOn: str):
        self.__filterOn = filterOn


    @property
    def allowUsePivotTables(self):
        return self.__allowUsePivotTables

    @allowUsePivotTables.setter
    def allowUsePivotTables(self, allowUsePivotTables: str):
        self.__allowUsePivotTables = allowUsePivotTables


    @property
    def pageBreakZoom(self):
        return self.__pageBreakZoom

    @pageBreakZoom.setter
    def pageBreakZoom(self, pageBreakZoom: str):
        self.__pageBreakZoom = pageBreakZoom


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def excelWorksheetType(self):
        return self.__excelWorksheetType

    @excelWorksheetType.setter
    def excelWorksheetType(self, excelWorksheetType: str):
        self.__excelWorksheetType = excelWorksheetType


    @property
    def allowFilter(self):
        return self.__allowFilter

    @allowFilter.setter
    def allowFilter(self, allowFilter: str):
        self.__allowFilter = allowFilter


    @property
    def allowInsertRows(self):
        return self.__allowInsertRows

    @allowInsertRows.setter
    def allowInsertRows(self, allowInsertRows: str):
        self.__allowInsertRows = allowInsertRows


    @property
    def splitVertical(self):
        return self.__splitVertical

    @splitVertical.setter
    def splitVertical(self, splitVertical: str):
        self.__splitVertical = splitVertical


    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected


    @property
    def displayRightToLeft(self):
        return self.__displayRightToLeft

    @displayRightToLeft.setter
    def displayRightToLeft(self, displayRightToLeft: str):
        self.__displayRightToLeft = displayRightToLeft


    @property
    def protectContentst(self):
        return self.__protectContentst

    @protectContentst.setter
    def protectContentst(self, protectContentst: str):
        self.__protectContentst = protectContentst


    @property
    def transitionExpressionEvaluation(self):
        return self.__transitionExpressionEvaluation

    @transitionExpressionEvaluation.setter
    def transitionExpressionEvaluation(self, transitionExpressionEvaluation: str):
        self.__transitionExpressionEvaluation = transitionExpressionEvaluation


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible


    @property
    def activePane(self):
        return self.__activePane

    @activePane.setter
    def activePane(self, activePane: str):
        self.__activePane = activePane


    @property
    def doNotDisplayOutline(self):
        return self.__doNotDisplayOutline

    @doNotDisplayOutline.setter
    def doNotDisplayOutline(self, doNotDisplayOutline: str):
        self.__doNotDisplayOutline = doNotDisplayOutline


    @property
    def activeColumn(self):
        return self.__activeColumn

    @activeColumn.setter
    def activeColumn(self, activeColumn: str):
        self.__activeColumn = activeColumn


    @property
    def leftColumnRightPane(self):
        return self.__leftColumnRightPane

    @leftColumnRightPane.setter
    def leftColumnRightPane(self, leftColumnRightPane: str):
        self.__leftColumnRightPane = leftColumnRightPane


    @property
    def leftColumnVisible(self):
        return self.__leftColumnVisible

    @leftColumnVisible.setter
    def leftColumnVisible(self, leftColumnVisible: str):
        self.__leftColumnVisible = leftColumnVisible


    @property
    def frozenNoSplit(self):
        return self.__frozenNoSplit

    @frozenNoSplit.setter
    def frozenNoSplit(self, frozenNoSplit: str):
        self.__frozenNoSplit = frozenNoSplit


    @property
    def allowSizeRows(self):
        return self.__allowSizeRows

    @allowSizeRows.setter
    def allowSizeRows(self, allowSizeRows: str):
        self.__allowSizeRows = allowSizeRows


    @property
    def unsynced(self):
        return self.__unsynced

    @unsynced.setter
    def unsynced(self, unsynced: str):
        self.__unsynced = unsynced


    @property
    def defaultRowHeight(self):
        return self.__defaultRowHeight

    @defaultRowHeight.setter
    def defaultRowHeight(self, defaultRowHeight: str):
        self.__defaultRowHeight = defaultRowHeight


    @property
    def transitionFormulaEntry(self):
        return self.__transitionFormulaEntry

    @transitionFormulaEntry.setter
    def transitionFormulaEntry(self, transitionFormulaEntry: str):
        self.__transitionFormulaEntry = transitionFormulaEntry


    @property
    def showPageBreakZoom(self):
        return self.__showPageBreakZoom

    @showPageBreakZoom.setter
    def showPageBreakZoom(self, showPageBreakZoom: str):
        self.__showPageBreakZoom = showPageBreakZoom


    @property
    def allowFormatCells(self):
        return self.__allowFormatCells

    @allowFormatCells.setter
    def allowFormatCells(self, allowFormatCells: str):
        self.__allowFormatCells = allowFormatCells


    @property
    def allowDeleteRows(self):
        return self.__allowDeleteRows

    @allowDeleteRows.setter
    def allowDeleteRows(self, allowDeleteRows: str):
        self.__allowDeleteRows = allowDeleteRows


    @property
    def topRowVisible(self):
        return self.__topRowVisible

    @topRowVisible.setter
    def topRowVisible(self, topRowVisible: str):
        self.__topRowVisible = topRowVisible


    @property
    def freezePanes(self):
        return self.__freezePanes

    @freezePanes.setter
    def freezePanes(self, freezePanes: str):
        self.__freezePanes = freezePanes


    @property
    def allowInsertHyperlinks(self):
        return self.__allowInsertHyperlinks

    @allowInsertHyperlinks.setter
    def allowInsertHyperlinks(self, allowInsertHyperlinks: str):
        self.__allowInsertHyperlinks = allowInsertHyperlinks


    @property
    def doNotDisplayZeros(self):
        return self.__doNotDisplayZeros

    @doNotDisplayZeros.setter
    def doNotDisplayZeros(self, doNotDisplayZeros: str):
        self.__doNotDisplayZeros = doNotDisplayZeros


    @property
    def allowInsertCols(self):
        return self.__allowInsertCols

    @allowInsertCols.setter
    def allowInsertCols(self, allowInsertCols: str):
        self.__allowInsertCols = allowInsertCols


    @property
    def displayPageBreak(self):
        return self.__displayPageBreak

    @displayPageBreak.setter
    def displayPageBreak(self, displayPageBreak: str):
        self.__displayPageBreak = displayPageBreak


    @property
    def allowDeleteCols(self):
        return self.__allowDeleteCols

    @allowDeleteCols.setter
    def allowDeleteCols(self, allowDeleteCols: str):
        self.__allowDeleteCols = allowDeleteCols


    @property
    def displayFormulas(self):
        return self.__displayFormulas

    @displayFormulas.setter
    def displayFormulas(self, displayFormulas: str):
        self.__displayFormulas = displayFormulas


    @property
    def rangeSelection(self):
        return self.__rangeSelection

    @rangeSelection.setter
    def rangeSelection(self, rangeSelection: str):
        self.__rangeSelection = rangeSelection


    @property
    def defaultColumnWidth(self):
        return self.__defaultColumnWidth

    @defaultColumnWidth.setter
    def defaultColumnWidth(self, defaultColumnWidth: str):
        self.__defaultColumnWidth = defaultColumnWidth


    @property
    def allowSort(self):
        return self.__allowSort

    @allowSort.setter
    def allowSort(self, allowSort: str):
        self.__allowSort = allowSort


    @property
    def doNotDisplayGridlines(self):
        return self.__doNotDisplayGridlines

    @doNotDisplayGridlines.setter
    def doNotDisplayGridlines(self, doNotDisplayGridlines: str):
        self.__doNotDisplayGridlines = doNotDisplayGridlines


    @property
    def standardWidth(self):
        return self.__standardWidth

    @standardWidth.setter
    def standardWidth(self, standardWidth: str):
        self.__standardWidth = standardWidth


    @property
    def protectScenarios(self):
        return self.__protectScenarios

    @protectScenarios.setter
    def protectScenarios(self, protectScenarios: str):
        self.__protectScenarios = protectScenarios


    @property
    def gridlineColorIndex(self):
        return self.__gridlineColorIndex

    @gridlineColorIndex.setter
    def gridlineColorIndex(self, gridlineColorIndex: str):
        self.__gridlineColorIndex = gridlineColorIndex


    @property
    def fitToPage(self):
        return self.__fitToPage

    @fitToPage.setter
    def fitToPage(self, fitToPage: str):
        self.__fitToPage = fitToPage


    @property
    def enableSelection(self):
        return self.__enableSelection

    @enableSelection.setter
    def enableSelection(self, enableSelection: str):
        self.__enableSelection = enableSelection


    @property
    def doNotDisplayColHeaders(self):
        return self.__doNotDisplayColHeaders

    @doNotDisplayColHeaders.setter
    def doNotDisplayColHeaders(self, doNotDisplayColHeaders: str):
        self.__doNotDisplayColHeaders = doNotDisplayColHeaders


    @property
    def noSummaryRowsBelowDetail(self):
        return self.__noSummaryRowsBelowDetail

    @noSummaryRowsBelowDetail.setter
    def noSummaryRowsBelowDetail(self, noSummaryRowsBelowDetail: str):
        self.__noSummaryRowsBelowDetail = noSummaryRowsBelowDetail


    @property
    def doNotDisplayRowHeaders(self):
        return self.__doNotDisplayRowHeaders

    @doNotDisplayRowHeaders.setter
    def doNotDisplayRowHeaders(self, doNotDisplayRowHeaders: str):
        self.__doNotDisplayRowHeaders = doNotDisplayRowHeaders


    @property
    def codeName(self):
        return self.__codeName

    @codeName.setter
    def codeName(self, codeName: str):
        self.__codeName = codeName


    @property
    def activeRow(self):
        return self.__activeRow

    @activeRow.setter
    def activeRow(self, activeRow: str):
        self.__activeRow = activeRow


    @property
    def w_worksheetOptions(self):
        return self.__w_worksheetOptions

    @w_worksheetOptions.setter
    def w_worksheetOptions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_WorksheetOptionsElt__w_worksheetOptions", None)
        self.__w_worksheetOptions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Worksheet67"):
                opp_val = getattr(old_value, "Worksheet67", None)
                if opp_val == self:
                    setattr(old_value, "Worksheet67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Worksheet67"):
                opp_val = getattr(value, "Worksheet67", None)
                setattr(value, "Worksheet67", self)

    @property
    def ps_worksheetOptions(self):
        return self.__ps_worksheetOptions

    @ps_worksheetOptions.setter
    def ps_worksheetOptions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_WorksheetOptionsElt__ps_worksheetOptions", None)
        self.__ps_worksheetOptions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PageSetup"):
                opp_val = getattr(old_value, "PageSetup", None)
                if opp_val == self:
                    setattr(old_value, "PageSetup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PageSetup"):
                opp_val = getattr(value, "PageSetup", None)
                setattr(value, "PageSetup", self)

    @property
    def p_worksheetOptions(self):
        return self.__p_worksheetOptions

    @p_worksheetOptions.setter
    def p_worksheetOptions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_WorksheetOptionsElt__p_worksheetOptions", None)
        self.__p_worksheetOptions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Print"):
                opp_val = getattr(old_value, "Print", None)
                if opp_val == self:
                    setattr(old_value, "Print", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Print"):
                opp_val = getattr(value, "Print", None)
                setattr(value, "Print", self)

class SpreadsheetMLStyles_ExcelWorkbook:

    def __init__(self, hideVerticalScrollBar: str, hideWorkbookTabs: str, windowHeight: str, windowWidth: str, windowTopX: str, windowTopY: str, activeSheet: str, selectedSheets: str, windowHidden: str, hideHorizontalScrollBar: str, protectWindows: str, displayInkNotes: str, embedSaveSmartTags: str, futureVer: str, tabRatio: str, windowIconic: str, displayDrawingObjects: str, activeChart: str, firstVisibleSheet: str, hidePivotTableFieldList: str, protectStructure: str, date1904: str, refModeR1C1: str, iteration: str, maxIterations: str, createBackup: str, calculation: str, doNotCalculateBeforeSave: str, noAutoRecover: str, acceptLabelsInFormulas: str, uncalced: str, maxChange: str, precisionAsDisplayed: str, doNotSaveLinkValues: str, wb_excelWorkbook: "Workbook" = None):
        self.hideVerticalScrollBar = hideVerticalScrollBar
        self.hideWorkbookTabs = hideWorkbookTabs
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.windowTopX = windowTopX
        self.windowTopY = windowTopY
        self.activeSheet = activeSheet
        self.selectedSheets = selectedSheets
        self.windowHidden = windowHidden
        self.hideHorizontalScrollBar = hideHorizontalScrollBar
        self.protectWindows = protectWindows
        self.displayInkNotes = displayInkNotes
        self.embedSaveSmartTags = embedSaveSmartTags
        self.futureVer = futureVer
        self.tabRatio = tabRatio
        self.windowIconic = windowIconic
        self.displayDrawingObjects = displayDrawingObjects
        self.activeChart = activeChart
        self.firstVisibleSheet = firstVisibleSheet
        self.hidePivotTableFieldList = hidePivotTableFieldList
        self.protectStructure = protectStructure
        self.date1904 = date1904
        self.refModeR1C1 = refModeR1C1
        self.iteration = iteration
        self.maxIterations = maxIterations
        self.createBackup = createBackup
        self.calculation = calculation
        self.doNotCalculateBeforeSave = doNotCalculateBeforeSave
        self.noAutoRecover = noAutoRecover
        self.acceptLabelsInFormulas = acceptLabelsInFormulas
        self.uncalced = uncalced
        self.maxChange = maxChange
        self.precisionAsDisplayed = precisionAsDisplayed
        self.doNotSaveLinkValues = doNotSaveLinkValues
        self.wb_excelWorkbook = wb_excelWorkbook
        
        pass
    @property
    def refModeR1C1(self):
        return self.__refModeR1C1

    @refModeR1C1.setter
    def refModeR1C1(self, refModeR1C1: str):
        self.__refModeR1C1 = refModeR1C1


    @property
    def acceptLabelsInFormulas(self):
        return self.__acceptLabelsInFormulas

    @acceptLabelsInFormulas.setter
    def acceptLabelsInFormulas(self, acceptLabelsInFormulas: str):
        self.__acceptLabelsInFormulas = acceptLabelsInFormulas


    @property
    def protectStructure(self):
        return self.__protectStructure

    @protectStructure.setter
    def protectStructure(self, protectStructure: str):
        self.__protectStructure = protectStructure


    @property
    def doNotCalculateBeforeSave(self):
        return self.__doNotCalculateBeforeSave

    @doNotCalculateBeforeSave.setter
    def doNotCalculateBeforeSave(self, doNotCalculateBeforeSave: str):
        self.__doNotCalculateBeforeSave = doNotCalculateBeforeSave


    @property
    def maxChange(self):
        return self.__maxChange

    @maxChange.setter
    def maxChange(self, maxChange: str):
        self.__maxChange = maxChange


    @property
    def createBackup(self):
        return self.__createBackup

    @createBackup.setter
    def createBackup(self, createBackup: str):
        self.__createBackup = createBackup


    @property
    def activeSheet(self):
        return self.__activeSheet

    @activeSheet.setter
    def activeSheet(self, activeSheet: str):
        self.__activeSheet = activeSheet


    @property
    def tabRatio(self):
        return self.__tabRatio

    @tabRatio.setter
    def tabRatio(self, tabRatio: str):
        self.__tabRatio = tabRatio


    @property
    def noAutoRecover(self):
        return self.__noAutoRecover

    @noAutoRecover.setter
    def noAutoRecover(self, noAutoRecover: str):
        self.__noAutoRecover = noAutoRecover


    @property
    def windowTopX(self):
        return self.__windowTopX

    @windowTopX.setter
    def windowTopX(self, windowTopX: str):
        self.__windowTopX = windowTopX


    @property
    def windowIconic(self):
        return self.__windowIconic

    @windowIconic.setter
    def windowIconic(self, windowIconic: str):
        self.__windowIconic = windowIconic


    @property
    def firstVisibleSheet(self):
        return self.__firstVisibleSheet

    @firstVisibleSheet.setter
    def firstVisibleSheet(self, firstVisibleSheet: str):
        self.__firstVisibleSheet = firstVisibleSheet


    @property
    def doNotSaveLinkValues(self):
        return self.__doNotSaveLinkValues

    @doNotSaveLinkValues.setter
    def doNotSaveLinkValues(self, doNotSaveLinkValues: str):
        self.__doNotSaveLinkValues = doNotSaveLinkValues


    @property
    def precisionAsDisplayed(self):
        return self.__precisionAsDisplayed

    @precisionAsDisplayed.setter
    def precisionAsDisplayed(self, precisionAsDisplayed: str):
        self.__precisionAsDisplayed = precisionAsDisplayed


    @property
    def futureVer(self):
        return self.__futureVer

    @futureVer.setter
    def futureVer(self, futureVer: str):
        self.__futureVer = futureVer


    @property
    def hideWorkbookTabs(self):
        return self.__hideWorkbookTabs

    @hideWorkbookTabs.setter
    def hideWorkbookTabs(self, hideWorkbookTabs: str):
        self.__hideWorkbookTabs = hideWorkbookTabs


    @property
    def windowHidden(self):
        return self.__windowHidden

    @windowHidden.setter
    def windowHidden(self, windowHidden: str):
        self.__windowHidden = windowHidden


    @property
    def embedSaveSmartTags(self):
        return self.__embedSaveSmartTags

    @embedSaveSmartTags.setter
    def embedSaveSmartTags(self, embedSaveSmartTags: str):
        self.__embedSaveSmartTags = embedSaveSmartTags


    @property
    def calculation(self):
        return self.__calculation

    @calculation.setter
    def calculation(self, calculation: str):
        self.__calculation = calculation


    @property
    def windowTopY(self):
        return self.__windowTopY

    @windowTopY.setter
    def windowTopY(self, windowTopY: str):
        self.__windowTopY = windowTopY


    @property
    def displayDrawingObjects(self):
        return self.__displayDrawingObjects

    @displayDrawingObjects.setter
    def displayDrawingObjects(self, displayDrawingObjects: str):
        self.__displayDrawingObjects = displayDrawingObjects


    @property
    def windowHeight(self):
        return self.__windowHeight

    @windowHeight.setter
    def windowHeight(self, windowHeight: str):
        self.__windowHeight = windowHeight


    @property
    def iteration(self):
        return self.__iteration

    @iteration.setter
    def iteration(self, iteration: str):
        self.__iteration = iteration


    @property
    def windowWidth(self):
        return self.__windowWidth

    @windowWidth.setter
    def windowWidth(self, windowWidth: str):
        self.__windowWidth = windowWidth


    @property
    def activeChart(self):
        return self.__activeChart

    @activeChart.setter
    def activeChart(self, activeChart: str):
        self.__activeChart = activeChart


    @property
    def hideVerticalScrollBar(self):
        return self.__hideVerticalScrollBar

    @hideVerticalScrollBar.setter
    def hideVerticalScrollBar(self, hideVerticalScrollBar: str):
        self.__hideVerticalScrollBar = hideVerticalScrollBar


    @property
    def protectWindows(self):
        return self.__protectWindows

    @protectWindows.setter
    def protectWindows(self, protectWindows: str):
        self.__protectWindows = protectWindows


    @property
    def uncalced(self):
        return self.__uncalced

    @uncalced.setter
    def uncalced(self, uncalced: str):
        self.__uncalced = uncalced


    @property
    def displayInkNotes(self):
        return self.__displayInkNotes

    @displayInkNotes.setter
    def displayInkNotes(self, displayInkNotes: str):
        self.__displayInkNotes = displayInkNotes


    @property
    def selectedSheets(self):
        return self.__selectedSheets

    @selectedSheets.setter
    def selectedSheets(self, selectedSheets: str):
        self.__selectedSheets = selectedSheets


    @property
    def hidePivotTableFieldList(self):
        return self.__hidePivotTableFieldList

    @hidePivotTableFieldList.setter
    def hidePivotTableFieldList(self, hidePivotTableFieldList: str):
        self.__hidePivotTableFieldList = hidePivotTableFieldList


    @property
    def date1904(self):
        return self.__date1904

    @date1904.setter
    def date1904(self, date1904: str):
        self.__date1904 = date1904


    @property
    def hideHorizontalScrollBar(self):
        return self.__hideHorizontalScrollBar

    @hideHorizontalScrollBar.setter
    def hideHorizontalScrollBar(self, hideHorizontalScrollBar: str):
        self.__hideHorizontalScrollBar = hideHorizontalScrollBar


    @property
    def maxIterations(self):
        return self.__maxIterations

    @maxIterations.setter
    def maxIterations(self, maxIterations: str):
        self.__maxIterations = maxIterations


    @property
    def wb_excelWorkbook(self):
        return self.__wb_excelWorkbook

    @wb_excelWorkbook.setter
    def wb_excelWorkbook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_ExcelWorkbook__wb_excelWorkbook", None)
        self.__wb_excelWorkbook = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workbook65"):
                opp_val = getattr(old_value, "Workbook65", None)
                if opp_val == self:
                    setattr(old_value, "Workbook65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workbook65"):
                opp_val = getattr(value, "Workbook65", None)
                setattr(value, "Workbook65", self)

class SpreadsheetMLStyles_Data:

    pass
class Comment:

    pass
class SpreadsheetMLStyles_Comment:

    def __init__(self, author: str, showAlways: str, c_comment: "Cell" = None, d_comment: "Data" = None):
        self.author = author
        self.showAlways = showAlways
        self.c_comment = c_comment
        self.d_comment = d_comment
        
        pass
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def showAlways(self):
        return self.__showAlways

    @showAlways.setter
    def showAlways(self, showAlways: str):
        self.__showAlways = showAlways


    @property
    def c_comment(self):
        return self.__c_comment

    @c_comment.setter
    def c_comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Comment__c_comment", None)
        self.__c_comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cell55"):
                opp_val = getattr(old_value, "Cell55", None)
                if opp_val == self:
                    setattr(old_value, "Cell55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cell55"):
                opp_val = getattr(value, "Cell55", None)
                setattr(value, "Cell55", self)

    @property
    def d_comment(self):
        return self.__d_comment

    @d_comment.setter
    def d_comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Comment__d_comment", None)
        self.__d_comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data57"):
                opp_val = getattr(old_value, "Data57", None)
                if opp_val == self:
                    setattr(old_value, "Data57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data57"):
                opp_val = getattr(value, "Data57", None)
                setattr(value, "Data57", self)

class ColOrRowElement:

    pass
class SpreadsheetMLStyles_Column(ColOrRowElement):

    def __init__(self, width: str, autoFitWidth: str, t_cols: "Table" = None):
        self.width = width
        self.autoFitWidth = autoFitWidth
        self.t_cols = t_cols
        
        pass
    @property
    def autoFitWidth(self):
        return self.__autoFitWidth

    @autoFitWidth.setter
    def autoFitWidth(self, autoFitWidth: str):
        self.__autoFitWidth = autoFitWidth


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def t_cols(self):
        return self.__t_cols

    @t_cols.setter
    def t_cols(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Column__t_cols", None)
        self.__t_cols = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table42"):
                opp_val = getattr(old_value, "Table42", None)
                if opp_val == self:
                    setattr(old_value, "Table42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table42"):
                opp_val = getattr(value, "Table42", None)
                setattr(value, "Table42", self)

class TableElement:

    pass
class SpreadsheetMLStyles_Cell(TableElement):

    def __init__(self, arrayRange: str, formula: str, hRef: str, mergeAcross: str, mergeDown: str, st_cell: set["SmartTagsCollection"] = None, r_cells: "Row" = None, d_cell: "Data" = None, c_cell: "Comment" = None):
        self.arrayRange = arrayRange
        self.formula = formula
        self.hRef = hRef
        self.mergeAcross = mergeAcross
        self.mergeDown = mergeDown
        self.st_cell = st_cell if st_cell is not None else set()
        self.r_cells = r_cells
        self.d_cell = d_cell
        self.c_cell = c_cell
        
        pass
    @property
    def mergeDown(self):
        return self.__mergeDown

    @mergeDown.setter
    def mergeDown(self, mergeDown: str):
        self.__mergeDown = mergeDown


    @property
    def arrayRange(self):
        return self.__arrayRange

    @arrayRange.setter
    def arrayRange(self, arrayRange: str):
        self.__arrayRange = arrayRange


    @property
    def formula(self):
        return self.__formula

    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula


    @property
    def mergeAcross(self):
        return self.__mergeAcross

    @mergeAcross.setter
    def mergeAcross(self, mergeAcross: str):
        self.__mergeAcross = mergeAcross


    @property
    def hRef(self):
        return self.__hRef

    @hRef.setter
    def hRef(self, hRef: str):
        self.__hRef = hRef


    @property
    def r_cells(self):
        return self.__r_cells

    @r_cells.setter
    def r_cells(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Cell__r_cells", None)
        self.__r_cells = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Row50"):
                opp_val = getattr(old_value, "Row50", None)
                if opp_val == self:
                    setattr(old_value, "Row50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Row50"):
                opp_val = getattr(value, "Row50", None)
                setattr(value, "Row50", self)

    @property
    def d_cell(self):
        return self.__d_cell

    @d_cell.setter
    def d_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Cell__d_cell", None)
        self.__d_cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data52"):
                opp_val = getattr(old_value, "Data52", None)
                if opp_val == self:
                    setattr(old_value, "Data52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data52"):
                opp_val = getattr(value, "Data52", None)
                setattr(value, "Data52", self)

    @property
    def st_cell(self):
        return self.__st_cell

    @st_cell.setter
    def st_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Cell__st_cell", None)
        self.__st_cell = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmartTagsCollection48"):
                    opp_val = getattr(item, "SmartTagsCollection48", None)
                    
                    if opp_val == self:
                        setattr(item, "SmartTagsCollection48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmartTagsCollection48"):
                    opp_val = getattr(item, "SmartTagsCollection48", None)
                    
                    setattr(item, "SmartTagsCollection48", self)
                    

    @property
    def c_cell(self):
        return self.__c_cell

    @c_cell.setter
    def c_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Cell__c_cell", None)
        self.__c_cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Comment"):
                opp_val = getattr(old_value, "Comment", None)
                if opp_val == self:
                    setattr(old_value, "Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Comment"):
                opp_val = getattr(value, "Comment", None)
                setattr(value, "Comment", self)

class SpreadsheetMLStyles_ColOrRowElement(TableElement):

    def __init__(self, hidden: str, span: str):
        self.hidden = hidden
        self.span = span
        
        pass
    @property
    def span(self):
        return self.__span

    @span.setter
    def span(self, span: str):
        self.__span = span


    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: str):
        self.__hidden = hidden


class SpreadsheetMLStyles_Row(ColOrRowElement):

    def __init__(self, autoFitHeight: str, height: str, t_rows: "Table" = None, c_row: set["Cell"] = None):
        self.autoFitHeight = autoFitHeight
        self.height = height
        self.t_rows = t_rows
        self.c_row = c_row if c_row is not None else set()
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def autoFitHeight(self):
        return self.__autoFitHeight

    @autoFitHeight.setter
    def autoFitHeight(self, autoFitHeight: str):
        self.__autoFitHeight = autoFitHeight


    @property
    def t_rows(self):
        return self.__t_rows

    @t_rows.setter
    def t_rows(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Row__t_rows", None)
        self.__t_rows = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table44"):
                opp_val = getattr(old_value, "Table44", None)
                if opp_val == self:
                    setattr(old_value, "Table44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table44"):
                opp_val = getattr(value, "Table44", None)
                setattr(value, "Table44", self)

    @property
    def c_row(self):
        return self.__c_row

    @c_row.setter
    def c_row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Row__c_row", None)
        self.__c_row = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cell46"):
                    opp_val = getattr(item, "Cell46", None)
                    
                    if opp_val == self:
                        setattr(item, "Cell46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cell46"):
                    opp_val = getattr(item, "Cell46", None)
                    
                    setattr(item, "Cell46", self)
                    

class Row:

    pass
class Column:

    pass
class StyledElement:

    pass
class SpreadsheetMLStyles_TableElement(StyledElement):

    def __init__(self, index: str, StyledElement: "SpreadsheetMLStyles_StyleType" = None):
        self.index = index
        
        pass
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index


class StyleType:

    pass
class SpreadsheetMLStyles_StyledElement(ABC):

    pass
class WorksheetOptionsElt:

    pass
class Table:

    pass
class SpreadsheetMLStyles_Worksheet:

    def __init__(self, name: str, protected: str, rightToLeft: str, wb_worksheets: "Workbook" = None, t_worksheet: "Table" = None, wo_worksheet: "WorksheetOptionsElt" = None):
        self.name = name
        self.protected = protected
        self.rightToLeft = rightToLeft
        self.wb_worksheets = wb_worksheets
        self.t_worksheet = t_worksheet
        self.wo_worksheet = wo_worksheet
        
        pass
    @property
    def protected(self):
        return self.__protected

    @protected.setter
    def protected(self, protected: str):
        self.__protected = protected


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def rightToLeft(self):
        return self.__rightToLeft

    @rightToLeft.setter
    def rightToLeft(self, rightToLeft: str):
        self.__rightToLeft = rightToLeft


    @property
    def wb_worksheets(self):
        return self.__wb_worksheets

    @wb_worksheets.setter
    def wb_worksheets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Worksheet__wb_worksheets", None)
        self.__wb_worksheets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workbook33"):
                opp_val = getattr(old_value, "Workbook33", None)
                if opp_val == self:
                    setattr(old_value, "Workbook33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workbook33"):
                opp_val = getattr(value, "Workbook33", None)
                setattr(value, "Workbook33", self)

    @property
    def wo_worksheet(self):
        return self.__wo_worksheet

    @wo_worksheet.setter
    def wo_worksheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Worksheet__wo_worksheet", None)
        self.__wo_worksheet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorksheetOptionsElt"):
                opp_val = getattr(old_value, "WorksheetOptionsElt", None)
                if opp_val == self:
                    setattr(old_value, "WorksheetOptionsElt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorksheetOptionsElt"):
                opp_val = getattr(value, "WorksheetOptionsElt", None)
                setattr(value, "WorksheetOptionsElt", self)

    @property
    def t_worksheet(self):
        return self.__t_worksheet

    @t_worksheet.setter
    def t_worksheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Worksheet__t_worksheet", None)
        self.__t_worksheet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table"):
                opp_val = getattr(old_value, "Table", None)
                if opp_val == self:
                    setattr(old_value, "Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table"):
                opp_val = getattr(value, "Table", None)
                setattr(value, "Table", self)

class SpreadsheetMLStyles_Table(StyledElement):

    def __init__(self, topCell: str, defaultColumnWidth: str, defaultRowHeight: str, expandedColumnCount: str, expandedRowCount: str, leftCell: str, fullColumns: str, fullRows: str, ws_table: "Worksheet" = None, c_table: set["Column"] = None, r_table: set["Row"] = None, StyledElement: "SpreadsheetMLStyles_StyleType" = None):
        self.topCell = topCell
        self.defaultColumnWidth = defaultColumnWidth
        self.defaultRowHeight = defaultRowHeight
        self.expandedColumnCount = expandedColumnCount
        self.expandedRowCount = expandedRowCount
        self.leftCell = leftCell
        self.fullColumns = fullColumns
        self.fullRows = fullRows
        self.ws_table = ws_table
        self.c_table = c_table if c_table is not None else set()
        self.r_table = r_table if r_table is not None else set()
        
        pass
    @property
    def fullColumns(self):
        return self.__fullColumns

    @fullColumns.setter
    def fullColumns(self, fullColumns: str):
        self.__fullColumns = fullColumns


    @property
    def defaultRowHeight(self):
        return self.__defaultRowHeight

    @defaultRowHeight.setter
    def defaultRowHeight(self, defaultRowHeight: str):
        self.__defaultRowHeight = defaultRowHeight


    @property
    def topCell(self):
        return self.__topCell

    @topCell.setter
    def topCell(self, topCell: str):
        self.__topCell = topCell


    @property
    def fullRows(self):
        return self.__fullRows

    @fullRows.setter
    def fullRows(self, fullRows: str):
        self.__fullRows = fullRows


    @property
    def leftCell(self):
        return self.__leftCell

    @leftCell.setter
    def leftCell(self, leftCell: str):
        self.__leftCell = leftCell


    @property
    def defaultColumnWidth(self):
        return self.__defaultColumnWidth

    @defaultColumnWidth.setter
    def defaultColumnWidth(self, defaultColumnWidth: str):
        self.__defaultColumnWidth = defaultColumnWidth


    @property
    def expandedRowCount(self):
        return self.__expandedRowCount

    @expandedRowCount.setter
    def expandedRowCount(self, expandedRowCount: str):
        self.__expandedRowCount = expandedRowCount


    @property
    def expandedColumnCount(self):
        return self.__expandedColumnCount

    @expandedColumnCount.setter
    def expandedColumnCount(self, expandedColumnCount: str):
        self.__expandedColumnCount = expandedColumnCount


    @property
    def ws_table(self):
        return self.__ws_table

    @ws_table.setter
    def ws_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Table__ws_table", None)
        self.__ws_table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Worksheet38"):
                opp_val = getattr(old_value, "Worksheet38", None)
                if opp_val == self:
                    setattr(old_value, "Worksheet38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Worksheet38"):
                opp_val = getattr(value, "Worksheet38", None)
                setattr(value, "Worksheet38", self)

    @property
    def c_table(self):
        return self.__c_table

    @c_table.setter
    def c_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Table__c_table", None)
        self.__c_table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    if opp_val == self:
                        setattr(item, "Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    setattr(item, "Column", self)
                    

    @property
    def r_table(self):
        return self.__r_table

    @r_table.setter
    def r_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_Table__r_table", None)
        self.__r_table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Row"):
                    opp_val = getattr(item, "Row", None)
                    
                    if opp_val == self:
                        setattr(item, "Row", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Row"):
                    opp_val = getattr(item, "Row", None)
                    
                    setattr(item, "Row", self)
                    

class NamesType:

    pass
class StylesCollection:

    pass
class ExcelWorkbook:

    pass
class DocumentPropertiesCollection:

    pass
class Worksheet:

    pass
class SmartTagType:

    pass
class Cell:

    pass
class SpreadsheetMLStyles_SmartTagsCollection:

    pass
class SmartTagsCollection:

    pass
class SpreadsheetMLStyles_SmartTagType:

    def __init__(self, namespaceuri: str, name: str, url: str, smartTagTypes: "SmartTagsCollection" = None):
        self.namespaceuri = namespaceuri
        self.name = name
        self.url = url
        self.smartTagTypes = smartTagTypes
        
        pass
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def namespaceuri(self):
        return self.__namespaceuri

    @namespaceuri.setter
    def namespaceuri(self, namespaceuri: str):
        self.__namespaceuri = namespaceuri


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def smartTagTypes(self):
        return self.__smartTagTypes

    @smartTagTypes.setter
    def smartTagTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_SmartTagType__smartTagTypes", None)
        self.__smartTagTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartTagsCollection"):
                opp_val = getattr(old_value, "SmartTagsCollection", None)
                if opp_val == self:
                    setattr(old_value, "SmartTagsCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartTagsCollection"):
                opp_val = getattr(value, "SmartTagsCollection", None)
                setattr(value, "SmartTagsCollection", self)

class SpreadsheetMLStyles_Workbook:

    pass
class CustomDocumentPropertiesCollection:

    pass
class SpreadsheetMLStyles_CustomDocumentProperty:

    def __init__(self, name: str, customDocumentProperties: "CustomDocumentPropertiesCollection" = None, SpreadsheetMLStyles_CustomDocumentProperty: "ValueType" = None):
        self.name = name
        self.customDocumentProperties = customDocumentProperties
        self.SpreadsheetMLStyles_CustomDocumentProperty = SpreadsheetMLStyles_CustomDocumentProperty
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def customDocumentProperties(self):
        return self.__customDocumentProperties

    @customDocumentProperties.setter
    def customDocumentProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_CustomDocumentProperty__customDocumentProperties", None)
        self.__customDocumentProperties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CustomDocumentPropertiesCollection"):
                opp_val = getattr(old_value, "CustomDocumentPropertiesCollection", None)
                if opp_val == self:
                    setattr(old_value, "CustomDocumentPropertiesCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CustomDocumentPropertiesCollection"):
                opp_val = getattr(value, "CustomDocumentPropertiesCollection", None)
                setattr(value, "CustomDocumentPropertiesCollection", self)

    @property
    def SpreadsheetMLStyles_CustomDocumentProperty(self):
        return self.__SpreadsheetMLStyles_CustomDocumentProperty

    @SpreadsheetMLStyles_CustomDocumentProperty.setter
    def SpreadsheetMLStyles_CustomDocumentProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_CustomDocumentProperty__SpreadsheetMLStyles_CustomDocumentProperty", None)
        self.__SpreadsheetMLStyles_CustomDocumentProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueType"):
                opp_val = getattr(old_value, "ValueType", None)
                if opp_val == self:
                    setattr(old_value, "ValueType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueType"):
                opp_val = getattr(value, "ValueType", None)
                setattr(value, "ValueType", self)

class CustomDocumentProperty:

    pass
class SpreadsheetMLStyles_CustomDocumentPropertiesCollection:

    pass
class VersionType:

    pass
class Workbook:

    pass
class SpreadsheetMLStyles_DocumentPropertiesCollection:

    def __init__(self, title: str, subject: str, keywords: str, description: str, category: str, author: str, lastAuthor: str, manager: str, company: str, hyperlinkBase: str, revision: str, presentationFormat: str, guid: str, appName: str, paragraphs: str, totalTime: str, pages: str, words: str, characters: str, charactersWithSpaces: str, bytes: str, lines: str, wb_docProperties: "Workbook" = None, SpreadsheetMLStyles_DocumentPropertiesCollection: "VersionType" = None, SpreadsheetMLStyles_DocumentPropertiesCollection5: "DateTimeType" = None, SpreadsheetMLStyles_DocumentPropertiesCollection8: "DateTimeType" = None, SpreadsheetMLStyles_DocumentPropertiesCollection11: "DateTimeType" = None):
        self.title = title
        self.subject = subject
        self.keywords = keywords
        self.description = description
        self.category = category
        self.author = author
        self.lastAuthor = lastAuthor
        self.manager = manager
        self.company = company
        self.hyperlinkBase = hyperlinkBase
        self.revision = revision
        self.presentationFormat = presentationFormat
        self.guid = guid
        self.appName = appName
        self.paragraphs = paragraphs
        self.totalTime = totalTime
        self.pages = pages
        self.words = words
        self.characters = characters
        self.charactersWithSpaces = charactersWithSpaces
        self.bytes = bytes
        self.lines = lines
        self.wb_docProperties = wb_docProperties
        self.SpreadsheetMLStyles_DocumentPropertiesCollection = SpreadsheetMLStyles_DocumentPropertiesCollection
        self.SpreadsheetMLStyles_DocumentPropertiesCollection5 = SpreadsheetMLStyles_DocumentPropertiesCollection5
        self.SpreadsheetMLStyles_DocumentPropertiesCollection8 = SpreadsheetMLStyles_DocumentPropertiesCollection8
        self.SpreadsheetMLStyles_DocumentPropertiesCollection11 = SpreadsheetMLStyles_DocumentPropertiesCollection11
        
        pass
    @property
    def bytes(self):
        return self.__bytes

    @bytes.setter
    def bytes(self, bytes: str):
        self.__bytes = bytes


    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject


    @property
    def appName(self):
        return self.__appName

    @appName.setter
    def appName(self, appName: str):
        self.__appName = appName


    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company: str):
        self.__company = company


    @property
    def revision(self):
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


    @property
    def guid(self):
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid


    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, words: str):
        self.__words = words


    @property
    def totalTime(self):
        return self.__totalTime

    @totalTime.setter
    def totalTime(self, totalTime: str):
        self.__totalTime = totalTime


    @property
    def hyperlinkBase(self):
        return self.__hyperlinkBase

    @hyperlinkBase.setter
    def hyperlinkBase(self, hyperlinkBase: str):
        self.__hyperlinkBase = hyperlinkBase


    @property
    def lastAuthor(self):
        return self.__lastAuthor

    @lastAuthor.setter
    def lastAuthor(self, lastAuthor: str):
        self.__lastAuthor = lastAuthor


    @property
    def paragraphs(self):
        return self.__paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs: str):
        self.__paragraphs = paragraphs


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords


    @property
    def characters(self):
        return self.__characters

    @characters.setter
    def characters(self, characters: str):
        self.__characters = characters


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def charactersWithSpaces(self):
        return self.__charactersWithSpaces

    @charactersWithSpaces.setter
    def charactersWithSpaces(self, charactersWithSpaces: str):
        self.__charactersWithSpaces = charactersWithSpaces


    @property
    def presentationFormat(self):
        return self.__presentationFormat

    @presentationFormat.setter
    def presentationFormat(self, presentationFormat: str):
        self.__presentationFormat = presentationFormat


    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, lines: str):
        self.__lines = lines


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager: str):
        self.__manager = manager


    @property
    def SpreadsheetMLStyles_DocumentPropertiesCollection5(self):
        return self.__SpreadsheetMLStyles_DocumentPropertiesCollection5

    @SpreadsheetMLStyles_DocumentPropertiesCollection5.setter
    def SpreadsheetMLStyles_DocumentPropertiesCollection5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_DocumentPropertiesCollection__SpreadsheetMLStyles_DocumentPropertiesCollection5", None)
        self.__SpreadsheetMLStyles_DocumentPropertiesCollection5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DateTimeType6"):
                opp_val = getattr(old_value, "DateTimeType6", None)
                if opp_val == self:
                    setattr(old_value, "DateTimeType6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DateTimeType6"):
                opp_val = getattr(value, "DateTimeType6", None)
                setattr(value, "DateTimeType6", self)

    @property
    def SpreadsheetMLStyles_DocumentPropertiesCollection8(self):
        return self.__SpreadsheetMLStyles_DocumentPropertiesCollection8

    @SpreadsheetMLStyles_DocumentPropertiesCollection8.setter
    def SpreadsheetMLStyles_DocumentPropertiesCollection8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_DocumentPropertiesCollection__SpreadsheetMLStyles_DocumentPropertiesCollection8", None)
        self.__SpreadsheetMLStyles_DocumentPropertiesCollection8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DateTimeType9"):
                opp_val = getattr(old_value, "DateTimeType9", None)
                if opp_val == self:
                    setattr(old_value, "DateTimeType9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DateTimeType9"):
                opp_val = getattr(value, "DateTimeType9", None)
                setattr(value, "DateTimeType9", self)

    @property
    def SpreadsheetMLStyles_DocumentPropertiesCollection11(self):
        return self.__SpreadsheetMLStyles_DocumentPropertiesCollection11

    @SpreadsheetMLStyles_DocumentPropertiesCollection11.setter
    def SpreadsheetMLStyles_DocumentPropertiesCollection11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_DocumentPropertiesCollection__SpreadsheetMLStyles_DocumentPropertiesCollection11", None)
        self.__SpreadsheetMLStyles_DocumentPropertiesCollection11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DateTimeType12"):
                opp_val = getattr(old_value, "DateTimeType12", None)
                if opp_val == self:
                    setattr(old_value, "DateTimeType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DateTimeType12"):
                opp_val = getattr(value, "DateTimeType12", None)
                setattr(value, "DateTimeType12", self)

    @property
    def wb_docProperties(self):
        return self.__wb_docProperties

    @wb_docProperties.setter
    def wb_docProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_DocumentPropertiesCollection__wb_docProperties", None)
        self.__wb_docProperties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workbook"):
                opp_val = getattr(old_value, "Workbook", None)
                if opp_val == self:
                    setattr(old_value, "Workbook", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workbook"):
                opp_val = getattr(value, "Workbook", None)
                setattr(value, "Workbook", self)

    @property
    def SpreadsheetMLStyles_DocumentPropertiesCollection(self):
        return self.__SpreadsheetMLStyles_DocumentPropertiesCollection

    @SpreadsheetMLStyles_DocumentPropertiesCollection.setter
    def SpreadsheetMLStyles_DocumentPropertiesCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLStyles_DocumentPropertiesCollection__SpreadsheetMLStyles_DocumentPropertiesCollection", None)
        self.__SpreadsheetMLStyles_DocumentPropertiesCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VersionType"):
                opp_val = getattr(old_value, "VersionType", None)
                if opp_val == self:
                    setattr(old_value, "VersionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VersionType"):
                opp_val = getattr(value, "VersionType", None)
                setattr(value, "VersionType", self)

class DateTimeType:

    pass
class ValueType:

    pass
class SpreadsheetMLStyles_ErrorValue(ValueType):

    pass
class SpreadsheetMLStyles_NumberValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLStyles_CustomDocumentProperty" = None, ValueType63: "SpreadsheetMLStyles_Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLStyles_BooleanValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLStyles_CustomDocumentProperty" = None, ValueType63: "SpreadsheetMLStyles_Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLStyles_DateTimeTypeValue(ValueType):

    pass
class SpreadsheetMLStyles_StringValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLStyles_CustomDocumentProperty" = None, ValueType63: "SpreadsheetMLStyles_Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Data:

    pass
class SpreadsheetMLStyles_ValueType(ABC):

    pass
class SpreadsheetMLStyles_VersionType:

    def __init__(self, n: str, nn: str):
        self.n = n
        self.nn = nn
        
        pass
    @property
    def nn(self):
        return self.__nn

    @nn.setter
    def nn(self, nn: str):
        self.__nn = nn


    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n: str):
        self.__n = n


class SpreadsheetMLStyles_DateTimeType:

    def __init__(self, year: str, month: str, day: str, hour: str, minute: str, second: str):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        
        pass
    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: str):
        self.__second = second


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: str):
        self.__hour = hour


    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute: str):
        self.__minute = minute


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

