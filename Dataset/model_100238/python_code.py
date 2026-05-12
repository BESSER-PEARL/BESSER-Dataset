from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Page:

    pass
class DatadiagramMLSimplified_PagesCollection:

    pass
class DatadiagramMLSimplified_MasterElt(ABC):

    pass
class ConnectsCollection:

    pass
class DatadiagramMLSimplified_Connect:

    def __init__(self, fromSheet: str, toSheet: str, fromCell: str, toCell: str, fromPart: str, toPart: str, connections: "ConnectsCollection" = None):
        self.fromSheet = fromSheet
        self.toSheet = toSheet
        self.fromCell = fromCell
        self.toCell = toCell
        self.fromPart = fromPart
        self.toPart = toPart
        self.connections = connections
        
        pass
    @property
    def toPart(self):
        return self.__toPart

    @toPart.setter
    def toPart(self, toPart: str):
        self.__toPart = toPart


    @property
    def toSheet(self):
        return self.__toSheet

    @toSheet.setter
    def toSheet(self, toSheet: str):
        self.__toSheet = toSheet


    @property
    def fromPart(self):
        return self.__fromPart

    @fromPart.setter
    def fromPart(self, fromPart: str):
        self.__fromPart = fromPart


    @property
    def fromCell(self):
        return self.__fromCell

    @fromCell.setter
    def fromCell(self, fromCell: str):
        self.__fromCell = fromCell


    @property
    def toCell(self):
        return self.__toCell

    @toCell.setter
    def toCell(self, toCell: str):
        self.__toCell = toCell


    @property
    def fromSheet(self):
        return self.__fromSheet

    @fromSheet.setter
    def fromSheet(self, fromSheet: str):
        self.__fromSheet = fromSheet


    @property
    def connections(self):
        return self.__connections

    @connections.setter
    def connections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLSimplified_Connect__connections", None)
        self.__connections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConnectsCollection"):
                opp_val = getattr(old_value, "ConnectsCollection", None)
                if opp_val == self:
                    setattr(old_value, "ConnectsCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConnectsCollection"):
                opp_val = getattr(value, "ConnectsCollection", None)
                setattr(value, "ConnectsCollection", self)

class Connect:

    pass
class NamedElt:

    pass
class IdentifiedElt:

    pass
class DatadiagramMLSimplified_Page(IdentifiedElt, NamedElt):

    def __init__(self, background: str, backPage: str, viewScale: str, viewCenterX: str, ViewCenterY: str, reviewerID: str, associatedPage: str, pages: "PagesCollection" = None, pe_page: set["PageElt"] = None):
        self.background = background
        self.backPage = backPage
        self.viewScale = viewScale
        self.viewCenterX = viewCenterX
        self.ViewCenterY = ViewCenterY
        self.reviewerID = reviewerID
        self.associatedPage = associatedPage
        self.pages = pages
        self.pe_page = pe_page if pe_page is not None else set()
        
        pass
    @property
    def backPage(self):
        return self.__backPage

    @backPage.setter
    def backPage(self, backPage: str):
        self.__backPage = backPage


    @property
    def viewScale(self):
        return self.__viewScale

    @viewScale.setter
    def viewScale(self, viewScale: str):
        self.__viewScale = viewScale


    @property
    def associatedPage(self):
        return self.__associatedPage

    @associatedPage.setter
    def associatedPage(self, associatedPage: str):
        self.__associatedPage = associatedPage


    @property
    def viewCenterX(self):
        return self.__viewCenterX

    @viewCenterX.setter
    def viewCenterX(self, viewCenterX: str):
        self.__viewCenterX = viewCenterX


    @property
    def reviewerID(self):
        return self.__reviewerID

    @reviewerID.setter
    def reviewerID(self, reviewerID: str):
        self.__reviewerID = reviewerID


    @property
    def ViewCenterY(self):
        return self.__ViewCenterY

    @ViewCenterY.setter
    def ViewCenterY(self, ViewCenterY: str):
        self.__ViewCenterY = ViewCenterY


    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLSimplified_Page__pages", None)
        self.__pages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagesCollection83"):
                opp_val = getattr(old_value, "PagesCollection83", None)
                if opp_val == self:
                    setattr(old_value, "PagesCollection83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagesCollection83"):
                opp_val = getattr(value, "PagesCollection83", None)
                setattr(value, "PagesCollection83", self)

    @property
    def pe_page(self):
        return self.__pe_page

    @pe_page.setter
    def pe_page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLSimplified_Page__pe_page", None)
        self.__pe_page = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PageElt"):
                    opp_val = getattr(item, "PageElt", None)
                    
                    if opp_val == self:
                        setattr(item, "PageElt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PageElt"):
                    opp_val = getattr(item, "PageElt", None)
                    
                    setattr(item, "PageElt", self)
                    

