from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DisplayDrawingObjectsType(Enum):
    ddot_displayShapes = "ddot_displayShapes"
    ddot_placeHolders = "ddot_placeHolders"
    ddot_hideAll = "ddot_hideAll"
class CommentsLayoutType(Enum):
    clt_InPlace = "clt_InPlace"
    clt_PrintNone = "clt_PrintNone"
    clt_SheetEnd = "clt_SheetEnd"
class CalculationWorkbookType(Enum):
    cwt_automaticCalculation = "cwt_automaticCalculation"
    cwt_manualCalculation = "cwt_manualCalculation"
    cwt_semiAutomaticCalculation = "cwt_semiAutomaticCalculation"
class ExcelWorksheetTypeType(Enum):
    ewt_Worksheet = "ewt_Worksheet"
    ewt_Chart = "ewt_Chart"
    ewt_Macro = "ewt_Macro"
    ewt_Dialog = "ewt_Dialog"
class VisibleType(Enum):
    vt_SheetVisible = "vt_SheetVisible"
    vt_SheetHidden = "vt_SheetHidden"
    vt_SheetVeryHidden = "vt_SheetVeryHidden"
class OrientationType(Enum):
    ot_Landscape = "ot_Landscape"
    ot_Portrait = "ot_Portrait"
class EnableSelectionType(Enum):
    est_UnlockedCells = "est_UnlockedCells"
    est_NoSelection = "est_NoSelection"


############################################
# Definition of Classes
############################################

class Data:

    pass
class Workbook:

    pass
class SpreadsheetMLPrintingSetup_DocumentPropertiesCollection:

    def __init__(self, revision: str, presentationFormat: str, guid: str, appName: str, totalTime: str, pages: str, words: str, characters: str, charactersWithSpaces: str, title: str, bytes: str, subject: str, lines: str, keywords: str, paragraphs: str, description: str, category: str, author: str, lastAuthor: str, manager: str, company: str, hyperlinkBase: str, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection: "VersionType" = None, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection5: "DateTimeType" = None, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection8: "DateTimeType" = None, SpreadsheetMLPrintingSetup_DocumentPropertiesCollection11: "DateTimeType" = None, wb_docProperties: "Workbook" = None):
        self.revision = revision
        self.presentationFormat = presentationFormat
        self.guid = guid
        self.appName = appName
        self.totalTime = totalTime
        self.pages = pages
        self.words = words
        self.characters = characters
        self.charactersWithSpaces = charactersWithSpaces
        self.title = title
        self.bytes = bytes
        self.subject = subject
        self.lines = lines
        self.keywords = keywords
        self.paragraphs = paragraphs
        self.description = description
        self.category = category
        self.author = author
        self.lastAuthor = lastAuthor
        self.manager = manager
        self.company = company
        self.hyperlinkBase = hyperlinkBase
        self.SpreadsheetMLPrintingSetup_DocumentPropertiesCollection = SpreadsheetMLPrintingSetup_DocumentPropertiesCollection
        self.SpreadsheetMLPrintingSetup_DocumentPropertiesCollection5 = SpreadsheetMLPrintingSetup_DocumentPropertiesCollection5
        self.SpreadsheetMLPrintingSetup_DocumentPropertiesCollection8 = SpreadsheetMLPrintingSetup_DocumentPropertiesCollection8
        self.SpreadsheetMLPrintingSetup_DocumentPropertiesCollection11 = SpreadsheetMLPrintingSetup_DocumentPropertiesCollection11
        self.wb_docProperties = wb_docProperties
        
        pass
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
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, lines: str):
        self.__lines = lines


    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject


    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, words: str):
        self.__words = words


    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company: str):
        self.__company = company


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
    def presentationFormat(self):
        return self.__presentationFormat

    @presentationFormat.setter
    def presentationFormat(self, presentationFormat: str):
        self.__presentationFormat = presentationFormat


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def characters(self):
        return self.__characters

    @characters.setter
    def characters(self, characters: str):
        self.__characters = characters


    @property
    def totalTime(self):
        return self.__totalTime

    @totalTime.setter
    def totalTime(self, totalTime: str):
        self.__totalTime = totalTime


    @property
    def bytes(self):
        return self.__bytes

    @bytes.setter
    def bytes(self, bytes: str):
        self.__bytes = bytes


    @property
    def appName(self):
        return self.__appName

    @appName.setter
    def appName(self, appName: str):
        self.__appName = appName


    @property
    def paragraphs(self):
        return self.__paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs: str):
        self.__paragraphs = paragraphs


    @property
    def charactersWithSpaces(self):
        return self.__charactersWithSpaces

    @charactersWithSpaces.setter
    def charactersWithSpaces(self, charactersWithSpaces: str):
        self.__charactersWithSpaces = charactersWithSpaces


    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


    @property
    def hyperlinkBase(self):
        return self.__hyperlinkBase

    @hyperlinkBase.setter
    def hyperlinkBase(self, hyperlinkBase: str):
        self.__hyperlinkBase = hyperlinkBase


    @property
    def guid(self):
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid


    @property
    def revision(self):
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision


    @property
    def SpreadsheetMLPrintingSetup_DocumentPropertiesCollection5(self):
        return self.__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection5

    @SpreadsheetMLPrintingSetup_DocumentPropertiesCollection5.setter
    def SpreadsheetMLPrintingSetup_DocumentPropertiesCollection5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_DocumentPropertiesCollection__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection5", None)
        self.__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection5 = value
        
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
    def SpreadsheetMLPrintingSetup_DocumentPropertiesCollection8(self):
        return self.__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection8

    @SpreadsheetMLPrintingSetup_DocumentPropertiesCollection8.setter
    def SpreadsheetMLPrintingSetup_DocumentPropertiesCollection8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_DocumentPropertiesCollection__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection8", None)
        self.__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection8 = value
        
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
    def SpreadsheetMLPrintingSetup_DocumentPropertiesCollection(self):
        return self.__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection

    @SpreadsheetMLPrintingSetup_DocumentPropertiesCollection.setter
    def SpreadsheetMLPrintingSetup_DocumentPropertiesCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_DocumentPropertiesCollection__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection", None)
        self.__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection = value
        
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
    def SpreadsheetMLPrintingSetup_DocumentPropertiesCollection11(self):
        return self.__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection11

    @SpreadsheetMLPrintingSetup_DocumentPropertiesCollection11.setter
    def SpreadsheetMLPrintingSetup_DocumentPropertiesCollection11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_DocumentPropertiesCollection__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection11", None)
        self.__SpreadsheetMLPrintingSetup_DocumentPropertiesCollection11 = value
        
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
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_DocumentPropertiesCollection__wb_docProperties", None)
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
class SpreadsheetMLPrintingSetup_DateTimeType:

    def __init__(self, day: str, hour: str, minute: str, second: str, year: str, month: str):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.year = year
        self.month = month
        
        pass
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: str):
        self.__second = second


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute: str):
        self.__minute = minute


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: str):
        self.__hour = hour


