from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class defaultname_FRAMESET:

    def __init__(self, cols: str, framespacing: str, frameborder: str, border: str, rows: str):
        self.cols = cols
        self.framespacing = framespacing
        self.frameborder = frameborder
        self.border = border
        self.rows = rows
        
        pass
    @property
    def frameborder(self):
        return self.__frameborder

    @frameborder.setter
    def frameborder(self, frameborder: str):
        self.__frameborder = frameborder


    @property
    def cols(self):
        return self.__cols

    @cols.setter
    def cols(self, cols: str):
        self.__cols = cols


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
    def framespacing(self):
        return self.__framespacing

    @framespacing.setter
    def framespacing(self, framespacing: str):
        self.__framespacing = framespacing


class FRAME:

    pass
class defaultname_IFRAME(FRAME):

    pass
class defaultname_NOFRAME:

    pass
class defaultname_FRAME:

    def __init__(self, src: str, name: str, marginwidth: str, marginheight: str, scrolling: str, noresize: str):
        self.src = src
        self.name = name
        self.marginwidth = marginwidth
        self.marginheight = marginheight
        self.scrolling = scrolling
        self.noresize = noresize
        
        pass
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
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def noresize(self):
        return self.__noresize

    @noresize.setter
    def noresize(self, noresize: str):
        self.__noresize = noresize


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


class defaultname_TEXTAREA:

    def __init__(self, rows: str, cols: str, name: str):
        self.rows = rows
        self.cols = cols
        self.name = name
        
        pass
    @property
    def cols(self):
        return self.__cols

    @cols.setter
    def cols(self, cols: str):
        self.__cols = cols


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


class defaultname_OBJECT:

    def __init__(self, classid: str, id: str, data: str, type: str, standby: str):
        self.classid = classid
        self.id = id
        self.data = data
        self.type = type
        self.standby = standby
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def classid(self):
        return self.__classid

    @classid.setter
    def classid(self, classid: str):
        self.__classid = classid


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


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


class defaultname_PARAM:

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


class defaultname_APPLET:

    def __init__(self, applet: str, class_: str, src: str, align: str, width: str, height: str):
        self.applet = applet
        self.class_ = class_
        self.src = src
        self.align = align
        self.width = width
        self.height = height
        
        pass
    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, class_: str):
        self.__class_ = class_


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


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
    def applet(self):
        return self.__applet

    @applet.setter
    def applet(self, applet: str):
        self.__applet = applet


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


class defaultname_DD:

    pass
class defaultname_DT:

    pass
class defaultname_DL:

    pass
class ListElement:

    pass
class defaultname_UL(ListElement):

    pass
class defaultname_LI(ListElement):

    def __init__(self, liValue: str):
        self.liValue = liValue
        
        pass
    @property
    def liValue(self):
        return self.__liValue

    @liValue.setter
    def liValue(self, liValue: str):
        self.__liValue = liValue


class defaultname_OL(ListElement):

    def __init__(self, start: str):
        self.start = start
        
        pass
    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start


class defaultname_ListElement(ABC):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class defaultname_OPTION:

    def __init__(self, selected: str, optionValue: str):
        self.selected = selected
        self.optionValue = optionValue
        
        pass
    @property
    def optionValue(self):
        return self.__optionValue

    @optionValue.setter
    def optionValue(self, optionValue: str):
        self.__optionValue = optionValue


    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected


class defaultname_SELECT:

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


class TABLEElement:

    pass
class defaultname_TABLE(TABLEElement):

    def __init__(self, width: str, cellspacing: str, cellpadding: str, border: str, table: set["defaultname_TR"] = None, TABLE: "defaultname_TR" = None):
        self.width = width
        self.cellspacing = cellspacing
        self.cellpadding = cellpadding
        self.border = border
        self.table = table if table is not None else set()
        self.TABLE = TABLE
        
        pass
    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border


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
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def TABLE(self):
        return self.__TABLE

    @TABLE.setter
    def TABLE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_TABLE__TABLE", None)
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

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_TABLE__table", None)
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
                    

class defaultname_INPUT:

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
    def inputValue(self):
        return self.__inputValue

    @inputValue.setter
    def inputValue(self, inputValue: str):
        self.__inputValue = inputValue


    @property
    def checked(self):
        return self.__checked

    @checked.setter
    def checked(self, checked: str):
        self.__checked = checked


    @property
    def maxlength(self):
        return self.__maxlength

    @maxlength.setter
    def maxlength(self, maxlength: str):
        self.__maxlength = maxlength


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class defaultname_FORM:

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
class defaultname_TH(TD):

    pass
