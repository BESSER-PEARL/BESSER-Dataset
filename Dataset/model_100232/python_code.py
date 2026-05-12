from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EnableSelectionType(Enum):
    est_UnlockedCells = "est_UnlockedCells"
    est_NoSelection = "est_NoSelection"
class CalculationWorkbookType(Enum):
    cwt_automaticCalculation = "cwt_automaticCalculation"
    cwt_manualCalculation = "cwt_manualCalculation"
    cwt_semiAutomaticCalculation = "cwt_semiAutomaticCalculation"
class VisibleType(Enum):
    vt_SheetVisible = "vt_SheetVisible"
    vt_SheetHidden = "vt_SheetHidden"
    vt_SheetVeryHidden = "vt_SheetVeryHidden"
class DisplayDrawingObjectsType(Enum):
    ddot_displayShapes = "ddot_displayShapes"
    ddot_placeHolders = "ddot_placeHolders"
    ddot_hideAll = "ddot_hideAll"
class ExcelWorksheetTypeType(Enum):
    ewt_Worksheet = "ewt_Worksheet"
    ewt_Chart = "ewt_Chart"
    ewt_Macro = "ewt_Macro"
    ewt_Dialog = "ewt_Dialog"


############################################
# Definition of Classes
############################################

class SpreadsheetMLWorksheetOpt_WorksheetOptionsElt:

    def __init__(self, fitToPage: str, doNotDisplayColHeaders: str, unsynced: str, selected: str, codeName: str, displayPageBreak: str, transitionExpressionEvaluation: str, transitionFormulaEntry: str, zoom: str, pageBreakZoom: str, doNotDisplayRowHeaders: str, gridlineColor: str, name: str, excelWorksheetType: str, intlMacro: str, standardWidth: str, visible: str, leftColumnVisible: str, displayRightToLeft: str, gridlineColorIndex: str, displayFormulas: str, doNotDisplayGridlines: str, doNotDisplayHeadings: str, showPageBreakZoom: str, defaultRowHeight: str, defaultColumnWidth: str, noSummaryColumnsRightDetail: str, doNotDisplayZeros: str, activeRow: str, activeColumn: str, filterOn: str, rangeSelection: str, doNotDisplayOutline: str, applyAutomaticOutlineStyles: str, noSummaryRowsBelowDetail: str, splitHorizontal: str, splitVertical: str, freezePanes: str, frozenNoSplit: str, tabColorIndex: str, protectContentst: str, topRowVisible: str, topRowBottomPane: str, leftColumnRightPane: str, activePane: str, allowSizeRows: str, allowInsertCols: str, allowInsertRows: str, allowInsertHyperlinks: str, allowDeleteCols: str, allowDeleteRows: str, allowSort: str, allowFilter: str, protectObjects: str, protectScenarios: str, enableSelection: str, allowFormatCells: str, allowSizeCols: str, allowUsePivotTables: str, w_worksheetOptions: "Worksheet" = None):
        self.fitToPage = fitToPage
        self.doNotDisplayColHeaders = doNotDisplayColHeaders
        self.unsynced = unsynced
        self.selected = selected
        self.codeName = codeName
        self.displayPageBreak = displayPageBreak
        self.transitionExpressionEvaluation = transitionExpressionEvaluation
        self.transitionFormulaEntry = transitionFormulaEntry
        self.zoom = zoom
        self.pageBreakZoom = pageBreakZoom
        self.doNotDisplayRowHeaders = doNotDisplayRowHeaders
        self.gridlineColor = gridlineColor
        self.name = name
        self.excelWorksheetType = excelWorksheetType
        self.intlMacro = intlMacro
        self.standardWidth = standardWidth
        self.visible = visible
        self.leftColumnVisible = leftColumnVisible
        self.displayRightToLeft = displayRightToLeft
        self.gridlineColorIndex = gridlineColorIndex
        self.displayFormulas = displayFormulas
        self.doNotDisplayGridlines = doNotDisplayGridlines
        self.doNotDisplayHeadings = doNotDisplayHeadings
        self.showPageBreakZoom = showPageBreakZoom
        self.defaultRowHeight = defaultRowHeight
        self.defaultColumnWidth = defaultColumnWidth
        self.noSummaryColumnsRightDetail = noSummaryColumnsRightDetail
        self.doNotDisplayZeros = doNotDisplayZeros
        self.activeRow = activeRow
        self.activeColumn = activeColumn
        self.filterOn = filterOn
        self.rangeSelection = rangeSelection
        self.doNotDisplayOutline = doNotDisplayOutline
        self.applyAutomaticOutlineStyles = applyAutomaticOutlineStyles
        self.noSummaryRowsBelowDetail = noSummaryRowsBelowDetail
        self.splitHorizontal = splitHorizontal
        self.splitVertical = splitVertical
        self.freezePanes = freezePanes
        self.frozenNoSplit = frozenNoSplit
        self.tabColorIndex = tabColorIndex
        self.protectContentst = protectContentst
        self.topRowVisible = topRowVisible
        self.topRowBottomPane = topRowBottomPane
        self.leftColumnRightPane = leftColumnRightPane
        self.activePane = activePane
        self.allowSizeRows = allowSizeRows
        self.allowInsertCols = allowInsertCols
        self.allowInsertRows = allowInsertRows
        self.allowInsertHyperlinks = allowInsertHyperlinks
        self.allowDeleteCols = allowDeleteCols
        self.allowDeleteRows = allowDeleteRows
        self.allowSort = allowSort
        self.allowFilter = allowFilter
        self.protectObjects = protectObjects
        self.protectScenarios = protectScenarios
        self.enableSelection = enableSelection
        self.allowFormatCells = allowFormatCells
        self.allowSizeCols = allowSizeCols
        self.allowUsePivotTables = allowUsePivotTables
        self.w_worksheetOptions = w_worksheetOptions
        
        pass
    @property
    def leftColumnRightPane(self):
        return self.__leftColumnRightPane

    @leftColumnRightPane.setter
    def leftColumnRightPane(self, leftColumnRightPane: str):
        self.__leftColumnRightPane = leftColumnRightPane


    @property
    def noSummaryColumnsRightDetail(self):
        return self.__noSummaryColumnsRightDetail

    @noSummaryColumnsRightDetail.setter
    def noSummaryColumnsRightDetail(self, noSummaryColumnsRightDetail: str):
        self.__noSummaryColumnsRightDetail = noSummaryColumnsRightDetail


    @property
    def allowInsertRows(self):
        return self.__allowInsertRows

    @allowInsertRows.setter
    def allowInsertRows(self, allowInsertRows: str):
        self.__allowInsertRows = allowInsertRows


    @property
    def displayRightToLeft(self):
        return self.__displayRightToLeft

    @displayRightToLeft.setter
    def displayRightToLeft(self, displayRightToLeft: str):
        self.__displayRightToLeft = displayRightToLeft


    @property
    def transitionExpressionEvaluation(self):
        return self.__transitionExpressionEvaluation

    @transitionExpressionEvaluation.setter
    def transitionExpressionEvaluation(self, transitionExpressionEvaluation: str):
        self.__transitionExpressionEvaluation = transitionExpressionEvaluation


    @property
    def codeName(self):
        return self.__codeName

    @codeName.setter
    def codeName(self, codeName: str):
        self.__codeName = codeName


    @property
    def defaultRowHeight(self):
        return self.__defaultRowHeight

    @defaultRowHeight.setter
    def defaultRowHeight(self, defaultRowHeight: str):
        self.__defaultRowHeight = defaultRowHeight


    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible


    @property
    def unsynced(self):
        return self.__unsynced

    @unsynced.setter
    def unsynced(self, unsynced: str):
        self.__unsynced = unsynced


    @property
    def splitHorizontal(self):
        return self.__splitHorizontal

    @splitHorizontal.setter
    def splitHorizontal(self, splitHorizontal: str):
        self.__splitHorizontal = splitHorizontal


    @property
    def allowInsertHyperlinks(self):
        return self.__allowInsertHyperlinks

    @allowInsertHyperlinks.setter
    def allowInsertHyperlinks(self, allowInsertHyperlinks: str):
        self.__allowInsertHyperlinks = allowInsertHyperlinks


    @property
    def gridlineColorIndex(self):
        return self.__gridlineColorIndex

    @gridlineColorIndex.setter
    def gridlineColorIndex(self, gridlineColorIndex: str):
        self.__gridlineColorIndex = gridlineColorIndex


    @property
    def pageBreakZoom(self):
        return self.__pageBreakZoom

    @pageBreakZoom.setter
    def pageBreakZoom(self, pageBreakZoom: str):
        self.__pageBreakZoom = pageBreakZoom


    @property
    def allowDeleteCols(self):
        return self.__allowDeleteCols

    @allowDeleteCols.setter
    def allowDeleteCols(self, allowDeleteCols: str):
        self.__allowDeleteCols = allowDeleteCols


    @property
    def applyAutomaticOutlineStyles(self):
        return self.__applyAutomaticOutlineStyles

    @applyAutomaticOutlineStyles.setter
    def applyAutomaticOutlineStyles(self, applyAutomaticOutlineStyles: str):
        self.__applyAutomaticOutlineStyles = applyAutomaticOutlineStyles


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def activeColumn(self):
        return self.__activeColumn

    @activeColumn.setter
    def activeColumn(self, activeColumn: str):
        self.__activeColumn = activeColumn


    @property
    def frozenNoSplit(self):
        return self.__frozenNoSplit

    @frozenNoSplit.setter
    def frozenNoSplit(self, frozenNoSplit: str):
        self.__frozenNoSplit = frozenNoSplit


    @property
    def protectContentst(self):
        return self.__protectContentst

    @protectContentst.setter
    def protectContentst(self, protectContentst: str):
        self.__protectContentst = protectContentst


    @property
    def noSummaryRowsBelowDetail(self):
        return self.__noSummaryRowsBelowDetail

    @noSummaryRowsBelowDetail.setter
    def noSummaryRowsBelowDetail(self, noSummaryRowsBelowDetail: str):
        self.__noSummaryRowsBelowDetail = noSummaryRowsBelowDetail


    @property
    def allowFormatCells(self):
        return self.__allowFormatCells

    @allowFormatCells.setter
    def allowFormatCells(self, allowFormatCells: str):
        self.__allowFormatCells = allowFormatCells


    @property
    def displayPageBreak(self):
        return self.__displayPageBreak

    @displayPageBreak.setter
    def displayPageBreak(self, displayPageBreak: str):
        self.__displayPageBreak = displayPageBreak


    @property
    def topRowBottomPane(self):
        return self.__topRowBottomPane

    @topRowBottomPane.setter
    def topRowBottomPane(self, topRowBottomPane: str):
        self.__topRowBottomPane = topRowBottomPane


    @property
    def intlMacro(self):
        return self.__intlMacro

    @intlMacro.setter
    def intlMacro(self, intlMacro: str):
        self.__intlMacro = intlMacro


    @property
    def enableSelection(self):
        return self.__enableSelection

    @enableSelection.setter
    def enableSelection(self, enableSelection: str):
        self.__enableSelection = enableSelection


    @property
    def gridlineColor(self):
        return self.__gridlineColor

    @gridlineColor.setter
    def gridlineColor(self, gridlineColor: str):
        self.__gridlineColor = gridlineColor


    @property
    def showPageBreakZoom(self):
        return self.__showPageBreakZoom

    @showPageBreakZoom.setter
    def showPageBreakZoom(self, showPageBreakZoom: str):
        self.__showPageBreakZoom = showPageBreakZoom


    @property
    def displayFormulas(self):
        return self.__displayFormulas

    @displayFormulas.setter
    def displayFormulas(self, displayFormulas: str):
        self.__displayFormulas = displayFormulas


    @property
    def defaultColumnWidth(self):
        return self.__defaultColumnWidth

    @defaultColumnWidth.setter
    def defaultColumnWidth(self, defaultColumnWidth: str):
        self.__defaultColumnWidth = defaultColumnWidth


    @property
    def protectObjects(self):
        return self.__protectObjects

    @protectObjects.setter
    def protectObjects(self, protectObjects: str):
        self.__protectObjects = protectObjects


    @property
    def allowUsePivotTables(self):
        return self.__allowUsePivotTables

    @allowUsePivotTables.setter
    def allowUsePivotTables(self, allowUsePivotTables: str):
        self.__allowUsePivotTables = allowUsePivotTables


    @property
    def standardWidth(self):
        return self.__standardWidth

    @standardWidth.setter
    def standardWidth(self, standardWidth: str):
        self.__standardWidth = standardWidth


    @property
    def tabColorIndex(self):
        return self.__tabColorIndex

    @tabColorIndex.setter
    def tabColorIndex(self, tabColorIndex: str):
        self.__tabColorIndex = tabColorIndex


    @property
    def activeRow(self):
        return self.__activeRow

    @activeRow.setter
    def activeRow(self, activeRow: str):
        self.__activeRow = activeRow


    @property
    def allowSort(self):
        return self.__allowSort

    @allowSort.setter
    def allowSort(self, allowSort: str):
        self.__allowSort = allowSort


    @property
    def freezePanes(self):
        return self.__freezePanes

    @freezePanes.setter
    def freezePanes(self, freezePanes: str):
        self.__freezePanes = freezePanes


    @property
    def allowSizeCols(self):
        return self.__allowSizeCols

    @allowSizeCols.setter
    def allowSizeCols(self, allowSizeCols: str):
        self.__allowSizeCols = allowSizeCols


    @property
    def splitVertical(self):
        return self.__splitVertical

    @splitVertical.setter
    def splitVertical(self, splitVertical: str):
        self.__splitVertical = splitVertical


    @property
    def excelWorksheetType(self):
        return self.__excelWorksheetType

    @excelWorksheetType.setter
    def excelWorksheetType(self, excelWorksheetType: str):
        self.__excelWorksheetType = excelWorksheetType


    @property
    def leftColumnVisible(self):
        return self.__leftColumnVisible

    @leftColumnVisible.setter
    def leftColumnVisible(self, leftColumnVisible: str):
        self.__leftColumnVisible = leftColumnVisible


    @property
    def transitionFormulaEntry(self):
        return self.__transitionFormulaEntry

    @transitionFormulaEntry.setter
    def transitionFormulaEntry(self, transitionFormulaEntry: str):
        self.__transitionFormulaEntry = transitionFormulaEntry


    @property
    def topRowVisible(self):
        return self.__topRowVisible

    @topRowVisible.setter
    def topRowVisible(self, topRowVisible: str):
        self.__topRowVisible = topRowVisible


    @property
    def fitToPage(self):
        return self.__fitToPage

    @fitToPage.setter
    def fitToPage(self, fitToPage: str):
        self.__fitToPage = fitToPage


    @property
    def activePane(self):
        return self.__activePane

    @activePane.setter
    def activePane(self, activePane: str):
        self.__activePane = activePane


    @property
    def zoom(self):
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom


    @property
    def protectScenarios(self):
        return self.__protectScenarios

    @protectScenarios.setter
    def protectScenarios(self, protectScenarios: str):
        self.__protectScenarios = protectScenarios


    @property
    def filterOn(self):
        return self.__filterOn

    @filterOn.setter
    def filterOn(self, filterOn: str):
        self.__filterOn = filterOn


    @property
    def allowDeleteRows(self):
        return self.__allowDeleteRows

    @allowDeleteRows.setter
    def allowDeleteRows(self, allowDeleteRows: str):
        self.__allowDeleteRows = allowDeleteRows


    @property
    def doNotDisplayRowHeaders(self):
        return self.__doNotDisplayRowHeaders

    @doNotDisplayRowHeaders.setter
    def doNotDisplayRowHeaders(self, doNotDisplayRowHeaders: str):
        self.__doNotDisplayRowHeaders = doNotDisplayRowHeaders


    @property
    def allowFilter(self):
        return self.__allowFilter

    @allowFilter.setter
    def allowFilter(self, allowFilter: str):
        self.__allowFilter = allowFilter


    @property
    def rangeSelection(self):
        return self.__rangeSelection

    @rangeSelection.setter
    def rangeSelection(self, rangeSelection: str):
        self.__rangeSelection = rangeSelection


    @property
    def allowInsertCols(self):
        return self.__allowInsertCols

    @allowInsertCols.setter
    def allowInsertCols(self, allowInsertCols: str):
        self.__allowInsertCols = allowInsertCols


    @property
    def doNotDisplayGridlines(self):
        return self.__doNotDisplayGridlines

    @doNotDisplayGridlines.setter
    def doNotDisplayGridlines(self, doNotDisplayGridlines: str):
        self.__doNotDisplayGridlines = doNotDisplayGridlines


    @property
    def doNotDisplayZeros(self):
        return self.__doNotDisplayZeros

    @doNotDisplayZeros.setter
    def doNotDisplayZeros(self, doNotDisplayZeros: str):
        self.__doNotDisplayZeros = doNotDisplayZeros


    @property
    def allowSizeRows(self):
        return self.__allowSizeRows

    @allowSizeRows.setter
    def allowSizeRows(self, allowSizeRows: str):
        self.__allowSizeRows = allowSizeRows


    @property
    def doNotDisplayOutline(self):
        return self.__doNotDisplayOutline

    @doNotDisplayOutline.setter
    def doNotDisplayOutline(self, doNotDisplayOutline: str):
        self.__doNotDisplayOutline = doNotDisplayOutline


    @property
    def doNotDisplayHeadings(self):
        return self.__doNotDisplayHeadings

    @doNotDisplayHeadings.setter
    def doNotDisplayHeadings(self, doNotDisplayHeadings: str):
        self.__doNotDisplayHeadings = doNotDisplayHeadings


    @property
    def doNotDisplayColHeaders(self):
        return self.__doNotDisplayColHeaders

    @doNotDisplayColHeaders.setter
    def doNotDisplayColHeaders(self, doNotDisplayColHeaders: str):
        self.__doNotDisplayColHeaders = doNotDisplayColHeaders


    @property
    def w_worksheetOptions(self):
        return self.__w_worksheetOptions

    @w_worksheetOptions.setter
    def w_worksheetOptions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_WorksheetOptionsElt__w_worksheetOptions", None)
        self.__w_worksheetOptions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Worksheet64"):
                opp_val = getattr(old_value, "Worksheet64", None)
                if opp_val == self:
                    setattr(old_value, "Worksheet64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Worksheet64"):
                opp_val = getattr(value, "Worksheet64", None)
                setattr(value, "Worksheet64", self)

