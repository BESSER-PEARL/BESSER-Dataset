from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class html_OBJECT:

    def __init__(self, data: str, type: str, standby: str, classid: str, id: str):
        self.data = data
        self.type = type
        self.standby = standby
        self.classid = classid
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def standby(self) -> str:
        return self.__standby

    @standby.setter
    def standby(self, standby: str):
        self.__standby = standby

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def classid(self) -> str:
        return self.__classid

    @classid.setter
    def classid(self, classid: str):
        self.__classid = classid

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

class html_PARAM:

    def __init__(self, name: str, paramValue: str):
        self.name = name
        self.paramValue = paramValue
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def paramValue(self) -> str:
        return self.__paramValue

    @paramValue.setter
    def paramValue(self, paramValue: str):
        self.__paramValue = paramValue

class FRAME:

    pass
class html_IFRAME(FRAME):

    pass
class html_NOFRAME:

    pass
class html_FRAME:

    def __init__(self, src: str, name: str, marginwidth: str, marginheight: str, scrolling: str, noresize: str):
        self.src = src
        self.name = name
        self.marginwidth = marginwidth
        self.marginheight = marginheight
        self.scrolling = scrolling
        self.noresize = noresize
        
    @property
    def noresize(self) -> str:
        return self.__noresize

    @noresize.setter
    def noresize(self, noresize: str):
        self.__noresize = noresize

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def scrolling(self) -> str:
        return self.__scrolling

    @scrolling.setter
    def scrolling(self, scrolling: str):
        self.__scrolling = scrolling

    @property
    def marginwidth(self) -> str:
        return self.__marginwidth

    @marginwidth.setter
    def marginwidth(self, marginwidth: str):
        self.__marginwidth = marginwidth

    @property
    def marginheight(self) -> str:
        return self.__marginheight

    @marginheight.setter
    def marginheight(self, marginheight: str):
        self.__marginheight = marginheight

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

class html_FRAMESET:

    def __init__(self, rows: str, cols: str, framespacing: str, frameborder: str, border: str):
        self.rows = rows
        self.cols = cols
        self.framespacing = framespacing
        self.frameborder = frameborder
        self.border = border
        
    @property
    def cols(self) -> str:
        return self.__cols

    @cols.setter
    def cols(self, cols: str):
        self.__cols = cols

    @property
    def frameborder(self) -> str:
        return self.__frameborder

    @frameborder.setter
    def frameborder(self, frameborder: str):
        self.__frameborder = frameborder

    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

    @property
    def framespacing(self) -> str:
        return self.__framespacing

    @framespacing.setter
    def framespacing(self, framespacing: str):
        self.__framespacing = framespacing

    @property
    def rows(self) -> str:
        return self.__rows

    @rows.setter
    def rows(self, rows: str):
        self.__rows = rows

class html_INPUT:

    def __init__(self, inputValue: str, name: str, type: str, align: str, maxlength: str, size: str, checked: str, src: str):
        self.inputValue = inputValue
        self.name = name
        self.type = type
        self.align = align
        self.maxlength = maxlength
        self.size = size
        self.checked = checked
        self.src = src
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def checked(self) -> str:
        return self.__checked

    @checked.setter
    def checked(self, checked: str):
        self.__checked = checked

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def maxlength(self) -> str:
        return self.__maxlength

    @maxlength.setter
    def maxlength(self, maxlength: str):
        self.__maxlength = maxlength

    @property
    def inputValue(self) -> str:
        return self.__inputValue

    @inputValue.setter
    def inputValue(self, inputValue: str):
        self.__inputValue = inputValue

class html_APPLET:

    def __init__(self, applet: str, class: str, src: str, align: str, width: str, height: str):
        self.applet = applet
        self.class = class
        self.src = src
        self.align = align
        self.width = width
        self.height = height
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def applet(self) -> str:
        return self.__applet

    @applet.setter
    def applet(self, applet: str):
        self.__applet = applet

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

class html_DD:

    pass
class html_DT:

    pass
class html_DL:

    pass
class ListElement:

    pass
class html_UL(ListElement):

    pass
class html_LI(ListElement):

    def __init__(self, liValue: str):
        self.liValue = liValue
        
    @property
    def liValue(self) -> str:
        return self.__liValue

    @liValue.setter
    def liValue(self, liValue: str):
        self.__liValue = liValue

class html_OL(ListElement):

    def __init__(self, start: str):
        self.start = start
        
    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

class html_ListElement(ABC):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class html_OPTION:

    def __init__(self, selected: str, optionValue: str):
        self.selected = selected
        self.optionValue = optionValue
        
    @property
    def selected(self) -> str:
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected

    @property
    def optionValue(self) -> str:
        return self.__optionValue

    @optionValue.setter
    def optionValue(self, optionValue: str):
        self.__optionValue = optionValue

class html_SELECT:

    def __init__(self, multiple: str, size: str, name: str):
        self.multiple = multiple
        self.size = size
        self.name = name
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def multiple(self) -> str:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: str):
        self.__multiple = multiple

