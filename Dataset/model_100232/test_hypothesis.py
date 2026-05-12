import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SpreadsheetMLWorksheetOpt_WorksheetOptionsElt,
    SpreadsheetMLWorksheetOpt_Data,
    SpreadsheetMLWorksheetOpt_ExcelWorkbook,
    SpreadsheetMLWorksheetOpt_Comment,
    Comment,
    ColOrRowElement,
    SpreadsheetMLWorksheetOpt_Row,
    SpreadsheetMLWorksheetOpt_Column,
    TableElement,
    SpreadsheetMLWorksheetOpt_Cell,
    SpreadsheetMLWorksheetOpt_ColOrRowElement,
    Column,
    StyledElement,
    SpreadsheetMLWorksheetOpt_TableElement,
    SpreadsheetMLWorksheetOpt_Table,
    SpreadsheetMLWorksheetOpt_StyledElement,
    Row,
    SpreadsheetMLWorksheetOpt_Worksheet,
    Worksheet,
    WorksheetOptionsElt,
    Table,
    SpreadsheetMLWorksheetOpt_Workbook,
    SmartTagType,
    Cell,
    ExcelWorkbook,
    SpreadsheetMLWorksheetOpt_SmartTagsCollection,
    DocumentPropertiesCollection,
    SpreadsheetMLWorksheetOpt_SmartTagType,
    CustomDocumentPropertiesCollection,
    SpreadsheetMLWorksheetOpt_CustomDocumentProperty,
    CustomDocumentProperty,
    SmartTagsCollection,
    SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection,
    VersionType,
    SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection,
    Workbook,
    Data,
    SpreadsheetMLWorksheetOpt_ValueType,
    SpreadsheetMLWorksheetOpt_VersionType,
    DateTimeType,
    ValueType,
    SpreadsheetMLWorksheetOpt_NumberValue,
    SpreadsheetMLWorksheetOpt_BooleanValue,
    SpreadsheetMLWorksheetOpt_ErrorValue,
    SpreadsheetMLWorksheetOpt_DateTimeTypeValue,
    SpreadsheetMLWorksheetOpt_StringValue,
    SpreadsheetMLWorksheetOpt_DateTimeType,
    ExcelWorksheetTypeType,
    CalculationWorkbookType,
    VisibleType,
    EnableSelectionType,
    DisplayDrawingObjectsType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_spreadsheetmlworksheetopt_worksheetoptionselt_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt)


def test_spreadsheetmlworksheetopt_worksheetoptionselt_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__init__)