class SpreadsheetMLWorksheetOpt_Data:

    pass
class SpreadsheetMLWorksheetOpt_ExcelWorkbook:

    def __init__(self, windowHidden: str, hideHorizontalScrollBar: str, hideVerticalScrollBar: str, hideWorkbookTabs: str, windowHeight: str, windowWidth: str, windowTopX: str, windowTopY: str, activeSheet: str, selectedSheets: str, displayInkNotes: str, embedSaveSmartTags: str, futureVer: str, tabRatio: str, windowIconic: str, displayDrawingObjects: str, activeChart: str, firstVisibleSheet: str, hidePivotTableFieldList: str, protectStructure: str, protectWindows: str, iteration: str, maxIterations: str, maxChange: str, precisionAsDisplayed: str, doNotSaveLinkValues: str, noAutoRecover: str, createBackup: str, calculation: str, doNotCalculateBeforeSave: str, date1904: str, refModeR1C1: str, acceptLabelsInFormulas: str, uncalced: str, wb_excelWorkbook: "Workbook" = None):
        self.windowHidden = windowHidden
        self.hideHorizontalScrollBar = hideHorizontalScrollBar
        self.hideVerticalScrollBar = hideVerticalScrollBar
        self.hideWorkbookTabs = hideWorkbookTabs
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.windowTopX = windowTopX
        self.windowTopY = windowTopY
        self.activeSheet = activeSheet
        self.selectedSheets = selectedSheets
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
        self.protectWindows = protectWindows
        self.iteration = iteration
        self.maxIterations = maxIterations
        self.maxChange = maxChange
        self.precisionAsDisplayed = precisionAsDisplayed
        self.doNotSaveLinkValues = doNotSaveLinkValues
        self.noAutoRecover = noAutoRecover
        self.createBackup = createBackup
        self.calculation = calculation
        self.doNotCalculateBeforeSave = doNotCalculateBeforeSave
        self.date1904 = date1904
        self.refModeR1C1 = refModeR1C1
        self.acceptLabelsInFormulas = acceptLabelsInFormulas
        self.uncalced = uncalced
        self.wb_excelWorkbook = wb_excelWorkbook
        
        pass
    @property
    def windowWidth(self):
        return self.__windowWidth

    @windowWidth.setter
    def windowWidth(self, windowWidth: str):
        self.__windowWidth = windowWidth


    @property
    def displayInkNotes(self):
        return self.__displayInkNotes

    @displayInkNotes.setter
    def displayInkNotes(self, displayInkNotes: str):
        self.__displayInkNotes = displayInkNotes


    @property
    def iteration(self):
        return self.__iteration

    @iteration.setter
    def iteration(self, iteration: str):
        self.__iteration = iteration


    @property
    def date1904(self):
        return self.__date1904

    @date1904.setter
    def date1904(self, date1904: str):
        self.__date1904 = date1904


    @property
    def maxChange(self):
        return self.__maxChange

    @maxChange.setter
    def maxChange(self, maxChange: str):
        self.__maxChange = maxChange


    @property
    def doNotSaveLinkValues(self):
        return self.__doNotSaveLinkValues

    @doNotSaveLinkValues.setter
    def doNotSaveLinkValues(self, doNotSaveLinkValues: str):
        self.__doNotSaveLinkValues = doNotSaveLinkValues


    @property
    def windowHidden(self):
        return self.__windowHidden

    @windowHidden.setter
    def windowHidden(self, windowHidden: str):
        self.__windowHidden = windowHidden


    @property
    def activeChart(self):
        return self.__activeChart

    @activeChart.setter
    def activeChart(self, activeChart: str):
        self.__activeChart = activeChart


    @property
    def protectWindows(self):
        return self.__protectWindows

    @protectWindows.setter
    def protectWindows(self, protectWindows: str):
        self.__protectWindows = protectWindows


    @property
    def windowTopX(self):
        return self.__windowTopX

    @windowTopX.setter
    def windowTopX(self, windowTopX: str):
        self.__windowTopX = windowTopX


    @property
    def refModeR1C1(self):
        return self.__refModeR1C1

    @refModeR1C1.setter
    def refModeR1C1(self, refModeR1C1: str):
        self.__refModeR1C1 = refModeR1C1


    @property
    def embedSaveSmartTags(self):
        return self.__embedSaveSmartTags

    @embedSaveSmartTags.setter
    def embedSaveSmartTags(self, embedSaveSmartTags: str):
        self.__embedSaveSmartTags = embedSaveSmartTags


    @property
    def tabRatio(self):
        return self.__tabRatio

    @tabRatio.setter
    def tabRatio(self, tabRatio: str):
        self.__tabRatio = tabRatio


    @property
    def hideVerticalScrollBar(self):
        return self.__hideVerticalScrollBar

    @hideVerticalScrollBar.setter
    def hideVerticalScrollBar(self, hideVerticalScrollBar: str):
        self.__hideVerticalScrollBar = hideVerticalScrollBar


    @property
    def protectStructure(self):
        return self.__protectStructure

    @protectStructure.setter
    def protectStructure(self, protectStructure: str):
        self.__protectStructure = protectStructure


    @property
    def precisionAsDisplayed(self):
        return self.__precisionAsDisplayed

    @precisionAsDisplayed.setter
    def precisionAsDisplayed(self, precisionAsDisplayed: str):
        self.__precisionAsDisplayed = precisionAsDisplayed


    @property
    def activeSheet(self):
        return self.__activeSheet

    @activeSheet.setter
    def activeSheet(self, activeSheet: str):
        self.__activeSheet = activeSheet


    @property
    def createBackup(self):
        return self.__createBackup

    @createBackup.setter
    def createBackup(self, createBackup: str):
        self.__createBackup = createBackup


    @property
    def maxIterations(self):
        return self.__maxIterations

    @maxIterations.setter
    def maxIterations(self, maxIterations: str):
        self.__maxIterations = maxIterations


    @property
    def hidePivotTableFieldList(self):
        return self.__hidePivotTableFieldList

    @hidePivotTableFieldList.setter
    def hidePivotTableFieldList(self, hidePivotTableFieldList: str):
        self.__hidePivotTableFieldList = hidePivotTableFieldList


    @property
    def firstVisibleSheet(self):
        return self.__firstVisibleSheet

    @firstVisibleSheet.setter
    def firstVisibleSheet(self, firstVisibleSheet: str):
        self.__firstVisibleSheet = firstVisibleSheet


    @property
    def uncalced(self):
        return self.__uncalced

    @uncalced.setter
    def uncalced(self, uncalced: str):
        self.__uncalced = uncalced


    @property
    def windowTopY(self):
        return self.__windowTopY

    @windowTopY.setter
    def windowTopY(self, windowTopY: str):
        self.__windowTopY = windowTopY


    @property
    def hideWorkbookTabs(self):
        return self.__hideWorkbookTabs

    @hideWorkbookTabs.setter
    def hideWorkbookTabs(self, hideWorkbookTabs: str):
        self.__hideWorkbookTabs = hideWorkbookTabs


    @property
    def noAutoRecover(self):
        return self.__noAutoRecover

    @noAutoRecover.setter
    def noAutoRecover(self, noAutoRecover: str):
        self.__noAutoRecover = noAutoRecover


    @property
    def selectedSheets(self):
        return self.__selectedSheets

    @selectedSheets.setter
    def selectedSheets(self, selectedSheets: str):
        self.__selectedSheets = selectedSheets


    @property
    def displayDrawingObjects(self):
        return self.__displayDrawingObjects

    @displayDrawingObjects.setter
    def displayDrawingObjects(self, displayDrawingObjects: str):
        self.__displayDrawingObjects = displayDrawingObjects


    @property
    def doNotCalculateBeforeSave(self):
        return self.__doNotCalculateBeforeSave

    @doNotCalculateBeforeSave.setter
    def doNotCalculateBeforeSave(self, doNotCalculateBeforeSave: str):
        self.__doNotCalculateBeforeSave = doNotCalculateBeforeSave


    @property
    def hideHorizontalScrollBar(self):
        return self.__hideHorizontalScrollBar

    @hideHorizontalScrollBar.setter
    def hideHorizontalScrollBar(self, hideHorizontalScrollBar: str):
        self.__hideHorizontalScrollBar = hideHorizontalScrollBar


    @property
    def acceptLabelsInFormulas(self):
        return self.__acceptLabelsInFormulas

    @acceptLabelsInFormulas.setter
    def acceptLabelsInFormulas(self, acceptLabelsInFormulas: str):
        self.__acceptLabelsInFormulas = acceptLabelsInFormulas


    @property
    def windowHeight(self):
        return self.__windowHeight

    @windowHeight.setter
    def windowHeight(self, windowHeight: str):
        self.__windowHeight = windowHeight


    @property
    def windowIconic(self):
        return self.__windowIconic

    @windowIconic.setter
    def windowIconic(self, windowIconic: str):
        self.__windowIconic = windowIconic


    @property
    def futureVer(self):
        return self.__futureVer

    @futureVer.setter
    def futureVer(self, futureVer: str):
        self.__futureVer = futureVer


    @property
    def calculation(self):
        return self.__calculation

    @calculation.setter
    def calculation(self, calculation: str):
        self.__calculation = calculation


    @property
    def wb_excelWorkbook(self):
        return self.__wb_excelWorkbook

    @wb_excelWorkbook.setter
    def wb_excelWorkbook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_ExcelWorkbook__wb_excelWorkbook", None)
        self.__wb_excelWorkbook = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workbook62"):
                opp_val = getattr(old_value, "Workbook62", None)
                if opp_val == self:
                    setattr(old_value, "Workbook62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workbook62"):
                opp_val = getattr(value, "Workbook62", None)
                setattr(value, "Workbook62", self)

