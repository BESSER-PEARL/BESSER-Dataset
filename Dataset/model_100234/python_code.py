from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OnOffType(Enum):
    oot_off = "oot_off"
    oot_on = "oot_on"
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
    fctp_begin = "fctp_begin"
    fctp_separate = "fctp_separate"
    fctp_end = "fctp_end"


############################################
# Definition of Classes
############################################

class WordprocessingMLBasicDef_SymElt:

    pass
class SymElt:

    pass
class RunContentElt:

    pass
class WordprocessingMLBasicDef_SoftHyphen(RunContentElt):

    pass
class WordprocessingMLBasicDef_Symbol(RunContentElt, SymElt):

    pass
class WordprocessingMLBasicDef_Cr(RunContentElt):

    pass
class WordprocessingMLBasicDef_EndnoteRef(RunContentElt):

    pass
class WordprocessingMLBasicDef_NoBreakHyphen(RunContentElt):

    pass
class WordprocessingMLBasicDef_FootnoteRef(RunContentElt):

    pass
class WordprocessingMLBasicDef_Tab(RunContentElt):

    pass
class WordprocessingMLBasicDef_AnnotationRef(RunContentElt):

    pass
class WordprocessingMLBasicDef_PgNum(RunContentElt):

    pass
class WordprocessingMLBasicDef_ContinuationSeparator(RunContentElt):

    pass
class WordprocessingMLBasicDef_Separator(RunContentElt):

    pass
class ParaElt:

    pass
class WordprocessingMLBasicDef_ParaContentElt(ABC):

    pass
class ParaContentElt:

    pass
class WordprocessingMLBasicDef_RunElt(ParaContentElt):

    pass
class BlockLevelChunkElt:

    pass
class WordprocessingMLBasicDef_ParaElt(BlockLevelChunkElt):

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


class RunElt:

    pass
class WordprocessingMLBasicDef_RunContentElt(ABC):

    pass
class BlockLevelElt:

    pass
class WordDocument:

    pass
class WordprocessingMLBasicDef_BodyElt:

    pass
class BodyElt:

    pass
class WordprocessingMLBasicDef_BlockLevelChunkElt(BlockLevelElt):

    pass
class NoteElt:

    pass
class WordprocessingMLBasicDef_Footnote(RunContentElt, NoteElt):

    pass
class WordprocessingMLBasicDef_Endnote(RunContentElt, NoteElt):

    pass
class WordprocessingMLBasicDef_BlockLevelElt(ABC):

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


class StringProperty:

    pass
class WordprocessingMLBasicDef_WordDocument:

    pass
class StringType:

    pass
class WordprocessingMLBasicDef_DelInstrText(RunContentElt, StringType):

    pass
class WordprocessingMLBasicDef_DelText(RunContentElt, StringType):

    pass
class WordprocessingMLBasicDef_Text(RunContentElt, StringType):

    pass
class WordprocessingMLBasicDef_InstrText(RunContentElt, StringType):

    pass
class WordprocessingMLBasicDef_StringProperty(StringType):

    pass
class WordprocessingMLBasicDef_FldCharElt:

    def __init__(self, fldLock: StringType, fldCharType: StringType, WordprocessingMLBasicDef_FldCharElt: "StringType" = None):
        self.fldLock = fldLock
        self.fldCharType = fldCharType
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
            if hasattr(old_value, "StringType21"):
                opp_val = getattr(old_value, "StringType21", None)
                if opp_val == self:
                    setattr(old_value, "StringType21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringType21"):
                opp_val = getattr(value, "StringType21", None)
                setattr(value, "StringType21", self)

class WordprocessingMLBasicDef_Picture(RunContentElt):

    pass
class FldCharElt:

    pass
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
                if hasattr(item, "BlockLevelElt15"):
                    opp_val = getattr(item, "BlockLevelElt15", None)
                    
                    if opp_val == self:
                        setattr(item, "BlockLevelElt15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BlockLevelElt15"):
                    opp_val = getattr(item, "BlockLevelElt15", None)
                    
                    setattr(item, "BlockLevelElt15", self)
                    

class WordprocessingMLBasicDef_FldChar(RunContentElt, FldCharElt):

    pass