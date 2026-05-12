import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SpreadsheetMLPrintingSetup::PageMarginsInfo,
    SpreadsheetMLPrintingSetup::Print,
    HeaderOrFooterElt,
    SpreadsheetMLPrintingSetup::Header,
    SpreadsheetMLPrintingSetup::HeaderOrFooterElt,
    SpreadsheetMLPrintingSetup::Footer,
    SpreadsheetMLPrintingSetup::Layout,
    PageMarginsInfo,
    SpreadsheetMLPrintingSetup::PageSetup,
    Footer,
    Header,
    Layout,
    PageSetup,
    Print,
    SpreadsheetMLPrintingSetup::WorksheetOptionsElt,
    SpreadsheetMLPrintingSetup::Data,
    SpreadsheetMLPrintingSetup::ExcelWorkbook,
    SpreadsheetMLPrintingSetup::Comment,
    Comment,
    ColOrRowElement,
    SpreadsheetMLPrintingSetup::Row,
    SpreadsheetMLPrintingSetup::Column,
    TableElement,
    SpreadsheetMLPrintingSetup::Cell,
    SpreadsheetMLPrintingSetup::ColOrRowElement,
    ExcelWorkbook,
    Row,
    Column,
    StyledElement,
    SpreadsheetMLPrintingSetup::TableElement,
    SpreadsheetMLPrintingSetup::Table,
    SpreadsheetMLPrintingSetup::StyledElement,
    WorksheetOptionsElt,
    Table,
    SpreadsheetMLPrintingSetup::Worksheet,
    Worksheet,
    CustomDocumentProperty,
    DocumentPropertiesCollection,
    SpreadsheetMLPrintingSetup::Workbook,
    SmartTagType,
    Cell,
    SpreadsheetMLPrintingSetup::SmartTagsCollection,
    SmartTagsCollection,
    SpreadsheetMLPrintingSetup::SmartTagType,
    CustomDocumentPropertiesCollection,
    SpreadsheetMLPrintingSetup::CustomDocumentProperty,
    SpreadsheetMLPrintingSetup::CustomDocumentPropertiesCollection,
    VersionType,
    ValueType,
    SpreadsheetMLPrintingSetup::NumberValue,
    SpreadsheetMLPrintingSetup::StringValue,
    Data,
    Workbook,
    SpreadsheetMLPrintingSetup::DocumentPropertiesCollection,
    SpreadsheetMLPrintingSetup::ErrorValue,
    SpreadsheetMLPrintingSetup::BooleanValue,
    DateTimeType,
    SpreadsheetMLPrintingSetup::DateTimeTypeValue,
    SpreadsheetMLPrintingSetup::DateTimeType,
    SpreadsheetMLPrintingSetup::ValueType,
    SpreadsheetMLPrintingSetup::VersionType,
    CalculationWorkbookType,
    CommentsLayoutType,
    VisibleType,
    ExcelWorksheetTypeType,
    EnableSelectionType,
    OrientationType,
    DisplayDrawingObjectsType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheetmlprintingsetup::pagemarginsinfo_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::PageMarginsInfo)


def test_spreadsheetmlprintingsetup::pagemarginsinfo_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::PageMarginsInfo.__init__)


def test_spreadsheetmlprintingsetup::pagemarginsinfo_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::PageMarginsInfo.__init__)
    params = list(sig.parameters.keys())
    assert "left" in params, "Missing parameter 'left'"
    assert "bottom" in params, "Missing parameter 'bottom'"
    assert "right" in params, "Missing parameter 'right'"
    assert "top" in params, "Missing parameter 'top'"

def test_spreadsheetmlprintingsetup::pagemarginsinfo_has_left():
    assert hasattr(SpreadsheetMLPrintingSetup::PageMarginsInfo, "left")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::PageMarginsInfo.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::pagemarginsinfo_has_bottom():
    assert hasattr(SpreadsheetMLPrintingSetup::PageMarginsInfo, "bottom")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::PageMarginsInfo.__mro__:
        if "bottom" in klass.__dict__:
            descriptor = klass.__dict__["bottom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::pagemarginsinfo_has_right():
    assert hasattr(SpreadsheetMLPrintingSetup::PageMarginsInfo, "right")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::PageMarginsInfo.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::pagemarginsinfo_has_top():
    assert hasattr(SpreadsheetMLPrintingSetup::PageMarginsInfo, "top")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::PageMarginsInfo.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::print_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Print)


def test_spreadsheetmlprintingsetup::print_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Print.__init__)


def test_spreadsheetmlprintingsetup::print_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Print.__init__)
    params = list(sig.parameters.keys())
    assert "leftToRight" in params, "Missing parameter 'leftToRight'"
    assert "printErrors" in params, "Missing parameter 'printErrors'"
    assert "draftQuality" in params, "Missing parameter 'draftQuality'"
    assert "commentsLayout" in params, "Missing parameter 'commentsLayout'"
    assert "blackAndWhite" in params, "Missing parameter 'blackAndWhite'"
    assert "paperSizeIndex" in params, "Missing parameter 'paperSizeIndex'"
    assert "fitHeight" in params, "Missing parameter 'fitHeight'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "gridlines" in params, "Missing parameter 'gridlines'"
    assert "verticalResolution" in params, "Missing parameter 'verticalResolution'"
    assert "validPrinterInfo" in params, "Missing parameter 'validPrinterInfo'"
    assert "numberOfCopies" in params, "Missing parameter 'numberOfCopies'"
    assert "horizontalResolution" in params, "Missing parameter 'horizontalResolution'"
    assert "rowColHeadings" in params, "Missing parameter 'rowColHeadings'"
    assert "fitWidth" in params, "Missing parameter 'fitWidth'"

def test_spreadsheetmlprintingsetup::print_has_leftToRight():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "leftToRight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "leftToRight" in klass.__dict__:
            descriptor = klass.__dict__["leftToRight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_printErrors():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "printErrors")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "printErrors" in klass.__dict__:
            descriptor = klass.__dict__["printErrors"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_draftQuality():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "draftQuality")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "draftQuality" in klass.__dict__:
            descriptor = klass.__dict__["draftQuality"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_commentsLayout():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "commentsLayout")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "commentsLayout" in klass.__dict__:
            descriptor = klass.__dict__["commentsLayout"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_blackAndWhite():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "blackAndWhite")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "blackAndWhite" in klass.__dict__:
            descriptor = klass.__dict__["blackAndWhite"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_paperSizeIndex():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "paperSizeIndex")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "paperSizeIndex" in klass.__dict__:
            descriptor = klass.__dict__["paperSizeIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_fitHeight():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "fitHeight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "fitHeight" in klass.__dict__:
            descriptor = klass.__dict__["fitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_scale():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "scale")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_gridlines():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "gridlines")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "gridlines" in klass.__dict__:
            descriptor = klass.__dict__["gridlines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_verticalResolution():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "verticalResolution")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "verticalResolution" in klass.__dict__:
            descriptor = klass.__dict__["verticalResolution"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_validPrinterInfo():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "validPrinterInfo")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "validPrinterInfo" in klass.__dict__:
            descriptor = klass.__dict__["validPrinterInfo"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_numberOfCopies():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "numberOfCopies")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "numberOfCopies" in klass.__dict__:
            descriptor = klass.__dict__["numberOfCopies"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_horizontalResolution():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "horizontalResolution")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "horizontalResolution" in klass.__dict__:
            descriptor = klass.__dict__["horizontalResolution"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_rowColHeadings():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "rowColHeadings")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "rowColHeadings" in klass.__dict__:
            descriptor = klass.__dict__["rowColHeadings"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::print_has_fitWidth():
    assert hasattr(SpreadsheetMLPrintingSetup::Print, "fitWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Print.__mro__:
        if "fitWidth" in klass.__dict__:
            descriptor = klass.__dict__["fitWidth"]
            break
    assert isinstance(descriptor, property)



def test_headerorfooterelt_is_not_abstract():
    assert not inspect.isabstract(HeaderOrFooterElt)


def test_headerorfooterelt_constructor_exists():
    assert callable(HeaderOrFooterElt.__init__)


def test_headerorfooterelt_constructor_args():
    sig = inspect.signature(HeaderOrFooterElt.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::header_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Header)


def test_spreadsheetmlprintingsetup::header_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Header.__init__)


def test_spreadsheetmlprintingsetup::header_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Header.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::headerorfooterelt_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::HeaderOrFooterElt)


def test_spreadsheetmlprintingsetup::headerorfooterelt_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::HeaderOrFooterElt.__init__)


def test_spreadsheetmlprintingsetup::headerorfooterelt_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::HeaderOrFooterElt.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "margin" in params, "Missing parameter 'margin'"

def test_spreadsheetmlprintingsetup::headerorfooterelt_has_data():
    assert hasattr(SpreadsheetMLPrintingSetup::HeaderOrFooterElt, "data")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::HeaderOrFooterElt.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::headerorfooterelt_has_margin():
    assert hasattr(SpreadsheetMLPrintingSetup::HeaderOrFooterElt, "margin")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::HeaderOrFooterElt.__mro__:
        if "margin" in klass.__dict__:
            descriptor = klass.__dict__["margin"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::footer_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Footer)


def test_spreadsheetmlprintingsetup::footer_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Footer.__init__)


def test_spreadsheetmlprintingsetup::footer_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Footer.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::layout_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Layout)


def test_spreadsheetmlprintingsetup::layout_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Layout.__init__)


def test_spreadsheetmlprintingsetup::layout_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Layout.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "centerVertical" in params, "Missing parameter 'centerVertical'"
    assert "centerHorizontal" in params, "Missing parameter 'centerHorizontal'"
    assert "startPageNumber" in params, "Missing parameter 'startPageNumber'"

def test_spreadsheetmlprintingsetup::layout_has_orientation():
    assert hasattr(SpreadsheetMLPrintingSetup::Layout, "orientation")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Layout.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::layout_has_centerVertical():
    assert hasattr(SpreadsheetMLPrintingSetup::Layout, "centerVertical")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Layout.__mro__:
        if "centerVertical" in klass.__dict__:
            descriptor = klass.__dict__["centerVertical"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::layout_has_centerHorizontal():
    assert hasattr(SpreadsheetMLPrintingSetup::Layout, "centerHorizontal")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Layout.__mro__:
        if "centerHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["centerHorizontal"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::layout_has_startPageNumber():
    assert hasattr(SpreadsheetMLPrintingSetup::Layout, "startPageNumber")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Layout.__mro__:
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



def test_spreadsheetmlprintingsetup::pagesetup_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::PageSetup)


def test_spreadsheetmlprintingsetup::pagesetup_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::PageSetup.__init__)


def test_spreadsheetmlprintingsetup::pagesetup_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::PageSetup.__init__)
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



def test_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_pagesetup_is_not_abstract():
    assert not inspect.isabstract(PageSetup)


def test_pagesetup_constructor_exists():
    assert callable(PageSetup.__init__)


def test_pagesetup_constructor_args():
    sig = inspect.signature(PageSetup.__init__)
    params = list(sig.parameters.keys())



def test_print_is_not_abstract():
    assert not inspect.isabstract(Print)


def test_print_constructor_exists():
    assert callable(Print.__init__)


def test_print_constructor_args():
    sig = inspect.signature(Print.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::worksheetoptionselt_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::WorksheetOptionsElt)


def test_spreadsheetmlprintingsetup::worksheetoptionselt_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__init__)


