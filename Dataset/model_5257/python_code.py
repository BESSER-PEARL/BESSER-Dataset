from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FRAME:

    pass
class HTML_IFRAME(FRAME):

    pass
class HTML_NOFRAME:

    pass
class HTML_FRAME:

    def __init__(self, src: str, name: str, marginwidth: str, marginheight: str, scrolling: str, noresize: str):
        self.src = src
        self.name = name
        self.marginwidth = marginwidth
        self.marginheight = marginheight
        self.scrolling = scrolling
        self.noresize = noresize
        
        pass
    @property
    def noresize(self):
        return self.__noresize

    @noresize.setter
    def noresize(self, noresize: str):
        self.__noresize = noresize


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def scrolling(self):
        return self.__scrolling

    @scrolling.setter
    def scrolling(self, scrolling: str):
        self.__scrolling = scrolling


    @property
    def marginheight(self):
        return self.__marginheight

    @marginheight.setter
    def marginheight(self, marginheight: str):
        self.__marginheight = marginheight


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def marginwidth(self):
        return self.__marginwidth

    @marginwidth.setter
    def marginwidth(self, marginwidth: str):
        self.__marginwidth = marginwidth


class HTML_TEXTAREA:

    def __init__(self, cols: str, name: str, rows: str):
        self.cols = cols
        self.name = name
        self.rows = rows
        
        pass
    @property
    def rows(self):
        return self.__rows

    @rows.setter
    def rows(self, rows: str):
        self.__rows = rows


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def cols(self):
        return self.__cols

    @cols.setter
    def cols(self, cols: str):
        self.__cols = cols


class HTML_FRAMESET:

    def __init__(self, border: str, rows: str, cols: str, framespacing: str, frameborder: str):
        self.border = border
        self.rows = rows
        self.cols = cols
        self.framespacing = framespacing
        self.frameborder = frameborder
        
        pass
    @property
    def frameborder(self):
        return self.__frameborder

    @frameborder.setter
    def frameborder(self, frameborder: str):
        self.__frameborder = frameborder


    @property
    def rows(self):
        return self.__rows

    @rows.setter
    def rows(self, rows: str):
        self.__rows = rows


    @property
    def framespacing(self):
        return self.__framespacing

    @framespacing.setter
    def framespacing(self, framespacing: str):
        self.__framespacing = framespacing


    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border


    @property
    def cols(self):
        return self.__cols

    @cols.setter
    def cols(self, cols: str):
        self.__cols = cols


class HTML_OBJECT:

    def __init__(self, classid: str, id: str, data: str, type: str, standby: str):
        self.classid = classid
        self.id = id
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
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def standby(self):
        return self.__standby

    @standby.setter
    def standby(self, standby: str):
        self.__standby = standby


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def classid(self):
        return self.__classid

    @classid.setter
    def classid(self, classid: str):
        self.__classid = classid


class HTML_PARAM:

    def __init__(self, name: str, paramValue: str):
        self.name = name
        self.paramValue = paramValue
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def paramValue(self):
        return self.__paramValue

    @paramValue.setter
    def paramValue(self, paramValue: str):
        self.__paramValue = paramValue


class HTML_APPLET:

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
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


class HTML_DD:

    pass
class HTML_DT:

    pass
class HTML_DL:

    pass
class ListElement:

    pass
class HTML_UL(ListElement):

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


class HTML_INPUT:

    def __init__(self, align: str, maxlength: str, size: str, checked: str, src: str, inputValue: str, name: str, type: str):
        self.align = align
        self.maxlength = maxlength
        self.size = size
        self.checked = checked
        self.src = src
        self.inputValue = inputValue
        self.name = name
        self.type = type
        
        pass
    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


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


    @property
    def checked(self):
        return self.__checked

    @checked.setter
    def checked(self, checked: str):
        self.__checked = checked


    @property
    def inputValue(self):
        return self.__inputValue

    @inputValue.setter
    def inputValue(self, inputValue: str):
        self.__inputValue = inputValue


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def maxlength(self):
        return self.__maxlength

    @maxlength.setter
    def maxlength(self, maxlength: str):
        self.__maxlength = maxlength


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class HTML_FORM:

    def __init__(self, action: str, method: str):
        self.action = action
        self.method = method
        
        pass
    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


class TD:

    pass
class HTML_TH(TD):

    pass
class TABLEElement:

    pass
