import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SpreadsheetMLStyles_NamedRange,
    SpreadsheetMLStyles_NamesType,
    NamedRange,
    SpreadsheetMLStyles_NumberFormatType,
    SpreadsheetMLStyles_InteriorType,
    SpreadsheetMLStyles_FontType,
    BorderType,
    SpreadsheetMLStyles_BordersType,
    SpreadsheetMLStyles_BorderType,
    SpreadsheetMLStyles_AlignmentType,
    FontType,
    SpreadsheetMLStyles_ProtectionType,
    ProtectionType,
    NumberFormatType,
    InteriorType,
    BordersType,
    AlignmentType,
    SpreadsheetMLStyles_StyleType,
    SpreadsheetMLStyles_StylesCollection,
    SpreadsheetMLStyles_Print,
    SpreadsheetMLStyles_PageMarginsInfo,
    HeaderOrFooterElt,
    SpreadsheetMLStyles_Footer,
    SpreadsheetMLStyles_Header,
    SpreadsheetMLStyles_HeaderOrFooterElt,
    Layout,
    SpreadsheetMLStyles_PageSetup,
    SpreadsheetMLStyles_Layout,
    PageMarginsInfo,
    Footer,
    Header,
    Print,
    PageSetup,
    SpreadsheetMLStyles_WorksheetOptionsElt,
    SpreadsheetMLStyles_ExcelWorkbook,
    SpreadsheetMLStyles_Data,
    Comment,
    SpreadsheetMLStyles_Comment,
    ColOrRowElement,
    SpreadsheetMLStyles_Column,
    TableElement,
    SpreadsheetMLStyles_Cell,
    SpreadsheetMLStyles_ColOrRowElement,
    SpreadsheetMLStyles_Row,
    Row,
    Column,
    StyledElement,
    SpreadsheetMLStyles_TableElement,
    StyleType,
    SpreadsheetMLStyles_StyledElement,
    WorksheetOptionsElt,
    Table,
    SpreadsheetMLStyles_Worksheet,
    SpreadsheetMLStyles_Table,
    NamesType,
    StylesCollection,
    ExcelWorkbook,
    DocumentPropertiesCollection,
    Worksheet,
    SmartTagType,
    Cell,
    SpreadsheetMLStyles_SmartTagsCollection,
    SmartTagsCollection,
    SpreadsheetMLStyles_SmartTagType,
    SpreadsheetMLStyles_Workbook,
    CustomDocumentPropertiesCollection,
    SpreadsheetMLStyles_CustomDocumentProperty,
    CustomDocumentProperty,
    SpreadsheetMLStyles_CustomDocumentPropertiesCollection,
    VersionType,
    Workbook,
    SpreadsheetMLStyles_DocumentPropertiesCollection,
    DateTimeType,
    ValueType,
    SpreadsheetMLStyles_NumberValue,
    SpreadsheetMLStyles_ErrorValue,
    SpreadsheetMLStyles_DateTimeTypeValue,
    SpreadsheetMLStyles_BooleanValue,
    SpreadsheetMLStyles_StringValue,
    Data,
    SpreadsheetMLStyles_ValueType,
    SpreadsheetMLStyles_VersionType,
    SpreadsheetMLStyles_DateTimeType,
    PositionType,
    ExcelNumberFormatType,
    CommentsLayoutType,
    VisibleType,
    HorizontalAlignementType,
    ExcelWorksheetTypeType,
    DisplayDrawingObjectsType,
    LineStyleType,
    UnderlineType,
    CalculationWorkbookType,
    ReadingOrderType,
    EnableSelectionType,
    OrientationType,
    VerticalAlignType,
    PatternType,
    VerticalAlignementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheetmlstyles_namedrange_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_NamedRange)


def test_spreadsheetmlstyles_namedrange_constructor_exists():
    assert callable(SpreadsheetMLStyles_NamedRange.__init__)


def test_spreadsheetmlstyles_namedrange_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_NamedRange.__init__)
    params = list(sig.parameters.keys())
    assert "refersTo" in params, "Missing parameter 'refersTo'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlstyles_namedrange_has_refersTo():
    assert hasattr(SpreadsheetMLStyles_NamedRange, "refersTo")
    descriptor = None
    for klass in SpreadsheetMLStyles_NamedRange.__mro__:
        if "refersTo" in klass.__dict__:
            descriptor = klass.__dict__["refersTo"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_namedrange_has_hidden():
    assert hasattr(SpreadsheetMLStyles_NamedRange, "hidden")
    descriptor = None
    for klass in SpreadsheetMLStyles_NamedRange.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_namedrange_has_name():
    assert hasattr(SpreadsheetMLStyles_NamedRange, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles_NamedRange.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_namestype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_NamesType)


def test_spreadsheetmlstyles_namestype_constructor_exists():
    assert callable(SpreadsheetMLStyles_NamesType.__init__)


def test_spreadsheetmlstyles_namestype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_NamesType.__init__)
    params = list(sig.parameters.keys())



def test_namedrange_is_not_abstract():
    assert not inspect.isabstract(NamedRange)


def test_namedrange_constructor_exists():
    assert callable(NamedRange.__init__)


def test_namedrange_constructor_args():
    sig = inspect.signature(NamedRange.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_numberformattype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_NumberFormatType)


def test_spreadsheetmlstyles_numberformattype_constructor_exists():
    assert callable(SpreadsheetMLStyles_NumberFormatType.__init__)


def test_spreadsheetmlstyles_numberformattype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_NumberFormatType.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_spreadsheetmlstyles_numberformattype_has_format():
    assert hasattr(SpreadsheetMLStyles_NumberFormatType, "format")
    descriptor = None
    for klass in SpreadsheetMLStyles_NumberFormatType.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_interiortype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_InteriorType)


def test_spreadsheetmlstyles_interiortype_constructor_exists():
    assert callable(SpreadsheetMLStyles_InteriorType.__init__)


def test_spreadsheetmlstyles_interiortype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_InteriorType.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "patternColor" in params, "Missing parameter 'patternColor'"
    assert "pattern" in params, "Missing parameter 'pattern'"

def test_spreadsheetmlstyles_interiortype_has_color():
    assert hasattr(SpreadsheetMLStyles_InteriorType, "color")
    descriptor = None
    for klass in SpreadsheetMLStyles_InteriorType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_interiortype_has_patternColor():
    assert hasattr(SpreadsheetMLStyles_InteriorType, "patternColor")
    descriptor = None
    for klass in SpreadsheetMLStyles_InteriorType.__mro__:
        if "patternColor" in klass.__dict__:
            descriptor = klass.__dict__["patternColor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_interiortype_has_pattern():
    assert hasattr(SpreadsheetMLStyles_InteriorType, "pattern")
    descriptor = None
    for klass in SpreadsheetMLStyles_InteriorType.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_fonttype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_FontType)


def test_spreadsheetmlstyles_fonttype_constructor_exists():
    assert callable(SpreadsheetMLStyles_FontType.__init__)


def test_spreadsheetmlstyles_fonttype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_FontType.__init__)
    params = list(sig.parameters.keys())
    assert "bold" in params, "Missing parameter 'bold'"
    assert "shadow" in params, "Missing parameter 'shadow'"
    assert "verticalAlign" in params, "Missing parameter 'verticalAlign'"
    assert "underline" in params, "Missing parameter 'underline'"
    assert "size" in params, "Missing parameter 'size'"
    assert "color" in params, "Missing parameter 'color'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "strikeThrough" in params, "Missing parameter 'strikeThrough'"
    assert "italic" in params, "Missing parameter 'italic'"
    assert "outline" in params, "Missing parameter 'outline'"

