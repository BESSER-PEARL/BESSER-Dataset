from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SpreadsheetMLBasicDef_Comment:

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
    def c_comment(self):
        return self.__c_comment

    @c_comment.setter
    def c_comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Comment__c_comment", None)
        self.__c_comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cell50"):
                opp_val = getattr(old_value, "Cell50", None)
                if opp_val == self:
                    setattr(old_value, "Cell50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cell50"):
                opp_val = getattr(value, "Cell50", None)
                setattr(value, "Cell50", self)

    @property
    def d_comment(self):
        return self.__d_comment

    @d_comment.setter
    def d_comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Comment__d_comment", None)
        self.__d_comment = value
        
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

class SpreadsheetMLBasicDef_Data:

    pass
class Comment:

    pass
class ColOrRowElement:

    pass
class SpreadsheetMLBasicDef_Column(ColOrRowElement):

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
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Column__t_cols", None)
        self.__t_cols = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table37"):
                opp_val = getattr(old_value, "Table37", None)
                if opp_val == self:
                    setattr(old_value, "Table37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table37"):
                opp_val = getattr(value, "Table37", None)
                setattr(value, "Table37", self)

class TableElement:

    pass
class SpreadsheetMLBasicDef_Cell(TableElement):

    def __init__(self, arrayRange: str, formula: str, hRef: str, mergeAcross: str, mergeDown: str, st_cell: set["SmartTagsCollection"] = None, d_cell: "Data" = None, c_cell: "Comment" = None, r_cells: "Row" = None):
        self.arrayRange = arrayRange
        self.formula = formula
        self.hRef = hRef
        self.mergeAcross = mergeAcross
        self.mergeDown = mergeDown
        self.st_cell = st_cell if st_cell is not None else set()
        self.d_cell = d_cell
        self.c_cell = c_cell
        self.r_cells = r_cells
        
        pass
    @property
    def hRef(self):
        return self.__hRef

    @hRef.setter
    def hRef(self, hRef: str):
        self.__hRef = hRef


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
    def c_cell(self):
        return self.__c_cell

    @c_cell.setter
    def c_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Cell__c_cell", None)
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
    def d_cell(self):
        return self.__d_cell

    @d_cell.setter
    def d_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Cell__d_cell", None)
        self.__d_cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data47"):
                opp_val = getattr(old_value, "Data47", None)
                if opp_val == self:
                    setattr(old_value, "Data47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data47"):
                opp_val = getattr(value, "Data47", None)
                setattr(value, "Data47", self)

    @property
    def r_cells(self):
        return self.__r_cells

    @r_cells.setter
    def r_cells(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Cell__r_cells", None)
        self.__r_cells = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Row43"):
                opp_val = getattr(old_value, "Row43", None)
                if opp_val == self:
                    setattr(old_value, "Row43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Row43"):
                opp_val = getattr(value, "Row43", None)
                setattr(value, "Row43", self)

    @property
    def st_cell(self):
        return self.__st_cell

    @st_cell.setter
    def st_cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Cell__st_cell", None)
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
                    

class SpreadsheetMLBasicDef_Row(ColOrRowElement):

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
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Row__t_rows", None)
        self.__t_rows = value
        
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

    @property
    def c_row(self):
        return self.__c_row

    @c_row.setter
    def c_row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Row__c_row", None)
        self.__c_row = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cell41"):
                    opp_val = getattr(item, "Cell41", None)
                    
                    if opp_val == self:
                        setattr(item, "Cell41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cell41"):
                    opp_val = getattr(item, "Cell41", None)
                    
                    setattr(item, "Cell41", self)
                    

class Row:

    pass
class SpreadsheetMLBasicDef_ColOrRowElement(TableElement):

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


class Table:

    pass
class SpreadsheetMLBasicDef_Worksheet:

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
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Worksheet__t_worksheet", None)
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
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Worksheet__wb_worksheets", None)
        self.__wb_worksheets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workbook30"):
                opp_val = getattr(old_value, "Workbook30", None)
                if opp_val == self:
                    setattr(old_value, "Workbook30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workbook30"):
                opp_val = getattr(value, "Workbook30", None)
                setattr(value, "Workbook30", self)

class Column:

    pass
class StyledElement:

    pass
class SpreadsheetMLBasicDef_TableElement(StyledElement):

    def __init__(self, index: str):
        self.index = index
        
        pass
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index


class SpreadsheetMLBasicDef_Table(StyledElement):

    def __init__(self, expandedRowCount: str, leftCell: str, topCell: str, fullColumns: str, fullRows: str, defaultColumnWidth: str, defaultRowHeight: str, expandedColumnCount: str, ws_table: "Worksheet" = None, c_table: set["Column"] = None, r_table: set["Row"] = None):
        self.expandedRowCount = expandedRowCount
        self.leftCell = leftCell
        self.topCell = topCell
        self.fullColumns = fullColumns
        self.fullRows = fullRows
        self.defaultColumnWidth = defaultColumnWidth
        self.defaultRowHeight = defaultRowHeight
        self.expandedColumnCount = expandedColumnCount
        self.ws_table = ws_table
        self.c_table = c_table if c_table is not None else set()
        self.r_table = r_table if r_table is not None else set()
        
        pass
    @property
    def defaultRowHeight(self):
        return self.__defaultRowHeight

    @defaultRowHeight.setter
    def defaultRowHeight(self, defaultRowHeight: str):
        self.__defaultRowHeight = defaultRowHeight


    @property
    def fullColumns(self):
        return self.__fullColumns

    @fullColumns.setter
    def fullColumns(self, fullColumns: str):
        self.__fullColumns = fullColumns


    @property
    def fullRows(self):
        return self.__fullRows

    @fullRows.setter
    def fullRows(self, fullRows: str):
        self.__fullRows = fullRows


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
    def expandedRowCount(self):
        return self.__expandedRowCount

    @expandedRowCount.setter
    def expandedRowCount(self, expandedRowCount: str):
        self.__expandedRowCount = expandedRowCount


    @property
    def topCell(self):
        return self.__topCell

    @topCell.setter
    def topCell(self, topCell: str):
        self.__topCell = topCell


    @property
    def expandedColumnCount(self):
        return self.__expandedColumnCount

    @expandedColumnCount.setter
    def expandedColumnCount(self, expandedColumnCount: str):
        self.__expandedColumnCount = expandedColumnCount


    @property
    def r_table(self):
        return self.__r_table

    @r_table.setter
    def r_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Table__r_table", None)
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
    def ws_table(self):
        return self.__ws_table

    @ws_table.setter
    def ws_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Table__ws_table", None)
        self.__ws_table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Worksheet33"):
                opp_val = getattr(old_value, "Worksheet33", None)
                if opp_val == self:
                    setattr(old_value, "Worksheet33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Worksheet33"):
                opp_val = getattr(value, "Worksheet33", None)
                setattr(value, "Worksheet33", self)

    @property
    def c_table(self):
        return self.__c_table

    @c_table.setter
    def c_table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_Table__c_table", None)
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
                    

class SpreadsheetMLBasicDef_StyledElement(ABC):

    pass
class SpreadsheetMLBasicDef_Workbook:

    pass
class SmartTagType:

    pass
class Cell:

    pass
class Worksheet:

    pass
class DocumentPropertiesCollection:

    pass
class SmartTagsCollection:

    pass
class SpreadsheetMLBasicDef_SmartTagType:

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
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


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
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_SmartTagType__smartTagTypes", None)
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

class SpreadsheetMLBasicDef_SmartTagsCollection:

    pass
class SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection:

    pass
class CustomDocumentPropertiesCollection:

    pass
class SpreadsheetMLBasicDef_CustomDocumentProperty:

    def __init__(self, name: str, customDocumentProperties: "CustomDocumentPropertiesCollection" = None, SpreadsheetMLBasicDef_CustomDocumentProperty: "ValueType" = None):
        self.name = name
        self.customDocumentProperties = customDocumentProperties
        self.SpreadsheetMLBasicDef_CustomDocumentProperty = SpreadsheetMLBasicDef_CustomDocumentProperty
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def SpreadsheetMLBasicDef_CustomDocumentProperty(self):
        return self.__SpreadsheetMLBasicDef_CustomDocumentProperty

    @SpreadsheetMLBasicDef_CustomDocumentProperty.setter
    def SpreadsheetMLBasicDef_CustomDocumentProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_CustomDocumentProperty__SpreadsheetMLBasicDef_CustomDocumentProperty", None)
        self.__SpreadsheetMLBasicDef_CustomDocumentProperty = value
        
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
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_CustomDocumentProperty__customDocumentProperties", None)
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
class VersionType:

    pass
class Workbook:

    pass
class SpreadsheetMLBasicDef_DocumentPropertiesCollection:

    def __init__(self, author: str, lastAuthor: str, manager: str, company: str, hyperlinkBase: str, revision: str, presentationFormat: str, guid: str, title: str, subject: str, keywords: str, description: str, category: str, pages: str, words: str, characters: str, appName: str, totalTime: str, charactersWithSpaces: str, bytes: str, lines: str, paragraphs: str, wb_docProperties: "Workbook" = None, SpreadsheetMLBasicDef_DocumentPropertiesCollection5: "DateTimeType" = None, SpreadsheetMLBasicDef_DocumentPropertiesCollection8: "DateTimeType" = None, SpreadsheetMLBasicDef_DocumentPropertiesCollection11: "DateTimeType" = None, SpreadsheetMLBasicDef_DocumentPropertiesCollection: "VersionType" = None):
        self.author = author
        self.lastAuthor = lastAuthor
        self.manager = manager
        self.company = company
        self.hyperlinkBase = hyperlinkBase
        self.revision = revision
        self.presentationFormat = presentationFormat
        self.guid = guid
        self.title = title
        self.subject = subject
        self.keywords = keywords
        self.description = description
        self.category = category
        self.pages = pages
        self.words = words
        self.characters = characters
        self.appName = appName
        self.totalTime = totalTime
        self.charactersWithSpaces = charactersWithSpaces
        self.bytes = bytes
        self.lines = lines
        self.paragraphs = paragraphs
        self.wb_docProperties = wb_docProperties
        self.SpreadsheetMLBasicDef_DocumentPropertiesCollection5 = SpreadsheetMLBasicDef_DocumentPropertiesCollection5
        self.SpreadsheetMLBasicDef_DocumentPropertiesCollection8 = SpreadsheetMLBasicDef_DocumentPropertiesCollection8
        self.SpreadsheetMLBasicDef_DocumentPropertiesCollection11 = SpreadsheetMLBasicDef_DocumentPropertiesCollection11
        self.SpreadsheetMLBasicDef_DocumentPropertiesCollection = SpreadsheetMLBasicDef_DocumentPropertiesCollection
        
        pass
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
    def characters(self):
        return self.__characters

    @characters.setter
    def characters(self, characters: str):
        self.__characters = characters


    @property
    def paragraphs(self):
        return self.__paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs: str):
        self.__paragraphs = paragraphs


    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject


    @property
    def bytes(self):
        return self.__bytes

    @bytes.setter
    def bytes(self, bytes: str):
        self.__bytes = bytes


    @property
    def charactersWithSpaces(self):
        return self.__charactersWithSpaces

    @charactersWithSpaces.setter
    def charactersWithSpaces(self, charactersWithSpaces: str):
        self.__charactersWithSpaces = charactersWithSpaces


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


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
    def appName(self):
        return self.__appName

    @appName.setter
    def appName(self, appName: str):
        self.__appName = appName


    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, lines: str):
        self.__lines = lines


    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager: str):
        self.__manager = manager


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


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
    def hyperlinkBase(self):
        return self.__hyperlinkBase

    @hyperlinkBase.setter
    def hyperlinkBase(self, hyperlinkBase: str):
        self.__hyperlinkBase = hyperlinkBase


    @property
    def presentationFormat(self):
        return self.__presentationFormat

    @presentationFormat.setter
    def presentationFormat(self, presentationFormat: str):
        self.__presentationFormat = presentationFormat


    @property
    def guid(self):
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid


    @property
    def totalTime(self):
        return self.__totalTime

    @totalTime.setter
    def totalTime(self, totalTime: str):
        self.__totalTime = totalTime


    @property
    def lastAuthor(self):
        return self.__lastAuthor

    @lastAuthor.setter
    def lastAuthor(self, lastAuthor: str):
        self.__lastAuthor = lastAuthor


    @property
    def wb_docProperties(self):
        return self.__wb_docProperties

    @wb_docProperties.setter
    def wb_docProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_DocumentPropertiesCollection__wb_docProperties", None)
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
    def SpreadsheetMLBasicDef_DocumentPropertiesCollection8(self):
        return self.__SpreadsheetMLBasicDef_DocumentPropertiesCollection8

    @SpreadsheetMLBasicDef_DocumentPropertiesCollection8.setter
    def SpreadsheetMLBasicDef_DocumentPropertiesCollection8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_DocumentPropertiesCollection__SpreadsheetMLBasicDef_DocumentPropertiesCollection8", None)
        self.__SpreadsheetMLBasicDef_DocumentPropertiesCollection8 = value
        
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
    def SpreadsheetMLBasicDef_DocumentPropertiesCollection11(self):
        return self.__SpreadsheetMLBasicDef_DocumentPropertiesCollection11

    @SpreadsheetMLBasicDef_DocumentPropertiesCollection11.setter
    def SpreadsheetMLBasicDef_DocumentPropertiesCollection11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_DocumentPropertiesCollection__SpreadsheetMLBasicDef_DocumentPropertiesCollection11", None)
        self.__SpreadsheetMLBasicDef_DocumentPropertiesCollection11 = value
        
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
    def SpreadsheetMLBasicDef_DocumentPropertiesCollection5(self):
        return self.__SpreadsheetMLBasicDef_DocumentPropertiesCollection5

    @SpreadsheetMLBasicDef_DocumentPropertiesCollection5.setter
    def SpreadsheetMLBasicDef_DocumentPropertiesCollection5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_DocumentPropertiesCollection__SpreadsheetMLBasicDef_DocumentPropertiesCollection5", None)
        self.__SpreadsheetMLBasicDef_DocumentPropertiesCollection5 = value
        
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
    def SpreadsheetMLBasicDef_DocumentPropertiesCollection(self):
        return self.__SpreadsheetMLBasicDef_DocumentPropertiesCollection

    @SpreadsheetMLBasicDef_DocumentPropertiesCollection.setter
    def SpreadsheetMLBasicDef_DocumentPropertiesCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpreadsheetMLBasicDef_DocumentPropertiesCollection__SpreadsheetMLBasicDef_DocumentPropertiesCollection", None)
        self.__SpreadsheetMLBasicDef_DocumentPropertiesCollection = value
        
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
class SpreadsheetMLBasicDef_VersionType:

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


class ValueType:

    pass
class SpreadsheetMLBasicDef_ErrorValue(ValueType):

    pass
class SpreadsheetMLBasicDef_BooleanValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLBasicDef_CustomDocumentProperty" = None, ValueType58: "SpreadsheetMLBasicDef_Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLBasicDef_DateTimeTypeValue(ValueType):

    pass
class SpreadsheetMLBasicDef_NumberValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLBasicDef_CustomDocumentProperty" = None, ValueType58: "SpreadsheetMLBasicDef_Data" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class SpreadsheetMLBasicDef_StringValue(ValueType):

    def __init__(self, value: str, ValueType: "SpreadsheetMLBasicDef_CustomDocumentProperty" = None, ValueType58: "SpreadsheetMLBasicDef_Data" = None):
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
class SpreadsheetMLBasicDef_ValueType(ABC):

    pass
class SpreadsheetMLBasicDef_DateTimeType:

    def __init__(self, year: str, month: str, day: str, hour: str, minute: str, second: str):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        
        pass
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute: str):
        self.__minute = minute


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
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: str):
        self.__hour = hour


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

