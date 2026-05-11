from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Html_FORM:

    def __init__(self, action: str, method: str):
        self.action = action
        self.method = method
        
        pass
    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method


class TD:

    pass
class Html_TH(TD):

    pass
class TABLE:

    pass
class Html_OPTION:

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


class Html_SELECT:

    def __init__(self, multiple: str, size: str, name: str):
        self.multiple = multiple
        self.size = size
        self.name = name
        
        pass
    @property
    def multiple(self):
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: str):
        self.__multiple = multiple


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


class Html_TEXTAREA:

    def __init__(self, name: str, rows: str, cols: str):
        self.name = name
        self.rows = rows
        self.cols = cols
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def rows(self):
        return self.__rows

    @rows.setter
    def rows(self, rows: str):
        self.__rows = rows


    @property
    def cols(self):
        return self.__cols

    @cols.setter
    def cols(self, cols: str):
        self.__cols = cols


class TR:

    pass
class TABLEElement:

    pass
class Html_TD(TABLEElement):

    def __init__(self, colspan: str, rowspan: str, valign: str, align: str, width: str, tds: "TR" = None):
        self.colspan = colspan
        self.rowspan = rowspan
        self.valign = valign
        self.align = align
        self.width = width
        self.tds = tds
        
        pass
    @property
    def rowspan(self):
        return self.__rowspan

    @rowspan.setter
    def rowspan(self, rowspan: str):
        self.__rowspan = rowspan


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
        old_value = getattr(self, f"_Html_TD__tds", None)
        self.__tds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TR21"):
                opp_val = getattr(old_value, "TR21", None)
                if opp_val == self:
                    setattr(old_value, "TR21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TR21"):
                opp_val = getattr(value, "TR21", None)
                setattr(value, "TR21", self)

class Html_TR(TABLEElement):

    def __init__(self, valign: str, align: str, trs: "TABLE" = None, tr: set["TD"] = None):
        self.valign = valign
        self.align = align
        self.trs = trs
        self.tr = tr if tr is not None else set()
        
        pass
    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def valign(self):
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign


    @property
    def trs(self):
        return self.__trs

    @trs.setter
    def trs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Html_TR__trs", None)
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

    @property
    def tr(self):
        return self.__tr

    @tr.setter
    def tr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Html_TR__tr", None)
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
                    

class Html_TABLE(TABLEElement):

    def __init__(self, border: str, width: str, cellspacing: str, cellpadding: str, table: set["TR"] = None):
        self.border = border
        self.width = width
        self.cellspacing = cellspacing
        self.cellpadding = cellpadding
        self.table = table if table is not None else set()
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def cellpadding(self):
        return self.__cellpadding

    @cellpadding.setter
    def cellpadding(self, cellpadding: str):
        self.__cellpadding = cellpadding


    @property
    def cellspacing(self):
        return self.__cellspacing

    @cellspacing.setter
    def cellspacing(self, cellspacing: str):
        self.__cellspacing = cellspacing


    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border


    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Html_TABLE__table", None)
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
                    

class HTML:

    pass
class HEADElement:

    pass
class Html_TITLE(HEADElement):

    pass
class Html_LINK(HEADElement):

    def __init__(self, rel: str, ahref: str, type: str, HEADElement: "Html_HEAD" = None):
        self.rel = rel
        self.ahref = ahref
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def rel(self):
        return self.__rel

    @rel.setter
    def rel(self, rel: str):
        self.__rel = rel


    @property
    def ahref(self):
        return self.__ahref

    @ahref.setter
    def ahref(self, ahref: str):
        self.__ahref = ahref


class HTMLElement:

    pass
class Html_BODY(HTMLElement):

    def __init__(self, background: str, bgcolor: str, text: str, link: str, alink: str, vlink: str, body: set["BODYElement"] = None, body13: "HTML" = None, HTMLElement: "Html_HTMLElement" = None, HTMLElement5: "Html_HTMLElement" = None):
        self.background = background
        self.bgcolor = bgcolor
        self.text = text
        self.link = link
        self.alink = alink
        self.vlink = vlink
        self.body = body if body is not None else set()
        self.body13 = body13
        
        pass
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
    def link(self):
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link


    @property
    def alink(self):
        return self.__alink

    @alink.setter
    def alink(self, alink: str):
        self.__alink = alink


    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Html_BODY__body", None)
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
                    

    @property
    def body13(self):
        return self.__body13

    @body13.setter
    def body13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Html_BODY__body13", None)
        self.__body13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HTML14"):
                opp_val = getattr(old_value, "HTML14", None)
                if opp_val == self:
                    setattr(old_value, "HTML14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HTML14"):
                opp_val = getattr(value, "HTML14", None)
                setattr(value, "HTML14", self)

