from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    ltr = "ltr"
    rtl = "rtl"
class TFrame(Enum):
    void = "void"
    above = "above"
    below = "below"
    hsides = "hsides"
    lhs = "lhs"
    rhs = "rhs"
    vsides = "vsides"
    box = "box"
    border = "border"
class Shape(Enum):
    default = "default"
    rect = "rect"
    circle = "circle"
    poly = "poly"
class FomeMethod(Enum):
    get = "get"
    post = "post"
class ValueType(Enum):
    data = "data"
    ref = "ref"
    object = "object"
class ButtonType(Enum):
    submit = "submit"
    reset = "reset"
    button = "button"
class Scope(Enum):
    row = "row"
    col = "col"
    rowgroup = "rowgroup"
    colgroup = "colgroup"
class CellVAlign(Enum):
    top = "top"
    middle = "middle"
    bottom = "bottom"
    baseline = "baseline"
class CellHAlign(Enum):
    right = "right"
    justify = "justify"
    char = "char"
    left = "left"
    center = "center"
class InputType(Enum):
    checkbox = "checkbox"
    radio = "radio"
    submit = "submit"
    reset = "reset"
    file = "file"
    hidden = "hidden"
    image = "image"
    button = "button"
    text = "text"
    password = "password"
class TRules(Enum):
    none = "none"
    groups = "groups"
    rows = "rows"
    cols = "cols"
    all = "all"


############################################
# Definition of Classes
############################################

class Tr:

    pass
class Cellvalign:

    pass
class Cellhalign:

    pass
class Col:

    pass
class XHTML_ColElement:

    pass
class Tbody:

    pass
class IDREFS:

    pass
class XHTML_TrElement(ABC):

    pass
class TrElement:

    pass
class MultiLength:

    pass
class XHTML_TableElement:

    pass
class Pixels:

    pass
class Colgroup:

    pass
class TableElement:

    pass
class Tfoot:

    pass
class Thead:

    pass
class ColElement:

    pass
class Caption:

    pass
class XHTML_Cellvalign(ABC):

    def __init__(self, valign: str):
        self.valign = valign
        
        pass
    @property
    def valign(self):
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign


class XHTML_Cellhalign(ABC):

    def __init__(self, align: str, XHTML_Cellhalign: "Character" = None, XHTML_Cellhalign518: "Length" = None):
        self.align = align
        self.XHTML_Cellhalign = XHTML_Cellhalign
        self.XHTML_Cellhalign518 = XHTML_Cellhalign518
        
        pass
    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def XHTML_Cellhalign(self):
        return self.__XHTML_Cellhalign

    @XHTML_Cellhalign.setter
    def XHTML_Cellhalign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Cellhalign__XHTML_Cellhalign", None)
        self.__XHTML_Cellhalign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Character516"):
                opp_val = getattr(old_value, "Character516", None)
                if opp_val == self:
                    setattr(old_value, "Character516", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Character516"):
                opp_val = getattr(value, "Character516", None)
                setattr(value, "Character516", self)

    @property
    def XHTML_Cellhalign518(self):
        return self.__XHTML_Cellhalign518

    @XHTML_Cellhalign518.setter
    def XHTML_Cellhalign518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Cellhalign__XHTML_Cellhalign518", None)
        self.__XHTML_Cellhalign518 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Length519"):
                opp_val = getattr(old_value, "Length519", None)
                if opp_val == self:
                    setattr(old_value, "Length519", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Length519"):
                opp_val = getattr(value, "Length519", None)
                setattr(value, "Length519", self)

class XHTML_FieldsetElement(ABC):

    pass
class XHTML_SelectElement(ABC):

    pass
class Option:

    pass
class SelectElement:

    pass
class Inlineforms:

    pass
class Charsets:

    pass
class ContentTypes:

    pass
class MapContent:

    pass
class XHTML_MapElementContent(ABC):

    pass
class XHTML_MapElement(ABC):

    pass
class MapElement:

    pass
class XHTML_MapContent:

    pass
class UriList:

    pass
class XHTML_ObjectElement(ABC):

    pass
class Fontstyle:

    pass
class Phrase:

    pass
class Focus:

    pass
class Specialpre:

    pass
class Coords:

    pass
class Blocktext:

    pass
class Datetime:

    pass
class Heading:

    pass
class DlElement:

    pass
class XHTML_Dd(DlElement):

    pass
class XHTML_Dt(DlElement):

    pass
class Li:

    pass
class Lists:

    pass
class Miscinline:

    pass
class EMPTY:

    pass
class XHTML_Base(EMPTY):

    pass
class XHTML_TitleBaseHeadElement:

    pass
class TitleBaseHeadElement:

    pass
class MediaDesc:

    pass
class LinkTypes:

    pass
class Attrs:

    pass
class XHTML_B(Attrs, Fontstyle):

    pass
class XHTML_H3(Attrs, Heading):

    pass
class XHTML_Th(Cellhalign, Cellvalign, TrElement, Attrs):

    def __init__(self, scope: str, XHTML_Th: set["Flow"] = None, XHTML_Th573: "Text" = None, XHTML_Th576: "CDATA" = None, XHTML_Th579: "IDREFS" = None, XHTML_Th581: "Number" = None, XHTML_Th584: "Number" = None, TrElement: "XHTML_Tr" = None):
        self.scope = scope
        self.XHTML_Th = XHTML_Th if XHTML_Th is not None else set()
        self.XHTML_Th573 = XHTML_Th573
        self.XHTML_Th576 = XHTML_Th576
        self.XHTML_Th579 = XHTML_Th579
        self.XHTML_Th581 = XHTML_Th581
        self.XHTML_Th584 = XHTML_Th584
        
        pass
    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope


    @property
    def XHTML_Th584(self):
        return self.__XHTML_Th584

    @XHTML_Th584.setter
    def XHTML_Th584(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Th__XHTML_Th584", None)
        self.__XHTML_Th584 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Number585"):
                opp_val = getattr(old_value, "Number585", None)
                if opp_val == self:
                    setattr(old_value, "Number585", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Number585"):
                opp_val = getattr(value, "Number585", None)
                setattr(value, "Number585", self)

    @property
    def XHTML_Th581(self):
        return self.__XHTML_Th581

    @XHTML_Th581.setter
    def XHTML_Th581(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Th__XHTML_Th581", None)
        self.__XHTML_Th581 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Number582"):
                opp_val = getattr(old_value, "Number582", None)
                if opp_val == self:
                    setattr(old_value, "Number582", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Number582"):
                opp_val = getattr(value, "Number582", None)
                setattr(value, "Number582", self)

    @property
    def XHTML_Th576(self):
        return self.__XHTML_Th576

    @XHTML_Th576.setter
    def XHTML_Th576(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Th__XHTML_Th576", None)
        self.__XHTML_Th576 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA577"):
                opp_val = getattr(old_value, "CDATA577", None)
                if opp_val == self:
                    setattr(old_value, "CDATA577", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA577"):
                opp_val = getattr(value, "CDATA577", None)
                setattr(value, "CDATA577", self)

    @property
    def XHTML_Th(self):
        return self.__XHTML_Th

    @XHTML_Th.setter
    def XHTML_Th(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Th__XHTML_Th", None)
        self.__XHTML_Th = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Flow571"):
                    opp_val = getattr(item, "Flow571", None)
                    
                    if opp_val == self:
                        setattr(item, "Flow571", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Flow571"):
                    opp_val = getattr(item, "Flow571", None)
                    
                    setattr(item, "Flow571", self)
                    

    @property
    def XHTML_Th579(self):
        return self.__XHTML_Th579

    @XHTML_Th579.setter
    def XHTML_Th579(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Th__XHTML_Th579", None)
        self.__XHTML_Th579 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IDREFS"):
                opp_val = getattr(old_value, "IDREFS", None)
                if opp_val == self:
                    setattr(old_value, "IDREFS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IDREFS"):
                opp_val = getattr(value, "IDREFS", None)
                setattr(value, "IDREFS", self)

    @property
    def XHTML_Th573(self):
        return self.__XHTML_Th573

    @XHTML_Th573.setter
    def XHTML_Th573(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Th__XHTML_Th573", None)
        self.__XHTML_Th573 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Text574"):
                opp_val = getattr(old_value, "Text574", None)
                if opp_val == self:
                    setattr(old_value, "Text574", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Text574"):
                opp_val = getattr(value, "Text574", None)
                setattr(value, "Text574", self)

class XHTML_Sub(Attrs, Phrase):

    pass
class XHTML_Tr(Attrs, Cellvalign, Cellhalign):

    pass
class XHTML_Code(Attrs, Phrase):

    pass
class XHTML_Li(Attrs):

    pass
class XHTML_Col(Cellhalign, Cellvalign, EMPTY, Attrs):

    pass
class XHTML_Hr(Blocktext, Attrs, EMPTY):

    pass
class XHTML_Sup(Attrs, Phrase):

    pass
class XHTML_Caption(Attrs):

    pass
class XHTML_Var(Attrs, Phrase):

    pass
class XHTML_Body(Attrs):

    pass
class XHTML_Tfoot(Attrs, Cellhalign, Cellvalign):

    pass
class XHTML_H2(Attrs, Heading):

    pass
class XHTML_H4(Attrs, Heading):

    pass
class XHTML_Input(Focus, Attrs, EMPTY, Inlineforms):

    def __init__(self, type: str, checked: str, disabled: str, readonly: str, XHTML_Input453: "ScriptExpression" = None, XHTML_Input456: "ContentTypes" = None, XHTML_Input435: "CDATA" = None, XHTML_Input438: "Number" = None, XHTML_Input441: "URI" = None, XHTML_Input444: "CDATA" = None, XHTML_Input: "CDATA" = None, XHTML_Input432: "CDATA" = None, XHTML_Input447: "URI" = None, XHTML_Input450: "ScriptExpression" = None):
        self.type = type
        self.checked = checked
        self.disabled = disabled
        self.readonly = readonly
        self.XHTML_Input453 = XHTML_Input453
        self.XHTML_Input456 = XHTML_Input456
        self.XHTML_Input435 = XHTML_Input435
        self.XHTML_Input438 = XHTML_Input438
        self.XHTML_Input441 = XHTML_Input441
        self.XHTML_Input444 = XHTML_Input444
        self.XHTML_Input = XHTML_Input
        self.XHTML_Input432 = XHTML_Input432
        self.XHTML_Input447 = XHTML_Input447
        self.XHTML_Input450 = XHTML_Input450
        
        pass
    @property
    def checked(self):
        return self.__checked

    @checked.setter
    def checked(self, checked: str):
        self.__checked = checked


    @property
    def readonly(self):
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: str):
        self.__readonly = readonly


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def disabled(self):
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: str):
        self.__disabled = disabled


    @property
    def XHTML_Input438(self):
        return self.__XHTML_Input438

    @XHTML_Input438.setter
    def XHTML_Input438(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Input__XHTML_Input438", None)
        self.__XHTML_Input438 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Number439"):
                opp_val = getattr(old_value, "Number439", None)
                if opp_val == self:
                    setattr(old_value, "Number439", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Number439"):
                opp_val = getattr(value, "Number439", None)
                setattr(value, "Number439", self)

    @property
    def XHTML_Input453(self):
        return self.__XHTML_Input453

    @XHTML_Input453.setter
    def XHTML_Input453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Input__XHTML_Input453", None)
        self.__XHTML_Input453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScriptExpression454"):
                opp_val = getattr(old_value, "ScriptExpression454", None)
                if opp_val == self:
                    setattr(old_value, "ScriptExpression454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScriptExpression454"):
                opp_val = getattr(value, "ScriptExpression454", None)
                setattr(value, "ScriptExpression454", self)

    @property
    def XHTML_Input444(self):
        return self.__XHTML_Input444

    @XHTML_Input444.setter
    def XHTML_Input444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Input__XHTML_Input444", None)
        self.__XHTML_Input444 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA445"):
                opp_val = getattr(old_value, "CDATA445", None)
                if opp_val == self:
                    setattr(old_value, "CDATA445", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA445"):
                opp_val = getattr(value, "CDATA445", None)
                setattr(value, "CDATA445", self)

    @property
    def XHTML_Input(self):
        return self.__XHTML_Input

    @XHTML_Input.setter
    def XHTML_Input(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Input__XHTML_Input", None)
        self.__XHTML_Input = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA430"):
                opp_val = getattr(old_value, "CDATA430", None)
                if opp_val == self:
                    setattr(old_value, "CDATA430", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA430"):
                opp_val = getattr(value, "CDATA430", None)
                setattr(value, "CDATA430", self)

    @property
    def XHTML_Input456(self):
        return self.__XHTML_Input456

    @XHTML_Input456.setter
    def XHTML_Input456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Input__XHTML_Input456", None)
        self.__XHTML_Input456 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContentTypes457"):
                opp_val = getattr(old_value, "ContentTypes457", None)
                if opp_val == self:
                    setattr(old_value, "ContentTypes457", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContentTypes457"):
                opp_val = getattr(value, "ContentTypes457", None)
                setattr(value, "ContentTypes457", self)

    @property
    def XHTML_Input450(self):
        return self.__XHTML_Input450

    @XHTML_Input450.setter
    def XHTML_Input450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Input__XHTML_Input450", None)
        self.__XHTML_Input450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScriptExpression451"):
                opp_val = getattr(old_value, "ScriptExpression451", None)
                if opp_val == self:
                    setattr(old_value, "ScriptExpression451", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScriptExpression451"):
                opp_val = getattr(value, "ScriptExpression451", None)
                setattr(value, "ScriptExpression451", self)

    @property
    def XHTML_Input447(self):
        return self.__XHTML_Input447

    @XHTML_Input447.setter
    def XHTML_Input447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Input__XHTML_Input447", None)
        self.__XHTML_Input447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI448"):
                opp_val = getattr(old_value, "URI448", None)
                if opp_val == self:
                    setattr(old_value, "URI448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI448"):
                opp_val = getattr(value, "URI448", None)
                setattr(value, "URI448", self)

    @property
    def XHTML_Input441(self):
        return self.__XHTML_Input441

    @XHTML_Input441.setter
    def XHTML_Input441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Input__XHTML_Input441", None)
        self.__XHTML_Input441 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI442"):
                opp_val = getattr(old_value, "URI442", None)
                if opp_val == self:
                    setattr(old_value, "URI442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI442"):
                opp_val = getattr(value, "URI442", None)
                setattr(value, "URI442", self)

    @property
    def XHTML_Input432(self):
        return self.__XHTML_Input432

    @XHTML_Input432.setter
    def XHTML_Input432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Input__XHTML_Input432", None)
        self.__XHTML_Input432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA433"):
                opp_val = getattr(old_value, "CDATA433", None)
                if opp_val == self:
                    setattr(old_value, "CDATA433", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA433"):
                opp_val = getattr(value, "CDATA433", None)
                setattr(value, "CDATA433", self)

    @property
    def XHTML_Input435(self):
        return self.__XHTML_Input435

    @XHTML_Input435.setter
    def XHTML_Input435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Input__XHTML_Input435", None)
        self.__XHTML_Input435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA436"):
                opp_val = getattr(old_value, "CDATA436", None)
                if opp_val == self:
                    setattr(old_value, "CDATA436", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA436"):
                opp_val = getattr(value, "CDATA436", None)
                setattr(value, "CDATA436", self)

class XHTML_Td(Cellhalign, Cellvalign, TrElement, Attrs):

    def __init__(self, scope: str, XHTML_Td592: "CDATA" = None, XHTML_Td: set["Flow"] = None, XHTML_Td589: "Text" = None, XHTML_Td595: "IDREFS" = None, XHTML_Td598: "Number" = None, XHTML_Td601: "Number" = None, TrElement: "XHTML_Tr" = None):
        self.scope = scope
        self.XHTML_Td592 = XHTML_Td592
        self.XHTML_Td = XHTML_Td if XHTML_Td is not None else set()
        self.XHTML_Td589 = XHTML_Td589
        self.XHTML_Td595 = XHTML_Td595
        self.XHTML_Td598 = XHTML_Td598
        self.XHTML_Td601 = XHTML_Td601
        
        pass
    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope


    @property
    def XHTML_Td595(self):
        return self.__XHTML_Td595

    @XHTML_Td595.setter
    def XHTML_Td595(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Td__XHTML_Td595", None)
        self.__XHTML_Td595 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IDREFS596"):
                opp_val = getattr(old_value, "IDREFS596", None)
                if opp_val == self:
                    setattr(old_value, "IDREFS596", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IDREFS596"):
                opp_val = getattr(value, "IDREFS596", None)
                setattr(value, "IDREFS596", self)

    @property
    def XHTML_Td589(self):
        return self.__XHTML_Td589

    @XHTML_Td589.setter
    def XHTML_Td589(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Td__XHTML_Td589", None)
        self.__XHTML_Td589 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Text590"):
                opp_val = getattr(old_value, "Text590", None)
                if opp_val == self:
                    setattr(old_value, "Text590", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Text590"):
                opp_val = getattr(value, "Text590", None)
                setattr(value, "Text590", self)

    @property
    def XHTML_Td592(self):
        return self.__XHTML_Td592

    @XHTML_Td592.setter
    def XHTML_Td592(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Td__XHTML_Td592", None)
        self.__XHTML_Td592 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA593"):
                opp_val = getattr(old_value, "CDATA593", None)
                if opp_val == self:
                    setattr(old_value, "CDATA593", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA593"):
                opp_val = getattr(value, "CDATA593", None)
                setattr(value, "CDATA593", self)

    @property
    def XHTML_Td(self):
        return self.__XHTML_Td

    @XHTML_Td.setter
    def XHTML_Td(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Td__XHTML_Td", None)
        self.__XHTML_Td = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Flow587"):
                    opp_val = getattr(item, "Flow587", None)
                    
                    if opp_val == self:
                        setattr(item, "Flow587", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Flow587"):
                    opp_val = getattr(item, "Flow587", None)
                    
                    setattr(item, "Flow587", self)
                    

    @property
    def XHTML_Td598(self):
        return self.__XHTML_Td598

    @XHTML_Td598.setter
    def XHTML_Td598(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Td__XHTML_Td598", None)
        self.__XHTML_Td598 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Number599"):
                opp_val = getattr(old_value, "Number599", None)
                if opp_val == self:
                    setattr(old_value, "Number599", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Number599"):
                opp_val = getattr(value, "Number599", None)
                setattr(value, "Number599", self)

    @property
    def XHTML_Td601(self):
        return self.__XHTML_Td601

    @XHTML_Td601.setter
    def XHTML_Td601(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Td__XHTML_Td601", None)
        self.__XHTML_Td601 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Number602"):
                opp_val = getattr(old_value, "Number602", None)
                if opp_val == self:
                    setattr(old_value, "Number602", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Number602"):
                opp_val = getattr(value, "Number602", None)
                setattr(value, "Number602", self)

class XHTML_Abbr(Attrs, Phrase):

    pass
class XHTML_Pre(Blocktext, Attrs):

    def __init__(self, xml_space: str, XHTML_Pre: set["PreContent"] = None):
        self.xml_space = xml_space
        self.XHTML_Pre = XHTML_Pre if XHTML_Pre is not None else set()
        
        pass
    @property
    def xml_space(self):
        return self.__xml_space

    @xml_space.setter
    def xml_space(self, xml_space: str):
        self.__xml_space = xml_space


    @property
    def XHTML_Pre(self):
        return self.__XHTML_Pre

    @XHTML_Pre.setter
    def XHTML_Pre(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Pre__XHTML_Pre", None)
        self.__XHTML_Pre = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PreContent"):
                    opp_val = getattr(item, "PreContent", None)
                    
                    if opp_val == self:
                        setattr(item, "PreContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PreContent"):
                    opp_val = getattr(item, "PreContent", None)
                    
                    setattr(item, "PreContent", self)
                    

class XHTML_Ol(Lists, Attrs):

    pass
class XHTML_Dl(Lists, Attrs):

    pass
class XHTML_Span(Attrs, Specialpre):

    pass
class XHTML_Small(Attrs, Fontstyle):

    pass
class XHTML_Ins(Attrs, Miscinline):

    pass
class XHTML_Big(Attrs, Fontstyle):

    pass
class XHTML_Address(Blocktext, Attrs):

    pass
class XHTML_H5(Attrs, Heading):

    pass
class XHTML_I(Attrs, Fontstyle):

    pass
class XHTML_Ul(Lists, Attrs):

    pass
class XHTML_Em(Attrs, Phrase):

    pass
class XHTML_Kbd(Attrs, Phrase):

    pass
class XHTML_Colgroup(Cellhalign, Cellvalign, Attrs):

    pass
class XHTML_Q(Attrs, Phrase):

    pass
class XHTML_Del(Attrs, Miscinline):

    pass
class XHTML_Area(Focus, Attrs, EMPTY, MapElement):

    def __init__(self, shape: str, nohref: str, XHTML_Area: "Coords" = None, XHTML_Area393: "URI" = None, XHTML_Area396: "Text" = None, MapElement: "XHTML_MapContent" = None):
        self.shape = shape
        self.nohref = nohref
        self.XHTML_Area = XHTML_Area
        self.XHTML_Area393 = XHTML_Area393
        self.XHTML_Area396 = XHTML_Area396
        
        pass
    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


    @property
    def nohref(self):
        return self.__nohref

    @nohref.setter
    def nohref(self, nohref: str):
        self.__nohref = nohref


    @property
    def XHTML_Area393(self):
        return self.__XHTML_Area393

    @XHTML_Area393.setter
    def XHTML_Area393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Area__XHTML_Area393", None)
        self.__XHTML_Area393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI394"):
                opp_val = getattr(old_value, "URI394", None)
                if opp_val == self:
                    setattr(old_value, "URI394", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI394"):
                opp_val = getattr(value, "URI394", None)
                setattr(value, "URI394", self)

    @property
    def XHTML_Area(self):
        return self.__XHTML_Area

    @XHTML_Area.setter
    def XHTML_Area(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Area__XHTML_Area", None)
        self.__XHTML_Area = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Coords391"):
                opp_val = getattr(old_value, "Coords391", None)
                if opp_val == self:
                    setattr(old_value, "Coords391", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Coords391"):
                opp_val = getattr(value, "Coords391", None)
                setattr(value, "Coords391", self)

    @property
    def XHTML_Area396(self):
        return self.__XHTML_Area396

    @XHTML_Area396.setter
    def XHTML_Area396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Area__XHTML_Area396", None)
        self.__XHTML_Area396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Text397"):
                opp_val = getattr(old_value, "Text397", None)
                if opp_val == self:
                    setattr(old_value, "Text397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Text397"):
                opp_val = getattr(value, "Text397", None)
                setattr(value, "Text397", self)

class XHTML_Blockquote(Blocktext, Attrs):

    pass
class XHTML_Select(Attrs, Inlineforms):

    def __init__(self, multiple: str, disabled: str, XHTML_Select: set["SelectElement"] = None, XHTML_Select460: "CDATA" = None, XHTML_Select463: "Number" = None, XHTML_Select466: "Number" = None, XHTML_Select469: "ScriptExpression" = None, XHTML_Select472: "ScriptExpression" = None, XHTML_Select475: "ScriptExpression" = None):
        self.multiple = multiple
        self.disabled = disabled
        self.XHTML_Select = XHTML_Select if XHTML_Select is not None else set()
        self.XHTML_Select460 = XHTML_Select460
        self.XHTML_Select463 = XHTML_Select463
        self.XHTML_Select466 = XHTML_Select466
        self.XHTML_Select469 = XHTML_Select469
        self.XHTML_Select472 = XHTML_Select472
        self.XHTML_Select475 = XHTML_Select475
        
        pass
    @property
    def disabled(self):
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: str):
        self.__disabled = disabled


    @property
    def multiple(self):
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: str):
        self.__multiple = multiple


    @property
    def XHTML_Select472(self):
        return self.__XHTML_Select472

    @XHTML_Select472.setter
    def XHTML_Select472(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Select__XHTML_Select472", None)
        self.__XHTML_Select472 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScriptExpression473"):
                opp_val = getattr(old_value, "ScriptExpression473", None)
                if opp_val == self:
                    setattr(old_value, "ScriptExpression473", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScriptExpression473"):
                opp_val = getattr(value, "ScriptExpression473", None)
                setattr(value, "ScriptExpression473", self)

    @property
    def XHTML_Select469(self):
        return self.__XHTML_Select469

    @XHTML_Select469.setter
    def XHTML_Select469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Select__XHTML_Select469", None)
        self.__XHTML_Select469 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScriptExpression470"):
                opp_val = getattr(old_value, "ScriptExpression470", None)
                if opp_val == self:
                    setattr(old_value, "ScriptExpression470", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScriptExpression470"):
                opp_val = getattr(value, "ScriptExpression470", None)
                setattr(value, "ScriptExpression470", self)

    @property
    def XHTML_Select463(self):
        return self.__XHTML_Select463

    @XHTML_Select463.setter
    def XHTML_Select463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Select__XHTML_Select463", None)
        self.__XHTML_Select463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Number464"):
                opp_val = getattr(old_value, "Number464", None)
                if opp_val == self:
                    setattr(old_value, "Number464", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Number464"):
                opp_val = getattr(value, "Number464", None)
                setattr(value, "Number464", self)

    @property
    def XHTML_Select460(self):
        return self.__XHTML_Select460

    @XHTML_Select460.setter
    def XHTML_Select460(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Select__XHTML_Select460", None)
        self.__XHTML_Select460 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA461"):
                opp_val = getattr(old_value, "CDATA461", None)
                if opp_val == self:
                    setattr(old_value, "CDATA461", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA461"):
                opp_val = getattr(value, "CDATA461", None)
                setattr(value, "CDATA461", self)

    @property
    def XHTML_Select(self):
        return self.__XHTML_Select

    @XHTML_Select.setter
    def XHTML_Select(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Select__XHTML_Select", None)
        self.__XHTML_Select = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SelectElement"):
                    opp_val = getattr(item, "SelectElement", None)
                    
                    if opp_val == self:
                        setattr(item, "SelectElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SelectElement"):
                    opp_val = getattr(item, "SelectElement", None)
                    
                    setattr(item, "SelectElement", self)
                    

    @property
    def XHTML_Select475(self):
        return self.__XHTML_Select475

    @XHTML_Select475.setter
    def XHTML_Select475(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Select__XHTML_Select475", None)
        self.__XHTML_Select475 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScriptExpression476"):
                opp_val = getattr(old_value, "ScriptExpression476", None)
                if opp_val == self:
                    setattr(old_value, "ScriptExpression476", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScriptExpression476"):
                opp_val = getattr(value, "ScriptExpression476", None)
                setattr(value, "ScriptExpression476", self)

    @property
    def XHTML_Select466(self):
        return self.__XHTML_Select466

    @XHTML_Select466.setter
    def XHTML_Select466(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Select__XHTML_Select466", None)
        self.__XHTML_Select466 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Number467"):
                opp_val = getattr(old_value, "Number467", None)
                if opp_val == self:
                    setattr(old_value, "Number467", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Number467"):
                opp_val = getattr(value, "Number467", None)
                setattr(value, "Number467", self)

class XHTML_DlElement(Attrs):

    pass
class XHTML_H6(Attrs, Heading):

    pass
class XHTML_Dfn(Attrs, Phrase):

    pass
class XHTML_Samp(Attrs, Phrase):

    pass
class XHTML_Cite(Attrs, Phrase):

    pass
class XHTML_Strong(Attrs, Phrase):

    pass
class XHTML_Tbody(Attrs, Cellhalign, Cellvalign):

    pass
class XHTML_Acronym(Attrs, Phrase):

    pass
class XHTML_Tt(Attrs, Fontstyle):

    pass
class XHTML_Optgroup(SelectElement, Attrs):

    def __init__(self, disabled: str, XHTML_Optgroup: set["Option"] = None, XHTML_Optgroup479: "Text" = None, SelectElement: "XHTML_Select" = None):
        self.disabled = disabled
        self.XHTML_Optgroup = XHTML_Optgroup if XHTML_Optgroup is not None else set()
        self.XHTML_Optgroup479 = XHTML_Optgroup479
        
        pass
    @property
    def disabled(self):
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: str):
        self.__disabled = disabled


    @property
    def XHTML_Optgroup479(self):
        return self.__XHTML_Optgroup479

    @XHTML_Optgroup479.setter
    def XHTML_Optgroup479(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Optgroup__XHTML_Optgroup479", None)
        self.__XHTML_Optgroup479 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Text480"):
                opp_val = getattr(old_value, "Text480", None)
                if opp_val == self:
                    setattr(old_value, "Text480", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Text480"):
                opp_val = getattr(value, "Text480", None)
                setattr(value, "Text480", self)

    @property
    def XHTML_Optgroup(self):
        return self.__XHTML_Optgroup

    @XHTML_Optgroup.setter
    def XHTML_Optgroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Optgroup__XHTML_Optgroup", None)
        self.__XHTML_Optgroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Option"):
                    opp_val = getattr(item, "Option", None)
                    
                    if opp_val == self:
                        setattr(item, "Option", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Option"):
                    opp_val = getattr(item, "Option", None)
                    
                    setattr(item, "Option", self)
                    

class XHTML_Thead(Cellhalign, Cellvalign, Attrs):

    pass
class XHTML_Label(Attrs, Inlineforms):

    pass
class XHTML_Button(Focus, Attrs, Inlineforms):

    def __init__(self, type: str, disabled: str, XHTML_Button: set["ButtonContent"] = None, XHTML_Button510: "CDATA" = None, XHTML_Button513: "CDATA" = None):
        self.type = type
        self.disabled = disabled
        self.XHTML_Button = XHTML_Button if XHTML_Button is not None else set()
        self.XHTML_Button510 = XHTML_Button510
        self.XHTML_Button513 = XHTML_Button513
        
        pass
    @property
    def disabled(self):
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: str):
        self.__disabled = disabled


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def XHTML_Button(self):
        return self.__XHTML_Button

    @XHTML_Button.setter
    def XHTML_Button(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Button__XHTML_Button", None)
        self.__XHTML_Button = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ButtonContent"):
                    opp_val = getattr(item, "ButtonContent", None)
                    
                    if opp_val == self:
                        setattr(item, "ButtonContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ButtonContent"):
                    opp_val = getattr(item, "ButtonContent", None)
                    
                    setattr(item, "ButtonContent", self)
                    

    @property
    def XHTML_Button510(self):
        return self.__XHTML_Button510

    @XHTML_Button510.setter
    def XHTML_Button510(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Button__XHTML_Button510", None)
        self.__XHTML_Button510 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA511"):
                opp_val = getattr(old_value, "CDATA511", None)
                if opp_val == self:
                    setattr(old_value, "CDATA511", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA511"):
                opp_val = getattr(value, "CDATA511", None)
                setattr(value, "CDATA511", self)

    @property
    def XHTML_Button513(self):
        return self.__XHTML_Button513

    @XHTML_Button513.setter
    def XHTML_Button513(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Button__XHTML_Button513", None)
        self.__XHTML_Button513 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA514"):
                opp_val = getattr(old_value, "CDATA514", None)
                if opp_val == self:
                    setattr(old_value, "CDATA514", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA514"):
                opp_val = getattr(value, "CDATA514", None)
                setattr(value, "CDATA514", self)

class XHTML_H1(Attrs, Heading):

    pass
class Html:

    pass
class HeadElement:

    pass
class HeadMisc:

    pass
class XHTML_Meta(HeadMisc, EMPTY):

    pass
class XHTML_Link(HeadMisc, Attrs, EMPTY):

    pass
class XHTML_Head:

    pass
class XHTML_HeadMisc(ABC):

    pass
class Body:

    pass
class XHTML_BaseHeadElement(HeadElement):

    pass
class Base:

    pass
class XHTML_BaseTitleHeadElement:

    pass
class BaseTitleHeadElement:

    pass
class Title:

    pass
class XHTML_TitleHeadElement(HeadElement):

    pass
class XHTML_HeadElement(ABC):

    pass
class XHTML_AContent(ABC):

    pass
class XHTML_Flow(ABC):

    pass
class XHTML_Block(ABC):

    pass
class Head:

    pass
class XHTML_Html:

    pass
class XHTML_ButtonContent(ABC):

    pass
class XHTML_FormContent(ABC):

    pass
class XHTML_PreContent(ABC):

    pass
class AContent:

    pass
class ButtonContent:

    pass
class inline:

    pass
class XHTML_Special(ButtonContent, inline):

    pass
class PreContent:

    pass
class XHTML_Phrase(ButtonContent, PreContent, AContent, inline):

    pass
class XHTML_Fontstyle(AContent, PreContent, inline, ButtonContent):

    pass
class XHTML_A(Focus, Attrs, PreContent, inline):

    def __init__(self, shape: str, XHTML_A: set["AContent"] = None, XHTML_A237: "Charset" = None, XHTML_A240: "ContentType" = None, XHTML_A243: "NMTOKEN" = None, XHTML_A245: "URI" = None, XHTML_A248: "LanguageCode" = None, XHTML_A251: "LinkTypes" = None, XHTML_A254: "LinkTypes" = None, XHTML_A257: "Coords" = None, PreContent: "XHTML_Pre" = None):
        self.shape = shape
        self.XHTML_A = XHTML_A if XHTML_A is not None else set()
        self.XHTML_A237 = XHTML_A237
        self.XHTML_A240 = XHTML_A240
        self.XHTML_A243 = XHTML_A243
        self.XHTML_A245 = XHTML_A245
        self.XHTML_A248 = XHTML_A248
        self.XHTML_A251 = XHTML_A251
        self.XHTML_A254 = XHTML_A254
        self.XHTML_A257 = XHTML_A257
        
        pass
    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


    @property
    def XHTML_A243(self):
        return self.__XHTML_A243

    @XHTML_A243.setter
    def XHTML_A243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_A__XHTML_A243", None)
        self.__XHTML_A243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NMTOKEN"):
                opp_val = getattr(old_value, "NMTOKEN", None)
                if opp_val == self:
                    setattr(old_value, "NMTOKEN", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NMTOKEN"):
                opp_val = getattr(value, "NMTOKEN", None)
                setattr(value, "NMTOKEN", self)

    @property
    def XHTML_A237(self):
        return self.__XHTML_A237

    @XHTML_A237.setter
    def XHTML_A237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_A__XHTML_A237", None)
        self.__XHTML_A237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Charset238"):
                opp_val = getattr(old_value, "Charset238", None)
                if opp_val == self:
                    setattr(old_value, "Charset238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Charset238"):
                opp_val = getattr(value, "Charset238", None)
                setattr(value, "Charset238", self)

    @property
    def XHTML_A240(self):
        return self.__XHTML_A240

    @XHTML_A240.setter
    def XHTML_A240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_A__XHTML_A240", None)
        self.__XHTML_A240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContentType241"):
                opp_val = getattr(old_value, "ContentType241", None)
                if opp_val == self:
                    setattr(old_value, "ContentType241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContentType241"):
                opp_val = getattr(value, "ContentType241", None)
                setattr(value, "ContentType241", self)

    @property
    def XHTML_A248(self):
        return self.__XHTML_A248

    @XHTML_A248.setter
    def XHTML_A248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_A__XHTML_A248", None)
        self.__XHTML_A248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LanguageCode249"):
                opp_val = getattr(old_value, "LanguageCode249", None)
                if opp_val == self:
                    setattr(old_value, "LanguageCode249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LanguageCode249"):
                opp_val = getattr(value, "LanguageCode249", None)
                setattr(value, "LanguageCode249", self)

    @property
    def XHTML_A245(self):
        return self.__XHTML_A245

    @XHTML_A245.setter
    def XHTML_A245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_A__XHTML_A245", None)
        self.__XHTML_A245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI246"):
                opp_val = getattr(old_value, "URI246", None)
                if opp_val == self:
                    setattr(old_value, "URI246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI246"):
                opp_val = getattr(value, "URI246", None)
                setattr(value, "URI246", self)

    @property
    def XHTML_A254(self):
        return self.__XHTML_A254

    @XHTML_A254.setter
    def XHTML_A254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_A__XHTML_A254", None)
        self.__XHTML_A254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LinkTypes255"):
                opp_val = getattr(old_value, "LinkTypes255", None)
                if opp_val == self:
                    setattr(old_value, "LinkTypes255", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LinkTypes255"):
                opp_val = getattr(value, "LinkTypes255", None)
                setattr(value, "LinkTypes255", self)

    @property
    def XHTML_A(self):
        return self.__XHTML_A

    @XHTML_A.setter
    def XHTML_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_A__XHTML_A", None)
        self.__XHTML_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AContent"):
                    opp_val = getattr(item, "AContent", None)
                    
                    if opp_val == self:
                        setattr(item, "AContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AContent"):
                    opp_val = getattr(item, "AContent", None)
                    
                    setattr(item, "AContent", self)
                    

    @property
    def XHTML_A251(self):
        return self.__XHTML_A251

    @XHTML_A251.setter
    def XHTML_A251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_A__XHTML_A251", None)
        self.__XHTML_A251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LinkTypes252"):
                opp_val = getattr(old_value, "LinkTypes252", None)
                if opp_val == self:
                    setattr(old_value, "LinkTypes252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LinkTypes252"):
                opp_val = getattr(value, "LinkTypes252", None)
                setattr(value, "LinkTypes252", self)

    @property
    def XHTML_A257(self):
        return self.__XHTML_A257

    @XHTML_A257.setter
    def XHTML_A257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_A__XHTML_A257", None)
        self.__XHTML_A257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Coords"):
                opp_val = getattr(old_value, "Coords", None)
                if opp_val == self:
                    setattr(old_value, "Coords", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Coords"):
                opp_val = getattr(value, "Coords", None)
                setattr(value, "Coords", self)

class Special:

    pass
class XHTML_Object(Special, Attrs, HeadMisc):

    def __init__(self, declare: str, XHTML_Object311: "URI" = None, XHTML_Object314: "URI" = None, XHTML_Object317: "URI" = None, XHTML_Object320: "ContentType" = None, XHTML_Object323: "ContentType" = None, XHTML_Object326: "UriList" = None, XHTML_Object328: "Text" = None, XHTML_Object334: "Length" = None, XHTML_Object337: "URI" = None, XHTML_Object340: "NMTOKEN" = None, XHTML_Object343: "Number" = None, XHTML_Object331: "Length" = None, XHTML_Object: set["ObjectElement"] = None, HeadMisc99: "XHTML_BaseHeadElement" = None, HeadMisc: "XHTML_Head" = None, HeadMisc106: "XHTML_TitleBaseHeadElement" = None, HeadMisc94: "XHTML_BaseTitleHeadElement" = None, HeadMisc88: "XHTML_TitleHeadElement" = None):
        self.declare = declare
        self.XHTML_Object311 = XHTML_Object311
        self.XHTML_Object314 = XHTML_Object314
        self.XHTML_Object317 = XHTML_Object317
        self.XHTML_Object320 = XHTML_Object320
        self.XHTML_Object323 = XHTML_Object323
        self.XHTML_Object326 = XHTML_Object326
        self.XHTML_Object328 = XHTML_Object328
        self.XHTML_Object334 = XHTML_Object334
        self.XHTML_Object337 = XHTML_Object337
        self.XHTML_Object340 = XHTML_Object340
        self.XHTML_Object343 = XHTML_Object343
        self.XHTML_Object331 = XHTML_Object331
        self.XHTML_Object = XHTML_Object if XHTML_Object is not None else set()
        
        pass
    @property
    def declare(self):
        return self.__declare

    @declare.setter
    def declare(self, declare: str):
        self.__declare = declare


    @property
    def XHTML_Object331(self):
        return self.__XHTML_Object331

    @XHTML_Object331.setter
    def XHTML_Object331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object331", None)
        self.__XHTML_Object331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Length332"):
                opp_val = getattr(old_value, "Length332", None)
                if opp_val == self:
                    setattr(old_value, "Length332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Length332"):
                opp_val = getattr(value, "Length332", None)
                setattr(value, "Length332", self)

    @property
    def XHTML_Object323(self):
        return self.__XHTML_Object323

    @XHTML_Object323.setter
    def XHTML_Object323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object323", None)
        self.__XHTML_Object323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContentType324"):
                opp_val = getattr(old_value, "ContentType324", None)
                if opp_val == self:
                    setattr(old_value, "ContentType324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContentType324"):
                opp_val = getattr(value, "ContentType324", None)
                setattr(value, "ContentType324", self)

    @property
    def XHTML_Object337(self):
        return self.__XHTML_Object337

    @XHTML_Object337.setter
    def XHTML_Object337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object337", None)
        self.__XHTML_Object337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI338"):
                opp_val = getattr(old_value, "URI338", None)
                if opp_val == self:
                    setattr(old_value, "URI338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI338"):
                opp_val = getattr(value, "URI338", None)
                setattr(value, "URI338", self)

    @property
    def XHTML_Object326(self):
        return self.__XHTML_Object326

    @XHTML_Object326.setter
    def XHTML_Object326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object326", None)
        self.__XHTML_Object326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UriList"):
                opp_val = getattr(old_value, "UriList", None)
                if opp_val == self:
                    setattr(old_value, "UriList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UriList"):
                opp_val = getattr(value, "UriList", None)
                setattr(value, "UriList", self)

    @property
    def XHTML_Object320(self):
        return self.__XHTML_Object320

    @XHTML_Object320.setter
    def XHTML_Object320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object320", None)
        self.__XHTML_Object320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContentType321"):
                opp_val = getattr(old_value, "ContentType321", None)
                if opp_val == self:
                    setattr(old_value, "ContentType321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContentType321"):
                opp_val = getattr(value, "ContentType321", None)
                setattr(value, "ContentType321", self)

    @property
    def XHTML_Object343(self):
        return self.__XHTML_Object343

    @XHTML_Object343.setter
    def XHTML_Object343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object343", None)
        self.__XHTML_Object343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Number344"):
                opp_val = getattr(old_value, "Number344", None)
                if opp_val == self:
                    setattr(old_value, "Number344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Number344"):
                opp_val = getattr(value, "Number344", None)
                setattr(value, "Number344", self)

    @property
    def XHTML_Object314(self):
        return self.__XHTML_Object314

    @XHTML_Object314.setter
    def XHTML_Object314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object314", None)
        self.__XHTML_Object314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI315"):
                opp_val = getattr(old_value, "URI315", None)
                if opp_val == self:
                    setattr(old_value, "URI315", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI315"):
                opp_val = getattr(value, "URI315", None)
                setattr(value, "URI315", self)

    @property
    def XHTML_Object334(self):
        return self.__XHTML_Object334

    @XHTML_Object334.setter
    def XHTML_Object334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object334", None)
        self.__XHTML_Object334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Length335"):
                opp_val = getattr(old_value, "Length335", None)
                if opp_val == self:
                    setattr(old_value, "Length335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Length335"):
                opp_val = getattr(value, "Length335", None)
                setattr(value, "Length335", self)

    @property
    def XHTML_Object340(self):
        return self.__XHTML_Object340

    @XHTML_Object340.setter
    def XHTML_Object340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object340", None)
        self.__XHTML_Object340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NMTOKEN341"):
                opp_val = getattr(old_value, "NMTOKEN341", None)
                if opp_val == self:
                    setattr(old_value, "NMTOKEN341", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NMTOKEN341"):
                opp_val = getattr(value, "NMTOKEN341", None)
                setattr(value, "NMTOKEN341", self)

    @property
    def XHTML_Object(self):
        return self.__XHTML_Object

    @XHTML_Object.setter
    def XHTML_Object(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object", None)
        self.__XHTML_Object = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ObjectElement"):
                    opp_val = getattr(item, "ObjectElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ObjectElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ObjectElement"):
                    opp_val = getattr(item, "ObjectElement", None)
                    
                    setattr(item, "ObjectElement", self)
                    

    @property
    def XHTML_Object311(self):
        return self.__XHTML_Object311

    @XHTML_Object311.setter
    def XHTML_Object311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object311", None)
        self.__XHTML_Object311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI312"):
                opp_val = getattr(old_value, "URI312", None)
                if opp_val == self:
                    setattr(old_value, "URI312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI312"):
                opp_val = getattr(value, "URI312", None)
                setattr(value, "URI312", self)

    @property
    def XHTML_Object328(self):
        return self.__XHTML_Object328

    @XHTML_Object328.setter
    def XHTML_Object328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object328", None)
        self.__XHTML_Object328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Text329"):
                opp_val = getattr(old_value, "Text329", None)
                if opp_val == self:
                    setattr(old_value, "Text329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Text329"):
                opp_val = getattr(value, "Text329", None)
                setattr(value, "Text329", self)

    @property
    def XHTML_Object317(self):
        return self.__XHTML_Object317

    @XHTML_Object317.setter
    def XHTML_Object317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Object__XHTML_Object317", None)
        self.__XHTML_Object317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI318"):
                opp_val = getattr(old_value, "URI318", None)
                if opp_val == self:
                    setattr(old_value, "URI318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI318"):
                opp_val = getattr(value, "URI318", None)
                setattr(value, "URI318", self)

class XHTML_Img(Special, Attrs, EMPTY):

    def __init__(self, ismap: str, XHTML_Img: "URI" = None, XHTML_Img359: "Text" = None, XHTML_Img362: "URI" = None, XHTML_Img365: "Length" = None, XHTML_Img368: "Length" = None, XHTML_Img371: "URI" = None):
        self.ismap = ismap
        self.XHTML_Img = XHTML_Img
        self.XHTML_Img359 = XHTML_Img359
        self.XHTML_Img362 = XHTML_Img362
        self.XHTML_Img365 = XHTML_Img365
        self.XHTML_Img368 = XHTML_Img368
        self.XHTML_Img371 = XHTML_Img371
        
        pass
    @property
    def ismap(self):
        return self.__ismap

    @ismap.setter
    def ismap(self, ismap: str):
        self.__ismap = ismap


    @property
    def XHTML_Img362(self):
        return self.__XHTML_Img362

    @XHTML_Img362.setter
    def XHTML_Img362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Img__XHTML_Img362", None)
        self.__XHTML_Img362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI363"):
                opp_val = getattr(old_value, "URI363", None)
                if opp_val == self:
                    setattr(old_value, "URI363", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI363"):
                opp_val = getattr(value, "URI363", None)
                setattr(value, "URI363", self)

    @property
    def XHTML_Img368(self):
        return self.__XHTML_Img368

    @XHTML_Img368.setter
    def XHTML_Img368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Img__XHTML_Img368", None)
        self.__XHTML_Img368 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Length369"):
                opp_val = getattr(old_value, "Length369", None)
                if opp_val == self:
                    setattr(old_value, "Length369", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Length369"):
                opp_val = getattr(value, "Length369", None)
                setattr(value, "Length369", self)

    @property
    def XHTML_Img359(self):
        return self.__XHTML_Img359

    @XHTML_Img359.setter
    def XHTML_Img359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Img__XHTML_Img359", None)
        self.__XHTML_Img359 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Text360"):
                opp_val = getattr(old_value, "Text360", None)
                if opp_val == self:
                    setattr(old_value, "Text360", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Text360"):
                opp_val = getattr(value, "Text360", None)
                setattr(value, "Text360", self)

    @property
    def XHTML_Img365(self):
        return self.__XHTML_Img365

    @XHTML_Img365.setter
    def XHTML_Img365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Img__XHTML_Img365", None)
        self.__XHTML_Img365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Length366"):
                opp_val = getattr(old_value, "Length366", None)
                if opp_val == self:
                    setattr(old_value, "Length366", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Length366"):
                opp_val = getattr(value, "Length366", None)
                setattr(value, "Length366", self)

    @property
    def XHTML_Img(self):
        return self.__XHTML_Img

    @XHTML_Img.setter
    def XHTML_Img(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Img__XHTML_Img", None)
        self.__XHTML_Img = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI357"):
                opp_val = getattr(old_value, "URI357", None)
                if opp_val == self:
                    setattr(old_value, "URI357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI357"):
                opp_val = getattr(value, "URI357", None)
                setattr(value, "URI357", self)

    @property
    def XHTML_Img371(self):
        return self.__XHTML_Img371

    @XHTML_Img371.setter
    def XHTML_Img371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Img__XHTML_Img371", None)
        self.__XHTML_Img371 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI372"):
                opp_val = getattr(old_value, "URI372", None)
                if opp_val == self:
                    setattr(old_value, "URI372", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI372"):
                opp_val = getattr(value, "URI372", None)
                setattr(value, "URI372", self)

class XHTML_Specialpre(Special, PreContent):

    pass
class Number:

    pass
class Character:

    pass
class XHTML_Focus(ABC):

    pass
class block:

    pass
class XHTML_P(Attrs, block, ButtonContent):

    pass
class XHTML_Lists(block, ButtonContent):

    pass
class XHTML_Table(Attrs, block, ButtonContent):

    def __init__(self, frame: str, rules: str, XHTML_Table: set["Caption"] = None, XHTML_Table522: "ColElement" = None, XHTML_Table524: "Thead" = None, XHTML_Table526: "Tfoot" = None, XHTML_Table528: "TableElement" = None, XHTML_Table530: "Text" = None, XHTML_Table538: "Length" = None, XHTML_Table541: "Length" = None, XHTML_Table533: "Length" = None, XHTML_Table536: "Pixels" = None, ButtonContent: "XHTML_Button" = None):
        self.frame = frame
        self.rules = rules
        self.XHTML_Table = XHTML_Table if XHTML_Table is not None else set()
        self.XHTML_Table522 = XHTML_Table522
        self.XHTML_Table524 = XHTML_Table524
        self.XHTML_Table526 = XHTML_Table526
        self.XHTML_Table528 = XHTML_Table528
        self.XHTML_Table530 = XHTML_Table530
        self.XHTML_Table538 = XHTML_Table538
        self.XHTML_Table541 = XHTML_Table541
        self.XHTML_Table533 = XHTML_Table533
        self.XHTML_Table536 = XHTML_Table536
        
        pass
    @property
    def rules(self):
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules


    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, frame: str):
        self.__frame = frame


    @property
    def XHTML_Table536(self):
        return self.__XHTML_Table536

    @XHTML_Table536.setter
    def XHTML_Table536(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Table__XHTML_Table536", None)
        self.__XHTML_Table536 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pixels"):
                opp_val = getattr(old_value, "Pixels", None)
                if opp_val == self:
                    setattr(old_value, "Pixels", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pixels"):
                opp_val = getattr(value, "Pixels", None)
                setattr(value, "Pixels", self)

    @property
    def XHTML_Table526(self):
        return self.__XHTML_Table526

    @XHTML_Table526.setter
    def XHTML_Table526(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Table__XHTML_Table526", None)
        self.__XHTML_Table526 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tfoot"):
                opp_val = getattr(old_value, "Tfoot", None)
                if opp_val == self:
                    setattr(old_value, "Tfoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tfoot"):
                opp_val = getattr(value, "Tfoot", None)
                setattr(value, "Tfoot", self)

    @property
    def XHTML_Table533(self):
        return self.__XHTML_Table533

    @XHTML_Table533.setter
    def XHTML_Table533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Table__XHTML_Table533", None)
        self.__XHTML_Table533 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Length534"):
                opp_val = getattr(old_value, "Length534", None)
                if opp_val == self:
                    setattr(old_value, "Length534", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Length534"):
                opp_val = getattr(value, "Length534", None)
                setattr(value, "Length534", self)

    @property
    def XHTML_Table524(self):
        return self.__XHTML_Table524

    @XHTML_Table524.setter
    def XHTML_Table524(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Table__XHTML_Table524", None)
        self.__XHTML_Table524 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Thead"):
                opp_val = getattr(old_value, "Thead", None)
                if opp_val == self:
                    setattr(old_value, "Thead", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Thead"):
                opp_val = getattr(value, "Thead", None)
                setattr(value, "Thead", self)

    @property
    def XHTML_Table(self):
        return self.__XHTML_Table

    @XHTML_Table.setter
    def XHTML_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Table__XHTML_Table", None)
        self.__XHTML_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Caption"):
                    opp_val = getattr(item, "Caption", None)
                    
                    if opp_val == self:
                        setattr(item, "Caption", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Caption"):
                    opp_val = getattr(item, "Caption", None)
                    
                    setattr(item, "Caption", self)
                    

    @property
    def XHTML_Table522(self):
        return self.__XHTML_Table522

    @XHTML_Table522.setter
    def XHTML_Table522(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Table__XHTML_Table522", None)
        self.__XHTML_Table522 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColElement"):
                opp_val = getattr(old_value, "ColElement", None)
                if opp_val == self:
                    setattr(old_value, "ColElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColElement"):
                opp_val = getattr(value, "ColElement", None)
                setattr(value, "ColElement", self)

    @property
    def XHTML_Table528(self):
        return self.__XHTML_Table528

    @XHTML_Table528.setter
    def XHTML_Table528(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Table__XHTML_Table528", None)
        self.__XHTML_Table528 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableElement"):
                opp_val = getattr(old_value, "TableElement", None)
                if opp_val == self:
                    setattr(old_value, "TableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableElement"):
                opp_val = getattr(value, "TableElement", None)
                setattr(value, "TableElement", self)

    @property
    def XHTML_Table538(self):
        return self.__XHTML_Table538

    @XHTML_Table538.setter
    def XHTML_Table538(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Table__XHTML_Table538", None)
        self.__XHTML_Table538 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Length539"):
                opp_val = getattr(old_value, "Length539", None)
                if opp_val == self:
                    setattr(old_value, "Length539", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Length539"):
                opp_val = getattr(value, "Length539", None)
                setattr(value, "Length539", self)

    @property
    def XHTML_Table530(self):
        return self.__XHTML_Table530

    @XHTML_Table530.setter
    def XHTML_Table530(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Table__XHTML_Table530", None)
        self.__XHTML_Table530 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Text531"):
                opp_val = getattr(old_value, "Text531", None)
                if opp_val == self:
                    setattr(old_value, "Text531", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Text531"):
                opp_val = getattr(value, "Text531", None)
                setattr(value, "Text531", self)

    @property
    def XHTML_Table541(self):
        return self.__XHTML_Table541

    @XHTML_Table541.setter
    def XHTML_Table541(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Table__XHTML_Table541", None)
        self.__XHTML_Table541 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Length542"):
                opp_val = getattr(old_value, "Length542", None)
                if opp_val == self:
                    setattr(old_value, "Length542", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Length542"):
                opp_val = getattr(value, "Length542", None)
                setattr(value, "Length542", self)

class XHTML_Div(Attrs, block, ButtonContent):

    pass
class XHTML_Fieldset(Attrs, block):

    pass
class XHTML_Blocktext(block, ButtonContent):

    pass
class XHTML_Heading(block, ButtonContent):

    pass
class PCDATA:

    pass
class XHTML_Option(SelectElement, PCDATA, Attrs):

    def __init__(self, selected: str, disabled: str, XHTML_Option: "Text" = None, XHTML_Option484: "CDATA" = None, PCDATA55: "XHTML_Flow" = None, PCDATA: "XHTML_Inline" = None, PCDATA308: "XHTML_ObjectElement" = None, PCDATA61: "XHTML_ButtonContent" = None, PCDATA57: "XHTML_AContent" = None, PCDATA59: "XHTML_PreContent" = None, PCDATA501: "XHTML_FieldsetElement" = None, SelectElement: "XHTML_Select" = None):
        self.selected = selected
        self.disabled = disabled
        self.XHTML_Option = XHTML_Option
        self.XHTML_Option484 = XHTML_Option484
        
        pass
    @property
    def disabled(self):
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: str):
        self.__disabled = disabled


    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected


    @property
    def XHTML_Option484(self):
        return self.__XHTML_Option484

    @XHTML_Option484.setter
    def XHTML_Option484(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Option__XHTML_Option484", None)
        self.__XHTML_Option484 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA485"):
                opp_val = getattr(old_value, "CDATA485", None)
                if opp_val == self:
                    setattr(old_value, "CDATA485", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA485"):
                opp_val = getattr(value, "CDATA485", None)
                setattr(value, "CDATA485", self)

    @property
    def XHTML_Option(self):
        return self.__XHTML_Option

    @XHTML_Option.setter
    def XHTML_Option(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Option__XHTML_Option", None)
        self.__XHTML_Option = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Text482"):
                opp_val = getattr(old_value, "Text482", None)
                if opp_val == self:
                    setattr(old_value, "Text482", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Text482"):
                opp_val = getattr(value, "Text482", None)
                setattr(value, "Text482", self)

class XHTML_Script(HeadMisc, PCDATA, Miscinline):

    def __init__(self, defer: str, xml_space: str, XHTML_Script175: "URI" = None, XHTML_Script: "ID" = None, XHTML_Script169: "Charset" = None, XHTML_Script172: "ContentType" = None, PCDATA55: "XHTML_Flow" = None, PCDATA: "XHTML_Inline" = None, PCDATA308: "XHTML_ObjectElement" = None, PCDATA61: "XHTML_ButtonContent" = None, PCDATA57: "XHTML_AContent" = None, PCDATA59: "XHTML_PreContent" = None, PCDATA501: "XHTML_FieldsetElement" = None, HeadMisc99: "XHTML_BaseHeadElement" = None, HeadMisc: "XHTML_Head" = None, HeadMisc106: "XHTML_TitleBaseHeadElement" = None, HeadMisc94: "XHTML_BaseTitleHeadElement" = None, HeadMisc88: "XHTML_TitleHeadElement" = None):
        self.defer = defer
        self.xml_space = xml_space
        self.XHTML_Script175 = XHTML_Script175
        self.XHTML_Script = XHTML_Script
        self.XHTML_Script169 = XHTML_Script169
        self.XHTML_Script172 = XHTML_Script172
        
        pass
    @property
    def defer(self):
        return self.__defer

    @defer.setter
    def defer(self, defer: str):
        self.__defer = defer


    @property
    def xml_space(self):
        return self.__xml_space

    @xml_space.setter
    def xml_space(self, xml_space: str):
        self.__xml_space = xml_space


    @property
    def XHTML_Script175(self):
        return self.__XHTML_Script175

    @XHTML_Script175.setter
    def XHTML_Script175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Script__XHTML_Script175", None)
        self.__XHTML_Script175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI176"):
                opp_val = getattr(old_value, "URI176", None)
                if opp_val == self:
                    setattr(old_value, "URI176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI176"):
                opp_val = getattr(value, "URI176", None)
                setattr(value, "URI176", self)

    @property
    def XHTML_Script(self):
        return self.__XHTML_Script

    @XHTML_Script.setter
    def XHTML_Script(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Script__XHTML_Script", None)
        self.__XHTML_Script = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ID167"):
                opp_val = getattr(old_value, "ID167", None)
                if opp_val == self:
                    setattr(old_value, "ID167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ID167"):
                opp_val = getattr(value, "ID167", None)
                setattr(value, "ID167", self)

    @property
    def XHTML_Script172(self):
        return self.__XHTML_Script172

    @XHTML_Script172.setter
    def XHTML_Script172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Script__XHTML_Script172", None)
        self.__XHTML_Script172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContentType173"):
                opp_val = getattr(old_value, "ContentType173", None)
                if opp_val == self:
                    setattr(old_value, "ContentType173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContentType173"):
                opp_val = getattr(value, "ContentType173", None)
                setattr(value, "ContentType173", self)

    @property
    def XHTML_Script169(self):
        return self.__XHTML_Script169

    @XHTML_Script169.setter
    def XHTML_Script169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Script__XHTML_Script169", None)
        self.__XHTML_Script169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Charset170"):
                opp_val = getattr(old_value, "Charset170", None)
                if opp_val == self:
                    setattr(old_value, "Charset170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Charset170"):
                opp_val = getattr(value, "Charset170", None)
                setattr(value, "Charset170", self)

class XHTML_Textarea(Focus, Attrs, PCDATA, Inlineforms):

    def __init__(self, disabled: str, readonly: str, XHTML_Textarea: "CDATA" = None, XHTML_Textarea489: "Number" = None, XHTML_Textarea492: "Number" = None, XHTML_Textarea495: "ScriptExpression" = None, XHTML_Textarea498: "ScriptExpression" = None, PCDATA55: "XHTML_Flow" = None, PCDATA: "XHTML_Inline" = None, PCDATA308: "XHTML_ObjectElement" = None, PCDATA61: "XHTML_ButtonContent" = None, PCDATA57: "XHTML_AContent" = None, PCDATA59: "XHTML_PreContent" = None, PCDATA501: "XHTML_FieldsetElement" = None):
        self.disabled = disabled
        self.readonly = readonly
        self.XHTML_Textarea = XHTML_Textarea
        self.XHTML_Textarea489 = XHTML_Textarea489
        self.XHTML_Textarea492 = XHTML_Textarea492
        self.XHTML_Textarea495 = XHTML_Textarea495
        self.XHTML_Textarea498 = XHTML_Textarea498
        
        pass
    @property
    def readonly(self):
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: str):
        self.__readonly = readonly


    @property
    def disabled(self):
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: str):
        self.__disabled = disabled


    @property
    def XHTML_Textarea489(self):
        return self.__XHTML_Textarea489

    @XHTML_Textarea489.setter
    def XHTML_Textarea489(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Textarea__XHTML_Textarea489", None)
        self.__XHTML_Textarea489 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Number490"):
                opp_val = getattr(old_value, "Number490", None)
                if opp_val == self:
                    setattr(old_value, "Number490", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Number490"):
                opp_val = getattr(value, "Number490", None)
                setattr(value, "Number490", self)

    @property
    def XHTML_Textarea492(self):
        return self.__XHTML_Textarea492

    @XHTML_Textarea492.setter
    def XHTML_Textarea492(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Textarea__XHTML_Textarea492", None)
        self.__XHTML_Textarea492 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Number493"):
                opp_val = getattr(old_value, "Number493", None)
                if opp_val == self:
                    setattr(old_value, "Number493", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Number493"):
                opp_val = getattr(value, "Number493", None)
                setattr(value, "Number493", self)

    @property
    def XHTML_Textarea498(self):
        return self.__XHTML_Textarea498

    @XHTML_Textarea498.setter
    def XHTML_Textarea498(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Textarea__XHTML_Textarea498", None)
        self.__XHTML_Textarea498 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScriptExpression499"):
                opp_val = getattr(old_value, "ScriptExpression499", None)
                if opp_val == self:
                    setattr(old_value, "ScriptExpression499", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScriptExpression499"):
                opp_val = getattr(value, "ScriptExpression499", None)
                setattr(value, "ScriptExpression499", self)

    @property
    def XHTML_Textarea(self):
        return self.__XHTML_Textarea

    @XHTML_Textarea.setter
    def XHTML_Textarea(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Textarea__XHTML_Textarea", None)
        self.__XHTML_Textarea = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA487"):
                opp_val = getattr(old_value, "CDATA487", None)
                if opp_val == self:
                    setattr(old_value, "CDATA487", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA487"):
                opp_val = getattr(value, "CDATA487", None)
                setattr(value, "CDATA487", self)

    @property
    def XHTML_Textarea495(self):
        return self.__XHTML_Textarea495

    @XHTML_Textarea495.setter
    def XHTML_Textarea495(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Textarea__XHTML_Textarea495", None)
        self.__XHTML_Textarea495 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScriptExpression496"):
                opp_val = getattr(old_value, "ScriptExpression496", None)
                if opp_val == self:
                    setattr(old_value, "ScriptExpression496", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScriptExpression496"):
                opp_val = getattr(value, "ScriptExpression496", None)
                setattr(value, "ScriptExpression496", self)

class XHTML_Style(PCDATA, HeadMisc):

    def __init__(self, xml_space: str, XHTML_Style: "I18n" = None, XHTML_Style155: "ID" = None, XHTML_Style158: "ContentType" = None, XHTML_Style161: "MediaDesc" = None, XHTML_Style164: "Text" = None, PCDATA55: "XHTML_Flow" = None, PCDATA: "XHTML_Inline" = None, PCDATA308: "XHTML_ObjectElement" = None, PCDATA61: "XHTML_ButtonContent" = None, PCDATA57: "XHTML_AContent" = None, PCDATA59: "XHTML_PreContent" = None, PCDATA501: "XHTML_FieldsetElement" = None, HeadMisc99: "XHTML_BaseHeadElement" = None, HeadMisc: "XHTML_Head" = None, HeadMisc106: "XHTML_TitleBaseHeadElement" = None, HeadMisc94: "XHTML_BaseTitleHeadElement" = None, HeadMisc88: "XHTML_TitleHeadElement" = None):
        self.xml_space = xml_space
        self.XHTML_Style = XHTML_Style
        self.XHTML_Style155 = XHTML_Style155
        self.XHTML_Style158 = XHTML_Style158
        self.XHTML_Style161 = XHTML_Style161
        self.XHTML_Style164 = XHTML_Style164
        
        pass
    @property
    def xml_space(self):
        return self.__xml_space

    @xml_space.setter
    def xml_space(self, xml_space: str):
        self.__xml_space = xml_space


    @property
    def XHTML_Style158(self):
        return self.__XHTML_Style158

    @XHTML_Style158.setter
    def XHTML_Style158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Style__XHTML_Style158", None)
        self.__XHTML_Style158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContentType159"):
                opp_val = getattr(old_value, "ContentType159", None)
                if opp_val == self:
                    setattr(old_value, "ContentType159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContentType159"):
                opp_val = getattr(value, "ContentType159", None)
                setattr(value, "ContentType159", self)

    @property
    def XHTML_Style155(self):
        return self.__XHTML_Style155

    @XHTML_Style155.setter
    def XHTML_Style155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Style__XHTML_Style155", None)
        self.__XHTML_Style155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ID156"):
                opp_val = getattr(old_value, "ID156", None)
                if opp_val == self:
                    setattr(old_value, "ID156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ID156"):
                opp_val = getattr(value, "ID156", None)
                setattr(value, "ID156", self)

    @property
    def XHTML_Style164(self):
        return self.__XHTML_Style164

    @XHTML_Style164.setter
    def XHTML_Style164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Style__XHTML_Style164", None)
        self.__XHTML_Style164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Text165"):
                opp_val = getattr(old_value, "Text165", None)
                if opp_val == self:
                    setattr(old_value, "Text165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Text165"):
                opp_val = getattr(value, "Text165", None)
                setattr(value, "Text165", self)

    @property
    def XHTML_Style(self):
        return self.__XHTML_Style

    @XHTML_Style.setter
    def XHTML_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Style__XHTML_Style", None)
        self.__XHTML_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "I18n153"):
                opp_val = getattr(old_value, "I18n153", None)
                if opp_val == self:
                    setattr(old_value, "I18n153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "I18n153"):
                opp_val = getattr(value, "I18n153", None)
                setattr(value, "I18n153", self)

    @property
    def XHTML_Style161(self):
        return self.__XHTML_Style161

    @XHTML_Style161.setter
    def XHTML_Style161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Style__XHTML_Style161", None)
        self.__XHTML_Style161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MediaDesc162"):
                opp_val = getattr(old_value, "MediaDesc162", None)
                if opp_val == self:
                    setattr(old_value, "MediaDesc162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MediaDesc162"):
                opp_val = getattr(value, "MediaDesc162", None)
                setattr(value, "MediaDesc162", self)

class XHTML_Title(PCDATA):

    pass
class FieldsetElement:

    pass
class XHTML_Legend(FieldsetElement, Attrs):

    pass
class MapElementContent:

    pass
class ObjectElement:

    pass
class XHTML_Param(ObjectElement, EMPTY):

    def __init__(self, valuetype: str, XHTML_Param: "ID" = None, XHTML_Param348: "CDATA" = None, XHTML_Param351: "CDATA" = None, XHTML_Param354: "ContentType" = None, ObjectElement: "XHTML_Object" = None):
        self.valuetype = valuetype
        self.XHTML_Param = XHTML_Param
        self.XHTML_Param348 = XHTML_Param348
        self.XHTML_Param351 = XHTML_Param351
        self.XHTML_Param354 = XHTML_Param354
        
        pass
    @property
    def valuetype(self):
        return self.__valuetype

    @valuetype.setter
    def valuetype(self, valuetype: str):
        self.__valuetype = valuetype


    @property
    def XHTML_Param351(self):
        return self.__XHTML_Param351

    @XHTML_Param351.setter
    def XHTML_Param351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Param__XHTML_Param351", None)
        self.__XHTML_Param351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA352"):
                opp_val = getattr(old_value, "CDATA352", None)
                if opp_val == self:
                    setattr(old_value, "CDATA352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA352"):
                opp_val = getattr(value, "CDATA352", None)
                setattr(value, "CDATA352", self)

    @property
    def XHTML_Param354(self):
        return self.__XHTML_Param354

    @XHTML_Param354.setter
    def XHTML_Param354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Param__XHTML_Param354", None)
        self.__XHTML_Param354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContentType355"):
                opp_val = getattr(old_value, "ContentType355", None)
                if opp_val == self:
                    setattr(old_value, "ContentType355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContentType355"):
                opp_val = getattr(value, "ContentType355", None)
                setattr(value, "ContentType355", self)

    @property
    def XHTML_Param(self):
        return self.__XHTML_Param

    @XHTML_Param.setter
    def XHTML_Param(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Param__XHTML_Param", None)
        self.__XHTML_Param = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ID346"):
                opp_val = getattr(old_value, "ID346", None)
                if opp_val == self:
                    setattr(old_value, "ID346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ID346"):
                opp_val = getattr(value, "ID346", None)
                setattr(value, "ID346", self)

    @property
    def XHTML_Param348(self):
        return self.__XHTML_Param348

    @XHTML_Param348.setter
    def XHTML_Param348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Param__XHTML_Param348", None)
        self.__XHTML_Param348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDATA349"):
                opp_val = getattr(old_value, "CDATA349", None)
                if opp_val == self:
                    setattr(old_value, "CDATA349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDATA349"):
                opp_val = getattr(value, "CDATA349", None)
                setattr(value, "CDATA349", self)

class FormContent:

    pass
class Flow:

    pass
class XHTML_Inline(FieldsetElement, ObjectElement, Flow):

    pass
class Block:

    pass
class XHTML_Form(FieldsetElement, ObjectElement, MapElementContent, Attrs, Block):

    def __init__(self, method: str, XHTML_Form400: "URI" = None, XHTML_Form403: "ContentType" = None, XHTML_Form406: "ScriptExpression" = None, XHTML_Form409: "ScriptExpression" = None, XHTML_Form412: "ContentTypes" = None, XHTML_Form414: "Charsets" = None, XHTML_Form: set["FormContent"] = None, Block: "XHTML_Noscript" = None, Block216: "XHTML_Blockquote" = None, Block179: "XHTML_Body" = None, ObjectElement: "XHTML_Object" = None, FieldsetElement: "XHTML_Fieldset" = None):
        self.method = method
        self.XHTML_Form400 = XHTML_Form400
        self.XHTML_Form403 = XHTML_Form403
        self.XHTML_Form406 = XHTML_Form406
        self.XHTML_Form409 = XHTML_Form409
        self.XHTML_Form412 = XHTML_Form412
        self.XHTML_Form414 = XHTML_Form414
        self.XHTML_Form = XHTML_Form if XHTML_Form is not None else set()
        
        pass
    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method


    @property
    def XHTML_Form403(self):
        return self.__XHTML_Form403

    @XHTML_Form403.setter
    def XHTML_Form403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Form__XHTML_Form403", None)
        self.__XHTML_Form403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContentType404"):
                opp_val = getattr(old_value, "ContentType404", None)
                if opp_val == self:
                    setattr(old_value, "ContentType404", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContentType404"):
                opp_val = getattr(value, "ContentType404", None)
                setattr(value, "ContentType404", self)

    @property
    def XHTML_Form412(self):
        return self.__XHTML_Form412

    @XHTML_Form412.setter
    def XHTML_Form412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Form__XHTML_Form412", None)
        self.__XHTML_Form412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContentTypes"):
                opp_val = getattr(old_value, "ContentTypes", None)
                if opp_val == self:
                    setattr(old_value, "ContentTypes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContentTypes"):
                opp_val = getattr(value, "ContentTypes", None)
                setattr(value, "ContentTypes", self)

    @property
    def XHTML_Form414(self):
        return self.__XHTML_Form414

    @XHTML_Form414.setter
    def XHTML_Form414(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Form__XHTML_Form414", None)
        self.__XHTML_Form414 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Charsets"):
                opp_val = getattr(old_value, "Charsets", None)
                if opp_val == self:
                    setattr(old_value, "Charsets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Charsets"):
                opp_val = getattr(value, "Charsets", None)
                setattr(value, "Charsets", self)

    @property
    def XHTML_Form406(self):
        return self.__XHTML_Form406

    @XHTML_Form406.setter
    def XHTML_Form406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Form__XHTML_Form406", None)
        self.__XHTML_Form406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScriptExpression407"):
                opp_val = getattr(old_value, "ScriptExpression407", None)
                if opp_val == self:
                    setattr(old_value, "ScriptExpression407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScriptExpression407"):
                opp_val = getattr(value, "ScriptExpression407", None)
                setattr(value, "ScriptExpression407", self)

    @property
    def XHTML_Form(self):
        return self.__XHTML_Form

    @XHTML_Form.setter
    def XHTML_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Form__XHTML_Form", None)
        self.__XHTML_Form = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FormContent"):
                    opp_val = getattr(item, "FormContent", None)
                    
                    if opp_val == self:
                        setattr(item, "FormContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FormContent"):
                    opp_val = getattr(item, "FormContent", None)
                    
                    setattr(item, "FormContent", self)
                    

    @property
    def XHTML_Form409(self):
        return self.__XHTML_Form409

    @XHTML_Form409.setter
    def XHTML_Form409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Form__XHTML_Form409", None)
        self.__XHTML_Form409 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScriptExpression410"):
                opp_val = getattr(old_value, "ScriptExpression410", None)
                if opp_val == self:
                    setattr(old_value, "ScriptExpression410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScriptExpression410"):
                opp_val = getattr(value, "ScriptExpression410", None)
                setattr(value, "ScriptExpression410", self)

    @property
    def XHTML_Form400(self):
        return self.__XHTML_Form400

    @XHTML_Form400.setter
    def XHTML_Form400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Form__XHTML_Form400", None)
        self.__XHTML_Form400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI401"):
                opp_val = getattr(old_value, "URI401", None)
                if opp_val == self:
                    setattr(old_value, "URI401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI401"):
                opp_val = getattr(value, "URI401", None)
                setattr(value, "URI401", self)

class XHTML_block(FieldsetElement, FormContent, MapElementContent, ObjectElement, Flow, Block):

    pass
class XHTML_Misc(ButtonContent, FieldsetElement, FormContent, MapElementContent, ObjectElement, Flow, Block):

    pass
class Inline:

    pass
class XHTML_inline(Inline):

    pass
class Misc:

    pass
class XHTML_Noscript(Misc, Attrs):

    pass
class XHTML_Miscinline(Misc, Inline, PreContent, AContent):

    pass
class XHTML_Inlineforms(PreContent, AContent, inline):

    pass
class ScriptExpression:

    pass
class XHTML_Events(ABC):

    pass
class LanguageCode:

    pass
class XHTML_I18n(ABC):

    def __init__(self, dir: str, XHTML_I18n: "LanguageCode" = None, XHTML_I18n14: "LanguageCode" = None):
        self.dir = dir
        self.XHTML_I18n = XHTML_I18n
        self.XHTML_I18n14 = XHTML_I18n14
        
        pass
    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def XHTML_I18n(self):
        return self.__XHTML_I18n

    @XHTML_I18n.setter
    def XHTML_I18n(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_I18n__XHTML_I18n", None)
        self.__XHTML_I18n = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LanguageCode"):
                opp_val = getattr(old_value, "LanguageCode", None)
                if opp_val == self:
                    setattr(old_value, "LanguageCode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LanguageCode"):
                opp_val = getattr(value, "LanguageCode", None)
                setattr(value, "LanguageCode", self)

    @property
    def XHTML_I18n14(self):
        return self.__XHTML_I18n14

    @XHTML_I18n14.setter
    def XHTML_I18n14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_I18n__XHTML_I18n14", None)
        self.__XHTML_I18n14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LanguageCode15"):
                opp_val = getattr(old_value, "LanguageCode15", None)
                if opp_val == self:
                    setattr(old_value, "LanguageCode15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LanguageCode15"):
                opp_val = getattr(value, "LanguageCode15", None)
                setattr(value, "LanguageCode15", self)

class Events:

    pass
class I18n:

    pass
class XHTML_Map(Specialpre, I18n, Events):

    pass
class CoreAttrs:

    pass
class XHTML_Bdo(Specialpre, CoreAttrs, Events):

    def __init__(self, dir: str, XHTML_Bdo: set["Inline"] = None, XHTML_Bdo263: "LanguageCode" = None, XHTML_Bdo266: "LanguageCode" = None):
        self.dir = dir
        self.XHTML_Bdo = XHTML_Bdo if XHTML_Bdo is not None else set()
        self.XHTML_Bdo263 = XHTML_Bdo263
        self.XHTML_Bdo266 = XHTML_Bdo266
        
        pass
    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def XHTML_Bdo266(self):
        return self.__XHTML_Bdo266

    @XHTML_Bdo266.setter
    def XHTML_Bdo266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Bdo__XHTML_Bdo266", None)
        self.__XHTML_Bdo266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LanguageCode267"):
                opp_val = getattr(old_value, "LanguageCode267", None)
                if opp_val == self:
                    setattr(old_value, "LanguageCode267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LanguageCode267"):
                opp_val = getattr(value, "LanguageCode267", None)
                setattr(value, "LanguageCode267", self)

    @property
    def XHTML_Bdo263(self):
        return self.__XHTML_Bdo263

    @XHTML_Bdo263.setter
    def XHTML_Bdo263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Bdo__XHTML_Bdo263", None)
        self.__XHTML_Bdo263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LanguageCode264"):
                opp_val = getattr(old_value, "LanguageCode264", None)
                if opp_val == self:
                    setattr(old_value, "LanguageCode264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LanguageCode264"):
                opp_val = getattr(value, "LanguageCode264", None)
                setattr(value, "LanguageCode264", self)

    @property
    def XHTML_Bdo(self):
        return self.__XHTML_Bdo

    @XHTML_Bdo.setter
    def XHTML_Bdo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_XHTML_Bdo__XHTML_Bdo", None)
        self.__XHTML_Bdo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Inline261"):
                    opp_val = getattr(item, "Inline261", None)
                    
                    if opp_val == self:
                        setattr(item, "Inline261", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Inline261"):
                    opp_val = getattr(item, "Inline261", None)
                    
                    setattr(item, "Inline261", self)
                    

class XHTML_Br(Specialpre, CoreAttrs, EMPTY):

    pass
class XHTML_Attrs(CoreAttrs, I18n, Events):

    pass
class URI:

    pass
class Text:

    pass
class StyleSheet:

    pass
class ID:

    pass
class XHTML_CoreAttrs(ABC):

    pass
class Length:

    pass
class XHTML_Coords:

    pass
class ContentType:

    pass
class XHTML_ContentTypes:

    pass
class CDATA:

    pass
class XHTML_Datetime(CDATA):

    pass
class XHTML_Text(CDATA):

    pass
class XHTML_Length(CDATA):

    pass
class XHTML_Pixels(CDATA):

    pass
class XHTML_ScriptExpression(CDATA):

    pass
class XHTML_MultiLength(CDATA):

    pass
class XHTML_StyleSheet(CDATA):

    pass
class XHTML_ContentType(CDATA):

    pass
class XHTML_EMPTY:

    pass
class IDREF:

    pass
class XHTML_IDREFS:

    pass
class XHTML_UriList:

    pass
class XHTML_URI(CDATA):

    pass
class XHTML_MediaDesc(CDATA):

    pass
class XHTML_LinkTypes(CDATA):

    pass
class XHTML_Number(CDATA):

    pass
class XHTML_Character(CDATA):

    pass
class NMTOKEN:

    pass
class XHTML_LanguageCode(NMTOKEN):

    pass
class Charset:

    pass
class XHTML_Charsets:

    pass
class XHTML_Charset(CDATA):

    pass
class ValuedElement:

    pass
class XHTML_ID(ValuedElement):

    pass
class XHTML_IDREF(ValuedElement):

    pass
class XHTML_PCDATA(ValuedElement):

    pass
class XHTML_NMTOKEN(ValuedElement):

    pass
class XHTML_CDATA(ValuedElement):

    pass
class XHTML_ValuedElement(ABC):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

