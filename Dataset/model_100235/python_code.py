from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class HighlightColorValues(Enum):
    hcv_black = "hcv_black"
    hcv_blue = "hcv_blue"
    hcv_cyan = "hcv_cyan"
    hcv_green = "hcv_green"
    hcv_magenta = "hcv_magenta"
    hcv_red = "hcv_red"
    hcv_yellow = "hcv_yellow"
    hcv_white = "hcv_white"
    hcv_dark_blue = "hcv_dark_blue"
    hcv_dark_cyan = "hcv_dark_cyan"
    hcv_dark_green = "hcv_dark_green"
    hcv_dark_magenta = "hcv_dark_magenta"
    hcv_dark_red = "hcv_dark_red"
    hcv_dark_yellow = "hcv_dark_yellow"
    hcv_dark_gray = "hcv_dark_gray"
    hcv_light_gray = "hcv_light_gray"
    hcv_none = "hcv_none"
class HintType(Enum):
    ht_fareast = "ht_fareast"
    ht_cs = "ht_cs"
    ht_default = "ht_default"
class JustificationValue(Enum):
    jv_left = "jv_left"
    jv_center = "jv_center"
    jv_right = "jv_right"
    jv_both = "jv_both"
class NoteValue(Enum):
    ftn_normal = "ftn_normal"
    ftn_separator = "ftn_separator"
    ftn_continuation_separator = "ftn_continuation_separator"
    ftn_continuation_notice = "ftn_continuation_notice"
class FldCharTypeProperty(Enum):
    fctp_begin = "fctp_begin"
    fctp_separate = "fctp_separate"
    fctp_end = "fctp_end"
class VerticalAlignRunType(Enum):
    vart_baseline = "vart_baseline"
    vart_superscript = "vart_superscript"
    vart_subscript = "vart_subscript"
class BreakType(Enum):
    bt_page = "bt_page"
    bt_column = "bt_column"
    bt_text_wrapping = "bt_text_wrapping"
class StyleKindValue(Enum):
    skv_paragraph = "skv_paragraph"
    skv_character = "skv_character"
    skv_table = "skv_table"
    skv_list = "skv_list"
class UnderlineValues(Enum):
    uv_single = "uv_single"
    uv_words = "uv_words"
    uv_double = "uv_double"
    uv_thick = "uv_thick"
    uv_dotted = "uv_dotted"
    uv_dotted_heavy = "uv_dotted_heavy"
    uv_dash = "uv_dash"
    uv_dashed_heavy = "uv_dashed_heavy"
    uv_dash_long = "uv_dash_long"
    uv_dash_long_heavy = "uv_dash_long_heavy"
    uv_none = "uv_none"
    uv_dot_dash = "uv_dot_dash"
    uv_dash_dot_heavy = "uv_dash_dot_heavy"
    uv_dot_dot_dash = "uv_dot_dot_dash"
    uv_dash_dot_dot_heavy = "uv_dash_dot_dot_heavy"
    uv_wave = "uv_wave"
    uv_wavy_heavy = "uv_wavy_heavy"
    uv_wavy_double = "uv_wavy_double"
class OnOffType(Enum):
    oot_on = "oot_on"
    oot_off = "oot_off"


############################################
# Definition of Classes
############################################

class WordprocessingMLStyles_TabElt:

    pass
class WordprocessingMLStyles_PictureType:

    pass
class WordprocessingMLStyles_SectPrElt:

    pass
class WordprocessingMLStyles_ListsElt:

    pass
