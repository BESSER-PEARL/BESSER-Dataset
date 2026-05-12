from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class XYABCDElt:

    pass
class DatadiagramMLXForm_EllipticalArcTo(XYABCDElt):

    pass
class DatadiagramMLXForm_XYABCDEElt(XYABCDElt):

    pass
class DatadiagramMLXForm_SplineStart(XYABCDElt):

    pass
class DatadiagramMLXForm_Ellipse(XYABCDElt):

    pass
class DatadiagramMLXForm_IXrequiredElt(ABC):

    def __init__(self, iX: str):
        self.iX = iX
        
        pass
    @property
    def iX(self):
        return self.__iX

    @iX.setter
    def iX(self, iX: str):
        self.__iX = iX


class Text:

    pass
class DatadiagramMLXForm_TextElt(ABC):

    pass
class Geom:

    pass
class XYElt:

    pass
class DatadiagramMLXForm_LineTo(XYElt):

    pass
class XYABElt:

    pass
class DatadiagramMLXForm_XYABCDElt(XYABElt):

    pass
class DatadiagramMLXForm_InfiniteLine(XYABElt):

    pass
class XYAElt:

    pass
class DatadiagramMLXForm_SplineKnot(XYAElt):

    pass
class DatadiagramMLXForm_XYABElt(XYAElt):

    pass
class DatadiagramMLXForm_PolylineTo(XYAElt):

    pass
class DatadiagramMLXForm_ArcTo(XYAElt):

    pass
class DatadiagramMLXForm_XYAElt(XYElt):

    pass
class DatadiagramMLXForm_MoveTo(XYElt):

    pass
