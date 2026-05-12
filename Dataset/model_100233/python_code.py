from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OnOffType(Enum):
    oot_on = "oot_on"
    oot_off = "oot_off"
class BreakType(Enum):
    bt_page = "bt_page"
    bt_column = "bt_column"
    bt_text_wrapping = "bt_text_wrapping"
class NoteValue(Enum):
    ftn_normal = "ftn_normal"
    ftn_separator = "ftn_separator"
    ftn_continuation_separator = "ftn_continuation_separator"
    ftn_continuation_notice = "ftn_continuation_notice"
class FldCharTypeProperty(Enum):
    fctp_end = "fctp_end"
    fctp_begin = "fctp_begin"
    fctp_separate = "fctp_separate"


############################################
# Definition of Classes
############################################

class WordprocessingMLBasicDef_NoteElt(ABC):

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
        old_value = getattr(self, f"_WordprocessingMLBasicDef_NoteElt__ble_note", None)
        self.__ble_note = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BlockLevelElt55"):
                    opp_val = getattr(item, "BlockLevelElt55", None)
                    
                    if opp_val == self:
                        setattr(item, "BlockLevelElt55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BlockLevelElt55"):
                    opp_val = getattr(item, "BlockLevelElt55", None)
                    
                    setattr(item, "BlockLevelElt55", self)
                    

class WordprocessingMLBasicDef_SymElt:

    pass
class SymElt:

    pass
class PictureType:

    pass
class RunContentElt:

    pass
class WordprocessingMLBasicDef_PgNum(RunContentElt):

    pass
class WordprocessingMLBasicDef_NoBreakHyphen(RunContentElt):

    pass
class WordprocessingMLBasicDef_ContinuationSeparator(RunContentElt):

    pass
class WordprocessingMLBasicDef_Symbol(SymElt, RunContentElt):

    pass
class WordprocessingMLBasicDef_Separator(RunContentElt):

    pass
class WordprocessingMLBasicDef_EndnoteRef(RunContentElt):

    pass
class WordprocessingMLBasicDef_FootnoteRef(RunContentElt):

    pass
class WordprocessingMLBasicDef_Cr(RunContentElt):

    pass
class WordprocessingMLBasicDef_SoftHyphen(RunContentElt):

    pass
class WordprocessingMLBasicDef_AnnotationRef(RunContentElt):

    pass
class WordprocessingMLBasicDef_Picture(PictureType, RunContentElt):

    pass
class WordprocessingMLBasicDef_BreakElt(RunContentElt):

    def __init__(self, type: StringType, RunContentElt: "WordprocessingMLBasicDef_RunElt" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: StringType):
        self.__type = type


class WordprocessingMLBasicDef_RunContentElt(ABC):

    pass
class RunElt:

    pass
class WordprocessingMLBasicDef_RunPrElt:

    pass
class ParaPrElt:

    pass
class BlockLevelChunkElt:

    pass
class WordprocessingMLBasicDef_ParaElt(BlockLevelChunkElt):

    pass
class RunPrElt:

    pass
class WordprocessingMLBasicDef_ParaContentElt(ABC):

    pass
class ParaElt:

    pass
class WordprocessingMLBasicDef_ParaPrElt:

    pass
class ParaContentElt:

    pass
class WordprocessingMLBasicDef_RunElt(ParaContentElt):

    pass
class WordprocessingMLBasicDef_BodyElt:

    pass
class NoteElt:

    pass
class WordprocessingMLBasicDef_Endnote(NoteElt, RunContentElt):

    pass
class WordprocessingMLBasicDef_Footnote(NoteElt, RunContentElt):

    pass
class WordprocessingMLBasicDef_BlockLevelElt(ABC):

    pass
class SectPrElt:

    pass
class BlockLevelElt:

    pass
class WordprocessingMLBasicDef_BlockLevelChunkElt(BlockLevelElt):

    pass
class FontsListElt:

    pass
class WordprocessingMLBasicDef_DocPrElt:

    pass
class StringProperty:

    pass
class BodyElt:

    pass
class DocPrElt:

    pass
class StylesElt:

    pass
class ListsElt:

    pass
class DocumentPropertiesCollection:

    pass
class WordprocessingMLBasicDef_WordDocument:

    pass
class SmartTagType:

    pass
