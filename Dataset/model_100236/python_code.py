from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class NoteValue(Enum):
    ftn_normal = "ftn_normal"
    ftn_separator = "ftn_separator"
    ftn_continuation_separator = "ftn_continuation_separator"
    ftn_continuation_notice = "ftn_continuation_notice"
class FldCharTypeProperty(Enum):
    fctp_begin = "fctp_begin"
    fctp_separate = "fctp_separate"
    fctp_end = "fctp_end"
class BreakType(Enum):
    bt_page = "bt_page"
    bt_column = "bt_column"
    bt_text_wrapping = "bt_text_wrapping"
class OnOffType(Enum):
    oot_on = "oot_on"
    oot_off = "oot_off"


############################################
# Definition of Classes
############################################

class WordprocessingMLTableElts_TabElt:

    pass
class WordprocessingMLTableElts_PictureType:

    pass
class WordprocessingMLTableElts_SectPrElt:

    pass
class WordprocessingMLTableElts_ListsElt:

    pass
class WordprocessingMLTableElts_FontsListElt:

    pass
class WordprocessingMLTableElts_TableCellPrElt:

    pass
class WordprocessingMLTableElts_StylesElt:

    pass
class WordprocessingMLTableElts_TableCellElt:

    pass
class WordprocessingMLTableElts_RowContentElt:

    pass
class TableCellPrElt:

    pass
class RowContentElt:

    pass
class TableRowPrElt:

    pass
class TablePrExElt:

    pass
class WordprocessingMLTableElts_RowElt:

    pass
class WordprocessingMLTableElts_TableRowPrElt:

    pass
class WordprocessingMLTableElts_TablePrExElt:

    pass
class RowElt:

    pass
class WordprocessingMLTableElts_TableContentElt:

    pass
class WordprocessingMLTableElts_TableGridElt:

    pass
class TableElt:

    pass
class RunLevelElt:

    pass
class TableGridElt:

    pass
class TablePrElt:

    pass
class WordprocessingMLTableElts_TablePrElt:

    pass
class TableContentElt:

    pass
class WordprocessingMLTableElts_FldCharElt:

    def __init__(self, fldCharType: StringType, fldLock: StringType, WordprocessingMLTableElts_FldCharElt: "StringType" = None):
        self.fldCharType = fldCharType
        self.fldLock = fldLock
        self.WordprocessingMLTableElts_FldCharElt = WordprocessingMLTableElts_FldCharElt
        
        pass
    @property
    def fldLock(self):
        return self.__fldLock

    @fldLock.setter
    def fldLock(self, fldLock: StringType):
        self.__fldLock = fldLock


    @property
    def fldCharType(self):
        return self.__fldCharType

    @fldCharType.setter
    def fldCharType(self, fldCharType: StringType):
        self.__fldCharType = fldCharType


    @property
    def WordprocessingMLTableElts_FldCharElt(self):
        return self.__WordprocessingMLTableElts_FldCharElt

    @WordprocessingMLTableElts_FldCharElt.setter
    def WordprocessingMLTableElts_FldCharElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLTableElts_FldCharElt__WordprocessingMLTableElts_FldCharElt", None)
        self.__WordprocessingMLTableElts_FldCharElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringType62"):
                opp_val = getattr(old_value, "StringType62", None)
                if opp_val == self:
                    setattr(old_value, "StringType62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringType62"):
                opp_val = getattr(value, "StringType62", None)
                setattr(value, "StringType62", self)

class FldCharElt:

    pass
class TabElt:

    pass
class WordprocessingMLTableElts_SymElt:

    pass
