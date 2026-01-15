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
        
    @property
    def marginheight(self) -> str:
        return self.__marginheight

    @marginheight.setter
    def marginheight(self, marginheight: str):
        self.__marginheight = marginheight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def marginwidth(self) -> str:
        return self.__marginwidth

    @marginwidth.setter
    def marginwidth(self, marginwidth: str):
        self.__marginwidth = marginwidth

    @property
    def noresize(self) -> str:
        return self.__noresize

    @noresize.setter
    def noresize(self, noresize: str):
        self.__noresize = noresize

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def scrolling(self) -> str:
        return self.__scrolling

    @scrolling.setter
    def scrolling(self, scrolling: str):
        self.__scrolling = scrolling

class HTML_FRAMESET:

    def __init__(self, rows: str, cols: str, framespacing: str, frameborder: str, border: str):
        self.rows = rows
        self.cols = cols
        self.framespacing = framespacing
        self.frameborder = frameborder
        self.border = border
        
    @property
    def frameborder(self) -> str:
        return self.__frameborder

    @frameborder.setter
    def frameborder(self, frameborder: str):
        self.__frameborder = frameborder

    @property
    def framespacing(self) -> str:
        return self.__framespacing

    @framespacing.setter
    def framespacing(self, framespacing: str):
        self.__framespacing = framespacing

    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

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

class HTML_OBJECT:

    def __init__(self, classid: str, id: str, data: str, type: str, standby: str):
        self.classid = classid
        self.id = id
        self.data = data
        self.type = type
        self.standby = standby
        
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
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

class HTML_PARAM:

    def __init__(self, name: str, paramValue: str):
        self.name = name
        self.paramValue = paramValue
        
    @property
    def paramValue(self) -> str:
        return self.__paramValue

    @paramValue.setter
    def paramValue(self, paramValue: str):
        self.__paramValue = paramValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HTML_APPLET:

    def __init__(self, applet: str, class: str, src: str, align: str, width: str, height: str):
        self.applet = applet
        self.class = class
        self.src = src
        self.align = align
        self.width = width
        self.height = height
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

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
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

class HTML_DD:

    pass
class HTML_DT:

    pass
class HTML_DL:

    pass
class ListElement:

    pass
class HTML_LI(ListElement):

    def __init__(self, liValue: str):
        self.liValue = liValue
        
    @property
    def liValue(self) -> str:
        return self.__liValue

    @liValue.setter
    def liValue(self, liValue: str):
        self.__liValue = liValue

class HTML_UL(ListElement):

    pass
class HTML_OL(ListElement):

    def __init__(self, start: str):
        self.start = start
        
    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

class HTML_ListElement(ABC):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class HTML_OPTION:

    def __init__(self, selected: str, optionValue: str):
        self.selected = selected
        self.optionValue = optionValue
        
    @property
    def optionValue(self) -> str:
        return self.__optionValue

    @optionValue.setter
    def optionValue(self, optionValue: str):
        self.__optionValue = optionValue

    @property
    def selected(self) -> str:
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected

class HTML_SELECT:

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
    def multiple(self) -> str:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: str):
        self.__multiple = multiple

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HTML_TEXTAREA:

    def __init__(self, name: str, rows: str, cols: str):
        self.name = name
        self.rows = rows
        self.cols = cols
        
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

    @property
    def rows(self) -> str:
        return self.__rows

    @rows.setter
    def rows(self, rows: str):
        self.__rows = rows

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
        
    @property
    def maxlength(self) -> str:
        return self.__maxlength

    @maxlength.setter
    def maxlength(self, maxlength: str):
        self.__maxlength = maxlength

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

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
    def checked(self) -> str:
        return self.__checked

    @checked.setter
    def checked(self, checked: str):
        self.__checked = checked

    @property
    def inputValue(self) -> str:
        return self.__inputValue

    @inputValue.setter
    def inputValue(self, inputValue: str):
        self.__inputValue = inputValue

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class HTML_FORM:

    def __init__(self, action: str, method: str):
        self.action = action
        self.method = method
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

class TD:

    pass
class HTML_TH(TD):

    pass
class TABLE:

    pass
class TR:

    pass
class TABLEElement:

    pass
class HTML_TR(TABLEElement):

    def __init__(self, valign: str, align: str, 132: "TABLE" = None, 135: set["TD"] = None):
        self.valign = valign
        self.align = align
        self.132 = 132
        self.135 = 135 if 135 is not None else set()
        
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
    def 135(self):
        return self.__135

    @135.setter
    def 135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TR__135", None)
        self.__135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#36"):
                    opp_val = getattr(item, "#36", None)
                    
                    if opp_val == self:
                        setattr(item, "#36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#36"):
                    opp_val = getattr(item, "#36", None)
                    
                    setattr(item, "#36", self)
                    

    @property
    def 132(self):
        return self.__132

    @132.setter
    def 132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TR__132", None)
        self.__132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#33"):
                opp_val = getattr(old_value, "#33", None)
                if opp_val == self:
                    setattr(old_value, "#33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#33"):
                opp_val = getattr(value, "#33", None)
                setattr(value, "#33", self)