def test_spreadsheetmlstyles_fonttype_has_bold():
    assert hasattr(SpreadsheetMLStyles_FontType, "bold")
    descriptor = None
    for klass in SpreadsheetMLStyles_FontType.__mro__:
        if "bold" in klass.__dict__:
            descriptor = klass.__dict__["bold"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_fonttype_has_shadow():
    assert hasattr(SpreadsheetMLStyles_FontType, "shadow")
    descriptor = None
    for klass in SpreadsheetMLStyles_FontType.__mro__:
        if "shadow" in klass.__dict__:
            descriptor = klass.__dict__["shadow"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_fonttype_has_verticalAlign():
    assert hasattr(SpreadsheetMLStyles_FontType, "verticalAlign")
    descriptor = None
    for klass in SpreadsheetMLStyles_FontType.__mro__:
        if "verticalAlign" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlign"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_fonttype_has_underline():
    assert hasattr(SpreadsheetMLStyles_FontType, "underline")
    descriptor = None
    for klass in SpreadsheetMLStyles_FontType.__mro__:
        if "underline" in klass.__dict__:
            descriptor = klass.__dict__["underline"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_fonttype_has_size():
    assert hasattr(SpreadsheetMLStyles_FontType, "size")
    descriptor = None
    for klass in SpreadsheetMLStyles_FontType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_fonttype_has_color():
    assert hasattr(SpreadsheetMLStyles_FontType, "color")
    descriptor = None
    for klass in SpreadsheetMLStyles_FontType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_fonttype_has_fontName():
    assert hasattr(SpreadsheetMLStyles_FontType, "fontName")
    descriptor = None
    for klass in SpreadsheetMLStyles_FontType.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_fonttype_has_strikeThrough():
    assert hasattr(SpreadsheetMLStyles_FontType, "strikeThrough")
    descriptor = None
    for klass in SpreadsheetMLStyles_FontType.__mro__:
        if "strikeThrough" in klass.__dict__:
            descriptor = klass.__dict__["strikeThrough"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_fonttype_has_italic():
    assert hasattr(SpreadsheetMLStyles_FontType, "italic")
    descriptor = None
    for klass in SpreadsheetMLStyles_FontType.__mro__:
        if "italic" in klass.__dict__:
            descriptor = klass.__dict__["italic"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_fonttype_has_outline():
    assert hasattr(SpreadsheetMLStyles_FontType, "outline")
    descriptor = None
    for klass in SpreadsheetMLStyles_FontType.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)



def test_bordertype_is_not_abstract():
    assert not inspect.isabstract(BorderType)


def test_bordertype_constructor_exists():
    assert callable(BorderType.__init__)


def test_bordertype_constructor_args():
    sig = inspect.signature(BorderType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_borderstype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_BordersType)


def test_spreadsheetmlstyles_borderstype_constructor_exists():
    assert callable(SpreadsheetMLStyles_BordersType.__init__)


def test_spreadsheetmlstyles_borderstype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_BordersType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_bordertype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_BorderType)


def test_spreadsheetmlstyles_bordertype_constructor_exists():
    assert callable(SpreadsheetMLStyles_BorderType.__init__)


def test_spreadsheetmlstyles_bordertype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_BorderType.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "color" in params, "Missing parameter 'color'"
    assert "position" in params, "Missing parameter 'position'"

def test_spreadsheetmlstyles_bordertype_has_weight():
    assert hasattr(SpreadsheetMLStyles_BorderType, "weight")
    descriptor = None
    for klass in SpreadsheetMLStyles_BorderType.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_bordertype_has_lineStyle():
    assert hasattr(SpreadsheetMLStyles_BorderType, "lineStyle")
    descriptor = None
    for klass in SpreadsheetMLStyles_BorderType.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_bordertype_has_color():
    assert hasattr(SpreadsheetMLStyles_BorderType, "color")
    descriptor = None
    for klass in SpreadsheetMLStyles_BorderType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_bordertype_has_position():
    assert hasattr(SpreadsheetMLStyles_BorderType, "position")
    descriptor = None
    for klass in SpreadsheetMLStyles_BorderType.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_alignmenttype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_AlignmentType)


def test_spreadsheetmlstyles_alignmenttype_constructor_exists():
    assert callable(SpreadsheetMLStyles_AlignmentType.__init__)


def test_spreadsheetmlstyles_alignmenttype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_AlignmentType.__init__)
    params = list(sig.parameters.keys())
    assert "horizontal" in params, "Missing parameter 'horizontal'"
    assert "shrinkToFit" in params, "Missing parameter 'shrinkToFit'"
    assert "verticalText" in params, "Missing parameter 'verticalText'"
    assert "rotate" in params, "Missing parameter 'rotate'"
    assert "wrapText" in params, "Missing parameter 'wrapText'"
    assert "readingOrder" in params, "Missing parameter 'readingOrder'"
    assert "indent" in params, "Missing parameter 'indent'"
    assert "vertical" in params, "Missing parameter 'vertical'"

def test_spreadsheetmlstyles_alignmenttype_has_horizontal():
    assert hasattr(SpreadsheetMLStyles_AlignmentType, "horizontal")
    descriptor = None
    for klass in SpreadsheetMLStyles_AlignmentType.__mro__:
        if "horizontal" in klass.__dict__:
            descriptor = klass.__dict__["horizontal"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_alignmenttype_has_shrinkToFit():
    assert hasattr(SpreadsheetMLStyles_AlignmentType, "shrinkToFit")
    descriptor = None
    for klass in SpreadsheetMLStyles_AlignmentType.__mro__:
        if "shrinkToFit" in klass.__dict__:
            descriptor = klass.__dict__["shrinkToFit"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_alignmenttype_has_verticalText():
    assert hasattr(SpreadsheetMLStyles_AlignmentType, "verticalText")
    descriptor = None
    for klass in SpreadsheetMLStyles_AlignmentType.__mro__:
        if "verticalText" in klass.__dict__:
            descriptor = klass.__dict__["verticalText"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_alignmenttype_has_rotate():
    assert hasattr(SpreadsheetMLStyles_AlignmentType, "rotate")
    descriptor = None
    for klass in SpreadsheetMLStyles_AlignmentType.__mro__:
        if "rotate" in klass.__dict__:
            descriptor = klass.__dict__["rotate"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_alignmenttype_has_wrapText():
    assert hasattr(SpreadsheetMLStyles_AlignmentType, "wrapText")
    descriptor = None
    for klass in SpreadsheetMLStyles_AlignmentType.__mro__:
        if "wrapText" in klass.__dict__:
            descriptor = klass.__dict__["wrapText"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_alignmenttype_has_readingOrder():
    assert hasattr(SpreadsheetMLStyles_AlignmentType, "readingOrder")
    descriptor = None
    for klass in SpreadsheetMLStyles_AlignmentType.__mro__:
        if "readingOrder" in klass.__dict__:
            descriptor = klass.__dict__["readingOrder"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_alignmenttype_has_indent():
    assert hasattr(SpreadsheetMLStyles_AlignmentType, "indent")
    descriptor = None
    for klass in SpreadsheetMLStyles_AlignmentType.__mro__:
        if "indent" in klass.__dict__:
            descriptor = klass.__dict__["indent"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_alignmenttype_has_vertical():
    assert hasattr(SpreadsheetMLStyles_AlignmentType, "vertical")
    descriptor = None
    for klass in SpreadsheetMLStyles_AlignmentType.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)



def test_fonttype_is_not_abstract():
    assert not inspect.isabstract(FontType)


def test_fonttype_constructor_exists():
    assert callable(FontType.__init__)


def test_fonttype_constructor_args():
    sig = inspect.signature(FontType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_protectiontype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_ProtectionType)


def test_spreadsheetmlstyles_protectiontype_constructor_exists():
    assert callable(SpreadsheetMLStyles_ProtectionType.__init__)


def test_spreadsheetmlstyles_protectiontype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_ProtectionType.__init__)
    params = list(sig.parameters.keys())
    assert "protected" in params, "Missing parameter 'protected'"

def test_spreadsheetmlstyles_protectiontype_has_protected():
    assert hasattr(SpreadsheetMLStyles_ProtectionType, "protected")
    descriptor = None
    for klass in SpreadsheetMLStyles_ProtectionType.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)



def test_protectiontype_is_not_abstract():
    assert not inspect.isabstract(ProtectionType)


def test_protectiontype_constructor_exists():
    assert callable(ProtectionType.__init__)


def test_protectiontype_constructor_args():
    sig = inspect.signature(ProtectionType.__init__)
    params = list(sig.parameters.keys())



def test_numberformattype_is_not_abstract():
    assert not inspect.isabstract(NumberFormatType)


def test_numberformattype_constructor_exists():
    assert callable(NumberFormatType.__init__)


def test_numberformattype_constructor_args():
    sig = inspect.signature(NumberFormatType.__init__)
    params = list(sig.parameters.keys())



def test_interiortype_is_not_abstract():
    assert not inspect.isabstract(InteriorType)


def test_interiortype_constructor_exists():
    assert callable(InteriorType.__init__)


def test_interiortype_constructor_args():
    sig = inspect.signature(InteriorType.__init__)
    params = list(sig.parameters.keys())



def test_borderstype_is_not_abstract():
    assert not inspect.isabstract(BordersType)


def test_borderstype_constructor_exists():
    assert callable(BordersType.__init__)


def test_borderstype_constructor_args():
    sig = inspect.signature(BordersType.__init__)
    params = list(sig.parameters.keys())



def test_alignmenttype_is_not_abstract():
    assert not inspect.isabstract(AlignmentType)


def test_alignmenttype_constructor_exists():
    assert callable(AlignmentType.__init__)


def test_alignmenttype_constructor_args():
    sig = inspect.signature(AlignmentType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_styletype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_StyleType)


def test_spreadsheetmlstyles_styletype_constructor_exists():
    assert callable(SpreadsheetMLStyles_StyleType.__init__)


def test_spreadsheetmlstyles_styletype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_StyleType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlstyles_styletype_has_id():
    assert hasattr(SpreadsheetMLStyles_StyleType, "id")
    descriptor = None
    for klass in SpreadsheetMLStyles_StyleType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_styletype_has_name():
    assert hasattr(SpreadsheetMLStyles_StyleType, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles_StyleType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_stylescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_StylesCollection)


def test_spreadsheetmlstyles_stylescollection_constructor_exists():
    assert callable(SpreadsheetMLStyles_StylesCollection.__init__)


def test_spreadsheetmlstyles_stylescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_StylesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_print_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Print)


def test_spreadsheetmlstyles_print_constructor_exists():
    assert callable(SpreadsheetMLStyles_Print.__init__)


def test_spreadsheetmlstyles_print_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Print.__init__)
    params = list(sig.parameters.keys())
    assert "leftToRight" in params, "Missing parameter 'leftToRight'"
    assert "validPrinterInfo" in params, "Missing parameter 'validPrinterInfo'"
    assert "printErrors" in params, "Missing parameter 'printErrors'"
    assert "paperSizeIndex" in params, "Missing parameter 'paperSizeIndex'"
    assert "verticalResolution" in params, "Missing parameter 'verticalResolution'"
    assert "fitHeight" in params, "Missing parameter 'fitHeight'"
    assert "fitWidth" in params, "Missing parameter 'fitWidth'"
    assert "gridlines" in params, "Missing parameter 'gridlines'"
    assert "horizontalResolution" in params, "Missing parameter 'horizontalResolution'"
    assert "commentsLayout" in params, "Missing parameter 'commentsLayout'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "rowColHeadings" in params, "Missing parameter 'rowColHeadings'"
    assert "draftQuality" in params, "Missing parameter 'draftQuality'"
    assert "blackAndWhite" in params, "Missing parameter 'blackAndWhite'"
    assert "numberOfCopies" in params, "Missing parameter 'numberOfCopies'"

def test_spreadsheetmlstyles_print_has_leftToRight():
    assert hasattr(SpreadsheetMLStyles_Print, "leftToRight")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "leftToRight" in klass.__dict__:
            descriptor = klass.__dict__["leftToRight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_validPrinterInfo():
    assert hasattr(SpreadsheetMLStyles_Print, "validPrinterInfo")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "validPrinterInfo" in klass.__dict__:
            descriptor = klass.__dict__["validPrinterInfo"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_printErrors():
    assert hasattr(SpreadsheetMLStyles_Print, "printErrors")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "printErrors" in klass.__dict__:
            descriptor = klass.__dict__["printErrors"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_paperSizeIndex():
    assert hasattr(SpreadsheetMLStyles_Print, "paperSizeIndex")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "paperSizeIndex" in klass.__dict__:
            descriptor = klass.__dict__["paperSizeIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_verticalResolution():
    assert hasattr(SpreadsheetMLStyles_Print, "verticalResolution")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "verticalResolution" in klass.__dict__:
            descriptor = klass.__dict__["verticalResolution"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_fitHeight():
    assert hasattr(SpreadsheetMLStyles_Print, "fitHeight")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "fitHeight" in klass.__dict__:
            descriptor = klass.__dict__["fitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_fitWidth():
    assert hasattr(SpreadsheetMLStyles_Print, "fitWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "fitWidth" in klass.__dict__:
            descriptor = klass.__dict__["fitWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_gridlines():
    assert hasattr(SpreadsheetMLStyles_Print, "gridlines")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "gridlines" in klass.__dict__:
            descriptor = klass.__dict__["gridlines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_horizontalResolution():
    assert hasattr(SpreadsheetMLStyles_Print, "horizontalResolution")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "horizontalResolution" in klass.__dict__:
            descriptor = klass.__dict__["horizontalResolution"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_commentsLayout():
    assert hasattr(SpreadsheetMLStyles_Print, "commentsLayout")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "commentsLayout" in klass.__dict__:
            descriptor = klass.__dict__["commentsLayout"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_scale():
    assert hasattr(SpreadsheetMLStyles_Print, "scale")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_rowColHeadings():
    assert hasattr(SpreadsheetMLStyles_Print, "rowColHeadings")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "rowColHeadings" in klass.__dict__:
            descriptor = klass.__dict__["rowColHeadings"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_draftQuality():
    assert hasattr(SpreadsheetMLStyles_Print, "draftQuality")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "draftQuality" in klass.__dict__:
            descriptor = klass.__dict__["draftQuality"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_blackAndWhite():
    assert hasattr(SpreadsheetMLStyles_Print, "blackAndWhite")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "blackAndWhite" in klass.__dict__:
            descriptor = klass.__dict__["blackAndWhite"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_print_has_numberOfCopies():
    assert hasattr(SpreadsheetMLStyles_Print, "numberOfCopies")
    descriptor = None
    for klass in SpreadsheetMLStyles_Print.__mro__:
        if "numberOfCopies" in klass.__dict__:
            descriptor = klass.__dict__["numberOfCopies"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_pagemarginsinfo_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_PageMarginsInfo)


def test_spreadsheetmlstyles_pagemarginsinfo_constructor_exists():
    assert callable(SpreadsheetMLStyles_PageMarginsInfo.__init__)


def test_spreadsheetmlstyles_pagemarginsinfo_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_PageMarginsInfo.__init__)
    params = list(sig.parameters.keys())
    assert "top" in params, "Missing parameter 'top'"
    assert "bottom" in params, "Missing parameter 'bottom'"
    assert "right" in params, "Missing parameter 'right'"
    assert "left" in params, "Missing parameter 'left'"

def test_spreadsheetmlstyles_pagemarginsinfo_has_top():
    assert hasattr(SpreadsheetMLStyles_PageMarginsInfo, "top")
    descriptor = None
    for klass in SpreadsheetMLStyles_PageMarginsInfo.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_pagemarginsinfo_has_bottom():
    assert hasattr(SpreadsheetMLStyles_PageMarginsInfo, "bottom")
    descriptor = None
    for klass in SpreadsheetMLStyles_PageMarginsInfo.__mro__:
        if "bottom" in klass.__dict__:
            descriptor = klass.__dict__["bottom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_pagemarginsinfo_has_right():
    assert hasattr(SpreadsheetMLStyles_PageMarginsInfo, "right")
    descriptor = None
    for klass in SpreadsheetMLStyles_PageMarginsInfo.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_pagemarginsinfo_has_left():
    assert hasattr(SpreadsheetMLStyles_PageMarginsInfo, "left")
    descriptor = None
    for klass in SpreadsheetMLStyles_PageMarginsInfo.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)



def test_headerorfooterelt_is_not_abstract():
    assert not inspect.isabstract(HeaderOrFooterElt)


def test_headerorfooterelt_constructor_exists():
    assert callable(HeaderOrFooterElt.__init__)


def test_headerorfooterelt_constructor_args():
    sig = inspect.signature(HeaderOrFooterElt.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_footer_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Footer)


def test_spreadsheetmlstyles_footer_constructor_exists():
    assert callable(SpreadsheetMLStyles_Footer.__init__)


def test_spreadsheetmlstyles_footer_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Footer.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_header_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Header)


def test_spreadsheetmlstyles_header_constructor_exists():
    assert callable(SpreadsheetMLStyles_Header.__init__)


def test_spreadsheetmlstyles_header_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Header.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_headerorfooterelt_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_HeaderOrFooterElt)


def test_spreadsheetmlstyles_headerorfooterelt_constructor_exists():
    assert callable(SpreadsheetMLStyles_HeaderOrFooterElt.__init__)


def test_spreadsheetmlstyles_headerorfooterelt_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_HeaderOrFooterElt.__init__)
    params = list(sig.parameters.keys())
    assert "margin" in params, "Missing parameter 'margin'"
    assert "data" in params, "Missing parameter 'data'"

def test_spreadsheetmlstyles_headerorfooterelt_has_margin():
    assert hasattr(SpreadsheetMLStyles_HeaderOrFooterElt, "margin")
    descriptor = None
    for klass in SpreadsheetMLStyles_HeaderOrFooterElt.__mro__:
        if "margin" in klass.__dict__:
            descriptor = klass.__dict__["margin"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_headerorfooterelt_has_data():
    assert hasattr(SpreadsheetMLStyles_HeaderOrFooterElt, "data")
    descriptor = None
    for klass in SpreadsheetMLStyles_HeaderOrFooterElt.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_pagesetup_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_PageSetup)


def test_spreadsheetmlstyles_pagesetup_constructor_exists():
    assert callable(SpreadsheetMLStyles_PageSetup.__init__)


def test_spreadsheetmlstyles_pagesetup_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_PageSetup.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_layout_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Layout)


def test_spreadsheetmlstyles_layout_constructor_exists():
    assert callable(SpreadsheetMLStyles_Layout.__init__)


def test_spreadsheetmlstyles_layout_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Layout.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "centerHorizontal" in params, "Missing parameter 'centerHorizontal'"
    assert "centerVertical" in params, "Missing parameter 'centerVertical'"
    assert "startPageNumber" in params, "Missing parameter 'startPageNumber'"

def test_spreadsheetmlstyles_layout_has_orientation():
    assert hasattr(SpreadsheetMLStyles_Layout, "orientation")
    descriptor = None
    for klass in SpreadsheetMLStyles_Layout.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_layout_has_centerHorizontal():
    assert hasattr(SpreadsheetMLStyles_Layout, "centerHorizontal")
    descriptor = None
    for klass in SpreadsheetMLStyles_Layout.__mro__:
        if "centerHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["centerHorizontal"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_layout_has_centerVertical():
    assert hasattr(SpreadsheetMLStyles_Layout, "centerVertical")
    descriptor = None
    for klass in SpreadsheetMLStyles_Layout.__mro__:
        if "centerVertical" in klass.__dict__:
            descriptor = klass.__dict__["centerVertical"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_layout_has_startPageNumber():
    assert hasattr(SpreadsheetMLStyles_Layout, "startPageNumber")
    descriptor = None
    for klass in SpreadsheetMLStyles_Layout.__mro__:
        if "startPageNumber" in klass.__dict__:
            descriptor = klass.__dict__["startPageNumber"]
            break
    assert isinstance(descriptor, property)



def test_pagemarginsinfo_is_not_abstract():
    assert not inspect.isabstract(PageMarginsInfo)


def test_pagemarginsinfo_constructor_exists():
    assert callable(PageMarginsInfo.__init__)


def test_pagemarginsinfo_constructor_args():
    sig = inspect.signature(PageMarginsInfo.__init__)
    params = list(sig.parameters.keys())



def test_footer_is_not_abstract():
    assert not inspect.isabstract(Footer)


def test_footer_constructor_exists():
    assert callable(Footer.__init__)


def test_footer_constructor_args():
    sig = inspect.signature(Footer.__init__)
    params = list(sig.parameters.keys())



def test_header_is_not_abstract():
    assert not inspect.isabstract(Header)


def test_header_constructor_exists():
    assert callable(Header.__init__)


def test_header_constructor_args():
    sig = inspect.signature(Header.__init__)
    params = list(sig.parameters.keys())



def test_print_is_not_abstract():
    assert not inspect.isabstract(Print)


def test_print_constructor_exists():
    assert callable(Print.__init__)


def test_print_constructor_args():
    sig = inspect.signature(Print.__init__)
    params = list(sig.parameters.keys())



def test_pagesetup_is_not_abstract():
    assert not inspect.isabstract(PageSetup)


def test_pagesetup_constructor_exists():
    assert callable(PageSetup.__init__)


def test_pagesetup_constructor_args():
    sig = inspect.signature(PageSetup.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_worksheetoptionselt_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_WorksheetOptionsElt)


def test_spreadsheetmlstyles_worksheetoptionselt_constructor_exists():
    assert callable(SpreadsheetMLStyles_WorksheetOptionsElt.__init__)


def test_spreadsheetmlstyles_worksheetoptionselt_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_WorksheetOptionsElt.__init__)
    params = list(sig.parameters.keys())
    assert "rangeSelection" in params, "Missing parameter 'rangeSelection'"
    assert "applyAutomaticOutlineStyles" in params, "Missing parameter 'applyAutomaticOutlineStyles'"
    assert "fitToPage" in params, "Missing parameter 'fitToPage'"
    assert "freezePanes" in params, "Missing parameter 'freezePanes'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "filterOn" in params, "Missing parameter 'filterOn'"
    assert "leftColumnRightPane" in params, "Missing parameter 'leftColumnRightPane'"
    assert "allowInsertRows" in params, "Missing parameter 'allowInsertRows'"
    assert "doNotDisplayRowHeaders" in params, "Missing parameter 'doNotDisplayRowHeaders'"
    assert "allowUsePivotTables" in params, "Missing parameter 'allowUsePivotTables'"
    assert "noSummaryRowsBelowDetail" in params, "Missing parameter 'noSummaryRowsBelowDetail'"
    assert "gridlineColor" in params, "Missing parameter 'gridlineColor'"
    assert "intlMacro" in params, "Missing parameter 'intlMacro'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "activePane" in params, "Missing parameter 'activePane'"
    assert "allowSizeRows" in params, "Missing parameter 'allowSizeRows'"
    assert "displayRightToLeft" in params, "Missing parameter 'displayRightToLeft'"
    assert "transitionFormulaEntry" in params, "Missing parameter 'transitionFormulaEntry'"
    assert "leftColumnVisible" in params, "Missing parameter 'leftColumnVisible'"
    assert "allowSizeCols" in params, "Missing parameter 'allowSizeCols'"
    assert "pageBreakZoom" in params, "Missing parameter 'pageBreakZoom'"
    assert "doNotDisplayZeros" in params, "Missing parameter 'doNotDisplayZeros'"
    assert "excelWorksheetType" in params, "Missing parameter 'excelWorksheetType'"
    assert "doNotDisplayOutline" in params, "Missing parameter 'doNotDisplayOutline'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"
    assert "allowDeleteCols" in params, "Missing parameter 'allowDeleteCols'"
    assert "doNotDisplayColHeaders" in params, "Missing parameter 'doNotDisplayColHeaders'"
    assert "noSummaryColumnsRightDetail" in params, "Missing parameter 'noSummaryColumnsRightDetail'"
    assert "allowFilter" in params, "Missing parameter 'allowFilter'"
    assert "allowDeleteRows" in params, "Missing parameter 'allowDeleteRows'"
    assert "splitHorizontal" in params, "Missing parameter 'splitHorizontal'"
    assert "selected" in params, "Missing parameter 'selected'"
    assert "splitVertical" in params, "Missing parameter 'splitVertical'"
    assert "allowFormatCells" in params, "Missing parameter 'allowFormatCells'"
    assert "gridlineColorIndex" in params, "Missing parameter 'gridlineColorIndex'"
    assert "tabColorIndex" in params, "Missing parameter 'tabColorIndex'"
    assert "zoom" in params, "Missing parameter 'zoom'"
    assert "topRowVisible" in params, "Missing parameter 'topRowVisible'"
    assert "codeName" in params, "Missing parameter 'codeName'"
    assert "allowInsertHyperlinks" in params, "Missing parameter 'allowInsertHyperlinks'"
    assert "topRowBottomPane" in params, "Missing parameter 'topRowBottomPane'"
    assert "allowSort" in params, "Missing parameter 'allowSort'"
    assert "doNotDisplayHeadings" in params, "Missing parameter 'doNotDisplayHeadings'"
    assert "allowInsertCols" in params, "Missing parameter 'allowInsertCols'"
    assert "doNotDisplayGridlines" in params, "Missing parameter 'doNotDisplayGridlines'"
    assert "activeColumn" in params, "Missing parameter 'activeColumn'"
    assert "showPageBreakZoom" in params, "Missing parameter 'showPageBreakZoom'"
    assert "protectScenarios" in params, "Missing parameter 'protectScenarios'"
    assert "name" in params, "Missing parameter 'name'"
    assert "transitionExpressionEvaluation" in params, "Missing parameter 'transitionExpressionEvaluation'"
    assert "protectContentst" in params, "Missing parameter 'protectContentst'"
    assert "activeRow" in params, "Missing parameter 'activeRow'"
    assert "displayPageBreak" in params, "Missing parameter 'displayPageBreak'"
    assert "enableSelection" in params, "Missing parameter 'enableSelection'"
    assert "unsynced" in params, "Missing parameter 'unsynced'"
    assert "displayFormulas" in params, "Missing parameter 'displayFormulas'"
    assert "standardWidth" in params, "Missing parameter 'standardWidth'"
    assert "protectObjects" in params, "Missing parameter 'protectObjects'"
    assert "frozenNoSplit" in params, "Missing parameter 'frozenNoSplit'"

def test_spreadsheetmlstyles_worksheetoptionselt_has_rangeSelection():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "rangeSelection")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "rangeSelection" in klass.__dict__:
            descriptor = klass.__dict__["rangeSelection"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_applyAutomaticOutlineStyles():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "applyAutomaticOutlineStyles")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "applyAutomaticOutlineStyles" in klass.__dict__:
            descriptor = klass.__dict__["applyAutomaticOutlineStyles"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_fitToPage():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "fitToPage")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "fitToPage" in klass.__dict__:
            descriptor = klass.__dict__["fitToPage"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_freezePanes():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "freezePanes")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "freezePanes" in klass.__dict__:
            descriptor = klass.__dict__["freezePanes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_filterOn():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "filterOn")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "filterOn" in klass.__dict__:
            descriptor = klass.__dict__["filterOn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_leftColumnRightPane():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "leftColumnRightPane")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "leftColumnRightPane" in klass.__dict__:
            descriptor = klass.__dict__["leftColumnRightPane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_allowInsertRows():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "allowInsertRows")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "allowInsertRows" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_doNotDisplayRowHeaders():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "doNotDisplayRowHeaders")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "doNotDisplayRowHeaders" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayRowHeaders"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_allowUsePivotTables():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "allowUsePivotTables")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "allowUsePivotTables" in klass.__dict__:
            descriptor = klass.__dict__["allowUsePivotTables"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_noSummaryRowsBelowDetail():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "noSummaryRowsBelowDetail")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "noSummaryRowsBelowDetail" in klass.__dict__:
            descriptor = klass.__dict__["noSummaryRowsBelowDetail"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_gridlineColor():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "gridlineColor")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "gridlineColor" in klass.__dict__:
            descriptor = klass.__dict__["gridlineColor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_intlMacro():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "intlMacro")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "intlMacro" in klass.__dict__:
            descriptor = klass.__dict__["intlMacro"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_visible():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "visible")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_activePane():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "activePane")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "activePane" in klass.__dict__:
            descriptor = klass.__dict__["activePane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_allowSizeRows():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "allowSizeRows")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "allowSizeRows" in klass.__dict__:
            descriptor = klass.__dict__["allowSizeRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_displayRightToLeft():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "displayRightToLeft")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "displayRightToLeft" in klass.__dict__:
            descriptor = klass.__dict__["displayRightToLeft"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_transitionFormulaEntry():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "transitionFormulaEntry")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "transitionFormulaEntry" in klass.__dict__:
            descriptor = klass.__dict__["transitionFormulaEntry"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_leftColumnVisible():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "leftColumnVisible")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "leftColumnVisible" in klass.__dict__:
            descriptor = klass.__dict__["leftColumnVisible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_allowSizeCols():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "allowSizeCols")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "allowSizeCols" in klass.__dict__:
            descriptor = klass.__dict__["allowSizeCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_pageBreakZoom():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "pageBreakZoom")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "pageBreakZoom" in klass.__dict__:
            descriptor = klass.__dict__["pageBreakZoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_doNotDisplayZeros():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "doNotDisplayZeros")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "doNotDisplayZeros" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayZeros"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_excelWorksheetType():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "excelWorksheetType")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "excelWorksheetType" in klass.__dict__:
            descriptor = klass.__dict__["excelWorksheetType"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_doNotDisplayOutline():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "doNotDisplayOutline")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "doNotDisplayOutline" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayOutline"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_allowDeleteCols():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "allowDeleteCols")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "allowDeleteCols" in klass.__dict__:
            descriptor = klass.__dict__["allowDeleteCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_doNotDisplayColHeaders():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "doNotDisplayColHeaders")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "doNotDisplayColHeaders" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayColHeaders"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_noSummaryColumnsRightDetail():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "noSummaryColumnsRightDetail")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "noSummaryColumnsRightDetail" in klass.__dict__:
            descriptor = klass.__dict__["noSummaryColumnsRightDetail"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_allowFilter():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "allowFilter")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "allowFilter" in klass.__dict__:
            descriptor = klass.__dict__["allowFilter"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_allowDeleteRows():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "allowDeleteRows")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "allowDeleteRows" in klass.__dict__:
            descriptor = klass.__dict__["allowDeleteRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_splitHorizontal():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "splitHorizontal")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "splitHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["splitHorizontal"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_selected():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "selected")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_splitVertical():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "splitVertical")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "splitVertical" in klass.__dict__:
            descriptor = klass.__dict__["splitVertical"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_allowFormatCells():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "allowFormatCells")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "allowFormatCells" in klass.__dict__:
            descriptor = klass.__dict__["allowFormatCells"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_gridlineColorIndex():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "gridlineColorIndex")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "gridlineColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["gridlineColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_tabColorIndex():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "tabColorIndex")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "tabColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["tabColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_zoom():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "zoom")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_topRowVisible():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "topRowVisible")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "topRowVisible" in klass.__dict__:
            descriptor = klass.__dict__["topRowVisible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_codeName():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "codeName")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "codeName" in klass.__dict__:
            descriptor = klass.__dict__["codeName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_allowInsertHyperlinks():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "allowInsertHyperlinks")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "allowInsertHyperlinks" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertHyperlinks"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_topRowBottomPane():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "topRowBottomPane")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "topRowBottomPane" in klass.__dict__:
            descriptor = klass.__dict__["topRowBottomPane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_allowSort():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "allowSort")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "allowSort" in klass.__dict__:
            descriptor = klass.__dict__["allowSort"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_doNotDisplayHeadings():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "doNotDisplayHeadings")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "doNotDisplayHeadings" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayHeadings"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_allowInsertCols():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "allowInsertCols")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "allowInsertCols" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_doNotDisplayGridlines():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "doNotDisplayGridlines")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "doNotDisplayGridlines" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayGridlines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_activeColumn():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "activeColumn")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "activeColumn" in klass.__dict__:
            descriptor = klass.__dict__["activeColumn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_showPageBreakZoom():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "showPageBreakZoom")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "showPageBreakZoom" in klass.__dict__:
            descriptor = klass.__dict__["showPageBreakZoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_protectScenarios():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "protectScenarios")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "protectScenarios" in klass.__dict__:
            descriptor = klass.__dict__["protectScenarios"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_name():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_transitionExpressionEvaluation():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "transitionExpressionEvaluation")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "transitionExpressionEvaluation" in klass.__dict__:
            descriptor = klass.__dict__["transitionExpressionEvaluation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_protectContentst():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "protectContentst")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "protectContentst" in klass.__dict__:
            descriptor = klass.__dict__["protectContentst"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_activeRow():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "activeRow")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "activeRow" in klass.__dict__:
            descriptor = klass.__dict__["activeRow"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_displayPageBreak():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "displayPageBreak")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "displayPageBreak" in klass.__dict__:
            descriptor = klass.__dict__["displayPageBreak"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_enableSelection():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "enableSelection")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "enableSelection" in klass.__dict__:
            descriptor = klass.__dict__["enableSelection"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_unsynced():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "unsynced")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "unsynced" in klass.__dict__:
            descriptor = klass.__dict__["unsynced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_displayFormulas():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "displayFormulas")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "displayFormulas" in klass.__dict__:
            descriptor = klass.__dict__["displayFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_standardWidth():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "standardWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "standardWidth" in klass.__dict__:
            descriptor = klass.__dict__["standardWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_protectObjects():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "protectObjects")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "protectObjects" in klass.__dict__:
            descriptor = klass.__dict__["protectObjects"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheetoptionselt_has_frozenNoSplit():
    assert hasattr(SpreadsheetMLStyles_WorksheetOptionsElt, "frozenNoSplit")
    descriptor = None
    for klass in SpreadsheetMLStyles_WorksheetOptionsElt.__mro__:
        if "frozenNoSplit" in klass.__dict__:
            descriptor = klass.__dict__["frozenNoSplit"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_excelworkbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_ExcelWorkbook)


def test_spreadsheetmlstyles_excelworkbook_constructor_exists():
    assert callable(SpreadsheetMLStyles_ExcelWorkbook.__init__)


def test_spreadsheetmlstyles_excelworkbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_ExcelWorkbook.__init__)
    params = list(sig.parameters.keys())
    assert "hideWorkbookTabs" in params, "Missing parameter 'hideWorkbookTabs'"
    assert "selectedSheets" in params, "Missing parameter 'selectedSheets'"
    assert "hideVerticalScrollBar" in params, "Missing parameter 'hideVerticalScrollBar'"
    assert "futureVer" in params, "Missing parameter 'futureVer'"
    assert "activeChart" in params, "Missing parameter 'activeChart'"
    assert "iteration" in params, "Missing parameter 'iteration'"
    assert "uncalced" in params, "Missing parameter 'uncalced'"
    assert "windowTopY" in params, "Missing parameter 'windowTopY'"
    assert "hidePivotTableFieldList" in params, "Missing parameter 'hidePivotTableFieldList'"
    assert "windowIconic" in params, "Missing parameter 'windowIconic'"
    assert "windowWidth" in params, "Missing parameter 'windowWidth'"
    assert "precisionAsDisplayed" in params, "Missing parameter 'precisionAsDisplayed'"
    assert "refModeR1C1" in params, "Missing parameter 'refModeR1C1'"
    assert "calculation" in params, "Missing parameter 'calculation'"
    assert "date1904" in params, "Missing parameter 'date1904'"
    assert "maxIterations" in params, "Missing parameter 'maxIterations'"
    assert "tabRatio" in params, "Missing parameter 'tabRatio'"
    assert "displayInkNotes" in params, "Missing parameter 'displayInkNotes'"
    assert "windowTopX" in params, "Missing parameter 'windowTopX'"
    assert "windowHeight" in params, "Missing parameter 'windowHeight'"
    assert "hideHorizontalScrollBar" in params, "Missing parameter 'hideHorizontalScrollBar'"
    assert "activeSheet" in params, "Missing parameter 'activeSheet'"
    assert "createBackup" in params, "Missing parameter 'createBackup'"
    assert "noAutoRecover" in params, "Missing parameter 'noAutoRecover'"
    assert "embedSaveSmartTags" in params, "Missing parameter 'embedSaveSmartTags'"
    assert "acceptLabelsInFormulas" in params, "Missing parameter 'acceptLabelsInFormulas'"
    assert "doNotCalculateBeforeSave" in params, "Missing parameter 'doNotCalculateBeforeSave'"
    assert "displayDrawingObjects" in params, "Missing parameter 'displayDrawingObjects'"
    assert "protectWindows" in params, "Missing parameter 'protectWindows'"
    assert "protectStructure" in params, "Missing parameter 'protectStructure'"
    assert "maxChange" in params, "Missing parameter 'maxChange'"
    assert "windowHidden" in params, "Missing parameter 'windowHidden'"
    assert "firstVisibleSheet" in params, "Missing parameter 'firstVisibleSheet'"
    assert "doNotSaveLinkValues" in params, "Missing parameter 'doNotSaveLinkValues'"

def test_spreadsheetmlstyles_excelworkbook_has_hideWorkbookTabs():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "hideWorkbookTabs")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "hideWorkbookTabs" in klass.__dict__:
            descriptor = klass.__dict__["hideWorkbookTabs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_selectedSheets():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "selectedSheets")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "selectedSheets" in klass.__dict__:
            descriptor = klass.__dict__["selectedSheets"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_hideVerticalScrollBar():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "hideVerticalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "hideVerticalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideVerticalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_futureVer():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "futureVer")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "futureVer" in klass.__dict__:
            descriptor = klass.__dict__["futureVer"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_activeChart():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "activeChart")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "activeChart" in klass.__dict__:
            descriptor = klass.__dict__["activeChart"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_iteration():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "iteration")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "iteration" in klass.__dict__:
            descriptor = klass.__dict__["iteration"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_uncalced():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "uncalced")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "uncalced" in klass.__dict__:
            descriptor = klass.__dict__["uncalced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_windowTopY():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "windowTopY")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "windowTopY" in klass.__dict__:
            descriptor = klass.__dict__["windowTopY"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_hidePivotTableFieldList():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "hidePivotTableFieldList")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "hidePivotTableFieldList" in klass.__dict__:
            descriptor = klass.__dict__["hidePivotTableFieldList"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_windowIconic():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "windowIconic")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "windowIconic" in klass.__dict__:
            descriptor = klass.__dict__["windowIconic"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_windowWidth():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "windowWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "windowWidth" in klass.__dict__:
            descriptor = klass.__dict__["windowWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_precisionAsDisplayed():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "precisionAsDisplayed")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "precisionAsDisplayed" in klass.__dict__:
            descriptor = klass.__dict__["precisionAsDisplayed"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_refModeR1C1():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "refModeR1C1")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "refModeR1C1" in klass.__dict__:
            descriptor = klass.__dict__["refModeR1C1"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_calculation():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "calculation")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "calculation" in klass.__dict__:
            descriptor = klass.__dict__["calculation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_date1904():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "date1904")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "date1904" in klass.__dict__:
            descriptor = klass.__dict__["date1904"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_maxIterations():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "maxIterations")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "maxIterations" in klass.__dict__:
            descriptor = klass.__dict__["maxIterations"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_tabRatio():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "tabRatio")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "tabRatio" in klass.__dict__:
            descriptor = klass.__dict__["tabRatio"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_displayInkNotes():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "displayInkNotes")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "displayInkNotes" in klass.__dict__:
            descriptor = klass.__dict__["displayInkNotes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_windowTopX():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "windowTopX")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "windowTopX" in klass.__dict__:
            descriptor = klass.__dict__["windowTopX"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_windowHeight():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "windowHeight")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "windowHeight" in klass.__dict__:
            descriptor = klass.__dict__["windowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_hideHorizontalScrollBar():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "hideHorizontalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "hideHorizontalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideHorizontalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_activeSheet():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "activeSheet")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "activeSheet" in klass.__dict__:
            descriptor = klass.__dict__["activeSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_createBackup():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "createBackup")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "createBackup" in klass.__dict__:
            descriptor = klass.__dict__["createBackup"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_noAutoRecover():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "noAutoRecover")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "noAutoRecover" in klass.__dict__:
            descriptor = klass.__dict__["noAutoRecover"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_embedSaveSmartTags():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "embedSaveSmartTags")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "embedSaveSmartTags" in klass.__dict__:
            descriptor = klass.__dict__["embedSaveSmartTags"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_acceptLabelsInFormulas():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "acceptLabelsInFormulas")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "acceptLabelsInFormulas" in klass.__dict__:
            descriptor = klass.__dict__["acceptLabelsInFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_doNotCalculateBeforeSave():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "doNotCalculateBeforeSave")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "doNotCalculateBeforeSave" in klass.__dict__:
            descriptor = klass.__dict__["doNotCalculateBeforeSave"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_displayDrawingObjects():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "displayDrawingObjects")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "displayDrawingObjects" in klass.__dict__:
            descriptor = klass.__dict__["displayDrawingObjects"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_protectWindows():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "protectWindows")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "protectWindows" in klass.__dict__:
            descriptor = klass.__dict__["protectWindows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_protectStructure():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "protectStructure")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "protectStructure" in klass.__dict__:
            descriptor = klass.__dict__["protectStructure"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_maxChange():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "maxChange")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "maxChange" in klass.__dict__:
            descriptor = klass.__dict__["maxChange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_windowHidden():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "windowHidden")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "windowHidden" in klass.__dict__:
            descriptor = klass.__dict__["windowHidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_firstVisibleSheet():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "firstVisibleSheet")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "firstVisibleSheet" in klass.__dict__:
            descriptor = klass.__dict__["firstVisibleSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_excelworkbook_has_doNotSaveLinkValues():
    assert hasattr(SpreadsheetMLStyles_ExcelWorkbook, "doNotSaveLinkValues")
    descriptor = None
    for klass in SpreadsheetMLStyles_ExcelWorkbook.__mro__:
        if "doNotSaveLinkValues" in klass.__dict__:
            descriptor = klass.__dict__["doNotSaveLinkValues"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_data_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Data)


def test_spreadsheetmlstyles_data_constructor_exists():
    assert callable(SpreadsheetMLStyles_Data.__init__)


def test_spreadsheetmlstyles_data_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Data.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_comment_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Comment)


def test_spreadsheetmlstyles_comment_constructor_exists():
    assert callable(SpreadsheetMLStyles_Comment.__init__)


def test_spreadsheetmlstyles_comment_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "showAlways" in params, "Missing parameter 'showAlways'"
    assert "author" in params, "Missing parameter 'author'"

def test_spreadsheetmlstyles_comment_has_showAlways():
    assert hasattr(SpreadsheetMLStyles_Comment, "showAlways")
    descriptor = None
    for klass in SpreadsheetMLStyles_Comment.__mro__:
        if "showAlways" in klass.__dict__:
            descriptor = klass.__dict__["showAlways"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_comment_has_author():
    assert hasattr(SpreadsheetMLStyles_Comment, "author")
    descriptor = None
    for klass in SpreadsheetMLStyles_Comment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(ColOrRowElement)


def test_colorrowelement_constructor_exists():
    assert callable(ColOrRowElement.__init__)


def test_colorrowelement_constructor_args():
    sig = inspect.signature(ColOrRowElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_column_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Column)


def test_spreadsheetmlstyles_column_constructor_exists():
    assert callable(SpreadsheetMLStyles_Column.__init__)


def test_spreadsheetmlstyles_column_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Column.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitWidth" in params, "Missing parameter 'autoFitWidth'"
    assert "width" in params, "Missing parameter 'width'"

def test_spreadsheetmlstyles_column_has_autoFitWidth():
    assert hasattr(SpreadsheetMLStyles_Column, "autoFitWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles_Column.__mro__:
        if "autoFitWidth" in klass.__dict__:
            descriptor = klass.__dict__["autoFitWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_column_has_width():
    assert hasattr(SpreadsheetMLStyles_Column, "width")
    descriptor = None
    for klass in SpreadsheetMLStyles_Column.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_cell_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Cell)


def test_spreadsheetmlstyles_cell_constructor_exists():
    assert callable(SpreadsheetMLStyles_Cell.__init__)


def test_spreadsheetmlstyles_cell_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Cell.__init__)
    params = list(sig.parameters.keys())
    assert "mergeAcross" in params, "Missing parameter 'mergeAcross'"
    assert "arrayRange" in params, "Missing parameter 'arrayRange'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "mergeDown" in params, "Missing parameter 'mergeDown'"
    assert "hRef" in params, "Missing parameter 'hRef'"

def test_spreadsheetmlstyles_cell_has_mergeAcross():
    assert hasattr(SpreadsheetMLStyles_Cell, "mergeAcross")
    descriptor = None
    for klass in SpreadsheetMLStyles_Cell.__mro__:
        if "mergeAcross" in klass.__dict__:
            descriptor = klass.__dict__["mergeAcross"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_cell_has_arrayRange():
    assert hasattr(SpreadsheetMLStyles_Cell, "arrayRange")
    descriptor = None
    for klass in SpreadsheetMLStyles_Cell.__mro__:
        if "arrayRange" in klass.__dict__:
            descriptor = klass.__dict__["arrayRange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_cell_has_formula():
    assert hasattr(SpreadsheetMLStyles_Cell, "formula")
    descriptor = None
    for klass in SpreadsheetMLStyles_Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_cell_has_mergeDown():
    assert hasattr(SpreadsheetMLStyles_Cell, "mergeDown")
    descriptor = None
    for klass in SpreadsheetMLStyles_Cell.__mro__:
        if "mergeDown" in klass.__dict__:
            descriptor = klass.__dict__["mergeDown"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_cell_has_hRef():
    assert hasattr(SpreadsheetMLStyles_Cell, "hRef")
    descriptor = None
    for klass in SpreadsheetMLStyles_Cell.__mro__:
        if "hRef" in klass.__dict__:
            descriptor = klass.__dict__["hRef"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_ColOrRowElement)


def test_spreadsheetmlstyles_colorrowelement_constructor_exists():
    assert callable(SpreadsheetMLStyles_ColOrRowElement.__init__)


def test_spreadsheetmlstyles_colorrowelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "span" in params, "Missing parameter 'span'"
    assert "hidden" in params, "Missing parameter 'hidden'"

def test_spreadsheetmlstyles_colorrowelement_has_span():
    assert hasattr(SpreadsheetMLStyles_ColOrRowElement, "span")
    descriptor = None
    for klass in SpreadsheetMLStyles_ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_colorrowelement_has_hidden():
    assert hasattr(SpreadsheetMLStyles_ColOrRowElement, "hidden")
    descriptor = None
    for klass in SpreadsheetMLStyles_ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_row_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Row)


def test_spreadsheetmlstyles_row_constructor_exists():
    assert callable(SpreadsheetMLStyles_Row.__init__)


def test_spreadsheetmlstyles_row_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Row.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "autoFitHeight" in params, "Missing parameter 'autoFitHeight'"

def test_spreadsheetmlstyles_row_has_height():
    assert hasattr(SpreadsheetMLStyles_Row, "height")
    descriptor = None
    for klass in SpreadsheetMLStyles_Row.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_row_has_autoFitHeight():
    assert hasattr(SpreadsheetMLStyles_Row, "autoFitHeight")
    descriptor = None
    for klass in SpreadsheetMLStyles_Row.__mro__:
        if "autoFitHeight" in klass.__dict__:
            descriptor = klass.__dict__["autoFitHeight"]
            break
    assert isinstance(descriptor, property)



def test_row_is_not_abstract():
    assert not inspect.isabstract(Row)


def test_row_constructor_exists():
    assert callable(Row.__init__)


def test_row_constructor_args():
    sig = inspect.signature(Row.__init__)
    params = list(sig.parameters.keys())



def test_column_is_not_abstract():
    assert not inspect.isabstract(Column)


def test_column_constructor_exists():
    assert callable(Column.__init__)


def test_column_constructor_args():
    sig = inspect.signature(Column.__init__)
    params = list(sig.parameters.keys())



def test_styledelement_is_not_abstract():
    assert not inspect.isabstract(StyledElement)


def test_styledelement_constructor_exists():
    assert callable(StyledElement.__init__)


def test_styledelement_constructor_args():
    sig = inspect.signature(StyledElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_tableelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_TableElement)


def test_spreadsheetmlstyles_tableelement_constructor_exists():
    assert callable(SpreadsheetMLStyles_TableElement.__init__)


def test_spreadsheetmlstyles_tableelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_spreadsheetmlstyles_tableelement_has_index():
    assert hasattr(SpreadsheetMLStyles_TableElement, "index")
    descriptor = None
    for klass in SpreadsheetMLStyles_TableElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_styletype_is_not_abstract():
    assert not inspect.isabstract(StyleType)


def test_styletype_constructor_exists():
    assert callable(StyleType.__init__)


def test_styletype_constructor_args():
    sig = inspect.signature(StyleType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_styledelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_StyledElement)


def test_spreadsheetmlstyles_styledelement_constructor_exists():
    assert callable(SpreadsheetMLStyles_StyledElement.__init__)


def test_spreadsheetmlstyles_styledelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_StyledElement.__init__)
    params = list(sig.parameters.keys())



def test_worksheetoptionselt_is_not_abstract():
    assert not inspect.isabstract(WorksheetOptionsElt)


def test_worksheetoptionselt_constructor_exists():
    assert callable(WorksheetOptionsElt.__init__)


def test_worksheetoptionselt_constructor_args():
    sig = inspect.signature(WorksheetOptionsElt.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_worksheet_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Worksheet)


def test_spreadsheetmlstyles_worksheet_constructor_exists():
    assert callable(SpreadsheetMLStyles_Worksheet.__init__)


def test_spreadsheetmlstyles_worksheet_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "protected" in params, "Missing parameter 'protected'"
    assert "rightToLeft" in params, "Missing parameter 'rightToLeft'"
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlstyles_worksheet_has_protected():
    assert hasattr(SpreadsheetMLStyles_Worksheet, "protected")
    descriptor = None
    for klass in SpreadsheetMLStyles_Worksheet.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheet_has_rightToLeft():
    assert hasattr(SpreadsheetMLStyles_Worksheet, "rightToLeft")
    descriptor = None
    for klass in SpreadsheetMLStyles_Worksheet.__mro__:
        if "rightToLeft" in klass.__dict__:
            descriptor = klass.__dict__["rightToLeft"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_worksheet_has_name():
    assert hasattr(SpreadsheetMLStyles_Worksheet, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles_Worksheet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_table_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Table)


def test_spreadsheetmlstyles_table_constructor_exists():
    assert callable(SpreadsheetMLStyles_Table.__init__)


def test_spreadsheetmlstyles_table_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Table.__init__)
    params = list(sig.parameters.keys())
    assert "fullColumns" in params, "Missing parameter 'fullColumns'"
    assert "topCell" in params, "Missing parameter 'topCell'"
    assert "fullRows" in params, "Missing parameter 'fullRows'"
    assert "leftCell" in params, "Missing parameter 'leftCell'"
    assert "expandedRowCount" in params, "Missing parameter 'expandedRowCount'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "expandedColumnCount" in params, "Missing parameter 'expandedColumnCount'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"

def test_spreadsheetmlstyles_table_has_fullColumns():
    assert hasattr(SpreadsheetMLStyles_Table, "fullColumns")
    descriptor = None
    for klass in SpreadsheetMLStyles_Table.__mro__:
        if "fullColumns" in klass.__dict__:
            descriptor = klass.__dict__["fullColumns"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_table_has_topCell():
    assert hasattr(SpreadsheetMLStyles_Table, "topCell")
    descriptor = None
    for klass in SpreadsheetMLStyles_Table.__mro__:
        if "topCell" in klass.__dict__:
            descriptor = klass.__dict__["topCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_table_has_fullRows():
    assert hasattr(SpreadsheetMLStyles_Table, "fullRows")
    descriptor = None
    for klass in SpreadsheetMLStyles_Table.__mro__:
        if "fullRows" in klass.__dict__:
            descriptor = klass.__dict__["fullRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_table_has_leftCell():
    assert hasattr(SpreadsheetMLStyles_Table, "leftCell")
    descriptor = None
    for klass in SpreadsheetMLStyles_Table.__mro__:
        if "leftCell" in klass.__dict__:
            descriptor = klass.__dict__["leftCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_table_has_expandedRowCount():
    assert hasattr(SpreadsheetMLStyles_Table, "expandedRowCount")
    descriptor = None
    for klass in SpreadsheetMLStyles_Table.__mro__:
        if "expandedRowCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedRowCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_table_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLStyles_Table, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLStyles_Table.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_table_has_expandedColumnCount():
    assert hasattr(SpreadsheetMLStyles_Table, "expandedColumnCount")
    descriptor = None
    for klass in SpreadsheetMLStyles_Table.__mro__:
        if "expandedColumnCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedColumnCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_table_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLStyles_Table, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles_Table.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)



def test_namestype_is_not_abstract():
    assert not inspect.isabstract(NamesType)


def test_namestype_constructor_exists():
    assert callable(NamesType.__init__)


def test_namestype_constructor_args():
    sig = inspect.signature(NamesType.__init__)
    params = list(sig.parameters.keys())



def test_stylescollection_is_not_abstract():
    assert not inspect.isabstract(StylesCollection)


def test_stylescollection_constructor_exists():
    assert callable(StylesCollection.__init__)


def test_stylescollection_constructor_args():
    sig = inspect.signature(StylesCollection.__init__)
    params = list(sig.parameters.keys())



def test_excelworkbook_is_not_abstract():
    assert not inspect.isabstract(ExcelWorkbook)


def test_excelworkbook_constructor_exists():
    assert callable(ExcelWorkbook.__init__)


def test_excelworkbook_constructor_args():
    sig = inspect.signature(ExcelWorkbook.__init__)
    params = list(sig.parameters.keys())



def test_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DocumentPropertiesCollection)


def test_documentpropertiescollection_constructor_exists():
    assert callable(DocumentPropertiesCollection.__init__)


def test_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_worksheet_is_not_abstract():
    assert not inspect.isabstract(Worksheet)


def test_worksheet_constructor_exists():
    assert callable(Worksheet.__init__)


def test_worksheet_constructor_args():
    sig = inspect.signature(Worksheet.__init__)
    params = list(sig.parameters.keys())



def test_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SmartTagType)


def test_smarttagtype_constructor_exists():
    assert callable(SmartTagType.__init__)


def test_smarttagtype_constructor_args():
    sig = inspect.signature(SmartTagType.__init__)
    params = list(sig.parameters.keys())



def test_cell_is_not_abstract():
    assert not inspect.isabstract(Cell)


def test_cell_constructor_exists():
    assert callable(Cell.__init__)


def test_cell_constructor_args():
    sig = inspect.signature(Cell.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_SmartTagsCollection)


def test_spreadsheetmlstyles_smarttagscollection_constructor_exists():
    assert callable(SpreadsheetMLStyles_SmartTagsCollection.__init__)


def test_spreadsheetmlstyles_smarttagscollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SmartTagsCollection)


def test_smarttagscollection_constructor_exists():
    assert callable(SmartTagsCollection.__init__)


def test_smarttagscollection_constructor_args():
    sig = inspect.signature(SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_SmartTagType)


def test_spreadsheetmlstyles_smarttagtype_constructor_exists():
    assert callable(SpreadsheetMLStyles_SmartTagType.__init__)


def test_spreadsheetmlstyles_smarttagtype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"
    assert "url" in params, "Missing parameter 'url'"

def test_spreadsheetmlstyles_smarttagtype_has_name():
    assert hasattr(SpreadsheetMLStyles_SmartTagType, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles_SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_smarttagtype_has_namespaceuri():
    assert hasattr(SpreadsheetMLStyles_SmartTagType, "namespaceuri")
    descriptor = None
    for klass in SpreadsheetMLStyles_SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_smarttagtype_has_url():
    assert hasattr(SpreadsheetMLStyles_SmartTagType, "url")
    descriptor = None
    for klass in SpreadsheetMLStyles_SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_workbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_Workbook)


def test_spreadsheetmlstyles_workbook_constructor_exists():
    assert callable(SpreadsheetMLStyles_Workbook.__init__)


def test_spreadsheetmlstyles_workbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_Workbook.__init__)
    params = list(sig.parameters.keys())



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_CustomDocumentProperty)


def test_spreadsheetmlstyles_customdocumentproperty_constructor_exists():
    assert callable(SpreadsheetMLStyles_CustomDocumentProperty.__init__)


def test_spreadsheetmlstyles_customdocumentproperty_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlstyles_customdocumentproperty_has_name():
    assert hasattr(SpreadsheetMLStyles_CustomDocumentProperty, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles_CustomDocumentProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentProperty)


def test_customdocumentproperty_constructor_exists():
    assert callable(CustomDocumentProperty.__init__)


def test_customdocumentproperty_constructor_args():
    sig = inspect.signature(CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_CustomDocumentPropertiesCollection)


def test_spreadsheetmlstyles_customdocumentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLStyles_CustomDocumentPropertiesCollection.__init__)


def test_spreadsheetmlstyles_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_versiontype_is_not_abstract():
    assert not inspect.isabstract(VersionType)


def test_versiontype_constructor_exists():
    assert callable(VersionType.__init__)


def test_versiontype_constructor_args():
    sig = inspect.signature(VersionType.__init__)
    params = list(sig.parameters.keys())



def test_workbook_is_not_abstract():
    assert not inspect.isabstract(Workbook)


def test_workbook_constructor_exists():
    assert callable(Workbook.__init__)


def test_workbook_constructor_args():
    sig = inspect.signature(Workbook.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_DocumentPropertiesCollection)


def test_spreadsheetmlstyles_documentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLStyles_DocumentPropertiesCollection.__init__)


def test_spreadsheetmlstyles_documentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "lines" in params, "Missing parameter 'lines'"
    assert "description" in params, "Missing parameter 'description'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "company" in params, "Missing parameter 'company'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "author" in params, "Missing parameter 'author'"
    assert "revision" in params, "Missing parameter 'revision'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "title" in params, "Missing parameter 'title'"
    assert "words" in params, "Missing parameter 'words'"
    assert "bytes" in params, "Missing parameter 'bytes'"

def test_spreadsheetmlstyles_documentpropertiescollection_has_category():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_keywords():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_appName():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_pages():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_manager():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_characters():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_lines():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_description():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_totalTime():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_company():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_paragraphs():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_author():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_revision():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_lastAuthor():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_subject():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_presentationFormat():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_guid():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_title():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_words():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_documentpropertiescollection_has_bytes():
    assert hasattr(SpreadsheetMLStyles_DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in SpreadsheetMLStyles_DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DateTimeType)


def test_datetimetype_constructor_exists():
    assert callable(DateTimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_numbervalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_NumberValue)


def test_spreadsheetmlstyles_numbervalue_constructor_exists():
    assert callable(SpreadsheetMLStyles_NumberValue.__init__)


def test_spreadsheetmlstyles_numbervalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlstyles_numbervalue_has_value():
    assert hasattr(SpreadsheetMLStyles_NumberValue, "value")
    descriptor = None
    for klass in SpreadsheetMLStyles_NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_errorvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_ErrorValue)


def test_spreadsheetmlstyles_errorvalue_constructor_exists():
    assert callable(SpreadsheetMLStyles_ErrorValue.__init__)


def test_spreadsheetmlstyles_errorvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_DateTimeTypeValue)


def test_spreadsheetmlstyles_datetimetypevalue_constructor_exists():
    assert callable(SpreadsheetMLStyles_DateTimeTypeValue.__init__)


def test_spreadsheetmlstyles_datetimetypevalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_BooleanValue)


def test_spreadsheetmlstyles_booleanvalue_constructor_exists():
    assert callable(SpreadsheetMLStyles_BooleanValue.__init__)


def test_spreadsheetmlstyles_booleanvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlstyles_booleanvalue_has_value():
    assert hasattr(SpreadsheetMLStyles_BooleanValue, "value")
    descriptor = None
    for klass in SpreadsheetMLStyles_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_stringvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_StringValue)


def test_spreadsheetmlstyles_stringvalue_constructor_exists():
    assert callable(SpreadsheetMLStyles_StringValue.__init__)


def test_spreadsheetmlstyles_stringvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlstyles_stringvalue_has_value():
    assert hasattr(SpreadsheetMLStyles_StringValue, "value")
    descriptor = None
    for klass in SpreadsheetMLStyles_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_valuetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_ValueType)


def test_spreadsheetmlstyles_valuetype_constructor_exists():
    assert callable(SpreadsheetMLStyles_ValueType.__init__)


def test_spreadsheetmlstyles_valuetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles_versiontype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_VersionType)


def test_spreadsheetmlstyles_versiontype_constructor_exists():
    assert callable(SpreadsheetMLStyles_VersionType.__init__)


def test_spreadsheetmlstyles_versiontype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "nn" in params, "Missing parameter 'nn'"
    assert "n" in params, "Missing parameter 'n'"

def test_spreadsheetmlstyles_versiontype_has_nn():
    assert hasattr(SpreadsheetMLStyles_VersionType, "nn")
    descriptor = None
    for klass in SpreadsheetMLStyles_VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_versiontype_has_n():
    assert hasattr(SpreadsheetMLStyles_VersionType, "n")
    descriptor = None
    for klass in SpreadsheetMLStyles_VersionType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles_datetimetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles_DateTimeType)


def test_spreadsheetmlstyles_datetimetype_constructor_exists():
    assert callable(SpreadsheetMLStyles_DateTimeType.__init__)


def test_spreadsheetmlstyles_datetimetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "minute" in params, "Missing parameter 'minute'"
    assert "year" in params, "Missing parameter 'year'"
    assert "month" in params, "Missing parameter 'month'"
    assert "day" in params, "Missing parameter 'day'"
    assert "second" in params, "Missing parameter 'second'"
    assert "hour" in params, "Missing parameter 'hour'"

def test_spreadsheetmlstyles_datetimetype_has_minute():
    assert hasattr(SpreadsheetMLStyles_DateTimeType, "minute")
    descriptor = None
    for klass in SpreadsheetMLStyles_DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_datetimetype_has_year():
    assert hasattr(SpreadsheetMLStyles_DateTimeType, "year")
    descriptor = None
    for klass in SpreadsheetMLStyles_DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_datetimetype_has_month():
    assert hasattr(SpreadsheetMLStyles_DateTimeType, "month")
    descriptor = None
    for klass in SpreadsheetMLStyles_DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_datetimetype_has_day():
    assert hasattr(SpreadsheetMLStyles_DateTimeType, "day")
    descriptor = None
    for klass in SpreadsheetMLStyles_DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_datetimetype_has_second():
    assert hasattr(SpreadsheetMLStyles_DateTimeType, "second")
    descriptor = None
    for klass in SpreadsheetMLStyles_DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles_datetimetype_has_hour():
    assert hasattr(SpreadsheetMLStyles_DateTimeType, "hour")
    descriptor = None
    for klass in SpreadsheetMLStyles_DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_positiontype_exists():
    # Check that the Enumeration exists
    assert PositionType is not None

def test_positiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PositionType]
    expected_literals = [
        "pt_Top",
        "pt_Right",
        "pt_Left",
        "pt_Bottom",
        "pt_DiagonalLeft",
        "pt_DiagonalRight",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PositionType"

def test_excelnumberformattype_exists():
    # Check that the Enumeration exists
    assert ExcelNumberFormatType is not None

def test_excelnumberformattype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExcelNumberFormatType]
    expected_literals = [
        "enft_On_Off",
        "enft_General",
        "enft_Euro_Currency",
        "enft_Medium_Time",
        "enft_Long_Date",
        "enft_Percent",
        "enft_General_Date",
        "enft_Short_Time",
        "enft_Currency",
        "enft_General_Number",
        "enft_Scientific",
        "enft_Fixed",
        "enft_Long_Time",
        "enft_Standard",
        "enft_Yes_No",
        "enft_Medium_Date",
        "enft_Short_Date",
        "enft_True_False",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExcelNumberFormatType"

def test_commentslayouttype_exists():
    # Check that the Enumeration exists
    assert CommentsLayoutType is not None

def test_commentslayouttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CommentsLayoutType]
    expected_literals = [
        "clt_SheetEnd",
        "clt_PrintNone",
        "clt_InPlace",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CommentsLayoutType"

def test_visibletype_exists():
    # Check that the Enumeration exists
    assert VisibleType is not None

def test_visibletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibleType]
    expected_literals = [
        "vt_SheetHidden",
        "vt_SheetVeryHidden",
        "vt_SheetVisible",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibleType"

def test_horizontalalignementtype_exists():
    # Check that the Enumeration exists
    assert HorizontalAlignementType is not None

def test_horizontalalignementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HorizontalAlignementType]
    expected_literals = [
        "hat_Fill",
        "hat_Left",
        "hat_Center",
        "hat_JustifyDistributed",
        "hat_Automatic",
        "hat_Right",
        "hat_CenterAcrossSelection",
        "hat_Justify",
        "hat_Distributed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HorizontalAlignementType"

def test_excelworksheettypetype_exists():
    # Check that the Enumeration exists
    assert ExcelWorksheetTypeType is not None

def test_excelworksheettypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExcelWorksheetTypeType]
    expected_literals = [
        "ewt_Chart",
        "ewt_Worksheet",
        "ewt_Dialog",
        "ewt_Macro",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExcelWorksheetTypeType"

def test_displaydrawingobjectstype_exists():
    # Check that the Enumeration exists
    assert DisplayDrawingObjectsType is not None

def test_displaydrawingobjectstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DisplayDrawingObjectsType]
    expected_literals = [
        "ddot_hideAll",
        "ddot_displayShapes",
        "ddot_placeHolders",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DisplayDrawingObjectsType"

def test_linestyletype_exists():
    # Check that the Enumeration exists
    assert LineStyleType is not None

def test_linestyletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyleType]
    expected_literals = [
        "lst_Dash",
        "lst_Dot",
        "lst_Double",
        "lst_Continuous",
        "lst_DashDotDot",
        "lst_SlantDashDot",
        "lst_None",
        "lst_DashDot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyleType"

def test_underlinetype_exists():
    # Check that the Enumeration exists
    assert UnderlineType is not None

def test_underlinetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnderlineType]
    expected_literals = [
        "ut_DoubleAccounting",
        "ut_SingleAccounting",
        "ut_Double",
        "ut_Single",
        "ut_None",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnderlineType"

def test_calculationworkbooktype_exists():
    # Check that the Enumeration exists
    assert CalculationWorkbookType is not None

def test_calculationworkbooktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CalculationWorkbookType]
    expected_literals = [
        "cwt_automaticCalculation",
        "cwt_semiAutomaticCalculation",
        "cwt_manualCalculation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CalculationWorkbookType"

def test_readingordertype_exists():
    # Check that the Enumeration exists
    assert ReadingOrderType is not None

def test_readingordertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReadingOrderType]
    expected_literals = [
        "rot_RightToLeft",
        "rot_LeftToRight",
        "rot_Context",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReadingOrderType"

def test_enableselectiontype_exists():
    # Check that the Enumeration exists
    assert EnableSelectionType is not None

def test_enableselectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnableSelectionType]
    expected_literals = [
        "est_NoSelection",
        "est_UnlockedCells",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnableSelectionType"

def test_orientationtype_exists():
    # Check that the Enumeration exists
    assert OrientationType is not None

def test_orientationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrientationType]
    expected_literals = [
        "ot_Landscape",
        "ot_Portrait",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrientationType"

def test_verticalaligntype_exists():
    # Check that the Enumeration exists
    assert VerticalAlignType is not None

def test_verticalaligntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VerticalAlignType]
    expected_literals = [
        "vat_Subscript",
        "vat_None",
        "vat_Superscript",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VerticalAlignType"

def test_patterntype_exists():
    # Check that the Enumeration exists
    assert PatternType is not None

def test_patterntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PatternType]
    expected_literals = [
        "pt_ThinDiagStripe",
        "pt_Gray125",
        "pt_ThinVertStripe",
        "pt_DiagCross",
        "pt_ReverseDiagStripe",
        "pt_Solid",
        "pt_ThinHorzCross",
        "pt_HorzStripe",
        "pt_ThinReverseDiagStripe",
        "pt_VertStripe",
        "pt_None",
        "pt_Gray75",
        "pt_Gray0625",
        "pt_ThinHorzStripe",
        "pt_DiagStripe",
        "pt_ThickDiagCross",
        "pt_Gray25",
        "pt_Gray50",
        "pt_ThinDiagCross",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PatternType"

def test_verticalalignementtype_exists():
    # Check that the Enumeration exists
    assert VerticalAlignementType is not None

def test_verticalalignementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VerticalAlignementType]
    expected_literals = [
        "vat_Top",
        "vat_Center",
        "vat_Distributed",
        "vat_JustifyDistributed",
        "vat_Justify",
        "vat_Automatic",
        "vat_Bottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VerticalAlignementType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
SpreadsheetMLStyles_NamedRange_strategy = st.builds(
    SpreadsheetMLStyles_NamedRange,
    refersTo=
        safe_text,
    hidden=
        safe_text,
    name=
        safe_text
)
SpreadsheetMLStyles_NamesType_strategy = st.builds(
    SpreadsheetMLStyles_NamesType,
)
NamedRange_strategy = st.builds(
    NamedRange,
)
SpreadsheetMLStyles_NumberFormatType_strategy = st.builds(
    SpreadsheetMLStyles_NumberFormatType,
    format=
        safe_text
)
SpreadsheetMLStyles_InteriorType_strategy = st.builds(
    SpreadsheetMLStyles_InteriorType,
    color=
        safe_text,
    patternColor=
        safe_text,
    pattern=
        safe_text
)
SpreadsheetMLStyles_FontType_strategy = st.builds(
    SpreadsheetMLStyles_FontType,
    bold=
        safe_text,
    shadow=
        safe_text,
    verticalAlign=
        safe_text,
    underline=
        safe_text,
    size=
        safe_text,
    color=
        safe_text,
    fontName=
        safe_text,
    strikeThrough=
        safe_text,
    italic=
        safe_text,
    outline=
        safe_text
)
BorderType_strategy = st.builds(
    BorderType,
)
SpreadsheetMLStyles_BordersType_strategy = st.builds(
    SpreadsheetMLStyles_BordersType,
)
SpreadsheetMLStyles_BorderType_strategy = st.builds(
    SpreadsheetMLStyles_BorderType,
    weight=
        safe_text,
    lineStyle=
        safe_text,
    color=
        safe_text,
    position=
        safe_text
)
SpreadsheetMLStyles_AlignmentType_strategy = st.builds(
    SpreadsheetMLStyles_AlignmentType,
    horizontal=
        safe_text,
    shrinkToFit=
        safe_text,
    verticalText=
        safe_text,
    rotate=
        safe_text,
    wrapText=
        safe_text,
    readingOrder=
        safe_text,
    indent=
        safe_text,
    vertical=
        safe_text
)
FontType_strategy = st.builds(
    FontType,
)
SpreadsheetMLStyles_ProtectionType_strategy = st.builds(
    SpreadsheetMLStyles_ProtectionType,
    protected=
        safe_text
)
ProtectionType_strategy = st.builds(
    ProtectionType,
)
NumberFormatType_strategy = st.builds(
    NumberFormatType,
)
InteriorType_strategy = st.builds(
    InteriorType,
)
BordersType_strategy = st.builds(
    BordersType,
)
AlignmentType_strategy = st.builds(
    AlignmentType,
)
SpreadsheetMLStyles_StyleType_strategy = st.builds(
    SpreadsheetMLStyles_StyleType,
    id=
        safe_text,
    name=
        safe_text
)
SpreadsheetMLStyles_StylesCollection_strategy = st.builds(
    SpreadsheetMLStyles_StylesCollection,
)
SpreadsheetMLStyles_Print_strategy = st.builds(
    SpreadsheetMLStyles_Print,
    leftToRight=
        safe_text,
    validPrinterInfo=
        safe_text,
    printErrors=
        safe_text,
    paperSizeIndex=
        safe_text,
    verticalResolution=
        safe_text,
    fitHeight=
        safe_text,
    fitWidth=
        safe_text,
    gridlines=
        safe_text,
    horizontalResolution=
        safe_text,
    commentsLayout=
        safe_text,
    scale=
        safe_text,
    rowColHeadings=
        safe_text,
    draftQuality=
        safe_text,
    blackAndWhite=
        safe_text,
    numberOfCopies=
        safe_text
)
SpreadsheetMLStyles_PageMarginsInfo_strategy = st.builds(
    SpreadsheetMLStyles_PageMarginsInfo,
    top=
        safe_text,
    bottom=
        safe_text,
    right=
        safe_text,
    left=
        safe_text
)
HeaderOrFooterElt_strategy = st.builds(
    HeaderOrFooterElt,
)
SpreadsheetMLStyles_Footer_strategy = st.builds(
    SpreadsheetMLStyles_Footer,
)
SpreadsheetMLStyles_Header_strategy = st.builds(
    SpreadsheetMLStyles_Header,
)
SpreadsheetMLStyles_HeaderOrFooterElt_strategy = st.builds(
    SpreadsheetMLStyles_HeaderOrFooterElt,
    margin=
        safe_text,
    data=
        safe_text
)
Layout_strategy = st.builds(
    Layout,
)
SpreadsheetMLStyles_PageSetup_strategy = st.builds(
    SpreadsheetMLStyles_PageSetup,
)
SpreadsheetMLStyles_Layout_strategy = st.builds(
    SpreadsheetMLStyles_Layout,
    orientation=
        safe_text,
    centerHorizontal=
        safe_text,
    centerVertical=
        safe_text,
    startPageNumber=
        safe_text
)
PageMarginsInfo_strategy = st.builds(
    PageMarginsInfo,
)
Footer_strategy = st.builds(
    Footer,
)
Header_strategy = st.builds(
    Header,
)
Print_strategy = st.builds(
    Print,
)
PageSetup_strategy = st.builds(
    PageSetup,
)
SpreadsheetMLStyles_WorksheetOptionsElt_strategy = st.builds(
    SpreadsheetMLStyles_WorksheetOptionsElt,
    rangeSelection=
        safe_text,
    applyAutomaticOutlineStyles=
        safe_text,
    fitToPage=
        safe_text,
    freezePanes=
        safe_text,
    defaultRowHeight=
        safe_text,
    filterOn=
        safe_text,
    leftColumnRightPane=
        safe_text,
    allowInsertRows=
        safe_text,
    doNotDisplayRowHeaders=
        safe_text,
    allowUsePivotTables=
        safe_text,
    noSummaryRowsBelowDetail=
        safe_text,
    gridlineColor=
        safe_text,
    intlMacro=
        safe_text,
    visible=
        safe_text,
    activePane=
        safe_text,
    allowSizeRows=
        safe_text,
    displayRightToLeft=
        safe_text,
    transitionFormulaEntry=
        safe_text,
    leftColumnVisible=
        safe_text,
    allowSizeCols=
        safe_text,
    pageBreakZoom=
        safe_text,
    doNotDisplayZeros=
        safe_text,
    excelWorksheetType=
        safe_text,
    doNotDisplayOutline=
        safe_text,
    defaultColumnWidth=
        safe_text,
    allowDeleteCols=
        safe_text,
    doNotDisplayColHeaders=
        safe_text,
    noSummaryColumnsRightDetail=
        safe_text,
    allowFilter=
        safe_text,
    allowDeleteRows=
        safe_text,
    splitHorizontal=
        safe_text,
    selected=
        safe_text,
    splitVertical=
        safe_text,
    allowFormatCells=
        safe_text,
    gridlineColorIndex=
        safe_text,
    tabColorIndex=
        safe_text,
    zoom=
        safe_text,
    topRowVisible=
        safe_text,
    codeName=
        safe_text,
    allowInsertHyperlinks=
        safe_text,
    topRowBottomPane=
        safe_text,
    allowSort=
        safe_text,
    doNotDisplayHeadings=
        safe_text,
    allowInsertCols=
        safe_text,
    doNotDisplayGridlines=
        safe_text,
    activeColumn=
        safe_text,
    showPageBreakZoom=
        safe_text,
    protectScenarios=
        safe_text,
    name=
        safe_text,
    transitionExpressionEvaluation=
        safe_text,
    protectContentst=
        safe_text,
    activeRow=
        safe_text,
    displayPageBreak=
        safe_text,
    enableSelection=
        safe_text,
    unsynced=
        safe_text,
    displayFormulas=
        safe_text,
    standardWidth=
        safe_text,
    protectObjects=
        safe_text,
    frozenNoSplit=
        safe_text
)
SpreadsheetMLStyles_ExcelWorkbook_strategy = st.builds(
    SpreadsheetMLStyles_ExcelWorkbook,
    hideWorkbookTabs=
        safe_text,
    selectedSheets=
        safe_text,
    hideVerticalScrollBar=
        safe_text,
    futureVer=
        safe_text,
    activeChart=
        safe_text,
    iteration=
        safe_text,
    uncalced=
        safe_text,
    windowTopY=
        safe_text,
    hidePivotTableFieldList=
        safe_text,
    windowIconic=
        safe_text,
    windowWidth=
        safe_text,
    precisionAsDisplayed=
        safe_text,
    refModeR1C1=
        safe_text,
    calculation=
        safe_text,
    date1904=
        safe_text,
    maxIterations=
        safe_text,
    tabRatio=
        safe_text,
    displayInkNotes=
        safe_text,
    windowTopX=
        safe_text,
    windowHeight=
        safe_text,
    hideHorizontalScrollBar=
        safe_text,
    activeSheet=
        safe_text,
    createBackup=
        safe_text,
    noAutoRecover=
        safe_text,
    embedSaveSmartTags=
        safe_text,
    acceptLabelsInFormulas=
        safe_text,
    doNotCalculateBeforeSave=
        safe_text,
    displayDrawingObjects=
        safe_text,
    protectWindows=
        safe_text,
    protectStructure=
        safe_text,
    maxChange=
        safe_text,
    windowHidden=
        safe_text,
    firstVisibleSheet=
        safe_text,
    doNotSaveLinkValues=
        safe_text
)
SpreadsheetMLStyles_Data_strategy = st.builds(
    SpreadsheetMLStyles_Data,
)
Comment_strategy = st.builds(
    Comment,
)
SpreadsheetMLStyles_Comment_strategy = st.builds(
    SpreadsheetMLStyles_Comment,
    showAlways=
        safe_text,
    author=
        safe_text
)
ColOrRowElement_strategy = st.builds(
    ColOrRowElement,
)
SpreadsheetMLStyles_Column_strategy = st.builds(
    SpreadsheetMLStyles_Column,
    autoFitWidth=
        safe_text,
    width=
        safe_text
)
TableElement_strategy = st.builds(
    TableElement,
)
SpreadsheetMLStyles_Cell_strategy = st.builds(
    SpreadsheetMLStyles_Cell,
    mergeAcross=
        safe_text,
    arrayRange=
        safe_text,
    formula=
        safe_text,
    mergeDown=
        safe_text,
    hRef=
        safe_text
)
SpreadsheetMLStyles_ColOrRowElement_strategy = st.builds(
    SpreadsheetMLStyles_ColOrRowElement,
    span=
        safe_text,
    hidden=
        safe_text
)
SpreadsheetMLStyles_Row_strategy = st.builds(
    SpreadsheetMLStyles_Row,
    height=
        safe_text,
    autoFitHeight=
        safe_text
)
Row_strategy = st.builds(
    Row,
)
Column_strategy = st.builds(
    Column,
)
StyledElement_strategy = st.builds(
    StyledElement,
)
SpreadsheetMLStyles_TableElement_strategy = st.builds(
    SpreadsheetMLStyles_TableElement,
    index=
        safe_text
)
StyleType_strategy = st.builds(
    StyleType,
)
SpreadsheetMLStyles_StyledElement_strategy = st.builds(
    SpreadsheetMLStyles_StyledElement,
)
WorksheetOptionsElt_strategy = st.builds(
    WorksheetOptionsElt,
)
Table_strategy = st.builds(
    Table,
)
SpreadsheetMLStyles_Worksheet_strategy = st.builds(
    SpreadsheetMLStyles_Worksheet,
    protected=
        safe_text,
    rightToLeft=
        safe_text,
    name=
        safe_text
)
SpreadsheetMLStyles_Table_strategy = st.builds(
    SpreadsheetMLStyles_Table,
    fullColumns=
        safe_text,
    topCell=
        safe_text,
    fullRows=
        safe_text,
    leftCell=
        safe_text,
    expandedRowCount=
        safe_text,
    defaultRowHeight=
        safe_text,
    expandedColumnCount=
        safe_text,
    defaultColumnWidth=
        safe_text
)
NamesType_strategy = st.builds(
    NamesType,
)
StylesCollection_strategy = st.builds(
    StylesCollection,
)
ExcelWorkbook_strategy = st.builds(
    ExcelWorkbook,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
Worksheet_strategy = st.builds(
    Worksheet,
)
SmartTagType_strategy = st.builds(
    SmartTagType,
)
Cell_strategy = st.builds(
    Cell,
)
SpreadsheetMLStyles_SmartTagsCollection_strategy = st.builds(
    SpreadsheetMLStyles_SmartTagsCollection,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)
SpreadsheetMLStyles_SmartTagType_strategy = st.builds(
    SpreadsheetMLStyles_SmartTagType,
    name=
        safe_text,
    namespaceuri=
        safe_text,
    url=
        safe_text
)
SpreadsheetMLStyles_Workbook_strategy = st.builds(
    SpreadsheetMLStyles_Workbook,
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
SpreadsheetMLStyles_CustomDocumentProperty_strategy = st.builds(
    SpreadsheetMLStyles_CustomDocumentProperty,
    name=
        safe_text
)
CustomDocumentProperty_strategy = st.builds(
    CustomDocumentProperty,
)
SpreadsheetMLStyles_CustomDocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLStyles_CustomDocumentPropertiesCollection,
)
VersionType_strategy = st.builds(
    VersionType,
)
Workbook_strategy = st.builds(
    Workbook,
)
SpreadsheetMLStyles_DocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLStyles_DocumentPropertiesCollection,
    category=
        safe_text,
    keywords=
        safe_text,
    appName=
        safe_text,
    pages=
        safe_text,
    manager=
        safe_text,
    hyperlinkBase=
        safe_text,
    characters=
        safe_text,
    lines=
        safe_text,
    description=
        safe_text,
    charactersWithSpaces=
        safe_text,
    totalTime=
        safe_text,
    company=
        safe_text,
    paragraphs=
        safe_text,
    author=
        safe_text,
    revision=
        safe_text,
    lastAuthor=
        safe_text,
    subject=
        safe_text,
    presentationFormat=
        safe_text,
    guid=
        safe_text,
    title=
        safe_text,
    words=
        safe_text,
    bytes=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
ValueType_strategy = st.builds(
    ValueType,
)
SpreadsheetMLStyles_NumberValue_strategy = st.builds(
    SpreadsheetMLStyles_NumberValue,
    value=
        safe_text
)
SpreadsheetMLStyles_ErrorValue_strategy = st.builds(
    SpreadsheetMLStyles_ErrorValue,
)
SpreadsheetMLStyles_DateTimeTypeValue_strategy = st.builds(
    SpreadsheetMLStyles_DateTimeTypeValue,
)
SpreadsheetMLStyles_BooleanValue_strategy = st.builds(
    SpreadsheetMLStyles_BooleanValue,
    value=
        safe_text
)
SpreadsheetMLStyles_StringValue_strategy = st.builds(
    SpreadsheetMLStyles_StringValue,
    value=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
SpreadsheetMLStyles_ValueType_strategy = st.builds(
    SpreadsheetMLStyles_ValueType,
)
SpreadsheetMLStyles_VersionType_strategy = st.builds(
    SpreadsheetMLStyles_VersionType,
    nn=
        safe_text,
    n=
        safe_text
)
SpreadsheetMLStyles_DateTimeType_strategy = st.builds(
    SpreadsheetMLStyles_DateTimeType,
    minute=
        safe_text,
    year=
        safe_text,
    month=
        safe_text,
    day=
        safe_text,
    second=
        safe_text,
    hour=
        safe_text
)

@given(instance=SpreadsheetMLStyles_NamedRange_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_namedrange_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_NamedRange)



@given(instance=SpreadsheetMLStyles_NamedRange_strategy)
def test_spreadsheetmlstyles_namedrange_refersTo_setter(instance):
    original = instance.refersTo
    instance.refersTo = original
    assert instance.refersTo == original



@given(instance=SpreadsheetMLStyles_NamedRange_strategy)
def test_spreadsheetmlstyles_namedrange_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original



@given(instance=SpreadsheetMLStyles_NamedRange_strategy)
def test_spreadsheetmlstyles_namedrange_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLStyles_NamesType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_namestype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_NamesType)

@given(instance=NamedRange_strategy)
@settings(max_examples=50)
def test_namedrange_instantiation(instance):
    assert isinstance(instance, NamedRange)

@given(instance=SpreadsheetMLStyles_NumberFormatType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_numberformattype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_NumberFormatType)



@given(instance=SpreadsheetMLStyles_NumberFormatType_strategy)
def test_spreadsheetmlstyles_numberformattype_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=SpreadsheetMLStyles_InteriorType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_interiortype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_InteriorType)



@given(instance=SpreadsheetMLStyles_InteriorType_strategy)
def test_spreadsheetmlstyles_interiortype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=SpreadsheetMLStyles_InteriorType_strategy)
def test_spreadsheetmlstyles_interiortype_patternColor_setter(instance):
    original = instance.patternColor
    instance.patternColor = original
    assert instance.patternColor == original



@given(instance=SpreadsheetMLStyles_InteriorType_strategy)
def test_spreadsheetmlstyles_interiortype_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=SpreadsheetMLStyles_FontType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_fonttype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_FontType)



@given(instance=SpreadsheetMLStyles_FontType_strategy)
def test_spreadsheetmlstyles_fonttype_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original



@given(instance=SpreadsheetMLStyles_FontType_strategy)
def test_spreadsheetmlstyles_fonttype_shadow_setter(instance):
    original = instance.shadow
    instance.shadow = original
    assert instance.shadow == original



@given(instance=SpreadsheetMLStyles_FontType_strategy)
def test_spreadsheetmlstyles_fonttype_verticalAlign_setter(instance):
    original = instance.verticalAlign
    instance.verticalAlign = original
    assert instance.verticalAlign == original



@given(instance=SpreadsheetMLStyles_FontType_strategy)
def test_spreadsheetmlstyles_fonttype_underline_setter(instance):
    original = instance.underline
    instance.underline = original
    assert instance.underline == original



@given(instance=SpreadsheetMLStyles_FontType_strategy)
def test_spreadsheetmlstyles_fonttype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=SpreadsheetMLStyles_FontType_strategy)
def test_spreadsheetmlstyles_fonttype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=SpreadsheetMLStyles_FontType_strategy)
def test_spreadsheetmlstyles_fonttype_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original



@given(instance=SpreadsheetMLStyles_FontType_strategy)
def test_spreadsheetmlstyles_fonttype_strikeThrough_setter(instance):
    original = instance.strikeThrough
    instance.strikeThrough = original
    assert instance.strikeThrough == original



@given(instance=SpreadsheetMLStyles_FontType_strategy)
def test_spreadsheetmlstyles_fonttype_italic_setter(instance):
    original = instance.italic
    instance.italic = original
    assert instance.italic == original



@given(instance=SpreadsheetMLStyles_FontType_strategy)
def test_spreadsheetmlstyles_fonttype_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original

@given(instance=BorderType_strategy)
@settings(max_examples=50)
def test_bordertype_instantiation(instance):
    assert isinstance(instance, BorderType)

@given(instance=SpreadsheetMLStyles_BordersType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_borderstype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_BordersType)

@given(instance=SpreadsheetMLStyles_BorderType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_bordertype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_BorderType)



@given(instance=SpreadsheetMLStyles_BorderType_strategy)
def test_spreadsheetmlstyles_bordertype_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=SpreadsheetMLStyles_BorderType_strategy)
def test_spreadsheetmlstyles_bordertype_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=SpreadsheetMLStyles_BorderType_strategy)
def test_spreadsheetmlstyles_bordertype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=SpreadsheetMLStyles_BorderType_strategy)
def test_spreadsheetmlstyles_bordertype_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=SpreadsheetMLStyles_AlignmentType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_alignmenttype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_AlignmentType)



@given(instance=SpreadsheetMLStyles_AlignmentType_strategy)
def test_spreadsheetmlstyles_alignmenttype_horizontal_setter(instance):
    original = instance.horizontal
    instance.horizontal = original
    assert instance.horizontal == original



@given(instance=SpreadsheetMLStyles_AlignmentType_strategy)
def test_spreadsheetmlstyles_alignmenttype_shrinkToFit_setter(instance):
    original = instance.shrinkToFit
    instance.shrinkToFit = original
    assert instance.shrinkToFit == original



@given(instance=SpreadsheetMLStyles_AlignmentType_strategy)
def test_spreadsheetmlstyles_alignmenttype_verticalText_setter(instance):
    original = instance.verticalText
    instance.verticalText = original
    assert instance.verticalText == original



@given(instance=SpreadsheetMLStyles_AlignmentType_strategy)
def test_spreadsheetmlstyles_alignmenttype_rotate_setter(instance):
    original = instance.rotate
    instance.rotate = original
    assert instance.rotate == original



@given(instance=SpreadsheetMLStyles_AlignmentType_strategy)
def test_spreadsheetmlstyles_alignmenttype_wrapText_setter(instance):
    original = instance.wrapText
    instance.wrapText = original
    assert instance.wrapText == original



@given(instance=SpreadsheetMLStyles_AlignmentType_strategy)
def test_spreadsheetmlstyles_alignmenttype_readingOrder_setter(instance):
    original = instance.readingOrder
    instance.readingOrder = original
    assert instance.readingOrder == original



@given(instance=SpreadsheetMLStyles_AlignmentType_strategy)
def test_spreadsheetmlstyles_alignmenttype_indent_setter(instance):
    original = instance.indent
    instance.indent = original
    assert instance.indent == original



@given(instance=SpreadsheetMLStyles_AlignmentType_strategy)
def test_spreadsheetmlstyles_alignmenttype_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original

@given(instance=FontType_strategy)
@settings(max_examples=50)
def test_fonttype_instantiation(instance):
    assert isinstance(instance, FontType)

@given(instance=SpreadsheetMLStyles_ProtectionType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_protectiontype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_ProtectionType)



@given(instance=SpreadsheetMLStyles_ProtectionType_strategy)
def test_spreadsheetmlstyles_protectiontype_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=ProtectionType_strategy)
@settings(max_examples=50)
def test_protectiontype_instantiation(instance):
    assert isinstance(instance, ProtectionType)

@given(instance=NumberFormatType_strategy)
@settings(max_examples=50)
def test_numberformattype_instantiation(instance):
    assert isinstance(instance, NumberFormatType)

@given(instance=InteriorType_strategy)
@settings(max_examples=50)
def test_interiortype_instantiation(instance):
    assert isinstance(instance, InteriorType)

@given(instance=BordersType_strategy)
@settings(max_examples=50)
def test_borderstype_instantiation(instance):
    assert isinstance(instance, BordersType)

@given(instance=AlignmentType_strategy)
@settings(max_examples=50)
def test_alignmenttype_instantiation(instance):
    assert isinstance(instance, AlignmentType)

@given(instance=SpreadsheetMLStyles_StyleType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_styletype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_StyleType)



@given(instance=SpreadsheetMLStyles_StyleType_strategy)
def test_spreadsheetmlstyles_styletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=SpreadsheetMLStyles_StyleType_strategy)
def test_spreadsheetmlstyles_styletype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLStyles_StylesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_stylescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_StylesCollection)

@given(instance=SpreadsheetMLStyles_Print_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_print_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Print)



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_leftToRight_setter(instance):
    original = instance.leftToRight
    instance.leftToRight = original
    assert instance.leftToRight == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_validPrinterInfo_setter(instance):
    original = instance.validPrinterInfo
    instance.validPrinterInfo = original
    assert instance.validPrinterInfo == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_printErrors_setter(instance):
    original = instance.printErrors
    instance.printErrors = original
    assert instance.printErrors == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_paperSizeIndex_setter(instance):
    original = instance.paperSizeIndex
    instance.paperSizeIndex = original
    assert instance.paperSizeIndex == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_verticalResolution_setter(instance):
    original = instance.verticalResolution
    instance.verticalResolution = original
    assert instance.verticalResolution == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_fitHeight_setter(instance):
    original = instance.fitHeight
    instance.fitHeight = original
    assert instance.fitHeight == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_fitWidth_setter(instance):
    original = instance.fitWidth
    instance.fitWidth = original
    assert instance.fitWidth == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_gridlines_setter(instance):
    original = instance.gridlines
    instance.gridlines = original
    assert instance.gridlines == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_horizontalResolution_setter(instance):
    original = instance.horizontalResolution
    instance.horizontalResolution = original
    assert instance.horizontalResolution == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_commentsLayout_setter(instance):
    original = instance.commentsLayout
    instance.commentsLayout = original
    assert instance.commentsLayout == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_rowColHeadings_setter(instance):
    original = instance.rowColHeadings
    instance.rowColHeadings = original
    assert instance.rowColHeadings == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_draftQuality_setter(instance):
    original = instance.draftQuality
    instance.draftQuality = original
    assert instance.draftQuality == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_blackAndWhite_setter(instance):
    original = instance.blackAndWhite
    instance.blackAndWhite = original
    assert instance.blackAndWhite == original



@given(instance=SpreadsheetMLStyles_Print_strategy)
def test_spreadsheetmlstyles_print_numberOfCopies_setter(instance):
    original = instance.numberOfCopies
    instance.numberOfCopies = original
    assert instance.numberOfCopies == original

@given(instance=SpreadsheetMLStyles_PageMarginsInfo_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_pagemarginsinfo_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_PageMarginsInfo)



@given(instance=SpreadsheetMLStyles_PageMarginsInfo_strategy)
def test_spreadsheetmlstyles_pagemarginsinfo_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original



@given(instance=SpreadsheetMLStyles_PageMarginsInfo_strategy)
def test_spreadsheetmlstyles_pagemarginsinfo_bottom_setter(instance):
    original = instance.bottom
    instance.bottom = original
    assert instance.bottom == original



@given(instance=SpreadsheetMLStyles_PageMarginsInfo_strategy)
def test_spreadsheetmlstyles_pagemarginsinfo_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original



@given(instance=SpreadsheetMLStyles_PageMarginsInfo_strategy)
def test_spreadsheetmlstyles_pagemarginsinfo_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=HeaderOrFooterElt_strategy)
@settings(max_examples=50)
def test_headerorfooterelt_instantiation(instance):
    assert isinstance(instance, HeaderOrFooterElt)

@given(instance=SpreadsheetMLStyles_Footer_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_footer_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Footer)

@given(instance=SpreadsheetMLStyles_Header_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_header_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Header)

@given(instance=SpreadsheetMLStyles_HeaderOrFooterElt_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_headerorfooterelt_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_HeaderOrFooterElt)



@given(instance=SpreadsheetMLStyles_HeaderOrFooterElt_strategy)
def test_spreadsheetmlstyles_headerorfooterelt_margin_setter(instance):
    original = instance.margin
    instance.margin = original
    assert instance.margin == original



@given(instance=SpreadsheetMLStyles_HeaderOrFooterElt_strategy)
def test_spreadsheetmlstyles_headerorfooterelt_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=SpreadsheetMLStyles_PageSetup_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_pagesetup_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_PageSetup)

@given(instance=SpreadsheetMLStyles_Layout_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_layout_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Layout)



@given(instance=SpreadsheetMLStyles_Layout_strategy)
def test_spreadsheetmlstyles_layout_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=SpreadsheetMLStyles_Layout_strategy)
def test_spreadsheetmlstyles_layout_centerHorizontal_setter(instance):
    original = instance.centerHorizontal
    instance.centerHorizontal = original
    assert instance.centerHorizontal == original



@given(instance=SpreadsheetMLStyles_Layout_strategy)
def test_spreadsheetmlstyles_layout_centerVertical_setter(instance):
    original = instance.centerVertical
    instance.centerVertical = original
    assert instance.centerVertical == original



@given(instance=SpreadsheetMLStyles_Layout_strategy)
def test_spreadsheetmlstyles_layout_startPageNumber_setter(instance):
    original = instance.startPageNumber
    instance.startPageNumber = original
    assert instance.startPageNumber == original

@given(instance=PageMarginsInfo_strategy)
@settings(max_examples=50)
def test_pagemarginsinfo_instantiation(instance):
    assert isinstance(instance, PageMarginsInfo)

@given(instance=Footer_strategy)
@settings(max_examples=50)
def test_footer_instantiation(instance):
    assert isinstance(instance, Footer)

@given(instance=Header_strategy)
@settings(max_examples=50)
def test_header_instantiation(instance):
    assert isinstance(instance, Header)

@given(instance=Print_strategy)
@settings(max_examples=50)
def test_print_instantiation(instance):
    assert isinstance(instance, Print)

@given(instance=PageSetup_strategy)
@settings(max_examples=50)
def test_pagesetup_instantiation(instance):
    assert isinstance(instance, PageSetup)

@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_worksheetoptionselt_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_WorksheetOptionsElt)



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_rangeSelection_setter(instance):
    original = instance.rangeSelection
    instance.rangeSelection = original
    assert instance.rangeSelection == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_applyAutomaticOutlineStyles_setter(instance):
    original = instance.applyAutomaticOutlineStyles
    instance.applyAutomaticOutlineStyles = original
    assert instance.applyAutomaticOutlineStyles == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_fitToPage_setter(instance):
    original = instance.fitToPage
    instance.fitToPage = original
    assert instance.fitToPage == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_freezePanes_setter(instance):
    original = instance.freezePanes
    instance.freezePanes = original
    assert instance.freezePanes == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_filterOn_setter(instance):
    original = instance.filterOn
    instance.filterOn = original
    assert instance.filterOn == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_leftColumnRightPane_setter(instance):
    original = instance.leftColumnRightPane
    instance.leftColumnRightPane = original
    assert instance.leftColumnRightPane == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_allowInsertRows_setter(instance):
    original = instance.allowInsertRows
    instance.allowInsertRows = original
    assert instance.allowInsertRows == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_doNotDisplayRowHeaders_setter(instance):
    original = instance.doNotDisplayRowHeaders
    instance.doNotDisplayRowHeaders = original
    assert instance.doNotDisplayRowHeaders == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_allowUsePivotTables_setter(instance):
    original = instance.allowUsePivotTables
    instance.allowUsePivotTables = original
    assert instance.allowUsePivotTables == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_noSummaryRowsBelowDetail_setter(instance):
    original = instance.noSummaryRowsBelowDetail
    instance.noSummaryRowsBelowDetail = original
    assert instance.noSummaryRowsBelowDetail == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_gridlineColor_setter(instance):
    original = instance.gridlineColor
    instance.gridlineColor = original
    assert instance.gridlineColor == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_intlMacro_setter(instance):
    original = instance.intlMacro
    instance.intlMacro = original
    assert instance.intlMacro == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_activePane_setter(instance):
    original = instance.activePane
    instance.activePane = original
    assert instance.activePane == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_allowSizeRows_setter(instance):
    original = instance.allowSizeRows
    instance.allowSizeRows = original
    assert instance.allowSizeRows == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_displayRightToLeft_setter(instance):
    original = instance.displayRightToLeft
    instance.displayRightToLeft = original
    assert instance.displayRightToLeft == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_transitionFormulaEntry_setter(instance):
    original = instance.transitionFormulaEntry
    instance.transitionFormulaEntry = original
    assert instance.transitionFormulaEntry == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_leftColumnVisible_setter(instance):
    original = instance.leftColumnVisible
    instance.leftColumnVisible = original
    assert instance.leftColumnVisible == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_allowSizeCols_setter(instance):
    original = instance.allowSizeCols
    instance.allowSizeCols = original
    assert instance.allowSizeCols == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_pageBreakZoom_setter(instance):
    original = instance.pageBreakZoom
    instance.pageBreakZoom = original
    assert instance.pageBreakZoom == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_doNotDisplayZeros_setter(instance):
    original = instance.doNotDisplayZeros
    instance.doNotDisplayZeros = original
    assert instance.doNotDisplayZeros == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_excelWorksheetType_setter(instance):
    original = instance.excelWorksheetType
    instance.excelWorksheetType = original
    assert instance.excelWorksheetType == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_doNotDisplayOutline_setter(instance):
    original = instance.doNotDisplayOutline
    instance.doNotDisplayOutline = original
    assert instance.doNotDisplayOutline == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_allowDeleteCols_setter(instance):
    original = instance.allowDeleteCols
    instance.allowDeleteCols = original
    assert instance.allowDeleteCols == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_doNotDisplayColHeaders_setter(instance):
    original = instance.doNotDisplayColHeaders
    instance.doNotDisplayColHeaders = original
    assert instance.doNotDisplayColHeaders == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_noSummaryColumnsRightDetail_setter(instance):
    original = instance.noSummaryColumnsRightDetail
    instance.noSummaryColumnsRightDetail = original
    assert instance.noSummaryColumnsRightDetail == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_allowFilter_setter(instance):
    original = instance.allowFilter
    instance.allowFilter = original
    assert instance.allowFilter == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_allowDeleteRows_setter(instance):
    original = instance.allowDeleteRows
    instance.allowDeleteRows = original
    assert instance.allowDeleteRows == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_splitHorizontal_setter(instance):
    original = instance.splitHorizontal
    instance.splitHorizontal = original
    assert instance.splitHorizontal == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_splitVertical_setter(instance):
    original = instance.splitVertical
    instance.splitVertical = original
    assert instance.splitVertical == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_allowFormatCells_setter(instance):
    original = instance.allowFormatCells
    instance.allowFormatCells = original
    assert instance.allowFormatCells == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_gridlineColorIndex_setter(instance):
    original = instance.gridlineColorIndex
    instance.gridlineColorIndex = original
    assert instance.gridlineColorIndex == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_tabColorIndex_setter(instance):
    original = instance.tabColorIndex
    instance.tabColorIndex = original
    assert instance.tabColorIndex == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_topRowVisible_setter(instance):
    original = instance.topRowVisible
    instance.topRowVisible = original
    assert instance.topRowVisible == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_codeName_setter(instance):
    original = instance.codeName
    instance.codeName = original
    assert instance.codeName == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_allowInsertHyperlinks_setter(instance):
    original = instance.allowInsertHyperlinks
    instance.allowInsertHyperlinks = original
    assert instance.allowInsertHyperlinks == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_topRowBottomPane_setter(instance):
    original = instance.topRowBottomPane
    instance.topRowBottomPane = original
    assert instance.topRowBottomPane == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_allowSort_setter(instance):
    original = instance.allowSort
    instance.allowSort = original
    assert instance.allowSort == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_doNotDisplayHeadings_setter(instance):
    original = instance.doNotDisplayHeadings
    instance.doNotDisplayHeadings = original
    assert instance.doNotDisplayHeadings == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_allowInsertCols_setter(instance):
    original = instance.allowInsertCols
    instance.allowInsertCols = original
    assert instance.allowInsertCols == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_doNotDisplayGridlines_setter(instance):
    original = instance.doNotDisplayGridlines
    instance.doNotDisplayGridlines = original
    assert instance.doNotDisplayGridlines == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_activeColumn_setter(instance):
    original = instance.activeColumn
    instance.activeColumn = original
    assert instance.activeColumn == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_showPageBreakZoom_setter(instance):
    original = instance.showPageBreakZoom
    instance.showPageBreakZoom = original
    assert instance.showPageBreakZoom == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_protectScenarios_setter(instance):
    original = instance.protectScenarios
    instance.protectScenarios = original
    assert instance.protectScenarios == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_transitionExpressionEvaluation_setter(instance):
    original = instance.transitionExpressionEvaluation
    instance.transitionExpressionEvaluation = original
    assert instance.transitionExpressionEvaluation == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_protectContentst_setter(instance):
    original = instance.protectContentst
    instance.protectContentst = original
    assert instance.protectContentst == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_activeRow_setter(instance):
    original = instance.activeRow
    instance.activeRow = original
    assert instance.activeRow == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_displayPageBreak_setter(instance):
    original = instance.displayPageBreak
    instance.displayPageBreak = original
    assert instance.displayPageBreak == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_enableSelection_setter(instance):
    original = instance.enableSelection
    instance.enableSelection = original
    assert instance.enableSelection == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_unsynced_setter(instance):
    original = instance.unsynced
    instance.unsynced = original
    assert instance.unsynced == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_displayFormulas_setter(instance):
    original = instance.displayFormulas
    instance.displayFormulas = original
    assert instance.displayFormulas == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_standardWidth_setter(instance):
    original = instance.standardWidth
    instance.standardWidth = original
    assert instance.standardWidth == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_protectObjects_setter(instance):
    original = instance.protectObjects
    instance.protectObjects = original
    assert instance.protectObjects == original



@given(instance=SpreadsheetMLStyles_WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles_worksheetoptionselt_frozenNoSplit_setter(instance):
    original = instance.frozenNoSplit
    instance.frozenNoSplit = original
    assert instance.frozenNoSplit == original

@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_excelworkbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_ExcelWorkbook)



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_hideWorkbookTabs_setter(instance):
    original = instance.hideWorkbookTabs
    instance.hideWorkbookTabs = original
    assert instance.hideWorkbookTabs == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_selectedSheets_setter(instance):
    original = instance.selectedSheets
    instance.selectedSheets = original
    assert instance.selectedSheets == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_hideVerticalScrollBar_setter(instance):
    original = instance.hideVerticalScrollBar
    instance.hideVerticalScrollBar = original
    assert instance.hideVerticalScrollBar == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_futureVer_setter(instance):
    original = instance.futureVer
    instance.futureVer = original
    assert instance.futureVer == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_activeChart_setter(instance):
    original = instance.activeChart
    instance.activeChart = original
    assert instance.activeChart == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_iteration_setter(instance):
    original = instance.iteration
    instance.iteration = original
    assert instance.iteration == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_uncalced_setter(instance):
    original = instance.uncalced
    instance.uncalced = original
    assert instance.uncalced == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_windowTopY_setter(instance):
    original = instance.windowTopY
    instance.windowTopY = original
    assert instance.windowTopY == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_hidePivotTableFieldList_setter(instance):
    original = instance.hidePivotTableFieldList
    instance.hidePivotTableFieldList = original
    assert instance.hidePivotTableFieldList == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_windowIconic_setter(instance):
    original = instance.windowIconic
    instance.windowIconic = original
    assert instance.windowIconic == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_windowWidth_setter(instance):
    original = instance.windowWidth
    instance.windowWidth = original
    assert instance.windowWidth == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_precisionAsDisplayed_setter(instance):
    original = instance.precisionAsDisplayed
    instance.precisionAsDisplayed = original
    assert instance.precisionAsDisplayed == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_refModeR1C1_setter(instance):
    original = instance.refModeR1C1
    instance.refModeR1C1 = original
    assert instance.refModeR1C1 == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_calculation_setter(instance):
    original = instance.calculation
    instance.calculation = original
    assert instance.calculation == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_date1904_setter(instance):
    original = instance.date1904
    instance.date1904 = original
    assert instance.date1904 == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_maxIterations_setter(instance):
    original = instance.maxIterations
    instance.maxIterations = original
    assert instance.maxIterations == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_tabRatio_setter(instance):
    original = instance.tabRatio
    instance.tabRatio = original
    assert instance.tabRatio == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_displayInkNotes_setter(instance):
    original = instance.displayInkNotes
    instance.displayInkNotes = original
    assert instance.displayInkNotes == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_windowTopX_setter(instance):
    original = instance.windowTopX
    instance.windowTopX = original
    assert instance.windowTopX == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_windowHeight_setter(instance):
    original = instance.windowHeight
    instance.windowHeight = original
    assert instance.windowHeight == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_hideHorizontalScrollBar_setter(instance):
    original = instance.hideHorizontalScrollBar
    instance.hideHorizontalScrollBar = original
    assert instance.hideHorizontalScrollBar == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_activeSheet_setter(instance):
    original = instance.activeSheet
    instance.activeSheet = original
    assert instance.activeSheet == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_createBackup_setter(instance):
    original = instance.createBackup
    instance.createBackup = original
    assert instance.createBackup == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_noAutoRecover_setter(instance):
    original = instance.noAutoRecover
    instance.noAutoRecover = original
    assert instance.noAutoRecover == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_embedSaveSmartTags_setter(instance):
    original = instance.embedSaveSmartTags
    instance.embedSaveSmartTags = original
    assert instance.embedSaveSmartTags == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_acceptLabelsInFormulas_setter(instance):
    original = instance.acceptLabelsInFormulas
    instance.acceptLabelsInFormulas = original
    assert instance.acceptLabelsInFormulas == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_doNotCalculateBeforeSave_setter(instance):
    original = instance.doNotCalculateBeforeSave
    instance.doNotCalculateBeforeSave = original
    assert instance.doNotCalculateBeforeSave == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_displayDrawingObjects_setter(instance):
    original = instance.displayDrawingObjects
    instance.displayDrawingObjects = original
    assert instance.displayDrawingObjects == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_protectWindows_setter(instance):
    original = instance.protectWindows
    instance.protectWindows = original
    assert instance.protectWindows == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_protectStructure_setter(instance):
    original = instance.protectStructure
    instance.protectStructure = original
    assert instance.protectStructure == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_maxChange_setter(instance):
    original = instance.maxChange
    instance.maxChange = original
    assert instance.maxChange == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_windowHidden_setter(instance):
    original = instance.windowHidden
    instance.windowHidden = original
    assert instance.windowHidden == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_firstVisibleSheet_setter(instance):
    original = instance.firstVisibleSheet
    instance.firstVisibleSheet = original
    assert instance.firstVisibleSheet == original



@given(instance=SpreadsheetMLStyles_ExcelWorkbook_strategy)
def test_spreadsheetmlstyles_excelworkbook_doNotSaveLinkValues_setter(instance):
    original = instance.doNotSaveLinkValues
    instance.doNotSaveLinkValues = original
    assert instance.doNotSaveLinkValues == original

@given(instance=SpreadsheetMLStyles_Data_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_data_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Data)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=SpreadsheetMLStyles_Comment_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_comment_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Comment)



@given(instance=SpreadsheetMLStyles_Comment_strategy)
def test_spreadsheetmlstyles_comment_showAlways_setter(instance):
    original = instance.showAlways
    instance.showAlways = original
    assert instance.showAlways == original



@given(instance=SpreadsheetMLStyles_Comment_strategy)
def test_spreadsheetmlstyles_comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=ColOrRowElement_strategy)
@settings(max_examples=50)
def test_colorrowelement_instantiation(instance):
    assert isinstance(instance, ColOrRowElement)

@given(instance=SpreadsheetMLStyles_Column_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_column_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Column)



@given(instance=SpreadsheetMLStyles_Column_strategy)
def test_spreadsheetmlstyles_column_autoFitWidth_setter(instance):
    original = instance.autoFitWidth
    instance.autoFitWidth = original
    assert instance.autoFitWidth == original



@given(instance=SpreadsheetMLStyles_Column_strategy)
def test_spreadsheetmlstyles_column_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SpreadsheetMLStyles_Cell_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_cell_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Cell)



@given(instance=SpreadsheetMLStyles_Cell_strategy)
def test_spreadsheetmlstyles_cell_mergeAcross_setter(instance):
    original = instance.mergeAcross
    instance.mergeAcross = original
    assert instance.mergeAcross == original



@given(instance=SpreadsheetMLStyles_Cell_strategy)
def test_spreadsheetmlstyles_cell_arrayRange_setter(instance):
    original = instance.arrayRange
    instance.arrayRange = original
    assert instance.arrayRange == original



@given(instance=SpreadsheetMLStyles_Cell_strategy)
def test_spreadsheetmlstyles_cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=SpreadsheetMLStyles_Cell_strategy)
def test_spreadsheetmlstyles_cell_mergeDown_setter(instance):
    original = instance.mergeDown
    instance.mergeDown = original
    assert instance.mergeDown == original



@given(instance=SpreadsheetMLStyles_Cell_strategy)
def test_spreadsheetmlstyles_cell_hRef_setter(instance):
    original = instance.hRef
    instance.hRef = original
    assert instance.hRef == original

@given(instance=SpreadsheetMLStyles_ColOrRowElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_colorrowelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_ColOrRowElement)



@given(instance=SpreadsheetMLStyles_ColOrRowElement_strategy)
def test_spreadsheetmlstyles_colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original



@given(instance=SpreadsheetMLStyles_ColOrRowElement_strategy)
def test_spreadsheetmlstyles_colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=SpreadsheetMLStyles_Row_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_row_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Row)



@given(instance=SpreadsheetMLStyles_Row_strategy)
def test_spreadsheetmlstyles_row_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=SpreadsheetMLStyles_Row_strategy)
def test_spreadsheetmlstyles_row_autoFitHeight_setter(instance):
    original = instance.autoFitHeight
    instance.autoFitHeight = original
    assert instance.autoFitHeight == original

@given(instance=Row_strategy)
@settings(max_examples=50)
def test_row_instantiation(instance):
    assert isinstance(instance, Row)

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=StyledElement_strategy)
@settings(max_examples=50)
def test_styledelement_instantiation(instance):
    assert isinstance(instance, StyledElement)

@given(instance=SpreadsheetMLStyles_TableElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_tableelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_TableElement)



@given(instance=SpreadsheetMLStyles_TableElement_strategy)
def test_spreadsheetmlstyles_tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=StyleType_strategy)
@settings(max_examples=50)
def test_styletype_instantiation(instance):
    assert isinstance(instance, StyleType)

@given(instance=SpreadsheetMLStyles_StyledElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_styledelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_StyledElement)

@given(instance=WorksheetOptionsElt_strategy)
@settings(max_examples=50)
def test_worksheetoptionselt_instantiation(instance):
    assert isinstance(instance, WorksheetOptionsElt)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SpreadsheetMLStyles_Worksheet_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_worksheet_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Worksheet)



@given(instance=SpreadsheetMLStyles_Worksheet_strategy)
def test_spreadsheetmlstyles_worksheet_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original



@given(instance=SpreadsheetMLStyles_Worksheet_strategy)
def test_spreadsheetmlstyles_worksheet_rightToLeft_setter(instance):
    original = instance.rightToLeft
    instance.rightToLeft = original
    assert instance.rightToLeft == original



@given(instance=SpreadsheetMLStyles_Worksheet_strategy)
def test_spreadsheetmlstyles_worksheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLStyles_Table_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_table_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Table)