class HTML_TD(TABLEElement):

    def __init__(self, colspan: str, rowspan: str, valign: str, align: str, width: str, TD: "HTML_TR" = None, tds: "HTML_TR" = None):
        self.colspan = colspan
        self.rowspan = rowspan
        self.valign = valign
        self.align = align
        self.width = width
        self.TD = TD
        self.tds = tds
        
        pass
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
    def tds(self):
        return self.__tds

    @tds.setter
    def tds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TD__tds", None)
        self.__tds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TR17"):
                opp_val = getattr(old_value, "TR17", None)
                if opp_val == self:
                    setattr(old_value, "TR17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TR17"):
                opp_val = getattr(value, "TR17", None)
                setattr(value, "TR17", self)

    @property
    def TD(self):
        return self.__TD

    @TD.setter
    def TD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TD__TD", None)
        self.__TD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tr"):
                opp_val = getattr(old_value, "tr", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tr"):
                opp_val = getattr(value, "tr", None)
                if opp_val is None:
                    setattr(value, "tr", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HTML_TR(TABLEElement):

    def __init__(self, valign: str, align: str, TR: "HTML_TABLE" = None, trs: "HTML_TABLE" = None, tr: set["HTML_TD"] = None, TR17: "HTML_TD" = None):
        self.valign = valign
        self.align = align
        self.TR = TR
        self.trs = trs
        self.tr = tr if tr is not None else set()
        self.TR17 = TR17
        
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
    def TR17(self):
        return self.__TR17

    @TR17.setter
    def TR17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TR__TR17", None)
        self.__TR17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tds"):
                opp_val = getattr(old_value, "tds", None)
                if opp_val == self:
                    setattr(old_value, "tds", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tds"):
                opp_val = getattr(value, "tds", None)
                setattr(value, "tds", self)

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

    @property
    def TR(self):
        return self.__TR

    @TR.setter
    def TR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TR__TR", None)
        self.__TR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table"):
                opp_val = getattr(old_value, "table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table"):
                opp_val = getattr(value, "table", None)
                if opp_val is None:
                    setattr(value, "table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HTML_TABLE(TABLEElement):

    def __init__(self, cellpadding: str, border: str, width: str, cellspacing: str, table: set["HTML_TR"] = None, TABLE: "HTML_TR" = None):
        self.cellpadding = cellpadding
        self.border = border
        self.width = width
        self.cellspacing = cellspacing
        self.table = table if table is not None else set()
        self.TABLE = TABLE
        
        pass
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
                    

    @property
    def TABLE(self):
        return self.__TABLE

    @TABLE.setter
    def TABLE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TABLE__TABLE", None)
        self.__TABLE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trs"):
                opp_val = getattr(old_value, "trs", None)
                if opp_val == self:
                    setattr(old_value, "trs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trs"):
                opp_val = getattr(value, "trs", None)
                setattr(value, "trs", self)

class BODYElement:

    pass
class HTML_PRE(BODYElement):

    pass
class HTML_H2(BODYElement):

    pass
class HTML_H3(BODYElement):

    pass
class HTML_AREA(BODYElement):

    def __init__(self, shape: str, coords: str, ahref: str):
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
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, coords: str):
        self.__coords = coords


    @property
    def ahref(self):
        return self.__ahref

    @ahref.setter
    def ahref(self, ahref: str):
        self.__ahref = ahref


class HTML_STYLE(BODYElement):

    pass
class HTML_BR(BODYElement):

    def __init__(self, clear: str):
        self.clear = clear
        
        pass
    @property
    def clear(self):
        return self.__clear

    @clear.setter
    def clear(self, clear: str):
        self.__clear = clear


class HTML_MAP(BODYElement):

    pass
class HTML_P(BODYElement):

    pass
class HTML_SUP(BODYElement):

    pass
class HTML_TABLEElement(BODYElement):

    def __init__(self, bgcolor: str, background: str):
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


class HTML_SMALL(BODYElement):

    pass
class HTML_SPAN(BODYElement):

    def __init__(self, style: str):
        self.style = style
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


class HTML_FONT(BODYElement):

    def __init__(self, color: str, face: str, size: str):
        self.color = color
        self.face = face
        self.size = size
        
        pass
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


    @property
    def face(self):
        return self.__face

    @face.setter
    def face(self, face: str):
        self.__face = face


class HTML_STRONG(BODYElement):

    pass
class HTML_H4(BODYElement):

    pass
class HTML_EMBED(BODYElement):

    def __init__(self, src: str, width: str, height: str, align: str, vspace: str, hspace: str, border: str):
        self.src = src
        self.width = width
        self.height = height
        self.align = align
        self.vspace = vspace
        self.hspace = hspace
        self.border = border
        
        pass
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


class HTML_B(BODYElement):

    pass
class HTML_I(BODYElement):

    pass
class HTML_A(BODYElement):

    def __init__(self, ahref: str, name: str, id: str):
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


class HTML_TT(BODYElement):

    pass
class HTML_STRIKE(BODYElement):

    pass
class HTML_EM(BODYElement):

    pass
class HTML_DIV(BODYElement):

    def __init__(self, align: str):
        self.align = align
        
        pass
    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


class HTML_IMG(BODYElement):

    def __init__(self, src: str, width: str, height: str, alt: str, align: str, border: str, vspace: str, hspace: str, ismap: str, usemap: str):
        self.src = src
        self.width = width
        self.height = height
        self.alt = alt
        self.align = align
        self.border = border
        self.vspace = vspace
        self.hspace = hspace
        self.ismap = ismap
        self.usemap = usemap
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


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
    def usemap(self):
        return self.__usemap

    @usemap.setter
    def usemap(self, usemap: str):
        self.__usemap = usemap


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
    def ismap(self):
        return self.__ismap

    @ismap.setter
    def ismap(self, ismap: str):
        self.__ismap = ismap


    @property
    def hspace(self):
        return self.__hspace

    @hspace.setter
    def hspace(self, hspace: str):
        self.__hspace = hspace


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def alt(self):
        return self.__alt

    @alt.setter
    def alt(self, alt: str):
        self.__alt = alt


class HTML_BIG(BODYElement):

    pass
class HTML_SUB(BODYElement):

    pass
class HTML_NOEMBED(BODYElement):

    pass
class HTML_H1(BODYElement):

    pass
class HEADElement:

    pass
class HTML_TITLE(HEADElement):

    pass
class HTML_LINK(HEADElement):

    def __init__(self, rel: str, title: str, ahref: str, type: str):
        self.rel = rel
        self.title = title
        self.ahref = ahref
        self.type = type
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


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
class HTML_HEADElement(HTMLElement):

    pass
class HTML_BODYElement(HTMLElement):

    pass
class HTML_HTMLElement:

    def __init__(self, value: str, HTML_HTMLElement: "HTML_HTMLElement" = None, HTML_HTMLElement3: set["HTML_HTMLElement"] = None):
        self.value = value
        self.HTML_HTMLElement = HTML_HTMLElement
        self.HTML_HTMLElement3 = HTML_HTMLElement3 if HTML_HTMLElement3 is not None else set()
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def HTML_HTMLElement3(self):
        return self.__HTML_HTMLElement3

    @HTML_HTMLElement3.setter
    def HTML_HTMLElement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_HTMLElement__HTML_HTMLElement3", None)
        self.__HTML_HTMLElement3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HTML_HTMLElement"):
                    opp_val = getattr(item, "HTML_HTMLElement", None)
                    
                    if opp_val == self:
                        setattr(item, "HTML_HTMLElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HTML_HTMLElement"):
                    opp_val = getattr(item, "HTML_HTMLElement", None)
                    
                    setattr(item, "HTML_HTMLElement", self)
                    

    @property
    def HTML_HTMLElement(self):
        return self.__HTML_HTMLElement

    @HTML_HTMLElement.setter
    def HTML_HTMLElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_HTMLElement__HTML_HTMLElement", None)
        self.__HTML_HTMLElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HTML_HTMLElement3"):
                opp_val = getattr(old_value, "HTML_HTMLElement3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HTML_HTMLElement3"):
                opp_val = getattr(value, "HTML_HTMLElement3", None)
                if opp_val is None:
                    setattr(value, "HTML_HTMLElement3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HTML_BODY(HTMLElement):

    def __init__(self, link: str, alink: str, vlink: str, background: str, bgcolor: str, text: str, BODY: "HTML_HTML" = None, HTML_BODY: set["HTML_BODYElement"] = None, body: "HTML_HTML" = None):
        self.link = link
        self.alink = alink
        self.vlink = vlink
        self.background = background
        self.bgcolor = bgcolor
        self.text = text
        self.BODY = BODY
        self.HTML_BODY = HTML_BODY if HTML_BODY is not None else set()
        self.body = body
        
        pass
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
    def alink(self):
        return self.__alink

    @alink.setter
    def alink(self, alink: str):
        self.__alink = alink


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


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
    def BODY(self):
        return self.__BODY

    @BODY.setter
    def BODY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_BODY__BODY", None)
        self.__BODY = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html2"):
                opp_val = getattr(old_value, "html2", None)
                if opp_val == self:
                    setattr(old_value, "html2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html2"):
                opp_val = getattr(value, "html2", None)
                setattr(value, "html2", self)

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_BODY__body", None)
        self.__body = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HTML12"):
                opp_val = getattr(old_value, "HTML12", None)
                if opp_val == self:
                    setattr(old_value, "HTML12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HTML12"):
                opp_val = getattr(value, "HTML12", None)
                setattr(value, "HTML12", self)

    @property
    def HTML_BODY(self):
        return self.__HTML_BODY

    @HTML_BODY.setter
    def HTML_BODY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_BODY__HTML_BODY", None)
        self.__HTML_BODY = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HTML_BODYElement"):
                    opp_val = getattr(item, "HTML_BODYElement", None)
                    
                    if opp_val == self:
                        setattr(item, "HTML_BODYElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HTML_BODYElement"):
                    opp_val = getattr(item, "HTML_BODYElement", None)
                    
                    setattr(item, "HTML_BODYElement", self)
                    

class HTML_HEAD(HTMLElement):

    pass
class HTML_HTML:

    pass