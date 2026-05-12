from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ListElement:

    pass
class HTML_OL(ListElement):

    def __init__(self, start: str):
        self.start = start
        
        pass
    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start


class HTML_ListElement(ABC):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class HTML_OPTION:

    def __init__(self, selected: str, optionValue: str):
        self.selected = selected
        self.optionValue = optionValue
        
        pass
    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected


    @property
    def optionValue(self):
        return self.__optionValue

    @optionValue.setter
    def optionValue(self, optionValue: str):
        self.__optionValue = optionValue


class HTML_Website:

    pass
class HTML_LI(ListElement):

    def __init__(self, liValue: str):
        self.liValue = liValue
        
        pass
    @property
    def liValue(self):
        return self.__liValue

    @liValue.setter
    def liValue(self, liValue: str):
        self.__liValue = liValue


class HTML_UL(ListElement):

    pass
class HTML_SELECT:

    def __init__(self, multiple: str, size: str, name: str):
        self.multiple = multiple
        self.size = size
        self.name = name
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def multiple(self):
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: str):
        self.__multiple = multiple


class TR:

    pass
class TD:

    pass
class HTML_TH(TD):

    pass
class TABLE:

    pass
class TABLEElement:

    pass
class HTML_TD(TABLEElement):

    def __init__(self, colspan: str, rowspan: str, valign: str, align: str, width: str, tds: "TR" = None):
        self.colspan = colspan
        self.rowspan = rowspan
        self.valign = valign
        self.align = align
        self.width = width
        self.tds = tds
        
        pass
    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def colspan(self):
        return self.__colspan

    @colspan.setter
    def colspan(self, colspan: str):
        self.__colspan = colspan


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def rowspan(self):
        return self.__rowspan

    @rowspan.setter
    def rowspan(self, rowspan: str):
        self.__rowspan = rowspan


    @property
    def valign(self):
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign


    @property
    def tds(self):
        return self.__tds

    @tds.setter
    def tds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TD__tds", None)
        self.__tds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TR20"):
                opp_val = getattr(old_value, "TR20", None)
                if opp_val == self:
                    setattr(old_value, "TR20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TR20"):
                opp_val = getattr(value, "TR20", None)
                setattr(value, "TR20", self)