class WordprocessingMLStyles_StyleElt:

    def __init__(self, type: StringType, default: StringType, sti: StringType, autoRedefine: StringType, hidden: StringType, semiHidden: StringType, locked: StringType, personal: StringType, personalCompose: StringType, personalReply: StringType, styles147: "StylesElt" = None, WordprocessingMLStyles_StyleElt: "StringType" = None, WordprocessingMLStyles_StyleElt152: "StringProperty" = None, WordprocessingMLStyles_StyleElt155: "StringProperty" = None, WordprocessingMLStyles_StyleElt158: "StringProperty" = None, rpe_styleElt: "RunPrElt" = None, WordprocessingMLStyles_StyleElt161: "StringProperty" = None, WordprocessingMLStyles_StyleElt164: "StringProperty" = None, WordprocessingMLStyles_StyleElt167: "StringType" = None, ppe_styleElt: "ParaPrElt" = None, tpe_styleElt: "TablePrElt" = None, trpe_styleElt: "TableRowPrElt" = None, tcpe_styleElt: "TableCellPrElt" = None):
        self.type = type
        self.default = default
        self.sti = sti
        self.autoRedefine = autoRedefine
        self.hidden = hidden
        self.semiHidden = semiHidden
        self.locked = locked
        self.personal = personal
        self.personalCompose = personalCompose
        self.personalReply = personalReply
        self.styles147 = styles147
        self.WordprocessingMLStyles_StyleElt = WordprocessingMLStyles_StyleElt
        self.WordprocessingMLStyles_StyleElt152 = WordprocessingMLStyles_StyleElt152
        self.WordprocessingMLStyles_StyleElt155 = WordprocessingMLStyles_StyleElt155
        self.WordprocessingMLStyles_StyleElt158 = WordprocessingMLStyles_StyleElt158
        self.rpe_styleElt = rpe_styleElt
        self.WordprocessingMLStyles_StyleElt161 = WordprocessingMLStyles_StyleElt161
        self.WordprocessingMLStyles_StyleElt164 = WordprocessingMLStyles_StyleElt164
        self.WordprocessingMLStyles_StyleElt167 = WordprocessingMLStyles_StyleElt167
        self.ppe_styleElt = ppe_styleElt
        self.tpe_styleElt = tpe_styleElt
        self.trpe_styleElt = trpe_styleElt
        self.tcpe_styleElt = tcpe_styleElt
        
        pass
    @property
    def personalReply(self):
        return self.__personalReply

    @personalReply.setter
    def personalReply(self, personalReply: StringType):
        self.__personalReply = personalReply


    @property
    def locked(self):
        return self.__locked

    @locked.setter
    def locked(self, locked: StringType):
        self.__locked = locked


    @property
    def autoRedefine(self):
        return self.__autoRedefine

    @autoRedefine.setter
    def autoRedefine(self, autoRedefine: StringType):
        self.__autoRedefine = autoRedefine


    @property
    def personal(self):
        return self.__personal

    @personal.setter
    def personal(self, personal: StringType):
        self.__personal = personal


    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: StringType):
        self.__hidden = hidden


    @property
    def sti(self):
        return self.__sti

    @sti.setter
    def sti(self, sti: StringType):
        self.__sti = sti


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: StringType):
        self.__type = type


    @property
    def personalCompose(self):
        return self.__personalCompose

    @personalCompose.setter
    def personalCompose(self, personalCompose: StringType):
        self.__personalCompose = personalCompose


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: StringType):
        self.__default = default


    @property
    def semiHidden(self):
        return self.__semiHidden

    @semiHidden.setter
    def semiHidden(self, semiHidden: StringType):
        self.__semiHidden = semiHidden


    @property
    def tpe_styleElt(self):
        return self.__tpe_styleElt

    @tpe_styleElt.setter
    def tpe_styleElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__tpe_styleElt", None)
        self.__tpe_styleElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TablePrElt174"):
                opp_val = getattr(old_value, "TablePrElt174", None)
                if opp_val == self:
                    setattr(old_value, "TablePrElt174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TablePrElt174"):
                opp_val = getattr(value, "TablePrElt174", None)
                setattr(value, "TablePrElt174", self)

    @property
    def ppe_styleElt(self):
        return self.__ppe_styleElt

    @ppe_styleElt.setter
    def ppe_styleElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__ppe_styleElt", None)
        self.__ppe_styleElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ParaPrElt170"):
                opp_val = getattr(old_value, "ParaPrElt170", None)
                if opp_val == self:
                    setattr(old_value, "ParaPrElt170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ParaPrElt170"):
                opp_val = getattr(value, "ParaPrElt170", None)
                setattr(value, "ParaPrElt170", self)

    @property
    def WordprocessingMLStyles_StyleElt152(self):
        return self.__WordprocessingMLStyles_StyleElt152

    @WordprocessingMLStyles_StyleElt152.setter
    def WordprocessingMLStyles_StyleElt152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__WordprocessingMLStyles_StyleElt152", None)
        self.__WordprocessingMLStyles_StyleElt152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringProperty153"):
                opp_val = getattr(old_value, "StringProperty153", None)
                if opp_val == self:
                    setattr(old_value, "StringProperty153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringProperty153"):
                opp_val = getattr(value, "StringProperty153", None)
                setattr(value, "StringProperty153", self)

    @property
    def WordprocessingMLStyles_StyleElt161(self):
        return self.__WordprocessingMLStyles_StyleElt161

    @WordprocessingMLStyles_StyleElt161.setter
    def WordprocessingMLStyles_StyleElt161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__WordprocessingMLStyles_StyleElt161", None)
        self.__WordprocessingMLStyles_StyleElt161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringProperty162"):
                opp_val = getattr(old_value, "StringProperty162", None)
                if opp_val == self:
                    setattr(old_value, "StringProperty162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringProperty162"):
                opp_val = getattr(value, "StringProperty162", None)
                setattr(value, "StringProperty162", self)

    @property
    def WordprocessingMLStyles_StyleElt158(self):
        return self.__WordprocessingMLStyles_StyleElt158

    @WordprocessingMLStyles_StyleElt158.setter
    def WordprocessingMLStyles_StyleElt158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__WordprocessingMLStyles_StyleElt158", None)
        self.__WordprocessingMLStyles_StyleElt158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringProperty159"):
                opp_val = getattr(old_value, "StringProperty159", None)
                if opp_val == self:
                    setattr(old_value, "StringProperty159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringProperty159"):
                opp_val = getattr(value, "StringProperty159", None)
                setattr(value, "StringProperty159", self)

    @property
    def tcpe_styleElt(self):
        return self.__tcpe_styleElt

    @tcpe_styleElt.setter
    def tcpe_styleElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__tcpe_styleElt", None)
        self.__tcpe_styleElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableCellPrElt178"):
                opp_val = getattr(old_value, "TableCellPrElt178", None)
                if opp_val == self:
                    setattr(old_value, "TableCellPrElt178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableCellPrElt178"):
                opp_val = getattr(value, "TableCellPrElt178", None)
                setattr(value, "TableCellPrElt178", self)

    @property
    def WordprocessingMLStyles_StyleElt167(self):
        return self.__WordprocessingMLStyles_StyleElt167

    @WordprocessingMLStyles_StyleElt167.setter
    def WordprocessingMLStyles_StyleElt167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__WordprocessingMLStyles_StyleElt167", None)
        self.__WordprocessingMLStyles_StyleElt167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringType168"):
                opp_val = getattr(old_value, "StringType168", None)
                if opp_val == self:
                    setattr(old_value, "StringType168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringType168"):
                opp_val = getattr(value, "StringType168", None)
                setattr(value, "StringType168", self)

    @property
    def WordprocessingMLStyles_StyleElt155(self):
        return self.__WordprocessingMLStyles_StyleElt155

    @WordprocessingMLStyles_StyleElt155.setter
    def WordprocessingMLStyles_StyleElt155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__WordprocessingMLStyles_StyleElt155", None)
        self.__WordprocessingMLStyles_StyleElt155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringProperty156"):
                opp_val = getattr(old_value, "StringProperty156", None)
                if opp_val == self:
                    setattr(old_value, "StringProperty156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringProperty156"):
                opp_val = getattr(value, "StringProperty156", None)
                setattr(value, "StringProperty156", self)

    @property
    def WordprocessingMLStyles_StyleElt(self):
        return self.__WordprocessingMLStyles_StyleElt

    @WordprocessingMLStyles_StyleElt.setter
    def WordprocessingMLStyles_StyleElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__WordprocessingMLStyles_StyleElt", None)
        self.__WordprocessingMLStyles_StyleElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringType150"):
                opp_val = getattr(old_value, "StringType150", None)
                if opp_val == self:
                    setattr(old_value, "StringType150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringType150"):
                opp_val = getattr(value, "StringType150", None)
                setattr(value, "StringType150", self)

    @property
    def styles147(self):
        return self.__styles147

    @styles147.setter
    def styles147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__styles147", None)
        self.__styles147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StylesElt148"):
                opp_val = getattr(old_value, "StylesElt148", None)
                if opp_val == self:
                    setattr(old_value, "StylesElt148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StylesElt148"):
                opp_val = getattr(value, "StylesElt148", None)
                setattr(value, "StylesElt148", self)

    @property
    def trpe_styleElt(self):
        return self.__trpe_styleElt

    @trpe_styleElt.setter
    def trpe_styleElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__trpe_styleElt", None)
        self.__trpe_styleElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableRowPrElt176"):
                opp_val = getattr(old_value, "TableRowPrElt176", None)
                if opp_val == self:
                    setattr(old_value, "TableRowPrElt176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableRowPrElt176"):
                opp_val = getattr(value, "TableRowPrElt176", None)
                setattr(value, "TableRowPrElt176", self)

    @property
    def WordprocessingMLStyles_StyleElt164(self):
        return self.__WordprocessingMLStyles_StyleElt164

    @WordprocessingMLStyles_StyleElt164.setter
    def WordprocessingMLStyles_StyleElt164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__WordprocessingMLStyles_StyleElt164", None)
        self.__WordprocessingMLStyles_StyleElt164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringProperty165"):
                opp_val = getattr(old_value, "StringProperty165", None)
                if opp_val == self:
                    setattr(old_value, "StringProperty165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringProperty165"):
                opp_val = getattr(value, "StringProperty165", None)
                setattr(value, "StringProperty165", self)

    @property
    def rpe_styleElt(self):
        return self.__rpe_styleElt

    @rpe_styleElt.setter
    def rpe_styleElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StyleElt__rpe_styleElt", None)
        self.__rpe_styleElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RunPrElt172"):
                opp_val = getattr(old_value, "RunPrElt172", None)
                if opp_val == self:
                    setattr(old_value, "RunPrElt172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RunPrElt172"):
                opp_val = getattr(value, "RunPrElt172", None)
                setattr(value, "RunPrElt172", self)