class Html_HEAD(HTMLElement):

    pass
class Html_HEADElement(HTMLElement):

    pass
class Html_HTMLElement:

    def __init__(self, value: str, id: str, class_: str, title: str, parent: set["HTMLElement"] = None, children: "HTMLElement" = None):
        self.value = value
        self.id = id
        self.class_ = class_
        self.title = title
        self.parent = parent if parent is not None else set()
        self.children = children
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_: str):
        self.__class_ = class_


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Html_HTMLElement__children", None)
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

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Html_HTMLElement__parent", None)
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
                    

class BODY:

    pass
class Html_BODYElement(HTMLElement):

    pass
class HEAD:

    pass
class Html_HTML:

    pass
class BODYElement:

    pass
class Html_NOEMBED(BODYElement):

    pass
class Html_IMG(BODYElement):

    def __init__(self, ismap: str, usemap: str, border: str, src: str, width: str, height: str, alt: str, align: str, vspace: str, hspace: str, BODYElement: "Html_BODY" = None):
        self.ismap = ismap
        self.usemap = usemap
        self.border = border
        self.src = src
        self.width = width
        self.height = height
        self.alt = alt
        self.align = align
        self.vspace = vspace
        self.hspace = hspace
        
        pass
    @property
    def hspace(self):
        return self.__hspace

    @hspace.setter
    def hspace(self, hspace: str):
        self.__hspace = hspace


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def ismap(self):
        return self.__ismap

    @ismap.setter
    def ismap(self, ismap: str):
        self.__ismap = ismap


    @property
    def usemap(self):
        return self.__usemap

    @usemap.setter
    def usemap(self, usemap: str):
        self.__usemap = usemap


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border


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
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


class Html_SUP(BODYElement):

    pass
class Html_B(BODYElement):

    pass
class Html_BIG(BODYElement):

    pass
class Html_AREA(BODYElement):

    def __init__(self, shape: str, coords: str, ahref: str, BODYElement: "Html_BODY" = None):
        self.shape = shape
        self.coords = coords
        self.ahref = ahref
        
        pass
    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


    @property
    def ahref(self):
        return self.__ahref

    @ahref.setter
    def ahref(self, ahref: str):
        self.__ahref = ahref


    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, coords: str):
        self.__coords = coords


class Html_EMBED(BODYElement):

    def __init__(self, src: str, width: str, height: str, align: str, vspace: str, hspace: str, border: str, BODYElement: "Html_BODY" = None):
        self.src = src
        self.width = width
        self.height = height
        self.align = align
        self.vspace = vspace
        self.hspace = hspace
        self.border = border
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def vspace(self):
        return self.__vspace

    @vspace.setter
    def vspace(self, vspace: str):
        self.__vspace = vspace


    @property
    def hspace(self):
        return self.__hspace

    @hspace.setter
    def hspace(self, hspace: str):
        self.__hspace = hspace


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border


class Html_SUB(BODYElement):

    pass
class Html_SMALL(BODYElement):

    pass
class Html_STRONG(BODYElement):

    pass
class Html_MAP(BODYElement):

    pass
class Html_H3(BODYElement):

    pass
class Html_STRIKE(BODYElement):

    pass
class Html_H2(BODYElement):

    pass
class Html_P(BODYElement):

    pass
class Html_I(BODYElement):

    pass
class Html_EM(BODYElement):

    pass
class Html_A(BODYElement):

    def __init__(self, ahref: str, name: str, BODYElement: "Html_BODY" = None):
        self.ahref = ahref
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ahref(self):
        return self.__ahref

    @ahref.setter
    def ahref(self, ahref: str):
        self.__ahref = ahref


class Html_H4(BODYElement):

    pass
class Html_SPAN(BODYElement):

    def __init__(self, style: str, BODYElement: "Html_BODY" = None):
        self.style = style
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


class Html_PRE(BODYElement):

    pass
class Html_STYLE(BODYElement):

    pass
class Html_DIV(BODYElement):

    def __init__(self, align: str, BODYElement: "Html_BODY" = None):
        self.align = align
        
        pass
    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


class Html_TT(BODYElement):

    pass
class Html_BR(BODYElement):

    def __init__(self, clear: str, BODYElement: "Html_BODY" = None):
        self.clear = clear
        
        pass
    @property
    def clear(self):
        return self.__clear

    @clear.setter
    def clear(self, clear: str):
        self.__clear = clear


class Html_H1(BODYElement):

    pass
class Html_FONT(BODYElement):

    def __init__(self, color: str, face: str, size: str, BODYElement: "Html_BODY" = None):
        self.color = color
        self.face = face
        self.size = size
        
        pass
    @property
    def face(self):
        return self.__face

    @face.setter
    def face(self, face: str):
        self.__face = face


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