class CellType:

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
class DatadiagramMLXForm_IdentifiedElt(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
        pass
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


class DatadiagramMLXForm_NamedElt(ABC):

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
class UniqueIdElt:

    pass
class DelElt:

    pass
class IXElt:

    pass
class DatadiagramMLXForm_XYElt(IXElt, DelElt):

    pass
class DatadiagramMLXForm_DelElt(ABC):

    def __init__(self, del_: str):
        self.del_ = del_
        
        pass
    @property
    def del_(self):
        return self.__del_

    @del_.setter
    def del_(self, del_: str):
        self.__del_ = del_


class DatadiagramMLXForm_IXElt(ABC):

    def __init__(self, iX: str):
        self.iX = iX
        
        pass
    @property
    def iX(self):
        return self.__iX

    @iX.setter
    def iX(self, iX: str):
        self.__iX = iX


class DatadiagramMLXForm_ShapeElt(ABC):

    pass
class ShapeElt:

    pass
class DatadiagramMLXForm_Geom(IXElt, DelElt, ShapeElt):

    pass
class ShapesCollection:

    pass
class DatadiagramMLXForm_Shape:

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
    def fillStyle(self):
        return self.__fillStyle

    @fillStyle.setter
    def fillStyle(self, fillStyle: str):
        self.__fillStyle = fillStyle


    @property
    def lineStyle(self):
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle


    @property
    def sse_shapeSheet(self):
        return self.__sse_shapeSheet

    @sse_shapeSheet.setter
    def sse_shapeSheet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_Shape__sse_shapeSheet", None)
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
        old_value = getattr(self, f"_DatadiagramMLXForm_Shape__shapes", None)
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

class DatadiagramMLXForm_UniqueIdElt(ABC):

    def __init__(self, UniqueID: str):
        self.UniqueID = UniqueID
        
        pass
    @property
    def UniqueID(self):
        return self.__UniqueID

    @UniqueID.setter
    def UniqueID(self, UniqueID: str):
        self.__UniqueID = UniqueID


class PageSheet:

    pass
class NamedElt:

    pass
class DatadiagramMLXForm_DocumentSheet(NamedElt, PageSheet):

    pass
class Shape:

    pass
class DatadiagramMLXForm_PageSheet(Shape, PageElt, UniqueIdElt, MasterElt):

    pass
class FaceName:

    pass
class DatadiagramMLXForm_FaceNamesTable:

    pass
class DatadiagramMLXForm_StyleSheetsCollection:

    pass
class DatadiagramMLXForm_EmailRoutingData:

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
        old_value = getattr(self, f"_DatadiagramMLXForm_EmailRoutingData__docEmailRoutingData", None)
        self.__docEmailRoutingData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisioDocument74"):
                opp_val = getattr(old_value, "VisioDocument74", None)
                if opp_val == self:
                    setattr(old_value, "VisioDocument74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisioDocument74"):
                opp_val = getattr(value, "VisioDocument74", None)
                setattr(value, "VisioDocument74", self)

class DatadiagramMLXForm_VBProjectData:

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
        old_value = getattr(self, f"_DatadiagramMLXForm_VBProjectData__docVBProjectData", None)
        self.__docVBProjectData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisioDocument72"):
                opp_val = getattr(old_value, "VisioDocument72", None)
                if opp_val == self:
                    setattr(old_value, "VisioDocument72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisioDocument72"):
                opp_val = getattr(value, "VisioDocument72", None)
                setattr(value, "VisioDocument72", self)

class IdentifiedElt:

    pass
class DatadiagramMLXForm_StyleSheet(NamedElt, Shape, IdentifiedElt):

    pass
class DatadiagramMLXForm_FaceName(IdentifiedElt):

    def __init__(self, name: str, unicodeRanges: str, charSet: str, panos: str, flags: str, faceNameEntries: "FaceNamesTable" = None):
        self.name = name
        self.unicodeRanges = unicodeRanges
        self.charSet = charSet
        self.panos = panos
        self.flags = flags
        self.faceNameEntries = faceNameEntries
        
        pass
    @property
    def charSet(self):
        return self.__charSet

    @charSet.setter
    def charSet(self, charSet: str):
        self.__charSet = charSet


    @property
    def flags(self):
        return self.__flags

    @flags.setter
    def flags(self, flags: str):
        self.__flags = flags


    @property
    def unicodeRanges(self):
        return self.__unicodeRanges

    @unicodeRanges.setter
    def unicodeRanges(self, unicodeRanges: str):
        self.__unicodeRanges = unicodeRanges


    @property
    def panos(self):
        return self.__panos

    @panos.setter
    def panos(self, panos: str):
        self.__panos = panos


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def faceNameEntries(self):
        return self.__faceNameEntries

    @faceNameEntries.setter
    def faceNameEntries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_FaceName__faceNameEntries", None)
        self.__faceNameEntries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaceNamesTable70"):
                opp_val = getattr(old_value, "FaceNamesTable70", None)
                if opp_val == self:
                    setattr(old_value, "FaceNamesTable70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaceNamesTable70"):
                opp_val = getattr(value, "FaceNamesTable70", None)
                setattr(value, "FaceNamesTable70", self)

class DatadiagramMLXForm_FontEntry(IdentifiedElt):

    def __init__(self, name: str, charSet: str, pitchAndFamily: str, attributes: str, weight: str, unicode: str, fontEntries: "FontsTable" = None):
        self.name = name
        self.charSet = charSet
        self.pitchAndFamily = pitchAndFamily
        self.attributes = attributes
        self.weight = weight
        self.unicode = unicode
        self.fontEntries = fontEntries
        
        pass
    @property
    def charSet(self):
        return self.__charSet

    @charSet.setter
    def charSet(self, charSet: str):
        self.__charSet = charSet


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def pitchAndFamily(self):
        return self.__pitchAndFamily

    @pitchAndFamily.setter
    def pitchAndFamily(self, pitchAndFamily: str):
        self.__pitchAndFamily = pitchAndFamily


    @property
    def unicode(self):
        return self.__unicode

    @unicode.setter
    def unicode(self, unicode: str):
        self.__unicode = unicode


    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, attributes: str):
        self.__attributes = attributes


    @property
    def fontEntries(self):
        return self.__fontEntries

    @fontEntries.setter
    def fontEntries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_FontEntry__fontEntries", None)
        self.__fontEntries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FontsTable65"):
                opp_val = getattr(old_value, "FontsTable65", None)
                if opp_val == self:
                    setattr(old_value, "FontsTable65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FontsTable65"):
                opp_val = getattr(value, "FontsTable65", None)
                setattr(value, "FontsTable65", self)

class FontEntry:

    pass
class DatadiagramMLXForm_FontsTable:

    pass
class DatadiagramMLXForm_PrintSetup:

    pass
class SnapAnglesCollection:

    pass
class IXrequiredElt:

    pass
class DatadiagramMLXForm_ColorEntry(IXrequiredElt):

    def __init__(self, rgb: str, colorEntries: "ColorsTable" = None):
        self.rgb = rgb
        self.colorEntries = colorEntries
        
        pass
    @property
    def rgb(self):
        return self.__rgb

    @rgb.setter
    def rgb(self, rgb: str):
        self.__rgb = rgb


    @property
    def colorEntries(self):
        return self.__colorEntries

    @colorEntries.setter
    def colorEntries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_ColorEntry__colorEntries", None)
        self.__colorEntries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorsTable58"):
                opp_val = getattr(old_value, "ColorsTable58", None)
                if opp_val == self:
                    setattr(old_value, "ColorsTable58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorsTable58"):
                opp_val = getattr(value, "ColorsTable58", None)
                setattr(value, "ColorsTable58", self)