class WordprocessingMLStyles_StylesElt:

    def __init__(self, versionOfBuiltInStylenames: StringType, styles: "WordDocument" = None, se_stylesElt: set["StyleElt"] = None):
        self.versionOfBuiltInStylenames = versionOfBuiltInStylenames
        self.styles = styles
        self.se_stylesElt = se_stylesElt if se_stylesElt is not None else set()
        
        pass
    @property
    def versionOfBuiltInStylenames(self):
        return self.__versionOfBuiltInStylenames

    @versionOfBuiltInStylenames.setter
    def versionOfBuiltInStylenames(self, versionOfBuiltInStylenames: StringType):
        self.__versionOfBuiltInStylenames = versionOfBuiltInStylenames


    @property
    def styles(self):
        return self.__styles

    @styles.setter
    def styles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StylesElt__styles", None)
        self.__styles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WordDocument143"):
                opp_val = getattr(old_value, "WordDocument143", None)
                if opp_val == self:
                    setattr(old_value, "WordDocument143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WordDocument143"):
                opp_val = getattr(value, "WordDocument143", None)
                setattr(value, "WordDocument143", self)

    @property
    def se_stylesElt(self):
        return self.__se_stylesElt

    @se_stylesElt.setter
    def se_stylesElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_StylesElt__se_stylesElt", None)
        self.__se_stylesElt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StyleElt145"):
                    opp_val = getattr(item, "StyleElt145", None)
                    
                    if opp_val == self:
                        setattr(item, "StyleElt145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StyleElt145"):
                    opp_val = getattr(item, "StyleElt145", None)
                    
                    setattr(item, "StyleElt145", self)
                    

class WordprocessingMLStyles_FontElt:

    pass
class WordprocessingMLStyles_FontsElt:

    def __init__(self, hint: StringType, defaultFonts: "FontsListElt" = None, rFonts: "RunPrElt" = None, WordprocessingMLStyles_FontsElt: "StringType" = None, WordprocessingMLStyles_FontsElt126: "StringType" = None, WordprocessingMLStyles_FontsElt129: "StringType" = None, WordprocessingMLStyles_FontsElt132: "StringType" = None):
        self.hint = hint
        self.defaultFonts = defaultFonts
        self.rFonts = rFonts
        self.WordprocessingMLStyles_FontsElt = WordprocessingMLStyles_FontsElt
        self.WordprocessingMLStyles_FontsElt126 = WordprocessingMLStyles_FontsElt126
        self.WordprocessingMLStyles_FontsElt129 = WordprocessingMLStyles_FontsElt129
        self.WordprocessingMLStyles_FontsElt132 = WordprocessingMLStyles_FontsElt132
        
        pass
    @property
    def hint(self):
        return self.__hint

    @hint.setter
    def hint(self, hint: StringType):
        self.__hint = hint


    @property
    def defaultFonts(self):
        return self.__defaultFonts

    @defaultFonts.setter
    def defaultFonts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_FontsElt__defaultFonts", None)
        self.__defaultFonts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FontsListElt120"):
                opp_val = getattr(old_value, "FontsListElt120", None)
                if opp_val == self:
                    setattr(old_value, "FontsListElt120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FontsListElt120"):
                opp_val = getattr(value, "FontsListElt120", None)
                setattr(value, "FontsListElt120", self)

    @property
    def rFonts(self):
        return self.__rFonts

    @rFonts.setter
    def rFonts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_FontsElt__rFonts", None)
        self.__rFonts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RunPrElt122"):
                opp_val = getattr(old_value, "RunPrElt122", None)
                if opp_val == self:
                    setattr(old_value, "RunPrElt122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RunPrElt122"):
                opp_val = getattr(value, "RunPrElt122", None)
                setattr(value, "RunPrElt122", self)

    @property
    def WordprocessingMLStyles_FontsElt126(self):
        return self.__WordprocessingMLStyles_FontsElt126

    @WordprocessingMLStyles_FontsElt126.setter
    def WordprocessingMLStyles_FontsElt126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_FontsElt__WordprocessingMLStyles_FontsElt126", None)
        self.__WordprocessingMLStyles_FontsElt126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringType127"):
                opp_val = getattr(old_value, "StringType127", None)
                if opp_val == self:
                    setattr(old_value, "StringType127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringType127"):
                opp_val = getattr(value, "StringType127", None)
                setattr(value, "StringType127", self)

    @property
    def WordprocessingMLStyles_FontsElt129(self):
        return self.__WordprocessingMLStyles_FontsElt129

    @WordprocessingMLStyles_FontsElt129.setter
    def WordprocessingMLStyles_FontsElt129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_FontsElt__WordprocessingMLStyles_FontsElt129", None)
        self.__WordprocessingMLStyles_FontsElt129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringType130"):
                opp_val = getattr(old_value, "StringType130", None)
                if opp_val == self:
                    setattr(old_value, "StringType130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringType130"):
                opp_val = getattr(value, "StringType130", None)
                setattr(value, "StringType130", self)

    @property
    def WordprocessingMLStyles_FontsElt(self):
        return self.__WordprocessingMLStyles_FontsElt

    @WordprocessingMLStyles_FontsElt.setter
    def WordprocessingMLStyles_FontsElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_FontsElt__WordprocessingMLStyles_FontsElt", None)
        self.__WordprocessingMLStyles_FontsElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringType124"):
                opp_val = getattr(old_value, "StringType124", None)
                if opp_val == self:
                    setattr(old_value, "StringType124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringType124"):
                opp_val = getattr(value, "StringType124", None)
                setattr(value, "StringType124", self)

    @property
    def WordprocessingMLStyles_FontsElt132(self):
        return self.__WordprocessingMLStyles_FontsElt132

    @WordprocessingMLStyles_FontsElt132.setter
    def WordprocessingMLStyles_FontsElt132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_FontsElt__WordprocessingMLStyles_FontsElt132", None)
        self.__WordprocessingMLStyles_FontsElt132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringType133"):
                opp_val = getattr(old_value, "StringType133", None)
                if opp_val == self:
                    setattr(old_value, "StringType133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringType133"):
                opp_val = getattr(value, "StringType133", None)
                setattr(value, "StringType133", self)