class SpreadsheetMLWorksheetOpt_Comment:

    def __init__(self, author: str, showAlways: str, c_comment: "Cell" = None, d_comment: "Data" = None):
        self.author = author
        self.showAlways = showAlways
        self.c_comment = c_comment
        self.d_comment = d_comment
        
        pass
    @property
    def showAlways(self):
        return self.__showAlways

    @showAlways.setter
    def showAlways(self, showAlways: str):
        self.__showAlways = showAlways


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def d_comment(self):
        return self.__d_comment

    @d_comment.setter
    def d_comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Comment__d_comment", None)
        self.__d_comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data54"):
                opp_val = getattr(old_value, "Data54", None)
                if opp_val == self:
                    setattr(old_value, "Data54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data54"):
                opp_val = getattr(value, "Data54", None)
                setattr(value, "Data54", self)

    @property
    def c_comment(self):
        return self.__c_comment

    @c_comment.setter
    def c_comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Comment__c_comment", None)
        self.__c_comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cell52"):
                opp_val = getattr(old_value, "Cell52", None)
                if opp_val == self:
                    setattr(old_value, "Cell52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cell52"):
                opp_val = getattr(value, "Cell52", None)
                setattr(value, "Cell52", self)

class Comment:

    pass
class ColOrRowElement:

    pass