class HTML_TD(TABLEElement):

    def __init__(self, colspan: str, rowspan: str, valign: str, align: str, width: str, 138: "TR" = None):
        self.colspan = colspan
        self.rowspan = rowspan
        self.valign = valign
        self.align = align
        self.width = width
        self.138 = 138
        
    @property
    def colspan(self) -> str:
        return self.__colspan

    @colspan.setter
    def colspan(self, colspan: str):
        self.__colspan = colspan

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
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def rowspan(self) -> str:
        return self.__rowspan

    @rowspan.setter
    def rowspan(self, rowspan: str):
        self.__rowspan = rowspan

    @property
    def 138(self):
        return self.__138

    @138.setter
    def 138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TD__138", None)
        self.__138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#39"):
                opp_val = getattr(old_value, "#39", None)
                if opp_val == self:
                    setattr(old_value, "#39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#39"):
                opp_val = getattr(value, "#39", None)
                setattr(value, "#39", self)

class HTML_TABLE(TABLEElement):

    def __init__(self, border: str, width: str, cellspacing: str, cellpadding: str, 129: set["TR"] = None):
        self.border = border
        self.width = width
        self.cellspacing = cellspacing
        self.cellpadding = cellpadding
        self.129 = 129 if 129 is not None else set()
        
    @property
    def cellspacing(self) -> str:
        return self.__cellspacing

    @cellspacing.setter
    def cellspacing(self, cellspacing: str):
        self.__cellspacing = cellspacing

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
    def cellpadding(self) -> str:
        return self.__cellpadding

    @cellpadding.setter
    def cellpadding(self, cellpadding: str):
        self.__cellpadding = cellpadding

    @property
    def 129(self):
        return self.__129

    @129.setter
    def 129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_TABLE__129", None)
        self.__129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#30"):
                    opp_val = getattr(item, "#30", None)
                    
                    if opp_val == self:
                        setattr(item, "#30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#30"):
                    opp_val = getattr(item, "#30", None)
                    
                    setattr(item, "#30", self)
                    

class BODYElement:

    pass
class HTML_SMALL(BODYElement):

    pass
class HTML_P(BODYElement):

    pass