def test_spreadsheetmlworksheetopt_worksheetoptionselt_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__init__)
    params = list(sig.parameters.keys())
    assert "filterOn" in params, "Missing parameter 'filterOn'"
    assert "selected" in params, "Missing parameter 'selected'"
    assert "codeName" in params, "Missing parameter 'codeName'"
    assert "enableSelection" in params, "Missing parameter 'enableSelection'"
    assert "allowSort" in params, "Missing parameter 'allowSort'"
    assert "excelWorksheetType" in params, "Missing parameter 'excelWorksheetType'"
    assert "allowInsertCols" in params, "Missing parameter 'allowInsertCols'"
    assert "splitHorizontal" in params, "Missing parameter 'splitHorizontal'"
    assert "allowSizeCols" in params, "Missing parameter 'allowSizeCols'"
    assert "rangeSelection" in params, "Missing parameter 'rangeSelection'"
    assert "showPageBreakZoom" in params, "Missing parameter 'showPageBreakZoom'"
    assert "allowFilter" in params, "Missing parameter 'allowFilter'"
    assert "allowFormatCells" in params, "Missing parameter 'allowFormatCells'"
    assert "splitVertical" in params, "Missing parameter 'splitVertical'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "doNotDisplayRowHeaders" in params, "Missing parameter 'doNotDisplayRowHeaders'"
    assert "freezePanes" in params, "Missing parameter 'freezePanes'"
    assert "activePane" in params, "Missing parameter 'activePane'"
    assert "displayFormulas" in params, "Missing parameter 'displayFormulas'"
    assert "displayRightToLeft" in params, "Missing parameter 'displayRightToLeft'"
    assert "allowInsertRows" in params, "Missing parameter 'allowInsertRows'"
    assert "frozenNoSplit" in params, "Missing parameter 'frozenNoSplit'"
    assert "doNotDisplayGridlines" in params, "Missing parameter 'doNotDisplayGridlines'"
    assert "unsynced" in params, "Missing parameter 'unsynced'"
    assert "zoom" in params, "Missing parameter 'zoom'"
    assert "leftColumnVisible" in params, "Missing parameter 'leftColumnVisible'"
    assert "topRowBottomPane" in params, "Missing parameter 'topRowBottomPane'"
    assert "tabColorIndex" in params, "Missing parameter 'tabColorIndex'"
    assert "pageBreakZoom" in params, "Missing parameter 'pageBreakZoom'"
    assert "allowDeleteRows" in params, "Missing parameter 'allowDeleteRows'"
    assert "intlMacro" in params, "Missing parameter 'intlMacro'"
    assert "topRowVisible" in params, "Missing parameter 'topRowVisible'"
    assert "allowUsePivotTables" in params, "Missing parameter 'allowUsePivotTables'"
    assert "noSummaryRowsBelowDetail" in params, "Missing parameter 'noSummaryRowsBelowDetail'"
    assert "activeColumn" in params, "Missing parameter 'activeColumn'"
    assert "protectObjects" in params, "Missing parameter 'protectObjects'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"
    assert "standardWidth" in params, "Missing parameter 'standardWidth'"
    assert "applyAutomaticOutlineStyles" in params, "Missing parameter 'applyAutomaticOutlineStyles'"
    assert "noSummaryColumnsRightDetail" in params, "Missing parameter 'noSummaryColumnsRightDetail'"
    assert "doNotDisplayOutline" in params, "Missing parameter 'doNotDisplayOutline'"
    assert "allowSizeRows" in params, "Missing parameter 'allowSizeRows'"
    assert "transitionFormulaEntry" in params, "Missing parameter 'transitionFormulaEntry'"
    assert "allowInsertHyperlinks" in params, "Missing parameter 'allowInsertHyperlinks'"
    assert "gridlineColorIndex" in params, "Missing parameter 'gridlineColorIndex'"
    assert "protectScenarios" in params, "Missing parameter 'protectScenarios'"
    assert "doNotDisplayZeros" in params, "Missing parameter 'doNotDisplayZeros'"
    assert "protectContentst" in params, "Missing parameter 'protectContentst'"
    assert "name" in params, "Missing parameter 'name'"
    assert "doNotDisplayHeadings" in params, "Missing parameter 'doNotDisplayHeadings'"
    assert "activeRow" in params, "Missing parameter 'activeRow'"
    assert "doNotDisplayColHeaders" in params, "Missing parameter 'doNotDisplayColHeaders'"
    assert "gridlineColor" in params, "Missing parameter 'gridlineColor'"
    assert "displayPageBreak" in params, "Missing parameter 'displayPageBreak'"
    assert "fitToPage" in params, "Missing parameter 'fitToPage'"
    assert "allowDeleteCols" in params, "Missing parameter 'allowDeleteCols'"
    assert "transitionExpressionEvaluation" in params, "Missing parameter 'transitionExpressionEvaluation'"
    assert "leftColumnRightPane" in params, "Missing parameter 'leftColumnRightPane'"

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_filterOn():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "filterOn")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "filterOn" in klass.__dict__:
            descriptor = klass.__dict__["filterOn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_selected():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "selected")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_codeName():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "codeName")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "codeName" in klass.__dict__:
            descriptor = klass.__dict__["codeName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_enableSelection():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "enableSelection")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "enableSelection" in klass.__dict__:
            descriptor = klass.__dict__["enableSelection"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_allowSort():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "allowSort")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "allowSort" in klass.__dict__:
            descriptor = klass.__dict__["allowSort"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_excelWorksheetType():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "excelWorksheetType")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "excelWorksheetType" in klass.__dict__:
            descriptor = klass.__dict__["excelWorksheetType"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_allowInsertCols():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "allowInsertCols")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "allowInsertCols" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_splitHorizontal():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "splitHorizontal")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "splitHorizontal" in klass.__dict__:
            descriptor = klass.__dict__["splitHorizontal"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_allowSizeCols():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "allowSizeCols")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "allowSizeCols" in klass.__dict__:
            descriptor = klass.__dict__["allowSizeCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_rangeSelection():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "rangeSelection")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "rangeSelection" in klass.__dict__:
            descriptor = klass.__dict__["rangeSelection"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_showPageBreakZoom():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "showPageBreakZoom")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "showPageBreakZoom" in klass.__dict__:
            descriptor = klass.__dict__["showPageBreakZoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_allowFilter():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "allowFilter")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "allowFilter" in klass.__dict__:
            descriptor = klass.__dict__["allowFilter"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_allowFormatCells():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "allowFormatCells")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "allowFormatCells" in klass.__dict__:
            descriptor = klass.__dict__["allowFormatCells"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_splitVertical():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "splitVertical")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "splitVertical" in klass.__dict__:
            descriptor = klass.__dict__["splitVertical"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_doNotDisplayRowHeaders():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "doNotDisplayRowHeaders")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "doNotDisplayRowHeaders" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayRowHeaders"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_freezePanes():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "freezePanes")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "freezePanes" in klass.__dict__:
            descriptor = klass.__dict__["freezePanes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_activePane():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "activePane")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "activePane" in klass.__dict__:
            descriptor = klass.__dict__["activePane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_displayFormulas():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "displayFormulas")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "displayFormulas" in klass.__dict__:
            descriptor = klass.__dict__["displayFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_displayRightToLeft():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "displayRightToLeft")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "displayRightToLeft" in klass.__dict__:
            descriptor = klass.__dict__["displayRightToLeft"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_allowInsertRows():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "allowInsertRows")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "allowInsertRows" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_frozenNoSplit():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "frozenNoSplit")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "frozenNoSplit" in klass.__dict__:
            descriptor = klass.__dict__["frozenNoSplit"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_doNotDisplayGridlines():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "doNotDisplayGridlines")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "doNotDisplayGridlines" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayGridlines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_unsynced():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "unsynced")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "unsynced" in klass.__dict__:
            descriptor = klass.__dict__["unsynced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_zoom():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "zoom")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_leftColumnVisible():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "leftColumnVisible")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "leftColumnVisible" in klass.__dict__:
            descriptor = klass.__dict__["leftColumnVisible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_topRowBottomPane():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "topRowBottomPane")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "topRowBottomPane" in klass.__dict__:
            descriptor = klass.__dict__["topRowBottomPane"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_tabColorIndex():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "tabColorIndex")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "tabColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["tabColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_pageBreakZoom():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "pageBreakZoom")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "pageBreakZoom" in klass.__dict__:
            descriptor = klass.__dict__["pageBreakZoom"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_allowDeleteRows():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "allowDeleteRows")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "allowDeleteRows" in klass.__dict__:
            descriptor = klass.__dict__["allowDeleteRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_intlMacro():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "intlMacro")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "intlMacro" in klass.__dict__:
            descriptor = klass.__dict__["intlMacro"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_topRowVisible():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "topRowVisible")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "topRowVisible" in klass.__dict__:
            descriptor = klass.__dict__["topRowVisible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_allowUsePivotTables():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "allowUsePivotTables")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "allowUsePivotTables" in klass.__dict__:
            descriptor = klass.__dict__["allowUsePivotTables"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_noSummaryRowsBelowDetail():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "noSummaryRowsBelowDetail")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "noSummaryRowsBelowDetail" in klass.__dict__:
            descriptor = klass.__dict__["noSummaryRowsBelowDetail"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_activeColumn():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "activeColumn")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "activeColumn" in klass.__dict__:
            descriptor = klass.__dict__["activeColumn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_protectObjects():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "protectObjects")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "protectObjects" in klass.__dict__:
            descriptor = klass.__dict__["protectObjects"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_visible():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "visible")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_standardWidth():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "standardWidth")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "standardWidth" in klass.__dict__:
            descriptor = klass.__dict__["standardWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_applyAutomaticOutlineStyles():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "applyAutomaticOutlineStyles")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "applyAutomaticOutlineStyles" in klass.__dict__:
            descriptor = klass.__dict__["applyAutomaticOutlineStyles"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_noSummaryColumnsRightDetail():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "noSummaryColumnsRightDetail")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "noSummaryColumnsRightDetail" in klass.__dict__:
            descriptor = klass.__dict__["noSummaryColumnsRightDetail"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_doNotDisplayOutline():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "doNotDisplayOutline")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "doNotDisplayOutline" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayOutline"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_allowSizeRows():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "allowSizeRows")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "allowSizeRows" in klass.__dict__:
            descriptor = klass.__dict__["allowSizeRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_transitionFormulaEntry():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "transitionFormulaEntry")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "transitionFormulaEntry" in klass.__dict__:
            descriptor = klass.__dict__["transitionFormulaEntry"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_allowInsertHyperlinks():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "allowInsertHyperlinks")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "allowInsertHyperlinks" in klass.__dict__:
            descriptor = klass.__dict__["allowInsertHyperlinks"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_gridlineColorIndex():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "gridlineColorIndex")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "gridlineColorIndex" in klass.__dict__:
            descriptor = klass.__dict__["gridlineColorIndex"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_protectScenarios():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "protectScenarios")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "protectScenarios" in klass.__dict__:
            descriptor = klass.__dict__["protectScenarios"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_doNotDisplayZeros():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "doNotDisplayZeros")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "doNotDisplayZeros" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayZeros"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_protectContentst():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "protectContentst")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "protectContentst" in klass.__dict__:
            descriptor = klass.__dict__["protectContentst"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_name():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "name")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_doNotDisplayHeadings():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "doNotDisplayHeadings")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "doNotDisplayHeadings" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayHeadings"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_activeRow():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "activeRow")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "activeRow" in klass.__dict__:
            descriptor = klass.__dict__["activeRow"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_doNotDisplayColHeaders():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "doNotDisplayColHeaders")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "doNotDisplayColHeaders" in klass.__dict__:
            descriptor = klass.__dict__["doNotDisplayColHeaders"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_gridlineColor():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "gridlineColor")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "gridlineColor" in klass.__dict__:
            descriptor = klass.__dict__["gridlineColor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_displayPageBreak():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "displayPageBreak")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "displayPageBreak" in klass.__dict__:
            descriptor = klass.__dict__["displayPageBreak"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_fitToPage():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "fitToPage")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "fitToPage" in klass.__dict__:
            descriptor = klass.__dict__["fitToPage"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_allowDeleteCols():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "allowDeleteCols")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "allowDeleteCols" in klass.__dict__:
            descriptor = klass.__dict__["allowDeleteCols"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_transitionExpressionEvaluation():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "transitionExpressionEvaluation")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "transitionExpressionEvaluation" in klass.__dict__:
            descriptor = klass.__dict__["transitionExpressionEvaluation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheetoptionselt_has_leftColumnRightPane():
    assert hasattr(SpreadsheetMLWorksheetOpt_WorksheetOptionsElt, "leftColumnRightPane")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_WorksheetOptionsElt.__mro__:
        if "leftColumnRightPane" in klass.__dict__:
            descriptor = klass.__dict__["leftColumnRightPane"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworksheetopt_data_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_Data)


def test_spreadsheetmlworksheetopt_data_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_Data.__init__)


def test_spreadsheetmlworksheetopt_data_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_Data.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworksheetopt_excelworkbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_ExcelWorkbook)


def test_spreadsheetmlworksheetopt_excelworkbook_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_ExcelWorkbook.__init__)


def test_spreadsheetmlworksheetopt_excelworkbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_ExcelWorkbook.__init__)
    params = list(sig.parameters.keys())
    assert "protectWindows" in params, "Missing parameter 'protectWindows'"
    assert "firstVisibleSheet" in params, "Missing parameter 'firstVisibleSheet'"
    assert "noAutoRecover" in params, "Missing parameter 'noAutoRecover'"
    assert "windowHidden" in params, "Missing parameter 'windowHidden'"
    assert "windowHeight" in params, "Missing parameter 'windowHeight'"
    assert "displayInkNotes" in params, "Missing parameter 'displayInkNotes'"
    assert "uncalced" in params, "Missing parameter 'uncalced'"
    assert "futureVer" in params, "Missing parameter 'futureVer'"
    assert "precisionAsDisplayed" in params, "Missing parameter 'precisionAsDisplayed'"
    assert "activeSheet" in params, "Missing parameter 'activeSheet'"
    assert "hideWorkbookTabs" in params, "Missing parameter 'hideWorkbookTabs'"
    assert "iteration" in params, "Missing parameter 'iteration'"
    assert "hideVerticalScrollBar" in params, "Missing parameter 'hideVerticalScrollBar'"
    assert "doNotCalculateBeforeSave" in params, "Missing parameter 'doNotCalculateBeforeSave'"
    assert "windowTopY" in params, "Missing parameter 'windowTopY'"
    assert "selectedSheets" in params, "Missing parameter 'selectedSheets'"
    assert "calculation" in params, "Missing parameter 'calculation'"
    assert "embedSaveSmartTags" in params, "Missing parameter 'embedSaveSmartTags'"
    assert "tabRatio" in params, "Missing parameter 'tabRatio'"
    assert "hidePivotTableFieldList" in params, "Missing parameter 'hidePivotTableFieldList'"
    assert "refModeR1C1" in params, "Missing parameter 'refModeR1C1'"
    assert "hideHorizontalScrollBar" in params, "Missing parameter 'hideHorizontalScrollBar'"
    assert "maxIterations" in params, "Missing parameter 'maxIterations'"
    assert "date1904" in params, "Missing parameter 'date1904'"
    assert "acceptLabelsInFormulas" in params, "Missing parameter 'acceptLabelsInFormulas'"
    assert "createBackup" in params, "Missing parameter 'createBackup'"
    assert "doNotSaveLinkValues" in params, "Missing parameter 'doNotSaveLinkValues'"
    assert "windowTopX" in params, "Missing parameter 'windowTopX'"
    assert "activeChart" in params, "Missing parameter 'activeChart'"
    assert "protectStructure" in params, "Missing parameter 'protectStructure'"
    assert "maxChange" in params, "Missing parameter 'maxChange'"
    assert "windowWidth" in params, "Missing parameter 'windowWidth'"
    assert "windowIconic" in params, "Missing parameter 'windowIconic'"
    assert "displayDrawingObjects" in params, "Missing parameter 'displayDrawingObjects'"

def test_spreadsheetmlworksheetopt_excelworkbook_has_protectWindows():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "protectWindows")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "protectWindows" in klass.__dict__:
            descriptor = klass.__dict__["protectWindows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_firstVisibleSheet():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "firstVisibleSheet")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "firstVisibleSheet" in klass.__dict__:
            descriptor = klass.__dict__["firstVisibleSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_noAutoRecover():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "noAutoRecover")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "noAutoRecover" in klass.__dict__:
            descriptor = klass.__dict__["noAutoRecover"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_windowHidden():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "windowHidden")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "windowHidden" in klass.__dict__:
            descriptor = klass.__dict__["windowHidden"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_windowHeight():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "windowHeight")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "windowHeight" in klass.__dict__:
            descriptor = klass.__dict__["windowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_displayInkNotes():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "displayInkNotes")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "displayInkNotes" in klass.__dict__:
            descriptor = klass.__dict__["displayInkNotes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_uncalced():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "uncalced")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "uncalced" in klass.__dict__:
            descriptor = klass.__dict__["uncalced"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_futureVer():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "futureVer")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "futureVer" in klass.__dict__:
            descriptor = klass.__dict__["futureVer"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_precisionAsDisplayed():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "precisionAsDisplayed")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "precisionAsDisplayed" in klass.__dict__:
            descriptor = klass.__dict__["precisionAsDisplayed"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_activeSheet():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "activeSheet")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "activeSheet" in klass.__dict__:
            descriptor = klass.__dict__["activeSheet"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_hideWorkbookTabs():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "hideWorkbookTabs")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "hideWorkbookTabs" in klass.__dict__:
            descriptor = klass.__dict__["hideWorkbookTabs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_iteration():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "iteration")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "iteration" in klass.__dict__:
            descriptor = klass.__dict__["iteration"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_hideVerticalScrollBar():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "hideVerticalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "hideVerticalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideVerticalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_doNotCalculateBeforeSave():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "doNotCalculateBeforeSave")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "doNotCalculateBeforeSave" in klass.__dict__:
            descriptor = klass.__dict__["doNotCalculateBeforeSave"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_windowTopY():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "windowTopY")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "windowTopY" in klass.__dict__:
            descriptor = klass.__dict__["windowTopY"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_selectedSheets():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "selectedSheets")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "selectedSheets" in klass.__dict__:
            descriptor = klass.__dict__["selectedSheets"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_calculation():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "calculation")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "calculation" in klass.__dict__:
            descriptor = klass.__dict__["calculation"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_embedSaveSmartTags():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "embedSaveSmartTags")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "embedSaveSmartTags" in klass.__dict__:
            descriptor = klass.__dict__["embedSaveSmartTags"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_tabRatio():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "tabRatio")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "tabRatio" in klass.__dict__:
            descriptor = klass.__dict__["tabRatio"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_hidePivotTableFieldList():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "hidePivotTableFieldList")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "hidePivotTableFieldList" in klass.__dict__:
            descriptor = klass.__dict__["hidePivotTableFieldList"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_refModeR1C1():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "refModeR1C1")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "refModeR1C1" in klass.__dict__:
            descriptor = klass.__dict__["refModeR1C1"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_hideHorizontalScrollBar():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "hideHorizontalScrollBar")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "hideHorizontalScrollBar" in klass.__dict__:
            descriptor = klass.__dict__["hideHorizontalScrollBar"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_maxIterations():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "maxIterations")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "maxIterations" in klass.__dict__:
            descriptor = klass.__dict__["maxIterations"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_date1904():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "date1904")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "date1904" in klass.__dict__:
            descriptor = klass.__dict__["date1904"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_acceptLabelsInFormulas():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "acceptLabelsInFormulas")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "acceptLabelsInFormulas" in klass.__dict__:
            descriptor = klass.__dict__["acceptLabelsInFormulas"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_createBackup():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "createBackup")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "createBackup" in klass.__dict__:
            descriptor = klass.__dict__["createBackup"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_doNotSaveLinkValues():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "doNotSaveLinkValues")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "doNotSaveLinkValues" in klass.__dict__:
            descriptor = klass.__dict__["doNotSaveLinkValues"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_windowTopX():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "windowTopX")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "windowTopX" in klass.__dict__:
            descriptor = klass.__dict__["windowTopX"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_activeChart():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "activeChart")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "activeChart" in klass.__dict__:
            descriptor = klass.__dict__["activeChart"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_protectStructure():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "protectStructure")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "protectStructure" in klass.__dict__:
            descriptor = klass.__dict__["protectStructure"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_maxChange():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "maxChange")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "maxChange" in klass.__dict__:
            descriptor = klass.__dict__["maxChange"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_windowWidth():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "windowWidth")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "windowWidth" in klass.__dict__:
            descriptor = klass.__dict__["windowWidth"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_windowIconic():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "windowIconic")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "windowIconic" in klass.__dict__:
            descriptor = klass.__dict__["windowIconic"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_excelworkbook_has_displayDrawingObjects():
    assert hasattr(SpreadsheetMLWorksheetOpt_ExcelWorkbook, "displayDrawingObjects")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ExcelWorkbook.__mro__:
        if "displayDrawingObjects" in klass.__dict__:
            descriptor = klass.__dict__["displayDrawingObjects"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworksheetopt_comment_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_Comment)


def test_spreadsheetmlworksheetopt_comment_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_Comment.__init__)


def test_spreadsheetmlworksheetopt_comment_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "showAlways" in params, "Missing parameter 'showAlways'"

def test_spreadsheetmlworksheetopt_comment_has_author():
    assert hasattr(SpreadsheetMLWorksheetOpt_Comment, "author")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Comment.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_comment_has_showAlways():
    assert hasattr(SpreadsheetMLWorksheetOpt_Comment, "showAlways")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Comment.__mro__:
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



def test_spreadsheetmlworksheetopt_row_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_Row)


def test_spreadsheetmlworksheetopt_row_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_Row.__init__)


def test_spreadsheetmlworksheetopt_row_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_Row.__init__)
    params = list(sig.parameters.keys())
    assert "autoFitHeight" in params, "Missing parameter 'autoFitHeight'"
    assert "height" in params, "Missing parameter 'height'"

def test_spreadsheetmlworksheetopt_row_has_autoFitHeight():
    assert hasattr(SpreadsheetMLWorksheetOpt_Row, "autoFitHeight")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Row.__mro__:
        if "autoFitHeight" in klass.__dict__:
            descriptor = klass.__dict__["autoFitHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_row_has_height():
    assert hasattr(SpreadsheetMLWorksheetOpt_Row, "height")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Row.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworksheetopt_column_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_Column)


def test_spreadsheetmlworksheetopt_column_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_Column.__init__)


def test_spreadsheetmlworksheetopt_column_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_Column.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "autoFitWidth" in params, "Missing parameter 'autoFitWidth'"

def test_spreadsheetmlworksheetopt_column_has_width():
    assert hasattr(SpreadsheetMLWorksheetOpt_Column, "width")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Column.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_column_has_autoFitWidth():
    assert hasattr(SpreadsheetMLWorksheetOpt_Column, "autoFitWidth")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Column.__mro__:
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



def test_spreadsheetmlworksheetopt_cell_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_Cell)


def test_spreadsheetmlworksheetopt_cell_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_Cell.__init__)


def test_spreadsheetmlworksheetopt_cell_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_Cell.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"
    assert "mergeAcross" in params, "Missing parameter 'mergeAcross'"
    assert "mergeDown" in params, "Missing parameter 'mergeDown'"
    assert "hRef" in params, "Missing parameter 'hRef'"
    assert "arrayRange" in params, "Missing parameter 'arrayRange'"

def test_spreadsheetmlworksheetopt_cell_has_formula():
    assert hasattr(SpreadsheetMLWorksheetOpt_Cell, "formula")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Cell.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_cell_has_mergeAcross():
    assert hasattr(SpreadsheetMLWorksheetOpt_Cell, "mergeAcross")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Cell.__mro__:
        if "mergeAcross" in klass.__dict__:
            descriptor = klass.__dict__["mergeAcross"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_cell_has_mergeDown():
    assert hasattr(SpreadsheetMLWorksheetOpt_Cell, "mergeDown")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Cell.__mro__:
        if "mergeDown" in klass.__dict__:
            descriptor = klass.__dict__["mergeDown"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_cell_has_hRef():
    assert hasattr(SpreadsheetMLWorksheetOpt_Cell, "hRef")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Cell.__mro__:
        if "hRef" in klass.__dict__:
            descriptor = klass.__dict__["hRef"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_cell_has_arrayRange():
    assert hasattr(SpreadsheetMLWorksheetOpt_Cell, "arrayRange")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Cell.__mro__:
        if "arrayRange" in klass.__dict__:
            descriptor = klass.__dict__["arrayRange"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworksheetopt_colorrowelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_ColOrRowElement)


def test_spreadsheetmlworksheetopt_colorrowelement_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_ColOrRowElement.__init__)


def test_spreadsheetmlworksheetopt_colorrowelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_ColOrRowElement.__init__)
    params = list(sig.parameters.keys())
    assert "span" in params, "Missing parameter 'span'"
    assert "hidden" in params, "Missing parameter 'hidden'"

def test_spreadsheetmlworksheetopt_colorrowelement_has_span():
    assert hasattr(SpreadsheetMLWorksheetOpt_ColOrRowElement, "span")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ColOrRowElement.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_colorrowelement_has_hidden():
    assert hasattr(SpreadsheetMLWorksheetOpt_ColOrRowElement, "hidden")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_ColOrRowElement.__mro__:
        if "hidden" in klass.__dict__:
            descriptor = klass.__dict__["hidden"]
            break
    assert isinstance(descriptor, property)



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



def test_spreadsheetmlworksheetopt_tableelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_TableElement)


def test_spreadsheetmlworksheetopt_tableelement_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_TableElement.__init__)


def test_spreadsheetmlworksheetopt_tableelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_TableElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_spreadsheetmlworksheetopt_tableelement_has_index():
    assert hasattr(SpreadsheetMLWorksheetOpt_TableElement, "index")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_TableElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworksheetopt_table_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_Table)


def test_spreadsheetmlworksheetopt_table_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_Table.__init__)


def test_spreadsheetmlworksheetopt_table_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_Table.__init__)
    params = list(sig.parameters.keys())
    assert "expandedColumnCount" in params, "Missing parameter 'expandedColumnCount'"
    assert "leftCell" in params, "Missing parameter 'leftCell'"
    assert "topCell" in params, "Missing parameter 'topCell'"
    assert "fullColumns" in params, "Missing parameter 'fullColumns'"
    assert "fullRows" in params, "Missing parameter 'fullRows'"
    assert "defaultRowHeight" in params, "Missing parameter 'defaultRowHeight'"
    assert "expandedRowCount" in params, "Missing parameter 'expandedRowCount'"
    assert "defaultColumnWidth" in params, "Missing parameter 'defaultColumnWidth'"

