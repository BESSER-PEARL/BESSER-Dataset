from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Smoothness(Enum):
    None = "None"
    Normal = "Normal"
    Less = "Less"
    More = "More"
class Sorting(Enum):
    None = "None"
    Manual = "Manual"
    Automatic = "Automatic"
class Alignment(Enum):
    Left = "Left"
    Right = "Right"
    Center = "Center"
    Top = "Top"
    Bottom = "Bottom"
class TextAlignment(Enum):
    Left = "Left"
    Right = "Right"
    Center = "Center"
class Filtering(Enum):
    None = "None"
    Manual = "Manual"
    Automatic = "Automatic"
class Routing(Enum):
    Manual = "Manual"
    Rectilinear = "Rectilinear"
    Tree = "Tree"
class SortingDirection(Enum):
    Ascending = "Ascending"
    Descending = "Descending"
class JumpLinkType(Enum):
    Semicircle = "Semicircle"
    Square = "Square"
    Chamfered = "Chamfered"
class ArrowType(Enum):
    None = "None"
    OpenArrow = "OpenArrow"
    SolidArrow = "SolidArrow"
class MeasurementUnit(Enum):
    Himetric = "Himetric"
    Pixel = "Pixel"
class LineType(Enum):
    Solid = "Solid"
    Dash = "Dash"
    Dot = "Dot"
    DashDot = "DashDot"
    DashDotDot = "DashDotDot"
    Double = "Double"
class GradientStyle(Enum):
    Vertical = "Vertical"
    Horizontal = "Horizontal"
class JumpLinkStatus(Enum):
    None = "None"
    All = "All"
    Below = "Below"
    Above = "Above"


############################################
# Definition of Classes
############################################

class DecorationNode:

    pass
class BasicDecorationNode:

    pass
class notation_DecorationNode(BasicDecorationNode):

    pass
class BasicSemanticCompartment:

    pass
class DrawerStyle:

    pass
class notation_BasicSemanticCompartment(BasicDecorationNode, DrawerStyle):

    pass
class notation_BasicCompartment(DecorationNode, DrawerStyle):

    pass
class DiagramStyle:

    pass
class Diagram:

    pass
class notation_StandardDiagram(DiagramStyle, Diagram):

    pass
class ConnectorStyle:

    pass
class Edge:

    pass
class notation_Connector(Edge, ConnectorStyle):

    pass
class FilteringStyle:

    pass
class SortingStyle:

    pass
class TitleStyle:

    pass
class notation_SemanticListCompartment(BasicSemanticCompartment, SortingStyle, FilteringStyle, TitleStyle):

    pass
class CanonicalStyle:

    pass
class BasicCompartment:

    pass
class notation_ListCompartment(BasicCompartment, SortingStyle, FilteringStyle, TitleStyle):

    pass
class notation_Compartment(BasicCompartment, CanonicalStyle, TitleStyle):

    pass
class ShapeStyle:

    pass
class Node:

    pass
class notation_BasicDecorationNode(Node):

    pass
class notation_Shape(ShapeStyle, Node):

    pass
class DataTypeStyle:

    pass
class notation_SingleValueStyle(DataTypeStyle):

    def __init__(self, rawValue: str):
        self.rawValue = rawValue
        
    @property
    def rawValue(self) -> str:
        return self.__rawValue

    @rawValue.setter
    def rawValue(self, rawValue: str):
        self.__rawValue = rawValue

    def getValue(self) -> str:
        # TODO: Implement getValue method
        pass

    def setValue(self, newValue: str):
        # TODO: Implement setValue method
        pass

class DiagramLinkStyle:

    pass
class notation_StringObjectConverter(ABC):

    def __init__(self):
        
    def getStringFromObject(self, objectValue: str) -> str:
        # TODO: Implement getStringFromObject method
        pass

    def getObjectFromString(self, stringValue: str) -> str:
        # TODO: Implement getObjectFromString method
        pass

class notation_ListValueStyle(DataTypeStyle):

    def __init__(self, rawValuesList: str):
        self.rawValuesList = rawValuesList
        
    @property
    def rawValuesList(self) -> str:
        return self.__rawValuesList

    @rawValuesList.setter
    def rawValuesList(self, rawValuesList: str):
        self.__rawValuesList = rawValuesList

class notation_EDataType:

    pass
class StringObjectConverter:

    pass