class SpreadsheetMLWorksheetOpt_Row(ColOrRowElement):

    def __init__(self, autoFitHeight: str, height: str, t_rows: "Table" = None, c_row: set["Cell"] = None):
        self.autoFitHeight = autoFitHeight
        self.height = height
        self.t_rows = t_rows
        self.c_row = c_row if c_row is not None else set()
        
        pass
    @property
    def autoFitHeight(self):
        return self.__autoFitHeight

    @autoFitHeight.setter
    def autoFitHeight(self, autoFitHeight: str):
        self.__autoFitHeight = autoFitHeight


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def t_rows(self):
        return self.__t_rows

    @t_rows.setter
    def t_rows(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Row__t_rows", None)
        self.__t_rows = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table41"):
                opp_val = getattr(old_value, "Table41", None)
                if opp_val == self:
                    setattr(old_value, "Table41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table41"):
                opp_val = getattr(value, "Table41", None)
                setattr(value, "Table41", self)

    @property
    def c_row(self):
        return self.__c_row

    @c_row.setter
    def c_row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Row__c_row", None)
        self.__c_row = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cell43"):
                    opp_val = getattr(item, "Cell43", None)
                    
                    if opp_val == self:
                        setattr(item, "Cell43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cell43"):
                    opp_val = getattr(item, "Cell43", None)
                    
                    setattr(item, "Cell43", self)
                    

class SpreadsheetMLWorksheetOpt_Column(ColOrRowElement):

    def __init__(self, autoFitWidth: str, width: str, t_cols: "Table" = None):
        self.autoFitWidth = autoFitWidth
        self.width = width
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
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Column__t_cols", None)
        self.__t_cols = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table39"):
                opp_val = getattr(old_value, "Table39", None)
                if opp_val == self:
                    setattr(old_value, "Table39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table39"):
                opp_val = getattr(value, "Table39", None)
                setattr(value, "Table39", self)

class TableElement:

    pass
class SpreadsheetMLWorksheetOpt_Cell(TableElement):

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
    def hRef(self):
        return self.__hRef

    @hRef.setter
    def hRef(self, hRef: str):
        self.__hRef = hRef


    @property
    def mergeDown(self):
        return self.__mergeDown

    @mergeDown.setter
    def mergeDown(self, mergeDown: str):
        self.__mergeDown = mergeDown


    @property
    def mergeAcross(self):
        return self.__mergeAcross

    @mergeAcross.setter
    def mergeAcross(self, mergeAcross: str):
        self.__mergeAcross = mergeAcross


    @property
    def c_cell(self):
        return self.__c_cell

    @c_cell.setter
    def c_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Cell__c_cell", None)
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

    @property
    def r_cells(self):
        return self.__r_cells

    @r_cells.setter
    def r_cells(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Cell__r_cells", None)
        self.__r_cells = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Row47"):
                opp_val = getattr(old_value, "Row47", None)
                if opp_val == self:
                    setattr(old_value, "Row47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Row47"):
                opp_val = getattr(value, "Row47", None)
                setattr(value, "Row47", self)

    @property
    def st_cell(self):
        return self.__st_cell

    @st_cell.setter
    def st_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Cell__st_cell", None)
        self.__st_cell = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmartTagsCollection45"):
                    opp_val = getattr(item, "SmartTagsCollection45", None)
                    
                    if opp_val == self:
                        setattr(item, "SmartTagsCollection45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmartTagsCollection45"):
                    opp_val = getattr(item, "SmartTagsCollection45", None)
                    
                    setattr(item, "SmartTagsCollection45", self)
                    

    @property
    def d_cell(self):
        return self.__d_cell

    @d_cell.setter
    def d_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Cell__d_cell", None)
        self.__d_cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data49"):
                opp_val = getattr(old_value, "Data49", None)
                if opp_val == self:
                    setattr(old_value, "Data49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data49"):
                opp_val = getattr(value, "Data49", None)
                setattr(value, "Data49", self)

class SpreadsheetMLWorksheetOpt_ColOrRowElement(TableElement):

    def __init__(self, hidden: str, span: str):
        self.hidden = hidden
        self.span = span
        
        pass
    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: str):
        self.__hidden = hidden


    @property
    def span(self):
        return self.__span

    @span.setter
    def span(self, span: str):
        self.__span = span


class Column:

    pass
class StyledElement:

    pass
class SpreadsheetMLWorksheetOpt_TableElement(StyledElement):

    def __init__(self, index: str):
        self.index = index
        
        pass
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index


class SpreadsheetMLWorksheetOpt_Table(StyledElement):

    def __init__(self, defaultColumnWidth: str, defaultRowHeight: str, expandedColumnCount: str, expandedRowCount: str, leftCell: str, topCell: str, fullColumns: str, fullRows: str, r_table: set["Row"] = None, ws_table: "Worksheet" = None, c_table: set["Column"] = None):
        self.defaultColumnWidth = defaultColumnWidth
        self.defaultRowHeight = defaultRowHeight
        self.expandedColumnCount = expandedColumnCount
        self.expandedRowCount = expandedRowCount
        self.leftCell = leftCell
        self.topCell = topCell
        self.fullColumns = fullColumns
        self.fullRows = fullRows
        self.r_table = r_table if r_table is not None else set()
        self.ws_table = ws_table
        self.c_table = c_table if c_table is not None else set()
        
        pass
    @property
    def leftCell(self):
        return self.__leftCell

    @leftCell.setter
    def leftCell(self, leftCell: str):
        self.__leftCell = leftCell


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
    def defaultRowHeight(self):
        return self.__defaultRowHeight

    @defaultRowHeight.setter
    def defaultRowHeight(self, defaultRowHeight: str):
        self.__defaultRowHeight = defaultRowHeight


    @property
    def expandedColumnCount(self):
        return self.__expandedColumnCount

    @expandedColumnCount.setter
    def expandedColumnCount(self, expandedColumnCount: str):
        self.__expandedColumnCount = expandedColumnCount


    @property
    def expandedRowCount(self):
        return self.__expandedRowCount

    @expandedRowCount.setter
    def expandedRowCount(self, expandedRowCount: str):
        self.__expandedRowCount = expandedRowCount


    @property
    def defaultColumnWidth(self):
        return self.__defaultColumnWidth

    @defaultColumnWidth.setter
    def defaultColumnWidth(self, defaultColumnWidth: str):
        self.__defaultColumnWidth = defaultColumnWidth


    @property
    def fullColumns(self):
        return self.__fullColumns

    @fullColumns.setter
    def fullColumns(self, fullColumns: str):
        self.__fullColumns = fullColumns


    @property
    def ws_table(self):
        return self.__ws_table

    @ws_table.setter
    def ws_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Table__ws_table", None)
        self.__ws_table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Worksheet35"):
                opp_val = getattr(old_value, "Worksheet35", None)
                if opp_val == self:
                    setattr(old_value, "Worksheet35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Worksheet35"):
                opp_val = getattr(value, "Worksheet35", None)
                setattr(value, "Worksheet35", self)

    @property
    def c_table(self):
        return self.__c_table

    @c_table.setter
    def c_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Table__c_table", None)
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
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Table__r_table", None)
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
                    

class SpreadsheetMLWorksheetOpt_StyledElement(ABC):

    pass
class Row:

    pass
class SpreadsheetMLWorksheetOpt_Worksheet:

    def __init__(self, name: str, protected: str, rightToLeft: str, t_worksheet: "Table" = None, wo_worksheet: "WorksheetOptionsElt" = None, wb_worksheets: "Workbook" = None):
        self.name = name
        self.protected = protected
        self.rightToLeft = rightToLeft
        self.t_worksheet = t_worksheet
        self.wo_worksheet = wo_worksheet
        self.wb_worksheets = wb_worksheets
        
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
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Worksheet__wb_worksheets", None)
        self.__wb_worksheets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workbook31"):
                opp_val = getattr(old_value, "Workbook31", None)
                if opp_val == self:
                    setattr(old_value, "Workbook31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workbook31"):
                opp_val = getattr(value, "Workbook31", None)
                setattr(value, "Workbook31", self)

    @property
    def t_worksheet(self):
        return self.__t_worksheet

    @t_worksheet.setter
    def t_worksheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Worksheet__t_worksheet", None)
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

    @property
    def wo_worksheet(self):
        return self.__wo_worksheet

    @wo_worksheet.setter
    def wo_worksheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_Worksheet__wo_worksheet", None)
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

class Worksheet:

    pass
class WorksheetOptionsElt:

    pass
class Table:

    pass
class SpreadsheetMLWorksheetOpt_Workbook:

    pass
class SmartTagType:

    pass
class Cell:

    pass
class ExcelWorkbook:

    pass
class SpreadsheetMLWorksheetOpt_SmartTagsCollection:

    pass
class DocumentPropertiesCollection:

    pass
class SpreadsheetMLWorksheetOpt_SmartTagType:

    def __init__(self, namespaceuri: str, name: str, url: str, smartTagTypes: "SmartTagsCollection" = None):
        self.namespaceuri = namespaceuri
        self.name = name
        self.url = url
        self.smartTagTypes = smartTagTypes
        
        pass
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
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def smartTagTypes(self):
        return self.__smartTagTypes

    @smartTagTypes.setter
    def smartTagTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_SmartTagType__smartTagTypes", None)
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

class CustomDocumentPropertiesCollection:

    pass
class SpreadsheetMLWorksheetOpt_CustomDocumentProperty:

    def __init__(self, name: str, customDocumentProperties: "CustomDocumentPropertiesCollection" = None, SpreadsheetMLWorksheetOpt_CustomDocumentProperty: "ValueType" = None):
        self.name = name
        self.customDocumentProperties = customDocumentProperties
        self.SpreadsheetMLWorksheetOpt_CustomDocumentProperty = SpreadsheetMLWorksheetOpt_CustomDocumentProperty
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def SpreadsheetMLWorksheetOpt_CustomDocumentProperty(self):
        return self.__SpreadsheetMLWorksheetOpt_CustomDocumentProperty

    @SpreadsheetMLWorksheetOpt_CustomDocumentProperty.setter
    def SpreadsheetMLWorksheetOpt_CustomDocumentProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_CustomDocumentProperty__SpreadsheetMLWorksheetOpt_CustomDocumentProperty", None)
        self.__SpreadsheetMLWorksheetOpt_CustomDocumentProperty = value
        
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

    @property
    def customDocumentProperties(self):
        return self.__customDocumentProperties

    @customDocumentProperties.setter
    def customDocumentProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_CustomDocumentProperty__customDocumentProperties", None)
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

class CustomDocumentProperty:

    pass
class SmartTagsCollection:

    pass
class SpreadsheetMLWorksheetOpt_CustomDocumentPropertiesCollection:

    pass
class VersionType:

    pass
class SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection:

    def __init__(self, title: str, subject: str, keywords: str, description: str, category: str, author: str, lastAuthor: str, manager: str, company: str, hyperlinkBase: str, appName: str, lines: str, paragraphs: str, totalTime: str, pages: str, words: str, revision: str, characters: str, presentationFormat: str, charactersWithSpaces: str, guid: str, bytes: str, wb_docProperties: "Workbook" = None, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection: "VersionType" = None, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection5: "DateTimeType" = None, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection8: "DateTimeType" = None, SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection11: "DateTimeType" = None):
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
        self.appName = appName
        self.lines = lines
        self.paragraphs = paragraphs
        self.totalTime = totalTime
        self.pages = pages
        self.words = words
        self.revision = revision
        self.characters = characters
        self.presentationFormat = presentationFormat
        self.charactersWithSpaces = charactersWithSpaces
        self.guid = guid
        self.bytes = bytes
        self.wb_docProperties = wb_docProperties
        self.SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection = SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection
        self.SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection5 = SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection5
        self.SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection8 = SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection8
        self.SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection11 = SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection11
        
        pass
    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, words: str):
        self.__words = words


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def characters(self):
        return self.__characters

    @characters.setter
    def characters(self, characters: str):
        self.__characters = characters


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
    def charactersWithSpaces(self):
        return self.__charactersWithSpaces

    @charactersWithSpaces.setter
    def charactersWithSpaces(self, charactersWithSpaces: str):
        self.__charactersWithSpaces = charactersWithSpaces


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def appName(self):
        return self.__appName

    @appName.setter
    def appName(self, appName: str):
        self.__appName = appName


    @property
    def bytes(self):
        return self.__bytes

    @bytes.setter
    def bytes(self, bytes: str):
        self.__bytes = bytes


    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager: str):
        self.__manager = manager


    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords


    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company: str):
        self.__company = company


    @property
    def hyperlinkBase(self):
        return self.__hyperlinkBase

    @hyperlinkBase.setter
    def hyperlinkBase(self, hyperlinkBase: str):
        self.__hyperlinkBase = hyperlinkBase


    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, lines: str):
        self.__lines = lines


    @property
    def presentationFormat(self):
        return self.__presentationFormat

    @presentationFormat.setter
    def presentationFormat(self, presentationFormat: str):
        self.__presentationFormat = presentationFormat


    @property
    def totalTime(self):
        return self.__totalTime

    @totalTime.setter
    def totalTime(self, totalTime: str):
        self.__totalTime = totalTime


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def lastAuthor(self):
        return self.__lastAuthor

    @lastAuthor.setter
    def lastAuthor(self, lastAuthor: str):
        self.__lastAuthor = lastAuthor


    @property
    def guid(self):
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid


    @property
    def paragraphs(self):
        return self.__paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs: str):
        self.__paragraphs = paragraphs


    @property
    def SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection5(self):
        return self.__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection5

    @SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection5.setter
    def SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection5", None)
        self.__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection5 = value
        
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
    def SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection(self):
        return self.__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection

    @SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection.setter
    def SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection", None)
        self.__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection = value
        
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

    @property
    def wb_docProperties(self):
        return self.__wb_docProperties

    @wb_docProperties.setter
    def wb_docProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection__wb_docProperties", None)
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
    def SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection8(self):
        return self.__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection8

    @SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection8.setter
    def SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection8", None)
        self.__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection8 = value
        
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
    def SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection11(self):
        return self.__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection11

    @SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection11.setter
    def SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection11", None)
        self.__SpreadsheetMLWorksheetOpt_DocumentPropertiesCollection11 = value
        
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

