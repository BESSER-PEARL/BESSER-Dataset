from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RendererHint(Enum):
    CANVAS = "CANVAS"
    DOM = "DOM"
    WEBGL = "WEBGL"
class ScriptContext(Enum):
    GLOBAL = "GLOBAL"
    MAP = "MAP"
    LAYER = "LAYER"
class SourceFormat(Enum):
    INTERNAL = "INTERNAL"
    GeoJSON = "GeoJSON"
    GPX = "GPX"
    KML = "KML"
class EventCondition(Enum):
    SINGLE_CLICK = "SINGLE_CLICK"
    CLICK = "CLICK"
    HOVER = "HOVER"


############################################
# Definition of Classes
############################################

class geom_geoff_Location:

    pass
class SimpleGeometry:

    pass
class geoff_geom_Polygon(SimpleGeometry):

    pass
class geoff_geom_LineString(SimpleGeometry):

    pass
class geoff_geom_Point(SimpleGeometry):

    pass
class style_geoff_Color:

    pass
class Text:

    pass
class Stroke:

    pass
class Fill:

    pass
class Image:

    pass
class geoff_style_Icon(Image):

    def __init__(self, src: str, Image: "geoff_style_Style"):
        self.src = src
        
    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

class geoff_style_Circle(Image):

    def __init__(self, radius: float, geoff_style_Circle: "Fill" = None, geoff_style_Circle37: "Stroke" = None, Image: "geoff_style_Style"):
        self.radius = radius
        self.geoff_style_Circle = geoff_style_Circle
        self.geoff_style_Circle37 = geoff_style_Circle37
        
    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        self.__radius = radius

    @property
    def geoff_style_Circle(self):
        return self.__geoff_style_Circle

    @geoff_style_Circle.setter
    def geoff_style_Circle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_style_Circle__geoff_style_Circle", None)
        self.__geoff_style_Circle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fill35"):
                opp_val = getattr(old_value, "Fill35", None)
                if opp_val == self:
                    setattr(old_value, "Fill35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fill35"):
                opp_val = getattr(value, "Fill35", None)
                setattr(value, "Fill35", self)

    @property
    def geoff_style_Circle37(self):
        return self.__geoff_style_Circle37

    @geoff_style_Circle37.setter
    def geoff_style_Circle37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_style_Circle__geoff_style_Circle37", None)
        self.__geoff_style_Circle37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Stroke38"):
                opp_val = getattr(old_value, "Stroke38", None)
                if opp_val == self:
                    setattr(old_value, "Stroke38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Stroke38"):
                opp_val = getattr(value, "Stroke38", None)
                setattr(value, "Stroke38", self)

class layer_geoff_StyleEntry:

    pass
class source_geoff_Feature:

    pass
class XYZ:

    pass
class geoff_source_BingMaps(XYZ):

    def __init__(self, key: str, imagerySet: str):
        self.key = key
        self.imagerySet = imagerySet
        
    @property
    def imagerySet(self) -> str:
        return self.__imagerySet

    @imagerySet.setter
    def imagerySet(self, imagerySet: str):
        self.__imagerySet = imagerySet

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class geoff_source_MapQuest(XYZ):

    def __init__(self, layer: str):
        self.layer = layer
        
    @property
    def layer(self) -> str:
        return self.__layer

    @layer.setter
    def layer(self, layer: str):
        self.__layer = layer

class geoff_source_OSM(XYZ):

    pass
class TileImage:

    pass
class geoff_source_XYZ(TileImage):

    pass
class TileSource:

    pass
class geoff_source_TileImage(TileSource):

    pass
class Source:

    pass
class geoff_source_VectorSource(Source):

    def __init__(self, url: str, projection: str, format: str, geoff_source_VectorSource: set["source_geoff_Feature"] = None, Source: "geoff_layer_Layer"):
        self.url = url
        self.projection = projection
        self.format = format
        self.geoff_source_VectorSource = geoff_source_VectorSource if geoff_source_VectorSource is not None else set()
        
    @property
    def projection(self) -> str:
        return self.__projection

    @projection.setter
    def projection(self, projection: str):
        self.__projection = projection

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def geoff_source_VectorSource(self):
        return self.__geoff_source_VectorSource

    @geoff_source_VectorSource.setter
    def geoff_source_VectorSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_source_VectorSource__geoff_source_VectorSource", None)
        self.__geoff_source_VectorSource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "source_geoff_Feature"):
                    opp_val = getattr(item, "source_geoff_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "source_geoff_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "source_geoff_Feature"):
                    opp_val = getattr(item, "source_geoff_Feature", None)
                    
                    setattr(item, "source_geoff_Feature", self)
                    