class defaultname_TD(TABLEElement):

    def __init__(self, colspan: str, rowspan: str, valign: str, align: str, width: str, TD: "defaultname_TR" = None, tds: "defaultname_TR" = None):
        self.colspan = colspan
        self.rowspan = rowspan
        self.valign = valign
        self.align = align
        self.width = width
        self.TD = TD
        self.tds = tds
        
        pass
    @property
    def valign(self):
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign


    @property
    def rowspan(self):
        return self.__rowspan

    @rowspan.setter
    def rowspan(self, rowspan: str):
        self.__rowspan = rowspan


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def colspan(self):
        return self.__colspan

    @colspan.setter
    def colspan(self, colspan: str):
        self.__colspan = colspan


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def TD(self):
        return self.__TD

    @TD.setter
    def TD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_TD__TD", None)
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

    @property
    def tds(self):
        return self.__tds

    @tds.setter
    def tds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_TD__tds", None)
        self.__tds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TR23"):
                opp_val = getattr(old_value, "TR23", None)
                if opp_val == self:
                    setattr(old_value, "TR23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TR23"):
                opp_val = getattr(value, "TR23", None)
                setattr(value, "TR23", self)

class defaultname_TR(TABLEElement):

    def __init__(self, valign: str, align: str, trs: "defaultname_TABLE" = None, tr: set["defaultname_TD"] = None, TR23: "defaultname_TD" = None, TR: "defaultname_TABLE" = None):
        self.valign = valign
        self.align = align
        self.trs = trs
        self.tr = tr if tr is not None else set()
        self.TR23 = TR23
        self.TR = TR
        
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
    def TR(self):
        return self.__TR

    @TR.setter
    def TR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_TR__TR", None)
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

    @property
    def tr(self):
        return self.__tr

    @tr.setter
    def tr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_TR__tr", None)
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
    def TR23(self):
        return self.__TR23

    @TR23.setter
    def TR23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_TR__TR23", None)
        self.__TR23 = value
        
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
    def trs(self):
        return self.__trs

    @trs.setter
    def trs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_TR__trs", None)
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

class BODYElement:

    pass
class defaultname_H4(BODYElement):

    pass
class defaultname_H3(BODYElement):

    pass
class defaultname_SMALL(BODYElement):

    pass
class defaultname_A(BODYElement):

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
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class defaultname_STRONG(BODYElement):

    pass
class defaultname_TT(BODYElement):

    pass
class defaultname_NOEMBED(BODYElement):

    pass
class defaultname_I(BODYElement):

    pass
class defaultname_BR(BODYElement):

    def __init__(self, clear: str):
        self.clear = clear
        
        pass
    @property
    def clear(self):
        return self.__clear

    @clear.setter
    def clear(self, clear: str):
        self.__clear = clear


class defaultname_B(BODYElement):

    pass
class defaultname_BIG(BODYElement):

    pass
class defaultname_EM(BODYElement):

    pass
class defaultname_EMBED(BODYElement):

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
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def hspace(self):
        return self.__hspace

    @hspace.setter
    def hspace(self, hspace: str):
        self.__hspace = hspace


    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


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
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


class defaultname_MAP(BODYElement):

    pass
class defaultname_DIV(BODYElement):

    def __init__(self, align: str):
        self.align = align
        
        pass
    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


class defaultname_IMG(BODYElement):

    def __init__(self, src: str, width: str, height: str, alt: str, align: str, vspace: str, hspace: str, ismap: str, usemap: str, border: str):
        self.src = src
        self.width = width
        self.height = height
        self.alt = alt
        self.align = align
        self.vspace = vspace
        self.hspace = hspace
        self.ismap = ismap
        self.usemap = usemap
        self.border = border
        
        pass
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


    @property
    def ismap(self):
        return self.__ismap

    @ismap.setter
    def ismap(self, ismap: str):
        self.__ismap = ismap


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def vspace(self):
        return self.__vspace

    @vspace.setter
    def vspace(self, vspace: str):
        self.__vspace = vspace


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
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