class Workbook:

    pass
class Data:

    pass
class SpreadsheetMLWorksheetOpt_ValueType(ABC):

    pass
class SpreadsheetMLWorksheetOpt_VersionType:

    def __init__(self, n: str, nn: str):
        self.n = n
        self.nn = nn
        
        pass
    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n: str):
        self.__n = n


    @property
    def nn(self):
        return self.__nn

    @nn.setter
    def nn(self, nn: str):
        self.__nn = nn


class DateTimeType:

    pass
class ValueType:

    pass
class SpreadsheetMLWorksheetOpt_DateTimeTypeValue(ValueType):

    pass
class SpreadsheetMLWorksheetOpt_BooleanValue(ValueType):

    def __init__(self, value: str, ValueType60: "SpreadsheetMLWorksheetOpt_Data" = None, ValueType: "SpreadsheetMLWorksheetOpt_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLWorksheetOpt_ErrorValue(ValueType):

    pass
class SpreadsheetMLWorksheetOpt_NumberValue(ValueType):

    def __init__(self, value: str, ValueType60: "SpreadsheetMLWorksheetOpt_Data" = None, ValueType: "SpreadsheetMLWorksheetOpt_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLWorksheetOpt_StringValue(ValueType):

    def __init__(self, value: str, ValueType60: "SpreadsheetMLWorksheetOpt_Data" = None, ValueType: "SpreadsheetMLWorksheetOpt_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLWorksheetOpt_DateTimeType:

    def __init__(self, year: str, month: str, day: str, hour: str, minute: str, second: str):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        
        pass
    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute: str):
        self.__minute = minute


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day


    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: str):
        self.__second = second


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: str):
        self.__hour = hour


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

