from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CalculationWorkbookType(Enum):
    cwt_automaticCalculation = "cwt_automaticCalculation"
    cwt_manualCalculation = "cwt_manualCalculation"
    cwt_semiAutomaticCalculation = "cwt_semiAutomaticCalculation"
class DisplayDrawingObjectsType(Enum):
    ddot_displayShapes = "ddot_displayShapes"
    ddot_placeHolders = "ddot_placeHolders"
    ddot_hideAll = "ddot_hideAll"


############################################
# Definition of Classes
############################################

class SpreadsheetMLWorkbookProp_ExcelWorkbook:

    def __init__(self, selectedSheets: str, windowHidden: str, hideHorizontalScrollBar: str, hideVerticalScrollBar: str, hideWorkbookTabs: str, windowHeight: str, protectStructure: str, protectWindows: str, displayInkNotes: str, embedSaveSmartTags: str, futureVer: str, windowWidth: str, windowTopX: str, windowTopY: str, activeSheet: str, activeChart: str, firstVisibleSheet: str, hidePivotTableFieldList: str, iteration: str, maxIterations: str, maxChange: str, precisionAsDisplayed: str, doNotSaveLinkValues: str, noAutoRecover: str, tabRatio: str, acceptLabelsInFormulas: str, windowIconic: str, displayDrawingObjects: str, createBackup: str, calculation: str, doNotCalculateBeforeSave: str, date1904: str, refModeR1C1: str, uncalced: str, wb_excelWorkbook: "Workbook" = None):
        self.selectedSheets = selectedSheets
        self.windowHidden = windowHidden
        self.hideHorizontalScrollBar = hideHorizontalScrollBar
        self.hideVerticalScrollBar = hideVerticalScrollBar
        self.hideWorkbookTabs = hideWorkbookTabs
        self.windowHeight = windowHeight
        self.protectStructure = protectStructure
        self.protectWindows = protectWindows
        self.displayInkNotes = displayInkNotes
        self.embedSaveSmartTags = embedSaveSmartTags
        self.futureVer = futureVer
        self.windowWidth = windowWidth
        self.windowTopX = windowTopX
        self.windowTopY = windowTopY
        self.activeSheet = activeSheet
        self.activeChart = activeChart
        self.firstVisibleSheet = firstVisibleSheet
        self.hidePivotTableFieldList = hidePivotTableFieldList
        self.iteration = iteration
        self.maxIterations = maxIterations
        self.maxChange = maxChange
        self.precisionAsDisplayed = precisionAsDisplayed
        self.doNotSaveLinkValues = doNotSaveLinkValues
        self.noAutoRecover = noAutoRecover
        self.tabRatio = tabRatio
        self.acceptLabelsInFormulas = acceptLabelsInFormulas
        self.windowIconic = windowIconic
        self.displayDrawingObjects = displayDrawingObjects
        self.createBackup = createBackup
        self.calculation = calculation
        self.doNotCalculateBeforeSave = doNotCalculateBeforeSave
        self.date1904 = date1904
        self.refModeR1C1 = refModeR1C1
        self.uncalced = uncalced
        self.wb_excelWorkbook = wb_excelWorkbook
        
        pass
    @property
    def noAutoRecover(self):
        return self.__noAutoRecover

    @noAutoRecover.setter
    def noAutoRecover(self, noAutoRecover: str):
        self.__noAutoRecover = noAutoRecover


    @property
    def activeSheet(self):
        return self.__activeSheet

    @activeSheet.setter
    def activeSheet(self, activeSheet: str):
        self.__activeSheet = activeSheet


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
    def maxChange(self):
        return self.__maxChange

    @maxChange.setter
    def maxChange(self, maxChange: str):
        self.__maxChange = maxChange


    @property
    def futureVer(self):
        return self.__futureVer

    @futureVer.setter
    def futureVer(self, futureVer: str):
        self.__futureVer = futureVer


    @property
    def precisionAsDisplayed(self):
        return self.__precisionAsDisplayed

    @precisionAsDisplayed.setter
    def precisionAsDisplayed(self, precisionAsDisplayed: str):
        self.__precisionAsDisplayed = precisionAsDisplayed


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
    def uncalced(self):
        return self.__uncalced

    @uncalced.setter
    def uncalced(self, uncalced: str):
        self.__uncalced = uncalced


    @property
    def doNotSaveLinkValues(self):
        return self.__doNotSaveLinkValues

    @doNotSaveLinkValues.setter
    def doNotSaveLinkValues(self, doNotSaveLinkValues: str):
        self.__doNotSaveLinkValues = doNotSaveLinkValues


    @property
    def windowTopX(self):
        return self.__windowTopX

    @windowTopX.setter
    def windowTopX(self, windowTopX: str):
        self.__windowTopX = windowTopX


    @property
    def tabRatio(self):
        return self.__tabRatio

    @tabRatio.setter
    def tabRatio(self, tabRatio: str):
        self.__tabRatio = tabRatio


    @property
    def hidePivotTableFieldList(self):
        return self.__hidePivotTableFieldList

    @hidePivotTableFieldList.setter
    def hidePivotTableFieldList(self, hidePivotTableFieldList: str):
        self.__hidePivotTableFieldList = hidePivotTableFieldList


    @property
    def protectWindows(self):
        return self.__protectWindows

    @protectWindows.setter
    def protectWindows(self, protectWindows: str):
        self.__protectWindows = protectWindows


    @property
    def protectStructure(self):
        return self.__protectStructure

    @protectStructure.setter
    def protectStructure(self, protectStructure: str):
        self.__protectStructure = protectStructure


    @property
    def hideHorizontalScrollBar(self):
        return self.__hideHorizontalScrollBar

    @hideHorizontalScrollBar.setter
    def hideHorizontalScrollBar(self, hideHorizontalScrollBar: str):
        self.__hideHorizontalScrollBar = hideHorizontalScrollBar


    @property
    def firstVisibleSheet(self):
        return self.__firstVisibleSheet

    @firstVisibleSheet.setter
    def firstVisibleSheet(self, firstVisibleSheet: str):
        self.__firstVisibleSheet = firstVisibleSheet


    @property
    def calculation(self):
        return self.__calculation

    @calculation.setter
    def calculation(self, calculation: str):
        self.__calculation = calculation


    @property
    def iteration(self):
        return self.__iteration

    @iteration.setter
    def iteration(self, iteration: str):
        self.__iteration = iteration


    @property
    def windowIconic(self):
        return self.__windowIconic

    @windowIconic.setter
    def windowIconic(self, windowIconic: str):
        self.__windowIconic = windowIconic


    @property
    def refModeR1C1(self):
        return self.__refModeR1C1

    @refModeR1C1.setter
    def refModeR1C1(self, refModeR1C1: str):
        self.__refModeR1C1 = refModeR1C1


    @property
    def maxIterations(self):
        return self.__maxIterations

    @maxIterations.setter
    def maxIterations(self, maxIterations: str):
        self.__maxIterations = maxIterations


    @property
    def createBackup(self):
        return self.__createBackup

    @createBackup.setter
    def createBackup(self, createBackup: str):
        self.__createBackup = createBackup


    @property
    def windowHidden(self):
        return self.__windowHidden

    @windowHidden.setter
    def windowHidden(self, windowHidden: str):
        self.__windowHidden = windowHidden


    @property
    def date1904(self):
        return self.__date1904

    @date1904.setter
    def date1904(self, date1904: str):
        self.__date1904 = date1904


    @property
    def windowWidth(self):
        return self.__windowWidth

    @windowWidth.setter
    def windowWidth(self, windowWidth: str):
        self.__windowWidth = windowWidth


    @property
    def windowHeight(self):
        return self.__windowHeight

    @windowHeight.setter
    def windowHeight(self, windowHeight: str):
        self.__windowHeight = windowHeight


    @property
    def embedSaveSmartTags(self):
        return self.__embedSaveSmartTags

    @embedSaveSmartTags.setter
    def embedSaveSmartTags(self, embedSaveSmartTags: str):
        self.__embedSaveSmartTags = embedSaveSmartTags


    @property
    def activeChart(self):
        return self.__activeChart

    @activeChart.setter
    def activeChart(self, activeChart: str):
        self.__activeChart = activeChart


    @property
    def doNotCalculateBeforeSave(self):
        return self.__doNotCalculateBeforeSave

    @doNotCalculateBeforeSave.setter
    def doNotCalculateBeforeSave(self, doNotCalculateBeforeSave: str):
        self.__doNotCalculateBeforeSave = doNotCalculateBeforeSave


    @property
    def displayInkNotes(self):
        return self.__displayInkNotes

    @displayInkNotes.setter
    def displayInkNotes(self, displayInkNotes: str):
        self.__displayInkNotes = displayInkNotes


    @property
    def acceptLabelsInFormulas(self):
        return self.__acceptLabelsInFormulas

    @acceptLabelsInFormulas.setter
    def acceptLabelsInFormulas(self, acceptLabelsInFormulas: str):
        self.__acceptLabelsInFormulas = acceptLabelsInFormulas


    @property
    def hideVerticalScrollBar(self):
        return self.__hideVerticalScrollBar

    @hideVerticalScrollBar.setter
    def hideVerticalScrollBar(self, hideVerticalScrollBar: str):
        self.__hideVerticalScrollBar = hideVerticalScrollBar


    @property
    def wb_excelWorkbook(self):
        return self.__wb_excelWorkbook

    @wb_excelWorkbook.setter
    def wb_excelWorkbook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_ExcelWorkbook__wb_excelWorkbook", None)
        self.__wb_excelWorkbook = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workbook61"):
                opp_val = getattr(old_value, "Workbook61", None)
                if opp_val == self:
                    setattr(old_value, "Workbook61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workbook61"):
                opp_val = getattr(value, "Workbook61", None)
                setattr(value, "Workbook61", self)