class WordprocessingMLBasicDef_StringType:

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
class WordprocessingMLBasicDef_InstrText(StringType, RunContentElt):

    pass
class WordprocessingMLBasicDef_DelText(RunContentElt, StringType):

    pass
class WordprocessingMLBasicDef_DelInstrText(StringType, RunContentElt):

    pass
class WordprocessingMLBasicDef_Text(StringType, RunContentElt):

    pass
class WordprocessingMLBasicDef_StringProperty(StringType):

    pass
class SmartTagsCollection:

    pass
class WordprocessingMLBasicDef_SmartTagType:

    def __init__(self, name: StringType, url: StringType, namespaceuri: StringType, smartTagTypes: "SmartTagsCollection" = None):
        self.name = name
        self.url = url
        self.namespaceuri = namespaceuri
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
        old_value = getattr(self, f"_WordprocessingMLBasicDef_SmartTagType__smartTagTypes", None)
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
class WordprocessingMLBasicDef_SmartTagsCollection:

    pass
class WordprocessingMLBasicDef_CustomDocumentPropertiesCollection:

    pass
class WordprocessingMLBasicDef_CustomDocumentProperty:

    def __init__(self, name: StringType, customDocumentProperties: "CustomDocumentPropertiesCollection" = None, WordprocessingMLBasicDef_CustomDocumentProperty: "ValueType" = None):
        self.name = name
        self.customDocumentProperties = customDocumentProperties
        self.WordprocessingMLBasicDef_CustomDocumentProperty = WordprocessingMLBasicDef_CustomDocumentProperty
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: StringType):
        self.__name = name


    @property
    def WordprocessingMLBasicDef_CustomDocumentProperty(self):
        return self.__WordprocessingMLBasicDef_CustomDocumentProperty

    @WordprocessingMLBasicDef_CustomDocumentProperty.setter
    def WordprocessingMLBasicDef_CustomDocumentProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLBasicDef_CustomDocumentProperty__WordprocessingMLBasicDef_CustomDocumentProperty", None)
        self.__WordprocessingMLBasicDef_CustomDocumentProperty = value
        
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
        old_value = getattr(self, f"_WordprocessingMLBasicDef_CustomDocumentProperty__customDocumentProperties", None)
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
class DateTimeType:

    pass
class ValueType:

    pass