class html_TEXTAREA:

    def __init__(self, name: str, rows: str, cols: str):
        self.name = name
        self.rows = rows
        self.cols = cols
        
    @property
    def rows(self) -> str:
        return self.__rows

    @rows.setter
    def rows(self, rows: str):
        self.__rows = rows

    @property
    def cols(self) -> str:
        return self.__cols

    @cols.setter
    def cols(self, cols: str):
        self.__cols = cols

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class html_FORM:

    def __init__(self, action: str, method: str):
        self.action = action
        self.method = method
        
    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

class TD:

    pass
class html_TH(TD):

    pass
class TABLEElement:

    pass
class html_TD(TABLEElement):

    def __init__(self, colspan: str, rowspan: str, valign: str, align: str, width: str, TD: "html_TR" = None, tds: "html_TR" = None):
        self.colspan = colspan
        self.rowspan = rowspan
        self.valign = valign
        self.align = align
        self.width = width
        self.TD = TD
        self.tds = tds
        
    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

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
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def TD(self):
        return self.__TD

    @TD.setter
    def TD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_TD__TD", None)
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
        old_value = getattr(self, f"_html_TD__tds", None)
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

class html_TR(TABLEElement):

    def __init__(self, valign: str, align: str, TR: "html_TABLE" = None, trs: "html_TABLE" = None, tr: set["html_TD"] = None, TR23: "html_TD" = None):
        self.valign = valign
        self.align = align
        self.TR = TR
        self.trs = trs
        self.tr = tr if tr is not None else set()
        self.TR23 = TR23
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def tr(self):
        return self.__tr

    @tr.setter
    def tr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_TR__tr", None)
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
        old_value = getattr(self, f"_html_TR__trs", None)
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
    def TR23(self):
        return self.__TR23

    @TR23.setter
    def TR23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_TR__TR23", None)
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
    def TR(self):
        return self.__TR

    @TR.setter
    def TR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_TR__TR", None)
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

class html_TABLE(TABLEElement):

    def __init__(self, border: str, width: str, cellspacing: str, cellpadding: str, table: set["html_TR"] = None, TABLE: "html_TR" = None):
        self.border = border
        self.width = width
        self.cellspacing = cellspacing
        self.cellpadding = cellpadding
        self.table = table if table is not None else set()
        self.TABLE = TABLE
        
    @property
    def cellspacing(self) -> str:
        return self.__cellspacing

    @cellspacing.setter
    def cellspacing(self, cellspacing: str):
        self.__cellspacing = cellspacing

    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def cellpadding(self) -> str:
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
        old_value = getattr(self, f"_html_TABLE__table", None)
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
        old_value = getattr(self, f"_html_TABLE__TABLE", None)
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
class html_TABLEElement(BODYElement):

    def __init__(self, background: str, bgcolor: str):
        self.background = background
        self.bgcolor = bgcolor
        
    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

    @property
    def bgcolor(self) -> str:
        return self.__bgcolor

    @bgcolor.setter
    def bgcolor(self, bgcolor: str):
        self.__bgcolor = bgcolor

class html_DIV(BODYElement):

    def __init__(self, align: str):
        self.align = align
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

class html_SUB(BODYElement):

    pass
class html_SMALL(BODYElement):

    pass
class html_H2(BODYElement):

    pass
class html_AREA(BODYElement):

    def __init__(self, shape: str, coords: str, ahref: str):
        self.shape = shape
        self.coords = coords
        self.ahref = ahref
        
    @property
    def ahref(self) -> str:
        return self.__ahref

    @ahref.setter
    def ahref(self, ahref: str):
        self.__ahref = ahref

    @property
    def coords(self) -> str:
        return self.__coords

    @coords.setter
    def coords(self, coords: str):
        self.__coords = coords

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

class html_NOEMBED(BODYElement):

    pass
class html_STRIKE(BODYElement):

    pass
class html_EMBED(BODYElement):

    def __init__(self, src: str, width: str, height: str, align: str, vspace: str, hspace: str, border: str):
        self.src = src
        self.width = width
        self.height = height
        self.align = align
        self.vspace = vspace
        self.hspace = hspace
        self.border = border
        
    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def vspace(self) -> str:
        return self.__vspace

    @vspace.setter
    def vspace(self, vspace: str):
        self.__vspace = vspace

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def hspace(self) -> str:
        return self.__hspace

    @hspace.setter
    def hspace(self, hspace: str):
        self.__hspace = hspace

class html_EM(BODYElement):

    pass
class html_BR(BODYElement):

    def __init__(self, clear: str):
        self.clear = clear
        
    @property
    def clear(self) -> str:
        return self.__clear

    @clear.setter
    def clear(self, clear: str):
        self.__clear = clear

class html_H4(BODYElement):

    pass