class ColorEntry:

    pass
class StyleSheet:

    pass
class DatadiagramMLXForm_ColorsTable:

    pass
class Page:

    pass
class DatadiagramMLXForm_SnapAngle:

    def __init__(self, angleValue: str, snapAngles: "SnapAnglesCollection" = None):
        self.angleValue = angleValue
        self.snapAngles = snapAngles
        
        pass
    @property
    def angleValue(self):
        return self.__angleValue

    @angleValue.setter
    def angleValue(self, angleValue: str):
        self.__angleValue = angleValue


    @property
    def snapAngles(self):
        return self.__snapAngles

    @snapAngles.setter
    def snapAngles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_SnapAngle__snapAngles", None)
        self.__snapAngles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SnapAnglesCollection53"):
                opp_val = getattr(old_value, "SnapAnglesCollection53", None)
                if opp_val == self:
                    setattr(old_value, "SnapAnglesCollection53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SnapAnglesCollection53"):
                opp_val = getattr(value, "SnapAnglesCollection53", None)
                setattr(value, "SnapAnglesCollection53", self)

class SnapAngle:

    pass
class DatadiagramMLXForm_SnapAnglesCollection:

    pass
class DateTimeType:

    pass
class CustomPropertiesCollection:

    pass
class DatadiagramMLXForm_DocumentSettingsElt:

    def __init__(self, dynamicGridEnabled: str, protectStyles: str, protectShapes: str, protectMasters: str, protectBkgnds: str, customMenusFile: str, customToolbarsFile: str, attachedToolbars: str, glueSettings: str, snapSettings: str, snapExtensions: str, DatadiagramMLXForm_DocumentSettingsElt40: "StyleSheet" = None, DatadiagramMLXForm_DocumentSettingsElt43: "StyleSheet" = None, DatadiagramMLXForm_DocumentSettingsElt46: "StyleSheet" = None, sa_docSettings: "SnapAnglesCollection" = None, docSettings: "VisioDocument" = None, DatadiagramMLXForm_DocumentSettingsElt: "Page" = None, DatadiagramMLXForm_DocumentSettingsElt38: "StyleSheet" = None):
        self.dynamicGridEnabled = dynamicGridEnabled
        self.protectStyles = protectStyles
        self.protectShapes = protectShapes
        self.protectMasters = protectMasters
        self.protectBkgnds = protectBkgnds
        self.customMenusFile = customMenusFile
        self.customToolbarsFile = customToolbarsFile
        self.attachedToolbars = attachedToolbars
        self.glueSettings = glueSettings
        self.snapSettings = snapSettings
        self.snapExtensions = snapExtensions
        self.DatadiagramMLXForm_DocumentSettingsElt40 = DatadiagramMLXForm_DocumentSettingsElt40
        self.DatadiagramMLXForm_DocumentSettingsElt43 = DatadiagramMLXForm_DocumentSettingsElt43
        self.DatadiagramMLXForm_DocumentSettingsElt46 = DatadiagramMLXForm_DocumentSettingsElt46
        self.sa_docSettings = sa_docSettings
        self.docSettings = docSettings
        self.DatadiagramMLXForm_DocumentSettingsElt = DatadiagramMLXForm_DocumentSettingsElt
        self.DatadiagramMLXForm_DocumentSettingsElt38 = DatadiagramMLXForm_DocumentSettingsElt38
        
        pass
    @property
    def glueSettings(self):
        return self.__glueSettings

    @glueSettings.setter
    def glueSettings(self, glueSettings: str):
        self.__glueSettings = glueSettings


    @property
    def protectShapes(self):
        return self.__protectShapes

    @protectShapes.setter
    def protectShapes(self, protectShapes: str):
        self.__protectShapes = protectShapes


    @property
    def customToolbarsFile(self):
        return self.__customToolbarsFile

    @customToolbarsFile.setter
    def customToolbarsFile(self, customToolbarsFile: str):
        self.__customToolbarsFile = customToolbarsFile


    @property
    def snapSettings(self):
        return self.__snapSettings

    @snapSettings.setter
    def snapSettings(self, snapSettings: str):
        self.__snapSettings = snapSettings


    @property
    def snapExtensions(self):
        return self.__snapExtensions

    @snapExtensions.setter
    def snapExtensions(self, snapExtensions: str):
        self.__snapExtensions = snapExtensions


    @property
    def protectStyles(self):
        return self.__protectStyles

    @protectStyles.setter
    def protectStyles(self, protectStyles: str):
        self.__protectStyles = protectStyles


    @property
    def protectMasters(self):
        return self.__protectMasters

    @protectMasters.setter
    def protectMasters(self, protectMasters: str):
        self.__protectMasters = protectMasters


    @property
    def dynamicGridEnabled(self):
        return self.__dynamicGridEnabled

    @dynamicGridEnabled.setter
    def dynamicGridEnabled(self, dynamicGridEnabled: str):
        self.__dynamicGridEnabled = dynamicGridEnabled


    @property
    def customMenusFile(self):
        return self.__customMenusFile

    @customMenusFile.setter
    def customMenusFile(self, customMenusFile: str):
        self.__customMenusFile = customMenusFile


    @property
    def protectBkgnds(self):
        return self.__protectBkgnds

    @protectBkgnds.setter
    def protectBkgnds(self, protectBkgnds: str):
        self.__protectBkgnds = protectBkgnds


    @property
    def attachedToolbars(self):
        return self.__attachedToolbars

    @attachedToolbars.setter
    def attachedToolbars(self, attachedToolbars: str):
        self.__attachedToolbars = attachedToolbars


    @property
    def sa_docSettings(self):
        return self.__sa_docSettings

    @sa_docSettings.setter
    def sa_docSettings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentSettingsElt__sa_docSettings", None)
        self.__sa_docSettings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SnapAnglesCollection"):
                opp_val = getattr(old_value, "SnapAnglesCollection", None)
                if opp_val == self:
                    setattr(old_value, "SnapAnglesCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SnapAnglesCollection"):
                opp_val = getattr(value, "SnapAnglesCollection", None)
                setattr(value, "SnapAnglesCollection", self)

    @property
    def docSettings(self):
        return self.__docSettings

    @docSettings.setter
    def docSettings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentSettingsElt__docSettings", None)
        self.__docSettings = value
        
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

    @property
    def DatadiagramMLXForm_DocumentSettingsElt(self):
        return self.__DatadiagramMLXForm_DocumentSettingsElt

    @DatadiagramMLXForm_DocumentSettingsElt.setter
    def DatadiagramMLXForm_DocumentSettingsElt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentSettingsElt__DatadiagramMLXForm_DocumentSettingsElt", None)
        self.__DatadiagramMLXForm_DocumentSettingsElt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page"):
                opp_val = getattr(old_value, "Page", None)
                if opp_val == self:
                    setattr(old_value, "Page", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page"):
                opp_val = getattr(value, "Page", None)
                setattr(value, "Page", self)

    @property
    def DatadiagramMLXForm_DocumentSettingsElt40(self):
        return self.__DatadiagramMLXForm_DocumentSettingsElt40

    @DatadiagramMLXForm_DocumentSettingsElt40.setter
    def DatadiagramMLXForm_DocumentSettingsElt40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentSettingsElt__DatadiagramMLXForm_DocumentSettingsElt40", None)
        self.__DatadiagramMLXForm_DocumentSettingsElt40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleSheet41"):
                opp_val = getattr(old_value, "StyleSheet41", None)
                if opp_val == self:
                    setattr(old_value, "StyleSheet41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleSheet41"):
                opp_val = getattr(value, "StyleSheet41", None)
                setattr(value, "StyleSheet41", self)

    @property
    def DatadiagramMLXForm_DocumentSettingsElt46(self):
        return self.__DatadiagramMLXForm_DocumentSettingsElt46

    @DatadiagramMLXForm_DocumentSettingsElt46.setter
    def DatadiagramMLXForm_DocumentSettingsElt46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentSettingsElt__DatadiagramMLXForm_DocumentSettingsElt46", None)
        self.__DatadiagramMLXForm_DocumentSettingsElt46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleSheet47"):
                opp_val = getattr(old_value, "StyleSheet47", None)
                if opp_val == self:
                    setattr(old_value, "StyleSheet47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleSheet47"):
                opp_val = getattr(value, "StyleSheet47", None)
                setattr(value, "StyleSheet47", self)

    @property
    def DatadiagramMLXForm_DocumentSettingsElt43(self):
        return self.__DatadiagramMLXForm_DocumentSettingsElt43

    @DatadiagramMLXForm_DocumentSettingsElt43.setter
    def DatadiagramMLXForm_DocumentSettingsElt43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentSettingsElt__DatadiagramMLXForm_DocumentSettingsElt43", None)
        self.__DatadiagramMLXForm_DocumentSettingsElt43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleSheet44"):
                opp_val = getattr(old_value, "StyleSheet44", None)
                if opp_val == self:
                    setattr(old_value, "StyleSheet44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleSheet44"):
                opp_val = getattr(value, "StyleSheet44", None)
                setattr(value, "StyleSheet44", self)

    @property
    def DatadiagramMLXForm_DocumentSettingsElt38(self):
        return self.__DatadiagramMLXForm_DocumentSettingsElt38

    @DatadiagramMLXForm_DocumentSettingsElt38.setter
    def DatadiagramMLXForm_DocumentSettingsElt38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentSettingsElt__DatadiagramMLXForm_DocumentSettingsElt38", None)
        self.__DatadiagramMLXForm_DocumentSettingsElt38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleSheet"):
                opp_val = getattr(old_value, "StyleSheet", None)
                if opp_val == self:
                    setattr(old_value, "StyleSheet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleSheet"):
                opp_val = getattr(value, "StyleSheet", None)
                setattr(value, "StyleSheet", self)

class DatadiagramMLXForm_CustomProperty:

    def __init__(self, name: str, dataType: str, cps_customProps: "CustomPropertiesCollection" = None):
        self.name = name
        self.dataType = dataType
        self.cps_customProps = cps_customProps
        
        pass
    @property
    def dataType(self):
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def cps_customProps(self):
        return self.__cps_customProps

    @cps_customProps.setter
    def cps_customProps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_CustomProperty__cps_customProps", None)
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
class DatadiagramMLXForm_CustomPropertiesCollection:

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
class MastersCollection:

    pass
class DocumentSheet:

    pass
class StyleSheetsCollection:

    pass
class VisioDocument:

    pass
class DatadiagramMLXForm_DocumentPropertiesCollection:

    def __init__(self, title: str, subject: str, creator: str, manager: str, company: str, category: str, keywords: str, description: str, hyperlinkBase_href: str, alternateNames: str, template: str, buildNumberCreated: str, buildNumberEdited: str, docProps: "VisioDocument" = None, DatadiagramMLXForm_DocumentPropertiesCollection27: "DateTimeType" = None, cps_docProp: "CustomPropertiesCollection" = None, DatadiagramMLXForm_DocumentPropertiesCollection: "DateTimeType" = None, DatadiagramMLXForm_DocumentPropertiesCollection21: "DateTimeType" = None, DatadiagramMLXForm_DocumentPropertiesCollection24: "DateTimeType" = None):
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
        self.buildNumberEdited = buildNumberEdited
        self.docProps = docProps
        self.DatadiagramMLXForm_DocumentPropertiesCollection27 = DatadiagramMLXForm_DocumentPropertiesCollection27
        self.cps_docProp = cps_docProp
        self.DatadiagramMLXForm_DocumentPropertiesCollection = DatadiagramMLXForm_DocumentPropertiesCollection
        self.DatadiagramMLXForm_DocumentPropertiesCollection21 = DatadiagramMLXForm_DocumentPropertiesCollection21
        self.DatadiagramMLXForm_DocumentPropertiesCollection24 = DatadiagramMLXForm_DocumentPropertiesCollection24
        
        pass
    @property
    def hyperlinkBase_href(self):
        return self.__hyperlinkBase_href

    @hyperlinkBase_href.setter
    def hyperlinkBase_href(self, hyperlinkBase_href: str):
        self.__hyperlinkBase_href = hyperlinkBase_href


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def creator(self):
        return self.__creator

    @creator.setter
    def creator(self, creator: str):
        self.__creator = creator


    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords


    @property
    def buildNumberEdited(self):
        return self.__buildNumberEdited

    @buildNumberEdited.setter
    def buildNumberEdited(self, buildNumberEdited: str):
        self.__buildNumberEdited = buildNumberEdited


    @property
    def buildNumberCreated(self):
        return self.__buildNumberCreated

    @buildNumberCreated.setter
    def buildNumberCreated(self, buildNumberCreated: str):
        self.__buildNumberCreated = buildNumberCreated


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


    @property
    def alternateNames(self):
        return self.__alternateNames

    @alternateNames.setter
    def alternateNames(self, alternateNames: str):
        self.__alternateNames = alternateNames


    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template


    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company: str):
        self.__company = company


    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager: str):
        self.__manager = manager


    @property
    def DatadiagramMLXForm_DocumentPropertiesCollection24(self):
        return self.__DatadiagramMLXForm_DocumentPropertiesCollection24

    @DatadiagramMLXForm_DocumentPropertiesCollection24.setter
    def DatadiagramMLXForm_DocumentPropertiesCollection24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentPropertiesCollection__DatadiagramMLXForm_DocumentPropertiesCollection24", None)
        self.__DatadiagramMLXForm_DocumentPropertiesCollection24 = value
        
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

    @property
    def DatadiagramMLXForm_DocumentPropertiesCollection27(self):
        return self.__DatadiagramMLXForm_DocumentPropertiesCollection27

    @DatadiagramMLXForm_DocumentPropertiesCollection27.setter
    def DatadiagramMLXForm_DocumentPropertiesCollection27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentPropertiesCollection__DatadiagramMLXForm_DocumentPropertiesCollection27", None)
        self.__DatadiagramMLXForm_DocumentPropertiesCollection27 = value
        
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
    def DatadiagramMLXForm_DocumentPropertiesCollection21(self):
        return self.__DatadiagramMLXForm_DocumentPropertiesCollection21

    @DatadiagramMLXForm_DocumentPropertiesCollection21.setter
    def DatadiagramMLXForm_DocumentPropertiesCollection21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentPropertiesCollection__DatadiagramMLXForm_DocumentPropertiesCollection21", None)
        self.__DatadiagramMLXForm_DocumentPropertiesCollection21 = value
        
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
    def docProps(self):
        return self.__docProps

    @docProps.setter
    def docProps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentPropertiesCollection__docProps", None)
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
    def DatadiagramMLXForm_DocumentPropertiesCollection(self):
        return self.__DatadiagramMLXForm_DocumentPropertiesCollection

    @DatadiagramMLXForm_DocumentPropertiesCollection.setter
    def DatadiagramMLXForm_DocumentPropertiesCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentPropertiesCollection__DatadiagramMLXForm_DocumentPropertiesCollection", None)
        self.__DatadiagramMLXForm_DocumentPropertiesCollection = value
        
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
    def cps_docProp(self):
        return self.__cps_docProp

    @cps_docProp.setter
    def cps_docProp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_DocumentPropertiesCollection__cps_docProp", None)
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