def test_spreadsheetmlworksheetopt_table_has_expandedColumnCount():
    assert hasattr(SpreadsheetMLWorksheetOpt_Table, "expandedColumnCount")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Table.__mro__:
        if "expandedColumnCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedColumnCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_table_has_leftCell():
    assert hasattr(SpreadsheetMLWorksheetOpt_Table, "leftCell")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Table.__mro__:
        if "leftCell" in klass.__dict__:
            descriptor = klass.__dict__["leftCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_table_has_topCell():
    assert hasattr(SpreadsheetMLWorksheetOpt_Table, "topCell")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Table.__mro__:
        if "topCell" in klass.__dict__:
            descriptor = klass.__dict__["topCell"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_table_has_fullColumns():
    assert hasattr(SpreadsheetMLWorksheetOpt_Table, "fullColumns")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Table.__mro__:
        if "fullColumns" in klass.__dict__:
            descriptor = klass.__dict__["fullColumns"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_table_has_fullRows():
    assert hasattr(SpreadsheetMLWorksheetOpt_Table, "fullRows")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Table.__mro__:
        if "fullRows" in klass.__dict__:
            descriptor = klass.__dict__["fullRows"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_table_has_defaultRowHeight():
    assert hasattr(SpreadsheetMLWorksheetOpt_Table, "defaultRowHeight")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Table.__mro__:
        if "defaultRowHeight" in klass.__dict__:
            descriptor = klass.__dict__["defaultRowHeight"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_table_has_expandedRowCount():
    assert hasattr(SpreadsheetMLWorksheetOpt_Table, "expandedRowCount")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Table.__mro__:
        if "expandedRowCount" in klass.__dict__:
            descriptor = klass.__dict__["expandedRowCount"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_table_has_defaultColumnWidth():
    assert hasattr(SpreadsheetMLWorksheetOpt_Table, "defaultColumnWidth")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Table.__mro__:
        if "defaultColumnWidth" in klass.__dict__:
            descriptor = klass.__dict__["defaultColumnWidth"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworksheetopt_styledelement_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_StyledElement)


def test_spreadsheetmlworksheetopt_styledelement_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_StyledElement.__init__)


def test_spreadsheetmlworksheetopt_styledelement_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_StyledElement.__init__)
    params = list(sig.parameters.keys())



def test_row_is_not_abstract():
    assert not inspect.isabstract(Row)


def test_row_constructor_exists():
    assert callable(Row.__init__)


def test_row_constructor_args():
    sig = inspect.signature(Row.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworksheetopt_worksheet_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_Worksheet)


def test_spreadsheetmlworksheetopt_worksheet_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_Worksheet.__init__)


def test_spreadsheetmlworksheetopt_worksheet_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_Worksheet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "protected" in params, "Missing parameter 'protected'"
    assert "rightToLeft" in params, "Missing parameter 'rightToLeft'"

def test_spreadsheetmlworksheetopt_worksheet_has_name():
    assert hasattr(SpreadsheetMLWorksheetOpt_Worksheet, "name")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Worksheet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheet_has_protected():
    assert hasattr(SpreadsheetMLWorksheetOpt_Worksheet, "protected")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Worksheet.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_worksheet_has_rightToLeft():
    assert hasattr(SpreadsheetMLWorksheetOpt_Worksheet, "rightToLeft")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_Worksheet.__mro__:
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



def test_spreadsheetmlworksheetopt_workbook_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_Workbook)


def test_spreadsheetmlworksheetopt_workbook_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_Workbook.__init__)


def test_spreadsheetmlworksheetopt_workbook_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_Workbook.__init__)
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