@given(instance=SpreadsheetMLStyles_Table_strategy)
def test_spreadsheetmlstyles_table_fullColumns_setter(instance):
    original = instance.fullColumns
    instance.fullColumns = original
    assert instance.fullColumns == original



@given(instance=SpreadsheetMLStyles_Table_strategy)
def test_spreadsheetmlstyles_table_topCell_setter(instance):
    original = instance.topCell
    instance.topCell = original
    assert instance.topCell == original



@given(instance=SpreadsheetMLStyles_Table_strategy)
def test_spreadsheetmlstyles_table_fullRows_setter(instance):
    original = instance.fullRows
    instance.fullRows = original
    assert instance.fullRows == original



@given(instance=SpreadsheetMLStyles_Table_strategy)
def test_spreadsheetmlstyles_table_leftCell_setter(instance):
    original = instance.leftCell
    instance.leftCell = original
    assert instance.leftCell == original



@given(instance=SpreadsheetMLStyles_Table_strategy)
def test_spreadsheetmlstyles_table_expandedRowCount_setter(instance):
    original = instance.expandedRowCount
    instance.expandedRowCount = original
    assert instance.expandedRowCount == original



@given(instance=SpreadsheetMLStyles_Table_strategy)
def test_spreadsheetmlstyles_table_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original