class WordprocessingMLTableElts_NoteElt(ABC):

    def __init__(self, type: StringType, suppressRef: StringType, ble_note: set["BlockLevelElt"] = None):
        self.type = type
        self.suppressRef = suppressRef
        self.ble_note = ble_note if ble_note is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: StringType):
        self.__type = type


    @property
    def suppressRef(self):
        return self.__suppressRef

    @suppressRef.setter
    def suppressRef(self, suppressRef: StringType):
        self.__suppressRef = suppressRef


    @property
    def ble_note(self):
        return self.__ble_note

    @ble_note.setter
    def ble_note(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLTableElts_NoteElt__ble_note", None)
        self.__ble_note = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BlockLevelElt56"):
                    opp_val = getattr(item, "BlockLevelElt56", None)
                    
                    if opp_val == self:
                        setattr(item, "BlockLevelElt56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BlockLevelElt56"):
                    opp_val = getattr(item, "BlockLevelElt56", None)
                    
                    setattr(item, "BlockLevelElt56", self)
                    

class WordDocument:

    pass
class WordprocessingMLTableElts_DocumentPropertiesCollection:

    def __init__(self, keywords: StringType, description: StringType, category: StringType, title: StringType, subject: StringType, totalTime: StringType, author: StringType, lastAuthor: StringType, manager: StringType, company: StringType, hyperlinkBase: StringType, revision: StringType, presentationFormat: StringType, guid: StringType, appName: StringType, lines: StringType, paragraphs: StringType, pages: StringType, words: StringType, characters: StringType, charactersWithSpaces: StringType, bytes: StringType, wd_docProperties: "WordDocument" = None, WordprocessingMLTableElts_DocumentPropertiesCollection: "VersionType" = None, WordprocessingMLTableElts_DocumentPropertiesCollection4: "DateTimeType" = None, WordprocessingMLTableElts_DocumentPropertiesCollection7: "DateTimeType" = None, WordprocessingMLTableElts_DocumentPropertiesCollection10: "DateTimeType" = None):
        self.keywords = keywords
        self.description = description
        self.category = category
        self.title = title
        self.subject = subject
        self.totalTime = totalTime
        self.author = author
        self.lastAuthor = lastAuthor
        self.manager = manager
        self.company = company
        self.hyperlinkBase = hyperlinkBase
        self.revision = revision
        self.presentationFormat = presentationFormat
        self.guid = guid
        self.appName = appName
        self.lines = lines
        self.paragraphs = paragraphs
        self.pages = pages
        self.words = words
        self.characters = characters
        self.charactersWithSpaces = charactersWithSpaces
        self.bytes = bytes
        self.wd_docProperties = wd_docProperties
        self.WordprocessingMLTableElts_DocumentPropertiesCollection = WordprocessingMLTableElts_DocumentPropertiesCollection
        self.WordprocessingMLTableElts_DocumentPropertiesCollection4 = WordprocessingMLTableElts_DocumentPropertiesCollection4
        self.WordprocessingMLTableElts_DocumentPropertiesCollection7 = WordprocessingMLTableElts_DocumentPropertiesCollection7
        self.WordprocessingMLTableElts_DocumentPropertiesCollection10 = WordprocessingMLTableElts_DocumentPropertiesCollection10
        
        pass
    @property
    def hyperlinkBase(self):
        return self.__hyperlinkBase

    @hyperlinkBase.setter
    def hyperlinkBase(self, hyperlinkBase: StringType):
        self.__hyperlinkBase = hyperlinkBase


    @property
    def guid(self):
        return self.__guid

    @guid.setter
    def guid(self, guid: StringType):
        self.__guid = guid


    @property
    def totalTime(self):
        return self.__totalTime

    @totalTime.setter
    def totalTime(self, totalTime: StringType):
        self.__totalTime = totalTime


    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: StringType):
        self.__keywords = keywords


    @property
    def bytes(self):
        return self.__bytes

    @bytes.setter
    def bytes(self, bytes: StringType):
        self.__bytes = bytes


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: StringType):
        self.__category = category


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: StringType):
        self.__author = author


    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, words: StringType):
        self.__words = words


    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject: StringType):
        self.__subject = subject


    @property
    def lastAuthor(self):
        return self.__lastAuthor

    @lastAuthor.setter
    def lastAuthor(self, lastAuthor: StringType):
        self.__lastAuthor = lastAuthor


    @property
    def appName(self):
        return self.__appName

    @appName.setter
    def appName(self, appName: StringType):
        self.__appName = appName


    @property
    def characters(self):
        return self.__characters

    @characters.setter
    def characters(self, characters: StringType):
        self.__characters = characters


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: StringType):
        self.__description = description


    @property
    def charactersWithSpaces(self):
        return self.__charactersWithSpaces

    @charactersWithSpaces.setter
    def charactersWithSpaces(self, charactersWithSpaces: StringType):
        self.__charactersWithSpaces = charactersWithSpaces


    @property
    def paragraphs(self):
        return self.__paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs: StringType):
        self.__paragraphs = paragraphs


    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company: StringType):
        self.__company = company


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: StringType):
        self.__pages = pages


    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager: StringType):
        self.__manager = manager


    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, lines: StringType):
        self.__lines = lines


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: StringType):
        self.__title = title


    @property
    def revision(self):
        return self.__revision

    @revision.setter
    def revision(self, revision: StringType):
        self.__revision = revision


    @property
    def presentationFormat(self):
        return self.__presentationFormat

    @presentationFormat.setter
    def presentationFormat(self, presentationFormat: StringType):
        self.__presentationFormat = presentationFormat


    @property
    def WordprocessingMLTableElts_DocumentPropertiesCollection10(self):
        return self.__WordprocessingMLTableElts_DocumentPropertiesCollection10

    @WordprocessingMLTableElts_DocumentPropertiesCollection10.setter
    def WordprocessingMLTableElts_DocumentPropertiesCollection10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLTableElts_DocumentPropertiesCollection__WordprocessingMLTableElts_DocumentPropertiesCollection10", None)
        self.__WordprocessingMLTableElts_DocumentPropertiesCollection10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DateTimeType11"):
                opp_val = getattr(old_value, "DateTimeType11", None)
                if opp_val == self:
                    setattr(old_value, "DateTimeType11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DateTimeType11"):
                opp_val = getattr(value, "DateTimeType11", None)
                setattr(value, "DateTimeType11", self)

    @property
    def wd_docProperties(self):
        return self.__wd_docProperties

    @wd_docProperties.setter
    def wd_docProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLTableElts_DocumentPropertiesCollection__wd_docProperties", None)
        self.__wd_docProperties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordDocument"):
                opp_val = getattr(old_value, "WordDocument", None)
                if opp_val == self:
                    setattr(old_value, "WordDocument", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordDocument"):
                opp_val = getattr(value, "WordDocument", None)
                setattr(value, "WordDocument", self)

    @property
    def WordprocessingMLTableElts_DocumentPropertiesCollection(self):
        return self.__WordprocessingMLTableElts_DocumentPropertiesCollection

    @WordprocessingMLTableElts_DocumentPropertiesCollection.setter
    def WordprocessingMLTableElts_DocumentPropertiesCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLTableElts_DocumentPropertiesCollection__WordprocessingMLTableElts_DocumentPropertiesCollection", None)
        self.__WordprocessingMLTableElts_DocumentPropertiesCollection = value
        
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
    def WordprocessingMLTableElts_DocumentPropertiesCollection4(self):
        return self.__WordprocessingMLTableElts_DocumentPropertiesCollection4

    @WordprocessingMLTableElts_DocumentPropertiesCollection4.setter
    def WordprocessingMLTableElts_DocumentPropertiesCollection4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLTableElts_DocumentPropertiesCollection__WordprocessingMLTableElts_DocumentPropertiesCollection4", None)
        self.__WordprocessingMLTableElts_DocumentPropertiesCollection4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DateTimeType5"):
                opp_val = getattr(old_value, "DateTimeType5", None)
                if opp_val == self:
                    setattr(old_value, "DateTimeType5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DateTimeType5"):
                opp_val = getattr(value, "DateTimeType5", None)
                setattr(value, "DateTimeType5", self)

    @property
    def WordprocessingMLTableElts_DocumentPropertiesCollection7(self):
        return self.__WordprocessingMLTableElts_DocumentPropertiesCollection7

    @WordprocessingMLTableElts_DocumentPropertiesCollection7.setter
    def WordprocessingMLTableElts_DocumentPropertiesCollection7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLTableElts_DocumentPropertiesCollection__WordprocessingMLTableElts_DocumentPropertiesCollection7", None)
        self.__WordprocessingMLTableElts_DocumentPropertiesCollection7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DateTimeType8"):
                opp_val = getattr(old_value, "DateTimeType8", None)
                if opp_val == self:
                    setattr(old_value, "DateTimeType8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DateTimeType8"):
                opp_val = getattr(value, "DateTimeType8", None)
                setattr(value, "DateTimeType8", self)

class ValueType:

    pass
class WordprocessingMLTableElts_FloatValue(ValueType):

    def __init__(self, value: StringType, ValueType: "WordprocessingMLTableElts_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: StringType):
        self.__value = value


class WordprocessingMLTableElts_BooleanValue(ValueType):

    def __init__(self, value: StringType, ValueType: "WordprocessingMLTableElts_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: StringType):
        self.__value = value


class WordprocessingMLTableElts_StringValue(ValueType):

    def __init__(self, value: StringType, ValueType: "WordprocessingMLTableElts_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: StringType):
        self.__value = value


class WordprocessingMLTableElts_ValueType(ABC):

    pass
class WordprocessingMLTableElts_VersionType:

    def __init__(self, n: StringType, nn: StringType):
        self.n = n
        self.nn = nn
        
        pass
    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n: StringType):
        self.__n = n


    @property
    def nn(self):
        return self.__nn

    @nn.setter
    def nn(self, nn: StringType):
        self.__nn = nn


class DateTimeType:

    pass
class WordprocessingMLTableElts_DateTimeTypeValue(ValueType):

    pass
class WordprocessingMLTableElts_DateTimeType:

    def __init__(self, hour: StringType, minute: StringType, second: StringType, year: StringType, month: StringType, day: StringType):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.year = year
        self.month = month
        self.day = day
        
        pass
    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute: StringType):
        self.__minute = minute


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: StringType):
        self.__day = day


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: StringType):
        self.__hour = hour


    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: StringType):
        self.__second = second


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: StringType):
        self.__month = month


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: StringType):
        self.__year = year