class SolutionXML:

    pass
class EmailRoutingData:

    pass
class DocumentPropertiesCollection:

    pass
class DatadiagramMLXForm_VisioDocument:

    def __init__(self, start: str, key: str, metric: str, buildnum: str, version: str, docLangId: str, dss_visioDocument: "DocumentSettingsElt" = None, cs_visioDocument: "ColorsTable" = None, ps_visioDocument: "PrintSetup" = None, fs_visioDocument: "FontsTable" = None, fns_visioDocument: "FaceNamesTable" = None, dps_visioDocument: "DocumentPropertiesCollection" = None, erd_visioDocument: "EmailRoutingData" = None, sx_visioDocument: set["SolutionXML"] = None, sss_visioDocument: "StyleSheetsCollection" = None, ds_visioDocument: "DocumentSheet" = None, ms_visioDocument: "MastersCollection" = None, ps_visioDocument10: "PagesCollection" = None, ws_visioDocument: "WindowsInfo" = None, el_visioDocument: "EventList" = None, ef_visioDocument: "HeaderFooter" = None, vpd_visioDocument: "VBProjectData" = None):
        self.start = start
        self.key = key
        self.metric = metric
        self.buildnum = buildnum
        self.version = version
        self.docLangId = docLangId
        self.dss_visioDocument = dss_visioDocument
        self.cs_visioDocument = cs_visioDocument
        self.ps_visioDocument = ps_visioDocument
        self.fs_visioDocument = fs_visioDocument
        self.fns_visioDocument = fns_visioDocument
        self.dps_visioDocument = dps_visioDocument
        self.erd_visioDocument = erd_visioDocument
        self.sx_visioDocument = sx_visioDocument if sx_visioDocument is not None else set()
        self.sss_visioDocument = sss_visioDocument
        self.ds_visioDocument = ds_visioDocument
        self.ms_visioDocument = ms_visioDocument
        self.ps_visioDocument10 = ps_visioDocument10
        self.ws_visioDocument = ws_visioDocument
        self.el_visioDocument = el_visioDocument
        self.ef_visioDocument = ef_visioDocument
        self.vpd_visioDocument = vpd_visioDocument
        
        pass
    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def buildnum(self):
        return self.__buildnum

    @buildnum.setter
    def buildnum(self, buildnum: str):
        self.__buildnum = buildnum


    @property
    def metric(self):
        return self.__metric

    @metric.setter
    def metric(self, metric: str):
        self.__metric = metric


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def docLangId(self):
        return self.__docLangId

    @docLangId.setter
    def docLangId(self, docLangId: str):
        self.__docLangId = docLangId


    @property
    def fs_visioDocument(self):
        return self.__fs_visioDocument

    @fs_visioDocument.setter
    def fs_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__fs_visioDocument", None)
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
    def ef_visioDocument(self):
        return self.__ef_visioDocument

    @ef_visioDocument.setter
    def ef_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__ef_visioDocument", None)
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
    def sss_visioDocument(self):
        return self.__sss_visioDocument

    @sss_visioDocument.setter
    def sss_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__sss_visioDocument", None)
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
    def dps_visioDocument(self):
        return self.__dps_visioDocument

    @dps_visioDocument.setter
    def dps_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__dps_visioDocument", None)
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

    @property
    def cs_visioDocument(self):
        return self.__cs_visioDocument

    @cs_visioDocument.setter
    def cs_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__cs_visioDocument", None)
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
    def erd_visioDocument(self):
        return self.__erd_visioDocument

    @erd_visioDocument.setter
    def erd_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__erd_visioDocument", None)
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
    def ps_visioDocument10(self):
        return self.__ps_visioDocument10

    @ps_visioDocument10.setter
    def ps_visioDocument10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__ps_visioDocument10", None)
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
    def dss_visioDocument(self):
        return self.__dss_visioDocument

    @dss_visioDocument.setter
    def dss_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__dss_visioDocument", None)
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
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__ms_visioDocument", None)
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
    def ds_visioDocument(self):
        return self.__ds_visioDocument

    @ds_visioDocument.setter
    def ds_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__ds_visioDocument", None)
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
    def sx_visioDocument(self):
        return self.__sx_visioDocument

    @sx_visioDocument.setter
    def sx_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__sx_visioDocument", None)
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
    def fns_visioDocument(self):
        return self.__fns_visioDocument

    @fns_visioDocument.setter
    def fns_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__fns_visioDocument", None)
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
    def ps_visioDocument(self):
        return self.__ps_visioDocument

    @ps_visioDocument.setter
    def ps_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__ps_visioDocument", None)
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
    def ws_visioDocument(self):
        return self.__ws_visioDocument

    @ws_visioDocument.setter
    def ws_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__ws_visioDocument", None)
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
    def el_visioDocument(self):
        return self.__el_visioDocument

    @el_visioDocument.setter
    def el_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__el_visioDocument", None)
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
    def vpd_visioDocument(self):
        return self.__vpd_visioDocument

    @vpd_visioDocument.setter
    def vpd_visioDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_VisioDocument__vpd_visioDocument", None)
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