def test_spreadsheetmlprintingsetup::worksheetoptionselt_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__init__)
    params = list(sig.parameters.keys())
    assert "standardWidth" in params, "Missing parameter 'standardWidth'"
    assert "name" in params, "Missing parameter 'name'"
    assert "doNotDisplayOutline" in params, "Missing parameter 'doNotDisplayOutline'"
    assert "allowInsertCols" in params, "Missing parameter 'allowInsertCols'"
    assert "zoom" in params, "Missing parameter 'zoom'"
    assert "enableSelection" in params, "Missing parameter 'enableSelection'"
    assert "allowDeleteCols" in params, "Missing parameter 'allowDeleteCols'"
    assert "transitionFormulaEntry" in params, "Missing parameter 'transitionFormulaEntry'"
    assert "fitToPage" in params, "Missing parameter 'fitToPage'"
    assert "splitVertical" in params, "Missing parameter 'splitVertical'"
    assert "noSummaryColumnsRightDetail" in params, "Missing parameter 'noSummaryColumnsRightDetail'"
    assert "displayFormulas" in params, "Missing parameter 'displayFormulas'"
    assert "rangeSelection" in params, "Missing parameter 'rangeSelection'"
    assert "allowSizeCols" in params, "Missing parameter 'allowSizeCols'"
    assert "gridlineColorIndex" in params, "Missing parameter 'gridlineColorIndex'"
    assert "protectObjects" in params, "Missing parameter 'protectObjects'"
    assert "gridlineColor" in params, "Missing parameter 'gridlineColor'"
    assert "allowFormatCells" in params, "Missing parameter 'allowFormatCells'"
    assert "excelWorksheetType" in params, "Missing parameter 'excelWorksheetType'"
    assert "protectContentst" in params, "Missing parameter 'protectContentst'"
    assert "allowSort" in params, "Missing parameter 'allowSort'"
    assert "displayRightToLeft" in params, "Missing parameter 'displayRightToLeft'"
    assert "allowFilter" in params, "Missing parameter 'allowFilter'"
    assert "doNotDisplayColHeaders" in params, "Missing parameter 'doNotDisplayColHeaders'"
    assert "allowSizeRows" in params, "Missing parameter 'allowSizeRows'"
    assert "topRowVisible" in params, "Missing parameter 'topRowVisible'"
    assert "doNotDisplayZeros" in params, "Missing parameter 'doNotDisplayZeros'"
    assert "filterOn" in params, "Missing parameter 'filterOn'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "activePane" in params, "Missing parameter 'activePane'"
    assert "splitHorizontal" in params, "Missing parameter 'splitHorizontal'"
    assert "allowUsePivotTables" in params, "Missing parameter 'allowUsePivotTables'"
    assert "leftColumnVisible" in params, "Missing parameter 'leftColumnVisible'"
    assert "tabColorIndex" in params, "Missing parameter 'tabColorIndex'"
    assert "frozenNoSplit" in params, "Missing parameter 'frozenNoSplit'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"
    assert "freezePanes" in params, "Missing parameter 'freezePanes'"
    assert "unsynced" in params, "Missing parameter 'unsynced'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "doNotDisplayRowHeaders" in params, "Missing parameter 'doNotDisplayRowHeaders'"
    assert "activeRow" in params, "Missing parameter 'activeRow'"
    assert "allowInsertHyperlinks" in params, "Missing parameter 'allowInsertHyperlinks'"
    assert "codeName" in params, "Missing parameter 'codeName'"
    assert "doNotDisplayHeadings" in params, "Missing parameter 'doNotDisplayHeadings'"
    assert "selected" in params, "Missing parameter 'selected'"
    assert "allowDeleteRows" in params, "Missing parameter 'allowDeleteRows'"
    assert "intlMacro" in params, "Missing parameter 'intlMacro'"
    assert "leftColumnRightPane" in params, "Missing parameter 'leftColumnRightPane'"
    assert "doNotDisplayGridlines" in params, "Missing parameter 'doNotDisplayGridlines'"
    assert "activeColumn" in params, "Missing parameter 'activeColumn'"
    assert "noSummaryRowsBelowDetail" in params, "Missing parameter 'noSummaryRowsBelowDetail'"
    assert "applyAutomaticOutlineStyles" in params, "Missing parameter 'applyAutomaticOutlineStyles'"
    assert "topRowBottomPane" in params, "Missing parameter 'topRowBottomPane'"
    assert "displayPageBreak" in params, "Missing parameter 'displayPageBreak'"
    assert "protectScenarios" in params, "Missing parameter 'protectScenarios'"
    assert "allowInsertRows" in params, "Missing parameter 'allowInsertRows'"
    assert "showPageBreakZoom" in params, "Missing parameter 'showPageBreakZoom'"
    assert "transitionExpressionEvaluation" in params, "Missing parameter 'transitionExpressionEvaluation'"
    assert "pageBreakZoom" in params, "Missing parameter 'pageBreakZoom'"

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_standardWidth():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "standardWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "standardWidth" in klass.__dict__:
            descriptor = klass.__dict__["standardWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_name():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "name")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_doNotDisplayOutline():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "doNotDisplayOutline")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "doNotDisplayOutline" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayOutline"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_allowInsertCols():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "allowInsertCols")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "allowInsertCols" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_zoom():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "zoom")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_enableSelection():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "enableSelection")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "enableSelection" in klass.__dict__:
            descriptor = klass.__dict__["enableSelection"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_allowDeleteCols():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "allowDeleteCols")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "allowDeleteCols" in klass.__dict__:
            descriptor = klass.__dict__["allowDeleteCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_transitionFormulaEntry():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "transitionFormulaEntry")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "transitionFormulaEntry" in klass.__dict__:
            descriptor = klass.__dict__["transitionFormulaEntry"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_fitToPage():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "fitToPage")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "fitToPage" in klass.__dict__:
            descriptor = klass.__dict__["fitToPage"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_splitVertical():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "splitVertical")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "splitVertical" in klass.__dict__:
            descriptor = klass.__dict__["splitVertical"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_noSummaryColumnsRightDetail():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "noSummaryColumnsRightDetail")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "noSummaryColumnsRightDetail" in klass.__dict__:
            descriptor = klass.__dict__["noSummaryColumnsRightDetail"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_displayFormulas():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "displayFormulas")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "displayFormulas" in klass.__dict__:
            descriptor = klass.__dict__["displayFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_rangeSelection():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "rangeSelection")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "rangeSelection" in klass.__dict__:
            descriptor = klass.__dict__["rangeSelection"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_allowSizeCols():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "allowSizeCols")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "allowSizeCols" in klass.__dict__:
            descriptor = klass.__dict__["allowSizeCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_gridlineColorIndex():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "gridlineColorIndex")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "gridlineColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["gridlineColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_protectObjects():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "protectObjects")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "protectObjects" in klass.__dict__:
            descriptor = klass.__dict__["protectObjects"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_gridlineColor():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "gridlineColor")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "gridlineColor" in klass.__dict__:
            descriptor = klass.__dict__["gridlineColor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_allowFormatCells():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "allowFormatCells")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "allowFormatCells" in klass.__dict__:
            descriptor = klass.__dict__["allowFormatCells"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_excelWorksheetType():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "excelWorksheetType")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "excelWorksheetType" in klass.__dict__:
            descriptor = klass.__dict__["excelWorksheetType"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_protectContentst():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "protectContentst")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "protectContentst" in klass.__dict__:
            descriptor = klass.__dict__["protectContentst"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_allowSort():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "allowSort")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "allowSort" in klass.__dict__:
            descriptor = klass.__dict__["allowSort"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_displayRightToLeft():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "displayRightToLeft")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "displayRightToLeft" in klass.__dict__:
            descriptor = klass.__dict__["displayRightToLeft"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_allowFilter():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "allowFilter")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "allowFilter" in klass.__dict__:
            descriptor = klass.__dict__["allowFilter"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_doNotDisplayColHeaders():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "doNotDisplayColHeaders")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "doNotDisplayColHeaders" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayColHeaders"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_allowSizeRows():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "allowSizeRows")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "allowSizeRows" in klass.__dict__:
            descriptor = klass.__dict__["allowSizeRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_topRowVisible():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "topRowVisible")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "topRowVisible" in klass.__dict__:
            descriptor = klass.__dict__["topRowVisible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_doNotDisplayZeros():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "doNotDisplayZeros")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "doNotDisplayZeros" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayZeros"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_filterOn():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "filterOn")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "filterOn" in klass.__dict__:
            descriptor = klass.__dict__["filterOn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_activePane():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "activePane")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "activePane" in klass.__dict__:
            descriptor = klass.__dict__["activePane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_splitHorizontal():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "splitHorizontal")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "splitHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["splitHorizontal"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_allowUsePivotTables():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "allowUsePivotTables")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "allowUsePivotTables" in klass.__dict__:
            descriptor = klass.__dict__["allowUsePivotTables"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_leftColumnVisible():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "leftColumnVisible")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "leftColumnVisible" in klass.__dict__:
            descriptor = klass.__dict__["leftColumnVisible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_tabColorIndex():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "tabColorIndex")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "tabColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["tabColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_frozenNoSplit():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "frozenNoSplit")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "frozenNoSplit" in klass.__dict__:
            descriptor = klass.__dict__["frozenNoSplit"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_freezePanes():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "freezePanes")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "freezePanes" in klass.__dict__:
            descriptor = klass.__dict__["freezePanes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_unsynced():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "unsynced")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "unsynced" in klass.__dict__:
            descriptor = klass.__dict__["unsynced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_visible():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "visible")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_doNotDisplayRowHeaders():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "doNotDisplayRowHeaders")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "doNotDisplayRowHeaders" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayRowHeaders"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_activeRow():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "activeRow")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "activeRow" in klass.__dict__:
            descriptor = klass.__dict__["activeRow"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_allowInsertHyperlinks():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "allowInsertHyperlinks")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "allowInsertHyperlinks" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertHyperlinks"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_codeName():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "codeName")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "codeName" in klass.__dict__:
            descriptor = klass.__dict__["codeName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_doNotDisplayHeadings():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "doNotDisplayHeadings")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "doNotDisplayHeadings" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayHeadings"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_selected():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "selected")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_allowDeleteRows():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "allowDeleteRows")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "allowDeleteRows" in klass.__dict__:
            descriptor = klass.__dict__["allowDeleteRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_intlMacro():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "intlMacro")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "intlMacro" in klass.__dict__:
            descriptor = klass.__dict__["intlMacro"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_leftColumnRightPane():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "leftColumnRightPane")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "leftColumnRightPane" in klass.__dict__:
            descriptor = klass.__dict__["leftColumnRightPane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_doNotDisplayGridlines():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "doNotDisplayGridlines")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "doNotDisplayGridlines" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayGridlines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_activeColumn():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "activeColumn")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "activeColumn" in klass.__dict__:
            descriptor = klass.__dict__["activeColumn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_noSummaryRowsBelowDetail():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "noSummaryRowsBelowDetail")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "noSummaryRowsBelowDetail" in klass.__dict__:
            descriptor = klass.__dict__["noSummaryRowsBelowDetail"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_applyAutomaticOutlineStyles():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "applyAutomaticOutlineStyles")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "applyAutomaticOutlineStyles" in klass.__dict__:
            descriptor = klass.__dict__["applyAutomaticOutlineStyles"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_topRowBottomPane():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "topRowBottomPane")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "topRowBottomPane" in klass.__dict__:
            descriptor = klass.__dict__["topRowBottomPane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_displayPageBreak():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "displayPageBreak")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "displayPageBreak" in klass.__dict__:
            descriptor = klass.__dict__["displayPageBreak"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_protectScenarios():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "protectScenarios")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "protectScenarios" in klass.__dict__:
            descriptor = klass.__dict__["protectScenarios"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_allowInsertRows():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "allowInsertRows")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "allowInsertRows" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_showPageBreakZoom():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "showPageBreakZoom")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "showPageBreakZoom" in klass.__dict__:
            descriptor = klass.__dict__["showPageBreakZoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_transitionExpressionEvaluation():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "transitionExpressionEvaluation")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "transitionExpressionEvaluation" in klass.__dict__:
            descriptor = klass.__dict__["transitionExpressionEvaluation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheetoptionselt_has_pageBreakZoom():
    assert hasattr(SpreadsheetMLPrintingSetup::WorksheetOptionsElt, "pageBreakZoom")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::WorksheetOptionsElt.__mro__:
        if "pageBreakZoom" in klass.__dict__:
            descriptor = klass.__dict__["pageBreakZoom"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::data_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Data)


def test_spreadsheetmlprintingsetup::data_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Data.__init__)


def test_spreadsheetmlprintingsetup::data_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Data.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::excelworkbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::ExcelWorkbook)


def test_spreadsheetmlprintingsetup::excelworkbook_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::ExcelWorkbook.__init__)


def test_spreadsheetmlprintingsetup::excelworkbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::ExcelWorkbook.__init__)
    params = list(sig.parameters.keys())
    assert "precisionAsDisplayed" in params, "Missing parameter 'precisionAsDisplayed'"
    assert "noAutoRecover" in params, "Missing parameter 'noAutoRecover'"
    assert "protectWindows" in params, "Missing parameter 'protectWindows'"
    assert "hideVerticalScrollBar" in params, "Missing parameter 'hideVerticalScrollBar'"
    assert "embedSaveSmartTags" in params, "Missing parameter 'embedSaveSmartTags'"
    assert "activeSheet" in params, "Missing parameter 'activeSheet'"
    assert "windowTopY" in params, "Missing parameter 'windowTopY'"
    assert "windowHeight" in params, "Missing parameter 'windowHeight'"
    assert "calculation" in params, "Missing parameter 'calculation'"
    assert "hideHorizontalScrollBar" in params, "Missing parameter 'hideHorizontalScrollBar'"
    assert "hidePivotTableFieldList" in params, "Missing parameter 'hidePivotTableFieldList'"
    assert "refModeR1C1" in params, "Missing parameter 'refModeR1C1'"
    assert "date1904" in params, "Missing parameter 'date1904'"
    assert "doNotCalculateBeforeSave" in params, "Missing parameter 'doNotCalculateBeforeSave'"
    assert "iteration" in params, "Missing parameter 'iteration'"
    assert "windowWidth" in params, "Missing parameter 'windowWidth'"
    assert "createBackup" in params, "Missing parameter 'createBackup'"
    assert "tabRatio" in params, "Missing parameter 'tabRatio'"
    assert "windowTopX" in params, "Missing parameter 'windowTopX'"
    assert "protectStructure" in params, "Missing parameter 'protectStructure'"
    assert "windowIconic" in params, "Missing parameter 'windowIconic'"
    assert "maxIterations" in params, "Missing parameter 'maxIterations'"
    assert "maxChange" in params, "Missing parameter 'maxChange'"
    assert "futureVer" in params, "Missing parameter 'futureVer'"
    assert "acceptLabelsInFormulas" in params, "Missing parameter 'acceptLabelsInFormulas'"
    assert "doNotSaveLinkValues" in params, "Missing parameter 'doNotSaveLinkValues'"
    assert "displayDrawingObjects" in params, "Missing parameter 'displayDrawingObjects'"
    assert "hideWorkbookTabs" in params, "Missing parameter 'hideWorkbookTabs'"
    assert "firstVisibleSheet" in params, "Missing parameter 'firstVisibleSheet'"
    assert "windowHidden" in params, "Missing parameter 'windowHidden'"
    assert "selectedSheets" in params, "Missing parameter 'selectedSheets'"
    assert "uncalced" in params, "Missing parameter 'uncalced'"
    assert "displayInkNotes" in params, "Missing parameter 'displayInkNotes'"
    assert "activeChart" in params, "Missing parameter 'activeChart'"

def test_spreadsheetmlprintingsetup::excelworkbook_has_precisionAsDisplayed():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "precisionAsDisplayed")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "precisionAsDisplayed" in klass.__dict__:
            descriptor = klass.__dict__["precisionAsDisplayed"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_noAutoRecover():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "noAutoRecover")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "noAutoRecover" in klass.__dict__:
            descriptor = klass.__dict__["noAutoRecover"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_protectWindows():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "protectWindows")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "protectWindows" in klass.__dict__:
            descriptor = klass.__dict__["protectWindows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_hideVerticalScrollBar():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "hideVerticalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "hideVerticalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideVerticalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_embedSaveSmartTags():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "embedSaveSmartTags")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "embedSaveSmartTags" in klass.__dict__:
            descriptor = klass.__dict__["embedSaveSmartTags"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_activeSheet():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "activeSheet")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "activeSheet" in klass.__dict__:
            descriptor = klass.__dict__["activeSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_windowTopY():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "windowTopY")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "windowTopY" in klass.__dict__:
            descriptor = klass.__dict__["windowTopY"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_windowHeight():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "windowHeight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "windowHeight" in klass.__dict__:
            descriptor = klass.__dict__["windowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_calculation():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "calculation")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "calculation" in klass.__dict__:
            descriptor = klass.__dict__["calculation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_hideHorizontalScrollBar():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "hideHorizontalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "hideHorizontalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideHorizontalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_hidePivotTableFieldList():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "hidePivotTableFieldList")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "hidePivotTableFieldList" in klass.__dict__:
            descriptor = klass.__dict__["hidePivotTableFieldList"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_refModeR1C1():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "refModeR1C1")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "refModeR1C1" in klass.__dict__:
            descriptor = klass.__dict__["refModeR1C1"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_date1904():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "date1904")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "date1904" in klass.__dict__:
            descriptor = klass.__dict__["date1904"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_doNotCalculateBeforeSave():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "doNotCalculateBeforeSave")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "doNotCalculateBeforeSave" in klass.__dict__:
            descriptor = klass.__dict__["doNotCalculateBeforeSave"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_iteration():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "iteration")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "iteration" in klass.__dict__:
            descriptor = klass.__dict__["iteration"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_windowWidth():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "windowWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "windowWidth" in klass.__dict__:
            descriptor = klass.__dict__["windowWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_createBackup():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "createBackup")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "createBackup" in klass.__dict__:
            descriptor = klass.__dict__["createBackup"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_tabRatio():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "tabRatio")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "tabRatio" in klass.__dict__:
            descriptor = klass.__dict__["tabRatio"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_windowTopX():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "windowTopX")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "windowTopX" in klass.__dict__:
            descriptor = klass.__dict__["windowTopX"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_protectStructure():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "protectStructure")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "protectStructure" in klass.__dict__:
            descriptor = klass.__dict__["protectStructure"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_windowIconic():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "windowIconic")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "windowIconic" in klass.__dict__:
            descriptor = klass.__dict__["windowIconic"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_maxIterations():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "maxIterations")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "maxIterations" in klass.__dict__:
            descriptor = klass.__dict__["maxIterations"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_maxChange():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "maxChange")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "maxChange" in klass.__dict__:
            descriptor = klass.__dict__["maxChange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_futureVer():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "futureVer")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "futureVer" in klass.__dict__:
            descriptor = klass.__dict__["futureVer"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_acceptLabelsInFormulas():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "acceptLabelsInFormulas")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "acceptLabelsInFormulas" in klass.__dict__:
            descriptor = klass.__dict__["acceptLabelsInFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_doNotSaveLinkValues():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "doNotSaveLinkValues")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "doNotSaveLinkValues" in klass.__dict__:
            descriptor = klass.__dict__["doNotSaveLinkValues"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_displayDrawingObjects():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "displayDrawingObjects")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "displayDrawingObjects" in klass.__dict__:
            descriptor = klass.__dict__["displayDrawingObjects"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_hideWorkbookTabs():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "hideWorkbookTabs")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "hideWorkbookTabs" in klass.__dict__:
            descriptor = klass.__dict__["hideWorkbookTabs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_firstVisibleSheet():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "firstVisibleSheet")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "firstVisibleSheet" in klass.__dict__:
            descriptor = klass.__dict__["firstVisibleSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_windowHidden():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "windowHidden")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "windowHidden" in klass.__dict__:
            descriptor = klass.__dict__["windowHidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_selectedSheets():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "selectedSheets")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "selectedSheets" in klass.__dict__:
            descriptor = klass.__dict__["selectedSheets"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_uncalced():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "uncalced")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "uncalced" in klass.__dict__:
            descriptor = klass.__dict__["uncalced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_displayInkNotes():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "displayInkNotes")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "displayInkNotes" in klass.__dict__:
            descriptor = klass.__dict__["displayInkNotes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::excelworkbook_has_activeChart():
    assert hasattr(SpreadsheetMLPrintingSetup::ExcelWorkbook, "activeChart")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ExcelWorkbook.__mro__:
        if "activeChart" in klass.__dict__:
            descriptor = klass.__dict__["activeChart"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::comment_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Comment)


def test_spreadsheetmlprintingsetup::comment_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Comment.__init__)


def test_spreadsheetmlprintingsetup::comment_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "showAlways" in params, "Missing parameter 'showAlways'"

def test_spreadsheetmlprintingsetup::comment_has_author():
    assert hasattr(SpreadsheetMLPrintingSetup::Comment, "author")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Comment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::comment_has_showAlways():
    assert hasattr(SpreadsheetMLPrintingSetup::Comment, "showAlways")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Comment.__mro__:
        if "showAlways" in klass.__dict__:
            descriptor = klass.__dict__["showAlways"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(ColOrRowElement)


def test_colorrowelement_constructor_exists():
    assert callable(ColOrRowElement.__init__)


def test_colorrowelement_constructor_args():
    sig = inspect.signature(ColOrRowElement.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::row_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Row)


def test_spreadsheetmlprintingsetup::row_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Row.__init__)


def test_spreadsheetmlprintingsetup::row_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Row.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitHeight" in params, "Missing parameter 'autoFitHeight'"
    assert "height" in params, "Missing parameter 'height'"

def test_spreadsheetmlprintingsetup::row_has_autoFitHeight():
    assert hasattr(SpreadsheetMLPrintingSetup::Row, "autoFitHeight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Row.__mro__:
        if "autoFitHeight" in klass.__dict__:
            descriptor = klass.__dict__["autoFitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::row_has_height():
    assert hasattr(SpreadsheetMLPrintingSetup::Row, "height")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Row.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::column_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Column)


def test_spreadsheetmlprintingsetup::column_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Column.__init__)


def test_spreadsheetmlprintingsetup::column_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Column.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitWidth" in params, "Missing parameter 'autoFitWidth'"
    assert "width" in params, "Missing parameter 'width'"

def test_spreadsheetmlprintingsetup::column_has_autoFitWidth():
    assert hasattr(SpreadsheetMLPrintingSetup::Column, "autoFitWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Column.__mro__:
        if "autoFitWidth" in klass.__dict__:
            descriptor = klass.__dict__["autoFitWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::column_has_width():
    assert hasattr(SpreadsheetMLPrintingSetup::Column, "width")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Column.__mro__:
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



def test_spreadsheetmlprintingsetup::cell_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Cell)


def test_spreadsheetmlprintingsetup::cell_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Cell.__init__)


def test_spreadsheetmlprintingsetup::cell_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Cell.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"
    assert "hRef" in params, "Missing parameter 'hRef'"
    assert "mergeDown" in params, "Missing parameter 'mergeDown'"
    assert "mergeAcross" in params, "Missing parameter 'mergeAcross'"
    assert "arrayRange" in params, "Missing parameter 'arrayRange'"

def test_spreadsheetmlprintingsetup::cell_has_formula():
    assert hasattr(SpreadsheetMLPrintingSetup::Cell, "formula")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::cell_has_hRef():
    assert hasattr(SpreadsheetMLPrintingSetup::Cell, "hRef")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Cell.__mro__:
        if "hRef" in klass.__dict__:
            descriptor = klass.__dict__["hRef"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::cell_has_mergeDown():
    assert hasattr(SpreadsheetMLPrintingSetup::Cell, "mergeDown")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Cell.__mro__:
        if "mergeDown" in klass.__dict__:
            descriptor = klass.__dict__["mergeDown"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::cell_has_mergeAcross():
    assert hasattr(SpreadsheetMLPrintingSetup::Cell, "mergeAcross")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Cell.__mro__:
        if "mergeAcross" in klass.__dict__:
            descriptor = klass.__dict__["mergeAcross"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::cell_has_arrayRange():
    assert hasattr(SpreadsheetMLPrintingSetup::Cell, "arrayRange")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Cell.__mro__:
        if "arrayRange" in klass.__dict__:
            descriptor = klass.__dict__["arrayRange"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::colorrowelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::ColOrRowElement)


def test_spreadsheetmlprintingsetup::colorrowelement_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::ColOrRowElement.__init__)


def test_spreadsheetmlprintingsetup::colorrowelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "hidden" in params, "Missing parameter 'hidden'"
    assert "span" in params, "Missing parameter 'span'"

def test_spreadsheetmlprintingsetup::colorrowelement_has_hidden():
    assert hasattr(SpreadsheetMLPrintingSetup::ColOrRowElement, "hidden")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::colorrowelement_has_span():
    assert hasattr(SpreadsheetMLPrintingSetup::ColOrRowElement, "span")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)



def test_excelworkbook_is_not_abstract():
    assert not inspect.isabstract(ExcelWorkbook)


def test_excelworkbook_constructor_exists():
    assert callable(ExcelWorkbook.__init__)


def test_excelworkbook_constructor_args():
    sig = inspect.signature(ExcelWorkbook.__init__)
    params = list(sig.parameters.keys())



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



def test_spreadsheetmlprintingsetup::tableelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::TableElement)


def test_spreadsheetmlprintingsetup::tableelement_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::TableElement.__init__)


def test_spreadsheetmlprintingsetup::tableelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_spreadsheetmlprintingsetup::tableelement_has_index():
    assert hasattr(SpreadsheetMLPrintingSetup::TableElement, "index")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::TableElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::table_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Table)


def test_spreadsheetmlprintingsetup::table_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Table.__init__)


def test_spreadsheetmlprintingsetup::table_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Table.__init__)
    params = list(sig.parameters.keys())
    assert "leftCell" in params, "Missing parameter 'leftCell'"
    assert "fullColumns" in params, "Missing parameter 'fullColumns'"
    assert "expandedColumnCount" in params, "Missing parameter 'expandedColumnCount'"
    assert "expandedRowCount" in params, "Missing parameter 'expandedRowCount'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "fullRows" in params, "Missing parameter 'fullRows'"
    assert "topCell" in params, "Missing parameter 'topCell'"

def test_spreadsheetmlprintingsetup::table_has_leftCell():
    assert hasattr(SpreadsheetMLPrintingSetup::Table, "leftCell")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Table.__mro__:
        if "leftCell" in klass.__dict__:
            descriptor = klass.__dict__["leftCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::table_has_fullColumns():
    assert hasattr(SpreadsheetMLPrintingSetup::Table, "fullColumns")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Table.__mro__:
        if "fullColumns" in klass.__dict__:
            descriptor = klass.__dict__["fullColumns"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::table_has_expandedColumnCount():
    assert hasattr(SpreadsheetMLPrintingSetup::Table, "expandedColumnCount")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Table.__mro__:
        if "expandedColumnCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedColumnCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::table_has_expandedRowCount():
    assert hasattr(SpreadsheetMLPrintingSetup::Table, "expandedRowCount")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Table.__mro__:
        if "expandedRowCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedRowCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::table_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLPrintingSetup::Table, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Table.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::table_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLPrintingSetup::Table, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Table.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::table_has_fullRows():
    assert hasattr(SpreadsheetMLPrintingSetup::Table, "fullRows")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Table.__mro__:
        if "fullRows" in klass.__dict__:
            descriptor = klass.__dict__["fullRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::table_has_topCell():
    assert hasattr(SpreadsheetMLPrintingSetup::Table, "topCell")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Table.__mro__:
        if "topCell" in klass.__dict__:
            descriptor = klass.__dict__["topCell"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::styledelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::StyledElement)


def test_spreadsheetmlprintingsetup::styledelement_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::StyledElement.__init__)


def test_spreadsheetmlprintingsetup::styledelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::StyledElement.__init__)
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



def test_spreadsheetmlprintingsetup::worksheet_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Worksheet)


def test_spreadsheetmlprintingsetup::worksheet_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Worksheet.__init__)


def test_spreadsheetmlprintingsetup::worksheet_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "protected" in params, "Missing parameter 'protected'"
    assert "name" in params, "Missing parameter 'name'"
    assert "rightToLeft" in params, "Missing parameter 'rightToLeft'"

def test_spreadsheetmlprintingsetup::worksheet_has_protected():
    assert hasattr(SpreadsheetMLPrintingSetup::Worksheet, "protected")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Worksheet.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheet_has_name():
    assert hasattr(SpreadsheetMLPrintingSetup::Worksheet, "name")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Worksheet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::worksheet_has_rightToLeft():
    assert hasattr(SpreadsheetMLPrintingSetup::Worksheet, "rightToLeft")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::Worksheet.__mro__:
        if "rightToLeft" in klass.__dict__:
            descriptor = klass.__dict__["rightToLeft"]
            break
    assert isinstance(descriptor, property)



def test_worksheet_is_not_abstract():
    assert not inspect.isabstract(Worksheet)


def test_worksheet_constructor_exists():
    assert callable(Worksheet.__init__)


def test_worksheet_constructor_args():
    sig = inspect.signature(Worksheet.__init__)
    params = list(sig.parameters.keys())



def test_customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentProperty)


def test_customdocumentproperty_constructor_exists():
    assert callable(CustomDocumentProperty.__init__)


def test_customdocumentproperty_constructor_args():
    sig = inspect.signature(CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())



def test_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DocumentPropertiesCollection)


def test_documentpropertiescollection_constructor_exists():
    assert callable(DocumentPropertiesCollection.__init__)


def test_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::workbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::Workbook)


def test_spreadsheetmlprintingsetup::workbook_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::Workbook.__init__)


def test_spreadsheetmlprintingsetup::workbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::Workbook.__init__)
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



def test_spreadsheetmlprintingsetup::smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::SmartTagsCollection)


def test_spreadsheetmlprintingsetup::smarttagscollection_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::SmartTagsCollection.__init__)


def test_spreadsheetmlprintingsetup::smarttagscollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SmartTagsCollection)


def test_smarttagscollection_constructor_exists():
    assert callable(SmartTagsCollection.__init__)


def test_smarttagscollection_constructor_args():
    sig = inspect.signature(SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::SmartTagType)


def test_spreadsheetmlprintingsetup::smarttagtype_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::SmartTagType.__init__)


def test_spreadsheetmlprintingsetup::smarttagtype_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"

def test_spreadsheetmlprintingsetup::smarttagtype_has_name():
    assert hasattr(SpreadsheetMLPrintingSetup::SmartTagType, "name")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::smarttagtype_has_url():
    assert hasattr(SpreadsheetMLPrintingSetup::SmartTagType, "url")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::smarttagtype_has_namespaceuri():
    assert hasattr(SpreadsheetMLPrintingSetup::SmartTagType, "namespaceuri")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::CustomDocumentProperty)


def test_spreadsheetmlprintingsetup::customdocumentproperty_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::CustomDocumentProperty.__init__)


def test_spreadsheetmlprintingsetup::customdocumentproperty_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlprintingsetup::customdocumentproperty_has_name():
    assert hasattr(SpreadsheetMLPrintingSetup::CustomDocumentProperty, "name")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::CustomDocumentProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::CustomDocumentPropertiesCollection)


def test_spreadsheetmlprintingsetup::customdocumentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::CustomDocumentPropertiesCollection.__init__)


def test_spreadsheetmlprintingsetup::customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_versiontype_is_not_abstract():
    assert not inspect.isabstract(VersionType)


def test_versiontype_constructor_exists():
    assert callable(VersionType.__init__)


def test_versiontype_constructor_args():
    sig = inspect.signature(VersionType.__init__)
    params = list(sig.parameters.keys())



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::numbervalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::NumberValue)


def test_spreadsheetmlprintingsetup::numbervalue_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::NumberValue.__init__)


def test_spreadsheetmlprintingsetup::numbervalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlprintingsetup::numbervalue_has_value():
    assert hasattr(SpreadsheetMLPrintingSetup::NumberValue, "value")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::stringvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::StringValue)


def test_spreadsheetmlprintingsetup::stringvalue_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::StringValue.__init__)


def test_spreadsheetmlprintingsetup::stringvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlprintingsetup::stringvalue_has_value():
    assert hasattr(SpreadsheetMLPrintingSetup::StringValue, "value")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::StringValue.__mro__:
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



def test_workbook_is_not_abstract():
    assert not inspect.isabstract(Workbook)


def test_workbook_constructor_exists():
    assert callable(Workbook.__init__)


def test_workbook_constructor_args():
    sig = inspect.signature(Workbook.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection)


def test_spreadsheetmlprintingsetup::documentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__init__)