class SymElt:

    pass
class PictureType:

    pass
class RunElt:

    pass
class WordprocessingMLTableElts_RunPrElt:

    pass
class RunContentElt:

    pass
class WordprocessingMLTableElts_Picture(RunContentElt, PictureType):

    pass
class WordprocessingMLTableElts_Cr(RunContentElt):

    pass
class WordprocessingMLTableElts_SoftHyphen(RunContentElt):

    pass
class WordprocessingMLTableElts_PgNum(RunContentElt):

    pass
class WordprocessingMLTableElts_Separator(RunContentElt):

    pass
class WordprocessingMLTableElts_ContinuationSeparator(RunContentElt):

    pass
class WordprocessingMLTableElts_NoBreakHyphen(RunContentElt):

    pass
class WordprocessingMLTableElts_AnnotationRef(RunContentElt):

    pass
class WordprocessingMLTableElts_FldChar(FldCharElt, RunContentElt):

    pass
class WordprocessingMLTableElts_FootnoteRef(RunContentElt):

    pass
class WordprocessingMLTableElts_BreakElt(RunContentElt):

    def __init__(self, type: StringType, RunContentElt: "WordprocessingMLTableElts_RunElt" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: StringType):
        self.__type = type


class WordprocessingMLTableElts_EndnoteRef(RunContentElt):

    pass