class FontElt:

    pass
class WordprocessingMLStyles_FontsListElt:

    pass
class WordprocessingMLStyles_TableCellPrElt:

    pass
class TableCellPrElt:

    pass
class WordprocessingMLStyles_TableCellElt:

    pass
class WordprocessingMLStyles_RowContentElt:

    pass
class WordprocessingMLStyles_TableRowPrElt:

    pass
class RowContentElt:

    pass
class TableRowPrElt:

    pass
class TablePrExElt:

    pass
class WordprocessingMLStyles_RowElt:

    pass
class RunLevelElt:

    pass
class RowElt:

    pass
class WordprocessingMLStyles_TableContentElt:

    pass
class WordprocessingMLStyles_TablePrExElt:

    pass
class TableElt:

    pass
class WordprocessingMLStyles_TablePrElt:

    pass
class TableContentElt:

    pass
class TableGridElt:

    pass
class TablePrElt:

    pass
class WordprocessingMLStyles_FldCharElt:

    def __init__(self, fldCharType: StringType, fldLock: StringType, WordprocessingMLStyles_FldCharElt: "StringType" = None):
        self.fldCharType = fldCharType
        self.fldLock = fldLock
        self.WordprocessingMLStyles_FldCharElt = WordprocessingMLStyles_FldCharElt
        
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
    def WordprocessingMLStyles_FldCharElt(self):
        return self.__WordprocessingMLStyles_FldCharElt

    @WordprocessingMLStyles_FldCharElt.setter
    def WordprocessingMLStyles_FldCharElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_FldCharElt__WordprocessingMLStyles_FldCharElt", None)
        self.__WordprocessingMLStyles_FldCharElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringType75"):
                opp_val = getattr(old_value, "StringType75", None)
                if opp_val == self:
                    setattr(old_value, "StringType75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringType75"):
                opp_val = getattr(value, "StringType75", None)
                setattr(value, "StringType75", self)

class WordprocessingMLStyles_TableGridElt:

    pass
class TabElt:

    pass
class WordprocessingMLStyles_SymElt:

    pass
class SymElt:

    pass
class PictureType:

    pass
class WordprocessingMLStyles_NoteElt(ABC):

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
        old_value = getattr(self, f"_WordprocessingMLStyles_NoteElt__ble_note", None)
        self.__ble_note = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BlockLevelElt69"):
                    opp_val = getattr(item, "BlockLevelElt69", None)
                    
                    if opp_val == self:
                        setattr(item, "BlockLevelElt69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BlockLevelElt69"):
                    opp_val = getattr(item, "BlockLevelElt69", None)
                    
                    setattr(item, "BlockLevelElt69", self)
                    

class FldCharElt:

    pass
class WordprocessingMLStyles_RunContentElt(ABC):

    pass
class WordprocessingMLStyles_LangElt:

    def __init__(self, val: StringType, bidi: StringType, language: "RunPrElt" = None):
        self.val = val
        self.bidi = bidi
        self.language = language
        
        pass
    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val: StringType):
        self.__val = val


    @property
    def bidi(self):
        return self.__bidi

    @bidi.setter
    def bidi(self, bidi: StringType):
        self.__bidi = bidi


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_LangElt__language", None)
        self.__language = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RunPrElt65"):
                opp_val = getattr(old_value, "RunPrElt65", None)
                if opp_val == self:
                    setattr(old_value, "RunPrElt65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RunPrElt65"):
                opp_val = getattr(value, "RunPrElt65", None)
                setattr(value, "RunPrElt65", self)

class LangElt:

    pass
class UnderlineProperty:

    pass
class FontsElt:

    pass
class RunElt:

    pass
