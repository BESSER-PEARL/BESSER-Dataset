import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SpreadsheetMLStyles::NamedRange,
    SpreadsheetMLStyles::NamesType,
    NamedRange,
    SpreadsheetMLStyles::NumberFormatType,
    SpreadsheetMLStyles::InteriorType,
    SpreadsheetMLStyles::FontType,
    BorderType,
    SpreadsheetMLStyles::BordersType,
    SpreadsheetMLStyles::BorderType,
    SpreadsheetMLStyles::AlignmentType,
    FontType,
    SpreadsheetMLStyles::ProtectionType,
    ProtectionType,
    NumberFormatType,
    InteriorType,
    BordersType,
    AlignmentType,
    SpreadsheetMLStyles::StyleType,
    SpreadsheetMLStyles::StylesCollection,
    SpreadsheetMLStyles::Print,
    SpreadsheetMLStyles::PageMarginsInfo,
    HeaderOrFooterElt,
    SpreadsheetMLStyles::Footer,
    SpreadsheetMLStyles::Header,
    SpreadsheetMLStyles::HeaderOrFooterElt,
    Layout,
    SpreadsheetMLStyles::PageSetup,
    SpreadsheetMLStyles::Layout,
    PageMarginsInfo,
    Footer,
    Header,
    Print,
    PageSetup,
    SpreadsheetMLStyles::WorksheetOptionsElt,
    SpreadsheetMLStyles::ExcelWorkbook,
    SpreadsheetMLStyles::Data,
    Comment,
    SpreadsheetMLStyles::Comment,
    ColOrRowElement,
    SpreadsheetMLStyles::Column,
    TableElement,
    SpreadsheetMLStyles::Cell,
    SpreadsheetMLStyles::ColOrRowElement,
    SpreadsheetMLStyles::Row,
    Row,
    Column,
    StyledElement,
    SpreadsheetMLStyles::TableElement,
    StyleType,
    SpreadsheetMLStyles::StyledElement,
    WorksheetOptionsElt,
    Table,
    SpreadsheetMLStyles::Worksheet,
    SpreadsheetMLStyles::Table,
    NamesType,
    StylesCollection,
    ExcelWorkbook,
    DocumentPropertiesCollection,
    Worksheet,
    SmartTagType,
    Cell,
    SpreadsheetMLStyles::SmartTagsCollection,
    SmartTagsCollection,
    SpreadsheetMLStyles::SmartTagType,
    SpreadsheetMLStyles::Workbook,
    CustomDocumentPropertiesCollection,
    SpreadsheetMLStyles::CustomDocumentProperty,
    CustomDocumentProperty,
    SpreadsheetMLStyles::CustomDocumentPropertiesCollection,
    VersionType,
    Workbook,
    SpreadsheetMLStyles::DocumentPropertiesCollection,
    DateTimeType,
    ValueType,
    SpreadsheetMLStyles::BooleanValue,
    SpreadsheetMLStyles::DateTimeTypeValue,
    SpreadsheetMLStyles::NumberValue,
    SpreadsheetMLStyles::ErrorValue,
    SpreadsheetMLStyles::StringValue,
    Data,
    SpreadsheetMLStyles::ValueType,
    SpreadsheetMLStyles::VersionType,
    SpreadsheetMLStyles::DateTimeType,
    PatternType,
    DisplayDrawingObjectsType,
    LineStyleType,
    CommentsLayoutType,
    VisibleType,
    OrientationType,
    VerticalAlignementType,
    ReadingOrderType,
    CalculationWorkbookType,
    VerticalAlignType,
    ExcelNumberFormatType,
    ExcelWorksheetTypeType,
    EnableSelectionType,
    UnderlineType,
    PositionType,
    HorizontalAlignementType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheetmlstyles::namedrange_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::NamedRange)


def test_spreadsheetmlstyles::namedrange_constructor_exists():
    assert callable(SpreadsheetMLStyles::NamedRange.__init__)


def test_spreadsheetmlstyles::namedrange_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::NamedRange.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "refersTo" in params, "Missing parameter 'refersTo'"

def test_spreadsheetmlstyles::namedrange_has_name():
    assert hasattr(SpreadsheetMLStyles::NamedRange, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles::NamedRange.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::namedrange_has_hidden():
    assert hasattr(SpreadsheetMLStyles::NamedRange, "hidden")
    descriptor = None
    for klass in SpreadsheetMLStyles::NamedRange.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::namedrange_has_refersTo():
    assert hasattr(SpreadsheetMLStyles::NamedRange, "refersTo")
    descriptor = None
    for klass in SpreadsheetMLStyles::NamedRange.__mro__:
        if "refersTo" in klass.__dict__:
            descriptor = klass.__dict__["refersTo"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::namestype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::NamesType)


def test_spreadsheetmlstyles::namestype_constructor_exists():
    assert callable(SpreadsheetMLStyles::NamesType.__init__)


def test_spreadsheetmlstyles::namestype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::NamesType.__init__)
    params = list(sig.parameters.keys())



def test_namedrange_is_not_abstract():
    assert not inspect.isabstract(NamedRange)


def test_namedrange_constructor_exists():
    assert callable(NamedRange.__init__)


def test_namedrange_constructor_args():
    sig = inspect.signature(NamedRange.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::numberformattype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::NumberFormatType)


def test_spreadsheetmlstyles::numberformattype_constructor_exists():
    assert callable(SpreadsheetMLStyles::NumberFormatType.__init__)


def test_spreadsheetmlstyles::numberformattype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::NumberFormatType.__init__)
    params = list(sig.parameters.keys())
    assert "format" in params, "Missing parameter 'format'"

def test_spreadsheetmlstyles::numberformattype_has_format():
    assert hasattr(SpreadsheetMLStyles::NumberFormatType, "format")
    descriptor = None
    for klass in SpreadsheetMLStyles::NumberFormatType.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::interiortype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::InteriorType)


def test_spreadsheetmlstyles::interiortype_constructor_exists():
    assert callable(SpreadsheetMLStyles::InteriorType.__init__)


def test_spreadsheetmlstyles::interiortype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::InteriorType.__init__)
    params = list(sig.parameters.keys())
    assert "patternColor" in params, "Missing parameter 'patternColor'"
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "color" in params, "Missing parameter 'color'"

def test_spreadsheetmlstyles::interiortype_has_patternColor():
    assert hasattr(SpreadsheetMLStyles::InteriorType, "patternColor")
    descriptor = None
    for klass in SpreadsheetMLStyles::InteriorType.__mro__:
        if "patternColor" in klass.__dict__:
            descriptor = klass.__dict__["patternColor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::interiortype_has_pattern():
    assert hasattr(SpreadsheetMLStyles::InteriorType, "pattern")
    descriptor = None
    for klass in SpreadsheetMLStyles::InteriorType.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::interiortype_has_color():
    assert hasattr(SpreadsheetMLStyles::InteriorType, "color")
    descriptor = None
    for klass in SpreadsheetMLStyles::InteriorType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::fonttype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::FontType)


def test_spreadsheetmlstyles::fonttype_constructor_exists():
    assert callable(SpreadsheetMLStyles::FontType.__init__)


def test_spreadsheetmlstyles::fonttype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::FontType.__init__)
    params = list(sig.parameters.keys())
    assert "outline" in params, "Missing parameter 'outline'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "color" in params, "Missing parameter 'color'"
    assert "strikeThrough" in params, "Missing parameter 'strikeThrough'"
    assert "shadow" in params, "Missing parameter 'shadow'"
    assert "italic" in params, "Missing parameter 'italic'"
    assert "verticalAlign" in params, "Missing parameter 'verticalAlign'"
    assert "size" in params, "Missing parameter 'size'"
    assert "underline" in params, "Missing parameter 'underline'"
    assert "bold" in params, "Missing parameter 'bold'"