def test_spreadsheetmlprintingsetup::documentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "lines" in params, "Missing parameter 'lines'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "company" in params, "Missing parameter 'company'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "words" in params, "Missing parameter 'words'"
    assert "title" in params, "Missing parameter 'title'"
    assert "description" in params, "Missing parameter 'description'"
    assert "author" in params, "Missing parameter 'author'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "category" in params, "Missing parameter 'category'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "revision" in params, "Missing parameter 'revision'"
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_paragraphs():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_lines():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_totalTime():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_pages():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_lastAuthor():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_company():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_manager():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_guid():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_words():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_title():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_description():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_author():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_appName():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_category():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_keywords():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_revision():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_bytes():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_subject():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_characters():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::documentpropertiescollection_has_presentationFormat():
    assert hasattr(SpreadsheetMLPrintingSetup::DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::errorvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::ErrorValue)


def test_spreadsheetmlprintingsetup::errorvalue_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::ErrorValue.__init__)


def test_spreadsheetmlprintingsetup::errorvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::BooleanValue)


def test_spreadsheetmlprintingsetup::booleanvalue_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::BooleanValue.__init__)


def test_spreadsheetmlprintingsetup::booleanvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlprintingsetup::booleanvalue_has_value():
    assert hasattr(SpreadsheetMLPrintingSetup::BooleanValue, "value")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DateTimeType)