class WordprocessingMLBasicDef_FloatValue(ValueType):

    def __init__(self, value: StringType, ValueType: "WordprocessingMLBasicDef_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: StringType):
        self.__value = value


class WordprocessingMLBasicDef_DateTimeTypeValue(ValueType):

    pass
class WordprocessingMLBasicDef_BooleanValue(ValueType):

    def __init__(self, value: StringType, ValueType: "WordprocessingMLBasicDef_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: StringType):
        self.__value = value


class WordprocessingMLBasicDef_StringValue(ValueType):

    def __init__(self, value: StringType, ValueType: "WordprocessingMLBasicDef_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: StringType):
        self.__value = value


class WordprocessingMLBasicDef_ValueType(ABC):

    pass
class WordDocument:

    pass
class WordprocessingMLBasicDef_DocumentPropertiesCollection:

    def __init__(self, title: StringType, subject: StringType, keywords: StringType, description: StringType, category: StringType, presentationFormat: StringType, guid: StringType, appName: StringType, totalTime: StringType, author: StringType, lastAuthor: StringType, manager: StringType, company: StringType, hyperlinkBase: StringType, revision: StringType, pages: StringType, words: StringType, characters: StringType, charactersWithSpaces: StringType, bytes: StringType, lines: StringType, paragraphs: StringType, wd_docProperties: "WordDocument" = None, WordprocessingMLBasicDef_DocumentPropertiesCollection: "VersionType" = None, WordprocessingMLBasicDef_DocumentPropertiesCollection4: "DateTimeType" = None, WordprocessingMLBasicDef_DocumentPropertiesCollection7: "DateTimeType" = None, WordprocessingMLBasicDef_DocumentPropertiesCollection10: "DateTimeType" = None):
        self.title = title
        self.subject = subject
        self.keywords = keywords
        self.description = description
        self.category = category
        self.presentationFormat = presentationFormat
        self.guid = guid
        self.appName = appName
        self.totalTime = totalTime
        self.author = author
        self.lastAuthor = lastAuthor
        self.manager = manager
        self.company = company
        self.hyperlinkBase = hyperlinkBase
        self.revision = revision
        self.pages = pages
        self.words = words
        self.characters = characters
        self.charactersWithSpaces = charactersWithSpaces
        self.bytes = bytes
        self.lines = lines
        self.paragraphs = paragraphs
        self.wd_docProperties = wd_docProperties
        self.WordprocessingMLBasicDef_DocumentPropertiesCollection = WordprocessingMLBasicDef_DocumentPropertiesCollection
        self.WordprocessingMLBasicDef_DocumentPropertiesCollection4 = WordprocessingMLBasicDef_DocumentPropertiesCollection4
        self.WordprocessingMLBasicDef_DocumentPropertiesCollection7 = WordprocessingMLBasicDef_DocumentPropertiesCollection7
        self.WordprocessingMLBasicDef_DocumentPropertiesCollection10 = WordprocessingMLBasicDef_DocumentPropertiesCollection10
        
        pass
    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: StringType):
        self.__keywords = keywords


    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject: StringType):
        self.__subject = subject


    @property
    def charactersWithSpaces(self):
        return self.__charactersWithSpaces

    @charactersWithSpaces.setter
    def charactersWithSpaces(self, charactersWithSpaces: StringType):
        self.__charactersWithSpaces = charactersWithSpaces


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: StringType):
        self.__category = category


    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, lines: StringType):
        self.__lines = lines


    @property
    def appName(self):
        return self.__appName

    @appName.setter
    def appName(self, appName: StringType):
        self.__appName = appName


    @property
    def lastAuthor(self):
        return self.__lastAuthor

    @lastAuthor.setter
    def lastAuthor(self, lastAuthor: StringType):
        self.__lastAuthor = lastAuthor


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: StringType):
        self.__pages = pages


    @property
    def presentationFormat(self):
        return self.__presentationFormat

    @presentationFormat.setter
    def presentationFormat(self, presentationFormat: StringType):
        self.__presentationFormat = presentationFormat


    @property
    def bytes(self):
        return self.__bytes

    @bytes.setter
    def bytes(self, bytes: StringType):
        self.__bytes = bytes


    @property
    def guid(self):
        return self.__guid

    @guid.setter
    def guid(self, guid: StringType):
        self.__guid = guid


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: StringType):
        self.__title = title


    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager: StringType):
        self.__manager = manager


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: StringType):
        self.__author = author


    @property
    def characters(self):
        return self.__characters

    @characters.setter
    def characters(self, characters: StringType):
        self.__characters = characters


    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company: StringType):
        self.__company = company


    @property
    def totalTime(self):
        return self.__totalTime

    @totalTime.setter
    def totalTime(self, totalTime: StringType):
        self.__totalTime = totalTime


    @property
    def hyperlinkBase(self):
        return self.__hyperlinkBase

    @hyperlinkBase.setter
    def hyperlinkBase(self, hyperlinkBase: StringType):
        self.__hyperlinkBase = hyperlinkBase


    @property
    def revision(self):
        return self.__revision

    @revision.setter
    def revision(self, revision: StringType):
        self.__revision = revision


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: StringType):
        self.__description = description


    @property
    def paragraphs(self):
        return self.__paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs: StringType):
        self.__paragraphs = paragraphs


    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, words: StringType):
        self.__words = words


    @property
    def WordprocessingMLBasicDef_DocumentPropertiesCollection10(self):
        return self.__WordprocessingMLBasicDef_DocumentPropertiesCollection10

    @WordprocessingMLBasicDef_DocumentPropertiesCollection10.setter
    def WordprocessingMLBasicDef_DocumentPropertiesCollection10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLBasicDef_DocumentPropertiesCollection__WordprocessingMLBasicDef_DocumentPropertiesCollection10", None)
        self.__WordprocessingMLBasicDef_DocumentPropertiesCollection10 = value
        
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
    def WordprocessingMLBasicDef_DocumentPropertiesCollection4(self):
        return self.__WordprocessingMLBasicDef_DocumentPropertiesCollection4

    @WordprocessingMLBasicDef_DocumentPropertiesCollection4.setter
    def WordprocessingMLBasicDef_DocumentPropertiesCollection4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLBasicDef_DocumentPropertiesCollection__WordprocessingMLBasicDef_DocumentPropertiesCollection4", None)
        self.__WordprocessingMLBasicDef_DocumentPropertiesCollection4 = value
        
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
    def WordprocessingMLBasicDef_DocumentPropertiesCollection7(self):
        return self.__WordprocessingMLBasicDef_DocumentPropertiesCollection7

    @WordprocessingMLBasicDef_DocumentPropertiesCollection7.setter
    def WordprocessingMLBasicDef_DocumentPropertiesCollection7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLBasicDef_DocumentPropertiesCollection__WordprocessingMLBasicDef_DocumentPropertiesCollection7", None)
        self.__WordprocessingMLBasicDef_DocumentPropertiesCollection7 = value
        
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

    @property
    def WordprocessingMLBasicDef_DocumentPropertiesCollection(self):
        return self.__WordprocessingMLBasicDef_DocumentPropertiesCollection

    @WordprocessingMLBasicDef_DocumentPropertiesCollection.setter
    def WordprocessingMLBasicDef_DocumentPropertiesCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLBasicDef_DocumentPropertiesCollection__WordprocessingMLBasicDef_DocumentPropertiesCollection", None)
        self.__WordprocessingMLBasicDef_DocumentPropertiesCollection = value
        
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
    def wd_docProperties(self):
        return self.__wd_docProperties

    @wd_docProperties.setter
    def wd_docProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLBasicDef_DocumentPropertiesCollection__wd_docProperties", None)
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