class HTML_TR(TABLEElement):

    def __init__(self, valign: str, align: str, trs: "TABLE" = None, tr: set["TD"] = None):
        self.valign = valign
        self.align = align
        self.trs = trs
        self.tr = tr if tr is not None else set()
        
        pass
    @property
    def valign(self):
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def tr(self):
        return self.__tr

    @tr.setter
    def tr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TR__tr", None)
        self.__tr = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TD"):
                    opp_val = getattr(item, "TD", None)
                    
                    if opp_val == self:
                        setattr(item, "TD", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TD"):
                    opp_val = getattr(item, "TD", None)
                    
                    setattr(item, "TD", self)
                    

    @property
    def trs(self):
        return self.__trs

    @trs.setter
    def trs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TR__trs", None)
        self.__trs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TABLE"):
                opp_val = getattr(old_value, "TABLE", None)
                if opp_val == self:
                    setattr(old_value, "TABLE", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TABLE"):
                opp_val = getattr(value, "TABLE", None)
                setattr(value, "TABLE", self)

class HTML_TABLE(TABLEElement):

    def __init__(self, border: str, width: str, cellspacing: str, cellpadding: str, table: set["TR"] = None):
        self.border = border
        self.width = width
        self.cellspacing = cellspacing
        self.cellpadding = cellpadding
        self.table = table if table is not None else set()
        
        pass
    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def cellspacing(self):
        return self.__cellspacing

    @cellspacing.setter
    def cellspacing(self, cellspacing: str):
        self.__cellspacing = cellspacing


    @property
    def cellpadding(self):
        return self.__cellpadding

    @cellpadding.setter
    def cellpadding(self, cellpadding: str):
        self.__cellpadding = cellpadding


    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TABLE__table", None)
        self.__table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TR"):
                    opp_val = getattr(item, "TR", None)
                    
                    if opp_val == self:
                        setattr(item, "TR", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TR"):
                    opp_val = getattr(item, "TR", None)
                    
                    setattr(item, "TR", self)
                    

class BODYElement:

    pass
class HTML_EM(BODYElement):

    pass
class HTML_H6(BODYElement):

    pass
class HTML_DIV(BODYElement):

    def __init__(self, align: str, BODYElement: "HTML_BBODY" = None):
        self.align = align
        
        pass
    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


class HTML_TABLEElement(BODYElement):

    def __init__(self, bgcolor: str, background: str, BODYElement: "HTML_BBODY" = None):
        self.bgcolor = bgcolor
        self.background = background
        
        pass
    @property
    def bgcolor(self):
        return self.__bgcolor

    @bgcolor.setter
    def bgcolor(self, bgcolor: str):
        self.__bgcolor = bgcolor


    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background


class HTML_STYLE(BODYElement):

    pass
class HTML_P(BODYElement):

    pass
class HTML_IMG(BODYElement):

    def __init__(self, border: str, src: str, width: str, height: str, alt: str, align: str, vspace: str, hspace: str, ismap: str, usemap: str, BODYElement: "HTML_BBODY" = None):
        self.border = border
        self.src = src
        self.width = width
        self.height = height
        self.alt = alt
        self.align = align
        self.vspace = vspace
        self.hspace = hspace
        self.ismap = ismap
        self.usemap = usemap
        
        pass
    @property
    def usemap(self):
        return self.__usemap

    @usemap.setter
    def usemap(self, usemap: str):
        self.__usemap = usemap


    @property
    def hspace(self):
        return self.__hspace

    @hspace.setter
    def hspace(self, hspace: str):
        self.__hspace = hspace


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border


    @property
    def ismap(self):
        return self.__ismap

    @ismap.setter
    def ismap(self, ismap: str):
        self.__ismap = ismap


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def vspace(self):
        return self.__vspace

    @vspace.setter
    def vspace(self, vspace: str):
        self.__vspace = vspace


    @property
    def alt(self):
        return self.__alt

    @alt.setter
    def alt(self, alt: str):
        self.__alt = alt


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


class HTML_BR(BODYElement):

    def __init__(self, clear: str, BODYElement: "HTML_BBODY" = None):
        self.clear = clear
        
        pass
    @property
    def clear(self):
        return self.__clear

    @clear.setter
    def clear(self, clear: str):
        self.__clear = clear


class HTML_H3(BODYElement):

    pass
class HTML_H1(BODYElement):

    pass
class HTML_H5(BODYElement):

    pass
class HTML_SPAN(BODYElement):

    def __init__(self, style: str, BODYElement: "HTML_BBODY" = None):
        self.style = style
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


class HTML_A(BODYElement):

    def __init__(self, ahref: str, name: str, id: str, BODYElement: "HTML_BBODY" = None):
        self.ahref = ahref
        self.name = name
        self.id = id
        
        pass
    @property
    def ahref(self):
        return self.__ahref

    @ahref.setter
    def ahref(self, ahref: str):
        self.__ahref = ahref


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class HTML_H2(BODYElement):

    pass
class HTML_H4(BODYElement):

    pass
class HTML_STRONG(BODYElement):

    pass
class HTML:

    pass
class HEADElement:

    pass
class HTML_TITLE(HEADElement):

    pass
class HTML_LINK(HEADElement):

    def __init__(self, rel: str, title: str, ahref: str, type: str, HEADElement: "HTML_HEAD" = None):
        self.rel = rel
        self.title = title
        self.ahref = ahref
        self.type = type
        
        pass
    @property
    def rel(self):
        return self.__rel

    @rel.setter
    def rel(self, rel: str):
        self.__rel = rel


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def ahref(self):
        return self.__ahref

    @ahref.setter
    def ahref(self, ahref: str):
        self.__ahref = ahref


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class HTMLElement:

    pass
class HTML_BODYElement(HTMLElement):

    pass
class HTML_HEADElement(HTMLElement):

    pass
class HTML_HEAD(HTMLElement):

    pass
class HTML_BBODY(HTMLElement):

    def __init__(self, alink: str, background: str, bgcolor: str, text: str, link: str, vlink: str, body: set["BODYElement"] = None, bbody: "HTML" = None, HTMLElement: "HTML_HTMLElement" = None, HTMLElement5: "HTML_HTMLElement" = None):
        self.alink = alink
        self.background = background
        self.bgcolor = bgcolor
        self.text = text
        self.link = link
        self.vlink = vlink
        self.body = body if body is not None else set()
        self.bbody = bbody
        
        pass
    @property
    def vlink(self):
        return self.__vlink

    @vlink.setter
    def vlink(self, vlink: str):
        self.__vlink = vlink


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def alink(self):
        return self.__alink

    @alink.setter
    def alink(self, alink: str):
        self.__alink = alink


    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link


    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background


    @property
    def bgcolor(self):
        return self.__bgcolor

    @bgcolor.setter
    def bgcolor(self, bgcolor: str):
        self.__bgcolor = bgcolor


    @property
    def bbody(self):
        return self.__bbody

    @bbody.setter
    def bbody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_BBODY__bbody", None)
        self.__bbody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HTML13"):
                opp_val = getattr(old_value, "HTML13", None)
                if opp_val == self:
                    setattr(old_value, "HTML13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HTML13"):
                opp_val = getattr(value, "HTML13", None)
                setattr(value, "HTML13", self)

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_BBODY__body", None)
        self.__body = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BODYElement"):
                    opp_val = getattr(item, "BODYElement", None)
                    
                    if opp_val == self:
                        setattr(item, "BODYElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BODYElement"):
                    opp_val = getattr(item, "BODYElement", None)
                    
                    setattr(item, "BODYElement", self)
                    

class HTML_HTMLElement:

    def __init__(self, value: str, parent: set["HTMLElement"] = None, children: "HTMLElement" = None):
        self.value = value
        self.parent = parent if parent is not None else set()
        self.children = children
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_HTMLElement__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HTMLElement"):
                    opp_val = getattr(item, "HTMLElement", None)
                    
                    if opp_val == self:
                        setattr(item, "HTMLElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HTMLElement"):
                    opp_val = getattr(item, "HTMLElement", None)
                    
                    setattr(item, "HTMLElement", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_HTMLElement__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HTMLElement5"):
                opp_val = getattr(old_value, "HTMLElement5", None)
                if opp_val == self:
                    setattr(old_value, "HTMLElement5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HTMLElement5"):
                opp_val = getattr(value, "HTMLElement5", None)
                setattr(value, "HTMLElement5", self)

class BBODY:

    pass
class HEAD:

    pass
class HTML_HTML:

    pass