class html_IMG(BODYElement):

    def __init__(self, hspace: str, ismap: str, usemap: str, border: str, src: str, width: str, height: str, alt: str, align: str, vspace: str):
        self.hspace = hspace
        self.ismap = ismap
        self.usemap = usemap
        self.border = border
        self.src = src
        self.width = width
        self.height = height
        self.alt = alt
        self.align = align
        self.vspace = vspace
        
    @property
    def alt(self) -> str:
        return self.__alt

    @alt.setter
    def alt(self, alt: str):
        self.__alt = alt

    @property
    def vspace(self) -> str:
        return self.__vspace

    @vspace.setter
    def vspace(self, vspace: str):
        self.__vspace = vspace

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def ismap(self) -> str:
        return self.__ismap

    @ismap.setter
    def ismap(self, ismap: str):
        self.__ismap = ismap

    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def usemap(self) -> str:
        return self.__usemap

    @usemap.setter
    def usemap(self, usemap: str):
        self.__usemap = usemap

    @property
    def hspace(self) -> str:
        return self.__hspace

    @hspace.setter
    def hspace(self, hspace: str):
        self.__hspace = hspace

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

class html_FONT(BODYElement):

    def __init__(self, color: str, face: str, size: str):
        self.color = color
        self.face = face
        self.size = size
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

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

class html_STYLE(BODYElement):

    pass
class html_STRONG(BODYElement):

    pass
class html_BIG(BODYElement):

    pass
class html_SPAN(BODYElement):

    def __init__(self, style: str):
        self.style = style
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

class html_A(BODYElement):

    def __init__(self, ahref: str, name: str, id: str):
        self.ahref = ahref
        self.name = name
        self.id = id
        
    @property
    def ahref(self) -> str:
        return self.__ahref

    @ahref.setter
    def ahref(self, ahref: str):
        self.__ahref = ahref

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class html_PRE(BODYElement):

    pass
class html_TT(BODYElement):

    pass
class html_B(BODYElement):

    pass
class html_SUP(BODYElement):

    pass
class html_H3(BODYElement):

    pass
class html_I(BODYElement):

    pass
class html_P(BODYElement):

    pass
class html_MAP(BODYElement):

    pass
class html_H1(BODYElement):

    pass
class HEADElement:

    pass
class html_TITLE(HEADElement):

    pass
class html_LINK(HEADElement):

    def __init__(self, rel: str, title: str, ahref: str, type: str):
        self.rel = rel
        self.title = title
        self.ahref = ahref
        self.type = type
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def rel(self) -> str:
        return self.__rel

    @rel.setter
    def rel(self, rel: str):
        self.__rel = rel

    @property
    def ahref(self) -> str:
        return self.__ahref

    @ahref.setter
    def ahref(self, ahref: str):
        self.__ahref = ahref

class HTMLElement:

    pass
class html_BODYElement(HTMLElement):

    pass
class html_HEADElement(HTMLElement):

    pass
class html_HTMLElement:

    def __init__(self, value: str, HTMLElement: "html_HTMLElement" = None, parent: set["html_HTMLElement"] = None, HTMLElement7: "html_HTMLElement" = None, children: "html_HTMLElement" = None):
        self.value = value
        self.HTMLElement = HTMLElement
        self.parent = parent if parent is not None else set()
        self.HTMLElement7 = HTMLElement7
        self.children = children
        
    @property
    def value(self) -> str:
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
        old_value = getattr(self, f"_html_HTMLElement__parent", None)
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
    def HTMLElement(self):
        return self.__HTMLElement

    @HTMLElement.setter
    def HTMLElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_HTMLElement__HTMLElement", None)
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
        old_value = getattr(self, f"_html_HTMLElement__children", None)
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

    @property
    def HTMLElement7(self):
        return self.__HTMLElement7

    @HTMLElement7.setter
    def HTMLElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_HTMLElement__HTMLElement7", None)
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

class html_BODY(HTMLElement):

    def __init__(self, background: str, bgcolor: str, text: str, link: str, alink: str, vlink: str, BODY: "html_HTML" = None, body: set["html_BODYElement"] = None, body15: "html_HTML" = None, BODY18: "html_BODYElement" = None):
        self.background = background
        self.bgcolor = bgcolor
        self.text = text
        self.link = link
        self.alink = alink
        self.vlink = vlink
        self.BODY = BODY
        self.body = body if body is not None else set()
        self.body15 = body15
        self.BODY18 = BODY18
        
    @property
    def bgcolor(self) -> str:
        return self.__bgcolor

    @bgcolor.setter
    def bgcolor(self, bgcolor: str):
        self.__bgcolor = bgcolor

    @property
    def alink(self) -> str:
        return self.__alink

    @alink.setter
    def alink(self, alink: str):
        self.__alink = alink

    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

    @property
    def link(self) -> str:
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def vlink(self) -> str:
        return self.__vlink

    @vlink.setter
    def vlink(self, vlink: str):
        self.__vlink = vlink

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_BODY__body", None)
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
    def body15(self):
        return self.__body15

    @body15.setter
    def body15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_BODY__body15", None)
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
        old_value = getattr(self, f"_html_BODY__BODY18", None)
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
    def BODY(self):
        return self.__BODY

    @BODY.setter
    def BODY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_BODY__BODY", None)
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

class html_HEAD(HTMLElement):

    pass
class html_HTML:

    pass