class SpreadsheetMLWorkbookProp_Comment:

    def __init__(self, author: str, showAlways: str, d_comment: "Data" = None, c_comment: "Cell" = None):
        self.author = author
        self.showAlways = showAlways
        self.d_comment = d_comment
        self.c_comment = c_comment
        
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
    def c_comment(self):
        return self.__c_comment

    @c_comment.setter
    def c_comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Comment__c_comment", None)
        self.__c_comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cell51"):
                opp_val = getattr(old_value, "Cell51", None)
                if opp_val == self:
                    setattr(old_value, "Cell51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cell51"):
                opp_val = getattr(value, "Cell51", None)
                setattr(value, "Cell51", self)

    @property
    def d_comment(self):
        return self.__d_comment

    @d_comment.setter
    def d_comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Comment__d_comment", None)
        self.__d_comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data53"):
                opp_val = getattr(old_value, "Data53", None)
                if opp_val == self:
                    setattr(old_value, "Data53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data53"):
                opp_val = getattr(value, "Data53", None)
                setattr(value, "Data53", self)

class Comment:

    pass
class SpreadsheetMLWorkbookProp_Data:

    pass
class TableElement:

    pass
class SpreadsheetMLWorkbookProp_Cell(TableElement):

    def __init__(self, arrayRange: str, formula: str, hRef: str, mergeAcross: str, mergeDown: str, r_cells: "Row" = None, st_cell: set["SmartTagsCollection"] = None, d_cell: "Data" = None, c_cell: "Comment" = None):
        self.arrayRange = arrayRange
        self.formula = formula
        self.hRef = hRef
        self.mergeAcross = mergeAcross
        self.mergeDown = mergeDown
        self.r_cells = r_cells
        self.st_cell = st_cell if st_cell is not None else set()
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
    def mergeAcross(self):
        return self.__mergeAcross

    @mergeAcross.setter
    def mergeAcross(self, mergeAcross: str):
        self.__mergeAcross = mergeAcross


    @property
    def mergeDown(self):
        return self.__mergeDown

    @mergeDown.setter
    def mergeDown(self, mergeDown: str):
        self.__mergeDown = mergeDown


    @property
    def hRef(self):
        return self.__hRef

    @hRef.setter
    def hRef(self, hRef: str):
        self.__hRef = hRef


    @property
    def d_cell(self):
        return self.__d_cell

    @d_cell.setter
    def d_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Cell__d_cell", None)
        self.__d_cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data48"):
                opp_val = getattr(old_value, "Data48", None)
                if opp_val == self:
                    setattr(old_value, "Data48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data48"):
                opp_val = getattr(value, "Data48", None)
                setattr(value, "Data48", self)

    @property
    def r_cells(self):
        return self.__r_cells

    @r_cells.setter
    def r_cells(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Cell__r_cells", None)
        self.__r_cells = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Row46"):
                opp_val = getattr(old_value, "Row46", None)
                if opp_val == self:
                    setattr(old_value, "Row46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Row46"):
                opp_val = getattr(value, "Row46", None)
                setattr(value, "Row46", self)

    @property
    def c_cell(self):
        return self.__c_cell

    @c_cell.setter
    def c_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Cell__c_cell", None)
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
    def st_cell(self):
        return self.__st_cell

    @st_cell.setter
    def st_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Cell__st_cell", None)
        self.__st_cell = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmartTagsCollection44"):
                    opp_val = getattr(item, "SmartTagsCollection44", None)
                    
                    if opp_val == self:
                        setattr(item, "SmartTagsCollection44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmartTagsCollection44"):
                    opp_val = getattr(item, "SmartTagsCollection44", None)
                    
                    setattr(item, "SmartTagsCollection44", self)
                    

class SpreadsheetMLWorkbookProp_ColOrRowElement(TableElement):

    def __init__(self, span: str, hidden: str):
        self.span = span
        self.hidden = hidden
        
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


class ColOrRowElement:

    pass
class SpreadsheetMLWorkbookProp_Row(ColOrRowElement):

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
    def c_row(self):
        return self.__c_row

    @c_row.setter
    def c_row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Row__c_row", None)
        self.__c_row = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cell42"):
                    opp_val = getattr(item, "Cell42", None)
                    
                    if opp_val == self:
                        setattr(item, "Cell42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cell42"):
                    opp_val = getattr(item, "Cell42", None)
                    
                    setattr(item, "Cell42", self)
                    

    @property
    def t_rows(self):
        return self.__t_rows

    @t_rows.setter
    def t_rows(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Row__t_rows", None)
        self.__t_rows = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table40"):
                opp_val = getattr(old_value, "Table40", None)
                if opp_val == self:
                    setattr(old_value, "Table40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table40"):
                opp_val = getattr(value, "Table40", None)
                setattr(value, "Table40", self)

class SpreadsheetMLWorkbookProp_Column(ColOrRowElement):

    def __init__(self, autoFitWidth: str, width: str, t_cols: "Table" = None):
        self.autoFitWidth = autoFitWidth
        self.width = width
        self.t_cols = t_cols
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def autoFitWidth(self):
        return self.__autoFitWidth

    @autoFitWidth.setter
    def autoFitWidth(self, autoFitWidth: str):
        self.__autoFitWidth = autoFitWidth


    @property
    def t_cols(self):
        return self.__t_cols

    @t_cols.setter
    def t_cols(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Column__t_cols", None)
        self.__t_cols = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table38"):
                opp_val = getattr(old_value, "Table38", None)
                if opp_val == self:
                    setattr(old_value, "Table38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table38"):
                opp_val = getattr(value, "Table38", None)
                setattr(value, "Table38", self)

class Column:

    pass
class StyledElement:

    pass
class SpreadsheetMLWorkbookProp_TableElement(StyledElement):

    def __init__(self, index: str):
        self.index = index
        
        pass
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index


class SpreadsheetMLWorkbookProp_Table(StyledElement):

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
    def defaultRowHeight(self):
        return self.__defaultRowHeight

    @defaultRowHeight.setter
    def defaultRowHeight(self, defaultRowHeight: str):
        self.__defaultRowHeight = defaultRowHeight


    @property
    def fullRows(self):
        return self.__fullRows

    @fullRows.setter
    def fullRows(self, fullRows: str):
        self.__fullRows = fullRows


    @property
    def expandedColumnCount(self):
        return self.__expandedColumnCount

    @expandedColumnCount.setter
    def expandedColumnCount(self, expandedColumnCount: str):
        self.__expandedColumnCount = expandedColumnCount


    @property
    def topCell(self):
        return self.__topCell

    @topCell.setter
    def topCell(self, topCell: str):
        self.__topCell = topCell


    @property
    def expandedRowCount(self):
        return self.__expandedRowCount

    @expandedRowCount.setter
    def expandedRowCount(self, expandedRowCount: str):
        self.__expandedRowCount = expandedRowCount


    @property
    def leftCell(self):
        return self.__leftCell

    @leftCell.setter
    def leftCell(self, leftCell: str):
        self.__leftCell = leftCell


    @property
    def fullColumns(self):
        return self.__fullColumns

    @fullColumns.setter
    def fullColumns(self, fullColumns: str):
        self.__fullColumns = fullColumns


    @property
    def defaultColumnWidth(self):
        return self.__defaultColumnWidth

    @defaultColumnWidth.setter
    def defaultColumnWidth(self, defaultColumnWidth: str):
        self.__defaultColumnWidth = defaultColumnWidth


    @property
    def r_table(self):
        return self.__r_table

    @r_table.setter
    def r_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Table__r_table", None)
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
                    

    @property
    def c_table(self):
        return self.__c_table

    @c_table.setter
    def c_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Table__c_table", None)
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
    def ws_table(self):
        return self.__ws_table

    @ws_table.setter
    def ws_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Table__ws_table", None)
        self.__ws_table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Worksheet34"):
                opp_val = getattr(old_value, "Worksheet34", None)
                if opp_val == self:
                    setattr(old_value, "Worksheet34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Worksheet34"):
                opp_val = getattr(value, "Worksheet34", None)
                setattr(value, "Worksheet34", self)

class SpreadsheetMLWorkbookProp_StyledElement(ABC):

    pass
class Table:

    pass
class Row:

    pass
class ExcelWorkbook:

    pass
class DocumentPropertiesCollection:

    pass
class SpreadsheetMLWorkbookProp_Workbook:

    pass
class SmartTagType:

    pass
class SpreadsheetMLWorkbookProp_Worksheet:

    def __init__(self, name: str, wb_worksheets: "Workbook" = None, t_worksheet: "Table" = None):
        self.name = name
        self.wb_worksheets = wb_worksheets
        self.t_worksheet = t_worksheet
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def t_worksheet(self):
        return self.__t_worksheet

    @t_worksheet.setter
    def t_worksheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Worksheet__t_worksheet", None)
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
    def wb_worksheets(self):
        return self.__wb_worksheets

    @wb_worksheets.setter
    def wb_worksheets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_Worksheet__wb_worksheets", None)
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

class Worksheet:

    pass
class SpreadsheetMLWorkbookProp_SmartTagsCollection:

    pass
class SmartTagsCollection:

    pass
class SpreadsheetMLWorkbookProp_SmartTagType:

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
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_SmartTagType__smartTagTypes", None)
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
class Cell:

    pass
class SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection:

    pass
class SpreadsheetMLWorkbookProp_CustomDocumentProperty:

    def __init__(self, name: str, customDocumentProperties: "CustomDocumentPropertiesCollection" = None, SpreadsheetMLWorkbookProp_CustomDocumentProperty: "ValueType" = None):
        self.name = name
        self.customDocumentProperties = customDocumentProperties
        self.SpreadsheetMLWorkbookProp_CustomDocumentProperty = SpreadsheetMLWorkbookProp_CustomDocumentProperty
        
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
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_CustomDocumentProperty__customDocumentProperties", None)
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
    def SpreadsheetMLWorkbookProp_CustomDocumentProperty(self):
        return self.__SpreadsheetMLWorkbookProp_CustomDocumentProperty

    @SpreadsheetMLWorkbookProp_CustomDocumentProperty.setter
    def SpreadsheetMLWorkbookProp_CustomDocumentProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_CustomDocumentProperty__SpreadsheetMLWorkbookProp_CustomDocumentProperty", None)
        self.__SpreadsheetMLWorkbookProp_CustomDocumentProperty = value
        
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
class VersionType:

    pass
class Workbook:

    pass
class SpreadsheetMLWorkbookProp_DocumentPropertiesCollection:

    def __init__(self, keywords: str, title: str, subject: str, totalTime: str, description: str, category: str, author: str, lastAuthor: str, manager: str, company: str, hyperlinkBase: str, revision: str, presentationFormat: str, guid: str, appName: str, pages: str, words: str, characters: str, charactersWithSpaces: str, bytes: str, lines: str, paragraphs: str, wb_docProperties: "Workbook" = None, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5: "DateTimeType" = None, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection: "VersionType" = None, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11: "DateTimeType" = None, SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8: "DateTimeType" = None):
        self.keywords = keywords
        self.title = title
        self.subject = subject
        self.totalTime = totalTime
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
        self.pages = pages
        self.words = words
        self.characters = characters
        self.charactersWithSpaces = charactersWithSpaces
        self.bytes = bytes
        self.lines = lines
        self.paragraphs = paragraphs
        self.wb_docProperties = wb_docProperties
        self.SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5 = SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5
        self.SpreadsheetMLWorkbookProp_DocumentPropertiesCollection = SpreadsheetMLWorkbookProp_DocumentPropertiesCollection
        self.SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11 = SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11
        self.SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8 = SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8
        
        pass
    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject


    @property
    def charactersWithSpaces(self):
        return self.__charactersWithSpaces

    @charactersWithSpaces.setter
    def charactersWithSpaces(self, charactersWithSpaces: str):
        self.__charactersWithSpaces = charactersWithSpaces


    @property
    def characters(self):
        return self.__characters

    @characters.setter
    def characters(self, characters: str):
        self.__characters = characters


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


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
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, lines: str):
        self.__lines = lines


    @property
    def paragraphs(self):
        return self.__paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs: str):
        self.__paragraphs = paragraphs


    @property
    def presentationFormat(self):
        return self.__presentationFormat

    @presentationFormat.setter
    def presentationFormat(self, presentationFormat: str):
        self.__presentationFormat = presentationFormat


    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager: str):
        self.__manager = manager


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def bytes(self):
        return self.__bytes

    @bytes.setter
    def bytes(self, bytes: str):
        self.__bytes = bytes


    @property
    def lastAuthor(self):
        return self.__lastAuthor

    @lastAuthor.setter
    def lastAuthor(self, lastAuthor: str):
        self.__lastAuthor = lastAuthor


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def guid(self):
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid


    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


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
    def revision(self):
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision


    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, words: str):
        self.__words = words


    @property
    def SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5(self):
        return self.__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5

    @SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5.setter
    def SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_DocumentPropertiesCollection__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5", None)
        self.__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection5 = value
        
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
    def SpreadsheetMLWorkbookProp_DocumentPropertiesCollection(self):
        return self.__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection

    @SpreadsheetMLWorkbookProp_DocumentPropertiesCollection.setter
    def SpreadsheetMLWorkbookProp_DocumentPropertiesCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_DocumentPropertiesCollection__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection", None)
        self.__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection = value
        
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
    def SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8(self):
        return self.__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8

    @SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8.setter
    def SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_DocumentPropertiesCollection__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8", None)
        self.__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection8 = value
        
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
    def SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11(self):
        return self.__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11

    @SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11.setter
    def SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_DocumentPropertiesCollection__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11", None)
        self.__SpreadsheetMLWorkbookProp_DocumentPropertiesCollection11 = value
        
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
        old_value = getattr(self, f"_SpreadsheetMLWorkbookProp_DocumentPropertiesCollection__wb_docProperties", None)
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

class DateTimeType:

    pass
class ValueType:

    pass
class SpreadsheetMLWorkbookProp_DateTimeTypeValue(ValueType):

    pass
class SpreadsheetMLWorkbookProp_BooleanValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLWorkbookProp_CustomDocumentProperty" = None, ValueType59: "SpreadsheetMLWorkbookProp_Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLWorkbookProp_NumberValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLWorkbookProp_CustomDocumentProperty" = None, ValueType59: "SpreadsheetMLWorkbookProp_Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLWorkbookProp_ErrorValue(ValueType):

    pass
class SpreadsheetMLWorkbookProp_StringValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLWorkbookProp_CustomDocumentProperty" = None, ValueType59: "SpreadsheetMLWorkbookProp_Data" = None):
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
class SpreadsheetMLWorkbookProp_ValueType(ABC):

    pass
class SpreadsheetMLWorkbookProp_VersionType:

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


class SpreadsheetMLWorkbookProp_DateTimeType:

    def __init__(self, hour: str, minute: str, year: str, month: str, day: str, second: str):
        self.hour = hour
        self.minute = minute
        self.year = year
        self.month = month
        self.day = day
        self.second = second
        
        pass
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
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: str):
        self.__hour = hour


    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: str):
        self.__second = second


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