class WordprocessingMLStyles_RunPrElt:

    def __init__(self, shadow: StringType, emboss: StringType, imprint: StringType, noProof: StringType, vanish: StringType, specVanish: StringType, rtl: StringType, color: StringType, highlight: StringType, verticalAlign: StringType, capitals: StringType, bold: StringType, bold_cs: StringType, italic: StringType, italic_cs: StringType, cs: StringType, smallCapitals: StringType, strike: StringType, doubleStrike: StringType, outline: StringType, rPr: "RunElt" = None, se_rPr: "StyleElt" = None, WordprocessingMLStyles_RunPrElt: "StringProperty" = None, fse_runPrElt: "FontsElt" = None, WordprocessingMLStyles_RunPrElt62: "UnderlineProperty" = None, le_runPrElt: "LangElt" = None):
        self.shadow = shadow
        self.emboss = emboss
        self.imprint = imprint
        self.noProof = noProof
        self.vanish = vanish
        self.specVanish = specVanish
        self.rtl = rtl
        self.color = color
        self.highlight = highlight
        self.verticalAlign = verticalAlign
        self.capitals = capitals
        self.bold = bold
        self.bold_cs = bold_cs
        self.italic = italic
        self.italic_cs = italic_cs
        self.cs = cs
        self.smallCapitals = smallCapitals
        self.strike = strike
        self.doubleStrike = doubleStrike
        self.outline = outline
        self.rPr = rPr
        self.se_rPr = se_rPr
        self.WordprocessingMLStyles_RunPrElt = WordprocessingMLStyles_RunPrElt
        self.fse_runPrElt = fse_runPrElt
        self.WordprocessingMLStyles_RunPrElt62 = WordprocessingMLStyles_RunPrElt62
        self.le_runPrElt = le_runPrElt
        
        pass
    @property
    def italic_cs(self):
        return self.__italic_cs

    @italic_cs.setter
    def italic_cs(self, italic_cs: StringType):
        self.__italic_cs = italic_cs


    @property
    def bold_cs(self):
        return self.__bold_cs

    @bold_cs.setter
    def bold_cs(self, bold_cs: StringType):
        self.__bold_cs = bold_cs


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: StringType):
        self.__color = color


    @property
    def imprint(self):
        return self.__imprint

    @imprint.setter
    def imprint(self, imprint: StringType):
        self.__imprint = imprint


    @property
    def emboss(self):
        return self.__emboss

    @emboss.setter
    def emboss(self, emboss: StringType):
        self.__emboss = emboss


    @property
    def specVanish(self):
        return self.__specVanish

    @specVanish.setter
    def specVanish(self, specVanish: StringType):
        self.__specVanish = specVanish


    @property
    def outline(self):
        return self.__outline

    @outline.setter
    def outline(self, outline: StringType):
        self.__outline = outline


    @property
    def shadow(self):
        return self.__shadow

    @shadow.setter
    def shadow(self, shadow: StringType):
        self.__shadow = shadow


    @property
    def capitals(self):
        return self.__capitals

    @capitals.setter
    def capitals(self, capitals: StringType):
        self.__capitals = capitals


    @property
    def italic(self):
        return self.__italic

    @italic.setter
    def italic(self, italic: StringType):
        self.__italic = italic


    @property
    def strike(self):
        return self.__strike

    @strike.setter
    def strike(self, strike: StringType):
        self.__strike = strike


    @property
    def cs(self):
        return self.__cs

    @cs.setter
    def cs(self, cs: StringType):
        self.__cs = cs


    @property
    def rtl(self):
        return self.__rtl

    @rtl.setter
    def rtl(self, rtl: StringType):
        self.__rtl = rtl


    @property
    def noProof(self):
        return self.__noProof

    @noProof.setter
    def noProof(self, noProof: StringType):
        self.__noProof = noProof


    @property
    def vanish(self):
        return self.__vanish

    @vanish.setter
    def vanish(self, vanish: StringType):
        self.__vanish = vanish


    @property
    def doubleStrike(self):
        return self.__doubleStrike

    @doubleStrike.setter
    def doubleStrike(self, doubleStrike: StringType):
        self.__doubleStrike = doubleStrike


    @property
    def verticalAlign(self):
        return self.__verticalAlign

    @verticalAlign.setter
    def verticalAlign(self, verticalAlign: StringType):
        self.__verticalAlign = verticalAlign


    @property
    def bold(self):
        return self.__bold

    @bold.setter
    def bold(self, bold: StringType):
        self.__bold = bold


    @property
    def smallCapitals(self):
        return self.__smallCapitals

    @smallCapitals.setter
    def smallCapitals(self, smallCapitals: StringType):
        self.__smallCapitals = smallCapitals


    @property
    def highlight(self):
        return self.__highlight

    @highlight.setter
    def highlight(self, highlight: StringType):
        self.__highlight = highlight


    @property
    def WordprocessingMLStyles_RunPrElt62(self):
        return self.__WordprocessingMLStyles_RunPrElt62

    @WordprocessingMLStyles_RunPrElt62.setter
    def WordprocessingMLStyles_RunPrElt62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_RunPrElt__WordprocessingMLStyles_RunPrElt62", None)
        self.__WordprocessingMLStyles_RunPrElt62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UnderlineProperty"):
                opp_val = getattr(old_value, "UnderlineProperty", None)
                if opp_val == self:
                    setattr(old_value, "UnderlineProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UnderlineProperty"):
                opp_val = getattr(value, "UnderlineProperty", None)
                setattr(value, "UnderlineProperty", self)

    @property
    def se_rPr(self):
        return self.__se_rPr

    @se_rPr.setter
    def se_rPr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_RunPrElt__se_rPr", None)
        self.__se_rPr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleElt57"):
                opp_val = getattr(old_value, "StyleElt57", None)
                if opp_val == self:
                    setattr(old_value, "StyleElt57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleElt57"):
                opp_val = getattr(value, "StyleElt57", None)
                setattr(value, "StyleElt57", self)

    @property
    def rPr(self):
        return self.__rPr

    @rPr.setter
    def rPr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_RunPrElt__rPr", None)
        self.__rPr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RunElt"):
                opp_val = getattr(old_value, "RunElt", None)
                if opp_val == self:
                    setattr(old_value, "RunElt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RunElt"):
                opp_val = getattr(value, "RunElt", None)
                setattr(value, "RunElt", self)

    @property
    def le_runPrElt(self):
        return self.__le_runPrElt

    @le_runPrElt.setter
    def le_runPrElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_RunPrElt__le_runPrElt", None)
        self.__le_runPrElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LangElt"):
                opp_val = getattr(old_value, "LangElt", None)
                if opp_val == self:
                    setattr(old_value, "LangElt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LangElt"):
                opp_val = getattr(value, "LangElt", None)
                setattr(value, "LangElt", self)

    @property
    def fse_runPrElt(self):
        return self.__fse_runPrElt

    @fse_runPrElt.setter
    def fse_runPrElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_RunPrElt__fse_runPrElt", None)
        self.__fse_runPrElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FontsElt"):
                opp_val = getattr(old_value, "FontsElt", None)
                if opp_val == self:
                    setattr(old_value, "FontsElt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FontsElt"):
                opp_val = getattr(value, "FontsElt", None)
                setattr(value, "FontsElt", self)

    @property
    def WordprocessingMLStyles_RunPrElt(self):
        return self.__WordprocessingMLStyles_RunPrElt

    @WordprocessingMLStyles_RunPrElt.setter
    def WordprocessingMLStyles_RunPrElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_RunPrElt__WordprocessingMLStyles_RunPrElt", None)
        self.__WordprocessingMLStyles_RunPrElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringProperty59"):
                opp_val = getattr(old_value, "StringProperty59", None)
                if opp_val == self:
                    setattr(old_value, "StringProperty59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringProperty59"):
                opp_val = getattr(value, "StringProperty59", None)
                setattr(value, "StringProperty59", self)