class WordprocessingMLTableElts_Symbol(RunContentElt, SymElt):

    pass
class WordprocessingMLTableElts_Tab(RunContentElt, TabElt):

    pass
class RunPrElt:

    pass
class WordprocessingMLTableElts_ParaContentElt(ABC):

    pass
class WordprocessingMLTableElts_RunContentElt(ABC):

    pass
class ParaContentElt:

    pass
class WordprocessingMLTableElts_HLinkElt(ParaContentElt):

    pass
class WordprocessingMLTableElts_SimpleFieldElt(ParaContentElt):

    pass
class WordprocessingMLTableElts_SubDocElt(ParaContentElt):

    pass
class WordprocessingMLTableElts_RunElt(ParaContentElt):

    pass
class ParaPrElt:

    pass
class BlockLevelChunkElt:

    pass
class WordprocessingMLTableElts_TableElt(BlockLevelChunkElt):

    pass
class WordprocessingMLTableElts_RunLevelElt(BlockLevelChunkElt):

    pass
class WordprocessingMLTableElts_ParaElt(BlockLevelChunkElt):

    pass
class TableCellElt:

    pass
class NoteElt:

    pass
class WordprocessingMLTableElts_Endnote(RunContentElt, NoteElt):

    pass
class WordprocessingMLTableElts_Footnote(RunContentElt, NoteElt):

    pass