def test_datetimetype_constructor_exists():
    assert callable(DateTimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::DateTimeTypeValue)


def test_spreadsheetmlprintingsetup::datetimetypevalue_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::DateTimeTypeValue.__init__)


def test_spreadsheetmlprintingsetup::datetimetypevalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::datetimetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::DateTimeType)


def test_spreadsheetmlprintingsetup::datetimetype_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::DateTimeType.__init__)


def test_spreadsheetmlprintingsetup::datetimetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "year" in params, "Missing parameter 'year'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "second" in params, "Missing parameter 'second'"
    assert "day" in params, "Missing parameter 'day'"

def test_spreadsheetmlprintingsetup::datetimetype_has_month():
    assert hasattr(SpreadsheetMLPrintingSetup::DateTimeType, "month")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::datetimetype_has_year():
    assert hasattr(SpreadsheetMLPrintingSetup::DateTimeType, "year")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::datetimetype_has_minute():
    assert hasattr(SpreadsheetMLPrintingSetup::DateTimeType, "minute")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::datetimetype_has_hour():
    assert hasattr(SpreadsheetMLPrintingSetup::DateTimeType, "hour")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::datetimetype_has_second():
    assert hasattr(SpreadsheetMLPrintingSetup::DateTimeType, "second")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::datetimetype_has_day():
    assert hasattr(SpreadsheetMLPrintingSetup::DateTimeType, "day")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup::valuetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::ValueType)


def test_spreadsheetmlprintingsetup::valuetype_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::ValueType.__init__)


def test_spreadsheetmlprintingsetup::valuetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup::versiontype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup::VersionType)


def test_spreadsheetmlprintingsetup::versiontype_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup::VersionType.__init__)


def test_spreadsheetmlprintingsetup::versiontype_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup::VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"
    assert "nn" in params, "Missing parameter 'nn'"

def test_spreadsheetmlprintingsetup::versiontype_has_n():
    assert hasattr(SpreadsheetMLPrintingSetup::VersionType, "n")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::VersionType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup::versiontype_has_nn():
    assert hasattr(SpreadsheetMLPrintingSetup::VersionType, "nn")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup::VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)

def test_calculationworkbooktype_exists():
    # Check that the Enumeration exists
    assert CalculationWorkbookType is not None

def test_calculationworkbooktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CalculationWorkbookType]
    expected_literals = [
        "cwt_manualCalculation",
        "cwt_semiAutomaticCalculation",
        "cwt_automaticCalculation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CalculationWorkbookType"

def test_commentslayouttype_exists():
    # Check that the Enumeration exists
    assert CommentsLayoutType is not None

def test_commentslayouttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CommentsLayoutType]
    expected_literals = [
        "clt_PrintNone",
        "clt_SheetEnd",
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
        "vt_SheetVeryHidden",
        "vt_SheetHidden",
        "vt_SheetVisible",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibleType"

def test_excelworksheettypetype_exists():
    # Check that the Enumeration exists
    assert ExcelWorksheetTypeType is not None

def test_excelworksheettypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExcelWorksheetTypeType]
    expected_literals = [
        "ewt_Worksheet",
        "ewt_Dialog",
        "ewt_Chart",
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
        "ot_Portrait",
        "ot_Landscape",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrientationType"

def test_displaydrawingobjectstype_exists():
    # Check that the Enumeration exists
    assert DisplayDrawingObjectsType is not None

def test_displaydrawingobjectstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DisplayDrawingObjectsType]
    expected_literals = [
        "ddot_hideAll",
        "ddot_placeHolders",
        "ddot_displayShapes",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DisplayDrawingObjectsType"


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
SpreadsheetMLPrintingSetup::PageMarginsInfo_strategy = st.builds(
    SpreadsheetMLPrintingSetup::PageMarginsInfo,
    left=
        safe_text,
    bottom=
        safe_text,
    right=
        safe_text,
    top=
        safe_text
)
SpreadsheetMLPrintingSetup::Print_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Print,
    leftToRight=
        safe_text,
    printErrors=
        safe_text,
    draftQuality=
        safe_text,
    commentsLayout=
        safe_text,
    blackAndWhite=
        safe_text,
    paperSizeIndex=
        safe_text,
    fitHeight=
        safe_text,
    scale=
        safe_text,
    gridlines=
        safe_text,
    verticalResolution=
        safe_text,
    validPrinterInfo=
        safe_text,
    numberOfCopies=
        safe_text,
    horizontalResolution=
        safe_text,
    rowColHeadings=
        safe_text,
    fitWidth=
        safe_text
)
HeaderOrFooterElt_strategy = st.builds(
    HeaderOrFooterElt,
)
SpreadsheetMLPrintingSetup::Header_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Header,
)
SpreadsheetMLPrintingSetup::HeaderOrFooterElt_strategy = st.builds(
    SpreadsheetMLPrintingSetup::HeaderOrFooterElt,
    data=
        safe_text,
    margin=
        safe_text
)
SpreadsheetMLPrintingSetup::Footer_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Footer,
)
SpreadsheetMLPrintingSetup::Layout_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Layout,
    orientation=
        safe_text,
    centerVertical=
        safe_text,
    centerHorizontal=
        safe_text,
    startPageNumber=
        safe_text
)
PageMarginsInfo_strategy = st.builds(
    PageMarginsInfo,
)
SpreadsheetMLPrintingSetup::PageSetup_strategy = st.builds(
    SpreadsheetMLPrintingSetup::PageSetup,
)
Footer_strategy = st.builds(
    Footer,
)
Header_strategy = st.builds(
    Header,
)
Layout_strategy = st.builds(
    Layout,
)
PageSetup_strategy = st.builds(
    PageSetup,
)
Print_strategy = st.builds(
    Print,
)
SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy = st.builds(
    SpreadsheetMLPrintingSetup::WorksheetOptionsElt,
    standardWidth=
        safe_text,
    name=
        safe_text,
    doNotDisplayOutline=
        safe_text,
    allowInsertCols=
        safe_text,
    zoom=
        safe_text,
    enableSelection=
        safe_text,
    allowDeleteCols=
        safe_text,
    transitionFormulaEntry=
        safe_text,
    fitToPage=
        safe_text,
    splitVertical=
        safe_text,
    noSummaryColumnsRightDetail=
        safe_text,
    displayFormulas=
        safe_text,
    rangeSelection=
        safe_text,
    allowSizeCols=
        safe_text,
    gridlineColorIndex=
        safe_text,
    protectObjects=
        safe_text,
    gridlineColor=
        safe_text,
    allowFormatCells=
        safe_text,
    excelWorksheetType=
        safe_text,
    protectContentst=
        safe_text,
    allowSort=
        safe_text,
    displayRightToLeft=
        safe_text,
    allowFilter=
        safe_text,
    doNotDisplayColHeaders=
        safe_text,
    allowSizeRows=
        safe_text,
    topRowVisible=
        safe_text,
    doNotDisplayZeros=
        safe_text,
    filterOn=
        safe_text,
    defaultRowHeight=
        safe_text,
    activePane=
        safe_text,
    splitHorizontal=
        safe_text,
    allowUsePivotTables=
        safe_text,
    leftColumnVisible=
        safe_text,
    tabColorIndex=
        safe_text,
    frozenNoSplit=
        safe_text,
    defaultColumnWidth=
        safe_text,
    freezePanes=
        safe_text,
    unsynced=
        safe_text,
    visible=
        safe_text,
    doNotDisplayRowHeaders=
        safe_text,
    activeRow=
        safe_text,
    allowInsertHyperlinks=
        safe_text,
    codeName=
        safe_text,
    doNotDisplayHeadings=
        safe_text,
    selected=
        safe_text,
    allowDeleteRows=
        safe_text,
    intlMacro=
        safe_text,
    leftColumnRightPane=
        safe_text,
    doNotDisplayGridlines=
        safe_text,
    activeColumn=
        safe_text,
    noSummaryRowsBelowDetail=
        safe_text,
    applyAutomaticOutlineStyles=
        safe_text,
    topRowBottomPane=
        safe_text,
    displayPageBreak=
        safe_text,
    protectScenarios=
        safe_text,
    allowInsertRows=
        safe_text,
    showPageBreakZoom=
        safe_text,
    transitionExpressionEvaluation=
        safe_text,
    pageBreakZoom=
        safe_text
)
SpreadsheetMLPrintingSetup::Data_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Data,
)
SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy = st.builds(
    SpreadsheetMLPrintingSetup::ExcelWorkbook,
    precisionAsDisplayed=
        safe_text,
    noAutoRecover=
        safe_text,
    protectWindows=
        safe_text,
    hideVerticalScrollBar=
        safe_text,
    embedSaveSmartTags=
        safe_text,
    activeSheet=
        safe_text,
    windowTopY=
        safe_text,
    windowHeight=
        safe_text,
    calculation=
        safe_text,
    hideHorizontalScrollBar=
        safe_text,
    hidePivotTableFieldList=
        safe_text,
    refModeR1C1=
        safe_text,
    date1904=
        safe_text,
    doNotCalculateBeforeSave=
        safe_text,
    iteration=
        safe_text,
    windowWidth=
        safe_text,
    createBackup=
        safe_text,
    tabRatio=
        safe_text,
    windowTopX=
        safe_text,
    protectStructure=
        safe_text,
    windowIconic=
        safe_text,
    maxIterations=
        safe_text,
    maxChange=
        safe_text,
    futureVer=
        safe_text,
    acceptLabelsInFormulas=
        safe_text,
    doNotSaveLinkValues=
        safe_text,
    displayDrawingObjects=
        safe_text,
    hideWorkbookTabs=
        safe_text,
    firstVisibleSheet=
        safe_text,
    windowHidden=
        safe_text,
    selectedSheets=
        safe_text,
    uncalced=
        safe_text,
    displayInkNotes=
        safe_text,
    activeChart=
        safe_text
)
SpreadsheetMLPrintingSetup::Comment_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Comment,
    author=
        safe_text,
    showAlways=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