class defaultname_FONT(BODYElement):

    def __init__(self, color: str, face: str, size: str):
        self.color = color
        self.face = face
        self.size = size
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def face(self):
        return self.__face

    @face.setter
    def face(self, face: str):
        self.__face = face


class defaultname_STYLE(BODYElement):

    pass
class defaultname_TABLEElement(BODYElement):

    def __init__(self, bgcolor: str, background: str):
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


class defaultname_PRE(BODYElement):

    pass
class defaultname_H2(BODYElement):

    pass
class defaultname_SUB(BODYElement):

    pass
class defaultname_P(BODYElement):

    pass
class defaultname_STRIKE(BODYElement):

    pass
class defaultname_AREA(BODYElement):

    def __init__(self, shape: str, coords: str, ahref: str):
        self.shape = shape
        self.coords = coords
        self.ahref = ahref
        
        pass
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


    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


class defaultname_SUP(BODYElement):

    pass
class defaultname_SPAN(BODYElement):

    def __init__(self, style: str):
        self.style = style
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


class defaultname_H1(BODYElement):

    pass
class HEADElement:

    pass
class defaultname_TITLE(HEADElement):

    pass
class defaultname_LINK(HEADElement):

    def __init__(self, rel: str, title: str, ahref: str, type: str):
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
class defaultname_BODYElement(HTMLElement):

    pass
class defaultname_HEADElement(HTMLElement):

    pass
class defaultname_BODY(HTMLElement):

    def __init__(self, background: str, bgcolor: str, text: str, link: str, alink: str, vlink: str, BODY: "defaultname_HTML" = None, body: set["defaultname_BODYElement"] = None, BODY18: "defaultname_BODYElement" = None, body15: "defaultname_HTML" = None):
        self.background = background
        self.bgcolor = bgcolor
        self.text = text
        self.link = link
        self.alink = alink
        self.vlink = vlink
        self.BODY = BODY
        self.body = body if body is not None else set()
        self.BODY18 = BODY18
        self.body15 = body15
        
        pass
    @property
    def vlink(self):
        return self.__vlink

    @vlink.setter
    def vlink(self, vlink: str):
        self.__vlink = vlink


    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background


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
    def BODY(self):
        return self.__BODY

    @BODY.setter
    def BODY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_BODY__BODY", None)
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
    def body15(self):
        return self.__body15

    @body15.setter
    def body15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_BODY__body15", None)
        self.__body15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HTML16"):
                opp_val = getattr(old_value, "HTML16", None)
                if opp_val == self:
                    setattr(old_value, "HTML16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HTML16"):
                opp_val = getattr(value, "HTML16", None)
                setattr(value, "HTML16", self)

    @property
    def BODY18(self):
        return self.__BODY18

    @BODY18.setter
    def BODY18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_BODY__BODY18", None)
        self.__BODY18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bodyElements"):
                opp_val = getattr(old_value, "bodyElements", None)
                if opp_val == self:
                    setattr(old_value, "bodyElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bodyElements"):
                opp_val = getattr(value, "bodyElements", None)
                setattr(value, "bodyElements", self)

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_BODY__body", None)
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
                    

class defaultname_HTMLElement:

    def __init__(self, value: str, HTMLElement: "defaultname_HTMLElement" = None, parent: set["defaultname_HTMLElement"] = None, HTMLElement7: "defaultname_HTMLElement" = None, children: "defaultname_HTMLElement" = None):
        self.value = value
        self.HTMLElement = HTMLElement
        self.parent = parent if parent is not None else set()
        self.HTMLElement7 = HTMLElement7
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
        old_value = getattr(self, f"_defaultname_HTMLElement__parent", None)
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
    def HTMLElement7(self):
        return self.__HTMLElement7

    @HTMLElement7.setter
    def HTMLElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_HTMLElement__HTMLElement7", None)
        self.__HTMLElement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def HTMLElement(self):
        return self.__HTMLElement

    @HTMLElement.setter
    def HTMLElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_HTMLElement__HTMLElement", None)
        self.__HTMLElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_defaultname_HTMLElement__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HTMLElement7"):
                opp_val = getattr(old_value, "HTMLElement7", None)
                if opp_val == self:
                    setattr(old_value, "HTMLElement7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HTMLElement7"):
                opp_val = getattr(value, "HTMLElement7", None)
                setattr(value, "HTMLElement7", self)

class defaultname_HEAD(HTMLElement):

    pass
class defaultname_HTML:

    pass