@given(instance=SpreadsheetMLStyles_Table_strategy)
def test_spreadsheetmlstyles_table_expandedColumnCount_setter(instance):
    original = instance.expandedColumnCount
    instance.expandedColumnCount = original
    assert instance.expandedColumnCount == original



@given(instance=SpreadsheetMLStyles_Table_strategy)
def test_spreadsheetmlstyles_table_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original

@given(instance=NamesType_strategy)
@settings(max_examples=50)
def test_namestype_instantiation(instance):
    assert isinstance(instance, NamesType)

@given(instance=StylesCollection_strategy)
@settings(max_examples=50)
def test_stylescollection_instantiation(instance):
    assert isinstance(instance, StylesCollection)

@given(instance=ExcelWorkbook_strategy)
@settings(max_examples=50)
def test_excelworkbook_instantiation(instance):
    assert isinstance(instance, ExcelWorkbook)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=Worksheet_strategy)
@settings(max_examples=50)
def test_worksheet_instantiation(instance):
    assert isinstance(instance, Worksheet)

@given(instance=SmartTagType_strategy)
@settings(max_examples=50)
def test_smarttagtype_instantiation(instance):
    assert isinstance(instance, SmartTagType)

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)

@given(instance=SpreadsheetMLStyles_SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_SmartTagsCollection)