class RunContentElt:

    pass
class WordprocessingMLStyles_Symbol(RunContentElt, SymElt):

    pass
class WordprocessingMLStyles_ContinuationSeparator(RunContentElt):

    pass
class WordprocessingMLStyles_FldChar(FldCharElt, RunContentElt):

    pass
class WordprocessingMLStyles_Separator(RunContentElt):

    pass
class WordprocessingMLStyles_NoBreakHyphen(RunContentElt):

    pass
class WordprocessingMLStyles_AnnotationRef(RunContentElt):

    pass
class WordprocessingMLStyles_FootnoteRef(RunContentElt):

    pass
class WordprocessingMLStyles_Picture(PictureType, RunContentElt):

    pass
class WordprocessingMLStyles_PgNum(RunContentElt):

    pass
class WordprocessingMLStyles_Cr(RunContentElt):

    pass
class WordprocessingMLStyles_EndnoteRef(RunContentElt):

    pass
class WordprocessingMLStyles_Tab(RunContentElt, TabElt):

    pass
class WordprocessingMLStyles_BreakElt(RunContentElt):

    def __init__(self, type: StringType, RunContentElt: "WordprocessingMLStyles_RunElt" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: StringType):
        self.__type = type


class WordprocessingMLStyles_SoftHyphen(RunContentElt):

    pass
class RunPrElt:

    pass
class WordprocessingMLStyles_ParaContentElt(ABC):

    pass
class StyleElt:

    pass
class ParaElt:

    pass
class WordprocessingMLStyles_ParaPrElt:

    def __init__(self, keepNext: StringType, keepLines: StringType, pageBreakBefore: StringType, supressLineNumbers: StringType, suppressAutoHyphens: StringType, contextualSpacing: StringType, bidi: StringType, justification: StringType, pPr: "ParaElt" = None, se_pPr: "StyleElt" = None, WordprocessingMLStyles_ParaPrElt: "StringProperty" = None):
        self.keepNext = keepNext
        self.keepLines = keepLines
        self.pageBreakBefore = pageBreakBefore
        self.supressLineNumbers = supressLineNumbers
        self.suppressAutoHyphens = suppressAutoHyphens
        self.contextualSpacing = contextualSpacing
        self.bidi = bidi
        self.justification = justification
        self.pPr = pPr
        self.se_pPr = se_pPr
        self.WordprocessingMLStyles_ParaPrElt = WordprocessingMLStyles_ParaPrElt
        
        pass
    @property
    def bidi(self):
        return self.__bidi

    @bidi.setter
    def bidi(self, bidi: StringType):
        self.__bidi = bidi


    @property
    def justification(self):
        return self.__justification

    @justification.setter
    def justification(self, justification: StringType):
        self.__justification = justification


    @property
    def suppressAutoHyphens(self):
        return self.__suppressAutoHyphens

    @suppressAutoHyphens.setter
    def suppressAutoHyphens(self, suppressAutoHyphens: StringType):
        self.__suppressAutoHyphens = suppressAutoHyphens


    @property
    def keepNext(self):
        return self.__keepNext

    @keepNext.setter
    def keepNext(self, keepNext: StringType):
        self.__keepNext = keepNext


    @property
    def pageBreakBefore(self):
        return self.__pageBreakBefore

    @pageBreakBefore.setter
    def pageBreakBefore(self, pageBreakBefore: StringType):
        self.__pageBreakBefore = pageBreakBefore


    @property
    def supressLineNumbers(self):
        return self.__supressLineNumbers

    @supressLineNumbers.setter
    def supressLineNumbers(self, supressLineNumbers: StringType):
        self.__supressLineNumbers = supressLineNumbers


    @property
    def contextualSpacing(self):
        return self.__contextualSpacing

    @contextualSpacing.setter
    def contextualSpacing(self, contextualSpacing: StringType):
        self.__contextualSpacing = contextualSpacing


    @property
    def keepLines(self):
        return self.__keepLines

    @keepLines.setter
    def keepLines(self, keepLines: StringType):
        self.__keepLines = keepLines


    @property
    def se_pPr(self):
        return self.__se_pPr

    @se_pPr.setter
    def se_pPr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_ParaPrElt__se_pPr", None)
        self.__se_pPr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleElt"):
                opp_val = getattr(old_value, "StyleElt", None)
                if opp_val == self:
                    setattr(old_value, "StyleElt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleElt"):
                opp_val = getattr(value, "StyleElt", None)
                setattr(value, "StyleElt", self)

    @property
    def WordprocessingMLStyles_ParaPrElt(self):
        return self.__WordprocessingMLStyles_ParaPrElt

    @WordprocessingMLStyles_ParaPrElt.setter
    def WordprocessingMLStyles_ParaPrElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_ParaPrElt__WordprocessingMLStyles_ParaPrElt", None)
        self.__WordprocessingMLStyles_ParaPrElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StringProperty50"):
                opp_val = getattr(old_value, "StringProperty50", None)
                if opp_val == self:
                    setattr(old_value, "StringProperty50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StringProperty50"):
                opp_val = getattr(value, "StringProperty50", None)
                setattr(value, "StringProperty50", self)

    @property
    def pPr(self):
        return self.__pPr

    @pPr.setter
    def pPr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_ParaPrElt__pPr", None)
        self.__pPr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ParaElt"):
                opp_val = getattr(old_value, "ParaElt", None)
                if opp_val == self:
                    setattr(old_value, "ParaElt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ParaElt"):
                opp_val = getattr(value, "ParaElt", None)
                setattr(value, "ParaElt", self)