def test_excelworkbook_is_not_abstract():
    assert not inspect.isabstract(ExcelWorkbook)


def test_excelworkbook_constructor_exists():
    assert callable(ExcelWorkbook.__init__)


def test_excelworkbook_constructor_args():
    sig = inspect.signature(ExcelWorkbook.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworksheetopt_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_SmartTagsCollection)


def test_spreadsheetmlworksheetopt_smarttagscollection_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_SmartTagsCollection.__init__)


def test_spreadsheetmlworksheetopt_smarttagscollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DocumentPropertiesCollection)


def test_documentpropertiescollection_constructor_exists():
    assert callable(DocumentPropertiesCollection.__init__)


def test_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworksheetopt_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_SmartTagType)


def test_spreadsheetmlworksheetopt_smarttagtype_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_SmartTagType.__init__)


def test_spreadsheetmlworksheetopt_smarttagtype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"
    assert "url" in params, "Missing parameter 'url'"

def test_spreadsheetmlworksheetopt_smarttagtype_has_name():
    assert hasattr(SpreadsheetMLWorksheetOpt_SmartTagType, "name")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_smarttagtype_has_namespaceuri():
    assert hasattr(SpreadsheetMLWorksheetOpt_SmartTagType, "namespaceuri")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_smarttagtype_has_url():
    assert hasattr(SpreadsheetMLWorksheetOpt_SmartTagType, "url")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworksheetopt_customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_CustomDocumentProperty)


def test_spreadsheetmlworksheetopt_customdocumentproperty_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_CustomDocumentProperty.__init__)


def test_spreadsheetmlworksheetopt_customdocumentproperty_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spreadsheetmlworksheetopt_customdocumentproperty_has_name():
    assert hasattr(SpreadsheetMLWorksheetOpt_CustomDocumentProperty, "name")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_CustomDocumentProperty.__mro__:
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



def test_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SmartTagsCollection)


def test_smarttagscollection_constructor_exists():
    assert callable(SmartTagsCollection.__init__)


def test_smarttagscollection_constructor_args():
    sig = inspect.signature(SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworksheetopt_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection)


def test_spreadsheetmlworksheetopt_customdocumentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection.__init__)


def test_spreadsheetmlworksheetopt_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_versiontype_is_not_abstract():
    assert not inspect.isabstract(VersionType)


def test_versiontype_constructor_exists():
    assert callable(VersionType.__init__)


def test_versiontype_constructor_args():
    sig = inspect.signature(VersionType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworksheetopt_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection)


def test_spreadsheetmlworksheetopt_documentpropertiescollection_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__init__)


def test_spreadsheetmlworksheetopt_documentpropertiescollection_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "description" in params, "Missing parameter 'description'"
    assert "company" in params, "Missing parameter 'company'"
    assert "category" in params, "Missing parameter 'category'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "revision" in params, "Missing parameter 'revision'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "lines" in params, "Missing parameter 'lines'"
    assert "title" in params, "Missing parameter 'title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "words" in params, "Missing parameter 'words'"
    assert "manager" in params, "Missing parameter 'manager'"

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_bytes():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_lastAuthor():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_pages():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_subject():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_paragraphs():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_presentationFormat():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_description():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_company():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_category():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_characters():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_keywords():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_revision():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_totalTime():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_guid():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_lines():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_title():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_author():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_appName():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_words():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_documentpropertiescollection_has_manager():
    assert hasattr(SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)



def test_workbook_is_not_abstract():
    assert not inspect.isabstract(Workbook)


def test_workbook_constructor_exists():
    assert callable(Workbook.__init__)


def test_workbook_constructor_args():
    sig = inspect.signature(Workbook.__init__)
    params = list(sig.parameters.keys())



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworksheetopt_valuetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_ValueType)


def test_spreadsheetmlworksheetopt_valuetype_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_ValueType.__init__)


def test_spreadsheetmlworksheetopt_valuetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworksheetopt_versiontype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_VersionType)


def test_spreadsheetmlworksheetopt_versiontype_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_VersionType.__init__)


def test_spreadsheetmlworksheetopt_versiontype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "nn" in params, "Missing parameter 'nn'"
    assert "n" in params, "Missing parameter 'n'"

def test_spreadsheetmlworksheetopt_versiontype_has_nn():
    assert hasattr(SpreadsheetMLWorksheetOpt_VersionType, "nn")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_versiontype_has_n():
    assert hasattr(SpreadsheetMLWorksheetOpt_VersionType, "n")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_VersionType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
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