@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)

@given(instance=SpreadsheetMLStyles_SmartTagType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_smarttagtype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_SmartTagType)



@given(instance=SpreadsheetMLStyles_SmartTagType_strategy)
def test_spreadsheetmlstyles_smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SpreadsheetMLStyles_SmartTagType_strategy)
def test_spreadsheetmlstyles_smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original



@given(instance=SpreadsheetMLStyles_SmartTagType_strategy)
def test_spreadsheetmlstyles_smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=SpreadsheetMLStyles_Workbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_workbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_Workbook)

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=SpreadsheetMLStyles_CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_CustomDocumentProperty)



@given(instance=SpreadsheetMLStyles_CustomDocumentProperty_strategy)
def test_spreadsheetmlstyles_customdocumentproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, CustomDocumentProperty)

@given(instance=SpreadsheetMLStyles_CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_CustomDocumentPropertiesCollection)

@given(instance=VersionType_strategy)
@settings(max_examples=50)
def test_versiontype_instantiation(instance):
    assert isinstance(instance, VersionType)

@given(instance=Workbook_strategy)
@settings(max_examples=50)
def test_workbook_instantiation(instance):
    assert isinstance(instance, Workbook)

@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_DocumentPropertiesCollection)



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original



@given(instance=SpreadsheetMLStyles_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles_documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=SpreadsheetMLStyles_NumberValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_numbervalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_NumberValue)