class SpreadsheetMLPrintingSetup_ValueType(ABC):

    pass
class SpreadsheetMLPrintingSetup_VersionType:

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


class SpreadsheetMLPrintingSetup_PageMarginsInfo:

    def __init__(self, left: str, right: str, top: str, bottom: str, ps_pageMargins: "PageSetup" = None):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.ps_pageMargins = ps_pageMargins
        
        pass
    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, top: str):
        self.__top = top


    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left: str):
        self.__left = left


    @property
    def bottom(self):
        return self.__bottom

    @bottom.setter
    def bottom(self, bottom: str):
        self.__bottom = bottom


    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right: str):
        self.__right = right


    @property
    def ps_pageMargins(self):
        return self.__ps_pageMargins

    @ps_pageMargins.setter
    def ps_pageMargins(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_PageMarginsInfo__ps_pageMargins", None)
        self.__ps_pageMargins = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PageSetup80"):
                opp_val = getattr(old_value, "PageSetup80", None)
                if opp_val == self:
                    setattr(old_value, "PageSetup80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PageSetup80"):
                opp_val = getattr(value, "PageSetup80", None)
                setattr(value, "PageSetup80", self)

class SpreadsheetMLPrintingSetup_Print:

    def __init__(self, commentsLayout: str, scale: str, printErrors: str, validPrinterInfo: str, paperSizeIndex: str, horizontalResolution: str, fitWidth: str, fitHeight: str, leftToRight: str, blackAndWhite: str, draftQuality: str, verticalResolution: str, gridlines: str, numberOfCopies: str, rowColHeadings: str, wo_print: "WorksheetOptionsElt" = None):
        self.commentsLayout = commentsLayout
        self.scale = scale
        self.printErrors = printErrors
        self.validPrinterInfo = validPrinterInfo
        self.paperSizeIndex = paperSizeIndex
        self.horizontalResolution = horizontalResolution
        self.fitWidth = fitWidth
        self.fitHeight = fitHeight
        self.leftToRight = leftToRight
        self.blackAndWhite = blackAndWhite
        self.draftQuality = draftQuality
        self.verticalResolution = verticalResolution
        self.gridlines = gridlines
        self.numberOfCopies = numberOfCopies
        self.rowColHeadings = rowColHeadings
        self.wo_print = wo_print
        
        pass
    @property
    def printErrors(self):
        return self.__printErrors

    @printErrors.setter
    def printErrors(self, printErrors: str):
        self.__printErrors = printErrors


    @property
    def fitHeight(self):
        return self.__fitHeight

    @fitHeight.setter
    def fitHeight(self, fitHeight: str):
        self.__fitHeight = fitHeight


    @property
    def validPrinterInfo(self):
        return self.__validPrinterInfo

    @validPrinterInfo.setter
    def validPrinterInfo(self, validPrinterInfo: str):
        self.__validPrinterInfo = validPrinterInfo


    @property
    def leftToRight(self):
        return self.__leftToRight

    @leftToRight.setter
    def leftToRight(self, leftToRight: str):
        self.__leftToRight = leftToRight


    @property
    def blackAndWhite(self):
        return self.__blackAndWhite

    @blackAndWhite.setter
    def blackAndWhite(self, blackAndWhite: str):
        self.__blackAndWhite = blackAndWhite


    @property
    def verticalResolution(self):
        return self.__verticalResolution

    @verticalResolution.setter
    def verticalResolution(self, verticalResolution: str):
        self.__verticalResolution = verticalResolution


    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale


    @property
    def horizontalResolution(self):
        return self.__horizontalResolution

    @horizontalResolution.setter
    def horizontalResolution(self, horizontalResolution: str):
        self.__horizontalResolution = horizontalResolution


    @property
    def commentsLayout(self):
        return self.__commentsLayout

    @commentsLayout.setter
    def commentsLayout(self, commentsLayout: str):
        self.__commentsLayout = commentsLayout


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
    def rowColHeadings(self):
        return self.__rowColHeadings

    @rowColHeadings.setter
    def rowColHeadings(self, rowColHeadings: str):
        self.__rowColHeadings = rowColHeadings


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
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Print__wo_print", None)
        self.__wo_print = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorksheetOptionsElt82"):
                opp_val = getattr(old_value, "WorksheetOptionsElt82", None)
                if opp_val == self:
                    setattr(old_value, "WorksheetOptionsElt82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorksheetOptionsElt82"):
                opp_val = getattr(value, "WorksheetOptionsElt82", None)
                setattr(value, "WorksheetOptionsElt82", self)

class HeaderOrFooterElt:

    pass
class SpreadsheetMLPrintingSetup_Header(HeaderOrFooterElt):

    pass
class SpreadsheetMLPrintingSetup_HeaderOrFooterElt(ABC):

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


class SpreadsheetMLPrintingSetup_Footer(HeaderOrFooterElt):

    pass
class SpreadsheetMLPrintingSetup_Layout:

    def __init__(self, centerVertical: str, startPageNumber: str, orientation: str, centerHorizontal: str, ps_layout: "PageSetup" = None):
        self.centerVertical = centerVertical
        self.startPageNumber = startPageNumber
        self.orientation = orientation
        self.centerHorizontal = centerHorizontal
        self.ps_layout = ps_layout
        
        pass
    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation


    @property
    def centerHorizontal(self):
        return self.__centerHorizontal

    @centerHorizontal.setter
    def centerHorizontal(self, centerHorizontal: str):
        self.__centerHorizontal = centerHorizontal


    @property
    def centerVertical(self):
        return self.__centerVertical

    @centerVertical.setter
    def centerVertical(self, centerVertical: str):
        self.__centerVertical = centerVertical


    @property
    def startPageNumber(self):
        return self.__startPageNumber

    @startPageNumber.setter
    def startPageNumber(self, startPageNumber: str):
        self.__startPageNumber = startPageNumber


    @property
    def ps_layout(self):
        return self.__ps_layout

    @ps_layout.setter
    def ps_layout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Layout__ps_layout", None)
        self.__ps_layout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PageSetup74"):
                opp_val = getattr(old_value, "PageSetup74", None)
                if opp_val == self:
                    setattr(old_value, "PageSetup74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PageSetup74"):
                opp_val = getattr(value, "PageSetup74", None)
                setattr(value, "PageSetup74", self)

class PageMarginsInfo:

    pass
class SpreadsheetMLPrintingSetup_PageSetup:

    pass
class Footer:

    pass
class Header:

    pass
class Layout:

    pass
class PageSetup:

    pass
class Print:

    pass
class SpreadsheetMLPrintingSetup_WorksheetOptionsElt:

    def __init__(self, name: str, excelWorksheetType: str, intlMacro: str, unsynced: str, fitToPage: str, doNotDisplayColHeaders: str, doNotDisplayRowHeaders: str, gridlineColor: str, defaultRowHeight: str, defaultColumnWidth: str, standardWidth: str, visible: str, leftColumnVisible: str, displayRightToLeft: str, gridlineColorIndex: str, displayFormulas: str, doNotDisplayGridlines: str, doNotDisplayHeadings: str, doNotDisplayOutline: str, selected: str, codeName: str, displayPageBreak: str, transitionExpressionEvaluation: str, transitionFormulaEntry: str, zoom: str, pageBreakZoom: str, showPageBreakZoom: str, topRowVisible: str, topRowBottomPane: str, leftColumnRightPane: str, activePane: str, splitHorizontal: str, splitVertical: str, freezePanes: str, applyAutomaticOutlineStyles: str, noSummaryRowsBelowDetail: str, noSummaryColumnsRightDetail: str, doNotDisplayZeros: str, activeRow: str, activeColumn: str, filterOn: str, rangeSelection: str, allowSizeCols: str, allowSizeRows: str, allowInsertCols: str, allowInsertRows: str, allowInsertHyperlinks: str, frozenNoSplit: str, tabColorIndex: str, protectContentst: str, protectObjects: str, protectScenarios: str, enableSelection: str, allowFormatCells: str, allowDeleteCols: str, allowDeleteRows: str, allowSort: str, allowFilter: str, allowUsePivotTables: str, w_worksheetOptions: "Worksheet" = None, p_worksheetOptions: "Print" = None, ps_worksheetOptions: "PageSetup" = None):
        self.name = name
        self.excelWorksheetType = excelWorksheetType
        self.intlMacro = intlMacro
        self.unsynced = unsynced
        self.fitToPage = fitToPage
        self.doNotDisplayColHeaders = doNotDisplayColHeaders
        self.doNotDisplayRowHeaders = doNotDisplayRowHeaders
        self.gridlineColor = gridlineColor
        self.defaultRowHeight = defaultRowHeight
        self.defaultColumnWidth = defaultColumnWidth
        self.standardWidth = standardWidth
        self.visible = visible
        self.leftColumnVisible = leftColumnVisible
        self.displayRightToLeft = displayRightToLeft
        self.gridlineColorIndex = gridlineColorIndex
        self.displayFormulas = displayFormulas
        self.doNotDisplayGridlines = doNotDisplayGridlines
        self.doNotDisplayHeadings = doNotDisplayHeadings
        self.doNotDisplayOutline = doNotDisplayOutline
        self.selected = selected
        self.codeName = codeName
        self.displayPageBreak = displayPageBreak
        self.transitionExpressionEvaluation = transitionExpressionEvaluation
        self.transitionFormulaEntry = transitionFormulaEntry
        self.zoom = zoom
        self.pageBreakZoom = pageBreakZoom
        self.showPageBreakZoom = showPageBreakZoom
        self.topRowVisible = topRowVisible
        self.topRowBottomPane = topRowBottomPane
        self.leftColumnRightPane = leftColumnRightPane
        self.activePane = activePane
        self.splitHorizontal = splitHorizontal
        self.splitVertical = splitVertical
        self.freezePanes = freezePanes
        self.applyAutomaticOutlineStyles = applyAutomaticOutlineStyles
        self.noSummaryRowsBelowDetail = noSummaryRowsBelowDetail
        self.noSummaryColumnsRightDetail = noSummaryColumnsRightDetail
        self.doNotDisplayZeros = doNotDisplayZeros
        self.activeRow = activeRow
        self.activeColumn = activeColumn
        self.filterOn = filterOn
        self.rangeSelection = rangeSelection
        self.allowSizeCols = allowSizeCols
        self.allowSizeRows = allowSizeRows
        self.allowInsertCols = allowInsertCols
        self.allowInsertRows = allowInsertRows
        self.allowInsertHyperlinks = allowInsertHyperlinks
        self.frozenNoSplit = frozenNoSplit
        self.tabColorIndex = tabColorIndex
        self.protectContentst = protectContentst
        self.protectObjects = protectObjects
        self.protectScenarios = protectScenarios
        self.enableSelection = enableSelection
        self.allowFormatCells = allowFormatCells
        self.allowDeleteCols = allowDeleteCols
        self.allowDeleteRows = allowDeleteRows
        self.allowSort = allowSort
        self.allowFilter = allowFilter
        self.allowUsePivotTables = allowUsePivotTables
        self.w_worksheetOptions = w_worksheetOptions
        self.p_worksheetOptions = p_worksheetOptions
        self.ps_worksheetOptions = ps_worksheetOptions
        
        pass
    @property
    def displayPageBreak(self):
        return self.__displayPageBreak

    @displayPageBreak.setter
    def displayPageBreak(self, displayPageBreak: str):
        self.__displayPageBreak = displayPageBreak


    @property
    def excelWorksheetType(self):
        return self.__excelWorksheetType

    @excelWorksheetType.setter
    def excelWorksheetType(self, excelWorksheetType: str):
        self.__excelWorksheetType = excelWorksheetType


    @property
    def allowSizeCols(self):
        return self.__allowSizeCols

    @allowSizeCols.setter
    def allowSizeCols(self, allowSizeCols: str):
        self.__allowSizeCols = allowSizeCols


    @property
    def frozenNoSplit(self):
        return self.__frozenNoSplit

    @frozenNoSplit.setter
    def frozenNoSplit(self, frozenNoSplit: str):
        self.__frozenNoSplit = frozenNoSplit


    @property
    def gridlineColor(self):
        return self.__gridlineColor

    @gridlineColor.setter
    def gridlineColor(self, gridlineColor: str):
        self.__gridlineColor = gridlineColor


    @property
    def doNotDisplayRowHeaders(self):
        return self.__doNotDisplayRowHeaders

    @doNotDisplayRowHeaders.setter
    def doNotDisplayRowHeaders(self, doNotDisplayRowHeaders: str):
        self.__doNotDisplayRowHeaders = doNotDisplayRowHeaders


    @property
    def leftColumnVisible(self):
        return self.__leftColumnVisible

    @leftColumnVisible.setter
    def leftColumnVisible(self, leftColumnVisible: str):
        self.__leftColumnVisible = leftColumnVisible


    @property
    def splitVertical(self):
        return self.__splitVertical

    @splitVertical.setter
    def splitVertical(self, splitVertical: str):
        self.__splitVertical = splitVertical


    @property
    def filterOn(self):
        return self.__filterOn

    @filterOn.setter
    def filterOn(self, filterOn: str):
        self.__filterOn = filterOn


    @property
    def defaultRowHeight(self):
        return self.__defaultRowHeight

    @defaultRowHeight.setter
    def defaultRowHeight(self, defaultRowHeight: str):
        self.__defaultRowHeight = defaultRowHeight


    @property
    def allowUsePivotTables(self):
        return self.__allowUsePivotTables

    @allowUsePivotTables.setter
    def allowUsePivotTables(self, allowUsePivotTables: str):
        self.__allowUsePivotTables = allowUsePivotTables


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
    def allowInsertRows(self):
        return self.__allowInsertRows

    @allowInsertRows.setter
    def allowInsertRows(self, allowInsertRows: str):
        self.__allowInsertRows = allowInsertRows


    @property
    def doNotDisplayOutline(self):
        return self.__doNotDisplayOutline

    @doNotDisplayOutline.setter
    def doNotDisplayOutline(self, doNotDisplayOutline: str):
        self.__doNotDisplayOutline = doNotDisplayOutline


    @property
    def transitionExpressionEvaluation(self):
        return self.__transitionExpressionEvaluation

    @transitionExpressionEvaluation.setter
    def transitionExpressionEvaluation(self, transitionExpressionEvaluation: str):
        self.__transitionExpressionEvaluation = transitionExpressionEvaluation


    @property
    def allowDeleteRows(self):
        return self.__allowDeleteRows

    @allowDeleteRows.setter
    def allowDeleteRows(self, allowDeleteRows: str):
        self.__allowDeleteRows = allowDeleteRows


    @property
    def allowSort(self):
        return self.__allowSort

    @allowSort.setter
    def allowSort(self, allowSort: str):
        self.__allowSort = allowSort


    @property
    def pageBreakZoom(self):
        return self.__pageBreakZoom

    @pageBreakZoom.setter
    def pageBreakZoom(self, pageBreakZoom: str):
        self.__pageBreakZoom = pageBreakZoom


    @property
    def applyAutomaticOutlineStyles(self):
        return self.__applyAutomaticOutlineStyles

    @applyAutomaticOutlineStyles.setter
    def applyAutomaticOutlineStyles(self, applyAutomaticOutlineStyles: str):
        self.__applyAutomaticOutlineStyles = applyAutomaticOutlineStyles


    @property
    def noSummaryRowsBelowDetail(self):
        return self.__noSummaryRowsBelowDetail

    @noSummaryRowsBelowDetail.setter
    def noSummaryRowsBelowDetail(self, noSummaryRowsBelowDetail: str):
        self.__noSummaryRowsBelowDetail = noSummaryRowsBelowDetail


    @property
    def defaultColumnWidth(self):
        return self.__defaultColumnWidth

    @defaultColumnWidth.setter
    def defaultColumnWidth(self, defaultColumnWidth: str):
        self.__defaultColumnWidth = defaultColumnWidth


    @property
    def zoom(self):
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom


    @property
    def allowDeleteCols(self):
        return self.__allowDeleteCols

    @allowDeleteCols.setter
    def allowDeleteCols(self, allowDeleteCols: str):
        self.__allowDeleteCols = allowDeleteCols


    @property
    def rangeSelection(self):
        return self.__rangeSelection

    @rangeSelection.setter
    def rangeSelection(self, rangeSelection: str):
        self.__rangeSelection = rangeSelection


    @property
    def protectScenarios(self):
        return self.__protectScenarios

    @protectScenarios.setter
    def protectScenarios(self, protectScenarios: str):
        self.__protectScenarios = protectScenarios


    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected


    @property
    def displayFormulas(self):
        return self.__displayFormulas

    @displayFormulas.setter
    def displayFormulas(self, displayFormulas: str):
        self.__displayFormulas = displayFormulas


    @property
    def transitionFormulaEntry(self):
        return self.__transitionFormulaEntry

    @transitionFormulaEntry.setter
    def transitionFormulaEntry(self, transitionFormulaEntry: str):
        self.__transitionFormulaEntry = transitionFormulaEntry


    @property
    def doNotDisplayGridlines(self):
        return self.__doNotDisplayGridlines

    @doNotDisplayGridlines.setter
    def doNotDisplayGridlines(self, doNotDisplayGridlines: str):
        self.__doNotDisplayGridlines = doNotDisplayGridlines


    @property
    def allowSizeRows(self):
        return self.__allowSizeRows

    @allowSizeRows.setter
    def allowSizeRows(self, allowSizeRows: str):
        self.__allowSizeRows = allowSizeRows


    @property
    def activeColumn(self):
        return self.__activeColumn

    @activeColumn.setter
    def activeColumn(self, activeColumn: str):
        self.__activeColumn = activeColumn


    @property
    def tabColorIndex(self):
        return self.__tabColorIndex

    @tabColorIndex.setter
    def tabColorIndex(self, tabColorIndex: str):
        self.__tabColorIndex = tabColorIndex


    @property
    def showPageBreakZoom(self):
        return self.__showPageBreakZoom

    @showPageBreakZoom.setter
    def showPageBreakZoom(self, showPageBreakZoom: str):
        self.__showPageBreakZoom = showPageBreakZoom


    @property
    def leftColumnRightPane(self):
        return self.__leftColumnRightPane

    @leftColumnRightPane.setter
    def leftColumnRightPane(self, leftColumnRightPane: str):
        self.__leftColumnRightPane = leftColumnRightPane


    @property
    def doNotDisplayHeadings(self):
        return self.__doNotDisplayHeadings

    @doNotDisplayHeadings.setter
    def doNotDisplayHeadings(self, doNotDisplayHeadings: str):
        self.__doNotDisplayHeadings = doNotDisplayHeadings


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
    def activePane(self):
        return self.__activePane

    @activePane.setter
    def activePane(self, activePane: str):
        self.__activePane = activePane


    @property
    def displayRightToLeft(self):
        return self.__displayRightToLeft

    @displayRightToLeft.setter
    def displayRightToLeft(self, displayRightToLeft: str):
        self.__displayRightToLeft = displayRightToLeft


    @property
    def splitHorizontal(self):
        return self.__splitHorizontal

    @splitHorizontal.setter
    def splitHorizontal(self, splitHorizontal: str):
        self.__splitHorizontal = splitHorizontal


    @property
    def enableSelection(self):
        return self.__enableSelection

    @enableSelection.setter
    def enableSelection(self, enableSelection: str):
        self.__enableSelection = enableSelection


    @property
    def protectContentst(self):
        return self.__protectContentst

    @protectContentst.setter
    def protectContentst(self, protectContentst: str):
        self.__protectContentst = protectContentst


    @property
    def doNotDisplayColHeaders(self):
        return self.__doNotDisplayColHeaders

    @doNotDisplayColHeaders.setter
    def doNotDisplayColHeaders(self, doNotDisplayColHeaders: str):
        self.__doNotDisplayColHeaders = doNotDisplayColHeaders


    @property
    def protectObjects(self):
        return self.__protectObjects

    @protectObjects.setter
    def protectObjects(self, protectObjects: str):
        self.__protectObjects = protectObjects


    @property
    def doNotDisplayZeros(self):
        return self.__doNotDisplayZeros

    @doNotDisplayZeros.setter
    def doNotDisplayZeros(self, doNotDisplayZeros: str):
        self.__doNotDisplayZeros = doNotDisplayZeros


    @property
    def allowInsertHyperlinks(self):
        return self.__allowInsertHyperlinks

    @allowInsertHyperlinks.setter
    def allowInsertHyperlinks(self, allowInsertHyperlinks: str):
        self.__allowInsertHyperlinks = allowInsertHyperlinks


    @property
    def allowFilter(self):
        return self.__allowFilter

    @allowFilter.setter
    def allowFilter(self, allowFilter: str):
        self.__allowFilter = allowFilter


    @property
    def freezePanes(self):
        return self.__freezePanes

    @freezePanes.setter
    def freezePanes(self, freezePanes: str):
        self.__freezePanes = freezePanes


    @property
    def topRowBottomPane(self):
        return self.__topRowBottomPane

    @topRowBottomPane.setter
    def topRowBottomPane(self, topRowBottomPane: str):
        self.__topRowBottomPane = topRowBottomPane


    @property
    def unsynced(self):
        return self.__unsynced

    @unsynced.setter
    def unsynced(self, unsynced: str):
        self.__unsynced = unsynced


    @property
    def topRowVisible(self):
        return self.__topRowVisible

    @topRowVisible.setter
    def topRowVisible(self, topRowVisible: str):
        self.__topRowVisible = topRowVisible


    @property
    def standardWidth(self):
        return self.__standardWidth

    @standardWidth.setter
    def standardWidth(self, standardWidth: str):
        self.__standardWidth = standardWidth


    @property
    def allowInsertCols(self):
        return self.__allowInsertCols

    @allowInsertCols.setter
    def allowInsertCols(self, allowInsertCols: str):
        self.__allowInsertCols = allowInsertCols


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def allowFormatCells(self):
        return self.__allowFormatCells

    @allowFormatCells.setter
    def allowFormatCells(self, allowFormatCells: str):
        self.__allowFormatCells = allowFormatCells


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible


    @property
    def w_worksheetOptions(self):
        return self.__w_worksheetOptions

    @w_worksheetOptions.setter
    def w_worksheetOptions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_WorksheetOptionsElt__w_worksheetOptions", None)
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

    @property
    def ps_worksheetOptions(self):
        return self.__ps_worksheetOptions

    @ps_worksheetOptions.setter
    def ps_worksheetOptions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_WorksheetOptionsElt__ps_worksheetOptions", None)
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
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_WorksheetOptionsElt__p_worksheetOptions", None)
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

class SpreadsheetMLPrintingSetup_Data:

    pass
class SpreadsheetMLPrintingSetup_ExcelWorkbook:

    def __init__(self, hideWorkbookTabs: str, windowHeight: str, windowWidth: str, windowTopX: str, windowTopY: str, activeSheet: str, activeChart: str, firstVisibleSheet: str, selectedSheets: str, windowHidden: str, hideHorizontalScrollBar: str, hideVerticalScrollBar: str, futureVer: str, maxChange: str, tabRatio: str, windowIconic: str, displayDrawingObjects: str, createBackup: str, calculation: str, doNotCalculateBeforeSave: str, hidePivotTableFieldList: str, date1904: str, protectStructure: str, refModeR1C1: str, protectWindows: str, iteration: str, displayInkNotes: str, embedSaveSmartTags: str, maxIterations: str, precisionAsDisplayed: str, doNotSaveLinkValues: str, noAutoRecover: str, acceptLabelsInFormulas: str, uncalced: str, wb_excelWorkbook: "Workbook" = None):
        self.hideWorkbookTabs = hideWorkbookTabs
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.windowTopX = windowTopX
        self.windowTopY = windowTopY
        self.activeSheet = activeSheet
        self.activeChart = activeChart
        self.firstVisibleSheet = firstVisibleSheet
        self.selectedSheets = selectedSheets
        self.windowHidden = windowHidden
        self.hideHorizontalScrollBar = hideHorizontalScrollBar
        self.hideVerticalScrollBar = hideVerticalScrollBar
        self.futureVer = futureVer
        self.maxChange = maxChange
        self.tabRatio = tabRatio
        self.windowIconic = windowIconic
        self.displayDrawingObjects = displayDrawingObjects
        self.createBackup = createBackup
        self.calculation = calculation
        self.doNotCalculateBeforeSave = doNotCalculateBeforeSave
        self.hidePivotTableFieldList = hidePivotTableFieldList
        self.date1904 = date1904
        self.protectStructure = protectStructure
        self.refModeR1C1 = refModeR1C1
        self.protectWindows = protectWindows
        self.iteration = iteration
        self.displayInkNotes = displayInkNotes
        self.embedSaveSmartTags = embedSaveSmartTags
        self.maxIterations = maxIterations
        self.precisionAsDisplayed = precisionAsDisplayed
        self.doNotSaveLinkValues = doNotSaveLinkValues
        self.noAutoRecover = noAutoRecover
        self.acceptLabelsInFormulas = acceptLabelsInFormulas
        self.uncalced = uncalced
        self.wb_excelWorkbook = wb_excelWorkbook
        
        pass
    @property
    def maxChange(self):
        return self.__maxChange

    @maxChange.setter
    def maxChange(self, maxChange: str):
        self.__maxChange = maxChange


    @property
    def maxIterations(self):
        return self.__maxIterations

    @maxIterations.setter
    def maxIterations(self, maxIterations: str):
        self.__maxIterations = maxIterations


    @property
    def protectWindows(self):
        return self.__protectWindows

    @protectWindows.setter
    def protectWindows(self, protectWindows: str):
        self.__protectWindows = protectWindows


    @property
    def displayDrawingObjects(self):
        return self.__displayDrawingObjects

    @displayDrawingObjects.setter
    def displayDrawingObjects(self, displayDrawingObjects: str):
        self.__displayDrawingObjects = displayDrawingObjects


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
    def doNotSaveLinkValues(self):
        return self.__doNotSaveLinkValues

    @doNotSaveLinkValues.setter
    def doNotSaveLinkValues(self, doNotSaveLinkValues: str):
        self.__doNotSaveLinkValues = doNotSaveLinkValues


    @property
    def createBackup(self):
        return self.__createBackup

    @createBackup.setter
    def createBackup(self, createBackup: str):
        self.__createBackup = createBackup


    @property
    def hideWorkbookTabs(self):
        return self.__hideWorkbookTabs

    @hideWorkbookTabs.setter
    def hideWorkbookTabs(self, hideWorkbookTabs: str):
        self.__hideWorkbookTabs = hideWorkbookTabs


    @property
    def activeChart(self):
        return self.__activeChart

    @activeChart.setter
    def activeChart(self, activeChart: str):
        self.__activeChart = activeChart


    @property
    def windowHidden(self):
        return self.__windowHidden

    @windowHidden.setter
    def windowHidden(self, windowHidden: str):
        self.__windowHidden = windowHidden


    @property
    def uncalced(self):
        return self.__uncalced

    @uncalced.setter
    def uncalced(self, uncalced: str):
        self.__uncalced = uncalced


    @property
    def iteration(self):
        return self.__iteration

    @iteration.setter
    def iteration(self, iteration: str):
        self.__iteration = iteration


    @property
    def displayInkNotes(self):
        return self.__displayInkNotes

    @displayInkNotes.setter
    def displayInkNotes(self, displayInkNotes: str):
        self.__displayInkNotes = displayInkNotes


    @property
    def embedSaveSmartTags(self):
        return self.__embedSaveSmartTags

    @embedSaveSmartTags.setter
    def embedSaveSmartTags(self, embedSaveSmartTags: str):
        self.__embedSaveSmartTags = embedSaveSmartTags


    @property
    def precisionAsDisplayed(self):
        return self.__precisionAsDisplayed

    @precisionAsDisplayed.setter
    def precisionAsDisplayed(self, precisionAsDisplayed: str):
        self.__precisionAsDisplayed = precisionAsDisplayed


    @property
    def acceptLabelsInFormulas(self):
        return self.__acceptLabelsInFormulas

    @acceptLabelsInFormulas.setter
    def acceptLabelsInFormulas(self, acceptLabelsInFormulas: str):
        self.__acceptLabelsInFormulas = acceptLabelsInFormulas


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
    def calculation(self):
        return self.__calculation

    @calculation.setter
    def calculation(self, calculation: str):
        self.__calculation = calculation


    @property
    def windowWidth(self):
        return self.__windowWidth

    @windowWidth.setter
    def windowWidth(self, windowWidth: str):
        self.__windowWidth = windowWidth


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
    def date1904(self):
        return self.__date1904

    @date1904.setter
    def date1904(self, date1904: str):
        self.__date1904 = date1904


    @property
    def firstVisibleSheet(self):
        return self.__firstVisibleSheet

    @firstVisibleSheet.setter
    def firstVisibleSheet(self, firstVisibleSheet: str):
        self.__firstVisibleSheet = firstVisibleSheet


    @property
    def hideHorizontalScrollBar(self):
        return self.__hideHorizontalScrollBar

    @hideHorizontalScrollBar.setter
    def hideHorizontalScrollBar(self, hideHorizontalScrollBar: str):
        self.__hideHorizontalScrollBar = hideHorizontalScrollBar


    @property
    def doNotCalculateBeforeSave(self):
        return self.__doNotCalculateBeforeSave

    @doNotCalculateBeforeSave.setter
    def doNotCalculateBeforeSave(self, doNotCalculateBeforeSave: str):
        self.__doNotCalculateBeforeSave = doNotCalculateBeforeSave


    @property
    def windowHeight(self):
        return self.__windowHeight

    @windowHeight.setter
    def windowHeight(self, windowHeight: str):
        self.__windowHeight = windowHeight


    @property
    def futureVer(self):
        return self.__futureVer

    @futureVer.setter
    def futureVer(self, futureVer: str):
        self.__futureVer = futureVer


    @property
    def windowTopY(self):
        return self.__windowTopY

    @windowTopY.setter
    def windowTopY(self, windowTopY: str):
        self.__windowTopY = windowTopY


    @property
    def refModeR1C1(self):
        return self.__refModeR1C1

    @refModeR1C1.setter
    def refModeR1C1(self, refModeR1C1: str):
        self.__refModeR1C1 = refModeR1C1


    @property
    def wb_excelWorkbook(self):
        return self.__wb_excelWorkbook

    @wb_excelWorkbook.setter
    def wb_excelWorkbook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_ExcelWorkbook__wb_excelWorkbook", None)
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

class SpreadsheetMLPrintingSetup_Comment:

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
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Comment__c_comment", None)
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

    @property
    def d_comment(self):
        return self.__d_comment

    @d_comment.setter
    def d_comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Comment__d_comment", None)
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

class Comment:

    pass
class ColOrRowElement:

    pass
class SpreadsheetMLPrintingSetup_Row(ColOrRowElement):

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
    def c_row(self):
        return self.__c_row

    @c_row.setter
    def c_row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Row__c_row", None)
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
                    

    @property
    def t_rows(self):
        return self.__t_rows

    @t_rows.setter
    def t_rows(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Row__t_rows", None)
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

class SpreadsheetMLPrintingSetup_Column(ColOrRowElement):

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
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Column__t_cols", None)
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
class SpreadsheetMLPrintingSetup_Cell(TableElement):

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
    def hRef(self):
        return self.__hRef

    @hRef.setter
    def hRef(self, hRef: str):
        self.__hRef = hRef


    @property
    def mergeAcross(self):
        return self.__mergeAcross

    @mergeAcross.setter
    def mergeAcross(self, mergeAcross: str):
        self.__mergeAcross = mergeAcross


    @property
    def formula(self):
        return self.__formula

    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula


    @property
    def arrayRange(self):
        return self.__arrayRange

    @arrayRange.setter
    def arrayRange(self, arrayRange: str):
        self.__arrayRange = arrayRange


    @property
    def mergeDown(self):
        return self.__mergeDown

    @mergeDown.setter
    def mergeDown(self, mergeDown: str):
        self.__mergeDown = mergeDown


    @property
    def r_cells(self):
        return self.__r_cells

    @r_cells.setter
    def r_cells(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Cell__r_cells", None)
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
    def d_cell(self):
        return self.__d_cell

    @d_cell.setter
    def d_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Cell__d_cell", None)
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

    @property
    def c_cell(self):
        return self.__c_cell

    @c_cell.setter
    def c_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Cell__c_cell", None)
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
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Cell__st_cell", None)
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
                    

class SpreadsheetMLPrintingSetup_ColOrRowElement(TableElement):

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


class ExcelWorkbook:

    pass
class Row:

    pass
class Column:

    pass
class StyledElement:

    pass
class SpreadsheetMLPrintingSetup_TableElement(StyledElement):

    def __init__(self, index: str):
        self.index = index
        
        pass
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index


class SpreadsheetMLPrintingSetup_Table(StyledElement):

    def __init__(self, defaultColumnWidth: str, defaultRowHeight: str, expandedColumnCount: str, expandedRowCount: str, leftCell: str, topCell: str, fullColumns: str, fullRows: str, ws_table: "Worksheet" = None, c_table: set["Column"] = None, r_table: set["Row"] = None):
        self.defaultColumnWidth = defaultColumnWidth
        self.defaultRowHeight = defaultRowHeight
        self.expandedColumnCount = expandedColumnCount
        self.expandedRowCount = expandedRowCount
        self.leftCell = leftCell
        self.topCell = topCell
        self.fullColumns = fullColumns
        self.fullRows = fullRows
        self.ws_table = ws_table
        self.c_table = c_table if c_table is not None else set()
        self.r_table = r_table if r_table is not None else set()
        
        pass
    @property
    def expandedRowCount(self):
        return self.__expandedRowCount

    @expandedRowCount.setter
    def expandedRowCount(self, expandedRowCount: str):
        self.__expandedRowCount = expandedRowCount


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
    def leftCell(self):
        return self.__leftCell

    @leftCell.setter
    def leftCell(self, leftCell: str):
        self.__leftCell = leftCell


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
    def defaultRowHeight(self):
        return self.__defaultRowHeight

    @defaultRowHeight.setter
    def defaultRowHeight(self, defaultRowHeight: str):
        self.__defaultRowHeight = defaultRowHeight


    @property
    def c_table(self):
        return self.__c_table

    @c_table.setter
    def c_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Table__c_table", None)
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
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Table__ws_table", None)
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
    def r_table(self):
        return self.__r_table

    @r_table.setter
    def r_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Table__r_table", None)
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
                    

class SpreadsheetMLPrintingSetup_StyledElement(ABC):

    pass
class WorksheetOptionsElt:

    pass
class Table:

    pass
class SpreadsheetMLPrintingSetup_Worksheet:

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
    def rightToLeft(self):
        return self.__rightToLeft

    @rightToLeft.setter
    def rightToLeft(self, rightToLeft: str):
        self.__rightToLeft = rightToLeft


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def wb_worksheets(self):
        return self.__wb_worksheets

    @wb_worksheets.setter
    def wb_worksheets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Worksheet__wb_worksheets", None)
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
    def wo_worksheet(self):
        return self.__wo_worksheet

    @wo_worksheet.setter
    def wo_worksheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Worksheet__wo_worksheet", None)
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
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_Worksheet__t_worksheet", None)
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

class Worksheet:

    pass
class CustomDocumentProperty:

    pass
class DocumentPropertiesCollection:

    pass
class SpreadsheetMLPrintingSetup_Workbook:

    pass
class SmartTagType:

    pass
class Cell:

    pass
class SpreadsheetMLPrintingSetup_SmartTagsCollection:

    pass
class SmartTagsCollection:

    pass
class SpreadsheetMLPrintingSetup_SmartTagType:

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
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_SmartTagType__smartTagTypes", None)
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
class SpreadsheetMLPrintingSetup_CustomDocumentProperty:

    def __init__(self, name: str, customDocumentProperties: "CustomDocumentPropertiesCollection" = None, SpreadsheetMLPrintingSetup_CustomDocumentProperty: "ValueType" = None):
        self.name = name
        self.customDocumentProperties = customDocumentProperties
        self.SpreadsheetMLPrintingSetup_CustomDocumentProperty = SpreadsheetMLPrintingSetup_CustomDocumentProperty
        
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
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_CustomDocumentProperty__customDocumentProperties", None)
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
    def SpreadsheetMLPrintingSetup_CustomDocumentProperty(self):
        return self.__SpreadsheetMLPrintingSetup_CustomDocumentProperty

    @SpreadsheetMLPrintingSetup_CustomDocumentProperty.setter
    def SpreadsheetMLPrintingSetup_CustomDocumentProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLPrintingSetup_CustomDocumentProperty__SpreadsheetMLPrintingSetup_CustomDocumentProperty", None)
        self.__SpreadsheetMLPrintingSetup_CustomDocumentProperty = value
        
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

class SpreadsheetMLPrintingSetup_CustomDocumentPropertiesCollection:

    pass
class VersionType:

    pass
class ValueType:

    pass
class SpreadsheetMLPrintingSetup_ErrorValue(ValueType):

    pass
class SpreadsheetMLPrintingSetup_NumberValue(ValueType):

    def __init__(self, value: str, ValueType60: "SpreadsheetMLPrintingSetup_Data" = None, ValueType: "SpreadsheetMLPrintingSetup_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLPrintingSetup_BooleanValue(ValueType):

    def __init__(self, value: str, ValueType60: "SpreadsheetMLPrintingSetup_Data" = None, ValueType: "SpreadsheetMLPrintingSetup_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLPrintingSetup_StringValue(ValueType):

    def __init__(self, value: str, ValueType60: "SpreadsheetMLPrintingSetup_Data" = None, ValueType: "SpreadsheetMLPrintingSetup_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLPrintingSetup_DateTimeTypeValue(ValueType):

    pass