def test_spreadsheetmlworksheetopt_numbervalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_NumberValue)


def test_spreadsheetmlworksheetopt_numbervalue_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_NumberValue.__init__)


def test_spreadsheetmlworksheetopt_numbervalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlworksheetopt_numbervalue_has_value():
    assert hasattr(SpreadsheetMLWorksheetOpt_NumberValue, "value")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworksheetopt_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_BooleanValue)


def test_spreadsheetmlworksheetopt_booleanvalue_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_BooleanValue.__init__)


def test_spreadsheetmlworksheetopt_booleanvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlworksheetopt_booleanvalue_has_value():
    assert hasattr(SpreadsheetMLWorksheetOpt_BooleanValue, "value")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworksheetopt_errorvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_ErrorValue)


def test_spreadsheetmlworksheetopt_errorvalue_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_ErrorValue.__init__)


def test_spreadsheetmlworksheetopt_errorvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_ErrorValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworksheetopt_datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_DateTimeTypeValue)


def test_spreadsheetmlworksheetopt_datetimetypevalue_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_DateTimeTypeValue.__init__)


def test_spreadsheetmlworksheetopt_datetimetypevalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_spreadsheetmlworksheetopt_stringvalue_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_StringValue)


def test_spreadsheetmlworksheetopt_stringvalue_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_StringValue.__init__)


def test_spreadsheetmlworksheetopt_stringvalue_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_spreadsheetmlworksheetopt_stringvalue_has_value():
    assert hasattr(SpreadsheetMLWorksheetOpt_StringValue, "value")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_spreadsheetmlworksheetopt_datetimetype_is_not_abstract():
    assert not inspect.isabstract(SpreadsheetMLWorksheetOpt_DateTimeType)


def test_spreadsheetmlworksheetopt_datetimetype_constructor_exists():
    assert callable(SpreadsheetMLWorksheetOpt_DateTimeType.__init__)


def test_spreadsheetmlworksheetopt_datetimetype_constructor_args():
    sig = inspect.signature(SpreadsheetMLWorksheetOpt_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "month" in params, "Missing parameter 'month'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "second" in params, "Missing parameter 'second'"
    assert "day" in params, "Missing parameter 'day'"
    assert "minute" in params, "Missing parameter 'minute'"

def test_spreadsheetmlworksheetopt_datetimetype_has_year():
    assert hasattr(SpreadsheetMLWorksheetOpt_DateTimeType, "year")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_datetimetype_has_month():
    assert hasattr(SpreadsheetMLWorksheetOpt_DateTimeType, "month")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_datetimetype_has_hour():
    assert hasattr(SpreadsheetMLWorksheetOpt_DateTimeType, "hour")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_datetimetype_has_second():
    assert hasattr(SpreadsheetMLWorksheetOpt_DateTimeType, "second")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_datetimetype_has_day():
    assert hasattr(SpreadsheetMLWorksheetOpt_DateTimeType, "day")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_spreadsheetmlworksheetopt_datetimetype_has_minute():
    assert hasattr(SpreadsheetMLWorksheetOpt_DateTimeType, "minute")
    descriptor = None
    for klass in SpreadsheetMLWorksheetOpt_DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_excelworksheettypetype_exists():
    # Check that the Enumeration exists
    assert ExcelWorksheetTypeType is not None

def test_excelworksheettypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExcelWorksheetTypeType]
    expected_literals = [
        "ewt_Macro",
        "ewt_Dialog",
        "ewt_Worksheet",
        "ewt_Chart",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExcelWorksheetTypeType"

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

def test_visibletype_exists():
    # Check that the Enumeration exists
    assert VisibleType is not None

def test_visibletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibleType]
    expected_literals = [
        "vt_SheetVisible",
        "vt_SheetHidden",
        "vt_SheetVeryHidden",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibleType"

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
SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_WorksheetOptionsElt,
    filterOn=
        safe_text,
    selected=
        safe_text,
    codeName=
        safe_text,
    enableSelection=
        safe_text,
    allowSort=
        safe_text,
    excelWorksheetType=
        safe_text,
    allowInsertCols=
        safe_text,
    splitHorizontal=
        safe_text,
    allowSizeCols=
        safe_text,
    rangeSelection=
        safe_text,
    showPageBreakZoom=
        safe_text,
    allowFilter=
        safe_text,
    allowFormatCells=
        safe_text,
    splitVertical=
        safe_text,
    defaultRowHeight=
        safe_text,
    doNotDisplayRowHeaders=
        safe_text,
    freezePanes=
        safe_text,
    activePane=
        safe_text,
    displayFormulas=
        safe_text,
    displayRightToLeft=
        safe_text,
    allowInsertRows=
        safe_text,
    frozenNoSplit=
        safe_text,
    doNotDisplayGridlines=
        safe_text,
    unsynced=
        safe_text,
    zoom=
        safe_text,
    leftColumnVisible=
        safe_text,
    topRowBottomPane=
        safe_text,
    tabColorIndex=
        safe_text,
    pageBreakZoom=
        safe_text,
    allowDeleteRows=
        safe_text,
    intlMacro=
        safe_text,
    topRowVisible=
        safe_text,
    allowUsePivotTables=
        safe_text,
    noSummaryRowsBelowDetail=
        safe_text,
    activeColumn=
        safe_text,
    protectObjects=
        safe_text,
    visible=
        safe_text,
    defaultColumnWidth=
        safe_text,
    standardWidth=
        safe_text,
    applyAutomaticOutlineStyles=
        safe_text,
    noSummaryColumnsRightDetail=
        safe_text,
    doNotDisplayOutline=
        safe_text,
    allowSizeRows=
        safe_text,
    transitionFormulaEntry=
        safe_text,
    allowInsertHyperlinks=
        safe_text,
    gridlineColorIndex=
        safe_text,
    protectScenarios=
        safe_text,
    doNotDisplayZeros=
        safe_text,
    protectContentst=
        safe_text,
    name=
        safe_text,
    doNotDisplayHeadings=
        safe_text,
    activeRow=
        safe_text,
    doNotDisplayColHeaders=
        safe_text,
    gridlineColor=
        safe_text,
    displayPageBreak=
        safe_text,
    fitToPage=
        safe_text,
    allowDeleteCols=
        safe_text,
    transitionExpressionEvaluation=
        safe_text,
    leftColumnRightPane=
        safe_text
)
SpreadsheetMLWorksheetOpt_Data_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_Data,
)
SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_ExcelWorkbook,
    protectWindows=
        safe_text,
    firstVisibleSheet=
        safe_text,
    noAutoRecover=
        safe_text,
    windowHidden=
        safe_text,
    windowHeight=
        safe_text,
    displayInkNotes=
        safe_text,
    uncalced=
        safe_text,
    futureVer=
        safe_text,
    precisionAsDisplayed=
        safe_text,
    activeSheet=
        safe_text,
    hideWorkbookTabs=
        safe_text,
    iteration=
        safe_text,
    hideVerticalScrollBar=
        safe_text,
    doNotCalculateBeforeSave=
        safe_text,
    windowTopY=
        safe_text,
    selectedSheets=
        safe_text,
    calculation=
        safe_text,
    embedSaveSmartTags=
        safe_text,
    tabRatio=
        safe_text,
    hidePivotTableFieldList=
        safe_text,
    refModeR1C1=
        safe_text,
    hideHorizontalScrollBar=
        safe_text,
    maxIterations=
        safe_text,
    date1904=
        safe_text,
    acceptLabelsInFormulas=
        safe_text,
    createBackup=
        safe_text,
    doNotSaveLinkValues=
        safe_text,
    windowTopX=
        safe_text,
    activeChart=
        safe_text,
    protectStructure=
        safe_text,
    maxChange=
        safe_text,
    windowWidth=
        safe_text,
    windowIconic=
        safe_text,
    displayDrawingObjects=
        safe_text
)
SpreadsheetMLWorksheetOpt_Comment_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_Comment,
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
SpreadsheetMLWorksheetOpt_Row_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_Row,
    autoFitHeight=
        safe_text,
    height=
        safe_text
)
SpreadsheetMLWorksheetOpt_Column_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_Column,
    width=
        safe_text,
    autoFitWidth=
        safe_text
)
TableElement_strategy = st.builds(
    TableElement,
)
SpreadsheetMLWorksheetOpt_Cell_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_Cell,
    formula=
        safe_text,
    mergeAcross=
        safe_text,
    mergeDown=
        safe_text,
    hRef=
        safe_text,
    arrayRange=
        safe_text
)
SpreadsheetMLWorksheetOpt_ColOrRowElement_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_ColOrRowElement,
    span=
        safe_text,
    hidden=
        safe_text
)
Column_strategy = st.builds(
    Column,
)
StyledElement_strategy = st.builds(
    StyledElement,
)
SpreadsheetMLWorksheetOpt_TableElement_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_TableElement,
    index=
        safe_text
)
SpreadsheetMLWorksheetOpt_Table_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_Table,
    expandedColumnCount=
        safe_text,
    leftCell=
        safe_text,
    topCell=
        safe_text,
    fullColumns=
        safe_text,
    fullRows=
        safe_text,
    defaultRowHeight=
        safe_text,
    expandedRowCount=
        safe_text,
    defaultColumnWidth=
        safe_text
)
SpreadsheetMLWorksheetOpt_StyledElement_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_StyledElement,
)
Row_strategy = st.builds(
    Row,
)
SpreadsheetMLWorksheetOpt_Worksheet_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_Worksheet,
    name=
        safe_text,
    protected=
        safe_text,
    rightToLeft=
        safe_text
)
Worksheet_strategy = st.builds(
    Worksheet,
)
WorksheetOptionsElt_strategy = st.builds(
    WorksheetOptionsElt,
)
Table_strategy = st.builds(
    Table,
)
SpreadsheetMLWorksheetOpt_Workbook_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_Workbook,
)
SmartTagType_strategy = st.builds(
    SmartTagType,
)
Cell_strategy = st.builds(
    Cell,
)
ExcelWorkbook_strategy = st.builds(
    ExcelWorkbook,
)
SpreadsheetMLWorksheetOpt_SmartTagsCollection_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_SmartTagsCollection,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
SpreadsheetMLWorksheetOpt_SmartTagType_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_SmartTagType,
    name=
        safe_text,
    namespaceuri=
        safe_text,
    url=
        safe_text
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
SpreadsheetMLWorksheetOpt_CustomDocumentProperty_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_CustomDocumentProperty,
    name=
        safe_text
)
CustomDocumentProperty_strategy = st.builds(
    CustomDocumentProperty,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)
SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection,
)
VersionType_strategy = st.builds(
    VersionType,
)
SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection,
    bytes=
        safe_text,
    lastAuthor=
        safe_text,
    pages=
        safe_text,
    subject=
        safe_text,
    paragraphs=
        safe_text,
    presentationFormat=
        safe_text,
    description=
        safe_text,
    company=
        safe_text,
    category=
        safe_text,
    characters=
        safe_text,
    keywords=
        safe_text,
    revision=
        safe_text,
    charactersWithSpaces=
        safe_text,
    totalTime=
        safe_text,
    hyperlinkBase=
        safe_text,
    guid=
        safe_text,
    lines=
        safe_text,
    title=
        safe_text,
    author=
        safe_text,
    appName=
        safe_text,
    words=
        safe_text,
    manager=
        safe_text
)
Workbook_strategy = st.builds(
    Workbook,
)
Data_strategy = st.builds(
    Data,
)
SpreadsheetMLWorksheetOpt_ValueType_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_ValueType,
)
SpreadsheetMLWorksheetOpt_VersionType_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_VersionType,
    nn=
        safe_text,
    n=
        safe_text
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
ValueType_strategy = st.builds(
    ValueType,
)
SpreadsheetMLWorksheetOpt_NumberValue_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_NumberValue,
    value=
        safe_text
)
SpreadsheetMLWorksheetOpt_BooleanValue_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_BooleanValue,
    value=
        safe_text
)
SpreadsheetMLWorksheetOpt_ErrorValue_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_ErrorValue,
)
SpreadsheetMLWorksheetOpt_DateTimeTypeValue_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_DateTimeTypeValue,
)
SpreadsheetMLWorksheetOpt_StringValue_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_StringValue,
    value=
        safe_text
)
SpreadsheetMLWorksheetOpt_DateTimeType_strategy = st.builds(
    SpreadsheetMLWorksheetOpt_DateTimeType,
    year=
        safe_text,
    month=
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

@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_WorksheetOptionsElt)



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_filterOn_setter(instance):
    original = instance.filterOn
    instance.filterOn = original
    assert instance.filterOn == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_codeName_setter(instance):
    original = instance.codeName
    instance.codeName = original
    assert instance.codeName == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_enableSelection_setter(instance):
    original = instance.enableSelection
    instance.enableSelection = original
    assert instance.enableSelection == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_allowSort_setter(instance):
    original = instance.allowSort
    instance.allowSort = original
    assert instance.allowSort == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_excelWorksheetType_setter(instance):
    original = instance.excelWorksheetType
    instance.excelWorksheetType = original
    assert instance.excelWorksheetType == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_allowInsertCols_setter(instance):
    original = instance.allowInsertCols
    instance.allowInsertCols = original
    assert instance.allowInsertCols == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_splitHorizontal_setter(instance):
    original = instance.splitHorizontal
    instance.splitHorizontal = original
    assert instance.splitHorizontal == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_allowSizeCols_setter(instance):
    original = instance.allowSizeCols
    instance.allowSizeCols = original
    assert instance.allowSizeCols == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_rangeSelection_setter(instance):
    original = instance.rangeSelection
    instance.rangeSelection = original
    assert instance.rangeSelection == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_showPageBreakZoom_setter(instance):
    original = instance.showPageBreakZoom
    instance.showPageBreakZoom = original
    assert instance.showPageBreakZoom == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_allowFilter_setter(instance):
    original = instance.allowFilter
    instance.allowFilter = original
    assert instance.allowFilter == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_allowFormatCells_setter(instance):
    original = instance.allowFormatCells
    instance.allowFormatCells = original
    assert instance.allowFormatCells == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_splitVertical_setter(instance):
    original = instance.splitVertical
    instance.splitVertical = original
    assert instance.splitVertical == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_doNotDisplayRowHeaders_setter(instance):
    original = instance.doNotDisplayRowHeaders
    instance.doNotDisplayRowHeaders = original
    assert instance.doNotDisplayRowHeaders == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_freezePanes_setter(instance):
    original = instance.freezePanes
    instance.freezePanes = original
    assert instance.freezePanes == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_activePane_setter(instance):
    original = instance.activePane
    instance.activePane = original
    assert instance.activePane == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_displayFormulas_setter(instance):
    original = instance.displayFormulas
    instance.displayFormulas = original
    assert instance.displayFormulas == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_displayRightToLeft_setter(instance):
    original = instance.displayRightToLeft
    instance.displayRightToLeft = original
    assert instance.displayRightToLeft == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_allowInsertRows_setter(instance):
    original = instance.allowInsertRows
    instance.allowInsertRows = original
    assert instance.allowInsertRows == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_frozenNoSplit_setter(instance):
    original = instance.frozenNoSplit
    instance.frozenNoSplit = original
    assert instance.frozenNoSplit == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_doNotDisplayGridlines_setter(instance):
    original = instance.doNotDisplayGridlines
    instance.doNotDisplayGridlines = original
    assert instance.doNotDisplayGridlines == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_unsynced_setter(instance):
    original = instance.unsynced
    instance.unsynced = original
    assert instance.unsynced == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_leftColumnVisible_setter(instance):
    original = instance.leftColumnVisible
    instance.leftColumnVisible = original
    assert instance.leftColumnVisible == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_topRowBottomPane_setter(instance):
    original = instance.topRowBottomPane
    instance.topRowBottomPane = original
    assert instance.topRowBottomPane == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_tabColorIndex_setter(instance):
    original = instance.tabColorIndex
    instance.tabColorIndex = original
    assert instance.tabColorIndex == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_pageBreakZoom_setter(instance):
    original = instance.pageBreakZoom
    instance.pageBreakZoom = original
    assert instance.pageBreakZoom == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_allowDeleteRows_setter(instance):
    original = instance.allowDeleteRows
    instance.allowDeleteRows = original
    assert instance.allowDeleteRows == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_intlMacro_setter(instance):
    original = instance.intlMacro
    instance.intlMacro = original
    assert instance.intlMacro == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_topRowVisible_setter(instance):
    original = instance.topRowVisible
    instance.topRowVisible = original
    assert instance.topRowVisible == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_allowUsePivotTables_setter(instance):
    original = instance.allowUsePivotTables
    instance.allowUsePivotTables = original
    assert instance.allowUsePivotTables == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_noSummaryRowsBelowDetail_setter(instance):
    original = instance.noSummaryRowsBelowDetail
    instance.noSummaryRowsBelowDetail = original
    assert instance.noSummaryRowsBelowDetail == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_activeColumn_setter(instance):
    original = instance.activeColumn
    instance.activeColumn = original
    assert instance.activeColumn == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_protectObjects_setter(instance):
    original = instance.protectObjects
    instance.protectObjects = original
    assert instance.protectObjects == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_standardWidth_setter(instance):
    original = instance.standardWidth
    instance.standardWidth = original
    assert instance.standardWidth == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_applyAutomaticOutlineStyles_setter(instance):
    original = instance.applyAutomaticOutlineStyles
    instance.applyAutomaticOutlineStyles = original
    assert instance.applyAutomaticOutlineStyles == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_noSummaryColumnsRightDetail_setter(instance):
    original = instance.noSummaryColumnsRightDetail
    instance.noSummaryColumnsRightDetail = original
    assert instance.noSummaryColumnsRightDetail == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_doNotDisplayOutline_setter(instance):
    original = instance.doNotDisplayOutline
    instance.doNotDisplayOutline = original
    assert instance.doNotDisplayOutline == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_allowSizeRows_setter(instance):
    original = instance.allowSizeRows
    instance.allowSizeRows = original
    assert instance.allowSizeRows == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_transitionFormulaEntry_setter(instance):
    original = instance.transitionFormulaEntry
    instance.transitionFormulaEntry = original
    assert instance.transitionFormulaEntry == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_allowInsertHyperlinks_setter(instance):
    original = instance.allowInsertHyperlinks
    instance.allowInsertHyperlinks = original
    assert instance.allowInsertHyperlinks == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_gridlineColorIndex_setter(instance):
    original = instance.gridlineColorIndex
    instance.gridlineColorIndex = original
    assert instance.gridlineColorIndex == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_protectScenarios_setter(instance):
    original = instance.protectScenarios
    instance.protectScenarios = original
    assert instance.protectScenarios == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_doNotDisplayZeros_setter(instance):
    original = instance.doNotDisplayZeros
    instance.doNotDisplayZeros = original
    assert instance.doNotDisplayZeros == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_protectContentst_setter(instance):
    original = instance.protectContentst
    instance.protectContentst = original
    assert instance.protectContentst == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_doNotDisplayHeadings_setter(instance):
    original = instance.doNotDisplayHeadings
    instance.doNotDisplayHeadings = original
    assert instance.doNotDisplayHeadings == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_activeRow_setter(instance):
    original = instance.activeRow
    instance.activeRow = original
    assert instance.activeRow == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_doNotDisplayColHeaders_setter(instance):
    original = instance.doNotDisplayColHeaders
    instance.doNotDisplayColHeaders = original
    assert instance.doNotDisplayColHeaders == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_gridlineColor_setter(instance):
    original = instance.gridlineColor
    instance.gridlineColor = original
    assert instance.gridlineColor == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_displayPageBreak_setter(instance):
    original = instance.displayPageBreak
    instance.displayPageBreak = original
    assert instance.displayPageBreak == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_fitToPage_setter(instance):
    original = instance.fitToPage
    instance.fitToPage = original
    assert instance.fitToPage == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_allowDeleteCols_setter(instance):
    original = instance.allowDeleteCols
    instance.allowDeleteCols = original
    assert instance.allowDeleteCols == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_transitionExpressionEvaluation_setter(instance):
    original = instance.transitionExpressionEvaluation
    instance.transitionExpressionEvaluation = original
    assert instance.transitionExpressionEvaluation == original