@given(instance=SpreadsheetMLStyles_NumberValue_strategy)
def test_spreadsheetmlstyles_numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLStyles_ErrorValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_errorvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_ErrorValue)

@given(instance=SpreadsheetMLStyles_DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_datetimetypevalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_DateTimeTypeValue)

@given(instance=SpreadsheetMLStyles_BooleanValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_booleanvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_BooleanValue)



@given(instance=SpreadsheetMLStyles_BooleanValue_strategy)
def test_spreadsheetmlstyles_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLStyles_StringValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_stringvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_StringValue)



@given(instance=SpreadsheetMLStyles_StringValue_strategy)
def test_spreadsheetmlstyles_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=SpreadsheetMLStyles_ValueType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_valuetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_ValueType)

@given(instance=SpreadsheetMLStyles_VersionType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_versiontype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_VersionType)



@given(instance=SpreadsheetMLStyles_VersionType_strategy)
def test_spreadsheetmlstyles_versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original



@given(instance=SpreadsheetMLStyles_VersionType_strategy)
def test_spreadsheetmlstyles_versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=SpreadsheetMLStyles_DateTimeType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles_datetimetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles_DateTimeType)



@given(instance=SpreadsheetMLStyles_DateTimeType_strategy)
def test_spreadsheetmlstyles_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=SpreadsheetMLStyles_DateTimeType_strategy)
def test_spreadsheetmlstyles_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=SpreadsheetMLStyles_DateTimeType_strategy)
def test_spreadsheetmlstyles_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=SpreadsheetMLStyles_DateTimeType_strategy)
def test_spreadsheetmlstyles_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=SpreadsheetMLStyles_DateTimeType_strategy)
def test_spreadsheetmlstyles_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original



@given(instance=SpreadsheetMLStyles_DateTimeType_strategy)
def test_spreadsheetmlstyles_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original