class ParaElt:

    pass
class WordprocessingMLTableElts_ParaPrElt:

    pass
class BlockLevelElt:

    pass
class WordprocessingMLTableElts_CfChunk(BlockLevelElt):

    pass
class WordprocessingMLTableElts_BlockLevelChunkElt(BlockLevelElt):

    pass
class WordprocessingMLTableElts_BodyElt:

    pass
class WordprocessingMLTableElts_DocPrElt:

    pass
class BodyElt:

    pass
class WordprocessingMLTableElts_BlockLevelElt(ABC):

    pass
class SectPrElt:

    pass
class StylesElt:

    pass
class ListsElt:

    pass
class FontsListElt:

    pass
class DocPrElt:

    pass
class DocumentPropertiesCollection:

    pass
class WordprocessingMLTableElts_WordDocument:

    pass
class StringProperty:

    pass
class WordprocessingMLTableElts_StringType:

    def __init__(self, val: StringType):
        self.val = val
        
        pass
    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val: StringType):
        self.__val = val


class StringType:

    pass
class WordprocessingMLTableElts_DelInstrText(StringType, RunContentElt):

    pass
class WordprocessingMLTableElts_InstrText(StringType, RunContentElt):

    pass
class WordprocessingMLTableElts_DelText(StringType, RunContentElt):

    pass
class WordprocessingMLTableElts_Text(StringType, RunContentElt):

    pass
class WordprocessingMLTableElts_StringProperty(StringType):

    pass
class SmartTagType:

    pass
class WordprocessingMLTableElts_SmartTagsCollection:

    pass
class CustomDocumentPropertiesCollection:

    pass
class WordprocessingMLTableElts_CustomDocumentProperty:

    def __init__(self, name: StringType, customDocumentProperties: "CustomDocumentPropertiesCollection" = None, WordprocessingMLTableElts_CustomDocumentProperty: "ValueType" = None):
        self.name = name
        self.customDocumentProperties = customDocumentProperties
        self.WordprocessingMLTableElts_CustomDocumentProperty = WordprocessingMLTableElts_CustomDocumentProperty
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: StringType):
        self.__name = name


    @property
    def WordprocessingMLTableElts_CustomDocumentProperty(self):
        return self.__WordprocessingMLTableElts_CustomDocumentProperty

    @WordprocessingMLTableElts_CustomDocumentProperty.setter
    def WordprocessingMLTableElts_CustomDocumentProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLTableElts_CustomDocumentProperty__WordprocessingMLTableElts_CustomDocumentProperty", None)
        self.__WordprocessingMLTableElts_CustomDocumentProperty = value
        
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
        old_value = getattr(self, f"_WordprocessingMLTableElts_CustomDocumentProperty__customDocumentProperties", None)
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
class WordprocessingMLTableElts_SmartTagType:

    def __init__(self, namespaceuri: StringType, name: StringType, url: StringType, smartTagTypes: "SmartTagsCollection" = None):
        self.namespaceuri = namespaceuri
        self.name = name
        self.url = url
        self.smartTagTypes = smartTagTypes
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: StringType):
        self.__name = name


    @property
    def namespaceuri(self):
        return self.__namespaceuri

    @namespaceuri.setter
    def namespaceuri(self, namespaceuri: StringType):
        self.__namespaceuri = namespaceuri


    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: StringType):
        self.__url = url


    @property
    def smartTagTypes(self):
        return self.__smartTagTypes

    @smartTagTypes.setter
    def smartTagTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLTableElts_SmartTagType__smartTagTypes", None)
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

class WordprocessingMLTableElts_CustomDocumentPropertiesCollection:

    pass
class VersionType:

    pass