@given(instance=SpreadsheetMLWorksheetOpt_WorksheetOptionsElt_strategy)
def test_spreadsheetmlworksheetopt_worksheetoptionselt_leftColumnRightPane_setter(instance):
    original = instance.leftColumnRightPane
    instance.leftColumnRightPane = original
    assert instance.leftColumnRightPane == original

@given(instance=SpreadsheetMLWorksheetOpt_Data_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_data_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_Data)

@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_excelworkbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_ExcelWorkbook)



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_protectWindows_setter(instance):
    original = instance.protectWindows
    instance.protectWindows = original
    assert instance.protectWindows == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_firstVisibleSheet_setter(instance):
    original = instance.firstVisibleSheet
    instance.firstVisibleSheet = original
    assert instance.firstVisibleSheet == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_noAutoRecover_setter(instance):
    original = instance.noAutoRecover
    instance.noAutoRecover = original
    assert instance.noAutoRecover == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_windowHidden_setter(instance):
    original = instance.windowHidden
    instance.windowHidden = original
    assert instance.windowHidden == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_windowHeight_setter(instance):
    original = instance.windowHeight
    instance.windowHeight = original
    assert instance.windowHeight == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_displayInkNotes_setter(instance):
    original = instance.displayInkNotes
    instance.displayInkNotes = original
    assert instance.displayInkNotes == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_uncalced_setter(instance):
    original = instance.uncalced
    instance.uncalced = original
    assert instance.uncalced == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_futureVer_setter(instance):
    original = instance.futureVer
    instance.futureVer = original
    assert instance.futureVer == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_precisionAsDisplayed_setter(instance):
    original = instance.precisionAsDisplayed
    instance.precisionAsDisplayed = original
    assert instance.precisionAsDisplayed == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_activeSheet_setter(instance):
    original = instance.activeSheet
    instance.activeSheet = original
    assert instance.activeSheet == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_hideWorkbookTabs_setter(instance):
    original = instance.hideWorkbookTabs
    instance.hideWorkbookTabs = original
    assert instance.hideWorkbookTabs == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_iteration_setter(instance):
    original = instance.iteration
    instance.iteration = original
    assert instance.iteration == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_hideVerticalScrollBar_setter(instance):
    original = instance.hideVerticalScrollBar
    instance.hideVerticalScrollBar = original
    assert instance.hideVerticalScrollBar == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_doNotCalculateBeforeSave_setter(instance):
    original = instance.doNotCalculateBeforeSave
    instance.doNotCalculateBeforeSave = original
    assert instance.doNotCalculateBeforeSave == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_windowTopY_setter(instance):
    original = instance.windowTopY
    instance.windowTopY = original
    assert instance.windowTopY == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_selectedSheets_setter(instance):
    original = instance.selectedSheets
    instance.selectedSheets = original
    assert instance.selectedSheets == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_calculation_setter(instance):
    original = instance.calculation
    instance.calculation = original
    assert instance.calculation == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_embedSaveSmartTags_setter(instance):
    original = instance.embedSaveSmartTags
    instance.embedSaveSmartTags = original
    assert instance.embedSaveSmartTags == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_tabRatio_setter(instance):
    original = instance.tabRatio
    instance.tabRatio = original
    assert instance.tabRatio == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_hidePivotTableFieldList_setter(instance):
    original = instance.hidePivotTableFieldList
    instance.hidePivotTableFieldList = original
    assert instance.hidePivotTableFieldList == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_refModeR1C1_setter(instance):
    original = instance.refModeR1C1
    instance.refModeR1C1 = original
    assert instance.refModeR1C1 == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_hideHorizontalScrollBar_setter(instance):
    original = instance.hideHorizontalScrollBar
    instance.hideHorizontalScrollBar = original
    assert instance.hideHorizontalScrollBar == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_maxIterations_setter(instance):
    original = instance.maxIterations
    instance.maxIterations = original
    assert instance.maxIterations == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_date1904_setter(instance):
    original = instance.date1904
    instance.date1904 = original
    assert instance.date1904 == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_acceptLabelsInFormulas_setter(instance):
    original = instance.acceptLabelsInFormulas
    instance.acceptLabelsInFormulas = original
    assert instance.acceptLabelsInFormulas == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_createBackup_setter(instance):
    original = instance.createBackup
    instance.createBackup = original
    assert instance.createBackup == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_doNotSaveLinkValues_setter(instance):
    original = instance.doNotSaveLinkValues
    instance.doNotSaveLinkValues = original
    assert instance.doNotSaveLinkValues == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_windowTopX_setter(instance):
    original = instance.windowTopX
    instance.windowTopX = original
    assert instance.windowTopX == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_activeChart_setter(instance):
    original = instance.activeChart
    instance.activeChart = original
    assert instance.activeChart == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_protectStructure_setter(instance):
    original = instance.protectStructure
    instance.protectStructure = original
    assert instance.protectStructure == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_maxChange_setter(instance):
    original = instance.maxChange
    instance.maxChange = original
    assert instance.maxChange == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_windowWidth_setter(instance):
    original = instance.windowWidth
    instance.windowWidth = original
    assert instance.windowWidth == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_windowIconic_setter(instance):
    original = instance.windowIconic
    instance.windowIconic = original
    assert instance.windowIconic == original



@given(instance=SpreadsheetMLWorksheetOpt_ExcelWorkbook_strategy)
def test_spreadsheetmlworksheetopt_excelworkbook_displayDrawingObjects_setter(instance):
    original = instance.displayDrawingObjects
    instance.displayDrawingObjects = original
    assert instance.displayDrawingObjects == original

@given(instance=SpreadsheetMLWorksheetOpt_Comment_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_comment_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_Comment)



@given(instance=SpreadsheetMLWorksheetOpt_Comment_strategy)
def test_spreadsheetmlworksheetopt_comment_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=SpreadsheetMLWorksheetOpt_Comment_strategy)
def test_spreadsheetmlworksheetopt_comment_showAlways_setter(instance):
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

@given(instance=SpreadsheetMLWorksheetOpt_Row_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_row_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_Row)



@given(instance=SpreadsheetMLWorksheetOpt_Row_strategy)
def test_spreadsheetmlworksheetopt_row_autoFitHeight_setter(instance):
    original = instance.autoFitHeight
    instance.autoFitHeight = original
    assert instance.autoFitHeight == original



@given(instance=SpreadsheetMLWorksheetOpt_Row_strategy)
def test_spreadsheetmlworksheetopt_row_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=SpreadsheetMLWorksheetOpt_Column_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_column_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_Column)



@given(instance=SpreadsheetMLWorksheetOpt_Column_strategy)
def test_spreadsheetmlworksheetopt_column_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=SpreadsheetMLWorksheetOpt_Column_strategy)
def test_spreadsheetmlworksheetopt_column_autoFitWidth_setter(instance):
    original = instance.autoFitWidth
    instance.autoFitWidth = original
    assert instance.autoFitWidth == original

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=SpreadsheetMLWorksheetOpt_Cell_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_cell_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_Cell)



@given(instance=SpreadsheetMLWorksheetOpt_Cell_strategy)
def test_spreadsheetmlworksheetopt_cell_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=SpreadsheetMLWorksheetOpt_Cell_strategy)
def test_spreadsheetmlworksheetopt_cell_mergeAcross_setter(instance):
    original = instance.mergeAcross
    instance.mergeAcross = original
    assert instance.mergeAcross == original



@given(instance=SpreadsheetMLWorksheetOpt_Cell_strategy)
def test_spreadsheetmlworksheetopt_cell_mergeDown_setter(instance):
    original = instance.mergeDown
    instance.mergeDown = original
    assert instance.mergeDown == original