class FaceNamesTable:

    pass
class FontsTable:

    pass
class PrintSetup:

    pass
class DatadiagramMLXForm_CellType:

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
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class ColorsTable:

    pass
class DocumentSettingsElt:

    pass
class DatadiagramMLXForm_SolutionXML:

    pass
class DatadiagramMLXForm_HeaderFooter:

    pass
class DatadiagramMLXForm_EventList:

    pass
class DatadiagramMLXForm_WindowsInfo:

    pass
class DatadiagramMLXForm_PageElt(ABC):

    pass
class DatadiagramMLXForm_Page(NamedElt, IdentifiedElt):

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
    def ViewCenterY(self):
        return self.__ViewCenterY

    @ViewCenterY.setter
    def ViewCenterY(self, ViewCenterY: str):
        self.__ViewCenterY = ViewCenterY


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
        old_value = getattr(self, f"_DatadiagramMLXForm_Page__pages", None)
        self.__pages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PagesCollection319"):
                opp_val = getattr(old_value, "PagesCollection319", None)
                if opp_val == self:
                    setattr(old_value, "PagesCollection319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PagesCollection319"):
                opp_val = getattr(value, "PagesCollection319", None)
                setattr(value, "PagesCollection319", self)

    @property
    def pe_page(self):
        return self.__pe_page

    @pe_page.setter
    def pe_page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_Page__pe_page", None)
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
                    