class WordprocessingMLBasicDef_DateTimeType:

    def __init__(self, year: StringType, month: StringType, day: StringType, hour: StringType, minute: StringType, second: StringType):
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
    def minute(self, minute: StringType):
        self.__minute = minute


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: StringType):
        self.__month = month


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
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: StringType):
        self.__year = year


    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: StringType):
        self.__second = second


class WordprocessingMLBasicDef_VersionType:

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


class WordprocessingMLBasicDef_TabElt:

    pass
class WordprocessingMLBasicDef_PictureType:

    pass
class WordprocessingMLBasicDef_SubDocElt(ParaContentElt):

    pass
class WordprocessingMLBasicDef_HLinkElt(ParaContentElt):

    pass
class WordprocessingMLBasicDef_SimpleFieldElt(ParaContentElt):

    pass
class WordprocessingMLBasicDef_CfChunk(BlockLevelElt):

    pass
class WordprocessingMLBasicDef_RunLevelElt(BlockLevelChunkElt):

    pass
class TabElt:

    pass
class WordprocessingMLBasicDef_Tab(TabElt, RunContentElt):

    pass
class WordprocessingMLBasicDef_StylesElt:

    pass
class WordprocessingMLBasicDef_ListsElt:

    pass
class WordprocessingMLBasicDef_FontsListElt:

    pass
class WordprocessingMLBasicDef_FldCharElt:

    def __init__(self, fldCharType: StringType, fldLock: StringType, WordprocessingMLBasicDef_FldCharElt: "StringType" = None):
        self.fldCharType = fldCharType
        self.fldLock = fldLock
        self.WordprocessingMLBasicDef_FldCharElt = WordprocessingMLBasicDef_FldCharElt
        
        pass
    @property
    def fldCharType(self):
        return self.__fldCharType

    @fldCharType.setter
    def fldCharType(self, fldCharType: StringType):
        self.__fldCharType = fldCharType


    @property
    def fldLock(self):
        return self.__fldLock

    @fldLock.setter
    def fldLock(self, fldLock: StringType):
        self.__fldLock = fldLock


    @property
    def WordprocessingMLBasicDef_FldCharElt(self):
        return self.__WordprocessingMLBasicDef_FldCharElt

    @WordprocessingMLBasicDef_FldCharElt.setter
    def WordprocessingMLBasicDef_FldCharElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLBasicDef_FldCharElt__WordprocessingMLBasicDef_FldCharElt", None)
        self.__WordprocessingMLBasicDef_FldCharElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringType61"):
                opp_val = getattr(old_value, "StringType61", None)
                if opp_val == self:
                    setattr(old_value, "StringType61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringType61"):
                opp_val = getattr(value, "StringType61", None)
                setattr(value, "StringType61", self)

class FldCharElt:

    pass
class WordprocessingMLBasicDef_FldChar(FldCharElt, RunContentElt):

    pass
class WordprocessingMLBasicDef_SectPrElt:

    pass