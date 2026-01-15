from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VariabilityType(Enum):
    na = "na"
    replaces = "replaces"
    localContribution = "localContribution"
    localReplacement = "localReplacement"
    extendsReplaces = "extendsReplaces"
    contributes = "contributes"
    extends = "extends"
class WorkOrderType(Enum):
    finishToFinish = "finishToFinish"
    startToStart = "startToStart"
    startToFinish = "startToFinish"
    finishToStart = "finishToStart"


############################################
# Definition of Classes
############################################

class LeafElement:

    pass
class uma_Image(LeafElement):

    def __init__(self, uri: str, mimeType: str):
        self.uri = uri
        self.mimeType = mimeType
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def mimeType(self) -> str:
        return self.__mimeType

    @mimeType.setter
    def mimeType(self, mimeType: str):
        self.__mimeType = mimeType

class uma_TextElement(LeafElement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class MethodConfiguration:

    pass
class uma_ProcessFamily(MethodConfiguration):

    pass
class GraphicPrimitive:

    pass
class uma_Ellipse(GraphicPrimitive):

    def __init__(self, radiusX: str, radiusY: str, rotation: str, startAngle: str, endAngle: str, uma_Ellipse: "uma_Point" = None):
        self.radiusX = radiusX
        self.radiusY = radiusY
        self.rotation = rotation
        self.startAngle = startAngle
        self.endAngle = endAngle
        self.uma_Ellipse = uma_Ellipse
        
    @property
    def startAngle(self) -> str:
        return self.__startAngle

    @startAngle.setter
    def startAngle(self, startAngle: str):
        self.__startAngle = startAngle

    @property
    def endAngle(self) -> str:
        return self.__endAngle

    @endAngle.setter
    def endAngle(self, endAngle: str):
        self.__endAngle = endAngle

    @property
    def radiusY(self) -> str:
        return self.__radiusY

    @radiusY.setter
    def radiusY(self, radiusY: str):
        self.__radiusY = radiusY

    @property
    def rotation(self) -> str:
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation

    @property
    def radiusX(self) -> str:
        return self.__radiusX

    @radiusX.setter
    def radiusX(self, radiusX: str):
        self.__radiusX = radiusX

    @property
    def uma_Ellipse(self):
        return self.__uma_Ellipse

    @uma_Ellipse.setter
    def uma_Ellipse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Ellipse__uma_Ellipse", None)
        self.__uma_Ellipse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Point319"):
                opp_val = getattr(old_value, "uma_Point319", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point319"):
                opp_val = getattr(value, "uma_Point319", None)
                setattr(value, "uma_Point319", self)

class uma_Polyline(GraphicPrimitive):

    def __init__(self, closed: str, uma_Polyline: set["uma_Point"] = None):
        self.closed = closed
        self.uma_Polyline = uma_Polyline if uma_Polyline is not None else set()
        
    @property
    def closed(self) -> str:
        return self.__closed

    @closed.setter
    def closed(self, closed: str):
        self.__closed = closed

    @property
    def uma_Polyline(self):
        return self.__uma_Polyline

    @uma_Polyline.setter
    def uma_Polyline(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Polyline__uma_Polyline", None)
        self.__uma_Polyline = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Point317"):
                    opp_val = getattr(item, "uma_Point317", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Point317", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Point317"):
                    opp_val = getattr(item, "uma_Point317", None)
                    
                    setattr(item, "uma_Point317", self)
                    

class uma_GraphicPrimitive(LeafElement):

    pass
class SemanticModelBridge:

    pass
class uma_CoreSemanticModelBridge(SemanticModelBridge):

    pass
class uma_UMASemanticModelBridge(SemanticModelBridge):

    pass
class uma_SimpleSemanticModelElement(SemanticModelBridge):

    def __init__(self, typeInfo: str):
        self.typeInfo = typeInfo
        
    @property
    def typeInfo(self) -> str:
        return self.__typeInfo

    @typeInfo.setter
    def typeInfo(self, typeInfo: str):
        self.__typeInfo = typeInfo

class GraphNode:

    pass
class DiagramElement:

    pass
class uma_Reference(DiagramElement):

    def __init__(self, isIndividualRepresentation: str, Reference: "uma_DiagramElement" = None, reference: "uma_DiagramElement" = None):
        self.isIndividualRepresentation = isIndividualRepresentation
        self.Reference = Reference
        self.reference = reference
        
    @property
    def isIndividualRepresentation(self) -> str:
        return self.__isIndividualRepresentation

    @isIndividualRepresentation.setter
    def isIndividualRepresentation(self, isIndividualRepresentation: str):
        self.__isIndividualRepresentation = isIndividualRepresentation

    @property
    def reference(self):
        return self.__reference

    @reference.setter
    def reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Reference__reference", None)
        self.__reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramElement290"):
                opp_val = getattr(old_value, "DiagramElement290", None)
                if opp_val == self:
                    setattr(old_value, "DiagramElement290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramElement290"):
                opp_val = getattr(value, "DiagramElement290", None)
                setattr(value, "DiagramElement290", self)

    @property
    def Reference(self):
        return self.__Reference

    @Reference.setter
    def Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Reference__Reference", None)
        self.__Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "referenced"):
                opp_val = getattr(old_value, "referenced", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "referenced"):
                opp_val = getattr(value, "referenced", None)
                if opp_val is None:
                    setattr(value, "referenced", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_SemanticModelBridge(DiagramElement):

    def __init__(self, presentation: str, SemanticModelBridge285: "uma_GraphElement" = None, SemanticModelBridge: "uma_Diagram" = None, namespace: "uma_Diagram" = None, semanticModel: "uma_GraphElement" = None):
        self.presentation = presentation
        self.SemanticModelBridge285 = SemanticModelBridge285
        self.SemanticModelBridge = SemanticModelBridge
        self.namespace = namespace
        self.semanticModel = semanticModel
        
    @property
    def presentation(self) -> str:
        return self.__presentation

    @presentation.setter
    def presentation(self, presentation: str):
        self.__presentation = presentation

    @property
    def SemanticModelBridge285(self):
        return self.__SemanticModelBridge285

    @SemanticModelBridge285.setter
    def SemanticModelBridge285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_SemanticModelBridge__SemanticModelBridge285", None)
        self.__SemanticModelBridge285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphElement284"):
                opp_val = getattr(old_value, "graphElement284", None)
                if opp_val == self:
                    setattr(old_value, "graphElement284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphElement284"):
                opp_val = getattr(value, "graphElement284", None)
                setattr(value, "graphElement284", self)

    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_SemanticModelBridge__namespace", None)
        self.__namespace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Diagram304"):
                opp_val = getattr(old_value, "Diagram304", None)
                if opp_val == self:
                    setattr(old_value, "Diagram304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Diagram304"):
                opp_val = getattr(value, "Diagram304", None)
                setattr(value, "Diagram304", self)

    @property
    def semanticModel(self):
        return self.__semanticModel

    @semanticModel.setter
    def semanticModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_SemanticModelBridge__semanticModel", None)
        self.__semanticModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphElement306"):
                opp_val = getattr(old_value, "GraphElement306", None)
                if opp_val == self:
                    setattr(old_value, "GraphElement306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphElement306"):
                opp_val = getattr(value, "GraphElement306", None)
                setattr(value, "GraphElement306", self)

    @property
    def SemanticModelBridge(self):
        return self.__SemanticModelBridge

    @SemanticModelBridge.setter
    def SemanticModelBridge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_SemanticModelBridge__SemanticModelBridge", None)
        self.__SemanticModelBridge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram272"):
                opp_val = getattr(old_value, "diagram272", None)
                if opp_val == self:
                    setattr(old_value, "diagram272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram272"):
                opp_val = getattr(value, "diagram272", None)
                setattr(value, "diagram272", self)

class uma_LeafElement(DiagramElement):

    pass
class uma_Property(DiagramElement):

    def __init__(self, key: str, value: str, uma_Property: "uma_DiagramElement" = None):
        self.key = key
        self.value = value
        self.uma_Property = uma_Property
        
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
    def uma_Property(self):
        return self.__uma_Property

    @uma_Property.setter
    def uma_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Property__uma_Property", None)
        self.__uma_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_DiagramElement"):
                opp_val = getattr(old_value, "uma_DiagramElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_DiagramElement"):
                opp_val = getattr(value, "uma_DiagramElement", None)
                if opp_val is None:
                    setattr(value, "uma_DiagramElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_DiagramLink(DiagramElement):

    def __init__(self, zoom: str, DiagramLink280: "uma_GraphElement" = None, DiagramLink: "uma_Diagram" = None, link: "uma_GraphElement" = None, uma_DiagramLink: "uma_Point" = None, diagramLink: "uma_Diagram" = None):
        self.zoom = zoom
        self.DiagramLink280 = DiagramLink280
        self.DiagramLink = DiagramLink
        self.link = link
        self.uma_DiagramLink = uma_DiagramLink
        self.diagramLink = diagramLink
        
    @property
    def zoom(self) -> str:
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom

    @property
    def DiagramLink280(self):
        return self.__DiagramLink280

    @DiagramLink280.setter
    def DiagramLink280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__DiagramLink280", None)
        self.__DiagramLink280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphElement"):
                opp_val = getattr(old_value, "graphElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphElement"):
                opp_val = getattr(value, "graphElement", None)
                if opp_val is None:
                    setattr(value, "graphElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DiagramLink(self):
        return self.__DiagramLink

    @DiagramLink.setter
    def DiagramLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__DiagramLink", None)
        self.__DiagramLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram"):
                opp_val = getattr(old_value, "diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram"):
                opp_val = getattr(value, "diagram", None)
                if opp_val is None:
                    setattr(value, "diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagramLink(self):
        return self.__diagramLink

    @diagramLink.setter
    def diagramLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__diagramLink", None)
        self.__diagramLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Diagram"):
                opp_val = getattr(old_value, "Diagram", None)
                if opp_val == self:
                    setattr(old_value, "Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Diagram"):
                opp_val = getattr(value, "Diagram", None)
                setattr(value, "Diagram", self)

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__link", None)
        self.__link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphElement295"):
                opp_val = getattr(old_value, "GraphElement295", None)
                if opp_val == self:
                    setattr(old_value, "GraphElement295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphElement295"):
                opp_val = getattr(value, "GraphElement295", None)
                setattr(value, "GraphElement295", self)

    @property
    def uma_DiagramLink(self):
        return self.__uma_DiagramLink

    @uma_DiagramLink.setter
    def uma_DiagramLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramLink__uma_DiagramLink", None)
        self.__uma_DiagramLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Point292"):
                opp_val = getattr(old_value, "uma_Point292", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point292"):
                opp_val = getattr(value, "uma_Point292", None)
                setattr(value, "uma_Point292", self)

class uma_GraphElement(DiagramElement):

    pass
class uma_Dimension:

    def __init__(self, width: str, height: str, uma_Dimension: "uma_GraphNode" = None):
        self.width = width
        self.height = height
        self.uma_Dimension = uma_Dimension
        
    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def uma_Dimension(self):
        return self.__uma_Dimension

    @uma_Dimension.setter
    def uma_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Dimension__uma_Dimension", None)
        self.__uma_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_GraphNode"):
                opp_val = getattr(old_value, "uma_GraphNode", None)
                if opp_val == self:
                    setattr(old_value, "uma_GraphNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_GraphNode"):
                opp_val = getattr(value, "uma_GraphNode", None)
                setattr(value, "uma_GraphNode", self)

class GraphElement:

    pass
class uma_GraphConnector(GraphElement):

    pass
class uma_GraphEdge(GraphElement):

    pass
class uma_GraphNode(GraphElement):

    pass
class uma_Point:

    def __init__(self, x: str, y: str, uma_Point: "uma_Diagram" = None, uma_Point278: "uma_GraphElement" = None, uma_Point300: "uma_GraphEdge" = None, uma_Point292: "uma_DiagramLink" = None, uma_Point317: "uma_Polyline" = None, uma_Point319: "uma_Ellipse" = None):
        self.x = x
        self.y = y
        self.uma_Point = uma_Point
        self.uma_Point278 = uma_Point278
        self.uma_Point300 = uma_Point300
        self.uma_Point292 = uma_Point292
        self.uma_Point317 = uma_Point317
        self.uma_Point319 = uma_Point319
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def uma_Point300(self):
        return self.__uma_Point300

    @uma_Point300.setter
    def uma_Point300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point300", None)
        self.__uma_Point300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_GraphEdge"):
                opp_val = getattr(old_value, "uma_GraphEdge", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_GraphEdge"):
                opp_val = getattr(value, "uma_GraphEdge", None)
                if opp_val is None:
                    setattr(value, "uma_GraphEdge", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Point(self):
        return self.__uma_Point

    @uma_Point.setter
    def uma_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point", None)
        self.__uma_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Diagram274"):
                opp_val = getattr(old_value, "uma_Diagram274", None)
                if opp_val == self:
                    setattr(old_value, "uma_Diagram274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Diagram274"):
                opp_val = getattr(value, "uma_Diagram274", None)
                setattr(value, "uma_Diagram274", self)

    @property
    def uma_Point317(self):
        return self.__uma_Point317

    @uma_Point317.setter
    def uma_Point317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point317", None)
        self.__uma_Point317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Polyline"):
                opp_val = getattr(old_value, "uma_Polyline", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Polyline"):
                opp_val = getattr(value, "uma_Polyline", None)
                if opp_val is None:
                    setattr(value, "uma_Polyline", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Point278(self):
        return self.__uma_Point278

    @uma_Point278.setter
    def uma_Point278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point278", None)
        self.__uma_Point278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_GraphElement"):
                opp_val = getattr(old_value, "uma_GraphElement", None)
                if opp_val == self:
                    setattr(old_value, "uma_GraphElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_GraphElement"):
                opp_val = getattr(value, "uma_GraphElement", None)
                setattr(value, "uma_GraphElement", self)

    @property
    def uma_Point319(self):
        return self.__uma_Point319

    @uma_Point319.setter
    def uma_Point319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point319", None)
        self.__uma_Point319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Ellipse"):
                opp_val = getattr(old_value, "uma_Ellipse", None)
                if opp_val == self:
                    setattr(old_value, "uma_Ellipse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Ellipse"):
                opp_val = getattr(value, "uma_Ellipse", None)
                setattr(value, "uma_Ellipse", self)

    @property
    def uma_Point292(self):
        return self.__uma_Point292

    @uma_Point292.setter
    def uma_Point292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Point__uma_Point292", None)
        self.__uma_Point292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_DiagramLink"):
                opp_val = getattr(old_value, "uma_DiagramLink", None)
                if opp_val == self:
                    setattr(old_value, "uma_DiagramLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_DiagramLink"):
                opp_val = getattr(value, "uma_DiagramLink", None)
                setattr(value, "uma_DiagramLink", self)

class uma_Diagram(GraphNode):

    def __init__(self, zoom: str, uma_Diagram: "uma_ProcessPackage" = None, uma_Diagram274: "uma_Point" = None, diagram: set["uma_DiagramLink"] = None, diagram272: "uma_SemanticModelBridge" = None, Diagram304: "uma_SemanticModelBridge" = None, Diagram: "uma_DiagramLink" = None):
        self.zoom = zoom
        self.uma_Diagram = uma_Diagram
        self.uma_Diagram274 = uma_Diagram274
        self.diagram = diagram if diagram is not None else set()
        self.diagram272 = diagram272
        self.Diagram304 = Diagram304
        self.Diagram = Diagram
        
    @property
    def zoom(self) -> str:
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom

    @property
    def uma_Diagram274(self):
        return self.__uma_Diagram274

    @uma_Diagram274.setter
    def uma_Diagram274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__uma_Diagram274", None)
        self.__uma_Diagram274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Point"):
                opp_val = getattr(old_value, "uma_Point", None)
                if opp_val == self:
                    setattr(old_value, "uma_Point", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Point"):
                opp_val = getattr(value, "uma_Point", None)
                setattr(value, "uma_Point", self)

    @property
    def diagram272(self):
        return self.__diagram272

    @diagram272.setter
    def diagram272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__diagram272", None)
        self.__diagram272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SemanticModelBridge"):
                opp_val = getattr(old_value, "SemanticModelBridge", None)
                if opp_val == self:
                    setattr(old_value, "SemanticModelBridge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SemanticModelBridge"):
                opp_val = getattr(value, "SemanticModelBridge", None)
                setattr(value, "SemanticModelBridge", self)

    @property
    def uma_Diagram(self):
        return self.__uma_Diagram

    @uma_Diagram.setter
    def uma_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__uma_Diagram", None)
        self.__uma_Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessPackage269"):
                opp_val = getattr(old_value, "uma_ProcessPackage269", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessPackage269"):
                opp_val = getattr(value, "uma_ProcessPackage269", None)
                if opp_val is None:
                    setattr(value, "uma_ProcessPackage269", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Diagram(self):
        return self.__Diagram

    @Diagram.setter
    def Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__Diagram", None)
        self.__Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagramLink"):
                opp_val = getattr(old_value, "diagramLink", None)
                if opp_val == self:
                    setattr(old_value, "diagramLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagramLink"):
                opp_val = getattr(value, "diagramLink", None)
                setattr(value, "diagramLink", self)

    @property
    def Diagram304(self):
        return self.__Diagram304

    @Diagram304.setter
    def Diagram304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__Diagram304", None)
        self.__Diagram304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "namespace"):
                opp_val = getattr(old_value, "namespace", None)
                if opp_val == self:
                    setattr(old_value, "namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "namespace"):
                opp_val = getattr(value, "namespace", None)
                setattr(value, "namespace", self)

    @property
    def diagram(self):
        return self.__diagram

    @diagram.setter
    def diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Diagram__diagram", None)
        self.__diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramLink"):
                    opp_val = getattr(item, "DiagramLink", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramLink"):
                    opp_val = getattr(item, "DiagramLink", None)
                    
                    setattr(item, "DiagramLink", self)
                    

class ProcessPackage:

    pass
class ActivityDescription:

    pass
class uma_ProcessDescription(ActivityDescription):

    def __init__(self, scope: str, usageNotes: str):
        self.scope = scope
        self.usageNotes = usageNotes
        
    @property
    def usageNotes(self) -> str:
        return self.__usageNotes

    @usageNotes.setter
    def usageNotes(self, usageNotes: str):
        self.__usageNotes = usageNotes

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

class ProcessDescription:

    pass
class uma_DeliveryProcessDescription(ProcessDescription):

    def __init__(self, scale: str, projectCharacteristics: str, riskLevel: str, estimatingTechnique: str, projectMemberExpertise: str, typeOfContract: str):
        self.scale = scale
        self.projectCharacteristics = projectCharacteristics
        self.riskLevel = riskLevel
        self.estimatingTechnique = estimatingTechnique
        self.projectMemberExpertise = projectMemberExpertise
        self.typeOfContract = typeOfContract
        
    @property
    def projectCharacteristics(self) -> str:
        return self.__projectCharacteristics

    @projectCharacteristics.setter
    def projectCharacteristics(self, projectCharacteristics: str):
        self.__projectCharacteristics = projectCharacteristics

    @property
    def riskLevel(self) -> str:
        return self.__riskLevel

    @riskLevel.setter
    def riskLevel(self, riskLevel: str):
        self.__riskLevel = riskLevel

    @property
    def estimatingTechnique(self) -> str:
        return self.__estimatingTechnique

    @estimatingTechnique.setter
    def estimatingTechnique(self, estimatingTechnique: str):
        self.__estimatingTechnique = estimatingTechnique

    @property
    def projectMemberExpertise(self) -> str:
        return self.__projectMemberExpertise

    @projectMemberExpertise.setter
    def projectMemberExpertise(self, projectMemberExpertise: str):
        self.__projectMemberExpertise = projectMemberExpertise

    @property
    def typeOfContract(self) -> str:
        return self.__typeOfContract

    @typeOfContract.setter
    def typeOfContract(self, typeOfContract: str):
        self.__typeOfContract = typeOfContract

    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

class BreakdownElementDescription:

    pass
class uma_DescriptorDescription(BreakdownElementDescription):

    def __init__(self, refinedDescription: str):
        self.refinedDescription = refinedDescription
        
    @property
    def refinedDescription(self) -> str:
        return self.__refinedDescription

    @refinedDescription.setter
    def refinedDescription(self, refinedDescription: str):
        self.__refinedDescription = refinedDescription

class uma_ActivityDescription(BreakdownElementDescription):

    def __init__(self, purpose: str, alternatives: str, howtoStaff: str):
        self.purpose = purpose
        self.alternatives = alternatives
        self.howtoStaff = howtoStaff
        
    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

    @property
    def alternatives(self) -> str:
        return self.__alternatives

    @alternatives.setter
    def alternatives(self, alternatives: str):
        self.__alternatives = alternatives

    @property
    def howtoStaff(self) -> str:
        return self.__howtoStaff

    @howtoStaff.setter
    def howtoStaff(self, howtoStaff: str):
        self.__howtoStaff = howtoStaff

class Process:

    pass
class uma_CapabilityPattern(Process):

    pass
class uma_ProcessPlanningTemplate(Process):

    pass
class uma_DeliveryProcess(Process):

    pass
class RoleDescriptor:

    pass
class uma_CompositeRole(RoleDescriptor):

    pass
class MethodPackage:

    pass
class uma_ProcessPackage(MethodPackage):

    pass
class uma_ContentPackage(MethodPackage):

    pass
class Activity:

    pass
class uma_Process(Activity):

    pass
class uma_Phase(Activity):

    pass
class uma_Iteration(Activity):

    pass
class Descriptor:

    pass
class uma_RoleDescriptor(Descriptor):

    pass
class uma_ProcessComponentDescriptor(Descriptor):

    pass
class uma_WorkProductDescriptor(Descriptor):

    def __init__(self, activityEntryState: str, activityExitState: str, uma_WorkProductDescriptor: "uma_Milestone" = None, uma_WorkProductDescriptor161: "uma_WorkProduct" = None, WorkProductDescriptor: "uma_WorkProductDescriptor" = None, impacts: set["uma_WorkProductDescriptor"] = None, WorkProductDescriptor167: "uma_WorkProductDescriptor" = None, impactedBy: set["uma_WorkProductDescriptor"] = None, uma_WorkProductDescriptor170: "uma_WorkProductDescriptor" = None, uma_WorkProductDescriptor168: set["uma_WorkProductDescriptor"] = None, uma_WorkProductDescriptor182: "uma_RoleDescriptor" = None, uma_WorkProductDescriptor185: "uma_RoleDescriptor" = None, uma_WorkProductDescriptor196: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor199: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor202: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor205: "uma_TaskDescriptor" = None, uma_WorkProductDescriptor312: "uma_ProcessComponentInterface" = None):
        self.activityEntryState = activityEntryState
        self.activityExitState = activityExitState
        self.uma_WorkProductDescriptor = uma_WorkProductDescriptor
        self.uma_WorkProductDescriptor161 = uma_WorkProductDescriptor161
        self.WorkProductDescriptor = WorkProductDescriptor
        self.impacts = impacts if impacts is not None else set()
        self.WorkProductDescriptor167 = WorkProductDescriptor167
        self.impactedBy = impactedBy if impactedBy is not None else set()
        self.uma_WorkProductDescriptor170 = uma_WorkProductDescriptor170
        self.uma_WorkProductDescriptor168 = uma_WorkProductDescriptor168 if uma_WorkProductDescriptor168 is not None else set()
        self.uma_WorkProductDescriptor182 = uma_WorkProductDescriptor182
        self.uma_WorkProductDescriptor185 = uma_WorkProductDescriptor185
        self.uma_WorkProductDescriptor196 = uma_WorkProductDescriptor196
        self.uma_WorkProductDescriptor199 = uma_WorkProductDescriptor199
        self.uma_WorkProductDescriptor202 = uma_WorkProductDescriptor202
        self.uma_WorkProductDescriptor205 = uma_WorkProductDescriptor205
        self.uma_WorkProductDescriptor312 = uma_WorkProductDescriptor312
        
    @property
    def activityExitState(self) -> str:
        return self.__activityExitState

    @activityExitState.setter
    def activityExitState(self, activityExitState: str):
        self.__activityExitState = activityExitState

    @property
    def activityEntryState(self) -> str:
        return self.__activityEntryState

    @activityEntryState.setter
    def activityEntryState(self, activityEntryState: str):
        self.__activityEntryState = activityEntryState

    @property
    def impactedBy(self):
        return self.__impactedBy

    @impactedBy.setter
    def impactedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__impactedBy", None)
        self.__impactedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkProductDescriptor167"):
                    opp_val = getattr(item, "WorkProductDescriptor167", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkProductDescriptor167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkProductDescriptor167"):
                    opp_val = getattr(item, "WorkProductDescriptor167", None)
                    
                    setattr(item, "WorkProductDescriptor167", self)
                    

    @property
    def impacts(self):
        return self.__impacts

    @impacts.setter
    def impacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__impacts", None)
        self.__impacts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkProductDescriptor"):
                    opp_val = getattr(item, "WorkProductDescriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkProductDescriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkProductDescriptor"):
                    opp_val = getattr(item, "WorkProductDescriptor", None)
                    
                    setattr(item, "WorkProductDescriptor", self)
                    

    @property
    def uma_WorkProductDescriptor312(self):
        return self.__uma_WorkProductDescriptor312

    @uma_WorkProductDescriptor312.setter
    def uma_WorkProductDescriptor312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor312", None)
        self.__uma_WorkProductDescriptor312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ProcessComponentInterface311"):
                opp_val = getattr(old_value, "uma_ProcessComponentInterface311", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ProcessComponentInterface311"):
                opp_val = getattr(value, "uma_ProcessComponentInterface311", None)
                if opp_val is None:
                    setattr(value, "uma_ProcessComponentInterface311", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor205(self):
        return self.__uma_WorkProductDescriptor205

    @uma_WorkProductDescriptor205.setter
    def uma_WorkProductDescriptor205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor205", None)
        self.__uma_WorkProductDescriptor205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor204"):
                opp_val = getattr(old_value, "uma_TaskDescriptor204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor204"):
                opp_val = getattr(value, "uma_TaskDescriptor204", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor202(self):
        return self.__uma_WorkProductDescriptor202

    @uma_WorkProductDescriptor202.setter
    def uma_WorkProductDescriptor202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor202", None)
        self.__uma_WorkProductDescriptor202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor201"):
                opp_val = getattr(old_value, "uma_TaskDescriptor201", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor201"):
                opp_val = getattr(value, "uma_TaskDescriptor201", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor201", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor196(self):
        return self.__uma_WorkProductDescriptor196

    @uma_WorkProductDescriptor196.setter
    def uma_WorkProductDescriptor196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor196", None)
        self.__uma_WorkProductDescriptor196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor195"):
                opp_val = getattr(old_value, "uma_TaskDescriptor195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor195"):
                opp_val = getattr(value, "uma_TaskDescriptor195", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor195", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor185(self):
        return self.__uma_WorkProductDescriptor185

    @uma_WorkProductDescriptor185.setter
    def uma_WorkProductDescriptor185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor185", None)
        self.__uma_WorkProductDescriptor185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_RoleDescriptor184"):
                opp_val = getattr(old_value, "uma_RoleDescriptor184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_RoleDescriptor184"):
                opp_val = getattr(value, "uma_RoleDescriptor184", None)
                if opp_val is None:
                    setattr(value, "uma_RoleDescriptor184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor168(self):
        return self.__uma_WorkProductDescriptor168

    @uma_WorkProductDescriptor168.setter
    def uma_WorkProductDescriptor168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor168", None)
        self.__uma_WorkProductDescriptor168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_WorkProductDescriptor170"):
                    opp_val = getattr(item, "uma_WorkProductDescriptor170", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_WorkProductDescriptor170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_WorkProductDescriptor170"):
                    opp_val = getattr(item, "uma_WorkProductDescriptor170", None)
                    
                    setattr(item, "uma_WorkProductDescriptor170", self)
                    

    @property
    def uma_WorkProductDescriptor161(self):
        return self.__uma_WorkProductDescriptor161

    @uma_WorkProductDescriptor161.setter
    def uma_WorkProductDescriptor161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor161", None)
        self.__uma_WorkProductDescriptor161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkProduct162"):
                opp_val = getattr(old_value, "uma_WorkProduct162", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkProduct162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkProduct162"):
                opp_val = getattr(value, "uma_WorkProduct162", None)
                setattr(value, "uma_WorkProduct162", self)

    @property
    def uma_WorkProductDescriptor199(self):
        return self.__uma_WorkProductDescriptor199

    @uma_WorkProductDescriptor199.setter
    def uma_WorkProductDescriptor199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor199", None)
        self.__uma_WorkProductDescriptor199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor198"):
                opp_val = getattr(old_value, "uma_TaskDescriptor198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor198"):
                opp_val = getattr(value, "uma_TaskDescriptor198", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorkProductDescriptor(self):
        return self.__WorkProductDescriptor

    @WorkProductDescriptor.setter
    def WorkProductDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__WorkProductDescriptor", None)
        self.__WorkProductDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "impacts"):
                opp_val = getattr(old_value, "impacts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "impacts"):
                opp_val = getattr(value, "impacts", None)
                if opp_val is None:
                    setattr(value, "impacts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor170(self):
        return self.__uma_WorkProductDescriptor170

    @uma_WorkProductDescriptor170.setter
    def uma_WorkProductDescriptor170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor170", None)
        self.__uma_WorkProductDescriptor170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkProductDescriptor168"):
                opp_val = getattr(old_value, "uma_WorkProductDescriptor168", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkProductDescriptor168"):
                opp_val = getattr(value, "uma_WorkProductDescriptor168", None)
                if opp_val is None:
                    setattr(value, "uma_WorkProductDescriptor168", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorkProductDescriptor167(self):
        return self.__WorkProductDescriptor167

    @WorkProductDescriptor167.setter
    def WorkProductDescriptor167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__WorkProductDescriptor167", None)
        self.__WorkProductDescriptor167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "impactedBy"):
                opp_val = getattr(old_value, "impactedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "impactedBy"):
                opp_val = getattr(value, "impactedBy", None)
                if opp_val is None:
                    setattr(value, "impactedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor(self):
        return self.__uma_WorkProductDescriptor

    @uma_WorkProductDescriptor.setter
    def uma_WorkProductDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor", None)
        self.__uma_WorkProductDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Milestone"):
                opp_val = getattr(old_value, "uma_Milestone", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Milestone"):
                opp_val = getattr(value, "uma_Milestone", None)
                if opp_val is None:
                    setattr(value, "uma_Milestone", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_WorkProductDescriptor182(self):
        return self.__uma_WorkProductDescriptor182

    @uma_WorkProductDescriptor182.setter
    def uma_WorkProductDescriptor182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkProductDescriptor__uma_WorkProductDescriptor182", None)
        self.__uma_WorkProductDescriptor182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_RoleDescriptor181"):
                opp_val = getattr(old_value, "uma_RoleDescriptor181", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_RoleDescriptor181"):
                opp_val = getattr(value, "uma_RoleDescriptor181", None)
                if opp_val is None:
                    setattr(value, "uma_RoleDescriptor181", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Package:

    pass
class WorkBreakdownElement:

    pass
class uma_TaskDescriptor(WorkBreakdownElement, Descriptor):

    pass
class uma_Milestone(WorkBreakdownElement):

    pass
class ProcessElement:

    pass
class uma_BreakdownElement(ProcessElement):

    def __init__(self, prefix: str, isPlanned: str, hasMultipleOccurrences: str, isOptional: str, uma_BreakdownElement: "uma_BreakdownElement" = None, uma_BreakdownElement103: "uma_BreakdownElement" = None, uma_BreakdownElement107: "uma_BreakdownElement" = None, uma_BreakdownElement105: "uma_BreakdownElement" = None, uma_BreakdownElement109: "uma_PlanningData" = None, BreakdownElement: "uma_Activity" = None, uma_BreakdownElement118: set["uma_Example"] = None, uma_BreakdownElement121: set["uma_Guideline"] = None, uma_BreakdownElement124: set["uma_ReusableAsset"] = None, uma_BreakdownElement127: set["uma_SupportingMaterial"] = None, uma_BreakdownElement130: set["uma_Template"] = None, uma_BreakdownElement133: set["uma_Report"] = None, uma_BreakdownElement136: set["uma_EstimationConsiderations"] = None, uma_BreakdownElement139: set["uma_ToolMentor"] = None, breakdownElements: "uma_Activity" = None, uma_BreakdownElement112: set["uma_Checklist"] = None, uma_BreakdownElement115: set["uma_Concept"] = None):
        self.prefix = prefix
        self.isPlanned = isPlanned
        self.hasMultipleOccurrences = hasMultipleOccurrences
        self.isOptional = isOptional
        self.uma_BreakdownElement = uma_BreakdownElement
        self.uma_BreakdownElement103 = uma_BreakdownElement103
        self.uma_BreakdownElement107 = uma_BreakdownElement107
        self.uma_BreakdownElement105 = uma_BreakdownElement105
        self.uma_BreakdownElement109 = uma_BreakdownElement109
        self.BreakdownElement = BreakdownElement
        self.uma_BreakdownElement118 = uma_BreakdownElement118 if uma_BreakdownElement118 is not None else set()
        self.uma_BreakdownElement121 = uma_BreakdownElement121 if uma_BreakdownElement121 is not None else set()
        self.uma_BreakdownElement124 = uma_BreakdownElement124 if uma_BreakdownElement124 is not None else set()
        self.uma_BreakdownElement127 = uma_BreakdownElement127 if uma_BreakdownElement127 is not None else set()
        self.uma_BreakdownElement130 = uma_BreakdownElement130 if uma_BreakdownElement130 is not None else set()
        self.uma_BreakdownElement133 = uma_BreakdownElement133 if uma_BreakdownElement133 is not None else set()
        self.uma_BreakdownElement136 = uma_BreakdownElement136 if uma_BreakdownElement136 is not None else set()
        self.uma_BreakdownElement139 = uma_BreakdownElement139 if uma_BreakdownElement139 is not None else set()
        self.breakdownElements = breakdownElements
        self.uma_BreakdownElement112 = uma_BreakdownElement112 if uma_BreakdownElement112 is not None else set()
        self.uma_BreakdownElement115 = uma_BreakdownElement115 if uma_BreakdownElement115 is not None else set()
        
    @property
    def isOptional(self) -> str:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional

    @property
    def hasMultipleOccurrences(self) -> str:
        return self.__hasMultipleOccurrences

    @hasMultipleOccurrences.setter
    def hasMultipleOccurrences(self, hasMultipleOccurrences: str):
        self.__hasMultipleOccurrences = hasMultipleOccurrences

    @property
    def isPlanned(self) -> str:
        return self.__isPlanned

    @isPlanned.setter
    def isPlanned(self, isPlanned: str):
        self.__isPlanned = isPlanned

    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def uma_BreakdownElement109(self):
        return self.__uma_BreakdownElement109

    @uma_BreakdownElement109.setter
    def uma_BreakdownElement109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement109", None)
        self.__uma_BreakdownElement109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_PlanningData"):
                opp_val = getattr(old_value, "uma_PlanningData", None)
                if opp_val == self:
                    setattr(old_value, "uma_PlanningData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_PlanningData"):
                opp_val = getattr(value, "uma_PlanningData", None)
                setattr(value, "uma_PlanningData", self)

    @property
    def uma_BreakdownElement124(self):
        return self.__uma_BreakdownElement124

    @uma_BreakdownElement124.setter
    def uma_BreakdownElement124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement124", None)
        self.__uma_BreakdownElement124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_ReusableAsset125"):
                    opp_val = getattr(item, "uma_ReusableAsset125", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_ReusableAsset125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_ReusableAsset125"):
                    opp_val = getattr(item, "uma_ReusableAsset125", None)
                    
                    setattr(item, "uma_ReusableAsset125", self)
                    

    @property
    def uma_BreakdownElement105(self):
        return self.__uma_BreakdownElement105

    @uma_BreakdownElement105.setter
    def uma_BreakdownElement105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement105", None)
        self.__uma_BreakdownElement105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_BreakdownElement107"):
                opp_val = getattr(old_value, "uma_BreakdownElement107", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement107"):
                opp_val = getattr(value, "uma_BreakdownElement107", None)
                setattr(value, "uma_BreakdownElement107", self)

    @property
    def uma_BreakdownElement139(self):
        return self.__uma_BreakdownElement139

    @uma_BreakdownElement139.setter
    def uma_BreakdownElement139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement139", None)
        self.__uma_BreakdownElement139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_ToolMentor140"):
                    opp_val = getattr(item, "uma_ToolMentor140", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_ToolMentor140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_ToolMentor140"):
                    opp_val = getattr(item, "uma_ToolMentor140", None)
                    
                    setattr(item, "uma_ToolMentor140", self)
                    

    @property
    def uma_BreakdownElement103(self):
        return self.__uma_BreakdownElement103

    @uma_BreakdownElement103.setter
    def uma_BreakdownElement103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement103", None)
        self.__uma_BreakdownElement103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_BreakdownElement"):
                opp_val = getattr(old_value, "uma_BreakdownElement", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement"):
                opp_val = getattr(value, "uma_BreakdownElement", None)
                setattr(value, "uma_BreakdownElement", self)

    @property
    def uma_BreakdownElement(self):
        return self.__uma_BreakdownElement

    @uma_BreakdownElement.setter
    def uma_BreakdownElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement", None)
        self.__uma_BreakdownElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_BreakdownElement103"):
                opp_val = getattr(old_value, "uma_BreakdownElement103", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement103"):
                opp_val = getattr(value, "uma_BreakdownElement103", None)
                setattr(value, "uma_BreakdownElement103", self)

    @property
    def uma_BreakdownElement130(self):
        return self.__uma_BreakdownElement130

    @uma_BreakdownElement130.setter
    def uma_BreakdownElement130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement130", None)
        self.__uma_BreakdownElement130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Template131"):
                    opp_val = getattr(item, "uma_Template131", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Template131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Template131"):
                    opp_val = getattr(item, "uma_Template131", None)
                    
                    setattr(item, "uma_Template131", self)
                    

    @property
    def uma_BreakdownElement136(self):
        return self.__uma_BreakdownElement136

    @uma_BreakdownElement136.setter
    def uma_BreakdownElement136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement136", None)
        self.__uma_BreakdownElement136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_EstimationConsiderations137"):
                    opp_val = getattr(item, "uma_EstimationConsiderations137", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_EstimationConsiderations137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_EstimationConsiderations137"):
                    opp_val = getattr(item, "uma_EstimationConsiderations137", None)
                    
                    setattr(item, "uma_EstimationConsiderations137", self)
                    

    @property
    def uma_BreakdownElement107(self):
        return self.__uma_BreakdownElement107

    @uma_BreakdownElement107.setter
    def uma_BreakdownElement107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement107", None)
        self.__uma_BreakdownElement107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_BreakdownElement105"):
                opp_val = getattr(old_value, "uma_BreakdownElement105", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement105"):
                opp_val = getattr(value, "uma_BreakdownElement105", None)
                setattr(value, "uma_BreakdownElement105", self)

    @property
    def breakdownElements(self):
        return self.__breakdownElements

    @breakdownElements.setter
    def breakdownElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__breakdownElements", None)
        self.__breakdownElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity"):
                opp_val = getattr(old_value, "Activity", None)
                if opp_val == self:
                    setattr(old_value, "Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity"):
                opp_val = getattr(value, "Activity", None)
                setattr(value, "Activity", self)

    @property
    def uma_BreakdownElement127(self):
        return self.__uma_BreakdownElement127

    @uma_BreakdownElement127.setter
    def uma_BreakdownElement127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement127", None)
        self.__uma_BreakdownElement127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_SupportingMaterial128"):
                    opp_val = getattr(item, "uma_SupportingMaterial128", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_SupportingMaterial128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_SupportingMaterial128"):
                    opp_val = getattr(item, "uma_SupportingMaterial128", None)
                    
                    setattr(item, "uma_SupportingMaterial128", self)
                    

    @property
    def BreakdownElement(self):
        return self.__BreakdownElement

    @BreakdownElement.setter
    def BreakdownElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__BreakdownElement", None)
        self.__BreakdownElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superActivities"):
                opp_val = getattr(old_value, "superActivities", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superActivities"):
                opp_val = getattr(value, "superActivities", None)
                if opp_val is None:
                    setattr(value, "superActivities", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_BreakdownElement115(self):
        return self.__uma_BreakdownElement115

    @uma_BreakdownElement115.setter
    def uma_BreakdownElement115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement115", None)
        self.__uma_BreakdownElement115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Concept116"):
                    opp_val = getattr(item, "uma_Concept116", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Concept116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Concept116"):
                    opp_val = getattr(item, "uma_Concept116", None)
                    
                    setattr(item, "uma_Concept116", self)
                    

    @property
    def uma_BreakdownElement118(self):
        return self.__uma_BreakdownElement118

    @uma_BreakdownElement118.setter
    def uma_BreakdownElement118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement118", None)
        self.__uma_BreakdownElement118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Example119"):
                    opp_val = getattr(item, "uma_Example119", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Example119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Example119"):
                    opp_val = getattr(item, "uma_Example119", None)
                    
                    setattr(item, "uma_Example119", self)
                    

    @property
    def uma_BreakdownElement112(self):
        return self.__uma_BreakdownElement112

    @uma_BreakdownElement112.setter
    def uma_BreakdownElement112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement112", None)
        self.__uma_BreakdownElement112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Checklist113"):
                    opp_val = getattr(item, "uma_Checklist113", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Checklist113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Checklist113"):
                    opp_val = getattr(item, "uma_Checklist113", None)
                    
                    setattr(item, "uma_Checklist113", self)
                    

    @property
    def uma_BreakdownElement133(self):
        return self.__uma_BreakdownElement133

    @uma_BreakdownElement133.setter
    def uma_BreakdownElement133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement133", None)
        self.__uma_BreakdownElement133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Report134"):
                    opp_val = getattr(item, "uma_Report134", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Report134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Report134"):
                    opp_val = getattr(item, "uma_Report134", None)
                    
                    setattr(item, "uma_Report134", self)
                    

    @property
    def uma_BreakdownElement121(self):
        return self.__uma_BreakdownElement121

    @uma_BreakdownElement121.setter
    def uma_BreakdownElement121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_BreakdownElement__uma_BreakdownElement121", None)
        self.__uma_BreakdownElement121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Guideline122"):
                    opp_val = getattr(item, "uma_Guideline122", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Guideline122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Guideline122"):
                    opp_val = getattr(item, "uma_Guideline122", None)
                    
                    setattr(item, "uma_Guideline122", self)
                    

class uma_PlanningData(ProcessElement):

    def __init__(self, startDate: str, finishDate: str, rank: str, uma_PlanningData: "uma_BreakdownElement" = None):
        self.startDate = startDate
        self.finishDate = finishDate
        self.rank = rank
        self.uma_PlanningData = uma_PlanningData
        
    @property
    def rank(self) -> str:
        return self.__rank

    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank

    @property
    def finishDate(self) -> str:
        return self.__finishDate

    @finishDate.setter
    def finishDate(self, finishDate: str):
        self.__finishDate = finishDate

    @property
    def startDate(self) -> str:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: str):
        self.__startDate = startDate

    @property
    def uma_PlanningData(self):
        return self.__uma_PlanningData

    @uma_PlanningData.setter
    def uma_PlanningData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_PlanningData__uma_PlanningData", None)
        self.__uma_PlanningData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_BreakdownElement109"):
                opp_val = getattr(old_value, "uma_BreakdownElement109", None)
                if opp_val == self:
                    setattr(old_value, "uma_BreakdownElement109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_BreakdownElement109"):
                opp_val = getattr(value, "uma_BreakdownElement109", None)
                setattr(value, "uma_BreakdownElement109", self)

class uma_WorkOrder(ProcessElement):

    def __init__(self, linkType: str, uma_WorkOrder: "uma_WorkBreakdownElement" = None, uma_WorkOrder142: "uma_WorkBreakdownElement" = None):
        self.linkType = linkType
        self.uma_WorkOrder = uma_WorkOrder
        self.uma_WorkOrder142 = uma_WorkOrder142
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def uma_WorkOrder142(self):
        return self.__uma_WorkOrder142

    @uma_WorkOrder142.setter
    def uma_WorkOrder142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkOrder__uma_WorkOrder142", None)
        self.__uma_WorkOrder142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkBreakdownElement143"):
                opp_val = getattr(old_value, "uma_WorkBreakdownElement143", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkBreakdownElement143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkBreakdownElement143"):
                opp_val = getattr(value, "uma_WorkBreakdownElement143", None)
                setattr(value, "uma_WorkBreakdownElement143", self)

    @property
    def uma_WorkOrder(self):
        return self.__uma_WorkOrder

    @uma_WorkOrder.setter
    def uma_WorkOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkOrder__uma_WorkOrder", None)
        self.__uma_WorkOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkBreakdownElement"):
                opp_val = getattr(old_value, "uma_WorkBreakdownElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkBreakdownElement"):
                opp_val = getattr(value, "uma_WorkBreakdownElement", None)
                if opp_val is None:
                    setattr(value, "uma_WorkBreakdownElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BreakdownElement:

    pass
class uma_ProcessComponentInterface(BreakdownElement):

    pass
class uma_TeamProfile(BreakdownElement):

    pass
class uma_Descriptor(BreakdownElement):

    def __init__(self, isSynchronizedWithSource: str):
        self.isSynchronizedWithSource = isSynchronizedWithSource
        
    @property
    def isSynchronizedWithSource(self) -> str:
        return self.__isSynchronizedWithSource

    @isSynchronizedWithSource.setter
    def isSynchronizedWithSource(self, isSynchronizedWithSource: str):
        self.__isSynchronizedWithSource = isSynchronizedWithSource

class uma_WorkBreakdownElement(BreakdownElement):

    def __init__(self, isRepeatable: str, isOngoing: str, isEventDriven: str, uma_WorkBreakdownElement: set["uma_WorkOrder"] = None, uma_WorkBreakdownElement143: "uma_WorkOrder" = None):
        self.isRepeatable = isRepeatable
        self.isOngoing = isOngoing
        self.isEventDriven = isEventDriven
        self.uma_WorkBreakdownElement = uma_WorkBreakdownElement if uma_WorkBreakdownElement is not None else set()
        self.uma_WorkBreakdownElement143 = uma_WorkBreakdownElement143
        
    @property
    def isEventDriven(self) -> str:
        return self.__isEventDriven

    @isEventDriven.setter
    def isEventDriven(self, isEventDriven: str):
        self.__isEventDriven = isEventDriven

    @property
    def isRepeatable(self) -> str:
        return self.__isRepeatable

    @isRepeatable.setter
    def isRepeatable(self, isRepeatable: str):
        self.__isRepeatable = isRepeatable

    @property
    def isOngoing(self) -> str:
        return self.__isOngoing

    @isOngoing.setter
    def isOngoing(self, isOngoing: str):
        self.__isOngoing = isOngoing

    @property
    def uma_WorkBreakdownElement143(self):
        return self.__uma_WorkBreakdownElement143

    @uma_WorkBreakdownElement143.setter
    def uma_WorkBreakdownElement143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkBreakdownElement__uma_WorkBreakdownElement143", None)
        self.__uma_WorkBreakdownElement143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkOrder142"):
                opp_val = getattr(old_value, "uma_WorkOrder142", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkOrder142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkOrder142"):
                opp_val = getattr(value, "uma_WorkOrder142", None)
                setattr(value, "uma_WorkOrder142", self)

    @property
    def uma_WorkBreakdownElement(self):
        return self.__uma_WorkBreakdownElement

    @uma_WorkBreakdownElement.setter
    def uma_WorkBreakdownElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_WorkBreakdownElement__uma_WorkBreakdownElement", None)
        self.__uma_WorkBreakdownElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_WorkOrder"):
                    opp_val = getattr(item, "uma_WorkOrder", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_WorkOrder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_WorkOrder"):
                    opp_val = getattr(item, "uma_WorkOrder", None)
                    
                    setattr(item, "uma_WorkOrder", self)
                    

class ContentCategory:

    pass
class uma_Discipline(ContentCategory):

    pass
class uma_WorkProductType(ContentCategory):

    pass
class uma_DisciplineGrouping(ContentCategory):

    pass
class uma_RoleSetGrouping(ContentCategory):

    pass
class uma_Domain(ContentCategory):

    pass
class uma_CustomCategory(ContentCategory):

    pass
class uma_Tool(ContentCategory):

    pass
class uma_RoleSet(ContentCategory):

    pass
class ContentDescription:

    pass
class uma_RoleDescription(ContentDescription):

    def __init__(self, skills: str, assignmentApproaches: str, synonyms: str):
        self.skills = skills
        self.assignmentApproaches = assignmentApproaches
        self.synonyms = synonyms
        
    @property
    def assignmentApproaches(self) -> str:
        return self.__assignmentApproaches

    @assignmentApproaches.setter
    def assignmentApproaches(self, assignmentApproaches: str):
        self.__assignmentApproaches = assignmentApproaches

    @property
    def skills(self) -> str:
        return self.__skills

    @skills.setter
    def skills(self, skills: str):
        self.__skills = skills

    @property
    def synonyms(self) -> str:
        return self.__synonyms

    @synonyms.setter
    def synonyms(self, synonyms: str):
        self.__synonyms = synonyms

class uma_GuidanceDescription(ContentDescription):

    def __init__(self, attachments: str):
        self.attachments = attachments
        
    @property
    def attachments(self) -> str:
        return self.__attachments

    @attachments.setter
    def attachments(self, attachments: str):
        self.__attachments = attachments

class uma_TaskDescription(ContentDescription):

    def __init__(self, purpose: str, alternatives: str):
        self.purpose = purpose
        self.alternatives = alternatives
        
    @property
    def alternatives(self) -> str:
        return self.__alternatives

    @alternatives.setter
    def alternatives(self, alternatives: str):
        self.__alternatives = alternatives

    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

class uma_BreakdownElementDescription(ContentDescription):

    def __init__(self, usageGuidance: str):
        self.usageGuidance = usageGuidance
        
    @property
    def usageGuidance(self) -> str:
        return self.__usageGuidance

    @usageGuidance.setter
    def usageGuidance(self, usageGuidance: str):
        self.__usageGuidance = usageGuidance

class uma_PracticeDescription(ContentDescription):

    def __init__(self, additionalInfo: str, problem: str, background: str, goals: str, application: str, levelsOfAdoption: str):
        self.additionalInfo = additionalInfo
        self.problem = problem
        self.background = background
        self.goals = goals
        self.application = application
        self.levelsOfAdoption = levelsOfAdoption
        
    @property
    def levelsOfAdoption(self) -> str:
        return self.__levelsOfAdoption

    @levelsOfAdoption.setter
    def levelsOfAdoption(self, levelsOfAdoption: str):
        self.__levelsOfAdoption = levelsOfAdoption

    @property
    def application(self) -> str:
        return self.__application

    @application.setter
    def application(self, application: str):
        self.__application = application

    @property
    def additionalInfo(self) -> str:
        return self.__additionalInfo

    @additionalInfo.setter
    def additionalInfo(self, additionalInfo: str):
        self.__additionalInfo = additionalInfo

    @property
    def goals(self) -> str:
        return self.__goals

    @goals.setter
    def goals(self, goals: str):
        self.__goals = goals

    @property
    def problem(self) -> str:
        return self.__problem

    @problem.setter
    def problem(self, problem: str):
        self.__problem = problem

    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

class uma_WorkProductDescription(ContentDescription):

    def __init__(self, purpose: str, impactOfNotHaving: str, reasonsForNotNeeding: str):
        self.purpose = purpose
        self.impactOfNotHaving = impactOfNotHaving
        self.reasonsForNotNeeding = reasonsForNotNeeding
        
    @property
    def reasonsForNotNeeding(self) -> str:
        return self.__reasonsForNotNeeding

    @reasonsForNotNeeding.setter
    def reasonsForNotNeeding(self, reasonsForNotNeeding: str):
        self.__reasonsForNotNeeding = reasonsForNotNeeding

    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

    @property
    def impactOfNotHaving(self) -> str:
        return self.__impactOfNotHaving

    @impactOfNotHaving.setter
    def impactOfNotHaving(self, impactOfNotHaving: str):
        self.__impactOfNotHaving = impactOfNotHaving

class Concept:

    pass
class uma_Whitepaper(Concept):

    pass
class WorkProductDescription:

    pass
class uma_DeliverableDescription(WorkProductDescription):

    def __init__(self, externalDescription: str, packagingGuidance: str):
        self.externalDescription = externalDescription
        self.packagingGuidance = packagingGuidance
        
    @property
    def packagingGuidance(self) -> str:
        return self.__packagingGuidance

    @packagingGuidance.setter
    def packagingGuidance(self, packagingGuidance: str):
        self.__packagingGuidance = packagingGuidance

    @property
    def externalDescription(self) -> str:
        return self.__externalDescription

    @externalDescription.setter
    def externalDescription(self, externalDescription: str):
        self.__externalDescription = externalDescription

class uma_ArtifactDescription(WorkProductDescription):

    def __init__(self, briefOutline: str, representationOptions: str, representation: str, notation: str):
        self.briefOutline = briefOutline
        self.representationOptions = representationOptions
        self.representation = representation
        self.notation = notation
        
    @property
    def notation(self) -> str:
        return self.__notation

    @notation.setter
    def notation(self, notation: str):
        self.__notation = notation

    @property
    def representation(self) -> str:
        return self.__representation

    @representation.setter
    def representation(self, representation: str):
        self.__representation = representation

    @property
    def representationOptions(self) -> str:
        return self.__representationOptions

    @representationOptions.setter
    def representationOptions(self, representationOptions: str):
        self.__representationOptions = representationOptions

    @property
    def briefOutline(self) -> str:
        return self.__briefOutline

    @briefOutline.setter
    def briefOutline(self, briefOutline: str):
        self.__briefOutline = briefOutline

class WorkDefinition:

    pass
class Section:

    pass
class uma_Step(WorkDefinition, Section):

    pass
class FulfillableElement:

    pass
class WorkProduct:

    pass
class uma_Deliverable(WorkProduct):

    pass
class uma_Outcome(WorkProduct):

    pass
class uma_Artifact(WorkProduct):

    pass
class Guidance:

    pass
class uma_Practice(Guidance):

    pass
class uma_Report(Guidance):

    pass
class uma_Template(Guidance):

    pass
class uma_Roadmap(Guidance):

    pass
class uma_ToolMentor(Guidance):

    pass
class uma_EstimationConsiderations(Guidance):

    pass
class uma_SupportingMaterial(Guidance):

    pass
class VariabilityElement:

    pass
class uma_Activity(WorkDefinition, FulfillableElement, WorkBreakdownElement, VariabilityElement):

    pass
class uma_Section(VariabilityElement):

    def __init__(self, sectionName: str, sectionDescription: str, uma_Section: "uma_ContentDescription" = None, uma_Section27: "uma_Section" = None, uma_Section25: set["uma_Section"] = None, uma_Section30: "uma_Section" = None, uma_Section28: "uma_Section" = None, uma_Section211: "uma_TaskDescriptor" = None):
        self.sectionName = sectionName
        self.sectionDescription = sectionDescription
        self.uma_Section = uma_Section
        self.uma_Section27 = uma_Section27
        self.uma_Section25 = uma_Section25 if uma_Section25 is not None else set()
        self.uma_Section30 = uma_Section30
        self.uma_Section28 = uma_Section28
        self.uma_Section211 = uma_Section211
        
    @property
    def sectionDescription(self) -> str:
        return self.__sectionDescription

    @sectionDescription.setter
    def sectionDescription(self, sectionDescription: str):
        self.__sectionDescription = sectionDescription

    @property
    def sectionName(self) -> str:
        return self.__sectionName

    @sectionName.setter
    def sectionName(self, sectionName: str):
        self.__sectionName = sectionName

    @property
    def uma_Section(self):
        return self.__uma_Section

    @uma_Section.setter
    def uma_Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section", None)
        self.__uma_Section = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ContentDescription22"):
                opp_val = getattr(old_value, "uma_ContentDescription22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ContentDescription22"):
                opp_val = getattr(value, "uma_ContentDescription22", None)
                if opp_val is None:
                    setattr(value, "uma_ContentDescription22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Section25(self):
        return self.__uma_Section25

    @uma_Section25.setter
    def uma_Section25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section25", None)
        self.__uma_Section25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Section27"):
                    opp_val = getattr(item, "uma_Section27", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Section27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Section27"):
                    opp_val = getattr(item, "uma_Section27", None)
                    
                    setattr(item, "uma_Section27", self)
                    

    @property
    def uma_Section211(self):
        return self.__uma_Section211

    @uma_Section211.setter
    def uma_Section211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section211", None)
        self.__uma_Section211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_TaskDescriptor210"):
                opp_val = getattr(old_value, "uma_TaskDescriptor210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_TaskDescriptor210"):
                opp_val = getattr(value, "uma_TaskDescriptor210", None)
                if opp_val is None:
                    setattr(value, "uma_TaskDescriptor210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Section28(self):
        return self.__uma_Section28

    @uma_Section28.setter
    def uma_Section28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section28", None)
        self.__uma_Section28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Section30"):
                opp_val = getattr(old_value, "uma_Section30", None)
                if opp_val == self:
                    setattr(old_value, "uma_Section30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Section30"):
                opp_val = getattr(value, "uma_Section30", None)
                setattr(value, "uma_Section30", self)

    @property
    def uma_Section27(self):
        return self.__uma_Section27

    @uma_Section27.setter
    def uma_Section27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section27", None)
        self.__uma_Section27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Section25"):
                opp_val = getattr(old_value, "uma_Section25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Section25"):
                opp_val = getattr(value, "uma_Section25", None)
                if opp_val is None:
                    setattr(value, "uma_Section25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_Section30(self):
        return self.__uma_Section30

    @uma_Section30.setter
    def uma_Section30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Section__uma_Section30", None)
        self.__uma_Section30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Section28"):
                opp_val = getattr(old_value, "uma_Section28", None)
                if opp_val == self:
                    setattr(old_value, "uma_Section28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Section28"):
                opp_val = getattr(value, "uma_Section28", None)
                setattr(value, "uma_Section28", self)

class MethodUnit:

    pass
class uma_ProcessComponent(ProcessPackage, MethodUnit):

    pass
class uma_MethodLibrary(Package, MethodUnit):

    pass
class uma_MethodPlugin(Package, MethodUnit):

    def __init__(self, userChangeable: str, supporting: bool, uma_MethodPlugin: "uma_MethodConfiguration" = None, uma_MethodPlugin246: set["uma_MethodPackage"] = None, uma_MethodPlugin250: "uma_MethodPlugin" = None, uma_MethodPlugin248: set["uma_MethodPlugin"] = None, uma_MethodPlugin323: "uma_MethodLibrary" = None):
        self.userChangeable = userChangeable
        self.supporting = supporting
        self.uma_MethodPlugin = uma_MethodPlugin
        self.uma_MethodPlugin246 = uma_MethodPlugin246 if uma_MethodPlugin246 is not None else set()
        self.uma_MethodPlugin250 = uma_MethodPlugin250
        self.uma_MethodPlugin248 = uma_MethodPlugin248 if uma_MethodPlugin248 is not None else set()
        self.uma_MethodPlugin323 = uma_MethodPlugin323
        
    @property
    def userChangeable(self) -> str:
        return self.__userChangeable

    @userChangeable.setter
    def userChangeable(self, userChangeable: str):
        self.__userChangeable = userChangeable

    @property
    def supporting(self) -> bool:
        return self.__supporting

    @supporting.setter
    def supporting(self, supporting: bool):
        self.__supporting = supporting

    @property
    def uma_MethodPlugin246(self):
        return self.__uma_MethodPlugin246

    @uma_MethodPlugin246.setter
    def uma_MethodPlugin246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin246", None)
        self.__uma_MethodPlugin246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPackage247"):
                    opp_val = getattr(item, "uma_MethodPackage247", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPackage247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPackage247"):
                    opp_val = getattr(item, "uma_MethodPackage247", None)
                    
                    setattr(item, "uma_MethodPackage247", self)
                    

    @property
    def uma_MethodPlugin250(self):
        return self.__uma_MethodPlugin250

    @uma_MethodPlugin250.setter
    def uma_MethodPlugin250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin250", None)
        self.__uma_MethodPlugin250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPlugin248"):
                opp_val = getattr(old_value, "uma_MethodPlugin248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPlugin248"):
                opp_val = getattr(value, "uma_MethodPlugin248", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPlugin248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPlugin323(self):
        return self.__uma_MethodPlugin323

    @uma_MethodPlugin323.setter
    def uma_MethodPlugin323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin323", None)
        self.__uma_MethodPlugin323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodLibrary"):
                opp_val = getattr(old_value, "uma_MethodLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodLibrary"):
                opp_val = getattr(value, "uma_MethodLibrary", None)
                if opp_val is None:
                    setattr(value, "uma_MethodLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPlugin(self):
        return self.__uma_MethodPlugin

    @uma_MethodPlugin.setter
    def uma_MethodPlugin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin", None)
        self.__uma_MethodPlugin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodConfiguration226"):
                opp_val = getattr(old_value, "uma_MethodConfiguration226", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodConfiguration226"):
                opp_val = getattr(value, "uma_MethodConfiguration226", None)
                if opp_val is None:
                    setattr(value, "uma_MethodConfiguration226", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPlugin248(self):
        return self.__uma_MethodPlugin248

    @uma_MethodPlugin248.setter
    def uma_MethodPlugin248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPlugin__uma_MethodPlugin248", None)
        self.__uma_MethodPlugin248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPlugin250"):
                    opp_val = getattr(item, "uma_MethodPlugin250", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPlugin250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPlugin250"):
                    opp_val = getattr(item, "uma_MethodPlugin250", None)
                    
                    setattr(item, "uma_MethodPlugin250", self)
                    

class uma_MethodConfiguration(MethodUnit):

    pass
class uma_ContentDescription(MethodUnit):

    def __init__(self, mainDescription: str, externalId: str, keyConsiderations: str, longPresentationName: str, uma_ContentDescription: "uma_DescribableElement" = None, uma_ContentDescription22: set["uma_Section"] = None):
        self.mainDescription = mainDescription
        self.externalId = externalId
        self.keyConsiderations = keyConsiderations
        self.longPresentationName = longPresentationName
        self.uma_ContentDescription = uma_ContentDescription
        self.uma_ContentDescription22 = uma_ContentDescription22 if uma_ContentDescription22 is not None else set()
        
    @property
    def keyConsiderations(self) -> str:
        return self.__keyConsiderations

    @keyConsiderations.setter
    def keyConsiderations(self, keyConsiderations: str):
        self.__keyConsiderations = keyConsiderations

    @property
    def mainDescription(self) -> str:
        return self.__mainDescription

    @mainDescription.setter
    def mainDescription(self, mainDescription: str):
        self.__mainDescription = mainDescription

    @property
    def longPresentationName(self) -> str:
        return self.__longPresentationName

    @longPresentationName.setter
    def longPresentationName(self, longPresentationName: str):
        self.__longPresentationName = longPresentationName

    @property
    def externalId(self) -> str:
        return self.__externalId

    @externalId.setter
    def externalId(self, externalId: str):
        self.__externalId = externalId

    @property
    def uma_ContentDescription22(self):
        return self.__uma_ContentDescription22

    @uma_ContentDescription22.setter
    def uma_ContentDescription22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ContentDescription__uma_ContentDescription22", None)
        self.__uma_ContentDescription22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Section"):
                    opp_val = getattr(item, "uma_Section", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Section", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Section"):
                    opp_val = getattr(item, "uma_Section", None)
                    
                    setattr(item, "uma_Section", self)
                    

    @property
    def uma_ContentDescription(self):
        return self.__uma_ContentDescription

    @uma_ContentDescription.setter
    def uma_ContentDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ContentDescription__uma_ContentDescription", None)
        self.__uma_ContentDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_DescribableElement"):
                opp_val = getattr(old_value, "uma_DescribableElement", None)
                if opp_val == self:
                    setattr(old_value, "uma_DescribableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_DescribableElement"):
                opp_val = getattr(value, "uma_DescribableElement", None)
                setattr(value, "uma_DescribableElement", self)

class Classifier:

    pass
class uma_TermDefinition(Guidance):

    pass
class uma_ReusableAsset(Guidance):

    pass
class uma_Example(Guidance):

    pass
class uma_Guideline(Guidance):

    pass
class uma_Checklist(Guidance):

    pass
class uma_Concept(Guidance):

    pass
class MethodElement:

    pass
class uma_DiagramElement(MethodElement):

    def __init__(self, isVisible: str, DiagramElement: "uma_GraphElement" = None, contained: "uma_GraphElement" = None, referenced: set["uma_Reference"] = None, uma_DiagramElement: set["uma_Property"] = None, DiagramElement290: "uma_Reference" = None):
        self.isVisible = isVisible
        self.DiagramElement = DiagramElement
        self.contained = contained
        self.referenced = referenced if referenced is not None else set()
        self.uma_DiagramElement = uma_DiagramElement if uma_DiagramElement is not None else set()
        self.DiagramElement290 = DiagramElement290
        
    @property
    def isVisible(self) -> str:
        return self.__isVisible

    @isVisible.setter
    def isVisible(self, isVisible: str):
        self.__isVisible = isVisible

    @property
    def DiagramElement290(self):
        return self.__DiagramElement290

    @DiagramElement290.setter
    def DiagramElement290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__DiagramElement290", None)
        self.__DiagramElement290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reference"):
                opp_val = getattr(old_value, "reference", None)
                if opp_val == self:
                    setattr(old_value, "reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reference"):
                opp_val = getattr(value, "reference", None)
                setattr(value, "reference", self)

    @property
    def uma_DiagramElement(self):
        return self.__uma_DiagramElement

    @uma_DiagramElement.setter
    def uma_DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__uma_DiagramElement", None)
        self.__uma_DiagramElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Property"):
                    opp_val = getattr(item, "uma_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Property"):
                    opp_val = getattr(item, "uma_Property", None)
                    
                    setattr(item, "uma_Property", self)
                    

    @property
    def referenced(self):
        return self.__referenced

    @referenced.setter
    def referenced(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__referenced", None)
        self.__referenced = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Reference"):
                    opp_val = getattr(item, "Reference", None)
                    
                    if opp_val == self:
                        setattr(item, "Reference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Reference"):
                    opp_val = getattr(item, "Reference", None)
                    
                    setattr(item, "Reference", self)
                    

    @property
    def DiagramElement(self):
        return self.__DiagramElement

    @DiagramElement.setter
    def DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__DiagramElement", None)
        self.__DiagramElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contained(self):
        return self.__contained

    @contained.setter
    def contained(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DiagramElement__contained", None)
        self.__contained = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphElement"):
                opp_val = getattr(old_value, "GraphElement", None)
                if opp_val == self:
                    setattr(old_value, "GraphElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphElement"):
                opp_val = getattr(value, "GraphElement", None)
                setattr(value, "GraphElement", self)

class uma_DescribableElement(MethodElement, Classifier):

    def __init__(self, shapeicon: str, nodeicon: str, uma_DescribableElement: "uma_ContentDescription" = None, uma_DescribableElement149: "uma_CustomCategory" = None):
        self.shapeicon = shapeicon
        self.nodeicon = nodeicon
        self.uma_DescribableElement = uma_DescribableElement
        self.uma_DescribableElement149 = uma_DescribableElement149
        
    @property
    def nodeicon(self) -> str:
        return self.__nodeicon

    @nodeicon.setter
    def nodeicon(self, nodeicon: str):
        self.__nodeicon = nodeicon

    @property
    def shapeicon(self) -> str:
        return self.__shapeicon

    @shapeicon.setter
    def shapeicon(self, shapeicon: str):
        self.__shapeicon = shapeicon

    @property
    def uma_DescribableElement149(self):
        return self.__uma_DescribableElement149

    @uma_DescribableElement149.setter
    def uma_DescribableElement149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DescribableElement__uma_DescribableElement149", None)
        self.__uma_DescribableElement149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_CustomCategory"):
                opp_val = getattr(old_value, "uma_CustomCategory", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_CustomCategory"):
                opp_val = getattr(value, "uma_CustomCategory", None)
                if opp_val is None:
                    setattr(value, "uma_CustomCategory", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_DescribableElement(self):
        return self.__uma_DescribableElement

    @uma_DescribableElement.setter
    def uma_DescribableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_DescribableElement__uma_DescribableElement", None)
        self.__uma_DescribableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_ContentDescription"):
                opp_val = getattr(old_value, "uma_ContentDescription", None)
                if opp_val == self:
                    setattr(old_value, "uma_ContentDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_ContentDescription"):
                opp_val = getattr(value, "uma_ContentDescription", None)
                setattr(value, "uma_ContentDescription", self)

class uma_MethodUnit(MethodElement):

    def __init__(self, changeDate: str, changeDescription: str, version: str, authors: str, uma_MethodUnit: "uma_SupportingMaterial" = None):
        self.changeDate = changeDate
        self.changeDescription = changeDescription
        self.version = version
        self.authors = authors
        self.uma_MethodUnit = uma_MethodUnit
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def authors(self) -> str:
        return self.__authors

    @authors.setter
    def authors(self, authors: str):
        self.__authors = authors

    @property
    def changeDate(self) -> str:
        return self.__changeDate

    @changeDate.setter
    def changeDate(self, changeDate: str):
        self.__changeDate = changeDate

    @property
    def changeDescription(self) -> str:
        return self.__changeDescription

    @changeDescription.setter
    def changeDescription(self, changeDescription: str):
        self.__changeDescription = changeDescription

    @property
    def uma_MethodUnit(self):
        return self.__uma_MethodUnit

    @uma_MethodUnit.setter
    def uma_MethodUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodUnit__uma_MethodUnit", None)
        self.__uma_MethodUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_SupportingMaterial24"):
                opp_val = getattr(old_value, "uma_SupportingMaterial24", None)
                if opp_val == self:
                    setattr(old_value, "uma_SupportingMaterial24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_SupportingMaterial24"):
                opp_val = getattr(value, "uma_SupportingMaterial24", None)
                setattr(value, "uma_SupportingMaterial24", self)

class uma_VariabilityElement(MethodElement):

    def __init__(self, variabilityType: str, uma_VariabilityElement: "uma_VariabilityElement" = None, uma_VariabilityElement31: "uma_VariabilityElement" = None):
        self.variabilityType = variabilityType
        self.uma_VariabilityElement = uma_VariabilityElement
        self.uma_VariabilityElement31 = uma_VariabilityElement31
        
    @property
    def variabilityType(self) -> str:
        return self.__variabilityType

    @variabilityType.setter
    def variabilityType(self, variabilityType: str):
        self.__variabilityType = variabilityType

    @property
    def uma_VariabilityElement(self):
        return self.__uma_VariabilityElement

    @uma_VariabilityElement.setter
    def uma_VariabilityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_VariabilityElement__uma_VariabilityElement", None)
        self.__uma_VariabilityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_VariabilityElement31"):
                opp_val = getattr(old_value, "uma_VariabilityElement31", None)
                if opp_val == self:
                    setattr(old_value, "uma_VariabilityElement31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_VariabilityElement31"):
                opp_val = getattr(value, "uma_VariabilityElement31", None)
                setattr(value, "uma_VariabilityElement31", self)

    @property
    def uma_VariabilityElement31(self):
        return self.__uma_VariabilityElement31

    @uma_VariabilityElement31.setter
    def uma_VariabilityElement31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_VariabilityElement__uma_VariabilityElement31", None)
        self.__uma_VariabilityElement31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_VariabilityElement"):
                opp_val = getattr(old_value, "uma_VariabilityElement", None)
                if opp_val == self:
                    setattr(old_value, "uma_VariabilityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_VariabilityElement"):
                opp_val = getattr(value, "uma_VariabilityElement", None)
                setattr(value, "uma_VariabilityElement", self)

class uma_WorkDefinition(MethodElement):

    pass
class uma_MethodPackage(Package, MethodElement):

    def __init__(self, global: str, uma_MethodPackage: "uma_MethodPackage" = None, uma_MethodPackage152: set["uma_MethodPackage"] = None, uma_MethodPackage156: "uma_MethodPackage" = None, uma_MethodPackage154: set["uma_MethodPackage"] = None, uma_MethodPackage229: "uma_MethodConfiguration" = None, uma_MethodPackage247: "uma_MethodPlugin" = None):
        self.global = global
        self.uma_MethodPackage = uma_MethodPackage
        self.uma_MethodPackage152 = uma_MethodPackage152 if uma_MethodPackage152 is not None else set()
        self.uma_MethodPackage156 = uma_MethodPackage156
        self.uma_MethodPackage154 = uma_MethodPackage154 if uma_MethodPackage154 is not None else set()
        self.uma_MethodPackage229 = uma_MethodPackage229
        self.uma_MethodPackage247 = uma_MethodPackage247
        
    @property
    def global(self) -> str:
        return self.__global

    @global.setter
    def global(self, global: str):
        self.__global = global

    @property
    def uma_MethodPackage154(self):
        return self.__uma_MethodPackage154

    @uma_MethodPackage154.setter
    def uma_MethodPackage154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage154", None)
        self.__uma_MethodPackage154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPackage156"):
                    opp_val = getattr(item, "uma_MethodPackage156", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPackage156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPackage156"):
                    opp_val = getattr(item, "uma_MethodPackage156", None)
                    
                    setattr(item, "uma_MethodPackage156", self)
                    

    @property
    def uma_MethodPackage(self):
        return self.__uma_MethodPackage

    @uma_MethodPackage.setter
    def uma_MethodPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage", None)
        self.__uma_MethodPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPackage152"):
                opp_val = getattr(old_value, "uma_MethodPackage152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPackage152"):
                opp_val = getattr(value, "uma_MethodPackage152", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPackage152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPackage247(self):
        return self.__uma_MethodPackage247

    @uma_MethodPackage247.setter
    def uma_MethodPackage247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage247", None)
        self.__uma_MethodPackage247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPlugin246"):
                opp_val = getattr(old_value, "uma_MethodPlugin246", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPlugin246"):
                opp_val = getattr(value, "uma_MethodPlugin246", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPlugin246", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPackage229(self):
        return self.__uma_MethodPackage229

    @uma_MethodPackage229.setter
    def uma_MethodPackage229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage229", None)
        self.__uma_MethodPackage229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodConfiguration228"):
                opp_val = getattr(old_value, "uma_MethodConfiguration228", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodConfiguration228"):
                opp_val = getattr(value, "uma_MethodConfiguration228", None)
                if opp_val is None:
                    setattr(value, "uma_MethodConfiguration228", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPackage156(self):
        return self.__uma_MethodPackage156

    @uma_MethodPackage156.setter
    def uma_MethodPackage156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage156", None)
        self.__uma_MethodPackage156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodPackage154"):
                opp_val = getattr(old_value, "uma_MethodPackage154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodPackage154"):
                opp_val = getattr(value, "uma_MethodPackage154", None)
                if opp_val is None:
                    setattr(value, "uma_MethodPackage154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uma_MethodPackage152(self):
        return self.__uma_MethodPackage152

    @uma_MethodPackage152.setter
    def uma_MethodPackage152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodPackage__uma_MethodPackage152", None)
        self.__uma_MethodPackage152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodPackage"):
                    opp_val = getattr(item, "uma_MethodPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodPackage"):
                    opp_val = getattr(item, "uma_MethodPackage", None)
                    
                    setattr(item, "uma_MethodPackage", self)
                    

class uma_Constraint(MethodElement):

    def __init__(self, body: str, uma_Constraint: "uma_MethodElement" = None, uma_Constraint50: "uma_WorkDefinition" = None, uma_Constraint53: "uma_WorkDefinition" = None):
        self.body = body
        self.uma_Constraint = uma_Constraint
        self.uma_Constraint50 = uma_Constraint50
        self.uma_Constraint53 = uma_Constraint53
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def uma_Constraint53(self):
        return self.__uma_Constraint53

    @uma_Constraint53.setter
    def uma_Constraint53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Constraint__uma_Constraint53", None)
        self.__uma_Constraint53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkDefinition52"):
                opp_val = getattr(old_value, "uma_WorkDefinition52", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkDefinition52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkDefinition52"):
                opp_val = getattr(value, "uma_WorkDefinition52", None)
                setattr(value, "uma_WorkDefinition52", self)

    @property
    def uma_Constraint50(self):
        return self.__uma_Constraint50

    @uma_Constraint50.setter
    def uma_Constraint50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Constraint__uma_Constraint50", None)
        self.__uma_Constraint50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_WorkDefinition"):
                opp_val = getattr(old_value, "uma_WorkDefinition", None)
                if opp_val == self:
                    setattr(old_value, "uma_WorkDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_WorkDefinition"):
                opp_val = getattr(value, "uma_WorkDefinition", None)
                setattr(value, "uma_WorkDefinition", self)

    @property
    def uma_Constraint(self):
        return self.__uma_Constraint

    @uma_Constraint.setter
    def uma_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_Constraint__uma_Constraint", None)
        self.__uma_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodElement"):
                opp_val = getattr(old_value, "uma_MethodElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodElement"):
                opp_val = getattr(value, "uma_MethodElement", None)
                if opp_val is None:
                    setattr(value, "uma_MethodElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DescribableElement:

    pass
class uma_FulfillableElement(DescribableElement):

    pass
class uma_ProcessElement(DescribableElement):

    pass
class uma_ContentElement(VariabilityElement, DescribableElement):

    pass
class uma_ApplicableMetaClassInfo(Classifier):

    def __init__(self, isPrimaryExtension: str, uma_ApplicableMetaClassInfo: "uma_Kind" = None):
        self.isPrimaryExtension = isPrimaryExtension
        self.uma_ApplicableMetaClassInfo = uma_ApplicableMetaClassInfo
        
    @property
    def isPrimaryExtension(self) -> str:
        return self.__isPrimaryExtension

    @isPrimaryExtension.setter
    def isPrimaryExtension(self, isPrimaryExtension: str):
        self.__isPrimaryExtension = isPrimaryExtension

    @property
    def uma_ApplicableMetaClassInfo(self):
        return self.__uma_ApplicableMetaClassInfo

    @uma_ApplicableMetaClassInfo.setter
    def uma_ApplicableMetaClassInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_ApplicableMetaClassInfo__uma_ApplicableMetaClassInfo", None)
        self.__uma_ApplicableMetaClassInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_Kind6"):
                opp_val = getattr(old_value, "uma_Kind6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_Kind6"):
                opp_val = getattr(value, "uma_Kind6", None)
                if opp_val is None:
                    setattr(value, "uma_Kind6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ContentElement:

    pass
class uma_Task(WorkDefinition, ContentElement):

    pass
class uma_Guidance(ContentElement):

    pass
class uma_ContentCategory(ContentElement):

    pass
class uma_WorkProduct(FulfillableElement, ContentElement):

    pass
class uma_Role(FulfillableElement, ContentElement):

    pass
class uma_Kind(ContentElement):

    pass
class Namespace:

    pass
class uma_Element(ABC):

    pass
class Element:

    pass
class uma_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class uma_Namespace(NamedElement):

    pass
class uma_PackageableElement(NamedElement):

    pass
class PackageableElement:

    pass
class uma_Package(Namespace, PackageableElement):

    pass
class uma_MethodElement(PackageableElement):

    def __init__(self, guid: str, presentationName: str, briefDescription: str, suppressed: str, orderingGuide: str, uma_MethodElement: set["uma_Constraint"] = None, uma_MethodElement2: set["uma_MethodElementProperty"] = None, uma_MethodElement4: set["uma_Kind"] = None, uma_MethodElement314: "uma_UMASemanticModelBridge" = None):
        self.guid = guid
        self.presentationName = presentationName
        self.briefDescription = briefDescription
        self.suppressed = suppressed
        self.orderingGuide = orderingGuide
        self.uma_MethodElement = uma_MethodElement if uma_MethodElement is not None else set()
        self.uma_MethodElement2 = uma_MethodElement2 if uma_MethodElement2 is not None else set()
        self.uma_MethodElement4 = uma_MethodElement4 if uma_MethodElement4 is not None else set()
        self.uma_MethodElement314 = uma_MethodElement314
        
    @property
    def suppressed(self) -> str:
        return self.__suppressed

    @suppressed.setter
    def suppressed(self, suppressed: str):
        self.__suppressed = suppressed

    @property
    def presentationName(self) -> str:
        return self.__presentationName

    @presentationName.setter
    def presentationName(self, presentationName: str):
        self.__presentationName = presentationName

    @property
    def guid(self) -> str:
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid

    @property
    def orderingGuide(self) -> str:
        return self.__orderingGuide

    @orderingGuide.setter
    def orderingGuide(self, orderingGuide: str):
        self.__orderingGuide = orderingGuide

    @property
    def briefDescription(self) -> str:
        return self.__briefDescription

    @briefDescription.setter
    def briefDescription(self, briefDescription: str):
        self.__briefDescription = briefDescription

    @property
    def uma_MethodElement(self):
        return self.__uma_MethodElement

    @uma_MethodElement.setter
    def uma_MethodElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElement__uma_MethodElement", None)
        self.__uma_MethodElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Constraint"):
                    opp_val = getattr(item, "uma_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Constraint"):
                    opp_val = getattr(item, "uma_Constraint", None)
                    
                    setattr(item, "uma_Constraint", self)
                    

    @property
    def uma_MethodElement2(self):
        return self.__uma_MethodElement2

    @uma_MethodElement2.setter
    def uma_MethodElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElement__uma_MethodElement2", None)
        self.__uma_MethodElement2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_MethodElementProperty"):
                    opp_val = getattr(item, "uma_MethodElementProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_MethodElementProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_MethodElementProperty"):
                    opp_val = getattr(item, "uma_MethodElementProperty", None)
                    
                    setattr(item, "uma_MethodElementProperty", self)
                    

    @property
    def uma_MethodElement314(self):
        return self.__uma_MethodElement314

    @uma_MethodElement314.setter
    def uma_MethodElement314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElement__uma_MethodElement314", None)
        self.__uma_MethodElement314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_UMASemanticModelBridge"):
                opp_val = getattr(old_value, "uma_UMASemanticModelBridge", None)
                if opp_val == self:
                    setattr(old_value, "uma_UMASemanticModelBridge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_UMASemanticModelBridge"):
                opp_val = getattr(value, "uma_UMASemanticModelBridge", None)
                setattr(value, "uma_UMASemanticModelBridge", self)

    @property
    def uma_MethodElement4(self):
        return self.__uma_MethodElement4

    @uma_MethodElement4.setter
    def uma_MethodElement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElement__uma_MethodElement4", None)
        self.__uma_MethodElement4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uma_Kind"):
                    opp_val = getattr(item, "uma_Kind", None)
                    
                    if opp_val == self:
                        setattr(item, "uma_Kind", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uma_Kind"):
                    opp_val = getattr(item, "uma_Kind", None)
                    
                    setattr(item, "uma_Kind", self)
                    

class uma_MethodElementProperty(PackageableElement):

    def __init__(self, value: str, uma_MethodElementProperty: "uma_MethodElement" = None):
        self.value = value
        self.uma_MethodElementProperty = uma_MethodElementProperty
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def uma_MethodElementProperty(self):
        return self.__uma_MethodElementProperty

    @uma_MethodElementProperty.setter
    def uma_MethodElementProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uma_MethodElementProperty__uma_MethodElementProperty", None)
        self.__uma_MethodElementProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uma_MethodElement2"):
                opp_val = getattr(old_value, "uma_MethodElement2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uma_MethodElement2"):
                opp_val = getattr(value, "uma_MethodElement2", None)
                if opp_val is None:
                    setattr(value, "uma_MethodElement2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uma_Type(PackageableElement):

    pass
class Type:

    pass
class uma_Classifier(Type):

    def __init__(self, isAbstract: str):
        self.isAbstract = isAbstract
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract
