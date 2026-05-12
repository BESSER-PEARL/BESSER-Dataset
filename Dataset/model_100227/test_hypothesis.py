import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SpreadsheetMLPrintingSetup_PageMarginsInfo,
    SpreadsheetMLPrintingSetup_Print,
    HeaderOrFooterElt,
    SpreadsheetMLPrintingSetup_Header,
    SpreadsheetMLPrintingSetup_HeaderOrFooterElt,
    SpreadsheetMLPrintingSetup_Footer,
    SpreadsheetMLPrintingSetup_Layout,
    PageMarginsInfo,
    SpreadsheetMLPrintingSetup_PageSetup,
    Footer,
    Header,
    Layout,
    PageSetup,
    Print,
    SpreadsheetMLPrintingSetup_WorksheetOptionsElt,
    SpreadsheetMLPrintingSetup_Data,
    SpreadsheetMLPrintingSetup_ExcelWorkbook,
    SpreadsheetMLPrintingSetup_Comment,
    Comment,
    ColOrRowElement,
    SpreadsheetMLPrintingSetup_Row,
    SpreadsheetMLPrintingSetup_Column,
    TableElement,
    SpreadsheetMLPrintingSetup_Cell,
    SpreadsheetMLPrintingSetup_ColOrRowElement,
    ExcelWorkbook,
    Row,
    Column,
    StyledElement,
    SpreadsheetMLPrintingSetup_TableElement,
    SpreadsheetMLPrintingSetup_Table,
    SpreadsheetMLPrintingSetup_StyledElement,
    WorksheetOptionsElt,
    Table,
    SpreadsheetMLPrintingSetup_Worksheet,
    Worksheet,
    CustomDocumentProperty,
    DocumentPropertiesCollection,
    SpreadsheetMLPrintingSetup_Workbook,
    SmartTagType,
    Cell,
    SpreadsheetMLPrintingSetup_SmartTagsCollection,
    SmartTagsCollection,
    SpreadsheetMLPrintingSetup_SmartTagType,
    CustomDocumentPropertiesCollection,
    SpreadsheetMLPrintingSetup_CustomDocumentProperty,
    SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection,
    VersionType,
    ValueType,
    SpreadsheetMLPrintingSetup_NumberValue,
    SpreadsheetMLPrintingSetup_StringValue,
    Data,
    Workbook,
    SpreadsheetMLPrintingSetup_DocumentPropertiesCollection,
    SpreadsheetMLPrintingSetup_ErrorValue,
    SpreadsheetMLPrintingSetup_BooleanValue,
    DateTimeType,
    SpreadsheetMLPrintingSetup_DateTimeTypeValue,
    SpreadsheetMLPrintingSetup_DateTimeType,
    SpreadsheetMLPrintingSetup_ValueType,
    SpreadsheetMLPrintingSetup_VersionType,
    CommentsLayoutType,
    OrientationType,
    DisplayDrawingObjectsType,
    EnableSelectionType,
    CalculationWorkbookType,
    ExcelWorksheetTypeType,
    VisibleType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheetmlprintingsetup_pagemarginsinfo_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_PageMarginsInfo)


def test_spreadsheetmlprintingsetup_pagemarginsinfo_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_PageMarginsInfo.__init__)


def test_spreadsheetmlprintingsetup_pagemarginsinfo_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_PageMarginsInfo.__init__)
    params = list(sig.parameters.keys())
    assert "bottom" in params, "Missing parameter 'bottom'"
    assert "right" in params, "Missing parameter 'right'"
    assert "top" in params, "Missing parameter 'top'"
    assert "left" in params, "Missing parameter 'left'"

def test_spreadsheetmlprintingsetup_pagemarginsinfo_has_bottom():
    assert hasattr(SpreadsheetMLPrintingSetup_PageMarginsInfo, "bottom")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_PageMarginsInfo.__mro__:
        if "bottom" in klass.__dict__:
            descriptor = klass.__dict__["bottom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_pagemarginsinfo_has_right():
    assert hasattr(SpreadsheetMLPrintingSetup_PageMarginsInfo, "right")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_PageMarginsInfo.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_pagemarginsinfo_has_top():
    assert hasattr(SpreadsheetMLPrintingSetup_PageMarginsInfo, "top")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_PageMarginsInfo.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_pagemarginsinfo_has_left():
    assert hasattr(SpreadsheetMLPrintingSetup_PageMarginsInfo, "left")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_PageMarginsInfo.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_print_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Print)


def test_spreadsheetmlprintingsetup_print_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Print.__init__)


def test_spreadsheetmlprintingsetup_print_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Print.__init__)
    params = list(sig.parameters.keys())
    assert "paperSizeIndex" in params, "Missing parameter 'paperSizeIndex'"
    assert "verticalResolution" in params, "Missing parameter 'verticalResolution'"
    assert "gridlines" in params, "Missing parameter 'gridlines'"
    assert "validPrinterInfo" in params, "Missing parameter 'validPrinterInfo'"
    assert "leftToRight" in params, "Missing parameter 'leftToRight'"
    assert "numberOfCopies" in params, "Missing parameter 'numberOfCopies'"
    assert "fitWidth" in params, "Missing parameter 'fitWidth'"
    assert "blackAndWhite" in params, "Missing parameter 'blackAndWhite'"
    assert "commentsLayout" in params, "Missing parameter 'commentsLayout'"
    assert "rowColHeadings" in params, "Missing parameter 'rowColHeadings'"
    assert "printErrors" in params, "Missing parameter 'printErrors'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "fitHeight" in params, "Missing parameter 'fitHeight'"
    assert "draftQuality" in params, "Missing parameter 'draftQuality'"
    assert "horizontalResolution" in params, "Missing parameter 'horizontalResolution'"

def test_spreadsheetmlprintingsetup_print_has_paperSizeIndex():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "paperSizeIndex")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "paperSizeIndex" in klass.__dict__:
            descriptor = klass.__dict__["paperSizeIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_verticalResolution():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "verticalResolution")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "verticalResolution" in klass.__dict__:
            descriptor = klass.__dict__["verticalResolution"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_gridlines():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "gridlines")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "gridlines" in klass.__dict__:
            descriptor = klass.__dict__["gridlines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_validPrinterInfo():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "validPrinterInfo")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "validPrinterInfo" in klass.__dict__:
            descriptor = klass.__dict__["validPrinterInfo"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_leftToRight():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "leftToRight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "leftToRight" in klass.__dict__:
            descriptor = klass.__dict__["leftToRight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_numberOfCopies():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "numberOfCopies")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "numberOfCopies" in klass.__dict__:
            descriptor = klass.__dict__["numberOfCopies"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_fitWidth():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "fitWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "fitWidth" in klass.__dict__:
            descriptor = klass.__dict__["fitWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_blackAndWhite():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "blackAndWhite")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "blackAndWhite" in klass.__dict__:
            descriptor = klass.__dict__["blackAndWhite"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_commentsLayout():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "commentsLayout")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "commentsLayout" in klass.__dict__:
            descriptor = klass.__dict__["commentsLayout"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_rowColHeadings():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "rowColHeadings")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "rowColHeadings" in klass.__dict__:
            descriptor = klass.__dict__["rowColHeadings"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_printErrors():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "printErrors")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "printErrors" in klass.__dict__:
            descriptor = klass.__dict__["printErrors"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_scale():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "scale")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_fitHeight():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "fitHeight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "fitHeight" in klass.__dict__:
            descriptor = klass.__dict__["fitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_draftQuality():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "draftQuality")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "draftQuality" in klass.__dict__:
            descriptor = klass.__dict__["draftQuality"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_print_has_horizontalResolution():
    assert hasattr(SpreadsheetMLPrintingSetup_Print, "horizontalResolution")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Print.__mro__:
        if "horizontalResolution" in klass.__dict__:
            descriptor = klass.__dict__["horizontalResolution"]
            break
    assert isinstance(descriptor, property)



def test_headerorfooterelt_is_not_abstract():
    assert not inspect.isabstract(HeaderOrFooterElt)


def test_headerorfooterelt_constructor_exists():
    assert callable(HeaderOrFooterElt.__init__)


def test_headerorfooterelt_constructor_args():
    sig = inspect.signature(HeaderOrFooterElt.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup_header_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Header)


def test_spreadsheetmlprintingsetup_header_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Header.__init__)


def test_spreadsheetmlprintingsetup_header_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Header.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup_headerorfooterelt_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_HeaderOrFooterElt)


def test_spreadsheetmlprintingsetup_headerorfooterelt_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_HeaderOrFooterElt.__init__)


def test_spreadsheetmlprintingsetup_headerorfooterelt_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_HeaderOrFooterElt.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "margin" in params, "Missing parameter 'margin'"

def test_spreadsheetmlprintingsetup_headerorfooterelt_has_data():
    assert hasattr(SpreadsheetMLPrintingSetup_HeaderOrFooterElt, "data")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_HeaderOrFooterElt.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_headerorfooterelt_has_margin():
    assert hasattr(SpreadsheetMLPrintingSetup_HeaderOrFooterElt, "margin")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_HeaderOrFooterElt.__mro__:
        if "margin" in klass.__dict__:
            descriptor = klass.__dict__["margin"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_footer_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Footer)


def test_spreadsheetmlprintingsetup_footer_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Footer.__init__)


def test_spreadsheetmlprintingsetup_footer_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Footer.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup_layout_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Layout)


def test_spreadsheetmlprintingsetup_layout_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Layout.__init__)


def test_spreadsheetmlprintingsetup_layout_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Layout.__init__)
    params = list(sig.parameters.keys())
    assert "centerHorizontal" in params, "Missing parameter 'centerHorizontal'"
    assert "centerVertical" in params, "Missing parameter 'centerVertical'"
    assert "startPageNumber" in params, "Missing parameter 'startPageNumber'"
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_spreadsheetmlprintingsetup_layout_has_centerHorizontal():
    assert hasattr(SpreadsheetMLPrintingSetup_Layout, "centerHorizontal")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Layout.__mro__:
        if "centerHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["centerHorizontal"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_layout_has_centerVertical():
    assert hasattr(SpreadsheetMLPrintingSetup_Layout, "centerVertical")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Layout.__mro__:
        if "centerVertical" in klass.__dict__:
            descriptor = klass.__dict__["centerVertical"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_layout_has_startPageNumber():
    assert hasattr(SpreadsheetMLPrintingSetup_Layout, "startPageNumber")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Layout.__mro__:
        if "startPageNumber" in klass.__dict__:
            descriptor = klass.__dict__["startPageNumber"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_layout_has_orientation():
    assert hasattr(SpreadsheetMLPrintingSetup_Layout, "orientation")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Layout.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_pagemarginsinfo_is_not_abstract():
    assert not inspect.isabstract(PageMarginsInfo)


def test_pagemarginsinfo_constructor_exists():
    assert callable(PageMarginsInfo.__init__)


def test_pagemarginsinfo_constructor_args():
    sig = inspect.signature(PageMarginsInfo.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup_pagesetup_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_PageSetup)


def test_spreadsheetmlprintingsetup_pagesetup_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_PageSetup.__init__)


def test_spreadsheetmlprintingsetup_pagesetup_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_PageSetup.__init__)
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



def test_spreadsheetmlprintingsetup_worksheetoptionselt_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_WorksheetOptionsElt)


def test_spreadsheetmlprintingsetup_worksheetoptionselt_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__init__)


def test_spreadsheetmlprintingsetup_worksheetoptionselt_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__init__)
    params = list(sig.parameters.keys())
    assert "selected" in params, "Missing parameter 'selected'"
    assert "protectObjects" in params, "Missing parameter 'protectObjects'"
    assert "allowDeleteRows" in params, "Missing parameter 'allowDeleteRows'"
    assert "allowSizeRows" in params, "Missing parameter 'allowSizeRows'"
    assert "displayRightToLeft" in params, "Missing parameter 'displayRightToLeft'"
    assert "displayPageBreak" in params, "Missing parameter 'displayPageBreak'"
    assert "transitionExpressionEvaluation" in params, "Missing parameter 'transitionExpressionEvaluation'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"
    assert "standardWidth" in params, "Missing parameter 'standardWidth'"
    assert "showPageBreakZoom" in params, "Missing parameter 'showPageBreakZoom'"
    assert "allowInsertHyperlinks" in params, "Missing parameter 'allowInsertHyperlinks'"
    assert "allowSizeCols" in params, "Missing parameter 'allowSizeCols'"
    assert "gridlineColor" in params, "Missing parameter 'gridlineColor'"
    assert "enableSelection" in params, "Missing parameter 'enableSelection'"
    assert "protectContentst" in params, "Missing parameter 'protectContentst'"
    assert "topRowVisible" in params, "Missing parameter 'topRowVisible'"
    assert "activePane" in params, "Missing parameter 'activePane'"
    assert "freezePanes" in params, "Missing parameter 'freezePanes'"
    assert "rangeSelection" in params, "Missing parameter 'rangeSelection'"
    assert "intlMacro" in params, "Missing parameter 'intlMacro'"
    assert "unsynced" in params, "Missing parameter 'unsynced'"
    assert "activeColumn" in params, "Missing parameter 'activeColumn'"
    assert "frozenNoSplit" in params, "Missing parameter 'frozenNoSplit'"
    assert "allowInsertCols" in params, "Missing parameter 'allowInsertCols'"
    assert "protectScenarios" in params, "Missing parameter 'protectScenarios'"
    assert "codeName" in params, "Missing parameter 'codeName'"
    assert "pageBreakZoom" in params, "Missing parameter 'pageBreakZoom'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "displayFormulas" in params, "Missing parameter 'displayFormulas'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "gridlineColorIndex" in params, "Missing parameter 'gridlineColorIndex'"
    assert "doNotDisplayColHeaders" in params, "Missing parameter 'doNotDisplayColHeaders'"
    assert "noSummaryRowsBelowDetail" in params, "Missing parameter 'noSummaryRowsBelowDetail'"
    assert "doNotDisplayGridlines" in params, "Missing parameter 'doNotDisplayGridlines'"
    assert "transitionFormulaEntry" in params, "Missing parameter 'transitionFormulaEntry'"
    assert "doNotDisplayZeros" in params, "Missing parameter 'doNotDisplayZeros'"
    assert "allowFormatCells" in params, "Missing parameter 'allowFormatCells'"
    assert "activeRow" in params, "Missing parameter 'activeRow'"
    assert "tabColorIndex" in params, "Missing parameter 'tabColorIndex'"
    assert "applyAutomaticOutlineStyles" in params, "Missing parameter 'applyAutomaticOutlineStyles'"
    assert "fitToPage" in params, "Missing parameter 'fitToPage'"
    assert "doNotDisplayHeadings" in params, "Missing parameter 'doNotDisplayHeadings'"
    assert "zoom" in params, "Missing parameter 'zoom'"
    assert "allowFilter" in params, "Missing parameter 'allowFilter'"
    assert "doNotDisplayOutline" in params, "Missing parameter 'doNotDisplayOutline'"
    assert "name" in params, "Missing parameter 'name'"
    assert "filterOn" in params, "Missing parameter 'filterOn'"
    assert "noSummaryColumnsRightDetail" in params, "Missing parameter 'noSummaryColumnsRightDetail'"
    assert "allowUsePivotTables" in params, "Missing parameter 'allowUsePivotTables'"
    assert "allowSort" in params, "Missing parameter 'allowSort'"
    assert "topRowBottomPane" in params, "Missing parameter 'topRowBottomPane'"
    assert "leftColumnRightPane" in params, "Missing parameter 'leftColumnRightPane'"
    assert "excelWorksheetType" in params, "Missing parameter 'excelWorksheetType'"
    assert "splitHorizontal" in params, "Missing parameter 'splitHorizontal'"
    assert "leftColumnVisible" in params, "Missing parameter 'leftColumnVisible'"
    assert "allowDeleteCols" in params, "Missing parameter 'allowDeleteCols'"
    assert "allowInsertRows" in params, "Missing parameter 'allowInsertRows'"
    assert "splitVertical" in params, "Missing parameter 'splitVertical'"
    assert "doNotDisplayRowHeaders" in params, "Missing parameter 'doNotDisplayRowHeaders'"

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_selected():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "selected")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_protectObjects():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "protectObjects")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "protectObjects" in klass.__dict__:
            descriptor = klass.__dict__["protectObjects"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_allowDeleteRows():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "allowDeleteRows")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "allowDeleteRows" in klass.__dict__:
            descriptor = klass.__dict__["allowDeleteRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_allowSizeRows():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "allowSizeRows")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "allowSizeRows" in klass.__dict__:
            descriptor = klass.__dict__["allowSizeRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_displayRightToLeft():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "displayRightToLeft")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "displayRightToLeft" in klass.__dict__:
            descriptor = klass.__dict__["displayRightToLeft"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_displayPageBreak():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "displayPageBreak")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "displayPageBreak" in klass.__dict__:
            descriptor = klass.__dict__["displayPageBreak"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_transitionExpressionEvaluation():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "transitionExpressionEvaluation")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "transitionExpressionEvaluation" in klass.__dict__:
            descriptor = klass.__dict__["transitionExpressionEvaluation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_standardWidth():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "standardWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "standardWidth" in klass.__dict__:
            descriptor = klass.__dict__["standardWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_showPageBreakZoom():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "showPageBreakZoom")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "showPageBreakZoom" in klass.__dict__:
            descriptor = klass.__dict__["showPageBreakZoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_allowInsertHyperlinks():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "allowInsertHyperlinks")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "allowInsertHyperlinks" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertHyperlinks"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_allowSizeCols():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "allowSizeCols")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "allowSizeCols" in klass.__dict__:
            descriptor = klass.__dict__["allowSizeCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_gridlineColor():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "gridlineColor")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "gridlineColor" in klass.__dict__:
            descriptor = klass.__dict__["gridlineColor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_enableSelection():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "enableSelection")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "enableSelection" in klass.__dict__:
            descriptor = klass.__dict__["enableSelection"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_protectContentst():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "protectContentst")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "protectContentst" in klass.__dict__:
            descriptor = klass.__dict__["protectContentst"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_topRowVisible():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "topRowVisible")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "topRowVisible" in klass.__dict__:
            descriptor = klass.__dict__["topRowVisible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_activePane():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "activePane")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "activePane" in klass.__dict__:
            descriptor = klass.__dict__["activePane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_freezePanes():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "freezePanes")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "freezePanes" in klass.__dict__:
            descriptor = klass.__dict__["freezePanes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_rangeSelection():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "rangeSelection")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "rangeSelection" in klass.__dict__:
            descriptor = klass.__dict__["rangeSelection"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_intlMacro():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "intlMacro")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "intlMacro" in klass.__dict__:
            descriptor = klass.__dict__["intlMacro"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_unsynced():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "unsynced")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "unsynced" in klass.__dict__:
            descriptor = klass.__dict__["unsynced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_activeColumn():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "activeColumn")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "activeColumn" in klass.__dict__:
            descriptor = klass.__dict__["activeColumn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_frozenNoSplit():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "frozenNoSplit")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "frozenNoSplit" in klass.__dict__:
            descriptor = klass.__dict__["frozenNoSplit"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_allowInsertCols():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "allowInsertCols")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "allowInsertCols" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_protectScenarios():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "protectScenarios")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "protectScenarios" in klass.__dict__:
            descriptor = klass.__dict__["protectScenarios"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_codeName():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "codeName")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "codeName" in klass.__dict__:
            descriptor = klass.__dict__["codeName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_pageBreakZoom():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "pageBreakZoom")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "pageBreakZoom" in klass.__dict__:
            descriptor = klass.__dict__["pageBreakZoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_visible():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "visible")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_displayFormulas():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "displayFormulas")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "displayFormulas" in klass.__dict__:
            descriptor = klass.__dict__["displayFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_gridlineColorIndex():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "gridlineColorIndex")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "gridlineColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["gridlineColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_doNotDisplayColHeaders():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "doNotDisplayColHeaders")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "doNotDisplayColHeaders" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayColHeaders"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_noSummaryRowsBelowDetail():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "noSummaryRowsBelowDetail")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "noSummaryRowsBelowDetail" in klass.__dict__:
            descriptor = klass.__dict__["noSummaryRowsBelowDetail"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_doNotDisplayGridlines():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "doNotDisplayGridlines")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "doNotDisplayGridlines" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayGridlines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_transitionFormulaEntry():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "transitionFormulaEntry")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "transitionFormulaEntry" in klass.__dict__:
            descriptor = klass.__dict__["transitionFormulaEntry"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_doNotDisplayZeros():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "doNotDisplayZeros")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "doNotDisplayZeros" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayZeros"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_allowFormatCells():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "allowFormatCells")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "allowFormatCells" in klass.__dict__:
            descriptor = klass.__dict__["allowFormatCells"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_activeRow():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "activeRow")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "activeRow" in klass.__dict__:
            descriptor = klass.__dict__["activeRow"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_tabColorIndex():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "tabColorIndex")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "tabColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["tabColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_applyAutomaticOutlineStyles():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "applyAutomaticOutlineStyles")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "applyAutomaticOutlineStyles" in klass.__dict__:
            descriptor = klass.__dict__["applyAutomaticOutlineStyles"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_fitToPage():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "fitToPage")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "fitToPage" in klass.__dict__:
            descriptor = klass.__dict__["fitToPage"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_doNotDisplayHeadings():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "doNotDisplayHeadings")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "doNotDisplayHeadings" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayHeadings"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_zoom():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "zoom")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_allowFilter():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "allowFilter")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "allowFilter" in klass.__dict__:
            descriptor = klass.__dict__["allowFilter"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_doNotDisplayOutline():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "doNotDisplayOutline")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "doNotDisplayOutline" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayOutline"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_name():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "name")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_filterOn():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "filterOn")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "filterOn" in klass.__dict__:
            descriptor = klass.__dict__["filterOn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_noSummaryColumnsRightDetail():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "noSummaryColumnsRightDetail")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "noSummaryColumnsRightDetail" in klass.__dict__:
            descriptor = klass.__dict__["noSummaryColumnsRightDetail"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_allowUsePivotTables():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "allowUsePivotTables")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "allowUsePivotTables" in klass.__dict__:
            descriptor = klass.__dict__["allowUsePivotTables"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_allowSort():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "allowSort")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "allowSort" in klass.__dict__:
            descriptor = klass.__dict__["allowSort"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_topRowBottomPane():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "topRowBottomPane")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "topRowBottomPane" in klass.__dict__:
            descriptor = klass.__dict__["topRowBottomPane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_leftColumnRightPane():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "leftColumnRightPane")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "leftColumnRightPane" in klass.__dict__:
            descriptor = klass.__dict__["leftColumnRightPane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_excelWorksheetType():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "excelWorksheetType")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "excelWorksheetType" in klass.__dict__:
            descriptor = klass.__dict__["excelWorksheetType"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_splitHorizontal():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "splitHorizontal")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "splitHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["splitHorizontal"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_leftColumnVisible():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "leftColumnVisible")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "leftColumnVisible" in klass.__dict__:
            descriptor = klass.__dict__["leftColumnVisible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_allowDeleteCols():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "allowDeleteCols")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "allowDeleteCols" in klass.__dict__:
            descriptor = klass.__dict__["allowDeleteCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_allowInsertRows():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "allowInsertRows")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "allowInsertRows" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_splitVertical():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "splitVertical")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "splitVertical" in klass.__dict__:
            descriptor = klass.__dict__["splitVertical"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheetoptionselt_has_doNotDisplayRowHeaders():
    assert hasattr(SpreadsheetMLPrintingSetup_WorksheetOptionsElt, "doNotDisplayRowHeaders")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_WorksheetOptionsElt.__mro__:
        if "doNotDisplayRowHeaders" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayRowHeaders"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_data_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Data)


def test_spreadsheetmlprintingsetup_data_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Data.__init__)


def test_spreadsheetmlprintingsetup_data_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Data.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup_excelworkbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_ExcelWorkbook)


def test_spreadsheetmlprintingsetup_excelworkbook_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_ExcelWorkbook.__init__)


def test_spreadsheetmlprintingsetup_excelworkbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_ExcelWorkbook.__init__)
    params = list(sig.parameters.keys())
    assert "displayInkNotes" in params, "Missing parameter 'displayInkNotes'"
    assert "tabRatio" in params, "Missing parameter 'tabRatio'"
    assert "date1904" in params, "Missing parameter 'date1904'"
    assert "windowHeight" in params, "Missing parameter 'windowHeight'"
    assert "refModeR1C1" in params, "Missing parameter 'refModeR1C1'"
    assert "activeSheet" in params, "Missing parameter 'activeSheet'"
    assert "selectedSheets" in params, "Missing parameter 'selectedSheets'"
    assert "protectStructure" in params, "Missing parameter 'protectStructure'"
    assert "displayDrawingObjects" in params, "Missing parameter 'displayDrawingObjects'"
    assert "doNotSaveLinkValues" in params, "Missing parameter 'doNotSaveLinkValues'"
    assert "windowIconic" in params, "Missing parameter 'windowIconic'"
    assert "embedSaveSmartTags" in params, "Missing parameter 'embedSaveSmartTags'"
    assert "firstVisibleSheet" in params, "Missing parameter 'firstVisibleSheet'"
    assert "protectWindows" in params, "Missing parameter 'protectWindows'"
    assert "precisionAsDisplayed" in params, "Missing parameter 'precisionAsDisplayed'"
    assert "maxIterations" in params, "Missing parameter 'maxIterations'"
    assert "windowTopX" in params, "Missing parameter 'windowTopX'"
    assert "windowTopY" in params, "Missing parameter 'windowTopY'"
    assert "doNotCalculateBeforeSave" in params, "Missing parameter 'doNotCalculateBeforeSave'"
    assert "iteration" in params, "Missing parameter 'iteration'"
    assert "acceptLabelsInFormulas" in params, "Missing parameter 'acceptLabelsInFormulas'"
    assert "windowHidden" in params, "Missing parameter 'windowHidden'"
    assert "hideHorizontalScrollBar" in params, "Missing parameter 'hideHorizontalScrollBar'"
    assert "noAutoRecover" in params, "Missing parameter 'noAutoRecover'"
    assert "hidePivotTableFieldList" in params, "Missing parameter 'hidePivotTableFieldList'"
    assert "hideVerticalScrollBar" in params, "Missing parameter 'hideVerticalScrollBar'"
    assert "createBackup" in params, "Missing parameter 'createBackup'"
    assert "calculation" in params, "Missing parameter 'calculation'"
    assert "futureVer" in params, "Missing parameter 'futureVer'"
    assert "windowWidth" in params, "Missing parameter 'windowWidth'"
    assert "hideWorkbookTabs" in params, "Missing parameter 'hideWorkbookTabs'"
    assert "maxChange" in params, "Missing parameter 'maxChange'"
    assert "uncalced" in params, "Missing parameter 'uncalced'"
    assert "activeChart" in params, "Missing parameter 'activeChart'"

def test_spreadsheetmlprintingsetup_excelworkbook_has_displayInkNotes():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "displayInkNotes")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "displayInkNotes" in klass.__dict__:
            descriptor = klass.__dict__["displayInkNotes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_tabRatio():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "tabRatio")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "tabRatio" in klass.__dict__:
            descriptor = klass.__dict__["tabRatio"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_date1904():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "date1904")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "date1904" in klass.__dict__:
            descriptor = klass.__dict__["date1904"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_windowHeight():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "windowHeight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "windowHeight" in klass.__dict__:
            descriptor = klass.__dict__["windowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_refModeR1C1():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "refModeR1C1")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "refModeR1C1" in klass.__dict__:
            descriptor = klass.__dict__["refModeR1C1"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_activeSheet():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "activeSheet")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "activeSheet" in klass.__dict__:
            descriptor = klass.__dict__["activeSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_selectedSheets():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "selectedSheets")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "selectedSheets" in klass.__dict__:
            descriptor = klass.__dict__["selectedSheets"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_protectStructure():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "protectStructure")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "protectStructure" in klass.__dict__:
            descriptor = klass.__dict__["protectStructure"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_displayDrawingObjects():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "displayDrawingObjects")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "displayDrawingObjects" in klass.__dict__:
            descriptor = klass.__dict__["displayDrawingObjects"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_doNotSaveLinkValues():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "doNotSaveLinkValues")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "doNotSaveLinkValues" in klass.__dict__:
            descriptor = klass.__dict__["doNotSaveLinkValues"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_windowIconic():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "windowIconic")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "windowIconic" in klass.__dict__:
            descriptor = klass.__dict__["windowIconic"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_embedSaveSmartTags():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "embedSaveSmartTags")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "embedSaveSmartTags" in klass.__dict__:
            descriptor = klass.__dict__["embedSaveSmartTags"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_firstVisibleSheet():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "firstVisibleSheet")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "firstVisibleSheet" in klass.__dict__:
            descriptor = klass.__dict__["firstVisibleSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_protectWindows():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "protectWindows")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "protectWindows" in klass.__dict__:
            descriptor = klass.__dict__["protectWindows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_precisionAsDisplayed():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "precisionAsDisplayed")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "precisionAsDisplayed" in klass.__dict__:
            descriptor = klass.__dict__["precisionAsDisplayed"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_maxIterations():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "maxIterations")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "maxIterations" in klass.__dict__:
            descriptor = klass.__dict__["maxIterations"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_windowTopX():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "windowTopX")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "windowTopX" in klass.__dict__:
            descriptor = klass.__dict__["windowTopX"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_windowTopY():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "windowTopY")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "windowTopY" in klass.__dict__:
            descriptor = klass.__dict__["windowTopY"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_doNotCalculateBeforeSave():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "doNotCalculateBeforeSave")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "doNotCalculateBeforeSave" in klass.__dict__:
            descriptor = klass.__dict__["doNotCalculateBeforeSave"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_iteration():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "iteration")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "iteration" in klass.__dict__:
            descriptor = klass.__dict__["iteration"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_acceptLabelsInFormulas():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "acceptLabelsInFormulas")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "acceptLabelsInFormulas" in klass.__dict__:
            descriptor = klass.__dict__["acceptLabelsInFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_windowHidden():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "windowHidden")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "windowHidden" in klass.__dict__:
            descriptor = klass.__dict__["windowHidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_hideHorizontalScrollBar():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "hideHorizontalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "hideHorizontalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideHorizontalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_noAutoRecover():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "noAutoRecover")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "noAutoRecover" in klass.__dict__:
            descriptor = klass.__dict__["noAutoRecover"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_hidePivotTableFieldList():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "hidePivotTableFieldList")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "hidePivotTableFieldList" in klass.__dict__:
            descriptor = klass.__dict__["hidePivotTableFieldList"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_hideVerticalScrollBar():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "hideVerticalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "hideVerticalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideVerticalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_createBackup():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "createBackup")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "createBackup" in klass.__dict__:
            descriptor = klass.__dict__["createBackup"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_calculation():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "calculation")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "calculation" in klass.__dict__:
            descriptor = klass.__dict__["calculation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_futureVer():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "futureVer")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "futureVer" in klass.__dict__:
            descriptor = klass.__dict__["futureVer"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_windowWidth():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "windowWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "windowWidth" in klass.__dict__:
            descriptor = klass.__dict__["windowWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_hideWorkbookTabs():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "hideWorkbookTabs")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "hideWorkbookTabs" in klass.__dict__:
            descriptor = klass.__dict__["hideWorkbookTabs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_maxChange():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "maxChange")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "maxChange" in klass.__dict__:
            descriptor = klass.__dict__["maxChange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_uncalced():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "uncalced")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "uncalced" in klass.__dict__:
            descriptor = klass.__dict__["uncalced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_excelworkbook_has_activeChart():
    assert hasattr(SpreadsheetMLPrintingSetup_ExcelWorkbook, "activeChart")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ExcelWorkbook.__mro__:
        if "activeChart" in klass.__dict__:
            descriptor = klass.__dict__["activeChart"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_comment_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Comment)


def test_spreadsheetmlprintingsetup_comment_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Comment.__init__)


def test_spreadsheetmlprintingsetup_comment_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "showAlways" in params, "Missing parameter 'showAlways'"

def test_spreadsheetmlprintingsetup_comment_has_author():
    assert hasattr(SpreadsheetMLPrintingSetup_Comment, "author")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Comment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_comment_has_showAlways():
    assert hasattr(SpreadsheetMLPrintingSetup_Comment, "showAlways")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Comment.__mro__:
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



def test_spreadsheetmlprintingsetup_row_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Row)


def test_spreadsheetmlprintingsetup_row_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Row.__init__)


def test_spreadsheetmlprintingsetup_row_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Row.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "autoFitHeight" in params, "Missing parameter 'autoFitHeight'"

def test_spreadsheetmlprintingsetup_row_has_height():
    assert hasattr(SpreadsheetMLPrintingSetup_Row, "height")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Row.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_row_has_autoFitHeight():
    assert hasattr(SpreadsheetMLPrintingSetup_Row, "autoFitHeight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Row.__mro__:
        if "autoFitHeight" in klass.__dict__:
            descriptor = klass.__dict__["autoFitHeight"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_column_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Column)


def test_spreadsheetmlprintingsetup_column_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Column.__init__)


def test_spreadsheetmlprintingsetup_column_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Column.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitWidth" in params, "Missing parameter 'autoFitWidth'"
    assert "width" in params, "Missing parameter 'width'"

def test_spreadsheetmlprintingsetup_column_has_autoFitWidth():
    assert hasattr(SpreadsheetMLPrintingSetup_Column, "autoFitWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Column.__mro__:
        if "autoFitWidth" in klass.__dict__:
            descriptor = klass.__dict__["autoFitWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_column_has_width():
    assert hasattr(SpreadsheetMLPrintingSetup_Column, "width")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Column.__mro__:
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



def test_spreadsheetmlprintingsetup_cell_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Cell)


def test_spreadsheetmlprintingsetup_cell_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Cell.__init__)


def test_spreadsheetmlprintingsetup_cell_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Cell.__init__)
    params = list(sig.parameters.keys())
    assert "hRef" in params, "Missing parameter 'hRef'"
    assert "mergeAcross" in params, "Missing parameter 'mergeAcross'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "arrayRange" in params, "Missing parameter 'arrayRange'"
    assert "mergeDown" in params, "Missing parameter 'mergeDown'"

def test_spreadsheetmlprintingsetup_cell_has_hRef():
    assert hasattr(SpreadsheetMLPrintingSetup_Cell, "hRef")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Cell.__mro__:
        if "hRef" in klass.__dict__:
            descriptor = klass.__dict__["hRef"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_cell_has_mergeAcross():
    assert hasattr(SpreadsheetMLPrintingSetup_Cell, "mergeAcross")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Cell.__mro__:
        if "mergeAcross" in klass.__dict__:
            descriptor = klass.__dict__["mergeAcross"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_cell_has_formula():
    assert hasattr(SpreadsheetMLPrintingSetup_Cell, "formula")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_cell_has_arrayRange():
    assert hasattr(SpreadsheetMLPrintingSetup_Cell, "arrayRange")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Cell.__mro__:
        if "arrayRange" in klass.__dict__:
            descriptor = klass.__dict__["arrayRange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_cell_has_mergeDown():
    assert hasattr(SpreadsheetMLPrintingSetup_Cell, "mergeDown")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Cell.__mro__:
        if "mergeDown" in klass.__dict__:
            descriptor = klass.__dict__["mergeDown"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_ColOrRowElement)


def test_spreadsheetmlprintingsetup_colorrowelement_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_ColOrRowElement.__init__)


def test_spreadsheetmlprintingsetup_colorrowelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "span" in params, "Missing parameter 'span'"
    assert "hidden" in params, "Missing parameter 'hidden'"

def test_spreadsheetmlprintingsetup_colorrowelement_has_span():
    assert hasattr(SpreadsheetMLPrintingSetup_ColOrRowElement, "span")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_colorrowelement_has_hidden():
    assert hasattr(SpreadsheetMLPrintingSetup_ColOrRowElement, "hidden")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
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



def test_spreadsheetmlprintingsetup_tableelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_TableElement)


def test_spreadsheetmlprintingsetup_tableelement_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_TableElement.__init__)


def test_spreadsheetmlprintingsetup_tableelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_spreadsheetmlprintingsetup_tableelement_has_index():
    assert hasattr(SpreadsheetMLPrintingSetup_TableElement, "index")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_TableElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_table_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Table)


def test_spreadsheetmlprintingsetup_table_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Table.__init__)


def test_spreadsheetmlprintingsetup_table_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Table.__init__)
    params = list(sig.parameters.keys())
    assert "leftCell" in params, "Missing parameter 'leftCell'"
    assert "topCell" in params, "Missing parameter 'topCell'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"
    assert "expandedColumnCount" in params, "Missing parameter 'expandedColumnCount'"
    assert "fullColumns" in params, "Missing parameter 'fullColumns'"
    assert "expandedRowCount" in params, "Missing parameter 'expandedRowCount'"
    assert "fullRows" in params, "Missing parameter 'fullRows'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"

def test_spreadsheetmlprintingsetup_table_has_leftCell():
    assert hasattr(SpreadsheetMLPrintingSetup_Table, "leftCell")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Table.__mro__:
        if "leftCell" in klass.__dict__:
            descriptor = klass.__dict__["leftCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_table_has_topCell():
    assert hasattr(SpreadsheetMLPrintingSetup_Table, "topCell")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Table.__mro__:
        if "topCell" in klass.__dict__:
            descriptor = klass.__dict__["topCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_table_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLPrintingSetup_Table, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Table.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_table_has_expandedColumnCount():
    assert hasattr(SpreadsheetMLPrintingSetup_Table, "expandedColumnCount")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Table.__mro__:
        if "expandedColumnCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedColumnCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_table_has_fullColumns():
    assert hasattr(SpreadsheetMLPrintingSetup_Table, "fullColumns")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Table.__mro__:
        if "fullColumns" in klass.__dict__:
            descriptor = klass.__dict__["fullColumns"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_table_has_expandedRowCount():
    assert hasattr(SpreadsheetMLPrintingSetup_Table, "expandedRowCount")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Table.__mro__:
        if "expandedRowCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedRowCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_table_has_fullRows():
    assert hasattr(SpreadsheetMLPrintingSetup_Table, "fullRows")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Table.__mro__:
        if "fullRows" in klass.__dict__:
            descriptor = klass.__dict__["fullRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_table_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLPrintingSetup_Table, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Table.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_styledelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_StyledElement)


def test_spreadsheetmlprintingsetup_styledelement_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_StyledElement.__init__)


def test_spreadsheetmlprintingsetup_styledelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_StyledElement.__init__)
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



def test_spreadsheetmlprintingsetup_worksheet_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Worksheet)


def test_spreadsheetmlprintingsetup_worksheet_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Worksheet.__init__)


def test_spreadsheetmlprintingsetup_worksheet_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "protected" in params, "Missing parameter 'protected'"
    assert "name" in params, "Missing parameter 'name'"
    assert "rightToLeft" in params, "Missing parameter 'rightToLeft'"

def test_spreadsheetmlprintingsetup_worksheet_has_protected():
    assert hasattr(SpreadsheetMLPrintingSetup_Worksheet, "protected")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Worksheet.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheet_has_name():
    assert hasattr(SpreadsheetMLPrintingSetup_Worksheet, "name")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Worksheet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_worksheet_has_rightToLeft():
    assert hasattr(SpreadsheetMLPrintingSetup_Worksheet, "rightToLeft")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_Worksheet.__mro__:
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



def test_spreadsheetmlprintingsetup_workbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_Workbook)


def test_spreadsheetmlprintingsetup_workbook_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_Workbook.__init__)


def test_spreadsheetmlprintingsetup_workbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_Workbook.__init__)
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



def test_spreadsheetmlprintingsetup_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_SmartTagsCollection)


def test_spreadsheetmlprintingsetup_smarttagscollection_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_SmartTagsCollection.__init__)


def test_spreadsheetmlprintingsetup_smarttagscollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SmartTagsCollection)


def test_smarttagscollection_constructor_exists():
    assert callable(SmartTagsCollection.__init__)


def test_smarttagscollection_constructor_args():
    sig = inspect.signature(SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_SmartTagType)


def test_spreadsheetmlprintingsetup_smarttagtype_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_SmartTagType.__init__)


def test_spreadsheetmlprintingsetup_smarttagtype_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlprintingsetup_smarttagtype_has_url():
    assert hasattr(SpreadsheetMLPrintingSetup_SmartTagType, "url")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_smarttagtype_has_namespaceuri():
    assert hasattr(SpreadsheetMLPrintingSetup_SmartTagType, "namespaceuri")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_smarttagtype_has_name():
    assert hasattr(SpreadsheetMLPrintingSetup_SmartTagType, "name")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup_customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_CustomDocumentProperty)


def test_spreadsheetmlprintingsetup_customdocumentproperty_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_CustomDocumentProperty.__init__)


def test_spreadsheetmlprintingsetup_customdocumentproperty_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlprintingsetup_customdocumentproperty_has_name():
    assert hasattr(SpreadsheetMLPrintingSetup_CustomDocumentProperty, "name")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_CustomDocumentProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection)


def test_spreadsheetmlprintingsetup_customdocumentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection.__init__)


def test_spreadsheetmlprintingsetup_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection.__init__)
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



def test_spreadsheetmlprintingsetup_numbervalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_NumberValue)


def test_spreadsheetmlprintingsetup_numbervalue_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_NumberValue.__init__)


def test_spreadsheetmlprintingsetup_numbervalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlprintingsetup_numbervalue_has_value():
    assert hasattr(SpreadsheetMLPrintingSetup_NumberValue, "value")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_stringvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_StringValue)


def test_spreadsheetmlprintingsetup_stringvalue_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_StringValue.__init__)


def test_spreadsheetmlprintingsetup_stringvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlprintingsetup_stringvalue_has_value():
    assert hasattr(SpreadsheetMLPrintingSetup_StringValue, "value")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_StringValue.__mro__:
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



def test_spreadsheetmlprintingsetup_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection)


def test_spreadsheetmlprintingsetup_documentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__init__)


def test_spreadsheetmlprintingsetup_documentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "characters" in params, "Missing parameter 'characters'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "lines" in params, "Missing parameter 'lines'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "author" in params, "Missing parameter 'author'"
    assert "description" in params, "Missing parameter 'description'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "category" in params, "Missing parameter 'category'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "title" in params, "Missing parameter 'title'"
    assert "company" in params, "Missing parameter 'company'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "words" in params, "Missing parameter 'words'"
    assert "revision" in params, "Missing parameter 'revision'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_characters():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_paragraphs():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_lines():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_presentationFormat():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_subject():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_manager():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_keywords():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_author():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_description():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_lastAuthor():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_category():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_totalTime():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_bytes():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_appName():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_title():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_company():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_words():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_revision():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_pages():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_guid():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(SpreadsheetMLPrintingSetup_DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_errorvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_ErrorValue)


def test_spreadsheetmlprintingsetup_errorvalue_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_ErrorValue.__init__)


def test_spreadsheetmlprintingsetup_errorvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_BooleanValue)


def test_spreadsheetmlprintingsetup_booleanvalue_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_BooleanValue.__init__)


def test_spreadsheetmlprintingsetup_booleanvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlprintingsetup_booleanvalue_has_value():
    assert hasattr(SpreadsheetMLPrintingSetup_BooleanValue, "value")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_BooleanValue.__mro__:
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



def test_spreadsheetmlprintingsetup_datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_DateTimeTypeValue)


def test_spreadsheetmlprintingsetup_datetimetypevalue_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_DateTimeTypeValue.__init__)


def test_spreadsheetmlprintingsetup_datetimetypevalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup_datetimetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_DateTimeType)


def test_spreadsheetmlprintingsetup_datetimetype_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_DateTimeType.__init__)


def test_spreadsheetmlprintingsetup_datetimetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "year" in params, "Missing parameter 'year'"
    assert "day" in params, "Missing parameter 'day'"
    assert "second" in params, "Missing parameter 'second'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "hour" in params, "Missing parameter 'hour'"

def test_spreadsheetmlprintingsetup_datetimetype_has_month():
    assert hasattr(SpreadsheetMLPrintingSetup_DateTimeType, "month")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_datetimetype_has_year():
    assert hasattr(SpreadsheetMLPrintingSetup_DateTimeType, "year")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_datetimetype_has_day():
    assert hasattr(SpreadsheetMLPrintingSetup_DateTimeType, "day")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_datetimetype_has_second():
    assert hasattr(SpreadsheetMLPrintingSetup_DateTimeType, "second")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_datetimetype_has_minute():
    assert hasattr(SpreadsheetMLPrintingSetup_DateTimeType, "minute")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_datetimetype_has_hour():
    assert hasattr(SpreadsheetMLPrintingSetup_DateTimeType, "hour")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlprintingsetup_valuetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_ValueType)


def test_spreadsheetmlprintingsetup_valuetype_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_ValueType.__init__)


def test_spreadsheetmlprintingsetup_valuetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlprintingsetup_versiontype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLPrintingSetup_VersionType)


def test_spreadsheetmlprintingsetup_versiontype_constructor_exists():
    assert callable(SpreadsheetMLPrintingSetup_VersionType.__init__)


def test_spreadsheetmlprintingsetup_versiontype_constructor_args():
    sig = inspect.signature(SpreadsheetMLPrintingSetup_VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "n" in params, "Missing parameter 'n'"
    assert "nn" in params, "Missing parameter 'nn'"

def test_spreadsheetmlprintingsetup_versiontype_has_n():
    assert hasattr(SpreadsheetMLPrintingSetup_VersionType, "n")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_VersionType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlprintingsetup_versiontype_has_nn():
    assert hasattr(SpreadsheetMLPrintingSetup_VersionType, "nn")
    descriptor = None
    for klass in SpreadsheetMLPrintingSetup_VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)

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

def test_displaydrawingobjectstype_exists():
    # Check that the Enumeration exists
    assert DisplayDrawingObjectsType is not None

def test_displaydrawingobjectstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DisplayDrawingObjectsType]
    expected_literals = [
        "ddot_placeHolders",
        "ddot_displayShapes",
        "ddot_hideAll",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DisplayDrawingObjectsType"

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

def test_excelworksheettypetype_exists():
    # Check that the Enumeration exists
    assert ExcelWorksheetTypeType is not None

def test_excelworksheettypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExcelWorksheetTypeType]
    expected_literals = [
        "ewt_Macro",
        "ewt_Worksheet",
        "ewt_Dialog",
        "ewt_Chart",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExcelWorksheetTypeType"

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
SpreadsheetMLPrintingSetup_PageMarginsInfo_strategy = st.builds(
    SpreadsheetMLPrintingSetup_PageMarginsInfo,
    bottom=
        safe_text,
    right=
        safe_text,
    top=
        safe_text,
    left=
        safe_text
)
SpreadsheetMLPrintingSetup_Print_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Print,
    paperSizeIndex=
        safe_text,
    verticalResolution=
        safe_text,
    gridlines=
        safe_text,
    validPrinterInfo=
        safe_text,
    leftToRight=
        safe_text,
    numberOfCopies=
        safe_text,
    fitWidth=
        safe_text,
    blackAndWhite=
        safe_text,
    commentsLayout=
        safe_text,
    rowColHeadings=
        safe_text,
    printErrors=
        safe_text,
    scale=
        safe_text,
    fitHeight=
        safe_text,
    draftQuality=
        safe_text,
    horizontalResolution=
        safe_text
)
HeaderOrFooterElt_strategy = st.builds(
    HeaderOrFooterElt,
)
SpreadsheetMLPrintingSetup_Header_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Header,
)
SpreadsheetMLPrintingSetup_HeaderOrFooterElt_strategy = st.builds(
    SpreadsheetMLPrintingSetup_HeaderOrFooterElt,
    data=
        safe_text,
    margin=
        safe_text
)
SpreadsheetMLPrintingSetup_Footer_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Footer,
)
SpreadsheetMLPrintingSetup_Layout_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Layout,
    centerHorizontal=
        safe_text,
    centerVertical=
        safe_text,
    startPageNumber=
        safe_text,
    orientation=
        safe_text
)
PageMarginsInfo_strategy = st.builds(
    PageMarginsInfo,
)
SpreadsheetMLPrintingSetup_PageSetup_strategy = st.builds(
    SpreadsheetMLPrintingSetup_PageSetup,
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
SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy = st.builds(
    SpreadsheetMLPrintingSetup_WorksheetOptionsElt,
    selected=
        safe_text,
    protectObjects=
        safe_text,
    allowDeleteRows=
        safe_text,
    allowSizeRows=
        safe_text,
    displayRightToLeft=
        safe_text,
    displayPageBreak=
        safe_text,
    transitionExpressionEvaluation=
        safe_text,
    defaultColumnWidth=
        safe_text,
    standardWidth=
        safe_text,
    showPageBreakZoom=
        safe_text,
    allowInsertHyperlinks=
        safe_text,
    allowSizeCols=
        safe_text,
    gridlineColor=
        safe_text,
    enableSelection=
        safe_text,
    protectContentst=
        safe_text,
    topRowVisible=
        safe_text,
    activePane=
        safe_text,
    freezePanes=
        safe_text,
    rangeSelection=
        safe_text,
    intlMacro=
        safe_text,
    unsynced=
        safe_text,
    activeColumn=
        safe_text,
    frozenNoSplit=
        safe_text,
    allowInsertCols=
        safe_text,
    protectScenarios=
        safe_text,
    codeName=
        safe_text,
    pageBreakZoom=
        safe_text,
    visible=
        safe_text,
    displayFormulas=
        safe_text,
    defaultRowHeight=
        safe_text,
    gridlineColorIndex=
        safe_text,
    doNotDisplayColHeaders=
        safe_text,
    noSummaryRowsBelowDetail=
        safe_text,
    doNotDisplayGridlines=
        safe_text,
    transitionFormulaEntry=
        safe_text,
    doNotDisplayZeros=
        safe_text,
    allowFormatCells=
        safe_text,
    activeRow=
        safe_text,
    tabColorIndex=
        safe_text,
    applyAutomaticOutlineStyles=
        safe_text,
    fitToPage=
        safe_text,
    doNotDisplayHeadings=
        safe_text,
    zoom=
        safe_text,
    allowFilter=
        safe_text,
    doNotDisplayOutline=
        safe_text,
    name=
        safe_text,
    filterOn=
        safe_text,
    noSummaryColumnsRightDetail=
        safe_text,
    allowUsePivotTables=
        safe_text,
    allowSort=
        safe_text,
    topRowBottomPane=
        safe_text,
    leftColumnRightPane=
        safe_text,
    excelWorksheetType=
        safe_text,
    splitHorizontal=
        safe_text,
    leftColumnVisible=
        safe_text,
    allowDeleteCols=
        safe_text,
    allowInsertRows=
        safe_text,
    splitVertical=
        safe_text,
    doNotDisplayRowHeaders=
        safe_text
)
SpreadsheetMLPrintingSetup_Data_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Data,
)
SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy = st.builds(
    SpreadsheetMLPrintingSetup_ExcelWorkbook,
    displayInkNotes=
        safe_text,
    tabRatio=
        safe_text,
    date1904=
        safe_text,
    windowHeight=
        safe_text,
    refModeR1C1=
        safe_text,
    activeSheet=
        safe_text,
    selectedSheets=
        safe_text,
    protectStructure=
        safe_text,
    displayDrawingObjects=
        safe_text,
    doNotSaveLinkValues=
        safe_text,
    windowIconic=
        safe_text,
    embedSaveSmartTags=
        safe_text,
    firstVisibleSheet=
        safe_text,
    protectWindows=
        safe_text,
    precisionAsDisplayed=
        safe_text,
    maxIterations=
        safe_text,
    windowTopX=
        safe_text,
    windowTopY=
        safe_text,
    doNotCalculateBeforeSave=
        safe_text,
    iteration=
        safe_text,
    acceptLabelsInFormulas=
        safe_text,
    windowHidden=
        safe_text,
    hideHorizontalScrollBar=
        safe_text,
    noAutoRecover=
        safe_text,
    hidePivotTableFieldList=
        safe_text,
    hideVerticalScrollBar=
        safe_text,
    createBackup=
        safe_text,
    calculation=
        safe_text,
    futureVer=
        safe_text,
    windowWidth=
        safe_text,
    hideWorkbookTabs=
        safe_text,
    maxChange=
        safe_text,
    uncalced=
        safe_text,
    activeChart=
        safe_text
)
SpreadsheetMLPrintingSetup_Comment_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Comment,
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
SpreadsheetMLPrintingSetup_Row_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Row,
    height=
        safe_text,
    autoFitHeight=
        safe_text
)
SpreadsheetMLPrintingSetup_Column_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Column,
    autoFitWidth=
        safe_text,
    width=
        safe_text
)
TableElement_strategy = st.builds(
    TableElement,
)
SpreadsheetMLPrintingSetup_Cell_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Cell,
    hRef=
        safe_text,
    mergeAcross=
        safe_text,
    formula=
        safe_text,
    arrayRange=
        safe_text,
    mergeDown=
        safe_text
)
SpreadsheetMLPrintingSetup_ColOrRowElement_strategy = st.builds(
    SpreadsheetMLPrintingSetup_ColOrRowElement,
    span=
        safe_text,
    hidden=
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
SpreadsheetMLPrintingSetup_TableElement_strategy = st.builds(
    SpreadsheetMLPrintingSetup_TableElement,
    index=
        safe_text
)
SpreadsheetMLPrintingSetup_Table_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Table,
    leftCell=
        safe_text,
    topCell=
        safe_text,
    defaultColumnWidth=
        safe_text,
    expandedColumnCount=
        safe_text,
    fullColumns=
        safe_text,
    expandedRowCount=
        safe_text,
    fullRows=
        safe_text,
    defaultRowHeight=
        safe_text
)
SpreadsheetMLPrintingSetup_StyledElement_strategy = st.builds(
    SpreadsheetMLPrintingSetup_StyledElement,
)
WorksheetOptionsElt_strategy = st.builds(
    WorksheetOptionsElt,
)
Table_strategy = st.builds(
    Table,
)
SpreadsheetMLPrintingSetup_Worksheet_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Worksheet,
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
SpreadsheetMLPrintingSetup_Workbook_strategy = st.builds(
    SpreadsheetMLPrintingSetup_Workbook,
)
SmartTagType_strategy = st.builds(
    SmartTagType,
)
Cell_strategy = st.builds(
    Cell,
)
SpreadsheetMLPrintingSetup_SmartTagsCollection_strategy = st.builds(
    SpreadsheetMLPrintingSetup_SmartTagsCollection,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)
SpreadsheetMLPrintingSetup_SmartTagType_strategy = st.builds(
    SpreadsheetMLPrintingSetup_SmartTagType,
    url=
        safe_text,
    namespaceuri=
        safe_text,
    name=
        safe_text
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
SpreadsheetMLPrintingSetup_CustomDocumentProperty_strategy = st.builds(
    SpreadsheetMLPrintingSetup_CustomDocumentProperty,
    name=
        safe_text
)
SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection,
)
VersionType_strategy = st.builds(
    VersionType,
)
ValueType_strategy = st.builds(
    ValueType,
)
SpreadsheetMLPrintingSetup_NumberValue_strategy = st.builds(
    SpreadsheetMLPrintingSetup_NumberValue,
    value=
        safe_text
)
SpreadsheetMLPrintingSetup_StringValue_strategy = st.builds(
    SpreadsheetMLPrintingSetup_StringValue,
    value=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
Workbook_strategy = st.builds(
    Workbook,
)
SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLPrintingSetup_DocumentPropertiesCollection,
    characters=
        safe_text,
    paragraphs=
        safe_text,
    lines=
        safe_text,
    presentationFormat=
        safe_text,
    subject=
        safe_text,
    manager=
        safe_text,
    keywords=
        safe_text,
    author=
        safe_text,
    description=
        safe_text,
    lastAuthor=
        safe_text,
    category=
        safe_text,
    totalTime=
        safe_text,
    bytes=
        safe_text,
    appName=
        safe_text,
    title=
        safe_text,
    company=
        safe_text,
    hyperlinkBase=
        safe_text,
    words=
        safe_text,
    revision=
        safe_text,
    pages=
        safe_text,
    guid=
        safe_text,
    charactersWithSpaces=
        safe_text
)
SpreadsheetMLPrintingSetup_ErrorValue_strategy = st.builds(
    SpreadsheetMLPrintingSetup_ErrorValue,
)
SpreadsheetMLPrintingSetup_BooleanValue_strategy = st.builds(
    SpreadsheetMLPrintingSetup_BooleanValue,
    value=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
SpreadsheetMLPrintingSetup_DateTimeTypeValue_strategy = st.builds(
    SpreadsheetMLPrintingSetup_DateTimeTypeValue,
)
SpreadsheetMLPrintingSetup_DateTimeType_strategy = st.builds(
    SpreadsheetMLPrintingSetup_DateTimeType,
    month=
        safe_text,
    year=
        safe_text,
    day=
        safe_text,
    second=
        safe_text,
    minute=
        safe_text,
    hour=
        safe_text
)
SpreadsheetMLPrintingSetup_ValueType_strategy = st.builds(
    SpreadsheetMLPrintingSetup_ValueType,
)
SpreadsheetMLPrintingSetup_VersionType_strategy = st.builds(
    SpreadsheetMLPrintingSetup_VersionType,
    n=
        safe_text,
    nn=
        safe_text
)

@given(instance=SpreadsheetMLPrintingSetup_PageMarginsInfo_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_pagemarginsinfo_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_PageMarginsInfo)



@given(instance=SpreadsheetMLPrintingSetup_PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup_pagemarginsinfo_bottom_setter(instance):
    original = instance.bottom
    instance.bottom = original
    assert instance.bottom == original



@given(instance=SpreadsheetMLPrintingSetup_PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup_pagemarginsinfo_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original



@given(instance=SpreadsheetMLPrintingSetup_PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup_pagemarginsinfo_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original



@given(instance=SpreadsheetMLPrintingSetup_PageMarginsInfo_strategy)
def test_spreadsheetmlprintingsetup_pagemarginsinfo_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_print_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Print)



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_paperSizeIndex_setter(instance):
    original = instance.paperSizeIndex
    instance.paperSizeIndex = original
    assert instance.paperSizeIndex == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_verticalResolution_setter(instance):
    original = instance.verticalResolution
    instance.verticalResolution = original
    assert instance.verticalResolution == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_gridlines_setter(instance):
    original = instance.gridlines
    instance.gridlines = original
    assert instance.gridlines == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_validPrinterInfo_setter(instance):
    original = instance.validPrinterInfo
    instance.validPrinterInfo = original
    assert instance.validPrinterInfo == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_leftToRight_setter(instance):
    original = instance.leftToRight
    instance.leftToRight = original
    assert instance.leftToRight == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_numberOfCopies_setter(instance):
    original = instance.numberOfCopies
    instance.numberOfCopies = original
    assert instance.numberOfCopies == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_fitWidth_setter(instance):
    original = instance.fitWidth
    instance.fitWidth = original
    assert instance.fitWidth == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_blackAndWhite_setter(instance):
    original = instance.blackAndWhite
    instance.blackAndWhite = original
    assert instance.blackAndWhite == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_commentsLayout_setter(instance):
    original = instance.commentsLayout
    instance.commentsLayout = original
    assert instance.commentsLayout == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_rowColHeadings_setter(instance):
    original = instance.rowColHeadings
    instance.rowColHeadings = original
    assert instance.rowColHeadings == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_printErrors_setter(instance):
    original = instance.printErrors
    instance.printErrors = original
    assert instance.printErrors == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_fitHeight_setter(instance):
    original = instance.fitHeight
    instance.fitHeight = original
    assert instance.fitHeight == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_draftQuality_setter(instance):
    original = instance.draftQuality
    instance.draftQuality = original
    assert instance.draftQuality == original



@given(instance=SpreadsheetMLPrintingSetup_Print_strategy)
def test_spreadsheetmlprintingsetup_print_horizontalResolution_setter(instance):
    original = instance.horizontalResolution
    instance.horizontalResolution = original
    assert instance.horizontalResolution == original

@given(instance=HeaderOrFooterElt_strategy)
@settings(max_examples=50)
def test_headerorfooterelt_instantiation(instance):
    assert isinstance(instance, HeaderOrFooterElt)

@given(instance=SpreadsheetMLPrintingSetup_Header_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_header_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Header)

@given(instance=SpreadsheetMLPrintingSetup_HeaderOrFooterElt_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_headerorfooterelt_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_HeaderOrFooterElt)



@given(instance=SpreadsheetMLPrintingSetup_HeaderOrFooterElt_strategy)
def test_spreadsheetmlprintingsetup_headerorfooterelt_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=SpreadsheetMLPrintingSetup_HeaderOrFooterElt_strategy)
def test_spreadsheetmlprintingsetup_headerorfooterelt_margin_setter(instance):
    original = instance.margin
    instance.margin = original
    assert instance.margin == original

@given(instance=SpreadsheetMLPrintingSetup_Footer_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_footer_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Footer)

@given(instance=SpreadsheetMLPrintingSetup_Layout_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_layout_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Layout)



@given(instance=SpreadsheetMLPrintingSetup_Layout_strategy)
def test_spreadsheetmlprintingsetup_layout_centerHorizontal_setter(instance):
    original = instance.centerHorizontal
    instance.centerHorizontal = original
    assert instance.centerHorizontal == original



@given(instance=SpreadsheetMLPrintingSetup_Layout_strategy)
def test_spreadsheetmlprintingsetup_layout_centerVertical_setter(instance):
    original = instance.centerVertical
    instance.centerVertical = original
    assert instance.centerVertical == original



@given(instance=SpreadsheetMLPrintingSetup_Layout_strategy)
def test_spreadsheetmlprintingsetup_layout_startPageNumber_setter(instance):
    original = instance.startPageNumber
    instance.startPageNumber = original
    assert instance.startPageNumber == original



@given(instance=SpreadsheetMLPrintingSetup_Layout_strategy)
def test_spreadsheetmlprintingsetup_layout_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=PageMarginsInfo_strategy)
@settings(max_examples=50)
def test_pagemarginsinfo_instantiation(instance):
    assert isinstance(instance, PageMarginsInfo)

@given(instance=SpreadsheetMLPrintingSetup_PageSetup_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_pagesetup_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_PageSetup)

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

@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_WorksheetOptionsElt)



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_protectObjects_setter(instance):
    original = instance.protectObjects
    instance.protectObjects = original
    assert instance.protectObjects == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_allowDeleteRows_setter(instance):
    original = instance.allowDeleteRows
    instance.allowDeleteRows = original
    assert instance.allowDeleteRows == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_allowSizeRows_setter(instance):
    original = instance.allowSizeRows
    instance.allowSizeRows = original
    assert instance.allowSizeRows == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_displayRightToLeft_setter(instance):
    original = instance.displayRightToLeft
    instance.displayRightToLeft = original
    assert instance.displayRightToLeft == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_displayPageBreak_setter(instance):
    original = instance.displayPageBreak
    instance.displayPageBreak = original
    assert instance.displayPageBreak == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_transitionExpressionEvaluation_setter(instance):
    original = instance.transitionExpressionEvaluation
    instance.transitionExpressionEvaluation = original
    assert instance.transitionExpressionEvaluation == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_standardWidth_setter(instance):
    original = instance.standardWidth
    instance.standardWidth = original
    assert instance.standardWidth == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_showPageBreakZoom_setter(instance):
    original = instance.showPageBreakZoom
    instance.showPageBreakZoom = original
    assert instance.showPageBreakZoom == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_allowInsertHyperlinks_setter(instance):
    original = instance.allowInsertHyperlinks
    instance.allowInsertHyperlinks = original
    assert instance.allowInsertHyperlinks == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_allowSizeCols_setter(instance):
    original = instance.allowSizeCols
    instance.allowSizeCols = original
    assert instance.allowSizeCols == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_gridlineColor_setter(instance):
    original = instance.gridlineColor
    instance.gridlineColor = original
    assert instance.gridlineColor == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_enableSelection_setter(instance):
    original = instance.enableSelection
    instance.enableSelection = original
    assert instance.enableSelection == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_protectContentst_setter(instance):
    original = instance.protectContentst
    instance.protectContentst = original
    assert instance.protectContentst == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_topRowVisible_setter(instance):
    original = instance.topRowVisible
    instance.topRowVisible = original
    assert instance.topRowVisible == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_activePane_setter(instance):
    original = instance.activePane
    instance.activePane = original
    assert instance.activePane == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_freezePanes_setter(instance):
    original = instance.freezePanes
    instance.freezePanes = original
    assert instance.freezePanes == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_rangeSelection_setter(instance):
    original = instance.rangeSelection
    instance.rangeSelection = original
    assert instance.rangeSelection == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_intlMacro_setter(instance):
    original = instance.intlMacro
    instance.intlMacro = original
    assert instance.intlMacro == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_unsynced_setter(instance):
    original = instance.unsynced
    instance.unsynced = original
    assert instance.unsynced == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_activeColumn_setter(instance):
    original = instance.activeColumn
    instance.activeColumn = original
    assert instance.activeColumn == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_frozenNoSplit_setter(instance):
    original = instance.frozenNoSplit
    instance.frozenNoSplit = original
    assert instance.frozenNoSplit == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_allowInsertCols_setter(instance):
    original = instance.allowInsertCols
    instance.allowInsertCols = original
    assert instance.allowInsertCols == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_protectScenarios_setter(instance):
    original = instance.protectScenarios
    instance.protectScenarios = original
    assert instance.protectScenarios == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_codeName_setter(instance):
    original = instance.codeName
    instance.codeName = original
    assert instance.codeName == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_pageBreakZoom_setter(instance):
    original = instance.pageBreakZoom
    instance.pageBreakZoom = original
    assert instance.pageBreakZoom == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_displayFormulas_setter(instance):
    original = instance.displayFormulas
    instance.displayFormulas = original
    assert instance.displayFormulas == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_gridlineColorIndex_setter(instance):
    original = instance.gridlineColorIndex
    instance.gridlineColorIndex = original
    assert instance.gridlineColorIndex == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_doNotDisplayColHeaders_setter(instance):
    original = instance.doNotDisplayColHeaders
    instance.doNotDisplayColHeaders = original
    assert instance.doNotDisplayColHeaders == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_noSummaryRowsBelowDetail_setter(instance):
    original = instance.noSummaryRowsBelowDetail
    instance.noSummaryRowsBelowDetail = original
    assert instance.noSummaryRowsBelowDetail == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_doNotDisplayGridlines_setter(instance):
    original = instance.doNotDisplayGridlines
    instance.doNotDisplayGridlines = original
    assert instance.doNotDisplayGridlines == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_transitionFormulaEntry_setter(instance):
    original = instance.transitionFormulaEntry
    instance.transitionFormulaEntry = original
    assert instance.transitionFormulaEntry == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_doNotDisplayZeros_setter(instance):
    original = instance.doNotDisplayZeros
    instance.doNotDisplayZeros = original
    assert instance.doNotDisplayZeros == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_allowFormatCells_setter(instance):
    original = instance.allowFormatCells
    instance.allowFormatCells = original
    assert instance.allowFormatCells == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_activeRow_setter(instance):
    original = instance.activeRow
    instance.activeRow = original
    assert instance.activeRow == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_tabColorIndex_setter(instance):
    original = instance.tabColorIndex
    instance.tabColorIndex = original
    assert instance.tabColorIndex == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_applyAutomaticOutlineStyles_setter(instance):
    original = instance.applyAutomaticOutlineStyles
    instance.applyAutomaticOutlineStyles = original
    assert instance.applyAutomaticOutlineStyles == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_fitToPage_setter(instance):
    original = instance.fitToPage
    instance.fitToPage = original
    assert instance.fitToPage == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_doNotDisplayHeadings_setter(instance):
    original = instance.doNotDisplayHeadings
    instance.doNotDisplayHeadings = original
    assert instance.doNotDisplayHeadings == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_allowFilter_setter(instance):
    original = instance.allowFilter
    instance.allowFilter = original
    assert instance.allowFilter == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_doNotDisplayOutline_setter(instance):
    original = instance.doNotDisplayOutline
    instance.doNotDisplayOutline = original
    assert instance.doNotDisplayOutline == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_filterOn_setter(instance):
    original = instance.filterOn
    instance.filterOn = original
    assert instance.filterOn == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_noSummaryColumnsRightDetail_setter(instance):
    original = instance.noSummaryColumnsRightDetail
    instance.noSummaryColumnsRightDetail = original
    assert instance.noSummaryColumnsRightDetail == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_allowUsePivotTables_setter(instance):
    original = instance.allowUsePivotTables
    instance.allowUsePivotTables = original
    assert instance.allowUsePivotTables == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_allowSort_setter(instance):
    original = instance.allowSort
    instance.allowSort = original
    assert instance.allowSort == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_topRowBottomPane_setter(instance):
    original = instance.topRowBottomPane
    instance.topRowBottomPane = original
    assert instance.topRowBottomPane == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_leftColumnRightPane_setter(instance):
    original = instance.leftColumnRightPane
    instance.leftColumnRightPane = original
    assert instance.leftColumnRightPane == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_excelWorksheetType_setter(instance):
    original = instance.excelWorksheetType
    instance.excelWorksheetType = original
    assert instance.excelWorksheetType == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_splitHorizontal_setter(instance):
    original = instance.splitHorizontal
    instance.splitHorizontal = original
    assert instance.splitHorizontal == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_leftColumnVisible_setter(instance):
    original = instance.leftColumnVisible
    instance.leftColumnVisible = original
    assert instance.leftColumnVisible == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_allowDeleteCols_setter(instance):
    original = instance.allowDeleteCols
    instance.allowDeleteCols = original
    assert instance.allowDeleteCols == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_allowInsertRows_setter(instance):
    original = instance.allowInsertRows
    instance.allowInsertRows = original
    assert instance.allowInsertRows == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_splitVertical_setter(instance):
    original = instance.splitVertical
    instance.splitVertical = original
    assert instance.splitVertical == original



@given(instance=SpreadsheetMLPrintingSetup_WorksheetOptionsElt_strategy)
def test_spreadsheetmlprintingsetup_worksheetoptionselt_doNotDisplayRowHeaders_setter(instance):
    original = instance.doNotDisplayRowHeaders
    instance.doNotDisplayRowHeaders = original
    assert instance.doNotDisplayRowHeaders == original

@given(instance=SpreadsheetMLPrintingSetup_Data_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_data_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Data)

@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_excelworkbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_ExcelWorkbook)



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_displayInkNotes_setter(instance):
    original = instance.displayInkNotes
    instance.displayInkNotes = original
    assert instance.displayInkNotes == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_tabRatio_setter(instance):
    original = instance.tabRatio
    instance.tabRatio = original
    assert instance.tabRatio == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_date1904_setter(instance):
    original = instance.date1904
    instance.date1904 = original
    assert instance.date1904 == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_windowHeight_setter(instance):
    original = instance.windowHeight
    instance.windowHeight = original
    assert instance.windowHeight == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_refModeR1C1_setter(instance):
    original = instance.refModeR1C1
    instance.refModeR1C1 = original
    assert instance.refModeR1C1 == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_activeSheet_setter(instance):
    original = instance.activeSheet
    instance.activeSheet = original
    assert instance.activeSheet == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_selectedSheets_setter(instance):
    original = instance.selectedSheets
    instance.selectedSheets = original
    assert instance.selectedSheets == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_protectStructure_setter(instance):
    original = instance.protectStructure
    instance.protectStructure = original
    assert instance.protectStructure == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_displayDrawingObjects_setter(instance):
    original = instance.displayDrawingObjects
    instance.displayDrawingObjects = original
    assert instance.displayDrawingObjects == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_doNotSaveLinkValues_setter(instance):
    original = instance.doNotSaveLinkValues
    instance.doNotSaveLinkValues = original
    assert instance.doNotSaveLinkValues == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_windowIconic_setter(instance):
    original = instance.windowIconic
    instance.windowIconic = original
    assert instance.windowIconic == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_embedSaveSmartTags_setter(instance):
    original = instance.embedSaveSmartTags
    instance.embedSaveSmartTags = original
    assert instance.embedSaveSmartTags == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_firstVisibleSheet_setter(instance):
    original = instance.firstVisibleSheet
    instance.firstVisibleSheet = original
    assert instance.firstVisibleSheet == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_protectWindows_setter(instance):
    original = instance.protectWindows
    instance.protectWindows = original
    assert instance.protectWindows == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_precisionAsDisplayed_setter(instance):
    original = instance.precisionAsDisplayed
    instance.precisionAsDisplayed = original
    assert instance.precisionAsDisplayed == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_maxIterations_setter(instance):
    original = instance.maxIterations
    instance.maxIterations = original
    assert instance.maxIterations == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_windowTopX_setter(instance):
    original = instance.windowTopX
    instance.windowTopX = original
    assert instance.windowTopX == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_windowTopY_setter(instance):
    original = instance.windowTopY
    instance.windowTopY = original
    assert instance.windowTopY == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_doNotCalculateBeforeSave_setter(instance):
    original = instance.doNotCalculateBeforeSave
    instance.doNotCalculateBeforeSave = original
    assert instance.doNotCalculateBeforeSave == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_iteration_setter(instance):
    original = instance.iteration
    instance.iteration = original
    assert instance.iteration == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_acceptLabelsInFormulas_setter(instance):
    original = instance.acceptLabelsInFormulas
    instance.acceptLabelsInFormulas = original
    assert instance.acceptLabelsInFormulas == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_windowHidden_setter(instance):
    original = instance.windowHidden
    instance.windowHidden = original
    assert instance.windowHidden == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_hideHorizontalScrollBar_setter(instance):
    original = instance.hideHorizontalScrollBar
    instance.hideHorizontalScrollBar = original
    assert instance.hideHorizontalScrollBar == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_noAutoRecover_setter(instance):
    original = instance.noAutoRecover
    instance.noAutoRecover = original
    assert instance.noAutoRecover == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_hidePivotTableFieldList_setter(instance):
    original = instance.hidePivotTableFieldList
    instance.hidePivotTableFieldList = original
    assert instance.hidePivotTableFieldList == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_hideVerticalScrollBar_setter(instance):
    original = instance.hideVerticalScrollBar
    instance.hideVerticalScrollBar = original
    assert instance.hideVerticalScrollBar == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_createBackup_setter(instance):
    original = instance.createBackup
    instance.createBackup = original
    assert instance.createBackup == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_calculation_setter(instance):
    original = instance.calculation
    instance.calculation = original
    assert instance.calculation == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_futureVer_setter(instance):
    original = instance.futureVer
    instance.futureVer = original
    assert instance.futureVer == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_windowWidth_setter(instance):
    original = instance.windowWidth
    instance.windowWidth = original
    assert instance.windowWidth == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_hideWorkbookTabs_setter(instance):
    original = instance.hideWorkbookTabs
    instance.hideWorkbookTabs = original
    assert instance.hideWorkbookTabs == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_maxChange_setter(instance):
    original = instance.maxChange
    instance.maxChange = original
    assert instance.maxChange == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_uncalced_setter(instance):
    original = instance.uncalced
    instance.uncalced = original
    assert instance.uncalced == original



@given(instance=SpreadsheetMLPrintingSetup_ExcelWorkbook_strategy)
def test_spreadsheetmlprintingsetup_excelworkbook_activeChart_setter(instance):
    original = instance.activeChart
    instance.activeChart = original
    assert instance.activeChart == original

@given(instance=SpreadsheetMLPrintingSetup_Comment_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_comment_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Comment)



@given(instance=SpreadsheetMLPrintingSetup_Comment_strategy)
def test_spreadsheetmlprintingsetup_comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=SpreadsheetMLPrintingSetup_Comment_strategy)
def test_spreadsheetmlprintingsetup_comment_showAlways_setter(instance):
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

@given(instance=SpreadsheetMLPrintingSetup_Row_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_row_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Row)



@given(instance=SpreadsheetMLPrintingSetup_Row_strategy)
def test_spreadsheetmlprintingsetup_row_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=SpreadsheetMLPrintingSetup_Row_strategy)
def test_spreadsheetmlprintingsetup_row_autoFitHeight_setter(instance):
    original = instance.autoFitHeight
    instance.autoFitHeight = original
    assert instance.autoFitHeight == original

@given(instance=SpreadsheetMLPrintingSetup_Column_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_column_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Column)



@given(instance=SpreadsheetMLPrintingSetup_Column_strategy)
def test_spreadsheetmlprintingsetup_column_autoFitWidth_setter(instance):
    original = instance.autoFitWidth
    instance.autoFitWidth = original
    assert instance.autoFitWidth == original



@given(instance=SpreadsheetMLPrintingSetup_Column_strategy)
def test_spreadsheetmlprintingsetup_column_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SpreadsheetMLPrintingSetup_Cell_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_cell_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Cell)



@given(instance=SpreadsheetMLPrintingSetup_Cell_strategy)
def test_spreadsheetmlprintingsetup_cell_hRef_setter(instance):
    original = instance.hRef
    instance.hRef = original
    assert instance.hRef == original



@given(instance=SpreadsheetMLPrintingSetup_Cell_strategy)
def test_spreadsheetmlprintingsetup_cell_mergeAcross_setter(instance):
    original = instance.mergeAcross
    instance.mergeAcross = original
    assert instance.mergeAcross == original



@given(instance=SpreadsheetMLPrintingSetup_Cell_strategy)
def test_spreadsheetmlprintingsetup_cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=SpreadsheetMLPrintingSetup_Cell_strategy)
def test_spreadsheetmlprintingsetup_cell_arrayRange_setter(instance):
    original = instance.arrayRange
    instance.arrayRange = original
    assert instance.arrayRange == original



@given(instance=SpreadsheetMLPrintingSetup_Cell_strategy)
def test_spreadsheetmlprintingsetup_cell_mergeDown_setter(instance):
    original = instance.mergeDown
    instance.mergeDown = original
    assert instance.mergeDown == original

@given(instance=SpreadsheetMLPrintingSetup_ColOrRowElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_colorrowelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_ColOrRowElement)



@given(instance=SpreadsheetMLPrintingSetup_ColOrRowElement_strategy)
def test_spreadsheetmlprintingsetup_colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original



@given(instance=SpreadsheetMLPrintingSetup_ColOrRowElement_strategy)
def test_spreadsheetmlprintingsetup_colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

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

@given(instance=SpreadsheetMLPrintingSetup_TableElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_tableelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_TableElement)



@given(instance=SpreadsheetMLPrintingSetup_TableElement_strategy)
def test_spreadsheetmlprintingsetup_tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=SpreadsheetMLPrintingSetup_Table_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_table_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Table)



@given(instance=SpreadsheetMLPrintingSetup_Table_strategy)
def test_spreadsheetmlprintingsetup_table_leftCell_setter(instance):
    original = instance.leftCell
    instance.leftCell = original
    assert instance.leftCell == original



@given(instance=SpreadsheetMLPrintingSetup_Table_strategy)
def test_spreadsheetmlprintingsetup_table_topCell_setter(instance):
    original = instance.topCell
    instance.topCell = original
    assert instance.topCell == original



@given(instance=SpreadsheetMLPrintingSetup_Table_strategy)
def test_spreadsheetmlprintingsetup_table_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original



@given(instance=SpreadsheetMLPrintingSetup_Table_strategy)
def test_spreadsheetmlprintingsetup_table_expandedColumnCount_setter(instance):
    original = instance.expandedColumnCount
    instance.expandedColumnCount = original
    assert instance.expandedColumnCount == original



@given(instance=SpreadsheetMLPrintingSetup_Table_strategy)
def test_spreadsheetmlprintingsetup_table_fullColumns_setter(instance):
    original = instance.fullColumns
    instance.fullColumns = original
    assert instance.fullColumns == original



@given(instance=SpreadsheetMLPrintingSetup_Table_strategy)
def test_spreadsheetmlprintingsetup_table_expandedRowCount_setter(instance):
    original = instance.expandedRowCount
    instance.expandedRowCount = original
    assert instance.expandedRowCount == original



@given(instance=SpreadsheetMLPrintingSetup_Table_strategy)
def test_spreadsheetmlprintingsetup_table_fullRows_setter(instance):
    original = instance.fullRows
    instance.fullRows = original
    assert instance.fullRows == original



@given(instance=SpreadsheetMLPrintingSetup_Table_strategy)
def test_spreadsheetmlprintingsetup_table_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original

@given(instance=SpreadsheetMLPrintingSetup_StyledElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_styledelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_StyledElement)

@given(instance=WorksheetOptionsElt_strategy)
@settings(max_examples=50)
def test_worksheetoptionselt_instantiation(instance):
    assert isinstance(instance, WorksheetOptionsElt)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SpreadsheetMLPrintingSetup_Worksheet_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_worksheet_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Worksheet)



@given(instance=SpreadsheetMLPrintingSetup_Worksheet_strategy)
def test_spreadsheetmlprintingsetup_worksheet_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original



@given(instance=SpreadsheetMLPrintingSetup_Worksheet_strategy)
def test_spreadsheetmlprintingsetup_worksheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SpreadsheetMLPrintingSetup_Worksheet_strategy)
def test_spreadsheetmlprintingsetup_worksheet_rightToLeft_setter(instance):
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

@given(instance=SpreadsheetMLPrintingSetup_Workbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_workbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_Workbook)

@given(instance=SmartTagType_strategy)
@settings(max_examples=50)
def test_smarttagtype_instantiation(instance):
    assert isinstance(instance, SmartTagType)

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)

@given(instance=SpreadsheetMLPrintingSetup_SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_SmartTagsCollection)

@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)

@given(instance=SpreadsheetMLPrintingSetup_SmartTagType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_smarttagtype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_SmartTagType)



@given(instance=SpreadsheetMLPrintingSetup_SmartTagType_strategy)
def test_spreadsheetmlprintingsetup_smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=SpreadsheetMLPrintingSetup_SmartTagType_strategy)
def test_spreadsheetmlprintingsetup_smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original



@given(instance=SpreadsheetMLPrintingSetup_SmartTagType_strategy)
def test_spreadsheetmlprintingsetup_smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=SpreadsheetMLPrintingSetup_CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_CustomDocumentProperty)



@given(instance=SpreadsheetMLPrintingSetup_CustomDocumentProperty_strategy)
def test_spreadsheetmlprintingsetup_customdocumentproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection)

@given(instance=VersionType_strategy)
@settings(max_examples=50)
def test_versiontype_instantiation(instance):
    assert isinstance(instance, VersionType)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=SpreadsheetMLPrintingSetup_NumberValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_numbervalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_NumberValue)



@given(instance=SpreadsheetMLPrintingSetup_NumberValue_strategy)
def test_spreadsheetmlprintingsetup_numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLPrintingSetup_StringValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_stringvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_StringValue)



@given(instance=SpreadsheetMLPrintingSetup_StringValue_strategy)
def test_spreadsheetmlprintingsetup_stringvalue_value_setter(instance):
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

@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection)



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original



@given(instance=SpreadsheetMLPrintingSetup_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlprintingsetup_documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original

@given(instance=SpreadsheetMLPrintingSetup_ErrorValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_errorvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_ErrorValue)

@given(instance=SpreadsheetMLPrintingSetup_BooleanValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_booleanvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_BooleanValue)



@given(instance=SpreadsheetMLPrintingSetup_BooleanValue_strategy)
def test_spreadsheetmlprintingsetup_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=SpreadsheetMLPrintingSetup_DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_datetimetypevalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_DateTimeTypeValue)

@given(instance=SpreadsheetMLPrintingSetup_DateTimeType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_datetimetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_DateTimeType)



@given(instance=SpreadsheetMLPrintingSetup_DateTimeType_strategy)
def test_spreadsheetmlprintingsetup_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=SpreadsheetMLPrintingSetup_DateTimeType_strategy)
def test_spreadsheetmlprintingsetup_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=SpreadsheetMLPrintingSetup_DateTimeType_strategy)
def test_spreadsheetmlprintingsetup_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=SpreadsheetMLPrintingSetup_DateTimeType_strategy)
def test_spreadsheetmlprintingsetup_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original



@given(instance=SpreadsheetMLPrintingSetup_DateTimeType_strategy)
def test_spreadsheetmlprintingsetup_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=SpreadsheetMLPrintingSetup_DateTimeType_strategy)
def test_spreadsheetmlprintingsetup_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=SpreadsheetMLPrintingSetup_ValueType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_valuetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_ValueType)

@given(instance=SpreadsheetMLPrintingSetup_VersionType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlprintingsetup_versiontype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLPrintingSetup_VersionType)



@given(instance=SpreadsheetMLPrintingSetup_VersionType_strategy)
def test_spreadsheetmlprintingsetup_versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original



@given(instance=SpreadsheetMLPrintingSetup_VersionType_strategy)
def test_spreadsheetmlprintingsetup_versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original
