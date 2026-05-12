from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DatadiagramMLBasicDef_HeaderFooter:

    pass
class DatadiagramMLBasicDef_EventList:

    pass
class DatadiagramMLBasicDef_WindowsInfo:

    pass
class DatadiagramMLBasicDef_FaceNamesTable:

    pass
class DatadiagramMLBasicDef_FontsTable:

    pass
class DatadiagramMLBasicDef_PrintSetup:

    pass
class DatadiagramMLBasicDef_SolutionXML:

    pass
class Page:

    pass
class DatadiagramMLBasicDef_ColorsTable:

    pass
class DatadiagramMLBasicDef_DocumentSettingsElt:

    pass
class DatadiagramMLBasicDef_PageElt(ABC):

    pass
class ConnectsCollection:

    pass
class DatadiagramMLBasicDef_Connect:

    def __init__(self, fromCell: str, toCell: str, fromPart: str, toPart: str, fromSheet: str, toSheet: str, connections: "ConnectsCollection" = None):
        self.fromCell = fromCell
        self.toCell = toCell
        self.fromPart = fromPart
        self.toPart = toPart
        self.fromSheet = fromSheet
        self.toSheet = toSheet
        self.connections = connections
        
        pass
    @property
    def fromCell(self):
        return self.__fromCell

    @fromCell.setter
    def fromCell(self, fromCell: str):
        self.__fromCell = fromCell


    @property
    def toPart(self):
        return self.__toPart

    @toPart.setter
    def toPart(self, toPart: str):
        self.__toPart = toPart


    @property
    def fromPart(self):
        return self.__fromPart

    @fromPart.setter
    def fromPart(self, fromPart: str):
        self.__fromPart = fromPart


    @property
    def fromSheet(self):
        return self.__fromSheet

    @fromSheet.setter
    def fromSheet(self, fromSheet: str):
        self.__fromSheet = fromSheet


    @property
    def toSheet(self):
        return self.__toSheet

    @toSheet.setter
    def toSheet(self, toSheet: str):
        self.__toSheet = toSheet


    @property
    def toCell(self):
        return self.__toCell

    @toCell.setter
    def toCell(self, toCell: str):
        self.__toCell = toCell


    @property
    def connections(self):
        return self.__connections

    @connections.setter
    def connections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_Connect__connections", None)
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
class DatadiagramMLBasicDef_PagesCollection:

    pass
class DatadiagramMLBasicDef_MasterElt(ABC):

    pass
class Icon:

    pass
class DatadiagramMLBasicDef_MastersCollection:

    pass
class Text:

    pass
class DatadiagramMLBasicDef_TextElt(ABC):

    pass
class MasterShortCut:

    pass
class Master:

    pass
class XYABCDElt:

    pass
class DatadiagramMLBasicDef_EllipticalArcTo(XYABCDElt):

    pass
class DatadiagramMLBasicDef_SplineStart(XYABCDElt):

    pass
class DatadiagramMLBasicDef_Ellipse(XYABCDElt):

    pass
class TextElt:

    pass
class DatadiagramMLBasicDef_StringElt(TextElt):

    def __init__(self, value: str, TextElt: "DatadiagramMLBasicDef_Text" = None):
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
class DatadiagramMLBasicDef_NURBSTo(XYABCDEElt):

    pass
class DatadiagramMLBasicDef_XYABCDEElt(XYABCDElt):

    pass
class XYAElt:

    pass
class DatadiagramMLBasicDef_SplineKnot(XYAElt):

    pass
class DatadiagramMLBasicDef_PolylineTo(XYAElt):

    pass
class DatadiagramMLBasicDef_ArcTo(XYAElt):

    pass
class XYABElt:

    pass
class DatadiagramMLBasicDef_XYABCDElt(XYABElt):

    pass
class DatadiagramMLBasicDef_InfiniteLine(XYABElt):

    pass
class DatadiagramMLBasicDef_XYABElt(XYAElt):

    pass
class NURBSTo:

    pass
class SplineStart:

    pass
class EllipticalArcTo:

    pass
class Ellipse:

    pass
class Geom:

    pass
class XYElt:

    pass
class DatadiagramMLBasicDef_MoveTo(XYElt):

    pass
class DatadiagramMLBasicDef_XYAElt(XYElt):

    pass
class DatadiagramMLBasicDef_LineTo(XYElt):

    pass
class LineTo:

    pass
class CellType:

    pass
class DelElt:

    pass
class IXElt:

    pass
class DatadiagramMLBasicDef_XYElt(DelElt, IXElt):

    pass