class DatadiagramMLSimplified_MasterShortCut(IdentifiedElt, NamedElt):

    def __init__(self, iconSize: str, patternFlags: str, prompt: str, shortcutURL: str, shortcutHelp: str, alignName: str, i_masterShortCut: set["Icon"] = None, masterShortCuts: "MastersCollection" = None):
        self.iconSize = iconSize
        self.patternFlags = patternFlags
        self.prompt = prompt
        self.shortcutURL = shortcutURL
        self.shortcutHelp = shortcutHelp
        self.alignName = alignName
        self.i_masterShortCut = i_masterShortCut if i_masterShortCut is not None else set()
        self.masterShortCuts = masterShortCuts
        
        pass
    @property
    def shortcutHelp(self):
        return self.__shortcutHelp

    @shortcutHelp.setter
    def shortcutHelp(self, shortcutHelp: str):
        self.__shortcutHelp = shortcutHelp


    @property
    def patternFlags(self):
        return self.__patternFlags

    @patternFlags.setter
    def patternFlags(self, patternFlags: str):
        self.__patternFlags = patternFlags


    @property
    def alignName(self):
        return self.__alignName

    @alignName.setter
    def alignName(self, alignName: str):
        self.__alignName = alignName


    @property
    def prompt(self):
        return self.__prompt

    @prompt.setter
    def prompt(self, prompt: str):
        self.__prompt = prompt


    @property
    def iconSize(self):
        return self.__iconSize

    @iconSize.setter
    def iconSize(self, iconSize: str):
        self.__iconSize = iconSize


    @property
    def shortcutURL(self):
        return self.__shortcutURL

    @shortcutURL.setter
    def shortcutURL(self, shortcutURL: str):
        self.__shortcutURL = shortcutURL


    @property
    def masterShortCuts(self):
        return self.__masterShortCuts

    @masterShortCuts.setter
    def masterShortCuts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLSimplified_MasterShortCut__masterShortCuts", None)
        self.__masterShortCuts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MastersCollection66"):
                opp_val = getattr(old_value, "MastersCollection66", None)
                if opp_val == self:
                    setattr(old_value, "MastersCollection66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MastersCollection66"):
                opp_val = getattr(value, "MastersCollection66", None)
                setattr(value, "MastersCollection66", self)

    @property
    def i_masterShortCut(self):
        return self.__i_masterShortCut

    @i_masterShortCut.setter
    def i_masterShortCut(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLSimplified_MasterShortCut__i_masterShortCut", None)
        self.__i_masterShortCut = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Icon"):
                    opp_val = getattr(item, "Icon", None)
                    
                    if opp_val == self:
                        setattr(item, "Icon", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Icon"):
                    opp_val = getattr(item, "Icon", None)
                    
                    setattr(item, "Icon", self)
                    

class MasterShortCut:

    pass
class Master:

    pass
class VisioDocument:

    pass
class DatadiagramMLSimplified_MastersCollection:

    pass
class Text:

    pass
class DatadiagramMLSimplified_TextElt(ABC):

    pass
class Icon:

    pass
class XYABCDElt:

    pass
class DatadiagramMLSimplified_Ellipse(XYABCDElt):

    pass
class XYABElt:

    pass
class DatadiagramMLSimplified_XYABCDElt(XYABElt):

    pass
class DatadiagramMLSimplified_InfiniteLine(XYABElt):

    pass
class TextElt:

    pass
class DatadiagramMLSimplified_StringElt(TextElt):

    def __init__(self, value: str, TextElt: "DatadiagramMLSimplified_Text" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class XYABCDEElt:

    pass
class DatadiagramMLSimplified_NURBSTo(XYABCDEElt):

    pass
class DatadiagramMLSimplified_XYABCDEElt(XYABCDElt):

    pass
class DatadiagramMLSimplified_SplineStart(XYABCDElt):

    pass
class DatadiagramMLSimplified_EllipticalArcTo(XYABCDElt):

    pass
class Geom:

    pass
class XYElt:

    pass
class DatadiagramMLSimplified_MoveTo(XYElt):

    pass
class DatadiagramMLSimplified_XYAElt(XYElt):

    pass
class DatadiagramMLSimplified_LineTo(XYElt):

    pass
class XYAElt:

    pass
class DatadiagramMLSimplified_SplineKnot(XYAElt):

    pass
class DatadiagramMLSimplified_XYABElt(XYAElt):

    pass
class DatadiagramMLSimplified_PolylineTo(XYAElt):

    pass
class DatadiagramMLSimplified_ArcTo(XYAElt):

    pass
class PolylineTo:

    pass
class SplineKnot:

    pass
class ArcTo:

    pass
class MoveTo:

    pass
class LineTo:

    pass
class NURBSTo:

    pass
class SplineStart:

    pass
class EllipticalArcTo:

    pass
class Ellipse:

    pass
class InfiniteLine:

    pass
class DatadiagramMLSimplified_ShapeElt(ABC):

    pass
class ShapeElt:

    pass
class DatadiagramMLSimplified_Text(ShapeElt):

    pass
class CellType:

    pass
class DelElt:

    pass
class IXElt:

    pass
class DatadiagramMLSimplified_XYElt(IXElt, DelElt):

    pass
class DatadiagramMLSimplified_Geom(ShapeElt, IXElt, DelElt):

    pass
class DatadiagramMLSimplified_DelElt(ABC):

    def __init__(self, del_: str):
        self.del_ = del_
        
        pass
    @property
    def del_(self):
        return self.__del_

    @del_.setter
    def del_(self, del_: str):
        self.__del_ = del_


class DatadiagramMLSimplified_IXElt(ABC):

    def __init__(self, iX: str):
        self.iX = iX
        
        pass
    @property
    def iX(self):
        return self.__iX

    @iX.setter
    def iX(self, iX: str):
        self.__iX = iX


class DatadiagramMLSimplified_IdentifiedElt(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
        pass
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


class DatadiagramMLSimplified_NamedElt(ABC):

    def __init__(self, name: str, nameU: str):
        self.name = name
        self.nameU = nameU
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def nameU(self):
        return self.__nameU

    @nameU.setter
    def nameU(self, nameU: str):
        self.__nameU = nameU


class PageElt:

    pass
class MasterElt:

    pass
class DatadiagramMLSimplified_ShapesCollection(PageElt, MasterElt):

    pass
class DatadiagramMLSimplified_Icon(MasterElt):

    def __init__(self, value: str, icons: "MasterShortCut" = None, MasterElt: "DatadiagramMLSimplified_Master" = None):
        self.value = value
        self.icons = icons
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def icons(self):
        return self.__icons

    @icons.setter
    def icons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLSimplified_Icon__icons", None)
        self.__icons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MasterShortCut69"):
                opp_val = getattr(old_value, "MasterShortCut69", None)
                if opp_val == self:
                    setattr(old_value, "MasterShortCut69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MasterShortCut69"):
                opp_val = getattr(value, "MasterShortCut69", None)
                setattr(value, "MasterShortCut69", self)

class UniqueIdElt:

    pass
class DatadiagramMLSimplified_Master(UniqueIdElt, IdentifiedElt, NamedElt):

    def __init__(self, baseID: str, matchByName: str, iconSize: str, patternFlags: str, prompt: str, hidden: str, iconUpdate: str, alignName: str, masters: "MastersCollection" = None, me_master: set["MasterElt"] = None):
        self.baseID = baseID
        self.matchByName = matchByName
        self.iconSize = iconSize
        self.patternFlags = patternFlags
        self.prompt = prompt
        self.hidden = hidden
        self.iconUpdate = iconUpdate
        self.alignName = alignName
        self.masters = masters
        self.me_master = me_master if me_master is not None else set()
        
        pass
    @property
    def matchByName(self):
        return self.__matchByName

    @matchByName.setter
    def matchByName(self, matchByName: str):
        self.__matchByName = matchByName


    @property
    def iconSize(self):
        return self.__iconSize

    @iconSize.setter
    def iconSize(self, iconSize: str):
        self.__iconSize = iconSize


    @property
    def alignName(self):
        return self.__alignName

    @alignName.setter
    def alignName(self, alignName: str):
        self.__alignName = alignName


    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: str):
        self.__hidden = hidden


    @property
    def iconUpdate(self):
        return self.__iconUpdate

    @iconUpdate.setter
    def iconUpdate(self, iconUpdate: str):
        self.__iconUpdate = iconUpdate


    @property
    def prompt(self):
        return self.__prompt

    @prompt.setter
    def prompt(self, prompt: str):
        self.__prompt = prompt


    @property
    def patternFlags(self):
        return self.__patternFlags

    @patternFlags.setter
    def patternFlags(self, patternFlags: str):
        self.__patternFlags = patternFlags


    @property
    def baseID(self):
        return self.__baseID

    @baseID.setter
    def baseID(self, baseID: str):
        self.__baseID = baseID


    @property
    def me_master(self):
        return self.__me_master

    @me_master.setter
    def me_master(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLSimplified_Master__me_master", None)
        self.__me_master = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MasterElt"):
                    opp_val = getattr(item, "MasterElt", None)
                    
                    if opp_val == self:
                        setattr(item, "MasterElt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MasterElt"):
                    opp_val = getattr(item, "MasterElt", None)
                    
                    setattr(item, "MasterElt", self)
                    

    @property
    def masters(self):
        return self.__masters

    @masters.setter
    def masters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLSimplified_Master__masters", None)
        self.__masters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MastersCollection71"):
                opp_val = getattr(old_value, "MastersCollection71", None)
                if opp_val == self:
                    setattr(old_value, "MastersCollection71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MastersCollection71"):
                opp_val = getattr(value, "MastersCollection71", None)
                setattr(value, "MastersCollection71", self)

class Shape:

    pass
class DatadiagramMLSimplified_PageSheet(UniqueIdElt, MasterElt, PageElt, Shape):

    pass
class ShapesCollection:

    pass
class DatadiagramMLSimplified_Shape:

    def __init__(self, lineStyle: str, fillStyle: str, textStyle: str, shapes: "ShapesCollection" = None, sse_shapeSheet: set["ShapeElt"] = None):
        self.lineStyle = lineStyle
        self.fillStyle = fillStyle
        self.textStyle = textStyle
        self.shapes = shapes
        self.sse_shapeSheet = sse_shapeSheet if sse_shapeSheet is not None else set()
        
        pass
    @property
    def textStyle(self):
        return self.__textStyle

    @textStyle.setter
    def textStyle(self, textStyle: str):
        self.__textStyle = textStyle


    @property
    def lineStyle(self):
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle


    @property
    def fillStyle(self):
        return self.__fillStyle

    @fillStyle.setter
    def fillStyle(self, fillStyle: str):
        self.__fillStyle = fillStyle


    @property
    def sse_shapeSheet(self):
        return self.__sse_shapeSheet

    @sse_shapeSheet.setter
    def sse_shapeSheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLSimplified_Shape__sse_shapeSheet", None)
        self.__sse_shapeSheet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ShapeElt"):
                    opp_val = getattr(item, "ShapeElt", None)
                    
                    if opp_val == self:
                        setattr(item, "ShapeElt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ShapeElt"):
                    opp_val = getattr(item, "ShapeElt", None)
                    
                    setattr(item, "ShapeElt", self)
                    

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLSimplified_Shape__shapes", None)
        self.__shapes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShapesCollection"):
                opp_val = getattr(old_value, "ShapesCollection", None)
                if opp_val == self:
                    setattr(old_value, "ShapesCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShapesCollection"):
                opp_val = getattr(value, "ShapesCollection", None)
                setattr(value, "ShapesCollection", self)

class DatadiagramMLSimplified_UniqueIdElt(ABC):

    def __init__(self, UniqueID: str):
        self.UniqueID = UniqueID
        
        pass
    @property
    def UniqueID(self):
        return self.__UniqueID

    @UniqueID.setter
    def UniqueID(self, UniqueID: str):
        self.__UniqueID = UniqueID


class PagesCollection:

    pass
class MastersCollection:

    pass
class DatadiagramMLSimplified_VisioDocument:

    pass
class DatadiagramMLSimplified_CellType:

    def __init__(self, unit: str, formula: str, err: str, value: str):
        self.unit = unit
        self.formula = formula
        self.err = err
        self.value = value
        
        pass
    @property
    def err(self):
        return self.__err

    @err.setter
    def err(self, err: str):
        self.__err = err


    @property
    def formula(self):
        return self.__formula

    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


class DatadiagramMLSimplified_PageElt(ABC):

    pass
class DatadiagramMLSimplified_ConnectsCollection(PageElt, MasterElt):

    pass