class ParaContentElt:

    pass
class WordprocessingMLStyles_RunElt(ParaContentElt):

    pass
class WordprocessingMLStyles_SubDocElt(ParaContentElt):

    pass
class WordprocessingMLStyles_SimpleFieldElt(ParaContentElt):

    pass
class WordprocessingMLStyles_HLinkElt(ParaContentElt):

    pass
class ParaPrElt:

    pass
class BlockLevelChunkElt:

    pass
class WordprocessingMLStyles_TableElt(BlockLevelChunkElt):

    pass
class WordprocessingMLStyles_RunLevelElt(BlockLevelChunkElt):

    pass
class WordprocessingMLStyles_ParaElt(BlockLevelChunkElt):

    pass
class DocPrElt:

    pass
class StylesElt:

    pass
class TableCellElt:

    pass
class NoteElt:

    pass
class WordprocessingMLStyles_Footnote(NoteElt, RunContentElt):

    pass
class WordprocessingMLStyles_Endnote(NoteElt, RunContentElt):

    pass
class WordprocessingMLStyles_BlockLevelElt(ABC):

    pass
class SectPrElt:

    pass
class BlockLevelElt:

    pass
class WordprocessingMLStyles_BlockLevelChunkElt(BlockLevelElt):

    pass
class WordprocessingMLStyles_CfChunk(BlockLevelElt):

    pass
class WordprocessingMLStyles_BodyElt:

    pass
class WordprocessingMLStyles_DocPrElt:

    pass
class BodyElt:

    pass
class WordprocessingMLStyles_WordDocument:

    pass
class ListsElt:

    pass
class FontsListElt:

    pass
class StringProperty:

    pass
class DocumentPropertiesCollection:

    pass
class WordprocessingMLStyles_UnderlineProperty:

    def __init__(self, val: StringType, color: StringType):
        self.val = val
        self.color = color
        
        pass
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: StringType):
        self.__color = color


    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val: StringType):
        self.__val = val


class WordprocessingMLStyles_StringType:

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
class WordprocessingMLStyles_DelInstrText(RunContentElt, StringType):

    pass
class WordprocessingMLStyles_Text(RunContentElt, StringType):

    pass
class WordprocessingMLStyles_InstrText(StringType, RunContentElt):

    pass
class WordprocessingMLStyles_DelText(StringType, RunContentElt):

    pass
class WordprocessingMLStyles_StringProperty(StringType):

    pass
class SmartTagType:

    pass
class WordprocessingMLStyles_SmartTagsCollection:

    pass
class SmartTagsCollection:

    pass
class WordprocessingMLStyles_SmartTagType:

    def __init__(self, namespaceuri: StringType, name: StringType, url: StringType, smartTagTypes: "SmartTagsCollection" = None):
        self.namespaceuri = namespaceuri
        self.name = name
        self.url = url
        self.smartTagTypes = smartTagTypes
        
        pass
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: StringType):
        self.__url = url


    @property
    def namespaceuri(self):
        return self.__namespaceuri

    @namespaceuri.setter
    def namespaceuri(self, namespaceuri: StringType):
        self.__namespaceuri = namespaceuri


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: StringType):
        self.__name = name


    @property
    def smartTagTypes(self):
        return self.__smartTagTypes

    @smartTagTypes.setter
    def smartTagTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_SmartTagType__smartTagTypes", None)
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

class VersionType:

    pass
class CustomDocumentPropertiesCollection:

    pass
class WordprocessingMLStyles_CustomDocumentProperty:

    def __init__(self, name: StringType, customDocumentProperties: "CustomDocumentPropertiesCollection" = None, WordprocessingMLStyles_CustomDocumentProperty: "ValueType" = None):
        self.name = name
        self.customDocumentProperties = customDocumentProperties
        self.WordprocessingMLStyles_CustomDocumentProperty = WordprocessingMLStyles_CustomDocumentProperty
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: StringType):
        self.__name = name


    @property
    def customDocumentProperties(self):
        return self.__customDocumentProperties

    @customDocumentProperties.setter
    def customDocumentProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_CustomDocumentProperty__customDocumentProperties", None)
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
    def WordprocessingMLStyles_CustomDocumentProperty(self):
        return self.__WordprocessingMLStyles_CustomDocumentProperty

    @WordprocessingMLStyles_CustomDocumentProperty.setter
    def WordprocessingMLStyles_CustomDocumentProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_CustomDocumentProperty__WordprocessingMLStyles_CustomDocumentProperty", None)
        self.__WordprocessingMLStyles_CustomDocumentProperty = value
        
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
class WordprocessingMLStyles_CustomDocumentPropertiesCollection:

    pass
class DateTimeType:

    pass
class ValueType:

    pass