class geoff_source_TileSource(Source):

    pass
class Location:

    pass
class geoff_StyleEntry:

    def __init__(self, key: str, geoff_StyleEntry: "Style" = None):
        self.key = key
        self.geoff_StyleEntry = geoff_StyleEntry
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def geoff_StyleEntry(self):
        return self.__geoff_StyleEntry

    @geoff_StyleEntry.setter
    def geoff_StyleEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_StyleEntry__geoff_StyleEntry", None)
        self.__geoff_StyleEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Style15"):
                opp_val = getattr(old_value, "Style15", None)
                if opp_val == self:
                    setattr(old_value, "Style15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Style15"):
                opp_val = getattr(value, "Style15", None)
                setattr(value, "Style15", self)

class geoff_StringToStringMapEntry:

    def __init__(self, key: str, value: str, geoff_StringToStringMapEntry: "geoff_Feature" = None):
        self.key = key
        self.value = value
        self.geoff_StringToStringMapEntry = geoff_StringToStringMapEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def geoff_StringToStringMapEntry(self):
        return self.__geoff_StringToStringMapEntry

    @geoff_StringToStringMapEntry.setter
    def geoff_StringToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_StringToStringMapEntry__geoff_StringToStringMapEntry", None)
        self.__geoff_StringToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "geoff_Feature13"):
                opp_val = getattr(old_value, "geoff_Feature13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "geoff_Feature13"):
                opp_val = getattr(value, "geoff_Feature13", None)
                if opp_val is None:
                    setattr(value, "geoff_Feature13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Style:

    pass
class Geometry:

    pass
class geoff_geom_SimpleGeometry(Geometry):

    pass
class geoff_Descriptive(ABC):

    def __init__(self, longDescription: str, shortDescription: str):
        self.longDescription = longDescription
        self.shortDescription = shortDescription
        
    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def longDescription(self) -> str:
        return self.__longDescription

    @longDescription.setter
    def longDescription(self, longDescription: str):
        self.__longDescription = longDescription

class geoff_XYZLocation(Location):

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, z: float):
        self.__z = z

class Interaction:

    pass
class geoff_interaction_Select(Interaction):

    def __init__(self, condition: str, multi: bool, Interaction: "geoff_GeoMap"):
        self.condition = condition
        self.multi = multi
        
    @property
    def multi(self) -> bool:
        return self.__multi

    @multi.setter
    def multi(self, multi: bool):
        self.__multi = multi

    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

class Layer:

    pass
class geoff_layer_VectorLayer(Layer):

    pass
class geoff_layer_TileLayer(Layer):

    pass
class Descriptive:

    pass
class Identifiable:

    pass
class geoff_style_Stroke(Identifiable):

    def __init__(self, lineCap: str, lineJoin: str, miterLimit: str, width: str, lineDash: float, geoff_style_Stroke: "style_geoff_Color" = None):
        self.lineCap = lineCap
        self.lineJoin = lineJoin
        self.miterLimit = miterLimit
        self.width = width
        self.lineDash = lineDash
        self.geoff_style_Stroke = geoff_style_Stroke
        
    @property
    def lineCap(self) -> str:
        return self.__lineCap

    @lineCap.setter
    def lineCap(self, lineCap: str):
        self.__lineCap = lineCap

    @property
    def miterLimit(self) -> str:
        return self.__miterLimit

    @miterLimit.setter
    def miterLimit(self, miterLimit: str):
        self.__miterLimit = miterLimit

    @property
    def lineDash(self) -> float:
        return self.__lineDash

    @lineDash.setter
    def lineDash(self, lineDash: float):
        self.__lineDash = lineDash

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def lineJoin(self) -> str:
        return self.__lineJoin

    @lineJoin.setter
    def lineJoin(self, lineJoin: str):
        self.__lineJoin = lineJoin

    @property
    def geoff_style_Stroke(self):
        return self.__geoff_style_Stroke

    @geoff_style_Stroke.setter
    def geoff_style_Stroke(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_style_Stroke__geoff_style_Stroke", None)
        self.__geoff_style_Stroke = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_geoff_Color33"):
                opp_val = getattr(old_value, "style_geoff_Color33", None)
                if opp_val == self:
                    setattr(old_value, "style_geoff_Color33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_geoff_Color33"):
                opp_val = getattr(value, "style_geoff_Color33", None)
                setattr(value, "style_geoff_Color33", self)

class geoff_Feature(Identifiable):

    def __init__(self, onclick: str, geoff_Feature: "Geometry" = None, geoff_Feature11: "Style" = None, geoff_Feature13: set["geoff_StringToStringMapEntry"] = None):
        self.onclick = onclick
        self.geoff_Feature = geoff_Feature
        self.geoff_Feature11 = geoff_Feature11
        self.geoff_Feature13 = geoff_Feature13 if geoff_Feature13 is not None else set()
        
    @property
    def onclick(self) -> str:
        return self.__onclick

    @onclick.setter
    def onclick(self, onclick: str):
        self.__onclick = onclick

    @property
    def geoff_Feature13(self):
        return self.__geoff_Feature13

    @geoff_Feature13.setter
    def geoff_Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_Feature__geoff_Feature13", None)
        self.__geoff_Feature13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "geoff_StringToStringMapEntry"):
                    opp_val = getattr(item, "geoff_StringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "geoff_StringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "geoff_StringToStringMapEntry"):
                    opp_val = getattr(item, "geoff_StringToStringMapEntry", None)
                    
                    setattr(item, "geoff_StringToStringMapEntry", self)
                    

    @property
    def geoff_Feature11(self):
        return self.__geoff_Feature11

    @geoff_Feature11.setter
    def geoff_Feature11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_Feature__geoff_Feature11", None)
        self.__geoff_Feature11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Style"):
                opp_val = getattr(old_value, "Style", None)
                if opp_val == self:
                    setattr(old_value, "Style", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Style"):
                opp_val = getattr(value, "Style", None)
                setattr(value, "Style", self)

    @property
    def geoff_Feature(self):
        return self.__geoff_Feature

    @geoff_Feature.setter
    def geoff_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_Feature__geoff_Feature", None)
        self.__geoff_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry"):
                opp_val = getattr(old_value, "Geometry", None)
                if opp_val == self:
                    setattr(old_value, "Geometry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry"):
                opp_val = getattr(value, "Geometry", None)
                setattr(value, "Geometry", self)

class geoff_style_Style(Identifiable):

    def __init__(self, zindex: str, geoff_style_Style: "Image" = None, geoff_style_Style26: "Fill" = None, geoff_style_Style28: "Stroke" = None, geoff_style_Style30: "Text" = None):
        self.zindex = zindex
        self.geoff_style_Style = geoff_style_Style
        self.geoff_style_Style26 = geoff_style_Style26
        self.geoff_style_Style28 = geoff_style_Style28
        self.geoff_style_Style30 = geoff_style_Style30
        
    @property
    def zindex(self) -> str:
        return self.__zindex

    @zindex.setter
    def zindex(self, zindex: str):
        self.__zindex = zindex

    @property
    def geoff_style_Style30(self):
        return self.__geoff_style_Style30

    @geoff_style_Style30.setter
    def geoff_style_Style30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_style_Style__geoff_style_Style30", None)
        self.__geoff_style_Style30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Text"):
                opp_val = getattr(old_value, "Text", None)
                if opp_val == self:
                    setattr(old_value, "Text", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Text"):
                opp_val = getattr(value, "Text", None)
                setattr(value, "Text", self)

    @property
    def geoff_style_Style26(self):
        return self.__geoff_style_Style26

    @geoff_style_Style26.setter
    def geoff_style_Style26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_style_Style__geoff_style_Style26", None)
        self.__geoff_style_Style26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fill"):
                opp_val = getattr(old_value, "Fill", None)
                if opp_val == self:
                    setattr(old_value, "Fill", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fill"):
                opp_val = getattr(value, "Fill", None)
                setattr(value, "Fill", self)

    @property
    def geoff_style_Style28(self):
        return self.__geoff_style_Style28

    @geoff_style_Style28.setter
    def geoff_style_Style28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_style_Style__geoff_style_Style28", None)
        self.__geoff_style_Style28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Stroke"):
                opp_val = getattr(old_value, "Stroke", None)
                if opp_val == self:
                    setattr(old_value, "Stroke", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Stroke"):
                opp_val = getattr(value, "Stroke", None)
                setattr(value, "Stroke", self)

    @property
    def geoff_style_Style(self):
        return self.__geoff_style_Style

    @geoff_style_Style.setter
    def geoff_style_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_style_Style__geoff_style_Style", None)
        self.__geoff_style_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Image"):
                opp_val = getattr(old_value, "Image", None)
                if opp_val == self:
                    setattr(old_value, "Image", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Image"):
                opp_val = getattr(value, "Image", None)
                setattr(value, "Image", self)

class geoff_Script(Identifiable):

    def __init__(self, src: str, type: str, context: str, geoff_Script: "geoff_GeoMap" = None):
        self.src = src
        self.type = type
        self.context = context
        self.geoff_Script = geoff_Script
        
    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def geoff_Script(self):
        return self.__geoff_Script

    @geoff_Script.setter
    def geoff_Script(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_Script__geoff_Script", None)
        self.__geoff_Script = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "geoff_GeoMap4"):
                opp_val = getattr(old_value, "geoff_GeoMap4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "geoff_GeoMap4"):
                opp_val = getattr(value, "geoff_GeoMap4", None)
                if opp_val is None:
                    setattr(value, "geoff_GeoMap4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class geoff_geom_Geometry(Identifiable):

    pass
class geoff_source_Source(Identifiable, Descriptive):

    pass
class geoff_interaction_Interaction(Identifiable):

    pass
class geoff_style_Image(Identifiable):

    pass
class geoff_View(Identifiable):

    def __init__(self, zoom: int, geoff_View: "geoff_GeoMap" = None, geoff_View8: "geoff_Location" = None):
        self.zoom = zoom
        self.geoff_View = geoff_View
        self.geoff_View8 = geoff_View8
        
    @property
    def zoom(self) -> int:
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: int):
        self.__zoom = zoom

    @property
    def geoff_View(self):
        return self.__geoff_View

    @geoff_View.setter
    def geoff_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_View__geoff_View", None)
        self.__geoff_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "geoff_GeoMap2"):
                opp_val = getattr(old_value, "geoff_GeoMap2", None)
                if opp_val == self:
                    setattr(old_value, "geoff_GeoMap2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "geoff_GeoMap2"):
                opp_val = getattr(value, "geoff_GeoMap2", None)
                setattr(value, "geoff_GeoMap2", self)

    @property
    def geoff_View8(self):
        return self.__geoff_View8

    @geoff_View8.setter
    def geoff_View8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_View__geoff_View8", None)
        self.__geoff_View8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "geoff_Location"):
                opp_val = getattr(old_value, "geoff_Location", None)
                if opp_val == self:
                    setattr(old_value, "geoff_Location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "geoff_Location"):
                opp_val = getattr(value, "geoff_Location", None)
                setattr(value, "geoff_Location", self)

class geoff_layer_Layer(Identifiable, Descriptive):

    pass
class geoff_Color(Identifiable):

    def __init__(self, red: int, green: int, blue: int, alpha: float):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
        
    @property
    def blue(self) -> int:
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue

    @property
    def alpha(self) -> float:
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: float):
        self.__alpha = alpha

    @property
    def red(self) -> int:
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red

    @property
    def green(self) -> int:
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green

class geoff_style_Fill(Identifiable):

    pass
class geoff_style_Text(Identifiable):

    def __init__(self, textAlign: str, textBaseLine: str, font: str, offsetX: float, offsetY: float, rotation: str, scale: str, text: str, geoff_style_Text: "Fill" = None, geoff_style_Text42: "Stroke" = None):
        self.textAlign = textAlign
        self.textBaseLine = textBaseLine
        self.font = font
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.rotation = rotation
        self.scale = scale
        self.text = text
        self.geoff_style_Text = geoff_style_Text
        self.geoff_style_Text42 = geoff_style_Text42
        
    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

    @property
    def textAlign(self) -> str:
        return self.__textAlign

    @textAlign.setter
    def textAlign(self, textAlign: str):
        self.__textAlign = textAlign

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def textBaseLine(self) -> str:
        return self.__textBaseLine

    @textBaseLine.setter
    def textBaseLine(self, textBaseLine: str):
        self.__textBaseLine = textBaseLine

    @property
    def offsetY(self) -> float:
        return self.__offsetY

    @offsetY.setter
    def offsetY(self, offsetY: float):
        self.__offsetY = offsetY

    @property
    def rotation(self) -> str:
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation

    @property
    def font(self) -> str:
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font

    @property
    def offsetX(self) -> float:
        return self.__offsetX

    @offsetX.setter
    def offsetX(self, offsetX: float):
        self.__offsetX = offsetX

    @property
    def geoff_style_Text42(self):
        return self.__geoff_style_Text42

    @geoff_style_Text42.setter
    def geoff_style_Text42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_style_Text__geoff_style_Text42", None)
        self.__geoff_style_Text42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Stroke43"):
                opp_val = getattr(old_value, "Stroke43", None)
                if opp_val == self:
                    setattr(old_value, "Stroke43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Stroke43"):
                opp_val = getattr(value, "Stroke43", None)
                setattr(value, "Stroke43", self)

    @property
    def geoff_style_Text(self):
        return self.__geoff_style_Text

    @geoff_style_Text.setter
    def geoff_style_Text(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_style_Text__geoff_style_Text", None)
        self.__geoff_style_Text = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fill40"):
                opp_val = getattr(old_value, "Fill40", None)
                if opp_val == self:
                    setattr(old_value, "Fill40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fill40"):
                opp_val = getattr(value, "Fill40", None)
                setattr(value, "Fill40", self)

class geoff_Location(Identifiable):

    def __init__(self, projectionCode: str, geoff_Location: "geoff_View" = None):
        self.projectionCode = projectionCode
        self.geoff_Location = geoff_Location
        
    @property
    def projectionCode(self) -> str:
        return self.__projectionCode

    @projectionCode.setter
    def projectionCode(self, projectionCode: str):
        self.__projectionCode = projectionCode

    @property
    def geoff_Location(self):
        return self.__geoff_Location

    @geoff_Location.setter
    def geoff_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_Location__geoff_Location", None)
        self.__geoff_Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "geoff_View8"):
                opp_val = getattr(old_value, "geoff_View8", None)
                if opp_val == self:
                    setattr(old_value, "geoff_View8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "geoff_View8"):
                opp_val = getattr(value, "geoff_View8", None)
                setattr(value, "geoff_View8", self)

class geoff_GeoMap(Descriptive, Identifiable):

    def __init__(self, rendererHint: str, geoff_GeoMap: set["Layer"] = None, geoff_GeoMap2: "geoff_View" = None, geoff_GeoMap4: set["geoff_Script"] = None, geoff_GeoMap6: set["Interaction"] = None):
        self.rendererHint = rendererHint
        self.geoff_GeoMap = geoff_GeoMap if geoff_GeoMap is not None else set()
        self.geoff_GeoMap2 = geoff_GeoMap2
        self.geoff_GeoMap4 = geoff_GeoMap4 if geoff_GeoMap4 is not None else set()
        self.geoff_GeoMap6 = geoff_GeoMap6 if geoff_GeoMap6 is not None else set()
        
    @property
    def rendererHint(self) -> str:
        return self.__rendererHint

    @rendererHint.setter
    def rendererHint(self, rendererHint: str):
        self.__rendererHint = rendererHint

    @property
    def geoff_GeoMap6(self):
        return self.__geoff_GeoMap6

    @geoff_GeoMap6.setter
    def geoff_GeoMap6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_GeoMap__geoff_GeoMap6", None)
        self.__geoff_GeoMap6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interaction"):
                    opp_val = getattr(item, "Interaction", None)
                    
                    if opp_val == self:
                        setattr(item, "Interaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interaction"):
                    opp_val = getattr(item, "Interaction", None)
                    
                    setattr(item, "Interaction", self)
                    

    @property
    def geoff_GeoMap(self):
        return self.__geoff_GeoMap

    @geoff_GeoMap.setter
    def geoff_GeoMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_GeoMap__geoff_GeoMap", None)
        self.__geoff_GeoMap = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Layer"):
                    opp_val = getattr(item, "Layer", None)
                    
                    if opp_val == self:
                        setattr(item, "Layer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Layer"):
                    opp_val = getattr(item, "Layer", None)
                    
                    setattr(item, "Layer", self)
                    

    @property
    def geoff_GeoMap2(self):
        return self.__geoff_GeoMap2

    @geoff_GeoMap2.setter
    def geoff_GeoMap2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_GeoMap__geoff_GeoMap2", None)
        self.__geoff_GeoMap2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "geoff_View"):
                opp_val = getattr(old_value, "geoff_View", None)
                if opp_val == self:
                    setattr(old_value, "geoff_View", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "geoff_View"):
                opp_val = getattr(value, "geoff_View", None)
                setattr(value, "geoff_View", self)

    @property
    def geoff_GeoMap4(self):
        return self.__geoff_GeoMap4

    @geoff_GeoMap4.setter
    def geoff_GeoMap4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_geoff_GeoMap__geoff_GeoMap4", None)
        self.__geoff_GeoMap4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "geoff_Script"):
                    opp_val = getattr(item, "geoff_Script", None)
                    
                    if opp_val == self:
                        setattr(item, "geoff_Script", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "geoff_Script"):
                    opp_val = getattr(item, "geoff_Script", None)
                    
                    setattr(item, "geoff_Script", self)
                    

class geoff_Identifiable(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id