ColOrRowElement_strategy = st.builds(
    ColOrRowElement,
)
SpreadsheetMLPrintingSetup::Row_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Row,
    autoFitHeight=
        safe_text,
    height=
        safe_text
)
SpreadsheetMLPrintingSetup::Column_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Column,
    autoFitWidth=
        safe_text,
    width=
        safe_text
)
TableElement_strategy = st.builds(
    TableElement,
)
SpreadsheetMLPrintingSetup::Cell_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Cell,
    formula=
        safe_text,
    hRef=
        safe_text,
    mergeDown=
        safe_text,
    mergeAcross=
        safe_text,
    arrayRange=
        safe_text
)
SpreadsheetMLPrintingSetup::ColOrRowElement_strategy = st.builds(
    SpreadsheetMLPrintingSetup::ColOrRowElement,
    hidden=
        safe_text,
    span=
        safe_text
)
ExcelWorkbook_strategy = st.builds(
    ExcelWorkbook,
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
SpreadsheetMLPrintingSetup::TableElement_strategy = st.builds(
    SpreadsheetMLPrintingSetup::TableElement,
    index=
        safe_text
)
SpreadsheetMLPrintingSetup::Table_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Table,
    leftCell=
        safe_text,
    fullColumns=
        safe_text,
    expandedColumnCount=
        safe_text,
    expandedRowCount=
        safe_text,
    defaultColumnWidth=
        safe_text,
    defaultRowHeight=
        safe_text,
    fullRows=
        safe_text,
    topCell=
        safe_text
)
SpreadsheetMLPrintingSetup::StyledElement_strategy = st.builds(
    SpreadsheetMLPrintingSetup::StyledElement,
)
WorksheetOptionsElt_strategy = st.builds(
    WorksheetOptionsElt,
)
Table_strategy = st.builds(
    Table,
)
SpreadsheetMLPrintingSetup::Worksheet_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Worksheet,
    protected=
        safe_text,
    name=
        safe_text,
    rightToLeft=
        safe_text
)
Worksheet_strategy = st.builds(
    Worksheet,
)
CustomDocumentProperty_strategy = st.builds(
    CustomDocumentProperty,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
SpreadsheetMLPrintingSetup::Workbook_strategy = st.builds(
    SpreadsheetMLPrintingSetup::Workbook,
)
SmartTagType_strategy = st.builds(
    SmartTagType,
)
Cell_strategy = st.builds(
    Cell,
)
SpreadsheetMLPrintingSetup::SmartTagsCollection_strategy = st.builds(
    SpreadsheetMLPrintingSetup::SmartTagsCollection,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)
SpreadsheetMLPrintingSetup::SmartTagType_strategy = st.builds(
    SpreadsheetMLPrintingSetup::SmartTagType,
    name=
        safe_text,
    url=
        safe_text,
    namespaceuri=
        safe_text
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
SpreadsheetMLPrintingSetup::CustomDocumentProperty_strategy = st.builds(
    SpreadsheetMLPrintingSetup::CustomDocumentProperty,
    name=
        safe_text
)
SpreadsheetMLPrintingSetup::CustomDocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLPrintingSetup::CustomDocumentPropertiesCollection,
)
VersionType_strategy = st.builds(
    VersionType,
)
ValueType_strategy = st.builds(
    ValueType,
)
SpreadsheetMLPrintingSetup::NumberValue_strategy = st.builds(
    SpreadsheetMLPrintingSetup::NumberValue,
    value=
        safe_text
)
SpreadsheetMLPrintingSetup::StringValue_strategy = st.builds(
    SpreadsheetMLPrintingSetup::StringValue,
    value=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
Workbook_strategy = st.builds(
    Workbook,
)
SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLPrintingSetup::DocumentPropertiesCollection,
    paragraphs=
        safe_text,
    lines=
        safe_text,
    hyperlinkBase=
        safe_text,
    totalTime=
        safe_text,
    pages=
        safe_text,
    lastAuthor=
        safe_text,
    company=
        safe_text,
    manager=
        safe_text,
    guid=
        safe_text,
    words=
        safe_text,
    title=
        safe_text,
    description=
        safe_text,
    author=
        safe_text,
    appName=
        safe_text,
    category=
        safe_text,
    keywords=
        safe_text,
    revision=
        safe_text,
    bytes=
        safe_text,
    subject=
        safe_text,
    charactersWithSpaces=
        safe_text,
    characters=
        safe_text,
    presentationFormat=
        safe_text
)
SpreadsheetMLPrintingSetup::ErrorValue_strategy = st.builds(
    SpreadsheetMLPrintingSetup::ErrorValue,
)
SpreadsheetMLPrintingSetup::BooleanValue_strategy = st.builds(
    SpreadsheetMLPrintingSetup::BooleanValue,
    value=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
SpreadsheetMLPrintingSetup::DateTimeTypeValue_strategy = st.builds(
    SpreadsheetMLPrintingSetup::DateTimeTypeValue,
)
SpreadsheetMLPrintingSetup::DateTimeType_strategy = st.builds(
    SpreadsheetMLPrintingSetup::DateTimeType,
    month=
        safe_text,
    year=
        safe_text,
    minute=
        safe_text,
    hour=
        safe_text,
    second=
        safe_text,
    day=
        safe_text
)
SpreadsheetMLPrintingSetup::ValueType_strategy = st.builds(
    SpreadsheetMLPrintingSetup::ValueType,
)
SpreadsheetMLPrintingSetup::VersionType_strategy = st.builds(
    SpreadsheetMLPrintingSetup::VersionType,
    n=
        safe_text,
    nn=
        safe_text
)

@given(instance=SpreadsheetMLPrintingSetup::PageMarginsInfo_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::pagemarginsinfo_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::PageMarginsInfo)

@given(instance=SpreadsheetMLPrintingSetup::PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup::pagemarginsinfo_left_type(instance):
    assert isinstance(instance.left, str)


@given(instance=SpreadsheetMLPrintingSetup::PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup::pagemarginsinfo_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=SpreadsheetMLPrintingSetup::PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup::pagemarginsinfo_bottom_type(instance):
    assert isinstance(instance.bottom, str)


@given(instance=SpreadsheetMLPrintingSetup::PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup::pagemarginsinfo_bottom_setter(instance):
    original = instance.bottom
    instance.bottom = original
    assert instance.bottom == original

@given(instance=SpreadsheetMLPrintingSetup::PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup::pagemarginsinfo_right_type(instance):
    assert isinstance(instance.right, str)


@given(instance=SpreadsheetMLPrintingSetup::PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup::pagemarginsinfo_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=SpreadsheetMLPrintingSetup::PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup::pagemarginsinfo_top_type(instance):
    assert isinstance(instance.top, str)


@given(instance=SpreadsheetMLPrintingSetup::PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup::pagemarginsinfo_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::print_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Print)

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_leftToRight_type(instance):
    assert isinstance(instance.leftToRight, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_leftToRight_setter(instance):
    original = instance.leftToRight
    instance.leftToRight = original
    assert instance.leftToRight == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_printErrors_type(instance):
    assert isinstance(instance.printErrors, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_printErrors_setter(instance):
    original = instance.printErrors
    instance.printErrors = original
    assert instance.printErrors == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_draftQuality_type(instance):
    assert isinstance(instance.draftQuality, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_draftQuality_setter(instance):
    original = instance.draftQuality
    instance.draftQuality = original
    assert instance.draftQuality == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_commentsLayout_type(instance):
    assert isinstance(instance.commentsLayout, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_commentsLayout_setter(instance):
    original = instance.commentsLayout
    instance.commentsLayout = original
    assert instance.commentsLayout == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_blackAndWhite_type(instance):
    assert isinstance(instance.blackAndWhite, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_blackAndWhite_setter(instance):
    original = instance.blackAndWhite
    instance.blackAndWhite = original
    assert instance.blackAndWhite == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_paperSizeIndex_type(instance):
    assert isinstance(instance.paperSizeIndex, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_paperSizeIndex_setter(instance):
    original = instance.paperSizeIndex
    instance.paperSizeIndex = original
    assert instance.paperSizeIndex == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_fitHeight_type(instance):
    assert isinstance(instance.fitHeight, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_fitHeight_setter(instance):
    original = instance.fitHeight
    instance.fitHeight = original
    assert instance.fitHeight == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_scale_type(instance):
    assert isinstance(instance.scale, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_gridlines_type(instance):
    assert isinstance(instance.gridlines, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_gridlines_setter(instance):
    original = instance.gridlines
    instance.gridlines = original
    assert instance.gridlines == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_verticalResolution_type(instance):
    assert isinstance(instance.verticalResolution, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_verticalResolution_setter(instance):
    original = instance.verticalResolution
    instance.verticalResolution = original
    assert instance.verticalResolution == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_validPrinterInfo_type(instance):
    assert isinstance(instance.validPrinterInfo, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_validPrinterInfo_setter(instance):
    original = instance.validPrinterInfo
    instance.validPrinterInfo = original
    assert instance.validPrinterInfo == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_numberOfCopies_type(instance):
    assert isinstance(instance.numberOfCopies, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_numberOfCopies_setter(instance):
    original = instance.numberOfCopies
    instance.numberOfCopies = original
    assert instance.numberOfCopies == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_horizontalResolution_type(instance):
    assert isinstance(instance.horizontalResolution, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_horizontalResolution_setter(instance):
    original = instance.horizontalResolution
    instance.horizontalResolution = original
    assert instance.horizontalResolution == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_rowColHeadings_type(instance):
    assert isinstance(instance.rowColHeadings, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_rowColHeadings_setter(instance):
    original = instance.rowColHeadings
    instance.rowColHeadings = original
    assert instance.rowColHeadings == original

@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_fitWidth_type(instance):
    assert isinstance(instance.fitWidth, str)


@given(instance=SpreadsheetMLPrintingSetup::Print_strategy)
def test_spreadsheetmlprintingsetup::print_fitWidth_setter(instance):
    original = instance.fitWidth
    instance.fitWidth = original
    assert instance.fitWidth == original

@given(instance=HeaderOrFooterElt_strategy)
@settings(max_examples=50)
def test_headerorfooterelt_instantiation(instance):
    assert isinstance(instance, HeaderOrFooterElt)

@given(instance=SpreadsheetMLPrintingSetup::Header_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::header_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Header)

@given(instance=SpreadsheetMLPrintingSetup::HeaderOrFooterElt_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::headerorfooterelt_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::HeaderOrFooterElt)

@given(instance=SpreadsheetMLPrintingSetup::HeaderOrFooterElt_strategy)
def test_spreadsheetmlprintingsetup::headerorfooterelt_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=SpreadsheetMLPrintingSetup::HeaderOrFooterElt_strategy)
def test_spreadsheetmlprintingsetup::headerorfooterelt_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=SpreadsheetMLPrintingSetup::HeaderOrFooterElt_strategy)
def test_spreadsheetmlprintingsetup::headerorfooterelt_margin_type(instance):
    assert isinstance(instance.margin, str)


@given(instance=SpreadsheetMLPrintingSetup::HeaderOrFooterElt_strategy)
def test_spreadsheetmlprintingsetup::headerorfooterelt_margin_setter(instance):
    original = instance.margin
    instance.margin = original
    assert instance.margin == original

@given(instance=SpreadsheetMLPrintingSetup::Footer_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::footer_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Footer)

@given(instance=SpreadsheetMLPrintingSetup::Layout_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::layout_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Layout)

@given(instance=SpreadsheetMLPrintingSetup::Layout_strategy)
def test_spreadsheetmlprintingsetup::layout_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=SpreadsheetMLPrintingSetup::Layout_strategy)
def test_spreadsheetmlprintingsetup::layout_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=SpreadsheetMLPrintingSetup::Layout_strategy)
def test_spreadsheetmlprintingsetup::layout_centerVertical_type(instance):
    assert isinstance(instance.centerVertical, str)


@given(instance=SpreadsheetMLPrintingSetup::Layout_strategy)
def test_spreadsheetmlprintingsetup::layout_centerVertical_setter(instance):
    original = instance.centerVertical
    instance.centerVertical = original
    assert instance.centerVertical == original

@given(instance=SpreadsheetMLPrintingSetup::Layout_strategy)
def test_spreadsheetmlprintingsetup::layout_centerHorizontal_type(instance):
    assert isinstance(instance.centerHorizontal, str)


@given(instance=SpreadsheetMLPrintingSetup::Layout_strategy)
def test_spreadsheetmlprintingsetup::layout_centerHorizontal_setter(instance):
    original = instance.centerHorizontal
    instance.centerHorizontal = original
    assert instance.centerHorizontal == original

@given(instance=SpreadsheetMLPrintingSetup::Layout_strategy)
def test_spreadsheetmlprintingsetup::layout_startPageNumber_type(instance):
    assert isinstance(instance.startPageNumber, str)


@given(instance=SpreadsheetMLPrintingSetup::Layout_strategy)
def test_spreadsheetmlprintingsetup::layout_startPageNumber_setter(instance):
    original = instance.startPageNumber
    instance.startPageNumber = original
    assert instance.startPageNumber == original

@given(instance=PageMarginsInfo_strategy)
@settings(max_examples=50)
def test_pagemarginsinfo_instantiation(instance):
    assert isinstance(instance, PageMarginsInfo)

@given(instance=SpreadsheetMLPrintingSetup::PageSetup_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::pagesetup_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::PageSetup)

@given(instance=Footer_strategy)
@settings(max_examples=50)
def test_footer_instantiation(instance):
    assert isinstance(instance, Footer)

@given(instance=Header_strategy)
@settings(max_examples=50)
def test_header_instantiation(instance):
    assert isinstance(instance, Header)

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=PageSetup_strategy)
@settings(max_examples=50)
def test_pagesetup_instantiation(instance):
    assert isinstance(instance, PageSetup)

@given(instance=Print_strategy)
@settings(max_examples=50)
def test_print_instantiation(instance):
    assert isinstance(instance, Print)

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::WorksheetOptionsElt)

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_standardWidth_type(instance):
    assert isinstance(instance.standardWidth, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_standardWidth_setter(instance):
    original = instance.standardWidth
    instance.standardWidth = original
    assert instance.standardWidth == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayOutline_type(instance):
    assert isinstance(instance.doNotDisplayOutline, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayOutline_setter(instance):
    original = instance.doNotDisplayOutline
    instance.doNotDisplayOutline = original
    assert instance.doNotDisplayOutline == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowInsertCols_type(instance):
    assert isinstance(instance.allowInsertCols, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowInsertCols_setter(instance):
    original = instance.allowInsertCols
    instance.allowInsertCols = original
    assert instance.allowInsertCols == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_zoom_type(instance):
    assert isinstance(instance.zoom, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_enableSelection_type(instance):
    assert isinstance(instance.enableSelection, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_enableSelection_setter(instance):
    original = instance.enableSelection
    instance.enableSelection = original
    assert instance.enableSelection == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowDeleteCols_type(instance):
    assert isinstance(instance.allowDeleteCols, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowDeleteCols_setter(instance):
    original = instance.allowDeleteCols
    instance.allowDeleteCols = original
    assert instance.allowDeleteCols == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_transitionFormulaEntry_type(instance):
    assert isinstance(instance.transitionFormulaEntry, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_transitionFormulaEntry_setter(instance):
    original = instance.transitionFormulaEntry
    instance.transitionFormulaEntry = original
    assert instance.transitionFormulaEntry == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_fitToPage_type(instance):
    assert isinstance(instance.fitToPage, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_fitToPage_setter(instance):
    original = instance.fitToPage
    instance.fitToPage = original
    assert instance.fitToPage == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_splitVertical_type(instance):
    assert isinstance(instance.splitVertical, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_splitVertical_setter(instance):
    original = instance.splitVertical
    instance.splitVertical = original
    assert instance.splitVertical == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_noSummaryColumnsRightDetail_type(instance):
    assert isinstance(instance.noSummaryColumnsRightDetail, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_noSummaryColumnsRightDetail_setter(instance):
    original = instance.noSummaryColumnsRightDetail
    instance.noSummaryColumnsRightDetail = original
    assert instance.noSummaryColumnsRightDetail == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_displayFormulas_type(instance):
    assert isinstance(instance.displayFormulas, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_displayFormulas_setter(instance):
    original = instance.displayFormulas
    instance.displayFormulas = original
    assert instance.displayFormulas == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_rangeSelection_type(instance):
    assert isinstance(instance.rangeSelection, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_rangeSelection_setter(instance):
    original = instance.rangeSelection
    instance.rangeSelection = original
    assert instance.rangeSelection == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowSizeCols_type(instance):
    assert isinstance(instance.allowSizeCols, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowSizeCols_setter(instance):
    original = instance.allowSizeCols
    instance.allowSizeCols = original
    assert instance.allowSizeCols == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_gridlineColorIndex_type(instance):
    assert isinstance(instance.gridlineColorIndex, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_gridlineColorIndex_setter(instance):
    original = instance.gridlineColorIndex
    instance.gridlineColorIndex = original
    assert instance.gridlineColorIndex == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_protectObjects_type(instance):
    assert isinstance(instance.protectObjects, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_protectObjects_setter(instance):
    original = instance.protectObjects
    instance.protectObjects = original
    assert instance.protectObjects == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_gridlineColor_type(instance):
    assert isinstance(instance.gridlineColor, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_gridlineColor_setter(instance):
    original = instance.gridlineColor
    instance.gridlineColor = original
    assert instance.gridlineColor == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowFormatCells_type(instance):
    assert isinstance(instance.allowFormatCells, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowFormatCells_setter(instance):
    original = instance.allowFormatCells
    instance.allowFormatCells = original
    assert instance.allowFormatCells == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_excelWorksheetType_type(instance):
    assert isinstance(instance.excelWorksheetType, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_excelWorksheetType_setter(instance):
    original = instance.excelWorksheetType
    instance.excelWorksheetType = original
    assert instance.excelWorksheetType == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_protectContentst_type(instance):
    assert isinstance(instance.protectContentst, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_protectContentst_setter(instance):
    original = instance.protectContentst
    instance.protectContentst = original
    assert instance.protectContentst == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowSort_type(instance):
    assert isinstance(instance.allowSort, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowSort_setter(instance):
    original = instance.allowSort
    instance.allowSort = original
    assert instance.allowSort == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_displayRightToLeft_type(instance):
    assert isinstance(instance.displayRightToLeft, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_displayRightToLeft_setter(instance):
    original = instance.displayRightToLeft
    instance.displayRightToLeft = original
    assert instance.displayRightToLeft == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowFilter_type(instance):
    assert isinstance(instance.allowFilter, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowFilter_setter(instance):
    original = instance.allowFilter
    instance.allowFilter = original
    assert instance.allowFilter == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayColHeaders_type(instance):
    assert isinstance(instance.doNotDisplayColHeaders, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayColHeaders_setter(instance):
    original = instance.doNotDisplayColHeaders
    instance.doNotDisplayColHeaders = original
    assert instance.doNotDisplayColHeaders == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowSizeRows_type(instance):
    assert isinstance(instance.allowSizeRows, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowSizeRows_setter(instance):
    original = instance.allowSizeRows
    instance.allowSizeRows = original
    assert instance.allowSizeRows == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_topRowVisible_type(instance):
    assert isinstance(instance.topRowVisible, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_topRowVisible_setter(instance):
    original = instance.topRowVisible
    instance.topRowVisible = original
    assert instance.topRowVisible == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayZeros_type(instance):
    assert isinstance(instance.doNotDisplayZeros, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayZeros_setter(instance):
    original = instance.doNotDisplayZeros
    instance.doNotDisplayZeros = original
    assert instance.doNotDisplayZeros == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_filterOn_type(instance):
    assert isinstance(instance.filterOn, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_filterOn_setter(instance):
    original = instance.filterOn
    instance.filterOn = original
    assert instance.filterOn == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_defaultRowHeight_type(instance):
    assert isinstance(instance.defaultRowHeight, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_activePane_type(instance):
    assert isinstance(instance.activePane, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_activePane_setter(instance):
    original = instance.activePane
    instance.activePane = original
    assert instance.activePane == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_splitHorizontal_type(instance):
    assert isinstance(instance.splitHorizontal, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_splitHorizontal_setter(instance):
    original = instance.splitHorizontal
    instance.splitHorizontal = original
    assert instance.splitHorizontal == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowUsePivotTables_type(instance):
    assert isinstance(instance.allowUsePivotTables, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowUsePivotTables_setter(instance):
    original = instance.allowUsePivotTables
    instance.allowUsePivotTables = original
    assert instance.allowUsePivotTables == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_leftColumnVisible_type(instance):
    assert isinstance(instance.leftColumnVisible, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_leftColumnVisible_setter(instance):
    original = instance.leftColumnVisible
    instance.leftColumnVisible = original
    assert instance.leftColumnVisible == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_tabColorIndex_type(instance):
    assert isinstance(instance.tabColorIndex, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_tabColorIndex_setter(instance):
    original = instance.tabColorIndex
    instance.tabColorIndex = original
    assert instance.tabColorIndex == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_frozenNoSplit_type(instance):
    assert isinstance(instance.frozenNoSplit, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_frozenNoSplit_setter(instance):
    original = instance.frozenNoSplit
    instance.frozenNoSplit = original
    assert instance.frozenNoSplit == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_defaultColumnWidth_type(instance):
    assert isinstance(instance.defaultColumnWidth, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_freezePanes_type(instance):
    assert isinstance(instance.freezePanes, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_freezePanes_setter(instance):
    original = instance.freezePanes
    instance.freezePanes = original
    assert instance.freezePanes == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_unsynced_type(instance):
    assert isinstance(instance.unsynced, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_unsynced_setter(instance):
    original = instance.unsynced
    instance.unsynced = original
    assert instance.unsynced == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_visible_type(instance):
    assert isinstance(instance.visible, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayRowHeaders_type(instance):
    assert isinstance(instance.doNotDisplayRowHeaders, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayRowHeaders_setter(instance):
    original = instance.doNotDisplayRowHeaders
    instance.doNotDisplayRowHeaders = original
    assert instance.doNotDisplayRowHeaders == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_activeRow_type(instance):
    assert isinstance(instance.activeRow, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_activeRow_setter(instance):
    original = instance.activeRow
    instance.activeRow = original
    assert instance.activeRow == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowInsertHyperlinks_type(instance):
    assert isinstance(instance.allowInsertHyperlinks, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowInsertHyperlinks_setter(instance):
    original = instance.allowInsertHyperlinks
    instance.allowInsertHyperlinks = original
    assert instance.allowInsertHyperlinks == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_codeName_type(instance):
    assert isinstance(instance.codeName, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_codeName_setter(instance):
    original = instance.codeName
    instance.codeName = original
    assert instance.codeName == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayHeadings_type(instance):
    assert isinstance(instance.doNotDisplayHeadings, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayHeadings_setter(instance):
    original = instance.doNotDisplayHeadings
    instance.doNotDisplayHeadings = original
    assert instance.doNotDisplayHeadings == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_selected_type(instance):
    assert isinstance(instance.selected, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowDeleteRows_type(instance):
    assert isinstance(instance.allowDeleteRows, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowDeleteRows_setter(instance):
    original = instance.allowDeleteRows
    instance.allowDeleteRows = original
    assert instance.allowDeleteRows == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_intlMacro_type(instance):
    assert isinstance(instance.intlMacro, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_intlMacro_setter(instance):
    original = instance.intlMacro
    instance.intlMacro = original
    assert instance.intlMacro == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_leftColumnRightPane_type(instance):
    assert isinstance(instance.leftColumnRightPane, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_leftColumnRightPane_setter(instance):
    original = instance.leftColumnRightPane
    instance.leftColumnRightPane = original
    assert instance.leftColumnRightPane == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayGridlines_type(instance):
    assert isinstance(instance.doNotDisplayGridlines, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_doNotDisplayGridlines_setter(instance):
    original = instance.doNotDisplayGridlines
    instance.doNotDisplayGridlines = original
    assert instance.doNotDisplayGridlines == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_activeColumn_type(instance):
    assert isinstance(instance.activeColumn, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_activeColumn_setter(instance):
    original = instance.activeColumn
    instance.activeColumn = original
    assert instance.activeColumn == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_noSummaryRowsBelowDetail_type(instance):
    assert isinstance(instance.noSummaryRowsBelowDetail, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_noSummaryRowsBelowDetail_setter(instance):
    original = instance.noSummaryRowsBelowDetail
    instance.noSummaryRowsBelowDetail = original
    assert instance.noSummaryRowsBelowDetail == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_applyAutomaticOutlineStyles_type(instance):
    assert isinstance(instance.applyAutomaticOutlineStyles, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_applyAutomaticOutlineStyles_setter(instance):
    original = instance.applyAutomaticOutlineStyles
    instance.applyAutomaticOutlineStyles = original
    assert instance.applyAutomaticOutlineStyles == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_topRowBottomPane_type(instance):
    assert isinstance(instance.topRowBottomPane, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_topRowBottomPane_setter(instance):
    original = instance.topRowBottomPane
    instance.topRowBottomPane = original
    assert instance.topRowBottomPane == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_displayPageBreak_type(instance):
    assert isinstance(instance.displayPageBreak, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_displayPageBreak_setter(instance):
    original = instance.displayPageBreak
    instance.displayPageBreak = original
    assert instance.displayPageBreak == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_protectScenarios_type(instance):
    assert isinstance(instance.protectScenarios, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_protectScenarios_setter(instance):
    original = instance.protectScenarios
    instance.protectScenarios = original
    assert instance.protectScenarios == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowInsertRows_type(instance):
    assert isinstance(instance.allowInsertRows, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_allowInsertRows_setter(instance):
    original = instance.allowInsertRows
    instance.allowInsertRows = original
    assert instance.allowInsertRows == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_showPageBreakZoom_type(instance):
    assert isinstance(instance.showPageBreakZoom, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_showPageBreakZoom_setter(instance):
    original = instance.showPageBreakZoom
    instance.showPageBreakZoom = original
    assert instance.showPageBreakZoom == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_transitionExpressionEvaluation_type(instance):
    assert isinstance(instance.transitionExpressionEvaluation, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_transitionExpressionEvaluation_setter(instance):
    original = instance.transitionExpressionEvaluation
    instance.transitionExpressionEvaluation = original
    assert instance.transitionExpressionEvaluation == original

@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_pageBreakZoom_type(instance):
    assert isinstance(instance.pageBreakZoom, str)


@given(instance=SpreadsheetMLPrintingSetup::WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup::worksheetoptionselt_pageBreakZoom_setter(instance):
    original = instance.pageBreakZoom
    instance.pageBreakZoom = original
    assert instance.pageBreakZoom == original

@given(instance=SpreadsheetMLPrintingSetup::Data_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::data_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Data)

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::excelworkbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::ExcelWorkbook)

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_precisionAsDisplayed_type(instance):
    assert isinstance(instance.precisionAsDisplayed, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_precisionAsDisplayed_setter(instance):
    original = instance.precisionAsDisplayed
    instance.precisionAsDisplayed = original
    assert instance.precisionAsDisplayed == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_noAutoRecover_type(instance):
    assert isinstance(instance.noAutoRecover, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_noAutoRecover_setter(instance):
    original = instance.noAutoRecover
    instance.noAutoRecover = original
    assert instance.noAutoRecover == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_protectWindows_type(instance):
    assert isinstance(instance.protectWindows, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_protectWindows_setter(instance):
    original = instance.protectWindows
    instance.protectWindows = original
    assert instance.protectWindows == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_hideVerticalScrollBar_type(instance):
    assert isinstance(instance.hideVerticalScrollBar, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_hideVerticalScrollBar_setter(instance):
    original = instance.hideVerticalScrollBar
    instance.hideVerticalScrollBar = original
    assert instance.hideVerticalScrollBar == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_embedSaveSmartTags_type(instance):
    assert isinstance(instance.embedSaveSmartTags, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_embedSaveSmartTags_setter(instance):
    original = instance.embedSaveSmartTags
    instance.embedSaveSmartTags = original
    assert instance.embedSaveSmartTags == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_activeSheet_type(instance):
    assert isinstance(instance.activeSheet, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_activeSheet_setter(instance):
    original = instance.activeSheet
    instance.activeSheet = original
    assert instance.activeSheet == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowTopY_type(instance):
    assert isinstance(instance.windowTopY, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowTopY_setter(instance):
    original = instance.windowTopY
    instance.windowTopY = original
    assert instance.windowTopY == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowHeight_type(instance):
    assert isinstance(instance.windowHeight, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowHeight_setter(instance):
    original = instance.windowHeight
    instance.windowHeight = original
    assert instance.windowHeight == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_calculation_type(instance):
    assert isinstance(instance.calculation, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_calculation_setter(instance):
    original = instance.calculation
    instance.calculation = original
    assert instance.calculation == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_hideHorizontalScrollBar_type(instance):
    assert isinstance(instance.hideHorizontalScrollBar, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_hideHorizontalScrollBar_setter(instance):
    original = instance.hideHorizontalScrollBar
    instance.hideHorizontalScrollBar = original
    assert instance.hideHorizontalScrollBar == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_hidePivotTableFieldList_type(instance):
    assert isinstance(instance.hidePivotTableFieldList, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_hidePivotTableFieldList_setter(instance):
    original = instance.hidePivotTableFieldList
    instance.hidePivotTableFieldList = original
    assert instance.hidePivotTableFieldList == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_refModeR1C1_type(instance):
    assert isinstance(instance.refModeR1C1, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_refModeR1C1_setter(instance):
    original = instance.refModeR1C1
    instance.refModeR1C1 = original
    assert instance.refModeR1C1 == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_date1904_type(instance):
    assert isinstance(instance.date1904, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_date1904_setter(instance):
    original = instance.date1904
    instance.date1904 = original
    assert instance.date1904 == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_doNotCalculateBeforeSave_type(instance):
    assert isinstance(instance.doNotCalculateBeforeSave, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_doNotCalculateBeforeSave_setter(instance):
    original = instance.doNotCalculateBeforeSave
    instance.doNotCalculateBeforeSave = original
    assert instance.doNotCalculateBeforeSave == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_iteration_type(instance):
    assert isinstance(instance.iteration, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_iteration_setter(instance):
    original = instance.iteration
    instance.iteration = original
    assert instance.iteration == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowWidth_type(instance):
    assert isinstance(instance.windowWidth, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowWidth_setter(instance):
    original = instance.windowWidth
    instance.windowWidth = original
    assert instance.windowWidth == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_createBackup_type(instance):
    assert isinstance(instance.createBackup, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_createBackup_setter(instance):
    original = instance.createBackup
    instance.createBackup = original
    assert instance.createBackup == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_tabRatio_type(instance):
    assert isinstance(instance.tabRatio, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_tabRatio_setter(instance):
    original = instance.tabRatio
    instance.tabRatio = original
    assert instance.tabRatio == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowTopX_type(instance):
    assert isinstance(instance.windowTopX, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowTopX_setter(instance):
    original = instance.windowTopX
    instance.windowTopX = original
    assert instance.windowTopX == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_protectStructure_type(instance):
    assert isinstance(instance.protectStructure, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_protectStructure_setter(instance):
    original = instance.protectStructure
    instance.protectStructure = original
    assert instance.protectStructure == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowIconic_type(instance):
    assert isinstance(instance.windowIconic, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowIconic_setter(instance):
    original = instance.windowIconic
    instance.windowIconic = original
    assert instance.windowIconic == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_maxIterations_type(instance):
    assert isinstance(instance.maxIterations, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_maxIterations_setter(instance):
    original = instance.maxIterations
    instance.maxIterations = original
    assert instance.maxIterations == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_maxChange_type(instance):
    assert isinstance(instance.maxChange, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_maxChange_setter(instance):
    original = instance.maxChange
    instance.maxChange = original
    assert instance.maxChange == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_futureVer_type(instance):
    assert isinstance(instance.futureVer, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_futureVer_setter(instance):
    original = instance.futureVer
    instance.futureVer = original
    assert instance.futureVer == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_acceptLabelsInFormulas_type(instance):
    assert isinstance(instance.acceptLabelsInFormulas, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_acceptLabelsInFormulas_setter(instance):
    original = instance.acceptLabelsInFormulas
    instance.acceptLabelsInFormulas = original
    assert instance.acceptLabelsInFormulas == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_doNotSaveLinkValues_type(instance):
    assert isinstance(instance.doNotSaveLinkValues, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_doNotSaveLinkValues_setter(instance):
    original = instance.doNotSaveLinkValues
    instance.doNotSaveLinkValues = original
    assert instance.doNotSaveLinkValues == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_displayDrawingObjects_type(instance):
    assert isinstance(instance.displayDrawingObjects, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_displayDrawingObjects_setter(instance):
    original = instance.displayDrawingObjects
    instance.displayDrawingObjects = original
    assert instance.displayDrawingObjects == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_hideWorkbookTabs_type(instance):
    assert isinstance(instance.hideWorkbookTabs, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_hideWorkbookTabs_setter(instance):
    original = instance.hideWorkbookTabs
    instance.hideWorkbookTabs = original
    assert instance.hideWorkbookTabs == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_firstVisibleSheet_type(instance):
    assert isinstance(instance.firstVisibleSheet, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_firstVisibleSheet_setter(instance):
    original = instance.firstVisibleSheet
    instance.firstVisibleSheet = original
    assert instance.firstVisibleSheet == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowHidden_type(instance):
    assert isinstance(instance.windowHidden, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_windowHidden_setter(instance):
    original = instance.windowHidden
    instance.windowHidden = original
    assert instance.windowHidden == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_selectedSheets_type(instance):
    assert isinstance(instance.selectedSheets, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_selectedSheets_setter(instance):
    original = instance.selectedSheets
    instance.selectedSheets = original
    assert instance.selectedSheets == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_uncalced_type(instance):
    assert isinstance(instance.uncalced, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_uncalced_setter(instance):
    original = instance.uncalced
    instance.uncalced = original
    assert instance.uncalced == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_displayInkNotes_type(instance):
    assert isinstance(instance.displayInkNotes, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_displayInkNotes_setter(instance):
    original = instance.displayInkNotes
    instance.displayInkNotes = original
    assert instance.displayInkNotes == original

@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_activeChart_type(instance):
    assert isinstance(instance.activeChart, str)


@given(instance=SpreadsheetMLPrintingSetup::ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup::excelworkbook_activeChart_setter(instance):
    original = instance.activeChart
    instance.activeChart = original
    assert instance.activeChart == original

@given(instance=SpreadsheetMLPrintingSetup::Comment_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::comment_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Comment)

@given(instance=SpreadsheetMLPrintingSetup::Comment_strategy)
def test_spreadsheetmlprintingsetup::comment_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=SpreadsheetMLPrintingSetup::Comment_strategy)
def test_spreadsheetmlprintingsetup::comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=SpreadsheetMLPrintingSetup::Comment_strategy)
def test_spreadsheetmlprintingsetup::comment_showAlways_type(instance):
    assert isinstance(instance.showAlways, str)


@given(instance=SpreadsheetMLPrintingSetup::Comment_strategy)
def test_spreadsheetmlprintingsetup::comment_showAlways_setter(instance):
    original = instance.showAlways
    instance.showAlways = original
    assert instance.showAlways == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=ColOrRowElement_strategy)
@settings(max_examples=50)
def test_colorrowelement_instantiation(instance):
    assert isinstance(instance, ColOrRowElement)

@given(instance=SpreadsheetMLPrintingSetup::Row_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::row_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Row)

@given(instance=SpreadsheetMLPrintingSetup::Row_strategy)
def test_spreadsheetmlprintingsetup::row_autoFitHeight_type(instance):
    assert isinstance(instance.autoFitHeight, str)


@given(instance=SpreadsheetMLPrintingSetup::Row_strategy)
def test_spreadsheetmlprintingsetup::row_autoFitHeight_setter(instance):
    original = instance.autoFitHeight
    instance.autoFitHeight = original
    assert instance.autoFitHeight == original

@given(instance=SpreadsheetMLPrintingSetup::Row_strategy)
def test_spreadsheetmlprintingsetup::row_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=SpreadsheetMLPrintingSetup::Row_strategy)
def test_spreadsheetmlprintingsetup::row_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=SpreadsheetMLPrintingSetup::Column_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::column_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Column)

@given(instance=SpreadsheetMLPrintingSetup::Column_strategy)
def test_spreadsheetmlprintingsetup::column_autoFitWidth_type(instance):
    assert isinstance(instance.autoFitWidth, str)


@given(instance=SpreadsheetMLPrintingSetup::Column_strategy)
def test_spreadsheetmlprintingsetup::column_autoFitWidth_setter(instance):
    original = instance.autoFitWidth
    instance.autoFitWidth = original
    assert instance.autoFitWidth == original

@given(instance=SpreadsheetMLPrintingSetup::Column_strategy)
def test_spreadsheetmlprintingsetup::column_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=SpreadsheetMLPrintingSetup::Column_strategy)
def test_spreadsheetmlprintingsetup::column_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SpreadsheetMLPrintingSetup::Cell_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::cell_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Cell)

@given(instance=SpreadsheetMLPrintingSetup::Cell_strategy)
def test_spreadsheetmlprintingsetup::cell_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=SpreadsheetMLPrintingSetup::Cell_strategy)
def test_spreadsheetmlprintingsetup::cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=SpreadsheetMLPrintingSetup::Cell_strategy)
def test_spreadsheetmlprintingsetup::cell_hRef_type(instance):
    assert isinstance(instance.hRef, str)


@given(instance=SpreadsheetMLPrintingSetup::Cell_strategy)
def test_spreadsheetmlprintingsetup::cell_hRef_setter(instance):
    original = instance.hRef
    instance.hRef = original
    assert instance.hRef == original

@given(instance=SpreadsheetMLPrintingSetup::Cell_strategy)
def test_spreadsheetmlprintingsetup::cell_mergeDown_type(instance):
    assert isinstance(instance.mergeDown, str)


@given(instance=SpreadsheetMLPrintingSetup::Cell_strategy)
def test_spreadsheetmlprintingsetup::cell_mergeDown_setter(instance):
    original = instance.mergeDown
    instance.mergeDown = original
    assert instance.mergeDown == original

@given(instance=SpreadsheetMLPrintingSetup::Cell_strategy)
def test_spreadsheetmlprintingsetup::cell_mergeAcross_type(instance):
    assert isinstance(instance.mergeAcross, str)


@given(instance=SpreadsheetMLPrintingSetup::Cell_strategy)
def test_spreadsheetmlprintingsetup::cell_mergeAcross_setter(instance):
    original = instance.mergeAcross
    instance.mergeAcross = original
    assert instance.mergeAcross == original

@given(instance=SpreadsheetMLPrintingSetup::Cell_strategy)
def test_spreadsheetmlprintingsetup::cell_arrayRange_type(instance):
    assert isinstance(instance.arrayRange, str)


@given(instance=SpreadsheetMLPrintingSetup::Cell_strategy)
def test_spreadsheetmlprintingsetup::cell_arrayRange_setter(instance):
    original = instance.arrayRange
    instance.arrayRange = original
    assert instance.arrayRange == original

@given(instance=SpreadsheetMLPrintingSetup::ColOrRowElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::colorrowelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::ColOrRowElement)

@given(instance=SpreadsheetMLPrintingSetup::ColOrRowElement_strategy)
def test_spreadsheetmlprintingsetup::colorrowelement_hidden_type(instance):
    assert isinstance(instance.hidden, str)


@given(instance=SpreadsheetMLPrintingSetup::ColOrRowElement_strategy)
def test_spreadsheetmlprintingsetup::colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=SpreadsheetMLPrintingSetup::ColOrRowElement_strategy)
def test_spreadsheetmlprintingsetup::colorrowelement_span_type(instance):
    assert isinstance(instance.span, str)


@given(instance=SpreadsheetMLPrintingSetup::ColOrRowElement_strategy)
def test_spreadsheetmlprintingsetup::colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original

@given(instance=ExcelWorkbook_strategy)
@settings(max_examples=50)
def test_excelworkbook_instantiation(instance):
    assert isinstance(instance, ExcelWorkbook)

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

@given(instance=SpreadsheetMLPrintingSetup::TableElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::tableelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::TableElement)

@given(instance=SpreadsheetMLPrintingSetup::TableElement_strategy)
def test_spreadsheetmlprintingsetup::tableelement_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=SpreadsheetMLPrintingSetup::TableElement_strategy)
def test_spreadsheetmlprintingsetup::tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::table_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Table)

@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_leftCell_type(instance):
    assert isinstance(instance.leftCell, str)


@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_leftCell_setter(instance):
    original = instance.leftCell
    instance.leftCell = original
    assert instance.leftCell == original

@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_fullColumns_type(instance):
    assert isinstance(instance.fullColumns, str)


@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_fullColumns_setter(instance):
    original = instance.fullColumns
    instance.fullColumns = original
    assert instance.fullColumns == original

@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_expandedColumnCount_type(instance):
    assert isinstance(instance.expandedColumnCount, str)


@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_expandedColumnCount_setter(instance):
    original = instance.expandedColumnCount
    instance.expandedColumnCount = original
    assert instance.expandedColumnCount == original

@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_expandedRowCount_type(instance):
    assert isinstance(instance.expandedRowCount, str)


@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_expandedRowCount_setter(instance):
    original = instance.expandedRowCount
    instance.expandedRowCount = original
    assert instance.expandedRowCount == original

@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_defaultColumnWidth_type(instance):
    assert isinstance(instance.defaultColumnWidth, str)


@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original

@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_defaultRowHeight_type(instance):
    assert isinstance(instance.defaultRowHeight, str)


@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original

@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_fullRows_type(instance):
    assert isinstance(instance.fullRows, str)


@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_fullRows_setter(instance):
    original = instance.fullRows
    instance.fullRows = original
    assert instance.fullRows == original

@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_topCell_type(instance):
    assert isinstance(instance.topCell, str)


@given(instance=SpreadsheetMLPrintingSetup::Table_strategy)
def test_spreadsheetmlprintingsetup::table_topCell_setter(instance):
    original = instance.topCell
    instance.topCell = original
    assert instance.topCell == original

@given(instance=SpreadsheetMLPrintingSetup::StyledElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::styledelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::StyledElement)

@given(instance=WorksheetOptionsElt_strategy)
@settings(max_examples=50)
def test_worksheetoptionselt_instantiation(instance):
    assert isinstance(instance, WorksheetOptionsElt)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SpreadsheetMLPrintingSetup::Worksheet_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::worksheet_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Worksheet)

@given(instance=SpreadsheetMLPrintingSetup::Worksheet_strategy)
def test_spreadsheetmlprintingsetup::worksheet_protected_type(instance):
    assert isinstance(instance.protected, str)


@given(instance=SpreadsheetMLPrintingSetup::Worksheet_strategy)
def test_spreadsheetmlprintingsetup::worksheet_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=SpreadsheetMLPrintingSetup::Worksheet_strategy)
def test_spreadsheetmlprintingsetup::worksheet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLPrintingSetup::Worksheet_strategy)
def test_spreadsheetmlprintingsetup::worksheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLPrintingSetup::Worksheet_strategy)
def test_spreadsheetmlprintingsetup::worksheet_rightToLeft_type(instance):
    assert isinstance(instance.rightToLeft, str)


@given(instance=SpreadsheetMLPrintingSetup::Worksheet_strategy)
def test_spreadsheetmlprintingsetup::worksheet_rightToLeft_setter(instance):
    original = instance.rightToLeft
    instance.rightToLeft = original
    assert instance.rightToLeft == original

@given(instance=Worksheet_strategy)
@settings(max_examples=50)
def test_worksheet_instantiation(instance):
    assert isinstance(instance, Worksheet)

@given(instance=CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, CustomDocumentProperty)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=SpreadsheetMLPrintingSetup::Workbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::workbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::Workbook)

@given(instance=SmartTagType_strategy)
@settings(max_examples=50)
def test_smarttagtype_instantiation(instance):
    assert isinstance(instance, SmartTagType)

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)

@given(instance=SpreadsheetMLPrintingSetup::SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::smarttagscollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::SmartTagsCollection)

@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)

@given(instance=SpreadsheetMLPrintingSetup::SmartTagType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::smarttagtype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::SmartTagType)

@given(instance=SpreadsheetMLPrintingSetup::SmartTagType_strategy)
def test_spreadsheetmlprintingsetup::smarttagtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLPrintingSetup::SmartTagType_strategy)
def test_spreadsheetmlprintingsetup::smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLPrintingSetup::SmartTagType_strategy)
def test_spreadsheetmlprintingsetup::smarttagtype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=SpreadsheetMLPrintingSetup::SmartTagType_strategy)
def test_spreadsheetmlprintingsetup::smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=SpreadsheetMLPrintingSetup::SmartTagType_strategy)
def test_spreadsheetmlprintingsetup::smarttagtype_namespaceuri_type(instance):
    assert isinstance(instance.namespaceuri, str)


@given(instance=SpreadsheetMLPrintingSetup::SmartTagType_strategy)
def test_spreadsheetmlprintingsetup::smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=SpreadsheetMLPrintingSetup::CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::customdocumentproperty_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::CustomDocumentProperty)

@given(instance=SpreadsheetMLPrintingSetup::CustomDocumentProperty_strategy)
def test_spreadsheetmlprintingsetup::customdocumentproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SpreadsheetMLPrintingSetup::CustomDocumentProperty_strategy)
def test_spreadsheetmlprintingsetup::customdocumentproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLPrintingSetup::CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::CustomDocumentPropertiesCollection)

@given(instance=VersionType_strategy)
@settings(max_examples=50)
def test_versiontype_instantiation(instance):
    assert isinstance(instance, VersionType)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=SpreadsheetMLPrintingSetup::NumberValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::numbervalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::NumberValue)

@given(instance=SpreadsheetMLPrintingSetup::NumberValue_strategy)
def test_spreadsheetmlprintingsetup::numbervalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLPrintingSetup::NumberValue_strategy)
def test_spreadsheetmlprintingsetup::numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLPrintingSetup::StringValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::stringvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::StringValue)

@given(instance=SpreadsheetMLPrintingSetup::StringValue_strategy)
def test_spreadsheetmlprintingsetup::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLPrintingSetup::StringValue_strategy)
def test_spreadsheetmlprintingsetup::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=Workbook_strategy)
@settings(max_examples=50)
def test_workbook_instantiation(instance):
    assert isinstance(instance, Workbook)

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::DocumentPropertiesCollection)

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_paragraphs_type(instance):
    assert isinstance(instance.paragraphs, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_lines_type(instance):
    assert isinstance(instance.lines, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_hyperlinkBase_type(instance):
    assert isinstance(instance.hyperlinkBase, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_totalTime_type(instance):
    assert isinstance(instance.totalTime, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_lastAuthor_type(instance):
    assert isinstance(instance.lastAuthor, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_company_type(instance):
    assert isinstance(instance.company, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_manager_type(instance):
    assert isinstance(instance.manager, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_guid_type(instance):
    assert isinstance(instance.guid, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_words_type(instance):
    assert isinstance(instance.words, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_appName_type(instance):
    assert isinstance(instance.appName, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_revision_type(instance):
    assert isinstance(instance.revision, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_bytes_type(instance):
    assert isinstance(instance.bytes, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_subject_type(instance):
    assert isinstance(instance.subject, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_charactersWithSpaces_type(instance):
    assert isinstance(instance.charactersWithSpaces, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_characters_type(instance):
    assert isinstance(instance.characters, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original

@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_presentationFormat_type(instance):
    assert isinstance(instance.presentationFormat, str)


@given(instance=SpreadsheetMLPrintingSetup::DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup::documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original

@given(instance=SpreadsheetMLPrintingSetup::ErrorValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::errorvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::ErrorValue)

@given(instance=SpreadsheetMLPrintingSetup::BooleanValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::booleanvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::BooleanValue)

@given(instance=SpreadsheetMLPrintingSetup::BooleanValue_strategy)
def test_spreadsheetmlprintingsetup::booleanvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=SpreadsheetMLPrintingSetup::BooleanValue_strategy)
def test_spreadsheetmlprintingsetup::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=SpreadsheetMLPrintingSetup::DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::datetimetypevalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::DateTimeTypeValue)

@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::datetimetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::DateTimeType)

@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_minute_type(instance):
    assert isinstance(instance.minute, str)


@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_hour_type(instance):
    assert isinstance(instance.hour, str)


@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_second_type(instance):
    assert isinstance(instance.second, str)


@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=SpreadsheetMLPrintingSetup::DateTimeType_strategy)
def test_spreadsheetmlprintingsetup::datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=SpreadsheetMLPrintingSetup::ValueType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::valuetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::ValueType)

@given(instance=SpreadsheetMLPrintingSetup::VersionType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup::versiontype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup::VersionType)

@given(instance=SpreadsheetMLPrintingSetup::VersionType_strategy)
def test_spreadsheetmlprintingsetup::versiontype_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=SpreadsheetMLPrintingSetup::VersionType_strategy)
def test_spreadsheetmlprintingsetup::versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=SpreadsheetMLPrintingSetup::VersionType_strategy)
def test_spreadsheetmlprintingsetup::versiontype_nn_type(instance):
    assert isinstance(instance.nn, str)


@given(instance=SpreadsheetMLPrintingSetup::VersionType_strategy)
def test_spreadsheetmlprintingsetup::versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original