def test_spreadsheetmlstyles::fonttype_has_outline():
    assert hasattr(SpreadsheetMLStyles::FontType, "outline")
    descriptor = None
    for klass in SpreadsheetMLStyles::FontType.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::fonttype_has_fontName():
    assert hasattr(SpreadsheetMLStyles::FontType, "fontName")
    descriptor = None
    for klass in SpreadsheetMLStyles::FontType.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::fonttype_has_color():
    assert hasattr(SpreadsheetMLStyles::FontType, "color")
    descriptor = None
    for klass in SpreadsheetMLStyles::FontType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::fonttype_has_strikeThrough():
    assert hasattr(SpreadsheetMLStyles::FontType, "strikeThrough")
    descriptor = None
    for klass in SpreadsheetMLStyles::FontType.__mro__:
        if "strikeThrough" in klass.__dict__:
            descriptor = klass.__dict__["strikeThrough"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::fonttype_has_shadow():
    assert hasattr(SpreadsheetMLStyles::FontType, "shadow")
    descriptor = None
    for klass in SpreadsheetMLStyles::FontType.__mro__:
        if "shadow" in klass.__dict__:
            descriptor = klass.__dict__["shadow"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::fonttype_has_italic():
    assert hasattr(SpreadsheetMLStyles::FontType, "italic")
    descriptor = None
    for klass in SpreadsheetMLStyles::FontType.__mro__:
        if "italic" in klass.__dict__:
            descriptor = klass.__dict__["italic"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::fonttype_has_verticalAlign():
    assert hasattr(SpreadsheetMLStyles::FontType, "verticalAlign")
    descriptor = None
    for klass in SpreadsheetMLStyles::FontType.__mro__:
        if "verticalAlign" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlign"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::fonttype_has_size():
    assert hasattr(SpreadsheetMLStyles::FontType, "size")
    descriptor = None
    for klass in SpreadsheetMLStyles::FontType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::fonttype_has_underline():
    assert hasattr(SpreadsheetMLStyles::FontType, "underline")
    descriptor = None
    for klass in SpreadsheetMLStyles::FontType.__mro__:
        if "underline" in klass.__dict__:
            descriptor = klass.__dict__["underline"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::fonttype_has_bold():
    assert hasattr(SpreadsheetMLStyles::FontType, "bold")
    descriptor = None
    for klass in SpreadsheetMLStyles::FontType.__mro__:
        if "bold" in klass.__dict__:
            descriptor = klass.__dict__["bold"]
            break
    assert isinstance(descriptor, property)



def test_bordertype_is_not_abstract():
    assert not inspect.isabstract(BorderType)


def test_bordertype_constructor_exists():
    assert callable(BorderType.__init__)


def test_bordertype_constructor_args():
    sig = inspect.signature(BorderType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::borderstype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::BordersType)


def test_spreadsheetmlstyles::borderstype_constructor_exists():
    assert callable(SpreadsheetMLStyles::BordersType.__init__)


def test_spreadsheetmlstyles::borderstype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::BordersType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::bordertype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::BorderType)


def test_spreadsheetmlstyles::bordertype_constructor_exists():
    assert callable(SpreadsheetMLStyles::BorderType.__init__)


def test_spreadsheetmlstyles::bordertype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::BorderType.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "color" in params, "Missing parameter 'color'"
    assert "position" in params, "Missing parameter 'position'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"

def test_spreadsheetmlstyles::bordertype_has_weight():
    assert hasattr(SpreadsheetMLStyles::BorderType, "weight")
    descriptor = None
    for klass in SpreadsheetMLStyles::BorderType.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::bordertype_has_color():
    assert hasattr(SpreadsheetMLStyles::BorderType, "color")
    descriptor = None
    for klass in SpreadsheetMLStyles::BorderType.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::bordertype_has_position():
    assert hasattr(SpreadsheetMLStyles::BorderType, "position")
    descriptor = None
    for klass in SpreadsheetMLStyles::BorderType.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::bordertype_has_lineStyle():
    assert hasattr(SpreadsheetMLStyles::BorderType, "lineStyle")
    descriptor = None
    for klass in SpreadsheetMLStyles::BorderType.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::alignmenttype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::AlignmentType)


def test_spreadsheetmlstyles::alignmenttype_constructor_exists():
    assert callable(SpreadsheetMLStyles::AlignmentType.__init__)


def test_spreadsheetmlstyles::alignmenttype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::AlignmentType.__init__)
    params = list(sig.parameters.keys())
    assert "vertical" in params, "Missing parameter 'vertical'"
    assert "horizontal" in params, "Missing parameter 'horizontal'"
    assert "wrapText" in params, "Missing parameter 'wrapText'"
    assert "indent" in params, "Missing parameter 'indent'"
    assert "shrinkToFit" in params, "Missing parameter 'shrinkToFit'"
    assert "verticalText" in params, "Missing parameter 'verticalText'"
    assert "readingOrder" in params, "Missing parameter 'readingOrder'"
    assert "rotate" in params, "Missing parameter 'rotate'"

def test_spreadsheetmlstyles::alignmenttype_has_vertical():
    assert hasattr(SpreadsheetMLStyles::AlignmentType, "vertical")
    descriptor = None
    for klass in SpreadsheetMLStyles::AlignmentType.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::alignmenttype_has_horizontal():
    assert hasattr(SpreadsheetMLStyles::AlignmentType, "horizontal")
    descriptor = None
    for klass in SpreadsheetMLStyles::AlignmentType.__mro__:
        if "horizontal" in klass.__dict__:
            descriptor = klass.__dict__["horizontal"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::alignmenttype_has_wrapText():
    assert hasattr(SpreadsheetMLStyles::AlignmentType, "wrapText")
    descriptor = None
    for klass in SpreadsheetMLStyles::AlignmentType.__mro__:
        if "wrapText" in klass.__dict__:
            descriptor = klass.__dict__["wrapText"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::alignmenttype_has_indent():
    assert hasattr(SpreadsheetMLStyles::AlignmentType, "indent")
    descriptor = None
    for klass in SpreadsheetMLStyles::AlignmentType.__mro__:
        if "indent" in klass.__dict__:
            descriptor = klass.__dict__["indent"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::alignmenttype_has_shrinkToFit():
    assert hasattr(SpreadsheetMLStyles::AlignmentType, "shrinkToFit")
    descriptor = None
    for klass in SpreadsheetMLStyles::AlignmentType.__mro__:
        if "shrinkToFit" in klass.__dict__:
            descriptor = klass.__dict__["shrinkToFit"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::alignmenttype_has_verticalText():
    assert hasattr(SpreadsheetMLStyles::AlignmentType, "verticalText")
    descriptor = None
    for klass in SpreadsheetMLStyles::AlignmentType.__mro__:
        if "verticalText" in klass.__dict__:
            descriptor = klass.__dict__["verticalText"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::alignmenttype_has_readingOrder():
    assert hasattr(SpreadsheetMLStyles::AlignmentType, "readingOrder")
    descriptor = None
    for klass in SpreadsheetMLStyles::AlignmentType.__mro__:
        if "readingOrder" in klass.__dict__:
            descriptor = klass.__dict__["readingOrder"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::alignmenttype_has_rotate():
    assert hasattr(SpreadsheetMLStyles::AlignmentType, "rotate")
    descriptor = None
    for klass in SpreadsheetMLStyles::AlignmentType.__mro__:
        if "rotate" in klass.__dict__:
            descriptor = klass.__dict__["rotate"]
            break
    assert isinstance(descriptor, property)



def test_fonttype_is_not_abstract():
    assert not inspect.isabstract(FontType)


def test_fonttype_constructor_exists():
    assert callable(FontType.__init__)


def test_fonttype_constructor_args():
    sig = inspect.signature(FontType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::protectiontype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::ProtectionType)


def test_spreadsheetmlstyles::protectiontype_constructor_exists():
    assert callable(SpreadsheetMLStyles::ProtectionType.__init__)


def test_spreadsheetmlstyles::protectiontype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::ProtectionType.__init__)
    params = list(sig.parameters.keys())
    assert "protected" in params, "Missing parameter 'protected'"

def test_spreadsheetmlstyles::protectiontype_has_protected():
    assert hasattr(SpreadsheetMLStyles::ProtectionType, "protected")
    descriptor = None
    for klass in SpreadsheetMLStyles::ProtectionType.__mro__:
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



def test_spreadsheetmlstyles::styletype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::StyleType)


def test_spreadsheetmlstyles::styletype_constructor_exists():
    assert callable(SpreadsheetMLStyles::StyleType.__init__)


def test_spreadsheetmlstyles::styletype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::StyleType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlstyles::styletype_has_id():
    assert hasattr(SpreadsheetMLStyles::StyleType, "id")
    descriptor = None
    for klass in SpreadsheetMLStyles::StyleType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::styletype_has_name():
    assert hasattr(SpreadsheetMLStyles::StyleType, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles::StyleType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::stylescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::StylesCollection)


def test_spreadsheetmlstyles::stylescollection_constructor_exists():
    assert callable(SpreadsheetMLStyles::StylesCollection.__init__)


def test_spreadsheetmlstyles::stylescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::StylesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::print_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Print)


def test_spreadsheetmlstyles::print_constructor_exists():
    assert callable(SpreadsheetMLStyles::Print.__init__)


def test_spreadsheetmlstyles::print_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Print.__init__)
    params = list(sig.parameters.keys())
    assert "fitHeight" in params, "Missing parameter 'fitHeight'"
    assert "gridlines" in params, "Missing parameter 'gridlines'"
    assert "validPrinterInfo" in params, "Missing parameter 'validPrinterInfo'"
    assert "commentsLayout" in params, "Missing parameter 'commentsLayout'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "numberOfCopies" in params, "Missing parameter 'numberOfCopies'"
    assert "blackAndWhite" in params, "Missing parameter 'blackAndWhite'"
    assert "verticalResolution" in params, "Missing parameter 'verticalResolution'"
    assert "rowColHeadings" in params, "Missing parameter 'rowColHeadings'"
    assert "leftToRight" in params, "Missing parameter 'leftToRight'"
    assert "fitWidth" in params, "Missing parameter 'fitWidth'"
    assert "draftQuality" in params, "Missing parameter 'draftQuality'"
    assert "horizontalResolution" in params, "Missing parameter 'horizontalResolution'"
    assert "paperSizeIndex" in params, "Missing parameter 'paperSizeIndex'"
    assert "printErrors" in params, "Missing parameter 'printErrors'"

def test_spreadsheetmlstyles::print_has_fitHeight():
    assert hasattr(SpreadsheetMLStyles::Print, "fitHeight")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "fitHeight" in klass.__dict__:
            descriptor = klass.__dict__["fitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_gridlines():
    assert hasattr(SpreadsheetMLStyles::Print, "gridlines")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "gridlines" in klass.__dict__:
            descriptor = klass.__dict__["gridlines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_validPrinterInfo():
    assert hasattr(SpreadsheetMLStyles::Print, "validPrinterInfo")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "validPrinterInfo" in klass.__dict__:
            descriptor = klass.__dict__["validPrinterInfo"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_commentsLayout():
    assert hasattr(SpreadsheetMLStyles::Print, "commentsLayout")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "commentsLayout" in klass.__dict__:
            descriptor = klass.__dict__["commentsLayout"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_scale():
    assert hasattr(SpreadsheetMLStyles::Print, "scale")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_numberOfCopies():
    assert hasattr(SpreadsheetMLStyles::Print, "numberOfCopies")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "numberOfCopies" in klass.__dict__:
            descriptor = klass.__dict__["numberOfCopies"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_blackAndWhite():
    assert hasattr(SpreadsheetMLStyles::Print, "blackAndWhite")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "blackAndWhite" in klass.__dict__:
            descriptor = klass.__dict__["blackAndWhite"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_verticalResolution():
    assert hasattr(SpreadsheetMLStyles::Print, "verticalResolution")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "verticalResolution" in klass.__dict__:
            descriptor = klass.__dict__["verticalResolution"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_rowColHeadings():
    assert hasattr(SpreadsheetMLStyles::Print, "rowColHeadings")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "rowColHeadings" in klass.__dict__:
            descriptor = klass.__dict__["rowColHeadings"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_leftToRight():
    assert hasattr(SpreadsheetMLStyles::Print, "leftToRight")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "leftToRight" in klass.__dict__:
            descriptor = klass.__dict__["leftToRight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_fitWidth():
    assert hasattr(SpreadsheetMLStyles::Print, "fitWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "fitWidth" in klass.__dict__:
            descriptor = klass.__dict__["fitWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_draftQuality():
    assert hasattr(SpreadsheetMLStyles::Print, "draftQuality")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "draftQuality" in klass.__dict__:
            descriptor = klass.__dict__["draftQuality"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_horizontalResolution():
    assert hasattr(SpreadsheetMLStyles::Print, "horizontalResolution")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "horizontalResolution" in klass.__dict__:
            descriptor = klass.__dict__["horizontalResolution"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_paperSizeIndex():
    assert hasattr(SpreadsheetMLStyles::Print, "paperSizeIndex")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "paperSizeIndex" in klass.__dict__:
            descriptor = klass.__dict__["paperSizeIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::print_has_printErrors():
    assert hasattr(SpreadsheetMLStyles::Print, "printErrors")
    descriptor = None
    for klass in SpreadsheetMLStyles::Print.__mro__:
        if "printErrors" in klass.__dict__:
            descriptor = klass.__dict__["printErrors"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::pagemarginsinfo_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::PageMarginsInfo)


def test_spreadsheetmlstyles::pagemarginsinfo_constructor_exists():
    assert callable(SpreadsheetMLStyles::PageMarginsInfo.__init__)


def test_spreadsheetmlstyles::pagemarginsinfo_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::PageMarginsInfo.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"
    assert "top" in params, "Missing parameter 'top'"
    assert "bottom" in params, "Missing parameter 'bottom'"
    assert "left" in params, "Missing parameter 'left'"

def test_spreadsheetmlstyles::pagemarginsinfo_has_right():
    assert hasattr(SpreadsheetMLStyles::PageMarginsInfo, "right")
    descriptor = None
    for klass in SpreadsheetMLStyles::PageMarginsInfo.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::pagemarginsinfo_has_top():
    assert hasattr(SpreadsheetMLStyles::PageMarginsInfo, "top")
    descriptor = None
    for klass in SpreadsheetMLStyles::PageMarginsInfo.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::pagemarginsinfo_has_bottom():
    assert hasattr(SpreadsheetMLStyles::PageMarginsInfo, "bottom")
    descriptor = None
    for klass in SpreadsheetMLStyles::PageMarginsInfo.__mro__:
        if "bottom" in klass.__dict__:
            descriptor = klass.__dict__["bottom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::pagemarginsinfo_has_left():
    assert hasattr(SpreadsheetMLStyles::PageMarginsInfo, "left")
    descriptor = None
    for klass in SpreadsheetMLStyles::PageMarginsInfo.__mro__:
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



def test_spreadsheetmlstyles::footer_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Footer)


def test_spreadsheetmlstyles::footer_constructor_exists():
    assert callable(SpreadsheetMLStyles::Footer.__init__)


def test_spreadsheetmlstyles::footer_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Footer.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::header_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Header)


def test_spreadsheetmlstyles::header_constructor_exists():
    assert callable(SpreadsheetMLStyles::Header.__init__)


def test_spreadsheetmlstyles::header_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Header.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::headerorfooterelt_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::HeaderOrFooterElt)


def test_spreadsheetmlstyles::headerorfooterelt_constructor_exists():
    assert callable(SpreadsheetMLStyles::HeaderOrFooterElt.__init__)


def test_spreadsheetmlstyles::headerorfooterelt_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::HeaderOrFooterElt.__init__)
    params = list(sig.parameters.keys())
    assert "margin" in params, "Missing parameter 'margin'"
    assert "data" in params, "Missing parameter 'data'"

def test_spreadsheetmlstyles::headerorfooterelt_has_margin():
    assert hasattr(SpreadsheetMLStyles::HeaderOrFooterElt, "margin")
    descriptor = None
    for klass in SpreadsheetMLStyles::HeaderOrFooterElt.__mro__:
        if "margin" in klass.__dict__:
            descriptor = klass.__dict__["margin"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::headerorfooterelt_has_data():
    assert hasattr(SpreadsheetMLStyles::HeaderOrFooterElt, "data")
    descriptor = None
    for klass in SpreadsheetMLStyles::HeaderOrFooterElt.__mro__:
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



def test_spreadsheetmlstyles::pagesetup_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::PageSetup)


def test_spreadsheetmlstyles::pagesetup_constructor_exists():
    assert callable(SpreadsheetMLStyles::PageSetup.__init__)


def test_spreadsheetmlstyles::pagesetup_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::PageSetup.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::layout_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Layout)


def test_spreadsheetmlstyles::layout_constructor_exists():
    assert callable(SpreadsheetMLStyles::Layout.__init__)


def test_spreadsheetmlstyles::layout_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Layout.__init__)
    params = list(sig.parameters.keys())
    assert "startPageNumber" in params, "Missing parameter 'startPageNumber'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "centerVertical" in params, "Missing parameter 'centerVertical'"
    assert "centerHorizontal" in params, "Missing parameter 'centerHorizontal'"

def test_spreadsheetmlstyles::layout_has_startPageNumber():
    assert hasattr(SpreadsheetMLStyles::Layout, "startPageNumber")
    descriptor = None
    for klass in SpreadsheetMLStyles::Layout.__mro__:
        if "startPageNumber" in klass.__dict__:
            descriptor = klass.__dict__["startPageNumber"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::layout_has_orientation():
    assert hasattr(SpreadsheetMLStyles::Layout, "orientation")
    descriptor = None
    for klass in SpreadsheetMLStyles::Layout.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::layout_has_centerVertical():
    assert hasattr(SpreadsheetMLStyles::Layout, "centerVertical")
    descriptor = None
    for klass in SpreadsheetMLStyles::Layout.__mro__:
        if "centerVertical" in klass.__dict__:
            descriptor = klass.__dict__["centerVertical"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::layout_has_centerHorizontal():
    assert hasattr(SpreadsheetMLStyles::Layout, "centerHorizontal")
    descriptor = None
    for klass in SpreadsheetMLStyles::Layout.__mro__:
        if "centerHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["centerHorizontal"]
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



def test_spreadsheetmlstyles::worksheetoptionselt_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::WorksheetOptionsElt)


def test_spreadsheetmlstyles::worksheetoptionselt_constructor_exists():
    assert callable(SpreadsheetMLStyles::WorksheetOptionsElt.__init__)


def test_spreadsheetmlstyles::worksheetoptionselt_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::WorksheetOptionsElt.__init__)
    params = list(sig.parameters.keys())
    assert "protectObjects" in params, "Missing parameter 'protectObjects'"
    assert "splitVertical" in params, "Missing parameter 'splitVertical'"
    assert "doNotDisplayZeros" in params, "Missing parameter 'doNotDisplayZeros'"
    assert "freezePanes" in params, "Missing parameter 'freezePanes'"
    assert "activePane" in params, "Missing parameter 'activePane'"
    assert "standardWidth" in params, "Missing parameter 'standardWidth'"
    assert "allowInsertRows" in params, "Missing parameter 'allowInsertRows'"
    assert "allowInsertHyperlinks" in params, "Missing parameter 'allowInsertHyperlinks'"
    assert "zoom" in params, "Missing parameter 'zoom'"
    assert "activeRow" in params, "Missing parameter 'activeRow'"
    assert "tabColorIndex" in params, "Missing parameter 'tabColorIndex'"
    assert "unsynced" in params, "Missing parameter 'unsynced'"
    assert "noSummaryColumnsRightDetail" in params, "Missing parameter 'noSummaryColumnsRightDetail'"
    assert "pageBreakZoom" in params, "Missing parameter 'pageBreakZoom'"
    assert "allowSort" in params, "Missing parameter 'allowSort'"
    assert "frozenNoSplit" in params, "Missing parameter 'frozenNoSplit'"
    assert "displayPageBreak" in params, "Missing parameter 'displayPageBreak'"
    assert "applyAutomaticOutlineStyles" in params, "Missing parameter 'applyAutomaticOutlineStyles'"
    assert "filterOn" in params, "Missing parameter 'filterOn'"
    assert "activeColumn" in params, "Missing parameter 'activeColumn'"
    assert "protectScenarios" in params, "Missing parameter 'protectScenarios'"
    assert "noSummaryRowsBelowDetail" in params, "Missing parameter 'noSummaryRowsBelowDetail'"
    assert "splitHorizontal" in params, "Missing parameter 'splitHorizontal'"
    assert "doNotDisplayHeadings" in params, "Missing parameter 'doNotDisplayHeadings'"
    assert "protectContentst" in params, "Missing parameter 'protectContentst'"
    assert "doNotDisplayOutline" in params, "Missing parameter 'doNotDisplayOutline'"
    assert "showPageBreakZoom" in params, "Missing parameter 'showPageBreakZoom'"
    assert "displayRightToLeft" in params, "Missing parameter 'displayRightToLeft'"
    assert "displayFormulas" in params, "Missing parameter 'displayFormulas'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "allowInsertCols" in params, "Missing parameter 'allowInsertCols'"
    assert "topRowVisible" in params, "Missing parameter 'topRowVisible'"
    assert "codeName" in params, "Missing parameter 'codeName'"
    assert "transitionFormulaEntry" in params, "Missing parameter 'transitionFormulaEntry'"
    assert "gridlineColorIndex" in params, "Missing parameter 'gridlineColorIndex'"
    assert "fitToPage" in params, "Missing parameter 'fitToPage'"
    assert "allowSizeRows" in params, "Missing parameter 'allowSizeRows'"
    assert "topRowBottomPane" in params, "Missing parameter 'topRowBottomPane'"
    assert "allowUsePivotTables" in params, "Missing parameter 'allowUsePivotTables'"
    assert "gridlineColor" in params, "Missing parameter 'gridlineColor'"
    assert "enableSelection" in params, "Missing parameter 'enableSelection'"
    assert "selected" in params, "Missing parameter 'selected'"
    assert "allowDeleteRows" in params, "Missing parameter 'allowDeleteRows'"
    assert "doNotDisplayColHeaders" in params, "Missing parameter 'doNotDisplayColHeaders'"
    assert "excelWorksheetType" in params, "Missing parameter 'excelWorksheetType'"
    assert "intlMacro" in params, "Missing parameter 'intlMacro'"
    assert "doNotDisplayGridlines" in params, "Missing parameter 'doNotDisplayGridlines'"
    assert "doNotDisplayRowHeaders" in params, "Missing parameter 'doNotDisplayRowHeaders'"
    assert "allowSizeCols" in params, "Missing parameter 'allowSizeCols'"
    assert "leftColumnRightPane" in params, "Missing parameter 'leftColumnRightPane'"
    assert "name" in params, "Missing parameter 'name'"
    assert "transitionExpressionEvaluation" in params, "Missing parameter 'transitionExpressionEvaluation'"
    assert "allowFormatCells" in params, "Missing parameter 'allowFormatCells'"
    assert "allowFilter" in params, "Missing parameter 'allowFilter'"
    assert "rangeSelection" in params, "Missing parameter 'rangeSelection'"
    assert "leftColumnVisible" in params, "Missing parameter 'leftColumnVisible'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "allowDeleteCols" in params, "Missing parameter 'allowDeleteCols'"

def test_spreadsheetmlstyles::worksheetoptionselt_has_protectObjects():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "protectObjects")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "protectObjects" in klass.__dict__:
            descriptor = klass.__dict__["protectObjects"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_splitVertical():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "splitVertical")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "splitVertical" in klass.__dict__:
            descriptor = klass.__dict__["splitVertical"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_doNotDisplayZeros():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "doNotDisplayZeros")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "doNotDisplayZeros" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayZeros"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_freezePanes():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "freezePanes")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "freezePanes" in klass.__dict__:
            descriptor = klass.__dict__["freezePanes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_activePane():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "activePane")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "activePane" in klass.__dict__:
            descriptor = klass.__dict__["activePane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_standardWidth():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "standardWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "standardWidth" in klass.__dict__:
            descriptor = klass.__dict__["standardWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_allowInsertRows():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "allowInsertRows")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "allowInsertRows" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_allowInsertHyperlinks():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "allowInsertHyperlinks")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "allowInsertHyperlinks" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertHyperlinks"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_zoom():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "zoom")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_activeRow():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "activeRow")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "activeRow" in klass.__dict__:
            descriptor = klass.__dict__["activeRow"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_tabColorIndex():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "tabColorIndex")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "tabColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["tabColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_unsynced():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "unsynced")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "unsynced" in klass.__dict__:
            descriptor = klass.__dict__["unsynced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_noSummaryColumnsRightDetail():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "noSummaryColumnsRightDetail")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "noSummaryColumnsRightDetail" in klass.__dict__:
            descriptor = klass.__dict__["noSummaryColumnsRightDetail"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_pageBreakZoom():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "pageBreakZoom")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "pageBreakZoom" in klass.__dict__:
            descriptor = klass.__dict__["pageBreakZoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_allowSort():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "allowSort")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "allowSort" in klass.__dict__:
            descriptor = klass.__dict__["allowSort"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_frozenNoSplit():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "frozenNoSplit")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "frozenNoSplit" in klass.__dict__:
            descriptor = klass.__dict__["frozenNoSplit"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_displayPageBreak():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "displayPageBreak")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "displayPageBreak" in klass.__dict__:
            descriptor = klass.__dict__["displayPageBreak"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_applyAutomaticOutlineStyles():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "applyAutomaticOutlineStyles")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "applyAutomaticOutlineStyles" in klass.__dict__:
            descriptor = klass.__dict__["applyAutomaticOutlineStyles"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_filterOn():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "filterOn")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "filterOn" in klass.__dict__:
            descriptor = klass.__dict__["filterOn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_activeColumn():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "activeColumn")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "activeColumn" in klass.__dict__:
            descriptor = klass.__dict__["activeColumn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_protectScenarios():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "protectScenarios")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "protectScenarios" in klass.__dict__:
            descriptor = klass.__dict__["protectScenarios"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_noSummaryRowsBelowDetail():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "noSummaryRowsBelowDetail")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "noSummaryRowsBelowDetail" in klass.__dict__:
            descriptor = klass.__dict__["noSummaryRowsBelowDetail"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_splitHorizontal():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "splitHorizontal")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "splitHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["splitHorizontal"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_doNotDisplayHeadings():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "doNotDisplayHeadings")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "doNotDisplayHeadings" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayHeadings"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_protectContentst():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "protectContentst")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "protectContentst" in klass.__dict__:
            descriptor = klass.__dict__["protectContentst"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_doNotDisplayOutline():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "doNotDisplayOutline")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "doNotDisplayOutline" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayOutline"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_showPageBreakZoom():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "showPageBreakZoom")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "showPageBreakZoom" in klass.__dict__:
            descriptor = klass.__dict__["showPageBreakZoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_displayRightToLeft():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "displayRightToLeft")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "displayRightToLeft" in klass.__dict__:
            descriptor = klass.__dict__["displayRightToLeft"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_displayFormulas():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "displayFormulas")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "displayFormulas" in klass.__dict__:
            descriptor = klass.__dict__["displayFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_allowInsertCols():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "allowInsertCols")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "allowInsertCols" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_topRowVisible():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "topRowVisible")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "topRowVisible" in klass.__dict__:
            descriptor = klass.__dict__["topRowVisible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_codeName():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "codeName")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "codeName" in klass.__dict__:
            descriptor = klass.__dict__["codeName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_transitionFormulaEntry():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "transitionFormulaEntry")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "transitionFormulaEntry" in klass.__dict__:
            descriptor = klass.__dict__["transitionFormulaEntry"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_gridlineColorIndex():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "gridlineColorIndex")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "gridlineColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["gridlineColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_fitToPage():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "fitToPage")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "fitToPage" in klass.__dict__:
            descriptor = klass.__dict__["fitToPage"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_allowSizeRows():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "allowSizeRows")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "allowSizeRows" in klass.__dict__:
            descriptor = klass.__dict__["allowSizeRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_topRowBottomPane():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "topRowBottomPane")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "topRowBottomPane" in klass.__dict__:
            descriptor = klass.__dict__["topRowBottomPane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_allowUsePivotTables():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "allowUsePivotTables")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "allowUsePivotTables" in klass.__dict__:
            descriptor = klass.__dict__["allowUsePivotTables"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_gridlineColor():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "gridlineColor")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "gridlineColor" in klass.__dict__:
            descriptor = klass.__dict__["gridlineColor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_enableSelection():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "enableSelection")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "enableSelection" in klass.__dict__:
            descriptor = klass.__dict__["enableSelection"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_selected():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "selected")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_allowDeleteRows():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "allowDeleteRows")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "allowDeleteRows" in klass.__dict__:
            descriptor = klass.__dict__["allowDeleteRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_doNotDisplayColHeaders():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "doNotDisplayColHeaders")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "doNotDisplayColHeaders" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayColHeaders"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_excelWorksheetType():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "excelWorksheetType")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "excelWorksheetType" in klass.__dict__:
            descriptor = klass.__dict__["excelWorksheetType"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_intlMacro():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "intlMacro")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "intlMacro" in klass.__dict__:
            descriptor = klass.__dict__["intlMacro"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_doNotDisplayGridlines():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "doNotDisplayGridlines")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "doNotDisplayGridlines" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayGridlines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_doNotDisplayRowHeaders():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "doNotDisplayRowHeaders")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "doNotDisplayRowHeaders" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayRowHeaders"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_allowSizeCols():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "allowSizeCols")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "allowSizeCols" in klass.__dict__:
            descriptor = klass.__dict__["allowSizeCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_leftColumnRightPane():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "leftColumnRightPane")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "leftColumnRightPane" in klass.__dict__:
            descriptor = klass.__dict__["leftColumnRightPane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_name():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_transitionExpressionEvaluation():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "transitionExpressionEvaluation")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "transitionExpressionEvaluation" in klass.__dict__:
            descriptor = klass.__dict__["transitionExpressionEvaluation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_allowFormatCells():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "allowFormatCells")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "allowFormatCells" in klass.__dict__:
            descriptor = klass.__dict__["allowFormatCells"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_allowFilter():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "allowFilter")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "allowFilter" in klass.__dict__:
            descriptor = klass.__dict__["allowFilter"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_rangeSelection():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "rangeSelection")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "rangeSelection" in klass.__dict__:
            descriptor = klass.__dict__["rangeSelection"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_leftColumnVisible():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "leftColumnVisible")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "leftColumnVisible" in klass.__dict__:
            descriptor = klass.__dict__["leftColumnVisible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_visible():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "visible")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheetoptionselt_has_allowDeleteCols():
    assert hasattr(SpreadsheetMLStyles::WorksheetOptionsElt, "allowDeleteCols")
    descriptor = None
    for klass in SpreadsheetMLStyles::WorksheetOptionsElt.__mro__:
        if "allowDeleteCols" in klass.__dict__:
            descriptor = klass.__dict__["allowDeleteCols"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::excelworkbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::ExcelWorkbook)


def test_spreadsheetmlstyles::excelworkbook_constructor_exists():
    assert callable(SpreadsheetMLStyles::ExcelWorkbook.__init__)


def test_spreadsheetmlstyles::excelworkbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::ExcelWorkbook.__init__)
    params = list(sig.parameters.keys())
    assert "createBackup" in params, "Missing parameter 'createBackup'"
    assert "protectWindows" in params, "Missing parameter 'protectWindows'"
    assert "date1904" in params, "Missing parameter 'date1904'"
    assert "displayDrawingObjects" in params, "Missing parameter 'displayDrawingObjects'"
    assert "hideHorizontalScrollBar" in params, "Missing parameter 'hideHorizontalScrollBar'"
    assert "doNotSaveLinkValues" in params, "Missing parameter 'doNotSaveLinkValues'"
    assert "calculation" in params, "Missing parameter 'calculation'"
    assert "activeSheet" in params, "Missing parameter 'activeSheet'"
    assert "windowHidden" in params, "Missing parameter 'windowHidden'"
    assert "displayInkNotes" in params, "Missing parameter 'displayInkNotes'"
    assert "windowWidth" in params, "Missing parameter 'windowWidth'"
    assert "tabRatio" in params, "Missing parameter 'tabRatio'"
    assert "windowHeight" in params, "Missing parameter 'windowHeight'"
    assert "selectedSheets" in params, "Missing parameter 'selectedSheets'"
    assert "hideVerticalScrollBar" in params, "Missing parameter 'hideVerticalScrollBar'"
    assert "doNotCalculateBeforeSave" in params, "Missing parameter 'doNotCalculateBeforeSave'"
    assert "protectStructure" in params, "Missing parameter 'protectStructure'"
    assert "maxChange" in params, "Missing parameter 'maxChange'"
    assert "firstVisibleSheet" in params, "Missing parameter 'firstVisibleSheet'"
    assert "activeChart" in params, "Missing parameter 'activeChart'"
    assert "hideWorkbookTabs" in params, "Missing parameter 'hideWorkbookTabs'"
    assert "embedSaveSmartTags" in params, "Missing parameter 'embedSaveSmartTags'"
    assert "windowIconic" in params, "Missing parameter 'windowIconic'"
    assert "acceptLabelsInFormulas" in params, "Missing parameter 'acceptLabelsInFormulas'"
    assert "windowTopX" in params, "Missing parameter 'windowTopX'"
    assert "refModeR1C1" in params, "Missing parameter 'refModeR1C1'"
    assert "hidePivotTableFieldList" in params, "Missing parameter 'hidePivotTableFieldList'"
    assert "futureVer" in params, "Missing parameter 'futureVer'"
    assert "noAutoRecover" in params, "Missing parameter 'noAutoRecover'"
    assert "precisionAsDisplayed" in params, "Missing parameter 'precisionAsDisplayed'"
    assert "iteration" in params, "Missing parameter 'iteration'"
    assert "uncalced" in params, "Missing parameter 'uncalced'"
    assert "windowTopY" in params, "Missing parameter 'windowTopY'"
    assert "maxIterations" in params, "Missing parameter 'maxIterations'"

def test_spreadsheetmlstyles::excelworkbook_has_createBackup():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "createBackup")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "createBackup" in klass.__dict__:
            descriptor = klass.__dict__["createBackup"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_protectWindows():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "protectWindows")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "protectWindows" in klass.__dict__:
            descriptor = klass.__dict__["protectWindows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_date1904():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "date1904")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "date1904" in klass.__dict__:
            descriptor = klass.__dict__["date1904"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_displayDrawingObjects():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "displayDrawingObjects")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "displayDrawingObjects" in klass.__dict__:
            descriptor = klass.__dict__["displayDrawingObjects"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_hideHorizontalScrollBar():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "hideHorizontalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "hideHorizontalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideHorizontalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_doNotSaveLinkValues():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "doNotSaveLinkValues")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "doNotSaveLinkValues" in klass.__dict__:
            descriptor = klass.__dict__["doNotSaveLinkValues"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_calculation():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "calculation")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "calculation" in klass.__dict__:
            descriptor = klass.__dict__["calculation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_activeSheet():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "activeSheet")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "activeSheet" in klass.__dict__:
            descriptor = klass.__dict__["activeSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_windowHidden():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "windowHidden")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "windowHidden" in klass.__dict__:
            descriptor = klass.__dict__["windowHidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_displayInkNotes():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "displayInkNotes")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "displayInkNotes" in klass.__dict__:
            descriptor = klass.__dict__["displayInkNotes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_windowWidth():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "windowWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "windowWidth" in klass.__dict__:
            descriptor = klass.__dict__["windowWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_tabRatio():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "tabRatio")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "tabRatio" in klass.__dict__:
            descriptor = klass.__dict__["tabRatio"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_windowHeight():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "windowHeight")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "windowHeight" in klass.__dict__:
            descriptor = klass.__dict__["windowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_selectedSheets():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "selectedSheets")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "selectedSheets" in klass.__dict__:
            descriptor = klass.__dict__["selectedSheets"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_hideVerticalScrollBar():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "hideVerticalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "hideVerticalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideVerticalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_doNotCalculateBeforeSave():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "doNotCalculateBeforeSave")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "doNotCalculateBeforeSave" in klass.__dict__:
            descriptor = klass.__dict__["doNotCalculateBeforeSave"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_protectStructure():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "protectStructure")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "protectStructure" in klass.__dict__:
            descriptor = klass.__dict__["protectStructure"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_maxChange():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "maxChange")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "maxChange" in klass.__dict__:
            descriptor = klass.__dict__["maxChange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_firstVisibleSheet():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "firstVisibleSheet")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "firstVisibleSheet" in klass.__dict__:
            descriptor = klass.__dict__["firstVisibleSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_activeChart():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "activeChart")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "activeChart" in klass.__dict__:
            descriptor = klass.__dict__["activeChart"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_hideWorkbookTabs():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "hideWorkbookTabs")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "hideWorkbookTabs" in klass.__dict__:
            descriptor = klass.__dict__["hideWorkbookTabs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_embedSaveSmartTags():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "embedSaveSmartTags")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "embedSaveSmartTags" in klass.__dict__:
            descriptor = klass.__dict__["embedSaveSmartTags"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_windowIconic():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "windowIconic")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "windowIconic" in klass.__dict__:
            descriptor = klass.__dict__["windowIconic"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_acceptLabelsInFormulas():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "acceptLabelsInFormulas")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "acceptLabelsInFormulas" in klass.__dict__:
            descriptor = klass.__dict__["acceptLabelsInFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_windowTopX():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "windowTopX")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "windowTopX" in klass.__dict__:
            descriptor = klass.__dict__["windowTopX"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_refModeR1C1():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "refModeR1C1")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "refModeR1C1" in klass.__dict__:
            descriptor = klass.__dict__["refModeR1C1"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_hidePivotTableFieldList():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "hidePivotTableFieldList")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "hidePivotTableFieldList" in klass.__dict__:
            descriptor = klass.__dict__["hidePivotTableFieldList"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_futureVer():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "futureVer")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "futureVer" in klass.__dict__:
            descriptor = klass.__dict__["futureVer"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_noAutoRecover():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "noAutoRecover")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "noAutoRecover" in klass.__dict__:
            descriptor = klass.__dict__["noAutoRecover"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_precisionAsDisplayed():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "precisionAsDisplayed")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "precisionAsDisplayed" in klass.__dict__:
            descriptor = klass.__dict__["precisionAsDisplayed"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_iteration():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "iteration")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "iteration" in klass.__dict__:
            descriptor = klass.__dict__["iteration"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_uncalced():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "uncalced")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "uncalced" in klass.__dict__:
            descriptor = klass.__dict__["uncalced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_windowTopY():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "windowTopY")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "windowTopY" in klass.__dict__:
            descriptor = klass.__dict__["windowTopY"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::excelworkbook_has_maxIterations():
    assert hasattr(SpreadsheetMLStyles::ExcelWorkbook, "maxIterations")
    descriptor = None
    for klass in SpreadsheetMLStyles::ExcelWorkbook.__mro__:
        if "maxIterations" in klass.__dict__:
            descriptor = klass.__dict__["maxIterations"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::data_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Data)


def test_spreadsheetmlstyles::data_constructor_exists():
    assert callable(SpreadsheetMLStyles::Data.__init__)


def test_spreadsheetmlstyles::data_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Data.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::comment_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Comment)


def test_spreadsheetmlstyles::comment_constructor_exists():
    assert callable(SpreadsheetMLStyles::Comment.__init__)


def test_spreadsheetmlstyles::comment_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "showAlways" in params, "Missing parameter 'showAlways'"
    assert "author" in params, "Missing parameter 'author'"

def test_spreadsheetmlstyles::comment_has_showAlways():
    assert hasattr(SpreadsheetMLStyles::Comment, "showAlways")
    descriptor = None
    for klass in SpreadsheetMLStyles::Comment.__mro__:
        if "showAlways" in klass.__dict__:
            descriptor = klass.__dict__["showAlways"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::comment_has_author():
    assert hasattr(SpreadsheetMLStyles::Comment, "author")
    descriptor = None
    for klass in SpreadsheetMLStyles::Comment.__mro__:
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



def test_spreadsheetmlstyles::column_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Column)


def test_spreadsheetmlstyles::column_constructor_exists():
    assert callable(SpreadsheetMLStyles::Column.__init__)


def test_spreadsheetmlstyles::column_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Column.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "autoFitWidth" in params, "Missing parameter 'autoFitWidth'"

def test_spreadsheetmlstyles::column_has_width():
    assert hasattr(SpreadsheetMLStyles::Column, "width")
    descriptor = None
    for klass in SpreadsheetMLStyles::Column.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::column_has_autoFitWidth():
    assert hasattr(SpreadsheetMLStyles::Column, "autoFitWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles::Column.__mro__:
        if "autoFitWidth" in klass.__dict__:
            descriptor = klass.__dict__["autoFitWidth"]
            break
    assert isinstance(descriptor, property)



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::cell_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Cell)


def test_spreadsheetmlstyles::cell_constructor_exists():
    assert callable(SpreadsheetMLStyles::Cell.__init__)


def test_spreadsheetmlstyles::cell_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Cell.__init__)
    params = list(sig.parameters.keys())
    assert "arrayRange" in params, "Missing parameter 'arrayRange'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "mergeDown" in params, "Missing parameter 'mergeDown'"
    assert "hRef" in params, "Missing parameter 'hRef'"
    assert "mergeAcross" in params, "Missing parameter 'mergeAcross'"

def test_spreadsheetmlstyles::cell_has_arrayRange():
    assert hasattr(SpreadsheetMLStyles::Cell, "arrayRange")
    descriptor = None
    for klass in SpreadsheetMLStyles::Cell.__mro__:
        if "arrayRange" in klass.__dict__:
            descriptor = klass.__dict__["arrayRange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::cell_has_formula():
    assert hasattr(SpreadsheetMLStyles::Cell, "formula")
    descriptor = None
    for klass in SpreadsheetMLStyles::Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::cell_has_mergeDown():
    assert hasattr(SpreadsheetMLStyles::Cell, "mergeDown")
    descriptor = None
    for klass in SpreadsheetMLStyles::Cell.__mro__:
        if "mergeDown" in klass.__dict__:
            descriptor = klass.__dict__["mergeDown"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::cell_has_hRef():
    assert hasattr(SpreadsheetMLStyles::Cell, "hRef")
    descriptor = None
    for klass in SpreadsheetMLStyles::Cell.__mro__:
        if "hRef" in klass.__dict__:
            descriptor = klass.__dict__["hRef"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::cell_has_mergeAcross():
    assert hasattr(SpreadsheetMLStyles::Cell, "mergeAcross")
    descriptor = None
    for klass in SpreadsheetMLStyles::Cell.__mro__:
        if "mergeAcross" in klass.__dict__:
            descriptor = klass.__dict__["mergeAcross"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::colorrowelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::ColOrRowElement)


def test_spreadsheetmlstyles::colorrowelement_constructor_exists():
    assert callable(SpreadsheetMLStyles::ColOrRowElement.__init__)


def test_spreadsheetmlstyles::colorrowelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "span" in params, "Missing parameter 'span'"

def test_spreadsheetmlstyles::colorrowelement_has_hidden():
    assert hasattr(SpreadsheetMLStyles::ColOrRowElement, "hidden")
    descriptor = None
    for klass in SpreadsheetMLStyles::ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::colorrowelement_has_span():
    assert hasattr(SpreadsheetMLStyles::ColOrRowElement, "span")
    descriptor = None
    for klass in SpreadsheetMLStyles::ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::row_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Row)


def test_spreadsheetmlstyles::row_constructor_exists():
    assert callable(SpreadsheetMLStyles::Row.__init__)


def test_spreadsheetmlstyles::row_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Row.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitHeight" in params, "Missing parameter 'autoFitHeight'"
    assert "height" in params, "Missing parameter 'height'"

def test_spreadsheetmlstyles::row_has_autoFitHeight():
    assert hasattr(SpreadsheetMLStyles::Row, "autoFitHeight")
    descriptor = None
    for klass in SpreadsheetMLStyles::Row.__mro__:
        if "autoFitHeight" in klass.__dict__:
            descriptor = klass.__dict__["autoFitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::row_has_height():
    assert hasattr(SpreadsheetMLStyles::Row, "height")
    descriptor = None
    for klass in SpreadsheetMLStyles::Row.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
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



def test_spreadsheetmlstyles::tableelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::TableElement)


def test_spreadsheetmlstyles::tableelement_constructor_exists():
    assert callable(SpreadsheetMLStyles::TableElement.__init__)


def test_spreadsheetmlstyles::tableelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_spreadsheetmlstyles::tableelement_has_index():
    assert hasattr(SpreadsheetMLStyles::TableElement, "index")
    descriptor = None
    for klass in SpreadsheetMLStyles::TableElement.__mro__:
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



def test_spreadsheetmlstyles::styledelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::StyledElement)


def test_spreadsheetmlstyles::styledelement_constructor_exists():
    assert callable(SpreadsheetMLStyles::StyledElement.__init__)


def test_spreadsheetmlstyles::styledelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::StyledElement.__init__)
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



def test_spreadsheetmlstyles::worksheet_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Worksheet)


def test_spreadsheetmlstyles::worksheet_constructor_exists():
    assert callable(SpreadsheetMLStyles::Worksheet.__init__)


def test_spreadsheetmlstyles::worksheet_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "rightToLeft" in params, "Missing parameter 'rightToLeft'"
    assert "protected" in params, "Missing parameter 'protected'"

def test_spreadsheetmlstyles::worksheet_has_name():
    assert hasattr(SpreadsheetMLStyles::Worksheet, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles::Worksheet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheet_has_rightToLeft():
    assert hasattr(SpreadsheetMLStyles::Worksheet, "rightToLeft")
    descriptor = None
    for klass in SpreadsheetMLStyles::Worksheet.__mro__:
        if "rightToLeft" in klass.__dict__:
            descriptor = klass.__dict__["rightToLeft"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::worksheet_has_protected():
    assert hasattr(SpreadsheetMLStyles::Worksheet, "protected")
    descriptor = None
    for klass in SpreadsheetMLStyles::Worksheet.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::table_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Table)


def test_spreadsheetmlstyles::table_constructor_exists():
    assert callable(SpreadsheetMLStyles::Table.__init__)


def test_spreadsheetmlstyles::table_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Table.__init__)
    params = list(sig.parameters.keys())
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"
    assert "leftCell" in params, "Missing parameter 'leftCell'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "topCell" in params, "Missing parameter 'topCell'"
    assert "expandedRowCount" in params, "Missing parameter 'expandedRowCount'"
    assert "fullRows" in params, "Missing parameter 'fullRows'"
    assert "fullColumns" in params, "Missing parameter 'fullColumns'"
    assert "expandedColumnCount" in params, "Missing parameter 'expandedColumnCount'"

def test_spreadsheetmlstyles::table_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLStyles::Table, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLStyles::Table.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::table_has_leftCell():
    assert hasattr(SpreadsheetMLStyles::Table, "leftCell")
    descriptor = None
    for klass in SpreadsheetMLStyles::Table.__mro__:
        if "leftCell" in klass.__dict__:
            descriptor = klass.__dict__["leftCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::table_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLStyles::Table, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLStyles::Table.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::table_has_topCell():
    assert hasattr(SpreadsheetMLStyles::Table, "topCell")
    descriptor = None
    for klass in SpreadsheetMLStyles::Table.__mro__:
        if "topCell" in klass.__dict__:
            descriptor = klass.__dict__["topCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::table_has_expandedRowCount():
    assert hasattr(SpreadsheetMLStyles::Table, "expandedRowCount")
    descriptor = None
    for klass in SpreadsheetMLStyles::Table.__mro__:
        if "expandedRowCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedRowCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::table_has_fullRows():
    assert hasattr(SpreadsheetMLStyles::Table, "fullRows")
    descriptor = None
    for klass in SpreadsheetMLStyles::Table.__mro__:
        if "fullRows" in klass.__dict__:
            descriptor = klass.__dict__["fullRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::table_has_fullColumns():
    assert hasattr(SpreadsheetMLStyles::Table, "fullColumns")
    descriptor = None
    for klass in SpreadsheetMLStyles::Table.__mro__:
        if "fullColumns" in klass.__dict__:
            descriptor = klass.__dict__["fullColumns"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::table_has_expandedColumnCount():
    assert hasattr(SpreadsheetMLStyles::Table, "expandedColumnCount")
    descriptor = None
    for klass in SpreadsheetMLStyles::Table.__mro__:
        if "expandedColumnCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedColumnCount"]
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



def test_spreadsheetmlstyles::smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::SmartTagsCollection)


def test_spreadsheetmlstyles::smarttagscollection_constructor_exists():
    assert callable(SpreadsheetMLStyles::SmartTagsCollection.__init__)


def test_spreadsheetmlstyles::smarttagscollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SmartTagsCollection)


def test_smarttagscollection_constructor_exists():
    assert callable(SmartTagsCollection.__init__)


def test_smarttagscollection_constructor_args():
    sig = inspect.signature(SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::SmartTagType)


def test_spreadsheetmlstyles::smarttagtype_constructor_exists():
    assert callable(SpreadsheetMLStyles::SmartTagType.__init__)


def test_spreadsheetmlstyles::smarttagtype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlstyles::smarttagtype_has_url():
    assert hasattr(SpreadsheetMLStyles::SmartTagType, "url")
    descriptor = None
    for klass in SpreadsheetMLStyles::SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::smarttagtype_has_namespaceuri():
    assert hasattr(SpreadsheetMLStyles::SmartTagType, "namespaceuri")
    descriptor = None
    for klass in SpreadsheetMLStyles::SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::smarttagtype_has_name():
    assert hasattr(SpreadsheetMLStyles::SmartTagType, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles::SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::workbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::Workbook)


def test_spreadsheetmlstyles::workbook_constructor_exists():
    assert callable(SpreadsheetMLStyles::Workbook.__init__)


def test_spreadsheetmlstyles::workbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::Workbook.__init__)
    params = list(sig.parameters.keys())



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::CustomDocumentProperty)


def test_spreadsheetmlstyles::customdocumentproperty_constructor_exists():
    assert callable(SpreadsheetMLStyles::CustomDocumentProperty.__init__)


def test_spreadsheetmlstyles::customdocumentproperty_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlstyles::customdocumentproperty_has_name():
    assert hasattr(SpreadsheetMLStyles::CustomDocumentProperty, "name")
    descriptor = None
    for klass in SpreadsheetMLStyles::CustomDocumentProperty.__mro__:
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



def test_spreadsheetmlstyles::customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::CustomDocumentPropertiesCollection)


def test_spreadsheetmlstyles::customdocumentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLStyles::CustomDocumentPropertiesCollection.__init__)


def test_spreadsheetmlstyles::customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::CustomDocumentPropertiesCollection.__init__)
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



def test_spreadsheetmlstyles::documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::DocumentPropertiesCollection)


def test_spreadsheetmlstyles::documentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLStyles::DocumentPropertiesCollection.__init__)


def test_spreadsheetmlstyles::documentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "description" in params, "Missing parameter 'description'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "lines" in params, "Missing parameter 'lines'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "words" in params, "Missing parameter 'words'"
    assert "revision" in params, "Missing parameter 'revision'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "category" in params, "Missing parameter 'category'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "author" in params, "Missing parameter 'author'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "title" in params, "Missing parameter 'title'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "company" in params, "Missing parameter 'company'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_spreadsheetmlstyles::documentpropertiescollection_has_lastAuthor():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_description():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_keywords():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_presentationFormat():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_bytes():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_lines():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_characters():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_words():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_revision():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_manager():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_category():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_totalTime():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_author():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_appName():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_guid():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_paragraphs():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_title():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_subject():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_company():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::documentpropertiescollection_has_pages():
    assert hasattr(SpreadsheetMLStyles::DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in SpreadsheetMLStyles::DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
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



def test_spreadsheetmlstyles::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::BooleanValue)


def test_spreadsheetmlstyles::booleanvalue_constructor_exists():
    assert callable(SpreadsheetMLStyles::BooleanValue.__init__)


def test_spreadsheetmlstyles::booleanvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlstyles::booleanvalue_has_value():
    assert hasattr(SpreadsheetMLStyles::BooleanValue, "value")
    descriptor = None
    for klass in SpreadsheetMLStyles::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::DateTimeTypeValue)


def test_spreadsheetmlstyles::datetimetypevalue_constructor_exists():
    assert callable(SpreadsheetMLStyles::DateTimeTypeValue.__init__)


def test_spreadsheetmlstyles::datetimetypevalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::numbervalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::NumberValue)


def test_spreadsheetmlstyles::numbervalue_constructor_exists():
    assert callable(SpreadsheetMLStyles::NumberValue.__init__)


def test_spreadsheetmlstyles::numbervalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlstyles::numbervalue_has_value():
    assert hasattr(SpreadsheetMLStyles::NumberValue, "value")
    descriptor = None
    for klass in SpreadsheetMLStyles::NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::errorvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::ErrorValue)


def test_spreadsheetmlstyles::errorvalue_constructor_exists():
    assert callable(SpreadsheetMLStyles::ErrorValue.__init__)


def test_spreadsheetmlstyles::errorvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::stringvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::StringValue)


def test_spreadsheetmlstyles::stringvalue_constructor_exists():
    assert callable(SpreadsheetMLStyles::StringValue.__init__)


def test_spreadsheetmlstyles::stringvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlstyles::stringvalue_has_value():
    assert hasattr(SpreadsheetMLStyles::StringValue, "value")
    descriptor = None
    for klass in SpreadsheetMLStyles::StringValue.__mro__:
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



def test_spreadsheetmlstyles::valuetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::ValueType)


def test_spreadsheetmlstyles::valuetype_constructor_exists():
    assert callable(SpreadsheetMLStyles::ValueType.__init__)


def test_spreadsheetmlstyles::valuetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlstyles::versiontype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::VersionType)


def test_spreadsheetmlstyles::versiontype_constructor_exists():
    assert callable(SpreadsheetMLStyles::VersionType.__init__)


def test_spreadsheetmlstyles::versiontype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "nn" in params, "Missing parameter 'nn'"
    assert "n" in params, "Missing parameter 'n'"

def test_spreadsheetmlstyles::versiontype_has_nn():
    assert hasattr(SpreadsheetMLStyles::VersionType, "nn")
    descriptor = None
    for klass in SpreadsheetMLStyles::VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::versiontype_has_n():
    assert hasattr(SpreadsheetMLStyles::VersionType, "n")
    descriptor = None
    for klass in SpreadsheetMLStyles::VersionType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlstyles::datetimetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLStyles::DateTimeType)


def test_spreadsheetmlstyles::datetimetype_constructor_exists():
    assert callable(SpreadsheetMLStyles::DateTimeType.__init__)


def test_spreadsheetmlstyles::datetimetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLStyles::DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "year" in params, "Missing parameter 'year'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "second" in params, "Missing parameter 'second'"
    assert "day" in params, "Missing parameter 'day'"
    assert "minute" in params, "Missing parameter 'minute'"

def test_spreadsheetmlstyles::datetimetype_has_month():
    assert hasattr(SpreadsheetMLStyles::DateTimeType, "month")
    descriptor = None
    for klass in SpreadsheetMLStyles::DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::datetimetype_has_year():
    assert hasattr(SpreadsheetMLStyles::DateTimeType, "year")
    descriptor = None
    for klass in SpreadsheetMLStyles::DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::datetimetype_has_hour():
    assert hasattr(SpreadsheetMLStyles::DateTimeType, "hour")
    descriptor = None
    for klass in SpreadsheetMLStyles::DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::datetimetype_has_second():
    assert hasattr(SpreadsheetMLStyles::DateTimeType, "second")
    descriptor = None
    for klass in SpreadsheetMLStyles::DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::datetimetype_has_day():
    assert hasattr(SpreadsheetMLStyles::DateTimeType, "day")
    descriptor = None
    for klass in SpreadsheetMLStyles::DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlstyles::datetimetype_has_minute():
    assert hasattr(SpreadsheetMLStyles::DateTimeType, "minute")
    descriptor = None
    for klass in SpreadsheetMLStyles::DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_patterntype_exists():
    # Check that the Enumeration exists
    assert PatternType is not None

def test_patterntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PatternType]
    expected_literals = [
        "pt_Gray75",
        "pt_ThinHorzCross",
        "pt_ThinVertStripe",
        "pt_Gray50",
        "pt_Gray0625",
        "pt_DiagStripe",
        "pt_ThinHorzStripe",
        "pt_Gray25",
        "pt_ReverseDiagStripe",
        "pt_Gray125",
        "pt_ThinDiagStripe",
        "pt_ThickDiagCross",
        "pt_VertStripe",
        "pt_DiagCross",
        "pt_None",
        "pt_ThinReverseDiagStripe",
        "pt_ThinDiagCross",
        "pt_HorzStripe",
        "pt_Solid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PatternType"

def test_displaydrawingobjectstype_exists():
    # Check that the Enumeration exists
    assert DisplayDrawingObjectsType is not None

def test_displaydrawingobjectstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DisplayDrawingObjectsType]
    expected_literals = [
        "ddot_displayShapes",
        "ddot_hideAll",
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
        "lst_DashDotDot",
        "lst_Double",
        "lst_Continuous",
        "lst_Dash",
        "lst_None",
        "lst_Dot",
        "lst_DashDot",
        "lst_SlantDashDot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyleType"

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
        "vt_SheetVisible",
        "vt_SheetVeryHidden",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibleType"

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

def test_verticalalignementtype_exists():
    # Check that the Enumeration exists
    assert VerticalAlignementType is not None

def test_verticalalignementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VerticalAlignementType]
    expected_literals = [
        "vat_Distributed",
        "vat_Center",
        "vat_Top",
        "vat_Automatic",
        "vat_Bottom",
        "vat_JustifyDistributed",
        "vat_Justify",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VerticalAlignementType"

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

def test_calculationworkbooktype_exists():
    # Check that the Enumeration exists
    assert CalculationWorkbookType is not None

def test_calculationworkbooktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CalculationWorkbookType]
    expected_literals = [
        "cwt_automaticCalculation",
        "cwt_manualCalculation",
        "cwt_semiAutomaticCalculation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CalculationWorkbookType"

def test_verticalaligntype_exists():
    # Check that the Enumeration exists
    assert VerticalAlignType is not None

def test_verticalaligntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VerticalAlignType]
    expected_literals = [
        "vat_Superscript",
        "vat_None",
        "vat_Subscript",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VerticalAlignType"

def test_excelnumberformattype_exists():
    # Check that the Enumeration exists
    assert ExcelNumberFormatType is not None

def test_excelnumberformattype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExcelNumberFormatType]
    expected_literals = [
        "enft_Scientific",
        "enft_Euro_Currency",
        "enft_Yes_No",
        "enft_Short_Date",
        "enft_Long_Time",
        "enft_General",
        "enft_Currency",
        "enft_Medium_Date",
        "enft_Long_Date",
        "enft_Medium_Time",
        "enft_Short_Time",
        "enft_Percent",
        "enft_General_Number",
        "enft_True_False",
        "enft_On_Off",
        "enft_General_Date",
        "enft_Fixed",
        "enft_Standard",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExcelNumberFormatType"

def test_excelworksheettypetype_exists():
    # Check that the Enumeration exists
    assert ExcelWorksheetTypeType is not None

def test_excelworksheettypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExcelWorksheetTypeType]
    expected_literals = [
        "ewt_Worksheet",
        "ewt_Chart",
        "ewt_Dialog",
        "ewt_Macro",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExcelWorksheetTypeType"

def test_enableselectiontype_exists():
    # Check that the Enumeration exists
    assert EnableSelectionType is not None

def test_enableselectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnableSelectionType]
    expected_literals = [
        "est_UnlockedCells",
        "est_NoSelection",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnableSelectionType"

def test_underlinetype_exists():
    # Check that the Enumeration exists
    assert UnderlineType is not None

def test_underlinetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnderlineType]
    expected_literals = [
        "ut_None",
        "ut_Single",
        "ut_Double",
        "ut_DoubleAccounting",
        "ut_SingleAccounting",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnderlineType"

def test_positiontype_exists():
    # Check that the Enumeration exists
    assert PositionType is not None

def test_positiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PositionType]
    expected_literals = [
        "pt_Bottom",
        "pt_Right",
        "pt_Left",
        "pt_DiagonalLeft",
        "pt_Top",
        "pt_DiagonalRight",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PositionType"

def test_horizontalalignementtype_exists():
    # Check that the Enumeration exists
    assert HorizontalAlignementType is not None

def test_horizontalalignementtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HorizontalAlignementType]
    expected_literals = [
        "hat_JustifyDistributed",
        "hat_Left",
        "hat_Fill",
        "hat_Right",
        "hat_Distributed",
        "hat_Justify",
        "hat_CenterAcrossSelection",
        "hat_Center",
        "hat_Automatic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HorizontalAlignementType"


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
SpreadsheetMLStyles::NamedRange_strategy = st.builds(
    SpreadsheetMLStyles::NamedRange,
    name=
        safe_text,
    hidden=
        safe_text,
    refersTo=
        safe_text
)
SpreadsheetMLStyles::NamesType_strategy = st.builds(
    SpreadsheetMLStyles::NamesType,
)
NamedRange_strategy = st.builds(
    NamedRange,
)
SpreadsheetMLStyles::NumberFormatType_strategy = st.builds(
    SpreadsheetMLStyles::NumberFormatType,
    format=
        safe_text
)
SpreadsheetMLStyles::InteriorType_strategy = st.builds(
    SpreadsheetMLStyles::InteriorType,
    patternColor=
        safe_text,
    pattern=
        safe_text,
    color=
        safe_text
)
SpreadsheetMLStyles::FontType_strategy = st.builds(
    SpreadsheetMLStyles::FontType,
    outline=
        safe_text,
    fontName=
        safe_text,
    color=
        safe_text,
    strikeThrough=
        safe_text,
    shadow=
        safe_text,
    italic=
        safe_text,
    verticalAlign=
        safe_text,
    size=
        safe_text,
    underline=
        safe_text,
    bold=
        safe_text
)
BorderType_strategy = st.builds(
    BorderType,
)
SpreadsheetMLStyles::BordersType_strategy = st.builds(
    SpreadsheetMLStyles::BordersType,
)
SpreadsheetMLStyles::BorderType_strategy = st.builds(
    SpreadsheetMLStyles::BorderType,
    weight=
        safe_text,
    color=
        safe_text,
    position=
        safe_text,
    lineStyle=
        safe_text
)
SpreadsheetMLStyles::AlignmentType_strategy = st.builds(
    SpreadsheetMLStyles::AlignmentType,
    vertical=
        safe_text,
    horizontal=
        safe_text,
    wrapText=
        safe_text,
    indent=
        safe_text,
    shrinkToFit=
        safe_text,
    verticalText=
        safe_text,
    readingOrder=
        safe_text,
    rotate=
        safe_text
)
FontType_strategy = st.builds(
    FontType,
)
SpreadsheetMLStyles::ProtectionType_strategy = st.builds(
    SpreadsheetMLStyles::ProtectionType,
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
SpreadsheetMLStyles::StyleType_strategy = st.builds(
    SpreadsheetMLStyles::StyleType,
    id=
        safe_text,
    name=
        safe_text
)
SpreadsheetMLStyles::StylesCollection_strategy = st.builds(
    SpreadsheetMLStyles::StylesCollection,
)
SpreadsheetMLStyles::Print_strategy = st.builds(
    SpreadsheetMLStyles::Print,
    fitHeight=
        safe_text,
    gridlines=
        safe_text,
    validPrinterInfo=
        safe_text,
    commentsLayout=
        safe_text,
    scale=
        safe_text,
    numberOfCopies=
        safe_text,
    blackAndWhite=
        safe_text,
    verticalResolution=
        safe_text,
    rowColHeadings=
        safe_text,
    leftToRight=
        safe_text,
    fitWidth=
        safe_text,
    draftQuality=
        safe_text,
    horizontalResolution=
        safe_text,
    paperSizeIndex=
        safe_text,
    printErrors=
        safe_text
)
SpreadsheetMLStyles::PageMarginsInfo_strategy = st.builds(
    SpreadsheetMLStyles::PageMarginsInfo,
    right=
        safe_text,
    top=
        safe_text,
    bottom=
        safe_text,
    left=
        safe_text
)
HeaderOrFooterElt_strategy = st.builds(
    HeaderOrFooterElt,
)
SpreadsheetMLStyles::Footer_strategy = st.builds(
    SpreadsheetMLStyles::Footer,
)
SpreadsheetMLStyles::Header_strategy = st.builds(
    SpreadsheetMLStyles::Header,
)
SpreadsheetMLStyles::HeaderOrFooterElt_strategy = st.builds(
    SpreadsheetMLStyles::HeaderOrFooterElt,
    margin=
        safe_text,
    data=
        safe_text
)
Layout_strategy = st.builds(
    Layout,
)
SpreadsheetMLStyles::PageSetup_strategy = st.builds(
    SpreadsheetMLStyles::PageSetup,
)
SpreadsheetMLStyles::Layout_strategy = st.builds(
    SpreadsheetMLStyles::Layout,
    startPageNumber=
        safe_text,
    orientation=
        safe_text,
    centerVertical=
        safe_text,
    centerHorizontal=
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
SpreadsheetMLStyles::WorksheetOptionsElt_strategy = st.builds(
    SpreadsheetMLStyles::WorksheetOptionsElt,
    protectObjects=
        safe_text,
    splitVertical=
        safe_text,
    doNotDisplayZeros=
        safe_text,
    freezePanes=
        safe_text,
    activePane=
        safe_text,
    standardWidth=
        safe_text,
    allowInsertRows=
        safe_text,
    allowInsertHyperlinks=
        safe_text,
    zoom=
        safe_text,
    activeRow=
        safe_text,
    tabColorIndex=
        safe_text,
    unsynced=
        safe_text,
    noSummaryColumnsRightDetail=
        safe_text,
    pageBreakZoom=
        safe_text,
    allowSort=
        safe_text,
    frozenNoSplit=
        safe_text,
    displayPageBreak=
        safe_text,
    applyAutomaticOutlineStyles=
        safe_text,
    filterOn=
        safe_text,
    activeColumn=
        safe_text,
    protectScenarios=
        safe_text,
    noSummaryRowsBelowDetail=
        safe_text,
    splitHorizontal=
        safe_text,
    doNotDisplayHeadings=
        safe_text,
    protectContentst=
        safe_text,
    doNotDisplayOutline=
        safe_text,
    showPageBreakZoom=
        safe_text,
    displayRightToLeft=
        safe_text,
    displayFormulas=
        safe_text,
    defaultRowHeight=
        safe_text,
    allowInsertCols=
        safe_text,
    topRowVisible=
        safe_text,
    codeName=
        safe_text,
    transitionFormulaEntry=
        safe_text,
    gridlineColorIndex=
        safe_text,
    fitToPage=
        safe_text,
    allowSizeRows=
        safe_text,
    topRowBottomPane=
        safe_text,
    allowUsePivotTables=
        safe_text,
    gridlineColor=
        safe_text,
    enableSelection=
        safe_text,
    selected=
        safe_text,
    allowDeleteRows=
        safe_text,
    doNotDisplayColHeaders=
        safe_text,
    excelWorksheetType=
        safe_text,
    intlMacro=
        safe_text,
    doNotDisplayGridlines=
        safe_text,
    doNotDisplayRowHeaders=
        safe_text,
    allowSizeCols=
        safe_text,
    leftColumnRightPane=
        safe_text,
    name=
        safe_text,
    transitionExpressionEvaluation=
        safe_text,
    allowFormatCells=
        safe_text,
    allowFilter=
        safe_text,
    rangeSelection=
        safe_text,
    leftColumnVisible=
        safe_text,
    defaultColumnWidth=
        safe_text,
    visible=
        safe_text,
    allowDeleteCols=
        safe_text
)
SpreadsheetMLStyles::ExcelWorkbook_strategy = st.builds(
    SpreadsheetMLStyles::ExcelWorkbook,
    createBackup=
        safe_text,
    protectWindows=
        safe_text,
    date1904=
        safe_text,
    displayDrawingObjects=
        safe_text,
    hideHorizontalScrollBar=
        safe_text,
    doNotSaveLinkValues=
        safe_text,
    calculation=
        safe_text,
    activeSheet=
        safe_text,
    windowHidden=
        safe_text,
    displayInkNotes=
        safe_text,
    windowWidth=
        safe_text,
    tabRatio=
        safe_text,
    windowHeight=
        safe_text,
    selectedSheets=
        safe_text,
    hideVerticalScrollBar=
        safe_text,
    doNotCalculateBeforeSave=
        safe_text,
    protectStructure=
        safe_text,
    maxChange=
        safe_text,
    firstVisibleSheet=
        safe_text,
    activeChart=
        safe_text,
    hideWorkbookTabs=
        safe_text,
    embedSaveSmartTags=
        safe_text,
    windowIconic=
        safe_text,
    acceptLabelsInFormulas=
        safe_text,
    windowTopX=
        safe_text,
    refModeR1C1=
        safe_text,
    hidePivotTableFieldList=
        safe_text,
    futureVer=
        safe_text,
    noAutoRecover=
        safe_text,
    precisionAsDisplayed=
        safe_text,
    iteration=
        safe_text,
    uncalced=
        safe_text,
    windowTopY=
        safe_text,
    maxIterations=
        safe_text
)
SpreadsheetMLStyles::Data_strategy = st.builds(
    SpreadsheetMLStyles::Data,
)
Comment_strategy = st.builds(
    Comment,
)
SpreadsheetMLStyles::Comment_strategy = st.builds(
    SpreadsheetMLStyles::Comment,
    showAlways=
        safe_text,
    author=
        safe_text
)
ColOrRowElement_strategy = st.builds(
    ColOrRowElement,
)
SpreadsheetMLStyles::Column_strategy = st.builds(
    SpreadsheetMLStyles::Column,
    width=
        safe_text,
    autoFitWidth=
        safe_text
)
TableElement_strategy = st.builds(
    TableElement,
)
SpreadsheetMLStyles::Cell_strategy = st.builds(
    SpreadsheetMLStyles::Cell,
    arrayRange=
        safe_text,
    formula=
        safe_text,
    mergeDown=
        safe_text,
    hRef=
        safe_text,
    mergeAcross=
        safe_text
)
SpreadsheetMLStyles::ColOrRowElement_strategy = st.builds(
    SpreadsheetMLStyles::ColOrRowElement,
    hidden=
        safe_text,
    span=
        safe_text
)
SpreadsheetMLStyles::Row_strategy = st.builds(
    SpreadsheetMLStyles::Row,
    autoFitHeight=
        safe_text,
    height=
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
SpreadsheetMLStyles::TableElement_strategy = st.builds(
    SpreadsheetMLStyles::TableElement,
    index=
        safe_text
)
StyleType_strategy = st.builds(
    StyleType,
)
SpreadsheetMLStyles::StyledElement_strategy = st.builds(
    SpreadsheetMLStyles::StyledElement,
)
WorksheetOptionsElt_strategy = st.builds(
    WorksheetOptionsElt,
)
Table_strategy = st.builds(
    Table,
)
SpreadsheetMLStyles::Worksheet_strategy = st.builds(
    SpreadsheetMLStyles::Worksheet,
    name=
        safe_text,
    rightToLeft=
        safe_text,
    protected=
        safe_text
)
SpreadsheetMLStyles::Table_strategy = st.builds(
    SpreadsheetMLStyles::Table,
    defaultColumnWidth=
        safe_text,
    leftCell=
        safe_text,
    defaultRowHeight=
        safe_text,
    topCell=
        safe_text,
    expandedRowCount=
        safe_text,
    fullRows=
        safe_text,
    fullColumns=
        safe_text,
    expandedColumnCount=
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
SpreadsheetMLStyles::SmartTagsCollection_strategy = st.builds(
    SpreadsheetMLStyles::SmartTagsCollection,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)
SpreadsheetMLStyles::SmartTagType_strategy = st.builds(
    SpreadsheetMLStyles::SmartTagType,
    url=
        safe_text,
    namespaceuri=
        safe_text,
    name=
        safe_text
)
SpreadsheetMLStyles::Workbook_strategy = st.builds(
    SpreadsheetMLStyles::Workbook,
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
SpreadsheetMLStyles::CustomDocumentProperty_strategy = st.builds(
    SpreadsheetMLStyles::CustomDocumentProperty,
    name=
        safe_text
)
CustomDocumentProperty_strategy = st.builds(
    CustomDocumentProperty,
)
SpreadsheetMLStyles::CustomDocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLStyles::CustomDocumentPropertiesCollection,
)
VersionType_strategy = st.builds(
    VersionType,
)
Workbook_strategy = st.builds(
    Workbook,
)
SpreadsheetMLStyles::DocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLStyles::DocumentPropertiesCollection,
    lastAuthor=
        safe_text,
    description=
        safe_text,
    keywords=
        safe_text,
    presentationFormat=
        safe_text,
    charactersWithSpaces=
        safe_text,
    bytes=
        safe_text,
    lines=
        safe_text,
    characters=
        safe_text,
    words=
        safe_text,
    revision=
        safe_text,
    manager=
        safe_text,
    hyperlinkBase=
        safe_text,
    category=
        safe_text,
    totalTime=
        safe_text,
    author=
        safe_text,
    appName=
        safe_text,
    guid=
        safe_text,
    paragraphs=
        safe_text,
    title=
        safe_text,
    subject=
        safe_text,
    company=
        safe_text,
    pages=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
ValueType_strategy = st.builds(
    ValueType,
)
SpreadsheetMLStyles::BooleanValue_strategy = st.builds(
    SpreadsheetMLStyles::BooleanValue,
    value=
        safe_text
)
SpreadsheetMLStyles::DateTimeTypeValue_strategy = st.builds(
    SpreadsheetMLStyles::DateTimeTypeValue,
)
SpreadsheetMLStyles::NumberValue_strategy = st.builds(
    SpreadsheetMLStyles::NumberValue,
    value=
        safe_text
)
SpreadsheetMLStyles::ErrorValue_strategy = st.builds(
    SpreadsheetMLStyles::ErrorValue,
)
SpreadsheetMLStyles::StringValue_strategy = st.builds(
    SpreadsheetMLStyles::StringValue,
    value=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
SpreadsheetMLStyles::ValueType_strategy = st.builds(
    SpreadsheetMLStyles::ValueType,
)
SpreadsheetMLStyles::VersionType_strategy = st.builds(
    SpreadsheetMLStyles::VersionType,
    nn=
        safe_text,
    n=
        safe_text
)
SpreadsheetMLStyles::DateTimeType_strategy = st.builds(
    SpreadsheetMLStyles::DateTimeType,
    month=
        safe_text,
    year=
        safe_text,
    hour=
        safe_text,
    second=
        safe_text,
    day=
        safe_text,
    minute=
        safe_text
)

@given(instance=SpreadsheetMLStyles::NamedRange_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::namedrange_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::NamedRange)

@given(instance=SpreadsheetMLStyles::NamedRange_strategy)
def test_spreadsheetmlstyles::namedrange_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLStyles::NamedRange_strategy)
def test_spreadsheetmlstyles::namedrange_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLStyles::NamedRange_strategy)
def test_spreadsheetmlstyles::namedrange_hidden_type(instance):
    assert isinstance(instance.hidden, str)


@given(instance=SpreadsheetMLStyles::NamedRange_strategy)
def test_spreadsheetmlstyles::namedrange_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=SpreadsheetMLStyles::NamedRange_strategy)
def test_spreadsheetmlstyles::namedrange_refersTo_type(instance):
    assert isinstance(instance.refersTo, str)


@given(instance=SpreadsheetMLStyles::NamedRange_strategy)
def test_spreadsheetmlstyles::namedrange_refersTo_setter(instance):
    original = instance.refersTo
    instance.refersTo = original
    assert instance.refersTo == original

@given(instance=SpreadsheetMLStyles::NamesType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::namestype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::NamesType)

@given(instance=NamedRange_strategy)
@settings(max_examples=50)
def test_namedrange_instantiation(instance):
    assert isinstance(instance, NamedRange)

@given(instance=SpreadsheetMLStyles::NumberFormatType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::numberformattype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::NumberFormatType)

@given(instance=SpreadsheetMLStyles::NumberFormatType_strategy)
def test_spreadsheetmlstyles::numberformattype_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=SpreadsheetMLStyles::NumberFormatType_strategy)
def test_spreadsheetmlstyles::numberformattype_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=SpreadsheetMLStyles::InteriorType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::interiortype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::InteriorType)

@given(instance=SpreadsheetMLStyles::InteriorType_strategy)
def test_spreadsheetmlstyles::interiortype_patternColor_type(instance):
    assert isinstance(instance.patternColor, str)


@given(instance=SpreadsheetMLStyles::InteriorType_strategy)
def test_spreadsheetmlstyles::interiortype_patternColor_setter(instance):
    original = instance.patternColor
    instance.patternColor = original
    assert instance.patternColor == original

@given(instance=SpreadsheetMLStyles::InteriorType_strategy)
def test_spreadsheetmlstyles::interiortype_pattern_type(instance):
    assert isinstance(instance.pattern, str)


@given(instance=SpreadsheetMLStyles::InteriorType_strategy)
def test_spreadsheetmlstyles::interiortype_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=SpreadsheetMLStyles::InteriorType_strategy)
def test_spreadsheetmlstyles::interiortype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=SpreadsheetMLStyles::InteriorType_strategy)
def test_spreadsheetmlstyles::interiortype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=SpreadsheetMLStyles::FontType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::fonttype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::FontType)

@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_outline_type(instance):
    assert isinstance(instance.outline, str)


@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original

@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_fontName_type(instance):
    assert isinstance(instance.fontName, str)


@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original

@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_strikeThrough_type(instance):
    assert isinstance(instance.strikeThrough, str)


@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_strikeThrough_setter(instance):
    original = instance.strikeThrough
    instance.strikeThrough = original
    assert instance.strikeThrough == original

@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_shadow_type(instance):
    assert isinstance(instance.shadow, str)


@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_shadow_setter(instance):
    original = instance.shadow
    instance.shadow = original
    assert instance.shadow == original

@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_italic_type(instance):
    assert isinstance(instance.italic, str)


@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_italic_setter(instance):
    original = instance.italic
    instance.italic = original
    assert instance.italic == original

@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_verticalAlign_type(instance):
    assert isinstance(instance.verticalAlign, str)


@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_verticalAlign_setter(instance):
    original = instance.verticalAlign
    instance.verticalAlign = original
    assert instance.verticalAlign == original

@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_underline_type(instance):
    assert isinstance(instance.underline, str)


@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_underline_setter(instance):
    original = instance.underline
    instance.underline = original
    assert instance.underline == original

@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_bold_type(instance):
    assert isinstance(instance.bold, str)


@given(instance=SpreadsheetMLStyles::FontType_strategy)
def test_spreadsheetmlstyles::fonttype_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original

@given(instance=BorderType_strategy)
@settings(max_examples=50)
def test_bordertype_instantiation(instance):
    assert isinstance(instance, BorderType)

@given(instance=SpreadsheetMLStyles::BordersType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::borderstype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::BordersType)

@given(instance=SpreadsheetMLStyles::BorderType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::bordertype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::BorderType)

@given(instance=SpreadsheetMLStyles::BorderType_strategy)
def test_spreadsheetmlstyles::bordertype_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=SpreadsheetMLStyles::BorderType_strategy)
def test_spreadsheetmlstyles::bordertype_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=SpreadsheetMLStyles::BorderType_strategy)
def test_spreadsheetmlstyles::bordertype_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=SpreadsheetMLStyles::BorderType_strategy)
def test_spreadsheetmlstyles::bordertype_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=SpreadsheetMLStyles::BorderType_strategy)
def test_spreadsheetmlstyles::bordertype_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=SpreadsheetMLStyles::BorderType_strategy)
def test_spreadsheetmlstyles::bordertype_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=SpreadsheetMLStyles::BorderType_strategy)
def test_spreadsheetmlstyles::bordertype_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=SpreadsheetMLStyles::BorderType_strategy)
def test_spreadsheetmlstyles::bordertype_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::alignmenttype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::AlignmentType)

@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_vertical_type(instance):
    assert isinstance(instance.vertical, str)


@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original

@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_horizontal_type(instance):
    assert isinstance(instance.horizontal, str)


@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_horizontal_setter(instance):
    original = instance.horizontal
    instance.horizontal = original
    assert instance.horizontal == original

@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_wrapText_type(instance):
    assert isinstance(instance.wrapText, str)


@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_wrapText_setter(instance):
    original = instance.wrapText
    instance.wrapText = original
    assert instance.wrapText == original

@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_indent_type(instance):
    assert isinstance(instance.indent, str)


@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_indent_setter(instance):
    original = instance.indent
    instance.indent = original
    assert instance.indent == original

@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_shrinkToFit_type(instance):
    assert isinstance(instance.shrinkToFit, str)


@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_shrinkToFit_setter(instance):
    original = instance.shrinkToFit
    instance.shrinkToFit = original
    assert instance.shrinkToFit == original

@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_verticalText_type(instance):
    assert isinstance(instance.verticalText, str)


@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_verticalText_setter(instance):
    original = instance.verticalText
    instance.verticalText = original
    assert instance.verticalText == original

@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_readingOrder_type(instance):
    assert isinstance(instance.readingOrder, str)


@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_readingOrder_setter(instance):
    original = instance.readingOrder
    instance.readingOrder = original
    assert instance.readingOrder == original

@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_rotate_type(instance):
    assert isinstance(instance.rotate, str)


@given(instance=SpreadsheetMLStyles::AlignmentType_strategy)
def test_spreadsheetmlstyles::alignmenttype_rotate_setter(instance):
    original = instance.rotate
    instance.rotate = original
    assert instance.rotate == original

@given(instance=FontType_strategy)
@settings(max_examples=50)
def test_fonttype_instantiation(instance):
    assert isinstance(instance, FontType)

@given(instance=SpreadsheetMLStyles::ProtectionType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::protectiontype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::ProtectionType)

@given(instance=SpreadsheetMLStyles::ProtectionType_strategy)
def test_spreadsheetmlstyles::protectiontype_protected_type(instance):
    assert isinstance(instance.protected, str)


@given(instance=SpreadsheetMLStyles::ProtectionType_strategy)
def test_spreadsheetmlstyles::protectiontype_protected_setter(instance):
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

@given(instance=SpreadsheetMLStyles::StyleType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::styletype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::StyleType)

@given(instance=SpreadsheetMLStyles::StyleType_strategy)
def test_spreadsheetmlstyles::styletype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=SpreadsheetMLStyles::StyleType_strategy)
def test_spreadsheetmlstyles::styletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=SpreadsheetMLStyles::StyleType_strategy)
def test_spreadsheetmlstyles::styletype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLStyles::StyleType_strategy)
def test_spreadsheetmlstyles::styletype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLStyles::StylesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::stylescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::StylesCollection)

@given(instance=SpreadsheetMLStyles::Print_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::print_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Print)

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_fitHeight_type(instance):
    assert isinstance(instance.fitHeight, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_fitHeight_setter(instance):
    original = instance.fitHeight
    instance.fitHeight = original
    assert instance.fitHeight == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_gridlines_type(instance):
    assert isinstance(instance.gridlines, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_gridlines_setter(instance):
    original = instance.gridlines
    instance.gridlines = original
    assert instance.gridlines == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_validPrinterInfo_type(instance):
    assert isinstance(instance.validPrinterInfo, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_validPrinterInfo_setter(instance):
    original = instance.validPrinterInfo
    instance.validPrinterInfo = original
    assert instance.validPrinterInfo == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_commentsLayout_type(instance):
    assert isinstance(instance.commentsLayout, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_commentsLayout_setter(instance):
    original = instance.commentsLayout
    instance.commentsLayout = original
    assert instance.commentsLayout == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_scale_type(instance):
    assert isinstance(instance.scale, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_numberOfCopies_type(instance):
    assert isinstance(instance.numberOfCopies, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_numberOfCopies_setter(instance):
    original = instance.numberOfCopies
    instance.numberOfCopies = original
    assert instance.numberOfCopies == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_blackAndWhite_type(instance):
    assert isinstance(instance.blackAndWhite, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_blackAndWhite_setter(instance):
    original = instance.blackAndWhite
    instance.blackAndWhite = original
    assert instance.blackAndWhite == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_verticalResolution_type(instance):
    assert isinstance(instance.verticalResolution, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_verticalResolution_setter(instance):
    original = instance.verticalResolution
    instance.verticalResolution = original
    assert instance.verticalResolution == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_rowColHeadings_type(instance):
    assert isinstance(instance.rowColHeadings, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_rowColHeadings_setter(instance):
    original = instance.rowColHeadings
    instance.rowColHeadings = original
    assert instance.rowColHeadings == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_leftToRight_type(instance):
    assert isinstance(instance.leftToRight, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_leftToRight_setter(instance):
    original = instance.leftToRight
    instance.leftToRight = original
    assert instance.leftToRight == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_fitWidth_type(instance):
    assert isinstance(instance.fitWidth, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_fitWidth_setter(instance):
    original = instance.fitWidth
    instance.fitWidth = original
    assert instance.fitWidth == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_draftQuality_type(instance):
    assert isinstance(instance.draftQuality, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_draftQuality_setter(instance):
    original = instance.draftQuality
    instance.draftQuality = original
    assert instance.draftQuality == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_horizontalResolution_type(instance):
    assert isinstance(instance.horizontalResolution, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_horizontalResolution_setter(instance):
    original = instance.horizontalResolution
    instance.horizontalResolution = original
    assert instance.horizontalResolution == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_paperSizeIndex_type(instance):
    assert isinstance(instance.paperSizeIndex, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_paperSizeIndex_setter(instance):
    original = instance.paperSizeIndex
    instance.paperSizeIndex = original
    assert instance.paperSizeIndex == original

@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_printErrors_type(instance):
    assert isinstance(instance.printErrors, str)


@given(instance=SpreadsheetMLStyles::Print_strategy)
def test_spreadsheetmlstyles::print_printErrors_setter(instance):
    original = instance.printErrors
    instance.printErrors = original
    assert instance.printErrors == original

@given(instance=SpreadsheetMLStyles::PageMarginsInfo_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::pagemarginsinfo_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::PageMarginsInfo)

@given(instance=SpreadsheetMLStyles::PageMarginsInfo_strategy)
def test_spreadsheetmlstyles::pagemarginsinfo_right_type(instance):
    assert isinstance(instance.right, str)


@given(instance=SpreadsheetMLStyles::PageMarginsInfo_strategy)
def test_spreadsheetmlstyles::pagemarginsinfo_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=SpreadsheetMLStyles::PageMarginsInfo_strategy)
def test_spreadsheetmlstyles::pagemarginsinfo_top_type(instance):
    assert isinstance(instance.top, str)


@given(instance=SpreadsheetMLStyles::PageMarginsInfo_strategy)
def test_spreadsheetmlstyles::pagemarginsinfo_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original

@given(instance=SpreadsheetMLStyles::PageMarginsInfo_strategy)
def test_spreadsheetmlstyles::pagemarginsinfo_bottom_type(instance):
    assert isinstance(instance.bottom, str)


@given(instance=SpreadsheetMLStyles::PageMarginsInfo_strategy)
def test_spreadsheetmlstyles::pagemarginsinfo_bottom_setter(instance):
    original = instance.bottom
    instance.bottom = original
    assert instance.bottom == original

@given(instance=SpreadsheetMLStyles::PageMarginsInfo_strategy)
def test_spreadsheetmlstyles::pagemarginsinfo_left_type(instance):
    assert isinstance(instance.left, str)


@given(instance=SpreadsheetMLStyles::PageMarginsInfo_strategy)
def test_spreadsheetmlstyles::pagemarginsinfo_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=HeaderOrFooterElt_strategy)
@settings(max_examples=50)
def test_headerorfooterelt_instantiation(instance):
    assert isinstance(instance, HeaderOrFooterElt)

@given(instance=SpreadsheetMLStyles::Footer_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::footer_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Footer)

@given(instance=SpreadsheetMLStyles::Header_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::header_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Header)

@given(instance=SpreadsheetMLStyles::HeaderOrFooterElt_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::headerorfooterelt_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::HeaderOrFooterElt)

@given(instance=SpreadsheetMLStyles::HeaderOrFooterElt_strategy)
def test_spreadsheetmlstyles::headerorfooterelt_margin_type(instance):
    assert isinstance(instance.margin, str)


@given(instance=SpreadsheetMLStyles::HeaderOrFooterElt_strategy)
def test_spreadsheetmlstyles::headerorfooterelt_margin_setter(instance):
    original = instance.margin
    instance.margin = original
    assert instance.margin == original

@given(instance=SpreadsheetMLStyles::HeaderOrFooterElt_strategy)
def test_spreadsheetmlstyles::headerorfooterelt_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=SpreadsheetMLStyles::HeaderOrFooterElt_strategy)
def test_spreadsheetmlstyles::headerorfooterelt_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=SpreadsheetMLStyles::PageSetup_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::pagesetup_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::PageSetup)

@given(instance=SpreadsheetMLStyles::Layout_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::layout_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Layout)

@given(instance=SpreadsheetMLStyles::Layout_strategy)
def test_spreadsheetmlstyles::layout_startPageNumber_type(instance):
    assert isinstance(instance.startPageNumber, str)


@given(instance=SpreadsheetMLStyles::Layout_strategy)
def test_spreadsheetmlstyles::layout_startPageNumber_setter(instance):
    original = instance.startPageNumber
    instance.startPageNumber = original
    assert instance.startPageNumber == original

@given(instance=SpreadsheetMLStyles::Layout_strategy)
def test_spreadsheetmlstyles::layout_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=SpreadsheetMLStyles::Layout_strategy)
def test_spreadsheetmlstyles::layout_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=SpreadsheetMLStyles::Layout_strategy)
def test_spreadsheetmlstyles::layout_centerVertical_type(instance):
    assert isinstance(instance.centerVertical, str)


@given(instance=SpreadsheetMLStyles::Layout_strategy)
def test_spreadsheetmlstyles::layout_centerVertical_setter(instance):
    original = instance.centerVertical
    instance.centerVertical = original
    assert instance.centerVertical == original

@given(instance=SpreadsheetMLStyles::Layout_strategy)
def test_spreadsheetmlstyles::layout_centerHorizontal_type(instance):
    assert isinstance(instance.centerHorizontal, str)


@given(instance=SpreadsheetMLStyles::Layout_strategy)
def test_spreadsheetmlstyles::layout_centerHorizontal_setter(instance):
    original = instance.centerHorizontal
    instance.centerHorizontal = original
    assert instance.centerHorizontal == original

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

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::worksheetoptionselt_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::WorksheetOptionsElt)

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_protectObjects_type(instance):
    assert isinstance(instance.protectObjects, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_protectObjects_setter(instance):
    original = instance.protectObjects
    instance.protectObjects = original
    assert instance.protectObjects == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_splitVertical_type(instance):
    assert isinstance(instance.splitVertical, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_splitVertical_setter(instance):
    original = instance.splitVertical
    instance.splitVertical = original
    assert instance.splitVertical == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayZeros_type(instance):
    assert isinstance(instance.doNotDisplayZeros, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayZeros_setter(instance):
    original = instance.doNotDisplayZeros
    instance.doNotDisplayZeros = original
    assert instance.doNotDisplayZeros == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_freezePanes_type(instance):
    assert isinstance(instance.freezePanes, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_freezePanes_setter(instance):
    original = instance.freezePanes
    instance.freezePanes = original
    assert instance.freezePanes == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_activePane_type(instance):
    assert isinstance(instance.activePane, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_activePane_setter(instance):
    original = instance.activePane
    instance.activePane = original
    assert instance.activePane == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_standardWidth_type(instance):
    assert isinstance(instance.standardWidth, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_standardWidth_setter(instance):
    original = instance.standardWidth
    instance.standardWidth = original
    assert instance.standardWidth == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowInsertRows_type(instance):
    assert isinstance(instance.allowInsertRows, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowInsertRows_setter(instance):
    original = instance.allowInsertRows
    instance.allowInsertRows = original
    assert instance.allowInsertRows == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowInsertHyperlinks_type(instance):
    assert isinstance(instance.allowInsertHyperlinks, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowInsertHyperlinks_setter(instance):
    original = instance.allowInsertHyperlinks
    instance.allowInsertHyperlinks = original
    assert instance.allowInsertHyperlinks == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_zoom_type(instance):
    assert isinstance(instance.zoom, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_activeRow_type(instance):
    assert isinstance(instance.activeRow, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_activeRow_setter(instance):
    original = instance.activeRow
    instance.activeRow = original
    assert instance.activeRow == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_tabColorIndex_type(instance):
    assert isinstance(instance.tabColorIndex, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_tabColorIndex_setter(instance):
    original = instance.tabColorIndex
    instance.tabColorIndex = original
    assert instance.tabColorIndex == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_unsynced_type(instance):
    assert isinstance(instance.unsynced, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_unsynced_setter(instance):
    original = instance.unsynced
    instance.unsynced = original
    assert instance.unsynced == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_noSummaryColumnsRightDetail_type(instance):
    assert isinstance(instance.noSummaryColumnsRightDetail, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_noSummaryColumnsRightDetail_setter(instance):
    original = instance.noSummaryColumnsRightDetail
    instance.noSummaryColumnsRightDetail = original
    assert instance.noSummaryColumnsRightDetail == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_pageBreakZoom_type(instance):
    assert isinstance(instance.pageBreakZoom, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_pageBreakZoom_setter(instance):
    original = instance.pageBreakZoom
    instance.pageBreakZoom = original
    assert instance.pageBreakZoom == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowSort_type(instance):
    assert isinstance(instance.allowSort, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowSort_setter(instance):
    original = instance.allowSort
    instance.allowSort = original
    assert instance.allowSort == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_frozenNoSplit_type(instance):
    assert isinstance(instance.frozenNoSplit, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_frozenNoSplit_setter(instance):
    original = instance.frozenNoSplit
    instance.frozenNoSplit = original
    assert instance.frozenNoSplit == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_displayPageBreak_type(instance):
    assert isinstance(instance.displayPageBreak, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_displayPageBreak_setter(instance):
    original = instance.displayPageBreak
    instance.displayPageBreak = original
    assert instance.displayPageBreak == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_applyAutomaticOutlineStyles_type(instance):
    assert isinstance(instance.applyAutomaticOutlineStyles, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_applyAutomaticOutlineStyles_setter(instance):
    original = instance.applyAutomaticOutlineStyles
    instance.applyAutomaticOutlineStyles = original
    assert instance.applyAutomaticOutlineStyles == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_filterOn_type(instance):
    assert isinstance(instance.filterOn, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_filterOn_setter(instance):
    original = instance.filterOn
    instance.filterOn = original
    assert instance.filterOn == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_activeColumn_type(instance):
    assert isinstance(instance.activeColumn, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_activeColumn_setter(instance):
    original = instance.activeColumn
    instance.activeColumn = original
    assert instance.activeColumn == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_protectScenarios_type(instance):
    assert isinstance(instance.protectScenarios, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_protectScenarios_setter(instance):
    original = instance.protectScenarios
    instance.protectScenarios = original
    assert instance.protectScenarios == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_noSummaryRowsBelowDetail_type(instance):
    assert isinstance(instance.noSummaryRowsBelowDetail, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_noSummaryRowsBelowDetail_setter(instance):
    original = instance.noSummaryRowsBelowDetail
    instance.noSummaryRowsBelowDetail = original
    assert instance.noSummaryRowsBelowDetail == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_splitHorizontal_type(instance):
    assert isinstance(instance.splitHorizontal, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_splitHorizontal_setter(instance):
    original = instance.splitHorizontal
    instance.splitHorizontal = original
    assert instance.splitHorizontal == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayHeadings_type(instance):
    assert isinstance(instance.doNotDisplayHeadings, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayHeadings_setter(instance):
    original = instance.doNotDisplayHeadings
    instance.doNotDisplayHeadings = original
    assert instance.doNotDisplayHeadings == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_protectContentst_type(instance):
    assert isinstance(instance.protectContentst, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_protectContentst_setter(instance):
    original = instance.protectContentst
    instance.protectContentst = original
    assert instance.protectContentst == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayOutline_type(instance):
    assert isinstance(instance.doNotDisplayOutline, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayOutline_setter(instance):
    original = instance.doNotDisplayOutline
    instance.doNotDisplayOutline = original
    assert instance.doNotDisplayOutline == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_showPageBreakZoom_type(instance):
    assert isinstance(instance.showPageBreakZoom, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_showPageBreakZoom_setter(instance):
    original = instance.showPageBreakZoom
    instance.showPageBreakZoom = original
    assert instance.showPageBreakZoom == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_displayRightToLeft_type(instance):
    assert isinstance(instance.displayRightToLeft, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_displayRightToLeft_setter(instance):
    original = instance.displayRightToLeft
    instance.displayRightToLeft = original
    assert instance.displayRightToLeft == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_displayFormulas_type(instance):
    assert isinstance(instance.displayFormulas, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_displayFormulas_setter(instance):
    original = instance.displayFormulas
    instance.displayFormulas = original
    assert instance.displayFormulas == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_defaultRowHeight_type(instance):
    assert isinstance(instance.defaultRowHeight, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowInsertCols_type(instance):
    assert isinstance(instance.allowInsertCols, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowInsertCols_setter(instance):
    original = instance.allowInsertCols
    instance.allowInsertCols = original
    assert instance.allowInsertCols == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_topRowVisible_type(instance):
    assert isinstance(instance.topRowVisible, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_topRowVisible_setter(instance):
    original = instance.topRowVisible
    instance.topRowVisible = original
    assert instance.topRowVisible == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_codeName_type(instance):
    assert isinstance(instance.codeName, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_codeName_setter(instance):
    original = instance.codeName
    instance.codeName = original
    assert instance.codeName == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_transitionFormulaEntry_type(instance):
    assert isinstance(instance.transitionFormulaEntry, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_transitionFormulaEntry_setter(instance):
    original = instance.transitionFormulaEntry
    instance.transitionFormulaEntry = original
    assert instance.transitionFormulaEntry == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_gridlineColorIndex_type(instance):
    assert isinstance(instance.gridlineColorIndex, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_gridlineColorIndex_setter(instance):
    original = instance.gridlineColorIndex
    instance.gridlineColorIndex = original
    assert instance.gridlineColorIndex == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_fitToPage_type(instance):
    assert isinstance(instance.fitToPage, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_fitToPage_setter(instance):
    original = instance.fitToPage
    instance.fitToPage = original
    assert instance.fitToPage == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowSizeRows_type(instance):
    assert isinstance(instance.allowSizeRows, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowSizeRows_setter(instance):
    original = instance.allowSizeRows
    instance.allowSizeRows = original
    assert instance.allowSizeRows == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_topRowBottomPane_type(instance):
    assert isinstance(instance.topRowBottomPane, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_topRowBottomPane_setter(instance):
    original = instance.topRowBottomPane
    instance.topRowBottomPane = original
    assert instance.topRowBottomPane == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowUsePivotTables_type(instance):
    assert isinstance(instance.allowUsePivotTables, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowUsePivotTables_setter(instance):
    original = instance.allowUsePivotTables
    instance.allowUsePivotTables = original
    assert instance.allowUsePivotTables == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_gridlineColor_type(instance):
    assert isinstance(instance.gridlineColor, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_gridlineColor_setter(instance):
    original = instance.gridlineColor
    instance.gridlineColor = original
    assert instance.gridlineColor == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_enableSelection_type(instance):
    assert isinstance(instance.enableSelection, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_enableSelection_setter(instance):
    original = instance.enableSelection
    instance.enableSelection = original
    assert instance.enableSelection == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_selected_type(instance):
    assert isinstance(instance.selected, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowDeleteRows_type(instance):
    assert isinstance(instance.allowDeleteRows, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowDeleteRows_setter(instance):
    original = instance.allowDeleteRows
    instance.allowDeleteRows = original
    assert instance.allowDeleteRows == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayColHeaders_type(instance):
    assert isinstance(instance.doNotDisplayColHeaders, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayColHeaders_setter(instance):
    original = instance.doNotDisplayColHeaders
    instance.doNotDisplayColHeaders = original
    assert instance.doNotDisplayColHeaders == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_excelWorksheetType_type(instance):
    assert isinstance(instance.excelWorksheetType, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_excelWorksheetType_setter(instance):
    original = instance.excelWorksheetType
    instance.excelWorksheetType = original
    assert instance.excelWorksheetType == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_intlMacro_type(instance):
    assert isinstance(instance.intlMacro, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_intlMacro_setter(instance):
    original = instance.intlMacro
    instance.intlMacro = original
    assert instance.intlMacro == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayGridlines_type(instance):
    assert isinstance(instance.doNotDisplayGridlines, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayGridlines_setter(instance):
    original = instance.doNotDisplayGridlines
    instance.doNotDisplayGridlines = original
    assert instance.doNotDisplayGridlines == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayRowHeaders_type(instance):
    assert isinstance(instance.doNotDisplayRowHeaders, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_doNotDisplayRowHeaders_setter(instance):
    original = instance.doNotDisplayRowHeaders
    instance.doNotDisplayRowHeaders = original
    assert instance.doNotDisplayRowHeaders == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowSizeCols_type(instance):
    assert isinstance(instance.allowSizeCols, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowSizeCols_setter(instance):
    original = instance.allowSizeCols
    instance.allowSizeCols = original
    assert instance.allowSizeCols == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_leftColumnRightPane_type(instance):
    assert isinstance(instance.leftColumnRightPane, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_leftColumnRightPane_setter(instance):
    original = instance.leftColumnRightPane
    instance.leftColumnRightPane = original
    assert instance.leftColumnRightPane == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_transitionExpressionEvaluation_type(instance):
    assert isinstance(instance.transitionExpressionEvaluation, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_transitionExpressionEvaluation_setter(instance):
    original = instance.transitionExpressionEvaluation
    instance.transitionExpressionEvaluation = original
    assert instance.transitionExpressionEvaluation == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowFormatCells_type(instance):
    assert isinstance(instance.allowFormatCells, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowFormatCells_setter(instance):
    original = instance.allowFormatCells
    instance.allowFormatCells = original
    assert instance.allowFormatCells == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowFilter_type(instance):
    assert isinstance(instance.allowFilter, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowFilter_setter(instance):
    original = instance.allowFilter
    instance.allowFilter = original
    assert instance.allowFilter == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_rangeSelection_type(instance):
    assert isinstance(instance.rangeSelection, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_rangeSelection_setter(instance):
    original = instance.rangeSelection
    instance.rangeSelection = original
    assert instance.rangeSelection == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_leftColumnVisible_type(instance):
    assert isinstance(instance.leftColumnVisible, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_leftColumnVisible_setter(instance):
    original = instance.leftColumnVisible
    instance.leftColumnVisible = original
    assert instance.leftColumnVisible == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_defaultColumnWidth_type(instance):
    assert isinstance(instance.defaultColumnWidth, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowDeleteCols_type(instance):
    assert isinstance(instance.allowDeleteCols, str)


@given(instance=SpreadsheetMLStyles::WorksheetOptionsElt_strategy)
def test_spreadsheetmlstyles::worksheetoptionselt_allowDeleteCols_setter(instance):
    original = instance.allowDeleteCols
    instance.allowDeleteCols = original
    assert instance.allowDeleteCols == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::excelworkbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::ExcelWorkbook)

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_createBackup_type(instance):
    assert isinstance(instance.createBackup, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_createBackup_setter(instance):
    original = instance.createBackup
    instance.createBackup = original
    assert instance.createBackup == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_protectWindows_type(instance):
    assert isinstance(instance.protectWindows, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_protectWindows_setter(instance):
    original = instance.protectWindows
    instance.protectWindows = original
    assert instance.protectWindows == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_date1904_type(instance):
    assert isinstance(instance.date1904, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_date1904_setter(instance):
    original = instance.date1904
    instance.date1904 = original
    assert instance.date1904 == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_displayDrawingObjects_type(instance):
    assert isinstance(instance.displayDrawingObjects, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_displayDrawingObjects_setter(instance):
    original = instance.displayDrawingObjects
    instance.displayDrawingObjects = original
    assert instance.displayDrawingObjects == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_hideHorizontalScrollBar_type(instance):
    assert isinstance(instance.hideHorizontalScrollBar, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_hideHorizontalScrollBar_setter(instance):
    original = instance.hideHorizontalScrollBar
    instance.hideHorizontalScrollBar = original
    assert instance.hideHorizontalScrollBar == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_doNotSaveLinkValues_type(instance):
    assert isinstance(instance.doNotSaveLinkValues, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_doNotSaveLinkValues_setter(instance):
    original = instance.doNotSaveLinkValues
    instance.doNotSaveLinkValues = original
    assert instance.doNotSaveLinkValues == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_calculation_type(instance):
    assert isinstance(instance.calculation, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_calculation_setter(instance):
    original = instance.calculation
    instance.calculation = original
    assert instance.calculation == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_activeSheet_type(instance):
    assert isinstance(instance.activeSheet, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_activeSheet_setter(instance):
    original = instance.activeSheet
    instance.activeSheet = original
    assert instance.activeSheet == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowHidden_type(instance):
    assert isinstance(instance.windowHidden, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowHidden_setter(instance):
    original = instance.windowHidden
    instance.windowHidden = original
    assert instance.windowHidden == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_displayInkNotes_type(instance):
    assert isinstance(instance.displayInkNotes, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_displayInkNotes_setter(instance):
    original = instance.displayInkNotes
    instance.displayInkNotes = original
    assert instance.displayInkNotes == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowWidth_type(instance):
    assert isinstance(instance.windowWidth, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowWidth_setter(instance):
    original = instance.windowWidth
    instance.windowWidth = original
    assert instance.windowWidth == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_tabRatio_type(instance):
    assert isinstance(instance.tabRatio, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_tabRatio_setter(instance):
    original = instance.tabRatio
    instance.tabRatio = original
    assert instance.tabRatio == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowHeight_type(instance):
    assert isinstance(instance.windowHeight, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowHeight_setter(instance):
    original = instance.windowHeight
    instance.windowHeight = original
    assert instance.windowHeight == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_selectedSheets_type(instance):
    assert isinstance(instance.selectedSheets, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_selectedSheets_setter(instance):
    original = instance.selectedSheets
    instance.selectedSheets = original
    assert instance.selectedSheets == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_hideVerticalScrollBar_type(instance):
    assert isinstance(instance.hideVerticalScrollBar, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_hideVerticalScrollBar_setter(instance):
    original = instance.hideVerticalScrollBar
    instance.hideVerticalScrollBar = original
    assert instance.hideVerticalScrollBar == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_doNotCalculateBeforeSave_type(instance):
    assert isinstance(instance.doNotCalculateBeforeSave, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_doNotCalculateBeforeSave_setter(instance):
    original = instance.doNotCalculateBeforeSave
    instance.doNotCalculateBeforeSave = original
    assert instance.doNotCalculateBeforeSave == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_protectStructure_type(instance):
    assert isinstance(instance.protectStructure, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_protectStructure_setter(instance):
    original = instance.protectStructure
    instance.protectStructure = original
    assert instance.protectStructure == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_maxChange_type(instance):
    assert isinstance(instance.maxChange, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_maxChange_setter(instance):
    original = instance.maxChange
    instance.maxChange = original
    assert instance.maxChange == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_firstVisibleSheet_type(instance):
    assert isinstance(instance.firstVisibleSheet, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_firstVisibleSheet_setter(instance):
    original = instance.firstVisibleSheet
    instance.firstVisibleSheet = original
    assert instance.firstVisibleSheet == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_activeChart_type(instance):
    assert isinstance(instance.activeChart, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_activeChart_setter(instance):
    original = instance.activeChart
    instance.activeChart = original
    assert instance.activeChart == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_hideWorkbookTabs_type(instance):
    assert isinstance(instance.hideWorkbookTabs, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_hideWorkbookTabs_setter(instance):
    original = instance.hideWorkbookTabs
    instance.hideWorkbookTabs = original
    assert instance.hideWorkbookTabs == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_embedSaveSmartTags_type(instance):
    assert isinstance(instance.embedSaveSmartTags, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_embedSaveSmartTags_setter(instance):
    original = instance.embedSaveSmartTags
    instance.embedSaveSmartTags = original
    assert instance.embedSaveSmartTags == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowIconic_type(instance):
    assert isinstance(instance.windowIconic, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowIconic_setter(instance):
    original = instance.windowIconic
    instance.windowIconic = original
    assert instance.windowIconic == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_acceptLabelsInFormulas_type(instance):
    assert isinstance(instance.acceptLabelsInFormulas, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_acceptLabelsInFormulas_setter(instance):
    original = instance.acceptLabelsInFormulas
    instance.acceptLabelsInFormulas = original
    assert instance.acceptLabelsInFormulas == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowTopX_type(instance):
    assert isinstance(instance.windowTopX, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowTopX_setter(instance):
    original = instance.windowTopX
    instance.windowTopX = original
    assert instance.windowTopX == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_refModeR1C1_type(instance):
    assert isinstance(instance.refModeR1C1, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_refModeR1C1_setter(instance):
    original = instance.refModeR1C1
    instance.refModeR1C1 = original
    assert instance.refModeR1C1 == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_hidePivotTableFieldList_type(instance):
    assert isinstance(instance.hidePivotTableFieldList, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_hidePivotTableFieldList_setter(instance):
    original = instance.hidePivotTableFieldList
    instance.hidePivotTableFieldList = original
    assert instance.hidePivotTableFieldList == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_futureVer_type(instance):
    assert isinstance(instance.futureVer, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_futureVer_setter(instance):
    original = instance.futureVer
    instance.futureVer = original
    assert instance.futureVer == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_noAutoRecover_type(instance):
    assert isinstance(instance.noAutoRecover, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_noAutoRecover_setter(instance):
    original = instance.noAutoRecover
    instance.noAutoRecover = original
    assert instance.noAutoRecover == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_precisionAsDisplayed_type(instance):
    assert isinstance(instance.precisionAsDisplayed, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_precisionAsDisplayed_setter(instance):
    original = instance.precisionAsDisplayed
    instance.precisionAsDisplayed = original
    assert instance.precisionAsDisplayed == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_iteration_type(instance):
    assert isinstance(instance.iteration, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_iteration_setter(instance):
    original = instance.iteration
    instance.iteration = original
    assert instance.iteration == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_uncalced_type(instance):
    assert isinstance(instance.uncalced, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_uncalced_setter(instance):
    original = instance.uncalced
    instance.uncalced = original
    assert instance.uncalced == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowTopY_type(instance):
    assert isinstance(instance.windowTopY, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_windowTopY_setter(instance):
    original = instance.windowTopY
    instance.windowTopY = original
    assert instance.windowTopY == original

@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_maxIterations_type(instance):
    assert isinstance(instance.maxIterations, str)


@given(instance=SpreadsheetMLStyles::ExcelWorkbook_strategy)
def test_spreadsheetmlstyles::excelworkbook_maxIterations_setter(instance):
    original = instance.maxIterations
    instance.maxIterations = original
    assert instance.maxIterations == original

@given(instance=SpreadsheetMLStyles::Data_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::data_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Data)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=SpreadsheetMLStyles::Comment_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::comment_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Comment)

@given(instance=SpreadsheetMLStyles::Comment_strategy)
def test_spreadsheetmlstyles::comment_showAlways_type(instance):
    assert isinstance(instance.showAlways, str)


@given(instance=SpreadsheetMLStyles::Comment_strategy)
def test_spreadsheetmlstyles::comment_showAlways_setter(instance):
    original = instance.showAlways
    instance.showAlways = original
    assert instance.showAlways == original

@given(instance=SpreadsheetMLStyles::Comment_strategy)
def test_spreadsheetmlstyles::comment_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=SpreadsheetMLStyles::Comment_strategy)
def test_spreadsheetmlstyles::comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=ColOrRowElement_strategy)
@settings(max_examples=50)
def test_colorrowelement_instantiation(instance):
    assert isinstance(instance, ColOrRowElement)

@given(instance=SpreadsheetMLStyles::Column_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::column_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Column)

@given(instance=SpreadsheetMLStyles::Column_strategy)
def test_spreadsheetmlstyles::column_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=SpreadsheetMLStyles::Column_strategy)
def test_spreadsheetmlstyles::column_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=SpreadsheetMLStyles::Column_strategy)
def test_spreadsheetmlstyles::column_autoFitWidth_type(instance):
    assert isinstance(instance.autoFitWidth, str)


@given(instance=SpreadsheetMLStyles::Column_strategy)
def test_spreadsheetmlstyles::column_autoFitWidth_setter(instance):
    original = instance.autoFitWidth
    instance.autoFitWidth = original
    assert instance.autoFitWidth == original

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SpreadsheetMLStyles::Cell_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::cell_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Cell)

@given(instance=SpreadsheetMLStyles::Cell_strategy)
def test_spreadsheetmlstyles::cell_arrayRange_type(instance):
    assert isinstance(instance.arrayRange, str)


@given(instance=SpreadsheetMLStyles::Cell_strategy)
def test_spreadsheetmlstyles::cell_arrayRange_setter(instance):
    original = instance.arrayRange
    instance.arrayRange = original
    assert instance.arrayRange == original

@given(instance=SpreadsheetMLStyles::Cell_strategy)
def test_spreadsheetmlstyles::cell_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=SpreadsheetMLStyles::Cell_strategy)
def test_spreadsheetmlstyles::cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=SpreadsheetMLStyles::Cell_strategy)
def test_spreadsheetmlstyles::cell_mergeDown_type(instance):
    assert isinstance(instance.mergeDown, str)


@given(instance=SpreadsheetMLStyles::Cell_strategy)
def test_spreadsheetmlstyles::cell_mergeDown_setter(instance):
    original = instance.mergeDown
    instance.mergeDown = original
    assert instance.mergeDown == original

@given(instance=SpreadsheetMLStyles::Cell_strategy)
def test_spreadsheetmlstyles::cell_hRef_type(instance):
    assert isinstance(instance.hRef, str)


@given(instance=SpreadsheetMLStyles::Cell_strategy)
def test_spreadsheetmlstyles::cell_hRef_setter(instance):
    original = instance.hRef
    instance.hRef = original
    assert instance.hRef == original

@given(instance=SpreadsheetMLStyles::Cell_strategy)
def test_spreadsheetmlstyles::cell_mergeAcross_type(instance):
    assert isinstance(instance.mergeAcross, str)


@given(instance=SpreadsheetMLStyles::Cell_strategy)
def test_spreadsheetmlstyles::cell_mergeAcross_setter(instance):
    original = instance.mergeAcross
    instance.mergeAcross = original
    assert instance.mergeAcross == original

@given(instance=SpreadsheetMLStyles::ColOrRowElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::colorrowelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::ColOrRowElement)

@given(instance=SpreadsheetMLStyles::ColOrRowElement_strategy)
def test_spreadsheetmlstyles::colorrowelement_hidden_type(instance):
    assert isinstance(instance.hidden, str)


@given(instance=SpreadsheetMLStyles::ColOrRowElement_strategy)
def test_spreadsheetmlstyles::colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=SpreadsheetMLStyles::ColOrRowElement_strategy)
def test_spreadsheetmlstyles::colorrowelement_span_type(instance):
    assert isinstance(instance.span, str)


@given(instance=SpreadsheetMLStyles::ColOrRowElement_strategy)
def test_spreadsheetmlstyles::colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original

@given(instance=SpreadsheetMLStyles::Row_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::row_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Row)

@given(instance=SpreadsheetMLStyles::Row_strategy)
def test_spreadsheetmlstyles::row_autoFitHeight_type(instance):
    assert isinstance(instance.autoFitHeight, str)


@given(instance=SpreadsheetMLStyles::Row_strategy)
def test_spreadsheetmlstyles::row_autoFitHeight_setter(instance):
    original = instance.autoFitHeight
    instance.autoFitHeight = original
    assert instance.autoFitHeight == original

@given(instance=SpreadsheetMLStyles::Row_strategy)
def test_spreadsheetmlstyles::row_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=SpreadsheetMLStyles::Row_strategy)
def test_spreadsheetmlstyles::row_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

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

@given(instance=SpreadsheetMLStyles::TableElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::tableelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::TableElement)

@given(instance=SpreadsheetMLStyles::TableElement_strategy)
def test_spreadsheetmlstyles::tableelement_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=SpreadsheetMLStyles::TableElement_strategy)
def test_spreadsheetmlstyles::tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=StyleType_strategy)
@settings(max_examples=50)
def test_styletype_instantiation(instance):
    assert isinstance(instance, StyleType)

@given(instance=SpreadsheetMLStyles::StyledElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::styledelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::StyledElement)

@given(instance=WorksheetOptionsElt_strategy)
@settings(max_examples=50)
def test_worksheetoptionselt_instantiation(instance):
    assert isinstance(instance, WorksheetOptionsElt)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SpreadsheetMLStyles::Worksheet_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::worksheet_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Worksheet)

@given(instance=SpreadsheetMLStyles::Worksheet_strategy)
def test_spreadsheetmlstyles::worksheet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLStyles::Worksheet_strategy)
def test_spreadsheetmlstyles::worksheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLStyles::Worksheet_strategy)
def test_spreadsheetmlstyles::worksheet_rightToLeft_type(instance):
    assert isinstance(instance.rightToLeft, str)


@given(instance=SpreadsheetMLStyles::Worksheet_strategy)
def test_spreadsheetmlstyles::worksheet_rightToLeft_setter(instance):
    original = instance.rightToLeft
    instance.rightToLeft = original
    assert instance.rightToLeft == original

@given(instance=SpreadsheetMLStyles::Worksheet_strategy)
def test_spreadsheetmlstyles::worksheet_protected_type(instance):
    assert isinstance(instance.protected, str)


@given(instance=SpreadsheetMLStyles::Worksheet_strategy)
def test_spreadsheetmlstyles::worksheet_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=SpreadsheetMLStyles::Table_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::table_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Table)

@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_defaultColumnWidth_type(instance):
    assert isinstance(instance.defaultColumnWidth, str)


@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original

@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_leftCell_type(instance):
    assert isinstance(instance.leftCell, str)


@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_leftCell_setter(instance):
    original = instance.leftCell
    instance.leftCell = original
    assert instance.leftCell == original

@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_defaultRowHeight_type(instance):
    assert isinstance(instance.defaultRowHeight, str)


@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original

@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_topCell_type(instance):
    assert isinstance(instance.topCell, str)


@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_topCell_setter(instance):
    original = instance.topCell
    instance.topCell = original
    assert instance.topCell == original

@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_expandedRowCount_type(instance):
    assert isinstance(instance.expandedRowCount, str)


@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_expandedRowCount_setter(instance):
    original = instance.expandedRowCount
    instance.expandedRowCount = original
    assert instance.expandedRowCount == original

@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_fullRows_type(instance):
    assert isinstance(instance.fullRows, str)


@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_fullRows_setter(instance):
    original = instance.fullRows
    instance.fullRows = original
    assert instance.fullRows == original

@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_fullColumns_type(instance):
    assert isinstance(instance.fullColumns, str)


@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_fullColumns_setter(instance):
    original = instance.fullColumns
    instance.fullColumns = original
    assert instance.fullColumns == original

@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_expandedColumnCount_type(instance):
    assert isinstance(instance.expandedColumnCount, str)


@given(instance=SpreadsheetMLStyles::Table_strategy)
def test_spreadsheetmlstyles::table_expandedColumnCount_setter(instance):
    original = instance.expandedColumnCount
    instance.expandedColumnCount = original
    assert instance.expandedColumnCount == original

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

@given(instance=SpreadsheetMLStyles::SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::smarttagscollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::SmartTagsCollection)

@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)

@given(instance=SpreadsheetMLStyles::SmartTagType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::smarttagtype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::SmartTagType)

@given(instance=SpreadsheetMLStyles::SmartTagType_strategy)
def test_spreadsheetmlstyles::smarttagtype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=SpreadsheetMLStyles::SmartTagType_strategy)
def test_spreadsheetmlstyles::smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=SpreadsheetMLStyles::SmartTagType_strategy)
def test_spreadsheetmlstyles::smarttagtype_namespaceuri_type(instance):
    assert isinstance(instance.namespaceuri, str)


@given(instance=SpreadsheetMLStyles::SmartTagType_strategy)
def test_spreadsheetmlstyles::smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original

@given(instance=SpreadsheetMLStyles::SmartTagType_strategy)
def test_spreadsheetmlstyles::smarttagtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLStyles::SmartTagType_strategy)
def test_spreadsheetmlstyles::smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLStyles::Workbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::workbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::Workbook)

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=SpreadsheetMLStyles::CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::customdocumentproperty_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::CustomDocumentProperty)

@given(instance=SpreadsheetMLStyles::CustomDocumentProperty_strategy)
def test_spreadsheetmlstyles::customdocumentproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLStyles::CustomDocumentProperty_strategy)
def test_spreadsheetmlstyles::customdocumentproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, CustomDocumentProperty)

@given(instance=SpreadsheetMLStyles::CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::CustomDocumentPropertiesCollection)

@given(instance=VersionType_strategy)
@settings(max_examples=50)
def test_versiontype_instantiation(instance):
    assert isinstance(instance, VersionType)

@given(instance=Workbook_strategy)
@settings(max_examples=50)
def test_workbook_instantiation(instance):
    assert isinstance(instance, Workbook)

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::DocumentPropertiesCollection)

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_lastAuthor_type(instance):
    assert isinstance(instance.lastAuthor, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_presentationFormat_type(instance):
    assert isinstance(instance.presentationFormat, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_charactersWithSpaces_type(instance):
    assert isinstance(instance.charactersWithSpaces, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_bytes_type(instance):
    assert isinstance(instance.bytes, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_lines_type(instance):
    assert isinstance(instance.lines, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_characters_type(instance):
    assert isinstance(instance.characters, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_words_type(instance):
    assert isinstance(instance.words, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_revision_type(instance):
    assert isinstance(instance.revision, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_manager_type(instance):
    assert isinstance(instance.manager, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_hyperlinkBase_type(instance):
    assert isinstance(instance.hyperlinkBase, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_totalTime_type(instance):
    assert isinstance(instance.totalTime, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_appName_type(instance):
    assert isinstance(instance.appName, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_guid_type(instance):
    assert isinstance(instance.guid, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_paragraphs_type(instance):
    assert isinstance(instance.paragraphs, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_company_type(instance):
    assert isinstance(instance.company, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original

@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=SpreadsheetMLStyles::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlstyles::documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=SpreadsheetMLStyles::BooleanValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::booleanvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::BooleanValue)

@given(instance=SpreadsheetMLStyles::BooleanValue_strategy)
def test_spreadsheetmlstyles::booleanvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLStyles::BooleanValue_strategy)
def test_spreadsheetmlstyles::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLStyles::DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::datetimetypevalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::DateTimeTypeValue)

@given(instance=SpreadsheetMLStyles::NumberValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::numbervalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::NumberValue)

@given(instance=SpreadsheetMLStyles::NumberValue_strategy)
def test_spreadsheetmlstyles::numbervalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLStyles::NumberValue_strategy)
def test_spreadsheetmlstyles::numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLStyles::ErrorValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::errorvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::ErrorValue)

@given(instance=SpreadsheetMLStyles::StringValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::stringvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::StringValue)

@given(instance=SpreadsheetMLStyles::StringValue_strategy)
def test_spreadsheetmlstyles::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLStyles::StringValue_strategy)
def test_spreadsheetmlstyles::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=SpreadsheetMLStyles::ValueType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::valuetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::ValueType)

@given(instance=SpreadsheetMLStyles::VersionType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::versiontype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::VersionType)

@given(instance=SpreadsheetMLStyles::VersionType_strategy)
def test_spreadsheetmlstyles::versiontype_nn_type(instance):
    assert isinstance(instance.nn, str)


@given(instance=SpreadsheetMLStyles::VersionType_strategy)
def test_spreadsheetmlstyles::versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original

@given(instance=SpreadsheetMLStyles::VersionType_strategy)
def test_spreadsheetmlstyles::versiontype_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=SpreadsheetMLStyles::VersionType_strategy)
def test_spreadsheetmlstyles::versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlstyles::datetimetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLStyles::DateTimeType)

@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_hour_type(instance):
    assert isinstance(instance.hour, str)


@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_second_type(instance):
    assert isinstance(instance.second, str)


@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_minute_type(instance):
    assert isinstance(instance.minute, str)


@given(instance=SpreadsheetMLStyles::DateTimeType_strategy)
def test_spreadsheetmlstyles::datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original