class DatadiagramMLXForm_PagesCollection:

    pass
class DatadiagramMLXForm_MasterElt(ABC):

    pass
class Connect:

    pass
class DatadiagramMLXForm_ConnectsCollection(PageElt, MasterElt):

    pass
class DatadiagramMLXForm_ShapesCollection(PageElt, MasterElt):

    pass
class ConnectsCollection:

    pass
class DatadiagramMLXForm_Connect:

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
    def fromPart(self):
        return self.__fromPart

    @fromPart.setter
    def fromPart(self, fromPart: str):
        self.__fromPart = fromPart


    @property
    def toCell(self):
        return self.__toCell

    @toCell.setter
    def toCell(self, toCell: str):
        self.__toCell = toCell


    @property
    def toSheet(self):
        return self.__toSheet

    @toSheet.setter
    def toSheet(self, toSheet: str):
        self.__toSheet = toSheet


    @property
    def toPart(self):
        return self.__toPart

    @toPart.setter
    def toPart(self, toPart: str):
        self.__toPart = toPart


    @property
    def fromCell(self):
        return self.__fromCell

    @fromCell.setter
    def fromCell(self, fromCell: str):
        self.__fromCell = fromCell


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
        old_value = getattr(self, f"_DatadiagramMLXForm_Connect__connections", None)
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