class HTML_DIV(BODYElement):

    def __init__(self, align: str, #21: "HTML_BODY"):
        self.align = align
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

class HTML_STRONG(BODYElement):

    pass
class HTML_H2(BODYElement):

    pass
class HTML_STRIKE(BODYElement):

    pass
class HTML_B(BODYElement):

    pass
class HTML_FONT(BODYElement):

    def __init__(self, color: str, face: str, size: str, #21: "HTML_BODY"):
        self.color = color
        self.face = face
        self.size = size
        
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
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class HTML_IMG(BODYElement):

    def __init__(self, src: str, width: str, height: str, alt: str, align: str, vspace: str, hspace: str, ismap: str, usemap: str, border: str, #21: "HTML_BODY"):
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
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

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
    def ismap(self) -> str:
        return self.__ismap

    @ismap.setter
    def ismap(self, ismap: str):
        self.__ismap = ismap

    @property
    def alt(self) -> str:
        return self.__alt

    @alt.setter
    def alt(self, alt: str):
        self.__alt = alt

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

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

class HTML_MAP(BODYElement):

    pass
class HTML_NOEMBED(BODYElement):

    pass
class HTML_TT(BODYElement):

    pass
class HTML_SUB(BODYElement):

    pass
class HTML_SPAN(BODYElement):

    def __init__(self, style: str, #21: "HTML_BODY"):
        self.style = style
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

class HTML_H3(BODYElement):

    pass
class HTML_AREA(BODYElement):

    def __init__(self, shape: str, coords: str, ahref: str, #21: "HTML_BODY"):
        self.shape = shape
        self.coords = coords
        self.ahref = ahref
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

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

class HTML_H4(BODYElement):

    pass
class HTML_SUP(BODYElement):

    pass
class HTML_EMBED(BODYElement):

    def __init__(self, src: str, width: str, height: str, align: str, vspace: str, hspace: str, border: str, #21: "HTML_BODY"):
        self.src = src
        self.width = width
        self.height = height
        self.align = align
        self.vspace = vspace
        self.hspace = hspace
        self.border = border
        
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
    def hspace(self) -> str:
        return self.__hspace

    @hspace.setter
    def hspace(self, hspace: str):
        self.__hspace = hspace

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def vspace(self) -> str:
        return self.__vspace

    @vspace.setter
    def vspace(self, vspace: str):
        self.__vspace = vspace

class HTML_I(BODYElement):

    pass
class HTML_EM(BODYElement):

    pass
class HTML_BIG(BODYElement):

    pass
class HTML_A(BODYElement):

    def __init__(self, ahref: str, name: str, id: str, #21: "HTML_BODY"):
        self.ahref = ahref
        self.name = name
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ahref(self) -> str:
        return self.__ahref

    @ahref.setter
    def ahref(self, ahref: str):
        self.__ahref = ahref

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class HTML_BR(BODYElement):

    def __init__(self, clear: str, #21: "HTML_BODY"):
        self.clear = clear
        
    @property
    def clear(self) -> str:
        return self.__clear

    @clear.setter
    def clear(self, clear: str):
        self.__clear = clear

class HTML_TABLEElement(BODYElement):

    def __init__(self, bgcolor: str, background: str, #21: "HTML_BODY"):
        self.bgcolor = bgcolor
        self.background = background
        
    @property
    def bgcolor(self) -> str:
        return self.__bgcolor

    @bgcolor.setter
    def bgcolor(self, bgcolor: str):
        self.__bgcolor = bgcolor

    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

class HTML_H1(BODYElement):

    pass
class HTML_PRE(BODYElement):

    pass
class HTML_STYLE(BODYElement):

    pass
class HTML:

    pass
class HEADElement:

    pass
class HTML_TITLE(HEADElement):

    pass
class HTML_LINK(HEADElement):

    def __init__(self, rel: str, title: str, ahref: str, type: str, #12: "HTML_HEAD"):
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
    def ahref(self) -> str:
        return self.__ahref

    @ahref.setter
    def ahref(self, ahref: str):
        self.__ahref = ahref

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

class HTMLElement:

    pass
class HTML_HEADElement(HTMLElement):

    pass
class HTML_HEAD(HTMLElement):

    pass
class HTML_BODY(HTMLElement):

    def __init__(self, background: str, bgcolor: str, text: str, link: str, alink: str, vlink: str, 120: set["BODYElement"] = None, 123: "HTML" = None, #6: "HTML_HTMLElement", #9: "HTML_HTMLElement"):
        self.background = background
        self.bgcolor = bgcolor
        self.text = text
        self.link = link
        self.alink = alink
        self.vlink = vlink
        self.120 = 120 if 120 is not None else set()
        self.123 = 123
        
    @property
    def alink(self) -> str:
        return self.__alink

    @alink.setter
    def alink(self, alink: str):
        self.__alink = alink

    @property
    def vlink(self) -> str:
        return self.__vlink

    @vlink.setter
    def vlink(self, vlink: str):
        self.__vlink = vlink

    @property
    def bgcolor(self) -> str:
        return self.__bgcolor

    @bgcolor.setter
    def bgcolor(self, bgcolor: str):
        self.__bgcolor = bgcolor

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

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
    def 120(self):
        return self.__120

    @120.setter
    def 120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_BODY__120", None)
        self.__120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#21"):
                    opp_val = getattr(item, "#21", None)
                    
                    if opp_val == self:
                        setattr(item, "#21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#21"):
                    opp_val = getattr(item, "#21", None)
                    
                    setattr(item, "#21", self)
                    

    @property
    def 123(self):
        return self.__123

    @123.setter
    def 123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_BODY__123", None)
        self.__123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#24"):
                opp_val = getattr(old_value, "#24", None)
                if opp_val == self:
                    setattr(old_value, "#24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#24"):
                opp_val = getattr(value, "#24", None)
                setattr(value, "#24", self)

class HTML_BODYElement(HTMLElement):

    pass
class HTML_HTMLElement:

    def __init__(self, value: str, 15: set["HTMLElement"] = None, 18: "HTMLElement" = None):
        self.value = value
        self.15 = 15 if 15 is not None else set()
        self.18 = 18
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def 18(self):
        return self.__18

    @18.setter
    def 18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_HTMLElement__18", None)
        self.__18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#9"):
                opp_val = getattr(old_value, "#9", None)
                if opp_val == self:
                    setattr(old_value, "#9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#9"):
                opp_val = getattr(value, "#9", None)
                setattr(value, "#9", self)

    @property
    def 15(self):
        return self.__15

    @15.setter
    def 15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HTML_HTMLElement__15", None)
        self.__15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#6"):
                    opp_val = getattr(item, "#6", None)
                    
                    if opp_val == self:
                        setattr(item, "#6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#6"):
                    opp_val = getattr(item, "#6", None)
                    
                    setattr(item, "#6", self)
                    

class BODY:

    pass
class HEAD:

    pass
class HTML_HTML:

    pass