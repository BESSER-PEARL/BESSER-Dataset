from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StyleKey(Enum):
    backgroundColor = "backgroundColor"
    color = "color"
    display = "display"
    lineHeight = "lineHeight"
    textAlign = "textAlign"
    textDecoration = "textDecoration"
    width = "width"
    padding = "padding"


############################################
# Definition of Classes
############################################

class HTMLElement:

    pass
class HTML_SPAN(HTMLElement):

    pass
class HTML_BR(HTMLElement):

    pass
class HTML_TR(HTMLElement):

    def __init__(self, valign: str, align: str, bgcolor: str, height: str, HTML_TR: "HTML_TABLE" = None, HTML_TR8: set["HTML_TD"] = None):
        self.valign = valign
        self.align = align
        self.bgcolor = bgcolor
        self.height = height
        self.HTML_TR = HTML_TR
        self.HTML_TR8 = HTML_TR8 if HTML_TR8 is not None else set()
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def bgcolor(self) -> str:
        return self.__bgcolor

    @bgcolor.setter
    def bgcolor(self, bgcolor: str):
        self.__bgcolor = bgcolor

    @property
    def HTML_TR(self):
        return self.__HTML_TR

    @HTML_TR.setter
    def HTML_TR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TR__HTML_TR", None)
        self.__HTML_TR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HTML_TABLE"):
                opp_val = getattr(old_value, "HTML_TABLE", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HTML_TABLE"):
                opp_val = getattr(value, "HTML_TABLE", None)
                if opp_val is None:
                    setattr(value, "HTML_TABLE", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def HTML_TR8(self):
        return self.__HTML_TR8

    @HTML_TR8.setter
    def HTML_TR8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TR__HTML_TR8", None)
        self.__HTML_TR8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HTML_TD"):
                    opp_val = getattr(item, "HTML_TD", None)
                    
                    if opp_val == self:
                        setattr(item, "HTML_TD", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HTML_TD"):
                    opp_val = getattr(item, "HTML_TD", None)
                    
                    setattr(item, "HTML_TD", self)
                    

class HTML_IMG(HTMLElement):

    def __init__(self, src: str, width: str, height: str, border: str):
        self.src = src
        self.width = width
        self.height = height
        self.border = border
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

class HTML_TD(HTMLElement):

    def __init__(self, colspan: str, rowspan: str, valign: str, align: str, width: str, bgcolor: str, height: str, HTML_TD: "HTML_TR" = None):
        self.colspan = colspan
        self.rowspan = rowspan
        self.valign = valign
        self.align = align
        self.width = width
        self.bgcolor = bgcolor
        self.height = height
        self.HTML_TD = HTML_TD
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def bgcolor(self) -> str:
        return self.__bgcolor

    @bgcolor.setter
    def bgcolor(self, bgcolor: str):
        self.__bgcolor = bgcolor

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def colspan(self) -> str:
        return self.__colspan

    @colspan.setter
    def colspan(self, colspan: str):
        self.__colspan = colspan

    @property
    def rowspan(self) -> str:
        return self.__rowspan

    @rowspan.setter
    def rowspan(self, rowspan: str):
        self.__rowspan = rowspan

    @property
    def HTML_TD(self):
        return self.__HTML_TD

    @HTML_TD.setter
    def HTML_TD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TD__HTML_TD", None)
        self.__HTML_TD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HTML_TR8"):
                opp_val = getattr(old_value, "HTML_TR8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HTML_TR8"):
                opp_val = getattr(value, "HTML_TR8", None)
                if opp_val is None:
                    setattr(value, "HTML_TR8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HTML_FONT(HTMLElement):

    def __init__(self, color: str, face: str, size: str, value: str):
        self.color = color
        self.face = face
        self.size = size
        self.value = value
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def face(self) -> str:
        return self.__face

    @face.setter
    def face(self, face: str):
        self.__face = face

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class HTML_U(HTMLElement):

    pass
class HTML_I(HTMLElement):

    pass
class HTML_DIV(HTMLElement):

    def __init__(self, align: str):
        self.align = align
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

class HTML_HR(HTMLElement):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class HTML_S(HTMLElement):

    pass
class HTML_B(HTMLElement):

    pass
class HTML_TABLE(HTMLElement):

    def __init__(self, border: int, width: str, cellspacing: str, cellpadding: str, align: str, bgcolor: str, HTML_TABLE: set["HTML_TR"] = None):
        self.border = border
        self.width = width
        self.cellspacing = cellspacing
        self.cellpadding = cellpadding
        self.align = align
        self.bgcolor = bgcolor
        self.HTML_TABLE = HTML_TABLE if HTML_TABLE is not None else set()
        
    @property
    def border(self) -> int:
        return self.__border

    @border.setter
    def border(self, border: int):
        self.__border = border

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def bgcolor(self) -> str:
        return self.__bgcolor

    @bgcolor.setter
    def bgcolor(self, bgcolor: str):
        self.__bgcolor = bgcolor

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def cellspacing(self) -> str:
        return self.__cellspacing

    @cellspacing.setter
    def cellspacing(self, cellspacing: str):
        self.__cellspacing = cellspacing

    @property
    def cellpadding(self) -> str:
        return self.__cellpadding

    @cellpadding.setter
    def cellpadding(self, cellpadding: str):
        self.__cellpadding = cellpadding

    @property
    def HTML_TABLE(self):
        return self.__HTML_TABLE

    @HTML_TABLE.setter
    def HTML_TABLE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TABLE__HTML_TABLE", None)
        self.__HTML_TABLE = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HTML_TR"):
                    opp_val = getattr(item, "HTML_TR", None)
                    
                    if opp_val == self:
                        setattr(item, "HTML_TR", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HTML_TR"):
                    opp_val = getattr(item, "HTML_TR", None)
                    
                    setattr(item, "HTML_TR", self)
                    

class HTML_Style:

    def __init__(self, key: str, value: str, HTML_Style: "HTML_HTMLElement" = None):
        self.key = key
        self.value = value
        self.HTML_Style = HTML_Style
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def HTML_Style(self):
        return self.__HTML_Style

    @HTML_Style.setter
    def HTML_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_Style__HTML_Style", None)
        self.__HTML_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HTML_HTMLElement5"):
                opp_val = getattr(old_value, "HTML_HTMLElement5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HTML_HTMLElement5"):
                opp_val = getattr(value, "HTML_HTMLElement5", None)
                if opp_val is None:
                    setattr(value, "HTML_HTMLElement5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HTML_HTMLElement:

    pass
class HTML_A(HTMLElement):

    def __init__(self, ref: str):
        self.ref = ref
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

class HTML_P(HTMLElement):

    def __init__(self, align: str):
        self.align = align
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

class HTML_HTML:

    pass