class notation_PropertyValue(StringObjectConverter):

    def __init__(self, rawValue: str, notation_PropertyValue: "notation_StringToPropertyValueMapEntry" = None, notation_PropertyValue49: "notation_EDataType" = None):
        self.rawValue = rawValue
        self.notation_PropertyValue = notation_PropertyValue
        self.notation_PropertyValue49 = notation_PropertyValue49
        
    @property
    def rawValue(self) -> str:
        return self.__rawValue

    @rawValue.setter
    def rawValue(self, rawValue: str):
        self.__rawValue = rawValue

    @property
    def notation_PropertyValue(self):
        return self.__notation_PropertyValue

    @notation_PropertyValue.setter
    def notation_PropertyValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_PropertyValue__notation_PropertyValue", None)
        self.__notation_PropertyValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_StringToPropertyValueMapEntry47"):
                opp_val = getattr(old_value, "notation_StringToPropertyValueMapEntry47", None)
                if opp_val == self:
                    setattr(old_value, "notation_StringToPropertyValueMapEntry47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_StringToPropertyValueMapEntry47"):
                opp_val = getattr(value, "notation_StringToPropertyValueMapEntry47", None)
                setattr(value, "notation_StringToPropertyValueMapEntry47", self)

    @property
    def notation_PropertyValue49(self):
        return self.__notation_PropertyValue49

    @notation_PropertyValue49.setter
    def notation_PropertyValue49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_PropertyValue__notation_PropertyValue49", None)
        self.__notation_PropertyValue49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_EDataType"):
                opp_val = getattr(old_value, "notation_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "notation_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_EDataType"):
                opp_val = getattr(value, "notation_EDataType", None)
                setattr(value, "notation_EDataType", self)

    def setValue(self, newValue: str):
        # TODO: Implement setValue method
        pass

    def getValue(self) -> str:
        # TODO: Implement getValue method
        pass

class notation_StringToPropertyValueMapEntry:

    def __init__(self, key: str, notation_StringToPropertyValueMapEntry: "notation_PropertiesSetStyle" = None, notation_StringToPropertyValueMapEntry47: "notation_PropertyValue" = None):
        self.key = key
        self.notation_StringToPropertyValueMapEntry = notation_StringToPropertyValueMapEntry
        self.notation_StringToPropertyValueMapEntry47 = notation_StringToPropertyValueMapEntry47
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def notation_StringToPropertyValueMapEntry47(self):
        return self.__notation_StringToPropertyValueMapEntry47

    @notation_StringToPropertyValueMapEntry47.setter
    def notation_StringToPropertyValueMapEntry47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_StringToPropertyValueMapEntry__notation_StringToPropertyValueMapEntry47", None)
        self.__notation_StringToPropertyValueMapEntry47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_PropertyValue"):
                opp_val = getattr(old_value, "notation_PropertyValue", None)
                if opp_val == self:
                    setattr(old_value, "notation_PropertyValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_PropertyValue"):
                opp_val = getattr(value, "notation_PropertyValue", None)
                setattr(value, "notation_PropertyValue", self)

    @property
    def notation_StringToPropertyValueMapEntry(self):
        return self.__notation_StringToPropertyValueMapEntry

    @notation_StringToPropertyValueMapEntry.setter
    def notation_StringToPropertyValueMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_StringToPropertyValueMapEntry__notation_StringToPropertyValueMapEntry", None)
        self.__notation_StringToPropertyValueMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_PropertiesSetStyle"):
                opp_val = getattr(old_value, "notation_PropertiesSetStyle", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_PropertiesSetStyle"):
                opp_val = getattr(value, "notation_PropertiesSetStyle", None)
                if opp_val is None:
                    setattr(value, "notation_PropertiesSetStyle", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedStyle:

    pass
class notation_DataTypeStyle(StringObjectConverter, NamedStyle):

    pass
class notation_EObjectValueStyle(NamedStyle):

    pass
class notation_BooleanListValueStyle(NamedStyle):

    def __init__(self, booleanListValue: str):
        self.booleanListValue = booleanListValue
        
    @property
    def booleanListValue(self) -> str:
        return self.__booleanListValue

    @booleanListValue.setter
    def booleanListValue(self, booleanListValue: str):
        self.__booleanListValue = booleanListValue

class notation_ByteArrayValueStyle(NamedStyle):

    def __init__(self, byteArrayValue: str):
        self.byteArrayValue = byteArrayValue
        
    @property
    def byteArrayValue(self) -> str:
        return self.__byteArrayValue

    @byteArrayValue.setter
    def byteArrayValue(self, byteArrayValue: str):
        self.__byteArrayValue = byteArrayValue

class notation_DoubleListValueStyle(NamedStyle):

    def __init__(self, doubleListValue: str):
        self.doubleListValue = doubleListValue
        
    @property
    def doubleListValue(self) -> str:
        return self.__doubleListValue

    @doubleListValue.setter
    def doubleListValue(self, doubleListValue: str):
        self.__doubleListValue = doubleListValue

class notation_IntListValueStyle(NamedStyle):

    def __init__(self, intListValue: int):
        self.intListValue = intListValue
        
    @property
    def intListValue(self) -> int:
        return self.__intListValue

    @intListValue.setter
    def intListValue(self, intListValue: int):
        self.__intListValue = intListValue

class notation_IntValueStyle(NamedStyle):

    def __init__(self, intValue: int):
        self.intValue = intValue
        
    @property
    def intValue(self) -> int:
        return self.__intValue

    @intValue.setter
    def intValue(self, intValue: int):
        self.__intValue = intValue

class notation_DoubleValueStyle(NamedStyle):

    def __init__(self, doubleValue: float):
        self.doubleValue = doubleValue
        
    @property
    def doubleValue(self) -> float:
        return self.__doubleValue

    @doubleValue.setter
    def doubleValue(self, doubleValue: float):
        self.__doubleValue = doubleValue

class notation_StringValueStyle(NamedStyle):

    def __init__(self, stringValue: str):
        self.stringValue = stringValue
        
    @property
    def stringValue(self) -> str:
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue

class notation_StringListValueStyle(NamedStyle):

    def __init__(self, stringListValue: str):
        self.stringListValue = stringListValue
        
    @property
    def stringListValue(self) -> str:
        return self.__stringListValue

    @stringListValue.setter
    def stringListValue(self, stringListValue: str):
        self.__stringListValue = stringListValue

class notation_BooleanValueStyle(NamedStyle):

    def __init__(self, booleanValue: bool):
        self.booleanValue = booleanValue
        
    @property
    def booleanValue(self) -> bool:
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: bool):
        self.__booleanValue = booleanValue

class notation_EObjectListValueStyle(NamedStyle):

    pass
class notation_PropertiesSetStyle(NamedStyle):

    def __init__(self, notation_PropertiesSetStyle: set["notation_StringToPropertyValueMapEntry"] = None):
        self.notation_PropertiesSetStyle = notation_PropertiesSetStyle if notation_PropertiesSetStyle is not None else set()
        
    @property
    def notation_PropertiesSetStyle(self):
        return self.__notation_PropertiesSetStyle

    @notation_PropertiesSetStyle.setter
    def notation_PropertiesSetStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_PropertiesSetStyle__notation_PropertiesSetStyle", None)
        self.__notation_PropertiesSetStyle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_StringToPropertyValueMapEntry"):
                    opp_val = getattr(item, "notation_StringToPropertyValueMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_StringToPropertyValueMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_StringToPropertyValueMapEntry"):
                    opp_val = getattr(item, "notation_StringToPropertyValueMapEntry", None)
                    
                    setattr(item, "notation_StringToPropertyValueMapEntry", self)
                    

    def createProperty(self, initialValue: str, propertyName: str) -> bool:
        # TODO: Implement createProperty method
        pass

    def setProperty(self, propertyName: str, newValue: str) -> bool:
        # TODO: Implement setProperty method
        pass

    def createProperty(self, initialValue: str, propertyName: str, instanceType: str) -> bool:
        # TODO: Implement createProperty method
        pass

    def removeProperty(self, propertyName: str) -> bool:
        # TODO: Implement removeProperty method
        pass

    def getProperty(self, propertyName: str) -> str:
        # TODO: Implement getProperty method
        pass

    def hasProperty(self, propertyName: str) -> bool:
        # TODO: Implement hasProperty method
        pass

class ImageStyle:

    pass
class notation_ImageBufferStyle(ImageStyle):

    pass
class GuideStyle:

    pass
class PageStyle:

    pass
class notation_NodeEntry:

    def __init__(self, value: str, notation_NodeEntry: "notation_Guide" = None, notation_NodeEntry39: "notation_Node" = None):
        self.value = value
        self.notation_NodeEntry = notation_NodeEntry
        self.notation_NodeEntry39 = notation_NodeEntry39
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def notation_NodeEntry(self):
        return self.__notation_NodeEntry

    @notation_NodeEntry.setter
    def notation_NodeEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_NodeEntry__notation_NodeEntry", None)
        self.__notation_NodeEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Guide37"):
                opp_val = getattr(old_value, "notation_Guide37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Guide37"):
                opp_val = getattr(value, "notation_Guide37", None)
                if opp_val is None:
                    setattr(value, "notation_Guide37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def notation_NodeEntry39(self):
        return self.__notation_NodeEntry39

    @notation_NodeEntry39.setter
    def notation_NodeEntry39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_NodeEntry__notation_NodeEntry39", None)
        self.__notation_NodeEntry39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Node40"):
                opp_val = getattr(old_value, "notation_Node40", None)
                if opp_val == self:
                    setattr(old_value, "notation_Node40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Node40"):
                opp_val = getattr(value, "notation_Node40", None)
                setattr(value, "notation_Node40", self)

class notation_Guide:

    def __init__(self, position: int, notation_Guide: "notation_GuideStyle" = None, notation_Guide35: "notation_GuideStyle" = None, notation_Guide37: set["notation_NodeEntry"] = None):
        self.position = position
        self.notation_Guide = notation_Guide
        self.notation_Guide35 = notation_Guide35
        self.notation_Guide37 = notation_Guide37 if notation_Guide37 is not None else set()
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def notation_Guide35(self):
        return self.__notation_Guide35

    @notation_Guide35.setter
    def notation_Guide35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Guide__notation_Guide35", None)
        self.__notation_Guide35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_GuideStyle34"):
                opp_val = getattr(old_value, "notation_GuideStyle34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_GuideStyle34"):
                opp_val = getattr(value, "notation_GuideStyle34", None)
                if opp_val is None:
                    setattr(value, "notation_GuideStyle34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def notation_Guide(self):
        return self.__notation_Guide

    @notation_Guide.setter
    def notation_Guide(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Guide__notation_Guide", None)
        self.__notation_Guide = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_GuideStyle"):
                opp_val = getattr(old_value, "notation_GuideStyle", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_GuideStyle"):
                opp_val = getattr(value, "notation_GuideStyle", None)
                if opp_val is None:
                    setattr(value, "notation_GuideStyle", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def notation_Guide37(self):
        return self.__notation_Guide37

    @notation_Guide37.setter
    def notation_Guide37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Guide__notation_Guide37", None)
        self.__notation_Guide37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_NodeEntry"):
                    opp_val = getattr(item, "notation_NodeEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_NodeEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_NodeEntry"):
                    opp_val = getattr(item, "notation_NodeEntry", None)
                    
                    setattr(item, "notation_NodeEntry", self)
                    

class RoutingStyle:

    pass
class LineStyle:

    pass
class notation_ConnectorStyle(LineStyle, RoutingStyle):

    pass
class FillStyle:

    pass
class DescriptionStyle:

    pass
class notation_DiagramStyle(GuideStyle, PageStyle, DescriptionStyle):

    pass
class FontStyle:

    pass
class notation_Image:

    def __init__(self, data: str, notation_Image: "notation_ImageBufferStyle" = None):
        self.data = data
        self.notation_Image = notation_Image
        
    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def notation_Image(self):
        return self.__notation_Image

    @notation_Image.setter
    def notation_Image(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Image__notation_Image", None)
        self.__notation_Image = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_ImageBufferStyle"):
                opp_val = getattr(old_value, "notation_ImageBufferStyle", None)
                if opp_val == self:
                    setattr(old_value, "notation_ImageBufferStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_ImageBufferStyle"):
                opp_val = getattr(value, "notation_ImageBufferStyle", None)
                setattr(value, "notation_ImageBufferStyle", self)

class Bendpoints:

    pass
class notation_RelativeBendpoints(Bendpoints):

    def __init__(self, points: str):
        self.points = points
        
    @property
    def points(self) -> str:
        return self.__points

    @points.setter
    def points(self, points: str):
        self.__points = points

class EModelElement:

    pass
class RoundedCornersStyle:

    pass
class notation_ShapeStyle(DescriptionStyle, RoundedCornersStyle, FontStyle, FillStyle, LineStyle):

    pass
class notation_RoutingStyle(RoundedCornersStyle):

    def __init__(self, routing: str, smoothness: str, avoidObstructions: bool, closestDistance: bool, jumpLinkStatus: str, jumpLinkType: str, jumpLinksReverse: bool):
        self.routing = routing
        self.smoothness = smoothness
        self.avoidObstructions = avoidObstructions
        self.closestDistance = closestDistance
        self.jumpLinkStatus = jumpLinkStatus
        self.jumpLinkType = jumpLinkType
        self.jumpLinksReverse = jumpLinksReverse
        
    @property
    def routing(self) -> str:
        return self.__routing

    @routing.setter
    def routing(self, routing: str):
        self.__routing = routing

    @property
    def smoothness(self) -> str:
        return self.__smoothness

    @smoothness.setter
    def smoothness(self, smoothness: str):
        self.__smoothness = smoothness

    @property
    def closestDistance(self) -> bool:
        return self.__closestDistance

    @closestDistance.setter
    def closestDistance(self, closestDistance: bool):
        self.__closestDistance = closestDistance

    @property
    def jumpLinksReverse(self) -> bool:
        return self.__jumpLinksReverse

    @jumpLinksReverse.setter
    def jumpLinksReverse(self, jumpLinksReverse: bool):
        self.__jumpLinksReverse = jumpLinksReverse

    @property
    def jumpLinkStatus(self) -> str:
        return self.__jumpLinkStatus

    @jumpLinkStatus.setter
    def jumpLinkStatus(self, jumpLinkStatus: str):
        self.__jumpLinkStatus = jumpLinkStatus

    @property
    def jumpLinkType(self) -> str:
        return self.__jumpLinkType

    @jumpLinkType.setter
    def jumpLinkType(self, jumpLinkType: str):
        self.__jumpLinkType = jumpLinkType

    @property
    def avoidObstructions(self) -> bool:
        return self.__avoidObstructions

    @avoidObstructions.setter
    def avoidObstructions(self, avoidObstructions: bool):
        self.__avoidObstructions = avoidObstructions

class Anchor:

    pass
class notation_IdentityAnchor(Anchor):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class Size:

    pass
class Location:

    pass
class notation_Bounds(Size, Location):

    pass
class LayoutConstraint:

    pass
class notation_Location(LayoutConstraint):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

class notation_Ratio(LayoutConstraint):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class notation_Size(LayoutConstraint):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

class notation_EObject:

    pass
class Style:

    pass
class notation_CanonicalStyle(Style):

    def __init__(self, canonical: bool):
        self.canonical = canonical
        
    @property
    def canonical(self) -> bool:
        return self.__canonical

    @canonical.setter
    def canonical(self, canonical: bool):
        self.__canonical = canonical

class notation_TitleStyle(Style):

    def __init__(self, showTitle: bool):
        self.showTitle = showTitle
        
    @property
    def showTitle(self) -> bool:
        return self.__showTitle

    @showTitle.setter
    def showTitle(self, showTitle: bool):
        self.__showTitle = showTitle

class notation_LineTypeStyle(Style):

    def __init__(self, lineType: str):
        self.lineType = lineType
        
    @property
    def lineType(self) -> str:
        return self.__lineType

    @lineType.setter
    def lineType(self, lineType: str):
        self.__lineType = lineType

class notation_SortingStyle(Style):

    def __init__(self, sorting: str, sortingKeys: str, notation_SortingStyle: set["notation_EObject"] = None):
        self.sorting = sorting
        self.sortingKeys = sortingKeys
        self.notation_SortingStyle = notation_SortingStyle if notation_SortingStyle is not None else set()
        
    @property
    def sorting(self) -> str:
        return self.__sorting

    @sorting.setter
    def sorting(self, sorting: str):
        self.__sorting = sorting

    @property
    def sortingKeys(self) -> str:
        return self.__sortingKeys

    @sortingKeys.setter
    def sortingKeys(self, sortingKeys: str):
        self.__sortingKeys = sortingKeys

    @property
    def notation_SortingStyle(self):
        return self.__notation_SortingStyle

    @notation_SortingStyle.setter
    def notation_SortingStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_SortingStyle__notation_SortingStyle", None)
        self.__notation_SortingStyle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_EObject"):
                    opp_val = getattr(item, "notation_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_EObject"):
                    opp_val = getattr(item, "notation_EObject", None)
                    
                    setattr(item, "notation_EObject", self)
                    

class notation_DiagramLinkStyle(Style):

    pass
class notation_DrawerStyle(Style):

    def __init__(self, collapsed: bool):
        self.collapsed = collapsed
        
    @property
    def collapsed(self) -> bool:
        return self.__collapsed

    @collapsed.setter
    def collapsed(self, collapsed: bool):
        self.__collapsed = collapsed

class notation_ArrowStyle(Style):

    def __init__(self, arrowSource: str, arrowTarget: str):
        self.arrowSource = arrowSource
        self.arrowTarget = arrowTarget
        
    @property
    def arrowSource(self) -> str:
        return self.__arrowSource

    @arrowSource.setter
    def arrowSource(self, arrowSource: str):
        self.__arrowSource = arrowSource

    @property
    def arrowTarget(self) -> str:
        return self.__arrowTarget

    @arrowTarget.setter
    def arrowTarget(self, arrowTarget: str):
        self.__arrowTarget = arrowTarget

class notation_HintedDiagramLinkStyle(DiagramLinkStyle, Style):

    def __init__(self, hint: str):
        self.hint = hint
        
    @property
    def hint(self) -> str:
        return self.__hint

    @hint.setter
    def hint(self, hint: str):
        self.__hint = hint

class notation_LineStyle(Style):

    def __init__(self, lineColor: int, lineWidth: int):
        self.lineColor = lineColor
        self.lineWidth = lineWidth
        
    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

    @property
    def lineColor(self) -> int:
        return self.__lineColor

    @lineColor.setter
    def lineColor(self, lineColor: int):
        self.__lineColor = lineColor

class notation_FilteringStyle(Style):

    def __init__(self, filtering: str, filteringKeys: str, notation_FilteringStyle: set["notation_EObject"] = None):
        self.filtering = filtering
        self.filteringKeys = filteringKeys
        self.notation_FilteringStyle = notation_FilteringStyle if notation_FilteringStyle is not None else set()
        
    @property
    def filtering(self) -> str:
        return self.__filtering

    @filtering.setter
    def filtering(self, filtering: str):
        self.__filtering = filtering

    @property
    def filteringKeys(self) -> str:
        return self.__filteringKeys

    @filteringKeys.setter
    def filteringKeys(self, filteringKeys: str):
        self.__filteringKeys = filteringKeys

    @property
    def notation_FilteringStyle(self):
        return self.__notation_FilteringStyle

    @notation_FilteringStyle.setter
    def notation_FilteringStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_FilteringStyle__notation_FilteringStyle", None)
        self.__notation_FilteringStyle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_EObject42"):
                    opp_val = getattr(item, "notation_EObject42", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_EObject42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_EObject42"):
                    opp_val = getattr(item, "notation_EObject42", None)
                    
                    setattr(item, "notation_EObject42", self)
                    

class notation_RoundedCornersStyle(Style):

    def __init__(self, roundedBendpointsRadius: int):
        self.roundedBendpointsRadius = roundedBendpointsRadius
        
    @property
    def roundedBendpointsRadius(self) -> int:
        return self.__roundedBendpointsRadius

    @roundedBendpointsRadius.setter
    def roundedBendpointsRadius(self, roundedBendpointsRadius: int):
        self.__roundedBendpointsRadius = roundedBendpointsRadius

class notation_FontStyle(Style):

    def __init__(self, fontColor: int, fontName: str, fontHeight: int, bold: bool, italic: bool, underline: bool, strikeThrough: bool):
        self.fontColor = fontColor
        self.fontName = fontName
        self.fontHeight = fontHeight
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.strikeThrough = strikeThrough
        
    @property
    def underline(self) -> bool:
        return self.__underline

    @underline.setter
    def underline(self, underline: bool):
        self.__underline = underline

    @property
    def fontName(self) -> str:
        return self.__fontName

    @fontName.setter
    def fontName(self, fontName: str):
        self.__fontName = fontName

    @property
    def fontHeight(self) -> int:
        return self.__fontHeight

    @fontHeight.setter
    def fontHeight(self, fontHeight: int):
        self.__fontHeight = fontHeight

    @property
    def bold(self) -> bool:
        return self.__bold

    @bold.setter
    def bold(self, bold: bool):
        self.__bold = bold

    @property
    def strikeThrough(self) -> bool:
        return self.__strikeThrough

    @strikeThrough.setter
    def strikeThrough(self, strikeThrough: bool):
        self.__strikeThrough = strikeThrough

    @property
    def fontColor(self) -> int:
        return self.__fontColor

    @fontColor.setter
    def fontColor(self, fontColor: int):
        self.__fontColor = fontColor

    @property
    def italic(self) -> bool:
        return self.__italic

    @italic.setter
    def italic(self, italic: bool):
        self.__italic = italic

class notation_NamedStyle(Style):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class notation_MultiDiagramLinkStyle(Style):

    pass
class notation_TextStyle(Style):

    def __init__(self, textAlignment: str):
        self.textAlignment = textAlignment
        
    @property
    def textAlignment(self) -> str:
        return self.__textAlignment

    @textAlignment.setter
    def textAlignment(self, textAlignment: str):
        self.__textAlignment = textAlignment

class notation_PageStyle(Style):

    def __init__(self, pageX: int, pageY: int, pageWidth: int, pageHeight: int):
        self.pageX = pageX
        self.pageY = pageY
        self.pageWidth = pageWidth
        self.pageHeight = pageHeight
        
    @property
    def pageHeight(self) -> int:
        return self.__pageHeight

    @pageHeight.setter
    def pageHeight(self, pageHeight: int):
        self.__pageHeight = pageHeight

    @property
    def pageWidth(self) -> int:
        return self.__pageWidth

    @pageWidth.setter
    def pageWidth(self, pageWidth: int):
        self.__pageWidth = pageWidth

    @property
    def pageY(self) -> int:
        return self.__pageY

    @pageY.setter
    def pageY(self, pageY: int):
        self.__pageY = pageY

    @property
    def pageX(self) -> int:
        return self.__pageX

    @pageX.setter
    def pageX(self, pageX: int):
        self.__pageX = pageX

class notation_ImageStyle(Style):

    def __init__(self, antiAlias: str, maintainAspectRatio: str, notation_ImageStyle: "notation_Bounds" = None):
        self.antiAlias = antiAlias
        self.maintainAspectRatio = maintainAspectRatio
        self.notation_ImageStyle = notation_ImageStyle
        
    @property
    def antiAlias(self) -> str:
        return self.__antiAlias

    @antiAlias.setter
    def antiAlias(self, antiAlias: str):
        self.__antiAlias = antiAlias

    @property
    def maintainAspectRatio(self) -> str:
        return self.__maintainAspectRatio

    @maintainAspectRatio.setter
    def maintainAspectRatio(self, maintainAspectRatio: str):
        self.__maintainAspectRatio = maintainAspectRatio

    @property
    def notation_ImageStyle(self):
        return self.__notation_ImageStyle

    @notation_ImageStyle.setter
    def notation_ImageStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_ImageStyle__notation_ImageStyle", None)
        self.__notation_ImageStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Bounds"):
                opp_val = getattr(old_value, "notation_Bounds", None)
                if opp_val == self:
                    setattr(old_value, "notation_Bounds", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Bounds"):
                opp_val = getattr(value, "notation_Bounds", None)
                setattr(value, "notation_Bounds", self)

class notation_GuideStyle(Style):

    pass
class notation_DescriptionStyle(Style):

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class notation_FillStyle(Style):

    def __init__(self, fillColor: int, transparency: int, gradient: str):
        self.fillColor = fillColor
        self.transparency = transparency
        self.gradient = gradient
        
    @property
    def gradient(self) -> str:
        return self.__gradient

    @gradient.setter
    def gradient(self, gradient: str):
        self.__gradient = gradient

    @property
    def fillColor(self) -> int:
        return self.__fillColor

    @fillColor.setter
    def fillColor(self, fillColor: int):
        self.__fillColor = fillColor

    @property
    def transparency(self) -> int:
        return self.__transparency

    @transparency.setter
    def transparency(self, transparency: int):
        self.__transparency = transparency

class notation_Style(ABC):

    pass
class notation_LayoutConstraint(ABC):

    pass
class notation_Anchor(ABC):

    pass
class notation_Bendpoints(ABC):

    pass
class notation_View(EModelElement):

    def __init__(self, visible: bool, type: str, mutable: bool, View: "notation_Edge" = None, View2: "notation_Edge" = None, source: set["notation_Edge"] = None, target: set["notation_Edge"] = None, notation_View: set["notation_Node"] = None, notation_View17: set["notation_Style"] = None, notation_View19: "notation_EObject" = None, notation_View22: "notation_Diagram" = None, notation_View24: set["notation_Node"] = None):
        self.visible = visible
        self.type = type
        self.mutable = mutable
        self.View = View
        self.View2 = View2
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.notation_View = notation_View if notation_View is not None else set()
        self.notation_View17 = notation_View17 if notation_View17 is not None else set()
        self.notation_View19 = notation_View19
        self.notation_View22 = notation_View22
        self.notation_View24 = notation_View24 if notation_View24 is not None else set()
        
    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mutable(self) -> bool:
        return self.__mutable

    @mutable.setter
    def mutable(self, mutable: bool):
        self.__mutable = mutable

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    setattr(item, "Edge", self)
                    

    @property
    def notation_View24(self):
        return self.__notation_View24

    @notation_View24.setter
    def notation_View24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__notation_View24", None)
        self.__notation_View24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_Node25"):
                    opp_val = getattr(item, "notation_Node25", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_Node25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_Node25"):
                    opp_val = getattr(item, "notation_Node25", None)
                    
                    setattr(item, "notation_Node25", self)
                    

    @property
    def notation_View17(self):
        return self.__notation_View17

    @notation_View17.setter
    def notation_View17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__notation_View17", None)
        self.__notation_View17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_Style"):
                    opp_val = getattr(item, "notation_Style", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_Style", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_Style"):
                    opp_val = getattr(item, "notation_Style", None)
                    
                    setattr(item, "notation_Style", self)
                    

    @property
    def View2(self):
        return self.__View2

    @View2.setter
    def View2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__View2", None)
        self.__View2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetEdges"):
                opp_val = getattr(old_value, "targetEdges", None)
                if opp_val == self:
                    setattr(old_value, "targetEdges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetEdges"):
                opp_val = getattr(value, "targetEdges", None)
                setattr(value, "targetEdges", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge13"):
                    opp_val = getattr(item, "Edge13", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge13"):
                    opp_val = getattr(item, "Edge13", None)
                    
                    setattr(item, "Edge13", self)
                    

    @property
    def notation_View(self):
        return self.__notation_View

    @notation_View.setter
    def notation_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__notation_View", None)
        self.__notation_View = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_Node15"):
                    opp_val = getattr(item, "notation_Node15", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_Node15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_Node15"):
                    opp_val = getattr(item, "notation_Node15", None)
                    
                    setattr(item, "notation_Node15", self)
                    

    @property
    def notation_View22(self):
        return self.__notation_View22

    @notation_View22.setter
    def notation_View22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__notation_View22", None)
        self.__notation_View22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Diagram"):
                opp_val = getattr(old_value, "notation_Diagram", None)
                if opp_val == self:
                    setattr(old_value, "notation_Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Diagram"):
                opp_val = getattr(value, "notation_Diagram", None)
                setattr(value, "notation_Diagram", self)

    @property
    def notation_View19(self):
        return self.__notation_View19

    @notation_View19.setter
    def notation_View19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__notation_View19", None)
        self.__notation_View19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_EObject20"):
                opp_val = getattr(old_value, "notation_EObject20", None)
                if opp_val == self:
                    setattr(old_value, "notation_EObject20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_EObject20"):
                opp_val = getattr(value, "notation_EObject20", None)
                setattr(value, "notation_EObject20", self)

    @property
    def View(self):
        return self.__View

    @View.setter
    def View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__View", None)
        self.__View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceEdges"):
                opp_val = getattr(old_value, "sourceEdges", None)
                if opp_val == self:
                    setattr(old_value, "sourceEdges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceEdges"):
                opp_val = getattr(value, "sourceEdges", None)
                setattr(value, "sourceEdges", self)

    def createChild(self, eClass: str) -> str:
        # TODO: Implement createChild method
        pass

    def getNamedStyle(self, name: str, eClass: str) -> str:
        # TODO: Implement getNamedStyle method
        pass

    def getStyle(self, eClass: str) -> Style:
        # TODO: Implement getStyle method
        pass

    def createStyle(self, eClass: str) -> Style:
        # TODO: Implement createStyle method
        pass

class View:

    pass
class notation_Diagram(View):

    def __init__(self, name: str, measurementUnit: str, notation_Diagram: "notation_View" = None, notation_Diagram27: set["notation_Edge"] = None, notation_Diagram30: set["notation_Edge"] = None, notation_Diagram57: "notation_DiagramLinkStyle" = None, notation_Diagram59: "notation_MultiDiagramLinkStyle" = None):
        self.name = name
        self.measurementUnit = measurementUnit
        self.notation_Diagram = notation_Diagram
        self.notation_Diagram27 = notation_Diagram27 if notation_Diagram27 is not None else set()
        self.notation_Diagram30 = notation_Diagram30 if notation_Diagram30 is not None else set()
        self.notation_Diagram57 = notation_Diagram57
        self.notation_Diagram59 = notation_Diagram59
        
    @property
    def measurementUnit(self) -> str:
        return self.__measurementUnit

    @measurementUnit.setter
    def measurementUnit(self, measurementUnit: str):
        self.__measurementUnit = measurementUnit

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def notation_Diagram27(self):
        return self.__notation_Diagram27

    @notation_Diagram27.setter
    def notation_Diagram27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Diagram__notation_Diagram27", None)
        self.__notation_Diagram27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_Edge28"):
                    opp_val = getattr(item, "notation_Edge28", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_Edge28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_Edge28"):
                    opp_val = getattr(item, "notation_Edge28", None)
                    
                    setattr(item, "notation_Edge28", self)
                    

    @property
    def notation_Diagram57(self):
        return self.__notation_Diagram57

    @notation_Diagram57.setter
    def notation_Diagram57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Diagram__notation_Diagram57", None)
        self.__notation_Diagram57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_DiagramLinkStyle"):
                opp_val = getattr(old_value, "notation_DiagramLinkStyle", None)
                if opp_val == self:
                    setattr(old_value, "notation_DiagramLinkStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_DiagramLinkStyle"):
                opp_val = getattr(value, "notation_DiagramLinkStyle", None)
                setattr(value, "notation_DiagramLinkStyle", self)

    @property
    def notation_Diagram(self):
        return self.__notation_Diagram

    @notation_Diagram.setter
    def notation_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Diagram__notation_Diagram", None)
        self.__notation_Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_View22"):
                opp_val = getattr(old_value, "notation_View22", None)
                if opp_val == self:
                    setattr(old_value, "notation_View22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_View22"):
                opp_val = getattr(value, "notation_View22", None)
                setattr(value, "notation_View22", self)

    @property
    def notation_Diagram30(self):
        return self.__notation_Diagram30

    @notation_Diagram30.setter
    def notation_Diagram30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Diagram__notation_Diagram30", None)
        self.__notation_Diagram30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_Edge31"):
                    opp_val = getattr(item, "notation_Edge31", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_Edge31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_Edge31"):
                    opp_val = getattr(item, "notation_Edge31", None)
                    
                    setattr(item, "notation_Edge31", self)
                    

    @property
    def notation_Diagram59(self):
        return self.__notation_Diagram59

    @notation_Diagram59.setter
    def notation_Diagram59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Diagram__notation_Diagram59", None)
        self.__notation_Diagram59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_MultiDiagramLinkStyle"):
                opp_val = getattr(old_value, "notation_MultiDiagramLinkStyle", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_MultiDiagramLinkStyle"):
                opp_val = getattr(value, "notation_MultiDiagramLinkStyle", None)
                if opp_val is None:
                    setattr(value, "notation_MultiDiagramLinkStyle", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def createEdge(self, eClass: str) -> str:
        # TODO: Implement createEdge method
        pass

class notation_Node(View):

    def __init__(self, notation_Node: "notation_LayoutConstraint" = None, notation_Node15: "notation_View" = None, notation_Node25: "notation_View" = None, notation_Node40: "notation_NodeEntry" = None):
        self.notation_Node = notation_Node
        self.notation_Node15 = notation_Node15
        self.notation_Node25 = notation_Node25
        self.notation_Node40 = notation_Node40
        
    @property
    def notation_Node25(self):
        return self.__notation_Node25

    @notation_Node25.setter
    def notation_Node25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Node__notation_Node25", None)
        self.__notation_Node25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_View24"):
                opp_val = getattr(old_value, "notation_View24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_View24"):
                opp_val = getattr(value, "notation_View24", None)
                if opp_val is None:
                    setattr(value, "notation_View24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def notation_Node(self):
        return self.__notation_Node

    @notation_Node.setter
    def notation_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Node__notation_Node", None)
        self.__notation_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_LayoutConstraint"):
                opp_val = getattr(old_value, "notation_LayoutConstraint", None)
                if opp_val == self:
                    setattr(old_value, "notation_LayoutConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_LayoutConstraint"):
                opp_val = getattr(value, "notation_LayoutConstraint", None)
                setattr(value, "notation_LayoutConstraint", self)

    @property
    def notation_Node40(self):
        return self.__notation_Node40

    @notation_Node40.setter
    def notation_Node40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Node__notation_Node40", None)
        self.__notation_Node40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_NodeEntry39"):
                opp_val = getattr(old_value, "notation_NodeEntry39", None)
                if opp_val == self:
                    setattr(old_value, "notation_NodeEntry39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_NodeEntry39"):
                opp_val = getattr(value, "notation_NodeEntry39", None)
                setattr(value, "notation_NodeEntry39", self)

    @property
    def notation_Node15(self):
        return self.__notation_Node15

    @notation_Node15.setter
    def notation_Node15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Node__notation_Node15", None)
        self.__notation_Node15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_View"):
                opp_val = getattr(old_value, "notation_View", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_View"):
                opp_val = getattr(value, "notation_View", None)
                if opp_val is None:
                    setattr(value, "notation_View", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def createLayoutConstraint(self, eClass: str) -> str:
        # TODO: Implement createLayoutConstraint method
        pass

class notation_Edge(View):

    def __init__(self, sourceEdges: "notation_View" = None, targetEdges: "notation_View" = None, notation_Edge: "notation_Bendpoints" = None, notation_Edge5: "notation_Anchor" = None, notation_Edge7: "notation_Anchor" = None, Edge: "notation_View" = None, Edge13: "notation_View" = None, notation_Edge28: "notation_Diagram" = None, notation_Edge31: "notation_Diagram" = None):
        self.sourceEdges = sourceEdges
        self.targetEdges = targetEdges
        self.notation_Edge = notation_Edge
        self.notation_Edge5 = notation_Edge5
        self.notation_Edge7 = notation_Edge7
        self.Edge = Edge
        self.Edge13 = Edge13
        self.notation_Edge28 = notation_Edge28
        self.notation_Edge31 = notation_Edge31
        
    @property
    def notation_Edge(self):
        return self.__notation_Edge

    @notation_Edge.setter
    def notation_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Edge__notation_Edge", None)
        self.__notation_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Bendpoints"):
                opp_val = getattr(old_value, "notation_Bendpoints", None)
                if opp_val == self:
                    setattr(old_value, "notation_Bendpoints", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Bendpoints"):
                opp_val = getattr(value, "notation_Bendpoints", None)
                setattr(value, "notation_Bendpoints", self)

    @property
    def notation_Edge7(self):
        return self.__notation_Edge7

    @notation_Edge7.setter
    def notation_Edge7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Edge__notation_Edge7", None)
        self.__notation_Edge7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Anchor8"):
                opp_val = getattr(old_value, "notation_Anchor8", None)
                if opp_val == self:
                    setattr(old_value, "notation_Anchor8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Anchor8"):
                opp_val = getattr(value, "notation_Anchor8", None)
                setattr(value, "notation_Anchor8", self)

    @property
    def sourceEdges(self):
        return self.__sourceEdges

    @sourceEdges.setter
    def sourceEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Edge__sourceEdges", None)
        self.__sourceEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "View"):
                opp_val = getattr(old_value, "View", None)
                if opp_val == self:
                    setattr(old_value, "View", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "View"):
                opp_val = getattr(value, "View", None)
                setattr(value, "View", self)

    @property
    def notation_Edge28(self):
        return self.__notation_Edge28

    @notation_Edge28.setter
    def notation_Edge28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Edge__notation_Edge28", None)
        self.__notation_Edge28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Diagram27"):
                opp_val = getattr(old_value, "notation_Diagram27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Diagram27"):
                opp_val = getattr(value, "notation_Diagram27", None)
                if opp_val is None:
                    setattr(value, "notation_Diagram27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def targetEdges(self):
        return self.__targetEdges

    @targetEdges.setter
    def targetEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Edge__targetEdges", None)
        self.__targetEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "View2"):
                opp_val = getattr(old_value, "View2", None)
                if opp_val == self:
                    setattr(old_value, "View2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "View2"):
                opp_val = getattr(value, "View2", None)
                setattr(value, "View2", self)

    @property
    def notation_Edge5(self):
        return self.__notation_Edge5

    @notation_Edge5.setter
    def notation_Edge5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Edge__notation_Edge5", None)
        self.__notation_Edge5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Anchor"):
                opp_val = getattr(old_value, "notation_Anchor", None)
                if opp_val == self:
                    setattr(old_value, "notation_Anchor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Anchor"):
                opp_val = getattr(value, "notation_Anchor", None)
                setattr(value, "notation_Anchor", self)

    @property
    def notation_Edge31(self):
        return self.__notation_Edge31

    @notation_Edge31.setter
    def notation_Edge31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Edge__notation_Edge31", None)
        self.__notation_Edge31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Diagram30"):
                opp_val = getattr(old_value, "notation_Diagram30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Diagram30"):
                opp_val = getattr(value, "notation_Diagram30", None)
                if opp_val is None:
                    setattr(value, "notation_Diagram30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Edge13(self):
        return self.__Edge13

    @Edge13.setter
    def Edge13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Edge__Edge13", None)
        self.__Edge13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def createBendpoints(self, eClass: str) -> str:
        # TODO: Implement createBendpoints method
        pass

    def createTargetAnchor(self, eClass: str) -> str:
        # TODO: Implement createTargetAnchor method
        pass

    def createSourceAnchor(self, eClass: str) -> str:
        # TODO: Implement createSourceAnchor method
        pass