class DatadiagramMLBasicDef_DelElt(ABC):

    def __init__(self, del_: str):
        self.del_ = del_
        
        pass
    @property
    def del_(self):
        return self.__del_

    @del_.setter
    def del_(self, del_: str):
        self.__del_ = del_


class DatadiagramMLBasicDef_IXElt(ABC):

    def __init__(self, iX: str):
        self.iX = iX
        
        pass
    @property
    def iX(self):
        return self.__iX

    @iX.setter
    def iX(self, iX: str):
        self.__iX = iX


class InfiniteLine:

    pass
class PolylineTo:

    pass
class SplineKnot:

    pass
class ArcTo:

    pass
class MoveTo:

    pass
class DatadiagramMLBasicDef_UniqueIdElt(ABC):

    def __init__(self, UniqueID: str):
        self.UniqueID = UniqueID
        
        pass
    @property
    def UniqueID(self):
        return self.__UniqueID

    @UniqueID.setter
    def UniqueID(self, UniqueID: str):
        self.__UniqueID = UniqueID


class DatadiagramMLBasicDef_IdentifiedElt(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
        pass
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


class DatadiagramMLBasicDef_NamedElt(ABC):

    def __init__(self, name: str, nameU: str):
        self.name = name
        self.nameU = nameU
        
        pass
    @property
    def nameU(self):
        return self.__nameU

    @nameU.setter
    def nameU(self, nameU: str):
        self.__nameU = nameU


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class PageElt:

    pass
class MasterElt:

    pass
class DatadiagramMLBasicDef_ConnectsCollection(PageElt, MasterElt):

    pass
class DatadiagramMLBasicDef_Icon(MasterElt):

    def __init__(self, value: str, icons: "MasterShortCut" = None, MasterElt: "DatadiagramMLBasicDef_Master" = None):
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
        old_value = getattr(self, f"_DatadiagramMLBasicDef_Icon__icons", None)
        self.__icons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MasterShortCut113"):
                opp_val = getattr(old_value, "MasterShortCut113", None)
                if opp_val == self:
                    setattr(old_value, "MasterShortCut113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MasterShortCut113"):
                opp_val = getattr(value, "MasterShortCut113", None)
                setattr(value, "MasterShortCut113", self)

class DatadiagramMLBasicDef_ShapesCollection(PageElt, MasterElt):

    pass
class UniqueIdElt:

    pass
class PageSheet:

    pass
class NamedElt:

    pass
class DatadiagramMLBasicDef_DocumentSheet(NamedElt, PageSheet):

    pass
class DatadiagramMLBasicDef_ShapeElt(ABC):

    pass
class ShapeElt:

    pass
class DatadiagramMLBasicDef_Text(ShapeElt):

    pass
class DatadiagramMLBasicDef_Geom(DelElt, ShapeElt, IXElt):

    pass
class ShapesCollection:

    pass
class DatadiagramMLBasicDef_Shape:

    def __init__(self, lineStyle: str, fillStyle: str, textStyle: str, shapes: "ShapesCollection" = None, sse_shapeSheet: set["ShapeElt"] = None):
        self.lineStyle = lineStyle
        self.fillStyle = fillStyle
        self.textStyle = textStyle
        self.shapes = shapes
        self.sse_shapeSheet = sse_shapeSheet if sse_shapeSheet is not None else set()
        
        pass
    @property
    def lineStyle(self):
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle


    @property
    def textStyle(self):
        return self.__textStyle

    @textStyle.setter
    def textStyle(self, textStyle: str):
        self.__textStyle = textStyle


    @property
    def fillStyle(self):
        return self.__fillStyle

    @fillStyle.setter
    def fillStyle(self, fillStyle: str):
        self.__fillStyle = fillStyle


    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_Shape__shapes", None)
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

    @property
    def sse_shapeSheet(self):
        return self.__sse_shapeSheet

    @sse_shapeSheet.setter
    def sse_shapeSheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_Shape__sse_shapeSheet", None)
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
                    

class DatadiagramMLBasicDef_EmailRoutingData:

    def __init__(self, data: str, size: str, docEmailRoutingData: "VisioDocument" = None):
        self.data = data
        self.size = size
        self.docEmailRoutingData = docEmailRoutingData
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


    @property
    def docEmailRoutingData(self):
        return self.__docEmailRoutingData

    @docEmailRoutingData.setter
    def docEmailRoutingData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_EmailRoutingData__docEmailRoutingData", None)
        self.__docEmailRoutingData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisioDocument37"):
                opp_val = getattr(old_value, "VisioDocument37", None)
                if opp_val == self:
                    setattr(old_value, "VisioDocument37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisioDocument37"):
                opp_val = getattr(value, "VisioDocument37", None)
                setattr(value, "VisioDocument37", self)

class DatadiagramMLBasicDef_VBProjectData:

    def __init__(self, data: str, docVBProjectData: "VisioDocument" = None):
        self.data = data
        self.docVBProjectData = docVBProjectData
        
        pass
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


    @property
    def docVBProjectData(self):
        return self.__docVBProjectData

    @docVBProjectData.setter
    def docVBProjectData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VBProjectData__docVBProjectData", None)
        self.__docVBProjectData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisioDocument35"):
                opp_val = getattr(old_value, "VisioDocument35", None)
                if opp_val == self:
                    setattr(old_value, "VisioDocument35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisioDocument35"):
                opp_val = getattr(value, "VisioDocument35", None)
                setattr(value, "VisioDocument35", self)

class DatadiagramMLBasicDef_CustomProperty:

    def __init__(self, name: str, dataType: str, cps_customProps: "CustomPropertiesCollection" = None):
        self.name = name
        self.dataType = dataType
        self.cps_customProps = cps_customProps
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def dataType(self):
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType


    @property
    def cps_customProps(self):
        return self.__cps_customProps

    @cps_customProps.setter
    def cps_customProps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_CustomProperty__cps_customProps", None)
        self.__cps_customProps = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CustomPropertiesCollection33"):
                opp_val = getattr(old_value, "CustomPropertiesCollection33", None)
                if opp_val == self:
                    setattr(old_value, "CustomPropertiesCollection33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CustomPropertiesCollection33"):
                opp_val = getattr(value, "CustomPropertiesCollection33", None)
                setattr(value, "CustomPropertiesCollection33", self)

class CustomProperty:

    pass
class DatadiagramMLBasicDef_CustomPropertiesCollection:

    pass
class IdentifiedElt:

    pass
class DatadiagramMLBasicDef_Page(NamedElt, IdentifiedElt):

    def __init__(self, background: str, backPage: str, viewScale: str, viewCenterX: str, ViewCenterY: str, reviewerID: str, associatedPage: str, pe_page: set["PageElt"] = None, pages: "PagesCollection" = None):
        self.background = background
        self.backPage = backPage
        self.viewScale = viewScale
        self.viewCenterX = viewCenterX
        self.ViewCenterY = ViewCenterY
        self.reviewerID = reviewerID
        self.associatedPage = associatedPage
        self.pe_page = pe_page if pe_page is not None else set()
        self.pages = pages
        
        pass
    @property
    def associatedPage(self):
        return self.__associatedPage

    @associatedPage.setter
    def associatedPage(self, associatedPage: str):
        self.__associatedPage = associatedPage


    @property
    def backPage(self):
        return self.__backPage

    @backPage.setter
    def backPage(self, backPage: str):
        self.__backPage = backPage


    @property
    def reviewerID(self):
        return self.__reviewerID

    @reviewerID.setter
    def reviewerID(self, reviewerID: str):
        self.__reviewerID = reviewerID


    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background


    @property
    def viewScale(self):
        return self.__viewScale

    @viewScale.setter
    def viewScale(self, viewScale: str):
        self.__viewScale = viewScale


    @property
    def viewCenterX(self):
        return self.__viewCenterX

    @viewCenterX.setter
    def viewCenterX(self, viewCenterX: str):
        self.__viewCenterX = viewCenterX


    @property
    def ViewCenterY(self):
        return self.__ViewCenterY

    @ViewCenterY.setter
    def ViewCenterY(self, ViewCenterY: str):
        self.__ViewCenterY = ViewCenterY


    @property
    def pe_page(self):
        return self.__pe_page

    @pe_page.setter
    def pe_page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_Page__pe_page", None)
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
                    

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_Page__pages", None)
        self.__pages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagesCollection127"):
                opp_val = getattr(old_value, "PagesCollection127", None)
                if opp_val == self:
                    setattr(old_value, "PagesCollection127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagesCollection127"):
                opp_val = getattr(value, "PagesCollection127", None)
                setattr(value, "PagesCollection127", self)

class DatadiagramMLBasicDef_Master(NamedElt, UniqueIdElt, IdentifiedElt):

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
    def baseID(self):
        return self.__baseID

    @baseID.setter
    def baseID(self, baseID: str):
        self.__baseID = baseID


    @property
    def iconSize(self):
        return self.__iconSize

    @iconSize.setter
    def iconSize(self, iconSize: str):
        self.__iconSize = iconSize


    @property
    def matchByName(self):
        return self.__matchByName

    @matchByName.setter
    def matchByName(self, matchByName: str):
        self.__matchByName = matchByName


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
    def me_master(self):
        return self.__me_master

    @me_master.setter
    def me_master(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_Master__me_master", None)
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
        old_value = getattr(self, f"_DatadiagramMLBasicDef_Master__masters", None)
        self.__masters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MastersCollection115"):
                opp_val = getattr(old_value, "MastersCollection115", None)
                if opp_val == self:
                    setattr(old_value, "MastersCollection115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MastersCollection115"):
                opp_val = getattr(value, "MastersCollection115", None)
                setattr(value, "MastersCollection115", self)

class DatadiagramMLBasicDef_MasterShortCut(NamedElt, IdentifiedElt):

    def __init__(self, iconSize: str, patternFlags: str, prompt: str, shortcutURL: str, shortcutHelp: str, alignName: str, masterShortCuts: "MastersCollection" = None, i_masterShortCut: set["Icon"] = None):
        self.iconSize = iconSize
        self.patternFlags = patternFlags
        self.prompt = prompt
        self.shortcutURL = shortcutURL
        self.shortcutHelp = shortcutHelp
        self.alignName = alignName
        self.masterShortCuts = masterShortCuts
        self.i_masterShortCut = i_masterShortCut if i_masterShortCut is not None else set()
        
        pass
    @property
    def prompt(self):
        return self.__prompt

    @prompt.setter
    def prompt(self, prompt: str):
        self.__prompt = prompt


    @property
    def alignName(self):
        return self.__alignName

    @alignName.setter
    def alignName(self, alignName: str):
        self.__alignName = alignName


    @property
    def shortcutURL(self):
        return self.__shortcutURL

    @shortcutURL.setter
    def shortcutURL(self, shortcutURL: str):
        self.__shortcutURL = shortcutURL


    @property
    def shortcutHelp(self):
        return self.__shortcutHelp

    @shortcutHelp.setter
    def shortcutHelp(self, shortcutHelp: str):
        self.__shortcutHelp = shortcutHelp


    @property
    def iconSize(self):
        return self.__iconSize

    @iconSize.setter
    def iconSize(self, iconSize: str):
        self.__iconSize = iconSize


    @property
    def patternFlags(self):
        return self.__patternFlags

    @patternFlags.setter
    def patternFlags(self, patternFlags: str):
        self.__patternFlags = patternFlags


    @property
    def i_masterShortCut(self):
        return self.__i_masterShortCut

    @i_masterShortCut.setter
    def i_masterShortCut(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_MasterShortCut__i_masterShortCut", None)
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
                    

    @property
    def masterShortCuts(self):
        return self.__masterShortCuts

    @masterShortCuts.setter
    def masterShortCuts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_MasterShortCut__masterShortCuts", None)
        self.__masterShortCuts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MastersCollection110"):
                opp_val = getattr(old_value, "MastersCollection110", None)
                if opp_val == self:
                    setattr(old_value, "MastersCollection110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MastersCollection110"):
                opp_val = getattr(value, "MastersCollection110", None)
                setattr(value, "MastersCollection110", self)

class Shape:

    pass
class DatadiagramMLBasicDef_PageSheet(PageElt, Shape, UniqueIdElt, MasterElt):

    pass
class DatadiagramMLBasicDef_StyleSheet(NamedElt, Shape, IdentifiedElt):

    pass
class StyleSheet:

    pass
class DatadiagramMLBasicDef_StyleSheetsCollection:

    pass
class VisioDocument:

    pass
class DatadiagramMLBasicDef_DocumentPropertiesCollection:

    def __init__(self, buildNumberEdited: str, title: str, subject: str, creator: str, manager: str, company: str, category: str, keywords: str, description: str, hyperlinkBase_href: str, alternateNames: str, template: str, buildNumberCreated: str, cps_docProp: "CustomPropertiesCollection" = None, DatadiagramMLBasicDef_DocumentPropertiesCollection: "DateTimeType" = None, DatadiagramMLBasicDef_DocumentPropertiesCollection21: "DateTimeType" = None, DatadiagramMLBasicDef_DocumentPropertiesCollection24: "DateTimeType" = None, docProps: "VisioDocument" = None, DatadiagramMLBasicDef_DocumentPropertiesCollection27: "DateTimeType" = None):
        self.buildNumberEdited = buildNumberEdited
        self.title = title
        self.subject = subject
        self.creator = creator
        self.manager = manager
        self.company = company
        self.category = category
        self.keywords = keywords
        self.description = description
        self.hyperlinkBase_href = hyperlinkBase_href
        self.alternateNames = alternateNames
        self.template = template
        self.buildNumberCreated = buildNumberCreated
        self.cps_docProp = cps_docProp
        self.DatadiagramMLBasicDef_DocumentPropertiesCollection = DatadiagramMLBasicDef_DocumentPropertiesCollection
        self.DatadiagramMLBasicDef_DocumentPropertiesCollection21 = DatadiagramMLBasicDef_DocumentPropertiesCollection21
        self.DatadiagramMLBasicDef_DocumentPropertiesCollection24 = DatadiagramMLBasicDef_DocumentPropertiesCollection24
        self.docProps = docProps
        self.DatadiagramMLBasicDef_DocumentPropertiesCollection27 = DatadiagramMLBasicDef_DocumentPropertiesCollection27
        
        pass
    @property
    def creator(self):
        return self.__creator

    @creator.setter
    def creator(self, creator: str):
        self.__creator = creator


    @property
    def buildNumberCreated(self):
        return self.__buildNumberCreated

    @buildNumberCreated.setter
    def buildNumberCreated(self, buildNumberCreated: str):
        self.__buildNumberCreated = buildNumberCreated


    @property
    def buildNumberEdited(self):
        return self.__buildNumberEdited

    @buildNumberEdited.setter
    def buildNumberEdited(self, buildNumberEdited: str):
        self.__buildNumberEdited = buildNumberEdited


    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template


    @property
    def hyperlinkBase_href(self):
        return self.__hyperlinkBase_href

    @hyperlinkBase_href.setter
    def hyperlinkBase_href(self, hyperlinkBase_href: str):
        self.__hyperlinkBase_href = hyperlinkBase_href


    @property
    def alternateNames(self):
        return self.__alternateNames

    @alternateNames.setter
    def alternateNames(self, alternateNames: str):
        self.__alternateNames = alternateNames


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords


    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager: str):
        self.__manager = manager


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject


    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company: str):
        self.__company = company


    @property
    def docProps(self):
        return self.__docProps

    @docProps.setter
    def docProps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_DocumentPropertiesCollection__docProps", None)
        self.__docProps = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisioDocument"):
                opp_val = getattr(old_value, "VisioDocument", None)
                if opp_val == self:
                    setattr(old_value, "VisioDocument", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisioDocument"):
                opp_val = getattr(value, "VisioDocument", None)
                setattr(value, "VisioDocument", self)

    @property
    def DatadiagramMLBasicDef_DocumentPropertiesCollection21(self):
        return self.__DatadiagramMLBasicDef_DocumentPropertiesCollection21

    @DatadiagramMLBasicDef_DocumentPropertiesCollection21.setter
    def DatadiagramMLBasicDef_DocumentPropertiesCollection21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_DocumentPropertiesCollection__DatadiagramMLBasicDef_DocumentPropertiesCollection21", None)
        self.__DatadiagramMLBasicDef_DocumentPropertiesCollection21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DateTimeType22"):
                opp_val = getattr(old_value, "DateTimeType22", None)
                if opp_val == self:
                    setattr(old_value, "DateTimeType22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DateTimeType22"):
                opp_val = getattr(value, "DateTimeType22", None)
                setattr(value, "DateTimeType22", self)

    @property
    def DatadiagramMLBasicDef_DocumentPropertiesCollection27(self):
        return self.__DatadiagramMLBasicDef_DocumentPropertiesCollection27

    @DatadiagramMLBasicDef_DocumentPropertiesCollection27.setter
    def DatadiagramMLBasicDef_DocumentPropertiesCollection27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_DocumentPropertiesCollection__DatadiagramMLBasicDef_DocumentPropertiesCollection27", None)
        self.__DatadiagramMLBasicDef_DocumentPropertiesCollection27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DateTimeType28"):
                opp_val = getattr(old_value, "DateTimeType28", None)
                if opp_val == self:
                    setattr(old_value, "DateTimeType28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DateTimeType28"):
                opp_val = getattr(value, "DateTimeType28", None)
                setattr(value, "DateTimeType28", self)

    @property
    def cps_docProp(self):
        return self.__cps_docProp

    @cps_docProp.setter
    def cps_docProp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_DocumentPropertiesCollection__cps_docProp", None)
        self.__cps_docProp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CustomPropertiesCollection"):
                opp_val = getattr(old_value, "CustomPropertiesCollection", None)
                if opp_val == self:
                    setattr(old_value, "CustomPropertiesCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CustomPropertiesCollection"):
                opp_val = getattr(value, "CustomPropertiesCollection", None)
                setattr(value, "CustomPropertiesCollection", self)

    @property
    def DatadiagramMLBasicDef_DocumentPropertiesCollection(self):
        return self.__DatadiagramMLBasicDef_DocumentPropertiesCollection

    @DatadiagramMLBasicDef_DocumentPropertiesCollection.setter
    def DatadiagramMLBasicDef_DocumentPropertiesCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_DocumentPropertiesCollection__DatadiagramMLBasicDef_DocumentPropertiesCollection", None)
        self.__DatadiagramMLBasicDef_DocumentPropertiesCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DateTimeType"):
                opp_val = getattr(old_value, "DateTimeType", None)
                if opp_val == self:
                    setattr(old_value, "DateTimeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DateTimeType"):
                opp_val = getattr(value, "DateTimeType", None)
                setattr(value, "DateTimeType", self)

    @property
    def DatadiagramMLBasicDef_DocumentPropertiesCollection24(self):
        return self.__DatadiagramMLBasicDef_DocumentPropertiesCollection24

    @DatadiagramMLBasicDef_DocumentPropertiesCollection24.setter
    def DatadiagramMLBasicDef_DocumentPropertiesCollection24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_DocumentPropertiesCollection__DatadiagramMLBasicDef_DocumentPropertiesCollection24", None)
        self.__DatadiagramMLBasicDef_DocumentPropertiesCollection24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DateTimeType25"):
                opp_val = getattr(old_value, "DateTimeType25", None)
                if opp_val == self:
                    setattr(old_value, "DateTimeType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DateTimeType25"):
                opp_val = getattr(value, "DateTimeType25", None)
                setattr(value, "DateTimeType25", self)

class DateTimeType:

    pass
class CustomPropertiesCollection:

    pass
class MastersCollection:

    pass
class DocumentSheet:

    pass
class StyleSheetsCollection:

    pass
class FaceNamesTable:

    pass
class FontsTable:

    pass
class PrintSetup:

    pass
class ColorsTable:

    pass
class DocumentSettingsElt:

    pass
class DocumentPropertiesCollection:

    pass
class SolutionXML:

    pass
class EmailRoutingData:

    pass
class VBProjectData:

    pass
class HeaderFooter:

    pass
class EventList:

    pass
class WindowsInfo:

    pass
class PagesCollection:

    pass
class DatadiagramMLBasicDef_DateTimeType:

    def __init__(self, month: str, day: str, hour: str, minute: str, second: str, year: str):
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.year = year
        
        pass
    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: str):
        self.__hour = hour


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute: str):
        self.__minute = minute


    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: str):
        self.__second = second