class Html_TABLEElement(BODYElement):

    def __init__(self, bgcolor: str, background: str, BODYElement: "Html_BODY" = None):
        self.bgcolor = bgcolor
        self.background = background
        
        pass
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


class FRAME:

    pass
class Html_IFRAME(FRAME):

    pass
class Html_NOFRAME:

    pass
class Html_FRAME:

    def __init__(self, src: str, name: str, marginwidth: str, marginheight: str, scrolling: str, noresize: str):
        self.src = src
        self.name = name
        self.marginwidth = marginwidth
        self.marginheight = marginheight
        self.scrolling = scrolling
        self.noresize = noresize
        
        pass
    @property
    def scrolling(self):
        return self.__scrolling

    @scrolling.setter
    def scrolling(self, scrolling: str):
        self.__scrolling = scrolling


    @property
    def marginwidth(self):
        return self.__marginwidth

    @marginwidth.setter
    def marginwidth(self, marginwidth: str):
        self.__marginwidth = marginwidth


    @property
    def marginheight(self):
        return self.__marginheight

    @marginheight.setter
    def marginheight(self, marginheight: str):
        self.__marginheight = marginheight


    @property
    def noresize(self):
        return self.__noresize

    @noresize.setter
    def noresize(self, noresize: str):
        self.__noresize = noresize


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Html_PARAM:

    def __init__(self, name: str, paramValue: str):
        self.name = name
        self.paramValue = paramValue
        
        pass
    @property
    def paramValue(self):
        return self.__paramValue

    @paramValue.setter
    def paramValue(self, paramValue: str):
        self.__paramValue = paramValue


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Html_APPLET:

    def __init__(self, applet: str, class_: str, src: str, align: str, width: str, height: str):
        self.applet = applet
        self.class_ = class_
        self.src = src
        self.align = align
        self.width = width
        self.height = height
        
        pass
    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def applet(self):
        return self.__applet

    @applet.setter
    def applet(self, applet: str):
        self.__applet = applet


    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_: str):
        self.__class_ = class_


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


class Html_DD:

    pass
class Html_DT:

    pass
class Html_DL:

    pass
class ListElement:

    pass
class Html_LI(ListElement):

    def __init__(self, liValue: str):
        self.liValue = liValue
        
        pass
    @property
    def liValue(self):
        return self.__liValue

    @liValue.setter
    def liValue(self, liValue: str):
        self.__liValue = liValue


class Html_UL(ListElement):

    pass
class Html_OL(ListElement):

    def __init__(self, start: str):
        self.start = start
        
        pass
    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start


class Html_ListElement(ABC):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class Html_FRAMESET:

    def __init__(self, rows: str, cols: str, framespacing: str, frameborder: str, border: str):
        self.rows = rows
        self.cols = cols
        self.framespacing = framespacing
        self.frameborder = frameborder
        self.border = border
        
        pass
    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border


    @property
    def rows(self):
        return self.__rows

    @rows.setter
    def rows(self, rows: str):
        self.__rows = rows


    @property
    def cols(self):
        return self.__cols

    @cols.setter
    def cols(self, cols: str):
        self.__cols = cols


    @property
    def framespacing(self):
        return self.__framespacing

    @framespacing.setter
    def framespacing(self, framespacing: str):
        self.__framespacing = framespacing


    @property
    def frameborder(self):
        return self.__frameborder

    @frameborder.setter
    def frameborder(self, frameborder: str):
        self.__frameborder = frameborder


class Html_OBJECT:

    def __init__(self, classid: str, data: str, type: str, standby: str):
        self.classid = classid
        self.data = data
        self.type = type
        self.standby = standby
        
        pass
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


    @property
    def classid(self):
        return self.__classid

    @classid.setter
    def classid(self, classid: str):
        self.__classid = classid


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def standby(self):
        return self.__standby

    @standby.setter
    def standby(self, standby: str):
        self.__standby = standby


class Html_INPUT:

    def __init__(self, type: str, align: str, maxlength: str, size: str, checked: str, src: str, inputValue: str, name: str):
        self.type = type
        self.align = align
        self.maxlength = maxlength
        self.size = size
        self.checked = checked
        self.src = src
        self.inputValue = inputValue
        self.name = name
        
        pass
    @property
    def inputValue(self):
        return self.__inputValue

    @inputValue.setter
    def inputValue(self, inputValue: str):
        self.__inputValue = inputValue


    @property
    def maxlength(self):
        return self.__maxlength

    @maxlength.setter
    def maxlength(self, maxlength: str):
        self.__maxlength = maxlength


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def checked(self):
        return self.__checked

    @checked.setter
    def checked(self, checked: str):
        self.__checked = checked