class DatadiagramMLXForm_MasterShortCut(NamedElt, IdentifiedElt):

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
    def alignName(self):
        return self.__alignName

    @alignName.setter
    def alignName(self, alignName: str):
        self.__alignName = alignName


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
        old_value = getattr(self, f"_DatadiagramMLXForm_MasterShortCut__masterShortCuts", None)
        self.__masterShortCuts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MastersCollection301"):
                opp_val = getattr(old_value, "MastersCollection301", None)
                if opp_val == self:
                    setattr(old_value, "MastersCollection301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MastersCollection301"):
                opp_val = getattr(value, "MastersCollection301", None)
                setattr(value, "MastersCollection301", self)

    @property
    def i_masterShortCut(self):
        return self.__i_masterShortCut

    @i_masterShortCut.setter
    def i_masterShortCut(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_MasterShortCut__i_masterShortCut", None)
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
class DatadiagramMLXForm_Master(NamedElt, UniqueIdElt, IdentifiedElt):

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
    def alignName(self):
        return self.__alignName

    @alignName.setter
    def alignName(self, alignName: str):
        self.__alignName = alignName


    @property
    def patternFlags(self):
        return self.__patternFlags

    @patternFlags.setter
    def patternFlags(self, patternFlags: str):
        self.__patternFlags = patternFlags


    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: str):
        self.__hidden = hidden


    @property
    def baseID(self):
        return self.__baseID

    @baseID.setter
    def baseID(self, baseID: str):
        self.__baseID = baseID


    @property
    def prompt(self):
        return self.__prompt

    @prompt.setter
    def prompt(self, prompt: str):
        self.__prompt = prompt


    @property
    def iconUpdate(self):
        return self.__iconUpdate

    @iconUpdate.setter
    def iconUpdate(self, iconUpdate: str):
        self.__iconUpdate = iconUpdate


    @property
    def masters(self):
        return self.__masters

    @masters.setter
    def masters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_Master__masters", None)
        self.__masters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MastersCollection306"):
                opp_val = getattr(old_value, "MastersCollection306", None)
                if opp_val == self:
                    setattr(old_value, "MastersCollection306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MastersCollection306"):
                opp_val = getattr(value, "MastersCollection306", None)
                setattr(value, "MastersCollection306", self)

    @property
    def me_master(self):
        return self.__me_master

    @me_master.setter
    def me_master(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DatadiagramMLXForm_Master__me_master", None)
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
                    

class Master:

    pass
class DatadiagramMLXForm_Icon(MasterElt):

    def __init__(self, value: str, icons: "MasterShortCut" = None, MasterElt: "DatadiagramMLXForm_Master" = None):
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
        old_value = getattr(self, f"_DatadiagramMLXForm_Icon__icons", None)
        self.__icons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MasterShortCut304"):
                opp_val = getattr(old_value, "MasterShortCut304", None)
                if opp_val == self:
                    setattr(old_value, "MasterShortCut304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MasterShortCut304"):
                opp_val = getattr(value, "MasterShortCut304", None)
                setattr(value, "MasterShortCut304", self)

class Icon:

    pass
class DatadiagramMLXForm_XForm(DelElt, ShapeElt):

    pass
class DatadiagramMLXForm_MastersCollection:

    pass
class DatadiagramMLXForm_Field(IXElt, DelElt, ShapeElt):

    pass
class TabsCollection:

    pass
class DatadiagramMLXForm_Tab(IXElt):

    pass
class Tab:

    pass
class DatadiagramMLXForm_TabsCollection(IXElt, DelElt, ShapeElt):

    pass
class DatadiagramMLXForm_Para(IXElt, DelElt, ShapeElt):

    pass
class DatadiagramMLXForm_Char(IXElt, DelElt, ShapeElt):

    pass
class TextElt:

    pass
class DatadiagramMLXForm_StringElt(TextElt):

    def __init__(self, value: str, TextElt: "DatadiagramMLXForm_Text" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class DatadiagramMLXForm_Fld(IXrequiredElt, TextElt):

    pass
class DatadiagramMLXForm_Tp(IXrequiredElt, TextElt):

    pass
class DatadiagramMLXForm_Cp(IXrequiredElt, TextElt):

    pass
class DatadiagramMLXForm_Pp(IXrequiredElt, TextElt):

    pass
class DatadiagramMLXForm_Text(ShapeElt):

    pass
class XYABCDEElt:

    pass
class DatadiagramMLXForm_NURBSTo(XYABCDEElt):

    pass
class DatadiagramMLXForm_DateTimeType:

    def __init__(self, hour: str, minute: str, year: str, month: str, day: str, second: str):
        self.hour = hour
        self.minute = minute
        self.year = year
        self.month = month
        self.day = day
        self.second = second
        
        pass
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second: str):
        self.__second = second


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour: str):
        self.__hour = hour


    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute: str):
        self.__minute = minute