class DatadiagramMLBasicDef_VisioDocument:

    def __init__(self, start: str, key: str, metric: str, buildnum: str, version: str, docLangId: str, ps_visioDocument10: "PagesCollection" = None, el_visioDocument: "EventList" = None, ef_visioDocument: "HeaderFooter" = None, vpd_visioDocument: "VBProjectData" = None, erd_visioDocument: "EmailRoutingData" = None, sx_visioDocument: set["SolutionXML"] = None, dps_visioDocument: "DocumentPropertiesCollection" = None, dss_visioDocument: "DocumentSettingsElt" = None, cs_visioDocument: "ColorsTable" = None, ps_visioDocument: "PrintSetup" = None, fs_visioDocument: "FontsTable" = None, fns_visioDocument: "FaceNamesTable" = None, sss_visioDocument: "StyleSheetsCollection" = None, ds_visioDocument: "DocumentSheet" = None, ms_visioDocument: "MastersCollection" = None, ws_visioDocument: "WindowsInfo" = None):
        self.start = start
        self.key = key
        self.metric = metric
        self.buildnum = buildnum
        self.version = version
        self.docLangId = docLangId
        self.ps_visioDocument10 = ps_visioDocument10
        self.el_visioDocument = el_visioDocument
        self.ef_visioDocument = ef_visioDocument
        self.vpd_visioDocument = vpd_visioDocument
        self.erd_visioDocument = erd_visioDocument
        self.sx_visioDocument = sx_visioDocument if sx_visioDocument is not None else set()
        self.dps_visioDocument = dps_visioDocument
        self.dss_visioDocument = dss_visioDocument
        self.cs_visioDocument = cs_visioDocument
        self.ps_visioDocument = ps_visioDocument
        self.fs_visioDocument = fs_visioDocument
        self.fns_visioDocument = fns_visioDocument
        self.sss_visioDocument = sss_visioDocument
        self.ds_visioDocument = ds_visioDocument
        self.ms_visioDocument = ms_visioDocument
        self.ws_visioDocument = ws_visioDocument
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def metric(self):
        return self.__metric

    @metric.setter
    def metric(self, metric: str):
        self.__metric = metric


    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start


    @property
    def buildnum(self):
        return self.__buildnum

    @buildnum.setter
    def buildnum(self, buildnum: str):
        self.__buildnum = buildnum


    @property
    def docLangId(self):
        return self.__docLangId

    @docLangId.setter
    def docLangId(self, docLangId: str):
        self.__docLangId = docLangId


    @property
    def dss_visioDocument(self):
        return self.__dss_visioDocument

    @dss_visioDocument.setter
    def dss_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__dss_visioDocument", None)
        self.__dss_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DocumentSettingsElt"):
                opp_val = getattr(old_value, "DocumentSettingsElt", None)
                if opp_val == self:
                    setattr(old_value, "DocumentSettingsElt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DocumentSettingsElt"):
                opp_val = getattr(value, "DocumentSettingsElt", None)
                setattr(value, "DocumentSettingsElt", self)

    @property
    def ms_visioDocument(self):
        return self.__ms_visioDocument

    @ms_visioDocument.setter
    def ms_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__ms_visioDocument", None)
        self.__ms_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MastersCollection"):
                opp_val = getattr(old_value, "MastersCollection", None)
                if opp_val == self:
                    setattr(old_value, "MastersCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MastersCollection"):
                opp_val = getattr(value, "MastersCollection", None)
                setattr(value, "MastersCollection", self)

    @property
    def ws_visioDocument(self):
        return self.__ws_visioDocument

    @ws_visioDocument.setter
    def ws_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__ws_visioDocument", None)
        self.__ws_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WindowsInfo"):
                opp_val = getattr(old_value, "WindowsInfo", None)
                if opp_val == self:
                    setattr(old_value, "WindowsInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WindowsInfo"):
                opp_val = getattr(value, "WindowsInfo", None)
                setattr(value, "WindowsInfo", self)

    @property
    def ps_visioDocument(self):
        return self.__ps_visioDocument

    @ps_visioDocument.setter
    def ps_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__ps_visioDocument", None)
        self.__ps_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrintSetup"):
                opp_val = getattr(old_value, "PrintSetup", None)
                if opp_val == self:
                    setattr(old_value, "PrintSetup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrintSetup"):
                opp_val = getattr(value, "PrintSetup", None)
                setattr(value, "PrintSetup", self)

    @property
    def vpd_visioDocument(self):
        return self.__vpd_visioDocument

    @vpd_visioDocument.setter
    def vpd_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__vpd_visioDocument", None)
        self.__vpd_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VBProjectData"):
                opp_val = getattr(old_value, "VBProjectData", None)
                if opp_val == self:
                    setattr(old_value, "VBProjectData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VBProjectData"):
                opp_val = getattr(value, "VBProjectData", None)
                setattr(value, "VBProjectData", self)

    @property
    def ef_visioDocument(self):
        return self.__ef_visioDocument

    @ef_visioDocument.setter
    def ef_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__ef_visioDocument", None)
        self.__ef_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HeaderFooter"):
                opp_val = getattr(old_value, "HeaderFooter", None)
                if opp_val == self:
                    setattr(old_value, "HeaderFooter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HeaderFooter"):
                opp_val = getattr(value, "HeaderFooter", None)
                setattr(value, "HeaderFooter", self)

    @property
    def cs_visioDocument(self):
        return self.__cs_visioDocument

    @cs_visioDocument.setter
    def cs_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__cs_visioDocument", None)
        self.__cs_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorsTable"):
                opp_val = getattr(old_value, "ColorsTable", None)
                if opp_val == self:
                    setattr(old_value, "ColorsTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorsTable"):
                opp_val = getattr(value, "ColorsTable", None)
                setattr(value, "ColorsTable", self)

    @property
    def sss_visioDocument(self):
        return self.__sss_visioDocument

    @sss_visioDocument.setter
    def sss_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__sss_visioDocument", None)
        self.__sss_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleSheetsCollection"):
                opp_val = getattr(old_value, "StyleSheetsCollection", None)
                if opp_val == self:
                    setattr(old_value, "StyleSheetsCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleSheetsCollection"):
                opp_val = getattr(value, "StyleSheetsCollection", None)
                setattr(value, "StyleSheetsCollection", self)

    @property
    def sx_visioDocument(self):
        return self.__sx_visioDocument

    @sx_visioDocument.setter
    def sx_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__sx_visioDocument", None)
        self.__sx_visioDocument = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SolutionXML"):
                    opp_val = getattr(item, "SolutionXML", None)
                    
                    if opp_val == self:
                        setattr(item, "SolutionXML", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SolutionXML"):
                    opp_val = getattr(item, "SolutionXML", None)
                    
                    setattr(item, "SolutionXML", self)
                    

    @property
    def el_visioDocument(self):
        return self.__el_visioDocument

    @el_visioDocument.setter
    def el_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__el_visioDocument", None)
        self.__el_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventList"):
                opp_val = getattr(old_value, "EventList", None)
                if opp_val == self:
                    setattr(old_value, "EventList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventList"):
                opp_val = getattr(value, "EventList", None)
                setattr(value, "EventList", self)

    @property
    def ps_visioDocument10(self):
        return self.__ps_visioDocument10

    @ps_visioDocument10.setter
    def ps_visioDocument10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__ps_visioDocument10", None)
        self.__ps_visioDocument10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagesCollection"):
                opp_val = getattr(old_value, "PagesCollection", None)
                if opp_val == self:
                    setattr(old_value, "PagesCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagesCollection"):
                opp_val = getattr(value, "PagesCollection", None)
                setattr(value, "PagesCollection", self)

    @property
    def erd_visioDocument(self):
        return self.__erd_visioDocument

    @erd_visioDocument.setter
    def erd_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__erd_visioDocument", None)
        self.__erd_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EmailRoutingData"):
                opp_val = getattr(old_value, "EmailRoutingData", None)
                if opp_val == self:
                    setattr(old_value, "EmailRoutingData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EmailRoutingData"):
                opp_val = getattr(value, "EmailRoutingData", None)
                setattr(value, "EmailRoutingData", self)

    @property
    def fs_visioDocument(self):
        return self.__fs_visioDocument

    @fs_visioDocument.setter
    def fs_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__fs_visioDocument", None)
        self.__fs_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FontsTable"):
                opp_val = getattr(old_value, "FontsTable", None)
                if opp_val == self:
                    setattr(old_value, "FontsTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FontsTable"):
                opp_val = getattr(value, "FontsTable", None)
                setattr(value, "FontsTable", self)

    @property
    def ds_visioDocument(self):
        return self.__ds_visioDocument

    @ds_visioDocument.setter
    def ds_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__ds_visioDocument", None)
        self.__ds_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DocumentSheet"):
                opp_val = getattr(old_value, "DocumentSheet", None)
                if opp_val == self:
                    setattr(old_value, "DocumentSheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DocumentSheet"):
                opp_val = getattr(value, "DocumentSheet", None)
                setattr(value, "DocumentSheet", self)

    @property
    def fns_visioDocument(self):
        return self.__fns_visioDocument

    @fns_visioDocument.setter
    def fns_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__fns_visioDocument", None)
        self.__fns_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaceNamesTable"):
                opp_val = getattr(old_value, "FaceNamesTable", None)
                if opp_val == self:
                    setattr(old_value, "FaceNamesTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaceNamesTable"):
                opp_val = getattr(value, "FaceNamesTable", None)
                setattr(value, "FaceNamesTable", self)

    @property
    def dps_visioDocument(self):
        return self.__dps_visioDocument

    @dps_visioDocument.setter
    def dps_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLBasicDef_VisioDocument__dps_visioDocument", None)
        self.__dps_visioDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DocumentPropertiesCollection"):
                opp_val = getattr(old_value, "DocumentPropertiesCollection", None)
                if opp_val == self:
                    setattr(old_value, "DocumentPropertiesCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DocumentPropertiesCollection"):
                opp_val = getattr(value, "DocumentPropertiesCollection", None)
                setattr(value, "DocumentPropertiesCollection", self)

class DatadiagramMLBasicDef_CellType:

    def __init__(self, unit: str, formula: str, err: str, value: str):
        self.unit = unit
        self.formula = formula
        self.err = err
        self.value = value
        
        pass
    @property
    def formula(self):
        return self.__formula

    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def err(self):
        return self.__err

    @err.setter
    def err(self, err: str):
        self.__err = err


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