@given(instance=SpreadsheetMLWorksheetOpt_Cell_strategy)
def test_spreadsheetmlworksheetopt_cell_hRef_setter(instance):
    original = instance.hRef
    instance.hRef = original
    assert instance.hRef == original



@given(instance=SpreadsheetMLWorksheetOpt_Cell_strategy)
def test_spreadsheetmlworksheetopt_cell_arrayRange_setter(instance):
    original = instance.arrayRange
    instance.arrayRange = original
    assert instance.arrayRange == original

@given(instance=SpreadsheetMLWorksheetOpt_ColOrRowElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_colorrowelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_ColOrRowElement)



@given(instance=SpreadsheetMLWorksheetOpt_ColOrRowElement_strategy)
def test_spreadsheetmlworksheetopt_colorrowelement_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original



@given(instance=SpreadsheetMLWorksheetOpt_ColOrRowElement_strategy)
def test_spreadsheetmlworksheetopt_colorrowelement_hidden_setter(instance):
    original = instance.hidden
    instance.hidden = original
    assert instance.hidden == original

@given(instance=Column_strategy)
@settings(max_examples=50)
def test_column_instantiation(instance):
    assert isinstance(instance, Column)

@given(instance=StyledElement_strategy)
@settings(max_examples=50)
def test_styledelement_instantiation(instance):
    assert isinstance(instance, StyledElement)

@given(instance=SpreadsheetMLWorksheetOpt_TableElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_tableelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_TableElement)



@given(instance=SpreadsheetMLWorksheetOpt_TableElement_strategy)
def test_spreadsheetmlworksheetopt_tableelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=SpreadsheetMLWorksheetOpt_Table_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_table_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_Table)



@given(instance=SpreadsheetMLWorksheetOpt_Table_strategy)
def test_spreadsheetmlworksheetopt_table_expandedColumnCount_setter(instance):
    original = instance.expandedColumnCount
    instance.expandedColumnCount = original
    assert instance.expandedColumnCount == original



@given(instance=SpreadsheetMLWorksheetOpt_Table_strategy)
def test_spreadsheetmlworksheetopt_table_leftCell_setter(instance):
    original = instance.leftCell
    instance.leftCell = original
    assert instance.leftCell == original



@given(instance=SpreadsheetMLWorksheetOpt_Table_strategy)
def test_spreadsheetmlworksheetopt_table_topCell_setter(instance):
    original = instance.topCell
    instance.topCell = original
    assert instance.topCell == original



@given(instance=SpreadsheetMLWorksheetOpt_Table_strategy)
def test_spreadsheetmlworksheetopt_table_fullColumns_setter(instance):
    original = instance.fullColumns
    instance.fullColumns = original
    assert instance.fullColumns == original



@given(instance=SpreadsheetMLWorksheetOpt_Table_strategy)
def test_spreadsheetmlworksheetopt_table_fullRows_setter(instance):
    original = instance.fullRows
    instance.fullRows = original
    assert instance.fullRows == original



@given(instance=SpreadsheetMLWorksheetOpt_Table_strategy)
def test_spreadsheetmlworksheetopt_table_defaultRowHeight_setter(instance):
    original = instance.defaultRowHeight
    instance.defaultRowHeight = original
    assert instance.defaultRowHeight == original



@given(instance=SpreadsheetMLWorksheetOpt_Table_strategy)
def test_spreadsheetmlworksheetopt_table_expandedRowCount_setter(instance):
    original = instance.expandedRowCount
    instance.expandedRowCount = original
    assert instance.expandedRowCount == original



@given(instance=SpreadsheetMLWorksheetOpt_Table_strategy)
def test_spreadsheetmlworksheetopt_table_defaultColumnWidth_setter(instance):
    original = instance.defaultColumnWidth
    instance.defaultColumnWidth = original
    assert instance.defaultColumnWidth == original

@given(instance=SpreadsheetMLWorksheetOpt_StyledElement_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_styledelement_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_StyledElement)

@given(instance=Row_strategy)
@settings(max_examples=50)
def test_row_instantiation(instance):
    assert isinstance(instance, Row)

@given(instance=SpreadsheetMLWorksheetOpt_Worksheet_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_worksheet_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_Worksheet)



@given(instance=SpreadsheetMLWorksheetOpt_Worksheet_strategy)
def test_spreadsheetmlworksheetopt_worksheet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SpreadsheetMLWorksheetOpt_Worksheet_strategy)
def test_spreadsheetmlworksheetopt_worksheet_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original



@given(instance=SpreadsheetMLWorksheetOpt_Worksheet_strategy)
def test_spreadsheetmlworksheetopt_worksheet_rightToLeft_setter(instance):
    original = instance.rightToLeft
    instance.rightToLeft = original
    assert instance.rightToLeft == original

@given(instance=Worksheet_strategy)
@settings(max_examples=50)
def test_worksheet_instantiation(instance):
    assert isinstance(instance, Worksheet)

@given(instance=WorksheetOptionsElt_strategy)
@settings(max_examples=50)
def test_worksheetoptionselt_instantiation(instance):
    assert isinstance(instance, WorksheetOptionsElt)

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)

@given(instance=SpreadsheetMLWorksheetOpt_Workbook_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_workbook_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_Workbook)

@given(instance=SmartTagType_strategy)
@settings(max_examples=50)
def test_smarttagtype_instantiation(instance):
    assert isinstance(instance, SmartTagType)

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)

@given(instance=ExcelWorkbook_strategy)
@settings(max_examples=50)
def test_excelworkbook_instantiation(instance):
    assert isinstance(instance, ExcelWorkbook)

@given(instance=SpreadsheetMLWorksheetOpt_SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_SmartTagsCollection)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=SpreadsheetMLWorksheetOpt_SmartTagType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_smarttagtype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_SmartTagType)



@given(instance=SpreadsheetMLWorksheetOpt_SmartTagType_strategy)
def test_spreadsheetmlworksheetopt_smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=SpreadsheetMLWorksheetOpt_SmartTagType_strategy)
def test_spreadsheetmlworksheetopt_smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original



@given(instance=SpreadsheetMLWorksheetOpt_SmartTagType_strategy)
def test_spreadsheetmlworksheetopt_smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=SpreadsheetMLWorksheetOpt_CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_CustomDocumentProperty)



@given(instance=SpreadsheetMLWorksheetOpt_CustomDocumentProperty_strategy)
def test_spreadsheetmlworksheetopt_customdocumentproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, CustomDocumentProperty)

@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)

@given(instance=SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection)

@given(instance=VersionType_strategy)
@settings(max_examples=50)
def test_versiontype_instantiation(instance):
    assert isinstance(instance, VersionType)

@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection)



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original



@given(instance=SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection_strategy)
def test_spreadsheetmlworksheetopt_documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

@given(instance=Workbook_strategy)
@settings(max_examples=50)
def test_workbook_instantiation(instance):
    assert isinstance(instance, Workbook)

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=SpreadsheetMLWorksheetOpt_ValueType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_valuetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_ValueType)

@given(instance=SpreadsheetMLWorksheetOpt_VersionType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_versiontype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_VersionType)



@given(instance=SpreadsheetMLWorksheetOpt_VersionType_strategy)
def test_spreadsheetmlworksheetopt_versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original



@given(instance=SpreadsheetMLWorksheetOpt_VersionType_strategy)
def test_spreadsheetmlworksheetopt_versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=SpreadsheetMLWorksheetOpt_NumberValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_numbervalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_NumberValue)



@given(instance=SpreadsheetMLWorksheetOpt_NumberValue_strategy)
def test_spreadsheetmlworksheetopt_numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLWorksheetOpt_BooleanValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_booleanvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_BooleanValue)



@given(instance=SpreadsheetMLWorksheetOpt_BooleanValue_strategy)
def test_spreadsheetmlworksheetopt_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLWorksheetOpt_ErrorValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_errorvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_ErrorValue)

@given(instance=SpreadsheetMLWorksheetOpt_DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_datetimetypevalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_DateTimeTypeValue)

@given(instance=SpreadsheetMLWorksheetOpt_StringValue_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_stringvalue_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_StringValue)



@given(instance=SpreadsheetMLWorksheetOpt_StringValue_strategy)
def test_spreadsheetmlworksheetopt_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SpreadsheetMLWorksheetOpt_DateTimeType_strategy)
@settings(max_examples=50)
def test_spreadsheetmlworksheetopt_datetimetype_instantiation(instance):
    assert isinstance(instance, SpreadsheetMLWorksheetOpt_DateTimeType)



@given(instance=SpreadsheetMLWorksheetOpt_DateTimeType_strategy)
def test_spreadsheetmlworksheetopt_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=SpreadsheetMLWorksheetOpt_DateTimeType_strategy)
def test_spreadsheetmlworksheetopt_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=SpreadsheetMLWorksheetOpt_DateTimeType_strategy)
def test_spreadsheetmlworksheetopt_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=SpreadsheetMLWorksheetOpt_DateTimeType_strategy)
def test_spreadsheetmlworksheetopt_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original



@given(instance=SpreadsheetMLWorksheetOpt_DateTimeType_strategy)
def test_spreadsheetmlworksheetopt_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=SpreadsheetMLWorksheetOpt_DateTimeType_strategy)
def test_spreadsheetmlworksheetopt_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original