class WordprocessingMLStyles_FloatValue(ValueType):

    def __init__(self, value: StringType, ValueType: "WordprocessingMLStyles_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: StringType):
        self.__value = value


class WordprocessingMLStyles_DateTimeTypeValue(ValueType):

    pass
class WordprocessingMLStyles_StringValue(ValueType):

    def __init__(self, value: StringType, ValueType: "WordprocessingMLStyles_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: StringType):
        self.__value = value


class WordprocessingMLStyles_ValueType(ABC):

    pass
class WordDocument:

    pass
class WordprocessingMLStyles_DocumentPropertiesCollection:

    def __init__(self, title: StringType, subject: StringType, keywords: StringType, description: StringType, category: StringType, author: StringType, lastAuthor: StringType, manager: StringType, company: StringType, hyperlinkBase: StringType, revision: StringType, totalTime: StringType, pages: StringType, words: StringType, characters: StringType, charactersWithSpaces: StringType, bytes: StringType, lines: StringType, paragraphs: StringType, presentationFormat: StringType, guid: StringType, appName: StringType, wd_docProperties: "WordDocument" = None, WordprocessingMLStyles_DocumentPropertiesCollection4: "DateTimeType" = None, WordprocessingMLStyles_DocumentPropertiesCollection7: "DateTimeType" = None, WordprocessingMLStyles_DocumentPropertiesCollection10: "DateTimeType" = None, WordprocessingMLStyles_DocumentPropertiesCollection: "VersionType" = None):
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
        self.revision = revision
        self.totalTime = totalTime
        self.pages = pages
        self.words = words
        self.characters = characters
        self.charactersWithSpaces = charactersWithSpaces
        self.bytes = bytes
        self.lines = lines
        self.paragraphs = paragraphs
        self.presentationFormat = presentationFormat
        self.guid = guid
        self.appName = appName
        self.wd_docProperties = wd_docProperties
        self.WordprocessingMLStyles_DocumentPropertiesCollection4 = WordprocessingMLStyles_DocumentPropertiesCollection4
        self.WordprocessingMLStyles_DocumentPropertiesCollection7 = WordprocessingMLStyles_DocumentPropertiesCollection7
        self.WordprocessingMLStyles_DocumentPropertiesCollection10 = WordprocessingMLStyles_DocumentPropertiesCollection10
        self.WordprocessingMLStyles_DocumentPropertiesCollection = WordprocessingMLStyles_DocumentPropertiesCollection
        
        pass
    @property
    def guid(self):
        return self.__guid

    @guid.setter
    def guid(self, guid: StringType):
        self.__guid = guid


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: StringType):
        self.__category = category


    @property
    def lastAuthor(self):
        return self.__lastAuthor

    @lastAuthor.setter
    def lastAuthor(self, lastAuthor: StringType):
        self.__lastAuthor = lastAuthor


    @property
    def bytes(self):
        return self.__bytes

    @bytes.setter
    def bytes(self, bytes: StringType):
        self.__bytes = bytes


    @property
    def revision(self):
        return self.__revision

    @revision.setter
    def revision(self, revision: StringType):
        self.__revision = revision


    @property
    def appName(self):
        return self.__appName

    @appName.setter
    def appName(self, appName: StringType):
        self.__appName = appName


    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager: StringType):
        self.__manager = manager


    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, words: StringType):
        self.__words = words


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: StringType):
        self.__pages = pages


    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject: StringType):
        self.__subject = subject


    @property
    def paragraphs(self):
        return self.__paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs: StringType):
        self.__paragraphs = paragraphs


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: StringType):
        self.__description = description


    @property
    def presentationFormat(self):
        return self.__presentationFormat

    @presentationFormat.setter
    def presentationFormat(self, presentationFormat: StringType):
        self.__presentationFormat = presentationFormat


    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: StringType):
        self.__keywords = keywords


    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, lines: StringType):
        self.__lines = lines


    @property
    def charactersWithSpaces(self):
        return self.__charactersWithSpaces

    @charactersWithSpaces.setter
    def charactersWithSpaces(self, charactersWithSpaces: StringType):
        self.__charactersWithSpaces = charactersWithSpaces


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
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: StringType):
        self.__author = author


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
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: StringType):
        self.__title = title


    @property
    def WordprocessingMLStyles_DocumentPropertiesCollection7(self):
        return self.__WordprocessingMLStyles_DocumentPropertiesCollection7

    @WordprocessingMLStyles_DocumentPropertiesCollection7.setter
    def WordprocessingMLStyles_DocumentPropertiesCollection7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_DocumentPropertiesCollection__WordprocessingMLStyles_DocumentPropertiesCollection7", None)
        self.__WordprocessingMLStyles_DocumentPropertiesCollection7 = value
        
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
    def WordprocessingMLStyles_DocumentPropertiesCollection(self):
        return self.__WordprocessingMLStyles_DocumentPropertiesCollection

    @WordprocessingMLStyles_DocumentPropertiesCollection.setter
    def WordprocessingMLStyles_DocumentPropertiesCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_DocumentPropertiesCollection__WordprocessingMLStyles_DocumentPropertiesCollection", None)
        self.__WordprocessingMLStyles_DocumentPropertiesCollection = value
        
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
    def WordprocessingMLStyles_DocumentPropertiesCollection10(self):
        return self.__WordprocessingMLStyles_DocumentPropertiesCollection10

    @WordprocessingMLStyles_DocumentPropertiesCollection10.setter
    def WordprocessingMLStyles_DocumentPropertiesCollection10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_DocumentPropertiesCollection__WordprocessingMLStyles_DocumentPropertiesCollection10", None)
        self.__WordprocessingMLStyles_DocumentPropertiesCollection10 = value
        
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
    def WordprocessingMLStyles_DocumentPropertiesCollection4(self):
        return self.__WordprocessingMLStyles_DocumentPropertiesCollection4

    @WordprocessingMLStyles_DocumentPropertiesCollection4.setter
    def WordprocessingMLStyles_DocumentPropertiesCollection4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_DocumentPropertiesCollection__WordprocessingMLStyles_DocumentPropertiesCollection4", None)
        self.__WordprocessingMLStyles_DocumentPropertiesCollection4 = value
        
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
    def wd_docProperties(self):
        return self.__wd_docProperties

    @wd_docProperties.setter
    def wd_docProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WordprocessingMLStyles_DocumentPropertiesCollection__wd_docProperties", None)
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

class WordprocessingMLStyles_BooleanValue(ValueType):

    def __init__(self, value: StringType, ValueType: "WordprocessingMLStyles_CustomDocumentProperty" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: StringType):
        self.__value = value


class WordprocessingMLStyles_VersionType:

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


class WordprocessingMLStyles_DateTimeType:

    def __init__(self, year: StringType, month: StringType, day: StringType, hour: StringType, minute: StringType, second: StringType):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        
        pass
    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: StringType):
        self.__month = month


    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: StringType):
        self.__second = second


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: StringType):
        self.__hour = hour


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
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: StringType):
        self.__year = year

